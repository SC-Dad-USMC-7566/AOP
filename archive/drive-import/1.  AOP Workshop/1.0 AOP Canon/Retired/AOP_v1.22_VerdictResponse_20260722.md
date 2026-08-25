# AOP v1.22 — Response to Ben's verdict (22 July 2026)

**Status: fold HELD**, per your instruction, until you/CP confirm the revised P1-2 wording, the §13
re-opening, and adjudicate the grep. These items **supersede** the corresponding items in the Decision
Package; say the word and I'll consolidate into a clean Package v2 so CP reviews one document.

---

## 1. P1 completeness — the grep (for CP to adjudicate)

Literal case-insensitive search for `fixed partition` / `fixed-partition` / `at a fixed` / `fixed cut`
across both masters. Proposed-master result: **5 sites covered by P1-1…P1-5, one missed (§9a → new P1-6
below), three benign correct-usages.**

**Benign hits — my adjudication (please confirm):**
- §4 "driving **at a fixed** reversible skeleton moves Cμ by ~1%" — about Drive, not Φ_MIP. Leave.
- §12 "whether Barrier, Flux, and Bank are fungible **at a fixed** persistence P" — the economics
  reframing. Leave.
- §13a "no single **fixed partition** scores a window straddling the relabel" — this is *correct*: a
  time-invariant partition genuinely cannot score a straddling window. It is the retraction's own R2
  text. Leave.

(The retraction *changeset* `…RETRACTION.md` §3/R3/R4 also uses "fixed partition" — a governance doc, not
the master; corrected there for consistency, non-load-bearing.)

---

## 2. Item 1 — the P1-2 scope self-contradiction, fixed (+ P1-1 tightened, + new P1-6)

You're right: P1-2 asserted cross-normalizer value-robustness while deferring the audit that would
establish it, and on the natural reading it's false (change the normalizer → change the objective → both
argmin and min value move). The defensible, more informative claim is **local near-degeneracy at the
relabel**, not global robustness. Rewritten accordingly.

**P1-2 · §12 Φ_MIP status-table row — REVISED**
NEW: "…narrows the “no individuation” refusal to “no ownership”; ordering rescaling-invariant.
Normalization enters at the level of *which* cut is minimal: because Φ_MIP is the value **after**
minimizing over cuts, changing the normalizer changes the objective and can move both the minimizing
partition **and** the minimum value — so the normalizer is part of the coordinate’s declaration whenever
Φ_MIP is reported (§4). What is stable is local: at a relabel crossing the two candidate cuts have
near-equal objective by construction, so the minimizing partition flips while the value barely moves —
near-degeneracy at the crossing, not robustness across the normalization family. Zero-calibration is
exact; the gate’s gradedness, irreducibility, and one-vs-many ordering claims are established only for the
declared convention actually tested and are **not** asserted to hold across other normalizers pending an
audit. Secure (zero-calibration) within static Gaussian models for a fixed candidate system at a fixed
grain; nested level-selection (a v1.20 closure **retracted in v1.22**) and the non-stationary/critical
extensions are frontier"

**P1-3 · Masthead clause — REVISED** (same conflation)
NEW: "records that Φ_MIP’s minimizing partition is normalizer-dependent — the normalizer is part of the
coordinate’s declaration — with only local near-degeneracy of the objective at a relabel crossing, not
robustness across normalizers;"

**P1-1 · §4 intro — TIGHTENED** (so it reads consistently with the near-degeneracy framing; the only
change from the package draft is the italicized clause)
NEW (fragment): "…the scalar minimum stays well defined and continuous through a relabel *along a coupling
ramp at a fixed convention* — the two candidate cuts are near-degenerate at the crossing, so the
minimizing cut is non-unique there while the value barely moves; and a change in that minimizing cut is a
least-disruptive-cut diagnostic, not by itself an individuation event. …" (remainder unchanged: normalizer
must be declared whenever Φ_MIP is reported; "fixed candidate system at a fixed grain under a declared MIP
normalization convention — not a ‘fixed partition’".)

