# AOP — Forced-Result Audit and v1.22 Pre-Fold Critic Verdict

**Reviewer:** Aster / outside critic  
**Date:** 22 July 2026  
**Status:** Non-canonical, attack-only review. Nothing folded; live v1.21 untouched.  
**Work order:** `AOP_WorkOrder_Aster_20260722.md`  

## Executive Summary

The mask-salvage headline fails the new standing rule.

**Task 1 exits (b): forced by construction.** On the declared equal-strength static-Gaussian K4 with `S={0,1}`, the actual coded predicate is

`salvage(a) = [lo_load(a) > hi_spectator(a)] AND [(hi_load(a)-lo_load(a))/W_total(a) <= 0.5]`.

As `a→0+`, the load edge has a first-order viability effect, while the spectator's largest effect and the coalition-dependent width enter at higher order. The reproduced weak-coupling behavior is `lo_load ~ a`, `hi_spectator ~ a^3`, and `width/W_total ~ (2/3)a`. Therefore every positive width tolerance admits a sufficiently weak interval in which the predicate is true. The reported non-empty intersection could not have failed on a sweep that includes sufficiently weak positive coupling. It is a self-consistency result, not a contingent salvage finding.

The upper merge at `a*=3.3027756…` is a different matter. It is a real closed-form crossing under the **full unmatched min–max envelope**. It is not a general redundancy ceiling: it disappears completely when coalitions are restricted to cardinality `|C|<=2`, under sparse sampling, and under the mean attribution. Under those conventions the result reduces to: **load remains above spectator at every tested coupling; context sensitivity widens, but there is no finite ceiling.**

**Task 2 exits (a): sound as scoped**, subject to the ordinary admissibility condition that a normalizer be finite and strictly positive on every candidate cut. Changing the normalizer can change both the argmin and the normalized minimum. Zero-calibration is exact across every admissible normalizer. At a relabel crossing, continuity of the minimized normalized objective is generic because the competing continuous branches are equal there; a cardinality-dependent normalizer moves the crossing but does not itself create a jump. What is not generic is a small slope. “The value barely moves” is valid only as a description of the deposited ramp, not as a theorem about all conventions.

**Task 3 finds a broader grading problem, not a new architectural failure.** Several active-body computations are already honestly described as demonstrations or theorems. Others still borrow the rhetoric of tests, confirmation, or independent reach despite having answers encoded by symmetry, topology, normalization, an unbounded control, or a chosen ensemble. The retroactive ledger below identifies the flipping parameter where one exists and says “none” where it does not.

**Task 4: the two artifacts are not the same object.** The v1.20 E17 coupled-Gaussian two-module mask is the earlier self-consistency calculation. The salvage diagnostic is a later three-model study whose decisive object is equal-strength K4 with `S={0,1}`. Its Model 2 also uses two three-node modules, but it is not the E17 calculation and does not collapse the diagnostic into E17. Shelving “the coupled-Gaussian two-module attempt” does not, by identity, return the verified K4 salvage computation to open.

Overall pre-fold judgment: **HOLD remains correct.** The mask-salvage result must be regraded before it can inform P2-5, while the revised Phi_MIP scope wording can stand with its mathematical conditions made explicit in the implementation record.

## Sources and Currency

Actually inspected:

- `AOP_WorkOrder_Aster_20260722.md` — attached work order.
- `AOP_MaskSalvage_VERIFICATION_memo_20260721.md` — Drive id `1MwKp5U3qhpZUptWWJRM70bnAadiUBwuH`.
- `AOP_MaskSalvage_Diagnostic_20260721.md` — Drive id `1pS-BhdfUrPsqB7BXbcCGVdJHh9ZGXYvq`.
- `mask_salvage.py` — Drive id `1GPcrRSySofAD_yZeCcPkpB_S53IOkrC_`; locally preserved SHA-256 `20c02ca1243ca6cb8d4f6a174be13d1b2dd338771078132b658a24c82dbaf062`, exactly matching the cited hash.
- `AOP_MaskSalvage_VERIFICATION_runlog_20260721.txt`.
- `AOP_CANON_MASTER_v1.22_PROPOSED_ASTER.md` — Drive id `1BPO2R0H8v4oYyUpYSdAJxJHsPr1JB-SA`.
- `AOP_CANON_MASTER_v1.21.md` — live master, Drive id `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`.
- `AOP_CANON_MASTER_v1.20.md` — retired comparison copy, Drive id `1EB8F4L6K1WiHsuaw3htm7MsvfHtzSsZz`.
- `AOP_Canon_ChangeSet_v1.21_to_v1.22_RETRACTION.md` — Drive id `1rJJppdn6ARzkFlMQD5k6bAVPCFJhHv-Q`.
- `AOP_v1.22_ReconciliationDiff_20260722.md` — Drive id `1y7bhZ_xSoABXMo4V8kbcWc0Dmqx-lMRs`.
- `REV_Aster_AOP_MaskSalvage_RedTeam_v1_20260721.md` — prior attack record.
- `phaseD1_levelselect.py`, the Phase B–D verification record, both level-selection recheck scripts, and `AOP_LevelSelection_Adversarial_Memo_rev2_20260721.md`.

Not available after exact-name search, broad search, folder listing, and recent-file inspection:

- `AOP_v1.22_DecisionPackage_20260722.md`
- `AOP_v1.22_VerdictResponse_20260722.md`

No conclusion below is attributed to either unavailable file. P2-5 is addressed only from the work order’s quotation and the primary computational artifacts.

## Task 1 — Attack on the Mask-Salvage Result

### 1. The predicate is not the predicate described in prose

The script’s header declares:

- `well_defined(g)`: the **maximum** span width over structural edges is below a threshold;
- `informative(g)`: load lies above spectator **and** midpoint separation exceeds a threshold;
- `salvageable(g) = well_defined(g) AND informative(g)`.

The executable body instead computes:

- well-definedness on the **load edge only**;
- an `inf` flag from a 0.02 midpoint threshold;
- `salv = disjoint AND wd_load`, ignoring `inf` entirely.

Thus the 0.02 information threshold cannot change the final verdict. In Model 3, the load edge happens also to be the widest edge, and interval disjointness happens to imply the unused midpoint condition, so this mismatch does not change the printed K4 table. It remains a **DEFECT** in the stated estimand and blocks any claim that the diagnostic tested the advertised three-part predicate.

Minimum repair: declare one predicate, implement that predicate, and report sensitivity to every threshold it contains. This is a specification repair, not replacement prose.

### 2. Non-emptiness is structural on the declared K4 ramp

Fresh probes of the exact deposited script give:

| `a` | load lower endpoint | spectator upper endpoint | load width / aggregate | coded salvage |
|---:|---:|---:|---:|:---:|
| `1e-6` | `9.99997e-7` | `0` at machine precision | `6.66662e-7` | yes |
| `1e-4` | `9.99700e-5` | `9.99523e-13` | `6.66556e-5` | yes |
| `1e-2` | `9.70904e-3` | `9.51836e-7` | `6.55780e-3` | yes |
| `1e-1` | `7.70753e-2` | `6.40615e-4` | `5.74186e-2` | yes |

The mechanism is the declaration itself. With equal K4 couplings and `S={0,1}`:

- edge `(0,1)` acts directly inside the declared viability set, giving an `O(a)` marginal viability effect;
- edge `(2,3)` acts only through paths that connect the complement back into `S`, so its largest effect is higher order (`O(a^3)` in the reproduced weak-coupling regime);
- coalition dependence vanishes relative to the aggregate at weak coupling (`width/W_total = O(a)`).

For every `rel_width_tol > 0`, there is therefore an `epsilon > 0` such that all `0<a<epsilon` pass width and disjointness simultaneously. Re-running all proper non-empty K4 declaration sizes gives the same existential result whenever two endpoint-membership edge classes exist:

- `|S|=1`: incident versus non-incident edge — non-empty overlap;
- `|S|=2`: inside-S versus outside-S edge — non-empty overlap;
- `|S|=3`: inside-S versus boundary edge — non-empty overlap;
- `|S|=4`: only one edge class exists, so informativeness is undefined rather than false.

No non-degenerate parameter change inside the declared equal-strength K4, proper-`S`, weak-coupling sweep empties the intersection. It can be made empty only by changing the question:

- truncate the domain above the envelope crossing (`a_min >= 3.3027756…`);
- set the width tolerance to exactly zero;
- remove the load edge (`theta_load=0`), which leaves the equal-strength K4 class;
- or choose `S=all nodes`, which destroys the load/spectator distinction rather than producing a negative result.

These are definition/window changes, not a system parameter that lets the advertised existential result genuinely fail.

**Required exit: (b), forced by construction.**

### 3. “Salvageable” is falsifiable pointwise but not existentially on this sweep

At a fixed coupling the coded predicate certainly fails: it is false above the full-envelope merge. On the original grid, `a in {5,8}` fails. The existential headline, however, asks whether the well-defined and informative regions overlap *anywhere*. Because the sweep includes the weak-coupling anchor, that existential predicate is guaranteed positive.

The correct scientific distinction is:

- **pointwise robust-envelope dominance** can fail and does fail near `a*=3.3027756…`;
- **existence of at least one passing coupling** cannot fail on the declared continuous weak-coupling family.

The verification memo reproduced the first fact and inadvertently promoted it as evidence for the contingency of the second.

### 4. The full min–max coalition interval is not uniquely “honest”

The full envelope answers a legitimate but strong question:

> Does the load edge dominate the spectator under every coalition context, even when the load minimum and spectator maximum occur under different and mutually incompatible backgrounds?

That is **worst-case, context-free robust dominance**. It is not the only honest per-edge attribution object, and it is not Kolchinsky–Wolpert’s unique-intervention criterion.

The reproduced coalition-cardinality result is decisive:

| Coalition contexts admitted | First envelope merge |
|---|---:|
| `|C|<=0` | none through `a=40` |
| `|C|<=1` | none |
| `|C|<=2` | none |
| `|C|<=3` | `a≈3.3–3.4` |
| full | `a≈3.3–3.4` |

Therefore the clause **“bounded above by a redundancy threshold” is load-bearing on admitting cardinality-three contexts and on comparing unmatched extremes.** Under the small-coalition or mean convention, the result becomes:

> The declared load edge remains ranked above the spectator at every coupling tested; the distribution of marginal effects broadens with coupling, but no finite loss-of-ordering threshold appears.

That narrower result is still useful. It is a phase diagram of attribution stability, not a universal salvage ceiling.

Grade:

- full-envelope crossing and its numeric location: **SETTLED within the declared model and convention**;
- naming the full envelope “the honest object”: **SYNTHESIS / unsupported preference**;
- promoting its crossing to a general redundancy ceiling: **DEFECT**;
- small-coalition and mean results: **SETTLED within their conventions**.

### 5. Probe A’s no-inversion reading is also structurally benign

The absence of full-interval inversion is not independent evidence that the mask fails gracefully. In the symmetric construction, the spectator interval retains a zero lower endpoint while the load edge has a non-negative, positive upper effect. A full interval with lower endpoint zero cannot lie strictly above the load interval. The “wrong-signed” exit is therefore excluded by the envelope geometry.

The uniform-coalition means also retain load-above-spectator throughout a sweep from `a=1e-6` to `a=1e6`. That mean ordering is consistent with the endpoint-membership symmetry supplied by `S`: load has two endpoints in `S`, spectator has none. It is a competence/self-consistency feature, not a second contingent probe.

Grade: **SETTLED within construction; no-inversion interpretation regraded to self-consistency.**

### 6. Final Task 1 grade

The result is not killed; its grade and claim class change.

