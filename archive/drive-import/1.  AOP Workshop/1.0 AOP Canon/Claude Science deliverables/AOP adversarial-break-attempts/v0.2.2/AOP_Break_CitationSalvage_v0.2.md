# AOP Break Attempt — Citation / External-Claim Lane

**Target:** `AOP_InterventionContract_v0.2.2` (Issued 2026-08-07; PROPOSAL, non-canon)
**Parent canon (context only):** `AOP_CANON_MASTER_v1.27.md`
**Lane:** external claims — anything v0.2.2 asserts about outside literature, named results,
named quantities, or named frameworks. Fidelity-to-canon and closed-form counterexamples are
other lanes and are not duplicated here.
**Deliverable version:** v0.2 (supersedes `AOP_Break_CitationSalvage_v0.1.md`, which targeted v0.2.1)
**Date:** 2026-08-08. Non-canon. Authorizes no canon edits.

---

## 0. The governing fact about this target

**v0.2.2 contains zero citations.** Verified mechanically: no author-year string, no DOI, no
arXiv identifier, no bracketed reference number, no reference list, no bibliography section
anywhere in the 21 KB document. The single proper noun in the entire contract is
"Kolchinsky–Wolpert" (§0), and it appears without a year, venue, or locator.

This is not a formatting complaint. The contract is a *methods contract* — a document whose
whole purpose is to fix what must be declared before a falsification gate runs — and §6.4
item 11 requires each executed model–contrast pair to report **"known theorem envelope and
whether the case is inside it."** A reader cannot discharge that requirement against a document
that names no theorem. Every finding in §4 below follows from this one structural fact.

**Method statement.** A row is VERIFIED only where I opened the primary source, located the
passage, and read it. Quotes are ≤20 words and in quotation marks. Where I confirmed only a
bibliographic record, or read a secondary/parent-canon statement rather than the primary, the
row says PARTIAL and says why. Retrieval failures are recorded as NOT VERIFIED and are never
reported as passes.

---

## 1. Per-item verdict table

| # | Claim in v0.2.2 | Verdict | Primary source actually read |
|---|---|---|---|
| 1 | "This is the reverse of the Kolchinsky–Wolpert value convention" (§0) | **VERIFIED** (sign), with a scope qualification | Kolchinsky & Wolpert 2018, arXiv:1806.08053 |
| 1b | Cross-framework comparability implied by "every comparison to that framework must say so" | **PARTIAL** — sign is not the only difference | same |
| 2a | `E = I(X_{≤0}; X_{≥1})`, contiguous past/future split, present on past side (§2.2) | **VERIFIED** | Crutchfield & Feldman 2003, Prop. 8 |
| 2b | Even Process: `ρ_k` "remains positive at every finite `k`" (§2.2) | **VERIFIED** (source + my computation) | C&F 2003 §VI E; own exact DP |
| 2c | Even Process: `ρ_k` "tending toward zero asymptotically" (§2.2) | **VERIFIED** — the v0.2.1→v0.2.2 repair is genuine | C&F 2003 Eq. 81; own exact DP |
| 2d | Distinction: infinite Markov order ≠ non-summable residual | **VERIFIED** | C&F 2003 §VI E |
| 2e | Published Even-Process `E` value usable as the benchmark target | **FALSE-MISATTRIBUTED (latent)** — the literature number is 1.8% off the exact value | C&F 2003 §VI E; own exact DP |
| 2f | Order-`k` Markov projection `M_k` as a diagnostic ladder (§2.2) | **VERIFIED** as a standard object with a closed form — **UNCITED** | C&F 2003 Prop. 11 |
| 3a | `σ_Δ(t) = Δ⁻¹ D_KL(P ‖ R P)` as entropy production (§2.3) | **PARTIAL → defective under the contract's own §1 field 11** | Roldán & Parrondo 2012; Parrondo, Van den Broeck & Kawai 2009; Seifert 2012 |
| 3b | "the stationary long-window limit, when it exists, is `σ`" | **VERIFIED** | Roldán & Parrondo 2012, Eq. (8) |
| 3c | Detailed-balance projection at fixed stationary distribution is **non-unique** | **VERIFIED** — the contract's concession is correct | own construction (exhibited below) |
| 3d | That projection is a standard named construction | **PARTIAL** — the standard object exists (additive reversibilization); its canonical attribution NOT VERIFIED | see §3, NOT-VERIFIED table |
| 3e | "Any current-shortens-persistence theorem is applied only inside its complete stated envelope" (§2.3) | **NOT VERIFIED as written** — real theorem, never named; envelope not retrievable from the contract | canon v1.27 names it; primaries not retrieved |
| 4a | Total correlation `TC` as an Integration reading (§2.4) | **PARTIAL** — definition standard, attribution not read at primary level, **UNCITED in contract** | canon v1.27 reference list; DOI title match only |
| 4b | `Φ_MIP` "under a fully declared partition search and **normalization rule**" (§2.4) | **SPECIFICATION GAP CONFIRMED** — normalization is contested in the primary literature | Tononi 2004; Mediano, Rosas et al. 2021 |
| 4c | Use of the symbol `Φ_MIP` at all | **FALSE-MISATTRIBUTED (terminological)** — imports an IIT object the parent canon deliberately renamed away from | Tononi 2004; canon v1.27 changelog |
| 5a | `B2 = I(inside; outside | F)` as interface screening (§2.1) | **NOT VERIFIED** — standard conditional-independence reading, primaries not read, **UNCITED** | — |
| 5b | i.i.d. source returns `E = 0` (§5.1 test 1) | **VERIFIED** — **UNCITED** | C&F 2003, process classification |
| 5c | Reversible correlated order-1 chain returns `E > 0` (§5.1 test 2) | **VERIFIED** via a closed form the contract never states — **UNCITED** | C&F 2003, Prop. 11 |
| 5d | Time-reversal parity / even–odd variables in declaration field 11 | **NOT VERIFIED** — primary for the parity decomposition not retrieved | — |

