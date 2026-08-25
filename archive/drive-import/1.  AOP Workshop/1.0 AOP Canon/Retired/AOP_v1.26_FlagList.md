# Flag list — AOP v1.26 red-team remediation

**From:** Claude Cowork (execution seat)
**To:** Prime (verification) and Ben (decision)
**Date:** 25 July 2026
**Companion to:** `AOP_ChangeSet_v1.25_to_v1.26_RedTeamRemediation.md`

Nine flags. Four are decisions the order explicitly reserved (F-1, F-4, F-8, and the retrieval residuals F-5). Four are places I departed from the literal instruction and am reporting rather than absorbing (F-2, F-3, F-6, F-7). One is a downstream consequence nobody asked about but that follows from the cuts (F-9).

I did not stop mid-build on any of these, because none of them blocked a specified edit. Each is reversible.

---

## F-1 — Joyce 1994 foreword: unretrieved, and the need may have vanished
**Raised by:** Task 4, which said to flag and not attempt retrieval.
**Status:** flagged; retrieval *was* attempted anyway as part of the parallel retrieval deliverable, and failed.

The foreword is not retrievable. The book exists on Internet Archive but is access-restricted (print-disabled / in-library, no search-inside), and no route reached the text. The page attribution "pp. xi–xii" is corroborated by three independent secondary reference lists; the wording varies between secondary sources ("self-sustained" vs "self-sustaining"); and one secondary source (Mix 2026, *Astrobiology*) attributes the definition to NASA's Exobiology Discipline Working Group rather than to Joyce personally, while another (PMC10392681) mis-cites it as "Joyce et al." with the editors as co-authors.

**The order anticipated correctly: the need has largely vanished from the core.** With the life block relocated (Task 19), the core paper no longer makes the NASA-definition comparison and no longer cites Joyce. The citation now lives only in the follow-on, where §1 carries an explicit source-status note saying the primary was not retrieved and that a secondary quotation is not primary verification.

**Decision needed:** whether the follow-on may cite it at all on secondary evidence. My recommendation is that it may, given the explicit note — but that is Ben's call, and the alternative (cite Cleland & Chyba 2002 directly for the formulation, and drop the Joyce attribution to a parenthetical) is clean and costs nothing.

---

## F-2 — Task 11.2 was already done in v1.25
**Type:** finding. The order asked for something that existed.

Task 11 part 2 said to "add **reversal convention** as an explicit slot in the declaration tuple **D**." It was already there. v1.25's §12″ reads:

> D = (S, E, F, P, δt, τ, **R**, V, I, N): the system variables, environment, interface, partition, time grain, horizon, **reversal convention**, viability functional, intervention class, and normalization.

The slot existed and was **inert** — no passage anywhere in v1.25 referenced R, and no reported quantity declared it. So the order's diagnosis was right even though its remedy was already formally satisfied.

**What I did instead of adding it:** made it load-bearing. §12″ now carries a block calling out R (with V and I) and wiring R explicitly to the D→M fourth scope condition — an entropy production reported without R has not said which involution it is a divergence against, and a memory floor derived from it inherits that gap. Table 1's Drive row names R directly. §2's rewritten paragraph makes the same point.

**Nothing to decide** unless Prime wants the wording changed. Reported because the order's Task 7 note ("the reversal convention this exposes is added to **D** there") reads as though Prime believed it was absent.

---

## F-3 — I did not sweep the historical changelog
**Type:** departure from the literal instruction. **Please rule on this.**

Tasks 14 and 19a both say to sweep "every echo in the version history." I did not, and I think sweeping it would be a mistake.

The changelog is the record of *what earlier versions said*. Editing the v1.14 entry so that it no longer says the paper "adds a graded, frontier definition of *alive*" would make the record false: v1.14 did say that. Same for renaming Φ_MIP inside the v1.12 entry that introduced it under that name. It would also conflict with Task 0, which specifies that the v1.26 master "inherits everything: masthead, changelog, gate ledgers, retraction history, verification notes."

**What I did:** swept the entire live body, all tables, both claim ledgers, the gate ledger row, Data Accessibility, and the reference list. Left v1.25 lines 836–997 byte-identical. The v1.26 changelog entry states the rename and the relocation explicitly, so a reader moving through the history is told what changed and when.

