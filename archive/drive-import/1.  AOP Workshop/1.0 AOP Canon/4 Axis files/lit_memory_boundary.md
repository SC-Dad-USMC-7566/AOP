# AOP Literature Closure — Memory (non-stationarity), Boundary maintenance cost, Screening↔CI

Date: 2026-07-20 · Agent: literature-closure
Markers: ✓ read primary · ~ abstract/named · ? unread lead
Grades: SETTLED (established peer-reviewed science) · SYNTHESIS (AOP's overlay on settled parts) · FRONTIER (open/contested)

---

## GAP A — A memory measure defined WITHOUT global stationarity

**VERDICT: CLOSABLE-BY-CITATION.** The information-dynamics literature already supplies a
memory quantity — **local (pointwise) active information storage (LAIS)** — whose *definition*
is per-agent, per-timestep and does **not** require the process to be stationary. Stationarity
in this literature is an *estimation convenience* (pooling samples across time), not part of the
definition. When the process is non-stationary, the established move is to estimate the required
time-resolved PDFs from an **ensemble of trials/realizations** at each time point. This directly
patches AOP's "definedness hole": excess entropy E = I(past;future) is stationary-only
(Crutchfield & Feldman 2003), but its *local, time-resolved* cousin is not.

### Verified results

1. ✓ **Lizier, Prokopenko & Zomaya (2012)**, "Local measures of information storage in complex
   distributed computation," *Information Sciences* 208:39–54 (read via author PDF + companion
   framework arXiv:0811.2690).
   - Local AIS is defined pointwise: a_X(n+1) = lim_{k→∞} log2 [ p(x_n^(k), x_{n+1}) /
     (p(x_n^(k)) p(x_{n+1})) ]. It is a value attached to a specific time index n+1, whose
     time-average recovers the (stationary) AIS.
   - Read verbatim on stationarity: PDFs were estimated by pooling observations "since the cells
     … are homogeneous variables and quasi-stationarity is assumed over the relatively short time
     interval." => Stationarity/homogeneity enters **only** to estimate p, not to define a(n+1).
   - Grade: **SETTLED** (the pointwise definition), for the definitional claim AOP needs.

2. ✓ **Wibral, Lizier, Vögler, Priesemann & Galuske (2014)**, "Local active information storage
   as a tool to understand distributed neural information processing," *Front. Neuroinform.* 8:1
   (read via Frontiers full text).
   - This is the load-bearing citation for non-stationarity. They explicitly treat non-stationary
     (stimulus-evoked, non-ergodic) neural data and estimate the time-resolved PDF p_t(·) by
     **pooling across trials at each time point t** ("multiple time-series realizations or trials
     would be required"), interpreting LAIS "local per agent and time step." Global temporal
     stationarity is replaced by an across-trials (cyclostationary) equivalence assumption at each
     moment t.
   - Grade: **SETTLED** as an applied method; the non-stationary use is exactly demonstrated.

3. ✓ **Spinney, Prokopenko & Lizier (2018)**, "Characterising information-theoretic storage and
   transfer in continuous time processes," *Phys. Rev. E* 98:012314 (arXiv:1804.03269; read via
   ar5iv). Important nuance:
   - The continuous-time **active memory utilisation rate** Ṁ_X is a genuine pathwise/dynamical
     rate and the framework "accommodates non-stationary processes through time-dependent rate
     functions" (stationarity only collapses the two rate variants, M̊_X = Ṁ_X).
   - BUT the **instantaneous predictive capacity** I_X (the continuous-time analogue closest to
     "stored information as a state quantity") is explicitly "defined in such a manner that it does
     not yield a rate and is thus not a dynamical quantity"; there is "no such analogous pathwise
     quantity." => Caveat for AOP: the *rate* of memory use survives continuous time and
     non-stationarity cleanly; the *amount* of information stored as an instantaneous state does
     not get a clean pathwise definition.
   - Grade: **SETTLED** result, with an honest limitation AOP should quote.

4. ~ **Schreiber (2000)** transfer entropy and Lizier's **local transfer entropy** (in
   arXiv:0811.2690): local TE t(i,j,n+1) is likewise pointwise and inherits the same
   stationarity-is-estimation-only status. Named/confirmed via the framework paper, not
   re-derived here.

