# AOP Intervention Contract — four axes (v0.1)

**Document:** `AOP_InterventionContract_FourAxis_v0.1_20260806`
**Issued:** 2026-08-06 · **Seat:** chat-discussion → Cowork build · **Status:** PROPOSAL, built to be attacked. Non-canon. Authorizes no canon edits.
**Purpose:** The pre-Phase-2 gate for §11.2 of `AOP_WorkOrder_SynthesisRebuild_v3`. It converts "is the interventional spine one method?" from an abstract question into a falsifiable specification. The spine decision closes on whether this contract *survives a falsification pass* — not on any prior argument.
**Provenance:** Synthesised from the Claude–Ben spine discussion (this session) and Aster's two reviews of 2026-08-06 (`REV_AOP_InterventionalSpine_PlanEvaluation`, `REV_AOP_HonestAssessment`). Two of Claude's earlier spine arguments were retracted under Aster's critique and the retractions are carried below. Not self-certified.

---

## 0. What this contract commits to, up front

The spine is **not** "one intervention across four axes." It is **one estimand and one reporting discipline across a grammar of four axis-specific interventions that act at different counterfactual levels.** The unity is in the readout and the audit, not in the operation.

**The common estimand.** For a declared axis *A*, a declared viability functional *V*, a declared horizon *τ*, an admissible null operation *N_A*, and a severity parameter *λ ∈ [0,1]* (0 = untouched, 1 = full null):

> **ΔV_A(λ) = V( N_A(system; λ) ) − V( system )**, evaluated on the same *V* and *τ* for all four axes.

Both signs are permitted. **ΔV_A = 0 means no detected viability relevance under that declaration, null, horizon, and model — not that the axis is absent.** Sign is an *outcome to report*, never evidence for the ontology (retraction R2, §0.1).

**The two intervention levels (organising heuristic).**

| Level | Axes | Object intervened on | Why it matters |
|---|---|---|---|
| State-distribution | **Boundary, Integration** | the joint state distribution at the intervention instant, then run the real dynamics forward | K&W's stored-information scramble applies; the main risk is *admissibility* of the scrambled state |
| Dynamical / generator | **Memory, Drive** | the transition kernel / generator | no state-scramble is admissible; the null is unavoidably *mechanistic* and typically *non-unique* |

This carve is a heuristic, not a theorem: **Integration straddles** (it can be tested at either level), and it *predicts the hard cases* — the dynamical axes (Memory, Drive) are where a clean mathematical null can fail to correspond to any realisable intervention. Use it to order the work, not to flatten the differences.

### 0.1 Two retractions carried from the spine discussion

- **R1 — "three static cuts share one operation" is withdrawn.** Boundary and Integration are synchronic cuts and admit an initial-condition scramble; **Memory is diachronic** and does not — a scrambled past–future joint may correspond to no realisable process. Memory's real intervention is on the dynamics/channel, which files it with Drive. [Aster V1, accepted.]
- **R2 — "Drive's opposite sign proves the axes are distinct" is withdrawn.** K&W permit the viability value of information to be **negative**, so an informational scramble can also raise viability; Drive does not own the negative side of the ledger. Opposite sign shows only that two interventions differ *in effect on one system under one V* — not independence, irreducibility, or correct individuation. **Distinctness is tested by the selectivity matrix (§5), not by sign.** [Aster V2, accepted.]

---

## 1. Axis contract — BOUNDARY  *(state-distribution level)*

| # | Field | Specification |
|---|---|---|
| 1 | Declared axis quantity | B = I(inside ; outside), the synchronic mutual information across the declared boundary at the intervention instant: D( p(in,out) ‖ p(in)p(out) ) |
| 2 | Declaration required | the inside/outside partition (the boundary); intervention time; state representation; *V*; *τ* |
| 3 | Object intervened on | the joint state distribution at the intervention instant (initial-condition intervention) |
| 4 | Null operation *N_B* | replace p(in,out) → p(in)·p(out), then run the **original** coupled dynamics forward to *τ* (K&W stored-information scramble across the spatial cut) [K&W operation — **UNVERIFIED**, §7] |
| 5 | Held fixed | marginals p(in), p(out); the generator; *V*, *τ* |
| 6 | Permitted to change | cross-boundary correlation (→0 at the instant) and everything the real dynamics regenerate from the decorrelated state |
| 7 | Admissibility constraint | the product state must lie in the reachable/physical manifold — product-marginal pairings can violate conservation laws or geometry. **Admissibility test mandatory** before the scramble is used |
| 8 | Null uniqueness | unique *as a distribution* given the marginals; if admissibility restricts pairings, the null becomes max-entropy-subject-to-constraints → report the **null family / robustness interval** |
| 9 | Viability functional & horizon | the common declared *V* over *τ* (same across all four axes) |
| 10 | Signed estimand | ΔV_B(λ). Negative → cross-boundary correlation is viability-supporting; positive → anti-viable; zero → not load-bearing under this declaration |
| 11 | Negative control & identity | *identity:* block-decomposable in/out gives ΔV_B = 0. *neg control:* a declared-but-spurious boundary reads ≈0 (K&W rock/hurricane) |
| 12 | Off-target (to other axes) | may move Integration (if in/out overlaps the parts partition) and Memory (decorrelated state alters downstream past–future structure). Measure all four post-null |

