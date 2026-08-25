# Task D — PRE-REGISTRATION (frozen before the first run)

**Builder proposal — Prime verifies; Ben decides. Touches no canon master.**
**From:** Claude Science (builder), AOP · **Frozen:** 22 July 2026, before executing any attribution-convention sweep.

> This note is a governance gate. It is written and deposited to Drive **before** the attribution-convention computations are run. A gate that has seen its results is not a gate. My predictions below are stated so they can be wrong; the results memo (Task D, separate file) will report against them verbatim.

## What is being computed

On the equal-strength K4, S={0,1}, load edge (0,1), spectator edge (2,3), pinned Laplacian scramble (Task A): for each attribution convention below, does the **load-vs-spectator merge** (the loss of resolvable discrimination) have a **finite ceiling a\*** in coupling strength, and if so approximately where?

Conventions to sweep:
1. Full unmatched min–max coalition envelope (the deposited interval: `lo_load > hi_spec`).
2. Bounded coalition cardinality |C| ≤ 0, 1, 2, 3, 4.
3. Random sparse sampling at 4 / 8 / 16 coalitions.
4. Matched-context comparison (load and spectator scored in the *same* coalition context).
5. Uniform-coalition mean (equal weight over all contexts).
6. True Shapley value (permutation-weighted mean).

## Predictions (what I expect, stated to be falsifiable)

**Mechanistic reasoning I am reasoning from (not results):** the deposited existential result is forced because the *envelope* compares the load's best-case (max) context against the spectator's worst-case (min) context — an unmatched min–max comparison that exaggerates separation and, symmetrically, can force a merge when the envelope's endpoints cross. Means (Shapley, uniform) and matched comparisons remove that unmatched asymmetry, so they should behave differently from the envelope.

| # | Convention | Predict finite ceiling a\*? | Reasoning |
|---|---|:--:|---|
| 1 | Full min–max envelope | **YES** | This is the deposited a\* = (3+√13)/2 ≈ 3.303; the envelope endpoints cross. |
| 2a | \|C\| ≤ 0 (empty context only) | **NO** | Spectator empty-context marginal is exactly 0 (Task A); load is O(a) > 0 always → load ranked above spectator at every a, never merges. |
| 2b | \|C\| ≤ 1 | **NO** | Still dominated by low-order contexts where spectator ≈ 0; separation persists. |
| 2c | \|C\| ≤ 2 | **NO (or very high)** | Work order states the ceiling vanishes under \|C\| ≤ 2. I expect no finite ceiling in [0,8]. |
| 2d | \|C\| ≤ 3 | **YES** | Work order states the ceiling exists at cardinality ≥ 3. Expect a\* to reappear. |
| 2e | \|C\| ≤ 4 | **YES** | Same; ceiling present, near the full-envelope value. |
| 3 | Sparse sampling 4/8/16 | **UNSTABLE** | Sampled envelopes are noisy estimators; I expect the ceiling to appear or not depending on which coalitions are drawn — directional at best, and I flag it as estimated, not analytic. |
| 4 | Matched-context | **NO** | Comparing both edges in the same context removes the unmatched asymmetry; load stays above spectator everywhere. |
| 5 | Uniform mean | **NO** | The work order states mean attribution gives "load stays ranked above spectator everywhere, no finite ceiling." |
| 6 | True Shapley | **NO** | Shapley is a (permutation-weighted) mean; same reasoning as #5. The deposited run already shows Shapley-mean separation persisting past a\* (load 0.874 vs spec 0.103 at a=8). |

**Summary expectation:** a finite ceiling exists **only** under the full min–max envelope and under bounded cardinality **≥ 3**; it **vanishes** under |C| ≤ 2, matched-context, uniform mean, and true Shapley. Sparse sampling is unstable/estimated.

## What would falsify this

- If the **mean or Shapley** conventions show a finite ceiling in [0,8] → my core claim (that the ceiling is an artifact of the unmatched min–max envelope) is **wrong**, and the ceiling is a more robust feature than I expect.
- If **|C| ≤ 2** shows a clean finite ceiling → the work order's cardinality claim and my prediction are both wrong.
- If **matched-context** shows a ceiling → the "unmatched asymmetry" mechanism I posit is not the driver.

Any of these would mean the convention-dependence story needs restating, not just tabulating.

## Grading commitment

Per the three-category scheme: a convention whose ceiling-status I have **pre-declared here** and which a coupling sweep can genuinely reverse is a **contingent result** for that convention. A convention that cannot flip within the class (e.g. |C| ≤ 0, where the spectator is identically zero) is an **identity/theorem demonstration** and earns no evidential weight. I will label each row accordingly in the results memo.

*Frozen before running. Syntactic layer only. Prime verifies; Ben decides.*