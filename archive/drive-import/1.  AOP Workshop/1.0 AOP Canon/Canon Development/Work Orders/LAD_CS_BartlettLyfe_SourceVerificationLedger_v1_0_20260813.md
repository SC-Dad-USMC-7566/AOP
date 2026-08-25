# D1 — Source and Verification Ledger: Bartlett–Wong "Lyfe" / Mindscape 106 audit

**File:** `LAD_CS_BartlettLyfe_SourceVerificationLedger_v1_0_20260813.md`
**Order:** `LAD_WorkOrder_Claude_BartlettLyfe_LadderAOP_v0_1_20260807.md` (Rowan/Codex Prime, commissioned by Ben)
**Seat:** Claude Cowork, acting as "Claude Science" (execution seat). Completion date 2026-08-13/14; all web fetches executed 2026-08-13/14 UTC.
**Method note:** literature verification was distributed across four parallel verification subagents (topic clusters) plus one follow-up-Bartlett reading subagent and one Ladder-document reading subagent, all operating under the work order's full-text, citation, and grading rules. The parent seat read the transcript, the Bartlett–Wong paper, and the AOP/Ladder governing sections directly. Verification levels below use the work order's vocabulary: **FULL TEXT** (body read), **ABSTRACT ONLY**, **METADATA ONLY**, **FULL TEXT NOT VERIFIED** (documented attempt failed). No source is reported above its access level anywhere in D2–D5.

---

## 0. Startup authority check (work order §3)

Startup check — 2026-08-13
[✓] AOP Charter — v1.2 (project instructions, read in full)
[✓] AOP Canon — **v1.27 swept stamp-ready candidate**, per Ben's ruling of 2026-08-13 (see §0.1)
[✓] Ladder Charter — v0.1 installed (v0.2 and v0.3 PROPOSED noted, not treated as authority)
[✓] Ladder Canon designation — `LAD_Canon_v1_0.md`, live 9,643-byte copy (fileId `1_FXOYEHw93fro9u24vpoKBIZRqRssmDE`); superseded 6,805-byte duplicate identified and NOT used
[✓] AOP → Ladder bridge: one-way support rule honored throughout (work order §3)
Drive connector: on.

### 0.1 The AOP master conflict, and Ben's ruling

The work order names `AOP_CANON_MASTER_v1.27.md` (fileId `1jnq…xty_`) as the current master. The startup check found a conflict, reported to Ben before any use of authority, per the work order's stop condition:

- That exact fileId is flagged in `AOP_Status_ContractV021_SessionAndCanon_20260807.md` as a **pre-sweep duplicate scheduled for trashing**.
- The real v1.27 is the C1/C3-swept stamp-ready candidate (md5 `43257601e39489f92a03cbcd64165d43`), which **awaits Ben's manual masthead stamp**; as of 2026-08-13 every v1.27-named file on Drive still carries the `version 1.26 · compiled 25 July 2026` masthead, and **the swept candidate file itself is not on Drive**.
- The `AOP_Canon_v1_0.md` designation copies findable on Drive are stale (pointing at v1.4–v1.16).

**Ben's ruling (2026-08-13, this session):** proceed using the swept stamp-ready candidate as the working master; record in every deliverable that the masthead stamp is outstanding; cite as "AOP v1.27, pending stamp."

**Reconstruction provenance (verifiable):** because the swept candidate is absent from Drive, it was reconstructed deterministically: base = `AOP_CANON_MASTER_v1.27.md` fileId `1mnX6Y8frvAkl8rpH3aP2OR27jriGVel-` downloaded and hash-verified (255,684 B, md5 `998aa87e0927f84ae6ea1676ebe8ca93` — exact match to the changeset-declared clean fold); the four count-asserted within-line edits of `AOP_ChangeNote_v1.27_C1C3_residual_sweep_20260806.md` were applied (each verified to hit exactly once); output verified at 255,714 B, md5 `43257601e39489f92a03cbcd64165d43` — **byte-exact match to the change-note record**. Any seat can re-run this check.

---

## 1. Core documents (mandatory full read)

