# AOP — Gate-Stakes Analysis: the E-vs-Cμ Dormancy Screen

_Built 2026-07-16. Addresses the red-team's sharpest content finding: the paper's
headline is "we put our predictions through a two-exit gate," but §10 concedes the
gates are "consistency checks, not tests that could fail." This record asks whether
one gate — the E-vs-Cμ dormancy screen — can be honestly defended as a test with a
**reachable GO exit**, rather than a check rigged to pass._

## The question, made precise

A pre-registered gate is a genuine test only if its GO exit was **reachable**: some
physically-realizable system in the pre-registered class must have been able to
trigger GO. If GO was unreachable — if the NULL followed from a symmetry of the model
rather than from the science — then the "test" is a consistency check wearing a test's
clothes, and reporting it as a passed test overstates the evidence.

The screen tested: **does Drive (entropy production σ̇) force a floor on stored
time-asymmetry** Ξ = Cμ⁺ − Cμ⁻ (the difference between forward and reverse statistical
complexity)? Pre-registered exits: GO if Ξ rises with σ̇; NULL if Ξ is drive-blind.
The screen returned **NULL** — Ξ = 0 at every drive on the driven ring.

**The worry.** On the original driven-ring model, time-reversal is just the ring
relabeled in the opposite direction, so Ξ = 0 is nearly forced by a symmetry. If that
were the whole story, GO was never reachable and the NULL is empty.

## The decisive experiment: a two-knob dissociation

Build a driven system **without** that reversal symmetry — a 3-ring driven by current
parameter `a`, plus a directional tail with structural forward/back ratio `r`, read out
through an asymmetric lump. Here reversal is *not* a relabeling, so Ξ is a-priori free
to be nonzero and free to track drive. Then move each knob independently, with Ξ
estimated by the same causal-irreversibility routine the corrected screen uses
(validated on positive controls to Ξ ≈ 0.9).

### Knob 1 — structure (drive off, σ̇ = 0)

| structural asymmetry r | σ̇ | \|Ξ\| (bits) |
|---|---|---|
| 1.00 | 0 | 0.000 |
| 1.25 | 0 | 0.293 |
| 1.50 | 0 | 0.626 |
| 2.00 | 0 | 1.247 |
| 3.00 | 0 | 1.931 |
| 4.00 | 0 | 2.046 |
| 6.00 | 0 | 1.818 |
| 8.00 | 0 | 1.631 |

\|Ξ\| rises steeply, **peaks near r ≈ 4 (~2.05 bits), then rolls off** at larger r
(1.82 at r=6, 1.63 at r=8) — the read-out lump saturates and begins to blur the
forward/reverse morph distinction, so the *estimate* of stored asymmetry declines
even as the underlying structural asymmetry keeps growing. The non-monotonicity does
not bear on the stakes question: the point is that stored asymmetry is a **live,
movable axis** that structure drives across a ~2-bit range. It is not pinned at zero
by construction. With zero drive, structure alone drives \|Ξ\| across a ~2-bit range (0 to a ~2.05-bit peak near r≈4; see the rollover note below). The estimator is not pinned at zero by construction — **GO
is reachable within the pre-registered model class.**

### Knob 2 — drive (structure fixed, r = 3)

| drive a | σ̇ | \|Ξ\| (bits) |
|---|---|---|
| 1 | 0.000 | 1.931 |
| 4 | 0.416 | 1.902 |
| 16 | 2.079 | 2.018 |
| 32 | 3.799 | 2.072 |
| 64 | 6.550 | 2.099 |

**Drive does not move it.** As σ̇ climbs ×64, \|Ξ\| holds flat at 1.9–2.1 bits (the ~9%
drift tracks the small growth of Cμ itself, not any growth in asymmetry). The gate's GO
exit was reachable and **was not triggered**.

## Verdict: the NULL is a real result

1. **GO was reachable.** Knob 1 exhibits a system in the pre-registered class carrying
   ~2 bits of stored time-asymmetry. A world in which Drive forced stored asymmetry
   would have shown Ξ rising with σ̇ under Knob 2. It did not.
2. **The NULL is informative, not tautological.** Drive and stored causal asymmetry are
   **orthogonal knobs**: one moves Ξ with no drive, the other moves σ̇ with no Ξ
   response. This orthogonality *is* the content of the D→M scoping — the Drive floor
   reaches predictive memory (excess entropy E) and stops there; it does not reach the
   time-asymmetry of stored complexity.
3. **The retracted-GO history corroborates it.** This gate already swung once: its
   first-pass GO was retracted when the "memory-irreversibility" quantity was shown to
   be the Roldán–Parrondo entropy-production estimator — a Drive object, not a memory
   object. A gate that both retracted a false GO and has a demonstrably reachable
   true-GO exit is the structural opposite of a rigged check.

## What this does and does not license

- **Does:** the E-vs-Cμ screen can be reported in the paper as a test with a reachable
  GO exit, not merely a consistency check. The §10 concession can be narrowed: at least
  one gate is defensibly a test that could have failed, on an argued-reachable exit.
- **Does not:** the model class remains toy Gaussian/Markov, and reachability is argued
  *within* that class. This does not elevate the gate to a test against nature. The
  honest framing is "a pre-registered test with a reachable alternative outcome on a
  minimal model," which is stronger than "consistency check" and weaker than "empirical
  test." F2 (nested-level / non-stationary Φ) remains the open route to real empirical
  stakes.

## Reproduce

`aop_gate_stakes.py` (requires the deposited `aop_ecmu_screen.py`); figure
`figS7_gate_stakes.png`.