---

## 2. The findings, in full

### 2.1 Item 1 — Kolchinsky–Wolpert. The sign claim is right; the comparability claim is not established.

**Source read.** Artem Kolchinsky & David H. Wolpert, "Semantic information, autonomous agency
and non-equilibrium statistical physics," arXiv:1806.08053v3, 19 pp. (published as *Interface
Focus* **8**(6):20180041, 2018, doi:10.1098/rsfs.2018.0041). Read from the project library copy
`kolchinsky_wolpert_2018_semantic_information_arxiv_1806.08053.pdf`.

**What K&W actually do.** Two places fix the convention, one prose and one formal.

- §I, prose: they define value as **"the difference between the system's viability after time τ
  under the actual distribution, versus"** the intervened distribution.
- §V A, formal, Eq. (6): `ΔV_tot^stored := V(p_Xτ) − V(p̂^full_Xτ)`.

Both are **actual minus intervened**. The contract's §0 sign is **intervened minus actual**.
**The contract's characterisation is correct: VERIFIED.**

**The qualification, which is a finding.** The contract writes that its convention "is the
reverse of the Kolchinsky–Wolpert value convention; every comparison to that framework must say
so" — i.e. it treats a sign flip as sufficient to make comparisons well-posed. It is not,
because in K&W `V` is not a free declaration:

- **`V` is a fixed functional, not a declared one.** K&W Eq. (2): `V(p_Xτ) := −S(p_Xτ)` — the
  negative Shannon entropy of the system marginal. They are explicit that this is a choice with
  reasons, and that **"the viability function is exogenously determined by the scientist"** —
  but *their* published quantities all use negentropy. The contract's §1 field 5 lets `V` be any
  declared endpoint, path, survival, or first-passage functional. A survival-probability `θ` and
  a negentropy `ΔV` are not the same quantity with opposite signs; they are different quantities.
- **The intervention class is fixed too.** K&W's `ΔV_tot^stored` is defined only against the
  *full scramble* of the initial system–environment mutual information, `p_{X0,Y0} ↦ p_{X0}p_{Y0}`
  (Eq. 5), and their graded family is generated by coarse-graining functions φ on the environment
  (Eq. 8). The contract's Type-A Boundary null is a product scramble of a *declared inside/outside*
  cut preserving declared within-side marginals — related but not identical, and its Memory and
  Drive contrasts are mechanism interventions with no K&W counterpart at all.

**Required repair.** §0 should state the comparison condition, not just the sign: a comparison
to K&W is meaningful only when `V` is negentropy of the declared system marginal *and* the
intervention is a scramble of initial system–environment mutual information. Otherwise the
frameworks share a schema, not a scale. And the sentence must carry the citation.

**Note for the record.** The contract nowhere cites K&W — no year, no venue, no DOI. This is
the contract's only named external framework and it is invoked bare.

---

### 2.2 Item 2 — Excess entropy, `M_k`, and the Even Process. The contract's repair is correct, and the literature value it would be checked against is wrong.

**Sources read.** J. P. Crutchfield & D. P. Feldman, "Regularities Unseen, Randomness Observed:
Levels of Entropy Convergence," *Chaos* **13**(1):25–54 (2003); read from the arXiv version
cond-mat/0102181v1, 35 pp., project library copy. Also J. P. Crutchfield & D. P. Feldman,
"Statistical Complexity of Simple 1D Spin Systems," arXiv:cond-mat/9702191v1, 4 pp., in library
(consulted; contributes nothing the 2003 paper does not carry, and is not the source for the
Even Process material).

**(a) The `E` definition — VERIFIED.** C&F Prop. 8: **"The excess entropy is the mutual
information between the left and right (past and future) semi-infinite halves"** of the chain,
their Eq. (53), *"when the limit exists."* The contract's `E = I(X_{≤0}; X_{≥1})` with a
contiguous split and the present on the past side is this object. C&F's gloss — `E` "measures
the amount of historical information stored in the present that is communicated to the future" —
is the reading the contract uses.

