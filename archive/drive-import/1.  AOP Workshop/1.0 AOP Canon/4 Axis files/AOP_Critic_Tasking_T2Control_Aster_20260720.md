# Critic Tasking — T2 Control Attack (for Aster / OAI)

**Compiled:** 20 July 2026 by Claude (prime), for Aster (OAI, outside critic). Non-canonical record.

**Role & governance.** Aster is the outside critic — attack the work, find what the rest of us missed. Builder (Claude Science) proposes, prime (Claude) verifies by re-running, Aster attacks, Ben decides. Nobody trusts a report they didn't independently reproduce. Findings go in one file in the Drive folder. Do NOT edit the canon or any `..._Preregistration_...` file — frozen preregs stand as pre-commitments.

## What just happened

The external *E. coli* / Keio benchmark was hardened. After the v1.1 fixes and a new T2 specificity control, the builder reports **no AOP-specific empirical advantage** on this system: T1 essentiality weak (~0.66), inherited from standard FBA; T3 fails on honest labels; T4 falsified (+0.61); and the one apparent win (T2 synthetic-lethal pairs) is now claimed **reproduced by a plain double-knockout screen with no AOP machinery**. Prime believes this read is probably right but has NOT independently re-run the control. That is Aster's job.

## Where to look

`AOP` → `Claude Science deliverables` → `AOP External Benchmark (Task 2, 2026-07-19)`

- Control: `REV_AOP_T2_Control_Preregistration_v1_0.md`, `aop_T2_doubleKO_control.py`, `T2_control_results.json`, `REV_AOP_T2_Control_Results_v1_0.md`
- v1.1 benchmark: `aop_external_benchmark.py`, `external_benchmark_results.json`, `REV_AOP_External_Benchmark_Results_v1_1.md`, `REV_AOP_External_Benchmark_ChangeNote_v1_0_to_v1_1.md`, frozen `REV_AOP_External_Benchmark_Preregistration_v1_0.md`
- Inputs: `MODEL_e_coli_core.xml` (MD5 `2fd9c214…`), `EXT_KEY_price2018_fitness_Keio_BW25113.tsv` (MD5 `936b99da…`)
- Prime's v1.0 verification (top of `AOP`): `AOP_Prime_Verification_ExternalBenchmark_20260719.md`

## What to attack (re-run the code; don't take numbers on faith)

1. **Did the control screen the full pair space, or only re-test AOP's 13 pairs?** The control loads the 13 pairs from AOP's frozen JSON. "Recovers 13/13" only means "AOP's pairs are also plain-SL-detectable" — weaker than "a plain screen independently surfaces the same 13." A fair specificity control screens the whole space and compares sets. Check which was done; it changes how decisive the result is.

2. **Load-bearing premise:** for all 13 pairs, are *both* singles really ΔV≈0? The "Möbius collapses to the joint drop" argument holds only if the singles are symmetric near zero. Find any pair where one single carries meaningful ΔV — there the coalition term does real work.

3. **Both sides.** Too generous to the critique — is there any regime (medium, threshold, ranking task, or a *genome-scale* model vs the small core) where the coalition/viability layer adds value a plain screen misses? Or too harsh — did the control borrow anything from AOP that biases it?

4. **Confirm v1.1 was actually independently re-run,** not just delivered. T3-fail and T4-falsified depend on the de-circularized v1.1 labels. Reproduce them; check whether a prime verification of v1.1 actually exists on Drive.

5. **The big question:** is the overall read correct — across every fair test on systems AOP didn't rig, no distinctive empirical content shown? Steelman both "AOP has no method-level content, only reframing" and "these benchmarks are the wrong test for what AOP actually claims."

Deposit a single findings file in the Task 2 folder. Prime re-verifies before anything reaches the canon.
