# AOP Canon — Change Log (running master)

**What this is.** A running, append-only ledger of changes to the AOP canon and its
designation. It implements the canon-break discipline: a change is recorded here the moment it
happens, so nothing is lost between deliberate change runs. A small change — a version-pointer
bump, a companion-document addition — does not warrant its own change run; it is logged here and
folded into the next one. The log is what makes deferral safe: a recorded change is not a silent
drift.

**Scope.** This log covers the canon (the paper) and its designation. It does not cover the
charter — charter changes are governance, rare, and handled on their own. It does not restate
canon claims; it records *that* and *how* the canon moved, and points at the version that holds
the detail.

**How it works.**
- Every canon change gets one short entry: what changed, where, why, status (Pending / Reconciled).
- Pending entries wait at the top. A *change run* is a deliberate pass that reconciles them — it
  updates the canon designation, propagates anything downstream (the cross-project bus, if the
  Ladder is affected), and moves the entries to Reconciled with the date.
- Keep it cheap. An entry is a few lines. If logging a change turns into a project, it is
  over-built — cut it back.

**Fixed name.** This is a standing living file, appended continuously; it keeps a fixed name (no
version suffix). *(This file replaces `AOP_ChangeLog_v1.19.md`, which carried a version suffix in
violation of that rule and whose reconciled history stopped at v1.16. The predecessor is being
moved to the Retired folder; renaming to the fixed `AOP_ChangeLog.md` restores the convention.)*

**Baseline & history.** The canon was designated at paper **v1.4**. The full reconciled history
**R1–R10 (v1.4 → v1.16)** lives in the archived predecessor `AOP_ChangeLog_v1.19.md` (Retired folder). That archived file is the authoritative inline record for R1–R10 — nothing there is
deleted, only moved. This running master **continues the ledger from v1.16** with R11 onward.
*(If a single self-contained file carrying R1–R13 inline is wanted, the R1–R10 entries can be
folded back in from the archived copy on request — see the note to Ben in the delivery message.)*

---

## Pending — to fold into the next change run

