# Aster Red-Team Review — Moving-MIP Proposal and Ptaszyński–Esposito Line-Check

**Date:** 21 July 2026  
**Reviewer lane:** external critique; non-canonical  
**Decision owner:** Ben  
**Builder:** Claude Science  

## Files actually reviewed

- `AOP_MovingMIP_Build_proposal_20260721.md` — current corrected file, Drive id `11R62Um47k070-pifCFDg3CMO3cVjGamf`
- `phaseE_movingMIP.py` — current corrected file, Drive id `1uXvn4IQKRGXetzOJIGZE5EG7jr834jM0`
- `phaseE_movingMIP_fig.png` — current corrected figure, Drive id `1JAXSneQkBFUQUXS-aPemZS9TgOYk8t4y`
- `AOP_LineCheck_PtaszynskiEsposito_20260721.md` — Drive id `13v_CB79dF6y-930Bg8esCKTOB9C-ym3_`
- `AOP_Canon_ChangeSet_v1.20_to_v1.21_rev2_20260721.md` — Drive id `13hDBhwnDgB4n-VOng1s5iKGK-mmB7EJO`
- live `AOP_CANON_MASTER_v1.20.md` — Drive id `1EB8F4L6K1WiHsuaw3htm7MsvfHtzSsZz`

The cited primary sources were independently checked where they bear directly on the verdict, especially Froyland–Koltai and Ptaszyński–Esposito. The three stale pre-correction moving-MIP files remain beside the current versions in Canon Development at the time of this review.

## 1. Executive Summary

### Verdicts

| Deliverable | Verdict | Canon consequence |
|---|---|---|
| Moving-MIP as a research direction | **YELLOW** | Worth repairing and testing; there is a legitimate temporally regularized partition-path proposal here. |
| Moving-MIP as closure of the principal FRONTIER item | **RED** | Do **not** move §4, §9a, or §13a from FRONTIER to SYNTHESIS on this deposit. |
| Claim that the AOP object was already solved independently in three fields | **RED** | The sources support analogies and reusable machinery, not identity of the objects or independent three-field solution of AOP's Φ problem. |
| Ptaszyński–Esposito line-check | **GREEN with one wording refinement** | It supports D2 v3's model-scoped feasibility constraint and removal of the D→I tendency arrow. |

The moving-MIP deposit contains a useful core: given the newly defined objective

\[
J_\lambda[P_{0:T}]=\sum_t \Phi(\Sigma_t,P_t)+\lambda\sum_t \operatorname{rot}(P_{t-1},P_t),
\]

dynamic programming finds its minimizing hard partition path exactly. That is a defensible proposed regularization of instantaneous MIPs.

It does not yet close the canon's open problem. The deposit currently conflates four different claims: defining a new regularized objective; solving that chosen objective; constructing a spectral analogue; and showing that either deserves to be called time-extended \(\Phi_{\mathrm{MIP}}\). Only the second is established. Worse, the reported “moving-MIP score” excludes the relabeling penalty that defines the objective, and the figure visibly contradicts the text's continuity claim. The spectral operator is neither derived as a relaxation of the discrete objective nor tied to the Gaussian total-correlation deficit. Its apparent lifetime readout is parameter- and threshold-dependent and, in this test graph, does not coincide with the underlying graph's spectral transition.

The Ptaszyński–Esposito memo is substantially sound. It preserves the load-bearing limitations: permutation invariance, discrete-state stochastic units, the technical meaning of robustness, and the open status of lattice/disordered generalizations. D2 v3 uses the source appropriately as a narrow feasibility constraint, not a causal arrow or tendency.

## 2. Critique

### 2.1 Stop-ship: the code does not report the objective it optimizes

`moving_mip` optimizes the total dynamic-programming cost containing `lam * R`, but returns

```text
score = mean(D[t, path[t]])
```

with the switching penalty omitted. Consequently, at \(\lambda=0.05,0.1,0.2\) it reports the per-slice lower bound `0.1655` even though the selected path incurs positive relabeling cost. On the 21-slice window, independent reproduction gives:

