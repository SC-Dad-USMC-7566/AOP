# Line-Check — Ptaszyński & Esposito (arXiv:2410.13375)

**Gates:** the canon gap-register **row 8** regrade (equilibrium vs. robust extensive multipartite correlation).
**Author lane:** Claude Science (builder). Proposal for Prime to verify / Ben to decide — not canon.
**Date:** 21 July 2026. **Method:** full text read from the primary source (PRL / arXiv v3), not from OpenAlex.

---

## Part 1 — Citation metadata (confirmed)

- **Exact title:** *Dissipation Enables Robust Extensive Scaling of Multipartite Correlations*
- **Authors (full list):** Krzysztof Ptaszyński; Massimiliano Esposito (University of Luxembourg; Ptaszyński also Institute of Molecular Physics, Polish Academy of Sciences, Poznań). Two authors.
- **Publication:** *Phys. Rev. Lett.* **135**, 057401 (2025). DOI `10.1103/j21x-hrsq`. OpenAlex `W4403579536`.
- **Preprint:** arXiv:2410.13375v3 (26 May 2025), `cond-mat.stat-mech`.
- **Note for canon:** if the reference is currently cited as an arXiv preprint, upgrade it to the PRL version.

## Part 2 — What the theorem actually says (from full text)

**Scope (load-bearing):** results hold for **permutation-invariant** systems — N identical classical discrete-state (Markov-jump) units, all-to-all coupled, analyzed via deterministic mean-field equations. Not a general-topology / all-systems statement.

**Theorem (Eqs. 10–11 + "Conditions of robust extensive scaling"):** the intensive multipartite mutual information is `lim_{N→∞} I_M/N = s(n̄_t) − \overline{s(n_t)}` (attractor- and time-averaged intensive entropy). Consequences:
- single fixed point ⇒ `I_M/N → 0` (**subextensive**);
- extensive (`I_M/N > 0`) is possible in exactly two scenarios — **(I)** relaxation to a time-dependent attractor (limit cycle / chaos), or **(II)** coexistence of several fixed points.

**Exact definition of "robust":** structural stability of the scenario under a transition-rate perturbation `W_λ(N) → W_λ(N) + εG_λ(N)`, arbitrarily small ε, finite `G_λ`. Under it:
- **(II) is NOT robust** — fixed-point coexistence needs fine-tuning to a discontinuous-transition point; a generic perturbation drives one attractor to `p_γ = 1` and kills extensivity.
- **(I) IS robust** — hyperbolic limit cycles (Floquet multipliers off the unit circle; their Appendix A) are structurally stable, and such attractors exist only out of equilibrium ⇒ require dissipation.

## Part 3 — Which of the four claims the theorem supports

| | Claim under test | Verdict |
|---|---|---|
| **(a)** | Impossibility of *robust* extensive multipartite correlation at equilibrium | **Supported, scoped.** True within permutation-invariant systems (equilibrium ⇒ only fixed-point attractors ⇒ only the non-robust scenario II). Not proven categorically for all systems. |
| **(b)** | Time-dependent / limit-cycle dynamics required | **Supported (same scope).** Robust extensivity ⇒ time-dependent attractor ⇒ far from equilibrium ⇒ dissipation. The paper's headline. |
| **(c)** | Citable tendency vs. open model-scoped question | **Both, split by scope.** *Within* the permutation-invariant class it is a **theorem, not a tendency** (stronger than "tendency"). *Beyond* it, the authors explicitly flag as **open** whether the conclusions hold — naming finite-dimensional lattices (spatiotemporal patterns/waves) and disordered systems (spin glasses; extensive degenerate equilibrium minima) as possibly different. |
| **(d)** | Gap-register row 8 "closes by citation" | **Only conditionally.** Closes for the **permutation-invariant / mean-field regime**. If row 8's claim is categorical (any topology), this citation does **not** close it — the general case is open per the authors. |

## Part 4 — Flag for the regrade (anything narrower than the summary claims)

1. **Model-scoped, not universal.** Any canon wording broader than *"in permutation-invariant (all-to-all / mean-field) stochastic systems, thermal equilibrium forbids robust extensive multipartite correlations"* overstates the primary source. Lattice and disordered cases are open by the authors' own "Final remarks."
2. **"Robust" must keep its technical meaning** (structural stability under small rate perturbations). Dropping the qualifier flips the truth value: non-robust extensive scaling *does* occur at equilibrium discontinuous-transition points (fine-tuned); it is only the *robust* version equilibrium forbids.

**Bottom line for row 8:** supports a regrade to a **model-scoped [SETTLED]**, not a universal one. If the surrounding canon claim reaches past permutation-invariance, grade **[SYNTHESIS]** or annotate the scope explicitly.

*Builder line-check. Prime verifies; Ben decides.*
