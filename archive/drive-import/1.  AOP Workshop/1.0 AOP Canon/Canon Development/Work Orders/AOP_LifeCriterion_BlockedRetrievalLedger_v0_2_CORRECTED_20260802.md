# Gate 1 — Blocked-retrieval ledger

**Seat:** Claude Science (builder). **Date:** 2 August 2026.
**Order:** `TASK_CS_AOP_LifeCriterion_SystemSelection_20260801.md` §5.4.
**Parent freeze:** `AOP_LifeCriterion_DispositionRule_FROZEN_v1_0_20260801.md`, md5 `b7eebcfd5a371a78b33a5fe230d52554` (verified by independent download this session).

Every source below was sought and not obtained. **No secondary has been substituted for any of them**
and no claim in the selection report is graded `[primary-verified]` on the strength of an unread source.
Where a substitution was made it is declared in the row rather than hidden.

No mirrors, archive sites, or proxy services were attempted for any paywalled item, and no user-agent
was spoofed. A paywall is recorded as a stop, not routed around.


**Scope of this ledger.** It covers the two retrieval tracks that returned (Chemotaxis; Set-point
theory) plus the parent seat's own retrievals. **Three tracks — Circadian, Synthetic, Two-component —
are parked on user-approval gates and have not filed their ledgers.** Their blocks are therefore
NOT represented below, and this ledger is incomplete until they land.

**Total blocked (tracks returned so far): 16**

### Alon U, Surette MG, Barkai N, Leibler S. Robustness in bacterial chemotaxis. Nature 397(6715):168-171, 14 January 1999. PMID 9923680.

- **DOI:** `10.1038/16483`
- **Track:** Chemotaxis
- **Routes attempted:** fetch_article_fulltext, which tried five routes in sequence: Unpaywall (HTTP 200, no OA location), Semantic Scholar (no openAccessPdf), PMC (no PMCID exists), Crossref TDM (no accessible content returned), and DOI resolution (landing page reachable, full text requires HTML scraping — not attempted). Independently enumerated OpenAlex locations via the api_key: three locations, all is_oa false (Nature, PubMed, and a RePEc submittedVersion pointer that resolves back to the same paywalled nature.com page). PubMed metadata and abstract retrieved successfully. No mirror, archive, proxy, or user-agent workaround attempted — out of policy.
- **Why it mattered:** The single most consequential gap in this track. The body holds the actual magnitude of the CheR/CheB expression sweep, the numerical spread of steady-state behaviour under that sweep, and the adaptation-time range — i.e. the direct quantitative evidence for both the SIZE of the S.3 set-point shift and the S.4 two-orders-of-magnitude question. The precision-versus-level distinction on which my S.3 PASS turns is taken from the abstract only, so it is sound as a qualitative distinction but carries no verified magnitudes. Related discipline note: I deliberately did NOT import the commonly recited '50-fold CheR overexpression' figure — the only 50-fold in any primary I read is Yi et al.'s report of ~50-fold variation in methylation rate from site to site on Tar, a different quantity. If a 50-fold CheR figure appears downstream it needs its own source.

### Barkai N, Leibler S. Robustness in simple biochemical networks. Nature 387(6636):913-917, 26 June 1997. PMID 9202124.

- **DOI:** `10.1038/43199`
- **Track:** Chemotaxis
- **Routes attempted:** fetch_article_fulltext: Unpaywall (200, no OA location), Semantic Scholar (SafeFetch redirect loop >5 starting at nature.com/articles/43199.pdf), PMC (no PMCID), Crossref TDM (none), DOI resolve (landing page only). OpenAlex: two locations, both is_oa false. Abstract retrieved. No mirror or proxy attempted.
- **Why it mattered:** The original two-state model whose robustness property the whole line rests on. Largely mitigated: Yi et al. 2000 restate, rearrange, and analyze the Barkai-Leibler equations in full, and I read that analysis in the primary, so the model STRUCTURE is primary-verified via Yi et al. rather than from Barkai-Leibler directly. What remains unread are BL's own parameter values and simulation details. I have flagged in the artifact that the derivation chain runs through Yi et al., not through BL itself.

### Kollmann M, Lovdok L, Bartholome K, Timmer J, Sourjik V. Design principles of a bacterial signalling network. Nature 438(7067):504-507, 24 November 2005. PMID 16306993.