**Hardest issue:** admissibility of the product-marginal state. **Kill condition for this axis:** if no admissible decorrelated initialisation exists for the target systems, Boundary drops to the dynamical level (cut the in↔out coupling in the generator) and is re-specified.

---

## 2. Axis contract — INTEGRATION  *(straddles; least mature — on a promotion gate)*

| # | Field | Specification |
|---|---|---|
| 1 | Declared axis quantity | **choose one and declare it** — (a) total correlation / cross-part MI across a declared partition; (b) minimum-cut dependence (canon quantity: MI across the least-disrupting bipartition); (c) predictive information beyond parts / causal irreducibility. **These are different targets** [Aster V6] |
| 2 | Declaration required | the partition into parts; the choice (a)/(b)/(c); for (b) the bipartition search; state representation; *V*; *τ* |
| 3 | Object intervened on | **declare which:** the part-state joint distribution (tests *stored* cross-part correlation) **or** the inter-part couplings in the generator (tests *causal* irreducibility). Different scientific questions |
| 4 | Null operation *N_I* | (state-level) p(part₁…partₙ) → ∏ p(partᵢ), run dynamics forward; **or** (coupling-level) zero the inter-part coupling terms, holding within-part generators fixed |
| 5 | Held fixed | part-marginals; within-part dynamics; *V*, *τ* |
| 6 | Permitted to change | cross-part correlation (state) or cross-part causal flow (coupling); regenerated downstream structure |
| 7 | Admissibility constraint | state-level product may be unreachable (as Boundary); coupling-level factorisation may not name a physical subsystem; retained dynamics may **regenerate** the correlation, so read at the instant or model the regeneration |
| 8 | Null uniqueness | **non-unique on two axes at once:** the partition is generally non-unique *and* (a)/(b)/(c) encode different irreducibility notions. Report partition + measure; if min-cut, report the search and its stability |
| 9 | Viability functional & horizon | common *V*, *τ* |
| 10 | Signed estimand | ΔV_I(λ); interpretation is relative to the declared target |
| 11 | Negative control & identity | *identity:* block-decomposable system → 0 (matches canon min-cut = 0 on block-decomposable). *neg control:* integrated-but-viability-irrelevant system tests selectivity |
| 12 | Off-target | **highest of the four** — a boundary cut is a special bipartition (Boundary overlap), and coupling-level nulls touch Memory/Drive. Expect strong off-diagonal |

**Promotion gate.** Integration is co-equal **only if** it can commit to one target, one intervention level, one partition rule, and pass identity + a selectivity check. **If it cannot: three-axis core (Boundary, Memory, Drive) + Integration as a labelled proposed extension** — do not weaken the whole paper to preserve four-fold symmetry [Aster P5].

---

## 3. Axis contract — MEMORY  *(dynamical / channel level — regrouped here per R1)*

