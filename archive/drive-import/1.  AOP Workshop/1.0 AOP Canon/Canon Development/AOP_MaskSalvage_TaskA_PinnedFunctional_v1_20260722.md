# Task A — the viability functional and scramble semantics `mask_salvage.py` implements, pinned

**Builder proposal — Prime verifies; Ben decides. Not a verdict; touches no canon master.**
**From:** Claude Science (builder), AOP · **Date:** 22 July 2026 (v1)
**Source artifact:** `mask_salvage.py`, Drive `1GPcrRSySofAD_yZeCcPkpB_S53IOkrC_`, **sha256 `20c02ca1243ca6cb8d4f6a174be13d1b2dd338771078132b658a24c82dbaf062` — verified before running** (matches the work-order hash exactly).

## Result in one line

The two re-derivations disagree **only about the scramble operation**, not the physics. The deposited script scrambles the **whole edge Laplacian** → load edge **O(a)**, matching the outside critic. Prime's re-derivation scrambles **only the off-diagonal precision entry** → load edge **O(a²)** (slope 2.0016). The spectator is **O(a³)** under both. Forced-ness holds either way, because the spectator vanishes strictly faster in both.

## The functional, in closed form (exactly as the script implements it)

Model class: static Gaussian on a coupling graph. For `N` nodes, edge set `E`, edge weights `θ_e`, base `β = 1`:

- Edge Laplacian `B_e` for edge `e = (i,j)`: `+1` on the `(i,i)` and `(j,j)` diagonal, `−1` on the `(i,j)` and `(j,i)` off-diagonal.
- Precision `J(θ) = β·I + Σ_e θ_e · B_e`.
- Covariance `Σ = J⁻¹`.
- **Viability functional (grounded in Kolchinsky & Wolpert 2018, Interface Focus 8:20180041 — Gaussian negentropy on the declared viability set S):**
  `V(θ; S) = −½ · log det Σ[S,S]` (the additive constant `+½|S|log(2πe)` cancels in every weight below).

**Scramble-and-rerun weight (the script's estimand).** "Scramble edge `e`" sets `θ_e → 0` — i.e. **subtracts the entire term `θ_e·B_e` from J**, which removes the off-diagonal coupling *and* decrements the two endpoint diagonals (degrees). The weight of `e` in context `C` (a set of already-scrambled edges) is the marginal viability drop:
`φ_e(C) = V(scramble C) − V(scramble C ∪ {e})`.
This is interval-valued over contexts `C ⊆ E∖{e}`: `[ min_C φ_e(C), max_C φ_e(C) ]`, with the mean over all `2^{|E|−1}` contexts equal to the Shapley value. All closed-form (matrix inverse + `slogdet` + exhaustive coalition enumeration); no sampling, no estimator.

## The weak-coupling expansion (closed form, symbolic)

On the equal-strength K4 (`edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]`, all `θ_e = a`), declared set `S = {0,1}`, load `= (0,1)`, spectator `= (2,3)`:

**Deposited-script scramble (whole Laplacian `θ_e·B_e → 0`):**
- Load edge, empty-context marginal: `φ_load(∅) = a − 3a² + (28/3)a³ + O(a⁴)` → **leading order O(a)** (numerical log-log slope **0.9992**; uniform across all `2⁵ = 32` contexts, slopes 0.997–0.999).
- Spectator edge: `φ_spec(∅) = 0` **exactly** (empty context); nonzero only once other edges are scrambled, at leading order **O(a³)** (max-over-context slope **3.0008**).

**Prime's scramble (off-diagonal precision entry `J[i,j] → 0`, diagonal left intact):**
- Load edge, empty-context marginal: `φ_load(∅) = −a²/2 + a³ + O(a⁴)` → **leading order O(a²)** (numerical slope **1.9995**, matching Prime's reported 2.0016).
- Spectator edge: `−2a³ + O(a⁴)` → **O(a³)** (matches Prime's 3.0007).

## Which re-derivation matches, and why the other differs

- **The outside critic (O(a)) matches the deposited script.** The script's `V_with_scrambled` sets `th[k] = 0.0` and rebuilds `J = β·I + Σ θ_e B_e`, so scrambling removes the full Laplacian term. Under that operation the load edge's marginal is O(a).
- **Prime's O(a²) is a different — also legitimate — scramble semantics:** zeroing the precision matrix's off-diagonal entry while leaving the endpoint degrees on the diagonal unchanged. That single change lifts the load exponent from 1 to 2 (`a → −a²/2`). It does **not** describe the deposited script.
- **Both give spectator O(a³) and load-above-spectator at every weak-coupling point**, so the work order's forced-ness conclusion is independent of the choice. The exponent enters the *rhetoric* of the regrade, not the conclusion — which is exactly why Task A pins it before any regrade text is written.

## Grading (three-category scheme)

This is an **identity / theorem demonstration** — the exponents are closed-form algebraic facts of the two operations; no parameter inside the declared class flips them. It **adds no evidential weight** to any salvage claim; it fixes the definition so the downstream tasks (B–D) can be read correctly.

## Recommendation for B–D (builder's proposal; Prime decides)

Reproduce and run **against the deposited-script Laplacian semantics** (load O(a)), since that is the operation in the audited artifact of record, and flag the off-diagonal alternative as a named convention. Every subsequent number in this workstream is reported under the Laplacian scramble unless explicitly labelled otherwise.

*Syntactic layer only (Φ / coupling graph / attribution). Touches no semantic-mask star or provenance quantity, no canon master. Prime verifies; Ben decides.*