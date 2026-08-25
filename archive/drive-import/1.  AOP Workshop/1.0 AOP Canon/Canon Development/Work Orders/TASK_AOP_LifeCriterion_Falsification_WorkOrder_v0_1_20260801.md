# Work order — put the life criterion at risk

**Document ID:** `TASK_AOP_LifeCriterion_Falsification_WorkOrder_v0_1_20260801.md`
**Issued by:** prime (chat seat), 1 August 2026
**Authority:** Ben's instruction of 1 August 2026 — face the life claim head-on, build a test that can lose, pay for the hard predictions.
**Status:** PROPOSAL. Prime drafted it; prime does not authorize it. Ben rules.
**Filing:** `Canon Development / Work Orders` — folder `10S59I_-xmcP1rdCV1xMygwJDB0ZALRTr`

**Design constraint, stated first because it governs the rest:** the workflow is built to survive its weakest link, which is the number of decisions routed through one person. Ben has **three** decision points in the whole arc. Everything else runs seat-to-seat. If a proposed addition to this order adds a fourth, it is probably wrong.

---

## 0 · One ruling has to come before anything else

**The sporulation phosphorelay is already spoken for.** It is the declared system for the external benchmark (H4/RED-25), and that benchmark has its own conditions file, its own rejected-candidates record, and its own contamination bookkeeping. Running the life-criterion experiment on the same system creates a problem that is cheap to avoid now and expensive later: **a seat that reads the sporulation literature for this experiment is contaminated for the benchmark, and vice versa.** Two independent tests sharing one answer key are not two independent tests.

Three ways out. Ben picks one before any other work starts.

- **(a) Different system.** The life experiment gets its own candidate, selected fresh. Costs a selection cycle; keeps both tests clean. Prime's recommendation.
- **(b) Explicit merge.** One system, one pre-registration, both questions scored off the same run, contamination accepted and declared once. Cheapest in effort; the cost is that a bad system choice now damages both workstreams.
- **(c) Benchmark yields.** The life experiment takes sporulation; H4/RED-25 re-selects. Only sensible if the phosphorelay is genuinely the best article for *this* question, which prime has not verified.

**Nothing below is authorized until this is ruled.** This is Ben's decision #1.

---

## 1 · What is actually being tested

The six-part conjunction as written is a definition, and definitions cannot fail. The experiment therefore does not test "is this the right definition of life." It tests **consequences the architecture must have if the criterion is tracking something real.** Three candidate predictions, in descending order of how much they cost us if they come back wrong:

**P1 — Competent misregulation exists.** A system with a genuinely decoupled reference has a failure mode a model-free corrector cannot have: corrupt the stored set-point without damaging the regulatory machinery and you get intact, precise regulation toward the *wrong* target. A star can only be degraded — it has no separable target to move. Prediction: for any system the criterion calls alive, such an intervention exists. Failure: a paradigm case where no intervention at any level produces competent misregulation, or a non-living system where one does.

**P2 — No knee.** The discrimination is claimed to be architectural, not a magnitude of timescale separation. Prediction: on a real system, the verdict holds flat across orders of magnitude of the slow/fast ratio, with no threshold. Failure: a knee. Cheap to run, cheap to lose, and it directly tests a claim the draft already makes.

**P3 — The architecture buys lifetime.** AOP's primitive is mean first-passage time out of the viable set. The criterion currently says nothing about whether decoupled regulation *helps*. Prediction: under a declared perturbation class, systems with the architecture show longer lifetime than matched systems without it. Failure: no effect, or the wrong sign.

P3 is the one that would make this material belong inside AOP rather than beside it. It is also the most likely to fail. Prime recommends carrying all three and scoring them separately — a mixed result is more informative than a single verdict, and the framework survives losing P1 or P3 in a way it does not survive losing all three.

---

## 2 · The arc: three gates, four seats

### Gate 1 — Design and freeze

**Prime** drafts the pre-registration: the three predictions restated operationally, the declaration tuple **D** fully populated (including **V** — there is no reading without it), the intervention class **I**, the perturbation class for P3, and the scoring rule. Also drafts the separability test that replaces the toy shortcut (see §4).

