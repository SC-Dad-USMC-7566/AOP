# Work Order — AOP canon v1.23 → v1.24 (tightening pass)

**Issued 23 July 2026 by the chat seat (prime), for the execution seat (Cowork).**
Cowork builds v1.24. Prime checks it by re-running, not reading over. Then the whole document goes to the
outside critic (OAI) as one. Nobody grades their own homework: **do not bless your own output — deliver it
for prime to verify.**

This is a **prose/consistency tightening pass only.** Substance is frozen on purpose, so the red team hits
the real claims and not seam-scarring. If an edit you want to make touches anything on the freeze list
below, **stop and flag it for prime** — do not make it silently.

---

## Startup (fill and confirm before working)
```
Startup check — [date]
[ ] AOP Charter — v1.2
[ ] AOP Canon (base for this pass) — v1.23 (see fingerprint below; must match)
[ ] AOP → Ladder bridge memo — n/a (this pass does not touch the Ladder connection)
Drive connector: [on/off]
```

## Base input (build from this exact byte-image — confirm the hash)
- **File:** `AOP_CANON_MASTER_v1.23.md` (the R1+R2-adopted body; place on Drive first if not already there).
- **SHA-256:** `352f8882f4dcb9c9a31ed4f3d02bb9d6de2892562505561105e1ac5404b7f4cf`
- **Size:** 217,359 bytes · 994 lines.
- If your base does not hash to this, **stop** — you have the wrong base. Do not proceed on v1.22 or any
  other version.
- **Masthead-format reference:** the live canonical master `AOP_CANON_MASTER_v1.21.md`
  (id `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`) — read its masthead to see how a *canonical* (non-proposed)
  master is stamped, and match that treatment in Task 1.

---

## Objective (one line)
Produce a clean canonical **v1.24** master by (1) stamping the masthead from "v1.22 PROPOSED / NON-CANONICAL"
to canonical v1.24, and (2) repairing prose fold-scars and one flagged cosmetic — **without changing any
claim, number, citation, grade, hedge, or scope word.**

---

## Scope — the ONLY categories of change permitted

**Task 1 — Designation / masthead (canonicalize).**
- Update the two masthead stamps to **canonical v1.24**, matching the format of `AOP_CANON_MASTER_v1.21.md`:
  - **Line 3** — the `> **PROPOSED / NON-CANONICAL — Aster synthesis for Ben's review.** …` banner. If v1.21
    carries no equivalent proposal banner, remove line 3 entirely; if it carries a canonical masthead line,
    match it.
  - **Line 15** — the "version line" beginning `Living review (Perspective) · version 1.22 (PROPOSED /
    NON-CANONICAL) · compiled 21 July 2026 · …`. Set the version token to **1.24**, remove the
    "(PROPOSED / NON-CANONICAL)" qualifier, and update the compile date to today. **Do not touch the
    embedded version-history prose that follows on that line** except the single "version 1.22 (PROPOSED /
    NON-CANONICAL)" token at its head — the historical summaries are records.
