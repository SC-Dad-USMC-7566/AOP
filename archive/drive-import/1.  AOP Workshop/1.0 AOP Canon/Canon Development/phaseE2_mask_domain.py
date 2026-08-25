#!/usr/bin/env python3
"""
phaseE2_mask_domain.py  —  AOP structural probe E2 (pre-red-team hardening)

Question: is the semantic mask sharp ONLY where integration is trivially low, or is
there a genuinely integrated regime where the per-edge mask weight is both WELL-DEFINED
and INFORMATIVE? This is the load-bearing methodological question. It may FAIL; report
either way. No threshold is moved after seeing results.

Model: Sigma = (I + g L)^-1 over three topologies L in {chain, mean-field, sparse-random},
sweeping global coupling g from near-zero to strong. Viability V = closeness of a
designated regulated node (node 0) to its target (its mean, 0): V = 1/Var(x_0).
One load-bearing edge and one inert spectator edge are designated by construction.
Mask weight w_e = fractional drop in V when edge e is scrambled (removed and re-solved).

------------------------------------------------------------------------------------------
FLAG TO PRIME (operationalization of h_e — resolvability half-width).
The work order says read the resolvability half-width from the canon's deposited signature
(inferential VIF term + interventional edge-drag; "report 1/sqrt(lambda_min), 1/sqrt(lambda_max)").
The NAIVE reading (eigenvalues of the precision M = I+gL) is DEGENERATE for a graph
Laplacian: L has a zero eigenvalue (constant mode), so lambda_min(M) == 1 for ALL g, and
1/sqrt(lambda_min) never grows — the blur mechanism the probe is about would never engage,
and the mask would appear trivially sharp everywhere for a spurious reason.
The inferential VIF the canon names (VIF = 1/(1-R^2)) is collinearity of the node states,
i.e. a property of the STATE CORRELATION matrix Corr(Sigma), not of M. As g rises the nodes
become collinear along the mean mode -> lambda_min(Corr) -> 0 -> 1/sqrt(lambda_min) diverges
(blur climbs) while 1/sqrt(lambda_max) stays bounded (aggregate stays sharp) — exactly the
Section 13 statement. So the resolvability spectrum is read on Corr(Sigma).
Frozen, parameter-free half-width (declared operationalization, analogous to B1 in E1):
    r = (1/sqrt(lam_min) - 1/sqrt(lam_max)) / (1/sqrt(lam_min) + 1/sqrt(lam_max))   in [0,1)
    h_e = |w_e| * r
r is the normalized sloppy-vs-stiff spread of Corr(Sigma); h_e is |w_e| scaled by it.
This has a clean reading: h_e <= 0.5|w_e|  <=>  sqrt(kappa) <= 3  <=>  kappa(Corr) <= 9,
where kappa = lam_max/lam_min is the correlation-matrix condition number. No free constant.
The frozen pass/fail thresholds rho=0.5, K=3, tau_floor are NOT moved; only the referent of
the spectrum is fixed (precision -> correlation) to make it non-degenerate. Per-node VIFs
(diag of Corr^-1) are also reported for cross-checking. Prime: please confirm this referent.
------------------------------------------------------------------------------------------
"""
import numpy as np
from itertools import combinations

SEED = 20260723
rng = np.random.default_rng(SEED)
N = 8
REGULATED = 0
RHO = 0.5      # frozen: well-defined <=> h_e <= RHO*|w_e|
K   = 3.0      # frozen: informative <=> (w_LB - w_inert) >= K*max(h_LB,h_inert)
FLOOR_RATIO = 0.05   # frozen: tau_floor = TC at g where off-diag coupling = 5% of diagonal

def laplacian(edges, n=N):
    L = np.zeros((n, n))
    for i, j in edges:
        L[i, j] -= 1; L[j, i] -= 1
        L[i, i] += 1; L[j, j] += 1
    return L

