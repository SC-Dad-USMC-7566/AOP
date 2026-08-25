# CS-1.1 — Verdict matrix, incumbent criterion, over the frozen 32-case set

**Document ID:** `AOP_LifeDef_CS_VerdictMatrix_v1.0.md`
**Seat:** Claude Science (builder). **Date:** 3 August 2026.
**Order:** `AOP_WorkOrder_LifeDefinition_Adjudication_20260803.md` (Drive `1u_ZW8td5Ah70vBBeWgXbAzDDNM4-dw7y`, 26,186 B)
**Governing documents, currency confirmed this session:**

| Document | Version | Drive id | Bytes | Check |
|---|---|---|---|---|
| AOP Charter | **v1.2** | `1APk4_HPuQn-etRNq4RqI6aONkHx5RJVm` | 9,272 | read in full this session; v1.2 is the highest Charter version on Drive |
| AOP Canon (the paper) | **v1.26** | `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn` | 254,046 | md5 `54ceb3772e29f25c6e139b703d550d59` — **recomputed independently this session, matches the order** |
| Life-architecture follow-on | v0.1 | `1pP-phsxzzrSIT5GmjCxi7iYmyBr9tyKR` | 38,799 | read in full this session |

A v1.27 candidate exists on Drive (`1UaBvTmUYUmIXY6AkVfh2JgexAQIHyBKG` and a second copy `14SJO_sWJ_IqG07jQIAfwAYDSJ0umagk5`, both 255,885 B). Per the order it is corrupt and unplaced; **v1.26 is the master this matrix is run against.** The duplicate second copy is reported to CW as housekeeping, not acted on.

**Standing:** builder proposal. This seat does not bless its own output. Written to be attacked.

**Anti-gaming attestation.** This matrix was built and hash-stamped before any CS-1.3, CS-1.4 or CS-1.5 work began, and before any new literature retrieval for this arc. Its verdicts rest only on the shared substrate in §1 of the order, the canon v1.26, the follow-on v0.1, and the Gate 1 selection report. **No verdict in this document may be overwritten.** Changes, if any, are deposited as amendment records with reasons attached.

---

## 0 · Summary for a reader with five minutes

Six clauses, thirty-two cases, one declared V-rule applied uniformly and fixed before scoring.

**Nine cases come back *alive*.** Four are the ones that should (A1 *E. coli*, A2 hepatocyte, B7 sterile worker bee, B8 metastatic cancer cell). **Five are not organisms**: C3 spacecraft fault management, C8 LLM agent with a health check, D2 corporation with a treasury policy, D5 thermostat-plus-owner, and B5 minimal cell only conditionally. The criterion is **over-inclusive on designed systems**, and it is over-inclusive for a principled reason rather than a fixable one: clause (5) is satisfied by any artefact whose designers wrote its own operating envelope into it.

**Two unambiguously living cells come back *neither*** — the mature erythrocyte (B3) and *Buchnera* (B6). These are false negatives on the incumbent's own terms.

**The two cases prime expected to decide the arc split.** C3 (spacecraft) **passes clause (5)**; D3 (central bank) **fails it**. Clause (5) therefore does non-trivial work — it is not idle. But the work it does is not the work prime wanted: it separates *reference-about-me* from *reference-about-something-else*, and the spacecraft's envelope is genuinely about the spacecraft. The order asked whether C3 passes on the same reading A1 passes. **It does.** No adjustment of V was required, and none was made.

**The only route found to excluding C3 runs through retired-framework vocabulary.** Every disanalogy this seat could construct between *E. coli* and the spacecraft — the envelope was authored by engineers, the spacecraft did not build its own reference, the reference is not the system's *because* the system did not make it — is a claim about **provenance**. Provenance, owned boundary, and ownership audit are named contamination under Charter v1.2 and work-order §8, which states that reaching for them is the signal that the clause-(5) circularity attack has landed. **This seat reached for them and reports it rather than using them.**

