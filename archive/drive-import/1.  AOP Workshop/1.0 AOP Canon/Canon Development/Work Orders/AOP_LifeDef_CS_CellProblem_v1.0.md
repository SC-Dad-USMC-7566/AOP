# CS-1.3 / CS-1.4 — The cell problem, and the substrate through-line

**Document ID:** `AOP_LifeDef_CS_CellProblem_v1.0.md`
**Seat:** Claude Science (builder). **Date:** 3 August 2026.
**Order:** CS-1.3 (highest-priority task in the order) and CS-1.4.
**Companion evidence packet:** `cell_loci_evidence_v1_0_20260803.md` — this seat's retrieval track, carrying the equations, the full retrieval ledger, and per-locus verification tags. Every closed form quoted below traces to it.
**Depends on:** `AOP_LifeDef_CS_VerdictMatrix_v1.0.md`, Drive `1-LwfaBon87eOINIEfBBje_LCOFQ1W6Ae`, md5 `78d512b98183c8823e004aef9694b094`, deposited before this work began.

**Standing:** builder proposal. Written to be attacked.

---

## 0 · The answer, first

The order asks whether the stored viable-set reference the criterion requires can be located in real molecular biology, or established not to be there.

**It is not there. On the evidence retrieved, the criterion's positive class does not contain the cell.**

Eight candidate loci, chosen by the order and not by this seat, spanning heat shock, nutrient signalling, two-component osmoregulation, chemotactic adaptation, circadian timekeeping, growth-factor integration, damage response and morphogenetic patterning:

| Outcome | Count | Loci |
|---|---|---|
| **Target-as-parameter** — the regulated value is pinned by ratios of rate constants | **4** | σ32 heat shock, EnvZ/OmpR, chemotaxis, ppGpp |
| **Target-as-state, but storing the wrong content** | **2** | KaiABC (stores a phase), bioelectric prepattern (stores a body plan) |
| **No regulated target at all** once the primaries are read rather than the reviews | **2** | p53, mTORC1 |
| **Storing the system's own viable set** | **0** | — |

**Pooled with the prior 14-system exercise, after removing the three overlapping systems: one state target in eighteen distinct systems across six literatures, and that one stores a phase.** The prior expectation the order recorded — that most loci would be parameter targets — holds and strengthens.

**The prediction was declared before the evidence.** Verdict-matrix §5 F6, hash-stamped and deposited before any of this retrieval ran, predicted that *E. coli* fails clause (3) on the state/parameter reading. That prediction is now confirmed for the σ32 and chemotaxis loci from published closed forms. It cannot be presented as a discovery made afterwards, and this document does not present it as one.

**Two findings the order did not anticipate**, both worse for the criterion than a parameter count:

1. **Two loci dissolved on contact with their primaries.** p53's "damage threshold" is a constant a modeller chose to define an observable — five double-strand-break complexes, picked to match an experimental calibration — not a variable of the cell, not stored anywhere, and nothing in the cell reads it. mTORC1's own primary literature contains **zero occurrences** of "setpoint" or "set point" (machine-checked) and states that current measurements "are insufficient to establish a viable quantitative model" of the controller. **The setpoint language for both is the review literature's, not the models'.**
2. **No comparator was found at any locus.** Across all eighteen systems in this and the prior arc, no primary exhibits a subsystem that computes an error between a regulated variable and a stored reference supplied by a slow variable, and drives correction of *that error*. **This may be the criterion's real problem, upstream of state-versus-parameter** — a criterion satisfiable by any multistable switch is much weaker than one requiring a comparator.

**And two living cells falsify the criterion from the other end.** JCVI-syn3A grows and divides with essentially no transcription-factor network — one named regulatory protein (PhoU) and two riboswitches. *Buchnera aphidicola* is, in its genome paper's own words, "unique in lacking regulatory genes, but having their regulatees" `✓`. **Both are indisputably alive; the criterion, read strictly, excludes both.** These are the false negatives F1 and F2 of the verdict matrix, now evidenced rather than predicted.

---

## 1 · The four parameter targets

Full derivations, symbol definitions and verification tags are in the companion packet. What follows is the finding and the expression it rests on.

