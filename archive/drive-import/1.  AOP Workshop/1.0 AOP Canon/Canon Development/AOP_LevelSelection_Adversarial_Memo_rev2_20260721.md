# Adversarial Memo: Four Prime Findings Against AOP Canon v1.21 §13a

**Date:** 21 July 2026  
**Seat:** Aster / outside critic  
**Mode:** attack only; no canon edit; no correction draft  
**Canon under test:** `AOP_CANON_MASTER_v1.21.md`, Drive ID `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`  
**Independent check script:** `aster_levelselection_attack_check_20260721.py`

## Executive Summary

Prime's four-findings package survives only in narrowed form. The most damaging result is not F1's claim that the scalar “does nothing.” That claim is mathematically false: the raw Φ_MIP envelope has a large derivative kink. The stronger attack is that §13a conflates three different operations—finding the full system's weakest partition, choosing a system boundary (module versus module-plus-environment), and choosing a coarse-graining of the same system—and then describes two numerically distinct events as occurring “at precisely” one crossover.

The independent calculations establish:

- Raw full-system MIP relabel, N=8: **b = 0.330221124862**.
- Marginal 4-node-module versus 8-node-whole raw Φ equality: **b = 0.300236704295**, not ≈0.33.
- The raw Φ_MIP value is continuous and increasing through the relabel, but its slope changes from approximately **0.625114** to **0.105195**. It is not smooth in the mathematical sense.
- Per-node scoring keeps the marginal module ahead over the requested **0≤b≤1.4** range; a spot check at b=10 does likewise. This demonstrates convention dependence but does not establish per-node scoring as canonical.
- Even before normalization, the module/whole equality depends on what “the module” means: marginal covariance gives **0.300237**, conditional covariance gives **0.216327**, and an isolated induced K4 gives **0.629563**.
- A literal two-supernode coarse-graining by module averages does not reproduce the claimed module→whole result: it ties the eight-node raw Φ through b*=0.330221 and exceeds it thereafter.

The per-finding dispositions are:

| Finding | Factual disposition | Implication disposition |
|---|---|---|
| F1 | Numerical values and monotonicity **STAND**; “smooth” **FALLS** because the derivative is discontinuous | **OVERREACH** |
| F2 | Cut-counting statement **STANDS within Aguilera's homogeneous limit**; “bookkeeping, not signal” **FALLS** | **OVERREACH** |
| F3 | **STANDS** as a precedent for comparing candidate systems/boundaries and as proof of what `phaseD1` omits | **OVERREACH** if called a nested-grain or method-validating precedent |
| F4 | Qualitative convention dependence **STANDS**; Prime's ≈0.33 raw equality is numerically wrong | **STANDS** as a diagnosis of underdetermination; **OVERREACH** as a completed level-selection result |

**Bottom line:** the proposed correction target survives, but the clean grounds are narrower and stronger than Prime's framing. §13a has not defined its candidate objects or cross-size comparison rule, `phaseD1` does not perform level selection, the cited literatures do not supply a plug-in normalization for static Gaussian Φ_MIP, and the prose's claimed coincidence is false under the very raw convention most favorable to it.

## Currency and Evidence Grounding

The live Canon folder contained `AOP_CANON_MASTER_v1.21.md` at the supplied ID, modified **2026-07-21 19:15:04 UTC**. No later master was visible in that folder when checked. The operative §13a language was read from that live file.

The following were also inspected: the prior independent verification memo and verifier; deposited `phaseD1_levelselect.py`; the Aguilera and Di Paolo primary; Hoel et al. 2016 on Φ across spatiotemporal scales; Liu, Yuan, and Zhang's linear-stochastic causal-emergence paper; and an already-present file titled `AOP_LevelSelection_Adversarial_Memo_20260721.md` plus its recheck script. That pre-existing adversarial file was treated as an object to audit, not as an authority. The F1/F4 calculations reported here were independently reimplemented from the model specification.

## Critique and Per-Finding Dispositions

