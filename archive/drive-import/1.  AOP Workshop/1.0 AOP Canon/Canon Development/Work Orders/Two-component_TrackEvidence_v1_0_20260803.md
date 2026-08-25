# Two-component (bifunctional HK) retrieval — Gate 1, AOP life-criterion falsification arc

**Track:** robust two-component systems (EnvZ/OmpR primary; NRII/NRI backup) as the leading
NEGATIVE CONTROL test article.
**Seat:** Claude Science (BUILDER). This document is a PROPOSAL for another seat to verify. It
selects nothing and pairs nothing.
**Version:** v1 · 2026-08-02

Retrieval tags used throughout: `[primary-verified]` = I read the passage in the primary;
`[primary-abstract-only]`; `[secondary]`; `[not-retrieved]`.

---

## 0. Headline findings (read these first)

1. **The set-point is a rate-constant expression, not a state.** Two independent primaries give the
   robust output in closed form as a ratio of kinetic constants with no dynamical variable in it.
   Batchelor & Goulian's Eq. 2 gives `[OmpR-P] = C_p + ...` where `C_p = (k_k/k_p)·K_Mp`
   `[primary-verified]`. Shinar et al.'s Eq. 7 gives `Y_P` as a function of rate constants only, and
   they state it plainly: <q>the output YP does not depend on the level of any of the proteins in the
   system, or on the level of ATP</q> `[primary-verified]`. This is **target-as-parameter** in the
   brief's sense, established from the equations, not asserted.
2. **The "corrects" half is WEAKER than the brief hoped, and I could not fix it.** Batchelor &
   Goulian 2003 is entirely steady-state. It establishes robustness *across* steady states reached
   under different sustained expression levels. I found **no** primary showing EnvZ/OmpR
   dynamically restoring OmpR-P after a kick to OmpR-P itself. The two claims are different and I
   did not conflate them. See §3.
3. **A second, independent problem for "corrects": the circuit is OPEN LOOP.** Batchelor, Silhavy &
   Goulian (J Bacteriol 2004) tested for feedback from porin output back into the regulatory circuit
   and found none: <q>porin osmoregulation is under open-loop, continuous control</q>
   `[primary-verified]`. This is a stronger and more awkward result than "no separable reference" —
   it says the regulated *output* is not even sensed. Prime needs this.
4. **The P1 kill-condition check returns a REAL THREAT, and it is the most important thing on this
   page.** Hsing & Silhavy (J Bacteriol 1998) isolated single-copy chromosomal *envZ* alleles that
   **reset the balance of EnvZ's kinase and phosphatase activities and hold OmpR-P at a shifted
   level while the correction machinery remains intact and functional**: <q>these suppressor
   mutations alone reset the balance of the enzymatic activity toward K+ P-</q> and <q>The balance
   was reset such that even at low osmolarity, the level of OmpR-P was still higher than that in the
   wild type at high osmolarity</q> `[primary-verified]`. See §4 for why this is and is not
   competent misregulation.
5. **A cleaner, non-mutational set-point mover exists: MzrA.** Overexpressing a *separate protein*
   biases EnvZ toward higher OmpR-P **while the system still responds to osmolarity**:
   <q>porin expression still responds to medium osmolarity in cells lacking or overexpressing
   MzrA</q> `[primary-verified]`. This is a trans-acting, dose-tunable set-point shift that leaves
   signal reception intact — a much better intervention handle than a point mutation, and it
   sharpens the P1 threat rather than dissolving it.

---

## 1. S.1 — dynamical description + performable interventions

**PASS.** `[primary-verified]`

Batchelor & Goulian give an explicit ODE model: <q>The system is characterized by six first-order
ordinary differential equations</q>, with ten parameters (eight rate constants plus `[OmpR]_T` and
`[EnvZ]_T`); the steady state <q>reduce to a cubic equation for [OmpR-P]</q>. In the physiological
limit `[OmpR]_T >> [EnvZ]_T` they derive Eq. 1 and then Eq. 2. `[primary-verified]`

