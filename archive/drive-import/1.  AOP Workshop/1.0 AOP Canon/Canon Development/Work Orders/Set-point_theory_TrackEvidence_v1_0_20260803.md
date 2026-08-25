# Set-point vs. settling-point: retrieval report (Gate 1, life-criterion arc)

**Track:** Is the stored-reference-versus-emergent-target distinction already in the peer-reviewed literature?
**Seat:** Claude Science (builder). This is a PROPOSAL for verification, not a verdict.
**Date:** 2026-08-02 · **File:** `Set-point_theory_retrieval_v1.md` · **Version:** v1

Retrieval tags used throughout: `[primary-verified]` (I read the passage in the primary),
`[primary-abstract-only]`, `[secondary]`, `[not-retrieved]`.

---

## 0. Headline answer

**Yes — the distinction AOP needs is already in the peer-reviewed literature, in at least three
independent fields, under three different names.** AOP should cite, not invent, the *distinction*.

| Field | Stored-reference term | Model-free / emergent term | Canonical primary |
|---|---|---|---|
| Body-weight physiology | set point | **settling point** | Wirtshafter & Davis 1977; Speakman et al. 2011 |
| Thermal physiology | set point / reference signal | **balance point** | Romanovsky 2006; Ramsay & Woods 2014 |
| Endocrinology (thyroid) | set point | **equilibrium point** | Fitzgerald, Bean & Fitzgerald 2017 |
| Control theory (formal) | internal model Σ_im | (absence thereof) | Sontag 2003 |

**However — and this is the finding that matters most for the arc — I could not find a published,
peer-reviewed OPERATIONAL DISCRIMINATOR of the kind AOP's separability test proposes: an
intervention that moves the stored reference while leaving the corrective machinery intact.** The
field states the distinction repeatedly and then says the discriminating experiments have not been
done. That gap is recorded precisely in §2.

---

## 1. Set point versus settling point — the definitional statements

### 1.1 Wirtshafter & Davis (1977) — the founding statement `[primary-abstract-only]`

Wirtshafter D, Davis JD. "Set points, settling points, and the control of body weight."
*Physiology & Behavior* 1977 Jul; PMID 11803695; DOI 10.1016/0031-9384(77)90162-7.
Bibliographic metadata verified against PubMed (authors, title, journal, year, DOI).

**Content status: ABSTRACT ONLY.** From the abstract, verified: they describe a feedback control
model containing "no set point" that nonetheless reproduces the lesion and defence data taken to
prove a set point exists, and conclude it is "unnecessary and unparsimonious to
introduce the concept of a neural set point" to explain defended body weight.

This is the cleanest historical statement of AOP's model-free corrector argued in physiology: a
system that *defends* a level without *storing* one. The full text is paywalled — see §5.

### 1.2 Speakman et al. (2011) — the fullest definitional treatment `[primary-verified]`

Speakman JR, Levitsky DA, Allison DB, Bray MS, de Castro JM, Clegg DJ, et al. "Set points, settling
points and some alternative models: theoretical options to understand how genes and environments
combine to regulate body adiposity." *Disease Models & Mechanisms* 2011 Nov;
DOI 10.1242/dmm.008698; PMC3209643. Full text read via PMC (PubMed/PMC).

Read and relied on:

- **Set point defined as a stored target with a comparator.** Kennedy's proposal is described as fat
  producing a signal sensed by the brain "where it was compared with a target level of body
  fatness", with any discrepancy driving intake/expenditure to close it. This is
  target-as-state: the target is an object the error signal is computed against.
- **Settling point defined as the equilibrium of opposing constitutive flows with no reference.**
  The reservoir/lake analogy: a reservoir with an input and an output settles wherever outflow
  matches inflow. The paper states the key negative claim explicitly — "There is no regulated
  level of the volume in this system, and yet it behaves as if this is a parameter that is being
  regulated."
- **The structural requirement of a settling-point system.** The paper states that the model
  requires *at least one* flow parameter that is independent of the reservoir level and *at least
  one* that varies with it. This is a testable structural signature, and it is the closest thing in
  this literature to a formal characterisation of the model-free corrector.
