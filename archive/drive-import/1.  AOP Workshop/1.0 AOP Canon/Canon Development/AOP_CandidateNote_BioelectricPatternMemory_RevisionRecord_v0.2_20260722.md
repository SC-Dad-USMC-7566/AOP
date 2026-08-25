# Revision record — candidate note v0.1 → v0.2, after reading Pezzulo et al. 2021 in full

**Prepared by prime, 22 July 2026.** Attaches to
`AOP_CandidateNote_BioelectricPatternMemory_v0.1_20260722.md`. Read this before evaluating that note;
it corrects a load-bearing assumption in it. Pezzulo, LaPalme, Durant & Levin 2021, *Phil. Trans. R.
Soc. B* 376:20190765 — **full text read this session ✓**.

---

## 1. The correction that matters

**v0.1 assumed Pezzulo 2021 was the telos-free formulation of the Memory result, and said so twice —
once as "load-bearing for the telos-free formulation," once as the paper that "would become the
preferred citation throughout." That was wrong, and it was asserted from the abstract.**

The paper is a **review in a theme issue titled "Basal cognition: multicellularity, neurons and the
cognitive lens."** Subject area as printed: *cognition*. Keywords include *cognitive science*. Its
argumentative spine is an extended analogy chain — planarian regeneration → hippocampal attractor
networks → theta flickering → Bayesian generative models → variational autoencoders — and it states
outright that regeneration works because tissues "exploit bioelectric encoding of **distributed goal
states**." §§4–8 are the analogy. The telos is not decoration here; it is the paper's thesis.

So Pezzulo is **more** thickly framed than Durant, not less. There is no clean paper to reach for.

## 2. What the paper nevertheless delivers — and it is more than expected

Two items of real value, both of which are **measurement or observation, not interpretation**:

**(a) §9 and figure 4 — an original experiment, not review material.** Intact *D. japonica* treated 3
days with 0.27 µM Nigericin (K⁺ ionophore) + 15 mM K-gluconate, washed out, cultured in plain water at
13 °C, then imaged with the voltage-sensitive dye DiBAC₄(3) at **one week and three weeks**. Both
treated groups were significantly depolarized relative to untreated controls (p < 0.01, Student's
t-test), with no significant difference between the one- and three-week groups.

This matters more than v0.1 anticipated. It is **direct measurement of the persistent bioelectric state
itself**, not merely of its anatomical consequence. Claim A needs exactly this: evidence that the store
is the bioelectric variable and that it holds for weeks with no reinforcement. Caveats stated plainly:
n is not given in the text read, it is a t-test, an ionophore is a blunt instrument, and the authors'
gloss that the pattern "gets stronger" between one and three weeks is read through a
memory-consolidation metaphor when slow relaxation toward a new steady state is an equally available
reading. **Cite the measurement, not the consolidation story.**

**(b) Figure 1c — a discrete state-transition diagram, entirely telos-free.** Wild-type worms treated
with octanol become either **Cryptic** or **double-headed**. Cryptic worms have normal one-headed
anatomy but on each recut produce double-headed offspring at roughly 25–30 %, indefinitely. Double-
headed is **absorbing** — once DH, always DH. Both Cryptic and DH can be reset to wild-type by
SCH-28080. That is a clean multistable transition structure with an absorbing state and a stochastic
state, and it requires no goal language whatsoever to state.

**(c) A framing the authors supply themselves, which AOP can use as-is:** the phenomenon is "an example
of epigenetics in Waddington's original sense of the term: **a non-genomic, re-writable medium for
information that controls growth and form.**" That sentence is Claim A without the telos, in the
source's own words.

## 3. Two findings that change the note's substance

**3.1 The bistability is at the level of the collective, not the cell — and this is a better anchor for
Claim D than what v0.1 used.** The paper reports that each fragment makes an independent decision
("coin flip"): two pieces from the same worm need not agree. But **within** a fragment there are no
mosaic outcomes — no worms where 70 % of cells build one head and 30 % build two. Every cell in the
fragment goes with the group. The stochasticity is at the population level; the coherence is at the
fragment level. The same pattern is reported for left–right identity and for melanocyte conversion,
where whole tadpoles rather than individual cells transform.

