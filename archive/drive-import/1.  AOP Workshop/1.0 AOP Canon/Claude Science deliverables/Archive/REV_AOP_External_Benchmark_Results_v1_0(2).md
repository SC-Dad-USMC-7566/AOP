# AOP External-Ground-Truth Benchmark — Results (v1.0)

**Compiled:** 19 July 2026 by Claude (builder). Scored strictly against the frozen preregistration (v1.0), which was deposited on Drive before this scoring was run. Non-canonical working document.

**Reproduce:** `python aop_external_benchmark.py` (reads `MODEL_e_coli_core.xml`, MD5 `2fd9c214652195707526448954b88696`, and `EXT_KEY_price2018_fitness_Keio_BW25113.tsv`, MD5 `936b99da2cbf37baa70a2b2e1b629c93`). Deterministic LP — no seed. cobra 0.31.1.

## Headline

**Mixed result, reported as such.** AOP does the two things it claims — its viability functional recovers experimental essentiality (T1 pass), and its coalition layer recovers real synthetic-lethal redundancy that a single-axis reading cannot see (T2 pass). But the toy model's *clean* "structural strength ⊥ viability" dissociation **does not fully survive contact with real metabolism**: flux strength and viability importance are moderately correlated here (Spearman +0.48, vs ≈0 in the §11b toy), and AOP's margin over the rival is exactly at — not clearly above — the preregistered bar. The framework's competence claims hold; its most quotable dissociation claim is shown to be partly a toy-model artifact.

## Scored population

116 core genes scored (11 experimentally essential/strongly-deleterious, 105 dispensable); 20 genes quarantined per prereg (absent from the RB-TnSeq assay but FBA-viable — ambiguous coverage, not scored). WT growth 0.8739 h⁻¹.

## Test-by-test (against frozen criteria)

| Test | Prediction | Result | Verdict |
|---|---|---|---|
| **T1** AOP viability recovers essentiality | AUROC(−ΔV) ≥ 0.75 | **0.848** | **PASS** |
| **T2** real synthetic-lethal coalition exists, single-axis misses it | ≥1 pair, both ΔV≈0 alone, joint lethal | **13 pairs**, all genuine isozymes | **PASS** |
| **T3** AOP beats rival by ≥0.10 AND rival misses coalitions | margin ≥0.10 | margin **0.0999**; coalition half holds | **PARTIAL** (margin just under bar) |
| **T4** strength ⊥ viability (Spearman ≤0.3) | ≤0.3 | **+0.482** | **PARTIAL** (not falsified >0.5, but well above 0.3) |

## What passed, honestly

**T1 — viability recovers essentiality (AUROC 0.848).** AOP's ΔV, read as the drop in the system's own viability functional under mechanism deletion, ranks the experimentally essential genes above dispensable ones at 0.85 AUROC — consistent with the known ~0.85 accuracy of FBA gene-essentiality. This is inherited competence, not a surprise, and the prereg said so.

**T2 — coalition recovery (13 synthetic-lethal pairs).** Every pair has both members individually dispensable (single-KO ΔV≈0) but jointly lethal (ΔV=1.0, Möbius h=+1.0). They are **real biochemical isozymes / redundant routes the model encodes from biology, not structure I designed**: aconitase (acnA/acnB), ribose-5-phosphate isomerase (rpiA/rpiB), transketolase (tktA/tktB), phosphate uptake (pitA/pitB), cytochrome oxidases (cyd/cbd), and the mannose PTS (crr/manXYZ). Single-deletion viability importance ranks all of them at zero; only the coalition (double-deletion Möbius) layer sees them. This is the external-ground-truth analogue of the toy benchmark's redundant {A,B} pair — and here the redundancy was put there by *E. coli*, not by me.

**T3, coalition half.** The rival (flux strength) scatters the synthetic-lethal members across its strength ranks 11–117 of 136 — it has no way to flag a pair as jointly essential, exactly as predicted. On the coalition axis AOP is strictly better.

## What did not pass, honestly

**T3 — AUROC margin (0.0999, just under 0.10).** AOP's 0.848 beats the rival's 0.748 by essentially exactly the preregistered 0.10 — 0.0999 before rounding. I will not round this up to "pass." The single-axis strength rival is a **respectable** essentiality classifier on real metabolism (AUROC 0.75), much better than it was on the toy model. AOP wins, but not by the margin I predicted.

**T4 — the dissociation is only partial (Spearman +0.48).** This is the important negative finding. In the §11b toy model, structural strength and viability importance were engineered to be near-orthogonal (Spearman −0.67 — strength *anti*-ranked viability). On real *E. coli* core metabolism they are **moderately positively correlated** (+0.48): high-flux genes are, more often than not, also more viability-important. The clean "strength anti-ranks viability" story is a property of the constructed toy, not a law of persistent systems. It is not *reversed* on real metabolism (the correlation is far from +1, and the essential genes are not simply the highest-flux ones — see the figure), but the orthogonality is substantially weakened.

**A concrete FBA over-call (model honesty).** The 13 *nuo* genes (NADH dehydrogenase I) get ΔV=0.76 from FBA but are experimentally dispensable (glucose fitness ≈ −0.3): the model cannot see the *ndh* bypass. AOP inherits this error from the metabolic model — a reminder that the viability functional is only as good as the model it is evaluated on.

## Verdict (per ADR-003 scoping)

The benchmark could have failed and partly did. AOP's **competence claims survive an external answer key it did not set**: it recovers essentiality (T1) and recovers real redundancy invisible to a single axis (T2, T3-coalition). Its **headline dissociation claim is externally qualified**: on real metabolism structural strength and viability importance are moderately correlated (T4), so "structural strength anti-ranks viability" is a toy-model result, not a general one. That qualification is a genuine finding this benchmark contributes — and exactly the kind of thing a competence-only benchmark could never have surfaced.

For a Perspective: this is a favorable-but-honestly-bounded external validation, not an adjudication. The correct manuscript posture is that the four-target apparatus recovers structure a single axis misses on a real system with an independent answer key, while explicitly not claiming the clean toy-model orthogonality holds in general.