**P1-6 · §9a — NEW EDIT (the site P1 missed)**
OLD: "…and Section 4 scopes Φ_MIP to static, Gaussian systems at a fixed partition, marking the
nested-level, non-stationary extension as frontier."
NEW: "…and Section 4 scopes Φ_MIP to static, Gaussian systems for a fixed candidate system at a fixed
grain under a declared MIP convention, marking the nested-level, non-stationary extension as frontier."
WHY: same fixed-partition mis-scope as P1-1/P1-4; caught by the completeness grep.

---

## 3. Item 2 — P2-5 now re-opens the discharged deliverable and names the structural reason

You're right on both. The OLD §13 text was *discharging* the v1.20 standing deliverable ("compute the
mask on a well-posed part-partition"); parking the salvage sends that deliverable back to **open**, and
the obstacle is structural (whether the mask's well-defined region and its informative region overlap at
all), not a scheduling delay.

**P2-5 · §13 — REVISED**
NEW: "…an interval rather than a point for each proxy sensitivity. That range is the framework's
*proposed* characteristic measurable — a declaration-sweep target, not a quantity a single computation
here renders. Figure MW establishes only that the edge-ablation intervention is well defined and
observer-relative on dynamical proxies (current, entropy production, relaxation rate); the sole
viability-grounded demonstration in this paper is the §11b finite-horizon competence check. **The standing
deliverable named in v1.20 — the mask computed on a well-posed part-partition — is therefore returned to
open.** The coupled-Gaussian two-module attempt is parked, not folded (see masthead): it is unresolved
whether the mask’s *well-defined* region (edges separately manipulable enough to bear a per-edge weight)
and its *informative* region (edges whose scrambling actually moves viability) overlap at all on a
strongly-integrated part-partition, and until that overlap is shown the per-edge part-partition mask is
not relied on here."

This kills "This has now been done" (the leak), returns the deliverable to open, and states the real
obstacle. If my read of the obstacle is wrong, tell me and I'll re-word.

---

## 4. Item 3 — provenance corrected

You did not author the critic pass; Aster did. The package wrongly labelled it "Aster / CP." Corrected:

- Provenance table row → **"Critic pass on §4 scope + MW regrade — Aster (outside critic)."**
- Appendix B header → **"Critic verdict summary — Aster (outside critic), 22 July 2026."**
- The pending row stays **"Independent check of the corrected change set — CP."** CP is a genuinely
  separate seat from both the critic (Aster) and the builder (Cowork); the independent check is not
  circular. Added a one-line note in the package to that effect.

---

## 5. Item 4 — fold sequence corrected (base vs live file)

The contradiction is fixed. The fold base is the **proposed** master; only the frozen v1.21 entry comes
from the live file.

**Fold step 2 — REVISED:** "Cowork folds byte-precise from the verified `…v1.22_PROPOSED_ASTER.md` (the
fold base): slice each OLD span from *that proposed master* — the OLD spans in this change set are
v1.22-only text and exist only in the proposed master, not in v1.21 — assert each replacement matches
exactly once, and diff to confirm only intended regions moved. The **only** content taken from the live
v1.21 master is the frozen v1.21 changelog entry, restored byte-exact for the append-only revert (P3-1)."

---

## 6. Your process finding — recorded

Three instances of the same defect — the v1.18 benchmark's forced Möbius inversion, the §13 embarrassment
condition being a theorem rather than a contingent claim, now Figure MW — is a process finding, not three
coincidences. Your proposed standing rule:

> **Any figure or benchmark claiming a result "could have come out otherwise" must name, before it runs,
> the specific parameter whose change would have flipped it.**

This is a governance/process rule (how confidence is earned), not a canon claim, so it belongs in the
project's working record, not the paper. Say the word and I'll add it to the project handoff/process
record as a standing pre-registration rule.

---

## 7. What I need before the fold

1. Confirm the revised **P1-2** wording (near-degeneracy, not cross-normalizer robustness).
2. Confirm the **§13 re-opening** (P2-5) — and my read of the obstacle (well-defined vs informative
   overlap).
3. Adjudicate the grep: approve **P1-6 (§9a)** and confirm the three benign hits.

On your go (and CP's independent check), I fold byte-precise from the proposed master, restore the frozen
v1.21 entry, and hand you `AOP_CANON_MASTER_v1.22.md` to place. The live v1.21 stays untouched until then.
