# Task B — reproduction of the headline numbers against the pinned definition

**Builder proposal — Prime verifies; Ben decides. Not a verdict; touches no canon master.**
**From:** Claude Science (builder), AOP · **Date:** 22 July 2026 (v1)
**Artifact:** `mask_salvage.py`, sha256 `20c02ca1243ca6cb8d4f6a174be13d1b2dd338771078132b658a24c82dbaf062` (verified before running). Full run log deposited alongside this memo as `AOP_MaskSalvage_runlog_v1_20260722.txt`.

## Headline numbers — reproduction status

| Quantity | Reported | Reproduced | Status |
|---|---|---|---|
| Interval-merge point a\* | 3.3027756… | **3.3027756377** | **exact** |
| Ω (O-information) at a\* | ≈ 0.81 | **0.812** | **exact** (to reported precision) |
| Model 3 interval table | (see runlog) | reproduced digit-for-digit | **exact** |

### a\* is analytic, not a grid artifact — and I have the closed form

The deposited script locates a\* with a coarse `np.linspace(0.2, 6.0, 59)` sweep (step ≈ 0.0983), which prints the merge at its grid node **a = 3.40** — *not* at 3.3027756. The reported eight-digit precision therefore **cannot** come from running the deposited script as-is; it is an analytic value. I recovered it two ways:

1. **Root-find** on the interval-gap `lo_load(a) − hi_spec(a)` (Brent, xtol 1e-10): **a\* = 3.3027756377**.
2. **Closed form** (charter: analytic over estimated). The merge condition is `φ_load(∅) = φ_spec({0,1,4})` — the load edge's empty-context marginal equals the spectator's marginal in the three-edge context {(0,1),(0,2),(1,3)}. Solving the resulting determinant-ratio equation symbolically gives

   **a\* = (3 + √13) / 2 = 3.30277563773199…**

   This is exact and closed-form; the numerical root matches it to 12 digits.

**Directional vs exact:** the a\* value **reproduces exactly** (and is now pinned to a closed form). The *grid location* in the deposited script is directional only (3.40, its nearest node) — flagged plainly, as required. Ω ≈ 0.81 reproduces exactly at 0.812.

### Model 3 interval table (deposited-script Laplacian semantics, S={0,1})

| a | W_agg | LOAD [lo, shap, hi] | SPEC [lo, shap, hi] | disjoint | salv |
|---:|---:|---|---|:--:|:--:|
| 0.1 | 0.245 | [0.077, 0.084, 0.091] | [0.000, 0.000, 0.001] | Y | YES |
| 0.5 | 0.752 | [0.203, 0.275, 0.347] | [0.000, 0.008, 0.024] | Y | YES |
| 1.0 | 1.060 | [0.255, 0.402, 0.549] | [0.000, 0.022, 0.077] | Y | YES |
| 3.0 | 1.592 | [0.310, 0.641, 0.973] | [−0.000, 0.061, 0.286] | Y | YES |
| 5.0 | 1.846 | [0.323, 0.761, 1.199] | [−0.000, 0.083, 0.442] | N | no |
| 8.0 | 2.080 | [0.332, 0.874, 1.417] | [−0.000, 0.103, 0.613] | N | no |

Salvageable (grid) on Model 3: `a ∈ [0.1 … 3.0]`; disjointness breaks between a = 3.0 and 5.0 (analytically at a\* = 3.3028). Reproduces the deposited FINAL VERDICT block exactly.

## The two documented code coincidences — both independently confirmed

The work order flags that the executable predicate (`salv = disjoint AND wd_load`) differs from the prose (`salvageable = well_defined AND informative`) yet prints the same K4 table by coincidence. I verified **both** coincidences hold:

1. **Load-only = global well-definedness here.** The load edge (0,1) is the **widest** structural edge at every a tested (widths at a=1.0: load 0.294 vs 0.212 for the four support edges vs 0.077 spectator). So `max over structural edges` and `load only` return the same well-definedness flag — coincidentally.
2. **disjoint ⟹ inf here.** At every grid point where the load/spectator intervals are disjoint, the 0.02·W midpoint-separation flag `inf` is also true. So dropping the `inf` conjunct from the executed predicate does not change the printed table — coincidentally.

Both are genuine coincidences of this K4 model, exactly as the work order states: **a re-execution confirms arithmetic, not that the estimand matches the prose.** Task C resolves which predicate to adopt.

## Grading (three-category scheme)

Reproduction is an **identity / theorem demonstration** — it verifies the code computes what the pinned definition says and recovers the published constants (a\* now closed-form). It **adds no evidential weight** to any salvage claim; the forced-ness of the existential result (established by Prime/critic) is unchanged.

*Syntactic layer only. Touches no canon master. Prime verifies; Ben decides.*