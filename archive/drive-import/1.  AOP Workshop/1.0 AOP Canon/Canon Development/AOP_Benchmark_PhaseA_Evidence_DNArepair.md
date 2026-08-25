# Benchmark Candidate Due Diligence: *E. coli* DNA Damage Repair / SOS Response, scored by UV survival

**Compiled:** 2026-07-25
**Provenance discipline:** strict. No citation, figure number, quantity, or quotation below is fabricated. Every number is traceable to a quoted passage actually retrieved, or is explicitly flagged as *derived*, *inferred*, or *contested*. Sources seen only as abstracts are marked **ABSTRACT ONLY**; sources not obtained are marked **NOT RETRIEVED**; PMC deposits that are page scans without a machine-readable text layer are marked **SCANNED, NO TEXT LAYER**.

---

## 0. RETRIEVAL CONDITIONS AND METHOD CAVEATS — READ FIRST

**Tooling.** The Nimble CLI was **not present** in this environment (`nimble: command not found`), so paywalled and JS-heavy pages could not be reached. All retrieval used `WebSearch` + `WebFetch`. `curl`/`wget`/`python` fetching was prohibited and not used.

**A systematic limitation that affects every quote in this document.** `WebFetch` renders pages through a summarizing model. I did not see raw HTML or raw PDF text for any source. Consequences:

- **Positive findings** (a passage exists and reads thus) are reasonably reliable, and load-bearing ones below were re-fetched on a second pass or a second endpoint.
- **Negative findings** ("the paper contains no survival data") are *weaker* — they are a summarizer's failure to surface a term, not a verified full-text search. Every negative below is flagged as such.
- **The summarizer was observed to silently paraphrase, and in at least three instances to wrap its own prose in quotation marks.** All such output was discarded. Load-bearing quotes were cross-checked.

**Nothing in this document meets a strict "verified against the primary source by a human reading the paper" bar.** The realistic grade for the best items here is *"verified against publisher-served abstract or OA full text, on two independent retrievals."* Several classical items do not even meet that.

**Infrastructure failures encountered, repeatedly:**
- `pmc.ncbi.nlm.nih.gov` served a Google reCAPTCHA on the majority of attempts.
- Europe PMC REST returned HTTP 429 on essentially every attempt; `europepmc.org` article pages are robots-disallowed.
- `sciencedirect.com`, `eutils.ncbi.nlm.nih.gov`, `api.openalex.org`, PMC full-text search, and `cshperspectives.cshlp.org` are robots-disallowed.
- `pnas.org`, `jbc.org`, `pubs.acs.org`, `onlinelibrary.wiley.com` returned 403.
- `journals.plos.org` returned **silently wrong article content** on three requests (two different DOIs returned the same unrelated paper). Nothing in this report is sourced from the PLOS site.
- The session `WebSearch` budget (200 calls) was exhausted; the last portion of the work was direct-URL construction only.

**One access route that worked and should be reused:** the NCBI BioC REST API bypasses the PMC reCAPTCHA —
`https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC<ID>/unicode`
`https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pubmed.cgi/BioC_json/<PMID>/unicode`
Limitation: PMC Open Access subset only; it does not serve table bodies.

**Verification tiers used below:**
- **[V2]** — retrieved through two independent endpoints or re-verified on a second pass. Highest confidence available here.
- **[V1]** — single retrieval, read directly.
- **[PR]** — paraphrase risk; treat as provisional.

---

## ITEM 1 — CAUSAL STRUCTURE (published pathway architecture)

**Retrieval status: GOOD for mechanism, MIXED for primary sources.** Most of the load-bearing statements were obtained from OA reviews and from Sancar's Nobel lecture; several canonical primary papers (Sancar & Rupp 1983 *Cell*; Walker 1984 *Microbiol Rev*; Little & Mount 1982 *Cell*) were **NOT RETRIEVED**.

### 1A. Nucleotide excision repair — uvrA, uvrB, uvrC (+ uvrD, polA)

> "I invented the maxicell method to specifically radiolabel plasmid-encoded proteins [48], which enabled me to identify and clone the three genes implicated in excision repair: uvrA, uvrB, and uvrC [49–51]. ... I found that the UvrA, B, C proteins repaired DNA by a mechanism different from the classic endonuclease/exonuclease (cut-and-paste) model: The three proteins instead act together to carry out concerted dual incisions at precise distances from the photoproduct [52], seven nucleotides 5' and three nucleotides 3' from the damage to generate a dodecamer (12-mer) carrying the T<>T photoproduct."

— Sancar A, "Mechanisms of DNA Repair by Photolyase and Excision Nuclease" (Nobel Lecture, 8 Dec 2015), p. 141. FULL TEXT. https://www.nobelprize.org/uploads/2018/06/sancar-lecture.pdf **[V1] [PR on incidental wording]**

> "UvrB forms a tight scaffold on the DNA for the arrival of UvrC, which contains two nuclease domains that cleave the phosphodiester bonds 8 nucleotides 5′ and 4–5 nucleotides 3′ to the damaged site. ... The postincision complex is displaced by the dual action of UvrD (helicase II) and DNA polymerase I (Pol I) that together work to excise the damage-containing oligonucleotide and allow turnover of the UvrB and UvrC proteins while filling in the resulting gap using the remaining complementary strand (Caron et al. 1985; Husain et al. 1985). The final step is achieved by the action of DNA ligase, which seals the newly created repair patch (Fig. 1)."

> "UV light induces two major photoproducts in DNA: a cyclobutane pyrimidine dimer and a 6-4 photoproduct at a ratio of 3:1 that are repaired by two evolutionarily conserved processes called photoreactivation and NER."

— Kisker C, Kuper J, Van Houten B. "Prokaryotic Nucleotide Excision Repair." *Cold Spring Harb Perspect Biol.* 2013;5(3):a012591. FULL TEXT. https://pmc.ncbi.nlm.nih.gov/articles/PMC3578354 **[V2]**

> "The UvrABC-excinuclease (consisting of UvrA, UvrB and UvrC proteins) was known to be involved in nucleotide excision repair (NER) which removes bulky adducts or structure-affecting lesions (e.g., pyrimidine dimers, pyrimidine (6-4) photoproducts, and abasic sites) from modified DNA."

— Janion C. "Inducible SOS Response System of DNA Repair and Mutagenesis in *Escherichia coli*." *Int J Biol Sci.* 2008;4(6):338–344. FULL TEXT. https://www.ijbs.com/v04p0338.htm **[V1]**

**Discrepancy, not smoothed over:** Sancar gives incision offsets as 7 nt 5′ / 3 nt 3′ (counting nucleotides); Kisker et al. give 8 nt 5′ / 4–5 nt 3′ (counting phosphodiester bonds). Both yield a 12–13-mer. The Nobel lecture is internally inconsistent between its body text ("three nucleotides 3′") and Fig. 10 caption ("3–4 nucleotides 3′"). **Do not report a single canonical offset.**

**NOT RETRIEVED:** Sancar A & Rupp WD (1983) *Cell* 33:249–260, "A novel repair enzyme: UVRABC excision nuclease of *Escherichia coli* cuts a DNA strand on both sides of the damaged region." Title verified verbatim from two independent reference lists; the paper itself was not obtained. Also NOT RETRIEVED: Van Houten B, *Microbiol Rev* 1990;54:18–51; Truglio et al. *Chem Rev* 2006; Goosen & Moolenaar 2008.

### 1B. Recombinational / postreplication repair — recA, recBCD, recFOR

> "The two major types of two-strand DNA lesions are channeled into two distinct pathways of recombinational repair: daughter-strand gaps are closed by the RecF pathway, while disintegrated replication forks are reestablished by the RecBCD pathway."

— Kuzminov A. "Recombinational Repair of DNA Damage in *Escherichia coli* and Bacteriophage λ." *Microbiol Mol Biol Rev.* 1999;63(4):751–813. **ABSTRACT ONLY** — the ASM site serves only front matter and references; the PMC copy was reCAPTCHA-blocked; not in the BioC OA subset. https://journals.asm.org/doi/full/10.1128/mmbr.63.4.751-813.1999 **[V2 — identical across two fetches]**

> "In *Escherichia coli*, the presynaptic phase involves either RecBCD or RecFOR proteins, which act on DNA double-stranded ends and DNA single-stranded gaps, respectively; the central synaptic steps are catalyzed by the ubiquitous DNA-binding protein RecA; and the postsynaptic phase involves either RuvABC or RecG proteins, which catalyze branch-migration and, in the case of RuvABC, the cleavage of Holliday junctions."

— Michel B, Leach D. "Homologous Recombination—Enzymes and Pathways." *EcoSal Plus.* 2012;5(1). PMID 26442826. **ABSTRACT ONLY** **[V1]**

> "*Escherichia coli* RecA is the defining member of an ancient and ubiquitous clade of DNA strand exchange proteins that are essential for homologous recombination."
> "The ATP-bound nucleoprotein filament serves as a surface catalyst for the search and capture of a homologous sequence of DNA, a process known as synapsis. Once a region of homology is found, the ssDNA strands on the homologous chromosomes are exchanged, producing heteroduplex DNA."

— Bell JC, Kowalczykowski SC. "RecA: Regulation and Mechanism of a Molecular Search Engine." *Trends Biochem Sci.* 2016;41(6):491–507. PMC4892382. FULL TEXT via BioC. **[V1]**

**Note the framing shift.** Michel & Leach describe RecBCD and RecFOR as *presynaptic phases* acting on different substrates — not as free-standing parallel pathways. See Item 7F below; this is load-bearing for whether an epistasis-group answer key built on the classical scheme is still current.

### 1C. Translesion synthesis — umuDC (Pol V), dinB (Pol IV), polB (Pol II)

> "The damage-inducible UmuD' and UmuC proteins are required for most SOS mutagenesis in *Escherichia coli*. Our recent assay to reconstitute this process in vitro, using a native UmuD'(2)C complex, revealed that the highly purified preparation contained DNA polymerase activity. Here we eliminate the possibility that this activity is caused by a contaminating DNA polymerase and show that it is intrinsic to UmuD'(2)C. *E. coli* dinB has recently been shown to have DNA polymerase activity (pol IV). We suggest that UmuD'(2)C, the fifth DNA polymerase discovered in *E. coli*, be designated as *E. coli* pol V."

— Tang M, Shen X, Frank EG, O'Donnell M, Woodgate R, Goodman MF. *PNAS* 1999;96(16):8919–24. PMID 10430871. **ABSTRACT ONLY** **[V2]**

> "In *Escherichia coli*, the dinB gene is required for the SOS-induced lambda untargeted mutagenesis pathway and confers a mutator phenotype to the cell when the gene product is overexpressed. Here, we report that the purified DinB protein is a DNA polymerase. This novel *E. coli* DNA polymerase (pol IV) is shown to be strictly distributive, devoid of proofreading activity, and prone to elongate bulged (misaligned) primer/template structures."

