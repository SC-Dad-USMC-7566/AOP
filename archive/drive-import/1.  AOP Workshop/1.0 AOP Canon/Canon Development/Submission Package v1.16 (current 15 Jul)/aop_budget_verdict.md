# AOP Gate — Is Persistence a Conserved "Budget"? VERDICT

**Frozen exit: NULL** (pre-registration `aop_budget_prereg.md`, v1, exits committed before
computation). The reframing's metaphor — "persistence is a budget met in three currencies; the
content is in the exchange rates" — **is either trivial or false**: there is no
mechanism-independent price for persistence. The claim adds no constraint beyond "persistence is
a well-defined scalar."

## Test A — loop product of exchange rates: PASSES, but VACUOUSLY

On the iso-P = 0.50 surface, the three pairwise exchange rates multiply to **−1.000000** at every
tested point (two independent generic points checked). But this is **forced by construction**: if
persistence is any smooth scalar function P(b,f,r), the exchange rates are ratios of its partials
(−P_b/P_f)(−P_f/P_r)(−P_r/P_b) ≡ −1 identically. The loop "closing" therefore tests nothing about
the framework — it confirms only that P is a state function, which was never in doubt. Per the
pre-committed trap-check, a vacuous pass **cannot** yield GO.

## Test B — is the cost a state function of persistence? FAILS

Walking the iso-P = 0.50 surface and recording entropy production σ̇ at each point:

| point on iso-P=0.50 | σ̇ |
|---|---|
| barrier corner (b=0.428) | **0.000** |
| bar/flux midpoint | 0.829 |
| flux/bank midpoint | 0.890 |
| bank corner (r=0.411) | 1.158 |
| flux corner (f=0.804) | **1.313** |

**σ̇ spread at fixed persistence: 0.00 → 1.31, i.e. 157% of the mean** — vastly over the 10% GO
threshold. The *same* persistence P=0.50 costs zero dissipation if bought with the barrier and
1.31 if bought with flux. Cost is not a function of persistence; it depends entirely on the
mechanism-mix.

## Verdict: NULL — no genuine budget

Test A is vacuous, Test B fails. There is no single currency in which persistence is priced.
The barrier is a passive equilibrium wall that buys persistence for free (σ̇ = 0); flux and bank
are non-equilibrium mechanisms that pay a running dissipative cost. Two systems equally
persistent can have arbitrarily different thermodynamic cost — so "one budget, three
interchangeable currencies" is a category error at the level of *price*, just as the previous
gate showed it is at the level of *reachability* (ceilings).

## What this establishes, with the substitutability gate

The two gates together settle the reframing's central economic claim from both sides:
- **Substitutability gate:** the mechanisms are not fungible at high persistence — flux and bank
  have hard ceilings, only the barrier is unbounded (strict ordering above the lowest ceiling).
- **Budget gate:** even where they *do* substitute (below the ceiling), they are not priced in a
  common currency — identical persistence costs 0 to 1.31 in σ̇ depending on mix.

So the "budget in currencies" picture is neither true at high persistence nor meaningful as a
conserved cost. This is a **second, independent reason not to adopt the 4→3 reframing.**

What survives and is worth keeping: persistence *is* a well-defined scalar with a genuine (if
regime-bounded) substitution surface, and the **cost heterogeneity is itself a result** — the
thermodynamic price of persistence is mechanism-dependent, with the passive wall free and the
active mechanisms dissipative. That is a sharper statement of the Boundary-vs-Drive distinction
the four-axis structure already draws, now quantified on the iso-persistence surface.

## Reproduce

`aop_budget_gate.py` (reuses the substitutability model). Numbers: loop product −1.000000
(vacuous, holds at all points); σ̇ on iso-P=0.50 ranges 0.000 (barrier) to 1.313 (flux),
157% of mean.