Shinar et al. 2007 give a seven-ODE mass-action model with a flux-balance *argument* (phosphoryl
influx `J_i` = outflux `J_o`) yielding Eq. 7 analytically. Note: this is a phosphoryl-flux balance
inside a kinetic model, **not** a constraint-based flux-balance metabolic model — S.1's exclusion of
flux-balance models does not bite here. `[primary-verified]`

Shinar & Feinberg's ACR framework is stated over mass-action reaction networks with explicit
reaction schemes: the EnvZ-OmpR network (7) has <q>nine complexes, three linkage classes, and its
rank is five, so its deficiency is one</q> `[primary-verified]` (read in the 2011 Math Biosci
companion, which is open; the Science 2010 paper itself is paywalled — see §7).

Interventions are physically performable and published: titratable expression of EnvZ or OmpR from
an IPTG-inducible plasmid `[primary-verified]`; chromosomal point mutations in *envZ* recombined in
single copy `[primary-verified]`; and MzrA overexpression / deletion `[primary-verified]`.

## 2. S.2 — candidate stored reference

**FAIL.** `[primary-verified]` — and this failure is the *point* of the negative control.

There is no slow variable whose value the fast dynamics track. The output is set by
`C_p = (k_k/k_p)·K_Mp` (Batchelor & Goulian Eq. 2) and by
`Y_P = (k_{-3}+v_p)/k_3 · v_a(s)/v_p` (Shinar Eq. 7) — expressions in rate constants alone.
`[primary-verified]`

The slow variables that *do* exist are the conserved protein totals `[EnvZ]_T` and `[OmpR]_T`,
which change on the slow synthesis/dilution timescale. But their role is the exact inverse of a
stored reference: the architecture makes the output **independent** of them. Shinar & Feinberg
state the timescale premise explicitly for the toy ACR system — <q>A and B are synthesized and
degraded over timescales that are much longer than the equilibration timescale</q> — and the
consequence: <q>All of the positive steady states of the system have exactly the same value for c_A,
regardless of the total protein concentration T</q>. `[primary-verified]`

So the one available slow variable is precisely what the target is *insensitive to*. This is a
model-free corrector with the target sitting in the constitutive kinetics, evidenced rather than
asserted.

Structural mechanism, verified against the ACR literature's own claim: bifunctionality is
load-bearing. Shinar et al. state that if dephosphorylation were done by a separate phosphatase Z,
<q>Robustness would be lost</q>, because the steady state would then depend on both sensor and
phosphatase levels. `[primary-verified]` Shinar & Feinberg give the structural version — deficiency
one plus <q>distinct non-terminal complexes that differ only in species s</q> (their Theorem 6.1),
satisfied in the EnvZ-OmpR network by the complexes `XT` and `XT + Y_p`. `[primary-verified]`

## 3. S.3 — independent perturbability (does an operation MOVE the set-point without disabling the machinery?)

**PARTIAL — and the partiality is informative.** `[primary-verified]`

Two published operations shift the output level while leaving the system responsive:

- **Point mutations in *envZ* that reset the kinase/phosphatase balance** (Hsing & Silhavy 1998).
  These move the target. But the same operation changes the rate constants that *are* the machinery
  — exactly the state-vs-parameter collision the brief anticipated. Not a clean set-point move.
  `[primary-verified]`
- **MzrA dosage** (Gerken, Charlson, Cicirelli, Kenney & Misra, Mol Microbiol 2009). A separate
  membrane protein whose overexpression biases EnvZ toward OmpR-P accumulation. Biochemically it
  works by shifting EnvZ's enzymology: the EnvZ R397L pleiotropic allele they characterize has
  <q>approximately 10-fold lower turnover rate (0.12 μmol Pi mg−1 h−1) compared with the wild type
  (1.48 μmol Pi mg−1 h−1)</q> with similar autophosphorylation, i.e. a phosphatase defect
  `[primary-verified]`. MzrA is a better *handle* (trans-acting, dose-tunable, machinery genetically
  untouched) but mechanistically it too acts by retuning kinase/phosphatase balance — it moves the
  parameter, not a state.

There is no operation in this literature that moves a stored value while leaving all rate constants
fixed, because there is no stored value. That is the correct answer for a negative control, but it
means S.3 is satisfied *only* in the degenerate sense that the target is movable-by-retuning.

