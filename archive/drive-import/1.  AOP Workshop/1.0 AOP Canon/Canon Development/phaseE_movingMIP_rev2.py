"""
phaseE_movingMIP.py - time-extended (moving) Phi_MIP over a window that STRADDLES
a relabeling transition. Builder proposal, 21 July 2026. Canon v1.20 FRONTIER item
(section 13a): "the MIP is a discrete argmin that relabels across a transition, so
no single time-extended partition scores a window straddling it."

WHAT THIS SCRIPT DOES (three self-contained, closed-form checks; no estimation):

  (A) THE OBSTACLE, made concrete. On a two-module coupled-Gaussian window whose
      inter-module coupling b(t) ramps through a phase transition, the per-slice
      Phi_MIP argmin relabels away from the module cut at b* ~ 0.43; no single
      fixed partition is the MIP on both sides.

  (B) THE DISCRETE MOVING-MIP (hard Viterbi temporal regularization). Score the
      whole window with a single time-COHERENT partition family P(t) by minimizing
      J_lambda = sum_t Phi(t,P_t) + lambda * sum_t rot(P_{t-1},P_t). Dynamic
      programming finds the exact minimizing HARD path. The OPTIMIZED objective
      J/T is continuous & piecewise-linear in lambda (min of finitely many affine
      path costs); the selected hard path can switch at breakpoints. This is a
      defensible proposed regularization of instantaneous MIPs - NOT a soft/
      annealed construction, and NOT yet a closed 'time-extended Phi_MIP'.
      [NOTE: an earlier version REPORTED only the deficit term (dropping the
      lambda*rot penalty it optimizes), which plotted as a spurious step and
      falsely contradicted the objective's continuity. Fixed here - the objective
      and its components are reported separately.]

  (C) THE SPECTRAL DIAGNOSTIC (inflated supra-Laplacian) - an INDEPENDENT graph-
      coherence read, NOT a derived surrogate for moving Phi_MIP. Build the space-
      time coupling graph (time-slices as layers, adjacent node copies coupled with
      weight a^2), diagonalize one operator, and read the leading spatial mode's
      L2-mass-per-slice. IMPORTANT SCOPE: this operator is NOT derived as a
      relaxation of the Gaussian log-det MIP objective, no bound relates their
      optima, and no map ties a<->lambda. In this test graph the graph-spectral
      crossing is ANALYTIC at b=1 (module-diff mode 6b vs within-module 3+3b),
      which does NOT coincide with the Gaussian-MIP relabel near b~0.43 - so the
      mass profile does not validate correspondence to Phi_MIP. Treat as a
      diagnostic pending a derivation (or de-scoping).

RELATED LITERATURE (verified against primary sources; these are PRECEDENT and
motivation - NOT a previously-published solution of this AOP object imported
unchanged. Temporal smoothing of changing partitions is established across four
literatures; this script is a LABELLED SYNTHESIS of those strategies):
  * Froyland & Koltai, "Detecting the birth and death of finite-time coherent
    sets," Comm. Pure Appl. Math. 76 (2023) [doi:10.1002/cpa.22115]: the inflated
    dynamic Laplacian  Delta_{G0,a} F = a^2 d_tt F + Delta_{g_t} F  is a Laplace-
    Beltrami operator from the pullback metric of a nonautonomous FLOW; parameter
    a interpolates per-slice (a->0) to frozen (a->inf). FK describe multilayer-
    network supra-Laplacians as STRUCTURALLY/FORMALLY SIMILAR with results that
    "should carry over" - a formal analogy, NOT operator identity with AOP's
    coupling-graph object. (C) borrows the inflation idea; it is not FK's operator.
  * Gomez et al., PRL 110 (2013) 028701; De Domenico et al., PRX 3 (2013) 041022:
    supra-Laplacian of a multilayer network (layers~time slices, interlayer
    coupling~a^2). A structural analogy to (C), per FK - not an independent
    rediscovery of the same solved object.
  * Rose, Proc. IEEE 86 (1998) 2210 [doi:10.1109/5.726788]; Tishby, Pereira &
    Bialek 1999 (information bottleneck); Parker & Dimitrov, Entropy 24 (2022) 1231
    [doi:10.3390/e24091231]: deterministic annealing / IB SOFTEN assignments with
    an entropy term and bifurcate as temperature drops. They motivate relaxation
    broadly; they do NOT derive the HARD switching-cost path functional in (B).
    A genuine annealed version (Gibbs path distribution, temperature tau) is the
    creative next step - see end matter of the proposal .md.
  * Closer discrete precedent: the temporal-community literature (snapshot quality
    + temporal smoothness as a combinatorial partition problem with convex
    relaxations), e.g. Chen, Kawadia & Urgaonkar (arXiv:1303.7226).

GRADING. (A) SETTLED (direct computation on the canon's own Phase-D model).
(B) FRONTIER (a defensible proposed hard temporal regularization of instantaneous
MIPs, solved exactly by DP; NOT yet shown to deserve the name time-extended
Phi_MIP - grid-dependence, degeneracy, and hard-vs-soft all open). (C) FRONTIER
(an independent spectral diagnostic; NOT derived as a relaxation of the Gaussian
MIP objective, and its transition does not coincide with the MIP relabel here).
This deposit does NOT close the canon FRONTIER item; open items named at the end.

Syntactic layer only (Phi_MIP, coupling graph). Touches no semantic-mask,
star, or provenance quantities.
"""
import numpy as np
import itertools

