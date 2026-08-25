# TASK — Aster deposit retrieval, blocker staleness triage, Integration kill-check

**Order ID:** `TASK_CW_AOP_Aster_Triage_20260725`
**Issued:** 25 July 2026 · chat seat (prime), for Ben's sign-off
**Seat:** Claude Cowork (execution)

---

## 0. Standing constraints

You built v1.26. You therefore **do not verify v1.26** under this order — that pass goes to a clean
seat. Nothing here asks you to judge whether your own build was correct.

You have read the sporulation answer key. §3 is written so that contamination cuts the safe way; do
not exceed its scope.

Phase B remains not begun. No answer key. No new candidate systems.

---

## 1. Retrieve the canonical Aster deposit (do this first)

What reached Ben is **four overlapping drafts concatenated**, citing **two different Google Doc IDs**
(`1oawXoCYujOq3rne3Kn--dZ8wVbugzbdYA3GYPbVHGSE` and `1iDHZqXgluuTVq7fD24OEOYmkya3XID2KT7Nr382_mKc`)
with dead `sandbox:` links. That artifact is not adjudicable.

**Task 1.1.** Locate the folder `1.2 AOP Reviews [OAI]`. List its contents with IDs, sizes, and
modified times.

**Task 1.2.** Identify the single canonical review deposit
(`REV_Aster_AOP_v1.25_Adversarial_RedTeam_v1_0_20260724`, Markdown preferred over Google Doc).
Download it, report **byte count, md5, sha256, and line count**, and state the claimed word count
against the actual.

**Task 1.3.** Report whether the two Doc IDs are the same content, different drafts, or one is a
duplicate. If multiple non-identical copies exist, say which is authoritative and on what basis —
do **not** delete or merge anything.

**Halt condition:** if no single complete deposit exists, stop and report. Do not reconstruct the
report from the concatenated chat text.

---

## 2. Blocker staleness triage (mechanical, no judgement)

Aster reviewed **v1.25**. The canon is at **v1.26**, which cut the physics block and recast Φ_MIP.
Several blockers may already be answered. Your job is to establish **which text still exists**, not
whether Aster is right.

Inputs: canonical Aster deposit (§1); `AOP_CANON_MASTER_v1.26.md` `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn`
(md5 `54ceb3772e29f25c6e139b703d550d59`); change set
`AOP_ChangeSet_v1.25_to_v1.26_RedTeamRemediation.md` `1mI3DkOKD_GOJzf-ImDThA1oSsRo4iEMd`;
v1.25 `13tI48fz-l5DundXuyQysPJf7JrSS9xck` (md5 `9c172e015f4adfc9fe827a42687ca2e7`).

**Task 2.1.** For each of the seven blockers, extract every **specific textual target** Aster names —
quoted phrases, section numbers, the "new definition" wording, the 1,443-word masthead figure, the
named archetype placements.

**Task 2.2.** For each target, determine by **text matching against v1.26**:

| Verdict | Meaning |
|---|---|
| LIVE | text present in v1.26 substantially as Aster quotes it |
| STALE | text removed or materially changed by v1.25→v1.26 |
| PARTIAL | some targets live, some stale — enumerate both |
| NOT-FOUND | Aster's quoted text is absent from v1.25 as well (report immediately; this would be a red-team accuracy problem) |

Cite line numbers in both versions. Where a target is STALE, name the change-set edit that removed it.

**Task 2.3.** Produce a one-page triage table: blocker → verdict → surviving targets → change-set
edit if stale. **No recommendations.** Do not assess whether Aster's criticisms are correct; that is
prime and Ben's adjudication.

**Note for calibration, not for you to act on:** blocker 2 (the Drive→Memory theorem) has already
been adjudicated by prime and is LIVE regardless of what text-matching returns — the counterexample
is analytic and version-independent. Do not re-litigate it; just report its textual status.

---

## 3. Integration vs Rival P — one-way kill check

Claude Science's Step 0 established that AOP's axes are **not** computable on topology alone: Drive is
identically zero at detailed balance for every graph, and Memory is undefined without a declared
process. **This section does not resurrect the desk-based discrimination check.** It runs exactly one
narrow question that Step 0 showed is well-posed without rates.

Integration computes in closed form on topology plus a partition via the canon's Σ = (I + gL)⁻¹
construction. Rival P (predict near-WT if ≥1 directed path from a surviving kinase to Spo0A remains;
collapse if zero paths remain) is a functional of connectivity. Both are functionals of the same
graph.

**Task 3.1.** On the published phosphorelay wiring (KinA/KinB/KinC → Spo0F → Spo0B → Spo0A, with
phosphatase drains), compute the canon's Integration measure for each perturbation in
`AOP_Benchmark_Sporulation_Conditions_REDACTED_v0.1.md`. Declare the partition explicitly and state
the coupling constant g and its sensitivity.

**Task 3.2.** Compute Rival P's label for the same conditions.

**Task 3.3.** Report whether the two **can** differ on any condition, and on which.

**Read the asymmetry before interpreting your result.** This test is decisive in one direction only:

- **If they cannot differ** — that is a real kill signal. AOP's only topology-computable axis is a
  relabelling of path-counting on this system, and the benchmark's discriminating power has to come
  from somewhere else or not at all. Report it plainly.
- **If they do differ** — this establishes **nothing** in AOP's favour. One axis is not the
  prediction; per Step 0 the prediction is a three-place semantic weight requiring a declared viable
  set and V, and the wiring supplies neither. A positive result here must be reported as
  *not-killed*, **not** as *discriminates*.

You know the sporulation outcomes, which biases you toward wanting the benchmark to survive — i.e.
toward the "they differ" branch. That is why only the negative branch is being treated as
informative. Do not soften a negative.

---

## 4. Deliverables

To Canon Development (`1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`), byte-verified, hashes reported:

- `AOP_Aster_Deposit_RetrievalNote_v0.1.md` (§1)
- `AOP_Aster_BlockerStaleness_Triage_v0.1.md` (§2)
- `AOP_Integration_vs_RivalP_KillCheck_v0.1.md` (§3), with code deposited alongside

## 5. What not to do

- Do not verify v1.26. Not your build to bless.
- Do not adjudicate any blocker, or repair any canon text.
- Do not re-attempt the Drive→Memory proof; prime has adjudicated the counterexample and the repaired
  re-proof is assigned to a clean seat.
- Do not treat a §3 "they differ" result as a green light.
- Do not grade your own output.
