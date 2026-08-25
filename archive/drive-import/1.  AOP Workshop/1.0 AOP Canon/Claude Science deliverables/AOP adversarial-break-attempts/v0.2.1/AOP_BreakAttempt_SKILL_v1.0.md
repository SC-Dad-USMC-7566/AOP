---
name: adversarial-break-attempt
description: Run a structured break attempt on a scientific proposal, protocol, or methods contract the user asks you to attack, stress-test, red-team, or "try to break." Fans three independent lanes — analytic counterexamples, parent-document fidelity, and primary-source citation verification — then reports fatal/major findings with dispositions and an honest ledger of attacks that failed. Use when the target is a versioned proposal document (intervention contract, pre-registration, benchmark spec, falsification gate) rather than a finished paper needing copy-edit.
---

# Adversarial break attempt

A break attempt is not a review. A review asks "is this good?"; a break attempt asks
**"can I make this produce a wrong answer, and can I do it inside the document's own
declared envelope?"** The strongest possible finding is a case the target permits, that
its own rules call valid, whose result is indeterminate or false.

## The governing rule

**Attack the method, not the framework.** A methods contract makes two kinds of claim:
what the science says (which lives in a parent canon/paper) and what the protocol will
do. You attack the second. Findings phrased as "this kills the framework" are almost
always overreach; findings phrased as "this bounds what the co-measurement method can
claim" survive. Report every finding against the target's **own** kill conditions and
dispositions where it has them.

## Three lanes, run in parallel

Fan these as independent sub-agents (`host.delegate` with a list). They find different
defect classes and cross-check each other; run sequentially and you will anchor lanes 2
and 3 on lane 1's framing.

1. **Analytic lane (keep this one yourself).** Closed-form counterexamples on the
   target's own declared models. This is where sign indeterminacy, degeneracy, and
   representation traps live.
2. **Fidelity lane.** Every cross-reference to the parent document, graded
   FAITHFUL / DRIFTED / UNSUPPORTED / CONTRADICTS; plus discharge of the review the
   target claims to implement, item by item.
3. **Citation lane.** Every external claim against primary sources, graded
   VERIFIED / PARTIAL / FALSE-MISATTRIBUTED.

**Exclusion rule: the seat that built the target does not grade it.** State in your
report that you did not build it. If you did, say so and decline.

## Workflow

1. **Fetch the target and confirm the parent's version.** Do not attack a document
   against a stale canon. Locate the parent's current version and note it; if the
   target cites "canon vX §N", read §N. When the source is Google Drive markdown, run
   `unescape_drive_markdown()` first — Drive backslash-escapes every `#`, `*`, `|` and
   hard-wraps lines, and diffing the raw export produces phantom findings.
2. **Read the review the target claims to implement**, if there is one. A document
   whose stated purpose is "implements reviewer items 1–8" hands you its own rubric,
   and partial discharge is a finding.
3. **Fan the three lanes.** Give each lane the target and parent as artifact markers,
   tell it explicitly what the other lanes cover so it stays in its own, and require
   that a failure to retrieve is reported as PARTIAL/NOT VERIFIED, never as a pass.
4. **Work the analytic lane while they run.** See the attack patterns below.
5. **Re-verify borrowed fatal findings yourself.** A sub-agent's fatal finding goes in
   your report only after you have read the quoted passage in the parent and, where it
   is computational, reproduced it. Quote verbatim; never paraphrase a parent document
   into a finding.
6. **Grade and dispose.** fatal / major / minor / cosmetic, each mapped to the target's
   own category, each with a concrete repair.
7. **Write the failed-attacks ledger.** Non-negotiable — see below.

## Analytic attack patterns

These recur across intervention protocols. Each has caught a real fatal finding.

- **Symmetry mismatch between reading and outcome.** Check the parity of the measured
  quantity and of the viability response under the same parameter. An entropy-production
  or divergence-type reading is typically **even** under current reversal while a
  first-passage or path outcome is **odd** — so two systems with identical readings get
  opposite-signed contrasts. Construct mirror pairs and tabulate.
- **Undeclared sub-choices.** Enumerate the declaration block's mandatory fields, then
  find a choice the result depends on that no field requires recording. "Which
  absorbing event does V measure?" is the canonical one. Two seats filling every field
  correctly and disagreeing is a fatal specification defect.
- **Representation traps.** Ask whether a change of state description preserves one
  quantity while collapsing another. Check whether the parent document already warns
  about this for this model — an omitted parent warning is worse than a novel finding,
  because the target invites a **false refutation of its own predicted result**.
