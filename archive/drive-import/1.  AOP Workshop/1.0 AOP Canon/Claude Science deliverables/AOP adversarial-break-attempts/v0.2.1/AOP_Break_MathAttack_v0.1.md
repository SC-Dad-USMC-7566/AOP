# Break attempt — AOP Intervention Contract v0.2.1: the analytic attack

**Date:** 2026-08-07
**Seat:** Claude Science, attack seat. **Did not build v0.2 or v0.2.1.**
**Target:** `AOP_InterventionContract_FourAxis_v0.2.1_20260807` (Drive id `11C1Tmnt00ixoDp4KsPcJ2Q_pF_82g59h`)
**Reference canon:** `AOP_CANON_MASTER_v1.27` (id `1PZdsto8bRLB1SgoAYnGfOvAjCuygFklD`)
**Review the target claims to implement:** `REV_AOP_InterventionContract_v0.2_GateReadiness_20260807`
**Status:** Non-canon attack report. Authorizes no canon edits. Every number below is closed-form or
exactly computed on the contract's own declared models; none is estimated from samples.

---

## 0. What was attacked, and what survived

The contract asks to be broken as a **method**: can an independent seat run the §9 gate and get a
determinate answer? I did not attack AOP's canon claims. I attacked the contract's executability, on
its own six computable models, with its own declared quantities.

**Four findings are fatal to the gate as written.** Two are mine, from the analytic attack; two come
from the parallel canon-fidelity audit (`AOP_Break_FidelityAudit_v0.1.md`) and I have re-verified both
against the canon text and, for F0a, against the contract's own model 4 by computation.

- **F0a (fatal). The canon's own scope warning about this exact ring is missing, and it is a
  live trap.** Canon Figure DM's caption warns that "the increment representation of the same ring
  preserves σ exactly while sending E to zero." Model 4 *is* that ring, its cut is declared only as
  "temporal + state," and the contract never fixes the state representation nor carries the warning.
  Computed below: in the increment representation σ is preserved to 1e−12 and **E is exactly 0**. A
  seat that declares increments — a legitimate reading of "state" — measures σ>0 with E=0 and reports
  a **refutation of the theorem the gate told it to expect**.
- **F0b (fatal). The Boundary contrast is the one proxy the canon disqualified.** Canon Table 1 leads
  the Boundary panel with B1/B2/B4 and retains B5 = I(in;out) "only as a descriptive quantity, and is
  explicitly the cross-cut slice of Integration (§4), not boundary strength." CBSD **is** B5. The
  canon supplies the instrument the contract says does not exist.
- **F1 (fatal). The Drive contrast has no determinate sign — and the declaration block cannot fix
  it.** On model 4, the contract's own designated Drive control, ΔV_Drive changes sign under a choice
  the declaration block does not require anyone to declare. Two seats can run model 4 exactly to spec
  and report opposite-signed Drive results.
- **F2 (fatal to the stated rationale). Model 3 does not have the property the contract assigns it.**
  The Even Process's projection residual ρ_k does **not** stay strictly positive as k grows — it
  decays geometrically, as k·2^(−k/2). The contract's stated reason for choosing model 3 ("the ladder
  never saturates, which is exactly the diagnostic value") is false as stated.

**Three further findings are major** (F3–F5): the Boundary and Integration contrasts cannot run on
four of the six computable models; the k≥1 "diagnostic rungs" do not dissociate Memory from Drive on
any σ=0 model, which is five of the six; and the §9 Model-4 rationale overstates a true claim in a
way that is refutable by a two-channel counterexample.

**What survived.** The typed-family architecture (§0) survived: I found no inconsistency in splitting
Type A from Type B, and the decision to refuse a single four-axis estimand is the right one and is
load-bearing for everything below. §3.1's CBSD disclaimer survived and is doing real work. The
Golden Mean number is **exactly right** (see §2). §7.3's separation of identifiability from
admissibility survived and, in fact, F1 is best understood as vindicating it: the contract built the
right category and then under-used it.

---

## 0a. F0a (fatal) — the increment-representation trap on model 4, computed

The canon states the warning and names the model. Canon §4 scope condition 1 requires σ and E on "the
same complete description"; canon Figure DM's caption makes it concrete for this ring:

> "the increment representation of the same ring preserves σ exactly while sending E to zero — see §4,
> scope condition 1."

