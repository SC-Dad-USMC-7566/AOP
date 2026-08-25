# AOP B/D/M/I — Proposed Operational Definition Specification

**Version:** v0.1  
**Date:** 4 August 2026  
**Status:** External-review proposal; non-canonical; no source text altered  
**Purpose:** Define Boundary, Drive, Memory, and Integration cleanly; distinguish identification from measurement; and specify what an AOP result may legitimately report.

## Executive Summary

Yes: B, D, M, and I can be defined clearly and identified reproducibly. They cannot honestly be reduced to four free-floating numbers.

The clean solution is a two-layer architecture:

1. **Structural layer:** Does the declared system exhibit selective separation, trajectory irreversibility, temporal predictive dependence, or cross-part nonfactorization?
2. **Persistence layer:** Does an admissible intervention on that structure change the declared persistence functional?

Every axis therefore returns three objects, not one:

- an **identification verdict**: PRESENT / ABSENT / UNDETERMINED;
- a **structural measurement profile**, with uncertainty and declaration sensitivity;
- a **persistence effect**, measured by an admissible intervention against a declared viability or persistence functional.

The four proposed core definitions are:

| Axis | Proposed core definition |
|---|---|
| **Boundary (B)** | The degree to which a declared interface sustains a dynamically distinguishable interior by selectively attenuating exchange or causal influence from a declared exterior over a declared horizon. |
| **Drive (D)** | The degree of time-reversal asymmetry in the declared system dynamics: the entropy produced per unit time, not energy throughput as such. |
| **Memory (M)** | The predictive constraint on the system’s future carried across time by its declared present/past state under a declared observation process and time grain. |
| **Integration (I)** | The degree to which the joint behavior of declared components fails to factor into independent component behaviors over the declared horizon. |

The present readiness is uneven:

| Axis | Readiness | Main issue |
|---|---|---|
| **D** | Green | A valid estimate requires a reversal convention and adequate state observation; partial observations usually provide only a lower bound. |
| **M** | Yellow | Predictive memory is definable; dormant physical organization is not the same quantity and requires a separate recovery-intervention protocol. |
| **I** | Yellow | The target is definable, but there is no canonical scalar; common causes and partition choice must be controlled. |
| **B** | Orange | Current B1 is insufficiently standardized and B2 measures interface mediation, not shielding by itself. Boundary requires a joint contrast-plus-shielding identification rule. |

The most important recommendation is to stop saying that each axis “returns a value.” The correct object is an **AOP assessment package under a frozen declaration**.

## 1. The Common Operational Grammar

### 1.1 Freeze the declaration before examining outcomes

Every assessment begins with the current AOP declaration tuple:

> **D = (S, E, F, P, δt, τ, R, V, I, N)**

where the analyst declares system variables, environment, interface, component/spatial partition, time grain, horizon, reversal convention, persistence functional, admissible intervention class, and normalization.

This proposal adds no new tuple slot. It makes the existing slots operationally binding.

An axis is **UNDETERMINED**, not absent, when the minimum required declaration or data is missing.

### 1.2 Keep four kinds of statement separate

For each axis, AOP must distinguish:

1. **Definition** — the conceptual target.
2. **Identification** — the evidence required to say the target is present.
3. **Structural magnitude** — the proxy panel describing how much or what kind of structure is present.
4. **Persistence effect** — the change in the declared persistence functional after an admissible intervention.

The fourth is not implied by the first three. A strongly dissipative or highly correlated mechanism may be irrelevant to persistence; the existing AOP benchmark’s inert spectator demonstrates exactly this.

### 1.3 Common persistence-effect notation

For an axis-relevant mechanism or coalition C, report:

> **ΔV(C) = V(actual) − V(intervened on C)**

The intervention must satisfy the current internal-edge intervention protocol: identify the changed mechanism, state a physical implementation, state what is held fixed, specify whether resources are fixed or free, preserve or explicitly relax relevant laws/topology, and remain inside the admissible model class.

