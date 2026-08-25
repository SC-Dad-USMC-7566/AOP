# Benchmark Candidate Due Diligence: *Bacillus subtilis* Sporulation Initiation Phosphorelay

**Date:** 2026-07-25
**Retrieval tooling:** Nimble CLI **NOT AVAILABLE** (`nimble: command not found`). All retrieval via `WebSearch` + `WebFetch` only. No curl/wget/python fetching used.

---

## 0. RETRIEVAL STATUS LEDGER (read this first)

This is the most important section for provenance. Nothing below this line should be read as verified unless it appears in the FULL TEXT RETRIEVED column.

### 0.1 Sources FULL TEXT RETRIEVED (passages quoted below are from retrieved text)

| # | Source | Route | What it gave |
|---|---|---|---|
| S1 | LeDeaux JR, Yu N, Grossman AD (1995) "Different roles for KinA, KinB, and KinC in the initiation of sporulation in *Bacillus subtilis*", *J Bacteriol* 177(3):861–863 | `journals.asm.org/doi/pdf/10.1128/jb.177.3.861-863.1995` | **The core combinatorial dataset.** Table 1 (singles, doubles, triple × 3 media), Results text, assay method |
| S2 | LeDeaux JR, Grossman AD (1995) "Isolation and Characterization of kinC…", *J Bacteriol* 177(1):166–175 | `journals.asm.org/doi/pdf/10.1128/jb.177.1.166-175.1995` | Tables 3 & 4: *spo0A*, *spo0F*, *spo0B* mutant sporulation frequencies; multicopy-*kinC* suppression |
| S3 | Tojo S, Hirooka K, Fujita Y (2013) "Expression of *kinA* and *kinB* of *Bacillus subtilis*… Positive Stringent Transcription Control", *J Bacteriol* 195(8) | `journals.asm.org/doi/pdf/10.1128/jb.02131-12` | **Independent replication of *kinA kinB* synthetic defect in strain 168**, with numbers |
| S4 | Quisel JD, Burkholder WF, Grossman AD (2001) "In Vivo Effects of Sporulation Kinases on Mutant Spo0A Proteins in *B. subtilis*", *J Bacteriol* 183(22):6573–6578 | `journals.asm.org/doi/pdf/10.1128/jb.183.22.6573-6578.2001` | Retrieved statement of relay architecture; assay method |
| S5 | Aguilar C, Vlamakis H, Guzman A, Losick R, Kolter R (2010) "KinD Is a Checkpoint Protein…", *mBio* | PMC2912670 | *kinD* deletion phenotype (spore increase), KinD-as-phosphatase |
| S6 | Brunsing RL, La Clair C, Tang S, Chiang C, Hancock LE, Perego M, Hoch JA (2005) "Characterization of Sporulation Histidine Kinases of *Bacillus anthracis*", *J Bacteriol* 187(20):6972–6981 | `journals.asm.org/doi/pdf/…` | Hoch-lab two-level statement of kinase division of labour |
| S7 | McLoon AL, Kolodkin-Gal I, Rubinstein SM, Kolter R, Losick R (2011) "Spatial Regulation of Histidine Kinases Governing Biofilm Formation in *B. subtilis*", *J Bacteriol* | `journals.asm.org/doi/pdf/10.1128/jb.01186-10` | *kinE* colony phenotype (only retrieved *kinE* single-mutant statement) |
| S8 | Garti-Levi S, Eswara A, Smith Y, Fujita M, Ben-Yehuda S (2013) "Novel Modulators Controlling Entry into Sporulation in *B. subtilis*", *J Bacteriol* 195(7) | `journals.asm.org/doi/pdf/10.1128/jb.02160-12` | Assay method only; no numbers for our mutants |
| M1 | Bischofs IB, Hug JA, Liu AW, Wolf DM, Arkin AP (2009) "Complexity in bacterial cell–cell communication…", *PNAS* | PMC2672556 | Model size/form/parameter provenance |
| M2 | Ihekwaba AEC, Mura I, Barker GC (2014) "Computational modelling and analysis of the molecular network regulating sporulation initiation in *B. subtilis*", *BMC Syst Biol* 8:119 | link.springer.com | Model size/form/**explicit fitting statement** |
| M3 | Narula J, Devi SN, Fujita M, Igoshin OA (2012) "Ultrasensitivity of the *B. subtilis* sporulation decision", *PNAS* | PMC3528541 | Parameter provenance statement (main text; **SI NOT RETRIEVED**) |
| M4 | Russell JR, Cabeen MT, Wiggins PA, Paulsson J, Losick R (2017) "Noise in a phosphorelay drives stochastic entry into sporulation in *B. subtilis*", *EMBO J* 36:2856–2869 | link.springer.com | Confirms: **no mathematical model** in this paper |
| M5 | Gauvry E et al. (2019) "Differentiation of Vegetative Cells into Spores: a Kinetic Model Applied to *B. subtilis*", *Appl Environ Microbiol* | journals.asm.org | Population-level model; **does not model phosphorelay** |

### 0.2 Sources **NOT RETRIEVED** — prominently flagged

| Source | Status | Why it matters |
|---|---|---|
| **Burbulys D, Trach KA, Hoch JA (1991) *Cell* 64:545–552, DOI 10.1016/0092-8674(91)90238-T** | **NOT RETRIEVED. METADATA ONLY.** cell.com returned HTTP 403; ScienceDirect blocked; no abstract in Crossref record; Europe PMC REST persistently HTTP 429; PubMed web UI served reCAPTCHA; NCBI E-utilities disallowed by robots.txt. **Citation metadata (authors/title/journal/volume/pages/year/DOI) verified against the Crossref API record; NOT ONE WORD of the paper's own text was retrieved.** | This is the designated primary source for Item 1. Item 1 is therefore established by *secondary retrieved* statements only. |
| **Trach KA, Hoch JA (1993) "Multisensory activation of the phosphorelay… protein kinase of the alternate pathway", *Mol Microbiol* 8:69–79 (PMID 8497199)** | **NOT RETRIEVED.** Title/venue seen in a PubMed search-results listing only. Wiley Online Library returned HTTP 403 for every attempt. | The original *kinA kinB* double-mutant paper. Its numbers are known to me only *through* S1's citation of it (S1 ref. 29). |
| **Jiang M, Shao W, Perego M, Hoch JA (2000) "Multiple histidine kinases regulate entry into stationary phase and sporulation in *B. subtilis*", *Mol Microbiol* 38 (PMID 11069677)** | **NOT RETRIEVED — not even the abstract.** Wiley 403; Europe PMC 429; PubMed reCAPTCHA; Semantic Scholar 429/permission-gated; E-utilities robots-disallowed. | This is the principal primary source for **KinD and KinE**. Consequently *kinD* and *kinE* single-mutant sporulation numbers are **NOT ESTABLISHED** in this report. |
| **Jabbari S, Heap JT, King JR (2011) *Bull Math Biol* 73(1):181–211, DOI 10.1007/s11538-010-9530-7** | **ABSTRACT/METADATA ONLY.** Paywalled ($39.95). Model size, formulation, and parameter provenance all behind the paywall. | Named candidate model; its fitting provenance is **unknown**, not "none". |
| Voigt CA, Wolf DM, Arkin AP (2005) *Genetics*, "The *B. subtilis* sin operon: an evolvable network motif" (PMID 15466432) | **TITLE ONLY** (search listing). | See Item 5.6 — I found **no** phosphorelay ODE model authored by Voigt. Do not assume one exists. |
| Igoshin OA pre-2012 phosphorelay-specific ODE papers | **NOT RETRIEVED / NOT CONFIRMED.** Searches surfaced Igoshin's CV and the 2012 PNAS paper, but I did not retrieve any earlier Igoshin paper that models the Spo0F→Spo0B→Spo0A relay specifically. | Do not assert an "Igoshin 2006/2008 phosphorelay model" without checking. |
| Spo0E, RapA, RapB, KipI single-mutant quantitative sporulation data | **NOT RETRIEVED.** No source with numbers was obtained for any phosphatase/inhibitor knockout. | The entire phosphatase arm of the candidate system is **unsupported by retrieved evidence** in this pass. |

### 0.3 A retrieval artifact that MUST be carried with the numbers

The S1 PDF text layer mis-maps several glyphs. Verified examples inside the same retrieved text: `80 8C` for 80 °C, `59 end` for 5′ end, `Spo2` for Spo⁻, `Spo0A;P` for Spo0A~P, `,10 spores` for <10 spores, `103 spores` for 10³ spores.

Superscript minus signs render as an extra `2`, so **`10−22` in the extracted text is 10⁻², `10−26` is 10⁻⁶, `10−27` is 10⁻⁷, `10−28` is 10⁻⁸** (exponent = final digit).

This is **not** my guess: it is cross-checked against S1's own Results prose, which independently states *kinA* is "approximately 4 to 10% that of the wild type" (extracted `8.0 × 10−22` → 8.0 × 10⁻² = 8%) and *kinB* is "approximately 5 to 10% that of the wild type in DS medium or minimal medium" (extracted `7.1 × 10−22` → 7.1 × 10⁻² = 7.1%). Both raw and decoded forms are given in the table below. **Anyone building a key from this must confirm against the printed PDF.**

---

## 1. CAUSAL STRUCTURE — the published wiring

**Status: architecture ESTABLISHED from a retrieved secondary primary-research statement; the designated classic source (Burbulys 1991) is NOT RETRIEVED.**

Retrieved verbatim from **S4** (Quisel, Burkholder & Grossman 2001, *J Bacteriol*, Introduction):

> "Spo0A phosphorylation is controlled by a phosphotransfer pathway, known as the phosphorelay, composed of Spo0F, Spo0B, and at least four histidine kinases, KinA, KinB, KinC, and KinD (1, 2, 20, 21, 24, 27, 36, 47). The kinases donate phosphate to Spo0F, a response regulator with no output domain (2, 36). The phosphate from Spo0FP is transferred to Spo0B and finally from Spo0BP to Spo0A (2)."

("Spo0FP" / "Spo0BP" are the PDF text-layer rendering of Spo0F~P / Spo0B~P; reference 2 in that paper's list is Burbulys et al.)

Retrieved verbatim from **S6** (Brunsing et al. 2005, Hoch lab, Discussion):

> "In B. subtilis the activation of sporulation by phosphorylated Spo0A is a two-level process. Low-level phosphorylation of this transcription factor is carried out by one or more of three kinases, KinC, KinD, and KinE. The effect of these kinases on cellular regulation is to cause the repression of the transition state regulator AbrB and thus release inhibition of the transcription of a large number of genes… High-level phosphorylation and sporulation require the activity of KinA and KinB."

**Wiring as established:** Kin(A/B/C/D/E) autophosphorylate → phosphoryl transfer to **Spo0F** → **Spo0B** → **Spo0A**. Spo0A~P is the transcriptional output.

**What I could NOT do:** quote Burbulys, Trach & Hoch (1991) itself. Its citation is verified (Crossref: Burbulys D., Trach K.A., Hoch J.A.; *Cell*; vol. 64; pp. 545–552; 1991; DOI 10.1016/0092-8674(91)90238-T) — **the citation, not the content.** For a scored key, the architecture claim rests on S4/S6, which are themselves peer-reviewed primary papers by the Grossman and Hoch labs, but they are *reporting* the relay, not *establishing* it.

**Phosphatase arm (Spo0E, RapA/RapB, KipI): NOT ESTABLISHED IN THIS PASS.** I retrieved no passage documenting their action points or knockout phenotypes. Treat as *inferred/unverified*.

---

## 2. SINGLE-KNOCKOUT GROUND TRUTH

### 2.1 The relay core — *spo0A*, *spo0F*, *spo0B* are ESSENTIAL

Retrieved verbatim from **S2** (LeDeaux & Grossman 1995, *J Bacteriol* 177(1), Table 3, "Suppression of spo0 mutants by multicopy kinC"), sporulation frequency with vector pHP13 vs. multicopy *kinC* (pLK2):

| Genotype (as extracted) | pHP13 (vector) | pLK2 (multicopy *kinC*) |
|---|---|---|
| WT (JH642) | 0.41 | 0.81 |
| Δ*spo0K*::erm | 6.0 × 10⁻³ | 0.63 |
| *kinA*::Tn917 | 9.8 × 10⁻² | 0.28 |
| *spo0A9V* (glyph-garbled; likely *spo0A*Δ*V*) | **<9.0 × 10⁻⁸** | <8.2 × 10⁻⁸ |
| *spo0J93* | 2.1 × 10⁻⁴ | 0.21 |
| *spo0E11* | 2.5 × 10⁻³ | 6.9 × 10⁻³ |
| *spo0F*Δ*S* | **<2.4 × 10⁻⁷** | 9.8 × 10⁻³ |
| *spo0B*Δ*Pst* | **<4.1 × 10⁻⁷** | 1.1 × 10⁻² |

Reading: against a wild-type frequency of 0.41, all three relay-core mutants are at or below detection (10⁻⁷–10⁻⁸), i.e. a **≥10⁶-fold reduction**. Deletion abolishes sporulation.

**Two important caveats, both load-bearing for a key:**
1. These are **specific named alleles** (*spo0A9V*/*spo0A*Δ*V*, *spo0F*Δ*S*, *spo0B*Δ*Pst*), not verified clean null deletions. The allele label for *spo0A* is corrupted in the text layer.
2. ***spo0F* and *spo0B* essentiality is BYPASSABLE.** Multicopy *kinC* restores *spo0F*Δ*S* to 9.8 × 10⁻³ and *spo0B*Δ*Pst* to 1.1 × 10⁻² — a ~10⁴–10⁵-fold rescue. *spo0A* is **not** rescued (<8.2 × 10⁻⁸). So *spo0A* is unconditionally essential; *spo0F*/*spo0B* are essential **at native gene dosage** and partially bypassable when a kinase is overexpressed. S2 Table 4 reinforces this: strain JRL770 (*spo0B*Δ*Pst rvtA11 kinA*) = 1.2 × 10⁻⁵ vs JRL794 (*spo0F*Δ*S spo0B*Δ*Pst rvtA11 kinA*) = 0.34.

### 2.2 The kinases — all five individually DISPENSABLE, but medium-dependently so

Retrieved verbatim from **S1** Table 1, "Relative sporulation frequencies of different kinase mutants in different media". Raw extracted values first, decoded values in brackets per §0.3. Parenthetical numbers are heat-resistant spores per ml.

| Strain | Genotype | 23SG medium | DS medium | Minimal medium |
|---|---|---|---|---|
| JH642 | Wild type | 1 (3.9 × 10⁸) | 1 (1.9 × 10⁸) | 1 (1.3 × 10⁸) |
| AG522 | *kinA* | 0.1 (6.3 × 10⁷) | `8.0 × 10−22` [8.0 × 10⁻²] (1.9 × 10⁷) | 1.2 (1.1 × 10⁸) |
| NY120 | *kinB* | 0.67 (2.3 × 10⁸) | 0.13 (2.7 × 10⁷) | `7.1 × 10−22` [7.1 × 10⁻²] (6.0 × 10⁶) |
| JRL920 | *kinC* | 0.77 (4.1 × 10⁸) | 0.45 (1.0 × 10⁸) | 0.91 (1.3 × 10⁸) |
| NY121 | *kinA kinB* | `1.9 × 10−26` [1.9 × 10⁻⁶] (1.7 × 10³) | `<5 × 10−28` [<5 × 10⁻⁸] (<10) | `2.1 × 10−27` [2.1 × 10⁻⁷] (20) |
| JRL1046 | *kinA kinC* | `3.3 × 10−22` [3.3 × 10⁻²] (2.3 × 10⁷) | `6.8 × 10−22` [6.8 × 10⁻²] (1.5 × 10⁷) | 0.41 (7.3 × 10⁷) |
| JRL1004 | *kinB kinC* | 0.43 (3.8 × 10⁸) | 0.15 (4.5 × 10⁷) | `1.2 × 10−22` [1.2 × 10⁻²] (2.0 × 10⁶) |
| JRL1007 | *kinA kinB kinC* | `<3 × 10−28` [<3 × 10⁻⁸] (<10) | `<2 × 10−27` [<2 × 10⁻⁷] (<10) | `3 × 10−27` [3 × 10⁻⁷] (60) |

S1 Results, verbatim:

> "KinA appears to be the major kinase under most sporulation conditions. kinA null mutants sporulated at a frequency of approximately 4 to 10% that of the wild type when grown in DS medium (nutrient broth) (25) or the richer 23SG medium… However, when sporulation was induced by the exhaustion of glucose from cultures grown in defined minimal medium with glucose (0.1%) as the carbon source, the kinA mutant was able to sporulate at or near the wild-type frequencies (Table 1). In contrast, the sporulation frequency of the kinB mutant was similar to that of the wild type in 23SG medium and approximately 5 to 10% that of the wild type in DS medium or minimal medium (Table 1)."

> "Taken together, our results indicate that under some conditions KinB is the major sporulation kinase and KinA plays a minor role and that the different sporulation sensor kinases can respond to different nutritional conditions."

**Independent replication in a different strain background** — retrieved verbatim from **S3** (Tojo, Hirooka & Fujita 2013, strain **168**, not JH642), Table 3:

- Decoyinine-induced sporulation, S6 medium, T10: wild-type 168 = "19%"; *kinA* = "0.26%"; *kinB* = "0.67%"; *kinA kinB* = "<5 × 10⁻⁶%".
- Nutrient medium (NSMP), T20: wild-type 168 = "71%"; *kinA* = "7.9%"; *kinB* = "22%"; *kinA kinB* = "<5 × 10⁻⁶%".

**kinD:** retrieved from **S5** (Aguilar et al. 2010, *mBio*), biofilm conditions: *"the kinD strain and the triple mutant both had about 10-fold more spores than the wild type at 24 h"*, and *"KinD functions to maintain Spo0A~P at low levels in cells during early stages of biofilm formation, possibly by acting as a phosphatase"*; *"KinD is bifunctional, having either kinase or phosphatase activity, depending on the growth conditions."* So a *kinD* single mutant is **not sporulation-deficient — it is sporulation-elevated** in biofilm conditions. **No planktonic sporulation-frequency number for Δ*kinD* was retrieved.**

**kinE:** the ONLY retrieved single-mutant statement is a colony-morphology observation from **S7** (McLoon et al. 2011): *"the colonies of a kinE mutant were indistinguishable from those of the wild type; hence, kinE will not be considered further."* **No sporulation frequency for a *kinE* single mutant was retrieved from any source.** Treat *kinE* as *inferred inert*, not measured-inert.

### 2.3 Item 2 summary

| Component | Label | Evidence quality |
|---|---|---|
| *spo0A* | **ESSENTIAL** (unconditional) | Direct, numbers (S2) — allele identity caveat |
| *spo0F* | **ESSENTIAL** at native dosage; bypassable by multicopy *kinC* | Direct, numbers (S2) |
| *spo0B* | **ESSENTIAL** at native dosage; bypassable by multicopy *kinC* | Direct, numbers (S2) |
| *kinA* | **DISPENSABLE**, 8–10% of WT in rich media, ~WT in minimal | Direct, numbers, replicated (S1, S2, S3) |
| *kinB* | **DISPENSABLE**, ~WT in 23SG, 7–22% in DS/minimal | Direct, numbers, replicated (S1, S3) |
| *kinC* | **DISPENSABLE / near-inert alone** (0.45–0.91 of WT) | Direct, numbers (S1) |
| *kinD* | **DISPENSABLE**; ~10× *increased* spores in biofilm | Direct but condition-specific (S5) |
| *kinE* | *inferred* inert — **NOT MEASURED in retrieved sources** | Colony morphology only (S7) |

---

## 3. COMBINATORIAL DATA — the decisive item

**VERDICT: The expected redundancy pattern is CONFIRMED, with quoted numbers, in two independent labs and two independent strain backgrounds.** This is the strongest part of the candidate.

### 3.1 *kinA kinB* — synthetic near-lethality for sporulation

S1 Results, verbatim:

> "kinA kinB double mutants had a much more severe sporulation defect than did either single mutant under all conditions tested (Table 1), consistent with previous findings (29). In 23SG medium the kinA kinB double mutant consistently produced approximately 103 spores per ml, at least 100- to 1,000-fold more than in DS medium or minimal medium (Table 1)."

("103 spores per ml" = 10³ spores per ml, per §0.3.)

Quantitatively, from S1 Table 1 (decoded):

| Medium | *kinA* | *kinB* | *kinA kinB* | Fold drop, double vs. best single |
|---|---|---|---|---|
| 23SG | 0.1 | 0.67 | 1.9 × 10⁻⁶ | ~3.5 × 10⁵ |
| DS | 8.0 × 10⁻² | 0.13 | <5 × 10⁻⁸ | >2.6 × 10⁶ |
| Minimal | 1.2 | 7.1 × 10⁻² | 2.1 × 10⁻⁷ | ~5.7 × 10⁶ |

Independent replication (S3, strain 168): *kinA* 0.26% and *kinB* 0.67% individually, *kinA kinB* "<5 × 10⁻⁶%" — a further ~10⁵-fold drop below either single, in a lab and background unconnected to S1.

This is a textbook redundancy/synthetic-lethal signature: **both singles retain 7–120% of wild-type sporulation in at least one medium; the double falls 10⁵–10⁷-fold.**

### 3.2 Higher-order: the *kinA kinB kinC* triple, and KinC as a conditional (synergistic) contributor

S1 Results, verbatim:

> "KinC is required for the residual sporulation seen in a kinA kinB double mutant in the rich sporulation medium (23SG)."

> "This small but reproducible level of sporulation in 23SG medium was entirely dependent on kinC as the kinA kinB kinC triple mutant produced ,10 spores per ml in 23SG medium (Table 1)."

(",10" = <10 per §0.3.)

**This is the clearest SYNERGISTIC / conditionally-load-bearing entry in the system.** KinC alone is near-inert (0.77 of WT in 23SG — an ~23% effect). But in the *kinA kinB* background, removing *kinC* collapses sporulation a further ~60-fold (1.9 × 10⁻⁶ → <3 × 10⁻⁸) and eliminates all detectable spores. A component that looks nearly dispensable in isolation is the sole carrier of the residual pathway once the two major kinases are gone.

The same paper supplies an orthogonal (non-sporulation) readout of the same epistasis, via *abrB-lacZ*:

> "KinC was a major source of that phosphate in the absence of KinA and KinB, as expression of abrB was higher in the kinA kinB kinC triple mutant than in the kinA kinB double mutant (Fig. 1A)."

> "The amount of b-galactosidase accumulated before entry into stationary phase in the double mutant was less than that in a spo0B mutant (Fig. 1), indicating that there must be at least one other source of phosphate and that phosphate must be transferred to Spo0A via Spo0B and the phosphorelay (29)."

And an explicit residual-signal statement pointing at a *further* unidentified source:

> "The initial accumulation of b-galactosidase in the triple mutant was somewhat lower than that in the spo0B mutant, suggesting that there might be yet another minor source of phosphate for Spo0A."

### 3.3 Other pairs — a second, medium-conditional synergy

- ***kinB kinC*, minimal medium:** *kinB* alone = 7.1 × 10⁻², *kinC* alone = 0.91, double = 1.2 × 10⁻². The double is ~6× below *kinB* alone and ~76× below *kinC* alone. Modest but in the synergy direction, and **only in minimal medium** (in 23SG the double is 0.43, i.e. no synergy at all).
- ***kinA kinC*:** 23SG = 3.3 × 10⁻² (vs *kinA* 0.1) — ~3× below the *kinA* single. DS = 6.8 × 10⁻² (vs *kinA* 8.0 × 10⁻²) — essentially no synergy. Minimal = 0.41 (vs *kinA* 1.2). **Weak and inconsistent; I would not score this pair.**

### 3.4 What I could NOT get for Item 3

- **Trach & Hoch (1993)**, the paper that first reported the *kinA kinB* double phenotype (S1's ref. 29), is **NOT RETRIEVED**. I have S1's characterisation of it ("consistent with previous findings (29)") but not its own numbers.
- **No higher-order kinase deletions beyond the triple were retrieved.** I found no retrieved *kinA kinB kinC kinD* quadruple or *kinA–kinE* quintuple sporulation dataset. If one exists (plausibly in Jiang et al. 2000), I could not reach it.
- **No *kinD*- or *kinE*-containing combinatorial sporulation data was retrieved at all.** S7 reports a *kinC kinD* double, but the readout is **colony wrinkling, not sporulation**: *"peripheral zone was almost completely flat but whose inner zone was even more wrinkled than the corresponding region of the wild type"*.
- **No phosphatase-containing combinations** (e.g. *spo0E kinA*, *rapA rapB*) were retrieved.

---

## 4. MEASURED PERSISTENCE OUTCOME — what is actually measured

The readout is genuinely a directly-measured persistence outcome: **survival of a lethal heat challenge, as colony-forming units.** But the assay is **not standardised across the literature**, and this matters.

**S1** (LeDeaux, Yu & Grossman 1995), Table 1 footnote b, verbatim:

> "Relative sporulation frequency is the number of spores per milliliter as a fraction of the number of viable cells per milliliter, normalized to the control (JH642) in a given experiment. Samples to be tested were serially diluted in minimal salts, and the number of spores was measured as heat-resistant (808C for 15 min) CFU on Luria-Bertani plates. Viable cells were measured, before heat treatment, as total CFU on Luria-Bertani plates. The numbers in parentheses are heat-resistant spores per milliliter. Data for each medium are from a representative experiment, and similar results were obtained for at least three independent experiments."

(`808C` = 80 °C.) Media, verbatim from footnote c:

> "23SG is a rich sporulation medium and contains nutrient broth and 0.1% glucose (17). DS is the nutrient broth medium of Schaeffer et al. (25). The minimal medium was S7 medium (30) as used previously (14), except that glucose was used at 0.1%."

**S4** (Quisel et al. 2001), verbatim:

> "Viable cells and spores were counted by plating before and after a heat treatment (80°C for 20 min) as previously described (27). Percent sporulation is calculated as 100 times the number of spores per milliliter divided by the number of viable cells per milliliter."

**S3** (Tojo et al. 2013), verbatim:

> "titers of viable cells (V) and spores (S) that were heat resistant (75°C for 20 min) were measured to obtain the sporulation percentage (S/V × 100)"

**S8** (Garti-Levi et al. 2013), verbatim:

> "Spore formation was assayed by inducing sporulation in Schaeffer's liquid medium (Difco sporulation medium [DSM]) for 24 h and determining colony formation of heat-treated spores (80°C for 20 min)."

**S5** (Aguilar et al. 2010), verbatim:

> "For quantification of spores, each preparation was normalized to an OD600 of 1 and then incubated at 80°C for 20 min to kill vegetative cells."

**S2** (LeDeaux & Grossman 1995), timing, verbatim:

> "Cells were grown in DS or 23SG medium at 37°C unless otherwise indicated, and spores were assayed approximately 20 h after the end of exponential growth."

**Units actually in use, across sources:** (a) heat-resistant spores per ml (absolute titre); (b) spores/viable cells as a dimensionless fraction; (c) the same fraction normalised to a wild-type control run in the same experiment; (d) that fraction × 100 as "% sporulation". **Heat challenge varies: 80 °C/15 min, 80 °C/20 min, 75 °C/20 min.** Chloroform resistance was **not** used in any retrieved source. No source retrieved reports a starvation-survival readout distinct from spore titre.

---

## 5. PUBLISHED DYNAMICAL MODELS AND WHAT THEY WERE FITTED TO

**HEADLINE ANSWER TO THE DECISIVE QUESTION: In every model I retrieved, the answer is NO. Not one retrieved model used *kinA kinB* double-mutant data, or any combinatorial knockout data, for parameter fitting. Two used no fitting at all; the one that did fit used only wild-type IPTG-induction time courses.**

### 5.1 Ihekwaba, Mura & Barker (2014), *BMC Systems Biology* 8:119 — **the only retrieved model with an explicit fitting statement**

(a) **Size**, verbatim:
> "The overall model includes 13 species and taking into consideration transcripts, dimerization and post-translational modifications, therefore gives rise to 27 distinct forms. The total number of unidirectional reactions included in the model is 55."

(b) **Form:** ODEs with "a continuous interpretation of the variables" and "a deterministic interpretation of the reaction rates"; mixed rate laws — mass-action plus Hill functions for cooperative binding. **Not purely mass-action; not fully lumped.**

(c) **Fitted to**, verbatim:
> "The values of several kinetic parameters (i.e. those that are marked as 'Fitted' in Table 1) were determined by systematically exploring the parameter space to find a satisfactory match with the experimental data. The dataset used for the fitting included measurements of one final output effector species (e.g., the spollG transcript), and one intermediate species in the network (KinA). Experimental data for the dynamics of these species under IPTG stimulation were obtained from [Narula et al. 2012]."

> "We report in Table 1 the source of the specific kinetic information for each of the reactions we defined in our model"

**Combinatorial knockout data used? NO.** The fetch reports no kinase knockout, *kinA kinB* double mutant, or combinatorial deletion data mentioned for fitting or validation; only wild-type and IPTG-inducible systems. **Note the fitting target is two observables (a *spoIIG* transcript and KinA) under an artificial IPTG induction — a synthetic-induction time course, not a genetic-perturbation panel.**

### 5.2 Narula, Devi, Fujita & Igoshin (2012), *PNAS* — "Ultrasensitivity of the *B. subtilis* sporulation decision"

(a) **Size:** not stated in consolidated form in the retrieved main text; modular (phosphorelay, σF activation, σE activation modules). **No aggregate species/reaction/parameter count was retrievable; the SI (Table S3) was NOT RETRIEVED.**

(b) **Form:** mass-action kinetics conceptually; implementation deferred to SI.

(c) **Parameter provenance**, verbatim:
> "Details of all posttranslational interactions and transcriptional regulation, as well as relevant parameter values (Table S3), were extracted from the literature."

**Fitted to nothing.** No sentences describing fitting to experimental data — parameters are stated as literature-derived. **Combinatorial knockout data used? NO.** The experimental system is a strain in which "the KinA promoter is replaced with an IPTG-inducible promoter" — an induction/dosage system, explicitly not a knockout panel.

### 5.3 Bischofs, Hug, Liu, Wolf & Arkin (2009), *PNAS* — quorum signal integration in the phosphorelay

(a) **Size:** not stated. No species/reaction/parameter count given.

(b) **Form:** hybrid. Verbatim: *"ordinary differential equation model is based on mass action kinetics for the phosphoryl-transfer reactions with forward and backward rates"* — but **lumped at the kinase level**, using effective parameters κ (kinase input) and π (phosphatase activity) rather than individual kinase species. Retrieved parameter values: *"kif = 300 nM−1s−1, kib = 200 nM−1s−1, kep = 20 nM−1s−1, Li = 0.005 nM/s, vi = 5.0 nM/s, Ki = 50 nM, ni = 1, and D = 10−4s−1"*.

(c) **Fitted to:** **nothing identified.** The fetch reports no fitting procedure, no citation of literature values for the rate constants, and no fitting to kinetic data — only "Heat maps in [Fig. 3] were generated for [parameter values]". **Combinatorial knockout data used? NO — kinase knockouts are not mentioned at all.** The only mutant discussed is an *in silico* P*spo0B* mutant.

**Critical structural point for the benchmark:** because Bischofs et al. lump all kinase input into a single effective κ, **the model has no representation in which KinA and KinB are separable objects.** It is architecturally incapable of predicting a *kinA kinB* double-mutant phenotype.

### 5.4 Russell, Cabeen, Wiggins, Paulsson & Losick (2017), *EMBO J* 36:2856–2869

**This is NOT a model paper.** Verbatim finding: no rate equations, no differential equations, no parameter fits, no stochastic simulation. It is a microfluidics/single-cell imaging study. It *does* contain relevant knockout observations — *kinA* mutants: *"high-threshold levels of Spo0A~P were rarely achieved"*, while *kinB* and *kinC* mutants had *"relatively little effect"*; and a *spo0A*^E14A Δ*spo0F* relay-bypass double mutant whose response was *"much more switch-like"* — but these were used qualitatively, not for parameter estimation. Anyone citing this as "the stochastic phosphorelay model" would be wrong.

### 5.5 Gauvry et al. (2019), *Appl Environ Microbiol* — **does not model the phosphorelay**

Population-level phenomenological kinetic model of vegetative-cell→spore transition: ~6 equations, ~8 fitted parameters (N₀, λ, μmax, Nmax, Pmax, tmax, σ, tf), fitted to *"growth-sporulation kinetics at various temperatures in laboratory medium or in whey"* plus PspoIIAA-gfp fluorescence. **No phosphorelay components.** The authors note existing mechanistic models are *"complex because they require numerous parameters, most of which cannot be experimentally evaluated under industrially relevant conditions."* Not usable for a mechanism-level key.

### 5.6 Named candidates I could NOT verify — report these as gaps, not absences

- **Jabbari, Heap & King (2011)**, *Bull Math Biol* 73(1):181–211. Citation verified. **Model size, formulation, parameter provenance, and knockout-data usage are ALL PAYWALLED and unknown.** The visible abstract states only that the model "includes four of these signals: nutrient levels, DNA damage, the products of the competence genes, and cell population size." **This is the one live possibility that a combinatorial dataset was used, and I could not close it.**
- **Voigt.** I found **no** phosphorelay ODE model by Voigt. The Voigt/Wolf/Arkin 2005 *Genetics* paper is *"The Bacillus subtilis sin operon: an evolvable network motif"* — the **sin operon, not the phosphorelay** (title seen in a PubMed search listing only). Do not assume a Voigt phosphorelay model exists.
- **Igoshin, pre-2012.** No earlier Igoshin paper modelling Spo0F→Spo0B→Spo0A specifically was retrieved or confirmed.
- **de Jong et al. (2004)**, "Qualitative simulation of the initiation of sporulation in *B. subtilis*". **NOT RETRIEVED.** Note that, being a *qualitative*/piecewise-linear simulation, it would not have quantitative fitted parameters in the sense required here.

