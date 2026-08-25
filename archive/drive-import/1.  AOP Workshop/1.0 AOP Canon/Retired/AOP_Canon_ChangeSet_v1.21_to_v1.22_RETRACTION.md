# AOP Canon — Proposed Change Set v1.21 → v1.22: retraction of the §13a level-selection closure

**Drafted 22 July 2026 by Prime (chat/judgment seat). PROPOSED — not applied. Master untouched.**
**Nobody grades their own homework: this draft must be checked by a seat that is not Prime before Cowork folds it.**

**Canon under change:** `AOP_CANON_MASTER_v1.21.md`, Canon folder `1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J`,
id `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`, 208,518 bytes, masthead "version 1.21", modified
2026-07-21T19:15:04Z. Currency confirmed against the live folder this session.

**What this change set is.** AOP's **first outright retraction**. Prior movements (v1.19, v1.21) were
de-scopes and re-grades: a claim was narrowed or its grade lowered. This one withdraws a result. The
§13a level-selection paragraph asserted a closure ("closes the level-selection half of the F2 seam")
whose every load-bearing element is false, undefined, or unevidenced. No amount of trimming leaves a
defensible residue, so the closure is withdrawn and the F2 seam returns to fully open.

**No claim is weakened by concealment and nothing is quietly dropped.** Every computed fact that
survives is retained and restated; what is withdrawn is the *individuation reading* laid over those
facts, and the closure grade that reading supported.

Markers: ✓ primary read this session · ~ named/result-level · ⊙ canon-inherited.
Grades: SETTLED / SYNTHESIS / FRONTIER / DEFECT / **RETRACTED**.

---

## 0. Provenance of the finding (who found what, and who checked it)

Recorded because the disposition rests on it, and because two of the three parties were wrong at
some point in the chain.

| Step | Seat | Outcome |
|---|---|---|
| Initial finding | Prime | §13a's crossover is an unnormalized small-side artifact; alleged `phaseD1` used a non-canonical selector |
| Independent verification | Aster | Computation **reproduced**; Prime's primary-source premise **contradicted** — Aguilera & Di Paolo's MIP selector *is* raw/unnormalized. Prime's allegation **retracted** |
| Prime re-check | Prime | Aguilera primary (arXiv:1806.07879) read directly: Eq. 5 is a bare Wasserstein distance, the MIP is `min` over cuts with no normalizer, the singleton sentence is verbatim. **Aster correct; Prime's premise dead** |
| Adversarial pass | Aster (rev2) | Four Prime findings graded STANDS / OVERREACH / FALLS; **six new defects** found, several higher-value than the original finding |
| Verification of the critic | Prime | All of Aster's new numbers independently reproduced (below). Citation defect confirmed against primary and found to be **larger** than stated |

**Prime's errors in this chain, recorded rather than buried.** (1) The Aguilera-normalization premise
was asserted on recall and was wrong. (2) Prime quoted the cross-grain crossover as "≈0.33" after
reading it off a coarse grid; the true value is 0.3002367 — the identical error Prime had just
criticized in `phaseD1`'s deposited ramp. Both were caught by the adversarial loop, which is the
loop working; but the lesson is that Prime's own quick computations require the same independent
re-run as any builder's.

---

## 1. Verification record for the numbers this change set relies on

Every number below was computed independently by Prime from specification, and independently by
Aster from specification. Model: `N` nodes in two equal complete modules, intra-module weight
a = 1.0, inter-module weight b, g = 1.0, Σ = (I + gL)⁻¹; Φ across a bipartition is the Gaussian
mutual information ½(logdet Σ_AA + logdet Σ_BB − logdet Σ); all bipartitions enumerated exhaustively;
exact linear algebra, no estimation.

| Quantity | Value | Status |
|---|---|---|
| Whole-system MIP relabel, module cut → singleton (N=8) | b = 0.330221124862 | ✓ reproduced by both seats |
| Whole-system MIP relabel (N=6) | b = 0.420600748420 | ✓ reproduced by both seats |
| Module/whole raw Φ equality, **marginal** module | b = 0.3002367 | ✓ reproduced by both seats |
| Module/whole raw Φ equality, **conditional** module | b = 0.2163268 | ✓ reproduced by both seats |
| Module/whole raw Φ equality, **isolated** module | b = 0.6295630 | ✓ reproduced by both seats |
| Size- and entropy-normalized selectors: module cut holds to b = 1, then balanced cut | b = 1.000 | ✓ reproduced by both seats |
| Φ_MIP value across the relabel (N=8, raw) | 0.195575 → 0.195700 → 0.196758 at b = 0.330 / 0.3302 / 0.34; monotone, with a derivative kink | ✓ values reproduced; **"smooth" was Prime's error — the kink is large** |
| Two-supernode coarse-graining vs micro | identical while the module cut is the MIP; macro strictly greater once the MIP goes singleton | ✓ reproduced |