- **Retain:** equal-strength K4 plus a local viability declaration produces a weak-coupling region of robust envelope separation; the full envelope merges at `a*=3.3027756…`; the mean and matched-context rankings survive; coalition cardinality controls the ceiling.
- **Withdraw:** “a clean negative could have occurred” for the existential overlap on the declared ramp; “confirmed salvageability” as a general property; and the interpretation of `a*` as a convention-free redundancy ceiling.
- **Regrade:** from `SYNTHESIS, CONFIRMED` to **SETTLED analytic self-consistency within one attribution convention**, with the broader salvage claim **OPEN/FRONTIER** across declarations, graph families, viability functionals, and intervention semantics.

## Task 2 — Revised Phi_MIP Scope Wording

### Bullet 1 — Normalizer changes objective, argmin, and minimum value

**Sound.** For candidate partitions `P`, the reported objective is of the form

`F_P(x) = I_P(x) / N_P(x)`.

Changing `N` changes each branch. It may change the minimizing partition and the minimized value. The earlier distinction “identity changes but magnitude does not” was under-scoped; the revised statement repairs it.

### Bullet 2 — Local near-degeneracy at a relabel crossing

**Sound with a precise interpretation.** If each branch `F_P(x)` is continuous in the coupling parameter and the optimizer exchanges from `P1` to `P2`, then at the crossing `F_P1=F_P2`. The minimized normalized objective is continuous; its derivative generally kinks because the active branch changes.

A normalizer discontinuous in **partition cardinality** does not by itself defeat this. Cardinality is fixed on each candidate branch, so it merely assigns different constants/functions to different branches and moves the crossing. The branches still meet at the point where the argmin exchanges.

Two boundaries must remain explicit:

- equality at a crossing guarantees no jump, not a small slope over a finite coupling step; “barely moves” is an empirical description of this ramp;
- if a normalized selector is used to choose a cut but an **unnormalized** mutual information is then reported, the selected raw value can jump at the normalized crossing. The continuity claim belongs to the same minimized objective used for selection.

These are interpretive constraints, not a defect in the revised scoped wording.

### Bullet 3 — Zero calibration and the other gate criteria

**Sound under admissible normalization.** If the covariance is block-decomposable, at least one cut has numerator `I_P=0`. For every finite, strictly positive normalizer, `I_P/N_P=0`, while mutual information is non-negative, so the minimum is exactly zero. This is genuinely normalizer-independent over the admissible family, not merely observed across the tested raw/size/entropy cases.

A convention with `N_P=0`, `N_P<0`, or an infinite value is not an admissible MIP normalizer and can make the objective undefined or reverse its ordering. The implementation record should state positivity and finiteness. The revised limitation of gradedness, irreducibility, and one-vs-many ordering to the tested convention is correct.

### Bullet 4 — Scope statement

**Sound.** “Static Gaussian, fixed candidate system at fixed grain, under a declared MIP normalization convention” matches what the coordinate actually computes. “Fixed partition” did not: the MIP is an exhaustive minimum over candidate cuts.

**Required exit: (a), sound as scoped.**  
**Grade:** **SETTLED mathematical scope correction**, with normalizer admissibility and same-object reporting noted in the implementation record.

## Task 3 — Retroactive Standing-Rule Sweep

Historical changelog entries are not rewritten here; the list concerns active-body claims and the active status/gate ledgers. The four already-known cases are included for completeness and marked **known**.