# ----------------------------------------------------------------------------
# Coupling model: two 3-node modules (intra weight 1.0), inter-module weight b.
# Gaussian stationary covariance Sigma = (I + g L)^{-1}, exactly as phaseD1/D2.
# ----------------------------------------------------------------------------
N = 6
G = 1.0
MODULE = frozenset({0, 1, 2})            # the "two individuals" cut


def _add(L, i, j, w):
    L[i, i] += w; L[j, j] += w; L[i, j] -= w; L[j, i] -= w


def L_of(b):
    """Graph Laplacian of the coupling at inter-module weight b."""
    L = np.zeros((N, N))
    for m in (range(0, 3), range(3, 6)):
        m = list(m)
        for i in range(len(m)):
            for j in range(i + 1, len(m)):
                _add(L, m[i], m[j], 1.0)
    for i in range(0, 3):
        for j in range(3, 6):
            _add(L, i, j, b)
    return L


def Sigma(b):
    return np.linalg.inv(np.eye(N) + G * L_of(b))


def tc(S, idx):
    """Total correlation of the sub-block indexed by idx (Gaussian, closed form)."""
    s = S[np.ix_(idx, idx)]
    return 0.5 * (np.sum(np.log(np.diag(s))) - np.log(np.linalg.det(s)))


# enumerate bipartitions (dedup complement at the half cut)
ALL = list(range(N))
PARTS = []
for r in range(1, N // 2 + 1):
    for c in itertools.combinations(ALL, r):
        c = frozenset(c)
        if r == N // 2 and (frozenset(ALL) - c) in PARTS:
            continue
        PARTS.append(c)
MOD_K = next(k for k, P in enumerate(PARTS)
             if P in (frozenset({0, 1, 2}), frozenset({3, 4, 5})))


def deficit(S, P):
    A = sorted(P); B = sorted(set(ALL) - P)
    return tc(S, ALL) - tc(S, A) - tc(S, B)


def phi_mip(S):
    defs = np.array([deficit(S, P) for P in PARTS])
    k = int(defs.argmin())
    return defs[k], PARTS[k]


# ----------------------------------------------------------------------------
# (A) THE OBSTACLE: the per-slice MIP relabels inside the window.
# ----------------------------------------------------------------------------
def check_A():
    print("(A) OBSTACLE - per-slice MIP relabels within a ramp window [SETTLED]")
    print("     b     Phi_MIP    MIP cut          on module boundary?")
    prev = None; bstar = None
    for b in np.linspace(0.0, 1.4, 15):
        phi, cut = phi_mip(Sigma(b))
        onmod = cut in (frozenset({0, 1, 2}), frozenset({3, 4, 5}))
        flag = "  <-- RELABEL" if (prev is not None and cut != prev) else ""
        if bstar is None and prev is not None and not onmod:
            bstar = b
        print(f"   {b:4.2f}  {phi:8.4f}   {str(sorted(cut)):15}  {onmod}{flag}")
        prev = cut
    print(f"   -> MIP leaves the module cut near b* ~ {bstar:.2f}; a window over"
          f" [0,1] straddles it.\n")


# ----------------------------------------------------------------------------
# (B) DISCRETE MOVING-MIP over a window, by dynamic programming (Viterbi).
#     Minimize  sum_t deficit(t, P_t)  +  lambda * sum_t rot(P_{t-1}, P_t),
#     rot = partition-change (Hamming distance mod complement).
# ----------------------------------------------------------------------------
def _rot(P, Q):
    a = np.zeros(N, int); a[list(P)] = 1
    b = np.zeros(N, int); b[list(Q)] = 1
    return int(min((a != b).sum(), (a != (1 - b)).sum()))


def moving_mip(bs, lam):
    T = len(bs)
    D = np.array([[deficit(Sigma(b), P) for P in PARTS] for b in bs])
    R = np.array([[_rot(P, Q) for Q in PARTS] for P in PARTS])
    K = len(PARTS)
    dp = D[0].copy(); bp = np.zeros((T, K), int)
    for t in range(1, T):
        cost = dp[:, None] + lam * R          # prev x cur
        bp[t] = cost.argmin(0)
        dp = D[t] + cost.min(0)
    e = int(dp.argmin()); path = [e]
    for t in range(T - 1, 0, -1):
        e = bp[t, e]; path.append(e)
    path = path[::-1]
    # REPORT THE OPTIMIZED OBJECTIVE, not just its data term. The deficit-only
    # component below is monotone-STEP in lambda and is NOT what the DP minimizes;
    # reporting it alone (as an earlier version did) produced a plotted step that
    # falsely contradicted the continuity of the true objective. [Aster review,
    # 21 Jul 2026 - defect confirmed by independent reproduction.]
    deficit_component = float(np.mean([D[t, path[t]] for t in range(T)]))
    rot_cost = sum(R[path[t - 1], path[t]] for t in range(1, T))   # total Hamming rotation
    n_changes = sum(path[t] != path[t - 1] for t in range(1, T))   # distinct change events
    objective = float((sum(D[t, path[t]] for t in range(T)) + lam * rot_cost) / T)  # J_lambda / T
    return path, objective, deficit_component, rot_cost, n_changes, D


def check_B():
    print("(B) MOVING-MIP - hard temporally-regularized partition path [FRONTIER]")
    bs = np.linspace(0.0, 1.0, 21)
    *_, D = moving_mip(bs, 0.0)
    perslice = float(D.min(1).mean())          # incoherent lower bound
    frozen = float(D.mean(0).min())            # best single fixed partition
    print(f"     per-slice optimum (incoherent lower bound): {perslice:.4f}")
    print(f"     best FROZEN single partition (upper bound): {frozen:.4f}")
    print("     The DP minimizes J_lambda = sum_t Phi(t,P_t) + lambda*sum_t rot;")
    print("     we report the OPTIMIZED objective J/T and decompose it. (Reporting")
    print("     the deficit component ALONE - as an earlier version did - is a step")
    print("     in lambda and misrepresents the objective's continuity.)")
    print("     lambda   J/T (objective)  deficit-part  rot-cost  change-events")
    for lam in (0.0, 0.05, 0.1, 0.2, 0.5, 1.0):
        _, obj, defc, rotc, nch, _ = moving_mip(bs, lam)
        print(f"     {lam:5.2f}   {obj:12.4f}   {defc:10.4f}  {rotc:7d}   {nch:8d}")
    # continuity of the TRUE objective, over a fine grid
    lg = np.linspace(0, 1.0, 101)
    Js = [moving_mip(bs, l)[1] for l in lg]
    max_jump = float(max(Js[i+1]-Js[i] for i in range(len(Js)-1)))
    print(f"     J/T over lambda in [0,1] (101 pts): monotone nondecreasing,"
          f" max step={max_jump:.4f}")
    print("     -> the OPTIMIZED objective is continuous/piecewise-linear in lambda")
    print("        (min of finitely many affine path costs); the selected HARD path")
    print("        can still switch at breakpoints. This is a hard Viterbi-regularized")
    print("        partition path, NOT a soft/annealed (Gibbs) construction.\n")
    path, *_ = moving_mip(bs, 0.1)
    labels = [tuple(sorted(PARTS[k])) for k in path]
    prev = None
    print("     path (lambda=0.1) - note the transition is module-cut -> a SINGLETON")
    print("     1|5 cut, and at b~0.43 SIX singleton cuts are degenerate minimizers")
    print("     (unnormalized-MIP small-side vulnerability; one is picked by")
    print("     enumeration order):")
    for t, l in enumerate(labels):
        if l != prev:
            print(f"       b={bs[t]:.2f}: partition {l}")
            prev = l
    print()


# ----------------------------------------------------------------------------
# (C) SPECTRAL SURROGATE: inflated supra-Laplacian on the space-time graph.
#     Delta_{a} = blockdiag(L(b_t))  +  a^2 * (temporal chain Laplacian).
#     == Froyland-Koltai inflated dynamic Laplacian == multilayer supra-Laplacian.
# ----------------------------------------------------------------------------
def supra_L(bs, a):
    T = len(bs)
    S = np.zeros((T * N, T * N))
    for t, b in enumerate(bs):
        S[t*N:(t+1)*N, t*N:(t+1)*N] += L_of(b)          # intra-slice
    for t in range(T - 1):                               # temporal chain (Neumann)
        for i in range(N):
            u, v = t*N + i, (t+1)*N + i
            S[u, u] += a**2; S[v, v] += a**2
            S[u, v] -= a**2; S[v, u] -= a**2
    return S


def check_C():
    print("(C) SPECTRAL DIAGNOSTIC - inflated supra-Laplacian (NOT a derived"
          " surrogate for moving Phi_MIP) [FRONTIER]")
    bs = np.linspace(0.2, 1.4, 31); a = 0.8
    S = supra_L(bs, a)
    w, V = np.linalg.eigh(S)
    T = len(bs)

    # FK Theorem 7 interpolation: leading eigenvalue rises with a toward the
    # a->inf (frozen, time-averaged) dynamic-Laplacian value.
    print("     FK Thm-7 interpolation (leading nontrivial supra eigenvalue vs a):")
    Lbar = np.mean([L_of(b) for b in bs], 0)
    ref = float(np.linalg.eigvalsh(Lbar)[1])
    for aa in (0.1, 0.3, 1.0, 3.0, 10.0):
        lam2 = float(np.linalg.eigvalsh(supra_L(bs, aa))[1])
        print(f"       a={aa:5.1f}  lambda_2={lam2:.4f}")
    print(f"       a->inf reference (time-averaged L) lambda_2={ref:.4f}"
          f"   (dynamic-Laplacian limit)")

    # FK spatial/temporal classifier: spatial mode has ~constant slice mean.
    def slice_mean_var(k):
        F = V[:, k].reshape(T, N)
        return F.mean(1).var() / (F.var() + 1e-12)
    kspat = next(k for k in range(1, 4 * N) if slice_mean_var(k) < 0.3)
    F = V[:, kspat].reshape(T, N)
    mass = np.linalg.norm(F, axis=1); mass /= mass.max()
    # lifetime: contiguous slices carrying > 5% of peak mass
    alive = np.where(mass > 0.05)[0]
    b0, b1 = bs[alive[0]], bs[alive[-1]]
    print(f"     leading SPATIAL mode k={kspat} (a={a}, classifier thr 0.3,"
          f" lifetime thr 5%): L2-mass-per-slice:")
    for t in range(0, T, 5):
        bar = "#" * int(round(mass[t] * 30))
        print(f"       b={bs[t]:.2f}  {mass[t]:.3f}  {bar}")
    # HONEST SCOPE (Aster review 2.6): the coupling-graph L(b) eigenvalues are
    # analytic - module-difference mode = 6b, within-module modes = 3+3b - so the
    # spectral crossing is at b=1, NOT at the Gaussian-MIP transition near b~0.43.
    wgap = np.sort(np.linalg.eigvalsh(L_of(1.0)))
    print(f"     graph-L crossing is ANALYTIC at b=1 (module-diff 6b vs within 3+3b);")
    print(f"     L(b=1) eigenvalues={np.round(wgap,2)} -> degenerate at 6.")
    print(f"     -> this is an INDEPENDENT graph-coherence diagnostic. It is NOT")
    print(f"        derived as a relaxation of the Gaussian log-det MIP objective,")
    print(f"        and its transition (b=1) does NOT coincide with the MIP relabel")
    print(f"        (b~0.43). The mass decay is localization where the instantaneous")
    print(f"        spectral cost is lowest, not validated correspondence to Phi_MIP.")
    print(f"        Readout depends on a, both thresholds, and window endpoints (no")
    print(f"        robustness sweep deposited).\n")


# ----------------------------------------------------------------------------
if __name__ == "__main__":
    print(__doc__.split("CITE-DON'T-INVENT")[0].strip()[:0] or "", end="")
    print("phaseE_movingMIP - time-extended (moving) Phi_MIP across a transition\n")
    check_A()
    check_B()
    check_C()
    print("STATUS: FRONTIER (NOT closure). This is a promising method proposal, not")
    print("a closed AOP result. Open items (Aster review, 21 Jul 2026, confirmed by")
    print("independent reproduction):")
    print("  1. The discrete path is HARD Viterbi temporal regularization, not a soft")
    print("     deterministic-annealing/Gibbs construction. Rose/Tishby/Parker-Dimitrov")
    print("     motivate relaxation broadly; they do NOT derive this switching-cost")
    print("     functional. (See end-matter 4.1 for the genuinely annealed version.)")
    print("  2. The score is not time-discretization invariant: the deficit sum scales")
    print("     with grid resolution while the per-transition rot cost does not. Needs")
    print("     a dt factor J=sum dt*Phi + lambda*TV(P), or a lambda scaling law.")
    print("  3. The demonstrated transition is module-cut -> six DEGENERATE 1|5")
    print("     singletons (unnormalized-MIP small-side vulnerability), not two")
    print("     nontrivially competing organizations. Needs a symmetry-broken / two-")
    print("     real-competing-partition benchmark, and to expose all tied paths.")
    print("  4. The spectral operator is NOT derived as a relaxation of the Gaussian")
    print("     log-det MIP objective; no bound relates their optima and no map ties")
    print("     a<->lambda. In this graph the spectral crossing (b=1) does not")
    print("     coincide with the MIP relabel (b~0.43). Either derive the relaxation")
    print("     or keep the supra-Laplacian as an independent diagnostic.")
    print("  5. Literature: 'temporal smoothing of changing partitions' is established")
    print("     across dynamic coherent-set, multilayer-network, temporal-community,")
    print("     and annealed-clustering work. This is a LABELLED SYNTHESIS of those")
    print("     strategies, NOT one previously-published object solved in three fields.")
