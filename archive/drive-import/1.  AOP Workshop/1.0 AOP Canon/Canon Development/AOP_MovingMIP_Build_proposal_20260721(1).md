# AOP Moving-MIP Build — Proposal

**Time-extended Φ_MIP over a window that straddles a relabeling transition**

- **Author lane:** Claude Science (builder). This is a **proposal** for Prime to verify and Ben to decide — not canon.
- **Date:** 21 July 2026
- **Against canon:** `AOP_CANON_MASTER_v1.20.md` (Canon folder `1.0 AOP Canon`, mod 2026-07-21 14:14 UTC — the live master; the identically-named copy in the `Retired` subfolder was ignored).
- **Charter:** `AOP_Charter_(V6).md` (Drive master, mod 2026-07-19).
- **Lane discipline:** syntactic layer only (Φ_MIP, coupling graph). No semantic-mask, star, or provenance quantities are touched. One item that *would* force a change elsewhere is flagged for Prime at the end (§7); it is not made here.
- **Deliverables:** this file + a runnable `phaseE_movingMIP.py` (self-contained, closed-form, matching the Phase B–D deposit style) + figure `phaseE_movingMIP_fig.png`.

---

## 1. The problem, exactly as canon states it

Canon §13a (and, inheriting it, the §9a collective living-threshold and the §4 individuation frontier) names the framework's *principal open problem*:

> "What remains genuinely open (FRONTIER) is the *time-extended* Φ_MIP over a developmental window, and the obstacle is now nameable: the MIP is a discrete argmin that relabels across a transition, so no single time-extended partition scores a window straddling it, and the temporal (effects-based) alternative inherits the §5 excess-entropy definedness hole (no stationary 'future')."

There are two dead ends, and both are real:

1. **The argmin dead end.** Φ_MIP(Σ) = min over bipartitions of the integration deficit Φ(P) = TC(whole) − TC(A) − TC(B). Over a developmental window the covariance Σ(t) moves through a transition, and the *arg*min jumps from one partition to another. No single fixed partition is the MIP on both sides, so scoring the window with any one partition mis-scores at least one side.
2. **The effects-based dead end.** The natural alternative — score the window by a temporal/predictive-information quantity — inherits the §5 hole: the excess entropy E = I(past; future) is *defined only for a stationary process* [Crutchfield & Feldman 2003], and a developmental window has no stationary "future." Crossing the non-stationarity, E does not merely change value; it loses its definition.

The adiabatic *spatial* half is already done (canon §13a; `phaseD2_movingMIP.py`): the instantaneous Φ_MIP[Σ(t)] is well-posed and its MIP relabels at a kink. What is missing is a construction that scores a **window** straddling that relabeling.

---

## 2. Charter's first move: this is a solved problem in three fields

Per charter discipline ("don't create when you can cite; be skeptical of anything that looks new; the strongest outcomes are where AOP's 'new' prediction is a known result independently found by three fields"), the first move was a wide literature search, not a construction. The problem — *score a functional over a window while the optimal partition moves through a transition* — is **already solved**, and the strongest-outcome signature applies: the same object appears independently in three peer-reviewed literatures.

### 2.1 Nonautonomous dynamical systems — the inflated dynamic Laplacian (load-bearing precedent)

**Froyland & Koltai, "Detecting the birth and death of finite-time coherent sets," *Comm. Pure Appl. Math.* 76 (2023).** DOI `10.1002/cpa.22115` (also arXiv:2103.16286v4). **Read in full** (construction, spectrum, and 1-D surrogate sections; the passages relied on are cited below).

Their problem is verbatim ours with "coherent set" for "individual" and "flow" for "developmental ramp": standard (Lagrangian) coherent-set methods require an object to stay coherent *throughout* the chosen window, so an object that is born or dies *inside* the window is mis-scored — exactly the straddle failure. Their fix:

- **Inflate the state space with a time fibre:** M₀ = [0, τ] × M. A trajectory becomes a line in this space-time domain (their eqns 3–5).
- **Inflated dynamic Laplace operator** (their eqn 7): `Δ_{G₀,a} F(t,·) = a² ∂_tt F(t,·) + Δ_{g_t} F(t,·)` — the spatial Laplacian at each time-slice plus a *temporal-diffusion* penalty with knob `a`.
- **Interpolation (their Theorem 7):** as `a → ∞` the operator recovers the dynamic Laplacian ∆_D (one strictly material, window-frozen partition); as `a → 0` the time-slices decouple (per-slice, non-material). `a` slides continuously from "one frozen partition" to "per-slice free."
- **Readout:** the spectrum splits into *temporal* modes (spatially flat, eigenvalue −(aπk/τ)², demoted as `a` grows) and *spatial* modes (constant slice-mean). The leading **spatial** eigenmode's L²-norm-per-slice `‖F(t,·)‖` is large where a coherent structure exists and collapses to zero where it does not — so a single window-spanning eigenmode reads off the **lifetime** (birth, duration, death) of the structure (their §4.2–4.3).

