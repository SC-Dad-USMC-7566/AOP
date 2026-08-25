# Circadian track — KaiABC clock of *Synechococcus elongatus* PCC 7942
## Gate 1 retrieval, life-criterion falsification arc — BUILDER PROPOSAL, not a verdict

**Track:** Circadian (cyanobacterial KaiABC) · **File:** Circadian_retrieval_v1.md · **Date:** 2026-08-02
**Standing:** Claude Science seat (builder). This is scored evidence for another seat to verify and pair. I do not select, do not pair, and certify nothing.

**Retrieval tags used on every substantive claim:**
`[primary-verified]` = I read the passage in the primary · `[primary-abstract-only]` = I read only the abstract of the primary · `[secondary]` = a review or another primary reports it · `[not-retrieved]` = citation only.

---

## 0. Headline finding, stated up front

The longlist rationale for this candidate was that its slow variable's autonomy may be **experimentally demonstrated** rather than merely modelled, which would make it the only candidate eligible under strict Reading A. **That rationale does not survive retrieval intact.** The autonomy demonstration is real, but it holds in the *in vitro* preparation, and the *in vitro* preparation has no regulated variable, no viable set, and no lifetime. The *in vivo* preparation — where the viability readout, the fitness competition and the misregulation phenotype all live — carries at least three documented feedback paths from the regulated coordinates back onto the slow variable. So:

- **Reading A (strict autonomy) is satisfiable, but not simultaneously with S.5.** The two live in disjoint preparations.
- **Reading B (scale separation) is satisfied cleanly, in vivo, with the strongest S.5 evidence of any candidate I would expect on the longlist.**
- The **target-as-state / target-as-parameter** filter comes out **STATE** for the object the criterion actually needs (clock *phase*), and **PARAMETER** for the S.4 knob (clock *period*). These are different objects and the distinction is empirically grounded, not stipulated.
- The **honest weakness is real and the literature supports it plainly**: the clock's stored content is calibrated by, and is only useful relative to, an **external periodic signal**. It is a model of the environment. Whether that also constitutes storing the cell's own viable set is a live argument, not a settled fact — I set out both sides in §7 rather than resolving it, because resolving it is adjudication and not mine.

---

## 1. S.1 — dynamical description + physically performable interventions → **PASS**

**Dynamical description exists at two levels, both with published equations constrained by data.**

- The post-translational oscillator has an explicit kinetic model over KaiC phosphoforms. `[primary-verified]` Rust et al. 2007 resolve four KaiC phosphoforms and fit a data-constrained model; the paper states that total phosphorylation cannot be the sole dynamical variable "since it traverses the same value twice each day, but each time in a different direction". Read in the PMC full text (PMC2427396).
- `[primary-verified]` Rust et al. 2011 present a data-constrained mathematical model of entrainment via the adenine-nucleotide pool (PMC3309039 full text).
- `[primary-verified]` Phong et al. 2013 (PNAS 110:1124) present a model in which "this ATPase-mediated delay in negative feedback gives rise to a compensatory mechanism" separating period robustness from phase/amplitude tunability (PMC3549141 full text).
- `[primary-verified]` Teng et al. 2013 (Science 340:737) fit a two-loop (post-translational + transcription-translation) model and perform parameter-space analysis (PMC3696982 full text).

**Physically performable interventions exist and are numerous:** dark pulses, ATP/ADP-ratio steps in vitro, initialization of the reconstituted reaction with a chosen KaiC phosphoform mix, point mutations in *kaiC*, deletion/complementation of *rpaA*, phosphomimetic *rpaA* alleles, decoupling *kaiBC* expression from clock control. Each is cited under the relevant criterion below.

This is not a structure-only or flux-balance system. **S.1 PASS.**

---

## 2. S.2 — candidate stored reference → **PASS (with a caveat about what "target" means)**

**The slow variable:** the phase of the KaiC phosphorylation cycle — operationally, the distribution of KaiC over its phosphoforms at S431 and T432.

- `[primary-verified]` The two autophosphorylation sites are Ser-431 and Thr-432, identified by mass spectrometry; alanine substitution at either impairs phosphorylation and the double mutant abolishes phosphorylated KaiC and rhythmicity (Nishiwaki et al. 2004, PNAS 101:13927; read in PMC518855).
- `[primary-verified]` The phase is a *state*, not a parameter: in the reconstituted reaction, "a reaction initiated with a KaiC pool enriched in T-KaiC begins in the phosphorylation phase, whereas a reaction initiated with high levels of S-KaiC begins in the dephosphorylation phase" (Rust et al. 2007, Fig. 1C). This is the cleanest single sentence in the retrieved corpus for the state claim.
- `[primary-verified]` The slow timescale is set by an intrinsic enzymatic rate, not by a fixed point of the fast dynamics: KaiC's ATPase activity is ~15 ATP per KaiC per day, and across wild type plus five period mutants the activities "are directly proportional to their in vivo circadian frequencies" (Terauchi et al. 2007, PNAS 104:16377; read in PMC2042214).

