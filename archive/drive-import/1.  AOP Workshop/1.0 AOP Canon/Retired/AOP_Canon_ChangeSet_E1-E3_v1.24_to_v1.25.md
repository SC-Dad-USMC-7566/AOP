# Consolidated Canon Change Set — E1–E3, v1.24 → v1.25

**Issued by the execution seat (Cowork), 23 July 2026, for prime to verify. Not self-blessed. Master is placed by Ben.**
Drafting/editing only — **no new computation**; E1/E2/E3 numbers were verified by prime. Every edit is an honesty/precision fix: **no claim retracted, none strengthened.**

- **Base:** `AOP_CANON_MASTER_v1.24.md` — SHA-256 `3e64ff0ca93eee3165d53520651dfbbac063489df1ccfa87e3c8242f0dd421cf`, 218,602 bytes.
- **Seven edits, five anchors** (three co-located on §4 line 189). Each OLD verified to occur **exactly once** in v1.24; applying all seven composes without overlap. Guards below.

**Coherence (the single statement all three B–I spots now agree on):** *Boundary and Integration dissociate generically (both corners populated) but are not free — they share substrate through the exact nesting identity `TC = I(in;out) + TC_in + TC_out`, whose correlational footprint is ensemble-specific (≈0.83 in the VAR(1)/Figure-T ensemble, near-zero in the phaseE1 interface ensemble).* The abstract (E1-A), §4 body (Task-A + E1-B), and Figure T caption (Task-A) are edited to say exactly this.

---

## Edit 1 — [E1-A · abstract, line 17] "by construction" → "generically" · **SYNTHESIS / analytic-model-result**
**WHY:** C1 shows both dissociation corners populated across random Gaussian systems (deposited `phaseE1`). Consistent with Task-A: "generically … but not free."

**OLD:**
```
while Boundary and Integration are dissociable only by construction and otherwise share a plane through an exact nesting identity, so the honest claim is four distinguishable axes, not four independent ones.
```
**NEW:**
```
while Boundary and Integration dissociate generically across random Gaussian systems — both dissociation corners (sealed-yet-integrated and leaky-yet-unintegrated) are populated and Boundary’s own content still spreads when Integration is held high (deposited `phaseE1`) — even though the cross-cut slice B5 = I(inside;outside) remains an algebraic component of Integration, so the honest claim is four distinguishable axes, not four independent ones.
```

---

## Edit 2 — [Task-A · §4 body, line 189, sentence 1] scope the generic ~0.83 · **honesty / DEFECT-fix**
**WHY:** the ≈0.83 is ensemble-specific, not a generic property; the "not free" side rests on the exact nesting identity (stated in the very next sentence, **untouched**), not on a generic correlation. The 0.83 is **scoped, not deleted.**

**OLD:**
```
yet across generic systems the two are positively correlated (~0.83) because both are static mutual-informations read off the same covariance matrix.
```
**NEW:**
```
yet they are not independent either: Boundary’s cross-cut slice is a component of Integration (the exact nesting identity stated next), so the two share substrate — and the correlational footprint of that sharing is ensemble-specific (≈0.83 in the VAR(1) systems of Figure T; ~0.01 in the phaseE1 interface-Gaussian ensemble, and only ~0.14 even with the interface F removed so the nesting is exact — deposited `phaseE1`).
```
**GUARD:** the following sentence — `This substrate-sharing is exact, not merely a correlation: total correlation decomposes as TC = I(inside;outside) + TC_inside + TC_outside (verified to machine precision, maximum error 1.8×10⁻¹⁵ over 4000 systems)…` — is **not touched.**

---

## Edit 3 — [Task-A · §4 body, line 189, sentence 2] fix the misattribution · **honesty / DEFECT-fix**
**WHY:** "the ≈0.83 is the nesting identity showing through" is a misattribution — the identity holds exactly even where the correlation is ~0. The reason Boundary earns a separate line rests on the **identity**, not the correlation. 0.83 retained (scoped).

