# Citation lane — salvaged verification against primary sources

**Date:** 2026-08-07
**Seat:** Claude Science, attack seat (main session).
**Status:** Non-canon. **Partial lane.** The dedicated citation seat parked >80 minutes on a
network-access approval and was stopped; this document is what I verified myself, from primary
sources already in the project's Functional Persistence Library plus one live fetch. Items I could
not retrieve are recorded as NOT VERIFIED, not as passes.

**Method note.** Every VERIFIED row below means I opened the PDF, located the passage, and read it.
Quotes are ≤20 words and in quotation marks. Where only the bibliographic record was confirmed, the
row says PARTIAL and says why.

---

## 1. VERIFIED (with a correction) — Crutchfield & Feldman 2003, Proposition 8

**Source read:** `Crutchfield_Feldman_2003_RegularitiesUnseen_arXiv_cond-mat_0102181v1.pdf`
(project library; arXiv version of Chaos 13(1):25–54).

**Contract's claim (§1.2):** cites "Crutchfield & Feldman 2003 Prop. 8" for E as the past–future
mutual information under the **present-in-past** convention.

**What Prop. 8 actually says.** It exists, it is numbered 8, and it states E as a mutual information:
"The excess entropy is the mutual information between the left and right (past and future)
semi-infinite halves of the chain," given as E = lim_{L→∞} I[S₀…S_{2L−1} ; S_{2L}…] (their Eq. 53),
"when the limit exists." The gloss immediately after: E "measures the amount of historical
information stored in the present that is communicated to the future."

**Correction to the contract.** Prop. 8 establishes the **semi-infinite contiguous-halves** form. It
does **not** itself adjudicate the present-in-past vs excluded-present question that canon §4
condition 5 and the contract's §1.2 hang on it — the split in Eq. 53 is between two contiguous
semi-infinite blocks, and the placement of the present is a convention the proposition's notation
inherits rather than argues for. The canon and the contract are **substantively right** about the
convention and right that C&F is the source for the contiguous form; the citation is slightly
over-specific in implying Prop. 8 settles the present's placement. **Consequence: cosmetic.** Cite
Prop. 8 for the contiguous semi-infinite MI form and state the present-in-past placement as the
convention adopted (which the canon already does correctly elsewhere).

**E = 0 ⟺ i.i.d.** The paper supports the direction the theorem needs, in its process
classification: "Memoryless processes: ... We have E = 0 and T = 0. Independent, identically
distributed (IID) processes are examples of this class." That is i.i.d. ⇒ E = 0, stated for the
memoryless class rather than proved as a biconditional. Canon §4 **derives** the equivalence inline
(via shift-invariance, stationarity, and induction on the split), which is the correct posture — and
note the fidelity audit's separate finding that the contract mis-numbers this to canon reference
[13], which is a different paper.

## 2. VERIFIED — the Golden Mean value, and an independent corroboration of F2

**Source read:** same PDF.

**Golden Mean.** "We find that E ≈ 0.2516 bits, and T = E" — matching the contract's asserted 0.2516
and my exact computation of 0.2516291674. The contract is right and this is the suite's one clean
benchmark. C&F also give H(1) ≈ 0.9183 bits for that process.

**Even Process — this is the important one.** C&F report the Even Process's entropy rate as
hµ = 2/3 bits/symbol (matching my exact value) and **"We find that E ≈ 0.902 bits"** — consistent
with my bracket [0.917810, 0.918493] at p = 1/2 up to their fit precision and their stated numerical
method. Decisively for **F2**, they characterize its convergence directly: "The convergence of
hµ(L) is exponential," fitting hµ(L) − hµ = A·2^(−γL) with **A = 0.388 ± 0.019 and γ = 0.501 ± 0.007**.

γ ≈ 1/2 is exactly the exponent I derived analytically for the projection residual, ρ_k ∝ k·2^(−k/2).
So the peer-reviewed source for the Even Process **independently corroborates F2**: the process's
memory converges geometrically with exponent 1/2. The contract's §3.2.2 claim that on the Even
Process "ρ_k stays strictly positive — the ladder never saturates" is contradicted not only by my
computation but by the primary literature on the very process it selected. C&F also confirm the
antecedent the contract got right: the even system is sofic and "no finite-order Markovian source can
generate this," i.e. infinite Markov order — which is precisely the distinction F2 says the contract
collapsed. **Consequence: upgrades F2 from an internal computation to a cited result.**

