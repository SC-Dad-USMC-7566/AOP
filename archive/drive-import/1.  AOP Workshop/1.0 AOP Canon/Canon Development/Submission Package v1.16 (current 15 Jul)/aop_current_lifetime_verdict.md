# AOP Gate — Does a Pure Current Move Lifetime-Persistence? VERDICT

**Frozen exit: GO** (pre-registration aop_current_lifetime_prereg.md, v1). A pure divergence-free
current, at fixed stationary distribution AND fixed dynamical activity, cuts lifetime by **5.7x**
(MFPT 12.35 -> 2.17 as J: 0 -> 0.95 t_min) while occupancy is invariant to 1e-14 by construction.

## Result (N=12 ring, well at site 0, erased state at site 6, flat activity t=1)
| J | current | MFPT (lifetime) | ratio |
|---|---|---|---|
| 0.00 | 0.00 | 12.346 | 1.000 |
| 0.20 | 0.20 | 8.627 | 0.699 |
| 0.40 | 0.40 | 5.081 | 0.412 |
| 0.60 | 0.60 | 3.428 | 0.278 |
| 0.80 | 0.80 | 2.572 | 0.208 |
| 0.95 t_min | 0.95 | 2.166 | 0.175 |

Occupancy of the viable arc = 0.9890 for **every** J (pi fixed by construction). So the two
persistence primitives dissociate completely: **current has zero leverage on occupancy and strong
leverage on lifetime.** Sign here is anti-persistent — the current stirs the system over its
barrier faster, shortening lifetime; sign is geometry-set (a current aimed into the well would
lengthen it).

## What this scopes (a correction to this session's own work)
1. The real-system/substitutability gate line "pure Flux has zero leverage on persistence; 
   persistence is a functional of the stationary distribution alone" is **true only for
   occupancy** and only vacuous-ly on acyclic (1-D birth-death) systems. It must be rewritten:
   *occupancy* is a pi-functional (current-blind); *lifetime* is not (current-sensitive).
2. Canon v9's §13 and Table 4 edits (folded earlier this session) inherit that occupancy framing
   and must be scoped to "occupancy-persistence," with the lifetime result recorded alongside.
3. The choice of primitive (occupancy vs lifetime) is foundational and belongs to the top of the
   paper. HANDOFF_AOP reports Ben has chosen **lifetime** (every primitive phrase - resists
   erasure, how long till it decays, the spore lasts - is lifetime language). Under lifetime,
   **Drive regains direct leverage on persistence**, consistent with driven persisters (flames,
   dissipative structures) existing at all.

## Grade: GO, established within the minimal ring. Generalization beyond the ring (higher-D,
real driven systems) is open - do NOT hard-canon the magnitude, only the qualitative dissociation.

## Reproduce
aop_current_lifetime_gate.py (self-contained; ring generator at fixed pi & activity, MFPT solve).
Numbers: MFPT 12.35 -> 2.17 (5.7x); occupancy 0.9890 invariant.