def chain_edges(n=N):    return [(i, i+1) for i in range(n-1)]
def complete_edges(n=N): return list(combinations(range(n), 2))
def sparse_edges(n=N, p=0.35):
    while True:
        e = [(i, j) for i, j in combinations(range(n), 2) if rng.random() < p]
        # connectivity check
        adj = {k: set() for k in range(n)}
        for i, j in e:
            adj[i].add(j); adj[j].add(i)
        seen = {0}; stack = [0]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen: seen.add(v); stack.append(v)
        if len(seen) == n and len(e) >= n:  # connected and not too sparse
            return e

def bfs_dist(edges, src, n=N):
    adj = {k: set() for k in range(n)}
    for i, j in edges: adj[i].add(j); adj[j].add(i)
    d = {src: 0}; stack = [src]
    while stack:
        u = stack.pop(0)
        for v in adj[u]:
            if v not in d: d[v] = d[u]+1; stack.append(v)
    return d

def cov(L, g):
    return np.linalg.inv(np.eye(N) + g*L)

def var0(L, g):
    return cov(L, g)[REGULATED, REGULATED]

def scramble_var0(edges, e, g):
    """remove edge e, rebuild Laplacian, return Var(x_0)"""
    L2 = laplacian([x for x in edges if x != e])
    return var0(L2, g)

def total_correlation(S):
    v = np.diag(S)
    s, ld = np.linalg.slogdet(S)
    return 0.5 * (np.sum(np.log(v)) - ld)

def corr_from_cov(S):
    d = np.sqrt(np.diag(S))
    return S / np.outer(d, d)

