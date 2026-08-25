# AOP External Benchmark — Sporulation Perturbation Conditions (REDACTED)

**File:** `AOP_Benchmark_Sporulation_Conditions_REDACTED_v0.1.md` · **Version:** v0.1
**Date:** 25 July 2026 · **Produced by:** Claude Cowork (execution seat), under `TASK_CW_AOP_Benchmark_Records_20260725` §3.1
**Intended reader:** an **uncontaminated seat** — one that has not seen the sporulation ground truth. Input to `TASK_CLEANSEAT_AOP_Step0_20260725` §3.2.

---

## READ THIS FIRST

This file lists **perturbation conditions only**. Every outcome has been removed.

There are **no** spore titres, **no** frequencies, **no** fold-changes, **no** ratios, **no** detection limits, **no** qualitative characterisations of any genotype's behaviour, **no** direction of effect, and **no** ordering that encodes rank. The row order is a fixed structural convention (stated in §4) chosen precisely so that it carries no information about results.

**If you are the clean seat: nothing in this file tells you what any of these perturbations did.** That is the point. Do not attempt to infer outcomes from what is present or from what is absent; both were shaped by redaction, not by the data.

The producing seat has read the unredacted material. It produced this file *because* it already knows the answers — redacting cannot leak what the redactor is careful about. §6 is that seat's honest audit of what a reader can and cannot infer.

---

## 1. What is being perturbed

**Organism:** *Bacillus subtilis*.
**System:** the sporulation-initiation phosphorelay.

**Genes in scope for the scored set:**

- Relay core: **`spo0A`**, **`spo0F`**, **`spo0B`**
- Sporulation histidine kinases: **`kinA`**, **`kinB`**, **`kinC`**

**Genes explicitly out of scope for the scored set:** `kinD`, `kinE`. *The reason is withheld — it is outcome-derived.* Do not model them, and do not infer anything from their exclusion.

Naming the in-scope gene list is not an outcome disclosure: it states which perturbations were assayed, not what happened when they were.

---

## 2. Measured observable (stated so the build targets the right quantity)

The observable is **survival of a lethal heat challenge, measured as colony-forming units**: heat-resistant CFU per ml, and/or that count divided by the pre-heat-treatment viable-cell count per ml, and/or that ratio normalised to a wild-type control run in the same experiment.

Naming the observable discloses no result.

**Assay parameters, as published:**

- Heat challenge: **80 °C for 15 min** (primary source table below). Other conditions in the wider corpus use 80 °C/20 min or 75 °C/20 min; these are *not* interchangeable and numbers across protocols are not commensurable.
- Viable cells counted before heat treatment; spores counted after; both as CFU on Luria–Bertani plates.
- Samples serially diluted in minimal salts before plating.
- Sampling time: approximately **20 h after the end of exponential growth**.
- Growth temperature: **37 °C**.
- Cultures were grown for **at least four to five doublings after inoculation before entry into stationary phase**. Treat this as a required protocol condition, not an optional one.
- Chloroform-resistance readouts were not used in any source underlying this set.

---

## 3. Genetic backgrounds and allele identities

Perturbations in the source material are **specific named alleles**, not verified clean null deletions. A model build must decide explicitly how to treat each; the choice is the builder's, and it is not determined by anything in this file.

| Gene | Allele as published | Note on what the perturbation actually removes |
|---|---|---|
| `spo0A` | `spo0A9V` / `spo0A∆V` — **the allele label is corrupted in the source PDF text layer and has not been resolved against the printed page** | Identity unconfirmed |
| `spo0F` | `spo0F∆S` | Partial-deletion allele |
| `spo0B` | `spo0B∆Pst` | Partial-deletion allele |
| `kinA` | `kinA::Tn917` (insertion) | Insertional disruption |
| `kinB` | deletion–insertion **"deleting part of `kinB` and all of `kapB`"** | **This "single mutant" is formally a `kinB kapB` double mutant.** A model that represents KapB must account for this; a model that does not must record the assumption |
| `kinC` | `kinC::pLK124` (plasmid disruption) | Insertional disruption |

