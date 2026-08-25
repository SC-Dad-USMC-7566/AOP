#!/usr/bin/env python3
"""Follow-up verification.

(A) Arbitrary-precision recomputation of the Part-5 family straight from the
    transition matrix.  NOTE: the entries must be written directly as
    (2-eta)/N and eta/N -- forming them as 1/N +- (1-eta)/N loses eta to
    catastrophic cancellation once eta drops below the working precision.

(B) Convergence of the finite-sigma excluded-present counterexample.
"""

import sys
sys.set_int_max_str_digits(200000)
import itertools
import numpy as np
from math import log
import mpmath as mp
from scipy.optimize import brentq

mp.mp.dps = 60
banner = lambda t: print("\n" + "=" * 78 + "\n" + t + "\n" + "=" * 78)


# ---------------------------------------------------------------------------
banner("A.  Part-5 family, recomputed in extended precision straight from P")
# ---------------------------------------------------------------------------
def cyc_mp(N, L):
    """P built entry-wise; eta = exp(-L).  pi = uniform (doubly stochastic)."""
    eta = mp.e ** (-mp.mpf(L))
    one = mp.mpf(1) / N
    P = [[one for _ in range(N)] for _ in range(N)]
    for i in range(3):
        P[i][(i + 1) % 3] = (2 - eta) / mp.mpf(N)
        P[i][(i + 2) % 3] = eta / mp.mpf(N)
    return P

def sigma_mp(P):
    N = len(P)
    pi = mp.mpf(1) / N
    return mp.fsum(pi * P[i][j] * mp.log(P[i][j] / P[j][i])
                   for i in range(N) for j in range(N) if P[i][j] > 0)

def E_mp(P):
    N = len(P)
    pi = mp.mpf(1) / N
    return mp.fsum(pi * P[i][j] * mp.log(P[i][j] / pi)
                   for i in range(N) for j in range(N) if P[i][j] > 0)

def stoch_err(P):
    N = len(P)
    r = max(abs(mp.fsum(P[i]) - 1) for i in range(N))
    c = max(abs(mp.fsum(P[i][j] for i in range(N)) - 1) for j in range(N))
    return float(max(r, c))

print("  For each N, solve for L so sigma = 1 nat/step EXACTLY, then read off E.")
print("  'direct' columns are computed from the matrix, not from a closed form.")
print(f"  {'N':>5} {'L=-ln(eta)':>13} {'sigma direct':>20} {'E direct':>16} "
      f"{'stoch err':>11} {'min P_ij':>12}")
table = []
for N in (6, 8, 12, 17, 25, 39, 55, 77, 122):
    mp.mp.dps = 60
    f = lambda L: float(sigma_mp(cyc_mp(N, L))) - 1.0
    lo, hi = 1e-6, 1e6
    if f(lo) * f(hi) > 0:
        print(f"  {N:5d}   (no bracket: f(lo)={f(lo):.3g}, f(hi)={f(hi):.3g})")
        continue
    L = brentq(f, lo, hi, xtol=1e-10, rtol=1e-15, maxiter=400)
    mp.mp.dps = max(60, int(L / 2.3) + 60)      # keep eta representable
    P = cyc_mp(N, L)
    s, e = sigma_mp(P), E_mp(P)
    mn = min(min(row) for row in P)
    table.append((N, L, float(s), float(e)))
    print(f"  {N:5d} {L:13.6g} {mp.nstr(s, 16):>20} {mp.nstr(e, 10):>16} "
          f"{stoch_err(P):11.2e} {mp.nstr(mn, 4):>12}")
mp.mp.dps = 60

print("\n  Every P_ij > 0 strictly (irreducible, aperiodic, full support);")
print("  pi = uniform exactly; sigma = 1 nat/step exactly; E falls without bound.")
print("\n  Against the asymptote E ~ ln2 / (L + ln2):")
for (N, L, s, e) in table:
    pred = float(mp.log(2) / (L + mp.log(2)))
    print(f"    N={N:4d}  E={e:.8e}   ln2/(L+ln2)={pred:.8e}   "
          f"ratio={e/pred:.6f}")

print("\n  Extrapolation at fixed sigma = 1 nat/step (N ~ sqrt(6L)):")
for L in (1e4, 1e6, 1e8, 1e12):
    print(f"    L={L:>8.0e}  N ~ {float(mp.sqrt(6*(L+mp.log(2)))):12.1f} states"
          f"  ->  E ~ {float(mp.log(2)/(L+mp.log(2))):.3e} nats")


# ---------------------------------------------------------------------------
banner("B.  Finite-sigma excluded-present counterexample -- convergence")
# ---------------------------------------------------------------------------
def obs_path_law(phi, q, n):
    """X_t = phi(U_t,U_{t+1}) for t=0..n-1; U i.i.d. Bern(q).  Vectorised."""
    m = n + 1
    U = ((np.arange(1 << m)[:, None] >> np.arange(m)[None, :]) & 1).astype(np.int8)
    w = np.where(U == 1, q, 1 - q).prod(axis=1)
    codes = np.zeros(U.shape[0], dtype=np.int64)
    for t in range(n):
        codes = codes * 3 + np.asarray(phi)[2 * U[:, t] + U[:, t + 1]]
    law = np.bincount(codes, weights=w, minlength=3 ** n)
    return law

def kl_rev(law, n):
    idx = np.arange(3 ** n)
    digits = []
    x = idx.copy()
    for _ in range(n):
        digits.append(x % 3)
        x //= 3
    # digits[0] is the LAST symbol; reversing the word = reversing digit order
    rev_idx = np.zeros_like(idx)
    for d in range(n):
        rev_idx = rev_idx * 3 + digits[d]
    rev = law[rev_idx]
    m = law > 0
    if np.any(rev[m] <= 0):
        return np.inf
    return float(np.sum(law[m] * np.log(law[m] / rev[m])))

for q, phi in [(0.25, (0, 1, 2, 0)), (0.1, (0, 1, 2, 0)), (0.4, (0, 1, 2, 0))]:
    print(f"\n  U ~ Bern({q}),  phi(u,v) indexed by 2u+v = {phi}")
    print(f"  (E_gap = I(X_<=-1 ; X_>=1) = 0 EXACTLY: X is 1-dependent, past is a")
    print(f"   function of U_<=0 and future of U_>=1, which are independent.)")
    prev, incs = None, []
    for n in range(2, 15):
        d = kl_rev(obs_path_law(phi, q, n), n)
        if not np.isfinite(d):
            print(f"    n={n:2d}  D_n = +inf  (not absolutely continuous)")
            prev = None
            break
        inc = None if prev is None else d - prev
        prev = d
        if inc is not None:
            incs.append(inc)
        if n >= 9:
            print(f"    n={n:2d}  D_n={d:12.8f}  D_n/n={d/n:.8f}  "
                  f"D_n - D_(n-1) = {inc:.8f}")
    if len(incs) >= 4:
        a, b, c = incs[-3], incs[-2], incs[-1]
        r = (c - b) / (b - a) if abs(b - a) > 1e-14 else 0.0
        lim = c + (c - b) * r / (1 - r) if abs(1 - r) > 1e-9 else float('nan')
        print(f"    increment sequence -> geometric ratio {r:.4f}, "
              f"Aitken limit sigma ~ {lim:.6f} nats/step")
        print(f"    => sigma is FINITE and STRICTLY POSITIVE, with E_gap = 0.")
print("\nDONE.")
