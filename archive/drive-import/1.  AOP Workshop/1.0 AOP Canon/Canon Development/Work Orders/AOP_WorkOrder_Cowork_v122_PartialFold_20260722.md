# AOP — Work Order for Cowork: fold the clean subset of v1.22

**Issued by:** Prime (chat seat), 22 July 2026.
**Authority:** Ben's decision, this session.
**Scope:** fold what has cleared review. Deliberately leave out what has not.

---

## The principle for this fold

v1.22 ships as the **retraction release plus the repairs that cleared independent review**. The
mask-salvage regrade and everything downstream of it is **deferred to v1.23**. Do not widen this fold to
absorb it. A retraction that never ships because its scope kept growing is a worse outcome than a
retraction that ships honestly incomplete and says so.

**The changelog must record what was deferred, not only what was folded.** A reader must not be able to
mistake v1.22 for a completed pass.

---

## Precondition — do this before touching anything

**The second completeness grep is still outstanding and blocks the fold.** The first grep searched four
literal strings Prime happened to name; it surfaced P1-6 (§9a), which means the phrase-level search was
not complete on its own terms. The defect is conceptual, so search the concept:

`at a given cut` · `for a single partition` · `partition held fixed` · `at one partition` ·
`a single cut` · `the declared cut` · `for a fixed cut` · `holding the partition`

Run across both `AOP_CANON_MASTER_v1.22_PROPOSED_ASTER.md` and `AOP_CANON_MASTER_v1.21.md`. Return the
hit list with surrounding lines **to Prime for adjudication before folding**. If it surfaces a site, it
becomes P1-8 and the fold waits for the ruling. Do not adjudicate the hits yourself.

---

## FOLD — the edits that clear

**A. Retraction R1–R8.** Unchanged. Verified faithful by the reconciliation diff (three verbatim).

**B. Coherence edits 1–5.** Unchanged. 1–4 merit-checked as internal-consistency fixes; 5 (Figure MW
regrade) confirmed correct by the outside critic.

**C. P1-1 through P1-6** — the §4 scope extension, in the **revised** form from the verdict response
(near-degeneracy at the crossing, not cross-normalizer robustness). Aster returned **exit (a), sound as
scoped**. Two additions, both to the **method/implementation record, not canon prose**:

- Normalizer admissibility: a MIP normalizer must be finite and strictly positive on every candidate
  cut. Zero, negative, or infinite normalizers are inadmissible — they make the objective undefined or
  reverse its ordering.
- Same-object continuity: the continuity claim belongs to the *same normalized objective used for
  selection*. If a normalized selector picks the cut but an unnormalized mutual information is then
  reported, the reported value can jump at the normalized crossing.

One wording scope, in canon prose: "the value barely moves" is a description of the deposited ramp, not
a theorem. Equality at a crossing guarantees no jump; it does not guarantee a small slope over a finite
coupling step. Scope the phrase accordingly.

**D. P1-7 — NEW THIS ROUND, log it as new.** §13a currently reads "no single **fixed partition** scores
a window straddling the relabel." The claim is correct, but it uses "fixed partition" in the
*time-invariant* sense, which collides with the sense §4 has just retired. Change to "no single
**time-invariant** partition scores a window straddling the relabel." Same claim; removes the
collision. This is a new edit, not part of the reviewed set — **it must appear in the changelog as
such.** Unlogged edits are the defect that sank the ASTER master; do not repeat it.

**E. P2-1, P2-2, P2-3, P2-4, P2-6.** Unchanged. Five of the six Figure MW propagation sites.

**F. P2-5 — REPLACED with a subtractive edit. This is the change from the prior package.**

