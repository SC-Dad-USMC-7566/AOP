# AOP External Benchmark — Rejected Candidates, Screening Criteria, and Parked Leads

**File:** `AOP_Benchmark_RejectedCandidates_v0.1.md` · **Version:** v0.1
**Date:** 25 July 2026 · **Seat:** Claude Cowork (execution)
**Order:** `TASK_CW_AOP_Benchmark_Records_20260725` — Tasks 1.1, 1.2, 2.1, 2.2, 4.1
**Status:** Records file. Owns **no** AOP scientific claim. Phase B not begun; no answer key written; no AOP quantity computed.

**Grading convention.** Every substantive statement below is tagged `[settled]`, `[synthesis]`, or `[frontier]` per the canon convention. Retrieval status is tagged separately: `[primary-verified]`, `[primary-abstract-only]`, `[secondary]`, `[not-retrieved]`.

**Retrieval caveat that applies to this whole file.** All web retrieval in this pass ran through `WebSearch` + `WebFetch` only (Nimble CLI absent). Passages marked verbatim passed through WebFetch's summarising layer — they are **reported-verbatim, not keystroke-verified against the rendered page**. Anyone freezing a key on these must confirm against the publisher PDF.

---

## 1. Purpose

This file records candidate systems **rejected** for the AOP external benchmark, the operative reason for each rejection, one **new screening criterion** derived from the pattern of rejections, and one lead **parked** pending a Step 0 ruling. It exists so that later seats do not re-litigate closed candidates, and so that the reasons remain auditable.

It does not select a system. System selection is closed pending `TASK_CLEANSEAT_AOP_Step0_20260725`.

---

## 2. Rejected candidates

### 2.1 Bacteriophage λ lysis–lysogeny — REJECTED (round two, 25 July 2026)

λ was recommended by this seat as the R2 lead in `AOP_Benchmark_PhaseA_Finding_20260725.md`, on the ground that the Arkin/Ross/McAdams model outputs lysogenization frequency — the same quantity the mutant experiments measure — and therefore clears A.1.8(b), which killed all four Phase A candidates.

**The recommendation is withdrawn. λ is rejected without a Phase A round two.** The operative reason is A.1.7 (gate power), not A.1.8.

#### 2.1.1 Operative reason — λ's architecture is serial, not redundant `[settled]`

The cII/cIII relationship is an **epistatic chain**, not two parallel donors. CIII does not supply the activity CII supplies; CIII acts *upstream of CII's destruction*, by inhibiting the host protease FtsH (HflB) that degrades CII. Remove the protease and CIII has nothing to do.

`[primary-verified]` **Kobiler O, Rokney A, Oppenheim AB (2007). "Phage Lambda CIII: A Protease Inhibitor Regulating the Lysis-Lysogeny Decision." *PLoS ONE* 2(4):e363. DOI 10.1371/journal.pone.0000363.** Full text retrieved (open access). Reported verbatim:

> "the protease inhibitor CIII is present as oligomeric amphipathic α helical structures and functions as a competitive inhibitor of FtsH by preventing binding of the CII substrate."

> "Real-time analysis of CII activity demonstrates that the effect of CIII is not seen in the absence of either FtsH or HflKC."

> "both host mutants show efficient suppression of the *cIII* mutation, suggesting that in the absence of FtsH and HflKC, CIII is dispensable."

That last sentence is the decisive one. A **redundant** donor's contribution does not vanish when a *different* component is removed; a **serial** component's does. λ's CIII is serial.

`[primary-abstract-only]` **Herman C, Thévenet D, D'Ari R, Bouloc P (1997). "The HflB protease of *Escherichia coli* degrades its inhibitor lambda cIII." *J Bacteriol* 179(2):358–363.** Abstract retrieved via PMC; full text not read. Reported verbatim:

> "The cIII protein of bacteriophage lambda is known to protect two regulatory proteins from degradation by the essential *Escherichia coli* protease HflB (also known as FtsH), viz., the lambda cII protein and the host heat shock sigma factor sigma32."

> "lambda cIII, itself an unstable protein, is partially stabilized when the HflB concentration is decreased, and its half-life is decreased when HflB is overproduced, strongly suggesting that it is degraded by HflB in vivo."

#### 2.1.2 λ's singles are not near-WT — the inverse of the redundancy signature `[synthesis]`

The gate (A.1.7) is built to score the LeDeaux signature: **singles ~WT, double collapses.** λ presents the inverse — a single perturbation of the CIII arm already collapses lysogeny.