### F1 — “Φ_MIP's value is smooth and monotone through the crossover”

Independent N=8 raw values:

| b | Φ_MIP |
|---:|---:|
| 0.330000000000 | 0.195575344854 |
| 0.330200000000 | 0.195700381070 |
| 0.330221124862 | 0.195713586632 |
| 0.340000000000 | 0.196758000037 |

At b*=0.330221124862, the module boundary and all eight singleton cuts tie. With h=10^-6, the one-sided slopes are:

- left: **0.625113763**;
- right: **0.105194829**;
- jump: **−0.519918934**.

**Disposition on fact:** the tabulated values and local monotonicity **STAND**. The word “smooth” **FALLS** unless Prime means merely “continuous-looking.” A minimum of smooth branches is generally only piecewise smooth, and this branch switch has a pronounced first-derivative discontinuity.

**Disposition on implication:** **OVERREACH.** Continuity does not imply that the individuation quantity “does nothing.” The active weakest-cut branch changes and the scalar records that as a kink. The canon is entitled to treat the kink as a structural diagnostic of its optimization problem.

What the kink does **not** establish is the canon's ontological gloss. A change in the identity of the least-cost cut proves a change in the optimizer. It does not prove that “the whole becomes one irreducible individual.” That bridge is especially weak here because the new minimizers are singleton cuts. Neither continuity nor non-differentiability supplies the missing bridge principle.

### F2 — “Aguilera treats MIP location as bookkeeping, not signal”

Aguilera and Di Paolo do state that, in their quasi-homogeneous infinite-size model, finding the MIP reduces to finding the partition cutting the fewest connections and that nonzero inter-region coupling makes a single-node isolation win. That scoped computational claim **STANDS**.

The “bookkeeping, not signal” gloss **FALLS**. The paper describes the MIP as the direction in which the system is least affected, interprets φ as susceptibility along that direction, and uses the resulting quantities to identify the predominant integrated unit. The authors do not dismiss MIP identity as a disposable convenience.

**Transfer verdict:** the source's homogeneous-limit derivation does not transfer as a theorem to arbitrary finite heterogeneous Gaussian models. It does transfer as a warning in this specific symmetric Gaussian, because exhaustive enumeration independently produces the same singleton behavior. The legitimate inference is: **singleton MIPs are structurally expected under raw cut minimization, so singleton location cannot automatically be promoted to an emergent-whole signature.** The illegitimate inference is: Aguilera shows MIP location is never informative.

**Disposition on implication:** **OVERREACH.** F2 weakens the canon's interpretation but does not source a general dismissal of MIP location.

### F3 — Aguilera §III.B / Fig. 3.G as precedent for claim 1

Aguilera's comparison is real and directly relevant. The paper asks whether A or coupled AE should count as the integrated unit, calculates φ_A and φ_AE, and compares their divergence coefficients near the shared critical point. Weak coupling favors A; stronger coupling favors AE. This is a genuine precedent for **candidate-system or boundary selection**.

It is not a nested-grain calculation. A versus AE changes the set of included variables—a subsystem is compared with its superset. Hoel et al.'s grain operation instead compares alternative macro representations of the same underlying micro system. Those are distinct exclusion questions:

1. **Span/boundary:** which elements belong to the candidate system?
2. **Resolution/grain:** how are the same underlying elements grouped into macro elements?

Canon §13a uses “grain” language while its claimed module-versus-whole transition is naturally a span/boundary comparison. `phaseD1` performs neither operation: it holds the eight-node system and representation fixed and changes only the identity of its weakest bipartition.

Aguilera also does not validate the canon's static-Gaussian port. Its φ is dynamical, intervention-based, and evaluated by relative divergence tendencies near criticality. The live canon uses static covariance, Gaussian mutual information, and absolute finite values. The paper establishes the logical need to compare competing candidates; it does not show that the AOP quantities are commensurable across sizes.

**Disposition:** **STANDS** as a conceptual precedent and as evidence that `phaseD1` omits the required comparison. **OVERREACH** if described as the same nested-grain operation or as validation of the static-Gaussian method.