| \(\lambda\) | returned deficit-only mean | actual optimized \(J_\lambda/T\) | change events | Hamming rotation cost |
|---:|---:|---:|---:|---:|
| 0.05 | 0.16546 | 0.17023 | 1 | 2 |
| 0.10 | 0.16546 | 0.17499 | 1 | 2 |
| 0.20 | 0.16546 | 0.18451 | 1 | 2 |
| 0.40 | 0.16546 | 0.20356 | 1 | 2 |
| 0.45 | 0.20687 | 0.20687 | 0 | 0 |

This explains panel B: the plotted quantity jumps from about `0.1655` to `0.2069` near \(\lambda=0.45\). The title says “not a jump,” and the proposal says the score is continuous. The figure shows the opposite.

The minimized full objective is continuous, monotone, and piecewise linear in \(\lambda\), because it is the pointwise minimum of finitely many affine path costs. The chosen hard path can still jump at breakpoints. The returned deficit-only component is stepwise and is not the optimized objective.

### 2.2 The construction is hard Viterbi regularization, not deterministic annealing

The partition at every slice remains hard. \(\lambda\) penalizes switching between adjacent hard assignments. In deterministic annealing, temperature weights an entropy term and produces a Gibbs/soft assignment at nonzero temperature. These are not the “same knob.” A temporal coupling parameter and an annealing temperature can coexist, but they perform different mathematical jobs.

Therefore the deposit's claims that the Viterbi path is “soft,” that it “dissolves the argmin discontinuity into a bifurcation,” and that Rose/Tishby/Parker–Dimitrov directly anchor this exact objective overreach. Those sources motivate relaxation broadly; they do not derive this path functional.

### 2.3 The score is not invariant to time discretization

The slice deficits are summed while the switching cost is charged once per transition. Refining the same physical window from 21 to 210 slices multiplies the data term by roughly ten while leaving a single switch cost unchanged. The effective meaning of \(\lambda\), the breakpoint at which the path freezes, and the proposed score therefore depend on the arbitrary sampling grid.

A time-extended quantity needs either a declared \(\Delta t\) factor,

\[
J=\sum_t \Delta t\,\Phi_t+\lambda\,\mathrm{TV}(P),
\]

or an explicitly normalized discrete convention with a scaling law for \(\lambda\). Until then, there is no grid-stable window score.

### 2.4 The demonstrated relabeling is a module-cut-to-singleton transition with degeneracy

The proposal describes a transition from the module cut to “cross-module cuts.” Direct enumeration shows that at \(b\approx0.43\) the minimizer instead moves from the unique 3|3 module cut to **six degenerate 1|5 singleton cuts**. At \(\lambda=0\), floating-point tie-breaking makes the chosen singleton label jitter repeatedly even though those cuts have equal theoretical value. With positive \(\lambda\), enumeration order selects one of the equivalent singleton tracks.

This matters conceptually. The example does not yet demonstrate tracking between two nontrivially competing organizations. It demonstrates the known vulnerability of an unnormalized MIP to small-side cuts plus arbitrary symmetry breaking. If that unnormalized choice is canonically intentional, the result can remain, but it must be described honestly and the degeneracy treated as part of the identity problem rather than hidden by one Viterbi path.

The code also labels the accumulated Hamming rotation distance `rots` as “relabelings.” In this run there is one change event but rotation cost 2. Those are distinct observables.

### 2.5 The spectral operator is not shown to relax the discrete moving-MIP

The discrete cost uses a Gaussian log-determinant quantity:

\[
\Phi(\Sigma,P)=TC(X)-TC(X_A)-TC(X_B)=I(X_A;X_B).
\]

The spectral construction instead diagonalizes the raw coupling-graph operator

\[
\operatorname{blockdiag}L(b_t)+a^2L_{\text{time}}.
\]

No derivation shows that the latter is a convex or spectral relaxation of the former, no bound relates their optima, and no map connects \(a\) to \(\lambda\). Calling the two “equivalent readings” is therefore unsupported. They are two different temporal-regularization ideas applied to two different instantaneous objectives.

