"""
AOP gate-stakes analysis: E-vs-Cμ dormancy screen — was the GO exit reachable?

Question: is the screen's NULL (Drive does not force stored time-asymmetry
Ξ = Cμ⁺ − Cμ⁻) a genuine test with a reachable GO exit, or a consistency check
disguised as a test? A gate is a real test only if some system in the
pre-registered class could have triggered GO.

Method: two-knob dissociation on a driven Markov network (3-ring driven by
current parameter a, plus a directional tail with forward/back structural ratio
r; asymmetric read-out). Ξ estimated by the causal-irreversibility routine from
the deposited screen module (validated on positive controls to Ξ≈0.9).

Result:
  Knob 1 (structure r, drive off, σ̇=0):  |Ξ| moves 0 → ~2.0 bits.
      => stored asymmetry is a live, movable axis; GO is reachable in-class.
  Knob 2 (drive a, structure fixed r=3):  σ̇ climbs 0 → 6.55 (×64),  |Ξ| flat ~1.9–2.1.
      => drive does not move stored asymmetry; GO reachable but NOT triggered.

Conclusion: NULL is informative, not tautological. Drive and stored causal
asymmetry are orthogonal knobs. Corroborated by this gate's retracted-GO history
(first-pass GO was the entropy-production estimator, a Drive object; retracted).

Requires the deposited module aop_ecmu_screen.py on the path.
"""
import numpy as np
from aop_ecmu_screen import (general_rate, stationary, entropy_production,
                             causal_irreversibility)

def two_knob(a, r):
    """3-ring driven by a; directional tail 0-3-4 with fwd/back ratio r."""
    fwd, bwd = np.sqrt(r), 1/np.sqrt(r)
    e = {(1,0):np.sqrt(a),(0,1):1/np.sqrt(a),(2,1):np.sqrt(a),(1,2):1/np.sqrt(a),
         (0,2):np.sqrt(a),(2,0):1/np.sqrt(a),
         (3,0):fwd,(0,3):bwd,(4,3):fwd,(3,4):bwd}
    return general_rate(e, 5)

EMIT=[0,1,0,1,2]; DT=0.2; D=4; Lf=4

if __name__ == "__main__":
    print("KNOB 1 — structure (a=1, σ̇=0):  r, σ̇, |Ξ|")
    for r in [1.0,1.25,1.5,2.0,3.0,4.0,6.0]:
        R=two_knob(1.0,r); p=stationary(R)
        _,_,Xi=causal_irreversibility(R,EMIT,DT,D,Lf)
        print(f"  r={r:4.2f}  sigma_dot={entropy_production(R,p):+.3f}  |Xi|={abs(Xi):.4f}")
    print("KNOB 2 — drive (r=3 fixed):  a, σ̇, |Ξ|")
    for a in [1.0,2.0,4.0,8.0,16.0,32.0,64.0]:
        R=two_knob(a,3.0); p=stationary(R)
        _,_,Xi=causal_irreversibility(R,EMIT,DT,D,Lf)
        print(f"  a={a:5.1f}  sigma_dot={entropy_production(R,p):6.3f}  |Xi|={abs(Xi):.4f}")
