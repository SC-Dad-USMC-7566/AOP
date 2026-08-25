# CW Verification Report — Life-Definition Adjudication and Hardening Arc

**Document ID:** `AOP_LifeDef_CW_VerificationReport_v0.1.md`
**Seat:** Cowork (CW). **Order:** CW-1, §5 of `AOP_WorkOrder_LifeDefinition_Adjudication_20260803.md` (`1u_ZW8td5Ah70vBBeWgXbAzDDNM4-dw7y`, 26,186 B).
**Run:** 3 August 2026. **Status:** partial — Gate 3 items blocked, unblocked items complete.
**Role discipline:** this seat verifies. Nothing below grades the science or rules on any case. Where the report says a claim is wrong, it means the bibliographic record does not support it as written, not that the underlying science is wrong.

---

## 0. Headline findings

1. **The v1.27 candidate repairs cleanly and reproduces the certified build byte-for-byte.** Stripping the three spliced paths — a deletion of exactly 201 bytes and nothing else — yields 255,684 B / md5 `998aa87e0927f84ae6ea1676ebe8ca93` / 851 lines. All three certification targets hit. **Not placed, per instruction.**
2. **The corruption destroyed nothing.** It was a pure insertion. The work order's characterisation — "destroying 1,108 characters" — is **incorrect**; no canon text was lost. Correcting this matters, because it changes the remedy from "rebuild" to "delete 201 bytes."
3. **The repaired v1.27 masthead was never bumped.** Line 13 of the repaired file is byte-identical to line 13 of v1.26 and still reads `version 1.26 · compiled 25 July 2026`. Reported, not fixed.
4. **Ten of the shared-substrate citations in §1.2 were pre-checked. Five carry errors and one does not resolve to a real paper.** The order says "cite these exactly; do not paraphrase the citations from memory" — so these are corrected below *before* CS and OAI build on them.
5. **CW-1 items 1–3 cannot start.** No CS or OAI deliverable under this order exists on Drive. Gate 1 has not been passed.

---

## 1. Startup check

Startup check — 3 August 2026
[✓] AOP Charter — v1.2 (read in full, current project instructions)
[✓] AOP Canon (the paper) — v1.26, **independently hash-verified**, not size-matched
[✓] `AOP_LifeArchitecture_Followon_v0.1.md` — retrieved and hashed
[ ] AOP → Ladder bridge memo — not read; this task does not touch the Ladder connection
Drive connector: **on**.

### 1.1 Independent hash verification of the governing documents

Method: raw bytes fetched via the Drive connector, decoded from base64, hashed locally. Line counts by `str.split("\n")` per the order's convention.

| Document | Drive ID | Bytes | md5 | Lines | vs. work order |
|---|---|---|---|---|---|
| `AOP_CANON_MASTER_v1.26.md` | `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn` | 254,046 | `54ceb3772e29f25c6e139b703d550d59` | 851 | **✓ byte count and md5 both match exactly** |
| `AOP_LifeArchitecture_Followon_v0.1.md` | `1pP-phsxzzrSIT5GmjCxi7iYmyBr9tyKR` | 38,799 | `9bad4a34922ce5b99846c05a774ea49a` | 221 | ✓ byte count matches; no md5 was stated in the order — one is supplied here for future runs |
| `AOP_WorkOrder_LifeDefinition_Adjudication_20260803.md` | `1u_ZW8td5Ah70vBBeWgXbAzDDNM4-dw7y` | 26,186 | not hashed (read via text extraction, not byte download) | — | — |

The canon v1.26 hash-verification claimed in the work order masthead is **confirmed independently**. Its text contains zero occurrences of `/Users/` — it is uncontaminated.

---

## 2. CW-1.5 — the corrupt v1.27 candidate

**Instruction:** strip the three local Downloads paths spliced into the masthead at line 13 and report whether the result reproduces the certified build byte-for-byte (255,684 B / md5 `998aa87e…` / 851 lines). **Do not place it either way.**

### 2.1 State as found

`AOP_CANON_MASTER_v1.27_candidate.md` (`1UaBvTmUYUmIXY6AkVfh2JgexAQIHyBKG`) — 255,885 B, md5 `70da21ff9be7720a41fee7b1dfb0c880`, 853 lines.

A **second byte-identical copy** exists at `14SJO_sWJ_IqG07jQIAfwAYDSJ0umagk5` in a different folder (`1UUMhzYjH1EKghb5E5eARK3KCj-0xIy4h`). Hashed independently; same md5. Both copies are corrupt. **No clean 255,684 B copy of v1.27 exists anywhere on Drive** — a title search across `v1.27` / `v1_27` returned only these two candidates and the changesets. The certified build exists only as a hash in prose.

