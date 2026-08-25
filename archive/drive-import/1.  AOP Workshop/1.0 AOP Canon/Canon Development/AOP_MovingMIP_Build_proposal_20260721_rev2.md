# AOP Moving-MIP Build — Proposal

**A hard temporally-regularized partition path for scoring a window that straddles a MIP relabeling** *(a proposed method — NOT a closure of the canon FRONTIER item)*

> **REVISION 2 (21 Jul 2026), post Aster red-team review — verdict accepted.** Aster returned **RED on closure** and **YELLOW on the research direction**, and the review was checked point-by-point against the code by independent reproduction; every checkable claim held. Corrections folded in: (1) a **stop-ship bug** — the script optimized `Σ Φ + λ·Σrot` but *reported* only the `Σ Φ` term, so the earlier Panel B plotted a step under a "not a jump" title; the objective and its components are now reported/plotted honestly; (2) the discrete path is **hard Viterbi regularization, not soft/annealed**; (3) the score is **not grid-invariant**; (4) the demonstrated transition is to **six degenerate 1|5 singleton cuts**, not competing organizations; (5) the spectral operator is **not** a derived surrogate (graph crossing `b=1` ≠ MIP relabel `b≈0.43`); (6) the **"solved in three fields" headline is withdrawn** — this is a labelled synthesis. **Grades B and C are lowered to FRONTIER. §4/§9a/§13a stay FRONTIER; canon was never edited.** The Ptaszyński–Esposito line-check was rated GREEN (one wording refinement, folded into that memo separately).

- **Author lane:** Claude Science (builder). This is a **proposal** for Prime to verify and Ben to decide — not canon.
- **Date:** 21 July 2026 (rev 2)
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

## 2. Charter's first move: reusable machinery exists in four literatures (not a three-field "solution")

Per charter discipline ("don't create when you can cite; be skeptical of anything that looks new"), the first move was a wide literature search, not a construction. **Correction (rev 2):** an earlier draft claimed the problem was *"already solved, the same object independently found in three fields."* That overclaims. What the literature actually supplies is **reusable temporal-partition-smoothing machinery and formal analogies** — across dynamic coherent-set detection, multilayer-network supra-Laplacians, deterministic-annealing/information-bottleneck clustering, and the temporal-community literature — not an identical object solved elsewhere and imported unchanged. Froyland & Koltai themselves describe the multilayer-network link as *"formally similar"* with results that *"should carry over,"* which is precedent, not identity. The honest classification of this deposit is a **labelled synthesis** of those strategies, with the AOP-specific observable and its validation still to be earned.

### 2.1 Nonautonomous dynamical systems — the inflated dynamic Laplacian (load-bearing precedent)

**Froyland & Koltai, "Detecting the birth and death of finite-time coherent sets," *Comm. Pure Appl. Math.* 76 (2023).** DOI `10.1002/cpa.22115` (also arXiv:2103.16286v4). **Read in full** (construction, spectrum, and 1-D surrogate sections; the passages relied on are cited below).

Their problem is *structurally analogous* to ours ("coherent set" for "individual," "flow" for "developmental ramp"): standard (Lagrangian) coherent-set methods require an object to stay coherent *throughout* the chosen window, so an object that is born or dies *inside* the window is mis-scored — the same shape as the straddle failure. Their operator is a Laplace–Beltrami operator from the pullback metric of a nonautonomous flow, so the analogy is a source of *machinery*, not an identity with AOP's coupling-graph object. Their fix:

- **Inflate the state space with a time fibre:** M₀ = [0, τ] × M. A trajectory becomes a line in this space-time domain (their eqns 3–5).
- **Inflated dynamic Laplace operator** (their eqn 7): `Δ_{G₀,a} F(t,·) = a² ∂_tt F(t,·) + Δ_{g_t} F(t,·)` — the spatial Laplacian at each time-slice plus a *temporal-diffusion* penalty with knob `a`.
- **Interpolation (their Theorem 7):** as `a → ∞` the operator recovers the dynamic Laplacian ∆_D (one strictly material, window-frozen partition); as `a → 0` the time-slices decouple (per-slice, non-material). `a` slides continuously from "one frozen partition" to "per-slice free."
- **Readout:** the spectrum splits into *temporal* modes (spatially flat, eigenvalue −(aπk/τ)², demoted as `a` grows) and *spatial* modes (constant slice-mean). The leading **spatial** eigenmode's L²-norm-per-slice `‖F(t,·)‖` is large where a coherent structure exists and collapses to zero where it does not — so a single window-spanning eigenmode reads off the **lifetime** (birth, duration, death) of the structure (their §4.2–4.3).

