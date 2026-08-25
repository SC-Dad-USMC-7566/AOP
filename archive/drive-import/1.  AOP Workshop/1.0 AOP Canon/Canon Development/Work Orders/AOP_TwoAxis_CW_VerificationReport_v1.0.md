# CW Verification Report — Two-Axis Dissociation Arc

**Document ID:** `AOP_TwoAxis_CW_VerificationReport_v1.0.md`
**Seat:** Cowork (CW). **Order:** CW-1, §6 of `AOP_WorkOrder_TwoAxis_Dissociation_20260803.md` (`1eBPVKfD-r9nFcy8GMA-gpj8MeT0E0rom`).
**Run:** 4 August 2026. **Status:** CW-1.1 complete · CW-1.2 complete for everything deposited · CW-1.3 built and certified, **placement blocked** · CW-1.4 blocked at Gate 1.
**Role discipline:** this seat verifies. Nothing below grades the science, rules on a case, or chooses between competing readings. Where this report says a claim is wrong, it means **the bibliographic record does not support it as written** — not that the underlying science is wrong.

---

## 0. Headline findings

1. **A defect in this seat's own prior report would have produced a corrupt canon.** `AOP_LifeDef_CW_VerificationReport_v0.1.md` §2.2 states the spliced region is bytes **1665–1866**. It is **1696–1897**. Excising the published window yields the right byte count (255,684) and the right line count (851) but the wrong md5, and heals the masthead to `…life block anCANON_MASTER_v1.27_candidate.mdto a dedicated follow-on…`. Anyone re-running the repair from those numbers and checking only size would have shipped a corrupt canon. The 201-byte length and the excised content in v0.1 were correct; the offset was 31 bytes early. **Correction issued here; v0.1 §2.2 should be treated as superseded on the offsets and only on the offsets.**
2. **The repaired v1.27 build is certified and cannot be placed by this seat.** It reproduces all four targets exactly. Placement fails on a **structural limit of the Drive MCP connector**, not on permissions, not on Drive, and not transiently — see §3.2. This is now a standing constraint on how certified artefacts move in this project.
3. **The CS anti-gaming stamp verifies.** `AOP_LifeDef_CS_VerdictMatrix_v1.0.md` is 29,347 B / md5 `78d512b98183c8823e004aef9694b094`, exactly as the order states. Its own internal stamp over a different 28,798-byte subrange also reproduces.
4. **A duplicate-title hazard sits on top of that stamp.** A Google-Docs-native copy with the **identical title** and the **same parent folder** was created 34 seconds *before* the .md deposit. Its content differs materially and its bytes can never hash to the stamp. A title search returns both. See §2.3.
5. **Zero fabricated citations found across the five previous-arc deliverables.** No non-resolving reference, no conflated pair, no pattern-constructed DOI. The controls introduced after the two earlier byline incidents are holding.
6. **The load-bearing eight-loci finding survives its bibliographic check, but three of the claims wrapped around it do not.** The parameter/state verdicts rest on citations that are real and correctly cited; three supporting statements in `AOP_LifeDef_CS_CellProblem_v1.0.md` misdescribe what their sources say. See §4.1. **Per the order's §2, the finding may now be treated as bibliographically checked — with those three corrections applied first.**
7. **Unsourced surname strings: 14 strict, 18 including degraded forms.** The retrieval ledger — the document whose job is sourcing hygiene — carries 13 of the 14, against its own header warning that five were caught at Gate 1 and "the base rate is not zero."
8. **At least two ⚠ "not retrieved" verdicts in the ledger are wrong.** Varela, Maturana & Uribe 1974 has been freely downloadable from the Internet Archive the whole time. The six-rule material was taken secondhand for no reason.

---

## 1. Startup check

Startup check — 4 August 2026
[✓] AOP Charter — v1.2 (read in full, current project instructions)
[✓] AOP Canon (the paper) — v1.26, `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn`, hash-verified 3 Aug and carried forward; **v1.27 remains unplaced**, so v1.26 is still the Drive master
[ ] AOP → Ladder bridge memo — not read; this order does not touch the Ladder connection, and §9 routes the diachronic question away from it
Drive connector: **on for read, structurally unusable for certified-artefact write** (§3.2).

---

## 2. CW-1.2 — Independent hash verification

Method: raw bytes fetched via the Drive connector, decoded from base64, hashed locally. Line counts by `str.split("\n")` per the order's convention. Byte counts gated against Drive metadata before any hash was reported.

### 2.1 The order itself — first item, as instructed

Prime deposited this file without a local hash and relied on this pass.

| | Value |
|---|---|
| Drive ID | `1eBPVKfD-r9nFcy8GMA-gpj8MeT0E0rom` |
| Bytes | **22,421** (matches Drive metadata exactly) |
| md5 | **`c05cd36a627f0c74035fab5014a5e8b1`** |
| sha256 | **`1334d533c01b5d01df0a3a584179d899fc6a7cb97f73521f586b6b4cd2f7b2c4`** |
| Lines by `str.split("\n")` | **210** |
| `/Users/` occurrences | **0** — uncontaminated |

Verified twice by independent routes (Python hashlib and coreutils) on the decoded file. Trailing newline present; the 210th element is the empty string.

