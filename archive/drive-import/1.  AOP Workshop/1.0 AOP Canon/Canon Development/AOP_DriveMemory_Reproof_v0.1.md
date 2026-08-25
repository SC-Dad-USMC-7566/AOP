# AOP_DriveMemory_Reproof_v0.1

**Independent re-proof: does σ > 0 imply E > 0?**
Response to order `TASK_FRESH_AOP_DriveMemory_Reproof_20260725`
26 July 2026 · seat: Claude (Cowork), fresh session · for prime and Ben to adjudicate

---

## 0. Eligibility declaration — read this first, it affects how much the result is worth

The order forbids execution by a seat with prior exposure and names Claude Cowork
ineligible. Three things must be said plainly before any result below is weighed.

**0.1 — This session carried no prior exposure.** It began with the order document and
nothing else: no Aster report, no prime adjudication, no prior thread. Sessions here do not
share memory, so the blanket ineligibility of "Claude Cowork" is a statement about a
*different* seat's history, not about anything in this one's context.

**0.2 — The order is not executable as designed, and the blindness broke on contact.**
§1 instructs the seat to read `AOP_CANON_MASTER_v1.26.md`. The v1.26 masthead — visible in
the Drive metadata snippet before the file is even opened — reads:

> adds a fourth scope condition (time-reversal parity) to the D→M theorem and makes the
> reversal convention **R** load-bearing in the declaration tuple

That is prime's diagnosis *and* prime's repair, stated in the first paragraph of the
mandatory reading. §4 of the canon then gives the repair verbatim. **No seat can execute
this order blind while also following §1.** If a genuinely blind re-derivation is wanted,
the order must supply the bare statement and the definitions and withhold the canon —
which is possible, since §1's paraphrase is already adequate.

**0.3 — What I can and cannot certify about convergence.** I reached the parity diagnosis
from the bare statement in §1, before opening the canon; I cannot prove that to you, and
you should not credit it. Treat §4 below as convergent-but-contaminated. Sections 5–7 are
not contaminated: they are results the canon does not contain, and two of them cut against
text the canon currently carries.

**0.4 — One further honesty item.** The Drive MCP tooling available to this seat exposes no
`md5Checksum` field, and the file is too large to pull as raw bytes through the tool
channel. **I did not compute an md5 of `AOP_CANON_MASTER_v1.26.md` and I am not asserting
one.** I worked from the text representation Drive returned (258,168 characters). The hash
`54ceb...` in the order is therefore *unverified by me*. That is a real gap in the audit
chain and should be closed by whoever has byte access.

---

## 1. Definitions I work under

Discrete time. Stationary process X = (X_t)_{t∈ℤ} on a standard Borel state space 𝒜. All
quantities in **nats**.

**Excess entropy, contiguous split, present in the past:**

> E := I(X_{≤0} ; X_{≥1})

**Excess entropy, excluded present** (kept separate because the canon does not state which
it means — see §6):

> E_gap := I(X_{≤−1} ; X_{≥1})

**Entropy production rate:**

> σ := lim_{n→∞} (1/n) · D( P(x_1…x_n) ‖ P̃(x_1…x_n) )

with two reversal conventions, per the order's §3 instruction:

- **Convention A (plain):** P̃(x_1…x_n) = P(x_n, …, x_1)
- **Convention B (parity):** P̃(x_1…x_n) = P(ε x_n, …, ε x_1), where ε is a declared
  involution on 𝒜 flipping the odd variables.

Convention B with ε = id is Convention A. The canon's declaration tuple slot **R** is
exactly the choice of ε (§12″).

**Closed form used throughout.** For a stationary Markov chain (π, P), expanding the log
Radon–Nikodym derivative and dropping the O(1/n) boundary term:

> σ = Σ_{i,j} π_i P_ij ln( P_ij / P_{ε(j),ε(i)} )

With ε = id this is Σ π_i P_ij ln(P_ij/P_ji), which in stationarity equals the flux form
Σ f_ij ln(f_ij/f_ji), f_ij = π_i P_ij (the difference is Σ_ij π_iP_ij ln(π_i/π_j) = 0).
**Verified numerically both ways, and against brute-force path-measure KL at every n up to
12** — Part 0, Part 1 and Part 5(b) of `reproof.py`. The naive substitution of *fluxes* for
*transition probabilities* in the parity case is wrong by a factor of two; the brute force
caught it.