— Wagner J, Gruz P, Kim SR, Yamada M, Matsui K, Fuchs RP, Nohmi T. *Mol Cell* 1999;4(2):281–6. PMID 10488344. **ABSTRACT ONLY** **[V1]**

> "*Escherichia coli* DNA polymerase II (Pol II) is a member of the group B, "alpha-like" family of DNA polymerases. Pol II is encoded by the damage-inducible dinA gene and exhibits SOS induction under the control of Lex A repressor."
> "Our sequence data reveal that polB and dinA represent the same gene and that the original transduction mapping of polB was inaccurate."

— Qiu Z, Goodman MF. *J Biol Chem* 1997;272(13):8611–7. PMID 9079692. **ABSTRACT ONLY** **[V1]**

> "In *Escherichia coli*, only Pol V (umuDC) was known to be essential for base substitution mutagenesis induced by UV light or abasic sites. Here we show that, depending upon the nature of the DNA damage and its sequence context, the two additional SOS-inducible DNA polymerases, Pol II (polB) and Pol IV (dinB), are also involved in error-free and mutagenic translesion synthesis (TLS)."

— Napolitano R, Janel-Bintz R, Wagner J, Fuchs RP. *EMBO J* 2000;19(22):6259–65. PMID 11080171. **ABSTRACT ONLY** **[V1]**

**Later refinement:** Jiang Q, Karata K, Woodgate R, Cox MM, Goodman MF, *Nature* 2009;460:359–63 — title verified verbatim: **"The active form of DNA polymerase V is UmuD'(2)C-RecA-ATP"**. The in vivo active species includes RecA and ATP.

**GAPS:** no retrieved sentence spells out "*two* molecules of UmuD′" — the stoichiometry rides entirely on the `UmuD'(2)C` notation. No verbatim sentence obtained for the classic result that *umuDC* mutants are **non-mutable** by UV (Kato & Shinoura 1977 — **NOT RETRIEVED**).

### 1D. The SOS regulatory circuit — LexA repressor, RecA coprotease, autocleavage

**LexA is the repressor; "SOS boxes"; and lexA/recA autoregulation, all in one passage:**

> "We show here that lexA protein is a repressor of at least two genes, recA and lexA. Purified protein bound specifically to the regulatory regions of the two genes, as judged by DNase I protection experiments, and it specifically inhibited in vitro transcription of both genes. ... These 20-bp sequences, which we term "SOS boxes," show considerable inverted repeat structure as well."

— Little JW, Mount DW, Yanisch-Perron CR. "Purified lexA protein is a repressor of the recA and lexA genes." *PNAS* 1981;78(7):4199–4203. **ABSTRACT ONLY** (raw publisher JATS via Crossref) **[V1]**

> "Experiments with this fusion phage and with multicopy plasmids that carry the lexA gene showed that the lexA gene product represses of its own promoter. This repression occurs even if the cell has no recA gene..."

— Brent R, Ptashne M. "The lexA gene product represses its own promoter." *PNAS* 1980;77(4):1932–1936. **ABSTRACT ONLY** **[V1]**. (The "represses **of** its own promoter" is as deposited; `[sic]`.)

> "LexA acts as a transcriptional repressor of these unlinked genes by binding to specific sequences (LexA boxes) located within the promoter region of each LexA-regulated gene. Alignment of 20 LexA binding sites found in the *E. coli* chromosome reveals a consensus of 5'-TACTG(TA)5CAGTA-3'."

— Fernández de Henestrosa AR et al. *Mol Microbiol* 2000;35(6):1560–72. PMID 10760155. **ABSTRACT ONLY** **[V2]**

**The coprotease / autocleavage distinction — this is the mechanistically decisive item and it was obtained cleanly:**

> "I show here that, under certain conditions, specific in vitro cleavage of highly-purified lexA protein can take place in the absence of recA protein. This autodigestion reaction cleaved the same alanine-glycine bond as did the recA-dependent cleavage reaction. ... The reaction appeared to be first-order, and its rate was independent of protein concentration over a wide range, strongly suggesting that it is intramolecular. ... These findings indicate that specific cleavage of lexA protein can be catalyzed by the protein itself and suggest that recA protein plays an indirect stimulatory role, perhaps as an allosteric effector, in the recA-dependent reaction, rather than acting directly as a protease."

— Little JW. "Autodigestion of lexA and phage lambda repressors." *PNAS* 1984;81(5):1375–1379. PMID 6231641. **ABSTRACT ONLY**, but **[V2 — character-identical across NCBI BioC and Crossref JATS]**

> "Specific LexA cleavage can occur under two different conditions: RecA-mediated cleavage requires an activated form of RecA, while an intramolecular self-cleavage termed autodigestion proceeds spontaneously at high pH and does not involve RecA. The two cleavage reactions are closely related. We postulate that RecA stimulates autodigestion rather than acting as a typical protease, and it is proposed to term this activity 'RecA coprotease' to emphasize this indirect role. The mechanism of autodigestion is similar to that of a serine protease, and RecA appears to act by reducing the pKa of a critical lysine residue LexA."

— Little JW. "Mechanism of specific LexA cleavage: autodigestion and the role of RecA coprotease." *Biochimie* 1991;73(4):411–421. PMID 1911941. **ABSTRACT ONLY** **[V2 — two URL formats returned character-identical text]**

> "This autodigestion reaction is intramolecular: it displays first-order kinetics, and its rate constant is independent of protein concentration. This behavior is one of the hallmarks of self-processing reactions. Autodigestion cuts the same bond as is cleaved in RecA-mediated cleavage. Several mutant proteins that are resistant to RecA-mediated cleavage also cannot autodigest. These and many other findings suggest that RecA stimulates repressor self-cleavage, rather than acting directly as a protease, and hence we term it a coprotease (25)."

— Little JW. "LexA cleavage and other self-processing reactions." *J Bacteriol* 1993;175(16):4943–4950. **FULL TEXT** (PDF text layer). https://journals.asm.org/doi/pdf/10.1128/jb.175.16.4943-4950.1993 **[V1]**

**RecA activation by ssDNA (the RecA* half):**

> "Although the central biochemical event in induction, activation of RecA protein through binding of single-stranded DNA and ATP to promote cleavage of the LexA repressor, is known, the cellular event that provides this activation following DNA damage has not been well understood."

— Sassanfar M, Roberts JW. *J Mol Biol* 1990;212(1):79–96. PMID 2108251. **ABSTRACT ONLY** **[V1]**

**Structural mechanism:**
> "We suggest RecA activates the self-cleavage of LexA and related proteins through selective stabilization of the cleavable conformation."
— Luo Y et al. "Crystal structure of LexA: a conformational switch for regulation of self-cleavage." *Cell* 2001;106(5):585–594. PMID 11551506. **ABSTRACT ONLY** **[V1]**

**Size of the LexA regulon — four different numbers in four different units. DO NOT COLLAPSE THESE.**

| Number | Source | Unit / basis |
|---|---|---|
| **31** genes | Fernández de Henestrosa et al. 2000 | Northern-verified, from 69 computational candidates |
| **26 + 17** | Courcelle et al. 2001 | chromosomal *regions/sites*, **not genes** |
| **~43** genes | Janion 2008 | derived as 26+17 from Courcelle — **not an independent count** |
| **57** genes | Simmons et al. 2008 | most inclusive verified tally |

> "These searches identified a total of 69 potential LexA-regulated genes/operons with a heterology index of <15 and included all previously characterized LexA-regulated genes. ... These experiments have allowed us to identify seven new LexA-regulated genes, thus bringing the present number of genes in the *E. coli* LexA regulon to 31."
— Fernández de Henestrosa et al. 2000, PMID 10760155. **ABSTRACT ONLY** **[V2]**

> "We report here the time courses of expression of the genes surrounding the 26 documented lexA-regulated regions on the *E. coli* chromosome." / "We observed 17 additional sites that responded in a lexA-dependent manner..."
— Courcelle J, Khodursky A, Peter B, Brown PO, Hanawalt PC. *Genetics* 2001;158(1):41–64. PMID 11333217. **ABSTRACT ONLY**; the PMC deposit is **SCANNED, NO TEXT LAYER**. **The identities of the 26 regions and 17 additional sites were never obtained.**

> "We also provide a comprehensive summary (Table 1) of all the genes known to be LexA regulated bringing the total number 57."
— Simmons LA, Foti JJ, Cohen SE, Walker GC. "The SOS Regulatory Network." *EcoSal Plus* 2008. PMC4196698. **FULL TEXT** **[V2]**. (Sentence is ungrammatical in the source; reproduced as printed.)

**Regulon membership (Simmons et al. 2008, Table 1, "LexA-dependent genes"), verified by two independent fetches:**

| Gene | Status in source |
|---|---|
| uvrA (dinE) | LexA-dependent — "Involved in nucleotide excision repair" |
| uvrB | LexA-dependent |
| uvrD | LexA-dependent — "DNA helicase II" |
| recA | LexA-dependent |
| lexA | LexA-dependent — "Transcriptional repressor of SOS genes" |
| recN | LexA-dependent — "Involved in recombinational repair" |
| ruvAB | LexA-dependent (listed as a **single row**, not separately) |
| umuCD | LexA-dependent — "DNA pol V involved in SOS mutagenesis and translesion DNA synthesis" (source writes *umuCD*) |
| polB (dinA) | LexA-dependent |
| dinB (dinP) | LexA-dependent |
| sulA | LexA-dependent — "Inhibitor of cell division" |
| **uvrC** | **ABSENT from the entire document** |
| **recF** | **OMITTED from both Table 1 sections and Table 2**; appears in body text as mechanism only |

**The uvrC subtlety, stated explicitly by a source:**
> "The *uvrA*, *uvrB*, and *ydjQ* (but not *uvrC*) genes are SOS-induced genes."
— Janion 2008. **FULL TEXT** **[V2]**. Independently corroborated: the string "uvrC" does not appear anywhere in Simmons et al. 2008 (verified via BioC full text), while uvrA, uvrB, uvrD and ydjQ are all listed.

**The recF subtlety — NOT RESOLVED.** No retrieved source states recF's regulon status either way. The honest write-up is **"omitted from the list"**, not "stated not to be regulated." Relevant but non-probative: *dnaN*, recF's operon partner, **is** listed by Simmons — under **LexA-independent genes**.

### 1E. Photoreactivation as a distinct light-dependent pathway

> "UV converts two adjacent pyrimidines, including thymines, to a CPD (cyclobutane pyrimidine dimer), and there is an enzyme called photolyase that uses blue light energy to break the two abnormal bonds joining the thymines and thus converts the thymine dimer to two canonical thymines."
> "The catalytic reaction is initiated by absorption of a photon (300–500 nm) by the folate (MTHF)."
> "In light-exposed cells, the T<>Ts completely disappeared as expected. In contrast, in cells kept in the dark, even though the T<>Ts disappeared from the genomic DNA, they accumulated quantitatively in the cytosol [36–38]."

— Sancar Nobel Lecture, pp. 142, 145, 147. **FULL TEXT** **[V2]**

