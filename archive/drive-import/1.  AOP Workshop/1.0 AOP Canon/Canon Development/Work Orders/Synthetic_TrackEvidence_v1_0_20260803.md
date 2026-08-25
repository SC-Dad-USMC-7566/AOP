# Synthetic_retrieval_v1 — Track: engineered and reconstituted controllers

**Seat:** Claude Science (BUILDER). **Status:** PROPOSAL for verification by another seat. Not a verdict.
**Gate:** AOP Gate 1, life-criterion falsification arc. **Date:** 2026-08-02.
**Scope discipline:** no AOP quantity computed; no pre-registration drafted; no selection or pairing made.

Retrieval tags used per claim: `[primary-verified]` = I read the relied-on passage in the primary;
`[primary-abstract-only]`; `[secondary]`; `[not-retrieved]`.

---

## 0. Headline findings (each tagged below)

1. **The antithetic set-point is a ratio of two kinetic rate constants, μ/θ — not a stored state.**
   Verified in two independent primaries from the originating group. This is a decisive S.2/S.3
   finding and it makes the flagship "reference-holding" engineered architecture come out
   **target-as-parameter**, contrary to the track brief's working expectation.
2. **A matched pair on one chassis exists and is better than expected — but the *positive* member of
   the best-matched pair is not reference-holding.** Frei et al. (PNAS 2022) run closed-loop
   antithetic integral vs. an open-loop analog differing by one promoter swap, same plant, same
   readout. Hu & Murray (Nat Commun 2022) run four architectures (open loop / cis / trans / layered)
   built to be genetic-context-matched by point-mutating the regulators rather than deleting them.
3. **Set-point retuning with the controller intact IS demonstrated** — but by *plasmid ratio*
   (Frei) or *inducer-set expression rate* (Filo, simulation), both of which move a **kinetic
   parameter**, not a state. The cleanest-in-biology S.3 operation the brief hoped for does not
   materialize as a state move.
4. **A viability-relevant antithetic application exists**: population growth control via the toxin
   CcdB coupled through quorum sensing. This partially answers the "arbitrary target vs. own viable
   set" objection but only at the *population* level, and I retrieved it as an analysis, not as the
   experimental primary.
5. **The fatal objection largely stands.** Every engineered controller I verified regulates a
   fluorescent reporter or an orthogonal protein. The reference is for an arbitrary target.

---

## 1. Antithetic integral feedback — what sets the set-point

### 1.1 The theory primary

**Citation.** Briat C, Gupta A, Khammash M. "Antithetic Integral Feedback Ensures Robust Perfect
Adaptation in Noisy Biomolecular Networks." *Cell Systems* 2 (2016) 15–26. DOI
10.1016/j.cels.2016.01.004. PMID 27136686 (a duplicate PubMed record, PMID 27135166, exists for the
same title — flagging for the metadata check).

**Provenance caveat — important.** `fetch_article_fulltext` on the Cell Systems DOI resolved to
**arXiv:1410.6064**, the author preprint, not the published Cell Systems article. Unpaywall reports
this as `oa_status: bronze` with the arXiv PDF as the OA location. Everything I quote below is read
from **that preprint PDF**, 19 pages. The *published* version is `[not-retrieved]`. Section titles
and Proposition/Theorem numbering matched what the published version is cited as containing, but I
did not verify the published text. **Any quotation must be re-checked against the Cell Systems
version of record before it is relied on.**

**Claim 1.1a — the controller is four reactions: reference, measurement, comparison, actuation.**
`[primary-verified]` The paper labels these four reactions explicitly in its Eq. (1): a birth
reaction for Z1 at rate μ (reference), a birth of Z2 at rate θ·X_ℓ (measurement), mutual
annihilation Z1+Z2 → ∅ at rate η (comparison), and birth of X1 at rate k·Z1 (actuation).

**Claim 1.1b — the set-point is μ/θ, and the paper says in its own words that this value is
implemented as a rate constant.** `[primary-verified]` The paper states the first reaction
<q>"sets the value of the reference"</q> and that <q>"This value is implemented as the birth-rate of
species Z1."</q> The reference is defined as μ* = μ/θ. Read on the preprint p. 6.