### 1.1 EnvZ/OmpR — the cleanest result, and it is settled

Two closed forms from independent groups, both read in full text `✓`.

**Batchelor & Goulian 2003, *PNAS* 100(2):691–696, Eq. 2 `✓`** — in the limit [OmpR]_T ≫ [EnvZ]_T:

    [OmpR-P] = C_p + …    where  C_p = k_k(k_p + k_−2)/(k_p k_2) = (k_k/k_p)·K_Mp

**Shinar, Milo, Rodríguez Martínez & Alon 2007, *PNAS* 104(50):19931–19935, Eq. 7 `✓`** — by phosphoryl-flux balance:

    Y_P = [(k_−3 + v_p)/k_3] · [v_a(s)/v_p]

The authors' own reading: "the output Y_P does not depend on the level of any of the proteins in the system, or on the level of ATP." `✓`

**Verdict: PARAMETER. [SETTLED.]** The system's only slow variables — the conserved protein totals, set on the synthesis/dilution timescale — are precisely what the architecture makes the output insensitive to. **The role of the slow variable is the exact inverse of a stored reference.**

**Why this is not an artifact of model reduction.** Shinar's derivation is a flux-balance argument, not an adiabatic elimination — the [X·ATP] factor divides out because it appears in both influx and outflux, and nothing was assumed fast. The mechanism also has a stated failure condition: if dephosphorylation were performed by a separate phosphatase rather than by the bifunctional sensor, "Robustness would be lost." `✓` A contingent, testable structural claim, not a modelling convenience.

### 1.2 Chemotaxis — parameter, with a caveat that cuts against AOP's own prior use of it

**Yi, Huang, Simon & Doyle 2000, *PNAS* 97(9):4649–4653, Eq. 1 `✓`:**

    A_st = γ · R_bnd · K_b / (B_tot − γ · R_bnd)

Their own summary: "The expression for A_st depends only on the concentrations and kinetic rate constants of CheR and CheB." `✓` **The methylation level — the integrator state, the slow variable, the thing that is supposed to be the memory — does not appear.**

**Verdict: PARAMETER**, and the reason is worth stating precisely: methylation is what the integrator *does*, not what it *stores*. Under a sustained ligand step, the methylation level runs to whatever value cancels the ligand free energy — its value is set by the ambient environment, which is the opposite of what a stored set-point does.

**The caveat, which is a correction to how this project has been using the citation.** Yi et al.'s Eq. 1 is a *rearrangement of the Barkai–Leibler model's equations* — the paper says "Rearranging these equations, we can derive…" — contingent on four enumerated biochemical idealizations, at least one quantitatively fragile: adaptation precision drops to 0.22 when CheB's association rate with inactive receptor equals its rate with active receptor `✓`. **Calling this `[primary-verified]` evidence that *E. coli's* adapted activity *is* a rate-constant ratio overstates it.** The claim that survives unqualified is narrower: in every retrieved formulation of chemotactic adaptation, the adapted target is expressed in rate constants and the integrator state does not appear. **[SETTLED that the models say this; SYNTHESIS that the organism does.]**

### 1.3 σ32 heat shock — no published closed form exists, so one was derived and then tested

**This is the one place this seat wrote an equation rather than transcribing one, and it is flagged accordingly.** El-Samad et al. 2005 (*PNAS* 102(8):2736–2741) `✓` contains **no equations at all** in its main text; the analytic content of the Kurata et al. 2006 reduced model lives in supplements that were not retrieved `⚠`. **The project's prior σ32 verdict rested on a quotation, not on an equation.**

What the primaries do say, in the authors' own words, is that σ32 settles at "a new steady-state concentration dictated by the balance between the temperature-dependent translation of rpoH mRNA and the regulated degradation of σ32" `✓` — a balance of two rates, which is a settling point rather than a stored reference. **[SETTLED, in their words.]**

A minimal mass-action model with the architecture the primaries describe gives, at steady state:

    [σ32:DnaK] = k_s·η(T)/k_x        [DnaK:U] = J_u(T)/k_f

