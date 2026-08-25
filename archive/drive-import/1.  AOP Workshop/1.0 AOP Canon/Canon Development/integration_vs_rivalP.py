#!/usr/bin/env python3
"""
AOP §3 one-way kill check: canon Integration vs Rival P on the B. subtilis
sporulation phosphorelay wiring.

Order: TASK_CW_AOP_Aster_Triage_20260725 §3.
Seat: Claude Cowork (execution).  This script is deposited alongside
AOP_Integration_vs_RivalP_KillCheck_v0.1.md.

DECLARATIONS (all explicit; nothing inferred from rates, which the wiring
does not supply -- see Claude Science Step 0):

  S (system variables / declared partition into parts):
      the named molecular species of the phosphorelay, one node each.
      Baseline node set  N0 = {KinA, KinB, KinC, Spo0F, Spo0B, Spo0A}
      Variant node set   N1 = N0 + {PhosF, PhosA}   (phosphatase drains as
                         explicit nodes: Rap-type drain on Spo0F, Spo0E-type
                         drain on Spo0A)

  P (the partition the min-cut searches over):
      the bipartitions of the declared node set.  The search is EXHAUSTIVE
      over all 2^(n-1) - 1 bipartitions; no partition is pre-selected.

  M (model class):
      static Gaussian.  Sigma = (I + g L)^-1 with L the combinatorial
      Laplacian L = D - A of the UNDIRECTED, unit-weighted wiring graph.
      Symmetrization is forced: (I + gL) must be symmetric positive definite
      for Sigma to be a covariance.  The canon's construction is defined on
      an undirected L.  Direction is therefore NOT available to Integration.
      This is declared, not hidden -- it is load-bearing for the result.

  g (coupling constant): baseline 1.0; swept over 0.1 .. 10.0.

  N (normalization): two reported --
      (a) raw min-cut mutual information (nats)
      (b) min-cut MI divided by min(|A|,|B|) (IIT-style size normalization)

  Perturbation = node deletion (remove node + incident edges), matching a
  gene disruption in the published grid.

Integration quantities computed (both are Integration-panel objects in the
canon, both closed-form on topology + partition):
  TC   -- total correlation, the Integration axis proxy
  PHI  -- minimum-cut dependence (formerly Phi_MIP), the irreducibility
          diagnostic, canon v1.26 Sec.4

Rival P: near-WT if >=1 directed path from a surviving kinase to Spo0A
         remains; collapse if zero such paths remain.  Computed on the
         DIRECTED graph.
"""
import itertools, math
import numpy as np

# ---------- wiring ----------
DIRECTED = [("KinA","Spo0F"),("KinB","Spo0F"),("KinC","Spo0F"),
            ("Spo0F","Spo0B"),("Spo0B","Spo0A")]
DRAINS   = [("PhosF","Spo0F"),("PhosA","Spo0A")]   # phosphatase drains
KINASES  = ["KinA","KinB","KinC"]
TARGET   = "Spo0A"

def build(nodes, edges):
    idx = {n:i for i,n in enumerate(nodes)}
    n = len(nodes)
    A = np.zeros((n,n))
    for u,v in edges:
        if u in idx and v in idx:
            A[idx[u],idx[v]] = 1.0
            A[idx[v],idx[u]] = 1.0          # symmetrization (declared)
    L = np.diag(A.sum(1)) - A
    return A, L

def sigma(L, g):
    n = L.shape[0]
    return np.linalg.inv(np.eye(n) + g*L)

def logdet(M):
    s, ld = np.linalg.slogdet(M)
    assert s > 0, "non-PD submatrix"
    return ld

def total_correlation(S):
    return 0.5*(np.sum(np.log(np.diag(S))) - logdet(S))