### 2.2 The splice, exactly

Three paths were inserted at byte offset 1665, joined by two newlines, in the middle of the masthead sentence. The original text read:

> `…relocates the life block and diachronic-identity material to a dedicated follow-on; and demotes the five archetypes…`

The corrupt text reads `…material ` + the three paths + `to a dedicated follow-on; and demotes…`:

```
/Users/benbayless/Downloads/AOP_ChangeSet_v1_25_to_v1_26_CORRIGENDUM.md
/Users/benbayless/Downloads/AOP_Canon_ChangeSet_v1_26_to_v1_27.md
/Users/benbayless/Downloads/AOP_CANON_MASTER_v1.27_candidate.md
```

Inserted region: bytes 1665–1866. Length: 71 + 1 + 65 + 1 + 63 = **201 bytes**. The two embedded newlines are what turned an 851-line file into an 853-line file.

### 2.3 Repair result

Excise bytes 1665–1866. No other edit. Result:

| Target | Certified | Repaired | |
|---|---|---|---|
| Byte count | 255,684 | **255,684** | ✓ |
| md5 | `998aa87e…` | **`998aa87e0927f84ae6ea1676ebe8ca93`** | ✓ |
| Lines (`str.split("\n")`) | 851 | **851** | ✓ |

sha256 of the repaired file, recorded for future runs: `99f64eccb5d28b3ce8dcaa4ccf79c3a9fb6c3dc4563747b799cc5c9903800aff`

**Verdict: the repaired file reproduces the certified build byte-for-byte.** Held locally to this session. **Not placed on Drive, per instruction.** It can be deposited on one word from Ben or prime.

### 2.4 Two findings the order did not anticipate

**Finding CW-A — nothing was destroyed.** The order states the splice destroyed 1,108 characters. It did not. 255,885 − 255,684 = 201, and the 201 removed bytes are exactly the three paths and their two newlines; the surrounding sentence closes correctly on `material to a dedicated follow-on`. The corruption was **insertion-only**. Whatever produced the 1,108 figure, it was not a byte diff against the certified build.

**Finding CW-B — the v1.27 masthead was never bumped.** A line-level diff of the repaired v1.27 against v1.26 gives **9 differing hunks, every one an in-place line replacement**, with no insertions or deletions anywhere (hence both files at 851 lines):

`40 · 123 · 125 · 147–148 · 181 · 236 · 442–444 · 573–574 · 588`

**Line 13 — the masthead — is not among them.** The certified v1.27 build still self-identifies as `version 1.26 · compiled 25 July 2026`. This is reported as an observation about the build, not as a defect to be repaired by this seat; whether it matters is prime's call.

---

## 3. Pre-pass — bibliographic verification of the §1.2 shared substrate

**Scope note, declared.** CW-1.1 tasks this seat with the citations in *CS and OAI deliverables*. No such deliverable exists yet. This seat extended scope to the ten citations in the work order's own §1.2 and §1.3 on the reasoning that §1.2 opens with *"Cite these exactly; do not paraphrase the citations from memory"* — so an error there propagates into both blinded seats simultaneously and is cheapest to catch now. **This is a scope extension and prime may reject it.** It contains no interpretation of the rival criteria; every entry is a record check.

Method: two independent verification passes against primary sources and publisher records. Tags per §1.4: ✓ full text read · ~ abstract/metadata only · ⚠ not retrieved.

### 3.1 Corrections required

