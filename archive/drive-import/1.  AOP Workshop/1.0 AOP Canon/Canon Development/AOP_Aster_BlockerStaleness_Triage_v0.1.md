# AOP — Aster blocker staleness triage (v1.25 → v1.26)

**File:** `AOP_Aster_BlockerStaleness_Triage_v0.1.md` · **Version:** v0.1
**Date:** 25 July 2026 · **Seat:** Claude Cowork (execution)
**Order:** `TASK_CW_AOP_Aster_Triage_20260725` §2
**Status:** Mechanical text-matching. **No recommendations. No adjudication.** Whether any Aster criticism is *correct* is prime's and Ben's; nothing below takes a position on that.

**Inputs, all retrieved and hash-checked:**

| Input | Drive ID | Bytes | md5 | Lines |
|---|---|---|---|---|
| Aster deposit (canonical `.md`) | `1hAa3KntWsdYwpJc8Cu96AKEGMhXJrYbW` | 72,519 | `ce85d732082186c326b46459770ec9b5` | 1,263 |
| `AOP_CANON_MASTER_v1.26.md` | `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn` | 254,046 | `54ceb3772e29f25c6e139b703d550d59` ✓ matches order | 851 |
| `AOP_CANON_MASTER_v1.25.md` | `13tI48fz-l5DundXuyQysPJf7JrSS9xck` | 224,340 | `9c172e015f4adfc9fe827a42687ca2e7` ✓ matches order | 996 |
| `AOP_ChangeSet_v1.25_to_v1.26_RedTeamRemediation.md` | `1mI3DkOKD_GOJzf-ImDThA1oSsRo4iEMd` | — | — | — |

All line numbers below are 1-indexed on those exact files.

---

## 0. Two things to read before the table

### 0.1 Which "seven blockers"

The deposit carries **two independent numbering schemes** and they do not correspond:

- §1 "The seven submission-blocking findings" (deposit lines 52–80) → **RED 1 … RED 7**. These are the seven blockers.
- §3 "Detailed Risk Register" (deposit lines 169–697) → **RED-1 … RED-27 / ORANGE-n**, a different sequence.

Mapping used throughout:

| Blocker (deposit §1) | Deposit lines | Detailed register entries supplying the targets |
|---|---|---|
| **RED 1** — physics / light cone / gravity boundary | 54–56 | RED-12 (434), RED-13 (461), RED-14 (479) |
| **RED 2** — Drive→Memory theorem | 58–60 | RED-4 (250), ORANGE-5 (292) |
| **RED 3** — life criterion | 62–64 | RED-17 (535), RED-18 (556), RED-19 (572) |
| **RED 4** — `Φ_MIP > 0` ≠ individual | 66–68 | RED-15 (495) |
| **RED 5** — archetypes as primary evidence | 70–72 | RED-22 (612), ORANGE-24 (646) |
| **RED 6** — observer/viability circularity | 74–76 | RED-11 (412) |
| **RED 7** — living master ≠ manuscript | 78–80 | RED-27 (684), RED-26 (667) |

### 0.2 Zones inside v1.26 — this distinction carries the whole triage

A target can "still exist" in three structurally different places, and lumping them would produce a false LIVE:

| Zone | v1.25 lines | v1.26 lines |
|---|---|---|
| **Masthead** (the version paragraph) | 13 | 13 |
| **Live body** (§1 … Data Accessibility) | 22–786 | 24–626 |
| **Back matter** (references, reference-audit paragraph, full version history) | 793–997 | 628–851 |

**Verdicts below are assigned on the live body.** Occurrences that survive only in the masthead or back matter are recorded separately — and they are precisely the material blocker RED 7 is about, so they matter to that blocker and to no other.

### 0.3 NOT-FOUND check — result: none

Every quoted phrase, section number, and numeric figure Aster names was located in v1.25 before v1.26 was consulted. **There is no NOT-FOUND. No red-team accuracy problem was detected.** Two numbers were independently recomputed and both check out:

- v1.25 masthead paragraph (line 13) = **1,443 words exactly**. Aster said "roughly 1,443."
- v1.25 = 996 lines, **32,515 words**. Aster said "996 lines; 32,518 words."

Aster's four claimed placements of the "new definition" wording were each verified in v1.25: head-of-paper (line 33), §11a (480–481), claim ledger §12 (653–654), version history (890, 909). All four present.

---

## 1. The triage table