**Primary sources read this session (✓).** Aguilera M, Di Paolo EA, *Integrated information in the
thermodynamic limit* (arXiv:1806.07879; Neural Networks 114:136–146, 2019) — Eq. 5, the MIP
definition, §III.B, Fig. 3.G, and the Discussion. Liu K, Yuan B, Zhang J, *An Exact Theory of Causal
Emergence for Linear Stochastic Iteration Systems* (arXiv:2405.09207v2) — title, author list,
journal-ref, and abstract.

---

## 2. The six defects that force the retraction

**D1 — The coincidence claim is quantitatively false.** §13a asserts the whole's MIP leaves the
module boundary "at precisely that crossover," welding the grain transition to the MIP relabel. They
are different points: 0.3002367 versus 0.3302211, separated by 0.030. Two distinct events, asserted
as one.

**D2 — The stated crossover number is wrong.** §13a gives "≈ half the intra-module weight in a
worked eight-node case," i.e. b ≈ 0.5. The MIP relabel is at 0.3302; the grain equality is at
0.3002. Neither is ≈0.5. The deposited ramp sampled coarsely (b = 0.3, then 0.5) and labelled the
first post-transition sample instead of locating the crossover.

**D3 — "Module" is undefined, and the answer moves with the construction.** The three natural
readings of the module as a subsystem — marginal, conditional on the complement, and isolated —
place the raw equality at 0.3002, 0.2163, and 0.6296 respectively: a factor of three. §13a declares
none of them. This is a failure of the framework's own declaration discipline (the declaration tuple
D, §2): the coarse-graining map is exactly the kind of object AOP requires to be declared.

**D4 — Claim 1 was never computed, and computed literally it goes the other way.** The paragraph
asserts the grain *maximizing* Φ_MIP moves module → whole. `phaseD1` contains no coarse-grained
covariance, no two-supernode Φ, no candidate-grain score table, and no maximization across grains;
it tracks the raw minimum cut of one fixed eight-node graph. Under a literal two-supernode
coarse-graining the result is tie → macro, not module → whole.

