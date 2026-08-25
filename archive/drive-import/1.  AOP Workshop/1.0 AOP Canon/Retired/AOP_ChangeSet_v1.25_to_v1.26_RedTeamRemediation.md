# Changeset — AOP v1.25 → v1.26 (red-team remediation)

**From:** Claude Cowork (execution seat)
**To:** Prime (chat seat), for verification; Ben decides
**Date:** 25 July 2026
**Order implemented:** `TASK_CW_AOP_v1_25_to_v1_26_RedTeam_Remediation_20260724.md`
**Status:** **PROPOSAL. Not self-certified. Not canon.**

---

## 0. Provenance and integrity

| Item | Value |
|---|---|
| Source master | `AOP_CANON_MASTER_v1.25.md`, Drive `13tI48fz-l5DundXuyQysPJf7JrSS9xck` |
| Source size / md5 | **224,340 bytes** / `9c172e015f4adfc9fe827a42687ca2e7` — byte-count verified against Drive metadata before any edit |
| Source lines | 997 |
| Output master | `AOP_CANON_MASTER_v1.26.md`, 851 lines |
| **Lines carried forward byte-identical** | **657** |
| Changed regions | 85 (enumerated in §4 below) |
| Lines replaced / inserted / deleted | 307 / 30 / 70 |

**Method.** The v1.25 master was copied and edited in place by exact-string and exact-line-index operations. No section was rewritten wholesale except where this order required it. Untouched sections are byte-identical **by construction**, and this is confirmed by machine diff (`difflib.SequenceMatcher`, `autojunk=False`), whose `equal` opcodes cover 657 lines.

**The historical changelog is byte-identical.** v1.25 lines 836–997 — every version-history entry from the reference-audit paragraph through the v1.25 entry — are unchanged. See §5, flag F-3, for why, and for what that means for the Task 14 / 19a sweep instructions.

---

## 1. Deliverables produced

| # | File | Lines | Purpose |
|---|---|---|---|
| 1 | `AOP_CANON_MASTER_v1.26.md` | 851 | Living master. All edits applied. Inherits masthead, changelog, gate ledger, retraction history. |
| 2 | `AOP_LifeArchitecture_Followon_v0.1.md` | — | Relocated life block + diachronic identity, with Tasks 5/16/17/19a–c applied. |
| 3 | `AOP_Submission_v0.1.md` | 717 | Submission derivative. Current claims only; apparatus stripped (Task 4). |
| 4 | This changeset | — | Edit → task → register-item mapping. |
| 5 | `AOP_v1.26_FlagList.md` | — | Items for Prime/Ben decision. |
| 6 | `retrieval_setA.md`, `retrieval_setB.md` | — | Deposited primary-source passages for Prime's line-check (parallel deliverable). |

---

## 2. Task-by-task disposition

### Task 0 — Fork the manuscript (L5 / RED-27) — **DONE**
Two files created from the v1.25 master. The living master inherits everything; the submission derivative receives the outputs of the edits and none of the governance apparatus. Both built locally; Drive placement per §6.

### Task 1 — Crystal sentence (L3 / RED-22 crystal) — **DONE**
**v1.25 line 430 → v1.26 line 393.** "Nothing it holds bears weight for continued persistence; it is terminal" replaced with the passive-load-bearing reading: the lattice bears weight (disrupt it and the crystal ceases) but costs no drive to hold; what was spent is the growth front. Suggested wording used with one change — the order's phrasing repeated "growth front," which the surrounding sentence already contains, so the second occurrence is compressed. Grade unchanged (synthesis).

### Task 2 — "dissociate generically" (L1 / ORANGE-23) — **DONE**
Two live instances replaced, `phaseE1` numbers and the dissociation-corner result untouched.
- **Abstract (line 17):** "dissociate generically across random Gaussian systems" → "dissociate throughout the declared Gaussian ensemble … populated throughout it."
- **§4 (v1.25 189 → v1.26 183):** "confirms the dissociation is generic, not merely constructible" → "confirms that the dissociation occurs throughout the declared Gaussian ensemble rather than only at hand-built corners."
- One further occurrence at v1.25 line 139 (§4, "generically *builds* it") is a **different sense** — it concerns strong readings of dissipative adaptation, not the E1 result — and was correctly left alone. One occurrence in the v1.25 changelog entry is history and is left byte-identical.

