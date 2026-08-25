# OAI adversarial review — Gate 1 selection and Prime adjudication

**Document ID:** `REV_AOP_LifeCriterion_Gate1_OAI_Attack_v0_1_20260803.md`  
**Seat:** OAI / Aster (outside critic)  
**Date:** 3 August 2026  
**Standing:** Gate 1 may feed a draft pre-registration, but **the pre-registration should not freeze at decision #2 until the conditions in §3 are discharged**.

## Materials actually accessed

OAI read the following Drive files in full unless a narrower scope is stated:

- [`AOP_LifeCriterion_SystemSelection_Report_v1_0_20260803.md`](https://drive.google.com/file/d/1TMyzJW7TPYQ_uq8fHmysTdc4jXf9KKUJ) — full text.
- [`AOP_LifeCriterion_RejectionLog_v1_0_20260803.md`](https://drive.google.com/file/d/1G30cFWNA5VeAmbDkx0Lu69hi5RSewxIo) — full text.
- [`AOP_LifeCriterion_Gate1_PrimeAdjudication_v0_1_20260803.md`](https://drive.google.com/file/d/16Ev9APq8gKDClQwbwhRXv4dQUD-JgK-h) — full text; Drive and supplied-local sizes both verified at 10,896 bytes.
- [`AOP_LifeCriterion_DispositionRule_FROZEN_v1_0_20260801.md`](https://drive.google.com/file/d/1-HkXf58z-UWnYVkT1mcNR3_y2hIi3PAy) — full text.
- [`TASK_CS_AOP_LifeCriterion_SystemSelection_20260801.md`](https://drive.google.com/file/d/1pqmKxzablE53V4IXpW8inq-1EgT8rXfH) and the governing work order — full text.
- [`AOP_CANON_MASTER_v1.26.md`](https://drive.google.com/file/d/1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn) — §11a and directly relevant masthead/context passages.
- `AOP_LifeArchitecture_Followon_v0.1.md` — §§2–4 and §10, retrieved through Drive search hydration; its direct stored-file fetch currently returns 404.
- Sontag, *Adaptation and regulation with signal detection implies internal model* — theorem statement, assumptions, decomposition, chemotaxis example, and relevant proof passages in the [author's arXiv primary](https://arxiv.org/abs/q-bio/0309003).
- Jones et al., *Robust and tunable signal processing in mammalian cells via engineered covalent modification cycles* — relevant architecture, tuning, and robustness passages in the [open primary](https://www.nature.com/articles/s41467-022-29338-w).
- Gerken et al., *MzrA: a novel modulator of the EnvZ/OmpR two-component regulon* — relevant MzrA/EnvZ claims in the [open primary](https://pmc.ncbi.nlm.nih.gov/articles/PMC2727453/).

**Verification bound.** OAI did not read the five track-evidence files or re-run the builder's complete 51-primary retrieval. This is a targeted logical, governance, and design attack. The queued independent bibliography pass remains necessary.

---

## 1. Executive Summary

**Top-line judgment:** Prime correctly defeats the double-standard objection at report §3.3.1, correctly identifies the definitional collapse that replaces it, and correctly raises the clock-only positive class as a design-level threat. But Prime's proposed P1 repair does **not** escape the hole, and its Reading B ruling is stronger than the cited theorem or the filed evidence warrants. The Gate 1 output is therefore useful but not freeze-ready.

The highest-priority findings are:

1. **P1's proposed phenotype dissociation is not an architectural consequence.** A parameter-target system can shift its equilibrium while preserving gain and settling time; a state-target shift can change local dynamics in a nonlinear system. “Parameter shift drags dynamics; state shift does not” is an unproved genericity assumption, not an operational definition.
2. **The EnvZ-derived cycle remains a required arm, but the published paper does not already run Prime's proposed test.** It demonstrates tunability and, in a related closed-loop design, robustness to selected perturbations. It does not report a same-system target sweep with gain, settling time, precision, and disturbance rejection jointly tested for equivalence.
3. **Sontag does not force Reading B.** The theorem supplies an output/error-driven internal model under strong assumptions; on the output-zeroing manifold that subsystem generates the exosystem autonomously. It does not supply timescale separation, viability content, or Prime's full Reading B. It attacks the canon's *global-autonomy wording*, not the entire invariant-subspace idea.
4. **The state-versus-parameter filter is valuable but not canon-ready.** As filed, it is representation-dependent: a parameter can be promoted to a constant state, and a slow state can be reduced to a parameter. It needs a physical intervention/persistence test before it can replace the similarity-invariant §11a formulation.
5. **The report's headline denominator is not auditable.** Its score table supports six parameter-target cases, one state-target case, and one undetermined case. Several additional systems are explicitly “not reached.” The filed report therefore does not support “13 of 14” without a candidate-by-candidate appendix showing the missing determinations.
6. **The clock dissent is correct and should be sharpened.** KaiABC stores an internal model of external time. A declared viability functional removes ownership language; it does not by itself show that clock phase stores a viable set. The positive arm may be an architecture probe whose only positive class is clocks, not a validated paradigm instance of a life criterion.
7. **P2 may be split from the positive article scientifically, but doing so is an amendment to Gate 1.** The selection order says a positive candidate “must clear all four” screens and makes S.4 a disqualifier. KaiABC does not clear it. The frozen P2 disposition need not change, but the Gate 1 order must be amended openly.

**Recommended working design:** draft a provisional three-arm pre-registration — KaiABC for the state-memory/P1 arm, engineered EnvZ/OmpR for the excluded-system/P1 arm, and a physical antithetic controller for the P2 method arm — while withholding the decision #2 freeze until the corrections in §3 are deposited.

---

## 2. Critique

### 2.1 §3.3.1: Prime finds the right problem and gives it the wrong repair

Prime is right on the initial adjudication. There is no double standard in saying that a rate-constant target moves only when the machinery parameters that constitute it move. That is the S.2 exclusion restated, not defeated.

Prime is also right that this defense collapses P1 back into the definition: if the negative kill requires a target move with target-defining parameters fixed, the kill condition is functionally asking whether the excluded system secretly had a state target after all.

The proposed phenotype repair, however, does not solve that problem. Consider the parameter-target system

\[
\dot y=-k(y-\theta).
\]

The target \(\theta\) is a parameter. Changing \(\theta\) shifts the target while leaving the local settling time \(1/k\), small-signal gain, and adaptation precision unchanged. Conversely, in a nonlinear state-target controller, shifting the reference state can move the operating point into a region with a different Jacobian, gain, noise level, or saturation margin. Target locus alone does not determine phenotype invariance.

The filed claim — that parameter-setting constants set both target and dynamics, whereas a state target moves orthogonally to dynamics — is therefore neither generally true nor supplied by the cited literature. If inserted as the scoring rule, it creates a new genericity premise that can fail for reasons unrelated to the criterion.

**What survives:** “intact” and “precise” must be operationalized with performance measures and non-inferiority bands. What does not survive is treating preservation of those measures as a unique signature of state-target architecture.

The stronger operational signature is **persistence after a transient intervention**:

- perturb the candidate reference during a bounded window;
- remove the perturbation;
- verify that target-defining kinetic parameters return to baseline;
- ask whether the commanded target remains displaced for a pre-declared number of settling times while regulation remains competent.

A pure parameter-target system should revert when the parameter-setting intervention is removed. If it does not, a hidden state or hysteretic memory has entered the description, and the exclusion itself needs revisiting. This test remains close to S.2, but at least it is physical, representation-constraining, and capable of exposing a hidden state.

For the non-definitional part of P1, define two errors separately:

- **internal tracking error**: deviation of the regulated output from the system's corrupted internal command;
- **viability error**: deviation of that command/output from the externally declared viability-relevant target under **D**.

Competent misregulation is the quadrant **low internal error + high viability error**, with the closed-loop performance vector inside pre-declared equivalence bounds. That is a measurable dissociation between what the controller is doing well and what persistence requires; it does more work than “the operating point moved.”

#### The EnvZ paper is an experiment specification, not an already-run kill

Jones et al. show an engineered EnvZ-derived covalent-modification cycle whose output varies with kinase:phosphatase dosage and with small-molecule control of phosphatase stability. They also show that a closed-loop phosphatase-feedback design reduces noise and mitigates selected gene-expression perturbations. Those results make the system an excellent required arm. They do **not** establish that the same target sweep preserves gain, settling time, precision, and disturbance rejection. Settling time is not reported in the relevant experiment, and the tuning and robustness claims are not the joint equivalence test Prime proposes.

The correct status is therefore: **live required test, not existing counterexample and not existing vindication**.

### 2.2 Reading A/B: the canon wording is defective, but Reading B is not theorem-forced

Prime's attribution correction is sound. Canon v1.26 §11a itself says the discriminator is a “proper invariant subspace whose dynamics are autonomous with respect to the regulated coordinates.” The defect is in canon as well as the follow-on.

The three grounds offered for Reading B do not all hold:

1. **Sontag is narrower and more subtle than the adjudication says.** Under stated assumptions, adaptation to a signal class plus signal detection implies an output-driven internal model. In the theorem's decomposition, the internal-model subsystem receives the regulated output/error; when that output is zero, its own dynamics generate the exosystem signals. This contradicts a requirement of *global* independence from the regulated error. It does not show that every invariant/zero-dynamics formulation is wrong, and it does not supply timescale separation, viability relevance, or separate physical addressability.
2. **The S.5 incompatibility is a KaiABC finding, not a universal refutation.** Strict autonomy and a lifetime observable are unavailable in the same Kai preparation. That can disqualify KaiABC under Reading A. It does not prove that no living system could exhibit an autonomous reference subsystem in vivo.
3. **Non-discrimination in this candidate set shows empirical redundancy, not logical falsity.** A necessary condition can be redundant with another filter in one sample. Before canon removal, the question is whether the condition adds invariant content or protects against false positives outside this set.

The better repair is a **Reading C** that keeps the invariant idea but allows error-driven regulation:

> There exists a physically identifiable internal-model subsystem \(z\), separately intervenable from the regulated path, with dynamics \(\dot z=f_z(z,e)\), where \(e\) is regulated error; on the output-zeroing manifold \(e=0\), \(z\) evolves under \(f_z(z,0)\) and can generate the admissible reference trajectory. A readout of \(z\) drives the regulated coordinates, and its content is causally relevant to the declared persistence functional \(V\).

This is compatible with the structure Sontag actually proves within his scope, does not reduce decoupling to slow timescale, and still excludes an antithetic controller whose integrator state is an actuator state while its target remains \(\mu/\theta\).

### 2.3 The valuable filter is overclaimed and currently non-invariant

The selection report's auditable score table contains:

| Target classification | Count shown in score table |
|---|---:|
| Parameter | 6 |
| State | 1 |
| Undetermined | 1 |

Several further candidates are expressly “longlisted, not reached.” On the filed artifacts, “13 of 14” is therefore unsupported. Either supply a fourteen-row appendix with the closed form and target classification for every system or replace the headline with the count the report actually displays. The present denominator inflates both the empirical independence and the severity of the clock-only result.

Even after that correction, target-as-state versus target-as-parameter cannot simply replace §11a. In ordinary dynamical modeling, a constant parameter can be represented as a state satisfying \(\dot\theta=0\); a slow state can be absorbed as a quasi-static parameter under model reduction. The distinction becomes physical only when tied to:

- the declared intervention class **I**;
- persistence of displacement after intervention washout;
- identifiability of unchanged kinetic parameters;
- causal readout from the candidate reference into the regulated path.

The filter is a strong **candidate operationalization**. It is not yet a similarity- or realization-invariant canon discriminator.

### 2.4 §4 dissent: KaiABC may be selecting temporal models, not living regulation

Prime's dissent should stand, with one sharpening. Clock phase is not straightforwardly a “set-point.” It is an internal state of an exosystem model; its readout supplies a time-varying command to downstream physiology. Period is a parameter. The report itself discovers this phase/period split, but then treats phase as sufficient for S.2.

The ownership-free language of canon v1.26 does not resolve the problem. Declaring \(V\) tells the analyst which persistence criterion semantic weight is evaluated against. It does not cause Kai phase to encode that criterion. Component (5) of the follow-on still requires a causal relation between reference content and the declared viable set, not merely correlation with an environmental variable that happens to affect fitness.

KaiABC can earn positive status only through an explicit content test, for example:

- a transient phase reset leaves the clock displaced after the perturbation is removed;
- internal tracking remains precise relative to the shifted clock program;
- the shifted program is wrong relative to a pre-declared light/dark environment and \(V\);
- a phase-matched environmental rescue restores the lifetime/growth outcome without repairing the clock.

That last rescue is especially valuable: it distinguishes “damaged clock” from “competent clock in the wrong world-alignment.”

Until then, KaiABC is a defensible **positive architecture probe** and a borderline **positive life-criterion article**. A one-member positive class consisting of a clock cannot support the claim that the criterion captures the cell paradigm. Nor can the filed search support “the cell's own regulators are all target-as-parameter,” because several named cellular systems were not reached.

### 2.5 P2: scientifically salvageable, procedurally an amendment

Prime is scientifically right that P2 is a claim about the discrimination method and can be tested on a system other than the positive P1 article. But the Gate 1 selection order says: “A candidate must clear all four,” and S.4 explicitly requires a two-order tunable slow/fast sweep. The report then says KaiABC is not rejected on S.4 because S.4 is “not a disqualifier under the order's phrasing.” That statement contradicts the order's text.

The clean action is:

- leave the frozen P2 substance and disposition rule unchanged;
- issue a dated **Gate 1 selection-order amendment** allowing prediction-specific articles;
- define “the chosen system” in P2's UNINFORMATIVE row as the pre-declared P2 arm;
- disclose that the original single-article S.4 screen was abandoned before P2 data were examined.

An in-silico construct may be used for power analysis and pipeline validation, but the frozen prediction says “on a real system.” The scored P2 arm should therefore be a physical antithetic controller or another experimentally realized construct.

P2 also needs an orthogonal sweep: vary the slow/fast ratio while holding target, architecture, dimension, intervention class, and nominal operating point as constant as practicable. If the same parameter sweep changes both target and timescale, a detected knee is uninterpretable. Finally, the verdict must come from a blinded empirical classifier. If the verdict is assigned directly from the algebraic label “state” or “parameter,” flatness is guaranteed by definition and P2 becomes another test that cannot fail.

---

## 3. Actionable Fixes

### Required before the decision #2 freeze

1. **Correct or substantiate “13 of 14.”** Deposit a fourteen-row target-classification appendix with the operative equation for each case, or revise every 13/14 claim to the auditable score-table count.
2. **Amend the Gate 1 selection order openly.** State that P1, P2, and P3 may use prediction-specific articles; identify the abandoned S.4 single-article requirement and why it was changed. Do not label this a neutral reading.
3. **Replace the proposed P1 dynamics rule.** Use a transient-intervention/washout test, parameter-return checks, an internal-error versus viability-error dissociation, and pre-declared non-inferiority margins for the performance vector. Remove the general assertion that parameter targets must drag dynamics.
4. **Carry engineered EnvZ/OmpR as a required P1 negative arm.** Treat the existing paper as design evidence. Pre-register the missing joint experiment rather than scoring the published tunability result as if it already measured preserved settling, gain, precision, and rejection.
5. **Adopt Reading C for this experiment.** Record Reading B as the looser alternative, not as theorem-forced. Keep any §11a canon replacement in proposal status until its invariance and false-positive behavior are tested.
6. **Make KaiABC's component-(5) burden explicit.** Pre-register the phase-matched environmental rescue or an equivalent causal content test. If that test cannot be specified, label KaiABC an architecture probe and narrow the claim accordingly.
7. **Build P2 on a real, orthogonally tunable construct.** Use simulation only to set range, power, and knee-detection thresholds. The empirical classifier and knee rule must be frozen before the sweep.
8. **Wait for the independent bibliography defect count.** Any further fabricated or unsupported attribution affecting a load-bearing claim must be corrected by visible corrigendum before freeze.

### Suggested pre-registration language for the P1 core

> Competent misregulation requires a post-intervention interval in which (i) the internal regulatory error relative to the displaced command remains within the pre-declared competence band; (ii) deviation from the viability-relevant target under the declared \(V\) exceeds the misregulation threshold; (iii) the perturbation has been removed and target-defining kinetic parameters have returned within their baseline equivalence bands; and (iv) gain, settling time, precision/noise, and disturbance rejection meet pre-declared non-inferiority margins. Failure of an excluded system to revert after washout triggers a hidden-state/reclassification review before it is scored as a P1 kill.

This language is optional and non-canonical. Numeric bands and observation windows remain to be filled from the selected systems and power analysis.

---

## 4. Creative Opportunities

### 4.1 The deeper discriminator may be target provenance, not merely target implementation

The clock objection reveals a second axis that state-versus-parameter misses:

| Target implementation | Target referent |
|---|---|
| state / distributed memory / parameter | declared viable set / external environment / arbitrary engineered command / constitutive equilibrium |

KaiABC is state-implemented but primarily models external time. Antithetic control is parameter-implemented and regulates an arbitrary engineered command. A genuine viability reference would need both an implementation claim and a referent/content claim. This two-axis taxonomy is more resistant to the “criterion for clocks” failure than either subspace autonomy or state-versus-parameter alone.

### 4.2 The clean P1 signature is an error dissociation

The most distinctive empirical object is not simply a moved operating point. It is the coexistence of:

- low controller error relative to its internal reference;
- high error relative to the declared viability target;
- preserved competence after a transient reference corruption.

That makes “competently wrong” literal and measurable. It also prevents temperature compensation, ordinary retuning, or an uninformative result from being converted automatically into support.

### 4.3 The failed denominator can become a better discovery program

Instead of claiming representativeness from 14 heterogeneous candidates, treat the current result as a hypothesis-generating audit: six auditable parameter targets, one state target, one undetermined. Then run a pre-declared replication panel across independent regulatory families, with one model form and one classification protocol. That would turn the report's best observation into evidence rather than a striking but unstable count.

---

## OAI disposition

**Gate 1: CONDITIONALLY OPEN.** The pair is promising enough to support drafting, but not enough to support freezing. The correct provisional structure is three arms: KaiABC (positive/state-memory and viability-content test), engineered EnvZ/OmpR (excluded-system P1 attack), and a physical antithetic controller (P2 method sweep). Decision #2 should wait for the numerical corrigendum, Gate 1 amendment, P1 rewrite, Kai content test, and bibliography report.

The most important canon proposal remains live but changes form: **do not yet replace subspace autonomy with state-versus-parameter. Replace global autonomy with an error-driven zero-dynamics/internal-model formulation, then add target implementation and target referent as separate operational tests.**

---

*End of `REV_AOP_LifeCriterion_Gate1_OAI_Attack_v0_1_20260803.md`. Outside-critic deposit. Recommendations only; no canon edit and no self-certification.*