Froyland and Koltai's actual operator is a Laplace–Beltrami operator built from the pullback metric of a nonautonomous flow. Their paper says multilayer-network supra-Laplacians have “structural similarities,” are “formally similar,” and that results “should carry over.” That is useful precedent, but it is explicitly weaker than the proposal's “this is the same operator” and “the problem is verbatim ours.” See [Froyland & Koltai 2023](https://arxiv.org/abs/2103.16286), especially §1.2 and the discussion of multilayer networks.

### 2.6 Panel C does not validate the MIP transition

For the exact two-module graph used in the code, the graph-Laplacian eigenvalues are analytic:

- module-difference mode: \(6b\);
- four within-module modes: \(3+3b\).

Their crossing is at \(b=1\), not at the Gaussian MIP relabeling near \(b=0.43\). The space-time eigenmode's mass decay near the left side of the ramp is therefore not evidence that the spectral construction reproduces the MIP change. It is consistent with localization where the instantaneous spectral cost is lowest.

The lifetime readout further depends on:

- hand-set \(a=0.8\);
- an eigenmode classifier threshold of `0.3`;
- a lifetime threshold of 5% of peak mass;
- the selected window endpoints and ramp sampling;
- the rule “first qualifying eigenvector,” which can be unstable at crossings or degeneracies.

No robustness sweep is deposited. The dashed \(b^*\approx0.43\) line in panel C visually encourages an identification the mathematics does not establish.

### 2.7 The “solved independently in three fields” headline fails

The literature supports three families of relevant machinery, not three independent solutions of the same AOP object:

1. Froyland–Koltai solve birth/death detection for semi-material coherent sets defined through flow geometry.
2. Supra-Laplacian papers study diffusion on multilayer networks. Froyland–Koltai cite this relation as a formal/structural analogy, so “independent rediscovery” is too strong.
3. Deterministic annealing/information bottleneck soften clustering assignments with entropy regularization; they do not produce the hard temporal switching-cost objective used here.

The honest classification is: **new AOP synthesis borrowing established temporal regularization ideas**, not **known solution imported unchanged**.

A closer precedent for the discrete idea is the temporal-community literature that optimizes snapshot quality subject to temporal smoothness, including formulations explicitly described as a combinatorial temporal-partition problem with convex relaxations; see, for example, [Chen, Kawadia & Urgaonkar](https://arxiv.org/abs/1303.7226). That literature would strengthen the ancestry while also making clear that the AOP-specific observable and validation remain new work.

### 2.8 The excess-entropy contrast is stated too categorically

The standard stationary excess-entropy scalar and its time-translation-invariant asymptotic identities require stationarity. But mutual information between a declared past block and future block remains mathematically definable for a nonstationary joint process at a specified cut. The problem is loss of the standard stationary invariant/limit and dependence on the cut, not literal nonexistence of any past–future mutual information.

This does not rescue or refute the moving-MIP proposal, but publication-strength language should avoid saying the quantity simply “loses its definition.”

### 2.9 Ptaszyński–Esposito line-check: sound, with one refinement

The memo correctly records the paper's scope and the PRL metadata. The primary source states that it studies discrete-state stochastic units on a permutation-invariant network; fixed-point attractors yield either subextensive correlations or non-robust extensivity; robust extensive scaling is impossible at equilibrium; and time-dependent attractors can give extensive scaling far from equilibrium. See [Ptaszyński & Esposito 2025](https://arxiv.org/abs/2410.13375).

One sentence should be tightened: a **time-dependent attractor** is the required class within the stated assumptions; a limit cycle is a robust example, not the uniquely required form. The memo's table heading “time-dependent / limit-cycle dynamics required” could be read as requiring limit cycles specifically. Suggested refinement: “time-dependent attractor required within scope; hyperbolic limit cycles are the structurally stable worked class, not the only conceivable time-dependent form.”

D2 v3 already handles this correctly with “e.g. a limit cycle, or certain chaotic attractors,” preserves the model scope, defines robustness, identifies the target as multipartite mutual information rather than AOP Integration generally, and refuses both a tendency and a causal arrow. **D2 v3 is green.**

## 3. Actionable Fixes

### Priority 0 — canon gate

1. Keep the moving-partition item **FRONTIER** in §§4, 9a, and 13a.
2. Do not use the current figure or current numerical score as evidence of continuity.
3. Trash or archive the three stale pre-correction files so reviewers cannot select them by title alone.

### Priority 1 — repair the discrete proposal

1. Return and plot the actual normalized objective, including the relabeling term.
2. Separately report: instantaneous-deficit component, temporal-penalty component, number of change events, and total rotation distance.
3. Add \(\Delta t\) or derive a sampling-resolution scaling for \(\lambda\); verify convergence under grid refinement.
4. Replace “soft/annealed” with “hard temporally regularized Viterbi path” unless a genuine entropy-regularized model is added.
5. Expose all tied optimal paths or use a probabilistic posterior rather than silently choosing one enumeration-dependent singleton.
6. Test a nondegenerate example with two meaningful competing partitions, not only a 3|3-to-1|5 transition.

### Priority 2 — establish or withdraw the spectral equivalence

Choose one:

- **Derive it:** produce a relaxation theorem or bound connecting the log-det Gaussian partition objective to a quadratic space-time operator, and derive a mapping or comparison between \(a\) and \(\lambda\); or
- **De-scope it:** call the supra-Laplacian an independent graph-coherence diagnostic, not a surrogate for moving \(\Phi_{\mathrm{MIP}}\).

Either route needs sweeps over \(a\), mass threshold, classifier threshold, time resolution, window endpoints, noise, and perturbations that break node symmetry. Compare spectral and discrete transition locations without placing the MIP threshold on the spectral panel unless correspondence is demonstrated.

### Priority 3 — correct the literature claim

Recommended classification:

> Temporal smoothing of changing partitions is established across dynamic coherent-set, multilayer-network, temporal-community, and annealed-clustering literatures. AOP's proposed log-det moving-MIP is a labeled synthesis of those strategies, not a previously published object, and its equivalence to the spectral port remains to be established.

This preserves the genuine strength without claiming identity across unlike objectives.

## 4. Creative Opportunities

### 4.1 Build the actually annealed moving-MIP

Introduce a path distribution

\[
p_{\lambda,\tau}(P_{0:T})\propto
\exp\!\left[-\frac{1}{\tau}\left(\sum_t\Delta t\,\Phi_t(P_t)
+\lambda\sum_t\operatorname{rot}(P_{t-1},P_t)\right)\right].
\]

Then \(\lambda\) controls temporal coherence while \(\tau\) controls softness. Forward–backward gives partition marginals and uncertainty; Viterbi is the \(\tau\to0\) MAP limit. This would handle degeneracy honestly, expose uncertainty near a relabeling, and make the Rose/Tishby ancestry real rather than rhetorical.

### 4.2 Treat MIP identity as a correspondence problem

The scientifically interesting object may be not a single scalar but a path plus uncertainty:

- instantaneous MIP value;
- posterior probability of each partition;
- transition hazard between partition families;
- ambiguity/degeneracy entropy;
- persistence time of a partition equivalence class.

That would turn the present tie problem into a feature: an individuation transition may be preceded by rising partition ambiguity.

### 4.3 Use a benchmark battery, not one symmetric ramp

At minimum: symmetry-broken two-module ramp; two real competing 2|4 or 3|3 partitions; merge–split–merge; node birth/death; multiple transitions; noisy estimated covariance; unequal sampling; and a null window with no transition. Pre-register what would falsify each claimed correspondence.

## 5. Bottom Line for Ben and Prime

**Ptaszyński–Esposito / D2 v3: GREEN.** The narrow feasibility result is represented honestly.

**Moving-MIP closure: RED.** There is a promising method proposal, but the present deposit does not justify FRONTIER→SYNTHESIS. The immediate reason is not philosophical caution; it is a concrete mismatch between objective, returned score, plotted score, and continuity claim. Independent of that bug, the spectral equivalence and three-field “same solved object” claims remain unproved.

The right disposition is **repair and re-test**, not discard. The Viterbi core is useful. It simply has not yet earned the name “time-extended Φ_MIP” as a closed AOP result.