| ID | Source | Access route | Level | What was read | Bears on |
|---|---|---|---|---|---|
| CORE-1 | `Mindscape_106_Stuart_Bartlett_What_Life_Means_Transcript.txt`, Drive `12D4RUeQ75z4eSh0FX9LDtMnejIc4AVIu` (71,324 B) | Drive read + local copy | **FULL TEXT** (parent seat; 100%, 181 transcript lines, opening through closing exchange) | entire supplied transcript | D2 throughout |
| CORE-2 | Bartlett S., Wong M.L. 2020. "Defining Lyfe in the Universe: From Three Privileged Functions to Four Pillars." *Life* 10(4):42. doi:10.3390/life10040042 | Drive PDF `1Vi5jHooO86hpWQs99TN3S0nkTKdj4FL7` (2,580,465 B, md5 `a283dec808a514fc35e6262b28c26583`), text-extracted; cross-checked against MDPI HTML/PDF by two subagents | **FULL TEXT** (parent seat; all 23 PDF pages incl. the 112-item reference list) | entire paper | D2, D3, D4, D5 |
| CORE-3 | Episode page, preposterousuniverse.com/podcast/2020/07/20/106-stuart-bartlett… | not fetched (transcript supplied; page adds no audited content) | METADATA ONLY | — | date/venue only |
| CORE-4 | Caltech repository record authors.library.caltech.edu/records/6mpbe-c6f30 | not fetched; MDPI version-of-record used instead | METADATA ONLY | — | none load-bearing |

**Transcript completeness caveat (flagged for Rowan/Codex):** the supplied transcript is ~12,200 words; a full ~1h45m Mindscape episode transcript is typically longer. Several items on the work order's audit list do not occur in the supplied transcript at all (Daisyworld by name; Keim & Nagel by name; explicit "mother tree" language; mycorrhizal fungi by name). D2 audits the supplied transcript as authoritative and marks each absent item explicitly. If a longer official transcript exists, the audit of the absent items should be re-run against it.

## 2. Governing documents

| ID | Source | Level | Notes |
|---|---|---|---|
| GOV-1 | AOP Charter v1.2 | FULL TEXT (parent seat) | project instructions |
| GOV-2 | AOP v1.27 (pending stamp), working master reconstructed as §0.1 | FULL TEXT of load-bearing sections by parent seat (§2, §3, §7, §8, §9, §9a, §11a, §11b, §13, §13a read in full; remaining sections read at structure level); full text held locally | D5 |
| GOV-3 | `AOP_LifeDef_CW_VerificationReport_v0.1.md` (project doc) | FULL TEXT (parent seat) | life-definition adjudication arc status; NASA-definition provenance flags |
| GOV-4 | `AOP_Status_ContractV021_SessionAndCanon_20260807.md`; `AOP_ChangeNote_v1.27_C1C3_residual_sweep_20260806.md`; `AOP_Handoff_InterventionContract_v0.2_20260806.md` | FULL TEXT (parent seat) | canon-stamp state; intervention-contract v0.2.1 typed-family architecture (benchmark schema for D5) |
| GOV-5 | Ladder Charter v0.1 (`1mwvipulVmoTCAF4UC7pwB21hq2qY3u9_`) | FULL TEXT (subagent; saved locally) | guardrails quoted verbatim in D4 |
| GOV-6 | `LAD_Canon_v1_0.md` live copy (`1_FXOYEHw93fro9u24vpoKBIZRqRssmDE`) + `LAD_Canon_ChangeLog.md` | FULL TEXT (subagent; saved locally) | spine, grades, committed-vs-grade |
| GOV-7 | `LAD_BeforeTheFirstRung_PrimeDraft_v0_7.md` (`1iVVNTfa9Vw4Pz9h7BesfkJJm51K2d1e_`, 63,142 B, mod. 2026-08-07) | FULL TEXT saved locally; chapters 1, 6–10, coda and version note read in full; chs. 2–5, 11–12 read at opening/excerpt level; complete vocabulary grep for all Bartlett-adjacent terms run over 100% of the text | D4 placements |
| GOV-8 | `LAD_BeforeTheFirstRung_PrimeDraft_v0_7_SourceAndGradeAudit.md` | FULL TEXT (subagent) | grading discipline; confirms no Bartlett-adjacent sources yet audited |
| GOV-9 | `LAD_Rung01_TheCell_AOP_v0_5.md` (`15R2SsTNB8sPmk1o7B52iAf14pkBRGd56`, 69,821 B, mod. 2026-08-02) — **current Rung 1, supersedes the work order's stale v0.3 pointer** | FULL TEXT saved locally; §§1–2, 5–6, honest-edge, competence table read in full; §§3–4, 7–12 headings + targeted excerpts | D4 |
| GOV-10 | `LAD_Canon_PROPOSED_TwoStacks_v0_1_20260801.md` (`1RbqrqHIU6bQ2usYdz3rhLCBE5iu9Qro7`) | FULL TEXT (subagent; saved locally); PROPOSED status preserved throughout | D4 |
| GOV-11 | `LAD_Handoff_Rung1RebuildAndTwoStacks_v1_0_20260801.md` | FULL TEXT (parent seat + subagent) | version-chain corrections |