### F4 — Cross-grain size bias and normalization ambiguity

Under Prime's stated construction—a four-node module scored from its marginal covariance versus the eight-node whole—the independent result is:

| b | Module raw Φ | Whole raw Φ | Module Φ/4 | Whole Φ/8 |
|---:|---:|---:|---:|---:|
| 0.000000 | 0.235001815 | 0.000000000 | 0.058750454 | 0.000000000 |
| 0.300236704 | 0.176721525 | 0.176721525 | 0.044180381 | 0.022090191 |
| 0.330221125 | 0.177733676 | 0.195713587 | 0.044433419 | 0.024464198 |
| 0.500000 | 0.188238786 | 0.216817993 | 0.047059696 | 0.027102249 |
| 1.000000 | 0.235001815 | 0.287682072 | 0.058750454 | 0.035960259 |
| 1.400000 | 0.274898780 | 0.340943496 | 0.068724695 | 0.042617937 |

The raw equality is **b=0.300236704295**, not ≈0.33. Per-node scoring keeps the marginal module ahead throughout 0≤b≤1.4; b=10 was also checked, but no universal all-b proof is claimed.

**Does a principled convention resolve the ambiguity? No—not for the measure canon declared.**

- Aguilera's region fractions r_R arise inside a thermodynamic-limit derivation. They are not a finite-system normalizer for comparing raw Gaussian MIP values across dimensions.
- IIT's Φ^Max compares Φ across candidate systems and macro mappings, but its Φ is built from causal repertoires and an explicit transition model. It does not authorize attaching a scalar normalizer to static Gaussian mutual information.
- Hoel's effective-information work defines a different intervention-based causal measure and macro model. It is not a normalization of Φ_MIP.
- Liu, Yuan, and Zhang explicitly use **dimension-averaged effective information** to control dimension growth in cross-dimensional comparisons. That makes Prime's intensive/per-node probe scientifically non-frivolous, but it remains an analogy, not the application of their measure. Their method requires a discrete-time dynamics matrix, a noise covariance, a linear macro map, and an information-loss constraint. Static Σ=(I+L)^−1 alone does not determine their answer.

Thus F4's ambiguity is real. Prime's per-node choice is not uniquely correct; it proves that the canon's raw result is not convention-free. A future principled convention might stabilize a result, but none of the cited candidates produces one for this undeclared static-Gaussian comparison by inspection.

**Disposition on fact:** qualitative convention dependence **STANDS**; the claimed raw crossover value needs correction to 0.3002367 under the stated probe.

**Disposition on implication:** **STANDS** as a diagnosis that claim 1 is presently underdetermined. **OVERREACH** if treated as a completed level-selection solution or proof that per-node scoring is the correct one.

## Cross-Cutting Answers

### (i) Does F1 also damage the adiabatic moving-MIP passage?

If F1's rule is “continuous Φ means no meaningful transition,” then yes—it destroys the moving-MIP passage too, because that passage expressly treats continuity plus a derivative kink as meaningful. That rule is self-defeating and should be rejected.

The consistent conclusion is narrower and applies to both passages:

- a relabel and derivative kink can validly diagnose a change in the active weakest cut;
- neither fact alone establishes a change in individuality;
- the ontological inference requires an independently defended bridge from optimizer identity to system identity.

So F1 does not erase the moving computation. It does undercut any stronger individuation reading of that computation unless the bridge is supplied. The moving passage is less exposed to the exact F1 rhetoric if its post-kink cut is genuinely cross-module rather than singleton, but it is not exempt from the inference problem.

### (ii) Work-order design defects

This order is materially better than the prior frozen-bin order because it explicitly permits split fact/inference dispositions. It still contains loaded compound claims:

