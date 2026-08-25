# AOP Canon Change Set — v1.23 → v1.24 (tightening pass)

Issued by the execution seat (Cowork), 23 July 2026, for prime to verify by re-running.
**This output is delivered for verification; it is not self-blessed.**

Base: `AOP_CANON_MASTER_v1.23.md` — SHA-256 `352f8882f4dcb9c9a31ed4f3d02bb9d6de2892562505561105e1ac5404b7f4cf`, 217,359 bytes, confirmed before any edit.
Build: `AOP_CANON_MASTER_v1.24.md` — SHA-256 `3e64ff0ca93eee3165d53520651dfbbac063489df1ccfa87e3c8242f0dd421cf`, 218,602 bytes.

Five edited spans, four categories. Reverting all five reproduces the v1.23 base **byte-for-byte** (verified, hash matches). No claim, number, citation, grade, hedge, or scope word changed outside these spans.

---

## Edit 1 — [T1 masthead] remove proposal banner (base line 3)
**WHY:** Canonical masters (cf. `AOP_CANON_MASTER_v1.21.md`) carry no proposal banner; v1.21 goes title → blank → "Living review (Perspective)". Per Task 1, remove line 3 entirely.

**OLD** (line 3 + its trailing blank line, removed):
```
> **PROPOSED / NON-CANONICAL — Aster synthesis for Ben’s review.** This file does not replace `AOP_CANON_MASTER_v1.21.md`, makes no silent change to canon, and should be adopted only after the project’s normal independent check and Ben’s decision.
```
**NEW:** (removed — masthead now reads: `The Architecture of Persistence` / blank / `Living review (Perspective)`)

---

## Edit 2 — [T1 masthead] version token + compile date (base line 15 head)
**WHY:** Stamp from the residual v1.22 PROPOSED/NON-CANONICAL state to canonical v1.24 in v1.21 format; set compile date to today. Embedded version-history prose that follows is untouched (record).

**OLD:**
```
version 1.22 (PROPOSED / NON-CANONICAL) · compiled 21 July 2026
```
**NEW:**
```
version 1.24 · compiled 23 July 2026
```

---

## Edit 3 — [T2 fold-seam] §13, base line 775
**WHY:** E17 fold-scar: the sentence "This has now been done." is redundant with the earlier "That has now been done:" in the same passage. Drop the redundant sentence and smooth into "Run per edge…". The claim (per-edge mask on a well-posed two-module partition; aggregate mode stays sharp) is preserved verbatim in substance. This is the one duplicate removed by a Task-2 seam fix (acceptance criterion 4 exception); it carries no citation, number, or grade token.

**OLD:**
```
…what the account says is there. This has now been done. Run per edge on a coupled-Gaussian system…
```
**NEW:**
```
…what the account says is there. Run per edge on a coupled-Gaussian system…
```

---

## Edit 4 — [T3 annotate] v1.12 changelog entry (base line 889)
**WHY:** The v1.12 entry states Φ_MIP's individuation ordering is "robust across minimum-partition normalizations" flatly; v1.22 later scoped that robustness (to magnitude at a fixed partition). Add one annotating clause so a careful reader does not hit an apparent contradiction. The historical entry is annotated, not rewritten.

**OLD:**
```
…is the minimum-cut member of the integration-measure family, not a canonical Φ). This narrows the framework
```
**NEW:**
```
…is the minimum-cut member of the integration-measure family, not a canonical Φ — a robustness v1.22 later scoped to magnitude at a fixed partition). This narrows the framework
```

---

## Edit 5 — [T4 changelog] append v1.24 entry (after the v1.23 entry, end of file)
**WHY:** Record the canonicalization + tightening pass in house style (bold `**Version 1.24 (23 July 2026)**` token, plain prose, not a `###` header). States: no claim, number, citation, grade, or scope changed.

**NEW (appended):**
```
**Version 1.24 (23 July 2026)** canonicalizes the adopted v1.23 body as a prose/consistency tightening pass — no new science, and no claim, number, citation, grade, or scope changed. **(1) Masthead.** The residual v1.22 proposal stamp is retired: the proposal banner is removed and the version line is stamped to canonical v1.24 in the standing-master format (version token and compile date updated), matching `AOP_CANON_MASTER_v1.21.md`. The historical changelog entries are left byte-identical, including the v1.22 proposal-state record. **(2) Fold-seams.** Redundant phrasing left by successive folds is repaired without altering any claim; the §13 passage carrying a doubled “has now been done” is reduced to a single statement, its per-edge two-module mask result (the aggregate collective mode stays sharp) preserved verbatim in substance. A body-wide scan for other seams of this kind — doubled sentences, dangling “This/That” transitions, mid-sentence fold-inserts — surfaced none beyond it. **(3) Annotation.** The v1.12 changelog’s “robust across minimum-partition normalizations” carries a one-clause forward note that v1.22 later scoped that robustness to magnitude at a fixed partition, so the historical record no longer reads as contradicting the current scope; the entry is annotated, not rewritten. This pass exists to give the red team a clean document, not to pre-empt it. **Status: tightening only; prime to verify, then red-team-ready.**
```

---

## Flagged (not edited) — for prime / red team, not for this pass
- **Task-2 bounded discovery: no other same-category fold-scars found.** A body-wide scan (doubled "has/now been done"; exact duplicate substantive sentences; doubled 5-gram phrasing within a line; doubled words; dangling "This/That" transitions; typographic fusion scars) surfaced nothing beyond the §13/line-775 target. Recurring strings that are **not** scars and were left alone: "Code and data are deposited (see Data Accessibility)." (×4, per-figure notice); "[✓ read this session; ⚠ confirm DOI before final.]" (×2, reference tag); the line-56 ownership restatement ("the fraction of its own upkeep/maintenance a system performs on its own behalf", ×2 — deliberate definition-then-failed-measurement parallel, differently worded); line-739 "the saddle's unstable eigenvalue" (general claim then computed instance); line-976 title-vs-gloss repeat.
- **No substantive problems logged this pass.** Nothing in the scan read as a wrong claim, off number, or misapplied citation. (Substance is frozen by design.)
- **Carried before-final debt (unchanged, not re-flagged):** full-text reads still `~` (Maes 2020, Schnakenberg 1976, Bouchet–Reygner 2016, Oono–Paniconi 1998); ⚠ pagination/DOI confirms (DiFrisco 2018, Joyce 1994, Ashby 1960, Hoel 2016, Bialek–Nemenman–Tishby 2001, Pearl 1988, Hatano–Sasa / Speck–Seifert). Submission-gating, not tightening/red-team items.
