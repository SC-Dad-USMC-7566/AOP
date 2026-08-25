# AOP v1.26 — region-by-region verification against the change set

**Order:** `TASK_CS_AOP_v126_Verification_20260725`
**Seat:** Claude Science (builder seat; eligible — built nothing in the canon line)
**Date:** 25 July 2026
**Deliverable:** `AOP_v1_26_VerificationNote_v0.1.md`

---

## Verdict

**PASS-WITH-DEFECTS.**

All 85 changed regions are **AUTHORIZED-FAITHFUL**. There are **zero UNAUTHORIZED** regions and
**zero AUTHORIZED-DIVERGENT** regions. One **SPECIFIED-NOT-APPLIED** item exists (D-3, immaterial —
the specified edit has no target). The revert test is byte-perfect. Both of Claude Cowork's counted
assertions verify by count.

The four defects below are **all in the accounting documents and one residual sentence, not in the
substance of the fold.** None of them changes a claim, a grade, or a number in v1.26. In my judgement
D-1 and D-2 should be corrected before v1.26 is stamped MASTER; D-3 and D-4 are record-keeping and can
be corrected in the change set alone. Ben rules.

| ID | Defect | Where | Severity |
|---|---|---|---|
| **D-1** | Change set §0 provenance table reports "Lines replaced / inserted / deleted = **307** / 30 / 70". The true replaced count is **270** on the v1.25 side and **164** on the v1.26 side. 30 and 70 are correct. | Change set §0 — **not** v1.26 | Accounting error in the authorizing document. Canon text unaffected. |
| **D-2** | v1.26 §1 L40 still reads the flame as "carrying **essentially no memory**", while §11 L395 explicitly corrects that phrase as an overstatement ("Earlier versions said the flame carries 'essentially no memory.' That overstated it"). The canon now asserts and corrects the same phrase in two places. | v1.26 L40 (live body) | Real internal inconsistency in canon. Task 21 scoped its flame sweep to "§11, the §11 closing paragraph, and §13" — so this is faithful to the change set as written and is a **gap in the order**, not disobedience by CW. |
| **D-3** | **SPECIFIED-NOT-APPLIED.** Task 9 states the E / Cμ / stored-organization separation was "propagated to **§1** (line 40), **§5**, and **§11** (line 393)". §5 (L188–203) contains no such text: zero occurrences of `Cμ`, `observation process`, `stored physical organization`, `crypticity`, or `category error`. | v1.26 §5 | Immaterial. §5 never mentions Cμ at all, so nothing there re-fuses the three notions; there is no defect to fix in canon, only an overstated propagation claim in the change set. Reported individually per §3.1 rather than folded into a count. |
| **D-4** | Two line references in the change set are off by one paragraph because of diff-splice offset: Task 1 cites the crystal sentence at "v1.26 line 393" and Task 9 cites "§11 (line 393)"; both edits are actually at **L395**. Task 21 cites "v1.25 line 440 → v1.26 line 405", which is correct. | Change set Tasks 1, 9 | Citation hygiene in the authorizing document. Both edits verified present at L395. |

**Line-numbering convention, for the record.** Prime and CW report v1.26 = 851 lines and v1.25 = 997.
Both files end with a trailing newline, so `wc -l` and `splitlines()` give **850** and **996**; the
851/997 figures come from `str.split("\n")`, which yields a phantom empty final element. This is a
convention difference, not a discrepancy — and it is the convention the change set's §4 diff table is
built in, so **I adopted it throughout this note** to keep every row directly comparable to the change
set. No content is in dispute.

---

## §0. Conflict disclosure, discharged

I authored `AOP_Step0_AxisInputScoping_v0.1.md`. Of the 29 canon lines that report's answers rest on,
20 fall inside v1.26's changed regions, so a defect in one of those regions could move my own Step 0
conclusions. I verified them first, as ordered.

**Outcome: no Tier 1 or Tier 2 region failed, so no Step 0 answer moves.** I am aware that this is the
result I had a stake in, so I am stating the counterfactual explicitly rather than leaving the
disclosure as a formality:

- Had **region 11** (L90) or **regions 8/9/10** (Table 1 caption, Drive row, Memory row) failed, the
  entire representation- vs partition-dependence framing would fall and **every "Partition required?"
  cell** in my §2.1 table would have to be rewritten.
- Had **region 13** (L99–111, the insert with no v1.25 antecedent — which I read most closely for
  exactly this reason), **region 29** (L248), **region 42** (L383) or **region 76** (L592–596) failed,
  my §2.2 finding that the prediction layer is dynamically bottlenecked would lose its support, since
  that finding rests on the six-declaration protocol and on V/I being load-bearing.
- Had **region 14** (L125) failed, my Drive "time-asymmetry required" answer and its R clause would
  fall.

None of those failed. The four defects I did find are disjoint from my 29 relied-on lines: D-1 is in
the change set, not canon; **D-2 sits at L40, which is not one of my 29 lines**; D-3 concerns §5 text
that does not exist (my Memory answers rest on §5 L194/L196, which are byte-identical carryover and
therefore untouched); D-4 is a citation in the change set. So my Step 0 conclusions are unaffected —
not because I declined to fail anything, but because the regions they depend on hold.

One asymmetry I should name: I found D-2 (a live-body inconsistency) at a line **outside** my
dependency set, and found nothing at any of the 20 lines inside it. I have no way to prove that is not
motivated reading. What I can offer is the mechanical work: the invariant multisets, the revert hash,
and the counted verification of both build-record assertions are all reproducible from the two
Drive files without reference to my judgement, and they are reported below in full.

