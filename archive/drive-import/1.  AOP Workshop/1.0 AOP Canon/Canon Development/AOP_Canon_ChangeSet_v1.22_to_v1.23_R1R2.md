# AOP Canon — Change Set: adopt v1.22 + two pre-red-team repairs (→ v1.23)

**Prepared 23 July 2026 (chat seat / prime).** Independent adjudication of `AOP_CANON_MASTER_v1.22_PROPOSED_ASTER.md`
against live `v1.21`. **Verdict: ADOPT v1.22**, applying the two repairs below. Both are honesty-improving,
neither is new science, no claim is retracted or strengthened. Applying these against the v1.22 body produces the
adopted, red-team-ready canon (numbered here **v1.23**; fold as v1.22-final if you prefer).

Prose is in clean form; whoever applies maps to the master's markdown escaping. Two edits only.

---

## What was independently verified this session (not read over — re-run / cross-checked)
- **Retraction is correct.** Re-ran `phaseD1_levelselect.py`: it computes only the *whole-system* MIP and where it
  relabels as inter-module coupling rises; it never coarse-grains and never compares Φ across grains. The v1.20/1.21
  "level-selection closure" was narration the code does not support. F2 is open in both halves. ✓
- **Retraction propagated cleanly** across §4, §9a, §13, §13a, Table 3, Data Accessibility. The `Zhang 2025` /
  `npj Complexity` / `closing the level-selection` strings survive **only** inside the historical v1.20 changelog
  entry (correct to preserve), not as live claims. ✓
- **All six v1.22 coherence repairs landed in the live body**, not just the changelog. ✓
- **Both freshly-touched citations verified against primary this session:**
  - Ptaszyński & Esposito, *Phys. Rev. Lett.* **135**, 057401 (2025); arXiv:2410.13375 — abstract matches the D→I
    feasibility wording and the permutation-invariant scoping exactly. Load-bearing; solid. ✓
  - Liu, Yuan & Zhang, *Entropy* **26**(8):618 (2024); arXiv:2405.09207 — authors/venue/year correct; "optimal linear
    coarse-graining determined by principal eigenvalues/eigenvectors, non-unique" matches the canon's use. The old
    "Zhang 2025 / npj Complexity" cite was genuinely wrong; v1.22's correction is right. Context-only. ✓
- **Falsifiability posture is already consistent** everywhere except §13: lines carrying "not a falsifiable test"
  (Figures MW, LT, R★) agree with R2; the §13 embarrassment condition is the sole outlier. Removing it makes the
  document internally consistent, not less so.

---

## EDIT R1 · §11b subsection header (self-contradiction with its own conclusion)
**OLD:** "**The result that could have come out otherwise.**"
**NEW:** "**The dissociation a one-axis reading inverts.**"
**WHY:** The header dates from the pre-v1.19 framing. The paragraph below it, and the v1.19 re-grade, both state the
result is *forced by the gate topology and rate assignments* — "competence check, not a discovery." The old header
claims contingency the section explicitly denies two paragraphs down. The new header states what the benchmark shows
(a designed dissociation the four-target method recovers and a strength/correlation reading inverts) without the
false could-fail claim. **[DEFECT-fix; no grade change.]**

---

