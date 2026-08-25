The Living Architecture: a decoupled-reference criterion and what it would take to earn it

Follow-on to *The Architecture of Persistence*

### The Living Architecture

Developing AOP's decoupled-reference regulatory architecture as a candidate criterion for the living state, with its present-tense tiers, its diachronic prerequisites, and an honest account of what the control-theory literature does and does not supply

⟨Author⟩

⟨Affiliation⟩  ·  Correspondence: ⟨email⟩

Follow-on paper · version 0.1 · compiled 25 July 2026 · **DRAFT — not peer reviewed, not canon** · derived from `AOP_CANON_MASTER_v1.25.md` under the v1.26 red-team remediation order of 24 July 2026, which relocated this material out of the core paper.

---

**Status of this document.** This is a v0.1 relocation draft, not a finished paper. Every substantive claim below was previously carried in the AOP core paper (§§4a, 9a, 11a, and the head-of-paper note on "life") and has been moved here, with the specific re-gradings the remediation order required already applied. It has **not** been re-argued, re-computed, or independently verified since the move. The core paper (`AOP_CANON_MASTER_v1.26.md`) retains only a one-paragraph pointer to the architecture and one sentence of the diachronic material; it does not name anything *alive*.

**Why the material moved.** The core paper is a synthesis about persistence. A criterion for life is a much larger claim resting on a much smaller evidence base, and carrying it inside the core meant that a reader assessing the coupling classification also had to assess a proposal about the definition of life. Separating them de-risks the core immediately and lets this material be argued on its own terms and at its own grade. The move is scope discipline, not retraction: nothing here is withdrawn, and the positions the red team attacked are defended below rather than conceded — where they are narrowed, the narrowing is stated.

**What changed in the move.** Six things, each required by the remediation order and each a weakening of a posture rather than of a result. (1) The **"new definition, graded frontier" announcement posture is removed.** This paper develops a candidate criterion; it does not announce a new definition of life. The frontier grade stays on the claim; the billing goes. (2) The **six-part conjunction is relabelled an AOP hypothesis** rather than something forced by cited control theory (§3 below). (3) The phrase **"the internal-model requirement of life" is retired** — the cited results are about regulation, not about life. (4) The **discriminator is restated subspace-wise** (§4 below), which hardens it against the coordinate-dependence attack rather than conceding it. (5) The **second tier is redefined as a counterfactual recovery capacity** and is no longer presented as readable from architecture alone (§6). (6) **Death is reframed as process-cessation-at-grain** rather than as simultaneous four-axis collapse (§8). Additionally, the **mule is dropped as a decisive proof** of the threshold (§5), and the Memory-axis semantic-weight computation that had lived inside §11a was returned to the core paper, where it belongs.

---

### 1A note on the word "life," read first

This paper uses *alive* in a specific and deliberately **frontier** sense, and it should not be read as restating the settled standard of the field. The community's operational reference point — which we treat as **settled** — is the "chemical Darwinian" definition (Joyce's formulation, adopted as a NASA-exobiology working reference), *"a self-sustained chemical system capable of undergoing Darwinian evolution"* [Joyce 1994; discussed in Cleland & Chyba 2002]. That definition welds two clauses (self-sustaining; capable of Darwinian evolution) and, by its authors' own account, scopes itself to chemistry for NASA's purposes.

The criterion developed here differs on purpose. It keeps the *self-sustaining* clause but (i) makes it **structural and substrate-independent** rather than chemical; (ii) is **present-tense and self-directed only** — it drops the *Darwinian evolution* clause, which concerns across-generation lineages and is placed above the AOP framework (AOP §9); and (iii) is defined as one specific coupling architecture — active self-maintenance against a dynamically decoupled internal reference for the system's own viable set — rather than by a checklist of life's hallmarks. Where it agrees with the reference definition (self-maintenance is necessary) we say so; where it departs (substrate-independence, no reproduction clause, structural rather than hallmark-based) we mark the departure rather than smooth it over.