- **The observational-equivalence problem, stated by the authors.** After a diet-then-refeed cycle,
  a settling-point system returns to its original composition, and the paper says an outside
  observer "could be misinterpreted as the individual defending a level of adiposity" —
  i.e. the two architectures are **behaviourally indistinguishable from the trajectory alone.**
  This is precisely why AOP needs an *interventional* separability test rather than an
  observational one.
- **Set-point shift dissolves the concept.** The authors note that explaining obesity by a shifted
  set point "effectively negate[s] the utility of the set point concept" — if it moves with
  social class or marital status, it is not "set".
- **Dual intervention point model** — upper and lower boundaries with weak or no regulation between
  them; "there is no defined target" and the two intervention points are independently regulated.
  Verified in the primary. This is a third architecture, neither stored-reference nor pure settling.

### 1.3 Speakman & Hall (2023) — the current model taxonomy `[primary-abstract-only]`

Speakman JR, Hall KD. "Models of body weight and fatness regulation." *Phil Trans R Soc B* 2023 Sep 4;
DOI 10.1098/rstb.2022.0231; PMC10475878. PMC record retrieved but body text is not deposited — only
front matter and abstract were obtainable.

From the abstract, verified: seven models are now in play (set-point, dynamic equilibrium, adiposity
force, control-theory/settling-point, Hall–Guo, operation point, dual intervention point); the
dynamic-equilibrium model holds that apparent regulation around a reference "is an illusion";
and the review concludes that "further experiments to test between the models are sorely
required." **That closing sentence is a 2023 statement, by the field's leading authors, that the
discriminating experiment has not been done.**

### 1.4 Speakman (2017) — why a stored lipostat may not even be evolvable `[primary-verified]`

Speakman JR. "Why lipostatic set point systems are unlikely to evolve." *Molecular Metabolism* 2017;
DOI 10.1016/j.molmet.2017.10.007; PMC5784320. Full text read via PMC.

Relied on: the argument that variation in component parameters makes the fitness optimum too
variable for a narrow stored set point to be selected, and that selection *can* resolve the edges of
a flat-fitness zone but not points inside it — hence a dual-intervention-point architecture is the
more likely evolutionary outcome. Verified in the primary.

### 1.5 Cabanac (2006) — the defence of the stored reference `[primary-abstract-only]`

Cabanac M. "Adjustable set point: to honor Harold T. Hammel." *J Appl Physiol* 2006 Apr;
DOI 10.1152/japplphysiol.01021.2005; PMID 16540712. **Full text paywalled** (see §5).

The abstract is directly on AOP's question and states the dichotomy in almost AOP's own terms: the
set point "may be determined by an external signal to which the regulated variable is compared
or may be determined by the structural characteristics of the system itself." That second
disjunct is the settling point. Cabanac argues abandoning set point, fever and anapyrexia is
"premature, at best". `[primary-abstract-only]` — I did not read the arguments themselves.

---

## 2. Is there already a published operational discriminator?

**Finding: NO — not one of the form AOP needs.** What exists:

**(a) A published population-statistical discriminator, in thyroid endocrinology.** `[primary-verified]`
Fitzgerald SP, Bean NG, Fitzgerald LN. "Population data indicate that thyroid regulation is
consistent with an equilibrium-point model, but not with a set-point model." *Temperature (Austin)*
2017; DOI 10.1080/23328940.2017.1281370; PMC5489013. Full text read via PMC.

This is the most valuable single find for AOP's methods section, because it is a real, published,
*discriminating* test rather than a restatement of the dichotomy. The logic is a separability
argument executed statistically: under a set-point model the FT4 reference is "set externally to
thyroid gland physiology and thus is independent of the T4 curve" — so the population regression
of FT4 on TSH must have positive slope. The empirical population curve has negative slope. The
authors conclude the set-point model "cannot be valid" for FT4. They also state the equilibrium
alternative in exactly AOP's terms: "an equilibrium or balance model requires no reference
level", the level being the balance point of the processes acting on the parameter.

