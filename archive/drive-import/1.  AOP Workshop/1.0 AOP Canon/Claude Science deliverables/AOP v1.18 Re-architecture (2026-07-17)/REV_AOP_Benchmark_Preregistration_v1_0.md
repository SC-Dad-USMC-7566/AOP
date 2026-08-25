# AOP Benchmark — Preregistration

**Status:** preregistration for OAI Phase 4, following the OAI Semantic-Intervention Protocol §10 template. Non-canonical. **Compiled:** 17 July 2026.

**What preregistration means here.** The model (`REV_AOP_Benchmark_Model_Specification_v1_0.md`) fixes the ground truth by construction. This document states the **predictions, tests, and GO/NULL/attribution-failure criteria** for whether the AOP semantic-intervention *method* recovers structure that a naive reading gets wrong. The predictions are written to be **falsifiable**: for each, a stated outcome would weaken AOP's favored interpretation. The verdicts are recorded separately (`REV_AOP_Benchmark_Results_v1_0.md`) so the reasoning is auditable as prediction-then-test, not post-hoc.

**A candid note on order.** In this single-session execution the model was validated before this document was written; I have not pretended otherwise. What makes the preregistration meaningful is not clock order but that **each prediction is stated with an outcome that would have falsified it**, and the model was not tuned to force any particular verdict — the parameters were tuned only to place the system in a metastable regime with dynamic range (a precondition for *any* test), not to produce a specific sign or ranking. Where a result could genuinely have gone either way, that is stated in the results doc against this list.

---

## Preregistered objects

- **Mechanism set** G = {A, B, C, R, S1, S2, Z} (see model spec §2).
- **Baseline** K = full model, all mechanisms on.
- **Viability** V(θ,τ) = finite-horizon survival; primary τ=15, family {8,12,15,20,30}; v_min=0.60.
- **Intervention** I-1 deletion primary; effect ΔV(S) = V₀ − V(off on S).
- **Coalition analysis** full table over all 2⁷=128 subsets (exact); Möbius h(S); Shapley φ; minimal failure cut-sets; minimal viability-preserving sets.

## The six preregistered tests (OAI Master Plan Phase 4)

| # | Test | Prediction | Falsifying outcome (would weaken AOP) |
|---|---|---|---|
| **T1** | Can the method discover an apparently strong but viability-inert coupling? | The mechanism ranked #1 by structural strength (rate and MI) is **Z**, whose viability effect ΔV(Z)=0. So structural strength ≠ importance. | If the highest-strength mechanism also had the highest ΔV, strength would suffice and the viability layer would add nothing. |
| **T2** | Can it identify a weak but load-bearing coupling? | **R** has low structural strength (small rate, low MI) but the **largest single-edge ΔV**. | If every load-bearing mechanism were also high-strength, again the viability layer would be redundant. |
| **T3** | Does edge attribution fail exactly when coalition effects dominate? | Single-edge ΔV(A)=ΔV(B)=0 but ΔV(A,B) large: single-edge attribution reports "nothing important" for a pair that is jointly essential. | If single-edge ΔV already flagged A,B as important, there would be no attribution failure to demonstrate. |
| **T4** | Does the hypergraph recover redundant alternatives and synergistic pairs? | Möbius h(A,B)>0 (redundant pair) and h(S1,S2)<0 (synergy pair); minimal cut-sets = {A,B},{R,S1},{R,S2}; a redundant route R⇄{S1,S2} is recovered. | If h-signs were uninformative or the cut-sets did not match the built-in structure, the coalition method would not be recovering ground truth. |
| **T5** | Are conclusions robust across a bounded family of horizons and partitions? | The T1–T4 sign verdicts hold across τ∈{8,12,15,20,30}. | If the verdicts flipped sign within the defensible horizon family, they would be artifacts of one convenient τ. |
| **T6** | Does the four-target panel discriminate regimes a named one-axis comparator merges? | *(Deferred to Phase 5 — rival adjudication. Stated here for completeness; not scored in this document.)* | — |

## Negative and positive controls (OAI protocol §11)

| Control | Purpose | Pass criterion |
|---|---|---|
| **Detailed-balance / passive** | remove the driven asymmetry (ρ=0, f=w): R should become inert | ΔV(R) ≈ 0 when there is nothing to suppress |
| **Inert spectator (Z)** | pipeline check | ΔV(Z)=0 and h(·,Z)=0 exactly |
| **Common-input confound** | z correlates with r via Z but feeds nothing | high MI(z;r) with ΔV(Z)=0 |
| **Redundant bypass ({A,B})** | expose single-edge deletion's blindness to joint necessity | ΔV single=0, ΔV joint large |
| **Synergistic pair ({S1,S2})** | positive control for interaction detection | ΔV(S1)=ΔV(S2)=ΔV(S1,S2), h<0 |
| **Budget-shift** | is an apparent edge effect just changed total input? | ΔV(R) survives compensating influx increase |
| **Inadmissible-intervention (ρ=1.8)** | show a large numerical ΔV can be causally meaningless | large viability change, labeled inadmissible |

## Decision criteria (OAI protocol §13 gates + Master Plan Phase 4 exit gate)

- **GO / non-triviality (the exit gate):** ≥1 preregistered result is **not guaranteed by construction**, **could have failed** under these criteria, and **changes the classification** of at least one mechanism relative to a naive reading. Concretely: T1 or T2 must show a rank *inversion* between structural strength and viability importance (not merely a weak correlation).
- **Coalition competence (Gate D):** the method must detect the redundant-bypass and synergistic-pair controls **without** misreporting them as independent edge effects.
- **NULL:** if structural strength and viability importance are positively rank-correlated (Spearman > +0.5) and single-edge ΔV already flags the jointly-essential pair, the benchmark returns NULL — AOP's viability layer adds no information here, and that is reported.
- **Attribution failure (reported, not hidden):** any mechanism for which the per-edge-weight conditions (isolable, additive, identifiable, stable) fail is reported as "edge attribution unresolved" with the coalition/hypergraph as the primary object — not forced into a number.
- **Model invalidation:** if the generator is not a valid CTMC (rows not summing to zero) or survival is not monotone in τ, the run is void.

## Primary outcomes to report

Raw ΔV(S) for all coalitions; Möbius h(S); Shapley φ; minimal failure cut-sets; minimal viability-preserving sets; Spearman(strength, importance); the horizon-robustness table; every control's pass/fail; and the honest exit-gate adjudication.
