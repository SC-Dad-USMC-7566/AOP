# Axis M — Memory. Deep dossier (canon v1.19)

Startup check — 2026-07-20
[✓] AOP Charter — v1.0
[✓] AOP Canon (the paper) — v1.19 (clean master)
[✓] AGENT_BRIEF (four-axis) + Operational Panels spec + State Report rev.2 + aop_depmap.py (rerun this session)
Drive connector: on (WebSearch/WebFetch used for new-literature verification).

---

## 1. The axis in one paragraph

**Memory** is the *time* dimension of persistence: how much of a persister's future is fixed by its
past. Its target is **predictive structure carried across time**; its lead formal quantity is the
**excess entropy E = I(X_past ; X_future)**, the past–future mutual information of computational
mechanics [Crutchfield & Feldman 2003 ⊙]. E is one of the two axes (with Drive) that is **cleanly
computable with no declared spatial partition** — but only *given* a numerator, and the numerator is
where the honesty lives. Memory is emphatically **not a single scalar**: the operational panel splits
it into five proxies (M1 predictive dependence E; M2 stored predictive state Cμ; M3 active information
storage; M4 retention depth; M5 semantic/load-bearing memory), and these can move independently. What
E does **not** measure is *storage*: E is the past–future **coupling**, not the amount a system must
physically hold to generate its future — that is M2 (statistical complexity Cμ), and E ≤ Cμ always,
with the gap being crypticity [Crutchfield, Ellison & Mahoney 2009 ⊙]. Two further limits are
structural, not incidental: E is **grain-relative in value and, uniquely on the time axis,
grain-relative in *definedness*** — it is defined only for a stationary process, so crossing a
non-stationarity does not rescale E, it removes it [Crutchfield & Feldman 2003 ⊙; §5]. Memory is the
**most distinct of the four axes** (0.59 unique rank-variance, more than Boundary or Integration); its
apparent ~0.61 correlation with Boundary and Integration is shared coupling strength only, and vanishes
when coupling is controlled.

---

## 2. The persister, per example

The mandate: name the **process** that persists, never the object. Memory's contribution is almost
always *stored predictive structure (Cμ)* or *predictive dependence (E)* — and the two come apart.

| Example | The persister (process) | The husk | Present-tense type (§9) | What Memory contributes |
|---|---|---|---|---|
| **Spore** | a **paused process** — architecture present, drive switched off, viability held in escrow (§11a) | the coat *read as a blueprint* (a description → would be dead, §4a) | **capacity** (semantics in escrow) | The standing witness that **Cμ ≠ E**: E ≈ 0 (near-zero drive, nothing predicts across the dormancy gap) while stored complexity Cμ is large. Persistence rides on **M2**, not M1. |
| **Crystal** | **was** the growth front — drive depositing lattice; once grown, drive → 0 | the lattice you hold: **memory made solid, semantics spent, terminal** | **configuration** (semantics spent) | Memory *frozen and spent*. A perfect lattice is periodic → **low, finite** Cμ = E = log(period): fully predictable, zero crypticity. "Memory made solid" is a metaphor, not large E. |
| **ε-machine / hidden-Markov process** | **the process itself** — the stationary generating structure (its causal-state machine) | any single sampled trajectory (a **record**, not the process) | **process** | The clean carrier that makes **M1 vs M2** concrete: E = I(past;future) is a property of the past–future coupling; Cμ = H[causal states] is what the process must *store* to stay statistically predictive. The pure-memory corner of the dependence map. |
| **Star** | the **self-regulating hydrostatic + fusion process** (Drive is the defining axis) | the ball of gas | **process** | Memory has **no single value**: E is defined on the **thermal (Kelvin–Helmholtz) clock** (stationary) and **undefined on the nuclear clock** (non-stationary, composition drifts). The definedness hole (Gap b) made physical. |
| **Flame** | the **process** — a boundary rebuilt each instant from current supply; no restoring force (§11a) | the current gas molecules (wholly replaced) | **process** | The **memoryless** pole: E ≈ 0, sharp boundary. The counter-witness that keeps **Boundary and Memory unwelded** — a maintained boundary a memory-maximizing individuality axis [Krakauer et al. 2020 ⊙] cannot score honestly. |

