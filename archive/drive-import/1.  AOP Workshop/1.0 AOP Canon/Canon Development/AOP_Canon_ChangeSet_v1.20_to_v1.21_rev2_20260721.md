# AOP Canon — Proposed Change Set v1.20 → v1.21 (rev2)

**Prepared by Prime, 21 July 2026.** Supersedes rev1 (`AOP_Canon_ChangeSet_v1.20_to_v1.21_20260721.md`,
id `1woW06pILyhyYhbWyNBpNNAteBJvImeyq` — archive it). Changes in rev2: **D2 revised to v3** after Aster's
yellow-gate pass (four scope defects, all conceded); the arXiv:2410.13375 citation **line-checked,
resolved, and upgraded** to the published PRL. D1, D1b, D3 unchanged from rev1.

**Status:** D1 + D1b + D3 ready. **D2 (v3): line-check CLOSED; awaiting one final Aster confirm** (last
pass found real defects, so one more cheap pass before fold). D4 parked. Fold as one run when D2 is green;
Prime byte-confirms against the master at fold.

Citation resolved this session (independent web verification, not on the critic's word):
**Ptaszyński K & Esposito M, "Dissipation enables robust extensive scaling of multipartite correlations,"
Phys. Rev. Lett. 135, 057401 (2025); arXiv:2410.13375 (v3, 26 May 2025).** Authors/venue confirmed;
abstract-level scope confirmed (permutation-invariant discrete-state units; "robust" = survives
arbitrarily small dynamics perturbations; time-dependent attractors with limit cycles as an example;
core result = feasibility/necessary-condition, "robust extensive scaling cannot occur at equilibrium").
Full-text theorem line-check (proposition numbers) still worth doing before journal submission, but the
scope needed for the regrade is confirmed.

---

## D1 · §12 Table 4 "Current → lifetime" cell — de-scope the star claim [FINAL]

**OLD (tail of the cell):** "A drive that appears to *lengthen* lifetime — a star's fusion — does not contradict this: fusion is not a measure-preserving current at fixed stationary distribution, it **reshapes the stationary state** (composition, energy content, the hydrostatic profile), so the theorem does not bind it; such a drive lengthens lifetime through the forced Boundary and Memory edges and a present dynamical restoring force (the negative-specific-heat thermostat, §11a), not through the measure-preserving lever. What Drive forces directly under the lifetime primitive is a change in lifetime; for a genuine measure-preserving current the direction is settled and downward. Generalization to finite noise, and the classification of drives that reshape the stationary state, remain open."

**NEW:** "A drive that *appears* to lengthen lifetime — a star's fusion — does not contradict this theorem, because fusion is not a measure-preserving current at fixed stationary distribution: it reshapes the stationary state (composition, energy content, the hydrostatic profile), so the theorem is out of scope. But out-of-scope is not a positive result. Whether fusion actually lengthens a star's AOP lifetime is **not established here**, and is a declared open item (§13 open problems): establishing it would require a declared intervention on nuclear energy generation, a declared AOP exit set — loss of hydrostatic equilibrium, departure from the main sequence, fuel exhaustion, and cessation of luminous fusion are *distinct* first-passage events — and a paired stellar-evolution counterfactual exhibiting a longer first-passage time under that intervention. Absent that, the star establishes only that the measure-preserving theorem does not bind it, not the sign of the effect. What Drive forces directly under the lifetime primitive is a change in lifetime; for a genuine measure-preserving current the direction is settled and downward. Generalization to finite noise, and the classification of drives that reshape the stationary state, remain open."

**WHY:** removes an undemonstrated mechanism; states the exact evidence a positive claim would need;
points at the parked open item. **[honesty downgrade; no new science.]**

**D1b:** add to §13 open-problems: "**Stellar positive-persistence mechanism [FRONTIER, parked].**
Whether fusion lengthens a star's AOP lifetime, and by what mediation, is open pending a declared
intervention + exit set + paired counterfactual (see §12, Current→lifetime)."

---

## D2 · §4 "Drive → Integration" edge — feasibility constraint, not an arrow [v3 — awaiting final Aster confirm]

Rev1's v2 landed the headline (withdrew the D→I tendency) but carried four scope defects Aster flagged,
all conceded: (1) generalized the scoped theorem to "integration demands drive"; (2) "direction I→D"
re-introduced an arrow the evidence doesn't support; (3) "correlation must be paid for" over-read a
protocol-dependent cost; (4) "limit-cycle" too narrow, "robust" undefined. v3 fixes all four.

**OLD:** "Drive → Integration is free at equilibrium and, over time, a conditional tendency — not a forced edge. Parts can be correlated at zero dissipation; integration exists statically for free. Dynamically, drive is a *precondition* for a strong form of maintained integration but does not *force* it: robust, size-extensive multipartite correlation cannot be sustained in thermal equilibrium and requires far-from-equilibrium, time-dependent (limit-cycle) dynamics [necessity result, 'Dissipation enables robust extensive scaling of multipartite correlations,' arXiv:2410.13375 (2024)], and maintaining correlation against thermal erasure carries a dissipative cost [Parrondo, Horowitz & Sagawa 2015] — so drive must pay for integration but does not automatically purchase it, and dissipation can equally destroy correlation. Claims that drive *maximizes* integration (maximum entropy production, not a settled principle) or generically *builds* it (strong readings of dissipative adaptation) are not relied on here. Conflating 'integration exists for free' with 'drive made this integration' remains an error."

**NEW (v3):** "Drive → Integration is free at equilibrium and, over time, a **feasibility (necessary-condition) constraint — not a causal or tendency edge in either direction, and in particular not a D→I tendency**. Parts can be correlated at zero dissipation; integration exists statically for free. The one dynamical result established is narrow: for classical discrete-state units on a permutation-invariant network, *robust extensive scaling* of stationary multipartite correlation — where 'robust' means the extensive scaling survives arbitrarily small perturbations of the dynamics — cannot occur in thermal equilibrium, and arises only when the system relaxes to a time-dependent attractor (e.g. a limit cycle, or certain chaotic attractors), which exists only far from equilibrium [Ptaszyński & Esposito, *Phys. Rev. Lett.* 135, 057401 (2025); arXiv:2410.13375]. This is a feasibility constraint on that specific quantity in that model class: robust extensive multipartite correlation is *infeasible without* dissipation. It does **not** establish that drive tends to build integration, nor a general 'integration requires drive' — the paper explicitly leaves generalization beyond permutation-invariant systems open, and its quantity is stationary multipartite mutual information, not AOP Integration at large. Separately, creating, transforming, or continuously stabilizing correlations against erasure carries a thermodynamic cost *under the relevant protocol* [Parrondo, Horowitz & Sagawa 2015] — protocol-dependent bookkeeping, not a claim that every correlation must be continuously paid for; equilibrium correlations are the standing counterexample. 'Requires' is not 'produces,' 'must be paid for' is not 'promoted by payment,' and dissipation can equally destroy correlation. Claims that drive *maximizes* integration (maximum entropy production, not a settled principle) or generically *builds* it (strong readings of dissipative adaptation) are not relied on here. A genuine D→I tendency would require separate directional-intervention evidence — a declared ensemble in which raising drive raises integration — which neither the feasibility constraint nor the cost bound supplies. 'Integration exists for free,' 'robust extensive integration is infeasible without drive,' and 'drive made this integration' are three distinct claims; conflating any two is an error."

**Table 2 D→I row tag:** "cited tendency" → "feasibility constraint (robust extensive I* infeasible without D; model-scoped); no D→I tendency; no causal arrow".

**WHY:** states exactly what the (now published, line-checked) result supports and nothing more; removes
the arrow entirely. **[honesty re-grade.]**

---

## D3 · The "1 of 15 / one genuine new work" score — honest, disposition-typed count [FINAL pending location]

*(Unchanged from rev1.)* Location note: this score lives in the planning docs (gap plan §0/§4;
`AOP_FourAxis_Combined_Report.md`), **not, on present evidence, in the canon master** — confirm no such
tally exists in `AOP_CANON_MASTER_v1.20.md` at fold; likely zero canon footprint.

**OLD (gap-plan style):** "of 15 rows, **1 is genuine new work** … Six close by citation, five by synthesis/edit, three are small closed-form computations that apply settled machinery."

**NEW:** "The 15 rows carry **distinct dispositions**, which a single closure fraction obscures. Typed honestly: genuinely open / new work — **≥2** (the time-extended moving-MIP, and the stellar positive-persistence mechanism surfaced by the v1.20 red-team); closed generally — the demonstrable defect-corrections and the algebraic nesting identity; closed within a named model only — the worked computations (a worked case is not the general edge); citation-lead not yet closure — rows whose cited proposition, assumptions, and target observable have not been shown to match the canon claim (screening↔conditional-independence; the star half of Drive→lifetime; critical Φ_MIP; the D→I feasibility edge); lemma-to-write — the full sector-split no-cross-coupling claim; proxy-with-admitted-residual — off-stationarity Memory. This is a **workload estimate for the team, not a referee-facing closure count**: 'we know what literature or computation to invoke' is not 'the scientific gap is closed.'"

**WHY:** replaces a misleading single number with an honest typed breakdown. **[honesty re-grade; planning-doc.]**

---

## Fold gate
D1 + D1b + D3: ready. D2 (v3): line-check closed; **one final Aster confirm pending**. When green, Prime
assembles the apply-ready v1.21 fold, byte-confirms against the master, brings to Ben for sign-off.

## Dispatch status
- **Claude Science line-check: CANCELLED (redundant).** Prime line-checked 2410.13375 this session; Science
  stays on the moving-MIP.
- **Aster: one confirm pass on D2 v3.**

## Parked
**D4 — paired stellar counterfactual: PARKED**, recorded as the §13 open item via D1b. Not commissioned.
