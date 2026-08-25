# Moving-MIP well-posedness gate — does the straddle obstacle survive size-normalization?

**Builder proposal — Prime verifies; Ben decides. Nobody grades their own homework.**
**From:** Claude Science (builder lane), AOP · **Date:** 21 July 2026 (v1)
**Verified against:** `AOP_CANON_MASTER_v1.21.md` (Drive id `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`, masthead v1.21, mod 2026-07-21T19:15Z)
**Task (from CP):** one closed-form well-posedness check that gates whether the moving-MIP repair is worth doing. **This is not the repair** — it decides whether the eight-item roadmap is pointed at a real problem. Deposit + grade; do not start the repair either way.

## Verdict

**The frontier item is WELL-POSED. The straddle obstacle is real, not a normalization artifact — the repair is worth scoping.**

- **(a) The relabeling survives normalization** — in a *cleaner, stronger* form. Size-normalization removes the singleton small-side artifact, but the per-slice MIP **still relabels across a straddle**: the module cut is the **unique** MIP for all `b < 1`, ties at the fully-symmetric point `b = 1`, and relabels to a **different balanced 3|3 cut** for `b > 1`. That is a genuine competition between two non-trivial organizations — exactly the object a moving partition would have to track.
- **(b) Zero-calibration is preserved.** `Φ_MIP = 0` exactly on the block-decomposable `Σ(b=0)` under both normalizations tested (a zero deficit divided by any positive factor is still zero). The load-bearing canon calibration (v1.21 lines 631 / 709) does not break.

This is the outcome CP flagged as the "survives" branch: the frontier item is well-posed and the repair is worth scoping. It does **not** authorize the repair — that remains Prime's/Ben's call.

## What was computed

Identical model to the deposited build (imported unchanged): `N = 6`, two 3-node modules `{0,1,2}|{3,4,5}`, intra-module weight 1.0, inter-module weight `b`, `g = 1.0`, `Σ = (I + gL)⁻¹`. `Φ` across a bipartition `(A,B)` is the Gaussian mutual information `I(A;B) = ½(logdet Σ_AA + logdet Σ_BB − logdet Σ)`. All 31 bipartitions enumerated exhaustively; matrix inverse + determinants; **no estimation**. `b`-ramp `0 → 1.4`, the same window as the build.

**Normalization choice.** Primary: `Φ_norm(A,B) = I(A;B) / min(|A|,|B|)` — the cut's mutual information per node of the *smaller* part. The small-side vulnerability is precisely that a one-node part severs few edges and so pays little total mutual information; dividing by the small-side node count removes that pure size advantage while staying inside the third-person coupling graph (no ownership scalar, consistent with the canon's ownership-free constraint). Cross-checked against an IIT-style entropy normalization `I(A;B) / min(H(A), H(B))` (`H` = Gaussian marginal entropy of the part): same qualitative verdict, so the finding is not an artifact of the particular normalizer.

## Results

**(b) Calibration at `b = 0`:**

| normalization | MIP | Φ_MIP (deficit) |
|---|---|---:|
| none | `{0,1,2}｜{3,4,5}` | 0.000000 |
| size (min\|A\|,\|B\|) | `{0,1,2}｜{3,4,5}` | 0.000000 |

**(a) MIP kind across the ramp:**

| normalization | `b < b*` | relabels at | destination |
|---|---|---|---|
| none (unnormalized) | module cut `{0,1,2}｜{3,4,5}` | `b* = 0.4207` | **1｜5 singleton** (small-side artifact; 7-way tie at the exact crossing) |
| size-normalized | module cut `{0,1,2}｜{3,4,5}` | `b = 1.000` | **balanced 3｜3** (e.g. `{0,2,3}｜{1,4,5}`) |

**Uniqueness margin (size-normalized), gap = best non-module Φ_norm − module-cut Φ_norm:**

| `b` | gap | module cut is… |
|---:|---:|---|
| 0.20 | +0.0675 | the unique MIP |
| 0.60 | +0.0253 | the unique MIP |
| 0.95 | +0.0025 | the unique MIP |
| 0.99 | +0.0005 | the unique MIP |
| 1.00 | 0.0000 | tied (symmetric point) |
| 1.20 | −0.0085 | not the MIP (relabelled) |

The relabel at `b = 1` is exactly the point where cross-coupling equals intra-coupling — where the planted community structure disappears and then inverts. That is a real reorganization of the coupling graph, not a scoring pathology.

## Interpretation, honestly bounded

- **What this shows.** The obstacle the canon names (a MIP that relabels *inside* a developmental window, so no single window-spanning partition scores a straddling window) is genuine under a principled normalization, and in fact becomes a *cleaner* test: module cut vs a competing balanced cut, not module cut vs a degenerate singleton. A moving-partition object has something real to track.
- **What it does not show.** It does not build the moving partition, does not make the window score grid-invariant, and does not establish that the relabel is an "individuation event" in any semantic sense — that reading belongs to the viability layer, out of this lane. The `b = 1` crossing in *this* model is also maximally symmetric: past `b = 1` the normalized MIP is **9-fold degenerate** (node-exchange symmetry of the complete two-weight graph). That degeneracy is a property of the toy model, not of normalization or of the small-side artifact — but it means the repair's benchmark should **fully break the node-exchange symmetry** (all pairwise weights distinct) so a *unique* competitor is singled out and all tied optimal paths are exposed. A fully symmetry-broken run (every edge weight jittered) confirms this: the normalized MIP is the module cut for `b < 1` and a **single** balanced 3\|3 competitor for `b > 1` (#tied = 1 throughout), with `b = 0` calibration preserved. (Note: breaking only the *module-level* symmetry — e.g. one module tighter than the other — is not enough; the within-module node interchangeability keeps the 9-fold tie past `b = 1`.) The `check_symmetry_broken` routine in the deposited script reproduces this.

## Consequence for the frontier register

The moving-MIP item in canon §§4 / 9a / 13a stays **FRONTIER** — this gate does not close it. What it establishes is that the item is **well-posed**: there is a real straddling relabeling to solve, so scoping the repair is justified. **No canon edit is warranted from this memo** (it neither closes nor restates a claim); it is a builder proposal for Prime to verify. If Prime concurs, the §8 repair roadmap can be scoped with the added benchmark-design requirement (symmetry-broken, unique competitor, all tied paths exposed).

## Grading

- **The computation: SETTLED** — closed-form on the canon's own Phase-D model; exact matrix algebra + exhaustive enumeration; reproduced by the deposited script and robust across two normalizations.
- **The "well-posed" reading: SYNTHESIS** — a defensible interpretation of the computed relabeling as a genuine competing-partition transition, grounded in the model but not itself a settled AOP claim.

## Files

- `phaseF_normalizedMIP_wellposedness_v1_20260721.py` — runnable, self-contained (NumPy only); reproduces every number above by deterministic direct computation and prints the four checks. Run with `--figure` (needs matplotlib) to regenerate the figure.
- `phaseF_normalizedMIP_wellposedness_fig_v1_20260721.png` — two-panel figure: (a) MIP partition-kind vs `b` for both normalizations; (b) size-normalized uniqueness margin.

*Syntactic layer only (Φ_MIP, coupling graph). Touches no semantic-mask, star, or provenance quantity. Builder proposal. Prime verifies; Ben decides.*