Per-example "persister / husk" lines, for the record:
- **Spore:** the persister is a *paused process* (life paused); the husk is the coat *if you mistake
  it for a blueprint*. Diachronic test (§4a): it restarts **itself** from its own held state →
  **same process**, paused not stopped. Held-state ≠ description.
- **Crystal:** the persister *was* the growth front; the husk is the lattice — the corpse of the
  process, not the process.
- **ε-machine:** the persister is the process/generating structure; the husk is a printed
  realization — a record something external would have to re-enact (a *new* process, §4a).
- **Star:** the persister is the hydrostatic+fusion loop; the husk is the gas. Its Memory is
  un-nameable until the clock is declared.
- **Flame:** the persister is the process; the husk is this instant's gas. Interrupt supply and it is
  gone — no held state to restart from (unlike the spore).

---

## 3. The axis independently

**The settled core.** E = I(past;future) is a bona-fide mutual information and is **the same object**
as **predictive information** [Bialek, Nemenman & Tishby 2001 ✓] and *effective measure complexity* —
BNT verify (I read the passage) that "mutual information between all of the past and all of the future
… is known also as the excess entropy, effective measure complexity, stored information." It is the
**subextensive part of the block entropy**: S(T) = S₀·T + S₁(T), with E = lim_{T→∞} S₁(T). This is
SETTLED and is the backbone of M4 below. **[SETTLED — E is the past–future MI / predictive
information; named published identity.]**

**The panel (M1–M5), sharply distinguished** — this is the axis's most important internal structure,
and conflating the members is the axis's central trap:

- **M1 — Predictive dependence: E = I(past;future).** How much of the future is fixed by the past.
  *Predictive coupling, not storage.* The **only** proxy the D→M floor touches.
- **M2 — Stored predictive state: Cμ = H[causal states].** The information a system must physically
  *hold* to be statistically predictive. **E ≤ Cμ**; the gap χ = Cμ − E is **crypticity** [Crutchfield,
  Ellison & Mahoney 2009 ⊙]. The spore lives here.
- **M3 — Active information storage: A_X = I(X_past ; X_next).** Predictive information about *only the
  next* value, complementary to the entropy rate [Lizier, Prokopenko & Zomaya 2012 ~ — definition read
  this session in Wibral, Lizier et al. 2014 ✓, which attributes and quotes it]. Where E is
  past↔*all* future, AIS is past↔*next step*; the natural bridge to transfer entropy.
- **M4 — Retention depth: the predictive-information curve E(T) / memory kernel.** BNT ✓ establish
  **three growth regimes** of I_pred(T): bounded (finite memory), **logarithmic** (K/2·log T, a
  K-parameter model), and **power-law** (T^{m/(m+1)}, nonparametric). Depth, not just presence.
- **M5 — Semantic / load-bearing memory.** Viability drop when the memory-bearing variable is
  scrambled (the mask, §3). This is where "which memory *matters*" is answered — and it is
  observer-relative, an interval not a point.

**The D→M floor forces M1 only.** σ > 0 ⇒ E > 0 is a **floor on predictive dependence**, and there is
**no floor on M2–M5**. The spore is the standing proof: near-zero σ, deep Cμ (§11, §4).

**Cleanest computable proxy + worked numbers.** For a stable VAR(1) Gaussian process, order-1 excess
entropy is closed-form, E = I(X_{t-1};X_t) = ½[2·logdet Σ − logdet J], J the lag-joint covariance
(aop_depmap.py, rerun this session). The dissociation corners (B, I, E), reproduced exactly:

| Constructed corner | B | I | **E** | reading |
|---|---|---|---|---|
| pure memory (diagonal dynamics, no cross-coupling) | 0.000 | 0.000 | **4.982** | **E alone** — memory with zero Boundary and Integration |
| all-coupled memoryless (A=0, high static corr) | 0.294 | 0.728 | **0.000** | strong B,I with **E = 0** |
| sealed modules | 0.000 | 1.532 | 0.000 | I without B, no memory |
| cross-cut only | 1.010 | 1.010 | 0.000 | B = I, no memory |

Memory **dissociates completely by construction**: pure-memory (E large at B=I=0) at one extreme,
strongly-coupled-but-memoryless (E = 0 at high B, I) at the other. **[analytic-model-result; computed
this session.]**

---

## 4. Interactions with the other three axes

Typed against the dependence map (aop_depmap.py, 4000 stable VAR(1) systems + constructed corners),
reproduced exactly this session.

### Memory ↔ Drive — **forced floor, on M1 only** (the one law that touches Memory)
σ > 0 ⇒ E > 0: sustained dissipation forces a strictly positive past–future MI, a **scoped corollary
of trajectory irreversibility** [Parrondo, Van den Broeck & Kawai 2009 ⊙], via E = 0 ⟺ i.i.d. ⇒
time-reversible ⇒ σ = 0, contrapositive σ > 0 ⇒ E > 0. **[forced (direction) × theorem/corollary.]**
Three scope conditions (§4): (i) σ and E read on the **same complete description** (coarse-graining
can hide a current so E reads ~0 while the full dynamics dissipate); (ii) **stationary** process;
(iii) it forces a **floor (E > 0), not depth**. The converse fails — a detailed-balance oscillator has
σ = 0 with E > 0 (remembers for free). The **thermodynamics of prediction** [Still, Sivak, Bell &
Crooks 2012 ✓ (canon-relied)] sharpens it: dissipated work is proportional to the **nonpredictive**
retained memory, so only predictive memory is free. **The floor stops at E and does not reach
M2–M5:** the pre-registered sector split shows the causal irreversibility Ξ = Cμ⁺ − Cμ⁻ = **0 at every
drive**, and Cμ magnitude covaries only *weakly* through the **symmetric** sector (≈1 % as σ̇ moves
~20×), as shared input, not through the current. **[Sector-split: SYNTHESIS, secure in two model
classes (Gaussian OU, finite Markov); generalization FRONTIER.]**

### Memory ↔ Boundary — **free / dissociable** (independent once coupling is removed)
Raw Spearman **B–M = 0.612**. But this is **shared coupling strength**: partial controlling for
Integration falls to **0.242**, and partial **controlling for raw coupling strength = −0.046** —
Memory's tie to Boundary **vanishes**. The one account that welds them, autonomy-as-boundary
[Krakauer et al. 2020 ⊙], does so *by construction* (the boundary is defined as the partition
maximizing a memory quantity); the **flame breaks the weld** (sharp boundary, E ≈ 0). **[dissociable
(free); the weld is definition/stipulated, not law. B–M|coupling = −0.05, computed this session.]**

### Memory ↔ Integration — **shared-driver + mild tradeoff at fixed coupling (suggestive)**
Raw Spearman **I–M = 0.607**; partial controlling for Boundary **0.223**; partial **controlling for
coupling = −0.621**. So the raw positive is again shared coupling strength, and *at fixed coupling*
there is a **mild negative tradeoff** — memory and integration behave as **substitutable strategies**,
consistent with bet-hedging theory [Rivoire & Leibler 2011 ⊙] (store the environment in memory, or
spread it across integrated parts). This is the strongest of the three non-energy signals but remains
**suggestive**, and it depends on the contested Integration measure (§6). **[shared-driver /
dissociable; I–M|coupling = −0.62, computed this session. SYNTHESIS.]**

