# Gate 1 — Blocked-retrieval ledger

*(v1_0, 3 August 2026 — supersedes the v0_1/v0_2 interim ledger; all five tracks have now reported.)*

**Seat:** Claude Science (builder). **Date:** 2 August 2026.
**Order:** `TASK_CS_AOP_LifeCriterion_SystemSelection_20260801.md` §5.4.
**Parent freeze:** `AOP_LifeCriterion_DispositionRule_FROZEN_v1_0_20260801.md`, md5 `b7eebcfd5a371a78b33a5fe230d52554` (verified by independent download this session).

Every source below was sought and not obtained. **No secondary has been substituted for any of them**
and no claim in the selection report is graded `[primary-verified]` on the strength of an unread source.
Where a substitution was made it is declared in the row rather than hidden.

No mirrors, archive sites, or proxy services were attempted for any paywalled item, and no user-agent
was spoofed. A paywall is recorded as a stop, not routed around.

**Total blocked across all five retrieval tracks: 30**

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

### Nakajima M, Imai K, Ito H, Nishiwaki T, Murayama Y, Iwasaki H, Oyama T, Kondo T. Reconstitution of circadian oscillation of cyanobacterial KaiC phosphorylation in vitro. Science 308:414-415 (2005). PMID 15831759.

- **DOI:** `10.1126/science.1108451`
- **Track:** Circadian
- **Routes attempted:** fetch_article_fulltext: Unpaywall returned 200 with no OA location; Semantic Scholar 200 with no openAccessPdf; PMC 200 with no PMCID; CrossRef TDM had no TDM links; DOI resolution reached a landing page requiring HTML scraping. PubMed PMID-to-PMCID conversion returned no PMCID. OpenAlex (with api_key) reported oa_status 'closed' and zero OA locations. I then called request_network_access for www.science.org, WAS GRANTED it, and received HTTP 403 Forbidden on both /doi/10.1126/science.1108451 and /doi/abs/10.1126/science.1108451. No mirror, archive, proxy or user-agent spoofing attempted.
- **Why it mattered:** This is THE autonomy primary and the entire longlist rationale for this track being the only strict-Reading-A candidate. Held at [primary-abstract-only]: what the abstract establishes is reconstitution 'by incubating KaiC with KaiA, KaiB, and adenosine triphosphate', that period 'was stable despite temperature change (temperature compensation)', and that in vivo KaiC-mutant periods matched in vitro. I took no numerical period or Q10 value from it. Its reconstitution claim is independently corroborated by Rust 2007, Ito-Miwa 2020 and Teng 2013 (all primary-verified), but those are [secondary] for Nakajima's own content and none of them reports Nakajima's measurements.

### Woelfle MA, Ouyang Y, Phanvijhitsiri K, Johnson CH. The adaptive value of circadian clocks: an experimental assessment in cyanobacteria. Curr Biol 14:1481-1486 (2004). PMID 15324665.

- **DOI:** `10.1016/j.cub.2004.08.023`
- **Track:** Circadian
- **Routes attempted:** fetch_article_fulltext: Unpaywall 200 with no valid OA PDF; Semantic Scholar rejected an http-only URL; PMC 200 with no PMCID; CrossRef TDM returned nothing accessible; DOI landing page needed scraping. OpenAlex (with api_key) reported oa_status 'bronze' with a PDF at cell.com. I called request_network_access for www.cell.com, WAS GRANTED it, and received HTTP 403 Forbidden on the article PDF path. No mirror, archive, proxy or user-agent spoofing attempted.
- **Why it mattered:** This is the arrhythmic-versus-wild-type comparison class — one of the two structural pillars the S.5 assessment rests on, and the paper that reports the advantage disappearing in constant environments (directly relevant to the section 8 environmental-model objection). Held at [primary-abstract-only]. Its design and numbers are reported in Ma, Woelfle & Johnson 2013, which I read in full and tag [secondary]. The S.5 STRONG score does not depend on Woelfle alone — Ouyang 1998, Lambert 2016, Diamond 2017 and Puszynska 2017 are all primary-verified — but Woelfle's own figures are unverified.

### Kondo T, Tsinoremas NF, Golden SS, Johnson CH, Kutsuna S, Ishiura M. Circadian clock mutants of cyanobacteria. Science 266:1233-1236 (1994). PMID 7973706.