**External-benchmark correction (§11b scope + §13 falsifier).** *Held, not yet in canon.* The
external *E. coli* / Keio benchmark produced a **T4 falsification**: on real metabolism, flux
strength and viability-importance are **positively** correlated (reproducible Spearman ≈ +0.53),
directly contradicting the toy-model "strength ⟂ viability" dissociation. When Claude Science
delivers the fixed benchmark (deterministic via pFBA; de-circularized answer key scored on
external labels only) **and prime re-verifies the fixed numbers**, one canon edit folds two
matched changes: (1) §11b re-scoped so the toy CTMC strength⊥viability dissociation is stated as
**toy-only, non-generalizing**; (2) the external T4 falsification recorded in the §13 falsifier
ledger. Held deliberately under *no self-grading / verify fixed numbers before canon* — the fix is
not yet on Drive (Task-2 folder still holds only Science's v1.0), so nothing is reconciled yet.

---

## Change run — 19 July 2026 (v1.19, prime verification fix + section reorder)

Folded one canon movement; its entry is Reconciled as **R13** (v1.18→v1.19). The canonical master
is held on Drive as `AOP_CANON_MASTER_v1.19.md`. Section bodies are byte-identical to v1.18 except
at the single logged §11b edit; the rest of this run is a structural reorder.

### R13 · Canon movement: v1.18 → v1.19 — reconciled 19 July 2026
- **What.** (1) Applied one prime-verification finding (v1.18 verification memo): the §11b prose
  that presented the internal CTMC benchmark's anti-ranking (strength⊥viability) and Möbius sign
  inversion as if they *could have come out otherwise* was corrected to a **competence check, not
  a discovery** — those patterns are **forced by construction** (the OR/AND gate topology fixes
  the Möbius inversion; hand-assigned rate constants fix the anti-correlation). The −0.67 Spearman
  value and the Möbius numbers are unchanged; only the epistemic framing was corrected, with a
  pointer added to the still-open external-ground-truth benchmark. (2) Structural reorder to
  monotone section numbering: §11a → §11b → §12 → §12′ → §12″ → §13.
- **Why.** Prime's independent re-run of the v1.18 benchmark showed the self-graded submission
  gate had PASSed item 3.2 ("discovery vs. built-in") when the result is deterministic from the
  construction. The framing fix removes the overclaim without touching any number.
- **Grade.** No promotions. §11b stays **[analytic-model-result; forced-by-construction]**; it
  clears the non-triviality bar, not an adjudication bar.
- **Verification.** Prime verified v1.18 as drift-free (every changed line maps to a logged edit;
  untouched sections byte-identical to v1.17) before applying the §11b framing patch. The reorder
  was checked to leave section bodies byte-identical.
- **Downstream / carried.** The **external** T4 falsification is *not* part of v1.19 — it is the
  Pending item above, held for Science's fixed benchmark plus prime re-verify. No Ladder
  propagation from this run.
- **Status.** Reconciled 19 July 2026. Canonical master on Drive (`AOP_CANON_MASTER_v1.19.md`).

---

## Change run — 17 July 2026 (v1.18, OAI maximal re-architecture)

Folded one canon movement; its entry is Reconciled as **R12** (v1.17→v1.18). v1.18 = frozen v1.17
edited **in place** (24,182 words carried verbatim except at logged edit points) plus three
appended architecture sections. Governing discipline: **no silent term migration** — every
relabeling, scoped caveat, and deletion is a logged before/after. Per-run detail:
`AOP_canon_v1_18_changelog.md` (v1.18 re-architecture folder).

### R12 · Canon movement: v1.17 → v1.18 — reconciled 17 July 2026
- **What — six P0 stop-ship repairs.**
  - **P0-1 (binding / rest-frame overreach, §10).** "Binding *manufactures* a rest frame … a
    clock" → "Binding is *associated with* a rest frame … a usable clock"; the stronger claim that
    binding *manufactures* proper time is **withdrawn**. Load-bearing-domain criterion recast as
    **operational** (coarse-grained subsystem + finite persistence horizon); relativistic reading
    scoped as synthesis. **Still pending Ben's adjudication** — OAI called this P0 stop-ship; the
    Claude P0 matrix downgraded it to a minor phrasing defect; neither the severity nor this
    wording has been ruled on. *This is the edit most worth Ben's eyes.*
  - **P0-2 (proxy glosses overstate what quantities measure, abstract + §2 status table).**
    Drive: "free-energy throughput" → **sustained dissipation / entropy-production rate** (σ is
    dissipation, not throughput). Boundary: mutual information I(inside;outside) reframed as a
    **panel** measuring statistical dependence across the cut, "not a physical membrane."
    Integration: "mutual information across a partition" → **total correlation / interdependence,
    not proven causal unity**, "not irreducible wholeness."
  - **P0-3 ("choice-free" language).** No-op: 0 occurrences in v1.17 (already removed upstream;
    the matrix item was stale). Recorded for completeness.
  - **P0-4 ("own viability" reads as self-supplied, subtitle + §7/§9a).** "a semantic mask read
    out by a system's *own viability*" → read out **through a declared viability functional on the
    system's viable set** ('own' = the set the functional is evaluated on, not a viability the
    system possesses or supplies; framework stays **ownership-free**). The "ownership-free /
    no-ownership" refusal (10 occurrences) is **deliberately kept** — it is the refusal, not the
    defect.
  - **P0-5 (fused "Status of claims" column, §12).** Split into an explicit **two-axis scheme** —
    dependency status {forced / conditionally-forced / dissociable / unidentified} × evidential
    status {theorem-corollary / definition-stipulated-weld / constructed-counterexample /
    analytic-model-result / numerical-simulation / random-ensemble-regularity /
    empirical-observation / conjecture-frontier}. Full re-graded ledger appended as **Table 3′
    (§12′)**. Rule encoded: a passed binding/manipulation check licenses at most
    "conditionally-forced," never "forced."
  - **P0-6 (version / reference reconciliation).** 52 reference-list entries; ~26 distinct works
    cited inline (13 numeric + 13 author-year); +6 Tier-1 PDFs; stale-count divergence resolved.
    The reconciliation doc is authoritative; the masthead does not restate counts.
- **What — three appended architecture sections.** **§11b** exactly-solvable non-triviality
  benchmark (36-state leaky autocatalytic CTMC; strength⊥viability Spearman −0.67; Möbius sign
  inversion; honest built-in-vs-discovered boundary — clears the non-triviality bar, not an
  adjudication bar). **§12′** Table 3′, the full 13-claim ledger under both axes. **§12″** the
  declaration tuple D = (S,E,F,P,δt,τ,R,V,I,N) and the four measurement panels.