**OLD:**
```
The ≈0.83 Boundary–Integration correlation is this nesting identity showing through, and it is why Boundary earns a separate line only where the cross-cut slice specifically carries persistence weight — reported otherwise, it double-counts a piece already inside Integration.
```
**NEW:**
```
The nesting identity — not that ensemble-specific ≈0.83 correlation, which can fall to near-zero while the identity holds exactly — is why Boundary earns a separate line only where the cross-cut slice specifically carries persistence weight; reported otherwise, it double-counts a piece already inside Integration.
```

---

## Edit 4 — [E1-B · §4 body, line 189, end] deposit + name Boundary's axis content · **SYNTHESIS / analytic-model-result**
**WHY:** name B1+B2 as Boundary's axis-defining content; B4=σ_hk, B5=I(in;out) are the D→B and I→B edges; cite the deposit. Stands as drafted (consistent with Edits 1–3).

**OLD:**
```
Figure T shows the reachable volume and the constructed corners.
```
**NEW:**
```
Figure T shows the reachable volume and the constructed corners. A random-Gaussian ensemble (≥4000 systems spanning sealed→leaky; deposited `phaseE1`) confirms the dissociation is generic, not merely constructible: both corners — sealed-yet-integrated (B2 low, TC high) and leaky-yet-unintegrated (B2 high, TC low) — are populated, and B1 (interior/exterior state contrast) and B2 (the screening residual) each retain a spread at least their own median within the top-Integration quartile. Boundary’s axis-defining content is therefore B1 and B2; B4 = σ_hk and B5 = I(inside;outside) are the D→B and I→B edges read at the interface, and the carving’s B–I independence rests on B1 and B2, which carry variation that is not an additive part of Integration.
```

---

## Edit 5 — [Task-A · Figure T caption, line 191] scope the ~0.83 in the caption · **honesty / DEFECT-fix**
**WHY:** rest the shared-plane claim on the identity; scope the caption's 0.83 to the VAR(1) ensemble and note it is ensemble-specific. 0.83 retained.

**OLD:**
```
Boundary and Integration share a plane (corr ≈ 0.83) because both are static cuts of one covariance.
```
**NEW:**
```
Boundary and Integration share a plane through the exact nesting identity — Boundary’s cross-cut slice I(inside;outside) is a component of Integration — so the shared plane rests on the identity, not on a correlation whose magnitude is ensemble-specific (corr ≈ 0.83 in these VAR(1) systems; near-zero in the phaseE1 interface-Gaussian ensemble).
```

---

## Edit 6 — [E2 · §13, line 773] sharpened: lead with the ceiling; referent resolved · **SYNTHESIS, computed**
**WHY (Task B):** the PASS region is *weakly* integrated (Φ_MIP ∈ [0.0003, 0.05], near-zero individuation). The NEW text now **leads with the ceiling** — well-defined ∧ informative only in a weak-to-moderate band, blurring out *before* strong integration (life, the star) — and states "not trivial" second. The h_e referent question is **resolved: confirmed by prime** (VIF = diag(Corr⁻¹); the state-correlation reading is the faithful — and harder — referent, vs. the degenerate precision reading), so the change set carries no open "please confirm."

**OLD:**
```
realizing the Section 6 resolvability limit on the mask’s own weights rather than on a separate model [deposited]. Like Figure MW it is a demonstration of self-consistency, not a test that could fail
```
**NEW:**
```
realizing the Section 6 resolvability limit on the mask’s own weights rather than on a separate model [deposited]. A sweep over three topologies (chain, mean-field, sparse-random; deposited `phaseE2`) bounds where the per-edge mask is usable, and the bound is tight: it is simultaneously well-defined (resolvable to within a factor of two — state-correlation condition number κ ≲ 9) and informative (the load-bearing/inert gap exceeds three times the blur) only in a weak-to-moderate integration band — total correlation up to ≈0.5 but with Φ_MIP ∈ [0.0003, 0.05], i.e. near-zero individuation — and it blurs out before strong integration is reached: the informative gap is swamped first, then the weight becomes unresolvable, so the mask does not reach the strongly integrated regime (life, the star) it was built to describe. The one thing it is not is trivial: this usable band lies above the near-separable triviality floor (total correlation above the 5%-coupling floor), so the mask is not confined to trivial cases — only to weak-to-moderate integration. Like Figure MW it is a demonstration of self-consistency, not a test that could fail
```

