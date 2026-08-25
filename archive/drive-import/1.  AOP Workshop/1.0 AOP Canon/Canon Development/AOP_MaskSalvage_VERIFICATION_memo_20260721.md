# AOP — Semantic-Mask Salvage Diagnostic — Independent Verification Memo

**Verifier:** Claude Cowork (execution seat), independent re-execution for CP/Prime.
**Homework rule:** This session did not build `mask_salvage.py` or the diagnostic; it is a clean
verifier. Re-run, not read-over — the script was executed unmodified and its primitives were
additionally re-derived from scratch.
**Date:** 2026-07-21 · **Env:** Python 3.11.15, numpy 2.4.4, fresh cloud container.
**Provenance:** `mask_salvage.py` (`1GPcrRSySofAD_yZeCcPkpB_S53IOkrC_`), sha256
`20c02ca1243ca6cb8d4f6a174be13d1b2dd338771078132b658a24c82dbaf062`; diagnostic
`AOP_MaskSalvage_Diagnostic_20260721.md` (`1pS-BhdfUrPsqB7BXbcCGVdJHh9ZGXYvq`). Run log deposited
alongside.

Startup check — 2026-07-21: [✓] AOP Charter v1.2 (project instructions) · [✓] Canon read at
v1.20 via the deposited change-set docs (task is semantic-layer-internal; canon not edited) ·
[–] Ladder bridge memo not opened (cross-lane items only flagged, per §7 of the diagnostic) ·
Drive connector: on. No canon movement is proposed here — verification only.

---

## 1. Verdict at a glance

**The diagnostic reproduces.** All three headline claims reproduce exactly on a fresh run, and
the underlying primitives match an independent from-scratch re-derivation to every printed digit.
The two Prime-flagged probes return: **(a) no inversion — the pattern is merge-only**; and
**(b) the a\* ceiling is real and is not driven by a single adversarial extreme coalition, but it
is not a property of "plausible" small coalitions** — capping coalition cardinality at ≤2 (or
sparse random sampling) removes the ceiling entirely. Detail below.

## 2. Reproduced-vs-claimed (the three required checks)

| Claim in the diagnostic | Claimed | Reproduced (this run) | Status |
|---|---|---|---|
| Model 3 salvageable region non-empty & non-trivial (well-defined ∩ informative) | non-empty, extends into redundancy-dominated band | salvageable at a ∈ {0.1, 0.2, 0.3, 0.5, 0.75, 1.0, 1.5, 2.0, 3.0}; **salvageable AND Ω>0.1** at a ∈ {0.75, 1.0, 1.5, 2.0, 3.0} | **REPRODUCED** |
| Interval-merge point a\* and Ω there | a\* ≈ 3.4, Ω ≈ 0.81 | script grid a\* = **3.40**, Ω = **0.812**; interpolated crossing a\* ≈ **3.30** (grid-resolution difference only) | **REPRODUCED** |
| Disjoint-then-merge pattern | disjoint below a\*, merged above | disjoint (lo_L > hi_S) through a = 3.0; merge at 3.4; merged at 5.0, 8.0; **no re-emergence** | **REPRODUCED** |

The Model-3 result table (load/spec interval endpoints and Ω at each a) matches the diagnostic's
§4 table cell-for-cell (e.g. a=1.0: load [0.255, 0.549], spec [0.000, 0.077], Ω=0.22; a=3.0:
load [0.310, 0.973], spec [0.000, 0.286], Ω=0.73). Models 1 and 2 also reproduce (salvageable
across their full swept ranges), consistent with the diagnostic's framing of them as the
"cheap"/baseline cases where syntactic distance carries the load.

**Primitive re-derivation (independent, not importing the script):** at a=1.0, from-scratch
Σ=J⁻¹, V=−½logdet Σ[S,S], the LOAD marginal, W_total, and the O-information Ω all equal the
deposited module's outputs to 6 digits (W=1.060132, lo_L=0.255413, Ω=0.223144). The numbers are
closed-form, not estimator artifacts — consistent with the charter's "analytic, not estimated"
requirement.

## 3. Probe A — inversion or only merge? **(merge-only; no inversion)**

Across a fine a-sweep out to a=40 (K4, S={0,1}), the load-above-spectator ordering **never
inverts**. The full spectator interval never rises strictly above the load interval
(lo_S > hi_L is False everywhere), and the Shapley-mean ordering never crosses (sh_S > sh_L is
False everywhere; at a=40, sh_L=1.270 vs sh_S=0.163). What happens at a\* is strictly a **loss of
disjointness** — the intervals begin to overlap while load stays ranked on top. **No inversion
finding.** This is the benign case for the diagnostic: the mask degrades to "unresolvable," not
to "wrong-signed."

