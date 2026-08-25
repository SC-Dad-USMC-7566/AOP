# Chemotaxis_retrieval_v1

**Track:** *E. coli* chemotactic adaptation via receptor methylation
**Seat:** Claude Science (BUILDER). This is a **proposal**, not a verdict. Not self-verified.
**Arc:** AOP Gate 1, life-criterion falsification. Retrieval track only — no selection, no pairing,
no pre-registration, no AOP quantity computed.
**Date:** 2026-08-02

---

## 0. Retrieval-status legend

`[primary-verified]` = I read the passage in the primary and quote/cite it below.
`[primary-abstract-only]` = abstract read; body not retrieved.
`[secondary]` = another paper reports it.
`[not-retrieved]` = citation only.

Bibliographic metadata is verified separately from content and stated separately.

---

## 1. Headline for prime — read this first

Prime's lead-candidate note flagged that every claim about this system was unverified
recollection. Three corrections, in descending order of consequence:

**(a) Prime's S.3 worry is half right, and the half that is wrong matters.** The celebrated
robustness result is about the **precision** of adaptation (that activity returns *exactly* to its
prestimulus value), **not** about the adapted **level**. The adapted level is *not* invariant to
CheR/CheB expression — it demonstrably moves. So S.3 is satisfiable. Alon et al. 1999's own
abstract separates the two properties explicitly, and Clausznitzer et al. 2010 moved the adapted
activity from A≈1/3 to A≈1/2 by halving CheB expression, machinery intact, exact adaptation
preserved. That is a demonstrated **competent-misregulation-shaped** operation.

**(b) But the target is a PARAMETER, not a state, and this is provable from the equations, not
inferred.** Yi et al. 2000's Eq. 1 gives the adapted activity in closed form as a function of
*only* CheR/CheB concentrations and their kinetic constants. The methylation level `m` — the slow
variable — appears **nowhere** in the expression for the adapted activity. `m` is the *integrator
state*, free to run to whatever value cancels the ligand free energy; it does not store the target.
The target is the **zero of the integrator's rate law**, set by the ratio of methylation to
demethylation kinetics. This is exactly the `target-as-parameter` horn the brief names as
threatening S.2 and S.3.

**(c) Reading A is cleanly, structurally excluded.** Not "unclear" — excluded by the published
model equations. The slow variable's rate law is a function of the regulated variable.

Net: the system passes S.1/S.3/S.4-partial and **fails the sharp S.2 filter**. Under Reading B it is
eligible; under Reading A it is not. Full reasoning below.

---

## 2. The integral-feedback formulation

### 2.1 Yi, Huang, Simon & Doyle 2000 — `[primary-verified]`

**Citation (metadata verified via Crossref DOI resolution + PubMed record PMID 10781070):**
Yi TM, Huang Y, Simon MI, Doyle J. "Robust perfect adaptation in bacterial chemotaxis through
integral feedback control." *PNAS* 97(9):4649–4653, 25 April 2000. DOI 10.1073/pnas.97.9.4649.
PMCID PMC18287.
**Retrieved:** full PDF via Europe PMC (green OA), text layer extracted, read.

**What the paper actually establishes.** Rearranging the Barkai–Leibler equations, they derive
(their Eq. 1) a closed-form steady-state activity

> A_st = γ·R_bnd·K_b / (B_tot − γ·R_bnd)

where R_bnd is CheR bound to receptor complex, K_b the Michaelis constant for CheB,
B_tot total CheB, and **γ = k_r/k_b the ratio of the turnover numbers for CheR and CheB**.
The paper states in its own words that <25 words: "The expression for Ast depends only on the
concentrations and kinetic rate constants of CheR and CheB." `[primary-verified]`

With CheR saturated (R_bnd ≈ R_tot) this reduces to A_st = K_b·V_max^R / (V_max^B − V_max^R),
which they attribute to Barkai & Leibler. `[primary-verified]`

**The simplified integral form.** They define `z` approximating total receptor methylation and give
`ż = r − b·A`, so at steady state `A → r/b`. `[primary-verified]` The error signal is `r − bA`
and its integral, `z` (methylation), is fed back because activity is a function of methylation.

**The block diagram (their Fig. 2 caption).** In the Barkai–Leibler mapping, chemoattractant is the
input, receptor activity the output, `ẋ = y` (y = output error), and **−x approximates the
methylation level of the receptors**. `[primary-verified]` So methylation *is* the integrator state
by the authors' own identification.