This is precisely a construction that scores a window straddling a birth/death transition, and it is built entirely from a Laplacian quadratic form — **no stationary "future" anywhere**, which is why it evades the §5 hole that killed the effects-based route.

### 2.2 Network science — the supra-Laplacian (a formal analogy per FK)

Froyland & Koltai note (their §1) that the inflated operator is *structurally/formally similar to* the supra-Laplacian of a multilayer/temporal network — layers = time-slices, intra-layer block = the slice Laplacian, inter-layer coupling = `a²` — and say results "should carry over." This is a **formal analogy the authors draw**, not a proof of operator identity; I take it as such.

- **Gómez, Díaz-Guilera, Gómez-Gardeñes, Pérez-Vicente, Moreno & Arenas, "Diffusion Dynamics on Multiplex Networks," *Phys. Rev. Lett.* 110 (2013) 028701.** DOI `10.1103/PhysRevLett.110.028701`. Studies the spectrum of exactly this supra-Laplacian as a function of interlayer coupling strength.
- **De Domenico, Solé-Ribalta, Cozzo, Kivelä, Moreno, Porter, Gómez & Arenas, "Mathematical Formulation of Multilayer Networks," *Phys. Rev. X* 3 (2013) 041022.** DOI `10.1103/PhysRevX.3.041022`. The general tensorial/supra-Laplacian formalism.

A closely related operator family in a different field — a source of reusable spectral machinery, per FK's own "formally similar" framing.

### 2.3 Information theory — deterministic annealing / the information bottleneck (motivating strategy)

The discrete-argmin obstacle is the *hard-assignment* problem of clustering, and its standard cure is to soften the assignment and anneal:

- **Rose, "Deterministic annealing for clustering, compression, classification, regression, and related optimization problems," *Proc. IEEE* 86 (1998) 2210–2239.** DOI `10.1109/5.726788`. A hard argmin over assignments is replaced by the minimizer of a temperature-regularized free energy; lowering the temperature the solution passes through a *sequence of phase transitions (bifurcations)*, not a discontinuity.
- **Tishby, Pereira & Bialek, "The information bottleneck method,"** 1999 (arXiv:physics/0004057). The relevance-compression trade-off solved by the same annealed soft-assignment.
- **Parker & Dimitrov, "Symmetry-Breaking Bifurcations of the Information Bottleneck and Related Problems," *Entropy* 24 (2022) 1231** (DOI `10.3390/e24091231`; OpenAlex W4294959637). Characterizes exactly *how* the optimal soft partition changes — through symmetry-breaking bifurcations — as the control parameter crosses a transition.

The shared lesson: **do not force one hard partition through the transition; use a time-coherent partition family that pays a bounded cost to rotate through it.** *Caveat (Aster 2.2):* these references motivate *relaxation broadly* — the temporal-diffusion `a` (FK / supra-Laplacian) and the annealing temperature (Rose / IB) are analogous smoothing weights — but they do **not** derive the specific **hard** switching-cost functional `J_λ` implemented in §3.1. Deriving a genuinely *soft/annealed* moving-MIP (a Gibbs distribution over partition paths at temperature `τ`, whose `τ→0` limit is the hard DP) is a concrete next step, not something already done here.

### 2.4 The level-selection anchor already in canon

Canon §13a already cites, for the *static* level-selection half, **Zhang et al. 2025** (closed-form Gaussian Φ analogue, optimal coarse-graining set by covariance eigenvalues/eigenvectors) and the IIT Φ^Max complex [Hoel et al. 2013; Marshall et al. 2026]. The moving-MIP is the natural time-extension of that same eigen-structure reading, so it plugs into the level-selection synthesis the canon already commits to.

---

## 3. The proposed construction (the AOP port)

The port onto AOP's static-Gaussian Φ_MIP on Σ = (I + gL)⁻¹ is explored two ways — a discrete one (exact DP on a hard switching-cost objective) and a spectral one (an inflated supra-Laplacian diagnostic). **These are not proven equivalent** and the spectral one is **not** a convex surrogate for the discrete objective — no relaxation bound is established and their transitions do not coincide in the test graph (§4C). Both are implemented in `phaseE_movingMIP.py`; treat them as two independent probes of the same phenomenon, not two readings of one solved object.

### 3.1 Discrete moving-MIP (exact; the Viterbi reading)

Over window slices `t = 0…T`, instead of one fixed partition or T independent argmins, choose a **time-coherent partition family** `P(t)` minimizing

    J[P] = Σ_t Φ(Σ(t), P_t)  +  λ · Σ_t rot(P_{t-1}, P_t)