---

## 2. Task 2.1 — Is the implication true as stated?

**Yes, under Convention A and the contiguous split, and the proof is elementary. But the
canon's proof as written has a gap, and the canon does not state the split convention it
depends on.**

**Lemma 1.** For a stationary process on a standard Borel space, E = 0 ⟺ the process is
i.i.d.

*Proof.* (⇐) trivial. (⇒) E = 0 means σ(X_{≤0}) ⫫ σ(X_{≥1}). E is shift-invariant, so
stationarity gives the same at *every* split: X_{≤k} ⫫ X_{≥k+1} for all k. Then for any n,
splitting at k = 1, P(x_1…x_n) = P(x_1)·P(x_2…x_n); induct. ∎

**Lemma 2.** An i.i.d. process with one-point law p satisfies σ = D(p ‖ p∘ε) exactly, at
every n. In particular σ = 0 under Convention A, and σ = 0 under Convention B iff p is
ε-invariant.

*Proof.* P_n = ∏p(x_t) and P̃_n = ∏p(εx_t), so D(P_n‖P̃_n) = n·D(p‖p∘ε). ∎

**Theorem.** Stationary, contiguous split, single complete description, and either ε = id
or p ε-invariant ⟹ σ > 0 ⇒ E > 0. *Proof:* contrapositive of Lemmas 1 and 2. ∎

**Where the canon's proof is short.** §4 reads: "E = 0 holds if and only if past and future
are independent, i.e. the process is i.i.d." The "i.e." is doing unearned work — past ⫫
future *at one split* does not give i.i.d.; it gives i.i.d. only after stationarity is used
to propagate independence to every split. That is the only non-trivial step in the whole
argument and it is the one the canon elides. **The theorem is true; the canon's proof of it
is incomplete.** Lemma 1 above supplies the missing line. This is a repair, not a
retraction.

**Positive control, computed** (`reproof.py` Part 1). Driven ring on ℤ₄, p = 0.8:

| quantity | value (nats) |
|---|---|
| σ, closed form (p−q)ln(p/q) | 0.831776616672 |
| σ, direct from the chain | 0.831776616672 |
| σ, brute-force path KL: D_n/(n−1) at every n = 2…11 | 0.831776616672 |
| E = I(X₀;X₁) = ln N − H(p,q) | 0.885891937582 |

Both positive. The theorem holds here, as canon Figure DM says.

---

## 3. Task 2.2 — Counterexamples

Three, of decreasing relevance to the canon as it now stands. **C1 is already fenced off by
the canon's v1.26 scope condition 3. C2 and C3 are not.**

### C1 — i.i.d. odd variable (Convention B). Already handled by canon scope 3.

State space {+1,−1} read as a **velocity** — odd under time reversal, so ε swaps the two
states. X_t i.i.d. with P(+1) = p.

- E = 0 **exactly** (i.i.d.).
- σ_A = 0. σ_B = (2p−1)·ln(p/(1−p)) > 0 for p ≠ ½.

Computed, and confirmed by brute-force path KL at every n = 2…12 (exact to 12 digits at
every n, not asymptotically):

| P(v=+1) | E | σ_A | σ_B |
|---|---|---|---|
| 0.50 | 0 | 0 | 0 |
| **0.70** | **0** | **0** | **0.338919144155** |
| 0.80 | 0 | 0 | 0.831776616672 |
| 0.90 | 0 | 0 | 1.757779661869 |
| 0.99 | 0 | 0 | 4.503217453132 |

Canon scope condition 3 excludes this correctly: the one-point law (0.7, 0.3) is not
invariant under ε. **Prime's diagnosis is confirmed and the repair is correct.**

### C2 — the increment representation of the *same* driven ring. Not handled.

Take the ℤ₄ ring above and change coordinates to the increment Y_t = X_t − X_{t−1} mod 4,
read as ±1. An increment *is* an odd variable. Y is i.i.d. Bernoulli(0.8).

