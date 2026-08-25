# Break attempt — AOP Intervention Contract v0.2.2

**README / synthesis · v1.0 · 2026-08-08**

**Target:** `AOP_InterventionContract_ThreeCorePlusExtension_v0.2.2_20260807.md`
(Drive id `1G11FteSv7yqcqHlyM0oqb2uLwOknlNLc`, 21,281 B as stored, 21,036 B unescaped)
**Parent consulted:** `AOP_CANON_MASTER_v1.27.md` (Drive id `1jnqgjhCg6X-7FzOSEEZWM4V40ck7xty_`, md5 `998aa87e0927f84ae6ea1676ebe8ca93`)

**Exclusion declaration.** The seat that built v0.2.2 did not grade it. This seat did build the v0.1
break attempt on v0.2.1 that v0.2.2's §8 ledger answers, so the ledger-discharge audit was run by an
independent lane, not by this seat. The analytic lane's findings are this seat's own.

---

## 0. Verdict

**On the contract's own §7 vocabulary: `gate not executable`.**

Not "contract fails". The distinction matters and is deliberate. v0.2.2's architecture is sound and
several of its repairs are genuinely correct — the Even-Process fix is exactly right and independently
corroborated three ways. What blocks the gate is that **three of the four contrasts cannot currently be
run to a reproducible number**, and one mandatory reporting field cannot be filled by any seat holding
only this document.

Per contrast:

| contrast | verdict | why |
|---|---|---|
| **Memory** | **family survives** | The ladder is analytically sound; the Even-Process repair is correct. Two benchmark traps to close (C4, C5). |
| **Boundary** | **survives with named reduction** | Panel restored correctly. B4 is decoupled from its canon identification (M-6). |
| **Drive** | **gate not executable** | θ_D is not a function of the declaration: sign flips with an unrecorded null choice (A1) and with target choice (A2). |
| **Integration** | **gate not executable; F5 fires by construction** | The mandated reading is identically the forbidden one on any bipartition (A4). |

**Above the contract, one finding outranks everything below it — see §1.**

---

## 1. The canon-version finding (read this first)

The Drive-master file is named `AOP_CANON_MASTER_v1.27.md`. Its body is **v1.26**, and that body
closes by declaring itself unratified. Verified directly against the file, not inferred:

- Masthead (line 12): `version 1.26 · compiled 25 July 2026`.
- Last changelog entry (line 837): **Version 1.26 (25 July 2026)**. There is no v1.27 entry, masthead, or change list.
- The only `1.27` string in 851 lines is a forward reference inside the D→M passage (line 443): "five of them as of v1.27".
- Closing status (line 849): **"This version is a proposal, not canon. It was built by the execution seat against a specified order and is not self-certified: prime verifies line-by-line against the order and the changeset, and Ben decides."**

Two consequences, and one honest limit:

1. **The startup discipline's "confirm currency, not just access" check does not pass on filename alone.**
   The charter warns that ticking "read the canon" against a stale copy is the failure the block exists
   to prevent. Here the failure mode is subtler: the filename asserts a version the body does not carry.
2. **Canon did not move between the two break attempts.** A normalized diff of this file against the copy
   the v0.2.1 lane used shows zero substantive differences across 850 lines. So no prior finding is stale
   on canon grounds, and **no v0.2.2 defect can be excused as canon drift**.
3. **Limit, stated honestly:** whether a ratified v1.27 exists elsewhere is **NOT VERIFIED**. No adoption
   record was retrieved and none was assumed. If one exists, every FAITHFUL grade in the fidelity audit
   must be re-run against it.

**Cheapest repair:** either rename the file to match its body, or promote and stamp a real v1.27 with a
masthead and changelog entry. Until then, "canon v1.27 §N" locators point at a version string with no
masthead behind it.

---

## 2. Fatal findings

Seven fatal findings across three independent lanes. Each is graded against the contract's **own**
failure conditions, and each carries a concrete cheapest repair.

### Analytic lane (closed-form; every number exact, no estimator)