where `rot` is the partition-change cost (Hamming distance mod complement) and `λ` weights temporal coherence. This is a chain-structured discrete optimization solved exactly by dynamic programming (Viterbi). It is the change-point-segmentation / annealed-soft-partition reading of a time-coherent MIP, anchored by Rose/Tishby/Parker–Dimitrov (§2.3).

- `λ → 0`: recovers the incoherent per-slice lower bound (T independent argmins).
- `λ → ∞`: recovers the best single frozen partition (the naive window score).
- **intermediate `λ`**: scores the whole window with one partition family that relabels *once*, at the transition, at bounded cost.

### 3.2 Spectral surrogate (the inflated supra-Laplacian; convex relaxation)

Build the space-time coupling graph and diagonalize one operator:

    Δ_a  =  blockdiag( L(b_t) )  +  a² · L_temporal

`L(b_t)` = the AOP coupling-graph Laplacian at slice t; `L_temporal` = the chain (Neumann) Laplacian coupling adjacent copies of each node with weight `a²`. This **borrows the inflation idea** from the Froyland–Koltai inflated dynamic Laplacian (§2.1) and the multilayer supra-Laplacian (§2.2). **It is not the same operator** and not a derived surrogate: FK's operator is a Laplace–Beltrami operator built from the pullback metric of a nonautonomous flow, and (crucially) **this construction has not been shown to be a spectral relaxation of the Gaussian log-det MIP objective** — no bound relates their optima and no map ties `a` to `λ`. Treat (C) as an *independent graph-coherence diagnostic* pending such a derivation. [Aster review, 21 Jul 2026 — §2.5–2.7; verdict accepted.]

---

## 4. What was computed, and what it shows

All three checks are closed-form on the canon's own Phase-D two-module Gaussian (Σ = (I + gL)⁻¹, two 3-node modules, inter-module weight `b(t)` ramped through the transition). Numbers below are reproduced by `phaseE_movingMIP.py`; the figure is `phaseE_movingMIP_fig.png`.