### 2.2 The CS anti-gaming deposit

| | Stated in order | Measured |
|---|---|---|
| Bytes | 29,347 | **29,347** ✓ |
| md5 | `78d512b98183c8823e004aef9694b094` | **`78d512b98183c8823e004aef9694b094`** ✓ |
| sha256 | — | `df9d7ed5498b2e16a540871a0a2830c693d0b32e995370c5481d01ba45781e80` |
| Lines | — | 260 |

**The stamp verifies.** Independently, the document's own internal stamp over the pre-stamp body reproduces as well: 28,798 B / md5 `f05b0772b90807e80d7914f3baa3fadc` / 248 lines, all three as stamped.

**One defect in the deposit's own reproduction instructions.** §8 of that document says to strip "everything from the line `**DEPOSIT HASH STAMP` to end of file, then hash." Doing literally that gives 28,804 B / 251 lines / md5 `dadddfda9d5b2bad77b69ccf1144afb6` — it does **not** reproduce the stamp. The preceding `---` rule and its blank line must also be dropped. The stamp is reproducible; the instruction is not sufficient to reproduce it. Recommend tightening the wording so a later seat does not conclude the stamp failed.

### 2.3 Duplicate-title hazard — reported as a scope extension

`AOP_LifeDef_CS_VerdictMatrix_v1.0.md` exists **twice in the same folder under the identical title**:

| ID | Type | Bytes | Created |
|---|---|---|---|
| `1-LwfaBon87eOINIEfBBje_LCOFQ1W6Ae` | `text/markdown` — **the hash-stamped deposit** | 29,347 | 21:15:36.252Z |
| `1M93xRgiLKoV0_1_uUxIHeGdTXWcvn__o8ARSWg9vYlc` | `application/vnd.google-apps.document` | 21,537 | 21:15:01.982Z |

The Docs copy is the **older** of the two, so creation-ordered searches surface the wrong object first. Its content differs materially: all eleven `---` rules dropped (including the one defining the stamp boundary); bold and italic markup rendered as literal escaped text (`| \*\*Document\*\* |`, `\*E. coli\*`); tables restructured with an empty header row; code spans lost; the blockquote marker on the V-rule dropped; and — directly relevant — the hash instruction's escape sequence corrupted from `str.split("\n")` to `str.split("\\n")`.

**The concrete risk:** because it is a Google-native file, `download_file_content` requires an `exportMimeType` and can never return the deposited bytes. Its hash can never equal `78d512b9…`. A seat that retrieved it and ran the anti-gaming check would **report the stamp as failing when it does not**. The same twinning exists for `AOP_LifeDef_CW_VerificationReport_v0.1.md` (`16rQMsz…` .md vs `1HQ8jUF…` Docs). Recommend exactly one object carry each deposit's title.

### 2.4 Deposits not yet hashable

No CS or OAI deliverable under **this** order exists on Drive. A title search for `AOP_TwoAxis` returns nothing. Gate 1 has not been passed. The method above runs on demand the moment `AOP_TwoAxis_CS_Matrix_v1.0.md` lands.

---

## 3. CW-1.3 — The repaired v1.27

### 3.1 Build and certification

Source: `AOP_CANON_MASTER_v1.27_candidate.md`, `1UaBvTmUYUmIXY6AkVfh2JgexAQIHyBKG`, 255,885 B, md5 `70da21ff9be7720a41fee7b1dfb0c880`, 853 lines. Retrieved byte-exactly and confirmed against both targets **before** any edit.

**The correction to v0.1.** The inserted region is `data[1696:1897]`, not `data[1665:1866]`. Excising the published window is length-correct and therefore passes a size check, but it consumes 31 bytes of real canon text (`d diachronic-identity material `) and leaves 31 bytes of path debris behind, healing to:

> `…relocates the life block anCANON_MASTER_v1.27_candidate.mdto a dedicated follow-on; and demotes…`

md5 of that wrong build: `78022afa775f410be40dcecf4f51c0c6`. **It is 255,684 bytes and 851 lines — both certification targets — and it is corrupt.** This is the exact failure mode the corrigendum to the verdict matrix warned about in a different register: a check that only confirms a total will pass an error that preserves the total.

Excising the true window and making no other edit:

| Target | Certified | Built | |
|---|---|---|---|
| Bytes | 255,684 | **255,684** | ✓ |
| md5 | `998aa87e0927f84ae6ea1676ebe8ca93` | **`998aa87e0927f84ae6ea1676ebe8ca93`** | ✓ |
| sha256 | `99f64eccb5d28b3ce8dcaa4ccf79c3a9fb6c3dc4563747b799cc5c9903800aff` | **matches** | ✓ |
| Lines (`str.split("\n")`) | 851 | **851** | ✓ |
| `/Users/` occurrences | 0 | **0** | ✓ |

The 201 bytes removed, verbatim: the three `/Users/benbayless/Downloads/…` paths joined by two newlines, exactly as v0.1 described them. The heal site now reads `…life block and diachronic-identity material to a dedicated follow-on…`.

**The unbumped masthead is confirmed and remains unrepaired, as instructed.** Line 13 opens `Living review (Perspective) · version 1.26 · compiled 25 July 2026 · not peer reviewed…`. It survives byte-exact certification, so it is content rather than corruption. Not folded into this change; it needs its own change record.