| Blocker | Verdict | Surviving targets (v1.26 live body) | Change-set edit where stale |
|---|---|---|---|
| **RED 1** — physics block | **STALE** | none | Task 18 (18a/18b/18c) |
| **RED 2** — D→M theorem | **LIVE** | the theorem, its proof route, and its `forced × theorem/corollary` status — all present; a fourth scope condition added, status not downgraded | — (Task 11 added scope; deliberately not a downgrade) |
| **RED 3** — life criterion | **STALE in canon; RELOCATED** | one invariant sentence at §12 (line 492) | Task 19a/19b/19c + Task 15 → `AOP_LifeArchitecture_Followon_v0.1.md` |
| **RED 4** — `Φ_MIP > 0` ≠ individual | **STALE** | the word "pile" as a property of the measure (line 340); the symbol `Φ_MIP` retained where labelled as a symbol | Task 14 (parts 1–3) |
| **RED 5** — archetypes | **PARTIAL** | **flame "essentially no memory" at §1 line 40**; the `n=3` polytrope model-specificity at line 403 | Task 21, Task 9 (for the stale ones) |
| **RED 6** — observer | **PARTIAL** | the observer-independent *membership* fact (line 248, declaration-relativized); selection as agentless **selector** (line 248, role narrowed from "evaluator") | Task 13 |
| **RED 7** — living master | **LIVE, and larger** | masthead 1,443 → **1,600 words**; ⚠ 15 → 18 lines; retraction language 22 → 26 lines; `[✓ …]` 15; `[P0-n]` 4; DOI placeholder; Table 4 gate ledger; full changelog, extended | — (Task 4 fixed this in the **derivative only**, by design) |

---

## 2. Target-by-target detail

### RED 1 — relativity / light cone / gravity boundary → **STALE**

| # | Aster's textual target | v1.25 | v1.26 | Verdict |
|---|---|---|---|---|
| 1.1 | "a local light cone as an object-specific causal membrane"; "the light cone of a system's own worldline, a one-way membrane" | **294** (verbatim: "the only boundary it makes is causal — the light cone of a system's own worldline, a one-way membrane fixed by global structure") | body: absent as a claim. "light cone" survives at **254** and **397** *only inside explicit deletion notices*, plus masthead 13 and changelog 844 | STALE |
| 1.2 | Figures 3 and 4, "Delete Figures 3 and 4" | captions at **292**, **298**; referenced 290, 294, 296, 432 | **zero occurrences of "Figure 3" or "Figure 4" anywhere in the file** | STALE |
| 1.3 | "a galaxy or atom carries a causal boundary because it is … bound"; Figure 4 caption "One persister, two boundaries" | **298**, **432** | **397** explicitly withdraws it: "it does not carry 'two boundaries,' because the light-cone half of that pairing is deleted throughout (§8, §10)" | STALE |
| 1.4 | "binding supplies a rest frame and present tense"; §10 title "binding, not rest mass" | §10 title **416**; body **418**, **420**, **422** | §10 retitled **379** "an operational scope condition"; **385** is a deletion notice naming "binding, not rest mass, draws the wall," binding-as-admission-criterion, and the rest-frame/proper-time/invariant-mass reading as removed | STALE |
| 1.5 | Force taxonomy: EM the unique maker of statistical boundaries; strong/weak disqualified; unscreened gravity ⇒ no statistical boundary; long-range non-additivity ⇒ nonzero Integration floor (register RED-12) | **290**, **292** | **254** lists all four as deleted; **252** retains only the narrow passive/actively-maintained statement. §8 retitled at **250** | STALE |
| 1.6 | Table 3 / Table 3′ row "Screenability & causal boundary \| forced \| definition/stipulated-weld (standard EM + GR)" | **750** | absent; **588** states "After v1.26 the hard floor is **one row**, not two … The second row that formerly sat beside it — the causal-boundary …" | STALE |

Change-set edits: **Task 18a** (light cones, Figures 3/4), **Task 18b** (binding / rest frame / present tense), **Task 18c** (force-screenability taxonomy) — order items H2 / RED-12, 13, 14.

### RED 2 — the Drive→Memory theorem → **LIVE**

