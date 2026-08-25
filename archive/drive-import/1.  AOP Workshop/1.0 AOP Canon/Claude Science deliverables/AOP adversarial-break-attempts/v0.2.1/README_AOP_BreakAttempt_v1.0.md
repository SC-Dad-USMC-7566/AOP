# AOP break attempt — v0.2.1 Intervention Contract

**Deposited:** 2026-08-07 · **Seat:** Claude Science (attack seat)
**Target:** `AOP_InterventionContract_FourAxis_v0.2.1_20260807` (Drive id `11C1Tmnt00ixoDp4KsPcJ2Q_pF_82g59h`)
**Parent canon:** `AOP_CANON_MASTER_v1.27` (Drive id `1PZdsto8bRLB1SgoAYnGfOvAjCuygFklD`)
**Review the target claims to implement:** `REV_AOP_InterventionContract_v0.2_GateReadiness_20260807`

**Status:** Non-canon. Authorizes no canon edits. The seat that produced this did **not**
build v0.2 or v0.2.1, and did not run any part of the gate on its own work.

---

## What is in this folder

| File | What it is |
|---|---|
| `AOP_Break_MathAttack_v0.1.md` | **Start here.** The analytic attack: four fatal findings (F0a, F0b, F1, F2), three major (F3–F5), each with closed-form derivation and a disposition mapped to the contract's own kill conditions. Ends with an explicit ledger of attacks that **failed**. |
| `AOP_Break_FidelityAudit_v0.1.md` | 28 canon cross-references graded FAITHFUL / DRIFTED / UNSUPPORTED / CONTRADICTS; all 8 Aster items and 8 P-fixes judged for discharge (5 undischarged, 11 partial). |
| `AOP_Break_CitationSalvage_v0.1.md` | Primary-source verification. **Partial lane** — see "Open items" below. Items that could not be retrieved are marked NOT VERIFIED, not passed. |
| `AOP_Break_Figure_v0.2.png` | Five panels: (a) σ even / ΔV odd in affinity; (b) mirror pairs at identical σ and E; (c) unbounded σ with vanishing ΔV; (d) the Even-Process ladder against k·2^(−k/2); (e) the increment-representation trap. |
| `AOP_BreakAttempt_SKILL_v1.0.md` | The reusable method this exercise produced, published as a Claude Science skill. Readable as a standalone protocol. |
| `AOP_BreakAttempt_kernel_v1.0.py` | The skill's computational helpers. Pure Python + numpy; runs anywhere. 15/15 regression checks against the verified numbers below. |

## The four fatal findings, in one line each

- **F0a — increment-representation trap.** Canon Figure DM's caption warns that the increment
  representation of that ring "preserves σ exactly while sending E to zero." Model 4 *is* that
  ring, its state is never fixed to position, and the warning is absent. Computed: σ agrees to
  <1e−12 across representations while E is **exactly 0**. A seat declaring increments reports a
  false refutation of σ>0 ⇒ E>0 — in the panel where §6 pre-told it to expect that edge.
- **F0b — CBSD is the demoted proxy.** Canon Table 1 keeps B5 = I(in;out) "only as a descriptive
  quantity... not boundary strength" and leads with B1/B2/B4. CBSD *is* B5. Canon §8 already
  computed the dissociation (B2 = 0.000 vs B5 = 0.896 nats sealed; 0.292 vs 1.685 bypassed).
- **F1 — Drive contrast is sign-indeterminate.** ΔV_Drive = 2/c − MFPT has numerator a(2a−c), so
  sign(ΔV) = sign(a−c/2). σ is **even** in the cycle affinity, ΔV is **odd**. The sign also flips
  with which first-passage target V measures — a choice §2's eleven mandatory fields never require
  recording. Two seats to spec, opposite answers.
- **F2 — the Even-Process ladder saturates.** ρ_k ∝ k·2^(−k/2) → 0, from an exact two-rung
  recurrence ratio (k+1)/(2k−2) → 1/2. Crutchfield & Feldman 2003 independently report the matching
  exponent γ = 0.501 ± 0.007 — in the paper the contract cites for E itself.

**Verdict:** §11.2 stays **OPEN**, for a different reason than Aster's. The gate is now specified
enough to run; running it on the designated Drive control gives a sign that depends on an undeclared
choice. Reported honestly, F1 becomes the Drive axis's own scope condition.

## Verified reference values (all closed-form or exact; nothing sampled)

| Quantity | Value |
|---|---|
| Golden Mean excess entropy | E = 0.2516291674 bits; ρ_k = 0 exactly for k ≥ 1 |
| Even Process | E ∈ [0.917810, 0.918493]; hµ = 2/3; Cµ = H(2/3,1/3) = 0.9182958 |
| Even ladder decay | two-rung ratio (k+1)/(2k−2) → 1/2; per-rung → 1/√2 |
| Ring (a,b) = (0.48, 0.12), position rep. | σ = 0.720000 bits/step, E = 0.180855 bits |
| Ring same rates, increment rep. | σ = 0.720000 (preserved), **E = 0 exactly** |
| Ring MFPT(0→1) | 2.380952 vs 3.333333 at the detailed-balance null |
| Two-state, one channel / two channels | σ = 0 / σ = 3.767867 nats/time |

## Open items — NOT verified, do not report as cleared

1. **K&W "Eq 5.2 / 5.14", "§5.1.1 / §5.2".** doi 10.1098/rsfs.2018.0041 resolves via Unpaywall to
   the arXiv preprint, which uses roman-numeral sectioning and contains none of those decimal
   numbers. Needs the *Interface Focus* published version. `AOP_KW2018_Verification_SpineClaims_20260806`
   is cited as having verified these — re-read it to see which version it checked.
2. **Spinney & Ford 2012 / Ford & Spinney 2012** — the odd/even-variable entropy-production
   decomposition behind canon §4 condition 3. Nobody in this session read it.
3. **Schnakenberg 1976** (or equivalent) for the cycle-affinity formula and Kolmogorov criterion —
   would put F5's correction on a cited footing rather than computation alone.

## A canon-side ticket, independent of this contract

Canon §4 cites reference **[13]** for E = 0 ⟺ i.i.d., but [13] is Crutchfield, Ellison & Mahoney,
"Time's barbed arrow" (2009) — not Crutchfield & Feldman 2003. This sits inside the section whose
purpose is correcting a citation error. Worth fixing before the paper leans on the theorem.

---

*Non-canon attack report. Every finding bounds what the co-measurement method can claim; none
rejects AOP, whose claims live in the canon independently.*