**Claim 1.1c — the tracking result is E[X_ℓ] → μ/θ.** `[primary-verified]` Theorem 2 (unimolecular
case) concludes asymptotic set-point tracking "i.e. E[X_ℓ(t)] → μ/θ as t → ∞", conditional on
ergodicity, output controllability (their condition 7) and accessibility of the set-point (their
condition 8). Proposition 3 gives the same limit for the specific gene-expression plant
X1 →(γ1) ∅, X1 →(k2) X1+X2, X2 →(γ2) ∅, and states it holds "for any positive values of the
parameters k, k2, γ1, γ2, η, θ and μ."

**Claim 1.1d — the integrator state and the target are different objects, in the paper's own
algebra.** `[primary-verified]` The paper defines δZ(t) := Z1(t) − Z2(t) and derives
dE[δZ]/dt = μ − θ·E[X_ℓ], then integrates to get E[δZ(t)] = θ∫₀ᵗ e(s)ds + E[δZ(0)] with tracking
error e(t) := μ/θ − E[X_ℓ(t)]. So δZ is the **integrator state** (it accumulates error), while μ/θ
— the **target** — is the zero of that rate law, built from two rate constants. This is exactly the
brief's target-as-parameter signature, and it is visible in the primary's own equations.

**Claim 1.1e — the authors themselves recommend tuning the set-point via θ.** `[primary-verified]`
In the metabolic-cost discussion they note a low metabolic load "can therefore be easily achieved by
first setting μ to a small value and then adjusting the set-point value with θ." θ is a rate
constant of the measurement reaction. Moving the set-point is, on the authors' own recommendation, a
kinetic-parameter change.

**Claim 1.1f — no slow/fast timescale ratio is declared for the controller in this paper.**
`[primary-verified, negative result]` A full-text scan for "timescale / time-scale / time scale"
returned a single hit, and it concerns fast creation/annihilation in a metabolic-load argument, not a
declared controller/plant separation. The paper's robustness claim is the opposite in spirit: the
result holds "for any k, η > 0", i.e. it is *not* premised on a timescale separation. S.4 for this
architecture has to be sourced elsewhere (see §5).

### 1.2 The equation-level corroboration (independent primary, gold OA, published version)

**Citation.** Filo M, Kumar S, Khammash M. "A hierarchy of biomolecular proportional-integral-
derivative feedback controllers for robust perfect adaptation and dynamic performance." *Nature
Communications* 13:2119 (2022). DOI 10.1038/s41467-022-29640-7. PMID 35440114. Gold OA; I read the
publisher PDF (19 pp).

**Claim 1.2a — set-point = μ/θ, stated as a closed-form result independent of the plant.**
`[primary-verified]` The paper's Eq. (3) is g(μ, x̄_L) = θ·x̄_L, and it states that for the aI and
aPI controllers of Class 1 and 2 the reference propensity is g(μ, x_L) = μ, "and thus x̄_L = μ/θ".
It then observes that this fixed-point equation "does not depend on the plant" and that the output
therefore "converges to a unique setpoint that is independent of the plant." This is a second,
independent, *published-version* confirmation of Claim 1.1b/1.1c.

**Claim 1.2b — for a higher-order aPID design the set-point is μ/(θβ), still a parameter ratio.**
`[primary-verified]` "the setpoint for the second-order design is given by x̄_L = μ/θβ with the
requirement that β < θ; whereas the set-points for both higher-order designs are given by
x̄_L = μ/θ." Note β is itself a rate constant, and the design carries a *constraint between rate
constants* (β < θ) — i.e. moving the target by moving β can violate the design condition. This is
the target-as-parameter hazard in concrete form.

**Claim 1.2c — the authors describe the set-point as residing in a rate.** `[primary-verified]` In
the genetic implementation of the third-order aPID controller they write that <q>"The setpoint is
encrypted in the expression rate μ of Z1"</q>, tunable with homoserine lactone (HSL). Their Fig. 8b
shows a simulated step change of set-point μ/θ at t = 8 h against a disturbance injected at t = 16 h
(aTc-tunable). **This is a simulation, not an experiment** — the paper's own words are "Deterministic
simulations… carried out using biologically realistic numerical values."

### 1.3 The experimental realisation — BLOCKED

**Citation (metadata verified, content not).** Aoki SK, Lillacci G, Gupta A, Baumschlager A,
Schweingruber D, Khammash M. "A universal biomolecular integral feedback controller for robust
perfect adaptation." *Nature* 570 (2019) 533–537. DOI 10.1038/s41586-019-1321-1. PMID 31217585.

