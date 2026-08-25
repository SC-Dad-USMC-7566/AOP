# D3 — Science Report: Bartlett–Wong's "Lyfe," Mindscape 106, and What Survives Checking

**File:** `LAD_CS_BartlettLyfe_ScienceReport_v1_0_20260813.md`
**Reader:** Ben. Companion files: D1 (every source and its verification level), D2 (claim-by-claim episode audit). Every load-bearing statement here carries a grade and rests on a D1 ledger entry; nothing is reported above its access level. This version incorporates the D6 red-team repairs (disposition table in D6 Part II).

---

## 1. Executive verdict

Bartlett & Wong 2020 is a *vocabulary proposal*, not a result — and judged as one, it is better than its critics usually allow and weaker than its fans usually notice. Its real contributions are three: it cleanly separates the **process question** (what does a living state do?) from the **component question** (what is it made of?); it makes classification explicitly **boundary-relative** ("the pillars that can be ascribed to a certain system depend specifically on the boundaries with which we use to refer to that system" — paper §2, p.7), which most rival definitions hide; and it supplies a genuinely useful comparative zoo of near-life systems. Its real weaknesses are also three: two of its four pillar definitions are stipulations at odds with the formal literatures they borrow from (**autocatalysis ≡ exponential growth** — an outcome-based stipulation at odds with the stoichiometric definitions, and violated by parabolic growth in real template chemistry in its operating regimes [Settled; D1 §4.2]; **homeostasis extended to passive equilibrium relaxation** — which the regulation literature distinguishes as mere dynamic stability [physiology core Settled; the architecture machinery Synthesis; Bich et al. 2015, FULL TEXT]); the **learning pillar bundles** syntactic record, semantic use, and diachronic evolutionary success into one criterion, which makes it circular at the definition's own boundary (learning is defined by contribution to survival/proliferation; lyfe is defined by learning); and the claim that the four pillars are **"necessary and sufficient"** (p.7) is under-argued in a specific, quotable way: sufficiency for *lyfe* is stipulative (their own coinage), necessity is informally motivated for dissipation and homeostasis but never argued for autocatalysis or learning, and independence and completeness are never addressed — fatal for a "necessary and sufficient" claim even granting the two motivated halves. The episode is a friendly, wide-ranging tour that is right about most of physics and origins-of-life humility and wrong in six flagship, checkable places (D2: C04, C08, C20, C22, C28, C32; three lesser defects C15, C25, C27 in the D2 roster).

For the two projects: the four pillars are **useful as a rival lens and as benchmark fodder, not as canon** — for the Ladder, a boxed comparison at the pre-rung seam where single-feature definitions are already refused; for AOP, a non-equivalence map plus a hostile-case benchmark suite (D5). Nothing found here forces a canon change in either project.

## 2. The four pillars, rigorously (work order §5 questions 1–8)

**Q1 — exact operational definitions (paper §2, quoted at the point of definition):**
- *Dissipation:* "Lyfe cannot exist at equilibrium" + free-energy transduction mechanisms coupling exergonic to endergonic processes. This is a **state condition** (off-equilibrium) plus a **mechanism condition** (transduction), not a measured rate.
- *Autocatalysis:* "The ability of a system to exhibit exponential growth of representative measures of size or population in ideal conditions… as long as the effect leads to exponential growth of a suitable metric."
- *Homeostasis:* "The ability of a system to maintain key internal variables within ranges of ideal set points," explicitly extended to equilibrium systems ("an ideal gas at equilibrium… the archetype of stability") with an honest caveat paragraph (Landauer citation) conceding that biological homeostasis differs by consuming free energy.
- *Learning:* "The ability of a system to record information about its external and internal environment, process that information, and carry out actions that feed back positively on its probability of surviving/proliferating," with Darwinian evolution named as "one commonly cited biological learning process."

