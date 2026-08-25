# AOP Gate — Do the Mechanism Ceilings Survive on a Real Driven System? VERDICT

**Frozen exit: NULL** (pre-registration `aop_realsystem_prereg.md`, v1). The ceiling ordering
found on the minimal constructed Markov model — Flux and Bank bounded, only Barrier unbounded —
**does not survive contact with real mass-action kinetics.** NULL fires on two of the three
pre-registered NULL criteria at once. This is the charter working exactly as designed: a "new"
result, tested harder, turned out to be an artifact of the toy model's construction.

## System

Schlögl bistable reaction network (A+2X⇌3X, B⇌X), chemostatted, as a birth–death process in
molecule number X at volume Ω=25. Bistable base found by parameter scan (a=0.95, b=5.27; modes
near X≈0 and X≈4Ω, saddle at n_s=43, base P(high)=0.415). Persistence P = stationary mass in the
high-X basin; entropy production σ̇ from the exact chemical-cycle affinity.

## Results against the frozen criteria

| mechanism | on the real system | GO expectation | met? |
|---|---|---|---|
| **Barrier** (deepen well on the detailed-balance manifold) | P → 1.000 at σ̇ = 0 | unbounded | yes |
| **Flux, pure** (cycle current at fixed stationary distribution) | **P invariant at 0.415** — zero leverage | ceiling < 0.95 | **no — worse: no leverage at all** |
| **Flux, chemostat** (raise b) | P → 1 but σ̇ blows up to ~1900 | ceiling < 0.95 | **no — and inseparable from Barrier** |
| **Bank** (reset low-X → high-X at rate r) | P → 0.895, 0.939, 0.965, 0.998 at r=0.5,1,2,50 — **unbounded** | ceiling < 0.95 | **no** |

Barrier is confirmed unbounded (GO criterion 1). But **Bank is also unbounded** on the real
system (NULL criterion 1: "Flux or Bank is unbounded"), and **Flux is not a well-posed
independent knob at all** (NULL criterion 3: the knobs are inseparable). Two NULL criteria fire.

## Why the ceilings were artifacts — the real finding

This is the instructive part, and it is a theorem, not a numerical accident.

1. **A one-dimensional birth–death system has no independent flux axis.** Its stationary
   distribution — and therefore P — is fixed entirely by the ratio W⁺/W⁻ of birth to death
   propensities. A pure cycle current (raising the cross-channel flux while holding W⁺ and W⁻
   fixed) changes σ̇ without touching the distribution: **flux has exactly zero leverage on
   persistence.** The minimal model's "flux knob" (a directional tail added to the ring) moved P
   only because it *also* changed the effective W⁺/W⁻ — it was a disguised barrier. On a system
   where flux is defined cleanly, the flux ceiling isn't low; there is no flux axis to have a
   ceiling on.

2. **Bank's ceiling was a lattice artifact.** In the 7-state minimal model, reset re-injected to
   a single fixed interior state and competed against a fixed kick, so it saturated at the basin's
   state-fraction. In a real bistable system the reset re-injects into the *deep metastable well*,
   whose own dynamics then hold the system there — so reset drives P → 1 without bound. The
   ceiling was a property of the toy's tiny fixed state space, not of "recovery-after-erasure."

## What this does to the earlier substitutability result

The **substitutability gate's headline — "strict ordering, only Barrier unbounded" — is
retracted as a general claim** and rescoped to the minimal model where it was computed. It does
not generalize to real driven persisters. What survives, and is now *more* honest:

- **Persistence in a birth–death system is a property of the stationary distribution alone.**
  The only way to raise it is to reshape that distribution — which Barrier (equilibrium) and Bank
  (reset into a metastable well) both do, and pure Flux cannot. This is a cleaner statement than
  the ceiling story: it says *flux/drive does not buy persistence directly at all* in this class,
  consistent with the canon's forced-edge structure (Drive acts on Memory and Boundary, not on
  persistence directly).
- The **budget gate's conclusion is untouched and in fact reinforced**: cost (σ̇) and persistence
  are independent, and here we see the extreme case — you can raise σ̇ without limit (pure flux)
  and move P not at all.

## Verdict: NULL, and a retraction

The ceiling ordering is model-specific. The canon's bounded-substitutability claim (folded in
this session) must be **scoped to the constructed model**, and the stronger "strict ordering"
reading removed. The four-axis structure and Φ-individuation result are untouched. Figure
`figS9_realsystem.png`.

## Reproduce

`aop_realsystem_gate.py` (Schlögl birth–death, three knobs, chemical σ̇). Numbers: base
P=0.415 at saddle n_s=43; barrier P→1 at σ̇=0; pure flux P≡0.415 (σ̇→∞); bank P→0.998 at r=50.