Interpretation:

- **ΔV > 0:** the targeted structure is persistence-supporting in the declared regime.
- **ΔV = 0 within uncertainty:** structurally present but persistence-inert under that intervention.
- **ΔV < 0:** the targeted structure is persistence-opposing in the declared regime.
- **No admissible intervention:** persistence role UNDETERMINED.

This sign must be measured. It must never be assumed from the axis magnitude.

## 2. Boundary (B)

### 2.1 Definition

> **Boundary is the degree to which a declared interface sustains a dynamically distinguishable interior by selectively attenuating exchange or causal influence from a declared exterior over a declared horizon.**

This definition deliberately requires both **difference** and **shielding**.

- Difference without shielding is merely a gradient.
- Shielding without a nontrivial interior is an inert enclosure.
- A membrane is one possible mechanism, not the definition.
- Active maintenance is optional: a passive potential well or shell may bound at negligible ongoing cost.

### 2.2 Identification rule

Boundary is PRESENT only when all four conditions are met:

1. **Declared cut:** interior X_in, interface F, and exterior X_out are specified.
2. **Nontrivial contrast:** at least one commensurable state variable differs across the cut or from the declared open-interface/equilibration reference.
3. **Selective attenuation:** the interface reduces transmission of at least one declared exterior perturbation or flux into the interior relative to a declared bypass/open-interface control.
4. **Temporal persistence:** the contrast and attenuation persist over the declared horizon τ.

Boundary is ABSENT when a valid assay shows no contrast or no attenuation. It is UNDETERMINED when there is no commensurable contrast variable, no perturbation/bypass control, or no time-resolved evidence.

### 2.3 Core measurement profile

Boundary should be reported as a mandatory pair, not one scalar:

#### B-C — Contrast

Measure the difference between the actual interior state distribution and a declared reference:

> **B_C = D[p(X_in) || p_ref(X_in)]**

The divergence D may be Jensen–Shannon, Wasserstein, or a domain-specific standardized contrast. The reference must be stated. Preferred references are the same interior with the interface opened/removed, or the equilibrated state under the same external conditions.

Comparing p(X_in) directly with p(X_out) is valid only when they are distributions over the same observable, units, support, and grain. Otherwise the comparison is undefined, not low.

#### B-S — Shielding

Measure attenuation of a declared environmental perturbation:

> **B_S = 1 − Response_in(interface intact) / Response_in(interface bypassed or open)**

The response may be a transfer function, causal effect, flux, concentration change, temperature change, or failure probability. Report the response curve across perturbation magnitude and frequency when possible. B_S is mechanism- and perturbation-specific, not a universal property of the object.

### 2.4 Diagnostic companions

- **B-Mediation:** I(X_in; X_out | F). A low value supports the claim that dependence is mediated by the declared interface. It does **not** by itself measure shielding or boundary strength.
- **B-Leak:** permeability or flux across F under a declared gradient.
- **B-Cost:** housekeeping entropy production required to hold the contrast against leak. This is a Drive→Boundary cross-loading, not Boundary’s defining magnitude.
- **B-Dependence:** I(X_in;X_out), retained only as descriptive cross-cut dependence. High cross-cut dependence is not strong separation.

### 2.5 Persistence measurement

Intervene by opening, bypassing, selectively permeabilizing, or disabling maintenance of F while holding declared controls fixed. Measure ΔV_B over the declared horizon.

Do not infer from ΔV_B that the chosen cut is the uniquely correct system boundary. The result says only that this interface is load-bearing for the declared persister and functional.

### 2.6 Current defect repaired

The current canon correctly rejects I(inside;outside) as boundary strength and elevates B1/B2. But B1 remains underspecified, and B2 is a conditional-independence/mediation diagnostic rather than an attenuation measure. The proposed contrast-plus-shielding pair gives Boundary axis-defining content that does not collapse into Integration or Drive.

## 3. Drive (D)

### 3.1 Definition