### Memory's unique standing
R² of Memory explained by (B, I) = **0.406 → unique rank-variance 0.59**, versus 0.29 for Boundary and
0.29 for Integration. **Memory is the most distinct axis.** It is a mutual information on the
**time-lagged** covariance — a genuinely different object from the instantaneous cuts that Boundary and
Integration read off the same static covariance (which is why *those two* nest at 0.83 via the exact
identity TC = I(in;out) + TC_in + TC_out). Memory earns its place emphatically. **[analytic-model-
result; computed this session.]**

---

## 5. Holes, traps, and DEFECTs

### DEFECT (canon edit required) — Fig T / Table 2 over-claim Memory's independence
The canon states in **three places** that Memory's raw correlation with B and I is below 0.05:
- §4 body: "*across random dynamics its correlation with each is below 0.05*";
- Fig T caption: "*Memory spreads freely of the Boundary–Integration plane (pairwise |corr| < 0.05)*";
- Table 2, M–I row: "*near-orthogonal across random dynamics (|corr| < 0.05)*".

**This is wrong.** The measured **raw** Spearman is **B–M = 0.61, I–M = 0.61**. The 0.05 figure is the
partial correlation *after controlling for coupling strength* (B–M|coupling = −0.05), **not** the raw
pairwise correlation. The canon reports a *conditioned* number as if it were the *unconditioned* one,
and thereby **over-claims orthogonality**. The correct, defensible statement — and it is *stronger*,
not weaker, for the axis — is: **Memory correlates ~0.61 with B and I as shared coupling strength;
controlling for coupling that tie vanishes (B) or inverts to a mild tradeoff (I); Memory carries 0.59
unique rank-variance (the most of any axis) and dissociates completely by construction.** Recommended
rewording of the Fig T caption: *"Memory shares only coupling strength with the Boundary–Integration
plane: raw |corr| ≈ 0.61, but partialling out coupling drives B–M to −0.05 and I–M to −0.62, and
Memory carries 0.59 unique rank-variance — the most distinct of the four axes."* **[DEFECT — dissociability
mistaken for orthogonality; fix is a rewording, the underlying finding survives and strengthens.]**

### HOLE (a) — the numerator: E vs Cμ
The D→M floor forces **E**; the spore forces **Cμ**. Which is *the* Memory numerator, and when? The
panel *names* both (M1, M2) but does not adjudicate which carries persistence. The literature already
supplies the connective tissue: E ≤ Cμ always, and **crypticity χ = Cμ − E** is the exact, computable
gap [Crutchfield, Ellison & Mahoney 2009 ⊙ — "Time's barbed arrow"]. A cryptic process (χ large)
stores far more than its past–future MI reveals — which is precisely the spore's regime and the reason
E reads it as inert while Cμ reads it as rich. **The honest position: E is the *forced* numerator (a
law touches it), Cμ is the *persistence-relevant* numerator for stored-structure persisters, and χ is
the diagnostic that tells you when they diverge.** Not yet stated this way in the canon.
**[FRONTIER-leaning SYNTHESIS; closable by synthesis, no new computation — the machinery is settled.]**

### HOLE (b) — E loses **definition** off-stationarity (a real definedness hole)
E is defined only for a **stationary** process [Crutchfield & Feldman 2003 ⊙]. This is not a rescaling
limit like σ's spatial-grain relativity — cross a non-stationarity and E does not change value, it
**ceases to exist**. The star makes it physical (thermal clock: E defined; nuclear clock: undefined),
but the hole is general and bites the systems AOP most cares about: **developing organisms** (ontogeny
is non-stationary by construction), **aging**, and any lineage on an evolutionary clock. The flagship
Memory *law* (the D→M floor) requires stationarity, so it too goes silent exactly here. A candidate
partial fix exists and should be pursued: **local / pointwise information dynamics** — local active
information storage [Lizier, Prokopenko & Zomaya 2012 ~] is defined *at each time step* and does not
require global stationarity, giving a time-resolved memory measure where E is undefined. **[FRONTIER —
genuine definedness hole; partially closable by synthesis (local AIS), fully open for a stationarity-free
E analogue.]**

