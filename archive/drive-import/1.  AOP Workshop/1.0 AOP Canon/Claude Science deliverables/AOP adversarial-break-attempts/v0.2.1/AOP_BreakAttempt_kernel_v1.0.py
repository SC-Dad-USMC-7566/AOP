"""Helpers for adversarial break attempts on AOP-style intervention protocols.

Exact/analytic computations on the AOP benchmark suite: labelled-transfer-matrix
HMMs (Golden Mean, Even Process), Markov-order projection ladders, entropy
production, and mean first-passage times on driven rings.
All quantities are closed-form or exact on finite state spaces -- nothing sampled.
"""
import re
import math

GOLDEN_MEAN_E_BITS = 0.2516291674
EVEN_PROCESS_ENTROPY_RATE_BITS = 0.6666666666666666
CF2003_EVEN_GAMMA = 0.501


def unescape_drive_markdown(text):
    """Undo the backslash-escaping Google Drive applies when exporting .md.

    Drive's read_file_content returns markdown with #, *, `, _, [, ], -, |, etc.
    backslash-escaped, and hard-wraps with two trailing spaces. Run this before
    reading or diffing any Drive-sourced markdown, or every heading and table
    will be mangled.
    """
    out = re.sub(r'\\([#*`_\[\]\-\\&~<>.|+])', r'\1', text)
    return out.replace("  \n", "\n")


def shannon_bits(probs):
    """Shannon entropy in bits of an iterable of probabilities."""
    total = 0.0
    for p in probs:
        if p > 1e-15:
            total -= p * math.log2(p)
    return total


def hmm_stationary_state(labelled_matrices):
    """Stationary distribution over hidden states for a labelled-matrix HMM."""
    import numpy as np
    T = sum(labelled_matrices)
    w, V = np.linalg.eig(T.T)
    v = np.real(V[:, np.argmin(np.abs(w - 1))])
    return v / v.sum()


def hmm_block_entropies(labelled_matrices, nmax):
    """Exact block entropies H(1..nmax) in bits by enumerating allowed words.

    labelled_matrices[s][i, j] = P(next state j, emit symbol s | state i).
    Word count grows with the process's topological entropy; nmax ~ 24 is
    comfortable for binary sofic processes, nmax ~ 30 is the practical ceiling.
    """
    ps = hmm_stationary_state(labelled_matrices)
    entropies = {0: 0.0}
    current = {(): ps.copy()}
    for n in range(1, nmax + 1):
        nxt = {}
        for word, vec in current.items():
            for s, T in enumerate(labelled_matrices):
                v2 = vec @ T
                if v2.sum() > 1e-18:
                    nxt[word + (s,)] = v2
        current = nxt
        entropies[n] = shannon_bits([v.sum() for v in current.values()])
    return entropies


def markov_ladder(block_entropies, kmax=None):
    """Order-k projection ladder from exact block entropies.

    Returns {'E_Mk', 'increments', 'E_bracket', 'rho_upper'}:
      E(M_k)   = H(k) - k*[H(k+1) - H(k)]  -- excess entropy of the order-k
                 Markov projection, exact at each k (no limit involved).
      rho_k    = E(mu) - E(M_k), the PROJECTION RESIDUAL.
    E(mu) is a limit, so it is BRACKETED from the monotone increments and a
    geometric tail bound rather than extrapolated -- report rho_k as an
    interval, and prefer claims about the increments (exact) over claims about
    rho_k (limit-dependent). A summable increment series proves rho_k -> 0,
    which is the estimator-free way to test a 'ladder never saturates' claim.
    """
    H = block_entropies
    top = max(H) - 1 if kmax is None else min(kmax, max(H) - 1)
    E_Mk = {k: H[k] - k * (H[k + 1] - H[k]) for k in range(0, top)}
    inc = {k: E_Mk[k + 1] - E_Mk[k] for k in range(0, top - 1)}
    last = top - 2
    # Increments alternate by parity on sofic processes, so a consecutive-rung
    # ratio can exceed 1 and is NOT a valid tail bound. Use the TWO-rung ratio;
    # the per-rung factor is its square root.
    window = range(max(2, last - 6), last + 1)
    if all(inc[k] <= 1e-12 for k in window):
        # Already exactly saturated (finite-order source): rho_k == 0 beyond
        # the true order, so there is no tail. Golden Mean does this at k=1.
        r2, tail = 0.0, 0.0
        exact = True
    else:
        ratios = [inc[k] / inc[k - 2] for k in window if inc[k - 2] > 1e-18]
        r2 = max(ratios) if ratios else 0.0
        tail = ((inc[last] + inc[last - 1]) * r2 / (1 - r2)
                if 0 < r2 < 1 else float('inf'))
        exact = False
    lo = E_Mk[top - 1]
    return {"E_Mk": E_Mk, "increments": inc,
            "E_bracket": (lo, lo + tail),
            "rho_upper": {k: lo + tail - E_Mk[k] for k in E_Mk},
            "two_rung_ratio": r2,
            "per_rung_factor": r2 ** 0.5 if r2 > 0 else 0.0,
            "saturated_exactly": exact,
            "summable": exact or 0 < r2 < 1}


