# AOP Submission Gate — Three-Reviewer Checklist (v1.18)

**Status:** OAI Phase 5 deliverable. A pre-submission gate for the v1.18 Perspective, structured as three named reviewer personas — the ones a Royal Society *Interface Focus* Perspective on this topic would actually draw. Each carries a checklist of the objections most likely to sink the paper, with the current disposition against the v1.18 package. A **PASS** means the objection is answered in the manuscript or a deposited deliverable; a **HOLD** means it needs Ben or a further pass before submission. Non-canonical. **Compiled:** 17 July 2026.

**Package under review:** `AOP_canon_v1_18_rebuild.md` (manuscript), `AOP_canon_v1_18_changelog.md`, `AOP_ADR_001_panel_architecture.md`, the three benchmark docs (spec/prereg/results), `REV_AOP_Operational_Panels_v1_0.md`, `REV_AOP_Diagnostic_Archetypes_v1_0.md`, `REV_AOP_Rival_Adjudication_v1_0.md`, `aop_benchmark_ctmc.py`.

---

## Reviewer 1 — The physicist (stochastic thermodynamics / non-equilibrium)

*Cares about: whether the Drive/dissipation claims are physically correct and whether the benchmark's thermodynamics is sound.*

| # | Checklist item | Disposition |
|---|---|---|
| 1.1 | Is "Drive" a physically defensible quantity, not a metaphor? | **PASS** — entropy-production rate σ, defined as the trajectory time-asymmetry; P0-2a removed the "free-energy throughput" gloss. |
| 1.2 | Is σ>0 ⇒ E>0 stated at the right strength (a floor, not depth; one direction only)? | **PASS** — §12 row is forced × theorem/corollary, converse explicitly fails (detailed-balance oscillator), scope stated. |
| 1.3 | Does the benchmark's NESS have a genuine stationary distribution and σ>0? | **PASS** — reinjecting variant, Σπ=1, σ=1.32; declared split (panels on NESS, viability on absorbing) is stated, not hidden. |
| 1.4 | Is the TUR claim scoped to where it's proven? | **PASS** — conditionally-forced (classical Markov regime), [4],[5]. |
| 1.5 | Detailed-balance negative control behaves correctly? | **PASS** — control C1: ΔV(R)=0 when nothing to suppress. |

## Reviewer 2 — The information theorist / complexity scientist

*Cares about: whether the Memory/Integration proxies mean what they're said to mean, and whether the semantic-mask machinery is well-posed.*

| # | Checklist item | Disposition |
|---|---|---|
| 2.1 | Are mutual information / total correlation over-interpreted as "separation" / "unity"? | **PASS** — P0-2b scopes both: MI = statistical dependence, TC = interdependence not proven unity; both framed as panel proxies. |
| 2.2 | Is the Memory numerator choice (Cμ vs E) principled, not ad hoc? | **PASS** — the spore archetype forces it; §12 gate shows the D→M floor reaches E only. |
| 2.3 | Is the semantic mask ("read out by own viability") free of the ownership defect? | **PASS** — P0-4 scopes "own" to the viable set the functional is evaluated on; framework stays ownership-free. |
| 2.4 | Is the coalition/Möbius analysis correct and reproducible? | **PASS** — full 2⁷ table closed-form; `aop_benchmark_ctmc.py` reproduces h(A,B)=+0.44, h(S1,S2)=−0.12. |
| 2.5 | Does the rival comparison use a real information measure, fairly? | **PASS** — transfer entropy, computed on the identical CTMC; reported as favorable-on-one-system, not adjudication. |

## Reviewer 3 — The skeptic / methodologist (the hardest reviewer)

*Cares about: whether the framework is falsifiable, whether "new" results are actually new, and whether the status labels are honest. This is the reviewer the charter's epistemic mode is written for.*

| # | Checklist item | Disposition |
|---|---|---|
| 3.1 | Is any claim promoted to a theorem it isn't? | **PASS** — two-axis ledger (Table 3′); passed binding check licenses at most "conditionally forced." |
| 3.2 | Is the benchmark's result actually a discovery, or built in? | **PASS** — §11b and the results doc separate built-in (redundancy/synergy classes) from could-have-failed (strength⊥viability, Möbius sign inversion, substitutability). |
| 3.3 | Is the benchmark preregistered, or post-hoc rationalized? | **HOLD (disclosed)** — prereg exists with falsifying outcomes, but candidly notes single-session execution validated the model before the prereg was written; tuning set only the metastable regime, not the verdicts. Honest, but a reviewer may still dock it — worth Ben's call on whether to re-run truly blind. |
| 3.4 | Is the rest-frame / domain-wall claim overreaching (theory-of-everything smell)? | **HOLD** — P0-1 softens "manufactures a rest frame" to an operational criterion and withdraws the "manufactures proper time" phrasing; **Ben should confirm** this is the intended resolution vs. cutting §10's relativistic paragraphs. |
| 3.5 | Are all references verified against primary sources? | **HOLD** — punchlist authoritative: 31 verified-in-body, 14 abstract-verified, 5 record-only, 2 needs-user-PDF (Ashby 1960, Parfit 1984 — print-only). The 5 record-only are not submission-ready under the charter standard. |
| 3.6 | Is there silent term migration between versions? | **PASS** — v1.18 change log records every relabel with before/after and a "what was NOT changed" guard. |
| 3.7 | Does the framework overclaim novelty? | **PASS** — the "don't create when you can cite" posture is visible; claims tied to named results; the benchmark clears a non-triviality bar, explicitly not adjudication. |

---

## Gate summary

- **PASS: 14 of 17 items** (Reviewer 1: 5/5; Reviewer 2: 5/5; Reviewer 3: 4/7). The physics (Reviewer 1) and information-theory (Reviewer 2) checklists pass clean.
- **HOLD: 3 items, all with the skeptic (Reviewer 3), all disclosed in the package:**
  1. **3.3** — prereg-after-validation, disclosed; Ben to decide whether a blind re-run is worth it.
  2. **3.4** — the P0-1 rest-frame softening; needs Ben's sign-off on the chosen resolution.
  3. **3.5** — 5 record-only references + 2 print-only books not yet submission-grade.

**Gate verdict: CONDITIONAL PASS.** No HOLD is a scientific defect in the re-architecture itself; all three are disclosure/curation items requiring Ben's judgment, not silent problems. The paper is submission-ready as a Perspective once the three HOLDs are cleared — none requires re-doing the benchmark, the panels, or the manuscript.