**What I established.** `[primary-abstract-only]` The abstract states they "genetically engineer a
synthetic integral feedback controller in living cells and demonstrate its tunability and adaptation
properties", and reports "A growth-rate control application in Escherichia coli". So *tunability* is
claimed and *growth rate* is the application — both directly on point for S.3 and for the
viability-relevance objection. **I could not read the passage, the equations, the tuning mechanism,
the numbers, or the range.** The brief asked for "the numbers and the range" for inducer-driven
set-point retuning; from this paper I do not have them. See the blocked ledger (§8).

**Indirect, weaker evidence about the same experiment.** `[secondary]` Filo et al. cite this work
(their ref. 9) as the source of the σ-factor / anti-σ-factor (SigW/RsiW) sequestration pair and as
the basis for HSL-tunable μ. Frei et al. describe it as "An earlier implementation of the antithetic
integral feedback motif in bacteria … used a σ and anti-σ factor pair to realize the sequestration
reaction." These are other papers' reports and do **not** substitute for the primary.

---

## 2. Is the set-point inducibly movable with the controller intact?

**Answer: yes, demonstrated experimentally — but the knob is a kinetic parameter, not a state.**

**Claim 2a — Frei et al. moved the set-point across a 32-fold range by plasmid ratio, with the
controller functioning, and confirmed adaptation at each set-point.** `[primary-verified]`
Frei T, Chang C-H, Filo M, Arampatzis A, Khammash M, "A genetic mammalian proportional–integral
feedback control circuit for robust and precise gene regulation," *PNAS* 119(24):e2122132119 (2022),
DOI 10.1073/pnas.2122132119, PMID 35687671; read via PMC full text. They "vary the setpoint by
transfecting the two plasmids at ratios ranging from 1/16 to 2 (activator plasmid / antisense
plasmid)", in HEK293T cells, measured 48 h post-transfection by flow cytometry, and report that "As
the setpoint ratio increases, so does the fluorescence of tTA-mCitrine, indicating that our circuit
permits setpoint control." Disturbance was applied as ASV-induced degradation via a SMASh tag
(0.033 µM in the main experiment; a 30 nM condition is used in the network-perturbation panel).
Adaptation criterion and result: "We consider a circuit to be adapting if its normalized
fluorescence intensity stays within 10% of the undisturbed control. Under this criterion, adaptation
is achieved for all the setpoints tested below two in the closed-loop configuration. In contrast,
none of the open-loop configurations manage to meet this adaptation requirement."

**Claim 2b — Frei et al. state in their own words that the set-point is determined by a ratio of
production rates.** `[primary-verified]` "the setpoint is a function of the ratio of the production
rates of the two controller species". They use this to explain why the set-point is robust to
shared-resource variation: when both controller-species production rates depend similarly on the
same resource pool, "the effect of this dependence cancels out", whereas if they draw on different
pools "the setpoint becomes sensitive". They also note the set-point "is determined by the ratio
between sense and antisense mRNA plasmid", and argue it survives cell division because both plasmids
partition without bias so the average ratio is preserved.

