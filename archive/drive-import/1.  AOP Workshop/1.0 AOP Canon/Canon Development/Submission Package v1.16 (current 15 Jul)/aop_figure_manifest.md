# AOP Figure Set — Manifest (Interface Focus submission)

Renumbered publication figure set for *The Architecture of Persistence*.
Every panel traces to a script in `scripts/`; all values below are computed, not asserted.
Canon: aop_canon_v1_16.md (version b5e9887b). Blueprint governs numbering.

## Main figures (6)

| New | Old | File | Script | Built | Key computed values (data-fidelity checks) |
|-----|-----|------|--------|-------|---------------------------------------------|
| **Fig 1** | Figure 1 | fig1_observer_grain.png | fig1_observer_grain.py | fresh | Driven ring N=210, p=0.62/q=0.10. σ_full=0.9488 = analytic (p−q)ln(p/q)=0.9488. Spatial grain 210→3 bins: σ swings **exactly 70.0×** (0.9488→0.0136), monotone; min σ=0.0136 **> 0** at every grain (law σ≥0 holds). |
| **Fig 2** | Figure 5 | fig2_fouraxis_shape.png | fig2_fouraxis_shape.py | fresh | Graphical-abstract. Illustrative B/D/M/I shape profiles (crystal, flame, spore). Canon rule honored: heights are *shape, not measured values*. B & I marked partition-dependent (italic). |
| **Fig 3** | Figure R + R★ (merged) | fig3_resolvability.png | fig3_resolvability.py (+3a/3b sources) | fresh merge | 8 persisters in resolvability plane; star focal VIF=3.733, drag=5.338. Panel b: star per-shell VIF from Lane–Emden n=3 operator, **max 3.733 = identical to plane placement** (internal consistency); mean-field caricature flat at ρ̄=0.059, max VIF 1.044. |
| **Fig 4** | Figure TF | fig4_topology_family.png | fig4_topology_family.py | deposited | Resolvability as a family indexed by coupling topology (mean-field/chain/lattice/modular/sparse) from topology_curves.npz. Aggregate/whole load-bearing in every case (var=1.000). |
| **Fig 5** | Figure LT | fig5_living_threshold.png | fig5_living_threshold.py | deposited | Living threshold: alive = load-bearing (weight>0.3) ∧ decoupled (sep>5). Cell model edge weight=0.701 @ sep=20 (ALIVE); star coupling weight=0.006 @ sep=2 and star intrinsic weight=0.551 @ sep=1 (not alive). Cutting cell model edge: V 0.667→0.20; cutting star coupling: V 0.98→0.975 (barely moves). |
| **Fig 6** | Figure MW | fig6_semantic_mask.png | fig6_semantic_mask.py | deposited (dpi 170→300) | Semantic mask on driven 3-state ring + inert spectator. σ=1.5175>0. Ring edge weights graded positive (e20 σ-weight=0.678, e12=0.521, e01=0.441); spectator e0S **exactly 0**. Detailed-balance control: σ=7.4e-32, all weights 0. |

## Supplementary figures (6)

| New | Old | File | Script | Built | Key computed values |
|-----|-----|------|--------|-------|---------------------|
| **Fig S1** | Figure 2 | figS1_integration_tradeoff.png | figS1_integration_tradeoff.py | deposited | Integration–resolvability trade-off: per-component weight blurs (√VIF, 1/√λ_min diverge) while aggregate stiff direction stays sharp. Third field: PID/Shapley attribution-order spread grows with integration. |
| **Fig S2** | Figure 3 | figS2_boundary_forces.png | figS2_boundary_forces.py | fresh | Which interactions make a boundary: EM screens ✓; strong confines ✗; weak short-ranged ✗; gravity unscreenable ✗ (anti-boundary; only boundary = causal horizon). |
| **Fig S3** | Figure 4 | figS3_two_boundaries.png | figS3_two_boundaries.py | fresh | One persister, two boundaries (H atom): EM screening skin (material/local/probeable/free) + causal light-cone (non-material/global/unscreenable). |
| **Fig S4** | Figure DM | figS4_DM_memory_floor.png | figS4_DM_memory_floor.py | deposited | D→M floor: σ>0 forces E=I(past;future)>0; converse fails (detailed balance σ=0 yet E>0). Coarse-graining hides current AND memory together (both →0). |
| **Fig S5** | Figure T | figS5_nonenergy_triangle.png | figS5_nonenergy_triangle.py | deposited | Non-energy triangle: 4000 random VAR(1) systems; every B/M/I corner reachable by construction. corr(B,M)=−0.048, corr(M,I)=−0.043, corr(B,I)=0.826. |
| **Fig S6** | Figure LT-T | figS6_LT_threshold.png | figS6_LT_threshold.py | deposited | Living threshold is architectural, not a timescale magnitude. Model-edge weight high & flat across star–cell window (2–20×): cell weight 0.788@2×, 0.717@20×, 0.383@100×; monotone decline, no knee. Discriminator is the decoupled-reference architecture (0/1), not separation magnitude. |

## Decisions
- **Fig 3 = merge of Figure R + Figure R★** into one two-panel figure (confirmed): the resolvability plane and the star that realizes the trough belong together.
- **LT-T kept standalone as Fig S6** (not a Fig 5 inset): the timescale sweep is too dense to inset without overloading Fig 5.
- **Fig 1 grain axis = spatial lumping on N=210**, giving exactly 70.0× (canon "roughly seventy-fold"). Temporal per-step σ subsampling was rejected: it aliases badly at large τ (non-monotone, unusable as a clean grain axis).
- **Four figures built fresh** (no deposited script existed): Fig 1, Fig 2, Fig S2, Fig S3.
- **Fig 6 (MW) re-rendered at 300 dpi** (deposited script saved at 170).

## Data provenance
- persister_rows.pkl (8 rows) → Fig 3a
- star_homology_arrays.npz (40 shells) → Fig 3b
- topology_curves.npz → Fig 4
- Figs 1, 2, S2, S3 are self-contained (parameters in-script).
- Figs 5, 6, S1, S4, S5, S6 self-contained in their deposited scripts.

## Reproduction
Each `scripts/<name>.py` writes its PNG at 300 dpi and uses the project `figure_style` helper
(`apply_figure_style`). Fig 3 reads its two data files via `PKL_ROWS` / `NPZ_HOM` env vars.
