# AOP — Integration vs Rival P: one-way kill check

**File:** `AOP_Integration_vs_RivalP_KillCheck_v0.1.md` · **Version:** v0.1
**Date:** 25 July 2026 · **Seat:** Claude Cowork (execution)
**Order:** `TASK_CW_AOP_Aster_Triage_20260725` §3
**Code deposited alongside:** `integration_vs_rivalP.py` (closed-form; no Monte-Carlo; regenerates every number below)

---

## 0. Result, stated first

**They cannot differ on the scored kinase grid. That is the negative branch, and it is what this run returned.**

On the fully-crossed published kinase design — the eight-genotype grid of `AOP_Benchmark_Sporulation_Conditions_REDACTED_v0.1.md` §4.1 — the canon's Integration measure is a **strictly monotone function of the number of surviving kinases**, which is exactly the statistic Rival P thresholds. A single threshold on Integration reproduces Rival P's labels on all eight conditions, under every declaration setting tested (2 partitions × 3 coupling constants × 2 normalizations × 2 Integration quantities). Integration carries no information about this system beyond the path count, and it is blind to precisely the combinatorial structure the published design was built to expose.

**AOP's only topology-computable axis is, on this system, a graded relabelling of path-counting.** Reported plainly, as the order requires.

The one place the two do come apart is stated in §5 and is **not** a point in AOP's favour: Integration and Rival P diverge only where node deletion disconnects the graph or strips its inputs, and where they diverge, Integration ranks the fully de-kinased triple mutant as the **most integrated** system on the grid.

---

## 1. Scope, and what this section is not

This is not the desk-based discrimination check. Claude Science's Step 0 established that AOP's axes are not computable on topology alone: Drive is identically zero at detailed balance for every graph, and Memory is undefined without a declared process. Neither is computed here and neither is claimed.

**Exactly one question is asked**, the one Step 0 left well-posed without rates: Integration computes in closed form on topology plus a partition, Rival P is a functional of connectivity, and both are functionals of the same graph — so **can they differ?**

**Contamination disclosure, per the order.** This seat has read the sporulation answer key and is therefore biased toward wanting the "they differ" branch. **No outcome was used in this computation.** The inputs were the published wiring and the redacted conditions file's perturbation grid; the code contains no titre, frequency, direction, or ranking. The asymmetry in §5 is honoured: the negative branch is treated as informative and is not softened; the divergence is not treated as a green light.

---

## 2. Declarations (Task 3.1 requires these explicit)

**S — system variables / the declared partition into parts.** One node per named molecular species of the phosphorelay.

- Baseline node set **N₀** = {KinA, KinB, KinC, Spo0F, Spo0B, Spo0A} — six nodes.
- Variant node set **N₁** = N₀ ∪ {PhosF, PhosA} — the phosphatase drains carried as explicit nodes (a Rap-type drain on Spo0F, a Spo0E-type drain on Spo0A). The order names "phosphatase drains" in the wiring; the conditions file supplies no quantitative material for any phosphatase or inhibitor arm, so the drains are carried as a **declaration variant, not as a fitted feature**, and every result is reported under both.

**Wiring, as published.** KinA→Spo0F, KinB→Spo0F, KinC→Spo0F, Spo0F→Spo0B, Spo0B→Spo0A; drains PhosF—Spo0F, PhosA—Spo0A in N₁.

**P — the partition the minimum cut searches over.** All bipartitions of the declared node set. The search is **exhaustive** over the 2ⁿ⁻¹−1 bipartitions; no partition is pre-selected, matching the canon's "exhaustively-searched minimum information partition" (v1.26 §4, line 472).

**M — model class.** Static Gaussian. **Σ = (I + gL)⁻¹**, with **L = D − A** the combinatorial Laplacian of the **undirected, unit-weighted** wiring graph.

> **Symmetrization is forced, and it is load-bearing.** (I + gL) must be symmetric positive definite for Σ to be a covariance, and the canon's construction is defined on an undirected L. **Direction is therefore not available to Integration at all.** This is declared, not buried: it is the mechanism by which Integration loses the only structure that could have distinguished it from an undirected connectivity statistic. Unit weights are likewise forced — the wiring supplies no rates (Step 0).

**g — coupling constant.** Baseline **g = 1.0**. Swept over **0.1, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0**. Sensitivity reported in §4.3: **g rescales every value and changes no ordering, no zero, and no verdict.**

**N — normalization.** Two reported: raw minimum-cut mutual information in nats, and minimum-cut MI divided by min(|A|,|B|). Both give the same verdict.

**Perturbation.** Node deletion — remove the node and all incident edges — matching a gene disruption. Conditions are taken verbatim from the redacted conditions file: §4.1 kinase grid (JH642, AG522, NY120, JRL920, NY121, JRL1046, JRL1004, JRL1007) and the three in-scope relay-core genotypes from §4.2 (`spo0A`, `spo0F`, `spo0B`). `spo0E`, `spo0J`, `spo0K` appear in the published §4.2 design but lie outside the §1 in-scope gene list and are not represented in the wiring; `kinD`/`kinE` are out of scope by the conditions file.

