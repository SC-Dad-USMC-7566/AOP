# AOP External-Ground-Truth Benchmark — Results (v1.1)

**Compiled:** 20 July 2026 by Claude (builder). Scored against the **frozen** preregistration v1.0 (unchanged — the pre-commitment). Non-canonical working document. **Supersedes the v1.0 results doc** (`REV_AOP_External_Benchmark_Results_v1_0.md`), which should be pruned.

**Why v1.1.** Prime's independent re-run (`AOP_Prime_Verification_ExternalBenchmark_20260719.md`) found the v1.0 numbers did not fully reproduce and two verdicts were stated too favorably. This version applies all three requested fixes and re-reports honestly. I confirmed prime's findings independently before fixing (details below).

**Reproduce:** `python aop_external_benchmark.py` (v1.1). Reads `MODEL_e_coli_core.xml` (MD5 `2fd9c214652195707526448954b88696`) and `EXT_KEY_price2018_fitness_Keio_BW25113.tsv` (MD5 `936b99da2cbf37baa70a2b2e1b629c93`) — same frozen inputs as v1.0. Output `external_benchmark_results.json` is now **byte-identical across repeated runs** (verified md5-stable over 3 runs).

---

## What changed from v1.0 (the three fixes)

**Fix 1 — determinism.** FBA has non-unique optimal flux vectors. v1.0 computed the rival's "coupling strength" and the T4 Spearman from `model.optimize()`, whose flux vector is solver-path dependent — so those metrics wandered run-to-run (prime saw T4 = 0.524 / 0.537 / 0.551; my own repeated v1.0 runs gave T1 = 0.818 / 0.851 / 0.871 and T4 = 0.474 / 0.511 / 0.536). Two sources, two fixes:
  - The WT flux vector is now **parsimonious FBA** (`cobra.flux_analysis.pfba`) — a unique flux distribution — so the rival strength and T4 are point values.
  - **All growth/viability/strength values are quantized to a fixed tolerance (1e-6) before any ranking or thresholding.** This was the second, subtler source: ~90 core genes are genuinely dispensable (ΔV = 0), but raw LP output puts ~1e-15 noise on those zeros, so `argsort`/`unique` split a true tie block into a noise-determined order — reshuffling AUROC ties and jittering **T1 and T3** as well (not just the flux metrics). Quantizing collapses the noise into a proper tie block. Verified robust: every reported value is identical across tolerance 1e-9 → 1e-3 (six orders of magnitude), confirming a clean gap between solver noise (~1e-15) and the smallest real signal (ΔV ≈ 3.6e-3). *This determinism defect was broader than "the T4/rival wander" — it touched every AUROC through the tie mechanism. Flagged for prime.*

**Fix 2 — de-circularization.** v1.0's 11 "essential" positives mixed **5 experimental-assay** essentials (glucose fitness < −2) with **6 model-labeled** ones (absent from the assay AND called lethal by the *model's own FBA*), then scored those 6 with the *same* FBA ΔV — circular, and guaranteed as top-ranked true positives. v1.1 reports the **external-assay-only labels (5 positives) as the PRIMARY result**, with the mixed-label version reported alongside as clearly-marked secondary.

**Fix 3 — honest re-report.** T4 is **falsified**, not "partial." Lead with T2. Report T1/T3 at true (weaker) strength. The general "structural strength ⊥ viability" claim is dropped.

---

## Headline (v1.1)

**One clean external win, one falsified claim, and two competence tests that are weak once de-circularized.**

- **T2 is the genuine, external, could-fail win.** AOP's coalition/Möbius layer recovers **13 synthetic-lethal isozyme pairs** — real biological redundancy *E. coli* encodes, individually invisible to single deletion and to the single-axis rival, on data AOP did not set. Robust, flux-independent, non-circular. This is the strongest genuinely-external AOP-specific result in the project.
- **T4 is falsified.** On real metabolism, structural strength and viability importance are **positively correlated** (reproducible Spearman **+0.61**; pFBA point value), firing the pre-registered falsifier (Spearman > 0.5). The §11b toy model's clean "strength ⊥ viability" dissociation **does not generalize**.
- **T1/T3 are weak once de-circularized.** On external-assay essentials only (n = 5), AOP's essentiality AUROC is **0.66** (a PARTIAL — above the 0.65 falsify floor, below the 0.75 pass bar), and the single-axis flux rival (**0.69**) actually edges it, so the **T3 margin goes negative (−0.02)** on the honest label set. The 0.85 / +0.10 headline was an artifact of the circular labels plus tie-noise. Even at full strength T1 is *inherited FBA competence*, which the prereg concedes.

---

## Scored population

116 core genes scored under mixed labels; 110 under external-only labels; 20 quarantined per prereg (absent from the RB-TnSeq assay AND FBA-viable). WT growth 0.8739 h⁻¹. The **external positive class is tiny (n = 5)** — the *core* model has few glucose-essential genes matched to the assay, a real scope limitation of the core (vs genome-scale) model. All statistics below are deterministic point values (pFBA + 1e-6 tie tolerance).