Model 4's declaration gives its cut as "temporal + state" and never fixes whether "state" means ring
**position** or ring **increment**. Both are complete descriptions of a trajectory; the increment
reading is the natural one for a seat thinking of a current. On the contract's own ring (a+b = 0.6):

| a | b | position rep: σ | position rep: E | increment rep: σ | increment rep: E |
|---|---|---|---|---|---|
| 0.120 | 0.480 | 0.720000 | 0.180855 | 0.720000 | **0** |
| 0.480 | 0.120 | 0.720000 | 0.180855 | 0.720000 | **0** |
| 0.001 | 0.599 | 5.517394 | 0.603342 | 5.517394 | **0** |
| 0.599 | 0.001 | 5.517394 | 0.603342 | 5.517394 | **0** |

σ agrees to <1e−12 across representations; E is **exactly** zero in the increment representation,
because the increments of a cyclically symmetric ring are i.i.d. (the step law does not depend on the
position). So a seat running model 4 with increments as its declared state observes σ = 5.517 with
E = 0 — a clean apparent counterexample to σ>0 ⇒ E>0 — on the model the contract chose *because* it
is the canon's computed witness **for** that theorem, and in the panel (§6) where the contract told
the seat in advance to expect the forced off-diagonal "so it is not 'discovered' as a bug."

This is the worst failure mode available to the gate: not a null result, but a **false refutation of a
canon theorem, pre-authorized by the contract's own framing.** The canon anticipated it and said so in
the caption of the figure the contract cites. The repair is one mandatory sentence — model 4's state
is the ring **position**, R is the position-space reversal, and the increment representation is
outside scope condition 1 — plus restoring the canon's warning to §5.

Note this also sharpens the canon's own §4 remark that the five conditions are *not independent*: the
position→increment map is simultaneously a change of description (condition 1) and a change to odd
variables (condition 3). The contract renders the five conditions as a five-box checklist and drops
that entanglement, telling the seat that clearing the boxes clears the scope. On this model it does
not.

## 0b. F0b (fatal) — CBSD is the Boundary proxy the canon demoted

§3.1 says the "Canon Boundary axis untouched" and offers CBSD = I(in;out) as the Boundary quantity,
with a prominent disclaimer that it "does **not** measure membrane integrity, permeability,
insulation, or boundary maintenance," and files a boundary-*maintenance* quantity as "**future
work**."

The canon does not agree. Canon Table 1's Boundary row:

> "Boundary panel — a family of proxies, not one scalar. The lead proxies are the Boundary-specific
> ones: a declared interior/exterior state contrast (B1), the screening residual I(inside;outside |
> interface) (B2), and the maintenance burden required to hold the contrast against leak (B4).
> Cross-boundary dependence I(inside;outside) (B5) is retained only as a descriptive quantity, and is
> explicitly the cross-cut slice of Integration (§4), not boundary strength."

CBSD is B5. So the contract takes a four-proxy panel, keeps the one proxy the canon explicitly says is
*not* boundary strength, and describes the axis as untouched. And the canon has already computed the
dissociation (canon §8, static Gaussian model with declared interface F):

| configuration | B2 = I(in;out \| F) | B5 = I(in;out) |
|---|---|---|
| inside/outside interact only *through* the interface | **0.000** | 0.896 nats |
| a coupling *bypasses* the interface | **0.292** | 1.685 nats |

with the canon's conclusion: "B2, not the dependence B5, distinguishes a cut *sealed by an interface*
from one merely *coupled across*." Three consequences:

1. **The disclaimer is backwards relative to the charter's first rule.** §3.1 invents a caveat
   ("maintenance is future work") where the canon supplies an *instrument* — B2 and B4 are defined,
   B2 is computed, and both carry citations. Don't create when you can cite: the fix is not a
   disclaimer, it is to use B2/B4.
2. **B4 is what the Drive-axis maintenance question needs**, and dropping it is why §7.4's controls
   (rock, hurricane) stay conceptual — a maintenance burden is exactly what separates a rock's
   boundary from a cell's.
