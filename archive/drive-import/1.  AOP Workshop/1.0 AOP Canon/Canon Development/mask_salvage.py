"""
mask_salvage.py  --  Semantic-mask salvage diagnostic (AOP, 21 July 2026)
==========================================================================

QUESTION (the standing prerequisite before any further mask-based build):
    Does the scramble-and-rerun semantic mask's WELL-DEFINED region overlap its
    INFORMATIVE region at all, or is the mask structurally confined to trivial cases?

    (a) well-defined region  = where the per-edge scramble weight is a resolvable
        number (narrow interval), not context-dependent to the point of uselessness;
    (b) informative region   = where the weights actually DISCRIMINATE a
        viability-relevant (load-bearing) edge from a spectator edge;
    (c) their intersection.

MODEL CLASS (charter: closed-form, analytic; same idiom as canon Phase C/D scripts).
    Static Gaussian on a coupling graph.  Precision  J(theta) = I + sum_e theta_e * B_e,
    B_e = Laplacian of edge e.  Covariance  Sigma = J^{-1}.  Everything below is a
    closed-form function of Sigma; there is no sampling and no estimator.

VIABILITY FUNCTIONAL (grounded, not invented).
    Kolchinsky & Wolpert 2018 (Interface Focus 8:20180041) define viability as the
    NEGENTROPY of the system's distribution.  For a Gaussian that is
        V = -H = -0.5 * log det( Sigma[S,S] )  + const,
    S = the DECLARED viability set (the observable slot of the AOP declaration tuple D).
    A local S admits a genuine spectator; S = all nodes recovers the KW whole-system case.

SCRAMBLE-AND-RERUN MASK.
    "Scramble edge e" = knock out that channel's coupling (theta_e -> 0) and rerun
    (recompute Sigma).  The weight of edge e IN CONTEXT C (a set of already-scrambled
    edges) is the marginal viability drop it then causes:
        phi_e(C) = V(scramble C) - V(scramble C U {e}).
    Because a coupled Gaussian is non-additive, phi_e depends on C: edge e's weight is
    INTERVAL-VALUED,  [ min_C phi_e(C) , max_C phi_e(C) ]  (canon E17's own language).
    The average over contexts is the Shapley value (Shapley 1953); the interval is the
    span of marginal contributions.  Single-edge marginals are non-additive exactly when
    edges interact -- a SETTLED fact of cooperative-game attribution, not a new claim.

WHAT WE MEASURE vs COUPLING g:
    - span width of each edge (well-definedness; the interventional "edge-drag")
    - separation of the LOAD edge's interval from the SPECTATOR edge's interval
      (resolvable discrimination = informativeness that is actually usable)
    - sloppy spectrum of the parameter Fisher F_{ee'} = 0.5 tr(Sigma B_e Sigma B_e')
      -> 1/sqrt(lambda_min) (sloppy) vs 1/sqrt(lambda_max) (stiff), and
         VIF_e = (F^{-1})_{ee} * F_{ee} = 1/(1-R_e^2)   (Marquardt 1970; the inferential blur)
    - redundancy sign (O-information, Rosas et al. 2019) on the declared set, to connect
      the blur to KW's own "non-unique under redundancy" caveat.

VERDICT LOGIC.
    well_defined(g)  : max span width over structural edges <= tau_wd
    informative(g)   : load interval lies ABOVE spectator interval AND their midpoints
                       are separated by >= tau_inf (a non-trivial, resolvable gap)
    salvageable(g)   : well_defined(g) AND informative(g)
    We sweep g, report the two regions and their intersection, and -- the honest core --
    report whether the LOAD and SPECTATOR intervals are ever simultaneously (i) narrow and
    (ii) disjoint.  A clean negative ("well-defined only where uninformative") is a valid result.
"""

import numpy as np
import itertools

np.set_printoptions(precision=4, suppress=True)


# ----------------------------------------------------------------------------- model
def edge_laplacian(N, i, j):
    B = np.zeros((N, N))
    B[i, i] += 1.0; B[j, j] += 1.0
    B[i, j] -= 1.0; B[j, i] -= 1.0
    return B