**Four necessary assumptions** (their list, needed to derive integral control): (i) CheB
demethylates only active receptors; (ii) CheR/CheB turnover numbers independent of methylation
state and ligand occupancy, with the ratio k_r(m)/k_b(m+1) = γ constant across methylation states;
(iii) unmethylated receptor activity negligible; (iv) bound CheR independent of ligand level.
Relaxing any one produces deviation from exact adaptation. `[primary-verified]`

They further quantify the sensitivity: setting CheB's association rate with *inactive* receptor
equal to its rate with active receptor drops adaptation precision P to 0.22 (P=1 is perfect);
at 1/100 of that rate, P = 0.93. `[primary-verified]`

### 2.2 Shimizu, Tu & Berg 2010 — `[primary-verified]`

**Citation (verified via PMC record):** Shimizu TS, Tu Y, Berg HC. "A modular gradient-sensing
network for chemotaxis in *Escherichia coli* revealed by responses to time-varying stimuli."
*Molecular Systems Biology* 6:382, 22 June 2010. DOI 10.1038/msb.2010.37. PMCID PMC2913400.
CC BY-NC-SA. **Retrieved:** full text via PMC, read.

Two-equation modular model, in their notation:
- **Eq. 1 (adaptation module, slow):** `dm/dt = F(a)` — methylation level `m` driven by kinase
  activity `a`.
- **Eq. 2 (receptor module, fast, algebraic):** `a = G([L], m)` — MWC allosteric form.

They state that the integral sign before F signifies integral feedback, "which is a direct
consequence of equation (1)": since F defines m's rate of change, m is the time integral of F.
`[primary-verified]`

They also state the sense of the coupling explicitly: increased `a` up-regulates CheB (which removes
methyls) and down-regulates CheR, so <25 words: "the sense of the feedback is negative, tending to
restore a toward its steady-state value". `[primary-verified]`

**This is the Reading-A killer, in the primary's own equations:** `ṁ = F(a)`, and `a` is the
regulated variable. The slow coordinate is not closed in itself.

---

## 3. What the slow variable actually is

**Slow variable = receptor methylation level `m`** — defined by Shimizu et al. as the average number
of methylated glutamyl residues per receptor monomer; for Tar there are four modification sites, so
max(m) = 4 per monomer. `[primary-verified]`

**Is it driven by the regulation error?** Yes, unambiguously, in every formulation retrieved:
- Yi et al.: `ż = r − bA`, with `r − bA` explicitly named "the normalized output or error of the
  system". `[primary-verified]`
- Shimizu et al.: `dm/dt = F(a)`, F measured empirically. `[primary-verified]`
- Clausznitzer et al. 2010: `dm/dt = γ_R(1−A) − γ_B·A` in their precise-adaptation model — again a
  function of activity only. `[primary-verified]`

**Is there any formulation in which methylation is autonomous?** I found none, and I looked. All
five model classes compared by Clausznitzer et al. make the methylation and demethylation rates
functions of receptor activity; that activity-dependence is stated there to be "believed to be a
requirement for robust precise adaptation." `[primary-verified]` An autonomous ṁ = f(m) would break
exact adaptation by construction, because nothing would then cancel the ligand free energy.

**Verdict:** methylation is an error-driven integrator. There is no autonomous formulation in the
retrieved literature.

---

## 4. Where the target lives — STATE or PARAMETER (the decisive S.2 question)

**Determination: PARAMETER.** From the equations, not from inference.

The argument, entirely from `[primary-verified]` sources:

1. Yi et al. Eq. 1 expresses the adapted activity A_st purely in terms of CheR/CheB concentrations
   and kinetic constants (γ = k_r/k_b, K_b, B_tot, R_bnd). **The methylation level does not appear.**
2. The simplified form `A → r/b` at steady state makes the same point in one line: the target is the
   *ratio* of the methylation rate to the demethylation rate constant.
3. The brief asked specifically whether the literature says the adapted level is set by the ratio of
   demethylation to methylation kinetics. **It does, in closed form, and that ratio is a kinetic
   parameter — γ = k_r/k_b — not a state variable.**
4. Clausznitzer et al. confirm this operationally in how they *fit* their model: <25 words — "The
   demethylation rate γB was determined to produce the adapted activity A≈1/3." `[primary-verified]`
   The adapted activity is an *output* of choosing a rate constant, not a stored value read out.
   Their fitted values: γ_R = 0.0019 s⁻¹, γ_B = 0.030 s⁻¹ for WT1.
