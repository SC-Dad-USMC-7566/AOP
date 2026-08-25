# AOP Canon — Proposed Change Set v1.19 → v1.20 (Phase A)

**Prepared 20 July 2026.** Phase A of the four-axis deepening: fold the corrections that require **no new
science** — three over-claim fixes, two honest re-grades (upgrade + downgrade), and three additive
citations that turn asserted edges into cited ones. Every edit either corrects a demonstrable error or
states an existing claim more honestly; **no claim is retracted and nothing is strengthened beyond what
is now cited.** This is a *proposed* change run, not applied to the Drive master — approve and it folds.

Verification for this run: ✓ primary read · ~ named/result-level (full text not line-checked) · ⊙
canon-inherited. Grades: SETTLED / SYNTHESIS / FRONTIER / DEFECT.

Each edit gives **LOCATION**, **OLD** (verbatim from v1.19), **NEW** (verbatim to fold), and a one-line
**WHY**. Prose is given in clean form; whoever applies maps to the master's markdown escaping.

---

## Group 1 — The "|corr| < 0.05" over-claim (DEFECT → reword). Flagged independently by all four axis groups.

The canon reports a *coupling-controlled partial* correlation as if it were the *raw* correlation. Raw
Spearman is ≈0.61 (B–M, I–M) and 0.83 (B–I); 0.05 is the value only after partialling out coupling
strength. The fix states the measured dependence, which is **stronger** for the axes (dissociable, not
orthogonal; Memory carries the most unique variance).

### EDIT 1 · §4, Faes paragraph (v1.19 line ~187)
**OLD:** "Computing all three non-energy dimensions on one such process, we find Memory dissociates freely from both Boundary and Integration — it is a mutual information on the time-lagged covariance, a different object from the instantaneous cuts, and across random dynamics its correlation with each is below 0.05."
**NEW:** "Computing all three non-energy dimensions on one such process, we find Memory is the most distinct axis, though not orthogonal to the others: it is a mutual information on the time-lagged covariance — a different object from the instantaneous cuts Boundary and Integration read off the static covariance — and it dissociates completely by construction (a pure-memory regime realizes large excess entropy at zero Boundary and Integration). Across random systems its *raw* correlation with each of Boundary and Integration is ≈0.61, but that is shared coupling strength, not a direct tie: partialling out overall coupling strength drives the Boundary–Memory correlation to −0.05 and the Integration–Memory correlation to −0.62 (a mild tradeoff at fixed coupling). Memory carries 0.59 of its rank-variance uniquely — against 0.29 each for Boundary and Integration — so it is genuinely the most independent axis while still sharing coupling strength with the plane."
**WHY:** corrects the misreport; states the true, stronger finding. **[DEFECT-fix; analytic-model-result.]**

### EDIT 2 · §4, Table 2, M–I row (v1.19 line ~177)
**OLD:** "memory and integration are near-orthogonal across random dynamics (|corr| < 0.05) and appear as substitutable strategies in bet-hedging theory [10]"
**NEW:** "raw correlation ≈0.61 across random dynamics, but this is shared coupling strength — partialling out coupling gives −0.62 (a mild tradeoff at fixed coupling), and memory and integration appear as substitutable strategies in bet-hedging theory [10]; dissociable, not orthogonal"
**WHY:** same correction in the ledger. Tag ("dissociable") unchanged. **[DEFECT-fix.]**

### EDIT 3 · §4, Figure T caption (v1.19 line ~189)
**OLD:** "(a) Four thousand random stable vector-autoregressive systems plotted in (Boundary, Integration, Memory) space: Memory spreads freely of the Boundary–Integration plane (pairwise |corr| < 0.05), while Boundary and Integration share a plane (corr ≈ 0.83)."
**NEW:** "(a) Four thousand random stable vector-autoregressive systems plotted in (Boundary, Integration, Memory) space: Memory is the most distinct axis (0.59 unique rank-variance) — its raw correlation with the Boundary–Integration plane is ≈0.61, but this is shared coupling strength (partialling out coupling gives B–M ≈ −0.05, I–M ≈ −0.62), so Memory is dissociable, not orthogonal; Boundary and Integration share a plane (corr ≈ 0.83) because both are static cuts of one covariance."
**WHY:** the caption is the most-quoted statement of the result; it must not read as orthogonality. **[DEFECT-fix.]**