- **DOI:** `10.1126/science.7973706`
- **Track:** Circadian
- **Routes attempted:** PubMed PMID-to-PMCID conversion returned no PMCID. Full-text fetch not further pursued after the same publisher (science.org) returned HTTP 403 on a granted domain for the 2005 Science article above, which established the publisher block. Metadata verified independently via CrossRef.
- **Why it mattered:** The classic in vivo period range for S.4 — '12 mutants... exhibit a broad spectrum of periods (between 16 and 60 hours)' plus arrhythmics from 150,000 clones — is therefore [primary-abstract-only]. Not load-bearing: the S.4 verdict rests on Ito-Miwa 2020 (primary-verified, 15-158 h in vitro), which supersedes it in both range and rigour.

### Ishiura M, Kutsuna S, Aoki S, Iwasaki H, Andersson CR, Tanabe A, Golden SS, Johnson CH, Kondo T. Expression of a gene cluster kaiABC as a circadian feedback process in cyanobacteria. Science 281:1519-1523 (1998). PMID 9727980.

- **DOI:** `10.1126/science.281.5382.1519`
- **Track:** Circadian
- **Routes attempted:** PubMed PMID-to-PMCID conversion returned no PMCID. Same publisher block as the two Science articles above (403 on a granted science.org domain). Metadata verified independently via CrossRef.
- **Why it mattered:** Would have supplied a third phase-resetting operation ('Temporal kaiC overexpression reset the phase of the rhythms') and the original kaiABC transcriptional-feedback result. Held at [primary-abstract-only]. Not load-bearing: S.3 already passes on dark pulses (Kiyohara 2005) and in vitro ADP steps (Rust 2011), and the transcriptional-feedback y -> x path is established by Teng 2013 and Markson 2013, all primary-verified.

### Aoki SK, Lillacci G, Gupta A, Baumschlager A, Schweingruber D, Khammash M. A universal biomolecular integral feedback controller for robust perfect adaptation. Nature 570:533-537 (2019). PMID 31217585. Bibliographic metadata verified via PubMed; content is [primary-abstract-only].

- **DOI:** `10.1038/s41586-019-1321-1`
- **Track:** Synthetic
- **Routes attempted:** Eight routes, all failed. (1) fetch_article_fulltext auto: Unpaywall returned no valid PDF, Semantic Scholar no openAccessPdf, PMC no PMCID, Crossref TDM no accessible content, DOI resolve reached the landing page only. (2) fetch_article_fulltext with prefer_format=pdf_url: same five routes, no PDF URL. (3) PubMed convert_article_ids: no PMCID exists, so no PMC route. (4) OpenAlex works record via API key: reports oa_status green, any_repository_has_fulltext true, oa_url http://hdl.handle.net/20.500.11850/351590 - an author-deposited acceptedVersion in ETH Zurich's own institutional repository (a legitimate green-OA route, not a mirror). (5) hdl.handle.net: blocked by sandbox allowlist (403 at proxy). (6) Requested and was GRANTED network access to www.research-collection.ethz.ch; the host then returned HTTP 403 to my client on the handle URL. (7) Three documented DSpace REST endpoints on that same granted host (/server/api/discover/search/objects, /rest/handle/..., /server/api/pid/find): all 403. (8) arXiv search via the literature connector: this 2019 Nature paper has no arXiv version (the 2016 theory paper does, arXiv:1410.6064; 1911.05732 is a different paper). NOT ATTEMPTED, DELIBERATELY: no user-agent spoofing, no mirrors, no archive or proxy sites.
- **Why it mattered:** The single most consequential block on this track. It is the experimental realisation of antithetic integral feedback and the brief specifically asked whether inducer-driven set-point retuning was demonstrated in the lab, with the numbers and the range - I do not have them. It also contains the E. coli growth-rate control application, which is the best candidate answer to the fatal objection that engineered controllers hold references for arbitrary targets rather than their own viable sets. Its abstract claims tunability was demonstrated and names growth-rate control, so both points are live but unverified. It could NOT rescue target_is: PARAMETER - that is settled by the equations in Briat and Filo - but it could establish an experimental retuning range and a viability-adjacent regulated variable.

### Becskei A, Serrano L. Engineering stability in gene networks by autoregulation. Nature 405:590-593 (2000). PMID 10850721. Content is [primary-abstract-only].

