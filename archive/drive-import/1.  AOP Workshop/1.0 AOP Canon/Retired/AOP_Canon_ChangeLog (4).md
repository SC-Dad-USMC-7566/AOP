# AOP Canon — Change Log (running master)

**What this is.** A running, append-only ledger of changes to the AOP canon and its designation. It
implements the Shared Core's canon-break discipline: a change is recorded here the moment it happens,
so nothing is lost between deliberate change runs. A small change — a version-pointer bump, a
companion-document addition — does not warrant its own change run; it is logged here and folded into
the next one. The log is what makes deferral safe: a recorded change is not a silent drift.

**Scope.** This log covers the canon (the paper) and its designation (AOP_Canon). It does not cover
the charter — charter changes are governance, rare, and handled on their own. It does not restate
canon claims; it records *that* and *how* the canon moved, and points at the version that holds the
detail.

**How it works.**
- Every canon change gets one short entry: what changed, where, why, status (Pending / Reconciled).
- Pending entries wait at the top. A *change run* is a deliberate pass that reconciles them — it
  updates the canon designation, propagates anything downstream (the cross-project bus, if the Ladder
  is affected), and moves the entries to Reconciled with the date.
- Keep it cheap. An entry is a few lines. If logging a change turns into a project, it is over-built
  — cut it back.

**Fixed name.** This is a standing living file, appended continuously; it keeps a fixed name (no
version suffix), like the per-project Parking Lots and the Idea Inbox.

**Baseline.** The canon was designated at paper **v1.4** (AOP_Canon_v1_0.md, this session). Entries
below track movement from that datum.

---

## Pending — to fold into the next change run

*(none — reconciled in the 8 July 2026 (v1.11) change run below)*

---

## Change run — 15 July 2026 (v1.15, red-team hardening of the life/individuation fold)

Folded one canon movement; its entry is Reconciled as R9 (v1.14→v1.15). The designation
(AOP_Canon_v1_0.md) now names **v1.15** as canonical and holds the Drive master (aop_canon_v1_15.md).
This run hardens the v1.14 life/individuation material against an independent red-team, with all accepted
fixes additive (no reference added or removed, no claim retracted).

### R9 · Canon movement: v1.14 → v1.15 — reconciled 15 July 2026
- **What.** Five of six red-team findings accepted and folded; one rejected on primary-source grounds.
  (1) §11a living predicate split into two present-tense tiers — *alive* (model edge load-bearing now,
  mask-detectable, Figure LT) and *viable/pausable* (decoupled-reference architecture structurally
  present now, read off structure without a restart) — placing the dormant spore as *life paused*
  without the future-tense restart §9 forbids; the spore forces the tiers apart as it forces E and Cμ
  apart in §11. (2) §11a discriminator restated as architectural (does a separate, separately-
  interventable reference node exist?) not a timescale-separation magnitude, shown by a slow/fast sweep
  (Figure LT-T; deposited figure_LT_threshold.py) in which the model-edge weight is high, load-bearing,
  and flat across the star–cell window (≈0.79 at 2× to ≈0.72 at 20×) with no threshold knee. (3) §9
  higher-individual lineage route downgraded to FRONTIER (leans on the nested-level, non-stationary
  Φ_MIP extension §4 scopes out); existence-now route unchanged [synthesis]. (4) §4a transporter verdict
  re-grounded in the physical continuity-of-instantiation fact as a stipulated definition, Parfit 1984
  cited consistently rather than against itself. (5) "No self-model" claim scoped to the minimal/naked
  virion, giant-virus (Mimivirus, pandoraviruses) gray zone named as a test-application site. Cleanup:
  Conant & Ashby 1970 marked as background, not load-bearing, in the §11a antecedent list. Masthead →
  v1.15 (15 July 2026) + closing changelog paragraph.
- **Why.** Harden the newly-folded life/individuation material where the red-team found the framework
  overreaching in its own terms (present-tense scope in §11a; frontier scope in §9) or misusing a source
  (Parfit in §4a), per the reviewed response aop_v1_14_redteam_response.md.