**(b) and (c) The Even Process ladder claim — VERIFIED, and it is a real repair.** v0.2.1 said
the residual "never saturates"; v0.2.2 says it "is expected to remain positive at every finite `k`
while tending toward zero asymptotically." Both halves check out.

*Positivity at every finite k.* C&F establish the antecedent directly: the even system is sofic,
its set of irreducible forbidden words is infinite, and **"no finite-order Markovian source can
generate this"** system. So no `M_k` reproduces the process and `ρ_k > 0` for every finite `k`.
I confirmed by exact computation (belief-state dynamic programming on the two-state ε-machine,
exact `H(L)` to `L = 4000`, `ρ_k = E − E(M_k)` with `E(M_k) = H(k) − k·h_μ(M_k)`):

| k | 1 | 2 | 4 | 8 | 16 | 24 | 32 | 40 | 48 | 60 |
|---|---|---|---|---|---|---|---|---|---|---|
| `ρ_k` | 8.74e−1 | 7.11e−1 | 4.81e−1 | 1.83e−1 | 1.93e−2 | 1.70e−3 | 1.37e−4 | 1.05e−5 | 7.75e−7 | 1.49e−8 |

Strictly positive throughout, monotone decreasing, no saturation.

*Asymptotic decay to zero.* My fit over `k ∈ [20, 50]` gives `ρ_k ~ 2^(−0.461 k)` — geometric.
C&F independently corroborate the mechanism: for the even process they fit
`h_μ(L) − h_μ = A·2^(−γL)` (their Eq. 81) and report **`A = .388 ± 0.019` and `γ = .501 ± .007`**.
The contract's asymptotic-decay claim is therefore supported both by my exact computation and by
the primary literature on the very process it selected. **The v0.2.1 defect is genuinely fixed.**

**(d) Infinite Markov order vs non-summable residual — VERIFIED as correctly distinguished.**
C&F carry exactly this distinction: the process is not finite-order Markovian (sofic), *and* its
entropy convergence is exponential, so `E` is finite and the residual is summable. Conflating
the two is what v0.2.1 did; v0.2.2 does not.

**(e) The benchmark number is a trap — this is the item's real finding.**

C&F report, for the Even Process, **"We find that E ≈ 0.902 bits"**, alongside `h_μ = 2/3`
bits/symbol and `H(1) ≈ 0.918`. Their `E` is a numerical estimate from entropy-convergence
curves (they also give the approximation `E_γ ≈ 0.86` from their Corollary 1).

The exact value is different. My belief-state DP gives

> `E(Even) = H(L) − L·h_μ` → `0.918295834007` at `L = 4000`,
> against `log₂3 − 2/3 = 0.918295834054` — agreement to `4.7e−11`.

So **`E(Even) = log₂3 − 2/3 ≈ 0.9182958` bits**, and the published `0.902` is **1.77% low**.

Why this matters for *this* contract, specifically: §6.1 declares an **analytic-first rule** —
"Use exact calculations on models 1–4 whenever possible" — and §5.1 test 3 makes the Even Process
a calibration benchmark. A harness built to §6.1 will compute `0.91830`. A reviewer regression-
checking it against the only published number, in the only paper the framework uses for `E`, will
see a 1.8% discrepancy and may score the harness as failing when it is the *source* estimate that
is imprecise. **Repair:** §4.1/§5.1 must state the exact benchmark target `log₂3 − 2/3` as the
analytic value, cite C&F for the process and its `h_μ = 2/3`, and note explicitly that C&F's
`E ≈ 0.902` is a numerical estimate not to be used as the tolerance anchor.

**A second, sharper trap in the same benchmark.** For the Even Process the exact `E` and the
single-symbol entropy coincide: `H(1) = H(1/3, 2/3) = log₂3 − 2/3`, the same number as `E`
(C&F's own `H(1) ≈ 0.918` is this quantity). Consequence for §6.3: a **mutation test that seeds a
"wrong lag" defect — computing `H(1)` where `E` was intended — will not be caught on this
benchmark**, because both give `0.9183`. §6.3 explicitly lists "wrong lag" among the defects the
suite must catch. The Even Process cannot serve as the detector for that mutation. This is a
genuine hole in the predeclared mutation battery and it is invisible without the exact values.

**(f) `M_k` is a standard object with a closed form the contract does not state.** The
contract's `M_k` construction (match the `k`-block law; transition kernel = observed conditional
on positive-probability contexts) is the standard order-`k` Markov approximation. C&F Prop. 11
gives its excess entropy in closed form: **"For an order-R Markovian process, the excess entropy
is given by `E = H(R) − R h_μ`"** (their Eq. 57). That single formula is what makes the whole
diagnostic ladder analytically computable — it is the formula my table above uses. The contract
requires the ladder and never states or cites the identity that makes it tractable.

---

### 2.3 Item 3 — Entropy production. The definition is standard; the contract's own declaration field breaks it.

**Sources read.**
- E. Roldán & J. M. R. Parrondo, "Entropy production and Kullback-Leibler divergence between
  stationary trajectories of discrete systems," *Phys. Rev. E* **85**:031129 (2012);
  arXiv:1201.5613v1, 14 pp. Fetched and read.