## Test-by-test (against frozen criteria)

| Test | Prereg criterion | v1.0 (withdrawn) | **v1.1 primary (external-only)** | v1.1 secondary (mixed) | Verdict |
|---|---|---|---|---|---|
| **T1** AOP viability recovers essentiality | AUROC ≥ 0.75 pass / < 0.65 falsify | 0.848 "PASS" | **0.66** | 0.85 | **PARTIAL** (weak) |
| **T2** real synthetic-lethal coalition, single-axis misses it | ≥ 1 pair | 13 pairs | **13 pairs** | 13 pairs | **PASS** (the win) |
| **T3** AOP beats rival by ≥ 0.10 | margin ≥ 0.10 | +0.10 "PASS" | **−0.02** | +0.10 | **FAIL** (primary) |
| **T4** strength ⊥ viability | Spearman ≤ 0.3 pass / > 0.5 falsify | +0.48 "PARTIAL" | **+0.61** | — | **FALSIFIED** |

Authoritative values are the frozen scorer's stored `external_benchmark_results.json`, not any hand-derived figure.

## What passed, honestly

**T2 — coalition recovery (13 synthetic-lethal pairs).** Every pair has both members individually dispensable (single-KO ΔV ≈ 0) but jointly lethal. They are real biochemical isozymes / redundant routes the model encodes from biology, not structure I designed: aconitase (*acnA*/*acnB*), ribose-5-P isomerase (*rpiA*/*rpiB*), transketolase (*tktA*/*tktB*), phosphate uptake (*pitA*/*pitB*), cytochrome oxidases (*cyd*/*cbd* family, 4 pairings), the mannose PTS (*crr*/*manXYZ*, 3 pairings), glutamine synthesis (*glnA*/*puuA*), and the anaplerotic *ppc*/*aceA* couple. Single-deletion viability importance ranks all members at zero; only the coalition (double-deletion Möbius) layer sees them. The flux-strength rival scatters these members across its mid-strength ranks and has no mechanism to flag a *pair* as jointly essential. This is the external-ground-truth analogue of the toy benchmark's redundant {A,B} pair — and here the redundancy was put there by *E. coli*, not by the modeler.

## What did not pass, honestly

**T4 — the dissociation is FALSIFIED (Spearman +0.61).** In the §11b toy model, structural strength and viability importance were engineered near-orthogonal (Spearman −0.67 — strength *anti*-ranked viability). On real *E. coli* core metabolism they are **positively correlated** (+0.61, reproducible): higher-flux genes are, more often than not, more viability-important. The pre-registered falsifier B (Spearman > 0.5) fires. The clean "strength anti-ranks viability" story is a **property of the constructed toy, not a law of persistent systems.** AOP must stop claiming orthogonality/anti-ranking as general. The defensible narrower claim: viability-importance and flux-strength are *correlated but not identical*, and the viability/coalition reading adds value **on redundancy (T2)** — not, on this system, on single-gene essentiality ranking.

**T1/T3 — weak once de-circularized.** External-only AUROC 0.66 (PARTIAL); the rival's 0.69 edges AOP, so T3's margin is −0.02 (FAIL on the honest labels). Even the mixed-label 0.85 is inherited FBA competence, not an AOP-specific result — the prereg said so. The small external positive class (n = 5) limits how much weight this can bear either way.

**A concrete FBA over-call (model honesty, unchanged from v1.0).** The 13 *nuo* genes (NADH dehydrogenase I) get ΔV = 0.76 from FBA but are experimentally dispensable (glucose fitness ≈ −0.3): the model cannot see the *ndh* bypass. AOP inherits this error from the metabolic model — the viability functional is only as good as the model it is evaluated on.

## Verdict (per ADR-003 scoping)

The benchmark could have failed and, on the honest scoring, **partly did — as designed.** AOP's one genuinely-external, AOP-specific, could-fail win survives: **T2**, recovering real redundancy a single-axis reading cannot see, on data AOP did not set. Its most quotable claim — the clean toy-model "strength ⊥ viability" dissociation — is **externally falsified** and must be withdrawn as a general claim. Its essentiality-ranking competence (T1/T3) is real but weak once the circular labels are removed, and is in any case inherited from FBA.

For a Perspective, the correct posture is: the four-target apparatus recovers coalition structure a single axis misses on a real system with an independent answer key (T2), while the framework explicitly **does not** claim the toy-model orthogonality holds in general (T4 falsified) and does not claim to beat a single flux axis at single-gene essentiality on this system (T1/T3). A pre-registered falsifier that fires is a result, not a defeat.

## Note for prime (canon / §11b)

Canon edits are prime's job; flagging the implication only. §11b currently presents the strength⊥viability dissociation as the benchmark's message. Given T4's external falsification, §11b's general framing needs to change from "strength anti-ranks viability" to "on the constructed toy the two are orthogonal by design; on real *E. coli* metabolism they are positively correlated (+0.61) — the dissociation is a toy property, and the externally-durable claim is the coalition/redundancy recovery (T2)." Prime applies the actual canon patch.