> **Drive is the degree of time-reversal asymmetry in the declared system dynamics: the entropy produced per unit time under a declared reversal convention.**

Drive is not energy input, fuel flow, useful work, or activity alone. Those quantities describe sources, sinks, and functions of a driven process. The axis itself is irreversibility/dissipation.

### 3.2 Identification rule

Drive is PRESENT when the forward trajectory ensemble is statistically distinguishable from its declared time reverse beyond uncertainty:

> **P_fwd[trajectory] ≠ P_rev^R[trajectory]**

Equivalent evidence includes broken detailed balance with nonzero stationary probability currents in a properly specified Markov model.

Required declarations:

- observed state variables;
- time grain δt;
- stationarity or finite-horizon regime;
- reversal convention R, including parity of variables;
- treatment of hidden degrees of freedom.

A positive lower bound identifies Drive as present. A zero estimate from partial observations does not establish absence because coarse-graining can hide dissipation.

### 3.3 Core measurement

The core quantity is entropy-production rate:

> **σ = lim(T→∞) (k_B/T) D_KL(P_fwd[0:T] || P_rev^R[0:T])**

For a stationary continuous-time Markov chain, the standard flux/affinity form may be used when the full rate matrix and stationary distribution are available.

Report:

- physical σ when thermodynamic calibration is available;
- trajectory-KL estimate as a **lower bound** when only a partial time series is observed;
- confidence interval, estimator bias, state completeness, and grain sensitivity.

### 3.4 Diagnostic companions

- resource/exergy input rate;
- useful maintained work or flux;
- housekeeping entropy production;
- excess/nonadiabatic entropy production in transient regimes;
- cycle affinities and currents.

These quantities explain the architecture of Drive. They are not substitutes for σ and should not be pooled into a “Drive score.”

### 3.5 Persistence measurement

Perturb a declared current, affinity, fuel source, or dissipative mechanism while controlling geometry and other flows as far as physically possible; then measure ΔV_D.

The sign is open. Drive may support, oppose, or leave persistence unchanged in different regimes. AOP’s own fixed-stationary-distribution current gate is a direct warning against treating σ as automatically pro-persistence.

## 4. Memory (M)

### 4.1 Definition

> **Memory is the predictive constraint on the system’s future carried across time by its declared present/past state under a declared observation process and time grain.**

This definition is deliberately narrower than “stored physical organization.” Memory is a property of a stochastic process under an observation channel. A molecule, genome, spore, or crystal does not have a Cμ or E until the observable and process have been declared.

### 4.2 Identification rule

Memory is PRESENT when knowledge of the declared system history improves prediction of its future over a no-history baseline at one or more nonzero lags.

Minimum requirements:

1. declared observable X and observation channel;
2. declared time grain and lag/horizon;
3. adequate time-series or transition-model evidence;
4. a stationarity claim for asymptotic excess entropy, or an explicitly local/finite-horizon alternative;
5. environmental/common-driver controls when the claim is **endogenous** memory rather than mere temporal predictability.

Memory is ABSENT only when a sufficiently powered assay finds no predictive improvement across the preregistered lag range. Without an observation process or under unresolved nonstationarity, it is UNDETERMINED.

### 4.3 Core measurement profile

#### M-P — Predictive dependence

For a stationary declared process:

> **E = I(X_≤0 ; X_≥1)**

This is the mutual information between semi-infinite past and future. In empirical work it is estimated with finite blocks and an explicit convergence analysis.

For controlled next-step analysis, use active information storage or conditional predictive gain, for example:

> **AIS = I(X_past ; X_t+1)**

When external input histories are observed, report the conditional gain attributable to system history beyond those inputs. The exact conditioning set must follow the causal design; no universal conditioning formula removes every common driver.

#### M-R — Retention profile

Report predictive information as a function of lag or block horizon rather than only its integral:

> **M_R(ℓ) = predictive information retained at lag ℓ**

The curve distinguishes shallow persistence from deep retention even when two systems have similar E.

#### M-C — Predictive-state complexity