**D5 — Three distinct operations are conflated.** §13a runs together (i) system-boundary selection
(which candidate *system* is the individual — Aguilera's φ_A vs φ_AE), (ii) coarse-grain selection
(which *grain* of a nested hierarchy maximizes Φ — Hoel's Φ-max), and (iii) MIP location within one
fixed system (where the weakest cut sits). Only (iii) was computed. The word "whole" does duty for
all three.

**D6 — The Gaussian anchor is misattributed, and the §13a body mischaracterizes it.** arXiv:2405.09207
is **Kaiwei Liu, Bing Yuan, Jiang Zhang**, published as ***Entropy* 2024, 26(8), 618**
(doi:10.3390/e26080618). The canon reference entry reads "Zhang J, Zhao K, et al. … *npj Complexity*
(2025)" — wrong first author, a co-author who does not appear, wrong venue, wrong year. Separately,
the §13a *body* attributes the optimal coarse-graining to eigenvectors "of the system's covariance";
the paper determines it from the principal eigenvalues and eigenvectors of the **dynamic system's
parameter matrix**, and states the optimal coarse-graining is **not unique**. (The reference entry's
own gloss, "dynamics-matrix eigenvalues," is correct; the body is not.)

**The unifying mechanism (Prime, adversarially unchecked — flagged).** Φ at the two-supernode grain
and Φ_MIP of the whole are *identical* for as long as the whole's MIP is the module cut, and diverge
only once the MIP relabels to a singleton. If this holds, the apparent grain transition is not a
grain phenomenon at all but the singleton relabel in different clothing, collapsing D1 and D4 into
one artifact. **This is Prime's observation, produced in the judgment seat and not yet attacked; it
is recorded as motivation, and no edit below depends on it.**

---

## 3. What survives

Stated explicitly so the retraction is bounded and nothing true is thrown away with the false.

- **The computed facts stand.** The MIP relabels from the module cut to a singleton at b = 0.3302211
  (N=8) and 0.4206007 (N=6); under size- and entropy-normalization the module cut holds to b = 1 and
  then yields to a balanced cut; Φ_MIP's value is monotone increasing throughout, with a derivative
  kink at each relabel; zero-calibration (Φ_MIP = 0 on block-decomposable Σ) is untouched.
- **The Φ_MIP axis itself is untouched.** §4's one-vs-many coordinate at a *fixed* partition, its
  five-criterion gate, and its zero-calibration are not in question. This retraction is confined to
  *level selection across grains* and to the reading of MIP relabeling.
- **The literature anchors stand as literature.** Hoel et al. 2016 and Marshall et al. 2026 remain
  a settled Φ-max grain rule *within IIT, on discrete systems*. Aguilera & Di Paolo §III.B remains a
  real precedent for selecting among candidate *systems* by comparing φ values. What fails is AOP's
  port and AOP's claim to have computed it.
- **The correct general statement, which replaces the retracted one:** a MIP relabeling proves that
  the argmin changed. It does not, on its own, evidence a change in individuality.

---

## 4. The edits

Each gives **LOCATION**, **OLD** (verbatim from v1.21), **NEW**, **WHY**, and a grade. Whoever
applies maps to the master's markdown escaping. Line numbers are from the decoded v1.21 master and
are advisory; match on text.

### EDIT R1 · §13a, level-selection paragraph (line ~775) — **RETRACT AND REPLACE**

**OLD (the full paragraph, beginning "**Level selection across a nested hierarchy** …"):** the
paragraph asserting that "the rule computes exactly: on a two-module Gaussian, the grain that
maximizes Φ_MIP is the module when inter-module coupling is weak and moves to the whole once
inter-module coupling is tightened past a crossover (≈ half the intra-module weight in a worked
eight-node case), with the whole's minimum information partition ceasing to fall on the module
boundary at precisely that crossover — the signature of the whole becoming one irreducible
individual," and grading the result **[SYNTHESIS; analytic-model-result]**.

**NEW:**

> **Level selection across a nested hierarchy [OPEN; a prior closure retracted in v1.22].** Φ_MIP
> fixes one-vs-many at a *fixed* grain; a nested system (nodes within modules within a whole) also
> poses the *which-grain* question. The literature supplies a rule: order candidate grains by their
> integrated information and read the maximizing grain as the most one-irreducible whole — the Φ^Max
> 'complex' of IIT [Hoel, Albantakis, Marshall & Tononi 2016; Marshall et al. 2026 — SETTLED within
> IIT, discrete binary systems], with a related closed-form treatment of optimal linear
> coarse-graining in continuous Gaussian systems [Liu, Yuan & Zhang 2024, analytic], and a precedent
> for choosing among candidate *systems* by comparing integrated information across them
> [Aguilera & Di Paolo 2019, §III.B].
>
> **This framework has not ported that rule.** Versions 1.20 and 1.21 reported a port as computed;
> that report is withdrawn. What the deposited computation established is narrower and is retained:
> on a two-module Gaussian, the minimum information partition of the *whole* system relabels from
> the module boundary to a single-node cut as inter-module coupling rises (b = 0.3302 for the
> eight-node case, b = 0.4206 for six nodes, intra-module weight 1), while Φ_MIP's *value* increases
> monotonically through that relabeling with only a derivative kink. **A relabeling of the minimum
> information partition demonstrates that the argmin has moved; it does not by itself evidence a
> change in individuality**, and the singleton outcome is the behaviour the cited source anticipates
> for homogeneous connectivity [Aguilera & Di Paolo 2019]. The relabeling is also normalization-
> dependent: size- and entropy-normalized selectors hold the module boundary until inter- and
> intra-module coupling are equal and then move to a balanced cross-module cut.
>
> A genuine level-selection result in this setting requires four declarations this framework has not
> made: a coarse-graining map; a construction of a part as a subsystem (marginal, conditional, and
> isolated constructions place the module/whole equality at b = 0.3002, 0.2163, and 0.6296
> respectively); a convention for comparing Φ across grains of different dimension, which carries the
> same size bias one level up; and an actual comparison of Φ across candidate grains rather than of
> partition location within one grain. Until those exist, **the level-selection half of the F2 seam
> is open, not closed.** **[RETRACTED closure; the residual computed facts are analytic-model-results.]**

**WHY:** the retracted paragraph rests on a false coincidence (D1), a wrong number (D2), an
undeclared construction (D3), an uncomputed claim (D4), a three-way conflation (D5), and a
misattributed anchor (D6). The replacement keeps every true computed fact, states the general
lesson, and names precisely what a real result would need. **[RETRACTION.]**

---

### EDIT R2 · §13a, moving-partition paragraph (line ~777) — correct the kink reading

**OLD (fragment):** "… along a ramp that merges two modules the MIP relabels at a kink where the
least-disrupting seam rotates from between-module to cross-module (Φ_MIP(t) continuous, its
derivative discontinuous) …"

**NEW:** "… along a ramp that merges two modules the MIP relabels at a kink where the least-disrupting
seam rotates from between-module to cross-module (Φ_MIP(t) continuous, its derivative discontinuous).
The kink marks a change of optimizer, not an individuation event: Φ_MIP is a minimum over
partitions, so an argmin exchange necessarily produces a derivative discontinuity whether or not the
system's individuality has changed. The relabeling is what a time-extended partition would have to
track; it is not itself evidence that the system became one individual. …"

**Also strike, in the same paragraph:** the clause reporting that level selection is synthesized —
"(§13/§13a, where level selection is synthesized …)" style cross-references, and the closing sentence
"The framework's principal open problem is therefore now the *time-extended moving partition*, not the
whole seam." **Replace the closing sentence with:** "With the level-selection closure retracted
(above), the F2 seam is open in both halves: level selection is unported, and the time-extended
moving partition remains the harder of the two."

**WHY:** the adversarial pass established that the F1 continuity argument, correctly stated, reaches
this passage as well. Left uncorrected, the canon would read a kink as an individuation signal in one
paragraph and deny it in the one above. **[correction; SYNTHESIS → scoped.]**

---

### EDIT R3 · §4, Φ_MIP introduction (line ~139) — strike the normalization-robustness claim

**OLD:** "Its individuation ordering is invariant under per-component rescaling and robust across
minimum-partition normalizations, so it needs no analogue of the resolvability K-convention;"

**NEW:** "Its individuation ordering is invariant under per-component rescaling. It is **not**
robust across minimum-partition normalizations where the question is *which* partition is minimal:
on a two-module Gaussian the raw selector relabels to a single-node cut at b ≈ 0.33 while size- and
entropy-normalized selectors hold the module boundary to b = 1 and then move to a balanced cut. The
normalizer is therefore a declaration the framework must make wherever partition *identity* carries
weight, though the *magnitude* ordering at a fixed partition is unaffected;"

**WHY:** the claim as written is contradicted for the partition-identity question. Scoped honestly,
magnitude ordering survives and identity does not. **[DEFECT-fix.]**

---

### EDIT R4 · §12, Φ_MIP status-table row (line ~632) — same correction in the ledger

**OLD (fragment):** "ordering rescaling-invariant and normalization-robust within the minimum-cut
family. Secure within static Gaussian models; nested level-selection and the non-stationary/critical
extensions are frontier"

**NEW (fragment):** "ordering rescaling-invariant; magnitude ordering at a fixed partition is
normalization-robust within the minimum-cut family, but partition *identity* is not — the normalizer
is a required declaration (§4). Secure within static Gaussian models; nested level-selection (a v1.20
closure **retracted in v1.22**) and the non-stationary/critical extensions are frontier"

**WHY:** aligns the ledger with R1 and R3. **[re-grade.]**

---

### EDIT R5 · §9a (line ~410) — the F2 seam is not half-closed

**OLD:** "bottlenecked on the nested-level Φ_MIP extension of Section 4 — the framework's principal
open problem — now narrowed to the *time-extended moving partition* (§13/§13a, where level selection
is synthesized and the adiabatic spatial extension is computed), shared with the Ladder rebuild.]**"

**NEW:** "bottlenecked on the nested-level Φ_MIP extension of Section 4 — the framework's principal
open problem. The v1.20 narrowing of this seam to the *time-extended moving partition* is withdrawn
in v1.22: the level-selection half is unported (§13a), so the seam is open in both halves, with the
adiabatic spatial extension computed but its individuation reading corrected. Shared with the Ladder
rebuild.]**"

