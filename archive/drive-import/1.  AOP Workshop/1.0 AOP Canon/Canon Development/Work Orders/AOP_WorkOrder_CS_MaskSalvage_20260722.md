# AOP — Work Order for Claude Science: the mask-salvage computational workstream

**Issued by:** Prime (chat seat), 22 July 2026.
**Role:** builder. Your output is a **proposal**, never a verdict. You do not grade your own work, and
nothing you produce enters the canon without passing through Prime and Ben.
**Hard constraint:** you touch **no canon master**. Cowork is folding v1.22 in parallel. Your artifacts
and Cowork's are disjoint by design. Do not edit, propose edits to, or open for writing any file in the
canon folder.

---

## Background — what happened and why this workstream exists

A semantic-mask salvage diagnostic (`mask_salvage.py`, K4 static-Gaussian, viability set S={0,1}) was
built and independently re-run on 21 July. The verification memo graded it SYNTHESIS/CONFIRMED, reporting
that the salvageable region — the intersection of the mask's *well-defined* and *informative* regions —
is non-empty and non-trivial, with a merge point a\* ≈ 3.3028.

The outside critic then established, and Prime independently confirmed by re-derivation, that **the
non-emptiness is forced by construction**. On the declared equal-strength K4 with a proper viability
subset, the load edge's marginal viability effect vanishes strictly more slowly than the spectator
edge's as coupling → 0. Prime's independent re-derivation reproduced the spectator's third-order scaling
(log-log slope 3.0007). Therefore load sits above spectator at every weak-coupling point, and any sweep
including weak coupling **cannot** return an empty intersection. The existential result could not have
failed.

Two further defects were found:

1. **The code does not implement the predicate its prose declares.** The header advertises
   `salvageable = well_defined AND informative`, with well-definedness as a maximum span width over
   *structural* edges and informativeness requiring load-above-spectator *and* a 0.02 midpoint
   separation. The executable body computes well-definedness on the **load edge only** and drops the
   informativeness flag entirely (`salv = disjoint AND wd_load`). It happens not to change the printed
   K4 table, because the load edge is coincidentally the widest and disjointness coincidentally implies
   the unused condition. The re-run reproduced the numbers faithfully and still missed this — **a
   re-execution confirms arithmetic, not that the estimand matches the prose.**

2. **The a\* ceiling is convention-dependent.** It exists under the full unmatched min–max coalition
   envelope and at coalition cardinality ≥ 3; it vanishes entirely under |C| ≤ 2, sparse sampling, and
   mean attribution — under which the result reduces to "load stays ranked above spectator everywhere,
   with no finite ceiling."

---

## Task A — Pin the viability functional. Do this first; everything else depends on it.

Two independent re-derivations disagree on the load edge's weak-coupling exponent. The outside critic
reports **O(a)**; Prime's from-scratch re-derivation, using Σ = J⁻¹ and V = −½·logdet Σ[S,S] on an
equal-strength K4 precision matrix, obtained a log-log slope of **2.0016** for the load edge while
reproducing **3.0007** for the spectator.

This is a definitional discrepancy, not a disagreement about the physics — the forced-ness conclusion
holds either way, since the spectator vanishes faster in both derivations. But **no regrade text can be
written until the functional is pinned**, because the exponent appears in the argument.

Deliver: the exact viability functional and edge-scrambling semantics `mask_salvage.py` implements,
stated in closed form; the analytic weak-coupling expansion for both edge classes; and a statement of
which re-derivation matches and why the other differs. Prime's script is available on request.

**Do not skip to reproducing the published numbers.** Re-running the script reproduces whatever it does,
including its coincidences. Pin the definition first, then reproduce.

---

## Task B — Reproduce the headline numbers against the pinned definition

Against `mask_salvage.py` (Drive `1GPcrRSySofAD_yZeCcPkpB_S53IOkrC_`, sha256
`20c02ca1243ca6cb8d4f6a174be13d1b2dd338771078132b658a24c82dbaf062` — verify the hash before running):
reproduce a\* to the reported precision (3.3027756…), Ω ≈ 0.81, and the Model 3 interval table.

