# E3 results note — is "alive" positively detectable, or negative-only?

**Script:** `phaseE3_life_detection.py` (SEED=20260723, closed-form OU / Lyapunov). Deliver for prime to verify by re-running.
**Base canon:** v1.24.

## Pre-registered questions (frozen) and computed results
- **Q1 (correctness).** On the OU star↔cell interpolation, the third-person procedure (load-bearing: ablate candidate reference edge, V drop ≥ w_min=0.30; decoupled: do-intervention clamp shifts x's set-point ∧ reference structurally separable from x) flags **d=1 (cell) ALIVE** and **rejects d=0 (star)**. Load-bearing drop: d=0 → 0.000, d=1 → 1.000 (at d=1, ablating the reference leaves x undriven → total viability loss). → **Q1 PASS.**
- **Q2 (architecture, not magnitude).** Sweeping the reference/regulated timescale ratio k_r/k_t over **k_r ∈ [0.01, 20]** (3+ orders of magnitude): d=1 stays alive and d=0 stays not-alive at every ratio. The flip along d is driven by the **existence of the separate reference node**, not by a slow/fast magnitude — matching the Figure LT-T claim. → **Q2 PASS.**
- **Q3 (decisive: second declaration?).** V declares the regulated node x. Testing every node blind for (2a)∧(2b): node x fails (2b) (clamping x clamps x); node r passes both. The qualifying model node = **{r}, unique, with no separate "this is the model" label.** → V suffices in the specified model.

## Verdict & grade
**Two-sided detector, up to the standing V-declaration.** Given only the coupling graph and V, the procedure positively flags the cell alive, rejects the star, is architectural (timescale-invariant), and singles out the reference node r without a second observer declaration. **Grade: FRONTIER, computed.** This supports upgrading the §11a criterion from "demonstrated for self-consistency" toward "positively detectable (up to V)."

## What was and was not shown — scoping caveat (report to prime)
- **Shown:** in the specified 2-node star↔cell family, aliveness is positively detectable from third-person access up to V, and node attribution is unique.
- **Not shown / caveat:** a **stress test** adding a second, symmetric decoupled reference z (x tracks both r and z; both hold μ*) shows (2a)∧(2b) return **{r, z}** — aliveness is still **detected** (a decoupled model exists) with no label, but **node attribution** is non-unique from (2a)+(2b)+V alone (r and z are symmetric; V cannot rank them). So: *detection* of aliveness needs no second declaration; *attribution* of which node is the model does, when multiple symmetric references exist. This is a scope on attribution, not a failure of detection. The star is correctly rejected in all cases (no separate reference node → (2a) gain = 0).
- **Model-class scope:** linear OU / Gaussian, static parameters; the non-stationary and multi-reference cases are frontier.
