# Break attempt — AOP Intervention Contract v0.2.2: the analytic attack

**Report:** `AOP_Break_MathAttack_v0.2.md`
**Target:** `AOP_InterventionContract_ThreeCorePlusExtension_v0.2.2_20260807.md` (Drive id `1G11FteSv7yqcqHlyM0oqb2uLwOknlNLc`, 21,048 bytes as downloaded, unescaped to 21,036)
**Parent canon consulted:** `AOP_CANON_MASTER_v1.27.md` (Drive id `1jnqgjhCg6X-7FzOSEEZWM4V40ck7xty_`, md5 `998aa87e0927f84ae6ea1676ebe8ca93`)
**Date:** 2026-08-08
**Lane:** analytic (closed-form counterexamples). Fidelity and citation lanes are separate reports.

**Exclusion declaration.** I did not build v0.2.2. I did build the v0.1 break attempt on v0.2.1 that
v0.2.2's §8 ledger responds to; accordingly I do **not** grade that ledger here — the discharge audit
was run by an independent fidelity lane. This report contains only findings derived from calculations
on the contract's own declared models.

**Everything below is exact.** No estimator, no sampling, no extrapolation. Every number is a closed-form
linear-algebra or information-theoretic result, reproducible from §8.

---

## 0. Summary of the analytic attack

| id | finding | grade | contract's own category |
|---|---|---|---|
| **A1** | The Drive null is non-unique by a **three-parameter family**, and θ_D changes sign inside it. One fully-filled declaration admits 13,824 valid nulls with θ_D from −47.62 to +0.298. | **fatal** | F7 (outcome-direction instability), and §2.3's own non-uniqueness clause is inadequate |
| **A2** | θ_D also flips sign with the choice of first-passage **target** at a *fixed* null: −0.952 vs +0.238. §1 field 6 requires the event be declared but supplies no rule making the contrast comparable across events. | **fatal** | F7; §1 field 6 |
| **A3** | Under an **endpoint/occupation** outcome, every stationary-law-preserving intervention gives θ → 0 geometrically. Both Panel A and Panel B wash out. §3's panel split does not prevent it. | **fatal** | F2 (constructional degeneracy) |
| **A4** | The mandated Integration reading `TC` is **identically equal** to the forbidden B5 on any bipartition. The contract requires and forbids the same number. | **fatal** | F5 / §2.4 internal contradiction |
| **A5** | On models 1, 2 and 3 the Drive null is the **identity map**, so θ_D = 0 analytically — which §5.2 F2 calls a declaration error. Three of nine benchmarks are structurally degenerate for Drive. | **major** | F2 |
| **A6** | §2.2's "necessarily removes Drive" is **false** for the reversals §1 field 11 explicitly permits: an odd-variable involution leaves σ > 0 after the order-0 Memory null. | **major** (stated reason) | §2.2 rationale |
| **A7** | On model 4 the ladder is **trivial**: the ring is order-1, so ρ_k = 0 for all k ≥ 1 and rungs k ≥ 2 carry no diagnostic content. | **minor** | §2.2 diagnostic rungs |

**Verdict on the gate (§7): `gate not executable` on Drive and Integration as currently declared, and
`family survives with named reduction` for Memory.** The Memory contrast is in good analytic shape and
v0.2.2's Even-Process repair is **correct** — see §6. The Drive contrast cannot be executed to a
reproducible sign, and the Integration reading is self-contradictory, until A1–A4 are repaired.

---

## 1. A1 (fatal) — the Drive null is non-unique by a three-parameter family, and θ_D changes sign inside it

### 1.1 Setup, verbatim from the target

> "The null is a declared detailed-balance projection at fixed stationary distribution relative to `R`.
> Any non-uniqueness in that projection must be resolved in `D`." (§2.3)

> "For the three-state ring benchmark, the observed state is the **ring position**, not the increment
> sequence. Position-space reversal is used." (§2.3)

And the benchmark's job, from §4: model 4 is the "driven three-state position ring", "Drive control;
forced Drive–Memory cross-effect".

### 1.2 The break

