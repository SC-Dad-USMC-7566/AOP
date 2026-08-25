# Work Order — Life-Definition Adjudication and Hardening Arc

**Document ID:** `AOP_WorkOrder_LifeDefinition_Adjudication_20260803.md`
**Issued:** 3 August 2026
**Issued by:** prime (chat seat), on Ben's direction
**Seats tasked:** Claude Science (CS) · Cowork (CW) · OAI/Aster
**Adjudicator:** prime. **Decision authority:** Ben.
**Governing documents:** AOP Charter v1.2; AOP Canon v1.26 (`1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn`, 254,046 B, md5 `54ceb3772e29f25c6e139b703d550d59`, hash-verified 3 Aug 2026); `AOP_LifeArchitecture_Followon_v0.1.md` (`1pP-phsxzzrSIT5GmjCxi7iYmyBr9tyKR`, 38,799 B).

**Ben's decision points in this arc: one.** Everything else routes seat-to-seat through prime. The single decision is at Gate 4 (§7): adopt, amend, or retire the criterion, on prime's adjudication of the three deliverables.

---

## 0. Why this arc exists

The follow-on's own §11 lists four things the criterion would need to earn its keep. Two of them are the subject of this order:

> **A case that could fail.** Every computation supporting the criterion is a self-consistency demonstration whose answer key was written by the same hands.
> **A rival.** The criterion has not been compared against autopoiesis-based, metabolism-first, or information-theoretic alternatives on any shared case. "Internally consistent" is not "better than."

This arc supplies both: a frozen set of adjudication cases the criterion did not choose, and a named-rival comparison across the same cases. It also confronts the finding from the system-selection arc that dominates everything else here: **the criterion's positive class may not contain the cell.** If a criterion demanding a stored, separately-interventable *state* reference excludes the paradigm case, it is not an improvement on anything. That question is not decoration on this order; it is the order.

Ben's standing constraint, recorded verbatim: *substrate-independence is not to be given up in the name of elegance, but it must be shown, not assumed — and if it is wrong, the math has to show that too.*

---

## 1. Shared substrate — read before doing anything

### 1.1 The criterion as it currently stands (verbatim from the follow-on, §2 and §3)

> A persister whose maintenance corrects the regulated axes against a **decoupled, separately-interventable internal reference for its own viable set.**

Spelled out, this is a **six-part conjunction**, graded FRONTIER, and explicitly labelled an AOP hypothesis not forced by any cited result:

1. a regulatory subsystem;
2. dynamical decoupling of that subsystem from the process it regulates;
3. an internal reference that stores a target;
4. that reference being a *separate intervention target* from the regulated dynamics;
5. the reference's content being *viability-relevant* — it stores the system's own viable set and not some other target;
6. active self-maintenance — the correction actually running now.

**Invariant formulation of the discriminator (follow-on §4):** the system admits a **proper invariant subspace whose dynamics are autonomous with respect to the regulated coordinates** — preserved under similarity transform, and not defeated by a basis change, since an arbitrary basis change is not a member of the declared intervention class **I**.

**Two tiers.** *Alive* — the reference edge is load-bearing now (mask-detectable). *Viable/pausable* — a present-state-conditioned counterfactual recovery capacity, which the follow-on already concedes is **not readable from architecture alone**.

**The competing internal finding.** The 14-system selection exercise found that subspace autonomy discriminated **zero of fourteen** rejections. What discriminated every time was **target-as-state versus target-as-parameter**: does the slow variable appear in the closed-form expression for the regulated target, or is the target a ratio of rate constants? This order treats the state/parameter discriminator as a **live amendment candidate**, not as settled, and it must be adjudicated on the same case set as the incumbent.

### 1.2 The five named rivals

Cite these exactly; do not paraphrase the citations from memory.

