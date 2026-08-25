# Work Order — AOP structural probes E1–E3 (pre-red-team hardening)

**Issued by the chat seat (prime), 23 July 2026, for the execution seat (Cowork).**
CW builds and reports; prime verifies by re-running; then the document goes to Aster. **Nobody grades their
own homework — deliver for verification, do not self-bless.**

These three probes attack the framework's *own* soft spots in its own idiom (closed-form Gaussian /
OU computation). They are not cosmetic. **E2 and E3 can come out badly for the framework.** If they do,
that is the point — report it honestly, do not tune to a favorable answer. Each probe's pass/fail
criterion and every threshold is **pre-registered below and frozen**; you may not move a threshold after
seeing a result. If a threshold looks ill-posed *when you build the model* (before running), stop and
flag it to prime rather than pick a convenient value.

## Startup (confirm before working)
```
Startup check — [date]
[ ] AOP Charter — v1.2
[ ] AOP Canon (the paper) — v1.24 (SHA-256 3e64ff0ca93eee3165d53520651dfbbac063489df1ccfa87e3c8242f0dd421cf, 218,602 bytes)
[ ] AOP → Ladder bridge memo — n/a
Drive connector: [on/off]
```
Canon folder `1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J`; Canon Development `1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`.

## Global rules (all three probes)
1. **Closed-form / analytic where possible** (charter: prefer derived to estimated). Gaussian MI, conditional
   MI, and TC have closed forms; use them, not Monte-Carlo estimation, wherever the quantity admits it.
2. **Seed every RNG** and print the seed; results must reproduce on re-run.
3. **Pre-registered pass/fail is frozen.** Report the computed result against the stated criterion whichever
   way it falls. No post-hoc threshold changes. If a probe fails, say so plainly and draft the honest canon
   caveat, not a spin.
4. **Deliverables per probe:** (a) a deposit-ready script `phaseE{n}_*.py` (self-contained, seeded); (b) a
   short results note stating the pre-registered criterion, the computed result, and the verdict; (c) *only if
   the result warrants a canon change*, a **change set** (verbatim OLD→NEW against v1.24) — never edit the
   master (Ben places it manually). Scripts + notes are small: write to Canon Development via `base64Content`.
5. **Grade every claim** (SETTLED / SYNTHESIS / FRONTIER). "Verified against primary" only if actually done.
6. **Do not overclaim.** State what was shown and what was not. A null or adverse result is a valid, valuable
   deliverable.

---

## PROBE E1 — Does the four-fold carving survive the Boundary–Integration collapse? [READY TO BUILD]

**Why.** §13 names the carving's own falsifier: it fails if two axes "collapse into one that always
co-moves." Boundary and Integration are the at-risk pair (the nesting identity makes B5 a component of I).
The canon currently says B and I are "dissociable only by construction." Prime's exploratory run (re-implement
independently from this spec; do **not** port prime's code) indicates they dissociate *generically*. Confirm it,
deposit it, and draft the precision fix.

**Model.** N=7 Gaussian nodes: inside `{0,1,2}`, interface `F={3}`, outside `{4,5,6}`. Build a random stable
precision matrix per system with: random intra-inside and intra-outside couplings; random inside–F and
F–outside (through-interface) couplings; and inside–outside **direct (bypass)** couplings whose presence is
gated by a per-system `seal_bias ∈ [0,1]` drawn uniformly (so the ensemble spans sealed→leaky). Enforce
positive-definiteness. Sample ≥4000 systems.

