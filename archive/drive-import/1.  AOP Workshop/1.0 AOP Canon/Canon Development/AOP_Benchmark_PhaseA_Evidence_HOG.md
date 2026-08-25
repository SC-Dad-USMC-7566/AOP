# Benchmark candidate-system due diligence: *S. cerevisiae* HOG osmostress pathway

**Compiled:** 2026-07-25
**Tooling:** Nimble CLI **NOT AVAILABLE** (`nimble: command not found`). All retrieval via `WebSearch` + `WebFetch`. No curl/wget/python fetching used.

---

## 0. PROVENANCE CAVEATS — READ FIRST

**0.1 — Second-order extraction.** `WebFetch` does not hand me raw page text; it fetches, converts to markdown, and a *small intermediary model* answers my prompt against it. Every "quote" below is therefore a quote **as returned by that intermediary**, not text I read directly. I prompted repeatedly for verbatim reproduction and rejected summaries where I could detect them, but **any single quotation below could in principle be a paraphrase that the intermediary presented as a quote.** For a scored answer key, the load-bearing quotes (esp. §2) should be re-verified by a human against the PDF. I have marked confidence accordingly throughout.

**0.2 — Hard retrieval failures.** The following were blocked and are **NOT RETRIEVED**:

| Source | Route attempted | Result |
|---|---|---|
| PubMed (all PMIDs) | pubmed.ncbi.nlm.nih.gov | Google reCAPTCHA interstitial — no content |
| PubMed Central (all PMCIDs) | pmc.ncbi.nlm.nih.gov | reCAPTCHA |
| PubMed Central (alt host) | ncbi.nlm.nih.gov/pmc/... | `ROBOTS_DISALLOWED` |
| NCBI E-utilities | eutils.ncbi.nlm.nih.gov | `ROBOTS_DISALLOWED` |
| Science / Science Signaling | science.org, science.sciencemag.org | HTTP 403 |
| Cell / ScienceDirect | cell.com, sciencedirect.com | HTTP 403 |
| Wiley (FEBS) | onlinelibrary.wiley.com | HTTP 403 |
| MMBR full text | journals.asm.org (HTML + PDF) | Metadata + references only; body paywalled |
| Mol Biol Cell | molbiolcell.org | HTTP 403 |
| BioModels | ebi.ac.uk/biomodels | HTTP 403 |
| Semantic Scholar | semanticscholar.org, api.semanticscholar.org | Empty body / provenance block |

**Consequence:** the four foundational primary papers for this system — **Brewster 1993, Maeda 1994, Maeda 1995, Posas & Saito 1997** — could **not** be retrieved in any form, not even their abstracts. Their titles/authors are confirmed only indirectly (§1.1). Every claim that would rest on them is sourced here to a *retrieved secondary or later primary source instead*, and labelled as such.

---

## 1. CAUSAL STRUCTURE

### 1.1 Authorship verification of the paywalled classics

**Status: INDIRECTLY VERIFIED (third-party reference list), not verified against the papers themselves.**

Retrieved from the **reference list** of O'Rourke & Herskowitz 1998, *Genes & Development* 12:2874 (full text retrieved from genesdev.cshlp.org):

> "Brewster J.L., de Valoir T., Dwyer N.D., Winter E., Gustin M.C. (1993) An osmosensing signal transduction pathway in yeast. Science 259:1760–1763."

> "Maeda T., Wurgler-Murphy S.M., Saito H. (1994) A two-component system that regulates an osmosensing MAP kinase cascade in yeast. Nature 369:242–245."

> "Maeda T., Takekawa M., Saito H. (1995) Activation of yeast PBS2 MAPKK by MAPKKKs or by binding of an SH3-containing osmosensor. Science 269:554–558."

> "Posas F., Saito H. (1997) Osmotic activation of the HOG MAPK pathway via Ste11p MAPKKK: Scaffold role of Pbs2p and Sho1p. Science 276:1702–1705."

**Findings and flags:**
- The task's premise "Maeda, Wurgler-Murphy & Saito 1994/1995" is **half wrong**. Wurgler-Murphy is an author on the **1994 Nature** paper only. The **1995 Science** paper is **Maeda, Takekawa & Saito**. Confirmed by the reference list above and consistent with PubMed search-result listings (title-level only) at PMIDs 8183345 and 7624781.
- **DISCREPANCY, unresolved:** the reference-list rendering gives the 1997 subtitle as *"Scaffold role of Pbs2p and Sho1p"*, whereas the PubMed and Science search-result listings both render it *"scaffold role of Pbs2p MAPKK"*. I could not resolve which is correct because both PubMed and Science are blocked. The intermediary model also flagged partial visibility on several of these entries. **Treat the 1997 subtitle as UNRESOLVED.**
- Reviews: **Hohmann 2002**, *Microbiol Mol Biol Rev* 66(2):300–372 — bibliographic record confirmed (journals.asm.org metadata + PubMed listing PMID 12040128); **full text NOT RETRIEVED**. **Saito & Posas 2012**, *Genetics* 192(2):289–318 — **RETRIEVED** (academic.oup.com, partial section coverage). Note the task listed "reviews by Hohmann and by Saito & Posas" — this is correct; Saito & Posas 2012 is in *Genetics*, not a Hohmann-authored venue.

### 1.2 The two-branch convergent architecture

**Source A — Saito & Posas 2012, *Genetics* 192:289. RETRIEVED (full-text HTML, academic.oup.com). Confidence: HIGH.**

Section *"Overview of the HOG pathway"*:

> "The upstream part of the HOG pathway comprises the functionally redundant, but mechanistically distinct, Sln1 and Sho1 branches. A signal emanating from either branch converges on a common MAPKK, Pbs2, which is the specific activator of the Hog1 MAPK."

This single sentence establishes: (i) two branches, (ii) functional redundancy, (iii) convergence on Pbs2, (iv) Pbs2 → Hog1 specificity.

**Source B — O'Rourke & Herskowitz 1998, *Genes Dev* 12:2874, Introduction. RETRIEVED. Confidence: HIGH.**

> "One involves a phosphorelay system related to the histidyl–aspartyl phosphorelay systems of bacteria and includes the integral membrane protein Sln1p and the response regulator Ssk1p."

> "Ssk1p activates two redundant MAPKKKs, Ssk2p and Ssk22p, which subsequently activate Pbs2p, the MAPKK for Hog1p."

> "The other input is through the osmosensor Sho1p, which is a putative membrane-spanning protein with a carboxy-terminal SH3 domain."

> "Activation of Pbs2p by Sho1p requires Ste11p, which phosphorylates Pbs2p."

**Source C — Tatebayashi et al. 2007, *EMBO J*, abstract. RETRIEVED (link.springer.com mirror). Confidence: HIGH.**

> "Upstream of the HOG pathway are functionally redundant SLN1 and SHO1 signaling branches."