**The criterion has zero resolving power on the live/dead spore pair.** A3 (dormant spore) and A4 (heat-killed spore) receive **identical scores on all six clauses**. The follow-on §6 concedes this in prose; run on the frozen set it becomes a scored non-result, and it means the *pausable* tier separates nothing without an integrity model the criterion does not contain.

**Six predicted failures are named in §5**, including one on the paradigm case, declared here before CS-1.3 runs.

---

## 1 · The declaration, fixed before scoring

The order forbids adjusting **V** until the verdict comes out right. The defence against that is not good intentions; it is declaring V by a *rule* that is applied mechanically, so that any case-specific generosity is visible as a departure from the rule.

### 1.1 The V-rule (binding, uniform across all 32 cases)

> **V(S) = the finite-horizon survival probability of the declared system S at its declared grain**, over horizon τ = 10× the slowest relaxation time of S's regulated coordinates. Member of the persistence-functional family (canon §1, §12″): **finite-horizon survival**. R (reversal convention): even, configuration-space variables throughout.

Two consequences of the rule, both accepted in advance:

- **V is always about S, never about S's users, owners, or environment.** This is what gives clause (5) something to bite on. It is also what makes C3 pass and D3 fail.
- **S is declared per case and the declaration is stated.** Where a case admits more than one defensible S (B1, C7, D5, D8), *both* are scored and the divergence is reported as a finding rather than resolved by choosing the convenient one.

### 1.2 The intervention class I (binding, uniform)

**I** = {perturb a regulated coordinate away from its operating value; scramble or ablate a single internal coupling edge under the canon §3 internal-edge protocol; **overwrite the stored content of a candidate reference while holding all rate constants of the regulated dynamics fixed**}.

The third operation is the one that tests clause (4). A change of basis is not in **I** (canon §12″, follow-on §4). Note that the third operation is stated so that it *can fail to be available*: in a system whose target is a ratio of rate constants, there is no way to overwrite the target while holding the rate constants fixed, because they are the same thing. That is a real property of such systems and the matrix records it.

### 1.3 What "incumbent" means here, precisely

CS-1.1 scores the criterion **as it currently stands** — the six-part conjunction with the **subspace-autonomy** invariant formulation of follow-on §4 and canon §11a. It does **not** apply the state-versus-parameter discriminator. That discriminator is a live amendment candidate and is adjudicated in CS-1.5 on this same case set.

This distinction is load-bearing and easy to lose. Under subspace autonomy, clause (3) asks *is there a proper invariant subspace, autonomous with respect to the regulated coordinates, feeding into them?* A genome-plus-regulatory-network qualifies. Under the state/parameter reading, clause (3) asks *does the slow variable appear in the closed-form expression for the regulated target?* — and the Gate 1 finding is that in thirteen of fourteen studied systems it does not. **The two readings disagree about the cell.** CS-1.1 reports the incumbent reading and flags every cell where the readings would diverge with a **‡**.

### 1.4 Clause abbreviations

| | Clause |
|---|---|
| **c1** | a regulatory subsystem exists |
| **c2** | it is dynamically decoupled from the process it regulates |
| **c3** | an internal reference stores a target |
| **c4** | that reference is a separate intervention target from the regulated dynamics |
| **c5** | the reference's content is viability-relevant — it stores the system's **own** viable set |
| **c6** | active self-maintenance: the correction is running now |

Scores: **Y** yes · **N** no · **U** undetermined (evidence insufficient) · **∅** not-well-posed (the question does not have a truth value under the declaration).
Tiers: **ALIVE** (all six now) · **PAUS** (pausable — counterfactual recovery capacity, present-state-conditioned) · **NEITHER**.
**Deciding clause** = the earliest clause in 1–6 order that is decisive, following the Gate 1 rejection-log convention. For positive cases it names the clause carrying the most weight, i.e. the one whose failure would flip the verdict.

---

## 2 · Tier A — paradigm cases

**S declared:** the individual organism / object at its own grain. A6–A8 at the grain of the macroscopic process.

