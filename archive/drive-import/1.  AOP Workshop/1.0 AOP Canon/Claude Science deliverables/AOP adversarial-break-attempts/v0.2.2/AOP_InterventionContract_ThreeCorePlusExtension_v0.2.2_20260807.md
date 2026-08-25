# AOP Intervention Contract — three core contrasts plus one internal-cut extension (v0.2.2)

**Issued:** 2026-08-07  
**Status:** PROPOSAL; non-canon; built to be attacked. Authorizes no canon edits.  
**Supersedes:** `AOP_InterventionContract_FourAxis_v0.2.1_20260807.md` for the next falsification gate.  
**Scope of revision:** targeted repair. The governing decisions remain **Memory A / typed family / declared cut**.  

This is a scientific contract, not a session record. It defines what must be declared, measured, intervened upon, and reported. It does not certify its own success.

---

## 0. Claim and architecture

The method is a **typed family of causal contrasts**, not one universal estimand and not a proof that AOP has four independent operational degrees of freedom.

Each runnable contrast has the form

> **θ_A(λ; D) = V_τ(P^{A,λ}_{μ₀}) − V_τ(P^0_{μ₀})**,

where `A` names the contrast, `λ` its severity or rung, `D` the complete declaration, `μ₀` the common initial ensemble, and larger `V` always means greater viability. The sign convention is **intervened minus actual**. This is the reverse of the Kolchinsky–Wolpert value convention; every comparison to that framework must say so.

The family contains:

| Contrast | Intervention type | Canonical reading | Status |
|---|---|---|---|
| **Boundary** | initial-state, external cut | boundary panel B1/B2/B4, with B5 descriptive | core |
| **Memory** | mechanism | excess entropy `E = I(past;future)` | core |
| **Drive** | mechanism | path asymmetry / entropy production `σ` relative to declared reversal `R` | core |
| **Integration** | initial-state, internal cut | a declared Integration reading, provisionally `TC` or `Φ_MIP` | internal-cut extension; not promoted |

The contrasts share a declaration discipline, outcome convention, sensitivity audit, and reporting schema. They do **not** have to share one null operator or one structural reading.

Zero `θ_A` means only: **no detected viability relevance under this declaration, horizon, estimator, and intervention.** It never means the feature is absent.

---

## 1. Complete declaration `D`

Every model–contrast pair must fill every applicable field below before execution. No silent defaults are permitted.

1. **System and level:** state space, variables, system boundary, model class, and level of description.
2. **Time:** time grain `δt`, total horizon `τ`, measurement windows, and evaluation schedule.
3. **Initial ensemble:** `μ₀`, conditioning rule, support, conservation constraints, and whether exactly the same `μ₀` is used for actual and intervened runs.
4. **Cut and interface:** external cut or internal partition; for Boundary, the interface variables `F`; for Integration, the partition rule and selected partition.
5. **Outcome:** exact `V`, its domain and type (endpoint, path, survival, or first-passage), and why larger means more viable.
6. **Outcome event:** for survival or first-passage, the start set, success/viable set, failure/absorbing set, target set, stopping rule, and orientation of any reference dynamics relative to those sets.
7. **Intervention:** Type A or B, the exact state or mechanism changed, severity `λ` or discrete rung, and the rule resolving non-unique nulls.
8. **Preserved and free quantities:** every marginal, rate, stationary law, resource flow, constraint, coupling, or other quantity held fixed; everything intentionally allowed to move.
9. **Admissibility:** separate judgments for probabilistic validity, constraint compatibility, dynamical reachability, physical implementability, and **AOP-domain membership**.
10. **Identifiability:** whether the effect can be attributed to the named contrast; expected off-target changes and known confounds.
11. **Representation and reversal:** observed state representation, coarse-graining, even/odd variables, and the time-reversal involution `R`.
12. **Estimator:** population or sample estimand, sample length/count, smoothing or regularization, uncertainty method, seed policy, and failure/undefined rule.
13. **Units:** bits or nats; per step or per unit time; rate parameterization and sweep variable.
14. **Sign:** intervened minus actual, restated beside the reported result.

A blank load-bearing field makes that model–contrast pair **NOT EXECUTABLE**, not negative and not zero.

---

## 2. Measurements

### 2.1 Boundary — a panel, not one scalar

Boundary means the role of a declared inside/outside cut. It does not by itself prove a membrane, wall, or material interface. The canonical Boundary reading is a small panel:

- **B1 — interior/exterior contrast:** the declared state contrast across the cut, with its variables and units.
- **B2 — interface screening:** `I(inside; outside | F)`, where `F` is the declared interface. This distinguishes dependence mediated by the interface from coupling that bypasses it.
- **B4 — maintenance burden:** the work, flow, control effort, or other declared burden required to hold B1 against leak or relaxation.
- **B5 — cross-cut stored dependence:** `I(inside; outside)`. B5 is retained as a descriptive cross-cut quantity. It is **not boundary strength** and cannot replace B1/B2/B4.