`[primary-verified]` Kobiler et al. 2007, Table 1: a dominant-negative CIII allele (R32A) carried on a plasmid reduced "the frequency of lysogeny from 10% to 0.22%" on infection by wild-type λ — a ~45-fold collapse from a **single** perturbation.

**What I did NOT verify, and it matters.** I did **not** retrieve a primary reporting a direct lysogenization frequency for a λ*cIII*⁻ phage versus λ⁺ under standard conditions, nor any number for a λ*cII*⁻ phage. Kobiler et al. 2007 does not print one (checked). The R32A figure above is a *host-carried dominant-negative*, not a phage *cIII* null; treating it as one would be a substitution. The claim "*cII* and *cIII* mutants lysogenize only rarely" is, in this file, supported by §2.1.1's epistasis plus the R32A datum — **not** by a retrieved null-mutant frequency. Grade it `[synthesis]`, not `[settled]`, until a primary is read.

#### 2.1.3 CORRECTION to the issuing order — the Arkin model does *not* lump CII degradation

The order (§1, third bullet) states that "the Arkin/McAdams/Ross model lumps CII degradation rather than carrying hflA and hflB as separate species, so that entry likely fails A.1.8 anyway." **This is not what the paper says, and the sub-argument should be struck.**

`[primary-verified]` **Arkin A, Ross J, McAdams HH (1998). "Stochastic Kinetic Analysis of Developmental Pathway Bifurcation in Phage λ-Infected *Escherichia coli* Cells." *Genetics* 149(4):1633–1648.** Full text PDF retrieved via PMC (PMC1460268). Reported verbatim:

> "The best satisfaction of the constraints (a) through (d) was obtained using a proteolytic system in which CII and CIII are competitive substrates for two independent proteases."

> "These proteases correspond to HflB and the putative second protease identified by Kihara et al. (1997)."

So: **two separate protease species (P1, P2), and CIII present as its own species with its own synthesis and degradation.** CII proteolysis is *not* lumped. On output, the model reports the quantity the experiments measure — reported verbatim: "The expected fraction of lysogens at a given API, F_lysogens, is then… F(M) is the estimated probability of lysogeny for cells with various MOIs."

**What this does and does not rescue.** It rescues A.1.8(b) — the model's output *is* the measured quantity — which is exactly why λ was proposed. It partly rescues A.1.8(a) for a *hflB*-like perturbation, since P1 is identified with HflB. It does **not** rescue a *hflA* perturbation: P2 is named as a *putative, unidentified* second protease, not as HflKC/HflA, so `hflA∆` has no well-defined referent in the model. λ therefore still fails A.1.8(a) *for the host-side pair specifically* — but on a narrower and more defensible ground than the order states.

**Net.** λ's rejection stands on **A.1.7**: the phage-side circuit is serial, so it cannot supply ≥2 redundant pairs, and the one plausibly-synergistic host-side pair (*hflA hflB*) is only half-representable in the model. The order's A.1.8 sub-argument is withdrawn as stated. `[synthesis]`

#### 2.1.4 The *hflA hflB* claim is UNVERIFIED

The order states "the clearest synergistic pair in λ is host-side — the *hflA hflB* double is more severe than either single." `[not-retrieved]` I could not verify this against a primary. The designated source, **Banuett F, Hoyt MA, McFarlane L, Echols H, Herskowitz I (1986), "hflB, a new *Escherichia coli* locus regulating lysogeny and the level of bacteriophage lambda cII protein," *J Mol Biol* 187(2):213–224 (PMID 2939254)**, was not retrieved: ScienceDirect is disallowed by robots.txt and PubMed served a reCAPTCHA. **Do not treat the *hflA hflB* synergy as established on the strength of this file.** It does not change the rejection, because §2.1.1 and §2.1.3 are sufficient on their own.

#### 2.1.5 λ verdict

**REJECTED.** Cannot plausibly reach A.1.7's ≥2 redundant pairs. No Phase A round two on λ. Do not reopen without a primary demonstrating two *parallel* λ components whose singles are near-WT.

---

### 2.2 Prior rejections (Phase A, 25 July 2026) — one line each

Full evidence in `AOP_Benchmark_PhaseA_SystemSelection_v0.1.md` (Drive `11XDVzDUD0TF4hpbEc8tO0C9lY9oWsTFD`) and the four evidence files.

