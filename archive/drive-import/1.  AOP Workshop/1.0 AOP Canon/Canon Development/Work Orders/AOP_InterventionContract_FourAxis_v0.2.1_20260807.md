# AOP Intervention Contract — four axes (v0.2.1)

**Issued:** 2026-08-07 · **Status:** PROPOSAL, built to be attacked. Non-canon. Authorizes no canon edits.
**Supersedes:** v0.2 (`AOP_InterventionContract_FourAxis_v0.2_20260807`) **for gate execution.** The typed-family architecture and Ben's three rulings (Memory-A + Markov ladder, typed family, Boundary rename) are **unchanged** — Aster provisionally accepted the architecture and found the §9 gate not yet *executable*. v0.2.1 is a narrow **specification-readiness repair** implementing Aster's eight technical items, not a re-architecture.
**Purpose:** Make the §9 gate executable by an independent seat. §11.2 stays **OPEN**; it closes only when an independent seat runs the repaired gate and it survives.
**Built by:** Claude Cowork (execution seat). **Not self-certified.** The seat that built this does not run the gate on it.

**Session/governance status is not in this document** (Aster item 8). It lives in `AOP_Status_ContractV021_SessionAndCanon_20260807`. This file is the scientific contract only.

---

## 0. Architecture (unchanged from v0.2)

Four typed causal contrasts sharing one outcome and one reporting discipline; **no single four-axis estimand.** Two intervention types, mapped to K&W's verified stored/observed split:

- **Type A — initial-state.** Scramble a declared joint at t=0, run the dynamics forward (K&W *stored*, Eq 5.2 / §5.1.1).
- **Type B — mechanism.** Intervene on the generator without changing the initial distribution (K&W *observed*, Eq 5.14 / §5.2, adapted).

**Three core contrasts + one internal-cut extension** (terminology fixed, used consistently below, Aster item 7):

| Contrast | Type | Quantity | Status |
|---|---|---|---|
| **Boundary** | A (external cut) | CBSD = I(in;out) | core |
| **Memory** | B (mechanism) | E = I(past;future) | core |
| **Drive** | B (mechanism) | σ = path asymmetry vs R | core |
| **Integration** | A (internal cut) | Type-A operation on an internal partition | **internal-cut extension** (not a co-equal fourth axis) |

