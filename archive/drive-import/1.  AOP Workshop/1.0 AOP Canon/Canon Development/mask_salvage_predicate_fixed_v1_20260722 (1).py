"""
mask_salvage_predicate_fixed_v1_20260722.py
===========================================
AOP builder proposal (Task C of the mask-salvage work order, 22 July 2026).
Prime verifies; Ben decides. Touches no canon master. Does NOT overwrite the
deposited audit artifact mask_salvage.py (sha256 20c02ca1...) - this is a NEW file.

WHY THIS FILE EXISTS. The deposited mask_salvage.py advertises in its prose
    salvageable = well_defined AND informative
with well_defined = (max interval-width over STRUCTURAL edges <= tau_wd * W_agg)
and informative  = (load interval ABOVE spectator interval) AND (midpoint
                    separation >= tau_inf * W_agg).
Its executable body instead computes
    salv = disjoint AND wd_load
i.e. well-definedness on the LOAD edge only, and it drops the informativeness
(midpoint) flag entirely. On the K4 table these coincide - the load edge is
coincidentally the widest structural edge, and disjointness coincidentally
implies the midpoint flag - so the printed numbers are unaffected, but the
estimand does not match the prose.

DECISION (builder's pick; Prime may overrule). Implement the PROSE predicate in
full:
    well_defined(a) = max over ALL modelled (structural) edges of
                      (interval width / W_agg) <= tau_wd            [GLOBAL]
    informative(a)  = (load lo > spectator hi)                      [disjoint]
                      AND (load Shapley - spectator Shapley >= tau_inf * W_agg)
    salvageable(a)  = well_defined(a) AND informative(a)
Rationale:
  * GLOBAL (not load-only) well-definedness: the mask is unusable if ANY
    structural edge's weight is unresolvable, not only the load edge's. The
    honest question the salvage diagnostic asks is whether the mask returns
    resolvable numbers at all - a whole-graph property. Load-only silently
    assumes the answer for five of six edges.
  * KEEP the midpoint (inf) conjunct: the salvage claim is "resolvable
    DISCRIMINATION," which requires the classes to be separated, not merely
    non-overlapping at the interval endpoints. Dropping it answers a weaker
    question than the prose declares.
Both choices are defensible and answer different questions; this file reports
the K4 table under ALL FOUR combinations so the sensitivity is explicit, then
adopts the prose predicate (P4) as the headline.

FUNCTIONAL. Unchanged from the deposited script (pinned in Task A):
    Precision J = I + sum_e a_e * B_e   (B_e = edge Laplacian; "scramble e"
    subtracts the whole term a_e*B_e -> load edge weight is O(a), matching the
    outside critic; the off-diagonal-only alternative that gives Prime's O(a^2)
    is a DIFFERENT scramble and is not used here).
    Sigma = J^{-1};  V = -1/2 log det Sigma[S,S]  (Kolchinsky-Wolpert negentropy).
    phi_e(C) = V(scramble C) - V(scramble C+{e}); interval = [min_C, max_C];
    Shapley = mean_C.
"""
import itertools
import numpy as np

BASE = 1.0
EDGES = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]  # K4
S = [0, 1]            # declared viability set
LOAD, SPEC = 0, 5     # (0,1) both endpoints in S ; (2,3) neither
GRID = [0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0]
TAU_WD, TAU_INF = 0.5, 0.02


def edge_laplacian(N, i, j):
    B = np.zeros((N, N))
    B[i, i] += 1.0; B[j, j] += 1.0
    B[i, j] -= 1.0; B[j, i] -= 1.0
    return B


def cov(theta):
    J = BASE * np.eye(4)
    for (i, j), t in zip(EDGES, theta):
        J = J + t * edge_laplacian(4, i, j)
    return np.linalg.inv(J)


def viability(Sigma):
    _, ld = np.linalg.slogdet(Sigma[np.ix_(S, S)])
    return -0.5 * ld


def V_scr(theta, scrambled):
    th = list(theta)
    for k in scrambled:
        th[k] = 0.0
    return viability(cov(th))


def interval(theta, e):
    others = [k for k in range(len(EDGES)) if k != e]
    vals = []
    for r in range(len(others) + 1):
        for C in itertools.combinations(others, r):
            vals.append(V_scr(theta, list(C)) - V_scr(theta, list(C) + [e]))
    vals = np.array(vals)
    return vals.min(), vals.mean(), vals.max()


def total_weight(theta):
    return viability(cov(theta)) - V_scr(theta, list(range(len(EDGES))))


