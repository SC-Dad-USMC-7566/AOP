# Tasking Order — AOP External Benchmark (H4 / RED-25)

**To:** Claude Cowork (execution seat)
**From:** Prime (chat seat), on Ben's decision ("I accept all challenges" — stiff gate)
**Date:** 25 July 2026
**Status:** This is the one build in the remediation cycle that introduces new empirical work. It is governed by pre-registration. Read the whole order before touching any data.

**Companion:** implements the deferred item of `TASK_CW_AOP_v1.25_to_v1.26_RedTeam_Remediation`. That order was subtraction; this one is the single item that was always going to require building something the framework could fail.

---

## 0. The point of this task, stated so it cannot be lost

Every computation in AOP to date is a self-consistency demonstration. The framework has never produced a result it could have gotten wrong against an answer key it did not write. This task builds exactly that and no more: **a real system, an externally-established ground truth, a pre-registered pass/fail line frozen before any AOP quantity is computed, and a named rival that gets a fair run.**

The deliverable is **not** "AOP passes." The deliverable is **a verdict** — pass or fail — that was capable of coming out either way. A build that can only pass is a rebuild of §11b at larger scale and is worthless here. If, at the end, the four-axis coalition read does not recover a distinction the rival provably loses, that is a **recorded failure**, it goes in the canon's status table as a failure, and it is the most valuable thing this project could produce short of a pass. **Ben has explicitly accepted this outcome.** Do not engineer around it. Do not tune to it. Do not, on seeing a failing result, reopen the pre-registration.

**The one rule that governs everything below: the answer key and the pass/fail gate are frozen and hashed before a single AOP quantity touches the real data.** This is bind-before-freeze, and it is not negotiable. Violating it silently is the worst thing you could do on this project, worse than a failed benchmark, because it destroys the thing the benchmark exists to create.

---

## 1. Structure of the build — five phases, hard walls between them

The phases are walled so that no downstream choice can leak back and soften an upstream commitment. Deliver each phase as its own file. **Do not begin a phase until the prior phase's file is frozen** (committed, hashed, deposited).

- **Phase A — System selection and ground-truth extraction.** Pick the system; extract the externally-established causal/structural facts; write the answer key. No AOP anywhere in this phase.
- **Phase B — Pre-registration.** Declare the tuple, the panels, the rival, the mapping from AOP outputs to answer-key predictions, and the explicit pass/fail gate. Freeze and hash. No data computed on yet.
- **Phase C — Blind computation.** Compute the AOP quantities and the rival's quantities on the system. First time real data is touched by either method.
- **Phase D — Adjudication.** Apply the frozen gate. Record the verdict.
- **Phase E — Handback.** Package for Prime's independent re-run and Aster's attack.

---

## 2. Phase A — System selection and ground truth

### A.1 Selection criteria (all must hold)
1. **External, published ground truth.** The load-bearing structure — which nodes/reactions are essential, which are redundant (parallel routes whose individual removal is tolerated), which are synergistic (jointly essential, individually dispensable) — is established in the peer-reviewed literature by someone other than us, ideally by direct experiment (knockout, deletion, perturbation) rather than by modeling.
2. **A measured persistence-like outcome.** There is a real measured survival/viability/persistence readout under perturbation — growth/no-growth, survival fraction, recovery, maintenance of a homeostatic variable — that a persistence functional V can be honestly mapped onto. Not a proxy we invent; a number someone measured.
3. **Perturbation data exists.** Single and, where available, combinatorial perturbations (double knockouts, epistasis) are in the literature, because the redundancy/synergy distinctions are exactly what separates the four-axis coalition read from a single-axis one, and those live in the *combinatorial* data.
4. **Tractable state space.** The dynamics can be written as a mass-action / Markov / Boolean / ODE model small enough to compute AOP quantities on in closed or near-closed form, in the spirit of the deposited Schlögl work — not a genome-scale network requiring estimation on ill-conditioned data (the PIC lesson: prefer analytic to estimated).
5. **Not already AOP-contaminated.** The system has not been looked at through AOP's lens. **This rules out the Schlögl network** — you already know its verdict, and a pre-registration on a known answer is not a pre-registration. Schlögl may be used only as a *methods shakedown* (see A.4), never as the benchmark system.