This is precisely a construction that scores a window straddling a birth/death transition, and it is built entirely from a Laplacian quadratic form — **no stationary "future" anywhere**, which is why it evades the §5 hole that killed the effects-based route.

### 2.2 Network science — the supra-Laplacian (independent rediscovery #1)

Froyland & Koltai note (their §1, "Laplace-spectral approaches to multilayer networks") that the inflated operator is *structurally the supra-Laplacian of a multilayer/temporal network*: layers = time-slices, intra-layer block = the slice Laplacian, inter-layer coupling = `a²`.

- **Gómez, Díaz-Guilera, Gómez-Gardeñes, Pérez-Vicente, Moreno & Arenas, "Diffusion Dynamics on Multiplex Networks," *Phys. Rev. Lett.* 110 (2013) 028701.** DOI `10.1103/PhysRevLett.110.028701`. Studies the spectrum of exactly this supra-Laplacian as a function of interlayer coupling strength.
- **De Domenico, Solé-Ribalta, Cozzo, Kivelä, Moreno, Porter, Gómez & Arenas, "Mathematical Formulation of Multilayer Networks," *Phys. Rev. X* 3 (2013) 041022.** DOI `10.1103/PhysRevX.3.041022`. The general tensorial/supra-Laplacian formalism.

Same operator, different field, arrived at independently.

### 2.3 Information theory — deterministic annealing / the information bottleneck (independent rediscovery #2)

The discrete-argmin obstacle is the *hard-assignment* problem of clustering, and its standard cure is to soften the assignment and anneal:

- **Rose, "Deterministic annealing for clustering, compression, classification, regression, and related optimization problems," *Proc. IEEE* 86 (1998) 2210–2239.** DOI `10.1109/5.726788`. A hard argmin over assignments is replaced by the minimizer of a temperature-regularized free energy; lowering the temperature the solution passes through a *sequence of phase transitions (bifurcations)*, not a discontinuity.
- **Tishby, Pereira & Bialek, "The information bottleneck method,"** 1999 (arXiv:physics/0004057). The relevance-compression trade-off solved by the same annealed soft-assignment.
- **Gedeon, Parker & co., "Symmetry-Breaking Bifurcations of the Information Bottleneck and Related Problems," *Entropy* 24 (2022);** and the antecedent **Parker & Gedeon, "Symmetry-breaking bifurcations of the information distortion,"** 2003. Characterize exactly *how* the optimal soft partition changes — through symmetry-breaking bifurcations — as the control parameter crosses a transition.

The lesson these three fields share: **do not force one hard partition through the transition. Use a soft, time-coherent partition family that pays a bounded cost to rotate through it.** The temporal-diffusion `a` (FK / supra-Laplacian) and the annealing temperature (Rose / IB) are the *same knob* — a smoothing weight that dissolves the argmin discontinuity into a bifurcation.

### 2.4 The level-selection anchor already in canon

Canon §13a already cites, for the *static* level-selection half, **Zhang et al. 2025** (closed-form Gaussian Φ analogue, optimal coarse-graining set by covariance eigenvalues/eigenvectors) and the IIT Φ^Max complex [Hoel et al. 2013; Marshall et al. 2026]. The moving-MIP is the natural time-extension of that same eigen-structure reading, so it plugs into the level-selection synthesis the canon already commits to.

---

## 3. The proposed construction (the AOP port)

The port onto AOP's static-Gaussian Φ_MIP on Σ = (I + gL)⁻¹ has two equivalent readings — a discrete one that is exact, and a spectral one that is the convex surrogate. Both are implemented and verified in `phaseE_movingMIP.py`.

### 3.1 Discrete moving-MIP (exact; the Viterbi reading)

Over window slices `t = 0…T`, instead of one fixed partition or T independent argmins, choose a **time-coherent partition family** `P(t)` minimizing

    J[P] = Σ_t Φ(Σ(t), P_t)  +  λ · Σ_t rot(P_{t-1}, P_t)