**WHY:** the narrowing was licensed by the level-selection closure. Retract one, retract the other.
**[propagated retraction.]**

---

### EDIT R6 · References (line ~968) — correct the misattributed entry

**OLD:** "Zhang J, Zhao K, et al. An exact theory of causal emergence for linear stochastic iteration
systems. *npj Complexity* (2025). arXiv:2405.09207. — closed-form Gaussian effective information;
optimal coarse-graining set by the dynamics-matrix eigenvalues (the Gaussian bridge for level
selection). [✓ named this session; ⚠ confirm full author list before final.]"

**NEW:** "Liu K, Yuan B, Zhang J. An exact theory of causal emergence for linear stochastic iteration
systems. *Entropy* **26**(8), 618 (2024). doi:10.3390/e26080618; arXiv:2405.09207. — closed-form
effective information for linear stochastic iteration systems with Gaussian noise; optimal linear
coarse-graining determined by the principal eigenvalues and eigenvectors of the **dynamics parameter
matrix**, and explicitly **not unique**. [✓ title, author list, journal-ref and abstract verified
against the primary this session; the v1.20 ⚠ on the author list is **discharged with correction** —
first author, venue and year were all wrong. Cited as context for level selection, which this
framework has **not** ported (§13a).]"

**WHY:** discharges a carried ⚠ by correcting rather than confirming it, and records the non-uniqueness
the retracted paragraph leaned against. **[DEFECT-fix; SETTLED bibliographic.]**