- **DOI:** `10.1038/nature04228`
- **Track:** Chemotaxis
- **Routes attempted:** fetch_article_fulltext: all five routes failed (Unpaywall no OA location; Semantic Scholar no openAccessPdf; PMC no PMCID; Crossref TDM none; DOI resolve landing page only). OpenAlex: four locations, all is_oa false. Abstract retrieved. No mirror or proxy attempted.
- **Why it mattered:** Would have supplied the topology-comparison and expression-noise robustness analysis the brief named as a useful additional primary. Partially mitigated by Lovdok et al. 2009 (PLoS Biol, same group, open, retrieved and read in full), which restates the topology and robustness argument. Kollmann-specific claims are therefore downgraded to secondary and are not load-bearing in any verdict above.

### Sourjik V, Berg HC. Binding of the Escherichia coli response regulator CheY to its target measured in vivo by fluorescence resonance energy transfer. PNAS 99(20):12669-12674, 2002. PMCID PMC130518, PMID 12232047.

- **DOI:** `10.1073/pnas.192463199`
- **Track:** Chemotaxis
- **Routes attempted:** PMC full-text call via the pubmed connector returned metadata and abstract only — no body deposited in PMC for this record. fetch_article_fulltext also returned the abstract-only PMC text (Unpaywall no OA location; Semantic Scholar route rejected for serving an http-only URL under an https-only fetch policy). No mirror or proxy attempted.
- **Why it mattered:** Source of the fast-timescale rate constants (~2 s^-1 for CheY-P/FliM decay after attractant, ~20 s^-1 for the rise after repellent) that form the denominator of the S.4 slow/fast ratio. The values are stated in the abstract with units so they are reliable as numbers, but I did not see the traces or the model fit behind them, so they are tagged primary-abstract-only and the derived ratio is flagged in the artifact as a cross-paper derivation rather than a published quantity.

### Meir Y, Jakovljevic V, Oleksiuk O, Sourjik V, Wingreen NS. Precision and kinetics of adaptation in bacterial chemotaxis. Biophysical Journal 99(9):2766-2774, 3 November 2010. PMCID PMC2965943, PMID 21044573.

- **DOI:** `10.1016/j.bpj.2010.08.051`
- **Track:** Chemotaxis
- **Routes attempted:** fetch_article_fulltext in auto mode returned a PMC text file containing front matter and abstract only (~2.4 kB). Re-requested in xml mode: the PMC XML carries an explicit publisher notice that full text may not be downloaded in XML form. Semantic Scholar route failed because the offered PDF URL was http-only and rejected by the https-only fetch policy. No mirror or proxy attempted.
- **Why it mattered:** Would have given an independent quantification of adaptation precision and, more usefully for S.4, of cell-to-cell variation in adaptation RATE — the closest thing in the literature to a documented spread of the slow timescale. Its central claim (precision loss arises from methylation slowing as modification sites become scarce) is recorded as primary-abstract-only and is not relied on in any verdict.

### Wirtshafter D, Davis JD. Set points, settling points, and the control of body weight. Physiology & Behavior 1977 Jul. PMID 11803695.

- **DOI:** `10.1016/0031-9384(77)90162-7`
- **Track:** Set-point theory
- **Routes attempted:** fetch_article_fulltext: Unpaywall (200, no OA location); Semantic Scholar (200, no openAccessPdf); PMC (200, no PMCID); CrossRef TDM (no accessible content); DOI resolve (200, landing page only, HTML scraping required). No mirrors, archives or proxies attempted. Metadata (authors, title, journal, year, DOI) verified against PubMed independently of content.
- **Why it mattered:** The founding statement of the settling-point account and AOP's most direct historical citation. The abstract alone establishes the claim — a feedback model with 'no set point' reproducing the lesion and defence data, making a neural set point 'unnecessary and unparsimonious' — but the argument itself is unread. Status for content: [primary-abstract-only].

### Romanovsky AA. Thermoregulation: some concepts have changed. Functional architecture of the thermoregulatory system. Am J Physiol Regul Integr Comp Physiol 2006. PMID 17008453.

- **DOI:** `10.1152/ajpregu.00668.2006`
- **Track:** Set-point theory
- **Routes attempted:** fetch_article_fulltext: Unpaywall (200, no OA location); Semantic Scholar (200, no openAccessPdf); PMC (200, no PMCID); CrossRef TDM (no TDM links); DOI resolve HTTP 403. Also searched PubMed for an open-access restatement by the same author (Temperature journal, Handbook of Clinical Neurology 2018) — the 2018 chapter is likewise not open.
- **Why it mattered:** The primary rejection of a unified thermoregulatory set point and the source of the 'balance point' proposal. Directly decides whether candidate #3 has a stored reference at all. The abstract carries the core claims verbatim ('No computation of an integrated Tb or its comparison with an obvious or hidden set point of a unified system is necessary') but the supporting analysis is unread. Status: [primary-abstract-only].