3. **K5 is unevaluable for a second, independent reason.** By canon Table 1, B5 already *is* the
   cross-cut slice of Integration. So the contract's Boundary and Integration contrasts are one
   quantity on two cuts *by canon definition* — which is what K5 nominally tests. K5 cannot discover
   this; it is true before the gate runs. (§3.4 defines the Integration reading *as* the Type-A
   operation on an internal cut, so K5's antecedent holds analytically. §8 concedes it is "the
   expected outcome" without concluding that K5 should be withdrawn or re-specified against a named
   quantity — canon Table 1's total correlation, or §4's minimum-cut Φ_MIP, neither of which appears
   anywhere in the contract.)

Note the interaction with F3 below: adopting B2 requires a declared **interface** F, and the
contract's §2 declaration block has no interface field — canon's declaration tuple D does. Fixing F0b
and F3 is one repair, not two.

---

## 1. F1 (fatal) — the Drive contrast is sign-indeterminate inside its own envelope

### 1.1 The setup, verbatim from the contract

§9 model 4 is a "Driven three-state Markov ring (canon Fig DM)", Drive control, V = "small-noise MFPT
(first-passage) — envelope-flagged", μ₀ = "non-π start (conditioned)". §3.3's null is the
"detailed-balance projection — symmetrise the generator at fixed stationary distribution relative to
R." §0 fixes the sign convention as intervened − actual.

I take the ring with clockwise rate a, counter-clockwise rate b, a+b = c = 0.6 held fixed. Cyclic
symmetry makes the stationary law **uniform for every (a,b)** — so the detailed-balance projection at
fixed π is exactly a=b=c/2, and the null is unambiguous. Closed form for the mean first-passage time
from state 0 to state 1:

> **MFPT(0→1) = (2c − a) / (c² − ac + a²)**, and at the null a=c/2 it equals **2/c**.

so the Drive contrast's outcome has the closed form

> **ΔV_Drive(a) = 2/c − MFPT(0→1) = a(2a − c) / [ c (a² − ac + c²) ]**

whose numerator factors as **a·(2a − c)**. The only root in (0, c) is **a = c/2**, the null itself.
Therefore **sign(ΔV_Drive) = sign(a − c/2)**: strictly negative for a < c/2, strictly positive for
a > c/2.

### 1.2 The break: σ is even in the affinity, ΔV is odd

The cycle affinity is A = 3·ln(a/b). The Drive **reading** σ is a divergence and is **even** in A —
it cannot distinguish clockwise from counter-clockwise. The **viability response** ΔV is **odd**. So
mirror pairs (a,b) and (b,a) are systems with *identical* Drive readings, *identical* Memory
readings, and *identical* stationary law, whose Drive contrasts have **opposite signs**:

| a | b | A | σ (bits/step) | E (bits) | ΔV_Drive (target = state 1) |
|---|---|---|---|---|---|
| 0.120 | 0.480 | −4.159 | 0.720000 | 0.180855 | **−0.238095** |
| 0.480 | 0.120 | +4.159 | 0.720000 | 0.180855 | **+0.952381** |
| 0.001 | 0.599 | −19.186 | 5.517394 | 0.603342 | **−0.002773** |
| 0.599 | 0.001 | +19.186 | 5.517394 | 0.603342 | **+1.661106** |

Not only the sign: at |A| = 19.186 the two members of the pair differ in |ΔV| by a factor of
**599**, at identical σ and identical E. So **neither the sign nor the magnitude of the Drive
contrast is a function of the Drive reading.**

### 1.3 Why the declaration block does not save it

The obvious rescue is "declare the direction." It fails, because the sign also flips under the choice
of *which first-passage event V measures*. The ring has two distinct targets from state 0, and by
reflection symmetry they are equivalent at the null (both MFPT = 2/c), so nothing in the null
declaration distinguishes them:

| a | b | ΔV, target = state 1 | ΔV, target = state 2 |
|---|---|---|---|
| 0.001 | 0.599 | −0.002773 | **+1.661106** |
| 0.120 | 0.480 | −0.238095 | **+0.952381** |
| 0.480 | 0.120 | +0.952381 | **−0.238095** |

The sign is opposite in **every** row. And §2's declaration block — fields (1)–(11), which the
contract calls mandatory with "no silent defaults" and "a blank field = inadmissible contrast" —
requires μ₀, V, V type, τ, schedule, null, preserved quantities, admissibility, identifiability, sign
convention, estimator. It requires declaring that V is a first-passage functional. **It nowhere
requires declaring which absorbing event.** Two independent seats, both filling every mandatory field
correctly, both reporting "V = small-noise MFPT, first-passage, τ to first passage," get
opposite-signed Drive results on the contract's own Drive control.