- **Grade.** No grade promotions: the living-threshold definition stays FRONTIER, its components SETTLED,
  its consistency SYNTHESIS; the §9 higher-individual route is *demoted* synthesis→frontier. The two-tier
  split and the architectural-discriminator statement are SYNTHESIS, the second computed (Figure LT-T).
- **Verification.** Figure LT-T reproduced from deposited code (figure_LT_threshold.py, runs clean:
  cell-type sweep 0.788/0.717/0.383 at 2/20/100×, monotone, positive; star weight 0.796 arch=0, cell
  0.717 arch=1). Rejected "cleanup": the definition-of-life quotation was re-verified in the primary-
  source PDF body (Cleland & Chyba 2002, quoting Joyce 1994) as "a self-sustained chemical system capable
  of undergoing Darwinian evolution" — the proposed reversion to "self-sustaining … capable of Darwinian
  evolution" would reintroduce the misquote v1.13 review corrected; not applied.
- **Downstream.** No new hub-classification movement beyond v1.12/v1.14 (the tier split and discriminator
  refinement sit inside §11a/§9); the §9 scope wall is unchanged in force. Prior propagation-bus flag
  (v1.12/v1.14) still stands, left for posting.
- **Status.** Reconciled 15 July 2026. Canonical master held on Drive (aop_canon_v1_15.md).

---

## Change run — 9 July 2026 (v1.14, life/individuation fold)

Folded two canon movements; their entries are moved to Reconciled as R7 (v1.11→v1.12) and R8 (v1.12→v1.14). The designation (AOP_Canon_v1_0.md) now names **v1.14** as canonical and holds the Drive master (aop_canon_v1_14.md). R7 records the individuation GO entering Table 4 as the gate ledger's first GO row; R8 records the persistence→life→individuation fold (§11a living threshold with Figure LT, §4a diachronic individuation, §9 clarification) after adversarial testing and an independent hard review whose three corrections were applied in the fold.

### R8 · Canon movement: v1.12 → v1.14 — reconciled 9 July 2026
- **What.** Folded the persistence→life→individuation thread (proposed as a v1.13 integration draft on
  Drive) into the master as v1.14. Adds §11a "The living threshold" (*alive* = active self-maintenance
  correcting the regulated axes against a decoupled, separately-interventable internal model of the
  system's own viability), with Figure LT computing the discriminator on two closed-form OU systems;
  §4a diachronic individuation (continuity of instantiation / genidentity; transporter-vs-Theseus;
  speciation as process fission); a head-of-paper "life" caveat; a §1 refusal-preserving paragraph; a §9
  present-tense clarification (lineage continuation placed above AOP); a dated/removable recombination
  frontier note; six Table 3 status rows; eighteen references; and the changelog. Masthead → v1.14.
- **Why.** Give the framework a structural, substrate-independent threshold for *alive* and a diachronic
  companion to v1.12's synchronic Φ_MIP, per the user's instruction to draft v1.14 accepting all review
  recommendations.
- **Grade.** The definition of *alive* is FRONTIER (a new proposal measured against the settled NASA
  "chemical Darwinian" reference); its control-theory components are SETTLED; its internal consistency is
  SYNTHESIS, computed (Figure LT). Diachronic individuation is a SETTLED named view with the axis mapping
  as synthesis. Refusals narrowed nowhere: a structural category is added and fenced from metaphysics of
  selfhood (§1, §7).
- **Verification.** Hard review (aop_v1_13_review.md) checked load-bearing citations against primary
  sources; three corrections were applied in the fold: (i) the model-free/model-based distinction re-based
  on Francis–Wonham 1976 + Bich et al. 2015, with the good-regulator theorem [Conant & Ashby 1970]
  demoted to a historical antecedent (its "model" is a homomorphic image under which a bare fixed point
  counts); (ii) the definition-of-life quotation corrected to "a self-sustained chemical system capable of
  undergoing Darwinian evolution" and labelled the "chemical Darwinian" formulation [Joyce 1994; Cleland &
  Chyba 2002]; (iii) "genidentity" reattributed to its process-metaphysics origin, DiFrisco 2018 cited for
  its application. Figure LT reproduced from deposited code (figure_LT.py): cell model edge load-bearing
  (0.70) ∧ decoupled (20×) → inside; star coupling (0.01, 2×) and intrinsic restoring (0.55, 1×) → outside.
  Reference DOIs Crossref-verified; ⚠ items (Joyce 1994 foreword text; DiFrisco 2018 pagination/in-chapter
  terms; Ashby 1960 pagination) remain to verify in full text before the bibliography is called final.