The Type-A Boundary null product-scrambles the initial inside/outside joint while preserving the declared within-side marginals and all other quantities named in `D`, then runs the unchanged dynamics forward. Report B1, B2, B4, B5, and `V` where defined. If no interface `F` or maintenance model exists, B2 or B4 is **NOT DEFINED** for that model; do not silently substitute B5.

### 2.2 Memory — keep `E`, use a projection ladder

The Memory target remains

> **E = I(X_{≤0}; X_{≥1})**

for a stationary process at a declared grain and representation, with a contiguous past/future split and the present on the past side.

For finite records or transient panels, report

> **E_{L₋,L₊}(t) = I(X_{t−L₋+1:t}; X_{t+1:t+L₊})**,

with `L₋`, `L₊`, `t`, and `δt` stated. Off stationarity, this finite-window object is a scoped local reading; it is not automatically an estimator of a stationary infinite-window `E`.

The full Memory null is **order 0**: replace the temporal mechanism with the i.i.d. process having the same one-time marginal. This drives `E` to zero but also changes kinetics and necessarily removes Drive. That lack of selectivity is reported, not hidden.

Diagnostic rungs use the order-`k` Markov projection `M_k`:

- finite alphabet and observed representation declared;
- initial `k`-block law equals the observed `k`-block marginal;
- transition kernel equals the observed conditional law on positive-probability contexts;
- zero-probability contexts remain outside the reachable support and are not assigned arbitrary transitions;
- preserved block statistics are stated explicitly;
- `k` is discrete, not presented as a continuous severity.

Report separately:

> `E(M_k)`,  
> `ρ_k = E(original) − E(M_k)`,  
> `θ_M(k) = V(M_k) − V(original)`.

`ρ_k` is a **projection residual**, not a renamed Memory axis. For a finite-order process it should reach zero at sufficient `k`. For the Even Process it is expected to remain positive at every finite `k` while tending toward zero asymptotically; that behavior is not failure.

**Finite-sample rule.** The population calculation is primary on analytic benchmarks. For simulated records, use the same estimator on actual and projected paths; predeclare record length, number of replicates, maximum `k`, context-count threshold, smoothing rule, and confidence or bootstrap interval. A rung is **UNRESOLVED** when its residual is not distinguishable from estimator bias or uncertainty. No extrapolation to `k → ∞` is allowed without a declared model and uncertainty.

### 2.3 Drive — declared path asymmetry and declared outcome

Drive is read as path asymmetry relative to a declared reversal `R`. For a window `[t,t+Δ]`,

> **σ_Δ(t) = Δ⁻¹ D_KL(P_[t,t+Δ] || R P_[t,t+Δ])**.

The stationary long-window limit, when it exists, is `σ`. The null is a declared detailed-balance projection at fixed stationary distribution relative to `R`. Any non-uniqueness in that projection must be resolved in `D`.

The sign and size of `θ_D` are properties of **Drive plus the exact viability event**, not of `σ` alone. Two systems can have equal `σ` and opposite effects on a directional target. Therefore every first-passage or survival use must declare the start, target, absorbing/failure sets, stopping rule, and orientation.

For the three-state ring benchmark, the observed state is the **ring position**, not the increment sequence. Position-space reversal is used. The increment representation is outside this benchmark declaration because it preserves the current reading while erasing the declared Memory reading. A change of representation is a change of the scientific question, not a harmless coding choice.

Any current-shortens-persistence theorem is applied only inside its complete stated envelope. Outside that envelope, the sign is empirical and no theorem-based prediction is made.

### 2.4 Integration — a measured internal-cut extension

The Integration intervention is the Type-A product scramble across a declared **internal** partition, but an operation alone is not a measurement. Every executable Integration case must select one reading before the run:

- **Total correlation `TC`** across a fixed multi-part partition; or
- **minimum-cut dependence `Φ_MIP`** under a fully declared partition search and normalization rule.

Predictive irreducibility or causal-coupling ablation may be proposed later, but cannot be mixed into the same gate without a new declaration.

The initial internal scramble preserves each part's marginal, runs the same dynamics forward, and reports the chosen Integration reading and `V`. B5 across an internal cut is reported only as descriptive dependence, not as the Integration reading itself.

Integration remains unpromoted. If its reading or viability response is completely determined by repeating the Boundary operation over an internal cut, report **operator collapse / no separate operational content**.

---

## 3. Response panels and interpretation

Use two panels; do not merge them into a rank test.