> "This protein binds specifically to UV (254 nm) irradiated DNA and upon exposure to near UV (300–500 nm) illumination repairs the UV damage and dissociates from DNA."
— Sancar GB, Smith FW, Sancar A. "Identification and amplification of the *E. coli phr* gene product." *Nucleic Acids Res.* 1983;11(19):6667–6678. PMID 6314252. **ABSTRACT ONLY** (PMC326406 is **SCANNED, NO TEXT LAYER**).

**Nomenclature warning:** the designation **"phrB" was NOT found verbatim in any retrieved source.** Retrieved literature supports "*phr*" only. The *phr* → *phrB* synonymy is *inferred*, not sourced.

**Also NOT SOURCED:** no retrieved source states "E. coli lacks (6-4) photolyase." Closest verified claim (Todo et al., *Science* 1996;272:109–12, **ABSTRACT ONLY**): "the (6-4)photolyase has been found only in *Drosophila melanogaster*."

---

## ITEM 2 — THE EPISTASIS-GROUP METHOD ITSELF ★ THE CRITICAL ITEM

**Retrieval status: SUCCESSFUL. This is the strongest single result of the whole exercise.** I obtained the field's own operational definition from two independent sources, one of which states the full three-way rule including the multiplicative expectation.

### 2.1 The three-way criterion, in the field's own words (Kuzminov, EcoSal Plus)

Section heading, verified exactly as printed: **"3.3. Epistatic analysis"**

Verbatim, recovered on two independent fetches with consistent text:

> "the double mutant possesses the phenotype of the single mutants (still shows only 30% drop), — this classic epistasis suggests that the two genes work in the same pathway; 2) the double mutant shows an "additive" (actually, multiplicative) effect (50% decrease), — the two genes must be working in separate pathways, and there are more functional pathways left; 3) the double mutant shows a synergistic effect (99% down)"

The third branch, from the first fetch, continues:
> "the double mutant shows a synergistic effect (99% down) — there are only two pathways, and the two mutations inactivate both"

— Kuzminov A. "Homologous Recombination—Experimental Systems, Analysis, and Significance." *EcoSal Plus* 2011. PMID 26442506, PMC4190071, §3.3. **FULL TEXT via NCBI BioC.** https://www.ncbi.nlm.nih.gov/research/bionlp/RESTful/pmcoa.cgi/BioC_json/PMC4190071/unicode **[V2 — two independent fetches returned consistent text]**

**Caveat, stated plainly:** a third fetch asking for the complete surrounding paragraph character-for-character returned **"VERBATIM NOT AVAILABLE"** rather than reproducing it. So the quoted fragments above are consistent across two passes but the full paragraph boundaries were never confirmed. **[PR: low-moderate]**

**This is exactly the operational definition an external answer key would be built on.** Note its three-way, not two-way, structure:
- **Epistatic (same pathway):** double ≈ the more sensitive single. No further drop.
- **"Additive" (explicitly glossed by the author as *actually multiplicative*) → separate pathways, with functional pathways still remaining.**
- **Synergistic (worse than the multiplicative expectation) → separate pathways, and the two mutations between them have removed all of them.**

The author's own parenthetical — `"additive" (actually, multiplicative)` — is the single most useful sentence in this entire report for benchmark-key purposes. The field's baseline expectation for independent pathways is the **product of the single-mutant survivals**, and the word "additive" in this literature is a term of art meaning multiplicative on survival fraction. A key built on a literal additive model would be scoring against a misreading of the field's own convention.

### 2.2 An independent, E. coli-specific statement of the same rule (Sandler lab)

> "If the two mutations are epistatic (they act in the same pathway), then the magnitude of the phenotypes should not be additive when comparing the single mutants with the double mutant (it should show the greater of the two). If they are not epistatic (they act in different pathways), then the magnitude of the phenotypes should be additive."

And, describing a worked application:

> "Strong evidence for this is seen from an experiment by Meddows *et al.* when they performed an epistasis analysis of *recA269*::Tn*10* and ∆*recN266* mutations with ionizing radiation...they found that while both single mutants were sensitive to ionizing radiation to different degrees, the double mutant was no more sensitive than the more sensitive of the two."

— Klimova AN, Sandler SJ. "An Epistasis Analysis of *recA* and *recN* in *Escherichia coli* K-12." *Genetics* 2020;216(2):381–393. **FULL TEXT.** https://pmc.ncbi.nlm.nih.gov/articles/PMC7536844/ **[V1]**

**Note the tension between the two statements.** Kuzminov distinguishes *three* outcomes and explicitly flags that "additive" means multiplicative. Klimova & Sandler use a *two-way* rule and do not distinguish additive from synergistic at all, nor do they state the multiplicative baseline. **The field does not speak with one voice on the quantitative baseline** — it agrees on the epistatic branch ("no worse than the more sensitive single") and is looser on the non-epistatic branch. Any answer key must choose, and the choice is not forced by the literature.

**NOT RETRIEVED:** the founding formalizations. Game & Cox (yeast, *Mutat Res* early 1970s) — **NOT RETRIEVED**; I could not verify its citation details and it should not be cited on my authority. Clark AJ, *Annu Rev Genet* 1973 — **NOT RETRIEVED**. Horii Z & Clark AJ, *J Mol Biol* 1973;80(2):327–344, "Genetic analysis of the recF pathway..." — citation **VERIFIED** (DOI 10.1016/0022-2836(73)90176-9) but the paper is a **total retrieval loss**. This is the founding *recF*-pathway paper and I have nothing from it but the citation. **The classical-era statement of the criterion was never obtained.** Both quotes above are modern (2011, 2020) restatements.

---

## ITEM 3 — QUANTITATIVE SINGLE- AND DOUBLE-MUTANT UV SURVIVAL DATA

**Retrieval status: POOR-TO-FAIR, and this is the candidate's central problem.**

**The headline finding on availability:** across roughly 40 papers touched, **UV survival is published almost exclusively as semilog curves in figures.** Numeric survival values in text or tables are rare. Nearly every classical source is behind a paywall or is a PMC page scan with no text layer.

### 3.1 Classical D37 values recovered from abstracts

**Howard-Flanders P, Theriot L, Stedeford JB. "Some Properties of Excision-defective Recombination-deficient Mutants of *Escherichia coli* K-12." *J Bacteriol* 1969;97(3):1134–1141.**
Authorship, volume, pages: **VERIFIED**. **ABSTRACT ONLY** (ASM landing page; full text behind the reader). https://journals.asm.org/doi/10.1128/jb.97.3.1134-1141.1969

> "Among the recombinants identified, one carrying *uvrA recA* proved to be of exceptional sensitivity to UV light. It is estimated from the UV dose (0.2 erg/mm2 at 253.7 nm) required to reduce the number of colony-forming cells by one natural logarithm that about 1.3 pyrimidine dimers were formed in a genome of 5 × 10^6 base pairs for each lethal event."

> "This double mutant is 40 times more UV-sensitive than the excision-defective strain carrying *uvrA6*."

> "The replication of one pyrimidine dimer is generally a lethal event in strains carrying *recA13*."

| Genotype | D37 | Converted | Provenance |
|---|---|---|---|
| *uvrA6 recA13* (double) | **0.2 erg/mm²** @ 253.7 nm | 0.02 J/m² *(my conversion; 1 erg/mm² = 0.1 J/m²)* | TEXT (abstract) |
| *uvrA6* (single) | ≈8 erg/mm² | ≈0.8 J/m² | **DERIVED BY ME** from the 40× statement — **NOT stated in the paper.** Flag as arithmetic, not as a Howard-Flanders number. |

Background: *E. coli* K-12, Hfr *uvrA6* × F⁻ *recA13* cross. **Strain designations NOT retrieved** (Table 1 inaccessible).

**Shlaes DM, Anderson JA, Barbour SD. "Excision Repair Properties of Isogenic *rec*⁻ Mutants of *Escherichia coli* K-12." *J Bacteriol* 1972;111(3):723–730.** **ABSTRACT ONLY.** https://journals.asm.org/doi/10.1128/jb.111.3.723-730.1972 — **independently retrieved twice with identical numbers; the most reliable single item in the haul.**

> "The doses of ultraviolet light (254 nm) required to reduce survival to 37% of the original population are 8 ergs/mm2 for *recA* or *recA recB* mutants, 5 ergs/mm2 for the *uvrB*− strain, 30 ergs/mm2 for the *recB recC* mutant, and 230 ergs/mm2 for the wild-type parent."

| Genotype | D37 (ergs/mm²) | D37 (J/m²) *(my conversion)* |
|---|---|---|
| wild-type parent | 230 | 23 |
| *recB recC* | 30 | 3.0 |
| ***recA*** or ***recA recB*** | **8** | **0.8** |
| *uvrB*⁻ | 5 | 0.5 |

Background stated only as "isogenic" K-12. **No strain names; no AB1157/MG1655/W3110 assignment retrieved.**

**This is a singles-and-double on one axis, and the result is a NULL: `recA recB` = `recA` alone (both 8 ergs/mm²).** That is textbook epistasis by the Kuzminov criterion — and it sits in direct tension with the 40× *uvrA recA* synergy. Different gene pairs, but note that the system does **not** show uniform double-mutant synergy.

### 3.2 Modern quantitative tables

**Zahradka D, Zahradka K, Petranović M, Đermić D, Brčić-Kostić K. "The RuvABC Resolvase Is Indispensable for Recombinational Repair in *sbcB15* Mutants of *E. coli*." *J Bacteriol* 2002;184(15):4141–4147.** https://journals.asm.org/doi/10.1128/jb.184.15.4141-4147.2002
Provenance: **TABLE 2**, caption verbatim "Survival of different *ruv* derivatives after UV irradiation", column header "Avg survival ratio ± SD at 10 J/m2". Methods verbatim: "irradiated with a dose of UV (254-nm) light of 10 J/m2." Background **AB1157**. Read twice, identical. **This is the richest singles-and-doubles table found. Single dose only — not a dose-response curve.**

| Strain | Genotype | Survival @ 10 J/m² |
|---|---|---|
| AB1157 | wild type | 0.89 ± 0.04 |
| LMM10 | Δ*ruvABC*::*cam* | 0.051 ± 0.002 |
| LMM1015 | *ruvB71*::*kan* | 0.045 ± 0.004 |
| JC5519 | *recB21 recC22* | 0.046 ± 0.012 |
| LMM20 | *recBC* Δ*ruvABC* | 0.035 ± 0.004 |
| JC7623 | *recBC sbcBC* | 0.73 ± 0.02 |
| LMM864 | *recBC sbcBC* Δ*ruvABC* | 0.0004 ± 0.00003 |
| LMM965 | *sbcBC* | 0.69 ± 0.04 |
| LMM966 | *sbcBC* Δ*ruvABC* | 0.0003 ± 0.0001 |
| LMM979 | *sbcB* | 0.84 ± 0.05 |
| LMM983 | *sbcB* Δ*ruvABC* | 0.00039 ± 0.00008 |
| N2364 | *sbcC* | 0.83 ± 0.05 |
| LMM971 | *sbcC* Δ*ruvABC* | 0.023 ± 0.003 |
| LMM1018 | *sbcB ruvB* | 0.00062 ± 0.00011 |
| LMM1032 | *recJ* | 0.54 ± 0.09 |
| LMM1033 | *recBC sbcBC recJ* | 0.00005 ± 0.00002 |
| LMM997 | Δ*xonA* | 0.90 ± 0.04 |
| LMM1017 | Δ*xonA ruvB* | 0.041 ± 0.005 |

