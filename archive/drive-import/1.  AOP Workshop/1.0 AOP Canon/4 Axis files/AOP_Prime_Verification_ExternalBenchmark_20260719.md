# Prime Verification — External (E. coli / Keio) Benchmark

**Compiled:** 19 July 2026 by Claude (prime). Independent re-run of the Task 2 builder deliverable. Non-canonical record.
**Inputs:** model + key MD5s match the prereg exactly (`2fd9c214…`, `936b99da…`). cobra 0.31.1, GLPK. Re-ran the frozen `aop_external_benchmark.py` multiple times + targeted diagnostics.

## Headline

The benchmark **design** is a real advance — genuine external answer key, pre-committed falsifiers, honestly a could-fail test. But on independent re-run the builder's numbers **do not fully reproduce**, and the honest verdicts are weaker than the results doc states. One pre-registered falsifier **fires**. Two methodological defects need fixing before the numbers can be quoted.

## Reproduced vs not

| Quantity | Builder | Prime re-run | Verdict |
|---|---|---|---|
| WT growth / scored / positives / quarantined | 0.8739 / 116 / 11 / 20 | **identical** | ✓ |
| T2 synthetic-lethal pairs | 13 | **13** (same isozymes) | ✓ robust |
| T1 AUROC (full scored set) | 0.848 | 0.849–0.854 | pass, but see defect B |
| T3 margin (AOP − rival AUROC) | "exactly 0.1000" | 0.107–0.112 | pass, but solver-dependent |
| **T4 Spearman(strength, ΔV)** | **+0.482 → "PARTIAL"** | **+0.53 (reproducible) → FALSIFIED** | **verdict flips** |

## Defect A — the benchmark is not deterministic

FBA has non-unique optimal flux distributions. Everything built on the WT flux vector (the rival's "coupling strength," and the T4 Spearman) changes run to run — my own repeated runs gave T4 = 0.524, 0.537, 0.551. The prereg asserted determinism ("LP, no seed needed") and promised "the builder's numbers stand only if prime reproduces them." They don't. **Fix:** compute the WT flux vector with parsimonious FBA (`pfba`) or a fixed tie-break so the flux-based metrics are reproducible. Under pFBA the reproducible values are T4 Spearman **0.528**, rival AUROC **0.745**.

## Defect B — the answer key is ~half circular, and it inflates T1

Of the 11 "essential" (positive) genes, only **5 come from the external assay** (experimental fitness < −2). The other **6 are model-labeled** — genes absent from the assay that the *model's own FBA* calls lethal, then scored by the *same* FBA ΔV. Those 6 are guaranteed top-ranked true positives.

- T1 AUROC on the full (mixed) set = **0.849**.
- T1 AUROC on **externally-labeled genes only** (drop the 6 circular positives) = **0.668**.

So AOP's recovery of *experimental* essentiality is a **weak pass (~0.67)**, not the headline 0.85. The external positive class is also tiny (n=5) — the *core* model has few glucose-essential genes matched to the assay, a real scope limit. **Fix:** score T1/T3 on external labels only (or report both prominently), and note the small external positive class.

## Corrected verdicts

- **T1 — WEAK PASS.** External-only AUROC ≈ 0.67 (just above the 0.65 falsification line); the 0.85 headline is inflated by circular labels. And even at full strength this is *inherited FBA competence*, which the prereg concedes — not an AOP-specific result.
- **T2 — PASS (the real win).** 13 synthetic-lethal isozyme pairs (acnA/acnB, rpiA/rpiB, tktA/tktB, pitA/pitB, cyd/cbd, crr/manXYZ) — real biological redundancy *E. coli* put there, individually invisible to single deletion, recovered only by the coalition/double-KO layer. Robust, flux-independent, not circular. This is the strongest, cleanest, genuinely-external AOP-specific result in the whole project.
- **T3 — SOFT PASS.** AOP's −ΔV beats flux-strength on essentiality ranking by ≈0.10–0.11, and the rival is blind to the T2 coalitions. Verdict holds, but the margin is solver-dependent and computed on the same partly-circular labels.
- **T4 — FALSIFIED (not partial).** Reproducible Spearman ≈ 0.53 (pFBA 0.528; 6/6 optimal-face draws 0.537). The prereg's own falsifier B ("Spearman > 0.5") fires. On real metabolism, structural strength and viability-importance are **positively correlated**, so the §11b toy model's "strength ⊥ viability" dissociation **does not generalize**.

## What it means (honest)

- The framework is **not sunk** — T2 is a genuine external, could-fail win: the coalition layer recovers real redundancy a single-axis reading cannot see, on data AOP did not set.
- But the toy model's headline **"strength ⊥ viability" dissociation is now externally falsified**, not merely "construction-forced" (as the CTMC re-run already showed). AOP must **stop claiming orthogonality/anti-ranking as general**. The defensible, narrower claim: viability-importance and flux-strength are *correlated but not identical*, and the viability/coalition reading adds value on redundancy (T2) and at the margin on ranking (T3).
- T1's essentiality recovery is real but weak once de-circularized, and is inherited from FBA regardless.

## Actions for the builder (Claude Science)

1. **Fix determinism:** switch the flux vector to pFBA (or fixed tie-break); re-run; report reproducible values.
2. **De-circularize:** score T1/T3 on external labels only (n=5 positives), or report both mixed and external-only with the external number as primary. Note the small positive class.
3. **Restate the results doc and §11b:** T4 is **falsified**, not partial. Lead with T2 as the result; report T1/T3 at their honest (weaker) strength; drop any general "strength ⊥ viability" claim.
4. Re-deposit; prime re-verifies.

## Governance note

This is the four-role split working exactly as intended: the builder's honest-but-favorable self-read ("3 of 4 pass, T4 partial") became, under independent prime re-run, "T2 solid, T1/T3 weak once de-circularized, T4 falsified, two defects to fix." No number a builder certifies on its own construction should be trusted until an independent party reproduces it — and here, several did not reproduce.
