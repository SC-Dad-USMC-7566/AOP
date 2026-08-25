# AOP handoff to OAI (outside critic) — external benchmark, v1.1

**From:** Claude Science (builder) · **Date:** 20 July 2026 · **Re:** the external *E. coli* / Keio benchmark, now fixed and re-verified

You are the outside critic on AOP. The four-role split is: builder proposes, prime verifies by independent re-run, **you attack**, Ben decides. Nobody grades their own homework. This note tells you what the external benchmark is, where every file lives on Drive, and where the soft spots are — attack them.

---

## The mission I was given

Build a benchmark with an **external answer key AOP could actually fail** — a test whose ground truth is set by biology and experiment, not by the modeler. (The prior §11b "competence check" was forced-by-construction; prime and Ben wanted a real could-fail test.) Concretely: take the standard *E. coli* core metabolic model, score AOP's viability functional (ΔV under gene deletion) and its coalition/Möbius layer against a **published experimental gene-fitness assay** (Price et al. 2018 RB-TnSeq, glucose minimal), with four tests pre-registered *before* scoring:

- **T1** — AOP's viability ΔV recovers experimental essentiality (AUROC).
- **T2** — the coalition layer finds real synthetic-lethal redundancy a single-axis reading misses.
- **T3** — AOP beats a single-axis flux-strength rival on essentiality ranking (margin ≥ 0.10).
- **T4** — structural strength and viability importance are ~orthogonal (the §11b toy's headline claim), tested on real metabolism.

I built and scored it (v1.0). Prime independently re-ran it and found: design good, but the numbers didn't fully reproduce, the answer key was ~half circular, and one verdict was too favorable. I applied prime's three fixes → **v1.1**, the version this handoff describes.

## What v1.1 found (the honest result)

| Test | v1.1 result (external-only primary) | Verdict |
|---|---|---|
| **T1** essentiality AUROC | 0.66 | **PARTIAL** (weak) |
| **T2** synthetic-lethal coalitions | 13 real isozyme/redundancy pairs | **PASS — the genuine external win** |
| **T3** AOP − rival margin | −0.02 (rival flux-strength edges AOP) | **FAIL** on honest labels |
| **T4** Spearman(strength, ΔV) | **+0.61** | **FALSIFIED** (pre-registered falsifier >0.5 fires) |

**Plain reading:** AOP's one clean, external, could-fail win is **T2** — its coalition layer recovers redundancy (aconitase, transketolase, ribose-5-P isomerase, the mannose PTS, cytochrome oxidases, etc.) that single deletion and the flux rival are both blind to, on redundancy *E. coli* put there, not me. But the toy model's quotable "structural strength ⊥ viability" dissociation is **externally falsified** — on real metabolism the two are positively correlated (+0.61) — and once the answer key is de-circularized, AOP does **not** beat a simple flux axis at single-gene essentiality (T3 fails, T1 weak). A pre-registered falsifier fired; we're reporting it as a result, not softening it.

## The three fixes (v1.0 → v1.1), so you can check them

1. **Determinism.** FBA has non-unique optimal flux vectors, so v1.0's rival strength and T4 wandered run-to-run. Fixed with parsimonious FBA (pfba) for the flux vector **plus** quantizing all growth/ΔV/strength to 1e-6 before ranking (the ~90 genuinely-zero-ΔV genes carried ~1e-15 LP noise that reshuffled AUROC ties — this jittered T1/T3 too, broader than first flagged). Output JSON is now byte-identical across runs; values are stable across tolerance 1e-9→1e-3.
2. **De-circularization.** v1.0's 11 "essential" positives mixed 5 experimental-assay essentials with 6 the *model's own FBA* called lethal, then scored those 6 with the same FBA — circular, inflating T1 from ~0.66 to 0.85. v1.1 leads with the **5 external-assay positives only**; mixed-label kept as secondary.
3. **Honest re-report.** T4 = FALSIFIED (not "partial"); T2 led as the win; the general "strength ⊥ viability" claim dropped.

## Where everything is on Drive

**Frozen inputs** (unchanged; MD5s pinned — the pre-commitment you're scoring against):
- Model: `MODEL_e_coli_core.xml` — MD5 `2fd9c214652195707526448954b88696`
- Answer key: `EXT_KEY_price2018_fitness_Keio_BW25113.tsv` — MD5 `936b99da2cbf37baa70a2b2e1b629c93`
- Preregistration: `REV_AOP_External_Benchmark_Preregistration_v1_0.md` (frozen, NOT edited)
- Design: `REV_AOP_External_Benchmark_Design_v1_0.md`; key provenance: `EXT_KEY_provenance.md`

**v1.1 deliverables** (Task-2 folder, `1su77Xw4yR8ga-O5aH5j7Y4WhA2jnTtcV`):
- `aop_external_benchmark.py` — the fixed, deterministic scorer (`python aop_external_benchmark.py` reproduces everything)
- `external_benchmark_results.json` — the authoritative stored values (md5 `c9fb7ca4…`)
- `REV_AOP_External_Benchmark_Results_v1_1.md` — the full results writeup
- `REV_AOP_External_Benchmark_ChangeNote_v1_0_to_v1_1.md` — one-page v1.0→v1.1 diff
- `fig_external_benchmark.png` — the corrected figure (T4 correlation + T2 coalition win; honest external-only ROC)

**Verification record** (top of AOP folder): `AOP_Prime_Verification_ExternalBenchmark_20260719.md` — prime's independent re-run and the source of the three fixes.

**Note:** superseded v1.0 copies (results doc, old script/json/fig) are still on Drive pending prime's prune — ignore anything tagged v1.0; the JSON's stored MD5 `c9fb7ca4…` identifies the current one.

## Where to aim (I want these attacked)

1. **Is T2 actually AOP-specific, or just double-deletion FBA?** The coalition layer is a Möbius/double-KO reading. Argue that any double-deletion scan finds these isozymes with no AOP machinery needed — is the "coalition" framing doing real work, or relabeling standard synthetic-lethality analysis?
2. **n=5 is tiny.** The external positive class is 5 genes. Every external-only AUROC (T1 0.66, rival 0.69) rides on 5 positives. Is any of T1/T3 statistically distinguishable from noise at n=5? I claim T3 "fails" at −0.02 — is that margin even meaningful at this n?
3. **The core model is the wrong scope.** *e_coli_core* has ~137 genes; the assay covers the genome. The 20 quarantined genes and the tiny positive class are artifacts of using the core model. Does the whole benchmark need the genome-scale model (iML1515) to say anything — and would AOP look better or worse there?
4. **Is T4's falsification fatal to the framework, or just to one sentence?** I claim it only kills the "strength ⊥ viability is general" claim while T2 survives. Push on whether the toy model's entire construction is now suspect if its headline dissociation doesn't generalize.
5. **The nuo over-call.** FBA gives 13 *nuo* genes ΔV=0.76 though they're experimentally dispensable (ndh bypass). AOP inherits every FBA error. How much of T1's "competence" is just inherited FBA, and does AOP add anything the underlying model doesn't?

Attack freely — a benchmark that survives you is worth more than one that doesn't. — Builder
