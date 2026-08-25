# Prime's adjudication — Gate 1 selection report

**Document ID:** `AOP_LifeCriterion_Gate1_PrimeAdjudication_v0_1_20260803.md`
**Seat:** prime (chat seat), 3 August 2026
**Adjudicates:** `AOP_LifeCriterion_SystemSelection_Report_v1_0_20260803.md` (`1TMyzJW7…`) and `AOP_LifeCriterion_RejectionLog_v1_0_20260803.md` (`1G30cFWNA5VeAmbDkx0Lu69hi5RSewxIo`)
**Parent freeze:** `1-HkXf58z-UWnYVkT1mcNR3_y2hIi3PAy`, md5 `b7eebcfd5a371a78b33a5fe230d52554` — confirmed independently by the builder seat this session; the Cowork check is discharged.
**Standing:** prime's determination. Subject to OAI attack before the pre-registration freezes. Adds no decision to Ben's three.

**Verification tier of this document.** Prime read the rejection log in full and confirmed all deposits by folder listing. Prime has **not** read the 42 KB selection report or the five track-evidence files end to end this session. The rulings below turn on structure and logic rather than on retrieved literature, and are marked where they depend on the builder's retrieval.

---

## 1 · The P1 threat at §3.3.1 — the objection fails, but it exposes a worse problem

**The builder's charge.** Excluded systems (native and engineered EnvZ/OmpR, chemotaxis) have published operations that shift the output while regulation keeps running. The escape — that changing a rate constant is a machinery change, not a set-point move — is the same argument that rejected those systems at S.2, and cannot be applied in one direction only.

**Ruling: there is no double standard.** S.2 asks where the target lives; P1 asks whether the target can be displaced with the machinery intact. In a system whose target *is* a ratio of rate constants, those two operations are **the same operation by construction**. An excluded system shifting its output under a rate-constant change is not a counterexample to P1; it is a restatement of why it was excluded. One claim, stated twice: in a parameter-target system, target and machinery are not separable. Consistent in both directions.

**But the defence costs more than the builder noticed.** If P1's kill condition reduces to *"an excluded system displaces its target with all rate constants fixed,"* and having a state-target just is *"the target can move with rate constants fixed,"* then **P1 has collapsed back into the definition.** The arc escaped the definitional trap for exactly one step and landed in it again. That is the real finding at §3.3.1, and it is more serious than the inconsistency charge it was filed under.

**The repair — P1 becomes a claim about phenotype, not about intervention.** Competent misregulation is target displacement **with the dynamic properties preserved**: gain, settling time, adaptation precision, disturbance rejection. In a parameter-target system the constants that set the target also set those properties, so displacement should generally **drag them** — the target and the dynamics move together. In a state-target system the target moves along a direction orthogonal to them. That dissociation is measurable, and it can come back wrong: if the engineered EnvZ cycle tunes across its output range with settling time and precision unchanged, P1 in this form is genuinely threatened by an excluded system, which is exactly the kill condition the freeze names.

This is an **operational refinement, not an amendment.** The frozen text specifies "intact, precise regulation toward a wrong target"; the phenotype reading is what that sentence already means, made measurable. It enters the pre-registration as the operational definition of *competent* and *intact*, with the dissociation test named.

**Consequence for selection:** the engineered EnvZ cycle is now a required arm, not an incidental finding. It is the sharpest available test of P1's second kill condition.

---

## 2 · S.4 and P2 — split P2 off the positive article

**The builder's finding.** No candidate clears S.4. For KaiABC the shortfall is architectural: the ~10× period range comes only from *kaiC* point mutations (machinery edits), and the two benign actuators are barred by design — temperature compensation holds Q10 ≈ 1.02–1.04, and ATP/ADP holds period within 5% while phase moves freely. P2 therefore heads for UNINFORMATIVE by construction. `[builder-retrieved; not re-verified by prime]`

**Ruling: correct, well flagged, and fixable — P2 does not belong on the positive article.**

P2 is not a claim about an organism. It is a claim about **the method**: that the verdict does not depend on the magnitude of the slow/fast ratio. It is testable wherever the ratio is freely tunable, which includes the synthetic antithetic controller and purpose-built in-silico constructs, none of which need satisfy the criterion. Running P2 on a positive article was an unexamined assumption in the work order, not a requirement of the science.

**Honesty about the freeze.** The frozen text's UNINFORMATIVE row for P2 reads "the achievable range on **the chosen system**," singular. Assigning P2 to a second article is therefore recorded as a **declared reading of the freeze**, filed before any data, with this reasoning attached. It is not presented as neutral. If Ben prefers, it can instead be a recorded amendment; either is clean, and silence would not be.