- **Property assignment.** When a model is chosen *because* it has property P, compute P.
  Distinguish the antecedent from the consequent: "infinite Markov order" does not imply
  "non-summable residual," and conflating them inverts a benchmark's purpose.
- **Prime state spaces.** A product-scramble or in/out-cut intervention needs a
  factorizable state space. Count states: 2 and 3 are prime, so the cut is undefined and
  the contrast cannot run on that model at all.
- **Degeneracy on the reference model.** A null that is the identity map on the
  all-null reference gives ΔV = 0 analytically — which the target's own degeneracy
  clause probably calls a declaration error.
- **Overstated rationales.** A conclusion can be right and its stated reason false.
  "A two-state chain is always detailed-balanced" is false (see
  `two_state_multichannel_sigma`) even though excluding it as a drive control was right.
  Flag reason-defects separately from decision-defects.

## Estimator discipline

Prefer a result you can derive to one you must estimate; a withdrawn headline number is
usually an estimator artifact. Concretely:

- Make claims about **exactly computable** objects. Ladder increments
  `E(M_{k+1}) − E(M_k)` are exact at each k; the residual `ρ_k` depends on a limit. A
  summable increment series proves `ρ_k → 0` without ever extrapolating.
- **Bracket limits, don't extrapolate them.** `markov_ladder` returns an `E_bracket`
  and `rho_upper`; report intervals.
- **Check sample reachability.** Count allowed words at each k and ask what N a plug-in
  estimator needs for its bias to fall below the effect. The interesting tail of a
  ladder is often exactly the part a sampled implementation cannot reach — which is
  usually the half of a finite-sample review item the target left unanswered.
- Never plot float noise as data: if a quantity is exactly zero, say so in text rather
  than drawing it at 1e-14 on a log axis.

## The failed-attacks ledger

Every report ends with what you could **not** break, named specifically. This is not
politeness — it is what makes the fatal findings credible, it tells the author which
parts are load-bearing and safe to build on, and it prevents the report from reading as
a hit piece. Include cases where the target's construction is *better* than the review
that prompted it, and cases where a finding of yours **vindicates** one of its
categories rather than refuting it.

## Report shape

Two or three artifacts, version-stamped in the filename:

- `<Project>_Break_MathAttack_v0.1.md` — findings, each with setup quoted from the
  target, the closed-form derivation, a table of computed values, and a disposition;
  then the failed-attacks ledger; then a dispositions table; then a reproduction
  section naming every formula so another seat can rerun it.
- `<Project>_Break_FidelityAudit_v0.1.md` — cross-reference and review-discharge tables.
- `<Project>_Break_CitationSalvage_v0.1.md` — per-item verdicts with ≤20-word locating
  quotes, and an explicit table of items **NOT VERIFIED** with what each needs.

Lead the chat summary with the fatal findings and the verdict on the target's own gate.
Say plainly which lanes are incomplete. Never report a parked or blocked lane as clear,
and never synthesize a stopped sub-agent's verdicts — if a lane cannot finish, verify
the reachable subset yourself from sources already on hand and file the rest as open.

## Kernel helpers

`skill({skill: "adversarial-break-attempt"})` loads these into your python kernel:

| helper | use |
|---|---|
| `unescape_drive_markdown(text)` | undo Drive's markdown escaping before reading/diffing |
| `hmm_block_entropies(mats, nmax)` | exact block entropies via labelled transfer matrices |
| `markov_ladder(H)` | `E(M_k)`, exact increments, bracketed `E`, `rho_upper`, `summable` |
| `golden_mean_matrices()`, `even_process_matrices()` | the two standard memory benchmarks |
| `word_distribution`, `sigma_window_bits` | finite-window path asymmetry against a declared reversal |
| `driven_ring`, `chain_sigma_bits`, `chain_excess_entropy_bits`, `ring_mfpt` | ring drive control, exact σ, E, first-passage |
| `ring_increment_law(a, b)` | the increment-representation trap: σ preserved, E exactly 0 |
| `two_state_multichannel_sigma(channels)` | two-state NESS — refutes "two-state ⇒ detailed balance" |

Reference values for regression-checking a fresh kernel: Golden Mean `E = 0.2516291674`
with `ρ_k = 0` exactly for k ≥ 1; Even Process `E ∈ [0.9178, 0.9185]`, two-rung ratio
→ 1/2 so `ρ_k ∝ k·2^(−k/2)`; ring at (a, b) = (0.48, 0.12) gives σ = 0.720000 and
E = 0.180855 in the position representation, σ = 0.720000 and E = 0 in increments;
`ring_mfpt` 2.380952 there against 3.333333 at the detailed-balance null.
