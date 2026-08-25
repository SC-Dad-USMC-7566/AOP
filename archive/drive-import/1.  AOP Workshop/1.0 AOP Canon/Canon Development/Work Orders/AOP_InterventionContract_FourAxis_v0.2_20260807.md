# AOP Intervention Contract — four axes (v0.2)

**Issued:** 2026-08-07 · **Status:** PROPOSAL, built to be attacked. Non-canon. Authorizes no canon edits.
**Supersedes:** v0.1 (`AOP_InterventionContract_FourAxis_v0.1_20260806`), which failed its own single-method gate under Aster's red-team of 2026-08-06. v0.1 is retained on Drive as the record.
**Purpose:** Pre-Phase-2 gate for §11.2 of `AOP_WorkOrder_SynthesisRebuild_v3`. §11.2 closes only when v0.2 survives an independent falsification pass against the 8-model benchmark suite (§9) — not on any argument in this document.
**Built by:** Claude Cowork (execution seat), to rulings handed down by Ben (chat seat) on 2026-08-07 (`AOP_Ruling_InterventionContract_v0.2_Blockers_20260807`). **Not self-certified.** Whoever built this does not bless it; an independent seat re-runs the gate.

---

## 0. What changed from v0.1, and why

v0.1 committed to "one estimand + one reporting discipline across a grammar of four axis-specific interventions." Aster's red-team broke the *one-estimand* half of that commitment on two independent grounds:

- **Memory's null was wrong.** v0.1 nulled Memory by "Markovianise/truncate memory order at fixed stationary marginal." An order-1 Markov chain still carries excess entropy E = I(past;future) > 0 — the Golden Mean process gives E ≈ 0.2516 bits, the symmetric 0.9-stay chain gives E ≈ 0.531 bits (both re-checked this session). So "Markovianise to order 1" does not null E. The null that *does* null E is the order-0 (i.i.d.) projection at the same marginal.
- **Boundary and state-Integration are the same operation.** Both are a product-scramble of a joint distribution at t=0, differing only in *which cut* is scrambled (in/out vs a within-system partition). They are not two independent measurements; they are one operation over two declared cuts. This is fatal to "four independent measurements," and it is why Integration is **not promoted** (§4).