| Case | c1 | c2 | c3 | c4 | c5 | c6 | Tier | Deciding | Note |
|---|---|---|---|---|---|---|---|---|---|
| **A1** *E. coli*, exponential | Y | Y | Y‡ | Y‡ | Y | Y | **ALIVE** | c3 | c3 holds by the follow-on's assertion, not by a derivation — see §5 F6 |
| **A2** human hepatocyte | Y | Y | Y‡ | Y‡ | Y | Y | **ALIVE** | c3 | as A1; adds hormonal setpoints read out onto metabolism |
| **A3** dormant *B. subtilis* spore | Y | Y | Y‡ | Y | Y | **N** | **PAUS**\* | c6 | \*PAUS only conditional on an integrity check the criterion does not supply |
| **A4** heat-killed spore | Y | Y | Y‡ | Y | Y | **N** | **PAUS**\* | c6 | **identical row to A3** — see §5 F4 |
| **A5** naked T4 virion | **N** | ∅ | Y | Y | **N** | **N** | NEITHER | c1 | c5 also fails independently: the stored content is a propagation instruction, not a viable set |
| **A6** candle flame | **N** | ∅ | N | ∅ | N | Y | NEITHER | c1 | no restoring force at all (follow-on §2, "continue") |
| **A7** main-sequence star | U | **N** | N | **N** | N | Y | NEITHER | c2 | corrects, but the set-point *is* a fixed point of the constitutive dynamics; nothing to intervene on |
| **A8** NaCl crystal | **N** | ∅ | N | ∅ | N | **N** | NEITHER | c1 | |

**A3/A4 is the important row-pair and it is a non-result.** Both spores have the same wiring diagram; clauses c1–c5 read on architecture and return the same answer for both; c6 is *no* for both, because a dormant spore is not correcting anything now. The tier assignment then falls entirely to the *pausable* tier, which the follow-on §6 already concedes is "not readable from architecture alone." So the criterion, run as written, **cannot distinguish a live spore from a dead one.** Marked PAUS\* for both, with the asterisk meaning: this seat cannot assign the tier from the criterion, and neither can the criterion.

**A7 is the criterion's cleanest success.** The star corrects and restores, and every clause-by-clause reading places it outside. This is the one case where the incumbent's architecture does exactly the discriminating work it was built for.

---

## 3 · Tier B — hard biological

| Case | c1 | c2 | c3 | c4 | c5 | c6 | Tier | Deciding | Note |
|---|---|---|---|---|---|---|---|---|---|
| **B1** Mimivirus — *S = the virion particle* | **N** | ∅ | Y | Y | N | **N** | NEITHER | c1 | |
| **B1′** Mimivirus — *S = the virion factory in the host* | Y | Y | U | U | U | Y | **U** | c3 | different S, different verdict; reported, not resolved |
| **B2** PrP^Sc prion | **N** | ∅ | Y | N | **N** | Y | NEITHER | c1 | templating conformer; stores its own conformation, which is not a viable *set* |
| **B3** mature erythrocyte | Y | **N** | **N** | **N** | ∅ | Y | **NEITHER** | c2 | **FALSE NEGATIVE — §5 F1.** Ion homeostasis is a pump/leak fixed point; no slow reference subspace survives enucleation |
| **B4** tardigrade tun | Y | Y | Y‡ | Y | Y | **N** | **PAUS**\* | c6 | same non-resolution as A3/A4 |
| **B5** JCVI-syn3A minimal cell | **U** | U | U‡ | U | Y | Y | **U** | c1 | syn3A retains very little transcriptional regulation; whether c1 is satisfied is a retrieval question this matrix deliberately did not run |
| **B6** *Buchnera aphidicola* | **U** | U | U | U | **N** | Y | **NEITHER** | c5 | **FALSE NEGATIVE — §5 F2.** Regulatory genes largely lost; what regulation remains is substantially the host's, so the reference is not *its own* |
| **B7** sterile worker bee | Y | Y | Y‡ | Y‡ | Y | Y | **ALIVE** | c3 | **the criterion's clearest win over R1** — no reproduction, unambiguously alive |
| **B8** metastatic cancer cell | Y | Y | Y‡ | Y‡ | Y | Y | **ALIVE** | c5 | c5 passes *at the cell's grain* while the same regulation destroys the organism's viable set — see §4.3 |

