# AOP v1.16 — Version & Count Reconciliation (P0-6)

**Purpose.** OAI Master Plan Phase 0 action 3: reconcile the canon pointer, manuscript title/version, submission blueprint, change log, and Data-Accessibility statement to one frozen baseline; resolve the README-vs-manifest count disagreement OAI flagged. All counts verified this session against the frozen baseline `FROZEN_aop_canon_v1_16.md` (MD5 `241153bc…`) and the authoritative `aop_reference_punchlist.md` (Drive, 16 Jul 2026 04:26).

**Compiled:** 17 July 2026, this session. **Status:** reproducibility artifact; not canon.

---

## 1. The count divergence OAI flagged — resolved

OAI reported "needs-user-PDF 8 vs 2; verified-in-body 25 vs 31." **This is a stale-snapshot artifact, not a genuine inconsistency.** Both number-sets are real; they are the same ledger before and after one work session:

| Source | Total | verified-in-body | abstract-verified | record-only | needs-user-PDF | Snapshot |
|---|---|---|---|---|---|---|
| `aop_submission_README.md` | 52 | **25** | 14 | 5 | **8** | **STALE** (pre-Tier-1-PDF) |
| `aop_reference_punchlist.md` (**authoritative**) | 52 | **31** | 14 | 5 | **2** | **CURRENT** (16 Jul 04:26) |
| `aop_handoff_manifest.md` | (47 shown) | 31 | 14 | — *(omits record-only)* | 2 | current but **incomplete** (drops the 5 record-only) |

**The arithmetic reconciles exactly.** The current session added **+6 verified-in-body** from user-supplied Tier-1 PDFs (Francis & Wonham 1976, Bich et al., Frank 1995, Szathmáry & Maynard Smith companion, Hammerschmidt/Rainey 2014, Moreno & Mossio). Those same 6 PDFs resolved 6 of the 8 needs-user-PDF items:
- verified-in-body: 25 + 6 = **31** ✓
- needs-user-PDF: 8 − 6 = **2** ✓ (Ashby 1960, Parfit 1984 — both print-only)

**Action:** the README must be updated to the punchlist numbers (31 / 14 / 5 / 2), and the handoff manifest must add the 5 record-only category so its total reads 52, not 47. The **punchlist is the single authoritative reference ledger**; README and manifest are derived views and must be regenerated from it, never edited independently.

## 2. Reference-count structure — correcting my own Phase-0 note

The frozen-baseline note's "13 inline references, contiguous" was **the numeric-`[n]` subset only** and undercounts the true citation set. The canon uses a **mixed citation style**, verified this session:

| Measure | Count | Notes |
|---|---|---|
| Numeric `[n]` inline cites | 13 distinct (`[1]`–`[13]`, contiguous) | 43 total occurrences |
| Author-year bracket cites `[Author YEAR]` | 13 distinct (whitespace-normalized) | 26 total occurrences |
| **Reference-list entries** | **52** (authoritative, per punchlist) | 49 carry a `doi:`; 3 are books w/o DOI (Ashby, Parfit, Maynard Smith & Szathmáry book — the last sharing a row with its verified companion *Nature* paper) |

So the canon cites **~26 distinct works inline** (13 numeric + 13 author-year) drawn from a 52-entry backing reference list. *(An earlier draft of this table said "15 distinct / ~28" — that count double-counted `Ashby 1960` via a line-break whitespace variant; corrected here after normalization.)* **This inline-subset-vs-full-list gap is the true source of the manifest divergence** and must be stated explicitly in the rebuilt Data-Accessibility section, so a reviewer is not left computing "13 vs 52" as an inconsistency. The rebuilt manuscript should adopt **one** citation style (recommend numeric throughout for a Royal Society Interface Focus Perspective) to remove the ambiguity at source.

## 3. Version-string reconciliation

| Artifact | Version string it currently carries | Correct value | Action |
|---|---|---|---|
| Frozen canon title block | "Perspective · version 1.16 · compiled 15 July 2026" | v1.16 | ✓ correct — the frozen datum |
| Canon designation (`AOP_Canon_v1_0.md` pointer) | names v1.16 canonical | v1.16 | ✓ correct per changelog |
| Change log | v1.16, **no pending entries** | v1.16 | ✓ current, not stale |
| `aop_submission_README.md` | "condensed from the canon (v1.16)" but notes "Drive master still v1.14 — user action" | v1.16 | **STALE line** — the "Drive master still v1.14" note is obsolete; Drive master is v1.16. Fix in rebuild. |
| Manuscript blueprint | references "Drive placement of v1.15/v1.16 (user uploads)" | v1.16 | update to v1.17 target on rebuild |
| Rebuilt manuscript (this program) | → **v1.17** | v1.17 | new designation on completion of Phase 4 |

**One residual version-pointer defect:** the README still contains a "Drive master still v1.14 — user action" line, written before the v1.15/v1.16 uploads. It is factually wrong now (Drive master is v1.16, three copies) and must be removed in the rebuild.

## 4. Outstanding items requiring Ben

1. **Ashby, *Design for a Brain* (1960)** — print-only; `needs-user-PDF`. Non-load-bearing: the internal-model claim rests on Francis & Wonham 1976 (now verified-in-body); Ashby is the older name-of-record. Blocks only a direct quotation of Ashby's "ultrastability" definition, if one is wanted.
2. **Parfit, *Reasons and Persons* (1984), Part 3** — print-only; `needs-user-PDF`. A conceptual reference (personal-identity / no-further-fact), not empirical. Non-blocking for the science; blocks only a verbatim Parfit quotation.
3. **Maynard Smith & Szathmáry 1995 *book*** — book pages remain unread (`abstract`/record level); the companion *Nature* paper IS verified-in-body. Note honestly if any claim leans on the book text specifically.
4. **5 record-only references** — bibliographic metadata confirmed but body/abstract not read. **Not submission-ready under the charter standard.** Each must be upgraded to at least abstract-verified, or the claim it supports restated as unattributed / cut, before submission.

## 5. Reconciliation verdict

The P0-6 defect is **mechanical and now resolved at the level of the frozen baseline**: one frozen file, one authoritative ledger (the punchlist), a fully-reconciled count trail (25→31, 8→2), and a documented inline-vs-list citation structure. Three cheap mechanical actions remain (regenerate README + manifest from the punchlist; delete the stale "v1.14 Drive master" line; adopt one citation style in the rebuild) and four items wait on Ben (2 print books, the Maynard Smith book pages, the 5 record-only upgrades). None blocks the re-architecture from proceeding.