Take the ring at (a, b) = (0.48, 0.12), n = 3 — the canonical parameterisation, with every §1 field
filled: state = position (field 11), V = −MFPT(0→1) with start {0}, absorbing target {1} (fields 5, 6),
intervention = detailed-balance projection at fixed stationary law (field 7), sign = intervened minus
actual (field 14).

The actual process has

| quantity | value |
|---|---|
| σ (position rep.) | **0.720000 bits/step** |
| E (position rep.) | **0.180855 bits** |
| cycle affinity A = 3 ln(a/b) | 4.158883 nats |
| MFPT(0→1) | 2.380952 |
| MFPT(0→2) | 3.571429 |

The ring's stationary law is uniform for **every** (a, b) by cyclic symmetry. Therefore the constraint
"detailed balance at fixed stationary distribution" reduces to: *any symmetric edge-weight assignment*.
Write the three undirected edge weights as x = w(0↔1), y = w(1↔2), z = w(2↔0). Every such chain has
π = (1/3, 1/3, 1/3) and σ = 0 exactly. **The null is a three-parameter family, not a point.**

Sweeping x, y, z on a 24-point grid over (0.02, 0.48] and keeping only the chains that are genuine
σ = 0 nulls with the stationary law preserved:

| statistic | value |
|---|---|
| admissible nulls found | **13,824** |
| θ_D minimum | **−47.619048** at (x,y,z) = (0.02, 0.02, 0.14) |
| θ_D maximum | **+0.297619** at (x,y,z) = (0.48, 0.48, 0.46) |
| fraction with θ_D > 0 | **5.29%** (731 of 13,824) |
| σ of every null | 0 (max |σ| over the family: 2.1×10⁻¹⁷) |
| stationary law of every null | (1/3, 1/3, 1/3) to 10 decimal places |

Restricting to the natural *one-parameter* sub-family (symmetric ring, common rate c) already breaks it,
and every one of these four choices is defensible prose in a declaration:

| null rule | c | σ | MFPT(0→1) | E(M) | **θ_D** |
|---|---|---|---|---|---|
| preserve total escape rate, c = (a+b)/2 | 0.300 | 0 | 3.333333 | 0.014012 | **−0.952381** |
| symmetrised log-rate, c = √(ab) | 0.240 | 0 | 4.166667 | 0.106117 | **−1.785714** |
| preserve fastest channel, c = max(a,b) | 0.480 | 0 | 2.083333 | 0.382670 | **+0.297619** |
| preserve slowest channel, c = min(a,b) | 0.120 | 0 | 8.333333 | 0.549922 | **−5.952381** |

θ_D(c) = MFPT_actual − 1/c crosses zero at c\* = 1/2.380952 = **0.420000**. Any admissible null with
c > 0.42 reports drive as *viability-enhancing*; any with c < 0.42 reports it as *viability-destroying*.
All four rules above are stated in one clause of ordinary declaration language, all four satisfy every
field of §1, and all four are detailed-balance projections at the fixed stationary distribution.

### 1.3 Why §2.3's own clause does not save it

§2.3 says non-uniqueness "must be resolved in `D`". But §1's fourteen fields contain **no field that
records which resolution was used**. Field 7 requires "the rule resolving non-unique nulls" — this is
the closest — yet nothing in §1, §3, §4.1 or §6.4 requires the *chosen* rule to be justified, compared
against alternatives, or reported alongside θ. Two seats filling all fourteen fields correctly, both
writing a one-line resolution rule in field 7, obtain **opposite-signed** θ_D on the same benchmark and
both pass every check in the document. That is a specification defect, not an execution error.

Note also that the four rules differ in E(M) by a factor of **39×** (0.014 to 0.550), so the choice of
Drive null silently sets the Memory reading of the null as well — an off-target movement §6.4 item 7
requires reporting but §2.3 gives no way to bound.

### 1.4 Disposition

**Fatal to gate execution, not to AOP, and not to σ.** σ = 0.720000 bits is a property of the actual
process and is unaffected. What fails is the *contrast*: θ_D is not a function of the declaration.
Repair (cheapest): add a §1 field 7a, "**null selection rule and its admissible alternatives**", and
require §6.4 to report θ under **at least two** declared alternative nulls, with the contrast reported
as an interval or explicitly marked UNRESOLVED when the interval straddles zero. Under that rule the
ring at (0.48, 0.12) reports θ_D ∈ [−47.6, +0.30] → **UNRESOLVED**, which is the honest answer.