**Quantities (closed-form Gaussian):**
- **Integration** TC = Σᵢ H(xᵢ) − H(X) (per-node total correlation — the canon's operational default).
- **B5** = I(inside ; outside).
- **B2** = I(inside ; outside | F)  (screening residual).
- **B1** = interior/exterior state contrast. **Declared operationalization:** symmetrized KL between the
  inside-block and outside-block marginal covariances. Also compute **one alternative** B1′ (e.g., mean
  per-node marginal-variance contrast) and confirm the verdict is robust to the choice.

**Pre-registered claims (frozen):**
- **C1 (corners non-empty):** both `{B2 in bottom 15% ∧ TC in top 15%}` (sealed-yet-integrated) and
  `{B2 in top 15% ∧ TC in bottom 15%}` (leaky-yet-unintegrated) are non-empty. **Carving survives the
  collapse test iff both corners are populated.**
- **C2 (spread at fixed integration):** within the top-TC quartile, B1 and B2 each retain a spread
  (max−min) of at least their own median. (Boundary's own content still moves when Integration is held high.)
- **C3 (honest correlation reporting):** report Spearman(B5,TC), Spearman(B2,TC), Spearman(B1,TC) as-is.
  **Do not claim** B2 is "freer" than B5 by correlation unless the numbers support it; state explicitly that
  B5's nesting is *algebraic* (an additive term of TC), best shown by the sealed-vs-bypass construction
  (phaseC1), not by rank correlation.

**Canon insert to draft (if C1 ∧ C2 hold):** a change set that (i) upgrades "dissociable only by construction"
→ "dissociates generically across random Gaussian systems (both dissociation corners populated; deposited
`phaseE1`)"; and (ii) states plainly that Boundary's **axis-defining content is B1 (state contrast) and B2
(screening residual)**, while **B4 = σ_hk and B5 = I(in;out) are the D→B and I→B edges read at the interface**
(as the canon already defines them) — so the carving's B–I independence rests on B1+B2, which are shown to
carry independent variation. Grade **SYNTHESIS / analytic-model-result.** If C1 fails, draft instead an honest
caveat that the pair may collapse and flag it to prime as a substantive problem.

**Acceptance (prime will run):** re-implement/re-run; confirm C1–C3 reproduce under the printed seed; confirm
the drafted insert maps to a real location in v1.24, changes no other claim, and is graded honestly.

---

## PROBE E2 — Does the semantic mask have any informative ∩ well-defined region above triviality? [PRE-REGISTERED]

**Why.** The mask is the framework's characteristic measurable, but §13/§6 say it blurs on strongly
integrated systems. The open question (parked in the canon's history as "mask salvage"): is the mask sharp
*only* where integration is so low the weights are degenerate — i.e., **confined to trivial cases** — or is
there a genuinely integrated regime where it is both well-defined and informative? This is the load-bearing
methodological question. It may fail; report it either way.

**Model.** Coupled Gaussian Σ=(I+gL)⁻¹ over three topologies L ∈ {chain, mean-field, sparse-random}, sweeping
global coupling `g` from near-zero to strong. Declare a present-tense viability functional V (closeness of a
designated regulated node to a target), as in Figure MW/LT. Designate one **load-bearing** edge and one
**inert spectator** edge by construction. Per edge e, compute the mask weight `w_e` = fractional drop in V
when e is scrambled, **and** its resolvability interval half-width `h_e` from the resolvability signature the
canon already deposits (inferential VIF term + interventional do-edge drag; report 1/√λ_min and 1/√λ_max).

**Pre-registered definitions and thresholds (frozen):**
- **Well-defined at e** ⇔ `h_e ≤ ρ·|w_e|` with **ρ = 0.5** (weight resolvable to within a factor of two).
- **Informative** ⇔ `(w_LB − w_inert) ≥ K·max(h_LB, h_inert)` with **K = 3** (the load-bearing/inert gap is
  resolvable, not swamped by the blur).
- **Triviality floor** ⇔ TC(system) ≤ τ_floor, where **τ_floor = TC of the same topology at g such that every
  off-diagonal coupling equals 5% of the diagonal** (an effectively separable system). Systems with TC ≤
  τ_floor are "trivial"; systems with TC > τ_floor are "non-trivial / genuinely integrated."

**Pre-registered question (frozen):** over the (topology, g) sweep, does there exist a system that is
simultaneously **well-defined ∧ informative ∧ non-trivial (TC > τ_floor)**?
- **PASS (mask salvageable):** yes for at least one topology at some g with TC > τ_floor. Report the region
  (which topologies, which g-band, the TC and Φ_MIP there). Draft a canon note: the mask's informative
  well-defined region is non-empty above triviality — deposited `phaseE2`. Grade **SYNTHESIS, computed.**
- **FAIL (confined to trivial cases):** the intersection is empty for all TC > τ_floor (holds only as g→0).
  **Do not soften this.** Draft the honest canon caveat that the mask is, on present evidence, confined to
  near-separable systems, and flag it to prime as a substantive limitation affecting every mask-dependent
  claim (including the §11a life operationalization). Grade the limitation **FRONTIER / adverse.**

**Acceptance (prime):** re-run; confirm the region (or its absence) reproduces under the frozen thresholds;
confirm CW did not move ρ, K, or τ_floor; confirm the verdict and grade match the computed result.

---

## PROBE E3 — Is the "alive" criterion positively detectable, or negative-only? [PRE-REGISTERED]

**Why.** §11a's *alive* = "load-bearing ∧ decoupled internal model of the system's own viable set." Every
external case (Levin/Bassler/Walker) failed the bar. That is either a sharp criterion or one defined so
nothing can satisfy it. Establish whether a system can be **positively** flagged alive from third-person
access, and — the subtle risk — whether doing so needs an **extra modeler declaration** beyond V.

**Model.** An OU family parameterized by `d ∈ [0,1]` interpolating **star-type** (d=0: the set-point is baked
into the intrinsic drift of the regulated variable x; no separate node) → **cell-type** (d=1: the set-point is
held in a distinct reference node r that drives x toward r's readout, r separately interventable). Declare V =
closeness of x to essential target μ*, as in Figure LT.

**Detection procedure (third-person, pre-registered):**
1. **Load-bearing** at the candidate reference edge ⇔ scrambling it drops V by ≥ **w_min = 0.30**.
2. **Decoupled** ⇔ ∃ node r such that (a) a clamp/intervention on r shifts the value x settles to (r acts as a
   set-point), **and** (b) r is structurally separable from the fast regulated path (r is not a deterministic
   function of x on the fast timescale; r can be clamped without directly clamping x). Read (b) from the
   generator/graph, not from labels.

**Pre-registered questions (frozen):**
- **Q1 (correctness):** does the procedure flag d=1 (cell) alive and reject d=0 (star)?
- **Q2 (architectural, not magnitude):** is the flip along `d` driven by the *existence of the separate
  reference node*, not by a slow/fast timescale-separation magnitude? (Vary the slow/fast ratio independently;
  confirm the verdict does not flip with it — matching the Figure LT-T claim.)
- **Q3 (the decisive one):** can step 2 be executed from the coupling graph + V alone, or does it require an
  **additional declaration** — the modeler nominating "node r stores the viable set"? Test by withholding any
  label of which node is the "model" and asking whether (2a)+(2b) alone single out r.

**Pre-registered verdict (frozen):**
- **Two-sided detector:** if Q1 holds, Q2 confirms architecture-not-magnitude, and Q3 shows (2a)+(2b) single
  out r **without** a separate "this is the model" declaration (V suffices) → *alive* is a genuine positive
  detector up to the standing V-declaration. Draft a canon note upgrading the life criterion from
  "demonstrated for self-consistency" toward "positively detectable (up to V)"; grade **FRONTIER, computed.**
- **Negative-only / second-declaration:** if Q3 shows the procedure needs the modeler to nominate the model
  node (a second observer-declaration beyond V) → *alive* detects "alive relative to a nominated candidate
  model," not intrinsically. **State this plainly** as a canon caveat (the life criterion carries a second
  declaration); grade **FRONTIER / scoped.** This is a valuable finding, not a failure to hide.

**Acceptance (prime):** re-run the interpolation; confirm Q1–Q3 reproduce; confirm the verdict follows the
frozen criteria and the grade is honest. Flag to prime on contact if the operationalization of (2b) looks
ill-posed before running.

---

## Deliverables summary
| Probe | Script | Note | Canon change set (if warranted) |
|---|---|---|---|
| E1 | `phaseE1_BI_dissociation.py` | criterion + result + verdict | upgrade "by construction"→"generically"; name B1+B2 as axis content |
| E2 | `phaseE2_mask_domain.py` | criterion + region (or absence) | salvageable-region note, or adverse confinement caveat |
| E3 | `phaseE3_life_detection.py` | criterion + Q1–Q3 verdict | positive-detector upgrade, or second-declaration caveat |

Scripts + notes → Canon Development (`base64Content`). Canon change sets → delivered for prime; master is
placed by Ben. **All results delivered for prime to verify by re-running, then to Aster.**