---

### EDIT R7 · Masthead — prepend the v1.22 clause

Prepend to the masthead's running summary, ahead of the v1.21 clause, leaving all prior text intact
(the masthead is a running summary; version history below it is **append-only** and the v1.20/v1.21
entries are **not** edited):

**ADD:** "v1.22 retracts one v1.20 result: the §13a nested-hierarchy level-selection closure. An
independent verification and an adversarial pass established that the reported crossover conflates two
distinct events 0.030 apart, quotes a wrong threshold, leaves the coarse-graining construction
undeclared (three natural constructions differ by a factor of three), and reports a cross-grain
maximization that the deposited computation never performed. The computed facts are retained and
restated; the individuation reading of a partition relabeling is withdrawn — a relabeling proves the
argmin moved, not that individuality changed — and the F2 seam returns to open in both halves. The
Gaussian anchor is re-attributed (Liu, Yuan & Zhang, *Entropy* 2024, not Zhang & Zhao, npj Complexity
2025). This is the framework's first retraction rather than a de-scope."

**WHY:** the masthead is the current-state statement and must not continue to advertise a withdrawn
closure. **[RETRACTION, surfaced.]**

---

### EDIT R8 · Data accessibility (line ~785) — scope the deposited script honestly

**ADD after the `phaseD1_levelselect.py` listing:** "`phaseD1_levelselect.py` computes the minimum
information partition of a single fixed graph as inter-module coupling varies. It does **not** compute
a cross-grain comparison; its header and console output describe the partition relabeling as a
module-to-whole grain transition, which the code does not perform. The script is retained as the
record of what was computed (§13a, v1.22 retraction)."

**WHY:** the deposited artifact's own labelling is part of the defect; the deposit stays, correctly
described. **[honesty fix.]**

---

## 5. Proposed changelog entry (append; do not edit prior entries)