## 3. VERIFIED — Still et al. 2012, and the contract's removal was correct

**Source read:** `Still_Sivak_Bell_Crooks_2012_ThermodynamicsOfPrediction_arXiv1203.3271v3.pdf`.

**The claim it is cited for** (canon [3], contract §5): dissipation is tied to the *nonpredictive*
retained information. The abstract states it: "The remaining nonpredictive information reflects model
complexity that does not improve predictive power," and the paper exposes "the fundamental
equivalence between this model inefficiency and thermodynamic inefficiency, measured by dissipation."
**VERIFIED** for exactly that claim.

**The removal check.** Searching the full text: "excess entropy" occurs **0** times, "entropy
production" occurs **0** times, "E > 0" occurs **0** times. The paper contains nothing that could
establish σ>0 ⇒ E>0. **The contract's §5 citation correction — removing Still et al. as the source of
that theorem and keeping it only for the nonpredictive-information claim — is correct and is a real
repair.** This one v0.2 → v0.2.1 fix is fully discharged.

## 4. VERIFIED — Baiesi & Maes supports the §10 sentence

**Source read:** `baiesi_maes_2018_life_efficiency_dissipation_rate_JPhysCommun_VOR.pdf` — Marco
Baiesi and Christian Maes, "Life efficiency does not always increase with the dissipation rate",
*J. Phys. Commun.* **2** (2018) 045017, doi 10.1088/2399-6528/aab654 (version of record, in the
project library).

**Contract's §10:** the budget-framing falsification is "now supported by Baiesi & Maes" — with no
citation given.

**Verdict: the claim is TRUE and the citation is MISSING.** The paper's abstract states: "There does
not exist a general positive correlation between important life-supporting properties and the entropy
production rate," because "nondissipative and time-symmetric kinetic aspects are also relevant for
establishing optimal functioning." That is direct support for the §10 finding that σ is not
substitutable against the other axes at fixed persistence (canon §12 Table 4: σ̇ "ranges 0.000
(barrier, a passive wall) to 1.313 (flux), 157% of its mean" on the iso-P surface — verified verbatim
by the fidelity audit).

**Consequence: minor but real.** The support is genuine, so this is not a false attribution — it is
an unreferenced one, which by the charter's own standard ("a reference is not verified until someone
has read the thing it points to") is a defect a reader cannot check. Add the full citation. Note the
paper's own framing is *stronger* than "supports": it independently reaches the contract's
conclusion, which is the charter's best case — a "new" result that a published paper already found.

## 5. VERIFIED — K&W stored/observed split and sign convention; equation numbers NOT VERIFIED

**Sources read:** `kolchinsky_wolpert_2018_semantic_information_arxiv_1806.08053.pdf` (project
library) and a live fetch of doi 10.1098/rsfs.2018.0041, which resolved via Unpaywall (bronze OA) to
**the same arXiv PDF** — byte-identical opening text, 19 pages.

**(a) Stored vs observed — VERIFIED.** The paper defines "stored semantic information" from the
initial joint p(x₀,y₀), and separately derives "observed semantic information" from transfer entropy,
noting stored semantic information "does not measure semantic information which is acquired by
ongoing dynamic interactions." The contract's §4 mapping of Type A → stored and Type B → observed,
and its nuance that K&W's observed operation severs environment→system while Memory severs the
system's own past→future, is faithful to this structure.

**(b) Sign convention — VERIFIED, contract is right.** The paper: "We define the (viability) value of
information as the difference between the system's viability after time τ under the actual
distribution, versus the system's viability after time τ under the intervened distribution." That is
**actual − intervened**, exactly as the contract's §0 asserts. So the contract's statement that
"K&W value = −(this contract's ΔV_N)" is correct, and its instruction to flag the sign on any K&W
cross-reference is sound. The paper also independently motivates the contract's model 6: it names the
negative case as "a mutant 'anti-chemotactic' bacteria, which senses the direction of" the gradient
and acts wrongly on it.

