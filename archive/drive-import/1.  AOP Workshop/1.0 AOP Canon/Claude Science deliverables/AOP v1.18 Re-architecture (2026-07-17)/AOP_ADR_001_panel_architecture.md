# ADR-001 — Target-vs-Proxy Panel Architecture, Declaration Tuple, and Two-Axis Status Labeling

**Status:** ADOPTED for the v1.17 rebuild (maximal path), 17 July 2026.
**Context source:** OAI Operational Definitions Specification + Semantic-Intervention Protocol (both non-canonical reviewer proposals, Drive, 17 Jul 2026), read against the frozen baseline `FROZEN_aop_canon_v1_16.md` (MD5 `241153bc…`).
**Decision owner:** Ben (approved the maximal path 17 Jul 2026). This ADR records *what the architecture is* so every downstream step (benchmark, panels, manuscript) builds against one spec. It records no scientific claim of its own; those live in the canon.

---

## Decision, in one paragraph

AOP is re-based from a **four-scalar architecture** ("Boundary, Drive, Memory, Integration are four numbers you compute") to a **four-target measurement panel**: Boundary, Drive, Memory, Integration are retained as *conceptual targets*, each represented by a declared *family of proxies*, and every reported quantity is conditional on a common **declaration tuple D**. Evidential status and dependency status become **two independent labels**, never one fused "Status" column. The four familiar names may still carry the prose; tables, figures, and formal claims must name the exact proxy flavor measured. This is adopted because the label-inherits-the-target defect (a proxy quietly standing in for the concept it only partially measures) is the single failure both the OAI review and the internal audit agree is real, and it cannot be fixed by prose caveats alone — it is an architecture fact about how claims are stated.

## Why adopt rather than patch (the hinge)

The minimalist alternative — relabel σ and MI, split the status column, ship — fixes the *symptoms* on the two axes where they're worst (Drive, Boundary) but leaves the *architecture* saying "four scalars." Under a Perspective/atlas posture (see §3 below) that would be survivable. But the maximal path was chosen precisely because AOP's one real credibility gap — the semantic mask has never run where it could fail (Issue Registry P1-6) — is closed by a benchmark, and a benchmark forces the panel architecture into existence anyway: you cannot report a benchmark's Boundary without saying *which* boundary measure, on *which* partition, over *which* horizon. So the panel is not extra scope; it is the frame the benchmark already requires. Adopting it now makes the manuscript and the benchmark speak the same language.

---

## 1. The four measurement panels

**Governing rule (from OAI opdefs §1):** every formal statement must be readable as *"Within declaration D and model class M, proxy P measures aspect A of target T."* No proxy defines its target by fiat unless the manuscript explicitly announces a stipulative definition and accepts the consequences.

Each panel below lists the proxies AOP will report, what aspect of the target each captures, and — critically — **what it does NOT establish**. The "already in v1.16?" column ties each to the Issue Registry.

### Boundary panel (target: maintained interior/exterior organization regulating exchange)