### EDIT 4 · Abstract (v1.19 line ~17)
**OLD:** "The separation is graded, not blanket: Memory is near-orthogonal to the rest across generic systems, while Boundary and Integration are dissociable only by construction and otherwise share a plane — so the honest claim is four distinguishable axes, not four independent ones."
**NEW:** "The separation is graded, not blanket: Memory is the most distinct axis — its raw correlation with the other two is shared coupling strength only, vanishing to a mild tradeoff once coupling is controlled, and it carries 0.59 of its variance uniquely — while Boundary and Integration are dissociable only by construction and otherwise share a plane through an exact nesting identity, so the honest claim is four distinguishable axes, not four independent ones."
**WHY:** aligns the abstract's "near-orthogonal" with the measured dependence. **[DEFECT-fix.]**

---

## Group 2 — Boundary lead-scalar (DEFECT → reword + make the nesting identity explicit)

Boundary's Table-1 lead proxy is `I(in;out)` = B5, which (i) measures dependence across the cut (high =
coupled, nearer "no boundary") and (ii) is *literally a slice of Integration*. Lead with the
Boundary-specific proxies; state the identity that makes this a defect.

### EDIT 5 · §2, Table 1, Boundary row, "Formal quantity" cell (v1.19 line ~91)
**OLD:** "Boundary panel (lead proxy: mutual information I(inside ; outside), a measure of statistical dependence across the cut, not of separation per se — the panel is a family, not this one scalar; see the operational-panels deliverable)"
**NEW:** "Boundary panel — a family of proxies, not one scalar (see the operational-panels deliverable). The lead proxies are the Boundary-specific ones: a declared interior/exterior state contrast (B1), the screening residual I(inside;outside | interface) (B2), and the maintenance burden required to hold the contrast against leak (B4). Cross-boundary dependence I(inside;outside) (B5) is retained only as a descriptive quantity, and is explicitly the cross-cut slice of Integration (§4), not boundary strength — a high value means the two sides are coupled, nearer 'no boundary' than 'sealed'."
**WHY:** retires the lead-scalar defect; a lone I(in;out) mis-scores Boundary regardless of the couplings. **[DEFECT-fix; SYNTHESIS.]**

### EDIT 6 · §4, Faes paragraph — make the B–I nesting identity explicit (insert after the "~0.83 … same covariance matrix" sentence, v1.19 line ~187)
**INSERT (new sentence):** "This substrate-sharing is exact, not merely a correlation: total correlation decomposes as TC = I(inside;outside) + TC_inside + TC_outside (verified to machine precision, maximum error 1.8×10⁻¹⁵ over 4000 systems), so Boundary's cross-cut proxy I(inside;outside) is literally a component of Integration. The ≈0.83 Boundary–Integration correlation is this nesting identity showing through, and it is why Boundary earns a separate line only where the cross-cut slice specifically carries persistence weight — reported otherwise, it double-counts a piece already inside Integration."
**WHY:** the identity is elementary/algebraic and machine-verified; stating it converts the 0.83 from an unexplained correlation into a structural fact and grounds Edit 5. **[SETTLED (algebraic) + SYNTHESIS (the reading).]**

---

## Group 3 — Drive→lifetime sign (reframe: this one changes a claim)

The v1.19 gate ledger says the sign of Drive's leverage on lifetime is "geometry-set." For AOP's exact
regime (a measure-preserving / divergence-free current at fixed stationary distribution, small noise)
the literature gives a **settled one-sided rule**: circulation can only shorten or neutralize the MFPT,
never lengthen it. Retire the geometry-free framing; reconcile any pro-persistent drive as a
hypothesis-non-match rather than a counterexample.