**OAI / Aster** attacks the pre-registration **before it freezes.** This is the highest-value moment for the critic and the cheapest moment to change anything. The brief is narrow: *find the version of this experiment that cannot fail, and show us where we built it.* Attacks land as a written deposit.

**Prime** revises. **Cowork** deposits, hashes, and records the timestamp.

**Ben** freezes. This is **decision #2**, and it carries one thing beyond approval — see §3.

### Gate 2 — Run

**Claude Science** builds and runs against the frozen pre-registration. The freeze is what makes this safe: with the predictions locked and hashed, the runner cannot tune toward a desired result, so the usual "builder can't score" worry is discharged by the pre-registration rather than by adding another seat.

In parallel and independently, **OAI / Aster** runs the rivals — autopoiesis, metabolism-first, and one information-theoretic account — on the same case, scored by the same rule, with the explicit brief of **making a rival win.** Not a fair-minded comparison; an adversarial one. "Internally consistent" is not "better than," and the only way to learn otherwise is to let someone try to beat us.

**Cowork** handles retrieval, deposits, and hash verification of every artifact. No adjudication.

### Gate 3 — Score and rule

**Prime** scores the run against the frozen predictions and writes the verdict, including any retraction. **OAI / Aster** attacks the verdict. **Ben** rules. **Decision #3.**

---

## 3 · What Ben actually does

1. **Rule §0** — which system, one of three options.
2. **Freeze the pre-registration** — and, in the same act, commit in writing to what happens if it dies. This is the part that cannot be deferred. Bind-before-freeze means declaring *now* which results retract the criterion outright, which merely narrow it, and which are uninformative. Deciding that after seeing the data is how a test stops being a test.
3. **Rule on the verdict.**

That is the whole list. If a seat asks Ben for anything else, the answer is that the seat should decide it and record the decision.

---

## 4 · Two build items that are not details

**The separability test.** The follow-on's detectability result operationalizes "separable from the fast regulated path" as "not the regulated node," which isolates the reference only because the toy model has no other nodes. On any real system this evaporates. A genuine separability criterion is a prerequisite for P1 and P2, not a refinement of them. If it cannot be built, the experiment does not run — and that itself is a finding worth having.

**Dynamics, not topology.** Step 0 established that AOP's axes are not computable from a wiring diagram: Drive is identically zero at detailed balance, and Memory is undefined without a declared process. This rules out any candidate system for which we have structure but not dynamics and interventions, and it narrows the field hard. System selection under §0(a) must apply this filter first.

---

## 5 · What this order does not do

It does not authorize any canon edit. It does not touch the Ladder, and no Ladder-born material bears weight anywhere in it. It does not resolve the two open AOP-side items from the 1 August brief — the missing tracking-relation slot in **D**, and the corrupt v1.27 deposit — both of which stand separately and neither of which blocks this work.

---

## 6 · Where prime expects this to break, stated in advance

- **P1 may not be cleanly losable.** "No intervention at any level produces competent misregulation" is a universal negative, and failing to find one is weak evidence. The pre-registration has to specify a bounded search, declared in advance, or P1 quietly becomes unfalsifiable in the same way the definition was.
- **One system is one system.** A result on a single organism is a result on a single organism. This arc should be built so a second case can be run against the same frozen predictions later without re-designing anything.
- **The rival run may be the most informative part and the least controlled.** Adversarial framing is the right call, but it means the rival result arrives with an advocate attached. Score it against the same rule, not against the advocacy.
- **Prime wrote this and prime scores Gate 3.** That is a self-grading risk. It is mitigated by the freeze and by OAI's attack on the verdict, not eliminated. If Ben wants it eliminated, Gate 3 scoring moves to a fresh seat and prime advises only — at the cost of one more handoff.

---

*End of `TASK_AOP_LifeCriterion_Falsification_WorkOrder_v0_1_20260801.md`. Proposal for Ben's ruling. Not authorized. Not self-certified.*