**Ypd1 in the phosphorelay:** the Sln1–Ypd1–Ssk1 phosphorelay is stated by Saito & Posas 2012 and originates with Posas et al. 1996 *Cell* 86:865. **Posas et al. 1996 NOT RETRIEVED** (not even a reference-list entry — the extraction reported it absent from the O'Rourke reference excerpt). The *specific* claim "Ypd1 is the intermediate histidine phosphotransfer protein" is here **INFERRED from review-level text only**, not from a retrieved passage naming Ypd1 in a mechanistic sentence.

**Cdc42 / Ste50 / Msb2 / Hkr1 in the SHO1 branch:** see §7.2. Ste50 and Ste20 are placed in the branch by O'Rourke & Herskowitz 1998 genetics (§2). Cdc42's adaptor role is from Tatebayashi et al. 2006 *EMBO J* 25:3033 — **NOT RETRIEVED**, surfaced in search results only. **Do not use Cdc42 in an answer key on this evidence.**

**Item 1 verdict:** ✅ **SOLID.** The two-branch convergent architecture is established by a directly-quoted passage from a retrieved authoritative review written by the discoverers, corroborated by a retrieved independent primary paper's introduction. The *foundational* primary papers themselves are NOT RETRIEVED.

---

## 2. THE REDUNDANCY CLAIM — the load-bearing item

### 2.1 Headline: CONFIRMED, but with a genotype correction that matters

The expected pattern is **confirmed**. But the task's stated pattern — "`ssk1Δ` alone osmotolerant, `sho1Δ` alone osmotolerant, **double** osmosensitive" — is **not the cleanest published form**, and one specific variant of it is **explicitly contradicted** in the literature.

### 2.2 The strongest retrieved primary evidence

**Source — O'Rourke & Herskowitz 1998, *Genes Dev* 12(18):2874–2886. FULL TEXT RETRIEVED. Confidence: HIGH (subject to §0.1).**

**Introduction (statement of the established pattern, with genotypes):**

> "Because there are two inputs for activating Hog1p, mutants defective in either the Sho1p branch or the Sln1p branch are not osmosensitive."

> "In contrast, mutants defective in both branches, for example, *ssk2 ssk22 sho1* or *ssk2 ssk22 ste11* strains are osmosensitive."

**Results / Figure 5A (this paper's own data):**

> "wild-type, *ssk1, sho1, ste50,* and *ste20* strains grew equally well on YEPD and YEPD + NaCl plates"

> "the *ste50 ssk1* double mutant was osmosensitive on YEPD + 1 m NaCl plates"

> "as was the *sho1 ssk1* double mutant"

> "The *ste50 sho1* double mutant was as osmoresistant as the *ste50* and *sho1* single mutants"

> "the *ssk1 ste20* strain was osmosensitive on YEPD + 1.2 m NaCl medium"

> "*ste50* and *ste20* mutations also caused osmosensitivity in strains lacking *SSK2* and *SSK22*"

**Figure 5B (signalling readout, not growth):**

> "when *SHO1, STE20, STE50,* or *STE11* is deleted in an *ssk1* mutant, Hog1p was not phosphorylated during exposure to 0.7 m NaCl"

**Growth assay method (verbatim, from the same retrieval):**

> "Yeast strains were streaked on YEPD, YEPD + 1 m NaCl, and YEPD + 1.2 m NaCl plates, as indicated, and grown for 3 days (YEPD), 6 days (YEPD + 1 m NaCl) or 8 days (YEPD + 1.2 m NaCl), at 30°C to assay growth."

**This is a clean, internally-controlled redundancy demonstration:**
- Singles osmotolerant: `ssk1Δ`, `sho1Δ`, `ste50Δ`, `ste20Δ` — all grow like WT on 1 M NaCl.
- Doubles osmosensitive: `sho1Δ ssk1Δ`, `ste50Δ ssk1Δ` (1 M NaCl); `ste20Δ ssk1Δ` (needs 1.2 M NaCl).
- **Negative control that the redundancy is specifically cross-branch:** `ste50Δ sho1Δ` (both mutations *within* the SHO1 branch) is **NOT** osmosensitive. This is a genuinely valuable control for an answer key — it shows the synergy is between branches, not between any two HOG genes.
- Same-branch confirmation in the other direction: `ste50Δ` and `ste20Δ` also synergise with `ssk2Δ ssk22Δ`.

### 2.3 The genotype distinction the task flagged — it is REAL and it matters

**Source — Saito & Posas 2012, *Genetics* 192:289. RETRIEVED. Confidence: MEDIUM-HIGH.**

> "osmostress does cause slight activation of the Hog1 MAPK in *ssk1*Δ *sho1*Δ mutants"

> "no activation is observed in *ssk2*Δ *ssk22*Δ *sho1*Δ mutants"

**This is the single most important nuance in this whole dossier.** `ssk1Δ sho1Δ` is **NOT** signalling-null: there is residual Hog1 activation, because Ssk2/Ssk22 retain some Ssk1-independent activity. Only `ssk2Δ ssk22Δ sho1Δ` (a **triple**) is signalling-null. So:

- `ssk1Δ` and `ssk2Δ ssk22Δ` are **NOT interchangeable** — confirmed with a quoted passage.
- The canonical "double mutant" in the literature is frequently a **triple deletion** (`ssk2Δ ssk22Δ sho1Δ`, `ssk2Δ ssk22Δ ste11Δ`).
- O'Rourke & Herskowitz nevertheless report `sho1Δ ssk1Δ` as osmosensitive on plates at 1 M NaCl. So the residual signalling in `ssk1Δ sho1Δ` is apparently **insufficient to rescue growth** at 1 M NaCl. Both statements can be true; but note they come from different labs and possibly different strain backgrounds. **This is a live inconsistency risk for a scored key** — the phospho-readout and the growth readout disagree in degree.

Corroborating branch-dependence statements from the same retrieval:

> "a mutant that lacks both the *SSK2* and *SSK22* genes (an *ssk2*Δ *ssk22*Δ mutant) is totally dependent on the Sho1 branch for activation of the Hog1 MAPK"

> "a mutant that lacks *STE11* is dependent on the Sln1 branch"

### 2.4 Which double/triple mutants were actually tested, and what was observed

| Genotype | Osmostress phenotype | Osmolyte / conc. | Readout | Source | Confidence |
|---|---|---|---|---|---|
| `ssk1Δ` | grows like WT | 1 M NaCl plates | streak, 6 d | O'Rourke & Herskowitz 1998 Fig 5A | HIGH |
| `sho1Δ` | grows like WT | 1 M NaCl plates | streak, 6 d | same | HIGH |
| `ste50Δ` | grows like WT | 1 M NaCl plates | streak, 6 d | same | HIGH |
| `ste20Δ` | grows like WT | 1 M NaCl plates | streak, 6 d | same | HIGH |
| **`sho1Δ ssk1Δ`** | **osmosensitive** | 1 M NaCl plates | streak, 6 d | same | HIGH |
| **`ste50Δ ssk1Δ`** | **osmosensitive** | 1 M NaCl plates | streak, 6 d | same | HIGH |
| **`ste20Δ ssk1Δ`** | **osmosensitive** | **1.2 M** NaCl plates | streak, 8 d | same | HIGH |
| `ste50Δ sho1Δ` | **osmoRESISTANT** (like singles) | 1 M NaCl plates | streak, 6 d | same | HIGH |
| `ste50Δ` or `ste20Δ` + `ssk2Δ ssk22Δ` | osmosensitive | not specified in retrieved text | streak | same | MEDIUM |
| `ssk2Δ ssk22Δ sho1Δ` | osmosensitive (stated in Intro) | not specified | — | same, Intro | MEDIUM |
| `ssk2Δ ssk22Δ ste11Δ` | osmosensitive (stated in Intro) | not specified | — | same, Intro | MEDIUM |
| `ssk1Δ sho1Δ` | *slight* Hog1 activation retained | not specified | phospho-Hog1 | Saito & Posas 2012 | MEDIUM |
| `ssk2Δ ssk22Δ sho1Δ` | **no** Hog1 activation | not specified | phospho-Hog1 | Saito & Posas 2012 | MEDIUM |
| `hkr1Δ msb2Δ` (in `ssk2/22Δ` bg) | "severely osmosensitive" | not specified | not specified | Tatebayashi et al. 2007 | MEDIUM |
| `hkr1Δ` or `msb2Δ` alone (in `ssk2/22Δ` bg) | "no osmosensitivity" | not specified | not specified | Tatebayashi et al. 2007 | MEDIUM |

**Not retrieved:** the original `ssk2Δ ssk22Δ sho1Δ` growth data (Maeda et al. 1995) and the `ssk2Δ ssk22Δ ste11Δ` growth data (Posas & Saito 1997). Both are known to me only through O'Rourke & Herskowitz's Introduction sentence quoted above, i.e. **second-hand**.

**On `ste11Δ` pleiotropy — the task's warning is correct.** `STE11` is shared with the mating and filamentous-growth MAPK pathways:

> "Surprisingly, three of these pathways (HOG, mating, and FIG) share many of the same signaling elements, including the Ste11 MAPKKK" — Saito & Posas 2012, RETRIEVED.

The same applies to `STE20` and `STE50`. A `ste11Δ`-based redundancy entry therefore has a confound that `sho1Δ`-based entries do not: the double mutant is also crippled in two other MAPK pathways.

### 2.5 A retrieved contradiction from SGD — flag it

Fetching SGD's SHO1 locus page (yeastgenome.org/locus/S000000920) returned a curated phenotype annotation:

> "osmotic stress resistance: decreased"

**This conflicts with the primary data** (`sho1Δ` grows like WT at 1 M NaCl). SGD annotations aggregate across alleles, backgrounds and combination genotypes and do not preserve the single/double distinction in the summary line. **Do not source an answer key from SGD phenotype summaries for this system.** I could not open SGD's underlying annotation table (rows rendered client-side and were not in the fetched content), so I cannot say which reference produced that annotation.

**Item 2 verdict:** ✅ **CONFIRMED**, with two caveats that must be encoded in any key: (a) `ssk1Δ` ≠ `ssk2Δ ssk22Δ` — the "double" is often really a triple; (b) `ste11Δ`/`ste20Δ`/`ste50Δ` are pleiotropic across three MAPK pathways. The cleanest, best-controlled retrieved entry is **`sho1Δ` × `ssk1Δ`** from O'Rourke & Herskowitz 1998, which uniquely carries a same-branch negative control (`ste50Δ sho1Δ`).

---

## 3. ESSENTIAL COMPONENTS (hog1Δ, pbs2Δ)

**Retrieval status: WEAKEST ITEM IN THE DOSSIER relative to how well-known the fact is.**

The canonical primary source is **Brewster, de Valoir, Dwyer, Winter & Gustin 1993, *Science* 259:1760–1763** — **NOT RETRIEVED** (science.org 403, PubMed captcha). I could not obtain even its abstract. I therefore have **no quoted primary passage** for `hog1Δ` or `pbs2Δ` osmosensitivity.

**What I did retrieve:**

**(a) SGD curated summary for HOG1** (yeastgenome.org/locus/S000004103/phenotype). Confidence: MEDIUM (curated database summary, not a primary passage; and see §2.5 on SGD reliability for this pathway):

> "sensitive to hyperosmotic stress and fails to accumulate glycerol under hyperosmotic conditions"

**(b) Saito & Posas 2012** — an indirect but strong statement, since it presupposes that `hog1Δ` *is* osmosensitive:

> "the mammalian stress-responsive p38 MAPK can rescue the osmosensitivity of *hog1*Δ mutations in response to hyperosmotic challenge"

This confirms `hog1Δ` osmosensitivity **by presupposition** (you cannot rescue an osmosensitivity that doesn't exist). Confidence: MEDIUM-HIGH for the fact, LOW as a citable primary passage.

**(c) Martin et al. 2015, *Mol Syst Biol*, E-MAP** (limlab.ucsf.edu PDF, RETRIEVED). Quantitative, genome-scale, sorbitol condition:

> "The top-ranked query genes in SO include the MAPK and MAPKK of the HOG pathway, Hog1 and Pbs2, respectively, as well as Nmd5."

("SO" = sorbitol; see §4/§5.) This independently places **both Hog1 and Pbs2 at the top of the osmostress-relevant gene ranking in a quantitative screen**, which is the best *quantitative* corroboration I could retrieve for their essentiality.

**(d) O'Rourke & Herskowitz 1998** — I specifically prompted for `hog1`/`pbs2` single-mutant growth statements and the extraction returned:

> "the paper does not provide explicit growth phenotype descriptions for *hog1*, *pbs2*, *ssk2 ssk22*, or *ste11* single mutants on high-osmolarity plates"

**Item 3 verdict:** ⚠️ **The FACT is not in doubt** (three independent retrieved sources presuppose or corroborate it). But **I have no retrieved primary quotation with a measured phenotype and a stated osmolyte concentration for `hog1Δ` or `pbs2Δ`.** For a strict-provenance answer key this entry is currently **"asserted by retrieved secondary sources; primary passage NOT RETRIEVED."** It needs Brewster 1993 pulled by hand.

Note also: "essential for osmoadaptation" ≠ "essential". `HOG1` and `PBS2` are non-essential genes under standard growth — the deletions are viable and grow normally without salt. The essentiality is **conditional on osmostress**. Any key must say so.

---

## 4. INERT / SPECTATOR COMPONENTS, AND SYNERGY

### 4.1 Genuine spectators (single deletion ≈ no osmostress phenotype)

| Gene | Evidence | Source | Confidence |
|---|---|---|---|
| `SHO1` | "grew equally well on YEPD and YEPD + NaCl plates" (1 M) | O'Rourke & Herskowitz 1998 Fig 5A | HIGH |
| `SSK1` | same sentence | same | HIGH |
| `STE50` | same sentence | same | HIGH |
| `STE20` | same sentence | same | HIGH |
| `SKN7` | "the *skn7*Δ mutants are not osmosensitive" | Saito & Posas 2012 | HIGH |
| `GPD2` | under high salinity, "behaved like the wild-type strain" | Ansell et al. 1997 *EMBO J* 16:2179 | HIGH |
| `MSB2` (alone, in `ssk2/22Δ` bg) | "conferred no osmosensitivity to yeast cells" | Tatebayashi et al. 2007 | MEDIUM |
| `HKR1` (alone, in `ssk2/22Δ` bg) | same sentence | same | MEDIUM |

**Best spectator candidate: `SKN7`.** It is a *bona fide* target of the same Sln1 phosphorelay (Sln1→Ypd1→Skn7 is the branch parallel to Sln1→Ypd1→Ssk1), so it is *wired into* the system yet contributes nothing to osmotolerance — exactly the "connected but not load-bearing" profile a good answer key wants. Quoted evidence: *"the skn7Δ mutants are not osmosensitive."* Caveat: I did **not** retrieve a passage establishing the Sln1→Ypd1→Skn7 wiring itself from a primary source; that link is **INFERRED** here.

**Runner-up: `GPD2`.** Same enzymatic activity as Gpd1, different regulation, no osmostress phenotype alone. Strongly quoted (§4.2).

### 4.2 Individually near-inert, jointly load-bearing — the best published synergy pairs

**PAIR A — `GPD1` × `GPD2`. Source: Ansell, Granath, Hohmann, Thevelein & Adler 1997, *EMBO J* 16:2179–2187. Abstract + results RETRIEVED (link.springer.com). Confidence: HIGH.**

Abstract, verbatim:

> "Previous studies showed that *GPD1* plays a role in osmoadaptation since its expression is induced by osmotic stress and *gpd1*Δ mutants are osmosensitive. Here we report that *GPD2* has an entirely different physiological role. Expression of *GPD2* is not affected by changes in external osmolarity, but is stimulated by anoxic conditions. Mutants lacking *GPD2* show poor growth under anaerobic conditions. Mutants deleted for both *GPD1* and *GPD2* do not produce detectable glycerol, are highly osmosensitive and fail to grow under anoxic conditions."

Results, verbatim as returned:

> `gpd1Δ`: "showed a markedly reduced salt tolerance"
> `gpd2Δ`: "behaved like the wild-type strain"
> `gpd1Δ gpd2Δ`: "Deletion of both *GPD1* and *GPD2* resulted in a very severe growth defect at high salinity."

**Assessment:** this is a *partial* rather than a *pure* synergy — `gpd1Δ` is already osmosensitive on its own ("markedly reduced salt tolerance"), so it is not a near-inert partner. The pattern is **inert (`gpd2Δ`) + impaired (`gpd1Δ`) → severe**. Good, but not the clean 0+0→1 pattern.

**PAIR B — `MSB2` × `HKR1` (in an `ssk2Δ ssk22Δ` background). Source: Tatebayashi et al. 2007, *EMBO J*. RETRIEVED (springer mirror). Confidence: MEDIUM.**

> "the *hkr1*Δ *msb2*Δ double‐mutant cells were severely osmosensitive"
> "*hkr1*Δ or *msb2*Δ alone (in the *ssk2/22*Δ background) conferred no osmosensitivity to yeast cells"

**This is the cleanest 0 + 0 → 1 synergy in the dossier**: two individually completely-inert deletions that are jointly severe. Caveats: (i) it is conditional on a sensitising `ssk2Δ ssk22Δ` background, so it is really a 4-gene construct; (ii) I did **not** retrieve the osmolyte, concentration, or growth-assay format; (iii) Msb2 is also a filamentous-growth pathway sensor (§7.2).

**PAIR C — the branch pairs themselves** (`sho1Δ` × `ssk1Δ`; `ste50Δ` × `ssk1Δ`; `ste20Δ` × `ssk1Δ`) — see §2.4. These are the **best-documented pure synergies** in the system: both singles explicitly grow like WT in the same figure, the double is osmosensitive, and there is a same-branch negative control.

### 4.3 Quantitative epistasis / genetic-interaction data

**Task named Costanzo et al., Collins et al., Schuldiner et al. — retrieval status:**

- **Costanzo et al. 2010/2016 SGA:** **NOT RETRIEVED.** boonelab supplement, PMC and science.org all blocked. Also note: the Costanzo genome-scale networks were measured on **standard rich medium**, not under osmostress, so even if retrieved they would give *unstressed* fitness interactions — of limited use for a persistence-under-osmostress key.
- **Costanzo et al. 2021, *Science* "Environmental robustness of the global yeast genetic interaction network":** **NOT RETRIEVED** (PMC captcha, science.org 403). This is the one that varies conditions and is the most relevant of the Costanzo series. **Recommend a manual pull.**
- **Collins et al. / Schuldiner et al. E-MAP:** **NOT RETRIEVED directly.** Their scoring method is referenced by Martin et al. (below).

**RETRIEVED substitute, and it is a good one — Martin et al. 2015, *Mol Syst Biol*, "Differential genetic interactions of yeast stress response MAPK pathways"** (limlab.ucsf.edu PDF; note this is a mirror on a third-party lab site — bibliographic details **not** independently confirmed against the publisher). Confidence: MEDIUM-HIGH for content, MEDIUM for citation metadata.

> "A total of 49 signalling-related query genes covering different pathways were crossed with an array containing approximately 1,200 genes that broadly cover different yeast cellular complexes and processes."

> "Double mutants were arrayed on agar plates either in optimal growth conditions or in the presence of five different agents to provide distinct stresses."

> "Double mutant colony sizes were quantified in each of the conditions, normalized and analysed to calculate a quantitative genetic interaction score (S-score)."

> "The static genetic interactions (S-score) in each condition were scored as previously described (Collins et al, 2006)."

Stress conditions (verbatim as returned; note OCR artefacts "lg" for "µg"):

> "0.6 M SO" (sorbitol) · "50 lg (1 U)/ml zymolyase 20T" · "1.5 mM H2O2" · "30 lg/ml Congo Red" · "4 mM caffeine"

> "The top-ranked query genes in SO include the MAPK and MAPKK of the HOG pathway, Hog1 and Pbs2, respectively, as well as Nmd5."

Query set explicitly includes HOG components — the extraction identified "Sho1 Msb2," "Pbs2 Hog1," "Ypd1 Ssk1" as query-gene labels in Figure 1B.

**This is the only quantitative, osmostress-condition epistasis dataset I could retrieve.** It gives S-scores from normalised colony size at **0.6 M sorbitol** for HOG query genes × ~1,200 array genes. **Critical limitation:** the array is ~1,200 *non-HOG* genes broadly covering complexes/processes; the HOG genes are *queries*. **I could NOT confirm that HOG-query × HOG-query pairs (e.g. `sho1` × `ssk1`) are present in this dataset.** The extraction explicitly returned: *"The paper does not explicitly state that the SLN1 and SHO1 branches show redundancy or report negative genetic interactions among HOG pathway components in the results presented."* **So the key double mutants of §2 are probably NOT in this quantitative dataset.**

**Item 4 verdict:** ✅ Good spectators exist (`SKN7` strongest, `GPD2` best-quoted). ✅ Genuine 0+0→1 synergy exists (`msb2Δ hkr1Δ`, quoted). ⚠️ Quantitative epistasis under osmostress exists (Martin 2015, S-scores at 0.6 M sorbitol) but **likely does not cover the branch-redundancy pairs**; the named Costanzo/Collins/Schuldiner datasets were **NOT RETRIEVED**.

---

## 5. MEASURED PERSISTENCE OUTCOME — what is actually measured, in what units

**Honest answer: the ground-truth phenotype for the redundancy claim is a QUALITATIVE PLATE +/-. That is the single biggest weakness of this candidate.**

### 5.1 What the redundancy evidence actually measures

O'Rourke & Herskowitz 1998, verbatim Methods:

> "Yeast strains were streaked on YEPD, YEPD + 1 m NaCl, and YEPD + 1.2 m NaCl plates, as indicated, and grown for 3 days (YEPD), 6 days (YEPD + 1 m NaCl) or 8 days (YEPD + 1.2 m NaCl), at 30°C to assay growth."

**Units: none.** This is a **streak on a plate, scored by eye, at one or two salt concentrations, after a fixed incubation.** The reported phenotypes ("grew equally well", "was osmosensitive", "as osmoresistant as") are **ordinal/binary**. There is no growth rate, no survival fraction, no dose–response, no error bar.

Babazadeh et al. 2014, *Sci Rep* 4:4697 (RETRIEVED) is the same picture a decade and a half later — spot dilutions:

> "Cells were pregrown overnight on YPD plates, resuspended in water to OD600 = 0.1 and 5 μl of a 10-fold dilution series were spotted onto YPD plates with or without KCl."

at "0.8 M KCl" after "1–2 days culture at 30°C". The extraction's explicit finding: *"The article does not provide explicit numerical growth rate, doubling time, lag time, or OD measurements for HOG pathway mutants under osmotic stress... growth assessments were qualitative, relying on visual colony formation on agar plates."* A 10-fold dilution series is **semi-quantitative** (it yields roughly a log-scale plating-efficiency estimate) but is still not a rate or a survival fraction.

### 5.2 Does ANY quantitative measurement exist?

**Yes — three, and none of them covers the double mutants.**

**(a) Martin et al. 2015 E-MAP — QUANTITATIVE, osmostress condition, but wrong gene pairs.**
Normalised **colony size** → **S-score** at **0.6 M sorbitol**. This is a real continuous fitness proxy under osmostress, genome-scale. But (§4.3) HOG×HOG double mutants are almost certainly not in it.

**(b) Petelenz-Kurdziel et al. 2013, *PLoS Comput Biol* 9:e1003084 — QUANTITATIVE growth rates, but wrong mutants.** RETRIEVED (journals.plos.org).

> "Changes in doubling times before and after stress are plotted in Fig. 5A. The observed decrease in growth rate is similar for wild type, *pfk26/27*Δ, and *HOG1-att* strains."

Strains measured: "wild type, *pfk26/27Δ*, *HOG1-att*, *FPS1-Δ1*, *gpd1Δ*, and *hog1Δ*." So there **are** doubling-time measurements under osmostress including for `hog1Δ` and `gpd1Δ`. **But:** the extraction reported that *"the article does not provide specific numerical values (e.g. doubling time in minutes) in the main text. The actual quantitative data appears relegated to figures."* **I have no retrieved numbers.** And **no branch mutants and no double mutants** were measured.

**(c) SGA/E-MAP colony size generally** — exists as a modality; the specific osmostress datasets covering HOG doubles were **NOT RETRIEVED**.

### 5.3 Bottom line for item 5

| Readout | Exists? | Covers singles? | Covers the redundancy doubles? |
|---|---|---|---|
| Qualitative plate streak/spot +/- | ✅ | ✅ | ✅ — **this is the only one that does** |
| Semi-quantitative 10-fold spot dilution | ✅ | ✅ | partially (Babazadeh) |
| Growth rate / doubling time (min) | ✅ (Petelenz-Kurdziel) | ✅ (`hog1Δ`, `gpd1Δ`) | ❌ |
| Colony-size fitness / S-score under osmostress | ✅ (Martin 2015, 0.6 M sorbitol) | ✅ (Hog1, Pbs2 as queries) | ❌ (likely) |
| Survival fraction (CFU/CFU₀) | **NOT FOUND** in any retrieved source | — | — |

**No quantitative survival-fraction measurement was found for any HOG mutant.** No quantitative growth-rate measurement was found for **any** of the branch-deletion double mutants. **The load-bearing redundancy claim rests entirely on eyeballed plate growth.**

---

## 6. PUBLISHED DYNAMICAL MODELS AND WHAT THEY WERE FITTED TO — the decisive item

**Headline: the answer is SPLIT, and the split runs against the task's hoped-for outcome for the two Klipp-lab models.**

### 6.1 Klipp, Nordlander, Krüger, Gennemark & Hohmann 2005, *Nat Biotechnol* 23:975–982

**Authorship VERIFIED** (nature.com/articles/nbt1114). **Abstract RETRIEVED VERBATIM. Full text NOT RETRIEVED** (paywall; all mirrors 403).

Abstract, verbatim:

> "Integration of experimental studies with mathematical modeling allows insight into systems properties, prediction of perturbation effects and generation of hypotheses for further research. We present a comprehensive mathematical description of the cellular response of yeast to hyperosmotic shock. The model integrates a biochemical reaction network comprising receptor stimulation, mitogen-activated protein kinase cascade dynamics, activation of gene expression and adaptation of cellular metabolism with a thermodynamic description of volume regulation and osmotic pressure. Simulations agree well with experimental results obtained under different stress conditions or with specific mutants. The model is predictive since it suggests previously unrecognized features of the system with respect to osmolyte accumulation and feedback control, as confirmed with experiments. The mathematical description presented is a valuable tool for future studies on osmoregulation in yeast and—with appropriate modifications—other organisms. It also serves as a starting point for a comprehensive description of cellular signaling."

- **(a) Size:** **NOT RETRIEVED.** No species/reaction/parameter counts obtained. Multiple routes tried (Nature full text, BioModels, two review chapters, a Schaber biophysics paper) — all returned NOT PRESENT or 403.
- **(b) Formalism:** **NOT RETRIEVED.** The abstract's "biochemical reaction network ... with a thermodynamic description of volume regulation" is consistent with mixed mass-action + biophysical, but this is **INFERRED, not established.**
- **(c) Fitting data:** **NOT RETRIEVED, and CONTESTED.** The abstract says *"Simulations agree well with experimental results obtained under different stress conditions or with specific mutants."* This is deliberately ambiguous between **fitting** and **validation**. **I cannot determine from retrieved material whether mutant data entered the objective function.** ⚠️ **Do not assume this model is WT-only-fitted.**

### 6.2 Zi, Liebermeister & Klipp 2010, *PLoS ONE* 5(4):e9522

**FULL TEXT RETRIEVED** (journals.plos.org, open access). **Confidence: HIGH.** This is the **cleanest result in item 6.**

- **(a) Size:** **22 fitted parameters.** Verbatim: *"With 22 optimized parameter values, the model fits several hundreds of experimental data points very well."* Total species count not stated in main text: *"The initial conditions, parameter values, and the whole system of ordinary differential equations are provided in the Tables S1, Table S2, Table S3."* State variables include Pbs2 phosphorylation, cytoplasmic and nuclear Hog1 phosphorylation, glycerol production with a transcriptional delay chain, volume and pressure.
- **(b) Formalism:** **predominantly mass-action, with Hill functions at two points.** Verbatim: *"All other reactions included in this model are modeled by mass-action kinetics. We did not choose Michaelis-Menten kinetics for these signaling transduction steps because this would require that the total concentration of the enzyme (also being a substrate in signaling pathways) concentration is much smaller than the substrate concentration, which may not be valid."* Pbs2 phosphorylation is *"modeled with a Hill function using turgor pressure as input."*
- **(c) Fitting data — DECISIVE, verbatim:**

> "We estimated 22 unknown parameters values of the model by fitting to several hundreds of data points generated from 13 different conditions of NaCl stimulations. We used these data sets from Mettetal *et al.* for parameter estimation: the data sets for constant 0.2 M NaCl stimulation ([Fig. 2D] in reference [10]), 0.2 M NaCl pulse stimulation at different frequencies ([Fig. S2] in reference [10]) and different strength of NaCl pulse stimulation ([Fig. S5] without CHX in reference [10])."

> "It was worth noting that these experimental data had not been used for the parameter estimation of the model" — stated when introducing validation against `ptp2Δ`/`ptp3Δ` mutants.

**Verdict: FITTED TO WILD-TYPE DATA ONLY** (Mettetal et al. microfluidic Hog1 timecourses). Mutant data (`ptp2Δ`, `ptp3Δ` — phosphatases, *not* branch mutants) were held out for validation. ✅ **Branch/double-deletion data was NOT used in fitting. The answer key would be independent of this fit.**

### 6.3 Schaber, Baltanas, Bush, Klipp, Colman-Lerner 2012, *Mol Syst Biol* 8:622 — "Modelling reveals novel roles of two parallel signalling pathways and homeostatic feedbacks in yeast"

**FULL TEXT RETRIEVED** (embopress → link.springer.com mirror). **Confidence: MEDIUM-HIGH.**

- **(a) Size:** ensemble of **192 candidate models**; best model "Nr. 22" had *"20 free parameters"*, fitted against ~390 data points, described as *"the lowest ratio of parameters to data points of all published HOG models."* Total species/reaction counts **NOT RETRIEVED**; components depicted include Hog1, Pbs2, Ssk2/Ssk22, Sho1, Ste11, Fps1, Gpd1, mRNA, protein, glycerol.
- **(b) Formalism:** **phenomenological in part.** Verbatim: *"Hog1 modification of glycerol production was modelled by a simple heuristic approach owing to the lack of a detailed mechanism."*
- **(c) Fitting data — DECISIVE, and it goes the WRONG WAY for the benchmark.** Datasets used in fitting, verbatim:

> "Hog1 phosphorylation of Sln1 branch mutant (*ste50*Δ) for different osmotic shocks"
> "Hog1 phosphorylation of Sho1 branch mutant (*ssk2*Δ *ssk22*Δ) for several osmotic shocks"
> "mRNA, Gpd1 and glycerol time series for 0.5 M NaCl"
> "Hog1 phosphorylation of Sho1 and Sln1 branch mutants of Hog1as strain upon addition of 5 μM Hog1 inhibitor SPP86"
> "Hog1 phosphorylation of wild‐type and *Fps1*Δ*1* mutant for 0.4 M NaCl, whereas only the *Fps1*Δ*1* was used for fitting"

⚠️ **This model was fitted DIRECTLY to branch-deletion mutant data**, including the **double deletion `ssk2Δ ssk22Δ`**, plus `ste50Δ` and `Fps1Δ1`. **The branch-architecture answer key is NOT independent of this fit.** (Note the naming convention in that paper: a `ste50Δ` strain is labelled the "Sln1 branch mutant" because it signals *through* Sln1 with the Sho1 branch broken, and vice versa for `ssk2Δ ssk22Δ`. Read carefully — the label names the *surviving* branch, not the deleted one.)

### 6.4 Schaber, Flöttmann, Li, Tiger, Hohmann & Klipp 2011, *PLoS ONE* 6(1):e14791 — modelMaGe / Sho1 branch

**FULL TEXT RETRIEVED** (journals.plos.org). Confidence: MEDIUM-HIGH.
- Ensemble of candidate models; e.g. model C10 with 20 parameters, simplest *"C5c only having five components"* with three fitted parameters.
- **Fitted to:** *"Saccharomyces cerevisiae cells BY4741 ssk1Δ"* — phospho-Hog1 Western timecourses after KCl shock.
- ⚠️ **Fitted to a branch-deletion mutant (`ssk1Δ`).** Not independent.

### 6.5 Muzzey, Gómez-Uribe, Mettetal & van Oudenaarden 2009, *Cell* 138:160–171

**Authorship confirmed only from search-result listings and a PMID (19596242) — title verified, author order NOT independently verified.**
**FULL TEXT NOT RETRIEVED.** cell.com 403 (both URL forms), sciencedirect 403, PMC captcha, researchgate not attempted/blocked. Two review chapters that cite it gave NOT PRESENT for model details.
- **(a) size / (b) formalism / (c) fitting data: ALL NOT RETRIEVED.**
- The task called this a decisive item. **For Muzzey 2009 I have nothing beyond the title.** Do not use.

### 6.6 Mettetal, Muzzey, Gómez-Uribe & van Oudenaarden 2008, *Science* 319:482 — "The Frequency Dependence of Osmo-Adaptation in *S. cerevisiae*"

**NOT RETRIEVED** (science.org 403, semanticscholar empty). Known only as the **source of the wild-type microfluidic data that Zi et al. 2010 fitted** (per §6.2, which names it explicitly). Its own model is a low-order/linear-systems description; **this is INFERRED from the Zi description, not retrieved.**

### 6.7 Item 6 summary table

| Model | Retrieved? | Size | Formalism | Fitted to | Branch/double-deletion data in the FIT? |
|---|---|---|---|---|---|
| Klipp et al. 2005 | Abstract only | NOT RETRIEVED | NOT RETRIEVED | ambiguous — "different stress conditions or with specific mutants" | ⚠️ **UNKNOWN / CONTESTED** |
| **Zi, Liebermeister & Klipp 2010** | **Full text** | 22 fitted params | mass-action + 2 Hill terms | **Mettetal WT microfluidic Hog1 data, 13 NaCl conditions** | ✅ **NO — WT only.** Mutants (`ptp2Δ`,`ptp3Δ`) held out for validation |
| Schaber et al. 2012 | Full text | 20 free params, 192-model ensemble, ~390 data pts | partly heuristic | `ste50Δ`, **`ssk2Δ ssk22Δ`**, `Fps1Δ1`, Hog1as | ❌ **YES — directly** |
| Schaber et al. 2011 (modelMaGe) | Full text | 5–10 species, 3–20 params | ODE ensemble | **`ssk1Δ`** (BY4741) phospho-Hog1 | ❌ **YES** |
| Muzzey et al. 2009 | **NOT RETRIEVED** | — | — | — | **UNKNOWN** |
| Mettetal et al. 2008 | **NOT RETRIEVED** | — | — | — | **UNKNOWN** (its WT data feed Zi 2010) |
| Talemi et al. 2016 (bonus) | Full text | — | — | *"single 0.8M sorbitol hyper-osmotic shock experiment and 0.8–0.27 M sorbitol dilution experiments... the volume data for 0.8 M sorbitol"* | apparently WT — **not confirmed** |

**Item 6 verdict:** **Zi, Liebermeister & Klipp 2010 is the one model I can certify as fitted to wild-type data only**, with an explicit verbatim statement that mutant data were withheld from estimation. It is the only model in this dossier for which a branch-deletion answer key is demonstrably **independent of the fit**. The two Schaber models are **disqualified** on this criterion. Klipp 2005 and Muzzey 2009 are **unknown** and cannot be used without manual retrieval.

---

## 7. HONEST ASSESSMENT: solid vs contested

### 7.1 Solid

1. **Two-branch convergent architecture on Pbs2→Hog1.** Quoted from a retrieved review by the discoverers and corroborated by a retrieved independent primary paper. As solid as anything in yeast signalling.
2. **Cross-branch redundancy at the level of plate growth.** O'Rourke & Herskowitz 1998 Figure 5A is a well-controlled single-figure demonstration with an internal same-branch negative control. This is the strongest single piece of evidence in the dossier.
3. **`GPD1`/`GPD2` division of labour.** Cleanly quoted abstract + results, one lab, one figure logic.
4. **`SKN7` as a non-contributor to osmotolerance.** Clean single quoted sentence.

### 7.2 Contested / complicating — each of these is a disqualification risk

**(a) Is Sho1 an osmosensor at all?** This is a live, *acknowledged* dispute, and the answer in the current literature is essentially "no, it's a co-osmosensor/scaffold."
- Tatebayashi et al. 2007, RETRIEVED: *"neither the osmosensor nor the signal generator of the SHO1 branch has been clearly defined"* and *"It has not, however, been experimentally determined if Sho1 serves an osmosensor function as originally postulated."*
- Saito & Posas 2012, RETRIEVED: *"A signaling response in the Sho1 branch is initiated by the putative osmosensors Msb2 and Hkr1, which are highly glycosylated single-pass TM proteins"*, acting through *"an as-yet-undefined mechanism that seems to involve an interaction between the Msb2/Hkr1 osmosensors and the Sho1 co-osmosensor."*
- **Impact:** Sho1's *mechanistic role label* is contested. Its *genetic* role (essential for the SHO1-branch signal, redundant with the SLN1 branch) is **not** contested. **An answer key may use Sho1 as a genetic node; it must not label Sho1 "the osmosensor."**

**(b) Pheromone/FIG pathway cross-talk and `ste11Δ`/`ste20Δ`/`ste50Δ` pleiotropy.**
- Saito & Posas 2012, RETRIEVED: *"three of these pathways (HOG, mating, and FIG) share many of the same signaling elements, including the Ste11 MAPKKK."*
- O'Rourke & Herskowitz 1998's entire thesis is that Hog1 *prevents* cross-talk — i.e. in `hog1Δ` and `pbs2Δ` backgrounds, osmostress inappropriately fires the pheromone pathway. **This means `hog1Δ` and `pbs2Δ` phenotypes are not "clean loss of osmoadaptation"; they include a gain of inappropriate signalling.** For a mechanism-attribution benchmark this is a real confound.
- Msb2 is also a FIG-pathway sensor, so the `msb2Δ hkr1Δ` synergy inherits a version of the same problem.
- **Impact:** `ste11Δ`-, `ste20Δ`-, `ste50Δ`- and `msb2Δ`-based entries carry a cross-pathway confound. `sho1Δ` × `ssk1Δ` is the cleanest.

**(c) `ssk1Δ` vs `ssk2Δ ssk22Δ` — not interchangeable.** §2.3. `ssk1Δ sho1Δ` retains *"slight activation of the Hog1 MAPK"*; only `ssk2Δ ssk22Δ sho1Δ` is null. Any key that treats "the double mutant" as a single well-defined object is wrong.

**(d) Signalling readout vs growth readout can disagree.** `ssk1Δ sho1Δ` shows residual phospho-Hog1 (Saito & Posas) but fails to grow at 1 M NaCl (O'Rourke & Herskowitz). A benchmark that scores "does the pathway still signal?" and one that scores "does the cell still grow?" would get different answers for this genotype.

**(e) Strain background.** **NOT ADDRESSED BY ANY RETRIEVED SOURCE.** I prompted Saito & Posas 2012 specifically for strain-background dependence and the extraction returned *"The provided text does not address strain-background dependence of HOG phenotypes."* O'Rourke & Herskowitz used their own (unretrieved) strains; Schaber's modelMaGe fits used **BY4741**; Babazadeh used unstated strains. **The redundancy phenotype's strain-robustness is UNVERIFIED.** Given that HOG-pathway and FIG-pathway phenotypes are famously background-dependent in yeast (Σ1278b vs S288C), **this is a genuine open risk, not a formality.**

**(f) Hog1 activation is not sufficient for osmoadaptation.** Surfaced but **NOT RETRIEVED**: Vázquez-Ibarra et al. 2018, *FEBS J* — *"Activation of the Hog1 MAPK by the Ssk2/Ssk22 MAP3Ks, in the absence of the osmosensors, is not sufficient to trigger osmostress adaptation in Saccharomyces cerevisiae"* (title only, from a search-result listing; wiley 403). If correct, this complicates any model that treats phospho-Hog1 as the sole determinant of growth outcome. **Flagged as a lead to chase, not as evidence.**

**(g) `FPS1` direction-of-effect.** I was unable to retrieve any statement of the `fps1Δ` osmostress growth phenotype. Fps1 is a glycerol *efflux* channel whose closure is part of adaptation, so its deletion plausibly *increases* osmotolerance — the opposite sign from every other component here. **NOT RETRIEVED; do not include Fps1 in a key.**

**(h) SGD annotation conflicts with primary data** (§2.5). `sho1Δ` is annotated "osmotic stress resistance: decreased" while the primary figure says it grows like WT. **Curated-database phenotype fields are unusable as ground truth for this system.**

### 7.3 What would disqualify entries from a scored key

- **Any entry using `hog1Δ`/`pbs2Δ` as a citation-backed "essential" call** — the primary passage (Brewster 1993) is NOT RETRIEVED here (§3).
- **Any entry labelling Sho1 an osmosensor** (§7.2a).
- **Any entry involving `STE11`, `STE20`, `STE50`, `MSB2`** without a cross-pathway-confound annotation (§7.2b).
- **Any entry that conflates `ssk1Δ` with `ssk2Δ ssk22Δ`** (§7.2c).
- **Any entry scored against a Schaber-family model** — those models saw branch-deletion data in fitting (§6.3, §6.4).
- **`FPS1` entries** (§7.2g).
- **Anything sourced from SGD phenotype summaries** (§7.2h).

---

## 8. COUNT — mechanisms that could carry a settled label from direct experimental evidence

**Count: 9 candidate entries. Of these, 4 are HIGH-confidence and fully quoted; 3 are MEDIUM; 2 should be excluded pending manual retrieval.**

| # | Mechanism | Label | Confidence | Source (quoted passage located at) |
|---|---|---|---|---|
| 1 | `sho1Δ` × `ssk1Δ` — singles grow like WT at 1 M NaCl, double osmosensitive; same-branch control `ste50Δ sho1Δ` is resistant | **REDUNDANT** | **HIGH** | O'Rourke & Herskowitz 1998, *Genes Dev* 12:2874, Fig 5A — §2.2 |
| 2 | `ste50Δ` × `ssk1Δ` — same pattern, 1 M NaCl | **REDUNDANT** | **HIGH** (⚠️ Ste50 pleiotropy) | same, Fig 5A — §2.2 |
| 3 | `ste20Δ` × `ssk1Δ` — same pattern but only at 1.2 M NaCl | **REDUNDANT (dose-shifted)** | **HIGH** (⚠️ Ste20 pleiotropy) | same, Fig 5A — §2.2 |
| 4 | `SKN7` — connected to the Sln1 phosphorelay, deletion has no osmostress phenotype | **INERT / spectator** | **HIGH** | Saito & Posas 2012, *Genetics* 192:289 — §4.1 |
| 5 | `GPD2` — deletion "behaved like the wild-type strain" at high salinity | **INERT / spectator** | **HIGH** | Ansell et al. 1997, *EMBO J* 16:2179 — §4.2 |
| 6 | `GPD1` × `GPD2` — `gpd2Δ` inert, `gpd1Δ` impaired, double "very severe growth defect at high salinity" | **SYNERGISTIC (partial)** | **HIGH** | Ansell et al. 1997 — §4.2 |
| 7 | `MSB2` × `HKR1` (in `ssk2Δ ssk22Δ` bg) — both singles confer "no osmosensitivity", double "severely osmosensitive" | **SYNERGISTIC (clean 0+0→1)** | **MEDIUM** (assay conditions not retrieved; FIG confound) | Tatebayashi et al. 2007, *EMBO J* — §4.2 |
| 8 | `ssk2Δ ssk22Δ` × `sho1Δ` — the true signalling-null combination; no Hog1 activation | **REDUNDANT (canonical form)** | **MEDIUM** (phospho readout retrieved; the *growth* data is second-hand via O'Rourke's Intro) | Saito & Posas 2012 + O'Rourke & Herskowitz 1998 Intro — §2.3 |
| 9 | `SSK1` is *not* strictly equivalent to `SSK2/SSK22` — residual Hog1 activation in `ssk1Δ sho1Δ` | **PARTIAL REDUNDANCY within the SLN1 branch** | **MEDIUM** | Saito & Posas 2012 — §2.3 |
| — | `HOG1` — deletion abolishes osmoadaptation | ESSENTIAL (conditional) | **EXCLUDE pending retrieval** — no primary passage; only SGD summary + presupposition + E-MAP ranking | §3 |
| — | `PBS2` — deletion abolishes osmoadaptation | ESSENTIAL (conditional) | **EXCLUDE pending retrieval** — no phenotype passage retrieved at all | §3 |

**Nine, dropping to seven if you require the "clean" (non-pleiotropic) subset, and to a core of four if you additionally require both a quoted single-mutant control and a quoted double-mutant phenotype from the same retrieved figure: entries 1, 2, 3 and 6.**

The two entries a benchmark would most want — `hog1Δ` and `pbs2Δ` as ESSENTIAL — are the two I cannot certify, purely for retrieval reasons. One manual PDF pull of Brewster et al. 1993, *Science* 259:1760 would move both to HIGH.

---

## 9. RETRIEVAL LEDGER

**Full text retrieved, quotes obtained:**
- O'Rourke & Herskowitz 1998, *Genes Dev* 12:2874 — genesdev.cshlp.org
- Saito & Posas 2012, *Genetics* 192:289 — academic.oup.com (**partial**: repeated fetches surfaced different sections; coverage is incomplete)
- Ansell et al. 1997, *EMBO J* 16:2179 — link.springer.com
- Tatebayashi et al. 2007, *EMBO J* — link.springer.com
- Zi, Liebermeister & Klipp 2010, *PLoS ONE* 5:e9522 — journals.plos.org
- Schaber et al. 2012, *Mol Syst Biol* 8 — link.springer.com (embopress redirect)
- Schaber et al. 2011, *PLoS ONE* 6:e14791 — journals.plos.org
- Petelenz-Kurdziel et al. 2013, *PLoS Comput Biol* 9:e1003084 — journals.plos.org
- Babazadeh et al. 2014, *Sci Rep* 4:4697 — nature.com
- Talemi et al. 2016, *Sci Rep* 6:30950 — nature.com
- Martin et al. 2015, *Mol Syst Biol* — limlab.ucsf.edu **(third-party mirror; publisher metadata not independently confirmed)**
- Nguyen/co-authors 2020 bioRxiv 2020.04.20.051599 — biorxiv.org

**ABSTRACT ONLY:**
- Klipp, Nordlander, Krüger, Gennemark & Hohmann 2005, *Nat Biotechnol* 23:975 — nature.com

**NOT RETRIEVED (nothing beyond title/bibliography):**
- Brewster, de Valoir, Dwyer, Winter & Gustin 1993, *Science* 259:1760
- Maeda, Wurgler-Murphy & Saito 1994, *Nature* 369:242
- Maeda, Takekawa & Saito 1995, *Science* 269:554
- Posas & Saito 1997, *Science* 276:1702
- Posas et al. 1996, *Cell* 86:865
- Hohmann 2002, *Microbiol Mol Biol Rev* 66:300 (full text)
- Muzzey, Gómez-Uribe, Mettetal & van Oudenaarden 2009, *Cell* 138:160
- Mettetal, Muzzey, Gómez-Uribe & van Oudenaarden 2008, *Science* 319:482
- Costanzo et al. 2010 / 2016 / 2021 (SGA); Collins et al.; Schuldiner et al. (E-MAP)
- Tatebayashi et al. 2006, *EMBO J* 25:3033 (Cdc42/Ste50/Sho1 adaptor functions)
- Vázquez-Ibarra et al. 2018, *FEBS J*
- Hohmann 2009, *FEBS Lett* (Control of high osmolarity signalling)
- SGD annotation tables (rendered client-side; only summary lines retrieved)

**Recommended manual pulls, in priority order:** (1) Brewster 1993 *Science* — unlocks items 3 and 8; (2) Klipp 2005 *Nat Biotechnol* Supplementary — the single unresolved question in item 6; (3) Muzzey 2009 *Cell* Supplementary — the other unresolved model; (4) Maeda 1995 *Science* — the original `ssk2Δ ssk22Δ sho1Δ` growth data; (5) Costanzo 2021 *Science* — the only plausible source of quantitative fitness for HOG doubles under stress.

---

# 10. MODEL REPRESENTATIONAL ADEQUACY

**Added 2026-07-25 in response to the coalition-object requirement.**

**Requirement being tested:** the dynamical model must represent the SLN1 branch and the SHO1 branch as **distinct, separately deletable paths**, plus Pbs2 and Hog1, and must produce an output mappable onto growth/survival under osmostress.

## 10.1 Zi, Liebermeister & Klipp 2010, *PLoS ONE* 5(4):e9522

Source: journals.plos.org full text, re-fetched specifically for this question. **Confidence: HIGH** — the authors state the answer explicitly and in their own voice.

### Q1 — Are the SLN1 and SHO1 branches separate species/reactions? **NO. They are absent from the model entirely.**

The paper says this itself, unambiguously (verbatim):

> "Although our previous comprehensive model contained a phospho-relay system, in which the SLN1 and SHO1 branches sense the osmotic stress signal and both activate the MAPKK, Pbs2. Here, we simplified and modeled the phosphorylation of Pbs2 with a Hill function using turgor pressure as input."

> "Here, we simplified and modeled the phosphorylation of Pbs2 with a Hill function using turgor pressure as input (Equation 4)."

The model's declared scope, verbatim:

> "The model accounts for the following processes: (1) biophysical changes including internal pressure, external pressure, turgor pressure, and volume changes... (2) The phosphorylation and dephosphorylation of Pbs2 and Hog1; (3) Hog1 nuclear-cytoplasmic shuttling; (4) The regulation of glycerol production and leakage."

**There is no Sln1, no Ypd1, no Ssk1, no Ssk2, no Ssk22, no Sho1, no Ste11, no Ste20, no Ste50, no Msb2, no Hkr1.** The most upstream signalling species in the model is **Pbs2**, and its phosphorylation rate is a **Hill function of turgor pressure** — a single scalar input term. The entire two-branch architecture that constitutes the answer key has been deliberately collapsed into one sigmoid.

Corroborating detail (verbatim): during estimation the authors found

> "a large value of the Hill coefficient (with a value of 8 in this model) is necessary for fitting the experimental data sets well, which suggests a non-linear cooperative effect for Pbs2 phosphorylation in the phospho-relay system."

The Hill coefficient of 8 is doing the work that the upstream network would otherwise do — it is a *lumped stand-in* for the phosphorelay, explicitly acknowledged as such.

⚠️ **Provenance flag on Equation 4.** The intermediary extraction reported that "the equation itself is displayed as an image" and then produced a formula (`v_phos_Pbs2 = kphos_Pbs2 * (PIt^n)/(Kphos_Pbs2^n + PIt^n)`). **That formula is almost certainly reconstructed by the extraction model from an image it could not read. I do not treat it as retrieved and it should not be quoted.** The *prose* statement that Pbs2 phosphorylation is a Hill function of turgor pressure is retrieved and reliable; the algebraic form is not.

**SBML deposit — NONE.** Verbatim:

> "most current systems biology markup language (SBML) supporting tools cannot deal with these situations. The Matlab source code for the model and simulations is provided in Code S1."

So there is no BioModels/SBML species list to check, because the authors deposited MATLAB rather than SBML, citing SBML's inability to express their formulation. The supplementary that would settle the species list independently is **Table S3, "Complete list of ordinary differential equations and other equations"** (`https://journals.plos.org/plosone/article/file?type=supplementary&id=10.1371/journal.pone.0009522.s013`) — **NOT RETRIEVED** (HTTP 400; binary document type the fetcher could not render). Table S1 (`.s011`, initial conditions) and Code S1 (`.s014`, MATLAB) likewise not retrieved. **However, the main-text prose above is decisive on its own and does not depend on the supplementary.**

### Q2 — Can `sho1Δ` and `ssk1Δ` / `ssk2Δ ssk22Δ` be represented as a parameter set to zero or a species removed? **NO. The operation is undefined on the model as published.**

There is no parameter, species or reaction corresponding to either branch. Setting the single Pbs2-phosphorylation Hill term to zero represents **"both branches destroyed simultaneously"** — it is equivalent to `pbs2Δ`, not to any single-branch deletion. The model cannot distinguish `sho1Δ` from `ssk1Δ` from `ssk1Δ sho1Δ`, because it contains no variable on which those three genotypes differ. **A branch deletion is not a well-defined operation on this model.**

Any attempt to fix this — splitting the Hill term into two additive branch terms — would be **new modelling**, would introduce parameters that were never estimated, and would be a structure whose behaviour under deletion is *chosen by whoever writes it* rather than inherited from the publication. That reintroduces exactly the answer-key contamination the WT-only-fit criterion was meant to exclude.

### Q3 — Does the model output anything mappable onto growth or survival? **NO.**

Outputs are, verbatim: *"nuclear phosphorylated Hog1 (denoted as Hog1PPn in the model)... Hog1 phosphorylation... nuclear Hog1 localization... glycerol... volume changes... turgor pressure."*

The only occurrence of "growth" anywhere in the retrieved text is an explicit statement that growth is **excluded**:

> "Although cell growth is observed after cell adaption to osmotic stress, we ignore the effect of cell growth on the volume change during the time scale of osmo-adaption."

No sentence containing "viability", "survival" or "fitness" was found. **The model has no growth, survival or fitness variable, by the authors' own design decision.**

This compounds the problem identified in §5 and §7.2(d): the benchmark's answer key is a **growth** phenotype, the model emits **phospho-Hog1**, and those two readouts are **documented to disagree for precisely the genotype in question** (`ssk1Δ sho1Δ` retains "slight activation of the Hog1 MAPK" per Saito & Posas 2012, yet fails to grow at 1 M NaCl per O'Rourke & Herskowitz 1998). Any phospho-Hog1 → growth mapping bolted onto this model would therefore be **not merely unvalidated but actively contradicted by the retrieved literature** at the one data point that matters most.

### Verdict on Zi 2010: **FAILS ALL THREE CRITERIA.**

## 10.2 Klipp, Nordlander, Krüger, Gennemark & Hohmann 2005

**Re-retrieval NOT POSSIBLE this session** — nature.com yields abstract only (§6.1); all mirrors 403; the WebSearch budget for this session is exhausted (200/200), so no new routes could be surfaced.

**What can nevertheless be said, from the Zi 2010 quote:** Zi et al. describe *"our previous comprehensive model"* as one that *"contained a phospho-relay system, in which the SLN1 and SHO1 branches sense the osmotic stress signal and both activate the MAPKK, Pbs2."* Zi and Klipp are the same lab, and Klipp et al. 2005 is the Klipp-lab comprehensive osmotic-shock model. **INFERRED, not asserted:** the branch-containing predecessor is Klipp et al. 2005.

If that inference holds, then:
- **Q1: likely YES** — Klipp 2005 probably does contain SLN1 and SHO1 as separate paths converging on Pbs2. *Inferred from a third party's description; the Klipp 2005 species list is NOT RETRIEVED.*
- **Q2: unknown.** Whether branch deletion is a clean parameter-zeroing operation depends on the actual reaction structure. NOT RETRIEVED.
- **Q3: NOT RETRIEVED.** The abstract describes "adaptation of cellular metabolism with a thermodynamic description of volume regulation and osmotic pressure" — no mention of growth, survival or fitness. There is no positive evidence of a growth output.

**And this is the trap.** Klipp 2005 is the model most likely to *have* the branches — and it is exactly the model whose fitting provenance is **ambiguous and unresolved** (§6.1: *"Simulations agree well with experimental results obtained under different stress conditions or with specific mutants"* — fitting or validation, unstated). **The candidate set is structured so that the model with the required architecture is the one that may have seen the answer key, and the model that certifiably did not see the answer key lacks the architecture.**

## 10.3 Muzzey, Gómez-Uribe, Mettetal & van Oudenaarden 2009

**NOT RETRIEVED** — cell.com and sciencedirect 403 on both URL forms, PMC captcha, search budget exhausted. **All three questions unanswered.** From its title and framing (perfect adaptation, integral feedback) it is a low-order control-theoretic description of the osmo-adaptation loop, which makes branch-resolved upstream structure *a priori* unlikely — but that is **speculation, not evidence, and should not be recorded as a finding.**

## 10.4 BioModels

**NOT RETRIEVED.** `ebi.ac.uk/biomodels` returned HTTP 403 on a direct entry page and persistent HTTP 429 from the fetch proxy across three attempts separated by 60–90 s waits. The search-based route to enumerate curated HOG entries is closed because the session WebSearch budget is exhausted. **This is the one check I was asked for and could not complete.** Note, however, that it would not have changed the Zi 2010 answer: that model has **no SBML deposit at all** (quoted in §10.1), so it cannot be in BioModels in a form that lists species.

## 10.5 BOTTOM LINE

# ❌ NOT EXECUTABLE ON PUBLISHED MODELS

Stated plainly, without softening:

1. **The only model with a certifiably clean, wild-type-only fit — Zi, Liebermeister & Klipp 2010 — does not contain the SLN1 and SHO1 branches at all.** The authors explicitly removed them and replaced the entire upstream network with a single Hill function of turgor pressure. Branch deletion is not a representable perturbation. A coalition object over the two branches cannot be computed on this model.

2. **That same model has no growth, survival or fitness output**, by explicit design ("we ignore the effect of cell growth"). It emits phospho-Hog1, nuclear Hog1, glycerol, volume and turgor. The benchmark's answer key is a growth phenotype. The mapping between them is not merely missing — it is contradicted by the retrieved literature at the `ssk1Δ sho1Δ` genotype, which is the single most important cell in the answer key.

3. **The model that plausibly does have the branches (Klipp et al. 2005) is the one whose fit provenance is unresolved**, and may have been fitted to mutant data. It fails the independence criterion, or at minimum cannot be certified as passing it, and its full text could not be retrieved.

4. The two Schaber models have the branches *and* are cleanly deletable in principle, but were **fitted directly to branch-deletion data** (`ssk2Δ ssk22Δ`, `ste50Δ`, `ssk1Δ`) — §6.3, §6.4. Disqualified on independence.

**No published HOG model simultaneously satisfies (a) wild-type-only fit, (b) branch-resolved deletable architecture, and (c) a growth/survival output.** Criteria (a) and (b) are satisfied by disjoint sets of models. Criterion (c) is satisfied by **none** of them — not one retrieved HOG dynamical model outputs growth or survival at all.

**What would change this verdict:** (i) retrieving Klipp 2005's Supplementary and finding both a branch-resolved species list *and* an unambiguous statement that fitting used wild-type data only — this is the only realistic path, and it is a coin-flip on the second condition; (ii) retrieving Muzzey 2009 and finding branch-resolved structure — unlikely on priors. **Neither path solves criterion (c).** Even in the best case the benchmark would need a phospho-Hog1 → growth mapping that no publication provides and that the `ssk1Δ sho1Δ` disagreement actively undermines.
