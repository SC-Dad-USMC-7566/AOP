# Gap 1 result — the resolvability × Integration tradeoff is a known, quantified law

## What AOP predicted (Section 13, currently unquantified)
As a system's Integration rises, a *per-component* semantic weight stops being a single number and
smears into a range; the *width* of that smear is what the framework actually forecasts as
measurable. AOP presents this as a qualitative tradeoff and, in v1.1, dressed it as
"uncertainty-relation-like" (v1.2 downgraded that to an explicit analogy).

## What the literature already contains (three independent fields, one phenomenon)
The disciplined-search rule paid off: this is not a new effect. Three peer-reviewed literatures
discovered and quantified it independently, under different names, and they agree to the letter.

- **Econometrics — multicollinearity / Variance Inflation Factor.** When predictors are
  correlated, per-coefficient standard errors inflate (Var β̂_i ∝ [R⁻¹]_ii) while the model's
  *predictive* power is untouched. Individual weights blur; the aggregate stays sharp. (This is
  the tangential/economics field the project ethos told us to look in — and it is the cleanest
  statement of AOP's own claim.)
- **Systems biology / physics — sloppy models (Sethna, Transtrum, Machta).** The Fisher
  Information Matrix eigenvalues span many orders of magnitude; "sloppy" parameter combinations are
  unconstrained (width ∝ 1/√λ_min) while "stiff" combinations and predictions are tightly
  determined.
- **Information theory — Partial Information Decomposition (Williams & Beer).** As sources
  synergize/become redundant, information ceases to be attributable to individual sources; the
  per-source weight becomes ambiguous (attribution-order / Shapley spread).

AOP's mask-resolvability × Integration tradeoff is the *same structural fact* these three express.
The right move for the paper is to cite this machinery, not to re-derive it — exactly the
"don't create when peer-reviewed work exists" discipline.

## The minimal model and the analytic law
A Gaussian with n=6 components and one Integration knob — equicorrelation ρ (off-diagonal of the
correlation matrix R). Everything is closed-form, so there are no estimator artifacts to contest.
- Integration is measured as **total correlation** TC = −½ ln det R (Watanabe 1960; a proper,
  cited multi-information measure of Integration), which rises monotonically as ρ→1.
- Per-component weight width (two ways): √VIF from R⁻¹, and 1/√λ_min of the FIM (=R).
- Aggregate (stiff-direction) width: 1/√λ_max.
- Attribution ambiguity (PID-flavored): spread between "added-first" and "added-last" per-component
  contributions to explained variance.

**Result.**
- Both per-component width measures diverge as **(1 − ρ)^(−1/2)** — the sloppy-direction width
  matches that law to a constant of 1.000; the VIF width rides the same divergence (ratio ≈ 0.91).
  For equicorrelation, λ_min = 1 − ρ exactly, so the divergence is analytic, not numerical luck.
- The **aggregate** stiff-direction width *shrinks* (1.0 → ~0.46 over the range): the whole gets
  **sharper** precisely as the parts become individually unresolvable.
- The independent PID/attribution-order spread **rises** monotonically with TC — third field, same
  signal.

So the prediction is not only true; it has a clean closed form (width ∝ (1−ρ)^{-1/2}, equivalently
∝ 1/√λ_min of the coupling matrix), and the "aggregate sharpens while parts blur" is exhibited in
the same model.

## What this does for AOP
1. **Section 13's prediction becomes concrete and cited.** "The measurable is the width a weight
   sweeps as integration rises" now has (a) a formula, (b) three independent literatures that
   already measure it, and (c) a worked minimal model. The paper graduates from "organizing scheme"
   to "organizing scheme with a quantified, borrowed-not-invented prediction."
2. **The honesty discipline is preserved and vindicated.** We did not stumble onto something new —
   we found that AOP's open prediction was independently established three times. That is the
   strongest possible outcome under the project's skepticism rule.
3. **New references to add** — verification pass COMPLETE (see aop_reference_audit.md, "Verification
   pass — the four new (Gap 1) references"). Status:
   - **Transtrum, Machta & Sethna, Phys. Rev. Lett. 104, 060201 (2010)** — VERIFIED (full text;
     "hierarchy of widths" confirmed verbatim). Ready for v1.3.
   - **Transtrum et al., J. Chem. Phys. 143, 010901 (2015)** (sloppiness review) — VERIFIED
     ("many small eigenvalues in the FIM ⇒ low effective dimensionality" confirmed). Ready.
   - **Williams & Beer 2010 (arXiv:1004.2515), PID** — VERIFIED ("unique information, redundancy,
     and synergy as the basic atoms of multivariate information" confirmed). Ready.
   - **Watanabe 1960, IBM J. Res. Dev. 4(1):66–82 (total correlation)** — bib CONFIRMED only
     (title/DOI/venue); no abstract or full text retrieved (closed access, fetch returned
     abstract:null). Safe as a definitional cite because total correlation is standard and
     uncontested, but its content was NOT read — weaker than the original audit's abstract-confirmed
     cases.
   - **Multicollinearity/VIF** — the phenomenon is textbook-certain, but the exact citation
     (e.g. Belsley, Kuh & Welsch 1980) is NOT yet verified; pick and confirm a canonical source
     before submission.

## Honest limits (for the referee)
- The (1−ρ)^{-1/2} law is exact for *equicorrelation*; general coupling gives width ∝ 1/√λ_min,
  which is the correct general statement. State the general form; use equicorrelation as the
  worked illustration.
- Gaussian is the maximally clean case (linear, analytic). The claim generalizes qualitatively
  (VIF/sloppiness/PID all extend beyond Gaussian), but the *closed form* is Gaussian-specific.
  Say so.
- "Integration" here is total correlation; AOP notes Integration has ≥6 inequivalent measures
  (Mediano). The tradeoff is robust to that choice in direction (all reasonable measures rise with
  ρ), but the exact exponent is tied to the TC/eigenvalue formulation. This is the honest scope.