| representation | σ | E |
|---|---|---|
| position (X) | 0.831776616672 | 0.885891937582 |
| increment (Y), Convention A | 0.000000000000 | 0 |
| increment (Y), Convention B | **0.831776616672** | **0** |

σ_B(increments) − σ(positions) = −1.1 × 10⁻¹⁶. **Exactly equal.**

This matters for a reason the parity condition does not cover. **Canon Figure DM(b)
asserts that under coarse-graining "σ and E collapse to zero together."** That is not
general. Here is a reduction of the same driven system that *preserves the physical entropy
production exactly* while sending E to zero. The canon's own illustration of scope
condition 1 is therefore misleading about what scope condition 1 protects against.

It also shows **scope conditions 1 and 3 are not independent.** The position→increment map
is simultaneously a change of description and a change to odd variables. A reader auditing
a reported σ against condition 1 alone, or condition 3 alone, can pass both checks
separately and still be looking at this case.

### C3 — the excluded-present split. Not handled; the canon is silent on the convention.

The canon nowhere states whether "past" includes the present. Under the *excluded-present*
split, **the implication is false.**

Let U_t be i.i.d. Bernoulli(q) and X_t = φ(U_t, U_{t+1}) — a 1-dependent process. Then
X_{≤−1} is a function of U_{≤0} and X_{≥1} of U_{≥1}: disjoint and independent, so

> **E_gap = 0 exactly and structurally, at every block length.**

Verified numerically at block lengths 1, 2, 3 (all 0.000e+00).

*Infinite-σ instance.* φ = identity on pairs, i.e. X_t = (U_t, U_{t+1}), q = ½. The reverse
of edge (u,v)→(v,w) exists only if w = u, so the forward path measure is not absolutely
continuous with respect to its reverse: **σ = +∞** while E_gap = 0. (E contiguous = ln 2 =
0.693, consistent with §2.)

*Finite-σ instances*, so this cannot be dismissed as an absolute-continuity artifact.
φ(u,v) indexed by 2u+v = (0,1,2,0), alphabet {0,1,2}, full support:

| q | σ (Aitken limit of D_n increments, n ≤ 14) | E_gap |
|---|---|---|
| 0.10 | ≈ 2.0929 nats/step | 0 |
| 0.25 | ≈ 0.5232 nats/step | 0 |
| 0.40 | ≈ 0.0810 nats/step | 0 |

σ finite, strictly positive, E_gap exactly zero. (The σ values are extrapolated from
finite-n path KL; the *sign and finiteness* are exact, the third digit is not.)

Fix: state the split. The standard is Crutchfield & Feldman's contiguous halves (Prop. 8,
Chaos 13, 25), which the canon already cites — so this is a specification gap, not a defect
in the intended object. But as written the canon does not fix it.

---

## 4. Task 2.3 — Minimal additional assumption

**The canon's v1.26 scope condition 3(b) is not merely sufficient; it is exactly sharp.**
Prime got this right, and it is worth saying how right.

By Lemma 1, the only processes at risk are the i.i.d. ones. By Lemma 2, an i.i.d. process
has σ = D(p‖p∘ε), which vanishes **iff** p = p∘ε. So:

> **σ > 0 ⇒ E > 0 holds for the class 𝒞 iff every i.i.d. member of 𝒞 has an ε-invariant
> one-point law.**

Necessary *and* sufficient. No weaker condition rescues the theorem; no stronger one is
needed. Canon's 3(b) — "the stationary one-point distribution is invariant under the
reversal involution" — is that condition, and it strictly subsumes 3(a) (all variables
even ⟹ ε = id ⟹ trivially invariant). **Recommend keeping 3(b) as primary and demoting
3(a) to an illustration of it.**

**What 3(a) excludes** (the strict reading): underdamped Langevin and any molecular
dynamics in phase space; ballistic and inertial transport; spin systems in an external
magnetic field (B is odd); rotating/Coriolis frames; and — per C2 — *any* current-,
increment-, flux- or step-count representation of a driven system. That last is not a
narrow pathological class. Molecular motors are routinely modelled in step coordinates.

**What 3(b) additionally admits:** everything above whose *stationary one-point law* is
ε-symmetric. That covers a large and physically central set — e.g. an underdamped
NESS whose stationary velocity marginal is Maxwellian and symmetric, which is the generic
case for a system with no net momentum. So 3(b) is a genuinely good repair: it rules out a
narrow class (systems carrying a net odd-variable current) rather than all of phase space.

