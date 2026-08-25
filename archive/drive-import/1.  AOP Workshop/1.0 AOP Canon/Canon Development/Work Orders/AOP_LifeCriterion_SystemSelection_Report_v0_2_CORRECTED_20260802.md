# Gate 1 — System selection for the life-criterion arc: SELECTION REPORT (INTERIM)

**Document ID:** `AOP_LifeCriterion_SystemSelection_Report_v0_1_20260802.md`
**Seat:** Claude Science (builder). **Date:** 2 August 2026.
**Order:** `TASK_CS_AOP_LifeCriterion_SystemSelection_20260801.md` (Drive `1pqmKxzablE53V4IXpW8inq-1EgT8rXfH`)
**Parent freeze:** `AOP_LifeCriterion_DispositionRule_FROZEN_v1_0_20260801.md` — Drive `1-HkXf58z-UWnYVkT1mcNR3_y2hIi3PAy`,
md5 `b7eebcfd5a371a78b33a5fe230d52554`. **Verified this session** by independent download and hashing
(6,824 bytes; computed md5 matches the order's).
**Ben's ruling in force:** §0 option (a). Sporulation reserved to H4/RED-25.

**Status: INTERIM. This report does not close Gate 1.** Three of five retrieval tracks are parked on
user-approval gates for publisher access and have not returned. Their absence is a *procedural* stop,
not a scientific finding, and it must not be read as a no-pair result. §7 states exactly what is
missing and what it would change.

**This seat does not select, does not pair, and does not grade its own output.** Prime verifies by
re-running retrievals or by independent reconstruction.

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

### 3.3 EnvZ/OmpR bifunctional two-component system — **leading negative control, with a caveat that may disqualify it**

*Contamination: clean. Track parked on approval; this section is the parent seat's own retrieval.*

**Both halves of the negative control's specification must be evidenced. One is; one is not.**

**Model-free: EVIDENCED.** `[primary-verified]` **[parent-reverified]** — this seat retrieved
Batchelor & Goulian 2003 (PNAS 100:691, via Europe PMC) and read the model section. In the
E. coli operating regime ([OmpR]_T ≫ [EnvZ]_T) the steady-state output reduces to a function of the
constants C_t and C_p, which are themselves combinations of Michaelis constants and rate constants
(C_p = k_k/k_p + …  = k_k/k_p·K_Mp). The paper states the circuit output is "independent of [EnvZ]_T"
in that limit, and that in the further limit it "is also independent of the phophotransfer rate
constants." **The output level is fixed by rate constants of the bifunctional enzyme; there is no
slow dynamical variable holding it.** This is exactly the target-as-parameter, model-free corrector
the order's §3 asks for — evidenced, not asserted.

**Corrects dynamically: NOT EVIDENCED, and this is a real gap.** `[not-retrieved]` The retrieved
primary establishes **robustness of the steady state across conditions**, not **restoration after a
kick**. Searching the full text for time-course, relaxation, transient, or recovery language returns
nothing: this is a steady-state analysis plus steady-state reporter measurements. **Robustness across
steady states and dynamic correction after a perturbation are different claims and must not be
conflated.** The order requires a negative control that *demonstrably corrects*. On the evidence
retrieved so far, EnvZ/OmpR is demonstrably **robust**; whether it demonstrably **corrects** is open.
Prime should treat this as a live requirement on the negative control, not a formality.

**Match quality with an *E. coli* positive candidate would be excellent** — same organism, same
phosphorylation-based signalling chemistry, comparable intervention class.

#### 3.3.1 ⚠ A live threat to P1, found in the negative control's own literature

**This is the most consequential finding in this report and it is a selection finding, not a
pre-registration one: it bears on whether this system can serve as the negative control at all.**

P1's second kill condition is that **a system the criterion excludes turns out to have competent
misregulation.** EnvZ/OmpR is a system the criterion excludes. There is a published, gold-OA result
in which an engineered EnvZ-derived covalent modification cycle is **simultaneously robust and
analogically tunable**: `[primary-verified]` **[parent-reverified]** — Jones RD, Qian Y, Ilia K,
Wang B, et al., "Robust and tunable signal processing in mammalian cells via engineered covalent
modification cycles," *Nat Commun*
13:1720 (2022), DOI 10.1038/s41467-022-29338-w, read in full by this seat. *(Author attribution
corrected on review: an earlier draft of this report named a first author that no retrieval in this
session had returned. The author list was subsequently retrieved from PubMed and is as given above;
the correction is recorded rather than silently made, because inventing an attribution is the
same class of defect this report was written to avoid.)* The output level "increases
gradually as the ratio of kinase-to-phosphatase increases," and the authors additionally tune the
output by modulating **phosphatase stability** with a small molecule (trimethoprim on a degradation
domain), with the machinery otherwise untouched.

**Why this threatens P1.** A model-free corrector is supposed to be only *degradable*, with no
separable target to move. Here the operating point is moved smoothly and reversibly by a small
molecule, and regulation continues. If that counts as *competent misregulation*, then a system the
criterion excludes has the failure mode the criterion says is exclusive to systems it includes, and
P1's second kill condition fires **on the negative control itself**.

**The counter-argument, stated fairly.** Changing the kinase:phosphatase ratio changes a kinetic
parameter *of the corrector*, which is arguably a machinery change rather than a set-point move — and
that is precisely why the state-versus-parameter distinction is load-bearing. Under that reading the
result is not competent misregulation but competent *re-parameterisation*.

**This seat does not adjudicate it.** But note the bind, because it is the sharpest thing Gate 1 has
surfaced: **the same argument that makes EnvZ/OmpR model-free (its target is a rate-constant ratio)
is the argument that makes its tunability not-a-set-point-move. If prime accepts that argument to
save P1, it must be applied consistently — and applied consistently it is also what rejected
chemotaxis at S.2.** The two systems' targets live in the same kind of place. What separates them is
whether a slow separable variable exists at all, not where the target is stored. Prime needs a
principled line here before the pre-registration freezes, and OAI will look for exactly this.

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

### 3.5 Candidates not scored

| Candidate | Disposition |
|---|---|
| *B. subtilis* sporulation phosphorelay | **Excluded by Ben's §0(a) ruling**, not by any S-criterion. Recorded so the exclusion is visibly a ruling. |
| KaiABC cyanobacterial clock | **PENDING** — track parked on approval. The only candidate expected eligible under Reading A. |
| Antithetic integral controller; negative autoregulation | **PENDING** — track parked on approval. |
| Yeast HOG; yeast GAL; *E. coli* DNA repair; phage λ | Longlisted, not reached. Contamination cost priced in the longlist. |
| Genome-scale FBA models | **Ineligible on the face of the order** (S.1: "not eligible"). |
| Mammalian/*Drosophila* circadian clock; leptin/adiposity; NRI/NRII; end-product inhibition | Longlisted, not reached. |

---

## 4 · Two findings that outrun the selection task

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

---

## 5 · Score summary

| # | Candidate | S.1 | S.2 | S.3 | S.4 | S.5 | Rd A | Rd B | Target | Role |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Chemotaxis (methylation) | PASS | **FAIL** | PASS | PART | WEAK | NO | YES | PARAM | not positive; near-miss |
| 10 | σ32 heat shock | PASS | **FAIL** | **FAIL** | PART | **STRONG** | NO | NO | PARAM | negative control |
| 8 | EnvZ/OmpR | PASS | **FAIL**(by design) | — | — | — | NO | NO | PARAM | negative control, caveated |
| 13 | Fever / hypothalamic | **FAIL** | UNDET | PASS | **FAIL** | — | NO | UNCL | UNDET | reject |
| 4 | KaiABC | \_ | \_ | \_ | \_ | \_ | \_ | \_ | \_ | **PENDING** |
| 2/11 | Antithetic / neg. autoreg. | \_ | \_ | \_ | \_ | \_ | \_ | \_ | \_ | **PENDING** |

*"FAIL(by design)" for EnvZ/OmpR: S.2 failure is what qualifies it as the negative control.*

**A pattern worth naming: every candidate scored so far is target-as-parameter.** Four systems, four
different literatures, no stored target anywhere. That is either evidence that the criterion is
selecting something rare and real, or evidence that its positive class may be empty among
well-characterised molecular systems. **Which of those it is depends entirely on the KaiABC track**,
the one candidate whose slow variable's value is plausibly the tracked reference — and that track
is parked.

---

## 6 · The pair — NOT YET DELIVERABLE

**Negative control: available.** σ32 heat-shock (§3.2) is the stronger nomination — it corrects, it is
model-free on the modelling authors' own words, and it has the only STRONG S.5. EnvZ/OmpR (§3.3) is
the better *match* for an *E. coli* positive article but carries two unresolved issues: dynamic
correction is not yet evidenced, and §3.3.1 is a live P1 threat.

**Positive article: none established.** Every candidate scored is target-as-parameter and fails S.2.
The one candidate expected to survive both readings is KaiABC, and its autonomy evidence
(Nakajima et al. 2005, the in vitro reconstitution) is **confirmed paywalled** — this seat attempted
retrieval independently and all five open routes failed.

**This is NOT a no-pair finding.** A no-pair finding under §5.3 would be an argued statement that no
pair *clears the criteria*. What this is instead: two candidate classes are unscored because retrieval
is blocked on pending approvals. Reporting a procedural stop as a scientific result would be exactly
the kind of overclaim this project's standing failure mode produces, and it would close Gate 1 on a
false basis.

---

## 7 · What is missing and what it would change

| Missing | Blocking on | What it decides |
|---|---|---|
| KaiABC autonomy (Nakajima 2005, *Science*) | `science.org` approval | Whether **any** candidate is Reading-A-eligible; whether a positive article exists at all |
| KaiABC fitness (Woelfle 2004, *Curr Biol*) | `cell.com` approval | The only STRONG S.5 available to a *positive* article |
| Antithetic controller equations (Aoki 2019, green OA at ETH) | repository approval | Whether an engineered integral controller is target-as-state or target-as-parameter; matched-pair feasibility on one chassis |
| Shinar 2007 ACR full text | Europe PMC served front matter only | Independent structural confirmation of the EnvZ/OmpR model-free claim |
| Dynamic correction in EnvZ/OmpR | not yet searched to exhaustion | Whether the leading negative control meets the order's "demonstrably corrects" requirement |

**On resumption, this report goes to v0.2 and either delivers the pair or argues the no-pair finding
on scientific grounds.**

---

## 8 · Compliance with the order's prohibitions

- No operational pre-registration content written, sketched, or implied. §3.3.1 and §4.2 flag
  questions *for* the pre-registration; neither proposes its content.
- **No AOP quantity computed** on any candidate.
- No system selected; no pair declared.
- No retired-framework vocabulary used.
- A.1.9 not applied. No benchmark rejection treated as grounds for rejection.
- No secondary substituted for a blocked primary; the one substitution made (Sontag preprint for the
  published version) is declared at point of use and in the ledger.
- **Two fabricated author attributions were caught on review and corrected** (§3.3.1 and the ledger).
  Both are recorded as corrections rather than silently fixed. See the ledger's note 3.

---

*End of `AOP_LifeCriterion_SystemSelection_Report_v0_1_20260802.md`. Builder's proposal. Interim.
Not authorized, not self-certified. Prime verifies.*
