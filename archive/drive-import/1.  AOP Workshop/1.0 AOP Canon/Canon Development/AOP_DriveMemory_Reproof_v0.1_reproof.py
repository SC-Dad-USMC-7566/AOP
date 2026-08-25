#!/usr/bin/env python3
"""
Independent re-proof: does sigma > 0 imply E > 0?

Order: TASK_FRESH_AOP_DriveMemory_Reproof_20260725
Deliverable: AOP_DriveMemory_Reproof_v0.1.md

All quantities in NATS.  Discrete time throughout.

DEFINITIONS USED (stated so the code is auditable):

  E     = I(past ; future), contiguous split, present in the past:
          E = I(X_{<=0} ; X_{>=1}).
          For a stationary Markov chain this equals I(X_0 ; X_1) exactly
          (past _|_ future | X_0).

  E_gap = I(X_{<=-1} ; X_{>=1}) -- the "excluded present" variant.
          Reported separately; AOP v1.26 does not state which split it means.

  sigma = lim_n (1/n) D( P(x_1..x_n) || Ptilde(x_1..x_n) )
          Convention A ("plain"):  Ptilde(x_1..x_n) = P(x_n, ..., x_1)
          Convention B ("parity"): Ptilde(x_1..x_n) = P(e.x_n, ..., e.x_1)
                                   e = declared involution (odd vars flip)

  Markov closed form, derived in the report (transition-ratio form):
          sigma = sum_ij pi_i P_ij ln( P_ij / P_{e(j),e(i)} )
  With e = identity this reduces to sum_ij pi_i P_ij ln(P_ij/P_ji), and (in
  stationarity) equals the flux form sum_ij f_ij ln(f_ij/f_ji).
  EVERY closed form below is cross-checked against brute-force path KL.
"""

import itertools
import numpy as np
from math import log
from scipy.optimize import brentq
import mpmath as mp

mp.mp.dps = 60
banner = lambda t: print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


# ---------------------------------------------------------------- utilities
def stationary(P):
    w, v = np.linalg.eig(P.T)
    i = int(np.argmin(np.abs(w - 1.0)))
    pi = np.real(v[:, i])
    pi = np.clip(pi / pi.sum(), 0.0, None)
    return pi / pi.sum()


def sigma_markov(P, pi=None, eps=None):
    """Transition-ratio form.  eps=None -> Convention A.  inf if not a.c."""
    if pi is None:
        pi = stationary(P)
    n = P.shape[0]
    if eps is None:
        eps = np.arange(n)
    s = 0.0
    for i in range(n):
        for j in range(n):
            f = pi[i] * P[i, j]
            if f <= 0:
                continue
            r = P[eps[j], eps[i]]
            if r <= 0:
                return np.inf
            s += f * log(P[i, j] / r)
    return s


def sigma_flux_form(P, pi=None):
    """sum_ij f_ij ln(f_ij/f_ji), f_ij = pi_i P_ij.  Convention A only."""
    if pi is None:
        pi = stationary(P)
    n = P.shape[0]
    s = 0.0
    for i in range(n):
        for j in range(n):
            f, r = pi[i] * P[i, j], pi[j] * P[j, i]
            if f <= 0:
                continue
            if r <= 0:
                return np.inf
            s += f * log(f / r)
    return s


def excess_entropy_markov(P, pi=None):
    """E = I(X_0 ; X_1), nats."""
    if pi is None:
        pi = stationary(P)
    n = P.shape[0]
    E = 0.0
    for i in range(n):
        for j in range(n):
            p = pi[i] * P[i, j]
            if p > 0:
                E += p * log(p / (pi[i] * pi[j]))
    return E


def path_dist_markov(P, pi, n):
    k = P.shape[0]
    d = {}
    for path in itertools.product(range(k), repeat=n):
        p = pi[path[0]]
        for a, b in zip(path, path[1:]):
            p *= P[a, b]
        if p > 0:
            d[path] = p
    return d


def reverse_dist(d, eps=None):
    out = {}
    for path, p in d.items():
        rp = tuple(reversed(path)) if eps is None else tuple(eps[x] for x in reversed(path))
        out[rp] = out.get(rp, 0.0) + p
    return out


def kl_paths(fwd, rev):
    s = 0.0
    for path, p in fwd.items():
        q = rev.get(path, 0.0)
        if q <= 0:
            return np.inf
        s += p * log(p / q)
    return s


def sigma_bruteforce(P, pi, nmax=10, eps=None):
    out = []
    for n in range(2, nmax + 1):
        fwd = path_dist_markov(P, pi, n)
        d = kl_paths(fwd, reverse_dist(fwd, eps=eps))
        out.append((n, d, d / n))
    return out


