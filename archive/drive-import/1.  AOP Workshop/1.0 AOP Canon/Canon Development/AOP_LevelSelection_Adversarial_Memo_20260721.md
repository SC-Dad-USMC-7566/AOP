# Adversarial Memo: Four Prime Findings Against AOP Canon v1.21 §13a

**Seat:** Aster / outside critic  
**Mode:** attack only; no canon edit; no correction draft  
**Date:** 21 July 2026  
**Canon checked:** `AOP_CANON_MASTER_v1.21.md`, Drive id `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`, in the live Canon folder; modified 2026-07-21 19:15:04 UTC.  
**Primary checked:** Aguilera & Di Paolo, *Integrated information in the thermodynamic limit*, arXiv:1806.07879v3 / *Neural Networks* 114 (2019), especially Eq. 5, §II.C, §III.B, Fig. 3.G, and Appendix B.

## Executive judgment

Prime found a real failure, but not quite the one advertised. The strongest defect is not that a smooth Φ value makes the crossover meaningless. It is that §13a identifies two distinct events as occurring “precisely” together when an independent cross-grain calculation places them at different couplings:

- full-system raw-MIP relabel: **b = 0.330221124862**;
- raw module-versus-whole Φ equality, using the 4-node module's marginal covariance as Prime specified: **b = 0.300236704295**.

Thus the cross-grain ordering has already changed before the whole system's MIP leaves the module boundary. The latter cannot be the signature or computational cause of the former in this worked model.

The four dispositions are:

| Finding | Fact | Prime's implication |
|---|---|---|
| F1 | **STANDS**, with an important omission: Φ is continuous and monotone but has a substantial derivative kink | **OVERREACH**: “does nothing” is false; smoothness alone does not remove significance |
| F2 | **FALLS as worded**: Aguilera does not treat MIP location as mere bookkeeping or “not signal” | **OVERREACH**: their singleton result transfers as a warning about cut geometry, not as a source-backed dismissal of MIP identity |
| F3 | **STANDS as a conceptual precedent** | **OVERREACH if called a method-validating precedent**; **STANDS** that phaseD1 omitted the necessary comparison |
| F4 | **STANDS that the result is convention-dependent** | **OVERREACH** as a completed level-selection result: per-node is ad hoc, and the probe compares a subsystem with the whole, not an explicitly constructed two-supernode grain |

Overall: the proposed §13a correction has a sound target—the existing analytic-model-result is not established—but should not rely on F1's smoothness rhetoric, F2's “bookkeeping” characterization, or F4 as though it were a completed grain-selection analysis.

## F1 — Smooth and monotone Φ through the crossover

### Independent reproduction

For N=8, a=g=1, exhaustive raw Gaussian MIP:

| b | Φ_MIP |
|---:|---:|
| 0.3300 | 0.195575344854 |
| 0.3302 | 0.195700381070 |
| 0.330221124862 | 0.195713586632 |
| 0.3400 | 0.196758000037 |

At the equality point the module cut and all eight singleton cuts tie. Numerical one-sided derivatives with h=10^-6 are:

- left slope: **0.625113763**;
- right slope: **0.105194829**;
- slope jump: **-0.519918934**.

### Disposition

**Fact: STANDS, but incompletely stated.** The value is continuous and monotone. It is not smooth in the differentiable sense: it has a pronounced kink.

**Implication: OVERREACH.** A min-envelope can carry structural information in its active branch even when its value remains continuous. The canon does not require a jump in Φ. Moreover, §13a explicitly recognizes derivative discontinuity as meaningful in the adiabatic passage. Prime cannot consistently argue that continuity makes the static crossover vacuous while retaining the moving-MIP kink as evidence.

The narrower attack survives: an argmin relabel is not by itself evidence that “the whole becomes one individual.” Here the winning post-crossover branch is a singleton cut, not a newly discovered balanced cross-module seam. That calls for an interpretation of why singleton isolation is an individuation event; neither the value's continuity nor its kink supplies that interpretation.

## F2 — Aguilera allegedly treats MIP location as bookkeeping

### Primary-source result

Aguilera defines the MIP as the raw minimum of the Wasserstein-distance perturbation measure. In their quasi-homogeneous infinite system, homogeneity makes MIP search equivalent to finding the partition cutting the fewest connections; with nonzero inter-region connections, a single-node isolation wins. That is a model result.

But “bookkeeping, not signal” is Prime's gloss, not theirs. Aguilera says the MIP identifies the direction in which the system is least affected, and then interprets Φ as susceptibility along that MIP direction. They use it as signal, not as a disposable computational convenience.

