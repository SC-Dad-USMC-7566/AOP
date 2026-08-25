# AOP Break — Fidelity Audit of `AOP Intervention Contract v0.2.2` (v0.2)

**Seat:** fidelity lane, independent adversarial break attempt. **This seat did not build v0.2.1 or v0.2.2.**
**Date:** 2026-08-08. **Non-canon. Authorizes no canon edits.**

**Target:** `AOP_contract_v0.2.2_target.md` — *AOP Intervention Contract — three core contrasts plus one internal-cut extension (v0.2.2)*, issued 2026-08-07, 21,269 bytes, 288 lines.
**Parent authority:** `AOP_CANON_MASTER_v1.27` as supplied (`v16163027_canon_v127_A.md`, 255,684 bytes, 851 lines). See §0 for the version verdict — the filename and the document body disagree.
**Prior break attempt (v0.2.1), read in full:** `AOP_Break_FidelityAudit_v0.1.md` (67,315 B), `AOP_Break_MathAttack_v0.1.md` (34,638 B), `AOP_Break_CitationSalvage_v0.1.md` (13,082 B).
**Also read:** `REV_AOP_InterventionContract_v0.2_GateReadiness` (`aster_gatereadiness.md`, 11,990 B) and `contract_v021.md` (25,069 B), to establish what the ledger rows are claiming to repair.

**Lane discipline.** Another seat is verifying external literature citations; the analytic lane is running closed-form counterexamples on the ring / Even Process / Markov ladder. Neither is duplicated here. Every canon quotation below is verbatim, ≤25 words, with a locating section. Nothing in this report rests on a passage I did not open.

---

## 0. Canon version verdict — establish this before reading anything else

The task named the parent file `AOP_CANON_MASTER_v1.27.md` and flagged that its front matter self-reports 1.26. That is correct, and the resolution is not a typo.

| Evidence | Location | What it says |
|---|---|---|
| Masthead | line 12 | "version 1.26 · compiled 25 July 2026" |
| Last changelog entry | line 837 | **Version 1.26 (25 July 2026)** — no v1.27 entry exists |
| Changelog closing | line 849 | "This version is a **proposal**, not canon" |
| Body forward-reference | line 443 | "scope conditions in §4 — five of them as of v1.27" |

**Verdict: the supplied file is a v1.26 body carrying one forward-reference to a v1.27 that the document does not otherwise contain.** There is no v1.27 changelog entry, no v1.27 masthead, and no v1.27 change list. Two consequences bind this whole audit:

1. **The highest version this file establishes is v1.26**, and v1.26 self-declares as a **proposal pending line-check and Ben's decision** (line 849), not as adopted canon. Every "canon says" verdict below is therefore "the v1.26 proposal body says," and a v0.2.2 claim graded FAITHFUL here is faithful to a document that has not itself been ratified. This is a **NOT VERIFIED** item, not a defect in v0.2.2: I could not retrieve a ratification record and did not assume one.
2. **The v1.27 filename is a claim the body does not support.** Any downstream document that cites "canon v1.27 §N" — as v0.2.1 did nineteen times — is citing a version string with no masthead behind it.

**Canon did not move between the two break attempts.** I diffed this file against the canon copy the v0.2.1 lane worked from (`canon_v127.md`, 255,605 B): **zero substantive differences** (whitespace only, after normalization). So no v0.2.2 finding can be excused as "canon changed underneath it," and no prior finding is stale on canon grounds.

**One canon-internal inconsistency, inherited not introduced.** §4 numbers the time-reversal parity condition **third** (line 124: "**Third — a time-reversal parity condition, new in v1.26.**") while §12″ calls it "**the fourth scope condition of the D→M theorem (§4)**" (line 593). Flagged in the v0.2.1 audit as A7; still unrepaired. Not a v0.2.2 defect — v0.2.2 states no scope conditions at all, which is its own finding (X7).

---

## 1. The finding that governs the rest

**v0.2.2 contains zero canon locators, zero citations, and zero references.**

| String | v0.2.1 | v0.2.2 |
|---|---:|---:|
| `§` (section pointer) | 56 | **1** |
| "canon" | 22 | 7 (all boilerplate: "non-canon", "canonical reading") |
| numbered references `[n]` | 6 | **0** |
| named external sources (Crutchfield, K&W, …) | 21 | **1** (unlocated) |
| doi / arXiv / URL | — | **0** |

The document's single named external appeal is "the Kolchinsky–Wolpert value convention," with no citation, no equation, no section. Every other structural commitment — the Boundary panel, excess entropy as the Memory reading, σ against a declared R, TC and Φ_MIP as Integration readings, the increment-representation rule, the "current-shortens-persistence theorem" and its envelope — is asserted bare.

This is the direct cost of ledger row 12. Aster item 8 asked to "Keep the contract limited to scientific definitions, declarations, models, tests, failure criteria, and source ledger." v0.2.2 removed the governance material (verified: zero occurrences of "Ben", "Aster", "seat", "§11", "OPEN", "self-certified") **and the source ledger with it**, while the ledger row claims it "retained only scientific status and gate rule." The housekeeping half of that row is discharged; the retention half is not.

Nothing below can be repaired one row at a time until this is fixed, because a cross-reference audit of a document with no cross-references is an audit of what the author remembers rather than of what the author cited.

---

## 2. Cross-reference table — v0.2.2's canon presuppositions

Every place v0.2.2 asserts or presupposes something about AOP canon. Grade: **FAITHFUL** (canon says this) / **DRIFTED** (canon says something adjacent, and the difference does work) / **UNSUPPORTED** (cannot be located in canon) / **CONTRADICTS**.

