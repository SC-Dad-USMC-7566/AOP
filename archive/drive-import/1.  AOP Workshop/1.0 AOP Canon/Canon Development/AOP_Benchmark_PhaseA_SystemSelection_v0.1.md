# AOP External Benchmark — Phase A: System Selection

**To:** Prime (chat seat) and Ben
**From:** Claude Cowork (execution seat)
**Date:** 25 July 2026
**Order implemented:** `TASK_CW_AOP_External_Benchmark_Prereg_20260725.md`, Phase A (§2)
**Status:** **HARD STOP.** Ben picks the system. Phase B is not begun. No AOP quantity has been computed on anything.

---

## 0. Headline, stated first because it changes the decision Ben is being asked to make

I screened four candidate systems against the order's five selection criteria plus two I added at the outset. **All four pass the ground-truth criteria to varying degrees. All four fail on a criterion nobody wrote down**, which emerged from the work and which I am naming here:

> **A.1.8 — Model representational adequacy.** The published dynamical model must (a) represent, as separate species or reactions, each mechanism the answer key scores, so that a knockout is a well-defined operation on the model; and (b) produce an output that maps onto the measured persistence outcome.

Neither half holds for any of the four candidates. Not "holds weakly" — **fails outright, for a systematic reason.**

**The reason, stated once.** Published dynamical models of biological systems are built to explain *molecular* observables — phospho-protein timecourses, reporter expression, metabolite levels. Published knockout ground truth is scored on *organism-level* outcomes — sporulation frequency, growth, survival fraction. Almost no model bridges the two. And modellers include the component they are studying and **lump the rest**: the sporulation models contain KinA and abstract away KinB–KinE; the independence-clean HOG model deleted both upstream branches on purpose and replaced them with a single Hill term. The redundancy that makes the ground truth valuable to us is precisely the structure modellers abstract away, because for their purposes it is noise.

This is a real obstacle, not a retrieval failure. I am reporting it rather than relaxing criterion A.1.4 and proceeding, because relaxing it quietly would produce a benchmark that cannot be executed and would surface as a mess in Phase C.

**Two structural resolutions are available. §6 sets them out; §7 is my recommendation. Ben chooses.**

---

## 1. Criteria applied

The order's five (§A.1), verbatim in intent:

1. External, published ground truth on essential / redundant / synergistic structure, ideally by direct experiment.
2. A measured persistence-like outcome that V can honestly map onto.
3. Perturbation data, single and combinatorial.
4. Tractable state space.
5. Not AOP-contaminated (Schlögl excluded).

Two I added before retrieval began, and flagged to Ben at the time:

6. **A.1.6 — Model/answer-key independence.** The model must not have been fitted to the combinatorial data the answer key is built from. Otherwise AOP recovers numbers the model was built to reproduce, and the key is external in provenance but internal in information — §11b with a citation on it.
7. **A.1.7 — Gate power.** ≥8 scored entries, including ≥2 experimentally established redundant pairs and ≥1 synergistic pair. Below that, a rank or exact-match criterion cannot distinguish AOP from a coin.

One that emerged from the work:

8. **A.1.8 — Model representational adequacy.** As stated in §0.

---

## 2. Scorecard

| | **Sporulation phosphorelay** | **Yeast HOG** | **Yeast GAL** | **E. coli DNA repair** |
|---|---|---|---|---|
| 1. External ground truth | **Strong** — quantitative, replicated across two strain backgrounds | Weak — qualitative plate streaks | Weak — canonical experiment is a *triple*, readout is expression | Moderate — classical, thin, key synergy single-source |
| 2. Measured persistence outcome | **Strong** — heat-resistant spore titre | Weak — binary, eyeballed | Weak — growth ≠ survival; bistable, history-dependent | **Strongest of the four** — survival fraction vs dose |
| 3. Combinatorial data | **Strong** — double *and* triple, quantitative | Present but qualitative | **Absent** for the load-bearing pair | Present, thin, mostly single-source |
| 4. Tractable state space | Pass | Pass | Pass | Pass |
| 5. Not AOP-contaminated | Pass | Pass | Pass | Pass |
| 6. Model/key independence | **Clean** | Split — one clean model, two disqualified | Clean | Clean |
| 7. Gate power (≥8) | **9** | 9 claimed / **4** clean | 8 claimed / **4** with primary quotes | **5 — fails** |
| 8. **Model representational adequacy** | **FAIL** | **FAIL** | **FAIL** | **FAIL** |

