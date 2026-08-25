# AOP Canon — v1.18 Change Log (OAI maximal re-architecture)

**What this is.** The complete, ordered record of every change from the frozen v1.17 baseline (`FROZEN_aop_canon_v1_17.md`, MD5 `26afc8a8e938…`) to the v1.18 rebuild (`AOP_canon_v1_18_rebuild.md`). The governing discipline for this rebuild is **no silent term migration**: every relabeling, every scoped caveat, every deletion is an entry here with its before/after, so no reader ever finds a v1.17 term quietly replaced by a v1.18 term without a trace. **Compiled:** 17 July 2026.

**Baseline provenance.** v1.18 rebases onto **local v1.17** (the lifetime-primitive spine), not the Drive v1.16 copy, per Ben's ruling of 17 July (see the Frozen Baseline Note addendum). OAI's review was written against v1.16; every P0 target was re-checked against v1.17 text before editing and all six survive the rebase with the same signatures.

**Method.** v1.18 = frozen v1.17 + the surgical edits below + three appended architecture sections. The manuscript text was **edited in place**, not regenerated, precisely so that no prose drifts or is fabricated: the 24,182 words of v1.17 are carried verbatim except at the logged edit points.

---

## P0 stop-ship repairs (six)

**P0-1 — Binding/rest-frame ontological overreach (§10).**
- *Before:* "Binding manufactures a rest frame, and with it a clock…"
- *After:* "Binding is *associated with* a rest frame, and with it a usable clock…" + an inline note that the load-bearing domain criterion is **operational** (coarse-grained subsystem + finite persistence horizon), the relativistic reading is scoped synthesis, and the stronger claim that binding *manufactures* proper time is **withdrawn** (a free excitation is not thereby denied a present tense).
- *Why:* the strong reading was flagged as a phrasing defect in the Claude-compiled P0 Adjudication Matrix (this session's own recommended disposition, graded "minor phrasing defect" — not a completed Ben ruling and not canon) and independently by OAI. The softened operational-criterion reading is applied here as that recommended disposition, **pending Ben's adjudication** — it has not been ruled on. **This is the edit most worth Ben's eyes.**

**P0-2 — Proxy glosses overstate what the quantities measure (abstract + §2 status table).**
- *2a Drive (abstract):* "a free-energy throughput that holds the system off equilibrium (Drive)" → "sustained dissipation — trajectory-level irreversibility — … (Drive, measured as entropy-production rate, **not** free-energy throughput)". σ is dissipation, not throughput.
- *2b Boundary (Table):* "mutual information I(inside;outside)" → framed as a **panel** whose lead proxy measures **statistical dependence across the cut, not separation per se**, with the caveat "the proxy names statistical organization, not a physical membrane."
- *2b Integration (Table):* "mutual information across a partition of components" → "total correlation … **interdependence / shared variance, not proven causal unity**", sign-blind for persistence without the §6 viability-alignment second coordinate; caveat "the proxy names interdependence, not irreducible wholeness."

**P0-3 — "Choice-free" language.** No edit required: 0 occurrences in v1.17 (already removed upstream; the P0 matrix item was stale). Recorded for completeness.

**P0-4 — "Own viability" reads as self-supplied (subtitle + §7/§9a usage).**
- *Before (subtitle):* "a semantic mask read out by a system's own viability".
- *After:* "read out **through a declared viability functional on the system's viable set** (the V slot of the declaration tuple; 'own' denotes the set the functional is evaluated on, not a viability the system possesses or supplies — the framework remains **ownership-free**, §9a)".
- *Why:* preserves the correct PIC-lesson refusal (no ownership) while removing the reading that the system self-supplies its viability criterion. The word "ownership-free / no ownership" (10 occurrences) is **deliberately kept** — it is the refusal, not the defect.

**P0-5 — Fused "Status of claims" column split into two axes (§12).**
- *Before:* single-word statuses ("secure, scoped", "definition + computed", …).
- *After:* an explicit **two-axis scheme** — dependency status {forced / conditionally-forced / dissociable / unidentified} × evidential status {theorem-corollary / definition-stipulated-weld / constructed-counterexample / analytic-model-result / numerical-simulation / random-ensemble-regularity / empirical-observation / conjecture-frontier}. Old single words map to the evidential axis; "scoped"/"static-Gaussian" caveats map to the dependency axis. Each visible row retagged with its [dependency × evidential] pair; the full re-graded ledger appended as **Table 3′ (§12′)**. Load-bearing rule encoded: a passed binding/manipulation check licenses **at most "conditionally forced," never "forced."**

**P0-6 — Version/reference reconciliation.** Handled in the Phase-0 artifacts (Frozen Baseline Note, Issue Registry, Version & Count Reconciliation): 52 reference-list entries; ~26 distinct works cited inline (13 numeric + 13 author-year, whitespace-normalized); README/manifest stale-count divergence resolved (+6 Tier-1 PDFs). The v1.18 masthead does not restate counts; the reconciliation doc is authoritative.

## Additions (new architecture, per ADR-001/002/003)

- **§11b — exactly-solvable non-triviality benchmark.** New section presenting the leaky autocatalytic compartment (36-state CTMC), the strength ⊥ viability dissociation (Spearman −0.67), the Möbius sign inversion, and the honest built-in-vs-discovered boundary. Clears the non-triviality bar, not an adjudication bar.
- **§12′ — Table 3′**, the full claim ledger under both axes (13 claims).
- **§12″ — the declaration tuple D and the measurement panels**, tying the four-panel apparatus and D = (S,E,F,P,δt,τ,R,V,I,N) into the body.
- **Masthead** bumped v1.17 → **v1.18** with a one-paragraph summary of the re-architecture.

## What was NOT changed (guard against silent migration)

- The lifetime primitive, the 5.7× dissociation, §9a, §11a, §4a, the five worked cases' prose, all references, all figures: **carried verbatim from v1.17.** The archetype re-grade lives in a **separate deliverable** (`REV_AOP_Diagnostic_Archetypes_v1_0.md`); it does not overwrite §11's prose, which is only annotated by §11b.
- No reference was added or removed. The 2 print-only books (Ashby 1960, Parfit 1984) remain outstanding (needs Ben).

## Open items carried to Ben

1. **P0-1 wording** — confirm the softened operational-criterion framing is the intended resolution (vs. deleting §10's relativistic paragraphs entirely, which was one earlier option).
2. The 2 print-only book references.
3. Whether v1.18 should now be pushed to Drive as the new canonical version (Drive connector can add but not delete; duplicates accumulate).