def phi_mip(S):
    """Gaussian integrated info across the minimum-cut bipartition:
       min over nonempty proper bipartitions of I(part;rest)."""
    n = S.shape[0]
    idx = list(range(n))
    best = np.inf
    for r in range(1, n//2 + 1):
        for A in combinations(idx, r):
            A = list(A); B = [k for k in idx if k not in A]
            s, lA = np.linalg.slogdet(S[np.ix_(A, A)])
            s, lB = np.linalg.slogdet(S[np.ix_(B, B)])
            s, lAB = np.linalg.slogdet(S)
            mi = 0.5*(lA + lB - lAB)
            # normalize by size of smaller part (min-information-partition convention)
            best = min(best, mi/min(len(A), len(B)))
    return best

def g_floor(edges):
    """g such that off-diagonal precision coupling = 5% of diagonal, at mean degree."""
    L = laplacian(edges)
    dbar = np.mean(np.abs(np.diag(L)))          # mean degree
    # M_ij = -g (unit edge); M_ii = 1 + g*deg ; ratio g/(1+g*dbar) = 0.05
    return FLOOR_RATIO / (1 - FLOOR_RATIO*dbar) if FLOOR_RATIO*dbar < 1 else 1e-3

def resolv(S):
    C = corr_from_cov(S)
    w = np.linalg.eigvalsh(C)
    w = np.clip(w, 1e-12, None)
    lam_min, lam_max = w[0], w[-1]
    s_min, s_max = 1/np.sqrt(lam_min), 1/np.sqrt(lam_max)
    r = (s_min - s_max) / (s_min + s_max)
    kappa = lam_max/lam_min
    vif = np.diag(np.linalg.inv(C))              # per-node VIF = 1/(1-R^2)
    return s_min, s_max, r, kappa, vif

def pick_edges(topo, edges):
    dist = bfs_dist(edges, REGULATED)
    # load-bearing: an edge incident to regulated node 0
    lb = next(e for e in edges if REGULATED in e)
    # inert: edge whose endpoints are farthest from 0 (structural, not effect-selected)
    inert = max(edges, key=lambda e: (min(dist[e[0]], dist[e[1]]), dist[e[0]]+dist[e[1]]))
    return lb, inert

print(f"# phaseE2 — mask informative-and-well-defined domain")
print(f"SEED={SEED}  N={N}  regulated=node{REGULATED}  RHO={RHO} K={K} floor_ratio={FLOOR_RATIO}")

topologies = {
    "chain":       chain_edges(),
    "mean-field":  complete_edges(),
    "sparse-rand": sparse_edges(),
}

gsweep = np.concatenate([np.array([0.0]), np.geomspace(0.01, 50, 40)])
any_pass = False
pass_records = []

for topo, edges in topologies.items():
    L = laplacian(edges)
    lb, inert = pick_edges(topo, edges)
    tau_floor = total_correlation(cov(L, g_floor(edges)))
    print(f"\n## topology={topo}  |E|={len(edges)}  LB_edge={lb}  inert_edge={inert}  "
          f"g_floor={g_floor(edges):.4f}  tau_floor(TC)={tau_floor:.4f}")
    header = f"{'g':>8} {'TC':>8} {'nontriv':>7} {'w_LB':>8} {'w_inert':>9} " \
             f"{'h_LB':>8} {'h_inert':>8} {'welldef':>7} {'inform':>6} {'1/√lmin':>8} {'1/√lmax':>8}"
    print(header)
    for g in gsweep:
        if g == 0.0:  # independent nodes: no mask, skip (trivially separable)
            continue
        S = cov(L, g)
        TC = total_correlation(S)
        s_min, s_max, r, kappa, vif = resolv(S)
        vL, vI = var0(L, g), None
        wLB = 1 - vL / scramble_var0(edges, lb, g)
        wIN = 1 - vL / scramble_var0(edges, inert, g)
        hLB, hIN = abs(wLB)*r, abs(wIN)*r
        welldef = (hLB <= RHO*abs(wLB)) and (hIN <= RHO*abs(wIN) if abs(wIN) > 1e-9 else True)
        # informative: LB/inert gap resolvable, not swamped by blur
        inform = (wLB - wIN) >= K*max(hLB, hIN)
        nontriv = TC > tau_floor
        star = "  <== PASS" if (welldef and inform and nontriv) else ""
        if (welldef and inform and nontriv):
            any_pass = True
            pass_records.append((topo, g, TC, phi_mip(S), kappa))
        # print a subsampled set of rows to keep output readable
        if g in gsweep[[1,5,10,15,20,25,30,35,40]] or star:
            print(f"{g:8.3f} {TC:8.3f} {str(nontriv):>7} {wLB:8.3f} {wIN:9.4f} "
                  f"{hLB:8.4f} {hIN:8.4f} {str(welldef):>7} {str(inform):>6} "
                  f"{s_min:8.3f} {s_max:8.3f}{star}")

print("\n## PRE-REGISTERED QUESTION")
print("   Exists a system that is well-defined AND informative AND non-trivial (TC>tau_floor)?")
print(f"   ANSWER: {'PASS (mask salvageable)' if any_pass else 'FAIL (confined to trivial cases)'}")
if any_pass:
    print("   Region(s) with well-defined & informative & non-trivial:")
    # summarize per topology: g-band, TC range, Phi_MIP range
    bytopo = {}
    for t, g, tc, phi, kap in pass_records:
        bytopo.setdefault(t, []).append((g, tc, phi, kap))
    for t, recs in bytopo.items():
        gs = [r[0] for r in recs]; tcs=[r[1] for r in recs]; phis=[r[2] for r in recs]; kaps=[r[3] for r in recs]
        print(f"     {t}: g in [{min(gs):.3f},{max(gs):.3f}]  TC in [{min(tcs):.3f},{max(tcs):.3f}]  "
              f"Phi_MIP in [{min(phis):.4f},{max(phis):.4f}]  kappa(Corr) in [{min(kaps):.2f},{max(kaps):.2f}]")
else:
    print("   The intersection is empty above the triviality floor: the mask is, on present")
    print("   evidence, confined to near-separable systems. (Adverse result — do not soften.)")
