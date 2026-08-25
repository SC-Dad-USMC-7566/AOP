# AOP External-Ground-Truth Benchmark — Design Specification (v1.0)

**Compiled:** 19 July 2026 by Claude (builder). Non-canonical working document.
**Status:** design frozen before any scoring was computed (see companion preregistration).
**Purpose:** Answer the open question prime and Ben identified after the §11b competence-check benchmark — build a benchmark whose ground truth is set *outside the modeler*, that AOP could actually fail.

---

## 1. Why the previous benchmark was not enough

The §11b leaky-autocatalytic-compartment benchmark is a **competence check**: the redundancy/synergy/inert/load-bearing structure, and therefore the strength-vs-viability anti-ranking and the Möbius sign pattern, are *built in* by the gate topology and rate assignments (swap the OR/AND wiring and the signs flip). It shows the method **recovers** designed structure that a single-axis reading inverts — but because the modeler set the answer, it cannot *fail* in a way that is informative about the world.

This benchmark removes that circularity by taking the answer key from an **independent experiment**.

## 2. The system

**E. coli core carbon metabolism** (`e_coli_core`; Orth, Fleming & Palsson 2010, *EcoSal Plus*). 95 reactions, 137 genes, 72 metabolites. Ships offline in cobrapy, so the whole benchmark is reproducible with no network dependency. Wild-type FBA biomass flux on glucose minimal medium (aerobic) = 0.8739 h⁻¹.

Frozen model: `MODEL_e_coli_core.xml` (SBML, MD5 `2fd9c214652195707526448954b88696`).

## 3. The AOP reading (what the framework computes)

| AOP construct | Metabolic instantiation |
|---|---|
| Viability functional **V** | FBA biomass flux (growth rate), the system's own present-tense viability |
| Viable set | flux polytope under the stoichiometric + medium constraints |
| Mechanism | a gene, mapped to reactions through the model's gene–protein–reaction (GPR) rules |
| Viability importance **ΔV(gene)** | biomass drop when the gene (and its GPR-forced reactions) is knocked out |
| Coalition / semantic layer | double-gene knockout; Möbius interaction h(g₁,g₂) = ΔV(g₁,g₂) − ΔV(g₁) − ΔV(g₂) |
| Synthetic-lethal coalition | pair with ΔV(g₁)=ΔV(g₂)=0 but ΔV(g₁,g₂) large (both dispensable alone, jointly essential) — the real-metabolism instance of the toy benchmark's redundant coalition |

## 4. The external answer key (what the framework is scored against)

**Experimental gene fitness on glucose minimal medium**, Price et al. 2018, *Nature* 557:503–509 (RB-TnSeq on *E. coli* BW25113, the Keio-collection parent). Retrieved from GitHub mirror `dbernste/E_coli_GEM_validation`. Frozen as `EXT_KEY_price2018_fitness_Keio_BW25113.tsv` (MD5 `936b99da2cbf37baa70a2b2e1b629c93`); provenance in `EXT_KEY_provenance.md`.

This key is external in the strict sense the task requires: the Arkin/Deutschbauer lab measured which genes a growing cell actually needs, with no reference to AOP or to this project. The modeler did not choose the answer.

**Binary essentiality label** (fixed in the preregistration before scoring): a core gene is labelled *experimentally-required* if it is **absent from the RB-TnSeq assay** (too few insertions to sample — the standard essential-gene signature) **and** FBA-lethal, OR present with strongly negative glucose fitness (threshold fixed in prereg). All other core genes are *dispensable*. Ambiguous cases (absent-from-assay but FBA-viable) are quarantined and reported separately, not scored.

## 5. The named rival (single-axis comparator)

**Structural coupling strength** = summed |wild-type flux| through the reactions a gene controls. This is a viability-blind, single-axis reading: it asks how much material moves through a mechanism, not whether removing it ends the system. Scored on the *same* model and answer key with its own definition, comparison fixed in advance.

## 6. What makes this able to fail

The §11b benchmark's dissociation was forced. Here it is an empirical question with a real risk of going against AOP:

- On real central metabolism, the highest-flux genes (glycolysis, ATP synthase) are frequently **also essential**. If flux magnitude tracks essentiality, the rival will match or beat AOP and the toy-model "strength ⊥ viability" dissociation will **not** generalize — a reportable failure of external validity.
- FBA gene-essentiality is a known ~0.85-accurate method, but it is not perfect; ΔV may under- or over-call against the experimental key.
- The coalition claim needs at least one genuine FBA synthetic-lethal pair in the core model; if none exists, the coalition layer has nothing to recover here.

Each of these is written as an explicit falsifier in the preregistration.

## 7. Deliverables

Design spec (this doc); frozen preregistration; self-contained code with fixed seeds; results; figures; plain-language pass/fail summary. All on Drive.