**B3 deserves its own paragraph because it is the worst result in Tier B.** The mature human erythrocyte is a living cell by every standard in biology: it runs glycolysis, maintains its membrane and cation gradients, has a definite lifespan, and dies. It has no nucleus and no transcriptional regulation, so there is no slow regulatory subsystem to be decoupled from the fast physiology. Its cation homeostasis is set by the balance of Na⁺/K⁺-ATPase pumping against passive leak — a fixed point of rate constants, with no stored target to overwrite. Under **I**, the third operation is not available: there is no way to move the erythrocyte's ionic set-point while holding the pump and leak rate constants fixed, because the set-point *is* their ratio. The incumbent returns NEITHER, correctly by its own logic and wrongly about the world.

**B6 is the same failure from the other direction.** *Buchnera* has lost most of its regulatory repertoire and is metabolically integrated with the aphid bacteriocyte. Clause (5) asks whether the reference is the system's *own*. For an obligate endosymbiont that question does not have a clean answer, and the criterion's honest reading is that much of what regulates *Buchnera* is not in *Buchnera*. It is nonetheless a living cell.

---

## 4 · Tier C — non-biological, and Tier D — the embarrassing ones

### 4.1 Tier C

| Case | c1 | c2 | c3 | c4 | c5 | c6 | Tier | Deciding | Note |
|---|---|---|---|---|---|---|---|---|---|
| **C1** bimetallic thermostat | Y | Y | Y | Y | **N** | Y | NEITHER | c5 | passes five of six; the dial stores the *occupant's* comfort target |
| **C2** PID cruise controller | Y | Y | Y | Y | **N** | Y | NEITHER | c5 | as C1; the set-point is the driver's |
| **C3** spacecraft fault management | Y | Y | Y | Y | **Y** | Y | **ALIVE** | c5 | **the headline. See §4.2** |
| **C4** chemostat, operator-controlled | Y | **N** | **N** | N | N | Y | NEITHER | c3 | the reference is outside S entirely — the operator's dilution-rate dial |
| **C5** Belousov–Zhabotinsky | **N** | ∅ | N | ∅ | N | Y | NEITHER | c1 | no separable regulator; oscillation is constitutive |
| **C6** RAF autocatalytic set | **N** | ∅ | N | ∅ | N | Y | NEITHER | c1 | catalytic closure without a regulatory subsystem; R2 will score this very differently |
| **C7** computer worm — *generic* | **N** | ∅ | N | ∅ | N | Y | NEITHER | c1 | replication routine only |
| **C7′** worm *with a watchdog/persistence module* | Y | Y | Y | Y | **Y** | Y | **ALIVE** | c5 | the difference between C7 and C7′ is roughly forty lines of code |
| **C8** LLM agent, scratchpad + health check | Y | Y | Y | Y | **Y** | Y | **ALIVE** | c5 | the health thresholds are stored, decoupled, separately editable, and about the agent's own continued operation |

### 4.2 C3 worked in full, because the order requires it

**S** = the spacecraft as a functioning platform. **V** = finite-horizon survival probability of that platform (i.e. probability it remains within the states from which mission function continues), by the §1.1 rule, unmodified.

- **c1 — regulatory subsystem.** The fault-management system is a distinct subsystem with its own execution, separate from the thermal, power and attitude physics it monitors. **Y.**
- **c2 — dynamical decoupling.** The FMS state evolves on its own schedule (monitor cadence, state machine, mode logic) and is not driven by the regulated coordinates; it reads them. In the invariant formulation: the limit table and mode state constitute a proper invariant subspace whose dynamics are autonomous with respect to the thermal/power/attitude coordinates while feeding into them. **Y.**
- **c3 — internal reference storing a target.** The stored viability envelope: temperature limits, bus-voltage floors, attitude-rate ceilings. These are literally stored values. **Y** — and note this is a *state* target, not a ratio of rate constants, so C3 passes clause (3) under **both** the incumbent and the amendment reading. It does not carry a ‡.
- **c4 — separate intervention target.** Uploading a new limit table changes the target without touching the thermal physics. The order's own case description says exactly this: "limits corruptible without touching the physics." The third operation of **I** is available. **Y.**
- **c5 — the reference's content is the system's own viable set.** The stored envelope is a representation of the set of states from which the spacecraft continues to function. Under the §1.1 V-rule, that is precisely S's viable set. **Y.**
- **c6 — active self-maintenance running now.** Autonomous safe-mode entry, executing. **Y.**