What this paper does **not** do is announce that it has a new definition of life. Earlier drafts said exactly that — "a new definition, graded frontier" — and that announcement is withdrawn. It promised more than the work supports: the criterion has been demonstrated for internal self-consistency on two closed-form systems, never tested against a rival, and never run on a case where it could have failed. A candidate criterion under development is what this is, and it is revisable or removable if it does not earn its keep. **[FRONTIER; stated as of July 2026.]**

**⚠ Source status, stated rather than assumed.** The Joyce 1994 foreword is a print-book foreword and has **not been retrieved**. The wording above is as quoted in Cleland & Chyba 2002, read from that paper's body; the page attribution (pp. xi–xii) is corroborated by independent secondary reference lists but has not been checked against the primary. Wording varies slightly between secondary sources ("self-sustained" vs "self-sustaining"), and at least one secondary source attributes the formulation to NASA's Exobiology Discipline Working Group rather than to Joyce personally. A secondary quotation is not primary verification, and this citation should not be described as verified until the foreword is read.

---

### 2Three modes of holding oneself off equilibrium

Three of AOP's worked persisters actively hold themselves off equilibrium — the flame, the star, and (were it running) the cell — and they do not do it the same way. The distinction is not *drive* (all three spend) and not *correction* (both the star and the cell restore after a perturbation). It is **what the correction is read against**, and it is a structural fact the framework can compute.

- **Continue** — no restoring force. The flame is marginally stable: rebuilt each instant from current supply, it is gone the moment supply cuts, with no fight (AOP §11). Its semantics are all in drive.

- **Correct, model-free** — a restoring force whose set-point *is* a fixed point of the constitutive dynamics. The star is the worked case: its negative-specific-heat thermostat pulls the core back when perturbed (AOP §11), but nothing in the star *stores* the target hydrostatic state; the target is where the physics sits. There is no separable reference to intervene on. What a system of this kind lacks is not stability but a *stored, separately-manipulable reference*.

- **Correct, model-based** — a restoring force driven against a **decoupled internal reference** that stores the system's own viable set (its *essential variables*, in Ashby's sense [Ashby 1960]) and is dynamically separable from the regulated variable it controls. The cell is the case: setpoints are held in a regulatory sub-network, read out onto the fast physiology, and can be corrupted independently of the physiology itself.

The third mode is what this paper is about. Stated as a candidate criterion: **a persister whose maintenance corrects the regulated axes against a decoupled, separately-interventable internal reference for its own viable set.** This is a threshold on AOP's existing four dimensions and its semantic mask, not a fifth axis — the reference is a load-bearing internal coupling from a slow reference onto the fast regulated dynamics, exactly the object the semantic mask (AOP §3) is built to detect. It is substrate-independent by construction, and it does not relabel neighbouring accounts: autopoiesis names self-production of components [Varela, Maturana & Uribe 1974] and is silent on a stored viability reference; the semantic mask's parent result concerns information a system holds about its *environment* [Kolchinsky & Wolpert 2018], whereas the reference here is about the system's *own* viable set.

---

### 3What the control-theory literature does and does not supply

This section states plainly what earlier drafts got wrong, because the correction matters more than the claim.

**The criterion is a six-part conjunction, and the conjunction is an AOP hypothesis.** Spelled out, it asserts the joint presence of: (1) a regulatory subsystem; (2) dynamical decoupling of that subsystem from the process it regulates; (3) an internal reference that stores a target; (4) that reference being a *separate intervention target* from the regulated dynamics; (5) the reference's content being *viability-relevant* — it stores the system's own viable set and not some other target; and (6) active self-maintenance, the correction actually running now. **No cited result forces this conjunction.** It is this framework's hypothesis, graded frontier, and it should be attacked as such.

