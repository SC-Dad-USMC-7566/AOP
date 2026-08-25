# AOP Step 0 — Axis-input scoping

**Deliverable:** `AOP_Step0_AxisInputScoping_v0.1.md`
**Order:** `TASK_CLEANSEAT_AOP_Step0_20260725` §2
**Date:** 25 July 2026
**Seat:** clean chat seat (eligibility declared in §0 below)
**Status:** §2 complete. **HALT at §2.4.** §3 not begun.

---

## 0. Eligibility and contamination declaration

Declared before any work, per the order's §0.

| Check | Status |
|---|---|
| `AOP_Benchmark_PhaseA_SystemSelection_v0.1.md` (`11XDVzD…`) | **Not read**, this session or any prior |
| `AOP_Benchmark_PhaseA_Sporulation_evidence` (`1y01p5w…`) | **Not read** |
| HOG / GAL / DNA-repair evidence files | **Not read** |
| LeDeaux, Yu & Grossman 1995 Table 1 | **Not read**, in any form |
| Tojo et al. 2013 | **Not read**, in any form |
| Am I Claude Cowork? | No |
| Am I the seat that produced the phage-λ analysis? | No |
| Am I prime? | No |

**Sources opened during this order, exhaustively:**

1. `AOP_CANON_MASTER_v1.26.md` — Drive `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn`
2. `AOP_ChangeSet_v1.25_to_v1.26_RedTeamRemediation.md` — Drive `1mI3DkOKD_GOJzf-ImDThA1oSsRo4iEMd`

Nothing else. No literature search was run, no external database queried, no *B. subtilis* source retrieved.

**Incidental-exposure disclosure:** none. No sporulation knockout phenotype data — spore titres, sporulation frequencies, mutant survival numbers — was encountered at any point. The two files above contain none. The order's §3 architecture sources (Burbulys, Trach & Hoch 1991) were **not** retrieved, since §2 does not require them and §3 has not been authorised.

**Integrity check on the source of truth, performed before reading:**

| Field | Expected (per order) | Observed | Match |
|---|---|---|---|
| Title | `AOP_CANON_MASTER_v1.26.md` | `AOP_CANON_MASTER_v1.26.md` | ✓ |
| Size | 254,046 bytes | 254,046 bytes | ✓ |
| md5 | `54ceb3772e29f25c6e139b703d550d59` | `54ceb3772e29f25c6e139b703d550d59` | ✓ |