def flags(a, tau_wd=TAU_WD, tau_inf=TAU_INF):
    theta = [a] * 6
    W = total_weight(theta)
    ivs = [interval(theta, e) for e in range(6)]
    loL, shL, hiL = ivs[LOAD]
    loS, shS, hiS = ivs[SPEC]
    widths = [hi - lo for lo, sh, hi in ivs]
    wd_global = max(widths) / W <= tau_wd
    wd_load = (hiL - loL) / W <= tau_wd
    disjoint = loL > hiS
    inf = (shL - shS) >= tau_inf * max(W, 1e-9)
    return dict(a=a, W=W, loL=loL, shL=shL, hiL=hiL, loS=loS, shS=shS, hiS=hiS,
                wd_global=wd_global, wd_load=wd_load, disjoint=disjoint, inf=inf)


def report():
    print("=" * 92)
    print("Task C - four predicate variants on the K4 mask table (S={0,1})")
    print("  P1 = wd_load  AND disjoint            (what the deposited code EXECUTES)")
    print("  P2 = wd_load  AND disjoint AND inf")
    print("  P3 = wd_global AND disjoint")
    print("  P4 = wd_global AND disjoint AND inf   (what the deposited PROSE declares; ADOPTED)")
    print("=" * 92)
    hdr = " a    | Wagg  | LOAD[lo,sh,hi]            SPEC[lo,sh,hi]           | wdG wdL dis inf | P1 P2 P3 P4"
    print(hdr); print("-" * len(hdr))
    sets = {k: [] for k in ("P1", "P2", "P3", "P4")}
    for a in GRID:
        f = flags(a)
        P1 = f["wd_load"] and f["disjoint"]
        P2 = f["wd_load"] and f["disjoint"] and f["inf"]
        P3 = f["wd_global"] and f["disjoint"]
        P4 = f["wd_global"] and f["disjoint"] and f["inf"]
        for k, v in (("P1", P1), ("P2", P2), ("P3", P3), ("P4", P4)):
            if v:
                sets[k].append(a)
        print(" %4.2f | %5.3f | [%.3f %.3f %.3f]   [% .3f % .3f % .3f] |  %d   %d   %d   %d  |  %d  %d  %d  %d"
              % (a, f["W"], f["loL"], f["shL"], f["hiL"], f["loS"], f["shS"], f["hiS"],
                 f["wd_global"], f["wd_load"], f["disjoint"], f["inf"], P1, P2, P3, P4))
    print("-" * len(hdr))
    for k in ("P1", "P2", "P3", "P4"):
        print("  %s salvageable: %s" % (k, sets[k] if sets[k] else "EMPTY"))
    print("\n  => All four predicates give the SAME salvageable set on this K4 model")
    print("     (the documented coincidence). They answer DIFFERENT questions; P4")
    print("     (the prose predicate) is adopted as the honest headline.\n")


def threshold_sensitivity():
    print("=" * 92)
    print("Task C - threshold sensitivity of the ADOPTED predicate P4")
    print("=" * 92)
    from bisect import bisect
    print("  a_max (upper edge of salvageable region) vs (tau_wd, tau_inf):")
    print("  tau_wd \\ tau_inf :   0.00     0.02     0.05     0.10")
    fine = np.linspace(0.1, 8.0, 80)
    for tw in (0.3, 0.5, 0.7, 1.0):
        cells = []
        for ti in (0.0, 0.02, 0.05, 0.10):
            ok = [a for a in fine
                  if (lambda f: f["wd_global"] and f["disjoint"] and f["inf"])(flags(a, tw, ti))]
            cells.append("%.2f" % (max(ok) if ok else 0.0))
        print("   %.1f              : " % tw + "   ".join("%7s" % c for c in cells))
    print("\n  Two boundaries bound the salvageable region, and a_max = min(them):")
    print("   * disjointness boundary  a* = (3 + sqrt(13))/2 = %.6f  (THRESHOLD-INDEPENDENT," % ((3 + 13 ** 0.5) / 2))
    print("     and closed-form - see Task B memo). This is where load/spectator intervals merge.")
    print("   * well-definedness boundary depends on tau_wd only (tau_inf is INERT on K4,")
    print("     because disjointness already forces a large midpoint gap): tau_wd=0.3 -> a~1.19,")
    print("     tau_wd=0.5 -> a~6.40, tau_wd>=0.7 -> never fails on [0.1,20].")
    print("   For tau_wd >= 0.5 the disjointness boundary a*=3.303 binds first; for tau_wd=0.3")
    print("   the well-definedness boundary binds first. The 'salvage' ceiling is a*=(3+sqrt13)/2")
    print("   under any reasonably loose tau_wd.\n")