**One observation held deliberately outside the scoring rule.** That temperature compensation makes the ratio *unmovable by benign means* is arguably itself evidence for what P2 asserts — the architecture holding its verdict invariant against the perturbation that would expose a knee. Prime notes this and **refuses to let it into the pre-registration**, because a claim that converts an uninformative result into a win is the definition of an unfalsifiable design. It may be discussed after scoring; it may not be pre-registered.

---

## 3 · Reading A versus Reading B — adopt Reading B, and the defect is in the canon, not the draft

**Correction to the builder's framing.** The report attributes the strict formulation to follow-on §4. It is **also in the canon core**, at v1.26 §11a, graded SYNTHESIS: *"a proper invariant subspace whose dynamics are autonomous with respect to the regulated coordinates."* Prime read that line directly from the hash-verified master on 1 August. This is a **canon defect, not a draft defect**, and it is the second one found in §11a's neighbourhood this week.

**Ruling: Reading B.** Three independent grounds.

1. **Sontag's internal-model theorem.** If it says what the builder reports, Reading A excludes the architecture a published theorem identifies as *necessary* for adaptation. `[builder-retrieved; prime has not read the primary — this must be verified before the ruling is folded anywhere]`
2. **Reading A and S.5 are jointly unsatisfiable.** Strict autonomy is demonstrable only in the reconstituted preparation, which has no viable set and no lifetime. A criterion for *life* satisfiable only by preparations that cannot persist refutes itself.
3. **Reading A did no work.** All thirteen rejections hold under both readings; the builder checked this explicitly and made it the log's main structural claim. Reading A buys nothing empirically and costs a theorem.

**The larger proposal, and the most valuable thing in the builder's report.** The filter that actually discriminated across fourteen systems in four literatures was **target-as-state versus target-as-parameter**, verified from published closed forms, identical under both readings. Subspace autonomy discriminated nothing. Prime proposes that §11a's discriminator be **restated in those terms**: not *autonomy of the reference subspace*, but *whether the regulated target is a stored state or a zero of a rate law*. It is crisper, mechanically checkable against any published model, survives Sontag, and is what the evidence actually used. Filed as a canon change proposal against §11a, to be attacked before drafting.

---

## 4 · Where prime dissents from the builder's reading of its own result

The report treats 13-of-14 target-as-parameter as two-ways-ambiguous — either the criterion has teeth, or its positive class is nearly empty. **Prime reads it more sharply and less comfortably.**

The single positive instance found among well-characterised molecular regulators is a **clock** — a system whose stored state models *external time*, not its own viable set. The criterion was built from the cell as its paradigm case. If the cell's own regulators are target-as-parameter, and the only state-target exemplar in four literatures is a borderline case the report itself declines to resolve (rejection log, item 5), then we may have built a criterion whose positive class does not contain the thing it was built to describe.

That is not a P1 or P2 kill — those are frozen and defined, and this is neither. It is a **design-level warning** and it should be recorded now, before data, so it cannot later be read as a post-hoc excuse. If the clock is the only member, the honest headline is not "the criterion has teeth." It is "the criterion may be selecting the wrong thing."

---

## 5 · The fabricated attributions

Two fabricated bylines committed, five unsourced surname strings caught in total, all disclosed visibly rather than repaired silently, with a ledger note naming the defect class. **That is the correct response and prime records it as such.**

It also raises the required tier on everything downstream. Five caught in one exercise means the base rate is not zero, and these deliverables are about to become the substrate for a freeze. **Task for Cowork:** an independent bibliographic pass over every citation in the v1.0 report, rejection log, and five track-evidence files — author lists checked against a retrieved record, not against the seat's recall. Report as a defect count. Do not repair; report.

---

## 6 · Housekeeping

- The builder's project context carries **Charter v1.0**; Drive carries **v1.2**. Refresh the builder's project. Governance-only, but the startup block exists to catch exactly this.
- **Two copies of the work order** now sit in the folder — `11YYUfUeisfzS3Wjv5sXG9TACmf5O6csQ` (prime's deposit) and `1WPywfir9ywmjL6qVXG5qLdK0X6ifRe_h` (duplicate). Byte-identical at 9,321. Prune one.
- Interim `v0_1` and `v0_2_CORRECTED` deliverables remain in the folder. The connector cannot delete; **Ben trashes manually.** Version stamps make the current set identifiable meanwhile.
- Still open and unblocked: the missing tracking-relation slot in **D** (§12″ enumerates ten, none of them a tracking relation), and the corrupt v1.27 candidate deposit.

---

*End of `AOP_LifeCriterion_Gate1_PrimeAdjudication_v0_1_20260803.md`. Prime's determination, written to be attacked. Not self-certified; §3's Sontag ground and §2's period-range figures rest on builder retrieval prime has not re-run.*