**The masthead is the edge case.** The masthead's long summary line is *also* historical — it recaps every prior version — and it contains phrases the sweep would otherwise catch ("Figure LT," "§4a," "virion," "transporter"). I prepended the v1.26 summary and left the historical remainder intact, on the same reasoning.

**If Prime disagrees**, the fix is mechanical and I can apply it in one pass — but I'd want the instruction to be explicit that the historical record is being rewritten, because that is what it amounts to.

---

## F-4 — Bounding-principle status: "screenability" narrowed, "rest mass" gone
**Raised by:** Task 18, which said to flag for Ben and not decide.

Two entries on the informal bounding-principle list change as a direct consequence of the physics-block cut:

- **"Screenability"** survives only in the narrowed §8 form: *a physical interface can be passive or actively maintained, and screenable interactions make passive interfaces cheap.* It no longer supports the claims that electromagnetic screening uniquely makes statistical boundaries, that the strong and weak interactions are disqualified from individuation, or that unscreened gravity implies the absence of a statistical boundary.
- **"Rest mass as the price of persistence"** does **not** survive in any form as a domain criterion. It is replaced by the operational scope condition of §10.

I have recorded this in §13 and in Table 3's domain row, both marked as flagged-not-decided. **The bounding-principle list itself is not in the canon file and I did not have it, so I could not update it.** Ben should confirm the list is updated wherever it lives.

---

## F-5 — Two retrieval findings bear on claims in this build, and neither is line-checked
**Type:** evidence status. **Do not rely on these until Prime reads the sources.**

The parallel retrieval deliverable turned up two findings that support edits made here. I deliberately did **not** assert either in canon as a verified fact; both are marked as retrieved-not-line-checked.

**(a) Aguilera & Di Paolo — bears on Task 14.2.** The retrieval reports that their construction is a kinetic Ising model with φ defined as a divergence between time-lagged conditionals, not a static covariance object, and that "Gaussian" and "covariance" do not appear. If confirmed, this strongly supports the order's instruction to treat AOP's static-Gaussian min-cut as an AOP construction rather than their measure imported. The bibliographic record checks out exactly (Neural Networks 114, 136–146, 2019, DOI 10.1016/j.neunet.2019.03.001).

**(b) Kolchinsky & Wolpert — bears on Task 20a.** Every intervention the retrieval could quote acts on the system–environment channel, with the on-point line that interventions "only perturb the information flow from the environment to the system, and not vice versa." This supports the order's instruction that internal-edge intervention is an unlicensed extension.

**Why I am not treating either as settled.** Both are *absence* claims — "their measure is not defined on X," "they nowhere license Y" — and both came through WebFetch's summarizing layer rather than direct transcription. Two fetches of the same PMC page disagreed on a single word, which is direct evidence of drift. An absence claim from a summarizer is the weakest thing such a tool can certify. Positive evidence points the same way in both cases, but neither is verified.

**Also material for Prime:**
- **Francis & Wonham 1976 was NOT retrieved.** Paywalled on every route. The bibliographic record is verified against Wonham's own publication list (entry J34), but no part of the paper was read, and the theorem's actual scope conditions are unverified. The follow-on says so explicitly in §3 and in its reference entry. This matters because the follow-on's Task 19b relabelling rests on what the theorem does and does not say.
- **Bich et al. was read in full**, and the decoupling requirement is there as a numbered condition. Two caveats: the retrieved copy is the 2015 online-first version against the 2016 print citation, and its page numbers are manuscript pages, not the journal's 237–265 range.
- **A citation conflation was found and is now flagged in the reference list.** "Ford & Spinney (2012), *Entropy production in full phase space for continuous stochastic dynamics*, PRE 85, 051113" pairs one author order with the other paper's title. There are two distinct 2012 PRE papers with opposite author order (Spinney & Ford, PRE 85, 051113; Ford & Spinney, PRE 86, 021127). Both are now cited correctly and the conflation is named in the entry. Note also an unretrieved Publisher's Note at PRL 108, 199905 whose content is unknown.
- **Crutchfield et al.: one correction.** The paper does **not** state "E ≤ Cμ." It states Cμ = E + χ; the inequality follows from χ ≥ 0. The canon's existing wording (χ = Cμ − E) is consistent and was not changed. The paper also contains **no** explicit warning against reading Cμ as material complexity — that framing in Task 9 is AOP's own inference from the definitional structure (a process as a communication channel over measurement outcomes), and I have written it as AOP's statement rather than as a cited one.