---

## 3. Candidate 1 — *Bacillus subtilis* sporulation initiation phosphorelay

**Full evidence:** `bench_candidate_sporulation.md`

### What is strong — and it is the strongest ground truth of the four by a wide margin

The redundancy is quantitative, large, and independently replicated in a different strain background.

**LeDeaux, Yu & Grossman 1995 (*J. Bacteriol.*), Table 1, relative sporulation frequency across three media (23SG / DS / minimal):**

| Genotype | 23SG | DS | Minimal |
|---|---|---|---|
| *kinA* | 0.1 | 0.08 | 1.2 |
| *kinB* | 0.67 | 0.13 | 0.071 |
| *kinA kinB* | 1.9 × 10⁻⁶ | < 5 × 10⁻⁸ | 2.1 × 10⁻⁷ |

A 10⁵–10⁷-fold collapse in the double against near-wild-type or mildly reduced singles. **This is the redundancy signature in its textbook form, measured, not inferred.**

Independently replicated by **Tojo et al. 2013** in strain 168 — a different background: *kinA* 0.26%, *kinB* 0.67%, double "< 5 × 10⁻⁶%".

There is also a genuine **synergistic** entry: *kinC* is near-inert alone (0.77 relative sporulation) but carries all residual sporulation in the *kinA kinB* background — *"the kinA kinB kinC triple mutant produced <10 spores per ml."*

Essentials are clean: *spo0A*, *spo0F*, *spo0B*.

**Count: 9 defensible entries** — 3 essential, a redundant pair (plus the pair itself as an entry), *kinC* as near-inert-alone and synergistic-in-background, and a weak *kinB kinC* synergy in minimal medium. Meets A.1.7.

**Persistence outcome:** heat-resistant spore titre / sporulation frequency. Quantitative, and genuinely a *survival* measure rather than a growth proxy — the closest of the four to what AOP means by lifetime.

**Model/answer-key independence: clean.** Ihekwaba 2014 was fitted only to wild-type IPTG timecourses. Narula, Devi, Fujita & Igoshin (*PNAS* 109(50):E3513, 2012) took parameters "from the literature" with no fitting. No model has ever been fitted to combinatorial knockout data.

### Why it fails A.1.8

| Model | KinA separate? | KinB? | KinC? | `kinA∆` definable? | Outputs spore titre? |
|---|---|---|---|---|---|
| Ihekwaba 2014 | Yes | **No** | **No** | Degenerate only | **No** |
| Narula/Igoshin 2012 | Yes | **No** | **No** | Not as published | **No** |
| Bischofs/Arkin 2009 | **No — lumped κ** | No | No | **No** | **No** |
| Gauvry 2019 | *no molecular species at all* | — | — | **No** | **Yes** |
| Jabbari 2011 | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN | UNKNOWN |

Ihekwaba is explicit: *"Out of the five kinases identified as capable of initiating sporulation in B. subtilis, we have considered KinA, the major kinase responsible for initiation of sporulation in our model."*

**Two independent disqualifiers.** (1) No published model contains KinB as a species. `kinB∆` has no referent, so the *kinA kinB* double — the single strongest fact in the ground truth — cannot be expressed as a perturbation of any published model. (2) Mechanism and observable are disjoint: every mechanistic model outputs Spo0A~P or sigma-factor or transcript levels; the only model outputting spore concentration contains no molecular species to intervene on.