Worked example of the Kuzminov criterion on real numbers: *sbcB* = 0.84, Δ*ruvABC* = 0.051, multiplicative expectation = 0.043, **observed double = 0.00039** — roughly 100-fold below expectation. Clean quantitative synergy. Conversely *recBC* = 0.046, Δ*ruvABC* = 0.051, expectation 0.0023, **observed 0.035** — far *above* expectation, i.e. epistatic.
**No *recA* row, no *recG* row, no *ruvC* single** (the operon deletion and *ruvB71* stand in).

**Weel-Sneve R, Bjørås M, Kristiansen KI. *Nucleic Acids Res* 2008;36(19):6249–6259.** https://academic.oup.com/nar/article/36/19/6249/2410430
Provenance: **TABLE 2**, header "Survival (%)". Read twice, identical.

| Strain | Genotype | 0 J/m² | 5 J/m² | 15 J/m² |
|---|---|---|---|---|
| AB1157 (+ pKK232-8) | wild type | 100 | 80 | 36 |
| DM49 (+ pKK232-8) | ***lexA3* (Ind⁻)** | 100 | **13** | **2.4** |

**Caveat: DM49's genetic background is not stated in the text read. Do not assume AB1157-isogenic.**

**Kuban W et al. *DNA Repair* 2012; PMC3419331.** https://pmc.ncbi.nlm.nih.gov/articles/PMC3419331/ — RUNNING TEXT:
> "Cell viability after exposure to 20 J/m² was in the range of 85–90% survival for wild-type, F10L and Y11F mutants and ~60–70% for vector control, pGB2, and the Y11A mutant."

Host RW584 = Δ*umuDC596*::*ermGT lexA51*(Def) *recA730*. The **pGB2 empty-vector** row is the functional no-Pol-V datapoint: ~60–70% @ 20 J/m² vs 85–90% complemented. First-author attribution is from the Europe PMC index, **not seen on the article page itself**.

**Courcelle CT, Landstrom AJ, Anderson B, Courcelle J. *J Bacteriol* 2012;194(15):3977–3986.** https://journals.asm.org/doi/10.1128/jb.00290-12 — RUNNING TEXT:
> "the hypersensitivity of priA2 was nearly identical to that of a recA mutant and had a mean (37%) lethal dose (LD37, or e−1 survival) occurring at 0.2 J/m2 or ∼6 lesions per genome"
> "Both priB302 and priC mutants were as resistant to UV irradiation as wild-type cells"

**LD37(*recA*) ≈ 0.2 J/m²**, background **SR108** (*thyA36 deoC2*, a W3110 derivative).
(Note: the ASM page reported page numbers and a PMCID that were **wrong**; the values above come from Crossref + NCBI ID converter.)

**Ghosh S, Orman MA. bioRxiv 2024.11.14.623584 (v2, 2025).** https://www.biorxiv.org/content/biorxiv/early/2025/06/09/2024.11.14.623584.full.pdf

> ⚠️ **THIS IS 302 nm UV-B, NOT 254 nm UV-C. Its doses are NOT commensurable with the classical germicidal-UV literature.** Do not plot these on the same axis as Howard-Flanders or Shlaes.

> "UV-B light (302 nm thin-line transilluminator, UVP ChemStudio, Analytik Jena) for varying exposure times (0, 2, 4, 8, 16, 24 and 32 min), ensuring a wide range of UV intensity from 120 J/m² to as high as 1920 J/m²"
> "UV-B irradiance was consistently measured at approximately 1000 mW/m²"
> "A 4-8 min exposure caused a 10-fold reduction, while 16 min led to a ~100-fold drop compared to the control."
> "Exposure times of 24 and 32 min resulted in a ~10,000-fold reduction"
> "CFU levels in the ΔrecA strain were below the limit of detection (1 CFU) for most UV treatment conditions; however, this was transient, as we observed a rapid increase in CFU levels (from 1 to 10^7) within 15 minutes of recovery"

⚠️ **INTERNAL INCONSISTENCY OBSERVED:** the v1 full-text page reported "UV intensity ∼2000 μW/cm²" (= 20 W/m²), **20× the v2 figure** of 1000 mW/m² (= 1 W/m²). The stated 120–1920 J/m² range is consistent only with 1 W/m². **Treat this paper's absolute dosimetry as unsettled.**

Genotypes: MG1655 wild type; deletions from the **Keio/BW25113** collection — **note the background mismatch**. Singles Δ*recA*, Δ*recN*, Δ*rmuC*, Δ*polB*, Δ*dinB*, Δ*recB*, Δ*umuC*, Δ*umuD*, Δ*ruvC*, Δ*uvrA*, Δ*uvrD*, Δ*katE*, Δ*mutY*, Δ*sulA*, Δ*tisB*, Δ*phr*; combinations Δ*recN*Δ*rmuC*, Δ*polB*Δ*dinB*, Δ*recN*Δ*polB*, Δ*recN*Δ*dinB*, Δ*sulA*Δ*tisB*, and two triples.
Verbatim, qualitative: Δ*ruvC*, Δ*umuC*, Δ*umuD* "showed no significant change in transient non-culturability immediately after UV-B treatment compared to the wild type"; Δ*recB*, Δ*uvrA*, Δ*uvrD* showed "even more drastic reductions following UV-B treatment compared to the wild type."
**Per-mutant dose-response numbers are in figures, not text.** The 3-fold / 1.5-fold / ~5-fold numbers in this paper are **Rif-resistance mutagenesis, not survival** — do not mistake them.

### 3.3 Verbatim double-vs-single comparisons that are qualitative only

> "Cells carrying a *uvr* mutation together with *recA13, recA56, recB21*, or *recC22* failed to show MMR and were more sensitive to ultraviolet radiation than either their *rec*+*uvr*− or *rec*−*uvr*+ parents."
— **Ganesan AK, Smith KC.** *J Bacteriol* 1970;102(2):404–410. **ABSTRACT ONLY.** https://journals.asm.org/doi/10.1128/jb.102.2.404-410.1970
*Attribution note: this is Ganesan & Smith, not Howard-Flanders.*

> "The relative UV radiation sensitivities of the multiply mutant strains in the Δ*uvrB* background were: *recF recB lexA > recF recB uvrD lexA, recF recB uvrD > recA > recF uvrD lexA > recF recB, recF uvrD > recF lexA > recB uvrD lexA > recB uvrD > recB lexA, lexA uvrD > recB > lexA, uvrD > recF*; three of these strains were more UV radiation sensitive than the *uvrB recA* strain."
— Wang T-cV, Smith KC. *Mol Gen Genet* 1981;183(1):37–44. **ABSTRACT ONLY.** **A complete rank-ordering of doubles/triples/quadruples — ordinal only, no doses, no survival fractions.** This is the richest epistasis *structure* found and it cannot support a single numeric claim.

> "When the ability to repair DNA daughter strand gaps was compared, *uvrB recF* cells showed a gross deficiency, whereas *uvrB recB* cells showed only a small deficiency." / "The introduction of a *recB* mutation into the *uvrB recF* strain greatly increased its UV radiation sensitivity…"
— Wang TC, Smith KC. *J Bacteriol* 1983;156(3):1093–1098. **ABSTRACT ONLY.**

> "Hypersensitivity was more severe in the *ruvAB recG* double mutant than in either single mutant and was comparable to that of *recA* (Figure 2A)."
— Donaldson JR, Courcelle CT, Courcelle J. *Genetics* 2004;166:1631–1640. https://web.pdx.edu/~justc/papers/DonaldsonGenetics2004.pdf — **FROM FIGURE, no numbers.**

> "mutants lacking all three DNA polymerases were no more sensitive to UV irradiation than the Pol V single mutant" / "a *uvrA* mutant was much more sensitive to UV irradiation than the triple-polymerase mutant" / "the sensitivity of the quadruple-*uvrA*-polymerase mutant was similar to that of the *uvrA* mutant alone"
— Courcelle CT, Belle JJ, Courcelle J. *J Bacteriol* 2005;187(20):6953–6961. https://web.pdx.edu/~justc/papers/CourcelleUvrPolV.pdf — **FROM FIGURE (Fig 1A/1B); zero numeric survival values anywhere in the paper.** Strains: CL646 = *polB dinB umuDC* triple; **CL681 = *polB dinB umuDC uvrA* quadruple**; all SR108. **This is the single most benchmark-relevant qualitative result in the corpus** — see Item 5.

> "In all cases, the double mutant had an additive phenotype."
— Klimova & Sandler, *Genetics* 2020;216:381–393 (*recA4190* Δ*recN*, AB1157 *recB21 recC22 sbcB15 sbcC201* background).

> ⚠️ **Klimova & Sandler Table 1 is a trap.** It contains attractive singles-and-double survival fractions (*recA4190* 0.10, Δ*recN* 0.02, double 0.0054) — but it is **I-SceI double-strand-break survival, NOT UV.** Their UV data is **Figure 1 only**, and the figure caption gives no dose or survival values.

---

## ITEM 4 — WHICH ENTRIES ARE SOLID

**Replicated quantitatively across independent groups:**
- ***recA* single, D37 only.** Shlaes 1972 → 0.8 J/m²; Courcelle 2012 → 0.2 J/m². **Two independent groups, but 4× apart**, in different (and in one case unspecified) backgrounds. Order-of-magnitude agreement only. **This is the ONLY genotype with genuine independent quantitative corroboration.**

**Single-source quantitative:**
- *uvrA recA* double — Howard-Flanders, Theriot & Stedeford 1969. **The headline double-mutant number rests on one sentence in one 1969 abstract.**
- *uvrB* single, *recB recC*, *recA recB*, wild type — all Shlaes 1972 (one paper).
- Δ*ruvABC*, *ruvB*, and all *sbcB*/*sbcBC*/*recJ* doubles — Zahradka 2002 (internally replicated across two *ruv* alleles, but one group).
- *lexA3* (Ind⁻) — Weel-Sneve 2008.
- Pol V-null equivalent @ 20 J/m² — Kuban 2012.
- MG1655 wild type under **UV-B** — Ghosh & Orman (non-commensurable dose regime).

**Qualitative / ordinal only — no numbers exist in any retrieved source:**
- Singles: *uvrC*, *recF*, *recO*, *recR*, *polB*, *dinB*, *ruvC*-alone, *recG*
- Doubles: *umuDC uvrA*, *recA recF*, *recB recF*, *uvrB recF*, *ruvAB recG*, and the entire Wang & Smith rank-ordering