def precision(N, edges, theta, base=1.0):
    """J = base*I + sum_e theta_e B_e."""
    J = base * np.eye(N)
    for (i, j), t in zip(edges, theta):
        J = J + t * edge_laplacian(N, i, j)
    return J


def cov(N, edges, theta, base=1.0):
    return np.linalg.inv(precision(N, edges, theta, base))


def viability(Sigma, S):
    """V = -H_gauss(S) up to the additive constant that cancels in every weight below.
       V = -0.5 * log det Sigma[S,S].  Higher V = tighter (more concentrated) target."""
    sub = Sigma[np.ix_(S, S)]
    sign, logdet = np.linalg.slogdet(sub)
    return -0.5 * logdet


# ----------------------------------------------------------- scramble-and-rerun weights
def V_with_scrambled(N, edges, theta, base, S, scrambled_idx):
    """Viability after knocking out the edges in `scrambled_idx` (theta_e -> 0)."""
    th = list(theta)
    for k in scrambled_idx:
        th[k] = 0.0
    return viability(cov(N, edges, th, base), S)


def edge_weight_interval(N, edges, theta, base, S, e):
    """Interval-valued weight of edge e: min/mean/max over all contexts C (coalitions of
       the OTHER edges already scrambled). phi_e(C) = V(scr C) - V(scr C+{e})."""
    others = [k for k in range(len(edges)) if k != e]
    vals = []
    for r in range(len(others) + 1):
        for C in itertools.combinations(others, r):
            v_without_e = V_with_scrambled(N, edges, theta, base, S, list(C))
            v_with_e = V_with_scrambled(N, edges, theta, base, S, list(C) + [e])
            vals.append(v_without_e - v_with_e)   # drop caused by additionally scrambling e
    vals = np.array(vals)
    return vals.min(), vals.mean(), vals.max()   # (lo, shapley, hi)


def total_weight(N, edges, theta, base, S):
    """W_total = V(all present) - V(all structural edges scrambled) = whole viability drop."""
    v_full = viability(cov(N, edges, theta, base), S)
    v_none = V_with_scrambled(N, edges, theta, base, S, list(range(len(edges))))
    return v_full - v_none


# --------------------------------------------------------------- sloppy Fisher spectrum
def param_fisher(N, edges, theta, base):
    """F_{ee'} = 0.5 tr(Sigma B_e Sigma B_e') -- Gaussian Fisher info in the edge params."""
    Sigma = cov(N, edges, theta, base)
    m = len(edges)
    Bs = [edge_laplacian(N, i, j) for (i, j) in edges]
    SB = [Sigma @ B for B in Bs]
    F = np.zeros((m, m))
    for a in range(m):
        for b in range(m):
            F[a, b] = 0.5 * np.trace(SB[a] @ SB[b])
    return F


def vif_vector(F):
    """VIF_e = (F^{-1})_{ee} * F_{ee} = 1/(1-R_e^2). Collinearity/blur of edge e's estimate."""
    Finv = np.linalg.inv(F)
    return np.array([Finv[e, e] * F[e, e] for e in range(F.shape[0])])


# ------------------------------------------------------------------- O-information (sign)
def o_information(Sigma):
    N = len(Sigma)

    def H(idx):
        s = Sigma[np.ix_(idx, idx)]
        _, ld = np.linalg.slogdet(s)
        return 0.5 * (len(idx) * np.log(2 * np.pi * np.e) + ld)

    allidx = list(range(N))
    Hall = H(allidx)
    TC = sum(H([i]) for i in allidx) - Hall
    DTC = sum(H([i for i in allidx if i != k]) for k in allidx) - (N - 1) * Hall
    return TC - DTC


# ============================================================================ EXPERIMENT
# The salvage question is scale-free if we phrase it as: are the LOAD edge's weight
# interval and the SPECTATOR edge's weight interval DISJOINT?  Disjointness (lo_L > hi_S)
# requires the weights to be both NARROW enough (well-defined) AND SEPARATED (informative)
# at once -- it is exactly "resolvable discrimination."  We decompose it into the two
# named sub-conditions and report all three, plus the aggregate-mode weight (E17's
# "aggregate stays sharp"), the redundancy sign Omega, and the sloppy Fisher spectrum.