**A1 — the Drive null is non-unique by a three-parameter family, and θ_D changes sign inside it. → F7**
The ring's stationary law is uniform for *every* (a, b) by cyclic symmetry, so "detailed balance at fixed
stationary distribution" reduces to *any* symmetric edge-weight assignment. One fully-filled declaration
admits **13,824 admissible nulls**, all with σ = 0 and the identical stationary law, with **θ_D spanning
−47.62 to +0.298** — 5.3% of them positive. Four one-line null rules, each defensible prose in field 7,
give θ_D = −0.952, −1.786, **+0.298**, −5.952. §2.3 says non-uniqueness "must be resolved in `D`" but §1
has **no field that records which resolution was used**. Two seats filling all fourteen fields correctly
get opposite-signed answers and both pass every check in the document.
*Repair:* field 7a recording the null-selection rule and its admissible alternatives; §6.4 reports θ under
≥2 nulls; an interval straddling zero ⇒ UNRESOLVED. The ring then honestly reports UNRESOLVED.

**A2 — θ_D flips sign with target choice at a *fixed* null. → F7**
Same system, same σ, same null, same sign convention: first passage 0→1 (with the current) gives
θ_D = **−0.952381**; 0→2 (against it) gives **+0.238095**. Both events are declared to the letter of §1
field 6. §2.3's repair makes each run reproducible but does not make runs **comparable**.
*Repair:* θ_D reported per declared event, no aggregate sign claim across events, and §5.1 test 4 runs both
orientations — which converts the defect into a positive control the contract would be stronger for having.

**A3 — under an endpoint outcome BOTH panels wash out. → F2**
Any stationary-law-preserving intervention has μP^τ → π regardless of μ, so θ decays as |λ₂|^τ to exactly
zero. Measured: |θ| falls from 4.76×10⁻² at τ=1 to machine zero by τ=50, with |θ| < 10⁻⁶ by **τ ≈ 13 steps**.
Critically **Panel B washes out too** — the order-0 Memory null is i.i.d. with the same one-time marginal,
so it preserves π by construction. §3's two-panel split is presented as the structure that keeps contrasts
meaningful; it does not do that work. With μ₀ = π and an endpoint V, θ = 0 *exactly at every τ*.
The escape hatch is the **outcome type**, which §3 never mentions: on a first-passage V the same model
gives θ_A = −2.155 and θ_B = +0.101, horizon-free and opposite-signed.
*Repair:* mandatory horizon-adequacy check in field 5; endpoint outcomes NOT EXECUTABLE past the washout scale.

**A4 — the mandated Integration reading is identically the forbidden one. → F5**
For a two-part partition, TC = H(X₁)+H(X₂)−H(X₁,X₂) = I(X₁;X₂) — which *is* B5 applied to the internal cut.
Computed: TC − B5 = **0.000×10⁰** on a bipartition (0.084 and 0.238 for 3 and 4 parts). §2.4 mandates TC as
an Integration reading and forbids B5 as one. §4.1 model 6 requires only "at least one internal partition",
which a bipartition satisfies. Worse, §2.4's own collapse test — "if its reading ... is completely determined
by repeating the Boundary operation over an internal cut, report operator collapse" — is then satisfied
**before any model is run**. The extension self-retires on its most natural instantiation.
*Repair:* require m ≥ 3 parts for the TC reading; declare TC-on-a-bipartition NOT DEFINED as an Integration
reading. A one-word change in §4.1 saves the extension.

### Fidelity lane (independent seat; graded against canon verbatim)

**F-1 — v0.2.2 deleted its entire source apparatus, and ledger row 12 states the opposite. → F3 / §7**
Counts, verified independently by this seat against the target file: section locators **56 → 1**; numbered
references **6 → 0**; named external sources **21 → 1**; DOI/arXiv/URL occurrences **0**. Ledger row 12
records "governance mixed into science → removed session housekeeping; retained only scientific status and
gate rule." The governance half *was* correctly removed — but the **source ledger went with it**, which the
row does not say. Consequence: §6.4 item 11 requires every report to record "known theorem envelope and
whether the case is inside it", and no reader holding only this document can do so.
*Repair:* a §9 source ledger — one row per canon-derived commitment with version, section, and the quoted
sentence (~20 rows). Nothing else changes; the governance separation is preserved.