**Interpretation for S.3 (mine, not the paper's).** Plasmid copy-number ratio is a durable,
externally imposed, physically performable operation that moves the target while the controller keeps
working — it satisfies the *letter* of S.3. But what it moves is the **ratio of two production
rates**, i.e. a kinetic parameter of the controller, set at transfection. It is not a stored state
that the fast dynamics read out and that could be re-written while the system runs.

**Claim 2c — Filo et al.'s HSL-tunable set-point is simulated, not measured.** `[primary-verified]`
See Claim 1.2c. Their experimental demonstration is a different thing: an *in silico* PID controller
in a hybrid "cyberloop" regulating an optogenetic circuit in single yeast cells — i.e. the controller
is a computer, not a biomolecular reference.

---

## 3. Negative-control candidates

### 3.1 Negative autoregulation — does it demonstrably CORRECT?

This is the requirement the brief flags: a negative control must be a *corrector*, not a
non-corrector. My verdict is **PARTIAL, and this is the weakest link in the track.**

**Claim 3.1a — the canonical NAR primaries are both paywalled.** `[not-retrieved]` for content:
- Becskei A, Serrano L. "Engineering stability in gene networks by autoregulation." *Nature* 405
  (2000) 590–593. DOI 10.1038/35014651. PMID 10850721. OpenAlex: `oa_status: closed`,
  `any_repository_has_fulltext: false`.
- Rosenfeld N, Elowitz MB, Alon U. "Negative autoregulation speeds the response times of
  transcription networks." *J Mol Biol* 323 (2002) 785–793. DOI 10.1016/S0022-2836(02)00994-4.
  PMID 12417193. OpenAlex: `oa_status: closed`.

For Becskei & Serrano I have `[primary-abstract-only]`: the abstract states they "designed and
constructed simple gene circuits consisting of a regulator and transcriptional repressor modules in
Escherichia coli and we show the gain of stability produced by negative feedback." That is a
*stability/variance-narrowing* claim. **The abstract does not establish a perturb-and-recover
experiment**, and I did not read the figures, so whether they demonstrate *correction after a
deliberate displacement* is `[not-retrieved]`. For Rosenfeld et al. I have neither content nor
abstract text beyond the title; response-time acceleration is in any case a *transient-dynamics*
claim, not a correction-after-perturbation claim.

**Claim 3.1b — a retrievable NAR primary with a matched no-feedback comparator on one chassis
exists.** `[primary-verified]` Nevozhay D, Adams RM, Murphy KF, Josić K, Balázsi G. "Negative
autoregulation linearizes the dose–response and suppresses the heterogeneity of gene expression."
*PNAS* 106(13):5123–5128 (2009). DOI 10.1073/pnas.0809901106. PMID 19279212. Retrieved as a green-OA
PDF via Semantic Scholar (Europe PMC render), 6 pp.

Their construct pair is exactly the shape a matched negative control wants, in *S. cerevisiae* with
chromosomally integrated cascades: an **NR cascade** (yEGFP reporter + constitutively expressed
TetR, no feedback) and a **linearizer NF cascade** built from it by "replacing the upstream PGAL1
promoter with the PGAL1-D12 promoter, thereby introducing negative autoregulation into the cascade."
They report the NF circuit gives a dose–response "linear up to 90% saturation" and a "massive
(7-fold) reduction of noise at intermediate induction."

**Claim 3.1c — the target in NAR is baked into kinetic constants, with no separable reference.**
`[primary-verified]` Their model (their Eqs. 1–2) is
dx/dt = a·F_x(x) − b·x·y − d·x ; dy/dt = C − b·x·y − f·y ; dz/dt = a·F_z(x) − d·z,
with F_x(x) = F_z(x) = θⁿ/(θⁿ + xⁿ) — θ the induction threshold, n the Hill coefficient, a synthesis
rate, b association, d dilution-by-growth, f inducer removal, C proportional to extracellular
inducer. The paper states explicitly that "The set of Eqs. 1 also describes the cascade without
feedback (NR) after setting F_x = 1" — i.e. the *only* structural difference between the pair is
whether the regulator represses its own promoter. There is no controller species, no integrator, no
slow variable holding a target: the operating point is fixed by {a, d, θ, n} and the inducer level C.
At steady state below saturation they derive z = C/d. **This is a clean model-free-corrector
signature: nothing separable to move.**

**Claim 3.1d — what Nevozhay does NOT show.** `[primary-verified, negative result]` A full-text
scan for perturbation/robustness language returned one hit, and it is about robustness of
*linearization to parameter variations*, not recovery from a displacement. Their experiments are
steady-state dose–response and noise measurements at various ATc levels. **They do not perform a
perturb-and-recover experiment.** So NAR-as-corrector is, across everything I retrieved, argued from
model structure and from variance narrowing — not demonstrated as active correction after
displacement. Prime should treat "the negative control demonstrably corrects" as **not yet
established** for NAR.

**Claim 3.1e — an alternative NAR primary I retrieved but which does not close the gap.**
`[primary-verified, negative result]` Dublanche Y, Michalodimitrakis K, Kümmerer N, Foglierini M,
Serrano L, "Noise in transcription negative feedback loops: simulation and experimental analysis,"
*Mol Syst Biol* 2:41 (2006), DOI 10.1038/msb4100081, PMC1681513 — full text retrieved (36.7 kB). Its
section structure is noise analysis, simulation, correlated noise, noise frequency. Scans for
"steady-state concentration/level/value" and for "perturb / recover / return to / disturbance"
returned **zero hits**. It is a noise paper, not a correction paper.

### 3.2 Reconstituted / in vitro corrector

**Claim 3.2a — a cell-free integral controller exists, with an explicit open-loop matched
comparator.** `[primary-verified]` Agrawal DK, Marshall R, Noireaux V, Sontag ED. "In vitro
implementation of robust gene regulation in a synthetic biomolecular integral controller." *Nature
Communications* 10:5760 (2019). DOI 10.1038/s41467-019-13626-z. PMID 31848346. Gold OA; I read the
publisher PDF (12 pp). Implemented in an *E. coli* cell-free TX-TL system.

Architecture, in the paper's terms: three genes x, y, z; sequestration ("annihilation") between
proteins X and Y performs the error computation; free X (denoted X_R, "the R for remaining after
binding to Y") acts as transcriptional activator on the y and z promoters; deGFP production rate is
the read-out. **The reference here is a DNA input concentration**: the paper states the reference
signal is "a scaled value of an input P_X … representing input gene copy number", and their figure
legend says "The reference is set by the input DNA P_X". Tested at 0.1–0.7 nM P_X with 1 nM each of
P_Z^tot and P_Y^tot.

**Claim 3.2b — they ran a genuinely matched open-loop control, and controlled for the obvious
confound.** `[primary-verified]` Open loop = replace P_Y^tot with P_YC^tot (a non-interacting
version of Y); closed loop = P_Y^tot present. Result: closed-loop deGFP slopes were linearly
proportional to P_X; open-loop slopes depended nonlinearly on P_X. They then re-ran the open loop
under conditions matching closed-loop output levels, "even when the open and closed-loop output
levels are similar", and state this "provides a controlled comparison and shows that feedback is
responsible for the reference tracking behavior." They also verified P_YC^tot has no effect on deGFP
slopes, and that no deGFP is produced absent P_X.

**Assessment for this track (mine).** This is a *reference-holding* in vitro controller whose
reference is an externally supplied DNA concentration — arguably closer to "target as a settable
quantity" than μ/θ, but it is an *input*, supplied from outside the system, not a state the system
maintains for itself. It also has no viable set and no lifetime: it is a batch TX-TL reaction whose
reporter has no degradation tag, so the paper explicitly cannot observe steady state ("we cannot
observe a steady-state behavior in the measured responses") and works with production-rate slopes
instead.

---

## 4. Matched-pair feasibility — the key deliverable

**Yes. Two same-chassis, same-plant, same-readout, architecture-only-difference pairs are
retrievable and verified. Neither is a perfect fit for the arc's needs, for different reasons.**

### Pair A — Frei et al. 2022 (PNAS), HEK293T `[primary-verified]`
- Positive member: closed-loop antithetic integral (sense/antisense mRNA sequestration).
- Negative member: open-loop analog. Difference is one promoter: "we built an open-loop analog of
  the closed-loop circuit, in which the TRE promoter was replaced by a noncognate promoter." They
  call it "An experimental control incapable of producing integral feedback".
- Same plant (tTA-mCitrine), same readout (mCitrine flow cytometry), same perturbations
  (ASV-induced degradation; an added L7Ae translational negative-feedback loop as a *network
  topology* perturbation; a shared-resource/burden disturbance with strengths varied 0.6–3.5).
- **Why it is imperfect for this arc:** the open-loop analog is a *non-corrector*, not a model-free
  corrector. The brief requires the negative control to correct. So Pair A is a
  corrector-vs-noncorrector contrast, which is the wrong axis.

### Pair B — Hu & Murray 2022 (Nat Commun), *E. coli* `[primary-verified]`
Hu CY, Murray RM. "Layered feedback control overcomes performance trade-off in synthetic
biomolecular networks." *Nature Communications* 13:5393 (2022). DOI 10.1038/s41467-022-33058-6.
PMID 36104365. Gold OA; publisher PDF read (13 pp).
- **Four architectures on one chassis:** open loop, cis feedback (sRNA AS/Att pair repressing
  sfYFP), trans feedback (LacI repressing P_Rhl/LacO), layered (both). Strain JS006 ΔLacI with
  genomic RhlR; two-plasmid system (p15A + ColE1); readout sfYFP.
- **The context-matching is deliberate and is the reason this pair matters:** "To avoid genetic
  context change and metabolic load variation, we created mutated regulator pieces to disable
  feedbacks without changing the genetic context." Specifically AS paired with an orthogonal
  attenuator Att(M) disables cis feedback, and LacI(M) — LacI with the LacO binding site removed —
  disables trans feedback. They separately part-characterized that Att(M) and LacI(M) are
  "appropriate control[s]". This is a stronger form of matching than a promoter swap: the same
  proteins are expressed, the same burden is carried, only the regulatory interaction is deleted.
- **It has a correction readout with an explicit recovery metric:** chemical perturbation introduced
  at steady state and removed after two hours; robustness = scaled peak disturbance, speed =
  settling time defined as time "from the beginning of the perturbation to the time it takes for the
  profile to recover into the error band", error band 0.25. Six perturbation experiments (chemical,
  temperature, nutrient — each in two directions). Reported differences across the four constructs
  were statistically significant for the chemical perturbations.
- **Honest caveat, from the paper:** in the nutrient down-shift experiment "most of the trajectories
  were not trending towards recovery after 26 h of growth", so no settling time was computed, and
  the authors say "it is unclear why the temporary nutrient down-shift would cause such a drastic
  dynamical up-shift." Also the reduced model stopped describing the dynamics past ~7 h as cultures
  approached stationary phase (dilution rate d is not constant).
- **Why it is imperfect for this arc:** none of the four architectures is an integral controller.
  All four are proportional-type negative feedback (or none). So Pair B is a
  corrector-vs-corrector-vs-noncorrector array **with no reference-holding member**. It is an
  excellent *negative-control* chassis and a poor positive article.

**Consequence for pairing (flagged, not decided — pairing is the parent seat's job).** The
best-matched pairs available on one chassis do not contain a reference-holding positive member in
the sense the criterion needs, because — per §1 — the antithetic architecture that *looks* like the
positive member is target-as-parameter. A same-chassis pair whose positive member holds a target as
a *state* did not appear anywhere in what I retrieved.

---

## 5. S.4 — slow/fast timescale ratio

**Claim 5a — the antithetic literature does declare a timescale separation, but on the wrong axis
for S.4.** `[primary-verified]` Olsman N, Baetica A-A, Xiao F, Leong YP, Murray RM, Doyle JC.
"Architectural Principles for Characterizing the Performance of Antithetic Integral Feedback
Networks." *iScience* 14 (2019) 277–291. DOI 10.1016/j.isci.2019.04.004. PMC6479019; full text
retrieved. They state that a condition on the sequestration binding rate η "characterizes a
separation of timescales between the production and degradation dynamics of the system … and the
antithetic feedback reaction", with the reading that "so long as binding is sufficiently fast, it
does not affect the stability and performance of the circuit's output."

That is a **fast-controller** separation (sequestration fast relative to the plant), the opposite
orientation from a slow reference variable sitting above fast regulated dynamics. I found **no
primary that declares and sweeps a slow-reference / fast-plant ratio over ≥2 orders of magnitude for
an engineered controller.** The tunable knobs plainly exist in principle (degradation tags,
dilution/growth rate, plasmid copy number, inducer kinetics) and Olsman et al. sweep η over ranges
in simulation, but I did not retrieve a passage establishing a ≥2-decade *slow/fast* sweep. S.4 is
therefore scored PARTIAL on evidence, not PASS — the engineering intuition that synthetics are
strong here is `[not-retrieved]` as a specific claim.

**Claim 5b — controller-species dilution/leak is a known, named problem.** `[secondary]` Two
retrieved titles address it directly: "Realizing 'integral control' in living cells: how to overcome
leaky integration due to dilution?" (*J R Soc Interface* 2018, PMC5832733) and Frei et al.'s own
treatment: `[primary-verified]` they note "In practice, the dilution/degradation rate is never
exactly zero, which makes the integrator 'leaky'", and that in that case no explicit steady-state
formula is available (only implicit polynomial ones, which they fit). This matters for the arc
because a leaky integrator's operating point is *not* purely μ/θ — it becomes plant-dependent.

---

## 6. S.5 — lifetime readout and viability relevance

**Claim 6a — no lifetime readout in anything I verified.** `[primary-verified, negative result]`
Scans of the Olsman full text for "lifetime / survival / first-passage / extinction" returned zero
hits. Frei, Filo, Agrawal, Hu & Murray and Nevozhay report fluorescence steady states, dose–response
curves, noise/CV, settling time and peak disturbance. **No survival curve, no hazard, no chemostat
washout, no first-passage-to-failure.** Hu & Murray's settling time is the closest thing to a
first-passage quantity, but it is passage back *into* an error band, not passage *out of* a viable
set.

**Claim 6b — a viability-relevant antithetic application does exist, at population level.**
`[primary-verified in Olsman; the underlying experiment not-retrieved]` Olsman et al. devote a
section to "Antithetic Integral Feedback in a Synthetic Bacterial Growth Control Circuit" where
"growth control is achieved by regulating the production of the toxin CcdB", coupled to population
size by quorum sensing via AHL, so that "the population as a whole will converge to a steady-state
size that is less than the carrying capacity of the environment"; antithetic feedback supplies the
extracellular set-point knob. They also note "Qualitatively similar long-term oscillatory behavior in
a CcdB-based growth control circuit was observed in" (a cited experimental work I did not retrieve).

**Assessment.** This is the strongest available answer to the brief's "arbitrary target vs. own
viable set" objection: a toxin-mediated growth-rate target is viability-relevant in a way mCitrine is
not. But (i) the regulated variable is *population size*, so the persister whose viable set is at
stake would be the population, not the cell — a boundary question I am not authorized to adjudicate;
(ii) I retrieved it as a modelling section, not as the experimental primary; and (iii) Aoki et al.'s
E. coli growth-rate control application, which is the on-point experiment, is blocked (§8).

**Claim 6c — the fatal objection stands for everything verified.** `[primary-verified]` Regulated
variables across the verified set: tTA-mCitrine fluorescence (Frei), deGFP production rate
(Agrawal), sfYFP (Hu & Murray), yEGFP (Nevozhay), an abstract species X_ℓ (Briat, Filo). All are
reporters or orthogonal proteins. The reference, where one exists, is for an arbitrary target.

---

## 7. Eligibility under both readings, and the target determination

### Reading A (STRICT / autonomy: ẋ = f(x), no dependence on y) — **NO**
`[primary-verified]` Excluded by construction and by the primaries' own equations. In Briat et al.
the measurement reaction produces Z2 at rate θ·X_ℓ, so the controller state is *driven by the
regulated output*: dE[Z2]/dt = θ·E[X_ℓ] − η·E[Z1Z2]. Frei et al. state the same topology in words:
"Z2 is produced at a reaction rate that is proportional to θ and the regulated output species X_L."
The slow controller coordinates are not closed in themselves. This is textbook integral feedback,
which Reading A excludes.

### Reading B (LOOSE / scale separation + load-bearing coupling + separate addressability) — **UNCLEAR, leaning NO**
`[primary-verified]` Two of three conditions are met and the third fails on the object that matters:
- Load-bearing coupling onto y that sets y's operating point: **met** (x̄_L = μ/θ, plant-independent).
- Separate intervention addressability: **met in practice** (plasmid ratio, HSL-set μ, θ).
- Declared timescale separation with a slow *reference*: **not met as retrieved** — the declared
  separation runs the other way (fast sequestration, §5a), and integrator leak by dilution is a
  known defect rather than a designed slow scale.

But the decisive problem is not the timescale: it is that the object being addressed is a rate
constant, so Reading B admits this system only if Reading B is willing to call a kinetic parameter a
"stored target." That is precisely the second filter, and it resolves against admission.

### Where the readings disagree
They disagree on *whether feedback y→x disqualifies*, and under Reading B alone this architecture
would look eligible on the coupling and addressability tests. **But the target-as-parameter filter
cuts it under both readings**, which is the useful finding: the two readings do not need to be
adjudicated to dispose of this candidate. That is worth flagging to the parent seat — this candidate
is insensitive to the Gate 1 ambiguity.

### target_is: **PARAMETER**
`[primary-verified]` The integrator *state* is δZ = Z1 − Z2 (Briat Eq. 3–4), which accumulates the
error and is emphatically not the target. The *target* is μ/θ (Briat Thm 2, Prop 3; Filo Eq. 3), a
ratio of two rate constants — a zero of the integrator's rate law. Moving it means changing μ or θ:
the birth rate of a controller species or the measurement gain. For the aPID second-order design the
target μ/θβ carries the design constraint β < θ, so the parameter move can break the design
condition. This is exactly the brief's target-as-parameter case, established from the models' own
equations in two independent primaries, one of them a published version-of-record.

**Caveat on the state/parameter call.** Frei's plasmid-ratio operation is a genuine physical
intervention that moves the target with machinery intact, and one *could* argue the plasmid copy
number is a slowly-varying material state of the cell rather than a parameter. I am flagging this as
the live counter-argument rather than dismissing it; the paper's own framing — "the setpoint is a
function of the ratio of the production rates" — is parameter language, so I score PARAMETER and
leave the counter-argument on the record for the parent seat.

---

## 8. Blocked-retrieval ledger

**8.1 Aoki et al. 2019, Nature — the single most consequential block on this track.**
DOI 10.1038/s41586-019-1321-1, PMID 31217585. Needed for: the experimental antithetic realisation;
whether inducer-driven set-point retuning was demonstrated *in the lab*; the numbers and range for
that retuning; and the E. coli growth-rate control application, which is the best candidate answer
to the viability-relevance objection. Routes attempted, all failed:
1. `fetch_article_fulltext` (auto) — Unpaywall returned no valid PDF; Semantic Scholar no
   openAccessPdf; PMC no PMCID; Crossref TDM no accessible content; DOI resolve reached the landing
   page only.
2. `fetch_article_fulltext` with `prefer_format=pdf_url` — same five routes, no PDF URL.
3. PubMed `convert_article_ids` — no PMCID exists, so no PMC route.
4. OpenAlex works record (via API key) — reports `oa_status: green`,
   `any_repository_has_fulltext: true`, `oa_url = http://hdl.handle.net/20.500.11850/351590`, an
   **acceptedVersion in ETH Zurich's own institutional repository** (author-deposited; a legitimate
   green-OA route, not a mirror).
5. `hdl.handle.net` — blocked by sandbox allowlist (403 at proxy).
6. Requested and was **granted** network access to `www.research-collection.ethz.ch`; the host then
   returned **HTTP 403 to my client** on the handle URL.
7. Three documented DSpace REST endpoints on that same host
   (`/server/api/discover/search/objects`, `/rest/handle/…`, `/server/api/pid/find`) — all 403.
8. arXiv search via the literature connector — the 2019 Nature paper has no arXiv version (the 2016
   theory paper does, arXiv:1410.6064; a related 1911.05732 is a different paper).
**Not attempted, deliberately:** no user-agent spoofing, no mirrors, no archive or proxy sites.
Bibliographic metadata is verified (authors, title, journal, year, DOI, PMID via PubMed); **content
is `[primary-abstract-only]`.**

**8.2 Becskei & Serrano 2000, Nature.** DOI 10.1038/35014651, PMID 10850721. Needed for: whether
negative autoregulation demonstrably corrects after perturbation. Routes: `fetch_article_fulltext`
(Unpaywall no OA location; Semantic Scholar none; no PMCID; Crossref TDM none; landing page only);
OpenAlex confirms `oa_status: closed`, `any_repository_has_fulltext: false` (an edoc Basel record
exists but is flagged not-OA). Status: `[primary-abstract-only]`.

**8.3 Rosenfeld, Elowitz & Alon 2002, J Mol Biol.** DOI 10.1016/S0022-2836(02)00994-4,
PMID 12417193. Needed for: NAR response-time acceleration. Routes: `fetch_article_fulltext` (all
five routes failed); OpenAlex `oa_status: closed`. A CaltechAUTHORS submittedVersion record exists
but is flagged not-OA. Status: `[not-retrieved]`.

**8.4 Briat, Gupta & Khammash 2016 — published version of record.** The Cell Systems text is
`[not-retrieved]`; I read the arXiv preprint that the OA route returned. See §1.1 provenance caveat.
Everything I quote from it needs re-checking against the published version.

**8.5 Aoki-adjacent items not pursued to primary.** The CcdB growth-control *experimental* paper
cited by Olsman et al. (`[not-retrieved]`); "Stabilization of antithetic control via molecular
buffering" (*J R Soc Interface* 2022, PMC8905164) returned an empty full-text body from PMC; the
2026 Cell Systems sAIF redesign (Hu CY, DOI 10.1016/j.cels.2026.101565, PMID 41856043) is
`[primary-abstract-only]` and its abstract mentions split-intein implementation in E. coli with
effective PI behavior — a possible successor with a same-chassis I-vs-PI contrast, worth a follow-up
if the parent seat wants Pair A strengthened.

**8.6 Tooling notes.** The bioRxiv connector's `search_preprints` has **no keyword search** (date and
category only), so it could not be used to hunt an open version of a specific paper. OpenAlex direct
HTTP from the analysis kernel works with the injected key; the literature connector's own OpenAlex
methods returned `openalex_key_required` and were unusable this session.

---

## 9. What would change this assessment

- Reading Aoki et al. 2019 §on growth-rate control could move S.5 and the viability-relevance
  objection materially. It cannot rescue `target_is: PARAMETER` — that is settled by the equations
  in Briat and Filo — but it could establish an experimentally demonstrated set-point retuning range
  and a growth-rate (hence viability-adjacent) regulated variable.
- A perturb-and-recover experiment on a negative-autoregulation circuit would convert the negative
  control from "corrector by model structure" to "demonstrated corrector". Hu & Murray's cis/trans
  feedback constructs with their 2-hour perturbation and settling-time metric are the closest
  retrieved instance and may already suffice — that is a judgment for the parent seat.
