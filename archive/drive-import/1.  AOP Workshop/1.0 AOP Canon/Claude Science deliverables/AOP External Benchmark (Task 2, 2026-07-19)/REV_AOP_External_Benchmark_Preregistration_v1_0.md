# AOP External-Ground-Truth Benchmark — Preregistration (v1.0, FROZEN)

**Compiled:** 19 July 2026 by Claude (builder). **Frozen before any scoring was run.**
**Governance:** builder proposes (this doc); prime verifies by independent re-run; ChatGPT attacks; Ben decides. Nobody grades their own homework.

## No-peek attestation

At the moment of freezing this preregistration, the following have been computed and seen:
- Wild-type FBA biomass flux (0.8739 h⁻¹) — a single scalar, needed to define the lethality threshold.
- The external key's fitness *distribution* (median ≈ 0, 96 of 3789 genes with mean glucose fitness < −2) — i.e. class balance of the answer key. This is the answer key itself, not the model's performance on it.

The following have **NOT** been computed or seen: per-gene ΔV; the ΔV-vs-fitness classification score; any double-knockout / Möbius result (the one exploratory `double_gene_deletion` call was **interrupted before it printed any output**); rival flux magnitudes; any correlation or AUROC. The predictions below are made blind to all model performance.

## Fixed analysis choices (locked)

- **Model:** `MODEL_e_coli_core.xml`, MD5 `2fd9c214652195707526448954b88696`. Medium: default glucose minimal, aerobic (EX_glc__D_e lower bound −10, EX_o2_e open).
- **Viability V:** FBA biomass objective, solved with the bundled GLPK/`optimize()`. Deterministic (LP, no seed needed). Double-KO uses cobrapy `double_gene_deletion`.
- **ΔV(gene):** (V_wt − V_knockout) / V_wt, GPR-aware (cobra `single_gene_deletion`).
- **Lethality threshold:** knockout is "FBA-lethal" if V_knockout < 0.01 · V_wt.
- **External binary label** (dispensable vs experimentally-required):
  - *experimentally-required* = (b-gene **absent** from the RB-TnSeq assay table) **AND** FBA-lethal; **OR** (present with mean glucose fitness < −2).
  - *dispensable* = present with mean glucose fitness ≥ −2.
  - *quarantined, not scored* = absent-from-assay but FBA-viable (ambiguous coverage).
- **Rival (coupling strength):** for each gene, Σ|WT flux| over the reactions in its GPR. Higher = "more important" under the single-axis reading.
- **Primary metric:** AUROC of the ranking (−ΔV for AOP, coupling strength for rival) as a classifier of the external binary label, over all scored core genes.

## Predictions and pass/fail criteria

**T1 — AOP viability recovers external essentiality.**
*Predict:* AUROC(−ΔV) ≥ 0.75.
*Pass:* ≥ 0.75. *Weak pass:* 0.65–0.75. *FALSIFIED:* < 0.65 (AOP's viability functional does not recover the external answer key on real metabolism).

**T2 — a real synthetic-lethal coalition exists and single-axis viability misses it.**
*Predict:* ≥ 1 gene pair with ΔV(g₁) ≈ ΔV(g₂) ≈ 0 (each below the lethal threshold alone) but ΔV(g₁,g₂) ≥ 0.5 (jointly lethal), i.e. Möbius h > 0. At least the top such pair corresponds to a documented isozyme / redundant-route relationship (named post hoc from the model's gene annotations, not invented).
*Pass:* ≥ 1 such pair found and single-deletion importance ranks both members at ~0. *FALSIFIED / inconclusive:* zero FBA synthetic-lethal pairs in the core model (coalition layer has nothing to recover here — reported honestly, not spun).

**T3 — AOP beats the single-axis rival, in the direction the toy model claims.**
*Predict:* AUROC(−ΔV) − AUROC(coupling-strength) ≥ 0.10, **and** the rival scores at least one synthetic-lethal pair member as high individual importance (i.e. the rival cannot see the coalition).
*Pass:* both hold. *Partial:* AOP wins by < 0.10. *FALSIFIED (falsifier A):* rival AUROC ≥ AOP AUROC — on real metabolism the single strength axis does as well or better, and AOP's dissociation advantage does not hold here.

**T4 — external-validity check on the headline dissociation (the toy model's central claim, exposed to data).**
*Predict:* structural strength (flux magnitude) and viability importance (ΔV) are **dissociated** — Spearman(coupling-strength, −ΔV) ≤ +0.3 across scored genes; specifically, the highest-flux genes are not simply the essential ones.
*Pass:* Spearman ≤ +0.3. *FALSIFIED (falsifier B):* Spearman > +0.5 — flux magnitude tracks essentiality on real metabolism, so the toy-model "strength ⊥ viability" dissociation does **not** generalize. This is the benchmark's most important possible failure and will be reported as such if it occurs.

## Honest-reporting commitments

1. If any Tn is falsified, the results document states it plainly in the headline, not buried. A reported failure is the intended, valuable outcome if that is what the data give.
2. No threshold, medium, or label rule will be changed after seeing a score to rescue a prediction. If a definitional choice is genuinely ambiguous, both are reported.
3. The rival is scored with its own honest best definition, not a strawman.
4. Prime re-runs the frozen code against the frozen key and model; the builder's numbers stand only if prime reproduces them.

## Falsification summary (what would embarrass AOP here)

- T1 false → viability functional doesn't recover real essentiality.
- T2 false → no coalition structure to find on this system.
- T3 false → single strength axis matches/beats AOP on real data.
- T4 false → the headline strength⊥viability dissociation is a toy-model artifact that doesn't survive contact with metabolism.

Any of these is a real, pre-committed way for the benchmark to fail.
