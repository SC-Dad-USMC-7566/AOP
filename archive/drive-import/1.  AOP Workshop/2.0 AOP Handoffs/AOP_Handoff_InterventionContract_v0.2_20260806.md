# Handoff — AOP Intervention Contract v0.1 → v0.2 (post-Aster red-team)

**Date:** 2026-08-06 · **From:** Claude Cowork (session near context budget) · **To:** the continuing Claude seat
**One-line state:** Aster red-teamed the four-axis Intervention Contract v0.1 and it **failed its own single-method gate**. v0.2 is a known rewrite, but it is **blocked on three Ben decisions**, one of which touches the just-frozen canon. Do not start v0.2 until those are ruled.

---

## 0. Startup read-in
- **Charter v1.2**, **Canon v1.27** (frozen this session, *pending Ben's manual masthead stamp* — see §5). Working method: chat seat thinks/decides/grades; execution seat builds; **nobody grades their own homework**; verify against primary source; grade every claim.
- This handoff is self-contained enough to continue without replaying the thread, but the live artifacts are on Drive (§6).

## 1. Where the session landed (four work-order decisions)
- **Decision 1 — §11.1 canon governance: CLOSED.** v1.26→v1.27 fold independently verified (both load-bearing math corrections sound); C-1/C-3 residual "floor→positivity" sweep applied at L17/L236/L393; frozen at v1.27. **Outstanding: Ben's manual stamp + placement** (stamp-ready master `md5 43257601` delivered) and Drive hygiene (trash the corrupt `_candidate` and the pre-sweep `v1.27.md`).
- **Decision 2 — §11.2 methods-paper scope: methods paper ACCEPTED by Ben.** Spine gated on the Intervention Contract surviving a falsification pass. **Aster's pass is back — see §2.**
- **Decision 3 — §11.3 pre-registration deviations (P1/P3 recast, P2 unassessed): OPEN, untouched.**
- **Decision 4 — §10 open-work register ("say what's missing"): OPEN, untouched.**
- **Phase 0 prior-art sweep: NOT run.** Blocks any novelty claim (Causal Leverage Density — Bartlett 2024 / Sowinski 2025; causal individuality — Bourrat 2023/24; interventional info-decomposition).

## 2. Aster's verdict on the contract
- **v0.1 does NOT survive as a single four-axis method.** Disposition = the contract's own named fallback: **a typed family of causal contrasts with common reporting rules — not "one estimand," not yet one co-measured four-axis method.**
- **Not a rejection** of AOP or the methods paper. v0.1 succeeded as a diagnostic.
- **Affirmed (do not relitigate):** R1/R2 retractions correct; declaration-vs-null separation correct; Integration promotion gate appropriate; the K&W verification correct on R1/R2. Aster added one correction to the K&W note: K&W's sign convention is *actual − intervened*; our contract uses *intervened − actual* — make the reversal explicit on import (not an error, just a convention to state).

## 3. THE BLOCKERS — decisions Ben must rule before v0.2 is built

**3.1 Memory repair — Option A vs B. Canon-touching. This is the important one.**
Aster proved the Memory target/null mismatch: the declared quantity is excess entropy E = I(X_{≤0};X_{≥1}), but "Markovianize to order 1" does **not** null E — a stationary order-1 chain can have large E (Golden Mean process, E ≈ 0.2516 bits; a 0.9-repeat binary chain, E ≈ 0.531 bits). Two coherent repairs:
- **Option A — keep E (canon-consistent).** Null = i.i.d./order-0 reference at the same one-time marginal: P₀(x_{t+1}|x_t)=π(x_{t+1}). Target-aligned (drives E→0). **Cost:** low selectivity — it also changes kinetics, residence times, and σ, so the reading isn't cleanly "Memory only." But low selectivity is an *honest, reportable* result, and it echoes the canon's own forced Drive→Memory edge (nulling to i.i.d. must move σ). **Preserves the just-frozen canon Memory definition.**
- **Option B — keep the Markovization null, change the target** to higher-order memory M_{k,L} = I(X_{≤t−k}; X_{t+1:t+L} | X_{t−k+1:t}). Target-aligned for an order-k projection. **Cost:** this **redefines the Memory axis away from E**, i.e. it **changes the canon we just froze** and would have to propagate to canon governance — partially unwinding v1.27's stabilization.
- **Cowork's recommendation:** **Option A.** It keeps Memory = E (canon), and its weakness (low selectivity) is a finding, not a defect, and is consistent with the frozen σ>0 ⇒ E>0 edge. Option B buys clean selectivity at the price of reopening canon on the very axis just settled. Ben rules.
- **Either way:** "retained Markov order" has no continuous severity λ (order is discrete). v0.2 must supply a continuous null path — a mixture pₗ=(1−λ)p+λp₀, a coarse-graining path, or an information-constraint family.

**3.2 Confirm the typed-family reframe** as the paper's spine (replaces "one estimand" with "four typed causal contrasts sharing a declared viability outcome, horizon convention, sensitivity audit, and reporting schema"). Cowork recommends yes — it is Aster's disposition and the contract's own fallback.

**3.3 Boundary identity.** Aster: instantaneous I(inside;outside) measures *stored dependence across a declared cut*, not a material boundary (an impermeable boundary can show low MI; a leaky one high MI via common cause). Pick one: (a) rename to **External Stored Dependence** and own the narrower meaning; (b) add a separate boundary-maintenance/causal-control quantity; (c) declare "Boundary" = the *role of the cut*, not the interface, and prohibit membrane readings. Cowork leans (c) for v0.2 with (a) as the honest fallback if a referee pushes.

## 4. v0.2 build spec (Aster P1–P7 + specific hits) — for after the rulings
1. **Reframe unity (P1):** typed family, not one estimand. Each axis is θ_A(λ;D) = V_τ(P^{A,λ}_{μ0}) − V_τ(P⁰_{μ0}) — four causal contrasts, common outcome/horizon/audit/reporting.
2. **Complete the common declaration (P2):** add **initial ensemble μ0** (+ conditioning rule e.g. μ0(·|viable at t=0), support, conservation constraints, whether the same μ0 is used under every null); **V domain + orientation** (larger = more viable, always); **V type** (endpoint distribution vs full path law vs survival/first-passage); **evaluation schedule** (at the instant, over [0,τ], at τ); **sign convention vs K&W**; **estimator + sample + uncertainty**.
3. **Memory (P3):** implement the ruling from §3.1 with a continuous severity path.
4. **Integration (P4): verdict = NOT PROMOTED.** Keep outside the co-measured core until it commits to one target (total-correlation / min-cut dependence / predictive irreducibility / causal-coupling ablation), one level, one partition rule, and passes identity + selectivity. Note Boundary and state-level Integration are the **same product-scramble operator over different cuts** (external vs internal) — the distinction is supplied by the declared partition, not discovered by the intervention, so it is not two operational DOF by itself.
5. **Replace the 4×4 selectivity matrix with typed response panels (P5).** The columns currently live on incompatible objects (Boundary/Integration instantaneous-distributional; E stationary semi-infinite-history; σ stationary path-rate; V finite-horizon) with no common ensemble or measurement time → entries undefined or meaning-shifting. Use **Panel A (initial-state interventions: Boundary, state-Integration; fixed generator; finite-time trajectories P_k(t), V(t) from the intervened initial ensemble)** and **Panel B (mechanism interventions: Memory, Drive; fixed initial ensemble; finite-horizon path quantities)**. Define finite-time versions of all readings before reporting cross-panel spillover. **Do not infer ontology from rank** — rank on one model measures local intervention→reading dimensionality, confounded by absence-in-specimen, saturation, severity calibration, horizon, estimator power. Report a *persistence-response signature* with uncertainty, not an axis count.
6. **Benchmark suite, not one model (P6):** (i) i.i.d.; (ii) reversible correlated Markov chain (E>0, σ=0); (iii) driven 3-state cycle at fixed uniform π (σ>0 but endpoint-marginal V blind — the degeneracy in §4-tech); (iv) higher-order / hidden Markov; (v) initially correlated but dynamically uncoupled parts; (vi) same decorrelation operator over external vs internal cut (Boundary–Integration collapse test); (vii) viability-irrelevant correlation; (viii) anti-viable information (signed-effect check).
7. **Reconcile "no outcome fatal" with §9 kill conditions (P7):** a kill condition is fatal to the *four-axis co-measured method*, not to AOP; it authorizes a reduced/typed paper.

**Two more technical carry-forwards so they aren't re-derived:**
- **Stationary-marginal degeneracy:** if μ0 = π (stationary) and V is a one-time marginal functional (e.g. negative entropy), any π-preserving null gives ΔV = 0 **by construction**, even with sharply different σ (three-state driven cycle, uniform π, symmetrized). ⇒ Drive/Memory need a **path-level or conditioned V and a nontrivial μ0**; "same stationary distribution" does not secure comparability.
- **Admissibility is five distinct standards, not one word:** probabilistic validity / constraint compatibility / dynamical reachability / physical implementability / identifiability-from-data. Declare which level each axis's null must meet.
- **Controls to tighten:** "block-decomposable ⇒ ΔV=0" holds only if the null leaves the *baseline distribution* unchanged (dynamically uncoupled blocks can stay initially correlated); the proper identity is "if the null leaves the baseline distribution unchanged, the effect is zero." Rocks/hurricanes are K&W conceptual examples, not completed AOP negative-control experiments.

## 5. Housekeeping still outstanding
- **Canon v1.27 stamp:** Ben's manual masthead edit (`version 1.26 · compiled 25 July 2026` → `version 1.27 · compiled 06 August 2026`) + changelog entry (proposed wording in `AOP_ChangeNote_v1.27_C1C3_residual_sweep`) + place as frozen master. Not yet done.
- **Drive hygiene:** trash corrupt `AOP_CANON_MASTER_v1.27_candidate.md` (`1UaB…`) and pre-sweep `AOP_CANON_MASTER_v1.27.md` (`1mnX…` + dup `1jnq…`).
- **Aster's raw red-team review is NOT yet on Drive** — Ben holds it in the chat; archive it as a `REV_` record (this handoff digests it but the raw belongs on Drive).
- **Decisions 3 & 4** (§11.3 pre-reg, §10 register) untouched. **Phase 0** not run.

## 6. Drive pointers (folder `10S59I_...` = task/working folder)
- Work order v3: `1iEoqawHzHUav4hzQKPiXGsrdJ1YveK16`
- Intervention Contract v0.1: `1QWLNzwTcZKlhvJjubtvLb1jQW76sW87r`
- K&W verification note: `1o7uABqP4iYIQRcnEcOFw09mLed3en07L`
- v1.27 change note: `1nf60cSALZYlTT2sCX7usqSuZc6ketheU`
- Canon v1.27 clean fold (pre-sweep, pre-stamp): `1mnX6Y8frvAkl8rpH3aP2OR27jriGVel-`; stamp-ready swept master delivered in chat (`md5 43257601`, 255,714 B).
- Canon v1.26 (base, hash-verified): `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn`

## 7. Immediate next action for the continuing session
Get Ben's three rulings (§3: Memory A/B, typed-family confirm, Boundary identity). **Then** build Intervention Contract **v0.2** to the §4 spec, **then** re-run the falsification gate on v0.2 against the §4.6 benchmark suite before anything enters Phase 2. Only after v0.2 survives does §11.2 close as "build the (typed) paper."

*Handoff produced by Claude Cowork, 2026-08-06. Digests Aster's red-team (`REV_AOP_InterventionContract_v0.1`, 2026-08-06) faithfully; the raw review should be archived to Drive. Authorizes no canon edits.*