When an ε-machine or equivalent predictive-state model is justified:

> **Cμ = H[predictive causal state]**

Cμ measures the information required by the minimal predictive model of the declared process. It is not the mass, molecular complexity, or physical storage capacity of the system.

### 4.4 Dormant or latent organization

The spore problem cannot be solved by relabeling physical structure as high Cμ. A dormant structure may show little ongoing E while retaining recovery-relevant constraints.

Treat this as a distinct **latent-memory assay**:

1. define a standardized activation/recovery protocol;
2. selectively damage, scramble, or remove candidate stored structures;
3. measure the loss in recovery probability, recovery time, or restored function;
4. report the coalition of stored structures required for recovery.

This produces a persistence-relative memory result. It does not create a free-standing information quantity unless an encoding/decoding channel is separately specified.

### 4.5 Persistence measurement

Intervene on a predictive state, memory-bearing mechanism, or latent recovery structure while preserving non-memory dynamics as far as admissible. Measure ΔV_M.

Do not infer semantic importance from E, AIS, or Cμ alone. Predictive information may be redundant, externally driven, or irrelevant to the declared persistence criterion.

### 4.6 Current defect repaired

The current panel correctly distinguishes E, Cμ, active information storage, retention depth, and semantic memory. Its risk is that “one panel” can still imply that all five are measurements of one homogeneous magnitude. They are not. The proposed specification makes E/AIS/retention the structural core, Cμ a model-complexity companion, and dormant physical organization an intervention-based latent-memory protocol.

## 5. Integration (I)

### 5.1 Definition

> **Integration is the degree to which the joint behavior of declared components fails to factor into independent component behaviors over the declared horizon.**

This is a nonfactorization target. It does not by itself establish consciousness, individuality, autonomy, causal closure, or “one true whole.”

### 5.2 Identification rule

Integration is PRESENT only relative to a declared component partition. A strong identification requires:

1. a joint distribution or joint dynamical model over the declared components;
2. evidence of nonfactorization across the preregistered cut family;
3. controls for common input, measurement mixing, and hidden shared causes;
4. when a causal or persistence claim is intended, cross-part interventions or perturbation-response evidence.

Positive total correlation identifies statistical dependence, not causal integration. Positive minimum-cut dependence identifies failure to factor across the least-dependent tested cut, not individuality. Without common-cause controls or an adequate cut search, causal Integration is UNDETERMINED.

### 5.3 Core measurement profile

No single canonical scalar should be declared. Use a mandatory profile:

#### I-T — Total dependence

> **TC = Σ_i H(X_i) − H(X_1,…,X_n)**

TC is nonnegative and measures total statistical dependence across the declared components. Report it in bits/nats with bias correction and uncertainty.

#### I-W — Weakest-cut dependence

> **I_W = min over preregistered bipartitions A|B of normalized I(X_A;X_B)**

The cut family and normalization are load-bearing. Raw, size-normalized, and entropy-normalized selectors can choose different minimum cuts. Report both the minimizing partition and its magnitude.

#### I-O — Redundancy/synergy character

Use O-information when the balance of shared/redundant versus synergistic dependence matters. Positive and negative values indicate different organization, not more versus less Integration on one line.

#### I-D — Dynamic/causal coupling

When time-series or interventions are available, add a dynamic or causal measure chosen for the declared model class. The measure must state whether it captures prediction gain, effective connectivity, causal density, or intervention response. These are not interchangeable.

### 5.4 Persistence measurement

The persistence reading is coalition-based by default:

- disable cross-part couplings singly and in preregistered combinations;
- compute minimal failure cut sets and minimal viability-preserving sets;
- test whether the joint effect is additive, redundant, or synergistic;
- report ΔV_I for the coalition structure.

Per-edge weights are summaries only where additivity and identifiability tests pass. This follows the current canon’s strongest repair.

### 5.5 Current defect repaired