- **Downstream.** Integration-side change touching the hub only through the mask (the living-threshold
  edge is a mask object); the scope wall at reproduction is a Ladder propagation-bus item. Bus note
  warranted, flagged, left for posting.
- **Status.** Reconciled 9 July 2026. Canonical master held on Drive (aop_canon_v1_14.md).

---

### R7 · Canon movement: v1.11 → v1.12 — reconciled 9 July 2026
- **What.** Folded the individuation GO into the canon as v1.12: Φ_MIP added as a graded, ownership-free
  one-vs-many individuation axis (§4 axis paragraph; §12 status row; a dedicated section; masthead), the
  "no individuation" refusal narrowed to "no ownership" (both halves stated together — ownership scalar
  still refused, PIC lesson stands; third-person coupling-based individuation admitted), and — per the
  user's explicit instruction — the GO entered in Table 4 as the gate ledger's first GO row, reframing the
  ledger as four cross-brick nulls plus one axis GO tested in both directions under one pre-registration.
- **Why.** Record the individuation gate's GO (all five pre-registered criteria passed) as a first-class
  canon result, per aop_individuation_GO_record.md.
- **Grade.** Framework synthesis, scoped static-Gaussian (Option 1); C1 zero-calibration and C5 coordinate
  well-posedness exact; nested level-selection and the non-stationary/critical extensions (Option 2)
  frontier. No ownership scalar; the PIC individuation refusal is narrowed, not dropped.
- **Verification.** Gate module (aop_individuation_gate.py) regenerates all five criteria end-to-end;
  every GO-row number cross-checked against gate output (C1 0/48; C5 exact; C3 matched pair
  2.800/1.856/Φ0 vs 2.792/1.911/Φ0.075; C4 ring 0.409 vs triangles 0).
- **Downstream.** Touches the hub classification the Ladder maps its rungs onto → cross-project bus note
  warranted, flagged, left for posting.
- **Status.** Reconciled 9 July 2026.

---

## Change run — 8 July 2026 (v1.11, cross-brick gate arc)