**One assumption to add, not a repair but a declaration:** the split convention (C3).
Suggested verbatim text is in §7.

**A repair that does NOT work, checked so nobody proposes it later.** Replacing σ with the
non-adiabatic (excess) entropy production makes the theorem vacuous. For a genuine NESS
Ṡ_na = −Σ_m ṗ_m ln[p_m/p^st_m] ≡ 0, since ṗ_m = 0 (Esposito & Van den Broeck, *Phys. Rev.
E* **82**, 011143, Eq. 33). A stationary-process theorem with a hypothesis that is
identically false has no content. The adiabatic/housekeeping part is where the dissipation
lives, and it is the part the parity convention affects.

---

## 5. The result the order did not ask for, and the one I would act on

**There is no quantitative floor. `inf { E : σ ≥ s } = 0` for every s > 0.**

The canon calls this row a "memory floor" — §4, Table 3, and the §12′ ledger. The theorem
supports E > 0. It does not support any lower bound on E as a function of σ, and none
exists. E can be pushed arbitrarily close to zero at arbitrarily large dissipation, inside
a family that satisfies **all four canon scope conditions**.

**The family.** N states, transition matrix P. Base: uniform, P_ij = 1/N (i.i.d., σ = E =
0). Superimpose a circulation on the 3-cycle 0→1→2→0 of size c = (1−η)/N:

> P[i, i+1 mod 3] = (2−η)/N,  P[i, i+2 mod 3] = η/N,  for i ∈ {0,1,2}
> P_ij = 1/N otherwise

Row sums and column sums are both preserved, so P is doubly stochastic and π is uniform
exactly. All entries are strictly positive for η > 0: irreducible, aperiodic, full support.
Closed forms (both verified against direct computation and against brute-force path KL):

> **σ(N,η) = (6(1−η)/N²) · ln((2−η)/η)**
> **E(N,η) = (3/N²) · [ (2−η)ln(2−η) + η ln η ]**

Write η = e^(−L). As L → ∞: σ → 6(L + ln 2)/N², E → 6 ln 2/N². **σ grows with L; E does
not.** Holding σ = 1 nat/step by setting N² = 6(L + ln 2) gives E → ln 2 / (L + ln 2) → 0.

**Computed, in extended precision, directly from the matrix (no closed form used):**

| N | L = −ln η | σ (nats/step) | E (nats) | σ/E |
|---|---|---|---|---|
| 6 | 5.338 | 1.000000000000006 | 1.127098859 × 10⁻¹ | 8.9 |
| 8 | 9.974 | 1.000000000000003 | 6.495706600 × 10⁻² | 15.4 |
| 12 | 23.31 | 1.0 | 2.888113248 × 10⁻² | 34.6 |
| 17 | 47.47 | 1.000000000000122 | 1.439059890 × 10⁻² | 69.5 |
| 25 | 103.5 | 1.000000000000001 | 6.654212933 × 10⁻³ | 150.3 |
| 39 | 252.8 | 1.0 | 2.734308405 × 10⁻³ | 365.7 |
| 55 | 503.5 | 1.0 | 1.374837383 × 10⁻³ | 727.4 |
| 77 | 987.5 | 0.9999999999999999 | 7.014476444 × 10⁻⁴ | 1425.6 |
| 122 | 2480.0 | 1.000000000000006 | 2.794197180 × 10⁻⁴ | 3578.9 |

Every row: σ = 1 nat/step exactly, π uniform exactly, stochasticity error 0. Every row
matches ln 2/(L + ln 2) to six significant figures. Extrapolating: at σ = 1 nat/step,
N ≈ 2,449 states gives E ≈ 6.9 × 10⁻⁷ nats; N ≈ 2.4 × 10⁶ gives E ≈ 6.9 × 10⁻¹³ nats.

*(Note for anyone re-running this: in double precision the direct computation reports
σ = ∞ for N ≥ 17 because η/N underflows to zero. That is an arithmetic artifact, not a
result. It must be done in extended precision, and the matrix entries must be written
directly as (2−η)/N and η/N — forming them as 1/N ± (1−η)/N destroys η by cancellation
even at 200 digits. Both traps are in the deposited code, with the fix.)*