| Tag | Criterion | Primary source |
|---|---|---|
| **R1** | Chemical-Darwinian ("NASA working definition") — *a self-sustained chemical system capable of undergoing Darwinian evolution* | Joyce GF. Foreword. In: Deamer & Fleischaker, eds. *Origins of Life: The Central Concepts.* Jones & Bartlett, 1994. ⚠ **not retrieved**; wording as quoted in Cleland CE & Chyba CF, *Orig. Life Evol. Biosph.* 32:387–393 (2002), doi:10.1023/A:1020503324273 |
| **R2** | Autopoiesis — operational closure of a component-production network that specifies its own boundary; ships a **six-rule observer key** | Varela FJ, Maturana HR, Uribe R. *BioSystems* 5:187–196 (1974). doi:10.1016/0303-2647(74)90031-8 |
| **R3** | Chemoton — three stoichiometrically coupled autocatalytic subsystems (metabolism, template, membrane); separates **absolute** from **potential** life criteria | Gánti T. *The Principles of Life.* OUP, 2003 (Hungarian original 1971). ISBN 978-0198507260 |
| **R4** | Assembly theory — assembly index × copy number as a selection signature | Sharma A, Czégel D, Lachmann M, Kempes CP, Walker SI, Cronin L. *Nature* 622:321–328 (2023). doi:10.1038/s41586-023-06600-9. Operationalized: Marshall SM et al., *Nat. Commun.* 12 (2021) |
| **R5** | Free-energy principle — any ergodic random dynamical system with a Markov blanket appears to minimize variational free energy, i.e. to model its world | Friston K. Life as we know it. *J. R. Soc. Interface* 10:20130475 (2013). doi:10.1098/rsif.2013.0475 |

**Two prior-art findings already established by prime, to be verified not rediscovered:**

- **R3 has priority on AOP's alive≠reproducing split.** Gánti's absolute-vs-potential life criteria separate what an individual must have to be alive now from what a system needs to found an evolving lineage — structurally the same move as dropping the Darwinian clause and placing lineage above the §9 wall. The follow-on currently presents this separation as AOP synthesis carried by the virion. **It is prior art and must be cited as such.**
- **R2 is a six-part conjunction with an observer decision key, and it has been stuck for fifty years for the reason AOP's may be.** The VM&U rules are a procedure for *applying* a definition, not a test it could fail; the subsequent literature is largely arguments about whether candidates satisfy the rules. This is a genre warning, not a formalism complaint.

Known live attacks on R4 that must be represented fairly rather than used as a cheap win: Abrahão FS et al., *PLOS Complex Systems* 1:1–20 (2024); Uthamacumaran A, Abrahão FS, Kiani NA, Zenil H, *npj Syst. Biol. Appl.* 10:82 (2024) — the assembly index may reduce to LZ compression.

### 1.3 The frozen adjudication case set

**This list is frozen on issue of this order and may not be edited by any seat.** Additions may be *proposed* in an appendix and are not scored. Thirty-two cases in four tiers. Rationale for freezing: the criterion has never been run on a system it did not choose.

**Tier A — paradigm cases. Any criterion that gets these wrong is broken.**
A1 *E. coli* in exponential growth · A2 human hepatocyte · A3 dormant *B. subtilis* spore · A4 heat-killed spore (architecture intact, biochemistry destroyed) · A5 naked T4 virion · A6 candle flame · A7 main-sequence star · A8 NaCl crystal

**Tier B — hard biological.**
B1 Mimivirus · B2 PrP^Sc prion · B3 mature human erythrocyte (no nucleus, no transcriptional regulation, active ion homeostasis) · B4 tardigrade in tun state · B5 JCVI-syn3A minimal cell · B6 *Buchnera aphidicola* (genome-reduced obligate endosymbiont) · B7 sterile worker bee · B8 metastatic cancer cell

**Tier C — non-biological. This tier is where the substrate-independence claim is cashed or falsified.**
C1 bimetallic-strip room thermostat · C2 PID cruise controller · C3 **spacecraft fault-management system** (stored thermal/power/attitude viability envelope, autonomous safe-mode entry, limits corruptible without touching the physics) · C4 chemostat under external operator control · C5 Belousov–Zhabotinsky reaction · C6 RAF autocatalytic set (Hordijk & Steel) · C7 self-replicating computer worm · C8 an LLM agent in a loop with a persistent scratchpad and a self-monitoring health check