This is precisely Aster's item 6 failure mode — "two independent seats may run different tests while
believing they ran the same gate" — surviving in v0.2.1 on the very model that was rewritten to
satisfy item 4.

### 1.4 An unbounded-σ / vanishing-ΔV corner

Worse for interpretation: taking a → 0 at fixed c drives the affinity and σ to infinity while ΔV → 0:

| a | \|A\| | σ (bits/step) | ΔV_Drive |
|---|---|---|---|
| 1e−2 | 12.23 | 3.4119 | −2.73e−02 |
| 1e−4 | 26.10 | 7.5278 | −2.78e−04 |
| 1e−6 | 39.91 | 11.5167 | −2.78e−06 |
| 1e−8 | 53.73 | 15.5031 | −2.78e−08 |

σ is unbounded; ΔV vanishes; and ΔV/σ → 0. So on the contract's Drive control there is a regime with
maximal Drive reading and **null viability response**, which §0 instructs the runner to report as "no
detected relevance under this declaration." That reading is defensible but it is not what a Drive
*control* is for: the model cannot certify that the Drive contrast detects Drive.

### 1.5 Disposition

This is **not** a kill of AOP, and it is not even a kill of the Drive axis. It is a kill of the
**claim that §9 as written is executable to a determinate result.** The right disposition is the one
the contract already has machinery for: §7.3 identifiability, declared per contrast. The repair is a
new mandatory declaration field — **the full specification of the V event, including the target set
and the orientation of the reference dynamics R relative to it** — plus an explicit statement that
sign(ΔV_Drive) is a property of (V, target, R-orientation) and not of σ. The §3.3 "envelope flag"
already gestures at this ("other V can flip the sign"); the finding here is stronger and more
specific: **the same V flips sign under a sub-choice the contract does not require declaring.**

---

## 2. F2 (fatal to the stated rationale) — the Even Process ladder does saturate

### 2.1 What the contract claims

§3.2.2: "for infinite-Markov-order processes (HMM/sofic, e.g. the Even Process, §9 model 3), ρ_k
stays strictly positive — **the ladder never saturates, which is exactly the diagnostic value**."
§9's model-3 rationale: the Even Process "has **infinite Markov order**, so ρ_k > 0 for all finite
k: it is the model that tests whether the ladder saturates."

### 2.2 What is true

The antecedent is right and the consequent does not follow the way the contract needs. ρ_k > 0 for
every finite k is true — but "strictly positive for all k" and "never saturates" are different
claims, and only the first is a theorem. Computed exactly (labelled transfer matrices, no sampling,
Even Process at p = 1/2):

| k | ρ_k | k | ρ_k |
|---|---|---|---|
| 0 | 0.917810 | 15 | 2.90e−02 |
| 1 | 0.873699 | 20 | 5.33e−03 |
| 5 | 0.425579 | 24 | 1.93e−03 |
| 10 | 0.106845 | 28 | ≤ 6.84e−04 |

and the decay is exactly characterized. The ladder increments E(M_{k+1}) − E(M_k) satisfy, to 1.8e−10
over k = 6…27, the **exact rational recurrence**

> **[E(M_{k+1}) − E(M_k)] / [E(M_{k−1}) − E(M_{k−2})] = (k+1)/(2k−2)  →  1/2**

so the per-rung factor tends to **1/√2** and **ρ_k ∝ k·2^(−k/2) → 0**. The increments are positive
and summable; E(M_k) is monotone increasing and bounded above by Cμ = H(2/3, 1/3) = 0.9182958, so
E(M_k) → E(μ) ∈ [0.917810, 0.918493] and **ρ_k → 0**. The ladder saturates. It saturates
*geometrically*.

Note this statement is deliberately estimator-free: I do not rely on an extrapolated E(μ). The
increments are exactly computable at each k, their ratio has a closed rational form, and
summability alone forces ρ_k → 0.

### 2.2a Independent corroboration from the contract's own cited source

