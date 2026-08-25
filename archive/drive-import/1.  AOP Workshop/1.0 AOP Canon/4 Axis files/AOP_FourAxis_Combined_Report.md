# AOP — Four-Axis Deepening & Gap-Closing Plan (canon v1.19)

**Prime synthesis, 20 July 2026.** Built from four parallel axis groups (Boundary, Drive, Memory,
Integration), a cross-axis reconciliation against the dependence map, and a literature-first gap-closure
pass. Sources: `AOP_CANON_MASTER_v1.19.md` (the canon, read in full), the operational-panels spec,
`FourAxis_State_Report_rev2.md`, and `aop_depmap.py`. Grading: **SETTLED / SYNTHESIS / FRONTIER /
DEFECT**. Verification: ✓ primary read this session · ~ named/abstract · ⊙ canon-inherited (already
verified) · ? unread lead.

> **Startup check — 20 July 2026**
> [✓] AOP Charter — the governing charter (project-instructions v1.0; a v6 charter also sits on Drive, dated 19 Jul — noted, non-blocking, flagged below).
> [✓] AOP Canon (the paper) — **v1.19**, confirmed current against the Drive master `AOP_CANON_MASTER_v1.19.md` (matches the uploaded rev.2 state report).
> [✓] Operational panels spec (B/D/M/I proxy families + declaration tuple D).
> Drive connector: **on** (used for primary-source verification of new literature).

---

## 0. Executive summary — the three headlines

**(1) Your intuition holds: this is a synthesis job, not an invention job.** Of the ~14 substantive
open items surfaced across the four axes, the literature-first pass closes almost all of them by
**citation** or **synthesis of existing results**. Exactly **one** requires genuinely new work — a
*non-stationary / time-varying* Φ_MIP (a minimum-information-partition that moves as the system
develops). Everything else is either a canon edit, a citation of settled science, or a small
closed-form computation applying settled machinery. "Close to all of it" was the right call.

**(2) The skeptical check paid for itself — one current AOP claim is likely wrong.** The state report's
reading that **Drive's leverage on lifetime is "geometry-set, no rule"** does not survive the
literature. For AOP's exact regime — a divergence-free current added at *fixed stationary distribution*,
small-noise limit — there is a **settled, one-sided rule**: measure-preserving circulation can only
**shorten or leave unchanged** the mean first-passage time; it can *never* lengthen it
[Lee & Seo 2021 ✓; Bouchet–Reygner 2016 ~]. The ring's anti-persistence is the general behavior; the
**star's apparent pro-persistence contradicts the theorem and must be reconciled** (finite-noise
prefactor effect, or — more likely — a hypothesis violation: a star cannot carry a genuinely
divergence-free current at fixed stationary distribution). This is exactly the charter's "be skeptical
of anything that looks new" working as designed: treat the pro-persistent prediction as **not real
until it survives the check**. This is the single most important scientific result of the exercise.

**(3) All four groups independently flagged the same DEFECT — and it strengthens the framework.** The
canon states in three places (Fig T caption, Table 2 M–I row, §4 body) that Memory's correlation with
Boundary and Integration is "|corr| < 0.05." **This is a misreport.** The measured *raw* Spearman is
~0.61; 0.05 is the *partial* after controlling for coupling strength. The honest — and stronger —
statement is that the axes are **dissociable, not orthogonal**: Memory carries 0.59 unique rank-variance
(the most of any axis) and comes apart completely by construction, but shares coupling strength with the
others. Reword, don't retract. Boundary carries a second, structural DEFECT (the lead-scalar problem)
that is the same nesting identity seen twice.

The rest of this report: the four axes condensed (§1), the cross-axis map and the unified
persister-identification table — the "process, not the husk" mandate (§2), the canon corrections that
fall out (§3), the master gap register with literature-first verdicts (§4), and the phased scientific
plan (§5).

---

## 1. The four axes, condensed

Full dossiers are preserved as `axis_B.md`, `axis_D.md`, `axis_M.md`, `axis_I.md`. Condensed here.