| # | As written in §1.2 | Finding | Corrected |
|---|---|---|---|
| **R2** | `Varela FJ, Maturana HR, Uribe R` | **Author initial wrong.** The printed byline is `F.G. VARELA, H.R. MATURANA and R. URIBE`. Varela published as Francisco **G.** Varela in this period and switched to Francisco **J.** later. Crossref confirms F.G. | `Varela FG, Maturana HR, Uribe R. "Autopoiesis: the organization of living systems, its characterization and a model." BioSystems 5(4):187–196 (1974). doi:10.1016/0303-2647(74)90031-8` **✓** |
| **R4b** | `Marshall SM et al., Nat. Commun. 12 (2021)` | Incomplete, not wrong. Nature Communications does not paginate; the locator is an article number. | `Marshall SM, Mathis C, Carrick E, Keenan G, Cooper GJT, Graham H, Craven M, Gromski PS, Moore DG, Walker SI, Cronin L. "Identifying molecules as biosignatures with assembly theory and mass spectrometry." Nat. Commun. 12:3033 (2021). doi:10.1038/s41467-021-23258-x` **✓** |
| **A1** | `Abrahão FS et al., PLOS Complex Systems 1:1–20 (2024)` | **Page range wrong.** There is no 1–20 pagination; `1–20` is the printable-PDF pagination, not the citable locator. | `Abrahão FS, Hernández-Orozco S, Kiani NA, Tegnér J, Zenil H. "Assembly Theory is an approximation to algorithmic complexity based on LZ compression that does not explain selection or evolution." PLOS Complex Systems 1(1):e0000014 (2024). doi:10.1371/journal.pcsy.0000014` **~** |
| **A4** (§1.3, cell-problem loci) | `Durant et al., Phil. Trans. R. Soc. B 2019` | **Does not resolve.** Year and venue belong to two different papers, and in the Phil Trans B paper Durant is third author, not first. | Two real candidates: (i) `Pezzulo G, LaPalme J, Durant F, Levin M. Phil. Trans. R. Soc. B 376(1821):20190765 (2021). doi:10.1098/rstb.2019.0765` — the DOI string contains "2019" but the issue is 2021; (ii) on content, the paper that actually says what the order cites it for is `Durant F, Morokuma J, Fields C, Williams K, Adams DS, Levin M. "Long-Term, Stochastic Editing of Regenerative Anatomy via Targeting Endogenous Bioelectric Gradients." Biophys. J. 112(10):2231–2243 (2017). doi:10.1016/j.bpj.2017.04.011` **~** — its abstract carries the rewritable-setpoint language ("permanently rewritten by a brief perturbation of endogenous bioelectrical networks"; "a multistable, epigenetic anatomical switch"). **Prime should pick one; this seat does not choose.** |
| **R4a** | `Sharma A, Czégel D, …` | Correct in every field. Diacritic on **Czégel** is present in the order and should be preserved downstream. | No change. **✓** |

### 3.2 Characterisation flags — the citation is right, the sentence around it is not

| # | Flag |
|---|---|
| **R1** | The order calls the Joyce wording the **"NASA working definition"** on Cleland & Chyba's authority. **Cleland & Chyba never use that phrase** — they call it the *"chemical Darwinian" definition*. They also attribute the wording to **two** Joyce items (`1994a;b`), not the Foreword alone. Separately, two wordings are in circulation: Cleland & Chyba print *"self-**sustained** … capable of **undergoing** Darwinian evolution"* (the order's variant); SEP and NASA Astrobiology print *"self-**sustaining** … capable of Darwinian evolution"*. **Which is Joyce's literal printed wording is unverified** — the Foreword itself is ⚠ **not retrieved**, exactly as the order already flags. Cleland & Chyba's own record is otherwise **✓ fully verified**: vol. 32(4):387–393 (2002), doi:10.1023/A:1020503324273, and they do quote the sentence verbatim. Recommend the order either attribute the wording explicitly to Cleland & Chyba or source the NASA framing elsewhere. |
| **R2** | The **six-rule observer key is confirmed verbatim** and the order's characterisation is exact, not loose. The paper's own words: *"The following is a six-point key for determining whether or not a given unity is autopoietic:"* — six gated pass/fail steps, pp. 192–193. **✓** |
| **R3** | Metadata **all correct** (OUP, 2003, ISBN 978-0198507260; Hungarian original *Az élet princípiuma*, Gondolat, Budapest, 1971). The **absolute vs. potential distinction is confirmed** as Gánti's own terminology. Two cautions: the volume is normally cited **with commentaries by Griesemer and Szathmáry**, and the **count of potential criteria is disputed in the secondary literature** — Griesemer enumerates five, Bedau collapses them to three. **Gánti's own pp. 77–79 were not read** (both hosted PDFs are image-only). Tag: **~**. If prime's priority claim for R3 on the alive≠reproducing split leans on the enumeration, it needs the printed pages. |
| **R5** | Citation **✓ fully correct**. But the characterisation needs tightening in two ways the author himself insists on: Friston calls it a **"heuristic proof,"** not a theorem; and the minimisation is predicated of **internal states**, over a free energy functional **of the blanket states** — not of "the system" minimising free energy simpliciter. Verbatim: *"life — or biological self-organization — is an inevitable and emergent property of any (ergodic) random dynamical system that possesses a Markov blanket."* If AOP leans on this as established, the author's own hedge should survive into the citation. |
| **A2** | Citation **correct** (Uthamacumaran A, Abrahão FS, Kiani NA, Zenil H, npj Syst. Biol. Appl. 10:82 (2024), doi:10.1038/s41540-024-00403-y). But **the explicit LZ claim lives in A1, not A2** — LZ is in A1's title; A2 makes the weaker general compression-equivalence claim. The order attributes "may reduce to LZ compression" to both; it belongs to A1. **~** |
| **A3** | Citation **✓ correct and full author list recovered**: `Hazen RM, Burns PC, Cleaves HJ II, Downs RT, Krivovichev SV, Wong ML. "Molecular assembly indices of mineral heteropolyanions: some abiotic molecules are as complex as large biomolecules." J. R. Soc. Interface 21(211):20230632 (2024). doi:10.1098/rsif.2023.0632`. The paper concludes abiotic heteropolyanions reach MA 21 and that *"values of molecular assembly indices ≥15 do not represent unambiguous biosignatures."* **Flag:** the order describes this as a ruling by *"Cronin/Walker"* on abiotic high-assembly minerals. **No author of A3 is from the Cronin or Walker groups.** If CS-1.2 cites A3 as the rival's authors ruling on their own case, that is a misattribution — it is a third-party refutation, which is a different evidentiary status. |