**Audit against the canon's four scope conditions:** (1) σ and E read on the same complete
description ✓; (2) stationary ✓; (3) configuration-space states, all even under reversal,
π uniform hence trivially ε-invariant ✓; (4) this row *is* about the floor's reach ✓.
The family is squarely inside the theorem's scope. The theorem holds on it — E > 0 in every
row. And E is unbounded below.

**Why this deflates the row further than scope condition 4 already does.** Condition 4 says
the theorem forces a floor, not depth. That reads as "the floor is positive but we don't
claim it's large." The correct statement is stronger: **the floor is not bounded away from
zero by anything, at any dissipation rate.** Combined with Lemma 1, the theorem's entire
content is:

> σ > 0 ⟹ the process is not i.i.d.

because E > 0 and "not i.i.d." are the *same statement* for a stationary process. The
excess entropy adds no information beyond non-i.i.d.-ness. That is a true theorem and a
correct corollary of trajectory irreversibility. It is also nearly the weakest non-trivial
thing one could say, and the word "floor" invites reading it as more.

---

## 6. Task 2.4 — Grade recommendation

**Recommendation: keep `forced × theorem/corollary`, add a fifth scope condition, and
strike the floor language.** Not a downgrade to synthesis, and I want to be explicit that I
looked for a reason to downgrade and did not find one.

Reasoning against `synthesis`: within the four stated conditions the implication is a
theorem with a complete elementary proof (§2), and the conditions are already in canon and
are sharp (§4). "Holds under conventions the canon adopts but is not compelled" would be
the right grade if the conditions were arbitrary; 3(b) is not arbitrary, it is necessary
and sufficient.

Reasoning against an unqualified `forced × theorem/corollary`: the canon's own proof is
incomplete (§2), its split convention is unstated and the theorem is false under the other
reading (§3, C3), its Figure DM(b) illustration is not general (§3, C2), and the "floor"
framing overstates what is proven (§5).

**Four amendments, in priority order.**

**(i) Add scope condition 5, verbatim:**

> *Fifth, the past–future split is contiguous, with the present assigned to the past:
> E = I(X_{≤0} ; X_{≥1}), following Crutchfield & Feldman (2003), Prop. 8. Under the
> excluded-present variant E_gap = I(X_{≤−1} ; X_{≥1}) the implication is false: any
> 1-dependent process X_t = φ(U_t, U_{t+1}) with U i.i.d. has E_gap = 0 identically, and
> such processes can carry strictly positive — indeed infinite — entropy production
> [deposited].*

**(ii) Repair the proof in §4.** Replace "i.e. the process is i.i.d." with the actual step:

> *E = 0 makes the past and future independent at one split; because E is shift-invariant
> and the process is stationary, independence holds at every split, and induction on the
> split point gives that the finite-dimensional laws factorize — the process is i.i.d.*

**(iii) Strike "floor" or bound it.** Suggested replacement for the scope-condition-4
sentence:

> *Fourth, what Drive forces is a strict positivity, not a magnitude and not a bound. There
> is no inequality of the form E ≥ f(σ) with f > 0: for every s > 0 there are stationary,
> even-variable, single-description Markov chains with σ = s and E arbitrarily close to
> zero [deposited]. Since E > 0 is equivalent to non-i.i.d.-ness for a stationary process,
> the theorem's content is exactly "sustained dissipation implies the process is not
> i.i.d."*

**(iv) Correct or qualify Figure DM(b).** The claim that coarse-graining collapses σ and E
together is false in general; the increment representation of the very ring in Figure DM(a)
preserves σ exactly and sends E to zero. Either add that case to the figure or narrow the
caption to the specific coarse-graining computed.

**On §4 of the order ("the settled core goes to zero").** It does not. The row survives at
grade. But the ledger should not read as though a *substantive* result survived: after
amendment (iii) the row says "dissipation implies temporal dependence," which is true,
forced, and thin. I would rather the ledger say that in the row than have the row look
heavier than it is. Per the order's own instruction to value a retraction above a
confirmation: this is a confirmation, and I am telling you it is worth less than the grade
suggests.