Folded the v1.10→v1.11 canon movement; the entry is moved to Reconciled as R6. The designation
(AOP_Canon_v1_0.md) now names **v1.11** as canonical and lists the v1.11 changelog among companions.
This run folds in a pre-registered search for a *forced* cross-brick coupling — an intervention on one
dimension's regime that provably moves another's admissible output through a shared mechanism, not a
shared input. Four gates were run (resolvability↔TUR at three read-outs; the E-vs-Cμ dormancy screen)
and all returned scoped nulls. The nulls are recorded as first-class results (new Table 4 gate ledger),
not omitted; the D→M memory floor is bounded to predictive memory (excess entropy) and shown by gate
to force no stored time-asymmetry (Ξ=Cμ⁺−Cμ⁻=0 at every drive) and no floor on stored complexity Cμ
(which covaries weakly with the drive parameter through the symmetric sector, not as a forced
consequence of the cost); and the shared reason for all four
nulls — the thermodynamic cost is a functional of the generator's antisymmetric sector while the
quantities carrying the forced claims (OU resolvability via Σ, and the asymmetry Ξ) are governed by its
time-symmetric sector, so no stored-structure quantity moves through the current as its mechanism — is
added as a synthesis-level structural note under the hub (§4) and a status-table row (§12), graded
synthesis and
secure only within the two model classes tested. One gate (E-vs-Cμ) first produced a spurious GO that an
adversarial re-test showed to be the entropy-production rate mislabeled as a memory asymmetry; it was
retracted in place and the retraction is shown in Table 4, not hidden. Resolvability's
coordinate-dependence is fixed by a stated K-convention (§6). **Propagation:** this run *does* touch the
hub classification the Ladder maps its rungs onto — the D→M spoke is now bounded and a new "no forced
Memory/structure↔Drive coupling" synthesis claim is added. A cross-project handoff note is warranted so
the Ladder and Time Machine threads learn the basement's hub gained a bound and a scoped negative; that
note is flagged here and left for posting (the bridge memo's rung mappings are not themselves changed,
but the hub's forced-spoke inventory is now explicitly closed at two).

### R6 · Canon movement: v1.10 → v1.11 — reconciled 8 July 2026
- **What.** Seven folded edits (G1–G7 in aop_v1_11_changelog.md), no reference added or removed
  (Barbed Arrow [13] and Parrondo–Van den Broeck–Kawai [1] were already present). §4 hub gains the
  bounded D→M edge + sector-split synthesis note; abstract hub line tightened; §12 gains a bounded D→M
  status row, a sector-split synthesis row, and the Table 4 gate ledger; §6 gains the K-convention
  coordinate-dependence note; masthead → v1.11 (8 July 2026) + closing note paragraph.
- **Why.** Fold the cross-brick gate arc (four pre-registered nulls + the sector-split positive) into
  the canon as first-class results, per the decision record aop_crossbrick_record_and_canon_actions.md.
- **Grade.** D→M floor unchanged (secure/scoped); the bounding negative and sector split are framework
  synthesis, frontier at the generalization beyond the Gaussian-OU and finite-Markov model classes.
- **Verification.** Physics check before editing confirmed the canon edge (σ>0⇒E>0, excess entropy) is
  a different Memory measure than the stored-complexity asymmetry Ξ the arc found drive-blind (Cμ
  magnitude covaries with drive; only Ξ=Cμ⁺−Cμ⁻ is exactly zero), so the arc sharpens
  rather than contradicts it; Ξ = Cμ⁺−Cμ⁻ source (arXiv:0902.1209) verified in body during the gate.
- **Downstream.** Hub-classification change → cross-project bus note warranted (flagged above, left for
  posting). Bridge-memo rung mappings unaffected in content; hub forced-spoke inventory now closed at
  two (E-floor, TUR).
- **Status.** Reconciled 8 July 2026.

---

## Change run — 7 July 2026 (v1.10, worked semantic mask)

Folded the v1.9→v1.10 canon movement; the entry is moved to Reconciled as R5. The designation
(AOP_Canon_v1_0.md) now names **v1.10** as canonical and lists the v1.10 changelog, the worked-mask
figure/script, and the verification verdict among companions. This run discharges the single structural
gap the v1.8 red-team named and every review since kept flagging: the semantic mask — the framework's
headline second layer — had never been *computed*, only described. An external contributor supplied a
worked instance; it was independently reproduced and pressure-tested before folding, and two claims in
the supplied material were found to overreach and were reframed rather than taken as given. No
cross-project handoff required — computing the mask on the paper's own Figure DM ring is internal and
moves no Ladder-facing rung mapping. The now-standing open item is narrower: compute the same mask on a
system whose part-partition is well posed, so the resolvability limit acts on the mask's own weights.

### R5 · Canon movement: v1.9 → v1.10 — reconciled 7 July 2026
- **What.** One folded change (E-mask), no reference added or removed. Figure MW computes the
  Kolchinsky–Wolpert [2] scramble-and-re-run mask on the internal couplings of the Figure DM driven
  three-state ring under three present-tense viability functionals (steady-state current, entropy
  production, relaxation rate): graded positive weights on the three driven ring edges, exactly zero on
  an added inert spectator, each load-bearing weight an interval across the functionals (the
  characteristic measurable), with a detailed-balance negative control returning zero everywhere. Edits
  to §3 (mask now computed, not only described), §13 (next step rewritten future→past; open item
  narrowed to a well-posed part-partition), the abstract, the §12 status table (Semantic-mask row →
  "definition + computed"), Data Accessibility (Figure MW added to the deposited list), and the closing
  reference note.
- **Two reframings applied, not taken as supplied.** Independent pressure-testing (300 random driven
  rate vectors) established that (a) the spectator's zero weight is exact by construction — scrambling an
  already-balanced coupling is a no-op — so it demonstrates the mask does not reward mere presence rather
  than discovering an inert coupling; and (b) the near-agreement of the three functionals on the most
  load-bearing edge is rate-specific (top edge agrees across all three only ~29% of random rate vectors),
  so the supplied note's link to the Comolatti–Hoel rank-survives regularity was dropped. Canon states
  both honestly.
- **Standing.** Like the star, Figure MW is a demonstration of self-consistency, not a confirmation that
  could have failed — stated with the figure.
- **References.** None added or removed; Kolchinsky & Wolpert [2] is now the cited procedure behind a
  computed figure. 27 entries retained.
- **Grade.** Mask procedure settled method [2]; extension to internal edges this framework's synthesis
  (§3, Table 3); the computation and controls computed and deposited.
- **Status.** Reconciled 7 July 2026. Designation updated; companion docs refreshed; deposited files
  (figure_MW_worked_mask.py/.png, aop_worked_mask_verdict.md) recorded.

---

## Change run — 6 July 2026 (v1.9, red-team pass)

Folded the v1.8→v1.9 canon movement; the entry is moved to Reconciled as R4. The designation
(AOP_Canon_v1_0.md) now names **v1.9** as canonical and lists the v1.9 changelog and the red-team
document among companions. This run answers an external red-team of v1.8: it verified the risky
citations and the load-bearing math and found no fabrication, leaving mechanical bugs plus structural
challenges. Every concrete red-team claim was re-checked before acting, by the
method appropriate to each: the Boyle 2025 author list was confirmed wrong against the Crossref
metadata record, and the Vazza "≈200 Myr" quote was confirmed present by reading the paper's PDF body
directly (the phrase appears four times) — Crossref verifies bibliographic metadata, not in-text quotes. No cross-project handoff required — all fixes and calibrations are internal to the paper and
move no Ladder-facing rung mapping. **One item deferred by decision:** computing a worked semantic
mask on a minimal model (the red-team's highest-leverage suggestion) is real new work with its own
modeling choice, is already named as the next step in Section 13, and is held for a scoped follow-up.

### R4 · Canon movement: v1.8 → v1.9 — reconciled 6 July 2026
- **What.** Five mechanical fixes (M1–M5) and four prose calibrations (S-A, S-C, S-D, S-E), no
  reference added or removed, no claim strengthened. M1: the resolvability family renamed Figure TF to
  end its collision with the §4 non-energy-triangle Figure T. M2: §8 anti-boundary cross-reference
  corrected to Figure 3. M3: the orphan Still–Sivak–Bell–Crooks citation [3] placed at the D→M spoke.
  M4: the σ-swing phrasing reconciled with Figure 1. M5: the Boyle et al. 2025 author list corrected
  against Crossref (Williams HTP removed; Moody, Babcock, McShea, Álvarez-Carretero, Donoghue restored).
  S-A: a stated embarrassment condition for the resolvability claim added to §13. S-C: the star marked
  in §11 as a demonstration of self-consistency, not a confirmation that could have failed. S-D: the
  abstract's four-axis claim aligned to the graded B–I/M–I finding ("four distinguishable axes, not
  four independent ones"). S-E: the flagship-in-the-silent-regime tension (the forced Memory law goes
  silent on the star's nuclear clock) named head-on in §11.
- **Why it holds together.** The four calibrations are all the same move — align stated confidence to
  what the body already shows — and all pull toward the charter's grading discipline rather than adding
  claims. The mechanical fixes are independent bugs.
- **References.** None added or removed; one author list corrected (M5). 27 entries retained.
- **Grade.** No grade changes. All edits are corrections or honest calibrations of existing claims.
- **Follow-up pass (F1–F3), same version.** A second review of the v1.9 text (7 July 2026) raised three
  more text fixes, applied without a version bump because they correct v1.9's own new prose: F1 rewrote
  the §13 falsification test — which had pinned width to *scalar* integration and so contradicted the
  topology-family result — into a topology-aware test (within a topology, VIF widens monotonically with
  coupling; at matched mean coupling the graded chain out-blurs degenerate mean-field), both verified on
  the deposited engine; F2 corrected the Still et al. [3] gloss direction (dissipation pays for the
  *nonpredictive* memory — β⟨W_diss⟩ = I_mem − I_pred), verified against the PDF body; F3 reconciled the
  Data Accessibility deposit list with the figure captions (all computed figures DM/T/R/TF/R★ listed;
  "illustrative" limited to 2/3/4/5). Canon re-saved (aop_v1_9.md v2); changelog updated. The one still-
  deferred red-team item (compute a semantic mask) is unchanged.
- **Status.** Reconciled 6 July 2026; follow-up F1–F3 folded 7 July 2026. Designation names v1.9;
  companion docs refreshed; the deferred semantic-mask computation is logged as the standing next step
  (Section 13), not a pending canon edit.

---

## Change run — 6 July 2026

Folded the v1.7→v1.8 canon movement in one deliberate pass; the entry is moved to Reconciled as R3.
The canon designation (AOP_Canon_v1_0.md) now names **v1.8** as canonical and carries the refreshed
companion-document list (v1.8 changelog; the stellar-structure-derived star model + Figure R★
superseding the v1.7 equicorrelation model; the topology family behind Figure T). This change run began
as a triage of a six-point critique of the v1.7 star work: two points were rebutted with evidence
(Campa read in full text on disk; the deposited R★ code computes 1/√λ_max as captioned) and are
recorded as rebuttals, four were conceded and three folded. No cross-project handoff was required —
rebuilding the star's coupling operator, splitting the resolvability limit into two topology-indexed
mechanisms, and adding the time-grain relativity of Memory are all internal to the paper and move no
Ladder-facing rung mapping. **Reversal noted honestly:** the time-grain Memory framing was one of three
items *held out* of canon in the v1.7 change run (R2); v1.8 folds it, because the star now gives it a
worked instance (E defined on the thermal clock, undefined on the nuclear one) rather than leaving it a
loose framing. The other two held items (scale-cap hierarchy, three-boundary correction) remain parked;
the scale-cap non-monotonicity was computed this session as a persister map but held out because the
galaxy placement is argued, not derived.

### R3 · Canon movement: v1.7 → v1.8 — reconciled 6 July 2026
- **What.** Three folded changes (E1–E3), plus two evidenced rebuttals, none weakening a surviving
  claim. (E1) The **star's resolvability model rebuilt from stellar structure** (Section 11, Figure
  R★): the v1.7 "confirms both halves" overclaim on an imposed equicorrelation caricature is retired
  and replaced by a coupling operator *derived* by linearizing the adiabatic pulsation equation on a
  Lane–Emden n=3 polytrope — a graded stiff-to-sloppy chain, not the degenerate two-level caricature —
  through which the star's parts blur *harder*, strengthening the claim. (E2) The **Section 6
  resolvability limit split** into an inferential (estimation) and interventional (isolation) mechanism
  and shown to be a **topology-indexed family** (new Figure T), the equicorrelation model being its
  degenerate mean-field member; §13's second limitation updated from an unquantified caveat to a
  characterized family. (E3) The **time-grain relativity of Memory** added to Section 5 (E is defined
  only for a stationary process — Crutchfield & Feldman 2003; complexity quoted at a declared temporal
  grain — Vazza 2020) and tied to the star's thermal-vs-nuclear stationarity in Section 11.
- **Why it holds together.** The three edits thread one spine already in the paper: §5 makes every
  magnitude observer-relative, §6's resolvability limit is the sharpest instance, §11's star is where
  it becomes computed. The edits cross-reference each other (verified in the coherence scan), so the
  movement is one argument, not three patches.
- **References.** Two added, both verified in full text and bibliographically confirmed against
  Crossref: Crutchfield & Feldman 2003 (Chaos 13, 25–54; doi:10.1063/1.1530990) and Vazza 2020 (MNRAS
  491, 5447–5463; doi:10.1093/mnras/stz3317). Total 27 bibliography entries.
- **Grade.** Settled components (Lane–Emden, LAWE, VIF, sloppiness spectrum, E-requires-stationarity,
  grain-relative complexity); the mappings onto the semantic mask and the space/time-grain twinning are
  this framework's synthesis. All computed quantities deposited.
- **Status.** Reconciled 6 July 2026. Designation updated; companion docs refreshed; no downstream
  propagation required.

---

## Change run — 5 July 2026

Folded the v1.6→v1.7 canon movement in one deliberate pass; the entry is moved to Reconciled as R2.
The canon designation (AOP_Canon_v1_0.md) now names **v1.7** as canonical and carries the refreshed
companion-document list (v1.7 changelog, star model result + figure). No cross-project handoff was
required: adding the star worked case, correcting the Section 8 "membrane-free" scope, and re-grading
the Integration floor are all internal to the paper and move no Ladder-facing rung mapping. The
gravitational-structure parking-lot note that seeded this work remains parked, with three items
deliberately held out of canon (scale-cap hierarchy claim, three-boundary / individuation correction,
time-grain Memory framing) for the reasons recorded in the v1.7 changelog.

### R2 · Canon movement: v1.6 → v1.7 — reconciled 5 July 2026
- **What.** Four changes plus a computed model, none weakening a surviving claim. (1) The **star**
  added as the fifth worked case (Section 11, abstract, Table 3 status row): high Drive, high
  Integration, gravitationally bound — the corner none of the four existing cases occupy. It carries
  the non-additivity synthesis (one settled property — gravitational non-additivity / negative
  specific heat — is the common root of gravity's anti-boundary character, the Integration floor, and
  the star's self-restoring drive), the flame/star restoring-force contrast, and the Section 6
  resolvability limit made physical. (2) A **closed-form resolvability model** (Figure R★): an n-shell
  equicorrelation model showing per-shell √VIF diverging as (1−ρ)^(−1/2) while aggregate 1/√λ_max
  falls — both halves of the §6 pairing, verified to machine precision; the paper's second genuinely
  computed figure. (3) **Section 8 "membrane-free" scope corrected** — the v1.6 text wrongly listed
  stars among membrane-free gravitationally-bound persisters; a star has a real photospheric EM screen,
  so "membrane-free" is re-scoped to galaxies (bound systems with no active radiative screen). (4) The
  **gravitational Integration floor re-graded** from implicit synthesis to settled, cited to Campa,
  Dauxois & Ruffo 2009, verified in full text this session. Reference count 24 → 25.
- **Where.** aop_v1_7.md (version header, abstract, §8, §11, Table 3, Data Accessibility, reference
  list + note). Companion: aop_v1_7_changelog.md; model: aop_star_resolvability_result.md +
  aop_star_resolvability.png; audit addition: aop_v1_4_reference_audit.md.
- **Why now.** A gravitational-structure parking-lot note (5 July) identified the Section 8
  membrane-free error as a must-fix, the non-additivity result as a genuine synthesis worth a worked
  case, and the star as the one case that demonstrates the Section 6 instrument going soft in the
  regime the framework most wants to describe. The star case was built as evidence (closed-form model)
  rather than assertion.
- **Downstream.** None into Ladder-facing claims. No cross-project handoff required.
- **Status.** Reconciled (5 July 2026).

---

## Change run — 3 July 2026

This run reconciled the deferred P1 pointer bump and folded in the v1.6 canon movement in one
deliberate pass. Both entries are moved to Reconciled below. The canon designation
(AOP_Canon_v1_0.md) now names **v1.6** as canonical and carries the refreshed companion-document list.
No cross-project handoff was required: the Table 3 fix, the reference audit, the carving argument, the
resolvability-residue framing, and the screenability compression are all internal to the paper and do
not move any Ladder-facing claim; the only downstream artifact (the domain-edge / photon / horizon
material) was already parked for the Ladder in v1.5 and is unchanged.

---

## Reconciled

### R1 · Canon movement: v1.5 → v1.6 — reconciled 3 July 2026
- **What.** The paper advanced from v1.5 to v1.6. Six changes, none a new claim: (1) Table 3's D→M
  basis line corrected — the all-biconditional chain `E=0 ⟺ i.i.d. ⟺ time-reversible ⟺ σ=0` was false
  and contradicted Figure DM; replaced with the single direction used, `E=0 ⟺ i.i.d. ⇒ (time-reversible
  ⇒) σ=0`, contrapositive `σ>0 ⇒ E>0`, converse fails. (2) A "why four axes, not one" argument added
  to Section 1 — the four-fold carving is now argued to beat the single-axis incumbents (Krakauer [6],
  Markov-blanket [11]) by not losing distinctions they must lose. (3) The four diagnostic cases
  (Section 11) promoted from illustration to the framework's primary evidence for the carving. (4) The
  resolvability residue (Section 6) owned as *interpretation* — the pairing is the stiff/sloppy fact
  of the sloppiness picture under AOP's no-ownership reading, not a phenomenon AOP found. (5) Section 8
  (screenability) compressed — the event-horizon set-piece that set up the deleted de Sitter reach was
  cut; the taxonomy, two-boundary hydrogen case, and Figure 4 retained. (6) The five v1.4 references
  audited against primary sources (three full-text: Rosas, Comolatti–Hoel, Boyle; two abstract-only,
  paywalled: Lenton, Bouchard — correcting v1.5's wrong "Lenton in full text"), and the open VIF
  citation finalized to Marquardt 1970. Reference count 23 → 24.
- **Where.** aop_v1_6.md (version header, Table 3, §1, §6, §8, §11, reference note + list).
  Companion: aop_v1_6_changelog.md; audit record: aop_v1_4_reference_audit.md.
- **Why now.** A referee-style follow-up to the v1.5 deflation identified the Table 3 contradiction as
  a must-fix and the missing carving argument as the highest-leverage addition once the predictive
  posture was gone. The reference audit closed the one place the canon overclaimed about itself.
- **Downstream.** None into Ladder-facing claims. No cross-project handoff required.
- **Status.** Reconciled (3 July 2026).

### P1 · Canonical version pointer: v1.4 → v1.5 → v1.6 — reconciled 3 July 2026
- **Original deferral (v1.4 → v1.5).** The v1.5 genre correction (predictive posture deflated,
  horizon material deferred to the Ladder, resolvability limit reframed as inherited multicollinearity,
  soft axes marked) advanced the paper past the v1.4 the designation named; the pointer bump was too
  small to warrant its own run and was logged here.
- **Reconciliation.** Folded through to v1.6 in this run. AOP_Canon_v1_0.md's "current canonical
  version" line now reads **v1.6** and states explicitly that the canonical version is a synthesis, not
  a forecast (the sentence P1 said the designation should gain). The companion-document list now
  includes the v1.5 and v1.6 changelogs, the v1.4 reference audit, and the Ladder parking-lot note.
- **Downstream.** As logged at deferral: none into the paper's claims; the removed material became the
  Ladder parking-lot note, which sits outside the AOP canon. No cross-project handoff beyond that note.
- **Status.** Reconciled (3 July 2026).

---

## Superseded pending text (retained for the record)

### P1 (original pending entry, v1.4 → v1.5)
- **What.** The paper advanced from v1.4 to v1.5. The canon designation still names v1.4 as the
  current canonical version, and its companion-document list does not yet include the v1.5 changelog.
- **Where.** AOP_Canon_v1_0.md — the "Current canonical version" line, and the companion-document
  list (add aop_v1_5_changelog.md).
- **Why deferred.** A one-line pointer update is too small to warrant its own change run. Logged here
  per your instruction, to fold into the next run.
- **Substance, so it is not lost.** v1.5 is not a *claim* change — it is a *genre correction*. The
  paper stopped posturing as a predictive theory and now owns itself as a Perspective. Specifically:
  the "concrete first prediction" language was deflated to "the shape a synthesis commits to, not a
  forecast"; the domain-edge material (the free-photon set-piece; the de Sitter / Gibbons–Hawking /
  Chandrasekaran horizon-holography reach) was removed from the paper and parked for the Ladder; the
  resolvability limit was reframed as *inherited* multicollinearity (a limitation), with the
  persistence-specific *dissociation* preserved as an organizing observation; the soft axes
  (Boundary, Integration) were marked in the figures. The sentence the designation should gain at
  reconciliation: the current canonical version is explicitly a synthesis, not a forecast.
- **Downstream.** None into the paper's claims. The removed material became Ladder parking-lot content
  (LAD_Notes_DomainEdge_Photon_Horizon_v1_0_20260703.md), which sits outside the AOP canon; the AOP →
  Ladder bridge memo is unaffected. No cross-project handoff required beyond the parking-lot note
  already written.
- **Status.** Superseded by the reconciled R1/P1 entries above.

---

*Running master. Append pending entries above; reconcile in deliberate change runs; never delete —
a reconciled entry is the record of what moved and when.*