Do **not** fold the rewritten P2-5 from the verdict response. Its stated obstacle ("unresolved whether
the mask's well-defined and informative regions overlap at all") is **false** — the regions overlap, and
they overlap *necessarily* on the declared weak-coupling family. Prime and the outside critic
independently confirmed the spectator edge's viability effect vanishes strictly faster than the load
edge's as coupling → 0, so the intersection cannot be empty on any sweep including weak coupling.

Fold instead a **subtractive** edit that removes the overclaim without asserting a replacement:

- **Strike** "This has now been done" and the entire coupled-Gaussian discharge passage that follows it.
- **Strike** the unqualified "That range is the framework's characteristic measurable"; replace
  "characteristic measurable" with "**proposed** characteristic measurable," consistent with P2-1.
- **Restore** the standing deliverable named in v1.20 — the mask computed on a well-posed part-partition
  — to **open**, in the §13 open-items list.
- **Say nothing** about why, nothing about the K4 salvage diagnostic, nothing about verification status.

The reason this is severable: removing a false statement does not require knowing the true one. What
eventually fills this gap is decided by the v1.23 regrade.

**G. P3-1, P3-2, P3-3.** Unchanged. Append-only revert; restore the v1.21 changelog entry byte-exact;
strip the PROPOSED banner only at placement.

---

## OPTIONAL — requires Ben's explicit yes, otherwise defer

Aster established that Φ_MIP zero-calibration is exactly zero for **every admissible normalizer**, not
merely across the normalizers tested: on a block-decomposable covariance at least one cut has numerator
zero, and mutual information is non-negative, so the minimum is exactly zero for any finite strictly
positive normalizer. That is a genuine strengthening and it is proved, not asserted.

It is also an addition beyond the reviewed set, in a release whose purpose is a retraction. **Do not
fold it on your own initiative.** If Ben says yes, log it as an explicit edit with OLD/NEW. If not, it
goes to v1.23 with the regrade.

---

## DO NOT FOLD

- The mask-salvage regrade in any form.
- Any disposition of the K4 salvage diagnostic. It is a **different computation** from E17 (outside
  critic, cold identity read). Their caveats cannot be transferred by identity, and no sentence in this
  fold may treat them as one object.
- The Task 3 retroactive hardening ledger. Separate workstream, separate change run.
- Anything arising from the `mask_salvage.py` predicate/code mismatch.

---

## Fold procedure

Base is `AOP_CANON_MASTER_v1.22_PROPOSED_ASTER.md`. Slice each OLD span from **that proposed master** —
the OLD spans are v1.22-only text and do not exist in v1.21. Assert each replacement matches exactly
once. Diff to confirm only intended regions moved. The **only** content taken from the live v1.21 master
is the frozen v1.21 changelog entry, restored byte-exact for P3-1.

Every changed line must map to a logged edit. Deliver `AOP_CANON_MASTER_v1.22.md` to Ben for manual
placement — do not write a file of that size via the create-file path, and do not overwrite the live
v1.21 master.

---

## Deposit to Drive

Three artifacts from this session exist only as local uploads and are not in the folder. Per the
charter, they do not count until they are:

- `AOP_v1.22_DecisionPackage_20260722.md`
- `AOP_v1.22_VerdictResponse_20260722.md`
- `REV_Aster_AOP_ForcedResult_Audit_20260722.md`

The outside critic could not locate the first two during its audit and correctly declined to attribute
any conclusion to them. Deposit all three.

---

## Changelog requirements

The v1.22 entry must state, explicitly:

1. What folded (retraction, coherence, §4 re-scope, MW propagation, append-only revert).
2. That P1-7 is new this round and was not in the reviewed change set.
3. That the §13 mask passage was **struck**, not rewritten, and the v1.20 standing deliverable is
   **returned to open**.
4. That the mask-salvage regrade, the E17/K4 disposition, and the retroactive hardening ledger are
   **deferred to v1.23** — named, so nobody later reads v1.22 as a completed pass.

---

## Boundary with the parallel workstream

Claude Science is working the mask-salvage computations in parallel under a separate order. **You touch
the masters; CS touches nothing in the canon folder.** The artifacts are disjoint by design. Do not
execute any part of the CS order, and do not fold any CS output — it arrives as a proposal and goes
through Prime first.
