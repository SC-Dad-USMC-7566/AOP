# Benchmark Candidate Due Diligence — *S. cerevisiae* GAL (galactose utilisation) regulatory network

**Compiled:** 2026-07-25
**Provenance standard applied:** no fabricated citations, figure numbers, quantities or quotations. Every factual claim is either (i) backed by a verbatim passage I retrieved, with the URL fetched, or (ii) explicitly marked *inferred*, *contested*, or NOT RETRIEVED.

---

## 0. RETRIEVAL ENVIRONMENT AND ITS LIMITS (read first)

**Tooling.** `nimble --version` → `command not found`. The Nimble CLI is **not installed**, so no paywall/JS-capable retrieval was available. All fetching used `WebFetch` + `WebSearch`. `curl`/`wget`/Python fetching was not used (prohibited).

**A structural caveat that applies to EVERY quote in this document.** `WebFetch` converts a page to markdown and passes it through a small extraction model. I never saw raw HTML or PDF bytes. Quotes below are therefore *"as extracted by the fetch tool from the stated URL"*, not *"read by a human off a rendered page."* This is a real, non-trivial provenance weakening. Where a quote is load-bearing I say so, and where two fetches of the same URL disagreed I report the disagreement rather than picking a winner. **Do not promote any quantity in this document to canon without a human eyeball on the primary PDF.**

**Hosts that blocked retrieval during this session:**

| Host | Failure |
|---|---|
| `pmc.ncbi.nlm.nih.gov` | Intermittent Google reCAPTCHA; roughly half of attempts failed |
| `pubmed.ncbi.nlm.nih.gov` | reCAPTCHA throughout |
| `www.ebi.ac.uk` (Europe PMC REST) | HTTP 429 on every attempt, across the whole session — search capability lost |
| `api.openalex.org` | ROBOTS_DISALLOWED |
| `api.semanticscholar.org` | HTTP 429 |
| `science.org`, `pnas.org`, `jbc.org` | HTTP 403 |
| `journals.asm.org`, Wiley (`onlinelibrary.wiley.com`) | HTTP 403 |
| `sciencedirect.com`, `yeastgenome.org/search` | robots.txt disallowed |
| `nature.com` | Abstracts only (paywall) |

**WebSearch budget was exhausted (200/200) partway through.** Later retrieval ran on the **Crossref REST API** (`api.crossref.org`) as a search substitute plus direct DOI resolution. Crossref gave verified authorship/title/venue metadata but no full text. Several planned retrievals were abandoned for this reason and are listed in §10.

**Old-literature problem.** The two most-cited primary papers in this system — Bhat & Hopper 1992 (*Mol Cell Biol*) and Meyer et al. 1991 (*Mol Cell Biol*) — are pre-1994 MCB, held on PMC only as **scanned page images**. Confirmed by fetch: PMC364464 returns *"Only the abstract and reference list are present."* The NCBI ID converter returned **no PMCID at all** for either DOI. **Their body text is unreachable by any tool available here.** For both papers I have the abstract (Bhat & Hopper) or Crossref metadata only (Meyer).

---

## 1. CAUSAL STRUCTURE — the published wiring of the GAL switch

**Status: SOLID. Retrieved and quoted from three independent sources.**

### 1.1 Core Gal4 / Gal80 / Gal3 logic

> "The transcriptional activation function of the *Saccharomyces cerevisiae* GAL4 protein is modulated by the GAL80 and GAL3 proteins. In the absence of galactose, GAL80 inhibits the function of GAL4, presumably by direct binding to the GAL4 protein. The presence of galactose triggers the relief of the GAL80 block. The key to this relief is the GAL3 protein."

— Bhat PJ, Hopper JE (1992). "Overproduction of the GAL1 or GAL3 protein causes galactose-independent activation of the GAL4 protein: evidence for a new model of induction for the yeast GAL/MEL regulon." *Molecular and Cellular Biology* 12(6):2701–2707. DOI 10.1128/mcb.12.6.2701-2707.1992.
URL fetched: `https://pmc.ncbi.nlm.nih.gov/articles/PMC364464/`
**Retrieval status: ABSTRACT ONLY (body text is scanned images, unreachable).** Authorship independently confirmed via Crossref (`https://api.crossref.org/works?query.bibliographic=...`), which returns "Paike Jayadeva Bhat, James E. Hopper."

### 1.2 Mechanism of Gal80 inhibition and its relief

> "Gal80p binds to a 28-amino-acid region inside the second activation domain of Gal4p, AR2, thereby physically blocking interactions of the activation domain with the transcriptional machinery."

> "Upon binding to galactose and ATP, ScGal3p (or KlGal1p) starts releasing Gal4p from Gal80-mediated inhibition through direct interaction with Gal80p."

> "the cytosolic binding of Gal3p to monomeric Gal80p competes with Gal80 self-association, thereby reducing nuclear levels of dimeric Gal80p, the form involved in the inhibition of Gal4p."

— Rubio-Texeira M (2005). "A comparative analysis of the GAL genetic switch between not-so-distant cousins: *Saccharomyces cerevisiae* versus *Kluyveromyces lactis*." *FEMS Yeast Research* 5(12):1115.
URL fetched: `https://academic.oup.com/femsyr/article/5/12/1115/534945`
**Retrieval status: FULL TEXT RETRIEVED.**

### 1.3 Gal4 is pre-bound at UAS_GAL; induction is fast

> "The yeast transcriptional activator Gal4 localizes to UAS_GAL sites even in the absence of galactose but cannot activate transcription due to an association with the Gal80 protein. By 4 min after galactose addition, Gal4-activated gene transcription ensues. It is well established that this rapid induction arises through a galactose-triggered association between the Gal80 and Gal3 proteins that decreases the association of Gal80 and Gal4."

— Egriboz O, Jiang F, Hopper JE (2011). "Rapid GAL Gene Switch of *Saccharomyces cerevisiae* Depends on Nuclear Gal3, Not Nucleocytoplasmic Trafficking of Gal3 and Gal80." *Genetics* 189(3):825–836. DOI 10.1534/genetics.111.131839.
URL fetched: `https://academic.oup.com/genetics/article/189/3/825/6063844`
**Retrieval status: FULL TEXT / ABSTRACT + BODY PASSAGES RETRIEVED.**

### 1.4 Gal80 is a *purely negative* regulator, and Gal4 is not merely an anti-Gal80 device

> "Deletion of the GAL80 gene in a gal4 cell does not restore GAL cluster and MEL1 gene expression."
> "(i) the GAL80 protein is a purely negative regulator, (ii) the GAL80 protein does not mediate carbon catabolite repression, and (iii) the GAL4 protein is not simply an antagonizer of GAL80-mediated repression."
> "Carbon catabolite repression of the GAL cluster and MEL1 genes, which occurs at the level of transcription, is retained in the null mutant."

— Torchia TE, Hamilton RW, Cano CL, Hopper JE (1984). "Disruption of regulatory gene GAL80 in *Saccharomyces cerevisiae*: effects on carbon-controlled regulation of the galactose/melibiose pathway genes." *Molecular and Cellular Biology* 4(8):1521–1527.
URL fetched: `https://pmc.ncbi.nlm.nih.gov/articles/PMC368943/`
**Retrieval status: FULL TEXT RETRIEVED.**

### 1.5 GAL3 is also required to *maintain* the induced state

> "Either *GAL3* function or *GAL1-10-7* functions are therefore required for both the initiation and the maintenance of the induced state."

— Torchia TE, Hopper JE (1986), *Genetics* 113(2):229–246 (full citation in §2).

**Independent corroborating title (metadata verified, text NOT RETRIEVED):** Nogi Y (1986), "GAL3 gene product is required for maintenance of the induced state of the GAL cluster genes in *Saccharomyces cerevisiae*," *J Bacteriol* 165:101–106, DOI 10.1128/jb.165.1.101-106.1986 (via Crossref).

### 1.6 Glucose repression via MIG1 — RETRIEVED ONLY AS ABSTRACT

> "Mig1, but not Mig2, is required for repression of some other glucose-repressed genes, including the GAL genes."

— Lutfiyya LL, Iyer VR, DeRisi J, DeVit MJ, Brown PO, Johnston M (1998). "Characterization of Three Related Glucose Repressors and Genes They Regulate in *Saccharomyces cerevisiae*." *Genetics* 150:1377–1391.
URL fetched: `https://academic.oup.com/genetics/article/150/4/1377/6034625`
**Retrieval status: ABSTRACT ONLY.** The *mig1Δ mig2Δ* Results were NOT RETRIEVED.

The primary MIG1→GAL paper — Nehlin JO, Carlberg M, Ronne H (1991), "Control of yeast GAL genes by MIG1 repressor: a transcriptional cascade in the glucose response," *EMBO J* 10(11):3373–7 — was **NOT RETRIEVED**; it is known here only through a BioGRID curation record (`https://thebiogrid.org/interaction/161066/mig1-gal80.html`), which lists the MIG1–GAL80 interaction as "Phenotypic Enhancement," "Low" throughput.

**§1 verdict: the Gal4/Gal80/Gal3 wiring is SETTLED and quotably established.** The MIG1 layer is real but, in this retrieval, rests on one abstract plus a database record.

---

## 2. THE GAL1/GAL3 REDUNDANCY CLAIM — the load-bearing item

### 2.1 Headline: the claim as stated in the brief is **NOT confirmed as stated. It requires substantial amendment.**

The brief states: *"`gal3Δ` shows a LONG LAG before induction while `gal1Δ gal3Δ` cannot induce at all."*

What the retrieved primary literature actually establishes:

- **The `gal3Δ` long lag: CONFIRMED**, with quoted evidence, on multiple readouts.
- **The `gal1Δ gal3Δ` double mutant: I could NOT retrieve any primary passage describing a `gal1Δ gal3Δ` double deletion.** The canonical experiment behind this claim is a **`gal3 gal1 gal7` TRIPLE mutant**, and its readout is **MEL1 gene expression, not growth on galactose**. See §2.3. This is a material difference and it is the single most important finding in this report.

### 2.2 The gal3Δ long lag — CONFIRMED

**Primary source, on RNA kinetics:**

> "During the galactose adaptation period of a *Saccharomyces cerevisiae* strain bearing a naturally occurring *gal3* allele, we found a longer induction lag and slower rate of accumulation of *GAL10* and *MEL1* RNAs compared to wild-type strains."