**The AOP-relevant structure here is the independence assumption**: a *stored* reference must be
statistically/causally independent of the constitutive gain curve; an *emergent* target cannot be.
That is a weaker but genuinely published cousin of AOP's separability test. It is observational, not
interventional, and it needs population variation — so it does not substitute for AOP's test, but
AOP can cite it as prior art for the underlying logic.

**(b) Romanovsky's threshold-dissociation test, in thermal physiology.** `[primary-abstract-only]`
Romanovsky AA. "Do fever and anapyrexia exist? Analysis of set point-based definitions."
*Am J Physiol Regul Integr Comp Physiol* 2004; DOI 10.1152/ajpregu.00068.2004; PMID 15191900.
**Paywalled** (see §5). From the abstract, verified: two tests are applied to set-point-based
definitions — (1) compatibility of measured *thermoeffector threshold shifts* with a single set-point
increase, and (2) the *T_b-versus-T_a dependence* test (a defended variable should be independent of
ambient temperature). Result per abstract: threshold changes are compatible with a set-point increase
in *some but not all* cases of fever; the febrile T_b "is defended in some (but not all)
cases"; and anapyrexia is incompatible with a single-set-point decrease. **This is an operational
discriminator, and applied to fever it returns a partial/mixed verdict.**

**(c) A formal control-theoretic criterion.** `[primary-verified]`
Sontag ED. "Adaptation and regulation with signal detection implies internal model."
*Systems and Control Letters* (arXiv q-bio/0309003, 2003-09-16). arXiv PDF read directly.
Relied on: the theorem statement that if Σ adapts to a class U of external signals then "Σ must
necessarily contain a subsystem which is capable of generating all the signals in U", and — the
part AOP should note — that the internal-model subsystem Σ_im must receive *only* y as its external
input, "receiving no other direct information from other parts of the system nor the input
signal u."

**This is directly load-bearing for the Reading A / Reading B adjudication and I flag it for prime.**
Sontag's IMP says the reference-generating subsystem is driven by the regulation error y and by
nothing else — which is *integral feedback*, i.e. Reading B, not Reading A. A theorem in the
formal literature therefore says that a corrector which adapts to a class of disturbances must
contain an error-driven internal model. If AOP's Reading A (STRICT: ẋ = f(x), no dependence on y)
is adopted, AOP is excluding the architecture the IMP identifies as necessary for adaptation.
That is a substantive tension, not a wording issue. **I do not adjudicate it; I record it.**

**(d) What does NOT exist, as far as I could retrieve.** No paper I found publishes a criterion of
the form *"perturb the putative reference without disabling the corrector; if the system regulates
competently toward the new value, the reference is stored."* Searches run: PubMed for operational/
experimental discriminators of regulated-vs-settled variables (multiple phrasings, all returning 0
hits); arXiv for internal-model-principle applications to biology; OpenAlex unavailable (§5).
The 2023 Speakman & Hall abstract and the 2025 Nature Reviews Endocrinology review
(Bosy-Westphal et al., DOI 10.1038/s41574-025-01149-1, `[primary-abstract-only]`, paywalled) both
state that the validity-testing experiments *remain to be designed* — the 2025 abstract explicitly
closes by discussing "the design of proof-of-concept experiments" for exactly this purpose.

**AOP's honest position: the distinction is settled prior art and must be cited; the interventional
separability test appears to be genuinely unclaimed.** Given this project's standing rule to be
sceptical of anything that looks new, I flag that (a) and (b) above are close enough that prime
should read Romanovsky 2004 and Fitzgerald 2017 in full before AOP claims novelty for the test.

---

## 3. Candidate #3 — hypothalamic thermoregulation and fever

### 3.1 What the primary literature actually establishes

`[primary-verified]` Morrison SF, Nakamura K. "Central neural pathways for thermoregulation."
*Front Biosci (Landmark)* 2011; DOI 10.2741/3677; PMC3051412. Full text read via PMC.

Verified from the primary:
- PGE2 acts in the preoptic area; the POA is the sole region that can sense E-series PGs to produce
  fever; responsive sites refined by nanoinjection to MPO and MnPO.