- **DOI:** `10.1038/35014651`
- **Track:** Synthetic
- **Routes attempted:** fetch_article_fulltext: Unpaywall no OA location, Semantic Scholar no openAccessPdf, no PMCID, Crossref TDM no content, landing page only. OpenAlex confirms oa_status closed and any_repository_has_fulltext false (an edoc Basel submittedVersion record exists but is flagged not-OA).
- **Why it mattered:** This is the canonical primary for negative autoregulation as the negative-control architecture, and the brief requires establishing that the negative control demonstrably CORRECTS. The abstract claims they 'show the gain of stability produced by negative feedback' - a stability/variance-narrowing claim. It does NOT establish a perturb-and-recover experiment, and I did not read the figures. So whether NAR demonstrates correction after a deliberate displacement remains unestablished, which is the weakest link in this track.

### Rosenfeld N, Elowitz MB, Alon U. Negative autoregulation speeds the response times of transcription networks. J Mol Biol 323:785-793 (2002). PMID 12417193. Content is [not-retrieved].

- **DOI:** `10.1016/S0022-2836(02)00994-4`
- **Track:** Synthetic
- **Routes attempted:** fetch_article_fulltext: all five routes failed (Unpaywall no OA location, Semantic Scholar none, no PMCID, Crossref TDM none, landing page only). OpenAlex: oa_status closed. A CaltechAUTHORS submittedVersion record exists but is flagged not-OA.
- **Why it mattered:** The brief named it for NAR response-time acceleration. Response-time acceleration is in any case a transient-dynamics claim rather than a correction-after-perturbation claim, so its absence weakens but does not by itself decide the NAR-as-corrector question.

### Briat C, Gupta A, Khammash M, Cell Systems 2:15-26 (2016) - the PUBLISHED VERSION OF RECORD.

- **DOI:** `10.1016/j.cels.2016.01.004`
- **Track:** Synthetic
- **Routes attempted:** fetch_article_fulltext returned the arXiv preprint (arXiv:1410.6064) rather than the Cell Systems text; Unpaywall classifies this as bronze OA with the arXiv PDF as the OA location. I did not attempt to bypass the Cell Press paywall.
- **Why it mattered:** All my Briat quotations - the four-reaction motif, 'This value is implemented as the birth-rate of species Z1', the dZ integrator derivation, Theorem 2, Proposition 3, the theta-tuning recommendation - were read in the preprint. Section titles and Theorem/Proposition numbering matched what the published version is cited as containing, but I did not verify the published text. The mu/theta finding does NOT rest on this alone: Filo et al. 2022 is a published version of record and independently establishes it. Still, every Briat quotation must be re-checked against the version of record before it is relied on.

### The CcdB-based growth control experimental paper cited by Olsman et al. as the source of observed long-term oscillatory behavior.

- **Track:** Synthetic
- **Routes attempted:** Not pursued to primary - identified only as an in-text citation within Olsman et al.; I did not resolve the reference number to a DOI within this session's budget.
- **Why it mattered:** It is the experimental instance of a viability-relevant (toxin/growth) antithetic application, and therefore the second-best answer after Aoki to the 'arbitrary target vs. own viable set' objection. Its absence means the CcdB growth-control claim rests on a modelling section rather than an experiment.

### Xiao F et al. Stabilization of antithetic control via molecular buffering. J R Soc Interface (2022). PMC8905164. And: Hu CY. Antithetic integral feedback control redesigned for improved dynamics and lower noise. Cell Systems (2026), PMID 41856043, DOI 10.1016/j.cels.2026.101565 - [primary-abstract-only].

- **Track:** Synthetic
- **Routes attempted:** PMC full-text call for PMC8905164 returned an empty body (0 characters). For the 2026 sAIF paper I retrieved metadata and abstract via PubMed only; no OA full-text route attempted within budget.
- **Why it mattered:** The 2026 sAIF paper's abstract describes sensor-based antithetic integral feedback implemented in E. coli using split inteins, yielding effective PI behavior without a separate proportional module - a possible successor containing a same-chassis I-vs-PI contrast, which is worth a follow-up if the parent seat wants matched Pair A strengthened with a corrector-vs-corrector axis.

### Shinar G. & Feinberg M., Structural sources of robustness in biochemical reaction networks, Science 327(5971):1389-1391 (2010).