- **Why.** Execute OAI's maximal re-architecture pass against the frozen v1.17 baseline, repairing
  the six stop-ship items and hardening the status apparatus, without regenerating prose.
- **Grade.** No promotions; §11b enters at [analytic-model-result; forced-by-construction] (this
  is what R13 later corrects the framing of). Load-bearing rule: passed check → at most
  "conditionally-forced."
- **Baseline provenance.** v1.18 rebases onto **local v1.17** (the lifetime-primitive spine), not
  the Drive v1.16 copy, per Ben's ruling of 17 July. OAI's review was written against v1.16; every
  P0 target was re-checked against v1.17 text before editing and all six survive the rebase.
- **What was NOT changed (guard against silent migration).** The lifetime primitive, the 5.7×
  dissociation, §9a, §11a, §4a, the five worked cases' prose, all references, all figures: carried
  verbatim from v1.17.
- **Open items carried to Ben.** (1) P0-1 wording (confirm the softened operational-criterion
  framing is the intended resolution vs. deleting §10's relativistic paragraphs). (2) The 2
  print-only book references (Ashby 1960, Parfit 1984) remain outstanding. (3) Whether v1.18/v1.19
  should be pushed to Drive as canonical (connector can add but not delete; duplicates accumulate).
- **Status.** Reconciled 17 July 2026. (Superseded by v1.19; canonical master now
  `AOP_CANON_MASTER_v1.19.md`.)

---

## Change run — 17 July 2026 (v1.17, lifetime-primitive spine — frozen local baseline)

Folded one canon movement; its entry is Reconciled as **R11** (v1.16→v1.17).

### R11 · Canon movement: v1.16 → v1.17 — reconciled 17 July 2026
- **What.** v1.17 established the **lifetime primitive** as the spine of the framework and the
  **5.7× lifetime-vs-occupancy dissociation**, and was frozen as the local rebase baseline
  (`FROZEN_aop_canon_v1_17.md`) that v1.18 edits in place.
- **Why.** Provide a stable, frozen local baseline for the v1.18 re-architecture, so the P0 edits
  are applied to a fixed text rather than a moving one (per Ben's 17 July ruling on rebasing onto
  local v1.17).
- **Status.** Reconciled 17 July 2026; frozen baseline held as `FROZEN_aop_canon_v1_17.md`.
- **⚠ Ledger note (honesty flag).** I did **not** locate a dedicated stand-alone v1.16→v1.17
  change-run document in the folders read this session. This R11 entry is reconstructed at summary
  resolution from the v1.18 changelog's baseline-provenance section and the Frozen Baseline Note
  (v1.16). If a discrete v1.17 changelog exists, it should be located and R11 expanded to match its
  detail; flagged for Ben rather than fabricated.

---

## History R1–R10 (v1.4 → v1.16)

Full inline entries are in the archived predecessor `AOP_ChangeLog_v1.19.md` (Retired folder).
Summary of what that record holds, newest first:

- **R10** — v1.15→v1.16 (15 Jul): new §9a "Individuality at the collective scale: the two-level
  reading"; one status-table row; no reference added or removed, no claim retracted.
- **R9** — v1.14→v1.15 (15 Jul): red-team hardening of the life/individuation fold (five of six
  findings accepted; §11a living-predicate split into *alive* / *viable-pausable*; §9
  higher-individual route demoted to FRONTIER; one primary-source-grounded rejection).
- **R8** — v1.12→v1.14 (9 Jul): persistence→life→individuation fold (§11a living threshold with
  Figure LT; §4a diachronic individuation; §9 clarification), three hard-review corrections applied.
- **R7** — v1.11→v1.12 (9 Jul): individuation GO — Φ_MIP added as a graded, ownership-free
  one-vs-many axis; "no individuation" refusal narrowed to "no ownership" (PIC lesson stands);
  entered Table 4 as the gate ledger's first GO row.
- **R6** — v1.10→v1.11 (8 Jul): cross-brick gate arc — pre-registered search for a forced
  cross-brick coupling; four gates returned scoped nulls, recorded as first-class Table 4 results.
- **R1–R5** — v1.4 → v1.10: see archived file.

*(This section is a pointer, not a re-statement. The archived file remains the authoritative
inline record for R1–R10.)*

---

*Running master. Append pending entries above; reconcile in deliberate change runs; never delete —
a reconciled entry is the record of what moved and when. R1–R10 preserved in the archived
predecessor; this file continues the ledger from v1.16.*
