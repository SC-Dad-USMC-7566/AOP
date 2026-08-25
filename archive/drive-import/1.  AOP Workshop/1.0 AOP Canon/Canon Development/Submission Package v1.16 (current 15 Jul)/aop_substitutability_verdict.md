# AOP Gate — Substitutability: VERDICT

**Frozen exit: NULL** (pre-registration `aop_substitutability_prereg.md`, v1, exits committed
before computation). The reframing's central testable claim — that Barrier, Flux, and Bank are
substitutable *at fixed persistence* — **fails at the pre-registered target P\* = 0.80**, and
the reason it fails is itself the finding.

## Result against the frozen criteria

The pre-registration required (GO criterion 1) that all three mechanisms reach P\* = 0.80
essentially alone. They do not:

| mechanism | ceiling on P (alone, knob → ∞) | reaches P\*=0.80? |
|---|---|---|
| **Barrier** b | 1.000 (equilibrium wall, unbounded climb) | **yes** (at b = 0.817, σ̇ = 0) |
| **Flux** f | **0.5714 = 4/7 exactly** | **no** |
| **Bank** r | 0.7052 (saturates) | **no** |

NULL criterion "a corner is unreachable" is met: two of the three mechanisms have a hard
ceiling **below** the frozen target. The three currencies are **not freely fungible** at an
arbitrary persistence level. Per the decision rule (GO requires all four; NULL requires any
one), the verdict is **NULL**.

## Why — and this is the real content

The ceilings are not tuning artifacts; each is structural.

- **Flux tops out at exactly 4/7**, the geometric fraction of basin states (4 of 7). A pure
  dissipative current, pushed arbitrarily hard, drives the distribution toward *uniform
  circulation* — it equalizes occupancy, it does not concentrate it. Throughput can stir the
  system into the basin but cannot pin it there beyond the basin's share of state space.
- **Bank saturates near 0.71.** Reset refills the erased state, but the fixed kick κ keeps
  draining; the reset rate races the kick and asymptotes. Recovery-after-erasure buys a bounded
  occupancy, not an arbitrary one.
- **Only Barrier is unbounded**, because deepening the wall changes the *equilibrium* itself —
  it is the one mechanism that alters where the system sits at rest rather than how hard it is
  pushed back after a kick.

This vindicates the charter's skepticism and, more importantly, the **specific worry raised in
my own assessment of the reframing**: Bank operates on recovery-after-erasure while Barrier
operates on never-being-erased. They are *not the same currency*, and the data show it — their
persistence ceilings differ because the observable differs. The "budget met in three
currencies" picture is, at fixed high persistence, a **category error**: you cannot buy
0.80-persistence with flux or bank at any price.

## The post-hoc finding (clearly labeled, does not reinterpret the frozen exit)

Substitutability is not absent — it is **bounded to the regime below the lowest ceiling.** At a
persistence level P = 0.50 (below flux's 0.571 and bank's 0.705), all three corners *are*
reachable alone, and a genuine continuous iso-persistence surface exists:

- **Barrier ↔ Flux** trade smoothly along {P = 0.50}: b from 0 → 0.428 against f from 0.804 → 0,
  with dissipation σ̇ falling 1.31 → 0 across the surface. Local exchange rate d f/d b ≈ −1.7
  (finite, bounded): one unit of barrier buys ~1.7 units of flux.
- **Barrier ↔ Bank** and **Flux ↔ Bank** iso-P=0.50 surfaces both exist with finite rates.

So the reframing is **right that a tradeoff surface exists and can be computed with measurable
exchange rates** — its core methodological insight is correct — but **wrong that it holds at
fixed arbitrary persistence.** The surface is real only in the low-persistence regime where no
mechanism has yet hit its ceiling. Above the lowest ceiling, the mechanisms stop being
interchangeable and become strictly ordered (only barrier survives).

## What this licenses

- **Do not adopt the reframing's "three fungible currencies" as a canon claim.** It is false as
  stated (fails at P\*=0.80) and true only in a bounded regime — which is a *weaker and more
  interesting* claim than the reframing makes.
- **The reframing's real contribution stands:** substitutability-on-a-surface is the right kind
  of falsifiable content, and it is now demonstrated (GO would have been the boring outcome;
  this bounded NULL is more informative). The framework now has a computed tradeoff surface with
  exchange rates on a worked system — the thing the reframing correctly said was missing.
- **The four-axis canon and the Φ-individuation result are untouched** — this gate tested the
  economics claim, not the axis count, exactly as pre-registered.
- **A candidate canon claim, graded frontier:** *persistence mechanisms are substitutable only
  below the lowest single-mechanism ceiling; above it they are strictly ordered, with the
  equilibrium wall (Barrier) the sole unbounded mechanism.* This is new, computed, and falsifiable.

## Reproduce

`aop_substitutability_gate.py` (self-contained; rebuilds the (N+1)-state model, ceilings, and
iso-P surfaces). Figure `figS8_substitutability.png`. Numbers: flux ceiling 4/7 = 0.5714, bank
ceiling 0.705, barrier reaches 0.80 at b=0.817; iso-P=0.50 surface d f/d b ≈ −1.7.