### EDIT 7 · §12, Table 4, "Current → lifetime" outcome cell (v1.19 line ~730)
**OLD (tail of the cell):** "… Sign is geometry-set (here anti-persistent: the current stirs the system over its barrier); generalization beyond the minimal ring open"
**NEW (tail of the cell):** "… For a measure-preserving current (divergence-free, at fixed stationary distribution) in the small-noise limit the sign is not free but one-sided: circulation can only shorten or leave unchanged the mean first-passage time, never lengthen it — the escape barrier is pinned to the fixed quasipotential and only the prefactor moves, which the non-reversible Eyring–Kramers analysis shows is monotone toward faster escape [Lee & Seo 2021; Bouchet & Reygner 2016]. The ring's anti-persistence is therefore the expected behaviour, not a coincidence of geometry. A drive that appears to *lengthen* lifetime (e.g. a star's fusion) does not contradict this: it is not a measure-preserving current at fixed stationary distribution — it reshapes the stationary state and acts through the forced Boundary and Memory edges — so the theorem does not bind it. What Drive forces directly, under the lifetime primitive, is a change in lifetime; for a genuine measure-preserving current the direction is settled and downward. Generalization to finite noise, and the classification of drives that reshape the stationary state, remain open."
**WHY:** replaces an incorrect "geometry sets the sign" with the settled result, and scopes the star correctly. **[SETTLED (the sign rule) + FRONTIER (finite-noise / stationary-reshaping drives).]**

---

## Group 4 — Sector-split status (upgrade FRONTIER → SETTLED for the σ̇ half)

The claim "σ̇ is a functional of the generator's antisymmetric sector" is not model-specific — it holds
for general diffusions and is the entropy-flux / frenesy decomposition. Upgrade that half; keep synthesis
on the full no-cross-coupling claim pending a one-line lemma AOP owns.

### EDIT 8 · §4, sector-split synthesis note, closing sentence (v1.19 line ~131)
**OLD:** "The claim is offered as framework synthesis, secure within the two model classes examined and argued but not proven beyond them; the generalization to arbitrary dynamics is the frontier step."
**NEW:** "The claim is offered as framework synthesis, but its first half is no longer model-specific: that the thermodynamic cost σ̇ is a functional of the generator's antisymmetric (irreversible) sector holds for general — including non-Gaussian and degenerate — diffusions [Da Costa et al. 2023], and is the general instance of the time-antisymmetric (entropy-flux) versus time-symmetric (frenesy / dynamical activity) split of the path-space action for Markov jump and diffusion processes [Maes 2020; Schnakenberg 1976]. What remains this framework's synthesis is the short step that AOP's own Memory/structure functionals — the equal-time covariance that sets resolvability, and the causal asymmetry Ξ — are time-symmetric observables; given that, no forced cross-sector coupling follows in general. That step is a lemma to write, not a frontier."
**WHY:** cites the general result; downgrades the remaining gap to a lemma. **[σ̇ half: SETTLED; full claim: SYNTHESIS.]**

### EDIT 9 · §12, status row "No forced Memory/structure ↔ Drive coupling (sector split)" — Status cell (v1.19 line ~622) and Basis cell tail (v1.19 line ~623)
**OLD (Status):** "synthesis; frontier at generalization"
**NEW (Status):** "σ̇ = antisymmetric-sector: settled (general diffusions); full no-cross-coupling: synthesis"
**OLD (Basis, tail):** "… Secure within the two model classes tested (Gaussian OU, finite Markov); the generalization to arbitrary dynamics is argued, not proven (§4, §13)"
**NEW (Basis, tail):** "… The σ̇ = antisymmetric-sector half is general, not model-specific [Da Costa et al. 2023 (entropy production depends only on the irreversible drift for general diffusions); Maes 2020 and Schnakenberg 1976 (the time-antisymmetric/time-symmetric split)]. What is argued-not-proven is only that AOP's specific Memory/structure functionals are time-symmetric observables, closing the no-cross-coupling claim generally — a lemma, not a frontier (§4, §13)."
**WHY:** aligns the status table with Edit 8. **[re-grade.]**

---

## Group 5 — Drive → Integration dynamic edge (grade honestly as a tendency, not a law)