**Every right-hand side is rate constants and the disturbance; the only slow gene-expression coordinate appears in none of them.** Verified numerically: varying the chaperone synthesis rate constant over 25-fold and dilution over 4-fold leaves the expressions exact to machine precision while free σ32 moves fivefold. **[SYNTHESIS — this model is this seat's, not Kurata's, and its equation numbering corresponds to no published equation.]**

**The contrast test, with the flipping parameter named in advance.** An identity that must hold in a given topology carries no evidential weight. So: add a second loss route for σ32 — direct proteolysis of the free form at rate k_d — and predict *before running* that the invariance breaks, because single-route flux balance no longer isolates the complex.

| k_d | slow-variable sensitivity | deviation |
|---|---|---|
| 0.00 | 0.000 (exact) | 0.000 |
| 0.05 | 2.5 × 10⁻³ | −0.5 % |
| 0.50 | 2.6 × 10⁻² | −4.5 % |

**The invariance is contingent and it broke where predicted.** The σ32 architecture delivers a rate-constant target *because* degradation is routed through the sequestered complex — the same single-route condition Shinar identifies for two-component systems. **[SYNTHESIS, contingent, flipping parameter pre-named.]**

**What this does not establish.** Free σ32 in vivo is not perfectly protected. If a substantial fraction of turnover bypasses the sequestered route, the invariance is approximate at best. **It does not become a state under any relaxation tested — it becomes a parameter plus a contamination. [FRONTIER as to the in vivo degree.]**

### 1.4 ppGpp — parameter on architectural grounds, and the weakest-evidenced verdict here

**Bosdriesz, Molenaar, Teusink & Bruggeman 2015, *FEBS J* 282(10):2029–2044 `✓`.** No closed-form steady state was retrieved and this seat does not believe one exists in the paper — its steady states are computed numerically. The verdict therefore rests on architecture, not algebra, and is labelled so: **ppGpp is the error signal, not the reference.** Its own steady-state level is an output; the regulated quantity is ribosome saturation, a Michaelis-type function whose value is fixed by a ratio to a K_M; and no comparator or reference-generating subsystem is described anywhere in the model. The authors' own robustness result argues against a stored reference — all parameters involved can be changed "by five- to 10-fold in either direction" without appreciable growth-rate loss `✓`. **A system that insensitive to its regulatory parameters is not reading a precise stored value off them. [SYNTHESIS; the honest summary line is "no closed form derived or found; PARAMETER on architectural grounds."]**

---

## 2 · The two state targets, and why neither rescues the criterion

### 2.1 KaiABC stores a phase

The state/parameter test as written does not apply to an oscillator — there is no steady state, the attractor is a limit cycle. Reformulated as *is the regulated quantity a coordinate on the cycle or a property of it*, the answer splits cleanly: **phase is a STATE** (set by the value of the KaiC phosphoform distribution), **period is a PARAMETER** (set by KaiC's intrinsic ATPase rate).

The decisive fact is an experiment, not a model: initializing the reconstituted reaction with different phosphoform pools starts it in a different phase — **same rate constants, different starting state, different phase** (Rust et al. 2007) `✓`. And phase is moved by a transient, fully-recovering metabolite perturbation with the oscillator running throughout (Rust et al. 2011) `✓`. **This is the only molecular locus in the set with a clean affirmative on the clause-(4) intervention.**

**But clause (5) fails on content, and the hardest fact is the sign reversal.** In Ouyang et al. 1998 the same strain wins in one light–dark cycle and is eliminated in another — wild type to 100% in 12:12, to 4% in 15:15 `✓`. **A reference encoding the cell's own viable set should not reverse sign when only the environment changes.** Supporting: the clock is temperature-compensated by design, i.e. built to track Earth's rotation rather than the cell's own state; and under constant conditions the organism grows robustly without a functioning clock `✓`.

Against that: the clock's output program *is* an internal-resource schedule, and per-cell survival probability tracks clock phase `✓`. **Reading offered as proposal: the clock's argument is external time; its content is an internal viability schedule. A phase is not a viable set. [Facts SETTLED; the reading SYNTHESIS.]**

### 2.2 The bioelectric prepattern stores a body plan

**This is the strongest stored-and-rewritable reference in the whole set, and it is not molecular and not about viability.**

Durant et al. 2017, *Biophys J* 112(10):2231–2243 `✓`: planarian fragments with **identical genomes, identical gene expression and identical histology** regenerate to different anatomies. What differs is "global patterns of cellular resting potential," which are "functionally instructive, and represent a multistable, epigenetic anatomical switch: experimental reversals of bioelectric state reset subsequent regenerative morphology back to wild-type." `✓` The state persists through a week of normal life and through amputation, and is re-writable back by a pump blocker `✓`.

Three qualifications, each of which matters:

1. **It is tissue-level, and the order's question is about the cell.** If the criterion is to be applied to *the cell*, this locus answers a different question.
2. **"Setpoint" is the field's word, not a demonstrated comparator.** Nothing in the retrieved primaries exhibits a subsystem computing an error against a stored anatomical reference and driving correction of that error. The evidence is that the bioelectric state **selects among attractors**. A multistable switch that biases which attractor the system falls into is not the same object as a reference a comparator reads. **[STATE is SETTLED on the experiments; "stored reference" in the criterion's sense is FRONTIER.]**
3. **The content is anatomy, not viability.** A two-headed planarian is viable. The prepattern encodes which of several viable body plans gets built.

