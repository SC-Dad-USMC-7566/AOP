# AOP Semantic-Mask Salvage Diagnostic — Adversarial Review

**Reviewer:** Aster / external red-team  
**Date:** 21 July 2026  
**Status:** Non-canonical review; no source or canon edits made  
**Verdict:** **RED on the stated salvageability verdict**; **YELLOW on a narrower edge-ablation game result**

## Sources actually inspected

- `mask_salvage.py` — Drive id `1GPcrRSySofAD_yZeCcPkpB_S53IOkrC_`; executed locally and independently probed.
- `AOP_MaskSalvage_Diagnostic_20260721.md` — Drive id `1pS-BhdfUrPsqB7BXbcCGVdJHh9ZGXYvq`.
- `AOP_CANON_MASTER_v1.21.md` — Drive id `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`; current v1.21 text inspected, especially §3 and the resolvability-limit discussion. Canon was not edited.
- Kolchinsky & Wolpert (2018), primary paper: https://doi.org/10.1098/rsfs.2018.0041 (formal intervention and viability construction checked against the paper).

## 1. Executive Summary

The deposited script reproduces its printed tables, but the conclusion

> “the mask’s well-defined and informative regions overlap non-trivially, bounded above by a redundancy ceiling a*≈3.4”

does **not** survive as a semantic-mask verdict.

What survives is only this narrower fact:

> In one selected static-Gaussian K4 edge-ablation cooperative game, with the selected viability subset `S={0,1}`, the full min–max marginal envelope of edge `(0,1)` lies above that of edge `(2,3)` for `a < 3.3027756`.

That fact is analytic and reproducible. It is not enough to establish that the AOP semantic mask is salvageable, and its crossing is not shown to be a redundancy ceiling in the Kolchinsky–Wolpert sense.

The strongest defects are:

1. **The claimed ceiling is a cross-context-envelope artifact.** Above the reported `a*`, the load edge still outranks the spectator in every matched scramble context tested, through `a=100`. The envelopes overlap only because the load minimum and spectator maximum are taken under mutually incompatible background coalitions.
2. **Model 3’s “semantic” ranking is encoded by `S`.** Once `S={0,1}` is declared, the edge classes are readable from endpoint membership: 2, 1, or 0 endpoints in `S`. Equal coupling strength removes one syntactic cue but does not turn recovery of an input label into independent semantic content.
3. **The verdict is not stable across declared viability sets.** On the same equal-strength K4, the interval crossing is `a*=1.6180` for `|S|=1`, `3.3028` for `|S|=2`, and `0.6404` for `|S|=3`; for `S=all nodes`, all edges are symmetry-equivalent and no load/spectator discrimination exists.
4. **The Kolchinsky–Wolpert grounding is not the operation implemented.** KW scramble system–environment mutual information in an initial distribution, or environment→system transfer entropy in dynamics, then measure viability after evolution to a later time. The script deletes an internal precision-matrix edge (`θ_e→0`) in a static Gaussian and reads the same-time marginal negentropy. This may be a legitimate AOP-inspired intervention, but it is an extension, not “the KW construction.” Canon v1.21 itself states that internal-edge use is an extension.
5. **The reported O-information is not computed on declared `S`, despite the method saying it is.** Model 3 reports whole-K4 Ω. For declared `S={0,1}`, O-information is identically zero. The claimed “Ω≈0.81 redundancy ceiling on the declared set” is therefore false as written.
6. **Threshold and implementation inconsistencies remain.** `rel_width_tol=0.5` is uncalibrated and materially controls how far the “well-defined” band extends; the 0.02 informativeness bar is dead code for the final verdict; and the printed “Shapley” mean is not a Shapley value.

Accordingly: **RED.** No canon movement should be based on this diagnostic. A repaired, explicitly AOP-specific edge-ablation study remains worth doing (**YELLOW research direction**).

## 2. Critique and Reproduced Defects