- Only EP3-receptor-deficient mice completely fail to show a febrile response to PGE2, IL-1β or
  endotoxin; EP1-deficient mice show partial attenuation.
- Mechanism: EP3-expressing POA neurons "normally maintain a tonic GABAergic inhibition of
  thermogenic neurons" in DMH/rRPa; PGE2 attenuates their tonic firing via reduced cAMP,
  disinhibiting downstream thermogenic circuits.
- Fever is described as "a defended elevation in body temperature".
- **Critically, this same primary declines to endorse a unitary set point.** It refers instead to
  the firing rates of warm-sensitive MPO projection neurons as "potentially a major contribution
  to the neurophysiological substrate underlying the thermoregulatory 'balance point'" — i.e.
  Morrison & Nakamura themselves use *balance point*, not *set point*.

Supporting circuit primaries, metadata verified and abstracts read:
- Nakamura K et al., *J Neurosci* 2002, DOI 10.1523/JNEUROSCI.22-11-04600.2002 (rRPa mediates
  pyrogenic transmission from POA). `[primary-abstract-only]` — the PMC "full text" record returned
  only front matter and abstract.
- Nakamura Y et al., *Eur J Neurosci* 2005, DOI 10.1111/j.1460-9568.2005.04515.x (direct EP3⁺ POA →
  DMH pyrogenic projection; muscimol into DMH/DH blocks the response to intra-POA PGE2).
  `[primary-abstract-only]` — same limitation.
- Lazarus M et al., *Nat Neurosci* 2007, DOI 10.1038/nn1949 (selective genetic deletion of EP3R in
  MnPO abrogates fever). `[primary-abstract-only]`, paywalled (§5).

### 3.2 The field disputes whether a stored set point exists here — critical for AOP

`[primary-abstract-only]` Romanovsky AA. "Thermoregulation: some concepts have changed. Functional
architecture of the thermoregulatory system." *Am J Physiol Regul Integr Comp Physiol* 2006;
DOI 10.1152/ajpregu.00668.2006; PMID 17008453. **Paywalled** (§5). From the abstract, verified: the
notion that deep T_b is regulated by a unified system with a single controller is *rejected*;
T_b is proposed to be regulated by independent thermoeffector loops each with its own afferent and
efferent branch; "No computation of an integrated T_b or its comparison with an obvious or
hidden set point of a unified system is necessary"; and the term **balance point** is proposed to
replace set point.

`[primary-verified]` Ramsay DS, Woods SC. "Clarifying the roles of homeostasis and allostasis in
physiological regulation." *Psychological Review* 2014; DOI 10.1037/a0035942; PMC4166604.
Full text read via PMC. This is the most explicit statement I found of the *architectural* claim:
body temperature is the consequence of multiple independent thermoeffector loops each with its own
activation threshold, "for which there is no central integrator that coordinates effector
activity"; the resulting level "reflects not a set point and rather a balancing or settling
point"; and the pattern of effector activity appears purposefully coordinated but occurs
"without using a comparator to evaluate the regulated value relative to a set point value".
They also flag the cost of the balance-point view: knowing the balance point moved is
"uninformative about underlying effector activity", and fever and passive heat exposure both raise
it — so the term alone does not distinguish them.

`[primary-verified]` Ramsay DS, Woods SC, Kaiyala KJ. *Temperature (Austin)* 2014;
DOI 10.4161/23328940.2014.944802; PMC4415621. Full text read via PMC. Empirical demonstration that
autonomic and behavioural thermoeffectors can act in *opposition* under nitrous-oxide challenge:
heat production rises while the animal simultaneously selects cooler ambient temperature. They
conclude the observed T_c "reflect[s] a balance point rather than a defended set-point."
**This is a published experimental result that a purported stored thermoregulatory reference
fails a coordination test.**

`[primary-verified]` Jänig W. "Thermosensors or not, this is the question." *Temperature (Austin)*
2015; DOI 10.1080/23328940.2015.1054553; PMC4843906. Full text read via PMC. Quotes Hensel on the
epistemics AOP should note: "In contrast to a technical control system, where the set point is
known by the control engineer, the set point of a living control system must indirectly be
assessed", and that the thermoregulatory system "has no single controlled variable and a high
redundancy". Also documents the Kobayashi position that peripheral thermoreceptors are themselves
*thermostats*, each with its own set point — a *distributed* reference, a third architecture.