5. The methylation level `m` is what the integrator *does*, not what it *stores*. Under a sustained
   ligand step, m runs to whatever value makes the methylation free-energy term cancel the ligand
   free-energy term (Shimizu et al.: `f_m(t) = −α·F(a)·t` balancing `f_L(t) = rt`). Its value is
   determined by the environment, not by the cell's target. A "stored set-point" ought to be
   invariant under a change of ambient ligand; m is precisely the thing that is *not*.

**The strongest counter-consideration, stated fairly.** One could argue the target is *both*: γ is a
parameter, but it is instantiated physically as a ratio of two protein concentrations
(V_R/V_B ∝ [CheR]k_cat^R / [CheB]k_cat^B), and protein concentration is a slow state variable of the
cell. Under that reading the "stored reference" is the CheR:CheB stoichiometry, which is slow
(expression-timescale), addressable (inducible promoters), and load-bearing. I record this as the
live counter-argument but do not endorse it, for two reasons: (i) it is not the variable any of these
papers calls the adaptation module's state — that is `m`; and (ii) the CheR:CheB ratio is *identically*
the regulatory machinery, so an intervention on it is not separable from an intervention on the
corrector, which is exactly what S.3 asks to separate. Prime should adjudicate.

**Answer to the schema field: `PARAMETER`.**

---

## 5. S.3 — perturbations that move the set-point with machinery intact

This is where prime's note needed correcting in both directions.

### 5.1 What is robust is PRECISION, not the LEVEL

**Alon, Surette, Barkai & Leibler 1999** — `[primary-abstract-only]`.
**Citation (metadata verified via OpenAlex + PubMed PMID 9923680):** Alon U, Surette MG, Barkai N,
Leibler S. "Robustness in bacterial chemotaxis." *Nature* 397(6715):168–171, 14 Jan 1999.
DOI 10.1038/16483. **Body not retrieved — paywalled (see ledger §8).**

From the abstract, which distinguishes the two properties directly: they report that some properties
— steady-state behaviour and adaptation time — "show strong variations in response to varying protein
concentrations," while <25 words: "the precision of adaptation is robust and does not vary with the
protein concentrations." `[primary-abstract-only]`

**Read that carefully.** Precision = the ratio of post-adaptation activity to prestimulus activity
(≈1). Steady-state behaviour = the prestimulus activity level itself. The celebrated invariant is the
*former*. The *latter* moves. Prime's worry ("the adapted level is ROBUST to those expression
changes") conflates the two; the paper's own abstract separates them.

I could not read the body, so I cannot report the magnitude of the CheR expression range they swept
or the numerical spread of steady-state behaviour. **Logged as a gap.** In particular I explicitly
did **not** import the commonly-recited "50-fold CheR overexpression" figure: the only 50-fold in any
primary I read is Yi et al.'s report of ~50-fold variation in *methylation rates from site to site*
on the Tar receptor (a different quantity entirely). Do not let that number migrate.

### 5.2 The operation that DOES move the set-point, verified in a primary

**Clausznitzer, Oleksiuk, Løvdok, Sourjik & Endres 2010** — `[primary-verified]`.
**Citation (metadata verified via PMC + Crossref):** Clausznitzer D, Oleksiuk O, Løvdok L, Sourjik V,
Endres RG. "Chemotactic response and adaptation dynamics in *Escherichia coli*." *PLoS Computational
Biology* 6(5):e1000784, 20 May 2010. DOI 10.1371/journal.pcbi.1000784. PMCID PMC2873904.
**Retrieved:** full text (PMC) + publisher PDF (gold OA); PDF text layer read for the numeric values
that the PMC text rendering dropped.

They made the prediction and then tested it experimentally:

- **Prediction:** raising the steady-state activity from A≈1/3 to 1/2 shifts the adaptation data
  collapse, and such an increase "can be achieved by decreasing CheB expression level, corresponding
  to a decreasing demethylation rate, at constant CheR expression level." `[primary-verified]`
- **Construction:** strain WT2 = VS124 Δ(cheB cheY cheZ) with wild-type CheB under an arabinose-
  inducible pBAD promoter; all other chemotaxis proteins as in WT1. CheB protein level by Western
  blot ≈ **0.5-fold** the native level. `[primary-verified]`