### Transfer test

The source's derivation does not transfer as a theorem to arbitrary finite heterogeneous Gaussian systems. Nevertheless, the warning transfers to this particular finite symmetric complete-block Gaussian because exhaustive computation independently produces the same small-side outcome. This is evidence of a recurring cut-geometry effect, not authority from Aguilera that the effect is meaningless.

### Disposition

**FALLS as worded; implication OVERREACH.** The defensible statement is narrower: Aguilera establishes that singleton MIPs can be structurally expected under raw, homogeneous connectivity, so singleton location cannot automatically be read as a phase boundary or emergent-whole event. It does not establish that MIP location is “bookkeeping,” nor that location is never informative in a finite heterogeneous model.

## F3 — Aguilera §III.B / Fig. 3.G as cross-grain precedent

### What the paper actually does

Aguilera explicitly asks whether A or coupled AE should be considered the integrated unit, computes φ_A and φ_AE, and finds weak coupling favors A while strong coupling favors AE near criticality. Fig. 3.G compares the coefficients of their common divergence and labels which is the more irreducible unit.

This is a genuine precedent for the **logical operation** required by §13a: compute integration for competing candidate systems and compare them. It also confirms the verification finding that phaseD1's full-graph MIP-location scan is not a substitute for a cross-candidate comparison.

It is not a drop-in validation of the canon's implementation. Aguilera compares a subsystem with a compound system, uses a dynamical intervention-based φ, and near criticality compares divergence coefficients. Canon §13a claims a nested grain selector for a static covariance and invokes modules as a coarser level. Those require an explicit coarse-graining map and a declared rule for comparing values across different dimensions. Aguilera supplies neither for this Gaussian port.

### Disposition

**STANDS as conceptual precedent; OVERREACH as methodological precedent.** F3 correctly identifies the missing class of computation and a source demonstrating its purpose. It does not establish that raw static Gaussian MI minima can be compared across sizes without further declaration.

## F4 — Cross-grain size bias and normalization ambiguity

### Independent reproduction and correction

Using N=8 and the 4x4 marginal covariance of one module:

| b | module raw Φ | whole raw Φ | raw winner | module Φ/4 | whole Φ/8 | per-node winner |
|---:|---:|---:|---|---:|---:|---|
| 0.0000 | 0.235001815 | 0.000000000 | module | 0.058750454 | 0.000000000 | module |
| 0.330221 | 0.177733676 | 0.195713587 | whole | 0.044433419 | 0.024464198 | module |
| 0.5000 | 0.188238786 | 0.216817993 | whole | 0.047059696 | 0.027102249 | module |
| 1.0000 | 0.235001815 | 0.287682072 | whole | 0.058750454 | 0.035960259 | module |
| 1.4000 | 0.274898780 | 0.340943496 | whole | 0.068724695 | 0.042617937 | module |

Raw equality is **b=0.300236704295**, not approximately 0.33 under the stated marginal-covariance probe. Per-node keeps the module ahead throughout 0≤b≤1.4 (and remains ahead at b=10 in an additional scope check).

### Is there a principled convention that resolves it?

None of the named alternatives supplies a canonical normalization for this exact comparison:

- Aguilera's r_R factors belong to a thermodynamic-limit region-fraction derivation and their A-versus-AE example fixes equal region fractions. They do not prescribe “divide finite Gaussian Φ by X nodes.”
- Hoel's effective-information framework defines a different intervention-based causal quantity and coarse-graining procedure. It is not a normalizer that can be attached to Gaussian mutual information without changing the measure.
- Zhang's eigenvalue-based result optimizes an explicitly defined linear stochastic coarse-graining. It can motivate a new calculation only after the dynamics matrix, macro map, and objective are declared; it does not return an answer for Prime's marginal-subsystem probe by inspection.

Therefore the ambiguity is real: raw and per-node implement two coherent but inequivalent questions, and §13a declares neither a cross-size comparison convention nor a Gaussian macro construction. Prime's per-node choice does not prove it is the right convention; it proves raw ordering is not convention-free.

### Disposition

**Fact: STANDS. Implication: OVERREACH in its strongest form.** The missing computation cannot presently rescue claim 1 because the result depends on an undeclared convention. But F4 itself does not settle level selection, because its “module” is a four-node embedded subsystem, not an explicitly coarse-grained system of two module supernodes. It diagnoses underdetermination; it is not the completed alternative analysis.