**F-2 — two structural commitments sit outside the scope canon establishes for them. → F3**
(i) Canon §3: "Coalitions are the default object; per-edge weights are the exception", retained only where
additivity and identifiability tests pass, inside a measured band. v0.2.2 has **zero** occurrences of
"coalition", "mask", or "additivity" and states no band, while instrumenting exactly the per-edge layer
v1.26 demoted. (ii) Canon §4 establishes minimum-cut dependence "only in the static Gaussian setting and only
at a fixed partition"; §2.4 offers Φ_MIP on model 6, an arbitrary multipart model, with no frontier flag.
*Repair:* two sentences — flag non-TC Integration readings and any off-Gaussian Φ_MIP as frontier; state that
the contract instruments the per-edge layer and inherits canon's band.

**F-3 — the D→M theorem is presupposed and stated nowhere; the current-shortens-persistence envelope is
invoked with zero of its five conditions. → §6.4 items 11–12 unexecutable**
The §4 map assigns model 4 the "forced Drive–Memory cross-effect" and §5.1 calibrates against it, but v0.2.2
names no theorem, no direction σ>0 ⇒ E>0, and none of canon's five scope conditions — of which time-reversal
parity is precisely what makes §1 field 11's `R` load-bearing. **This is a regression:** v0.2.1 stated five of
five D→M conditions and two of five envelope conditions.
*Repair:* one boxed subsection reproducing both envelopes verbatim from canon with locators.

### Citation lane (primary sources read, not titles)

**C1 — the σ_Δ definition is transcribed faithfully but loses its bound under the contract's own field 11.**
Roldán & Parrondo (Phys Rev E 85:031129, 2012) establish that for observables rather than the microstate,
the KL divergence **only lower-bounds** entropy production, saturating only at the microstate with infinite
sampling. §1 field 11 explicitly licenses declared coarse-graining; §2.3 then calls the result "entropy
production" with no bound language. Model 4's position-space declaration is exactly such a reduction.
*Repair:* state σ_Δ as a lower bound under coarse-graining, citing Roldán & Parrondo Eq. (12).

**C2 — "any current-shortens-persistence theorem" is an uncitable theorem invoked by description.**
Mechanically searched: the 21 KB document contains **zero** author names, years, DOIs, arXiv ids, or bracketed
references. The theorem is real and canon §12 states its envelope (measure-preserving/divergence-free current
at fixed stationary distribution, ∇U·ℓ = 0, small-noise limit, MFPT primitive, fixed dynamical activity). The
contract strips the name and the envelope and keeps only the hedge. Compounds F-3.

**C3 — Φ_MIP's normalization gap is confirmed against primary sources.** Tononi (BMC Neurosci 5:42, 2004)
normalizes only the *argmin* — Φ itself is "the (non-normalized) value of EI(A↔B) for the minimum information
bipartition". Two harnesses can both satisfy §2.4's "fully declared normalization rule" and report different
numbers, so a declared rule buys **reproducibility, not comparability** — and §5.2 F5 can turn on which rule
was chosen. Mediano/Rosas et al. (arXiv:2109.13186) further show Φ^WMS can go **negative** for redundancy
reasons unrelated to viability, while TC is non-negative by construction. The two are offered as
interchangeable and are not; §5.1 test 8's signed control is confounded by the choice.

**C4 — the Even Process's only published E value disagrees with the exact one, by construction.**
Exact: **E = log₂3 − 2/3 = 0.918295834054**. Independently confirmed by this seat: the value falls inside the
analytic lane's bracket [0.9124844, 0.9192443], while C&F's published **0.902** falls **outside** it (low by
1.77%). §6.1's analytic-first rule therefore guarantees a compliant harness will disagree with the literature
number a runner is most likely to check against.
*Repair:* deposit the exact value in the benchmark declaration and note the published estimate is numerical.

**C5 — the wrong-lag mutation is undetectable on the Even Process.**
E = H(1) exactly on this process — both equal log₂3 − 2/3. Confirmed by this seat: difference **1.11×10⁻¹⁶**.
§6.3 requires the suite to catch a seeded "wrong lag" defect; on this benchmark that defect **cannot** be caught.
*Repair:* seed the wrong-lag mutation on a benchmark where E ≠ H(1) — the Golden Mean process works.

---

## 3. Selected major findings

- **A5 → F2.** The Drive null is the **identity map** on models 1, 2 and 3 (all σ = 0: 1.6×10⁻¹⁷, 2.1×10⁻¹⁷,
  0.000), so θ_D = 0 analytically — which F2 calls a declaration error. The §4 map marks Drive required on all
  three. This conflates "the σ *reading* is defined here" with "the θ_D *contrast* is executable here", and it
  means **model 4 is the entire Drive evidence base** — so A1 and A2 are not one benchmark's problem.
  *Repair:* split the map's `D` column into `D-read` and `D-θ`.
