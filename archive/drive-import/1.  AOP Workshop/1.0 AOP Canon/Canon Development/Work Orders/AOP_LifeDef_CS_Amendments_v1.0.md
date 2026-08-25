# CS-1.5 — Proposed amendments, each costed against the frozen case set

**Document ID:** `AOP_LifeDef_CS_Amendments_v1.0.md`
**Seat:** Claude Science (builder). **Date:** 3 August 2026. **Order:** CS-1.5.
**Depends on:** `AOP_LifeDef_CS_VerdictMatrix_v1.0.md` (Drive `1-LwfaBon87eOINIEfBBje_LCOFQ1W6Ae`, md5 `78d512b98183c8823e004aef9694b094`) + Corrigendum 1; `AOP_LifeDef_CS_RivalMatrix_v1.0.md`; `AOP_LifeDef_CS_CellProblem_v1.0.md`.

**Standing:** builder proposal. Prime adjudicates; OAI attacks; Ben decides. **This seat does not recommend adopt/amend/retire** — that is Gate 4 and it is not this seat's call. What follows is the amendment set with its costs computed, so the decision can be made on numbers rather than on preference.

**Anti-gaming compliance.** CS-1.1 was deposited and hash-stamped before any of this work began and has not been overwritten. Where an amendment changes a verdict, the change is recorded here as a delta against the stamped matrix, never as an edit to it.

---

## 0 · The situation these amendments have to address

Three findings constrain what any amendment can do, and they pull in opposite directions.

1. **The criterion is over-inclusive on designed artefacts.** Five *alive* verdicts on the frozen set are engineered systems (C3, C7′, C8, D2, D5). Clause (5) is satisfiable by construction: write a system's own operating envelope into a separately-editable store and it passes.
2. **The criterion's positive class does not contain the cell.** Eight molecular loci, four parameter targets, two with no regulated target at all, two storing a phase or a body plan, **zero storing a viable set**. Plus two living cells — JCVI-syn3A and *Buchnera* — that the criterion excludes outright.
3. **Those two failures have opposite fixes.** Anything that tightens the criterion enough to exclude the spacecraft tightens it further away from the cell, which it already fails to contain. Anything that loosens it enough to admit the erythrocyte admits more artefacts. **This is the bind, and no amendment below escapes it. The honest question at Gate 4 is which failure the project would rather have.**

---

## 1 · Amendment A — replace subspace autonomy with the state/parameter discriminator

