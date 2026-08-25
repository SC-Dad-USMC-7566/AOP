# AOP Diagnostic Archetypes — Re-grade

**Status:** OAI Phase 3 deliverable — re-grades the five worked cases (§11 of the frozen v1.17 canon) from *measured semantic profiles* to **diagnostic archetypes**, each with its declaration tuple (ADR-002) and two-axis status label (ADR-002b). Non-canonical. **Compiled:** 17 July 2026. Baseline: `FROZEN_aop_canon_v1_17.md`.

---

## The re-grade, and why it is honest

The frozen v1.17 §11 already carries the correct posture in prose: the five cases are *"not decoration; they are the framework's primary evidence that the four-fold carving is the right one … Each is a persister that forces two axes apart and so refutes a collapse the single-axis incumbents would make,"* and the figure caption states *"bar heights are illustrative shape, not measured values."* The OAI defect was that the profiles nonetheless **looked like measurements** (bar charts over four axes), inviting a reader to treat an illustrative shape as data.

**The re-grade makes the diagnostic role structural, not decorative.** Each archetype is re-stated as: (1) the **dissociation** it forces (which two axes it pries apart), (2) the **incumbent collapse** it refutes, (3) its **declaration tuple**, and (4) its **two-axis status label**. No archetype is assigned a numeric four-axis profile it cannot support; where a value is genuinely computable (Drive, Memory — partition-free) it may carry one, and where it is not (Boundary, Integration — partition-dependent) it carries a *sign/ordinal* claim only.

## The five diagnostic archetypes

| Archetype | Dissociation it forces | Incumbent collapse it refutes | Computable axes | Status label (dependency × evidential) |
|---|---|---|---|---|
| **Flame** | Boundary ⊥ Memory | a memory-maximizing individuality axis [6] cannot honestly score a maintained boundary with ≈0 memory | Drive (high), Memory (≈0) | **dissociable** (the weld is breakable) × **constructed-counterexample** |
| **Spore** | Memory-as-storage ⊥ Drive; forces the Memory numerator choice (Cμ over E) | a drive- or E-centric axis reads deep stored structure at zero drive as "inert" | Drive (≈0), Memory (high, Cμ) | **dissociable** × **constructed-counterexample** |
| **Crystal** | fixes the spent-semantics pole (Memory solid, Drive=0, no live dependence) | a persistence≡activity reading calls a stable crystal "dead" or scoreless | Drive (0), Memory (frozen) | **forced** (terminal pole is real) × **analytic-model-result** |
| **Bound atom** | marks the minimal admitted case at the domain's low edge | a boundary-requires-metabolism reading excludes a persistent bound state | Drive (0), Memory (N/A) | **forced** (domain-edge) × **definition/stipulated-weld** |
| **Star** | high-Drive ∧ high-Integration ∧ gravitationally bound; realizes the §6 resolvability limit | a "more integration ⇒ sharper parts" reading; the star blurs *harder* because its coupling is the real derived one | Drive (high), Integration (high) | **conditionally-forced** (rests on Lane–Emden n=3 linearization) × **analytic-model-result** (VIF from derived stellar operator) |

## Declaration tuples

The archetypes are qualitative persisters, not one CTMC, so their tuples are **partial** — they declare the slots a diagnostic claim actually rests on and leave the rest N/A (this is itself the honest move: an archetype does not pretend to a full measurement). Template per ADR-002 D = (S, E, F, P, δt, τ, R, V, I, N):

- **Flame:** S = combustion front; E = fuel/O₂ reservoir + heat sink; F = the thermal/luminous edge (explicitly observer-relative — thermal ≠ ionization ≠ luminous); P = front vs surround; V = maintained-boundary predicate; **claim rides on F and V being definable with Memory numerator ≈ 0.** Status: dissociable × constructed-counterexample.
- **Spore:** S = dormant genome+coat; E = germinant field; F = coat (a lock, not a reader); τ = conditional-future horizon; V = re-formability given a coupling; **claim rides on Memory = Cμ (structural), not E (predictive), being the load-bearing numerator.** Status: dissociable × constructed-counterexample.
- **Crystal:** S = lattice; Drive = 0 by construction; V = configuration-stability; **claim rides on the spent-semantics pole being a real terminal state, not a low score.** Status: forced × analytic-model-result.
- **Bound atom:** S = bound electron-nucleus state; F = the binding (binding, not rest mass — the §10 domain criterion); **claim rides on the domain admitting a Drive=0, Integration-N/A minimal case.** Status: forced × definition/stipulated-weld.
- **Star:** S = radial shell chain; F = self-gravitating envelope; coupling operator = linearized adiabatic pulsation on a Lane–Emden n=3 polytrope; V = resolvability (VIF per shell); **claim rides on the derived operator's stiff-to-sloppy spectrum, conditionally-forced on the n=3 linearization.** Status: conditionally-forced × analytic-model-result.

## How this threads to the benchmark

The benchmark (`REV_AOP_Benchmark_Results_v1_0.md`) is the sixth diagnostic archetype and the only **exactly-solvable** one: it forces the dissociation **structural-strength ⊥ viability-importance** (Spearman −0.67) and refutes the collapse *"coupling strength ranks importance."* Where the five canonical archetypes each pry apart two of AOP's own axes, the benchmark pries apart the **method's input** (correlation/rate) from its **verdict** (viability), closed-form. It is the archetype whose declaration tuple is complete (model spec §3) — the others are deliberately partial — and so it is the one that carries the non-triviality proof the five illustrative cases cannot.