- **Panel A — initial-state interventions:** Boundary external-cut scramble and Integration internal-cut scramble. Fixed dynamics; report B1/B2/B4/B5, selected Integration reading, finite-window Memory reading, Drive reading, and `V(t)` wherever each is defined.
- **Panel B — mechanism interventions:** Memory projections and Drive null. Fixed initial ensemble; report the same defined readings and `V(t)`.

Every cell receives one status:

- **ESTIMATED** — value plus uncertainty;
- **ANALYTIC** — exact result or derivation;
- **NOT DEFINED** — the model lacks the required cut, interface, partition, stationary limit, or outcome object;
- **NOT EXECUTABLE** — the declaration or intervention is incomplete or inadmissible;
- **UNRESOLVED** — estimator power or finite-sample bias prevents a conclusion.

Off-target movement is a result. Do not infer how many real axes exist from matrix rank, diagonal appearance, or one model's response pattern.

---

## 4. Benchmark suite and applicability map

The gate does **not** run every contrast on every model. It runs each contrast only where its required objects exist, while ensuring that every contrast has at least one positive control, one failure or dissociation test, and one admissibility/definedness challenge.

| # | Benchmark | Primary job | B | M | D | I |
|---|---|---|:---:|:---:|:---:|:---:|
| 1 | i.i.d. finite-alphabet source | all-null and estimator-bias control | — | ✓ | ✓ | — |
| 2 | reversible correlated order-1 chain | Memory without Drive | — | ✓ | ✓ | — |
| 3 | Even Process | infinite-order ladder; asymptotic residual decay | — | ✓ | ✓ | — |
| 4 | driven three-state position ring | Drive control; forced Drive–Memory cross-effect | — | ✓ | ✓ | — |
| 5 | external-cut interface model | B2/B5 dissociation and maintenance/no-maintenance test | ✓ | optional | optional | — |
| 6 | multipart model with both external and internal cuts | Boundary–Integration operator-collapse test | ✓ | optional | optional | ✓ |
| 7 | driven, memory-bearing model with viability-relevant and irrelevant channels | Memory–Drive selectivity and viability-invariant control | optional | ✓ | ✓ | optional |
| 8 | anti-viable information model | signed-effect control | ✓ | optional | optional | optional |
| 9 | deliberately inadmissible or out-of-domain construction | exercise admissibility and domain reporting | as declared | as declared | as declared | as declared |

`—` means **not required and normally not defined**, not zero. `optional` means it may run only after the full declaration is filled.

### 4.1 Minimum declarations for the benchmark worlds

**Models 1–4 — temporal/process models.** No external or internal spatial cut is inferred. State alphabet, `δt`, representation, stationary law or nonstationary initialization, path outcome, estimator, units, and reversal are declared. Model 4 fixes position-space representation and an exact first-passage or survival event.

**Model 5 — external interface.** Declare inside, outside, and interface `F`; parameterize a through-interface condition and a bypass-coupling condition; declare the burden needed to maintain B1 against leak. The benchmark must contain at least one case with high B5 but B2 near zero and no material maintenance, so B5 cannot masquerade as Boundary strength.

**Model 6 — nested cuts.** Declare one external cut and at least one internal partition on the same system. Use the same Type-A scramble rule over both cuts, but read Boundary with B1/B2/B4 and Integration with `TC` or `Φ_MIP`. This makes operator overlap testable without assuming measurement identity.

**Model 7 — driven memory.** Must have `σ>0`, genuine temporal Memory, a nontrivial viability event, and at least one manipulation that changes a structural reading without changing `V`. This model, not a reversible chain, tests whether Memory and Drive can be distinguished when both are active.

**Model 8 — signed control.** Information or dependence must predictably reduce viability under the declared event, so the sign convention is tested rather than assumed beneficial.

**Model 9 — admissibility/domain challenge.** Intentionally omit or violate one named requirement. The expected output is NOT EXECUTABLE or OUTSIDE DOMAIN with the precise failed field—not a numeric contrast.

Before execution, each checked model–contrast pair receives a separate declaration sheet containing all 14 fields in §1. A summary table is not a substitute.

---

## 5. Predeclared tests and failure conditions

### 5.1 Identity and calibration tests

1. The i.i.d. source returns `E=0` and `σ=0` within the declared analytic or estimator tolerance.
2. The reversible correlated chain returns `E>0` and `σ=0`.
3. The Even Process shows no finite-order exact saturation but a residual compatible with asymptotic decay.
4. The driven position ring returns `σ>0` away from detailed balance; the detailed-balance null returns `σ=0`; representation is held fixed.
5. Boundary B2 distinguishes interface-mediated dependence from bypass coupling; B5 alone does not.
6. The nested-cut model makes the same scramble operator visible across two cuts while permitting Boundary and Integration readings to differ.
7. The driven-memory model exposes cross-loading rather than enforcing a diagonal call graph.
8. The signed control recovers the predeclared sign under the intervened-minus-actual convention.
9. The inadmissible model is refused for the correct named reason.