Report every number that does **not** reproduce exactly, and say so plainly. Directional-only
reproductions must be labelled directional — the project has been burned before by parameter sets that
were not preserved.

---

## Task C — Resolve the predicate/code mismatch

Decide **one** predicate, implement exactly that predicate, and report sensitivity to every threshold it
contains. The two live questions:

- global (max over structural edges) versus load-only well-definedness;
- disjointness alone versus disjointness AND the 0.02 midpoint informativeness flag.

Both defensible; they answer different questions. Pick one, justify the pick, implement it, and show
what changes in the K4 table under each. Deposit the corrected script under a **new filename** — do not
overwrite the deposited artifact, which is now part of the audit record.

---

## Task D — The attribution-convention table. Pre-register before you run.

The single most useful thing this workstream can produce: turn the convention-dependence of the ceiling
from an assertion into a table.

Compute the merge behavior under: full unmatched min–max envelope · |C| ≤ 0,1,2,3,4 · random sparse
sampling at 4/8/16 coalitions · matched-context comparison · uniform-coalition mean · true Shapley value.
For each: does a finite ceiling exist, and where.

**Pre-registration is mandatory and is a governance requirement, not a preference.** Before running,
deposit a short frozen note declaring which conventions you expect to show a ceiling, and what result
would falsify your expectation. Freeze it to Drive with a timestamp *before* the first run. A gate that
has seen its results is not a gate.

---

## Task E — Stretch, only if A–D land. Graded as a lead, not a workstream.

The outside critic proposed that the useful object hiding inside the failed headline is not one scalar
ceiling but a **semantic-attribution phase diagram** with three coordinates: semantic relevance in
matched contexts, attribution stability across coalition contexts, and mechanistic
identifiability/intervenability. The K4 result already hints they separate — matched-context and mean
rankings survive where context-free envelope dominance fails.

This is a plausible and interesting lead. It is **not** approved work, it has no grade, and it must not
acquire canon status by virtue of having appeared in a critic report. If A–D land cleanly and you have
capacity, sketch whether the three coordinates are genuinely independent on the existing K4 model. Sketch
only.

---

## Standing rules that bind this workstream

**Adopt the three-category grading scheme** (from the outside critic, accepted by Prime) in place of the
earlier binary rule. Every computed result you deliver must be classified as one of:

1. **Identity / theorem demonstration** — no flipping parameter exists inside the declared class. Verifies
   code against mathematics; adds **no** evidential weight to the underlying claim.
2. **Constructed contrast / competence check** — a parameter flips the result because the intervention
   *is* the answer key. Establishes logical dissociability or computational competence, not validation.
3. **Contingent result** — a pre-declared parameter can genuinely reverse or erase the outcome. **Only
   this category earns "could have come out otherwise," and only with the parameter named in advance.**

Do not use "pre-registered" as a substitute for contingency. A pre-registered demonstration is still a
demonstration.

**Cite the document.** Any statement that something is open, settled, parked, or discharged must cite the
document that establishes it. Two claims propagated into a fold decision from summaries today without a
source underneath; both were wrong.

**Analytic over estimated.** Closed-form results preferred to estimated ones, per charter. This project
withdrew headline numbers once already because they were estimator artifacts.

**Deposit everything to Drive.** If it isn't in the folder it doesn't count. Prime has no direct channel
to you — the Drive folder is the only shared surface. Deposit scripts, run logs, the pre-registration
note, and your findings memo, and preserve parameter sets. The last workstream lost its originals and had
to be reconstructed.

---

## What you do not do

Do not touch the canon masters. Do not propose canon prose — the regrade text is written by Prime and
Ben after your numbers land. Do not grade your own output as settled. Do not fold anything.

---

## Governance note for Ben, not a task

Charter v1.2 names four working positions: Ben, the chat seat, the execution seat (Cowork), and the
outside critic. Claude Science is not among them. If CS is an active seat, the charter should say so and
say what its output is worth. Governance housekeeping, non-blocking — flagged so it doesn't drift.