### 3.3 Scoring — thermoregulation/fever

- **S.1 (dynamical description + performable interventions): PARTIAL.** Interventions are excellent
  and real: intra-POA PGE2 nanoinjection, EP3R genetic deletion (global and MnPO-selective),
  muscimol into DMH/rRPa. But what the primaries supply is a *circuit diagram with pharmacological
  perturbation*, not a quantitative dynamical model with a written slow variable and state
  equations. Morrison & Nakamura 2011 contains no set of ODEs and no declared timescales. Prime's
  expectation of failure is **confirmed as to the dynamical model**, refuted as to interventions.
- **S.2 (candidate stored reference): FAIL under Reading A, PARTIAL under Reading B.** No
  identifiable slow state variable stores the target. The best candidate — tonic firing rate of
  EP3⁺ warm-sensitive POA neurons — is called by the primaries a contributor to a *balance point*,
  and Romanovsky 2006 and Ramsay & Woods 2014 explicitly deny that any integrated reference exists.
  A federated-effector architecture has no stored reference to move.
- **S.3 (independent perturbability): PARTIAL, but the wrong shape.** PGE2 does move the operating
  point reversibly with the machinery intact — which is the P1 phenomenology. But it does so by
  *disinhibiting an effector loop*, not by rewriting a stored value; and the same manoeuvre would be
  described by Romanovsky as shifting individual effector thresholds. The intervention cannot
  distinguish the two architectures, which is exactly the ambiguity AOP is trying to escape.
- **S.4 (slow/fast ratio tunable over ≥2 decades): FAIL.** No declared slow/fast decomposition exists
  in the retrieved primaries, so there is nothing to tune. Prime's expectation is **confirmed**.
- **S.5 (lifetime readout + matched comparison): WEAK.** Fever-survival literature exists but no
  matched architecture-only comparison class was retrieved on this track.

**Assessment: fever is the most vivid *illustration* of P1 in biology and the worst possible
*test article* for it, because the field itself disputes whether the thing being shifted is a
stored reference. Using it would make AOP's central distinction hostage to an unresolved
physiology controversy.** I recommend prime read it as a motivating case in the canon, not as a
Gate-1 candidate.

---

## 4. Candidate #2 — *E. coli* σ32 heat-shock response

### 4.1 The quantitative model literature

`[primary-verified]` El-Samad H, Kurata H, Doyle JC, Gross CA, Khammash M. "Surviving heat shock:
control strategies for robustness and performance." *PNAS* 2005;102(8):2736–2741;
DOI 10.1073/pnas.0403510102. Full text read (PDF via Europe PMC/Semantic Scholar).

`[primary-verified]` Kurata H, El-Samad H, Iwasaki R, Ohtake H, Doyle JC, Grigorova I, et al.
"Module-based analysis of robustness tradeoffs in the heat shock response system."
*PLoS Comput Biol* 2006; DOI 10.1371/journal.pcbi.0020059; PMC1523291. Full text read via PMC.

`[primary-verified]` Guisbert E, Yura T, Rhodius VA, Gross CA. "Convergence of molecular, modeling,
and systems approaches for an understanding of the *E. coli* heat shock response."
*Microbiol Mol Biol Rev* 2008; DOI 10.1128/MMBR.00007-08. Full text read (PDF).

### 4.2 The state-versus-parameter determination — this is the decisive result

**Determination: the σ32 temperature target is a PARAMETER, not a stored state. The heat-shock
system is a settling-point / model-free corrector with respect to temperature.**

Evidence, all `[primary-verified]`:

1. **The authors of the canonical model say so in the primary, in the field's own words.**
   El-Samad et al. 2005, discussing the feedforward mutant's altered steady state, write that the
   lower σ32 level is "the result of a new setpoint dictated by the balance between σ32 lower
   synthesis rate at high temperature and its degradation rate." A "setpoint dictated by the
   balance" between two rate constants **is a settling point in Speakman's exact sense** — the
   equilibrium of opposing constitutive flows. It is not a stored value; it is where the kinetics sit.
   The only other use of "set point" in that paper is the thermostat *analogy* for a house.

