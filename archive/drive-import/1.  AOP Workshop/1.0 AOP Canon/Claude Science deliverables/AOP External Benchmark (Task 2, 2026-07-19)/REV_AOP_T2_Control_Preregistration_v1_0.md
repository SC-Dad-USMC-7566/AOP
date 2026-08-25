# AOP T2 Specificity Control — Preregistration (v1.0, FROZEN before running)

**Compiled:** 20 July 2026 by Claude (builder), *before* running the control. Non-canonical. This is a separate, small prereg for the fourth task; the frozen benchmark prereg is NOT edited.

**Provenance discipline:** this note is deposited to Drive *before* the control screen is executed. The pass/fail criterion below is fixed now and will not be moved after seeing the result.

---

## The question

T2 (the one genuine external win) is: AOP's coalition/viability layer flags 13 synthetic-lethal isozyme pairs the single-axis flux-strength rival cannot see. The referee-killer (OAI critic Q1, prime concurs): **"the single-axis rival can't see them" is not "AOP is needed to see them."** Does an ordinary double-knockout FBA synthetic-lethal screen — with **no** AOP coalition/viability/Möbius machinery — already recover the same 13 pairs? If yes, T2 is standard double-KO SL detection in AOP vocabulary and cannot be reported as AOP-specific.

## What the AOP T2 layer actually computes (stated now, for honesty)

Inspection of the frozen v1.1 scorer: T2 pairs are flagged when both single deletions are viable (ΔV < 0.01, i.e. growth > 0.99·WT) and the double deletion drops viability by ≥ 0.5 (ΔV_joint ≥ 0.5). The Möbius interaction h = ΔV_joint − ΔV_g1 − ΔV_g2. For all 13 pairs both singles have ΔV ≈ 0, so **h ≈ ΔV_joint** — the "coalition/Möbius" quantity collapses to the raw double-KO growth drop. This tells me, before running, that I should **expect** a plain double-KO screen with matched thresholds to recover the same set, and expect the h-ranking to be monotone with the plain joint-growth-drop. The control below tests that expectation honestly rather than assuming it.

## Design (frozen)

All screens on the **same frozen core model** (`MODEL_e_coli_core.xml`, MD5 `2fd9c214652195707526448954b88696`), deterministic: pFBA-consistent solver settings + all growth/ΔV values quantized to 1e-6 before thresholding (same as Fix 1). No AOP layer — raw FBA growth of single and double mutants only.

**A. Matched-threshold plain screen (PRIMARY — isolates "machinery").** For each pair (i,j) of genes each individually viable (growth > 0.99·WT): flag as synthetic-lethal if double-KO ΔV_joint ≥ 0.5. This uses the *same operational thresholds* as the AOP T2 layer but strips the Möbius/viability framing — it is raw double-KO growth only. Compare its flagged set to the 13 AOP pairs.

**B. Standard strict SL screen (CONTEXT).** A single conventional threshold τ = 0.01·WT (the standard essentiality cutoff): each single viable (growth > τ) and double lethal (growth ≤ τ). Report its set and overlap with the 13, noting explicitly that any difference from set A is a **threshold choice** (0.5 vs 0.99 joint drop), not AOP machinery.

**C. Ranking check.** Is the AOP Möbius-h ranking of the 13 pairs monotone (identical order, ties allowed) with ranking by plain joint-growth-drop ΔV_joint? If yes, the coalition layer confers no ranking advantage.

For each screen report: (1) the pairs it flags, (2) how many of the 13 AOP pairs it recovers, (3) any SL pairs it finds that AOP does **not** surface.

## Pre-registered pass/fail criterion (FROZEN — decided now)

**T2 AOP-specificity is NOT established** if *all* of:
- the matched-threshold plain screen (A) recovers **all 13** AOP pairs (AOP ⊆ plain screen), AND
- AOP surfaces no additional biologically-meaningful synthetic-lethal structure the plain screen misses, AND
- the Möbius-h ranking (C) is monotone with the plain joint-growth-drop (no ranking advantage).

In that case T2 is reported as **"AOP reproduces standard synthetic-lethal detection"** — NOT a unique AOP win.

**T2 AOP-specificity is supported ONLY IF** the coalition/viability layer either (i) recovers biologically meaningful pairs the plain screen misses, or (ii) organizes/ranks the pairs in a way the plain screen structurally cannot — and that difference is stated **concretely** (which pairs, what the plain screen does with them), not asserted.

The overlap is reported **either way**. A control that dissolves the win is a result, not something to hide — same discipline as T4.

## Note on interpretation (frozen)

Even if screen B (strict τ) recovers fewer than 13 while AOP's ≥0.5 threshold recovers all 13 (e.g. the cyd/cbd oxidase pairs sit at ΔV_joint ≈ 0.76, below strict lethality), that is **not** evidence of AOP-specificity: a plain screen run at the same ≥0.5 threshold (screen A) finds them too. Threshold generosity is not machinery. This is fixed now so it cannot be retro-fitted into a win after seeing the numbers.