**What the cited results actually support is components.** The internal model principle of control theory [Francis & Wonham 1976] establishes that robust asymptotic regulation requires the controller to embed a model of the exosystem modes — the dynamics generating the reference and disturbance signals — within its stated scope. That supports component (1) and bears on (3). It does **not** establish that a regulator must hold a model of *its own viability*, which is a different object entirely, nor does it establish decoupling, separate interventability, or self-maintenance. The organizational account of biological regulation [Bich, Mossio, Ruiz-Mirazo & Moreno 2016] locates genuine regulation in a subsystem that is *dynamically decoupled* from the process it regulates — operating at a different dynamical scale and under different constraints. That supports component (2), and it is the strongest external support the criterion has. It does not supply components (3)–(6).

**"The internal-model requirement of life" is retired as a description.** Earlier drafts used that phrase for the Francis–Wonham result. It is wrong twice over: the result is about regulation, not life, and it is about exosystem modes, not viability. The phrase is removed here and in the core paper, and the citations are reattached to the component claims they actually support.

**The good-regulator theorem remains background only.** [Conant & Ashby 1970] is sometimes read as forcing every regulator to carry a model; it establishes only that the optimal-and-maximally-simple regulator is a *homomorphic image* of the regulated system — a notion under which even a bare fixed point qualifies. It therefore does not supply the decoupled-reference distinction, and it is not load-bearing anywhere in this paper.

**⚠ Verification status of the two load-bearing citations, stated honestly.** Francis & Wonham 1976 (*Automatica* 12(5):457–465) was **not retrieved** in the preparation of this draft — it is paywalled on every route attempted, and no part of the paper was read. The bibliographic record is verified against Wonham's own publication list; the *statement* of the internal model principle above is reconstructed from two open Wonham-authored restatements (a 2018 note and 2022 slides), which give a later, more abstract discrete-time formulation and cite Wonham's 1976 *SIAM J. Control* paper rather than the *Automatica* one. **The 1976 theorem's actual scope conditions are unverified.** Bich et al. **was** read in full text (author-hosted manuscript), and the decoupling requirement appears as a numbered condition; two caveats travel with it — the retrieved copy is the 2015 online-first version against the 2016 print citation, and its page numbers are manuscript pages, not the journal's 237–265 range. Neither citation should be described as line-checked until prime has done so.

---

### 4The discriminator, stated invariantly

Earlier drafts stated the discriminator as the existence of a **separate reference node**. That formulation invites a coordinate-dependence objection: a node is a basis-dependent object, so a change of coordinates could seem to create or destroy the very thing the criterion turns on. The objection is answered by restating the criterion at the level of subspaces rather than nodes, which is where it always belonged.

**The invariant formulation.** The system admits a **proper invariant subspace whose dynamics are autonomous with respect to the regulated coordinates** — a subspace the dynamics preserve, evolving under its own law without being driven by the variables it regulates, while feeding into them.

Two properties make this the right object. First, it is **preserved under similarity transformation**: invariant subspaces map to invariant subspaces under a change of basis, so the criterion returns the same verdict in every coordinate system. Nothing about it can be created or destroyed by rewriting the model. Second, and independently, **an arbitrary basis change is not an admissible intervention.** AOP's declaration tuple carries an explicit intervention class **I** (AOP §12″), populated by physical operations one could actually perform on a system; a change of coordinates is a re-description of the model, not an operation on the world, and it is not a member of **I** for any physical system. The declared intervention class fixes the basis in which "separately interventable" is evaluated.

This hardens the criterion; it does not concede the objection. The node formulation was a convenient shorthand for the subspace fact, and where the shorthand appears below it should be read as pointing at the subspace.

**Computed, not only described (Figure LT).** The discriminator is made concrete on two minimal closed-form (Ornstein–Uhlenbeck) systems that both correct toward the same essential target μ* and both restore after a kick. The *cell-type* system carries a regulated variable driven toward the readout of a reference that relaxes twenty times more slowly than it does; the *star-type* system carries two fast structural shells whose restoring set-point is baked into the intrinsic drift, with no slow reference. Each internal coupling is scrambled in isolation under the internal-edge intervention protocol (AOP §3) and the fractional drop in a present-tense viability functional (closeness of the regulated variable to μ*) is read as its semantic weight; the generator spectrum supplies each edge's timescale separation.