### 3.3 Count

Ten citations checked. **Five carry a correction** (R2 initial, R4b incompleteness, A1 locator, A4 non-resolving, plus R1's attribution). **Four carry a characterisation flag** where the record is right but the surrounding sentence overstates or misattributes (R1, R5, A2, A3). **Two remain unverifiable at the primary source** and are correctly tagged ⚠/~ already (Joyce's Foreword; Gánti's pp. 77–79). **No fabricated author bylines were found** in this set — the §1.4 base-rate warning did not recur here, though A4's conflation of two real papers into one non-existent one is the same failure mode at lower severity.

---

## 4. Blocked items — gate status

| Item | Status |
|---|---|
| **CW-1.1** bibliographic pass over CS and OAI deliverables | **Blocked.** No deliverable under this order exists. A Drive title search for `AOP_LifeDef` returns nothing. The four CS deposits (`…VerdictMatrix`, `…RivalMatrix`, `…CellProblem`, `…Amendments`) and `AOP_LifeDef_OAI_Attack_v1.0.md` are all absent. **Gate 1 has not been passed.** |
| **CW-1.2** independent hash verification of deposits | **Blocked** — nothing deposited. Method rehearsed and confirmed working in §1.1 and §2; will run on demand. |
| **CW-1.3** chart build | **Blocked** — depends on CS-1.2 content, which does not exist. This seat will not synthesise verdicts to populate it. |
| **CW-1.4** confirm CS's context refreshed to Charter v1.2 | **Not verifiable from this seat.** Cowork cannot inspect another seat's loaded project context. Recommend CS state its charter version in the CS-1.1 masthead so the check becomes an artifact check rather than an assertion. **Reported as instructed.** |
| **CW-1.5** v1.27 repair | **Complete.** §2. |

Related documents that exist but belong to the **prior** arc (`TASK AOP LifeCriterion Falsification WorkOrder v0.1`, 1 Aug), not this one — noted so they are not mistaken for Gate 1 deposits:
`AOP_LifeCriterion_Gate1_PrimeAdjudication_v0_1_20260803.md` (`16Ev9APq8gKDClQwbwhRXv4dQUD-JgK-h`) · `REV_AOP_LifeCriterion_Gate1_OAI_Attack_v0_1_20260803.md` (`13NjxqrOHXzDn99ElGQ2zkCaVk0XzvmwD`) · `AOP_Handoff_Prime_20260803.md` (`1V4ICkgLgpbpCARenWRnF_bKK1LgyvwwE`).

---

## 5. What this seat did not do

- Did not place the repaired v1.27, in either direction.
- Did not repair the unbumped masthead.
- Did not read Joyce's Foreword or Gánti pp. 77–79. Both are tagged accordingly and neither is claimed as verified.
- Did not read the full bodies of A1, A2, or the A4 candidates — abstract and publisher-record level only, tagged ~.
- Did not rule on any of the 32 cases, did not grade any claim, did not choose between the two A4 candidates.
- Did not hash the work order itself (retrieved via text extraction rather than byte download).

---

*End of `AOP_LifeDef_CW_VerificationReport_v0.1.md`. Deposited to Drive by the Cowork seat, 3 August 2026. Nothing in this report grades its own homework; the repair in §2 is verifiable by any seat that re-runs the 201-byte excision against the stated md5.*