| # | Field | Specification |
|---|---|---|
| 1 | Declared axis quantity | E = I(X_{≤0} ; X_{≥1}) — excess entropy under the **present-in-past split** (frozen canon v1.27) at the declared **time grain** |
| 2 | Declaration required | the split convention (present-in-past); the clock/grain (grain-relative — a star's E differs on thermal vs nuclear clock); state representation; *V*; *τ* |
| 3 | Object intervened on | the temporal channel / transition kernel — **not** a scrambled past–future joint (inadmissible: a scrambled history need not be any process's history) |
| 4 | Null operation *N_M* | intervene on the conditional dynamics so the future is conditionally independent of the deep past given the present — **Markovianise / truncate memory to a declared order**, holding the stationary marginal fixed; sweep retained order as severity λ [K&W dynamic-information operation, adapted — **UNVERIFIED**, §7] |
| 5 | Held fixed | single-time (stationary) marginal; present-state accessibility; *V*, *τ* |
| 6 | Permitted to change | the kernel's higher-order memory structure; E → reduced |
| 7 | Admissibility constraint | the truncated kernel must be a **valid stochastic dynamics with the same stationary distribution**. This is achievable but the null is **mechanistic, not a pure information scramble** — the contract owns that [Aster V1] |
| 8 | Null uniqueness | **non-unique** — many kernels share a stationary distribution and a memory order. Report the null family, or a principled representative (e.g. maximum-caliber) |
| 9 | Viability functional & horizon | common *V*, *τ*, **evaluated on the declared clock** (grain-dependence is real for this axis) |
| 10 | Signed estimand | ΔV_M(λ). Negative → stored predictive memory is viability-supporting. Reading is clock-indexed |
| 11 | Negative control & identity | *identity:* i.i.d. process (E=0) → nulling does nothing (ties to canon E=0 ⇔ i.i.d.). *neg control:* a true order-*k* Markov process → nulling above order *k* does nothing |
| 12 | Off-target | reducing memory order changes the generator → touches **Drive** (σ depends on the kernel) and possibly Integration. Measure all four |

**Hardest issue:** the null is unavoidably mechanistic and non-unique; the binding constraint is "valid kernel at fixed stationary distribution." **Kill condition:** if no admissible memory-truncation preserves the stationary marginal for the target systems, Memory's estimand is not comparable to the state-level axes and must be reported on its own footing.

---

## 4. Axis contract — DRIVE  *(dynamical / generator level)*

| # | Field | Specification |
|---|---|---|
| 1 | Declared axis quantity | σ — entropy-production rate, the path-space asymmetry D(P_forward ‖ P_reverse) per unit time, relative to a declared time-reversal **R** (canon: R is load-bearing) |
| 2 | Declaration required | the reversal R (parity of state variables); the stationary distribution / dynamical class; *V*; *τ* |
| 3 | Object intervened on | the generator / probability current |
| 4 | Null operation *N_D* | **symmetrise the generator** relative to the stationary measure and R — zero the antisymmetric (current-carrying) part, retain the symmetric (detailed-balance) part with the **same stationary distribution**; interpolate current amplitude 1→0 as severity λ |
| 5 | Held fixed | stationary distribution; symmetric part of the generator; *V*, *τ* |
| 6 | Permitted to change | the probability current (→0) — **and, flagged, dynamical activity, local transition rates, residence times, accessibility.** Symmetrising does **not** hold these fixed; report them, do not assume them away [Aster V3] |
| 7 | Admissibility constraint | the reversible projection is canonical only relative to (stationary measure, dynamical class, R); well-defined for Markov generators, needs restatement for other classes |
| 8 | Null uniqueness | unique given (stationary measure, R, generator) — **but only that triple.** Different R → different null. Report R-dependence |
| 9 | Viability functional & horizon | common *V*, *τ*. **ENVELOPE FLAG:** the frozen MFPT theorem (a measure-preserving current can only shorten or leave unchanged the *small-noise mean first-passage time* at fixed stationary distribution) holds for **V = small-noise MFPT only**. For other *V* (throughput, recovery, cycling) the sign of ΔV_D is **not** preordained and may flip [Aster V3; Lee–Seo scope]. State the envelope; never generalise it |
| 10 | Signed estimand | ΔV_D(λ). *Inside* the MFPT envelope, expected ≥ 0 (nulling current raises persistence). *Outside* it, sign is open — and that openness is itself an instance of declaration-sensitivity (choice of *V*), not a universal fact about Drive |
| 11 | Negative control & identity | *identity:* an already-reversible system (σ=0) → nulling does nothing. *neg controls:* canon's hurricane and rock, Bartlett's Jupiter — worked negatives dissociating Drive from the informational axes |
| 12 | Off-target | symmetrising changes the kernel → touches Memory. **Drive→Memory is a *forced* canon edge (σ>0 ⇒ E>0), so expect structured off-diagonal here — not zero.** Measure all four |

**Hardest issue:** the null changes more than the current, and the sign of the effect is *V*-dependent rather than universal. **Kill condition:** if no single *V* makes Drive's estimand comparable to the informational axes without changing *V*'s meaning, Drive is reported as a distinct-footing axis, not a co-measured one.

---

## 5. The distinctness test — cross-axis selectivity matrix

Sign does not establish distinctness (R2). **Selectivity does.** After nulling axis *j* at severity λ_j, measure not only *V* but **all four axis readings** *P_k*:

> **R_jk = ΔP_k / Δλ_j**  (a normalised local or finite-difference response)

- Near-diagonal R → the nulls are selective → the four labels have separable operational content.
- Strong off-diagonal R → the axes are entangled (some are, by construction: Boundary↔Integration overlap; the **forced** Drive→Memory edge).
- **Rank-deficient R → fewer operational degrees of freedom than four labels → the four axes are not four.** This is a real, publishable finding, not a failure.

No outcome is fatal; each is interpretable. This matrix — not the sign ledger — is the empirical content of the claim "these are genuinely different axes."

---

## 6. The two audits — kept separate

Conflating these was a defect in Claude's earlier framing [Aster V5, accepted]. They are orthogonal knobs and must be run as two analyses:

- **Declaration-sensitivity** — vary *what is measured*: boundary/partition, horizon *τ*, viability set, state coarse-graining, time grain, reversal R. Tells you whether a reading is observer-relative.
- **Null-sensitivity** — hold the declaration fixed, vary *how it is tested*: the admissible counterfactual within the null family (§§1–4, field 8). Tells you whether a reading is fragile to an arbitrary counterfactual.

A result that is declaration-robust but null-fragile (or vice versa) means very different things. The paper cannot report "sensitivity" as one number.

**"The audit is the paper" is a hypothesis until it is an operational method** [Aster V4, accepted]. To earn a standalone contribution the audit must answer: which declarations are varied and over what admissible neighbourhood; which conclusions must remain stable; what counts as a declaration-robust axis reading; how partition-induced discontinuities are handled; how declaration-sensitivity is separated from data/null uncertainty. Merely noting that declarations matter is **not** novel — K&W already noted it [**UNVERIFIED**, §7].

---

## 7. Verification & prerequisite ledger (forward discipline)

No claim about a source's internals is treated as settled here until the passage is read. Tagged items block nothing in *drafting this contract* but **block the methods paper**:

- **[UNVERIFIED] K&W two operations.** That K&W 2018 use (i) an initial system–environment product-scramble for stored information and (ii) a conditional-dynamics intervention for information flow. Load-bearing: it is *why* Memory groups with Drive (R1). Carried from Aster + recollection. **Retrieve K&W 2018 and read the relevant section before Phase 2.**
- **[UNVERIFIED] K&W signed value.** That K&W permit the viability value of information to be negative. Load-bearing for R2. Same retrieval.
- **[VERIFIED this session] MFPT envelope.** The "current can only shorten/leave-unchanged small-noise MFPT at fixed stationary distribution" result was independently re-derived during the v1.27 fold check and held — **but only in that envelope.** Restate the domain wherever it is used; do not carry it as general.
- **[PHASE 0 — not done] Prior art on the combination.** Causal Leverage Density (Bartlett 2024; Sowinski et al. 2025), causal/interventionist individuality (Bourrat 2023/24), and interventional information decomposition must be swept before any novelty claim. Both Aster docs flag these as central comparators, not peripheral citations. The contract's *contribution statement stays blank until Phase 0 returns.*

---

## 8. Scope gates — when the four-axis paper proceeds

Proceed with the full four-axis method **only if all hold** [Aster P5]:

1. All four axes have an admissible contract (a realisable null, not only a mathematical one).
2. **One** viability functional *V* serves all four without changing its meaning. *(Open risk: Memory's grain-relativity may break a single shared V. If so, that is itself a scope finding to report.)*
3. Each null passes its identity check and its target-removal check (§§1–4, field 11).
4. Off-target effects are measurable (the §5 matrix is computable).
5. At least one worked model runs the entire protocol end to end.

**Fallbacks, pre-committed:** if Integration's contract fails → three-axis core + Integration extension. If Memory cannot be separated from a general mechanism intervention → split state-level and mechanism-level counterfactuals into explicit, separately-reported classes rather than hiding the distinction.

## 9. The falsification pass this contract must survive

Before Phase 2, point an adversary (Aster, or a fresh seat) at this document with instructions to break it, specifically to force one of:

- two axes' nulls are the *same* operation → collapse them (the spine has fewer than four axes);
- no single *V* survives across axes → it is not one method (report as a family with common reporting rules only);
- the §5 matrix is rank-deficient on the worked model → the four labels are not four operational degrees of freedom;
- an axis has no admissible null on the target systems → it exits the co-measured core.

**§11.2 closes when this pass returns** — either "the contract survives, build the four-axis paper," or a named, defensible reduction (three-axis core, or a family-with-common-reporting). Both are real methods contributions; neither is decided here.

---

*End of `AOP_InterventionContract_FourAxis_v0.1`. Built by Claude Cowork from the spine discussion and Aster's reviews, 2026-08-06. A proposal to be attacked, not a result. Not self-certified; authorizes no canon edits.*
