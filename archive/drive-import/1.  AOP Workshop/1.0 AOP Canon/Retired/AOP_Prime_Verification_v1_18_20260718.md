# Prime Verification — v1.18 against the v1.17 baseline

**Compiled:** 18 July 2026 by Claude (prime), after `FROZEN_aop_canon_v1_17.md` landed on Drive.
**Method:** downloaded both files, ran a full line diff, read every hunk, checked each against the v1.18 change log. Non-canonical record.

## Verdict: CLEAN construction, one content fix outstanding

**No silent drift.** Diff = 12 lines removed, 56 added, across a 24,182-word document. Every changed line maps to a logged edit. §4a, §9a, §11a, the five worked cases, all references, all figures are byte-identical. "Edited in place, not regenerated" is confirmed true. v1.18 = v1.17 + the logged edits, nothing else.

**The six P0 fixes landed and match the agreed dispositions:**

| P0 | Edit in v1.18 | Matches agreed? |
|---|---|---|
| P0-1 | §10 "manufactures a rest frame" -> "associated with"; "manufactures proper time" withdrawn; operational domain criterion added | Yes |
| P0-2 | §1 Drive -> "entropy-production rate, not free-energy throughput"; §2 Boundary & Integration reframed as panels (dependence/interdependence, not separation/unity); Integration proxy corrected to total correlation | Yes |
| P0-3 | none (confirmed absent) | Yes |
| P0-4 | subtitle "a system's own viability" -> "declared viability functional on the viable set... ownership-free" | Yes |
| P0-5 | §12 status column split into dependency × evidential; rule "passed binding check licenses at most conditionally-forced, never forced"; full re-grade in appended Table 3' | Yes |
| P0-6 | reconciled in Phase-0 artifacts (not manuscript text) | Per changelog |

The appended §12' (two-axis ledger) and §12" (declaration tuple + panels) are honest and strong — the ledger explicitly holds all but two rows below "forced," which is the correct posture for a living review.

## The one content fix: §11b overclaim (align prose to its own ledger)

§11b's prose claims the strength-vs-viability dissociation and the Möbius sign inversion are "*not* built in... the actual result." Prime's independent re-run this session disproves this: swapping the OR/AND gates flips the Möbius signs, so they are forced by the gate choice; the strength dissociation is forced by the hand-assigned rates. **§11b's own evidential tag ("forced by the construction") and the Table 3' row ("forced-by-construction") already concede this** — only the prose paragraph overstates. Fix = make the prose match the ledger.

**Patch — replace the "What is and is not claimed" paragraph in §11b:**

*Before:* "That {A,B} are redundant and {S1,S2} synergistic is built in — it is the benchmark's ground truth, not a discovery. What is *not* built in, and is the actual result: that structural strength anti-ranks viability importance, that the Möbius signs invert the naive reading, and that the substitution structure is recoverable — none of which a correlation- or rate-based method reports correctly."

*After:* "The ground truth is built in throughout: {A,B} redundant, {S1,S2} synergistic, Z inert, R load-bearing, and — because these are set by the gate topology and the rate assignments — the strength-vs-viability anti-ranking and the Möbius sign pattern follow from the construction (swapping the OR/AND wiring flips the Möbius signs). The benchmark is therefore a **competence check, not a discovery**: it shows the coalition-aware, viability-anchored method *correctly recovers* this designed structure on a system where a strength- or correlation-based reading inverts it. That is what a Perspective needs — a closed-form case where the four-target apparatus is demonstrably necessary to get the right answer — and no more than that. It does not establish that AOP is uniquely correct or beats every rival."

This aligns §11b with its own evidential tag and Table 3' row. It does not weaken the paper's real content — the competence claim survives; only the "could have come out otherwise" framing is corrected.

## Two minor pre-submission items (not drift)

1. **Section order:** §11b, §12', §12" are appended after §13, so numbering runs §13 -> §11b -> §12' -> §12" -> References. Reorder before submission (§11b after §11a; §12'/§12" after §12).
2. **Changelog wording:** it says "each visible status row retagged"; only three rows carry inline bracket tags, with the full retag in Table 3'. Cosmetic.

## What this does and does not settle

Settles: v1.18 is a trustworthy, drift-free evolution of v1.17, and can be treated as the working manuscript once the §11b prose is fixed and the sections reordered.

Does NOT settle: the benchmark is a competence check, so the open scientific question — a test whose ground truth is *not* set by the modeler, one the framework could actually fail — remains the top outstanding work.
