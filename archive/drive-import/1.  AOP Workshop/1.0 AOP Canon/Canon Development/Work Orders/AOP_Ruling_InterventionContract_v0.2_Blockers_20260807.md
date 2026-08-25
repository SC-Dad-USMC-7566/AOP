# Ruling record — Intervention Contract v0.2 blockers

**Date:** 2026-08-07 · **Ruled by:** Ben (chat seat) · **Recorded by:** Claude Cowork (execution seat)

**Context:** Aster's red-team of Intervention Contract v0.1 (see handoff `AOP_Handoff_InterventionContract_v0.2_20260806.md`). The three blockers gating the v0.2 build are now ruled. v0.2 build is unblocked.

## Ruling 1 — Memory axis: Option A, with amendments (canon-touching question; canon PRESERVED)

Keep excess entropy **E = I(past;future)** as the canonical target. Use a precisely defined **Markov-order projection family**:

- **k=0 is the full null:** the i.i.d. process with the same one-time marginal — genuinely forces E=0.
- **k≥1 are partial diagnostic projections** showing how much temporal dependence survives at each retained order.
- Each projection must be **defined canonically** — e.g., the order-k Markov process induced by the observed conditional distribution and preserving the relevant block marginals. "Markov_k" must not be left informal.

**k is an ordinal/discrete intervention index.** Do not claim mixtures between rungs solve continuous severity unless a specific interpolation is defined and shown to preserve the required constraints. Continuous λ is not essential here. (This overrules the execution seat's mixture-interpolation suggestion — correctly: a mixture of Markov_k with the original process is not characterized without proof.)

**Report two separate curves, never conflated:**

- structural: E(M_k), or E(original) − E(M_k);
- viability: V(M_k) − V(original).

**Selectivity caveat (mandatory in v0.2):** the k=0 null also eliminates σ, per the frozen σ>0⇒E>0 result. That coupling is real and must be reported — but it means the full Memory null is **not selective with respect to Drive**, so the resulting viability effect cannot be uniquely attributed to Memory. The theorem *explains* the off-target effect; it does not make the intervention selective.

## Ruling 2 — Typed-family reframe: ACCEPTED

Replace "one estimand" with **"four typed causal contrasts sharing a common outcome and reporting discipline."** The common declaration block is **mandatory for every contrast, with no silent defaults**, and must include at least: initial ensemble, conditioning rule, viability functional and orientation, horizon, measurement schedule, intervention/null, preserved quantities, admissibility standard, sign convention, and uncertainty method.

## Ruling 3 — Boundary identity: BOTH declare and rename

Canon Boundary axis untouched. The contract-level operational quantity is **renamed** to something like **"cross-boundary stored dependence."** State prominently that it measures **statistical dependence across a declared external cut** — not membrane integrity, permeability, insulation, or boundary maintenance. **No** new boundary-maintenance measure in v0.2; parked as future work.

## Standing constraints reaffirmed in the ruling

- Integration remains **unpromoted** (Boundary and state-Integration are the same product-scramble over different cuts).
- The cross-axis rank matrix **does not return** as an ontological-distinctness test.

## Disposition

Revise to **Contract v0.2 as a typed intervention family** per the above + the v0.2 spec in the 2026-08-06 handoff (Aster P1–P7 summary). §11.2 closes only when v0.2 survives the re-run falsification gate against the 8-model suite.