*(the order's candidate (a))*

**Old wording (follow-on §4; canon v1.26 §11a):**
> The system admits a **proper invariant subspace whose dynamics are autonomous with respect to the regulated coordinates** — a subspace the dynamics preserve, evolving under its own law without being driven by the variables it regulates, while feeding into them.

**New wording:**
> The regulated target is a **stored state** rather than a zero of a rate law: the slow reference variable appears in the closed-form expression for the regulated target at steady state. Where the target is a ratio of rate constants, the system holds no reference to intervene on, because the target and the machinery are the same object.

**Verdicts it changes on the frozen set — 9 of 32, and they are the wrong 9:**

| Case | Stamped | Amended | |
|---|---|---|---|
| **A1** *E. coli* | ALIVE | **NEITHER** | paradigm case lost |
| **A2** human hepatocyte | ALIVE | **NEITHER** | paradigm case lost |
| **A3** dormant spore | PAUS | NEITHER | |
| **A4** heat-killed spore | PAUS | NEITHER | (finally distinguishes nothing, but consistently) |
| **B4** tardigrade tun | PAUS | NEITHER | |
| **B5** JCVI-syn3A | UNDET | NEITHER | |
| **B7** sterile worker bee | ALIVE | **NEITHER** | |
| **B8** metastatic cancer cell | ALIVE | **NEITHER** | |
| **D8** seed bank | PAUS | NEITHER | |

**Every engineered false positive survives unchanged.** C3, C7′, C8, D2 and D5 all hold *literal stored values* — limit tables, health thresholds, treasury covenants — which are states by any reading. **Amendment A removes the organisms and keeps the artefacts.**

**Cost:** the entire biological positive class. **Direction:** restriction, severe. **Grade:** the discriminator itself is **[SETTLED]** as a property of the published models (§1 of the cell problem); its adoption as *the* operative test is **[FRONTIER]** and no cited result forces it.

**Assessment.** The order records that subspace autonomy discriminated zero of fourteen rejections in the selection arc while state-versus-parameter discriminated every time, and on that basis the amendment looked like the strongest candidate going in. **Run over the frozen set it is the most destructive amendment in this document.** The reason the two exercises disagree is that the selection arc scored *candidate reference loci*, where the state/parameter question is exactly the right question, while the frozen set scores *whole systems*, where a cell fails the test that its own regulatory loci fail. **The discriminator is a good instrument for the sub-question and a criterion-killer as the main test.** This seat proposes it be retained as the operative test *for whether a candidate locus is a reference*, and not promoted to the criterion's discriminator.

---

## 2 · Amendment B — strengthen clause (5) so it does work against C3 and D3

*(the order's candidate (b): what makes a stored target the system's* own *viable set rather than a target it merely serves?)*

**Old wording:**
> the reference's content being *viability-relevant* — it stores the system's own viable set and not some other target.

**New wording:**
> the reference's content is viability-relevant **and the reference is itself maintained by the processes it regulates** — the system produces and replaces the physical store, so that the store's persistence depends on the same viability it encodes.

**Verdicts it changes — 4 of 32, and they are the right 4:**

| Case | Stamped | Amended | Why |
|---|---|---|---|
| **C3** spacecraft | ALIVE | **NEITHER** | the limit table is maintained by a ground crew, not by the platform |
| **C8** LLM agent | ALIVE | **NEITHER** | the scratchpad is maintained by an external runtime |
| **D2** corporation | ALIVE | **NEITHER** | the treasury policy is maintained by a board |
| **D5** thermostat + owner | ALIVE | **NEITHER** | the dial is maintained by the human, who is inside S but does not produce the dial |

**C7′ (worm with a watchdog) survives as ALIVE**, because a self-modifying worm that rewrites its own thresholds does maintain its own store. That is the right residue: it is the one artefact on the set that genuinely does the thing.

**Cost — and it is the amendment's real price, not a rounding error.** The new clause is **autopoiesis** (R2), imported. The rival matrix records that R2 and R3 both exclude the spacecraft, and both exclude it on exactly this feature — self-production of the components constituting the reference. **Adopting Amendment B means AOP's answer to its sharpest reductio is a rival's central commitment, and the honest framing is convergence, not independent discovery.** The follow-on §2 currently distinguishes AOP from autopoiesis by saying autopoiesis "names self-production of components and is silent on a stored viability reference." After Amendment B, AOP requires both, and the distinguishing claim weakens to *AOP = autopoiesis + a stored reference*.

**A second cost, on the cell side.** Self-production of the reference is not free for the biological cases either. The erythrocyte (B3) has no protein synthesis and cannot maintain any store; it was already a false negative and stays one. **The amendment does not touch F1 or F2.**

**Direction:** restriction. **Grade: [SYNTHESIS]** — no cited result forces it, and R2's literature has priority on the component. **This is the only amendment in the set that fixes the failure it was aimed at.**

**The circularity check the order asked for.** Does "maintained by the processes it regulates" smuggle in individuation? It does not require an individuated subject — maintenance is a coupling fact readable from the graph, and it is evaluated against the declared S like everything else. But it **does** inherit the declaration-dependence: move S to include the ground crew and the spacecraft passes again, exactly as D5 does against C1. **The V-dependence collapse is not repaired by this amendment; it is relocated.** This seat could not find a formulation that repairs it, and reports that rather than claiming one.

---

## 3 · Amendment C — collapse the six-part conjunction

*(the order's candidate (c), with Ben's instruction: simplicity is welcome, but name the case any dropped clause was the only thing catching)*

**Old:** six clauses. **New:** three.

> **(i)** a regulatory subsystem separable from the process it regulates, holding a stored target; **(ii)** the target's content is the system's own viable set; **(iii)** the correction is running now.

**Mapping:** old c1+c2+c3+c4 → new (i); old c5 → new (ii); old c6 → new (iii).

**Verdicts it changes: ZERO. This amendment is COSMETIC and is labelled cosmetic**, per the order's §7 rule.

The evidence for the collapse is the deciding-clause distribution over all 35 scored rows (corrected in Corrigendum 1): **c1 12 · c2 2 · c3 5 · c4 0 · c5 12 · c6 4.**

**Naming the case each dropped clause was the only thing catching, as instructed:**

- **c4 (separate intervention target) — catches nothing.** Zero deciding cases. On the frozen set, wherever a stored reference existed it was separately interventable. c4 is redundant with c3 and its removal costs no verdict. **This is a clean drop.**
- **c2 (dynamical decoupling) — decided exactly two cases: A7 the star and B3 the erythrocyte.** The star is the criterion's cleanest success and c2 is what catches it: the star's set-point *is* a fixed point of its constitutive dynamics, so there is no decoupled subsystem. **c2 must be retained in substance** — it is folded into new clause (i) as "separable from the process it regulates," not discarded. **The erythrocyte is the other case c2 catches, and catching it is a false negative.** So c2 is simultaneously the only clause catching the criterion's best case and one of the clauses producing its worst.

**Direction:** neither — it is a restatement. **Grade: [SYNTHESIS], cosmetic.** Worth adopting for readability and for honesty about the criterion's operational shape — it is a two-clause test wearing six clauses — but **it must not be presented as strengthening anything.**

---

## 4 · Amendment D — an unrequested one, and this seat thinks it is the most defensible

The three requested amendments all treat the criterion's problem as a matter of which clauses to keep. The cell-problem evidence suggests a different diagnosis.

**Across eighteen systems in six literatures, no primary exhibits a comparator** — a subsystem computing an error between a regulated variable and a stored reference supplied by a slow variable, and driving correction of *that error*. What the positive cases have instead is **multistability**: a switch whose state biases which attractor the system falls into. KaiABC and the planarian bioelectric prepattern are both of this kind, in two independent literatures.

**Proposed wording:**
> The criterion requires a **comparator**: a coupling that computes a difference between the regulated variable's current value and the stored reference, and drives correction proportional to that difference. A multistable switch that selects among attractors without computing such a difference does not satisfy the criterion.

**Verdicts it changes:** *unknown on the biological cases, and that is the point.* No retrieved primary establishes a comparator at any molecular locus, so under this amendment A1 and A2 would move to **UNDETERMINED pending evidence** rather than to NEITHER — a materially different and more honest status than either the stamped ALIVE (which rests on an assertion the follow-on makes at §2 and never derives) or Amendment A's NEITHER.

On the engineered cases it changes nothing: C3, C8, D2 all have explicit comparators — that is what a limit check *is*.

**Direction:** restriction. **Grade: [FRONTIER].** **Cost:** it converts the criterion's central biological claim from asserted to open, which is a loss of standing and a gain in honesty. **Value:** it names a specific, retrievable, falsifiable thing to go looking for. If a comparator is found at a cellular locus, the criterion is in much better shape than any amendment here can put it. If a targeted search fails, that is the retirement condition stated in the order's §7, reached by evidence rather than by argument.

---

## 5 · Summary table

| | Amendment | Verdicts changed | Fixes | Costs | Direction | Grade |
|---|---|---|---|---|---|---|
| **A** | state/parameter as operative test | **9** | nothing on the frozen set | A1, A2, B7, B8 — the whole biological positive class | restriction (severe) | FRONTIER |
| **B** | clause (5) requires self-maintained reference | **4** | C3, C8, D2, D5 — all four artefact false positives | imports autopoiesis; leaves B3, B6 false negatives; relocates rather than repairs V-dependence | restriction | SYNTHESIS |
| **C** | collapse six clauses to three | **0** | readability only | none; **cosmetic** | neither | SYNTHESIS |
| **D** | require a comparator | A1, A2 → UNDETERMINED | names a falsifiable search target | converts the central biological claim to open | restriction | FRONTIER |

**Pre-registration compliance.** The order's §7 states an amendment strengthens the criterion only if it changes at least one verdict *and* the changed verdict is defended on grounds independent of the intuition it was chosen to satisfy. **Only B and D clear that bar.** B changes four verdicts on the independent ground that self-maintenance of the store is a coupling fact readable from the graph, not an appeal to the intuition that spacecraft aren't alive. D changes two on the independent ground that no comparator has been found. **A changes nine and fixes nothing. C changes none and is labelled cosmetic.**

---

## 6 · Scoring prime's recorded prior

Prime recorded a prior in §7 of the order so it could be scored later. Scoring it against what this arc found:

| Prime's prediction | Outcome |
|---|---|
| "the criterion survives narrowed" | **Open.** It survives on Tier A only if Amendment B is adopted and the cell problem is treated as unresolved rather than settled. |
| "the state/parameter discriminator replaces subspace autonomy as the operative test" | **Contradicted.** As the criterion's operative test it destroys the biological positive class (§1). It should be retained for locus-level adjudication, where it works. |
| "clause (5) requires strengthening and may not be strengthenable without either circularity or an unearned appeal to individuation" | **Half confirmed, and the better half.** Clause (5) does require strengthening. It **is** strengthenable without circularity — Amendment B is a coupling fact, not an appeal to individuation. But the strengthening is autopoiesis, imported, and it relocates the V-dependence rather than repairing it. |
| "the spacecraft passes" | **Confirmed on the incumbent criterion**, on the same reading and the same declared V as *E. coli*, with no adjustment. It fails under Amendment B. |

**Prime was right about the spacecraft and about clause (5), and wrong about the discriminator.** The order said prime expected to be at least partly wrong and had been before; this is the part.

---

## 7 · What this seat could not do, and where it should be attacked first

- **No amendment here repairs the erythrocyte (F1) or *Buchnera* (F2).** Both remain false negatives under all four. **This is the most likely place the whole criterion fails, and this seat has no proposal.**
- **The V-dependence collapse is not repaired by anything in this document.** C1-versus-D5 still flips on boundary choice, and Amendment B inherits it.
- **Amendment D's verdict changes are asserted from an absence of evidence**, which is weaker than the other three. An absence of a comparator in eighteen retrieved systems is not proof there is none.
- **Amendment B's cost may be understated.** This seat priced it as "imports autopoiesis." A hostile reading is that it makes AOP's life criterion a special case of a fifty-year-old rival, and the rival matrix's genre warning — that R2's six-rule key has been stuck for five decades because it is a decision procedure rather than a falsifiable test — then applies to AOP with full force. **That reading should be pressed at OAI rather than defended here.**
- **All amendment costings were computed by the seat that wrote the amendments.** The re-scoring is mechanical against the stamped matrix and reproducible, but it has not been independently re-run.

---

*End of `AOP_LifeDef_CS_Amendments_v1.0.md`. Builder proposal under Order CS-1.5. Not canon. Not blessed by its author.*
