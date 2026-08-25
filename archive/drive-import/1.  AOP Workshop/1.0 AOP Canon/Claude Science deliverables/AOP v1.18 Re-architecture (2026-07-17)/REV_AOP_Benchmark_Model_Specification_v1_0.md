# AOP Benchmark Model Specification — Leaky Autocatalytic Compartment

**Status:** fills OAI Remediation deliverable #4 (the OAI Drive stub `REV_OAI_AOP_Benchmark_Model_Specification` is empty). Non-canonical; this is the model the semantic-intervention protocol is exercised on. **Compiled:** 17 July 2026, this session. Reproducible script: `aop_benchmark_ctmc.py` (all numbers below regenerate from it).

**Design goal (OAI Phase 4):** demonstrate that the AOP semantic-intervention method produces **non-trivial information on a system whose answer is not built in** — i.e. where naive correlation/strength readings and single-edge attribution give the *wrong* answer, and only the coalition-aware viability analysis gives the right one.

---

## 1. The system

A minimal leaky autocatalytic compartment, modeled as an **exactly-solvable continuous-time Markov chain (CTMC)** — closed-form throughout, no Monte-Carlo, honoring the charter's "build on analytic results, not estimated ones."

**State** `(n, r, z)`:
| Var | Range | Meaning |
|---|---|---|
| `n` | 0..N (N=8) | copy number of the core autocatalytic species (the interior). **n=0 is extinction — absorbing.** |
| `r` | {0,1} | fuel-driven internal regulator (off/on). Its cycle is driven, giving the system sustained entropy production. |
| `z` | {0,1} | downstream readout that **tracks** r but feeds nothing back — the built-in inert spectator. |

36 states total (n∈0..8 × r∈{0,1} × z∈{0,1} = 9×2×2); 4 absorbing (n=0 × r,z), 32 transient.

## 2. Mechanisms (the intervenable couplings)

The mechanism set `G = {A, B, C, R, S1, S2, Z}`. The gate logic is chosen so the redundancy/synergy controls are **clean**, not artifacts of additive rates:

| Mech | Role | Implementation | Ground-truth class |
|---|---|---|---|
| **A** | birth path α | OR-gated autocatalytic birth `k_auto·n(1−n/N)` — A **or** B suffices | redundant (with B) |
| **B** | birth path β | same OR gate | redundant (with A) |
| **S1** | synergy half | AND-gated birth `kS·n(1−n/N)` — needs **both** S1 and S2 | synergistic (with S2) |
| **S2** | synergy half | same AND gate | synergistic (with S1) |
| **R** | leak suppression | death rate `×(1−ρ)` when r=1 | load-bearing single |
| **C** | weak influx | constitutive `+kC` birth | weak-but-real |
| **Z** | readout tracking | drives z→r correlation at rate λ; **no effect on any n or r rate** | inert spectator |

**Rates** (a.u.): `k_auto=0.72, kS=0.34, kC=0.055, δ=0.38, δ₀=0.03, ρ=0.55, f=0.9, w=0.7, λ=1.4, λ₀=0.05`. Chosen to place the system in a **metastable regime** (baseline finite-horizon survival ≈ 0.93 at τ=15, QSD lifetime ≈ 159) so interventions have dynamic range to move viability without saturating at 0 or 1.

## 3. Declaration tuple D (per ADR-002)

| Slot | Value |
|---|---|
| **S** system | `(n, r)` — interior population + regulator |
| **E** environment | fuel/waste baths (implicit in birth/death rates), exogenous |
| **F** interface | the permeable membrane, represented by leak coefficient δ and influx kC |
| **P** partition | interior `n` vs exterior; regulator/readout as internal components |
| **δt** grain | continuous-time (CTMC generator) |
| **τ** horizon | primary τ=15; family {8,12,15,20,30} |
| **R** reversal | standard CTMC time-reversal; the driven r-cycle is the entropy-producing part |
| **V** viability | finite-horizon survival family (see §4) |
| **I** intervention | mechanism deletion (I-1) primary; scaling (I-2) and the inadmissible ρ>1 demo |
| **N** normalization | ΔV in absolute survival-probability units; MI in bits |

## 4. Viability family V(θ,τ)

`V_θ,τ(x_t) = P(not extinct by t+τ | X_t = x_t)`, computed closed-form as `(e_start · exp(T·τ) · 1)` where T is the transient subgenerator. This is **conditioned on the present state but evaluates present capacity through future dynamics** — OAI's finite-horizon prescription, avoiding teleology without pretending capacity is readable from an instant.

- **Primary functional:** survival from the healthy start `(N,0,0)` over τ=15.
- **Family Θ×T:** {survival} × {τ=8,12,15,20,30}. Robustness is reported across this family (a mechanism is load-bearing "for all / most / selected" members).
- **Threshold** for categorical viability: `v_min = 0.60`. A coalition S is failure-inducing if `V(off on S) < v_min`. Threshold sensitivity is reported.

## 5. Interventions and invariants

Primary intervention class **I-1 (mechanism deletion):** set the mechanism's gate/rate to zero, leaving all other rates fixed. **Invariants held:** state space, untargeted transition rules, environmental forcing, initial distribution, time grain, viability definition. **Not held (and declared):** total resource input changes when a birth path is deleted — this is why the **budget-shift control** exists (does an apparent effect merely reflect changed total input?).

Physical-status labels applied: deletions of A/B/C/R/S1/S2 are **mechanistically interpretable** (coherent mechanism-level counterfactuals); the ρ=1.8 edit is **inadmissible** (drives death rates negative) and is used only to demonstrate why admissibility matters.

## 6. What is built in vs. what is tested (the honesty boundary)

**Built in (ground truth — not a discovery):** that {A,B} are redundant, {S1,S2} synergistic, Z inert, R load-bearing. A benchmark *must* have known ground truth; that is what makes it a benchmark.

**NOT built in (could have come out otherwise — this is what the exit gate tests):**
1. Whether the AOP viability-intervention method **recovers** that ground truth when a correlation/strength reading does not.
2. The **sign and magnitude** of the Möbius interaction terms (a reviewer's naive expectation — h>0 ⇒ synergy, h<0 ⇒ redundancy — is *inverted* here; that inversion is a derived result, not a specification).
3. The **quantitative dissociation** between structural strength and viability importance (the Spearman correlations).
4. **Emergent** structure I did not design: the R ⇄ {S1,S2} substitutability (two disjoint routes to viability), which falls out of the closed-form solution.

See the preregistration and results documents for the tests and verdicts.