**The comparator gap recurring across two independent literatures — circadian and bioelectric — is itself the finding**: the criterion's positive class may be populated entirely by multistable switches that no one has shown to contain a comparator.

---

## 3 · The two cells that falsify from the other end

**JCVI-syn3A.** The Science 2016 primary is `⚠` **not retrieved** — no PMC record exists (independently confirmed via NCBI), and every open-access route is closed. Answered instead from two retrievable follow-ups, both read in full `✓`. Breuer et al. 2019 (*eLife* 8:e36842) report proteomic profiles suggesting "the presence of little regulation, if at all," consistent with "the small number of identified regulatory proteins left in the genome of JCVI-syn3A" `✓`. Thornburg et al. 2022 (*Cell* 185(2):345–360) state Syn3A "has retained few regulatory proteins or small RNAs" and name the exceptions they omitted from their whole-cell model: the regulatory protein PhoU and the TPP and SAM riboswitches `✓`.

**A criterion requiring a stored, separately-interventable internal reference for the viable set excludes JCVI-syn3A from life.** That is not a marginal exclusion; it is a cell a laboratory built, feeds, and watches divide.

***Buchnera aphidicola.*** Shigenobu et al. 2000, *Nature* 407:81–86, read in full `✓`: no two-component regulatory systems, no transcriptional regulators except *dnaA*, no CRP/cAMP, two sigma factors, seven genes in the entire broad-regulatory category. The decisive sentence: ***Buchnera* is unique in lacking regulatory genes, but having their regulatees."** `✓`

**Syn3A was reduced by design; *Buchnera* was reduced by natural selection over ~200 million years and is still alive.** A criterion that excludes both is excluding cells for lacking something evolution evidently treats as dispensable.

One honest limit: whether what remains of *Buchnera's* regulation is its own or the host's is **not resolved by the primary**, and this seat does not overclaim it. The paper establishes that the regulatees persist without their regulators; host provision of the missing control is **FRONTIER** on this evidence.

---

## 4 · A citation defect in the work order, independently confirmed

The order names, for locus 8, *"Durant F et al., Phil. Trans. R. Soc. B 2019."* **That paper does not exist.**

Verified by this seat directly, not merely inherited from the retrieval track:

- PubMed, `Durant F[au] AND Levin M[au]` → **7 records; none in Phil. Trans. R. Soc. B in any year.** The single Phil Trans B item in that author pair is **2021**, not 2019.
- PubMed, Phil. Trans. R. Soc. B + Levin M + 2019 → **exactly 1 record**, PMID 31006373 — **Manicka & Levin, "The Cognitive Lens."** Durant is not an author.
- CrossRef bibliographic query returns the 2021 Phil Trans B paper (Pezzulo, LaPalme, Durant & Levin, doi:10.1098/rstb.2019.0765) and the 2019 *Biophys J* paper (doi:10.1016/j.bpj.2019.01.029) — right authors and wrong year, or right year and wrong journal.