def min_cut_dependence(S):
    """Exhaustive min-cut. Returns (raw, normalized, argmin partition)."""
    n = S.shape[0]
    if n < 2:
        return 0.0, 0.0, None
    best_raw, best_norm, best_part = None, None, None
    full = logdet(S)
    for r in range(1, n//2 + 1):
        for A in itertools.combinations(range(n), r):
            if r == n - r and 0 not in A:      # dedupe complementary halves
                continue
            B = tuple(i for i in range(n) if i not in A)
            mi = 0.5*(logdet(S[np.ix_(A,A)]) + logdet(S[np.ix_(B,B)]) - full)
            mi = max(mi, 0.0)
            nm = mi/min(len(A), len(B))
            if best_raw is None or mi < best_raw - 1e-15:
                best_raw, best_norm, best_part = mi, nm, (A,B)
    return best_raw, best_norm, best_part

def rival_P(nodes, edges):
    """>=1 directed path surviving-kinase -> Spo0A ?"""
    if TARGET not in nodes:
        return "collapse", 0          # target itself deleted
    adj = {}
    for u,v in edges:
        if u in nodes and v in nodes:
            adj.setdefault(u, []).append(v)
    count = 0
    for k in KINASES:
        if k not in nodes:
            continue
        seen, stack = set(), [k]
        while stack:
            x = stack.pop()
            if x == TARGET:
                count += 1
                break
            if x in seen: continue
            seen.add(x)
            stack.extend(adj.get(x, []))
    return ("near-WT" if count >= 1 else "collapse"), count

# ---------- conditions ----------
# 4.1 kinase grid (strain -> genes disrupted); 4.2 relay-core grid
CONDITIONS = [
 ("JH642",   "wild type",            []),
 ("AG522",   "kinA",                 ["KinA"]),
 ("NY120",   "kinB (+kapB)",         ["KinB"]),
 ("JRL920",  "kinC",                 ["KinC"]),
 ("NY121",   "kinA kinB",            ["KinA","KinB"]),
 ("JRL1046", "kinA kinC",            ["KinA","KinC"]),
 ("JRL1004", "kinB kinC",            ["KinB","KinC"]),
 ("JRL1007", "kinA kinB kinC",       ["KinA","KinB","KinC"]),
 ("(4.2)",   "spo0A",                ["Spo0A"]),
 ("(4.2)",   "spo0F",                ["Spo0F"]),
 ("(4.2)",   "spo0B",                ["Spo0B"]),
]

def run(with_drains, g, verbose=True):
    base_nodes = ["KinA","KinB","KinC","Spo0F","Spo0B","Spo0A"]
    edges = list(DIRECTED)
    if with_drains:
        base_nodes = base_nodes + ["PhosF","PhosA"]
        edges = edges + DRAINS
    rows = []
    for strain, geno, dele in CONDITIONS:
        nodes = [x for x in base_nodes if x not in dele]
        A, L = build(nodes, edges)
        S = sigma(L, g)
        tc = total_correlation(S)
        phi, phin, part = min_cut_dependence(S)
        lab, npaths = rival_P(set(nodes), edges)
        partstr = ""
        if part:
            partstr = "{" + ",".join(nodes[i] for i in part[0]) + "}"
        rows.append(dict(strain=strain, geno=geno, n=len(nodes), TC=tc,
                         PHI=phi, PHIn=phin, cut=partstr,
                         rival=lab, paths=npaths))
    if verbose:
        print(f"\n=== drains={'ON ' if with_drains else 'OFF'}  g={g} ===")
        print(f"{'genotype':<18}{'n':>3}{'TC':>10}{'PHI':>10}{'PHI/min|.|':>12}"
              f"{'argmin cut':>26}{'RivalP':>10}{'#paths':>7}")
        for r in rows:
            print(f"{r['geno']:<18}{r['n']:>3}{r['TC']:>10.5f}{r['PHI']:>10.6f}"
                  f"{r['PHIn']:>12.6f}{r['cut']:>26}{r['rival']:>10}{r['paths']:>7}")
    return rows

if __name__ == "__main__":
    for drains in (False, True):
        run(drains, 1.0)

    print("\n=== g-sensitivity of PHI (drains OFF) ===")
    gs = [0.1,0.25,0.5,1.0,2.0,5.0,10.0]
    base = run(False, 1.0, verbose=False)
    print(f"{'genotype':<18}" + "".join(f"{'g='+str(g):>11}" for g in gs))
    for i,(strain,geno,dele) in enumerate(CONDITIONS):
        vals=[]
        for g in gs:
            vals.append(run(False, g, verbose=False)[i]['PHI'])
        print(f"{geno:<18}" + "".join(f"{v:>11.6f}" for v in vals))

    print("\n=== monotonicity check on the kinase grid (drains OFF, g=1) ===")
    rows = run(False,1.0,verbose=False)[:8]
    for r in rows:
        k = 3 - sum(1 for kk in KINASES if kk in r['geno'].replace('kin','Kin'))
        print(f"{r['geno']:<18} surviving kinases={r['paths']:>1}  PHI={r['PHI']:.6f}  TC={r['TC']:.6f}")

# ---------------- §3.3 separability analysis (appended) ----------------
def separability(rows, label):
    """Can a single monotone threshold on PHI reproduce Rival P's labels?"""
    near = sorted(r['PHI'] for r in rows if r['rival'] == 'near-WT')
    coll = sorted(r['PHI'] for r in rows if r['rival'] == 'collapse')
    # try both orientations
    hi_ok = max(near) < min(coll)          # collapse = high PHI
    lo_ok = max(coll) < min(near)          # collapse = low PHI
    print(f"\n[{label}]")
    print(f"  near-WT PHI: {[round(x,6) for x in near]}")
    print(f"  collapse PHI: {[round(x,6) for x in coll]}")
    print(f"  single threshold reproduces Rival P?  collapse=high: {hi_ok}   collapse=low: {lo_ok}")
    return hi_ok or lo_ok

def order_isomorphism(rows):
    """On the kinase grid: is PHI a strictly monotone function of path count?"""
    pairs = sorted(((r['paths'], round(r['PHI'], 12)) for r in rows), reverse=True)
    print("\n[order isomorphism on the kinase grid]")
    seen = {}
    for p, phi in pairs:
        seen.setdefault(p, set()).add(phi)
    for p in sorted(seen, reverse=True):
        print(f"  surviving kinases = {p}: PHI values = {sorted(seen[p])}")
    strict = all(len(v) == 1 for v in seen.values())
    vals = [sorted(seen[p])[0] for p in sorted(seen, reverse=True)]
    mono = all(vals[i] < vals[i+1] for i in range(len(vals)-1))
    print(f"  PHI is a FUNCTION of path count (no within-level spread): {strict}")
    print(f"  PHI is STRICTLY MONOTONE (decreasing path count -> increasing PHI): {mono}")
    return strict and mono

if __name__ == "__main__":
    print("\n" + "="*74)
    print("SEPARABILITY / ORDER-ISOMORPHISM  (the §3.3 question)")
    print("="*74)
    for drains in (False, True):
        for g in (0.25, 1.0, 5.0):
            rows = run(drains, g, verbose=False)
            tag = f"drains={'ON' if drains else 'OFF'} g={g}"
            order_isomorphism(rows[:8])
            separability(rows[:8], tag + "  KINASE GRID (8 conditions)")
            separability(rows,    tag + "  ALL 11 CONDITIONS")
