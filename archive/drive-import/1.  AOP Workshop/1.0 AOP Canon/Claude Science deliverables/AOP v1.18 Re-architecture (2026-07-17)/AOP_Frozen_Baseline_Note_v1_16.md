# AOP v1.16 — Frozen Source Baseline

> **⚠ BASELINE REBASED TO v1.17 — 17 July 2026 (read this first).**
> After this note was written, a baseline conflict surfaced: the Drive copy frozen below as "v1.16" (MD5 `241153bc…`, masthead *"version 1.16 · compiled 15 July"*) carries the **old** persistence-primitive framing, but a more-advanced **local** canon artifact (`8128569c`, latest version `8b381622-e566-448b-9d20-8f83e4908f35`, filename `aop_canon_v1_16.md` but internal masthead **"version 1.17 · compiled 17 July"**) carries the **lifetime-primitive spine change** — the 5.7× lifetime-vs-occupancy dissociation and the two guardrails (non-fungibility; description≠derivation). Evidence: the frozen Drive v1.16 has **0** hits for `lifetime`/`first-passage`/`occupancy`/`5.7`/`non-fungible`/`guardrail`; the local v1.17 has 21/4/14/3/1/2 respectively, and the changelog's Pending entry tracks v1.17 as the working state.
>
> **Ben's ruling:** rebase the re-architecture onto **local v1.17** (no scientific regression), keep it as the baseline, fold the OAI panel/tuple/labeling re-architecture on top, and version the rebuild **v1.18**. The new frozen baseline is **`FROZEN_aop_canon_v1_17.md`** (artifact `a40a51b7-081e-413a-8571-efc89e826141`, version `c7479fbc-8e50-4ed0-9730-790eb958ef0f`, MD5 `26afc8a8e938f2f052e388aea9039844`, 24,182 words, 20 section headers = the same §1–§13/§4a/§9a/§11a skeleton as v1.16).
>
> **P0 re-check against v1.17 text (done):** every OAI P0 target survives the rebase with the same signatures — P0-1 rest-frame present (4 hits), P0-3 "choice-free" already absent (0 hits, stale), P0-4 "own viability" present incl. abstract subtitle (15 hits) with "ownership-free/no ownership" preserved as the correct refusal (10 hits), P0-2 Drive "free-energy throughput" (1) + Boundary "mutual information" (8) present, P0-5 fused status column present. The v1.16 designation below is retained as the record of *why* the rebase was needed; all downstream work targets `FROZEN_aop_canon_v1_17.md`.

---

**Purpose.** OAI Remediation Master Plan, Phase 0, exit-gate requirement: *"one file is the frozen source baseline."* This note designates that file and records the evidence for the choice, so that every downstream step of the maximal re-architecture (benchmark, panels, manuscript rebuild, rival adjudication) is written against one unambiguous datum and cannot silently drift onto a different copy.

**Compiled:** 17 July 2026, this session. **Status:** governance/reproducibility artifact — not canon, records no scientific claim.

---

## The designated frozen baseline