| Proxy | Measures | Does NOT establish | In v1.16? |
|---|---|---|---|
| **B1 State contrast** | declared divergence between interior and exterior state distributions, e.g. D_KL[p(X_in) ‖ p_ref(X_out)] | that the contrast is actively maintained vs. incidental | new |
| **B2 Interface mediation** | conditional dependence given interface, I(X_in;X_out∣F) — screening | that screening is physical vs. statistical artifact | new |
| **B3 Leakage/permeability** | physical flux / transition rate / escape probability across interface | the cost of resisting it | new |
| **B4 Maintenance burden** | work / free-energy / entropy production to hold the contrast over τ | (links to Drive panel — flag the coupling, don't double-count) | new |
| **B5 Cross-boundary dependence** | I(X_in;X_out) — **labeled exactly as dependence** | separation, screening, or boundary strength | **v1.16 uses this as the Boundary scalar** (P0-2 Boundary) |

**Acceptance rule:** "strongly bounded" may be asserted only after stating which of B1–B5 is high/low and why that pattern is a boundary in the chosen model. A single MI value is insufficient. *(This retires the status-table row "Boundary (B) | mutual information I(inside;outside)".)*

### Drive panel (target: resource flow + irreversible activity sustaining a nonequilibrium regime)

| Proxy | Measures | Does NOT establish | In v1.16? |
|---|---|---|---|
| **D1 Resource input** | exergy / chemical potential / energy in per unit time | how much is usefully used | new |
| **D2 Useful maintained work/flux** | the part of input sustaining the target process | total dissipation | new |
| **D3 Housekeeping dissipation** | cost of holding a NESS (when decomposable) | — | new |
| **D4 Nonadiabatic/relaxation dissipation** | cost of moving between states / relaxing to reference | — | new |
| **D5 Total entropy production / irreversibility** | σ = lim_τ D_KL(P_fwd‖P_rev)/τ (finite-τ form when non-stationary) | resource input, useful work, or throughput | **v1.16's Drive scalar, glossed as "free-energy throughput"** (P0-2 Drive) |

**Naming rule:** if D5 is the only computed quantity, the formal axis is **"Dissipation/Irreversibility"**; "Drive" remains the conceptual target. High resource input / useful work may **not** be inferred from σ alone. *(This is the P0-2 Drive fix, done structurally.)*

### Memory panel (target: persistence-relevant information carried across time)

| Proxy | Measures | Does NOT establish | In v1.16? |
|---|---|---|---|
| **M1 Predictive dependence** | excess entropy E = I(X_past;X_future) | how much is stored *now*, depth, accessibility, or use | **yes — v1.16 already uses E as "predictive memory"** |
| **M2 Stored predictive state** | statistical complexity Cμ (or declared state-memory measure) | that it is causally used | **yes — v1.16 separates Cμ from E** (P0-2 Memory *already done*) |
| **M3 Active information storage** | present state's incremental predictive contribution | — | new |
| **M4 Retention depth** | decay time / predictive-info curve / memory kernel | — | partial (time-grain relativity discussed) |
| **M5 Semantic / load-bearing memory** | viability effect of intervening on the memory-bearing variable (per the intervention protocol) | — | **this is what the benchmark tests** |

**Drive→Memory floor (P1-7, already in v1.16):** under a complete stationary description + stated reversal convention, σ>0 ⇒ E>0. This is a floor on **M1 only**. It establishes no floor on M2–M5. *(Confirmed present in frozen text; preserve wording.)*

### Integration panel (target: extent to which parts form an interdependent / irreducible whole under a declared partition)

| Proxy | Measures | Does NOT establish | In v1.16? |
|---|---|---|---|
| **I1 Multivariate interdependence** | total correlation TC = ΣH(Xᵢ) − H(X) | irreducibility; large for redundant copies / common input | **v1.16's Integration scalar** — already labeled the redundancy flavor (P0-2 Integration *already done*) |
| **I2 Redundancy vs synergy** | O-information / declared PID | — | partial |
| **I3 Cut irreducibility** | minimum-partition quantity (scoped Φ_MIP, within its validated model class) | unity outside the static-Gaussian scope | **yes — v1.16 introduces Φ_MIP separately, scoped static-Gaussian** |
| **I4 Dynamic/causal integration** | intervention-sensitive measure when causal closure is the target | — | new |
| **I5 Modularity / alternative decompositions** | number & stability of near-minimum cuts | that the minimum cut is unique | partial (resolvability blur) |

**Naming rule:** TC is labeled **"Interdependence"** in formal displays; "Integration" remains the family name; every numeric claim names I1/I2/I3/I4/I5. *(v1.16 is already substantially here — this panel is the least-changed.)*

---

## 2. Common declaration tuple D (ADR-002)

**Decision:** every reported AOP profile — in the benchmark, the archetypes, and any figure — must declare the 10-slot tuple. **A reported value without D is not an invariant property of the system; it is a value relative to an unstated description.** This is the mechanism that stops a proxy from silently claiming target-level generality.

**D = (S, E, F, P, δt, τ, R, V, I, N)**

| Slot | Name | What it fixes |
|---|---|---|
| **S** | System variables | which variables are *in* the system description |
| **E** | Environment variables | included, or treated as exogenous |
| **F** | Interface | interface variables / physical boundary representation |
| **P** | Partition | component partition + any inside/outside cut |
| **δt** | Temporal grain | sampling grain (the "which clock" choice — load-bearing for Memory) |
| **τ** | Horizon | observation & viability horizon |
| **R** | Reversal convention | time-reversal convention incl. odd-parity variables (load-bearing for Drive/σ) |
| **V** | Viability family | viability functional or bounded family (see intervention protocol) |
| **I** | Intervention class | admissible interventions + invariants held fixed |
| **N** | Normalization | normalization & units used for comparison |

**Minimum reporting standard** (OAI opdefs §10) — every computed result reports: (1) D; (2) target + exact proxy flavor; (3) units, normalization, uncertainty; (4) model class + stationarity assumptions; (5) dependency status and evidential status *separately*; (6) viability functional + horizon when semantic weight is invoked; (7) intervention admissibility + invariants; (8) code/data/figure lineage.

## 2b. Two-axis status labeling — retiring the fused "Status" column (P0-5)

**Decision:** the v1.16 §12 "Status of claims" table single "Status" column (which fuses e.g. "secure, scoped") is split into **two independent axes**. A claim carries one label from each.

**Dependency status** — *does the relation hold within the model class?*
| Label | Meaning |
|---|---|
| **Forced** | holds for every admissible model under stated assumptions |
| **Conditionally forced** | holds only when a stated additional condition is satisfied |
| **Dissociable** | explicit admissible countermodels realize one quantity without the other |
| **Unidentified** | available evidence does not determine the relation |

**Evidential status** — *what kind of warrant backs it?*
| Label | Meaning |
|---|---|
| **Theorem/corollary** | proved |
| **Definition / stipulated weld** | true by construction (exact, but carries no physical-law evidence) |
| **Constructed counterexample** | a witness object |
| **Analytic model result** | closed-form on a specified model |
| **Numerical simulation** | computed, estimator-dependent |
| **Random-ensemble regularity** | holds across a sampled ensemble (supports empirical regularity *within that ensemble* — cannot alone establish modal freedom) |
| **Empirical observation** | measured in a real system |
| **Conjecture / frontier** | proposed, untested |

**Why two axes matter (the P0-5 payload):** the fusion lets a hostile reader read "secure, scoped" as a one-example result overstated as secure. Split, the same claim reads e.g. *"dependency: conditionally-forced (static-Gaussian); evidential: analytic model result"* — exactly as strong as it is and no stronger. This also cross-checks the charter's grade-every-claim rule: the old [SETTLED]/[SYNTHESIS]/[FRONTIER] grade maps onto the **evidential** axis, and the "scoped / static-Gaussian / frontier-at-generalization" caveats map onto the **dependency** axis — they were never the same thing.

**Interaction with the bind-before-freeze insight (project memory):** a "binding-passed" result — the knob moves the named measure in the claimed direction — is evidence about **dependency status** (the coupling is present and directional), and is *silent* on whether that measure determines the outcome. So binding-passed maps to at most "conditionally forced," never to a high evidential grade. The two-axis labeling makes this legible where the fused column hid it.

---

## 3. Venue commitment (ADR-003)

**Decision:** AOP submits as a **Perspective / atlas**. The **genre** ("Perspective") is stated in the frozen v1.16 title block ("Preprint · version 1.16 · compiled 15 July 2026 · not peer reviewed · Perspective"). The **target venue** — Royal Society *Interface Focus* — is named not in the canon itself but in the submission-package documents: `aop_submission_README.md` ("AOP — Interface Focus Submission Package") and `aop_manuscript_blueprint.md` ("Target: Royal Society *Interface Focus*, Perspective — main text ~8,000 words"). The genre is further backed by the prior on-record genre decision (the paper is owned as a *Perspective / synthesis of established results, not a predictive theory*; the photon-at-the-wall and de Sitter / horizon-holography set-pieces were removed as theory-of-everything overreach and parked for the Ladder). *(An earlier draft of this ADR wrongly attributed "Interface Focus" to the title block; the title block names only the genre, not the venue.)*

**This is the hinge that makes the re-architecture coherent** (Issue Registry, "the hinge"). The maximalist and minimalist paths are not contradictory on the science — they diverge on venue:

- **As a Perspective/atlas** — "here is a vocabulary and a dependency ledger for thinking about persistence" — the panel architecture is the honest, correct presentation of what AOP measures, and the benchmark is a *demonstration that the panel does real work*, not a claim to have beaten a rival at prediction.
- **As an adjudicating framework** — "AOP tells you something a one-axis view gets wrong" — the panel plus benchmark plus rival comparison would have to *win*, and any null would be a failure of the paper.

**What the Perspective posture commits the panels to, and what it does not:**

| Commits to | Does NOT commit to |
|---|---|
| Each panel is a declared, reproducible measurement family with stated proxies | That any single proxy is *the* correct measure of its target |
| The benchmark shows the panel discriminating regimes (a worked demonstration) | That the benchmark *proves* AOP superior to all rivals |
| The dependency ledger separates forced from dissociable relations | That the forced relations are novel discoveries vs. known results assembled |
| One bounded comparative claim vs. one named rival (Phase 5) | A general adjudication tournament against the field |
| Honest grading: demonstrations labeled as demonstrations | Passing off self-consistency demos as tests that could have failed |

**Manuscript posture language** (from OAI Phase 6): use "atlas," "audit," "measurement panel," "dependency architecture." Avoid claims of a universal domain wall, a master geometry of persistence, or a new physical theory.

**Consequence for the benchmark exit gate:** because the venue is a Perspective, the benchmark's job is to clear a *non-triviality* bar (≥1 preregistered result not guaranteed by construction, could have failed, changes the system's classification) — **not** an *adjudication* bar (must beat the rival). If the rival comparison (Phase 5) comes out even, that is an acceptable, reportable Perspective result ("AOP is an organizing vocabulary here"); it is only a failure under the adjudicating posture we are explicitly not adopting. This keeps the empirical keystone honest without staking the paper on an outcome we cannot guarantee.

---

## Decision record

| ADR | Decision | Status |
|---|---|---|
| ADR-001 | Four-target measurement panel (B1–B5, D1–D5, M1–M5, I1–I5) replaces four-scalar architecture | ADOPTED |
| ADR-002 | Declaration tuple D = (S,E,F,P,δt,τ,R,V,I,N) required on every reported profile; 8-point minimum reporting standard | ADOPTED |
| ADR-002b | Two-axis status labeling (dependency × evidential) replaces the fused §12 Status column | ADOPTED |
| ADR-003 | Perspective/atlas venue (Interface Focus); benchmark clears non-triviality, not adjudication | ADOPTED |

All four are inputs the downstream steps (Phase 2 benchmark, Phase 3 panels, Phase 4 manuscript, Phase 5 rival) build against. No scientific claim originates in this ADR; claims live in the rebuilt canon.
