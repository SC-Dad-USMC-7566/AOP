# Gate 1 — System selection for the life-criterion arc: SELECTION REPORT

**Document ID:** `AOP_LifeCriterion_SystemSelection_Report_v1_0_20260803.md`
**Seat:** Claude Science (builder). **Date:** 3 August 2026.
**Order:** `TASK_CS_AOP_LifeCriterion_SystemSelection_20260801.md` (Drive `1pqmKxzablE53V4IXpW8inq-1EgT8rXfH`)
**Parent freeze:** `AOP_LifeCriterion_DispositionRule_FROZEN_v1_0_20260801.md` — Drive `1-HkXf58z-UWnYVkT1mcNR3_y2hIi3PAy`,
md5 `b7eebcfd5a371a78b33a5fe230d52554`. **Verified this session** by independent download and hashing
(6,824 bytes; computed md5 matches the order's).
**Ben's ruling in force:** §0 option (a). Sporulation reserved to H4/RED-25.
**Supersedes:** the v0_1/v0_2 interim report deposited 2 August, written while three retrieval tracks
were parked on publisher-access approvals. All five tracks have now reported. **51 primaries read;
30 blocked retrievals logged.**

**A pair is delivered (§6), with its weaknesses stated rather than smoothed.**

**This seat does not select, does not pair by fiat, and does not grade its own output.** The pair
below is a builder's recommendation with the operative trade-offs priced. Prime verifies by re-running
retrievals or by independent reconstruction.

---

## 0 · Summary for a reader with five minutes

1. **Positive article: the cyanobacterial KaiABC circadian clock** (*Synechococcus elongatus*
   PCC 7942). The only candidate of fourteen whose target is a **state** rather than a kinetic
   parameter, and the only one with a strong lifetime readout. S.1 PASS, S.2 PASS, S.3 PASS,
   S.4 **PARTIAL (~10×, one order short of the order's ≥2)**, S.5 STRONG.
2. **Negative control: EnvZ/OmpR** (*E. coli*), with σ32 heat-shock as the alternative that trades
   match quality for a survival readout. Model-free is **evidenced from two independent closed
   forms**, not asserted.
3. **The striking empirical pattern: thirteen of fourteen candidates are target-as-parameter.**
   Four independent literatures — chemotaxis, heat shock, two-component signalling, synthetic
   integral control — put the regulated target in a ratio of rate constants. Only the clock stores it
   as a state. **If the criterion is picking out something real, it is picking out something rare.**
4. **Three findings that outrun the selection task and need prime's attention:** AOP's central
   distinction is prior art under four names (§4.1); Sontag's internal-model theorem cuts against the
   strict reading of AOP's own criterion (§4.2); and **P1 faces a live kill-condition threat from two
   different directions** (§3.3.1, §4.3).
5. **The honest cost of the pair: S.4 cannot be satisfied by any candidate found.** For the clock the
   two most benign actuators are *architecturally barred* from tuning the slow timescale. Under the
   freeze this points at P2 returning UNINFORMATIVE by construction, which prime must price before
   the pre-registration freezes (§6.3).

---


## 1 · Grading and retrieval convention

Per the benchmark records file (`AOP_Benchmark_RejectedCandidates_v0.1.md`), retrieval status is
tagged separately from scientific grade: `[primary-verified]`, `[primary-abstract-only]`,
`[secondary]`, `[not-retrieved]`. No claim below is tagged `[primary-verified]` unless the passage
relied on was read. Where a track's finding was additionally re-checked by this seat against the
primary, it is marked **[parent-reverified]**.

**A.1.9 is not applied anywhere in this report.** It is a benchmark heuristic about redundant
architecture, graded frontier on five observations, and this arc does not require redundancy.

**No benchmark rejection has been treated as grounds for rejection here.**

---

## 2 · The eligibility question, and why it governs every score below

Full statement: `elig_memo.md` (deposited alongside this report). Summary:

The follow-on (`AOP_LifeArchitecture_Followon_v0.1.md` §4) defines the discriminator as *"a proper
invariant subspace whose dynamics are autonomous with respect to the regulated coordinates — a
subspace the dynamics preserve, evolving under its own law without being driven by the variables it
regulates."* Read strictly, *without being driven by the variables it regulates* excludes **integral
feedback**, where the slow variable is by construction driven by the regulation error.

But the follow-on's own §3 names Bich et al. as supplying the decoupling component, and what Bich
supplies is operation *"at a different dynamical scale"* — a weaker condition that integral feedback
satisfies. **The two supports are not co-extensive and the follow-on does not say which governs.**

- **Reading A (strict/autonomy):** ẋ = f(x), no dependence on regulated coordinates y.
- **Reading B (loose/scale separation):** timescale separation + load-bearing x→y + separate
  addressability; feedback y→x permitted.

**A second, independent filter — the sharper one.** "Stores a target" needs a referent. In integral
feedback the integrator's *value* is a state but is not the target; the target y\* is a **zero of the
integrator's rate law**, i.e. a kinetic parameter. A candidate can therefore satisfy "has a slow
separable variable" and still fail "stores a target." **This filter, not the autonomy question,
turned out to decide every candidate scored so far.**

Every candidate below is scored under both readings and against both filters.

---

## 3 · Candidates scored

### 3.1 *E. coli* chemotactic adaptation via receptor methylation — **REJECTED as positive article (S.2)**

*Prime's lead candidate. Contamination: clean.*

| Criterion | Verdict | Basis |
|---|---|---|
| S.1 | **PASS** | Two closed-form dynamical models with measured transfer functions; large intervention class. `[primary-verified]` |
| **S.2** | **FAIL** | **The operative rejection.** See below. `[primary-verified]` **[parent-reverified]** |
| S.3 | PASS | Reducing CheB expression moves the adapted kinase-activity set-point with machinery intact and exact adaptation preserved. `[primary-verified]` |
| S.4 | PARTIAL | Baseline separation ~1–2 decades (τ_slow ~10–200 s vs τ_fast ~0.05–0.5 s); no documented ≥2-decade *sweep* under experimental control. `[primary-verified]` for the baseline figures |
| S.5 | **WEAK** | No declared viable set, no survival/hazard observable, no architecture-matched comparison class. `[primary-verified]` |

**Reading A: NO** — structurally excluded. The model is dm/dt = F(a) with *a* the regulated variable;
Yi et al. identify the fed-back quantity as the system's error. This is the canonical integral-feedback
case Reading A was written to exclude. **Reading B: YES** — all three clauses met and quantified.

**Target: PARAMETER. This is the rejection, and it is provable from the published equations rather
than estimated.** Yi et al. (2000) Eq. 1 gives the adapted activity in closed form:

> A_st = γ·R_bnd·K_b / (B_tot − γ·R_bnd),  where γ = k_r/k_b

and the paper states the expression "depends only on the concentrations and kinetic rate constants of
CheR and CheB." **The methylation level — the slow variable — is absent from the expression.** Under
CheR saturation it reduces to K_b·Vmax_R/(Vmax_B − Vmax_R). The slow variable is what the integrator
*does*, not what it *stores*; the target is a ratio of rate constants.

**[parent-reverified]** — this seat independently retrieved Yi et al. 2000 (PNAS 97:4649, PMC18287,
green OA) and read Eq. 1 and the sentence following it in the PDF. The finding does not rest on the
track's report. Per the charter's preference for analytic over estimated results, it rests on no fit.

**Two corrections to the order's §4.1 recollection, both material:**

1. **Prime's S.3 concern is a conflation, and correcting it does not save the candidate.** What the
   Alon et al. robustness result holds invariant is the **precision** of adaptation, not the adapted
   **level**; the abstract separates them explicitly, stating that steady-state behaviour does vary
   with protein concentration. So S.3 passes. The candidate then fails one step *earlier*, on S.2,
   from a cause the order did not flag as the risk.
2. **An experimental datum converts the equation-reading into a measured result.** Shimizu et al.'s
   22 °C vs 32 °C comparison moved the adapted set-point from ~1/3 to ~1/2 **with protein expression
   demonstrably unchanged**, attributed by the authors to the catalytic rate constants. A
   stored-state target cannot behave that way. `[primary-verified]`

**Recommended role: not the positive article.** Its genuine value is as a **near-miss that
discriminates Reading A from Reading B** — a system with a large, separable, intervenable slow module
and no stored target. Note this is a *third* category: it is not model-free in the ordinary sense
(it corrects via an internal dynamical variable, which a star does not), so it does not cleanly fill
the negative-control slot either. **The pairing scheme currently has no slot for it, and that is
itself a finding.**

*One live route back, recorded for prime's judgement and not recommended by this seat:* if Gate 1
rules that CheR:CheB stoichiometry is the slow stored state, S.2 flips to PASS and a published
CheB-expression experiment becomes an already-in-print competent-misregulation demonstration. This
seat judges the stoichiometry to *be* the machinery, but the empirical facts are the same either way.

---

### 3.2 *E. coli* heat-shock response (σ32) — **REASSIGNED: negative control, not positive article**

*Prime's candidate #2. Contamination: clean.*

| Criterion | Verdict | Basis |
|---|---|---|
| S.1 | PASS | Explicit mechanistic ODE model with named equation table; control-theoretic analysis with open/closed-loop decomposition. `[primary-verified]` |
| **S.2** | **FAIL** | No slow variable stores a target. σ32 is the *fastest* component (half-life ~1 min at 30 °C, ~20 s at 42 °C) and its level is the **output** of a rate balance, not a reference for it. `[primary-verified]` |
| **S.3** | **FAIL** | Every operation that moves where the system settles alters synthesis rate, FtsH-mediated degradation, chaperone affinity or abundance — each a component of the corrector. Retrieved perturbations **degrade rather than redirect**. `[primary-verified]` / `[primary-abstract-only]` for the null phenotypes |
| S.4 | PARTIAL | ~3 orders of magnitude, measured — but *between corrector components*, not between a stored reference and a regulated variable. Does not rescue S.2. `[primary-verified]` |
| **S.5** | **STRONG** | **The strongest S.5 in the candidate set.** Survival and growth at elevated temperature — a genuine first-passage-style observable — with published, architecture-differentiated comparison classes (WT vs *rpoH*-null vs *dnaK* deletion vs feedforward-disabled vs constitutive-degradation variants). `[primary-verified]` |

**Reading A: NO. Reading B: NO** — fails on the separate-addressability clause, not the feedback clause.

**Target: PARAMETER**, on the modelling authors' own words. El-Samad et al. describe their feedforward
mutant's altered steady state as "a new setpoint dictated by the balance between" σ32's lower synthesis
rate at high temperature and its degradation rate. **A setpoint dictated by the balance of two rate
constants is a zero of a rate law, not a state.** `[primary-verified]`

**Prime's read is confirmed on both counts** — best S.5 of the four, and it does fail S.2. The
reassignment follows: a system that corrects competently, has no separable target, and carries a real
survival observable is precisely what the matched negative control requires.

---

### 3.3 EnvZ/OmpR bifunctional two-component system — **RECOMMENDED NEGATIVE CONTROL**

*Contamination: clean. 10 primaries read.*

Both halves of the negative control's specification must be evidenced. One is, firmly; the other is
qualified, and the qualification changes what the pre-registration must declare.

**Model-free: EVIDENCED, from two independently derived closed forms.** `[primary-verified]`
**[parent-reverified]** — this seat independently retrieved Batchelor & Goulian 2003 (PNAS 100:691, via
Europe PMC) and read the model section. Their Eq. 2 gives the output as C_p + …, with
C_p = (k_k/k_p)·K_Mp; Shinar et al.'s Eq. 7 states the output "does not depend on the level of any of
the proteins in the system, or on the level of ATP." The structural account is absolute concentration
robustness, and bifunctionality is the structural reason. **The target is a rate-constant expression;
there is no state whose value the fast dynamics track.** Even the physiological signal acts
parametrically, through a rate constant.

**Reading A: NO — and note it fails at the *first* clause, not the integral-feedback clause: there is
no slow coordinate x at all to be closed.** **Reading B: NO** — the available slow variables
([EnvZ]_T, [OmpR]_T) do have timescale separation and separate addressability, but their coupling onto
the output is *structurally nullified*, which is exactly what absolute concentration robustness means.
**A coupling engineered to have no effect on the operating point is the opposite of load-bearing.**
**Both readings agree**, so the negative control's exclusion is not reading-dependent — a real
strength for the pair.

**"Corrects" is qualified, and a further result sharpens why.** `[primary-verified]` The retrieved
primary is a steady-state analysis: it establishes robustness *across* steady states, not dynamic
restoration after a kick. Worse, Batchelor, Silhavy & Goulian 2004 tested for feedback from porin
output back into the circuit and **found none**, describing porin osmoregulation as under open-loop
control. **Consequence the pre-registration must absorb: the correcting variable has to be OmpR-P
against an osmotic signal, not porin level against a need.** For a negative control this is in one
sense ideal — model-free *and* the regulated output is not sensed — but it means "demonstrably
corrects" must be declared on the OmpR-P variable, and the dynamic-restoration experiment on OmpR-P
appears never to have been run.

**Match quality with the KaiABC positive article: moderate.** Same intervention class in kind
(chromosomal point mutation, titratable expression, trans-acting modulator dosage) and same readout
technology (chromosomal two-colour fluorescent transcriptional fusions), and architecturally it is the
bifunctional limb of the contrast the robustness literature itself names as decisive — a structurally
motivated comparator rather than a convenient one. **But it is a different organism from the positive
article, and it has no lifetime readout** (`[not-retrieved]`: no osmotic-survival or fitness assay for
*envZ*/*ompR* mutants was found; recorded as a gap, not a negative result). §6.2 prices the
alternative.

#### 3.3.1 ⚠ A live threat to P1, from the negative control's own literature

**This bears on whether the system can serve as the negative control at all, and it now has two
independent instances — one engineered, one native.**

P1's second kill condition: **a system the criterion excludes turns out to have competent
misregulation.** EnvZ/OmpR is excluded by the criterion. Two published results show its output
set-point moved while regulation continues:

**(a) Engineered.** `[primary-verified]` **[parent-reverified]** — Jones RD, Qian Y, Ilia K, Wang B,
et al., "Robust and tunable signal processing in mammalian cells via engineered covalent modification
cycles," *Nat Commun* 13:1720 (2022), DOI 10.1038/s41467-022-29338-w, read in full by this seat.
Output "increases gradually as the ratio of kinase-to-phosphatase increases," and is additionally
tuned by modulating **phosphatase stability** with a small molecule (trimethoprim on a degradation
domain), machinery otherwise untouched. *(Author attribution corrected on review: an earlier draft of
this report named a first author that no retrieval had returned. The correction is recorded rather
than silently made, because inventing an attribution is the same class of defect this report was
written to avoid.)*

**(b) Native, and cleaner because it is non-mutational.** `[primary-verified]` — **MzrA dosage**: a
trans-acting membrane protein whose overexpression or deletion biases EnvZ toward OmpR-P accumulation,
dose-tunable, with the authors themselves certifying that signal reception survives — porin expression
still responds to medium osmolarity in cells lacking or overexpressing MzrA. Also *envZ* chromosomal
point mutations that reset the kinase/phosphatase balance.

**Why this threatens P1.** A model-free corrector is supposed to be only *degradable*, with no
separable target to move. Here the operating point is moved — reversibly and by a trans-acting dosage
knob in the native system — and regulation continues.

**The counter-argument, stated fairly.** Both operations retune kinase/phosphatase balance, i.e. change
a kinetic parameter *of the corrector*. The pleiotropic *envZ* R397L allele that shifts output also
loses roughly ten-fold of phosphatase turnover. Under that reading these are competent
*re-parameterisations*, not set-point moves.

**This seat does not adjudicate it, but records the bind precisely, because it is the sharpest thing
Gate 1 has surfaced.** The same argument that makes EnvZ/OmpR model-free — its target is a
rate-constant ratio — is the argument that makes its tunability not-a-set-point-move. **Applied
consistently, that argument is also what rejected chemotaxis and the antithetic controller at S.2.**
The honest statement, in the two-component track's own words: these are target shifts achieved by
retuning the machinery, which is exactly what target-as-parameter predicts should be indistinguishable
from a machinery change — **and P1's current phrasing does not settle whether that counts.** Prime
needs a principled line before the pre-registration freezes; OAI will aim here. Note also that the
decisive experiment — a robustness titration in a set-point-shifted background — appears never to have
been run, so every P1 conclusion here is bounded by that absence.

---

### 3.4 Hypothalamic thermoregulation / fever — **REJECTED (S.1, S.4), and for a further reason**

*Prime's candidate #3. Contamination: clean.*

Prime is right that this is conceptually the cleanest instance of P1 in biology, and right to expect
it to fail S.1 and S.4. Confirmed: no published quantitative dynamical model with a declared slow
variable was retrieved, and no tunable slow/fast ratio exists. S.3 is genuinely strong (intra-POA PGE2
reversibly moves the operating point with machinery intact) `[primary-abstract-only]`.

**The further reason is the important one.** The field has an **active, unresolved dispute over
whether the object PGE2 shifts is a stored reference at all.** Leading reviews argue thermoregulation
is a federation of independent effector loops with no unified set point, and use "balance point" for
what is being shifted. **Selecting this system would make AOP's central distinction hostage to a live
physiology controversy.** Retain as a motivating illustration in the canon; do not use as a test article.

---

### 3.5 Cyanobacterial KaiABC circadian clock — **RECOMMENDED POSITIVE ARTICLE**

*Contamination: clean. 15 primaries read as PMC full text.*

| Criterion | Verdict | Basis |
|---|---|---|
| S.1 | **PASS** | Data-constrained dynamical models at two levels, resolving four KaiC phosphoforms with fitted kinetics; large intervention class. `[primary-verified]` |
| **S.2** | **PASS** | **The only PASS on S.2 in the entire candidate set.** Slow variable = phase of the KaiC phosphorylation cycle (distribution over S431/T432 phosphoforms). Slow rate is KaiC's intrinsic ATPase (~15 ATP/KaiC/day) — an enzymatic rate, not a fixed point of a fast drift. `[primary-verified]` |
| S.3 | **PASS** | Three independent phase-moving operations, oscillator demonstrably still running: a 5 h dark pulse giving a stable 10 h phase advance; a transient ADP step (ATP fraction to ~50%, recovering within an hour) with a graded dose-response; initialising the reconstituted reaction from a T-KaiC- vs S-KaiC-enriched pool. `[primary-verified]` |
| **S.4** | **PARTIAL** | **~10× (one order of magnitude), one order short of the order's requirement.** Period 15 h→158 h across single substitutions at KaiC residue 402. See §6.3 — this is the pair's principal defect. `[primary-verified]`; `[primary-abstract-only]` for the classic 16–60 h in vivo range |
| **S.5** | **STRONG** | Competitive exclusion in mixed culture within ~5.4–6.8 turbidostat generations; wild type 52%→100% in LD 12:12 and 52%→4% in LD 15:15. Three matched comparison classes including a genetic-rescue control. `[primary-verified]` |

**Target: STATE.** Phase is set by the *value* of the phosphoform variables with all rate constants
unchanged, is moved by a transient reversible metabolite perturbation with no parameter edited, and is
read out by downstream regulation (SasA kinase / CikA phosphatase activated at distinct clock times,
converting phase into an RpaA~P level that selects the dawn or dusk expression program). `[primary-verified]`

**Reading B: YES**, all three clauses verified. **Reading A: UNCLEAR — and the reason is the most
important structural finding about this candidate.**

The autonomy evidence that put the clock on the longlist is real: the oscillator runs reconstituted
from three purified proteins and ATP, requiring neither transcription nor translation, and KaiC's
period-setting ATPase is temperature-compensated even without KaiA and KaiB. **But that autonomy
obtains only in the reconstituted preparation, which has no regulated coordinates, no viable set, and
no lifetime.** In the living cell three feedback paths from the regulated coordinates onto the slow
variable are documented: the kaiBC promoter is itself under circadian control; the output regulator
RpaA feeds back on core-oscillator gene expression, with *rpaA* deletion causing oscillator failure;
and metabolic state (ATP/ADP) entrains the oscillator. `[primary-verified]`

**Strict Reading A and S.5 are not available in the same preparation.** That is a structural property
of the candidate, not a gap in the literature, and it means the strict reading buys its cleanliness by
discarding every viability observable. **Prime should treat this as the strongest practical argument
for Reading B** — under Reading A the criterion may be satisfiable only by preparations that cannot
exhibit persistence.

**A P1-shaped phenotype is already in print.** A clock running at the wrong phase relative to the
environment produces competent, precisely-timed, misdirected regulation that kills cells: the same
strain wins in LD 12:12 and is eliminated in LD 15:15, and clock-phase-dependent irreversible growth
arrest is documented. `[primary-verified]` This is what P1 predicts, observed before P1 was written.

**The live objection, which is a criterion-interpretation question and not an empirical one.** The
clock's *argument* is external time, but its *content* is an internal viability schedule (RpaA-dependent
dusk carbon-catabolism genes whose deletion impairs viability in light–dark but not constant light;
clock-phase-dependent starvation tolerance). Whether that satisfies component (5) — the reference
storing the system's *own viable set* rather than a model of the environment — is for prime.
**Canon v1.26 bears on this and should be read before ruling:** it restates semantic claims as relative
to *a declared persistence criterion* rather than to "the system's own viability," and its title block
states that "own" denotes the set the functional is evaluated on, not a viability the system supplies.
On that reading the objection is substantially softened, because the viable set is declared in **D**
rather than possessed by the system.

---

### 3.6 Synthetic antithetic integral feedback controller — **REJECTED as positive article (S.2)**

*Contamination: clean. 8 primaries read.*

Prime nominated engineered controllers for the negative-control slot; this seat scored the *integral*
controller as a positive-article candidate, and it fails.

**Target: PARAMETER — verified from the models' own equations in two independent primaries.** The
integrator *state* is dZ = Z₁ − Z₂, which accumulates the tracking error; the *target* is μ/θ, a ratio
of two kinetic rate constants and the zero of that state's rate law. `[primary-verified]`

**S.3 PARTIAL:** an experimentally demonstrated 32-fold set-point sweep by plasmid ratio with
adaptation preserved at each set-point — the "turn a dial and the controller keeps working" operation
the brief hoped for. But what the dial moves is a ratio of production rates. **S.4 PARTIAL and against
expectation:** no ≥2-decade slow/fast sweep is evidenced anywhere, and the declared separation in this
literature runs the *opposite* way (fast sequestration relative to plant). **S.5 WEAK:** every
regulated variable retrieved is a reporter or orthogonal protein, so the reference is for an arbitrary
target, not the system's own viable set — component (5) fails.

**A structurally useful result for the gate: this candidate is insensitive to the Reading A/B
ambiguity.** Reading A excludes it as integral feedback; Reading B would admit it on coupling and
addressability; **but the target-as-parameter filter cuts it under both.** Prime does not need to
adjudicate the readings to dispose of it.

**Matched-pair situation, both better and worse than hoped.** Two same-chassis, same-plant,
same-readout arrays exist — one matched more stringently than a promoter swap, by point-mutating
regulators so the same proteins are expressed and the same burden carried, with a genuine recovery
metric (settling time to re-enter an error band after a 2 h perturbation). **But neither array
contains a reference-holding positive member:** one array's negative member is a *non*-corrector (the
wrong axis — the negative control must correct), and the other's four architectures are all
proportional-type. **A same-chassis pair whose positive member holds a target as a state does not
appear in the retrieved literature.**

---

### 3.7 Candidates not scored

| Candidate | Disposition |
|---|---|
| *B. subtilis* sporulation phosphorelay | **Excluded by Ben's §0(a) ruling**, not by any S-criterion. Recorded so the exclusion is visibly a ruling. |
| Negative autoregulation (synthetic) | Scored on the Synthetic track as a **third negative-control option** — the cleanest model-free corrector available (operating point fixed entirely by its own kinetic constants; no slow controller variable exists). **But "demonstrably corrects" is NOT established for it**: the canonical literature shows stability and variance narrowing, not perturb-and-recover. `[primary-abstract-only]` / `[not-retrieved]` |
| NRI/NRII (NtrB/NtrC) | Same bifunctional architecture as EnvZ/OmpR; retained as the negative-control backup, scored less deeply. |
| Yeast HOG; yeast GAL; *E. coli* DNA repair; phage λ | Longlisted, not reached — the pair was found outside all five benchmark systems, so **no contamination cost was incurred and no benchmark literature was read for this arc.** |
| Genome-scale FBA models | **Ineligible on the face of the order** (S.1). |
| Mammalian/*Drosophila* clock; leptin/adiposity; end-product inhibition | Longlisted, not reached. The mammalian clock shares the KaiABC architecture with far worse intervention access. |

**A note on contamination, since the order asked for it to be priced.** The recommended pair —
KaiABC and EnvZ/OmpR — lies **entirely outside the five benchmark-rejected systems**. The order's
preference for a candidate outside all five is satisfied, and **the external benchmark's seat
availability is unaffected.** No contamination cost is claimed or owed.

## 4 · Three findings that outrun the selection task

**4.1 — AOP's core distinction is established prior art under four independent names.** The
stored-reference-versus-emergent-target distinction is argued in at least four literatures:
**settling point** (body-weight physiology), **balance point** (thermal physiology), **equilibrium
point** (thyroid endocrinology), and **absence of an internal model** (control theory). Per the
charter's *don't create when you can cite*, AOP should cite these rather than present the distinction
as new — and convergent independent discovery across four fields **strengthens** the framework rather
than diminishing it. This is the same shape as the project's strongest prior outcome.

A caution travels with it: the body-weight literature already states AOP's methodological problem —
that after a diet-refeed cycle a settling-point system returns to baseline in a way that could be
misread as defending a level — and, as of a 2023 review, states that experiments to discriminate the
models are still needed. **AOP's interventional separability test is the right shape of answer to a
problem this literature has posed and not solved.** That is the best available case that AOP's
contribution is real. It is also the reason to read the two paywalled Romanovsky papers before
claiming novelty.

**4.2 — ⚠ Sontag's internal-model theorem cuts against Reading A.** The theorem states that a system
adapting to a class of external signals must contain a subsystem capable of generating those signals,
and that this subsystem receives **only the error** as input. That is integral feedback — Reading B.
**If Gate 1 adopts the strict reading, AOP excludes the very architecture a published theorem
identifies as necessary for adaptation**, and needs an answer to why that error-driven internal model
is not a stored reference. This is a theoretical objection, not a retrieval gap. It should be
answered before Gate 2, and it is exactly where a competent critic will aim.
*(Retrieval note: read in the author's own arXiv preprint, `q-bio/0309003v1`; the published version is
paywalled. The substitution is declared, and the published wording is unverified.)*

**4.3 — ⚠ P1's second kill condition is under pressure from two directions, and prime should see them
together.** The freeze says P1 KILLS if "a system the criterion excludes is shown to have" competent
misregulation. Gate 1 has surfaced *three* excluded systems with published set-point-shifting operations
that leave regulation running:

| Excluded system | The operation | Machinery intact? |
|---|---|---|
| EnvZ/OmpR (native) | MzrA dosage — trans-acting, dose-tunable | Authors certify signal reception survives |
| EnvZ-derived cycle (engineered) | kinase:phosphatase ratio; small-molecule phosphatase destabilisation | Reversible, machinery otherwise untouched |
| Chemotaxis | CheB expression reduction; a 10 °C temperature change | Exact adaptation preserved throughout |

**All three are target-as-parameter systems, and in all three the target moved.** If any counts as
competent misregulation, P1 fires its kill condition on a system the criterion excludes — before the
experiment is run. The escape is that changing a rate constant is a machinery change; **but that escape
is the same argument that rejected these systems at S.2, and it must be applied in one direction only
at the risk of incoherence.** Either a rate-constant target is a target (then these systems have
competent misregulation and P1 is in trouble), or it is not (then they are correctly excluded, and P1's
kill condition needs re-phrasing so that a re-parameterisation does not satisfy it). **This is a
pre-registration drafting problem for prime, and it is the highest-value thing OAI could be pointed at.**


---

## 5 · Score summary

| # | Candidate | S.1 | S.2 | S.3 | S.4 | S.5 | Rd A | Rd B | Target | Role |
|---|---|---|---|---|---|---|---|---|---|---|
| **4** | **KaiABC clock** | **PASS** | **PASS** | **PASS** | PART (~10×) | **STRONG** | UNCLEAR | **YES** | **STATE** | **POSITIVE ARTICLE** |
| **8** | **EnvZ/OmpR** | PASS | FAIL* | PART | PART | WEAK | NO | NO | PARAM | **NEGATIVE CONTROL** |
| 10 | σ32 heat shock | PASS | FAIL* | FAIL | PART | **STRONG** | NO | NO | PARAM | negative control (alt.) |
| 1 | Chemotaxis (methylation) | PASS | **FAIL** | PASS | PART | WEAK | NO | YES | PARAM | reject; near-miss |
| 2 | Antithetic integral controller | PASS | **FAIL** | PART | PART | WEAK | NO | UNCLEAR | PARAM | reject |
| 11 | Negative autoregulation | PASS | FAIL* | — | — | WEAK | NO | NO | PARAM | negative control (3rd alt.) |
| 13 | Fever / hypothalamic | **FAIL** | UNDET | PASS | **FAIL** | — | NO | UNCL | UNDET | reject |
| 9 | NRI/NRII | PASS | FAIL* | — | — | — | NO | NO | PARAM | negative control (backup) |

*\*"FAIL\*" marks candidates for which the S.2 failure is the **qualification** for the negative-control
role rather than a defect.*

**The empirical pattern, and it is the most interesting thing in this report.** **Thirteen of fourteen
candidates are target-as-parameter.** Chemotaxis, heat shock, two-component signalling, synthetic
integral control, negative autoregulation, nitrogen regulation — four independent literatures, and in
every case the regulated target turns out to be a ratio of rate constants rather than a stored state.
**Only the clock stores its target as a state.**

Two readings of that, and this seat does not choose between them:

- **Favourable.** The criterion is not vacuous — it is selecting something rare, and it selects it
  correctly, placing a clock inside and every rate-constant regulator outside. This is what a criterion
  with teeth looks like.
- **Unfavourable.** The positive class may be nearly empty among well-characterised molecular systems,
  and the one member found is a system whose reference is arguably a model of the *environment* rather
  than of viability. A criterion that admits one borderline case out of fourteen is at risk of being a
  criterion for *clocks*.

**Either way, the state-versus-parameter filter did the work, not the autonomy question.** It disposed
of every rejected candidate, and it did so identically under both readings for all but one. **Gate 1's
substantive product is that filter**, and prime should consider whether it, rather than the invariant
subspace formulation, is the separability test §4 of the work order asks for.

---

## 6 · The pair

### 6.1 Recommendation

| Role | System | Standing |
|---|---|---|
| **Positive article** | **Cyanobacterial KaiABC clock** (*S. elongatus* PCC 7942) | Only S.2 PASS in the set; only target-as-STATE; STRONG S.5; a P1-shaped phenotype already in print |
| **Matched negative control** | **EnvZ/OmpR** (*E. coli*) | Model-free evidenced from two independent closed forms; both readings agree on exclusion; demonstrably corrects **on OmpR-P, not porin level** (§3.3) |

**Matched on:** both are dynamically-characterised molecular regulators with published quantitative
models; both have large physically performable intervention classes of the same *kind* (chromosomal
point mutation, titratable expression, trans-acting dosage); both read out through
phosphorylation-state-dependent transcriptional programs measured by fluorescent fusions. The contrast
is architectural in exactly the intended way — a stored phase read out onto a regulated program, versus
a target dissolved into the rate constants of one bifunctional enzyme.

**Where the match is imperfect, stated plainly:**

1. **Different organisms.** A cyanobacterium and an enterobacterium. Not matched on growth physiology,
   genetic toolkit, or environment.
2. **The negative control has no lifetime readout.** `[not-retrieved]` — so P3 cannot be run on the
   pair as constituted. The clock supplies a lifetime observable; EnvZ/OmpR does not.
3. **Asymmetric evidence for "corrects."** The clock's correction is dynamically demonstrated;
   EnvZ/OmpR's is established as steady-state robustness, with the dynamic-restoration experiment on
   OmpR-P apparently never run.

### 6.2 The alternative, and the trade-off prime must price

**Swap EnvZ/OmpR → σ32 heat-shock** and the pair gains a **STRONG lifetime readout on the negative
side** (survival and growth at elevated temperature, with published architecture-differentiated
comparison classes), which makes **P3 runnable on both arms**. The cost: σ32 also fails S.3 (every
retrieved perturbation degrades rather than redirects), so it is a *less* informative negative — it
fails on more axes than the one the criterion cares about. EnvZ/OmpR fails *only* on the sharp filter,
which is the more probative contrast.

**This seat's judgement, offered as a recommendation and not a decision: pair with EnvZ/OmpR if the arc
prioritises P1, and with σ32 if it prioritises P3.** Since P1 can kill the criterion and P3 cannot
(per the freeze), P1 should dominate — hence the §6.1 recommendation. **A third option prime should
consider: carry both negatives.** The order requires *a* matched negative control, not exactly one, and
the marginal cost of a second is low relative to what it buys on P3.

### 6.3 ⚠ The pair's principal defect: S.4 is not satisfiable by any candidate found

**No candidate in the set clears S.4's ≥2-orders-of-magnitude requirement**, and for the recommended
positive article the shortfall is *architectural rather than incidental*:

- Period spans 15 h→158 h across single substitutions at one KaiC residue — **~10×, a full order of
  magnitude, and still one order short.**
- **The two most benign actuators are barred by design.** Temperature does not tune period (Q10 ≈ 1.02–1.04
  in vivo) — that is temperature compensation, the system's signature. ATP/ADP does not tune period
  either: the oscillator holds period within 5% of 24 h across the physiological range **while phase
  and amplitude shift freely.** The system is built to separate a tunable phase from a robust period.
- **Every knob that does sweep the slow timescale is a *kaiC* point mutation — a machinery edit.**
- The one candidate fast-side knob (growth/dilution rate) tunes only ~5× and demonstrably feeds back on
  the oscillator.

**This is a genuine irony worth stating in the pre-registration rather than hiding: the property that
makes the clock a clean instance of a stored reference — a robust period — is the property that
prevents sweeping the slow/fast ratio.**

**Consequence under the freeze, which prime must price before decision #2.** P2's UNINFORMATIVE
disposition reads: "the achievable range on the chosen system is too narrow for a knee to have been
visible had one existed." **On the evidence retrieved, P2 is heading for UNINFORMATIVE by construction
on this pair.** That is not a reason to reject the pair — P2 cannot kill the criterion and no candidate
does better — but declaring a prediction whose uninformative outcome is foreseeable at selection time
is precisely the "version of this experiment that cannot fail" that OAI is briefed to hunt. **Better to
state the ceiling now, in the pre-registration, than to report it as a finding afterwards.**

Also note the reusable distinction this surfaced: **phase is a state, period is a parameter, and the
word "set-point" conflates them.** S.3 rides on phase; S.4 rides on period. Both read as "moving the
set-point with machinery intact" in prose, and they are not the same operation.

---

## 7 · What remains open

| Item | Status | Bearing |
|---|---|---|
| P1's line between a set-point move and a machinery change | **Unresolved; prime's call** | §3.3.1. Decides whether the negative control survives its own P1 threat, and must be consistent with the S.2 rejections |
| Reading A vs Reading B | **Unresolved; prime's call** | §2. Only the positive article is reading-sensitive; every rejection holds under both |
| Component (5) for the clock — own viable set vs model of the environment | **Unresolved; criterion interpretation** | §3.5. Canon v1.26's "declared persistence criterion" framing softens it substantially |
| Dynamic restoration of OmpR-P after a kick | `[not-retrieved]` | §3.3. Apparently never run; the pre-registration must declare the correcting variable accordingly |
| Sontag's theorem vs the strict reading | **Open theoretical objection** | §4.2. Needs an answer before Gate 2 |
| A lifetime readout for EnvZ/OmpR | `[not-retrieved]` | §6.1. Blocks P3 on the negative arm unless σ32 is carried |
| Nakajima 2005; Woelfle 2004; Aoki 2019; Becskei & Serrano 2000 | **Paywalled** | Ledger. None is load-bearing for the pair: the autonomy and fitness claims are independently `[primary-verified]` from other primaries |

---

## 8 · Compliance with the order's prohibitions

- **No operational pre-registration content written, sketched, or implied.** §§3.3.1, 4.2, 6.3 and 7
  flag questions *for* the pre-registration and price consequences under the *already-frozen*
  dispositions; none proposes declaration-tuple content, an intervention class, a search bound, or a
  numeric threshold.
- **No AOP quantity computed** on any candidate — no Drive, Memory, Integration, Boundary, semantic
  mask, MFPT, or minimum-cut dependence.
- **No system selected by this seat.** §6 is a builder's recommendation with trade-offs priced;
  selection concludes inside Gate 1 above this seat.
- No retired-framework vocabulary. A.1.9 not applied. No benchmark rejection treated as grounds for
  rejection here.
- **No secondary substituted for a blocked primary.** Two substitutions are declared at point of use
  and in the ledger (Sontag preprint for the published version; Briat et al. arXiv preprint for the
  *Cell Systems* version of record).
- **Author attributions:** three fabricated author lists were caught by review or self-check and
  corrected against PubMed records; the corrections are recorded, not silent. See the ledger's note 3.

---

*End of `AOP_LifeCriterion_SystemSelection_Report_v1_0_20260803.md`. Builder's proposal. Not
authorized, not self-certified. Prime verifies.*
