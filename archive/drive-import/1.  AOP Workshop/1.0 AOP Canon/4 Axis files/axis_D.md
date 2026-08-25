# Axis D — Drive

**Group D dossier · AOP canon v1.19 · prepared 20 July 2026**
Verification markers: ✓ read against primary source this session · ~ named/abstract-level only · ⊙ canon-inherited (already in the canon's verified list) · ? unverified lead.
Grades: SETTLED · SYNTHESIS · FRONTIER · DEFECT.

---

## 1. The axis in one paragraph

Drive is the energy axis, and it is the odd one out among the four: not a static mutual information across a cut but the **time-asymmetry of the dynamics themselves**. Its formal quantity is the entropy-production rate,

  σ = lim(τ→∞) (1/τ) · D_KL( P_fwd ‖ P_rev ),

the Kullback–Leibler divergence per unit time between the distribution over forward trajectories and the distribution over their time-reverses [Parrondo–Van den Broeck–Kawai 2009 ⊙]. This makes Drive the **cleanest axis in the framework**: alone with Memory, it is computable with *no declared partition* — there is no inside/outside or part/part choice to argue over, only the trajectory ensemble and its reverse. It is also the **hub** of the coupling graph (§4 below). Two things it is emphatically *not*: it is not free-energy throughput or resource input (that is D1–D2 of the panel; σ is D5, the *dissipation*, what is thrown away), and it is not the persistence primitive itself — persistence is *lifetime* (mean first-passage time out of the viable set), and Drive is one operation that lengthens or shortens it, not the thing being lengthened. The honest scope: what σ measures is **dissipation / trajectory irreversibility**, and if only D5 is computed the axis should be *labelled* "Dissipation/Irreversibility," reserving "Drive" for the broader target the D-panel (D1–D5) spans.

---

## 2. The persister, per example

The mandate: name the **process** that persists, never the husk you can point at. Drive is the axis on which this matters most, because a drive-dominated persister is *defined* by an activity, and the material carrying that activity is almost always wholly replaced.

| Example | The persister (process) | The husk | Present-tense type (§9) | What Drive contributes |
|---|---|---|---|---|
| **Flame** | the self-sustaining reaction front, rebuilt each instant from fresh fuel + oxidiser | the particular gas molecules (wholly replaced); cold soot once it dies | **process** | *everything* — the whole persistence is drive; marginally stable, **no restoring force** |
| **Star** | the self-regulating hydrostatic + fusion process | the ball of gas / the burnt-out remnant (white dwarf, collapsing envelope) once fusion ceases | **process**, with a **strong restoring force** | *defining axis* — fusion resupplies the pressure that fights gravity + radiative loss |
| **Crystal** | *was* the growth front — drive depositing structure | the finished lattice: memory made solid, drive → 0, terminal | **configuration** | *nothing now* — drive is spent; the lattice is the corpse of the drive process |
| **Spore** | a **paused** process — architecture present, drive switched off, viability in escrow | a mere blueprint / description would be the husk (and would be *dead*, §4a) | **capacity** | drive ≈ 0 *by design*; held in reserve, re-forms when a coupling re-forms |
| **Dissipative structure** (Bénard cell, driven Markov ring, BZ oscillator) | the sustained ordered flow pattern maintained by throughput | the vessel and the medium (molecules cycle through and out) | **process** | *its entire reason to exist* — the order is present **only** while σ > 0; cut supply and it relaxes to equilibrium |
| **Bound atom** | the screened, bound electron–nucleus configuration | — (minimal case; little turnover) | **configuration** | ≈ 0 — a Coulomb well is free; the low-Drive admitted corner, opposite the star |

Persister-is / husk-is lines, with the diachronic test (§4a) where it bites:

- **Flame.** *The persister is the process; the husk is the current gas.* Present-tense: a process held above threshold. Diachronic: it does **not** restart itself — interrupt supply and it is simply gone, no held state to reboot from. Marginal stability, drive-only semantics.
- **Star.** *The persister is the self-regulating hydrostatic+fusion process; the husk is the ball of gas (and, at death, the remnant).* This is the flagship — treated in full in §3. Diachronic: a star does not pause and self-restart; kill the drive and it dies on a Kelvin–Helmholtz time, leaving a remnant that is a *new* (degenerate or collapsing) process, not the resumed original.
- **Crystal.** *The persister was the growth front; the husk is the lattice you hold.* The living thing was drive depositing structure; once grown, σ → 0 and only memory-made-solid remains. It cannot restart itself — regrowing it requires an external drive rebuilding it from a template, i.e. a *new* process. Terminal, spent semantics.
- **Spore.** *The persister is a paused process; the husk would be a bare description.* The distinction is load-bearing: a held-state (regulatory architecture physically present, drive switched off) is *life paused* (§11a, viable/pausable tier), whereas a mere record is dead. Diachronic test passes on the right side: the spore restarts *itself* from its *own* held state (germinant = key to a still-functional lock) → same process; a mammoth reconstructed from a sequenced genome is rebuilt from a *record* → new process.
- **Dissipative structure.** *The persister is the maintained flow pattern; the husk is the medium it runs in.* This is the purest Drive case: the pattern's present-tense viability *is* σ > 0. It is the cleanest physical home of σ = D_KL(P_fwd‖P_rev), because the structure exists exactly to the extent the forward and reverse trajectory ensembles differ. A limit-cycle dissipative structure has a restoring force (star-like); a marginally-stable one does not (flame-like) — same axis, two stability classes.
- **Bound atom.** *The persister is the bound configuration; there is little husk.* It persists **without drive** — the reminder that persistence does not require dissipation, and the low-Drive corner that anchors the opposite end of the axis from the star.

---

## 3. The axis independently

### 3.1 The settled core

**σ = trajectory time-asymmetry. [SETTLED ⊙]** Entropy production equals the KL divergence between forward and time-reversed trajectory distributions [Parrondo–Van den Broeck–Kawai 2009 ⊙]. Operationally this is not just a definition but a *measurable*: the KLD between a stationary time series and its time-reverse, multiplied by k_B, is a **lower bound** on the entropy production, with the bound tightening as the observed degrees of freedom more completely capture the state [Roldán & Parrondo, *Phys. Rev. E* 85, 031129 (2012) ✓ — verified this session: "This KLD … turns out to be a lower bound to the entropy production along the process"]. That tightness caveat is the same coarse-graining fact the framework states elsewhere (below): σ read on an incomplete description under-reports.

**It has been measured in real persisters. [SETTLED ⊙]** Broken detailed balance — σ > 0 read directly from trajectory irreversibility — is measured in living cells [Battle et al. 2016 ⊙] and in the human brain [Lynn et al. 2021 ⊙]. This is what lets the Drive axis touch reality rather than remain a formal object.

**No partition choice. [SETTLED ⊙]** Unlike Boundary and Integration, Drive needs no declared inside/outside or component partition (Table 1). This is why it, with Memory, is one of the two "hard" (choice-free) axes.

### 3.2 The panel (D1–D5)

The declaration-tuple discipline forbids reporting a lone σ as "Drive." The Drive target is a **panel**:

- **D1** — resource input (energy / chemical potential / exergy per time)
- **D2** — useful maintained work or flux sustaining the target process
- **D3** — housekeeping dissipation (cost of holding the NESS)
- **D4** — nonadiabatic / relaxation dissipation
- **D5** — total entropy production / irreversibility, σ = lim (1/τ) D_KL(P_fwd‖P_rev); finite-horizon form when non-stationary

The naming rule is a guardrail against Trap 1 (§5): **σ alone (D5) does not imply high resource input (D1) or useful work (D2).** A system can dissipate heavily while doing nothing useful, or run large useful throughput at modest σ. Report σ as "Dissipation/Irreversibility," and only claim "high Drive" once you say *which* of D1–D5 and why.

### 3.3 The cleanest computable proxy, with worked numbers

The closed-form home of the axis is the **driven three-state Markov ring** (Figure DM): swept from strong reverse bias through detailed balance to strong forward bias, every dissipating configuration has σ > 0, and at detailed balance σ = 0 exactly. On the same object the forced floor to Memory is computed (§4.1). **[SETTLED base + SYNTHESIS, analytic-model-result.]**

**Grain-relativity of the magnitude. [SETTLED law + SYNTHESIS reading.]** The *law* σ ≥ 0 is observer-independent; the *number* is not. Coarse-grained entropy production swings roughly **70-fold** with the observer's grain (spatial bins × time-step) in the Figure 1 model, while σ ≥ 0 holds at every grain [Parrondo–Van den Broeck–Kawai 2009 ⊙; Hoel et al. 2013 ⊙ for coarse-graining creating/destroying apparent causal structure]. A σ reported without a declared cut (the D tuple) is not an invariant of the system. This is the same observer-relativity Roldán–Parrondo's "completeness of observed DOF" caveat names from the estimation side.

### 3.4 The load-bearing distinction: Drive acts on **lifetime**, not occupancy

This is the single most important Drive result, and it is why Drive is not inert under the framework's primitive. **[SETTLED within model, GO gate; SYNTHESIS in placement.]**

The current→lifetime gate (Table 4) drove a **divergence-free** current on a ring at *fixed stationary distribution and fixed dynamical activity*, and measured mean first-passage time to erasure:

- **lifetime falls 5.7×** (MFPT 12.35 → 2.17 as the current rises to 0.95·activity)
- **occupancy invariant to 1e-14** by construction
  *(the rev.2 recompute reports 5.4× / 1e-15 — same conclusion, minor numerical spread.)*

The two candidate primitives dissociate *completely*. A pure current — pure Drive — leaves stationary occupancy of the viable set exactly fixed (occupancy is a functional of the stationary distribution alone, hence current-blind) while changing lifetime severalfold. Under the framework's chosen primitive (lifetime, §1), **Drive has direct leverage on persistence**, not only indirect leverage through Boundary and Memory. Had the framework kept the earlier "persistence = occupancy" reading, it would have declared Drive inert where a flame plainly is not. This is why occupancy was retracted (Trap 2, §5).

One subtlety worth flagging as its own result: **the sign of Drive's leverage on lifetime is geometry-set, not universal.** On this minimal ring the current is *anti*-persistent — it stirs the system over its barrier and *cuts* lifetime. But the star's fusion current is the opposite: it is exactly what *keeps the star alive*. So "Drive raises persistence" is false as a blanket claim; Drive → lifetime is a **signed** edge whose sign depends on the geometry of the viable set. (Gap G4.)

---

## 4. Interactions with the other three axes — the energy hub, and its uneven spokes

Drive is the hub, but the spokes are not alike, and the unevenness is the spine of the structure. Note a structural point first: the 4,000-system dependence map (`aop_depmap.py`) is a **B–I–E map** — its three coordinates are Boundary, Integration, and Memory-as-excess-entropy. **Drive (σ) sits outside that static map**, because σ is a trajectory object, not a static cut of the covariance. Drive couples *into* the map through exactly two forced floor-type edges and the lifetime leverage above; it does not appear in the pairwise Spearman table. That is itself the finding: the hub reaches the static triangle only through the two forced spokes, and nowhere else forcibly.

### 4.1 Drive → Memory — **FORCED FLOOR, directional** [SETTLED (direction) / conditionally-forced (reach)]

σ > 0 ⇒ E > 0, where E = I(past; future) is the excess entropy. This is **not a fresh guess** but a scoped corollary of the same trajectory-irreversibility identity that defines Drive [Parrondo–Van den Broeck–Kawai 2009 ⊙]: E = 0 ⟺ the process is i.i.d. ⟺ it equals its own time-reverse ⟺ σ = 0; contrapositive, σ > 0 ⇒ E > 0.

- **It is a floor, not a depth.** It guarantees *some* past–future correlation exists, not that the load-bearing memory is large.
- **The converse fails.** At detailed balance σ = 0 while E > 0 (Figure DM: E ≈ 0.70 at the balance point) — a reversible oscillator remembers for free. Necessity runs one way only.
- **Three scope conditions or it is false/vacuous:** σ and E must be read on the *same complete stationary description* (coarse-graining can hide a current so a reduced observable looks reversible — the Memory-axis twin of §3.3; and exactly the Roldán–Parrondo completeness caveat); the process must be stationary; and the floor reaches predictive memory (E) *only*.
- **The reach stops at E.** Pre-registered gates show the drive forces **no stored time-asymmetry** (Ξ = Cμ⁺ − Cμ⁻ = 0 at every drive) and **no floor on stored complexity** Cμ (Cμ covaries with the drive *parameter* weakly — ~1% while σ̇ moves 20× at fixed reversible skeleton — and only through the generator's *symmetric* sector, i.e. shared input, not through the current as mechanism). The spore is the standing witness: near-zero σ carrying deep Cμ [Crutchfield–Ellison–Mahoney 2009 ⊙].

The **why** is the sector split [SYNTHESIS, secure in Gaussian-OU + finite-Markov, frontier beyond]: σ̇ is a functional of the generator's **antisymmetric (current) sector**, while the structure-side quantities are governed by the **time-symmetric sector**. A forced cross-sector coupling would need one quantity depending on the antisymmetric sector *as its mechanism*; among tested quantities only σ̇ and E do — and E is exactly the one the D→M floor already names. Hence the hub's forced spokes are exactly the two floor-type edges and no more.

**Do not attribute the floor to Still 2012.** Still et al. (thermodynamics of prediction) ⊙ supplies a *different, complementary* point: the dissipated work is proportional to the *nonpredictive* retained information, so efficiency drives stored memory to be predictive and only predictive memory is free. That is *why* the memory Drive forces is the predictive part (E), but the floor σ > 0 ⇒ E > 0 itself is the trajectory-irreversibility corollary [Parrondo–Van den Broeck–Kawai 2009 ⊙], not a Still result. Keeping these straight matters (see the "excess entropy production" collision, Trap 3).

Dependence-map cross-check: the map shows M (= E) is the **most distinct axis** — 59% unique rank-variance, and its raw ~0.61 correlation with B and I *vanishes* controlling for coupling strength (B–M|coupling = −0.05). So Drive pins a *floor* under the M axis but does not say where on it a system sits; and E's ties to B, I are shared-driver artifacts, not structure. The forced D→M edge and the map's "M is most independent" verdict are consistent: a floor is not a determination.

### 4.2 Drive → Reliability (TUR) — **FORCED, regime-bounded** [SETTLED, conditionally-forced]

The precision of any current a system runs is bounded by its dissipation: the thermodynamic uncertainty relation prices steadiness [Barato & Seifert 2015 ⊙; Gingrich et al. 2016 ⊙]. Within the classical Markov regime in which it is proven, this is a law. It is the hub's second clean forced spoke. It is not an edge to B/M/I but a bound on the *reliability of the drive's own output* — semantic precisely when the current is load-bearing.

### 4.3 Drive → Boundary — **CONDITIONAL** [SYNTHESIS / known]

Holding a gradient costs nothing at equilibrium — a potential well (the bound atom's Coulomb skin) is free — and costs drive only when the boundary must be held **against a leak**, the price set by how leaky it is (B3 permeability × B4 maintenance burden in the Boundary panel). Not in the static B–I–E map (that map has no σ coordinate). The star is the case where this bites hardest: scramble the photospheric opacity (the leak the drive works against) and the star stops being a star.

### 4.4 Drive → Integration — **FREE (static) / OPEN (dynamic)** [SETTLED (static) / FRONTIER (dynamic)]

Parts can be correlated at *zero* dissipation; integration exists statically for free. Whether drive *builds or maintains* integration over time is a separate, unsettled question, and conflating the two is an error. The static half is visible in the map (Integration is a covariance object, computed with σ = 0). The dynamic half — does sustained drive grow integration under selection? — is genuinely open and is where England-style dissipative-adaptation claims would live (see G5).

---

## 5. The star — the flagship Drive case

The star earns a section of its own because **Drive is its defining axis**, and because it is where the framework's own instrument is driven soft. Everything below is checkable *now*; none of it is teleology.

**The persister.** *The persister is the self-regulating hydrostatic + fusion process; the husk is the ball of gas, and, at death, the remnant.* Fusion is a **coherent central entropy source** that resupplies, against radiative loss, the thermal pressure that balances gravity. Kill the drive and the star does not pause — it dies on a **Kelvin–Helmholtz (thermal) time**, contracting and reradiating its gravitational binding energy, ending as a degenerate remnant that is a new process, not the resumed original. Drive here is not one axis among four of comparable weight; it is the axis whose failure *is* the death.

**Flame vs star — same character, opposite stability class. [SYNTHESIS.]** Both are all-in-drive, boundary-rebuilt-continuously persisters. The flame is **marginally stable** — at the mercy of current supply, gone the moment it is cut, *with no fight*. The star has a **strong restoring force**: the negative-specific-heat thermostat. Core cools ⇒ pressure drops ⇒ core contracts ⇒ virial heating ⇒ steeply temperature-sensitive fusion climbs ⇒ balance restored. This is the distinction the flame alone left ambiguous, and it answers a §9 worry head-on: the star's apparent goal-directedness ("keep burning") is **not** hindsight worn as a goal — it is present dynamical stability, read off the current state (hydrostatic + thermal balance), exactly as the present-tense principle demands.

**The single settled root: gravitational non-additivity. [SETTLED base + SYNTHESIS.]** One physical property is the common cause of *three* of the star's features at once. Gravity is a long-range interaction (potential ∼ 1/r), and long-range interactions are **non-additive** — the energy of a whole is not the sum of its parts' energies [Campa, Dauxois & Ruffo 2009 ⊙]. From that one fact follow:

1. **Anti-boundary character** — no negative mass ⇒ gravity is unscreenable ⇒ it builds no statistical boundary (only a causal one).
2. **The Integration floor** — subsystems never fully decouple, so nothing is ever perfectly separable.
3. **Self-regulation** — a self-gravitating system has **negative specific heat**: radiate energy and it gets *hotter*. This is the microcanonical signature of the same non-additivity, and it is the star's thermostat.

The property that *denies* the star a boundary is the property that *stabilises its drive*. This is the framework's synthesis, and it is why the star is worth working rather than merely illustrating.

**New primary source strengthening this root [✓ verified this session].** The canon grounds negative specific heat in Campa–Dauxois–Ruffo 2009 (a review). The *original* establishment for self-gravitating systems is **Lynden-Bell & Wood, *MNRAS* 138, 495–525 (1968)** — the gravothermal catastrophe: "Self-gravitating systems have negative specific heats, thus if heat is allowed to flow between two of them, the hotter one loses heat and gets yet hotter while the colder gains heat and gets yet colder." I recommend citing Lynden-Bell & Wood 1968 as the settled primary alongside Campa et al. 2009 as the modern review; it makes the star's restoring-force claim rest on the founding result, not a survey. (Antecedent history: Antonov 1962; and negative specific heat across astronomy/physics/chemistry, Lynden-Bell 1999, *Physica A* 263, 293 — a ? lead, not read this session.)

**Memory has no single value — the time-grain made concrete. [SETTLED law + SYNTHESIS reading.]** The excess-entropy numerator E is defined only for a stationary process [Crutchfield & Feldman 2003 ⊙], and a star's stationarity is *clock-dependent*: stationary on its thermal (KH) clock, manifestly **non-stationary on its nuclear clock**, along which composition drifts and the evolutionary track moves. So the star's E is not merely un-asserted between E and Cμ — it is **undefined until the clock is named**. This is Drive-relevant because it produces the sharpest tension in the framework: the cleanest forced Drive→Memory claim (σ > 0 ⇒ E > 0) holds *only for a stationary process*, so on the very flagship the paper spends the most ink on, it can be evaluated only on the thermal clock and goes silent on the nuclear one. The flagship sits precisely where the Memory-axis law is undefined. Taken as the point, not an embarrassment: it is the star that shows the floor is a *clock-relative* statement, not a defect in the floor.

**The star corrects, but is model-free ⇒ not alive. [FRONTIER definition; SETTLED components.]** This is the §11a placement, and it matters for Drive because it separates *drive + correction* from *life*. The star's restoring set-point **is** a fixed point of the constitutive dynamics — the target hydrostatic state is *where the physics sits*, with no separately-interventable reference node storing it. That is the Francis–Wonham internal-model / Bich et al. organizational-regulation distinction, **not** a good-regulator-theorem point (the good-regulator "model" is a homomorphic image under which even a bare fixed point counts, so it does not supply the decoupled-reference distinction). Computed (Figure LT): the star-type system's structural coupling has mask weight **0.01** at 2× separation and its intrinsic restoring edge weight **0.55** at 1× — both *outside* the alive region — while a cell's model edge is weight **0.70** at 20×, decoupled, *inside*. A slow/fast sweep (Figure LT-T) shows the model-edge weight flat (≈0.79 at 2× down to ≈0.72 at 20×) with **no threshold knee**: what separates star from cell is *architectural* (does a separate reference node exist?), not a timescale magnitude. **Drive alone — even drive with a genuine restoring force — does not make a thing alive.** The star is the worked proof of that.

**The instrument goes soft on the star. [conditionally-forced, Lane–Emden n=3.]** Because hydrostatic equilibrium locks every shell to the weight above and structure below, the star sits high on Integration, where per-edge semantic weights blur. Linearising the adiabatic pulsation equation on a Lane–Emden n = 3 polytrope (settled stellar structure) gives a **tridiagonal shell-to-shell operator** — a chain with a global hydrostatic constraint — whose spectrum is a graded stiff-to-sloppy band (Figure R★), roughly an order of magnitude wider than the mean-field equicorrelation caricature at matched mean correlation, with *larger* per-shell attribution uncertainty. The star sits high on *both* blur mechanisms at once — per-shell weights inferentially unresolvable, and gravity resisting intervention entirely (interventional) — while the aggregate collective mode stays sharp. It realises the resolvability limit *from its own physics*, not by relabeling. This is a demonstration of self-consistency (any strongly coupled linear system has a stiff/sloppy spectrum), not a test that could have failed.

---

## 6. Holes, traps, and DEFECTs

**Drive has no lead-scalar DEFECT.** Unlike Boundary (whose canonical Table-1 proxy, I(in;out) = B5, is the *weakest* reading and mis-scores the concept), Drive's lead proxy σ = D5 is the *correct* object for what it measures. The Drive axis is the framework's cleanest. Its exposure is entirely in *scope* and *sign*, not in a broken proxy.

**Traps already fallen into (name them, keep them fixed):**

1. **σ = throughput / free-energy input.** *Fixed.* σ is dissipation (D5), what is *thrown away* — not exergy taken in (D1) or useful work done (D2). A high-throughput steady state can carry modest σ; heavy σ can do nothing useful. Guardrail: if only D5 is computed, label the axis **"Dissipation/Irreversibility,"** not "Drive."
2. **persistence = occupancy.** *Retracted.* Occupancy is current-blind (a functional of the stationary distribution alone); lifetime is not. A divergence-free current cuts lifetime 5.7× at fixed occupancy (§3.4). Occupancy-persistence would declare Drive inert; lifetime does not.
3. **E vs "excess entropy production" — name collision.** *Live hazard.* E = I(past; future) is a **Memory** quantity (computational mechanics). "Excess entropy production" is a distinct steady-state stochastic-thermodynamics quantity living on the **Drive** axis. Unrelated objects; do not let the shared word fuse them. (The gate ledger records exactly this failure mode caught once: an entropy-production rate wearing a memory label produced a spurious positive on the E-vs-Cμ gate, retracted.)
4. **Star self-regulation = teleology.** *Fixed by §9/§11.* It is present dynamical stability (negative-specific-heat thermostat), checkable now, not a bet on the future.
5. **Star self-regulates ⇒ star is alive.** *Fixed by §11a.* Model-free correction; no decoupled reference; not alive.

**Open / frontier on this axis:**

- **Sector-split generality.** σ̇ = antisymmetric-sector functional is proven only in Gaussian-OU + finite-Markov classes; arbitrary dynamics is frontier. Every forced Drive claim inherits this scope.
- **Sign of D → lifetime.** Established only on the minimal ring, where it is *anti*-persistent; the star shows the opposite sign. The general rule mapping geometry → sign is open (G4).
- **σ's grain-relativity.** Not a defect but a discipline: any reported σ needs the D tuple, or it is not an invariant (~70× swing with grain).

---

## 7. Gap list for Axis D

**G1 — Does the sector split (σ̇ ∈ antisymmetric sector; structure ∈ symmetric sector) generalise beyond Gaussian-OU and finite Markov chains?**
(a) Literature likely partial: the Hodge/Helmholtz decomposition of Markov generators into detailed-balance + circulation parts is standard (Schnakenberg network theory; the Maes–Netočný "traffic vs. current" / frenesy-vs-entropy-production split is exactly a symmetric/antisymmetric decomposition and is a strong candidate that may already carry this). (b) SYNTHESIS → would become SETTLED if the frenesy literature proves it. (c) Needs **synthesis** (find the general result) first; new computation only if none exists. *Candidate leads: Maes 2020 "Frenesy" review; Schnakenberg 1976 — both ? unverified.*

**G2 — Is σ > 0 ⇒ E > 0 tight, or only a floor with no useful lower quantitative bound?**
The canon establishes existence (E > 0) but not a magnitude E ≥ f(σ). (a) Still et al. 2012 ⊙ bounds *nonpredictive* stored information by dissipated work — possibly re-usable to lower-bound E itself; the predictive-information / thermodynamics-of-prediction literature (Bialek–Nemenman–Tishby; Sivak–Crooks) may already have the inequality. (b) FRONTIER. (c) Likely **synthesis** (re-read Still 2012 for a magnitude bound), with a small **computation** on the ring to check tightness.

**G3 — Which of D1–D5 do the empirical measurements (Battle 2016, Lynn 2021) actually report, and does the framework's σ = D5 match?**
Cells/brain broken-detailed-balance measurements are trajectory-irreversibility estimates (D5-like, à la Roldán–Parrondo). (a) Literature answers it directly — check what estimator each paper uses. (b) SETTLED once checked. (c) Pure **synthesis** (read the methods sections). Worth doing to state the empirical touchpoint in panel terms, not vaguely.

**G4 — What sets the sign of Drive's leverage on lifetime?**
On the ring a divergence-free current is anti-persistent (stirs over the barrier); the star's current is pro-persistent. The sign is "geometry-set" but the framework has no rule. (a) Likely answerable via large-deviation / MFPT theory: Freidlin–Wentzell quasipotential and Kramers escape with a non-gradient (rotational) drift term — whether circulation raises or lowers the escape rate depends on the interplay of the rotational component with the quasipotential gradient. This is a known and studied problem in nonequilibrium escape theory. (b) FRONTIER (in AOP) but plausibly SETTLED in the escape-rate literature. (c) Needs **synthesis** (import the quasipotential result) + a confirming **computation** generalising the ring gate. *This is the highest-value Drive gap — it decides whether "Drive lengthens persistence" is ever a clean statement.*

**G5 — Does sustained drive build/maintain Integration over time (the D→I dynamic edge)?**
Static D→I is free; dynamic is open. (a) This is precisely the territory of England's **dissipative adaptation** (self-organization of driven matter toward high-absorption/high-dissipation configurations) and of MaxEP / dissipative-structures (Prigogine) claims. These are contested and must be handled carefully — dissipative adaptation is suggestive, not a theorem, and MaxEP is not a settled principle. (b) FRONTIER. (c) Needs **synthesis** (survey and grade the England/Prigogine/MaxEP claims honestly — most likely they support only a *tendency*, not a forced edge) before any AOP computation. *Candidate leads, all ? unverified this session: England 2015 "Dissipative adaptation in driven self-assembly," Nat. Nanotech.; Perunov–Marsland–England 2016, PRX; Prigogine–Nicolis dissipative structures.*

**G6 — Is the star's negative-specific-heat restoring force expressible as a mask/semantic weight in the same idiom as the cell?**
Figure LT gives the star-type OU system weights (0.01, 0.55) but the *real* stellar thermostat's per-edge weights are unresolvable (§5, the instrument goes soft). (a) No clean literature answer; it is the resolvability limit biting. (b) FRONTIER. (c) Needs **new computation** on the Lane–Emden operator, but the canon already predicts it returns an aggregate weight, not per-edge — so the honest deliverable is the *aggregate* stellar drive weight, not a per-shell decomposition.

---

## 8. Citations used

**Verified against primary source this session (✓):**
- **Roldán E, Parrondo JMR.** Entropy production and Kullback–Leibler divergence between stationary trajectories of discrete systems. *Phys. Rev. E* 85, 031129 (2012). — KLD between forward and reverse stationary trajectories is a lower bound on entropy production; tightness depends on completeness of observed DOF. *(Grounds the σ = D5 estimator and the same-complete-description scope condition.)*
- **Lynden-Bell D, Wood R.** The gravo-thermal catastrophe in isothermal spheres and the onset of red-giant structure for stellar systems. *MNRAS* 138(4), 495–525 (1968). doi:10.1093/mnras/138.4.495 — self-gravitating systems have negative specific heat (gravothermal catastrophe). *(Primary source for the star's restoring-force / thermostat claim; strengthens Campa et al. 2009.)*

**Canon-inherited, in the canon's verified list (⊙):**
- Parrondo JMR, Van den Broeck C, Kawai R. Entropy production and the arrow of time. *New J. Phys.* 11, 073008 (2009). — σ = D_KL(P_fwd‖P_rev); coarse-graining dependence. *(The Drive axis's founding identity and the σ>0⇒E>0 corollary.)*
- Still S, Sivak DA, Bell AJ, Crooks GE. Thermodynamics of prediction. *PRL* 109, 120604 (2012). — dissipated work ∝ nonpredictive retained information. *(Why the forced memory is predictive; NOT the source of the E-floor.)*
- Barato AC, Seifert U. Thermodynamic uncertainty relation for biomolecular processes. *PRL* 114, 158101 (2015). — TUR. *(D→Reliability.)*
- Gingrich TR, Horowitz JM, Perunov N, England JL. Dissipation bounds all steady-state current fluctuations. *PRL* 116, 120601 (2016). — TUR (general). *(D→Reliability.)*
- Battle C, et al. Broken detailed balance at mesoscopic scales in active biological systems. *Science* 352, 604 (2016). — σ>0 measured in cells.
- Lynn CW, et al. Broken detailed balance and entropy production in the human brain. *PNAS* 118, e2109889118 (2021). — σ>0 measured in brain.
- Campa A, Dauxois T, Ruffo S. Statistical mechanics and dynamics of solvable models with long-range interactions. *Phys. Rep.* 480, 57 (2009). — non-additivity, negative specific heat, ensemble inequivalence. *(The single settled root of the star's three features.)*
- Crutchfield JP, Feldman DP. Regularities unseen, randomness observed. *Chaos* 13, 25 (2003). — E defined only for a stationary process. *(The star's clock-dependent Memory.)*
- Crutchfield JP, Ellison CJ, Mahoney JR. Time's barbed arrow. *PRL* 103, 094101 (2009). — E vs Cμ; the spore witness.
- Hoel EP, Albantakis L, Tononi G. *PNAS* 110, 19790 (2013). — coarse-graining creates/destroys apparent causal structure.

**Named / abstract-level only (~):**
- Seifert U. Stochastic thermodynamics, fluctuation theorems and molecular machines. *Rep. Prog. Phys.* 75, 126001 (2012). — standard σ review; named in the state report, not read this session.

**Unverified leads (?), proposed to fill gaps — treat as leads, not facts:**
- Maes C. Frenesy: time-symmetric dynamical activity and nonequilibria (review, ~2020). — candidate general form of the symmetric/antisymmetric sector split (G1).
- Schnakenberg J. Network theory of microscopic and macroscopic behavior of master equation systems. *Rev. Mod. Phys.* 48, 571 (1976). — cycle/circulation decomposition (G1).
- Freidlin–Wentzell quasipotential / Kramers escape with rotational drift — sign of current's effect on MFPT (G4).
- England JL. Dissipative adaptation in driven self-assembly. *Nat. Nanotechnol.* 10, 919 (2015); Perunov, Marsland & England, *PRX* 6, 021036 (2016). — D→I dynamic edge (G5); contested, grade with care.
- Lynden-Bell D. Negative specific heat in astronomy, physics and chemistry. *Physica A* 263, 293 (1999). — modern review of the star's thermostat property (§5).
- Prigogine/Nicolis dissipative structures; MaxEP literature — D→I dynamic (G5); most likely support a tendency, not a forced edge.

*Contamination check: no retired-framework vocabulary used (no closure of constraints, C2, Ψ/ρ/κ, substrate-coupled, owned boundary/provenance, three-condition conjunction). "Own viability" used only as a declared functional V on the viable set, ownership-free.*