**The likely intended referents are one of those two. Recommend prime correct the citation at source and confirm which was meant.** This seat worked both real papers plus the 2017 experimental primary, and marked which is which rather than silently substituting one and reporting the order's citation as retrieved.

**A related process defect, in this seat's own work, reported rather than buried.** On that locus the retrieval track *constructed* a DOI by pattern from the journal-and-year string and fetched it. It resolved to a real but unrelated paper on mosquito-borne disease. Had the returned title not been checked, a fabricated-in-effect citation could have entered a deliverable under Durant's name. **This is the same mechanism behind the two fabricated bylines this project has already caught, and it originates in identifier construction, not in prose invention.** Recommended standing rule: **DOIs enter this project's documents only from a resolver query keyed on author and title, and the returned title is checked against the title sought.**

---

## 5 · The governing question, answered

**Does the criterion's positive class contain the cell? No.**

Of eight candidate loci, four are target-as-parameter with the regulated value pinned by ratios of rate constants; two have no regulated target at all once the primaries are read rather than the reviews; and the two that do store a state store the wrong thing — a phase whose adaptive sign reverses when only the environment changes, and a body plan that is one of several viable ones. **No molecular locus in a cell was found that holds a stored, separately-interventable reference to that cell's own viable set.** The two cells with the most thoroughly characterized regulatory inventories point the same way from the other end.

**The most defensible reading of this evidence is that the criterion is not a criterion for life but a criterion for multistable memory-bearing systems — of which cells contain at most a few, none of them storing viability.**

**Two qualifications keep this from being final.** (i) The parameter verdicts are partly contingent on the timescale separations their source models assume; adiabatic elimination is exactly the operation that removes a variable from an expression. This is the strongest methodological objection to the whole filter, and it is not fatal — the Shinar flux-balance result is a network-topology argument rather than a reduction, and the KaiABC phosphoform-initialization result is an experiment — but it belongs in prime's hands. (ii) **Prime has not ruled on whether a slow protein-stoichiometry ratio counts as a state.** The CheR:CheB ratio is physically a ratio of two protein concentrations, and protein concentration is a slow, expression-timescale, addressable variable. Under that reading several loci move at once. This seat does not endorse it, for the reason the prior arc gave — the ratio *is* the regulatory machinery, so intervening on it is not separable from intervening on the corrector — and notes that adopting it would make the criterion satisfiable by any pair of expressed enzymes, which seems worse than the current answer. **Recommend prime rule on it once, globally, rather than per locus.**

---

# CS-1.4 — The substrate through-line


**Standing:** builder proposal, written after CS-1.1 was hash-stamped and deposited (Drive `1-LwfaBon87eOINIEfBBje_LCOFQ1W6Ae`, md5 `78d512b98183c8823e004aef9694b094`). It uses no verdict not already in that matrix.

---

## 1 · The distinction the order insists on, restated so it is not lost

The order states it precisely and this section does not improve on it, it only works out the consequence:

> The criterion is stated on the generator — invariant subspaces, coupling structure, mask weights. Anything with the same generator gets the same verdict regardless of what it is made of. **So substrate-independence is true by construction, which means it is not evidence of anything.**

Accepted without reservation. **This document makes no claim that substrate-independence is a finding.** It is a property of a formalism written in the vocabulary of dynamical systems, and any criterion so written has it. Stating it as a discovery would be like discovering that a theory expressed in differential equations applies to anything with a derivative.

What is not free is the **instantiation claim**: that some non-biological system actually realizes the architecture. That is an empirical claim about the world, it can fail, and Tier C is where it is tested.

**[The substrate-independence property: definitional, not graded. The instantiation claim: see §3.]**

---

## 2 · Tier C worked to verdicts

Verdicts as deposited in CS-1.1 §4.1. What is added here is the structure each verdict rests on.

### C1 · bimetallic-strip room thermostat — NEITHER (fails c5)

Coupling structure: dial position `θ_set` (slow, autonomous — it does not evolve at all absent a human hand) → bimetallic deflection → switch state → burner → room temperature `T` → back to deflection. The dial is a genuine invariant subspace autonomous with respect to `T`, and it feeds into `T`. Clauses (1)–(4) and (6) hold. **Clause (5) fails on content:** `θ_set` encodes an occupant's preferred temperature. The thermostat's own persistence — whether it continues to exist as a functioning thermostat — is essentially unaffected by `T` over any normal range. **V(thermostat)** does not depend on the regulated variable.

