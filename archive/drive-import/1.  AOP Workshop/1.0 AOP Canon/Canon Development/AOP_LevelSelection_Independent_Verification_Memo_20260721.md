# Independent Verification Memo: AOP §13a Level Selection

**Date:** 21 July 2026  
**Seat:** Aster / independent non-CS verifier  
**Scope:** Verify only. No canon edit; no critic pass.  
**Canon grounded:** `AOP_CANON_MASTER_v1.21.md`, live Canon-folder file ID `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`, modified 2026-07-21 19:15:04 UTC.  
**Deposited evidence inspected:** `phaseD1_levelselect.py` (ID `1UBjKQxufF0v9H8IeKy5wRhLUJhArNR3K`) and `VERIFICATION_phaseBCD.md`; later full-graph moving/normalized-MIP scripts were checked only for evidence scope. None of those scripts was run.  
**Independent implementation:** `aop_levelselect_independent_verify_20260721.py`; SHA-256 `362471de5e36dbb2b96eee75407707a0bd00194899e40b4642e09862ac545657`.

## Verdict against the frozen criteria

**Mixed result; no frozen decision bin is fully satisfied.** Prime's computational diagnosis is confirmed, but its primary-source premise is contradicted.

- **UPHELD criterion: not met.** Job A reproduces the singleton-versus-balanced split, and the normalized selectors remove the approximately half-weight crossover. But Job B finds that Aguilera and Di Paolo select the MIP on the raw partition distance, not on a normalized quantity. Therefore the required premise that `phaseD1` used a non-canonical unnormalized selector is false.
- **REFUTED criterion: not met.** The cited paper does use the raw selector and explicitly anticipates singleton MIPs in its homogeneous thermodynamic-limit model. That establishes source fidelity, not a principled demonstration that the singleton transition is a valid finite-model individuation signal rather than a small-side effect. Job C also finds no independent cross-grain computation that could rescue claim 1.
- **PARTIAL criterion: not met as written.** Its condition requires claim 1 to be separately sound. The deposited evidence does not compute claim 1 at all.

The clean disposition is therefore: **the allegation that `phaseD1` computes a non-canonical selector is contradicted; §13a is nevertheless not verified because its cross-grain claim is unevidenced and its MIP-location individuation gloss is normalization-sensitive.** This is a builder/verifier finding, not a canon decision.

## A. Independent exhaustive computation

The verifier was implemented from the work-order specification. For every (b\in[0,1.4]), it constructs the weighted Laplacian, computes Σ = (I + L)⁻¹, and enumerates all unordered nontrivial bipartitions: 31 for (N=6) and 127 for (N=8). Gaussian mutual information is evaluated by log determinants. No estimation is used. The entropy selector uses Gaussian differential entropy in nats,

\[
h(A)=\tfrac12\left(|A|\log(2\pi e)+\log\det\Sigma_{AA}\right).
\]

| N | Selector | Module boundary remains MIP | Transition | MIP after transition |
|---:|---|---|---|---|
| 6 | Raw (I(A;B)) | (b<0.420600748420) | At (b^*=0.420600748420), the module cut ties with all six singleton cuts | Singleton (1\mid5) |
| 6 | Size-normalized (I/\min|A|,|B|) | (b<1) | At (b=1), all balanced (3\mid3) cuts tie, including the module cut | Balanced cross-module (3\mid3) |
| 6 | Entropy-normalized (I/\min(h(A),h(B))) | (b<1) | Same (b=1) balanced tie | Balanced cross-module (3\mid3) |
| 8 | Raw (I(A;B)) | (b<0.330221124862) | At (b^*=0.330221124862), the module cut ties with all eight singleton cuts | Singleton (1\mid7) |
| 8 | Size-normalized (I/\min|A|,|B|) | (b<1) | At (b=1), all balanced (4\mid4) cuts tie, including the module cut | Balanced cross-module (4\mid4) |
| 8 | Entropy-normalized (I/\min(h(A),h(B))) | (b<1) | Same (b=1) balanced tie | Balanced cross-module (4\mid4) |