## 4. THE P1 KILL-CONDITION CHECK — a live threat, reported without softening

**Does a published mutant of EnvZ/OmpR regulate precisely to a shifted output level with the
correction machinery intact? YES, arguably.** `[primary-verified]`

Hsing & Silhavy 1998 constructed intragenic suppressors of two kinase-deficient (K− P+) *envZ*
alleles, then recombined the suppressor mutations **alone, in single copy, at the chromosomal
locus** — so this is not a plasmid-overexpression artifact. Result: <q>all of the isolated
suppressor mutations tested activate ompC and repress ompF constitutively, suggesting that these
suppressor mutations alone reset the balance of the enzymatic activity toward K+ P-</q>, and
crucially, <q>The balance was reset such that even at low osmolarity, the level of OmpR-P was still
higher than that in the wild type at high osmolarity.</q> `[primary-verified]`

The framing in that paper is itself set-point language: <q>the level of ompF and ompC transcription
reflects the level of OmpR-P, which is set by the sum of EnvZ kinase and phosphatase activities in
vivo</q>. `[primary-verified]`

And MzrA gives the non-mutational version with reception demonstrably intact: <q>porin expression
still responds to medium osmolarity in cells lacking or overexpressing MzrA</q> — with the authors'
own conclusion that <q>MzrA appears to alter the output of the EnvZ/OmpR system but not its ability
to receive and respond to various environmental signals</q>. `[primary-verified]`

**Why this is a threat to P1.** P1 dies if a system the criterion EXCLUDES turns out to have
competent misregulation. EnvZ/OmpR is exactly such a system (S.2 FAIL → excluded). And here is an
intervention producing regulation toward a wrong output level with the regulatory machinery
functional and still signal-responsive. On a naive reading of "competent misregulation," this
qualifies.

**Why it may not be, stated as the conceptual subtlety and not as a rescue.** In every case the
operation *is* a change to the rate constants that constitute the corrector — R397L's 10-fold
turnover loss is a machinery change, and the Hsing suppressors are described as changing enzymatic
balance, not as moving a separately stored value. So the honest statement is: this is a *target
shift achieved by retuning the machinery*, which is precisely what "target-as-parameter" predicts
should be indistinguishable from a machinery change. Whether that counts as competent misregulation
depends on how Gate 1 adjudicates the state-vs-parameter distinction — and P1's phrasing does not
currently settle it.

**Unresolved and material: precision.** "Regulates *precisely* toward the wrong target" requires
showing the shifted level is regulated (held, robust) and not merely elevated. I found **no**
primary that repeats the Batchelor & Goulian robustness assay (titrating `[EnvZ]_T`/`[OmpR]_T`) in
one of these shifted backgrounds. That experiment appears not to have been done. Its absence is
the single largest gap in this track, and it is the experiment that would decide whether P1 is
actually threatened.

## 5. S.4 — tunable slow/fast ratio over ≥2 orders of magnitude

**PARTIAL.** `[primary-verified]` for the intervention range; the *ratio* is not what S.4 wants.

Batchelor & Goulian tuned EnvZ <q>over a wide range from 10-fold below to 10-fold above WT
levels</q> (~2 orders of magnitude) and OmpR <q>over almost 2.5 orders of magnitude (10-fold below
to 30-fold above WT levels)</q>. `[primary-verified]` So the *concentration* axis is tunable over
≥2 OOM by published methods.

But the slow/fast *timescale ratio* is a different axis. The separation invoked in this literature
is protein synthesis/dilution (slow) vs phosphotransfer equilibration (fast) `[primary-verified]`,
and I found no published protocol tuning that ratio over orders of magnitude in this system. Since
S.2 already fails — there is no slow reference variable — a slow/fast ratio scan has no reference
whose timescale to scan. For a negative control this is arguably moot; I flag it rather than score
it PASS.

## 6. S.5 — lifetime readout and comparison class

**WEAK.** `[secondary]` / `[not-retrieved]` for the survival link.