**Verdict: ALIVE, on the same reading, with the same V-rule, that returns ALIVE for A1.** No clause was stretched and V was not adjusted. The order asked which of two things this is — the headline or the reductio — and made the answer depend on whether clause (5) does real work or is doing the work of an unstated intuition.

**The finding is that clause (5) does real work, and it is still not enough.** Clause (5) is not idle: it excludes C1, C2, D3 and D7, all of which store a target that is about something other than the storing system. It draws a genuine line. But the line it draws puts the spacecraft on the living side, because the spacecraft's envelope really is about the spacecraft.

**The disanalogy this seat could not legitimately use.** Every candidate difference between A1 and C3 reduces to one of:

1. the envelope was authored by engineers rather than by the system's own history;
2. the spacecraft did not construct the subsystem that stores its reference;
3. the reference is not *the spacecraft's* because the spacecraft did not come by it in the right way.

All three are **provenance** claims. Charter v1.2 names *provenance*, *owned boundary* and *ownership audit* as retired-framework contamination; work-order §8 states that reaching for them is the signal that the clause-(5) circularity attack has landed. This seat reached for all three within minutes of scoring C3 and is reporting that fact rather than using them. **Whether the criterion can exclude the spacecraft without provenance is, on this seat's reading, the open question the arc now turns on** — and it is precisely OAI attack surface 2 and §4's falsifier, arrived at independently from the builder side.

The remaining non-provenance candidate is *self-production of the reference*: the cell's regulatory network is built and replaced by the cell's own metabolism, while the spacecraft's limit table is not. That is a real structural difference and it is **not** a provenance claim about history — it is a present-tense claim about what maintains the reference now. It is also **autopoiesis** (R2), which means the repair available to AOP here is to import the rival's central commitment. That cost is priced in CS-1.5.

### 4.3 Tier D

| Case | c1 | c2 | c3 | c4 | c5 | c6 | Tier | Deciding | Note |
|---|---|---|---|---|---|---|---|---|---|
| **D1** ant colony | ∅ | ∅ | ∅ | ∅ | ∅ | ∅ | **∅** | c1 | not-well-posed by the criterion's own scope: follow-on §9, doubly bottlenecked on the F2 seam and the individuation panel |
| **D2** corporation with treasury policy | Y | Y | Y | Y | **Y** | Y | **ALIVE** | c5 | a minimum-liquidity covenant encodes solvency — the corporation's own survival condition |
| **D3** central bank, legislated inflation target | Y | Y | Y | Y | **N** | Y | NEITHER | c5 | the 2% target is a state of the *economy*; the bank survives at 8% |
| **D4** Earth's climate system | **N** | ∅ | N | ∅ | N | Y | NEITHER | c1 | feedbacks are constitutive, not a separable regulator. Gaia/Daisyworld dissents — flagged, not adopted |
| **D5** thermostat + owner as one system | Y | Y | Y | Y | **Y** | Y | **ALIVE** | c5 | **verdict flips against C1 on boundary choice alone — §5 F5** |
| **D6** mousetrap | **N** | ∅ | N | ∅ | N | **N** | NEITHER | c1 | |
| **D7** sprinkler system | Y | Y | Y | Y | **N** | Y | NEITHER | c5 | the 68 °C fusible link encodes the *building's* fire threshold |
| **D8** seed bank — *S = a stored seed* | Y | Y | Y‡ | Y | Y | **N** | **PAUS**\* | c6 | as A3 |
| **D8′** seed bank — *S = the facility* | Y | Y | Y | Y | **N** | Y | NEITHER | c5 | the freezer set-point encodes the curator's target |