### 2.1 The `a*` ceiling compares incompatible contexts

For each edge, the diagnostic takes the minimum and maximum marginal viability drop over all coalitions of other already-scrambled edges. It then declares the semantic classes unresolved when the two separately constructed envelopes overlap.

At `a=5`, the reproduced extrema are:

| Quantity | Value | Background scrambled coalition |
|---|---:|---|
| load `(0,1)` minimum | 0.323314 | `(5,)`, i.e. spectator already absent |
| spectator `(2,3)` maximum | 0.441978 | `(0,1,4)`, i.e. load already absent plus support edges |

Those two values cannot be observed under the same background intervention. Their crossing does not show that a load and spectator are indistinguishable in any single context.

I compared the two marginal effects under every **common** background coalition drawn from the four remaining support edges. Results:

| `a` | minimum matched-context `(load − spectator)` | all matched contexts rank load > spectator? |
|---:|---:|---|
| 3.4 | 0.313449 | yes |
| 5 | 0.323314 | yes |
| 8 | 0.331647 | yes |
| 15 | 0.338443 | yes |
| 100 | 0.345328 | yes |

Thus the statement that “semantic discrimination degenerates at `a*`” is false. What degenerates is a stronger **context-free robust-envelope dominance** property. That can be a useful criterion, but it must be named and defended as such. It is neither necessary for discrimination nor implied by “well-definedness.”

This is the decisive attack on the ceiling claim.

### 2.2 The “fine sweep” does not locate the threshold

The code samples `np.linspace(0.2,6.0,59)`, a step of 0.1, and reports the first failed grid point as `a*=3.4`. Bisection on the actual crossing gives:

`a* = 3.3027756377319886`.

Calling 3.4 an approximation is not fatal, but calling the procedure a “fine sweep” and treating the first failed grid value as the threshold overstates precision.

### 2.3 Model 3 does not establish semantics beyond `S + graph`

In equal-strength K4, the graph is symmetric before `S` is declared. After `S={0,1}` is supplied, the diagnostic defines:

- load: both endpoints in `S`;
- support: one endpoint in `S`;
- spectator: no endpoints in `S`.

The three equivalence classes are therefore determined directly by the declared subset and graph automorphisms. The computation supplies magnitudes and the envelope crossing, but it does not discover which edge class is viability-relevant. The “load” and “spectator” labels already encode that answer.

This is analogous to the canon’s earlier §11b competence-check issue: recovering a designed ordering can show internal consistency, but not independent semantic content. Equal edge strengths remove coupling-magnitude leakage; they do not remove declaration leakage.

The defensible grade is **competence/self-consistency check**, not “semantic-beyond-syntactic decisive test.”

### 2.4 The result changes sharply with other declared `S`

Using the same K4, same equal strengths, same interval criterion, and representative highest- versus lowest-endpoint-membership edge classes:

| Declared viability set | Available endpoint classes | interval crossing |
|---|---|---:|
| `S={0}` | 1 vs 0 endpoints in `S` | `a*=1.61803399` |
| `S={0,1}` | 2 vs 1 vs 0 | `a*=3.30277564` |
| `S={0,1,2}` | 2 vs 1 | `a*=0.64038820` |
| `S={0,1,2,3}` | only 2 | no load/spectator distinction exists |

The diagnostic itself states that `S=all nodes` recovers the KW whole-system viability case. Yet precisely there its informativeness test is undefined: symmetry gives all six edges the same interval.

Therefore the three-model selection supports only an existential statement about some local declarations. It does not establish a stable salvage region for the declared AOP mask, and `a*≈3.4` is not even robust within the same graph family.

### 2.5 The 0.5 width tolerance materially manufactures “non-trivial” breadth

For Model 3, the load interval is also the widest edge interval, so correcting the code’s advertised “max over structural edges” rule does not change this particular model. But the chosen tolerance determines how far the well-defined region extends:

