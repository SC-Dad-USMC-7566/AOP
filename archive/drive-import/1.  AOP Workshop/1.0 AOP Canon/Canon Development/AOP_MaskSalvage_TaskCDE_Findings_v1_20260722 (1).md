# Tasks C, D, E — predicate resolution, attribution-convention table, phase-diagram sketch

**Builder proposal — Prime verifies; Ben decides. Not a verdict; touches no canon master.**
**From:** Claude Science (builder), AOP · **Date:** 22 July 2026 (v1)
**Pinned functional:** Task A (deposited-script Laplacian scramble, load O(a)). **Reproduction:** Task B (a\* = (3+√13)/2 closed-form).

---

## Task C — the predicate/code mismatch, resolved

**Decision (builder's pick; Prime may overrule): adopt the PROSE predicate in full —**
`salvageable(a) = well_defined_GLOBAL(a) AND disjoint(a) AND informative_midpoint(a)`, i.e.

- **global** well-definedness (max interval-width / W_agg over *all* structural edges ≤ τ_wd), not load-only;
- disjointness (load interval above spectator interval) **AND** the 0.02·W_agg midpoint-separation flag.

**Why.** (i) The mask is unusable if *any* structural edge's weight is unresolvable, so the honest well-definedness question is whole-graph, not load-only; load-only silently assumes the answer for five of six edges. (ii) The salvage claim is *resolvable discrimination*, which requires the classes to be separated (midpoint flag), not merely non-overlapping at the endpoints. This is the predicate the prose declared; the deposited code computed a weaker one (`disjoint AND wd_load`).

**What changes on the K4 table:** *nothing* — all four predicate variants (load-only vs global × disjoint-only vs disjoint+midpoint) return the **identical** salvageable set `a ∈ [0.1 … 3.0]` on the grid. This confirms the documented coincidence directly:
- the load edge **is** the widest structural edge at every a (widths at a=1: load 0.294 vs 0.212 support vs 0.077 spectator) → global = load-only here;
- disjointness ⟹ midpoint-flag at every grid point → dropping the midpoint conjunct is invisible here.

They coincide **on this model**; they answer different questions in general. Corrected implementation: `mask_salvage_predicate_fixed_v1_20260722.py` (new file — does **not** overwrite the audit artifact).

**Threshold sensitivity of the adopted predicate.** The salvageable region's upper edge is `a_max = min(disjointness boundary, well-definedness boundary)`:
- **disjointness boundary** a\* = (3+√13)/2 ≈ 3.303 — **closed-form, threshold-independent**;
- **well-definedness boundary** depends on **τ_wd only**: τ_wd=0.3 → a≈1.19 (binds first), τ_wd=0.5 → a≈6.40, τ_wd≥0.7 → never on [0.1,20];
- **τ_inf is inert** on K4 (0.00–0.10 give the same a_max), because disjointness already forces a large midpoint gap.

So for any reasonably loose τ_wd ≥ 0.5 the salvage ceiling is the disjointness point a\* = (3+√13)/2; only a tight τ_wd < ~0.4 makes well-definedness bind first.

**Grade:** the predicate choice is a **definitional** decision, not a result. The K4-table invariance under all four variants is an **identity/theorem demonstration** (no parameter flips it within the class) — **no evidential weight**.

---

## Task D — the attribution-convention table (pre-registered; see frozen note, Drive-timestamped 22 Jul 22:14:09Z, *before* this run)

**Every analytic convention matched the pre-registration.** Finite ceiling a\* in coupling strength on (0, 12]:

| Convention | Finite ceiling? | a\* | Pre-registered | Category |
|---|:--:|---|:--:|---|
| Full min–max envelope | **YES** | (3+√13)/2 = 3.303 | YES ✓ | contingent |
| \|C\| ≤ 0 | no | — | NO ✓ | identity (spectator ≡ 0 in ∅) |
| \|C\| ≤ 1 | no | — | NO ✓ | contingent |
| \|C\| ≤ 2 | no | — | NO ✓ | contingent |
| \|C\| ≤ 3 | **YES** | 3.303 | YES ✓ | contingent |
| \|C\| ≤ 4 | **YES** | 3.303 | YES ✓ | contingent |
| Matched-context | no | — | NO ✓ | contingent |
| Uniform mean | no | — | NO ✓ | contingent |
| True Shapley | no | — (gap grows +0.39→+0.81) | NO ✓ | contingent |
| Sparse n=4/8/16 (envelope base) | YES but **biased/variable** | median 3.95 / 3.50 / 3.41 | "unstable/estimated" ✓ | **estimated — not analytic** |

**Reading.** The finite ceiling exists **only** under the full min–max envelope and under bounded coalition cardinality **≥ 3**. It is *created by the unmatched min–max comparison* (load's best-case context vs spectator's worst-case context), and it needs high-order (|C|≥3) contexts to exist at all — exactly the contexts that a low-cardinality or matched or mean convention never forms. Under every mean-type convention (uniform mean, true Shapley, matched) the load stays ranked above the spectator at **every** coupling strength, with **no finite ceiling** — the Shapley gap *grows* with a (+0.39 at a=1 → +0.81 at a=8).

**Sparse sampling is estimated, not analytic** (flagged as such per charter): on the envelope base it *does* recover a ceiling in 30/30 seeds, but **biased upward and variable** (n=4 median 3.95, up to 5.81; converging to the true 3.303 only as n→16). A subsampled envelope misses the extremal contexts that define the true merge, so it overestimates a\*. This is a directional confirmation of the envelope result, not an independent one.

**Consequence:** the "ceiling" is real but **convention-specific** — it is a property of the min–max envelope at cardinality ≥ 3, not of the attribution problem. Under the conventions one would defend as canonical (Shapley, matched, mean), there is no finite ceiling: load stays above spectator everywhere. This turns the work order's assertion into a table, as requested.

**Grade:** the envelope and |C|≥3 ceilings are **contingent results** — the pre-declared cardinality/convention parameter genuinely erases them, and it was named in advance (frozen note). The |C|≤0 no-ceiling is an **identity** (spectator marginal ≡ 0 in the empty context). Sparse rows are **estimated**, labelled.

---

## Task E — three-coordinate phase diagram: sketch only (a lead, not approved work, no grade)

The critic proposed the useful object is not one scalar ceiling but a phase diagram over three coordinates: **C1 semantic relevance** (matched-context), **C2 attribution stability** (across contexts), **C3 mechanistic identifiability/intervenability**. Quick check on the existing K4 of whether they are genuinely independent:

| Coordinate (proxy) | LOAD | support | SPEC | ranking |
|---|---:|---:|---:|---|
| C1 relevance (mean marginal) | 0.641 | 0.245 | 0.061 | LOAD > support > SPEC |
| C2 stability (1/(1+interval width)) | 0.601 | 0.646 | 0.778 | **SPEC > support > LOAD** |
| C3 identifiability (1/VIF from param Fisher) | 0.800 | 0.800 | 0.800 | **degenerate — all equal** |

**Finding of the sketch (not a result):**
- **C1 and C2 are genuinely independent** — they rank the edges in **opposite** order. The load edge is the *most relevant* but *least stable* (its marginal is largest yet most context-sensitive); the spectator is *least relevant* but *most stable*. Relevance and stability dissociate cleanly on K4. This supports the critic's intuition that they separate.
- **C3 collapses on K4.** On the equal-strength complete graph every edge has the same VIF (by symmetry), so identifiability carries **no information here** and cannot be tested for independence from C1/C2 on this model. Testing C3 requires an **asymmetric** coupling model (distinct weights) where collinearity varies per edge.

So: two of the three coordinates are demonstrably independent on the existing model; the third needs a richer model to evaluate. This is a **plausible lead worth a scoped model**, nothing more — it has **no grade** and must not acquire canon status by having appeared in a critic report or here. Sketch only, as instructed.

---

## Bottom line for Prime (builder's summary, not a verdict)

1. **Forced-ness confirmed and pinned (Task A):** the existential non-emptiness is forced; the load/spectator exponent discrepancy is purely a scramble-semantics choice (Laplacian → O(a) = critic; off-diagonal → O(a²) = Prime), and the conclusion holds under both.
2. **Headline numbers reproduce (Task B):** a\* = (3+√13)/2 ≈ 3.3027756 (now closed-form), Ω ≈ 0.812.
3. **Predicate fixed (Task C):** adopt the prose predicate (global + midpoint); K4 table invariant across all four variants, so the published numbers stand, but the estimand now matches the prose. Ceiling = min(a\*, τ_wd-boundary).
4. **Ceiling is convention-specific (Task D):** exists only under the min–max envelope at cardinality ≥ 3; **vanishes under Shapley, matched, and mean**, where load stays above spectator everywhere. Pre-registered, all predictions held.
5. **Phase-diagram lead (Task E):** relevance and stability dissociate on K4; identifiability needs an asymmetric model. Sketch only.

*Syntactic layer only (Φ / coupling graph / attribution). No canon master touched, no canon prose proposed, nothing folded, nothing self-graded as settled. Prime verifies; Ben decides.*