- **TRAP — do not touch the third occurrence.** `PROPOSED / NON-CANONICAL` also appears inside the **v1.22
  changelog entry** ("**Version 1.22 (PROPOSED / NON-CANONICAL; 21 July 2026)** is a corrective
  consolidation…"). That is the historical record of what v1.22 was and **must stay byte-identical.**

**Task 2 — Fold-seam repair (prose only).**
Successive folds have left redundant/doubled phrasing and orphaned transitions. Remove the redundancy and
restore flow **without altering any claim.**
- **Required target (known):** §13 passage (line 775) contains a doubled "has now been done." The text runs
  "…That has now been done: the mask is computed on the Figure DM ring … A clean single number would hide
  exactly what the account says is there. **This has now been done. Run per edge** on a coupled-Gaussian
  system with a well-posed two-module part-partition, the scramble-and-rerun mask shows…". The second
  "This has now been done." is an E17 fold-scar redundant with the earlier "That has now been done:". Repair
  the seam (e.g., drop the redundant sentence and smooth into "Run per edge…") so the passage reads as one
  clean statement. **The claim — mask computed per edge on a well-posed two-module partition, aggregate mode
  stays sharp — must be preserved verbatim in substance.**
- **Bounded discovery (same category only):** scan the body for other fold-scars *of this kind* — doubled
  "has/now been done", repeated sentences, dangling "This/That" transitions, a fold-insert glued mid-sentence
  onto the prior one. Propose each as a Task-2 edit with a one-line justification. If you are unsure whether
  something is a fold-scar or load-bearing repetition, **flag it, don't edit it.**

**Task 3 — One flagged cosmetic (annotate, do not rewrite).**
- The **v1.12 changelog entry** states Φ_MIP is "robust across minimum-partition normalizations" flatly — a
  claim v1.22 later scoped (to magnitude at a fixed partition). It is historical, so it is not wrong, but a
  careful reader hits an apparent contradiction. Add **one annotating clause** (e.g., "— scoped in v1.22 to
  magnitude at a fixed partition") to that historical entry. **Do not rewrite the entry; annotate only.**

**Task 4 — Add the v1.24 changelog entry.**
- Append a v1.24 entry in house style (bold version token `**Version 1.24 (23 July 2026)**` then plain
  prose, matching the existing entries — not a `###` header). It should state: canonicalized from the
  adopted v1.23; a tightening pass only (masthead stamped canonical; fold-seams repaired; v1.12 normalization
  claim annotated); **no claim, number, citation, grade, or scope changed.** Draft it; prime will check it.

---

## Freeze list — NON-NEGOTIABLE. If a "tightening" would touch any of these, STOP and flag for prime.
- Any **graded claim** or the grade word attached to it: SETTLED / SYNTHESIS / FRONTIER / SPECULATIVE /
  UNKNOWN / DEFECT.
- Any **hedge or scope word**: "not established", "open", "conditional", "necessary condition", "does not
  bind", "feasibility", "out of scope", "frontier", "synthesis", "settled", "retracted", "suspended", etc.
- Any **number, quantity, or symbol value**: correlations, VIF/λ terms, μ₊(A), ξ₁=6.897, ~287×, ~5.7×,
  Spearman −0.67, b-values, nats, dates inside historical entries, etc.
- Any **citation** — no add, remove, reorder, or reword of `[Author YEAR]` / venue / DOI content.
- The **R1 and R2 text** just folded (the §11b header "The dissociation a one-axis reading inverts." and the
  §13 "It is worth being exact about the kind of exposure…" block). Frozen.
- The **abstract's claim content**, any **section that carries a claim**, any **figure/table value**, and the
  historical **changelog entries** (annotation in Task 3 excepted; the v1.22 "(PROPOSED / NON-CANONICAL)"
  token excepted per Task 1's trap note).
- **No merging or splitting** of claim-bearing sections or paragraphs beyond the local seam repair in Task 2.

---

## Deliverables (all three)
1. **Change set** — `AOP_Canon_ChangeSet_v1.23_to_v1.24.md`: verbatim **OLD → NEW** for every edit, each
   tagged `[T1 masthead | T2 fold-seam | T3 annotate | T4 changelog]` with a one-line WHY. Small file — fine
   to write to Drive (Canon Development, `1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`) via base64Content.
2. **Built body** — `AOP_CANON_MASTER_v1.24.md`: deliver **locally via present_files for manual placement.**
   **Do NOT** re-upload the ~200k master via create_file (transcription-corruption risk on a file that size).
3. **Verification note** — state: the base SHA-256 you built from (must equal the fingerprint above); edit
   count by category; confirmation that **reverting all your edits reproduces the v1.23 base byte-for-byte
   outside the intended spans**; and a list of anything you **flagged rather than edited.**

---

## Acceptance criteria (what prime will run before red team — build to this bar)
1. **Base match** — your build hashes from the v1.23 fingerprint; wrong base = reject.
2. **Every edit mapped** — each change is in the change set, verbatim, matches the body exactly once, and is
   prose-only.
3. **Clean diff** — reverting all edits reproduces the v1.23 base byte-for-byte except the intended spans
   (masthead lines, the seam-repair spans, the v1.12 annotation, the appended v1.24 changelog). Anything else
   moved = reject.
4. **Invariant multiset** — the set of citations, the set of numeric tokens, and the set of grade/scope words
   is **unchanged** between v1.23 and v1.24, with the sole permitted exception of a duplicate removed by a
   Task-2 seam fix (which must be individually justified in the change set). Any other delta = reject.
5. **Masthead** — reads canonical v1.24 in the v1.21 format; the v1.22 historical changelog entry is
   byte-identical; the v1.24 changelog entry is present and accurate.
6. **Encoding** — UTF-8 clean, no replacement chars; fragile tokens intact (Φ_MIP, Ptaszyński, R★, μ₊(A),
   ξ₁=6.897, §-refs).

---

## Notes
- **This pass is frozen on substance by design.** Its value is a cleaner document for the red team to attack —
  not to pre-empt the red team. Resist the urge to "improve" a claim; that's the critic's job next.
- If the scan surfaces something that looks like a real substantive problem (not a prose scar) — a claim that
  reads wrong, a number that looks off, a citation that seems misapplied — **do not fix it here.** Log it as a
  flag for prime / the red team. Substantive changes do not belong in a tightening pass.
- Carried before-final debt (out of scope here, listed so you don't re-flag it): full-text reads still `~`
  (Maes 2020, Schnakenberg 1976, Bouchet–Reygner 2016, Oono–Paniconi 1998); ⚠ pagination/DOI confirms
  (DiFrisco 2018, Joyce 1994, Ashby 1960, Hoel 2016, Bialek–Nemenman–Tishby 2001, Pearl 1988, Hatano–Sasa /
  Speck–Seifert). These are submission-gating, not tightening-pass or red-team items.