where `rot` is the partition-change cost (Hamming distance mod complement) and `λ` weights temporal coherence. This is a chain-structured discrete optimization solved exactly by dynamic programming (Viterbi). It is the change-point-segmentation / annealed-soft-partition reading of a time-coherent MIP, anchored by Rose/Tishby/Gedeon (§2.3).

- `λ → 0`: recovers the incoherent per-slice lower bound (T independent argmins).
- `λ → ∞`: recovers the best single frozen partition (the naive window score).
- **intermediate `λ`**: scores the whole window with one partition family that relabels *once*, at the transition, at bounded cost.

### 3.2 Spectral surrogate (the inflated supra-Laplacian; convex relaxation)

Build the space-time coupling graph and diagonalize one operator:

    Δ_a  =  blockdiag( L(b_t) )  +  a² · L_temporal

`L(b_t)` = the AOP coupling-graph Laplacian at slice t; `L_temporal` = the chain (Neumann) Laplacian coupling adjacent copies of each node with weight `a²`. This *is* the Froyland–Koltai inflated dynamic Laplacian (§2.1) and the multilayer supra-Laplacian (§2.2), ported onto the coupling-graph Laplacian instead of the diffusion generator. Its leading **spatial** eigenmode's slice-wise mass profile reads off the lifetime of a split; `a` interpolates per-slice ↔ frozen exactly as FK Theorem 7.

---

## 4. What was computed, and what it shows

All three checks are closed-form on the canon's own Phase-D two-module Gaussian (Σ = (I + gL)⁻¹, two 3-node modules, inter-module weight `b(t)` ramped through the transition). Numbers below are reproduced by `phaseE_movingMIP.py`; the figure is `phaseE_movingMIP_fig.png`.