1. F1 says “smooth” while its own steelman predicts a derivative kink. “Continuous” and “smooth” should not be bundled.
2. F2 embeds Prime's interpretation (“bookkeeping, not signal”) inside a purported source claim.
3. F3 says Aguilera performs the comparison “correctly,” pre-judging whether its critical dynamical method transfers to the Gaussian port.
4. F4 asks what a principled convention “gives” without defining whether the candidate is a marginal subsystem, conditional subsystem, isolated induced subgraph, two-supernode macro system, or something else.
5. “Cross-grain” is used for a subsystem-versus-superset calculation. That terminology prejudges the largest conceptual issue in the section.

The allowed split dispositions prevent these defects from forcing an incorrect bin, but each finding should have been atomized into factual, transfer, and interpretive propositions.

## Unlisted Defects

### 1. The canon's claimed numerical coincidence is false

Under the raw marginal-module probe most favorable to canon, module/whole Φ equality occurs at **0.300236704295**, while the full-system MIP relabel occurs at **0.330221124862**. The cross-candidate ordering has already changed before the full system's weakest cut leaves the module boundary. The phrase “at precisely that crossover” joins two different events.

### 2. “Grain” and “system boundary” are conflated

A four-node module versus an eight-node whole is a subset/superset or boundary comparison. An eight-node micro representation versus a two-supernode macro representation is a grain comparison. Aguilera directly precedents the first; Hoel directly precedents the second. Canon's prose treats them as interchangeable, while `phaseD1` computes only a third object—the weakest partition of the fixed eight-node representation.

### 3. The candidate module is undefined even before normalization

Three defensible module constructions give three raw equality points:

| Module construction | Module/whole raw equality b |
|---|---:|
| Marginal covariance Σ_AA | 0.300236704295 |
| Conditional covariance Σ_A\|E | 0.216326766242 |
| Isolated induced four-node K4 | 0.629563014099 |

This sensitivity is prior to the raw-versus-per-node dispute. AOP must declare how the environment is treated when scoring a candidate subsystem.

### 4. A literal two-supernode grain gives a different qualitative result

Using the symmetry-respecting macro map that replaces each four-node module by its average produces a two-variable Gaussian. Its raw Φ equals the eight-node whole's raw MIP for b≤0.330221, because the whole's active cut is exactly the module boundary. Above the relabel, the two-supernode Φ is larger because the eight-node optimizer switches to a cheaper singleton cut. Examples:

| b | Two-supernode Φ | Eight-node Φ |
|---:|---:|---:|
| 0.300000 | 0.176569645 | 0.176569645 |
| 0.330221 | 0.195713587 | 0.195713587 |
| 0.500000 | 0.293893332 | 0.216817993 |
| 1.000000 | 0.510825624 | 0.287682072 |

This natural grain construction does not yield the advertised weak-module/strong-whole crossover. It yields tie→macro. It is not declared canonical; its value is diagnostic precisely because §13a has not declared any macro map.

### 5. The purported Zhang Gaussian bridge is mischaracterized

The cited primary is **Kaiwei Liu, Bing Yuan, and Jiang Zhang**, published in *Entropy* in **2024** (arXiv:2405.09207), not naturally “Zhang et al. 2025.” More importantly, its optimal coarse-graining is governed chiefly by eigenvalues/eigenvectors of the **dynamics parameter matrix**, with noise covariance also entering the causal-emergence expression. The live canon says “principal eigenvalues and eigenvectors of the system's covariance.” That is not what the paper states.

This is load-bearing. The paper is presented as the closed-form Gaussian bridge for §13a, but AOP supplies only a static covariance and no discrete-time macro dynamics or information-loss constraint. The cited result therefore cannot ground the claimed static-Gaussian level selector as written.

### 6. Degenerate argmin sets are suppressed

At the raw crossover, the module boundary ties all eight singleton cuts. At b=1 under the tested normalized selectors, the module cut ties the complete family of balanced cuts. A single representative “seam” conceals a set-valued optimizer. Any topological or individuation reading must report the full tie set and explain how identity is assigned at degeneracy.

### 7. Cross-size maximization changes both the quantity and its search space