---

## F-6 — The head-of-paper "life" note was moved, not softened
**Type:** departure, larger than the literal instruction. **Please confirm.**

Task 19a says to "remove the explicit 'new definition, graded frontier' posture (line ~33 and every echo)." Taken literally that is a phrase-level edit to a note that stays in the core.

I moved the whole note to the follow-on and left nothing in its place. The reason: the note opens *"This paper uses alive in a specific and deliberately frontier sense."* Once the core names nothing *alive* — which is exactly what 19a requires — that sentence is false on its face, and so is the rest of the note, which is entirely about how the paper's *alive* relates to the NASA definition. A head-of-paper note explaining a term the paper no longer uses would be worse than either keeping it or removing it.

**In the follow-on**, the note is retained in full with the de-announcement applied: it now says the criterion "differs on purpose," and a short paragraph states that the "new definition, graded frontier" announcement is withdrawn because it promised more than the work supports.

**If Ben wants a note in the core**, the natural replacement is one sentence in §11a saying the architecture is deliberately not being named and pointing at the follow-on — which the §11a pointer paragraph already does.

---

## F-7 — One item moved into the core rather than out of it
**Type:** placement decision the order did not cover.

v1.25 line 511, inside §11a, computes the **semantic weight of the memory-bearing edge**: scrambling the cell-type system's slow-reference readout drops a present-tense viability functional by [0.45, 0.80] across three viability choices, versus exactly 0 for an inert spectator, with the weight inverting where the remembered set-point is noisier than the tolerance.

That is a **Memory-axis** result, not a life claim. Moving it to the follow-on with the rest of §11a would have cost the core a deposited computed number about when a memory edge earns semantic weight.

I relocated it **into the core at §5**, immediately after the E(T) retention-depth paragraph — which already describes the same cell-type and star-type OU systems, so it lands without needing the model re-introduced. I trimmed the clause tying it to Figure LT-T's model-edge range (that figure moved) and added a parenthetical noting that the regulatory-architecture reading of the same two systems is developed in the follow-on.

**Reversible either way.** If Prime prefers it travel with §11a, say so and I'll move it.

---

## F-8 — Life-block timing: I took the default (move now)
**Raised by:** Task 19's sequencing flag, which left open whether the move happens now or after the benchmark, with "move now" as the stated default.

I moved it now. It de-risks the core immediately, as the order says, and the alternative — holding it — would have left the core carrying the "new definition" posture that Task 19a removes, which is incoherent with the rest of the build.

**If Ben wants it held**, this is the single largest reversal in the build and it is clean: restore v1.25 lines 22–41 (head-of-paper note), 193–242 (§4a), 443–574 (§11a), and 397–412 (§9a collective question), then re-apply Tasks 5, 16, 17, 19a–c in place. I have all four blocks preserved verbatim in the extraction files. Say the word and I'll do it.

---

## F-9 — A consequence of the cuts nobody flagged: the settled core is now one row
**Type:** downstream consequence. Not a request; make sure it is intended.

Cutting the physics block (Task 18) removes "Screenability & the causal boundary — forced × definition/stipulated-weld (standard EM + GR)" from Table 3′. That row was one of the two the ledger called "the framework's hard floor."

**After this build, exactly one row is forced × theorem/corollary: the σ>0 ⇒ E>0 direction** — and that one now carries four scope conditions rather than three (Task 11).

I have written this into §12′'s "Reading the ledger" and §13's exposure list explicitly, rather than letting the ledger quietly shrink. It is the honest outcome and I am not arguing against it. But it is worth Ben seeing it stated plainly: **the paper is more honest and thinner in the same move**, and a referee will notice that the settled core of a synthesis paper is a single corollary. The taxonomic argument (§13: a carving is justified by the distinctions it refuses to lose) is now carrying proportionally more of the paper's weight than it was, and the external benchmark — deferred by this order — is the thing that would change that.

---

## Nothing I had to stop on

No specified edit turned out to contradict the canon or to be under-specified past the point of execution. The four departures above are reported, not improvised fixes to scientific judgment. Every task in the order is dispositioned in the changeset, and the two deferred items (external benchmark; primary-source folding) were not attempted — retrieval was performed and deposited, but nothing from it was folded into canon as a claim.

**Do not treat this build as verified.** It is a proposal from the seat that produced it.