**The unit of decision is the fragment.** That is an individuation observation, directly on §9/§9a, and
it is a stronger and cleaner Claim D anchor than the gap-junction/cancer story v0.1 leaned on. Revise
Claim D accordingly.

**3.2 Claim A is less novel to biology than v0.1 implied — downgrade its novelty, not its usefulness.**
The paper places the phenomenon in an existing lineage: **ciliate cortical inheritance** (Beisson 2008;
Pilling et al. 2017), **bacterial persistence as a phenotypic switch** (Balaban et al. 2004, *Science*;
Kussell et al. 2005), and **attractor states in cancer regulatory networks** (Huang & Ingber 2006).
Non-genomic, bistable, heritable state is an established phenomenon class with a literature that has
nothing to do with Levin.

Consequence: **AOP's contribution is not the discovery of a third register — it is the placement of a
known register on the axes.** v0.1 read closer to discovery than it should have. Charter discipline
("be skeptical of anything that looks new") applies to prime's own framing here. The good news is that
the independent lineage makes the empirical base much sturdier than a single lab's result — Balaban
2004 in particular is a high-profile, widely-replicated anchor outside the bioelectric field entirely.

**Also soften the crypticity point.** v0.1 noted that the authors independently arrived at the word
"cryptic." In fact *Cryptic* is their proper name for one specific state. The mapping to χ = Cμ − E is
still apt — a Cryptic worm has normal anatomy and behaviour, carries hidden state, and discloses it
only under intervention — but state it as an analogy AOP draws, not as convergent vocabulary
vindicating the framework.

## 4. The import protocol — answering "can we take it without the baggage?"

**Yes, but not by finding a clean source. There isn't one, and there structurally won't be.** This
literature is published in cognition venues because the cognitive framing is what places and funds it.
What exists is telos-free *observations* inside teleological *papers*.

Proposed standing rule, to sit under Claim R:

> **Cite figures and measurements; do not cite interpretations.** From this literature AOP imports
> state-transition structures, voltage measurements, penetrance ratios and reset experiments. It does
> not import the analogy chains that surround them. Where a source's own non-cognitive framing exists —
> e.g. Waddington-sense epigenetics as a non-genomic rewritable medium — prefer it. Every import is
> restated in dynamical-systems terms before use, and the restatement is checked against the figure to
> confirm it preserves the observation.

Applied to Pezzulo 2021 specifically: **cite figure 1c, figure 4, and §9. Do not cite §§4–8.**

## 5. Verification status after this read

| Source | v0.1 status | v0.2 status |
|---|---|---|
| Pezzulo et al. 2021 | unread; assumed telos-free formulation | **read in full ✓; assumption refuted; value relocated to §9/fig. 1c/fig. 4** |
| Durant et al. 2017 | abstract only | unchanged — **still the single most important read**, and still the only place the histology / polarity-gene / neoblast controls can be checked |
| Balaban et al. 2004; Beisson 2008; Pilling 2017; Huang & Ingber 2006 | not identified | **newly identified as the independent non-Levin lineage for Claim A** — none read |
| Emmons-Bell 2015; Srivastava 2021; Jaeger | unread | unchanged |

**The archive-alternative retraction condition (v0.1 §9) is not resolved by this read.** Direct voltage
measurement shows the bioelectric variable itself carries a persistent difference, which is necessary
but not sufficient — it does not exclude a chromatin or methylation correlate co-varying with it.
Durant 2017 remains the place to check, and it stays the first thing a verifier should do.

## 6. Net effect on the candidate note

- **Claim A** — empirical support **strengthened** (direct voltage persistence at 3 weeks; independent
  non-Levin lineage); **novelty downgraded** (the register is known; AOP's contribution is placement).
- **Claim B** — unaffected.
- **Claim C** — unaffected.
- **Claim D** — **re-anchored** on the fragment-as-decision-unit observation, which is stronger than the
  gap-junction/cancer framing.
- **Claim R** — **strengthened, and now has an operational rule** (§4 above). This is the part of the
  note that has gained the most from the read.

Prime wrote this and does not bless it. Independent verification still required, per v0.1 §11.

*— prime, 22 July 2026.*