**The coupling onto the regulated variable is load-bearing, not decorative.**

- `[primary-verified]` RpaA is the master output regulator: "Deletion of rpaA abrogates gene expression rhythms globally and arrests cells in a dawn-like expression state," and critically, "rescuing oscillator function does not restore global expression rhythms" — the rescue experiment separates loss-of-output from loss-of-oscillator (Markson et al. 2013, Cell 155:1396; read in PMC3935230).
- `[primary-verified]` The clock state is read out through phosphorylation of RpaA by two antagonistic, clock-timed enzymes: "SasA acts as a kinase toward RpaA, whereas CikA, previously implicated in clock input, acts as a phosphatase that dephosphorylates RpaA" (Gutu & O'Shea 2013, Mol Cell 50:288; read in PMC3674810).
- `[primary-verified]` The output pathway was identified as SasA→RpaA, with clock-state-dependent phosphotransfer, and circadian transcription severely attenuated in *sasA* and *rpaA* mutants (Takai et al. 2006, PNAS 103:12109; read in PMC1832256).

**Caveat I will not paper over.** What the clock supplies to the regulated dynamics is a *schedule*, and the clock-to-output link as retrieved is largely feedforward: clock phase → RpaA~P level → expression program. I found **no primary passage** establishing a comparator that computes an error between a regulated variable and a clock-supplied reference and drives correction of that error. The criterion's phrase "actively corrects its regulated variables against a decoupled internal reference" is therefore satisfied in the *reference-supplying* half and **not demonstrated** in the *error-correcting* half. `[not-retrieved]` for the comparator; I looked and did not find it, rather than concluding it does not exist.

**S.2 PASS** on the stored-reference reading; the comparator gap is logged as an open item for the pairing seat.

---

## 3. S.3 — independent perturbability: moving the reference without disabling the machinery → **PASS**

Two operationally distinct classes, both verified in primaries.

### (a) Phase resetting — moves the state, machinery demonstrably still running

- `[primary-verified]` **In vivo dark pulse.** A 4-h dark pulse yields a phase response curve; the authors selected "a 5-h dark pulse starting after 5 h of LL (LL5), which causes a stable 10-h phase advance." The *pr1* mutant isolated in the same screen had a normal free-running period (24.9 ± 0.2 h vs 24.6 ± 0.4 h wild type) but no phase shift — i.e. phase-shifting capability is genetically separable from oscillation (Kiyohara et al. 2005, J Bacteriol 187:2559; read in PMC1070383).
- `[primary-verified]` **In vitro ATP/ADP step.** Adding ADP to bring ATP/(ATP+ADP) to ~50% for ~5 h produces large phase shifts, and "the phase response curve obtained by altering the ATP/ADP ratio in vitro was similar to that observed in live cells treated with pulses of darkness." Induced shift was "a graded function of the amount of ADP added." In vivo, after 2–3 h dark the ratio fell to nearly 50% and recovered to ~85% within an hour of re-illumination (Rust et al. 2011, Science 331:220; read in PMC3309039). This is a reference-moving operation with a **reversible, non-destructive** actuator.
- `[primary-verified]` **In vitro phosphoform initialization.** Rust et al. 2007 Fig. 1C (quoted in §2) sets initial phase by choice of the starting KaiC phosphoform pool. The machinery is by construction intact — it is the same three purified proteins.
- `[primary-abstract-only]` Temporal *kaiC* overexpression resets the phase of the rhythms (Ishiura et al. 1998, Science 281:1519 — abstract only; primary blocked, see §9).

### (b) Period mutants — clock still functions, period changed

- `[primary-abstract-only]` The founding mutant collection: 12 mutants "exhibit a broad spectrum of periods (between 16 and 60 hours)" plus arrhythmics, from 150,000 screened clones (Kondo et al. 1994, Science 266:1233 — abstract only; primary blocked).
- `[primary-verified]` Specific alleles with a still-functioning clock: **S157P** and **F470Y** (short period), and named period mutants whose purified KaiC ATPase rates scale with in vivo frequency (Terauchi et al. 2007). **Y402C** in vivo period ~85 h with in vitro period 103 h; **Y402A** in vitro period 158 h; **Y402W** 15 h; **Y402F** close to 24 h; **Y402D** arrhythmic (Ito-Miwa et al. 2020, PNAS 117:20926; read via PMC7456120).
- `[primary-verified]` **P28** (long period, ≈30 h) and **SP22** (short period, ≈23 h) each carry a missense mutation in *kaiC*, with wild type ≈25 h at 30 °C; **P28R** is the genetically rescued derivative returning to ≈25 h (Ouyang et al. 1998, PNAS 95:8660; read via PMC21132).

### Critical distinction for the criterion
Phase resetting moves a **state** and leaves every rate constant untouched. Period mutation changes a **kinetic parameter** (KaiC ATPase rate — Terauchi 2007 makes this quantitative). Both are "set-point-moving with machinery intact" in the loose sense, but only phase resetting is the operation S.3 actually asks for. **S.3 PASS on phase resetting; period mutants pass only under a parameter-permissive reading.**

### The sharpest P1 case: does a wrong-phase clock produce competent-but-misdirected regulation?
Yes, and this is the strongest P1-shaped evidence I retrieved.

- `[primary-verified]` Ouyang et al. 1998: in non-resonant FRP/LD combinations the clock keeps running and entrains, but "the phase relationships between the rhythms and the LD cycles are different among the strain types," with the winning combinations "correlated with a phase relationship of rhythmic psbAI promoter activity being low in the early day and peaking near dusk." The losing strains are not broken — they are precisely regulating to the wrong phase.
- `[primary-verified]` Lambert et al. 2016 give the single-cell version with a hazard readout: decreased fitness "can result from a catastrophic growth arrest caused by unexpected darkness in a small subset of cells with incorrect clock times corresponding to the subjective morning," and "the probability of dark-induced growth arrest oscillated with clock time, reaching a minimum at subjective dusk." Arrest was irreversible: cells "ceased and did not resume even after 36 h of subsequent light exposure," and the effect required prolonged darkness — no arrest after 5-h pulses (Biophys J 111:883; read via PMC5002072).

That is competent machinery, intact regulation, wrong target, measurable death. It is P1's shape almost exactly — with the caveat in §7 that the "wrong target" is wrong *relative to the environment*, which is precisely the objection.

---

## 4. S.4 — tunable slow/fast ratio spanning ≥2 orders of magnitude → **PARTIAL**

**Period range achieved (numerator).**
- `[primary-verified]` **15 h → 158 h in vitro** from single substitutions at KaiC residue 402: "from 15 h (0.6 d) to 158 h (6.6 d)", a stated 10-fold dynamic range, with Y402A's rhythm "persisting for ~20 d" (Ito-Miwa et al. 2020).
- `[primary-abstract-only]` 16–60 h in vivo across the Kondo 1994 mutant collection.

So the slow variable alone is tunable over **one order of magnitude (≈10×), not two.**

**What does not extend the range.**
- `[primary-verified]` **Temperature does not** — and the irony flagged in the brief is confirmed. Q10 of period is 1.04 (WT) and 1.02 (Y402C) in vivo over 25–30 °C, and 1.05–1.13 in vitro for several Y402 variants. Temperature compensation survives even the 10-fold period change (Ito-Miwa et al. 2020). Temperature is a non-knob by design.
- `[primary-verified]` **ATP/ADP ratio does not** — it is a phase/amplitude knob, explicitly not a period knob: "the core oscillator continued to measure time robustly across a range of ATP/ADP ratios… Rhythms persist with a period that remains close to 24 h (within 5%)" (Phong et al. 2013). This is a clean, deliberate architectural separation of phase-tunable from period-robust, and it means the least destructive actuator available is unusable for S.4.
- **Stoichiometry:** `[primary-verified]` Y402C and Y402A required 3-fold and 3.5-fold higher KaiA to oscillate at all, and excess KaiA degraded temperature compensation even in WT (Q10 1.30 and 1.27). So KaiA titration is coupled to compensation and is not a clean period knob. I found **no primary** reporting a systematic KaiA:KaiB:KaiC stoichiometry-vs-period sweep — `[not-retrieved]`.

**The denominator (fast timescale) is where the second order of magnitude would have to come from.**
- `[primary-verified]` Output-pathway biochemistry is minutes-scale: phosphotransfer profiling of SasA/CikA onto RpaA is reported at a five-minute time point, with kinase and phosphatase rates as initial linear slopes (Gutu & O'Shea 2013).
- `[primary-verified]` Growth/dilution rate is independently tunable over ≈5× in a microfluidic chemostat: one division per 14–16 h versus one per 72 h (Teng et al. 2013). Note this is a *coupled* knob — Teng et al. show the post-translational-only strain desynchronizes faster at faster growth, so moving the fast timescale changes oscillator behaviour too.

**Verdict.** ≈10× on the slow variable via *kaiC* residue-402 alleles is solidly established in a primary. Reaching ≥2 orders requires composing that with a fast-timescale change, and the available fast-timescale knob (growth rate) is not independent of the oscillator. Also: every period knob that works is a kinetic-parameter change, i.e. a machinery modification. **S.4 PARTIAL.** I would not report this as a pass, and the brief's suspicion that period mutants "may only span a factor of a few" is too pessimistic by about 3× but right in kind.

---

## 5. S.5 — lifetime readout + matched comparison class → **STRONG**

This is the candidate's strongest dimension, and the comparison classes really are matched on architecture.

### Competition as a fitness/hazard-adjacent observable
`[primary-verified]` Ouyang et al. 1998 (read via PMC21132):
- **Matched-on-everything-but-the-clock, verified explicitly.** Strains were "selected on the basis of equivalent growth rates in LL," and in pure culture "the growth rates of the various strains… are indistinguishable in both LL (Fig. 1B) and a 24-h LD 12:12 cycle (Fig. 1C)"; similar results for LD 11:11 and LD 15:15. Doubling times reported: one division per 16.1 h in LD, per 6.3 h in LL.
- **Resonance result.** In LD 11:11 (22-h cycle) the short-period SP22 defeats wild type; in LD 15:15 (30-h cycle) the long-period P28 takes over; head-to-head, "the strain whose period most closely matches that of the LD cycle eliminates the competitor."
- **The constant-light control that makes it a clock effect.** "When these same combinations are grown together in LL, however, both strains are maintained."
- **Genetic-background control.** Two independently marked wild types (AMC149 vs AMC343) coexist for many generations, and the rescued P28R returns to ≈25 h.
- **Independent apparatus replication.** Turbidostat at constant cell density reproduced the batch result. Reported Table 1 values: LD 12:12, wild type went 52%→96% at day 15 and →100% at day 19; LD 15:15, wild type went 52%→5% then →4% while P28 rose to 95–96%. **Elapsed generations are 5.4 at day 15 and 6.8 at day 19** — exclusion is fast, not slow. (The n = 77–87 values in the same table are colony sample sizes per timepoint, not generations; I misread them as generations in v1 of this file and corrected it here.) Batch competitions in Fig. 2 ran 27 days.
- **Effect size.** Modelled relative fitness of the losing strain "as low as 0.7–0.8" (wild type ≈0.7 in LD 15:15; P28 ≈0.85 in LD 12:12).

### Arrhythmic-versus-rhythmic in matched conditions
- `[primary-abstract-only]` Woelfle et al. 2004 (Curr Biol 14:1481): "strains with a functioning biological clock defeat clock-disrupted strains in rhythmic environments… this competitive advantage disappears in constant environments." **Primary blocked — see §9.** I am not calling this retrieved.
- `[primary-verified, but secondary for Woelfle's data]` Ma, Woelfle & Johnson 2013 (Chaos Solitons Fractals 50:65; read via PMC3633149) reports the design in detail: arrhythmic **CLAb** carries *kaiC* **G460E**; wild type became predominant within ~20 generations in LD 12:12; the CLAb point mutation was rescued by a wild-type *kaiC* copy and the rescued strain then held ~equal proportions against wild type; in LL the CLAb fraction significantly *increased* (p = 0.01). A second mutant **CLAc** (**T495A**, rapidly damping) lost in LD but persisted as a small fraction past 30 generations, versus CLAb's rapid decline within 20 — a graded dose-response in rhythmicity. Also reports that in pure culture no strain's growth rate differs significantly from wild type in LL or LD. Tagged `[secondary]` for the underlying Woelfle/Ouyang data.

### A genuine per-cell hazard readout
`[primary-verified]` Lambert et al. 2016: probability of irreversible dark-induced growth arrest as a function of clock phase, single cells, minimum at subjective dusk (quotes in §3). This is a first-passage-adjacent observable measured directly rather than inferred from population composition.

### Output-pathway deletion gives outright conditional lethality, matched on condition
- `[primary-verified]` Diamond et al. 2017 (PNAS 114:E580; read via PMC5278464): "rpaA-null mutants are inviable after several hours in the dark"; viable-cell counts (CFU) taken through the dark period; cells "did not resume growth during a following light period, even when transitioned back to LL growth conditions."
- `[primary-verified]` Puszynska & O'Shea 2017 (eLife 6:e23210; read via PMC5400509): "in constant light wild type and the rpaA- cells grow at the same rate… however, the rpaA- strain is not viable when cultured in alternating light/dark conditions"; ectopic *rpaA* complementation "fully restores viability"; the phosphomimetic **RpaA D53E** restores viability in LD while **D53A** does not; the defect persists in a *clock-rescue* background, separating loss-of-RpaA from loss-of-oscillator. Mechanistically the affected genes are the dusk-peaking carbon-catabolism set (*gnd*, *glgP_gap1*, *fbp_zwf_opcA*), and independent deletion of those operons "results in impaired viability in light/dark cycles but not in constant light conditions."

**S.5 STRONG.** Lifetime readouts: competitive exclusion within ~5–7 turbidostat generations (and within ~20 generations for arrhythmic vs wild type in Ma 2013), per-cell irreversible-arrest hazard vs clock phase, and CFU viability through darkness. Comparison classes: period-mutant vs wild type in resonant vs non-resonant LD with an LL control; arrhythmic vs wild type with a genetic-rescue control; output-null vs wild type in LD vs LL with complementation and phosphomimetic controls. This is unusually well-matched.

---

## 6. Reading A vs Reading B

### Reading A (STRICT / autonomy): ẋ = f(x), no functional dependence on y → **UNCLEAR, and preparation-dependent**

**The autonomy evidence, for real.** `[primary-abstract-only]` Nakajima et al. 2005 (Science 308:414): the self-sustaining KaiC phosphorylation oscillation was reconstituted "by incubating KaiC with KaiA, KaiB, and adenosine triphosphate"; "the period of the in vitro oscillation was stable despite temperature change (temperature compensation)"; and "the circadian periods observed in vivo in KaiC mutant strains were consistent with those measured in vitro." **The Nakajima primary is paywalled and I could not read it — see §9.** I therefore hold its specifics at abstract level and record no numerical period from it. Corroborating primaries I *did* read:
- `[primary-verified]` "circadian oscillations can be reconstituted in vitro using only three proteins: KaiA, KaiB, and KaiC," and the clock "requires neither transcription nor translation" (Rust et al. 2007, introduction).
- `[primary-verified]` "When the three clock proteins KaiA, KaiB, and KaiC are mixed in a test tube, the phosphorylation state of KaiC exhibits a temperature-compensated circadian rhythm," and KaiC's ATPase "exhibits temperature compensation and correlation with a circadian frequency even in the absence of KaiA and KaiB" (Ito-Miwa et al. 2020) — the second clause is a strong autonomy statement: the period-setting rate is intrinsic to KaiC alone.
- `[primary-verified]` "in vivo circadian oscillations are stable in dark conditions, where transcription is repressed and cells are not growing" (Teng et al. 2013, introduction) — autonomy from transcription *inside* a cell, though with the regulated output also suppressed.

**Why this does not deliver Reading A in the living system.** Three documented y → x paths:
1. `[primary-verified]` **Transcriptional feedback onto the oscillator.** *kaiBC* promoter activity is under circadian control (Teng et al. 2013); the post-translational-only strain, built by making *kaiBC* expression constitutive, oscillates but loses population synchrony — synchronization index drops ~70% over 5 days vs ~25% for wild type — and the wild-type system is far less sensitive to parameter variation. So the transcriptional loop is not decorative: it is what makes the in vivo clock stable.
2. `[primary-verified]` **The output regulator feeds back on the core oscillator.** Phosphorylated RpaA "regulates the expression of not only clock components, generating feedback on the core oscillator" (Markson et al. 2013), and *rpaA* deletion "causes core oscillator failure by perturbing clock gene expression."
3. `[primary-verified]` **Metabolic state entrains the oscillator.** ATP/ADP, a regulated physiological variable, shifts clock phase in vivo and in vitro (Rust et al. 2011). The clock reads the cell's energetic state.

**Reading A verdict: UNCLEAR.** In the reconstituted system, ẋ = f(x) holds and is experimentally demonstrated — but there is no y at all, hence no S.5, no viable set, and nothing for the criterion's regulation clause to apply to. In the cell, y → x coupling is documented three ways. **Strict Reading A and S.5 cannot be obtained in the same preparation for this candidate.** That is the single most consequential thing on this page.

### Reading B (LOOSE / scale separation) → **YES**

All three requirements met and verified: (i) declared timescale separation — ~24 h clock (Ito-Miwa 2020: 15–158 h across alleles) versus minutes-scale output phosphotransfer (Gutu & O'Shea 2013) and hours-scale expression programs; (ii) load-bearing coupling onto y that sets y's operating point — *rpaA* deletion abolishes global rhythms and the clock-rescue experiment shows the coupling, not the oscillator, is what carries it (Markson et al. 2013); (iii) separate intervention addressability — dark pulses and ADP steps move phase without touching the output machinery, and *rpaA*/phosphomimetic alleles move the output without touching the oscillator (Puszynska & O'Shea 2017). Feedback y → x is permitted under Reading B, so the three paths above are not disqualifying.

---

## 7. Target-as-state or target-as-parameter → **STATE** (for the object the criterion needs)

**Determination: STATE.**

The referent of "stores a target" here is **clock phase**, and phase is a dynamical state of the KaiC phosphoform distribution — not a rate-law constant. The decisive empirical facts:
- `[primary-verified]` Phase is set by the *value* of the phosphoform variables: initializing with T-KaiC-enriched versus S-KaiC-enriched pools starts the reaction in the phosphorylation versus the dephosphorylation phase respectively (Rust et al. 2007, Fig. 1C). Same rate constants, different starting state, different phase.
- `[primary-verified]` Phase is moved by a transient, reversible perturbation of a metabolite pool, with full recovery of the pool — ATP/(ATP+ADP) fell to ~50% and returned to ~85% within an hour — while the oscillator continues (Rust et al. 2011). No parameter was edited.
- `[primary-verified]` Downstream regulation reads the *value* of the slow state: SasA kinase and CikA phosphatase are activated at distinct clock times by specific KaiC phosphoforms/complexes, converting phase into an RpaA~P level (Gutu & O'Shea 2013); RpaA~P level then selects the dawn or dusk program, and forcing it with a constitutively active allele switches cells between those programs (Markson et al. 2013).

**Where PARAMETER shows up, and why it is a different object.** The *period* — the S.4 knob — is a parameter. `[primary-verified]` Period is set by KaiC's intrinsic ATPase rate, with mutant ATPase activities directly proportional to in vivo frequencies (Terauchi et al. 2007), and every period-tuning operation retrieved is a point substitution in KaiC (Ito-Miwa 2020, Terauchi 2007, Ouyang 1998). Editing period means editing the machinery. So:

| object | kind | operation | machinery intact? | criterion role |
|---|---|---|---|---|
| clock **phase** | **STATE** | dark pulse, ADP step, phosphoform initialization | yes, demonstrated | S.3 — this is what S.3 wants |
| clock **period** | **PARAMETER** | *kaiC* point mutation (ATPase rate) | mutated but functional | S.4 knob only |

The favourable answer on the sharp filter is therefore real, but it is favourable for **S.3 only**. S.4 rides entirely on parameter edits.

---

## 8. The honest weakness: environmental model, or the cell's own viable set?

I was asked to state this plainly if the literature supports it. **It does, and this is the most serious objection to the candidate.** I set out the case each way and do not adjudicate.

**The case that the clock stores a model of an EXTERNAL periodic signal:**
- `[primary-verified]` The fitness of a given stored phase/period is defined *relative to the environment*, not intrinsically. In Ouyang et al. 1998 the very same strain wins in one LD cycle and is eliminated in another: wild type goes to 100% in LD 12:12 and to 4% in LD 15:15. A stored reference encoding the cell's own viable set should not reverse sign when only the environment changes.
- `[primary-abstract-only]` Woelfle et al. 2004's stated conclusion is that the adaptive value "is only fulfilled in cyclic environments" and that the intrinsic-value model is contradicted — the clock confers no advantage in constant conditions.
- `[primary-verified]` The clock is temperature-compensated *by design* (Q10 ≈ 1.0, Ito-Miwa 2020), i.e. engineered to track Earth's rotation rather than the cell's own thermal/metabolic state. Ito-Miwa et al. describe circadian clocks as "encoding Earth's physical rotation time as a pacemaker."
- `[primary-verified]` Without a rhythmic environment there is no clock phenotype at all: "under constant conditions, *S. elongatus* can grow robustly even without a functioning clock" (Lambert et al. 2016, introduction), and Ma et al. 2013 report the arrhythmic mutant's fraction *rising* in LL.
- The variable being tracked is *set by entrainment to light*, an external signal (dark-pulse PRCs, Kiyohara 2005; ATP/ADP as the light proxy, Rust 2011).

**The case that viability content is nonetheless what is stored:**
- `[primary-verified]` What the clock's output program actually encodes is an internal-resource schedule: RpaA-dependent dusk genes are glycogen breakdown, glycolysis and the oxidative pentose phosphate pathway, and independent deletion of those operons impairs LD viability but not LL viability (Puszynska & O'Shea 2017). The stored phase indexes *which internal metabolic state the cell must be in to survive the coming dark*.
- `[primary-verified]` The clock, not the environment, determines the cell's survival probability at a given moment: dark-induced irreversible arrest probability oscillates with clock phase, minimum at subjective dusk, and the vulnerable window coincides with the fastest-growth window — "the clock mediates a fundamental trade-off between growth and starvation tolerance" (Lambert et al. 2016). This is a viability-relevant internal variable read off the clock state.
- `[primary-verified]` Loss of the readout is lethal on its own terms, via internal redox collapse rather than external mismatch: ΔrpaA dies in darkness through failure to activate reductant-requiring pathways that detoxify reactive oxygen species (Diamond et al. 2017).

**My honest reading, offered as a proposal and nothing more.** The clock's *argument* is external time; its *content* is an internal viability schedule. Whether that counts as "storing its own viable set" under the criterion's component (5) turns on whether the criterion requires the stored object to be indexed by the system's own variables or merely to be *about* them. That is a criterion-interpretation question, not an empirical one, and it is exactly the kind of question I am not the seat to settle. What I can say evidentially: **the sign-reversal result in Ouyang 1998 is the hardest single fact against viability-set storage, and Lambert 2016 plus Puszynska 2017 are the hardest two facts for it.** All three are primary-verified.

---

## 9. Blocked-retrieval ledger

Four blocks. All were pursued through multiple routes before being logged; none was replaced by a secondary and called retrieved.

| Citation | DOI | Routes attempted | Outcome | Why it mattered |
|---|---|---|---|---|
| Nakajima M, Imai K, Ito H, Nishiwaki T, Murayama Y, Iwasaki H, Oyama T, Kondo T. Reconstitution of circadian oscillation of cyanobacterial KaiC phosphorylation in vitro. *Science* 308:414–415 (2005). PMID 15831759 | 10.1126/science.1108451 | `fetch_article_fulltext` (Unpaywall → no OA location; Semantic Scholar → no OA PDF; PMC → no PMCID; CrossRef TDM → no links); PMID→PMCID conversion returned none; OpenAlex `oa_status: closed`, zero OA locations; publisher landing page at science.org — **requested and was granted network access**, then received HTTP 403 on both `/doi/` and `/doi/abs/` | **PAYWALLED — `[primary-abstract-only]`.** Abstract read via PubMed. No numerical period or temperature-compensation figure taken from it. | This is the **autonomy** primary — the whole Reading A rationale for this track. Its in-vitro reconstitution claim is corroborated by Rust 2007, Ito-Miwa 2020 and Teng 2013 (all primary-verified), but those are `[secondary]` *for Nakajima's own content*. |
| Woelfle MA, Ouyang Y, Phanvijhitsiri K, Johnson CH. The adaptive value of circadian clocks: an experimental assessment in cyanobacteria. *Curr Biol* 14:1481–1486 (2004). PMID 15324665 | 10.1016/j.cub.2004.08.023 | `fetch_article_fulltext` (Unpaywall → no valid OA PDF; Semantic Scholar → http-only URL rejected; PMC → no PMCID; CrossRef TDM → nothing accessible); OpenAlex reported a bronze-OA PDF at cell.com — **requested and was granted network access to www.cell.com**, then received HTTP 403 on the article PDF path. Did not spoof a user agent or seek a mirror. | **PUBLISHER-BLOCKED — `[primary-abstract-only]`.** Its design is described in detail by Ma et al. 2013, which I read; that is tagged `[secondary]`. | The arrhythmic-versus-wild-type comparison class — one of the two structural claims S.5 rests on. The claim survives on Ouyang 1998 (primary-verified) plus Ma 2013 (secondary), but the Woelfle numbers themselves are not verified. |
| Kondo T, Tsinoremas NF, Golden SS, Johnson CH, et al. Circadian clock mutants of cyanobacteria. *Science* 266:1233–1236 (1994). PMID 7973706 | 10.1126/science.7973706 | PMID→PMCID → none; `fetch_article_fulltext` not attempted after conversion showed no PMC and the same publisher (science.org) had already returned 403 for a 2005 article on a granted domain | **PAYWALLED — `[primary-abstract-only]`.** The 16–60 h period range is an abstract-level claim. | S.4's in vivo period range. Superseded in practice by Ito-Miwa 2020 (primary-verified, 15–158 h in vitro), so the S.4 verdict does not depend on it. |
| Ishiura M, Kutsuna S, Aoki S, Iwasaki H, et al. Expression of a gene cluster kaiABC as a circadian feedback process in cyanobacteria. *Science* 281:1519–1523 (1998). PMID 9727980 | 10.1126/science.281.5382.1519 | PMID→PMCID → none; same publisher block as above | **PAYWALLED — `[primary-abstract-only]`.** "Temporal kaiC overexpression reset the phase of the rhythms" is abstract-level. | A third phase-resetting operation. Not load-bearing: S.3 already passes on dark pulses (Kiyohara 2005) and ADP steps (Rust 2011), both primary-verified. |

**Additional PMC access note (not a content block).** Twelve of the PMC records I relied on carry publisher restrictions on XML download ("The publisher of this article does not allow downloading of the full text in XML form"). I retrieved these via the ordinary PMC article HTML on pmc.ncbi.nlm.nih.gov, which is the same public full text a reader sees: PMC21132 (Ouyang 1998), PMC1832256 (Takai 2006), PMC2427396 (Rust 2007), PMC3935230 (Markson 2013), PMC3549141 (Phong 2013), PMC5278464 (Diamond 2017), PMC2042214 (Terauchi 2007), PMC1070383 (Kiyohara 2005), PMC518855 (Nishiwaki 2004), PMC7456120 (Ito-Miwa 2020), PMC5002072 (Lambert 2016), PMC3674810 (Gutu & O'Shea 2013). The remaining three — PMC3309039 (Rust 2011), PMC3696982 (Teng 2013), PMC5400509 (Puszynska & O'Shea 2017) — plus PMC3633149 (Ma 2013, cited as `[secondary]`) came through NCBI efetch XML. Everything tagged `[primary-verified]` above was read as full text in one of these forms.

**Bibliographic verification, separate from content.** Author lists, journal, volume, pages, year and DOI for every citation in this document were checked against CrossRef, independently of whether the content was readable — including the four paywalled entries. Pagination for Diamond 2017 (114:E580–E589) came from PubMed esummary, since CrossRef carries no page range for it. Nothing in the reference list is reproduced from memory.

**Searches that returned nothing (recorded gaps, not filled from training):**
- No primary found reporting a systematic KaiA:KaiB:KaiC **stoichiometry-versus-period** sweep. `[not-retrieved]`
- No primary found establishing a **comparator** that computes an error between a regulated variable and a clock-supplied reference and drives correction of that error. `[not-retrieved]` (§2 caveat)
- No primary found reporting **genome-wide mRNA decay rates** for *S. elongatus*, which would pin the fast timescale for S.4 quantitatively. `[not-retrieved]`

---

## 10. Summary table

| Criterion | Verdict | One-line basis |
|---|---|---|
| S.1 dynamics + interventions | **PASS** | Data-constrained kinetic models (Rust 2007, Rust 2011, Phong 2013, Teng 2013) plus a large intervention repertoire |
| S.2 stored reference | **PASS** (comparator gap logged) | KaiC phosphorylation phase (S431/T432); slow rate intrinsic to KaiC ATPase; load-bearing coupling via SasA/CikA→RpaA |
| S.3 independent perturbability | **PASS** | Dark-pulse and ADP-step phase resetting; oscillator demonstrably keeps running; *pr1* separates resetting from oscillation |
| S.4 slow/fast ratio ≥2 orders | **PARTIAL** | 15–158 h (≈10×, one order) via *kaiC* Y402 alleles; temperature and ATP/ADP explicitly do *not* tune period; every period knob is a parameter edit |
| S.5 lifetime + matched comparison | **STRONG** | Competitive exclusion within ~5–7 turbidostat generations (LD 12:12 wild type 52%→100% by 6.8 generations) with LL control and genetic rescue; per-cell clock-phase-dependent irreversible arrest; ΔrpaA CFU lethality in LD but not LL with complementation controls |
| Reading A (strict autonomy) | **UNCLEAR** | Demonstrated in vitro where no regulated variable exists; three y→x paths in vivo where S.5 lives |
| Reading B (scale separation) | **YES** | All three requirements verified in primaries |
| Target-as-state / parameter | **STATE** | Phase is a state (Rust 2007 Fig. 1C; Rust 2011 reversible ADP step); period is a parameter (Terauchi 2007 ATPase) |
| Role recommendation | **POSITIVE_ARTICLE** (caveated) | Cannot be the negative control — it has a separably addressable target, which is exactly what a model-free corrector lacks |

**One line for the pairing seat.** This candidate is strong on S.1/S.2/S.3/S.5 and honest-partial on S.4; its advertised strict-Reading-A advantage is real only in a preparation that has no viable set, and the environmental-model objection in §8 is live and evidenced on both sides. It is a positive article, not a control.
