# Pre-registration — Q1: Is maintenance measurable on all four axes?

**Document ID:** `AOP_PreReg_Q1_MaintenanceMeasurability_20260804.md`
**Date:** 4 August 2026
**Origin seat:** prime (chat seat)
**Status:** PROPOSAL — pre-registration. Not canon. No canon edit is authorised by this document.
**Anti-gaming stamp:** this document is deposited and hashed **before any system is examined**. Any deviation from the protocol below is permitted but must be declared in the execution report, with the deviation stated before its result.

---

## 0. Conflict-of-interest declaration

The hypothesis under test was proposed by prime in conversation with Ben on 4 August 2026. **Prime therefore does not execute, does not score, and does not adjudicate this question.** Prime's role ends at this document. Nobody grades their own homework.

---

## 1. What is being tested

AOP's four axes each return a *value* — how much Boundary, Drive, Memory, Integration a system has. The canon currently carries, for exactly one axis, a second quantity: **the cost of holding that value.** Boundary's maintenance burden is B4 (the housekeeping dissipation required to hold the interior/exterior contrast against leak, grounded in Hatano & Sasa 2001 and Speck & Seifert 2005).

Memory and Integration have no equivalent. Drive's status is ambiguous because Drive may *be* the supply rather than a coordinate with a supply.

**This asymmetry has not previously been named.** It is either an accident of how the framework was built, in which case it can be repaired, or it reflects something real about the axes, in which case that is a finding about their structure.

**The hypothesis (H1):** for each of the four axes there exists a statable perturbation-and-recovery protocol distinguishing a coordinate that is *actively maintained* from one that is *passively held*, and for a single well-characterised organism each such protocol is instantiated in the primary experimental literature.

**H1 is stated so that it can fail.** Section 5 gives the conditions under which it does.

---

## 2. Scope — what this does NOT test

This question is deliberately narrow. It does **not** test:

- whether maintenance distinguishes living from non-living systems;
- whether maintenance carries information beyond the existing four-vector;
- whether maintenance predicts persistence, lifetime, or viability;
- anything about the semantic mask, the declaration tuple, or boundary choice.

Those are downstream and depend on this. **If H1 fails, none of them are worth asking.** Q1 is a measurability gate, not a science claim.

Nothing here bears on the open decision between arc option (a) and option (b). This is not a substitute for that ruling.

---

## 3. Test article and negative control

**Test article:** *Escherichia coli* K-12, exponential growth phase, standard laboratory conditions. Chosen because it is the most experimentally characterised free-living organism available, which maximises the chance that protocols exist in the literature. If a protocol cannot be found for *E. coli*, it is unlikely to exist anywhere.

**Mandatory negative control:** the same four perturbations, applied to a system where no maintenance is expected. Two candidates, and the executing seat selects and justifies one:

- heat-killed *E. coli* of the same strain and preparation, or
- a protein-free lipid vesicle of comparable size in the same buffer.

**The control is not optional and is not decorative.** If the negative control scores MAINTAINED on any axis, the protocol for that axis is measuring something other than maintenance, and that axis returns UNDETERMINED regardless of what the test article did.

---

## 4. Protocol

For each of the four axes, the executing seat must supply five items. A protocol is complete only when all five are present.

1. **The coordinate.** What is being held, stated in AOP's own terms and referenced to the canon section that defines the axis.
2. **The perturbation.** A specific, physically realisable intervention that moves the coordinate away from its held value **without killing the system**. Named agent, named magnitude where the literature gives one.
3. **The predicted recovery.** What the coordinate does after the perturbation is removed, including a timescale. A prediction with no timescale is not a prediction.
4. **The primary source.** A peer-reviewed experimental paper reporting the actual recovery. **Reviews do not satisfy this requirement.** The passage relied upon must be read and quoted in the ledger, not inferred from title or abstract — abstract-only sourcing is a charter defect and has already produced retractions in this project.
5. **The negative-control result.** What the same perturbation does to the control.

### 4.1 Axis-specific notes

**Boundary.** A protocol is expected to exist and the canon already points at the quantity (B4). The executing seat should treat this axis as the calibration case: if the procedure cannot produce a clean result on Boundary, the procedure itself is at fault, not the axis.

**Drive.** Flagged as structurally awkward before execution. If Drive is the free-energy supply from which the other three draw, then perturbing Drive perturbs everything, and Drive may not be independently perturbable. **This is an anticipated finding, not a failure.** The executing seat should report which it is, and should not force an independent protocol into existence to make the set of four look tidy.

**Memory.** A protocol is expected to exist. The executing seat should be explicit about *which* stored quantity is the coordinate, since the canon separates excess entropy (E), statistical complexity (Cμ), and stored physical organisation, and these are not interchangeable.