### A.2 What to deliver in Phase A
- **Two or three candidate systems**, each with: the published source(s) for its causal structure; the specific perturbation/knockout data and its source; the measured persistence outcome and its source; a sketch of the tractable dynamical model; and an honest note on where the ground truth is solid versus contested.
- **Candidate classes to consider** (not prescriptive — propose what the literature actually supports best):
  - A small microbial regulatory or metabolic circuit with published knockout/epistasis data and a growth/survival readout (e.g. a well-characterized two-component system, a stress-response module, a small essential sub-network with known redundant paralogs).
  - A synthetic biology circuit (toggle switch, repressilator, autocatalytic/protocell compartment) with published perturbation response and a maintenance readout.
  - A minimal autocatalytic set / (M,R)-system or CRN with literature-established essential-vs-redundant reaction structure and a persistence measure.
- **Your recommendation** among them, with reasons, but **Ben picks the system.** Do not proceed to Phase B on your own choice. This is the one place the order deliberately stops and waits.

### A.3 The answer key
Once Ben picks, extract from the literature — **before any AOP computation** — a frozen answer key stating, for the chosen system:
- which mechanisms are **essential** (removal collapses persistence),
- which are **redundant** (individually removable, jointly essential — the coalition signature),
- which are **synergistic** (individually near-inert, jointly load-bearing),
- which are **inert/spectator** (removal changes little),
- and the **rank or partial order** of mechanisms by persistence impact, to whatever resolution the data supports.

Cite the primary source for every entry. Mark each entry's confidence (direct experiment / inferred / contested). Where the literature is genuinely ambiguous, say so and **exclude that mechanism from the gate** rather than guessing — the gate is scored only on entries the literature settles.

### A.4 Provenance discipline (the project's standing rule)
Never claim a source verified on title or abstract alone. For every answer-key entry, the passage establishing it must be retrieved and quoted, or the entry is marked inferred/contested and kept out of the scored gate. If retrieval fails for a load-bearing source, say so plainly — an unretrieved essential-gene claim is not an answer key. Prime will line-check the answer key against the primary sources before Phase B freezes, exactly as with the red-team retrieval set.

---

## 3. Phase B — Pre-registration (freeze before any data)

Write and **hash** a pre-registration document containing all of the following. Once hashed and deposited, it does not change. If Phase C reveals the pre-registration was ill-posed, you **stop and report** — you do not quietly amend it.

### B.1 The declaration tuple D
Fully specified for the chosen system: system variables S, environment E, interface F, partition P, time grain δt, horizon τ, **reversal convention R** (now load-bearing per v1.26), viability functional V on its declared viable set, intervention class I, normalization N. Every slot filled with a justified choice. V must map onto the *measured* persistence outcome from A.2, not a convenient surrogate.

### B.2 The panels to compute
Which proxies on each of the four axes will be computed (Boundary B1/B2/B4; Drive σ and housekeeping; Memory E and companions; Integration total correlation, minimum-cut dependence). Named now so the choice cannot be made after seeing which one works.

### B.3 The coalition object
The mask output that will be compared to the answer key: minimal failure cut sets, minimal viability-preserving sets, and the redundancy/synergy classification per the promoted coalition semantics (v1.26 §3, §11). State the exact procedure mapping AOP's coalition output onto the answer key's essential/redundant/synergistic/inert labels and rank. **This mapping is frozen here** — you may not, after seeing results, redefine what counts as AOP calling a mechanism "redundant."

### B.4 The rival
At least one named single-axis account, run with **its own operational definition**, not a strawman. The honest candidates:
- a pure **coupling-strength / correlation** read (rank mechanisms by interaction magnitude),
- a pure **flux / dissipation** read (rank by throughput or entropy production),
- a pure **connectivity / centrality** read (rank by graph degree or betweenness).
Pick the rival that is the *strongest* competitor for this system — the one a domain scientist would actually reach for — and state its ranking procedure exactly. The rival gets a fair run on the same data; you are not building it to lose.