**Wild-type reference strain:** `JH642`.

**Strain designations appearing in the primary perturbation table:** JH642, AG522, NY120, JRL920, NY121, JRL1046, JRL1004, JRL1007. These are labels only; the mapping to genotype is given in §4 and carries no outcome information.

---

## 4. The perturbation grid

**Ordering convention — read before using the table.** Rows are ordered by (i) number of deleted/disrupted genes, ascending, then (ii) alphabetically by gene symbol. This is a fixed structural rule applied mechanically. **It encodes no rank, no magnitude, and no result.** Do not read the order as meaningful.

### 4.1 Kinase perturbation grid — full published design

Every genotype below was assayed in **every one of the three media**. The design is a complete crossing; no cell of the grid is missing, and no cell is emphasised.

| Strain | Genotype (genes disrupted) | Media assayed |
|---|---|---|
| JH642 | *none* — wild-type reference | 23SG · DS · Minimal |
| AG522 | `kinA` | 23SG · DS · Minimal |
| NY120 | `kinB` *(see §3 — also removes `kapB`)* | 23SG · DS · Minimal |
| JRL920 | `kinC` | 23SG · DS · Minimal |
| NY121 | `kinA` `kinB` | 23SG · DS · Minimal |
| JRL1046 | `kinA` `kinC` | 23SG · DS · Minimal |
| JRL1004 | `kinB` `kinC` | 23SG · DS · Minimal |
| JRL1007 | `kinA` `kinB` `kinC` | 23SG · DS · Minimal |

**Media definitions, as published:**

- **23SG** — a rich sporulation medium; nutrient broth plus 0.1% glucose.
- **DS** — the nutrient broth medium of Schaeffer et al.
- **Minimal** — S7 minimal medium, with glucose at 0.1% as the carbon source; sporulation induced by exhaustion of the glucose.

No higher-order kinase deletion beyond the triple exists in the source material for this observable.

### 4.2 Relay-core perturbation grid — full published design

Each genotype below was assayed under **two plasmid conditions**: carrying vector `pHP13`, and carrying `pLK2` (a plasmid supplying `kinC` at multicopy). The design is a complete crossing.

| Genotype (allele as published) | Plasmid conditions |
|---|---|
| *none* — wild-type reference (JH642) | pHP13 · pLK2 |
| `spo0A9V` / `spo0A∆V` *(label corrupted — see §3)* | pHP13 · pLK2 |
| `spo0B∆Pst` | pHP13 · pLK2 |
| `spo0E11` | pHP13 · pLK2 |
| `spo0F∆S` | pHP13 · pLK2 |
| `spo0J93` | pHP13 · pLK2 |
| `spo0K::erm` (deletion) | pHP13 · pLK2 |
| `kinA::Tn917` | pHP13 · pLK2 |

**Note on scope.** This table reproduces the *complete* published design of its source table, including genotypes (`spo0E`, `spo0J`, `spo0K`) that lie outside the in-scope gene list in §1. They are listed for design completeness and to avoid the emphasis that a filtered list would create. **Only the §1 in-scope genes belong to the scored set.**

---

## 5. Deliberately withheld

Stated openly, so the clean seat knows the shape of what it is not being given and does not mistake absence for non-existence:

1. **All outcomes.** Every number, direction, characterisation, and comparison.
2. **Which subset of §4 constitutes the scored set.** A superset is supplied on purpose. Naming the exact scored subset would itself signal which entries are informative.
3. **A second strain background.** An independent replication of *part* of the §4.1 design exists in a different *B. subtilis* strain background, under two further induction regimes, published by a different laboratory. Its conditions are withheld **because listing only the genotypes it covers would flag those genotypes as the interesting ones** — an emphasis leak, not an outcome leak. If the build requires them, request them from prime; they can be released without releasing any result.
4. **Every phosphatase and inhibitor arm** (`spo0E` as a phosphatase, `rapA`, `rapB`, `kipI`). No quantitative material for these was retrieved at all, so there is nothing to redact — but do not read their absence as a finding.
5. **The reason `kinD` and `kinE` are out of scope.**

