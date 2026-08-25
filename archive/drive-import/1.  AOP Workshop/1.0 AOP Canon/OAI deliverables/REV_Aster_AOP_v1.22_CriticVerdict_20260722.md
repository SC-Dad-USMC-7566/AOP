# AOP v1.22 Critic Verdict — §4 Scope and Figure MW Regrade

**Reviewer:** Aster / outside-critic seat  
**Date:** 22 July 2026  
**Status:** REVIEW MEMO — NON-CANONICAL; no source file edited  
**Work order:** `AOP_v1.22_CriticWorkOrder.md`

## Executive Summary

**Q1 verdict: exit (b). The retraction is under-scoped at §4, but the defect must be stated precisely.** The scalar minimum can remain mathematically well defined when the minimizing partition relabels; at the crossing, the value is single-valued while the argmin is set-valued and the derivative can kink. What fails is the claim that §4 is a “fixed-partition” coordinate. The deposited §4 gate exhaustively minimizes over partitions. It is a fixed-*system* or fixed-*grain* computation under a declared minimum-partition convention, not a fixed-partition computation. Consequently, the retraction’s general lesson applies inside §4 whenever the identity of the MIP is given an individuation reading, and normalization is part of the coordinate’s definition rather than a caveat needed only when partition identity “carries weight.” Edit R3 is directionally correct but insufficient.

The §4 axis does not need to be withdrawn. Its zero-calibration and the raw-convention model results survive. Its claim must be narrowed to: under a declared selector/normalization, Φ_MIP supplies a scalar minimum-cut irreducibility score for a fixed candidate system at a fixed grain; a change in the minimizing cut is not evidence of a change in individuality. The five-criterion gate should be reported as convention-scoped until its ordering claims are re-audited across the declared normalization family.

**Q2 verdict: exit (b), for incomplete propagation—not because the central regrade is wrong.** Figure MW is correctly demoted to a dynamical proxy-ablation diagnostic. Steady-state current, entropy production, and relaxation rate are not the paper’s mean-first-passage lifetime primitive; their response to edge scrambling does not establish causal necessity for continued existence. Section 11b legitimately becomes the closest viability-grounded computation because finite-horizon survival is a point on the exit-time survival curve. It earns only “constructed competence check,” not external validation, discovery, uniqueness, or a proof that the AOP apparatus is necessary in general.

The proposed master is not self-consistent after that regrade. Section 13 directly restores the old Figure MW reading; §11a falsely says its viability calculation works “exactly as in Figure MW”; Data Accessibility still calls MW a worked semantic mask; the abstract continues to call the declaration-sweep range the characteristic measurable without a surviving computation establishing the full range it names; and §11b contains stronger language that conflicts with its own competence-check disclaimer.

**Fold recommendation:** do not fold the proposed master as written. Grow the retraction through §4 and complete the Figure MW propagation edits. These are bounded corrections, not reasons to reject the AOP architecture.

## Critique

### Q1 — Why §4 is not ring-fenced

For a fixed candidate system and grain, the construction has the form

\[
\Phi_{\mathrm{MIP}}^{N}(\Sigma)
= \min_{P\in\mathcal P(\Sigma)} s_N(P,\Sigma),
\]

where \(P\) ranges over admissible bipartitions and \(N\) denotes the declared scoring or normalization convention. Even if two partitions tie at a relabel point, the minimum value remains one number. The optimizer can be non-unique without the optimized value being undefined. The reproduced result—continuous Φ_MIP with a derivative kink—is exactly what this distinction predicts.

That mathematical well-posedness does not rescue the present wording:

1. **“Fixed partition” is factually wrong.** Section 4 defines Φ_MIP by the least-disrupting bipartition; Data Accessibility says the gate exhaustively searches the MIP. A fixed-partition score would be \(\Phi_P\), not \(\Phi_{\mathrm{MIP}}\).
2. **The retraction’s lesson applies inside §4.** When the module cut yields to a singleton cut, the fact established is that the optimizer changed. If §4 reads the cut identity as revealing “one individual or many,” it commits the same inference the §13a retraction rejects.
3. **Normalization is constitutive, not optional.** Different normalizers select different minima. Therefore \(N\) belongs in the declaration tuple whenever Φ_MIP is reported, not only when someone later chooses to interpret the optimizer’s identity. The current defense—“magnitude ordering at a fixed partition is unaffected”—concerns a different object, because the advertised coordinate is defined after minimization.
4. **The gate results survive only at their demonstrated scope.** Exact zero on a block-decomposable system is robust. The reported gradedness, matched-budget one-vs-many separation, and individuation ordering survive in the convention actually computed. They have not thereby been shown invariant across alternative MIP conventions.