### EDIT 10 · §4, "Drive → Integration" edge (v1.19 line ~137)
**OLD:** "Drive → Integration is free at equilibrium, open under selection. Parts can be correlated at zero dissipation; integration exists statically for free. Whether drive builds or maintains integration over time is a separate, unsettled question, and conflating the two is an error."
**NEW:** "Drive → Integration is free at equilibrium and, over time, a conditional tendency — not a forced edge. Parts can be correlated at zero dissipation; integration exists statically for free. Dynamically, drive is a *precondition* for a strong form of maintained integration but does not *force* it: robust, size-extensive multipartite correlation cannot be sustained in thermal equilibrium and requires far-from-equilibrium, time-dependent (limit-cycle) dynamics [necessity result, 'Dissipation enables robust extensive scaling of multipartite correlations,' arXiv:2410.13375 (2024)], and maintaining correlation against thermal erasure carries a dissipative cost [Parrondo, Horowitz & Sagawa 2015] — so drive must pay for integration but does not automatically purchase it, and dissipation can equally destroy correlation. Claims that drive *maximizes* integration (maximum entropy production, not a settled principle) or generically *builds* it (strong readings of dissipative adaptation) are not relied on here. Conflating 'integration exists for free' with 'drive made this integration' remains an error."
**WHY:** states the honest, cited status; explicitly refuses MaxEP/England as law. **[SYNTHESIS/tendency; not FORCED, not blankly OPEN.]**

---

## Group 6 — Additive citations that harden existing claims (no wording change to the claim)

### EDIT 11 · §11 (star) and §8 (gravitational floor) — add the founding primary for negative specific heat
Where the star's negative specific heat is invoked (§11, "a self-gravitating system has negative specific heat (radiate energy and it gets hotter)…") and the gravitational Integration floor is cited (§8), add the founding primary alongside the existing review:
**ADD citation:** "[the gravothermal result of Lynden-Bell & Wood 1968; long-range-interaction synthesis, Campa, Dauxois & Ruffo 2009]"
**WHY:** the star's restoring-force claim currently rests on a 2009 *review*; Lynden-Bell & Wood 1968 is the founding primary (negative specific heat of self-gravitating systems / the gravothermal catastrophe), read this session. **[strengthens SETTLED base.]**

### EDIT 12 · §4 (D→M spore sentence, v1.19 line ~129) — E vs Cμ adjudication via crypticity
After "… the quantity Drive compels (E) and the quantity that does the persisting work (statistical complexity Cμ) can come apart [13]." **INSERT:**
"The gap between them is exactly the crypticity χ = Cμ − E [13]: E is the *forced* numerator (a law touches it — the D→M floor), Cμ is the *persistence-relevant* numerator for stored-structure persisters (the spore's semantics live here), and χ is the diagnostic of when the two diverge — large for the spore (deep stored structure invisible to the past–future channel), and essentially zero for a periodic crystal (fully predictable, Cμ = E)."
**WHY:** answers the standing "which Memory numerator, and when" using machinery already cited ([13]); synthesis, no new computation. **[SYNTHESIS.]**

### EDIT 13 · §5 (E requires stationarity, v1.19 line ~248) — a stationarity-free Memory proxy exists
After "… cross a non-stationarity and E does not merely change value, it loses its definition." **INSERT:**
"Where a persister is genuinely non-stationary — a developing organism, an aging system, the star on its nuclear clock — the time-resolved cousin of E survives: local (pointwise) active information storage is defined per time step and does not require global stationarity [Lizier, Prokopenko & Zomaya 2012], estimated off-stationarity from an ensemble of realizations rather than a time-average [Wibral, Lizier et al. 2014], with the honest caveat that the continuous-time formulation yields a clean memory-*use rate* but no clean instantaneous stored-*amount* off-stationarity [Spinney, Prokopenko & Lizier 2018]. E remains the stationary lead proxy (M1); local active information storage is the scoped proxy where stationarity fails."
**WHY:** turns the definedness hole from an open flag into a cited, scoped patch (M-panel proxy M3/M5). **[SETTLED components + SYNTHESIS scoping; a real residual — no instantaneous stored-amount off-stationarity — is stated honestly.]**

---

## Reference-list additions (with verification markers)

Add to §References. Items marked ~ or with a full-text caveat carry the canon's standard "verify before
final" flag (like the existing ⚠ entries).