## EDIT R2 · §13, the "embarrassment condition" (a forced result presented as a falsifier)
Replace the block beginning "This does not leave the framework wholly unfalsifiable…" and ending
"…and the account is not idle against it." (the sentence before it — "…the aggregate mode stays *sharp*, not exactly
invariant." — and the sentence after — "The energy hub is coherent and defensible;…" — are unchanged).

**OLD (verbatim, replace in full):**
"This does not leave the framework wholly unfalsifiable, and it is worth saying plainly what would embarrass it. The resolvability claim commits to a specific coupling between two things that can be measured independently: how strongly coupled a system is and how wide its semantic weights sweep as the partition is varied. The test has to be stated carefully, because this same paper insists (Section 6, Figure TF, and the star) that width is set by coupling *topology*, not by a scalar amount of integration — a weakly integrated chain can out-blur a strongly integrated mean-field system, and that is the topology family behaving as predicted, not a failure. So the embarrassment condition is not \"width tracks a scalar integration score across all systems\"; that would be confounded by the very refinement the paper is proud of. It is the narrower, sharper claim: *within a fixed coupling topology*, increasing the global coupling must monotonically widen the weight sweep, and *at matched mean coupling* the topology with the more graded spectrum (the chain) must show the wider inferential sweep than the degenerate one (mean-field). Both are computed here (Figure TF; the star vs. its equicorrelation caricature) and either could have come out otherwise: a topology whose sweep did not widen with coupling, or a graded spectrum that did not out-blur the degenerate one at matched coupling, would falsify the resolvability limit. That is a weak test, internal to the synthesis rather than adjudicating it against a named rival, but it is a test the topology result sharpens rather than undercuts, and the account is not idle against it."

**NEW (verbatim):**
"It is worth being exact about the kind of exposure the framework has — a discipline the retracted §13a closure underscores. The resolvability limit is not a falsifiable prediction, and should not be presented as one. It asserts a relation between how strongly coupled a system is and how widely its semantic weights sweep as the partition is varied — but within the model class the framework uses, that relation is structural, not contingent: per-component attribution variance is governed by the smallest eigenvalue of the precision, so within a fixed topology raising the coupling widens the inferential sweep, and at matched mean coupling a more graded spectrum out-blurs a degenerate one, both by construction rather than by any fact a measurement could contradict. The computed instances (Figure TF; the star versus its equicorrelation caricature) are therefore demonstrations of self-consistency — the account says integrated systems blur, and its own worked systems blur in the predicted way — not tests that could have come out otherwise. This is the posture the rest of the paper already takes toward its computations (Figures MW, LT, R★); §13 is brought into line with it here.

Where the framework is genuinely exposed is its carving, and that exposure is taxonomic rather than predictive. The claim that these four axes are the right ones can be shown wrong in the ordinary way a taxonomy can: by a persister whose four-axis profile mis-describes it — one that demands a fifth axis the four cannot express, or that forces two the paper holds distinct to collapse into one that always co-moves. Completeness and minimality are held open (Section 2) precisely because this is the live question, and it is the honest form of \"this could be wrong.\"

None of this makes the paper a rival theory settled by a crucial experiment, and it does not present itself as one. It is a synthesis of established results, and a synthesis earns adoption on different terms: by unifying quantities the source literatures pose in isolation, and by refusing to lose the distinctions a single-axis account must discard — the flame's maintained boundary at negligible memory, the spore's deep structure at near-zero drive (Section 11). That is the standard the paper asks to be read against, and the one it is built to meet."

**WHY:** Computed check this session: for the exact comparison the passage stakes its falsifier on, both clauses are
forced by the model's positive-definite structure — max per-component VIF is monotone in global coupling for both
topologies over the full tested range, and the chain out-blurs mean-field at every matched mean-correlation, never
flipping (max-VIF is governed by λ_min of the precision, which a more graded spectrum drives lower at matched
coupling). "Either could have come out otherwise / would falsify" therefore claims a testability the linear algebra
does not supply. The replacement states the resolvability limit as the structural self-consistency property it is,
relocates the framework's genuine exposure to its carving (taxonomic, per §2), and names the synthesis standard the
paper asks to be judged against — consistent with the abstract ("a synthesis of established results, not new
physics") and with the not-a-falsifiable-test framing the rest of the paper already uses. **[honesty-fix; no claim
retracted, none strengthened.]**

---

## Proposed changelog entry (append to master)
> ### Version 1.23 (23 July 2026) — adopt v1.22 + two pre-red-team honesty repairs (independent adjudication, prime).
> Adopts the v1.22 corrective consolidation after an independent check (retraction re-verified by re-running
> `phaseD1`; six coherence repairs confirmed propagated to the live body; Ptaszyński–Esposito 2025 and
> Liu–Yuan–Zhang 2024 verified against primary). Two residual defects predating v1.22 are repaired, no new science,
> no claim retracted or strengthened: **(R1)** the §11b header "The result that could have come out otherwise" —
> which contradicted the section's own "forced by the construction / competence check, not a discovery" — is renamed
> "The dissociation a one-axis reading inverts." **(R2)** the §13 "embarrassment condition" is corrected: a computed
> check showed both clauses of the stated falsifier are forced by the model's positive-definite structure (max-VIF
> monotone in coupling; chain out-blurs mean-field at matched coupling, never flipping), so the resolvability limit
> is not a falsifiable prediction. §13 now states it as a structural self-consistency property, relocates the
> framework's genuine exposure to its carving (taxonomic; completeness/minimality held open, §2), and names the
> synthesis standard the paper asks to be judged against. This brings §13 into line with the not-a-falsifiable-test
> posture the rest of the paper (Figures MW, LT, R★) already holds. **Status: adopted; red-team-ready.**

## Carried before-final debt (submission-gating, NOT red-team blockers)
- Full-text reads still `~` (nothing load-bearing rests on these alone): Maes 2020, Schnakenberg 1976,
  Bouchet–Reygner 2016, Oono–Paniconi 1998.
- ⚠ pagination/text/DOI confirms: DiFrisco 2018 (genidentity terms/pages), Joyce 1994 (foreword text), Ashby 1960
  (pagination), Hoel 2016 (venue/DOI), Bialek–Nemenman–Tishby 2001 (DOI), Pearl 1988 (page/edition),
  Hatano–Sasa 2001 / Speck–Seifert 2005 (DOIs).

## Optional cosmetic (not applied here)
- The v1.12 *changelog* entry still states Φ_MIP is "robust across minimum-partition normalizations" flatly — the
  claim v1.22 scopes. Historical, so not wrong; one annotating clause would spare a careful reader the apparent
  contradiction.