| `rel_width_tol` | largest `a` passing width + disjointness |
|---:|---:|
| 0.05 | ≈0.0845 |
| 0.10 | ≈0.1947 |
| 0.20 | ≈0.5334 |
| 0.30 | ≈1.1801 |
| 0.40 | ≈2.6109 |
| 0.50 | ≈3.2997 |

At the actual envelope crossing, the load width is about `0.428 × Wagg`. The advertised ceiling at 3.3 is therefore visible only if “well-defined” permits an interval almost half as wide as the aggregate effect. A stricter but equally plausible 0.2 bar ends the region near `a=0.53`.

The strongest existential claim (“some overlap exists”) survives any positive tolerance in the `a→0` corner. The stronger claim (“non-trivial,” “genuinely coupled,” extending well into redundancy) is threshold-dependent and cannot be called settled without an externally justified resolution criterion.

### 2.6 The 0.02 information threshold is not tuned; it is ignored

The code computes

`inf = sh_L - sh_S >= 0.02 * Wagg`

but defines

`salv = disjoint and wd_load`.

Thus changing 0.02 cannot change the final salvage verdict. This threshold did not manufacture the positive; it is dead with respect to the claimed result. That is still a specification defect because the docstring defines `salvageable = well_defined AND informative`, while the implementation substitutes interval disjointness for the `inf` flag.

### 2.7 The printed “Shapley” values are not Shapley values

`edge_weight_interval` returns the unweighted mean over all `2^(m−1)` coalitions. A Shapley value weights a coalition of size `r` by

`r! (m-r-1)! / m!`,

equivalently averaging a player’s marginal over random orderings. The two are not generally equal.

Reproduction for the Model 3 spectator:

| `a` | code’s “Shapley” mean | true Shapley value |
|---:|---:|---:|
| 1 | 0.022162 | 0.014720 |
| 3 | 0.061440 | 0.040372 |
| 8 | 0.102911 | 0.066441 |
| 15 | 0.127865 | 0.081428 |

The special load edge happens to have equal uniform and Shapley averages here because of symmetry, but the spectator does not. This error does not rescue the interval verdict; it invalidates the deposited Shapley interpretation and any claims based on its printed magnitude.

### 2.8 O-information is computed on the wrong object

The diagnostic says O-information is computed “on the declared set.” The code calls `o_information(Sigma)` on the full covariance matrix.

For Model 3:

| `a` | Ω on full K4 (reported object) | Ω on declared `S={0,1}` |
|---:|---:|---:|
| 0.75 | 0.148216 | 0 |
| 3.3 | 0.792946 | 0 |
| 5 | 1.082864 | 0 |

For two variables, O-information is identically zero. Consequently:

- “Ω≈0.81 at the declared-set ceiling” is false;
- “the Ω sign plus interval test” is not the cheap declared-set diagnostic claimed;
- KW non-uniqueness, O-information redundancy, and the envelope crossing have not been shown to be the same phenomenon.

Whole-system Ω may still be a useful covariate. It must be labelled whole-system Ω and its relationship to the edge-attribution crossing demonstrated rather than asserted.

### 2.9 Kolchinsky–Wolpert is inspiration, not grounding for this operator

KW’s construction has four load-bearing features absent here:

1. a system/environment decomposition `X/Y`;
2. a dynamical timescale from initial state to future viability;
3. an intervention that scrambles syntactic information—initial `I(X0;Y0)` for stored information or environment→system transfer entropy for observed information—while running the dynamics;
4. an optimization over interventions that preserve viability while minimizing remaining syntactic information.

The deposited diagnostic instead:

- has a static equilibrium Gaussian;
- declares an internal node subset `S`;
- deletes an internal coupling parameter `θ_e` from the precision matrix;
- immediately recomputes marginal negentropy;
- constructs a cooperative game over edge deletions.