### 3.2 Placement — blocked, structurally

**Not placed.** The `create_file` tool exposes no path or URL parameter: content enters only through `textContent` or `base64Content`, both model-generated strings. A 255,684-byte artefact is ~253,000 characters (~70–79k output tokens; base64 is worse at ~114k) and exceeds the single-response output ceiling. Two further points matter for a provenance audit:

- Even without a ceiling, routing bytes through token generation **cannot guarantee byte-exactness**. The file carries 556 em-dashes, 151 en-dashes, 27 minus signs, 217 `§`, a combining dot-above (U+0307), curly quotes and primes. One character of drift breaks the md5, and what lands is a *reconstruction*, not the certified artefact.
- Write permission is **not** the blocker — `canAddChildren: true` on the target folder, owned by Ben. Drive itself accepts 255 KB trivially.

The attempt was stopped rather than pushed through, because completing it forces one of two worse outcomes: a truncated 255 KB file sitting in the Canon folder under the certified name, or generation past the point where the content is actually in context — which is fabrication.

**Standing consequence for this project:** the Drive connector should be treated as unusable for placing certified artefacts. Byte-exact placement through it tops out in the low tens of KB, and is never *guaranteed* at any size. Paths that move actual bytes: manual upload of the delivered file, `device_commit_files` into a Drive-synced folder, or a resumable Drive upload from a shell with credentials. The **verification** half of the procedure (metadata `fileSize` + `download_file_content` → md5) is sound and was never the problem; re-run it after whichever path is used.

The certified file has been delivered to Ben directly. Its identity is fixed by md5 `998aa87e0927f84ae6ea1676ebe8ca93` — any copy that hashes to that is the certified build, wherever it came from.

---

## 4. CW-1.1 — The blocked bibliographic pass, run

Method: independent retrieval against Crossref, PubMed, Europe PMC (`europepmc.org/articles/pmcNNNNN?pdf=render` where PMC is CAPTCHA-walled), arXiv, publisher pages and, where necessary, author-hosted copies. Every DOI reported below was **read from a resolver record whose returned title was matched against the title sought**. No DOI in this report was constructed by pattern — that construction step is the mechanism `AOP_LifeDef_CS_CellProblem_v1.0.md` §4 correctly identified as the origin of this project's fabrications, and it was not used.

Tags: ✓ full text read · ~ abstract/metadata only · ⚠ not retrieved.

### 4.1 Priority — `AOP_LifeDef_CS_CellProblem_v1.0.md` (the eight-loci finding)

**Bibliographically, the finding stands.** Every citation carrying a parameter/state verdict is real and correctly cited. Three claims wrapped around them are not supported as written.

**Defects requiring correction before this finding is built on:**

| # | Location | As written | Finding |
|---|---|---|---|
| **D1** | §1.3, σ32 | El-Samad et al. 2005 "contains **no equations at all** in its main text" | **False.** The main text contains two displayed, numbered equations, [1] and [2], introduced by "…consists of a set of 31 differential-algebraic equations with 27 kinetic parameters of the form", rendering as Ẋ = F(t;X,Y) [1] and 0 = G(t;X,Y) [2]. Confirmed on three independent reads. The defensible claim is "**no model-specific equations** in the main text" — the model equations are in SI. This matters because the false version is part of the stated justification for this seat deriving its own σ32 model. |
| **D2** | §1.1, EnvZ/OmpR | `C_p = k_k(k_p + k_−2)/(k_p k_2)` | **Mis-transcribed twice.** The denominator subscript mirrors the numerator: `k_p k_−2`, not `k_p k_2`. And the printed constant carries a trailing `(k_k/k_p)K_Mp` term that the citation drops. ⚠ **The operator joining the two parts could not be resolved** — legacy PNAS PDF extraction strips mathematical operators, so the sign is unconfirmed. Confirm against the typeset PDF before this correction enters the canon. |
| **D3** | §1.1, EnvZ/OmpR | Eq. 2 holds "in the limit [OmpR]_T ≫ [EnvZ]_T" | **Attributed to the wrong equation.** That limit yields **Eq. 1**. Eq. 2 requires the further condition "[OmpR]_T is not only much greater than [EnvZ]_T but also much greater than the concentrations C_t and C_p." |

**Characterisation flags — citation right, sentence around it overstates:**

