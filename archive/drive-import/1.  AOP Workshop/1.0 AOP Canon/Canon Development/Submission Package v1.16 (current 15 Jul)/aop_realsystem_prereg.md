# AOP Gate — Do the Mechanism Ceilings Survive on a Real Driven System? (PRE-REGISTRATION)

**Status: pre-registration. Exits frozen before computation. Two exits only: GO / NULL.**
_Drafted 2026-07-16. Test #1 of the substitutability follow-ons. The ceiling ordering (Flux and
Bank have hard ceilings below full persistence; only Barrier is unbounded) was found on a
minimal constructed Markov chain with hand-built linear rates. This gate asks whether the
ordering is a lattice artifact of that construction or survives on a **real driven chemical
system with mass-action kinetics** — the "one real system" the reframing demanded._

---

## The system (frozen)

The **Schlögl model** — the canonical bistable chemical reaction network with a genuine
non-equilibrium steady state and a real, computable entropy production:

  A + 2X ⇌ 3X   (k1, k2);   B ⇌ X   (k4, k3)

A and B are chemostatted (held fixed), giving a birth–death process in the molecule number
X ∈ {0,…,X_max} whose stationary distribution is bistable for suitable parameters. Mesoscopic
propensities (volume Ω): birth W⁺(n) = k1·a·n(n−1)/Ω + k4·b·Ω; death W⁻(n) = k2·n(n−1)(n−2)/Ω² +
k3·n. Persistence **P** ≡ stationary probability mass in the high-X basin (X ≥ the unstable
saddle X_s). Entropy production σ̇ computed from the exact birth–death NESS formula
σ̇ = Σ_n (W⁺(n)p_n − W⁻(n+1)p_{n+1})·ln[W⁺(n)p_n / W⁻(n+1)p_{n+1}].

Three knobs, defined as cleanly as the chemistry allows (their separability is itself part of
the test):
- **Barrier** b_k — a detailed-balance-preserving deepening of the high-X well (scale the
  autocatalytic forward/back pair together so the *equilibrium* shifts toward high X; σ̇ stays 0).
- **Flux** d — the chemical drive: push the chemostat ratio away from the equilibrium ratio,
  breaking detailed balance and creating a net A→B cycle current with σ̇ > 0.
- **Bank** r — a reset reaction firing at low X (X ≤ X_s): re-inject to a high-X state at rate r
  (a reader re-instantiating the pattern), the mesoscopic analog of the previous gate's reset.

## GO requires (frozen)

The qualitative ceiling ordering from the minimal model reproduces on the Schlögl system:
1. **Barrier is unbounded** — increasing b_k alone drives P → 1 (within tolerance) at σ̇ = 0.
2. **Flux has a ceiling** — increasing d alone saturates P at a value **< 0.95** no matter how
   hard it is driven (pure throughput cannot pin the system in the basin).
3. **Bank has a ceiling** — increasing r alone saturates P at a value **< 0.95**.
4. The ordering is strict: at least one mechanism (Barrier) reaches a persistence the other two
   cannot, so on the real system the three are **not** freely fungible at high P.

## NULL requires (any one, frozen)

- **Flux (or Bank) is unbounded on the real system** — it drives P → 1, so the ceiling was a
  construction artifact and the ordering does not survive contact with real kinetics.
- **Barrier ceils too** — no mechanism reaches high P, so there is no ordering to report.
- **The knobs are inseparable** — b_k, d, r cannot be varied independently on the real system
  (moving one unavoidably moves another), so the three-mechanism decomposition itself fails on
  real chemistry. (Reported honestly as a NULL for the decomposition, not forced into a pass.)

## Why both exits are reachable

GO reachable: nothing forces a real autocatalytic drive to saturate. NULL reachable and taken
seriously: mass-action rates are quadratic/cubic in X, unlike the constructed linear rates, so
the ceiling values and even their existence could differ — the whole point of testing on real
kinetics.

## Decision rule

GO only if all four GO criteria hold. NULL if any NULL criterion holds. No third exit.

## What a result licenses

- GO: the ceiling ordering is a real property of driven persisters, not a toy artifact — the
  substitutability result graduates from "minimal model" toward "worked system," the thing the
  reframing correctly said was missing.
- NULL: the ordering (or the three-mechanism decomposition) is model-specific; the canon's
  bounded-substitutability claim must be scoped to the constructed model and not generalized.
- Neither exit touches the four-axis structure or the Φ-individuation result.
