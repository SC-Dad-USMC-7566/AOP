# AOP Axis Audit — Card 1 of 4: BOUNDARY (B)

**Auditor:** Claude Prime · **Date:** 20 July 2026
**Audited against:** `AOP_CANON_MASTER_v1.19.md` (confirmed highest version on Drive; nothing newer)
**Sources read verbatim:** canon v1.19 — Table 1, §1, §2, §3, §4, §8, §10, §12 declaration-tuple para; `AOP_ADR_001_panel_architecture.md` (ADOPTED 17 Jul, panel spec); `REV_OAI_AOP_Operational_Definitions_v1_0` §3 (Boundary panel source); `REV_AOP_Operational_Panels_v1_0` + `panel_sensitivity.csv` (Boundary panel as actually computed).
**Not read:** panel/benchmark source code; the intervention-protocol file. Stated so the check is honest.

---

### 1. Concept
*How well a system keeps a distinct interior against its exterior — a maintained inside/outside separation.*
Canon prose: "a maintained separation of interior from exterior (Boundary)" (§1); aspect = "space," the "inside-versus-outside" relative-entropy cut (Table 1). **Drift to flag:** the adopted panel restates the target as "maintained interior/exterior *organization regulating exchange*" (ADR-001). That is not the same concept — "separation" forbids high cross-boundary traffic; "organization regulating exchange" permits and even expects it. The concept itself is not pinned; two live wordings pull opposite ways.

### 2. Measure
**Canon Table 1 (still current) lead proxy:** mutual information **I(inside; outside)** across a declared cut. Inputs: joint distribution/covariance over system vars + a declared inside/outside cut. Operation: MI across the cut. Output: bits. Table 1 already hedges — "statistical dependence across the cut, not of separation per se … not this one scalar."
**Adopted panel (ADR-001, the real measure) — five proxies, not one:**
- B1 state contrast — D_KL[p(X_in) ‖ p_ref(X_out)]
- B2 interface mediation — I(X_in;X_out | F), i.e. *screening* (→ low for a good screen)
- B3 leakage/permeability — physical flux / escape rate across the interface
- B4 maintenance burden — work / entropy-production to hold the contrast over τ (couples to Drive)
- B5 cross-boundary dependence — I(X_in;X_out), "labeled exactly as dependence, **not** boundary strength"
The canon's lead proxy *is* B5. ADR-001 explicitly retires it as the Boundary scalar: "*This retires the status-table row 'Boundary (B) | mutual information I(inside;outside)'.*"
**As actually computed** (only worked instance, `REV_AOP_Operational_Panels`, on the now-closed benchmark): Boundary panel = I(n;r), I(n;z), H(n) spread, 1−P(empty) — two more *unconditional* MIs + a spread + an occupancy. The specified **screening proxy (B2, conditional MI) and maintenance-cost proxy (B4) were never computed.** So the separation reading of Boundary has been *specified* but never *exercised* anywhere.

### 3. Units / scale / "mass"
Lead proxy: relative entropy, in bits. Zero = inside ⊥ outside; high = strong dependence across the cut.
**This is the broken yardstick, and it is the core finding.** For a *separation* concept, independence (MI = 0) is the strong-boundary pole and high MI is the leaky pole — the mass runs *backwards* from the concept. And it is worse than inverted: per the source (opdefs §3), high MI can mean organized mediation, leakage, common input, *or* external control; low MI can mean insulation *or* mere absence of interaction. So I(in;out) is **non-monotone / four-ways ambiguous** as a score of the concept. There is no single "mass" for Boundary; the panel proxies carry different units (bits for B1/B2/B5, a physical rate for B3, energy-per-time for B4) — which is *why* the panel exists.

### 4. What it is NOT
- **NOT Integration.** Boundary's proxy (MI across a cut) and Integration's proxy (total correlation across a partition) are the *same kind of object* — static mutual-informations off one covariance — and the canon reports them **positively correlated ~0.83 across generic systems**, "dissociable only by construction" (§2/§6, Fig T). The measure does **not** cleanly exclude Integration. *This is the most important line on the card for Phase 2.*
- **NOT a physical membrane.** [P0-2]: "the proxy names statistical organization, not a physical membrane."
- **NOT screening.** I(in;out) is unconditional; §8 defines a statistical boundary as inside ⊥ outside **given the interface** (conditional). The lead proxy is not that conditioned quantity, and the two can move oppositely.
- **NOT one object.** "Boundary" bundles ≥3 things the canon itself separates: the informational blanket, the thermodynamic gradient-maintenance cost (§8/¶290: "conflating them is a known error"), and the causal/light-cone boundary (§8, §10). The Table 1 scalar reaches at most the first, mis-signed.
Exclusion check: membrane — yes (admitted); Integration — **no** (~0.83); screening — **no** (wrong conditioning); the three-notion bundle — held apart only by prose, not by the number.

### 5. Gap verdict: **LOOSE — bordering BROKEN for the still-current lead scalar.**
- Concept ("maintained separation") vs canon lead proxy (dependence) are misaligned in **direction and monotonicity**. v1.19 adopted the *word* "panel" and the caveat but still names I(inside;outside) the "lead proxy" — re-committing the exact P0-2 defect ADR-001 was built to retire. **Concrete inconsistency to resolve:** Table 1 v1.19 "lead proxy: I(inside;outside)" vs ADR-001 "retires 'Boundary (B) | mutual information I(inside;outside)'." Pick one.
- The proxies that *would* capture separation (B1 contrast, B2 screening, B4 cost) are specified but never computed; the one computed instance used dependence-flavored MIs and dropped screening and cost. The corrected Boundary axis has **no worked example**.
- On the canon's own numbers the measure does not separate from Integration (~0.83) — a Phase-2 problem, not this card's to solve, but flagged here as originating in the Boundary definition.
**Not broken outright** because the concept *is* capturable (B1/B2/B4 are the right objects) and the framework already names the defect. **Loose** because the current canonical lead scalar mis-scores the concept and the fix is unexercised.

**Recommended fix (for Ben — not applied):** in Table 1, demote I(inside;outside) from "lead proxy" to "B5, dependence only," and name B2 (screening) or B1 (contrast) as the lead for the separation reading — i.e. finish in the canon the retirement ADR-001 already decided. Separately, log B–I ≈ 0.83 as the first thing Phase 2 must try to break.

---
*Next axis on Ben's go: Drive. Not started until Ben reacts to this card (handoff §2: iterative, not batch).*