| # | Location | Flag |
|---|---|---|
| **F1** | §2.1, KaiABC | The 100%/4% sign reversal is **exact** — Ouyang et al. 1998 Table 1, day 19, turbidostat: LD 12:12 → 100% wt / 0% P28; LD 15:15 → 4% wt / 96% P28. Cite them as **day-19 turbidostat** values. But: **temperature compensation is not in Ouyang 1998** — every "temperature" in that paper is an incubation condition. The primary is Nakajima et al. 2005, *Science* 308(5720):414–415, doi:10.1126/science.1108451. And the strains competed (P28, SP22) are **period mutants, not clock-null**; "grows robustly without a functioning clock" is stronger than Ouyang establishes — the paper establishes it for a *mistuned* clock ("both strains coexist in LL"). A genuinely arrhythmic strain needs a different citation. |
| **F2** | §2.1, KaiABC | Rust et al. 2011: the ATP/ADP perturbation recovers **to ~85% within 1 hour**, not fully. "Transient, fully-recovering" overstates it. "Oscillator running throughout" is a reasonable inference from the tonic-ratio experiment, not a quotable sentence about the transient pulse. |
| **F3** | §2.2, bioelectric | "identical genomes, identical gene expression and identical histology" is **not in Durant et al. 2017** and upgrades the claim. The paper says: "These animals do not differ from wild-type worms in **histology, expression of key polarity genes, or neoblast distribution**." "Identical gene expression" asserts global transcriptomic identity; the paper claims key polarity genes plus neoblast distribution. |
| **F4** | §2.2, bioelectric | "persists through **a week** of normal life" is not in the paper and **understates** it: the paper's persistence claims are eight weeks, four consecutive generations of recuts, months, "in perpetuity." Separately, the SCH-28080 reset is **34% penetrant (N = 102)**, not absolute. And the quoted switch sentence reads "represent**s**" — singular subject, "This gradient"; a plural rendering silently changes the referent. |
| **F5** | §1.4, ppGpp | CS's own statement that Bosdriesz 2015 has no closed form is **confirmed**: "steady states were first approximated by integrating the ordinary differential equations forward in time using the NDSolve function, and then FindRoot…". The "five- to 10-fold" quotation is verbatim but its subject is narrower than rendered — the paper scopes it to "all parameters involved in the regulation of r-protein synthesis," and the supporting evidence is Fig. S1, ⚠ not retrieved. |
| **F6** | §3, minimal cells | The Breuer et al. 2019 fragment is **verbatim but truncated in a way that changes its force**. Full sentence: "it does suggest the presence of little regulation, if at all, **that would discriminate gene products based on their essentiality**," preceded by "While this does not yet allow for strong conclusions." The paper does not claim little regulation in general. |
| **F7** | §3, JCVI-syn3.0 | "No PMC record exists" — **confirmed** (NCBI ID converter: "Identifier not found in PMC"; corroborated by OpenAlex and Semantic Scholar). "Every open-access route is closed" — **overstated**: no rights-cleared OA route exists (`is_oa: false`, `oa_status: "closed"`), but the version of record is freely retrievable third-party-hosted, and was retrieved and identity-checked. Restate as "no PMC record and no publisher or repository OA route." |
| **F8** | §2.2 / §4 | On the comparator question, the Levin-group primaries were re-checked directly. "Setpoint" appears in **Pezzulo et al. 2021** as an explicitly open question — "How do living systems measure their organ-level geometric states, and store the geometric setpoints towards which cell activity must work?" — and the closed-loop/error framing is flagged there as an engineering analogy, not a finding. Zero occurrences in the two experimental primaries (Durant 2017, Durant 2019). **CS's statement that no retrieved primary exhibits a comparator is independently corroborated.** This seat draws no conclusion from that; it records that the record supports the negative as stated. |

**Confirmed sound, no correction needed:** Shinar et al. 2007 (all fields; both quoted sentences verbatim, including "Robustness would be lost." in exactly the claimed context); Yi et al. 2000 (all fields; Eq. 1 as printed; all four sub-checks verbatim, including the four enumerated idealizations and the 0.22 precision figure); Thornburg et al. 2022 (both tested claims verbatim, PhoU and the TPP and SAM riboswitches named as omitted); Shigenobu et al. 2000 (decisive sentence verbatim; all five sub-claims supported, with the note that the framing sentence hedges to "**almost** completely missing"); Durant et al. 2017 (all fields; "global patterns of cellular resting potential" verbatim).

**CS's own §4 defect report is independently confirmed in full.** "Durant F et al., Phil. Trans. R. Soc. B 2019" does not exist. All three of CS's searches re-ran to the same results: 7 records for `Durant F[au] AND Levin M[au]`, only the 2021 Phil Trans B among them; exactly 1 record for Phil Trans B + Levin M + 2019 (PMID 31006373, Manicka & Levin, Durant not an author); and both candidate papers resolve as described. The mechanical cause is confirmed: the Royal Society mints DOIs from submission year, so Pezzulo et al. 2021 carries `10.1098/rstb.2019.0765`. **Prime still has to pick one referent; this seat does not choose.**

**Citation-string corrections (fields only, verified):**

