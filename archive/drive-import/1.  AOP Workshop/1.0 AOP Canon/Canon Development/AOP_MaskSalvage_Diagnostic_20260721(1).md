# AOP — Semantic-Mask Salvage Diagnostic

**Prepared 21 July 2026 · builder/analyst proposal · NOT folded — for Prime verification before any canon movement.**

Startup check — 2026-07-21
[✓] AOP Charter — v1.0 (project-instructions copy; a Drive `AOP_Charter_(V6).md` also exists — governance reconciliation is open work item #1 in the handoff and does not bear on this task)
[✓] AOP Canon (the paper) — v1.20 (`AOP_CANON_MASTER_v1.20.md`, 201,962 bytes, Drive; read via the v1.19→v1.20 consolidated change set + the Phase B–D reconstruction record, both current project docs)
[✓] AOP → Ladder bridge memo — not opened; this task is semantic-layer-internal. Cross-lane consequences are **flagged, not acted on** (§7 below).
Drive connector: on.

---

## 0. The question, and the standing prerequisite it answers

Before any further investment in mask-based build, one prerequisite must be settled: **does the scramble-and-rerun semantic mask's well-defined region overlap its informative region at all, or is the mask structurally confined to trivial cases?** Concretely, compute on an analytic model class:

- **(a)** the region where the mask is **well-defined** — the per-edge scramble weight is a *resolvable* number, not so context-dependent as to be useless;
- **(b)** the region where it carries **non-trivial information** — the weights actually *discriminate* viability-relevant edges from spectators, and do so beyond what the coupling graph already hands you;
- **(c)** their intersection — non-empty and non-trivial, or empty/trivial.

A clean negative would have been valid and valuable. The finding is not a clean negative, nor a clean positive: **the intersection is non-empty and non-trivial, but bounded above by a redundancy threshold.** Details below.

## 1. What E17 did, and why it is not this question (stated explicitly, per instruction)

v1.20 Edit **E17** discharged the standing §13 item "compute the same mask on a system whose part-partition is well posed." It ran the scramble-and-rerun mask on one coupled-Gaussian two-module system and showed the per-edge weights "becoming interval-valued and unresolvable as coupling rises … while the aggregate collective-mode weight stays load-bearing and far sharper," and it graded this — correctly and in its own words — as **"a demonstration of self-consistency, not a test that could fail."**

That is a demonstration that the blur *exists* on one partition. **It is not the overlap question.** E17 did not locate where region (a) and region (b) sit relative to each other, nor whether they intersect, nor where any boundary between "resolvable" and "informative" falls. Reading E17 as having settled the salvage question would be a conflation. If the canon anywhere treats the E17 self-consistency demo as answering whether the mask is salvageable, that is a defect and should be corrected: **E17 shows the failure mode is real; this diagnostic determines that the failure mode has a boundary, and that a usable region sits below it.**

## 2. Method and provenance (charter discipline: cite before inventing)

The mask is not a new object; it is the **Kolchinsky–Wolpert semantic-information construction** [Kolchinsky & Wolpert 2018, *Interface Focus* 8:20180041 — **✓ primary read**]. They define viability as the **negentropy of the system's distribution**, and semantic information as "the syntactic information between the system and the environment that causally contributes to … maintaining the value of the viability function," operationalized by *scrambling* (intervening on) correlations and measuring the resulting viability drop. Decisively for this task, they already flag the well-definedness failure: "the optimal intervention may not be unique … the non-uniqueness of the optimal intervention, if it occurs, indicates that the system possesses multiple redundant sources of semantic information." **The per-component decomposition is well-defined when the intervention is unique, and ambiguous under redundancy.** The salvage question is therefore, in existing terms, *how much redundancy the per-edge decomposition tolerates before it degenerates* — not a new question, a quantitative one.

Three further existing results supply the rest of the spine, so nothing load-bearing is invented:

- **Per-edge attribution of a jointly-determined viability is a cooperative-game attribution problem.** A single edge's scramble weight is its *marginal contribution*, and marginal contributions vary across the coalition (context) of what else is scrambled — so the honest per-edge object is an **interval** (the span of marginal contributions), whose average is the Shapley value; the *values* sum to the whole (efficiency axiom) but the *raw marginals* do not [Shapley 1953; interaction-index framing, Grabisch & Roubens 1999 — **~ named/result-level**; the coalition-dependence and averaging confirmed against a primary description]. This is exactly E17's "interval-valued weights," named to its known source.
- **Resolvability of the per-edge weights is a sloppy-spectrum question.** The parameter Fisher information `F_ee' = ½ tr(Σ Bₑ Σ Bₑ')` has a stiff/sloppy spectrum; per-edge identifiability degrades as `1/√λ_min`, and the collinearity blur is `VIF_e = (F⁻¹)_ee·F_ee = 1/(1−R²_e)` [Transtrum et al. 2015; Marquardt 1970 — **⊙ canon-inherited**]. These are E17's two named blur mechanisms (inferential variance-inflation and interventional edge-drag).
- **Redundancy has a computable sign.** The O-information Ω>0 marks redundancy-domination [Rosas et al. 2019 — **⊙ canon-inherited**, recomputed here]. This is the same Ω that E16 found the star to carry, so the salvage boundary and the star's integration sign are the *same* quantity read two ways.

**Model class (closed-form, per charter — no sampling, no estimator).** Static Gaussian on a coupling graph: precision `J(θ) = I + Σₑ θₑ Bₑ`, `Bₑ` = edge Laplacian, covariance `Σ = J⁻¹`. Declared viability `V = −½ log det Σ[S,S]` (Kolchinsky–Wolpert negentropy restricted to the declared observable set `S` — the observable slot of the AOP declaration tuple D; `S` = all nodes recovers their whole-system case). Scrambling edge e = knocking out that channel (`θₑ→0`) and recomputing Σ. Everything is a closed-form function of Σ. Runnable script: `mask_salvage.py` (deposited alongside).

## 3. The three tests and what each isolates

| Model | Construction | What it isolates |
|---|---|---|
| **1 — concentrated viability** | Path 0–1–2–3–4, `S={0}`; one edge holds the lone target | The *degenerate easy* case: viability rests on one identifiable edge, spectator is topologically far, redundancy low |
| **2 — collective viability** | Two 3-node modules, `S`=module 1 held by 3 substitutable intra-edges; weak bridge | The case E17 worries about: a collective mode, but the spectator sits in another module (*syntactically distant*) |
| **3 — semantic-beyond-syntactic** | Complete graph K4, **all edges equal strength**, `S={0,1}` | The **decisive** test: discrimination can come *only* from the declared viability set, never from coupling strength — the mask must read semantics, not syntax |

Model 3 is the one that matters. Models 1–2 let the coupling graph itself carry the load/spectator distinction (the spectator is far in `L`), so a "positive" there is cheap — the mask would be merely re-reporting the syntactic layer. Model 3 removes that crutch: every edge is syntactically identical, so any discrimination the mask achieves is genuine semantic content beyond `L`.

## 4. Results

**Well-definedness** is measured as the width of each edge's marginal-contribution interval (relative to the aggregate weight). **Informativeness** is measured as whether the load-bearing edge's interval lies *disjointly above* the spectator's — a single scale-free condition that requires the weights to be simultaneously narrow enough (resolvable) and separated (discriminating). Disjointness (`lo_load > hi_spec`) is **tolerance-free** — it is raw interval overlap, no threshold chosen.

**Model 1 (concentrated):** salvageable at *every* coupling tested (g = 0.05 → 5.0). The spectator weight stays ~0 and the load interval sits far above it. *But this is the case with essentially no attribution problem — one edge does all the work. It does not generalize, and is reported only as the trivial baseline.*

**Model 2 (collective, distant spectator):** salvageable at every coupling tested (a = 0.1 → 8.0), including where Ω climbs past 1.0. The load (intra-module) interval never merges with the spectator (other-module) interval, because a weak bridge pins the spectator near 0. **This is real but still partly cheap** — the spectator is syntactically distant.

**Model 3 (semantic-beyond-syntactic — decisive):**

| a (uniform strength) | Ω | load interval [lo, hi] | spec interval [lo, hi] | disjoint? |
|---|---|---|---|---|
| 0.3 | 0.03 | [0.159, 0.235] | [0.000, 0.009] | **yes** |
| 1.0 | 0.22 | [0.255, 0.549] | [0.000, 0.077] | **yes** |
| 2.0 | 0.50 | [0.294, 0.805] | [0.000, 0.188] | **yes** |
| 3.0 | 0.73 | [0.310, 0.973] | [0.000, 0.286] | **yes** |
| **3.4 = a\*** | **0.81** | lo = 0.313 | hi = 0.321 | **merge** |
| 5.0 | 1.08 | [0.323, 1.199] | [0.000, 0.442] | no |
| 8.0 | 1.45 | [0.332, 1.417] | [0.000, 0.613] | no |

The per-edge mask **resolvably discriminates a semantically load-bearing edge from a semantic spectator across weak-to-moderate coupling, well into the redundancy-dominated regime (Ω up to ~0.8)** — and then the two intervals **merge at a\* ≈ 3.4, Ω ≈ 0.81**. Beyond a\*, the spectator's *upper* marginal (its weight when all support edges are scrambled, so it becomes the last path holding the collective) rises to meet the load edge's *lower* marginal (its weight when all support edges are present, so it is dispensable). Only the **aggregate-mode weight stays sharp** past a\* (confirming E17's aggregate claim — but now as the *boundary* of the per-edge mask's usefulness, not a free-standing property).

**The verdict depends on the resolution standard, and this must be stated honestly.** Under the **interval** standard (E17's own "interval-valued weights"), the mask degenerates at a\*. Under a **Shapley-mean** standard, the mean separation persists to arbitrarily strong coupling (load 1.03 vs spec 0.13 even at a = 15, Ω = 2.0) — but that mean averages over an interval as wide as the weight itself. **It hides the context-sensitivity; it does not remove it.** The honest per-edge object is the interval, and the interval merges.

## 5. Verdict (graded)

**The intersection (a)∩(b) is NON-EMPTY and NON-TRIVIAL, but BOUNDED ABOVE by a redundancy threshold.** [**SYNTHESIS, analytic-model-result**, on the static-Gaussian class.]

- **Non-empty and non-trivial** — this refutes the strongest negative hypothesis ("the mask is well-defined only where it is uninformative"). The mask resolvably reads *semantic* structure the coupling graph does not hand it (Model 3, equal-strength edges) across a genuinely coupled, redundancy-dominated band (Ω up to ~0.8). It is *not* confined to the decoupled/trivial corner. [**SETTLED within the class**: the interval-disjointness below a\* is a tolerance-free closed-form fact.]
- **Bounded** — beyond a redundancy threshold (a\* ≈ 3.4, Ω ≈ 0.81 in the K4 test) the per-edge intervals merge and only the aggregate mode survives. This boundary *is* the phenomenon Kolchinsky–Wolpert flagged (non-unique optimal intervention under redundancy) and Rosas quantifies (Ω). [**SETTLED** that a boundary exists; the boundary *value* is model-specific — see caveats.]
- **The boundary is not a defect; it is the semantic layer agreeing with the framework's refusal to individuate.** [**SYNTHESIS/FRONTIER.**] At maximal integration (all edges equal, coupling → ∞) the declared target is held equally by every edge through the consensus mode, and "which edge holds it" genuinely has no resolvable per-edge answer. The mask correctly returns *overlapping intervals* rather than a false crisp number. A per-edge semantic attribution that dissolves exactly as the system becomes one indivisible integrated whole is the mask behaving as an ownership-free framework should.

**Bottom line for the build decision.** The mask is salvageable *as a per-edge object* in a computable, non-trivial region — mask-based build is not chasing an empty set. But its resolvable region has a ceiling at strong integration, and the framework's flagship integrated systems (the star, a tight module, a candidate "higher individual") can sit on **either side** of that ceiling depending on coupling. **Per-edge mask resolvability is therefore not guaranteed for the central integrated cases and must be checked case-by-case** (the check is cheap and closed-form — the Ω sign plus the interval-disjointness test in the deposited script). Where a target system is past its a\*, the honest deliverable is the aggregate-mode weight (a scalar), not a per-edge mask.

## 6. Honest residuals and scope limits

- **Threshold value is model-specific.** a\* ≈ 3.4 / Ω\* ≈ 0.81 are for K4, `S={0,1}`. The *structure* (a redundancy-bounded salvage region; tolerance-free interval merge) reproduces across all three models, but the numeric ceiling will move with graph, declared `S`, and coupling pattern. No universal Ω\* is claimed.
- **Static-Gaussian only.** Same class as the canon's Phase C/D results; consistent with the framework's other computed claims, and inheriting the same "does not by itself extend to non-Gaussian / non-stationary" caveat.
- **Interval = full min–max Shapley-marginal span.** This is the strict reading (every coalition, including adversarial ones). It is the right reading for "is the weight resolvable," and it is E17's stated framing, but a reader who accepts the Shapley mean as "the" weight will read the mask as informative everywhere — §4 states both and argues the interval is the honest object.
- **Not a falsifiable test.** Like E17 and Figure MW, this is a closed-form determination on a declared model class, not an experiment that could surprise us against nature. Graded accordingly.
- **Citation markers.** Kolchinsky–Wolpert 2018 **✓** (primary read, the load-bearing one). Rosas 2019, Transtrum 2015, Marquardt 1970 **⊙** canon-inherited (Ω recomputed here). Shapley 1953 / Grabisch–Roubens 1999 **~** named/result-level — the coalition-dependence-of-marginals and Shapley-averaging were confirmed against a primary description, but the interaction-index papers were not line-checked; nothing in the verdict rests on the interaction index specifically, only on the elementary non-additivity of marginal contributions.

## 7. Cross-lane consequences — FLAGGED for Prime, not acted on

This diagnostic stays in the semantic (mask / viability read-out) lane. It does **not** touch Φ_MIP, the moving-MIP, or the star reconciliation. But it surfaces two connections Prime should weigh:

1. **The mask's resolvability ceiling is the O-information sign (E16) read in the semantic lane.** The per-edge mask degenerates exactly as Ω grows — i.e., the *more integrated/redundant* a collective (higher Ω, and plausibly higher Φ), the *less* the per-edge semantic mask resolves. This ties the semantic layer's resolvability directly to the integration layer's redundancy measure. Whether it also ties to Φ_MIP is an integration-lane question — **flagged, not pursued.**
2. **"Per-edge attribution genuinely vanishes at maximal integration" is a semantic-layer statement of the refusal to individuate,** and it bears on the §9 higher-individual and §9a collective-alive routes (a maximally integrated collective has no resolvable per-edge viability attribution — only an aggregate one). This is adjacent to the F2 seam the handoff lists as the principal open problem. **Flagged for Prime; not acted on.**

If any of this warrants a canon movement or a Ladder propagation-bus note, that is Prime's call after verification.

## 8. Deposited artifacts

- `AOP_MaskSalvage_Diagnostic_20260721.md` (this file)
- `mask_salvage.py` — self-contained, closed-form, reproduces every number above (three models, the a\* threshold sweep, the Fisher/VIF spectrum, and the Ω recomputation). No sampling; runs in seconds on numpy+scipy.

---

### References cited in this diagnostic
- Kolchinsky, A. & Wolpert, D. H. (2018). Semantic information, autonomous agency and non-equilibrium statistical physics. *Interface Focus* 8: 20180041. **[✓ primary read]**
- Shapley, L. S. (1953). A value for n-person games. *Contributions to the Theory of Games II*. **[~ named/result-level]**
- Grabisch, M. & Roubens, M. (1999). An axiomatic approach to the concept of interaction among players in cooperative games. *Int. J. Game Theory* 28. **[~ named/result-level]**
- Transtrum, M. K. et al. (2015). Perspective: Sloppiness and emergent theories in physics, biology, and beyond. *J. Chem. Phys.* 143: 010901. **[⊙ canon-inherited]**
- Marquardt, D. W. (1970). Generalized inverses, ridge regression, biased linear estimation, and nonlinear estimation (VIF). *Technometrics* 12. **[⊙ canon-inherited]**
- Rosas, F. E. et al. (2019). Quantifying high-order interdependencies via multivariate extensions of the mutual information (O-information). *Phys. Rev. E* 100: 032305. **[⊙ canon-inherited, recomputed here]**

— End of diagnostic. Proposal only; awaiting Prime verification before any fold. —