### Romanovsky AA. Do fever and anapyrexia exist? Analysis of set point-based definitions. Am J Physiol Regul Integr Comp Physiol 2004. PMID 15191900.

- **DOI:** `10.1152/ajpregu.00068.2004`
- **Track:** Set-point theory
- **Routes attempted:** Same five routes as above; DOI resolve HTTP 403.
- **Why it mattered:** HIGHEST-PRIORITY UNREAD SOURCE ON THIS TRACK. It contains the closest published analogue to an operational discriminator: two tests applied to set-point-based definitions — thermoeffector threshold-shift compatibility, and the Tb-versus-ambient-temperature dependence test. Per the abstract, applied to fever it returns a mixed verdict: threshold changes compatible with a set-point increase in 'some (but not all) cases', febrile Tb 'defended in some (but not all) cases'. Before AOP claims novelty for its separability test, someone must read this in full. Status: [primary-abstract-only].

### Cabanac M. Adjustable set point: to honor Harold T. Hammel. J Appl Physiol 2006 Apr. PMID 16540712.

- **DOI:** `10.1152/japplphysiol.01021.2005`
- **Track:** Set-point theory
- **Routes attempted:** Same five routes; DOI resolve HTTP 403. Also attempted the companion Boulant paper on Hammel's model (PMID 16540713) — no valid DOI resolved via CrossRef.
- **Why it mattered:** The defence of the stored reference against Romanovsky. Its abstract already states AOP's own dichotomy almost verbatim — the set point 'may be determined by an external signal to which the regulated variable is compared or may be determined by the structural characteristics of the system itself' — so the full argument may contain a discriminator. Status: [primary-abstract-only].

### Fernández-Verdejo R, Ravussin E, Galgani JE, et al. Body weight regulation models in humans: insights for testing their validity. Nature Reviews Endocrinology 2025 Jul 24. PMID 40707700.

- **DOI:** `10.1038/s41574-025-01149-1`
- **Track:** Set-point theory
- **Routes attempted:** fetch_article_fulltext: Unpaywall (200, no OA location); Semantic Scholar (200, no openAccessPdf); PMC (200, no PMCID); CrossRef TDM (no accessible content); DOI resolve (200, landing page only).
- **Why it mattered:** Its stated purpose is exactly this track's question — how to test the validity of body-weight regulation models, closing with 'the design of proof-of-concept experiments'. If a published operational discriminator exists anywhere, it is most likely proposed here. NOTE: I did not verify the author list; only title, journal, year, DOI and abstract were retrieved. Status: [primary-abstract-only].

### Speakman JR, Hall KD. Models of body weight and fatness regulation. Phil Trans R Soc B 2023 Sep 4. PMID 37661735, PMC10475878.

- **DOI:** `10.1098/rstb.2022.0231`
- **Track:** Set-point theory
- **Routes attempted:** PMC full-text record retrieved but contains only front matter and abstract (body text not deposited); Unpaywall no OA location; Semantic Scholar no openAccessPdf.
- **Why it mattered:** The current authoritative taxonomy of the seven competing models and, in the abstract, the field's own admission that 'further experiments to test between the models are sorely required' — the 2023 evidence that the discriminator does not exist. Status: [primary-abstract-only].

### Lazarus M, Yoshida K, Coppari R, Bass CE, Mochizuki T, Lowell BB, et al. EP3 prostaglandin receptors in the median preoptic nucleus are critical for fever responses. Nature Neuroscience 2007. PMID 17676060.

- **DOI:** `10.1038/nn1949`
- **Track:** Set-point theory
- **Routes attempted:** Unpaywall (200, no OA location); Semantic Scholar (returned text/html, not a PDF); PMC (200, no PMCID); CrossRef TDM (no accessible content); DOI resolve (200, landing page only).
- **Why it mattered:** The cleanest causal demonstration that MnPO EP3R is required for fever — load-bearing for any S.3 claim about fever. Status: [primary-abstract-only].

### Nakamura K et al., J Neurosci 2002 (DOI 10.1523/JNEUROSCI.22-11-04600.2002) and Nakamura Y et al., Eur J Neurosci 2005 (DOI 10.1111/j.1460-9568.2005.04515.x).