| Candidate | Operative reason for rejection |
|---|---|
| ***B. subtilis* sporulation phosphorelay** | **A.1.8(a).** No published dynamical model carries KinB or KinC as a species, so the *kinA kinB* double — the strongest and best-replicated fact in the ground truth — is not expressible as a perturbation of any published model. A.1.8(b) fails in parallel: mechanism-bearing models emit Spo0A~P and transcripts, never a spore titre. |
| **Yeast HOG pathway** | **A.1.8**, compounded by weak ground truth. The one independence-clean model deliberately deleted both branches and replaced them with a Hill term; the combinatorial ground truth is qualitative plate streaks; only 4 clean entries — fails A.1.7 on power as well. |
| **Yeast GAL network** | **A.1.7 (combinatorial data absent).** The canonical experiment is a *triple* with an expression readout; no double-knockout data for the key pair. Growth is not survival, and the system is bistable, so the persistence outcome is not well-posed. 4 entries. |
| ***E. coli* DNA repair** | **A.1.7 (power).** Best persistence readout of the four (survival fraction), but only 5 scorable entries from a thin, single-source classical literature. A.1.8 fails as well. |

---

## 3. New screening criterion

### A.1.9 — the adequacy/redundancy anti-correlation `[frontier — screening heuristic]`

> **A.1.9.** Condition (b) satisfaction and redundancy-richness are anti-correlated across the candidate space, and not by accident. Systems whose models emit the measured quantity are studied as *switches* (bistability, decision), and switches have no redundant architecture to score. Systems with redundant architecture are studied as *survival* systems, and their models stop at molecular observables. Any future candidate must be screened against this jointly, not against (b) and A.1.7 in sequence.

**Grade and standing — read this before using A.1.9.** A.1.9 is a **screening heuristic derived from two rounds of negative results** (four Phase A candidates, then λ). It is **not** an established law of biological modelling, it has no independent literature support, and no one has tested it against a systematic sample of the modelling literature. Its evidence base is five candidates, all screened by one seat, in one pass, with an exhausted search budget. It is `[frontier]` under the canon convention, and it should be used the way a triage rule is used — to order the search, never to close a candidate on its own.

**How to apply it.** Screen (b) and A.1.7 **jointly and first**: before spending retrieval on a candidate, ask whether the same paper population that supplies its quantitative combinatorial knockout data also supplies a dynamical model emitting that same measured quantity. If the ground truth and the models sit in disjoint literatures, expect failure and price the retrieval accordingly.

**What would falsify it.** A single candidate system carrying (i) a published dynamical model whose output is the organism-level persistence observable, *and* (ii) ≥2 redundant pairs with near-WT singles expressible as perturbations of that model. One such system refutes A.1.9 as stated and is, by construction, the benchmark system we are looking for. **A.1.9 must not be used as a reason to stop searching for exactly that system.**

---

## 4. Parked leads — do not pursue before Step 0 reports

### 4.1 Genome-scale metabolic models (FBA) `[frontier — parked]`

> Flux-balance models emit growth rate; quantitative double-knockout fitness maps supply redundancy and synergy at enormous scale; models are built from stoichiometry rather than fitted to the interaction data, so A.1.6 independence is clean. **Fatal caveat, unresolved:** FBA is steady-state with no dynamics, so Drive and Memory may not be computable on it at all. This lead lives or dies on Step 0 §2.1, and must not be pursued before Step 0 reports.

**One paragraph on Drive, then stop (per order §4.1).** Drive, as AOP defines it, is a claim about the maintained flow that holds a system away from equilibrium — a rate quantity read off a trajectory. A flux-balance solution is a stationary flux vector obtained by optimising an objective subject to stoichiometric and capacity constraints; it has fluxes, which is more than a purely structural model offers, but it has no time axis and no relaxation. Whether a stationary flux distribution supports an AOP Drive reading, or whether Drive requires an explicitly dynamical trajectory (in which case FBA is disqualified outright and Memory with it, since Memory is a claim about history-dependence and a steady state has no history), is precisely the question Step 0 §2.1 is convened to settle. **No retrieval has been done on this lead and none should be until Step 0 reports.** `[frontier]`

---

## 5. Closed as moot (Task 2.2)

| Item | Prior status | Now |
|---|---|---|
| **Jabbari S, King JR, Heap JT (2011), *Bull Math Biol* 73:181–211** | Open retrieval gap; internals unread after five blocked routes | **CLOSED — MOOT.** A.1.8(b) is fatal to the sporulation candidate regardless of Jabbari's species list: the sporulation ground truth is a spore titre and no sporulation model emits one. Its internals cannot change the verdict. Do not re-attempt. (Author-order discrepancy between the Springer and Birmingham records remains unresolved and now does not matter.) |
| **BioModels curated sporulation/phosphorelay entries** | Open retrieval gap; `ebi.ac.uk` returned 429 then 403 across four attempts | **CLOSED — MOOT.** Same reason, plus system selection is closed pending Step 0. Do not re-attempt. |

