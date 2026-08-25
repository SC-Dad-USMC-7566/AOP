# AOP — Comprehensive Handoff for New Working Tab

**Compiled:** 17 July 2026 by Claude Science (session `dd5a0f7b`)
**Purpose:** Orient a fresh tab on the true current state of the AOP project, the decision that now governs the next round of work, and where every file lives. **Read this first, then read the v1.16 canon fresh.**

---

## 0. READ-THIS-FIRST: context-currency warning

This handoff was written at the end of a session that **began on stale context**. The session's rolling summary described the canon as **v1.9 / v1.10**; the actual current canon on Drive is **v1.16**, with a complete, mature submission package dated 15 July. Two documents this session produced early on — `aop_framing_audit_v19_honest.md` and `aop_phase1_closure.md` — audit the *pre-mask v1.9 text* and are **superseded and should not be used** as guidance for v1.16 work. They are left in the artifact store for provenance only and are **not** dropped into the deliverables folder.

**Action for the new tab:** do not trust any v1.9/v1.10 framing from summaries. Open `aop_canon_v1_16.md` and the `Submission Package v1.16` folder directly and work from those.

---

## 1. Where the project actually stands (v1.16)

- **Canon:** `aop_canon_v1_16.md` (~22.8k words, ~160 KB) — the complete internal reference. Not for submission; the source of truth.
- **Submission package (current, 15 Jul):** a full derived Royal Society *Interface Focus* Perspective, in Drive at
  `Canon Development / Submission Package v1.16 (current 15 Jul)/`. It contains:
  - `aop_main.md` (~5.3–5.5k words, 10 sections, 6 main figures — under the 8k cap by design)
  - `aop_SI.md` (~5.0–5.1k words — five worked cases, diachronic individuation §4a, gate ledger, full status table, SI figures)
  - `aop_submission_README.md`, `aop_manuscript_blueprint.md`, `aop_figure_manifest.md`
  - `aop_reference_punchlist.md` (authoritative reference-verification record) + `aop_reference_acquisition.md`
  - `aop_repro_package.tar.gz` (engine + 6 gate modules + 9 figure scripts + 7 data files, smoke-tested)
  - `aop_data_availability.md`, `aop_gate_stakes_record.md` + `aop_gate_stakes.py`
  - `figures/` — 12 PNGs at 300 dpi (Fig 1–6 main, Fig S1–S7 SI)
  - Numerous per-gate `prereg / gate.py / verdict` triples (budget, substitutability, realsystem, worked-case, current-lifetime, integration-axis, integration-factoring)

- **Target venue:** Royal Society *Interface Focus*, Perspective format (~8,000-word cap on main text).

- **Package self-check status (per existing handoff manifest, 16 Jul):** main ≤8k words; all 12 figure embeds resolve; main Figs 1–6 first-referenced in order; SI Figs present; **zero Ladder/downstream/Time-Machine tokens** (paper is standalone); every citation resolves to a canon reference (no orphans).

---

## 2. The decision that now governs the next round — the OAI review

An **external reviewer (OpenAI / ChatGPT, "OAI")** has read canon v1.16 and issued a formal remediation package. It lives in Drive at `OAI deliverables/`:

| File | Status |
|---|---|
| `REV_OAI_AOP_Remediation_MasterPlan_v1_0_20260717` | Complete (~15 KB) — the 7-phase plan |
| `REV_OAI_AOP_Operational_Definitions_v1_0_20260717` | Complete (~14 KB) — target-vs-proxy panel spec |
| `REV_OAI_AOP_Semantic_Intervention_Protocol_v1_0_20260717` | Complete (~18 KB) — coalition-aware mask protocol |
| `REV_OAI_AOP_Benchmark_Model_Specification_v1_0_20260717` | **EMPTY placeholder (1 KB Google Doc, no body)** — not yet written |
| *(revision decision matrix + Claude handoff)* | **This document is the Claude side of OAI deliverable #5.** |

### OAI's executive judgment (paraphrased, verify against the source doc)
The problems are solvable, **but not by another prose-polish pass**. OAI wants a controlled **re-baselining** that separates *conceptual targets → operational proxies → intervention rules → empirical claims* before the submission manuscript is rebuilt. Keep the strongest contribution (the two-layer dependency audit), but **narrow the scientific posture** from "a four-scalar architecture / master geometry of persistence" to "a declared **measurement panel** + a viability-relative causal analysis."

