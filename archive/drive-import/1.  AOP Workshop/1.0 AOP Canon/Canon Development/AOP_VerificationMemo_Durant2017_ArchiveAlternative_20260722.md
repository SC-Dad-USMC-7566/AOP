# Verification memo — Durant et al. 2017 and the archive alternative (Claim A)

**Prepared by prime, 22 July 2026.** Companion to `AOP_CandidateNote_BioelectricPatternMemory_v0.1`
and its `RevisionRecord_v0.2`. Subject: the standing retraction condition on **Claim A** — the proposal
that bioelectric pattern memory is a *third memory register*, metastable, drive-maintained, externally
rewritable, sitting in neither the robust archive nor the transient effector layer.

**Source read status: FULL TEXT ✓.** Durant F, Morokuma J, Fields C, Williams K, Spencer Adams D,
Levin M. "Long-Term, Stochastic Editing of Regenerative Anatomy via Targeting Endogenous Bioelectric
Gradients." *Biophysical Journal* 112(10):2231–2243 (2017). doi:10.1016/j.bpj.2017.04.011.
Read in full from the PDF in the AOP source library (Drive `18cNGT7CBJIV-zUCtjYXQ-iD7laLO3pi5`,
file `1q4-v_4MTrRfwztA97ToTWDsXu4EnzZJq`): Abstract, Materials and Methods, Results, Discussion,
reference list. Supplementary figures S1–S6 and Table S1 were **not** retrieved (hosted separately);
nothing below rests on them, and where a supplement is load-bearing it is flagged.

**Startup check — 22 July 2026**
- [✓] AOP Charter — v1.2
- [✓] AOP Canon — v1.20 (current; **not re-read this session** — this memo touches no canon claim, it
  grades a *candidate* claim that has not entered canon)
- Drive connector: on

---

## 0. Bottom line

**The retraction condition is not resolved by Durant 2017, and the paper does not attempt to resolve
it. It says the opposite of exclusion.** In the Discussion the authors state that bioelectric signaling
operates together with downstream target genes and chromatin modifications, and that additional
components of the double-head effect **likely** include other epigenetic mechanisms integrating with
bioelectrics. They then explicitly set the question aside — their stated contribution is that the
molecular genetics can be *bypassed* as a control point, regardless of which genes or epigenetic
mechanisms are involved.

So the position is worse for Claim A than "unresolved." The load-bearing source affirmatively declines
the exclusion and records the co-varying archive as probable. Claim A's central content — the *location
of the store* — is unsupported by the paper it was built on.

**Recommended grade change: Claim A drops from "SYNTHESIS (structure) + SETTLED-pending (empirical
anchor)" to FRONTIER / unsupported-as-stated.** Not retracted — nothing falsifies it — but it cannot
enter canon at any grade that implies the register question has been settled empirically.

---

## 1. The complete assay list (the thing the abstract summarises and the Methods specifies)

The abstract's control claim is that cryptic animals do not differ from wild-type in histology,
expression of key polarity genes, or neoblast distribution. The Methods and Results give the actual
panel behind that sentence. It is:

| Assay | Target | Layer probed |
|---|---|---|
| Whole-mount in situ, PC2 | CNS marker | transcript |
| Whole-mount in situ, 0821_HN | anterior fringe sensory cells | transcript |
| Whole-mount in situ, 1008_HH | brain branches | transcript |
| Whole-mount in situ, *ndk* | earliest anterior specification marker | transcript |
| Whole-mount in situ, *frizzled-T* (FzT) | posterior/tail Wnt receptor, quantified | transcript |
| Immunofluorescence, anti-phospho-histone H3 (H3P) | mitotic neoblast distribution | cell distribution |
| DiBAC4(3) voltage reporter | membrane resting potential | physiology |

That is the whole molecular panel: **five in-situ probes, one mitotic-cell marker, one voltage dye.**

**No chromatin assay. No DNA-methylation assay. No ChIP, no ATAC, no bisulfite, no transcriptome-wide
measurement of any kind.** Every molecular control is a targeted transcript readout in the *uncut*
animal, plus a proliferation stain.

This matters because the archive alternative predicts exactly this result. A poised or bivalent
chromatin state — or any mark that is transcriptionally silent until amputation triggers the patterning
cascade — leaves a five-probe in-situ panel of the resting animal looking wild-type. **The controls do
not discriminate the two hypotheses; they were never designed to.** The authors are careful about this
in one place and it is worth recording: on *ndk* they note it cannot be ruled out that differences would
be found using as-yet undiscovered anterior determinant genes.

---