### Task 3 — Star O-information attribution (L2 / ORANGE-24) — **DONE**
**v1.25 line 434 → v1.26 397–399.** "the O-information is **redundancy-dominated (Ω > 0)**" → "the **declared polytropic shell covariance is redundancy-dominated in O-information (Ω > 0)**." The consequent sentence is re-attributed from "the integrated star's interdependence" to "the interdependence *of that declared covariance*," with an added line stating that "the star is redundancy-dominated" is not licensed. Ω > 0 computation unchanged. `phaseC3_integration.py` description in Data Accessibility updated to match.

### Task 4 — Citation & submission hygiene (L4 / RED-26) — **DONE (submission derivative only)**
Removed from `AOP_Submission_v0.1.md`, retained in the master: the repository-DOI placeholder (replaced with a data-availability pointer), the "cite specific section … at submission" instruction on Bruineberg et al., all `[✓ …]` / `[~ …]` verification tags, every `⚠` annotation and unverified page-range note, the `[P0-n]` audit markers, the gate ledger (Table 4) and its prose, the §13a retraction narrative, the entire version history, and all inline "deleted in v1.26 / earlier versions / withdrawn" commentary. Verified by grep: zero occurrences of `v1.x`, `Versions ≤`, `⚠`, `prime`, `this session`, or retraction language remain in the derivative.
**Joyce 1994 flagged, not resolved** — see flag **F-1**.

### Task 5 — Virion/mule (L6 / ORANGE-20) — **DONE (in the follow-on)**
The block moved with the life material (Task 19), and the edit was applied at its destination: follow-on §5. The virion contrast is retained explicitly as the motivation for separating organismal maintenance from lineage evolution. The mule is **dropped as decisive proof** and retained as illustration, with the reason stated — using it as proof is circular (it is adjudicated by the very intuitions the criterion is being tested against), and the objection it names is contested rather than settled in the source.

