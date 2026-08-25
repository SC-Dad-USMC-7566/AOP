# Work Order — E1–E3 change-set finalization (follow-up)

**Issued by the chat seat (prime), 23 July 2026, for the execution seat (Cowork).**
Prime has verified all three probes by re-running: E1/E2/E3 reproduce exactly and the operationalizations
hold up (the E2 correlation-matrix referent and the E3 ablation choice are both confirmed sound). This is a
**drafting/editing task only — no new computation.** Deliver a consolidated change set for prime to verify;
the master is placed by Ben. Then we fold E1–E3 into **v1.25** and send that to Aster.

## Startup
```
Startup check — [date]
[ ] AOP Charter — v1.2
[ ] AOP Canon — v1.24 (SHA-256 3e64ff0ca93eee3165d53520651dfbbac063489df1ccfa87e3c8242f0dd421cf, 218,602 bytes)
Drive connector: [on/off]
```
Canon Development: `1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`.

---

## Task A — draft the ~0.83 scoping fix (the one thing E1 flagged but did not draft)

Prime's independent check confirmed the tension and made it sharper: the algebraic nesting
`TC = I(in;out) + TC_in + TC_out` is robust and always true (verified to 1.8×10⁻¹⁵), **but the ≈0.83
correlation is ensemble-specific** — even with F removed so that B5 is *literally* an additive component of
TC, the B5–TC rank correlation is only ~0.14 (and ~0.01 in the phaseE1 interface ensemble). So the identity
holds in ensembles where the correlation is near-zero; the canon's claim that "the ≈0.83 is this nesting
identity showing through" is a **misattribution**, and "across generic systems ~0.83" over-generalizes.

**The fix (two locations — draft verbatim OLD→NEW against v1.24):**

- **§4 body, line ~189.** Reframe the two sentences that (i) assert a generic ~0.83 and (ii) attribute it to
  the identity. Target sentences:
  - "…yet across generic systems the two are positively correlated (~0.83) because both are static
    mutual-informations read off the same covariance matrix."
  - "The ≈0.83 Boundary–Integration correlation is this nesting identity showing through, and it is why
    Boundary earns a separate line only where the cross-cut slice specifically carries persistence weight…"
  Rewrite so that: the **algebraic nesting** carries the weight (B5 is a component of Integration — retained
  verbatim); the **correlation magnitude is declared ensemble-specific** (≈0.83 in the VAR(1)/Figure-T
  ensemble; near-zero in the phaseE1 interface-Gaussian ensemble, and only ~0.14 even when F is removed so
  the nesting is exact — deposited `phaseE1`); and the reason Boundary earns a separate line (B5
  double-counts a slice of Integration) rests on the **identity**, not the correlation. **Do not delete the
  0.83** — scope it to its ensemble. **Do not touch** the algebraic-identity sentence (TC = I(in;out) +
  TC_in + TC_out, 1.8×10⁻¹⁵).

- **Figure T caption, line ~191.** The caption states "Boundary and Integration share a plane (corr ≈ 0.83)
  because both are static cuts of one covariance." Scope the 0.83 to *this* (VAR(1)) ensemble and note the
  correlation is ensemble-specific (near-zero in the phaseE1 ensemble); the shared-plane claim rests on the
  identity, not this correlation.

- **Consistency check.** Reconcile this with the E1-A abstract edit ("dissociate generically"): the coherent
  statement across all three spots is *Boundary and Integration dissociate generically (both corners
  populated) but are not free — they share substrate through the exact nesting identity, whose correlational
  footprint is ensemble-specific.* Make the abstract, §4 body, and Figure T caption agree on that.

Grade: **honesty/DEFECT-fix — no claim retracted, none strengthened** (the substrate-sharing claim is moved
onto the robust algebraic fact).

---

## Task B — two sharpenings to the existing E2 and E3 change sets

- **E2 change set — lead with the ceiling, and mark the referent confirmed.** The PASS region is *weakly*
  integrated: **Φ_MIP ∈ [0.0003, 0.05]** (near-zero individuation). Revise the NEW text so the ceiling leads,
  not "salvageable": state the mask is well-defined ∧ informative only in a **weak-to-moderate** band and
  blurs out *before* strong integration — the regime (life, the star) it was built to describe. Keep "TC up
  to ~0.5" but pair it with the Φ_MIP range so "moderate" is not read as "strongly integrated." Also: the
  change set's open request for prime to confirm the h_e referent is now **resolved — confirmed by prime**
  (VIF = diag(Corr⁻¹), so the state-correlation-matrix reading is the faithful referent, and it is the
  *harder* choice than the degenerate precision reading). Update that note from "please confirm" to
  "confirmed by prime."

- **E3 change set — foreground "up to V," and state the (2b) scope.** Make explicit that the detector finds a
  decoupled, load-bearing **set-point**, and it is **V that certifies the set-point as viable** — E3 does not
  detect life without a declared viability functional; "up to V" is load-bearing, not a footnote. Also state
  that (2b) "separable from the fast regulated path" is operationalized as "not the regulated node," which
  isolates the reference only because the OU toy has no non-reference nodes — so positive-detection is scoped
  to that model class (keep the existing attribution and model-class caveats).

E1's two edits (E1-A, E1-B) stand as drafted — no change beyond ensuring consistency with Task A.

---

## Deliverable & flow
- One **consolidated change set** `AOP_Canon_ChangeSet_E1-E3_v1.24_to_v1.25.md`: verbatim OLD→NEW for E1-A,
  E1-B, E2 (sharpened), E3 (sharpened), and the new Task-A 0.83 fix (§4 body + Figure T caption), each
  graded, each mapping to a unique v1.24 anchor. Write to Canon Development via `base64Content`. **Do not edit
  the master.**
- Deliver for **prime to verify** (anchors map, reframes honest, no other claim moved). On Ben's decision we
  fold to **v1.25** and send to Aster.
- No new computation; the E1/E2/E3 numbers are already verified. Grade every edit; nothing is strengthened —
  these are honesty/precision fixes.
