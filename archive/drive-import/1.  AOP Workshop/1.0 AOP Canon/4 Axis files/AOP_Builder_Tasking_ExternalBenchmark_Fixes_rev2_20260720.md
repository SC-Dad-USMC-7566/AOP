# Builder Tasking — Fix and Re-run the External Benchmark (rev. 2)

**Compiled:** 19 July 2026 by Claude (prime), for Claude Science (builder). Non-canonical.
**Revised:** 20 July 2026 — adds the **T2 specificity control** (fourth task) after the OAI critic's
Q1 and prime's concurrence. Supersedes `AOP_Builder_Tasking_ExternalBenchmark_Fixes_20260719.md`
(prune the old copy).
**Companion:** `AOP_Prime_Verification_ExternalBenchmark_20260719.md` (read first).

---

**Governance reminder:** you're the builder — you propose, prime verifies by independent re-run,
ChatGPT attacks, Ben decides. Everything goes in the AOP Drive folder. One file per artifact —
deliver the final and say if you revise, so the old copy can be pruned. You do **not** touch the
canon; canon edits (including the §11b update this implies) are prime's job.

## What prime found (so you're working from the same facts)

- Your numbers don't fully reproduce. The benchmark isn't deterministic — FBA has non-unique
  optimal flux vectors, so the rival's coupling-strength and the T4 Spearman change run to run.
  Prime's repeated runs gave T4 = 0.524, 0.537, 0.551.
- The answer key is ~half circular: of 11 "essential" positives, only 5 come from the experimental
  assay; the other 6 are model-labeled (absent-from-assay AND FBA-lethal) and then scored by the
  same FBA. That inflates T1 from an honest **0.67** (external-only) to the headline **0.85**.
- T4 is **falsified**, not partial: the reproducible Spearman is ~0.53 (pFBA 0.528), over your
  pre-registered 0.5 falsification line. The 0.482 was one non-reproducible draw.

## Three fixes — do all three, then re-run against the same frozen model + key

1. **Make it deterministic.** Compute the WT flux vector with parsimonious FBA
   (`cobra.flux_analysis.pfba`) or an explicit fixed tie-break, so coupling-strength and the T4
   Spearman are reproducible point values. State the method.

2. **De-circularize the labels.** Score T1 and T3 on the **external-experimental labels only** (the
   5 assay-based positives) as the primary result. You may report the mixed-label version
   alongside, but the external-only number leads. Note the small external positive class (n=5) as a
   scope limitation of the *core* model.

3. **Re-report honestly.** Lead with **T2** — the 13 real synthetic-lethal isozyme pairs the
   single-axis rival can't see; that's the genuine external win. Report T1/T3 at their true
   (weaker) strength. State **T4 as falsified**: on real metabolism, structural strength and
   viability-importance are positively correlated (~0.53), so the toy model's "strength ⊥
   viability" dissociation does not generalize. Report the falsification plainly in the headline — a
   pre-registered failure that fires is a valuable result, not something to soften.

## Deliverables for the three fixes (in the Task 2 folder, one copy each)

- fixed `aop_external_benchmark.py`
- regenerated `external_benchmark_results.json`
- updated results doc
- a one-line note of what changed from v1.0

Do **not** edit the frozen prereg — it stands as the pre-commitment you're being scored against.
Prime re-runs your fixed code and re-verifies before anything reaches the canon.

---

## Fourth task — the T2 specificity control (do this AFTER the three fixes; pre-register before running)

**Why this is the highest-value next test.** T2 is the one genuine external win — 13 synthetic-lethal
isozyme pairs the single-axis rival can't see. But "the single-axis rival can't see them" is not the
same as "AOP is needed to see them." The referee-killer question — raised by the OAI critic, and
prime concurs the original verification memo under-weighted it — is: **does an ordinary
double-knockout FBA synthetic-lethal screen, with no AOP coalition/viability machinery at all,
already recover the same 13 pairs?** If it does, T2 is standard double-KO SL detection wearing AOP
vocabulary, and it cannot be reported as an AOP-specific result. This control decides that, and it
doubles as a direct measurement of how much of T2 is inherited FBA competence (the critic's Q4).

**Design.**
1. On the **same frozen core model**, run a plain double-knockout FBA synthetic-lethal screen with
   **no AOP layer**. For each reaction/gene pair (i,j): if each single KO is individually viable
   (growth > τ) but the double KO is lethal (growth ≤ τ), flag (i,j) as synthetic-lethal. Use pFBA
   + the same fixed tie-break as Fix 1 so the screen is deterministic. State τ.
2. Take the **13 AOP coalition pairs** as the comparison set.
3. Compute the overlap: how many of the 13 AOP pairs the plain screen also flags, and how many
   synthetic-lethal pairs the plain screen finds that AOP does *not* surface. Report the two sets
   and their intersection explicitly.

**Pre-registered could-fail criterion (freeze before running).**
- If the plain double-KO screen recovers **all 13** AOP pairs (AOP ⊆ plain screen) and AOP surfaces
  nothing the plain screen misses, then **T2's AOP-specificity is NOT established** — report T2 as
  "AOP reproduces standard synthetic-lethal detection," not as a unique AOP win.
- AOP-specificity is supported **only** if the coalition/viability layer recovers biologically
  meaningful structure the plain screen misses, or organizes/ranks the pairs in a way the plain
  screen structurally cannot — and that difference must be **stated concretely** (which pairs, what
  the plain screen does with them), not asserted.
- Report the overlap either way. A control that dissolves the win is a valuable result, not
  something to hide — same discipline as T4.

**Deliverables (Task 2 folder, one copy each).**
- `aop_T2_doubleKO_control.py` — the plain screen + overlap computation
- `T2_control_results.json` — the two sets and their intersection
- a short **prereg note frozen before the run** stating the criterion above, plus a one-paragraph
  honest readout after
- this control gets its **own** small prereg; do not edit the frozen benchmark prereg.

Prime re-runs your control and re-verifies the overlap before **any** T2 claim — AOP-specific or
not — reaches the canon.

---

**Sequencing.** Fixes 1–3 first (they harden what exists); then the T2 control (it tests whether the
one win survives). Both live in the Task 2 folder. Prime verifies each independently; Ben decides
what reaches canon. Downstream, noted but **not** tasked here: a genome-scale reconstruction
(iML1515) is a "before strong claims" step, not a prerequisite for reporting the current honest
mixed result.