After completing the computation above I read Crutchfield & Feldman 2003 directly
(`AOP_Break_CitationSalvage_v0.1.md`, item 2). They report the Even Process's entropy-rate
convergence as exponential, fitting hµ(L) − hµ = A·2^(−γL) with **A = 0.388 ± 0.019, γ = 0.501 ±
0.007**, and give E ≈ 0.902 bits. γ ≈ 1/2 is the same exponent as the ρ_k ∝ k·2^(−k/2) law derived
above. So F2 is not merely my computation against the contract: **the primary source the contract
cites for E itself has reported this process's geometric convergence since 2003.** They also confirm
the antecedent the contract got right — the even system is sofic and "no finite-order Markovian source
can generate this" — which is exactly the infinite-Markov-order / summable-residual distinction the
contract collapsed.

### 2.3 Why this matters, and why it is not fatal to model 3

The contract chose model 3 to be the model where ρ_k **fails** to saturate, and told the gate seat in
advance to expect non-saturation. A seat running the gate will observe geometric decay and — following
the contract — may record it as an anomaly or a bug. It is neither. It is the correct behaviour of a
residual against a finite-order projection of a finite-Cμ process.

The deeper problem is that the contract has conflated **infinite Markov order** with **non-summable
residual**. Infinite Markov order says no finite k reproduces the process exactly. It says nothing
about the *rate* at which the order-k projection approaches it. The Even Process has infinite Markov
order and a finite, small statistical complexity, and its residual decays as fast as a geometric
series. To get a residual that genuinely refuses to saturate you need a process with infinite E, and
the Even Process is not one.

Model 3 is still a **good** benchmark — it is the only model in the suite where the ladder is
non-trivially graded, and F2 upgrades what it tests. But the §3.2.2 and §9 rationales must be
rewritten: the diagnostic content is the **decay law**, not a floor. And §8's K4 needs re-reading,
since its "if the k≥1 diagnostic rungs also fail to isolate any Memory-specific structure" test was
written expecting a persistent residual to isolate.

**A caution the repaired text should carry.** The rungs where ρ_k is largest are the rungs that are
cheapest to estimate, and vice versa. Counting allowed k-words on the Even Process: at k=16 there are
4180 words and a plug-in entropy estimator needs N ≳ 1.6e5 samples for its bias to fall below ρ_16;
at k=22, 75024 words and N ≳ 1.8e7. So the interesting tail of the ladder is exactly the part that a
sampled implementation cannot reach — which is the half of Aster's item 2 (finite-sample estimation,
smoothing) that v0.2.1 does not answer at all.

---

## 3. F3 (major) — Boundary and Integration cannot run on models 1–4

§9's gate rule: "Run every contrast (Boundary/CBSD, Memory ladder, Drive, Integration internal-cut
extension) on **at least the computable models 1–6** end to end."

CBSD = I(X_in ; X_out) requires a declared in/out partition of the state space; the Type-A null is a
product scramble μ̂ = μ_in ⊗ μ_out. Models 1–3 are single-symbol binary processes (|alphabet| = 2)
and model 4 is a three-state ring (|S| = 3). **Two and three are prime; none of these state spaces
admits a non-trivial product factorization.** There is nothing to cut and nothing to scramble. The
contract half-concedes this for model 1, whose cut field reads "trivial single cut," but then requires
all four contrasts on models 1–6 anyway; and model 4's cut field, "temporal + state," names no
partition.

| model | Boundary (CBSD) | Memory | Drive | Integration |
|---|---|---|---|---|
| 1 i.i.d. | **undefined** | degenerate (§3.2, below) | trivially 0 | **undefined** |
| 2 Golden Mean | **undefined** | yes | 0 | **undefined** |
| 3 Even | **undefined** | yes | 0 | **undefined** |
| 4 three-state ring | **undefined** | yes | yes | **undefined** |
| 5 K&W | yes | yes | yes | yes |
| 6 K&W anti | yes | yes | yes | yes |

So the Boundary contrast and the Integration extension each have **exactly two** computable cases,
both K&W variants, and both flagged "simulable" rather than analytic — against a charter preference
for analytic results. Worse for K5: the kill condition asks whether the Integration reading is a
determined function of the Boundary Type-A operation on that cut. That comparison needs at least one
model where both run and the internal partition is not the external one. Models 5 and 6 share a
single system/environment cut. **K5 as written cannot be evaluated by the suite that is supposed to
evaluate it** — which is Aster's P4 slot 6 ("internal-cut scramble demonstrating operator overlap")
silently dropped in the model-3/model-4 rewrite.

