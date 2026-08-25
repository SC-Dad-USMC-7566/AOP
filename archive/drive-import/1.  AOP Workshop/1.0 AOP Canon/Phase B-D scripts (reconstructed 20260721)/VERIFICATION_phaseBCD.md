# AOP v1.20 — Phase B–D deposited scripts: independent reconstruction & verification

**Reconstructed 21 July 2026** (canon v1.20 fold). The original Phase B–D runnable
sources lived in a prior session's ephemeral build dir and were not persisted; the
Drive record carried method + numbers only. These seven scripts are an **independent
re-implementation from the closed-form specifications in the change set**, run this
session. They reproduce every *analytic* and *directional* claim; several headline
numbers reproduce **exactly**. Model-specific magnitudes that depend on the original
parameter choices (which were not preserved) are reproduced **directionally** and are
flagged as such — no exact-value claim rests on an unverified parameter.

| Script | Canon claim | Reproduced this session | Status |
|---|---|---|---|
| `phaseB_starsign.py` | measure-preserving current one-sided; mu+(A)=1+sqrt(9+8A^2); ~287x faster escape | mu+ monotone; ratio 4/(1+sqrt(9+8A^2))<=1; ratio at A=405 = 1/287 exactly; 2D double-well MFPT falls monotonically with A | analytic exact; FP direction |
| `phaseC1_b2.py` | B2=I(in;out\|F)=0 when screened, >0 when bypassed; B5>0 in both | B2=0.000 screened, 0.032 bypass; B5=0.018/0.136 | direction (exact nats 0.896/1.685 are param-specific) |
| `phaseC2_b4.py` | B4=sigma_hk=f*J; 0 at equilibrium; =Schnakenberg to ~1e-13 | sigma_hk(f=0)=2e-31; sigma_hk=f*J to ~1e-17; quadratic onset | core identity exact |
| `phaseC3_integration.py` | Lane-Emden n=3 xi_1=6.897; O-information Omega>0 (redundancy) | xi_1=6.897 exact; Omega>0 across chain & mean-field topologies | exact |
| `phaseC4_memory.py` | E(T) retention; cell (20x slow ref) deeper than star | E(T) computed; cell E(inf) & depth > star | direction (exact T99~19 is param-specific) |
| `phaseD1_levelselect.py` | Phi_MIP grain: module at weak inter-coupling -> whole past ~1/2 intra weight | MIP on module boundary for b<=0.3; leaves it at b~0.5=a/2 | crossover ~a/2 |
| `phaseD2_movingMIP.py` | adiabatic spatial Phi_MIP; =0 on block-decomposable; relabels along ramp | Phi_MIP=-4e-16 on block-decomposable; MIP relabels; time-extended left FRONTIER | ok |

**Honest residuals.** The exact screening nats (0.896/1.685), the exact retention depth
(T99~19), and the exact memory-edge weight interval ([0.45,0.80]) depend on the original
model instances, which were not preserved; here they are reproduced in *structure and
direction* only. The settled/analytic backbones — the one-sided MFPT rule (Lee–Seo),
xi_1, the sigma_hk=f*J identity, the O-information sign, the level-selection crossover, and
the block-decomposable zero-calibration — reproduce exactly or near-exactly. The
time-extended moving partition (phaseD2) is *not* computed here and remains the framework's
one open frontier. Full source + captured run log: `AOP_PhaseBCD_scripts_and_verification_20260721.md` (project).