**Genotypes on the target list with ZERO retrieved numbers of any kind:** ***recF*, *recO*, *recR*** (not one dose/survival pair, single or double, from any source); ***polB*** and ***dinB*** singles; ***umuDC uvrA***.

**Blunt summary of Item 4:** exactly **one** entry (*recA* single) is replicated. Exactly **two** sources put singles and a double on the same quantitative axis (Shlaes 1972; Zahradka 2002), and **they disagree in kind** — Shlaes reports a null (epistasis), Zahradka reports 100-fold synergy for a different pair. The *uvrA recA* synergy that makes this candidate attractive is **single-source, abstract-only, 1969, with the comparator single-mutant value not stated in the paper.**

---

## ITEM 5 — INERT / SPECTATOR

### 5.1 The proposed spectator (phr in the dark) does NOT hold up

**The premise fails.** No primary paper was found stating that *phr* mutants are indistinguishable from wild type without photoreactivating light. Multiple labs report the opposite.

> "An *Escherichia coli recA phr*+ *purA* strain was more resistant to ultraviolet radiation than its isogenic derivative *recA phr*+ *purA*+ in the absence of photoreactivating light, whereas their nearly isogenic derivative *recA phr* showed most UV-induced lethality. The amounts of photoreactivating enzyme (PRE) per cell in the *recA phr*+ *purA* was higher than in the *recA phr*+ *purA*+. The *recA phr* is defective for photoreactivation. Thus, in the *recA* strain, UV resistance in the dark increased in proportion to the amounts of PRE per cell, suggesting that PRE participates in the process of dark repair of UV-damaged DNA."
— Yamamoto K, Fujiwara Y, Shinagawa H. "Evidence that the *phr*+ gene enhances the ultraviolet resistance of *Escherichia coli recA* strains in the dark." *Mol Gen Genet* 1983;192:282–284. **ABSTRACT ONLY.** https://link.springer.com/article/10.1007/BF00327679
**A *phr* null was the most UV-killed strain of the set, in the dark.** Caveat: *recA* background.

> "As previously reported, al introduced phr genes provided the host cells with photoreactivation-repair activity and the introduced E. coli phr gene rendered the host cells more UV-resistant in the dark. E. coli cells harboring foreign phr genes, however, were found to be more sensitive to UV light in the dark than cells containing the vector plasmid only. These differences in UV sensitivity in the dark disappeared when the host cells had an additional mutation, uvrA, suggesting that the foreign photolyases inhibited the E. coli excision-repair system."
— Kobayashi T, Takao M, Oikawa A, Yasui A. *Mutat Res* 1990;236(1):27–34. PMID 2114539. **ABSTRACT ONLY.** ("al" is a typo present in the source as returned.)
**The dark effect is mediated through excision repair — it vanishes in *uvrA*.**

> "We found that photolyase stimulates the removal of pyrimidine dimers but not other DNA adducts by uvrABC excision nuclease."
— Sancar A, Franklin KA, Sancar GB. "*Escherichia coli* DNA photolyase stimulates uvrABC excision nuclease in vitro." *PNAS* 1984;81(23):7397–7401. **ABSTRACT ONLY**; PMC392153 is **SCANNED, NO TEXT LAYER**.

> "In the absence of photoreactivating light, this enzyme binds to pyrimidine dimers but is unable to repair them."
> "This effect is similar to the effect of *Escherichia coli* photolyase on excision repair in the bacterium."
> "Instead, Phr1 was found to be a potent inhibitor of dark repair in *recA* strains but had no effect in *uvrA* strains."
> "We propose that enhancement of nucleotide excision repair by photolyases is a general phenomenon and that photolyase should be considered an accessory protein in this pathway."
— Sancar GB, Smith FW. *Mol Cell Biol* 1989;9(11):4767–4776. **ABSTRACT ONLY**; PMC363625 is **SCANNED, NO TEXT LAYER**.

> "…have identified a new role for photolyases in dark-repair processes which has implications for the mechanism of nucleotide excision repair in both prokaryotes and eukaryotes."
— Sancar GB. "DNA photolyases: physical properties, action mechanism, and roles in dark repair." *Mutat Res* 1990;236(2–3):147–160. PMID 2204823. **ABSTRACT ONLY.**

**The honest, narrow statement:** photolyase binds cyclobutane dimers in the dark, stimulates uvrABC in vitro, and measurably changes dark UV survival in vivo — but **all the in vivo dark evidence comes from *recA* backgrounds and/or multicopy/overexpressed *phr*.** The specific experiment that would settle it — **chromosomal *phrB* null vs wild type, *uvr*⁺ *recA*⁺, dark plating — was NOT RETRIEVED and remains open in either direction.** The field's own review literature calls photolyase "an accessory protein in this pathway," which is the opposite of spectator.

**Evidence FOR spectator status: NOT FOUND.** Multiple search formulations targeting Harm, Rupert, Setlow JK, Youngs & Smith returned nothing. The closest modern statement points the other way, and is in the wrong organism:
> "ES114 also appeared slightly more resistant to UV light than the mutant, even when recovery was in the dark"
— Walker EL, Bose JL, Stabb EV. *Appl Environ Microbiol* 2006;72(10):6600–6606. FULL TEXT. **This is *Vibrio fischeri*, not E. coli.**

**Is *phr* under LexA/SOS control? CONTESTED and unresolved.**
- FOR: Ihara M, Yamamoto K, Ohnishi T. *Mol Gen Genet* 1987;209:200–202 — the fetch was partly paraphrased; the fragment vouched for is the authors' conclusion that "induction of the phr gene is one of the SOS responses." **[PR]**
- AGAINST: Payne NS, Sancar A. "The LexA protein does not bind specifically to the two SOS box-like sequences immediately 5′ to the *phr* gene." *Mutat Res/DNA Repair* 1989;218(3):207–210. Metadata verified verbatim via Crossref. **ABSTRACT NOT RETRIEVED. The title is the only evidence I have, and a title is not a quoted finding.**
- *phrB* does not appear in the Simmons et al. 2008 LexA-dependent list.

**Methods practice (safelight):** the specific "yellow/gold safelight" methods statement common in E. coli genetics was **NOT RETRIEVED**. What was retrieved:
> "the remaining plates for the 'dark' treatment were kept in the darkroom during recovery and were dilution plated under a dim red light" — Walker et al. 2006 (*V. fischeri*)
> "After irradiation, the petri dish was covered with foil to prevent further light penetration." — Zimmer JL, Slawson RM. *Appl Environ Microbiol* 2002;68(7):3293–3299.
Treat "standard UV survival work uses yellow safelight" as *inferred/unsourced*.

### 5.2 A BETTER spectator candidate emerged: translesion synthesis

This is the most useful unexpected result of the exercise. **The three SOS-inducible polymerases are close to inert for UV survival**, even though they are essential for UV *mutagenesis*:

> "mutants lacking all three DNA polymerases were no more sensitive to UV irradiation than the Pol V single mutant"
> "a *uvrA* mutant was much more sensitive to UV irradiation than the triple-polymerase mutant"
> "the sensitivity of the quadruple-*uvrA*-polymerase mutant was similar to that of the *uvrA* mutant alone"
— Courcelle CT, Belle JJ, Courcelle J. *J Bacteriol* 2005;187(20):6953–6961. **FROM FIGURE (Fig 1A/1B); no numeric values in the paper.**

> Δ*ruvC*, Δ*umuC*, Δ*umuD* "showed no significant change in transient non-culturability immediately after UV-B treatment compared to the wild type"
— Ghosh & Orman 2024 bioRxiv. **UV-B, 302 nm.**

**Read carefully: the quadruple *uvrA polB dinB umuDC* mutant ≈ *uvrA* alone.** By the Kuzminov criterion that is textbook epistasis — but it is epistasis of *nothing with something*, i.e. the TLS module contributes essentially no survival on top of NER loss. **For a survival-scored answer key, *polB*, *dinB* and *umuDC* are the genuine spectators — not *phr*.** But note the evidence is **figure-only and single-group**, and it is confounded with the fact that Pol V is measured here in a background where its main phenotype (mutagenesis) is not the readout.

---

## ITEM 6 — PUBLISHED DYNAMICAL MODELS, AND WHAT THEY WERE FITTED TO ★ DECISIVE ITEM

**Headline: NO published dynamical model of the E. coli SOS response predicts survival fraction. Zero of nine. And none used repair-mutant survival data in fitting.**

### Per-model report

**(1) Aksenov SV, Krasavin EA, Litvin AA.** "Mathematical model of the SOS response regulation of an excision repair deficient mutant of *Escherichia coli* after ultraviolet irradiation." *J Theor Biol* 1997;186:251–260.
Citation recovered **from the author's own later reference list**, not from the article page (PubMed reCAPTCHA ×3; Europe PMC 429 ×5; Crossref 429/403 ×3). DOI not retrieved. Note a title discrepancy: PubMed search results render "…ultraviolet **light** irradiation"; the author's own reference omits "light."
**(b)–(f) NOT RETRIEVED.** No model description, no calibration data, no outputs. **Nothing about this paper should be asserted.**

**(2) Aksenov SV.** "Dynamics of the inducing signal for the SOS regulatory system in *Escherichia coli* after ultraviolet irradiation." *Math Biosci* 1999;157(1–2):269–86. DOI 10.1016/s0025-5564(98)10086-x. PMID 10194933. **Single author — verified on the PubMed article page.** **ABSTRACT ONLY.**
> "In the present study a model for quantitative description of the signal dynamics is developed. We derive the inducing signal, in terms of concentration of single-stranded DNA, as a function of time since the moment of ultraviolet irradiation."
> "The model is verified against available experimental data for LexA protein level in ultraviolet radiation-induced *Escherichia coli* cells."
> "Simulation of the signal level after irradiation with two doses of 5 and 20 J m-2 is presented."
(a) Deterministic; species = ssDNA signal, LexA. Equation/parameter counts **NOT RETRIEVED**.
(c) Calibrated to **LexA protein level time courses**; the assay modality is not stated in the abstract — *unknown*.
(d) No survival language in the abstract. *Absence of evidence in an abstract, not verified absence.*
(e) **Outputs ssDNA signal and LexA level. No survival.** *Inferred pending full text.*