**Authority findings flagged:** (a) Rung 1 authority has moved v0.3 → v0.4 (Ben) → **v0.5 (current, 2026-08-02)**; the work order's item 6 pointer is stale; D4 runs against v0.5. (b) A `Ladder_Charter_v0_3_PROPOSED.md` exists and the v0.7 audit reports treating "Charter v0.3" as its instruction field — installed status ambiguous; flagged for Ben, not resolved here. (c) The dedicated work-order deliverables folder under "2. Handoffs" also holds the AOP intervention-contract copies; a second, empty subfolder (`13Al5WrtIEUAE4RN1JCcCcnwzhmTjONd4`) exists. D1–D7 are placed in the folder containing the work order and transcript (`10S59I_-xmcP1rdCV1xMygwJDB0ZALRTr`), per work order §9 ("The source transcript and this work order will be present there").

## 3. Follow-up Bartlett work (mandatory full read; later development, never credited to 2020)

| ID | Source | Level | Key findings |
|---|---|---|---|
| FB-1 | Bartlett & Louapre 2022. "Provenance of life: Chemical autonomous agents surviving through associative learning." *Phys Rev E* 106:034401. doi:10.1103/PhysRevE.106.034401; arXiv:2210.05227 | **FULL TEXT** (arXiv/ar5iv render; PRE paywalled) | simulation-only associative learning in a hand-designed minimal reaction network (S→M short-term memory, M+T→L long-term AND-gate, antidote synthesis); survival advantage vs direct-response and pre-emptive strategies; extended into 2-D Gray–Scott spots. Does NOT establish wet-chemistry realization or emergence of learning. ~16 citations, no published critique found. |
| FB-2 | Bartlett, Gao & Yung 2022. "Computation by Convective Logic Gates and Thermal Communication." *Artificial Life* 28(1):96–107. doi:10.1162/artl_a_00358; arXiv:2204.11937 | **FULL TEXT** (arXiv/ar5iv; journal page 403) | 2-D lattice-Boltzmann Rayleigh–Bénard NOR gates (Ra=10⁴), cascaded five-NOR half-adder; "towards Turing-universality" only; no physical device; peer-reviewed (MIT Press *Artificial Life*). |
| FB-3 | Bartlett 2014 PhD thesis, U. Southampton (eprints.soton.ac.uk/370613) | **FULL TEXT** (ePrints PDF; abstract, TOC, chs. 7–8 read; chs. 2–6 at TOC/summary level) | thermo-chemical Gray–Scott: exothermic spots destabilize via plumes; moderate endothermic stable; exo+endo two-species "thermal symbiosis" mutually stabilizes, breaks at strong imbalance; thesis's own framing: compensatory response "not true homeostasis." Also anti-universal-MEPP result. |
| FB-4 | Bartlett & Bullock 2016. "A Precarious Existence: Thermal Homeostasis of Simple Dissipative Structures." ALIFE 2016 (MIT Press) pp. 608–615. doi:10.1162/978-0-262-33936-0-ch097 | **ABSTRACT ONLY** — direct.mit.edu 403 ×2, doi 403, CORE 403, Wayback 403, Semantic Scholar 404/429; metadata via OpenAlex (Gold OA claimed but unreachable this session) | the load-bearing source for B&W's region-8 "thermal Gray–Scott spots" sentence; abstract claims bidirectional boundary-temperature compensation, "completely emergent." Quantitative regime details sourced to FB-3 (read in full) instead. ≈3 citations. |
| FB-5 | Bartlett & Bullock 2015 (ECAL York), eprints.soton.ac.uk/376656 | **FULL TEXT** (ePrints PDF) | competition/oscillation between dissipative structures; **contains no homeostasis claim and no exponential-growth demonstration**. |
| FB-6 | Wong & Bartlett 2022. "Asymptotic burnout and homeostatic awakening." *J R Soc Interface* 19:20220029 | ABSTRACT + record (RSP 403, PMC captcha) | civilization-scale extension of the homeostasis pillar; published methodological rebuttal: Jackson & Criado-Perez 2024, doi:10.1098/rsif.2024.0140; no reply found. |
| FB-7 | Wong, Cleland, …, Bartlett, …, Hazen 2023. "On the roles of function and selection in evolving systems." *PNAS* 120(43):e2310223120 | ABSTRACT/METADATA (PNAS/PMC blocked) | "law of increasing functional information"; heavily criticized in the peer-reviewed record: Root-Bernstein 2024 PNAS Letter (doi:10.1073/pnas.2318689121) + authors' reply (doi:10.1073/pnas.2406598121); Lynch 2025 PNAS (doi:10.1073/pnas.2425772122), severe. Criticisms must not be back-propagated onto the 2020 paper. |
| FB-8 | Mechanotroph follow-up: no published realization or discovery 2020–2026. Priority caveat: Schulze-Makuch & Irwin's "kinetotroph" (2001) is a published antecedent the 2020 paper does not cite. | search-level | D3 |
| FB-9 | Sel'kov 1968 (glycolytic oscillator; tud.ttu.ee PDF) | **FULL TEXT** (subagent) | grounds the Selkov/Gray–Scott naming question (D2-C12) |