The current canon says Integration is the degree to which parts act as one irreducible whole, then uses TC as the lead proxy while conceding that TC measures interdependence rather than irreducible wholeness. The proposed definition removes that contradiction: Integration is nonfactorization; irreducibility across the weakest cut is one coordinate; individuality remains a separate panel-level judgment.

## 6. The Required Reporting Form

Never publish this:

> B = 0.7, D = 0.4, M = 0.8, I = 0.9.

Publish this:

| Field | Required content |
|---|---|
| Declaration | Complete D tuple and model class |
| Identification | PRESENT / ABSENT / UNDETERMINED for each axis, with the satisfied or missing criteria |
| Structural profile | Named proxy values, units, estimator, uncertainty, and validity domain |
| Partition/grain sensitivity | Results across the preregistered defensible declaration family |
| Persistence effect | ΔV for admissible interventions; coalition structure where nonadditive |
| Controls | Negative, bypass/open-interface, common-driver, and estimator controls as applicable |
| Missingness | Explicit reason a proxy is undefined, not available, or only a lower bound |

### 6.1 Cross-system comparison

Cross-system comparisons are valid only when the measurement protocol, units, relevant declaration slots, and normalizer are held fixed or explicitly harmonized.

- Do not compare raw σ across systems with different state completeness or clock units.
- Do not compare E across different observation channels or time grains.
- Do not compare TC across different numbers of components without a declared normalization and sensitivity check.
- Do not compare Boundary contrasts across noncommensurable variables.
- Never sum B, D, M, and I. They are noncommensurable profiles, not currencies.

## 7. Implications for the Proposed Declaration-Sensitivity Audit

The audit should vary declarations only after freezing the measurement protocol above.

For each system and each preregistered boundary/grain declaration:

1. apply the same identification criteria;
2. compute the same named structural proxies;
3. preserve the same normalization and missingness rules;
4. apply the same intervention class where physically meaningful;
5. report how identification, structural magnitude, persistence effect, and uncertainty change.

The audit’s primary object should be **profile robustness**, not movement of “four numbers.” A declaration change can legitimately change:

- whether an axis is defined at all;
- the structural magnitude;
- the persistence effect;
- the identity of a minimum cut or load-bearing coalition;
- the estimator uncertainty.

Those changes must not be collapsed into one distance until their types are reported separately.

## 8. Actionable Fixes

### Priority 1 — Freeze the ontology

Adopt the four core definitions in this proposal, or equivalent definitions with the same separation of target, identification, structural magnitude, and persistence effect.

### Priority 2 — Repair Boundary before executing cross-system work

Define B1 against a valid reference and add an explicit shielding/attenuation assay. Do not use conditional mutual information alone as “boundary strength.”

### Priority 3 — Narrow the Memory core

Make predictive dependence and retention the structural core. Keep Cμ explicitly tied to a declared predictive model. Move dormant physical organization into the recovery-intervention protocol unless an actual encoding/observation channel is specified.

### Priority 4 — Make Integration a profile by rule

Require TC plus weakest-cut dependence; add O-information where character matters and a causal/dynamic measure only when the model supports it. Prohibit “high Integration” without a badge naming the measure.

### Priority 5 — Standardize identification verdicts and missingness

Use PRESENT / ABSENT / UNDETERMINED. An unavailable, invalid, nonstationary, noncommensurable, or underpowered measurement is never scored as zero.

### Priority 6 — Build one worked real-system measurement protocol

Before a broad audit, run the complete specification on one system with enough published dynamics and perturbation data to support all four axes. The goal is not to prove AOP; it is to discover whether the operational constitution can actually be followed without analyst improvisation.

## 9. Creative Opportunities

### 9.1 AOP’s characteristic output may be a structured assessment, not a coordinate

The framework becomes stronger if it stops aspiring to a four-number phenotype. Its distinctive object can be:

> **a declaration-indexed structural profile plus a coalition-indexed persistence map.**

That is richer than a radar chart and more faithful to the science.

### 9.2 Boundary and Integration become dual but nonredundant

Under these definitions:

