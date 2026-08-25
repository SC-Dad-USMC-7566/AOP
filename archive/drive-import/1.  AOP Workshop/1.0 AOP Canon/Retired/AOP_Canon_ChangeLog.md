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

### P1 · Canonical version pointer: v1.4 → v1.5
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
- **Status.** Pending.

---

## Reconciled

*(none yet — the first change run will move P1 here, dated)*

---

*Running master. Append pending entries above; reconcile in deliberate change runs; never delete —
a reconciled entry is the record of what moved and when.*
