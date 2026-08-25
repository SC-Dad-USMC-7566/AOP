# AOP T2 Specificity Control — Results (v1.0)

**Compiled:** 20 July 2026 by Claude (builder). Scored against the frozen prereg `REV_AOP_T2_Control_Preregistration_v1_0.md` (deposited on Drive at 17:37 UTC, **before** this run). Non-canonical working document.

**Reproduce:** `python aop_T2_doubleKO_control.py` (reads `MODEL_e_coli_core.xml`, MD5 `2fd9c214652195707526448954b88696`, and the frozen `external_benchmark_results.json` for the 13 AOP pairs). Deterministic — output `T2_control_results.json` is byte-identical across runs (md5 `351e55ca…`, verified over 3 runs). cobra 0.31.1.

---

## Headline — the control fired. T2 is not AOP-specific on detection.

The referee-killer question was: does a plain double-knockout FBA synthetic-lethal screen, with **no** AOP coalition/viability/Möbius machinery, already recover the 13 pairs AOP flags? **It does — all 13, exactly, with nothing added and nothing missed.** Per the pre-registered criterion, **T2's AOP-specificity is NOT established.** T2 should be reported as *"AOP reproduces standard synthetic-lethal detection,"* not as a unique AOP win.

This is a pre-registered control that dissolved the framework's one genuine external win. Reporting it plainly, same discipline as T4.

## Results against the frozen criterion

The prereg said AOP-specificity is **NOT established** if all three hold. All three hold:

| Frozen condition | Result | Holds? |
|---|---|---|
| Matched-threshold plain screen (A) recovers **all 13** AOP pairs (AOP ⊆ A) | 13/13; AOP ⊆ A = **True** | **yes** |
| AOP surfaces no SL structure the plain screen misses | A-extra-not-in-AOP = ∅; A-missed = ∅ | **yes** |
| Möbius-h ranking is monotone with plain joint-drop (no ranking advantage) | identical order (h ≡ joint_drop; both singles ≈ 0) | **yes** |

→ **T2 AOP-specificity: NOT ESTABLISHED.**

## The three screens

**Screen A — matched threshold (primary; isolates "machinery").** Plain double-KO FBA over all 90 individually-viable genes: flag (i,j) if joint ΔV ≥ 0.5. Same operational thresholds as the AOP T2 layer, but raw FBA growth only — no viability functional, no Möbius. **Result: exactly the same 13 pairs.** AOP ⊆ A, A ⊆ AOP. The "coalition/Möbius" quantity h = ΔV_joint − ΔV_g1 − ΔV_g2 adds nothing: for every one of these pairs both singles have ΔV ≈ 0, so h collapses to the raw double-KO drop that Screen A already computes.

**Screen B — strict SL (context).** Standard essentiality cutoff τ = 0.01·WT: each single viable (> τ), double lethal (≤ τ). Finds **9** pairs — recovers 9 of the 13, missing the four cytochrome-oxidase pairs (*cydA/B* × *cbdA/B*), which sit at joint ΔV ≈ 0.76 (severe but not fully lethal). **This is not an AOP advantage:** Screen A, a plain screen at the ≥0.5 threshold, recovers those four too. The difference between B and the 13 is entirely the lethality threshold (0.5 vs 0.99 joint drop), a modeling choice available to any plain screen — exactly the interpretation frozen in the prereg before running.

**Screen C — ranking.** Ranking the 13 by AOP Möbius-h vs by plain joint-growth-drop gives the **identical order** (nine pairs tied at drop 1.0, four cyd/cbd pairs at 0.7578). The coalition layer confers no ranking advantage.

## What this does and does not mean (honest)

**What it kills.** The claim that T2 is an *AOP-specific* result. It is not: any double-KO FBA screen at the same threshold finds the identical 13 pairs, and the Möbius/viability framing does no detection or ranking work over raw joint growth. Combined with the critic's Q4 — how much is inherited FBA — the answer here is: **on T2, essentially all of it.** The pairs are real biology (isozymes/redundant routes the model encodes), and FBA double-KO finds them; AOP's apparatus relabels that, it does not add to it.

**What survives.** The biology is still real — these are genuine synthetic-lethal isozyme pairs in *E. coli*, recovered on an external model AOP did not build. What is now clear is that **recovering them requires only standard double-KO FBA**, so they cannot carry an AOP-specific claim. AOP's coalition layer is, on this system, a re-description of double-deletion synthetic-lethality — a legitimate lens, but not a capability a plain screen lacks.

**Net effect on the external benchmark.** After the v1.1 fixes and this control, the honest external-benchmark scorecard is:
- **T1** essentiality — weak (external-only AUROC 0.66), and inherited FBA competence.
- **T2** coalition redundancy — real biology, but **not AOP-specific** (this control); reproduced by plain double-KO FBA.
- **T3** vs single-axis rival — **fails** on honest labels (rival edges AOP).
- **T4** strength ⊥ viability — **falsified** (Spearman +0.61 on real metabolism).

So the external benchmark, fully hardened, does not currently establish an AOP-specific advantage on this system. That is the result. A genome-scale reconstruction (iML1515) is the noted next step *before* any strong T2 claim — but it is not tasked here, and it would not change this control's finding on the core model.

## Note for prime (canon / §11b)

Canon edits are prime's job; flagging the implication only. Any canon text that presents the *E. coli* T2 result as an AOP-specific win (the coalition layer "seeing" what a single axis cannot) needs to be qualified: on the core model, a plain double-KO FBA screen recovers the identical 13 pairs, so T2 demonstrates that AOP's coalition reading is *consistent with* standard synthetic-lethal detection, not that it exceeds it. Prime applies the actual patch.