The under-scoping appears in the proposed master at:

- Masthead/version summary, line 15: “normalization robustness to magnitude at a fixed partition.”
- §4, line 143: “only for the one-vs-many question at a fixed partition.”
- §12 status ledger, line 636: “magnitude ordering at a fixed partition is normalization-robust within the minimum-cut family.”
- §13, line 775: “it resolves one-vs-many only for a fixed partition.”
- v1.22 changelog entry, line 990: “The Φ_MIP fixed-partition individuation axis is untouched.”
- Retraction changeset §3/R3/R4, which uses the same fixed-partition ring fence.

By contrast, §13a line 781 uses the correct category: a **fixed-system** fact. That should be the organizing distinction everywhere.

### Q2 — What Figure MW and §11b actually establish

#### Figure MW

The demotion is correct. Current, entropy production, and relaxation rate can be scientifically useful dynamical observables, but none is equivalent to survival probability or mean exit time. In AOP’s own framework their persistence signs are not even generically aligned: a measure-preserving current can shorten lifetime, entropy production can accompany either maintenance or destruction, and a faster relaxation mode does not by itself imply a longer first-passage lifetime. Scramble sensitivity therefore establishes sensitivity of those observables, not semantic weight in the paper’s stated viability sense.

MW still earns three modest claims:

- the intervention can be executed on the toy ring;
- an inert or already-balanced control returns zero;
- proxy sensitivities can be graded and declaration-relative.

It does **not** earn “load-bearing,” “causally necessary for continued existence,” “semantic mask computed,” or “characteristic measurable rendered.”

#### Section 11b

Section 11b is better aligned with AOP’s primitive. If \(T_{\rm exit}\) is the exit time, its functional is \(S(\tau)=P(T_{\rm exit}>\tau)\). That is genuinely viability-grounded and is related to the mean lifetime by

\[
E[T_{\rm exit}] = \int_0^\infty S(t)\,dt.
\]

But a value at one or several finite horizons is not itself the mean lifetime, and the model’s topology and rates manufacture the answer key. Section 11b therefore demonstrates correct recovery of a designed survival structure. It does not establish empirical validity, discover the structure, prove AOP uniquely necessary, or show performance on ground truth set outside the modeler.

The proposed master acknowledges this at §3 line 125 and §11b line 587, but over-credits the gate elsewhere:

- §11b line 581 says the apparatus is “necessary” to get the right answer. The computation defeats the named strength/correlation baselines; it does not prove necessity against all alternatives.
- §11b line 585 is headed “The result that could have come out otherwise,” even though line 587 concedes that the anti-ranking and Möbius pattern follow from the designed topology and rates.
- The same paragraph calls the substitutability “not built in.” That requires a separate preregistration/provenance showing; it cannot coexist unqualified with the general built-in-answer-key disclaimer.

### Dangling-reference inventory after the MW regrade

The following current-body passages require cleanup:

1. **Abstract, line 19 — two computations / characteristic measurable.** It says the semantic mask is computed in “two deliberately scoped demonstrations,” although one is now expressly not viability-grounded. It later calls the range across partition, resolution, and viability “the framework’s characteristic measurable.” That may remain a synthesis target, but the full range named is not established by MW or by the single-declaration §11b check. Recast it as a proposed declaration-sweep object unless a genuine viability-grounded sweep is cited.
2. **§3, line 123 — “The mask is computed here in two … demonstrations.”** The paragraph’s next sentence denies that MW is a persistence test. Call these two ablation calculations, only one of which computes a viability-grounded semantic mask.
3. **§11a, line 494 — “exactly as in Figure MW.”** False after regrade. Figure LT uses an explicit present-tense viability functional; MW uses three dynamical proxies. The shared operation is scrambling an edge, not the semantic interpretation of the output.
4. **§11b, lines 581 and 585 — necessity / could-have-come-out-otherwise language.** These conflict with the competence-check limitation at line 587.
5. **§13, line 775 — direct contradiction and highest-priority cleanup.** It calls MW a semantic mask with an explicit present-tense viability functional, calls its edges load-bearing, and says the interval is the framework’s characteristic measurable. Every one of those descriptions reinstates the pre-regrade reading. The same long paragraph also promotes the coupled-Gaussian mask-salvage result despite the v1.22 masthead saying that result was not folded.
6. **Data Accessibility, line 791 — “worked semantic mask … Figure MW.”** The same line later correctly calls the outputs proxy sensitivities. The opening inventory must use the corrected label.