- **A6 → §2.2 rationale.** "This ... **necessarily** removes Drive" is **false** for the reversals §1 field 11
  permits. Under an odd involution (+v ↔ −v), the order-0 null preserves the one-time marginal by construction,
  so σ survives: **0.147 and 1.684 bits/step** for two ordinary marginals, with E driven to exactly 0. The
  *decision* to report the null's lack of selectivity is right; the universal quantifier is wrong.
- **M-1.** §4's coverage guarantee ("every contrast has at least one positive control") is **false for
  Integration** — it is required on exactly one row, model 6, whose job is a *failure* test. F5's disposition
  (retire the extension) becomes reachable for the wrong reason.
- **M-2.** Model 1's Memory null is the identity map, and the document gives that one analytic fact **three
  incompatible readings**: §0 calls a zero a result, §5.1 test 1 calls it a calibration pass, F2 calls it a
  declaration error. No rule assigns which.
- **M-3.** **F7 has no test that exercises it** — §4.1 declares away the target choice F7 needs varied, and
  §6.4 item 10's sensitivity list omits the outcome event entirely. A failure condition written for the prior
  attempt's central finding, which no test can trigger.
- **M-4.** Three status vocabularies with no crosswalk; `OUTSIDE DOMAIN` appears in §4.1 and F3 but in neither
  status list; ANALYTIC vs ESTIMATED has no assignment rule.
- **M-5.** Canon states TC = I(inside;outside) + TC_inside + TC_outside and warns B5 "is an algebraic component
  of Integration". v0.2.2 reports both with no statement of the nesting — the independent route to A4.

---

## 4. What could not be broken

Named specifically, because this is what makes the fatal findings credible.

1. **The Even-Process repair is correct — the single best fix in v0.2.2, and it is correct on both halves.**
   v0.2.1 said the residual "never saturates"; that was fatal to the stated rationale. v0.2.2 now says it
   "remains positive at every finite `k` while tending toward zero asymptotically; that behavior is not
   failure." Attacked and could not be broken, and **independently corroborated three ways**: this seat's exact
   ladder (ρ_k positive at every k ≤ 15, summable, two-rung ratio 0.583333), the citation lane's belief-state
   DP to L = 4000, and C&F's own published fit γ = 0.501 ± 0.007. The infinite-Markov-order / non-summable-
   residual conflation is now correctly separated, and "that behavior is not failure" pre-empts the false-
   refutation reading.
2. **The increment-representation trap is genuinely closed.** The trap is real — in increments the same ring
   gives σ = 0.720000 (preserved) and E = **0.000000 exactly**, a false refutation of canon's σ>0 ⇒ E>0. §2.3
   now fixes position space by name and adds "A change of representation is a change of the scientific
   question, not a harmless coding choice." Prior fatal F0a: **discharged**.
3. **The applicability map's `—` entries for Boundary and Integration on models 1–4 are correct.** Tried to show
   over-caution; failed. The product scramble needs a factorizable state space and those models have sizes
   3, 3, 2, 3 — **all prime**. The cut is undefined and the contrast genuinely cannot run.
4. **σ = 0.720000 bits on the ring is exact and survives every attack.** The Drive *reading* is sound; only the
   *contrast* built on it fails. This is why the Drive verdict is "gate not executable", not "contract fails".
5. **The B1/B2/B4/B5 restoration holds.** "If no interface `F` or maintenance model exists, B2 or B4 is NOT
   DEFINED; do not silently substitute B5" closes prior fatal F0b directly. No compliant substitution could be
   constructed.
6. **The Kolchinsky–Wolpert sign claim is VERIFIED.** Their Eq. (6) is actual-minus-intervened; the contract's
   intervened-minus-actual is correctly described as the reverse. (One qualification: sign is not the *only*
   difference — K&W fix V := −S(p) and fix the intervention class, so §0 should state the comparison condition
   too. That is a PARTIAL, not a refutation.)
7. **The status vocabulary is expressive.** Tried to find a measurement outcome none of the five labels can
   express, and failed. "NOT EXECUTABLE ≠ zero" is stated twice and is the right refusal.