- J. M. R. Parrondo, C. Van den Broeck & R. Kawai, "Entropy production and the arrow of time,"
  *New J. Phys.* **11**:073008 (2009); arXiv:0904.1573, 15 pp. Fetched and read.
- U. Seifert, "Stochastic thermodynamics, fluctuation theorems and molecular machines,"
  *Rep. Prog. Phys.* **75**:126001 (2012); arXiv:1205.4176, 105 pp. Fetched; read §5 (Eqs. 146–150)
  and §3.3.

**(a) The KL-per-unit-time form — the literature is unambiguous and the contract matches it.**
Roldán & Parrondo Eq. (8) gives the entropy production rate in a NESS as
`⟨Ṡ⟩ = lim_{τ→∞} (k/τ)·D[P({z(t)}) ‖ P({z̃(τ−t)})]`, and their Eqs. (10)–(11) define the
`m`-th order KLD `D_m^X = D[p(x_1^m) ‖ p(x_m^1)]` against the *reversed sequence*, with the KLD
rate `d^X = lim_{m→∞} D_m^X / m`. Parrondo–Van den Broeck–Kawai give the protocol-level identity
`⟨W⟩_diss = kT·D(ρ‖ρ̃)` (their Eq. 2), stating an **"exact relationship between the entropy
production and the distinguishability of a process from its time-reverse."** Seifert's Eq. (146)
introduces the same tool as `D[p‖q] ≡ ∫dy p(y) ln[p(y)/q(y)] ≥ 0`.

The contract's `σ_Δ(t) = Δ⁻¹ D_KL(P_[t,t+Δ] ‖ R P_[t,t+Δ])` is this object at finite window, and
its "the stationary long-window limit, when it exists, is `σ`" is exactly Roldán & Parrondo's
`τ → ∞`. **VERIFIED as a faithful transcription.**

**(b) The defect: under the contract's own §1 field 11, `σ_Δ` is not entropy production — it is a
lower bound on it, and the contract never says so.**