- No survival, hazard, or first-passage readout for EnvZ/OmpR was retrieved. My searches for
  osmotic-survival or fitness phenotypes of *envZ*/*ompR* mutants returned nothing on point.
  `[not-retrieved]`
- The nearest thing to a lifetime-flavoured result is theoretical and cuts against the system:
  Anderson, Enciso & Johnston (J R Soc Interface 2014) show ACR networks under stochastic kinetics
  <q>undergo an extinction event</q> destroying ACR, with a quasi-stationary distribution beforehand
  `[primary-verified]`; Enciso (J R Soc Interface 2016) shows the robustness is <q>transiently
  robust</q> — Poisson-like around the deterministic mean for long finite times `[primary-verified]`.
  These are first-passage-flavoured results about the *architecture*, not organismal survival, and I
  am not computing anything from them.
- Comparison class: the ACR literature supplies the matched contrast structurally rather than
  experimentally — Shinar et al. state that a *monofunctional* kinase plus separate phosphatase Z
  loses robustness `[primary-verified]`. A monofunctional-HK system in the same organism would be a
  clean architecture-matched comparator; I did not find one built and assayed.

## 7. Reading A / Reading B eligibility

- **Reading A (STRICT / autonomy): NO.** Reading A needs slow coordinates `x` closed in themselves,
  `ẋ = f(x)`, with `y` depending on `x`. Here the target is not a coordinate at all — it is
  `(k_k/k_p)·K_Mp`, a constant of the rate law `[primary-verified]`. There is no `x` to be closed.
  Fails at the first clause, not on the feedback clause.
- **Reading B (LOOSE / scale separation): NO.** Reading B is more permissive but still needs a slow
  *variable* with a load-bearing coupling that sets `y`'s operating point. The available slow
  variables (`[EnvZ]_T`, `[OmpR]_T`) have a declared timescale separation `[primary-verified]` and
  are separately addressable `[primary-verified]`, but their coupling onto the output is
  **structurally nullified** — that is the content of ACR `[primary-verified]`. A coupling engineered
  to have no effect on the operating point is the opposite of load-bearing.
- **The two readings AGREE here.** That agreement is worth noting: EnvZ/OmpR is ineligible under
  both, so it does not sit in the zone where Gate 1's unadjudicated ambiguity could flip a verdict.
  For a negative control this is a strength — the exclusion is not reading-dependent.

## 8. Target-as-state or target-as-parameter

**PARAMETER**, determined from the published equations rather than inferred. `[primary-verified]`

The target appears in two independently derived closed forms as a function of rate constants only:
Batchelor & Goulian Eq. 2 (`C_p = (k_k/k_p)·K_Mp`) and Shinar et al. Eq. 7. Moving it requires
changing a kinetic constant, and the retrieved mutants confirm that this is the same operation as
degrading the machinery: EnvZ R397L shifts the output and loses ~10-fold of phosphatase turnover
`[primary-verified]`. There is no state whose value the fast dynamics track.

Note the one genuinely parameter-like *input*: the signal enters Shinar's Eq. 7 through `v_a(s)` —
<q>The output is responsive to the input signal via the rate constant va(s)</q> `[primary-verified]`.
So even the physiological signal acts by moving a rate constant. The architecture has no state-valued
target anywhere.

## 9. Role recommendation

**NEGATIVE_CONTROL**, with two caveats prime must weigh (I do not pair and do not select).

The model-free half is well evidenced: closed-form rate-constant set-point from two independent
primaries, structural ACR account of *why* (bifunctionality), and a stated loss-of-robustness
condition if bifunctionality is removed. All `[primary-verified]`.

Caveat 1 — **"corrects" is not established in the dynamic sense.** What is established is
robustness across steady states, plus the negative result that the circuit is open loop
`[primary-verified]`. If the order requires a system that *demonstrably restores* its output after a
kick, EnvZ/OmpR does not currently have that evidence, and the open-loop finding suggests it may not
be obtainable for the porin output at all.

Caveat 2 — **the P1 threat in §4 is real and unresolved**, and it lands on the negative control
itself. An excluded system with published set-point-shifted-but-still-responsive variants is exactly
the shape of P1's kill condition.

**Match quality for pairing with an *E. coli* positive candidate** (offered as evidence, not as a
pairing): same organism; same signalling chemistry (His-Asp phosphotransfer); same intervention
class (chromosomal point mutation, titratable plasmid expression, trans-acting modulator dosage);
same readout technology (chromosomal two-colour fluorescent transcriptional fusions,
`[primary-verified]`). Architecturally it is the *bifunctional* limb of the contrast that the ACR
literature itself names as decisive, which makes it a structurally motivated comparator rather than
a merely convenient one.

## 10. NRII/NRI (NtrB/NtrC) — backup, less depth

- Straube (PLoS Comput Biol 2014) treats NRII/NRI alongside PhoQ/PhoP as bifunctional systems where
  <q>binding of an allosteric effector (or PII) inhibits the autokinase activity and, concomitantly,
  activates the phosphatase activity</q>, and reports that in NRII/NRI <q>the occurrence of
  ultrasensitivity is (partly) suppressed by the intrinsic autophosphatase activity of NRI</q>.
  `[primary-verified]` Same structural verdict as EnvZ/OmpR: robustness/target from enzymology, no
  stored state.
- Straube also confirms the Batchelor-Goulian result independently: the model <q>predicts that, in
  the limit, the concentration of OmpR-P is approximately independent of variations in the total
  concentration of the sensor kinase</q>. `[primary-verified]`
- The nitrogen system's bifunctional-enzyme robustness result (Hart, Madar, Yuan, Bren, Mayo,
  Rabinowitz & Alon,
  *Robust control of nitrogen assimilation by a bifunctional enzyme in E. coli*, Mol Cell 2011,
  DOI 10.1016/j.molcel.2010.12.023) is **paywalled and `[not-retrieved]`** — abstract only, via
  PubMed metadata: the mechanism is <q>based on the avidity of a bifunctional enzyme,
  adenylyltransferase (AT/AR), to its multimeric substrate</q> `[primary-abstract-only]`. I did not
  read its equations and make no claim about them. See §11.
- No nitrogen-starvation survival readout retrieved. `[not-retrieved]`

## 11. Blocked-retrieval ledger

| Citation | DOI | Routes attempted | Why it mattered |
|---|---|---|---|
| Shinar G. & Feinberg M., *Structural sources of robustness in biochemical reaction networks*, Science 327:1389–1391 (2010) | 10.1126/science.1183372 | `fetch_article_fulltext` (Unpaywall → no OA location; Semantic Scholar → no openAccessPdf; PMC → no PMCID; CrossRef TDM → no links; DOI resolve → HTTP 403). No mirrors or proxies attempted. | The canonical structural ACR statement. **Mitigated, not solved:** I read the authors' own open-access companion (Shinar & Feinberg, Math Biosci 231:39–48, 2011, PMC3086454) which restates Theorem 6.1 and works the EnvZ-OmpR network explicitly. Claims in §2 rest on that 2011 primary, which I read, and are tagged accordingly. The Science paper itself remains `[not-retrieved]`. |
| Hart Y., Madar D., Yuan J., Bren A., Mayo A.E., Rabinowitz J.D. & Alon U., *Robust control of nitrogen assimilation by a bifunctional enzyme in E. coli*, Mol Cell 41(1):117–127 (2011) | 10.1016/j.molcel.2010.12.023 | `fetch_article_fulltext` twice (Unpaywall → no valid OA PDF; Semantic Scholar → http-only URL refused by the fetcher; PMC → no PMCID; CrossRef TDM → nothing accessible; DOI resolve → landing page only). Note: the first attempt returned a *mismatched* title ("Ewing sarcoma protein…"), so that response was discarded rather than used. | The bifunctional-enzyme robustness result for the nitrogen system — the backup track's core primary. Its equations would settle whether the AT/AR avidity mechanism is also target-as-parameter. §10 is abstract-only and labelled as such. |
| Aiba et al. 1989 (J Biol Chem); Tokishita et al. 1991 (J Biol Chem) — prior pleiotropic *envZ* alleles with elevated OmpR-P half-life | none indexed in PubMed metadata | PubMed metadata retrieved; no PMCID; no DOI to route to `fetch_article_fulltext`. | These are the earliest reports of phosphatase-diminished *envZ* alleles and would extend the §4 mutant series. I rely on them only as reported by Gerken et al. 2009 — `[secondary]`, and I have not verified their content. |
| Robustness assay repeated in a set-point-shifted *envZ* background | — | Searched PubMed across ACR-mutant, envZ-allele, and set-point phrasings; nothing on point returned. | This is the experiment that would decide whether the §4 mutants show *precise* regulation to a wrong target (i.e. whether P1 is genuinely threatened). I believe it has not been published; recorded as a gap, not as a negative result. |

## 12. Primaries actually read (bibliographic metadata verified separately from content)

**Metadata provenance.** Author lists, titles, journals, years, volumes, issues and page ranges below
were read from PubMed `get_article_metadata` records (author `last_name`/`initials` fields and the
`citation` volume/issue/pages fields) — not from memory. Items 8 and 9 (Anderson et al.; Enciso) had
no PubMed record in hand, so their authors, volume and article numbers were read from the "Cite this
article" line and byline of the PDFs themselves. "Read" means I read the passage relied on;
bibliographic verification is separate from content verification, per the brief.

Three author-list errors were caught and corrected during this check, and I flag them rather than
silently fixing them: I had written Hsing & Silhavy 1998 with two authors (the record shows four:
Hsing W., Russo F.D., Bernd K.K., Silhavy T.J.); I had attached a spurious "Zhang Y. et al." to the
mBio 2017 paper (the record shows two authors: Gao R., Stock A.M.); and I had the Hart et al. 2011
author list wrong and incomplete (the record shows seven: Hart Y., Madar D., Yuan J., Bren A.,
Mayo A.E., Rabinowitz J.D., Alon U.). All three were surname strings I had not sourced from a tool
result. No content claim in this document depended on them.

1. **Batchelor E. & Goulian M.**, *Robustness and the cycle of phosphorylation and dephosphorylation
   in a two-component regulatory system*, PNAS 100(2):691–696 (2003). DOI 10.1073/pnas.0234782100;
   PMC141058; PMID 12522261. **Read:** model description, Eq. 1, Eq. 2, definitions of `C_t`/`C_p`,
   the EnvZ and OmpR titration ranges. `[primary-verified]`
2. **Shinar G., Milo R., Rodríguez Martínez M. & Alon U.**, *Input–output robustness in simple
   bacterial signaling systems*, PNAS 104(50):19931–19935 (2007). DOI 10.1073/pnas.0706792104;
   PMC2148400; PMID 18077424. **Read:** flux-balance derivation Eqs. 1–7, the statement that `Y_P`
   depends only on rate constants, the `Y_T` threshold caveat, and the three necessity arguments
   (ATP-dependent dephosphorylation, bifunctionality, two-step kinase). `[primary-verified]`
3. **Shinar G. & Feinberg M.**, *Design principles for robust biochemical reaction networks: what
   works, what cannot work, and what might almost work*, Math Biosci 231(1):39–48 (2011).
   DOI 10.1016/j.mbs.2011.02.012; PMC3086454; PMID 21377478. **Read:** ACR definition, toy system
   Eqs. 1–4, §3.1 EnvZ-OmpR networks (7)/(8) with deficiency-one accounting, Theorem 5.1,
   Theorem 6.1. `[primary-verified]`
4. **Batchelor E., Silhavy T.J. & Goulian M.**, *Continuous control in bacterial regulatory
   circuits*, J Bacteriol 186(22):7618–7625 (2004). DOI 10.1128/JB.186.22.7618-7625.2004; PMC524909;
   PMID 15516575. **Read:** open/closed-loop framing, the porin feedback test design, and the
   open-loop conclusion. `[primary-verified]`
5. **Hsing W., Russo F.D., Bernd K.K. & Silhavy T.J.**, *Mutations that alter the kinase and
   phosphatase activities of the two-component sensor EnvZ*, J Bacteriol 180(17):4538–4546 (1998).
   DOI 10.1128/JB.180.17.4538-4546.1998;
   PMC107465; PMID 9721293. **Read:** K+P−/K−P+ framing, suppressor isolation and single-copy
   chromosomal reconstruction, the "balance was reset" passage, Fig. 3 osmoregulation assay
   description. `[primary-verified]`
6. **Gerken H., Charlson E.S., Cicirelli E.M., Kenney L.J. & Misra R.**, *MzrA: a novel modulator of
   the EnvZ/OmpR two-component regulon*, Mol Microbiol 72(6):1408–1422 (2009).
   DOI 10.1111/j.1365-2958.2009.06728.x; PMC2727453; PMID 19432797. **Read:** abstract conclusion on
   altering output but not signal reception, the osmolarity-response experiment (Fig. 2A), the R397L
   allele characterization and the ATPase turnover numbers. `[primary-verified]`
7. **Straube R.**, *Reciprocal regulation as a source of ultrasensitivity in two-component systems
   with a bifunctional sensor kinase*, PLoS Comput Biol 10(5):e1003614 (2014).
   DOI 10.1371/journal.pcbi.1003614; PMC4014401; PMID 24809699. **Read:** abstract, the
   Batchelor-Goulian concentration-robustness recapitulation, the NRII/NRI and PhoQ/PhoP reciprocal
   regulation passages, QSSA setup. `[primary-verified]`
8. **Anderson D.F., Enciso G.A. & Johnston M.D.**, *Stochastic analysis of biochemical reaction
   networks with absolute concentration robustness*, J R Soc Interface 11(93):20130943 (2014).
   DOI 10.1098/rsif.2013.0943; PMC3928931. **Read:** abstract/introduction — extinction result,
   quasi-stationary distribution, EnvZ/OmpR as motivating case. `[primary-verified]`
9. **Enciso G.A.**, *Transient absolute robustness in stochastic biochemical networks*, J R Soc
   Interface 13(121):20160475 (2016). DOI 10.1098/rsif.2016.0475; PMC5014071. **Read:**
   abstract/introduction — transient robustness, Poisson approximation. `[primary-verified]`
10. **Gao R. & Stock A.M.**, *Quantitative kinetic analyses of shutting off a two-component system*,
    mBio 8(3):e00412-17 (2017). DOI 10.1128/mBio.00412-17; PMC5433096;
    PMID 28512092. **Read:** abstract and framing — PhoR-PhoB, in vivo shutoff kinetics, reset to
    prestimulus levels by growth dilution. `[primary-verified]` **Relevance and its limit:** this is
    the closest published *dynamic* shutoff analysis for a bifunctional TCS, but it is PhoR-PhoB, not
    EnvZ/OmpR, and it measures deactivation after stimulus removal — not restoration of output after
    a perturbation to the output. It does not close the §3 gap.

## 13. Surprises

- **The open-loop result was not on my search list and is the biggest thing I did not expect.**
  Batchelor/Silhavy/Goulian 2004 deliberately tested for feedback from porin expression into the
  circuit and found none `[primary-verified]`. For a negative control this is almost too good — the
  system is model-free *and* the regulated output is not sensed — but it also undercuts "demonstrably
  corrects" in a way the brief did not anticipate. If prime's negative control must *correct*, the
  correcting variable has to be OmpR-P against a signal, not porin level against a need.
- **The P1 threat is genuinely live, and it comes with a clean non-mutational version.** I expected
  to find only rate-constant mutants where target-shift and machinery-damage are inseparable. MzrA
  dosage is a *trans*-acting intervention where the authors themselves certify that signal reception
  survives `[primary-verified]`. That is much closer to "competent misregulation" than I expected to
  find in an ACR system, and prime should not treat the state-vs-parameter distinction as
  automatically disposing of it.
- **The decisive experiment is missing from the literature.** Nobody appears to have run the
  Batchelor-Goulian titration assay in a shifted background to test whether the shifted level is
  *robustly* held. Every P1 conclusion here is limited by that absence.
- **The Science 2010 paywall cost less than expected** because the same authors' 2011 Math Biosci
  companion is open and contains the theorem and the worked EnvZ-OmpR network. Recorded in the
  ledger anyway, since the Science paper is what everyone cites and I did not read it.
