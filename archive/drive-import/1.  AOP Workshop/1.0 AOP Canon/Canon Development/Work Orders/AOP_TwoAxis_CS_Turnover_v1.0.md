# CS-1.3 — Turnover as the physical quantity on axis A

**Document ID:** `AOP_TwoAxis_CS_Turnover_v1.0.md`
**Seat:** Claude Science (builder). **Date:** 4 August 2026. **Order:** CS-1.3.
**Depends on:** `AOP_TwoAxis_CS_Matrix_v1.0.md`, Drive `1fYUdHTACQmPzXXFdVSyX9XB31dDKN_4J`, 36,803 B, md5 `c03d0aaf11e8c61946364a7b36b3e73e` — **deposited and hash-stamped before this work began.**
**Governing:** AOP Charter v1.2 · AOP Canon v1.26 (md5 `54ceb3772e29f25c6e139b703d550d59`, verified this session).

**Standing:** builder proposal. Written to be attacked.

**Verification tags:** `✓` full text read · `~` abstract/metadata only · `⚠` not retrieved.

---

## 0 · The answer, first

The order asks this seat to establish or fail to establish that replacement-rate-against-degradation-rate is **measurable and discriminating**, and names the erythrocyte as the test case: *the account predicts its lifetime as the decay of unreplaced constraint rather than merely placing it in a bin. If that prediction can be made quantitative it is the strongest thing this arc can produce; if it cannot, say so.*

**It can be made quantitative, and it is not the strongest thing this arc can produce, because a standard hematology model already fits the same data about as well.** Both halves of that sentence are load-bearing.

**What works.** Θ = 0 predicts the erythrocyte survival curve is **linear in a random-age labelled cohort**, hence **MPL/T₅₀ = 2.000 exactly**. Observed, from primary data: **1.983 and 1.982** for the two lowest biotin densities (Mock et al. 2011, `✓` full text via PMC3089718). A constant-hazard model with the *same* T₅₀ predicts MPL/T₅₀ = **3.226** and leaves 25% of cells circulating at day 115, where observation finds essentially none. **Random destruction is excluded by a factor of 1.6 on a ratio the account predicts with no free parameters.**

**What does not work, and this seat states it rather than letting a reviewer find it.** The Weibull full-lifespan distribution fitted by Shrestha et al. 2016 (`✓`, PMC4887310) — shape *k* = 5.38 as recovered here from their published mean 115.60 d and SD 24.77 d — predicts **MPL/T₅₀ = 2.071**, against observed 1.983 and AOP's 2.000. **AOP is closer, but the margin is 0.07 on a ratio whose two observed replicates differ by 0.001, and the Weibull is a curve fit with two free parameters while AOP's is a parameter-free consequence.** The honest comparison is not "AOP wins"; it is that AOP derives with zero free parameters what the standard model obtains with two, and that the two are not distinguishable by this statistic alone.

**The real finding is not the erythrocyte at all.** Θ is not a gradient. Solving the constraint-decay equation gives a **threshold at Θ_crit = c*/(1−c*)**: below it lifetime is finite and set by the decay of unreplaced constraint; above it lifetime **diverges** and persistence stops being turnover-limited. This is why the four-vector must stay a four-vector — a system can sit above threshold on three axes and below it on the fourth, and the finite one sets the lifetime.

**Domain: a real rate exists for 12 of 44 rows.** The order's suspicion is correct. Θ is available for the well-studied cells, for BIOS-3, and for a handful of artefacts where it is exactly zero. It is **undefined** — not zero — for any monotonically accumulating store, which breaks it on E5/C8.

---

## 1 · The quantity, defined so it can fail

For each constraint **C** holding one of AOP's four axes, at declared grain τ:

> **Θ(C) = k_rep / k_deg** — the rate at which the system replaces C, against the rate at which C degrades.

Constraint integrity C(t) ∈ [0,1] obeys, in the minimal linear form:

    dC/dt = k_rep·(1 − C) − k_deg·C

with steady state **C_∞ = Θ/(1+Θ)**. Declare a viability floor **c\*** — the integrity below which the system leaves its viable set, which under the §1.1 V-rule is where finite-horizon survival collapses. Then:

    lifetime is finite  ⟺  C_∞ ≤ c*  ⟺  Θ ≤ c*/(1 − c*)  ≡  Θ_crit

**This is the discriminating structure, and it is a threshold rather than a spectrum.** At c* = 0.5, Θ_crit = 1: a system replacing its constraint as fast as it degrades persists indefinitely, and one replacing it even slightly slower has a finite, computable lifetime.

| Θ | C_∞ | time to floor (days, calibrated so Θ=0 gives 115 d) |
|---|---|---|
| 0.00 | 0.000 | **115.0** |
| 0.10 | 0.091 | 120.4 |
| 0.25 | 0.200 | 130.2 |
| 0.50 | 0.333 | 153.3 |
| 0.90 | 0.474 | 261.6 |
| 1.00 | 0.500 | **∞** |
| ≥ 1 | > 0.5 | ∞ |