2. **The sensing mechanism is titration, and titration has no stored referent.** Guisbert et al.
   2008: under the unfolded-protein titration model, σ32 "is not responding to the total level of
   chaperones in the cell but rather is responding to the ratio of chaperone relative to those of its
   unfolded protein substrates." A ratio at which binding balances is a kinetic zero, not a state.
   Kurata et al. 2006 formalises this as a SEQ-FB (sequestration feedback) flux module whose function
   is regulating σ32 *activity*; the word "set point" does not occur anywhere in that paper.

3. **There is no comparator and no reference-generating subsystem.** The Kurata modular
   decomposition names FF (feedforward), SEQ-FB, DEG-FB and amplifier flux modules. No module stores
   a target. The feedforward loop is explicitly a *dynamic sensor* (direct temperature control of
   σ32 translation rate), not a reference.

4. **Moving the "target" means changing a rate law, which is also how you break the machinery.**
   To move where the system settles you must alter σ32 synthesis rate, its FtsH-mediated degradation
   rate, chaperone binding affinity, or chaperone abundance — each of which is a component of the
   corrector itself. This is the target-as-parameter failure mode exactly as the brief defines it:
   S.3's "move the set-point without disabling the machinery" has **no available operation**.

**Independent confirmation that perturbations here only DEGRADE, never redirect** `[primary-abstract-only]`:
- rpoH null (σ32 deleted): Zhou YN, Kusukawa N, Erickson JW, Gross CA, Yura T, *J Bacteriol*
  1988;170(8):3640–3649; DOI 10.1128/jb.170.8.3640-3649.1988. Abstract verified: strains lacking
  σ32 are "extremely temperature sensitive and grow only at temperatures less than or equal to
  20 degrees C." That is destruction of the corrector, not misregulation toward a wrong target.
- ΔdnaK52: Bukau B, Walker GC, *J Bacteriol* 1989;171(5):2337–2346;
  DOI 10.1128/jb.171.5.2337-2346.1989. Abstract verified: severe division defects, slow growth, poor
  viability at 30 °C; both cold- and temperature-sensitive. Again degradation, not redirection.

**This is the P1 signature of a model-free corrector.** It is the same signature AOP attributes to
its canonical star.

### 4.3 Scoring — σ32 heat-shock response

- **S.1: PASS.** Genuine quantitative ODE models exist (Kurata 2006 gives the full mechanistic
  equation set; El-Samad 2005 the modular control analysis), and the intervention class is rich and
  physically performable: gene deletion (rpoH, ftsH, dnaK, groEL), chaperone over- and
  under-expression, feedforward-disabling point mutants, controlled temperature upshift/downshift.
- **S.2: FAIL.** No slow variable stores a target. σ32 itself is the *fastest* component
  (half-life ~1 min at 30 °C, ~20 s at 42 °C — Guisbert 2008, `[primary-verified]`), and its level
  is the *output* of the balance, not a reference for it. The closest slow object is chaperone
  abundance, which is a fast-driven effector pool, not a stored set.
- **S.3: FAIL.** No published operation moves the settling temperature without touching the
  corrector's own kinetics. Every retrieved perturbation degrades.
- **S.4: PARTIAL, and better than expected.** The system has a genuine, published, *measured*
  timescale hierarchy that an experiment could tune: σ32 degradation t½ ≈ 20 s–1 min; transient
  stabilisation window 5–10 min after upshift; long-term chaperone-overexpression adaptation over
  ~20 h with σ32 activity returning to near wild-type (Guisbert 2008, `[primary-verified]`) — that
  span alone is ~3 orders of magnitude. FtsH deletion renders σ32 "almost completely stable",
  an unbounded slowing of the degradation arm. So the ratio IS tunable over ≥2 decades. But it is
  a slow/fast ratio *between corrector components*, not between a stored reference and a regulated
  variable — because there is no stored reference. **Score PARTIAL, with the caveat that satisfying
  S.4 here does not help, since S.2 fails.**