Roldán & Parrondo state the restriction plainly: when one observes not the microtrajectory but
"the trajectory followed by one or several observables of the system x(t), **the KLD only
provides a lower bound to the entropy production**." Formally their Eq. (12): `⟨Ṡ⟩ ≥ k·d^X`,
with equality "saturated if the random variable is the microstate of the system" and the sampling
rate infinite, or if the observable determines the entropy production uniquely. The mechanism is
their Eq. (2), the data-processing inequality: KLD decreases under coarse-graining. Seifert makes
the same point at Eq. (149)–(150) (coarse graining "leads to a lower bound on the dissipated work
since relative entropy decreases under coarse graining").

Now read the contract against that. §1 field 11 requires the declaration to fix "observed state
representation, **coarse-graining**, even/odd variables, and the time-reversal involution `R`."
The contract therefore *anticipates and licenses* coarse-grained readings — and §2.3 then calls
the resulting quantity "**path asymmetry / entropy production `σ`**" with no bound language
anywhere. Under any declared coarse-graining the identification is false as an equality.

This is not pedantry within this contract's own logic: §3 requires each cell to be labelled
ANALYTIC or ESTIMATED, and §6.4 item 11 requires the theorem envelope. A quantity that is an
equality on the microstate and an inequality on every coarse-graining has an envelope, and the
contract states neither the envelope nor which side of it a given benchmark sits on. Benchmark 4
(the driven three-state *position* ring, with the increment representation explicitly excluded) is
precisely a declared coarse-graining of the underlying dynamics.

**Repair.** §2.3 must either (i) rename the quantity — "declared-representation irreversibility
rate", reserving "entropy production" for the microstate case — or (ii) state the bound
`σ_true ≥ σ_Δ^declared` with the saturation condition and cite Roldán & Parrondo Eq. (12). And
§1 field 11 should carry an explicit flag for whether the declared representation saturates the
bound. Note this cuts *for* the contract in one place: making the coarse-graining declared is
exactly what lets the bound direction be stated at all. The defect is the missing sentence, not
the design.

**(c) Non-uniqueness of the detailed-balance projection — the contract's concession is correct.**

§2.3: "The null is a declared detailed-balance projection at fixed stationary distribution
relative to `R`. Any non-uniqueness in that projection must be resolved in `D`." I tried to break
this by showing the projection *is* unique under natural side constraints. It is not. On a
4-state ring with uniform stationary law `π` and generator `L[i,i+1] = w+a`, `L[i,i−1] = w−a`
(`w=1, a=0.6`), all four of the following are detailed-balance with respect to the *same* `π`:

| construction | DB wrt π | π-stationary | per-state escape rate |
|---|---|---|---|
| additive reversibilization `(L + L*)/2`, `L* = diag(π)⁻¹Lᵀdiag(π)` | yes | yes | (2, 2, 2, 2) |
| equal-conductance ring | yes | yes | (2, 2, 2, 2) |
| alternating-conductance ring (0.5 / 1.5) | yes | yes | (2, 2, 2, 2) |
| ring + chords | yes | yes | (2.7, 2.7, 2.7, 2.7) |

Rows 1–3 agree on stationary law **and** on every per-state escape rate and still differ as
generators; row 4 shows the family is not even confined to the original support. The projection
is a continuum, not a point. The contract is right to require `D` to pin it, and right that
failing to pin it is a declaration error rather than a result. **Could not falsify.**

**(d) The construction has a standard name, which the contract does not use.** The `(L + L*)/2`
object above is the additive reversibilization, standard in the non-reversible Markov-chain
literature. I attempted the canonical attribution (Fill 1991, *Ann. Appl. Probab.* 1(1):62–87)
and retrieved the PDF, but the scan carries **no text layer** (882 characters extracted across
the whole document, all of it JSTOR boilerplate), so I could not read the definition. Recorded
as NOT VERIFIED, not as a pass. The contract should name whichever projection it declares.

**(e) "Any current-shortens-persistence theorem" — an uncitable theorem invoked by description.**

This is the item the lane brief anticipated, and it is a finding.

§2.3 says: "Any current-shortens-persistence theorem is applied only inside its complete stated
envelope. Outside that envelope, the sign is empirical and no theorem-based prediction is made."
The epistemic posture is exemplary. The problem is that **the contract never names the theorem,
its authors, its statement, or its envelope** — so "its complete stated envelope" has no
referent, and §6.4 item 11 ("known theorem envelope and whether the case is inside it") cannot
be discharged by any reader working from the contract alone.

The theorem is real. The parent canon v1.27 names it and states an envelope: for a
**measure-preserving current (divergence-free, at fixed stationary distribution, with ∇U·ℓ = 0)
in the small-noise limit**, circulation "can only shorten or leave unchanged the mean first-
passage time, never lengthen it," attributed to **Lee & Seo 2021, Lemma 3.4 & Cor. 3.9** and
**Bouchet & Reygner 2016**, with the canon's own double-well confirmation
(`μ₊(A) = 1 + √(9+8A²)`, ~287× faster escape). So this is a **contract defect, not a canon
defect**: the canon carries the citation and the envelope; the contract strips both and keeps
only the hedge.

**I did not read Lee & Seo 2021 or Bouchet & Reygner 2016.** The arXiv interface rate-limited
(HTTP 429) and the DOI I tried for Bouchet–Reygner resolved to an unrelated paper (a
Ruijsenaars–Schneider lattice article), so I have no primary text for either. Both are recorded
NOT VERIFIED below. What I verify here is only that the contract invokes an unnamed theorem and
that its parent document names one that fits the description.

**Repair.** §2.3 must name the theorem, state the envelope inline (measure-preserving current,
fixed stationary distribution, small-noise limit, MFPT as the persistence functional), and cite
it — otherwise §6.4 item 11 is unexecutable and benchmark 4's Drive prediction has no declared
theoretical status.

---

### 2.4 Item 4 — `TC` and `Φ_MIP`. One uncited standard; one requirement that presumes a settled object.

**(a) Total correlation.** The definition the framework uses is `TC = Σ_i H(X_i) − H(X)`, which
the parent canon attributes to **Watanabe S., "Information theoretical analysis of multivariate
correlation," *IBM J. Res. Dev.* 4:66–82 (1960), doi:10.1147/rd.41.0066** — I read that entry in
canon v1.27's reference list, and the DOI resolves to a record whose title matches exactly. But
the paper is **closed access**: Unpaywall, Semantic Scholar, PMC, and CrossRef TDM all report no
open location. **I did not read Watanabe 1960.** PARTIAL — bibliographic record confirmed, primary
passage not read. Separately: **v0.2.2 itself never mentions Watanabe** (no occurrence of the
name in the contract), so `TC` is invoked as an undefined-in-document, unattributed quantity in
§2.4 and §4.1 model 6.

**(b) `Φ_MIP` and the normalization requirement — the specification gap is confirmed.**

**Source read.** G. Tononi, "An information integration theory of consciousness," *BMC
Neuroscience* **5**:42 (2004), 22 pp., project library copy.

Tononi's construction is precise, and it does *not* do what the contract's phrasing implies.
Effective information across a bipartition, `EI(A↔B)`, is compared across bipartitions only after
normalization — **"should be normalized by Hmax(A↔B) = min{Hmax(A); Hmax(B)}"** — and the
minimum information bipartition is the one minimizing `EI(A↔B)/Hmax(A↔B)`. But then:
**"The information integration for subset S, or Φ(S), is simply the (non-normalized) value of
EI(A↔B) for the minimum information bipartition"** — i.e. `Φ(S) = EI(MIB_{A↔B})`.

So in the source, normalization enters the **argmin only**, never the reported value. A contract
that requires "a fully declared partition search **and normalization rule**" as if the two were
one knob has already lost the distinction that the primary source draws. Two harnesses could both
comply with §2.4 and report different numbers by normalizing the *value* rather than only the
*selection*.

**Source read.** P. A. M. Mediano, F. E. Rosas, A. I. Luppi, R. L. Carhart-Harris, D. Bor,
A. K. Seth & A. B. Barrett, "Towards an extended taxonomy of information dynamics via Integrated
Information Decomposition," arXiv:2109.13186v1, 29 pp., project library copy.

This settles the "is normalization contested?" question in the affirmative, and worse. The
whole-minus-sum measure `Φ^WMS` (their Eq. 3) **"can be negative in highly redundant systems"**,
which they note has **"been used as an argument to discard Φ^WMS as a suitable measure"**, and
they propose a *revised* `Φ^R` that adds back double-counted redundancy. On a Gaussian AR system
`Φ^WMS` goes negative while `Φ^R` stays positive; on a whole-brain model `Φ^WMS` shows a downward
peak — **"a conceptually problematic negative value of integration"** — where `Φ^R` shows a
strong positive one. They also demonstrate the deeper problem for benchmarking: three qualitatively
different two-bit systems (copy, downward-XOR, parity-preserving-random) are **"'equally
integrated': Φ^WMS = 1 for all of them."**

Consequences for the contract, both concrete:
1. **A declared normalization rule buys reproducibility, not comparability.** §2.4 gets a number
   a second party can reproduce, but that number is not comparable to any published `Φ` and not
   comparable across contract executions using different declared rules. §3's status labels have
   no cell for "reproducible but incommensurable," and §5.2 F5 (Integration adds no content) can
   be triggered or avoided by the choice of rule.
2. **`Φ`-family measures can be sign-unstable.** §5.1 test 8 requires the signed control to
   "recover the predeclared sign under the intervened-minus-actual convention." If the declared
   Integration reading is a whole-minus-sum-type `Φ`, the *reading itself* can go negative for
   reasons unrelated to viability — a confound the contract's sign machinery does not separate.
   `TC` is immune (non-negative by construction); `Φ_MIP` is not. §2.4 offers them as
   interchangeable alternatives and they are not.

**(c) The symbol `Φ_MIP` is itself a misattribution the parent canon already fixed.** Canon v1.27
records that it "**renames Φ_MIP to minimum-cut dependence and deletes the inference from its
positivity to individuality**." Contract §2.4 writes "minimum-cut dependence `Φ_MIP`", using the
retired symbol as an apposition to the current name. Writing `Φ_MIP` imports the IIT object —
and with it the consciousness/individuality reading the canon deliberately severed. As an
external-attribution matter: the contract claims kinship with a literature whose claims it does
not intend to inherit, and says nothing to disclaim them. **Repair:** drop `Φ_MIP`; use
"minimum-cut dependence" and, if the IIT lineage is wanted, cite Tononi 2004 with an explicit
statement of what is *not* being carried over.

---

### 2.5 Item 5 — Other external anchors found

- **`B2 = I(inside; outside | F)` as interface screening (§2.1).** The conditional-independence /
  screening reading is standard and the parent canon anchors it (Pearl 1988; Faes, Marinazzo &
  Stramaglia 2017). I read neither primary. The contract cites neither. NOT VERIFIED + UNCITED.
- **i.i.d. ⇒ `E = 0` (§5.1 test 1).** C&F, process classification: **"Memoryless processes: ... We
  have E = 0 and T = 0. Independent, identically distributed (IID) processes are examples of this
  class."** VERIFIED; uncited in the contract.
- **Reversible order-1 chain gives `E > 0`, `σ = 0` (§5.1 test 2).** Follows from C&F Prop. 11 at
  `R = 1`: `E = H(1) − h_μ`. Confirmed numerically on a symmetric two-state chain with `p = 0.8`:
  `H(1) = 1.000000`, `h_μ = 0.721928`, `E = 0.278072`. VERIFIED; the closed form is uncited.
- **The i.i.d. Memory null (§2.2, "order 0").** The contract states that replacing the mechanism
  with the i.i.d. process of the same one-time marginal "drives `E` to zero but also changes
  kinetics and necessarily removes Drive." The `E → 0` half is the C&F memoryless class above. The
  "necessarily removes Drive" half is an implication (`E = 0 ⇒ i.i.d. ⇒ σ = 0`) that the canon
  derives with **five** stated scope conditions including a time-reversal parity condition; the
  contract asserts it in a subordinate clause with none of them. Flagged as an external-claim
  compression; the parity primary is NOT VERIFIED (below).
- **Transfer entropy.** Mentioned only as a possible future reading in §2.4 ("predictive
  irreducibility ... may be proposed later"). No external claim is made; nothing to verify.
- **Benchmarks named in §4.** The suite names the i.i.d. source and the Even Process (both
  standard, both traceable to C&F) but **not** the golden-mean process, which the v0.2.1-era
  material used. No golden-mean claim survives in v0.2.2 to check.

---

## 3. Items NOT VERIFIED, and exactly what each needs

Recorded as open. None of these is a pass.

| # | Item | What it needs | Why it matters |
|---|---|---|---|
| N1 | **Lee & Seo 2021**, Lemma 3.4 & Cor. 3.9 — the non-reversible Eyring–Kramers / current-shortens-MFPT result | Primary text (arXiv rate-limited at HTTP 429 during this lane; needs a retry or a library copy). Then: confirm the lemma numbers, the exact hypotheses, and the small-noise limit statement | It is the theorem §2.3 gestures at. Until read, the contract's Drive envelope rests on the canon's summary, not on a passage anyone in this lane has seen |
| N2 | **Bouchet & Reygner 2016** — generalized Eyring–Kramers for irreversible diffusions | Correct DOI or arXiv id. The DOI I tried (10.1007/s00023-015-0434-9) resolved to an unrelated Ruijsenaars–Schneider paper; that fetch is void and is not used anywhere above | Second leg of the same envelope |
| N3 | **Watanabe 1960**, *IBM J. Res. Dev.* 4:66–82 — total correlation | Publisher or library access; the paper is closed and has no OA location in Unpaywall / S2 / PMC / CrossRef TDM | `TC` is one of only two permitted Integration readings; its definitional source is unread |
| N4 | **Fill 1991**, *Ann. Appl. Probab.* 1(1):62–87 — additive reversibilization | A copy with a text layer, or OCR of the scan (the retrieved PDF yields 882 characters, all boilerplate) | Would let §2.3's detailed-balance projection be named rather than described |
| N5 | **Spinney & Ford 2012** — odd/even-variable entropy-production decomposition | Primary text | Declaration field 11's even/odd variables and the parity scope condition on `σ`-to-`E` rest on it |
| N6 | **Pearl 1988; Faes, Marinazzo & Stramaglia 2017** — screening / conditional-independence reading of `B2` | Primary text | `B2` is the Boundary panel's discriminating proxy (§5.1 test 5) |
| N7 | **Kolchinsky & Wolpert** *Interface Focus* published version | The journal version. The DOI (10.1098/rsfs.2018.0041) resolves via Unpaywall to the arXiv PDF, which uses roman-numeral sectioning | Not load-bearing for v0.2.2 (which cites no equation numbers), but closes a v0.2.1-era open item |

---

## 4. Uncited external claims the contract must be required to cite

Every entry below is a place where v0.2.2 relies on an outside result, definition, convention, or
named object without a citation. The list is complete for the document as read.

1. **§0 — "the Kolchinsky–Wolpert value convention."** Needs the full reference *and* the scope
   condition under which a comparison is well-posed (see §2.1 above), not merely the sign flip.
2. **§0 / §2.2 — `E = I(past; future)` as the Memory reading.** Crutchfield & Feldman 2003,
   Prop. 8, for the semi-infinite contiguous-halves form.
3. **§2.2 — the order-`k` Markov projection and its excess entropy.** C&F 2003 Prop. 11
   (`E = H(R) − R h_μ`), which is what makes the ladder analytically computable.
4. **§2.2 / §4 / §5.1 — the Even Process.** C&F 2003 §VI E for the process, its soficity, `h_μ = 2/3`,
   and the exponential convergence `γ = 0.501 ± 0.007`. Plus an explicit note that C&F's
   `E ≈ 0.902` is a numerical estimate and the analytic target is `log₂3 − 2/3 ≈ 0.9182958`.
5. **§4 / §5.1 — the i.i.d. control returning `E = 0`.** C&F 2003, memoryless-process class.
6. **§5.1 test 2 — the reversible order-1 chain returning `E > 0`.** C&F 2003 Prop. 11 at `R = 1`.
7. **§2.3 — `σ_Δ = Δ⁻¹D_KL(P ‖ RP)` as entropy production.** Roldán & Parrondo 2012 (Eqs. 8, 10–12);
   Parrondo, Van den Broeck & Kawai 2009 (Eq. 2); Seifert 2012 (Eqs. 146–150). **And with them the
   bound direction under coarse-graining**, which is the substantive omission, not the reference.
8. **§2.3 — the detailed-balance projection at fixed stationary distribution.** Name the
   construction (additive reversibilization or whichever is declared) and cite it.
9. **§2.3 — "any current-shortens-persistence theorem."** Name it, state its envelope inline, cite
   it. As written, §6.4 item 11 cannot be discharged.
10. **§2.4 — total correlation `TC`.** Watanabe 1960.
11. **§2.4 — `Φ_MIP` / minimum-cut dependence.** Tononi 2004 for the MIB construction, with an
    explicit statement of what is *not* inherited; and a normalization-status note citing
    Mediano, Rosas et al. 2021 for the contested state of `Φ`-family measures.
12. **§2.1 — `B2 = I(inside; outside | F)` as interface screening.** The conditional-independence
    /screening literature the canon already uses.
13. **§2.2 — "necessarily removes Drive."** The `E = 0 ⇒ σ = 0` implication and its scope
    conditions (the canon states five; the contract states none).
14. **Document-level — a reference list.** There is none. §6.4 item 11 and §7's "gate not
    executable" disposition both presuppose one.

---

## 5. Failed-attacks ledger

External claims I set out to falsify and could not. Each is a place where v0.2.2 is stronger than
it looks, and each should be recorded so a later reviewer does not re-spend the effort.

1. **"This is the reverse of the Kolchinsky–Wolpert value convention."** Attacked on sign. K&W
   Eq. (6) is `ΔV := V(actual) − V(intervened)` and the prose matches. The contract is right.
   *(The scope qualification in §2.1 is a separate, weaker finding — it does not overturn the
   sign claim.)*
2. **"For the Even Process `ρ_k` is expected to remain positive at every finite `k`."** Attacked by
   searching for a finite `k` at which the order-`k` projection saturates. None exists: computed
   exactly to `k = 60` (`ρ_60 = 1.5e−8 > 0`), and it cannot exist, because the even system is
   strictly sofic and C&F state that "no finite-order Markovian source can generate this."
3. **"...while tending toward zero asymptotically."** Attacked by looking for a non-vanishing
   residual floor. `ρ_k` decays geometrically, `~2^(−0.46k)`, consistent with C&F's independently
   fitted `γ = 0.501 ± 0.007` for `h_μ(L)` convergence on the same process. The v0.2.1 → v0.2.2
   repair is real and is corroborated by the framework's own source.
4. **The infinite-Markov-order / summable-residual distinction.** Attacked as a possible
   equivocation. It is not one: C&F carry both facts about the same process, and v0.2.2 keeps
   them apart correctly.
5. **"Any non-uniqueness in that projection must be resolved in `D`."** Attacked by trying to show
   the detailed-balance projection at fixed `π` is unique under natural side constraints
   (stationary law fixed; per-state escape rates fixed; support preserved). It is not — I exhibited
   three distinct DB generators on a 4-ring agreeing on all three constraints. The contract's
   concession is correct and its remedy (resolve in `D`) is the right one.
6. **The `M_k` treatment of zero-probability contexts.** Attacked as potentially ill-defined on the
   Even Process, whose forbidden-word structure creates zero-probability order-`k` contexts. The
   contract's rule ("zero-probability contexts remain outside the reachable support and are not
   assigned arbitrary transitions") is exactly right, and `E(M_k)` is well-defined without any
   arbitrary completion — my exact computation runs cleanly on that rule.
7. **A published closed form for the Even Process `E` that would contradict `log₂3 − 2/3`.**
   Searched C&F 2003 and C&F 1997; neither gives a closed form, only C&F's numerical `E ≈ 0.902`
   and the approximation `E_γ ≈ 0.86`. So my exact value is not contradicted — but it is also not
   independently confirmed by a published analytic result, and it is reported here as my
   computation with the discrepant published estimate stated alongside.
8. **`σ_Δ` finite-window framing.** Attacked as conflating a finite-window object with a
   stationary rate. It does not: §2.3 says "the stationary long-window limit, **when it exists**,
   is `σ`", which is the correct hedge and matches Roldán & Parrondo's `τ → ∞`. The defect in that
   subsection is the missing coarse-graining bound, not this.

---

## 6. What this lane changes

Three items, in descending order of consequence.

1. **§2.3 names its Drive quantity "entropy production" while §1 field 11 licenses coarse-graining
   — under which the primary literature says it is a lower bound, not the quantity.** The contract
   never states the bound. This is a live specification defect, cheaply repaired by one sentence
   plus a citation, and it touches every benchmark that declares a reduced representation —
   including benchmark 4, whose position-space declaration is exactly such a reduction.
2. **The Even-Process benchmark carries two numerical traps.** The published `E ≈ 0.902` is 1.8%
   off the exact `log₂3 − 2/3 ≈ 0.9182958`, so a §6.1-compliant analytic harness will *disagree
   with the literature by construction*; and `E` coincides exactly with `H(1)` on this process, so
   the "wrong lag" mutation that §6.3 requires the suite to catch **cannot be caught here**. Both
   are invisible without exact computation, and both are fixable by stating the analytic target
   and moving the wrong-lag mutation to a benchmark where `E ≠ H(1)`.
3. **`Φ_MIP` is offered as interchangeable with `TC` and is not.** Its normalization is contested
   in the primary literature, whole-minus-sum variants can go negative for redundancy reasons
   unrelated to viability, and the parent canon already renamed the symbol away to avoid importing
   IIT's individuality claims. A "declared normalization rule" delivers reproducibility, not
   comparability — and §5.2 F5's verdict can turn on the rule chosen.

Against these, the contract's Memory lane survives the citation attack essentially intact: the `E`
definition, the projection ladder, the Even-Process behaviour, and the i.i.d. and reversible-chain
controls are all faithful to Crutchfield & Feldman, and the v0.2.1 → v0.2.2 Even-Process repair is
genuine and independently corroborated. What is missing there is references, not correctness.

*Citation / external-claim lane, 2026-08-08. Non-canon. Authorizes no canon edits. Items in §3 are
open and must not be reported as cleared.*