def mutual_info_blocks(joint):
    pa, pb = {}, {}
    for (a, b), p in joint.items():
        pa[a] = pa.get(a, 0.0) + p
        pb[b] = pb.get(b, 0.0) + p
    return sum(p * log(p / (pa[a] * pb[b])) for (a, b), p in joint.items() if p > 0)


# ============================================================================
banner("PART 0.  Sanity -- transition-ratio form == flux form in stationarity")
rng = np.random.default_rng(20260726)
for t in range(5):
    A = rng.random((4, 4)) + 0.05
    P = A / A.sum(axis=1, keepdims=True)
    pi = stationary(P)
    a, b = sigma_markov(P, pi), sigma_flux_form(P, pi)
    print(f"  trial {t}: ratio {a:.12f}  flux {b:.12f}  diff {abs(a-b):.2e}")


# ============================================================================
banner("PART 1.  Positive control -- driven ring on Z_4, position coordinates")
def ring(N, p):
    P = np.zeros((N, N))
    for i in range(N):
        P[i, (i + 1) % N] = p
        P[i, (i - 1) % N] = 1.0 - p
    return P

N, p = 4, 0.8
P = ring(N, p); pi = stationary(P)
sig_ring = sigma_markov(P, pi)
E_ring = excess_entropy_markov(P, pi)
print(f"  N={N}, p={p}, q={1-p:.1f};  pi = {pi}")
print(f"  sigma computed        = {sig_ring:.12f} nats/step")
print(f"  sigma (p-q)ln(p/q)    = {(2*p-1)*log(p/(1-p)):.12f}")
print(f"  E = I(X0;X1)          = {E_ring:.12f} nats")
print(f"  E = lnN - H(p,q)      = {log(N)+p*log(p)+(1-p)*log(1-p):.12f}")
print("  brute-force path KL (Convention A):  D_n should equal (n-1)*sigma")
for n, d, r in sigma_bruteforce(P, pi, nmax=11):
    print(f"    n={n:2d}  D_n={d:.10f}  D_n/(n-1)={d/(n-1):.12f}  D_n/n={r:.10f}")
print("  -> sigma > 0 and E > 0.  Theorem holds here (canon Figure DM).")


# ============================================================================
banner("PART 2.  COUNTEREXAMPLE 1 -- odd variables (Convention B)\n"
       "         i.i.d. velocity: E = 0 exactly, sigma > 0.")
# {+1,-1} read as a VELOCITY (odd under time reversal); eps swaps them.
print(f"  {'P(v=+1)':>8} {'E':>12} {'sigma_A':>16} {'sigma_B':>16} {'closed form':>16}")
for pv in (0.5, 0.7, 0.8, 0.9, 0.99):
    Q = np.array([[pv, 1 - pv], [pv, 1 - pv]])
    piQ = np.array([pv, 1 - pv]); epsQ = np.array([1, 0])
    closed = 0.0 if pv == 0.5 else (2*pv - 1) * log(pv / (1 - pv))
    print(f"  {pv:8.2f} {excess_entropy_markov(Q,piQ):12.3e} "
          f"{sigma_markov(Q,piQ):16.12f} {sigma_markov(Q,piQ,eps=epsQ):16.12f} {closed:16.12f}")

pv = 0.7
Q = np.array([[pv, 1-pv], [pv, 1-pv]]); piQ = np.array([pv, 1-pv]); epsQ = np.array([1, 0])
print("\n  brute-force path KL, Convention B, pv=0.7 (exact, every n):")
for n, d, r in sigma_bruteforce(Q, piQ, nmax=12, eps=epsQ):
    print(f"    n={n:2d}  D_n={d:.10f}  D_n/n={r:.12f}")
print("  brute-force, Convention A, same process (identically zero):")
for n, d, r in sigma_bruteforce(Q, piQ, nmax=8):
    print(f"    n={n:2d}  D_n={d:.3e}  D_n/n={r:.3e}")
print("\n  VERDICT: stationary, E = 0 exactly, sigma_B = 0.3389191442 nats/step.")
print("  Canon scope condition 3 correctly excludes it: the one-point law")
print("  (0.7,0.3) is NOT invariant under the involution.")


# ============================================================================
banner("PART 3.  The increment representation of the SAME driven ring.\n"
       "         sigma preserved EXACTLY; E collapses to 0.")
