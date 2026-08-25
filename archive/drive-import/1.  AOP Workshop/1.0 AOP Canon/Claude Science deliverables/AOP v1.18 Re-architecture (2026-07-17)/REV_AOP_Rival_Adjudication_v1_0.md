# AOP Rival Adjudication — Benchmark Scored Under a Named One-Axis Comparator

**Status:** OAI Phase 5 deliverable. Scores the benchmark under one named, computable single-axis rival and reports the comparison honestly, at the scope ADR-003 permits (a Perspective may report a favorable comparison; it may not claim adjudication). Non-canonical. **Compiled:** 17 July 2026. Data: `rival_transfer_entropy.json`, `benchmark_results.json`.

---

## The rival: transfer entropy (single directed-information axis)

The fairest one-axis comparator is not a strawman "coupling strength" but a respected, widely-used measure of directed influence: **transfer entropy** (Schreiber 2000), which asks, for each pair of components, how much the source's history reduces uncertainty about the target's future beyond the target's own history. It is the standard answer to "what drives what" from a single information-theoretic axis, and — critically — it is **computable in closed form on the same CTMC**, so the comparison is on identical ground, not rhetoric.

**Rival importance score:** for each mechanism, the total transfer entropy across all component pairs (n,r,z) that is lost when the mechanism is deleted. This is the most viability-agnostic importance a one-axis method can assign: it reads the system's directed information architecture and ranks mechanisms by how much of it they carry.

## The result

| Mechanism | TE-importance (bits) | Viability ΔV | Ground truth |
|---|---|---|---|
| **Z** | **+0.058 (rank 1, 82% of total TE)** | **0.000** | inert spectator |
| C | +0.015 | 0.008 | weak-but-real |
| R | +0.015 (rank ~3) | **0.163 (rank 1)** | load-bearing |
| S1 | +0.005 | 0.118 | synergy |
| S2 | +0.005 | 0.118 | synergy |
| A | 0.000 | 0.000 | redundant |
| B | 0.000 | 0.000 | redundant |

- **The rival ranks Z first** — it assigns 82% of all directed information flow to the mechanism whose viability contribution is exactly zero. The z↔r tracking coupling is genuinely where most of the system's directed information lives; transfer entropy is not *wrong* about the information architecture, it is answering a different question than "what does persistence depend on."
- **The true load-bearing mechanism R** (rank 1 by viability) sits at **rank 3** under transfer entropy, tied with the weak influx C.
- **The redundant pair {A,B}** scores exactly **zero** under transfer entropy, exactly as it does under single-edge viability — a single-axis method cannot see joint necessity, whichever axis it picks.
- **Spearman(TE-importance, viability ΔV) = +0.41** — weakly positive, but it places the wrong mechanism at the top, which is the decision that matters.

## Adjudication (scoped)

**What the comparison shows.** On this benchmark, a strong, standard single-axis method (transfer entropy) returns a mechanism ranking whose top element is the causally inert one, and misses the redundant coalition entirely. The AOP apparatus — viability-relative ΔV plus the coalition/Möbius layer — returns the correct ranking (R on top, {A,B} recovered as a jointly-necessary coalition, Z at zero). The four-target, viability-anchored method is **necessary** here: no single axis, including the best one-axis directed-information measure, recovers the viability structure.

**What the comparison does NOT show (ADR-003 scope discipline).**
1. It does not show AOP is *uniquely* correct — only that this named rival fails on this system. A different rival, or a viability-augmented transfer entropy, might do better; that is a further test, not a foregone conclusion.
2. It does not show transfer entropy is a *bad* measure — it is a good measure of the wrong quantity for this question. The honest framing is *"single-axis directed-information importance and viability importance are dissociated on this benchmark,"* not *"transfer entropy is refuted."*
3. **This is one benchmark.** The comparison is an existence proof of dissociation, not a survey. A Perspective may report it as *"here is a system where the standard one-axis method gets the ranking wrong and the four-target method gets it right"* — a legitimate, bounded, favorable comparison — and no more.

**Verdict:** the benchmark clears the rival-comparison bar **as a Perspective result** — a demonstrated, closed-form dissociation between a named one-axis comparator and the AOP method, with the top-ranked mechanism differing (Z vs R). It is reported as a favorable comparison on one exactly-solvable system, explicitly not as an adjudication of AOP against all rivals.