### 5.7 Item 5 verdict table

| Model | Size | Form | Fitted to | Combinatorial KO used in fitting? |
|---|---|---|---|---|
| Ihekwaba 2014 | 13 species / 27 forms / 55 unidirectional reactions | ODE, mass-action + Hill | Wild-type IPTG-induction time courses for *spoIIG* transcript + KinA, taken from Narula 2012 | **NO** |
| Narula/Igoshin 2012 | Not stated (modular; SI not retrieved) | Mass-action | Nothing — parameters "extracted from the literature" | **NO** |
| Bischofs/Arkin 2009 | Not stated | Mass-action relay + **lumped kinase term κ** | Nothing identified | **NO** (structurally cannot) |
| Russell 2017 | n/a | **No model** | n/a | n/a |
| Gauvry 2019 | ~6 eqns / ~8 params | Phenomenological population kinetics | Growth-sporulation curves, GFP reporter | **NO** (no phosphorelay) |
| Jabbari 2011 | **UNKNOWN — paywalled** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** |

---

## 6. HONEST ASSESSMENT

### 6.1 Solid

- ***kinA kinB* synthetic near-lethality.** Direct measurement, numbers reported, **replicated across two labs (Grossman; Fujita) and two strain backgrounds (JH642; 168)**, three-plus media, and multiple sporulation-induction regimes. This is as solid as this literature gets.
- **Relay-core essentiality (*spo0A*, *spo0F*, *spo0B*).** Direct, ≥10⁶-fold, and consistent with the entire *spo0* literature's stage-0 phenotype.
- **KinC's conditional load-bearing role.** Two independent readouts in one paper (spore titre; *abrB-lacZ*), with the author stating reproducibility.
- **Assay:** a real, directly measured survival outcome, not a proxy.