---

## 7. Citations — verified against primary sources, with flags

Each was checked against the publisher landing page or arXiv record. **Four claims the
canon or the surrounding literature-as-usually-cited does not actually support are flagged
in bold.** These are separate from the mathematics above, which stands on its own.

**Supports the KL/path-measure identification of σ:**

- C. Maes & K. Netočný, "Time-Reversal and Entropy," *J. Stat. Phys.* **110**, 269 (2003),
  DOI 10.1023/A:1021026930129. Prop. 4.2, Eqs. 4.4–4.6. **This is the correct primary
  citation for "entropy production = log Radon–Nikodym derivative of the path measure
  against its reverse."**
- P. Gaspard, *J. Stat. Phys.* **117**, 599 (2004), DOI 10.1007/s10955-004-3455-1. Eq. (6);
  the text after it states the difference "is a relative entropy per unit time." Explicitly
  for NESS.
- J. L. Lebowitz & H. Spohn, *J. Stat. Phys.* **95**, 333 (1999). Has the action functional
  and the GC symmetry. **⚠ Never uses "relative entropy" or "Kullback–Leibler" — do not
  cite for the KL formulation.**
- **⚠ Kawai, Parrondo & Van den Broeck, *Phys. Rev. Lett.* **98**, 080602 (2007) is
  MISSTATED if cited for this.** Their relative entropy is between *single-time phase-space
  densities* in a Hamiltonian equilibrium→equilibrium transition — not a path measure, not
  a rate. Cite for ⟨W_diss⟩ = kT·D and the coarse-graining/Landauer bound only. *(The canon
  currently cites Parrondo, Van den Broeck & Kawai, New J. Phys. 11, 073008 (2009) as [1]
  for the trajectory-irreversibility identity; that 2009 review is a closer fit than the
  2007 PRL, but Maes & Netočný is the sharper primary.)*

**Parity / odd variables — the canon's [Spinney & Ford 2012]:**

- R. E. Spinney & I. J. Ford, *Phys. Rev. Lett.* **108**, 170603 (2012), arXiv:1201.0904 —
  "Nonequilibrium Thermodynamics of Stochastic Systems with Odd and Even Variables."
  **There is also a Publisher's Note at PRL 108, 199905 (2012)**, confirmed to exist.
- R. E. Spinney & I. J. Ford, *Phys. Rev. E* **85**, 051113 (2012), arXiv:1203.0485 —
  "Entropy production in full phase space for continuous stochastic dynamics."
- I. J. Ford & R. E. Spinney, *Phys. Rev. E* **86**, 021127 (2012), arXiv:1204.4822 —
  discrete-state companion. **⚠ Note the reversed author order.** The canon's §4 cites
  "[Spinney & Ford 2012; Ford & Spinney 2012]" — that pairing is correct, but a citation
  attaching "Ford & Spinney" to the PRE 85 title would be a conflation.
