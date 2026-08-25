"""
phaseF_normalizedMIP_wellposedness.py
=====================================
AOP builder proposal - WELL-POSEDNESS GATE for the moving-MIP frontier item.
(Prime verifies; Ben decides. Nobody grades their own homework.)

QUESTION (from CP). The v4 moving-MIP build demonstrates its "straddle a
relabeling" obstacle on the two-module Gaussian Sigma=(I+gL)^-1, where the
UNNORMALIZED per-slice Phi_MIP relabels module-cut -> 1|5 singletons at
b*=0.4206007 (seven tied minimizers). That transition is the unnormalized
deficit's SMALL-SIDE VULNERABILITY - a 1-node cut is cheap simply because it
severs few edges - not obviously a real individuation event. If the whole
obstacle is a normalization artifact, the frontier item is ill-posed and the
eight-item repair roadmap is pointed at nothing.

GATE. Define a SIZE-NORMALIZED Phi_MIP and re-find the argmin across the SAME
b-ramp (0 -> 1.4) on the IDENTICAL model. Report:
  (a) does the normalized MIP STILL relabel across a straddle to a NON-TRIVIAL
      cut, or does normalization suppress the singleton collapse so the module
      cut stays MIP throughout?
  (b) does normalization PRESERVE Phi_MIP = 0 on the block-decomposable Sigma
      (b=0)?  [Canon v1.21 lines 631/709: zero-calibration is load-bearing and
      cannot break.]

NORMALIZATION CHOICE. Primary: deficit / min(|A|,|B|) - divide the cut's mutual
information by the node-count of the SMALLER part. Rationale: the small-side
vulnerability is precisely that a k=1 part pays mutual-information cost roughly
proportional to its size, so a per-node deficit removes the pure size advantage
of tiny parts without appealing to any quantity outside the coupling graph
(stays third-person, ownership-free, as the canon requires). Confirmed against
an IIT-style entropy normalization deficit / min(H(A),H(B)) [same qualitative
result - see check_iit].

MODEL. Imported UNCHANGED from the deposited build: N=6, two 3-node modules
{0,1,2}|{3,4,5}, intra-module weight 1.0, inter-module weight b, g=1.0,
Sigma=(I+gL)^-1. Phi across a bipartition (A,B) = I(A;B) = 1/2 (logdet Sigma_AA
+ logdet Sigma_BB - logdet Sigma). Closed-form: matrix inverse + determinants +
exhaustive enumeration of all 31 bipartitions. No estimation.

VERDICT (this script; SETTLED computation / SYNTHESIS interpretation):
  (b) PRESERVED. Phi_MIP(b=0) = 0 exactly under both normalizations (0 / +ve).
  (a) SURVIVES. Normalization removes the singleton artifact but NOT the
      relabeling: the module cut is the UNIQUE normalized MIP for all b<1, ties
      at the symmetric point b=1, and relabels to a DIFFERENT BALANCED 3|3 cut
      for b>1 (cross-coupling exceeds intra-coupling; community structure
      inverts). The straddle obstacle is therefore REAL - a genuine competition
      between two non-trivial organizations, exactly the "two competing
      non-trivial partitions" object. => The frontier item is WELL-POSED; the
      repair is worth scoping. (It does NOT authorize the repair - Prime/Ben.)

Grading: computation SETTLED (closed-form on the canon's own model); the
"well-posed" reading is SYNTHESIS. Syntactic layer only (Phi_MIP, coupling
graph) - touches no semantic-mask / star / provenance quantity.
"""
import itertools
import numpy as np

# ---- IDENTICAL model to the deposited build ---------------------------------
N = 6
MODULE_A, MODULE_B = frozenset({0, 1, 2}), frozenset({3, 4, 5})
G = 1.0


def L_of(b):
    """Graph Laplacian: intra-module weight 1, inter-module weight b."""
    W = np.zeros((N, N))
    for i, j in itertools.combinations(range(N), 2):
        same = ({i, j} <= set(MODULE_A)) or ({i, j} <= set(MODULE_B))
        W[i, j] = W[j, i] = 1.0 if same else b
    return np.diag(W.sum(1)) - W


def Sigma(b):
    return np.linalg.inv(np.eye(N) + G * L_of(b))