**(A) The obstacle, made concrete [SETTLED — direct computation].** On a window with `b(t)` ramping `0 → 1.4`, the per-slice Φ_MIP argmin is the module cut `{0,1,2}|{3,4,5}` up to `b* ≈ 0.43` (finely resolved; the script's coarse 15-point grid brackets the relabeling at the `b = 0.5` node) and relabels to cross-module cuts beyond it. A window over `b ∈ [0,1]` straddles the relabeling. This confirms the canon's obstacle is real and locates it.

**(B) Moving-MIP scores the straddling window [SYNTHESIS].** Over `b ∈ [0,1]`:
- per-slice optimum (incoherent lower bound): **0.1655**
- best frozen single partition (upper bound): **0.2069**
- **straddle gap = 0.0414 (a 25% penalty for forcing one label)** — the quantified cost of the discrete-argmin obstacle.
- At intermediate `λ` (0.05–0.2) the window score returns to the per-slice optimum **0.1655** using **exactly one relabeling event** (2 distinct partitions): the module cut `{0,1,2}` up to `b ≈ 0.45`, then a single rotation to a cross-module cut. The window score is **continuous and monotone in `λ`** (annealed; interpolates incoherent ↔ frozen with no discontinuity).

This is the single window-spanning score the canon said did not exist.

**(C) Spectral surrogate reads a lifetime [SYNTHESIS].** The inflated supra-Laplacian's leading eigenvalue rises with `a` toward the `a → ∞` time-averaged (dynamic-Laplacian) reference, reproducing FK Theorem 7. Its leading **spatial** eigenmode (isolated by the FK slice-mean-variance classifier) has an L²-mass-per-slice profile that is large where the two-module split is coherent and collapses to zero as the modules weld — a **birth/death lifetime read off one space-time eigenmode**, requiring no stationary "future" and so cleanly sidestepping the §5 excess-entropy hole.

![Moving-MIP: obstacle, discrete resolution, spectral lifetime]({{artifact:art_b62905ec-49b3-44de-b3d1-7630a3085bf2}})

*Figure. (a) The obstacle: the per-slice MIP argmin relabels away from the module cut at b\* ≈ 0.43, so no fixed partition is the MIP across the window. (b) The moving-MIP window score vs the temporal-coherence weight λ: it interpolates continuously (annealed) between the incoherent per-slice optimum and the best frozen partition, and at intermediate λ scores the whole straddling window with a single bounded relabeling. (c) The spectral surrogate: the leading spatial eigenmode of one inflated supra-Laplacian carries mass only while the two-module split lives, giving its lifetime directly.*

---

## 5. How this evades the two dead ends

- **Against the argmin dead end:** the moving-MIP never asks for one partition to be the MIP on both sides. It asks for a *time-coherent family* whose relabeling cost is bounded, and solves that exactly. The straddle gap (§4B) is the price the old fixed-partition scoring paid; the moving-MIP does not pay it.
- **Against the effects-based dead end:** the whole construction is a *structural* quadratic form (a Laplacian / total-correlation deficit over the window). It reads the split's lifetime from a spatial eigenmode, never from a predictive quantity, so it never needs a stationary future. The §5 excess-entropy definedness hole simply does not arise for this route — a point worth making sharply, because it is exactly why the *effects-based* alternative failed and the *state-partition* alternative does not.

---

## 6. Grading (per charter)

| Claim | Grade | Basis |
|---|---|---|
| The per-slice MIP relabels within a ramp window (the obstacle) | **SETTLED** | Direct closed-form computation on the canon's Phase-D Gaussian |
| Discrete moving-MIP scores a straddling window via a time-coherent family + bounded relabeling | **SYNTHESIS** | Viterbi/change-point reading of a time-coherent MIP; annealed-soft-partition, anchored by Rose 1998 / Tishby et al. 1999 / Gedeon et al. 2022 |
| Spectral surrogate = inflated dynamic Laplacian = supra-Laplacian, ported to the AOP coupling graph; leading spatial mode reads a lifetime | **SYNTHESIS** | Labelled port of Froyland–Koltai 2023 (CPAM) and Gómez 2013 / De Domenico 2013 |
| `a`/`λ` interpolate per-slice ↔ frozen (Thm-7 behavior reproduced) | **SETTLED (borrowed)** | Froyland–Koltai 2023 Theorem 7; reproduced numerically here |

**Citation verification honesty.** Every DOI above was resolved and confirmed against the primary bibliographic record (title, authors, venue, year) via OpenAlex/arXiv. The Froyland–Koltai 2023 paper was **read in full text** — its construction (eqns 3–7), Theorem 7 interpolation, and the spatial/temporal-mode readout (§§3.4, 4.2–4.3) are the passages relied on and are quoted/paraphrased from the retrieved PDF. Rose 1998, Gómez 2013, De Domenico 2013, Tishby et al. 1999, and Gedeon et al. 2022 were verified at the **abstract/bibliographic-record level** (venue, DOI, and the specific result attributed), not read in full; this is stated rather than overclaimed.

---

## 7. Lane boundary — one item flagged for Prime (not acted on)

Canon §9a's collective living-threshold and §4's individuation frontier are stated to be *bottlenecked on the nested-level Φ_MIP extension → now the time-extended moving partition* and "**shared with the Ladder rebuild**." If Prime accepts this construction, the FRONTIER tag on the moving partition in **§4, §9a, and §13a** would move to SYNTHESIS, and the "principal open problem" language in §13a would need rewording. **That is a canon change across three sections and a Ladder-bridge propagation — Prime's call and Ben's decision, not the builder's.** I have not edited canon. Per the charter's propagation discipline, if this folds, the basement-moved note goes to the cross-project handoff bus so the Ladder/Time-Machine threads learn of it.

---

## 8. Frontier residue (named, not claimed closed)

Honest limits of what is built here:

1. **Single-transition scope.** (A)–(C) verify a window with **one** relabeling. A closed-form map between the number of surviving leading spatial modes and the discrete moving-MIP relabeling count in the **multi-transition** case is not established.
2. **Parameter selection not yet derived.** `λ` (discrete) and `a` (spectral) are set by the FK `a_min` heuristic / an annealing schedule, not yet derived from an adiabatic validity bound tied to the §5 `ε = ramp-rate / relaxation-rate`. Closing that — deriving the coherence weight from the differential-Lyapunov adiabaticity condition the canon already quantifies for the spatial half — is the natural next gate.
3. **Gaussian-only.** As with all Phase B–D work, the model class is the coupled Gaussian; generalization beyond it is open (consistent with the canon's own scoping of Φ_MIP).

---

## 9. Files

- `AOP_MovingMIP_Build_proposal_20260721.md` — this proposal.
- `phaseE_movingMIP.py` — runnable, self-contained, closed-form; reproduces every number in §4 and prints the frontier residue. Depends only on NumPy.
- `phaseE_movingMIP_fig.png` — the three-panel figure.

*Builder proposal. Prime verifies; Ben decides. Nobody grades their own homework.*