**(3) Aksenov SV.** "Induction of the SOS Response in Ultraviolet-Irradiated *Escherichia coli* Analyzed by Dynamics of LexA, RecA and SulA Proteins." *J Biol Phys* 1999;25(2):263–277. DOI 10.1023/A:1005163310168. **Citation VERIFIED on the Springer page. ABSTRACT ONLY.**
> "Here, induction of the SOS response in *Escherichia coli* with normal and impaired excision repair function is studied by simulation of intracellular levels of regulatory LexA and RecA proteins, and SulA protein."
> "Results of the simulations show that nucleotide excision repair influences time-courses of LexA, RecA and SulA induction by modulating the dynamics of RecA protein distribution between its normal and SOS-activated forms."
(a) Three protein species + repair state; deterministic ODEs — corroborated by the reference list citing the ODE integrator EPISODE (ref. 25).
(c) Body text NOT RETRIEVED. Reference list points at Sassanfar & Roberts 1990; Weisemann et al. 1984 (*recA–lacZ* fusions); **Quillardet & Hofnung 1984, "Induction by UV light of the SOS function sfiA in Escherichia coli strains deficient or proficient in excision repair"** — note that last one is an **SOS-reporter (β-galactosidase) study in excision-repair mutants, NOT a survival study.** Which were fitted vs merely cited is *inferred*.
(d) **This paper does model excision-repair-deficient cells — but the mutant dataset in its reference list is SOS induction, not colony-forming ability.**
(e) **No survival.** It models SulA, the division inhibitor — **filamentation/division arrest, not viability. Do not conflate the two.**

**(4) Krishna S, Maslov S, Sneppen K.** "UV-Induced Mutagenesis in *Escherichia coli* SOS Response: A Quantitative Model." *PLoS Comput Biol* 2007;3(3):e41. DOI 10.1371/journal.pcbi.0030041. PMID 17367202. **FULL TEXT (PLOS HTML + arXiv q-bio/0701013, cross-checked).**
(a)
> "We mathematically model the temporal dynamics of the density of UV-induced lesions, as well as concentrations of LexA, RecA*, unbound UmuD, unbound UmuD′, UmuD–UmuD′ heterodimer, and Pol V, using a set of ordinary differential equations."
> "Our model is fully specified by 18 parameters."
> "The model has a total of 18 parameters of which only 3 could not be fixed by experimental data."
> "Thus, our model ignores stochastic fluctuations."
**7 tracked quantities, deterministic ODEs, 18 parameters, 3 free.** Pol V is algebraic, not an independent ODE.
(c)
> "Most parameters in our model have been fixed using experimental data. For example, the experiments in refs. [3, 4, 12] allow us to fix the RecA*-mediated cleavage rates of LexA and UmuD."
> "λ = 0.035 min−1, corresponding to a half-life of approximately 20 min as reported in [27] for cyclobutane pyrimidine dimers"
> "we choose NfLRecA*τRecA* × γl fixed so that the maximum rate of LexA degradation… corresponding to a half-life of about 1.5 min, chosen to match pulse-labeling measurements of LexA degradation rates"
> "we show in Figure 8A the peak heights averaged more than 200 runs with varying Nf. The resultant peak height versus UV dose curves match the data of [10] satisfactorily…"
**Fitted to: DNA-lesion decay kinetics, protein cleavage/degradation rates, and Friedman et al. 2005 single-cell promoter-GFP time courses.**
(d) **NO survival data.** Two independent renderings (PLOS HTML and arXiv PDF) both returned NOT PRESENT for *survival / surviv / colony / viability / cell death / killing / lethal*. **A double negative from two renderings — weighted as strong.**
(e) **NO.** And note — despite "Mutagenesis" in the title, both fetches also returned NOT PRESENT for a computed **mutation frequency or mutation rate**. The mutagenesis proxy is the **Pol V concentration time course**: Figure 6 caption verbatim — "Pol V concentration as a function of time, following an instantaneous pulse of UV at time zero, for different UV doses." Headline result is qualitative: "a tight regulation of mutagenesis resulting, we show, in a 'digital' turn-on and turn-off of Pol V." **So: not survival, and arguably not even mutation frequency — it outputs the mutagenic-polymerase availability window.**

**(5) Shimoni Y, Altuvia S, Margalit H, Biham O.** "Stochastic Analysis of the SOS Response in *Escherichia coli*." *PLoS ONE* 2009;4(5):e5363. PMID 19424504. **FULL TEXT** via PMC2675100.
(a)
> "deterministic analysis of the SOS system using rate equations and stochastic analysis using Monte Carlo simulations based on the Gillespie algorithm"
Tracks "the copy number of each molecule in a single cell as a function of time." Species: *recA* mRNA, *lexA* mRNA, reporter mRNA, RecA, LexA, GFP, LexA–promoter bound states. **Table 1 lists 16 processes** (rate constants 0.001–0.1 s⁻¹). Exact ODE count is in supplementary material, **NOT RETRIEVED**. Key result: "Notably, deterministic simulations of the same model do not produce peaks in the promoter activities."
(c)
> "A GFP reporter gene was inserted into *E. coli* on a plasmid that carried the same promoter site as *recA*. These bacteria were then irradiated by UV, causing DNA damage. The amount of GFP was measured in single cells vs. time."
Follows the experimental procedure of Friedman et al. 2005. **Qualitative peak-timing matching, not a formal fit — no fitting procedure was described in what was retrieved.**
(d) **NO.** ("No mentions found" for survival fraction, colony forming ability, viability, cell death. *Single-pass summarizer negative.*)
(e) **NO.** Outputs *recA* promoter activity vs time, peak-timing distributions, population averages.

**(6) Friedman N, Vardi S, Ronen M, Alon U, Stavans J.** "Precise Temporal Modulation in the Response of the SOS DNA Repair Network in Individual Bacteria." *PLoS Biol* 2005;3(7):e238. **FULL TEXT.**
**⚠️ THIS IS NOT A MODEL PAPER. It is experimental.** The only quantitative relation retrieved:
> "The linear relation that exists between 1/T₁ and 1/TD (1/T₁ = 1/TD + 1/τ) suggests that the peaks' timing is governed by the effective lifetime of a factor that is diluted by cell growth at a rate 1/TD and is degraded at a rate 1/τ = 1/68 min⁻¹"
No ODE system. **It is the canonical *data source* the other SOS models fit to, not a model itself.** Data:
> "time-lapse fluorescence microscopy to measure the fluorescence intensity and size of bacteria containing the reporter plasmids over 150 min following DNA-damaging UV irradiation, at a 2-min temporal resolution"
(d)/(e) **NO survival.** The only damage-consequence statement retrieved: "Some cells grow and undergo cell division (e.g., cell #1), while others exhibit filamentation (e.g., cell #2), as a consequence of DNA damage." **Filamentation ≠ death.**
*(A companion primer, *PLoS Biol* 3(7):e255, "After 30 Years of Study, the Bacterial SOS Response Still Surprises Us," PMID 16000023, is a different paper — do not confuse them.)*

**(7) Ronen M, Rosenberg R, Shraiman BI, Alon U.** "Assigning numbers to the arrows: Parameterizing a gene regulation network by using accurate expression kinetics." *PNAS* 2002;99(16):10555–10560. PMID 12145321. **FULL TEXT** via PMC124972. (The fetch rendered the issue date as "Jul 26"; publisher pages give 23 July — treat the exact day as *contested*.)
(a) Deterministic, **algebraic (not ODE)** Michaelis–Menten repression: **Xi(t) = βi · A(t) / (ki + A(t))**. **Two parameters per gene (βi, ki) across eight genes**, plus an inferred A(t). Genes: *uvrA, uvrD, lexA, recA, ruvA, polB, umuD, uvrY* (+ *lacZ* control). **This is a parameter-inference framework, not a mechanistic SOS simulator** — LexA cleavage, RecA*, ssDNA and lesions are not dynamical variables; A(t) is *inferred from the data*, not derived.
(c)
> "We constructed GFP reporter strains for eight of the SOS operons. The GFP used in this study becomes fluorescent within minutes after transcription and its degradation rate is negligible."
> "Promoter activity is given by Eq. [1], Xi(t) = [dGi(t)/dt]/ODi(t)"
Low-copy pSC101 plasmids with *gfpmut3*; plate-fluorimeter reads every ~3 min.
(d) **NO** (NOT PRESENT for survival/viability/colony/lethal). (e) **NO** — outputs promoter-activity time courses and kinetic parameters.

**(8) Belov OV, Krasavin EA, Parkhomenko AYu.** "Model of SOS-induced mutagenesis in bacteria *Escherichia coli* under ultraviolet irradiation." *J Theor Biol* 2009;261(3):388–395. DOI 10.1016/j.jtbi.2009.08.016.
**Citation VERIFIED via Crossref metadata only. NOT RETRIEVED — abstract never obtained** (ScienceDirect robots-disallowed; PubMed/Europe PMC blocked or 429 across six attempts). **THIS IS THE SINGLE BIGGEST GAP IN ITEM 6** — it is the one candidate whose title suggests it might couple SOS dynamics to a cell-level outcome.

What *can* be said, from verified companion papers by the same group:
- Belov OV, Chuluunbaatar O, Kapralov MI, Sweilam NH. *J Theor Biol* 2013;332:30–41. PMID 23643530. **ABSTRACT ONLY:**
  > "For this purpose, mathematical models of the SOS network, translesion synthesis and mismatch repair are developed."
  > "…the bacterial mismatch repair system is responsible for attenuation of **mutation frequency** during ultraviolet-induced SOS response via removal of the nucleotides misincorporated by DNA polymerase V (the UmuD′2C complex)."
  → **Output is mutation frequency. No survival.**
- Bugay A, Vasilyeva M, Parkhomenko A, Krasavin E. "Mathematical Analysis of Regulatory Networks and Damage Repair Efficiency in Bacterial Cells," in *Genetics, Evolution and Radiation*, 2016, pp. 175–185. DOI 10.1007/978-3-319-48838-7_15. **ABSTRACT ONLY:**
  > "An extended mathematical model of the UV-induced mutation process in *E. coli* bacterial cells has been developed. It describes the whole sequence of molecular events involved in nucleotide excision repair of initial damage, replication kinetics and postreplication repair. The model provides ab initio calculation of the number of **mismatches** as a result of translesion synthesis for both wild type and **repair-deficient mutant** cells. A comparison of efficiency of different repair systems has been carried out."
  → **The closest anything in this literature comes: it does treat repair-deficient mutants — but the modelled endpoint is mismatches/mutations, not colony-forming survival.**
- Belov OV, Krasavin EA, Parkhomenko AYu. *Biophysics* 2010;55(4):682–690. DOI 10.1134/S0006350910040287. **ABSTRACT ONLY:** "The probability of mutations during translesion synthesis is estimated."

**(9) Jones EC, Uphoff S.** "Single-molecule imaging of LexA degradation in *Escherichia coli* elucidates regulatory mechanisms and heterogeneity of the SOS response." *Nat Microbiol* 2021;6(8):981–990. PMID 34183814. **FULL TEXT** via PMC7611437.
*(Attribution note: **Jones is first author**, not Uphoff — Uphoff is the lab.)*
(a) **Not a network ODE model** — kinetic/statistical fitting: a diffusion-state mixture model (`D = MSD/(4·Δt), Δt = 7.48 ms`), exponential decay fits (free LexA "half-life of 19 min after 50 J/m2 UV (16–27 min 95% CI)"), a gene-regulatory input function ("promoter affinity of LexA between 2-10 nM"), least-squares `(NORM(Dmodel*P - Dmeasured))²`.
(c) Single-molecule tracking, in-gel TMR fluorescence, SDS-PAGE, mother-machine P*recA*-GFP dynamics, UV/ciprofloxacin/MMS.
(d) **This is the ONLY paper in the set where survival data appears at all:**
  > "UV survival was partially reduced for LexA-Halo compared to wild-type"
  > "LexA-Halo shows the same sensitivity to ciprofloxacin and methyl methanesulfonate"
  > "The LexA-Halo strain has the same death rate as the wild-type"
  > "LexAG85D mutant has a higher spontaneous death rate"
  **But read what this is:** strain-validation controls (does the Halo tag break LexA?) and phenotyping of a *lexA* regulatory allele. **Not survival data fed into any model fit**, and these are *lexA* alleles, not repair-pathway mutants.