The cell-type system contains an edge that is **both** load-bearing (scrambling the reference readout collapses viability and drives the regulated variable off target) **and** decoupled — its set-point is held in an autonomous invariant subspace, not baked into the fast constitutive drift. The star-type system's only load-bearing edge carries its target *in that fast drift itself*: it corrects, but there is no separate subspace to scramble.

Decoupling is thus an **architectural** fact, not a timescale-separation magnitude. A sweep of the slow/fast ratio (Figure LT-T) shows the model edge stays high and load-bearing and flat across the whole star–cell window (≈0.79 at the star's 2× down to ≈0.72 at the cell's 20×), with no threshold knee — crossing a separation value nowhere flips the verdict, so it cannot be what separates the two. What separates them is whether the autonomous subspace exists at all. The threshold is therefore the joint condition *load-bearing ∧ decoupled*, and it correctly places the star — which AOP already treats as corrects-but-not-alive — outside it.

**This is a demonstration of self-consistency, not a test that could fail**, and that limitation is not a footnote. The model edge is load-bearing by construction. What the computation establishes is that the discriminator separates the two structures cleanly, is computable in the framework's own idiom (mask weight × generator spectrum), and does not misclassify the star. It establishes nothing about whether the criterion is *correct*. Code and data are deposited. **[SYNTHESIS, computed.]**

**Third-person detectability, and its two scopes.** Beyond self-consistency, the criterion is positively detectable from third-person access — but only up to the declared viability functional V, which is load-bearing rather than incidental: the procedure detects a decoupled, load-bearing set-point, and it is V that certifies that set-point as the system's viable target. There is no detection without a declared V. On an OU star↔cell interpolation, a graph-plus-V procedure (load-bearing by edge ablation; decoupling by a do-intervention that shifts the regulated variable's set-point, plus structural separability of the reference) flags the cell and rejects the star, and the verdict is architectural — invariant to the reference/regulated timescale ratio across three orders of magnitude (deposited `phaseE3`). Two scopes bound this. (i) "Separable from the fast regulated path" is operationalized as "not the regulated node," which isolates the reference only because the OU toy has no non-reference nodes — so positive detection is scoped to that model class. (ii) With more than one symmetric decoupled reference, the architecture is still detected but *which* subspace is the reference is not uniquely attributable from the graph and V alone.

---

### 5Alive and reproducing come apart

The criterion is self-directed and present-tense; reproduction is lineage-directed and cashes out only across generations. The two separate, and the separation is what licenses AOP's scope wall between present-tense persistence and the theory of evolution.

**The virion supplies the contrast, and that is the work it does here.** The minimal, naked virion carries a pure "make-more-of-me" instruction with no "keep-me-viable" clause — a copy-me blueprint with the engine off, aimed at propagation, not self-reboot. It reproduces (in a host) and holds no decoupled reference for its own viable set. That contrast is the reason **organismal maintenance and lineage evolution must be separated** rather than run together, and it is retained on exactly that basis. (The claim is scoped to the minimal/naked virion, where it is airtight. The giant viruses — Mimivirus, the pandoraviruses — carry translation-associated and metabolism-adjacent genes and sit in a live gray zone; the criterion may well still exclude them, but that is a place the *load-bearing ∧ decoupled* test would have to be **applied** to a specific architecture rather than asserted.)

**The mule is retained as illustration and dropped as proof.** Earlier drafts ran the sterile persister — the mule, the worker, the childless organism — as the decisive mirror case establishing the threshold: fully alive, zero reproduction. That is more weight than it can carry. Whether the mule is "alive" is a verdict delivered by the very intuitions the criterion is supposed to be tested against, so using it as proof is circular; and the standing objection it names is contested in the literature rather than settled — it is stated in order to be rebutted at the population level [Chodasewicz 2013], and while even the rebuttal concedes that the *individual* mule does not itself evolve, that concession is a point about the reference definition's scope, not a demonstration that this paper's threshold is correctly placed. The mule remains a useful illustration of why the two clauses of the reference definition are separable. It is not evidence for the criterion, and it is no longer presented as such.