- **DOI:** `10.1523/JNEUROSCI.22-11-04600.2002`
- **Track:** Set-point theory
- **Routes attempted:** PMC get_full_text_article returned 0 characters for both; fetch_article_fulltext reached PMC text records that contain only front matter and abstract (author manuscript deposits without body text). Semantic Scholar routes failed on http-only URLs and a 500 error respectively.
- **Why it mattered:** Circuit-level detail of the pyrogenic POA-to-rRPa and POA-to-DMH pathways, needed for a proper S.1/S.3 assessment of fever interventions. Status: [primary-abstract-only].

### Zhou YN, Kusukawa N, Erickson JW, Gross CA, Yura T. J Bacteriol 1988;170(8):3640-3649 (DOI 10.1128/jb.170.8.3640-3649.1988); and Bukau B, Walker GC. J Bacteriol 1989;171(5):2337-2346 (DOI 10.1128/jb.171.5.2337-2346.1989).

- **DOI:** `10.1128/jb.170.8.3640-3649.1988`
- **Track:** Set-point theory
- **Routes attempted:** PMC get_full_text_article returned 0 characters for both PMC211339 and PMC209906 — these are scanned legacy J Bacteriol issues with no machine-readable body text in PMC. Metadata and abstracts verified via PubMed.
- **Why it mattered:** The rpoH-null and dnaK-deletion phenotypes are the evidence that sigma32-system perturbations only degrade. The abstracts state the phenotypes explicitly ('grow only at temperatures less than or equal to 20 degrees C'), which is enough for the S.3 verdict, but the quantitative survival data are unread. Status: [primary-abstract-only].

### Sontag ED. Adaptation and regulation with signal detection implies internal model. Systems and Control Letters 2003 — PUBLISHED VERSION.

- **DOI:** `10.1016/S0167-6911(03)00136-1`
- **Track:** Set-point theory
- **Routes attempted:** Unpaywall (no OA location); Semantic Scholar (rejected http-only arXiv URL); PMC (no PMCID); CrossRef TDM (no accessible content); DOI resolve (200, landing page only). SUBSTITUTION MADE AND DECLARED: read the author's own arXiv preprint q-bio/0309003v1 instead, downloaded directly from arXiv.
- **Why it mattered:** The theorem bearing on Reading A vs Reading B. The preprint is the author's own and its comment line says 'to appear in Systems and Control Letters', so the theorem statement is reliable, but I have not verified the published version's wording or pagination.

### OpenAlex — all queries this session (citation-graph search for prior art on the discriminator).

- **Track:** Set-point theory
- **Routes attempted:** host.credentials.request('openalex') invoked in the repl kernel; host.credentials.list() confirms a credential named 'OpenAlex' is registered, but every openalex_search_works call returned the error openalex_key_required. Waited and retried once after the credential request. Never called keyless; never sent mailto. PubMed and arXiv were used as substitutes.
- **Why it mattered:** Without OpenAlex I could not run a citation-graph sweep for statements of the stored-reference/emergent-target distinction OUTSIDE biomedicine — economics, engineering, ecology. Given this project's finding that its strongest results are ones independently discovered by three fields, that coverage gap is material: there may be a fourth or fifth independent statement of the distinction, or even a published operational discriminator, that this track did not see. I recommend a follow-up sweep once the OpenAlex key is working.

---

## Parent-seat retrievals (this seat, not a track)

Attempted directly by the parent seat while retrieval tracks were parked.

### Nakajima M, Imai K, Ito H, Nishiwaki T, Murayama Y, Iwasaki H, Oyama T, Kondo T. "Reconstitution of Circadian Oscillation of Cyanobacterial KaiC Phosphorylation in Vitro." *Science* 308(5720):414–415 (2005).

- **DOI:** `10.1126/science.1108451`
- **Routes attempted:** Unpaywall (HTTP 200, no OA location); Semantic Scholar (200, no openAccessPdf);
  PMC (200, no PMCID found); Crossref TDM (no TDM links); DOI resolution (landing page reachable, full
  text requires HTML scraping — not attempted). No mirror, archive, or proxy attempted; no user-agent spoofed.