## 4. Probe B — is a\* real, or an extreme-coalition artifact? **(real, but cardinality-gated)**

Recomputing the per-edge interval over restricted coalition sets and relocating a\*:

| Coalition set used for the interval | a\* (merge point) |
|---|---|
| Full (all 2⁵ = 32 contexts) | **3.30** (≈ script's 3.4) |
| Cardinality \|C\| ≤ 0 (marginal only) | **no merge** in [0.2, 40] |
| \|C\| ≤ 1 | **no merge** |
| \|C\| ≤ 2 | **no merge** |
| \|C\| ≤ 3 | **3.30** (identical to full) |
| \|C\| ≤ 4 | **3.30** |
| Random 4 / 8 / 16-coalition sample per edge | **no merge** (all three) |

Reading: the merge is driven by the **spectator's maximum marginal, which sits at cardinality
\|C\| = 3** (not the fully-scrambled \|C\| = 5 extreme). So the ceiling is **not** an artifact of the
single most adversarial coalition — dropping only the top extreme leaves a\* unchanged, and it
appears the moment coalitions of cardinality ≥3 are admitted. **But** it is equally **not** a
property of "plausible," low-cardinality coalitions: restrict to \|C\| ≤ 2, or sample the coalition
space sparsely, and the ceiling vanishes — the mask then reads salvageable at every coupling
tested. The ceiling is a genuine **moderate-order redundancy** phenomenon, tied to admitting
contexts in which ~half the graph is already scrambled.

This does not overturn the diagnostic; it sharpens it. The diagnostic (§4, §6) explicitly commits
to the **full min–max interval** ("every coalition, including adversarial ones") as the honest
per-edge object, and already notes the Shapley-mean reading yields separation everywhere. Probe B
adds a third calibration point — a *restricted-coalition* interval also yields separation
everywhere below \|C\|=3 — and pins the ceiling's origin to cardinality-≥3 contexts.

## 5. One flagged imprecision (not verdict-changing)

The diagnostic's mechanistic gloss says the merge is set by the spectator's weight "when **all
support edges are scrambled**, so it becomes the last path holding the collective." The actual
merge-driving endpoint is at **\|C\| = 3**, not the all-others-scrambled \|C\| = 5 extreme. The
*direction* of the story (spectator's high-context marginal climbing to meet the load's
low-context marginal) is correct; the "all support edges" phrasing overstates the cardinality.
Recommend softening that clause to "when enough support edges are scrambled that it becomes a
near-last path (here \|C\|≈3)." Cosmetic; the verdict stands.

## 6. Grade

- **Three required reproductions — CONFIRMED / SETTLED-within-class.** Re-run reproduces the
  numbers, and an independent from-scratch re-derivation confirms the primitives. The
  interval-disjointness and its merge are tolerance-free closed-form facts on the static-Gaussian
  K4 class.
- **Diagnostic's overall verdict (intersection non-empty, non-trivial, bounded above by a
  redundancy threshold) — CONFIRMED, SYNTHESIS grade, with one added caveat.** The "bounded"
  clause survives the probes but is **coalition-set-dependent**: the ceiling exists under the full
  (and ≥3-cardinality) interval and disappears under a small-coalition reading. The diagnostic
  already flags the interval-vs-mean sensitivity in §6; Probe B extends that honesty caveat rather
  than contradicting it.
- **Probe A — CONFIRMED:** merge-only, no inversion (own finding: none).
- **Probe B — new sharpening:** a\* is robust to dropping the single extreme coalition but is gated
  at coalition cardinality ≥3; below that there is no ceiling. **FRONTIER-adjacent** — a candidate
  addition to §6 residuals if Prime folds anything.

**Scope of this verification.** Static-Gaussian K4 with S={0,1}, as deposited. a\* ≈ 3.3–3.4 and
Ω\* ≈ 0.81 are model-specific (the diagnostic says so). Nothing here is a claim about non-Gaussian
or non-stationary systems, and no canon movement is proposed — this is a reproduction check plus
two probes, handed back to the chat seat for the fold decision.

## 7. Bottom line for Prime

The deposited diagnostic is **sound and reproducible**. Recommend it may proceed to whatever fold
CP intends, with two small edits worth considering: (i) soften the "all support edges scrambled"
gloss to the actual \|C\|≈3 driver; (ii) add one line to §6 noting that the a\* ceiling is a
moderate-order (\|C\|≥3) redundancy effect — under a small-coalition interval it does not appear,
which is a stronger, more precise statement of the same "the interval is the strict reading"
caveat already present. Neither edit changes the verdict.