What survives is the structural separation itself, which needs only the virion side and the plain observation that the field's working definition welds two clauses that come apart. **[SYNTHESIS on the separation; the mule is illustration only.]**

---

### 6The spore, and the second tier

The predicate splits into two present-tense tiers, and the spore is the case that forces the split.

- **Alive** — the reference edge is *load-bearing now*: active correction against the decoupled reference, the mask-detectable, present-tense quantity Figure LT operationalizes. In a dormant spore drive ≈ 0 and nothing is being corrected now, so scrambling the reference edge produces zero present-tense viability drop: by this tier the spore reads inert, indistinguishable from a crystal. Cell: yes. Spore, crystal, naked virion: no.

- **Viable / pausable** — a **present-state-conditioned counterfactual recovery capacity**: conditional on the system's present state, would it resume correcting against its decoupled reference under a declared perturbation or restart protocol?

**The second tier is not readable from architecture alone, and earlier drafts said it was.** They defined the pausable tier as "the decoupled-reference architecture is structurally present now — the regulatory wiring physically exists," and claimed this could be read off structure without restarting the system. The counterexample is immediate and fatal: **a dead spore retains the visible architecture.** Denatured proteins, a fragmented genome, a collapsed proton gradient — none of these necessarily changes what the wiring diagram looks like, and a criterion that scores a dead spore as *life paused* has not distinguished anything.

The tier is therefore restated as a capacity, and the restatement carries an honest cost. A counterfactual recovery capacity is **evaluated through a model of future dynamics** — biochemical integrity, recoverability under a declared perturbation, or an explicit functional intervention (attempt germination). It is not a present-tense structural reading, and it cannot be made into one. What keeps it inside AOP's present-tense principle is that the *conditioning* is on the present state: the question is what this state would do, not what this system will in fact do, and the former is a property of the current configuration in the way "soluble" is a property of a crystal now. What is given up is the claim that no model of future dynamics is needed. It is needed, and the second tier should say so.

**The first tier is unaffected.** *Alive* remains strictly present-tense-active and mask-detectable; the present-tense principle is intact there, and the mask operationalizes exactly that tier. The two tiers do different jobs, and only the first is a present-tense reading.