| Location | Claim as written or operative claim | Flipping parameter? | Verdict under standing rule |
|---|---|---|---|
| §3 / Figure MW **(known)** | Inert spectator returns exactly zero; proxy mask recovers graded edge sensitivities | Yes only by changing the construction: set a feedback/coupling from spectator `Z` into the viability-relevant dynamics from `0` to `>0` | Zero is forced by the spectator’s disconnection. Correctly a negative control/proxy diagnostic, not confirmation. **SETTLED self-consistency.** |
| §11b **(known)** | Strength anti-ranks viability; Möbius signs invert naive redundancy/synergy labels; “could have come out otherwise” | Yes: swap OR and AND wiring to flip Möbius signs; make `Z` feed back to make its weight nonzero; change assigned rates to remove the anti-ranking | Answer key is manufactured. Current competence-check regrade is correct; any remaining necessity/adjudication language is a **DEFECT**. |
| §13 embarrassment condition **(known)** | Within topology, coupling must widen sweep; chain must out-blur mean-field at matched coupling; “either could have come out otherwise” | No flipping parameter is named inside the declared positive-coupling covariance family; monotonicity and ranking are consequences of the constructed spectra and matching rule | “Could have come out otherwise” is unsupported. Regrade as analytic family property unless a predeclared signed/frustrated coupling or alternative matching convention is shown to flip it. **DEFECT in test rhetoric.** |
| §4 / Figure DM | Figure DM “confirms” `sigma>0 => E>0` and shows converse failure | No within the stated stationary complete-description assumptions; the implication is a corollary. Detailed balance (`sigma=0`) supplies the allowed converse counterexample | Computation illustrates a theorem; it does not confirm it. **SETTLED demonstration.** |
| §4 / Boundary B2 calculation | Screening residual is exactly zero with interface-only paths and positive with a bypass | Yes: bypass coupling `h=0` gives the zero; `h>0` gives positive residual | The flip is encoded by the Markov-blanket condition and added bypass. Constructed contrast, not independent validation. **SETTLED self-consistency.** |
| §4 / Boundary B4 calculation | Maintenance cost is zero at equilibrium and rises with leak and held contrast | Yes: `g=0` or `Delta=0` gives zero; `g>0` and `Delta!=0` gives positive cost | Direct consequence of `sigma_hk=fJ` and the declared pump–leak model. Analytic identity, not a test. **SETTLED.** |
| §4 / Figure T constructed corners | Five regimes establish no non-energy edge is welded shut | Yes by construction: turn the relevant lagged, cross-cut, or within-module coupling on/off | The counterexamples legitimately prove logical dissociability, but cannot validate population-level independence. **SETTLED constructed-counterexample.** |
| §4 / Figure T random ensemble | Raw correlations `~0.61`, B–I `~0.83`, partial correlations and 0.59 unique variance support the graded separation | Yes: the variance/range of the shared global coupling parameter `g`. Setting `Var(g)=0` removes the shared-input positive component and exposes the fixed-coupling tradeoff | Genuine ensemble statistic, but its sign/magnitude are distribution-dependent. Grade **random-ensemble regularity**, not confirmation. Ensemble law and seed are required declarations. |
| §5 retention-depth computation | Cell-type `T99~19` versus star-type `~1`; 12-fold difference from timescale structure | Yes: slow/fast pole ratio. Ratio `=1` removes the difference; reversing which system has the slower observed pole reverses the ordering | Designed parameterized illustration. The closed-form dependency is real; the biological labels do not independently validate it. **SETTLED within model.** |
| §6 Figure R | Per-component uncertainty diverges while aggregate direction sharpens | No within the equicorrelation model; both are eigenvalue identities. `rho=0` removes blur, but cannot reverse the sign | Already largely described honestly as inherited sloppiness. **SETTLED demonstration, not AOP evidence.** |
| §6 Figure TF | Topology ranks the two blur mechanisms differently; aggregate mode stays at `1.000` | The topology category changes the ranking, but aggregate `1.000` is held by the normalization/matching convention | The decomposition is useful; the conserved aggregate is partly imposed. Grade topology rankings as **analytic-model-results**, aggregate invariance as **normalization identity**. Do not call the package independent confirmation. |
| §11 Figure R-star O-information | Derived star operator is redundancy-dominated; only a common-effect/collider structure flips it to synergy | Yes: categorical coupling architecture, cooperative/common-cause to collider/common-effect | A real flip exists in the stated comparison family. It supports a scoped sign result, not a universal star claim. **SYNTHESIS / analytic-model-result.** |
| §11 / Figure R-star blur | A real integrated system “could not have come out not blurred”; star demonstrates self-consistency | None inside the strongly coupled linear class | Correctly self-graded in the body. **SETTLED self-consistency; no repair.** |
| §11a / Figure LT | Living discriminator separates cell-type from star-type and does not misclassify the star | None: cell has a separate reference node and star does not; load-bearing status is designed | Correctly identified as self-consistency. It does not validate the frontier definition of life. **SYNTHESIS demonstration.** |
| §11a memory-edge weight | Weight `[0.45,0.80]`; edge earns semantic weight only where reference is tighter than tolerance, and inverts when noisier | Yes: reference-noise / viability-tolerance ratio. Crossing noise above the tolerance flips the weight | This is a genuine within-model flip because the parameter and direction are named. **Analytic-model-result**, not empirical validation. |
| Table 4, three resolvability–TUR gates | Snapshot/B/K gates return NULL and jointly support a sector split | Snapshot and trajectory-B: none within their parameterization (`Sigma` and `F_B` are `Q`-free). K-gate: no predeclared scalar flip is documented in the master | First two nulls are algebraically forced by the chosen sector decomposition. The K-gate is a scoped control comparison, not a general null. **SETTLED within model / SYNTHESIS beyond.** |
| Table 4, `E` versus `Cmu` dormancy gate | `Xi=Cmu+−Cmu−=0` at every drive | Yes only by breaking the relabeling symmetry, e.g. introduce rate heterogeneity/asymmetry `delta!=0`; within the symmetric ring it is forced | The deposited symmetric-ring null is an identity. It does not establish `Xi=0` generally. **SETTLED within construction.** |
| Table 4, Phi_MIP axis gate | Five criteria pass and establish a distinct one-vs-many coordinate | Zero-calibration: none under admissible normalizers. Gradedness: coupling `g=0` gives zero and `g>0` welds by design. Ordering can move with the declared normalizer and system family | A valid coordinate competence gate, not external validation of individuation. Current static-Gaussian scoping is essential. **SYNTHESIS / analytic-model-result.** |
| Table 4, mechanism substitutability | NULL at target persistence `P*=0.80`; a finite exchange surface exists below ceilings | **Yes, explicitly:** set `P*=0.50` and the gate changes from infeasible to a genuine iso-persistence substitution surface | This is the cleanest genuine could-have-failed/changed result in the ledger because the flipping parameter is already named. **SETTLED within minimal model.** |
| Table 4, common-price gate | No mechanism-independent persistence price; dissipation spans `0` to `1.313` on iso-`P=0.50` | No non-trivial flip inside the declared mechanism set: a passive equilibrium barrier has zero housekeeping cost while active flux dissipates | The no-price result is forced once a zero-cost equilibrium wall and a positive-cost driven mechanism are both admitted at the same `P`. Valid counterexample to universal fungibility, not a contingent test. **SETTLED constructed-counterexample.** |
| Table 4, Schlögl ceiling gate | Bank unbounded and pure Flux has zero occupancy leverage | Bank: no, because reset strength is allowed unbounded. Flux: no within a one-dimensional birth–death chain; add a cyclic/multidimensional state graph to permit a divergence-free current | Both exits are structural consequences of control domain and topology. Useful model correction, not external validation. **SETTLED within class.** |
| Table 4, worked-case ceiling prediction | Prediction returns NULL after Bank ceiling is retracted | None; it is a logical dependency result | Not a new test. Correctly a withdrawal by dependency. **SETTLED bookkeeping.** |
| Table 4, current→lifetime | Current changes MFPT 5.7-fold; metastable sign is one-sided downward | `A=0` yields equality; any effective nonzero circulation in the deposited double well lowers the asymptotic MFPT. Sign cannot reverse under theorem assumptions | Magnitude is parameter-dependent; sign is theorem-constrained. “Confirmation” language should mean numerical illustration only. **SETTLED theorem + model instance.** |
| §13a adiabatic moving MIP | MIP relabels; minimized value continuous; derivative kinks | Yes for occurrence of relabel: stop the ramp below raw `b=0.3302211`, or choose a different normalizer that moves the crossing. Continuity at a continuous crossing has no flip; a kink can disappear under tangential branch contact | Optimizer path is computed; continuity is structural; kink is generic but not guaranteed. No individuation validation follows. **Analytic-model-result.** |