- **Status:** `[primary-abstract-only]` — abstract retrieved and read; body not obtained.
- **Why it mattered:** THE load-bearing source for the whole arc's positive side. The in vitro
  reconstitution is the autonomy evidence: an oscillator running from three purified proteins and ATP
  with no transcription cannot be driven by the regulated coordinates, which would make KaiABC the
  only Reading-A-eligible candidate found. **A pending user approval for `science.org` may resolve this.**

### Woelfle MA, Ouyang Y, Phanvijhitsiri K, Johnson CH. "The adaptive value of circadian clocks: an experimental assessment in cyanobacteria." *Curr Biol* 14(16):1481–1486 (2004).

- **DOI:** `10.1016/j.cub.2004.08.023`
- **Routes attempted:** Unpaywall (200, no valid OA PDF despite bronze status); Semantic Scholar
  (rejected — offered an http-only URL under an https-only fetch policy); PMC (no PMCID); Crossref TDM
  (no accessible content); DOI resolution (landing page only). No mirror/archive/proxy attempted.
- **Status:** `[not-retrieved]` — not even the abstract was obtained through these routes.
- **Why it mattered:** The competition-assay fitness observable, which would be the only STRONG S.5
  attaching to a *positive* article. **A pending user approval for `cell.com` may resolve this.**

### Shinar G, Milo R, Martínez MR, Alon U. "Input–output robustness in simple bacterial signaling systems." *PNAS* 104(50):19931–19935 (2007).

- **DOI:** `10.1073/pnas.0706792104`
- **Routes attempted:** Unpaywall (200, no OA location); Semantic Scholar (returned text/html, not a
  PDF); PMC (200 — **record retrieved but contains front matter and abstract only**; body not deposited).
- **Status:** `[primary-abstract-only]`. **Explicitly recorded because the PMC call "succeeded":** a
  200 with a populated record is not full text, and treating it as such is precisely the failure mode
  this ledger exists to prevent.
- **Why it mattered:** Independent structural confirmation (via absolute concentration robustness)
  that the EnvZ/OmpR output set-point is fixed by rate constants. The claim currently rests on
  Batchelor & Goulian alone, which this seat did read in full.

### Dynamic correction in EnvZ/OmpR — a gap, not a paywall

- **Status:** `[not-retrieved]` — no primary establishing **restoration after a perturbation** (as
  distinct from robustness of the steady state across conditions) has been retrieved.
- **Routes attempted:** full-text search of Batchelor & Goulian 2003 for time-course, relaxation,
  transient, recovery, and post-shift language — zero hits; that paper is a steady-state analysis with
  steady-state reporter measurements.
- **Why it matters:** the order requires a negative control that **demonstrably corrects**. This gap is
  a live requirement on the leading negative control, and it is a search gap rather than a paywall —
  it may well close with more retrieval, and it should be closed before the pair is fixed.

---

## Two notes on ledger discipline

**1. A successful HTTP call is not a retrieval.** Three entries in this ledger (Shinar 2007; and in the
track ledgers, Speakman & Hall 2023 and the Nakamura papers) returned HTTP 200 with a populated PMC
record containing only front matter and an abstract. Any of these could have been logged as retrieved
by a seat checking status codes rather than reading the body.

**2. One substitution was made and is declared rather than hidden.** Sontag's internal-model theorem
was read in the author's own arXiv preprint (`q-bio/0309003v1`) because the published version
(*Systems and Control Letters*, 2003) is paywalled. The preprint's comment line states it is to appear
in that journal, so the theorem statement is reliable, but **the published wording, scope conditions,
and pagination are unverified.** Any AOP text relying on this theorem must cite it at that standing
until the published version is read. Per order §5.4, no secondary was substituted anywhere else.

**3. Two author attributions were fabricated in the v0.1 drafts and are corrected here.** A review
pass found that this seat had named first authors for two papers whose author lists no retrieval in
this session had returned — "Bhatt et al." for the Nat Commun 2022 engineered-EnvZ paper, and
"Bosy-Westphal A et al." for the 2025 *Nat Rev Endocrinol* review. Both were subsequently retrieved
from PubMed and corrected to the actual lists (**Jones RD, Qian Y, Ilia K, Wang B, et al.** and
**Fernández-Verdejo R, Ravussin E, Galgani JE, et al.** respectively). The correction is recorded
rather than made silently: an invented attribution is the same class of defect — a claim asserted
past what retrieval returned — that this ledger and the retrieval-tag convention exist to prevent,
and it occurred in documents whose own text warns against it. **Bibliographic metadata must be
retrieved, not recalled**, and a paper read in full is not thereby a paper whose byline was read.
