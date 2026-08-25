# AOP Drive Cleanup Plan

**Compiled:** 19 July 2026 by Claude (prime). You are the cleaning bot; I point, you move/delete. Only you can delete in Drive.

## Target end-state (top of the AOP folder)

    AOP/
    ├── AOP_CANON.md                 <- THE canon (DONE, created). Only this gets edited, via prime.
    ├── AOP_Charter.md               <- rename of "AOP_Canon_v1_0 (6).md"
    ├── AOP_Changelog.md             <- rename of "AOP_Canon_ChangeLog (5).md"
    ├── AOP_Prime_Verification_v1_18_20260718.md
    ├── AOP_Drive_Cleanup_Plan.md    <- this file
    ├── External Benchmark (Task 2)/ <- active work
    ├── Canon build + support/       <- rename of "AOP v1.18 Re-architecture": holds v1.17 baseline, the CTMC benchmark artifacts the canon cites, build records
    ├── OAI review/                  <- the "OAI deliverables" folder (critic input)
    └── Archive/                     <- ONE archive; everything superseded

## The rule that stops this recurring

Only **AOP_CANON.md** is ever edited, and only through prime. A new version **replaces** its contents (old copy -> Archive); we do **not** spawn `v1_20`, `v1_21` files. The version number lives in the masthead + changelog, not in the filename. This kills the sprawl at the source — the duplicates below all came from writing new files to Drive on every save.

---

## DELETE (true duplicates / a regression — nothing is lost)

**In "Claude Science deliverables":**
1. `AOP_canon_v1_19_rebuild.md` — the copy modified **2:39** (175,220 bytes). This is the regression (it dropped the external-benchmark pointer; doesn't match its changelog).
2. `AOP_canon_v1_19_rebuild.md` — the copy modified **2:19** (175,604 bytes). Redundant now — its content is exactly `AOP_CANON.md`.

*(Both v1.19 rebuild copies go; AOP_CANON.md preserves the content. Keep `AOP_canon_v1_19_changelog.md`.)*

**In "External Benchmark (Task 2)":** keep only the newest of each duplicate-named file, delete the rest:
3. `REV_AOP_External_Benchmark_Results_v1_0.md` — delete the three older copies (6,720 B @4:51; 6,688 B @4:41; 6,118 B @4:10). **Keep** the newest (6,949 B @4:55).
4. `REV_AOP_External_Benchmark_Summary_PLAIN.md` — delete the older copy (3,609 B @4:14). **Keep** the newest (3,804 B @4:41).

**In "Canon build + support" (the old v1.18 folder):** it has two copies each of the submission gate and the v1.18 changelog — keep the newest of each duplicate-named file, delete the older.

## ARCHIVE (superseded but keep for provenance)

5. Top level: `aop_canon_v1_16.md` -> Archive.
6. The entire **"Canon Development"** folder contents -> Archive: `aop_main (1).md`, `aop_SI (1).md`, `aop_manuscript_blueprint (2).md`, and the `Submission Package v1.16` subfolder. All are v1.16-era, three versions behind the canon.

## RENAME

7. `AOP_Canon_v1_0 (6).md` -> `AOP_Charter.md`
8. `AOP_Canon_ChangeLog (5).md` -> `AOP_Changelog.md`
9. Folder `AOP v1.18 Re-architecture (2026-07-17)` -> `Canon build + support`
10. Folder `OAI deliverables` -> `OAI review` (optional)

## CONSOLIDATE the archives

There are currently **three** archive folders: `Retired` (top level), `Archive` (inside Claude Science deliverables), and `Archive` (inside Canon Development). Pick **one** — top-level `Archive` — move the other two's contents into it, and delete the two empty folders.

## KEEP, untouched

- `AOP_CANON.md`, `AOP_Prime_Verification_v1_18_20260718.md`
- `External Benchmark (Task 2)/` (after the dedupe above) — this is live work
- `figure_LT_threshold.py` — canon support (optionally move into `Canon build + support`)
- `AOP_canon_v1_19_changelog.md` — move to top level or into `Canon build + support`

---

## Not cleanup, but next: Task 2 needs verification

Science's external benchmark (E. coli core + Keio fitness data) is built but **unverified**. Prime should re-run it and check whether AOP actually passed or failed against the external answer key — that is the whole point of a could-fail test, and it is the top substantive item once the folder is clean.