p = 0.8
Y = np.array([[p, 1-p], [p, 1-p]]); piY = np.array([p, 1-p]); epsY = np.array([1, 0])
sYA, sYB = sigma_markov(Y, piY), sigma_markov(Y, piY, eps=epsY)
EY = excess_entropy_markov(Y, piY)
print(f"  Y_t = X_t - X_{{t-1}} mod 4, read as +-1 (an increment IS an odd variable)")
print(f"    position  repr:  sigma = {sig_ring:.12f}   E = {E_ring:.12f}")
print(f"    increment repr:  sigma_A = {sYA:.12f}  sigma_B = {sYB:.12f}  E = {EY:.3e}")
print(f"    sigma_B(increments) - sigma(positions) = {sYB - sig_ring:.3e}")
assert abs(sYB - sig_ring) < 1e-12
print("  -> EXACTLY EQUAL.  A reduction that preserves the physical EPR while")
print("     sending E to zero.  Canon Fig. DM(b) exhibits coarse-grainings where")
print("     sigma and E collapse TOGETHER; this one does not.  Scope conditions 1")
print("     and 3 are therefore not independent.")


# ============================================================================
banner("PART 4.  COUNTEREXAMPLE 2 -- the excluded-present split (E_gap).\n"
       "         Canon states no split convention.")
qU = 0.5
states = [(0,0),(0,1),(1,0),(1,1)]; idx = {s:i for i,s in enumerate(states)}
Ppair = np.zeros((4,4))
for (u,v) in states:
    for w in (0,1):
        Ppair[idx[(u,v)], idx[(v,w)]] += (qU if w==1 else 1-qU)
piP = stationary(Ppair)
print(f"  X_t = (U_t, U_{{t+1}}), U i.i.d. Bern({qU}).  pi = {piP}")
print(f"  E (contiguous) = I(X0;X1) = {excess_entropy_markov(Ppair,piP):.12f}  > 0")
for L in (1,2,3):
    joint = {}
    for path in itertools.product(range(4), repeat=2*L+1):
        pr = piP[path[0]]
        for a,b in zip(path, path[1:]):
            pr *= Ppair[a,b]
        if pr > 0:
            k = (path[:L], path[L+1:])
            joint[k] = joint.get(k, 0.0) + pr
    print(f"    E_gap at block length L={L}: {mutual_info_blocks(joint):.3e}")
print(f"  sigma (Convention A) = {sigma_markov(Ppair,piP)}")
print("  -> +inf: the reverse of edge (u,v)->(v,w) exists only if w=u, so the")
print("     forward path measure is not absolutely continuous w.r.t. its reverse.")
print("  Under the excluded-present split: sigma > 0, E_gap = 0.  FALSE as stated.")


banner("PART 4b.  Finite-sigma version of the excluded-present counterexample")
def obs_path_law(phi, q, n):
    """X_t = phi(U_t,U_{t+1}), t=0..n-1;  U i.i.d. Bern(q)."""
    law = {}
    for u in itertools.product((0,1), repeat=n+1):
        pr = 1.0
        for x in u:
            pr *= q if x == 1 else 1-q
        if pr <= 0:
            continue
        obs = tuple(phi[2*u[t] + u[t+1]] for t in range(n))
        law[obs] = law.get(obs, 0.0) + pr
    return law

best, n = None, 10
for q in (0.5, 0.4, 0.3, 0.25, 0.2, 0.1):
    for phi in itertools.product(range(3), repeat=4):
        fwd = obs_path_law(phi, q, n)
        d = kl_paths(fwd, reverse_dist(fwd))
        if np.isfinite(d) and d > 1e-9:
            if best is None or d/n > best[0]:
                best = (d/n, q, phi, d)
if best:
    r, q, phi, d = best
    print(f"  found: U ~ Bern({q}),  phi(u,v) indexed by 2u+v = {phi}")
    print(f"         D_n/n at n={n}:  {r:.10f} nats/step   (finite, > 0)")
    for nn in (6,8,10,12):
        fwd = obs_path_law(phi, q, nn)
        dd = kl_paths(fwd, reverse_dist(fwd))
        print(f"           n={nn:2d}  D_n={dd:.10f}  D_n/n={dd/nn:.10f}  "
              f"D_n/(n-1)={dd/(nn-1):.10f}")
    print("  E_gap = 0 EXACTLY and structurally: X is 1-dependent, so X_{<=-1} is a")
    print("  function of U_{<=0} and X_{>=1} of U_{>=1}, which are independent.")
else:
    print("  none found in this search class")


# ============================================================================
banner("PART 5.  MAIN RESULT -- the 'memory floor' is not bounded below.\n"
       "  A family satisfying ALL FOUR canon scope conditions with sigma fixed\n"
       "  at 1 nat/step and E -> 0.")
# N states, pi uniform (doubly stochastic).  Base uniform 1/N (i.i.d.).
# Add a circulation of size c on the 3-cycle 0->1->2->0:
#   P[i,i+1] += c, P[i,i+2] -= c  (i mod 3).  Row and column sums preserved.
# Write c = (1-eta)/N, so P[i,i+1] = (2-eta)/N and P[i,i+2] = eta/N.
def cyc(Nst, eta):
    P = np.full((Nst, Nst), 1.0/Nst)
    c = (1.0 - eta)/Nst
    for i in range(3):
        P[i, (i+1) % 3] += c
        P[i, (i+2) % 3] -= c
    return P