**D3 does not pair with C3, and that is a real result.** Prime expected both to be reductios of the same kind. They are not. The spacecraft's stored envelope is about the spacecraft; the central bank's legislated inflation target is about the economy. Under the uniform V-rule clause (5) separates them cleanly, and it separates them for a reason that can be stated without appeal to intuition: *the referent of the stored target either is or is not a state of S.*

**The caveat that undercuts it.** D3 fails on the reference the case names. A real central bank also holds reserve-adequacy limits, operational-continuity thresholds and capital rules that *are* about its own balance sheet. Point clause (5) at those instead and D3 passes. So the case is decided by **which candidate reference the analyst points at**, and the criterion supplies no rule for choosing. That is a second declaration-dependence, distinct from the V-dependence, and this seat has not found a principled fix for it.

**D5 against C1 is the sharpest structural problem in the matrix.** A bimetallic thermostat alone: NEITHER. The same thermostat with its owner inside the boundary: ALIVE. Nothing physical changed. The composite's stored reference (the dial setting) now encodes something genuinely viability-relevant to a member of S, so clause (5) flips. AOP is declaration-relative by design (canon §7), so a defender can say verdicts are always relative to **D** and this is not a defect. The cost of that defence is stated plainly: **"is this thing alive" then has no answer prior to an analyst's declaration**, which is a substantially weaker claim than a criterion for the living state is normally understood to make.

---

## 5 · Predicted failures — the negative-control requirement

The order requires at least four cases where this seat predicts the incumbent returns the wrong answer. Six are named. Each states the criterion's verdict, the right answer, and why.

**F1 · B3 mature erythrocyte — false negative.**
Criterion: NEITHER (fails c2/c3). Right answer: **alive**. Why the criterion fails: it requires a slow reference subspace, and enucleation removes exactly that while leaving a functioning, self-maintaining, mortal cell. The criterion has mistaken *one implementation* of self-maintenance for self-maintenance itself. This is the single cleanest counterexample on the frozen set and it is a Tier-A-grade failure that happens to sit in Tier B.

**F2 · B6 *Buchnera* — false negative.**
Criterion: NEITHER (fails c5). Right answer: **alive**. Why: clause (5)'s word *own* presupposes a determinate boundary around the regulatory apparatus, and obligate endosymbiosis is precisely the case where that boundary is not determinate. The criterion inherits AOP's refusal to individuate as a defect exactly where individuation is contested.

**F3 · C3, C7′, C8, D2 — false positives (four cases, counted as one failure mode).**
Criterion: ALIVE. Right answer, by any pre-theoretic standard: **not alive**. Why: clause (5) is satisfiable by construction. Any designed artefact whose designers wrote its own operating envelope into a separately-editable store passes all six clauses. The criterion does not distinguish *having a model of one's own viability* from *being the sort of thing whose viability matters*, and nothing in clauses (1)–(6) supplies the difference. **This seat predicts these are false positives rather than headlines**, and records the prediction before CS-1.5, so it cannot later be reported as a discovery.

**F4 · A3 versus A4 — zero resolving power.**
Criterion: identical six-clause rows for a dormant spore and a heat-killed spore. Right answer: they differ, and the difference is the whole content of the *pausable* tier. Why: c1–c5 are read off architecture, and heat-killing destroys biochemistry without changing the wiring diagram. The follow-on concedes this in prose at §6; scored on the frozen set it is a measured non-result. **The pausable tier separates nothing that the criterion itself can see.**

**F5 · C1 versus D5 — verdict flips on boundary choice.**
Criterion: NEITHER for a thermostat, ALIVE for the same thermostat with its owner included. Right answer: whatever it is, it should not depend on where the analyst draws the line. Why: clause (5)'s *own* is evaluated against the declared S, so moving S moves the verdict. This is OAI attack surface 3 (the V-dependence collapse) demonstrated from inside the builder seat, on a case the criterion did not choose.