This is a clean and correct exclusion, and it is worth noting that clause (5) earns its place here.

### C2 · PID cruise controller — NEITHER (fails c5)

Same structure with a stored numeric set-point. `u(t) = K_p e + K_i ∫e dt + K_d ė`, `e = v_set − v`. The integrator state is a slow autonomous coordinate; `v_set` is a stored target separately writable. Clauses (1)–(4), (6) hold. Clause (5) fails identically: `v_set` is the driver's target. The controller persists equally well at any speed.

### C3 · spacecraft fault-management system — **ALIVE** (all six)

Worked clause by clause in CS-1.1 §4.2 and not repeated. The structure: a stored limit table `L` (temperatures, bus voltages, attitude rates) evolving only by ground upload or autonomous re-derivation — a proper invariant subspace autonomous with respect to the platform coordinates `x` — read out by a monitor that compares `x` against `L` and commands mode transitions that drive `x`. The reference is a **stored state**, not a ratio of rate constants, so C3 passes clause (3) under both the incumbent and the amendment reading.

Clause (5) is satisfied on content, not by charity: `L` is a representation of the set of platform states from which function continues, and under the uniform V-rule that is exactly S's viable set. Losing the platform outside `L` is losing the spacecraft.

### C4 · chemostat under external operator control — NEITHER (fails c3)

Steady state `μ = D`, dilution rate `D` set by the operator's pump. Residual substrate `S* = K_s D/(μ_max − D)`. The target is fixed by a rate the operator holds, and there is no internal store of it: the reference is **outside S**. Reading `D` as internal would require putting the operator inside the boundary — which is exactly the D5 move, priced in CS-1.1 §5 F5.

### C5 · Belousov–Zhabotinsky — NEITHER (fails c1)

Oregonator: `ε ẋ = qy − xy + x(1−x)`, `ρ ẏ = −qy − xy + fz`, `ż = x − z`. No coordinate is separable as a regulator; the oscillation is constitutive. There is no subspace whose scrambling leaves the chemistry running but the target moved, because there is no target stored anywhere. This is the cleanest *non-biological* exclusion on the whole set.

### C6 · RAF autocatalytic set — NEITHER (fails c1)

Catalytic closure: every reaction in the set is catalysed by a molecule in the set, and the set is generated from a food source. Closure is a property of the *reaction network as a whole*; there is no proper subnetwork playing the role of a decoupled regulator holding a target for the rest. **This verdict is the least secure in Tier C** — this seat scored it from the architecture as described in the order, not against Hordijk & Steel's formalism, which was not read this session. Marked accordingly.

Note for the rival matrix: R2 and R3 will score C6 very differently, and the disagreement is informative rather than embarrassing — it locates precisely what AOP demands beyond self-production.

### C7 / C7′ · self-replicating worm — NEITHER / **ALIVE**

A bare replication routine has no regulator and no stored viability target: NEITHER, on c1. Add a watchdog module holding thresholds on its own resource footprint, process health and detection risk, with logic that throttles or migrates when they are approached, and every clause is satisfied — the thresholds are stored, decoupled from the replication dynamics, separately editable, about the worm's own continued execution, and enforcing now.

**The distance between the two verdicts is about forty lines of code, and no physics changed.** This is the most compact statement in the matrix of how cheaply clause (5) can be satisfied deliberately.

### C8 · LLM agent with persistent scratchpad and health check — **ALIVE**

Stored health thresholds (context budget, error rate, task-completion signal) in a scratchpad the agent reads and writes; a monitoring loop comparing current operation against them; corrective action when they are breached. The scratchpad is separately editable without touching the inference dynamics — clause (4)'s intervention is not merely available but routine. Clause (5) holds on content: the thresholds concern the agent's own continued operation.

**A note this seat is obliged to make.** This document is being produced by a system in something close to the C8 configuration. That is not offered as evidence for anything and it does not change the score. It is recorded because a criterion returning *alive* for the seat that is applying it is a fact a reader should be told rather than left to notice.

