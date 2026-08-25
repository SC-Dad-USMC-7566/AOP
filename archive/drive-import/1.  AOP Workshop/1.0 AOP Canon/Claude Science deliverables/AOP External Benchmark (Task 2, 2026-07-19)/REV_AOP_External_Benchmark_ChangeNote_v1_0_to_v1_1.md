# External Benchmark — change note, v1.0 → v1.1 (builder, 20 Jul 2026)

Applied prime's three fixes to the frozen-prereg scoring (prereg itself UNCHANGED):

1. **Determinism** — WT flux vector now `pfba` (unique), and all growth/viability/strength values quantized to 1e-6 before ranking/thresholding (kills ~1e-15 LP tie-noise that was reshuffling zero-ΔV genes). Output JSON is now byte-identical across runs. *Note: the tie-noise moved T1/T3 too, not only the rival/T4 — the determinism defect was broader than stated.*
2. **De-circularization** — T1/T3 now scored on external-assay labels only (5 positives) as PRIMARY; mixed-label (11 positives) kept as clearly-marked secondary.
3. **Honest re-report** — T4 stated FALSIFIED (reproducible Spearman +0.61 > 0.5 falsifier); T2 led as the genuine external win; general "strength ⊥ viability" claim dropped.

**Net verdict change:** T2 PASS (unchanged, the win). T4 PARTIAL → **FALSIFIED**. T1 0.85 "PASS" → **0.66 PARTIAL** (external-only). T3 +0.10 "PASS" → **−0.02 FAIL** (external-only; rival edges AOP on the 5 assay essentials).

**Superseded (prune):** REV_AOP_External_Benchmark_Results_v1_0.md; the v1.0 external_benchmark_results.json and fig_external_benchmark.png (regenerated).
**Delivered (one copy each):** aop_external_benchmark.py (v1.1), external_benchmark_results.json (regenerated), fig_external_benchmark.png (regenerated), REV_AOP_External_Benchmark_Results_v1_1.md, this change note.
