# Change set — AOP Canon v1.26 → v1.27

**Order implemented:** `TASK_CW_AOP_v127_ChangeSet_20260726`
**From:** Claude Cowork (execution seat / builder)
**To:** prime (chat seat) for verification; **Ben** places and stamps
**Date:** 27 July 2026
**Status:** **PROPOSAL. Not self-certified. Not canon.** A different seat verifies this fold (I built it; I did not verify it). Ben places the candidate manually and stamps the master.

---

## 0. Provenance and integrity

| Item | Value |
|---|---|
| Base master | `AOP_CANON_MASTER_v1.26.md`, Drive `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn` |
| Base size | **254,046 bytes** — verified before any edit |
| Base md5 | `54ceb3772e29f25c6e139b703d550d59` — **verified, matches order** |
| Base sha256 | `2c298d47d170fd1c87a261ca988f1b831d9b02c7acb46fecfbcf955ebcf22271` — **verified, matches order** |
| Base lines (`str.split("\n")`) | **851** |
| Output candidate | `AOP_CANON_MASTER_v1.27_candidate.md` |
| Output size | **255,684 bytes** (Δ +1,638) |
| Output md5 | `998aa87e0927f84ae6ea1676ebe8ca93` |
| Output sha256 | `99f64eccb5d28b3ce8dcaa4ccf79c3a9fb6c3dc4563747b799cc5c9903800aff` |
| Output lines (`str.split("\n")`) | **851** (unchanged — every edit is within-line; no line inserted or deleted) |

**Method.** The verified v1.26 master was edited by exact-string, count-asserted operations (each replacement verified to hit exactly its intended target — 29 operations, all count-1 except where noted). Because no edit adds or removes a newline, v1.26 line numbers locate every edit in the candidate as well. Line-numbering convention is `str.split("\n")` (851 for v1.26 / 997 for v1.25), per the order.

**Invariants against v1.26** (full table in §6): **References section byte-identical**; inline numeric-citation multiset **identical**; bracketed named-author citation multiset **identical**; all grade-tag counts **unchanged** except the raw substring `forced` (+1), which is the ordinary word inside the authorized ledger-honesty phrase "true, forced, and thin," **not** a grade change (the `forced × theorem/corollary` tags are byte-preserved). **Citation count unchanged, as §3 of the order requires.**

---

## 1. The edits

Each edit gives the authorizing order item, the v1.26 line, and before → after. Unicode (σ, E, ⇒, ≤, −, φ, —, →) is reproduced as in the master.

### Edit 1 — flame contradiction D-2 (order §1). §1, L40.

