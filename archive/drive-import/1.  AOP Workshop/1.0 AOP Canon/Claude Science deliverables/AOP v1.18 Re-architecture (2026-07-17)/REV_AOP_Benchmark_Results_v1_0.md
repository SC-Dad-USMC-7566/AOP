# AOP Benchmark — Results and Exit-Gate Verdict

**Status:** results for OAI Phase 4, scored against `REV_AOP_Benchmark_Preregistration_v1_0.md`. Non-canonical. **Compiled:** 17 July 2026. All numbers from `aop_benchmark_ctmc.py` / `benchmark_results.json`; figures `fig_benchmark_dissociation.png`, `fig_benchmark_hypergraph.png`.

**Model validity:** generator rows sum to zero (max |row-sum| = 2×10⁻¹⁵); survival monotone-decreasing in τ. Run valid. Baseline **V(τ=15) = 0.9302**; QSD metastable lifetime ≈ 159.

---

## 1. Headline numbers (τ=15, v_min=0.60)

| Mechanism | Structural rate | MI signature (bits) | Single-edge ΔV | Shapley φ | Ground-truth class |
|---|---|---|---|---|---|
| **Z** | **1.400 (highest)** | **0.151 (highest)** | **0.0000** | **0.0000** | inert spectator |
| A | 0.720 | 0.016 | 0.0000 | 0.2665 | redundant |
| B | 0.720 | 0.016 | 0.0000 | 0.2665 | redundant |
| S1 | 0.340 | 0.016 | 0.1180 | 0.0844 | synergy |
| S2 | 0.340 | 0.016 | 0.1180 | 0.0844 | synergy |
| **R** | 0.209 (low) | 0.016 (low) | **0.1629 (highest single ΔV)** | 0.1924 | load-bearing |
| C | 0.055 | 0.000 | 0.0081 | 0.0193 | weak-but-real |

**Coalition / Möbius:** h(A,B) = **+0.4379**; h(S1,S2) = **−0.1180**; h(A,R)=h(A,C)=h(C,Z)=h(A,Z)=0.
**Minimal failure cut-sets:** {A,B}, {R,S1}, {R,S2} — **no single mechanism is a cut-set.**
**Minimal viability-preserving sets:** {A,R}, {B,R}, {A,S1,S2}, {B,S1,S2}.
**Rank dissociation:** Spearman(rate, single-ΔV) = **−0.667**; Spearman(MI, ΔV) = **−0.136**.

## 2. Preregistered test verdicts

| # | Prediction | Result | Verdict |
|---|---|---|---|
| **T1** strong-but-inert | Z highest strength, ΔV=0 | Z is #1 by both rate (1.40) and MI (0.151); ΔV(Z)=φ(Z)=0 exactly | **PASS** |
| **T2** weak-but-load-bearing | R low strength, highest single ΔV | R rate 0.209 (2nd lowest), MI tied-low; ΔV(R)=0.163 = largest single-edge | **PASS** |
| **T3** edge-attribution failure | ΔV(A)=ΔV(B)=0, ΔV(A,B) large | 0.000, 0.000, 0.438 | **PASS** |
| **T4** hypergraph recovery | h(A,B)>0, h(S1,S2)<0, cut-sets match | h(A,B)=+0.44, h(S1,S2)=−0.12; cut-sets {A,B},{R,S1},{R,S2}; R⇄{S1,S2} route recovered | **PASS** |
| **T5** horizon robustness | T1–T4 signs hold over τ∈{8..30} | h(A,B)>0 in 5/5; h(S1,S2)<0 in 5/5; ΔV(Z)=0 in 5/5; ΔV(A)=ΔV(B)=0 in 5/5 | **PASS** |
| **T6** rival discrimination | deferred to Phase 5 | — | deferred |

## 3. Controls

| Control | Result | Pass |
|---|---|---|
| Detailed-balance (ρ=0, f=w) | base 0.767, ΔV(R)=0.0000 (R inert with nothing to suppress) | ✓ |
| Inert spectator Z | ΔV(Z)=0, h(·,Z)=0 exactly | ✓ |
| Common-input confound | MI(z;r)=0.151 bits, ΔV(Z)=0 | ✓ |
| Redundant bypass {A,B} | single 0.000 / joint 0.438, h=+0.44 | ✓ |
| Synergistic pair {S1,S2} | 0.118=0.118=0.118, h=−0.12 | ✓ |
| Budget-shift | ΔV(R)=0.163; with +0.15 compensating influx ΔV(R)_eff=0.114 (>0) | ✓ |
| Inadmissible (ρ=1.8) | V=0.974 vs 0.930 — large change, causally meaningless (negative death rates); labeled inadmissible | ✓ |

## 4. The honest exit-gate adjudication

**What is guaranteed by construction (NOT a discovery).** I built A,B redundant, S1,S2 synergistic, Z inert, R load-bearing. That the coalition ΔV pattern *matches* these classes is therefore not evidence for anything except that the code computes what I specified. A benchmark must have known ground truth; claiming the recovery of ground truth as a scientific finding would be circular, and I do not.

**What could have failed, and is the actual result (the non-triviality payload).**
1. **The rank inversion (T1+T2) was not forced by the tuning.** I tuned rates only to reach a metastable regime. Nothing in that tuning required that the *highest-strength* mechanism (Z) be the *zero-importance* one, nor that the *lowest-strength* driven mechanism (R) carry the largest single-edge effect. That the strength/importance Spearman came out **negative** (−0.67), rather than merely weak-positive, is a computed outcome that a one-axis reader would get exactly backwards. This clears the gate's rank-inversion bar.
2. **The Möbius sign inversion (T4) is a genuine derived result.** The naive reading "h>0 ⇒ synergy, h<0 ⇒ redundancy" is *inverted* here: the redundant pair gives h=+0.44 and the synergistic pair gives h=−0.12. This is a real trap the benchmark demonstrates, not a specification — I did not set the signs, the CTMC solution did.
3. **The R ⇄ {S1,S2} substitutability is emergent.** I did not design two interchangeable maintenance routes; the minimal viability-preserving sets {A,R} and {A,S1,S2} fell out of the closed-form solution. This is structure the method *found* rather than structure I planted.

**Verdict: GO (non-triviality bar cleared).** At least one preregistered result (in fact T1, T2, T4) is not guaranteed by construction, could have failed the stated criteria, and inverts the classification a naive strength/correlation reading would assign. The coalition-competence gate (D) is also cleared: the method detects the redundant-bypass and synergistic-pair controls without misreporting either as an independent edge effect.

**What this does NOT establish (scope discipline, per ADR-003).** GO here means the benchmark **clears the non-triviality bar** — the AOP method produces information a one-axis reading does not, on a system where the answer was not readable from coupling strength. It does **not** establish that AOP is the uniquely correct framework, nor that it beats every rival (that is Phase 5's bounded, single-named-rival comparison, and even a favorable result there is an acceptable *Perspective* result, not an adjudication). The benchmark is a keystone existence proof: "here is a system where the four-target, coalition-aware, viability-anchored method is necessary to get the right answer." That is what a Perspective needs, and no more than it can support.

## 5. Attribution-failure reporting (per protocol)

For the redundant pair {A,B}, the per-edge-weight conditions (isolability, additivity) **fail by design**: no scalar weight on edge A or edge B can represent a coupling whose single-edge effect is zero and whose joint effect is 0.44. The benchmark reports this as **edge attribution unresolved for {A,B}**, with the coalition value h(A,B) and the cut-set {A,B} as the primary objects — exactly the two-layer (syntactic edge / semantic mask) move the canon prescribes, here shown to be *necessary* rather than stylistic.