## 4. Independent literature set — per-cluster ledgers

The four cluster subagent reports are reproduced in full in the working record; the consolidated ledger below lists every source with its final verification level. Sources marked ▲ carry a load-bearing use in D2/D3; per the full-text rule, no ▲ source is below FULL TEXT unless its use is explicitly downgraded at point of use in D2/D3.

### 4.1 Definitions, evolution, open-endedness (cluster agent 1; fetches 2026-08-13/14)

- ▲ NASA Astrobiology "About Life Detection" page + NASA Science "Life in the Lab" — **FULL TEXT** (both pages). NASA's own pages vary between "the NASA definition" and "working definition." Provenance of the 1994 Joyce panel wording NOT primary-verified (converges with GOV-3's finding: Joyce Foreword unretrieved; Cleland & Chyba 2002 print a variant wording).
- ▲ Packard et al. 2019, OEE overview, *Artificial Life* 25(2) / arXiv:1909.04430 — **FULL TEXT** (arXiv PDF; §§1, 3.1, 3.5, 4). Establishes: OEE unachieved in ALife models; **no parasite-saturation mechanism anywhere in it**.
- ▲ Mills, Peterson & Spiegelman 1967, PNAS 58:217 — **FULL TEXT** (via mirror PDF at dosequis.colorado.edu; PNAS/PMC blocked). Verbatim: "By the 74th transfer, 83 per cent of the original genome had been eliminated." Paper does NOT claim a minimal sequence was reached. Work-order PMIDs (5328121/5248825) could not be confirmed — do not propagate.
- Kacian et al. 1972; Oehlenschläger & Eigen 1997 (further reductions to ~218 nt, ~50 nt) — SECONDARY ONLY (Wikipedia-level); not load-bearing, marked at point of use.
- Szathmáry & Maynard Smith 1995, *Nature* 374:227 — **ABSTRACT ONLY** (paywall). Book (1995/1997) SECONDARY ONLY.
- Watson & Szathmáry 2016 TREE — **ABSTRACT ONLY** (paywall; Soton ePrints PDF 403). Published critical response (Žliobaitė & Stenseth 2016) + authors' reply: METADATA ONLY.
- ▲ Watson et al. 2016, "Evolutionary Connectionism," *Evol Biol* 43:553 — **FULL TEXT** (Springer OA).
- ▲ Nonacs 2011 (NAS volume ch., NBK424872) — **FULL TEXT**. Hamilton's rule; worker sterility as kin-selection showcase.
- ▲ Warner, Mikheyev & Linksvayer 2017, MBE 34:1780 — **FULL TEXT** (OUP). Genomic signature of kin selection in obligately sterile workers.
- Hamilton 1964 — FULL TEXT NOT VERIFIED this session (role as primary formal proposal confirmed via the above).
- Nowak, Tarnita & Wilson 2010 *Nature* 466:1057 — ABSTRACT ONLY. Abbot et al. 2011 reply (~137 authors) — ABSTRACT ONLY (opening text).
- ▲ Valiant 2009, "Evolvability," *J ACM* 56(1) — **FULL TEXT** (mirror PDF). Evolvable ⊊ SQ ⊊ PAC; parity not evolvable; explicitly a computational model.
- ▲ Ray 1991, "An Approach to the Synthesis of Life" (Tierra; author-hosted PDF) — **FULL TEXT**. Parasites drove arms races and maintained diversity; stagnation attributed to mutation-driven melting, not parasites.
- ▲ Zaman et al. 2014, *PLoS Biol* 12:e1002023 — **FULL TEXT**. Host–parasite coevolution **increases** complexity (EQU in 17/50 coevolving vs 0/50 without).
- Mizuuchi, Furubayashi & Ichihashi 2022, *Nat Commun* 13:1460 — ABSTRACT ONLY (post-2020 movement).
- Green et al. 2021 (CoLD scale) — METADATA ONLY (post-2020 context).