| Field | Value |
|---|---|
| **Frozen file** | `aop_canon_v1_16 (2).md` |
| **Drive file ID** | `1cm52xYY4ig-fMovTqVLhWxx-KmBuWgC-` |
| **Drive modified time** | 2026-07-15T19:03:43Z |
| **MD5 (decoded UTF-8 text)** | `241153bc85d3e457cfa37105a0eac62b` |
| **Size** | 154,655 chars · ~22,776 words · 853 lines |
| **Local frozen copy** | `FROZEN_aop_canon_v1_16.md` (this session's workspace artifact) |
| **Designation** | This is the single source of truth for the v1.17 rebuild. |

## Why this copy and not the other two

Drive holds **three** files named as v1.16 — this ambiguity is itself an instance of the reproducibility defect OAI flagged (P0-6). They are **not identical**; I diffed all three rather than assume the newest-by-name:

| File | Words | MD5 (12) | Relation |
|---|---|---|---|
| `aop_canon_v1_16.md` | 22,449 | `d3106d6908d7` | **Internally inconsistent** — body carries §9a but its reference list is **missing the 6 references §9a cites** (Michod 2007, Queller & Strassmann 2009, Grosberg & Strathmann 2007, Frank 1995, Hammerschmidt/Rainey 2014, Aktipis 2015). |
| `aop_canon_v1_16 (1).md` | 22,773 | `813bdbc6ffb4` | Adds the 6 missing §9a references. Body/reference-list now agree. |
| `aop_canon_v1_16 (2).md` | 22,776 | `241153bc85d3` | **← FROZEN.** `(1)` + one reference-year correction (Bich et al. 2015 → 2016, fuller citation `Biology & Philosophy 31, 237–265`). |

`(2)` is the only copy whose body and reference list are mutually consistent **and** carries the latest correction. `(1)` vs `(2)` differ by exactly one line (the Bich year); base vs `(2)` differ by 12 lines (the 6 refs + the Bich line + a version-note wording tweak). Chosen on **completeness + internal consistency**, not on filename recency.

**Action for cleanup (needs Ben):** the two superseded copies (`aop_canon_v1_16.md`, `aop_canon_v1_16 (1).md`) should be moved to a review archive or renamed, so no future session picks the internally-inconsistent base copy by mistake. Per Drive-hygiene rule 3 in the OAI naming convention: revisions should increment an explicit version, not rely on `(1)`/`(2)` suffixes.

## Verified structural facts (the authoritative counts)

Established by direct inspection of the frozen text, decoded from Drive this session (Drive export escapes markdown: headers are `\#\#\#`, cites are `\[n\]` — raw counts must account for this):

- **Citation style is mixed** (see the separate Version & Count Reconciliation for the full breakdown): **13 distinct numeric `[n]` cites** (`[1]`–`[13]`, contiguous) **plus 13 distinct author-year bracket cites** (whitespace-normalized) = **~26 distinct works cited inline**. An earlier draft of this note said "13 inline references" (numeric subset only), then "15 author-year / ~28 total" (which double-counted `Ashby 1960` via a line-break variant); both are corrected here.
- **Reference-list entries: 52** (authoritative, per `aop_reference_punchlist.md`): 49 carry a `doi:`; 3 are books without DOI (Ashby, Parfit, Maynard Smith & Szathmáry book). The gap between ~26 cited-inline and 52 listed, and the mixed citation style, are the true source of the README-vs-manifest count divergence OAI flagged — reconciled in the companion document and to be stated explicitly in the rebuild's Data-Accessibility section.
- **Sections present (full header inventory, by direct `\#\#\#`-header extraction):** §1 Introduction and scope · §2 The object: four dimensions as differences · §3 Two layers: syntactic correlation and semantic mask · §4 The coupling graph and its classification · §4a Diachronic individuation · §5 Laws versus quantities · §6 The two-axis view · *(unnumbered) A resolvability limit: the mask blurs as Integration rises* · §7 The observer, located · §8 What can make a boundary: screenability · §9 Present-tense viability · §9a Individuality at the collective scale · §10 The domain and its edge: binding, not rest mass · §11 Five worked cases · §11a The living threshold · §12 Status of claims · §13 Limitations and outlook · *(unnumbered) Data Accessibility · References*. **16 numbered sections** (1,2,3,4,4a,5,6,7,8,9,9a,10,11,11a,12,13) plus title block, the resolvability-limit interlude, Data Accessibility, and References. §9a is the v1.15→v1.16 addition; the changelog shows **no pending entries** after it, confirming v1.16 is the current, non-stale designation. *(An earlier draft of this list was derived from inline "§N" back-references, not header extraction — it wrongly added a bare "1", omitted §2 and §8, and is corrected here.)*
- **Genre line (title block):** "Perspective · version 1.16 · compiled 15 July 2026 · not peer reviewed." The venue commitment is already stated in the frozen text — the rebuild inherits it, it does not introduce it.

## Freeze discipline for downstream steps

1. All rebuild steps read `FROZEN_aop_canon_v1_16.md` (MD5 `241153bc…`), never a Drive copy directly, so the source cannot move mid-rebuild.
2. Every movement from this baseline to v1.17 gets a change-log entry (Phase 4, step "Log every change; no silent migration").
3. The 2 print-only books OAI flags as needing acquisition — **Ashby, *Design for a Brain* (1960)** and **Parfit, *Reasons and Persons* (1984)** — are recorded here as the only reference items that cannot be verified against a retrievable primary source this session. They gate any [S]-graded claim that leans on them; see the issue registry.