> ### R[next] · Canon movement: v1.21 → v1.22 — retraction of the §13a level-selection closure
> - **What.** One v1.20 result is **retracted**: the nested-hierarchy level-selection paragraph (§13a)
>   and its claim to close the level-selection half of the F2 seam. Six defects force it: (1) the
>   asserted coincidence between the grain crossover and the MIP relabel is false — 0.3002367 versus
>   0.3302211; (2) the quoted threshold "≈ half the intra-module weight" is wrong for both events;
>   (3) the construction of a "module" as a subsystem is undeclared, and the marginal, conditional and
>   isolated constructions place the equality at 0.3002, 0.2163 and 0.6296; (4) the cross-grain
>   maximization was never computed, and a literal two-supernode coarse-graining gives tie → macro,
>   not module → whole; (5) three distinct operations (system-boundary selection, coarse-grain
>   selection, MIP location) are conflated; (6) the Gaussian anchor is misattributed and the §13a body
>   misstates which matrix supplies the eigenstructure. The general lesson is folded into §13a and the
>   moving-partition passage: **a minimum-information-partition relabeling proves the argmin moved, not
>   that individuality changed.** Consequential edits: the normalization-robustness claim is scoped to
>   magnitude-at-fixed-partition (§4, §12); the §9a narrowing of the principal open problem is
>   withdrawn and the F2 seam returns to open in both halves; the reference entry is corrected to Liu,
>   Yuan & Zhang, *Entropy* 26(8):618 (2024); the deposited script is re-described to match what it
>   computes.
> - **What is retained.** Every computed number stands and is restated: the MIP relabel points
>   (0.3302211 at N=8, 0.4206007 at N=6), the monotone Φ_MIP value with a derivative kink at each
>   relabel, the normalized selectors' behaviour at b = 1, and zero-calibration. The Φ_MIP axis itself
>   (§4, one-vs-many at a fixed partition, and its five-criterion gate) is untouched.
> - **Why.** Prime raised a defect whose primary-source premise was then **contradicted** by an
>   independent verification; the corrected finding was routed to an adversarial pass which graded
>   Prime's four follow-on findings (two STAND, two OVERREACH in their implications, one factual
>   element FALLS) and surfaced six further defects, most of them larger than the original. Prime then
>   independently reproduced every one of the critic's numbers and verified the citation defect against
>   the primary.
> - **Grade.** One **retraction** (level-selection closure: SYNTHESIS → RETRACTED/OPEN); one
>   correction (the kink reading, §13a moving partition); one scoping fix (normalization-robustness);
>   one propagated withdrawal (§9a seam narrowing); one bibliographic correction discharging a carried
>   ⚠ by correcting it. No claim is strengthened. The disposition-typed count of genuinely open items
>   rises from ≥2 to ≥3 (level selection rejoins the time-extended moving partition and the stellar
>   positive-persistence mechanism).
> - **Verification.** Aguilera & Di Paolo 2019 (arXiv:1806.07879) and Liu, Yuan & Zhang 2024
>   (arXiv:2405.09207v2) read against primary this session (✓). All computed values independently
>   reproduced by two seats from specification (Prime and Aster), exhaustive enumeration, exact linear
>   algebra, no estimation.
> - **Downstream.** The F2 seam re-opening and the corrected kink reading change the open-problem
>   inventory → cross-project (Ladder) propagation-bus note warranted. The CS moving-MIP
>   well-posedness gate inferred well-posedness from a surviving relabel and inherits the corrected
>   reading; its "well-posed" stamp is **suspended pending re-examination**, and the moving-MIP repair
>   remains parked.
> - **Status.** Proposed — awaiting an independent check of this draft, then fold.

---

## 6. Ladder propagation-bus note (draft)

The basement moved, and this time downward. (1) The level-selection half of the F2 seam is **open
again** — the v1.20 closure is retracted; any Ladder rung that inherited "which level is the
individual is settled for static Gaussian systems" loses that support. (2) The general correction
applies wherever the Ladder reads a partition change as an individuation event: **a MIP relabeling
proves an optimizer changed, not that individuality changed.** (3) The framework's principal open
problem is no longer "narrowed to the time-extended moving partition"; it is open in both halves.
(4) The §9 higher-individual and §9a collective-alive routes remain bottlenecked, now on a wider
seam than v1.21 recorded. Post to the bus.

---

## 7. Open items this change set does **not** close

- **The unifying mechanism** (Φ_macro ≡ Φ_whole until the MIP goes singleton) is Prime's, unattacked,
  and load-bearing on nothing here. If it survives a critic pass it would simplify §13a's account of
  why the two crossovers appeared near-coincident; it is not required for the retraction.
- **The CS moving-MIP well-posedness gate** needs re-examination under the corrected kink reading
  before the moving-MIP repair is scoped. Its verdict was "well-posed because a genuine relabel
  survives normalization"; that inference is the same overreach corrected in R2.
- **Whether a genuine level-selection result is obtainable** in the static-Gaussian setting at all,
  given that the cross-grain comparison inherits the size bias and the cited Gaussian treatment
  states its optimal coarse-graining is not unique. This is now an open research question, not a
  deferred computation.
- **Carried verification debt, unchanged:** Marshall et al. 2026 (Neurosci. Conscious. niag013)
  author list; full-text reads of Maes 2020, Schnakenberg 1976, Bouchet–Reygner 2016, Oono–Paniconi
  1998. The Ptaszyński & Esposito and Liu–Yuan–Zhang items are now discharged.

---

*Drafted in the judgment seat. Prime found the original defect, was wrong about its cause, and was
wrong again about one number; both errors were caught by independent seats and are recorded above
rather than absorbed. This draft is a proposal. It must be checked by a seat that is not Prime, and
Ben decides, before Cowork folds it. The master has not been touched.*