So the spore is *life paused*: alive-tier no (edge not load-bearing now), pausable-tier yes **conditional on an integrity check that a wiring diagram does not supply**. The virion is its false twin: also engine-off, but even its architecture is a propagation blueprint rather than a decoupled self-reference, so it fails both tiers and never crosses the threshold on reboot. **[SYNTHESIS; the second tier's model-dependence is stated rather than hidden.]**

---

### 7Diachronic individuation: when two slices are one process

AOP supplies a synchronic irreducibility coordinate (minimum-cut dependence, AOP §4). Persistence also poses the orthogonal, *diachronic* question: when do two time-slices belong to **one** persisting process? The core paper retains one sentence of this — *diachronic comparison requires a declared tracking relation* — and the development is here.

A persisting thing is a process — a form continuously instantiated through changing material — and it is individuated over time by **continuity of instantiation**, causal continuity of the process itself (*genidentity* — the term originates in early-20th-century process metaphysics, from Lewin and later Reichenbach, and long predates its use here; it is applied to biological individuals as processes by DiFrisco 2018, in Nicholson & Dupré 2018, whose in-chapter terminology is paraphrased pending full-text verification) — not by retained substance and not by a preserved description. This is a settled position imported, not a new invention; what is this framework's is the mapping onto the four axes and the present-tense principle. **[SETTLED named view; the mapping is SYNTHESIS.]**

Two contrasting thought experiments fix the criterion, and their difference *is* the result. In the **transporter/de-extinction** case the process stops and a *description* is re-enacted elsewhere; the result is a look-alike, a cover version, not the resumed original. In the **Ship of Theseus** case continuity of instantiation holds *through total material turnover*, because the pattern is never interrupted; it is the same ship though it keeps no original plank. The two cases involve the *same* total substance swap; the only difference is whether instantiation was unbroken (Theseus) or interrupted-and-re-enacted-from-a-record (transporter). Continuity is unbroken instantiation, not preserved material. "Same process ≡ unbroken instantiation" is this framework's **stipulated definition**, and "the transporter makes a new process" follows *by that definition*, not by a discovery about identity. This is consistent with the deflationary reading on which there is "no further fact" beyond continuity itself [Parfit 1984] — no identity fact is claimed *beyond* continuity; continuity is defined as the fact.

**The position is not conceded.** The red team's objection was scope, not error: a criterion of diachronic identity is a large philosophical commitment for a physics-adjacent synthesis to carry in its core. That is why the material sits here. The continuity-of-instantiation position is retained in full, and what the core keeps is the minimal operational residue — that no two-time comparison is well posed until a tracking relation is declared, which enters as part of the declaration **D**.

**Fission is the honest hard case.** One continuously-instantiated lineage that splits into two leaves both descendants genidentity-legitimate; asking "which is the original?" has no unique answer, exactly as in the fission cases of the personal-identity literature [Parfit 1984]. Diachronic identity is therefore not always one-to-one, and the framework does not force it to be: speciation is a branching of one process into two, both continuations, neither uniquely the original. This is a property of the criterion, marked, not a defect to be patched. **[SYNTHESIS; FRONTIER at the formal treatment of branching.]**

---

### 8Death, reframed

**Death is not a fifth erasure.** A persister is a process with a present tense **at a declared grain**; death is that process stopping at that grain — not a new axis, and not a simultaneous collapse of all four dimensions.

On a tightly integrated persister the four failures commonly arrive together, drive-failure typically leading into mixing, forgetting, and fragmentation behind it; a cell dies this way because it holds hard on all four and the collapse of one pulls the rest. But lower-grain processes may run on after — membranes intact, gradients decaying slowly, a genome persisting — which is expected: those are subordinate grains outliving the one that stopped, not the persister still alive. A crystal cannot die in this sense (it barely holds a present tense to lose). **[SYNTHESIS.]**

**Why this is a reframing and not a fence.** The earlier statement defined death as "the four dimensions failing as one on an integrated persister." Against that definition, intact membranes, persisting genomes, transient metabolism, and gradients decaying on different timescales are counterexamples: the four plainly do not fail as one. Against cessation-at-grain they are **confirmations** — exactly what the reframing predicts when a higher-grain process stops. The counterexamples are dissolved rather than scoped out, which is the stronger repair.

The reframing costs nothing new, because it is a corollary of two things AOP already owns, applied to cessation: the **present-tense principle** (a persister is a process with a present tense) and the **time-grain relativity of the axes** (AOP §5; the star's thermal-versus-nuclear Memory is the worked instance). If a persister is a process at a declared grain, then its death is that process halting at that grain, and nothing further need be assumed.

**The cascade is separated from the definition.** The causal cascade — drive-failure leading into mixing, forgetting, and fragmentation, "the collapse of one pulls the rest" — is a real pattern but a **more contestable** claim than the definition, and the earlier statement baked it in. Organisms also die by trauma, by rupture, by information loss, and in those routes drive-failure does not lead. The cascade is therefore retained as **one common route on tightly integrated systems**, not as what death *is*. The definition is cessation-at-grain; the cascade is a frequent pattern on a particular class of persister.

This also secures why death must be real. If "the blueprint still exists, so it persists" were admitted, nothing would ever die and persistence would mean nothing. A frozen genome is a description, not a paused process; the mammoth species stopped when its last member did, and de-extinction would begin a new process rather than resume the old. The operational test is present-tense and needs no foresight: does the system restart *itself* from its own held state (spore → paused), or must something external rebuild it from a record (mammoth → new process)? *Paused ≠ stopped*, and *held-state ≠ description* — subject to the integrity caveat of §6, since a dead spore restarts from nothing.

---

### 9The collective scale: an open question

The regulatory architecture can in principle be asked about at the collective scale as well as the part scale. Does a collective ever hold a decoupled reference for the *collective's* viable set, one that is not simply the sum of its members' self-references? An ant colony regulates its nest toward a set-point that no single ant represents: each ant is model-free, following a local cue exactly as the star corrects without carrying a reference, yet the colony holds the reference somewhere above any ant. By this paper's criterion, a collective would cross the threshold *as* a collective exactly when it holds a decoupled reference for its own viable set — one that could be intervened on and that lives in no single part.

Whether any actual colony clears that line is **not settled here**, and the reason is precise and doubled. First, certifying that the collective is the right object to evaluate would require the nested-level, non-stationary extension of minimum-cut dependence that AOP §4 scopes out — the F2 seam, open in both halves after the v1.22 level-selection retraction (AOP §13a). Second, and independently, AOP §4 as of v1.26 no longer licenses the inference from a positive minimum-cut result to "this is one individual" at all; that inference is deleted, and a verdict now requires an individuation panel (autonomy, causal closure, intervention stability, common-cause controls) that neither paper completes. The collective question therefore inherits two open problems rather than one. **[FRONTIER; bottlenecked on the F2 seam and on the individuation panel.]**

---

### 10Status of claims in this paper

| Claim | Dependency | Evidential |
|---|---|---|
| Three modes (continue / correct model-free / correct model-based) | dissociable (the star and cell separate on *load-bearing ∧ decoupled*) | analytic-model-result (two OU systems, Figure LT) |
| The six-part conjunction as a criterion for *alive* | unidentified | **conjecture/frontier — an AOP hypothesis, not forced by cited control theory** |
| Regulatory subsystem; internal model of exosystem modes | conditionally-forced (within the cited theorem's scope) | theorem [Francis & Wonham 1976] — ⚠ **not retrieved; scope conditions unverified** |
| Dynamical decoupling of the regulatory subsystem | conditionally-forced (within the cited account) | organizational account [Bich et al. 2016] — full text read; 2015/2016 edition caveat |
| Discriminator as an autonomous invariant subspace | forced (similarity-invariant by construction) | definition/stipulated + analytic-model-result |
| Third-person detectability up to declared V | conditionally-forced (static OU model class) | analytic-model-result (`phaseE3`); node-attribution scope stated |
| Alive ≠ reproducing (structural separation) | dissociable | synthesis; the **virion** carries it, the **mule** is illustration only |
| Two tiers; pausable = counterfactual recovery capacity | dissociable | synthesis; **model-dependent** — not readable from architecture alone |
| Diachronic individuation by continuity of instantiation | forced by stipulation | settled named view [DiFrisco 2018; Parfit 1984] + synthesis (the mapping) |
| Speciation = process fission | dissociable | synthesis; frontier at formalization |
| Death = process cessation at a declared grain | forced (corollary of present-tense + grain relativity) | synthesis |
| Death cascade (drive-failure leading) | dissociable — one common route, not the definition | synthesis; contestable, and marked |
| Collective-scale threshold | unidentified | conjecture/frontier; doubly bottlenecked (§9) |

**Reading this ledger.** Nothing here is settled science except the imported named views and the components of the control-theory support. The criterion itself is a frontier hypothesis demonstrated for self-consistency on systems built to demonstrate it. That is the honest standing of this paper, and the reason it is a follow-on rather than a section of the core.

---

### 11What this paper would need to earn its keep

Four things, none of them attempted here.

1. **A case that could fail.** Every computation supporting the criterion is a self-consistency demonstration whose answer key was written by the same hands. The criterion has never been run on a system where it might have returned the wrong answer.
2. **A rival.** The criterion has not been compared against autopoiesis-based, metabolism-first, or information-theoretic alternatives on any shared case. "Internally consistent" is not "better than."
3. **Primary-source verification of the control-theory support.** Specifically: Francis & Wonham 1976 read in full, with the theorem's actual scope conditions checked against the use made of it here; and Bich et al. checked against the published 2016 version rather than the 2015 online-first manuscript.
4. **The gray-zone applications.** The giant viruses, the dormant-but-dead spore, the ant colony — each is named above as a place the test would have to be *applied* rather than asserted. None has been.

---

### References

References follow the core paper (`AOP_CANON_MASTER_v1.26.md`) except where noted. The entries load-bearing here, with honest verification tags:

Ashby WR. *Design for a Brain: The Origin of Adaptive Behaviour.* 2nd ed. London: Chapman & Hall, 1960. ⚠ verify exact pagination if a definition of "ultrastability" is quoted.

Bich L, Mossio M, Ruiz-Mirazo K, Moreno A. Biological regulation: controlling the system from within. *Biology & Philosophy* 31, 237–265 (2016; published online 2015). doi:10.1007/s10539-015-9497-8 — cited for the **dynamical decoupling** component only. [✓ full text read (author-hosted manuscript, 2015 online-first); ⚠ page numbers are manuscript pages, not the 237–265 journal range; confirm against the published version.]

Chodasewicz K. Evolution, reproduction and definition of life. *Theory Biosci.* 133, 39–45 (2013). doi:10.1007/s12064-013-0184-5 — cited as *stating* the Mule's problem in order to rebut it at the population level; used here as illustration, not as evidence.

Cleland CE, Chyba CF. Defining 'life'. *Orig. Life Evol. Biosph.* 32, 387–393 (2002). doi:10.1023/A:1020503324273 — the source actually read for the Joyce formulation.

Conant RC, Ashby WR. Every good regulator of a system must be a model of that system. *Int. J. Syst. Sci.* 1, 89–97 (1970). doi:10.1080/00207727008920220 — **background only**, not load-bearing.

DiFrisco J. Biological processes: criteria of identity and persistence. In: Nicholson & Dupré 2018, ch. 4. doi:10.1093/oso/9780198779636.003.0004. ⚠ page range and the specific terms genidentity/causal cohesion/perdurance not confirmed in-chapter — paraphrased; verify before quoting.

Francis BA, Wonham WM. The internal model principle of control theory. *Automatica* 12, 457–465 (1976). doi:10.1016/0005-1098(76)90006-6 — cited for the **regulatory-subsystem / exosystem-model** component only, **not** for a "requirement of life." [⚠ **NOT RETRIEVED.** Bibliographic record verified against Wonham's own publication list (entry J34). No part of the paper was read; the statement used here is reconstructed from later open Wonham restatements, which give a more abstract discrete-time formulation and cite a different 1976 paper. Scope conditions unverified. Do not describe as verified.]

Joyce GF. Foreword. In: Deamer DW, Fleischaker GR, eds. *Origins of Life: The Central Concepts.* Boston: Jones & Bartlett, 1994. [⚠ **NOT RETRIEVED.** The book is access-restricted on every route attempted. Wording above is as quoted in Cleland & Chyba 2002; page attribution pp. xi–xii corroborated by independent secondary reference lists only. Secondary quotation is not primary verification.]

Kolchinsky A, Wolpert DH. Semantic information, autonomous agency and non-equilibrium statistical physics. *Interface Focus* 8, 20180041 (2018). doi:10.1098/rsfs.2018.0041 — cited for the semantic-mask method, whose intervention acts on the system–environment channel; AOP's internal-edge extension is AOP's own (core paper §3).

Moreno A, Mossio M. *Biological Autonomy: A Philosophical and Theoretical Enquiry.* Dordrecht: Springer, 2015. doi:10.1007/978-94-017-9837-2

Parfit D. *Reasons and Persons.* Oxford: Oxford University Press, 1984 (Part 3, Personal Identity). — cited for the teletransporter and fission thought experiments and the "no further fact" reading, not for a claim that a copy is determinately not the original.

Varela FJ, Maturana HR, Uribe R. Autopoiesis: the organization of living systems, its characterization and a model. *BioSystems* 5, 187–196 (1974). doi:10.1016/0303-2647(74)90031-8

---

**End of `AOP_LifeArchitecture_Followon_v0.1.md`. Proposal for prime's verification and Ben's decision; not canon.**