---

## 2. A2 (fatal) — θ_D flips sign with the target choice at a *fixed* null

### 2.1 Setup, verbatim

> "The sign and size of `θ_D` are properties of **Drive plus the exact viability event**, not of `σ`
> alone. Two systems can have equal `σ` and opposite effects on a directional target. Therefore every
> first-passage or survival use must declare the start, target, absorbing/failure sets, stopping rule,
> and orientation." (§2.3)

This is the v0.2.1 repair. It is a real improvement — the contract now *knows* about the problem. The
attack is that knowing is not sufficient.

### 2.2 The break

Hold the null **fixed** at c = (a+b)/2 = 0.30. Vary only the declared first-passage event — both
choices fully specify start, target, absorbing set, stopping rule and orientation, as §1 field 6 demands:

| declared event | MFPT actual | MFPT null | **θ_D** |
|---|---|---|---|
| first passage 0 → 1 (one step **with** the current) | 2.380952 | 3.333333 | **−0.952381** |
| first passage 0 → 2 (one step **against** the current) | 3.571429 | 3.333333 | **+0.238095** |

Both events are declared to the letter of field 6. The same system, the same σ, the same null, the same
sign convention — and Drive is reported as viability-destroying under one event and viability-enhancing
under the other.

### 2.3 Why this is distinct from A1

A1 is non-uniqueness of the *intervention*; A2 is non-uniqueness of the *outcome*. §2.3's repair
addresses neither: it requires the event be **declared**, which makes each run reproducible, but it does
not make runs **comparable**, and §7's gate dispositions ("family survives", "contract fails") are
statements about the family, not about one declaration. A gate that returns "Drive matters, sign
negative" from a document in which the sign was set by an unforced choice has not measured Drive.

### 2.4 Disposition

**Fatal to any cross-model or cross-contrast claim about the sign of Drive.** Repair: §2.3 should state
that θ_D is reported **per declared event** and that no aggregate sign claim may be made across events;
and §5.1 test 4 should be extended to require the ring be run on **both** a with-current and an
against-current event, with the sign reversal reported as an *expected* result rather than a failure.
Note this converts A2 from a defect into a positive control — the contract would be *stronger* for
predicting the flip.

---

## 3. A3 (fatal) — under an endpoint outcome both panels are degenerate at long horizon

### 3.1 Setup, verbatim

> "**Panel A — initial-state interventions:** Boundary external-cut scramble and Integration internal-cut
> scramble. Fixed dynamics ...
> **Panel B — mechanism interventions:** Memory projections and Drive null. Fixed initial ensemble ..." (§3)

> "**Outcome:** exact `V`, its domain and type (**endpoint**, path, survival, or first-passage) ..." (§1 field 5)

Endpoint is the *first* listed outcome type and is permitted throughout.

### 3.2 The break