Recording these as **closed-as-moot** rather than **open** is deliberate: an open gap invites a future seat to spend retrieval on it. Neither can change any live decision.

---

## 6. Burbulys, Trach & Hoch 1991 — retrieval note (Task 2.1)

*Folded into this file rather than deposited separately, per order §5's "your call". This is that call, and it is stated here so the record is unambiguous.*

**Target.** Burbulys D, Trach KA, Hoch JA (1991). "Initiation of sporulation in *B. subtilis* is controlled by a multicomponent phosphorelay." *Cell* 64(3):545–552. DOI 10.1016/0092-8674(91)90238-T. PMID 1846779.

**Status: NOT RETRIEVED. `[not-retrieved]` Not one word of the paper's own text — not even its abstract — was obtained in this pass.** Citation metadata (authors, title, journal, volume, pages, year, DOI) was verified against the Crossref record in the prior pass and is unchanged; **the citation is verified, the content is not.**

### 6.1 Routes tried, this pass

| # | Route | Result |
|---|---|---|
| 1 | `cell.com/cell/abstract/0092-8674(91)90238-T` | **HTTP 403** |
| 2 | `sciencedirect.com/science/article/abs/pii/009286749190238T` | **Disallowed by robots.txt** |
| 3 | `pubmed.ncbi.nlm.nih.gov/1846779/` | **reCAPTCHA challenge page served instead of content** |
| 4 | Europe PMC REST API (`ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:…`) | **Fetch permission not granted (provenance gate); no response obtained** |
| 5 | `europepmc.org/article/MED/1846779` | **Fetch permission not granted (provenance gate)** |
| 6 | `api.openalex.org/works/doi:10.1016/0092-8674(91)90238-T` | **All paths disallowed by robots.txt** |
| 7 | Targeted PDF sweeps (`filetype:pdf`, repository/Semantic Scholar/ResearchGate terms) | **No open copy surfaced.** Every hit was a *citing* paper, not the paper |
| 8 | Semantic Scholar paper page | **Empty content returned** |

Routes tried in the **prior** pass and still failing: ScienceDirect, Crossref (metadata only, no abstract in record), Europe PMC REST (HTTP 429), PubMed web UI (reCAPTCHA), NCBI E-utilities (disallowed by robots.txt).

**Assessment.** *Cell* 1991 is closed-access with no green-OA deposit and no PMC record. This is not a route-selection failure that a cleverer query fixes; the text is behind a paywall this seat cannot lawfully pass. **Escalation to Ben is required:** an institutional login, a library ILL request, or a purchased PDF is the realistic path. Two routes (4 and 5, Europe PMC) failed only on an interactive permission gate and **may succeed in an attended session** — those are the cheapest retries and should be tried first.

### 6.2 The wiring, as the primary states it — CANNOT BE REPORTED

The order asks for the wiring as the primary states it: which kinases feed which phosphotransfer step, where the phosphatases act, and whether the primary itself distinguishes KinA from KinB as separate donors. **None of these can be answered from the primary, because the primary was not read.** No substitution is offered, per order §2.1 ("Do not substitute a secondary and call it retrieved").

For the record, and explicitly **not** as a substitute: the architecture is currently held in the Phase A evidence file on the strength of two *retrieved* primary-research papers that report (not establish) the relay — Quisel, Burkholder & Grossman 2001, *J Bacteriol* 183(22):6573–6578, and Brunsing et al. 2005, *J Bacteriol* 187(20):6972–6981. Those give Kin(A/B/C/D/E) → Spo0F → Spo0B → Spo0A. **This is architecture-known, not primary-verified**, and per order §2.1 it remains insufficient to close the gap.

**Consequence for sequencing:** the Burbulys gap is still open, and per order §2.1 and Step 0 §3.1 it must close **before any answer key freezes**. It is now the binding retrieval constraint on the benchmark. `[settled — procedural]`

---

## 7. What this file does not do

- It does not select a benchmark system. That is closed pending Step 0.
- It does not write, sketch, or imply an answer key.
- It does not grade its own output. Prime verifies by re-running the retrievals or by independent reconstruction — in particular §2.1.3 (the correction to the order) and §6.1 (the blocked-route ledger), which are the two places where this seat contradicts or constrains the issuing order.

---

*End of `AOP_Benchmark_RejectedCandidates_v0.1.md` v0.1.*
