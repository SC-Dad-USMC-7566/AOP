# Warm handoff — for Aster (OAI review)

**From:** Claude Science (builder lane), AOP
**Date:** 21 July 2026
**Where everything lives:** Google Drive → **Canon Development** (folder id `1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`)

Hi Aster — two related builder deliverables are ready for your review, both from today. Both are **proposals**, not canon: Prime verifies and Ben decides. Here's what each one is and where to find it.

---

## 1. Moving-MIP build (the framework's principal open problem)

**What it is.** Canon v1.20 §13a names the time-extended (moving) Φ_MIP as AOP's principal open FRONTIER item: how to score a minimum-information-partition over a developmental window when the covariance moves through a transition and the MIP — a discrete argmin — relabels partway through, so no single fixed partition scores a straddling window. The build's finding is the charter's strong-outcome signature: **the "new" object is a solved problem, independently, in three peer-reviewed fields** — the Froyland–Koltai inflated dynamic Laplacian (CPAM 2023, read in full), the multilayer supra-Laplacian (Gómez PRL 2013 / De Domenico PRX 2013), and deterministic annealing / the information bottleneck (Rose 1998; Tishby et al. 1999; Parker & Dimitrov 2022). All three say: don't force one hard partition through the transition — use a soft, time-coherent partition family that pays a bounded relabeling cost. Two equivalent constructions are built and verified closed-form on the canon's Phase-D Gaussian: a discrete moving-MIP (exact, dynamic programming) and a spectral inflated-supra-Laplacian surrogate.

**Files (all current versions):**
- `AOP_MovingMIP_Build_proposal_20260721.md` — id `11R62Um47k070-pifCFDg3CMO3cVjGamf` (17,923 B) — the proposal.
- `phaseE_movingMIP.py` — id `1uXvn4IQKRGXetzOJIGZE5EG7jr834jM0` (13,320 B) — runnable, self-contained, NumPy-only; reproduces every number and prints the frontier residue.
- `phaseE_movingMIP_fig.png` — id `1JAXSneQkBFUQUXS-aPemZS9TgOYk8t4y` (218,874 B) — three panels: obstacle, discrete resolution, spectral lifetime.

**Where it would touch canon if it holds (Prime's call, not mine):** FRONTIER → SYNTHESIS in §4, §9a, §13a, plus a Ladder-bridge propagation. I did **not** edit canon.

**Known frontier residue (stated in the proposal, §8):** single-transition scope only; the coherence weight λ / diffusion `a` are set by heuristic, not yet derived from the §5 adiabaticity bound; Gaussian model class only.

## 2. Line-check of Ptaszyński & Esposito (gates a canon regrade)

**What it is.** A citation line-check on arXiv:2410.13375 = *Dissipation Enables Robust Extensive Scaling of Multipartite Correlations*, now published as **Phys. Rev. Lett. 135, 057401 (2025)** (Ptaszyński & Esposito). Full text was read from the primary source. The verdict gates the canon gap-register **row 8** regrade. Headline: the impossibility-of-robust-extensive-correlation-at-equilibrium result is real and citable, **but it is scoped to permutation-invariant (all-to-all / mean-field) systems** — the authors themselves flag generalization to lattices / disordered systems as open. Anything broader than that scope overstates the source, and "robust" must keep its technical meaning (structural stability under small rate perturbations).

**File:**
- `AOP_LineCheck_PtaszynskiEsposito_20260721.md` — id `13v_CB79dF6y-930Bg8esCKTOB9C-ym3_` (4,720 B).

---

## One cleanup caveat — please read before opening files

The Google Drive connector I use can **add** files but cannot **update or delete** them, so when I corrected an author-attribution error (an earlier draft misattributed the *Entropy* 2022 bifurcation paper to "Gedeon et al."; it is **Parker & Dimitrov**, OpenAlex W4294959637), the corrected files went in as **new** files alongside the stale originals. Canon Development therefore currently holds **duplicate names**. Use the ids above for the current versions. The **stale originals to ignore** (Ben will trash them) are:
- proposal `1qXOBzcAhserKohqHLHGka0eg707BT8GL` (17,759 B — older, has the "Gedeon" error)
- script `1iLWTxkeMD_2pnYqqIRMkvGNEtgb_Jhnc` (13,255 B — older)
- figure `17Zd-KHdVZkAwpGMdUZ9vwTMeXbtfmqzG` (223,701 B — older)

Quick disambiguation if you're unsure which is which: the **current** proposal and script are the **larger** byte sizes; the current figure is the **smaller** one (218,874 B — it was re-rendered after a label-overlap fix).

Thank you for looking these over.

— Claude Science (builder)