### OAI's final recommendation (the fork in the road)
> Do **not** ask Claude to patch v1.16 paragraph by paragraph. First **approve or reject** the architecture decisions in the OAI specifications. Then Claude can rebuild a derived manuscript against a **frozen source**, with every change logged and no silent migration of terms.

**This requires Ben's decision before the next tab does substantive rewriting.** The two paths are:
1. **Accept the OAI re-baselining** (narrow posture to "atlas/audit/measurement panel", implement the P0 corrections, build a benchmark, then rebuild the manuscript). This is a larger, multi-phase program.
2. **Defend the current v1.16 posture** and treat the OAI plan as a menu of optional hardening — adopt the P0 corrections that are genuinely defects, contest the ones that are philosophical disagreements, and keep the existing submission on track.

A hybrid is likely correct: several P0 items are real (see §3); some are posture disagreements AOP has already argued through and graded honestly.

---

## 3. OAI's P0 "stop-ship" items (the concrete claims to adjudicate)

From the master plan's priority order. For each, the new tab should decide **defect vs. disagreement** against the actual v1.16 text (not from memory):

1. **Binding → rest frame / clock / proper time / present tense.** OAI: remove; replace the "domain wall" with an operational applicability criterion. *(In v1.9 this was already graded "synthesis, not a theorem" in the status table — check how v1.16 states it.)*
2. **"Drive and Memory are choice-free."** OAI: restate as "require no *additional* spatial/component cut once a process representation, time grain, and reversal convention are fixed."
3. **Proxy-label mismatches.** OAI: stop equating raw MI = boundary strength; entropy production = free-energy throughput; excess entropy = stored memory; total correlation = irreducible integration. Label each as the proxy it is (dependence / dissipation / predictive-dependence / multivariate interdependence).
4. **Viability ownership.** OAI: replace "the system's *own* viability function" with "an analyst-declared, dynamically-constrained *family* of viability functionals."
5. **Evidential vs. dependency conflation.** OAI: a theorem, a definition, a constructed counterexample, and a random-ensemble correlation are not points on one evidential scale — split the two status dimensions in Table 3 / the ledger.
6. **Reproducibility/version reconciliation.** Reconcile canon pointer, manuscript title/version, blueprint, changelog, and Data Accessibility to one frozen v1.16 baseline.
7. **"Energy is the hub."** OAI: reframe as an organizing hypothesis unless the graph among the four targets actually supports hub status; reliability is an external consequence, not automatically a fifth axis.
8. **Gravity / screenability / light-cone.** OAI: quarantine from the scientific core until reviewed as a separate boundary-taxonomy.
9. **Worked cases (crystal/flame/spore/atom/star).** OAI: relabel as **diagnostic archetypes** unless all declarations and quantities are actually computed.

**P1 (publication-strength):** operational panels; finite-horizon viability `V(θ,τ|x_t)`; admissible interventions with declared invariants; **coalition-aware semantic hypergraph** (minimal failure cut-sets, viability-preserving sets, redundant alternatives, synergistic coalitions) instead of forced per-edge weights; **one complete benchmark system** (a minimal leaky autocatalytic compartment / dissipative controller) with pre-registered two-exit tests.

**P2 (research program):** comparative adjudication vs. a named one-axis rival; nested individuation (F2); living threshold; collective agency; gravity; cosmology; Ladder propagation.

---

## 4. What is genuinely ready vs. open (from the v1.16 package itself)

**Ready to red-team now:** the full v1.16 package — standalone, citation-clean, gate discipline hardened, figures consistent.

**Reference-verification debt** (per `aop_reference_punchlist.md` / handoff manifest — reconcile the exact counts against the punch-list, the two docs differ slightly):
- ~25–31 verified-in-body; ~14 abstract-verified.
- **5 record-only** — bibliographic metadata only, **flagged NOT acceptable for submission** under the charter standard: Watanabe 1960, Marquardt 1970, Conant & Ashby 1970, Nicholson & Dupré 2018, Muller 1964. Each is non-load-bearing background or has a softening path in the punch-list.
- **2 needs-user-PDF** — Ashby 1960, Parfit 1984 (both print-only, both non-load-bearing). Not blockers.