8. **§6.3's mutation-test requirement is well-aimed.** "A check that inverts the same function it validates is
   not independent" is the correct statement of the problem. Its seeded-defect list covers every defect class
   exploited here except null non-uniqueness — which would be a good eighth seed.
9. **Two findings vindicate the contract's own categories rather than refuting them.** A3 is *exactly* what F2
   describes; A1/A2 are *exactly* what F7 describes. The contract predicted both failure modes correctly. What
   it lacks is a rule stopping a runner from walking into them — a far smaller repair than a new failure
   condition, and to v0.2.2's credit that the categories were already there to receive these findings.

---

## 5. Cheapest path to a runnable gate

Ordered by cost, not by severity. None of these is a rewrite.

1. **Field 7a** — record the null-selection rule and its alternatives; report θ under ≥2 nulls (A1).
2. **One word in §4.1** — "at least one internal partition **into three or more parts**" (A4).
3. **One sentence in §1 field 5** — horizon-adequacy check for stationary-law-preserving interventions (A3).
4. **Split the map's `D` column** into `D-read` / `D-θ`; mark `D-θ` as `—` on models 1–3 (A5).
5. **Add the outcome event** to §6.4 item 10's sensitivity sweep; run model 4 on both targets (A2, M-3).
6. **A §9 source ledger**, ~20 rows, canon version + section + quoted sentence (F-1, F-3, C2).
7. **Qualify "necessarily removes Drive"** to even-`R`, and require σ measured on the null (A6).
8. **Deposit E(Even) = log₂3 − 2/3 exactly**; move the wrong-lag mutation seed to the Golden Mean (C4, C5).
9. **Rename the canon master, or promote a real v1.27** (§1).

Items 1–5 are what stand between v0.2.2 and a Drive/Integration gate that returns a reproducible number.

---

## 6. Lane completeness — stated plainly

All three lanes ran to completion. Nothing here is a synthesized or stopped-lane verdict.

- **Analytic lane** — complete. Every number closed-form; reproduction formulas in `AOP_Break_MathAttack_v0.2.md` §10.
- **Fidelity lane** — complete: 27 cross-references graded, all 13 ledger rows discharged, 11 silent drops, 15 failed attacks.
- **Citation lane** — complete, **with named gaps honestly recorded as NOT VERIFIED, not as passes**: Watanabe 1960
  (closed access, no OA location found — TC's attribution therefore unread); Fill 1991 (PDF retrieved but no text
  layer, so the additive-reversibilization definition was not read); B2's screening anchors (Pearl 1988, Faes et
  al. 2017 — not read in this lane); and both current-shortens-persistence primaries (not read; the canon's
  statement of the envelope was read instead).
- **Borrowed fatal findings re-verified by this seat before entering this README:** the canon-version claim
  (checked against the file's masthead, changelog and closing status), the E = log₂3 − 2/3 value (inside this
  seat's independent bracket; C&F's 0.902 outside it), the E = H(1) identity (difference 1.11×10⁻¹⁶), and F-1's
  citation counts (0 DOIs, 0 numbered refs, 1 external name, 1 section locator).

---

## 7. Files

| file | contents |
|---|---|
| `README_AOP_BreakAttempt_v022_v1.0.md` | this synthesis |
| `AOP_Break_MathAttack_v0.2.md` | analytic lane — 7 findings, failed-attacks ledger, dispositions, full reproduction section |
| `AOP_Break_FidelityAudit_v0.2.md` | fidelity lane — cross-reference table, 13-row ledger discharge, silent drops, failed attacks |
| `AOP_Break_CitationSalvage_v0.2.md` | citation lane — per-item verdicts with locating quotes, NOT-VERIFIED table, uncited-claims list |
| `AOP_Break_v022_Figure_v0.1.png` | three panels: null non-uniqueness, horizon washout, Even-Process residual decay |

**Version-stamp note.** Reports carry `_v0.2` (findings against target v0.2.2, second break attempt in the
lineage); the README carries `_v1.0` on its own lineage, matching the convention used for the v0.2.1 attempt.

---

*Independent break attempt. Non-canon. Authorizes no canon edits and certifies nothing. Per §5.2, these
conditions are fatal only to the stated co-measurement or contrast claims — they do not by themselves reject AOP.*