Two historical occurrences survive in the append-only version record: the v1.11 masthead history at line 15 and the v1.10 revision entry at line 889 describe MW as the worked semantic mask. They are historical statements about what those versions claimed, not current scientific assertions. Do not rewrite them. The v1.22 changelog should explicitly record that the earlier characterization was regraded, which the proposed entry already does.

The following passages are consistent and should not be swept up unnecessarily:

- §3 line 125 correctly calls §11b a competence check with a built-in answer key.
- §5 line 264 describes declaration-sweep width as a diagnostic and future measurement task; it does not claim MW established it.
- §12 line 624 and Table 3′ line 754 correctly separate proxy diagnostic, competence check, and open external validation.
- Data Accessibility line 791’s later description of MW as proxy sensitivities is correct; only its opening label dangles.

## Actionable Fixes

### Priority 1 — Extend the retraction through §4

1. Replace every live “fixed-partition” defense with **“fixed candidate system at a fixed grain, under a declared MIP scoring/normalization convention.”**
2. In §4, distinguish the scalar minimum from the identity of its optimizer. State that the scalar may remain well defined and continuous through a relabel while the minimizing cut is non-unique at the crossing.
3. Make the normalizer \(N\) mandatory whenever Φ_MIP is reported. Do not condition that declaration on whether partition identity is later interpreted.
4. State explicitly that MIP identity is a least-disruptive-cut diagnostic, not by itself an individuation event.
5. Scope the five-criterion gate to the raw/declared convention actually tested. Retain zero-calibration; audit the other ordering claims across normalization conventions before calling them convention-robust.
6. Propagate the same correction to the §12 ledger, §13 outlook, masthead summary, v1.22 changelog, and the retraction changeset’s “what survives” section.

### Priority 2 — Complete the Figure MW propagation

1. Reserve **semantic weight** for an intervention evaluated with a declared viability functional. Call MW’s outputs **proxy sensitivities**.
2. Rewrite the abstract and §3 to say that MW tests proxy-ablation mechanics and §11b is the sole viability-grounded mask competence check in the present paper.
3. Remove the “exactly as Figure MW” claim from §11a; compare only the common intervention form.
4. Replace the opening of §13 line 775. Do not call MW’s intervals semantic weights, load-bearing edges, or the characteristic measurable. Remove the unfurled mask-salvage result from the proposed master if it is genuinely parked.
5. Fix the Data Accessibility inventory label.
6. Narrow §11b’s “necessary,” “could have come out otherwise,” and “not built in” language to recovery of a deliberately designed answer key against the named naive baselines.

### Priority 3 — Align the competence check with the lifetime primitive

For a later version, evaluate the full survival curve \(S(t)\) under each intervention and integrate it to obtain \(\Delta E[T_{\rm exit}]\). That would turn §11b from a finite-horizon viability check into a direct lifetime-grounded competence check without pretending it is external validation.

## Creative Opportunities

The cleanest long-term repair is terminological and mathematical:

- **Proxy sensitivity:** \(a_e(Q,D)\), the change in any declared observable \(Q\) after scrambling edge \(e\).
- **Semantic weight:** \(w_e(V,D)\), the change only when \(V\) is a declared viability functional.
- **Declaration sweep:** \(W_e=\{w_e(V,D):D\in\mathcal D\}\), the range or distribution of semantic weight across admissible declarations.

That three-level hierarchy preserves MW as useful evidence, keeps §11b honest, and gives “characteristic measurable” a precise future target rather than letting one phrase slide among three different objects.

For Φ_MIP, the parallel distinction is equally valuable:

- **partition score** \(\Phi_P\): value at a declared fixed cut;
- **minimum value** \(\Phi_{\rm MIP}^{N}\): scalar after optimization under declared convention \(N\);
- **optimizer identity** \(\operatorname{argmin}_P\): potentially set-valued and liable to relabel.

The v1.22 retraction becomes much stronger once those three objects are named separately. Most of the present confusion comes from moving among them without changing notation.

## Final Verdict for the Fold Gate

- **Q1: (b) — under-scoped.** Extend the retraction into §4 and its propagated summaries. Preserve the scalar axis only in a fixed-system/fixed-grain, convention-declared form; withdraw the fixed-partition defense and any individuation reading of optimizer identity.
- **Q2: (b) — central regrade correct, propagation incomplete and §11b modestly over-credited.** MW remains a proxy-ablation diagnostic; §11b remains a constructed finite-horizon viability competence check. Clean the six current-body passages listed above before fold.

**Recommendation to Ben:** yellow/red for the proposed master as written; green after the bounded Q1 scope repair and Q2 propagation cleanup are independently checked. The live v1.21 master should remain untouched until then.

