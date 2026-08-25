# Verification Note — AOP v1.24 build (for prime)

**Delivered for independent verification — not self-blessed. Please re-run, do not read over.**

## 1. Base match
Built from `AOP_CANON_MASTER_v1.23.md`, SHA-256 **352f8882f4dcb9c9a31ed4f3d02bb9d6de2892562505561105e1ac5404b7f4cf** (217,359 bytes, 994 lines). Confirmed equal to the work-order fingerprint before any edit. Wrong base would have stopped the pass.

## 2. Build identity
`AOP_CANON_MASTER_v1.24.md` — SHA-256 **3e64ff0ca93eee3165d53520651dfbbac063489df1ccfa87e3c8242f0dd421cf**, 218,602 bytes.

## 3. Edit count by category
- T1 masthead: **2** spans (banner removed; version-token + compile-date restamped).
- T2 fold-seam: **1** span (§13 doubled "has now been done" → single statement).
- T3 annotate: **1** span (v1.12 normalization-robustness forward-annotated to v1.22 scope).
- T4 changelog: **1** span (v1.24 entry appended).
Total: **5 edited spans**, all prose-only.

## 4. Clean-diff proof
Reverting all five edits reproduces the v1.23 base **byte-for-byte** — recomputed SHA-256 of the reverted text equals the base fingerprint exactly. A line-level diff (difflib, autojunk off) shows exactly and only these moved regions: base line 3 deleted; base line 15 replaced; base line 775 replaced; base line 889 replaced; one block inserted at end. Nothing else moved.

## 5. Invariant multiset
- **Citations:** added {} / removed {} — the `[Author YEAR]` set is identical between v1.23 and v1.24. No add, remove, reorder, or reword.
- **Formal grade tags** (SETTLED / SYNTHESIS / FRONTIER / SPECULATIVE / UNKNOWN / DEFECT): added {} / removed {} — unchanged.
- **Numeric tokens:** the only deltas are version/section/list-numbering tokens *inside the intended spans* — added `1.24`×2, `23`×2, `2026`, `13` (as "§13"), and list markers `1`/`2`/`3`; removed `1.22`, `21` (the masthead token and compile date). **No claim number moved** — correlations, VIF/λ terms, μ₊(A), ξ₁ = 6.897, ~287×, ~5.7×, Spearman −0.67, b-values, and all historical-entry dates are byte-identical (guaranteed by the §4 byte-for-byte revert).
- The T2 seam fix removed the duplicate sentence "This has now been done." — it contains no citation, number, or grade token, so it does not perturb any of the three multisets. This is the sole Task-2 duplicate-removal permitted by acceptance criterion 4.

## 6. Masthead
Reads canonical **version 1.24 · compiled 23 July 2026** in the v1.21 format (no proposal banner; title / blank / "Living review (Perspective)"). The v1.22 historical changelog entry (`**Version 1.22 (PROPOSED / NON-CANONICAL; 21 July 2026)**`, base line 990) is **byte-identical** — the Task-1 trap third occurrence was not touched. The appended v1.24 changelog entry is present and accurate.

## 7. Encoding
UTF-8 clean, no replacement characters. Fragile tokens verified intact: Φ_MIP, Ptaszyński, R★, μ₊(A), ξ₁ = 6.897, §13, §11b.

## 8. Flags
One structural flag only: the Task-2 bounded discovery found **no** same-category fold-scars beyond the §13/line-775 target (scan detail in the change set). No substantive problems logged — substance is frozen by design.
