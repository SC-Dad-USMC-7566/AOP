# Candidate canon note — Bioelectric pattern memory: a third register, and what it does to the four axes

**Status: PROPOSAL. Not canon. Not blessed.** Written by prime, 22 July 2026, against canon v1.20 and
charter v1.2. Prime wrote this and therefore does not grade it — it requires an independent verifier
who re-reads the sources, and an adversarial pass, before any part of it folds. Nobody grades their own
homework.

---

## 0. The blocking condition — read before evaluating anything below

**This note proposes canon content on a literature prime has largely not read.** That is a defect, and
it is stated here rather than buried.

| Source | Role in this note | Read status |
|---|---|---|
| Durant, Morokuma, Fields, Williams, Adams & Levin 2017, *Biophys. J.* 112:2231–43 | **load-bearing for Claim A** | abstract + results-figure text only (~) |
| Pezzulo, LaPalme, Durant & Levin 2021, *Phil. Trans. R. Soc. B* 376:20190765 | **load-bearing for the telos-free formulation** | **unread**; bibliographic record confirmed |
| Emmons-Bell et al. 2015 | supporting, Claim D | **unread** |
| Srivastava, Kane, Harrison & Levin 2021, *Bioelectricity* 3(1):42–67 | would establish breadth of the Vmem base | abstract only |
| Biswas, Manicka, Hoel & Levin 2021, *iScience* 24:102131 | supporting, Claim D | abstract only |
| Sacco, Sakthivadivel & Levin 2026, *Phil. Trans. R. Soc. A* 384:20250011 | supporting, Claim D | **full text read ✓** |
| Jaeger, "Why TAME is lame" | the standing critique | **unread** |

**Consequence for evaluation.** What follows is a proposed *structure* — how these results would sit in
the framework if they hold as their abstracts describe. The structure is the contribution and can be
assessed on its own terms now. **No citation here may enter the canon at its stated grade until someone
has read the paper.** §7 lists exactly what must clear.

---

## 1. What is proposed

| # | Claim | Proposed grade | Placement |
|---|---|---|---|
| **A** | Bioelectric pattern memory is a **third memory register** — metastable, drive-maintained, externally rewritable — sitting in neither the robust archive nor the transient effector layer | SYNTHESIS (structure) + SETTLED-pending (the empirical anchor) | §5 (Memory), and the archive/effector discussion |
| **B** | In this system **Boundary, Drive and Memory are carried on one degree of freedom** (Vmem), giving E14's computed B4 an empirical face | SYNTHESIS | §2 Table 1 / §4 (D→B edge) / case gallery |
| **C** | §11a's separately-interventable set-point criterion has an **empirical instance**: a reference that is readable, rewritable, and rewritable back with the genome untouched | SYNTHESIS — *illustration, not test* | §11a |
| **D** | Inter-cell coupling is a **physical knob on the level-selection crossover**, and therefore a candidate external ground truth for a could-fail benchmark | FRONTIER — proposed, bridge unbuilt | §9/§9a, benchmark programme |
| **R** | A **stated refusal**: AOP declines the goal-directed reading of these results and restates each in dynamical-systems terms | REFUSAL (governance of vocabulary, owns no empirical claim) | §3 refusals |

---

## 2. The empirical base, stated telos-free

Everything in this section is a restatement of published results with the goal-language removed. Where
the removal changes what is being claimed, that is flagged.

**The core result (Durant et al. 2017).** A transient perturbation of a planarian's bioelectric state
produces animals that regenerate with altered head morphology. The altered pattern is **persistent
across subsequent rounds of amputation and regeneration in plain water**, with no further intervention.
Animals that regenerate with apparently normal morphology nonetheless carry the alteration — recutting
reproduces the same ratio of double-headed outcomes. The authors call this a *cryptic phenotype*. The
carriers reportedly do not differ from wild-type in histology, expression of key polarity genes, or
neoblast distribution. The state can be driven back by a hyperpolarizing H⁺,K⁺-ATPase inhibitor.

*Telos removed:* the standard framing is "the worm remembers a different target morphology." What is
observed is a **bistable (or multistable) dynamical system whose selected attractor can be switched by
an external perturbation and which retains the selection across large perturbations to the substrate.**
Pezzulo et al. 2021 reportedly gives exactly this formulation — hence its load-bearing status here.
Nothing in the observation requires a goal, a target, or a stored description of an endpoint.

**The maintained variable (Vmem).** Resting membrane potential is a contrast in ion concentration across
a membrane, held against passive leak by ATP-consuming pumps, principally Na⁺/K⁺-ATPase. This is
standard electrophysiology and is **SETTLED** independent of anything in the developmental-bioelectric
literature.

**Inter-cell coupling (gap junctions).** Gap junctions electrically and small-molecule-wise couple
adjacent cytoplasms. Coupling strength is externally manipulable, pharmacologically and genetically.
Also SETTLED as physiology; the *consequences* claimed for patterning are not.

---

## 3. Claim A — the third memory register