**Target comparison.** Prime's qualitative targets are reproduced. The (N=8) raw relabel occurs between 0.3 and 0.4, while both normalized versions hold to equality. The (N=6) raw threshold is 0.4206007, and both normalized versions relabel only across (b=1). The exact (N=8) raw threshold is approximately 0.3302, not approximately 0.5; the deposited coarse ramp labeled the first sampled post-transition value rather than locating the crossover.

**Computation grade: PASS (A).** Independent implementation, exhaustive partition enumeration, exact model construction, deterministic results, and successful syntax/run checks. Numerical caveat: log determinants and root location use double-precision linear algebra; transition identities are stable far beyond the precision material to the claim.

## B. Primary-source line check

Primary source: Miguel Aguilera and Ezequiel A. Di Paolo, [“Integrated information in the thermodynamic limit,” *Neural Networks* 114 (2019), 136–146](https://doi.org/10.1016/j.neunet.2019.03.001), published open-access version inspected.

Their Eq. 5 defines each partition's value as an unnormalized Wasserstein distance between the intact and partitioned conditional distributions. Their MIP definition then minimizes that partition value directly; no size or entropy normalizer appears. The paper makes the resulting small-side behavior explicit:

> “For infinite size systems where inter-region connections are not zero, the MIP will be one of the possible partitions that isolate just one node.”

Accordingly, Aguilera and Di Paolo's MIP selector is **raw/unnormalized**. Their paper does not support the work order's proposed reading that the canonically cited MIP is entropy-normalized or size-normalized.

`phaseD1` therefore computes the canon's explicitly declared static-Gaussian quantity—raw Gaussian mutual information minimized across bipartitions—and its raw argmin convention matches the cited paper. It is not, however, a literal implementation of Aguilera and Di Paolo's φ: their model is a dynamical kinetic Ising system and their partition distance is Wasserstein, whereas `phaseD1` uses static Gaussian covariance and mutual information. The accurate description is **source-aligned MIP convention, different model and partition-distance measure**, not “non-canonical unnormalized implementation.”

**Reading grade: PASS (A).** The published primary text, equations, MIP definition, and explicit singleton statement were checked. This finding contradicts Job B's anticipated normalized-source premise.

## C. Evidence location for the two §13a claims

| §13a claim | What the deposited script actually computes | Evidence status |
|---|---|---|
| **Claim 1:** the grain maximizing Φ_MIP moves module → whole | No coarse-grained module-level covariance, no two-supernode Φ, no candidate-grain score table, and no maximization across grains appear in `phaseD1`. | **Not computed by the deposited evidence inspected.** |
| **Claim 2:** the whole's MIP leaves the module boundary | `phaseD1` computes Σ for one full eight-node graph, enumerates its bipartitions, and tracks the raw minimum cut as (b) changes. | **Computed, but only for the raw selector.** |

The script's header and print statements call the MIP-location change a module-to-whole grain transition, but the algorithm performs no cross-grain comparison. The later moving-MIP and normalized-MIP deposited scripts also analyze partitions of the full graph; they do not supply the missing two-supernode-versus-whole calculation. Thus the evidence supports claim 2 only. Claim 1 remains an inference that requires a separately declared coarse-graining map and an actual comparison of Φ across candidate grains.

## Secondary normalization-robustness check

For the §13a level-selection application, the live canon's statements that individuation ordering is “robust across minimum-partition normalizations” and “normalization-robust within the minimum-cut family” are contradicted by Job A. Changing only the normalizer moves the MIP transition from (b\approx0.3302/0.4206) to (b=1) and changes the winning cut from singleton to balanced. This finding is scoped to **MIP location and the level-selection interpretation**; it does not by itself re-test every earlier between-system scalar ordering to which the canon may also apply the phrase.

## Verified and not verified

Verified: live canon currency; exact §13a wording; all specified (N=6) and (N=8) selectors; raw and normalized transition locations and winning cut types; Aguilera and Di Paolo's raw MIP convention; and the computational scope of deposited `phaseD1` plus the later full-graph MIP scripts.

Not verified: a genuine cross-grain Φ comparison, because the deposited evidence does not contain one and the work order does not specify the coarse-graining map needed to construct it; any philosophical claim that a singleton raw MIP is or is not intrinsically the correct individuation signal; any non-Gaussian or larger-(N) generalization; or any canon correction. The master was not touched, and no deposited script was executed.