> "An otherwise wild-type strain that bears a chromosomal *gal3* gene disruption mutation does not produce wild-type *GAL3* RNA and exhibits induction comparable to a strain bearing the naturally occurring *gal3*."

> "Since the strains bearing either the naturally occurring *gal3* allele or the *gal3* disruption (null) allele do induce…"

— Torchia TE, Hopper JE (1986). "GENETIC AND MOLECULAR ANALYSIS OF THE GAL3 GENE IN THE EXPRESSION OF THE GALACTOSE/MELIBIOSE REGULON OF *SACCHAROMYCES CEREVISIAE*." *Genetics* 113(2):229–246. DOI 10.1093/genetics/113.2.229. PMID 3013721, PMCID PMC1202836.
URL fetched: `https://academic.oup.com/genetics/article-abstract/113/2/229/5996959`
**Retrieval status: ABSTRACT ONLY (OUP serves this issue as abstract + PDF; PMC1202836 was reCAPTCHA-blocked on three attempts).** Authorship independently confirmed via Crossref.

**Named phenomenon, and the only retrieved statement of its duration:**

> "*S. cerevisiae* mutant strains lacking Gal3p suffer a substantially delayed induction of the *GAL* genes in galactose (phenomenon known as 'long-term adaptation'…"

— Rubio-Texeira 2005, `https://academic.oup.com/femsyr/article/5/12/1115/534945` — **FULL TEXT RETRIEVED**. (Quote is truncated mid-parenthesis exactly as returned.) **No duration is given in this source.**

> "Surprisingly, the *S. uvarum gal3* null mutant did not show the classic Long-Term Adaptation (LTA) phenotype of the *S. cerevisiae gal3* null mutant… Instead of a growth delay of multiple days, we observed a delay of only a few hours."

— Kuang MC, Hutchins PD, Russell JD, Coon JJ, Hittinger CT (2016). "Ongoing resolution of duplicate gene functions shapes the diversification of a metabolic network." *eLife* 5:e19027.
URL fetched: `https://elifesciences.org/articles/19027`
**Retrieval status: FULL TEXT RETRIEVED.**

**This is the only quantitative-ish lag figure I could retrieve: "a growth delay of multiple days" for *S. cerevisiae* gal3Δ, contrasted with "a few hours" for *S. uvarum* gal3Δ.** It is a comparative statement in a 2016 paper, not a primary measurement with error bars. **I could NOT retrieve any primary paper reporting a numeric lag time in hours for *S. cerevisiae* gal3Δ.** A targeted request to the same paper for "the number of days" returned ABSENT — the paper does not state a day count.

**Third readout — growth curves with GAL1 substituted at the GAL3 locus:**

> "Shown are growth curves of three strains of targeted replacements of the *GAL3* coding region by *GAL3* (*GAL3+*; the wild-type-like reference strain), *GAL1* (*GAL1+*) and deletion of *GAL3* (*Δgal3*)."
> "*GAL1+* strain showed a much longer lag phase than *GAL3+*."
> "13 h after transfer to 0.08% galactose, the cell density for *GAL1+* strain was 2.5-fold lower than for *GAL3+*."

— Lavy T, Yanagida H, Tawfik DS (2016). "Gal3 Binds Gal80 Tighter than Gal1 Indicating Adaptive Protein Changes Following Duplication." *Molecular Biology and Evolution* 33(2):472–477. DOI 10.1093/molbev/msv240.
URL fetched: `https://academic.oup.com/mbe/article/33/2/472/2579548`
**Retrieval status: FULL TEXT RETRIEVED.** Authorship confirmed via Crossref (note: Crossref lists year 2015 for the online record, the article page states 2016, volume 33 issue 2 pages 472–477 in both).

### 2.3 The double-mutant claim — WHAT THE LITERATURE ACTUALLY SAYS

The decisive retrieved passage:

> "A strain of genotype *gal3 gal1 gal7* is noninducible for *MEL1* gene expression, but this expression block is bypassed by overexpression of the *GAL4* gene or by deletion of the *GAL80* gene, either of which causes a constitutive phenotype."

> "In experiments in which the presence of either the plasmid-carried cloned *GAL3* gene or the plasmid-carried cloned *GAL1-10-7* genes allows *MEL1* induction of a *gal3 gal1 gal7* cell, we find that loss of the plasmid results in the shutoff of *MEL1* expression even when galactose is continuously present."

> "…the plasmid loss experiments indicate the existence of two completely independent induction initiation-maintenance pathways, one requiring *GAL3* function, the other requiring *GAL1-10-7* function."

— Torchia & Hopper 1986, *Genetics* 113(2):229–246, abstract, `https://academic.oup.com/genetics/article-abstract/113/2/229/5996959`. **ABSTRACT ONLY.**

**Read this carefully. Four things differ from the claim in the brief:**

1. **The strain is a triple mutant `gal3 gal1 gal7`, not a double `gal1 gal3`.** GAL7 is deleted too — presumably to avoid galactose-1-phosphate accumulation (see §3), but that is my *inference*; the abstract does not state the reason.
2. **The readout is `MEL1` expression (α-galactosidase / RNA), not growth on galactose.** These strains cannot grow on galactose regardless — `gal1` and `gal7` are both catabolic nulls. So "noninducible" here means *the regulatory switch does not fire*, which is a different measurement from *the organism does not persist*.
3. **The complementing unit is the plasmid-borne `GAL1-10-7` cluster, not `GAL1` alone.** The authors attribute the second pathway to "*GAL1-10-7* function," not to GAL1 specifically. **On this evidence alone, the second induction pathway is not resolved to GAL1.** Attributing it to GAL1 requires the separate evidence in §2.4.
4. The "two completely independent induction initiation-maintenance pathways" framing is the authors', and it is a **redundancy claim about induction**, not about catabolism.

**Verdict on the load-bearing item:** the *substance* of the redundancy claim (a GAL3-independent induction route exists, and it maps to the GAL1-10-7 locus) is **CONFIRMED by a retrieved primary abstract**. The *specific formulation in the brief* — a `gal1Δ gal3Δ` double that "cannot induce at all" — is **NOT RETRIEVED** and should be marked *inferred* until the Torchia & Hopper full text or a later double-mutant paper is read.

### 2.4 THE CONFOUND — GAL1's inducer function versus its catabolic function

**The confound is real, it is exactly as the brief describes, and — importantly — the literature was aware of it and addressed it.**

**Statement of the confound (retrieved):**

> "In *S. cerevisiae*, the *GAL1* and *GAL3* paralogs are descended from an ancestral bi-functional protein that was both a co-inducer and a galactokinase… They are almost completely subfunctionalized: ScerGAL3 lost its galactokinase activity and became a dedicated co-inducer, whereas ScerGAL1 lost most of its co-inducer activity but maintains galactokinase activity."

> "the *S. uvarum gal1* null mutant did not grow better in 2% galactose than it did without any carbon source, a phenotype similar to the *S. cerevisiae gal1* null mutant."

— Kuang et al. 2016, *eLife* 5:e19027, `https://elifesciences.org/articles/19027` — **FULL TEXT RETRIEVED.**

> "Although itself lacking galactokinase activity, ScGal3p has yet a 73% identity and 92% similarity to ScGal1p at the amino acid level."
> "In conditions of induction, Gal80p can bind both Gal3p and Gal1p with 1:1 stoichiometry. ScGal1p is bifunctional, presenting both galactokinase and ligand sensing activities. Its ligand sensor activity is, however, weaker (40-fold less efficient) than that of Gal3p, replacing it only in later stages."

— Rubio-Texeira 2005, **FULL TEXT RETRIEVED**. *Note: this is a review; the primary source for the 40-fold figure was **NOT RETRIEVED**.*

Independently, the same 40-fold figure appears in a modelling paper — and is the reason that model excludes Gal1p feedback entirely:

> "Gal1p is 40 times less effective than its homolog Gal3p at activating the GAL switch in response to galactose, we did not include its weak potential feedback role in the model."

— Ramsey SA, Smith JJ, Orrell D, Marelli M, Petersen TW, de Atauri P, Bolouri H, Aitchison JD (2006), *Nature Genetics* 38(9):1082–1087 (see §7.3 for retrieval caveats).

**So: `gal1Δ` fails to grow on galactose because it has no galactokinase, independent of any inducer role. Growth-on-galactose therefore CANNOT be used to test the inducer redundancy. This is a genuine, unavoidable confound.**

### 2.5 HOW THE LITERATURE DISENTANGLES IT — four independent strategies, all retrieved

**(a) Catalytically-dead ("galactokinaseless") GAL1 alleles — YES, this exists, and it is the direct answer to the brief's question.**

> "A galactose-independent mechanism of constitutivity is further indicated by the inducing properties of two newly created galactokinaseless alleles of GAL1."

> "Overproduction of the GAL1 protein (galactokinase) also causes constitutivity, consistent with the observations that GAL1 is strikingly similar in amino acid sequence to GAL3 and has GAL3-like induction activity."

— Bhat & Hopper 1992, *MCB* 12(6):2701–2707, abstract, `https://pmc.ncbi.nlm.nih.gov/articles/PMC364464/`. **ABSTRACT ONLY.**

**This is the cleanest disentanglement in the literature: Gal1p variants with the kinase activity destroyed still induce.** Caveat that must not be dropped: this was demonstrated in an **overproduction / constitutivity** assay, *not* in a lag-rescue-of-`gal3Δ` assay at native expression. It shows that Gal1p's inducer function is separable from its kinase function; it does **not** by itself show that native-level catalytically-dead Gal1p rescues the `gal3Δ` lag.

**(b) GAL1 driven from the GAL3 promoter/locus (promoter swap).** Lavy et al. 2016 replaced "the *GAL3* coding region by … *GAL1*" and measured growth. This decouples GAL1's inducer contribution from its own native regulation, though *not* from its kinase activity. Result quoted in §2.2: much longer lag, 2.5-fold lower density at 13 h in 0.08% galactose.

**(c) Cross-species complementation with a naturally bifunctional GAL1.** Metadata verified via Crossref:

Meyer J, Walker-Jonah A, Hollenberg CP (1991). "Galactokinase encoded by GAL1 is a bifunctional protein required for induction of the GAL genes in *Kluyveromyces lactis* and is able to suppress the gal3 phenotype in *Saccharomyces cerevisiae*." *Molecular and Cellular Biology* 11:5454–5461. DOI 10.1128/mcb.11.11.5454-5461.1991.
**Retrieval status: TITLE + AUTHORSHIP VERIFIED VIA CROSSREF ONLY. FULL TEXT AND ABSTRACT NOT RETRIEVED** — `journals.asm.org` returned 403; the NCBI ID converter returned **no PMCID** for this DOI. The title alone asserts suppression of the gal3 phenotype, but **I have read no passage from this paper and no data from it.** Treat the suppression claim as *asserted-by-title*, not verified.