1. **Lee JS, Seo I.** Non-reversible metastable diffusions with Gibbs invariant measure I: the Eyring–Kramers formula. *Probab. Theory Relat. Fields* (2021). arXiv:2008.08291. — measure-preserving circulation raises the saddle's unstable eigenvalue ⇒ E[τ] ≤ E_rev[τ] always (Thm 3.5, Lemma 3.4, Cor 3.9). **✓ main theorems read.** *(Drive-sign, Edit 7.)*
2. **Bouchet F, Reygner J.** Generalisation of the Eyring–Kramers transition-rate formula to irreversible diffusion processes. *Ann. Henri Poincaré* 17, 3499 (2016). arXiv:1507.02104. — barrier set by the Freidlin–Wentzell quasipotential; irreversibility enters the prefactor. **~ abstract.** *(Drive-sign, Edit 7.)*
3. **Da Costa L, Barp A, et al.** The entropy production of stationary diffusions. *J. Phys. A* 56, 365001 (2023). arXiv:2212.05125. — entropy production is a quadratic form of the irreversible (antisymmetric) drift only, for general non-elliptic/degenerate diffusions. **✓ propositions/theorem read.** *(Sector split, Edits 8–9.)*
4. **Maes C.** Frenesy: time-symmetric dynamical activity in nonequilibria. *Phys. Rep.* 850, 1–71 (2020). arXiv:1904.10485. — path-space action splits into a time-antisymmetric entropy-flux part and a time-symmetric frenesy part (Markov jump + diffusion). **~ concept verified this session; full text not line-checked.** *(Sector split.)*
5. **Schnakenberg J.** Network theory of microscopic and macroscopic behavior of master-equation systems. *Rev. Mod. Phys.* 48, 571 (1976). — cycle/affinity decomposition; EP is a sum over cycle affinities × currents. **~ standard result, named.** *(Sector split.)*
6. **Lynden-Bell D, Wood R.** The gravo-thermal catastrophe in isothermal spheres and the onset of red-giant structure for stellar systems. *MNRAS* 138, 495–525 (1968). doi:10.1093/mnras/138.4.495. — self-gravitating systems have negative specific heat. **✓ statement read this session.** *(Star, Edit 11.)*
7. **[Authors TBD]** Dissipation enables robust extensive scaling of multipartite correlations. arXiv:2410.13375 (2024). — robust extensive scaling of multipartite mutual information cannot occur in equilibrium; requires far-from-equilibrium time-dependent attractors. **~ result verified this session; full theorem + author list not line-checked — ⚠ verify before final.** *(D→I, Edit 10.)*
8. **Parrondo JMR, Horowitz JM, Sagawa T.** Thermodynamics of information. *Nat. Phys.* 11, 131–139 (2015). doi:10.1038/nphys3230. — thermodynamic cost of creating/maintaining/erasing correlations. **✓ bibliographic + scope verified this session.** *(D→I, Edit 10.)*
9. **Lizier JT, Prokopenko M, Zomaya AY.** Local measures of information storage in complex distributed computation. *Inf. Sci.* 208, 39–54 (2012). — pointwise (local) active information storage; definition is per-timestep, stationarity is only an estimation convenience. **✓ definition read.** *(Non-stationary Memory, Edit 13.)*
10. **Wibral M, Lizier JT, Vögler S, Priesemann V, Galuske R.** Local active information storage as a tool to understand distributed neural information processing. *Front. Neuroinform.* 8:1 (2014). — non-stationary estimation via an ensemble of trials. **✓ read.** *(Edit 13.)*
11. **Spinney RE, Prokopenko M, Lizier JT.** Characterising information-theoretic storage and transfer in continuous-time processes. *Phys. Rev. E* 98, 012314 (2018). arXiv:1804.03269. — continuous-time memory-use rate survives non-stationarity; no clean instantaneous stored-amount. **✓ read.** *(Edit 13.)*

(Crutchfield–Ellison–Mahoney 2009 — the crypticity χ = Cμ − E used in Edit 12 — is already reference [13].)

---

## Proposed changelog entry (append to the running master, R-style)