- **Result:** <25 words — "The steady-state activity was estimated to be A≈1/2 (compared to 1/3 in
  WT1)." The measured data collapse for WT2 matched the curve predicted for A≈1/2.
  `[primary-verified]`

**This is an S.3-satisfying operation.** A ~2-fold change in a single protein's expression level
moved the adapted activity set-point by ~50%, while the regulatory machinery remained fully
functional — WT2 still adapts, and still adapts *precisely*, to the new level. In P1's vocabulary,
the system regulates competently toward a different target. What is being changed, however, is a
kinetic parameter (the demethylation rate), which is the `target-as-parameter` case.

**A second, sharper variant in the same paper.** They also built a **CheB^D56E** point mutant —
non-phosphorylatable at the CheB phosphorylation site, retaining "about 10 percent of CheB-P
activity" — and raised its expression ≈5-fold above native CheB to recover WT2's kinase activity
(A≈1/2). `[primary-verified]` This is precisely the "altered CheB phosphorylation-site variant" the
brief asked about. Note what it demonstrates: the *phosphorylation feedback* and the *set-point* are
separable knobs — you can delete the feedback and compensate the set-point with expression level.

### 5.3 A third set-point-moving operation, discovered incidentally: temperature

**Shimizu et al. 2010** — `[primary-verified]`. The adapted steady-state activity is
a₀ ≈ 1/3 at 22°C and a₀ ≈ 1/2 at 32°C. Critically, they establish that this is *not* an expression
effect: growth conditions were identical and measurements were in a medium not supporting protein
synthesis, so "the expression levels of enzymes were the same" at both temperatures, and they
conclude the k_cat's for methylation and demethylation are the parameters most sensitive to
temperature. `[primary-verified]` Fitted saturating velocities: {V_R, V_B(0)} = {0.010, 0.013} s⁻¹
at 22°C, {0.030, 0.030} s⁻¹ at 32°C.

**Why this is the most probative datum in the whole track.** Here the set-point moved with protein
levels held fixed, and the primary attributes the move to the catalytic rate constants — i.e. to γ.
This is a direct experimental demonstration that **the target rides on the kinetic parameters**, not
on a stored state. It confirms §4 empirically rather than by reading equations. (Caveat: temperature
is a global perturbation, not a clean separate intervention target — it will move much else besides.
It is evidence about *where the target lives*, not a proposed S.3 operation.)

### 5.4 What does NOT count

**Receptor modification-site mutants (EEEE/QEEE/QEQE/QEQQ/QQQQ) do not move a set-point.** Shimizu et
al. state that these "modification-standard strains" are built in **CheR⁻ CheB⁻** backgrounds
precisely so the receptor module can be measured "in an open-loop configuration, without adaptation
feedback." `[primary-verified]` The corrector has been deleted. That is degradation, not a set-point
shift, and must not be scored under S.3.

**S.3 verdict: PASS**, on the CheB-expression operation, with the caveat that the moved object is a
kinetic parameter.

---

## 6. S.4 — achievable slow/fast ratio

### Fast timescale
**Sourjik & Berg 2002 (PNAS 99:12669)** — `[primary-abstract-only]` for the numbers below; I
retrieved the PMC record but it served abstract only (body not in PMC).
**Citation (metadata verified, PMCID PMC130518):** Sourjik V, Berg HC. "Binding of the *Escherichia
coli* response regulator CheY to its target measured in vivo by fluorescence resonance energy
transfer." *PNAS* 99(20):12669–12674, 2002. DOI 10.1073/pnas.192463199.
On flash release of caged chemoeffectors, CheY~P bound to FliM decayed with a rate constant of about
**2 s⁻¹** after attractant addition and rose at about **20 s⁻¹** after repellent addition.
`[primary-abstract-only]` → τ_fast ≈ 0.05–0.5 s.

Shimizu et al. corroborate the separation qualitatively: receptor-modification reactions are "much
slower than all other reactions in the system," which is why m gets a differential equation and `a`
an algebraic one. `[primary-verified]`

### Slow timescale
All `[primary-verified]`:
- Shimizu et al.: activity relaxation time constant **τ_a ≈ 29 s at 22°C, ≈ 11 s at 32°C**;
  characteristic frequency ν_m ≈ 0.006 Hz (22°C) and ≈ 0.018 Hz (32°C) — a ~3-fold shift from a
  10 °C change.