**(d) Removing GAL7 from the test strain.** Torchia & Hopper's `gal3 gal1 gal7` genotype removes the Leloir step whose loss causes Gal-1-P accumulation. That this was the *purpose* is my **inference** — not stated in the retrieved abstract.

**(e) Evolutionary/comparative dissection.** Hittinger CT, Carroll SB (2007). "Gene duplication and the adaptive evolution of a classic genetic switch." *Nature* 449:677–681. **ABSTRACT ONLY** (`https://www.nature.com/articles/nature06151`):

> "The genetic switch controlling the yeast galactose use pathway includes two paralogous genes in *Saccharomyces cerevisiae* that encode a co-inducer (*GAL3*) and a galactokinase (*GAL1*). These paralogues arose from a single bifunctional ancestral gene as is still present in *Kluyveromyces lactis*."
> "…here we assess the effects of precise replacement of coding and non-coding sequences on organismal fitness."

**(f) Biophysical separation.** Lavy, Yanagida & Tawfik 2016 measured binding directly, sidestepping growth entirely:

> "The equilibrium dissociation constants (*Kd*) of the Gal80 complexes were found to be 44 ± 15 nM with Gal3 and 490 ± 47 nM with Gal1. These values indicate approximately 10-fold higher affinity."
> "Gal3 (at 13–200 nM concentrations), and Gal1 (90–1,500 nM) were allowed to flow over immobilized Gal80"

**Note a genuine tension worth flagging: the biophysics gives ~10-fold (Kd), the physiology/reviews give ~40-fold (inducer efficiency). These are different quantities measured differently and need not agree, but a benchmark answer key must not treat them as the same number.**

### 2.6 Summary table for item 2

| Sub-claim | Status | Best evidence |
|---|---|---|
| GAL1 and GAL3 are WGD paralogs, ~73% identical | CONFIRMED | Rubio-Texeira 2005 (full text) |
| GAL3 is the primary/dedicated co-inducer | CONFIRMED | Kuang 2016 (full text) |
| gal3Δ shows a long induction lag ("long-term adaptation") | CONFIRMED | Torchia & Hopper 1986 (abstract); Kuang 2016 (full text) |
| That lag is "multiple days" | RETRIEVED but weak — one comparative sentence in a 2016 paper; **no primary numeric measurement retrieved** | Kuang 2016 |
| GAL1 substitutes for GAL3 as inducer | CONFIRMED IN PRINCIPLE, not resolved to GAL1 alone in the canonical experiment | Bhat & Hopper 1992 (abstract); Lavy 2016 (full text); Meyer 1991 (title only) |
| **`gal1Δ gal3Δ` double cannot induce at all** | **NOT RETRIEVED as stated.** Canonical experiment is `gal3 gal1 gal7` triple, readout MEL1 expression | Torchia & Hopper 1986 (abstract) |
| GAL1's kinase function is separable from its inducer function | CONFIRMED | Bhat & Hopper 1992 (abstract): "galactokinaseless alleles of GAL1" |
| gal1Δ fails to grow on galactose for a catabolic reason unrelated to induction | CONFIRMED | Kuang 2016 (full text) |

---

## 3. ESSENTIAL COMPONENTS — which single deletions abolish growth on galactose