Deleting a coupling changes the physical/statistical mechanism and generally changes multiple marginal and joint properties. It is not the same intervention as scrambling a selected system–environment information channel. KW explicitly allow researchers to choose other interventions, so this is not illegitimate; it is simply not settled KW method.

The diagnostic also maps KW’s possible **non-uniqueness of an optimal intervention** onto the width of **all coalition marginals for a preselected edge**. KW’s statement concerns multiple minimizers of their information-preserving optimization. It does not establish the min–max edge interval or its crossing as the relevant non-uniqueness criterion.

Canon v1.21 is more accurate than the diagnostic here: it already says that applying KW’s idea to internal couplings is “an extension of their method rather than a direct application.” The diagnostic should not upgrade that extension to “the KW semantic-information construction.”

### 2.10 Fisher/VIF is decorative for the verdict

The Fisher matrix is computed for edge parameters from the full Gaussian distribution, not from the declared viability readout on `S`. Neither Fisher condition number nor VIF enters `salv`. They are ancillary diagnostics, not grounding for well-defined semantic attribution. Any claim that they independently validate the same boundary needs a derived relation or a predeclared correlated prediction.

## 3. Actionable Fixes

1. **Withdraw the current verdict and rename the object.** Call it an “AOP internal-edge ablation cooperative game with a negentropy payoff,” inspired by KW. Do not call it the KW construction.
2. **Choose the estimand before choosing the criterion.** Distinguish:
   - context-specific marginal attribution;
   - matched-context load/spectator ranking;
   - Shapley attribution;
   - worst-case context-free envelope dominance.
   These answer different questions. Interval disjointness is a sufficient robust-dominance test, not the definition of salvageability.
3. **Pre-register a declaration ensemble.** At minimum sweep all non-empty `S` on K4 and report the `S=all` null. Better: sample graph families, `S` sizes, and coupling patterns with selection rules fixed before results.
4. **Correct Shapley weighting** and expose the full context-value distribution rather than only min/mean/max.
5. **Make code match specification.** If salvageability is `well_defined AND informative`, use the declared `inf` flag; if it is width plus disjointness, remove the unused 0.02 rule. If well-definedness is global, actually test all structural edges.
6. **Replace the binary 0.5 tolerance with a sensitivity surface** or justify the tolerance from measurement resolution / decision loss outside the model.
7. **Separate whole-system from declared-set redundancy.** Compute and label both where defined. Do not treat Ω as the KW redundancy measure or assert a shared ceiling without a demonstrated mapping.
8. **Use the canon’s honest grade.** This is a self-consistency/competence calculation and a possible method-development direction, not a settled semantic-mask salvage result.

## 4. Creative Opportunities

The failure is scientifically useful. It exposes three distinct notions that the current “salvageability” label collapses:

- **semantic relevance:** whether an edge affects a declared viability payoff;
- **attribution stability:** whether that effect is stable across background interventions;
- **mechanistic identifiability:** whether an edge can be separately manipulated or estimated.

A stronger next diagnostic would plot these as separate axes. The interesting result may not be a single ceiling at all, but a phase diagram in which matched-context relevance survives while context-free ownership attribution and parameter identifiability dissolve at different rates. That would fit AOP’s refusal of ownership more cleanly than forcing all three into one interval-overlap threshold.

## 5. Final Grade

**RED — the stated salvage verdict does not hold.**

The chosen model has a real weak-to-moderate-coupling interval-envelope separation, but:

- the “semantic” class structure is supplied by `S`;
- the result is unstable across permitted `S`;
- the `a*` ceiling is an unmatched-context envelope crossing, not loss of semantic ranking;
- the Ω linkage is computed on the wrong set;
- and the intervention is not the KW scramble claimed as its settled grounding.

**YELLOW only for the narrower research direction:** an AOP-specific internal-edge ablation game can be defined and studied, provided its operator, attribution convention, declaration dependence, and thresholds are made explicit.

— End of review —