> ### R[next] · Canon movement: v1.19 → v1.20 — Phase A corrections (four-axis deepening)
> - **What.** Thirteen edits, no claim retracted. (1) Fixed the "|corr| < 0.05" over-claim in three places (Fig T caption, Table 2 M–I row, §4 body) plus the abstract: the figure is the coupling-controlled *partial*; the raw B–M/I–M correlation is ≈0.61, Memory carries 0.59 unique rank-variance — dissociable, not orthogonal (Edits 1–4). (2) Retired Boundary's lead-scalar defect: Table 1 now leads with B1/B2/B4 and marks B5 = I(in;out) as the cross-cut slice of Integration, with the exact nesting identity TC = I(in;out)+TC_in+TC_out (1.8e-15) stated in §4 (Edits 5–6). (3) Reframed the Drive→lifetime sign: for a measure-preserving current at fixed stationary distribution the sign is settled one-sided (never lengthening) [Lee & Seo 2021; Bouchet & Reygner 2016]; the star reconciled as a stationary-reshaping drive the theorem does not bind (Edit 7). (4) Upgraded the sector-split σ̇-half from frontier to settled-general [Da Costa et al. 2023; Maes 2020; Schnakenberg 1976], leaving a one-line time-symmetry lemma as the only synthesis step (Edits 8–9). (5) Re-graded Drive→Integration (dynamic) as a cited tendency/necessity [arXiv:2410.13375; Parrondo et al. 2015], not a forced edge, and explicitly not MaxEP/England (Edit 10). (6) Added Lynden-Bell & Wood 1968 as the founding primary for the star's negative specific heat (Edit 11); folded the E-vs-Cμ crypticity adjudication [13] (Edit 12) and local active information storage as the stationarity-free Memory proxy [Lizier 2012; Wibral 2014; Spinney 2018] (Edit 13). Eleven references added.
> - **Why.** A four-axis deepening (four parallel axis groups + a literature-first gap-closure pass) surfaced the over-claims and found the open items closable by citation/synthesis. Every edit corrects an error or grades an existing claim more honestly.
> - **Grade.** No promotions to theorem beyond what is cited; one honest *downgrade* (Drive→I dynamic: open → cited tendency), one honest *upgrade* (sector-split σ̇-half: frontier → settled-general), one *correction* (the |corr| figure), one *reframe* (Drive-sign).
> - **Verification.** Da Costa 2023, Lee–Seo 2021, Lynden-Bell–Wood 1968, Parrondo–Horowitz–Sagawa 2015, Lizier 2012 / Wibral 2014 / Spinney 2018 read against primary this session (✓). Maes 2020, Schnakenberg 1976, Bouchet–Reygner 2016 named/result-level (~). arXiv:2410.13375 result-verified but full theorem + author list not line-checked (⚠ before final). The |corr| numbers and the nesting identity are reproduced from the deposited depmap.
> - **Downstream.** The Drive-sign reframe and the sector-split upgrade change the hub's forced-spoke inventory description → cross-project (Ladder) propagation-bus note warranted; flag and leave for posting.
> - **Status.** Proposed — awaiting fold into the Drive master.

---

## Deferred (NOT in Phase A — these are Phase B–D, they need computation or new work)
- **B2, B4 computations** (screening residual; housekeeping σ_hk pump+leak) — Phase C. Machinery cited (Edits await the numbers).
- **Reconcile the star's apparent pro-persistence** by finite-noise / hypothesis check — Phase B (the highest-value single task). Edit 7 states the settled rule; the star computation confirms the reconciliation.
- **F2 seam** — level-selection is synthesizable (Hoel 2016 / Marshall 2026 / Zhang 2025, graded per Krakauer 2020); non-stationary/moving-MIP is the one genuine new-work item — Phase D.
- **O-info sign on the star, E(T) retention curves, mask on a memory edge / well-posed partition** — Phase C small computations.

---

## Before-final verification to close (charter discipline)
- arXiv:2410.13375 — line-check the theorem statement, the "robust" definition, and confirm the author list before the master is finalized (currently ⚠).
- Maes 2020 (Phys. Rep. 850) and Schnakenberg 1976 — read the decomposition statement in full text (currently ~).
- Bouchet & Reygner 2016 — full text was blocked; the decisive sign result is Lee–Seo 2021 (✓), so the claim does not rest on Bouchet–Reygner, but confirm the quasipotential statement before quoting it.
