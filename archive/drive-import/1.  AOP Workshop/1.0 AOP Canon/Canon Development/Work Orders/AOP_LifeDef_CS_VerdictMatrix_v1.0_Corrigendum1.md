# CS-1.1 CORRIGENDUM 1 — arithmetic corrections to the §6 score summary

**Document ID:** `AOP_LifeDef_CS_VerdictMatrix_v1.0_Corrigendum1.md`
**Seat:** Claude Science (builder). **Date:** 3 August 2026.
**Corrects:** `AOP_LifeDef_CS_VerdictMatrix_v1.0.md` — Drive `1-LwfaBon87eOINIEfBBje_LCOFQ1W6Ae`, 29,347 B, md5 `78d512b98183c8823e004aef9694b094`, 260 lines.

**Why this is a separate file.** The matrix is hash-stamped under the order's anti-gaming clause and may not be overwritten. It is not overwritten. This corrigendum is deposited alongside it, per §1.4: *disclose rather than repair silently.*

**NO CASE VERDICT CHANGES.** Every per-case row in §2, §3, §4.1 and §4.3 of the stamped matrix stands exactly as deposited. What was wrong was my own tallying of those rows in the §6 summary. The granular data was right; the summary of it was not.

---

## 1 · The two errors

Found by an independent review pass, confirmed by re-parsing all 35 scored rows out of the stamped file itself.

### Error 1 — the NEITHER count

| | |
|---|---|
| §6 stated | NEITHER = **17** |
| Correct | NEITHER = **19** |

The enumerated list in the same table already named 19 cases (A5, A6, A7, A8, B1, B2, B3, B6, C1, C2, C4, C5, C6, C7, D3, D4, D6, D7, D8′). The list was right; the integer beside it was wrong. Corrected score summary:

| Verdict | Count | Cases |
|---|---|---|
| ALIVE | 9 | A1, A2, B7, B8, C3, C7′, C8, D2, D5 |
| PAUS\* | 4 | A3, A4, B4, D8 |
| **NEITHER** | **19** | A5, A6, A7, A8, B1, B2, B3, B6, C1, C2, C4, C5, C6, C7, D3, D4, D6, D7, D8′ |
| UNDETERMINED | 2 | B1′, B5 |
| NOT-WELL-POSED | 1 | D1 |
| **Total scored rows** | **35** | 32 frozen cases + 3 alternate-S scorings (B1′, C7′, D8′) |

9 + 4 + 19 + 2 + 1 = 35. The stamped version's arithmetic did not close; this does.

### Error 2 — the deciding-clause distribution

| Clause | §6 stated | Correct |
|---|---|---|
| c1 | 11 | **12** |
| c2 | 2 | 2 |
| c3 | 6 | **5** |
| c4 | 0 | 0 |
| c5 | 12 | 12 |
| c6 | 4 | 4 |

Sum: 35, matching the row count. The stamped figures summed to 35 as well, which is why the error survived my own check — **two compensating misassignments between c1 and c3**, not a dropped row. A checksum on the total would not have caught it; only re-parsing the column did.

The downstream sentence in §6 read *"Together they decide 23 of 32."* Correct: **c1 and c5 together decide 24 of 35 scored rows** — 12 + 12. Note the denominator was also wrong in the stamped text: 32 is the number of frozen cases, but 35 rows are scored, because three cases carry a second scoring under an alternate declaration of S.

---

## 2 · What survives, and it is all of it

Both corrections **strengthen** the findings they appear in, which is worth stating explicitly so no one has to check:

- **Clause (4) still decided nothing.** c4 = 0 in both the stated and the corrected distribution. The observation in §6 that separate-interventability is redundant with clause (3) on this case set is untouched.
- **The two-clause shape of the criterion is sharper, not weaker.** c1 and c5 decide 24 of 35 rows (69%) rather than 23 of 32 (72%) — a marginally lower fraction of a larger, correctly-counted denominator, and the qualitative claim is unchanged: the criterion operates as a two-clause test, *is there a separable regulator, and is its stored target about the system itself?*
- **Clause (5) remains the single most decisive clause**, tied with c1 at 12 and carrying every Tier C and Tier D exclusion.
- **All six predicted failures in §5 stand**, including F6 on the paradigm case. None depended on a tally.

---

## 3 · The disclosure

This seat produced a summary table that contradicted the data in its own document, and did not catch it before deposit. The error was found by review, not by the author. Recording it here because the order treats the base rate of defects as non-zero and asks for disclosure rather than silent repair, and because a seat that only reports the defects someone else would not have found is not being audited.

The failure mode is worth naming for CW: **the totals summed correctly while the individual counts were wrong.** A verification pass that checks only whether a distribution sums to the row count will pass this error. Re-parsing the column is the check that catches it.

---

*End of `AOP_LifeDef_CS_VerdictMatrix_v1.0_Corrigendum1.md`. The stamped matrix is not modified.*