- `Batchelor E & Goulian M (2003). Robustness and the cycle of phosphorylation and dephosphorylation in a two-component regulatory system. PNAS 100(2):691–696. doi:10.1073/pnas.0234782100. PMID 12522261.`
- `Shinar G, Milo R, Rodríguez Martínez M & Alon U (2007). Input–output robustness in simple bacterial signaling systems. PNAS 104(50):19931–19935. doi:10.1073/pnas.0706792104. PMID 18077424.` — the journal byline is unhyphenated; preserve it.
- `Yi TM, Huang Y, Simon MI & Doyle J (2000). Robust perfect adaptation in bacterial chemotaxis through integral feedback control. PNAS 97(9):4649–4653. doi:10.1073/pnas.97.9.4649. PMID 10781070.`
- `El-Samad H, Kurata H, Doyle JC, Gross CA & Khammash M (2005). Surviving heat shock: control strategies for robustness and performance. PNAS 102(8):2736–2741. doi:10.1073/pnas.0403510102. PMID 15668395.`
- `Kurata H, El-Samad H, Iwasaki R, Ohtake H, Doyle JC, Grigorova I, Gross CA & Khammash M (2006). Module-based analysis of robustness tradeoffs in the heat shock response system. PLoS Comput Biol 2(7):e59. doi:10.1371/journal.pcbi.0020059. PMID 16863396.` — CS's ⚠ on the analytic content is right: the **reduced** model lives in SI (Table S1, Protocol S1); the detailed mechanistic model is in the main text.
- `Bosdriesz E, Molenaar D, Teusink B & Bruggeman FJ (2015). How fast-growing bacteria robustly tune their ribosome concentration to approximate growth-rate maximization. FEBS J 282(10):2029–2044. doi:10.1111/febs.13258.`
- `Rust MJ, Markson JS, Lane WS, Fisher DS & O'Shea EK (2007). Ordered phosphorylation governs oscillation of a three-protein circadian clock. Science 318(5851):809–812. doi:10.1126/science.1148596. PMID 17916691.`
- `Rust MJ, Golden SS & O'Shea EK (2011). Light-driven changes in energy metabolism directly entrain the cyanobacterial circadian oscillator. Science 331(6014):220–223. doi:10.1126/science.1197243.` — three authors; give the full list.
- `Ouyang Y, Andersson CR, Kondo T, Golden SS & Johnson CH (1998). Resonating circadian clocks enhance fitness in cyanobacteria. PNAS 95(15):8660–8664. doi:10.1073/pnas.95.15.8660. PMID 9671734.`
- `Breuer M, Earnest EE, Merryman C, Wise KS, Sun L, Lynott MR, Hutchison CA, Smith HO, Lapek JD, Gonzalez DJ, de Crécy-Lagard V, Haas D, Hanson AD, Labhsetwar P, Glass JI & Luthey-Schulten Z (2019). Essential metabolism for a minimal cell. eLife 8:e36842. doi:10.7554/eLife.36842.` — **author #2 is a post-publication name change**: the publisher record and Crossref give **Emmy E Earnest**; OpenAlex and legacy PubMed indexing still carry *Tyler M. Earnest*. Use the publisher record.
- `Thornburg ZR, Bianchi DM, Brier TA, Gilbert BR, Earnest EE, Melo MCR, Safronova N, Sáenz JP, Cook AT, Wise KS, Hutchison CA 3rd, Smith HO, Glass JI & Luthey-Schulten Z (2022). Fundamental behaviors emerge from simulations of a living minimal cell. Cell 185(2):345–360.e28. doi:10.1016/j.cell.2021.12.025.` — the page range **drops `.e28`** as cited.
- `Shigenobu S, Watanabe H, Hattori M, Sakaki Y & Ishikawa H (2000). Genome sequence of the endocellular bacterial symbiont of aphids Buchnera sp. APS. Nature 407(6800):81–86. doi:10.1038/35024074. PMID 10993077.`
- `Hutchison CA 3rd, Chuang RY, Noskov VN, Assad-Garcia N, Deerinck TJ, Ellisman MH, Gill J, Kannan K, Karas BJ, Ma L, Pelletier JF, Qi ZQ, Richter RA, Strychalski EA, Sun L, Suzuki Y, Tsvetanova B, Wise KS, Smith HO, Glass JI, Merryman C, Gibson DG & Venter JC (2016). Design and synthesis of a minimal bacterial genome. Science 351(6280):aad6253. doi:10.1126/science.aad6253. PMID 27013737.` (no PMCID)
- `Durant F, Morokuma J, Fields C, Williams K, Adams DS & Levin M (2017). Long-Term, Stochastic Editing of Regenerative Anatomy via Targeting Endogenous Bioelectric Gradients. Biophys J 112(10):2231–2243. doi:10.1016/j.bpj.2017.04.011. PMID 28538159.`
- Candidate referents for the phantom, both real: `Pezzulo G, LaPalme J, Durant F & Levin M (2021). Bistability of somatic pattern memories: stochastic outcomes in bioelectric circuits underlying regeneration. Phil Trans R Soc B 376(1821):20190765. doi:10.1098/rstb.2019.0765. PMID 33550952.` and `Durant F, Bischof J, Fields C, Morokuma J, LaPalme J, Hoi A & Levin M (2019). The Role of Early Bioelectric Signals in the Regeneration of Planarian Anterior/Posterior Polarity. Biophys J 116(5):948–961. doi:10.1016/j.bpj.2019.01.029. PMID 30799071.`

### 4.2 `AOP_LifeDef_CS_RivalMatrix_v1.1.md`

20 citations. **20 exist. 0 fabricated, 0 conflated, 0 constructed DOIs.** No field the document asserts is wrong. Every correction is an **addition** — the document has **no reference list**, and 12 author strings carrying verdict weight are untraceable without external search (Zeleny & Hufford 1992, Varela/Maturana/Uribe 1974, Joyce 1994, Sharma 2023, Uthamacumaran 2024, Cleland & Chyba 2002, Ruiz-Mirazo/Peretó/Moreno 2010, Abrahão 2024, Gánti 2003, Friston 2013, Griesemer 2015, Bruineberg 2022).

