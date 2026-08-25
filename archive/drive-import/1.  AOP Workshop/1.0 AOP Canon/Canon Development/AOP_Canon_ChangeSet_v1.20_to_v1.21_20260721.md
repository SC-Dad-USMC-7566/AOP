# AOP Canon — Proposed Change Set v1.20 → v1.21 (red-team corrections)

**Prepared by Prime, 21 July 2026.** Folds the three low-hanging corrections surfaced by Aster's
red-team (`AOP_RedTeam_v1.20_20260721.md`) and reviewed in `AOP_Prime_RedTeam_Review_20260721.md`.
All three are honesty edits — a claim is de-scoped or re-graded, none strengthened, none new science.
D4 (the paired stellar counterfactual) is **parked as a declared open item**, not built.

**Status: NOT READY TO FOLD.** D1 final. D3 final pending a location confirm. **D2 provisional** —
awaiting (a) the arXiv:2410.13375 line-check and (b) Aster's confirmation that the regrade lands the
objection. Canon moves in one deliberate run; this batch folds only when all three are green.

OLD blocks are quoted from the v1.20 folded text; whoever folds confirms the exact string against
`AOP_CANON_MASTER_v1.20.md` and maps markdown escaping (standard practice).

---

## D1 · §12 Table 4 "Current → lifetime" cell — de-scope the star claim [FINAL]