**Q2 — necessary, sufficient, independent, ordered?** The paper claims the four are "**necessary and sufficient** requirements of the lyving state" (p.7). The claim is partially motivated, never proven: dissipation's necessity is argued from the second law ("certainly the first necessary aspect of life"), homeostasis's from perturbation-plus-growth ("must have means to limit the variation"); autocatalysis and learning receive no necessity argument, and independence and completeness are nowhere addressed. Sufficiency is stipulative — lyfe is their coinage — so the exposed substantive claim is necessity-for-life ("life must be a subset of lyfe"), where dormancy is the pressure case (§4.1). They are *not* claimed independent: the Fig. 5 caption makes autocatalysis and learning **contingent on dissipation** ("require a continuous supply of free energy"), while homeostasis is *not* contingent ("can occur even in equilibrium systems"). Causal ordering is explicitly left open — the episode (L156–161) treats sequential-vs-simultaneous emergence as undecided, and the paper's §2.1 warns against reading the sublyfe list as a stepwise origin story. [Report grade: the necessity/sufficiency claim is **Speculative** as stated; the contingency structure is **Synthesis**.]

**Q3 — why eight sublyfe regions, not fifteen nonempty combinations?** Four binary properties give 15 nonempty subsets, 14 partial. The paper lists 8 partial regions + lyfe = 9. The six missing combinations are exactly the subsets containing **autocatalysis or learning without dissipation** ({A}, {L}, {A,L}, {A,H}, {H,L}, {A,H,L}). This follows from the Venn topology: A and L are drawn strictly inside D.

**Q4 — are the omissions logically, physically, or definitionally excluded?** **Definitionally-cum-physically**, and the paper says so in one sentence (Fig. 5 caption): sustained growth and learning are taken to require free-energy throughput (for learning, the Landauer argument in §2.1 does real work: harnessing equilibrium fluctuations would require measurement and erasure, which cannot be free). This is defensible physics [Settled for the Landauer half; Synthesis for the growth half], but note it makes the pillar count effectively *three-and-a-half*: dissipation is a precondition of two others, so the four are not four independent axes — a point that matters when anyone is tempted to map them onto AOP's four axes by cardinality (D5 §2).

**Q5 — does the autocatalysis definition improperly equate autocatalysis with exponential growth? Yes, with one adjudication to state carefully.** The formal literature defines autocatalysis stoichiometrically (Blokhuis, Lacoste & Nghe 2020, FULL TEXT: five minimal autocatalytic cores; no growth-law axiom), and the best-characterized non-enzymatic autocatalysts grow **sub-exponentially** in their operating regimes — von Kiedrowski's parabolic (√-law) growth from product inhibition, generalized by Sakref & Rivoire 2024 (FULL TEXT). The "ideal conditions" hedge is weaker than it looks but not dead: Sakref & Rivoire themselves note that "exponentiality is not an intrinsic property of an autocatalyst, but crucially depends on extrinsic conditions" and that exponential autocatalysts are designable — so a B&W defender can read "ideal conditions" as exactly that extrinsic qualifier. What the hedge cannot repair: the definition classifies by *outcome* (a growth law) rather than *mechanism* (stoichiometry), so it excludes the canonical non-enzymatic autocatalysts in the regimes where they actually run, and it admits externally driven exponential amplification with no autocatalytic mechanism at all (e.g., the output of an externally programmed amplifier). Exponential growth is a special case, not the definition. [Settled counter-evidence for the stoichiometric definition and the sub-exponential growth laws; the hedge-adjudication is this report's Synthesis.]