Disposition (Aster's, affirmed by Ben): this is **not a rejection**. It triggers the contract's own pre-declared fallback. v0.2 is a **typed family of four causal contrasts sharing one outcome and one reporting discipline**, not one estimand. What Aster affirmed and v0.2 keeps: the retractions R1/R2, the declaration-vs-null split, the Integration promotion gate (now resolved *against* promotion), and the K&W stored/observed grounding (verified on primary source, `AOP_KW2018_Verification_SpineClaims_20260806`).

---

## 1. Commitment (typed family)

The spine is **four typed causal contrasts sharing a common outcome and a common reporting discipline.** There is no single four-axis estimand. Each contrast is one of two *types*:

- **Type A — initial-state (state-distribution) contrasts.** Scramble a declared joint distribution at t=0, then run the system's own dynamics forward. This is K&W's *stored* operation (Eq 5.2 / §5.1.1). **Boundary** is Type A. State-Integration would also be Type A — which is exactly why it collapses onto Boundary and is not promoted.
- **Type B — mechanism (dynamical/generator) contrasts.** Intervene on the kernel/generator without modifying the initial distribution. This is K&W's *observed* operation (Eq 5.14 / §5.2), adapted. **Memory** and **Drive** are Type B. Their nulls are mechanistic and non-unique.

**Common outcome.** For a declared system, viability functional V, horizon τ, and admissible intervention/null N, every contrast reports the same-shaped quantity:

> **ΔV_N = V(N(system)) − V(system)** — the *intervened minus actual* difference, same V and τ across all four contrasts.

**Sign convention (mandatory, stated explicitly — this is the K&W convention fix).**
This contract uses **intervened − actual**: ΔV_N = V(intervened) − V(actual). Kolchinsky & Wolpert 2018 define semantic value with the *opposite* sign — **actual − intervened** — so that a positive value means the destroyed structure *helped* viability. **The two conventions are negatives of each other.** When cross-referencing a K&W value, flip the sign: K&W ΔV_semantic = −(this contract's ΔV_N). v0.1 already used intervened − actual implicitly; v0.2 makes it explicit and names the relationship to K&W, per Aster's one convention-fix note. Every contrast states its sign convention in the declaration block regardless; the contract-wide default is intervened − actual.

Zero ΔV = **no detected relevance under this declaration/null/horizon/model**, never "axis absent." Sign is an **outcome**, never validation of the ontology, and never a distinctness test (R2).

---

## 2. The common declaration block (mandatory per contrast, no silent defaults)

Aster P2 and Ben's ruling: the failure mode of a typed family is "measure whatever moves and name it the axis." The declaration block is the only thing preventing that, so it is **mandatory for every contrast, with no defaults filled in silently.** A contrast with any field left blank is not admissible. Minimum fields:

1. **Initial ensemble μ₀** — the distribution the contrast starts from, stated explicitly (see the stationary-marginal degeneracy warning, §7).
2. **Conditioning rule / support / constraints** — what is held fixed, what is conditioned on, the support of the intervened distribution.
3. **Viability functional V and its orientation** — the map to viability, and the declared direction: **larger V = more viable.**
4. **V type** — endpoint / path-functional / first-passage (MFPT). Stated, because the type determines whether the stationary-marginal degeneracy bites (§7).
5. **Horizon τ and evaluation schedule** — the time τ, and *when* V is read (single endpoint vs a finite-time schedule; §6 requires finite-time curves P_k(t)/V(t)).
6. **Intervention / null N** — the exact operation, including its Type (A or B) and, for Type B, which mechanism is altered and how the non-uniqueness of the null is handled.
7. **Preserved quantities** — what the null leaves invariant (e.g. one-time marginal, block marginals). **Load-bearing for the identity claims (§5): a block-decomposable identity holds only if the null leaves the baseline distribution unchanged.**
8. **Admissibility standard** — which of the five senses (§7) the intervened state satisfies, and how.
9. **Sign convention** — restate, per §1 (default intervened − actual; flag any K&W cross-reference).
10. **Estimator + uncertainty method** — how ΔV and the axis reading are computed, and how uncertainty is quantified. **Prefer analytic/closed-form over estimated** (the PIC lesson: estimator artifacts on ill-conditioned covariance withdrew a headline result).

---

## 3. Per-axis contracts

Each axis is one typed contrast. Full 12-field declaration blocks are instantiated per benchmark model at build time; the axis-defining content is below.

### 3.1 Boundary — Type A — **renamed: "cross-boundary stored dependence"**

**The identity problem, ruled (Ben, Blocker 3: both declare and rename).** The measured quantity is I(in;out), the mutual information across a declared external cut. **I(in;out) is not the material boundary.** It does not measure membrane integrity, permeability, insulation, or boundary maintenance. To stop every reader from silently reading it as such, the canon Boundary axis is left untouched but **the contract-level operational quantity is renamed to "cross-boundary stored dependence"** (CBSD), and every instance carries the prominent declaration:

> CBSD measures statistical dependence across a declared external cut. It does **not** measure membrane integrity, permeability, insulation, or the maintenance of a boundary. It is the informational *role* of a declared partition, not a boundary *mechanism*.

- **Quantity:** CBSD = I(in;out) under the declared in/out cut.
- **Null (Type A):** product-scramble of the in/out joint at t=0, μ̂ = μ_in ⊗ μ_out, then run the dynamics forward.
- **Identity:** a block-decomposable initial joint → CBSD = 0 — **but only if the scramble leaves the baseline (single-block) distributions unchanged** (§5 caveat).
- **Hardest issue:** admissibility of the product state (§7, five senses).
- **Parked as future work (Ben):** a separate boundary-*maintenance* quantity. Not in v0.2.

### 3.2 Memory — Type B — **E retained, discrete Markov-order ladder** (this was the canon-touching blocker; canon PRESERVED)

**Ruled (Ben, Blocker 1: Option A with amendments).** Keep excess entropy **E = I(past;future)** as the canonical target — it is the citable quantity (Crutchfield & Feldman 2003; predictive information, Bialek et al.) and the frozen σ>0 ⇒ E>0 theorem is *about* E. Do not retarget to a bespoke M_{k,L}; that would orphan the theorem and redefine a just-frozen canon axis.

**The intervention is a precisely-defined Markov-order projection family, indexed by ordinal k:**

- **k = 0 — the full null.** The i.i.d. process with the same one-time marginal as the observed process. This genuinely forces **E = 0**. This, not order-1, is the Memory null.
- **k ≥ 1 — partial diagnostic projections.** The order-k Markov process **induced by the observed conditional distribution and preserving the relevant block marginals** (canonical maximum-entropy Markov projection consistent with the observed order-(k+1) block statistics). These are *diagnostic*, not nulls: they show how much temporal dependence survives at each retained order. "Markov_k" is defined canonically here — it is **not** left informal.

**k is an ordinal/discrete intervention index.** v0.2 makes **no claim** that mixtures between rungs provide a continuous severity path. (This overrules the execution seat's earlier mixture suggestion: a mixture of Markov_k with the original process is not characterized without a specific interpolation shown to preserve the required constraints. Continuous λ is not essential for Memory; the ordinal ladder is the severity path.)

**Report two separate curves, never conflated (Ben):**

- **Structural:** E(M_k), or equivalently E(original) − E(M_k) — memory-beyond-order-k.
- **Viability:** V(M_k) − V(original).

Do **not** read a reduction in E as a viability effect, or vice versa.

**Selectivity caveat (mandatory in every Memory contrast).** The k=0 null also eliminates σ, by the frozen σ>0 ⇒ E>0 result: an i.i.d. process has zero entropy production. This coupling is **real and must be reported.** Its consequence: the full Memory null is **not selective with respect to Drive**, so any viability effect of the k=0 null **cannot be uniquely attributed to Memory.** The theorem *explains* the off-target effect; it does **not** make the intervention selective. (The k≥1 diagnostic rungs are where Memory-specific structure, if any, shows up without the total Drive confound.)

- **Identity:** i.i.d. (k=0) → E = 0.
- **Non-uniqueness:** the null is mechanistic; the canonical induced-Markov construction is the declared choice, stated per contrast.

### 3.3 Drive — Type B

- **Quantity:** σ = path/trajectory asymmetry relative to a declared reference dynamics R.
- **Null (Type B):** symmetrise the generator at fixed stationary distribution (detailed-balance projection relative to R).
- **Envelope flag (mandatory, do not generalise):** the frozen MFPT "current-shortens-persistence" result holds **only** for V = small-noise mean-first-passage-time, fixed stationary distribution. Other V can flip the sign. Restate the domain in every Drive contrast; never generalise it.
- **Forced off-diagonal:** Drive → Memory is a forced canon edge (σ>0 ⇒ E>0, Still et al. 2012), so expect structured coupling into the Memory reading. This is a *carry-forward finding to report*, not a defect to hide (§10).
- **Identity:** detailed-balance / zero net current → σ = 0.
- **Re-verify σ>0 ⇒ E>0 against Still et al. 2012 in the Memory read-thread before the paper cites it** (open source requirement, §8).

### 3.4 Integration — Type A would-be — **NOT PROMOTED**

**Resolved against promotion (Aster, affirmed Ben).** The promotion gate in v0.1 required Integration to commit to one target (total correlation / min-cut dependence / causal irreducibility) and one level, then pass identity + selectivity. It fails the selectivity precondition *by construction*: a **state-Integration** contrast is a product-scramble of a within-system partition at t=0 — the **same Type A operation as Boundary, over a different cut.** Boundary and state-Integration are therefore not two independent axes; they are one operation over two declared cuts.

Consequence for v0.2:

- Integration is **not a co-equal fourth axis.** The core is **three axes** (Boundary/CBSD, Memory, Drive) plus Integration as a **declared-cut extension of the Type A operation**, reported as "the Type A contrast under partition P" rather than as an independent measurement.
- The **cross-axis rank matrix does not return** as an ontological-distinctness test (§6). Rank-deficiency of a response matrix would only re-state the Boundary/Integration collapse we already know analytically; it does not license an ontology claim.

---

## 4. Two intervention types, mapped to K&W (verified)

| Axis (contract quantity) | Type | K&W operation | Null holds fixed |
|---|---|---|---|
| Boundary (CBSD = I(in;out)) | A initial-state | *stored* scramble, Eq 5.2 | run dynamics forward from product μ̂ |
| Integration (Type A, declared cut) | A initial-state | *stored* scramble (different cut) | — **not promoted** |
| Memory (E = I(past;future)) | B mechanism | *observed* dynamic op, Eq 5.14, **adapted** | one-time marginal (k=0); block marginals (k≥1) |
| Drive (σ vs R) | B mechanism | *observed* dynamic op, adapted | stationary distribution |

**Nuance the contract keeps (from the K&W verification note):** K&W's observed intervention severs environment → system flow; Memory severs the system's own past → future. Same operation *type*, different channel. Memory's estimand is an adaptation of the K&W *operation*, not the K&W *quantity* — do not call E "observed semantic information."

---

## 5. Distinctness and identity — what replaces the 4×4 selectivity matrix

v0.1 proposed a 4×4 cross-axis selectivity matrix R_jk and read its rank as the empirical content of "distinct axes." **Removed.** Reasons: (i) with Integration unpromoted, the matrix's most-cited entry (Boundary↔Integration) is an analytic identity, not a measurement; (ii) inferring ontology (how many axes "really" exist) from the rank of a finite-time response matrix is exactly the "don't infer ontology from rank" error Aster flagged (P5).

**Replacement — typed response panels (Aster P5).** Two panels, reported separately, never merged into one number:

- **Panel A — initial-state responses.** How each axis reading and V respond to Type A nulls (Boundary/CBSD, and the Integration declared-cut extension). Finite-time trajectories **P_k(t)** (each axis reading over t) and **V(t)** on the declared schedule, not a single endpoint scalar.
- **Panel B — mechanism responses.** How each axis reading and V respond to Type B nulls (Memory's Markov ladder, Drive's detailed-balance projection). Same finite-time P_k(t)/V(t) reporting.

**Identity claims — the control caveat (carry-forward, tightened).** A block-decomposable identity ("this null drives this axis reading to zero") **holds only if the null leaves the baseline distribution unchanged.** If the scramble also perturbs a single-block marginal, the "→ 0" identity is not clean and must be reported as approximate with the residual quantified. This is a per-contrast check, not an assumption.

**Do not infer ontology from rank.** The panels report *how much each reading moves under each typed null* and *how much co-movement there is* (the forced Drive→Memory edge will show as real off-diagonal in Panel B). They do **not** return a verdict on how many axes exist. That the four labels may share degrees of freedom is reported as a measured coupling, not adjudicated as an ontology.

---

## 6. Kill conditions — fatal to four-axis co-measurement, NOT to AOP (Aster P6)

These conditions, if met on the benchmark suite, kill **the claim that the four axes can be co-measured as a typed family under one V and τ.** They do **not** kill AOP, which owns its claims in the canon independently of this methods contract.

- **K1 — No admissible common V.** If no single viability functional serves all four contrasts without changing meaning across them (V that is endpoint for one axis and path for another is *not* the same V), the family does not close. → fall back to per-axis V, reported as separate methods, no common-outcome claim.
- **K2 — Degenerate-by-construction outcome.** If the declared μ₀ and V force ΔV = 0 analytically (the stationary-marginal degeneracy, §7), the contrast measures nothing. → not a kill of AOP; a declaration error to be repaired before the gate runs.
- **K3 — Inadmissible null on a real model.** If a Type A product-scramble lands on a state no dynamics can reach or implement (fails ≥1 of the five admissibility senses) on a benchmark model, that contrast is inadmissible **for that model** — report it, do not paper over it.
- **K4 — Memory null non-selective everywhere.** The k=0 Memory null is known non-selective wrt Drive (§3.2). If the k≥1 diagnostic rungs *also* fail to isolate any Memory-specific structure across the whole suite, Memory is not separately measurable as a typed contrast → report as "Memory not dissociable from Drive under this protocol," a real finding.
- **K5 — Integration cannot be even an extension.** Already resolved analytically (§3.4); listed for completeness. Integration's failure to promote is not a kill of AOP.

**None of K1–K5 is a rejection of AOP.** Each is a bound on what the four-axis *co-measurement method* can claim. The pre-declared outcomes are: four-axis family survives; or three-axis core + Integration extension; or a named reduction (per-axis methods / Memory-Drive fused). All three are real contributions.

---

## 7. Carry-forwards — admissibility, degeneracy, controls

**7.1 Stationary-marginal degeneracy (must be checked before any contrast runs).** If μ₀ = π (the stationary distribution) **and** V is a one-time-marginal functional, then a null that preserves the marginal gives **ΔV = 0 by construction** — the contrast is dead before it starts. Escape: use a **path-functional or conditioned V** (first-passage, trajectory functional) **and/or a non-trivial μ₀** (μ₀ ≠ π, or conditioned on an event). Every declaration block states μ₀, V type, and whether this degeneracy is avoided. (This is why the declaration block forces fields 1, 4, and 7.)

**7.2 Admissibility = five senses.** An intervened (especially Type A product-scrambled) state is "admissible" only against a stated sense. The five:

1. **Probabilistic** — a normalizable distribution on the state space.
2. **Constraint** — respects the system's hard constraints (conservation laws, support).
3. **Reachability** — reachable by *some* dynamics from *some* prior state.
4. **Implementability** — producible by a physically realizable intervention.
5. **Identifiability** — the resulting ΔV is attributable to the declared axis and not confounded.

A contrast declares which senses its null satisfies. A product-scramble that is probabilistically fine but unreachable and unimplementable is a *conceptual* contrast, not a *runnable* one — say which.

**7.3 Controls — conceptual vs completed.** The rock (equilibrium, all axes ~null) and hurricane (high Drive, low informational axes — dissociates Drive from Memory/Boundary) are **conceptual controls, not completed ones.** Bartlett's Jupiter is a third conceptual negative control. None has been run through the four contrasts end to end. v0.2 does **not** claim them as validated controls; they enter the benchmark suite (§9) as targets to operationalize, flagged as conceptual until a contrast actually runs on them.

---

## 8. Verification ledger

- **[VERIFIED this session, primary source]** K&W two operations (stored/observed) — Eq 5.2/§5.1.1, Eq 5.14/§5.2. Grounds Type A/Type B split. (`AOP_KW2018_Verification_SpineClaims_20260806`.)
- **[VERIFIED this session, primary source]** K&W signed viability value can be negative — anti-chemotactic example, ΔV ≈ −13.7 bits, App. B. Grounds R2 and the sign convention.
- **[VERIFIED this session, re-derived]** Memory counterexamples: Golden Mean E ≈ 0.2516 bits, 0.9-stay chain E ≈ 0.531 bits — order-1 Markov does not null E. Grounds the k=0 ruling.
- **[VERIFIED prior session]** MFPT envelope — small-noise / fixed-stationary / MFPT only. Restate domain, never generalise (§3.3).
- **[OPEN — source requirement]** σ>0 ⇒ E>0 against Still et al. 2012 — re-verify in the Memory read-thread before the paper cites it.
- **[OPEN — Phase 0, not run]** Prior-art sweep: Causal Leverage Density (Bartlett 2024; Sowinski 2025), causal individuality (Bourrat 2023/24), interventional information decomposition. This is a **novelty** question, not a correctness one; the contribution statement stays blank until Phase 0 returns. v0.2's correctness does not depend on it.
- **[OPEN — K&W paper-citation stage]** Direct page-render of the K&W anchors (Eq 5.2, 5.14, App. B) — the verification note used a fetch-pipeline extraction with concrete anchors; a direct eyeball is the cheap final confirmation before the *paper* cites them.

---

## 9. The falsification gate — 8-model benchmark suite (replaces v0.1's single-model gate)

Aster P7: one worked model is not a gate; a co-measurement method must be tried against a **suite** spanning the axes and the dissociations. The suite below is **proposed, built to be attacked.** It mixes **computable models** (analytic or directly simulable — the gate's real load) and **conceptual controls** (§7.3, to be operationalized). Prefer analytic readings throughout (PIC lesson).

| # | Model | Role | Computable? | Expected signature |
|---|---|---|---|---|
| 1 | i.i.d. source (same marginal) | all-null reference | analytic | E=0, σ=0; every null → ~0 ΔV |
| 2 | Golden Mean process (order-1) | Memory positive control | analytic (E≈0.2516) | E>0 at k=0 null, gone by k=1 diagnostic |
| 3 | Near-deterministic 0.9-stay chain | high Memory | analytic (E≈0.531) | large E, survives to higher k |
| 4 | Driven 2-state NESS / ratchet | Drive positive control | analytic/simulable | σ>0; detailed-balance null → σ=0; forced E>0 (edge) |
| 5 | K&W coupled system–environment channel | viability-anchored, positive stored value | simulable (K&W code) | CBSD>0, ΔV<0 under scramble (helps viability) |
| 6 | Anti-chemotactic K&W variant | sign control | simulable | CBSD>0 but ΔV>0 under scramble (anti-viable structure) |
| 7 | Hurricane-type dissipative structure | Drive/informational dissociation | **conceptual** (§7.3) | high σ, low E/CBSD — to operationalize |
| 8 | Rock / equilibrium relaxing gas | hard negative control | **conceptual** (§7.3) | all axes ~null except trivial — to operationalize |

**Gate rule.** The gate runs every contrast (Boundary/CBSD, Memory ladder, Drive, Integration-extension) on **at least the computable models (1–6)** end to end, reports Panel A and Panel B finite-time curves, checks each identity against the §5 control caveat, and checks each declaration against the stationary-marginal degeneracy (§7.1) and the five admissibility senses (§7.2). Models 7–8 enter as operationalization targets; the gate reports them as conceptual until a contrast runs.

**§11.2 closes when an independent seat (Aster or a fresh seat, told to break it) re-runs this gate and returns** either "typed family survives — build the four-axis (three-axis-core-plus-extension) methods paper," or a **named reduction** under K1–K5. Both are real contributions; neither is decided here. **The seat that built v0.2 does not run the gate on it** — nobody grades their own homework.

---

## 10. Standing carry-forwards preserved (not cancelled by the rewrite)

- **Budget-framing falsification** (four axes → three substitutable currencies failed a pre-registered gate; entropy production ranged 157% of its mean at fixed persistence). Carries into §3.3 Drive; now has independent support in Baiesi & Maes.
- **Drive→Memory forced edge** (σ>0 ⇒ E>0). Carried, reported as real off-diagonal in Panel B, re-verify against Still et al. 2012.
- **Embarrassment-condition finding** (both clauses of §13's resolvability condition forced by positive-definite linear algebra; honest fix strikes "could have come out otherwise"). A real result; do not let the rewrite erase it.
- **Semantic mask + external benchmark work** — where the framework's falsifiability currently sits. Must survive into the Synthesis Draft or be consciously retired with reasons.

---

## 11. Session context and next action

Decision 1 (§11.1 canon governance): CLOSED — v1.27 verified + C1/C3 residual sweep, frozen pending Ben's masthead stamp (stamp-ready md5 `43257601…`). Decision 2 (§11.2 methods-paper scope): ACCEPTED; spine now gated on **v0.2** surviving §9. Decision 3 (§11.3 pre-reg deviations) and §10 open-work register: still **OPEN**. Phase 0 prior-art: **not run**.

**Next action:** hand v0.2 to an independent seat to re-run the §9 gate against the computable benchmark models (1–6), operationalize controls 7–8, then Phase 2. §11.2 closes only when v0.2 survives.

---

*Built by Claude Cowork (execution seat), 2026-08-07, to Ben's three rulings. Non-canon. Authorizes no canon edits. Not self-certified — the §9 gate is re-run by an independent seat before §11.2 closes.*