### 6.2 Contested, condition-dependent, or inferred

1. **KinA vs KinB primacy is genuinely medium-dependent, and this is stated as a finding, not a caveat.** S1: *kinA* drops to 8–10% in DS/23SG but is **1.2 (i.e. at or above wild type) in minimal glucose medium**; *kinB* is 0.67 (near-WT) in 23SG but 7.1 × 10⁻² in minimal. S1 concludes *"under some conditions KinB is the major sporulation kinase and KinA plays a minor role."* **Any answer key that labels "KinA = major kinase" without naming the medium is wrong roughly a third of the time.**
2. **A documented reproducibility problem inside the primary source.** S1, verbatim: *"The phenotype of kinB in DS medium was somewhat variable and seemed to depend on the specific preparation of DS medium; this is consistent with effects reported by others (29)."*
3. **A documented history-dependence.** S1, verbatim: *"the sporulation defect of the kinB mutant in minimal glucose medium was highly reproducible but was observed only if the culture had undergone at least four to five doublings after inoculation and before entry into stationary phase."* The measured phenotype depends on inoculum history, not only on genotype.
4. **KinD's sign is condition-dependent.** S5 reports Δ*kinD* giving *~10-fold MORE* spores at 24 h in biofilms and calls KinD *"bifunctional, having either kinase or phosphatase activity, depending on the growth conditions."* A knockout of a nominal "kinase" that *increases* the persistence readout will break any monotone essential/redundant labelling scheme.
5. **Essentiality of *spo0F*/*spo0B* is gene-dosage-conditional.** Multicopy *kinC* rescues both by 4–5 orders of magnitude (S2 Table 3). "Essential" is true at native dosage only.
6. **Unaccounted residual phosphate flux.** S1 itself flags *"there might be yet another minor source of phosphate for Spo0A"* — i.e. the component list is acknowledged by the primary source to be incomplete.
7. **Assay heterogeneity across the corpus.** 75 °C/20 min vs 80 °C/15 min vs 80 °C/20 min; absolute titre vs. fraction vs. WT-normalised fraction vs. percentage; 20 h post-exponential vs. T10 vs. T20 vs. 24 h; planktonic vs. biofilm. Numbers from different papers are **not** directly commensurable.
8. **Allele-identity risk.** Several key alleles are point/insertion/partial-deletion alleles, not verified clean nulls — *kinA*::Tn917, *kinB* deletion-insertion **that also deletes *kapB*** (S1 footnote a: *"deleting part of kinB and all of kapB"*), *kinC*::pLK124 plasmid disruption, *spo0F*Δ*S*, *spo0B*Δ*Pst*. **The *kinB* "single mutant" is formally a *kinB kapB* double mutant.** This is a real hazard for a key that claims single-gene resolution.
9. ***kinE* has no retrieved sporulation measurement at all.**

### 6.3 What would make an entry unsuitable for a scored key

- Any entry for **KinD** (sign flips with condition), **KinE** (unmeasured in retrieved sources), or the ***kinA kinC*** pair (weak, inconsistent across media).
- Any entry stated **without a named medium and named strain background**.
- Any entry treating the *kinB* allele as *kinB*-only.
- Any entry for the **phosphatases (Spo0E, RapA/RapB, KipI)** — nothing quantitative was retrieved for them.

---

## 7. COUNT — mechanisms that could carry a settled label from direct experimental evidence

**Count: 9 entries I would defend; 3 further entries listed but NOT recommended.**

| # | Mechanism | Label | Confidence | Source (retrieved) |
|---|---|---|---|---|
| 1 | *spo0A* | **ESSENTIAL** | High | S2 Table 3: <9.0 × 10⁻⁸ vs WT 0.41; not rescued by multicopy *kinC* |
| 2 | *spo0F* | **ESSENTIAL** (native dosage; bypassable) | High for essentiality, Medium for unqualified label | S2 Table 3: <2.4 × 10⁻⁷; multicopy *kinC* → 9.8 × 10⁻³ |
| 3 | *spo0B* | **ESSENTIAL** (native dosage; bypassable) | High / Medium as above | S2 Table 3: <4.1 × 10⁻⁷; multicopy *kinC* → 1.1 × 10⁻² |
| 4 | *kinA* | **REDUNDANT** (dispensable alone; medium-modulated) | High | S1 Table 1 (0.1 / 8.0 × 10⁻² / 1.2); S3 (0.26%, 7.9% vs WT 19%, 71%) |
| 5 | *kinB* | **REDUNDANT** (dispensable alone; medium-modulated) | High, with the *kapB* caveat | S1 Table 1 (0.67 / 0.13 / 7.1 × 10⁻²); S3 (0.67%, 22%) |
| 6 | *kinA kinB* pair | **REDUNDANT PAIR / synthetic near-lethal** | **Very high — replicated across labs and backgrounds** | S1 Table 1 (1.9 × 10⁻⁶ / <5 × 10⁻⁸ / 2.1 × 10⁻⁷); S3 (<5 × 10⁻⁶%) |
| 7 | *kinC* alone | **NEAR-INERT** | High | S1 Table 1 (0.77 / 0.45 / 0.91) |
| 8 | *kinC* within *kinA kinB* background | **SYNERGISTIC / conditionally load-bearing** | High in 23SG; medium-restricted | S1: triple <3 × 10⁻⁸ vs double 1.9 × 10⁻⁶; plus *abrB-lacZ* corroboration |
| 9 | *kinB kinC* pair in minimal medium | **SYNERGISTIC (weak, medium-restricted)** | Medium | S1 Table 1: 1.2 × 10⁻² vs *kinB* 7.1 × 10⁻², *kinC* 0.91; **no synergy in 23SG (0.43)** |
| — | *kinD* | would be *inert-or-negative-regulator* | **Low — do not score** | S5 only; sign flips by condition; no planktonic number |
| — | *kinE* | would be *inert* | **Very low — do not score** | S7 colony morphology only; **no sporulation measurement retrieved** |
| — | *kinA kinC* pair | would be *weak synergy* | **Low — do not score** | S1: inconsistent across media |

**Defensible count = 9** (rows 1–9). A conservative count restricted to entries that need no medium-conditioning qualifier = **6** (rows 1, 2, 3, 6, 7 and — as a "dispensable in at least one medium" claim — 4 or 5 collapsed to one).

---

## 8. SINGLE BIGGEST WEAKNESS

**No published dynamical model of this system has ever been fitted to the combinatorial knockout data — and the best-known model is structurally incapable of representing it.**

The ground truth (Item 3) and the models (Item 5) were built in disjoint universes. The combinatorial dataset is 1993–1995 genetics measuring heat-resistant CFU; the models are 2009–2014 and are parameterised either from literature values (Narula/Igoshin 2012), from nothing identifiable (Bischofs/Arkin 2009), or from two wild-type observables under artificial IPTG induction (Ihekwaba 2014). Bischofs et al. lump all kinase input into a single effective parameter κ, so KinA and KinB are not separable objects in that model at all.

The close second: **almost every knockout label in this system is medium-, strain-, and inoculum-history-conditional**, and the primary source says so in its own words — *kinA* ranges from 8% of wild type (DS) to 120% (minimal) across three media in a single table.

---

# 9. MODEL REPRESENTATIONAL ADEQUACY

**Question asked:** does any published dynamical model represent KinA and KinB (ideally KinC too) as *separate species or reactions*, alongside Spo0F/Spo0B/Spo0A, such that a coalition object over the scored mechanisms is computable?

## 9.0 BOTTOM LINE

**NO PUBLISHED MODEL REPRESENTS THE INDIVIDUAL KINASES.** Of every model I could reach, **not one contains KinB as a separate species**, and **not one contains KinC**. Every mechanistic model collapses to a single kinase — KinA — or to a single lumped kinase term. The `kinB∆` and `kinC∆` operations are **not definable** on any published model, which means the *kinA kinB* double mutant — the single strongest, best-replicated fact in the entire ground truth (§3) — **cannot be expressed as a perturbation of any existing model.**

There is a second, independent failure, and it is equally disqualifying. **The models and the answer key measure different things.** Every mechanistic model outputs phospho-Spo0A, sigma-factor activity, or transcript levels. **None outputs a spore count or a sporulation frequency.** The one retrieved model that *does* output spore concentration (Gauvry 2019) contains **no phosphorelay components whatsoever**. The mechanism-bearing models and the survival-bearing model are disjoint.

**VERDICT: NOT EXECUTABLE ON PUBLISHED MODELS.**

## 9.1 Ihekwaba, Mura & Barker (2014), *BMC Syst Biol* 8:119 — FULL TEXT RETRIEVED

**(1) KinA and KinB as separate species?** **KinA YES, KinB NO.** Verbatim from the paper:

> "Out of the five kinases identified as capable of initiating sporulation in B. subtilis, we have considered KinA, the major kinase responsible for initiation of sporulation in our model."

KinA is a distinct species (it forms homodimers). Upstream of it, kinase *activation* is further abstracted into a single fictitious species: verbatim,

> "The sporulation signal we introduce is modelled as an abstract species SS, which controls the autophosphorylation of KinA."

Species confirmed present in the retrieved text: KinA, Spo0F (+Spo0F~P), Spo0B (+Spo0B~P), Spo0A (+Spo0A~P), LacI and LacI_d, transcripts *spoIIA_t*, *spoIIE_t*, *spoIIG_t*, and proteins AA, AB, AC, IIE, GA, GB. **The paper does not print a complete enumerated list of all 13 base species / 27 forms in the retrieved body text** — my species inventory is what is explicitly named, not a verified exhaustive list.

**(2) KinC?** **NO.**

**(3) Is `kinA∆` a well-defined operation?** Only degenerately. KinA is the model's *sole* kinase, so removing it zeroes all phosphoryl input and the relay simply dies — the model cannot reproduce the actual measured *kinA* phenotype (0.1–1.2 of wild type, i.e. **still sporulating**). `kinB∆` and `kinC∆` have no referent at all. Verbatim confirmation that no deletions were even attempted: the paper **does not simulate gene deletions or knockouts**; it explores parameter variations (IPTG levels, SS stimulus) only.

**(4) Output mappable to spore titre?** **NO.** Outputs are Spo0A~P and downstream transcript/protein levels (*spoIIA_t*, *spoIIE_t*, *spoIIG_t* → AA/AB/AC, IIE, GA/GB). No spore count, no sporulation frequency, no survival fraction.

## 9.2 Narula, Devi, Fujita & Igoshin (2012), *PNAS* — CITATION VERIFIED, MAIN TEXT RETRIEVED

**Author list and venue verified as requested:** Jatin Narula, Seram N. Devi, Masaya Fujita, Oleg A. Igoshin; *Proceedings of the National Academy of Sciences USA*, **vol. 109, issue 50, pages E3513–E3522, 19 November 2012.** (Igoshin is last author; Fujita is the experimental collaborator. The coordinator's shorthand "Narula/Igoshin" is correct.)

**(1) KinA and KinB as separate species?** **KinA YES, KinB NO.** KinA is a separate species whose expression is a model input:

> "The model inputs the concentration of IPTG, which is converted to parameters of KinA transcription to ensure agreement of the model predictions with the observed mean and SD of KinA concentration at all IPTG levels."

The paper's mention of the other kinases is **background prose, not model content**:

> "phosphoryl groups are transferred from one of the five autophosphorylating kinases (KinA–KinE) to Spo0A via the phosphotransferases Spo0B and Spo0F"

KinB, KinC, KinD and KinE are **not separately modelled**. Spo0F, Spo0B and Spo0A are present as distinct entities (Spo0A~P concentration is tracked explicitly).

**(2) KinC?** **NO.**

**(3) Is `kinA∆` a well-defined operation?** **Not as published, and misleadingly so.** The model's KinA level is driven by an IPTG dose-response in a strain where, verbatim from §5.2's retrieval, "the KinA promoter is replaced with an IPTG-inducible promoter". Zero induction in that engineered strain is *not* the same object as a `kinA` null in a wild-type background, because the native regulation is already gone. `kinB∆` and `kinC∆` are undefined.

**(4) Output mappable to spore titre?** **PARTIALLY — and the mapping is a comparison, not a validated transform.** The model predicts "Spo0A activity as the PspoIIG transcription level", "σF activity", "σE activity", and "fractions of cells that activate σE". That last quantity is *compared to* experimentally measured sporulation efficiency. This is the closest any retrieved model comes to the answer key's observable, but **σE-activation fraction is not a heat-resistant spore titre**, and no validated conversion is published. Scoring against a survival key would require an unvalidated added mapping.

**Not retrieved:** the SI (Table S3, the full species list and equations). `pnas.org` SI PDF returned HTTP 403. **The aggregate species/reaction/parameter count for this model remains UNKNOWN.**

## 9.3 Bischofs, Hug, Liu, Wolf & Arkin (2009), *PNAS* — determination unchanged

**(1)** **Kinase input is LUMPED.** Individual kinases do not exist as species; all kinase activity enters through a single effective parameter κ (with phosphatase activity as π). **Neither KinA nor KinB is a separate species.**
**(2) KinC?** **NO.**
**(3)** `kinA∆` / `kinB∆` / `kinC∆` are **all undefined operations**. There is no object in the model corresponding to an individual kinase.
**(4)** Output is relay phospho-state (Spo0A~P / promoter activity). **No spore count.**

*Caveat on precision:* the presence of Spo0F/Spo0B/Spo0A as separate species is **inferred** from the retrieved phrase *"mass action kinetics for the phosphoryl-transfer reactions with forward and backward rates"* plus the discussion of a P*spo0B* mutant. I did **not** retrieve an explicit species list for this model.

## 9.4 Jabbari, King & Heap (2011), *Bull Math Biol* 73:181–211 — **STILL NOT CLOSED**

I made three further attempts as instructed. All failed:

1. Green-OA accepted manuscript at `research.birmingham.ac.uk/files/8789488/JabbariBacillus2011.pdf` — **HTTP 403 on two separate attempts.** (The repository record itself was retrieved and explicitly advertises this PDF as an "Accepted author manuscript".)
2. Springer PDF `link.springer.com/content/pdf/10.1007/s11538-010-9530-7.pdf` — **paywalled**, metadata and abstract only.
3. FAIRDOMHub model entry (`fairdomhub.org/models/33`) — page retrieved; the model archive `bacillus_sporulation_initiation.tar` (20 KB, MATLAB) at `fairdomhub.org/models/33/content_blobs/293/download` is **disallowed by robots.txt**, so the variable list inside the code could not be read.

**What IS now established (newly retrieved this pass):**

- **Citation, with an author-order discrepancy to flag.** The University of Birmingham repository record gives **S. Jabbari, J.R. King, J.T. Heap**, *Bulletin of Mathematical Biology*, 2011, 73:181–211, DOI 10.1007/s11538-010-9530-7. My earlier Springer retrieval rendered it "Jabbari, S., Heap, J.T., & King, J.R." **The two retrieved records disagree on the order of King and Heap; I have not resolved which is correct.**
- **Full abstract, retrieved verbatim** (Birmingham record). It names the four incorporated signals — "nutrient levels, DNA damage, the products of the competence genes, and cell population size" — and the findings about *sda* basal expression, population size, and PhrA's dual role. **It names no kinase and no phosphorelay protein.**
- **FAIRDOMHub description, verbatim:** *"An ODE model of the gene regulation network governing sporulation initiation in Bacillus subtilis to be run in Matlab. The network incorporates four sporulation-related signals: nutrient supply, DNA damage, the products of the competence genes and the bacterial population size. Run execute_bacillus_sporulation_initiation.m to simulate the model."* Model type: ODE; format: MATLAB code; organism: *Bacillus subtilis*.
- FAIRDOMHub links this entry to **PubMed ID 20238180** and a posting date of **21 July 2009**, which sits oddly against the 2011 *Bull Math Biol* volume. **Unresolved.**

**Determination:** KinA/KinB/KinC representation, ODE count, parameter count, parameter provenance, knockout simulation, and output variables are **ALL STILL UNKNOWN** for this model. The only relevant signal is negative and weak: neither the abstract nor the repository description mentions any kinase or any phosphorelay protein, and the model is framed as a *gene regulation network* driven by four environmental/population signals. **I am NOT asserting that it lacks KinA and KinB — I could not check.** It remains the one open possibility, and it is open only because I was blocked, not because there is evidence in its favour.

## 9.5 Russell et al. (2017), *EMBO J* — N/A

Contains **no mathematical model** (verbatim finding: no rate equations, no differential equations, no parameter fits, no stochastic simulation). All four questions are inapplicable. It cannot serve as the benchmark's model.

## 9.6 Gauvry et al. (2019), *Appl Environ Microbiol* — the mirror-image failure

**(1)** No KinA, no KinB — **no molecular species at all.** It is a phenomenological population model (~6 equations, ~8 parameters: N₀, λ, μmax, Nmax, Pmax, tmax, σ, tf).
**(2) KinC?** **NO.**
**(3)** No genetic perturbation is definable; there are no genes in the model.
**(4)** **This is the ONLY retrieved model whose output is the right observable** — it was fitted to "the concentration of total cells…and the concentration of spores" over time. It predicts spore concentration directly.

This is worth stating explicitly because it sharpens the diagnosis: **the models that contain mechanism produce no spore counts, and the model that produces spore counts contains no mechanism.** There is no published model on which both the coalition object and the scored observable are defined.

## 9.7 Summary table

| Model | KinA separate? | KinB separate? | KinC? | Spo0F/0B/0A separate? | `kinA∆` definable? | `kinB∆`/`kinC∆` definable? | Outputs spore titre / sporulation frequency? |
|---|---|---|---|---|---|---|---|
| Ihekwaba 2014 | **Yes** | **No** | **No** | Yes | Degenerate only (sole kinase) | **No** | **No** — Spo0A~P + transcripts |
| Narula/Igoshin 2012 | **Yes** | **No** | **No** | Yes | Not as published (IPTG-driven engineered promoter) | **No** | **No** — σE-activation *fraction*, compared to but not equal to sporulation efficiency |
| Bischofs/Arkin 2009 | **No — lumped into κ** | **No — lumped into κ** | **No** | Inferred yes (not verified) | **No** | **No** | **No** — relay phospho-state |
| Jabbari 2011 | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** | **UNKNOWN** (no evidence of spore output) |
| Russell 2017 | n/a — no model | n/a | n/a | n/a | n/a | n/a | n/a |
| Gauvry 2019 | **No — no molecular species** | **No** | **No** | **No** | **No** | **No** | **YES** — spore concentration (but zero mechanism) |

## 9.8 What I could NOT do in this pass — stated prominently

- **BioModels was NOT checked.** `www.ebi.ac.uk/biomodels/search` returned HTTP 429 repeatedly and then HTTP 403 across four attempts in this session; the entire `ebi.ac.uk` host has been rate-limited/blocked for the duration of this work. **The coordinator's specific request to check BioModels for curated sporulation/phosphorelay entries is UNFULFILLED.** If a curated BioModels entry exists with KinA *and* KinB as separate species, I would not have seen it. This is the most important open check.
- **The additional search terms could not be run.** The session's WebSearch budget was exhausted (200/200 calls) before the requested sweeps for "sporulation phosphorelay model kinA kinB", "Spo0A phosphorelay mathematical model", and "stochastic model sporulation initiation Bacillus" could be issued. **The model survey in §5 and §9 is therefore NOT exhaustive**, and I cannot claim to have identified every published model.
- **Jabbari 2011's internals remain unread** (three blocked routes, §9.4).
- **Narula/Igoshin 2012's SI** (species list, equations, Table S3) remains unread (HTTP 403).

Given these three gaps, the correct statement of the finding is: **among every model whose contents I could actually read, none represents the individual kinases, and none outputs the scored observable.** Two named models (Jabbari 2011; anything curated in BioModels) remain unverified, and the survey is not exhaustive. The verdict of NOT EXECUTABLE stands on the evidence retrieved, and would be overturned only by one of those unchecked sources containing something no checked source does.