### Task 3 bottom line

The standing rule should distinguish three categories rather than forcing everything into “test” versus “not test”:

1. **Identity/theorem demonstrations** — no flipping parameter inside the declared class (Figure DM, Figure R, the measure-preserving MFPT sign, zero-calibration).
2. **Constructed contrasts/competence checks** — a parameter flips the result because the answer key is the intervention itself (B2 bypass, OR/AND wiring, Figure LT architecture).
3. **Contingent ensemble/model results** — a predeclared parameter can reverse or erase the outcome (Figure T coupling-variance ensemble, retention pole ratio, memory-noise/tolerance ratio, target persistence `P*`).

Only category 3 earns “could have come out otherwise” without qualification. Category 2 can establish logical dissociability or computational competence. Category 1 can verify code against mathematics but cannot add evidential weight to the underlying claim.

## Task 4 — Cold Identity Read

**They are different objects.**

- **E17 / v1.20 object:** a coupled-Gaussian **two-module** mask calculation introduced to discharge the standing “well-posed part-partition” item. Its result is per-edge interval widening and blur with coupling while the aggregate mode stays sharper. The canon itself grades it as self-consistency.
- **Mask-salvage object:** a later three-model diagnostic. Its decisive test is equal-strength **K4**, `S={0,1}`, load `(0,1)`, spectator `(2,3)`, with the overlap/merge analysis and `a*`. Its Model 2 happens to contain two three-node modules, but that is one baseline inside the later diagnostic, not identity with E17.