def run_experiment(title, N, edges, S, load_idx, spec_idx, theta_of, grid,
                   rel_width_tol=0.5):
    """rel_width_tol: an edge weight is 'well-defined' if its interval width is at most
       this fraction of the aggregate (whole-set) weight -- a scale-free resolvability bar."""
    print("=" * 100)
    print(title)
    print("viability V = -0.5 log det Sigma[S,S]  (Kolchinsky-Wolpert negentropy on declared set S=%s)" % S)
    print("LOAD edge = %s   SPECTATOR edge = %s" % (edges[load_idx], edges[spec_idx]))
    print("well-defined(edge): interval width <= %.2f x aggregate weight;  "
          "salvageable: LOAD interval disjoint above SPECTATOR interval" % rel_width_tol)
    print("=" * 100)
    header = (" ctrl | Wagg  | LOAD[lo, shap, hi]         SPEC[lo, shap, hi]        | "
              "disjoint  loWidth/Wagg | Omega  condF  VIFmax | wd_load inf SALV")
    print(header); print("-" * len(header))
    recs = []
    for c in grid:
        theta = theta_of(c)
        Sigma = cov(N, edges, theta, BASE)
        Wagg = total_weight(N, edges, theta, BASE, S)
        lo_L, sh_L, hi_L = edge_weight_interval(N, edges, theta, BASE, S, load_idx)
        lo_S, sh_S, hi_S = edge_weight_interval(N, edges, theta, BASE, S, spec_idx)
        widthL = hi_L - lo_L
        disjoint = lo_L > hi_S
        rel_w = widthL / Wagg if Wagg > 1e-12 else np.inf
        wd_load = rel_w <= rel_width_tol
        inf = sh_L - sh_S >= 0.02 * max(Wagg, 1e-9)   # midpoints separated (scale-relative)
        salv = disjoint and wd_load
        F = param_fisher(N, edges, theta, BASE)
        ev = np.linalg.eigvalsh(F)
        condF = ev[-1] / max(ev[0], 1e-300)
        Om = o_information(Sigma)
        vif = vif_vector(F)
        recs.append(dict(c=c, Wagg=Wagg, disjoint=disjoint, wd_load=wd_load, inf=inf,
                         salv=salv, rel_w=rel_w, Om=Om, condF=condF,
                         lo_L=lo_L, hi_L=hi_L, lo_S=lo_S, hi_S=hi_S))
        print("%5.2f | %5.3f | [%.3f %.3f %.3f]   [% .3f % .3f % .3f] | %5s   %8.2f     | "
              "% .3f %6.1f %6.1f | %5s %4s %4s"
              % (c, Wagg, lo_L, sh_L, hi_L, lo_S, sh_S, hi_S, str(disjoint), rel_w,
                 Om, condF, vif.max(),
                 "Y" if wd_load else "-", "Y" if inf else "-", "YES" if salv else "no"))
    print("-" * len(header))
    salv_c = [r["c"] for r in recs if r["salv"]]
    disj_c = [r["c"] for r in recs if r["disjoint"]]
    wd_c = [r["c"] for r in recs if r["wd_load"]]
    print("  well-defined LOAD (narrow interval): %s" % (wd_c if wd_c else "EMPTY"))
    print("  discrimination survives (disjoint):  %s" % (disj_c if disj_c else "EMPTY"))
    print("  SALVAGEABLE (both at once):          %s" % (salv_c if salv_c else "EMPTY"))
    return recs


BASE = 1.0

# --- MODEL 1: CONCENTRATED viability (path, lone distant target). The easy/degenerate case.
#     viability rests on ONE identifiable edge; spectator is topologically far; low redundancy.
edges1 = [(0, 1), (1, 2), (2, 3), (3, 4)]
recs1 = run_experiment(
    "MODEL 1 -- CONCENTRATED VIABILITY (path 0-1-2-3-4, S={0}; one edge holds the target)",
    N=5, edges=edges1, S=[0], load_idx=0, spec_idx=3,
    theta_of=lambda g: [g] * 4,
    grid=[0.05, 0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0])