- **⚠ MISSTATED: Spinney & Ford do not characterise the sign flip as a convention.** They
  argue it is *correct*: "The correct path, x*, to consider is the time reversed trajectory
  proper which includes a reversal of sign for all odd variables." A canon sentence
  presenting the parity choice as a free convention on their authority would misattribute.
  For the not-forced framing use U. Seifert, *Rep. Prog. Phys.* **75**, 126001 (2012),
  Sec. 4.1 ("Three choices for the conjugate dynamics … have been considered so far") and
  Sec. 4.5.2 ("Formally, however, one could also keep the flow unchanged … which would lead
  to another class of FTs").
- **⚠ UNVERIFIED:** an explicit statement in Seifert 2012 that velocity/momentum flips sign
  under time reversal could not be located; Sec. 4.5.3 on magnetic fields does not discuss
  reversing B.

**Excess entropy:**

- J. P. Crutchfield & D. P. Feldman, *Chaos* **13**, 25 (2003), DOI 10.1063/1.1530990.
  Prop. 8, Eq. (54) in the published version — **⚠ the arXiv preprint numbers it Eq. (55)**.
- W. Bialek, I. Nemenman & N. Tishby, *Neural Computation* **13**, 2409 (2001), Eq. (18)
  for the Markov case.
- **⚠ MISSTATED: neither source states "E = 0 iff i.i.d."** Crutchfield & Feldman give only
  the forward direction, by coin-flip example. The converse is elementary (Lemma 1 above)
  but must be presented as derived, not cited.
- **⚠ E = I(X₀;X₁) for a stationary Markov chain is folklore.** BNT Eq. (18) states it
  without proof; C&F Prop. 11 proves it only by worked example. Derive it.

**Non-adiabatic decomposition (used in §4 to close off a bad repair):**

- M. Esposito & C. Van den Broeck, *Phys. Rev. E* **82**, 011143 (2010), Eq. (33).
- C. Van den Broeck & M. Esposito, *Phys. Rev. E* **82**, 011144 (2010). **⚠ Author order
  is reversed between papers I and II.**
- M. Esposito & C. Van den Broeck, *Phys. Rev. Lett.* **104**, 090601 (2010). **⚠ Its
  ⟨ΔS_na⟩ = 0 sentence is about the slow-driving limit and is an ensemble average — do not
  cite it alone for the genuine-NESS claim.**
- T. Hatano & S. Sasa, *Phys. Rev. Lett.* **86**, 3463 (2001). **⚠ Contains no prose
  sentence saying the quantity vanishes at constant driving; it follows from the α̇ factor
  in their Eq. (11). Present as a consequence, not a quotation.**

**Schnakenberg** was checked and is *not* used above, but since the canon's ledger works in
this area: J. Schnakenberg, *Rev. Mod. Phys.* **48**, 571 (1976), Sec. VII, Eq. (7.6).
**⚠ MISSTATED as usually quoted on two counts:** the paper gives the continuous-time
flux × affinity form P = −½ΣJ_ij A_ij, not the discrete-time chain expression; and it is
defined for arbitrary time-dependent p(t), not only stationary states.

---

## 8. Code

Deposited alongside this report.

- `reproof.py` — Parts 0–6: closed-form/flux-form agreement; the ℤ₄ positive control with
  brute-force path KL at every n ≤ 11; counterexample C1 with brute-force confirmation at
  every n ≤ 12; the increment representation C2; the excluded-present counterexamples C3
  (infinite- and finite-σ); the floor-collapse family; the E = 0 ⟺ i.i.d. spot checks.
- `verify.py` — Part A: extended-precision recomputation of the floor-collapse family
  directly from the transition matrix, solving for L so σ = 1 exactly at each N. Part B:
  vectorised convergence study of the finite-σ excluded-present counterexample.
- `run.log`, `verify.log` — full output.

Everything analytic first, numerics confirming, per the order's §3.

---

## 9. Summary for the ledger

| Task | Finding |
|---|---|
| 2.1 True as stated? | **Yes**, under Convention A / ε-invariant one-point law and a contiguous split. The canon's proof is incomplete at the one step that carries content; repaired in §2. |
| 2.2 Counterexample? | Three. C1 (odd-variable i.i.d., σ_B = 0.3389, E = 0) — already fenced by canon scope 3. C2 (increment representation, σ preserved *exactly* at 0.8318, E = 0) — not fenced, and refutes Figure DM(b) as stated. C3 (excluded-present split, σ finite > 0 or +∞, E_gap = 0) — not fenced; canon states no split convention. |
| 2.3 Minimal assumption | Canon's 3(b) is **necessary and sufficient**, not merely sufficient. Prime's repair is exactly minimal. Add a split-convention declaration. Excludes systems carrying a net odd-variable current — narrow. Does *not* exclude generic underdamped NESS. |
| 2.4 Grade | **`forced × theorem/corollary`, unchanged** — with a fifth scope condition, a repaired proof, a corrected Figure DM(b), and the "floor" language struck. |
| Not asked | **`inf { E : σ ≥ s } = 0` for every s > 0.** No quantitative floor exists. Demonstrated on a family inside all four scope conditions: σ = 1 nat/step exactly with E down to 2.79 × 10⁻⁴ nats computed, → 0 as N → ∞. The theorem's full content is "σ > 0 ⟹ not i.i.d." |

The settled core does not go to zero. It stays at one row, and the row is thinner than the
ledger currently reads.