**Status: WEAK. This is the second-biggest evidentiary hole in this candidate.** Every one of the four target genes traces, in this retrieval, to **SGD database annotations whose underlying primary citations could not be retrieved** (SGD's annotation *tables* render client-side and never loaded; the SGD backend API is robots-blocked).

### 3.1 gal4Δ

> "Non-essential gene in reference strain S288C; null mutants cannot utilize galactose, and show increased resistance to antimalarial quinine, caffeine, and many common chemicals…"

— SGD, GAL4 (YPL248C), `https://www.yeastgenome.org/locus/S000006169/phenotype`. **DATABASE ANNOTATION; primary citations NOT RETRIEVED.**

Indirect primary support (both full-text retrieved), establishing that Gal4 is strictly required for GAL/MEL expression:
- Torchia et al. 1984: *"Deletion of the GAL80 gene in a gal4 cell does not restore GAL cluster and MEL1 gene expression."* (`https://pmc.ncbi.nlm.nih.gov/articles/PMC368943/`)
- Suzuki Y, Nogi Y, Abe A, Fukasawa T (1988), *MCB* 8:4991–4999: *"Deficiency of Gal4, the major transcription activator for GAL1,7,10, was epistatic over the gal11 defect."* (`https://pmc.ncbi.nlm.nih.gov/articles/PMC365593/`)

**Label: essential (regulatory). Confidence MEDIUM-HIGH.** The *expression* requirement is primary-sourced; the *growth* claim is database-only.

### 3.2 gal1Δ

> "Non-essential gene in reference strain S288C; null mutant defective in utilizing galactose as a carbon source"
> "Galactokinase; phosphorylates alpha-D-galactose to alpha-D-galactose-1-phosphate in the first step of galactose catabolism… GAL1 has a paralog, GAL3, that arose from the whole genome duplication"

— SGD, GAL1 (YBR020W), `https://www.yeastgenome.org/locus/GAL1`. **DATABASE ANNOTATION.** Note the hedged wording "defective in utilizing," not "abolished."

**Primary-literature support (full text):** Kuang et al. 2016 — *"the S. uvarum gal1 null mutant did not grow better in 2% galactose than it did without any carbon source, a phenotype similar to the S. cerevisiae gal1 null mutant."* **Label: essential (catabolic). Confidence MEDIUM-HIGH.**

### 3.3 gal7Δ — essential, BUT the mechanism is contested

> "Non-essential gene in reference strain S288C; null mutant cannot utilize galactose **and grows more slowly in the presence of galactose**; in large-scale studies, null mutant shows reduced competitive fitness in minimal or galactose-containing medium but increased fitness in rich medium containing ethanol…"

— SGD, GAL7 (YBR018C), `https://www.yeastgenome.org/locus/GAL7`. **DATABASE ANNOTATION.**

The "and grows more slowly in the presence of galactose" clause is the galactosemia phenotype: **loss-of-function and toxic-intermediate accumulation are BOTH present, not alternatives.** And the field's own attribution is hedged:

> "cells are unable to grow using galactose in strains lacking galactose-1-phosphate uridyl transferase (GAL7), **presumably** due to the accumulation of galactose-1-phosphate"
> "Previous models of galactosemia in yeast have used mutations of GAL7 that exhibit functional consequences only when cells are grown on galactose"
> [on their alternative system] it "exhibits galactosemic phenotypes even in the presence of glucose. This isolates the accumulation of galactose-1-phosphate from a requirement for galactose metabolism"
> "Despite widespread observations of sugar-phosphate toxicity, the molecular mechanism behind these observations remains unclear"

— Gibney PA, Schieler A, Chen JC, et al. (2018). "Common and divergent features of galactose-1-phosphate and fructose-1-phosphate toxicity in yeast." *Molecular Biology of the Cell* 29.
URL fetched: `https://pdfs.semanticscholar.org/1417/f5496a1ec30eefb45fc9cc2de7efa45dbe6d.pdf` (publisher page returned 403). **FULL TEXT RETRIEVED (author-accessible PDF).** Author list beyond "et al." NOT FULLY VERIFIED.

**These authors built a separate constitutive-overexpression system precisely because `gal7Δ` confounds toxicity with loss of metabolic function.** So the *mechanism* in gal7Δ is not cleanly established by that mutant alone.

Supporting epistasis on a stress readout (not growth):
> "The deletion of the galactokinase gene blocked the galactose-dependent UPR activation in both the lithium-induced and the *gal7Δ* mutant models of galactosemia."
> "Galactose also induced the splicing of HAC1 mRNA in the *gal7Δ* strain, but not in the control strain"
— *Disease Models & Mechanisms* 7(1):55, 2014, `https://journals.biologists.com/dmm/article/7/1/55/19991/...`. **FULL TEXT RETRIEVED.** Full author list NOT VERIFIED.

**Label: essential. Confidence MEDIUM. Mechanism: CONTESTED.**

### 3.4 gal10Δ

> "Non-essential gene in reference strain S288C; null mutant displays small defect in vacuolar fragmentation, defective endocytosis, slow growth, and is unable to utilize galactose as a carbon source; heterozygous null is haploproficient"
> "UDP-glucose-4-epimerase; catalyzes interconversion of UDP-galactose and UDP-D-glucose in galactose metabolism…"

— SGD, GAL10 (YBR019C), `https://www.yeastgenome.org/locus/GAL10`. **DATABASE ANNOTATION.**

**Three honest negatives:** partial/residual growth — NOT RETRIEVED (no evidence either way). A bypass around the epimerase — NOT RETRIEVED. gal10Δ galactose-*sensitivity* — NOT RETRIEVED; unlike GAL7, SGD's GAL10 summary contains **no** "grows more slowly in the presence of galactose" clause. **Do not transfer the gal7Δ toxicity story to gal10Δ by analogy.** The two most on-point sources (JBC "Relationship between UDP-Galactose 4′-Epimerase Activity and Galactose Sensitivity in Yeast"; *Mol Genet Metab* 2007 "Distinct roles of galactose-1P in galactose-mediated growth arrest of yeast deficient in GALT and GALE") were both blocked.

**gal10Δ also has galactose-independent pleiotropy** (vacuolar fragmentation, endocytosis, slow growth) consistent with UDP-galactose being needed for glycosylation. **This makes gal10Δ a poor clean test of carbon-source essentiality. Label: essential. Confidence LOW-MEDIUM.**

### 3.5 gal80Δ — the clean negative control

> "Both *S. cerevisiae* and *K. lactis gal80* mutants show constitutive expression of the *GAL* genes to levels even higher than those of a fully-induced wild-type strain…"
— Rubio-Texeira 2005, **FULL TEXT RETRIEVED.**

> "Non-essential gene in reference strain S288C; null mutant shows decreased growth rate of newly germinated spores… **decreased growth in the absence of galactose**, decreased chronological lifespan, sensitivity to UV, formamide, and heat"
— SGD, GAL80, `https://www.yeastgenome.org/locus/GAL80/phenotype`. **DATABASE ANNOTATION.**

The annotated cost is *in the absence of* galactose — the price of constitutivity. **No galactose-growth defect. This is a clean dissociation: regulatory-state change without loss of the metabolic capability.**

### 3.6 PGM2 — flagged CONTESTED, do not use

SGD says the null "cannot grow on galactose," but PGM2 has a WGD paralog PGM1, and the only supporting evidence retrievable was from *S. boulardii* with a truncating point mutation, not S288C with a deletion (`https://journals.asm.org/doi/full/10.1128/aem.02858-17`, full text retrieved). A *Frontiers in Plant Science* paper (`https://www.frontiersin.org/journals/plant-science/articles/10.3389/fpls.2020.00167/full`, full text retrieved) characterises and *criticises* the yeast evidence: *"However, Gal-1P was not directly determined. Instead of Gal-1P galactose uptake and growth rate of yeast cultures were measured."* **Exclude from any answer key.**

---

## 4. INERT / SPECTATOR COMPONENTS

### 4.1 gal2Δ — a CONDITIONAL spectator. This is the strongest finding in §4.

> "*Gal2* deletion mutants grow very poorly on media containing galactose as a sole carbon source."
> "Such a role has recently been ascribed to the glucose transporters which have been demonstrated to transport galactose in very small amounts."
> "the Gal2p transporter is able to transport glucose with high capacity and high affinity (*K*m(glucose) about 2 mM)."

— Boles E, Hollenberg CP (1997). "The molecular genetics of hexose transport in yeasts." *FEMS Microbiology Reviews* 21(1):85.
URL fetched: `https://academic.oup.com/femsre/article/21/1/85/551032`
**Retrieval status: FULL TEXT RETRIEVED — and independently re-fetched with a differently worded prompt, returning character-identical strings.** Highest-confidence retrieval in §4.

Context: the second quote appears in a discussion of how galactose must initially enter the cell *independently of Gal2p* in order to induce *GAL2* in the first place — the redundancy is required for the switch to bootstrap.

> "Non-essential gene in reference strain S288C; null mutant is unable to grow on low concentrations of galactose but can grow on high galactose concentrations **as long as cells are respiratory-competent**; null mutation confers resistance to toxaphene; overexpression causes slow growth"
— SGD, GAL2 (YLR081W), `https://www.yeastgenome.org/locus/GAL2`. **DATABASE ANNOTATION; re-fetched twice, character-identical.**

**Flag an internal contradiction in SGD:** its *description* field says GAL2 is "required for utilization of galactose" while its *phenotype* field says the null "can grow on high galactose concentrations." The phenotype field is the operative claim; the description is a legacy simplification. **Any answer key built from SGD descriptions would score this wrong.**

**Answer: gal2Δ retains growth on galactose, conditionally — at high galactose and with respiratory competence. Uptake redundancy is real. Label: redundant/conditional-inert. Confidence MEDIUM-HIGH. No quantitative rate or lag for a gal2Δ single mutant was retrieved.**

### 4.2 The scale of uptake redundancy

> "the hexose transporter genes were sequentially deleted in 17 deletions rounds in the following order from first to last: *HXT15*, *HXT16*, *HXT13*, *HXT14*, *HXT12*, *HXT9*, *HXT11*, *HXT10*, *HXT8*, *HXT4*-*1*-*5*, *HXT2*, *HXT3*-*6*-*7*, *GAL2*, *STL1*, *AGT1*, *MPH2* and *MPH3*"
> "The resulting strain, named EBY.VW4000, was also unable to utilize fructose, galactose and mannose, but its growth on maltose was not impaired."

— Solis-Escalante D, et al. (2015). "The genome sequence of the popular hexose-transport-deficient *Saccharomyces cerevisiae* strain EBY.VW4000 reveals LoxP/Cre-induced translocations and gene loss." *FEMS Yeast Research* 15(2):fou004.
URL fetched: `https://academic.oup.com/femsyr/article/15/2/fou004/534426`
**Retrieval status: FULL TEXT RETRIEVED — but this is a SECONDHAND restatement of Wieczorke et al. 1999 (*FEBS Lett*), which returned 403 and is NOT RETRIEVED.** Also note the strain is not clean: the paper's own title flags "LoxP/Cre-induced translocations and gene loss."

### 4.3 CONTESTED: do HXTs actually carry galactose?

Two retrieved full texts disagree:
- **Yes, weakly:** Boles & Hollenberg 1997 — "demonstrated to transport galactose in very small amounts."
- **Hxt1 specifically, no:** *"the human Glut1 transports glucose, galactose but not fructose [47], whereas the yeast Hxt1 transports glucose and fructose, but not galactose"* — "Assessing Glucose Uptake through the Yeast Hexose Transporter 1 (Hxt1)," *PLOS ONE* 10(3):e0121985, 2015, `https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0121985`. **FULL TEXT RETRIEVED.**
- **Older review, restrictive:** *"Galactose transport has only one natural substrate, d-galactose, and is encoded by the gene GAL2."* — Lagunas R (1993), *FEMS Microbiol Rev* 10(3-4):229, `https://academic.oup.com/femsre/article/10/3-4/229/497148`. **FULL TEXT RETRIEVED.**

**Reconciliation (inferred, not quoted): Hxt1 specifically does not carry galactose, but some HXT family member(s) do, at low capacity.** The strongest *functional* evidence remains §4.2: you must delete GAL2 *and* all 17 HXTs to abolish galactose utilisation.

### 4.4 Other spectators

- **GAL80** — best-supported spectator for growth on galactose (§3.5). Deleting it changes the regulatory state without costing galactose growth. **Confidence MEDIUM-HIGH.**
- **GAL3** — a *kinetic* spectator only: gal3Δ eventually grows (§2.2). **Confidence HIGH for "not essential," but this is a lag phenotype, not inertness.**
- **MEL1** — secreted α-galactosidase, "required for catabolic conversion of melibiose to glucose and galactose" (SGD, `https://yeastgenome.org/locus/S000029662`). A co-regulated regulon member irrelevant to galactose-as-sole-carbon-source. **SGD reports NO phenotype data for MEL1, and whether MEL1 is even present in S288C was NOT RETRIEVED. Confidence LOW — do not score.**
- **MIG1** — under galactose-only conditions with no glucose, MIG1 should be a spectator. **This is inference; I retrieved no galactose-sole-carbon-source growth measurement for mig1Δ.**

### 4.5 A hidden variable worth naming

Both gal2Δ and gal3Δ carry the identical SGD qualifier "unless/as long as cells are respiratory-competent." **A petite derivative would score both genes as ESSENTIAL when they are not.** I have no quoted mechanism for this; flagged as an observation.

---

## 5. COMBINATORIAL / EPISTASIS DATA

### 5.1 The genome-scale data (Costanzo et al.) is **near-useless for this system**, and the reason is quotable

Citations verified via Crossref:
- Costanzo M et al. (2010). "The Genetic Landscape of a Cell." *Science* 327(5964):425–431. DOI 10.1126/science.1180823. **53 authors**, Costanzo first, Boone last. (`https://api.crossref.org/works/10.1126/science.1180823`) — **METADATA ONLY; full text NOT RETRIEVED (science.org 403).**
- Costanzo M et al. (2016). "A global genetic interaction network maps a wiring diagram of cellular function." *Science* 353(6306):aaf1420. DOI 10.1126/science.aaf1420. **54 authors.** Main body retrieved via `https://pmc.ncbi.nlm.nih.gov/articles/PMC5661885/` — **FULL TEXT RETRIEVED (MAIN BODY ONLY; Methods absent from the PMC deposit).**

> "a global genetic interaction network resulting from the combination of the NxN, ExN, and ExE networks was generated from analysis of ~23 million double mutants encompassing 5,416 different genes"

**THE CRITICAL POINT — the carbon source. The Costanzo papers' own Methods text is NOT RETRIEVED** (science.org 403; the Boone lab hosts Materials & Methods only inside a 500 MB `SOM.zip`; the PMC deposit omits Methods). What *was* retrieved is the Boone lab's own SGA protocol, which these screens cite:

> Double-mutant selection plate: "Add 1.7 g yeast nitrogen base w/o amino acids or ammonium sulfate, 1 g MSG, 2 g amino-acids supplement powder mixture (DO – His/Arg/Lys), 100 mL water… Combine autoclaved solutions, **add 50 mL 40% glucose**, cool medium to ~65o C, add 0.5 mL canavanine…"
> Haploid selection: "…**add 50 mL 40% glucose**, cool medium to ~65o C, add 0.5 mL canavanine (50 mg/L) and 0.5 mL thialysine (50 mg/L)…"
> YEPD: "After autoclaving, **add 50 mL of 40% glucose solution**…"

— Tong AHY, Boone C. "Synthetic Genetic Array (SGA) Analysis in *Saccharomyces cerevisiae*." *Methods in Molecular Biology*, Humana Press. `https://boonelab.ccbr.utoronto.ca/pdf/SGA_protocol_final.pdf` — **FULL TEXT RETRIEVED.**

Corroborated twice more: Kuzmin E, Rahman M, VanderSluis B, Costanzo M, Myers CL, Andrews BJ, Boone C (2021), τ-SGA, *Nature Protocols* (`https://pmc.ncbi.nlm.nih.gov/articles/PMC9127509/`, full text) — *"Supplement with 2% glucose (w/v), 50 μg/ml of canavanine and 50 μg/ml thialysine."*; and *Cold Spring Harbor Protocols* 2016 pdb.rec089458 (`https://cshprotocols.cshlp.org/content/2016/4/pdb.rec089458.full?text_only=true`, full text) — SDMSG medium includes "50 mL glucose solution (40%, sterile)."

**50 mL of 40% glucose into ~1 L = 2% (w/v) glucose. No galactose, raffinose, glycerol or ethanol appears in any recipe.**

**Consequence (inference, clearly labelled): under 2% glucose the GAL regulon is catabolite-repressed and Gal4 is inactive, so GAL structural-gene deletions are phenotypically near-silent and their SGA scores carry essentially no information about galactose utilisation.**

**And the field says so itself — this is the best quote in §5:**

> "It has shown previously that deletion of *GAL4* suppresses the slow-growth phenotype associated with *gal80*Δ (Ideker et al, 2001)… and this is a relationship we successfully detected in our E-MAP."
> "**We did not detect an interaction between *GAL4* and *HTZ1* (or SWR-C) in the medium we used lacking galactose as Gal4 is not functional in these circumstances.**"
> "By generating double mutants for 151 predicted STFs, as well as 172 components of the general transcriptional machinery… we collected genetic interaction data for 48 391 pairs of genes."

— Zheng J, Benschop JJ, Shales M, Kemmeren P, Greenblatt J, Cagney G, Holstege F, Li H, Krogan NJ (2010). "Epistatic relationships reveal the functional organization of yeast transcription factors." *Molecular Systems Biology* 6:420.
URL fetched: `https://pmc.ncbi.nlm.nih.gov/articles/PMC2990640/` — **FULL TEXT RETRIEVED.**

**That is a published, quotable admission of a false negative caused by the carbon source.** (The Zheng E-MAP's own medium is NOT RETRIEVED; Ideker et al. 2001 is NOT RETRIEVED — quoted here only as it appears inside Zheng et al.)

**Presence of GAL genes in the SGA arrays:** only **GAL2** confirmed — BioGRID record for GAL2 × BCS1 from Costanzo 2016: "Negative Genetic Interaction," "High Throughput (SGA)," "SGA score = -0.1211 (P-value = 0.01207)," "Phenotype measure: colony size" (`https://thebiogrid.org/interaction/2150276`). **GAL1/3/4/7/10/80 and MIG1 individually: NOT RETRIEVED** (SGD and BioGRID gene pages render interaction tables client-side). Their presence is a strong inference (all non-essential, and the array is "the corresponding *kanMX*-marked deletion mutant collection") but it is an **inference**.

**TheCellMap.org** is reachable (`https://thecellmap.org/`, `https://thecellmap.org/yeast/`, both fetched) and exposes a "Gene mutant" query field; the companion paper (Ušaj M et al. 2017, *G3* 7(5):1539–1549, `https://academic.oup.com/g3journal/article/7/5/1539/6028278`, full text) describes querying "by inputting the systematic or common gene name(s) into the search window" and holdings of "∼550,000 negative and ∼350,000 positive genetic interactions." **I did NOT execute a GAL query** — it is a client-side JS app WebFetch cannot drive.

**Costanzo M, Hou J, Messier V, … Boone C, Andrews B (2021), "Environmental robustness of the global yeast genetic interaction network," *Science*** (`https://pmc.ncbi.nlm.nih.gov/articles/PMC9132594/?report=classic`, full text, Methods thin) DID include a non-glucose condition:

> "we examined 14 diverse conditions and scored 30,000 functionally representative yeast gene pairs for dynamic, differential interactions"
> "**an alternative carbon source**, osmotic and genotoxic stress, and treatment with 11 bioactive compounds"
> "One copy was grown in the **standard SGA reference condition**, while the two other copies were each grown in different conditional media"

**The identity of that alternative carbon source is NOT RETRIEVED** — it lives in `Costanzo_et_al_Data_File_1_Conditions_Strains_Fitness.xlsx` on Dryad (`https://datadryad.org/dataset/doi:10.5061/dryad.3r2280gfd`), an .xlsx not openable with permitted tools. **DO NOT ASSUME IT IS GALACTOSE.** This is the highest-value open thread in §5.

### 5.2 Targeted double mutants that DO exist

| Pair | Result | Source | Status |
|---|---|---|---|
| `gal4` × `gal80Δ` | gal4 epistatic to gal80: *"Deletion of the GAL80 gene in a gal4 cell does not restore GAL cluster and MEL1 gene expression."* | Torchia, Hamilton, Cano & Hopper 1984, *MCB* 4(8):1521–1527, `https://pmc.ncbi.nlm.nih.gov/articles/PMC368943/` | **FULL TEXT** |
| `gal4Δ` × `gal80Δ` (fitness) | gal4Δ suppresses gal80Δ slow growth; detected in an E-MAP | Zheng et al. 2010 (quoting Ideker et al. 2001) | **FULL TEXT of Zheng; Ideker NOT RETRIEVED** |
| `gal4` × `gal11` | *"Deficiency of Gal4… was epistatic over the gal11 defect."* Also *"Strains bearing a gal11 mutation synthesize these enzymes at 10 to 30% of the wild-type level in the induced state."* | Suzuki, Nogi, Abe & Fukasawa 1988, *MCB* 8:4991–4999, `https://pmc.ncbi.nlm.nih.gov/articles/PMC365593/` | **FULL TEXT** |
| `gal3 gal1 gal7` triple | Noninducible for MEL1; bypassed by GAL4 overexpression or gal80Δ | Torchia & Hopper 1986 | **ABSTRACT** |
| `mig1` × `gal80` | "Phenotypic Enhancement," low throughput | BioGRID curation of Nehlin et al. 1991 | **DATABASE RECORD ONLY** |
| `mig1Δ mig2Δ` | Mig1 but not Mig2 required for GAL repression | Lutfiyya et al. 1998 | **ABSTRACT ONLY** |
| `gal2Δ` + 17 `hxt` | Abolishes galactose utilisation (EBY.VW4000) | Solis-Escalante 2015 restating Wieczorke 1999 | **SECONDHAND** |

**NOT RETRIEVED:** gal3Δ gal80Δ; quantitative gal4Δ gal80Δ; snf1Δ, reg1Δ, hxk2Δ combinations; Hillenmeyer et al. 2008; Szappanos et al. 2011.

### 5.3 The one good galactose-specific fitness dataset

> "The complete collection was grown in environments consisting of one of four possible carbon sources paired with one of seven nitrogen sources, for a total of 28 different well-defined metabolic environments."
> "Carbon sources included glucose, **galactose**, ribose, and glycerol."
> "We define a galactose-sensitive gene for this purpose as having a significant fitness defect in at least four of our seven galactose conditions and we obtain a list of 565 such genes."

— VanderSluis B, Hess DC, Pesyna C, Krumholz EW, Syed T, Szappanos B, Nislow C, Papp B, Troyanskaya OG, Myers CL, Caudy AA (2014). "Broad metabolic sensitivity profiling of a prototrophic yeast deletion collection." *Genome Biology* 15(4):R64.
URL fetched: `https://pmc.ncbi.nlm.nih.gov/articles/PMC4053978/` — **FULL TEXT RETRIEVED.**

**Whether GAL1/2/3/4/7/10/80 appear in that 565-gene list was NOT RETRIEVED. One targeted follow-up would settle it and would be the single most valuable addition to this dossier.**

Giaever et al. 2002 *Nature* 418:387 also assayed galactose — *"genes are necessary for optimal growth under six well-studied conditions: high salt, sorbitol, **galactose**, pH 8, minimal medium and nystatin treatment"* (`https://www.nature.com/articles/nature00935`) — **ABSTRACT ONLY**; medium composition and which GAL genes scored are NOT RETRIEVED.

---

## 6. MEASURED PERSISTENCE OUTCOME — what is measured, in what units

**Honest headline: every readout in this system is a GROWTH or GENE-EXPRESSION measure. NOT ONE is a survival measure.** No retrieved source measures viability, death rate, colony-forming units after a lethal challenge, or time-to-extinction. If the benchmark's persistence functional is survival, this candidate does not supply it.

| Readout | Units / method | Source (retrieval status) |
|---|---|---|
| Growth curve on galactose; lag phase; cell density | Culture density over time; e.g. *"13 h after transfer to 0.08% galactose, the cell density for GAL1+ strain was 2.5-fold lower than for GAL3+"*; *"GAL1+ strain showed a much longer lag phase than GAL3+"* | Lavy et al. 2016 MBE (**FULL TEXT**) |
| Growth delay on galactose | Qualitative time scale: *"a growth delay of multiple days"* vs *"a delay of only a few hours"*; *"did not grow better in 2% galactose than it did without any carbon source"* | Kuang et al. 2016 eLife (**FULL TEXT**) |
| Growth medium (methods) | *"Strains were first streaked on YPD (10 g/L yeast extract, 20 g/L peptone, 20 g/L glucose, 18 g/L agar) plates from frozen glycerol stocks. Next, a single colony of each strain was cultured in synthetic complete (SC) medium plus 0.2% glucose…"*; *"Strains were cultured in SC + 2% galactose"* | Kuang et al. 2016 eLife (**FULL TEXT — but the methods extraction TERMINATED MID-SENTENCE; OD wavelength, instrument, and the lag/growth-rate computation were NOT RETRIEVED**) |
| Induction lag + RNA accumulation rate | *"a longer induction lag and slower rate of accumulation of GAL10 and MEL1 RNAs"* (Northern blot) | Torchia & Hopper 1986 (**ABSTRACT**) |
| Enzyme activity + RNA level | *"Enzyme activities and RNA levels for the GAL cluster and MEL1 genes were constitutively expressed…"* | Torchia et al. 1984 (**FULL TEXT**) |
| Induction kinetics, minutes | *"By 4 min after galactose addition, Gal4-activated gene transcription ensues."* | Egriboz et al. 2011 (**FULL TEXT**) |
| Fraction of induced cells / bimodality | Flow cytometry of a *"genome integrated GAL10 promoter fusion to Venus (YFP)"*; *"Flow cytometry distributions were analyzed using a Gaussian mixture model algorithm (GMM, MATLAB)"*; bimodality criterion *"\|µ₁ − µ₂\| > 2 max(σ₁, σ₂), min(ξ₁, ξ₂) > 0.1"* | Venturelli 2013 CaltechTHESIS (**FULL TEXT** — see §7.2 provenance warning) |
| Single-cell induction level | *"By measuring the distribution of fluorescent intensity in individual cells using fluorescence-activated cell sorting (FACS), we quantified the induction levels of GAL1 in these yeast strains."* | Hong et al. 2021 PLoS Comput Biol (**FULL TEXT**) |
| Colony size as fitness proxy | *"Using colony size as a proxy for fitness, we developed a method for measuring fitness-based genetic interactions"*; *"the final output arrays consisting of haploid double-mutant colonies are imaged at a single time point"* | Baryshnikova et al. 2010, *Nat Methods* 7:1017–1024, `https://pmc.ncbi.nlm.nih.gov/articles/PMC3117325/` (**FULL TEXT**) — **but on GLUCOSE, see §5.1** |
| Competitive fitness, barcode pools | 28 carbon×nitrogen environments incl. 7 galactose conditions; "significant fitness defect in at least four of our seven galactose conditions" | VanderSluis et al. 2014 (**FULL TEXT**) |

**Three functionals are being conflated across this literature and must not be pooled in an answer key:**
1. **Growth on galactose** (does the organism increase in biomass) — the persistence-like outcome.
2. **Lag / time-to-induction** (how fast the switch fires) — a *rate*, not a capability.
3. **Gene expression level or induced-cell fraction** (does the switch fire at all) — the readout for `gal3 gal1 gal7`, which cannot grow on galactose under any circumstance.

**The GAL1/GAL3 redundancy claim lives in functional (3). The essentiality claims live in functional (1). They are not the same measurement and a benchmark that scores them together is scoring two different systems.**

---

## 7. PUBLISHED DYNAMICAL MODELS — and what each was fitted to

**Decisive item first: of every GAL model retrieved, NOT ONE was fitted to `gal1Δ gal3Δ` double-deletion data. One used a related but materially different strain.**

### 7.1 Acar M, Becskei A, van Oudenaarden A (2005)

- **Citation VERIFIED (Crossref + PDF):** "Enhancement of cellular memory by reducing stochastic transitions." *Nature* 435(7039):228–232. DOI 10.1038/nature03524. **Attribution in brief is CORRECT.** `https://www.hubrecht.eu/app/uploads/2017/11/2005-Acar-M-Nature.pdf` — **FULL TEXT RETRIEVED.**
- **(a) Size:** NOT RETRIEVED. No species/equation/parameter counts stated.
- **(b) Formalism:** reduced/phenomenological, NOT mass action. *"The first-order differential equation describing the time evolution of the Gal3p concentration is analogous to the equation of motion of an overdamped particle in an energy landscape."* Potential *"U(x) = −∫x₀[f(x′) − g(x′)]dx′"*, escape rate *"exp(−ΔU/k_BT)"*.
- **(c) Fitted to:** its own bifurcation boundaries from single-cell fluorescence. *"Energy barriers were calculated with experimentally determined parameters obtained from fitting the experimentally determined boundaries (Fig. 3b, red circles) to the network model (Fig. 3b, solid black lines)."*
- **(d) gal1Δ gal3Δ: NO.** Tool response on direct interrogation: *"NOT PRESENT. No mention of a gal1 gal3 double deletion strain exists in this document."*
- **Critical nuance:** the "deletion" strains are **feedback interruptions by promoter replacement, not nulls** — *"feedback loop was interrupted by replacement of the endogenous, Gal4p-dependent, promoter by an externally inducible…PTET promoter."* Named: *"gal2Δ"* (MA0215), *"GAL3 loop knockout"* (MA0182), *"GAL80 loop knockout"* (MA0188). **GAL1 is not manipulated at all.**

### 7.2 Venturelli OS, El-Samad H, Murray RM (2012) — the closest any model comes

- **Citation VERIFIED (Crossref):** "Synergistic dual positive feedback loops established by molecular sequestration generate robust bimodal response." *PNAS* 109(48):E3324–E3333. DOI 10.1073/pnas.1211902109. **Attribution and order in brief are CORRECT.**
- **⚠ PROVENANCE WARNING: the PNAS paper itself is NOT RETRIEVED** (PNAS 403; PMC3511703 reCAPTCHA ×4; EuropePMC fullTextXML 404). **All quotes below are from the first author's open thesis** — Venturelli OS (2013), "Role of feedback and dynamics in a gene regulatory network," CaltechTHESIS, `https://thesis.library.caltech.edu/7863/13/Venturelli-O-S-2013-thesis.pdf` — **FULL TEXT RETRIEVED. Wording in the published paper may differ.**
- **(a) Size:** partial. *"the set of differential equations for G1, G3, G4 and G80"* — 4 state variables in the reduced model. Total species/reaction/parameter counts NOT RETRIEVED.
- **(b) Formalism:** LUMPED, Hill + QSSA. *"Hill coefficients for the feedback functions involving GAL1, GAL3 and GAL80 were set to 3, 2 and 2, respectively"*; *"Using the quasi-steady-state assumption, the concentrations of the complexes…reached their respective equilibria significantly faster."*
- **(c) Fitted to:** **NOT a formal fit.** *"Parameters were approximated from experimental measurements and values from the literature (Section S2.5)"*; *"Parameters for the model were estimated from experimental measurements and previous studies (Table SI)."* A direct request for a fitting-methodology passage naming datasets/strains returned NOT PRESENT.
- **(d) gal1Δ gal3Δ: PARTIALLY — and NOT as a clean double null.**
  > *"By stark contrast, the simultaneous deletion of GAL1 and the GAL3 feedback loop (GAL1∆ GAL3∆ fb) produced a graded response for the entire range of galactose"*
  > *"Remarkably, this graded response persisted irrespective of the constitutive Gal3p production rate in contrast to the single GAL3 feedback knockout that displayed bimodality for some range of constitutive Gal3p levels"*
  > *"Removing both the GAL1 and GAL3 feedback loops abolished bistability for the entire range of αgal"*
  **The strain is "GAL1∆ GAL3∆ fb": GAL1 null PLUS GAL3 feedback decoupled — Gal3p is still expressed, from a TET promoter, and is titratable ("irrespective of the constitutive Gal3p production rate").** Construction: *"we deleted the coding region of a given gene and integrated a single copy of this gene regulated by an inducible TET promoter or a constitutive promoter"*; for GAL3∆ fb, *"GAL3 was expressed from a TET promoter."*
  **This is NOT the Torchia & Hopper non-inducible genotype. If your claim needs the *uninducible* phenotype, this paper does not supply it. If your claim needs loss of bistability when both positive feedback loops are severed, it does.**
  Whether it served as *fitting* or *validation*: best characterised as **validation/consistency** (parameters were "approximated," not fitted). A passage settling this definitively was NOT RETRIEVED.
- Other strains: *"Eliminating the GAL2 or GAL80 feedback loops did not abolish the GAL system's bimodal response."*

### 7.2b Venturelli OS, Zuleta I, Murray RM, El-Samad H (2015)

- **⚠ TITLE IN THE BRIEF IS WRONG.** Actual title, verified via Crossref and PMC: **"Population Diversification in a Yeast Metabolic Program Promotes Anticipation of Environmental Shifts."** *PLoS Biology* 13(1):e1002042. DOI 10.1371/journal.pbio.1002042. The brief's "…promotes anticipatory behavior" is incorrect. Author order is correct. `https://pmc.ncbi.nlm.nih.gov/articles/PMC4307983/` — **FULL TEXT RETRIEVED.**
- **(a) Size:** NOT RETRIEVED. *"We constructed a simplified mathematical model of this circuit based on canonical knowledge about the galactose system (equations are described in the S1 Text)."* Species named: Gal1p (G1), Gal80p (G80), Gal4p (G4), plus a glucose-dependent repressor R.
- **(b) Formalism:** mixed; QSSA invoked — *"traverses a series of quasi-steady-states as a function of decaying sugar concentration."* A verbatim mass-action assertion was NOT RETRIEVED.
- **(c) Fitted to:** essentially NOT RETRIEVED — only *"The parameter values are listed in S1 Table and S2 Table."* S1 Text NOT RETRIEVED.
- **(d) gal1Δ gal3Δ: NO.** Strains are again feedback decouplings: *"GAL80Δ fb"*, *"GAL3Δ fb"* (aTc-responsive), *"GAL2Δ"* (aTc-inducible TET), *"a strain lacking endogenous Gal4p"* (estradiol-inducible Gal4 chimera).

### 7.3 Ramsey SA et al. (2006)

- **⚠ ATTRIBUTION IN BRIEF IS INCOMPLETE — 8 authors, not 3.** Verified TWICE (Crossref `https://api.crossref.org/works/10.1038/ng1869` and nature.com): **Stephen A. Ramsey, Jennifer J. Smith, David Orrell, Marcello Marelli, Timothy W. Petersen, Pedro de Atauri, Hamid Bolouri, John D. Aitchison.** "Dual feedback loops in the GAL regulon suppress cellular heterogeneity in yeast." *Nature Genetics* 38(9):1082–1087. DOI 10.1038/ng1869.
  **Note for the brief's candidate list: de Atauri, Orrell and Bolouri are co-authors on THIS paper. If a source list treats "de Atauri/Orrell/Bolouri" as a separate GAL model, that is likely a duplicate of this one.**
- **Retrieval: ABSTRACT retrieved from nature.com; body/supplement only via academia.edu — UNRELIABLE.**
- **(a) Size: ⚠ CONFLICTING RETRIEVALS — TREAT AS NOT RELIABLY RETRIEVED.** Two fetches of the *same* academia.edu URL disagreed. Fetch 1 reported 18 species with a full name list and *"18 dynamical equations"* and a rate constant *"kir,gal1 = 0.7379 molec min⁻¹"*; fetch 2, asked directly, answered *"NOT PRESENT — does not explicitly state total counts."* **I am NOT certifying the 18/18 figures or that rate constant.** Requires a human read of the Nature Genetics supplement.
- **(b) Formalism:** Hill-like fractional activation, e.g. *"F1 (P, Q) = P / (1 + P + PQ)"*, with multi-site variants for four and five Gal4p binding sites. **Low confidence — single unreplicated fetch.**
- **(c) Fitted to:** mostly literature-derived with ONE tuned free parameter. *"Rate constants for degradation of mRNA were taken from [3, 4]"*; *"The equilibrium dissociation constant for galactose activation of Gal3p was taken from [12]"*; *"The equilibrium dissociation constant for Gal3p*-Gal80p complex formation was the remaining important free parameter in the model; it was adjusted to give a fractional activity for the reporter gene consistent with the results of [15]."* Comparison data: *"time-course fluorescence measurements"*, *"flow cytometry events in which the fluorescence is greater than three times the autofluorescence intensity."* **Not a global least-squares fit.**
- **(d) gal1Δ gal3Δ: NO — and structurally excluded.**
  > *"Gal1p is 40 times less effective than its homolog Gal3p at activating the GAL switch in response to galactose, we did not include its weak potential feedback role in the model."*
  **This is the strongest negative in the set: Gal1p feedback is excluded from the model by design, so gal1Δ is outside the model's structure.**

### 7.4 Verma M, Bhat PJ, Venkatesh KV (2003)

- **Citation VERIFIED (Crossref):** "Quantitative Analysis of GAL Genetic Switch of *Saccharomyces cerevisiae* Reveals That Nucleocytoplasmic Shuttling of Gal80p Results in a Highly Sensitive Response to Galactose." *J Biol Chem* 278(49):48764–48769. **DOI 10.1074/jbc.M303526200.** Attribution in brief is CORRECT.
- **Retrieval status: TITLE/CITATION ONLY. BODY NOT RETRIEVED** (jbc.org 403 ×2; ScienceDirect blocked; PubMed captcha).
- **(a)–(d): ALL NOT RETRIEVED.**
- Related lab output, from the Venkatesh lab's own page (`https://www.che.iitb.ac.in/web/faculty/kvv/genetic/GALregulon.html`, SECONDARY): Verma, Bhat & Venkatesh (2004) *Biotechnol Appl Biochem* 39(1):89–97 on a **GAL80-lacking** strain.

### 7.5 Apostu R, Mackey MC (2012) — the best-documented parameter provenance

- **Citation VERIFIED; ⚠ YEAR CORRECTION: 2012, not 2011.** "Mathematical model of GAL regulon dynamics in *Saccharomyces cerevisiae*." *J Theor Biol* 293:219–235. DOI 10.1016/j.jtbi.2011.10.012. `https://www.mcgill.ca/mathematical-physiology-lab/files/mathematical-physiology-lab/2011oct_math_model_gal.pdf` — **FULL TEXT RETRIEVED; quotes replicated across two independent fetches** (highest-confidence quantitative quotes in §7).
- **(a) Size:** *"a system of five ordinary differential equations (Eqs. (22)) and four algebraic relations (Eqs. (17))."* Five state variables (M3, G3, Gn3, M80, G80); **16 model parameters.**
- **(b) Formalism:** HYBRID — mass action for slow processes, QSSA for fast, Hill-like transcription term. *"The Gal80 dimerization, the DNA–protein binding and unbinding as well as the protein-protein interactions occur on a faster time scale than transcription, translation, and the degradation processes."*
- **(c) Fitted to: NOT FITTED. Parameters assembled from heterogeneous published literature; 4 of 16 unconstrained.**
  > *"The literature on the GAL system contains a collection of independent experiments involving different strains of yeast, and different experimental set-ups with various carbon sources used for cell growth (see Table C2). This information is sufficient to provide an estimation of 12 out of the 16 model parameters."*
  Data sources: genome-wide mRNA/protein abundance datasets (Arava 2003, Holstege 1998, Ghaemmaghami 2003, Lashkari 1997, Ideker 2001) — **not GAL-specific dose-response curves.** Three parameters (k_cat, K_S, k_C) not estimated from data. **The parameter set is assembled across mismatched strains and carbon sources, by the authors' own admission.**
- **(d) gal1Δ gal3Δ: NO.** No gal1 deletion; *"does not include the synthesis of Gal2p."* Comparison strains are **Acar's promoter-replacement strains re-used**: *"Each of the mutant strains gal2D, gal3D, and gal80D had been engineered by replacing the endogenous promoter controlling the targeted gene… with a doxycycline-inducible promoter."*

### 7.6 Other models found

| Model | Size | Fitted to | gal1Δ gal3Δ | Status |
|---|---|---|---|---|
| **Hong J, Palme J, Hua B, Springer M (2021)**, "Computational analysis of GAL pathway pinpoints mechanisms underlying natural variation," *PLoS Comput Biol* 17:e1008691 — **the most explicitly fitted model found** | 13 equations. ⚠ **parameter count internally inconsistent in extraction**: both *"among the 36 free parameters in our model"* and *"45 parameters in our model"* returned. Do not cite a count without a human check | **YES, explicitly:** *"We fit our model both to the wild-type response of an S288C strain and to two GAL pathway mutants in this strain (S288Cgal80Δ and S288Cmig1Δ). We reasoned that simultaneously fitting the model to all three strains would reduce the risk of over-fitting."* Data: *"the distribution of fluorescent intensity in individual cells using fluorescence-activated cell sorting (FACS)"* | **NO** | FULL TEXT |
| **Palme J, Wang J, Springer M (2021)**, "Variation in the modality of a yeast signaling pathway is mediated by a single regulator," *eLife* 10:e69974 | phenomenological | *"this function was fitted to the induced level curves of natural isolates"* | **NO** — but directly relevant: *"GAL3, the galactose sensor, controls the fraction of induced cells…"*; *"Swapping the alleles of GAL1, the second galactose sensor…does not affect modality."* | FULL TEXT |
| **Salerno L, Cosentino C, Merola A, Bates DG, Amato F (2013)**, *BMC Syst Biol* 7:39 — best-specified size | 9 species *"x:=(G3 G_int G3a G4 G80 G4,80 G80,3a G2 G1)^T"*; **23 parameters / 23 reactions**, N ∈ ℝ^(9×23) | **NO fitting** — robustness analysis of an inherited parameter set | **NO** — though the model carries both G1 and G3 as state variables, so it is *structurally capable* of representing the double knockout | FULL TEXT |
| **Prasad V, Venkatesh KV (2008)**, *BMC Syst Biol* 2:97 (⚠ **Prasad & Venkatesh, NOT Verma/Bhat**) | NOT RETRIEVED | *"forward rate constants are estimated using information from the dynamic deterministic model of Ruhela et al…. values were set to match predicted expression to the mean steady state profiles obtained by Verma et al."* + CFU growth assays | **NO** | FULL TEXT |
| **Escalante-Chong R, Savir Y, Carroll SM, Ingraham JB, Wang J, Marx CJ, Springer M (2015)**, *PNAS* 112(5):1636–1641, DOI 10.1073/pnas.1418058112 | NOT RETRIEVED | NOT RETRIEVED | NOT RETRIEVED | **AUTHORS VERIFIED via Crossref; body NOT RETRIEVED (PNAS 403)** |
| **Venkat P, Saumar H, Bhartiya S, Venkatesh KV**, "Growth Related Model of the Gal System In *Saccharomyces Cerevisiae* Predicts Behavior Of Several Mutant Strains," *IET Syst Biol* | — | — | — | **NOT RETRIEVED (IET 403). Its title promises "several mutant strains" — HIGHEST-VALUE UNRETRIEVED ITEM for the decisive question.** |

### 7.7 BioModels / SBML

**NOT RETRIEVED.** Every attempt to reach `www.ebi.ac.uk/biomodels/*` failed (403/429 throughout). Weak negative evidence only: a `site:ebi.ac.uk` search surfaced only genome-scale metabolic reconstructions (BIOMD0000001063 yeastGEM, BIOMD0000000496/497 Stanford2013, MODEL1209060000, MODEL1002240000, BMID000000141353) — **no GAL regulatory-network model surfaced.** No BioModels page was fetched, so **no species or parameter count from BioModels may enter canon from this report.**

### 7.8 §7 verdict

**No published GAL dynamical model has been fitted to `gal1Δ gal3Δ` double-deletion data.** The single closest case (Venturelli 2012) uses a `GAL1∆ GAL3∆ fb` strain in which Gal3p is still expressed, and it functions as validation rather than fitting. Ramsey et al. **explicitly exclude Gal1p feedback from the model structure**, which means the most-cited GAL model cannot represent the perturbation at all. Apostu & Mackey and Salerno et al. do not fit anything. Hong et al. 2021 is the only model with a clean, explicit, multi-strain fit — and its strains are `gal80Δ` and `mig1Δ`.

---

## 8. HONEST ASSESSMENT — solid vs contested

### SOLID (quoted primary or well-corroborated)
1. Gal4/Gal80/Gal3 wiring, including Gal4 pre-bound at UAS_GAL and ~4-min induction (§1).
2. Gal80 is a purely negative regulator and does not mediate catabolite repression (§1.4).
3. GAL1/GAL3 are WGD paralogs; GAL3 is the dedicated co-inducer, GAL1 the galactokinase (§2.4).
4. `gal3Δ` induces late — "long-term adaptation" (§2.2).
5. Gal1p's inducer function is separable from its kinase function (galactokinaseless alleles, §2.5a).
6. Gal3–Gal80 binds ~10× tighter than Gal1–Gal80 (Kd 44 ± 15 nM vs 490 ± 47 nM) (§2.5f).
7. `gal4Δ` is epistatic to `gal80Δ` (§5.2).
8. `gal2Δ` retains conditional growth on galactose; uptake is redundant with HXTs (§4.1–4.2).
9. `gal80Δ` is constitutive with no galactose-growth cost (§3.5).
10. SGA/E-MAP genome-scale data was collected on 2% glucose (§5.1).

### CONTESTED OR UNDERDETERMINED
1. **The exact `gal1Δ gal3Δ` claim.** The canonical genotype is `gal3 gal1 gal7`, readout MEL1 expression, complemented by the whole `GAL1-10-7` cluster (§2.3).
2. **The mechanism of gal7Δ failure.** Gibney et al.: *"presumably due to the accumulation of galactose-1-phosphate"*; *"the molecular mechanism… remains unclear"* (§3.3).
3. **gal10Δ** — no evidence retrieved for partial growth, a bypass, or galactose-sensitivity. Three open questions, not three negatives (§3.4).
4. **Do HXTs carry galactose?** Boles & Hollenberg say yes weakly; the Hxt1 PLOS ONE paper says Hxt1 specifically does not (§4.3).
5. **10-fold (Kd) vs 40-fold (inducer efficiency)** for Gal3 vs Gal1 — different quantities, not interchangeable (§2.5f).
6. **PGM2** — SGD says "cannot grow on galactose," but it has a WGD paralog and the supporting evidence is from *S. boulardii* with a point mutation (§3.6).
7. **Gal3/Gal80 shuttling vs cytoplasmic sequestration.** Retrieved and quoted from Egriboz et al. 2011:
   > *"One suggests that Gal3 interacts with Gal80 exclusively in the cytoplasm and sequesters it away from nuclear Gal4. A strikingly different hypothesis specifies that cytoplasmic Gal3 binds galactose and then moves into the nucleus to bind to Gal80."*
   > *"Limited recovery of the GFP fluorescence in the nucleus was detectable beginning only after 450 sec, and the compartments did not fully re-equilibrate by 10 min… These results provide direct evidence that Gal3 does not exhibit rapid nuclear import and challenge the hypothesis that Gal3 moves from the cytoplasm into the nucleus in response to galactose."*
   **Note this directly opposes the Verma/Bhat/Venkatesh 2003 model, whose TITLE asserts that "Nucleocytoplasmic Shuttling of Gal80p Results in a Highly Sensitive Response to Galactose" — and whose body I could NOT retrieve. A live, unresolved mechanistic dispute sits underneath one of the candidate models.**

### DISQUALIFYING OR NEAR-DISQUALIFYING COMPLICATIONS
1. **Bistability and hysteresis make "growth on galactose" history-dependent.** Acar et al. 2005 is built on exactly this; Venturelli 2012 reports *"Removing both the GAL1 and GAL3 feedback loops abolished bistability."* **A single-valued "grows / does not grow" label is not well-defined without specifying the pre-growth carbon source.** Any answer key that omits growth history is scoring a non-function.
2. **Respiratory competence is a hidden variable.** Both `gal2Δ` and `gal3Δ` carry the SGD qualifier "unless/as long as cells are respiratory-competent." **A petite derivative would score both as ESSENTIAL when they are not.**
3. **Strain-background variation is first-order, not noise.** Hong et al. 2021 is titled around *"natural variation"*; Palme et al. 2021 show modality varies across natural isolates; Kuang et al. 2016 show *S. uvarum gal3Δ* loses the multi-day LTA phenotype entirely. **The gal3Δ label is not species-invariant and may not be strain-invariant.**
4. **Every SGD phenotype summary is explicitly scoped "in reference strain S288C."**
5. **Glucose repression silences the whole regulon**, which is why the genome-scale interaction data is uninformative here (§5.1).
6. **Galactose concentration matters qualitatively**, not just quantitatively — gal2Δ fails at low galactose and grows at high (§4.1); Lavy et al. used 0.08% galactose.
7. **EBY.VW4000 carries "LoxP/Cre-induced translocations and gene loss"** — inferences from it carry unintended genomic damage.
8. **No survival measure exists in this system** (§6).

---

## 9. COUNT — mechanisms carrying a settled label from direct experimental evidence

**Answer: 8 defensible entries, of which only 5 are high-confidence. A ninth (the redundancy itself) is the one the benchmark most wants and it is MEDIUM at best.**

| # | Component / pair | Label | Confidence | Evidence (retrieval status) |
|---|---|---|---|---|
| 1 | **GAL4** | **Essential** (regulatory) | **HIGH** for expression; MEDIUM for growth | Torchia et al. 1984 (FULL TEXT); Suzuki et al. 1988 (FULL TEXT); SGD growth claim is DATABASE ANNOTATION only |
| 2 | **GAL1** | **Essential** (catabolic — galactokinase) | **MEDIUM-HIGH** | Kuang et al. 2016 (FULL TEXT): *"did not grow better in 2% galactose than it did without any carbon source, a phenotype similar to the S. cerevisiae gal1 null mutant"*; SGD |
| 3 | **GAL7** | **Essential** | **MEDIUM** (mechanism contested) | SGD (ANNOTATION); Gibney et al. 2018 (FULL TEXT) — *"presumably due to the accumulation of galactose-1-phosphate"* |
| 4 | **GAL10** | **Essential** | **LOW-MEDIUM** | SGD ANNOTATION only; no primary retrieved; pleiotropic glycosylation role muddies the label |
| 5 | **GAL3** | **Redundant** (kinetic — long lag, eventual growth) | **HIGH** | Torchia & Hopper 1986 (ABSTRACT); Rubio-Texeira 2005 (FULL TEXT); Kuang et al. 2016 (FULL TEXT) |
| 6 | **GAL2** | **Inert / redundant, CONDITIONAL** (high galactose + respiratory-competent) | **MEDIUM-HIGH** | Boles & Hollenberg 1997 (FULL TEXT, double-verified); SGD; EBY.VW4000 (SECONDHAND) |
| 7 | **GAL80** | **Inert for growth on galactose** (deletion = constitutive) | **MEDIUM-HIGH** | Rubio-Texeira 2005 (FULL TEXT); Torchia et al. 1984 (FULL TEXT); SGD |
| 8 | **GAL4 × GAL80** | **Epistatic** (gal4 epistatic to gal80) | **HIGH** | Torchia et al. 1984 (FULL TEXT); corroborated in Zheng et al. 2010 (FULL TEXT) |
| 9 | **GAL1 backing up GAL3 as inducer** | **Redundant (synergistic pair)** | **MEDIUM — the weakest link in the whole candidate** | Torchia & Hopper 1986 is a `gal3 gal1 gal7` triple complemented by the `GAL1-10-7` cluster, so GAL1 is not resolved; Bhat & Hopper 1992 ABSTRACT ONLY; Meyer et al. 1991 TITLE ONLY; Lavy et al. 2016 FULL TEXT (promoter swap) |

**Excluded as not settled:** MEL1 (no phenotype data), MIG1 under galactose-only (no measurement retrieved), PGM2 (contested), GAL11/MED15 (mediator, arguably outside the network), all HXT genes individually.

**If the answer key requires a *primary, full-text-verified, quoted* passage for every entry, the count drops to 4** — entries 1 (expression only), 5, 6, 8 — because entries 2, 3, 4, 7 and 9 depend on database annotations, abstracts, or secondhand restatements.

---

## 10. WHAT COULD NOT BE RETRIEVED — reported as prominently as what could

**Blocking the load-bearing item (§2):**
1. **Bhat & Hopper 1992, *MCB* 12:2701 — BODY TEXT.** PMC holds it as scanned images: *"Only the abstract and reference list are present."* NCBI ID converter returns **no PMCID** for the DOI. ASM 403. **The galactokinaseless-GAL1 experiment is known to me only through one abstract sentence.**
2. **Torchia & Hopper 1986, *Genetics* 113:229 — BODY TEXT.** OUP serves abstract + PDF only; PMC1202836 reCAPTCHA-blocked ×3. **The entire `gal3 gal1 gal7` result is known to me only through the abstract.**
3. **Meyer, Walker-Jonah & Hollenberg 1991, *MCB* 11:5454 — EVERYTHING except Crossref metadata.** ASM 403; no PMCID exists. **The "GAL1 suppresses the gal3 phenotype" claim is asserted-by-title only.**
4. **Kar RK, Qureshi MT, DasAdhikari AK, Zahir T, Venkatesh KV, Bhat PJ (2014), "Stochastic galactokinase expression underlies GAL gene induction in a GAL3 mutant of *Saccharomyces cerevisiae*," *FEBS J* 281:1798–1817, DOI 10.1111/febs.12741** (authorship VERIFIED via Crossref) — **Wiley 403. This is the single most on-point modern paper for the GAL1/GAL3 mechanism and the gal3Δ lag, and I could not read one word of it.** Highest-priority follow-up.
5. **Any primary numeric lag time (in hours) for *S. cerevisiae* gal3Δ.** The only figure retrieved is *"a growth delay of multiple days"* in a 2016 comparative sentence.
6. **The primary source of the "40-fold" Gal1-vs-Gal3 inducer efficiency figure.**

**Blocking §3:**
7. **Johnston M 1987, *Microbiol Rev* 51:458 — PMC373127 returns only the reference list and scanned page images. Zero body text.** Named as the best free review; yielded nothing.
8. **Douglas & Hawthorne 1964 and 1966, *Genetics*** — PDF-only, fetch blocked. **The historical origin of the gal7/gal10 galactose-sensitivity claim is UNVERIFIED.**
9. **Sellick, Campbell & Reece 2008, *Int Rev Cell Mol Biol* 269:111** — the free mirror redirects https→http in a loop WebFetch cannot break; ScienceDirect paywalled. **Likely the richest single source for §3; its loss is why §3 rests on SGD.**
10. **JBC "Relationship between UDP-Galactose 4′-Epimerase Activity and Galactose Sensitivity in Yeast"; *Mol Genet Metab* 2007 "Distinct roles of galactose-1P…"; Ross/Davis/Fridovich-Keil "Differential roles of the Leloir pathway enzymes…"** — all blocked. **This is why gal10Δ has no toxicity evidence.**
11. **SGD phenotype annotation TABLES never rendered on any of ~8 SGD pages** (client-side; backend API robots-blocked). **Consequence: NO primary citation behind ANY SGD annotation in this report.**
12. **Giaever et al. 2002** — abstract only; galactose medium and per-gene results NOT RETRIEVED.

**Blocking §5:**
13. **The Methods text of Costanzo 2010 and Costanzo 2016 themselves** (science.org 403; M&M only inside a 500 MB SOM.zip; PMC omits Methods). The glucose conclusion rests on the lab's *protocol* papers.
14. **The identity of the "alternative carbon source" in Costanzo et al. 2021** — inside a Dryad .xlsx. **Do not assume galactose.**
15. **Per-gene confirmation that GAL1/3/4/7/10/80 and MIG1 are in the SGA arrays** — only GAL2 confirmed.
16. **An executed GAL query on TheCellMap.org** — client-side JS app.
17. **Whether GAL genes appear in VanderSluis et al.'s 565 galactose-sensitive genes.**
18. **Ideker et al. 2001; Nehlin et al. 1991; Lutfiyya 1998 Results; Wieczorke et al. 1999; Reifenberger et al. 1997; Hillenmeyer et al. 2008; Szappanos et al. 2011.**

**Blocking §7:**
19. **Venturelli et al. 2012 PNAS primary text** — substituted by the first author's open thesis.
20. **Verma, Bhat & Venkatesh 2003 JBC — entire body.**
21. **Ramsey et al. 2006 model size / parameter counts — CONFLICTING retrievals, not certified.** Exact strain genotypes NOT RETRIEVED.
22. **Venkat, Saumar, Bhartiya & Venkatesh, *IET Syst Biol*, "…Predicts Behavior Of Several Mutant Strains"** — IET 403. Highest-value unretrieved model.
23. **Escalante-Chong et al. 2015 PNAS body.**
24. **BioModels/SBML availability for any GAL model.**
25. **Hong et al. 2021 parameter count — internally inconsistent extraction (36 vs 45).**

**A DOI warning:** `10.1371/journal.pone.0019353`, surfaced by search as "External Control of the GAL Network…", resolved TWICE to Zi, Liebermeister & Klipp (2010), "A Quantitative Study of the Hog1 MAPK Response…", an unrelated osmotic-stress paper. **Do not cite that DOI for a GAL paper without independent checking.**

**Attribution corrections found during verification:**
- Venturelli et al. 2015 *PLoS Biology* title is **"…Promotes Anticipation of Environmental Shifts,"** not "…promotes anticipatory behavior."
- Ramsey et al. 2006 has **8 authors**; de Atauri, Orrell and Bolouri are co-authors on it, not a separate paper.
- Apostu & Mackey is **2012**, not 2011.
- Verma et al. 2003 correct DOI is **10.1074/jbc.M303526200**.
- Prasad & Venkatesh 2008 is **not** Verma/Bhat/Venkatesh.
- Kar et al. 2014 correct DOI is **10.1111/febs.12741**.
