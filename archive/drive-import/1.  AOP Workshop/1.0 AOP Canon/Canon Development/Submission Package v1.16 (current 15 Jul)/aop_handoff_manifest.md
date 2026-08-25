# AOP Submission Package — Red-Team Handoff Manifest

_Compiled 2026-07-16. Target venue: Royal Society *Interface Focus* (Perspective). This
manifest indexes the complete package and states, honestly, what is solid and what is
still open. Everything below is standalone: no reference to any downstream project._

## The deliverables

| # | Document | What it is |
|---|---|---|
| 1 | **aop_main.md** (5,530 w) | Submission main text — 10 sections, 6 figures. Under the 8k cap by design. |
| 2 | **aop_SI.md** (5,110 w) | Supplementary Information — 5 worked cases, diachronic individuation, gate ledger, full status table, 7 SI figures. |
| 3 | **aop_submission_README.md** | Package index + known soft-points list. |
| 4 | **aop_manuscript_blueprint.md** | Production record (contribution statement, arc, split/renumber maps). |
| 5 | **aop_figure_manifest.md** | 12-figure manifest, data-fidelity checked. |
| 6 | **aop_reference_punchlist.md** | Per-entry verification record — the authoritative reference-status document. |
| 7 | **aop_reference_acquisition.md** | Fetch list for still-open sources. |
| 8 | **aop_repro_package.tar.gz** | Engine + 6 gate modules + figure scripts + data. |
| 9 | **aop_data_availability.md** | Data-availability statement. |
| 10 | **aop_gate_stakes_record.md** + **aop_gate_stakes.py** | The gate-stakes analysis (below) and its reproducible script. |
| 11 | **aop_canon_v1_16.md** | Backing canon — the complete internal reference the main text is condensed from. |
| — | **figures/** | 12 PNGs at 300 dpi (Fig 1–6 main, Fig S1–S7 SI). |

## Integrity check (all pass)

- Main text ≤ 8,000 words (5,530); SI substantial (5,110).
- All 12 figure embeds resolve; main Figs 1–6 present and first-referenced in order; SI Figs S1–S7 all present.
- Zero Ladder / downstream / Time-Machine tokens anywhere — the paper is standalone.
- Every author-year citation in main + SI resolves to a canon reference entry (no orphans).
- Gate-stakes result folded into §7.4 and §10, with Fig S7 captioned in the SI.

## Reference verification status

- **31 verified-in-body** — passage relied on read from the primary-source body.
- **14 abstract-verified** — abstract-level claims, only abstract retrievable.
- **5 record-only** — bibliographic metadata only; **flagged NOT acceptable for submission**
  under the charter standard (Watanabe 1960, Marquardt 1970, Conant & Ashby 1970,
  Nicholson & Dupré 2018, Muller 1964). Each is either non-load-bearing background or has a
  softening path noted in the punch-list.
- **2 needs-user-PDF** — Ashby 1960 and Parfit 1984, both print-only and **both
  non-load-bearing**: the internal-model idea rests on Francis & Wonham (verified); Parfit is
  a conceptual reference needing no body check. Not blockers.

## The gate-stakes result (the paper's strongest defense)

The red-team's sharpest content charge is that §10 concedes the gates are "consistency
checks, not tests that could fail." The gate-stakes analysis answers this for the
E-vs-Cμ memory-irreversibility screen: on a model built *without* the driven ring's
reversal symmetry, stored asymmetry Ξ is a **live, movable axis** (structure alone moves
|Ξ| across ~2 bits at zero dissipation), yet cranking the drive ×64 at fixed structure
leaves |Ξ| flat. **The GO exit was reachable and not triggered** — the NULL is
informative, not tautological. Corroborated by this gate's retracted-GO history. Honest
boundary: reachability is argued within the toy model class, not against nature — a
pre-registered test with a reachable alternative outcome on a minimal model, which is
stronger than "consistency check" and weaker than "empirical test."

## The one open scientific problem (honestly frontier)

**F2 — nested-level, non-stationary extension of the integration axis.** The
individuation axis (Φ_MIP) is closed only in the static Gaussian setting; the
higher-individual route for lineages, the collective living-threshold, and the
critical/Ising regime all wait on extending it to nested levels and non-stationary
partitions. Stated as frontier throughout; does not weaken the §4 forced edges or the
present-tense claims. This is the intended attack surface.

## What is genuinely ready, and what waits on the user

- **Ready to red-team now:** the full package above — standalone, citation-clean,
  gate discipline hardened, figures consistent.
- **Waits on user:** (a) two print-only books (Ashby, Parfit) — non-blocking; (b) if
  desired, upgrading the 5 record-only sources with library PDFs; (c) Drive housekeeping —
  the current package lives in one clean folder, but older duplicate copies from earlier
  sessions remain in the parent folders (the connector can add files but not delete them).