def golden_mean_matrices(stay_prob=0.5):
    """Golden Mean process as an order-1 chain on {0,1} (no 00 allowed)."""
    import numpy as np
    q = stay_prob
    return [np.array([[0.0, 0.0], [1 - q, 0.0]]),
            np.array([[0.0, 1.0], [0.0, q]])]


def even_process_matrices(p=0.5):
    """Even Process: sofic, INFINITE Markov order, but finite C_mu.

    Infinite Markov order does NOT imply a non-summable projection residual --
    rho_k here decays as k*2^(-k/2). Crutchfield & Feldman 2003 report the
    matching exponential convergence, gamma = 0.501 +/- 0.007.
    """
    import numpy as np
    return [np.array([[1 - p, 0.0], [0.0, 0.0]]),
            np.array([[0.0, p], [1.0, 0.0]])]


def word_distribution(labelled_matrices, length):
    """Exact distribution over words of the given length."""
    ps = hmm_stationary_state(labelled_matrices)
    current = {(): ps.copy()}
    for _ in range(length):
        nxt = {}
        for word, vec in current.items():
            for s, T in enumerate(labelled_matrices):
                v2 = vec @ T
                if v2.sum() > 1e-16:
                    nxt[word + (s,)] = v2
        current = nxt
    return {w: float(v.sum()) for w, v in current.items()}


def sigma_window_bits(word_dist, delta):
    """Windowed path asymmetry: KL(forward word law || its reversal) per step.

    Requires a DECLARED reversal involution; this uses plain word reversal.
    An unreversed sigma has not said which involution it diverges against.
    """
    total = 0.0
    for w, p in word_dist.items():
        if p <= 1e-15:
            continue
        q = word_dist.get(tuple(reversed(w)), 0.0)
        if q <= 1e-18:
            return float('inf')
        total += p * math.log2(p / q)
    return total / delta


def chain_stationary(P):
    """Stationary distribution of a row-stochastic transition matrix."""
    import numpy as np
    w, V = np.linalg.eig(P.T)
    v = np.real(V[:, np.argmin(np.abs(w - 1))])
    return v / v.sum()


def chain_sigma_bits(P):
    """Exact per-step entropy production (bits) of a Markov chain."""
    pi = chain_stationary(P)
    total = 0.0
    n = len(P)
    for i in range(n):
        for j in range(n):
            f = pi[i] * P[i, j]
            r = pi[j] * P[j, i]
            if f > 1e-15:
                total += f * math.log2(f / r)
    return total


def chain_excess_entropy_bits(P):
    """Excess entropy E = I(past;future) of a first-order Markov chain."""
    pi = chain_stationary(P)
    return shannon_bits(pi) - sum(pi[i] * shannon_bits(P[i]) for i in range(len(P)))


def driven_ring(a, b, n=3):
    """n-state driven ring: rate a forward, b backward, remainder stays.

    Stationary law is UNIFORM for every (a, b) by cyclic symmetry, so the
    detailed-balance projection at fixed pi is exactly a == b. Cycle affinity
    A = n*ln(a/b); sigma > 0 iff A != 0.
    """
    import numpy as np
    P = np.zeros((n, n))
    for i in range(n):
        P[i, (i + 1) % n] = a
        P[i, (i - 1) % n] = b
        P[i, i] = 1.0 - a - b
    return P


def ring_increment_law(a, b):
    """Step law (+1, -1, 0) of a driven ring -- the increment representation.

    THE TRAP: ring increments are i.i.d. (the step law does not depend on
    position), so E == 0 EXACTLY in this representation while sigma is
    preserved. A protocol that puts a driven ring forward as a Drive control
    without fixing state == POSITION lets a runner produce a false refutation
    of sigma>0 => E>0. Always compare against the position representation.
    """
    stay = 1.0 - a - b
    fwd = a * math.log2(a / b) if a > 1e-15 else 0.0
    rev = b * math.log2(b / a) if b > 1e-15 else 0.0
    return {"law": (a, b, stay), "sigma_bits": fwd + rev,
            "excess_entropy_bits": 0.0}


def ring_mfpt(P, start, target):
    """Mean first-passage time from start to target by exact linear solve."""
    import numpy as np
    idx = [i for i in range(len(P)) if i != target]
    A = np.eye(len(idx)) - P[np.ix_(idx, idx)]
    m = np.linalg.solve(A, np.ones(len(idx)))
    return float(m[idx.index(start)])


def two_state_multichannel_sigma(channels):
    """Entropy production of a TWO-state system with several parallel channels.

    channels = [(k_forward, k_reverse), ...]. A two-state chain is
    detailed-balanced only with a SINGLE channel; with two or more independent
    channels it is a genuine NESS with sigma > 0 -- the cycle lives in channel
    space, not state space. Use this to check any 'two-state chains are always
    detailed-balanced' rationale.
    """
    k12 = sum(c[0] for c in channels)
    k21 = sum(c[1] for c in channels)
    p1 = k21 / (k12 + k21)
    p2 = 1.0 - p1
    total = 0.0
    for f, r in channels:
        J = p1 * f - p2 * r
        total += J * math.log((p1 * f) / (p2 * r))
    return total