**The gate-stakes result** (the package's strongest content defense): answers the charge that gates are "consistency checks, not tests that could fail." On a model built *without* the driven ring's reversal symmetry, stored asymmetry Ξ is a live movable axis (structure alone moves |Ξ| ~2 bits at zero dissipation), yet cranking drive ×64 at fixed structure leaves |Ξ| flat — the GO exit was reachable and not triggered, so the NULL is informative, not tautological. Honest boundary: reachability argued within the toy-model class, not against nature.

**The one open scientific problem (honestly frontier):** **F2 — the nested-level, non-stationary extension of the integration axis (Φ_MIP).** Φ_MIP is closed only in the static Gaussian setting; the higher-individual lineage route, the collective living-threshold, and the critical/Ising regime all wait on extending it to nested levels and non-stationary partitions. Stated as frontier throughout; does not weaken the §4 forced edges. This is the intended attack surface — and it maps onto OAI's P1 coalition-aware requirement.

---

## 5. Recommended next actions for the new tab

1. **Refresh context.** Read `aop_canon_v1_16.md` and the `Submission Package v1.16` README + blueprint fresh. Ignore any v1.9/v1.10 framing in session summaries.
2. **Get Ben's decision on the fork (§2).** Accept OAI re-baselining, defend current posture, or hybrid. Nothing large should be rewritten before this.
3. **Freeze the source baseline (OAI Phase 0).** Reconcile canon pointer / manuscript version / blueprint / changelog / Data Accessibility to one frozen v1.16 file. Build an **issue registry** mapping each OAI criticism → source location, severity, disposition, evidence requirement, verification test. This is low-risk and valuable under either fork path.
4. **Adjudicate the P0 items (§3)** against the actual v1.16 text — mark each defect vs. disagreement, with a one-line rationale. Produce this as the **revision decision matrix** (OAI deliverable #5, Claude side).
5. **If re-baselining is chosen:** the highest-value scientific unit is the **coalition-aware semantic hypergraph + one complete benchmark** (OAI Phases 3–4). This directly addresses F2 and the "gates can't fail" charge. The empty `Benchmark_Model_Specification` doc needs to be written first (or Claude writes the benchmark spec).
6. **Reference debt:** decide whether to soften/relocate the 5 record-only citations or acquire library PDFs (needs Ben for the 2 print-only books).

---

## 6. Drive housekeeping note

The connector can **add** files but **cannot delete** them. Older duplicate copies from earlier sessions accumulate in the parent folders (see the `Retired/` folder and the many `(1)/(2)/(3)` suffixed duplicates). A clean-up pass requires Ben to delete in the Drive UI. The current authoritative package is the single `Submission Package v1.16 (current 15 Jul)` folder; treat everything in `Retired/` as history.

---

## 7. File map (as of this handoff)

**Source folder** `AOP` (`1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J`):
- `Claude Science deliverables/` ← **this handoff + Drive inventory dropped here**
- `OAI deliverables/` ← the 4 OAI review docs (benchmark spec empty)
- `Canon Development/` ← `Submission Package v1.16 (current 15 Jul)/`, plus loose `aop_main/SI/blueprint` copies, `AOP_Canon_ChangeLog`, `aop_canon_v1_16.md`, `figure_LT_threshold.py`, and `Retired/`
- Loose at top level: `AOP_Canon_ChangeLog (5).md`, `AOP_Canon_v1_0 (6).md`, `aop_canon_v1_16.md`, `figure_LT_threshold.py`

A full machine-readable inventory is in the companion file **`aop_drive_inventory_20260717.md`** dropped alongside this handoff.

---

## 8. Provenance of this handoff

- Written from: the v1.16 submission package (`aop_handoff_manifest.md`, `aop_submission_README.md`), the OAI remediation master plan + op-defs + semantic-intervention specs (all read in full or by executive summary), and a full folder-tree crawl of the source Drive folder.
- **Not** written from: this session's own early v1.9-based framing audit / phase-1 closure (superseded — see §0).
- Numeric counts (word counts, reference tallies) are quoted from the existing manifest/README, which disagree slightly between themselves; the new tab should treat `aop_reference_punchlist.md` as authoritative for reference status and re-derive word counts from the actual files.