**(A) The obstacle, made concrete [SETTLED — direct computation].** On a window with `b(t)` ramping `0 → 1.4`, the per-slice Φ_MIP argmin is the module cut `{0,1,2}|{3,4,5}` up to `b* ≈ 0.43` (finely resolved; the script's coarse 15-point grid brackets the relabeling at the `b = 0.5` node) and relabels to cross-module cuts beyond it. A window over `b ∈ [0,1]` straddles the relabeling. This confirms the canon's obstacle is real and locates it.

**(B) Moving-MIP: hard temporally-regularized partition path [FRONTIER].** Over `b ∈ [0,1]`, the DP minimizes `J_λ = Σ_t Φ(t,P_t) + λ Σ_t rot(P_{t-1},P_t)`. **Report the optimized objective `J/T`, decomposed** (an earlier version of this deposit reported only the deficit term, dropping the `λ·rot` penalty it optimizes — that mis-plot is corrected here):

| λ | J/T (objective) | deficit part | rot cost | change events |
|---:|---:|---:|---:|---:|
| 0.00 | 0.1655 | 0.1655 | 18 | 9 |
| 0.05 | 0.1702 | 0.1655 | 2 | 1 |
| 0.10 | 0.1750 | 0.1655 | 2 | 1 |
| 0.20 | 0.1845 | 0.1655 | 2 | 1 |
| 0.50 | 0.2069 | 0.2069 | 0 | 0 |

- The **optimized objective `J/T` is continuous, monotone, piecewise-linear** in `λ` (min of finitely many affine path costs; verified 101-pt grid, max step 0.0010). The **selected hard path can still switch at breakpoints** — this is *hard Viterbi regularization, not a soft/annealed (Gibbs) construction*.
- **Correction to an earlier claim:** the transition is module cut `{0,1,2}` → a **1|5 singleton** cut, and at `b ≈ 0.43` **six 1|5 singleton cuts are degenerate minimizers** (the unnormalized-MIP small-side vulnerability), one picked by enumeration order — *not* a transition between two nontrivially competing organizations. The example does not yet demonstrate tracking between competing partitions.
- **`rot cost` (Hamming) ≠ change events**: one change event here carries rotation cost 2; these are distinct observables (an earlier version conflated them).

This is a defensible *proposed* regularization of instantaneous MIPs — it does **not** yet establish "the single window-spanning score the canon said did not exist," and it does not close the FRONTIER item.

**(C) Spectral diagnostic — not a derived surrogate [FRONTIER].** The inflated supra-Laplacian's leading eigenvalue rises with `a` toward the `a → ∞` time-averaged reference (FK Theorem 7 behavior). Its leading **spatial** eigenmode's L²-mass-per-slice concentrates early and decays. **But this is not validated correspondence to Φ_MIP:** for this exact graph the coupling-Laplacian eigenvalues are analytic (module-difference mode `6b`, within-module modes `3+3b`), so the **graph-spectral crossing is at `b = 1`, not at the Gaussian-MIP relabel near `b ≈ 0.43`**. The mass decay reflects localization where the instantaneous spectral cost is lowest, not a moving-MIP transition. The readout also depends on hand-set `a = 0.8`, a classifier threshold, a lifetime threshold, and the window endpoints, with no robustness sweep deposited.

![Moving-MIP: obstacle, objective vs mis-plot, spectral non-correspondence]({{artifact:art_b62905ec-49b3-44de-b3d1-7630a3085bf2}})

*Figure. (a) The obstacle: the per-slice MIP argmin leaves the module cut at b\* ≈ 0.43 — to six degenerate 1|5 singleton cuts. (b) The optimized objective J/T (solid) is continuous and monotone in λ; the deficit-only component (dashed) — the score reported in an earlier version — is a step, which is why the earlier panel appeared to jump. (c) The spectral diagnostic: the leading spatial-mode mass decays, but the analytic graph-spectral crossing (b = 1) does not coincide with the MIP relabel (b ≈ 0.43), so the panel does not validate correspondence between the two constructions.*

---

## 5. How this evades the two dead ends

- **Against the argmin dead end (partial):** the moving-MIP does not ask for one partition to be the MIP on both sides; it asks for a *time-coherent family* whose relabeling cost is bounded, and solves that exactly. This is a genuine step — but see §4B: the objective is grid-dependent and the demonstrated transition is to degenerate singleton cuts, so the obstacle is *reformulated*, not yet dissolved.
- **Against the effects-based dead end:** the construction is a *structural* quadratic form (total-correlation deficit / Laplacian over the window), read from state partitions, never from a predictive quantity — so it does not require a stationary "future." One wording correction (Aster §2.8): it is over-categorical to say the excess-entropy quantity "loses its definition." Past–future mutual information at a *specified* cut remains mathematically definable for a nonstationary process; what fails off-stationarity is the standard **stationary invariant / asymptotic limit** (and the result becomes cut-dependent). The structural route sidesteps *that* failure — which is the accurate, publication-strength statement.

---

## 6. Grading (per charter)

| Claim | Grade | Basis |
|---|---|---|
| The per-slice MIP relabels within a ramp window (the obstacle) | **SETTLED** | Direct closed-form computation on the canon's Phase-D Gaussian |
| A hard temporally-regularized partition path `J_λ` is well-defined and DP solves it exactly | **FRONTIER** | Correct as a *proposed* method (Viterbi over a time-coherent family). Does **not** close the canon item: score is grid-dependent (§4B/Aster 2.3), it is hard regularization not soft/annealed (Aster 2.2), and the demonstrated transition is to degenerate singleton cuts (Aster 2.4). |
| The spectral supra-Laplacian is a *surrogate* for moving Φ_MIP | **FRONTIER — not established** | Not derived as a relaxation of the log-det MIP objective; no `a↔λ` map; graph crossing (`b=1`) ≠ MIP relabel (`b≈0.43`) (Aster 2.5–2.6). Keep as an independent diagnostic. |
| "Same object solved independently in three fields" | **withdrawn** | The literature supports reusable machinery and formal analogies (FK call the multilayer link "formally similar," results "should carry over"), not identity of objects. Honest classification: a **labelled synthesis** of temporal-partition-smoothing strategies (Aster 2.7). |
| `a`/`λ` interpolate per-slice ↔ frozen (Thm-7 behavior reproduced) | **SETTLED (borrowed)** | Froyland–Koltai 2023 Theorem 7; reproduced numerically here |

**Citation verification honesty.** Every DOI above was resolved and confirmed against the primary bibliographic record (title, authors, venue, year) via OpenAlex/arXiv. The Froyland–Koltai 2023 paper was **read in full text** — its construction (eqns 3–7), Theorem 7 interpolation, and the spatial/temporal-mode readout (§§3.4, 4.2–4.3) are the passages relied on and are quoted/paraphrased from the retrieved PDF. Rose 1998, Gómez 2013, De Domenico 2013, Tishby et al. 1999, and Parker & Dimitrov 2022 were verified at the **abstract/bibliographic-record level** (venue, DOI, authors, and the specific result attributed), not read in full; this is stated rather than overclaimed. (An earlier draft misattributed the *Entropy* 24 (2022) bifurcation paper to "Gedeon et al."; the OpenAlex record W4294959637 gives the authors as A. E. Parker & A. G. Dimitrov, corrected here.)

---

## 7. Lane boundary — one item flagged for Prime (not acted on)

Canon §9a's collective living-threshold and §4's individuation frontier are stated to be *bottlenecked on the nested-level Φ_MIP extension → now the time-extended moving partition* and "**shared with the Ladder rebuild**."

**Rev-2 status: no canon change is warranted on this deposit.** An earlier draft suggested that acceptance would move the FRONTIER tag in §4/§9a/§13a to SYNTHESIS. The Aster red-team review returned **RED on closure**, and independent reproduction confirmed every defect (grid-dependence, hard-not-soft, degenerate transition, unproven spectral correspondence, withdrawn three-field claim). **§4, §9a, and §13a should therefore remain FRONTIER, and the "principal open problem" language in §13a stands.** I have not edited canon, and there is nothing to propagate to the Ladder/Time-Machine bus (the basement did not move). What *is* deliverable here is a **research direction rated YELLOW/worth-repairing** plus the concrete repair roadmap in §8 — for Prime and Ben to weigh, not a closure to ratify.

---

## 8. Frontier residue — the open items that keep this FRONTIER

These are the reasons the deposit does **not** close §4/§9a/§13a. Items 1–6 are the Aster red-team findings (accepted after independent reproduction); 7–8 are the pre-existing scope limits.

1. **Grid-dependence (must fix before any closure claim).** The deficit sum scales with temporal resolution while the per-transition `rot` cost does not, so the balance between them — and the selected path — shifts with the number of slices. Fix: an integral objective `J = ∫ Φ dt + λ·TV(P)` with an explicit `Δt` factor, or a stated `λ`-vs-`Δt` scaling law. Until then no reported `J/T` value is discretization-invariant.
2. **Hard, not soft.** §3.1 is exact hard Viterbi regularization. A genuinely annealed construction — a Gibbs distribution over partition paths `∝ exp(−J_λ/τ)`, with the hard DP as its `τ→0` limit — would (a) actually earn the "annealing / bifurcation" language borrowed from Rose/Tishby and (b) give a soft occupancy that is differentiable in the control parameter. Building and testing that is the priority-1 repair.
3. **Degenerate, not competing.** The demonstrated transition is module cut → six degenerate 1|5 singletons (unnormalized-MIP small-side vulnerability). A convincing benchmark needs a model with **two genuinely competing non-trivial organizations** (e.g. a 3|3 module cut that yields to a *different* balanced 3|3 cut, or a normalized MIP that resists singleton collapse), and it must expose all tied optimal paths rather than letting enumeration order hide the degeneracy.
4. **Spectral–MIP correspondence unproven.** §4C is an independent diagnostic, not a surrogate: no derivation shows the inflated supra-Laplacian relaxes the Gaussian log-det MIP objective, no `a↔λ` map exists, and the graph-spectral crossing (`b=1`) does not coincide with the MIP relabel (`b≈0.43`). Either derive the relaxation (with a bound relating the optima) or keep (C) explicitly de-scoped.
5. **Robustness unswept.** The (C) readout depends on `a`, a classifier threshold, a lifetime threshold, and window endpoints, with no sensitivity analysis deposited.
6. **Multi-transition map absent.** A closed-form relation between surviving leading spatial modes and the discrete relabeling count is established only for a single transition.
7. **Parameter selection not yet derived.** `λ` and `a` are set by heuristic, not from the §5 adiabatic bound `ε = ramp-rate / relaxation-rate` (the differential-Lyapunov condition the canon quantifies for the spatial half).
8. **Gaussian-only.** As with all Phase B–D work, the model class is the coupled Gaussian; generalization is open (consistent with canon scoping).

**Closer discrete precedent to fold in (Aster):** the temporal-community-detection literature treats "snapshot quality + temporal smoothness" as exactly this combinatorial partition-path problem with convex relaxations — e.g. Chen, Kawadia & Urgaonkar, arXiv:1303.7226. It is a nearer neighbor than the annealing references and should anchor §3.1 in a revision.

---

## 9. Files

- `AOP_MovingMIP_Build_proposal_20260721.md` — this proposal.
- `phaseE_movingMIP.py` — runnable, self-contained, closed-form; reproduces every number in §4 and prints the frontier residue. Depends only on NumPy.
- `phaseE_movingMIP_fig.png` — the three-panel figure.

*Builder proposal. Prime verifies; Ben decides. Nobody grades their own homework.*