- Keegstra et al. 2017 (*eLife* 6:e26796, DOI 10.7554/eLife.26796, PMCID PMC5809148; full text
  retrieved and read): single-cell FRET activity autocorrelation time constant **9.5 ± 0.5 s** for
  cells adapted in buffer, with large fluctuations on the 10–100 s scale. `[primary-verified]`
- Neumann/Sourjik "Imprecision of adaptation" 2014 (§7): adaptation times (time to regain 50% of
  initial activity) run from tens of seconds to **>200 s** depending on stimulus size, with total
  adaptation to a single stimulus taking up to **30–45 min** for the largest steps.
  `[primary-verified]`

### Derived ratio — flagged as a cross-paper derivation, not a published quantity
Taking τ_fast ≈ 0.5 s (attractant direction) with τ_slow ∈ [9.5 s, ~200 s] gives a slow/fast ratio of
roughly **2×10¹ to 4×10²** — about **1.3 decades**, and that spread is produced by varying *stimulus
amplitude* and *temperature*, not by a designed expression-level knob.

**Can it be swept ≥2 decades by expression-level control?** **I could not establish this from a
primary.** What I can report:
- Alon et al. 1999 abstract says adaptation time "show[s] strong variations" with protein
  concentration — but the magnitude is in the unretrieved body. `[primary-abstract-only]`
- Frankel et al. 2014 (*eLife* 3:e03526, DOI 10.7554/eLife.03526, PMCID PMC4210811; full text
  retrieved and read) state that intracellular CheR/CheB levels "are known to change both adaptation
  timescale and clockwise bias," and that increasing mean CheR level decreased mean adaptation time
  — but this is a *modeling* paper; the statement is a model property with citations, not a
  measurement they report. `[primary-verified]` that they say it; the underlying measurement is
  `[secondary]` from here.
- Shimizu et al. demonstrate only a ~3-fold tuning (temperature). `[primary-verified]`

**S.4 verdict: PARTIAL.** The separation is real, large, and quantified at baseline (~1–2 decades
between the fast and slow modules). A *demonstrated, numerically documented ≥2-decade sweep of the
ratio under experimental control* is not something I retrieved. The likeliest place for it is the
body of Alon et al. 1999, which I could not reach.

---

## 7. S.5 — lifetime readout

**Score: WEAK.** There is no declared viable set and no survival/hazard observable tied to the
adaptation architecture in anything I retrieved. Honest answer: **chemotactic competence is not a
survival observable** in this literature. What exists:

**(a) A measured growth effect, causally uncommitted.** Neumann S, Løvdok L, Bartoszek K, Kollmann M,
Endres RG, Sourjik V. "Imprecision of adaptation in *Escherichia coli* chemotaxis." *PLoS ONE*
9(1):e84904, 8 Jan 2014. DOI 10.1371/journal.pone.0084904. PMCID PMC3885661. Full text retrieved and
read. `[primary-verified]`
They measured relative growth rate of MG1655 in M9 and confirmed that serine and cysteine above
0.1 mM reduce growth, and note that "the growth inhibition occurs in the same concentration range
where the precision of adaptation strongly deteriorates." But their own framing of the causal claim
is explicitly speculative — they write that they "speculate that the large imprecision of adaptation
for some amino acids may benefit bacteria." `[primary-verified]` **This is a correlation between two
concentration ranges, not a measured fitness consequence of adaptation precision.**
Their simulations further found that reducing precision of adaptation by up to 60% "had little
effect on the chemotactic drift velocity up a gradient," changing mainly the width of the steady-state
spatial distribution. `[primary-verified]` That cuts *against* a strong lifetime payoff from precision.

**(b) A fitness framework that is constructed, not measured.** Frankel et al. 2014 build
survival/fitness explicitly as a modeling layer: survival probability is imposed as a Hill function
of accumulated nutrient with two free parameters, and colonization fitness as a step-down function of
arrival time. `[primary-verified]` These are **assigned selection functions on simulation output**,
not measured hazards. Under the project's three-category grading convention this is at best a
constructed contrast, not a contingent result.

**Comparison class matched on everything but the architecture:** none found. The natural comparator
(cheR/cheB deletion) removes the corrector rather than the architecture, so it is a degradation
control, not an architecture-matched one.

---

## 8. Blocked-retrieval ledger