**Integration.** **Prime cannot name a perturbation for this axis.** This is stated deliberately and is the substantive content of the question. Prime declines to supply a candidate, because supplying an undefended one is the exact defect that damaged the two-axis work order (an unjustified threshold introduced to make a required structure exist). The executing seat may propose one, must defend it, and must report failure plainly if none can be defended.

Two constraints on any Integration proposal: the perturbation must act on the *relations between parts* rather than on the parts themselves, and it must not silently redefine the declared system boundary (e.g. moving from a single cell to a population).

---

## 5. Kill conditions — frozen

These are binding and are stated before execution.

**K1.** If no perturbation-and-recovery protocol for **Integration** can be stated and defended for *E. coli*, with a primary source, then H1 is false and the maintained/passive scheme is not measurable on all four axes. **H1 dies.**

**K2.** If **two or more** axes return UNDETERMINED, H1 dies regardless of which two.

**K3.** If the **negative control** scores MAINTAINED on any axis, the protocol for that axis is invalid and that axis returns UNDETERMINED, feeding K2.

**K4.** If **Drive** proves not independently perturbable, H1 is **not** killed, but the scheme is restricted: maintenance becomes an attribute of three axes drawing on a fourth, and this must be reported as a structural finding about the axes rather than folded silently into the result. Note that this outcome is adjacent to the budget framing already falsified by a pre-registered gate (entropy production ranging 157% of its mean at fixed persistence); **the executing seat must check its result against that gate before concluding anything about source-and-sink structure.**

**Sole survival condition:** H1 survives only if Boundary, Memory and Integration each return a complete five-item protocol with a primary source, and the negative control returns PASSIVE or UNDETERMINED on all four.

---

## 6. Scoring rule

Three values only. No fourth category may be introduced during execution.

- **MAINTAINED** — all five protocol items present; coordinate recovers after perturbation; primary source read and quoted.
- **PASSIVE** — perturbation is statable and was applied; no recovery occurs and none is expected; the coordinate is held by structure rather than by process.
- **UNDETERMINED** — no defensible perturbation can be named, or no primary source reports the recovery, or the negative control invalidates the protocol.

**UNDETERMINED is a legitimate and expected outcome and must not be avoided.** A forced MAINTAINED verdict with a weak source is worth less than an honest UNDETERMINED.

---

## 7. Execution order

Fixed, to prevent the result being fitted to an expectation:

1. Negative control, all four axes.
2. Integration.
3. Memory.
4. Drive.
5. Boundary.

**Integration is scored second, immediately after the control, and before any axis expected to succeed.** Scoring the easy axes first establishes a pattern that the hard one gets fitted to. Boundary is scored last precisely because its answer is already half-known.

---

## 8. Seats

- **Prime** — designed this question. Does not execute, score, or adjudicate. May clarify intent if asked, and must record any clarification in the execution report.
- **Executing seat — Claude Science (CS), assigned by Ben, 4 August 2026** — retrieves, reads primaries, produces the four protocols and the control, deposits an execution report with a retrieval ledger. Output is a **proposal**, not a verdict.
- **Verifying seat — Claude Cowork (CW)** — re-runs the citation check independently, by opening the sources, not by reading the report. Confirms each quoted passage exists and says what the report claims.
- **OAI** — receives this document **before results exist** and is asked to break the *design*: are the kill conditions gameable, is the negative control adequate, is the Integration refusal in §4.1 a genuine open question or a rhetorical hedge.
- **Ben** — rules on whether H1 survived, and on whether anything proceeds.

---

## 9. Provenance of the idea, stated for the record

The maintained-versus-passive framing arose in conversation on 4 August 2026 and is **prime's, unverified, FRONTIER**. Several adjacent ideas surfaced in the same conversation and are **deliberately excluded** from this pre-registration because they are unverified and would contaminate a measurability gate with a science claim:

- accretion-versus-repair as a flame/crystal discriminator;
- constraint count as a flame/cell discriminator;
- the naked-axis corners;
- memory-as-distributed-arrangement (positional information), which is additionally flagged as sitting in the literature where this project has already taken abstract-only retractions;
- assembly theory, which is diachronic and reaches AOP only through the Ladder bridge memo.

One further observation is recorded here because it bears on how the result should be weighed: **seven distinct routes in that conversation converged on self-production.** If those seven are the same argument in different vocabulary, the convergence is one piece of evidence rather than seven. That question is posed separately to OAI and is not part of Q1.

---

## 10. Deposit

This document is hashed at deposit. The hash is recorded in the execution report and re-verified by the verifying seat before any result is accepted.

**Scope ruling in force (Ben, 4 August 2026):** Ladder-side material may be consulted where the purpose is fixing the identity of the four axes. This grant covers inputs only; Ladder work still produces no AOP canon edit, and any canon-facing consequence routes through the versioned bridge memo.

---

*End of `AOP_PreReg_Q1_MaintenanceMeasurability_20260804.md`.*