### Honest weaknesses beyond A.1.8

- Labels are **medium-, strain- and inoculum-history-conditional**. *kinA* runs from 8% to 120% of wild type across three media *in one table*. Any answer key must fix the medium and say so.
- The "*kinB* single mutant" in LeDeaux is formally a *kinB kapB* double.
- *kinD* and *kinE* are not scoreable — Jiang et al. 2000 was not retrieved by any route.
- The 1995 PDF's text layer mangles superscript minus signs. I decoded them and cross-checked against the paper's own prose, but anyone building the key must confirm against the printed PDF.
- **Burbulys, Trach & Hoch 1991 was NOT retrieved** — the canonical relay architecture paper. Architecture was established instead from Quisel, Burkholder & Grossman 2001. The citation metadata is Crossref-verified; not one word of its text was read.

---

## 4. Candidate 2 — *S. cerevisiae* HOG osmostress pathway

**Full evidence:** `bench_candidate_hog.md`

The two-branch redundancy is real and cleanly attested — **O'Rourke & Herskowitz 1998** (*Genes Dev* 12:2874, full text retrieved) has `ssk1`, `sho1`, `ste50`, `ste20` singles growing "equally well on YEPD and YEPD + NaCl plates", the `sho1 ssk1` and `ste50 ssk1` doubles osmosensitive at 1 M NaCl, **and a same-branch negative control**: `ste50 sho1` "was as osmoresistant as the *ste50* and *sho1* single mutants." A negative control inside the ground truth is a genuine asset and no other candidate has one.

**But the readout is a qualitative eyeballed plate streak** — "streaked on YEPD, YEPD + 1 m NaCl… to assay growth". No units, no error bars. Quantitative data exists (Martin 2015 E-MAP S-scores; Petelenz-Kurdziel 2013 doubling times) but **neither covers any branch-deletion double mutant**. No survival-fraction measurement exists anywhere in this system.

A genotype correction worth recording: **Saito & Posas 2012** shows `ssk1∆` and `ssk2∆ ssk22∆` are *not* interchangeable — "osmostress does cause slight activation of the Hog1 MAPK in *ssk1*Δ *sho1*Δ mutants" while "no activation is observed in *ssk2*Δ *ssk22*Δ *sho1*Δ mutants". The canonical null is a triple, and the signalling and growth readouts **disagree** for `ssk1∆ sho1∆`.

`hog1∆` and `pbs2∆` are excluded from the count — Brewster 1993 was unretrievable, so there is no quoted phenotype passage for either. Clean core: **4 entries.** Fails A.1.7.

### Why it fails A.1.8 — and this one is self-documenting

The only model with a certifiable wild-type-only fit is **Zi, Liebermeister & Klipp 2010**. Its authors describe what they removed:

> "Although our previous comprehensive model contained a phospho-relay system, in which the SLN1 and SHO1 branches sense the osmotic stress signal and both activate the MAPKK, Pbs2. Here, we simplified and modeled the phosphorylation of Pbs2 with a Hill function using turgor pressure as input."

There is no Sln1, Ypd1, Ssk1, Ssk2, Ssk22, Sho1, Ste11, Ste20, Ste50, Msb2 or Hkr1 in it. Zeroing the single Hill term destroys both branches at once — that is `pbs2∆`, not a branch deletion. The model contains no variable on which `sho1∆`, `ssk1∆` and `ssk1∆ sho1∆` differ. And it outputs phospho-Hog1, nuclear Hog1, glycerol, volume and turgor — never growth: *"we ignore the effect of cell growth on the volume change during the time scale of osmo-adaption."*

Schaber 2011 and Schaber 2012 **were** fitted to branch-deletion data and are disqualified on A.1.6. So the criteria are satisfied by **disjoint model sets**, and criterion (b) — growth output — is satisfied by none of them.

---

## 5. Candidates 3 and 4 — briefly, both fail earlier