Therefore P2-5’s phrase “the coupled-Gaussian two-module attempt” identifies E17, not the verified K4 result. Attaching E17’s caveat to the K4 artifact would conflate computations; treating the K4 result as “returned to open” would erase a completed and independently reproduced computation, even though Task 1 above requires its **claim and grade** to be narrowed.

No corrected wording is proposed, per work order.

## Actionable Fixes

Prioritized minimum repairs only:

1. **Regrade mask-salvage before any fold.** Mark non-emptiness as forced weak-coupling self-consistency; retain `a*` only as a full-envelope, cardinality-`>=3`, unmatched-context crossing.
2. **Resolve the predicate/code mismatch.** Decide global versus load-only well-definedness and disjointness versus the 0.02 informativeness flag; then implement exactly one declared predicate.
3. **Separate attribution conventions.** Full envelope, restricted coalition, matched-context, uniform-coalition mean, and true Shapley value answer different questions. No one is “the honest object” without a decision criterion.
4. **Keep the revised Phi_MIP scope.** Add the normalizer admissibility condition to the method record and ensure continuity claims refer to the same normalized objective used for selection.
5. **Apply the three-category standing-rule grade.** Identity/theorem demonstration; constructed competence/counterexample; contingent result with named flip. Do not use “pre-registered” as a substitute for contingency.
6. **Do not let P2-5 merge E17 and K4.** They require separate dispositions.

## Creative Opportunities

The useful result hiding inside the failed salvage headline is not one scalar ceiling but a **semantic-attribution phase diagram** with at least three independent coordinates:

- semantic relevance in matched contexts;
- attribution stability across coalition contexts;
- mechanistic identifiability/intervenability.

The K4 calculation already suggests these separate: matched-context and mean ranking survive while context-free envelope dominance fails. Turning that separation into the object of study would fit AOP’s ownership-free posture better than asking whether one per-edge weight is globally “salvageable.” It would also supply genuine future tests: predeclare a graph/declaration ensemble and ask which of the three boundaries moves when redundancy, topology, or intervention class changes.

## Final Disposition

- **Task 1:** exit **(b), forced by construction**; existential salvage claim regraded.
- **Task 2:** exit **(a), sound as scoped**; admissible-positive normalizer and same-object continuity conditions recorded.
- **Task 3:** multiple additional forced/constructed results identified; table above is the retroactive ledger.
- **Task 4:** **different computations**; E17 caveat cannot be attached to K4 by identity.

**Fold status:** HOLD.  
**Canon status:** live v1.21 untouched; proposed v1.22 untouched.  

— End of outside-critic verdict —