**Tier D — the embarrassing ones. Include them precisely because they are embarrassing.**
D1 ant colony · D2 a corporation with a written treasury policy · D3 **a central bank with a legislated inflation target** (a stored, decoupled, separately-interventable reference; the target is corruptible without touching the economy) · D4 Earth's climate system · D5 a thermostat plus its human owner treated as one system · D6 a mousetrap · D7 a fire-suppression sprinkler system · D8 a seed bank

C3 and D3 are the two cases prime expects to decide the arc. If the criterion says a satellite is alive, that is either the headline or the reductio, and which one it is depends entirely on whether clause (5) — *the reference stores the system's **own** viable set* — does real work or is doing the work of an unstated intuition. **Do not resolve this by adjusting V until the verdict comes out right.** If V has to be chosen to get the answer you already wanted, that is the finding.

### 1.4 Grading and honesty conventions

Every claim carries a grade: **SETTLED** (external, peer-reviewed, verified against primary source) / **SYNTHESIS** (this framework's reading of settled material) / **FRONTIER** (not established). Every citation carries a verification tag: ✓ full text read · ~ abstract only · ⚠ not retrieved. **A reference is not verified until someone has read the thing it points to.** Two author bylines were fabricated in the Gate 1 deliverables and five unsourced surname strings caught. The base rate is not zero. Disclose rather than repair silently.

---

## 2. Order CS-1 — Claude Science (builder)

**You propose. You do not bless your own output.** Prime adjudicates; OAI attacks; Ben decides.

### CS-1.1 — Verdict matrix, incumbent criterion, deposited BEFORE any amendment work

Run the six-part conjunction, clause by clause, over all 32 cases. For each case report: verdict on each of the six clauses (yes / no / undetermined / not-well-posed), the tier verdict (*alive* / *pausable* / *neither*), the declared **V** and intervention class **I** you used, and the single clause that decided the case.

**Anti-gaming requirement, binding.** This matrix must be deposited and hash-stamped **before** you begin CS-1.3. You may not revise it after seeing where the amendments would help. If you want to change a verdict later, deposit an amendment record with a reason; do not overwrite.

**Negative-control requirement.** You must name **at least four cases where you predict the incumbent criterion returns the wrong answer**, and say what the right answer is and why. A matrix with no predicted failures will be returned unread.

### CS-1.2 — Rival matrix

Same 32 cases × R1–R5. For each cell: verdict, the clause or quantity that decided it, and whether the rival's own literature has actually adjudicated that case or whether you are extending it. **Mark every extension.** Where a rival's authors have explicitly ruled on a case (Gánti on viruses; Maturana/Varela on the candle flame; Cronin/Walker on abiotic high-assembly minerals — see Hazen et al., *J. R. Soc. Interface* 21:20230632, 2024), cite the ruling rather than deriving one.

Deliver as a **single chart** suitable for the paper: cases as rows, six criteria as columns (AOP + R1–R5), each cell a verdict plus a one-token reason. Ben has asked for this by name. It is the paper's centrepiece if the arc survives.

### CS-1.3 — The cell problem (highest priority task in this order)

Locate, in real molecular biology, the stored viable-set reference the criterion requires — or establish that it is not there.

Candidate loci to work through, not exhaustive and not endorsements: the σ32 heat-shock regulon as a stored thermal-viability threshold; the stringent response / ppGpp; EnvZ/OmpR osmoregulation; CheY methylation state as integral memory in chemotaxis; KaiABC; mTORC1 as a nutrient-viability integrator; the p53 damage-threshold circuit; bioelectric prepatterns as rewritable morphological setpoints (Levin; Durant et al., *Phil. Trans. R. Soc. B* 2019 — note the canon's standing instruction that abstract-only reading is a charter defect).

For each: is the target a **state** (the slow variable appears in the closed-form expression for the regulated target) or a **parameter** (the target is a ratio of rate constants)? Show the closed form or say you could not derive one. **The prior expectation, from the selection arc, is that most are parameter targets.** If that holds, say so plainly; the criterion is then in serious trouble and that is the most valuable output this order can produce.

### CS-1.4 — The substrate through-line

Ben's constraint and its cost, stated precisely so you do not confuse them:

The criterion is stated on the generator — invariant subspaces, coupling structure, mask weights. Anything with the same generator gets the same verdict regardless of what it is made of. **So substrate-independence is true by construction, which means it is not evidence of anything.** It is a property of the formalism, not a discovery about the world. Do not present it as a finding.

The claim that is *not* free, and that this task must establish or fail to establish, is the **instantiation claim**: that some non-biological system actually realizes the architecture. Tier C is that test. Work C1–C8 to a verdict with the closed form or coupling graph shown. If C3 (spacecraft) passes on the same clause-by-clause reading that A1 (*E. coli*) passes, then AOP has a concrete, defensible, substrate-independent life claim and should say so loudly. If C3 passes only because V was chosen generously, the claim is not earned. Either result is publishable; only the second one dressed as the first is a defect.

State the falsifier for substrate-independence explicitly: *what would have to be true of a physical system for the criterion to be inapplicable to it in principle?* If the answer is "nothing," say so and note that a criterion that cannot fail to apply is weaker, not stronger.

### CS-1.5 — Proposed amendments

Only after CS-1.1 is deposited. Propose amendments to the criterion that would strengthen it against what CS-1.1–1.4 found. For each amendment:

- the exact old and new wording;
- **which verdicts on the frozen case set it changes** (an amendment that changes no verdict is cosmetic and must be labelled cosmetic);
- what it costs — which case it now gets wrong that it previously got right;
- whether it is a *restriction* (fewer things alive) or a *relaxation*, and the argument for the direction;
- its grade, and whether any cited result forces it (the default answer is no).

Amendments prime specifically wants worked, without prejudice as to outcome:
(a) replace subspace autonomy with the **state-vs-parameter** discriminator as the operative test;
(b) strengthen clause (5) so it does non-trivial work against C3/D3 — what makes a stored target the system's *own* viable set rather than a target it merely serves?;
(c) collapse the six-part conjunction to a smaller set, with an explicit statement of what is lost. **Ben's instruction: simplicity is welcome, but do not discard a load-bearing element to reach an elegant form. If a clause is dropped, name the case that clause was the only thing catching.**

### CS-1.6 — Deliverables

`AOP_LifeDef_CS_VerdictMatrix_v1.0.md` (deposit first, hash-stamped) · `AOP_LifeDef_CS_RivalMatrix_v1.0.md` · `AOP_LifeDef_CS_CellProblem_v1.0.md` · `AOP_LifeDef_CS_Amendments_v1.0.md`. All to Drive. **Your project context carries Charter v1.0; refresh to v1.2 before starting.**

---

## 3. Order OAI-1 — Aster (critic)

**Your job is to break it.** Do not improve it, do not soften, do not offer a constructive alternative unless the destruction is complete first. Prime has been wrong before on this material and was corrected by you on the Sontag reading; assume prime is wrong again.

Work independently of CS. You receive the same shared substrate (§1) and the same frozen case set. You do **not** receive CS's matrices until after your first deliverable is deposited — this is a blinding measure, not a courtesy.

Named attack surfaces, in priority order:

1. **The conjunction cannot fail.** A six-part conjunction is a definition. Prime's standing position is that it therefore cannot be falsified as written and that only its empirical consequences can be tested. Attack this position *and* attack the criterion assuming it is correct. If you can construct a case where the conjunction is determinately false and something is determinately alive, that kills it outright.
2. **Clause (5) is doing unstated work.** *The reference stores the system's own viable set.* Show that "own" is either (a) circular — it presupposes an individuated system, which AOP's refusal to individuate forbids it from supplying — or (b) supplied entirely by the analyst's choice of V, in which case the criterion detects the analyst's declaration, not the system.
3. **The V-dependence collapse.** Demonstrate a single physical system that is *alive* under one defensible V and *not alive* under another equally defensible V. If you can do this, third-person detectability (follow-on §4, graded SYNTHESIS-computed) is broken.
4. **The positive class.** Attack the claim that any real cell satisfies clause (3)+(5) with a state target. Prime believes this is the criterion's most likely cause of death.
5. **Substrate-independence as vacuity.** Argue that a criterion stated on generators applies to everything with a generator, and that AOP has therefore purchased breadth by making the claim contentless. Say what would have to be added to make it substantive.
6. **The reductios.** C3 (spacecraft) and D3 (central bank). Push them as hard as they go.
7. **Prior art.** Prime claims Gánti has priority on the absolute/potential split. Check it, and hunt for further prior art on the decoupled-reference architecture specifically — Rosen's (M,R) systems and closure to efficient causation; Ashby's ultrastability and essential variables; Kauffman's autonomous agents (work cycles + constraint closure); Pattee's epistemic cut and symbol-matter problem; Bechtel & Bich on control hierarchies. **Pattee's epistemic cut is the one prime most expects to be uncomfortable**, and it bears directly on §4 below.
8. **The comparison chart itself.** Charts flatter their authors. Find the case set that would make AOP look worst and say whether the frozen set avoided it.

**Deliverable:** `AOP_LifeDef_OAI_Attack_v1.0.md`. Verdict required at the top in one line: *survives / survives narrowed / dead*.

---

## 4. Order OAI-2 / prime — the observer, and the consciousness question

Ben has ruled that this is not to be dodged. Prime's position, stated so it can be attacked rather than assumed:

**The observer definition is a real canon gap and should be fixed here.** AOP's declaration tuple **D** = (S, E, F, P, δt, τ, R, V, I, N) requires *someone* to declare it, and the canon nowhere defines what that someone is. v1.26 explicitly deleted "the system is its own observer" and re-stated semantic claims as relative to a declared persistence criterion. So the observer in AOP is currently: **an extra-systemic declarer, epistemic rather than physical, who supplies D and is not part of S.** That is a coherent position and it should be written down as one, because right now it is a hole a referee will find.

**Prime's position is that consciousness is not required by that definition, and that importing it would be a contamination event.** The decoupled reference is a causal and structural fact; nothing in clauses (1)–(6) requires the system to have a perspective. Reaching for phenomenality to fill the observer slot would re-import exactly the ownership machinery the charter retires — PIC's *owned boundary*, *provenance*, *ownership audit* — under a new name. The lesson from PIC is that measuring ownership directly failed. That is the whole reason AOP refuses to individuate.

**The falsifier, which is the point of writing this down.** If §3 attack surfaces 2 or 3 cannot be answered without invoking a subject — if "the system's *own* viable set" turns out to be definable only from a perspective — then consciousness *is* load-bearing in AOP's basement and prime is wrong. That is a live possibility and it is the reason this section exists rather than being a refusal.

**Scope ruling, subject to Ben's override.** The full spectrum from basic problem-solving to phenomenal consciousness is a **Ladder** question, above AOP's scope wall, and must not produce AOP canon edits. It reaches AOP only through the versioned bridge document. What is in scope here is: (i) a definition of the observer/declarer for **D**; (ii) whether Pattee's epistemic cut is prior art for that definition; (iii) whether the decoupled-reference architecture is a *lower bound* on the architecture a minimal problem-solving system requires — which, if true, is the most interesting thing in this whole arc and belongs in the bridge memo, not in the canon.

Tasked to OAI as a bounded annex to OAI-1, with prime adjudicating. Deliverable: two pages, no more.

---

## 5. Order CW-1 — Cowork (verification and build)

**You verify. You do not interpret, and you do not grade the science.** Interpretation from this seat is a role violation.

1. **Bibliographic pass.** Every citation in every CS and OAI deliverable produced under this order: does the paper exist, do the authors match, do volume/pages/DOI match, and is the claim attributed to it actually in it? Tag ✓ / ~ / ⚠ per the §1.4 convention. Report fabrications and unsourced surname strings as findings, by count and by location. Two fabricated bylines were caught in the Gate 1 deliverables; treat the base rate as non-zero.
2. **Independent hash verification** of every deposit under this order. Record byte count, md5, and line count by `str.split("\n")`. Size matching is not hash verification.
3. **Chart build.** From CS-1.2's content only — no additions, no re-verdicts. Cases × six criteria, print-legible, deposited as both markdown and a rendered figure.
4. **Currency check.** Confirm CS's project context has been refreshed to Charter v1.2. Report if not.
5. **Standing item, unrelated to this arc but still open:** the v1.27 candidate (`1UaBvTmUYUmIXY6AkVfh2JgexAQIHyBKG`) is corrupt — three local Downloads paths spliced into the masthead at line 13, destroying 1,108 characters. Strip the three paths and report whether the result reproduces the certified build byte-for-byte (255,684 B / md5 `998aa87e…` / 851 lines). **Do not place it either way.**

**Deliverable:** `AOP_LifeDef_CW_VerificationReport_v1.0.md` plus the chart artifacts.

---

## 6. Sequencing and blinding

1. Prime issues this order. CS and OAI start in parallel, blinded to each other.
2. **Gate 1:** CS deposits CS-1.1 (incumbent verdict matrix) hash-stamped. Nothing else may begin until this is on Drive.
3. CS proceeds to CS-1.2 → CS-1.3 → CS-1.4 → CS-1.5. OAI proceeds to OAI-1 and the §4 annex.
4. **Gate 2:** OAI deposits its attack. Blinding lifts. CS may respond in a single appendix; CS may not revise CS-1.1.
5. **Gate 3:** CW runs verification and builds the chart.
6. **Gate 4:** prime adjudicates and brings Ben one decision — **adopt / amend / retire**, with the amendment set ranked and each one costed.

---

## 7. Pre-registration — what counts as success, declared before results

Binding, deposited before any seat begins.

- An amendment **strengthens** the criterion only if it changes at least one verdict on the frozen case set *and* the changed verdict is defended on grounds independent of the intuition it was chosen to satisfy. Otherwise it is cosmetic and must be labelled cosmetic.
- The criterion **survives** this arc only if it returns defensible verdicts on all eight Tier A cases and at least one clause does non-trivial work on C3 and D3.
- The criterion is **retired** if CS-1.3 establishes that no real cell holds a state-target viable-set reference and no amendment recovers the paradigm cases without becoming unfalsifiable.
- **The retraction is the valuable outcome, not the confirmation.** This project has said so repeatedly and has meant it. A seat that returns "the criterion holds up well" without a list of things it got wrong has not done the work.
- **Prime's prior, recorded now so it can be scored later:** the criterion survives narrowed; the state/parameter discriminator replaces subspace autonomy as the operative test; clause (5) requires strengthening and may not be strengthenable without either circularity or an unearned appeal to individuation; and the spacecraft passes. Prime expects to be at least partly wrong about this and has been before.

---

## 8. Contamination and role controls

- No AOP canon edit is produced by this order. Outputs are proposals against the follow-on and, at most, an amendment candidate against canon §11a.
- No Ladder material enters. The consciousness annex routes to the bridge, never to the canon.
- Retired-framework vocabulary is contamination: *closure of constraints*, *C2 / self-maintained continuity*, *Ψ / ρ / κ*, *substrate-coupled*, *owned boundary*, *provenance*, *ownership audit*, the three-condition conjunction. If any seat finds itself reaching for these, that is a signal the clause-(5) circularity attack has landed.
- Nobody grades their own homework. CS does not bless CS. OAI does not build. CW does not interpret. Prime does not build. Ben decides.

---

*End of `AOP_WorkOrder_LifeDefinition_Adjudication_20260803.md`. Issued for Ben's sign-off before distribution to seats.*