**GAL network** (`bench_candidate_gal.md`). The load-bearing redundancy claim does not survive retrieval. **No primary passage describing a `gal1∆ gal3∆` double deletion was retrievable anywhere.** The canonical experiment (Torchia & Hopper 1986) is a **triple** — *"A strain of genotype gal3 gal1 gal7 is noninducible for MEL1 gene expression"* — with an **expression** readout, complemented by the whole plasmid-borne GAL1-10-7 cluster, so the second induction pathway is *not resolved to GAL1*. The confound I asked about is real: `gal1∆` fails to grow on galactose for a purely catabolic reason (*"did not grow better in 2% galactose than it did without any carbon source"*), and the literature's disentangling strategies exist but were demonstrated in overproduction assays, not lag-rescue. Compounding it, bistability makes "grows on galactose" history-dependent, so the label is undefined without specifying pre-growth carbon source. On A.1.8: Ramsey et al. 2006 *excludes Gal1p feedback by design* — *"we did not include its weak potential feedback role in the model"* — so the one model that could represent the redundancy deliberately does not. **Fails at criterion 3 before A.1.8 is reached.**

**E. coli DNA repair** (`bench_candidate_dnarepair.md`). This candidate has the best *readout* of the four — survival fraction against dose — and it recovered the thing I most wanted: the field's own operational definition of redundancy versus synergy, in **Kuzminov's EcoSal Plus** chapter, including the critical gloss that an *"additive" (actually, multiplicative)* double means separate pathways. That definition is a genuine asset and I would reuse it wherever this benchmark lands.

But it fails twice. **A.1.7:** only 5 mechanisms carry a settled label. **A.1.8, decisively: zero of nine models predict survival fraction.** Every one outputs promoter-GFP activity, LexA/RecA/ssDNA levels, or mutation counts. And the ground truth itself is thinner than its reputation — only two sources put singles and a double on the same quantitative axis, only *recA* is replicated (and the two replicates are 4× apart), and the famous *uvrA recA* synergy rests on one sentence in one 1969 abstract. Also: *phr* is **not** a clean spectator in the dark — three sources show dark effects mediated through *uvrA*.

---

## 6. The choice Ben is actually being asked to make

The order asked me to recommend a system. The honest state of play is that the recommendation has to come with a structural decision attached, because no candidate is executable as the order is written.

### R1 — Keep the sporulation system; a separate seat builds the model blind

Take the *B. subtilis* phosphorelay, whose ground truth is the strongest of the four and the only one meeting A.1.7. Have a seat that **has not seen the answer key** build a mass-action phosphorelay model from published biochemistry — relay stoichiometry from the primary architecture literature, KinA / KinB / KinC as separate parallel phosphate donors to Spo0F, literature rate constants where they exist — and freeze it. Only then does AOP compute on it.

**Why this preserves the ability to fail, which is the whole point.** A mass-action model with KinA and KinB as parallel donors does **not** automatically reproduce a 10⁵-fold collapse in the double. Whether it does depends entirely on the kinetics and on where the Spo0A~P threshold sits. Two parallel donors with the wrong relative fluxes give a double mutant that is merely additive, not catastrophic. **AOP can genuinely fail this**, and so can the model.

**What it costs.** It adds a seat and a freeze to the order's structure — a governance change, and therefore Ben's and Prime's call rather than mine. It also means the model's parameters are chosen by us where the literature is silent, which the B.6 robustness sweep must cover rather than paper over.

**The contamination risk, named.** I have now read the answer key. I must not be the seat that builds the model. The builder should receive the wiring papers and nothing else — specifically not LeDeaux 1995 or Tojo 2013.

### R2 — Change system class: find one where the model's output *is* the measured quantity

The failure is systematic, so the fix might be to select against it directly: look for systems where the published model predicts the same population-level quantity the experiments measure. My best untested lead is **phage λ lysis–lysogeny** — the Arkin/Ross/McAdams stochastic model outputs *lysogenization frequency*, which is exactly what the mutant experiments measure, and cI/cro/cII/cIII are separate species with published mutant phenotypes. Whether it carries a redundant pair and a synergistic pair is unknown to me and would need a Phase A round two.