**Unsourced surname strings: 5** (6 counting `Darwin` as a criterion label rather than an attribution).

| # | Surname | Location | What it carries |
|---|---|---|---|
| 1 | Luhmann | §3.3 | The R2 ◆ on D3 — one of two cases §3.3 designates arc-deciding — plus the "family precedent ▪" cells at D1/D2/D5 |
| 2 | Leduc | §3.4 | The entire R2 published-false-positive finding; reached only through Zeleny & Hufford |
| 3 | **von Neumann** | §4 | **Most serious.** The "solid-state/von Neumann ruling, graded ~ from a search snippet" underwrites C7 and C8's R3 cells, which are **▪-marked as authors' rulings** — two cells claim citation status while resting on an unretrieved snippet and an uncited surname |
| 4 | Pearl | §4 | Explicitly disclaimed as not relied on |
| 5 | Bedau | §4 | Surname + bare title, no year/venue/publisher; explicitly disclaimed |

**Three internal-consistency defects found in passing** (reported, not repaired):

1. **§5 says "28 of 160 rival cells are citations; 132 are extensions." Direct count of the ▪ marks in the §2 table gives 30** (R1 3 · R2 7 · R3 4 · R4 7 · R5 9), exactly as §2 states. Correct §5 to **30 / 130**. This is precisely the defect v1.1's own version note claims to have corrected — fixed in §2, left standing in §5.
2. The footer reads `End of AOP_LifeDef_CS_RivalMatrix_v1.0.md` in a document headed v1.1.
3. §3.4's "(p. 154)" is **unresolved** — two extraction passes over the Zeleny & Hufford PDF disagreed (153 vs 154); the pass reading running headers supports 154. The quotation itself is verbatim. Flagged, not called an error.

### 4.3 `AOP_LifeDef_CS_Amendments_v1.0.md`

**Zero external citations. Zero surname strings.** But three argumentative claims rest on unnamed literature:

- "Across eighteen systems in six literatures, no primary exhibits a comparator" — §4, the **entire basis of Amendment D** and its [FRONTIER] grade. Not one of the eighteen systems or six literatures is named. **Amendment D's evidence base is unauditable as written.** The §7 self-criticism ("asserted from an absence of evidence") is honest but does not repair the unauditability.
- "KaiABC and the planarian bioelectric prepattern are both of this kind, in two independent literatures" — §4, two empirical claims, zero citations.
- "The new clause is **autopoiesis** (R2), imported… a fifty-year-old rival" — §2, §7, the stated *cost* of the only amendment clearing the pre-registration bar; no citation.

**Dependency defect:** the header declares a dependency on `AOP_LifeDef_CS_RivalMatrix_v1.0.md` — the version v1.1 explicitly orders pruned. Repoint to v1.1.

### 4.4 `AOP_LifeDef_CS_VerdictMatrix_v1.0_Corrigendum1.md`

**Zero citations, zero surname strings, no corrections.** The arithmetic it asserts re-parses correctly: 9+4+19+2+1 = 35; c1 12 + c2 2 + c3 5 + c4 0 + c5 12 + c6 4 = 35; c1+c5 = 24; 24/35 = 68.6% ≈ 69%; the 19-case NEITHER list contains 19 entries. Its own stated lesson — that a pass checking only whether a distribution sums to the row count will miss this class of error — is correct, and is the same lesson §3.1 of this report re-learns on a byte offset.

### 4.5 `AOP_LifeDef_OAI_Attack_v1.0.md`

18 external citations. **0 fabricated, 0 conflated, 0 constructed DOIs.** Notably clean.

**Unsourced surname strings: 1.** §9's "**NASA's** working definition is a broad operational heuristic" — an argumentative claim about NASA's *definition of life*, with no citation anywhere. The document's only NASA/JPL citations are a software-engineering safe-mode page and flight-system design principles; neither is a definition of life. This is the same defect class already logged for the order's own R1 (Cleland & Chyba never use the phrase "NASA working definition").

**Corrections:**

- **The JPL URL is dead** — 302 to a generic acquisition landing page; the document is not served. It is tagged ✓ in the deliverable. **Downgrade to ⚠ or supply a live locator (JPL Rules DocID).**
- The ECB page is now titled "Two per cent inflation target"; the cited title is stale. The substantive 2% claim holds.
- `Rosen R (1958). A relational theory of biological systems. Bull Math Biophys 20(3):245–260. doi:10.1007/BF02478302.` — add issue and DOI, both of which exist.
- Gánti 2003: add the Griesemer and Szathmáry commentary to the entry. ⚠ The attached `chemoton.com` URL could not be verified and its filename indicates a **Hungarian-language collection**, not the English OUP 2003 edition cited. Verify or drop the URL.
- Cleland & Chyba 2002 is in the reference ledger but cited nowhere in the body — cite it or remove it.
- Verified sound and exact: Varela/Maturana/Uribe 1974, Ashby 1960, Conant & Ashby 1970, Pattee 2001, Yi 2000, Batchelor & Goulian 2003, Bich et al. 2016, Bechtel & Bich 2021, Kauffman 2003, Friston 2013, Sharma et al. 2023. The NASA SWEHB safe-mode passage is confirmed verbatim ("…the spacecraft is commandable… The safe state shall be power-positive.").

