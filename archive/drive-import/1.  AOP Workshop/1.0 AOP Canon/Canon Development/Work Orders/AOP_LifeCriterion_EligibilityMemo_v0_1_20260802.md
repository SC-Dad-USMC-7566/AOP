# Gate 1, Step A — The eligibility question, stated before any candidate is scored

**Seat:** Claude Science (builder). **Date:** 2 August 2026.
**Parent freeze:** `AOP_LifeCriterion_DispositionRule_FROZEN_v1_0_20260801.md`, md5 `b7eebcfd5a371a78b33a5fe230d52554` (verified by independent download this session).
**Status:** Records file. Owns no AOP scientific claim. Does not adjudicate. Feeds the pre-registration; prime drafts that.

---

## Why this document exists

S.2 asks for "an identifiable slow variable that plausibly stores a target for the fast
regulated dynamics, and that is *not* simply a fixed point of the fast constitutive drift."
Applying that requires knowing what counts as *stores*. The follow-on supplies a formulation,
and read strictly it excludes the architecture class that contains prime's lead candidate.
Scoring candidates without settling this first would produce a selection whose verdicts flip
under a reading the pre-registration has not yet fixed. So the readings are stated here, both
are carried, and every candidate is scored twice.

**This is not a request for a fourth Ben decision.** It is a question the work order already
assigns to Gate 1: §4 makes the separability test a prerequisite for P1 and P2, drafted by prime
inside the pre-registration. This document hands prime a sharpened version of that question with
the candidate consequences priced.

---

## The text at issue

`AOP_LifeArchitecture_Followon_v0.1.md` §4, the invariant formulation:

> "a **proper invariant subspace whose dynamics are autonomous with respect to the regulated
> coordinates** — a subspace the dynamics preserve, evolving under its own law without being
> driven by the variables it regulates, while feeding into them."

The operative clause is *without being driven by the variables it regulates*. It is a
one-directional-coupling requirement: reference → regulated, and not back.

The follow-on's external support pulls the other way. §3 names Bich et al. 2016 as supplying
component (2) and calls it "the strongest external support the criterion has," and the property
it supplies is that the regulatory subsystem is "*dynamically decoupled* from the process it
regulates — operating at a different dynamical scale and under different constraints." A
different dynamical *scale* is a weaker condition than one-directional coupling: a slow
integrator driven by a fast error signal satisfies scale separation and violates autonomy.

The two supports are therefore not co-extensive, and the follow-on does not say which governs.

---

## Reading A — STRICT (autonomy)

**Test.** Let the state split into regulated coordinates *y* (fast) and candidate reference
coordinates *x* (slow). A candidate is eligible under Reading A iff the *x*-dynamics can be
written ẋ = f(x) — closed in *x*, with no functional dependence on *y* — up to the declared
grain, while *y*-dynamics depend on *x*.

**Admits:** free-running oscillators and other autonomous slow generators whose output is read
onto a regulated variable; stored discrete states (epigenetic, methylation-as-record) that are
written by something other than the regulation error.

**Excludes:** every **integral-feedback** architecture. In integral feedback the slow variable is
the integral of the regulation error, so ẋ = k·(y − y\*) depends on *y* by construction. This is
not a marginal case; it is the definitional form.

**Cost of Reading A.** It excludes prime's lead candidate (chemotactic methylation), every
synthetic antithetic controller, and most of what molecular biology calls robust perfect
adaptation. It leaves a narrow admitted class, which is either a virtue (the criterion is sharp)
or a defect (the criterion excludes the paradigm cases of biological regulation it was built to
capture). That is prime's call, not this seat's.

## Reading B — LOOSE (scale separation)

**Test.** A candidate is eligible under Reading B iff there is a slow variable *x* with (i) a
timescale separation from *y* of a declared magnitude, (ii) a load-bearing coupling x → y that
sets *y*'s operating point, and (iii) *x* addressable as a separate intervention target from the
machinery implementing the x → y readout. Feedback y → x is permitted.

**Admits:** integral feedback, and therefore chemotaxis, antithetic controllers, and the robust
perfect-adaptation literature generally.

**Cost of Reading B.** Scale separation is a magnitude, and P2 stakes the framework on the
discrimination being architectural rather than a magnitude of timescale separation. Reading B
puts a magnitude inside the eligibility condition. It does not automatically collapse P2 — the
P2 sweep is over the ratio *given* an admitted architecture, not over admission itself — but it
brings the two closer than the freeze's P2 language assumes, and an adversarial reader will say
so. **This is a place where OAI should be pointed deliberately.**

---

## The second question, which is separable and sharper

Under **either** reading, S.2's phrase "stores a target" needs a referent, and in integral
feedback there are two different objects competing for it:

| Object | What it is | Is it a stored state? |
|---|---|---|
| the integrator variable *x* | the running integral of past error | a dynamical state, yes — but its value is not the target |
| the target *y*\* | the zero of the integrator's rate law | a **kinetic parameter**, not a state |

In ẋ = k·(y − y\*), what the system holds in a slow degree of freedom is the *integral*; the
*set-point* is a constant of the rate law. So an integral-feedback system can satisfy "has a slow
separable variable" while failing "stores a target," because its target lives in the same place a
model-free corrector's does — in the kinetics.

This is the sharpest form of S.2, and it is what separates the candidate classes:

- **Target-as-parameter.** The slow variable integrates; the target is a rate-law constant.
  Moving the target means changing a kinetic parameter — which is also how you degrade the
  machinery. This threatens **S.3** (P1's independent perturbability) as well as S.2.
- **Target-as-state.** The slow variable's *value* is what the fast dynamics track, so the target
  is a state and can be moved by moving the state, machinery untouched. This is the shape S.3
  wants.

**Consequence for selection, stated in advance of scoring.** A candidate whose target is a
parameter is weak on S.2 and S.3 *under both readings*, independent of the autonomy question.
Candidates whose slow variable's value is itself the tracked reference are strong on both. The
autonomy question (A vs B) and the state-vs-parameter question are therefore **two filters, not
one**, and a candidate can fail either.

---

## What this seat does with the two readings

Every candidate is scored against S.1–S.5 twice, and each rejection names which reading it is
rejected under. Where the two readings disagree on a candidate, that disagreement is reported as
the operative finding rather than resolved by preference. A pair is proposed only if it clears
the criteria under a stated reading, and the reading is stated in the proposal.

**A prior expectation, recorded before retrieval so it can be scored against.** This seat expects
the strict reading to admit an autonomous-oscillator candidate and reject the adaptation
candidates, and expects the state-vs-parameter filter to be the harder of the two to pass. If
retrieval contradicts this, the contradiction is reported.

---

*End of eligibility memo. No candidate has been scored at the time of writing. No AOP quantity
computed. Not self-certified — prime verifies.*
