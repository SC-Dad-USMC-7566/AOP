# Prime Verification — T2 Control + v1.1 Scorecard (external E. coli benchmark)

**Compiled:** 20 July 2026 by Claude (prime). Independent re-run of the T2 specificity control and the v1.1 benchmark verdicts. Non-canonical record.
**Inputs:** model + key MD5s match (`2fd9c214…`, `936b99da…`). cobra 0.31.1.

## Verdict: the control fired, and it reproduces exactly. Confirmed.

**T2 specificity control — reproduced byte-for-byte.**
- My independent run of `aop_T2_doubleKO_control.py` is **md5-identical** to the deposited `T2_control_results.json` (`351e55ca…`), and deterministic across runs.
- Screen A is a genuine independent full screen: `double_gene_deletion` over all 90 individually-viable genes (~4,000 pairs), threshold-matched (joint drop ≥ 0.5). It surfaces **exactly AOP's 13 pairs — AOP ⊆ A, A-extra = 0, A-missed = 0.**
- Premise verified: all 13 pairs have both singles ΔV≈0 (sole exception ppc/aceA at 0.0036), so the Möbius interaction h ≈ joint-drop for every pair. The coalition/viability framing does **no detection or ranking work** beyond a standard double-KO synthetic-lethal screen.
- Screen B (strict τ) finds 9/13, missing the four cyd/cbd oxidase pairs — but those are recovered by the plain Screen A at the matched ≥0.5 threshold, so B's miss is a threshold choice, not AOP machinery (interpretation frozen before the run).

**Conclusion:** T2's AOP-specificity is **not established**. The one apparent external win dissolves into ordinary FBA synthetic-lethal detection.

**T3 / T4 — independently recomputed from the model (not from deposited numbers):**
- T3 external-only: AOP AUROC **0.6648**, rival **0.6857**, margin **−0.021** — exact match to v1.1. AOP loses to the plain flux-strength rival on honest labels. **T3 fails.**
- T4: independent Spearman(strength, ΔV) = **0.579** (deposited 0.614); both > 0.5. **T4 falsified** (verdict robust; exact value has minor residual flux-vector sensitivity).
- v1.1 fixes confirmed present: `flux_method = pfba` (determinism), external-only labels primary (de-circularized).

## Fully hardened scorecard (E. coli core, fair baselines, honest labels)

| Test | Result |
|---|---|
| T1 essentiality | Weak (AUROC ≈ 0.66 external, n_pos = 5); inherited FBA competence, not AOP-specific |
| T2 synthetic-lethal | Real biology, but **reproduced exactly by a plain double-KO screen** — not AOP-specific |
| T3 vs rival | **Fails** — plain flux-strength rival edges AOP (margin −0.021) |
| T4 strength ⊥ viability | **Falsified** — Spearman ≈ 0.58–0.61 (> 0.5) |

**On this system, with fair baselines, AOP demonstrates no AOP-specific empirical advantage.**

## Governance note (the four-role split, working at full depth)

- **Builder (Science)** built and ran the control that dissolved its own earlier "win," and reported it honestly. Correct conduct.
- **Critic (Aster)** returned a directional review without re-running, and called T2 "the strongest evidence for AOP" — the opposite of what the control shows. A review is not a reproduction; her T2 claim does not survive the re-run.
- **Prime (this session)** re-ran everything and confirms the control (md5-exact), T3, T4, and the fixes. This also **corrects prime's own earlier error**: two sessions ago prime called T2 "the real win / genuinely AOP-specific." That was wrong — the fair baseline is a plain SL screen, which matches AOP exactly. Logged so the mistake isn't repeated.

## Implication for canon (prime's job; not yet applied)

Any canon text presenting the E. coli T2 result — or any benchmark result — as an AOP-specific advantage must be corrected. The honest state: the external benchmark validates that AOP's quantities *recover known structure* (competence), and **falsifies** the stronger "strength ⊥ viability" dissociation, while showing **no method-level advantage** over standard FBA/SL baselines on this system. This pushes AOP back toward its charter identity: an organizing reframing of existing science, not a distinctive method.