Change set as retrieved: 36,796 bytes, md5 `0fcd16d83000d411f549e5bd657201f8` (no hash was specified in the order for this file; recorded for prime's ledger).

**Standing caveat honoured.** v1.26 is a proposal whose 85 changed regions are unverified against the change set. I worked from it as the current line, as instructed, and §2.3 records exactly which of my answers hang on changed text.

---

## 1. Scope of what follows

The order asks one question with a table attached: **what is the minimal mathematical object AOP needs in order to compute B, D, M, and I?**

Two framing points, both from the canon, that govern how the table below must be read — they are not hedges, they change what the table can be used for.

**Nodes are not scalars.** Under the ontology fixed at §1 (v1.26 lines 43–53), Boundary, Drive, Memory and Integration are *conceptual targets*; each carries a **panel** of proxies, and "no single proxy is the node." So "the input object for Boundary" is not well posed as a single answer — it is per-proxy, and the proxies within one panel have genuinely different input requirements. Where a panel splits, the table splits with it. This is the single most consequential structural fact for the question asked, and collapsing it would produce a cleaner table and a wrong one.

**An axis value is not a prediction.** AOP's output on a perturbation is not four axis numbers. It is a **semantic weight** — a viability drop under a declared intervention (§3) — and per §7 (line 248) a semantic weight is a *three-place* quantity: an edge, a declared viable set, and a declared functional **V** evaluated on it, with "report a weight without V and nothing has been reported." §2.2 returns to this, because it dominates the rollup.

---

## 2.1 The four axes

### Boundary (B)

Boundary is a panel, and it splits cleanly into two groups with different input requirements. Per §4 (line 183), **B1 and B2 are Boundary's axis-defining content**; B4 and B5 are explicitly the D→B and I→B edges *read at the interface* — cross-loadings, not the node's own content (§1 ontology, line 53).

| Field | B1 — interior/exterior state contrast | B2 — screening residual I(in;out \| F) | B4 — maintenance burden | B5 — cross-boundary dependence |
|---|---|---|---|---|
| **Canonical quantity** | Declared interior/exterior state contrast (Table 1, §2 line 72) | I(X_in ; X_out \| X_F), the Markov-blanket condition written as a number (§8 line 256) | σ_hk = f·J, housekeeping entropy production at the interface; σ_hk ≈ ½·Δ²·g(g+w)/w (§4 line 131) | I(X_in ; X_out); retained as **descriptive only** — an algebraic component of Integration, not boundary strength (Table 1 line 72) |
| **Input object** | A joint state ensemble over declared interior and exterior variables. Worked case: a static Gaussian covariance Σ with a declared cut | The same joint, **plus a declared interface variable set F**. One instantaneous joint distribution suffices | A nonequilibrium steady state with a declared drive force f and futile-cycle current J — i.e. **rate constants** (leak conductance g, turnover w, contrast Δ) | Same joint as B1/B2 |
| **Partition required?** | **Yes** — declared inside/outside cut. Boundary is one of the two axes carrying the *additional* partition requirement over and above representation-dependence (Table 1 caption, line 63; §2 body, line 90) | **Yes**, and strictly more: a declared cut **and** a declared interface F | **Yes** | **Yes** |
| **Rates required?** | No | No | **Yes** — decisively. σ_hk is a rate | No |
| **Time-asymmetry required?** | No | No | **Yes** — σ_hk is a housekeeping *entropy production*; it inherits Drive's forward/reverse requirement and the reversal convention **R** | No |
| **Computable on topology alone?** | **No.** A wiring diagram carries no state contrast | **Partially** — see note below | **No** | **No** |
| **Computable on a steady-state model, no dynamics?** | **Yes, if** the model emits a *joint distribution* over components. A single optimal flux vector is one point and has no covariance; a sampled flux ensemble does | **Yes**, same condition, plus a declared F | **No** — a growth-rate-emitting steady-state model does not expose the futile-cycle current | **Yes**, same condition as B1 |

**Note on B2 and topology.** The canon establishes (§8 line 256, on a declared Gaussian model) that B2 vanishes exactly when inside and outside interact only *through* the interface, and stays positive when a coupling bypasses it — B2 = 0.000 screened versus 0.292 bypassed, against B5 = 0.896 / 1.685. The step from that to *"on a wiring diagram, B2 = 0 iff the declared interface d-separates inside from outside"* is **my inference, not the canon's**, and it carries a faithfulness assumption: it holds where no accidental parameter cancellation makes a graphically-open path informationally closed. Under that assumption the **zero/nonzero verdict** of B2 is readable off topology; its **magnitude** is not. That is the whole of Boundary's topological reach. `[GRADE: inference from a canon analytic-model-result; faithfulness assumption is mine and is not discharged.]`

---

### Drive (D)

| Field | Report |
|---|---|
| **Canonical quantity** | Entropy production rate **σ**, trajectory time-asymmetry: the relative entropy between the forward and time-reversed trajectory distributions (Table 1 §2 line 77; §2 line 61). The canon is explicit that Drive is measured as entropy-production rate, **not free-energy throughput** (§1 line 28) |
| **Input object** | A **trajectory ensemble**. Equivalently, for a Markov model: a full rate matrix carrying **both** forward and reverse rates, plus its stationary distribution — σ is a functional of the ratio k_ij p_i / k_ji p_j. Plus a declared state-variable set, time grain δt, and reversal convention **R** |
| **Partition required?** | **No.** Drive is representation-dependent — declared state variables, grain δt, and reversal convention R — with **no additional partition required** (Table 1 Drive row, line 78; §2 body, line 90) |
| **Rates required?** | **Yes, and in both directions.** This is the strongest requirement on any axis. A net flux is not enough: σ needs the forward/reverse *ratio*, and a net flux is a difference |
| **Time-asymmetry required?** | **Yes, definitionally** — and v1.26 makes the convention load-bearing rather than decorative. Slot **R** must be declared: "a σ reported without R has not said which involution it is a divergence against" (§12″ line 594; the fourth D→M scope condition, §4 line 125) |
| **Computable on topology alone?** | **No.** Emphatically, and for a reason worth stating: σ = 0 at detailed balance *regardless of topology*. A driven ring and an equilibrium ring are the same wiring diagram. Topology cannot distinguish them, and the distinction is the entire content of the axis |
| **Computable on a steady-state model, no dynamics?** | **No.** A steady-state model that emits net fluxes and a growth rate does not expose the reverse rates σ requires. The stationary distribution alone is insufficient — it is one of two inputs |

---

### Memory (M)

| Field | Report |
|---|---|
| **Canonical quantity** | Excess entropy **E = I(past ; future)**, the past–future mutual information of computational mechanics (Table 1 §2 line 82; §4 line 125). Lead proxy **M1**. Where stationarity fails, the scoped proxy is local (pointwise) active information storage (§5 line 196) |
| **Input object** | A **stationary stochastic process over a declared observable** — operationally, the joint distribution of past and future blocks at a declared time grain δt. Requires a **stationarity claim at that grain**. For a Markov model: rate matrix plus stationary distribution, from which the block statistics follow |
| **Partition required?** | **No.** Representation-dependent — declared observable, time grain δt, stationarity claim — with no additional partition required, given the numerator (Table 1 Memory row, line 83; §2 body, line 90) |
| **Rates required?** | **Yes.** E is a functional of the process's transition structure. Topology fixes which transitions exist, not their statistics |
| **Time-asymmetry required?** | **No** — and this is a genuine and useful asymmetry with Drive. Memory is the **time-symmetric** axis (past-versus-future state), against Drive's directional forward-versus-reverse trajectory (§2 line 61). The canon reinforces this from the other side: the causal irreversibility Ξ = Cμ⁺ − Cμ⁻ is *exactly zero at every drive* (§4 line 125). **Memory needs a time course; it does not need an arrow.** No R declaration is required for E itself |
| **Computable on topology alone?** | **No** — and the failure is harder than the others. Without a declared stationary process at a grain, E is not merely unmeasured, it is **undefined**: "E is defined only for a stationary process, and stationarity is a claim about a chosen time-scale… cross a non-stationarity and E does not merely change value, it loses its definition" (§5 line 194) |
| **Computable on a steady-state model, no dynamics?** | **No.** A model with no time course has no past and no future blocks. There is nothing for I(past;future) to be computed on. This is the cleanest No in the table |

---

### Integration (I)

| Field | Report |
|---|---|
| **Canonical quantity** | Integration panel. Operational default lead proxy: **total correlation TC = Σ H(Xᵢ) − H(X)** across a declared component partition [Watanabe 1960] — chosen as non-negative by construction, monotone in coupling, closed-form in the Gaussian case (§2 line 92). Signed companion where synergy/redundancy character matters: **O-information**. Separate irreducibility diagnostic: **minimum-cut dependence** (renamed from Φ_MIP in v1.26) (§4 line 135) |
| **Input object** | A **joint distribution over the declared components**. Worked case throughout the canon: a static state covariance Σ. Minimum-cut dependence additionally needs a minimum-cut search over bipartitions **and a declared normalizer** (raw, size-normalized and entropy-normalized selectors disagree on which partition is minimal — §4 line 135) |
| **Partition required?** | **Yes** — declared component partition; the second of the two partition-dependent axes (Table 1 caption line 63; §2 body line 90) |
| **Rates required?** | **Partially — see note below.** No rates are needed if a joint distribution is in hand. Rates are needed to *derive* that joint distribution from a mechanism |
| **Time-asymmetry required?** | **No.** TC and minimum-cut dependence are instantaneous cuts of one covariance (§4 line 183) |
| **Computable on topology alone?** | **Partially, and only by model substitution** — see note |
| **Computable on a steady-state model, no dynamics?** | **Yes, if** the model emits a joint distribution / covariance over the declared components. A single deterministic steady-state solution is one point and yields no covariance; an ensemble does |

**Note on Integration and topology.** Integration is the one axis with a canon-internal route from a wiring diagram to a number. The minimum-cut dependence construction is "a minimum-cut search over the static Gaussian covariance **Σ = (I + gL)⁻¹**" (§4 line 135), where L is a graph Laplacian and g a scalar coupling knob. That construction maps *topology plus one declared scalar* onto a covariance, and every Integration proxy then follows in closed form. So: **yes, computable on topology alone, given a declared coupling scalar and the acceptance of that graph→covariance model.**

The caveat is not small and should not be buried. This computes Integration *of a declared Gaussian surrogate whose covariance was generated from the wiring diagram*, not Integration of the system. It substitutes an assumption for the missing dynamics, and the canon is explicit that the construction is AOP's own — built in the lineage of Aguilera & Di Paolo [2019] but "not their measure imported unchanged," carrying "only such warrant as the deposited gate here supplies" (§4 line 135). Any benchmark prediction resting on it inherits that status. `[GRADE: canon-stated construction (SYNTHESIS); the reading of it as a topology→Integration route is mine.]`

---

### Cross-axis structure — the result the table makes visible

Stated separately because it is the finding, not a summary. **The two axes that need a partition and the two that need dynamics are disjoint sets.**

| | No additional partition | Additional partition required |
|---|---|---|
| **Static joint distribution suffices** | — | **Boundary** (B1, B2), **Integration** |
| **Dynamics required** | **Drive**, **Memory** | *(B4 only — a cross-loading, not axis-defining content)* |

The v1.26 T7 recast — representation-dependence (all four) versus partition-dependence (B and I additionally) — is a statement about *what must be declared*. It is not the same split as *what must be measured*, and the two cut the four axes into the same two pairs but for unrelated reasons. B and I are partition-dependent because they are cuts; they are statically computable because they are **instantaneous** cuts. D and M are partition-free because they are read on the whole declared description; they need dynamics because they are read **across time** — D across trajectory direction, M across past/future.

The one entry that crosses the diagonal is B4, and the canon already classifies it correctly as the Drive panel's housekeeping term read at the interface (§4 line 131, line 183). It behaves like Drive because it *is* Drive, read somewhere else. `[GRADE: SYNTHESIS — this is my reading of the canon's own structure, computed from Table 1 and §4. It is not stated as such in v1.26 and should not be cited as canon.]`

---

## 2.2 The rollup — can the four axes be evaluated on a published wiring diagram plus a declared partition, with no kinetic model?

**Partially — Boundary and Integration yes in reduced form, Drive and Memory no — and the two that work are not the two the benchmark needs.**

Precisely: on a wiring diagram plus a declared partition, **Integration** is computable in full closed form, but only by adopting the canon's Σ = (I + gL)⁻¹ substitution, which computes the Integration of a Gaussian surrogate generated from the graph rather than of the system. **Boundary** yields the zero/nonzero verdict of its screening residual B2 as a graph-separation fact under faithfulness, and nothing more — no magnitude on B1 or B2, and nothing at all on B4, which needs rates. **Drive** is not computable, and not approximable: σ is identically zero at detailed balance for every topology, so the wiring diagram is exactly silent on the quantity that defines the axis. **Memory** is not computable, and the failure is categorical rather than practical: without a declared stationary process at a declared grain, E = I(past;future) has no past and no future to be a mutual information between, and per §5 it loses its definition rather than its value.

That is the answer to the question as asked. But the question as asked is narrower than the question behind it, and the gap decides the §3 disposition, so it is stated here rather than left for prime to find.

**AOP's prediction on a perturbation is not an axis value.** It is a semantic weight, and under v1.26 a semantic weight is a viability drop: three-place, requiring an edge, a declared viable set, and a declared functional **V** on it, with no reading available without V (§7 line 248; §12″ line 594). The declared outcome primitive is **lifetime** — mean first-passage time to erasure, or a named member of the persistence-functional family (§1 line 28). The canon's own worked instance declares finite-horizon survival probability on a fully specified 36-state continuous-time Markov chain (§11b line 419). And the intervention that produces the weight must satisfy the six-declaration internal-edge protocol (§3 lines 99–111), of which at least three are irreducibly dynamical: a physical operation that could implement the change, whether resource flow is fixed or free, and whether detailed balance and conservation laws survive it.

A wiring diagram plus a partition supplies none of these. It cannot supply V, because a viable set over what states is not a graph-theoretic object; it cannot supply lifetime, because a first-passage time needs a generator. **So even a full Yes at the axis level would not have made a knockout prediction a desk exercise.** The axes are, in the canon's own ontology, "operations *on* lifetime" (§1 line 43) — and the operand is what the wiring diagram is missing.

**The minimal sufficient object**, stated positively so the R1 build has a target: a continuous-time Markov chain (or a stochastic mass-action model) over declared species states carrying **both-direction** rates; a declared component partition and inside/outside cut; a declared viable set with a functional **V** and a horizon τ; a reversal convention **R**; and a declared intervention class **I**. That is the §10 five-declaration scope condition (line 383) with rate constants added — and the rates are added by D and M specifically, not by the framework's admission criterion, which the five declarations alone satisfy.

**Consequence for §3, flagged not decided.** Under the order's §3 gate — "runs only if Step 0 returns Yes or a workable Partially" — this return is a Partially whose workable half is Integration-under-a-substitution and a Boundary yes/no verdict. Whether that constitutes a *workable* Partially for a discrimination check against Rival P is Ben's and prime's ruling, not mine. I record only what the Partially consists of, and note that the discrimination question the order poses — does AOP say something different from a path-count rival — is sharpened rather than blocked by this finding: on a wiring diagram plus a partition, the AOP quantity that *is* computable (Integration via Σ = (I + gL)⁻¹) is a functional of the graph Laplacian, and Rival P is a functional of graph connectivity. Whether two functionals of the same graph can differ on the scored conditions is a well-posed question that does not need rates to ask. **I have not asked it. §3 is not begun.**

---

## 2.3 Verification coupling — which answers rest on changed regions

Every canon line this report relies on was checked against the 85 changed regions enumerated in the change set §4 machine diff. **20 of 29 relied-on lines fall inside changed regions.** That headline number is not useful on its own, because the regions differ in whether they *create* an answer or merely *restate* one inherited from byte-identical text. Graded accordingly, for prime's queue.

### Tier 1 — answers that exist ONLY because of v1.26 text. Verify these first.

| v1.26 lines | Task | What of mine depends on it |
|---|---|---|
| **90** | T7 | The entire representation- vs partition-dependence framing the order instructs me to use. Every "Partition required?" row |
| **99–111** | T20a, T20c | The six-declaration intervention protocol and the coalition default. My §2.2 finding that the prediction layer is dynamically bottlenecked rests on this insert, which is **new text with no v1.25 antecedent** |
| **592–596** | T6, T11.2, T13, T20c | The declaration tuple block making **R, V, I** load-bearing. My "no semantic reading without V" and the R requirement on Drive |
| **383** | T18b | The five-declaration operational scope condition. §10 was **entirely replaced**; the prior domain wall was a different construction. My "minimal sufficient object" is stated against this |
| **248** | T13 | Semantic weight as three-place (edge, viable set, V). §7 rewritten; "the system is its own observer" dropped. Load-bearing for the §2.2 rollup |
| **125** | T11 | The fourth D→M scope condition (time-reversal parity) and R as load-bearing. My Drive "time-asymmetry required" answer and its R clause |
| **608** | T20c/E2 | The per-edge mask's usable band (κ ≲ 9, gap > 3× blur, TC ≲ 0.5, minimum-cut dependence ∈ [0.0003, 0.05]). Not used in the §2.1 table, but any §3 per-edge reading must clear it |

### Tier 2 — answers reframed by v1.26 over an unchanged underlying quantity.

| v1.26 lines | Task | Dependency |
|---|---|---|
| **63, 78, 83** | T7 | Table 1 caption and the Drive/Memory rows. The **quantities** σ and E are unchanged; what changed is the dependence column ("None: cleanly computable" → representation-dependent). My input-object answers survive a failure here; my partition answers do not |
| **28** | T8 | MFPT was already the lead primitive; the **persistence-functional family** (survival curve, hazard, finite-horizon, recovery probability) and the four inappropriate regimes are new. My "declared outcome primitive is lifetime" is inherited; the family is not |
| **135** | T14 | Rename to minimum-cut dependence, the Provenance block, and the deletion of positivity→individuality. The **Σ = (I + gL)⁻¹ construction itself predates v1.26**; what is new is its attribution and the refusal built on it |
| **183** | T2 | B1/B2 as Boundary's axis-defining content with B4/B5 as cross-loadings. This predates v1.26 (it is the v1.20 B-lead-scalar fix); the v1.26 edit narrowed "dissociate generically" to "throughout the declared Gaussian ensemble" |
| **256** | T18c | The B2 screening computation. The change set certifies the **numbers as retained verbatim** (B2 = 0.000/0.292, B5 = 0.896/1.685) while the surrounding line was replaced to add that it is a property of the declared Gaussian model. My B2 answer uses the numbers (unchanged) and the scoping (changed) |
| **96** | T20a | KW intervene on the system–environment channel; internal-edge intervention is AOP's unlicensed extension. Frames §2.2 but does not change any §2.1 cell |
| **43** | T6 | The "ontology, fixed once" block — nodes are targets, proxies are families, lifetime is the primitive. **New front-of-paper text.** My §1 framing point that a node is not a scalar rests on it |
| **600** | T20b/c | §13 exposure statement. Corroborative only |

### Tier 3 — answers resting on byte-identical carryover. Lowest verification priority.

v1.26 lines **61** (four as relative entropies; Memory time-symmetric, Drive directional), **72** (Table 1 Boundary row and its panel), **87** (Table 1 Integration row), **92** (Integration measure ambiguity; TC as operational default), **131** (D→B conditional; B4 = σ_hk = f·J and the ½Δ²g(g+w)/w form), **194** (E defined only for a stationary process; definedness is grain-relative), **196** (local active information storage as the off-stationarity proxy), **230** (resolvability read on the precision partition K), **419** (§11b's 36-state CTMC and its finite-horizon V).

These carry the load for the **Rates required?**, **Time-asymmetry required?** and **Computable on topology alone?** columns — which is a good outcome for the report's robustness: the *measurement* requirements are inherited from pre-v1.26 canon, and only the *declaration* requirements are new. My Memory answers in particular rest almost entirely on Tier 3.

### Summary list, in the form the order requested

> Answers **B/D/M/I "Partition required?"**, and the whole T7 framing, depend on changed regions **63, 78, 83, 90**.
> Answer **§2.2's prediction-layer bottleneck** depends on changed regions **99–111, 248, 383, 592–596**.
> Answer **Drive "time-asymmetry required" (R clause)** depends on changed region **125**.
> Answer **Integration "computable on topology alone"** depends on changed region **135** for attribution, but on **unchanged** text for the construction itself.
> Answer **Boundary "computable on topology alone"** depends on changed region **256** for scoping and **183** for the B1/B2 lead, but on **unchanged** text (line 72) for the panel roster.
> Answers **all "Rates required?" and "Time-asymmetry required?" cells** rest predominantly on **unchanged** regions (61, 72, 87, 92, 131, 194).

**Nothing in this report treats a changed region as settled.** Where an answer is Tier 1, it is flagged above rather than asserted.

---

## 2.4 HALT

§2 is complete. **This report stops here.** §3 — the discrimination pre-registration — is **not begun**: no rival was scored, no perturbation list was retrieved, no partition was declared for a phosphorelay, no AOP prediction was generated. `AOP_Benchmark_Sporulation_Conditions_REDACTED_v0.1.md` was not opened and its presence on Drive was not checked.

Ben and prime rule on what §3 becomes.

---

## 3. Grading of this report's own claims

Per charter, so the reader can always tell which is which.

| Claim | Grade |
|---|---|
| The canonical quantity, input object, partition/rate/asymmetry requirements per axis | **Canon-reported.** Read off v1.26 with section references; not my synthesis. Subject to the v1.26-unverified caveat |
| B2's zero/nonzero verdict is readable off topology under faithfulness | **My inference.** Canon supplies only the Gaussian-model computation; the graphical reading and its faithfulness assumption are mine and undischarged |
| Σ = (I + gL)⁻¹ constitutes a topology→Integration route | **My reading** of a canon-stated construction. The construction is canon (SYNTHESIS-graded there); the reading of it as a benchmark-enabling route is mine |
| The partition-dependent and dynamics-dependent axis pairs are disjoint | **My synthesis**, computed from Table 1 and §4. Not stated in v1.26; do not cite as canon |
| Memory fails on topology by *undefinedness* rather than by unmeasurability | **Canon-reported** (§5 line 194), applied by me to the topology case |
| The prediction layer, not the axis layer, is the binding constraint | **My synthesis**, assembled from §1 (line 28), §3 (99–111), §7 (248) and §11b (419). This is the report's principal finding and the one most worth attacking |
| Anything about *B. subtilis*, sporulation, phosphorelay behaviour, or knockout outcomes | **Not claimed.** No such source was read |

I have not graded my own output for correctness; per the order's §5, prime verifies by re-running.

---

*End of Step 0 report. Halt per §2.4.*