**Integration quantities computed.** Both canon Integration-panel objects that are closed-form on topology plus partition: **TC** (total correlation, the Integration axis proxy) and **Φ** (minimum-cut dependence, formerly Φ_MIP, canon v1.26 §4).

---

## 3. Task 3.2 — Rival P's labels

Rival P: near-WT if ≥1 directed path from a surviving kinase to Spo0A remains; collapse if zero remain. Computed on the **directed** graph.

| Strain | Genotype | Directed kinase→Spo0A paths | Rival P |
|---|---|---:|---|
| JH642 | wild type | 3 | near-WT |
| AG522 | `kinA` | 2 | near-WT |
| NY120 | `kinB` (+`kapB`) | 2 | near-WT |
| JRL920 | `kinC` | 2 | near-WT |
| NY121 | `kinA kinB` | 1 | near-WT |
| JRL1046 | `kinA kinC` | 1 | near-WT |
| JRL1004 | `kinB kinC` | 1 | near-WT |
| JRL1007 | `kinA kinB kinC` | 0 | **collapse** |
| — | `spo0A` | 0 (target deleted) | **collapse** |
| — | `spo0F` | 0 (relay severed) | **collapse** |
| — | `spo0B` | 0 (relay severed) | **collapse** |

---

## 4. Task 3.1 — Integration, and the kill signal

### 4.1 Baseline, g = 1.0, drains OFF (node set N₀)

| Genotype | n | TC | Φ (raw) | Φ / min\|·\| | argmin cut | Rival P |
|---|---:|---:|---:|---:|---|---|
| wild type | 6 | 0.38678 | 0.060680 | 0.030340 | {Spo0B, Spo0A} | near-WT |
| `kinA` | 5 | 0.35126 | 0.071550 | 0.035775 | {Spo0B, Spo0A} | near-WT |
| `kinB` | 5 | 0.35126 | 0.071550 | 0.035775 | {Spo0B, Spo0A} | near-WT |
| `kinC` | 5 | 0.35126 | 0.071550 | 0.035775 | {Spo0B, Spo0A} | near-WT |
| `kinA kinB` | 4 | 0.30075 | 0.087177 | 0.043588 | {KinC, Spo0F} | near-WT |
| `kinA kinC` | 4 | 0.30075 | 0.087177 | 0.043588 | {KinB, Spo0F} | near-WT |
| `kinB kinC` | 4 | 0.30075 | 0.087177 | 0.043588 | {KinA, Spo0F} | near-WT |
| `kinA kinB kinC` | 3 | 0.22314 | **0.111572** | 0.111572 | {Spo0F} | **collapse** |
| `spo0A` | 5 | 0.30830 | 0.077075 | 0.077075 | {KinA} | **collapse** |
| `spo0F` | 5 | 0.14384 | **0.000000** | 0.000000 | {KinA} | **collapse** |
| `spo0B` | 5 | 0.27348 | **0.000000** | 0.000000 | {Spo0A} | **collapse** |

### 4.2 The two findings that carry the section

**(i) Integration is a function of the kinase count and of nothing else.**

All three single mutants return **numerically identical** TC and Φ. All three doubles return numerically identical TC and Φ. This is not a coincidence of the numbers: under unit weights the three kinases are **graph automorphic**, so no undirected functional of the wiring can distinguish `kinA` from `kinB` from `kinC`, or `kinA kinB` from `kinB kinC`. The published design's entire combinatorial content — which kinase, which pair — is invisible to Integration **by construction**. Recovering it would require rate weights, which Step 0 established the wiring does not supply.

**(ii) On the kinase grid, Integration is order-isomorphic to Rival P's path count.**

| Surviving kinases | Φ (g=1, drains OFF) | TC |
|---:|---:|---:|
| 3 | 0.060680 | 0.386778 |
| 2 | 0.071550 | 0.351261 |
| 1 | 0.087177 | 0.300751 |
| 0 | 0.111572 | 0.223144 |

Φ is a strictly increasing function of *kinases deleted*; TC is strictly decreasing. Either is a bijective relabelling of the count 3, 2, 1, 0 — which is Rival P's path count exactly. A single threshold on Φ (or on TC) reproduces Rival P's eight labels with no error.

Machine check, `separability()` in the deposited code, over all six declaration settings:

| Setting | Kinase grid (8 conditions): single threshold reproduces Rival P? | All 11 conditions? |
|---|---|---|
| drains OFF, g = 0.25 | **yes** | no |
| drains OFF, g = 1.0 | **yes** | no |
| drains OFF, g = 5.0 | **yes** | no |
| drains ON, g = 0.25 | **yes** | no |
| drains ON, g = 1.0 | **yes** | no |
| drains ON, g = 5.0 | **yes** | no |

`order_isomorphism()` returns `PHI is a FUNCTION of path count: True` and `PHI is STRICTLY MONOTONE: True` in all six.

### 4.3 g-sensitivity

Φ over g ∈ {0.1 … 10}, drains OFF:

| Genotype | g=0.1 | g=0.25 | g=0.5 | g=1.0 | g=2.0 | g=5.0 | g=10.0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| wild type | 0.003068 | 0.011787 | 0.028045 | 0.060680 | 0.123067 | 0.281425 | 0.472986 |
| any single kinase | 0.003286 | 0.013235 | 0.032502 | 0.071550 | 0.145008 | 0.324279 | 0.532223 |
| any double | 0.003538 | 0.015089 | 0.038646 | 0.087177 | 0.176570 | 0.383284 | 0.610538 |
| triple | 0.003831 | 0.017546 | 0.047655 | 0.111572 | 0.225993 | 0.470492 | 0.720605 |
| `spo0A` | 0.003322 | 0.013699 | 0.034496 | 0.077075 | 0.155077 | 0.336865 | 0.542727 |
| `spo0F` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| `spo0B` | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 | 0.000000 |

**g is a scale, not a discriminator.** It multiplies every value monotonically, preserves every ordering, and cannot move an exact zero. No choice of g rescues discriminating power, and no choice of g changes any verdict in this note. The exact zeros are topological (a disconnected graph gives a block-diagonal Σ, so the minimum cut is exactly independent) and are g-invariant by construction.

---

## 5. Task 3.3 — where they *can* differ, and why it establishes nothing

Over the full eleven conditions no single threshold on Integration reproduces Rival P, under either partition. The divergences:

| Condition | Φ | Rival P | Disagreement | Robust to the drain declaration? |
|---|---:|---|---|---|
| `kinA kinB kinC` | **maximal** on the grid (0.1116 OFF / 0.0835 ON) | collapse | Integration ranks it the **most integrated** system tested | **yes** — under both partitions |
| `spo0A` | 0.0771 (drains OFF) / **0** (drains ON) | collapse | Integration places it mid-band under one partition, at exact zero under the other | **no** — the verdict flips with a declaration choice |
| `spo0F`, `spo0B` | 0 | collapse | none — they agree | yes |

**This is not discriminating power. Read against the order's asymmetry, it is not-killed at best, and it is closer to a second negative.** Three reasons, stated rather than softened:

1. **The sign is backwards.** The condition Rival P calls collapse because every input is gone is the condition Integration scores highest. Deleting leaves from a graph raises the minimum cut over the surviving chain; that is an artifact of node removal, not a statement about persistence. Anyone reading Integration as tracking viability here would read it exactly wrong.

2. **Where Integration does hit zero it is reporting graph disconnection, not viability.** `spo0F`∆ isolates all three kinases; `spo0B`∆ severs Spo0A. Σ goes block-diagonal and Φ = 0 exactly. Rival P reaches the same labels from the same disconnection. Both are reading connectivity; only one of them claims to be reading anything else.

3. **One divergence is a declaration artifact.** `spo0A`∆ scores 0.0771 with drains off and exactly 0 with drains on. Choosing the partition that produces the "right" answer would require knowing the answer — which is circular, and is the failure mode the whole benchmark exists to avoid.

There is also a comparability problem underneath all of this that cuts the same way: node deletion changes n, so Φ and TC are being compared **across different-sized systems**. The canon supplies no normalization that makes that comparison safe (v1.26 §1/§2 explicitly deny a common normalization), and the `Φ/min|·|` variant does not fix it. Every cross-condition Integration comparison in §4 inherits that weakness — which weakens the divergences of §5 further, not the kill signal of §4, since the §4 result is an ordering within a single monotone family.

---

## 6. What this does and does not establish

**Establishes (negative, and the order says to report it plainly):** on the *B. subtilis* sporulation phosphorelay, under the only construction the canon licenses for topology-plus-partition input, the Integration axis is a graded relabelling of path counting on the scored kinase grid, and it is blind to which kinase or which pair was removed. If the benchmark's discriminating power is to come from anywhere, it does not come from here.

**Does not establish:** anything about the other three axes; anything about the benchmark's viability overall; anything about whether AOP is right. Per Step 0, the AOP prediction is a three-place semantic weight requiring a declared viable set and a functional V, and the wiring supplies neither. **One axis is not the prediction.**

**Not attempted, per order §§0 and 5:** Phase B; any answer key; any new candidate system; any use of the sporulation outcomes; any verification of v1.26; any adjudication of an Aster blocker; any re-attempt at the Drive→Memory proof.

**Not graded by this seat.** The code is deposited so prime, or a clean seat, can re-run rather than re-read. The result above is the negative branch, and this seat has the bias that would have made it want the other one.

---

## 7. Reproduction

`integration_vs_rivalP.py` — closed-form throughout (`numpy.linalg.inv`, `slogdet`, exhaustive bipartition enumeration). No random seeds, no sampling, no fitting. Running it regenerates §4.1, §4.2, §4.3 and §5 verbatim, including the `order_isomorphism()` and `separability()` machine checks.

---

*End of `AOP_Integration_vs_RivalP_KillCheck_v0.1.md` v0.1. Produced by the execution seat under contamination disclosure. Prime verifies by re-running, not by reading.*
