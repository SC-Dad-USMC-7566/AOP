# AOP Gate — Does a Pure Current Move Lifetime-Persistence? (PRE-REGISTRATION)

**Status: pre-registration. Exits frozen before computation. Two exits only: GO / NULL.**
_Drafted 2026-07-16. Runs the crux flagged in HANDOFF_AOP #2. This session earlier concluded
"a pure dissipative current has zero leverage on persistence." That was tested on 1-D
birth-death chains (which by topology carry NO cycle current) and measured OCCUPANCY (stationary
mass in the viable set). This gate tests the claim where it can actually be tested: a driven
RING (real cycle current) with LIFETIME (mean first-passage time to erasure) as the primitive._

## Object (frozen)
N-site ring. Stationary distribution pi (a well = viable basin) and dynamical activity profile
t_i BOTH held fixed; a divergence-free current J is the only remaining knob. Exact construction:
w+(i)=(t_i+J)/(2 pi_i), w-(i+1)=(t_i-J)/(2 pi_{i+1}); pi and t invariant for all J (t_i>|J|).
Lifetime = MFPT from the well peak to the absorbing erased state.

## Exits (frozen)
- GO: lifetime changes materially (>20% over the accessible J range) at fixed pi and fixed t.
  => a pure current HAS direct leverage on lifetime-persistence; the session's zero-leverage
  line is scoped to occupancy and to acyclic topologies.
- NULL: lifetime invariant to J at fixed pi and t. => the zero-leverage line generalizes.

## Why both reachable
NULL reachable: if lifetime were a pi-functional it would be fixed like occupancy. GO reachable:
kinetic first-passage depends on the full generator, not pi alone. We report whichever falls.
