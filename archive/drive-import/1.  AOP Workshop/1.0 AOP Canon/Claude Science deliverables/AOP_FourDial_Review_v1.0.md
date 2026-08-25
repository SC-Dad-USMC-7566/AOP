# Review — AOP Four-Dial Testbed v0.1

**Reviewer:** Claude Science (BUILDER seat, acting as reviewer of an artifact it did not build)
**Date:** 2026-08-07
**Object under review:** `AOP_FourDial_Testbed_v0_1_20260806` (Drive folder `1Y_rKygNKDOcahRbfNe25Gd4S60vnQpcP`), 13 files
**Grounding:** `AOP_CANON_MASTER_v1.27.md` (sha256 `99f64ecc…00aff`; masthead reads v1.26), `AOP_Charter_v1_2.md`, `REV_AOP_BDMI_Operational_Definition_Specification_v0_1_20260804.md`
**Status:** noncanonical review of a noncanonical artifact

---

## Startup check — 2026-08-07

- [x] AOP Charter — v1.2 (Drive id `1S8BsrGHQgp1-pG6V6bfUUSuglRX3Z1-S`)
- [x] AOP Canon (the paper) — file `AOP_CANON_MASTER_v1.27.md`, body masthead v1.26 (the known filename/body mismatch; carried, not silently resolved)
- [ ] AOP → Ladder bridge memo — not read; this task does not touch the Ladder connection
- Drive connector: on.

---

## 0. Verdict

The code is clean, well-organized, deterministic, and reproduces bit-for-bit. **That is the problem.**
It is a correct implementation of a construction that cannot fail, and it reports the outputs of that
construction as if they were findings. Nine of nine preregistered checks pass, and at least four of
the nine are analytically incapable of failing.