- **S.5: STRONG — the best on this track.** Survival at elevated temperature is a real
  first-passage-style observable with published matched comparison classes: wild-type vs rpoH-null
  (grows only ≤20 °C), vs ΔdnaK, vs feedforward-disabled point mutants (El-Samad 2005 §"Feedforward:
  A Dynamic Sensor"), vs regulated-vs-constitutive degradation variants. Prime's read is confirmed.

**Reassignment recommendation: σ32 heat shock is a NEGATIVE CONTROL, and a good one.** It
demonstrably corrects — robustly, with feedback and feedforward, with a published control-theoretic
analysis — and it is demonstrably model-free with respect to its temperature target, on the
authors' own words. It carries the strongest lifetime readout of anything I retrieved. That is
precisely the matched negative control the pair needs.

---

## 5. Blocked-retrieval ledger

Every item below is `[not-retrieved]` or `[primary-abstract-only]` for content. Routes attempted are
listed in full. No mirrors, archive sites, proxies or user-agent spoofing were used.

| Source | Routes attempted | Result | Why it mattered |
|---|---|---|---|
| Wirtshafter & Davis 1977, *Physiol Behav*, DOI 10.1016/0031-9384(77)90162-7 | `fetch_article_fulltext` (Unpaywall → no OA location; Semantic Scholar → no OA PDF; PMC → no PMCID; CrossRef TDM → no accessible content; DOI resolve → landing page, HTML only) | Abstract only | The founding statement of the settling-point account; AOP's most direct historical citation |
| Romanovsky 2006, *AJP-RICP*, DOI 10.1152/ajpregu.00668.2006 | `fetch_article_fulltext` (Unpaywall no OA; Semantic Scholar no OA PDF; PMC no PMCID; CrossRef TDM none; DOI resolve **HTTP 403**) | Abstract only | The primary rejection of a unified thermoregulatory set point — directly decides whether candidate #3 has a stored reference |
| Romanovsky 2004, *AJP-RICP*, DOI 10.1152/ajpregu.00068.2004 | same five routes; DOI resolve **HTTP 403** | Abstract only | Contains the two operational discriminators (threshold dissociation; T_b-vs-T_a dependence) — the closest published thing to AOP's test |
| Cabanac 2006, *J Appl Physiol*, DOI 10.1152/japplphysiol.01021.2005 | same five routes; DOI resolve **HTTP 403** | Abstract only | The defence of the stored reference; the abstract already states AOP's dichotomy verbatim |
| Lazarus et al. 2007, *Nat Neurosci*, DOI 10.1038/nn1949 | Unpaywall no OA; Semantic Scholar returned HTML not PDF; PMC no PMCID; CrossRef TDM none; DOI resolve landing page only | Abstract only | The cleanest causal demonstration that MnPO EP3R is required for fever |
| Bosy-Westphal et al. 2025, *Nat Rev Endocrinol*, DOI 10.1038/s41574-025-01149-1 | all five routes; closed | Abstract only | Its stated purpose is designing the proof-of-concept experiments to discriminate the models — highest-value unread source on this track |
| Speakman & Hall 2023, *Phil Trans R Soc B*, DOI 10.1098/rstb.2022.0231 | PMC record retrieved but body text not deposited (front matter + abstract only) | Abstract only | Current authoritative taxonomy of the seven models |
| Nakamura K et al. 2002 (*J Neurosci*), Nakamura Y et al. 2005 (*Eur J Neurosci*) | PMC full-text records return front matter/abstract only; `fetch_article_fulltext` reached PMC text of the same limited scope | Abstract only | Circuit-level detail of the pyrogenic pathway |
| Zhou et al. 1988; Bukau & Walker 1989 (*J Bacteriol*) | PMC full text returned 0 characters (scanned legacy issues) | Abstract only | The rpoH-null and ΔdnaK degradation phenotypes |
| Sontag, *Systems and Control Letters* 2003 published version, DOI 10.1016/S0167-6911(03)00136-1 | Unpaywall no OA; Semantic Scholar http-only URL rejected; PMC no PMCID; DOI resolve landing page | **Substituted the author's own arXiv preprint q-bio/0309003v1, read in full.** Stated explicitly as a preprint substitution; the arXiv comment line confirms "to appear in Systems and Control Letters" | The internal-model theorem bearing on Reading A vs Reading B |
| **OpenAlex (all queries)** | `host.credentials.request("openalex")` invoked; a credential named "OpenAlex" is registered but every call returned `openalex_key_required`; waited and retried once | **Tool unavailable this session** | Citation-graph search for prior art on the discriminator; PubMed + arXiv were used as substitutes, so coverage of non-biomedical statements of the distinction (economics, engineering, ecology) is likely incomplete |
| bioRxiv connector | called with an unsupported argument; schema mismatch | Not retried — PMC/arXiv coverage was sufficient for this track | Preprint versions of paywalled items |

---

## 6. Eligibility under both readings, and the target determination

Scored for the two candidates this track examined. **I do not select and I do not pair.**

### σ32 heat-shock response
- **Reading A (STRICT / autonomy): NO.** There is no slow coordinate set closed in itself. Every
  candidate slow variable (chaperone pool, σ32 level) is driven by the regulated quantity (unfolded
  protein load). The architecture is pure feedback with a feedforward sensor.
- **Reading B (LOOSE / scale separation): UNCLEAR, leaning NO.** A declared timescale separation
  does exist and is measured. But Reading B still requires the slow variable to *set y's operating
  point* and be *separately addressable*. Here the operating point is set by the ratio of rate
  constants, and no addressing operation exists that does not also alter the corrector. It fails
  Reading B on the separate-addressability clause rather than on the feedback clause.
- **target_is: PARAMETER.** On the modelling authors' own words — a setpoint "dictated by the
  balance" between synthesis and degradation rates.

### Hypothalamic thermoregulation / fever
- **Reading A: NO.** No autonomous slow reference coordinate appears in any retrieved primary; the
  leading reviews deny a unified reference exists at all.
- **Reading B: UNCLEAR.** PGE2 is a separately addressable input that reversibly moves the operating
  point with machinery intact — the strongest Reading-B-shaped evidence on this track. But it moves
  effector thresholds, and the field disputes whether anything is being *stored*. Cannot be resolved
  from the retrieved literature; the two sources that would resolve it (Romanovsky 2004, 2006) are
  paywalled.
- **target_is: UNDETERMINED.** No published dynamical model with explicit equations was retrieved
  for this system, so the state-versus-parameter test cannot be run against equations. Honest gap.

---

## 7. Surprises worth prime's attention

1. **The strongest source in this whole track is the σ32 modelling paper describing its own system's
   steady state as a "setpoint dictated by the balance" of two rate constants.** That is a
   peer-reviewed, quantitative-modelling group in systems biology independently articulating the
   settling-point concept and applying it to their own system. AOP's distinction is confirmed prior
   art in a field entirely separate from physiology.
2. **The distinction has four independent names in four fields** (settling point, balance point,
   equilibrium point, and — formally — absence of an internal model). AOP should say so; it
   strengthens rather than weakens the framework.
3. **Sontag's internal-model theorem cuts against Reading A.** A published theorem states that
   adaptation to a class of disturbances *requires* an error-driven internal-model subsystem —
   which is Reading B's integral feedback, the very architecture Reading A excludes. If AOP adopts
   Reading A it must say why the IMP's Σ_im does not count as a stored reference. This is a
   theoretical objection prime should have an answer to before Gate 2.
4. **Fever is a bad test article for the reason nobody expects.** Not because the experiment is
   hard, but because the field has an active, unresolved dispute over whether the object being
   shifted exists. AOP would be borrowing a controversy.
5. **Speakman et al. 2011 anticipates AOP's own methodological problem** — that a settling-point
   system's return to baseline "could be misinterpreted as the individual defending a level". The
   observational trajectory does not discriminate. Only intervention does. AOP's separability test
   is the right *shape* of answer to a problem the physiology literature has stated and not solved.