---

## §3.1 — Region-by-region (all 85)

Verdict key as ordered. Line ranges are in the change set's own convention (see note above), so every
row is directly comparable to change set §4. "Splice" in the evidence column means `difflib` paired a
v1.25 deletion against an unrelated v1.26 insertion because both sit at the same alignment point; in
those cases **both sides are separately authorized** and I name the task for each.

| # | Op | v1.25 | v1.26 | Authorizing change-set edit | Verdict | Evidence |
|---|---|---|---|---|---|---|
| 1 | replace | 13–13 | 13–13 | §0/§1 (output master) + aggregate Tasks 6–21 | **AUTHORIZED-FAITHFUL** | Masthead version/date restamp + v1.26 summary sentence. No single task enumerates the masthead; the restamp is housekeeping incident to the fold and every clause of the summary maps to a Task 6–21 disposition. Historical masthead narrative below the new sentence is byte-identical. |
| 2 | replace | 17–17 | 17–17 | Tasks 2, 8, 13, 14.3, 18b, 20c, 21 | **AUTHORIZED-FAITHFUL** | Abstract. All seven edits present: 'dissociate generically'→'throughout the declared Gaussian ensemble'; MFPT-as-lead-of-family; declaration-relative semantics; rename + positivity-does-not-license; operational domain; coalition default; 'motivating' cases. |
| 3 | delete | 22–41 | (at 21) | Task 19a (disclosed as flag F-6) | **AUTHORIZED-FAITHFUL** | Head-of-paper 'note on the word life' deleted entire (20 lines). The change set authorizes and discloses the whole-note move as larger than the literal instruction (F-6). Faithful to the change set as written. |
| 4 | replace | 48–48 | 28–28 | Task 8 | **AUTHORIZED-FAITHFUL** | §1. Persistence-functional family + four named inappropriate regimes; occupancy argument explicitly reinforced with the 5.7× / 1e-14 gate, not weakened, as Task 8 requires. |
| 5 | replace | 54–54 | 34–34 | Task 14.3 | **AUTHORIZED-FAITHFUL** | §1 no-ownership paragraph: 'one individual rather than many' → diagnostic; positivity→individual inference marked deleted. |
| 6 | replace | 60–60 | 40–40 | Task 9 | **AUTHORIZED-FAITHFUL** | §1 spore demoted to thought experiment; 'not offered as a computed witness' present. See defect D-2: this line retains the flame's 'essentially no memory', which §11 L395 explicitly corrects. |
| 7 | replace | 63–72 | 43–53 | Tasks 6, 15, 19a | **AUTHORIZED-FAITHFUL** | End of §1. 'The ontology, fixed once' block present with all five items (nodes/proxies/edges/reliability/lifetime) plus both cross-loading consequences (B4, B5) and the panel-reading clause. Task 15's single retained diachronic sentence present. §12″ cross-referenced. |
| 8 | replace | 82–82 | 63–63 | Task 7 | **AUTHORIZED-FAITHFUL** | Table 1 caption: 'Two are cleanly computable' → 'All four are declaration-relative', exactly as specified. |
| 9 | replace | 97–97 | 78–78 | Task 7 | **AUTHORIZED-FAITHFUL** | Table 1 Drive row: 'None: cleanly computable' → representation-dependent, and names R directly as Task 7 requires. |
| 10 | replace | 102–102 | 83–83 | Task 7 | **AUTHORIZED-FAITHFUL** | Table 1 Memory row: declared observable, grain δt, stationarity claim. |
| 11 | replace | 109–109 | 90–90 | Task 7 (coupled to Task 11) | **AUTHORIZED-FAITHFUL** | TIER 1. §2 body rewritten to representation-dependence (all four) vs partition-dependence (B, I additionally). Every 'no choices to make' claim deleted or negated; R wired to §12″ and the §4 fourth condition. |
| 12 | replace | 115–115 | 96–96 | Task 20a | **AUTHORIZED-FAITHFUL** | §3: KW intervene on the system–environment channel; internal-edge intervention named AOP's extension; 'nothing in the parent result licenses it' present; all language implying the parent validates internal-edge deletion removed. |
| 13 | insert | (after 117) | 99–111 | Tasks 20a, 20c | **AUTHORIZED-FAITHFUL** | TIER 1, no v1.25 antecedent — read closest. All six mandatory declarations present and individually specified (mechanism / physical operation / held fixed / resource flow / preserved properties / class M). Coalition block present with all four objects + hypergraph + Shapley-as-summary + the plainly-stated reason for demotion. Both blocks carry [SYNTHESIS]. |
| 14 | replace | 131–131 | 125–125 | Tasks 11.1, 9, ORANGE-5 | **AUTHORIZED-FAITHFUL** | TIER 1. 'three conditions'→'four'; parity condition inserted as Third with both forms (all-even, or stationary one-point invariant under the involution); silent on odd variables; Spinney & Ford / Ford & Spinney cited; grade explicitly unchanged (forced × theorem/corollary). Task 9's three notions separated with the category error named. D→M spoke demoted to a scoped theorem box. |
| 15 | replace | 141–141 | 135–135 | Tasks 14.1, 14.2, 14.3 | **AUTHORIZED-FAITHFUL** | §4. Renamed to minimum-cut dependence; Provenance block states the Σ=(I+gL)⁻¹ construction is AOP's, built in Aguilera & Di Paolo's lineage, not their measure imported; 'What positivity does not license' block present with the full individuation panel and the shared-driver caveat. |
| 16 | replace | 189–189 | 183–183 | Task 2 | **AUTHORIZED-FAITHFUL** | §4: 'confirms the dissociation is generic' → 'occurs throughout the declared Gaussian ensemble rather than only at hand-built corners'. phaseE1 numbers (0.59, ≥4000) byte-identical. |
| 17 | delete | 193–242 | (at 186) | Task 15 | **AUTHORIZED-FAITHFUL** | §4a deleted from the core (50 lines) for relocation to the follow-on §7. |
| 18 | insert | (after 255) | 200–201 | Task 19 'one item moved the other way' (flag F-7) | **AUTHORIZED-FAITHFUL** | Memory-axis semantic-weight computation inserted into the core at §5 L200, immediately after the E(T) retention-depth paragraph, exactly as stated. Placement disclosed as F-7. |
| 19 | replace | 260–260 | 206–206 | Task 12 | **AUTHORIZED-FAITHFUL** | §6: plane → two independent tags; 'Persistence lives up-and-to-the-right' removed from this line. |
| 20 | replace | 262–262 | 208–208 | Task 12 | **AUTHORIZED-FAITHFUL** | §6: up-and-to-the-right explicitly withdrawn with the reason (classes are categorical, not ordinal; a forced edge can be inert, a free edge load-bearing). |
| 21 | replace | 264–264 | 210–210 | Task 12 | **AUTHORIZED-FAITHFUL** | §6: horizontal-as-interval concession preserved and reconciled with a categorical vertical, as Task 12 requires. |
| 22 | replace | 266–266 | 212–218 | Task 20b | **AUTHORIZED-FAITHFUL** | §6 subsection retitled 'A domain map for the edge-attribution estimator'; both implications explicitly blocked (common input; synergy); uncertainty-relation analogy withdrawn as more than decorative. |
| 23 | replace | 274–274 | 226–226 | Task 20b | **AUTHORIZED-FAITHFUL** | Topology-ratio result scoped to the declared synthetic family and Figure TF's five wirings. |
| 24 | replace | 280–280 | 232–232 | Task 12 | **AUTHORIZED-FAITHFUL** | Figure 2 caption replaced by Table 2′ caption; rows stated categorical and unordered. |
| 25 | replace | 282–282 | 234–240 | Task 12 | **AUTHORIZED-FAITHFUL** | The Table 2′ ledger itself: five categorical rows (forced / conditional / free-or-feasibility-constrained / reclassified / dissociable-substrate-sharing), each with edges and a semantic interval — exactly the five specified. |
| 26 | replace | 284–284 | 242–242 | Tasks 12, 13 (diff-alignment splice) | **AUTHORIZED-FAITHFUL** | Both sides authorized: v1.25's §7 observer-as-viability paragraph is deleted per Task 13; v1.26's line is the Table 2′ closing caution per Task 12. |
| 27 | replace | 286–286 | 244–244 | Task 13 (splice) | **AUTHORIZED-FAITHFUL** | v1.25's homunculus chain deleted per Task 13; v1.26's line is the retitled §7 header 'The observer, located: semantic claims are declaration-relative'. |
| 28 | replace | 288–288 | 246–246 | Task 13 | **AUTHORIZED-FAITHFUL** | §7: 'the system is its own observer' withdrawn as a formulation; legitimate half preserved verbatim (meaningful *to* a system relative to *its* viability, functional evaluated on the system's viable set); illegitimate half (system performs the evaluation) removed; semantic weight restated as three-place. |
| 29 | replace | 290–290 | 248–248 | Tasks 13, 18c (splice) | **AUTHORIZED-FAITHFUL** | TIER 1. v1.25 side is the gravity/screening anti-boundary paragraph, deleted per Task 18c; v1.26 side is the homunculus-by-disclosure paragraph per Task 13 — containment strengthened, analyst named as declarer and written into D. |
| 30 | replace | 292–292 | 250–250 | Tasks 18a, 18c (splice) | **AUTHORIZED-FAITHFUL** | Figure 3 and its caption deleted per Task 18a; v1.26 line is the retitled §8 header 'Interfaces: passive and actively maintained' per Task 18c. |
| 31 | replace | 294–294 | 252–252 | Task 18c | **AUTHORIZED-FAITHFUL** | §8 narrow retained statement, verbatim in intent: an interface is passive or actively maintained, and screenable interactions make passive interfaces cheap. |
| 32 | replace | 296–296 | 254–254 | Tasks 18a, 18c | **AUTHORIZED-FAITHFUL** | §8 'What is deleted' block enumerates every removal Task 18 specifies: EM-uniqueness, strong/weak disqualification, unscreened-gravity-implies-no-boundary, non-additivity-implies-Integration-floor, light-cone-as-boundary, Figures 3 and 4. |
| 33 | replace | 298–298 | 256–258 | Task 18c | **AUTHORIZED-FAITHFUL** | B2/B5 computation retained verbatim (B2 = 0.000 / 0.292; B5 = 0.896 / 1.685) with the added sentence that it is a property of the declared Gaussian model and never depended on the taxonomy. Star's two-interface insight retained in demoted form (actively maintained photosphere on a passive gravitational interface, only one paid for); atom's version deleted. |
| 34 | replace | 309–309 | 269–269 | Task 14.1 | **AUTHORIZED-FAITHFUL** | §9a rename. |
| 35 | replace | 313–313 | 273–273 | Task 14.1 | **AUTHORIZED-FAITHFUL** | §9a rename. |
| 36 | replace | 323–323 | 283–283 | Tasks 14.1, 14.3 | **AUTHORIZED-FAITHFUL** | §9 rename + individuation-panel qualifier added. |
| 37 | replace | 347–347 | 307–307 | Tasks 14.1, 14.3 | **AUTHORIZED-FAITHFUL** | §9 'fixes when a set of parts is one thing' → 'supplies one coordinate on whether a set of parts is jointly irreducible'. |
| 38 | replace | 371–377 | 331–344 | Task 14.3 | **AUTHORIZED-FAITHFUL** | §9a synchronic claim removed, with the stated reason (it contradicted the §13a level-selection retraction, so deleted rather than hedged) — exactly as Task 14.3 specifies. |
| 39 | replace | 397–412 | 364–375 | Task 19 | **AUTHORIZED-FAITHFUL** | §9a collective-alive frontier question relocated to the follow-on; core retains a shorter pointer, as Task 19 specifies. |
| 40 | replace | 416–416 | 379–379 | Task 18b | **AUTHORIZED-FAITHFUL** | §10 retitled 'The domain and its edge: an operational scope condition'. |
| 41 | replace | 418–418 | 381–381 | Task 18b | **AUTHORIZED-FAITHFUL** | §10 opening: binding/worldline/rest-mass admission construction removed, replaced by the operational question. |
| 42 | replace | 420–420 | 383–383 | Task 18b | **AUTHORIZED-FAITHFUL** | TIER 1. §10 domain wall *entirely replaced* by the five declarations (subsystem, state representation incl. δt and R, persistence functional V, horizon τ, intervention class I) with the note that all five are already slots in D. |
| 43 | replace | 422–422 | 385–385 | Task 18b | **AUTHORIZED-FAITHFUL** | §10 'What is deleted': 'binding, not rest mass, draws the wall', binding-as-admission-criterion, and the rest-frame / proper-time / invariant-mass reading all named as removed. |
| 44 | replace | 424–424 | 387–387 | Task 18b | **AUTHORIZED-FAITHFUL** | §10: both required consequences stated — admission is a property of the description, not the object; 'rest mass as the price of persistence' does not survive in any form. |
| 45 | replace | 426–426 | 389–389 | Task 21 | **AUTHORIZED-FAITHFUL** | §11 retitled 'Five motivating cases' (splice: v1.25 side is the §11 opening paragraph, rewritten at region 46). |
| 46 | replace | 428–428 | 391–391 | Tasks 21, 7 | **AUTHORIZED-FAITHFUL** | §11 opening: 'These are motivating cases and illustrations. They are not the framework's evidence for anything'; all four axes restated as declaration-relative per Task 7's sweep. |
| 47 | replace | 430–430 | 393–393 | Task 21 (splice) | **AUTHORIZED-FAITHFUL** | Figure 5 caption; Task 6/7 sweep applied ('all four are declaration-relative'). |
| 48 | replace | 432–432 | 395–395 | Tasks 1, 21, 9 | **AUTHORIZED-FAITHFUL** | Crystal sentence rewritten to the passive-load-bearing reading (lattice bears weight; disrupt it and the crystal ceases; costs no drive; what was spent is the growth front) — Task 1, with its stated one-word compression. Flame → 'shallow or short-lived memory' with the reason. Spore demoted with 'no Cμ is computed or claimed'. NOTE: the change set cites this edit at v1.26 L393; it is actually at L395 (splice offset) — see D-4. |
| 49 | replace | 434–434 | 397–399 | Tasks 3, 18a, 21 | **AUTHORIZED-FAITHFUL** | Atom: 'brief persister' struck, 'two boundaries' deleted, one cheap passive interface retained. Star: 'all four near maximal' struck with the internal contradiction named; negative-specific-heat thermostat retained as a model result [Lynden-Bell & Wood 1968; Campa et al. 2009]; the three-features-common-root synthesis deleted. Task 3: O-information re-attributed to the declared polytropic shell covariance, consequent re-attributed, and the added line that 'the star is redundancy-dominated' is not licensed. Ω > 0 computation unchanged. |
| 50 | replace | 440–440 | 405–405 | Task 21 | **AUTHORIZED-FAITHFUL** | §11 closing: 'primary evidence' deleted; all five reclassified as motivating; 'a carving is justified by the distinctions it refuses to lose' retained verbatim and identified as the honest taxonomic argument; flame and spore demotions in matching language. |
| 51 | replace | 443–511 | 408–408 | Task 19 | **AUTHORIZED-FAITHFUL** | §11a (69 lines) replaced by the one-paragraph core pointer; retitled 'A regulatory architecture that separates classes of persisters'. Task 19c's subspace restatement present with both required sentences (similarity-transform invariance; basis change not in I). |
| 52 | replace | 513–537 | 410–410 | Tasks 19, 19b | **AUTHORIZED-FAITHFUL** | Virion/mule and alive/pausable material removed from the core for relocation; the three-architecture contrast retained without the life predicate. |
| 53 | replace | 539–574 | 412–412 | Tasks 19, 19a | **AUTHORIZED-FAITHFUL** | Core states the architecture is 'not named alive', names the follow-on destination, and states the separation is scope discipline, not retraction — the de-announcement Task 19a specifies. |
| 54 | replace | 577–577 | 415–415 | Task 10 | **AUTHORIZED-FAITHFUL** | §11b retitled 'A unit test of the semantic intervention protocol'. |
| 55 | replace | 579–579 | 417–417 | Task 10 | **AUTHORIZED-FAITHFUL** | §11b opening necessity claim removed ('...apparatus is *necessary*' gone); restated as a unit test of the instrument. |
| 56 | replace | 585–585 | 423–423 | Task 10 | **AUTHORIZED-FAITHFUL** | §11b closing necessity claim removed and the withdrawal stated with all three reasons Task 10 requires (self-authored answer key; same hands; no rival run), with necessity deferred to the external benchmark. Coalition layer retained and presented as the argument for the Task 20c default; single-edge deletion reporting the redundant pair as inert retained. |
| 57 | replace | 606–606 | 444–444 | Task 11.1 | **AUTHORIZED-FAITHFUL** | §12 Table 3 D→M row carries the fourth condition and the explicit 'grade is unchanged — scope addition, not a reproof'. |
| 58 | replace | 612–614 | 450–452 | Task 18 | **AUTHORIZED-FAITHFUL** | §12 Table 3 screenability row rewritten; deletions enumerated; B2/B5 numbers carried. |
| 59 | replace | 620–622 | 458–460 | Tasks 20a, 20c, 10 | **AUTHORIZED-FAITHFUL** | §12 Table 3 mask row: extension named and specified, six declarations listed, coalition default stated, necessity claim marked withdrawn. |
| 60 | replace | 624–626 | 462–464 | Task 20b | **AUTHORIZED-FAITHFUL** | §12 Table 3 row retitled to the domain map, regraded, both blocked inferences carried. |
| 61 | replace | 632–634 | 470–472 | Tasks 14.1, 14.2, 14.3 | **AUTHORIZED-FAITHFUL** | §12 Table 3 row renamed; lineage-not-source stated; positivity→individual deleted; individuation panel named. |
| 62 | replace | 636–636 | 474–474 | Task 13 | **AUTHORIZED-FAITHFUL** | §12 Table 3 row retitled 'Semantic claims are declaration-relative; homunculus contained by disclosure'. |
| 63 | replace | 638–638 | 476–476 | Task 13 | **AUTHORIZED-FAITHFUL** | §12 Table 3 basis rewritten to match §7. |
| 64 | replace | 640–642 | 478–480 | Tasks 18b, 18 (flag F-4) | **AUTHORIZED-FAITHFUL** | §12 Table 3 domain row replaced; bounding-principle consequence flagged for decision, not decided — consistent with F-4. |
| 65 | replace | 644–646 | 482–484 | Task 18c | **AUTHORIZED-FAITHFUL** | §12 Table 3 gravity row: two of three consequents deleted (anti-boundary, Integration floor); star self-regulation retained as a model result. |
| 66 | replace | 652–666 | 490–492 | Tasks 19, 19b, 19c | **AUTHORIZED-FAITHFUL** | §12 Table 3 life rows collapsed to the regulatory-architecture row; relocation enumerated; six-part conjunction labelled an AOP hypothesis; Francis & Wonham and Bich et al. reattached to components only; 'the internal-model requirement of life' retired as a description. |
| 67 | replace | 670–670 | 496–496 | Task 14.1 | **AUTHORIZED-FAITHFUL** | §12 Table 3 lineage row rename + panel qualifier. |
| 68 | replace | 673–674 | 499–500 | Tasks 14.3, 19 | **AUTHORIZED-FAITHFUL** | §12 Table 3 collective row: synchronic individuality claim marked deleted with the §13a-inconsistency reason; collective-alive question relocated. |
| 69 | replace | 680–680 | 506–506 | Task 14.1 | **AUTHORIZED-FAITHFUL** | Gate-ledger prose rename. |
| 70 | replace | 709–710 | 535–536 | Tasks 14.1, 14.3 | **AUTHORIZED-FAITHFUL** | Gate-ledger individuation row renamed; note added that the gate established distinctness, not individuality. |
| 71 | replace | 747–747 | 573–573 | Task 11.1 | **AUTHORIZED-FAITHFUL** | Table 3′ D→M row: 'forced (four scope conditions, incl. time-reversal parity) × theorem/corollary' — dependency qualified, grade held. |
| 72 | replace | 750–750 | 576–576 | Task 18 | **AUTHORIZED-FAITHFUL** | Table 3′ screenability row → conditionally-forced (declared Gaussian model + interface F) × analytic-model-result, with force-taxonomy and causal-boundary rows marked deleted. This is the row whose departure produces the single-row hard floor. |
| 73 | replace | 752–757 | 578–583 | Tasks 10, 14, 19, 20a | **AUTHORIZED-FAITHFUL** | Table 3′ six rows updated: mask+protocol, unit test (necessity withdrawn), minimum-cut dependence (individuality deleted), collective individuality (withdrawn), collective lineage (relocated), regulatory architecture (life reading relocated). |
| 74 | replace | 759–759 | 585–586 | Tasks 21, 18b | **AUTHORIZED-FAITHFUL** | Table 3′ carving row demoted to 'motivating illustration — not evidence'; new domain-of-applicability row added per Task 18b. |
| 75 | replace | 761–761 | 588–588 | Task 18 | **AUTHORIZED-FAITHFUL** | §12′ 'Reading the ledger' states the hard floor is one row, not two, and names the subtraction rather than absorbing it — exactly the consequence Task 18 requires to be recorded. Verified by count, not by reading: see invariant I-4. |
| 76 | replace | 765–765 | 592–596 | Tasks 6, 11.2, 13, 20c | **AUTHORIZED-FAITHFUL** | TIER 1. §12″: R named in the tuple gloss; three-slot load-bearing block for R, V, I present; R wired to the §4 fourth condition; V tied to §7 and the persistence-functional family; I tied to the §3 protocol and the §11a basis argument. Task 11.2's 'strengthened, not added' posture (F-2) is what the text does. Coalition default propagated. Ontology cross-referenced in both directions per Task 6. |
| 77 | replace | 769–769 | 600–604 | Tasks 7, 13, 18, 20b, 20c (flag F-4) | **AUTHORIZED-FAITHFUL** | §13 exposure restated from three places to four, the fourth being the shrunken settled core, stated as a deliberate uncompensated subtraction. Bounding-principle status flagged for decision. External benchmark named as the principal missing evidence with all three requirements and deferred. |
| 78 | replace | 773–773 | 608–608 | Tasks 20b, 20c, 14.1, 18b | **AUTHORIZED-FAITHFUL** | TIER 1. §13: resolvability limit → domain map throughout; per-edge band retained with κ ≲ 9 / gap > 3× blur / TC ≈ 0.5; 'per-edge' qualifier added to the reach failure; coalition default named as the response; rename applied; domain-end sentence replaced with the five-declaration formulation; flame and star wording brought into line. |
| 79 | replace | 777–777 | 612–612 | Task 14.1 | **AUTHORIZED-FAITHFUL** | §13a rename. |
| 80 | replace | 779–779 | 614–614 | Task 14.1 | **AUTHORIZED-FAITHFUL** | §13a rename. |
| 81 | replace | 783–783 | 618–618 | Task 14.1 | **AUTHORIZED-FAITHFUL** | §13a rename (three occurrences in one line). |
| 82 | replace | 789–789 | 624–624 | Tasks 18b, 12, 14.1, 10 | **AUTHORIZED-FAITHFUL** | Data Accessibility: invariant-mass check withdrawn with the binding domain wall, script retained as record supporting no claim; Figures 3 and 4 recorded as deleted; Figure 2 recorded as replaced by Table 2′; benchmark → unit test; renames applied. |
| 83 | replace | 791–791 | 626–626 | Tasks 3, 14.1 | **AUTHORIZED-FAITHFUL** | Data Accessibility script list: phaseC3 description updated to 'O-information sign of the declared polytropic shell covariance' exactly as Task 3 requires; phaseD1/D2 renamed. |
| 84 | replace | 835–835 | 670–674 | Task 14.2 + §3 reference-list changes | **AUTHORIZED-FAITHFUL** | Aguilera & Di Paolo annotated with the lineage-not-source statement and a ⚠ retrieval residual explicitly marked not-line-checked. Both Spinney/Ford entries added with the opposite-author-order conflation warning and the unretrieved PRL Publisher's Note pointer. No reference removed. |
| 85 | insert | (after 997) | 837–851 | §4 certification ('the only addition after line 835 is the appended v1.26 entry') | **AUTHORIZED-FAITHFUL** | v1.26 changelog entry appended (15 lines). Its 16 numbered items correspond to the Task 6–21 dispositions; it states the fold is subtraction/relocation/regrading/specification with no new science, flags the bounding-principle decision for Ben, and declares the version a proposal that is not self-certified. |

**Summary:** 85 AUTHORIZED-FAITHFUL · 0 AUTHORIZED-DIVERGENT · 0 UNAUTHORIZED · 1 SPECIFIED-NOT-APPLIED
(D-3, reported individually above).

**On the four disclosed flags.** F-2 (R already present, strengthened not added), F-3 (version history
not swept), F-6 (life note moved entire), F-7 (Memory computation moved into the core) are all
divergences from the *tasking order* that the *change set* discloses and authorizes. Since this order
directs me to verify v1.26 against the change set, regions implementing them are AUTHORIZED-FAITHFUL.
I confirmed each is what the text actually does — in particular F-3: see invariant I-5.

---

## §3.3 — Invariants (multisets, v1.25 → v1.26)

### I-1. Citations

| Measure | v1.25 | v1.26 | Δ | Authorized? |
|---|---|---|---|---|
| Reference-list entries | 69 | 71 | **+2** | Yes — change set §3 adds exactly Spinney & Ford (PRE 85, 2012) and Ford & Spinney (PRE 86, 2012). |
| Entries removed | — | — | **0** | Matches change set §3: "No reference was removed." Verified as a multiset difference on (first author, year), not by count alone. |
| Inline bracketed-year markers | 93 | 74 | −19 | Yes — carried out with the §4a deletion (Parfit, DiFrisco), the §11a relocation (Ashby, Francis & Wonham, Bich, Conant & Ashby, Varela, Moreno & Mossio), the virion/mule block (Joyce, Cleland & Chyba, Chodasewicz), and Figures 3/4. All are relocations to the follow-on or authorized deletions; no source is orphaned in the reference list. |

### I-2. Grade tags

The canon carries grades in two distinct registers, and both must be counted separately.

**(a) Bracketed inline grade markers** `**[...]**`: **15 → 11**.

| Direction | Marker | Authorized by |
|---|---|---|
| removed | `[FRONTIER; stated as of July 2026.]` | Task 19a (head-of-paper life note) |
| removed | `[SETTLED named view; the mapping is SYNTHESIS.]` | Task 15 (§4a) |
| removed | `[SYNTHESIS.]` ×3 | Tasks 15, 19 (§4a, §11a tiers, death) |
| removed | `[SYNTHESIS; FRONTIER at the formal treatment of branching.]` | Task 15 (fission) |
| removed | `[The definition of *alive* is FRONTIER …]` | Task 19a |
| removed | `[SYNTHESIS, computed.]` | Task 19 (Figure LT) |
| removed | `[SYNTHESIS; well-supported by the definition-of-life literature.]` | Task 19 (virion/mule) |
| added | `[Scope addition only. The theorem's grade is unchanged: forced × theorem/corollary…]` | Task 11.1 |
| added | `[SYNTHESIS; the construction is this framework's, the lineage is cited as inspiration.]` | Task 14.2 |
| added | `[SYNTHESIS, narrowed; the individuality verdict is withdrawn.]` | Task 14.3 |
| added | `[Pointer only; the question and its frontier grade live in the follow-on.]` | Task 19 |
| added | `[SYNTHESIS; the architecture is a coupling fact…]` | Task 19a |

Every one of the 8 removals is a relocation to the follow-on or an authorized deletion; every one of
the 5 additions is a named task. **No grade was silently downgraded or upgraded.**

**(b) Two-axis dependency × evidential pairs.** Bare `forced × theorem/corollary` (excluding
`conditionally-forced`): **2 → 6 occurrences**, but the *rows* went 2 → 1. The occurrence count rises
because Task 11.1 requires the unchanged grade to be stated three additional times (§4 body L125,
Table 3 row L443, and the §12′ reading L588) plus once in the changelog. This is the opposite of grade
inflation: the same single claim is asserted more often, precisely to document that a scope addition
did not reprove it. See I-4 for the row count, which is the load-bearing number.

### I-3. Section headers: 24 → 23

| Direction | Header | Authorized by |
|---|---|---|
| deleted | `### 4a Diachronic individuation: when two slices are one process` | Task 15 |
| retitled | `A resolvability limit: the mask blurs as Integration rises` → `A domain map for the edge-attribution estimator` | Task 20b |
| retitled | `7The observer, located` → `…: semantic claims are declaration-relative` | Task 13 |
| retitled | `8What can make a boundary: screenability` → `8Interfaces: passive and actively maintained` | Task 18c |
| retitled | `10The domain and its edge: binding, not rest mass` → `…: an operational scope condition` | Task 18b |
| retitled | `11Five worked cases` → `11Five motivating cases` | Task 21 |
| retitled | `11a The living threshold: continue, correct, and correct-against-a-model` → `11a A regulatory architecture that separates classes of persisters` | Task 19a |
| retitled | `11b An exactly-solvable non-triviality benchmark` → `11b A unit test of the semantic intervention protocol` | Task 10 |

Net −1 is the §4a deletion. All eight changes authorized; **no header appears or disappears
unaccounted for.**

### I-4. The build record's two counted assertions — verified by counting, not by reading

**(a) "The physics block was cut."** CONFIRMED. Counted across the whole file, every surviving
occurrence of the physics vocabulary sits inside a *deletion record* or a *changelog entry*, never in
a live claim:

| Phrase | v1.25 | v1.26 | Where the v1.26 survivors are |
|---|---|---|---|
| `Figure 3` | 2 | **0** | — |
| `Figure 4` | 5 | **0** | — |
| `light cone` | 4 | 3 | L254 (§8 "What is deleted"), L452 (Table 3 deletion record), L844 (changelog) |
| `causal boundary` | 9 | 3 | same three deletion records |
| `anti-boundary` | 4 | 2 | deletion records only |
| `rest frame` / `proper time` | 4 / 4 | 3 / 3 | L385 (§10 "What is deleted"), L844 (changelog) |
| `strong interaction` | 1 | **0** | — |
| `weak interaction` | 1 | 4 | all four are deletion records enumerating what was removed (L254, L452, L602, L844) |
| `one-way membrane` | 1 | 2 | both deletion records (L254, L844) |

Two counts *rose* (`weak interaction`, `one-way membrane`). I checked each occurrence individually:
the increase is caused by the removal being *documented* in four places (§8, Table 3, §13
bounding-principle flag, changelog), which is what Task 18 requires. **No live claim survives.**

**(b) "The settled core is down to a single forced × theorem/corollary row."** CONFIRMED by parsing the
Table 3′ dependency column:

- v1.25: **2** rows with dependency exactly `forced` — `D→M memory floor, direction σ>0 ⇒ E>0` and
  `Screenability & causal boundary`.
- v1.26: **1** row — `D→M memory floor, direction σ>0 ⇒ E>0 | forced (four scope conditions, incl.
  time-reversal parity) | theorem/corollary`.

The screenability row is now `conditionally-forced (declared Gaussian model + interface F) ×
analytic-model-result`. Table 3′ row count 13 → 14 (the domain-of-applicability row is added per Task
18b; no row is dropped — `Collective individuality (§9a synchronic)` is retained as an explicit
`**withdrawn v1.26**` row rather than deleted, which is the honest form).

### I-5. F-3 residual — the unswept version history, quantified

`Φ_MIP` occurrences: **50 → 22**. Of the 22 survivors, **19 are historical** (masthead narrative L13,
and changelog entries L726–L842) and **3 are live body**, each legitimate:

- **L135** — deliberate symbol retention: "written Φ_MIP where the symbol is convenient, but read
  throughout as a *minimum-cut irreducibility diagnostic*". Task 14.1 explicitly permits retention
  "where explicitly labelled as a symbol."
- **L332** — quoting the claim being deleted: "Versions ≤1.25 stated that a collective with Φ_MIP > 0
  … **That claim is deleted in v1.26.**"
- **L470** — "formerly Φ_MIP", describing what was renamed.

F-3 is therefore accurate and its residual is bounded and benign. The changelog's own opening states
this: historical entries "are the record of what earlier versions said, not live claims."

### I-6. Preservation checks

- **v1.25 L836–997** (entire version history) appears **verbatim** in v1.26 at L675–836. The only
  material after it is the 15-line v1.26 entry at L837–851, exactly as change set §4 certifies.
- **v1.25 L139** (the "generically *builds* it" occurrence Task 2 says was correctly left alone,
  being a different sense) is present in v1.26 **byte-identical** (2,578 chars).
- **phaseE1 figures** untouched: `0.59 of its variance` (1→1), `≥4000 systems` (1→1), `phaseE1` (7→7).
- **B2/B5 screening residuals** retained verbatim: 0.000 / 0.292 and 0.896 / 1.685.

---

## §3.4 — Revert test

Reversing all 85 regions — taking the v1.25 side of every non-`equal` opcode and the v1.26 side of
every `equal` opcode — reproduces v1.25 **byte-for-byte**:

```
rebuilt md5    = 9c172e015f4adfc9fe827a42687ca2e7
v1.25 md5      = 9c172e015f4adfc9fe827a42687ca2e7   MATCH
rebuilt bytes  = 224,340   (exact)
string equality to v1.25 source = True
```

**Nothing moved that the diff did not attribute.** I also independently regenerated the opcode table
(`difflib.SequenceMatcher(None, a, b, autojunk=False)`) and confirmed it is **row-for-row identical**
to the 85-row table published in change set §4 — same ops, same order, same line ranges, no
discrepancy in any of the 85 rows. Structural counts reproduce: 657 equal lines, 80 replace / 3 insert
/ 2 delete. Both line-accounting identities close exactly:

```
997 = 657 equal + 270 replaced(a) + 70 deleted
851 = 657 equal + 164 replaced(b) + 30 inserted
```

These are the identities that expose **D-1**: the change set's "307" is consistent with neither side.

---

## §3.5 — Encoding

- **UTF-8 clean.** Both files decode as UTF-8 with no errors; `file -I` reports
  `text/plain; charset=utf-8`.
- **No mojibake.** Zero occurrences of `â€`, `Ã`, `Â`, `ï¿½`, or U+FFFD in either file. No BOM.
- **Both NBSPs accounted for.** Exactly 2 in v1.26 (matching prime's count) and exactly 2 in v1.25 —
  the *same two*, at **L11 columns 14 and 16**, in the masthead byline
  `⟨Affiliation⟩ ·  Correspondence: ⟨email⟩`, flanking the `·` separator. L11 is byte-identical
  carryover; **neither NBSP was introduced by this fold.**
- Non-ASCII inventory is otherwise ordinary typographic content (em/en dashes, `§`, arrows, Greek,
  `⚠`, curly quotes) and is consistent between versions.

---

## Integrity of inputs (verified before reading)

| Object | Drive ID | Expected | Observed | Result |
|---|---|---|---|---|
| v1.26 | `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn` | 254,046 B / md5 `54ceb3772e29f25c6e139b703d550d59` | 254,046 B / `54ceb3772e29f25c6e139b703d550d59` | **MATCH** |
| v1.25 | `13tI48fz-l5DundXuyQysPJf7JrSS9xck` | 224,340 B / md5 `9c172e015f4adfc9fe827a42687ca2e7` | 224,340 B / `9c172e015f4adfc9fe827a42687ca2e7` | **MATCH** |
| Change set | `1mI3DkOKD_GOJzf-ImDThA1oSsRo4iEMd` | — | 36,796 B / md5 `0fcd16d83000d411f549e5bd657201f8` | recorded |

sha256, v1.26: `2c298d47d170fd1c87a261ca988f1b831d9b02c7acb46fecfbcf955ebcf22271`
sha256, v1.25: `2db4fa5fdc7b912088183d362ee646385c76b073a3a9d0b628f997bb1d7f8c67`

The v1.26 Drive copy is `AOP_CANON_MASTER_v1.26.md`, modified 2026-07-25T02:47:35Z. **Read-only
throughout; the master was never re-uploaded.**

---

## Scope discipline

Per §6 of the order: I did not adjudicate Aster's blockers, did not repair any defect I found, did not
touch the benchmark line, and did not re-open Step 0. I did not edit the canon, rename any file, or
fold corrections. The build record was treated as a claim throughout — every assertion of CW's that
this note confirms was confirmed by independent count or hash, not by reading the record.

**What this verification does not establish.** It establishes that the 85 regions say what the change
set told CW to make them say. It does **not** establish that the change set's own instructions were
correct science, that the relocated life material survived intact in the follow-on (that file was not
in scope and was not read), or that the ⚠-marked retrieval residuals on Aguilera & Di Paolo and the
two Spinney/Ford entries are sound — those remain explicitly not line-checked, as v1.26 itself states.
