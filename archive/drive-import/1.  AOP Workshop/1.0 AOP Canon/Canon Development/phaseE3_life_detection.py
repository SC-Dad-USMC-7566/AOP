#!/usr/bin/env python3
"""
phaseE3_life_detection.py  —  AOP structural probe E3 (pre-red-team hardening)

Question: is the Section-11a "alive" criterion (load-bearing AND decoupled internal model
of the system's own viable set) POSITIVELY detectable from third-person access, or is it
negative-only / does it need an EXTRA modeler declaration beyond the viability functional V?

Model: linear OU family, parameter d in [0,1] interpolating
   star-type (d=0): the set-point mu* is baked into x's own intrinsic drift; no separate node
   cell-type (d=1): the set-point is held in a distinct reference node r that x tracks; r is
                    separately interventable.
V = closeness of the regulated node x to its viable target mu*  =  1 / E[(x-mu*)^2].

All quantities closed-form (stationary OU covariance via Lyapunov; intervention means analytic).
Seed printed. Pre-registered questions Q1,Q2,Q3 and thresholds (w_min=0.30) frozen.

Operationalization notes (declared; prime please confirm):
 * "scramble the candidate reference edge" (step 1, load-bearing) = ABLATE the coupling term
   x<-r (remove it), then re-solve. At d=1 this leaves x with zero drift (non-stationary) =>
   total viability loss (V_scr=0). "Replace-with-mean" is NOT used, because r's mean equals the
   target mu*, so replacing r by its mean would leave x regulated and spuriously read the
   load-bearing edge as inert. Ablation is the faithful "remove the dependency" operation here.
 * "clamp r shifts where x settles" (step 2a) = do-intervention: hold r=c, solve x's stationary
   mean; gain = d(x_settle)/dc. This is the interventional (do) reading, not conditioning.
 * "r separable from the fast regulated path" (step 2b) = r has its own dynamics not
   instantaneously slaved to x (B[r,x] carries no algebraic clamp of x); the regulated node x
   itself fails 2b (clamping x directly clamps x).
"""
import numpy as np
from scipy.linalg import solve_continuous_lyapunov

SEED = 20260723
np.random.seed(SEED)
MU = 2.0            # viable target for x
KS = 1.0           # star self-regulation gain
KT = 1.0           # cell tracking gain
KR = 0.3           # reference node relaxation (baseline; r slower than x)
SX = 1.0; SR = 1.0 # noise amplitudes
W_MIN = 0.30       # frozen: load-bearing <=> scramble drops V by >= 0.30
GAIN_CUT = 0.05    # "clamp shifts x" cutoff (reported; verdict not knife-edge on it)

def B_cell(d, ks=KS, kt=KT, kr=KR):
    """2-node drift (deviation coords): nodes x=0, r=1."""
    return np.array([[ (1-d)*ks + d*kt , -d*kt ],
                     [ 0.0            ,  kr   ]])

def stationary_cov(B, D):
    # B Σ + Σ B^T = D  (OU dX=-B X dt + sqrt(D) dW). requires B stable (eig>0).
    if np.min(np.real(np.linalg.eigvals(B))) <= 1e-9:
        return None
    return solve_continuous_lyapunov(B, D)

def V_of(varx):
    return np.inf if varx <= 0 else 1.0/varx

def var_x(B, D):
    S = stationary_cov(B, D)
    return None if S is None else S[0,0]

def load_bearing_drop(d):
    """ablate x<-r edge, measure fractional drop in V (V=1/Var_x, mean stays mu*)."""
    D = np.diag([SX**2, SR**2])
    vx = var_x(B_cell(d), D)
    V0 = V_of(vx)
    # ablate the tracking term: x drift becomes only (1-d)ks (x-mu*); off-diag ->0, and the
    # d*kt part of x's self-decay is removed too (the whole x<-r coupling term is deleted).
    Bab = np.array([[ (1-d)*KS , 0.0 ],
                    [ 0.0      , KR  ]])
    vxa = var_x(Bab, D)
    Vs = 0.0 if vxa is None else V_of(vxa)     # non-stationary => total viability loss
    drop = 1.0 - (Vs/V0 if np.isfinite(V0) and V0>0 else 0.0)
    return drop, V0, Vs

def clamp_gain_on_x(d, node):
    """do-intervention: clamp `node` at c; gain = d(x stationary mean)/dc."""
    if node == 0:      # clamping x clamps x
        return 1.0
    if node == 1:      # clamp r
        denom = (1-d)*KS + d*KT
        return (d*KT)/denom if denom > 0 else 0.0
    return 0.0

def separable_from_x(node):
    """2b: node has own dynamics not instantaneously slaved to x; x itself fails."""
    return node != 0

print(f"# phaseE3 — 'alive' positive-detectability")
print(f"SEED={SEED}  mu*={MU}  ks={KS} kt={KT} kr={KR}  w_min={W_MIN}")

# ---------------- Q1: correctness across the interpolation ----------------
print("\n## Q1 (correctness: flag d=1 alive, reject d=0)")
print(f"{'d':>5} {'V_intact':>9} {'LB_drop':>8} {'load-bear':>9} {'clampgain_r':>11} {'2a':>4} {'2b(r)':>6} {'ALIVE':>6}")
alive_by_d = {}
for d in [0.0, 0.25, 0.5, 0.75, 1.0]:
    drop, V0, Vs = load_bearing_drop(d)
    lb = drop >= W_MIN
    gain = clamp_gain_on_x(d, 1)
    a2 = gain > GAIN_CUT
    b2 = separable_from_x(1)
    alive = lb and a2 and b2
    alive_by_d[d] = alive
    v0s = f"{V0:.3f}" if np.isfinite(V0) else "inf"
    print(f"{d:5.2f} {v0s:>9} {drop:8.3f} {str(lb):>9} {gain:11.3f} {str(a2):>4} {str(b2):>6} {str(alive):>6}")