**Note what this does to the *alive* spectrum.** The order says axis A "has a direction and it is measurable." It has a direction, and the measurable quantity is **discontinuous at Θ_crit**. Systems are not smoothly more or less alive on turnover; they are turnover-limited or they are not. **[SYNTHESIS — the threshold is a consequence of the declared linear model; a saturating or cooperative replacement law moves Θ_crit but preserves the threshold. This seat has not tested a nonlinear law and does not claim generality.]**

---

## 2 · The erythrocyte, worked

### 2.1 Why it is the test case

The mature human erythrocyte has **Θ = 0 exactly on all four axes** — the only system on the frozen set for which that is true of a living cell. It has no nucleus and no ribosomes, so band-3 and spectrin, once made, are never replaced. It is the pure case: constraint that decays and is not renewed.

### 2.2 The prediction, made without free parameters

The biotin method labels **a representative sample of RBCs of all ages** (Franco 2012, `✓`) — this is the fact the derivation turns on. If clearance is age-determined at lifespan L, then a random-age cohort has residual lifetimes uniform on [0, L], so:

    S(t) = 1 − t/L

**exactly linear**, giving T₅₀ = L/2 and x-intercept L, hence:

> **MPL / T₅₀ = 2.000, with no fitted parameter.**

Under Mock's own estimator (linear least-squares to all points >10% remaining; x-intercept = MPL — procedure read from the primary, `✓`):

| Model | T₅₀ (d) | MPL (d) | MPL/T₅₀ |
|---|---|---|---|
| **H_A · age-determined, Θ = 0 (AOP)** | 57.5 | 115.0 | **2.000** |
| H_B · random destruction (constant hazard, T₅₀-matched) | 58.0 | 187.1 | 3.226 |
| H_C · Weibull lifespan, Shrestha params (k = 5.38) | 58.0 | 120.0 | 2.071 |
| **OBSERVED** (Mock 2011, two lowest biotin densities) | **57.5** | **114.0** | **1.983** |

Observed values, verbatim from the primary `✓`: T₅₀ = **58 ± 4 d and 57 ± 4 d**; MPL = **115 ± 8 d and 113 ± 9 d**. Cross-checked in the same paper against ⁵¹Cr (MPL 116 ± 16 d) and against Mollison (115 d) and Bentley (110 ± 21 d).

**H_B is excluded.** A pure random-destruction process with the observed T₅₀ leaves **25.3%** of the labelled cohort circulating at day 115. Observation finds essentially none.

### 2.3 The concession that keeps this from being a headline

**H_C is not excluded, and H_C is the standard model.** Shrestha et al. fit Weibull, gamma and lognormal lifespan distributions to biotin data and report "equally excellent goodness-of-fit" `✓` for all three, with mean full lifespan 115.60 d (95% CI 109.17–121.66) and SD 24.77 d. The recovered shape **k = 5.38** is neither 1 (random) nor ∞ (deterministic): **clearance is age-determined but stochastic, with a lifespan CV of 0.214.**

So the correct statement of the result is narrower than the order hoped for:

> **The Θ = 0 account predicts, with no free parameters, the qualitative feature that distinguishes erythrocyte clearance from random destruction — near-linear survival, MPL/T₅₀ ≈ 2 — and gets the value right to 0.9%. It does not outperform a two-parameter lifespan fit, and the residual spread (CV 0.21) is something the account does not predict at all.**