| # | v0.2.2 claim | Canon passage (verbatim, ≤25 words) | Locator | Grade |
|---|---|---|---|---|
| X1 | Four axes Boundary/Drive/Memory/Integration, with the method "not a proof that AOP has four independent operational degrees of freedom" (§0) | "The count is held open—at least these four, not a claim that exactly four exhaust the phenomenon" | §2, line 89 | **FAITHFUL** |
| X2 | Boundary is "a panel, not one scalar": B1/B2/B4 lead, B5 descriptive (§2.1) | "Boundary panel — a family of proxies, not one scalar… a declared interior/exterior state contrast (B1), the screening residual" | Table 1, line 71 | **FAITHFUL** |
| X3 | **B5 "is not boundary strength and cannot replace B1/B2/B4"** (§2.1) | "Cross-boundary dependence I(inside;outside) (B5) is retained only as a descriptive quantity, and is explicitly the cross-cut slice of Integration" | Table 1, line 71 | **FAITHFUL** — canon says "not boundary strength" in the same sentence. Repairs prior F0b. |
| X4 | B5 is a "cross-cut stored dependence" reported descriptively (§2.1, §2.4) — but the contract never says B5 is *part of* Integration | "B5 = I(inside;outside) is an algebraic component of Integration read at the same" interface; "a per-edge weight here double-counts" | §1 line 52; Table 2, line 239 | **DRIFTED** — canon's nesting identity `TC = I(inside;outside) + TC_inside + TC_outside` (§4, line 182, "verified to machine precision") is nowhere in v0.2.2, so a seat can report B5 on the Boundary panel and TC on the Integration panel and double-count the same quantity |
| X5 | B4 = "the work, flow, control effort, or other declared burden required to hold B1 against leak" (§2.1) | "the maintenance burden (Boundary panel B4) equals the housekeeping entropy-production rate σ_hk = f·J" | §4, line 130 | **DRIFTED** — canon identifies B4 with a specific entropy-production rate and calls it "the Drive panel's housekeeping term read at the interface" (§1, line 52). v0.2.2's open-ended list admits burdens canon's identification excludes, and never records the Drive cross-loading |
| X6 | Memory reading is `E = I(X_{≤0}; X_{≥1})`, contiguous split, present on the past side (§2.2) | "the past–future split is contiguous, with the present assigned to the past: E = I(X_{≤0} ; X_{≥1})" | §4 cond. 5, line 124 | **FAITHFUL** |
| X7 | Model 4 is a "Drive control; forced Drive–Memory cross-effect" (§4 map) — the D→M theorem is **presupposed and never stated** | "Drive → Memory: dissipation forces strict memory positivity… (σ > 0 ⇒ E > 0)"; "five conditions must be stated or it is either false or vacuous" | §4, lines 122, 124 | **UNSUPPORTED as used** — v0.2.2 names no theorem, no direction, and none of the five scope conditions. Regression from v0.2.1, whose §5 stated all five |
| X8 | Off-stationarity, finite-window E "is a scoped local reading; it is not automatically an estimator of a stationary infinite-window `E`" (§2.2) | "E remains the stationary lead proxy (M1); local active information storage is the scoped proxy where stationarity fails" | §5, line 195 | **DRIFTED** — the caveat is now correctly stated (a real improvement on v0.2.1), but canon's *named, thrice-cited* off-stationarity proxy is still neither used nor declined. Charter rule 1, still inverted |
| X9 | Drive = "path asymmetry / entropy production `σ` relative to declared reversal `R`" (§0, §2.3) | "entropy production rate σ (trajectory time-asymmetry)"; "Representation-dependent (declared state variables, grain δt, and time-reversal convention R)" | Table 1, lines 76–77 | **FAITHFUL** |
| X10 | R is a mandatory declaration field (§1 field 11) | "Declaring R is therefore mandatory wherever Drive or the D→M edge is reported" | §12″, line 593 | **FAITHFUL** |
| X11 | Ring observed state is **position**, not increments; "The increment representation is outside this benchmark declaration" (§2.3) | "the increment representation of the same ring preserves σ exactly while sending E to zero" | Figure DM, line 180 | **FAITHFUL** — closes prior fatal F0a |
| X12 | Increment exclusion is justified as a *benchmark declaration choice* | "These conditions are not fully independent: the position→increment map on the driven ring is simultaneously a change of description (condition 1)" | §4, line 124 | **DRIFTED** — canon's reason is a scope condition of a theorem, not a local declaration. As written the exclusion binds model 4 only; nothing stops a seat re-declaring increments on model 7, which also has σ>0 and Memory |
| X13 | Integration reading is "Total correlation `TC` across a fixed multi-part partition" (§2.4) | "we therefore declare an operational default: total correlation, TC = Σ H(Xᵢ) − H(X) [Watanabe 1960]" | §2, line 91 | **FAITHFUL** |
| X14 | The alternative is "**minimum-cut dependence `Φ_MIP`**" (§2.4) | "written Φ_MIP where the symbol is convenient, but read throughout as a *minimum-cut irreducibility diagnostic*" | §4, line 134 | **FAITHFUL** — v1.26 renamed the quantity ("Φ_MIP is renamed minimum-cut dependence", changelog line 841) but explicitly licenses the symbol. v0.2.2 uses canon's current name *and* the licensed symbol. **This attack failed** |
| X15 | Φ_MIP is offered as an Integration reading on **model 6**, an arbitrary multipart model | "This coordinate is established here only in the static Gaussian setting and only at a fixed partition" | §4, line 134 | **DRIFTED** — v0.2.2 licenses the reading outside the only setting canon establishes it in, and carries no frontier flag |
| X16 | Φ_MIP requires "a fully declared partition search and normalization rule" (§2.4) | "The normalizer is therefore a required declaration wherever partition identity carries weight" | §4, line 134 | **FAITHFUL** |
| X17 | Each case picks TC **or** Φ_MIP freely, with no selection rule | "no exact Integration value is load-bearing"; every such claim "is stated in its directional form" | §2, line 91 | **DRIFTED** — canon's six-measure ambiguity ("no two show consistent agreement", §2 line 91) means a suite where model 6 uses Φ_MIP and model 8 uses TC cannot compare Integration across models, which §5.2 F5 requires |
| X18 | Representation is a mandatory field and "A change of representation is a change of the scientific question" (§1 field 11, §2.3) | "**All four axes are declaration-relative.** None is computable with no choices to make" | §2, line 89 | **FAITHFUL** in substance; canon's *asymmetry* (Boundary and Integration additionally require a partition) is unstated but is operationally honoured by the map's `—` cells |
| X19 | The semantic layer: 14 declaration fields, per-mechanism interventions throughout | "**Coalitions are the default object; per-edge weights are the exception**"; per-edge retained "only where additivity and identifiability tests pass" | §3, line 110 | **CONTRADICTS** — v0.2.2 is entirely a per-mechanism instrument (zero occurrences of "coalition", "mask", "additivity"), i.e. the layer v1.26 demoted, with no statement of the band canon licenses it in (changelog line 839: "κ ≲ 9, gap > 3× blur, TC up to ≈0.5") |
| X20 | Intervention declaration = §1 fields 7–9 | "Every intervention reported anywhere in this paper must declare six things, and an intervention that cannot declare them is not admissible" | §3, line 99 | **DRIFTED** — canon's protocol is mandatory and v0.2.2 never invokes it. Field 8 now covers resource flow (a real repair), but canon's #5 requires "detailed balance, conservation laws, and network topology survive the alteration, **each stated separately**" (§3, line 105); v0.2.2 lumps them into one preserved-quantities list, which matters precisely for §2.3's detailed-balance projection null |
| X21 | V: "exact `V`, its domain and type… and why larger means more viable" (§1 field 5) | "A semantic weight is a three-place quantity: an edge, a declared viable set, and a declared functional V evaluated on that set" | §7, line 245 | **FAITHFUL** on structure |
| X22 | No admissibility sense tests whether V is present-tense checkable (§1 field 9) | "A viability that requires foresight—“this will eventually reproduce”—is illegitimate" | §9, line 261 | **UNSUPPORTED** — a foresight-based V passes all 14 fields and all five admissibility judgments. Canon's present-tense principle has no hook in the contract |
| X23 | V type taxonomy: "endpoint, path, survival, or first-passage" (§1 field 5) | family members are "the survival curve S(t), the hazard function h(t), finite-horizon survival probability P(τ), and recovery probability" | §1, line 27 | **DRIFTED** — a different, unmapped taxonomy; canon's four regimes in which MFPT is inappropriate are absent, and §2.3 makes first-passage the ring's outcome |
| X24 | "AOP-domain membership" is an admissibility judgment (§1 field 9) | "AOP applies wherever the following five can be declared: a **subsystem** S; a **state representation** for it" | §10, line 382 | **DRIFTED** — the sense is named (repairing prior item 7(b)) but canon's five-declaration operational test is not reproduced, so "domain membership" has no decision procedure |
| X25 | "Any current-shortens-persistence theorem is applied only inside its complete stated envelope" (§2.3) | "For a measure-preserving current (divergence-free, at fixed stationary distribution, with ∇U·ℓ = 0) in the small-noise limit" — plus "fixed dynamical activity" | §12, lines 562, 560 | **UNSUPPORTED as usable** — the envelope has **five** conditions and v0.2.2 states **none**. §6.4 item 11 then requires reporting "known theorem envelope and whether the case is inside it," a field no seat can fill from this document. v0.2.1 stated two of five; this is a regression |
| X26 | The ownership-free refusal is honoured — no individuation anywhere | "No ownership. Which aggregate is the “true” individual… is never the question" | §1, line 33 | **FAITHFUL** — zero ownership, self-maintenance, or individuality language in v0.2.2. **Attack failed** |
| X27 | Sign convention "is the reverse of the Kolchinsky–Wolpert value convention" (§0) | canon-external; verified in the prior lane's citation report against K&W 2018 primary text | — | **FAITHFUL in substance, UNCITED** — the prior lane read the paper and confirmed actual − intervened; v0.2.2 removed the citation that made it checkable |