print()

# --- MODEL 2: COLLECTIVE viability (two 3-node modules, well-posed partition). The case E17
#     actually worries about: viability of module 1 is a COLLECTIVE mode held by three
#     mutually-substitutable intra-module edges -> redundancy-dominated as coupling rises.
#     LOAD = an intra-module-1 edge (holds the collective).  SPECTATOR = an intra-module-2 edge.
#     Sweep intra-module coupling a; bridge coupling b fixed small.
N2 = 6
edges2 = [(0, 1), (1, 2), (0, 2),        # module 1 (S) -- indices 0,1,2
          (3, 4), (4, 5), (3, 5),        # module 2       -- indices 3,4,5
          (2, 3)]                        # bridge         -- index 6
B_BRIDGE = 0.15
def theta2(a):
    return [a, a, a, a, a, a, B_BRIDGE]
recs2 = run_experiment(
    "MODEL 2 -- COLLECTIVE VIABILITY (two 3-node modules, S={0,1,2}; a collective mode"
    "\n            held by 3 substitutable intra-module edges; bridge b=%.2f)" % B_BRIDGE,
    N=N2, edges=edges2, S=[0, 1, 2], load_idx=0, spec_idx=3,
    theta_of=theta2,
    grid=[0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0])

# --- also: the AGGREGATE-mode weight in model 2 (scramble ALL of module 1's edges at once)
#     vs a single intra-1 edge -- E17's claim that the aggregate stays sharp while parts blur.
print("\nAGGREGATE-MODE CHECK (model 2): whole-module weight (sharp) vs single-edge share (blurs)")
print("   a    | W(module1 aggregate) | single intra-1 edge interval [lo, hi]  width/Wagg")
for a in [0.3, 1.0, 3.0, 8.0]:
    theta = theta2(a)
    Wagg = total_weight(N2, edges2, theta, BASE, [0, 1, 2])   # scrambles ALL 7 edges though
    # aggregate of just module-1's 3 edges:
    v_full = viability(cov(N2, edges2, theta, BASE), [0, 1, 2])
    v_mod1_off = V_with_scrambled(N2, edges2, theta, BASE, [0, 1, 2], [0, 1, 2])
    W_mod1 = v_full - v_mod1_off
    lo, sh, hi = edge_weight_interval(N2, edges2, theta, BASE, [0, 1, 2], 0)
    print("  %4.2f |      %6.3f          | [%.3f, %.3f]   width/Wmod1 = %.2f"
          % (a, W_mod1, lo, hi, (hi - lo) / max(W_mod1, 1e-9)))

# --- MODEL 3: SEMANTIC-BEYOND-SYNTACTIC (the real test). Complete graph K4 on {0,1,2,3},
#     ALL edges the SAME coupling strength a (syntactically symmetric). Discrimination can
#     come ONLY from the declared viability set S={0,1}, never from coupling strength.
#       (0,1) LOAD      : both endpoints in S  (directly holds the declared pair)
#       (0,2)(0,3)(1,2)(1,3) support: one endpoint in S
#       (2,3) SPECTATOR : neither endpoint in S
#     If the mask is reading V (semantics) it must rank (0,1) > support > (2,3) with
#     resolvable (disjoint) intervals. If under strong a the LOAD and SPECTATOR intervals
#     merge, the mask's semantic discrimination is confined to the weak-coupling corner.
edges3 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
recs3 = run_experiment(
    "MODEL 3 -- SEMANTIC-BEYOND-SYNTACTIC (K4, ALL edges equal strength a, S={0,1};"
    "\n            discrimination can come only from the declared viability set, not coupling)",
    N=4, edges=edges3, S=[0, 1], load_idx=0, spec_idx=5,
    theta_of=lambda a: [a] * 6,
    grid=[0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0])