| Citation | DOI | Routes attempted | Outcome | Why it mattered |
|---|---|---|---|---|
| Alon U, Surette MG, Barkai N, Leibler S. "Robustness in bacterial chemotaxis." *Nature* 397(6715):168–171 (1999) | 10.1038/16483 | `fetch_article_fulltext` (Unpaywall → no OA location; Semantic Scholar → no openAccessPdf; PMC → no PMCID; Crossref TDM → no accessible content; DOI resolve → landing page only). OpenAlex `locations` enumerated: all three locations `is_oa: false` (Nature, PubMed, a RePEc submittedVersion pointer that resolves to the same paywalled nature.com page). PubMed metadata + abstract retrieved. | **Paywalled. Abstract only.** No mirror/proxy/archive attempted — out of policy. | **The single most consequential gap in this track.** It holds the actual magnitude of the CheR/CheB expression sweep, the numerical spread of steady-state behaviour, and the adaptation-time range — i.e. the direct evidence for both the S.3 magnitude and the S.4 two-decade question. Everything I say about the *size* of those effects is therefore bounded by the abstract. |
| Barkai N, Leibler S. "Robustness in simple biochemical networks." *Nature* 387(6636):913–917 (1997) | 10.1038/43199 | `fetch_article_fulltext` (Unpaywall → no OA location; Semantic Scholar → redirect loop >5 on nature.com PDF; PMC → no PMCID; Crossref TDM → none; DOI resolve → landing page only). OpenAlex: 2 locations, both `is_oa: false`. Abstract retrieved. | **Paywalled. Abstract only.** | The original two-state model. Mitigated: Yi et al. 2000 restate and analyze the BL model's equations in full, and I read that analysis, so the model structure is `[primary-verified]` *via Yi et al.* rather than from BL itself. The BL parameter values and simulation details remain unread. |
| Kollmann M, Løvdok L, Bartholomé K, Timmer J, Sourjik V. "Design principles of a bacterial signalling network." *Nature* 438(7067):504–507 (2005) | 10.1038/nature04228 | `fetch_article_fulltext` (all five routes failed as above). OpenAlex: 4 locations, all `is_oa: false`. Abstract retrieved. | **Paywalled. Abstract only.** | Robustness-to-expression-noise topology comparison. Partially mitigated by Løvdok et al. 2009 (*PLoS Biol* 7(8):e1000171, PMCID PMC2716512), same group, open, retrieved and read, which restates the topology argument. Downgrades Kollmann-specific claims to `[secondary]`. |
| Sourjik V, Berg HC. *PNAS* 99:12669 (2002) — CheY~P/FliM kinetics | 10.1073/pnas.192463199 | PMC record retrieved but serves **abstract only** (no body deposited); `fetch_article_fulltext` returned the same abstract-only text. | **Body not retrieved.** The 2 s⁻¹ / 20 s⁻¹ rate constants are `[primary-abstract-only]`. | These are the fast-timescale numbers in the S.4 ratio. They are stated in the abstract with units, so the values are sound, but I have not seen the traces they come from. |
| Meir Y, Jakovljevic V, Oleksiuk O, Sourjik V, Wingreen NS. *Biophys J* 99(9):2766–2774 (2010) | 10.1016/j.bpj.2010.08.051 | `fetch_article_fulltext` → PMC returned metadata + abstract; PMC XML carries the explicit notice that the publisher does not allow full-text XML download. Semantic Scholar route failed (http-only URL rejected by the fetcher's https-only policy). | **Body not retrieved. Abstract only.** | Would have given an independent quantification of adaptation precision and cell-to-cell variation in adaptation *rate* — relevant to S.4's tunability. Its central claim (precision loss arises from methylation slowing as sites become scarce) is `[primary-abstract-only]`. |

**No blocked retrieval was worked around via a mirror, archive, proxy, or spoofed user agent.**
Where a paywalled source was needed, I either substituted an open primary that independently
establishes the same equations (Yi et al. for the BL model) and said so, or recorded the gap.

---

## 9. Screening scorecard

| Criterion | Verdict | Basis |
|---|---|---|
| **S.1** dynamical description + performable interventions | **PASS** | Two published closed-form dynamical models (`ṁ = F(a)`, `a = G([L],m)`) with experimentally measured transfer functions; interventions are routine molecular genetics (inducible CheR/CheB, point mutants, modification-site mutants). Not flux-balance. `[primary-verified]` |
| **S.2** candidate stored reference | **FAIL** | Slow variable `m` exists and is genuinely slow, but it is the *integrator state*, not a stored target. The adapted activity is given in closed form (Yi Eq. 1) with `m` absent; the target is γ = k_r/k_b, a kinetic parameter. `m` is also not a fixed point of a fast constitutive drift — it is driven by the error — so it fails S.2 from the *other* direction than the one S.2's exclusion clause anticipates. `[primary-verified]` |
| **S.3** independent perturbability | **PASS** | CheB expression at ~0.5× native moves adapted activity 1/3 → 1/2 with machinery intact and precision preserved (Clausznitzer). Also CheB^D56E + expression compensation. `[primary-verified]` The operation moves a parameter, not a state. |
| **S.4** tunable slow/fast ratio ≥2 decades | **PARTIAL** | Baseline separation ~1–2 decades quantified (τ_fast ≈ 0.05–0.5 s; τ_slow ≈ 9.5–200+ s). Demonstrated *tuning* range documented in retrieved primaries is only ~3-fold (temperature). The ≥2-decade sweep claim is unverified; the evidence for it sits in the paywalled Alon 1999 body. |
| **S.5** lifetime readout + matched comparison class | **WEAK** | No declared viable set, no measured survival/hazard tied to adaptation architecture. Growth-inhibition correlation is real but causally uncommitted by its own authors; fitness functions in the modeling literature are assigned, not measured. No architecture-matched comparison class. |

## 10. Eligibility under both readings

**Reading A (STRICT / autonomy): NO — structurally excluded, not merely unclear.**
Reading A requires ẋ = f(x) with no functional dependence on the regulated coordinates. The
published model is `dm/dt = F(a)` where `a` is the regulated variable, and Yi et al. name `r − bA`
as the system error whose integral is `m`. This is the textbook case Reading A was written to
exclude — it is, by the primary's own title, integral feedback control. `[primary-verified]`

**Reading B (LOOSE / scale separation): YES, with one reservation.**
- Declared timescale separation: yes, explicit and quantified (τ_fast ≈ 0.05–0.5 s vs τ_slow ≈ 10–200 s).
- Load-bearing coupling m → a setting a's operating point: yes, quantified — f_m(m) linear in m with
  α ≈ 2 kT per methyl group, N = 6, K_I/K_A = 0.0062. `[primary-verified]`
- Separate intervention addressability: yes for the *slow module* (inducible CheR/CheB, CheB^D56E).
- Feedback a → m: permitted under Reading B.
- **Reservation:** Reading B still says "stores a target," and §4 shows this system's target is not
  stored in the slow variable. Reading B admits the *architecture*; the second filter still bites.
  If Gate 1 adopts Reading B, prime should decide whether Reading B's "stores a target" clause is
  meant to carry the state/parameter distinction or is satisfied by mere set-point-setting coupling.
  **These two readings disagree here, and the disagreement is not marginal.**

## 11. Role recommendation

**REJECT as the positive article. Recommend as a strong NEGATIVE CONTROL candidate — with a caveat
prime must weigh.**

*Why not positive:* the positive article must have a stored reference that is a separate intervention
target from the regulated dynamics. This system's reference is a rate-law constant. Building the P1
test on it would mean "corrupting the stored set-point" by changing a kinetic parameter of the
corrector — which is the operation the criterion is trying to distinguish *from*. The test would not
discriminate.

*Why it is an unusually good negative control:* it is the strongest possible negative — a system that
looks maximally like the positive case (slow variable, huge timescale separation, exact adaptation,
set-point-shifting perturbations, quantified dynamical model, decades of FRET data) and yet has no
target-as-state. A negative control that fails only on the sharp filter is far more informative than
one that fails on everything. And unlike a star, it *does* have a separable slow module — so it tests
whether the criterion's teeth are in "decoupled reference" or merely in "has a slow variable."

*The caveat, stated plainly.* A negative control is supposed to "demonstrably correct but be
model-free." This system is **not** model-free in the ordinary sense — it corrects via an internal
dynamical variable, which a star does not. If the arc's negative control is meant to be model-free,
chemotaxis is the wrong shape for that slot too, and its real role is as a **third category**: a
*near-miss* that discriminates the two readings. Prime pairs; I am flagging that neither of the two
offered slots is a clean fit, and that this is itself a finding.

*One live route back to POSITIVE, for prime's judgement only.* If Gate 1 adopts the counter-argument
in §4 — that the CheR:CheB stoichiometry is itself the slow stored state — then S.2 flips to PASS and
the Clausznitzer CheB-expression experiment becomes a competent-misregulation demonstration already
in the literature. I do not recommend this, for the reasons in §4, but the decision is prime's and
the empirical facts are the same either way.

## 12. Surprises worth prime's attention

1. **Prime's S.3 concern is a conflation, and correcting it does not save the candidate.** Precision
   is robust; the level is not. So S.3 passes. But the candidate fails anyway, on S.2 — a filter
   prime's note did not flag as the risk. The system dies one step later than expected, from a
   different cause.
2. **The failure is provable from equations, not estimated.** Yi et al. Eq. 1 is closed-form and the
   methylation level is simply absent from it. Per the project's preference for analytic over
   estimated results, this determination does not rest on a fit.
3. **Shimizu et al.'s temperature result is the cleanest single datum in the track**, and it was
   incidental to what I was looking for: the set-point moved 1/3 → 1/2 with protein expression held
   fixed, attributed by the authors to k_cat. A stored-state target could not do that.
4. **The competent-misregulation phenotype P1 wants already exists in print** (Clausznitzer WT2:
   precise adaptation to a shifted level). Whatever system the arc selects, this is a published
   reference example of the phenotype's *shape* — useful to prime independent of this candidate's fate.
5. **The imprecision paper cuts against P3 for this system**: reducing adaptation precision by up to
   60% barely changed chemotactic drift velocity in their simulations. If the architecture buys
   anything here, it is not obviously drift performance.
6. **A number to keep out of the record:** the "50-fold" often attached to CheR overexpression in
   recollection does not appear in any primary I read in that role. The only 50-fold I verified is
   site-to-site variation in *methylation rate* on Tar (Yi et al., citing Terwilliger & Koshland).
   If a 50-fold CheR figure appears in downstream AOP documents, it needs its own source.

---

## 13. Primaries read in full (content verified)

1. Yi TM, Huang Y, Simon MI, Doyle J. *PNAS* 97(9):4649–4653 (2000). DOI 10.1073/pnas.97.9.4649.
   PMCID PMC18287. — Eq. 1, the four assumptions, the ż = r − bA reduction, Fig. 2 caption.
2. Shimizu TS, Tu Y, Berg HC. *Mol Syst Biol* 6:382 (2010). DOI 10.1038/msb.2010.37. PMCID PMC2913400.
   — Eqs. 1–2, F(a) measurement, τ_a, ν_m, MWC calibration, temperature comparison, modification-
   standard strain genotypes.
3. Clausznitzer D, Oleksiuk O, Løvdok L, Sourjik V, Endres RG. *PLoS Comput Biol* 6(5):e1000784
   (2010). DOI 10.1371/journal.pcbi.1000784. PMCID PMC2873904. — WT2 CheB-expression experiment,
   γ_R/γ_B, CheB^D56E, five-model comparison.
4. Neumann S, Løvdok L, Bartoszek K, Kollmann M, Endres RG, Sourjik V. *PLoS ONE* 9(1):e84904 (2014).
   DOI 10.1371/journal.pone.0084904. PMCID PMC3885661. — precision vs adaptation time, growth
   inhibition, drift-velocity simulations.
5. Keegstra JM, Kamino K, Anquez F, Lazova MD, Emonet T, Shimizu TS. *eLife* 6:e26796 (2017).
   DOI 10.7554/eLife.26796. PMCID PMC5809148. — single-cell FRET autocorrelation 9.5 ± 0.5 s.
6. Frankel NW, Pontius W, Dufour YS, Long J, Hernandez-Nunez L, Emonet T. *eLife* 3:e03526 (2014).
   DOI 10.7554/eLife.03526. PMCID PMC4210811. — phenotypic parameters, constructed fitness functions.
7. Løvdok L, Bentele K, Vladimirov N, Müller A, Pop FS, Lebiedz D, Kollmann M, Sourjik V.
   *PLoS Biol* 7(8):e1000171 (2009). DOI 10.1371/journal.pbio.1000171. PMCID PMC2716512. —
   topology/robustness restatement; adapted activity set by receptor-bound CheR:CheB ratio.

**Abstract-only (content NOT verified):** Alon et al. 1999 (10.1038/16483); Barkai & Leibler 1997
(10.1038/43199); Kollmann et al. 2005 (10.1038/nature04228); Sourjik & Berg 2002 PNAS 99:12669
(10.1073/pnas.192463199); Meir et al. 2010 (10.1016/j.bpj.2010.08.051).

---

*End Chemotaxis_retrieval_v1. Builder output — proposal for verification, not a verdict.*