Related, and smaller: model 1 is i.i.d. **by construction**, so its k=0 Memory null (project onto the
single-symbol marginal) is the **identity map** — ΔV = 0 for every V, analytically. That is exactly
§7.1/K2 "degenerate by construction," which §8 says is a declaration error to be repaired *before*
the gate. Model 1's assigned role, "all-null reference," makes the degeneracy intentional. It should
be labelled as an analytic identity check rather than a contrast, or K2 fires on the reference model
by design.

---

## 4. F4 (major) — the k≥1 rungs do not dissociate Memory from Drive on five of six models

§3.2.4 is careful and correct about the k=0 null: an i.i.d. process has zero entropy production, so
the full Memory null drives σ→0 and is "not identifiable against Drive." It then says: "The k≥1
diagnostic rungs are where Memory-specific structure, if any, appears **without the total Drive
confound**."

That inference presumes the confound is *partial* at k≥1 — that climbing the ladder buys back
identifiability by degrees. On the suite as declared, it buys nothing, because there is no Drive to
be confounded with. Measured path asymmetry σ_Δ (Δ=10, exact word distributions):

| model | σ |
|---|---|
| 1 i.i.d. | 0 (equals its own reverse) |
| 2 Golden Mean | 0.000e+00 |
| 3 Even | 0.000e+00 |
| 4 three-state ring | 0.720 (tunable; the only σ > 0 model) |

and on the Even process, σ_Δ(M_k) = 0 at **every** rung k = 0…6, not just k = 0. Five of the six
computable models have σ = 0 identically. On those, "Memory is confounded with Drive" and "Memory is
cleanly identified" are indistinguishable, because ΔV_Drive ≡ 0 whatever you do. There is no
gradient of confound to climb, so the k≥1 rungs cannot demonstrate the dissociation §3.2.4 promises
them.

Consequence for the panels: §6 tells the gate seat that the forced σ>0 ⇒ E>0 edge "will appear as
real off-diagonal in Panel B by construction **on model 4**." That is right, and it is the whole of
it — the promised off-diagonal has exactly one computable witness, and it is the same single model
that F1 shows is sign-indeterminate. The Drive column of Panel B rests entirely on model 4.

And on model 4 the two nulls are distinguishable as *interventions* (Drive null a=b=0.3 gives
σ=0, E=0.014012; Memory k=0 null gives σ≈0, E≈0) but not as *attributions*: at a=0.48 the two
contrasts give ΔV_Drive = +0.952381 and ΔV_Mem,k=0 = +0.619048 — same sign, same order of magnitude.
§3.2.4's non-identifiability is real and it is not repaired by the ladder.

---

## 5. F5 (major) — the Model-4 rationale overstates a true claim

§9's recorded rationale: "A two-state Markov chain satisfies detailed balance for *every* rate
choice, so its stationary entropy production is identically zero — it can never exhibit σ>0 and is
disqualified as a Drive control."

The **conclusion** is right and Aster's item 4 was right to force the rewrite. The **reason** as
stated is false, and it is false in a way that matters, because it is stated as a property of
two-state chains rather than of single-channel two-state chains. A two-state system with **two or
more independent transition channels** is a genuine NESS with σ > 0:

| channels (k₁₂, k₂₁) | stationary π | σ (nats/time) |
|---|---|---|
| (1, 1), (10, 0.1) | (0.0909, 0.9091) | **3.767867** |
| (1, 2), (5, 0.3) | — | **4.098025** |
| (0.5, 4), (7, 0.05) | — | **17.005612** |
| (2, 1), (6, 3) — equal ratios | — | 1.23e−32 ≈ 0 |

The last row is the control: when the two channels have equal forward/reverse ratios there is no
cycle affinity and σ vanishes, as it must. Two states, multiple channels, σ > 0 — the cycle lives in
*channel space*, not state space.

