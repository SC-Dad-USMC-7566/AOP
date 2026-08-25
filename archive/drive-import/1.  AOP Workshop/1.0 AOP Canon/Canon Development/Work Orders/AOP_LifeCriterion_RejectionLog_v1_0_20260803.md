# Gate 1 — REJECTION LOG

**Document ID:** `AOP_LifeCriterion_RejectionLog_v1_0_20260803.md`
**Seat:** Claude Science (builder). **Date:** 3 August 2026.
**Required by:** anti-gaming clause 2 of `AOP_LifeCriterion_DispositionRule_FROZEN_v1_0_20260801.md`
(md5 `b7eebcfd5a371a78b33a5fe230d52554`, verified this session).
**Standing:** an explicit attack target for OAI at Gate 1. Written to be attacked.
**Supersedes** the v0_1 interim log of 2 August. All five retrieval tracks have reported.

**One criterion is named as operative per rejection** — the earliest in the S-order that is decisive on
retrieved evidence. Additional failures are listed but are not the operative ground.

---

## Rejected as positive article

| # | Candidate | Operative | Reason | Retrieval |
|---|---|---|---|---|
| 1 | *E. coli* chemotactic adaptation (receptor methylation) | **S.2** | The slow variable (methylation) is the integrator state, not a stored target. Yi et al. Eq. 1 gives the adapted activity as a closed-form function of CheR/CheB rate constants **in which the methylation level does not appear**; under CheR saturation it reduces to K_b·Vmax_R/(Vmax_B−Vmax_R). Target is a ratio of rate constants. Additional: S.5 WEAK. **Not rejected on S.3 — S.3 passes**, contrary to the order's expectation. | `[primary-verified]` **[parent-reverified]** |
| 2 | Synthetic antithetic integral feedback controller | **S.2** | The integrator state is dZ = Z₁−Z₂; the target is μ/θ, a ratio of two kinetic rate constants and the zero of that state's rate law. Verified from the equations in two independent primaries. Additional: S.5 WEAK — the regulated variable is a reporter, so the reference is for an arbitrary target, not the system's own viable set (component 5). | `[primary-verified]` |
| 10 | *E. coli* heat-shock response (σ32) | **S.2** | Rejected **as positive article only**; reassigned to negative control, where the S.2 failure is the qualification. No slow variable stores a target; σ32 is the fastest component and its level is the output of a rate balance. The modelling authors describe their own steady state as a setpoint dictated by the balance of synthesis and degradation rates. Additional: S.3 fails. | `[primary-verified]` |
| 13 | Hypothalamic thermoregulation / fever | **S.1** | No published quantitative dynamical description with a declared slow variable retrieved. Additional: **S.4** fails outright. Further and independently disqualifying: the field disputes whether the shifted object is a stored reference at all, so selection would make AOP's central distinction hostage to a live physiology controversy. **S.3 is genuinely strong and is not the reason for rejection.** | `[primary-verified]` for the model absence; `[primary-abstract-only]` for the PGE2 claim |
| — | Genome-scale flux-balance models | **S.1** | Ineligible on the face of the order: "not eligible." Not evaluated. | n/a |
| — | Structure-only / wiring-diagram-only candidates | **S.1** | Rejected at that line; Step 0 established the axes are not computable from a wiring diagram. | n/a |
| — | AOP's canonical star | **S.1** (intervention class) | The order states it: cannot be intervened on. Retained as the conceptual reference for a model-free corrector. | n/a |

## Excluded by ruling, not by criterion

| # | Candidate | Basis |
|---|---|---|
| 5 | *B. subtilis* sporulation phosphorelay | **Ben's §0(a) ruling.** Reserved to the external benchmark (H4/RED-25). Recorded so the exclusion is visibly a ruling and no future seat re-litigates it as a scored rejection. |

## Not rejected — assigned to the negative-control role (S.2 failure is the qualification)

| # | Candidate | Standing |
|---|---|---|
| 8 | **EnvZ/OmpR** | **Recommended negative control.** Model-free evidenced from two independent closed forms; both readings agree on exclusion. Two open issues in report §3.3: dynamic restoration of OmpR-P `[not-retrieved]`, and a live P1 threat (§3.3.1). |
| 10 | σ32 heat shock | Alternative negative control — adds a STRONG lifetime readout, at the cost of failing S.3 too (less probative). |
| 11 | Negative autoregulation | Third option — cleanest model-free architecture, but **"demonstrably corrects" is not established**. |
| 9 | NRI/NRII | Backup, same bifunctional architecture. |

## Longlisted, not reached

Yeast HOG; yeast GAL; *E. coli* DNA repair; phage λ; mammalian/*Drosophila* clock; leptin/adiposity;
end-product feedback inhibition. **The pair was found outside all five benchmark systems, so none of
their literatures was read and no contamination cost was incurred.**

---

## Rejections this log deliberately does NOT make

Recorded because their absence is a decision, and an attacker is entitled to see it was deliberate.

1. **No candidate is rejected for having been rejected by the external benchmark.** The order forbids
   it and the filters differ.
2. **A.1.9 is not applied anywhere.** It is a frontier heuristic about redundant architecture on five
   observations, and its own records file says it must never close a candidate alone.
3. **No candidate is rejected under Reading A alone.** Every rejection above holds under **both**
   readings. For the antithetic controller this was checked explicitly: Reading A excludes it, Reading B
   would admit it, and the target-as-parameter filter cuts it under both — so no rejection is contingent
   on Gate 1's unadjudicated ambiguity. **This is the log's main structural claim and the place to
   attack it.**
4. **KaiABC is not rejected on S.4** despite PARTIAL (~10× vs the required ≥2 orders). S.4 is a
   screening criterion, not a disqualifier under the order's phrasing for the positive article, and **no
   candidate found does better** — rejecting on it would empty the field. The consequence (P2 heading
   for UNINFORMATIVE by construction) is priced in report §6.3 rather than hidden.
5. **KaiABC is not rejected on the environmental-model objection** (that a clock models external time
   rather than its own viable set). That is a criterion-interpretation question for prime, not an
   empirical finding, and canon v1.26's "declared persistence criterion" framing bears on it directly.
6. **Chemotaxis is not rejected as a negative control**, only as the positive article. It fits neither
   offered slot cleanly — it is not model-free in the ordinary sense, since it corrects via an internal
   dynamical variable. Its value is as a **near-miss discriminating Reading A from Reading B**, a third
   category the pairing scheme lacks.

---

*End of `AOP_LifeCriterion_RejectionLog_v1_0_20260803.md`. Builder's proposal. Not self-certified.*