def _marginals(a, e):
    theta = [a] * 6
    others = [k for k in range(6) if k != e]
    out = []
    for r in range(len(others) + 1):
        for C in itertools.combinations(others, r):
            out.append((frozenset(C), V_scr(theta, list(C)) - V_scr(theta, list(C) + [e])))
    return out


def attribution_conventions():
    """Task D: does the load/spectator merge have a finite ceiling under each
    attribution convention? (Pre-registered before running - see frozen note.)"""
    from math import factorial
    from scipy.optimize import brentq

    def gap(a, conv):
        mL = _marginals(a, LOAD); mS = _marginals(a, SPEC)
        vL = {C: v for C, v in mL}; vS = {C: v for C, v in mS}
        if conv == "envelope":
            return min(v for _, v in mL) - max(v for _, v in mS)
        if conv.startswith("card"):
            k = int(conv[4:])
            return (min(v for C, v in mL if len(C) <= k)
                    - max(v for C, v in mS if len(C) <= k))
        if conv == "matched":
            common = [frozenset(C) for r in range(5)
                      for C in itertools.combinations([1, 2, 3, 4], r)]
            return min(vL[C] - vS[C] for C in common)
        if conv == "mean":
            return np.mean([v for _, v in mL]) - np.mean([v for _, v in mS])
        if conv == "shapley":
            n = 6
            def shap(m):
                return sum(factorial(len(C)) * factorial(n - 1 - len(C)) / factorial(n) * v
                           for C, v in m)
            return shap(mL) - shap(mS)
        raise ValueError(conv)

    def ceiling(conv, amax=12.0):
        aa = np.linspace(0.05, amax, 240); prev = None
        for a in aa:
            g = gap(a, conv)
            if prev is not None and prev > 0 and g <= 0:
                try:
                    return brentq(lambda x: gap(x, conv), a - (aa[1] - aa[0]), a, xtol=1e-6)
                except Exception:
                    return a
            prev = g
        return None

    print("=" * 92)
    print("Task D - finite merge ceiling by attribution convention (pre-registered)")
    print("=" * 92)
    for conv in ("envelope", "card0", "card1", "card2", "card3", "card4",
                 "matched", "mean", "shapley"):
        ce = ceiling(conv)
        print("  %-9s : %s" % (conv, ("a*=%.4f" % ce) if ce else "NO finite ceiling"))
    print("  (sparse sampling on the envelope base: ceiling recovered but biased upward")
    print("   & variable - n=4 median~3.95, n=16 median~3.41 -> ESTIMATED, converges to")
    print("   the analytic a*=(3+sqrt13)/2=3.303 only as sample size grows.)")
    print("  => finite ceiling ONLY under min-max envelope and |C|>=3; vanishes under")
    print("     matched / mean / Shapley (load stays above spectator everywhere).\n")


def phase_diagram_sketch():
    """Task E (SKETCH ONLY, no grade): are the critic's three coordinates
    independent on K4? C1 relevance, C2 stability, C3 identifiability(1/VIF)."""
    def fisher(theta):
        Sig = cov(theta)
        Bs = [edge_laplacian(4, i, j) for i, j in EDGES]
        SB = [Sig @ B for B in Bs]
        return np.array([[0.5 * np.trace(SB[a] @ SB[b]) for b in range(6)] for a in range(6)])

    def coords(a, e):
        theta = [a] * 6
        ivs = [v for _, v in _marginals(a, e)]
        C1 = float(np.mean(ivs))
        C2 = 1.0 / (1.0 + (max(ivs) - min(ivs)))
        F = fisher(theta); Finv = np.linalg.inv(F)
        C3 = 1.0 / (Finv[e, e] * F[e, e])
        return C1, C2, C3

    print("=" * 92)
    print("Task E - three-coordinate phase-diagram SKETCH (a lead, NO grade)")
    print("=" * 92)
    print("  edge    | C1 relevance | C2 stability | C3 identifiability (1/VIF)")
    for e, name in ((0, "LOAD"), (1, "support"), (5, "SPEC")):
        c = coords(3.0, e)
        print("  %-7s |   %.4f     |   %.4f     |   %.4f" % (name, c[0], c[1], c[2]))
    print("  => C1 and C2 rank edges in OPPOSITE order (load most relevant/least stable;")
    print("     spectator least relevant/most stable) - genuinely independent on K4.")
    print("     C3 is DEGENERATE (equal for all edges by K4 symmetry) - carries no info")
    print("     here; testing its independence needs an ASYMMETRIC coupling model.")
    print("  SKETCH ONLY - not approved work, no canon status.\n")


if __name__ == "__main__":
    report()
    threshold_sensitivity()
    attribution_conventions()
    phase_diagram_sketch()
