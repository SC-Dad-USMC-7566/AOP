# AOP — Four-Axis State Report (canon v1.19) — REV.2

**Prime, 20 July 2026, rev.2.** Supersedes the morning version (`AOP_FourAxis_State_Report_20260720.md` — safe to prune). Reframed after Ben's steer: **dependence between axes is a finding to map, not a failure to fix.** The test is dissociability (does each axis carry a residual the others don't) and structure (what *is* the relationship) — not orthogonality. Rendered companion with typeset math + figures: `AOP_FourAxis_State_Report_20260720_rev2.html`; analysis code `aop_depmap.py` + `aop_figs.py`.

Grading: SETTLED / SYNTHESIS / FRONTIER / DEFECT; verification ✓ primary · ~ named · ⊙ canon-inherited · ? unverified.

## 0 · State of the canon
AOP is a Perspective/atlas (target *Interface Focus*). Synthesis: persistence = lifetime (MFPT out of the viable set, not occupancy), resisted along four non-commensurable relative-entropy axes. Two layers (syntactic coupling graph + semantic mask). Panel architecture (ADR-001): each axis a family of proxies under declaration tuple D. Governing line — **"four distinguishable axes, not four independent ones"** — is correct; §5 maps the dependence instead of forcing orthogonality. The only canon line needing change is Fig T's "|corr|<0.05," which overclaims independence.

## 1 · Boundary — DEFECT (lead scalar), B–I relationship reframed
- Lead-scalar defect stands: Table 1 still leads with I(in;out)=B5, which ADR-001 retired; B2 (screening)/B4 (cost) specified, never computed. This is the genuinely broken thing and the top fix — it mis-scores the concept regardless of the couplings.
- **B–I is nested, not a collapse.** Exact identity (verified 1.8e-15 over 4000 systems): TC = I(in;out) + TC_in + TC_out. Boundary is the cross-cut slice of Integration; the rest is within-side structure. The 0.83 correlation is this identity. Modelling choice: report Boundary separately only where the cross-cut piece specifically carries weight.

## 2 · Drive — cleanest axis [unchanged]
σ = lim (1/τ) D_KL(P_fwd‖P_rev). Forced spokes: TUR; σ>0⇒E>0. Sources: Seifert 2012 ⊙ / Roldán–Parrondo ✓ / Barato–Seifert 2015 ✓ / Still 2012 ✓ / Battle 2016 ✓ / Lynn 2021 ✓. Traps fallen in: σ=throughput (fixed), persistence=occupancy (retracted). Avoid: E vs "excess entropy production" collision.

## 3 · Memory — the MOST distinct axis (reframed)
- Math: E = I(past;future); Cμ = H[causal states]; Ξ = Cμ⁺−Cμ⁻. Order-1 Gaussian E = I(X_{t-1};X_t). Spore forces E vs Cμ apart. Sources: Crutchfield–Feldman 2003 ✓; Still 2012 ✓; Vazza 2020 ⊙.
- **Dependence map result (replaces the morning "discrepancy" framing).** Memory correlates ≈0.61 with B and I across random systems, but this is *shared coupling strength*: partial out coupling and Memory's tie to Boundary vanishes (−0.05); control for the third axis and partials fall to ~0.23. Memory carries **59% unique rank-variance** — more than B or I. It dissociates completely by construction: strongly-coupled-but-memoryless (E≈0 at high B,I) and pure-memory (E large at B=I=0). Memory earns its place emphatically. Canon edit: reword Fig T's "|corr|<0.05" to the measured dependence. Faes–Marinazzo–Stramaglia 2017 ⊙ is the tool for *mapping* the relationship, not decorrelating it away.
- Holes: numerator E vs Cμ (spore forces Cμ; floor touches only E); E loses definition off-stationarity (star, nuclear clock). Traps: E as "stored memory" (it's predictive); quoting E without the clock.

## 4 · Integration — no canonical measure [unchanged]
TC (Watanabe); O-info (Rosas 2019 ✓, signed); six Φ's disagree (Mediano–Seth–Barrett 2019 ✓; Comolatti–Hoel 2025 ⊙ — direction survives, magnitude doesn't). Φ_MIP scoped static-Gaussian. Resolvability blur grounded in sloppiness (Gutenkunst 2007 / Waterfall 2006 / Transtrum–Sethna 2015 ✓). Traps fallen in: coalition/Möbius=integration (T2 added nothing). Avoid: TC as unity; measure-shopping for a sign; entanglement entropy (use classical MI, Koashi–Winter).

## 5 · The dependence map (recomputed, 4000 VAR(1) + corners)
**Exact identity:** TC = I(in;out) + TC_in + TC_out (max err 1.8e-15). Boundary = cross-cut slice of Integration.

| Pair | Raw Spearman | Partial | Reading |
|---|---|---|---|
| B–I | 0.83 | 0.73 (control M) | direct, shared-substrate (nesting identity) |
| B–M | 0.61 | 0.24 (ctrl I); −0.05 (ctrl coupling) | correlated only via coupling strength → independent when removed |
| I–M | 0.61 | 0.22 (ctrl B); −0.62 (ctrl coupling) | shared-driver; mild tradeoff at fixed coupling (suggestive) |

**Unique residual (R² explained by other two → unique):** Memory 0.41→**0.59** (most distinct); Boundary 0.71→0.29; Integration 0.71→0.29.

**Dissociation corners (B, I, E):** sealed modules (0, 1.53, 0) = I without B; cross-cut only (1.01, 1.01, 0) = B=I with no internal; all-coupled memoryless (0.29, 0.73, 0) = coupling without E; pure memory (0, 0, 4.98) = E alone. Every axis comes apart.

**Other reproductions stand:** σ>0⇒E>0 with converse failing (σ≈0, E=0.70 at detailed balance); divergence-free current moves lifetime 5.4× while occupancy flat to 1e-15.

**Forced edge (keep, don't fight):** Drive→Memory, σ>0⇒E>0 (Still et al. 2012 ✓). The map's job is to type each edge (forced / shared-driver / nested / free), not sever it.

Read: correlated, dependent, every one still its own thing = "distinguishable, not independent," measured. Phase 2 becomes *characterise the couplings*, not *which axes survive*.

## 6 · Master holes & traps (updated)
Fallen in: MI=boundary strength (live — top fix); σ=throughput (fixed); persistence=occupancy (retracted); coalition/Möbius=integration (closed); self-graded benchmark (caught by recompute); **claiming more independence than measured** (Fig T |corr|<0.05 — reword; don't mistake dissociability for orthogonality). Avoid: proxy inheriting target's name; E/"excess entropy production" collision; grain-relative magnitudes without D; realist reading of instrumental blanket; measure-shopping on Integration; self-consistency demo read as a could-have-failed test.
Ranked open work: (1) characterise the couplings + reword the one over-strong line (nothing collapses); (2) **Boundary lead-scalar defect** (the real break); (3) semantic mask salvage; (4) numerator E vs Cμ + off-stationarity; (5) sector-split generality.

## 7 · References — 25 graded entries; see rev.2 HTML and the morning MD.
MDEOF
