# AOP — Audit of the five v1.4 references against primary sources

**Run:** v1.6 preparation, 3 July 2026. **Discipline:** confirm bibliographic form, then check the
specific claim-as-used against source text (not just the abstract) wherever full text is retrievable.
This closes the gap the existing `aop_reference_audit.md` left open — that file covered the original
15 plus the Gap-1 and Gap-2 additions, but not the five references added in v1.4.

| # | Reference | DOI | Retrieval | Claim as used in canon | Verdict |
|---|-----------|-----|-----------|------------------------|---------|
| 1 | Rosas, Mediano, Gastpar & Jensen 2019, *Phys. Rev. E* 100, 032305 | 10.1103/PhysRevE.100.032305 | **Full text** (unpaywall→arXiv 1902.11239) | O-information is the signed companion measure: negative for synergy-dominated, positive for redundancy-dominated structure | **SUPPORTS** — source defines Ω(Xⁿ)>0 as "interdependencies more efficiently explained as shared randomness" (redundancy) and characterises "synergy- and redundancy-dominated systems"; sign convention matches exactly |
| 2 | Comolatti & Hoel 2025, *Entropy* 27, 825 | 10.3390/e27080825 | **Full text** (PMC) | >dozen independently developed causal measures are near-rediscoveries of a small set of shared primitives, agreeing on structural conclusions (causal emergence) while differing in assigned values | **SUPPORTS** — source: "over a dozen measures … based on a small set of related 'causal primitives'"; "remarkable agreement in terms of what constitutes a strong or weak cause"; title/result: causal emergence found across measures. Direction survives, magnitude does not — as cited |
| 3 | Boyle et al. 2025, *PNAS* 122, e2406344122 | 10.1073/pnas.2406344122 | **Full text** (PMC) | Persistence selection between biogeochemical cycle variants for their distinct Earth-system effects | **SUPPORTS** — source: distinct cycle variants "compete by climatic impact phenotypes"; "embraces differential persistence"; persistence-based selection |
| 4 | Lenton et al. 2021, *Trends Ecol. Evol.* 36, 333–344 | 10.1016/j.tree.2020.12.003 | **Abstract only** (paywalled; CrossRef TDM returned coredata + abstract, no body) | Differential persistence demonstrated for self-perpetuating feedback systems from autocatalytic networks to ecosystems, belief systems, economies | **SUPPORTS (abstract)** — abstract confirms every element: "natural selection … based solely on differential persistence"; "self-perpetuating feedback cycles"; autocatalytic networks; ecosystems; "dominant belief systems, and economies." NOTE: v1.5 wrongly listed this as full-text-verified; corrected in v1.6 |
| 5 | Bouchard 2008, *Philos. Sci.* 75, 560–570 | 10.1086/594507 | **Abstract only** (closed access) | Differential persistence of lineages as a measure of ecological fitness | **SUPPORTS (abstract)** — abstract: "differential persistence of lineages can be used as a way to assess ecological fitness." Already handled honestly in v1.5 (title/DOI/abstract) |

## VIF / multicollinearity citation (the one open item)

| Reference | DOI | Retrieval | Claim as used | Verdict |
|-----------|-----|-----------|---------------|---------|
| Marquardt 1970, *Technometrics* 12, 591–612 | 10.1080/00401706.1970.10488699 | Bib confirmed (title + venue + DOI verified via retrieval attempt; closed access, no body) | The variance-inflation-factor form 1/(1−R²) for per-coefficient variance under correlated regressors | **BIB-CONFIRMED, definitional** — Marquardt 1970 is the origin of the term "variance inflation factor." The identity is standard textbook econometrics and, as the canon states, load-bearing on nothing. Handled at the same standard as Watanabe 1960: bibliographic form verified, content not claimed to have been read beyond the definitional attribution |

## Net
- **Three of five v1.4 refs verified in full text** (Rosas, Comolatti–Hoel, Boyle) — claim-as-used
  checked against source body.
- **Two confirmed by abstract only** (Lenton, Bouchard) — both paywalled; abstracts confirm the
  cited claims. The v1.5 note's "Lenton … in full text" was an overclaim, now corrected.
- **VIF citation closed** to Marquardt 1970, bib-confirmed and definitional.
- No claim in the canon depends on an unverified source. The reference apparatus has no open items.

*Source PDFs / text in `articles/`; sign-convention and primitive passages were read directly from
source body for the three full-text cases.*