**Common outcome:** ΔV_N = V(N(system)) − V(system), same V and τ across contrasts. **Sign convention (mandatory, stated): intervened − actual.** K&W define semantic value as actual − intervened, so K&W value = −(this contract's ΔV_N); flag the sign on any K&W cross-reference. Zero ΔV = no detected relevance under this declaration, never "axis absent." Sign is an outcome, never a distinctness test (R2).

---

## 1. Finite-window (transient) definitions for the response panels (Aster item 1)

The panels report finite-time trajectories, not stationary scalars. Each axis reading is defined as an explicit finite-window functional of the run-forward (possibly intervened) process. **None of these is a placeholder.**

**1.1 CBSD(t) — transient cross-cut dependence.** Under the declared in/out cut and an initial law μ₀ (actual or Type-A-scrambled), run the dynamics forward and read the *instantaneous* mutual information across the cut at time t:

> **CBSD(t) = I( X_in(t) ; X_out(t) )**, the MI between the in-block and out-block states of the single-time distribution at t.

At t=0 under the product scramble, CBSD(0)=0 by construction; CBSD(t) for t>0 is the re-correlation the dynamics generate across the cut. Report the curve CBSD(t) on the declared schedule.

**1.2 E_L(t) — finite-window excess entropy.** For window length L and split point t, present-in-past convention (canon §4, condition 5; Crutchfield & Feldman 2003 Prop. 8):

> **E_L(t) = I( X_{t−L+1 : t} ; X_{t+1 : t+L} )** — L-block past (present included) vs L-block future MI at split t.

The stationary excess entropy E is the limit L→∞ on the stationary process; the panel reports the finite (L, t) values actually computed, and states L. On a Type-B (Markov-ladder or Drive) intervention, E_L(t) is read on the *intervened* process. **E_L is defined only for the declared temporal grain** (canon §4: E's *definedness*, not just value, is grain-relative).

**1.3 σ_Δ(t) — finite-window path asymmetry.** For trajectory window length Δ starting at t and declared time-reversal involution R (see §3.3 and the canon §4 parity condition):

> **σ_Δ(t) = (1/Δ) · D_KL( P_{[t, t+Δ]} ‖ R · P_{[t, t+Δ]} )** — the windowed KL divergence between the forward path law on [t, t+Δ] and its R-reversal, per unit time.

As Δ→∞ on a stationary process this → the entropy-production rate σ. The panel reports σ_Δ(t) with Δ and R stated. **σ_Δ is only interpretable once R is declared** — an unreversed σ has not said which involution it is a divergence against (canon §4, condition 3).

These three finite-window functionals ARE the P_k(t) family of §6 — each axis reading as a declared finite-time trajectory.

---

## 2. The common declaration block (mandatory per contrast, no silent defaults)

Unchanged from v0.2 in force; restated fields (a blank field = inadmissible contrast): (1) initial ensemble μ₀; (2) conditioning/support/constraints; (3) V and orientation (larger V = more viable); (4) V type (endpoint / path / first-passage); (5) horizon τ + evaluation schedule; (6) intervention/null N with Type and, for Type B, the mechanism altered and how non-uniqueness is handled; (7) preserved quantities (load-bearing for identity claims, §6); (8) admissibility standard — **four senses** (§7.2), stated per null; (9) **identifiability** — separately declared (§7.3), no longer folded into admissibility; (10) sign convention; (11) estimator + uncertainty, analytic preferred.

---

## 3. Per-contrast specifications

### 3.1 Boundary (core) — Type A — "cross-boundary stored dependence" (CBSD)

Canon Boundary axis untouched; contract-level quantity renamed CBSD, carrying prominently:

> CBSD measures statistical dependence across a declared external cut. It does **not** measure membrane integrity, permeability, insulation, or boundary maintenance. It is the informational *role* of a declared partition, not a boundary *mechanism*.

Quantity CBSD = I(in;out); transient form CBSD(t) (§1.1). Null (Type A): product-scramble μ̂ = μ_in ⊗ μ_out at t=0, run forward. Identity: block-decomposable initial joint → CBSD = 0 **only if the scramble leaves the single-block distributions unchanged** (§6). Hardest issue: admissibility of the product state (§7.2). A separate boundary-*maintenance* quantity is **future work**, not in this contract.

### 3.2 Memory (core) — Type B — E retained, Markov-order projection ladder

Target **E = I(past;future)**, transient form E_L(t) (§1.2). Canon Memory axis preserved.

**3.2.1 Full M_k path-law construction (Aster item 2).**

- **Domain.** A stationary, ergodic process μ on a finite alphabet 𝒜, described by its shift-invariant measure. (The construction is stated for finite 𝒜; continuous-state analogues require a separately declared partition and are out of scope for the benchmark suite.)
- **M_k definition.** The order-k Markov process induced by μ: initial law = the observed k-block marginal μ(x_{1:k}); transition kernel T_k(a | c) = μ( x_{t+1}=a | x_{t−k+1:t}=c ) for every context c ∈ 𝒜^k with μ(c) > 0. M_k is the maximum-entropy process consistent with μ's order-(k+1) block statistics.
- **Initial block law.** μ(x_{1:k}) exactly (for k=0, the empty context: M_0's initial and stepwise law is the single-symbol marginal μ(x_1), i.e. i.i.d.).
- **Zero-probability contexts.** Contexts c with μ(c)=0 lie off the support of the stationary measure. The M_k initial law places no mass on them, and T_k conditions only on realized contexts, so the constructed chain never reaches them; the kernel is left **undefined** there and this is harmless (a measure-zero, unreachable set). State this per model; do not fill zero-context kernels with arbitrary mass, which would perturb the preserved marginals.
- **Preserved marginals.** M_k reproduces μ's block statistics **up to order k+1** (exactly the k-block marginal and the order-k conditionals); it does **not** preserve blocks of order > k+1 in general. **k=0 preserves only the single-symbol marginal → E=0** (the full Memory null). **k≥1 are diagnostic projections**, not nulls.

**3.2.2 Projection residual (renamed, Aster item 2).** Define

> **ρ_k := E(μ) − E(M_k)** — the **projection residual**: the excess entropy removed by the order-k Markov projection.

Do **not** call ρ_k "memory beyond order k" unless that identification is proved or cited. For a genuinely order-m source, ρ_k → 0 for k ≥ m; for infinite-Markov-order processes (HMM/sofic, e.g. the Even Process, §9 model 3), ρ_k stays strictly positive — the ladder never saturates, which is exactly the diagnostic value. Report ρ_k as a residual and let its saturation (or non-saturation) across k be the finding.

**3.2.3 Two curves, never conflated (Ben's ruling).** Structural: E(M_k) and the residual ρ_k. Viability: V(M_k) − V(original). k is an **ordinal/discrete** index; v0.2.1 makes **no** mixture-interpolation claim.

**3.2.4 Selectivity caveat (mandatory).** The k=0 null also drives σ→0 (an i.i.d. process has zero entropy production), by the internal σ>0⇒E>0 theorem (§3.3). This coupling is real and must be reported: the full (k=0) Memory null is **not identifiable against Drive** (§7.3), so its viability effect cannot be uniquely attributed to Memory. The theorem *explains* the off-target effect; it does **not** make the intervention selective. The k≥1 diagnostic rungs are where Memory-specific structure, if any, appears without the total Drive confound.

### 3.3 Drive (core) — Type B

Quantity σ = path/trajectory asymmetry relative to declared reference dynamics R (the reversal involution), transient form σ_Δ(t) (§1.3). Null (Type B): detailed-balance projection — symmetrise the generator at fixed stationary distribution relative to R. Identity: detailed balance / zero net current → σ = 0.

**Envelope flag (do not generalise):** the frozen MFPT "current-shortens-persistence" result holds only for V = small-noise MFPT, fixed stationary distribution; other V can flip the sign. Restate per contrast.

**The R (reversal) declaration is load-bearing**, per canon §4 condition 3: σ is a divergence against a declared involution. For even-variable configuration-space Markov processes (all §9 computable models) the parity condition holds trivially; for states with odd variables (momenta, currents, spins) the internal theorem is explicitly silent — declare R and flag it.

### 3.4 Integration (internal-cut extension) — NOT a co-equal axis

A **state-Integration** contrast is a Type-A product-scramble of an **internal** partition at t=0 — the same operation as Boundary over an internal cut rather than the external one. It is therefore reported as **"the Type-A contrast under internal partition P,"** an extension of the Boundary operation, not an independent measurement. Consequences: the core is **three contrasts + one internal-cut extension**; the cross-axis rank matrix does **not** return as an ontology test (§6); Integration's non-promotion is not a defect of AOP.

---

## 4. Type ↔ K&W map (verified, `AOP_KW2018_Verification_SpineClaims_20260806`)

| Contrast | Type | K&W operation | Null holds fixed |
|---|---|---|---|
| Boundary (CBSD) | A external cut | *stored* scramble, Eq 5.2 | product μ̂, run forward |
| Integration | A internal cut | *stored* scramble (internal cut) | **extension, not co-equal** |
| Memory (E) | B mechanism | *observed*, Eq 5.14, **adapted** | k-block marginal (k=0: 1-block) |
| Drive (σ) | B mechanism | *observed*, adapted | stationary distribution |

Nuance kept: K&W's observed op severs environment→system; Memory severs the system's own past→future. Same operation *type*, different channel. E is an adaptation of the K&W *operation*, not the K&W *quantity* — do not call E "observed semantic information."

---

## 5. The internal σ>0 ⇒ E>0 theorem — corrected citation and scope (Aster item 3)

**Citation correction.** v0.2 attributed σ>0⇒E>0 to Still et al. 2012. **Removed.** Still et al. 2012 (reference [3], thermodynamics of prediction) supports a *different* claim — that dissipated work is proportional to the *nonpredictive* retained information — and is cited for that claim only. It is **not** the source of the σ>0⇒E>0 theorem.

**What the theorem actually is.** An **internal AOP result**, canon v1.27 **§4** ("Drive → Memory: dissipation forces strict memory positivity"). It is a **scoped corollary of the trajectory-irreversibility identity** (reference [1]) combined with the computational-mechanics fact **E=0 ⟺ i.i.d.** (reference [13], Crutchfield & Feldman 2003). Proof direction (verbatim structure from §4): E=0 ⟺ i.i.d. ⇒ (i.i.d. equals its own time-reverse in distribution ⇒) σ=0; the contrapositive is σ>0 ⇒ E>0. The converse fails — a detailed-balance oscillator has σ=0 with E>0 — so it forces **strict positivity, not depth or a magnitude bound.** Computed witness: canon Figure DM, a driven **three-state Markov ring** (which is why §9 model 4 is a three-state ring — it is the canon's own Drive control).

**Precise scope — the five conditions stated in canon §4 (do not run the gate outside them):**

1. **Same complete description.** σ and E read on one complete state; coarse-graining can hide a current (E reads ~0 while the full dynamics dissipate).
2. **Stationarity.** The regime in which σ = D(forward ‖ reverse) is the clean object.
3. **Time-reversal parity.** The i.i.d.⇒σ=0 step needs the stationary one-point law invariant under the reversal involution (holds if all state variables are even under R). **Explicitly silent** for odd variables (momenta, currents, spins) until R is declared for that case.
4. **Strict positivity, not magnitude.** No bound E ≥ f(σ) with f>0 exists: for every s>0 there are stationary, even-variable, single-description Markov chains with σ=s and E arbitrarily close to 0 [deposited]. Content is exactly "sustained dissipation ⇒ not i.i.d."
5. **Contiguous split, present-in-past.** E = I(X_{≤0}; X_{≥1}) (Crutchfield & Feldman 2003 Prop. 8). The excluded-present variant E_gap makes the implication false (a 1-dependent process has E_gap=0 with σ possibly infinite [deposited]).

**Grade and status.** Canon grade: **forced × theorem/corollary**, within the five scope conditions (canon §12 gate ledger). **Kept provisional pending independent audit** (Ben): the theorem rests on reference [1], and [1]'s exact content carries an **open source requirement (C-1** in work-order §10: "[1] describes a single-time phase-space identity, not a stationary trajectory-level rate") — that must be discharged against the primary source before the *paper* leans on the theorem. The gate may use the theorem to *predict* the Drive→Memory off-diagonal (model 4), but reports it as internal-and-provisional, not as an external citation.

---

## 6. Response panels replace the 4×4 selectivity matrix (Aster P5)

Two panels, reported separately, finite-time (§1), never merged into one scalar and never read for ontology:

- **Panel A — initial-state responses.** Each reading's CBSD(t), E_L(t), σ_Δ(t) and V(t) under **Type A** nulls (Boundary external cut; Integration internal-cut extension).
- **Panel B — mechanism responses.** The same finite-time readings under **Type B** nulls (Memory Markov ladder; Drive detailed-balance projection). The forced σ>0⇒E>0 edge (§5) will appear as **real off-diagonal in Panel B by construction on model 4** — the gate seat is told this in advance so it is not "discovered" as a bug.

**Identity control (carry-forward, tightened).** "This null drives this reading to 0" holds **only if the null leaves the baseline distribution unchanged** (preserved-quantities field, §2.7). If the scramble perturbs a single-block marginal, the "→0" identity is approximate; report the residual.

**Do not infer ontology from rank.** The panels report how much each reading moves and co-moves under each typed null. Shared degrees of freedom among the four labels are reported as **measured coupling**, not adjudicated as a count of "real" axes.

---

## 7. Admissibility, identifiability, degeneracy (carry-forwards, repaired)

**7.1 Stationary-marginal degeneracy (check before any contrast runs).** If μ₀ = π (stationary) **and** V is a one-time-marginal functional, a marginal-preserving null gives ΔV = 0 by construction — dead contrast. Escape: path/first-passage/conditioned V **and/or** non-trivial μ₀ (μ₀ ≠ π or conditioned). Every declaration states μ₀, V type, and that this degeneracy is avoided.

**7.2 Admissibility = FOUR senses (identifiability removed, Aster item 7).** Whether an intervened state can exist:

1. **Probabilistic** — a normalizable distribution on the state space.
2. **Constraint** — respects hard constraints (conservation laws, support).
3. **Reachability** — reachable by some dynamics from some prior state.
4. **Implementability** — producible by a physically realizable intervention.

A null that is probabilistically fine but unreachable/unimplementable is a *conceptual* contrast, not a *runnable* one — say which.

**7.3 Identifiability — a SEPARATE check (Aster item 7).** Identifiability is **not** an existence property and is removed from the admissibility list. It asks: **is the resulting ΔV attributable to the declared axis, and not confounded by an off-target effect?** The Memory k=0 / Drive coupling (§3.2.4) is an identifiability failure, not an admissibility failure — the i.i.d. state is perfectly admissible; the *attribution* is confounded. Declared per contrast (field §2.9).

**7.4 Controls — conceptual vs completed.** Rock (equilibrium, all readings ~null), hurricane (high Drive, low informational readings — dissociates Drive from Memory/Boundary), Jupiter (Bartlett's negative control) are **conceptual controls, not completed ones.** None has run through the contrasts end to end. They enter §9 as operationalization targets, flagged conceptual until a contrast runs.

---

## 8. Kill conditions — fatal to co-measurement, NOT to AOP (Aster P6, K3/K5 repaired)

Each condition bounds what the **co-measurement method** can claim; none rejects AOP, whose claims live in the canon independently.

- **K1 — No admissible common V.** No single V serves all contrasts without changing meaning (endpoint-for-one, path-for-another is not one V) → fall back to per-axis V, no common-outcome claim.
- **K2 — Degenerate by construction.** μ₀ and V force ΔV=0 analytically (§7.1) → declaration error, repair before the gate; not a kill of AOP.
- **K3 — Inadmissible null (repaired: admissibility only).** A null fails ≥1 of the **four** admissibility senses (§7.2) on a real model → that contrast is inadmissible **for that model**; report it. (K3 no longer smuggles in identifiability.)
- **K4 — Memory not identifiable from Drive (repaired: identifiability).** The k=0 null is non-identifiable against Drive by §5. If the k≥1 diagnostic rungs **also** fail to isolate any Memory-specific structure across the suite, Memory is not separately measurable under this protocol → report "Memory not dissociable from Drive," a real finding. (This is an **identifiability** kill, §7.3, now cleanly separated from K3's admissibility kill.)
- **K5 — Internal-cut extension collapses (repaired).** If the Integration reading under internal partition P is a **determined function** of the Boundary Type-A operation on that cut (i.e., it adds no information beyond re-running the same stored scramble on a different cut), Integration is not even an independent extension → report as "Integration = Boundary operation under internal cut, no separate content." Not a kill of AOP; it is the expected outcome given §3.4.

Pre-declared dispositions: four-axis family survives; or **three core contrasts + internal-cut extension**; or a named reduction (per-axis methods / Memory–Drive fused). All three are real contributions.

---

## 9. Falsification gate — 8-model benchmark suite, each a complete declared world (Aster items 4, 5, 6)

Every benchmark is a **complete declared world** (μ₀, partitions, V, τ, schedule, admissibility) for the computable models; the two conceptual controls are declared as **incomplete worlds with the missing fields named** (that incompleteness is their status, §7.4). Prefer analytic readings (PIC lesson). **Model 4 is now a three-state driven ring** (was two-state — a two-state Markov chain is always detailed-balanced, so σ=0 identically; it *cannot* be a Drive control, Aster item 4). **Model 3 is now the Even Process** (was a second order-1 chain — redundant with model 2; Aster item 5).

| # | Model | Role | μ₀ | Cut / partition | V (type) | τ, schedule | Admissibility | Computable? |
|---|---|---|---|---|---|---|---|---|
| 1 | i.i.d. source (declared marginal) | all-null reference | δ on a fixed symbol, ≠ π-trivial | trivial single cut | first-passage to a marginal event (path) | fixed τ, per-step | all 4 senses | analytic |
| 2 | Golden Mean process (order-1 HMM) | order-1 Memory control | k-block observed marginal | temporal | E-linked path V | τ = several relaxation times | all 4 | analytic (E≈0.2516) |
| 3 | **Even Process (HMM, infinite Markov order)** | ladder stress test (ρ_k never saturates) | observed block marginal | temporal | E-linked path V | τ multi-scale | all 4 | analytic/simulable |
| 4 | **Driven three-state Markov ring** (canon Fig DM) | Drive control (tunable affinity A) | non-π start (conditioned) | temporal + state | small-noise MFPT (first-passage) — envelope-flagged | τ to first passage | all 4; R = even-variable | analytic (σ, E closed-form on the ring) |
| 5 | K&W coupled system–environment channel | viability-anchored, positive stored value | K&W initial joint | in/out (system/env) | K&W viability V | K&W schedule | all 4; scramble reachability checked | simulable (K&W code) |
| 6 | Anti-chemotactic K&W variant | sign control (ΔV opposite) | as 5 | in/out | K&W V | as 5 | all 4 | simulable |
| 7 | Hurricane-type dissipative structure | Drive/informational dissociation | **incomplete — needs declared μ₀** | **needs declared cut** | **needs V** | **needs τ** | conceptual | **conceptual** |
| 8 | Rock / equilibrium relaxing gas | hard negative control | **incomplete — needs μ₀** | **needs cut** | **needs V** | **needs τ** | conceptual | **conceptual** |

**Model-4 rationale (recorded, Aster item 4).** A two-state Markov chain satisfies detailed balance for *every* rate choice, so its stationary entropy production is identically zero — it can never exhibit σ>0 and is disqualified as a Drive control. The minimal genuine NESS is a **three-state ring** with cycle affinity A = ln( (k₁₂k₂₃k₃₁)/(k₂₁k₃₂k₁₃) ); σ>0 for A≠0, σ=0 at A=0 (detailed balance). This is the canon's own computed Drive control (Figure DM), so model 4 also lets the gate reproduce a canon figure as a cross-check.

**Model-3 rationale (recorded, Aster item 5).** Models 2 and 3 in v0.2 were both order-1 (Golden Mean; 0.9-stay chain) — redundant for the Markov ladder. The **Even Process** (a finite-ε-machine hidden Markov / sofic process) has **infinite Markov order**, so ρ_k > 0 for all finite k: it is the model that tests whether the ladder saturates and whether ρ_k behaves as a residual should. Golden Mean is retained as the order-1 positive control (ρ_k → 0 for k ≥ 1).

**Gate rule.** Run every contrast (Boundary/CBSD, Memory ladder, Drive, Integration internal-cut extension) on **at least the computable models 1–6** end to end; report Panel A and Panel B finite-time curves (§1, §6); check each identity against the §6 control caveat; check each declaration against the §7.1 degeneracy and the four §7.2 admissibility senses; declare identifiability (§7.3) per contrast. Operationalize models 7–8 (complete their declared worlds) as a follow-on; report them as conceptual until a contrast runs.

**Closure.** §11.2 closes when an **independent seat** (Aster or a fresh seat, told to break it) runs this gate and returns either "typed family survives — build the three-core-plus-extension methods paper," or a **named reduction** under K1–K5. **The seat that built v0.2.1 does not run the gate on it.**

---

## 10. Standing carry-forwards preserved (not cancelled)

Budget-framing falsification (four axes → three substitutable currencies failed a pre-registered gate; σ ranged 157% of its mean at fixed persistence) → §3.3, now supported by Baiesi & Maes. Drive→Memory forced edge (§5), reported as Panel-B off-diagonal, C-1 source requirement open. Embarrassment-condition finding (both clauses of §13's resolvability condition forced by positive-definite linear algebra) — a real result, do not let the rewrite erase it. Semantic mask + external benchmark work — where falsifiability currently sits; must survive into the Synthesis Draft or be consciously retired with reasons.

---

*Built by Claude Cowork (execution seat), 2026-08-07, implementing Aster's eight spec-readiness items on the architecture Ben ruled. Non-canon. Authorizes no canon edits. Not self-certified — the §9 gate is run by an independent seat before §11.2 closes. §11.2 remains OPEN.*