### Recommendation for AOP
Replace/augment E = I(past;future) with **local active information storage** as the Memory
quantity that survives a non-stationarity. State it precisely: the *definition* is pointwise and
stationarity-free; off-stationarity you pay for it with an **ensemble of realizations** (trials,
or many copies of the developing/aging/stellar system) to estimate the time-resolved PDF, rather
than a time-average. Cite Lizier–Prokopenko–Zomaya 2012 (definition), Wibral–Lizier 2014
(non-stationary estimation), Spinney–Prokopenko–Lizier 2018 (continuous-time rate + the honest
"no instantaneous stored-amount" caveat). This is a citation, not new work — but flag that the
ensemble requirement is a real substitution of assumptions (stationarity → replicate availability),
which is itself a defensible AOP point: a lone non-repeatable trajectory across a non-stationarity
genuinely loses a well-defined stored-information *amount*.

---

## GAP B — B4 maintenance burden: the Drive→Boundary edge as a number

**VERDICT: CLOSABLE-BY-CITATION (settled machinery) + a short CLOSABLE-BY-SYNTHESIS step to
instantiate it on a minimal leak+pump model.** The housekeeping/excess decomposition of entropy
production is settled steady-state thermodynamics. The cost of *holding* a nonequilibrium contrast
is exactly the **housekeeping entropy production** — the dissipation required by the nonzero
steady-state probability current — and it is closed-form (Σ of thermodynamic force × flux) for a
minimal pump+leak model. AOP's verbal claim ("free at equilibrium; costs drive ∝ leakiness when
maintained") is the correct qualitative reading of this machinery and can be turned into a number.

### Verified results

1. ✓ **Hatano & Sasa (2001)**, "Steady-State Thermodynamics of Langevin Systems," *Phys. Rev.
   Lett.* 86:3463 (arXiv:cond-mat/0010405; abstract/result read). Establishes the extended second
   law for transitions *between* nonequilibrium steady states and splits dissipation into a
   **housekeeping** part (continuous heat dumped just to sustain the NESS, i.e. its nonzero
   current) and an **excess** part (extra heat from *changing* the state); the Shannon-entropy
   difference is tied to the excess heat in quasi-static operation. Formalizes Oono–Paniconi.
   Grade: **SETTLED**.

2. ~ **Oono & Paniconi (1998)**, "Steady state thermodynamics," *Prog. Theor. Phys. Suppl.*
   130:29 — the framework that introduced the housekeeping/excess split (named; foundational).
   Grade: **SETTLED** (as originating framework).

3. ✓ **Speck & Seifert (2005)**, "Integral fluctuation theorem for the housekeeping heat,"
   *J. Phys. A* 38:L581 (arXiv:cond-mat/0507420; located/abstract). Puts the housekeeping heat on
   a rigorous fluctuation-theorem footing: Q_hk is generated by the local mean velocity / steady
   current, so its ensemble average is exactly the steady-state entropy production that must be
   paid to hold the NESS. Grade: **SETTLED**.

