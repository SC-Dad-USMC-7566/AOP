# AOP — Four-Axis State Report (audited against canon v1.19)

**Prime, 20 July 2026.** Perspective-internal working document; owns no canon claim. This is the text record; the rendered companion (math typeset, four recomputed figures) is `AOP_FourAxis_State_Report_20260720.html`, and the recomputation code is `aop_figs.py` (both delivered alongside).

**Grading.** Claim status: SETTLED / SYNTHESIS / FRONTIER / DEFECT. Citation verification *this session*: ✓ primary (abstract/passage read) · ~ named (attribution confirmed via a citing source) · ⊙ canon-inherited (not re-verified here) · ? unverified (general knowledge, provisional). Honest scope: exhaustive breadth, graded verification — load-bearing sources were opened; forty papers were not read cover to cover. Figures are my own recompute, not the canon's deposited images.

---

## 0 · State of the canon
AOP is a Perspective/atlas (target: Royal Society *Interface Focus* — the KW venue). Claim = a synthesis: persistence, fixed as **lifetime** (mean first-passage time out of the viable set, not stationary occupancy), resisted along four non-commensurable relative-entropy axes. Not a new instrument (that side-claim died on external metabolic data; autopsy closed). Two layers: syntactic coupling graph (edges forced/conditional/free) + semantic mask (viability-load-bearing couplings, via Kolchinsky–Wolpert scramble-and-rerun). Panel architecture (ADR-001): each axis is a family of proxies under a declared tuple D=(S,E,F,P,δt,τ,R,V,I,N); no proxy defines its target by fiat. Governing honest line: **"four distinguishable axes, not four independent ones."** §5 recomputes both halves — one holds, one did not.

## 1 · Boundary — DEFECT (lead scalar)
- **Concept.** Maintained inside/outside separation. DEFECT: concept unpinned — canon prose "separation" vs panel "organization regulating exchange" (opposite on cross-boundary traffic).
- **Math.** Lead proxy B = I(in;out) = ½ log(det Σ_in det Σ_out / det Σ). Panel: B1 D_KL state contrast; B2 I(in;out|F) screening; B3 leakage/flux; B4 maintenance work/σ; B5 I(in;out) dependence.
- **Canon state.** Table 1 (v1.19) still leads with I(in;out) = B5, which ADR-001 explicitly **retired** as boundary strength. I(in;out) is non-monotone in the concept (high MI = mediation OR leakage OR common input OR external control). B2/B4 (the separation-correct proxies) specified but never computed.
- **Sources.** Kolchinsky & Wolpert 2018 ✓ (semantic layer / intervention); Friston Markov blanket ⊙ (natural home of B2; instrumental vs realist reading must not be merged — Bruineberg/Biehl); Krakauer et al. 2020 ✓ (individuality = max propagated info — the B↔M weld AOP defines against; flame is the counter-witness); Campa–Dauxois–Ruffo 2009 ⊙ (long-range non-additivity → gravity anti-boundary).
- **Holes.** No worked separation computation; three-notion bundle (blanket/gradient-cost/causal); does not separate from Integration (0.83, §5).
- **Traps.** FALLEN IN: MI=boundary strength (still live). AVOID: conflating the three boundary notions ("a known error"); realist reading of an instrumental blanket.

## 2 · Drive — cleanest axis (forced × theorem)
- **Concept.** Sustained dissipation (trajectory irreversibility) holding the system off equilibrium; entropy-production rate, NOT free-energy throughput; no partition needed.
- **Math.** σ = lim (1/τ) D_KL(P_fwd ‖ P_rev) ≥ 0; Markov form σ = Σ π_j K_ij ln(K_ij π_j / K_ji π_i). Two forced spokes: TUR Var(J)/⟨J⟩² ≥ 2k_B/σ; D→M floor σ>0 ⇒ E>0.
- **Canon state.** Panel D1–D5, D5=σ canonical; v1.16 gloss "free-energy throughput" (P0-2) fixed → axis renamed Dissipation/Irreversibility. The σ>0⇒E>0 direction and the causal-boundary physics are the framework's only forced×theorem floor.
- **Sources.** Maes–Netočný / Seifert 2012 ⊙ + Roldán–Parrondo 2012 ✓ (σ=KLD); Barato–Seifert 2015 ✓ (TUR, classical-Markov-scoped); Still–Sivak–Bell–Crooks 2012 ✓ (thermodynamics of prediction → floor reaches predictive memory and stops); Battle et al. 2016 ✓ (cells) + Lynn et al. 2021 ✓ (brain) measured σ; Prigogine ? (active vs passive).
- **Holes.** Sector-split (why exactly two forced spokes) proven only OU/Markov — generalization FRONTIER; σ grain-relative (coarse-graining hides currents, ~70× swings); sign of current's lifetime effect is geometry-set.
- **Traps.** FALLEN IN: σ=free-energy throughput; persistence=occupancy (current-blind — retracted ceiling result). AVOID: E vs "excess entropy production" name collision (a spurious gate positive came from exactly this).

