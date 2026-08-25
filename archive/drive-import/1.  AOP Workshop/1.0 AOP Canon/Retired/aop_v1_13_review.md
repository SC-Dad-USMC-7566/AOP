# Hard review — proposed canon update v1.13 (life threshold + diachronic individuation)

**Reviewer:** AOP session, 9 July 2026. **Governing:** Charter v1.0; Canon v1.12 (live).
**Source reviewed:** Drive file `1C8hTjpJwL_xtjdRH7f26E1g12MBJR004` = `aop_canon_v1_13.md` (integration
draft, new/changed blocks only, 4519 words). **Method:** every load-bearing citation checked against the
primary source or the Crossref record; scope-wall and refusal integrity assessed against the charter.

## Bottom line
**Strong draft — accept with revisions, not as-is.** The architecture is right, the grading is honest,
the scope discipline is genuinely good (the head-of-paper "life" caveat and the ⚠ reference flags are
exactly what the charter asks), and the diachronic-individuation half is the stronger of the two. But
there is **one load-bearing citation misuse** that must be fixed before this enters canon, **one
misquotation** of the definition it builds on, and a handful of smaller items. None sink the fold; all
are fixable in text.

## What I verified against primary sources
- **Chodasewicz 2013** (full text read): the draft's use is **correct**. He states the "mule's problem"
  as a *criticism* of the Darwinian definition and rebuts it at the population level ("an object cannot
  be accounted as a living or non-living one without a broader population perspective"). The draft's
  parenthetical — that even the rebuttal concedes the *individual* mule is not the unit of evolution — is
  faithful.
- **Cleland & Chyba 2002** (full text read): confirms the "Darwinian definition" and attributes the
  "careful formulation" to Joyce 1994. **But the exact wording is "a self-sustain*ed* chemical system
  capable of undergoing Darwinian evolution"** — the draft repeatedly writes "self-sustain*ing*," inside
  quotation marks. Misquotation of the very definition the section is built against. **Fix required.**
- **Reference DOIs** (Crossref-verified, 9 of the new entries): all resolve with correct title, authors,
  year, venue — Conant & Ashby 1970, Francis & Wonham 1976, Bich et al. 2015 (4 authors), Varela-Maturana-
  Uribe 1974, DiFrisco 2018 ("Biological Processes," *Everything Flows*), Bernstein et al. 1985 (4
  authors), Otto 2009, Muller 1964. The bibliographic layer is clean.
- **Good regulator theorem** (Conant & Ashby 1970; primary PDF paywalled/WAF-blocked, so verified via
  the theorem's standard statement across multiple independent expositions): the *optimality-and-simplicity*
  caveat the draft relies on is **real** — "good" means the regulator is both optimal and maximally
  simple, and only such a regulator is provably a (homomorphic-image) model. So the draft's reference
  note is right about the caveat. **The problem is one level up — see Finding 1.**

## Finding 1 — LOAD-BEARING: the Conant–Ashby citation is used backwards, and for the wrong "model"
The §11a discriminator hinges on this sentence:
> "a good regulator need not carry a model, and the ones that do not are simply the non-optimal or
> unnecessarily complex ones [Conant & Ashby 1970] — a bare stable fixed point is not thereby a model."

Two things are wrong with leaning on Conant–Ashby here:
1. **Direction.** The theorem says: *among optimal regulators, the maximally simple one is (homomorphic
   to) a model.* It does **not** classify model-free regulators as "the non-optimal or unnecessarily
   complex ones." That inverts the result — the theorem is a statement about what optimal-simple
   regulators *must* be, not a taxonomy of the regulators that aren't models.
2. **Wrong notion of "model."** Conant–Ashby's "model" is a **homomorphic image** — a weak notion under
   which a bare fixed point, even an identity map, *does* count as a "model" of the system. That is the
   opposite of what §11a needs, which is a **decoupled, separately-interventable stored reference**. So
   Conant–Ashby, read correctly, would if anything let the star count as carrying a "model" — exactly the
   conclusion §11a is trying to deny.

**The distinction §11a actually wants is sound — but its support is Francis–Wonham + Bich et al., not
Conant–Ashby.** The internal model principle (Francis & Wonham 1976) and the organizational-regulation
account (Bich et al. 2015) are what distinguish a *stored, dynamically-separable* set-point from a fixed
point baked into the constitutive dynamics. **Fix:** demote Conant–Ashby from the load-bearing citation
to at most a historical mention, and rest the continue / correct-model-free / correct-model-based
distinction on Francis–Wonham (decoupled internal model) and Bich et al. (separable regulatory
sub-system). The star-is-not-alive result then stands on the right foundation: the star's set-point is
not *separately interventable*, which is a Francis–Wonham/Bich point, not a good-regulator-theorem point.
This is the single change I'd hold the fold for.

## Finding 2 — the "self-sustaining" vs "self-sustained" misquotation (fix required, mechanical)
Every quoted instance of the NASA/Joyce definition should read "self-sustain**ed** chemical system
capable of undergoing Darwinian evolution" (Cleland & Chyba's rendering of Joyce). The draft's paraphrase
clause ("keeps the self-sustaining clause") is fine as paraphrase; only the **quoted** form must match.
Also: the draft calls it "the NASA Exobiology working definition." Cleland & Chyba call it the "chemical
Darwinian" definition and credit Joyce's formulation; the "NASA working definition" label is a common
secondary attribution but is not how the primary source frames it. Recommend: quote it as the Joyce/
"chemical Darwinian" formulation and note the NASA-working-group provenance as secondary — which is
roughly what the ⚠ Joyce flag already anticipates.

## Finding 3 — Figure LT is honestly labelled but the honesty should be louder
The draft correctly says Figure LT is "a demonstration of self-consistency, not a test that could fail —
the model edge is load-bearing by construction." Good — this is the same posture as Figure MW and it is
stated. My only push: because "we defined *alive*, then built two systems where our definition separates
them" is exactly the shape a skeptic will attack, the non-falsifiability should sit in the **figure
caption and the Table 3 row**, not only in the body. The draft *mostly* does this (Table 3 row says "a
demonstration of self-consistency, not a falsifiable test") — so this is a nudge, not a defect. The
computation itself (mask-weight × generator-spectrum, twentyfold vs twofold separation) is in the
framework's established idiom and is the right way to make it concrete. **I have not re-run the deposited
Figure LT code** — it was not attached; before final master, the OU computation should be reproduced the
way the individuation gate was.

## Finding 4 — diachronic individuation (§4a) is the strong half; one caution
The genidentity / continuity-of-instantiation criterion is a genuine settled position (process biology;
DiFrisco 2018 chapter title Crossref-confirmed) and the transporter-vs-Theseus contrast is a clean way to
fix it. The Parfit citations are correctly scoped in the draft's own note ("cited for the thought
experiments and the 'no further fact' reading, not for a claim that a copy is determinately not the
original") — this is the right, careful use. **Caution:** DiFrisco's in-chapter terminology
(genidentity / causal cohesion / perdurance) and pagination are flagged ⚠ *unverified* by the draft
itself, and the §4a text uses "genidentity" as though sourced to him. Either verify the term appears in
his chapter, or attribute "genidentity" to its actual origin (Lewin/Reichenbach lineage) and cite
DiFrisco for the process-identity criterion in his own words. Do not quote him until the chapter is read.

## Finding 5 — scope-wall integrity (§9 clarification + Insert G): clean
The §9 clarification does **not** modify the present-tense principle (confirmed — it adds a paragraph
beneath it), and it correctly keeps *future continuation* above AOP as a Ladder propagation-bus item.
This is the charter-critical boundary and the draft respects it. The recombination frontier note
(Insert G) is properly dated, marked removable, and explicitly placed above the scope wall — this is
model behavior for a frontier note, not a defect. Muller 1964, Bernstein et al. 1985, and
Otto 2009 Crossref-verify; Felsenstein 1974 (doi:10.1093/genetics/78.2.737, *Genetics* 78(2):737)
Crossref-verified on re-check.

## Finding 6 — refusal integrity: clean, and this is the highest-risk edit
Insert A states both halves together: "alive" is a structural property of a coupling architecture, read
by the third-person mask, individuating nothing by an ownership scalar; the homunculus stays contained
(§7). This is exactly the safeguard the individuation fold needed and it is done correctly — the refusals
are *narrowed nowhere*; a structural category is added and explicitly fenced off from "metaphysics of
selfhood or worth." No concern.

## Smaller items
- "Death is not a fifth erasure" and "spore = life paused" are clean synthesis and follow from the axes;
  no citation risk.
- The changelog is accurate and complete, and it front-loads the primary-source corrections — good
  practice.
- ⚠ items the draft itself flags (Joyce 1994 foreword text unread; DiFrisco pagination/terms; Ashby 1960
  pagination) are correctly held as pending; none should be quoted until read. Agreed.
- Grade tags are present on every block and are calibrated correctly (frontier for the definition of
  alive; settled for the control-theory antecedents; synthesis for the mappings). This is charter-honest.

## Recommendation
Accept the fold **after** three changes: (1) **Finding 1** — re-base the §11a discriminator on
Francis–Wonham + Bich, demote Conant–Ashby to historical mention (hold the fold for this one); (2)
**Finding 2** — fix the "self-sustained" quotation and soften the "NASA working definition" label to
secondary attribution; (3) **Finding 4** — do not use "genidentity" as DiFrisco's word until the chapter
is read, or reattribute. Findings 3/5/6 are nudges or already-clean. Before the assembled master ships,
reproduce the Figure LT OU computation (not attached here) the way the individuation gate was
reproduced. The diachronic half is close to ready; the living-threshold half needs the citation
re-basing to be defensible under review.