4. ~ Closed-form applicability to a leak+pump / gradient model: standard stochastic-NESS result
   that the steady entropy-production rate = Σ_edges J · X (flux × thermodynamic force), e.g. Qian's
   stochastic-NESS treatment and the ion-flux nonequilibrium-thermodynamics literature
   (MDPI *Entropy* 19(1):40, 2017, "Nonequilibrium Thermodynamics of Ion Flux through Membrane
   Channels"). For a two-state pump+leak cycle this is elementary and analytic — matching AOP's
   "closed-form, not estimated" discipline. Grade: **SETTLED** machinery / **SYNTHESIS** to
   instantiate on AOP's minimal model.
   - Also a strong lead: ? **"Information thermodynamics of cellular ion pumps,"** *Phys. Rev.
     Research* (recent) — ties pump housekeeping cost directly to information thermodynamics; worth
     reading before AOP writes B4, as it may already state AOP's Drive→Boundary edge.

5. ✓ Empirical anchor (Na/K-ATPase share of ATP budget): **20–45%** of resting-tissue energy is
   spent on the Na+/K+ pump, rising toward **~2/3** in electrically active neurons (BioNumbers
   #106429, primary source Whittam 1964; corroborated by StatPearls / astrocyte energetics
   literature). This is the empirical face of B4: the housekeeping cost of holding the boundary
   gradient is a dominant, measurable fraction of the cell's drive budget. Grade: **SETTLED**
   (well-anchored empirical value; note it's a broad 20–45% range, cite as such).

### Recommendation for AOP
Define B4 (Drive→Boundary maintenance burden) as the **housekeeping entropy production rate** of
the boundary's NESS: σ_hk = Σ J_i X_i over the pump+leak cycle. At equilibrium (no gradient, zero
current) σ_hk = 0 — "free at equilibrium" is exactly recovered. With a maintained gradient against
a leak conductance g, the pump current needed to hold the contrast scales with leakiness, so
σ_hk ∝ (leak) — AOP's verbal claim becomes a derivation. Cite Oono–Paniconi 1998 and Hatano–Sasa
2001 for the decomposition, Speck–Seifert 2005 for the housekeeping heat's status, and the
Na/K-ATPase 20–45% figure as the empirical anchor. The only "new work" is writing down and solving
the two-state model — trivial, closed-form, and in-house. Check the PRR "ion pumps" paper first in
case B4 is already published verbatim.

---

## GAP C — Screening ↔ conditional-independence bridge (lower priority)

**VERDICT: CLOSABLE-BY-CITATION for the physics; CLOSABLE-BY-SYNTHESIS for the mapping.** The
physical fact is textbook-settled and independently known in several fields; the
conditional-independence reading is AOP's clean overlay on it, not novel physics.

### Verified results

1. ✓ Exponential decay of electrostatic correlations over the **Debye screening length λ_D** is
   classical Debye–Hückel / Poisson–Boltzmann theory — "interactions in dilute electrolytes decay
   exponentially with distance, with the Debye screening length the characteristic length-scale"
   (read via Smith, Lee & Perkin, arXiv:1607.03926 / *J. Phys. Chem. Lett.* 2016, which frames this
   as the established baseline before its own concentrated-electrolyte anomaly). Grade: **SETTLED**.
   - Caveat worth one line: in *concentrated* electrolytes the measured decay length can
     *exceed* λ_D ("underscreening"), so AOP should say "screened residual dependence falls off
     over the screening length λ_screen (≈ λ_D in the dilute regime)," not "exactly λ_D."

2. Cross-field corroboration (the "known in three fields" pattern AOP prizes): the same
   "screening ⇒ exponential decay of correlations ⇒ effective statistical independence at long
   range" statement appears as the **correlation length / Ornstein–Zernike** decay in statistical
   mechanics and as **cluster decomposition / mass-gap screening** in field theory. So the
   physics is multiply-established. Grade: **SETTLED** (physics) / **SYNTHESIS** (the explicit
   map: interface variables screen inside from outside ⇒ I(in;out | interface) → 0 exponentially
   in interface thickness/λ_D ⇒ a literal Markov blanket).

### Recommendation for AOP
Treat the screened-interface ⇒ conditional-independence claim as **settled physics wearing an
information-theoretic label**, not a discovery. State: a screened boundary of thickness ≳ few λ_D
makes the residual cross-interface dependence I(in;out|interface) decay ~exp(−thickness/λ_D); this
is Debye–Hückel screening (and its stat-mech/field-theory analogues) restated as a Markov-blanket
condition. Low risk, cite the electrolyte-screening literature, and note the underscreening caveat
so the λ_D identification isn't overclaimed. Not novel; do not present as an AOP prediction.

---

## One-line status table
- GAP A (non-stationary memory): CLOSABLE-BY-CITATION — local AIS, def is stationarity-free; ensemble replaces stationarity. SETTLED (+ honest continuous-time caveat).
- GAP B (B4 maintenance burden): CLOSABLE-BY-CITATION + trivial in-house synthesis — housekeeping entropy production; SETTLED machinery, closed-form on pump+leak; Na/K 20–45% anchor.
- GAP C (screening↔CI): CLOSABLE-BY-CITATION (physics SETTLED, multi-field) + SYNTHESIS mapping; not novel.