### 5.2 Method-level failure conditions

- **F1 — no common outcome:** no single `V` retains one meaning across the intended contrasts. Disposition: per-contrast outcomes; abandon common-outcome claim.
- **F2 — constructional degeneracy:** `μ₀`, `V`, or the preserved quantities force `θ=0`. Disposition: declaration error; repair before scientific interpretation.
- **F3 — inadmissible or outside domain:** a null fails a named admissibility or domain test. Disposition: that contrast is unavailable on that model.
- **F4 — Memory/Drive not dissociable:** after driven-memory benchmarks and diagnostic rungs, all Memory interventions remain inseparable from Drive effects. Disposition: fuse or qualify the operational claims; do not claim separate measurement.
- **F5 — Integration adds no content:** chosen Integration reading and response are determined by the external-cut operation under relabeling. Disposition: retire the extension from the measured core.
- **F6 — Boundary panel cannot be instantiated:** no interface or maintenance quantity can be declared on any target class. Disposition: restrict Boundary claims to the instantiated subpanel; B5 alone may only be called external stored dependence.
- **F7 — outcome-direction instability:** reasonable undeclared target choices reverse the result. Disposition: the declaration was incomplete; after exact event declaration, report sign as event-relative.
- **F8 — estimator failure:** seeded scientific defects or known analytic controls are missed beyond the predeclared tolerance. Disposition: estimator/test suite fails even if the model code is deterministic.

These conditions are fatal only to the stated co-measurement or contrast claim. They do not by themselves reject AOP.

---

## 6. Estimation, mutation testing, and reporting

### 6.1 Analytic-first rule

Use exact calculations on models 1–4 whenever possible. Simulation validates implementation; it does not turn an algebraic identity into an empirical discovery.

### 6.2 Finite-sample rule

For every estimated reading, report sample size, replicate count, estimator, smoothing, bias assessment, interval, seed policy, and convergence sweep. Results must include raw values, not only pass/fail labels.

### 6.3 Mutation test

Before accepting the harness, seed defects that alter scientific meaning—wrong lag, wrong reversal, wrong target, ignored horizon, changed entropy-production factor, transposed generator, changed state representation—and require the suite to catch them. A check that inverts the same function it validates is not independent.

### 6.4 Required output per model–contrast pair

1. completed declaration sheet;
2. status for each measurement;
3. actual and intervened structural readings;
4. actual and intervened `V`;
5. `θ` with sign convention beside it;
6. uncertainty or analytic derivation;
7. off-target movements;
8. admissibility and domain verdicts, each separate;
9. identifiability verdict;
10. sensitivity to horizon, grain, severity/rung, representation, and estimator;
11. known theorem envelope and whether the case is inside it;
12. PASS / FAIL / UNRESOLVED / NOT EXECUTABLE, with reason.

---

## 7. Gate disposition

Version 0.2.2 is ready only for an **independent break attempt** after the benchmark declaration sheets and executable harness are built. Its builder cannot certify it.

The independent gate must return one of:

- **family survives** — proceed with a three-core-plus-extension methods paper;
- **family survives with named reduction** — specify which contrasts remain and which claims are withdrawn;
- **contract fails** — name the exact declaration, measurement, intervention, benchmark, or estimator failure and the cheapest repair;
- **gate not executable** — name every missing field or artifact.

Until that occurs, the methods-paper gate remains open.

---

## 8. v0.2.2 repair ledger

| v0.2.1 defect | v0.2.2 disposition |
|---|---|
| B5/CBSD substituted for Boundary | restored B1/B2/B4 panel; retained B5 as descriptive only |
| survival event underdeclared | added start, target, viable/failure sets, stopping rule, and orientation |
| every contrast ordered on every model | replaced with applicability map and explicit undefined statuses |
| ring representation ambiguous | fixed position-space representation and reversal |
| Integration had an operation but no reading | requires preselected `TC` or `Φ_MIP` |
| time grain, interface, resource-flow and domain fields missing | added to complete declaration |
| Even Process rationale said residual simply “never saturates” | distinguishes finite-order non-saturation from asymptotic decay toward zero |
| no finite-sample/smoothing rule | added estimator and UNRESOLVED rules |
| no driven memory-bearing dissociation model | added model 7 |
| missing internal/external-cut overlap model | added nested-cut model 6 |
| no admissibility/domain challenge | added model 9 |
| governance mixed into science | removed session housekeeping; retained only scientific status and gate rule |
| deterministic checks could validate themselves | added independent mutation-test requirement |

---

*Proposal v0.2.2. Non-canon. Preserves Memory A, the typed-family architecture, and Boundary as a declared cut while restoring the canonical Boundary measurements. Authorizes no canon edits and makes no claim of having passed the independent gate.*