- Boundary asks whether an interface attenuates outside-to-inside influence while sustaining a contrast.
- Integration asks whether the inside components fail to factor from one another.

One is selective insulation across a cut; the other is dependence within/across a component decomposition. Their algebraic overlap becomes understandable rather than embarrassing.

### 9.3 Memory gains an honest dormant-state route

The latent-memory assay provides a principled home for spores, seeds, genomes, immune memory, and stored regulatory architecture without pretending that molecular complexity is Cμ. It also gives the axis a direct experimental program: perturb the stored constraints and test recovery.

### 9.4 The audit can discover type changes, not merely magnitude changes

A boundary shift may turn a quantity from defined to undefined, change the minimizing partition, or replace an additive edge attribution with a coalition-only report. Those are scientifically meaningful declaration effects that a scalar robustness score would erase.

## 10. Bottom-Line Judgment

The B/D/M/I ontology is salvageable and can be made clean. Drive is already close. Integration needs disciplined plural measurement. Memory needs a narrowed informational core plus a separate latent-recovery assay. Boundary needs the most substantive repair: a boundary must be identified by a conjunction of contrast and selective shielding, not by dependence or conditional independence alone.

If AOP adopts this constitution, the declaration-sensitivity experiment becomes well posed. If it does not, the experiment will measure a mixture of boundary choice, proxy choice, undefinedness, and analyst discretion.

## Sources Actually Accessed

### Current AOP source of truth

- [AOP_CANON_MASTER_v1.27.md](https://drive.google.com/file/d/1mnX6Y8frvAkl8rpH3aP2OR27jriGVel-/view) — current placed file accessed in full. Its internal masthead still says v1.26; this report uses the placed file identity and does not silently resolve that version-stamp defect.

### AOP development sources

- [AOP Step 0 — Axis-input scoping](https://drive.google.com/file/d/1l4P-GAXQfNdMmWxk7MyQo2D4BM-H1MYB/view) — current v1.26-grounded input-requirement analysis.
- [AOP Operational Panels — Computed on the Benchmark](https://drive.google.com/file/d/11IQNDZvYP3ptePP4prUGTuCp3dCzg2Uq/view) — non-canonical benchmark panel implementation; used to inspect what the existing panels actually return.
- [Axis B dossier](https://drive.google.com/file/d/10G9OQ09v2VJf3GTYuUXAR8dwLgcZ9-FH/view), [Axis D dossier](https://drive.google.com/file/d/1YZijMx8duvI6Gf2YLmS6_P9-spqn-HUI/view), [Axis M dossier](https://drive.google.com/file/d/1wan5ZAq4MvZxzp3Zo3Ku0mcWVIGOrANE/view), and [Axis I dossier](https://drive.google.com/file/d/13kWIx40qQ5i-bMjA6tVHG9d1F9onPwY9/view) — historical v1.19 deepening documents, used only as development history where consistent with the current canon.

### Primary literature checked

- Parrondo, Van den Broeck & Kawai (2009), relative entropy and dissipation: [DOI](https://doi.org/10.1088/1742-5468/2009/02/P02025).
- Roldán & Parrondo (2012), time-series irreversibility as a lower bound on entropy production: [Physical Review E](https://doi.org/10.1103/PhysRevE.85.031129).
- Crutchfield & Feldman (2003), excess entropy and process memory: [DOI](https://doi.org/10.1063/1.1530990).
- Rosas et al. (2019), O-information: [Physical Review E](https://doi.org/10.1103/PhysRevE.100.032305).
- Mediano, Seth & Barrett (2019), comparison of integrated-information measures: [Entropy](https://doi.org/10.3390/e21010017).
- Kolchinsky & Wolpert (2018), viability-relative semantic information and intervention: [Interface Focus](https://doi.org/10.1098/rsfs.2018.0041).
- Watanabe (1960), total correlation: [IBM Journal of Research and Development](https://doi.org/10.1147/rd.41.0066).

---

**End of proposed specification.**