### 3.1 The current canon picture

Canon holds that life partitions into a **robust archive** (DNA; Schrödinger's aperiodic crystal) and a
**marginal effector layer** (proteins, membranes, cytoskeleton), with Drive as the continuous cost of
holding editable structures above their own deep, dead wells; and that robustness and editability are
one axis read in opposite directions, since a potential well resists control inputs and noise equally.
Whether "a marginal machine reading a robust tape" is incidental or constitutive of life is a stated
open question.

### 3.2 What bioelectric memory does to that picture

The store described in §2 fits neither slot:

- **Not the archive.** Genome unaltered; reportedly no difference in polarity-gene expression or
  histology. Whatever holds the state, it is not the tape.
- **Not transient effector state.** It survives complete tissue reconstruction, repeatedly, indefinitely,
  with no reinforcement.
- **Drive-dependent.** It is held by pumps. Remove drive and the contrast decays. It is not a passive
  well the system falls into for free.
- **Externally rewritable, in both directions**, without touching the archive.

Proposed statement: **there is a third memory register — metastable, drive-maintained, and editable —
occupying the position the two-store picture leaves empty.** Its defining property is not that it is
robust *or* labile but that it purchases editability with continuous dissipation. That is a direct
instance of the canon's own robustness/editability identity: a state held at a shallow, actively
maintained minimum is cheap to rewrite precisely because it is expensive to keep.

### 3.3 Why this belongs on the Memory axis specifically

In panel terms this is a **Cμ store with near-zero E**. The alteration is invisible in the ordinary
past→future channel of an undisturbed animal — the carriers look normal and behave normally — and
becomes readable only under intervention (amputation). That is **large crypticity χ = Cμ − E**, and it
is the sharpest physical instance of the E-vs-Cμ distinction folded at Edit E12. The authors arrived at
the word "cryptic" independently, which is worth noting and worth not over-reading: it is convergent
vocabulary, not a citation of the framework.

### 3.4 Consequence for the open question

This does **not** refute "marginal machine reading a robust tape." It shows the two-register split is
**not exhaustive**, and that the interesting biological memory may be the third register rather than
either of the two. That is a sharpening of the open question, not an answer to it. Proposed grade:
SYNTHESIS, with the open question restated rather than closed.

---

## 4. Claim B — three axes on one degree of freedom

Vmem is simultaneously:

- **B1**, a declared interior/exterior state contrast;
- **B4**, a maintenance burden held against leak — and Edit E14's computed σ_hk ≈ ½Δ²g(g+w)/w is
  literally the thermodynamics of this quantity, with the Na⁺/K⁺-ATPase's ~20–45 % resting-cell ATP
  share already cited in canon as B4's empirical face;
- **M**, the register carrying the state of Claim A.

Proposed statement: **in this system the three axes are instantiated on a single physical variable.**

**Anti-overclaim, and it matters.** This is a *coincidence of instantiation*, not an identity of axes.
Edits E1–E4 established the axes are dissociable but not orthogonal; nothing here revises that. The
claim is that a particular persister happens to carry three axes on one variable — which is unusual,
useful for exposition, and exactly the kind of case where the panels can be read against each other on
common ground. It is not evidence that the axes collapse in general, and must not be written as if it
were.

---

## 5. Claim C — §11a's criterion, given an empirical instance

§11a discriminates the star (corrects, but model-free — set-point baked into constitutive dynamics, no
separately-interventable reference ⇒ not alive) from systems holding a decoupled reference. That
criterion currently rests on argument.

The bioelectric literature supplies an instance where the reference is **separately addressable in
practice**: it can be read out, rewritten, and rewritten back, while the archive is untouched and the
constitutive dynamics are unchanged. That is precisely the property §11a requires and the star lacks.

**Grade honestly: this is an illustration, not a test.** It cannot falsify §11a. A criterion that finds
a confirming instance has not been tested — and the framework has already been burned once by treating a
result forced by construction as though it could have come out otherwise (v1.18, §11b). Write it as
"here is what the criterion picks out in a real organism," never as "the criterion has been validated."

Proposed grade: SYNTHESIS.

---

## 6. Claim D — the Integration knob, and a benchmark candidate (FRONTIER)

Stripped of "cognitive glue," the claim in the literature is: **reduce inter-cell coupling and the
partition at which the system is irreducible moves down toward the single cell; restore coupling and it
moves back up.** That is the Phase D1 level-selection crossover (Edit E20) with a physical dial.

Independent support from an unrelated formalism: **Sacco, Sakthivadivel & Levin 2026, Theorem 4** —
clique-structured graphs admit a non-empty parameter window of local order with global disorder, i.e.
many individuals rather than one, under a thermodynamic condition (2J > T log nᵢ) where D1 gives a
coupling-ratio condition (b ≈ a/2). **Consilience, not equivalence** — different order parameter,
different regime, and the correspondence would itself be work. See
`AOP_VerificationMemo_SaccoSakthivadivelLevin2026_20260721.md`, including why that paper's Corollary 1
must not be cited and why its equilibrium scope limits what it can bind.

**Why this is worth flagging despite being unbuilt.** The outstanding benchmark requirement is ground
truth **sourced externally**, pre-registered, not forced by the model's own construction. Coupling is
externally manipulated; anatomical outcome is externally scored; neither is set by the topology of the
AOP model. This is the first non-circular candidate to surface.

**Why it is FRONTIER and not a plan.** Φ_MIP as canon uses it lives on a static Gaussian
Σ = (I + gL)⁻¹. A planarian is neither static nor Gaussian. The bridge is unbuilt and may not exist. Any
attempt must pre-register its gate *before* looking at outcomes, per standing governance.

---

## 7. Claim R — the proposed refusal

AOP holds a small set of load-bearing refusals. This note proposes adding one, scoped to vocabulary
rather than to any empirical matter:

> **The framework declines the goal-directed reading of bioelectric pattern control.** Where the source
> literature says a tissue *remembers a target morphology* or *pursues a goal state*, AOP states the same
> observation as a multistable dynamical system whose selected attractor is externally switchable and
> which retains the selection across substrate turnover. This is not a claim that the goal-language is
> false; it is a refusal to let it become load-bearing, consistent with the anti-telos principle. Every
> result imported from this literature is restated in attractor terms before it is used, and the
> restatement is checked to preserve the observation.

Two reasons to make this explicit rather than implicit. First, it is the anti-telos principle applied to
the largest single body of teleological vocabulary the framework will ever import — the place where the
principle is most likely to erode quietly. Second, it does protective work: it states on the record that
AOP's use of these results carries no commitment to their authors' interpretive programme.

---

## 8. What this note does **not** support

Stated explicitly so that a later reader cannot mistake scope.

- **Nothing about consciousness.** AOP has no consciousness commitment and acquires none here. Rouleau &
  Levin 2026 is on Drive and is deliberately not cited.
- **No adoption of the cognitive-light-cone construct.** It is irreducibly teleological — "the largest
  goal state pursuable" has nothing left after the strip.
- **No adoption of the Platonic/ingression programme.** Non-naturalist, and its stated argument ("we get
  more out than we put in") is what a constraint-satisfaction landscape looks like from the inside.
- **No claim that bioelectric signalling is *instructive* rather than permissive.** This is a live
  dispute in the field and is not settled by the pharmacological results — many rely on channel blockers
  with real off-target problems. **Claims A–C do not require instructiveness**; they require only that
  the state is persistent, drive-maintained, and externally switchable. Claim D does lean on it and is
  weaker for that.
- **No grade above SYNTHESIS anywhere in this note.**

---

## 9. What would retract this

- **Claim A** falls if the persistent state turns out to be archived after all — chromatin, methylation,
  or another heritable substrate co-varying with the bioelectric perturbation. This is the obvious
  alternative and prime does not know whether the source papers exclude it. **The single most important
  thing for the verifier to check in Durant 2017.**
- **Claim A** also weakens substantially if the effect fails independent replication outside the
  originating lab.
- **Claim B** is unaffected by any of the above — it rests on electrophysiology.
- **Claim C** falls if the reference turns out not to be separable from the constitutive dynamics after
  all, i.e. if "rewriting the set-point" is better described as changing the machine.
- **Claim D** dies quietly if the static-Gaussian bridge cannot be built. That is the expected outcome
  and would not be a failure.

---

## 10. Verification debt that must clear before any fold

1. **Read Durant 2017 in full.** Specifically: does the paper exclude epigenetic/chromatin co-variation?
   Are the histology and expression controls as broad as the abstract implies? What is n?
2. **Read Pezzulo et al. 2021 in full.** Confirm it is the attractor formulation. If it is, it becomes
   the preferred citation throughout and Durant becomes the empirical support.
3. **Independent replication** outside Tufts. This is the gate on grading anything SETTLED. Nobody has
   searched for it.
4. **Read Jaeger.** Prime's characterization of that critique to Ben came from a third party's summary,
   not the critique. Charter names this defect explicitly.
5. **Read Srivastava 2021** with the caveat that it is a Levin-lab synthesis in a subfield journal, not
   an outside audit — prime's earlier recommendation of it overstated its independence.
6. **Read Emmons-Bell 2015** before Claim D cites it.

---

## 11. Adjudication

Prime drafted this and does not bless it. Required before any part folds into canon:

- an **independent verifier** who reads the sources rather than this note, per §10;
- an **adversarial pass** (ChatGPT), pointed specifically at Claim A — the archive-alternative in §9 is
  where it should be aimed, and at the question of whether the "third register" is a real distinction or
  a re-description of ordinary bistability;
- **Ben decides.**

If only one item survives, prime expects it to be **Claim B**, which rests on settled electrophysiology
and needs no bioelectric-patterning result to be true. **Claim A is the most valuable and the most
fragile.** Claim R costs nothing and protects something.

*— prime, 22 July 2026. Canon v1.20 unchanged by this note.*