# scale-free informativeness: does the mask recover the semantic ordering (2,1,1,1,1,0 endpoints
# in S) with intervals that do not overlap ACROSS relevance classes?  Report the load-vs-spectator
# margin lo_L - hi_S as a fraction of the aggregate weight.
print("\nSEMANTIC MARGIN (model 3): (LOAD.lo - SPEC.hi)/Wagg  -- positive = classes resolvably separated")
print("   a    | margin/Wagg | Omega  | verdict")
for r in recs3:
    a = r["c"]
    margin = (r["lo_L"] - r["hi_S"]) / max(r["Wagg"], 1e-9)
    print("  %4.2f |   % .3f    | % .3f | %s"
          % (a, margin, r["Om"], "resolvably separated" if margin > 0 else "MERGED (unresolvable)"))

# --- THRESHOLD LOCATION (model 3): find a* where the LOAD and SPECTATOR intervals merge
#     (lo_L = hi_S), and the redundancy Omega there. Also show the Shapley-MEAN separation
#     persists past a* -- i.e. the verdict depends on the resolution standard used.
print("\nTHRESHOLD (model 3): interval-merge point a*  (fine sweep)")
print("   a    | lo_L   hi_S  disjoint | Shapley sep sh_L-sh_S | Omega")
a_star = None
prev_disj = True
for a in np.linspace(0.2, 6.0, 59):
    theta = [a] * 6
    Sig = cov(4, edges3, theta, BASE)
    lo_L, sh_L, hi_L = edge_weight_interval(4, edges3, theta, BASE, [0, 1], 0)
    lo_S, sh_S, hi_S = edge_weight_interval(4, edges3, theta, BASE, [0, 1], 5)
    disj = lo_L > hi_S
    if prev_disj and not disj and a_star is None:
        a_star = a
        Om = o_information(Sig)
        print("  %4.2f | %.3f  %.3f  %5s | interval MERGE here     | Omega=%.3f  <== a*"
              % (a, lo_L, hi_S, str(disj), Om))
    prev_disj = disj
# report Shapley-mean separation well past the merge
for a in [a_star if a_star else 3.0, 8.0, 15.0]:
    theta = [a] * 6
    _, sh_L, _ = edge_weight_interval(4, edges3, theta, BASE, [0, 1], 0)
    _, sh_S, _ = edge_weight_interval(4, edges3, theta, BASE, [0, 1], 5)
    Om = o_information(cov(4, edges3, theta, BASE))
    print("  a=%.1f: Shapley-MEAN load=%.3f spec=%.3f (still separated=%s)  Omega=%.2f"
          % (a, sh_L, sh_S, sh_L > sh_S + 0.02, Om))
print("  => Under the INTERVAL (resolvable per-edge weight) standard the mask degenerates at a*;")
print("     under the SHAPLEY-MEAN standard a separation persists, but that mean AVERAGES OVER")
print("     an interval as wide as the weight itself -- it hides the context-sensitivity, it")
print("     does not remove it. The honest per-edge object is the interval, and it merges at a*.")

# --------------------------------------------------------------------------- FINAL VERDICT
print("\n" + "=" * 100)
print("FINAL VERDICT")
print("=" * 100)
s1 = [r["c"] for r in recs1 if r["salv"]]
s2 = [r["c"] for r in recs2 if r["salv"]]
s3 = [r["c"] for r in recs3 if r["salv"]]
red_dominated_2 = [r["c"] for r in recs2 if r["Om"] > 0.1]
red_dominated_3 = [r["c"] for r in recs3 if r["Om"] > 0.1]
print("MODEL 1 (concentrated, low-redundancy viability):        salvageable at %s" % (s1 if s1 else "EMPTY"))
print("MODEL 2 (collective, spectator syntactically distant):   salvageable at %s" % (s2 if s2 else "EMPTY"))
print("MODEL 3 (semantic-beyond-syntactic, equal-strength K4):  salvageable at %s" % (s3 if s3 else "EMPTY"))
print("MODEL 3 redundancy-dominated (Omega>0.1) at:             %s" % (red_dominated_3 if red_dominated_3 else "none"))
overlap3 = set(s3) & set(red_dominated_3)
print("MODEL 3 salvageable AND redundancy-dominated:            %s" % (sorted(overlap3) if overlap3 else "EMPTY"))
