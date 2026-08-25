# Task order — Gate 1, system selection for the life-criterion arc

**Document ID:** `TASK_CS_AOP_LifeCriterion_SystemSelection_20260801.md`
**Issued by:** prime (chat seat), 1 August 2026
**Seat:** Claude Science (builder)
**Parent freeze:** `AOP_LifeCriterion_DispositionRule_FROZEN_v1_0_20260801.md` — Drive `1-HkXf58z-UWnYVkT1mcNR3_y2hIi3PAy`, md5 `b7eebcfd5a371a78b33a5fe230d52554`, frozen 2026-08-01 19:52:57 −0700
**Governing work order:** Drive `11YYUfUeisfzS3Wjv5sXG9TACmf5O6csQ`
**Ben's ruling in force:** §0 option **(a)** — own test article; sporulation stays reserved to H4/RED-25.

**This order adds no decision to Ben's three.** Selection concludes inside Gate 1 and reaches Ben only as part of the operational pre-registration he freezes at decision #2.

---

## 1 · The benchmark's rejections do not transfer, and this matters

Five systems have been rejected for the **external benchmark**: *B. subtilis* sporulation, yeast HOG, yeast GAL, *E. coli* DNA repair, and phage λ. **None of those rejections applies here.** They were scored against A.1.7 (≥2 redundant pairs with near-WT singles) and A.1.8 (a published model emitting the measured persistence quantity) — criteria built for a question about coalition and redundancy structure. This arc asks a different question and needs a different filter: **is there a stored, separately-perturbable set-point?**

Two consequences:

- A benchmark rejection is **not** grounds to reject a candidate here. If one of the five is the best article for this question, say so and defend it.
- **But contamination is real and runs the other way.** Cowork has read the HOG, GAL, DNA-repair, and λ literatures for benchmark purposes. Sporulation is reserved outright by Ben's ruling. Selecting any of the remaining four means that seat cannot serve on the benchmark thereafter. Prefer a candidate outside all five; if you cannot, state the contamination cost explicitly and let Gate 1 price it.

A.1.9 — the adequacy/redundancy anti-correlation — is a benchmark heuristic graded frontier on five observations. **Do not apply it here.** Its reasoning is about redundant architecture, which this arc does not require.

---

## 2 · Screening criteria for this arc

A candidate must clear all four. Score each explicitly; a candidate failing any one is rejected with that criterion named.

**S.1 — Dynamics and interventions, not topology.** Step 0 established that AOP's axes are not computable from a wiring diagram: Drive is identically zero at detailed balance, Memory is undefined without a declared process. The candidate needs a dynamical description *and* a class of physically performable interventions. Structure-only systems are rejected at this line. Flux-balance models remain parked and are not eligible.

**S.2 — A candidate stored reference.** There must be an identifiable slow variable that plausibly stores a target for the fast regulated dynamics, and that is *not* simply a fixed point of the fast constitutive drift. This is the object the whole arc is about. State what it is and why it is separable.

**S.3 — Independent perturbability of the reference (P1).** There must be at least one operation that plausibly moves the stored set-point *without* disabling the regulatory machinery. This is what makes P1 testable rather than rhetorical. If every available perturbation degrades rather than redirects, the candidate cannot test P1.

**S.4 — A tunable slow/fast ratio spanning at least two orders of magnitude (P2).** Without a sweepable ratio, P2's kill condition — a reproducible knee — cannot be looked for, and P2 returns UNINFORMATIVE by construction.

**S.5 (desirable, not disqualifying) — a lifetime readout and a matched comparison class (P3).** A declared viable set with a survival, hazard, or first-passage observable, plus systems matched on everything but the architecture. Score it; do not reject on it. P3 cannot kill the criterion, so it should not drive selection.

---

## 3 · The negative control is not optional

P1 has a second kill condition: **a system the criterion excludes turns out to have competent misregulation.** That cannot be tested with a positive article alone. Selection must therefore deliver a **pair**:

- a **positive article** — a system the criterion calls alive, and
- a **matched negative control** — a system that demonstrably *corrects* but is model-free, where the target sits in the constitutive dynamics with no separable reference.

The star is AOP's canonical model-free corrector and is useless here because it cannot be intervened on. Find one that can be. A reconstituted or engineered corrector with a target baked into its kinetics is the obvious shape. **A selection that delivers only a positive article is incomplete and does not close Gate 1.**

---

## 4 · Prime's shortlist — recall only, verify or discard

**Verification tier: none.** The four below are prime's recollection, stated to order the search, and **not one of them has been checked against a primary this session.** Abstract-level inference is this project's documented standing failure mode — four retractions in the bioelectric arc had exactly this shape. Treat every claim below as a hypothesis about the literature, not a report of it. Discard freely; a better candidate you find yourself is worth more than confirming one of mine.

1. **Chemotactic adaptation via receptor methylation (*E. coli*).** The methylation state is slow and plausibly stores the adaptation set-point, separably from the fast receptor-to-motor path; set-point-shifting perturbations of the methylation enzymes plausibly exist; the ratio is plausibly tunable by expression level. Prime's lead candidate on S.2–S.4. Weak on S.5 — the link from chemotactic competence to a declared viable set is indirect and would need arguing.
2. **Heat-shock regulation via chaperone titration (*E. coli*).** Plausibly the best S.5 of the four, since survival at elevated temperature is a genuine lifetime observable with matched comparison classes available. Whether the set-point is genuinely *stored* rather than emergent from titration kinetics is exactly the question S.2 asks, and it may fail there.
3. **Hypothalamic thermoregulation / fever (mammalian).** Conceptually the cleanest instance of P1 anywhere in biology — a pyrogen shifts the set-point, the machinery stays intact, and regulation proceeds competently toward the wrong target, reversibly. Strong on S.2 and S.3, likely weak on S.1 (quantitative dynamical description) and S.4, and expensive. Worth scoring even if rejected, because it sharpens what P1 is asking for.
4. **A reconstituted oscillator or engineered controller.** Prime's leading shape for the **negative control** under §3, not for the positive article. Full intervention access is the point.

---

## 5 · Deliverables

1. **Selection report.** Each candidate scored against S.1–S.5, with retrieval status per claim (`[primary-verified]`, `[primary-abstract-only]`, `[secondary]`, `[not-retrieved]`) in the convention the benchmark records file already uses.
2. **Rejection log.** Every candidate considered and rejected, with the operative criterion named. Required by anti-gaming clause 2 of the freeze, and it is an explicit attack target for OAI.
3. **The pair.** A positive article and a matched negative control, or an argued statement that no pair clears the criteria — which is itself a reportable finding and closes Gate 1 differently.
4. **A blocked-retrieval ledger** where paywalls stop you. Do not substitute a secondary and call it retrieved.

**Do not** write, sketch, or imply the operational pre-registration. Selection feeds it; prime drafts it; OAI attacks it before it freezes; Ben freezes it. Do not compute any AOP quantity on a candidate. Do not grade your own output — prime verifies by re-running retrievals or by independent reconstruction.

---

*End of `TASK_CS_AOP_LifeCriterion_SystemSelection_20260801.md`. Proposal for Ben's release to the seat. Prime drafted it and does not authorize it.*