---

## 6. Self-check — what an ignorant reader can and cannot infer

*Required by order §3.1. The producing seat re-read this file as though it knew nothing, and reports honestly.*

### 6.1 What a reader CAN infer

- The organism, the pathway, and the six in-scope gene symbols.
- That the observable is heat-resistant spore survival measured as CFU, and the exact assay parameters needed to reproduce the measurement conditions.
- The **complete experimental design**: which genotypes exist, in which media, under which plasmid conditions. This is by design — a model cannot be built against conditions it has not been told about.
- That the `kinB` allele is confounded with `kapB`, and that several alleles are not verified nulls. These are perturbation-definition facts, not results.
- That the kinase grid is fully crossed and includes singles, doubles, and one triple — i.e. that combinatorial data exists. **Knowing that a double mutant was assayed says nothing about how it behaved.**
- That `kinD` and `kinE` were excluded for a reason the file will not give.
- That a second-background replication exists somewhere.

### 6.2 What a reader CANNOT infer

- Any spore titre, frequency, ratio, fold-change, or detection limit for any genotype.
- Whether any single mutant is impaired, unimpaired, or enhanced relative to wild type.
- Whether any double or the triple differs from its component singles, in which direction, or by how much.
- Whether any perturbation is medium-dependent, or which medium is permissive for which genotype.
- Whether the relay-core perturbations differ in severity from the kinase perturbations.
- Whether the multicopy-`kinC` plasmid condition changed anything for any genotype.
- Which of the §4 rows are scored and which are not.
- Anything about `kinD` or `kinE`.

### 6.3 Residual inference risks — stated, not hidden

Three places where a determined reader could extract *something*, all judged sub-threshold but recorded so the judgement is auditable rather than assumed:

1. **The `pLK2` (multicopy `kinC`) arm.** Its existence tells a reader that someone thought it worth testing whether extra `kinC` changes the relay-core phenotypes. That is a fact about what was *asked*, not about what was *found*, and the direction of the answer is not recoverable — the experiment is equally publishable whether or not it worked. **Judged safe.**
2. **The triple mutant's existence.** That a `kinA kinB kinC` triple was constructed implies the doubles were not the end of the story. Again: a fact about the research programme, not about a result. **Judged safe.**
3. **Domain knowledge the clean seat already has.** Any competent microbiologist knows independently that `spo0A` is the sporulation master regulator and that relay-core mutants are stage-0 blocked. This file does not supply that; it also cannot un-supply it. **Not a leak from this file.** It is a limit on how "clean" any biologically literate seat can be, and the Step 0 design should account for it rather than assume it away.

### 6.4 Verdict

**A reader of this file cannot infer any result from the scored sporulation set.** The residual risks in §6.3 concern research-programme structure, not outcomes, and none of them yields a direction, a magnitude, or a ranking.

---

## 7. Provenance of the source material

The conditions above are transcribed from primary-source tables and methods sections retrieved and recorded in `AOP_Benchmark_PhaseA_Sporulation_*` (Drive `1y01p5w5mpKIVBoXkTXc-JxOqjUZoeSj4`). **Source citations are deliberately not printed here**: naming the papers would let a reader retrieve the unredacted tables in a single search and defeat the redaction entirely. Prime holds the citations and can release them once the clean seat's build is frozen.

**One transcription hazard carried forward** (it affects conditions, not outcomes): the source PDF's text layer mis-maps several glyphs, and one consequence is the corrupted `spo0A` allele label in §3. Any build that depends on the exact `spo0A` allele must resolve it against the printed page first.

---

*End of `AOP_Benchmark_Sporulation_Conditions_REDACTED_v0.1.md` v0.1. Produced by a contaminated seat; redaction integrity is the deliverable. Prime verifies by independent re-read, not by this seat's assurance.*
