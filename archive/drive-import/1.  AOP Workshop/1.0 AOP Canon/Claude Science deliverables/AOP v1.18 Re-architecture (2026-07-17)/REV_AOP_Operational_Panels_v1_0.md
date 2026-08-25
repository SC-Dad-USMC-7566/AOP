# AOP Operational Panels — Computed on the Benchmark

**Status:** OAI Phase 3 deliverable — the four measurement panels (ADR-001) computed on the leaky autocatalytic compartment benchmark, each proxy family with its declaration tuple (ADR-002). Non-canonical. **Compiled:** 17 July 2026. Data: `panel_sensitivity.csv`, `fig_panel_sensitivity.png`; model `aop_benchmark_ctmc.py` (NESS variant).

**Modeling choice (declared).** Panels require a proper non-equilibrium steady state (entropy production, stationary mutual information, predictive information). The absorbing viability model has no NESS, so the panels are computed on a **reinjecting (NESS) variant** — identical mechanism set, but the constitutive influx C fires from n=0, so extinction reinjects rather than absorbs. **Viability (ΔV) is computed on the absorbing variant; panels on the NESS variant.** This split is the honest way to report both — a single model cannot carry an absorbing boundary (for lifetime) and a positive stationary mass at n=0 (for NESS) simultaneously. NESS entropy production σ = 1.32 > 0 confirms the driven character.

---

## The four panels (per ADR-001) and their proxy families

Each panel is a **family** of measurable proxies, not one scalar (the OAI defect being repaired: a single proxy inherits the ambiguity of the target it stands in for). Values are baseline (all mechanisms on) and the change Δ when each mechanism is deleted (full table in `panel_sensitivity.csv`).

### Boundary panel — *statistical organization of interior vs exterior*
| Proxy | Baseline | Moved most by |
|---|---|---|
| B1 = I(n;r) | 0.013 | C, R (0.013) |
| B2 = I(n;z) | 0.016 | C, R, Z (0.016) |
| B3 = H(n) spread | 2.954 | C (2.95 — influx sets interior spread) |
| B4 = 1 − P(empty) | 0.860 | C (0.86), R (0.26), S1/S2 (0.22) |

### Drive panel — *dissipation / irreversibility*
| Proxy | Baseline | Moved most by |
|---|---|---|
| D1 = σ (entropy-production rate) | 1.319 | **Z (1.198 = 91%)**, then C/R (0.12) |
| D2 = realized cycle affinity | 0.141 | (regulator cycle; ~invariant to deletions) |
| D3 = active fraction | 0.562 | (regulator occupancy) |

### Memory panel — *predictive dependence*
| Proxy | Baseline | Moved most by |
|---|---|---|
| M1 = predictive I(n), lag-1 | 0.800 | C (0.80 — interior predictability rests on influx), S1/S2 (−0.32, *raise* it) |
| M2 = predictive I(r) | 0.030 | ~flat |
| M3 = predictive I(z) | 0.094 | Z (0.63 — readout self-prediction) |

### Integration panel — *interdependence*
| Proxy | Baseline | Moved most by |
|---|---|---|
| I1 = TC(n,r,z) | 0.171 | **Z (0.158 = 92%)** |
| I2 = I(r;z) | 0.151 | **Z (0.151 = 100%)** |

## The headline cross-panel finding

**The inert spectator Z dominates three of the four panels** — 91% of the Drive entropy-production rate, 92% of the Integration total correlation, 100% of I(r;z) — because the fast z↔r tracking coupling is where most of the model's stationary dissipation and cross-component correlation live. **Yet Z's viability importance is exactly zero** (ΔV(Z)=0, Shapley 0). Meanwhile the **redundant pair {A,B} is invisible to every single-deletion panel proxy** (all Δ=0), exactly as it is invisible to single-edge viability — its necessity is only visible in the coalition.

This is the four-target architecture earning its place at the panel level: **a panel reading is a description of where activity and correlation sit, not a ranking of what the system's persistence depends on.** The two coincide only after the viability-relative, coalition-aware layer is applied. A framework that collapsed the panels to a single "persistence score" would read Z as the most important mechanism in the system. The benchmark shows, in closed form, that it is the least.

## Declaration tuples

Every proxy above is reported under the common declaration tuple **D = (S, E, F, P, δt, τ, R, V, I, N)** fixed in ADR-002. The panel-specific instances:

- **Boundary/Integration proxies** (information-theoretic): V = stationary distribution of the NESS variant; I = mechanism deletion; N = bits (log₂); δt = continuous; τ = ∞ (stationary). R (reversal) enters only through the comparison to the equilibrium (detailed-balance) control.
- **Drive proxies** (thermodynamic): V = NESS; N = nats for σ (natural log in the entropy-production sum), dimensionless for active fraction; R = the CTMC time-reversal that defines σ = ½ Σ (J_ij) ln(π_i Q_ij / π_j Q_ji).
- **Memory proxies** (predictive): add a lag parameter δt_lag = 1.0 to the tuple; V = NESS; I = deletion; N = bits.
- **Viability ΔV** (the contrast row): V = finite-horizon survival, τ = 15, on the **absorbing** variant; I = deletion; N = survival-probability units. Reported alongside the panels precisely to show the panels do not predict it.

The full declaration tuple for the benchmark system is recorded in `REV_AOP_Benchmark_Model_Specification_v1_0.md` §3.