## 2. What the paper does establish (and it is substantial — this is not a weak paper)

Stated telos-free, the results are clean and I do not want the negative verdict above to obscure them:

1. **A 48-hour gap-junction blockade (octanol, 8-OH, washes out of tissue in 24 h by GC-MS) produces a
   permanent change in regenerative outcome.** Double-heads recur through repeated recuts in plain
   water over months, and through spontaneous fission (100%, N=100).
2. **The apparent "escapees" are not escapees.** Morphologically normal regenerates recut in plain
   water up to eight weeks later give 23% double-heads (N=155). Wild-type gives 0%.
3. **The ratio is fixed and re-treatment does not move it** — 25% DH / 72% cryptic on first treatment
   (N=593), 24.5% DH on a second 8-OH exposure of cryptics (N=439).
4. **The decision unit is the fragment, not the animal.** Two transverse pieces of one worm can take
   different patterning fates. (This is the observation that re-anchored Claim D in RevisionRecord v0.2;
   the full read confirms it.)
5. **Voltage overrides an already-committed transcriptional state.** 8-OH applied days 2–5, *after* tail
   markers are expressed, abolishes or diminishes FzT expression by day 5.
6. **Cryptic worms carry a distinguishing physiological signature.** Cryptics show an ectopic
   depolarized posterior region; wild-type tails are significantly hyperpolarized relative to heads
   (p<0.01), cryptic tails are not (p>0.05).
7. **The state is bidirectionally rewritable.** Hyperpolarization with the H,K-ATPase inhibitor
   SCH-28080 resets 34% of double-heads (N=102) to a single-head state stable across at least four
   generations of recuts, while DMSO controls stay 100% DH.

Points 1, 2, 5 and 7 are strong and I have no quarrel with them. **Vmem is demonstrably a sufficient
control point that writes and resets a heritable morphological outcome.** That is the finding.

---

## 3. Why that does not establish Claim A

Claim A is not a claim about a control point. It is a claim about **where the state is stored** — that
the store is a metastable, drive-maintained physiological variable rather than an archive. The paper
supports sufficiency of the *lever* and does not address identity of the *store*.

Two readings survive every experiment in the paper:

- **(i) Vmem is the register.** Voltage pattern is the store; it is held against leak by pumps at a
  housekeeping cost; regeneration reads it.
- **(ii) Vmem is the write-head on an archive.** Voltage change induces a chromatin state in trunk
  cells; the chromatin state is the store; SCH-28080 hyperpolarization re-writes it back.

Reading (ii) reproduces every observation: permanence, the fixed stochastic ratio, the fragment-level
decision, the transcriptional override, the bidirectional reset, and the wild-type-looking in-situ
panel. Nothing in the paper separates them — and the authors' own Discussion leans toward a
both/integrated version of (ii).

**Three further limitations from the full read that specifically weaken (i):**

- **The voltage measurement is superficial.** DiBAC4(3) imaging is explicitly limited to the outermost
  few cell layers, at most ~50 µm, due to tissue opacity and pigmentation. The authors state the
  prepattern exists *at least* in surface tissues and that identifying which cell types store the
  bioelectric state awaits transgenic voltage reporters. So the store's location is unknown even within
  reading (i).
- **The reset is 34%, not near-complete.** Two-thirds of double-heads treated with SCH-28080 stayed DH.
  A register you can only rewrite a third of the time is a weaker claim to being *the* register than
  the "reset it back" framing suggests.
- **The authors' own mechanistic model is a signalling model, not a storage model.** The Fig. S6 model
  attributes the cryptic state to breakdown of a continuously-transmitted anterior→posterior memory
  signal that actively suppresses stochastic competition — and it notes such a memory signal requires
  an energy-consuming dynamic process. That is congenial to AOP's drive-maintained framing, but it is a
  *model output*, not a measurement, and it is in a supplementary figure I did not retrieve.

---

## 4. Can the archive alternative be closed from existing literature?

**On my search: no, and there does not appear to be a study that would close it.** I found no chromatin
or methylation profiling of cryptic-versus-wild-type or two-headed-versus-wild-type planaria. The
planarian epigenomics literature that exists (ChIP-seq for bivalent histone marks; NuRD, PRC, SET1/MLL,
PIWI work) is about neoblast pluripotency and differentiation, not about pattern memory.

One partial narrowing, with a caveat that blocks it from transferring cleanly:

- The planarian epigenetics literature reports a **lack of endogenous DNA methylation in *Schmidtea
  mediterranea***. If that held for Durant's animal it would eliminate methylation as an archive
  candidate. **But Durant used *Dugesia japonica*, a different species,** so the finding does not carry
  over without a species-specific check. I have not verified the methylation status of *D. japonica*.
