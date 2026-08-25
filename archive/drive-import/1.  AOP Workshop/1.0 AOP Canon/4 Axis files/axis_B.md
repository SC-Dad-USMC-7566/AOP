# Axis B — Boundary: deep dossier (AOP canon v1.19)

**Startup check — 20 Jul 2026**
[✓] AOP Charter — v1.0 (read via session brief)
[✓] AOP Canon (the paper) — v1.19 (read §1–§6, §8, §9, §10, §11, §11a, §12 + Table 1/2/3 in full)
[✓] Operational Panels spec — Boundary panel B1–B5 read in full
[✓] Dependence map — `FourAxis_State_Report_rev2.md` §1, §5 + `aop_depmap.py` (identity, partials, corners) read
Drive connector: off (local files only).
Grading: SETTLED / SYNTHESIS / FRONTIER / DEFECT. Verification: ✓ read primary this session · ~ named/abstract only · ⊙ canon-inherited · ? unverified.

---

## 1 · The axis in one paragraph

**Boundary is the *space* axis of persistence: a maintained separation of interior from exterior, held over time.** It is not a substance and not a membrane you can point at; it is a computed difference across a *declared* inside/outside cut, inferred from residues and screened flows, never observed directly (canon §2). Formally it is **not a single scalar but a panel** of proxies under the declaration tuple D (Panels spec): B1 state contrast `D_KL[p(X_in)‖p_ref(X_out)]`; **B2 interface mediation** `I(X_in;X_out | F)` (screening — the residual dependence *after* conditioning on the interface); B3 leakage/permeability (physical flux across the interface); **B4 maintenance burden** (work/entropy-production to hold the contrast against leakage over τ); B5 cross-boundary dependence `I(X_in;X_out)`. Boundary is one of the two **soft** axes (with Integration): it requires a declared partition and the answer moves with it (canon Table 1). **What it measures:** statistical organization across a chosen cut, and — in the physically loaded proxies — whether that cut is *screenable* and what it *costs* to hold. **What it does NOT measure:** a physical membrane (the proxy names statistical dependence, not a wall — canon [P0-2]), separation *per se* (high `I(in;out)` means the two sides are *coupled*, i.e. dependent, which is the opposite of sealed), and it does not by itself tell you the boundary is load-bearing (that is the semantic mask's job, §3). The flame makes the softness maximal: its thermal, ionization, and luminous edges genuinely differ, so "the" boundary is observer-relative before any measurement is taken (§11).

---

## 2 · The persister, per example (identification mandate)

For each case: the boundary is a property **of the process**, not of the object you can hold. The husk is not the persister.

| Example | The persister (process) | The husk / corpse | Present-tense type (§9) | What Boundary contributes to *its* persistence |
|---|---|---|---|---|
| **Flame** | a combustion front continuously rebuilding a sharp interface from *current* supply; today's gas is wholly replaced from moment to moment | the current parcel of hot gas (already leaving) | **process** (keep a reaction above threshold) | Boundary is nearly the *whole* semantic story — a screenable EM/thermal skin re-drawn each instant; interrupt supply → no restoring force → gone (§11a "continue") |
| **Crystal** | *was* the growth front — drive depositing lattice order across the solid/solution interface | the grown lattice (memory made solid; drive→0; terminal) | **configuration** (stay in a shape) | Boundary's semantics are **spent**: the interface did its work while growing; the static facet now bounds nothing that is still being maintained |
| **Spore** | a *paused* process — the boundary-maintenance architecture is structurally present but switched off (life paused, §11a tier two) | — (not a corpse: the coat is a lock awaiting its key, not a description) | **capacity** (stay able to act) | Boundary is held **in escrow**: the coat is a present, screenable barrier at ~zero maintenance cost; it is present-structure now, not a promise — distinguish held-state (paused) from a mere blueprint (dead, §4a) |
| **Bound H atom** | the bound electron–proton process holding a localized interior with a present tense (minimal admitted persister, §8, Fig 4) | — (a free electron + free proton is no persister: unbound, no interior) | **configuration/process** | **Two boundaries at once**: a cheap *screening* EM skin (electron in the Coulomb well, ~zero drive) giving an interior, plus an unscreenable *causal* boundary (its worldline's light cone). Screening boundary = material/local/probeable; causal = non-material/global |
| **Star** | the self-regulating hydrostatic+fusion process (Drive is defining; kill fusion → dies on a Kelvin–Helmholtz time) | the ball of gas (the object is not the persister) | **process** (corrects, model-free → not alive, §11a) | **Two *load-bearing* boundaries of different force-types**: the unscreenable *causal* boundary from gravitational binding, AND a genuine *screening* photospheric skin (interior optically thick, radiation random-walks out, inside conditionally independent of outside given the surface). Scramble the photospheric opacity and it stops being a star (§8) |
| **Galaxy** | a gravitationally bound, membrane-free process — mostly empty, starlight free-streams, nothing screened | — (no husk: there is no material skin to leave behind) | **configuration/process** on the galactic clock | Boundary is **gravity alone**, and gravity is the *anti-boundary* interaction (§8): unscreenable, infinite-ranged, non-additive. The only boundary is causal. This is the clean "gravity is the entire boundary" case the star is *not* |

**Persister-is / husk-is lines (the mandate, explicit):**
- Flame — *the persister is the combustion front (a boundary rebuilt each instant); the husk is the gas parcel already leaving it.*
- Crystal — *the persister was the growth front; the husk is the lattice you hold — the boundary's corpse, semantics spent.*
- Spore — *the persister is the paused boundary-maintenance architecture; there is no husk, because the coat is a lock, not a record.*
- Bound H atom — *the persister is the bound EM process holding an interior; the husk is a free electron and proton, which bound nothing.*
- Star — *the persister is the hydrostatic+fusion process; the husk is the gas ball — and it carries two live boundaries, causal and photospheric.*
- Galaxy — *the persister is the gravitationally bound process; there is no husk and no membrane — gravity is the whole (anti-)boundary.*

**Diachronic test (§4a), where it bites:** the flame passes by *continuity of instantiation* through total material turnover (Ship-of-Theseus form: same process, no original molecule) — its boundary is genidentical, not substance-identical. The spore restarts *itself* from its own held boundary architecture (paused, same process); a genome print of it would be a *description* (dead). The husk-crystal fails the present-tense check: nothing is being maintained across its interface *now*.

---

## 3 · The axis independently

### 3a. The settled core: screenability (§8) — Boundary's deepest, most defensible content

The one genuinely settled, non-partition-dependent thing Boundary says is **which interactions can make a boundary at all**, and it is a clean import from standard physics, gradable SETTLED:

- **A statistical boundary requires the interaction to be *screenable* (interruptible)** — inside conditionally independent of outside *given the interface*. This is exactly a **Markov blanket** condition: a variable is conditionally independent of all others given its blanket (Pearl 1988 ✓). So B2 = `I(X_in;X_out | F)` is not an ad-hoc proxy — it is the blanket/screening test written as a number, and a *perfect* screen drives B2 → 0. **[SETTLED — the blanket definition; SYNTHESIS — reading B2 as its scalarization.]**
- **Electromagnetism screens.** Opposite charges, a Faraday cage, a lipid membrane. The quantitative fact is the **Debye (Debye–Hückel) screening length**: mobile charges cloak a test charge so the bare Coulomb potential is *exponentially screened over λ_D*, beyond which its influence is negligible (Debye length, ✓). This is the physics under "EM builds membranes," and it makes screening a *length*, not a metaphor. **[SETTLED.]**
- **The strong force confines rather than screens; the weak force is intrinsically short-ranged (massive mediators).** Neither builds a statistical boundary at persister scales (§8). **[SETTLED.]**
- **Gravity is the anti-boundary interaction.** No negative mass, infinite range ⇒ unscreenable ⇒ *no* statistical boundary; its only boundary is causal (the worldline's light cone). And because gravity is long-range and therefore **non-additive** — the energy of a whole ≠ the sum of subsystem energies — subsystems never fully decouple, so gravity imposes an **unscreenable floor on Integration** (Campa, Dauxois & Ruffo 2009 ⊙). Negative specific heat / ensemble inequivalence are the thermodynamic signatures of the same non-additivity, and (canon §11 synthesis) the *same* property is the common root of the star's anti-boundary character, its Integration floor, and its self-regulation. **[SETTLED base + SYNTHESIS on the common-root reading.]**

This is the axis's strongest asset and it is under-exploited: screenability turns "declare a cut" from an arbitrary choice into a physically constrained one — you may only draw a *screening* boundary where a screenable interaction exists. Gravity-bound-but-radiatively-unscreened systems (the galaxy) are the limiting case where no screening cut is available at all.

### 3b. The panel and the cleanest computable proxy

The Gaussian VAR(1) machinery (Faes, Marinazzo & Stramaglia 2017 ⊙) gives Boundary's proxies in closed form on a declared cut. In `aop_depmap.py` the computed Boundary is **B5** specifically: `B = ½[logdet Σ_in + logdet Σ_out − logdet Σ] = I(X_in;X_out)`. This runs cleanly (4000 systems) and is the quantity behind every number below — but see §5: **B5 is the panel's *weakest* reading, and leading with it is the axis's DEFECT.** B1, B2, B4 are specified but **never computed** anywhere in the codebase or canon.

Worked numbers that exist (from `aop_depmap.py`, seed 20260720):
- **Dissociation corners (B, I, E)** confirm Boundary comes apart from the others by construction: *sealed modules* → (0, 1.53, 0): Integration with **zero Boundary**; *cross-cut only* → (1.01, 1.01, 0): **Boundary = Integration**, no within-side structure; *all-coupled memoryless* → (0.29, 0.73, 0): coupling without memory. **[SYNTHESIS, analytic-model-result.]**
- Boundary's **unique rank-variance = 0.29** (vs Memory 0.59, Integration 0.29): Boundary is the *least* distinct of the three — it shares a plane with Integration and carries the smallest residual the other two cannot predict. **[analytic-model-result; ✓ reproduced logic from code.]**

---

## 4 · Interactions with the other three axes

### 4a. Boundary ↔ Integration — **NESTED (an identity, not a correlation)**

The load-bearing fact. There is an **exact algebraic identity** (max err **1.8e-15** over 4000 systems, `aop_depmap.py`):

> **TC = I(in;out) + TC_in + TC_out**

i.e. total Integration decomposes into the **cross-cut slice** (`I(in;out)` = Boundary's B5) plus within-inside and within-outside integration. So **Boundary's lead proxy is literally a component of the Integration axis.** The raw Spearman B–I = **0.83** and the partial **B–I|M = 0.73** are not a coincidence to be explained away — they *are* this nesting identity showing up statistically (state report §5). Type: **nested.** **[SETTLED identity (algebraic); SYNTHESIS on the reading.]**

**What this means for reporting Boundary separately.** Because B5 is a slice of TC, reporting B5 as an independent "Boundary" score *double-counts the cross-cut mutual information already inside Integration.* Boundary (as B5) earns a separate line **only where the cross-cut slice specifically carries weight** — i.e. where the persistence-relevant structure lives *on* the in/out cut rather than *within* either side. The corners make the rule concrete: sealed modules (B=0, I high) → the cross-cut piece is empty, so Boundary is correctly silent and Integration says everything; cross-cut-only (B=I) → Boundary *is* Integration, and reporting both is pure redundancy. **The honest modelling default: report Boundary separately iff `I(in;out)` is a non-trivial fraction of TC *and* the question is about the separation itself** — and even then, prefer the proxies that are *not* slices of TC (B1, B2, B4; see §5).

### 4b. Boundary ↔ Memory — **FREE (dissociable; the weld is by construction, not law)**

Raw Spearman B–M = **0.61**, but this is *shared coupling strength*, not a real tie: partial **B–M|I = 0.24**, and controlling for raw coupling strength **B–M|coupling = −0.05** — Memory's link to Boundary **vanishes** once coupling is removed (state report §5, `aop_depmap.py`). Type: **free.** The canon's [6] account (Krakauer et al.) *welds* Boundary to Memory by *defining* the boundary as the partition that maximizes a memory-like autonomy quantity — but that weld is imposed by a definition, not compelled by a law, and **the flame is the standing counter-witness**: a sharp, actively maintained boundary carrying essentially no memory (canon §4, §11, Table 2 "reclassified"). **[SETTLED that the weld is definitional; analytic-model-result that B and M dissociate; the flame is the constructed counterexample.]**

### 4c. Boundary ↔ Drive — **CONDITIONAL (this is where B4 lives, and it is uncomputed)**

Canon §4: **D→B is conditional** — "holding a gradient costs nothing at equilibrium (a potential well is free) and costs drive only when the boundary must be maintained against a leak, with the price set by how leaky it is." This is exactly **B4 (maintenance burden)** of the panel, and it is the bridge from Boundary to Drive: B4 = 0 for a free potential well (the bound H atom's cheap EM skin), B4 > 0 and set by leakiness for an actively maintained boundary (the star's photosphere; a cell membrane held against ionic leak). Type: **conditional.** Crucially, **B4 is specified in the panel and asserted in §4 but never computed** — the D→B "conditional" edge has no worked number anywhere. **[SETTLED direction (equilibrium gradient is free — standard thermo); the leak-priced-cost claim is plausible-but-uncomputed.]**

The concrete cost anchor for B4, at named level: maintaining transmembrane ion gradients is a large, real, measured metabolic burden — the Na⁺/K⁺-ATPase is a canonical example, consuming a substantial fraction of cellular/neural ATP budget to hold the gradient against leak (Na/K-ATPase energetics, ~ named-level only — PubMed abstract blocked this session, treat as a *lead* not a fact). This is the empirical face of B4 and of D→B.

---

## 5 · Holes, traps, and DEFECTs

- **DEFECT (the genuinely broken thing, top fix): the lead-scalar defect.** Old Table 1 leads Boundary with `I(inside;outside)` = **B5**, which the Panels spec explicitly retired as *cross-boundary dependence, not boundary strength*. Two independent reasons it is wrong to lead with: (i) `I(in;out)` measures how *dependent* the two sides are — a **high** value means they are strongly coupled, which is nearer to "no boundary" than to "sealed"; the intuition points the wrong way. (ii) By the §4a identity, B5 is **a slice of Integration**, so "Boundary" as currently scored is *not even a Boundary-specific quantity* — it is why B–I sits at 0.83, and it means the axis cannot be separated from Integration *by its own definition*. The DEFECT and the nesting correlation are **the same problem seen twice.** The fix is to lead with the proxies that carry genuinely Boundary-specific, non-TC content: **B1** (interior/exterior state contrast), **B2** (screening residual), **B4** (maintenance cost). **[DEFECT — mis-scores the concept regardless of the couplings.]**

- **Concretely, what computing B2 and B4 on a minimal model would take:**
  - **B2 (screening / interface mediation), cheap — a few lines on the existing model.** On the same 6-node Gaussian VAR(1) of `aop_depmap.py`, add an explicit **interface partition F** to D (declare which variables are the interface, e.g. one boundary-adjacent node per side, or a mediating latent). Then B2 = `I(X_in;X_out | X_F)` is closed-form Gaussian via Schur complements: `½[logdet Σ(in|F) + logdet Σ(out|F) − logdet Σ(in∪out|F)]`, where `Σ(·|F) = Σ_·· − Σ_·F Σ_FF⁻¹ Σ_F·`. The **screening efficacy** is the drop `I(in;out) − I(in;out|F)`; a good screen sends B2 → 0 (the Markov-blanket limit). Deliverable: a screened vs. unscreened pair showing B5 high but B2 ≈ 0 for the screened case — the number that separates "coupled across a cut" from "sealed by an interface." *Cost: low; reuses the existing covariance code plus one conditioning step.*
  - **B4 (maintenance burden), harder — needs a *driven* model the codebase does not yet have.** The `aop_depmap.py` corners all set A = 0 (zero drive), so B4 is identically 0 there. B4 needs a **two-compartment leak+pump** minimal model: a leak conductance g across the interface that relaxes the interior/exterior contrast toward equilibrium, and a pump/drive that holds a contrast Δ against it. Then B4 = the **housekeeping entropy production** (or steady work rate) required to maintain the contrast — closed-form for a linear/OU or small Markov model via the Hatano–Sasa / Oono–Paniconi housekeeping-heat split, `σ_hk` on the antisymmetric current part. The prediction to reproduce is exactly canon §4's D→B: **B4 = 0 at equilibrium, B4 ∝ leakiness g when maintained.** This *unifies* Boundary with Drive (B4 is a Drive-panel quantity read on the interface) and would turn the "conditional" D→B edge from asserted into computed. *Cost: moderate; new minimal model + the housekeeping decomposition.*

- **Trap — realist reading of an instrumental boundary.** The informational Markov blanket is observer-relative *by nature*: one first chooses which node is "inside," and only then does the blanket appear; conflating the instrumental construction with a realist claim about a thing-in-the-world is a known error (Bruineberg et al. / canon [11] ⊙). Boundary being soft is the axis honestly wearing this.

- **Trap — the maximally observer-relative boundary (flame).** The flame's thermal, ionization, and luminous edges genuinely differ (canon §11). "The flame's boundary" is undefined until D fixes *which* edge; there is no fact of the matter prior to the declaration. Make this vivid rather than hide it — it is the cleanest illustration in the paper that Boundary magnitudes are not invariants.

- **Over-claim to reword (shared with Integration/Memory groups):** Fig T's "|corr| < 0.05" overstates independence; the measured B–I is 0.83 (nested), B–M is free only *after* controlling coupling. Reword to the measured dependence (state report §0, §6). **[fix — do not claim more independence than measured.]**

- **Two boundaries, not one, is the norm, not an exception.** The bound atom and the star both carry a screening *and* a causal boundary simultaneously (Fig 4; §8). Any "the boundary" phrasing is already a simplification; the panel should record boundary *type* (screening / causal) alongside magnitude.

---

## 6 · Gap list for Boundary

1. **Compute B2 (screening residual `I(in;out|F)`) on the minimal Gaussian model.** (a) Literature likely answers the *method* fully: it is Gaussian conditional MI / partial correlation (Faes–Marinazzo–Stramaglia 2017 ⊙) and the Markov-blanket screening condition (Pearl 1988 ✓); no new theory needed. (b) SYNTHESIS. (c) **Needs computation, but small** — reuses existing code.
2. **Compute B4 (maintenance burden) and thereby the D→B conditional edge.** (a) The physics is settled (housekeeping heat: Hatano–Sasa 2001, Oono–Paniconi — *not verified this session, leads*; empirical cost: Na/K-ATPase energetics ~named). (b) SYNTHESIS turning into analytic-model-result. (c) **Needs a new minimal driven model** (leak+pump), moderate effort — the single highest-value computation for this axis after B2.
3. **Decide what Boundary's Table 1 lead proxy should be, and whether Boundary warrants a standalone axis at all given the nesting identity.** (a) Partly synthesis-internal; the identity `TC = I(in;out)+TC_in+TC_out` argues Boundary should lead with a *non-TC* proxy (B1/B2/B4) or be reported as "the cross-cut slice of Integration, flagged when it carries weight." (b) DEFECT→SYNTHESIS. (c) **Synthesis only** (a modelling decision + a canon edit to Table 1).
4. **Formal screening↔conditional-independence bridge: Debye length ⇄ Markov blanket.** Does the physical screening length λ_D map cleanly onto the rate at which B2 = `I(in;out|F)` decays with interface thickness? (a) Likely *already implicit* in stochastic-thermodynamics / field-theory literature (screened correlations decay over λ_D); a genuine "known in three fields" candidate — worth a literature pass before claiming novelty. (b) FRONTIER→SETTLED-if-found. (c) **Synthesis + literature search.**
5. **Which flame edge is the persistence-relevant boundary?** The thermal/ionization/luminous edges differ; is there a *viability-selected* edge (the one whose scrambling drops the flame's viability most, via the §3 mask)? (a) No known result; genuinely open. (b) FRONTIER. (c) **Needs computation** (a mask run on a flame-like reaction-diffusion model) — speculative.
6. **Boundary *type* in the panel (screening vs causal).** The atom and star carry both; the panel records magnitude but not type. (a) Settled physics distinguishes them (§8, §10); the gap is bookkeeping. (b) SYNTHESIS. (c) **Synthesis only.**

---

## 7 · Citations used (with verification markers)

- **Pearl, J. (1988)** *Probabilistic Reasoning in Intelligent Systems* — Markov blanket / boundary = conditional independence of a node from all others given its blanket. **✓** (definition + originator verified via Wikipedia "Markov blanket" this session; primary text not opened — the *attribution and definition* are what I verified, mark ✓ for that, ~ for the book text itself).
- **Debye length / Debye–Hückel screening length** (standard electrostatics) — mobile charges screen a test charge; bare Coulomb potential exponentially screened over λ_D. **✓** (Wikipedia "Debye length," verified this session; a settled textbook result).
- **Campa, Dauxois & Ruffo (2009)**, *Phys. Rep.* — long-range interactions are non-additive; negative specific heat / ensemble inequivalence for gravitating systems. **⊙** (canon-inherited, canon §8/§11).
- **Faes, Marinazzo & Stramaglia (2017)**, *Entropy* 19(8):408 — closed-form information decomposition for Gaussian VAR processes; the tool behind B, B2, TC computations. **⊙** (canon-inherited).
- **Bruineberg et al. / Friedman — the instrumental-vs-realist Markov blanket** (canon [11]) — boundary is observer-relative; realist/instrumental readings must not be conflated. **⊙** (canon-inherited; the "Emperor's New Markov Blankets" preprint surfaced in search this session but was not read — the canon's use is what I rely on).
- **Krakauer et al. (canon [6])** — individuality as the memory-maximizing (autonomy) partition; the source of the B–M weld the flame breaks. **⊙** (canon-inherited).
- **Watanabe (1960)** — total correlation `TC = ΣH(Xᵢ) − H(X)`, the Integration quantity the nesting identity decomposes. **⊙** (canon-inherited).
- **Na⁺/K⁺-ATPase energetics** (maintenance cost of ion gradients, the empirical face of B4) — **~ / ? named-level only**; PubMed abstract was CAPTCHA-blocked this session. Treat as a *lead* for B4, not a verified figure.
- **Hatano–Sasa (2001) / Oono–Paniconi — housekeeping heat** (the closed-form basis for computing B4) — **? unverified this session**; named as the method to reach for, not read.
- Dependence-map facts (identity 1.8e-15; B–I 0.83, B–I|M 0.73; B–M 0.61, B–M|I 0.24, B–M|coupling −0.05; Boundary unique variance 0.29; corners) — **✓ read `aop_depmap.py` + state report rev.2 this session.**
