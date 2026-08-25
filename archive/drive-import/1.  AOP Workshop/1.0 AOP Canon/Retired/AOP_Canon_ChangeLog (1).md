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

*(none — reconciled in the 3 July 2026 change run below)*

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