## 3 · Memory — numerator unsettled
- **Concept.** Information the present carries constraining its own future; computable given a numerator.
- **Math.** E = I(past;future) excess entropy; Cμ = H[causal states] statistical complexity; Ξ = Cμ⁺−Cμ⁻ causal irreversibility. Generically E ≤ Cμ. Order-1 Gaussian: E = I(X_{t-1};X_t).
- **Canon state.** Panel M1=E, M2=Cμ, M3 active storage, M4 retention depth, M5 semantic. Drive floor lands on M1 only. Time-grain relativity sharpest here: E defined only for stationary process; star's E undefined until clock named — the flagship sits where the Memory law is undefined (nuclear clock).
- **Sources.** Crutchfield–Feldman 2003 ✓ (E, = predictive information Bialek et al. 2001 ⊙); Shalizi–Crutchfield 2001 / Crutchfield–Young 1989 ? (Cμ, ε-machines); Crutchfield–Ellison–Mahoney 2009 ~ (Ξ); Still et al. 2012 ✓ (only predictive memory is free); Vazza 2020 ⊙ (cosmic-web complexity, grain).
- **RECOMPUTE DISCREPANCY (major).** Canon: Memory near-orthogonal to B and I, |Spearman|<0.05. My recompute (3000 VAR(1), E=I(X_{t-1};X_t)): **Spearman ≈ 0.61 with both** — NOT orthogonal. Likely the canon's <0.05 needs the Faes–Marinazzo–Stramaglia 2017 ⊙ time-lagged-covariance construction, which decorrelates from instantaneous coupling; the naive lagged MI does not. "Memory is free of B and I" is UNVERIFIED until that exact construction is reproduced.
- **Holes.** Numerator choice E vs Cμ (spore forces Cμ; floor only touches E); E loses *definition* off-stationarity; near-orthogonality unreproduced.
- **Traps.** FALLEN IN: E as "stored memory" (it's predictive; depth≠floor). AVOID: quoting E without the clock; E / "excess entropy production" collision.

## 4 · Integration — no canonical measure
- **Concept.** Degree to which many parts act as one irreducible whole; partition-dependent AND no single canonical measure; source of the fake T2 "win."
- **Math.** TC = Σ H(X_i) − H(X) (Watanabe); O-information Ω (signed: <0 synergy, >0 redundancy); Φ_MIP = min over partitions [whole − Σ parts]. Default TC (non-neg, monotone, closed-form Gaussian). No exact Integration value load-bearing — directional only.
- **Canon state.** Panel I1=TC, I2=O-info, I3=Φ_MIP (scoped static-Gaussian), I4 dynamic/causal, I5 modularity. Φ_MIP (v1.12) tells one-vs-many for a fixed partition only; non-stationary/critical payoffs need a phase transition the Gaussian setting lacks.
- **Sources.** Watanabe 1960 ? (TC); Rosas et al. 2019 ✓ (O-info); Mediano–Seth–Barrett 2019 ✓ (six Φ measures, no two agree, some negative, ranks survive not values); Comolatti–Hoel 2025 ⊙ (measures of causation are near-rediscoveries — direction survives, magnitude doesn't); IIT origin Tononi/Oizumi ?; Koashi–Winter ? (macroscopic integration must run on classical correlation, not entanglement — AOP already uses MI, on the right side). Resolvability limit grounded in sloppiness: Gutenkunst 2007 / Waterfall 2006 / Transtrum–Sethna 2015 ✓.
- **Holes.** No canonical measure (six Φ's); Φ_MIP scoped static-Gaussian; mask-resolvability tradeoff blurs strongly-integrated systems (a specified failure family — FIG D).
- **Traps.** FALLEN IN: coalition/Möbius = integration signal (T2 recovered the same 13 pairs a plain screen finds — added nothing). AVOID: TC as irreducible unity (redundant copies inflate it); measure-shopping for a sign; entanglement entropy for macroscopic integration.

## 5 · Separability — recomputed
| Canon claim | Recomputed | Verdict |
|---|---|---|
| B–I share a plane, corr ≈ 0.83 | Spearman 0.834 (3000 VAR(1)) | REPRODUCED |
| Memory near-orthogonal, \|corr\|<0.05 | Spearman ≈ 0.61 | DID NOT REPRODUCE |
| σ>0 ⇒ E>0, converse fails | σ≈0, E=0.70 at detailed balance | REPRODUCED |
| Divergence-free current moves lifetime ~5.7× | 5.4×, occupancy flat to 1e-15 | REPRODUCED |

**Phase-2 read.** B and I are not separable on the natural Gaussian construction — Phase-2 target #1. Memory's independence is not established under the obvious proxy — reproduce the Faes construction before "Memory is free" can stand. Two of four axes are in question at the definitional level; this is why the axis audit had to precede separability. Frontier (death has two faces): NESS collapse vs bifurcation + critical slowing (Scheffer 2009 ?); husk-vs-corpse (floor-reachability at drive-failure) appears to be AOP's own synthesis.

## 6 · Master holes & traps
Fallen in: MI=boundary strength (live); σ=throughput (fixed); persistence=occupancy (retracted); coalition/Möbius=integration (closed); self-graded benchmark (caught by recompute); Memory-orthogonality asserted robust (unreproduced). Avoid: proxy inheriting target's name; E/"excess entropy production" collision; quoting grain-relative magnitudes without D; realist reading of instrumental blanket; measure-shopping on Integration; reading a self-consistency demo as a could-have-failed test. Ranked open holes: (1) B–I collapse; (2) Memory independence unreproduced; (3) semantic mask salvage; (4) numerator E vs Cμ + off-stationarity; (5) sector-split generality.

## 7 · References, graded
1 Kolchinsky & Wolpert 2018 Interface Focus 8(6):20180041 ✓ · 2 Krakauer et al. 2020 Theory Biosci 139:209 ✓ · 3 Bertschinger–Olbrich–Ay–Jost 2008 Biosystems 91:331 ~ · 4 Seifert 2012 Rep Prog Phys 75:126001 ⊙ · 5 Roldán & Parrondo 2012 ✓ · 6 Barato & Seifert 2015 PRL 114:158101 ✓ · 7 Still–Sivak–Bell–Crooks 2012 PRL 109:120604 ✓ · 8 Battle et al. 2016 Science 352:604 ✓ · 9 Lynn et al. 2021 PNAS 118:e2109889118 ✓ · 10 Crutchfield & Feldman 2003 Chaos 13:25 ✓ · 11 Shalizi–Crutchfield 2001 / Crutchfield–Young 1989 ? · 12 Crutchfield–Ellison–Mahoney 2009 PRL 103:094101 ~ · 13 Bialek–Nemenman–Tishby 2001 ⊙ · 14 Watanabe 1960 ? · 15 Rosas et al. 2019 PRE 100:032305 ✓ · 16 Mediano–Seth–Barrett 2019 Entropy 21:17 ✓ · 17 Comolatti & Hoel 2025 ⊙ · 18 Faes–Marinazzo–Stramaglia 2017 Entropy 19:408 ⊙ · 19 Campa–Dauxois–Ruffo 2009 Phys Rep ⊙ · 20 Gutenkunst 2007 / Waterfall 2006 PRL / Transtrum–Sethna 2015 JCP 143:010901 ✓ · 21 Vazza 2020 ⊙ · 22 Prigogine (Nobel 1977) ? · 23 Scheffer et al. 2009 Nature 461:53 ? · 24 Koashi–Winter 2004 ? · 25 "Causal Leverage Density" 2024 arXiv 2407.07335 ✓
