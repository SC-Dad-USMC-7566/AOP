# E1 results note — Boundary–Integration collapse test

**Script:** `phaseE1_BI_dissociation.py` (SEED=20260723, NSYS=6000, closed-form Gaussian). Deliver for prime to verify by re-running.
**Base canon:** v1.24 (SHA-256 3e64ff0c…0dd421cf).

## Pre-registered criteria (frozen) and computed results
- **C1 (both dissociation corners non-empty).** Corner A (B2 ≤ p15 ∧ TC ≥ p85, "sealed-yet-integrated") = **308** systems; Corner B (B2 ≥ p85 ∧ TC ≤ p15, "leaky-yet-unintegrated") = **72** systems. Both non-empty → **C1 PASS.**
- **C2 (spread at fixed integration).** Within the top-TC quartile (n=1500): B1 spread 4.230 ≥ in-quartile median 0.840; B2 spread 0.368 ≥ median 0.063; B1′ spread 0.512 ≥ median 0.055. All hold under both the in-quartile and whole-ensemble median readings → **C2 PASS.** (Verdict robust to the B1/B1′ choice.)
- **C3 (honest correlation reporting; no pass/fail).** Spearman/Pearson vs TC: B5 +0.009/+0.115; B2 −0.248/−0.239; B1 +0.500/+0.612; B1′ +0.310/+0.412. Mean I(in;out)/TC share = 0.254.

## Verdict
C1 ∧ C2 hold → **the four-fold carving survives the Boundary–Integration collapse test.** Boundary and Integration dissociate *generically* across random Gaussian systems, not only by hand-built construction. **Grade: SYNTHESIS / analytic-model-result.**

## What was and was not shown
- **Shown:** across 6000 random N=7 systems spanning sealed→leaky (seal_bias-gated bypass), both dissociation corners are populated and Boundary's own content (B1 state-contrast, B2 screening-residual) retains spread when Integration is held high. The carving's own §13 falsifier ("two axes collapse into one that always co-moves") does **not** fire for B–I.
- **Not shown:** this is a claim about the operational Gaussian model class, not a proof over all systems. B5 = I(in;out) remains an **algebraic** component of TC (nesting identity) — its dissociation is not claimed; B1 and B2 carry the independent Boundary content.

## FLAG FOR PRIME (substantive, not folded here)
The canon (v1.24 line 189) states a **~0.83 Boundary–Integration correlation** as "the nesting identity showing through." In the phaseE1 random-Gaussian ensemble the **B5–TC rank correlation is ≈0.01** (Pearson ≈0.12): TC's variance is dominated by the intra-block terms TC_in/TC_out, which swamp B5's ~25% share. The ~0.83 figure is therefore **construction-specific, not a generic property.** This is a possible tension with a canon number; per tightening-pass discipline I did not alter the number — logging it for prime / red team to adjudicate. It does not affect the C1/C2 verdict (which rests on B1, B2, not on the B5–TC correlation).