### Traps (some already half-fallen-into in the prose)
- **E as "stored memory."** E is **predictive dependence**, not storage. The panel is careful (M1
  says "predictive dependence"), but §11's "memory made solid" (crystal) and loose "stored structure"
  phrasing invite the slip. Storage is M2 (Cμ) / M3 (AIS). *Say "predictive dependence" for E; reserve
  "stored memory" for Cμ.*
- **Quoting E without naming the clock/grain.** E has no observer-free value; on the time axis its very
  definedness is grain-relative. The star is the standing example — its Memory is un-nameable until the
  clock is declared. Any E number in the paper must carry its temporal grain in the declaration tuple D.
- **E vs "excess entropy production" collision.** E = I(past;future) (Memory axis) must not be confused
  with steady-state **excess entropy production** (a Drive-axis quantity). The canon flags this in §4;
  keep the flag.
- **Crystal "memory made solid" mis-scored.** A perfect periodic lattice has *low, finite* Cμ = E =
  log(period) and zero crypticity — it is fully predictable, not memory-rich. The persistence-relevant
  reading is *spent* semantics (terminal), not *large* memory.

---

## 6. Gap list for this axis

1. **Which numerator carries persistence — E or Cμ — and when?** (a) Literature likely answers the
   *machinery*: computational mechanics gives E ≤ Cμ and crypticity χ = Cμ − E [Crutchfield–Ellison–
   Mahoney 2009 ⊙]; the *persistence adjudication* (Cμ for stored-structure persisters, E where a law
   must bite) is AOP's to state. (b) FRONTIER-leaning SYNTHESIS. (c) **Synthesis only** — no new
   computation; write χ into the panel as the E–Cμ diagnostic.
2. **A memory measure that survives non-stationarity.** (a) Candidate fields: local/transient
   information dynamics (local AIS [Lizier et al. 2012 ~]; local transfer entropy [Schreiber 2000 ?]),
   time-varying / windowed complexity, and the continuous-time storage/transfer formalism (Spinney,
   Lizier et al. 2018 ?). (b) FRONTIER (real definedness hole). (c) **Synthesis to adopt local AIS as a
   scoped M-proxy for non-stationary persisters; new computation** to demonstrate it on a non-stationary
   worked case (developing OU system / the star's nuclear clock).
3. **Fix the Fig T / Table 2 over-claim.** (a) No literature needed — it is a misreport of AOP's own
   depmap output (raw 0.61 vs partial 0.05). (b) DEFECT. (c) **Synthesis only** — reword three passages
   to the measured dependence; the finding strengthens the axis.
4. **Does the D→M floor generalize beyond the two tested model classes?** (a) Likely reachable via
   general fluctuation-theorem / hidden-process results (Crutchfield computational mechanics; general
   stochastic thermodynamics), but the sector-split proof is currently OU + finite-Markov only. (b)
   FRONTIER. (c) **New computation / proof** — the generalization step the canon already flags.
5. **M4 retention-depth regime for real persisters.** (a) BNT's ✓ three growth regimes (bounded / log /
   power-law) classify *how deep* a persister's memory runs; mapping AOP's worked cases onto that
   trichotomy is undone. (b) SYNTHESIS. (c) **Small new computation** — E(T) curves for the spore-type
   and cell-type OU systems already in the LT figures.
6. **M5 semantic memory computed on a memory-bearing edge.** (a) The mask method exists (Figure MW/LT);
   it has not been run with the *memory variable* as the scrambled target to read Memory's semantic
   weight directly. (b) SYNTHESIS. (c) **New computation** — reuse the LT cell-type OU system, scramble
   the slow reference (a memory node) and read the viability interval.

---

## 7. Citations used, with verification markers