(e) **NO** — NOT PRESENT for survival-fraction prediction.

**(10) Ghosh S, Orman MA.** bioRxiv 2024, DOI 10.1101/2024.11.14.623584. **FULL TEXT. NO MODEL** — "The manuscript contains no equations, differential equations, or formal stochastic model descriptions." Purely experimental. **It has exactly the Δ*recA*/Δ*uvrA*/Δ*umuC* CFU-survival dataset that a model would need — with no model attached.**

### Item 6 verdict

**(i) Models that predict survival fraction: NONE.** Zero of nine. Endpoints are: promoter activity / GFP time courses (Ronen 2002; Shimoni 2009), regulator-protein and ssDNA levels (Aksenov 1997/1999×2), Pol V availability as a mutagenesis proxy (Krishna–Maslov–Sneppen 2007), and mutation/mismatch frequency (Belov group 2009/2010/2013; Bugay 2016). **SulA/filamentation appears in Aksenov 1999 (J Biol Phys) — that is division arrest, not death, and must not be read as survival.**

**(ii) Models that used repair-mutant survival data in fitting or validation: NONE**, on the evidence retrievable. The Belov/Bugay lineage does model repair-deficient mutants, but calibrates and reports on mutation counts.

**(iii) Consequence for the candidate.** The SOS modelling literature and the SOS survival-phenotype literature **have essentially never been joined.** Scoring any of these models against a survival answer key would require an added, unvalidated mapping from molecular state (LexA level, Pol V window, ssDNA) to colony-forming ability. No such mapping was found published, fitted, or validated anywhere in the corpus.

**(iv) The one paper that could still overturn (iii): Belov et al. 2009 *J Theor Biol* 261:388–395 — NOT RETRIEVED.** That should be opened by hand before this conclusion is asserted as final.

**(v) Attribution corrections to the original candidate list:** "Aksenov" is **three** distinct papers, not one. **Friedman et al. 2005 is not a model** — it is the data source others fit to. "Kozlowski" as an SOS modeller was **NOT FOUND** and is probably a misattribution (a negative that cannot be proven from search alone). **Sassanfar & Roberts is not a model** — it is a calibration data source.

---

## ITEM 7 — HONEST ASSESSMENT: SOLID VS CONTESTED, AND COMPLICATIONS

### 7A. Solid
- **The pathway architecture** (NER / recombinational repair / TLS / photoreactivation) and the **SOS circuit** (LexA repressor, RecA* coprotease, LexA autocleavage, lexA/recA autoregulation) are settled science with clean quoted evidence, including the mechanistically important coprotease-vs-protease distinction (Little 1984, 1991, 1993).
- **The epistasis-group method has an explicit, retrievable operational definition** in the field's own words, including the multiplicative baseline (Kuzminov 2011 §3.3; Klimova & Sandler 2020). **This is the candidate's genuine strength and it survived checking.**
- **Pol V = UmuD′₂C**, **Pol IV = DinB**, **Pol II = PolB = DinA** — all verified from primary abstracts.
- **A handful of quantitative survival datapoints** exist and are internally consistent: Shlaes 1972 D37 set; Zahradka 2002 Table 2 (AB1157, 10 J/m²); Weel-Sneve 2008 Table 2 (*lexA3*).

### 7B. Contested or unresolved
- **The classical epistasis-group assignments have been mechanistically reinterpreted, and the pathway boundary is demonstrably leaky.** This is the most important complication for an answer key. See 7C.
- ***phr* is not a clean spectator in the dark.** See Item 5.
- ***recF*'s LexA-regulon status is unresolved** by any retrieved source.
- ***phr*'s SOS-regulation status is contested** (Ihara 1987 for; Payne & Sancar 1989 title against, abstract not retrieved).
- **The LexA regulon size has four published numbers in three different units** (31 / 26+17 / ~43 / 57).
- **The *recA* D37 differs 4× between the two groups reporting it** (0.8 vs 0.2 J/m²).

### 7C. Have epistasis-group assignments been revised? — RETAINED BUT REINTERPRETED, AND LEAKY

I went looking for a repudiation and did not find one. The most likely critic says the opposite:

> "It is worth noting in retrospect that, although the original "recombination system" with three pathways turned out to be too "conjugation-centric" to be universal, the general idea of separate recombinational pathways was fully validated (see 3.2. and 3.3.)."
> "Isolation of the secondary recombination-deficient mutations in the suppressed rec mutants naturally lead to the idea of several recombinational pathways in E. coli, the major one (RecBC) and two minor ones (RecE and RecF), the latter two normally suppressed in the wild type cells."
> "Subsequent biochemical analysis revealed the two-fold meaning of the recBC sbcA and recBC sbcBC alternative pathways: 1) alternative ways of producing 3′-overhangs at double-strand ends; 2) alternative ways of loading RecA protein on these overhangs. In other words, in the wild type cells, only one way of double-strand end processing and RecA loading at this end is available (controlled by RecBC), while the RecF pathway loads RecA at single-strand gaps."
— Kuzminov A, *EcoSal Plus* 2011, PMC4190071. **FULL TEXT** **[V2 — character-identical across two fetches]**

**Read precisely — it cuts both ways.** *Against* the classical scheme: RecE and RecF as historically named were "normally suppressed in the wild type cells" — they were made visible by **suppressor backgrounds** (*sbcA*, *sbcB sbcC*), and the original conjugation-based scheme is conceded to have been too narrow. *For* it: Kuzminov holds RecF-pathway function is real in wild-type cells, acting on single-strand gaps. **The classical framing was redefined by substrate, not abandoned.**

**The suppressor problem, stated by the source:**
> "Quite a different logic of extragenic suppression is exemplified by the *recBC sbcBC* recombination-proficient mutant combination. In this case, suppression is conferred by two unlinked mutations, *sbcB* (317) and *sbcC* (188) (or *sbcD* (92)), and the mechanism of it can be considered opposite to the *recBC sbcA* suppression: instead of activating an analogous function to compensate for the *recBC* defect, the *sbcBC* suppressors dramatically modify the metabolism of linear DNA in E. coli cells."

**RecFOR recast as a RecA-loading mediator rather than a parallel pathway:**
> "Here, we show that the concerted action of the RecFOR complex directs the loading of RecA protein specifically onto gapped DNA that is coated with single-stranded DNA binding (SSB) protein, thereby accelerating DNA strand exchange. ... Thus, the RecFOR complex is a structure-specific mediator that targets recombinational repair to ssDNA-dsDNA junctions."
— Morimatsu K, Kowalczykowski SC. *Mol Cell* 2003;11(5):1337–47. PMID 12769856. **ABSTRACT ONLY** **[V2] [PR on one fetch]**

> "RecA is also regulated by the action of other proteins. To date, these include the RecF, RecO, RecR, DinI, RecX, RdgC, PsiB, and UvrD proteins. ... The RecO and RecR, and possibly the RecF proteins, all facilitate RecA loading onto SSB-coated ssDNA."
— Cox MM. *Crit Rev Biochem Mol Biol* 2007. PMID 17364684. **ABSTRACT ONLY.** RecF/RecO/RecR are here enumerated as **RecA regulators alongside DinI, RecX, RdgC, PsiB, UvrD** — not as a parallel pathway.

**The boundary is demonstrably leaky — from a principal of the classical school:**
> "In *Escherichia coli*, at least two groups of proteins, or "recombination machines," can operate independently on broken DNA to produce a 3'-terminated single-stranded DNA filament coated with RecA protein and ready for synapsis with intact homologous DNA. Recent analyses of mutants lacking one or more of the activities required for presynaptic filament formation by one recombination machine demonstrate that **parts of the two normally separate machines can interchange** to initiate homologous recombination."
— Amundsen SK, Smith GR. "Interchangeable parts of the *Escherichia coli* recombination machinery." *Cell* 2003;112(6):741–4. PMID 12654241. **ABSTRACT ONLY** **[V2]**