### 4.6 `AOP_LifeDef_CS_RetrievalLedger_v1.0.md`

**0 fabricated, 0 conflated, 0 constructed DOIs.** But this is the document whose job is sourcing hygiene, and it is the worst offender on its own standard.

**Unsourced surname strings: 13 strict, 17 including degraded forms.** Its own header warns that five were caught in this project's Gate 1 deliverables and "the base rate is not zero." It carries nearly three times that.

Strict (no title, no venue, no resolvable identifier anywhere): Clausznitzer et al. · Rust 2007 · Rust 2011 · Ouyang 1998 · Kiyohara 2005 · Lambert 2016 · Puszynska & O'Shea 2017 · Friston 2013 "(PMC)" · Scott 2014 · Bollenbach et al. (no year) · Joyce 1994 foreword · Gánti 1987 OMIKK (publisher + pages, **no title**) · Bedau "What is Life?" (title only).

Degraded: Griesemer 2015 (DOI only, no title/volume/pages) · Manicka & Levin (PMID only) · **"the mTORC1 primary" — no author string at all, yet carrying a load-bearing negative claim** · "arXiv:1606.03620" (identifier only).

**Tag audit — the ledger's own ✓/~/⚠ marks, spot-checked on nine entries:**

| Entry | Ledger tag | Finding |
|---|---|---|
| **Varela, Maturana & Uribe 1974** | ⚠ — "seven routes exhausted" | **MIS-TAGGED, and this is the consequential one.** A complete scanned PDF is freely downloadable without login from the Internet Archive (`archive.org/details/autopoiesis-f.-g-varela-r.-uribe`, uploaded Sept 2024). The Internet Archive was not among the seven routes tried. **The six-rule material was taken secondhand for no reason.** |
| **Gánti, *The Principles of Life*** | ⚠ — "no OA copy in any index" | **Refuted as stated.** A PDF of the Griesemer/Szathmáry OUP 2003 edition is openly hosted. Hosting verified; contents **not** — it appears to be an image-only scan and could not be machine-read. |
| **Bruineberg et al. 2022** | ~ abstract only | Openly available in author-hosted and PhilPapers/Semantic Scholar copies. Low stakes — correctly recorded as not relied on. Add authors 2–4 and article number **e183**. |
| **Francis & Wonham 1976** | ⚠ "already-failed" | Fields fully confirmed (*Automatica* 12(5):457–465, doi:10.1016/0005-1098(76)90006-6); open copies exist. The ⚠ appears **stale rather than false** — not re-attempted. |
| **Zeleny & Hufford 1992** | ✓ full text read | **Could not corroborate.** Taylor & Francis returns 403. IJGS 21(2) does contain an autopoiesis paper, but authorship and the 145–160 range are unconfirmed from here. This seat cannot show it was *not* retrieved — but it is the ledger's **only** route to the Varela six rules, and given that Varela itself was reachable all along, this ✓ warrants re-verification. |
| Sparta 2023 · Marshall 2021 · Hazen 20230632 · Walker 20240367 · Kurata 2006 · Abrahão 2024 · Uthamacumaran 2024 | ✓ | **Sound** — genuinely open and correctly cited. |

**The ledger's own self-reported defects all held on retest:** Hutchison "no PMC record exists" (not refuted); the Abrahão locator correction to e0000014; Manicka & Levin as a real 2019 Phil Trans B Levin paper.

**p53 and mTORC1 — the two loci that "dissolved on contact with their primaries":**

- **The string "p53" appears ZERO times in the ledger** (machine-checked on the retrieved text), as do "double-strand", "DSB", and "damage threshold". The p53 source is present only as the opaque string "Ma et al. *PNAS* 102:14266–14271 (2005)" with no title. It is real and correct in every field: `Ma L, Wagner J, Rice JJ, Hu W, Levine AJ & Stolovitzky GA (2005). A plausible model for the digital response of p53 to DNA damage. PNAS 102(40):14266–14271. doi:10.1073/pnas.0501352102. PMID 16186499.` **The downstream claim — that the "damage threshold" of five double-strand-break complexes is a modeller's chosen constant rather than a variable of the cell — is ⚠ NOT ESTABLISHED here.** BioModels holds the model with DSB/ATM quantities as parameters, which is consistent, but the primary text could not be retrieved to confirm the number five or its status. **Record it as unverified, not verified.**
- **mTORC1 is named nowhere in the ledger** — §5 says only "the mTORC1 primary." By elimination it is `Sparta B, Kosaisawe N, Pargett M, Patankar M, DeCuzzi N & Albeck JG (2023). Continuous sensing of nutrients and growth factors by the mTORC1-TFEB axis. eLife 12:e74903.`, confirmed real and correct. **Both halves of the downstream claim are CONFIRMED**: no occurrence of "setpoint" or "set point", and the sentence is present verbatim in the Introduction — "However, current measurements of this controller's function are insufficient to establish a viable quantitative model." ⚠ **One caveat stated plainly:** raw fetching is blocked at this session's gateway, so the term-absence check was a full-text read, **not a byte-level grep**. The finding is strong but is not the same class of evidence as the ledger's "machine-checked."