**Verified this session (✓ — read the relied-on passage):**
- **Bialek W, Nemenman I, Tishby N. Predictability, Complexity, and Learning. *Neural Computation*
  13, 2409–2463 (2001).** ✓ — confirmed predictive information = I(past;future) = **excess entropy** =
  subextensive block entropy; three growth regimes (bounded / logarithmic K/2·log T / power-law
  T^{m/(m+1)}). Read: Princeton PDF (wbialek/our_papers/bnt_01a.pdf). *New literature — supports M4 and
  the E-as-predictive-information identity.*
- **Wibral M, Lizier JT, et al. Local active information storage as a tool to understand distributed
  neural information processing. *Front. Neuroinform.* 8:1 (2014).** ✓ — read the AIS definition
  A_X = I(X_past^{(k)}; X_next) and its stated distinction from excess entropy; attributes AIS to
  Lizier, Prokopenko & Zomaya 2012. *New literature — supports M3 and Gap 2.*

**Canon-inherited, pre-verified (⊙):**
- Crutchfield JP, Feldman DP. *Chaos* 13, 25–54 (2003). ⊙ — E defined only for stationary process
  (Gaps a, b; §5).
- Still S, Sivak DA, Bell AJ, Crooks GE. *PRL* 109, 120604 (2012). ⊙ — thermodynamics of prediction;
  dissipation pays for nonpredictive memory (§4, D→M).
- Crutchfield JP, Ellison CJ, Mahoney JR. *PRL* 103, 094101 (2009). ⊙ — "Time's barbed arrow";
  crypticity χ = Cμ − E, causal irreversibility Ξ = Cμ⁺ − Cμ⁻, stored information (M2, Gap a, sector split).
- Vazza F. *MNRAS* 491, 5447–5463 (2020). ⊙ — statistical complexity quoted at a declared temporal
  grain (~200 Myr) (§5, trap on grain).
- Parrondo JMR, Van den Broeck C, Kawai R. *NJP* 11, 073008 (2009). ⊙ — trajectory irreversibility =
  KL(fwd‖rev); the identity the D→M floor is a corollary of.
- Rivoire O, Leibler S. *J. Stat. Phys.* 142, 1124–1166 (2011). ⊙ — value of information; memory/
  integration as substitutable bet-hedging strategies (M–I).
- Krakauer D, Bertschinger N, Olbrich E, Flack JC, Ay N. *Theory Biosci.* 139, 209–223 (2020). ⊙ —
  information theory of individuality; autonomy-as-boundary weld broken by the flame (B–M).
- Faes L, Marinazzo D, Stramaglia S. *Entropy* 19, 408 (2017). ⊙ — closed-form Gaussian VAR info
  decomposition; the tool that *maps* the M–B/M–I relationship (not decorrelates it).
- Watanabe S. *IBM J. Res. Dev.* 4, 66–82 (1960). ⊙ — total correlation (Integration proxy, for the
  identity and corners).

**Named-only / lead (~, ?):**
- Lizier JT, Prokopenko M, Zomaya AY. Local measures of information storage in complex distributed
  computation. *Information Sciences* 208, 39–54 (2012). ~ — title/venue confirmed; **AIS definition
  read this session via Wibral et al. 2014 (✓), primary PDF blocked by an HTTPS→HTTP redirect.** Treat
  as strong lead for M3 / Gap 2, primary not yet read directly.
- Schreiber T. Measuring information transfer. *PRL* 85, 461 (2000). ? — transfer entropy; lead for
  M3 / directed memory. Not read this session.
- Kelly JL. A new interpretation of information rate (1956); Spinney RE, Lizier JT, Prokopenko M,
  continuous-time storage/transfer (*J. Stat. Mech.* 2018). ? — leads for bet-hedging ancestry and the
  non-stationary/continuous-time memory measure (Gap 2). Not read this session.

**Computed this session (analytic-model-result):**
- aop_depmap.py rerun — raw Spearman B–M 0.612, I–M 0.607; partials B–M|coupling −0.046, I–M|coupling
  −0.621; Memory unique rank-variance 0.59; corners pure-memory E = 4.982, all memoryless corners
  E = 0.000; identity max err 1.78e-15.