**Cost:** another retrieval cycle before anything freezes. **Benefit:** if it holds, the benchmark is executable without adding any seat or building anything.

### R3 — Proceed on a shrunken scored set

Score only the entries a published model can represent. I record this for completeness and recommend against it: for every candidate, the entries the models *can* represent are exactly the ones with no redundancy or synergy in them. The scored set collapses to the essentials, where a strength-based rival does fine, and the gate stops being able to separate AOP from the rival at all. This is the option that produces a benchmark that cannot fail *and* cannot inform.

---

## 7. Recommendation

**R1, on the sporulation phosphorelay** — with R2 run in parallel as a hedge if Ben wants the option of avoiding a built model entirely.

Reasons, in order of weight:

1. **The ground truth is the best available and it is not close.** A 10⁵–10⁷-fold effect, quantified, replicated in a second strain background by a different group, with a redundant pair *and* a synergistic third member. Nothing else I screened has both, quantitatively.
2. **The persistence outcome is a survival measure**, not a growth proxy — heat-resistant spore titre is close to what AOP means by lifetime, and closer than growth-on-galactose or optical-density growth under salt.
3. **Model/answer-key independence is clean**, and would remain clean under R1 by construction.
4. **It meets the power threshold at 9 entries** where HOG and GAL meet it only nominally and DNA repair fails it.
5. **The rival's predicted failure is easy to state in advance and genuinely uncertain.** A coupling-strength or flux read on the phosphorelay should rank KinA above KinB (KinA is "the major kinase" by every account) and should rank both above the near-inert KinC — and should therefore **miss that KinA and KinB are jointly essential while individually dispensable**, and miss KinC's synergistic role entirely. That is a sharp, pre-registerable prediction about the rival that could itself turn out wrong.

Against it, recorded honestly: the model must be built rather than taken off the shelf, and the labels are medium-conditional in a way the declaration must pin down.

**If Ben prefers not to build a model at all**, R2 is the right path and I should run Phase A round two on phage λ and one or two comparable systems before anything freezes.

---

## 8. What I have NOT done

- **No answer key has been written.** Order §A.3 puts that after Ben's pick. The retrieval files contain the raw material for one, but they are candidate evidence, not a frozen key, and should not be treated as one.
- **No AOP quantity has been computed on anything.** Phase B is not begun and nothing is hashed.
- **No pre-registration exists.** Nothing to freeze yet.

## 9. Retrieval limitations affecting this phase

The Nimble CLI was absent in this environment, so all four candidates were worked with WebSearch/WebFetch only. Blocked throughout: PubMed/PMC (reCAPTCHA), NCBI E-utilities (robots), ScienceDirect, cell.com, science.org, PNAS, JBC, Wiley, ASM full text, and **BioModels** (403 then persistent 429). The WebSearch budget was exhausted on three of the four candidates.

**Three specific gaps that matter and are unclosed:**
- **BioModels was never reached.** Its entries list species explicitly, which is the direct way to settle A.1.8 for any model. This is the single most valuable unfulfilled check in this phase.
- **Jabbari 2011** (sporulation) internals remain unread after five blocked routes. It is the one model that could in principle overturn the sporulation A.1.8 verdict.
- **Burbulys, Trach & Hoch 1991** — the canonical phosphorelay architecture paper — was not retrieved. If Ben picks sporulation, this must be read before the answer key freezes.

Every quotation in the underlying reports passed through WebFetch's summarising layer rather than direct transcription. They are reported-verbatim, not keystroke-verified. Under the project's standing rule that is **not** verification, and Prime's line-check applies to the answer key when it is written, not to this selection document.

---

**HARD STOP. Ben picks the system, and rules on R1 / R2 / R3. Phase B does not begin until then.**