---

## 3. Repair-ledger discharge table (§8, 13 rows)

Each row traced to the prior finding it claims to repair, then checked against the v0.2.2 body.

| # | Ledger row | Prior finding | Body implements? | Grade |
|---|---|---|---|---|
| 1 | B5/CBSD substituted for Boundary → restored B1/B2/B4 panel; B5 descriptive only | Fidelity A17 (**fatal**), Math F0b (**fatal**) | §2.1 defines B1/B2/B4/B5, states B5 "is **not boundary strength**", adds "If no interface `F` or maintenance model exists, B2 or B4 is **NOT DEFINED**… do not silently substitute B5" | **DISCHARGED** — the strongest repair in the document, and stronger than the finding required. Residual: canon's nesting identity (X4) is still unstated |
| 2 | survival event underdeclared → added start, target, viable/failure sets, stopping rule, orientation | Math F1 (**fatal**) | §1 field 6 lists all five; §2.3 states "Two systems can have equal `σ` and opposite effects on a directional target" | **DISCHARGED** for declaration. Residual: §6.4's sensitivity list (item 10) omits target/event, so F7 has no reporting hook — see IC-4 |
| 3 | every contrast ordered on every model → applicability map with explicit undefined statuses | Math F3 (major), Fidelity item 6/P5 (**fatal**) | §4 map with per-contrast cells; "`—` means **not required and normally not defined**, not zero" | **DISCHARGED** — closes v0.2.1's "Run every contrast … on **at least the computable models 1–6** end to end" defect cleanly. Residual: the map breaks §4's own coverage guarantee for Integration — see IC-1 |
| 4 | ring representation ambiguous → fixed position-space representation and reversal | Math F0a (**fatal**), Fidelity A11 (**fatal**) | §2.3 fixes ring position as the observed state, position-space reversal, and excludes increments with the canon-correct reason; §5.1 test 4 adds "representation is held fixed" | **DISCHARGED** — the false-refutation trap is closed. Residual: X12 (scoped to model 4 only) |
| 5 | Integration had an operation but no reading → requires preselected `TC` or `Φ_MIP` | Fidelity A21 (major), Math F0b/F3 | §2.4: "an operation alone is not a measurement. Every executable Integration case must select one reading before the run" | **PARTIAL** — a reading is now required (real repair, and it makes F5 non-vacuous). But Φ_MIP is licensed outside canon's static-Gaussian scope (X15), and free per-model choice between two non-agreeing measures breaks the cross-model comparison F5 needs (X17) |
| 6 | time grain, interface, resource-flow, domain fields missing → added to complete declaration | Fidelity A20 (major), item 7(b) (major) | §1 field 2 (`δt`), field 4 (interface `F`), field 8 ("resource flow"), field 9 ("AOP-domain membership") | **PARTIAL** — all four fields exist (genuine repair of the ~70×-σ grain gap). But "domain membership" reproduces no decision procedure (X24), and the map's model-9 output `OUTSIDE DOMAIN` has no home in §3's status list — see IC-5 |
| 7 | Even Process rationale said residual "never saturates" → distinguishes finite-order non-saturation from asymptotic decay | Math F2 (**fatal**), Citation item 2 (VERIFIED corroboration) | §2.2: "expected to remain positive at every finite `k` while tending toward zero asymptotically; that behavior is not failure"; §5.1 test 3 | **DISCHARGED**, ledger row **MISSTATED** — the prior finding was that the v0.2.1 claim was **false** (ρ_k ∝ k·2^(−k/2), corroborated by Crutchfield & Feldman's γ = 0.501 ± 0.007 in the paper the contract itself cited), not that the wording was imprecise. The corrected body carries neither the decay law nor the citation, so §5.1 test 3's "compatible with asymptotic decay" has no predeclared criterion |
| 8 | no finite-sample/smoothing rule → added estimator and UNRESOLVED rules | Fidelity item 2/P2 (major) | §2.2 Finite-sample rule: predeclared record length, replicates, max `k`, context-count threshold, smoothing, interval; UNRESOLVED defined; "No extrapolation to `k → ∞`… without a declared model" | **PARTIAL** — the rule exists and is good. The specific mechanism both prior lanes identified is not carried: plug-in block-entropy bias **grows with k** and mimics model 3's own signature (the math lane computed N ≳ 1.6×10⁵ at k=16 and N ≳ 1.8×10⁷ at k=22). Nothing tells a seat where the ladder stops being estimable |
| 9 | no driven memory-bearing dissociation model → added model 7 | Math F4 (major) | Map row 7; §4.1 model 7 requires σ>0, real Memory, nontrivial viability event; §5.1 test 7; F4 | **DISCHARGED** — directly answers "Five of the six computable models have σ = 0 identically" |
| 10 | missing internal/external-cut overlap model → added nested-cut model 6 | Math F3 (major), Fidelity P4 slot 6 (**fatal**) | Map row 6 (B ✓, I ✓); §4.1 model 6 requires one external cut and ≥1 internal partition on the same system; §5.1 test 6; F5 | **DISCHARGED** — K5's successor (F5) is now firable in principle |
| 11 | no admissibility/domain challenge → added model 9 | Fidelity P4 slot 8 (**fatal**), item 7(b) | Map row 9; §4.1 model 9 "Intentionally omit or violate one named requirement"; §5.1 test 9; F3 | **DISCHARGED**. Residual: the expected output `OUTSIDE DOMAIN` is not a status §3 defines — IC-5 |
| 12 | governance mixed into science → removed session housekeeping; **retained only scientific status and gate rule** | Fidelity item 8/P8 (major) | Verified absent: "Ben", "Aster", "seat", "session record", "§11.2", "OPEN", "self-certified", "ruling". File is complete, not truncated | **MISSTATED** — the housekeeping half is fully discharged and the truncation defect is fixed. But the removal also took the **scientific source ledger** (Aster item 8 explicitly said to keep it): 56 § pointers → 1, 6 numbered references → 0, all named sources → 1 unlocated. The disposition's word "retained" is not what happened. This is finding **F-1** |
| 13 | deterministic checks could validate themselves → added independent mutation-test requirement | **none located** | §6.3 mutation test exists and is well specified ("A check that inverts the same function it validates is not independent") | **MISSTATED** — I searched all three prior break-attempt reports and the Aster gate-readiness review for `mutation`, `seeded`, `self-valid`, `validate themselves`, `inverts`, `deterministic`, `harness`: **zero occurrences in all four documents**. The §6.3 requirement is a good addition and is the only trigger F8 has. The ledger claim that it repairs a v0.2.1 defect is **NOT VERIFIED** against any source available to me — I did not have the companion status file, so I report this as unlocated, not as fabricated |

**Ledger score:** 7 DISCHARGED · 3 PARTIAL · 0 NOT DISCHARGED · 3 MISSTATED (rows 7, 12, 13).

---

## 4. Internal-consistency findings

Contradictions between §4 (map), §4.1 (minimum declarations), §5.1 (predeclared tests), §5.2 (failure conditions), §3 (statuses), and §6.4 (required output).

**IC-1 (major). §4's own coverage guarantee fails for Integration.**
§4 states the gate ensures "every contrast has at least one positive control, one failure or dissociation test, and one admissibility/definedness challenge." Integration is marked required (`✓`) on **exactly one** row: model 6, whose primary job is "Boundary–Integration operator-collapse test" — a *failure* test. Models 7 and 8 mark I `optional`, which §4 defines as "may run only after the full declaration is filled," i.e. not guaranteed. So Integration has **no required positive control**. Either the guarantee is false as written, or model 6 must serve as its own positive control and failure test, which is exactly the self-validating structure §6.3 forbids elsewhere. Maps to **F5** (whose disposition, "retire the extension," would then be reachable for the wrong reason). *Cheapest repair:* mark I `✓` on model 7 and declare it the Integration positive control, or amend §4's guarantee to exempt the unpromoted extension explicitly.

**IC-2 (major). Model 1 is required to run a contrast that is degenerate by construction — and the document gives that fact three incompatible readings.**
§2.2's full Memory null is "order 0: replace the temporal mechanism with the i.i.d. process having the same one-time marginal." On model 1, an i.i.d. finite-alphabet source, that null is the **identity map**, so θ_M ≡ 0 analytically. The map marks M `✓` (required) on row 1. Then:
- **§0** reads the zero as "no detected viability relevance under this declaration" — a result;
- **§5.1 test 1** reads it as a calibration **pass** ("returns `E=0` and `σ=0`");
- **§5.2 F2** reads it as a failure condition — "constructional degeneracy: `μ₀`, `V`, or the preserved quantities force `θ=0`. Disposition: **declaration error; repair before scientific interpretation**."
The identical analytic fact is a result, a pass, and a declaration error, with no rule assigning which. The prior math lane raised this as a minor item ("Model 1's k=0 null is the identity map"… "It should be labelled as an analytic identity check rather than a contrast"); v0.2.2 did not carry it and the new F2 turned it into a contradiction. Maps to **F2**. *Cheapest repair:* one sentence in §5.1 — "on model 1 the order-0 Memory null is the identity map; θ_M = 0 is an analytic identity check, not an F2 trigger."

**IC-3 (major). F6 cannot fire on this suite, by construction.**
F6 triggers when "no interface or maintenance quantity can be declared on **any** target class." §4.1 model 5 *requires* declaring "inside, outside, and interface `F`" and "the burden needed to maintain B1 against leak." A suite that mandates a model in which the Boundary panel is instantiable cannot produce evidence that it is never instantiable. F6 is therefore method-level rhetoric with no benchmark path. This is not fatal — F6's disposition is a claim restriction, not a run outcome — but the contract presents F1–F8 as a uniform set of testable conditions and one of them is untestable. *Cheapest repair:* relabel F6 as an out-of-suite condition assessed on target classes, not on benchmarks.

**IC-4 (major). F7's trigger is foreclosed by §4.1 and has no reporting channel in §6.4.**
F7 — "outcome-direction instability: reasonable undeclared target choices reverse the result" — is the codification of the prior lane's fatal Drive-sign finding. But §4.1 model 4 requires "an exact first-passage or survival event," which *declares away* the choice F7 needs varied; no test in §5.1 requires running two admissible targets; and **§6.4 item 10's sensitivity list is "horizon, grain, severity/rung, representation, and estimator" — target/event is absent.** So F7 can only fire by accident. Given that the prior attempt broke v0.2.1 on precisely this axis (σ is even under current reversal, ΔV is odd; sign flipped in every row of the two-target comparison), a failure condition written for it that no test exercises is a live gap. *Cheapest repair:* add "outcome event/target set" to §6.4 item 10's sensitivity sweep, and add a §5.1 test requiring model 4 to report both admissible first-passage targets.

**IC-5 (major). Three status vocabularies, one crosswalk missing, and a status with no rule.**
- §3: "Every cell receives **one** status" — ESTIMATED / ANALYTIC / NOT DEFINED / NOT EXECUTABLE / UNRESOLVED.
- §6.4 item 12: "**PASS / FAIL / UNRESOLVED / NOT EXECUTABLE**, with reason" — a second, overlapping vocabulary that adds PASS/FAIL and drops ESTIMATED/ANALYTIC/NOT DEFINED.
- §4.1 model 9 and §5.2 F3: "**OUTSIDE DOMAIN**" — a third label appearing in neither list.
No crosswalk is given, and nothing says whether a cell can be ANALYTIC *and* PASS. Separately, **ANALYTIC vs ESTIMATED has no assignment rule**: §6.1 says "Use exact calculations on models 1–4 whenever possible," which is a preference, not a criterion. And §4's `—` cells are described as "normally not defined," pre-assigning §3's NOT DEFINED status before any run. *Cheapest repair:* one status table — measurement status (§3's five) × case verdict (PASS/FAIL) — with OUTSIDE DOMAIN added to the measurement column and a rule that ANALYTIC requires a closed form deposited.

**IC-6 (minor–major). Model 5 requires a Drive-panel quantity on a row where Drive is optional.**
§4.1 model 5 requires "the burden needed to maintain B1 against leak" and a case with "no material maintenance." B4 is that burden, and canon identifies it as the housekeeping entropy production σ_hk read at the interface (§4, line 130). The map marks model 5 **D `optional`**. So a required Boundary reading is a Drive-panel quantity on a row where Drive may not be run. Maps to **F6**'s subpanel disposition. *Cheapest repair:* mark D `✓` on row 5, or state in §2.1 that B4 is measured within the Boundary contrast and is not the Drive contrast.

**IC-7 (minor). Model 7's required manipulation falls outside §1's declaration scope.**
§4.1 model 7 requires "at least one manipulation that changes a structural reading without changing `V`" — the viability-invariant control §5.1 test 7 depends on. That manipulation is neither the Memory projection nor the Drive null nor either scramble, so it is not a member of the typed family; but §1's 14 fields are specified per **"model–contrast pair"** and §1 governs only contrasts. The control has no declaration discipline. *Cheapest repair:* name it a fifth declared intervention type in §1, or specify it as a severity-0 rung of an existing contrast.

**IC-8 (minor). F8's tolerance is predeclared for one of nine tests.**
F8 triggers when defects or controls "are missed **beyond the predeclared tolerance**." Only §5.1 test 1 mentions a tolerance ("within the declared analytic or estimator tolerance"); tests 2–9 predeclare none. *Cheapest repair:* one line requiring a tolerance per test in the declaration sheet.

**IC-9 (minor). Model 1's second job has no test.**
The map assigns model 1 "all-null **and estimator-bias control**." §5.1 test 1 checks only that E=0 and σ=0. The estimator-bias job is exercised nowhere except §6.3's mutation test, which is about seeded defects, not bias. *Cheapest repair:* fold it into §5.1 test 1 as a bias-vs-record-length sweep.

**IC-10 (minor). Model 8's Boundary requirement is unsupported by its own minimum declaration.**
Map row 8 marks B `✓` on the "anti-viable information model," but §4.1 model 8's minimum declaration says only that "Information or dependence must predictably reduce viability under the declared event" — it declares no inside/outside cut and no interface `F`, both of which §1 field 4 and §2.1 require before a Boundary contrast is executable. As written, row 8 orders a contrast its own declaration cannot support. *Cheapest repair:* mark B `optional` on row 8, or add the cut and `F` to §4.1 model 8.

---

## 5. Silent drops — prior findings the ledger does not mention

Each was open at the end of the v0.2.1 attempt and appears in none of the 13 ledger rows.

| Prior finding | Severity then | Status in v0.2.2 |
|---|---|---|
| **A10** — canon's warning that the five D→M scope conditions "are not fully independent" was deleted | major | Still absent; v0.2.2 now omits the conditions entirely (X7), so the warning has nothing to attach to |
| **A12** — the D→M grade was truncated (direction forced × theorem/corollary; **reach** only conditionally-forced × constructed-counterexample) and cited to the wrong canon table | major | The grade is now stated nowhere. The defect is removed by deletion, not repaired; a seat cannot tell what warrant model 4's "forced Drive–Memory cross-effect" carries |
| **A13 / C-1** — the contract's σ_Δ is a stationary trajectory-level KL rate; the canon reference for that identity supplies a single-time phase-space relative entropy | major | §2.3 still defines `σ_Δ(t) = Δ⁻¹ D_KL(P_[t,t+Δ] ‖ R P_[t,t+Δ])` with no flag. The finding was that the flag belongs on this definition, and it is still not there |
| **A18** — canon's named off-stationarity Memory proxy (local active information storage, M1) is neither used nor declined | major | Still unmentioned (X8). The caveat improved; the omission did not |
| **A20 (part)** — canon §3's six-item internal-edge intervention protocol is never invoked; "each stated separately" for detailed balance / conservation laws / topology | major | Resource-flow was added (row 6). The protocol is still uncited and the three structural properties are still lumped (X20) |
| **A22** — the current-shortens-persistence envelope was stated with two of five conditions | major | Now stated with **zero** of five — a regression, and it makes §6.4 item 11 unfillable (X25) |
| **A3 / A4** — a mis-numbered reference and a canon-derived step relabelled as a cited fact, inside the section that existed to repair a citation error | major | Moot by deletion: all citations removed (F-1). The correct source chain was not supplied |
| **A27 / Citation 5c** — K&W equation locators marked "verified" that resolve in no retrievable version | major | The K&W appeal survives in §0 with **no** locator at all. A NOT VERIFIED item was neither repaired nor recorded |
| **Math F5** — "a two-state Markov chain satisfies detailed balance for *every* rate choice" is false as stated (multi-channel two-state chains are genuine NESS with σ > 0) | major (stated reason) | The model-4 rationale is gone entirely; the corrected statement is recorded nowhere, so the error is available to be re-made |
| **Math, model 1 k=0 null is the identity map** | minor | Not carried — and now collides with F2 (IC-2) |
| **Fidelity A25 / A26** ("Baiesi & Maes" author list; "Jupiter (Bartlett's negative control)") | minor | Moot: §10 and §7.4 were removed wholesale |

Three of these (A22, A12, A13) are cases where **v0.2.2 is weaker than v0.2.1 on the same point.** A ledger that lists thirteen repairs and no regressions is not a complete account of the revision.

---

## 6. Findings, graded

### Fatal

**F-1. The contract's entire canon and source apparatus was deleted, and the ledger row that did it claims the opposite.**
Zero section pointers, zero references, one unlocated external name. Aster item 8 said to keep the source ledger; ledger row 12 says "retained only scientific status and gate rule." Consequence: every structural claim in §§2–5 is now uncheckable by locator, and the three most substantive canon-fidelity gaps (X19 coalition default, X25 theorem envelope, X7 the unstated D→M theorem) are invisible to a reader who has only this document. Maps to **F3 (inadmissible)** at the level of the contract itself and to §7's "**gate not executable** — name every missing field or artifact."
*Cheapest repair:* a §9 source ledger — one line per canon-derived commitment, giving the canon version, section, and the exact quoted sentence. Roughly 20 rows. Nothing else in the document changes.

**F-2. Two structural commitments are made outside the scope canon establishes for them.**
(i) The whole instrument is per-mechanism, i.e. the per-edge layer v1.26 demoted: canon §3 (line 110) says "**Coalitions are the default object; per-edge weights are the exception**," retained "only where additivity and identifiability tests pass," inside a measured band. v0.2.2 has no coalition object, no additivity test, and no band. (ii) Φ_MIP is offered as an Integration reading on an arbitrary multipart model, where canon §4 (line 134) establishes the coordinate "only in the static Gaussian setting and only at a fixed partition."
Maps to **F3** (a null "fails a named admissibility or domain test" — here, canon's own scope). *Cheapest repair:* two sentences in §2.4 and §3 — Integration readings other than TC on non-Gaussian models are reported as frontier; per-mechanism attribution is reported alongside the minimal failure cut set, or the contract states plainly that it is instrumenting the per-edge layer and inherits its band.

**F-3. The D→M theorem is presupposed by the benchmark map and stated nowhere, so §6.4's envelope field cannot be filled.**
The map assigns model 4 the "forced Drive–Memory cross-effect" and §5.1 tests 1–4 are calibration against it, but v0.2.2 names no theorem, no direction σ>0 ⇒ E>0, and none of canon's five scope conditions — of which the time-reversal parity condition is the one that makes §1 field 11's R load-bearing. Simultaneously §2.3 invokes an unnamed "current-shortens-persistence theorem" whose envelope (five conditions in canon §12) is not stated, while §6.4 item 11 requires every report to record "known theorem envelope and whether the case is inside it." Two mandatory reporting fields have no source in the document.
*Cheapest repair:* one boxed subsection reproducing both envelopes verbatim from canon with locators. This is the item v0.2.1 got closest to and v0.2.2 removed.

### Major

**M-1. §4's coverage guarantee is false for Integration** — no required positive control (IC-1). Maps to F5.
**M-2. Model 1's degenerate Memory contrast has three incompatible readings** across §0, §5.1 and F2 (IC-2). Maps to F2.
**M-3. F7 has no test and no reporting channel** (IC-4) — on the exact axis the prior attempt broke v0.2.1. Maps to F7.
**M-4. Three status vocabularies with no crosswalk, and OUTSIDE DOMAIN has no rule for assignment** (IC-5). Maps to §7's "gate not executable."
**M-5. The nesting identity is unstated, so B5 and TC can be double-counted** (X4). Canon calls this out directly (Table 2, line 239: a per-edge weight there "double-counts"). Maps to F5 — an Integration reading that silently contains the Boundary reading will look determined by it.
**M-6. B4 is decoupled from its canon definition** (X5, IC-6): canon fixes B4 = σ_hk and calls it a Drive cross-loading; v0.2.2 leaves the burden open-ended and marks Drive optional where B4 is required.
**M-7. No admissibility sense tests present-tense checkability of V** (X22). A foresight-based V passes all 14 fields. Maps to F3.
**M-8. F6 is untriggerable by the suite** (IC-3).
**M-9. Free per-model choice between TC and Φ_MIP breaks the cross-model comparison F5 requires** (X17), given canon's finding that Integration measures agree in rank and not in value.
**M-10. Two ledger rows misstate their own provenance:** row 13 cites a v0.2.1 defect I could not locate in any prior report or the Aster review (NOT VERIFIED, not fabricated — I did not have the companion status file); row 7 recasts a demonstrated falsehood as imprecise wording and drops both the analytic decay law and the primary-source corroboration.
**M-11. Three silent regressions** (A22 envelope five conditions → zero; A12 grade → absent; A13/C-1 flag still off the σ_Δ definition), none acknowledged in a ledger that reports only improvements.

### Minor

- IC-6 through IC-10 as itemized above (model 5 D-optional; model 7's undeclared manipulation; F8's single tolerance; model 1's untested second job; model 8's unsupported B ✓).
- X12: the increment exclusion is scoped to model 4 by declaration rather than by canon's scope condition, leaving model 7 exposed to the same trap.
- X23: the V-type taxonomy ("endpoint, path, survival, or first-passage") does not map onto canon's persistence-functional family, and canon's four regimes where MFPT is inappropriate are unstated.
- X8: the off-stationarity caveat is now correct but still neither uses nor declines canon's named M1 proxy.
- X18: canon's representation-vs-partition asymmetry is honoured operationally by the map but never stated, so the `—` cells look like a suite choice rather than a canon consequence.
- §2.2's finite-sample rule does not bound where the ladder stops being estimable (ledger row 8 residual).
- §8's ledger has no row for anything the revision made *worse*; a "known regressions" column would cost one line each.

---

## 7. FAILED-ATTACKS LEDGER — what I tried to break and could not

This is the mandatory half of the report. Every item below is an attack I set up expecting a finding and abandoned on the evidence, or a place where v0.2.2 is genuinely better than v0.2.1.

1. *Attack: Canon renamed Φ_MIP, so v0.2.2 contradicts canon.* I expected CONTRADICTS: the v1.26 changelog says "**Φ_MIP is renamed minimum-cut dependence**… throughout the live body" (line 841). But §4 (line 134) explicitly licenses the symbol — "written Φ_MIP where the symbol is convenient" — and v0.2.2 writes "**minimum-cut dependence `Φ_MIP`**," using canon's current name *and* the licensed symbol. **FAITHFUL.** The attack failed on the canon's own text. (The live finding about Φ_MIP is scope, X15 — a different attack that succeeded.)

2. *Attack: Canon does not actually say B5 is 'not boundary strength'.* It does, verbatim, in Table 1 (line 71), in the same sentence that demotes it to descriptive. v0.2.2's §2.1 is faithful and goes *further* than canon requires by adding an explicit anti-substitution rule ("If no interface `F` or maintenance model exists, B2 or B4 is **NOT DEFINED**… do not silently substitute B5"). **This closes prior fatal F0b/A17 completely.** The single best repair in the document.

3. *Attack: The increment-representation trap is still live.* It is not. §2.3 fixes the ring's observed state as position, uses position-space reversal, and excludes increments with the canon-correct reason ("it preserves the current reading while erasing the declared Memory reading"), and §5.1 test 4 adds "representation is held fixed." I could not construct a reading of §2.3 under which a compliant seat measures σ>0 with E=0 on model 4. **Prior fatal F0a is closed.**

4. *Attack: The Even Process rationale is still false.* It is not. "expected to remain positive at every finite `k` while tending toward zero asymptotically; that behavior is not failure" is exactly the distinction the prior lanes established analytically (ρ_k ∝ k·2^(−k/2)) and confirmed against Crutchfield & Feldman's γ = 0.501 ± 0.007. **Prior fatal F2 is closed on substance.** My surviving finding is about the ledger's framing and the missing tolerance, not the claim.

5. *Attack: Boundary and Integration are still ordered on models with no factorizable state space.* They are not. The §4 applicability map marks B and I as `—` on models 1–4 and states "`—` means **not required and normally not defined**, not zero." This is a clean, complete repair of prior major F3 and prior fatal item 6/P5's all-contrasts-on-all-models instruction. Two new models (6, 7) and a domain challenge (9) were added rather than reassigning existing slots — the specific defect that made prior P4 fatal.

6. *Attack: K5's successor is still true by definition.* It is not. §2.4's "an operation alone is not a measurement. Every executable Integration case must select one reading before the run" separates the operator from the reading, and §4.1 model 6 makes the point explicitly: "This makes operator overlap testable without assuming measurement identity." F5 is now a substantive test where K5 was vacuous. **Prior fatal A21/F0b(3) is closed.**

7. *Attack: The ownership-free refusal has leaked back in.* It has not. Zero occurrences of ownership, self-maintenance, individuality, or any equivalent in v0.2.2, and no inference from Φ_MIP positivity to individuality — the inference v1.26 deleted (§4, line 134: "It does **not** establish that the system is *one individual*"). The refusal is honoured throughout.

8. *Attack: Governance material survives, as in v0.2.1.* It does not. I searched for every string the prior audit listed: `Ben`, `Aster`, `seat`, `session record`, `ruling`, `self-certified`, `§11.2`, `OPEN`, `Drive connector` — **zero occurrences**. The one governance-adjacent sentence, "Its builder cannot certify it," is a scope statement about the gate, not housekeeping. And the file is **not truncated** — v0.2.1 ended mid-sentence at "`§11.2 remains `"; v0.2.2 closes with a complete paragraph. Prior major item 8/P8's shipping defect is fixed.

9. *Attack: The four-axis title drift survives.* It does not. The title is "three core contrasts plus one internal-cut extension," §0's opening sentence says "**not** a proof that AOP has four independent operational degrees of freedom," and §3 adds "Do not infer how many real axes exist from matrix rank, diagonal appearance, or one model's response pattern." Prior item 7(a)/P7 is discharged — and it is **not claimed** in the ledger, so the revision is quieter about this than it is entitled to be. Same for the units field (§1 field 13, "bits or nats"), which closes prior minor item 23 without taking credit.

10. *Attack: The map's `—` cells smuggle in a zero.* They do not: "`—` means **not required and normally not defined**, not zero" is stated at the map, and §0 independently says "Zero `θ_A` means only: **no detected viability relevance under this declaration, horizon, estimator, and intervention.** It never means the feature is absent." I tried to construct a reading in which a `—` cell is later summarized as a null result and could not.

11. *Attack: Canon changed between the two attempts, so some v0.2.1 findings are stale.* It did not. The canon file supplied to this lane is byte-identical (whitespace-normalized) to the one the v0.2.1 lane used: **zero substantive diff lines** over 850 lines. Every prior finding stands or falls on its own merits.

12. *Attack: The K&W sign-convention statement is wrong.* It is not. §0's "This is the reverse of the Kolchinsky–Wolpert value convention" matches the prior citation lane's primary-source read (K&W define value as actual − intervened). The claim is correct; my finding (X27) is that the citation which made it checkable was deleted.

13. *Attack: The mutation test is decorative.* It is not. §6.3 names the defect classes to seed (wrong lag, wrong reversal, wrong target, ignored horizon, changed entropy-production factor, transposed generator, changed state representation) and states the independence principle: "A check that inverts the same function it validates is not independent." It is the only trigger F8 has and it is well specified. My finding is that its *provenance claim* in ledger row 13 is unlocated — not that the requirement is bad.

14. *Attack: The declaration block still drops the time grain.* It does not. §1 field 2 carries `δt` — the slot canon's Figure 1 shows is worth roughly seventy-fold on σ — and field 4 carries the interface `F` that B2 conditions on. Prior major A20's two headline omissions are repaired.

---

## 8. Verification statement

**Read in full:** the target (288 lines); the supplied canon (851 lines) with §§1, 2, 3, 4, 5, 6, 7, 8, 9, 9a, 10, 11, 12, 12′, 12″, 13, 13a and the complete v1.26 changelog read directly; all three v0.2.1 break-attempt reports; the Aster gate-readiness review; the v0.2.1 contract.

**Method.** Every canon quotation above was located by line number in the supplied file and re-matched verbatim by exact regex before being written into a finding; all 39 quotation checks matched. String-absence findings (no coalition object, no citations, no governance material, no mutation-test antecedent) are exhaustive searches over the full texts, not impressions. The canon-identity check is a normalized unified diff against the v0.2.1 lane's canon copy.

**NOT VERIFIED — stated plainly, never as passes.**
- **Canon ratification status.** The supplied body self-describes v1.26 as "a **proposal**, not canon" pending line-check and Ben's decision. I could not retrieve any adoption record, and no v1.27 changelog exists in the file. Whether a ratified v1.27 exists elsewhere is open; if it does, every FAITHFUL grade above needs re-running against it.
- **Ledger row 13's antecedent.** No prior report or review available to me contains any mutation-test, self-validation, or harness finding. The companion status file the v0.2.1 contract referenced (`AOP_Status_ContractV021_SessionAndCanon_20260807`) was **not supplied and not read**; if the finding lives there, row 13 is discharged and my grade should be withdrawn. I did not assume either way.
- **External literature.** No primary source was retrieved by this lane. Where I rely on a source-level fact (the Even Process convergence exponent, the K&W sign convention), I am relying on the prior citation lane's recorded reads and say so; those are not independent verifications by me.
- **Executable artifacts.** The §7 "benchmark declaration sheets and executable harness" do not exist yet by the contract's own statement, so no finding here tests a running gate.

*Fidelity lane, 2026-08-08. Non-canon. Authorizes no canon edits. Report of defects and of failed attacks; repairs are named only where the canon or the prior attempt already supplies the fix.*