def cf_sigma(Nst, L):
    """closed form with eta = exp(-L), arbitrary precision"""
    eta = mp.e**(-mp.mpf(L))
    return (6*(1-eta)/mp.mpf(Nst)**2) * mp.log((2-eta)/eta)

def cf_E(Nst, L):
    eta = mp.e**(-mp.mpf(L))
    return (3/mp.mpf(Nst)**2) * ((2-eta)*mp.log(2-eta) + eta*mp.log(eta))

print("  (a) closed forms vs direct computation (double precision regime):")
print(f"  {'N':>5} {'eta':>10} {'sigma direct':>16} {'sigma closed':>16} "
      f"{'E direct':>14} {'E closed':>14} {'pi unif':>8}")
for (Nst, L) in [(6,1.2),(10,6.9),(25,18.4),(60,120.0),(78,600.0)]:
    eta = float(mp.e**(-mp.mpf(L)))
    P = cyc(Nst, eta); pi = stationary(P)
    print(f"  {Nst:5d} {eta:10.2e} {sigma_markov(P,pi):16.10f} "
          f"{float(cf_sigma(Nst,L)):16.10f} {excess_entropy_markov(P,pi):14.6e} "
          f"{float(cf_E(Nst,L)):14.6e} {str(np.allclose(pi,1/Nst)):>8}")

print("\n  (b) brute-force path-KL check on one member (N=6, eta=0.3):")
P6 = cyc(6, 0.3); pi6 = stationary(P6)
print(f"      closed-form sigma = {float(cf_sigma(6, -log(0.3))):.12f}")
for n, d, r in sigma_bruteforce(P6, pi6, nmax=8):
    print(f"      n={n}  D_n={d:.10f}  D_n/(n-1)={d/(n-1):.12f}")

print("\n  (c) hold sigma = 1.000000000 nat/step exactly; drive E down.")
print(f"  {'L=-ln(eta)':>12} {'N':>6} {'sigma':>18} {'E (nats)':>16} {'sigma/E':>14}")
rows = []
for L0 in (5, 10, 25, 50, 100, 250, 500, 1000, 2500, 10000, 100000):
    Nreal = float(mp.sqrt(6*(L0 + mp.log(2))))
    Nst = max(6, int(round(Nreal)))
    g = lambda LL: float(cf_sigma(Nst, LL) - 1)
    try:
        Lstar = brentq(g, 1e-6, 1e7, xtol=1e-12, rtol=1e-15, maxiter=500)
    except ValueError:
        continue
    s, e = cf_sigma(Nst, Lstar), cf_E(Nst, Lstar)
    rows.append((Lstar, Nst, float(s), float(e)))
    print(f"  {Lstar:12.4g} {Nst:6d} {float(s):18.12f} {float(e):16.9e} {float(s/e):14.2f}")

print("\n  (d) double-precision confirmation for the members with eta > 1e-308:")
for (Lstar, Nst, s, e) in rows:
    eta = float(mp.e**(-mp.mpf(Lstar)))
    if eta < 1e-300:
        continue
    P = cyc(Nst, eta); pi = stationary(P)
    print(f"      N={Nst:4d}  sigma_direct={sigma_markov(P,pi):.12f}  "
          f"E_direct={excess_entropy_markov(P,pi):.9e}  (closed: {e:.9e})")

print("\n  Asymptotics (eta -> 0, sigma held at s):  E -> s * ln2 / (L + ln2) -> 0.")
print("  Hence  inf { E : sigma >= s } = 0  for every s > 0.")
print("  Every member is stationary, doubly stochastic, single complete")
print("  description, configuration-space (all state variables even).")
print("  It satisfies all four canon scope conditions -- and E is unbounded below.")


# ============================================================================
banner("PART 6.  Lemma check: E = 0 <=> i.i.d. (contiguous split)")
rng = np.random.default_rng(7)
for t in range(4):
    A = rng.random((4,4)) + 0.02
    P = A/A.sum(axis=1, keepdims=True); pi = stationary(P)
    print(f"    random trial {t}: E={excess_entropy_markov(P,pi):.6e}  "
          f"max|P_ij - pi_j|={np.abs(P - pi[None,:]).max():.6e}")
Piid = np.tile(np.array([0.1,0.2,0.3,0.4]), (4,1)); pii = stationary(Piid)
print(f"    i.i.d. chain:     E={excess_entropy_markov(Piid,pii):.3e}  "
      f"sigma_A={sigma_markov(Piid,pii):.3e}")
print("\nDONE.")