Comparing raw minima for four- and eight-variable systems changes covariance dimension, candidate partitions, and the number of opportunities to find a cheap cut. Raw total Φ and intensive Φ/node answer different questions. Without a declared target—total intrinsic integration, integration density, causal effectiveness, predictive sufficiency, or something else—“maximize Φ” imports rather than discovers the level-selection rule.

## Actionable Tests Before Any Correction Is Drafted

These are tests, not correction language:

1. Freeze whether §13a is solving **boundary/span selection** or **resolution/grain selection**. Do not accept one calculation as evidence for the other.
2. For boundary selection, preregister marginal, conditional, or interventionally isolated treatment of the excluded environment and justify it against the declared semantics of Φ_MIP.
3. For grain selection, preregister an explicit macro map W and derive the macro covariance or dynamics rather than treating a four-node subset as a grain.
4. Freeze the cross-dimensional objective before running: raw total, per-dimension/intensive, IIT causal Φ, or Liu–Yuan–Zhang dimension-averaged effective information.
5. Report the entire argmin set and branch derivatives at every crossover.
6. Separate three numerical events in the results table: candidate-score equality, full-system MIP relabel, and any derivative nonanalyticity. Test rather than assume their coincidence.

## Creative / Adversarial Opportunities

- Use the exact block symmetry to derive closed forms for the module-boundary, singleton, marginal-module, conditional-module, and two-supernode branches. That would turn the current numerical counterexamples into an analytic impossibility map showing which definitions can and cannot share a crossover.
- Construct two systems with identical static Σ but different transition matrices. If the Liu–Yuan–Zhang selector chooses different macro maps, that would directly falsify the canon's claim that the cited dynamical result can be read from covariance alone.
- Break module symmetry slightly and track whether the simultaneous eight-singleton tie unfolds into unstable winner switching. If tiny heterogeneity moves the alleged individuation point substantially, the “signature” reading is structurally fragile.
- Compare nested grain and nested span in the same model. If their preferred levels diverge, §13a will need two named selectors rather than one overloaded “which-grain” rule.

## What Was Checked Versus Asserted

### Checked directly

- Live master identity, parent folder, modified time, and operative §13a text.
- Aguilera and Di Paolo's raw MIP definition, singleton statement, A-versus-AE calculation, critical divergence comparison, and interpretation of MIP susceptibility.
- Hoel et al.'s candidate-system and macro-level search structure.
- Liu, Yuan, and Zhang's dimension-averaged effective-information rationale, required dynamical objects, and parameter-matrix/eigenvector result.
- F1 values, full tie structure, and one-sided derivatives by exhaustive bipartition enumeration.
- F4 marginal raw/per-node values and marginal raw equality by independent implementation.
- Conditional, isolated-module, and two-supernode sensitivity probes.
- The prior independently verified raw and normalized full-system MIP crossovers.

### Not checked or not claimed

- No claim that per-node normalization is uniquely correct.
- No implementation of IIT Φ^Max, Hoel effective information, Aguilera's kinetic Ising model, or Liu–Yuan–Zhang causal emergence on this graph.
- No claim that no future fully declared Gaussian dynamics and macro map can produce stable level selection.
- The spot check at b=10 is not a proof of Prime's “every b” wording over an unbounded domain.
- No canon correction was drafted and the master was not modified.

## Primary Sources

- Miguel Aguilera and Ezequiel A. Di Paolo, “Integrated information in the thermodynamic limit,” arXiv:1806.07879; *Neural Networks* 114 (2019), 136–146. https://arxiv.org/abs/1806.07879
- Erik P. Hoel, Larissa Albantakis, William Marshall, and Giulio Tononi, “Can the macro beat the micro? Integrated information across spatiotemporal scales,” *Neuroscience of Consciousness* 2016, niw012. https://doi.org/10.1093/nc/niw012
- Kaiwei Liu, Bing Yuan, and Jiang Zhang, “An Exact Theory of Causal Emergence for Linear Stochastic Iteration Systems,” *Entropy* 26 (2024), 618. https://doi.org/10.3390/e26080618