Underlying experiment (in a background with **intact** *sbcB*/*sbcC*, so not a suppressor artifact): Ivančić-Baće I et al., *Genetics* 2003;163(2):485–94 — "RecFOR functions rescue the repair and recombination deficiency of the *recB1080* mutant," i.e. **RecFOR loading RecA at a double-strand end**, squarely across the classical boundary. **ABSTRACT ONLY.**
Also: Handa N, Morimatsu K, Lovett ST, Kowalczykowski SC, *Genes Dev* 2009;23:1234–45 — title verified: **"Reconstitution of initial steps of dsDNA break repair by the RecF pathway of E. coli"** — the "RecF pathway" doing double-strand break repair. **Full text NOT RETRIEVED.**

> "Together, the results suggest the existence of multiple pathways, perhaps overlapping, for the resolution or reversal of recombination intermediates created by RecA protein in post-replication gaps within the broader RecF pathway."
— Jain K, Wood EA, Cox MM. *PLoS Genet* 2021;17(12):e1009972. PMID 34936656. **ABSTRACT ONLY.**

**Explicit negative result, honestly flagged:** a targeted search of Kuzminov 2011's full text for "misnomer", "misleading", "artifact", "cryptic", "unfortunate", "terminology" returned nothing. **No retrieved author calls the pathway nomenclature a misnomer.** Because PMC full-text search is robots-blocked, this negative rests on one article's full text plus abstracts, not a corpus sweep. **Treat as provisional.**

### 7D. Other complications, itemised

1. **Dose regime / wavelength.** Ghosh & Orman 2024 use **302 nm UV-B**; everything classical uses **254 nm UV-C**. Not commensurable. That paper additionally shows a **20× internal inconsistency in its own stated irradiance between v1 and v2.**
2. **Repair time / liquid-holding recovery.** The retrieved corpus gives essentially no controlled information on this. Ghosh & Orman explicitly observe transience — Δ*recA* CFU "below the limit of detection… however, this was transient, as we observed a rapid increase in CFU levels (from 1 to 10^7) within 15 minutes of recovery." **A survival fraction in this system is a function of when you plate and how long you hold. This is not a nuisance parameter; it can move the readout by seven logs.**
3. **Strain background.** The corpus spans **AB1157** (Zahradka; Klimova & Sandler; Weel-Sneve), **SR108/W3110** (Courcelle), **MG1655 with Keio/BW25113 deletions** (Ghosh & Orman — a background mismatch within a single paper), unspecified K-12 (Shlaes 1972; Howard-Flanders 1969), and **RW584** (*lexA51*(Def) *recA730*, a constitutively SOS-on background — Kuban 2012). **Cross-paper comparison of survival fractions across these is not defensible.**
4. **"UV sensitivity" vs "loss of viability."** Multiple retrieved endpoints are *not* survival: **filamentation** (Friedman 2005), **division arrest via SulA** (Aksenov 1999), **mutation frequency** (Belov lineage), **strand-joining fluence thresholds** (Rothman & Clark 1977 — its "1 J/m2" is a strand-joining threshold, **not** a survival value; an easy trap), **I-SceI break survival** (Klimova & Sandler Table 1 — **not UV**), and **transient non-culturability** (Ghosh & Orman). Conflating any of these with colony-forming survival would corrupt an answer key.
5. **The epistatic vs synergistic call is genuinely dataset-dependent.** In the one table with real numbers (Zahradka 2002), *recBC* × Δ*ruvABC* reads as **epistatic** while *sbcB* × Δ*ruvABC* reads as **~100-fold synergistic**, on the same axes in the same paper. Meanwhile Shlaes 1972 reports *recA recB* = *recA* (epistatic) and Howard-Flanders 1969 reports *uvrA recA* at 40× (synergistic). **The system contains both outcomes, which is good for discrimination — but only two papers put singles and a double on the same quantitative axis at all.**
6. **Suppressor-background dependence.** Much of the *recF*-pathway evidence rests on *recBC sbcBC* strains. **A benchmark that scores "recF" as a redundant module is implicitly scoring a phenotype that is largely revealed only in a suppressed background.**

---

## ITEM 8 — COUNT: MECHANISMS THAT COULD CARRY A SETTLED LABEL FROM DIRECT EXPERIMENTAL EVIDENCE

Criterion applied: the mechanism must be (i) established as a distinct molecular module by primary evidence, AND (ii) have at least one retrieved, quantitative UV-survival observation attached to it, AND (iii) not have its pathway identity currently under reinterpretation.

### Settled — 5

| # | Mechanism | Label | Confidence | Direct survival evidence retrieved |
|---|---|---|---|---|
| 1 | **Nucleotide excision repair** (uvrABC) | **Essential** for UV survival | **High** | *uvrB* D37 = 5 ergs/mm² vs WT 230 (Shlaes 1972, ABSTRACT text); *uvrA* "much more sensitive" than triple-pol mutant (Courcelle 2005, figure); Δ*uvrA* "drastic reductions" (Ghosh & Orman, UV-B). Mechanism: Sancar Nobel Lecture; Kisker 2013 |
| 2 | **RecA-dependent recombinational repair** | **Essential** | **High** | D37 = 8 ergs/mm² (Shlaes 1972) and LD37 = 0.2 J/m² (Courcelle 2012) — **the only genotype with two independent groups**, though 4× apart |
| 3 | **RecBCD double-strand-end processing** | **Essential (partial)** | **Medium-High** | *recB recC* D37 = 30 ergs/mm² vs WT 230 (Shlaes 1972); *recB21 recC22* survival 0.046 @ 10 J/m² vs WT 0.89 (Zahradka 2002 Table 2, AB1157) |
| 4 | **RuvABC Holliday-junction resolution** | **Essential (partial), and a documented synergy partner** | **Medium-High** | Zahradka 2002 Table 2 — the only full singles-and-doubles quantitative table found. Δ*ruvABC* 0.051; *sbcB* Δ*ruvABC* 0.00039 (≈100× below multiplicative expectation) |
| 5 | **SOS transcriptional induction** (LexA/RecA circuit) | **Essential as a regulatory layer** | **Medium-High** | *lexA3*(Ind⁻) survival 13% @ 5 J/m² and 2.4% @ 15 J/m² vs WT 80% / 36% (Weel-Sneve 2008 Table 2). Circuit mechanism: Little 1981/1984/1991/1993 **[V2]** |

### Settled as a mechanism but NOT scorable as essential on survival — 2

| # | Mechanism | Label | Confidence | Evidence |
|---|---|---|---|---|
| 6 | **Translesion synthesis** (umuDC/polB/dinB) | **Near-spectator for survival; essential for mutagenesis** | **Medium** | *polB dinB umuDC* triple "no more sensitive… than the Pol V single mutant"; quadruple with *uvrA* ≈ *uvrA* alone (Courcelle 2005 — **figure-only, single group**). Δ*umuC*, Δ*umuD* "no significant change" (Ghosh & Orman, UV-B). Molecular identity: Tang 1999 **[V2]** |
| 7 | **Photoreactivation** (phr/photolyase) | **Conditionally essential (light) / NOT a clean spectator (dark)** | **Medium-Low** | Mechanism and 300–500 nm requirement: Sancar GB 1983 abstract; Sancar Nobel Lecture **[V2]**. Dark non-inertness: Yamamoto 1983; Kobayashi 1990; Sancar GB & Smith 1989 — **all ABSTRACT ONLY, all in *recA* and/or overexpression backgrounds.** The decisive experiment (chromosomal *phr* null, *uvr*⁺ *recA*⁺, dark) was **NOT RETRIEVED** |

### NOT settled — 2

| # | Mechanism | Why not |
|---|---|---|
| 8 | **RecFOR daughter-strand-gap pathway** | **ZERO quantitative UV survival numbers retrieved for *recF*, *recO*, or *recR* — single or double, from any source.** Evidence is ordinal only (Wang & Smith 1981). Pathway identity is actively reinterpreted: RecFOR as a RecA-loading mediator (Morimatsu & Kowalczykowski 2003; Cox 2007), boundary shown to be crossable (Amundsen & Smith 2003; Ivančić-Baće 2003; Handa 2009), and its classical definition rests on *sbcB sbcC* suppressor backgrounds |
| 9 | **UvrD / Pol I resynthesis step as a separable module** | No survival data separating it from NER was retrieved; Δ*uvrD* is grouped with Δ*uvrA* qualitatively (Ghosh & Orman) |

### Count

**5 mechanisms can carry a settled label from direct experimental evidence.** A sixth (TLS) is settled as a *mechanism* but its survival label is "near-spectator," which is a defensible key entry only from **one figure-only, single-group source**. A seventh (photoreactivation) is settled as a mechanism but its dark-condition label is **actively contested**. Two are not settled.

---

## THE SINGLE BIGGEST WEAKNESS

**The quantitative double-mutant survival data — the thing that makes this candidate attractive — is almost entirely unretrievable and almost entirely unreplicated.**

Across ~40 papers, exactly **two** sources put single mutants and a double mutant on the same quantitative axis (Shlaes 1972, abstract-only D37s; Zahradka 2002, Table 2 at one dose). Exactly **one** genotype (*recA* single) has quantitative data from two independent groups, and those two disagree by 4×. The famous *uvrA recA* synergy rests on **one sentence in one 1969 abstract**, with the comparator single-mutant value not stated in the paper (it was derived here by arithmetic from a "40 times" claim). **Zero** quantitative datapoints exist in the retrieved corpus for *recF*, *recO*, or *recR* — the very genes whose pathway status defines the classical redundancy claim.

The field's own operational definition of redundancy vs synergy (Item 2) was recovered cleanly and is genuinely usable. But it is a *rule*, and the *data* the rule would be applied to is published as semilog figures in paywalled and scanned mid-century journals. A key built from this candidate would be a key built on figure-digitized values from single groups — which is exactly the failure mode (headline numbers that are estimator or digitization artifacts) that this project's own methodology exists to prevent.

Compounding it, and nearly as serious: **no dynamical model in this system predicts survival fraction** (Item 6), so the modelling half of the candidate cannot be scored against the survival half without inventing an unvalidated mapping.

---

## APPENDIX: PRIORITY MANUAL-RETRIEVAL LIST

If this candidate is pursued, these must be opened by a human:
1. **Sargentini NJ, Gularte NP, Hudman DA. *Mutat Res* 2016;793–794:1–14** — "Screen for genes involved in radiation survival of E. coli and construction of a reference database." **NOTHING retrieved, not even an abstract.** Almost certainly the best single source for per-gene quantitative survival.
2. **Howard-Flanders P, Theriot L. *Genetics* 1966;53(6):1137–1150.** DOI 10.1093/genetics/53.6.1137 verified; OUP paywall ("This content is only available as a PDF"); PMC deposit has no text layer. **No number in this paper can currently be vouched for.**
3. **Howard-Flanders, Theriot & Stedeford 1969 *J Bacteriol* 97:1134–1141** — full text, for the strain table and the *uvrA6* single-mutant D37 that is currently only inferred.
4. **Belov OV et al. *J Theor Biol* 2009;261(3):388–395** — the only unread model that might couple SOS dynamics to a cell-level outcome.
5. **Horii Z, Clark AJ. *J Mol Biol* 1973;80(2):327–344** — the founding *recF*-pathway paper; a total retrieval loss.
6. **Lloyd RG, Porton MC, Buckman C. *Mol Gen Genet* 1988;212(2):317–324** — likely tabulates *recF, recJ, recN, recO, ruv* UV survival.
7. **Tseng Y-C, Hung J-L, Wang T-CV. *Mutat Res* 1994;315(1):1–9** — best candidate for *recF*/*recO*/*recR* numbers.
8. **Kuzminov 2011 EcoSal Plus, Table 2** — BioC does not serve table bodies; holds the direct quantitative evidence on whether *recF*/*recO*/*recR* matter in wild-type cells.
9. **Kuzminov 1999 MMBR body text** — the two-pathway claim currently rests on the abstract.
10. **Courcelle et al. 2001 *Genetics* 158:41–64** — PMC deposit is **SCANNED, NO TEXT LAYER**; the identities of the 26 regions and 17 additional sites were never obtained. *(Note: this is a microarray gene-expression paper, WT vs lexA1 — not a survival-curve paper.)*

### Citations that could NOT be verified and should NOT be used
- **"Howard-Flanders P, Boyce RP, Radiation Research ~1966"** — authorship, title, volume and pages **could not be confirmed at all**. Do not cite until someone confirms it exists as stated.
- **Game & Cox** (yeast epistasis-group formalization) — **NOT RETRIEVED**; citation details unverified.
- **"Kozlowski" SOS model** — **NOT FOUND**; probably a misattribution.
- **Walker GC 1984 *Microbiol Rev*** — four access routes failed. **Do not attribute any sentence to it.**
- **PMC2781627** ("DNA Repair Mechanisms: the Work of Aziz Sancar") — content retrieved but journal/authors/year **not confirmed**. Do not cite.

### Two near-miss fabrications, caught and discarded
A guessed PMCID (PMC17709) resolved to a paper on human factor VIIa, not Tang et al.; a guessed PMID (10488348) resolved to a South African gynaecology paper, not Wagner et al. Neither was used. Every citation above had its title and authors checked against a fetched page — **except** those explicitly listed in the "could NOT be verified" block immediately above.