The correct statement is the one Aster actually made: a two-state chain **with a single edge pair**
has no cycle in its transition graph, hence no independent cycle affinity, hence σ ≡ 0 at
stationarity (Kolmogorov's criterion). The contract should say "a two-state chain with a single
transition channel," and should keep the three-state ring for the separate and better reason that it
is the canon's own computed Drive control (Figure DM).

This is a defect of *stated reason*, not of decision. I flag it because the sentence is recorded as a
rationale for a benchmark choice, and a reviewer who knows multi-channel two-state NESS will read it
as an error about elementary stochastic thermodynamics and discount the surrounding argument.

---

## 6. What I could not break

Honest ledger of attacks that failed.

- **The typed A/B split (§0).** I looked for a case where a Type-A and a Type-B null coincide or
  where the assignment is forced the other way. I did not find one. The split is doing real work.
- **§3.1's CBSD disclaimer.** The renaming and the "not a boundary mechanism" warning are correct and
  necessary; I could not construct a case where CBSD is mistaken for a maintenance measure once the
  disclaimer is honoured. The disclaimer's cost is F3: once CBSD is only an informational role
  measure, it needs a factorizable state space, and the suite mostly does not supply one.
- **The Golden Mean value.** The contract asserts E ≈ 0.2516 for model 2. Exactly computed:
  **E = 0.2516291674**, and ρ_k = 0 for all k ≥ 1 to within 5e−14 (floating point). Model 2 does
  exactly what the contract says it does. This is the suite's one fully clean, fully analytic,
  fully verified benchmark.
- **§7.1's degeneracy escape.** The contract's escape (path/first-passage V and/or non-trivial μ₀)
  genuinely works on model 4: the Drive null preserves π = uniform exactly, and MFPT is a
  first-passage functional, so ΔV ≠ 0 and the contrast is non-degenerate. §7.1 is sound. The irony is
  that the escape route is what creates F1 — first-passage functionals are direction-sensitive in a
  way one-time-marginal functionals are not.
- **§7.3 separating identifiability from admissibility.** Not only survived; F1 is an instance of it.
  The i.i.d. and detailed-balance states are perfectly admissible and the *attribution* is what
  fails. The contract built the right category.
- **The identity control caveat (§6).** On a purpose-built factorizable 4-state model (in ⊗ out,
  2×2), the product scramble left both single-block marginals unchanged to ≤1.1e−16 after a forward
  step, at couplings giving CBSD from 0 to 0.113874. The caveat is correctly stated; I could not make
  it bite where the state space actually factorizes.

---

## 7. Dispositions

Against the contract's own §8 pre-declared dispositions. **None of these findings rejects AOP**;
every one bounds what the co-measurement method can currently claim.

| # | Finding | Severity | Contract's own category | Disposition |
|---|---|---|---|---|
| F0a | Increment representation of model 4 gives σ>0, E=0 — a false refutation the canon warned about | **fatal** | §5 scope condition 1 / canon Fig DM caption | Declare model 4's state as ring **position**, R as position-space reversal; restore the canon's increment warning; stop rendering the five conditions as independent boxes. |
| F0b | CBSD is canon's B5, the proxy canon says is *not* boundary strength; B2/B4 omitted | **fatal** | §3.1 "canon axis untouched" | Either adopt B2 (screening residual) and B4 (maintenance burden) as the Boundary contrast, or state plainly that the contract measures the *descriptive* cross-cut slice and is not a Boundary-axis method. Add an interface field F to §2. Withdraw or re-specify K5. |
| F1 | ΔV_Drive sign-indeterminate under an undeclared sub-choice of V | **fatal to gate execution** | §7.3 identifiability / Aster item 6 | Add mandatory V-event declaration (target set + R orientation). State that sign(ΔV_Drive) is a property of (V, target, R), not of σ. §11.2 stays OPEN. |
| F2 | Even-Process ρ_k decays as k·2^(−k/2); ladder saturates | **fatal to the §3.2.2 / §9 rationale** | §3.2.2, model-3 rationale | Rewrite: diagnostic content is the decay law, not a floor. Distinguish infinite Markov order from non-summable residual. Re-read K4. |
| F3 | Boundary and Integration undefined on models 1–4; K5 unevaluable | major | §9 gate rule, K5, Aster P4 slot 6 | Add a factorizable model with a genuine internal partition ≠ external cut. Until then K5 is not testable and must be reported as such. |
| F4 | k≥1 rungs dissociate nothing on the five σ=0 models | major | §3.2.4, K4 | Soften §3.2.4's claim for the rungs; state that dissociation is testable only on model 4, i.e. on one model. |
| F5 | "Two-state chain is always detailed-balanced" is false as stated | major (stated reason) | §9 model-4 rationale | Insert "with a single transition channel." Keep the ring on the Figure-DM ground. |
| — | Model 1's k=0 null is the identity map | minor | §7.1 / K2 | Relabel as an analytic identity check, not a contrast. |

**Citation lane.** Partially discharged in `AOP_Break_CitationSalvage_v0.1.md` — the dedicated seat
parked on a network approval and was stopped, so I verified the reachable subset myself from the
project library. Net: the Golden Mean value, the Still et al. correction (a v0.2.1 repair that fully
worked), K&W's stored/observed split and its actual−intervened sign convention all **verify**; the
Baiesi & Maes support is **true but uncited**; the C&F Prop. 8 attribution needs a cosmetic
narrowing; and K&W's "Eq 5.2 / 5.14" are **NOT VERIFIED** — the DOI resolves to the arXiv preprint,
which uses roman-numeral sectioning and contains none of those decimal numbers. Spinney & Ford,
Schnakenberg, and a second read of Parrondo remain open.

**Companion findings.** The canon-fidelity audit run in parallel
(`AOP_Break_FidelityAudit_v0.1.md`) contributed F0a and F0b above and carries further items in its own
lane that I have not duplicated here — including a mis-numbered reference for E=0 ⟺ i.i.d. inside the
very section that exists to correct a citation error, a truncated canon grade string that upgrades the
theorem by omission, the dropped grain δt and interface F from the declaration tuple, and a
substantively **correct** C-1 finding whose consequence runs back into the contract's own §1.3
definition of σ_Δ. Read the two reports together; where they overlap they were reached independently.

**Verdict on the gate.** §11.2 should stay **OPEN**, and for a reason different from Aster's. Aster
found the gate under-specified; v0.2.1 repaired most of that. What I find is that the gate is now
specified enough to run, and running it on the contract's own designated Drive control yields a
result whose **sign** depends on a choice the specification does not require anyone to record. That
is not a specification gap of the kind v0.2.2 can close by adding prose — it is a genuine property of
first-passage viability functionals under current-reversing interventions, and the contract should
say so out loud. Reported that way, F1 stops being an embarrassment and becomes the contract's own
§5-style scope condition for the Drive axis: **σ is even under current reversal; viability need not
be, so a Drive contrast reports a magnitude cleanly and a sign only relative to a declared event.**

That is a real result, and it is the kind §7.4 and Aster's §5 both say the method should be able to
expose about itself.

---

## 8. Reproduction

All numbers are closed-form or exact-arithmetic on finite state spaces; nothing is sampled.

- Block entropies via labelled transfer matrices on the ε-machines (Golden Mean, Even Process),
  words enumerated to length 30, `H` in bits.
- E(M_k) = H(k) − k·[H(k+1) − H(k)]; ρ_k = E(μ) − E(M_k), with E(μ) bracketed by the monotone
  increments and Cμ, never extrapolated.
- σ for Markov chains as the exact per-step KL rate Σ π_i P_ij log₂(π_i P_ij / π_j P_ji); σ_Δ for
  symbol processes as the windowed forward-vs-reversed word-law KL, per step.
- MFPT by solving (I − P_restricted) m = 1; the ring closed form verified against the linear solve to
  1e−15.
- Ring affinity A = 3·ln(a/b), the a+b = c parameterization giving uniform π for all (a,b).
- Increment representation of the ring: step law (a, b, 1−a−b) on {+1, −1, 0}; i.i.d. because the step
  probabilities do not depend on position, hence E = 0 exactly; its σ is the KL of that law against
  its reversal (+1 ↔ −1), which reproduces the position-space σ to <1e−12.

Figure: `AOP_Break_Figure_v0.2.png` — (a) σ even / ΔV odd in A; (b) mirror pairs at identical σ and E;
(c) unbounded σ with vanishing ΔV; (d) the Even-Process ladder against k·2^(−k/2); (e) the
increment-representation trap, σ coincident across representations while E collapses to zero.

*Attack seat: Claude Science, 2026-08-07. Non-canon. Authorizes no canon edits. The seat that built
v0.2.1 did not run this attack, and this seat did not build v0.2 or v0.2.1.*