### B.5 The gate — stiff, per Ben's instruction
The pass/fail line, stated as a specific predicate over the frozen answer key, capable of both outcomes. The stiff form (Ben's choice):

> **AOP passes iff its coalition read recovers a specific distinction the rival provably misses, on a pre-named mechanism set, AND does not itself misclassify the answer-key structure.**

Concretely, name in advance:
- the **specific answer-key entries** the gate is scored on (the redundant set and the synergistic set are the natural targets — they are where a coalition read should win and a strength read should fail);
- the **rival's predicted failure** — state now, from the rival's definition alone, where it will mis-rank (e.g. a strength read ranks a high-coupling spectator above a low-coupling essential node);
- the **quantitative bar**: e.g. AOP's coalition classification matches the answer key on the scored set at a stated agreement level (rank correlation, exact-match on the redundant/synergistic labels, or a confusion-matrix criterion — pick one and fix it), *and* the rival falls below a stated bar on the same set.
- **Both failure modes are recorded:** AOP fails the gate if it misses the distinction (no better than rival) OR if it misclassifies the structure (calls essential inert, or inert essential). State both.

A gate that AOP's own architecture guarantees it passes is forbidden. Before freezing, apply this test to the gate itself: *can I, from the system's structure alone, prove AOP must pass?* If yes, the gate is circular — stiffen it until the answer is no. Document that check in the pre-registration.

### B.6 Robustness declaration
State now which declaration choices (partition, grain, V-member, normalization) will be varied as robustness checks, and the range. A verdict that holds only at one hand-picked declaration is not a verdict. Frozen here so robustness cannot be cherry-picked after the fact.

---

## 4. Phase C — Blind computation

Only now does real data meet either method. Compute:
- the AOP panels and coalition object per B.2/B.3,
- the rival's ranking per B.4,
- across the robustness range per B.6.

Deposit all code and outputs. Change nothing in the pre-registration. If something in the pre-registration proves unexecutable, **stop and report to Prime** — do not improvise a fix that alters the frozen commitments.

---

## 5. Phase D — Adjudication

Apply the frozen B.5 gate to the Phase C outputs. Record:
- the verdict (PASS / FAIL), with the failure mode named if FAIL,
- the AOP-vs-answer-key agreement on the scored set,
- the rival-vs-answer-key agreement on the same set,
- robustness: does the verdict hold across the B.6 range,
- an honest statement of any answer-key entry that turned out more contested than Phase A judged.

**Do not soften a FAIL into a "partial pass."** The gate is binary by construction. If it fails, it fails, and that is the recorded scientific result.

---

## 6. Phase E — Handback

Package for the two independent seats:
- **For Prime:** everything needed to re-run the verdict from scratch — pre-registration hash, code, data provenance, and the frozen gate — so verification is a re-run, not a re-read. Nobody grades their own homework; this benchmark is the reason that rule exists.
- **For Aster:** the result framed for attack — here is the system, the answer key, the gate, the verdict; break it. Aster runs before anything folds to canon.

Nothing from this task enters the canon until Prime's re-run and Aster's attack are both complete and Ben decides.

---

## 7. Seats and rules (unchanged, restated because this is the task they were built for)

- **CW builds and pre-registers.** You do Phases A–E. You do not verify your own verdict.
- **Prime verifies by re-running** against the frozen gate.
- **Aster attacks** the result before canon.
- **Ben decides** the system (end of Phase A) and the final disposition (after E).
- **Bind-before-freeze is absolute.** The §11b failure at v1.18 — a self-graded gate that passed a result forced by construction — is the exact failure this structure prevents. It was caught because a different seat verified. This time the structure prevents it from being built in the first place.

---

## 8. What to deliver

1. `AOP_Benchmark_PhaseA_SystemSelection_v0.1.md` — candidates, sources, recommendation. **Stops for Ben's pick.**
2. `AOP_Benchmark_PhaseA_AnswerKey_v0.1.md` — frozen answer key with primary-source quotes, after Ben picks. **For Prime's line-check before B.**
3. `AOP_Benchmark_PhaseB_Preregistration_v0.1.md` — full tuple, panels, coalition mapping, rival, gate, robustness. **Hashed and frozen.**
4. `AOP_Benchmark_PhaseC_Computation_v0.1.md` + deposited code/outputs.
5. `AOP_Benchmark_PhaseD_Verdict_v0.1.md` — the binary verdict, both agreements, robustness.
6. `AOP_Benchmark_PhaseE_Handback_v0.1.md` — packaged for Prime and Aster.

Deliver via Drive to the Canon Development subfolder (`1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`); if Drive write fails, local build + present_files and Ben places manually.

**Two hard stops built into this order:** (1) after Phase A, for Ben to pick the system; (2) anywhere the pre-registration proves ill-posed, for report to Prime rather than silent amendment. Hit either and stop.

**Do not self-certify. Do not tune to a pass. A verdict that could only have come out one way is a failed deliverable regardless of which way it came out.**

---

**End of tasking order.**