| # | Aster's textual target | v1.25 | v1.26 | Verdict |
|---|---|---|---|---|
| 2.1 | "The paper's proof of `sigma > 0 => E > 0`" | **129**, **605–606**, **747** | **123** ("a strictly positive entropy production rate implies a strictly positive excess entropy (σ > 0 ⇒ E > 0)"), **443–444**, **573** | LIVE |
| 2.2 | "the premise that an i.i.d. process equals its own time reversal" | **129**, **606** | **444** still runs the same route verbatim: "E=0 ⟺ i.i.d. ⇒ (time-reversible ⇒) σ=0, whose contrapositive is σ>0 ⇒ E>0". **125** adds "**Third — a time-reversal parity condition, new in v1.26**" as one of four scope conditions | LIVE, scope condition added |
| 2.3 | "the claim cannot remain `forced x theorem/corollary`" | **747**: `\| D→M memory floor, direction σ>0 ⇒ E>0 \| forced \| theorem/corollary \|` | **573**: `\| D→M memory floor, direction σ>0 ⇒ E>0 \| forced (four scope conditions, incl. time-reversal parity) \| theorem/corollary \|` | **LIVE — status not downgraded**, annotated only |
| 2.4 | Source locations "Section 4; Table 2; Table 3; Table 3-prime" | §4 at **125**; Tables at **587**, **741** | §4 at **119**; Table 3 at **425**; Table 3′ at **567** — all present | LIVE |
| 2.5 | "downgrade … to conditionally forced × proposed lemma" (Aster's status recommendation) | — | **588** does the opposite: it names this row as the framework's **single** remaining `forced × theorem/corollary` hard floor | not adopted |

**Per the order's calibration note:** prime has already adjudicated blocker 2 as LIVE on analytic, version-independent grounds. Text-matching returns the same verdict independently. Not re-litigated here.

### RED 3 — the life criterion → **STALE in canon, RELOCATED**

| # | Aster's textual target | v1.25 | v1.26 canon | Verdict |
|---|---|---|---|---|
| 3.1 | "the internal-model requirement of life" | **460**, **464**, **654** | 2 occurrences: **492** (§12 row, describing the relocation/regrade) and **846** (changelog). §11a itself (**408–413**) does not carry it | STALE |
| 3.2 | the test "does a separate reference node exist?" | **495** ("its set-point is held in a *separate, separately-interventable reference node*"), **503** | phrase absent. **492** restates it as "a proper invariant subspace whose dynamics are autonomous with respect to the regulated coordinates — preserved under similarity transform" | STALE as quoted |
| 3.3 | the "new definition" wording, "at the head of the paper, in Section 11a, in the claim ledger, and in the version history" | head **33**; §11a **480–481**; ledger **653–654**; history **890**, **909** — **all four confirmed** | live body: **zero**. Sole occurrence is **846** (changelog, recording the removal). The head-of-paper life note (v1.25 22–43) is gone; v1.26 line 22 is `---`. §11a at **412**: "deliberately **not** named *alive* here" | STALE in body |
| 3.4 | Francis–Wonham / Bich et al. over-read (register RED-17) | **460**, **463–464**, **478** | body: **492** only, as a relocation record. Reference entries at **694**, **696** | STALE in body |
| 3.5 | coordinate/realization dependence, "Apply arbitrary similarity transforms" (register RED-18 required test) | **654** carries the smaller E3 version | **492** asserts the invariant restatement | text present; **whether the test was run is not a text-matching question and is not answered here** |

Change-set edits: **Task 19a** (de-announce), **19b** (control-theory relabel), **19c** (subspace restatement), **Task 15** (§4a relocation), destination `AOP_LifeArchitecture_Followon_v0.1.md`.

### RED 4 — `Φ_MIP > 0` does not establish an individual → **STALE**

| # | Aster's textual target | v1.25 | v1.26 | Verdict |
|---|---|---|---|---|
| 4.1 | "a `Phi_MIP > 0` collective is a single higher persister" | **372** (verbatim), also masthead **13**, ledger **674**, changelog **980** | **332–333**: "Versions ≤1.25 stated that a collective with Φ_MIP > 0 at the part-partition **is a single higher persister** … **That claim is deleted in v1.26.**" Ledger row **499** carries "synchronic individuality claim deleted" | STALE |
| 4.2 | "`Phi_MIP approximately 0` is a pile" | **374** ("a collective with Φ_MIP ≈ 0 is a pile with no collective present tense") | **340** retains "exactly zero on a block-decomposable pile" **as a property of the measure**, without the individuality reading | word survives, claim stale |
| 4.3 | Aguilera & Di Paolo citation mismatch (register RED-15 A) | **141** ("[Aguilera & Di Paolo 2019]" attached directly to Φ_MIP); reference entry **835** | **135**, **472**, **670** all re-attribute as lineage/inspiration with explicit non-transfer language | STALE |
| 4.4 | Aster's recommended rename to "minimum-cut dependence / minimum-cut irreducibility diagnostic" | 0 occurrences in v1.25 | **24 lines** in v1.26; `Φ_MIP` occurrences fall **36 → 13**, several of the 13 in masthead/back matter | adopted |
| 4.5 | "The manuscript contradicts its own retraction" (§9a vs §13a) | **371–377** vs **775** ff | **335** names the §13a contradiction as the stated reason for deletion | STALE |

Change-set edit: **Task 14**, parts 1–3.

### RED 5 — the five archetypes → **PARTIAL**

| # | Aster's textual target | v1.25 | v1.26 | Verdict |
|---|---|---|---|---|
| 5.1 | "primary evidence" | **440** ("they are the framework's primary evidence that the four-fold carving is the right one") | **405** deletes it explicitly. Remaining occurrences at masthead **13** and changelog **842** only | STALE |
| 5.2 | **Crystal:** "Nothing it holds bears weight for continued persistence; it is terminal" | **430** | **395** replaced with the passive-load-bearing reading ("disrupt the lattice and the crystal ceases … yet holding that lattice costs no drive at all") | STALE |
| 5.3 | **Flame:** "essentially no memory" | **60** (§1) and **430** (§11) | **395** (§11) fixed to "shallow or short-lived memory" with the overstatement named. **§1 line 40 still reads "A flame is a real persister — a sharp, actively maintained boundary — carrying essentially no memory."** | **LIVE** — one of two live-body survivors |
| 5.4 | **Spore:** `C_mu` read off material complexity | §4 **131**, §11, §5 | **125** / §4 / §11 separate the three notions; the spore is demoted to a motivating thought experiment and named a category error to read `C_μ` off material complexity | STALE |
| 5.5 | **Atom:** "a 'brief' persister"; EM skin as membrane; private light cone | **432** ("It persists — briefly, modestly, really") | **397** explicitly strikes "brief" and deletes the light-cone half | STALE |
| 5.6 | **Star:** "All four dimensions near maximal" | **434** | **399** explicitly struck, with the no-common-normalization reason stated | STALE |
| 5.7 | **Star:** "An `n=3` polytrope is not a generic star"; model-specificity | Figure R★ caption **438** | Figure R★ retained at **403**, `n=3` Lane–Emden construction intact; now labelled a model result (Task 3 / 21) | **LIVE** — the construction Aster calls model-specific is still the construction |

Change-set edits: **Task 21** (archetype demotion), **Task 9** (spore/`C_μ` separation). **The §1 flame instance (5.3) is not covered by any change-set edit.** Task 21 records the flame fix as "Applied in §11, the §11 closing paragraph, and §13" — §1 is not in that list, and line 40 is unchanged from v1.25 line 60 on this phrase.

### RED 6 — the observer → **PARTIAL**

| # | Aster's textual target | v1.25 | v1.26 | Verdict |
|---|---|---|---|---|
| 6.1 | "the observer is the system's own viability function" | **284** ("At the grain that matters for persistence, the observer is nothing external: it is the system's own viability function") | **246** quotes and withdraws it: "'The system is its own observer' is therefore withdrawn as a formulation" | STALE |
| 6.2 | "the viable fact is observer-independent" | **286** ("what is observer-independent is only the bare fact that the current state either is or is not viable") | **248** retains the structural-fact chain, reworded: "the bare membership fact … is analyst-independent *once the set is declared*" | **PARTIAL** — claim survives, relativized |
| 6.3 | "agentless selection evaluates it" | **286** ("What plays the evaluator is selection, which is agentless") | **248**: "What plays the *selector* over such states is selection, which is agentless" | **PARTIAL** — sentence survives, role-word narrowed evaluator → selector |
| 6.4 | §7 as the site (register RED-11 source locations §§3, 7, 9, 11a, 12″) | title **282** "The observer, located" | title **244** "The observer, located: **semantic claims are declaration-relative**" — Aster's recommended clean position adopted as the section title | adopted |

Change-set edit: **Task 13**.

### RED 7 — the living master is not a journal manuscript → **LIVE, and larger**

Measured on the master, live-body-versus-back-matter distinction deliberately set aside because this blocker is *about* the back matter.

| # | Aster's textual target | v1.25 | v1.26 | Δ |
|---|---|---|---|---|
| 7.1 | "The masthead version paragraph alone is roughly 1,443 words" | line 13 = **1,443 words** (exact) | line 13 = **1,600 words** | **+157 (+10.9%)** |
| 7.2 | retractions inside the article | 22 lines match `retract*` | 26 lines | +4 |
| 7.3 | verification notes / unresolved citation warnings | `⚠` on 15 lines; `[✓ …]` 15; `[~ …]` 4 | `⚠` on **18** lines; `[✓ …]` 15; `[~ …]` **6** | +3 / 0 / +2 |
| 7.4 | repository DOI placeholder (register RED-26) | present | present, Data Accessibility line **624** | — |
| 7.5 | unretrieved Joyce foreword (register RED-26) | 9 lines mention Joyce | 6 lines; ⚠-flagged status retained | — |
| 7.6 | status gates (Table 4 gate ledger) | present | present at **508**, **606**, **726** | — |
| 7.7 | `[P0-n]` audit markers | 4 lines | 4 lines (**13**, **73**, **88**, **429**) | — |
| 7.8 | full changelog inside the article | back matter | back matter, **extended** by the appended v1.26 entry (**837–851**) | longer |
| — | whole file | 996 lines / 32,515 words | **851 lines / 37,079 words** | body shrank, document grew |

**This is LIVE by design, not by omission.** Change-set Task 4 removed exactly this material — **from `AOP_Submission_v0.1.md` only**, "retained in the master." Blocker 7's disposition therefore does not live in v1.26 at all; it lives in the derivative.

---

## 3. Where the relocated text went — extension beyond the declared inputs

The order's §2 inputs are the deposit, v1.26, v1.25, and the change set. Blockers **3** and **7** are answered by *relocation*, so "STALE in v1.26" alone would be misleading: a blocker whose text moved is relocated, not answered. Both destination files were therefore located and checked for **presence/absence of Aster's named targets only**.

**This is a retrieval fact, not a verification.** Both destination files are this seat's own build; per order §5 this seat does not verify them, and nothing below claims the relocated treatments are adequate. That judgement belongs to a clean seat and to prime.

| File | Drive ID | Bytes | md5 | Lines / words |
|---|---|---|---|---|
| `AOP_LifeArchitecture_Followon_v0.1.md` | `1pP-phsxzzrSIT5GmjCxi7iYmyBr9tyKR` | 38,799 | `9bad4a34922ce5b99846c05a774ea49a` | 221 / 5,792 |
| `AOP_Submission_v0.1.md` | `1f7KokyHoWnF3jHzBco1DdyRVt8QWsnER` | 179,393 | `09b04a234dbf5cd4a6079fba496fcc5f` | 709 / 26,640 |
| `AOP_v1.26_FlagList.md` | `1JYbfdmT45wlE2RmiM3hJNO4WPA559Xs7` | 15,126 | — | — |

All three are in the **Canon** folder `1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J`, not Canon Development.

**Blocker 3 targets in the follow-on** — present, and present as *withdrawals*: line 21 records the "new definition, graded frontier" posture removed, the six-part conjunction relabelled an AOP hypothesis, and "the internal-model requirement of life" retired; line 31 restates the withdrawal; line 55 labels the conjunction an AOP hypothesis with "**No cited result forces this conjunction**"; line 59 retires the Francis–Wonham phrase; lines 69–71 restate the discriminator subspace-wise; line 85 carries the third-person detectability scopes. Aster's blocker-21 target ("Death is the four axes failing as one") appears at lines 137–139, reframed as cessation-at-grain. **"essentially no memory" — zero occurrences.** The follow-on's own masthead is 41 words, so blocker 7 does not attach to it.

**Blocker 7 targets in the submission derivative** — masthead line 13 is **18 words**; `⚠` **0**; `[✓ …]` **0**; `[~ …]` **0**; `[P0-n]` **0**; `Version 1.x` changelog entries **0**; DOI-placeholder pattern **0**; "new definition" **0**; "primary evidence" **0**; Table 4 gate ledger **0**. Two residual matches for a clean seat to look at, reported without comment: `retract` at line **560**, and `light cone` at line **446**.

**One cross-file consistency fact, reported as data:** `"essentially no memory"` appears at **line 40 of v1.26** and at **line 40 of the submission derivative** — the same §1 sentence, carried into both. This is the RED 5 survivor (5.3 above) reaching the submission file. Recorded; not adjudicated; not this seat's to fix.

---

## 4. What this triage does not establish

- It does **not** say whether Aster is right about anything. Seven blockers, zero adjudications.
- A **STALE** verdict means *the text Aster quoted is gone or materially changed*. It does not mean the underlying objection was answered — text can move (blockers 3, 7), be narrowed (blocker 6), or be deleted for a different stated reason than the one Aster gave.
- A **LIVE** verdict means *the text is still there*. It does not mean Aster is correct that it should not be. Blocker 2 is the sharp case: LIVE, and prime has separately adjudicated that the criticism stands on analytic grounds; blocker 7 is LIVE by an explicit design decision.
- It does **not** verify the v1.26 build. That pass is a clean seat's, per order §5.

---

*End of `AOP_Aster_BlockerStaleness_Triage_v0.1.md` v0.1. Produced by the execution seat, which built v1.26 and therefore does not bless it. Prime verifies by independent re-match, not by reading this over.*