### 4.2 Dissipative structures, autocatalysis, regulation, material memory (cluster agent 2; fetches 2026-08-14)

- ▲ Zhabotinsky, Scholarpedia BZ article — **FULL TEXT**. ▲ Winfree 1984, *J Chem Educ* 61:661 (prehistory of BZ; caltech-hosted PDF) — **FULL TEXT**; two-rejection history documented; exact rejection years need one further check (Kiprijanov 2016 located, not fetched).
- Pearson 1993 *Science* 261:189 (arXiv patt-sol/9304003) — ABSTRACT ONLY (landing page; spot growth/division language verified there).
- Lee, McCormick, Ouyang & Swinney 1994, *Nature* 369:215 — ABSTRACT ONLY ("'birth' through replication and 'death' through overcrowding").
- ▲ Lagzi, Soh, Wesson, Browne & Grzybowski 2010, JACS 132:1198 — **FULL TEXT** (mirror; ACS 403). Maze-solving; droplets "always found the shortest path"; **Hanczyc not an author**.
- ▲ Hanczyc 2014, *Life* 4:1038 (review) — **FULL TEXT** (MDPI). Hanczyc's own review credits maze-solving to Lagzi et al.
- Čejková, Novák, Štěpánek & Hanczyc 2014, *Langmuir* 30:11937 — FULL TEXT NOT VERIFIED (ACS 403, PubMed captcha; metadata via Semantic Scholar; maze-channel navigation seen only in press/supplementary-video coverage).
- Holler, Porcelli, Ieropoulos & Hanczyc 2018, *Sci Rep* 8:8408 — **FULL TEXT**.
- Keim & Nagel 2011, PRL 107:010603 — ABSTRACT ONLY (APS). ▲ Keim, Paulsen, Zeravcic, Sastry & Nagel 2019, *Rev Mod Phys* 91:035002 — **FULL TEXT** (arXiv:1810.08587).
- ▲ Blokhuis, Lacoste & Nghe 2020, PNAS 117:25230 — **FULL TEXT** (PMC7568248). Stoichiometric autocatalysis definition; five minimal cores; no growth-law axiom.
- ▲ Sakref & Rivoire 2024, *Commun Chem* 7 (PMC11494078 — identified) — **FULL TEXT**. Sub-exponential growth typical for non-enzymatic autocatalysts (product inhibition); exponentiality extrinsic-conditions-dependent.
- Sievers & von Kiedrowski 1994 *Nature* 369:221 — ABSTRACT ONLY; parabolic-growth law corroborated FULL TEXT via *Entropy* 13:1882 (2011, MDPI) and Sakref & Rivoire 2024. von Kiedrowski 1986 — cited via those; not fetched.
- Hordijk & Steel RAF theory — via Blokhuis et al.'s explicit linkage only.
- ▲ Bich, Mossio, Ruiz-Mirazo & Moreno 2015, *Biol Philos* 31:237 — **FULL TEXT** (author PDF; §§4, 5, 7). Dynamic stability vs regulation ("second-order control… dynamically decoupled").
- ▲ Sel'kov 1968 — **FULL TEXT** (see FB-9).