## Cross-cutting answers

### (i) Does F1 also damage the moving-MIP passage?

If F1's rule were “continuous Φ means no meaningful transition,” yes: it would directly undercut the moving-MIP passage, which treats continuity plus a derivative kink as meaningful. That rule should be rejected. The consistent position is:

- a kink/relabel can be a legitimate diagnostic of a change in the weakest cut;
- it does not, without an independent bridge principle, establish a change in ontological individuality;
- the bridge is particularly weak when the new active cut is a singleton generated by raw cut geometry.

Applied consistently, this narrows both passages. It does not erase their computed kinks; it blocks the stronger individuation reading unless independently validated.

### (ii) Work-order design defects

This work order is better than the prior frozen-bin design because it permits split dispositions. It still contains bundled and loaded claims:

1. F1 combines a true numerical observation with the false phrase “the individuation quantity does nothing.”
2. F2 embeds the unsupported interpretive label “bookkeeping, not signal” in what is presented as a source claim.
3. F3 says Aguilera performs the comparison “correctly,” which prejudges whether a critical divergence-coefficient comparison is correct for the static Gaussian port.
4. F4 asks for what a “principled convention” gives without specifying the candidate grain, coarse-graining map, or whether the target is total, density, causal, or predictive integration. Different named literatures answer different questions.

The split fact/inference disposition saves the grading, but the findings should have been atomized before review.

### (iii) Unlisted defects

#### 1. The canon's claimed coincidence is numerically false

The largest new defect is the separation **0.3002367 versus 0.3302211**. Under the raw convention most favorable to canon, the module-versus-whole ordering switches before the whole's MIP relabels. The sentence's “at precisely that crossover” unifies nonidentical events.

#### 2. “Grain” is not operationally defined

A four-node module as an embedded mechanism, a four-node marginal subsystem, and a two-supernode coarse-graining are different mathematical objects. Canon moves among “nodes → modules → whole” without declaring which object is scored. PhaseD1 scores only the whole at node grain; Prime F4 scores a marginal subsystem versus the whole; neither constructs the advertised module-grain macro system.

#### 3. The comparison may not be nested

“Module when weak, whole when strong” compares a proper subset against its superset. “Nodes within modules within a whole” suggests a spatial grain transformation over the same underlying system. Those are distinct exclusion problems. Aguilera supports subset-versus-compound selection; Zhang/Hoel address coarse-graining more directly. Canon conflates them.

#### 4. Symmetry creates massive degeneracy

At the raw relabel, the module boundary ties all singleton cuts. At b=1 the graph is homogeneous and many balanced cuts tie under normalized selectors. Calling either point a unique rotation or a unique selected seam suppresses degeneracy. Any topological interpretation must report the full argmin set, not one representative partition.

#### 5. Larger Φ can reflect opportunity to cut, not greater irreducibility

Comparing minima across systems of different dimension changes both the covariance and the partition search space. Raw Φ_total is extensive-ish; Φ/node is intensive-ish. Without a declared target, “maximizes Φ” bakes the answer into the scaling choice. This is not cured by citing a maximization rule developed for a different causal measure.

## What was checked versus asserted

### Checked directly

- Live Drive currency, file id, title, parent folder, modified time, and current §13a text.
- Aguilera & Di Paolo arXiv primary: definitions, raw MIP, singleton statement, A-versus-AE comparison, critical divergence coefficients, and stated interpretation.
- F1 values, full tie set, and numerical one-sided derivatives by exhaustive bipartition enumeration.
- F4 marginal-module versus whole raw and per-node values, raw equality by bisection, and per-node non-crossover on the requested range plus b=10.
- Prior independently verified raw MIP crossover and normalized-selector behavior.

### Not checked / not claimed

- No reproduction of Prime's exact unpublished F4 implementation; the calculation was reimplemented from the work-order description.
- No implementation of Hoel effective information, Zhang's optimal coarse-graining, IIT Φ^Max, or Aguilera's critical Ising model.
- No claim that per-node normalization is uniquely correct.
- No claim that no future declared Gaussian coarse-graining can yield stable level selection.
- No attack on the already-settled raw-selector source reading.

## Bottom line

The correction target survives, but the cleanest basis is now stronger and narrower than Prime's four-findings package: **§13a has not operationalized a module grain, its deposited computation does not perform cross-grain selection, and the two raw crossovers the prose calls one event are independently unequal.** F1's continuity argument, F2's “bookkeeping” gloss, and F4's per-node result should not be promoted beyond those limits.