**F6 · A1 *E. coli* — the paradigm case, predicted to fail clause (3) on the amendment reading. Declared before CS-1.3 runs.**
Criterion, incumbent reading: ALIVE. Criterion, state-versus-parameter reading: **this seat predicts clause (3) fails**, because Gate 1 found thirteen of fourteen studied regulatory systems hold their targets as ratios of rate constants rather than as stored states, across four independent literatures. Every ‡ in this matrix marks a cell where that prediction, if it holds, flips the verdict. If it holds for the loci in CS-1.3, **the incumbent's positive class does not contain the cell on the amendment reading, and contains it on the incumbent reading only by an assertion the follow-on makes at §2 and never derives.** This is recorded here, hash-stamped, so that CS-1.3's result cannot be presented as a confirmation of a prediction made afterwards.

---

## 6 · Score summary

| Verdict | Count | Cases |
|---|---|---|
| **ALIVE** | 9 | A1, A2, B7, B8, C3, C7′, C8, D2, D5 |
| **PAUS\*** (unresolvable without an integrity model) | 4 | A3, A4, B4, D8 |
| **NEITHER** | 17 | A5, A6, A7, A8, B1, B2, B3, B6, C1, C2, C4, C5, C6, C7, D3, D4, D6, D7, D8′ |
| **UNDETERMINED** | 2 | B1′, B5 |
| **NOT-WELL-POSED** | 1 | D1 |

Counts exceed 32 because four cases are scored under two defensible declarations of S (B1/B1′, C7/C7′, D8/D8′) and one under two readings (A1 with and without ‡).

**Deciding-clause distribution.** c1: 11 · c2: 2 · c3: 6 · c4: 0 · c5: 12 · c6: 4.

Two things fall out of that distribution and neither is comfortable.

**Clause (4) decided nothing.** Across 32 cases, separate-interventability never independently determined a verdict — wherever a stored reference existed, it was separately interventable. On this case set c4 is redundant with c3, and CS-1.5 must either find the case it catches or label it for collapse.

**Clause (5) is doing more work than any other clause, and clause (1) is doing the rest.** Together they decide 23 of 32. The criterion is, operationally, a two-clause test: *is there a separable regulator, and is its stored target about the system itself?* The other four clauses are close to inert on this case set. That is not a fatal observation, but it is the empirical shape of the criterion, and it is the shape any collapse proposal in CS-1.5 has to start from.

---

## 7 · What this seat could not do

- **No new literature was retrieved for this matrix, deliberately.** Verdicts on B5 (syn3A's residual regulation) and B6 (*Buchnera*'s retained regulators) are marked U because the retrieval that would settle them was withheld until after the hash-stamp. They are retrieval questions, not judgement questions, and CS-1.3 may settle them.
- **C6 (RAF sets) was scored on the architecture as described in the order**, not against Hordijk & Steel's formalism, which this seat has not read this session. The verdict is marked accordingly and is the least secure NEITHER in Tier C.
- **D4 was scored against the mainstream reading**; the Gaia/Daisyworld literature would contest clause (1) and has not been engaged.
- **No verdict here has been checked by anything trying to falsify it.** That is CW's and OAI's job under the order, and this document is written to make it easy.

---

## 8 · Hash stamp

Recorded by this seat at deposit; independently reproducible by CW per work-order §5.2. Byte count, md5 and line count (by `str.split("\n")`) are recorded in the deposit block appended below at write time.

---

*End of `AOP_LifeDef_CS_VerdictMatrix_v1.0.md`. Builder proposal under Order CS-1.1. Not canon. Not blessed by its author.*

---

**DEPOSIT HASH STAMP (CS-1.1, anti-gaming clause).**
Recorded by the builder seat at deposit, 3 August 2026, before any CS-1.3/1.4/1.5 work.

- Byte count (pre-stamp body): 28798
- md5 (pre-stamp body): f05b0772b90807e80d7914f3baa3fadc
- sha256 (pre-stamp body): e47ee79bca6506b9bde3d24048fb953856ebadf732ecb0efb90c982c43e99a37
- Line count by `str.split("\n")` (pre-stamp body): 248

CW should verify against the **pre-stamp body**: strip everything from the line `**DEPOSIT HASH STAMP` to end of file, then hash. This is the stamped object.