**Q6 — does the homeostasis definition conflate passive relaxation with active regulation? Yes, deliberately, and the paper flags it.** Region 2 grants "homeostasis only" to an equilibrium ideal gas. Bich et al. 2015 (FULL TEXT) is the sharpest published corrective: passive return is *dynamic stability*; even stoichiometric feedback is *constitutive stability*; **regulation** requires a dedicated, dynamically decoupled second-order subsystem. (Grading note: that homeostasis in the physiological tradition is active is settled; the specific stability/constitutive/second-order triple is the organizational school's proposal — Synthesis, one school, flagged as such.) AOP §11a sharpens the same cut into three architectures (no restoring force / set-point-as-fixed-point / decoupled separately-interventable reference) [AOP v1.27 pending stamp, §11a; SYNTHESIS there]. B&W's usage collapses all three into one pillar — which is precisely what makes their Venn regions legible to a general reader and useless as a discriminator at the life boundary.

**Q7 — does the learning definition bundle record/processing/use/function/survival in a circular or diachronic way? Yes, both.** The definition's third clause ("feed back positively on its probability of surviving/proliferating") imports (a) a **semantic** criterion (use, not mere storage — this half is well-posed and is exactly Kolchinsky–Wolpert semantic information, the construction AOP builds on), and (b) a **diachronic** criterion (proliferation; Darwinian evolution as a learning process), which quantifies over lineage success across generations. The circularity: lyfe is defined by learning, learning by contribution to survival/proliferation — i.e., by persistence itself. This is not fatal (one can read it as a fixed-point definition), but it means pillar 4 is not an independent test: you must already be able to score survival/proliferation to score learning. [Synthesis, this report's analysis; the KW anchor is Settled.]

**Q8 — how sensitive is classification to the declared system boundary? Maximally, and the paper embraces it.** The virus worked example (§2, p.7–8): a virion alone performs *no* pillar; virus+host+nutrients performs autocatalysis and dissipation; virus-in-coevolving-biosphere adds learning; some ecosystems add homeostatic contributions (auxiliary metabolic genes, lysis recycling). The paper concludes "lyfeness" is best assessed at ecosystem/planetary scale. What the paper does *not* supply is any discipline for declaring the boundary — no declaration schema, no rule for when re-drawing the boundary is legitimate, no treatment of nested systems' conflicting classifications. This is the single deepest point of contact with AOP, which has exactly that machinery (declaration tuple **D**) and exactly the corresponding open problem (level selection, §13a). See D5 §3.5.

## 3. Strongest contributions (worth keeping regardless of project use)