**(c) Equation numbers "Eq 5.2", "Eq 5.14", sections "5.1.1", "5.2" — NOT VERIFIED.** The arXiv
version uses **roman-numeral** sectioning (II, V, VI …); the strings `5.1.1`, `(5.2)` and `(5.14)`
occur **zero** times in it. The contract's decimal numbering must come from the *Interface Focus*
published version, which I could not retrieve — the DOI resolves to the arXiv preprint. **This is
the contract's most specific citational commitment and it is currently uncheckable by any seat
working from the open-access copy.** Since `AOP_KW2018_Verification_SpineClaims_20260806` is cited as
having verified these, that document should be re-read to confirm which version it checked. Repair:
cite both (arXiv §V B and the journal equation numbers), or cite the arXiv numbering only.

**(d) K&W code — VERIFIED as available.** `kolchinsky_semantic_information_code_20260805.tar.gz`
is in the project library, so §9's "simulable (K&W code)" for models 5 and 6 is supportable. I did
not run it.

---

## 6. NOT VERIFIED — items the stopped seat was to cover

Recorded honestly as open, not as passes. Each needs a seat with publisher access or a library copy.

| Item | What is needed | Why it matters |
|---|---|---|
| **Spinney & Ford 2012 / Ford & Spinney 2012** | Primary text for the odd/even-variable entropy-production decomposition, and the claim that the two-component treatment is the special case where the stationary law is symmetric in odd variables | Canon §4 condition 3 and the contract's parity condition rest on it. Canon cites it in bracketed author-year form; nobody in this session read it. |
| **Schnakenberg 1976** (Rev. Mod. Phys. 48:571) or equivalent | The cycle-affinity formula and Kolmogorov's cycle criterion | Would put F5's correction ("single transition channel," not "two-state") on a cited footing rather than my computation alone. My two-channel counterexample stands on its own arithmetic, but the textbook statement should be cited. |
| **Parrondo, Van den Broeck & Kawai 2009** (New J. Phys. 11:073008) | Independent re-read of canon reference [1] | The fidelity audit read this and found C-1 **substantively correct** — [1] gives a single-time phase-space identity, not a stationary trajectory-level KL rate. That is a canon repair ticket and deserves a second reader, since the contract's own §1.3 σ_Δ(t) is defined as exactly the object [1] does not supply. |

---

## 7. Net effect on the break attempt

| # | Item | Verdict | Effect |
|---|---|---|---|
| 1 | C&F Prop. 8 for present-in-past | VERIFIED with correction | cosmetic — cite Prop. 8 for the contiguous form, state the convention separately |
| 2 | Golden Mean E ≈ 0.2516 | VERIFIED | contract right; the suite's one clean benchmark |
| 2 | Even Process convergence γ = 0.501 ± 0.007 | VERIFIED | **strengthens F2** — the primary source independently gives the 2^(−k/2) exponent |
| 3 | Still et al. cited only for nonpredictive information | VERIFIED | **a v0.2.1 repair that fully worked**; removal was correct |
| 4 | "now supported by Baiesi & Maes" | TRUE but UNCITED | minor — add the reference; the support is real and independently reached |
| 5a/5b | K&W stored/observed; sign = actual − intervened | VERIFIED | contract faithful |
| 5c | K&W "Eq 5.2 / 5.14", "§5.1.1 / §5.2" | **NOT VERIFIED** | open — uncheckable from the OA copy; re-read the spine-claims verification doc |
| 6 | Spinney & Ford; Schnakenberg; Parrondo re-read | **NOT VERIFIED** | open — needs publisher access |

**One finding here changes a verdict elsewhere.** Item 2 moves F2 from "my computation contradicts
the contract" to "my computation and the contract's own cited source both contradict the contract."
The Even Process's geometric convergence with exponent ≈1/2 has been in the literature since 2003, in
the paper the contract cites for E itself.

*Attack seat, 2026-08-07. Non-canon. Authorizes no canon edits. Items marked NOT VERIFIED are open,
and must not be reported as cleared.*