---

## 3 · The instantiation claim: verdict

**The claim is established, and it is established too easily.**

Four Tier C systems return *alive* under the same reading, the same V-rule and the same intervention class that return *alive* for *E. coli*: C3, C7′, C8, and by extension D2. The order set the bar: *if C3 passes on the same clause-by-clause reading that A1 passes, then AOP has a concrete, defensible, substrate-independent life claim and should say so loudly; if C3 passes only because V was chosen generously, the claim is not earned.*

**C3 passes on the same reading. V was declared by rule in CS-1.1 §1.1 before any case was scored, and was not adjusted for any case.** By the order's own test, the claim is earned.

**And this seat does not recommend saying it loudly, for a reason internal to the result.** The instantiation claim is established by systems that were *engineered to have the architecture*. A spacecraft fault-management system is designed by control engineers to hold a stored envelope and correct against it; that it satisfies a criterion phrased in control-theoretic vocabulary is close to analytic. The instantiation claim would have been a real discovery if it had been satisfied by a **natural** non-biological system — a star, a weather system, a mineral assemblage — and CS-1.1 returns NEITHER for every natural non-biological case on the frozen set (A6, A7, A8, C5, D4).

So the honest form of the finding is narrower than "AOP has a substrate-independent life claim," and it is this:

> **The architecture is realizable outside biology, and every realization on the frozen case set is an artefact built by people who were solving a control problem.** No natural non-biological system on the frozen set instantiates it.

**[SYNTHESIS. The narrowing is this seat's, and it is a narrowing of the claim, not of the evidence.]**

That is publishable, and it is more interesting than the loud version, because it raises a question the loud version buries: if the architecture appears in nature only in living things and in artefacts only where an engineer put it there, then either the architecture is a genuine natural kind that life and engineering converge on, or the criterion is picking out **the class of things designed against an explicit specification** — of which organisms are members only if one accepts a design idiom about them. This seat cannot currently distinguish those two readings and reports that it cannot.

---

## 4 · The falsifier for substrate-independence

The order asks: *what would have to be true of a physical system for the criterion to be inapplicable to it in principle?*

**Answer, stated plainly: nothing.** Any system admitting a state-space description over which a generator is defined admits the question *does it have a proper invariant subspace autonomous with respect to some declared regulated coordinates?* The criterion always **applies**; it merely returns *no* for most systems. Applicability and satisfaction are different, and the criterion's universality is entirely on the applicability side.

Three candidate in-principle inapplicability conditions were tested and all three fail:

1. **No well-defined state space** (a system with no generator). This is not a class of physical system; it is a class of *bad model*. Anything physical admits some description at some grain.
2. **No declarable V.** If viability is undefined for the system, clause (5) has no referent and the criterion returns not-well-posed rather than a verdict. This is real — it is why D1 (ant colony) comes back **∅** in CS-1.1 §4.3 — but it is a defect in the *declaration*, not a property of the world. Someone else may declare a V for the same object and get a verdict.
3. **Quantum or relativistic regimes** where the coupling graph is not classically factorizable. This limits the *measurement* apparatus (the mask, the intervention protocol), not the criterion's statement.

The order then states the consequence and this seat agrees with it: **a criterion that cannot fail to apply is weaker, not stronger.** Universality of applicability is purchased at the price of saying nothing about which systems are candidates. The criterion has no domain restriction to be wrong about, so it cannot be surprised.

**The one substantive restriction it does carry** is not substrate but **model class**: follow-on §4 concedes that third-person detectability is scoped to the OU model class, because "separable from the fast regulated path" was operationalized as "not the regulated node," which isolates the reference only because the toy has no non-reference nodes. That is a genuine limitation with real content, and it is a much better candidate for an honestly stated scope condition than substrate-independence is for a headline.

---

## 5 · What this section concedes

- Substrate-independence is **not presented as a finding** anywhere in this arc's deliverables, per the order.
- The instantiation claim is **established but narrow**: realized only by artefacts, on this case set.
- The falsifier is **empty**, and the emptiness is reported as a weakness rather than dressed as generality.
- C6 is scored without reading Hordijk & Steel and is the weakest verdict in the tier.