**[The observed numbers: SETTLED, primary-verified. The linear-survival derivation: SETTLED (it is elementary renewal theory, not this framework's). The identification of L with decay-of-unreplaced-constraint: SYNTHESIS. The claim that this discriminates AOP from standard hematology: NOT ESTABLISHED — this seat looked and found it does not.]**

### 2.4 Prior art on this exact result, checked before claiming anything

Per the charter's *be skeptical of anything that looks new*: the linear-survival-implies-age-determined-clearance inference is **long-established hematology**, not an AOP finding. Korell, Coulter & Duffull 2011 (`~`) model RBC survival with an explicit **bathtub hazard** separating "death of RBCs due to senescence (age-dependent increasing hazard rate) and random destruction (constant hazard)" — the same two hypotheses this section compares, published fifteen years earlier and with a finer decomposition. **AOP has not discovered that erythrocyte clearance is age-determined. What AOP adds is the identification of the age variable with unreplaced-constraint decay, and the placement of that case on a common axis with BIOS-3, Voyager and *E. coli*.** That is a synthesis contribution and is graded as one.

---

## 3 · Θ across the case set — where a real rate exists

**12 of 44 rows carry a rate that can be sourced.** The rest are Θ = 0 by inspection (nothing is replaced) or undefined.

| Case | Θ | Basis | Tag |
|---|---|---|---|
| **A1** *E. coli* | ≫ 1 | replacement dominated by growth dilution at 20–40 min doubling; bulk protein degradation slow against it | `~` |
| **A2** hepatocyte | ≫ 1 | mammalian protein half-lives measured genome-wide (Schwanhäusser et al. 2011, *Nature* 473:337–342, `~`) are short against cell lifetime | `~` |
| **B3** erythrocyte | **0 exactly** | no protein synthesis; §2 | `✓` |
| **B5** syn3A | ≫ 1 | divides; whole-cell model published (Thornburg et al. 2022) | `~` |
| **B8** cancer cell | ≫ 1 | as A1 | `~` |
| **A7** star | ≥1 photosphere / **0** core fuel | main-sequence lifetime *is* the fuel-depletion time | `~` |
| **A6** candle flame | ≈ 1 | reaction zone regenerated on the same ms timescale it is consumed | `~` |
| **E2** BIOS-3 | **0.91 aggregate** | "The total closure of material turnover constituted 91%", water and gas exchange fully closed, 5-month crewed run (Gitelson et al. 1989, *Adv Space Res* 9(8):65–71, `✓` abstract; full text `~`) | `✓` |
| **E1** Apollo-class | ≈ 0 | tanked oxygen, packed food; mission duration *is* the depletion time | `~` |
| **E3** Voyager-class | **0**; lifetime = RTG decay constant | nothing replaced; decay is nuclear | `~` |
| **C3 / C7′ / D7 / D8′** artefacts | **0** | no constraint replaced | by inspection |
| **A3 / A4 / A5 / A8 / B4 / D6 / D8** | **0** | nothing replaced | by inspection |

### 3.1 BIOS-3 is the one composite with a real number, and it lands below threshold

**Θ = 0.91 against Θ_crit = 1** (at c* = 0.5). BIOS-3 is a *measured* system sitting just under the divergence, which is exactly what its history shows: it ran 5-month crewed closures successfully and was never self-sufficient. On the table in §1 a Θ of 0.90 gives a lifetime **2.3× longer** than Θ = 0 — a large effect, still finite. **This is the single best vindication of the quantity on the whole set: a real, instrumented, historically-operated system whose measured closure fraction and whose actual operating history agree with where the threshold puts it.**

**The caveat, stated plainly.** 91% is closure of *material turnover*, which is not the same object as Θ for any one of the four constraints, and mapping one onto the other is this seat's move, not the source's. **[The 91% figure: SETTLED, primary. Its identification with Θ: SYNTHESIS, and the weakest step in this section.]**

---

## 4 · Where the quantity breaks

**4.1 Monotonically accumulating stores make Θ undefined, not zero.** For E5 (LLM instance) and C8, the within-episode context store **accumulates and does not degrade**: k_deg = 0, so Θ = k_rep/0. This is not a high score and not a low one — the ratio has no value. Any store that grows without decaying breaks the quantity. **This is why the matrix scores E5's Memory axis *partial* on other grounds and withdraws the turnover claim (matrix §5 NC6).**

**4.2 One object, two answers.** The star has Θ ≥ 1 for the photosphere and Θ = 0 for the core fuel. Which one is *the* turnover depends on which constraint is asked about, and axis A supplies no rule for choosing. Since the finite one sets the lifetime, the defensible convention is **Θ = min over the four constraints** — but that is a collapse to a scalar by another route, and the order forbids collapsing the four-vector. **This seat records the tension and does not resolve it.**

**4.3 The trivial-satisfaction attack (OAI surface 8) partly lands.** Any dissipative structure replaces *something* — a flame's reaction zone scores Θ ≈ 1. Θ does **not** by itself separate a flame from a cell. What separates them is the four-vector: the flame is at 2 of 4 produced, the cell at 4 of 4. **Θ is a quantity attached to each axis; it is not a life criterion and cannot be used as one.**

**4.4 c\* is declared, not measured.** Θ_crit depends on the viability floor, which is an analyst declaration under the canon's V-slot. Different c\* moves the threshold. The *existence* of a threshold does not depend on c\*; its location does.

---

## 5 · What this seat could not do

- **No new measurement of Θ was made.** Every rate is sourced or declared unavailable.
- **The B7 path-integration retrieval was run before the matrix stamp** and is disclosed there (matrix §7). Its supporting records: Dyer & Dickinson-adjacent vector-navigation literature located via PubMed (e.g. Dyer 2002, *Naturwissenschaften*, `~`; Patel et al. 2022, *Curr Biol*, "Vector navigation in walking bumblebees", `~`). **Neither was read in full text, and B7's G verdict is therefore supported at `~` only — for the row that alone holds the high-A/high-G quadrant open on real systems. This is the weakest evidentiary point in the entire arc and this seat flags it as such rather than leaving CW to find it.**
- **Gitelson et al. 1989 full text `~`** — the 91% figure is from the abstract, which states it directly.
- **Schwanhäusser 2011 `~`** — abstract only; note its published *Nature* corrigendum (2013, 495:126–127) is acknowledged here and its content not checked.
- **No nonlinear replacement law was tested.** The threshold result is model-dependent to that extent.

---

*End of `AOP_TwoAxis_CS_Turnover_v1.0.md`. Builder proposal under Order CS-1.3. Not canon. Not blessed by its author.*