The Type-A scramble changes only μ₀ and leaves the dynamics fixed (§2.1: "then runs the unchanged
dynamics forward"). For any ergodic chain, μP^τ → π regardless of μ. Therefore under an endpoint or
occupation-probability V, θ decays as |λ₂|^τ to **exactly zero**.

On a 4-state ergodic chain factorised as inside {0,1} × outside {2,3}, V = P(occupy viable set at τ),
μ₀ non-stationary and correlated across the cut:

| τ | \|θ\| initial-state (Panel A) | \|θ\| mechanism (Panel B) |
|---|---|---|
| 1 | 4.762×10⁻² | 4.004×10⁻³ |
| 5 | 2.450×10⁻³ | 1.023×10⁻³ |
| 10 | 3.678×10⁻⁵ | 1.621×10⁻⁵ |
| 20 | 7.740×10⁻⁹ | 3.424×10⁻⁹ |
| 30 | 1.625×10⁻¹² | 7.197×10⁻¹³ |
| 50 | 5.6×10⁻¹⁷ (machine zero) | 1.3×10⁻¹⁵ (machine zero) |

|λ₂| = 0.428764, so |θ| < 10⁻⁶ by **τ ≈ 13 steps**.

**The critical point: Panel B washes out too.** The order-0 Memory null of §2.2 is "the i.i.d. process
having the same one-time marginal" — which for a stationary run *preserves the stationary law by
construction*. So the mechanism intervention also converges to the same π, and its endpoint contrast also
decays to zero. §3's two-panel architecture is presented as the structure that keeps the contrasts
meaningful; it does not do that work here. The thing that determines whether the contrast survives is the
**outcome type**, which §3 does not mention at all.

Worse, in the fully stationary case (μ₀ = π, endpoint V) both panels give θ = **0 exactly at every τ**,
not merely asymptotically — because V_actual(τ) = π·viable for all τ and the null preserves π.

### 3.3 The escape hatch, and why it must be mandatory

A first-passage outcome is horizon-free and does not wash out. Same model, same μ₀, V = −E[T_hit]:

| contrast | θ |
|---|---|
| initial-state (Panel A) | **−2.154939** |
| mechanism (Panel B) | **+0.100751** |

Both nonzero, both τ-independent, and note they have **opposite signs** — the panels are genuinely
dissociated once the outcome type is right.

### 3.4 Disposition

Maps directly onto the contract's **own F2**: "`μ₀`, `V`, or the preserved quantities force `θ=0`.
Disposition: declaration error; repair before scientific interpretation." The contract has the right
failure condition and no rule that prevents a runner from walking into it. Repair (cheapest): add to §1
field 5 a mandatory **horizon-adequacy check** — if the intervention preserves the stationary law and V is
of endpoint/occupation type, the declaration must report |λ₂|^τ (or the mixing time) and is
**NOT EXECUTABLE** when τ exceeds the washout scale. Better: state in §3 that stationary-law-preserving
interventions require a path, survival, or first-passage outcome, and that endpoint outcomes are admissible
only with an explicitly non-ergodic or absorbing target.

---

## 4. A4 (fatal) — the mandated Integration reading is identically the forbidden one

### 4.1 Setup, verbatim

> "Every executable Integration case must select one reading before the run:
> - **Total correlation `TC`** across a fixed multi-part partition; or
> - **minimum-cut dependence `Φ_MIP`** under a fully declared partition search and normalization rule." (§2.4)

> "B5 across an internal cut is reported only as descriptive dependence, not as the Integration reading
> itself." (§2.4)

> "**B5 — cross-cut stored dependence:** `I(inside; outside)`. B5 is retained as a descriptive cross-cut
> quantity. It is **not boundary strength** and cannot replace B1/B2/B4." (§2.1)

### 4.2 The break

Total correlation over a partition into parts X₁ … X_m is TC = Σᵢ H(Xᵢ) − H(X₁…X_m). For **m = 2** this
is exactly H(X₁) + H(X₂) − H(X₁,X₂) = I(X₁;X₂) — which is precisely B5's definition applied to the
internal cut. Computed on random joint laws:

| partition | TC | B5 = I(in;out) | TC − B5 |
|---|---|---|---|
| 2 parts | 0.120720917 | 0.120720917 | **0.000×10⁰** |
| 3 parts | 0.202295478 | 0.118331323 | 8.396×10⁻² |
| 4 parts | 0.502948211 | 0.264746752 | 2.382×10⁻¹ |

The identity is exact, not numerical: for m = 2, TC ≡ I.

So on any **bipartition** — and §4.1 model 6 requires only "at least one internal partition", which a
bipartition satisfies — the contract simultaneously *mandates* TC as the Integration reading and
*forbids* the identical number as the Integration reading. A runner reporting a single number satisfies
one rule and violates the other, with no way to tell which.

This also collides with §2.4's own collapse test: "If its reading or viability response is completely
determined by repeating the Boundary operation over an internal cut, report **operator collapse / no
separate operational content**." On a bipartition the reading *is* the Boundary B5 quantity computed
over an internal cut — so §2.4's collapse condition is satisfied **by construction**, before any model
is run. The Integration extension self-retires on its own most natural instantiation.

### 4.3 Disposition

**Fatal to the Integration extension as specified**, and it maps onto the contract's own **F5**:
"chosen Integration reading and response are determined by the external-cut operation under relabeling.
Disposition: retire the extension from the measured core." Repair (cheapest, preserves the extension):
require m ≥ 3 for the TC reading, and state explicitly that TC on a bipartition is definitionally B5 and
is therefore **NOT DEFINED** as an Integration reading. That makes model 6's "at least one internal
partition" into "at least one internal partition into three or more parts" — a one-word change in §4.1
that saves the extension. Alternatively require Φ_MIP for bipartitions, but see the citation lane on
whether Φ_MIP's normalization is well-posed.

---

## 5. A5 (major) — three of the nine benchmarks have an identity Drive null

§4's applicability map marks Drive (`D`) as required (✓) on models 1, 2, 3 and 4. Computing the actual
processes:

| model | job per §4 | σ (actual) | is the DB projection the identity? | θ_D |
|---|---|---|---|---|
| 1 — i.i.d. finite-alphabet source | "all-null and estimator-bias control" | 1.6×10⁻¹⁷ (= 0) | **yes** — an i.i.d. chain is already detailed-balanced | **0 exactly** |
| 2 — reversible correlated order-1 chain | "Memory without Drive" | 2.1×10⁻¹⁷ (= 0) | **yes** — reversible by construction | **0 exactly** |
| 3 — Even Process | "infinite-order ladder" | 0.000 at windows L = 4, 6, 8 | **yes** — reversible | **0 exactly** |
| 4 — driven position ring | "Drive control" | 0.720000 | no | non-zero (but see A1/A2) |

For models 1–3 the intervention is the identity map, so θ_D = 0 **analytically, for every V and every τ**.
The contract's own **F2** says: "`μ₀`, `V`, or the preserved quantities force `θ=0`. Disposition:
declaration error; repair before scientific interpretation."

This is not a defect in the *models* — a σ = 0 control is exactly right for §5.1 tests 1 and 2, which ask
the i.i.d. source to "return `E=0` and `σ=0`" and the reversible chain to return "`E>0` and `σ=0`". Those
are **measurement** checks on σ, and they pass. The defect is that the map marks the Drive **contrast**
(θ_D) as required on models where the contrast is constructionally degenerate.

**Disposition: major, and cheap.** The map conflates "the Drive *reading* σ is defined here" with "the
Drive *contrast* θ_D is executable here". Repair: split the `D` column into `D-read` and `D-θ`, and mark
`D-θ` as `—` (not required, not defined) on models 1–3. That leaves model 4 as the *only* model carrying
the Drive contrast — which is worth stating plainly, because it means A1 and A2 are not one benchmark's
problem, they are the **entire** Drive evidence base.

---

## 6. A6 (major, stated reason) — "necessarily removes Drive" is false for the reversals §1 permits

### 6.1 Setup, verbatim

> "The full Memory null is **order 0**: replace the temporal mechanism with the i.i.d. process having the
> same one-time marginal. This drives `E` to zero but also changes kinetics and **necessarily removes
> Drive**." (§2.2)

> "**Representation and reversal:** observed state representation, coarse-graining, **even/odd variables**,
> and the time-reversal involution `R`." (§1 field 11)

### 6.2 The break

§1 field 11 explicitly admits **odd** variables — i.e. involutions R that act non-trivially on the state
space, the standard convention for velocities, currents and momenta. Take the three-symbol alphabet
{+v, −v, 0} with the odd involution +v ↔ −v, 0 fixed. For an i.i.d. source, σ per step is the KL
divergence between the one-time law and its R-image:

| i.i.d. marginal (the null's marginal, preserved by construction) | σ under **odd** R | σ under **even** R | E |
|---|---|---|---|
| (1/3, 1/3, 1/3) | 0.000000 | 0 | 0 |
| (0.5, 0.3, 0.2) | **0.147393 bits/step** | 0 | 0 |
| (0.7, 0.1, 0.2) | **1.684413 bits/step** | 0 | 0 |

The order-0 Memory null preserves the one-time marginal *by construction* (§2.2). If that marginal is
asymmetric under the declared odd involution, σ **survives the null intact**. The null removes E
(exactly, to 0) but does not remove Drive.

### 6.3 Why this is a reason-defect, not a decision-defect

The *decision* — to report the order-0 null's lack of selectivity — is correct and v0.2.2 deserves credit
for stating it ("That lack of selectivity is reported, not hidden"). What is false is the **universal
quantifier**: "necessarily". Under the even reversal (the implicit default) the claim holds; under the odd
reversals field 11 admits, it does not. A contract whose stated rationale is false in a case its own
declaration block permits invites a runner to skip the σ measurement on the null — precisely the check
that would catch it.

**Disposition: major (stated reason).** Repair: replace "necessarily removes Drive" with "removes Drive
whenever the declared reversal `R` is even on the observed representation; under an odd `R` the null's
preserved one-time marginal may retain σ > 0, and σ must therefore be measured on the null as well as on
the actual process." Add σ-on-the-null to §6.4's required outputs.

---

## 7. A7 (minor) — the ladder is trivial on model 4

§4 marks Memory (`M`) as required on model 4, and §2.2 specifies the order-k projection ladder. But the
driven ring is a **first-order Markov chain on positions**. Therefore M₁ = the original process, E(M₁) = E
exactly, and ρ_k = 0 for every k ≥ 1. Rungs k ≥ 2 carry no diagnostic content on this model; the entire
ladder collapses to its first rung.

This is not wrong — §2.2 says "For a finite-order process it should reach zero at sufficient `k`", and
this is that case, with sufficient k = 1. It is a **coverage** observation: models 1 and 4 are order-0 and
order-1, model 2 is order-1, so the only benchmark exercising the ladder as a *ladder* is model 3 (Even
Process). §4's `✓` in the M column overstates how much ladder evidence models 1, 2 and 4 supply.

**Disposition: minor.** Repair: annotate the map's M column with each model's Markov order, so a reader
sees at a glance that ladder evidence rests on model 3 alone.

---

## 8. What I could not break — the failed-attacks ledger

This section is not politeness. These are attacks I ran and lost, and they mark the parts of v0.2.2 that
are load-bearing and safe to build on.

**8.1 The Even-Process repair is CORRECT, and it is the single best fix in v0.2.2.**
v0.2.1 said the residual "never saturates"; my v0.1 report found that fatal to the stated rationale.
v0.2.2 now says: "For the Even Process it is expected to remain positive at every finite `k` while tending
toward zero asymptotically; that behavior is not failure." I attacked this and **could not break it** —
it is exactly right on both halves:

| k | ρ_k (exact upper bound, bits) | ratio ρ_k/ρ_{k−1} |
|---|---|---|
| 1 | 0.8751338815 | 0.95201 |
| 4 | 0.4821515911 | 0.74687 |
| 8 | 0.1841565385 | 0.69268 |
| 12 | 0.0624773065 | 0.67096 |
| 14 | 0.0356445916 | 0.66604 |
| 15 | 0.0304754 | — |

Positive at every finite k ≤ 15: **true**. Summable, hence ρ_k → 0: **true** (two-rung ratio 0.583333,
consistent with the k·2^(−k/2) law). E(μ) bracketed in **[0.9124844, 0.9192443]** bits. The distinction
between "infinite Markov order" and "non-summable residual" is now drawn correctly, and the sentence
"that behavior is not failure" pre-empts the false-refutation reading. This row of the repair ledger is
fully discharged on the analytic evidence.

**8.2 The increment-representation trap is genuinely closed.** §2.3 fixes position space and says "A
change of representation is a change of the scientific question, not a harmless coding choice." I tried
to get the trap to fire anyway and could not. For the record the trap is real — in the increment
representation the same ring gives σ = 0.720000 (preserved) and E = **0.000000 exactly**, which would be
a false refutation of the canon's σ>0 ⇒ E>0 result — and v0.2.2's declaration now excludes it by name.
This was fatal finding F0a against v0.2.1 and it is **discharged**.

**8.3 The applicability map's `—` entries for Boundary and Integration on models 1–4 are correct.**
I tried to show the map was over-cautious. It is not: the Type-A product scramble needs a factorizable
state space, and models 1–4 have state-space sizes 3, 3, 2 and 3 — **all prime**, no non-trivial
factorization. The cut is undefined and the contrast cannot run. The map is right, and v0.2.2's replacement
of "every contrast on every model" with an applicability map is a genuine structural improvement over
v0.2.1.

**8.4 σ = 0.720000 bits on the ring is exact and survives every attack.** The *reading* is robust; only
the *contrast* built on it (A1, A2) fails. This distinction matters for the gate disposition: the Drive
**measurement** is sound.

**8.5 The B1/B2/B4/B5 restoration holds up.** §2.1's explicit "If no interface `F` or maintenance model
exists, B2 or B4 is **NOT DEFINED** for that model; do not silently substitute B5" closes the v0.2.1 defect
directly. I could not construct a case where a runner following §2.1 substitutes B5 for boundary strength
without violating a stated rule. (Whether B5's demotion matches canon is the fidelity lane's call, not mine.)

**8.6 The status vocabulary is genuinely useful.** I tried to find a measurement outcome that none of
ESTIMATED / ANALYTIC / NOT DEFINED / NOT EXECUTABLE / UNRESOLVED can express, and failed. The five labels
cover the space. In particular NOT EXECUTABLE ≠ zero is stated twice (§1, §4) and is the right refusal.

**8.7 A finding of mine vindicates one of the contract's categories rather than refuting it.** A3's
washout is *exactly* what F2 describes, and A1/A2's sign instability is *exactly* what F7 describes. The
contract predicted both failure modes correctly; what it lacks is a rule that stops a runner from walking
into them. That is a much smaller repair than a new failure condition, and it is to v0.2.2's credit that
the categories were already there to receive these findings.

**8.8 §6.3's mutation-test requirement is well-aimed.** "A check that inverts the same function it
validates is not independent" is the correct statement of the problem, and the seeded-defect list (wrong
lag, wrong reversal, wrong target, ignored horizon, changed entropy-production factor, transposed
generator, changed state representation) covers every defect class I exploited in this report except
null non-uniqueness — which is A1's point, and which I would add to that list as an eighth seed.

---

## 9. Dispositions

| id | finding | grade | contract's own hook | cheapest repair |
|---|---|---|---|---|
| A1 | Drive null non-unique by a 3-parameter family; θ_D spans −47.62 to +0.298 across 13,824 valid nulls, 5.3% positive | **fatal** | F7; §1 field 7 | new field 7a recording the null-selection rule; §6.4 reports θ under ≥2 alternative nulls; straddling zero ⇒ UNRESOLVED |
| A2 | θ_D flips sign with target choice at fixed null (−0.952 vs +0.238) | **fatal** | F7; §1 field 6 | θ_D reported per declared event; no aggregate sign claim; §5.1 test 4 runs both orientations |
| A3 | Endpoint V + stationary-law-preserving intervention ⇒ θ → 0 geometrically in **both** panels | **fatal** | F2 | horizon-adequacy check in §1 field 5; endpoint outcomes NOT EXECUTABLE past the washout scale |
| A4 | TC ≡ B5 on any bipartition — the mandated reading is the forbidden one; §2.4's collapse test fires by construction | **fatal** | F5; §2.4 | require m ≥ 3 parts for the TC reading; declare TC-on-bipartition NOT DEFINED as an Integration reading |
| A5 | Drive null is the identity on models 1–3 ⇒ θ_D = 0 analytically | **major** | F2 | split map's `D` column into `D-read` / `D-θ`; mark `D-θ` as `—` on models 1–3 |
| A6 | "necessarily removes Drive" false under odd reversals §1 field 11 permits (σ up to 1.684 bits survives) | **major** (reason) | §2.2 | qualify to even-`R`; require σ measured on the null |
| A7 | Ring is order-1 ⇒ ρ_k = 0 for k ≥ 1; ladder trivial on model 4 | **minor** | §2.2, §4 | annotate map's M column with each model's Markov order |

**Gate verdict from this lane alone (§7 vocabulary):**

- Memory contrast — **family survives**. The Even-Process repair is correct; the ladder is analytically sound.
- Boundary contrast — **not assessed by this lane** beyond A3 (the panel is restored; instantiation is the fidelity lane's call).
- Drive contrast — **gate not executable** until A1 and A2 are repaired. θ_D is not currently a function of the declaration.
- Integration extension — **gate not executable**, and on the bipartition case **F5 fires by construction** (A4).

None of these reject AOP. Per §5.2, "These conditions are fatal only to the stated co-measurement or
contrast claim." A1–A4 bound what the *contract* can claim; the canon's σ and E readings are untouched.

---

## 10. Reproduction

All results are closed-form. Helpers are from the `adversarial-break-attempt` skill kernel; formulas are
named so another seat can rerun independently.

**Ring (A1, A2, A5, A7).** `driven_ring(a, b, n)` — rate a forward, b backward, remainder stays;
stationary law uniform by cyclic symmetry for all (a, b). σ from `chain_sigma_bits(P)` =
Σᵢⱼ πᵢPᵢⱼ log₂(πᵢPᵢⱼ / πⱼPⱼᵢ). E from `chain_excess_entropy_bits(P)` = I(X₀;X₁) for a first-order chain.
MFPT by exact linear solve (I − Q)t = 1 on the non-target states, `ring_mfpt(P, start, target)`.
Parameters (a, b, n) = (0.48, 0.12, 3). Reference values: σ = 0.720000, E = 0.180855,
MFPT(0→1) = 2.380952, MFPT(0→2) = 3.571429, affinity 3 ln(a/b) = 4.158883 nats.

**Null family sweep (A1).** Symmetric-weight ring P[0,1]=P[1,0]=x, P[1,2]=P[2,1]=y, P[2,0]=P[0,2]=z,
diagonal = 1 − row sum. Grid: 24 points linearly spaced on [0.02, 0.48] in each of x, y, z (13,824
combinations, all admissible). Retained only chains with |σ| < 10⁻⁹. V = −MFPT(0→1);
θ_D = V_null − V_actual. Zero crossing of the one-parameter sub-family at c\* = 1/MFPT_actual = 0.420000.

**Panel washout (A3).** 4-state chain P drawn from Dirichlet(0.8) rows, seed `np.random.seed(0)`;
π from the left Perron eigenvector; inside = {0,1}, outside = {2,3}; viable set = {0,1}.
μ₀ = (0.55, 0.05, 0.10, 0.30) non-stationary; product scramble preserves both within-side marginals,
giving (0.39, 0.21, 0.26, 0.14). Endpoint V(τ) = μ₀P^τ · 1_viable. Mechanism null = i.i.d. chain with rows
equal to π. First-passage V = −μ₀·t where (I − Q)t = 1 for absorbing target {3}. |λ₂| = 0.428764.

**TC vs B5 (A4).** TC = Σᵢ H(Xᵢ) − H(X₁…X_m) on Dirichlet(0.7) joint laws over m binary parts,
`default_rng(7)`; B5 = I(part 0; rest). Identity for m = 2: TC = H(X₁)+H(X₂)−H(X₁,X₂) = I(X₁;X₂).

**Even Process / Golden Mean ladder (A7, §8.1).** `even_process_matrices(0.5)`, `golden_mean_matrices(0.5)`
→ `hmm_block_entropies(mats, 22)` → `markov_ladder(H)`. E(M_k) = H(k) − k[H(k+1) − H(k)], exact at each k.
ρ_k reported as the bracketed upper bound, never extrapolated. Golden Mean E = 0.2516291674 with increments
< 7.4×10⁻¹² for k ≥ 1 (exact saturation at k = 1). Even Process E ∈ [0.9124844, 0.9192443],
two-rung ratio 0.583333.

**Odd-reversal σ (A6).** For an i.i.d. source with one-time law p and involution ι, σ per step =
Σᵢ pᵢ log₂(pᵢ / p_{ι(i)}). Alphabet {+v, −v, 0}, ι = (+v ↔ −v, 0 fixed).

**Factorizability (§8.3).** State-space sizes 3, 3, 2, 3 for models 1–4; trial division confirms all prime.