### 4.3 Forests, longevity, senescence, Gaia, planetary thermodynamics (cluster agent 3; fetches 2026-08-14)

- Simard et al. 1997, *Nature* 388:579 — ABSTRACT ONLY (paywall; 6%-of-uptake net transfer, shading modulation from abstract).
- Karst, Jones & Hoeksema 2023, *Nat Ecol Evol* 7:501 — ABSTRACT + publisher summary/figure captions (paywall; author correction doi:10.1038/s41559-023-02035-7 fetched FULL). Three-claim evaluation incl. "no peer-reviewed, published evidence" for mother-tree preferential provisioning.
- Henriksson et al. 2023, *New Phytol* 239:19 — ABSTRACT (Semantic Scholar; Wiley 403). Rillig et al. 2024, *Funct Ecol* — **FULL TEXT** (unito.it repository).
- ▲ USFS FEIS *Pinus longaeva* species review — **FULL TEXT** (fs.usda.gov mirror). Cones dehiscent, wind-dispersed, **not serotinous**; only low-severity surface fire survivable; a living White Mountains tree aged 5,062 yr.
- May et al. 2009, *PLoS ONE* 4:e8346 (Jurupa Oak >13,000 yr) — ABSTRACT (OA full text exists, not fetched). Vasek 1980 (King Clone) — FULL TEXT NOT VERIFIED (secondary only). Pando 2024–25 age preprint — preprint-stage, post-2020 movement only.
- Martínez 1998, *Exp Gerontol* 33:217 — ABSTRACT ONLY (PubMed). Schaible et al. 2015, PNAS 112:15701 — ABSTRACT ONLY (Semantic Scholar; PMC captcha).
- Jones et al. 2014, *Nature* 505:169 ("Diversity of ageing across the tree of life") — ABSTRACT (Semantic Scholar); demographic senescence definition anchor.
- ▲ Watson & Lovelock 1983, Daisyworld, *Tellus B* 35:284 — **FULL TEXT** (Tellus open archive). **Context only — Daisyworld does not occur in the supplied transcript.**
- ▲ Kirchner 2003, *Climatic Change* 58:21 — **FULL TEXT** (Harvard mirror). ▲ Lenton et al. 2018, TREE 33:633 — **FULL TEXT** (Soton accepted MS). Tyrrell 2013 *On Gaia* — SECONDARY ONLY. Lenton 1998 — NOT VERIFIED.
- ▲ Kleidon 2009, *Naturwissenschaften* 96:653 — **FULL TEXT** (Springer). Entropy budget (~900 mW m⁻² K⁻¹ total), solar ~5,760 K emission (visible/shortwave-dominated), MEP "no firm foundation yet."
- *Monorhaphis chuni* ~11,000-yr sponge (Jochum et al. 2012) — SECONDARY ONLY.

### 4.4 Bioenergetics, origin of life, translation, information engines (cluster agent 4; fetches 2026-08-14)