- Even granting it, this only removes one branch. **Histone/chromatin state remains fully live** — and
  it is the branch the authors themselves name as likely.

So the archive alternative splits into (a) DNA methylation, possibly constrained but not for this
species, and (b) histone/chromatin state, entirely open and endorsed as probable by the source.

**Anticipated counter, and why it fails.** Levin's 2016 review argues the memory must be distributed
through the trunk, because the reprogrammed blastema is discarded at each round of cutting and only
trunk fragments are taken. That is a good argument about *where* the memory sits. It says nothing about
*what medium* holds it — chromatin in trunk cells satisfies it exactly as well as voltage in trunk
cells. It does not rescue Claim A.

**What would settle it:** chromatin profiling (ATAC-seq and/or histone ChIP-seq, plus a methylation
assay if *D. japonica* has methylation) on cryptic versus wild-type **trunk** tissue, ideally with a
SCH-28080-reset arm to test whether the mark reverts with the phenotype. Nobody has run it. This is an
experiment, not a literature search — which means **the retraction condition on Claim A is not
resolvable from the published record at all.**

---

## 5. Consequence for the candidate note

- **Claim A — downgrade.** The empirical anchor does not support the register location. Restate the
  retraction condition as *unresolvable from existing literature* rather than *unresolved pending a
  read of Durant*. The read has now happened; that route is closed.
  - A weaker claim does survive intact: **Vmem is a sufficient, bidirectional control point over a
    heritable morphological state.** But that is control-point content, and it largely collapses into
    Claim B and Claim C territory rather than earning a separate memory-register claim.
  - Note what the archive alternative costs specifically: the property that made Claim A *interesting*
    to AOP is that the store **buys editability with continuous dissipation** — a Cμ store held above
    its own floor by drive. A chromatin mark is a quasi-static archive and is not drive-maintained in
    that sense. So if (ii) is true, Claim A does not merely lose its anchor; it loses the exact feature
    that made it worth having. It would be an ordinary epigenetic archive with a physiological write-head.
- **Claim B — unaffected**, and this read strengthens the prior expectation recorded in candidate-note
  §11 that B is the claim most likely to survive. It rests on the electrophysiology of a maintained
  contrast held against leak, not on the patterning interpretation.
- **Claim C — unaffected as *illustration, not test*.** Note the reset is 34%-penetrant; if C is ever
  written up, that number goes in.
- **Claim D — confirmed at the observation level.** The fragment-as-decision-unit result is in the
  primary text (Fig. 1D), not only in Pezzulo's review of it.
- **Claim R — unaffected.** The cite-figures-not-interpretations rule performed exactly as designed
  here: every result in §2 above is statable with no goal language, and every one of them survived.

---

## 6. Verification status and what I did not do

- Durant et al. 2017 — **full text read ✓ this session** (main article). **Supplementary figures S1–S6
  and Table S1 not retrieved (~)** — Fig. S6 (the model) and Table S1 (paired Vmem statistics) are the
  two that would matter for any further claim.
- The *D. japonica* DNA-methylation status — **unverified (?)**. Flagged, not relied on.
- The absence of a chromatin-profiling study on cryptic worms — **a negative from a bounded search,
  not a proof of absence.** Graded accordingly. An evaluator should re-run this before the negative is
  treated as settled.
- Levin 2016 review (*Regeneration* 3:78–102) — **snippet-level only (~)** for the
  discarded-blastema/distributed-memory argument in §4.

**Prime wrote this memo and does not bless it.** Independent verification required per the charter:
whoever checks it should confirm (a) the assay list in §1 against the Methods, and (b) the Discussion
sentence in §0 against the primary text, since the whole verdict turns on those two.

---

## 7. The pattern, recorded

This is the fourth walk-back in this arc, and it has the same shape as the three from the previous
session — Sacco, Srivastava, Pezzulo. In each case a claim was carried on an abstract, and the abstract
was written to sell an interpretation the body of the paper is more careful about.

Durant's abstract says the altered bodyplan **is stored** via global patterns of cellular resting
potential. Durant's Discussion says chromatin involvement is **likely** and that the genetics were
**bypassed**, not excluded. Both sentences are in the same paper. Only one of them is in the abstract.

The operational rule already on the record — cite figures and measurements, never interpretations —
should be extended by one clause: **in this literature, the abstract is an interpretation.** Treat it
as such. The controls a paper actually ran are in the Methods, and they are frequently narrower than
the abstract's summary of them implies.

*— prime, 22 July 2026.*