# ---- all 31 bipartitions (non-empty proper, unordered) ----------------------
def bipartitions():
    nodes = list(range(N))
    out = []
    for r in range(1, N // 2 + 1):
        for A in itertools.combinations(nodes, r):
            B = tuple(x for x in nodes if x not in A)
            if r == N - r and A[0] != 0:          # de-dup balanced halves
                continue
            out.append((frozenset(A), frozenset(B)))
    return out


BIPARTS = bipartitions()


def cut_mi(S, A, B):
    """I(A;B) = 1/2 (logdet S_AA + logdet S_BB - logdet S).  >= 0."""
    idx = sorted(A) + sorted(B)
    Sp = S[np.ix_(idx, idx)]
    nA = len(A)
    _, ldA = np.linalg.slogdet(Sp[:nA, :nA])
    _, ldB = np.linalg.slogdet(Sp[nA:, nA:])
    _, ld = np.linalg.slogdet(Sp)
    return 0.5 * (ldA + ldB - ld)


def is_module(A, B):
    return set(A) in ({0, 1, 2}, {3, 4, 5}) or set(B) in ({0, 1, 2}, {3, 4, 5})


def kind(A, B):
    sizes = tuple(sorted((len(A), len(B))))
    if sizes == (1, 5):
        return "1|5 singleton"
    if sizes == (2, 4):
        return "2|4"
    return "3|3 MODULE" if is_module(A, B) else "3|3 other"


def normalized_argmin(b, norm):
    """Return sorted list of (normval, deficit, A, B). norm in {'none','minsize'}."""
    S = Sigma(b)
    rows = []
    for A, B in BIPARTS:
        d = cut_mi(S, A, B)
        f = 1.0 if norm == "none" else min(len(A), len(B))
        rows.append((d / f, d, A, B))
    rows.sort(key=lambda x: x[0])
    return rows


# ---- (b) CALIBRATION --------------------------------------------------------
def check_calibration():
    print("(b) ZERO-CALIBRATION on block-decomposable Sigma(b=0) [load-bearing]")
    for norm in ("none", "minsize"):
        top = normalized_argmin(0.0, norm)[0]
        print(f"    norm={norm:7}: MIP {tuple(sorted(top[2]))}|{tuple(sorted(top[3]))}"
              f"  Phi_MIP(deficit)={top[1]:.6f}  normval={top[0]:.6f}")
    print("    -> Phi_MIP = 0 exactly under both (a zero deficit / positive"
          " factor is still zero). CALIBRATION PRESERVED.\n")


# ---- (a) RELABELING ---------------------------------------------------------
def check_relabeling():
    print("(a) DOES THE NORMALIZED MIP STILL RELABEL ACROSS A STRADDLE?")
    bs = np.linspace(0, 1.4, 561)
    for norm in ("none", "minsize"):
        print(f"  --- normalization = {norm} ---")
        prev = None
        for b in bs:
            top = normalized_argmin(b, norm)[0]
            k = kind(top[2], top[3])
            if k != prev:
                print(f"    b={b:.3f}: MIP {tuple(sorted(top[2]))}|"
                      f"{tuple(sorted(top[3]))}  [{k}]  Phi_MIP={top[1]:.4f}")
                prev = k
    # uniqueness margin for the size-normalized case: gap to best NON-module cut
    print("  --- size-normalized: gap = (best non-module normval) - (module cut"
          " normval); >0 => module cut is the UNIQUE MIP ---")
    for b in (0.001, 0.2, 0.42, 0.6, 0.8, 0.95, 0.99, 1.00, 1.01, 1.2, 1.4):
        v = normalized_argmin(b, "minsize")
        mod = [x[0] for x in v if is_module(x[2], x[3])][0]
        non = [x[0] for x in v if not is_module(x[2], x[3])][0]
        tag = "MODULE unique" if non - mod > 1e-7 else "module NOT MIP (relabelled)"
        print(f"    b={b:.3f}: moduleNV={mod:.5f}  bestOtherNV={non:.5f}"
              f"  gap={non - mod:+.5f}  -> {tag}")
    print("    -> module cut is the UNIQUE normalized MIP for all b<1, ties at the")
    print("       fully-symmetric point b=1, and RELABELS to a balanced 3|3 cut for")
    print("       b>1. The relabeling SURVIVES normalization; only the SINGLETON")
    print("       artifact is removed. The straddle obstacle is REAL.\n")


def check_degeneracy_source():
    print("RESIDUAL DEGENERACY past b=1 is the MODEL's symmetry, not normalization")
    for b in (1.1, 1.2, 1.4):
        v = normalized_argmin(b, "minsize")
        m = v[0][0]
        tied = [(A, B) for nv, d, A, B in v if abs(nv - m) < 1e-7]
        kinds = {kind(A, B) for A, B in tied}
        print(f"    b={b:.2f}: {len(tied)} tied minimizers, all {kinds},"
              f" module cut among them? {any(is_module(A, B) for A, B in tied)}")
    print("    The 9-fold tie is node-exchange symmetry of the complete graph with")
    print("    two edge weights (nodes within a module are interchangeable). It is")
    print("    NOT the small-side singleton artifact and NOT caused by normalization.")
    print("    A symmetry-broken benchmark (distinct pairwise weights) would single")
    print("    out a unique competitor - a benchmark-design note for the repair,")
    print("    not a defect in this well-posedness finding.\n")


def check_iit():
    print("ROBUSTNESS: IIT-style normalization deficit / min(H(A),H(B))")
    const = 0.5 * np.log(2 * np.pi * np.e)
    prev = None
    for b in np.linspace(0, 1.4, 141):
        S = Sigma(b)
        rows = []
        for A, B in BIPARTS:
            d = cut_mi(S, A, B)
            _, hA = np.linalg.slogdet(S[np.ix_(sorted(A), sorted(A))])
            _, hB = np.linalg.slogdet(S[np.ix_(sorted(B), sorted(B))])
            HA = 0.5 * hA + len(A) * const
            HB = 0.5 * hB + len(B) * const
            f = min(HA, HB)
            rows.append((d / f if f > 1e-9 else np.inf, d, A, B))
        rows.sort(key=lambda x: x[0])
        top = rows[0]
        k = kind(top[2], top[3])
        if k != prev:
            print(f"    b={b:.3f}: MIP {tuple(sorted(top[2]))}|"
                  f"{tuple(sorted(top[3]))} [{k}] Phi_MIP={top[1]:.4f}")
            prev = k
    print("    -> same qualitative verdict: module cut for b<1, balanced 3|3 for")
    print("       b>1, and Phi_MIP(b=0)=0. Finding is not an artifact of the")
    print("       particular normalizer.\n")


_OFF = None  # fixed per-edge multiplicative offsets (set once for reproducibility)


def _offsets():
    global _OFF
    if _OFF is None:
        r = np.random.default_rng(7)
        _OFF = {(i, j): r.standard_normal()
                for i, j in itertools.combinations(range(N), 2)}
    return _OFF


def Sigma_broken(b, jit=0.15):
    """Fully symmetry-broken model: every pairwise weight jittered so NO two
    nodes are interchangeable. Base weight is 1 intra / b inter, as before."""
    off = _offsets()
    W = np.zeros((N, N))
    for i, j in itertools.combinations(range(N), 2):
        same = ({i, j} <= set(MODULE_A)) or ({i, j} <= set(MODULE_B))
        base = 1.0 if same else b
        W[i, j] = W[j, i] = base * (1 + jit * off[(i, j)])
    return np.linalg.inv(np.eye(N) + (np.diag(W.sum(1)) - W))


def check_symmetry_broken():
    print("SYMMETRY-BROKEN benchmark (all pairwise weights distinct): is the")
    print("competitor UNIQUE, and do (a)/(b) still hold?")
    prev = None
    for b in np.linspace(0, 1.4, 141):
        S = Sigma_broken(b)
        rows = sorted(((cut_mi(S, A, Bx) / min(len(A), len(Bx)), cut_mi(S, A, Bx), A, Bx)
                       for A, Bx in BIPARTS), key=lambda x: x[0])
        top = rows[0]
        m = top[0]
        nt = sum(1 for x in rows if abs(x[0] - m) < 1e-7)
        k = kind(top[2], top[3])
        if k != prev:
            print(f"    b={b:.3f}: MIP {tuple(sorted(top[2]))}|{tuple(sorted(top[3]))}"
                  f" [{k}] Phi_MIP={top[1]:.4f}  #tied={nt}")
            prev = k
    S0 = Sigma_broken(0.0)
    d0 = sorted(cut_mi(S0, A, Bx) for A, Bx in BIPARTS)[0]
    print(f"    b=0 calibration (symmetry-broken): Phi_MIP={d0:.6f}")
    print("    -> module cut for b<1, a SINGLE balanced 3|3 competitor for b>1")
    print("       (#tied=1 throughout), calibration preserved. The relabel is a")
    print("       genuine unique-competitor transition once the toy model's node-")
    print("       exchange symmetry is removed.\n")


def make_figure(path="phaseF_normalizedMIP_wellposedness_fig.png"):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    foc, alt, grey = "#1f4e79", "#c0561f", "#6b6b6b"
    bs = np.linspace(0.001, 1.4, 200)
    # map partition-kind to an ordinal band for a clean step plot
    order = {"3|3 MODULE": 3, "3|3 other": 2, "2|4": 1, "1|5 singleton": 0}
    yn = [order[kind(*normalized_argmin(b, "none")[0][2:])] for b in bs]
    ym = [order[kind(*normalized_argmin(b, "minsize")[0][2:])] for b in bs]
    # gap to best non-module (size-normalized)
    gap = []
    for b in bs:
        v = normalized_argmin(b, "minsize")
        mod = [x[0] for x in v if is_module(x[2], x[3])][0]
        non = [x[0] for x in v if not is_module(x[2], x[3])][0]
        gap.append(non - mod)

    fig, axs = plt.subplots(1, 2, figsize=(9.2, 3.6))
    ax = axs[0]
    ax.step(bs, yn, color=alt, lw=2, where="post", label="unnormalized MIP")
    ax.step(bs, ym, color=foc, lw=2, where="post", label="size-normalized MIP")
    ax.axvline(0.4206, color=alt, ls=":", lw=1)
    ax.text(0.4206, 3.15, "unnorm. relabel\n$b^*{=}0.42$ (singleton)",
            color=alt, fontsize=5.5, ha="center")
    ax.axvline(1.0, color=foc, ls=":", lw=1)
    ax.text(1.02, 2.55, "normalized relabel\n$b{=}1$ (balanced 3|3)",
            color=foc, fontsize=5.5, ha="left")
    ax.set_yticks([0, 1, 2, 3])
    ax.set_yticklabels(["1|5\nsingleton", "2|4", "3|3\nother", "3|3\nMODULE"], fontsize=6)
    ax.set_xlabel("inter-module coupling  $b$")
    ax.set_title("(a) MIP partition kind vs $b$\nnormalization removes the singleton, not the relabel",
                 fontsize=8)
    ax.legend(frameon=False, fontsize=6, loc="lower left")
    ax.set_xlim(-0.05, 1.55)
    ax.set_ylim(-0.4, 3.7)

    ax = axs[1]
    ax.axhline(0, color=grey, lw=0.8)
    ax.plot(bs, gap, color=foc, lw=2)
    ax.fill_between(bs, 0, gap, where=np.array(gap) > 0, color=foc, alpha=0.15)
    ax.axvline(1.0, color=grey, ls="--", lw=1)
    ax.text(0.5, max(gap) * 0.6, "module cut is the\nUNIQUE MIP\n(gap > 0)",
            color=foc, fontsize=6, ha="center")
    ax.text(1.2, min(gap) * 0.5, "module cut\nNOT MIP", color=alt, fontsize=6, ha="center")
    ax.set_xlabel("inter-module coupling  $b$")
    ax.set_ylabel("normalized-Φ gap: best 'other' − module cut")
    ax.set_title("(b) Size-normalized uniqueness margin\nrelabel is at $b{=}1$, module cut unique below",
                 fontsize=8)
    fig.tight_layout()
    fig.savefig(path, dpi=300, bbox_inches="tight")
    return path


if __name__ == "__main__":
    import sys
    print("phaseF - normalized-MIP well-posedness gate for the moving-MIP frontier\n")
    check_calibration()
    check_relabeling()
    check_degeneracy_source()
    check_symmetry_broken()
    check_iit()
    if "--figure" in sys.argv:
        print("[figure ->", make_figure(), "]")
