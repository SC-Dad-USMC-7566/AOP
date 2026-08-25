# Gate 1, Step B — Candidate longlist, before retrieval

**Seat:** Claude Science (builder). **Date:** 2 August 2026.
**Status:** Records file. A longlist is not a shortlist and not a selection. Entries are here to be
scored, including entries this seat expects to reject.

**Contamination bookkeeping.** The five systems rejected for the external benchmark are
*B. subtilis* sporulation, yeast HOG, yeast GAL, *E. coli* DNA repair, and phage λ. Per the order,
no benchmark rejection is grounds for rejection here. Sporulation is reserved outright by Ben's
§0(a) ruling. For the other four, selecting one costs this seat's availability to the benchmark,
and that cost is priced per entry below rather than assumed fatal.

**A.1.9 is not applied.** It is a benchmark heuristic about redundant architecture, graded frontier
on five observations, and this arc does not require redundancy.

---

## Class 1 — Integral-feedback regulators (slow variable integrates the regulation error)

| # | Candidate | On the list because | Contamination |
|---|---|---|---|
| 1 | ***E. coli* chemotactic adaptation, receptor methylation (CheR/CheB)** | Prime's lead. Best-characterised robust-adaptation system in biology; quantitative dynamical models, single-cell FRET readouts, expression-level control of the slow arm. Eligible only under Reading B. | Clean |
| 2 | **Synthetic antithetic integral feedback controller** | The cleanest realisation of integral feedback with full parameter access. Prime assigns engineered systems to the negative control; an *integral* controller is the wrong shape for that, so it enters here as a positive-article candidate and is expected to fail on viability-relevance. | Clean |
| 3 | **Yeast HOG osmoadaptation** | Carries integral-like adaptation with a genuine survival readout. Listed for completeness because the benchmark rejection does not transfer. | **Contaminated** — cowork has read this literature |

## Class 2 — Autonomous slow reference (slow variable not driven by the regulated coordinates)

| # | Candidate | On the list because | Contamination |
|---|---|---|---|
| 4 | **Cyanobacterial KaiABC circadian clock (*Synechococcus elongatus*)** | The only candidate this seat can name whose slow variable's autonomy is *experimentally demonstrated rather than modelled* — the oscillator runs reconstituted in vitro from three proteins and ATP, with no transcriptional output to be driven by. Phase is a state, not a parameter. Period is genetically tunable; phase is resettable. Carries a fitness observable with a matched comparison class. Eligible under Reading A **and** B. | Clean |
| 5 | ***B. subtilis* sporulation phosphorelay** | Would otherwise be scored. **Excluded by Ben's §0(a) ruling, not by any S-criterion.** Recorded so the exclusion is visibly a ruling. | Reserved |
| 6 | **Bacteriophage λ lysis–lysogeny bistable switch** | A stored discrete state. Enters to be scored on whether a bistable memory is a *reference for regulation* or merely a state. | **Contaminated** |
| 7 | **Mammalian/*Drosophila* circadian clock** | Same architecture as #4 with a richer physiology and far worse intervention access. Enters to be scored and expected to fail S.1/S.4. | Clean |

## Class 3 — Robust set-point systems where the target is fixed by rate constants (negative-control candidates)

| # | Candidate | On the list because | Contamination |
|---|---|---|---|
| 8 | **EnvZ/OmpR bifunctional two-component system (*E. coli*)** | Leading negative control. Demonstrably corrects; robustness of the output level is attributed to the bifunctional enzyme architecture, i.e. the target sits in the rate constants with no slow reference to move. Same organism as #1, so a strong match. Fully interventable. | Clean |
| 9 | **NRI/NRII (NtrB/NtrC) nitrogen regulation** | Same bifunctional architecture; backup negative control if #8 fails. | Clean |
| 10 | ***E. coli* heat-shock regulation by chaperone titration (σ32)** | Prime's #2, listed as a positive candidate. This seat expects it to score as a **negative control** instead: if the target is emergent from titration kinetics it is model-free by S.2, which is a better use for it. Strongest S.5 of any candidate (survival at elevated temperature). | Clean |

## Class 4 — Engineered / reconstituted correctors with the target baked into kinetics (§3's stated shape)

| # | Candidate | On the list because | Contamination |
|---|---|---|---|
| 11 | **Synthetic negative autoregulation (single gene, self-repressing)** | Corrects toward a level set entirely by its own kinetic constants; no reference state exists to move. Complete intervention access. The §3 shape, in its minimal form. | Clean |
| 12 | **End-product feedback inhibition in an amino-acid biosynthesis operon** | Native model-free corrector with a metabolic readout; alternative to #11 if a native negative control is preferred over an engineered one. | Clean |

## Class 5 — Mammalian set-point physiology

| # | Candidate | On the list because | Contamination |
|---|---|---|---|
| 13 | **Hypothalamic thermoregulation / fever** | Prime's #3, and prime is right that it is the cleanest *conceptual* instance of P1. Scored because it sharpens what P1 asks for, expected to fail S.1 and S.4, and expensive. | Clean |
| 14 | **Body-weight / adiposity regulation (leptin)** | The literature where the stored-set-point-versus-settling-point dispute is actually argued. Scored partly for that literature's own sake — see the set-point/settling-point retrieval track. | Clean |

## Ineligible on the face of the order

| Candidate | Why |
|---|---|
| **Genome-scale flux-balance models** | S.1 explicitly: "Flux-balance models remain parked and are not eligible." |
| **Any structure-only / wiring-diagram-only system** | S.1: rejected at that line. |
| **AOP's canonical star** | The order says so: it cannot be intervened on. Retained only as the conceptual reference for what a model-free corrector is. |

---

## Candidate pairings this longlist makes available

Recorded now so that the pair is chosen by the scoring rather than assembled after it.

- **Pair I — #1 chemotaxis (positive) / #8 EnvZ-OmpR (negative).** Best *match*: same organism,
  both phosphorylation-based stimulus-response regulators, comparable intervention classes and
  model maturity. Requires **Reading B**; dies under Reading A.
- **Pair II — #4 KaiABC (positive) / #8 or #11 (negative).** Survives **both readings** and has the
  only strong S.5 on the positive side. Match is weaker: the negative control is a different
  organism (#8) or a synthetic construct (#11).
- **Pair III — #2 antithetic controller (positive) / #11 negative autoregulation (negative).**
  Best possible match — same chassis, same plant, same readout, architecture the only difference —
  and expected to fail because a synthetic controller regulating a reporter holds no reference to
  *its own viable set*, which is component (5) of the criterion.

The trade-off is visible and it is real: **the best-matched pairs are the least eligible, and the
most eligible pair is the least well matched.** Retrieval decides which side of that to take.

---

*End of longlist. No candidate scored. No AOP quantity computed. Not self-certified.*