1. **Process-over-components, argued not just asserted** — the privileged-function critique (§1.1: RNA-first, metabolism-first, compartment-first all assume their function was primordial, "little to no evidence" survives the LUCA horizon), the Shinkansen/locomotive analogy, and the exaptation catalog make a genuinely good case that component-based origins definitions overcommit. [Synthesis, well-sourced.]
2. **Boundary-relative classification stated openly** (Q8) — most definitions of life smuggle the system boundary; B&W declare it. [Synthesis.]
3. **The comparative zoo** — fire, gas, damped oscillator, neural network, tragedy-of-commons systems, smart thermostat, Gray–Scott spots — is pedagogically excellent and maps cleanly onto benchmark cases (D5 §4).
4. **The lyfe/life split itself** — separating the universal-narrative question from the Earth-historical question (§1.3's historical/synthetic/universal taxonomy, after Mariscal et al. 2019) is a real conceptual service to astrobiology.
5. **Honest self-flagging** — the equilibrium-homeostasis caveat, the azotosome refutation citation (Sandström & Rahm 2020), and the "super-lyfe" agnosticism are all better epistemic conduct than the genre average.

## 4. Strongest failures and overstatements

1. **"Necessary and sufficient," under-argued** (Q2). The exposed claim is necessity-for-life, and dormancy is the counterexample the paper never confronts: a dormant spore flunks dissipation-as-ongoing-throughput on short clocks while remaining paradigmatically alive on the capacity reading. Two of four pillars get no necessity argument at all; independence and completeness get none. [This report's adversarial reading; Synthesis.]
2. **Autocatalysis ≡ exponential growth** (Q5) — an outcome-based stipulation at odds with the mechanism-based formal definitions, excluding real sub-exponential autocatalysts. [Settled counter-evidence for the definitions and growth laws; see Q5 for the hedge adjudication.]
3. **Homeostasis stretched to equilibrium relaxation** (Q6) — makes the pillar trivially satisfiable and forfeits the one distinction (regulation vs stability) that does discriminating work at the life boundary. [Physiology core Settled; the regulation-architecture machinery Synthesis, one school — see Q6.]
4. **Learning's diachronic bundling** (Q7) — folds evolution into a present-tense-sounding criterion; on any operational reading, scoring pillar 4 for a biosphere requires observing lineage dynamics, which collapses the definition's synchronic pretension.
5. **Episode-level defects** (fully documented in D2): parasite-caused complexity saturation (C04 — contradicted by Ray 1991 and Zaman et al. 2014, both FULL TEXT); "worker genes get nothing" (C08 — contradicted by kin-selection theory and genomic evidence); bristlecone fire-activated cones (C20 — contradicted by USFS FEIS); senescence = programmed cell death, hydra lack apoptosis (C22); "reconstructed primitive ribosome that still translates" (C28 — no such demonstration exists; the closest is a single uncoded peptide bond); "walker motion is not powered by ATP" (C32 — contradicted for kinesin by Hwang & Karplus 2019). These are the episode's errors, not the paper's; the paper is consistently more careful than the interview.

## 5. A serious defense of the framework

The strongest honest case for B&W: *definitions of life are instruments, and instruments are judged by what they let you do, not by their metaphysical hygiene.* NASA's Darwinian definition operationalizes poorly for mission design (evolution is unobservable on flyby timescales); B&W's pillars at least point at observables with shorter integration times (disequilibrium chemistry, growth curves, regulatory responses, adaptive behavior). The stipulative definitions are features on this reading: "exponential growth in ideal conditions" is *measurable in culture*; "maintains key variables" is *testable by perturbation*; even the equilibrium-homeostasis extension is a deliberate choice to make the Venn diagram exhaustive rather than to legislate biology. The boundary-relativity that critics call a bug is the framework being honest about something every rival hides. And the framework has been *productive*: it framed Bartlett & Louapre 2022 (chemical associative learning with survival advantage — the first constructive demonstration that pillar-4 behavior is achievable in a minimal reaction network), and it gives astrobiology a vocabulary for the Titan/mechanotroph class of hypotheses that the NASA definition cannot even state. A vocabulary that generates testable model systems is earning its keep. [Defense grade: Synthesis; the Bartlett & Louapre result is FULL TEXT-verified but simulation-only.]

## 6. A serious adversarial critique

The strongest honest case against: *the four pillars are a redescription, not a definition — and where they are precise, they are wrong.* Every pillar either borrows a formal concept and blunts it (autocatalysis without stoichiometry; homeostasis without regulation; learning without a semantics that stops short of natural selection) or states a truism (life is out of equilibrium). The necessity-and-sufficiency claim is doing no work: no borderline case in the paper is *decided* by the pillars that was not already decided by intuition — viruses are relocated rather than resolved (the system-level move makes "is X alyve?" unanswerable for any X smaller than an ecosystem, which is an abdication dressed as a paradigm shift). The Venn topology is inconsistent on its own terms: if homeostasis-as-stability is allowed at equilibrium, then crystals and buffered solutions hold "key variables in ranges" and region 2 swallows most of chemistry; if it is not, region 2 is empty. The framework's subsequent trajectory confirms the diagnosis: where it stayed qualitative (Fermi-paradox burnout, the PNAS "law of increasing functional information") it drew published rebuttals (Jackson & Criado-Perez 2024; Root-Bernstein 2024; Lynch 2025 — a severe critique from a leading evolutionary geneticist [METADATA ONLY per D1; characterization not quoted above its access level]); where it got quantitative (Bartlett & Louapre 2022), it had to *hand-design* the learning network, conceding that the pillars do not predict emergence. Four unweighted checkboxes with a declared-but-undisciplined boundary is a mnemonic, not a theory. [Critique grade: Synthesis; every factual anchor Settled per D1.]

## 7. 2020 vs later — what must not be conflated

The 2020 paper/episode may be credited with: the vocabulary, the sublyfe zoo, the boundary-relativity stance, the mechanotroph *proposal* (note: Schulze-Makuch & Irwin's "kinetotroph," 2001, is a published antecedent the paper does not cite). **Later developments, never retro-credited:** chemical associative learning (Bartlett & Louapre 2022); convective logic gates (Bartlett, Gao & Yung 2022, *Artificial Life*); civilization-scale homeostasis (Wong & Bartlett 2022; rebutted 2024); the "law of increasing functional information" (Wong et al. 2023 PNAS; heavily criticized 2024–25 — those criticisms also must not be back-propagated onto the 2020 paper); protoribosome peptide-bond results (Bose et al. 2022); the Karst et al. 2023 mycorrhizal corrective; Moody et al. 2024 LUCA reconstruction; Pando age preprints. The thermal-homeostasis simulations *predate* 2020 (thesis 2014; ALIFE 2016) and flow into the paper, not out of it.

## 8. Link atlas (verified primary/authoritative links; level per D1)

**The paper and its line**
- Bartlett & Wong 2020, *Life* 10(4):42 (OA): https://doi.org/10.3390/life10040042 [FULL TEXT]
- Bartlett & Louapre 2022, PRE 106:034401 / arXiv:2210.05227: https://doi.org/10.1103/PhysRevE.106.034401 [FULL TEXT via arXiv]
- Bartlett, Gao & Yung 2022, *Artificial Life* 28:96: https://arxiv.org/abs/2204.11937 [FULL TEXT]
- Bartlett 2014 PhD thesis: https://eprints.soton.ac.uk/370613/ [FULL TEXT]
- Wong & Bartlett 2022, JRSI 19:20220029: https://doi.org/10.1098/rsif.2022.0029 [ABSTRACT]; rebuttal: https://doi.org/10.1098/rsif.2024.0140 [METADATA]

**Dissipative-structure zoo**
- Winfree 1984, BZ prehistory (the rejection story, documented): https://dna.caltech.edu/Papers/prehistory1984.pdf [FULL TEXT]
- Zhabotinsky's own BZ article: http://www.scholarpedia.org/article/Belousov-Zhabotinsky_reaction [FULL TEXT]
- Pearson 1993, Gray–Scott patterns: https://arxiv.org/abs/patt-sol/9304003 [ABSTRACT]
- Lee et al. 1994, self-replicating spots: https://doi.org/10.1038/369215a0 [ABSTRACT]
- Lagzi et al. 2010, maze-solving droplets (the *correct* attribution): https://doi.org/10.1021/ja9076793 [FULL TEXT via mirror]
- Hanczyc 2014 droplet review (OA): https://doi.org/10.3390/life4041038 [FULL TEXT]
- Keim et al. 2019, "Memory formation in matter," RMP 91:035002: https://arxiv.org/abs/1810.08587 [FULL TEXT]

**Autocatalysis, formally**
- Blokhuis, Lacoste & Nghe 2020, PNAS 117:25230 (OA via PMC): https://doi.org/10.1073/pnas.2013527117 [FULL TEXT]
- Sakref & Rivoire 2024, *Commun Chem* (growth laws, product inhibition): https://doi.org/10.1038/s42004-024-01250-y [FULL TEXT]
- Bich et al. 2015, biological regulation: https://doi.org/10.1007/s10539-015-9497-8 [FULL TEXT via author PDF]

**Evolution, learning, workers**
- Ray 1991, Tierra: http://tomray.me/pubs/alife2/Ray1991AnApproachToTheSynthesisOfLife.pdf [FULL TEXT]
- Zaman et al. 2014, coevolution drives complexity: https://doi.org/10.1371/journal.pbio.1002023 [FULL TEXT]
- Packard et al. 2019, OEE overview: https://arxiv.org/abs/1909.04430 [FULL TEXT]
- Mills, Peterson & Spiegelman 1967 (mirror scan): https://dosequis.colorado.edu/Courses/MethodsLogic/papers/Speigelman1967.pdf [FULL TEXT]
- Valiant 2009, "Evolvability," JACM (mirror): https://www.diochnos.com/about/ValiantEvolvability.pdf [FULL TEXT]
- Watson et al. 2016, Evolutionary Connectionism (OA): https://doi.org/10.1007/s11692-015-9358-z [FULL TEXT]
- Nonacs 2011, kin selection in social insects: https://www.ncbi.nlm.nih.gov/books/NBK424872/ [FULL TEXT]
- Warner et al. 2017, genomic kin-selection signature: https://doi.org/10.1093/molbev/msx123 [FULL TEXT]

**Trees, hydra, Gaia, planet**
- USFS FEIS, *Pinus longaeva* (the serotiny corrective): https://www.fs.usda.gov/database/feis/plants/tree/pinlon/all.html [FULL TEXT]
- Karst, Jones & Hoeksema 2023 (mycorrhizal corrective): https://doi.org/10.1038/s41559-023-01986-1 [ABSTRACT+]
- Simard et al. 1997: https://doi.org/10.1038/41557 [ABSTRACT]
- Martínez 1998: https://doi.org/10.1016/S0531-5565(97)00113-7 [ABSTRACT]; Schaible et al. 2015: https://doi.org/10.1073/pnas.1521002112 [ABSTRACT]
- Watson & Lovelock 1983, Daisyworld (open archive): https://b.tellusjournals.se/articles/10.3402/tellusb.v35i4.14616 [FULL TEXT] *(context: not in the supplied transcript)*
- Kirchner 2003, Gaia conjectures & refutations: https://doi.org/10.1023/A:1023494111532 [FULL TEXT via mirror]
- Lenton et al. 2018, Selection for Gaia: https://doi.org/10.1016/j.tree.2018.05.006 [FULL TEXT via ePrints]
- Kleidon 2009, Earth-system thermodynamics: https://doi.org/10.1007/s00114-009-0509-x [FULL TEXT]

**Bioenergetics, ribosome, code, motors, demons**
- Mitchell 1961 (hosted scan): https://naturedocumentaries.org/wp-content/uploads/2020/04/ProtonGradient_Mitchell1961.pdf [FULL TEXT]
- Noji et al. 1997, F1 rotation: https://doi.org/10.1038/386299a0 [ABSTRACT]
- Orgel 2008, implausibility of prebiotic cycles: https://doi.org/10.1371/journal.pbio.0060018 [FULL TEXT]
- Kitadai et al. 2017, rTCA origins perspective: https://doi.org/10.3390/life7040039 [FULL TEXT]
- Garritano et al. 2022, carbon-fixation distribution: https://doi.org/10.1093/pnasnexus/pgac226 [FULL TEXT]
- Woese 1998, the universal ancestor: https://doi.org/10.1073/pnas.95.12.6854 [FULL TEXT]
- Petrov et al. 2014, ribosome accretion (author PDF): https://williams.chemistry.gatech.edu/publications/LDW_102.pdf [FULL TEXT]
- Bowman et al. 2020, Root of the Tree (author PDF): https://williams.chemistry.gatech.edu/publications/LDW_132.pdf [FULL TEXT]
- Bose et al. 2022, protoribosome peptide bond: https://doi.org/10.1093/nar/gkac052 [FULL TEXT]
- Koonin & Novozhilov 2017, genetic code: https://doi.org/10.1146/annurev-genet-120116-024713 [FULL TEXT via hosted PDF]
- Toyabe et al. 2010, information-to-energy: https://doi.org/10.1038/nphys1821 [ABSTRACT]
- Serreli et al. 2007, molecular information ratchet: https://doi.org/10.1038/nature05452 [ABSTRACT]
- Wilson et al. 2016, autonomous chemically fuelled motor: https://doi.org/10.1038/nature18013 [ABSTRACT]
- Hwang & Karplus 2019, power stroke vs ratchet (author PDF): https://doi.org/10.1073/pnas.1818589116 [FULL TEXT]
- Moody et al. 2024, LUCA (OA): https://doi.org/10.1038/s41559-024-02461-1 [FULL TEXT]

— End of D3. —
