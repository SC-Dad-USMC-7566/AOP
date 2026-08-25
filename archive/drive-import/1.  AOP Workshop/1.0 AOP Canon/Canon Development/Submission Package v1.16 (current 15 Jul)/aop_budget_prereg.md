# AOP Gate — Is Persistence a Conserved "Budget"? (PRE-REGISTRATION)

**Status: pre-registration. Exits frozen before computation. Two exits only: GO / NULL.**
_Drafted 2026-07-16. Follow-on to the substitutability gate (which returned NULL at fixed high
persistence, bounded-substitutability positive below the lowest ceiling). The reframing's
metaphor is that "persistence is a budget met in three currencies; the content is in the
exchange rates." This gate tests whether "budget" is a real, non-vacuous claim — i.e. whether
the substitution is path-independent in a way that actually constrains the framework._

---

## The trap this gate must avoid (pre-committed)

If persistence is a single scalar state function P(b, f, r), then the three pairwise exchange
rates along an iso-P surface are ratios of its partial derivatives:

  (∂f/∂b)|_P = −P_b/P_f,  (∂r/∂f)|_P = −P_f/P_r,  (∂b/∂r)|_P = −P_r/P_b,

and their loop product is **−1 identically**, for *any* smooth P, at *every* point. So "the
exchange rates are consistent / the loop closes / no arbitrage" is **forced by P being a state
function** and tests nothing about the framework — exactly the reachability failure the
gate-stakes analysis warned against. We therefore pre-commit: **if the loop-product test passes,
we first check whether it is forced-by-construction; if so it is graded VACUOUS and cannot by
itself yield GO.**

## The non-vacuous claim (frozen)

"Budget in three currencies" is only content-bearing if there is an **independent conserved
cost** — a single price paid to buy persistence, the same unit whichever mechanism spends it.
The one objective, model-independent cost available is the thermodynamic cost, entropy
production σ̇. So the real test:

**Is σ̇ a state function of persistence — i.e. constant along an iso-P surface?**
If persistence P is genuinely bought with a common currency, then reaching a given P costs a
definite amount of that currency regardless of the mechanism-mix, so σ̇ should be (near-)constant
on {P = const}. If instead σ̇ varies with mechanism-mix at fixed P, then persistence and cost are
independent axes and there is no single budget: the "currencies" are not priced in a common unit.

## Method (frozen)

Same (N+1)-state model as the substitutability gate (`aop_substitutability_gate.py`; N=6,
κ=1.0, basin={≥3}, knobs Barrier b / Flux f / Bank r). On the iso-P = 0.50 surface (the regime
where all three mechanisms participate, established last gate):

1. **Loop-product test (A).** At several points on the surface, compute the three pairwise
   exchange rates and their product. Report whether |product| = 1, AND whether that is forced by
   P being a scalar state function (check: does it hold at generic, non-special points?).
2. **Cost-as-state-function test (B).** Walk the iso-P = 0.50 surface from the barrier-dominated
   corner to the flux-dominated corner to the bank-dominated corner and record σ̇ at each point.
   Compute the spread of σ̇ at fixed P.

## Exits (frozen)

- **GO — persistence is a genuine conserved budget:** (A) holds *non-vacuously* AND (B) holds —
  σ̇ is (near-)constant on the iso-P surface (spread ≤ 10% of its mean). Persistence would then
  behave like a conserved budget with a real, mechanism-independent price.
- **NULL — no genuine budget:** either (A) holds only *vacuously* (forced by P being a scalar
  state function) while (B) fails (σ̇ spread > 10% at fixed P), OR (A) fails outright. In this
  case the "budget in currencies" metaphor is either trivial (it says only "P is a scalar") or
  false (the mechanisms share no cost unit).

## Why both exits are genuinely reachable

GO is reachable: a model in which every mechanism dissipated at the same persistence-efficiency
would show σ̇ ≈ const on iso-P. Nothing forbids that a priori. NULL is reachable and, by charter
skepticism, expected: Barrier is a passive equilibrium wall (σ̇ = 0) while Flux and Bank are
non-equilibrium (σ̇ > 0), so σ̇ likely varies from ~0 at the barrier corner to >0 elsewhere at
fixed P — no shared cost, no budget. We commit to reporting whichever way it falls.

## Decision rule

GO only if (A) non-vacuous AND (B) σ̇ spread ≤ 10% of mean on iso-P. NULL otherwise. No third
exit; a vacuous pass is not upgraded to a win.

## What a result licenses

- GO: persistence is a conserved budget with a real price — strong support for the reframing's
  metaphor, worth reconsidering the axis structure.
- NULL: the "budget" metaphor is trivial-or-false; it adds no constraint beyond "persistence is
  a well-defined scalar." Combined with the substitutability ceilings, this would settle that the
  mechanisms are neither fungible at high persistence nor priced in a common currency — a second,
  independent reason not to adopt the 4→3 reframing.
- Neither exit touches the four-axis canon or the Φ-individuation result.
