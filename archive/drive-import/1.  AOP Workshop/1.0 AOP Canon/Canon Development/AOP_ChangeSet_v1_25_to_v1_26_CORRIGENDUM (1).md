# Corrigendum — AOP change set v1.25 → v1.26 (red-team remediation)

**Corrects:** `AOP_ChangeSet_v1.25_to_v1.26_RedTeamRemediation.md`, Drive `1mI3DkOKD_GOJzf-ImDThA1oSsRo4iEMd`
**Issued with:** order `TASK_CW_AOP_v127_ChangeSet_20260726`, §4
**From:** Claude Cowork (execution seat)
**To:** prime (chat seat) for verification; **Ben** decides
**Date:** 27 July 2026
**Status:** PROPOSAL. Not self-certified.

Three defects live in the v1.25 → v1.26 change set **document only** — not in the canon. Per the order, they are corrected here openly rather than by silent amendment of the original. Two are independently recomputed below from primary artifacts; the third is corroborated against the canon text.

---

## D-1 — the §0 provenance counts are wrong (replaced count)

The change set's §0 "Provenance and integrity" table reports:

> Lines replaced / inserted / deleted | **307 / 30 / 70**

**The replaced figure is wrong.** A `replace` opcode spans a different number of lines on the two sides, so a single scalar "307" cannot be right; the true per-side counts are:

| Quantity | Change set said | **True (recomputed)** |
|---|---|---|
| Lines replaced (v1.25 side) | 307 | **270** |
| Lines replaced (v1.26 side) | 307 | **164** |
| Lines inserted (v1.26) | 30 | **30** ✓ |
| Lines deleted (v1.25) | 70 | **70** ✓ |
| Lines equal (carried byte-identical) | 657 | **657** ✓ |
| Changed regions | 85 | **85** ✓ |

**Insertions (30), deletions (70), equal (657), and region count (85) are correct.** Only the single "replaced = 307" scalar is in error; it should be stated per side as **270 (v1.25) / 164 (v1.26)**.

**Independently recomputed**, `difflib.SequenceMatcher(None, v125_lines, v126_lines, autojunk=False)`, `str.split("\n")`:
- Base `AOP_CANON_MASTER_v1.25.md` (`13tI48fz-l5DundXuyQysPJf7JrSS9xck`): **224,340 bytes, md5 `9c172e015f4adfc9fe827a42687ca2e7`** — matches the change set's own reported source size and hash.
- Base `AOP_CANON_MASTER_v1.26.md` (`1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn`): 254,046 bytes, md5 `54ceb3772e29f25c6e139b703d550d59` (order-verified).
- Result: equal = 657, replace = 270 → 164, insert = 30, delete = 70, regions = 85. This also matches the change set's own §4 machine-diff table when its opcode line-spans are summed.

No canon consequence: the byte-level integrity certification (657 equal lines, references and version history byte-identical) is unaffected — only the summary scalar was mis-stated.

---

## D-3 — Task 9 overstates the propagation to §5 (no canon defect)

Task 9's disposition claims the E / Cμ / stored-organization separation was propagated to **§1 (L40), §5, and §11 (L393)**:

> Three notions separated permanently and never re-fused, in **§4** (v1.25 131 → v1.26 125), with the separation propagated to **§1** (line 40), **§5**, and **§11** (line 393)…

**§5 received no such propagation.** In v1.26 §5 (`str.split("\n")` L188–L203) there is **no occurrence** of `Cμ`, `observation process`, `stored physical organization`, `crypticity`, or `category error` — verified by scan of the section. The separation does appear in §1 (L40) and §11, but the "§5" claim is an **overstated propagation report**, not an executed edit.

This is a defect in the change set's *claim*, not in the canon: §5 is not wrong for lacking the separation — it simply was not touched in that respect. Correction: strike "§5" from Task 9's propagation list (or execute the propagation in a future fold, if desired — a decision for Ben, not folded here).

---

## D-4 — Tasks 1 and 9 cite the crystal sentence / §11 propagation at the wrong line (splice offset)

Task 1 states the crystal-sentence edit as **"v1.25 line 430 → v1.26 line 393"**, and Task 9 lists the §11 propagation at **"§11 (line 393)."** The change set's §4 machine-diff table likewise maps `replace | v1.25 430–430 | v1.26 393–393`.

**The crystal sentence is at v1.26 L395, not L393.** Verified: `A crystal is configuration whose semantics are spent…` begins at L395 (`str.split("\n")`); L393 is the bar-profile description ("the flame's are all in drive…"). There is a **2-line splice offset** in the v1.26 line numbers Tasks 1 and 9 report.

**Task 21's citation is correct:** it gives "v1.25 line 440 → v1.26 line 405," and "motivating cases and illustrations" is indeed at L405.

Correction: Tasks 1 and 9 should read **v1.26 L395** for the crystal sentence and the §11 propagation; Task 21's L405 stands. No canon consequence — the edits themselves landed correctly; only the reported v1.26 line numbers for Tasks 1/9 are off by two.

---

## Summary

| ID | Where | Defect | Correction | Canon affected? |
|---|---|---|---|---|
| D-1 | §0 provenance table | "replaced = 307" is a single scalar for a two-sided quantity and is wrong | **270 (v1.25) / 164 (v1.26)**; 30/70/657/85 stand | No |
| D-3 | Task 9 | "propagated to §5" — §5 was not touched | strike "§5" from the propagation list | No |
| D-4 | Tasks 1, 9 | crystal sentence / §11 propagation cited at v1.26 L393 | **L395** (2-line splice offset); Task 21's L405 correct | No |

All three are document-level. The v1.26 canon is unaffected; it was independently verified 85/85 AUTHORIZED-FAITHFUL and adopted as the base for v1.27.

— End of corrigendum. —