### Task 6 — Freeze the ontology (M1 / RED-1) — **DONE**
A front-of-paper block, **"The ontology, fixed once,"** added at the end of §1 (v1.26 lines 45–53), stating all five items verbatim in intent: nodes are conceptual targets; proxies are attached measurement families; edges are propositions relating specified proxy aspects under **D** and model class **M**; reliability is a downstream outcome, not a fifth node; lifetime is the declared outcome primitive. Cross-loading is explicitly preserved and named *as* cross-loading (B4 as the Drive panel's housekeeping term at the interface; B5 as an algebraic component of Integration). A closing clause states that any later bar-height or scalar display is a panel reading under a declaration, never a node identity. §12″ is cross-referenced as the operational form and now says so in both directions.
**Sweep performed:** §2 Table 1, §6, §11 §11 figure caption, and §12″ were checked and adjusted so no later passage redefines an axis as a scalar or panel identity.

### Task 7 — Partition- vs representation-dependence (M2 / RED-2) — **DONE**
**v1.25 82, 97, 102, 109 → v1.26 63, 78, 83, 90.**
- Table 1 caption: "Two are cleanly computable; two exist only relative to a declared partition" → "**All four are declaration-relative**; Boundary and Integration *additionally* require an explicit spatial or component partition."
- Drive row: "None: cleanly computable" → "Representation-dependent (declared state variables, grain δt, and time-reversal convention R); no additional partition required."
- Memory row: "None: cleanly computable" → "Representation-dependent (declared observable, time grain δt, and a stationarity claim at that grain)."
- Body paragraph rewritten to the *representation-dependence (all four)* vs *partition-dependence (Boundary, Integration additionally)* frame, with the specific choices each of Drive and Memory requires spelled out. **Every surviving "no choices to make" claim deleted.**
**Coupled to Task 11 and done in the same pass** — the reversal convention this exposes is wired to slot **R** and to the D→M fourth scope condition, and Table 1's Drive row names R directly.

### Task 8 — MFPT as lead, not essence (M3 / RED-3) — **DONE**
Abstract and §1 (v1.26 line 28). MFPT retained as the named lead primitive. **The §1 occupancy argument is not weakened** — it is explicitly reinforced ("The lifetime-versus-occupancy distinction above is load-bearing and is not weakened here"), with the deposited gate cited (5.7× on MFPT, occupancy invariant to 1e-14). Added: the **persistence-functional family** (survival curve, hazard function, finite-horizon survival, recovery probability) and the four named regimes in which MFPT is inappropriate — infinite/undefined mean; heavy tails; aging/developmental/path-dependent systems; self-modifying viable sets. §11b's finite-horizon declaration is cross-referenced as a worked instance.

### Task 9 — Spore Cμ / material-complexity separation (M4 / RED-6) — **DONE**
Three notions separated permanently and never re-fused, in **§4** (v1.25 131 → v1.26 125), with the separation propagated to **§1** (line 40), **§5**, and **§11** (line 393):
(i) predictive dependence **E**; (ii) predictive-state complexity **Cμ** *of a declared observation process* — a property of a measurement channel, never of an object's molecules; (iii) **stored physical organization**, explicitly *not* a member of the crypticity decomposition. Reading Cμ off material complexity with no declared observation process is named a category error. The spore is retained as a **motivating thought experiment** and is stated in three places to be **not a computed witness** of high Cμ at low E, because no observation model has been declared or measured for one. The crystal's Cμ = E pole is put on the same footing.
**Consistency with Task 12/21 confirmed:** the spore is demoted from computed evidence in both the §4 numerator argument and the §11 archetype closing paragraph, in identical language.

### Task 10 — §11b as unit test (M5 / RED-8) — **DONE**
Section retitled **"A unit test of the semantic intervention protocol."** Both necessity claims removed: the §11b opening ("to show the four-target … apparatus is *necessary*") and the closing ("a closed-form case where the four-target apparatus is demonstrably necessary"). The withdrawal is stated with its reason — a self-authored answer key cannot establish necessity, the benchmark was built by the same hands as the apparatus, and no rival was run — and necessity is explicitly deferred to the external benchmark. Retained and strengthened: the recovery of the designed inert / load-bearing / redundant / synergistic structure, and the observation that the **coalition layer** is what does the recovering while single-edge deletion reports the redundant pair as inert — which is now presented as the argument for the Task 20c coalition default.

### Task 11 — D→M scope condition + reversal convention in D (H1 / RED-4) — **DONE, with one finding**
**Part 1 — fourth scope condition.** v1.25 line 131 → v1.26 line 125 ("three conditions" → "four conditions"; new condition inserted as *Third*, floor-not-depth renumbered *Fourth*). The condition: the result holds when all state variables are even under the declared time-reversal, or when the stationary one-point distribution is invariant under the reversal involution. States that it holds trivially for the configuration-space Markov models computed on here (Figure DM's driven ring named) and is **explicitly silent** on odd-variable systems (momenta, currents, spins) until R is declared for that case. Cited to Spinney & Ford 2012 / Ford & Spinney 2012, both added to the reference list. Table 3's D→M row carries the same condition.
**Status held: forced × theorem/corollary. NOT downgraded.** Stated three times (§4 body, Table 3 row, Table 3′ row) that this is a scope addition, not a reproof.
**Verification hook, per the order:** the counterexample the condition addresses — odd-parity i.i.d., 0.83 nats at q = 0.8 under parity reversal, exactly 0 under sequence reversal — is the case in which the "i.i.d. ⇒ equals its own time-reverse in distribution" step fails, because the stationary one-point distribution is not invariant under the parity involution while it is invariant under sequence reversal. The condition as written excludes exactly that case and admits every model in the paper.
**Part 2 — reversal convention in D: ALREADY PRESENT. See flag F-2.** v1.25's §12″ already read `D = (S, E, F, P, δt, τ, R, V, I, N)` with **R = reversal convention**. It was inert — nothing referenced it. Rather than "add" an existing slot, §12″ now carries a block making R (with V and I) load-bearing and wiring R to the D→M condition, and Table 1's Drive row names it.
**ORANGE-5 — D→M spoke demoted.** Added to the end of the D→M paragraph: the spoke is a scoped theorem box, not a pillar of "energy as hub"; it forces E > 0 and nothing further — no stored-complexity floor, no stored time-asymmetry (Ξ = 0), no claim about stored physical organization. Emphasis change only; the gate ledger already bounded it this hard.

### Task 12 — Modal×semantic plane → ledger (M6 / ORANGE-9) — **DONE**
**Figure 2 deleted and replaced by Table 2′,** a tagged ledger with five categorical rows (forced / conditional / free-or-feasibility-constrained / reclassified / dissociable-substrate-sharing), each holding its edges and a semantic **interval**. §6's opening paragraph now states that modal class is **categorical, not ordinal**, and "persistence lives up-and-to-the-right" is withdrawn with the reason (it requires an ordering the classes do not carry; a forced edge can be inert, a free edge load-bearing). The horizontal-axis-as-interval concession at v1.25 line 262 is preserved and is now consistent with a categorical vertical. Data Accessibility figure list updated.

### Task 13 — Observer = declaration-relativity (M7 / RED-11) — **DONE**
§7 retitled **"The observer, located: semantic claims are declaration-relative."** One position adopted and held: every semantic claim is explicitly relative to a **declared persistence criterion** (a declared viable set and a functional V on it). **"The system is its own observer" is dropped**, with the legitimate half preserved verbatim (semantic information is meaningful *to* a system relative to *its* viability; the functional is evaluated on the system's viable set) and the illegitimate half — that the system *performs* the evaluation — removed. The masthead's scoping of "own" is extended to every occurrence rather than stated once. Homunculus containment is **preserved and strengthened**: the analyst is named as declarer, written into **D**, and available to be disputed; a hidden evaluator was the dangerous case and there is now no hiding place. Table 3's row retitled and rewritten to match. Sweep covered §§3, 7, 9, 11a-successor, 12″, and the abstract.

### Task 14 — Rename Φ_MIP (M8 / RED-15) — **DONE, three parts**
1. **Renamed to "minimum-cut dependence"** (read as a minimum-cut irreducibility diagnostic) throughout the **live body**: §1 refusals, §4, §9, §9a, §12 Table 3, §12 gate-ledger row, §12′ Table 3′, §13, §13a, Data Accessibility. The symbol Φ_MIP is retained only where explicitly labelled as a symbol or where the text is describing what was renamed. **Historical changelog not swept — see flag F-3.**
2. **Aguilera & Di Paolo re-attributed as lineage/inspiration.** The §4 paragraph now carries a **Provenance** block stating that the minimum-cut search over the static Gaussian covariance Σ = (I + gL)⁻¹ is AOP's construction, built in their lineage, **not their measure imported unchanged**, and that their results do not transfer to it. The reference-list entry carries the same statement. A retrieval finding bearing on this is flagged (**F-5**) and is *not* asserted in canon.
3. **Inference from positivity to individual deleted.** A **"What positivity does not license"** block added in §4: positivity establishes non-factorization across the least-disrupting bipartition and **not** that the system is one individual. The quantity is made one coordinate in an **individuation panel** alongside autonomy, causal closure, intervention stability, and common-cause controls — with the note that a shared driver produces irreducibility across every cut without producing an individual. **The §9a synchronic claim is removed** (v1.25 371–377 → v1.26 331–344), with the reason stated: as written it contradicted the §13a level-selection retraction, and that internal inconsistency is the priority, so it is deleted rather than hedged. Table 3, Table 3′, and the gate-ledger row all carry the withdrawal.

### Task 15 — Diachronic identity to outlook (M9 / ORANGE-16) — **DONE**
**§4a deleted from the core** (v1.25 193–242) and relocated to the follow-on §7. The core retains exactly one sentence of it, placed in the §1 pointer paragraph: *comparing a system at two times requires a declared tracking relation*, entering as part of **D**. **The continuity-of-instantiation position is not conceded** — the follow-on states explicitly that the objection was scope, not error, and retains the position in full. Per the order's note, §4a travelled to the same follow-on as the life block.

### Task 16 — Spore second tier as counterfactual capacity (M10 / RED-19) — **DONE (in the follow-on §6)**
The pausable tier is redefined as a **present-state-conditioned counterfactual recovery capacity** and it is stated plainly that it is **evaluated through a model of future dynamics** (biochemical integrity, recoverability under a declared perturbation, or a functional intervention). The claim that it is readable from architecture alone is deleted, with the counterexample named: **a dead spore retains the visible architecture.** The cost is stated rather than hidden — the second tier is not a present-tense structural reading and cannot be made into one; what keeps it inside the present-tense principle is that the *conditioning* is on the present state. **The alive tier is explicitly unaffected** and remains strictly present-tense-active and mask-detectable. The §8 death section carries a matching caveat ("subject to the integrity caveat of §6, since a dead spore restarts from nothing").

### Task 17 — Reframe death as process-cessation-at-grain (M11 / RED-21) — **DONE (in the follow-on §8)**
The suggested rewrite is used essentially verbatim, with the surrounding argument the order asked for. Death is defined as **the persister-process stopping at its own declared grain**, derived as a corollary of two things the paper already owns — the present-tense principle and the time-grain relativity of the axes (the star's thermal-vs-nuclear Memory named as the worked instance). A paragraph states that this **dissolves** rather than fences out the counterexamples: intact membranes, persisting genomes, transient metabolism, and slow-decaying gradients are subordinate grains outliving the one that stopped, i.e. confirmations. **The cascade is separated from the definition** and retained as *one common route on tightly integrated persisters*, with the contestable cases named (trauma, rupture, information loss, where drive-failure does not lead). Grade kept: **synthesis**.

### Task 18 — Cut the physics block (H2 / RED-12, 13, 14) — **DONE, three parts**
**18a — Light cones.** Every claim that a light cone is a one-way membrane, a causal boundary, or an object-specific boundary is deleted, in §8 (v1.25 292–298), §10, §11 (the star's boundary sentence, and the atom), and Table 3 / Table 3′. **Figures 3 and 4 and their captions are deleted.** The atom's "one persister, two boundaries" observation is deleted entirely along with the light-cone half; the atom now carries one cheap passive interface.
**18b — Binding / rest frame / present tense.** §10 retitled **"The domain and its edge: an operational scope condition"** and the domain wall **entirely replaced** by: *AOP applies wherever a subsystem, state representation, persistence functional, horizon, and admissible intervention class can be declared* — with the note that all five are already slots in **D**. "Binding, not rest mass, draws the wall," binding-as-admission-criterion, and the rest-frame/proper-time/invariant-mass reading are removed. Two consequences are stated: admission is a property of the description, not the object; and "rest mass as the price of persistence" does not survive in any form.
**18c — Force/screenability taxonomy.** §8 retitled **"Interfaces: passive and actively maintained."** Removed from the core: EM screening as the unique maker of statistical boundaries; strong/weak interactions disqualified from individuation; unscreened gravity implying absence of a statistical boundary; long-range non-additivity implying a nonzero Integration floor. **Retained narrow statement:** a physical interface can be passive or actively maintained, and screenable interactions make passive interfaces cheap.
**What survives, as required:**
- **B2/B5 screening-residual computation retained verbatim** (B2 = 0.000 sealed / 0.292 bypassed; B5 = 0.896 / 1.685), with an added sentence noting it is a property of the declared Gaussian model and never depended on the taxonomy.
- **Star's two-boundary insight in demoted form retained**: an actively maintained radiative interface (photosphere — scramble the opacity and it stops being a star) on a passive gravitational one, with the asymmetry (only one is paid for) named as the surviving content.
- The star's **negative-specific-heat thermostat** is retained as a model result [Lynden-Bell & Wood 1968; Campa, Dauxois & Ruffo 2009]; only the wider "one property is the common root of three features" synthesis is deleted.
**Consequence recorded, not absorbed:** the causal-boundary row leaves the hard floor of Table 3′, leaving **exactly one** forced × theorem/corollary row. §12′'s "Reading the ledger" says so explicitly.
**Bounding-principle status flagged for Ben, not decided — flag F-4.**

### Task 19 — Move the life block to a follow-on (H3 / RED-3-exec, RED-17, RED-18) — **DONE; timing default taken**
**19a — De-announce.** The "new definition, graded frontier" posture is removed. In the core the architecture is presented as a **candidate regulatory architecture that separates classes of persisters** and is **not named *alive***; the core notes only that readers will see where paradigmatic living things land. The head-of-paper note on "life" is **moved in full** to the follow-on rather than softened in place — see flag **F-6**, this is larger than the literal instruction and is flagged as such.
**19b — Control-theory support relabelled.** In the follow-on §3: the six-part conjunction (regulatory subsystem, dynamical decoupling, internal reference, separate intervention target, viability relevance, active self-maintenance) is spelled out item by item and labelled an **AOP hypothesis**, not forced by the cited results. Francis & Wonham is reattached to the regulatory-subsystem / exosystem-model component only; Bich et al. to the dynamical-decoupling component only. **"The internal-model requirement of life" is retired as a description**, in both the follow-on and the core, with the reason stated (the result is about regulation, not life, and about exosystem modes, not viability). Conant & Ashby remains background only.
**19c — Discriminator restated subspace-wise.** "Separate reference node" → *there exists a proper invariant subspace whose dynamics are autonomous with respect to the regulated coordinates*, in the follow-on §4 and in the core's §11a pointer and Table 3 row. Both required sentences are present: invariant subspaces map to invariant subspaces under similarity transform, so the verdict is basis-independent; and an arbitrary basis change is **not an admissible intervention**, because the declared physical intervention class **I** fixes the basis. Framed as hardening, not conceding.
**Destination:** `AOP_LifeArchitecture_Followon_v0.1.md`. Moved: §11a in full, the alive/pausable tiers, the discriminator, §4a, the virion/mule material, the death paragraph, the §9a collective-alive frontier question, and the head-of-paper life note. Core retains a one-paragraph pointer (§11a) plus a shorter pointer in §9a.
**One item moved the other way:** the "Memory's own semantic weight" computation (v1.25 line 511) sat inside §11a but is a **Memory-axis** result, not a life claim. It is relocated **into the core at §5**, immediately after the E(T) retention-depth paragraph, which already describes the same cell-type and star-type OU systems. Flagged as a placement decision (**F-7**).
**Sequencing:** the order's default — **move now** — was taken. Flag **F-8** if Ben wants it held.

### Task 20 — Specify the protocol; promote coalition semantics (H6 / RED-7, RED-10) — **DONE, three parts**
**20a — Named and specified.** The extension is named the **internal-edge intervention protocol** and given a specification block in §3 with all six required declarations: structural mechanism changed; a physical operation that could implement it; variables and laws held fixed; whether resource flow is fixed or free; whether detailed balance / conservation / topology are preserved; whether the altered model stays in the admissible class **M**. §3's preceding paragraph now states explicitly that KW intervene on the **system–environment channel**, that internal-edge intervention is AOP's extension, and that **nothing in the parent result licenses it**; KW is cited as inspiration and as the special case. All language implying the parent method validates internal-edge deletion is removed. Table 3's mask row carries the same.
**20b — Resolvability limit demoted to a domain map.** §6 subsection retitled **"A domain map for the edge-attribution estimator."** Reframed as a **model-specific domain map for the estimator**, not a law of persistence. The inferential/interventional split is kept; "both are functions of integration, topology fixes the ratio" is explicitly scoped to the declared synthetic family and to Figure TF's five wirings. **Both implications removed and explicitly blocked**: high total correlation does *not* imply mechanisms cannot be separately intervened on (common input breaks it), and low total correlation does *not* guarantee well-posed attribution (synergy breaks the converse). The uncertainty-relation analogy is withdrawn as more than decorative. Table 3 row retitled and regraded; §13 updated to match.
**20c — Coalition object promoted to default.** A block in §3 makes coalition-level semantics the **default** semantic layer: minimal failure cut sets, minimal viability-preserving sets, equivalence classes of viable mechanisms, allocation summaries (Shapley and relatives) only where additivity is justified and labelled as summaries, and a semantic hypergraph where no unique edge decomposition exists. Per-edge weights retained only where additivity/identifiability tests pass, with the `phaseE2` band cited (κ ≲ 9, gap > 3× blur, TC up to ≈ 0.5). It is stated plainly that **the per-edge mask does not reach the strongly integrated regime it was built for** and that the coalition object is the response to that failure, not a refinement of a working instrument. Propagated to the abstract, §12″, §13, and §11b.

### Task 21 — Archetypes to illustrations (H5 / RED-5, RED-22) — **DONE**
**v1.25 line 440 → v1.26 line 405.**
- **"Primary evidence" deleted.** All five reclassified as **motivating cases / illustrations**, in the §11 header ("Five motivating cases"), the §11 opening paragraph, and the closing paragraph.
- **Refuses-to-lose framing kept in full** — "a carving is justified by the distinctions it refuses to lose" is retained verbatim and identified as the honest taxonomic argument that does not need the word *evidence*.
- **Flame:** "essentially no memory" → "shallow or short-lived memory," with the reason (temporal correlation in temperature, radical-concentration, flow, and front-position fields is not zero). Applied in §11, the §11 closing paragraph, and §13.
- **Atom:** "brief persister" struck ("persists — briefly, modestly, really" removed; a ground-state H atom is stable absent perturbation). Light-cone framing removed with Task 18.
- **Star:** "all four dimensions near maximal" struck, with the internal contradiction named (no common normalization, which the paper denies elsewhere). Retained as **model results**: the negative-specific-heat thermostat, time-grain Memory, and the resolvability signature computed from stellar structure — all attributed per Task 3.
- **Consistency with Task 9 confirmed:** the spore is demoted from computed evidence in both places, in matching language.

### DEFERRED — not attempted, as ordered
- **External benchmark (H4 / RED-25).** Not attempted. §13 now names it as the framework's principal missing evidence and states its three requirements (externally-sourced ground truth, pre-registered gate frozen before any run, bind-before-freeze), explicitly deferred.
- **Primary-source retrieval.** **Attempted and delivered** as a parallel deliverable (`retrieval_setA.md`, `retrieval_setB.md`). Nothing from it was folded into canon as a claim. Two of its findings bear on Tasks 14 and 20a and are flagged (**F-5**), marked in canon as *retrieved but not line-checked*.

---

## 3. Reference-list changes

| Action | Entry |
|---|---|
| Annotated | Aguilera & Di Paolo 2019 — recast as lineage/inspiration; explicit note that AOP's static-Gaussian construction is not their measure; ⚠ retrieval residual added (master only). |
| **Added** | Spinney RE, Ford IJ. *Phys. Rev. E* **85**, 051113 (2012). doi:10.1103/PhysRevE.85.051113; arXiv:1203.0485. |
| **Added** | Ford IJ, Spinney RE. *Phys. Rev. E* **86**, 021127 (2012). doi:10.1103/PhysRevE.86.021127; arXiv:1204.4822 — with an explicit warning that these are two distinct papers with opposite author order and that pairing "Ford & Spinney" with the PRE 85 title is a conflation, plus a pointer to *Phys. Rev. Lett.* **108**, 170603 and its unretrieved Publisher's Note at 108, 199905. |
| Unchanged | All other entries, byte-identical. |

No reference was removed.

---

## 4. Machine diff — all 85 changed regions

Generated by `difflib.SequenceMatcher(None, v125_lines, v126_lines, autojunk=False)`. Every region not listed is `equal` and therefore byte-identical.

| Op | v1.25 lines | v1.26 lines |
|---|---|---|
| replace | v1.25 13–13 | v1.26 13–13 |
| replace | v1.25 17–17 | v1.26 17–17 |
| delete | v1.25 22–41 | v1.26 22–21 |
| replace | v1.25 48–48 | v1.26 28–28 |
| replace | v1.25 54–54 | v1.26 34–34 |
| replace | v1.25 60–60 | v1.26 40–40 |
| replace | v1.25 63–72 | v1.26 43–53 |
| replace | v1.25 82–82 | v1.26 63–63 |
| replace | v1.25 97–97 | v1.26 78–78 |
| replace | v1.25 102–102 | v1.26 83–83 |
| replace | v1.25 109–109 | v1.26 90–90 |
| replace | v1.25 115–115 | v1.26 96–96 |
| insert | v1.25 118–117 | v1.26 99–111 |
| replace | v1.25 131–131 | v1.26 125–125 |
| replace | v1.25 141–141 | v1.26 135–135 |
| replace | v1.25 189–189 | v1.26 183–183 |
| delete | v1.25 193–242 | v1.26 187–186 |
| insert | v1.25 256–255 | v1.26 200–201 |
| replace | v1.25 260–260 | v1.26 206–206 |
| replace | v1.25 262–262 | v1.26 208–208 |
| replace | v1.25 264–264 | v1.26 210–210 |
| replace | v1.25 266–266 | v1.26 212–218 |
| replace | v1.25 274–274 | v1.26 226–226 |
| replace | v1.25 280–280 | v1.26 232–232 |
| replace | v1.25 282–282 | v1.26 234–240 |
| replace | v1.25 284–284 | v1.26 242–242 |
| replace | v1.25 286–286 | v1.26 244–244 |
| replace | v1.25 288–288 | v1.26 246–246 |
| replace | v1.25 290–290 | v1.26 248–248 |
| replace | v1.25 292–292 | v1.26 250–250 |
| replace | v1.25 294–294 | v1.26 252–252 |
| replace | v1.25 296–296 | v1.26 254–254 |
| replace | v1.25 298–298 | v1.26 256–258 |
| replace | v1.25 309–309 | v1.26 269–269 |
| replace | v1.25 313–313 | v1.26 273–273 |
| replace | v1.25 323–323 | v1.26 283–283 |
| replace | v1.25 347–347 | v1.26 307–307 |
| replace | v1.25 371–377 | v1.26 331–344 |
| replace | v1.25 397–412 | v1.26 364–375 |
| replace | v1.25 416–416 | v1.26 379–379 |
| replace | v1.25 418–418 | v1.26 381–381 |
| replace | v1.25 420–420 | v1.26 383–383 |
| replace | v1.25 422–422 | v1.26 385–385 |
| replace | v1.25 424–424 | v1.26 387–387 |
| replace | v1.25 426–426 | v1.26 389–389 |
| replace | v1.25 428–428 | v1.26 391–391 |
| replace | v1.25 430–430 | v1.26 393–393 |
| replace | v1.25 432–432 | v1.26 395–395 |
| replace | v1.25 434–434 | v1.26 397–399 |
| replace | v1.25 440–440 | v1.26 405–405 |
| replace | v1.25 443–511 | v1.26 408–408 |
| replace | v1.25 513–537 | v1.26 410–410 |
| replace | v1.25 539–574 | v1.26 412–412 |
| replace | v1.25 577–577 | v1.26 415–415 |
| replace | v1.25 579–579 | v1.26 417–417 |
| replace | v1.25 585–585 | v1.26 423–423 |
| replace | v1.25 606–606 | v1.26 444–444 |
| replace | v1.25 612–614 | v1.26 450–452 |
| replace | v1.25 620–622 | v1.26 458–460 |
| replace | v1.25 624–626 | v1.26 462–464 |
| replace | v1.25 632–634 | v1.26 470–472 |
| replace | v1.25 636–636 | v1.26 474–474 |
| replace | v1.25 638–638 | v1.26 476–476 |
| replace | v1.25 640–642 | v1.26 478–480 |
| replace | v1.25 644–646 | v1.26 482–484 |
| replace | v1.25 652–666 | v1.26 490–492 |
| replace | v1.25 670–670 | v1.26 496–496 |
| replace | v1.25 673–674 | v1.26 499–500 |
| replace | v1.25 680–680 | v1.26 506–506 |
| replace | v1.25 709–710 | v1.26 535–536 |
| replace | v1.25 747–747 | v1.26 573–573 |
| replace | v1.25 750–750 | v1.26 576–576 |
| replace | v1.25 752–757 | v1.26 578–583 |
| replace | v1.25 759–759 | v1.26 585–586 |
| replace | v1.25 761–761 | v1.26 588–588 |
| replace | v1.25 765–765 | v1.26 592–596 |
| replace | v1.25 769–769 | v1.26 600–604 |
| replace | v1.25 773–773 | v1.26 608–608 |
| replace | v1.25 777–777 | v1.26 612–612 |
| replace | v1.25 779–779 | v1.26 614–614 |
| replace | v1.25 783–783 | v1.26 618–618 |
| replace | v1.25 789–789 | v1.26 624–624 |
| replace | v1.25 791–791 | v1.26 626–626 |
| replace | v1.25 835–835 | v1.26 670–674 |
| insert | v1.25 998–997 | v1.26 837–851 |

**Certification of the untouched remainder:** 657 of 997 source lines appear in the output unchanged, byte for byte. In particular, v1.25 lines **836–997** — the entire version history, including the v1.12, v1.14, v1.15, v1.16, v1.20, v1.21, v1.22, v1.23, v1.24, and v1.25 entries and the reference-audit paragraph — are unchanged. The only addition after line 835 is the appended v1.26 entry.

---

## 5. Where the order was not followed literally

Four places, each flagged rather than silently resolved. Full detail in `AOP_v1.26_FlagList.md`.

1. **Task 11.2** asked to add the reversal convention to **D**. It was already there as slot **R**. Strengthened instead of added (**F-2**).
2. **Tasks 14 and 19a** asked to sweep "every echo in the version history." The version history was **not** swept (**F-3**).
3. **Task 19a** asked to remove a posture from the head-of-paper life note. The note was **moved entire** (**F-6**).
4. **Task 19** did not specify where the Memory-axis semantic-weight computation inside §11a should go. It was moved **into the core**, not the follow-on (**F-7**).

Two harmless cross-reference slips in the order itself, noted for the record: its Task 0 preamble points at "Task 13" for assembling the submission derivative (Task 13 is the observer edit; the derivative is Deliverable 2 and was assembled last as intended), and Task 15's note refers to "Task 9-life" where the life-block move is Task 19.

---

## 6. Delivery and status

Files delivered to Ben and, where Drive write succeeded, placed in the Canon folder `1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J`.

**This build is a proposal.** It has not been self-certified, and no claim in it has been blessed by the seat that produced it. Prime verifies line-by-line against the tasking order and this changeset; Ben decides; nothing here is canon until it lands on Drive with Ben's sign-off.
