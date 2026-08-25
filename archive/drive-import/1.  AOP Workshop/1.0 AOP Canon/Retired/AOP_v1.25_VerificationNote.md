# Verification Note — AOP v1.25 cut (for prime's final re-run)

**Delivered for independent verification — not self-blessed. Master placed by Ben.**
This is the fold of the prime-blessed consolidated change set (E1–E3) onto v1.24. No new computation.

## 1. Base match
Built from `AOP_CANON_MASTER_v1.24.md`, SHA-256 **3e64ff0ca93eee3165d53520651dfbbac063489df1ccfa87e3c8242f0dd421cf** (218,602 bytes). Confirmed before any edit.

## 2. Build identity
`AOP_CANON_MASTER_v1.25.md` — SHA-256 **2db4fa5fdc7b912088183d362ee646385c76b073a3a9d0b628f997bb1d7f8c67**, 224,340 bytes.

## 3. Edits applied (9 spans, all intended)
- **7 blessed content edits** (E1-A abstract; Task-A §4 sentence 1; Task-A §4 sentence 2; E1-B §4 append; Task-A Figure T caption; E2 §13; E3 §11a). The three §4/line-189 edits are non-overlapping substrings that compose into one line change.
- **Masthead restamp:** `version 1.24` → `version 1.25` (compile date unchanged — same working day, 23 July 2026).
- **v1.25 changelog entry** appended in house style (bold token, numbered sub-points, "no claim retracted, none strengthened").

## 4. Clean-diff proof
Reverting all edits reproduces the v1.24 base **byte-for-byte** — recomputed SHA equals the base fingerprint. Line-level diff (difflib, autojunk off) shows only: base line 13 (masthead token), line 17 (abstract), line 189 (§4 body), line 191 (Figure T caption), line 654 (§11a), line 773 (§13), and one block inserted at end (v1.25 changelog). Nothing else moved.

## 5. Invariant multiset
- **Citations:** added {} / removed {} — the `[Author YEAR]` set is identical between v1.24 and v1.25.
- **Formal grade tags** (SETTLED / SYNTHESIS / FRONTIER / SPECULATIVE / UNKNOWN / DEFECT): added {} / removed {} — unchanged.
- New numeric tokens appear only inside intended spans and are already-verified deposit numbers (`~0.14`, `~0.01`, `κ ≲ 9`, `Φ_MIP ∈ [0.0003, 0.05]`, `≈0.5`).

## 6. Guards
- **~0.83 scoped, not deleted:** the token survives (6 occurrences, ensemble-scoped in each).
- **Nesting identity untouched:** `TC = I(inside;outside) + TC_inside + TC_outside … 1.8×10⁻¹⁵ …` is byte-identical (outside every edit span).
- **v1.22 trap byte-identical:** `**Version 1.22 (PROPOSED / NON-CANONICAL; 21 July 2026)**` unchanged.

## 7. Encoding
UTF-8 clean, no replacement characters. Fragile tokens verified intact: Φ_MIP, Ptaszyński, R★, μ₊(A), ξ₁ = 6.897, §13, §11b. Masthead reads canonical **version 1.25 · compiled 23 July 2026**.

## 8. Notes for prime / Aster
- **Masthead inline version-history** still leads with "v1.22 is a corrective consolidation …" — left as a record (same minimal discipline as the v1.24 cut; only the head version token moved). Not a defect; flagged so it isn't mistaken for one.
- **Abstract/§4 redundancy** (per Ben's decision) is **left in place**: "dissociate generically" appears in both the abstract (summary) and §4 body (deposit). Intentional, not trimmed this cut.
- **Carried before-final debt** (unchanged, not red-team-gating): full-text reference reads still `~` (Maes 2020, Schnakenberg 1976, Bouchet–Reygner 2016, Oono–Paniconi 1998); ⚠ pagination/DOI confirms (DiFrisco 2018, Joyce 1994, Ashby 1960, Hoel 2016, Bialek–Nemenman–Tishby 2001, Pearl 1988, Hatano–Sasa / Speck–Seifert). Submission-gating only.

**Status: v1.25 cut, folded from prime-blessed E1–E3. Delivered for prime's final re-run, then Aster.**
