# AOP Gate — Substitutability of the Persistence Mechanisms (PRE-REGISTRATION)

**Status: pre-registration. Exits frozen before any computation. Two exits only: GO / NULL.**
_Drafted 2026-07-16. Tests the one falsifiable idea in the first-principles reframing thread
(canon-suspended doc, 16 Jul): that Barrier, Flux, and Bank are **substitutable at fixed
persistence** — "persistence is a budget met in three currencies; the content is in the
exchange rates." This is the move that would answer the standing charge that the framework
"by its own admission cannot be wrong." It is registered as a gate because it can fail._

---

## The claim under test

The reframing asserts three mechanisms for keeping a basin occupied against its kicks —
Barrier (lower the coupling / deepen the wall), Flux (pay throughput to steer back), Bank
(store the pattern and re-instantiate through a reader) — and claims they are **fungible at
fixed persistence**: the flame is all flux, the spore all bank, the crystal all barrier, and
these are "three solutions to one problem" between which a system can trade continuously.

The claim is only content-bearing if persistence is a **single currency all three pay into**,
and if all three can **independently** carry it. If Bank's "persistence" (survive-by-recovery)
is a different observable from Barrier's (never-be-erased), the exchange rate is undefined and
the three-currency picture is a category error dressed as a theory.

## The system (frozen)

A continuous-time Markov chain on states {0, 1, …, N} built from the deposited resolvability
engine's rate machinery (`general_rate`, `stationary`, `entropy_production`). State 0 is the
**erased** state; states near N are **deep in the basin**. A fixed **perturbation spectrum**
is a state-independent downward kick rate κ (toward erasure) — frozen at κ = 1.0, N = 6.

Three independently-set knobs, each a distinct mechanism:

- **Barrier** b ≥ 0 — an equilibrium (detailed-balance) upward bias: transition rates carry a
  Boltzmann factor e^{+b} favouring climbing away from 0. Costs no dissipation (σ̇ = 0 when b
  is the only knob on). This is the passive wall.
- **Flux** f ≥ 0 — a non-equilibrium driven current circulating 0→…→N→0 that pumps probability
  back up. Costs dissipation σ̇ > 0, monotone in f. This is the throughput.
- **Bank** r ≥ 0 — a direct reset rate from the erased state 0 back to a basin state (the reader
  re-instantiating from a stored copy). Detailed-balance-breaking only at the reset edge; its
  signature is recovery-after-erasure, not never-erasing.

**Persistence currency (frozen before computation):** P ≡ stationary probability mass in the
basin set B = {states ≥ N/2}, under the fixed kick κ. One scalar, in [0,1]. All three knobs
raise P. Target persistence for the substitution test: **P\* = 0.80**, frozen.

## What GO requires (all four, frozen)

A level set {P = P\*} that is a genuine 2-D substitution surface with all three mechanisms
participating:

1. **Three pure corners reachable.** Each mechanism can, with at most one partner held at a
   floor value, reach P\* essentially alone: a barrier-dominated point (f≈0, r≈0), a
   flux-dominated point (b≈0, r≈0), and a bank-dominated point (b≈0, f≈0) all attain P\* = 0.80
   within tolerance. (The flame/spore/crystal claim, made literal.)
2. **Continuous trading between corners.** The iso-P surface connects the corners without a gap
   — one can walk from the barrier corner to the flux corner to the bank corner along
   {P = P\*}, trading one currency for another the whole way.
3. **Finite exchange rates.** The local trade ratios (∂b/∂f, ∂f/∂r, ∂b/∂r along the surface)
   are finite and bounded over the accessed range — no mechanism requires an unbounded amount
   of itself to offset a finite loss of another.
4. **The knobs are distinct axes.** Flux carries σ̇ > 0 at its corner; Barrier's corner has
   σ̇ ≈ 0; Bank's corner is distinguished by nonzero recovery flux through the reset edge with
   its own signature. If any two knobs turn out to move the same underlying quantity (surface
   collapses to 1-D, or two corners coincide), that fails this criterion.

## What NULL requires (any one, frozen)

- **A corner is unreachable.** Some mechanism cannot reach P\* even with a partner at its
  accessible ceiling — the mechanisms are not fungible; at least one is not a full currency.
- **The currency is not shared.** Bank's contribution to stationary basin-occupancy P is not
  comparable to Barrier/Flux's — e.g. reset raises P only by a mechanism that is really a
  disguised barrier, so "trading" is trading a thing against itself.
- **Degenerate surface.** The iso-P set is not a genuine 2-D surface with three participating
  axes (it is 1-D, or one axis does not move P at fixed others), so there is no substitution to
  measure.

## Why both exits are genuinely reachable (the stakes check, pre-committed)

GO is reachable: nothing in the construction forces a corner to fail — three monotone knobs on
one scalar *could* each carry it. NULL is reachable and, by charter skepticism, the **expected**
outcome: Bank operates on recovery-after-erasure while Barrier/Flux operate on never-being-
erased, so it is entirely possible the bank corner reaches a *different* P-regime and cannot be
equated — the exchange rate would be undefined, and the three-currency picture would fail on its
own terms. We commit to reporting whichever way it falls.

## Decision rule

GO only if **all four** GO criteria hold. NULL if **any one** NULL criterion holds. No third
exit; a null is not reinterpreted into a win. Tolerance on P\*: |P − 0.80| ≤ 0.02.

## What a result would and would not license

- GO would give the framework its first **falsifiable, quantitative** claim demonstrated on a
  worked system — substitutability with measured exchange rates — the thing the reframing
  correctly identifies as missing. It would still be a minimal model, not nature.
- NULL would be equally informative: it would show the "three currencies" picture is a
  category error, and that persistence mechanisms are *not* freely fungible — which would be a
  reason **not** to adopt the reframing's central move, and a finding in its own right.
- Neither exit touches the four-axis canon structure or the Φ-based individuation result; this
  gate tests the reframing's economics claim, not the axis count.