The design document is unusually honest about this in §6 ("The diagonal calibration is deliberately
easy"; "The persistence coupling is stipulated"). But the executive summary and the results file are
not: they present "maximum dial-recovery error 1.67×10⁻¹⁶" and "summing the three single-ablation
effects overcounts by exactly 3×" as the payoff. Neither is a measurement. The first is floating-point
noise in a round-trip through a bijection; the second is the integer 3.

**Three findings are load-bearing for the science and should block promotion of any result from this
rig:** (S1) the Drive axis is given a persistence sign that contradicts the canon's own established
one-sided gate; (S2) "zero cross-talk" is a property of the code's call graph, not of the axes, and
the canon's actual Memory quantity cross-loads with Drive by 3,291× on this very rig; (S3) the
acceptance suite misses 4 of 7 seeded scientific defects.

Reproduction: `python3 -m four_dial` → 9/9 checks, 625 rows, md5 identical to all three delivered
result files. Test suite: 8/8 pass. Nothing here is a reproducibility complaint.

---

## 1. Science findings

### S1 — The Drive axis is given the wrong persistence sign, against the canon's own established result

**This is the most serious finding.** The rig routes rotor current into the repair rate,
`μ = c · J(D) · M · I`, so raising Drive lengthens the persister's lifetime — MFPT rises 4.5×
from D=0 to D=1 (4.98 → 22.53). The canon's §12 status table contains an entry that points the
other way, graded **GO (established within model)**:

> for a measure-preserving current (divergence-free, at fixed stationary distribution, with ∇U·ℓ = 0)
> in the small-noise limit the sign is not free but **one-sided**: circulation can only shorten or
> leave unchanged the mean first-passage time, never lengthen it.

The canon backs this with a cited non-reversible Eyring–Kramers analysis (Lee & Seo 2021, Lemma 3.4
& Cor. 3.9; Bouchet & Reygner 2016), a 2D double-well confirmation, and an on-ring 5.7× lifetime
*fall*.

I checked whether the rig's rotor is inside that gate's scope class, and it is: its stationary
distribution is uniform and invariant in D to 3×10⁻¹⁶ (verified across D ∈ [0,1] at 101 points),
which is exactly "divergence-free circulation at fixed stationary distribution."

The rig does not contradict the theorem — the theorem constrains first-passage time on the *rotor's
own* state space, and the rig instead makes rotor current an input to a *separate* two-state health
chain, where nothing forbids a positive sign. But that is precisely the problem: the rig has taken
the one axis where AOP has an established directional result and stipulated the opposite direction
by construction, without noting the tension, and without stating the coupling that would be required
to physically justify current-as-repair-fuel. The design document's §6.3 says favorable signs are
"regime-specific" — true, but insufficient. This is not a neutral regime choice; it is the reverse
of the canon's settled direction on the same axis.

*What is required:* either (a) state the scope difference explicitly and justify why rotor current
may be spent as repair capacity without reshaping the health chain's stationary state, or (b) run
the Drive dial in a configuration where the canon's gate binds, and confirm the rig recovers the
downward sign. Option (b) is the real test, and it is the one the rig currently cannot pass because
its repair law forecloses it. Note also §12's warning about the star: "out-of-scope is not a positive
result." The same applies here.

### S2 — "Zero structural cross-talk" is a property of the code, not of the axes

`CAL.structural_selectivity` reports `max_off_target_structural_range = 0` exactly. This is not an
empirical finding about B/D/M/I. Inspect the signatures: `boundary_profile(b, p_E)`,
`memory_profile(m, lags)`, `integration_profile(i)` — **no module function can see any dial but its
own.** Zero off-target range is therefore forced by Python's call graph. The check cannot fail; it
has no power whatsoever. The design document concedes this in §6.1, but the results file still lists
it as a passed acceptance check alongside checks that could in principle fail, which misleads a
reader scanning the table.

Worse, the claim is false for the canon's own Memory quantity. The canon's Table 1 defines
Memory as **excess entropy E = I(past; future)** of the declared process. The rig's declared system
state S is the product of interface bit, rotor, memory chain, and the A|B pair — so E(S) is additive
across those components. Computing E on the rig's own rotor at the rig's own grain δt = 1:

| D | rotor E (bits) |
|---|---:|
| 0.00 | 3.52×10⁻³ |
| 0.25 | 2.35×10⁻³ |
| 0.50 | 6.12×10⁻⁴ |
| 0.75 | 5.28×10⁻⁵ |
| 1.00 | 1.07×10⁻⁶ |

Drive moves the canon's Memory axis by a factor of **3,291** across the dial range — and it moves
it *downward* while σ rises from 0 to 12.78. Integration cross-loads too: the A|B pair contributes
E = 0 → 1 bit as I goes 0 → 1. Grouping the 625 grid cells by dial, as `evaluation.py` does, the
within-level range of E(S) is **2.00 bits on the D axis and 1.00 bit on the I axis** — not zero.

The rig gets zero only because it substitutes **AIS at lag 1 of one submodule** for the canon's E of
the declared system. That substitution is what manufactures the diagonal. So the headline calibration
result inverts: read with the canon's own quantities, this rig is a demonstration that the four axes
**do** cross-load, on the very construction built to show they separate cleanly. That is a more
interesting result than the one reported, and it should be reported.

### S3 — Four claimed structural readouts are not the canon's, and one contradicts §8

Mapping the rig's readouts onto the canon and the operational spec:

| Axis | Canon / spec requires | Rig reports | Assessment |
|---|---|---|---|
| B | panel B1/B2/B4 (contrast, screening residual I(in;out\|F), maintenance burden) | response ratio `1 − r_intact/r_open` | This is the spec's **B-S** (shielding), which is legitimate — but the spec §2.3 makes contrast+shielding a **mandatory pair**, and B-C here is a JSD *against the open interface*, i.e. a second shielding measure, not an independent contrast. B4 maintenance burden absent entirely. |
| D | σ under a declared reversal convention R | σ = (k₊−k₋)·a | Correct, and R is declared. The one axis the rig gets right. |
| M | E = I(past;future) | AIS at lag 1 | Substitution, unflagged. Drives S2. |
| I | TC across a component partition (canon default) | lagged MI, labelled `lagged_total_correlation_bits` | The canon's default TC on this module is **0.000 at every I level** — A_t and B_t are marginally independent; only the *lagged* pair is dependent. Calling a lagged MI "total correlation" is a mislabel of the canon's named default proxy. |

The Boundary case additionally collides with canon §8. There, `B2 = I(X_in;X_out|F) → 0` is what
distinguishes a cut *sealed by an interface* from one merely *coupled across*. On the rig's boundary
module, B2 = 1−B exactly: at B = 0.6 the interface reads B2 = 0.4 bits, i.e. **unsealed** — and not
because anything bypasses it, but because the rig's "interface" is a stochastic gate that transmits
the exterior bit verbatim 40% of the time. There is no interface *mediating* anything; there is a
coin flip choosing between transparent and opaque. That is a defensible model of a leaky barrier,
but it is not a declared interface F in the canon's sense, and the declaration tuple's F slot
("probabilistic interface gate") papers over the difference.

### S4 — The "3× overcount" is the integer 3, not a finding

Reported as "the central payoff": ΔV for D, M, I are each 0.309279, summing to 0.927838 = 3× the
joint effect. But `μ = c·J(D)·M·I` is a product, so zeroing *any single factor* sets μ = 0 exactly.
All three single-ablations are therefore **the identical intervention** — the same μ = 0 chain — and
the sum of n copies of one number divided by that number is n. I confirmed the overcount factor
equals the number of multiplicative factors, exactly, for n = 2…6 (Fig. 1b).

The methodological point the rig wants to make — serially necessary mechanisms must not be priced
as additive currencies — is correct and is already canon (§3: "Allocation summaries … are reported
only where additivity is separately justified"). But this rig does not *test* it, it *instantiates*
it. The acceptance threshold `minimum_series_overcount_factor: 2.5` reads as an empirical bar; it is
satisfied by construction the moment three factors are multiplied. Preregistering a threshold on a
quantity you have algebraically fixed is not preregistration.

### S5 — The coalition layer reports cut sets while no cut set exists

`minimal_repair_cut_sets: [["D"],["M"],["I"]]` is hardcoded, and the canon defines a **minimal
failure cut set** as a set of mechanisms whose joint removal *ends viability*. On this rig, zeroing
all four dials gives λ = 0.7, μ = 0 → V = 0.0595, and the minimum V anywhere on the 625-cell grid is
**0.0595 > 0**. No intervention, singly or in any coalition, ends viability. The rig has no failure
cut set at all; what it has are sets that reduce V. Likewise `minimal_viability_preserving_sets` —
the canon's other named coalition object — is never computed.

### S6 — The persistence layer has 2 degrees of freedom, not 4

V is a function of exactly two scalars, (λ, μ). Across the 625-cell grid there are 5 distinct λ,
37 distinct μ, and **185 distinct V values**; 305 of 625 cells (49%) share the single μ = 0
no-repair regime. The "5×5×5×5 factorial" is a factorial design over the *structural* layer only.
Presenting 625 configurations as the persistence evidence base overstates it by roughly 3.4×.
M and I enter V *only* through the product M·I and are formally indistinguishable there: swapping
(M, I) = (0.7, 0.8) for (0.8, 0.7) leaves every persistence quantity identical. Two of the four
axes are not separately identifiable in the persistence chamber.

### S7 — The identification trichotomy is not implemented

The operational spec's Priority 5 is explicit: "Use PRESENT / ABSENT / UNDETERMINED. An unavailable,
invalid, nonstationary, noncommensurable, or underpowered measurement is never scored as zero."
The rig's verdict logic is `"ABSENT" if dial == 0.0 else "PRESENT"` on all four axes. **UNDETERMINED
appears nowhere in the executable code** — it occurs once in the whole repo, in a design-document
sentence recommending it. The verdict is read off the knob position, which is exactly the failure
mode §8.4 of the design document names as the joke to preserve.

Two specific consequences. (i) `o_information: None` is handled well — genuine missingness, correctly
badged. Good. (ii) `predictive_state_complexity_bits = 0.0 if m == 0.0 else 1.0` is a hardcoded
two-valued literal, not a computed Cμ. The canon is emphatic (§4) that Cμ is a property of a declared
observation process and that reading it off structure is "a category error." A constant 1.0 is not a
measured Cμ, and it should be `None` with a missingness note, or removed.

### S8 — σ > 0 with E ≈ 0 sits uncomfortably close to the canon's forced edge

The canon's one **forced** coupling is D→M: σ > 0 ⇒ E > 0. On the rig, 100 of 625 grid cells have
σ > 0 with the reported Memory readout exactly 0.0 (M dial = 0). Read on the rig's own submodule
metric this looks like a violation of the framework's only theorem.

It is not an actual violation — computed properly on the declared product state S, E > 0 everywhere
(minimum 2.65×10⁻⁴ bits at D = 0.6, M = 0; 1.07×10⁻⁶ at D = 1, M = 0), because the driven rotor
itself carries positive excess entropy. The theorem holds. But the rig's own reported numbers appear
to falsify the framework's only forced edge in 16% of its grid, and neither the results file nor the
design document notices. A rig that cannot see its parent framework's one theorem being satisfied is
not instrumented to test it — and the near-violation is instructive: E(S) is driven to 10⁻⁶ bits,
which is exactly the canon's fourth scope condition ("there is no inequality of the form E ≥ f(σ)
with f > 0"). The rig accidentally illustrates the canon's own tightness result and reports it as
nothing.

---

## 2. Method / instrument findings

### M1 — The acceptance suite misses 4 of 7 seeded scientific defects

I mutated the model to inject defects that change reported science, then re-ran all nine checks:

| Seeded defect | Changes reported science | Caught? |
|---|---|---|
| Entropy production halved (wrong EPR) | σ 3.695 → 1.848 | **MISSED** |
| AIS read at lag 2 instead of lag 1 | AIS 0.390 → 0.181 | **MISSED** |
| Survival horizon 50 instead of declared τ=5 | V 0.704 → 0.022 | **MISSED** |
| Generator transposed in the survival solve | V 0.704 → 0.982 | **MISSED** |
| Repair law additive instead of multiplicative | breaks serial-chain claim | caught |
| Boundary attenuation sense inverted | monotonicity flips | caught |
| I causal effect := statistical MI (conflation) | breaks recovery | caught |

**Detection rate 3/7.** The mechanism of failure is structural: `CAL.dial_recovery` inverts *the same
function* it validates (`_invert_monotone` calls `drive_profile` to invert `drive_profile`). Any
monotone distortion of a readout cancels exactly in the round trip. A bijection composed with its own
numerical inverse is the identity regardless of whether the bijection is the physically correct one.
This is why max recovery error is 1.67×10⁻¹⁶: it measures bisection convergence, nothing else.

Note further that B and I "recovery" is not even a numerical inversion — `recovered_B` is
`boundary["shielding"]`, which *is* B, and `recovered_I` is `integration["cross_part_causal_effect"]`,
which *is* I. Both are literal identity assignments; I confirmed `recovered == dial` bit-exactly for
all 625 rows, with per-axis error B = 0, D = 0, I = 0 and only M nonzero. Three of the four axes
contribute *nothing* to the headline calibration number.

*Required fix:* the design document's own Priority 1 (blind the estimators on finite trajectories) is
the right answer, and until it is done, no calibration claim from this rig should be quoted.

### M2 — Uniformization silently returns 0 for large ν·t

`transient_survival` opens with `weight = exp(-x)`, `x = ν·h`. For x ≳ 745 this underflows to 0.0 in
IEEE double, and the whole series is then identically zero — the function returns a confident 0.0
survival with no warning. Measured threshold: at ν·t = 745 the code returns 5.09×10⁻¹⁴ against an
exact 2.91×10⁻¹⁴ (already wrong by 75%); at ν·t = 750 it returns exactly 0.0 against 2.36×10⁻¹⁴.
At the frozen operating point ν·t ≈ 9.2, so **v0.1's published numbers are unaffected** — I verified
survival against a `scipy.linalg.expm` solve, agreement 6.7×10⁻¹⁶. But this is a live trap for any
longer-horizon or stiffer follow-on, and it returns a *confident wrong zero*, which is the exact
failure mode the rig is built to warn against. Fix: log-domain accumulation, or scaling-and-squaring
via `expm`.

### M3 — No guard on λ = 0; MFPT divides by zero

`persistence_profile` computes `mfpt = (mu + 3λ)/(2λ²)`. With `residual_leak_fraction = 0` and B = 1,
λ = 0 and this raises `ZeroDivisionError`. The frozen protocol sets the leak to 0.05 so v0.1 never
hits it, but the parameter is exposed and 0 is the natural "perfect boundary" value a reader would
try first. `transient_survival` guards this case (`if damage <= 0: return 1.0`); the MFPT path does
not.

### M4 — Two "adversarial controls" are hardcoded constants, not computations

- `coarse_two_state_one_step_lower_bound: 0.0` — a literal. The claim "the declared coarse estimate
  is exactly zero even when full-state σ is positive" is asserted, not computed. I computed it
  independently: lumping the ring's states {0} vs {1,2} and taking the one-step antisymmetric flux
  gives −6.2×10⁻³³, i.e. zero to machine precision. **The claim is true** — but the rig does not
  establish it, and a reader cannot tell the difference between a verified zero and a typed zero.
  For contrast, a *time-subsampled* 3-state observation gives 0.0714 (δt=0.5), 7.0×10⁻⁴ (δt=1),
  0.0 (δt=3) — a graded, informative family the rig could have reported instead of a constant.
- `common_input_control()` returns a dict of four literals (`1.0`, `0.0`, `0.0`, verdicts). The
  common-input trap — the single most valuable control in the design, since it is where a real
  estimator would fail — involves no computation at all. `I.common_input_control` is a check that
  three typed constants equal three typed thresholds.

### M5 — No uncertainty anywhere, and the CSV invites the forbidden reading

Zero occurrences of confidence interval, standard error, bootstrap, sample size, or random seed in
the executable code. This is disclosed (§6.5) and acceptable for an analytic rig. But
`four_dial_factorial_grid_v0_1.csv` lays out four dial columns beside four readout columns for 625
rows — precisely the "B = 0.7, D = 0.4, M = 0.8, I = 0.9" table the operational spec §6 says
**"Never publish this."** The interpretive guard lives in prose in two other files; the artifact most
likely to be opened in a spreadsheet and read as a four-number phenotype carries no guard at all.
Add a declaration/missingness header, or emit the required reporting form.

### M6 — Packaging: the module does not run as documented

`README.md` says `python3 -m four_dial`. Under Python 3.11 with `PYTHONSAFEPATH` set (or any
`-P`/isolated invocation), this fails with `No module named four_dial` because the CWD is not on
`sys.path`. `PYTHONPATH=. python3 -m four_dial` works. `tests/test_four_dial.py` handles this
correctly by inserting ROOT itself; `__main__.py` does not. One-line fix, but the documented
invocation should work as written.

### M7 — Version-stamp and provenance defects

- The canon is cited in `SOURCE_MANIFEST.md` under Drive id `1PZdsto8bRLB1SgoAYnGfOvAjCuygFklD`.
  The copy currently in the AOP Canon folder is id `1jnqgjhCg6X-7FzOSEEZWM4V40ck7xty_`. I downloaded
  both: identical, 255,684 bytes, sha256 `99f64ecc…00aff`. Content provenance is sound; there are
  **at least three Drive copies** of the canon (the operational spec cites a third,
  `1mnX6Y8frvAkl8rpH3aP2OR27jriGVel-`). The manifest hash is what saved this, and it should be kept.
- The filename/body version mismatch (v1.27 filename, v1.26 masthead) is correctly flagged and
  retained rather than silently resolved. Good practice; worth keeping.
- Per house convention, result filenames use `v0_1` but the design document's own version is only in
  the title. The visualization file `four-dial-lab.html` carries **no version stamp at all** and will
  be unidentifiable in a folder scan.

### M8 — The interactive lab duplicates the model in JavaScript

`four-dial-lab.html` reimplements `damage`, `repair`, `drive`, and the full uniformization loop in
JS. It is currently faithful (I read it line by line against `model.py`), including the same
`exp(-x)` underflow. But two independent implementations of the same physics with no cross-check will
drift. Either generate the JS constants from the frozen protocol, or add a test that the JS and
Python agree at the operating point.

---

## 3. What the rig gets right

Worth stating plainly, because the findings above are severe and the work is not bad:

- **Drive is operationalized correctly.** σ = (k₊−k₋)·a is right; I verified it against an
  independent flux/affinity sum over the full rate matrix, agreeing to 4×10⁻¹⁵. The reversal
  convention R is declared, the parity condition is stated, and the ring is in even variables —
  which is exactly the canon's third scope condition on the D→M theorem. This axis is done properly.
- **The survival solve is numerically correct** in its operating regime (6.7×10⁻¹⁶ vs `expm`), and
  the analytic MFPT formula checks out.
- **O-information missingness is handled exactly as the canon requires** — `None` plus a reason
  string, not zero. This is the single best piece of epistemic hygiene in the repo.
- **The declaration tuple is complete and frozen before outcomes**, and the design document's §6
  self-critique correctly identifies the diagonal-calibration and stipulated-coupling problems.
  The gap is that §1 and the results file do not inherit §6's honesty.
- **Full determinism and bit-exact reproducibility**, with a hashed source manifest. This is what
  let me audit it in an afternoon.

---

## 4. Recommended disposition

**Do not promote any result from this rig to the canon, and do not cite its calibration numbers.**
The rig is usable as what its README says it is — a calibration bench that "recovers known controls"
— but the recovery is of controls it defined to be recoverable.

Ordered by what changes conclusions:

1. **Resolve S1 (Drive sign) before anything else.** Either justify current-as-repair against the
   canon's §12 gate, or rebuild the chamber so the gate binds and check the sign is recovered
   downward. This is the one finding that touches an established canon claim.
2. **Recompute all four structural readouts as the canon's own quantities** (E not AIS; TC not
   lagged MI; B1/B2/B4 not a bare response ratio) and re-report the off-target ranges. Expect the
   diagonal to disappear. Report *that* as the result — it is the honest and more interesting one.
3. **Execute Priority 1 (blind estimation).** Until readouts are estimated from finite trajectories
   by code that does not know the generative parameters, `CAL.dial_recovery` has no content. Score
   the suite by mutation detection rate, not by pass count.
4. **Implement UNDETERMINED** and delete `predictive_state_complexity_bits` (or make it `None`).
5. **Compute the two adversarial controls** instead of typing their answers.
6. **Drop the "3×" framing.** Report the coalition structure (which it does correctly) and state
   that the factor equals the chain length by construction.
7. **Fix M2/M3/M6** (underflow, λ=0 guard, module path) — these are cheap and one of them silently
   returns a wrong zero.
8. **Re-describe the 625-cell grid** as 5×5×5×5 structural / 185-point persistence, and note that
   M and I are not separately identifiable in V.

---

## 5. What I verified, and what I did not

**Verified by independent computation** (not by reading the rig's output): entropy production via
flux/affinity sum over the full generator; the coarse two-state lumping estimate; finite-horizon
survival via `scipy.linalg.expm`; the analytic MFPT; all ablation deltas; the overcount factor for
chain lengths 2–6; excess entropy of the rotor, memory chain, and A|B pair at δt = 1; instantaneous
TC on the Integration module; canon proxies B2/B5 on the Boundary module; rotor stationary
distribution invariance in D; the uniformization underflow threshold; the λ=0 divide; per-axis
recovery-error decomposition; grid degeneracy counts; and the 7-mutant detection rate.

**Verified by reproduction:** `python3 -m four_dial` regenerates all three result files with md5
identical to those delivered on Drive; 8/8 unit tests pass.

**Read in full:** the four repo Python files, both result markdown files, the frozen protocol, the
design document, `SOURCE_MANIFEST.md`, `README.md`, the HTML visualization, canon §§1–9, 12, 12′,
12″, the charter, and the operational-definition spec.

**Not verified:** I did not check the cited external literature against primary sources
(Lee & Seo 2021; Bouchet & Reygner 2016; Spinney & Ford 2012) — I relied on the canon's own
statement of its §12 gate and its grade. Anyone acting on S1 should read Lee & Seo directly.
I did not attempt to reproduce the canon's 5.7× ring result; my own ad-hoc ring probe was
non-monotone with a 0.08% range and is not evidence of anything, which is why S1 rests on the
canon's established gate and on the verified scope fact, not on my probe. I did not read the
Ladder bridge memo. I did not review the earlier `AOP_CA_Benchmark_v0_1`.

**Governance note:** I did not build this artifact, so reviewing it does not breach "nobody grades
their own homework." But this review is a builder-seat product and is **not** an independent
verification — it should go to prime for that if any of its findings are to be acted on as canon.

---

*End of review.*
