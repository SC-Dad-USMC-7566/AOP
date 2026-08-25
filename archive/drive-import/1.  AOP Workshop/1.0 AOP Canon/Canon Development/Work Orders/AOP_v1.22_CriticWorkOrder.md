# Critic work-order — two questions to clear before folding AOP v1.22

**For:** the outside critic (OAI/Aster seat). **From:** the chat/judgment seat (Ben + Cowork).
**Standing rule:** try to *break* each claim. Default to "under-scoped / not established" if uncertain.
Nothing is folded until these two clear. The live master is `AOP_CANON_MASTER_v1.21.md`; the
proposed master is `AOP_CANON_MASTER_v1.22_PROPOSED_ASTER.md`; the retraction changeset is
`AOP_Canon_ChangeSet_v1.21_to_v1.22_RETRACTION.md`.

---

## Question 1 — Is the level-selection retraction UNDER-SCOPED at §4?

The v1.22 retraction withdraws the §13a nested-hierarchy level-selection closure and confines the
argmin-relabel instability (the minimum-information-partition jumping from the module boundary to a
single-node cut as coupling rises) to *level selection*. It explicitly **ring-fences §4**, stating
the Φ_MIP individuation axis is untouched because it is "one-vs-many at a **fixed** partition."

The tension: the deposited individuation gate (§4, Data Accessibility) computes Φ_MIP across the
**exhaustively-searched *minimum* information partition** of Σ = (I + gL)⁻¹ — i.e. at *the* argmin
over cuts, not at a declared fixed cut. If §4's coordinate is in practice read at the MIP, the same
relabel instability the retraction pins to level-selection reaches §4 itself.

**Attack:**
1. Is §4's Φ_MIP coordinate well-defined *independently* of which partition is minimal, or does it
   inherit the argmin instability the moment coupling crosses a relabel point?
2. Does the retraction's own general lesson — "a MIP relabel proves the argmin changed, not that
   individuality changed" — apply to §4's own one-vs-many reading, not only to level selection?
3. If yes: does the retraction need to extend an edit into §4 (e.g. scope §4 to a *declared* fixed
   partition, or add the normalization-declaration caveat there too), or is the existing §4
   normalization-robustness scoping (edit R3) already sufficient?

**Two exits:** (a) §4 is genuinely fixed-partition and the retraction is correctly scoped; or
(b) §4 inherits the instability and the retraction must grow to cover it. State which, with the
reason.

---

## Question 2 — Is the Figure MW regrade correct, and does it leave dangling references?

v1.22 regrades **Figure MW** from "the framework's characteristic measurable / three present-tense
viability functionals" to a **proxy-ablation diagnostic** — arguing its three functionals (steady-state
current, entropy production, relaxation rate) are *dynamical proxies*, none of which is the paper's
primitive (mean first-passage *lifetime*), so MW shows edge-sensitivity is well-defined but does **not**
establish that the affected edges are causally necessary for continued existence. It elevates **§11b**
(finite-horizon survival probability on a 36-state CTMC, with a built-in answer key) as the real
viability-grounded demonstration.

**Attack:**
1. Is the demotion correct — are current / entropy-production / relaxation-rate genuinely *not*
   lifetime-grounded, so MW cannot carry a causal-necessity reading?
2. Does §11b actually earn the elevation? Its answer key is manufactured by AOP (the gate topology and
   rates encode the designed inert/load-bearing/redundant/synergistic structure), so it is a
   *competence check*, not external validation. Is the paper now over-crediting §11b?
3. **Dangling-reference check:** the abstract and §13 still describe "the range a weight sweeps … the
   framework's **characteristic measurable**," language that originally pointed at the Figure MW
   computation. After the regrade, does §13 (and any other passage) still call the MW range the
   characteristic measurable while §3/§12 now demote MW to a proxy diagnostic? List every surviving
   passage that is now inconsistent with the regrade.

**Two exits:** (a) the regrade is correct and self-consistent (list any cleanup edits still needed);
or (b) it over-demotes MW / over-credits §11b, or leaves the paper internally inconsistent — say where.

---

## Context the critic can assume already verified (do not redo)

- R1–R8 retraction edits: numbers independently reproduced by a third seat (MIP relabel b = 0.330221
  at N=8, 0.420601 at N=6; module/whole equality 0.3002/0.2163/0.6296 for marginal/conditional/isolated).
- Ptaszyński & Esposito (arXiv:2410.13375 = PRL 135, 057401 (2025)) and Liu–Yuan–Zhang (*Entropy*
  26(8):618, 2024) and Marshall et al. (niag013) citations line-checked against primary.
- Coherence edits 1–4 (Drive sign, commensurability, energy-hub as SYNTHESIS, non-energy triangle
  two-grade split) judged internal-consistency fixes by the chat seat; spot-check only.
- The append-only violation on the v1.21 changelog entry will be reverted regardless of the critic's answer.

Return a verdict on Q1 and Q2 with reasons. Ben decides the fold after.