### 4.7 Counts

| Metric | Count |
|---|---|
| Distinct citations inventoried across the five deliverables | ~100 |
| Citations independently resolved and field-checked | **~75** |
| **Fabricated / non-existent** | **0** |
| **Conflated-pair failures** | **0** (the one known instance — the phantom Durant Phil Trans B — is in the *work order*, not in a deliverable, and CS caught it) |
| **Pattern-constructed DOIs** | **0** |
| Carrying a field-level correction | **~20** |
| Dead URLs | **1** (JPL) |
| **Unsourced surname strings** | **14 strict · 18 including degraded forms** — RivalMatrix 5(6) · OAI Attack 1 · RetrievalLedger 13(17) · Amendments 0 · Corrigendum 0 |
| Unsourced literature claims carrying no surname | **3** (all Amendments §4/§2) |
| Ledger tag mis-marks confirmed | **3** (Varela ⚠, Gánti ⚠, Bruineberg ~) + 1 stale ⚠ + 1 uncorroborated ✓ |
| Internal-consistency defects | **3** (RivalMatrix §5 count, RivalMatrix footer version, Amendments stale dependency) |

---

## 5. CW-1.4 — Chart build

**Blocked.** `AOP_TwoAxis_CS_Matrix_v1.0.md` does not exist on Drive; a title search for `AOP_TwoAxis` returns nothing. Gate 1 has not been passed. **This seat will not synthesise verdicts to populate a chart** — the order restricts CW-1.4 to CS-1.1 content only, with no additions and no re-verdicts, and there is no content. The build runs on demand once the matrix is deposited.

---

## 6. Scope extensions taken, and why

The order endorses extending scope where an error would otherwise propagate into both blinded seats. Three were taken:

1. **§2.3, the duplicate-title hazard.** Left alone, a seat running the anti-gaming check against the wrong twin would report a passing stamp as failed. Costless to report now.
2. **§3.1, correcting this seat's own prior offsets.** The published numbers pass a size check and produce a corrupt canon. This had to be corrected before anyone acted on v0.1.
3. **§4.6, auditing the ledger's tags rather than only its citations.** A wrong ⚠ sends the next seat down a secondhand route for material that was reachable directly, which is what happened to Varela.

None of these contains an interpretation of any case, a grade, or a verdict.

---

## 7. What this seat did not do

- **Did not place v1.27 on Drive** — could not, per §3.2, and did not create a truncated file in order to report having tried.
- Did not repair the unbumped v1.27 masthead. Reported only; it needs its own change record.
- Did not repair any defect in any CS or OAI deliverable. Every correction above is reported for prime, not applied.
- Did not choose between the two candidate referents for the phantom Durant citation.
- **Did not produce a per-document unsourced-surname count for `AOP_LifeDef_CS_CellProblem_v1.0.md`** — that document was scanned for citation accuracy and quotation fidelity, which the order made the priority, not for surname sourcing. The count above excludes it and is therefore a **floor, not a total**.
- Did not reach: Ma et al. 2005 full text (and therefore the five-DSB-complex claim); Zeleny & Hufford 1992 authorship and page range; Gánti 1987 pp. 68–69 and Gánti 2003 contents; Friston 2019 arXiv pp. 50 and 83 (both underwriting ▪-marked cells — the highest-priority remaining gap in the rival matrix); Bosdriesz Fig. S1; Rust 2011 supplementary; the Batchelor & Goulian typeset PDF needed to fix the sign in D2; and fifteen ledger entries not individually resolved from rate-limit exhaustion rather than any sign of defect (El-Samad 2005, Shinar 2007, Bosdriesz 2015, Durant 2017, Durant 2019, Pezzulo 2021, Breuer 2019, Thornburg 2022 — all of which were, however, resolved independently in §4.1 — plus Ruiz-Mirazo 2010, Friston arXiv:1906.10184, Kempes arXiv:2406.12176, arXiv:1606.03620, Scott 2010, Shinar & Feinberg 2010, Shimizu/Tu/Berg 2010).
- Did not grade any claim, rule on any case, or interpret any finding.

---

*End of `AOP_TwoAxis_CW_VerificationReport_v1.0.md`. Run by the Cowork seat, 4 August 2026. Nothing in this report grades its own homework: every hash is reproducible by any seat that re-runs it against the stated targets, and every citation correction is checkable against the resolver record named beside it. The §3.1 correction is a defect in this seat's own prior work, found by re-running the repair rather than by re-reading the report.*

**DEPOSIT HASH STAMP — pre-stamp body**

Reproduce by deleting everything from the blank line immediately preceding this stamp's heading through end of file — i.e. the file truncated to the final `*` of the closing italic paragraph plus its trailing newline — then hashing the remainder. (The CS verdict matrix's §8 instruction omits the preceding rule and blank line and therefore does not reproduce its own stamp; this wording is written to avoid that.)

| Quantity | Value |
|---|---|
| Bytes | 39,287 |
| md5 | `623033f9834a6e9ec59cb35679ecebb7` |
| sha256 | `a97f7a073bcdf5dae3858c7f764670100fb82a3b24506db7d82a6d1949755bce` |
| Lines by `str.split("\n")` | 304 |