### 1.1 Boundary (space) — soft; carries a DEFECT
Target: a maintained interior/exterior separation held over time; a computed difference across a
*declared* cut, never a membrane you can point at. Read as a **panel** (B1 state contrast · B2 interface
mediation / screening `I(in;out|F)` · B3 leakage · B4 maintenance burden · B5 cross-boundary dependence
`I(in;out)`), not a scalar. **Settled core:** *screenability* (§8) — which interactions can build a
boundary at all. Electromagnetism screens (Debye length λ_D, exponential; ✓); the strong force confines,
the weak force is short-ranged, neither builds a statistical boundary; **gravity is the anti-boundary
interaction** — unscreenable, infinite-ranged, non-additive, so its only boundary is causal. This maps
cleanly onto the **Markov-blanket** condition (B2 = a scalarized blanket test; Pearl ✓). **DEFECT:** the
old Table-1 lead proxy is B5 = `I(in;out)`, which measures *dependence across the cut* (high = coupled =
nearer "no boundary") and, worse, is **literally a slice of Integration** (see §2.1). Lead with B1/B2/B4
instead.

### 1.2 Drive (energy) — the cleanest axis and the hub
Target: sustained trajectory-level irreversibility holding the system off equilibrium. Formal quantity
σ = lim (1/τ) D_KL(P_fwd‖P_rev) [Parrondo–Van den Broeck–Kawai 2009 ⊙]; measurable as a lower bound from
a time series and its reverse [Roldán–Parrondo 2012 ✓], and measured in real persisters (cells
[Battle 2016 ⊙], brain [Lynn 2021 ⊙]). **No lead-scalar DEFECT** — σ = D5 is the correct object, though
if only D5 is computed the axis should be *labelled* "Dissipation/Irreversibility" (σ is what is thrown
away, not resource input D1 or useful work D2). **The load-bearing result:** Drive acts on **lifetime,
not occupancy** — a divergence-free current cuts lifetime ~5.7× while leaving occupancy invariant to
1e-14, which is why "persistence = occupancy" was retracted and why Drive has *direct* leverage. The
star is the flagship (§2.2). Two forced spokes only (D→M floor, D→Reliability/TUR); the reason is the
**sector split** (σ̇ lives in the generator's antisymmetric sector). Traps, all named/fixed:
σ = throughput; persistence = occupancy; the E vs "excess entropy production" name collision.

### 1.3 Memory (time) — the most distinct axis
Target: predictive structure carried across time. Lead quantity E = I(past; future), the past–future
mutual information = **predictive information** [Bialek–Nemenman–Tishby 2001 ✓; Crutchfield–Feldman
2003 ⊙]. Panel: M1 predictive dependence (E) · M2 stored state (Cμ) · M3 active info storage · M4
retention depth · M5 semantic. **Most distinct axis: 0.59 unique rank-variance.** Its ~0.61 raw
correlation with B and I is *shared coupling strength only* — controlling coupling, B–M → −0.05 (free),
I–M → −0.62 (mild tradeoff). It dissociates completely by construction (pure-memory corner E=4.98 at
B=I=0). Two real holes: **(a) the numerator** — the D→M floor forces E, but the spore forces Cμ; the
diagnostic that separates them is **crypticity χ = Cμ − E** [Crutchfield–Ellison–Mahoney 2009 ⊙]; and
**(b) definedness off-stationarity** — E exists only for a stationary process, so it doesn't rescale
across a non-stationarity, it *vanishes* (the star's nuclear clock; development; aging).

### 1.4 Integration (parts) — no canonical measure; owns the resolvability blur
Target: how much the parts are one interdependent whole. **No canonical measure** — six Φ's agree on
rank but disagree on value and sign [Mediano–Seth–Barrett 2019 ✓]; direction survives measure choice,
magnitude does not [Comolatti–Hoel 2025 ✓]. So AOP inherits the ambiguity but not its stakes: every
Integration claim is **directional**, no exact value load-bearing. Three coordinates kept distinct: **TC**
(interdependence, operational default; Watanabe 1960 ⊙), **Φ_MIP** (one-vs-many individuation, zero on
block-decomposable systems; Aguilera–Di Paolo 2019 ✓), and **resolvability blur** (not a measure — the
mask's failure on strongly-integrated systems). The **F2 seam** — nested-level + non-stationary Φ_MIP —
is the framework's principal open problem: it bottlenecks both "a superorganism is one individual" (§9)
and "a collective can be alive" (§9a). Traps: TC = unity (it's interdependence, not proven irreducible
wholeness); measure-shopping for a sign; entanglement entropy for classical persisters.

---

## 2. Cross-axis synthesis

### 2.1 The dependence map, typed (from `aop_depmap.py`, 4000 VAR(1) + corners)

The reframe stands: correlation between axes is a **finding to type**, not a failure to fix. The
question is never "does each axis survive?" (they all dissociate — see the corners) but "**what *is* the
relationship?**"

| Pair | Raw ρ | Partial (ctrl 3rd) | Partial (ctrl coupling) | Type | Grade |
|---|---|---|---|---|---|
| **B–I** | 0.83 | 0.73 (ctrl M) | — | **nested — an identity** | SETTLED (algebraic) |
| **B–M** | 0.61 | 0.24 (ctrl I) | **−0.05** | **free** (tie is coupling only) | analytic-model-result |
| **I–M** | 0.61 | 0.22 (ctrl B) | **−0.62** | **shared-driver + mild tradeoff** (suggestive) | SYNTHESIS |
| **D→M** | — | — | — | **forced floor**, σ>0⇒E>0 (E only) | SETTLED (direction) |
| **D→Reliability** | — | — | — | **forced**, TUR, regime-bounded | SETTLED |
| **D→B** | — | — | — | **conditional** (= B4, uncomputed) | SYNTHESIS |
| **D→I** | — | — | — | **free static / tendency dynamic** (§3.4) | SETTLED / FRONTIER |

**The load-bearing structural fact — B–I is a nesting identity, not a correlation.** Exact, machine-
precision (max err **1.8e-15** over 4000 systems):

> **TC = I(in;out) + TC_in + TC_out**

Boundary's lead proxy `I(in;out)` is the **cross-cut slice** of Integration's total correlation; the rest
is within-side structure. The 0.83 correlation *is* this identity showing through — both are static cuts
of the same covariance. This single fact does double duty: it is why B–I co-move, and it is *why the
Boundary DEFECT is a DEFECT* — scoring "Boundary" as B5 double-counts a piece already inside Integration.
Reporting rule: report Boundary separately only where the cross-cut slice carries persistence weight, and
lead with the non-TC proxies (B1/B2/B4).

**Unique rank-variance:** Memory 0.59 (most distinct) · Boundary 0.29 · Integration 0.29. Drive sits
*outside* this static B–I–E map (σ is a trajectory object) and reaches the triangle only through its two
forced floor-type spokes — which is itself the finding: the hub couples in narrowly, not everywhere.

**Dissociation corners (B, I, E)** — every axis comes apart by construction: sealed modules (0, 1.53, 0)
= Integration without Boundary; cross-cut only (1.01, 1.01, 0) = Boundary = Integration; all-coupled
memoryless (0.29, 0.73, 0) = coupling without Memory; pure memory (0, 0, 4.98) = Memory alone.
**Dissociable, not orthogonal** is the exact, defensible claim.

### 2.2 The persister, not the husk — unified identification table

The point of the exercise, per your steer: for every case, name the **process** that persists, never
the physical object. The husk is the corpse of the process, not the process.

| Case | **The persister (process)** | The husk / corpse | Present-tense type (§9) | Diachronic test (§4a) |
|---|---|---|---|---|
| **Crystal** | *was* the **growth front** — drive depositing lattice order | the grown lattice you hold (memory made solid, drive→0, terminal) | configuration, **spent** | fails: nothing maintained across the interface *now* |
| **Flame** | the **combustion front** rebuilt each instant from current supply | this instant's gas parcel (wholly replaced) | process | same process by continuity through total turnover; **no** self-restart (no held state) |
| **Spore** | a **paused process** — regulatory/boundary architecture present, drive off, viability in escrow | the coat *mistaken for a blueprint* (a description would be *dead*) | capacity | **restarts itself** from its own held state → same process; held-state ≠ description |
| **Bound atom** | the **bound EM process** holding a localized interior | a free electron + proton (bound nothing) | configuration/process | minimal admitted persister |
| **Star** | the **self-regulating hydrostatic + fusion process** | the ball of gas; the remnant once fusion ceases | process — **corrects but model-free ⇒ not alive** | no self-restart; kill drive → dies on a Kelvin–Helmholtz time; remnant is a *new* process |
| **Galaxy** | a **gravitationally bound, membrane-free process** | — (no material skin to leave) | configuration/process | continuity of instantiation on the galactic clock |
| **Dissipative structure** (Bénard, BZ, driven ring) | the **maintained ordered flow pattern** | the vessel + medium (molecules cycle through) | process — order present only while σ>0 | limit-cycle → has restoring force; marginally-stable → flame-like |
| **ε-machine / hidden process** | the **generating structure** (its causal-state machine) | any single sampled trajectory (a record) | process | a printed realization is a record → re-enacting it is a *new* process |
| **Multicellular collective** | the **cooperating whole** — but *one* persister only if Φ_MIP > 0 at the part-partition (§9a) | the pile of cells (a corpse = parts that stopped cohering) | process | continuity of the integrated physiology |
| **Two independent modules** | **two** persisters, not one (Φ_MIP = 0 though TC high) | — | two processes | the decisive negative case: TC ≠ individuation |
| **Virion (naked)** | a **propagation blueprint with the engine off** — reproduces, not alive (no decoupled self-model; §11a) | — | — | fails both living tiers; the spore's false twin |
| **Mule / sterile worker** | a **fully alive process** with zero reproduction | — | process, alive | alive ≠ reproducing — the mirror of the virion |

Two structural notes the table forces: **the persister is almost always the process, and the husk is
what the process leaves behind when a specific axis's semantics are spent** (crystal = spent Drive;
frozen lattice = spent Integration; a genome print = the spore's held-state degraded to a mere
description). And **"which axis is the persister carried on" differs by case** — the flame lives on
Boundary+Drive, the spore on stored structure (Cμ, an Integration/Memory escrow), the star on Drive, the
ε-machine on Memory. Naming the persister *is* naming which axes bear its weight now.

### 2.3 The star, worked across all four axes (the hard case you flagged)

The star is where all four axes go near-maximal and entangled, and where the framework's own instrument
goes soft — which is why it earns a corner none of the other cases occupy. **Persister = the
self-regulating hydrostatic+fusion process.** **Drive** is the defining axis: fusion is a coherent
central entropy source resupplying, against radiative loss, the thermal pressure that balances gravity;
its negative-specific-heat thermostat is a *present* restoring force (checkable now — hydrostatic +
thermal balance — not teleology), which is what distinguishes the star (strong restoring force) from the
flame (marginally stable, none). **Boundary** is *two* load-bearing boundaries of different force-types:
the unscreenable causal boundary from gravitational binding, and a genuine screening photosphere
(scramble its opacity and the star stops being a star). **Integration** is very high and non-separable
(hydrostatic equilibrium locks every shell), which drives the star into the resolvability trough from its
own physics (Lane–Emden n=3 → tridiagonal shell operator → graded stiff/sloppy band, Figure R★).
**Memory** has *no single value*: E is defined on the thermal clock, undefined on the nuclear clock — the
time-grain relativity made physical, and the sharpest tension in the paper (the cleanest forced Memory
law goes silent on the flagship's nuclear clock).

The **single settled root** ties three of these together: gravitational non-additivity (negative specific
heat) is the common cause of the anti-boundary character, the Integration floor, *and* the self-
regulation. **New primary source (✓ this session):** the founding establishment is **Lynden-Bell & Wood
1968** (the gravothermal catastrophe), which is stronger than the Campa–Dauxois–Ruffo 2009 *review* the
canon currently leans on — cite the 1968 primary alongside the review. And the star **corrects but is
model-free** (set-point baked into the constitutive dynamics, no separately-interventable reference), so
by §11a it is **not alive** — the worked proof that drive + a genuine restoring force is not life.

---

## 3. Canon corrections that fall out of this work

These are the concrete edits the deepening produced. All are **synthesis/DEFECT-fix**, none require new
science, and every one either preserves or *strengthens* the underlying claim.

**3.1 The "|corr| < 0.05" over-claim (DEFECT → reword).** Fig T caption, Table 2 M–I row, and the §4 body
report a *conditioned* correlation as if it were the raw one. Replace with the measured dependence:
*Memory shares only coupling strength with the B–I plane (raw |corr| ≈ 0.61); controlling for coupling,
B–M → −0.05 and I–M → −0.62; Memory carries 0.59 unique rank-variance and dissociates completely by
construction — the most distinct of the four axes.* Flagged independently by all four axis groups.

**3.2 Boundary lead-scalar (DEFECT → reword + reclassify).** Stop leading Boundary with B5 = `I(in;out)`.
Lead with B1/B2/B4 (genuinely Boundary-specific, non-TC content), and report B5 as "the cross-cut slice
of Integration, flagged where that slice carries weight," per the nesting identity.

**3.3 Drive→lifetime sign (reframe — this one changes a claim).** Retire the "geometry sets the sign, no
rule" framing for the fixed-measure small-noise regime. The rule exists and is one-sided: measure-
preserving circulation can only shorten/neutralize MFPT [Lee–Seo 2021 ✓]. State the ring result as the
*expected* behavior, and demote the star's apparent pro-persistence to a **claim to be reconciled** (finite-noise, or a hypothesis violation — a star carries no divergence-free current at fixed stationary distribution). Do not assert two-sided geometry-dependence.

**3.4 Sector-split status (upgrade FRONTIER → SETTLED for half).** The σ̇ = antisymmetric-sector claim
generalizes beyond OU/finite-Markov: it is the frenesy / entropy-production decomposition
[Da Costa et al. 2023 ✓; Maes 2020 ~; Schnakenberg 1976]. Cite these; keep a SYNTHESIS tag on the *full*
no-cross-coupling claim pending a one-line lemma that AOP's Memory functionals (equal-time covariance;
Ξ) are time-symmetric observables.

**3.5 D→I dynamic edge (grade honestly as tendency, not law).** State it as a conditional
tendency/necessity: robust size-extensive integration is *impossible* at equilibrium and *requires*
far-from-equilibrium dynamics [arXiv:2410.13375 ~], and maintaining correlation carries a dissipative
cost [Parrondo et al. 2015 ~]. **Do not** cite MaxEP (not a settled principle, per its own advocate
Martyushev ✓) or England's dissipative adaptation (a Perspective, unproven, and about *dissipation* not
*integration*) as if either were a law.

**3.6 Governance note (non-scientific).** The project-instructions charter reads v1.0 while a Drive
charter reads "V6" (19 Jul). Worth reconciling which is authoritative — a governance housekeeping item,
not a canon change.

---

## 4. Master gap register with literature-first verdicts

The charter rule ("don't create when you can cite; verify before believing") was applied to every gap.
Verdicts: **CITE** (a published result settles it) · **SYNTHESIS** (assemble/edit; no new science) ·
**COMPUTE** (small closed-form, settled machinery, no new theory) · **NEW WORK** (genuine invention).

| # | Gap | Verdict | What closes it (verified) | Grade |
|---|---|---|---|---|
| 1 | "|corr|<0.05" over-claim | **SYNTHESIS** | reword to measured dependence — numbers already in `aop_depmap.py` | DEFECT-fix |
| 2 | Boundary lead-scalar | **SYNTHESIS** | lead B1/B2/B4; report B5 as slice of TC (nesting identity) | DEFECT-fix |
| 3 | Compute B2 (screening residual `I(in;out|F)`) | **COMPUTE** | Gaussian conditional MI, Schur complement on existing model; Pearl blanket ✓, Faes 2017 ⊙ | small |
| 4 | Compute B4 / the D→B edge | **CITE + COMPUTE** | housekeeping entropy production σ_hk = ΣJ·X; Hatano–Sasa 2001 ✓, Speck–Seifert 2005 ✓, Oono–Paniconi 1998; Na/K-ATPase 20–45% ✓; closed-form pump+leak | SETTLED machinery |
| 5 | Screening ↔ conditional-independence (Debye ↔ blanket) | **CITE** | exponential decay over λ_D: Debye–Hückel, Ornstein–Zernike, field-theory screening ✓; *not novel* (underscreening caveat) | SETTLED |
| 6 | **Drive→lifetime SIGN** | **CITE (refutes framing)** | Lee–Seo 2021 ✓: measure-preserving circulation never lengthens MFPT; Bouchet–Reygner 2016 ~ | SETTLED |
| 7 | Sector-split generality (σ̇ half) | **CITE** | Da Costa et al. 2023 ✓ (ep = antisymmetric only, arbitrary diffusions); Maes frenesy ~; Schnakenberg | SETTLED |
| 7b | Sector-split (full no-cross-coupling) | **SYNTHESIS** | one lemma: AOP's Memory functionals are time-symmetric | SYNTHESIS |
| 8 | D→I dynamic edge | **CITE (as tendency)** | arXiv:2410.13375 ~ (dissipation necessary for robust extensive correlation) + Parrondo 2015 ~; NOT MaxEP/England | FRONTIER/tendency |
| 9 | F2 seam — level selection | **SYNTHESIS** | maximize-Φ rule: Hoel et al. 2016 ✓, Marshall et al. 2026 ✓; Gaussian analytic bridge Zhang et al. 2025 ✓; frame graded per Krakauer 2020 ✓ | SYNTHESIS |
| 10 | F2 seam — critical Φ_MIP | **CITE** | Aguilera–Di Paolo 2019 ✓: Φ diverges at criticality in the thermodynamic limit | SETTLED |
| 11 | **F2 seam — non-stationary / moving MIP** | **NEW WORK** | no source defines Φ_MIP under time-varying covariance; the one genuine invention | FRONTIER |
| 12 | Memory numerator (E vs Cμ) | **SYNTHESIS** | state E = forced numerator, Cμ = persistence-relevant, χ = Cμ−E the divergence diagnostic [Crutchfield–Ellison–Mahoney ⊙] | SYNTHESIS |
| 13 | Memory off-stationarity definedness | **CITE (partial)** | local AIS defined pointwise, stationarity-free: Lizier 2012 ✓, Wibral–Lizier 2014 ✓; honest residual: instantaneous stored *amount* has no clean pathwise definition [Spinney 2018 ✓] | SETTLED + residual |
| 14 | Small closed-form computations to just run | **COMPUTE** | O-info sign on star (I2); E(T) retention curves (M4); mask on a memory edge (M5) and on a well-posed part-partition (I3) | small |

**Score:** of 15 rows, **1 is genuine new work** (row 11). Six close by citation, five by synthesis/edit,
three are small closed-form computations that apply settled machinery. Your "we don't need to invent
anything — or close to it" intuition is **confirmed**, with the single, well-defined exception of the
non-stationary moving-MIP.

---

## 5. The scientific plan (prioritized, literature-first, phased)

Ordered so that no computation is run before the literature has been mined, and cheap high-value fixes
land before expensive open problems.

**Phase A — Canon corrections (no new science; do first).**
Reword the three over-claims/reframes (§3.1 |corr|; §3.2 Boundary lead; §3.3 Drive-sign) and upgrade the
sector-split status (§3.4) and D→I grade (§3.5). Fold the E/Cμ/crypticity statement (row 12) and the
local-AIS non-stationary Memory proxy (row 13) into the Memory panel. Add Lynden-Bell & Wood 1968 as the
star's founding primary. These are edits the deepening already justifies; each strengthens or honestly
grades an existing claim. *Propagation: the Drive-sign reframe and the sector-split upgrade touch the hub
inventory → cross-project (Ladder) bus note.*

**Phase B — Reconcile the Drive→lifetime sign (highest-value single scientific task).**
Before any new AOP claim about Drive and persistence: pin down why the star reads pro-persistent against
a theorem that forbids it. Check (a) the finite-noise regime (the μ^σ ≥ λ^σ ordering is an ε→0
statement), and (b) whether the star even satisfies the hypotheses (a divergence-free current at fixed
stationary distribution; a Kramers saddle). Likely outcome: the star's "current" is not a measure-
preserving circulation, so the theorem simply does not bind it — in which case AOP states the two regimes
separately rather than as "geometry-dependent." One targeted computation (generalize the ring gate to a
system with a genuine barrier + tunable circulation) confirms the reconciliation. *This decides whether
"Drive lengthens persistence" is ever a clean statement.*

**Phase C — Closed-form computations that apply settled machinery (cite-then-compute).**
Each of these turns an asserted edge into a number using tools verified above; none is new theory.
Compute **B2** (screening residual, Schur-complement conditional MI on the existing model) and **B4**
(housekeeping σ_hk on a two-state pump+leak model → recovers "free at equilibrium, ∝ leakiness"),
unifying Boundary with Drive. Run the small ones: **O-info sign** on the star (redundancy vs synergy),
**E(T) retention curves** for the spore-type and cell-type OU systems (M4 regime classification), and
the **mask on a memory-bearing edge** (M5) and on a **well-posed part-partition** (the standing §13
deliverable). Check the recent PRR "Information thermodynamics of cellular ion pumps" first — B4 may
already be published verbatim.

**Phase D — The F2 seam (the one genuine frontier).**
Split it as the literature splits it. **Level-selection is synthesizable now:** adopt the
maximize-integration ordering (Hoel et al. 2016 ✓, Marshall et al. 2026 ✓), port it to AOP's static-
Gaussian scope via the closed-form Gaussian effective-information / eigenvalue construction (Zhang et al.
2025 ✓), and frame the output **graded** (Krakauer et al. 2020 ✓) so it stays consistent with AOP's
refusal to individuate — Φ_MIP-max as a syntactic *ordering* over levels, with the viability layer
reading out which level(s) matter. **Criticality is a citation** (Aguilera–Di Paolo 2019 ✓). What
remains genuinely open is the **non-stationary / time-varying MIP** — defining the minimum-information-
partition when the covariance itself moves as the system develops. This is the single piece to *build*,
and it is worth building because it unlocks both the §9 higher-individual route and the §9a collective-
alive question at once. Because it needs a model class with a phase transition and a moving partition,
prefer an analytic/closed-form construction (per the charter) over an estimated one.

**Provenance honesty for the plan.** Two literature items the plan leans on were read at abstract/result
level only and should be line-checked before the canon rests weight on them: **arXiv:2410.13375**
(the dissipation-necessary-for-extensive-correlation theorem — check the "robust" definition and
permutation-invariance assumptions) and **Bouchet–Reygner 2016** (full text was blocked; the decisive
sign result is Lee–Seo 2021, which *was* read ✓). The Aguilera 2019 *Entropy* Gaussian-criticality
companion is an unread lead (?).

---

## 6. References with verification markers

**Verified against primary source this session (✓):**
- Lee J, Seo I. Non-reversible metastable diffusions with Gibbs invariant measure I. *Probab. Theory Relat. Fields* (2021); arXiv:2008.08291. — measure-preserving circulation never lengthens MFPT (Thm 3.5, Lemma 3.4, Cor 3.9). *[Drive-sign, row 6]*
- Da Costa L, Barp A, et al. The entropy production of stationary diffusions. *J. Phys. A* 56, 365001 (2023); arXiv:2212.05125. — ep depends only on the antisymmetric drift, general (non-Gaussian, degenerate) diffusions. *[sector split, row 7]*
- Hatano T, Sasa S. Steady-state thermodynamics of Langevin systems. *PRL* 86, 3463 (2001). — housekeeping/excess split. *[B4, row 4]*
- Speck T, Seifert U. Integral fluctuation theorem for the housekeeping heat. *J. Phys. A* 38, L581 (2005). *[B4, row 4]*
- Hoel EP, Albantakis L, Marshall W, Tononi G. Can the macro beat the micro? *Neurosci. Consciousness* 2016, niw012. — the Φ-max grain fixes the level. *[F2 level-selection, row 9]*
- Marshall W, et al. Intrinsic units: identifying a system's causal grain. *Neurosci. Consciousness* 2026, niag013. *[row 9]*
- Zhang/Zhao et al. An exact theory of causal emergence for linear stochastic iteration systems. *npj Complexity* (2025); arXiv:2405.09207. — closed-form Gaussian effective information; optimal coarse-graining from the dynamics-matrix eigenvalues. *[row 9, Gaussian bridge]*
- Krakauer D, Bertschinger N, Olbrich E, Flack J, Ay N. The information theory of individuality. *Theory Biosci.* 139, 209 (2020); arXiv:1412.2447. — graded, nested individuality; refuses a single privileged level. *[row 9]*
- Aguilera M, Di Paolo EA. Integrated information in the thermodynamic limit. *Neural Networks* 114, 136 (2019). — Φ diverges at criticality in the thermodynamic limit; stationary-anchored. *[rows 10, 11]*
- Mediano PAM, Seth AK, Barrett AB. Measuring integrated information. *Entropy* 21, 17 (2019). — six measures disagree on value/sign. *[Integration]*
- Comolatti R, Hoel E. Consilience in causation. *Entropy* 27, 825 (2025). — direction survives, magnitude does not. *[Integration]*
- Bialek W, Nemenman I, Tishby N. Predictability, complexity, and learning. *Neural Comput.* 13, 2409 (2001). — E = predictive information; three growth regimes (M4). *[Memory]*
- Lizier JT, Prokopenko M, Zomaya AY. Local measures of information storage. *Information Sciences* 208, 39 (2012); Wibral M, Lizier JT, et al. *Front. Neuroinform.* 8:1 (2014); Spinney RE, Prokopenko M, Lizier JT. *Phys. Rev. E* 98, 012314 (2018). — local AIS is pointwise/stationarity-free; ensemble replaces stationarity; instantaneous stored *amount* has no clean pathwise def. *[row 13]*
- Roldán E, Parrondo JMR. *Phys. Rev. E* 85, 031129 (2012). — KLD as a lower bound on entropy production. *[Drive]*
- Lynden-Bell D, Wood R. The gravo-thermal catastrophe... *MNRAS* 138, 495 (1968). — negative specific heat of self-gravitating systems; the star's founding primary. *[star]*
- Martyushev LM. The maximum entropy production principle: two basic questions. *Phil. Trans. R. Soc. B* 365, 1333 (2010). — "a principle like MEPP cannot be proved." *[D→I, row 8]*
- Debye screening / conditional-independence physics (Debye–Hückel; Smith–Lee–Perkin 2016 on underscreening). *[row 5]*
- Pearl J. Markov blanket = conditional independence given the blanket. *[B2]*

**Canon-inherited, pre-verified (⊙):** Parrondo–Van den Broeck–Kawai 2009; Still et al. 2012;
Barato–Seifert 2015; Gingrich et al. 2016; Battle et al. 2016; Lynn et al. 2021; Crutchfield–Feldman
2003; Crutchfield–Ellison–Mahoney 2009; Vazza 2020; Watanabe 1960; Rosas et al. 2019; Aguilera–Di Paolo
2019 (Φ_MIP construction); Faes–Marinazzo–Stramaglia 2017; Campa–Dauxois–Ruffo 2009; Rivoire–Leibler
2011; Krakauer et al. 2020; Aktipis et al. 2015; Transtrum–Sethna sloppiness; Marquardt 1970;
Williams–Beer 2010.

**Named / abstract-level (~) and unread leads (?):** Bouchet–Reygner 2016 (~); Maes frenesy 2020 (~);
Schnakenberg 1976 (?); Maier–Stein 1993 (?); England 2015 / Perunov–Marsland–England 2016 (~, graded
FRONTIER — do not cite as law); Prigogine–Nicolis 1977 (~, existence settled, no governing law);
arXiv:2410.13375 (~, line-check before leaning on); Parrondo–Horowitz–Sagawa 2015 (~); Aguilera 2019
*Entropy* Gaussian-criticality companion (?); Oono–Paniconi 1998 (~); PRR "Information thermodynamics of
cellular ion pumps" (?, check before writing B4); Koashi–Winter 2004 (?).

---

*Prepared by four axis groups + a literature-closure pass, reconciled by Prime. No retired-framework
vocabulary used. "Own viability" appears only as a declared functional V on the viable set, ownership-
free. Every citation marked with what was actually verified; no citation is presented as verified on the
strength of its title alone.*