- ▲ Mitchell 1961, *Nature* 191:144 — **FULL TEXT** (hosted scan; publisher paywalled).
- Noji, Yasuda, Yoshida & Kinosita 1997, *Nature* 386:299 — ABSTRACT ONLY (γ-subunit rotation, >100 revolutions, >40 pN·nm).
- ▲ Kitadai, Kameya & Fujishima 2017, *Life* 7(4):39 (PMC5745552 — identified) — **FULL TEXT**. ▲ Orgel 2008, *PLoS Biol* 6:e18 — **FULL TEXT**. Muchowska et al. 2017 *Nat Ecol Evol* (6/11 rTCA reactions metal-promoted) — ABSTRACT ONLY. Muchowska, Varma & Moran 2019 *Nature* 569:104 — ABSTRACT ONLY. ▲ Garritano, Song & Thomas 2022, *PNAS Nexus* 1:pgac226 (rTCA taxon distribution) — **FULL TEXT** (OUP OA).
- Powner, Gerland & Sutherland 2009, *Nature* 459:239 — ABSTRACT ONLY.
- ▲ Woese 1998, PNAS 95:6854 (PMC22660) — **FULL TEXT** ("The universal ancestor is not a discrete entity…").
- ▲ Petrov et al. 2014, PNAS 111:10251 — **FULL TEXT** (author-hosted PDF LDW_102; PNAS/PMC blocked). Structural/computational retrodiction; **no functional reconstruction performed**.
- ▲ Bowman, Petrov, Frenkel-Pinter, Penev & Williams 2020, *Chem Rev* 120:4848 — **FULL TEXT** (author-hosted LDW_132). LSU catalyzes uncoded peptidyl transfer without SSU; decoding arrives late in the accretion model; **nowhere reports a stripped ribosome that translates**.
- ▲ Bose et al. 2022, *Nucleic Acids Res* 50:1815 — **FULL TEXT** (OUP OA). Protoribosome (60–150 nt PTC vestiges) forms a **single uncoded peptide bond**; no mRNA, no tRNA, no decoding. Post-2020.
- ▲ Koonin & Novozhilov 2017, *Annu Rev Genet* 51:45 — **FULL TEXT** (hosted PDF).
- Toyabe et al. 2010, *Nat Phys* 6:988 — ABSTRACT ONLY (nature.com + arXiv:1009.5287 abstract). Serreli, Lee, Kay & Leigh 2007, *Nature* 445:523 — ABSTRACT ONLY. Wilson et al. 2016, *Nature* 534:235 — ABSTRACT ONLY.
- ▲ Xie 2010, *Int J Biol Sci* 6:665 (PMC2974169 — identified) — **FULL TEXT** (a ratchet-flavored model paper, not consensus).
- ▲ Hwang & Karplus 2019, PNAS 116:19777 — **FULL TEXT** (author-hosted PDF). Kinesin force generation requires an active power stroke; mechanisms "not mutually exclusive."
- ▲ Moody et al. 2024, *Nat Ecol Evol* 8:1654 (LUCA ~4.2 Ga, ~2,657 proteins) — **FULL TEXT** (OA). Post-2020 movement only.
- Weiss et al. 2016, *Nat Microbiol* 1:16116 — ABSTRACT ONLY.

## 5. Retraction / correction status

Checked for every ledger source: **no retractions or expressions of concern found**. Corrections found and applied: Karst et al. 2023 author correction (reference-list only). Known version issues: arXiv vs journal versions used are noted per entry; Bartlett & Louapre read in the arXiv accepted-manuscript equivalent.

## 6. Search log

Consolidated per-cluster search logs (terms + dates + failure modes: PNAS 403s, PMC reCAPTCHA, EuropePMC robots, ACS 403s, Wiley 403s, paywalled Nature) are retained in the working record of each cluster report; representative entries are embedded in §4 above. All fetches 2026-08-13/14 UTC.

## 7. Access-failure summary (work order: documented attempts)

Systematically inaccessible this session: pnas.org (403 on all attempts; mitigated via PMC or author-hosted PDFs), pmc.ncbi.nlm.nih.gov (intermittent reCAPTCHA), europepmc.org (robots), ACS journals (403; mitigated via mirrors), Wiley (403), Nature paywalled titles (abstract-level only), direct.mit.edu ALIFE proceedings (403 — the one materially regrettable failure: FB-4 stays ABSTRACT ONLY; quantitative regime facts were instead taken from the thesis FB-3, read in full).

## 8. Reception-record gap (post-red-team addition)

B&W 2020 core-paper reception: ~76 citations (OpenAlex, 2026-08-14); no published rebuttal located by this session's searches. A systematic uptake/critique survey of the 2020 paper itself (treatment in post-2020 definition-of-life reviews) was NOT run and is carried to D7 as an open item (D6 finding 14).

— End of D1. No existing file was overwritten in producing this ledger. —
