# E2 results note — does the mask have an informative ∩ well-defined region above triviality?

**Script:** `phaseE2_mask_domain.py` (SEED=20260723, N=8, closed-form Gaussian). Deliver for prime to verify by re-running.
**Base canon:** v1.24.

## Pre-registered definitions & thresholds (frozen — not moved)
- Well-defined at edge e ⇔ h_e ≤ **ρ·|w_e|**, ρ=0.5.
- Informative ⇔ (w_LB − w_inert) ≥ **K·max(h_LB,h_inert)**, K=3.
- Triviality floor: TC ≤ τ_floor, τ_floor = TC at g where off-diagonal precision coupling = 5% of diagonal (per topology).
- Question: does a system exist that is well-defined ∧ informative ∧ non-trivial (TC > τ_floor)?

## Operationalization flag (declared; prime please confirm)
The resolvability spectrum is read on the **state correlation matrix** Corr(Σ), not on the precision M=I+gL. Reason: for a graph Laplacian, λ_min(M)≡1 for all g (the constant mode), so 1/√λ_min never grows and the blur mechanism the probe is about would never engage — a degenerate reading. The inferential VIF the canon names (1/(1−R²)) is collinearity of the node states = a property of Corr(Σ). As g rises, nodes become collinear → λ_min(Corr)→0 → 1/√λ_min diverges (blur) while 1/√λ_max stays bounded (aggregate sharp), exactly the §13 statement. Frozen, parameter-free half-width: h_e = |w_e|·(1/√λ_min − 1/√λ_max)/(1/√λ_min + 1/√λ_max). This gives the clean reading **well-defined ⇔ κ(Corr) ≤ 9** and (for inert weight ≈0) **informative ⇔ κ(Corr) ≤ 4**, where κ = λ_max/λ_min. No free constant; ρ, K, τ_floor unchanged.

## Computed result — PASS (mask salvageable), with a quantified ceiling
A well-defined ∧ informative ∧ non-trivial region exists for **all three topologies**, at low-to-moderate coupling:

| topology | τ_floor(TC) | region g-band | region TC | region Φ_MIP | region κ(Corr) |
|---|---|---|---|---|---|
| chain | 0.0087 | 0.057–0.789 | 0.009–0.479 | 0.0003–0.0155 | 1.21–3.88 |
| mean-field | 0.0566 | 0.089–0.329 | 0.072–0.493 | 0.0089–0.0488 | 1.71–3.63 |
| sparse-random | 0.0098 | 0.057–0.634 | 0.010–0.370 | 0.0006–0.0205 | 1.24–3.56 |

As g rises further, **informative** fails first (LB/inert gap swamped by blur), then **well-defined** fails; on strongly integrated systems (high g, TC ≳ 1) the intersection is empty.

## Verdict & grade
**PASS (mask salvageable):** the mask's informative, well-defined region is **non-empty above the triviality floor** — it is not confined to near-separable systems. **Grade: SYNTHESIS, computed.**

## What was and was not shown
- **Shown:** the mask survives into a genuinely-integrated (TC up to ~0.5, above the 5%-coupling floor) but **modest** regime, for all three topologies.
- **Not shown / honest ceiling:** the region does **not** extend to the strongly integrated systems "it was built to describe" (v1.24 line 17). The mask is sharp on moderately-integrated systems and blurs out above them — consistent with, and now quantifying, §6/§13's own blur admission. The PASS is real but bounded; do not read it as "the mask works on strongly integrated systems." The verdict depends on the declared Corr-matrix h_e; prime should confirm the referent.