The v1.20 cell asserts a *mechanism* for the star ("lengthens lifetime through the forced Boundary and
Memory edges and a present dynamical restoring force"). Aster F1, concurred: E7 shows the theorem is
out of scope for the star; it does not show fusion lengthens stellar lifetime, or by what mechanism.
Out-of-scope is not a positive sign. Downgrade to honest.

**OLD (tail of the cell):** "A drive that appears to *lengthen* lifetime — a star's fusion — does not contradict this: fusion is not a measure-preserving current at fixed stationary distribution, it **reshapes the stationary state** (composition, energy content, the hydrostatic profile), so the theorem does not bind it; such a drive lengthens lifetime through the forced Boundary and Memory edges and a present dynamical restoring force (the negative-specific-heat thermostat, §11a), not through the measure-preserving lever. What Drive forces directly under the lifetime primitive is a change in lifetime; for a genuine measure-preserving current the direction is settled and downward. Generalization to finite noise, and the classification of drives that reshape the stationary state, remain open."

**NEW:** "A drive that *appears* to lengthen lifetime — a star's fusion — does not contradict this theorem, because fusion is not a measure-preserving current at fixed stationary distribution: it reshapes the stationary state (composition, energy content, the hydrostatic profile), so the theorem is out of scope. But out-of-scope is not a positive result. Whether fusion actually lengthens a star's AOP lifetime is **not established here**, and is a declared open item (§13 open problems): establishing it would require a declared intervention on nuclear energy generation, a declared AOP exit set — loss of hydrostatic equilibrium, departure from the main sequence, fuel exhaustion, and cessation of luminous fusion are *distinct* first-passage events — and a paired stellar-evolution counterfactual exhibiting a longer first-passage time under that intervention. Absent that, the star establishes only that the measure-preserving theorem does not bind it, not the sign of the effect. What Drive forces directly under the lifetime primitive is a change in lifetime; for a genuine measure-preserving current the direction is settled and downward. Generalization to finite noise, and the classification of drives that reshape the stationary state, remain open."

**WHY:** removes an undemonstrated mechanism; states the exact evidence a positive claim would need
(Aster's settling condition); points at the parked open item. **[honesty downgrade; no new science.]**

**Companion (D1b):** add to the §13 open-problems / frontier register a one-line declared item:
"**Stellar positive-persistence mechanism [FRONTIER, parked].** Whether fusion lengthens a star's AOP
lifetime, and by what mediation, is open pending a declared intervention + exit set + paired
counterfactual (see §12, Current→lifetime)."

---

## D2 · §4 "Drive → Integration" edge — regrade tendency → necessity/cost [PROVISIONAL]

Aster F2, concurred (sharpest catch): two independent defects. (a) the load-bearing citation
arXiv:2410.13375 is still `[Authors TBD]` and unaudited; (b) even granting it verbatim, it supports
I⇒needs-D (a necessity) and a cost bound — **not** D⇒I (a tendency). "Requires" is not "produces";
"must be paid for" is not "promoted by payment." The canon's own hedge already concedes (b).

**OLD:** "Drive → Integration is free at equilibrium and, over time, a conditional tendency — not a forced edge. Parts can be correlated at zero dissipation; integration exists statically for free. Dynamically, drive is a *precondition* for a strong form of maintained integration but does not *force* it: robust, size-extensive multipartite correlation cannot be sustained in thermal equilibrium and requires far-from-equilibrium, time-dependent (limit-cycle) dynamics [necessity result, 'Dissipation enables robust extensive scaling of multipartite correlations,' arXiv:2410.13375 (2024)], and maintaining correlation against thermal erasure carries a dissipative cost [Parrondo, Horowitz & Sagawa 2015] — so drive must pay for integration but does not automatically purchase it, and dissipation can equally destroy correlation. Claims that drive *maximizes* integration (maximum entropy production, not a settled principle) or generically *builds* it (strong readings of dissipative adaptation) are not relied on here. Conflating 'integration exists for free' with 'drive made this integration' remains an error."

**NEW (provisional):** "Drive → Integration is free at equilibrium and, over time, a **necessity/cost constraint with direction I→D — not a D→I tendency, and not a forced edge**. Parts can be correlated at zero dissipation; integration exists statically for free. Dynamically, the supported direction runs from integration to drive: a strong form of maintained integration *requires* drive — robust, size-extensive multipartite correlation cannot be sustained in thermal equilibrium and requires far-from-equilibrium, time-dependent (limit-cycle) dynamics [necessity result, 'Dissipation enables robust extensive scaling of multipartite correlations,' arXiv:2410.13375 (2024) — ⚠ theorem statement, definition of 'robust', and author list pending line-check] — and maintaining correlation against thermal erasure carries a dissipative cost [Parrondo, Horowitz & Sagawa 2015]. Together these establish that integration *demands* drive (a necessity) and that correlation *must be paid for* (a cost). They do **not** establish that drive *tends to build* integration: 'requires' is not 'produces,' 'must be paid for' is not 'promoted by payment,' and dissipation can equally destroy correlation. Claims that drive *maximizes* integration (maximum entropy production, not a settled principle) or generically *builds* it (strong readings of dissipative adaptation) are not relied on here. A genuine D→I tendency would require separate directional-intervention evidence — a declared ensemble in which raising drive raises integration — which the necessity/cost results cannot supply. 'Integration exists for free,' 'integration requires drive,' and 'drive made this integration' are three distinct claims; conflating any two is an error."

**Table 2 D→I row tag:** "cited tendency" → "necessity/cost (I→D); D→I tendency unproven".

**WHY:** corrects the direction of inference and flags the unaudited citation inline. **[honesty
re-grade.]** Provisional until the line-check returns and Aster confirms the regrade addresses F2.

---

## D3 · The "1 of 15 / one genuine new work" score — honest, disposition-typed count [FINAL pending location]

Aster F3, concurred on substance: the single fraction is a workload estimate, not a referee closure
count. It lumps heterogeneous dispositions (defect-correction, citation-lead, lemma-to-write,
measure-port, worked-case computation, proxy-with-residual) as if each were a closed gap.

**Location note (verify before applying):** this score lives in the **planning docs** — the gap plan
(`AOP_FourAxis_Deepening_and_GapPlan_v1.md`, §0 and §4) and `AOP_FourAxis_Combined_Report.md` — **not,
on present evidence, in the canon master** (the canon carries per-claim SETTLED/SYNTHESIS/FRONTIER
grades, not a closure tally). So D3 is most likely a planning-doc correction with **zero canon
footprint**. Confirm no "1 of 15"–type tally exists in `AOP_CANON_MASTER_v1.20.md` before treating this
as closed; if one does, it gets the same rewrite.

**OLD (gap-plan style):** "of 15 rows, **1 is genuine new work** … Six close by citation, five by synthesis/edit, three are small closed-form computations that apply settled machinery."

**NEW:** "The 15 rows carry **distinct dispositions**, which a single closure fraction obscures. Typed honestly: genuinely open / new work — **≥2** (the time-extended moving-MIP, and the stellar positive-persistence mechanism surfaced by the v1.20 red-team); closed generally — the demonstrable defect-corrections and the algebraic nesting identity; closed within a named model only — the worked computations (a worked case is not the general edge); citation-lead not yet closure — rows whose cited proposition, assumptions, and target observable have not been shown to match the canon claim (screening↔conditional-independence; the star half of Drive→lifetime; critical Φ_MIP; the D→I necessity/cost edge); lemma-to-write — the full sector-split no-cross-coupling claim; proxy-with-admitted-residual — off-stationarity Memory. This is a **workload estimate for the team, not a referee-facing closure count**: 'we know what literature or computation to invoke' is not 'the scientific gap is closed.'"

**WHY:** replaces a misleading single number with an honest typed breakdown; states the score's true
purpose. **[honesty re-grade; planning-doc.]**

---

## Dispatched alongside this changeset
- **Claude Science (side-order, do not interrupt moving-MIP):** line-check arXiv:2410.13375 — full author
  list + title (OpenAlex ok for metadata), and the **theorem statement + definition of 'robust' from the
  full text** (OpenAlex cannot supply this; read the primary). Report which of E10's four dependent
  commitments the theorem actually supports. Gates D2.
- **Aster (OAI):** one confirmation pass on the D2 NEW text — does the necessity/cost regrade land F2, or
  does it still overreach? Gates D2.

## Fold gate
D1 + D1b: ready. D3: ready pending the canon-master location check (Prime, at fold). D2: hold for
line-check + Aster confirm. When all green, Prime assembles the apply-ready v1.21 fold, byte-confirms
against the master, and brings it to Ben for sign-off. Nothing folds before then.

## Parked (Ben's decision, 21 Jul)
**D4 — paired stellar counterfactual: PARKED, noted for return.** Recorded as the §13 declared open item
via D1b. Not commissioned. Revisit when the moving-MIP build clears.