Q1 = alive_by_d[1.0] and (not alive_by_d[0.0])
print(f"Q1 PASS = {Q1}  (d=1 alive={alive_by_d[1.0]}, d=0 alive={alive_by_d[0.0]})")

# ---------------- Q2: architecture, not timescale magnitude ----------------
print("\n## Q2 (verdict driven by existence of separate reference, NOT slow/fast magnitude)")
print("   sweep kr/kt over 3 orders of magnitude; verdict must not flip")
flips = []
print(f"{'kr':>8} {'kr/kt':>7} {'d0_alive':>9} {'d1_alive':>9}")
for kr in [0.01, 0.05, 0.2, 0.5, 1.0, 2.0, 5.0, 20.0]:
    def lb_drop_kr(d):
        D = np.diag([SX**2, SR**2])
        v0 = var_x(np.array([[(1-d)*KS+d*KT, -d*KT],[0.0, kr]]), D)
        V0 = V_of(v0)
        vab = var_x(np.array([[(1-d)*KS,0.0],[0.0,kr]]), D)
        Vs = 0.0 if vab is None else V_of(vab)
        return 1.0 - (Vs/V0 if np.isfinite(V0) and V0>0 else 0.0)
    def alive_kr(d):
        drop = lb_drop_kr(d)
        gain = (d*KT)/((1-d)*KS + d*KT) if ((1-d)*KS + d*KT)>0 else 0.0
        return (drop>=W_MIN) and (gain>GAIN_CUT) and separable_from_x(1)
    a0, a1 = alive_kr(0.0), alive_kr(1.0)
    flips.append((a0, a1))
    print(f"{kr:8.2f} {kr/KT:7.2f} {str(a0):>9} {str(a1):>9}")
Q2 = all((not a0) and a1 for a0, a1 in flips)
print(f"Q2 PASS = {Q2}  (d=1 stays alive and d=0 stays not-alive across all kr => architectural)")

# ---------------- Q3: does detection need a 2nd declaration beyond V? ----------------
print("\n## Q3 (can (2a)+(2b) single out r from graph+V alone, no 'this is the model' label?)")
print("   V declares the regulated node x (node 0). Test every node blind for (2a)&(2b):")
d = 1.0
qualifiers = []
for node, name in [(0,"x"),(1,"r")]:
    gain = clamp_gain_on_x(d, node)
    a2 = gain > GAIN_CUT
    b2 = separable_from_x(node)
    q = a2 and b2 and (node != 0)   # candidate MODEL node must not be the regulated node itself
    print(f"   node {name}: clamp_gain={gain:.3f}  2a={a2}  2b={b2}  qualifies_as_model={q}")
    if q: qualifiers.append(name)
Q3_base = (qualifiers == ["r"])
print(f"   base 2-node: qualifying model node(s) = {qualifiers}  -> unique r without label: {Q3_base}")

# distractor stress test: add node z that x ALSO tracks, z also holds mu* (separable, symmetric)
print("\n   [stress test] add a 2nd decoupled reference z (x tracks r AND z; both hold mu*):")
def B_cell_3(d, ks=KS, kt=KT, kr=KR, kz=KR):
    # nodes x=0, r=1, z=2 ; x tracks r and z equally
    return np.array([[ (1-d)*ks + d*(kt+kt),  -d*kt, -d*kt],
                     [ 0.0,                    kr,    0.0 ],
                     [ 0.0,                    0.0,   kz  ]])
d = 1.0
denom = (1-d)*KS + d*(KT+KT)
qual3 = []
for node, name in [(0,"x"),(1,"r"),(2,"z")]:
    if node==0: gain=1.0
    else: gain = (d*KT)/denom if denom>0 else 0.0
    a2 = gain>GAIN_CUT; b2 = node!=0
    q = a2 and b2
    print(f"   node {name}: clamp_gain={gain:.3f}  2a={a2}  2b={b2}  qualifies={q}")
    if q: qual3.append(name)
print(f"   distractor case: qualifying model node(s) = {qual3}")
print(f"   -> aliveness DETECTED (a decoupled model exists): {len(qual3)>=1}")
print(f"   -> node ATTRIBUTION unique from (2a)+(2b)+V alone: {len(qual3)==1}  "
      f"(r and z are symmetric, both hold mu*; V cannot rank them)")

print("\n## VERDICT (frozen criteria)")
print(f"   Q1={Q1}  Q2={Q2}  Q3(base, singles out r w/o label)={Q3_base}")
two_sided = Q1 and Q2 and Q3_base
print(f"   => {'TWO-SIDED DETECTOR up to the standing V-declaration' if two_sided else 'NEGATIVE-ONLY / SECOND-DECLARATION'}")
print( "   Scoping caveat (stress test): DETECTION of aliveness needs no node label, but with")
print( "   more than one decoupled reference, NODE ATTRIBUTION is non-unique from (2a)+(2b)+V")
print( "   alone (symmetric references) — attribution, not detection, would need a further")
print( "   declaration. Report both to prime.")