Live canon defect: §1 asserted the flame carries "essentially no memory," which §11 (L395) explicitly retracts. Brought L40 into line with the §11 correction with a minimal edit (no restatement of §11's reasoning), using the phrasing §11/§13/§11-L405 already carry ("shallow, short-lived memory").

- **Before:** `A flame is a real persister — a sharp, actively maintained boundary — carrying essentially no memory;`
- **After:** `A flame is a real persister — a sharp, actively maintained boundary — carrying only shallow, short-lived memory;`

The downstream clause "…importing a memory it does not have (Section 11)" is left unchanged: it is now exactly parallel to the corrected construction already at L405 ("shallow, short-lived memory that a memory-maximizing individuality axis … cannot represent without either importing memory it does not have or denying it a boundary").

**Sweep for surviving instances of the retracted phrasing (order §1, "outside §11"):** the only other occurrence of "essentially no memory" outside §11 is in the **changelog (L842)** — `the flame's "essentially no memory" becomes shallow or short-lived memory` — which *documents* the v1.26 correction and is left byte-identical (it is history, not an assertion). See §5 for one in-§11 residual ("negligible memory," L393) surfaced but left, per the order's scoping.

### Edit 2 — scope condition 5, split convention (order §2, Edit 2). §4, L125.

Closes a live falsity: the canon nowhere stated whether the past includes the present, and under the excluded-present split the theorem is false. Verbatim text folded, inserted as the fifth enumerated condition (after the Fourth condition and its thermodynamics-of-prediction elaboration, before "Three notions must be kept apart"):

> *Fifth, the past–future split is contiguous, with the present assigned to the past: E = I(X_{≤0} ; X_{≥1}), following Crutchfield & Feldman (2003), Prop. 8. Under the excluded-present variant E_gap = I(X_{≤−1} ; X_{≥1}) the implication is false: any 1-dependent process X_t = φ(U_t, U_{t+1}) with U i.i.d. has E_gap = 0 identically, and such processes can carry strictly positive — indeed infinite — entropy production [deposited].*

**Consequential count updates** (a fifth condition makes every "four conditions" statement internally false — the same defect class as Edit 1; updated for consistency and reported here):

| v1.26 line | Before | After |
|---|---|---|
| L125 | `four conditions must be stated` | `five conditions must be stated` |
| L125 | `a box with four scope conditions and one conclusion` | `a box with five scope conditions and one conclusion` |
| L236 | `four scope conditions, §4` | `five scope conditions, §4` |
| L444 (Table 3) | `four of them as of v1.26, the new one being a **time-reversal parity condition**` | `five of them as of v1.27, the v1.26 addition being a **time-reversal parity condition**` |
| L573 (§12′) | `four scope conditions, incl. time-reversal parity` | `five scope conditions, incl. time-reversal parity` |
| L588 (§12′) | `within its four stated scope conditions` | `within its five stated scope conditions` |

(The masthead L13 and the cross-references at L90/L594/L672 that call the *parity* condition "the fourth scope condition" are **not** touched — they name parity as the fourth-*added* condition, which adding a fifth does not change. See §5 for the pre-existing ordinal looseness.)

### Edit 3 — repair the §4 proof (order §2, Edit 3). §4, L123.

The canon's "i.e." elided the only non-trivial step (propagating single-split independence to i.i.d. via stationarity). Repair, not retraction — the theorem is true; its proof was incomplete.

- **Before:** `E = 0 holds if and only if past and future are independent, i.e. the process is i.i.d.`
- **After:** `E = 0 makes the past and future independent at one split; because E is shift-invariant and the process is stationary, independence holds at every split, and induction on the split point gives that the finite-dimensional laws factorize — the process is i.i.d.`

### Edit 4 — strike the "floor" language (order §2, Edit 4). Highest-consequence edit.

**4a — scope-condition-4 sentence replacement.** §4, L125. Verbatim:

- **Before:** `Fourth, and as before, what Drive forces is a memory floor (E > 0), not memory depth: it guarantees that some past–future correlation exists, not that the load-bearing memory is large.`
- **After:** `Fourth, what Drive forces is a strict positivity, not a magnitude and not a bound. There is no inequality of the form E ≥ f(σ) with f > 0: for every s > 0 there are stationary, even-variable, single-description Markov chains with σ = s and E arbitrarily close to zero [deposited]. Since E > 0 is equivalent to non-i.i.d.-ness for a stationary process, the theorem's content is exactly "sustained dissipation implies the process is not i.i.d."`

**4b — floor sweep** (order: "Sweep every occurrence of 'floor' attached to this row, in §4, Table 3, and the §12′ ledger. Report each one you change and each one you judge unrelated."). Full report in **§2 below.**

**4c — ledger honesty requirement.** §4/Table 3, L444. Appended to the D→M basis cell so the row does not read as though a substantive result survived:

- **Appended after** `…does not reach the stored-structure quantities (gate ledger below)`:
  `; since E > 0 is equivalent to non-i.i.d.-ness for a stationary process, the row's content is exactly "sustained dissipation implies the process is not i.i.d." — true, forced, and thin`

**Grade unchanged** (`forced × theorem/corollary`), per the adjudication: 3(b) is necessary *and* sufficient, so "not compelled" would be the wrong characterization. What changed is scope, proof, and framing — not the grade.

### Edit 5 — correct Figure DM(b) (order §2, Edit 5). §4, L181.

Figure DM(b) asserted that under coarse-graining "σ and E collapse to zero together" — false in general (the increment representation of the same ring preserves σ exactly while sending E to zero). Caption **narrowed to the specific coarse-graining computed**, with the counterexample named:

- **Before:** `(b) The scope condition: read on the full driven state, σ and E are both positive; coarse-grained to a reduced observable, both collapse to zero together — the implication binds only when σ and E are read on one complete description.`
- **After:** `(b) The scope condition: read on the full driven state, σ and E are both positive; under the particular coarse-graining computed here, both collapse to zero together. (This joint collapse is not general: the increment representation of the same ring preserves σ exactly while sending E to zero — see §4, scope condition 1.) The implication binds only when σ and E are read on one complete description.`

**Related observation folded** (order §2, Edit 5): that scope conditions 1 and 3 are not independent. Added in §4 (L125), immediately after the Fifth condition:

> *These conditions are not fully independent: the position→increment map on the driven ring is simultaneously a change of description (condition 1) and a change to odd variables (condition 3), so an auditor can pass each condition separately and still be looking at the same reducible case.*

---

## 2. Floor sweep report (Edit 4b)

Scope, per the order: §4, Table 3, and the §12′ ledger. Policy applied: change instances that **name the E > 0 result a "floor"** (which invites the false magnitude/lower-bound reading Edit 4a corrects) to positivity language; **leave** instances that are (a) *negative* ("there is **no** floor on X" — true and the whole point), or (b) architectural descriptors that also cover the TUR bound, which is a genuine floor.

### Changed (17)

| v1.26 line | Location | Before → After |
|---|---|---|
| L123 | §4 headline | `dissipation forces a memory floor.` → `dissipation forces strict memory positivity.` |
| L125 | §4 (cond. 3 tail) | `a memory floor derived from it inherits that gap` → `a memory-positivity result derived from it inherits that gap` |
| L125 | §4 (cond. 4) | *(handled by Edit 4a — "memory floor (E > 0)" → "strict positivity")* |
| L125 | §4 | `the D→M floor. Cμ is the` → `the D→M positivity. Cμ is the` |
| L125 | §4 | `So the floor Drive forces reaches predictive memory` → `So the positivity Drive forces reaches predictive memory` |
| L125 | §4 | `the predictive-memory floor (E > 0)` → `the predictive-memory positivity (E > 0)` |
| L125 | §4 | `It forces a floor on predictive memory` → `It forces strict positivity of predictive memory` |
| L147 | §4 / Table 2 cell | `forced floor, directional` → `forced positivity, directional` |
| L148 | §4 / Table 2 cell | `dissipation forces a memory floor (E > 0), not depth` → `dissipation forces strict positivity (E > 0), not depth` |
| L181 | §4 / Figure DM title | `The memory floor, computed.` → `Strict memory positivity, computed.` |
| L442 | Table 3 row label | `D→M memory floor (directional)` → `D→M memory positivity (directional)` |
| L443 | Table 3 status | `the floor's reach is conditionally-forced` → `the result's reach is conditionally-forced` |
| L444 | Table 3 basis | `so this forces a floor (E>0), not depth` → `so this forces strict positivity (E>0), not depth` |
| L444 | Table 3 basis | `The floor reaches predictive memory (E) and no further` → `The result reaches predictive memory (E) and no further` |
| L444 | Table 3 basis | `the D→M floor does not reach the stored-structure quantities` → `the D→M result does not reach the stored-structure quantities` |
| L573 | §12′ ledger | `D→M memory floor, direction σ>0 ⇒ E>0` → `D→M memory positivity, direction σ>0 ⇒ E>0` |
| L574 | §12′ ledger | `D→M floor reaches E only` → `D→M positivity reaches E only` |

### Judged unrelated / left inside the three sweep locations (with reason)

- **L121 (§4)** — "two forced **floor-type** spokes." Architectural descriptor covering *both* the D→M edge and the TUR reliability bound; the TUR bound is a genuine lower bound, so "floor-type" is accurate for it. Left.
- **L127 (§4)** — "escape the Drive floor," "it carries **no** floor," "the two **floor-type** edges (E > 0 and the TUR reliability bound)" (×2). Negative statements and TUR-inclusive descriptors. Left.
- **L125 (§4)** — "carries **no** floor," "with **no** forced floor (Cμ magnitude)," "forcing neither a floor on stored complexity," "**no** floor on stored complexity." All *negative* — asserting the absence of a floor is true and is exactly what Edit 4 wants said. Left.
- **L444 (Table 3)** — "**no** floor on stored complexity Cμ." Negative, correct. Left.
- **L588 (§12′)** — "the hard **floor** is one row." Foundation/bedrock sense (the settled core), not the E-magnitude sense; consistent with L588's own "the settled core is small and named" and with L600/L844. Left (count updated to five).

### Floor namings OUTSIDE the three sweep locations — flagged for Ben, not changed

The order bounded the sweep to §4 / Table 3 / §12′. These name the row a "floor" elsewhere; leaving them produces mild cross-section terminology drift. Surfaced for a ruling (see §5, flag C-1):

- **L236** (two-axis / domain-map area): "D → M (predictive-memory **floor**, five scope conditions, §4)" — count updated to five; "floor" left.
- **L594** (§12″): "any memory **floor** derived from it inherits that gap."
- **L17, L13** (masthead / abstract / changelog): "dissipation forces a **floor** on predictive memory"; "the D→M **floor** is bounded to…" — masthead/history; also stamping territory (Ben's).

---

## 3. Prepared but NOT applied — 3(a)/3(b) demotion (order §2, "Optional; flag for Ben")

The re-proof recommends keeping 3(b) (stationary one-point law invariant under the reversal involution) as primary and demoting 3(a) (all variables even) to an illustration of it, since 3(b) strictly subsumes 3(a). Prime concurs but has not ruled. **Not applied.** Prepared edit, for Ben's word:

- **Target:** §4, L125, within the Third condition.
- **Before:** `it holds when **all state variables are even under the declared time-reversal**, or, more generally, **when the stationary one-point distribution is invariant under the reversal involution**.`
- **Proposed after:** `it holds when **the stationary one-point distribution is invariant under the reversal involution** — of which the case that **all state variables are even under the declared time-reversal** is the strictly stronger, more easily checked special case.`

If Ben rules yes, this is a one-line swap; the count and grade are unaffected.

---

## 4. Not touched

- **References (order §3).** No reference altered, added, or removed. The re-proof's MISSTATED-citation flags (Kawai/Parrondo/Van den Broeck 2007, Spinney & Ford convention framing, Crutchfield & Feldman for "E = 0 iff i.i.d.", Schnakenberg, and others) are **under separate verification and were not folded.** References section is byte-identical.
- **The benchmark line.** Untouched.
- **The master stamp.** No version bump, no compile-date change, no v1.27 changelog entry — that is Ben's when he places (masthead still reads "version 1.26"). The candidate carries the *content* of the fold only.

---

## 5. Flags and observations for Ben

- **C-1 — out-of-sweep-location floor namings.** L236, L594, and the masthead (L13/L17) still call the row a "floor." The order scoped the sweep to §4/Table 3/§12′; these were left. Ben may want them swept for consistency (they would otherwise read "floor" against §4's new "positivity").
- **C-2 — parity ordinal looseness (pre-existing, not from this fold).** §4 (L125) enumerates the parity condition positionally as **Third**, while the masthead (L13) and L90/L594/L672 call it "the **fourth** scope condition" (i.e., fourth-*added*). Adding the Fifth (split) condition does not touch parity's label, so the fold does not worsen this — but with a fifth condition now present the "third vs fourth" mismatch is more visible. Left as pre-existing; flag if you want it reconciled.
- **C-3 — in-§11 residual (Edit 1).** L393 (§11) reads "the flame's are all in drive (sharp boundary, **negligible memory**)," which is in mild tension with the L395 correction ("its memory is … not zero … shallow and short-lived"). The order scoped Edit 1's sweep to *outside* §11 (Task 21 handled §11), so this was left. Surfaced for a ruling.
- **Placement note (Edit 2 / Edit 5).** The Fifth condition and the "conditions 1 & 3 not independent" note were placed at the end of the enumerated-conditions block in L125, before "Three notions must be kept apart," so First→Fifth read consecutively and the Fourth condition keeps its own thermodynamics-of-prediction elaboration adjacent to it.

---

## 6. Invariant report (candidate vs v1.26)

| Invariant | v1.26 | v1.27 candidate | Status |
|---|---|---|---|
| References section (bytes) | 60,982 | 60,982 | **byte-identical** |
| Inline numeric cites `[n]` (total) | 48 | 48 | **multiset identical** |
| Bracketed named-author cites `[Author YEAR]` | 72 | 72 | **multiset identical** |
| `[deposited]` markers | 3 | 5 | +2 (Edits 2 & 4; deposit markers, not citations) |
| grade tag `theorem/corollary` | 11 | 11 | unchanged |
| grade tag `conditionally-forced` | 10 | 10 | unchanged |
| grade tag `constructed-counterexample` | 3 | 3 | unchanged |
| tags settled / synthesis / frontier | 39 / 52 / 29 | 39 / 52 / 29 | unchanged |
| raw word `forced` (substring) | 76 | 77 | +1 = "true, **forced**, and thin" (prose, not a grade tag) |

**Citation count unchanged**, as the order requires.

---

## 7. Deliverables

1. `AOP_Canon_ChangeSet_v1_26_to_v1_27.md` — this document.
2. `AOP_ChangeSet_v1_25_to_v1_26_CORRIGENDUM.md` — corrigendum to the prior change set (three document-level defects; no canon defect). Separate file.
3. `AOP_CANON_MASTER_v1.27_candidate.md` — the built candidate, for Ben to place manually. **Not stamped. Not verified by the builder.**

— End of change set v1.26 → v1.27 (proposal). —