- **DOI:** `10.1126/science.1183372`
- **Track:** Two-component
- **Routes attempted:** fetch_article_fulltext: Unpaywall -> no OA location; Semantic Scholar -> no openAccessPdf; PMC -> no PMCID found; CrossRef TDM -> no TDM links; DOI resolve -> HTTP 403. No mirrors, archive sites, proxies, or user-agent spoofing attempted (prohibited).
- **Why it mattered:** The canonical structural-ACR statement and the reference the brief named. MITIGATED BUT NOT SOLVED: I read the same authors' open-access companion (Shinar & Feinberg, Math Biosci 231:39-48, 2011, PMC3086454), which restates Theorem 6.1 and works the EnvZ-OmpR network explicitly with the deficiency-one accounting. All structural claims rest on that 2011 primary, which I read and tagged. The Science 2010 paper itself remains [not-retrieved] and I make no claim about its wording.

### Hart Y., Madar D., Yuan J., Bren A., Mayo A.E., Rabinowitz J.D. & Alon U., Robust control of nitrogen assimilation by a bifunctional enzyme in E. coli, Mol Cell 41(1):117-127 (2011).

- **DOI:** `10.1016/j.molcel.2010.12.023`
- **Track:** Two-component
- **Routes attempted:** fetch_article_fulltext twice: Unpaywall -> no valid OA PDF (oa_status bronze); Semantic Scholar -> http-only URL refused by the fetcher; PMC -> no PMCID; CrossRef TDM -> nothing accessible; DOI resolve -> landing page only, would require HTML scraping. Also note: the FIRST fetch attempt returned a mismatched title ('The Ewing sarcoma protein regulates DNA damage-induced alternative splicing'), so that response was discarded rather than used.
- **Why it mattered:** The bifunctional-enzyme robustness result for the nitrogen system — the backup track's core primary. Its equations would settle whether the AT/AR avidity mechanism is also target-as-parameter. Only the abstract was read, via PubMed metadata: mechanism 'based on the avidity of a bifunctional enzyme, adenylyltransferase (AT/AR), to its multimeric substrate' [primary-abstract-only]. The NRII/NRI section of my report is abstract-only plus Straube 2014, and is labelled as such.

### Aiba H. et al. (1989, J Biol Chem) and Tokishita S. et al. (1991, J Biol Chem) — earlier pleiotropic envZ alleles with diminished phosphatase activity and elevated OmpR-P half-life.

- **Track:** Two-component
- **Routes attempted:** PubMed metadata retrieved (no PMCID, no DOI indexed for either record), so there was no identifier to route into fetch_article_fulltext. No further routes attempted.
- **Why it mattered:** These are the earliest reports of phosphatase-diminished envZ alleles and would extend the P1 mutant series backwards. I rely on them ONLY as reported by Gerken et al. 2009 — [secondary] — and I have not verified their content. Any weight prime places on the mutant series should rest on Hsing & Silhavy 1998 and Gerken et al. 2009, which I read.

### A repeat of the Batchelor-Goulian robustness titration assay performed in a set-point-shifted envZ background (or under MzrA overexpression).

- **Track:** Two-component
- **Routes attempted:** PubMed searched across ACR-mutant, envZ-allele, set-point-shift, and robustness-mutant phrasings; nothing on point returned. This is a gap in the published literature, not a retrieval failure on a known paper.
- **Why it mattered:** THIS IS THE DECISIVE MISSING EXPERIMENT. 'Regulates precisely toward the wrong target' requires showing the shifted OmpR-P level is robustly HELD (e.g. still insensitive to [EnvZ]_T/[OmpR]_T titration), not merely elevated. Without it, the P1 threat in my findings is strong but not closed. Recorded as a gap; I did not fill it from training.

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

## Five notes on ledger discipline

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


**4. One further substitution, declared.** The Briat/Gupta/Khammash antithetic-feedback theory was read
in the authors' arXiv preprint (`arXiv:1410.6064`) because the DOI resolves there and the *Cell Systems*
version of record is `[not-retrieved]`. All set-point equations quoted from it must be re-checked against
the published version before anything relies on them.

**5. Self-checks caught three further fabricated author lists.** Beyond the two corrected in note 3, a
retrieval track re-verifying its own bibliography against PubMed records found three more unsourced
surname strings in its draft and corrected them. No content claim depended on any of the five, but the
pattern is the point: **author lists are the easiest thing in a bibliography to supply from memory and
the easiest to check, and this project's documented failure mode is exactly that gap.** Every author
list in the Gate 1 deliverables has now been either retrieved from a PubMed record or read from the
paper's own citation line.