---

## Edit 7 — [E3 · §11a, line 654] sharpened: foreground "up to V"; state the (2b) toy-scope · **FRONTIER, computed**
**WHY (Task B):** make "up to V" load-bearing — the detector finds a decoupled, load-bearing **set-point**, and it is **V that certifies it as viable** (no detection of life without a declared V). State that (2b) "separable from the fast regulated path" is operationalized as "not the regulated node," which isolates the reference only because the OU toy has no non-reference nodes — so positive detection is model-class-scoped. Attribution + model-class caveats retained.

**OLD:**
```
A demonstration of self-consistency, not a falsifiable test. Threshold location is graded, not a bright line
```
**NEW:**
```
A demonstration of self-consistency, not a falsifiable test. Beyond self-consistency, the criterion is positively detectable from third-person access — but only up to the declared viability functional V, which is load-bearing, not a footnote: the procedure detects a decoupled, load-bearing set-point, and it is V that certifies that set-point as the system’s viable target, so there is no detection of life without a declared V. On an OU star↔cell interpolation a graph-plus-V procedure (load-bearing by edge ablation; decoupling by a do-intervention that shifts x’s set-point, plus structural separability of the reference) flags the cell alive and rejects the star, and the verdict is architectural — invariant to the reference/regulated timescale ratio across three orders of magnitude, matching Figure LT-T (deposited `phaseE3`). Two scopes bound this: (i) “separable from the fast regulated path” is operationalized as “not the regulated node,” which isolates the reference only because the OU toy has no non-reference nodes — so positive detection is scoped to that model class; and (ii) with more than one symmetric decoupled reference, aliveness is still detected without a label but which node is the model is not uniquely attributable from the graph and V alone. Threshold location is graded, not a bright line
```

---

## Guards / verification (run against v1.24; prime to reproduce)
- **Anchors:** all seven OLD strings occur **exactly once** in v1.24; the three §4 line-189 edits are non-overlapping substrings and compose cleanly.
- **0.83 retained, not deleted:** the token `0.83` survives in all four of its edited/adjacent occurrences (scoped to its ensemble in each).
- **Identity untouched:** `TC = I(inside;outside) + TC_inside + TC_outside … 1.8×10⁻¹⁵ …` is byte-identical (not inside any edit span).
- **Invariant multiset:** citation set unchanged (added {} / removed {}); formal grade-tag set (SETTLED/SYNTHESIS/FRONTIER/…) unchanged (added {} / removed {}). New numeric tokens appear only inside intended spans and are already-verified deposit numbers: `~0.14` and `~0.01` (E1 correlations, prime-supplied / phaseE1), and `κ ≲ 9`, `Φ_MIP ∈ [0.0003, 0.05]`, `≈0.5` (E2, deposited `phaseE2`).
- **No computation performed;** numbers are quoted from the verified E1/E2/E3 deposits.

## Fold note (for prime → v1.25)
On adoption, this becomes **v1.25**: masthead version token + compile date restamped, and a v1.25 changelog entry appended in house style (canonicalized from v1.24; E1–E3 folded — B–I generic-dissociation deposit and ~0.83 scoping; mask weak-to-moderate-band ceiling; life criterion positively detectable up to V; honesty/precision only, no claim strengthened). Not drafted here — flagged so it isn't missed at fold time.
