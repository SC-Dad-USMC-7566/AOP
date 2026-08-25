# Builder Tasking — Fix and Re-run the External Benchmark

**Compiled:** 19 July 2026 by Claude (prime), for Claude Science (builder). Non-canonical.
**Companion:** `AOP_Prime_Verification_ExternalBenchmark_20260719.md` (read first).

---

**Governance reminder:** you're the builder — you propose, prime verifies by independent re-run, ChatGPT attacks, Ben decides. Everything goes in the AOP Drive folder. One file per artifact — deliver the final and say if you revise, so the old copy can be pruned. You do **not** touch the canon; canon edits (including the §11b update this implies) are prime's job.

## What prime found (so you're working from the same facts)

- Your numbers don't fully reproduce. The benchmark isn't deterministic — FBA has non-unique optimal flux vectors, so the rival's coupling-strength and the T4 Spearman change run to run. Prime's repeated runs gave T4 = 0.524, 0.537, 0.551.
- The answer key is ~half circular: of 11 "essential" positives, only 5 come from the experimental assay; the other 6 are model-labeled (absent-from-assay AND FBA-lethal) and then scored by the same FBA. That inflates T1 from an honest **0.67** (external-only) to the headline **0.85**.
- T4 is **falsified**, not partial: the reproducible Spearman is ~0.53 (pFBA 0.528), over your pre-registered 0.5 falsification line. The 0.482 was one non-reproducible draw.

## Three fixes — do all three, then re-run against the same frozen model + key

1. **Make it deterministic.** Compute the WT flux vector with parsimonious FBA (`cobra.flux_analysis.pfba`) or an explicit fixed tie-break, so coupling-strength and the T4 Spearman are reproducible point values. State the method.

2. **De-circularize the labels.** Score T1 and T3 on the **external-experimental labels only** (the 5 assay-based positives) as the primary result. You may report the mixed-label version alongside, but the external-only number leads. Note the small external positive class (n=5) as a scope limitation of the *core* model.

3. **Re-report honestly.** Lead with **T2** — the 13 real synthetic-lethal isozyme pairs the single-axis rival can't see; that's the genuine external win. Report T1/T3 at their true (weaker) strength. State **T4 as falsified**: on real metabolism, structural strength and viability-importance are positively correlated (~0.53), so the toy model's "strength ⊥ viability" dissociation does not generalize. Report the falsification plainly in the headline — a pre-registered failure that fires is a valuable result, not something to soften.

## Deliverables (in the Task 2 folder, one copy each)

- fixed `aop_external_benchmark.py`
- regenerated `external_benchmark_results.json`
- updated results doc
- a one-line note of what changed from v1.0

Do **not** edit the frozen prereg — it stands as the pre-commitment you're being scored against. Prime re-runs your fixed code and re-verifies before anything reaches the canon.
