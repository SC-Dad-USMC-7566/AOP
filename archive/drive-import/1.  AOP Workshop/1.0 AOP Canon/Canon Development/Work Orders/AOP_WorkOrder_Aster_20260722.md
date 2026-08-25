# AOP — Work Order for Aster (outside critic)

**Issued by:** Prime (chat seat), 22 July 2026.
**Status:** v1.22 fold **HELD**. Live master `AOP_CANON_MASTER_v1.21.md` untouched.
**Your role:** break this. You are not being asked to approve a fold, propose replacement prose, or
build anything. You are being asked to find what is wrong.

---

## Why this order exists

You already ran the Q1/Q2 critic pass and returned exit (b) on both — §4 under-scoped, Figure MW
propagation incomplete. Cowork implemented repairs; Prime checked them and sent four back. Three came
back correct.

The fourth did not, and the failure is the reason you are being called again. Prime asserted from
memory that a question about the semantic mask was unresolved. Cowork wrote that assertion into
proposed canon prose as the stated reason for shelving a result, then asked Prime to confirm it. Nobody
opened the source document. When Prime finally did, the source said the opposite: the question had been
answered on 21 July and independently verified.

**Treat that as the operating assumption for this pass: statements in the decision package and the
verdict response are unsourced until you find the document that establishes them.** Two claims moved
from summary into a fold decision today without a source underneath. Assume there are more.

---

## Task 1 — PRIMARY. Attack the mask-salvage result itself.

**The claim under attack.** `AOP_MaskSalvage_VERIFICATION_memo_20260721.md` reports that on Model 3
the salvageable region — the intersection of the mask's *well-defined* region and its *informative*
region — is non-empty and non-trivial, reproduced on fresh re-run with a from-scratch re-derivation of
primitives matching to six digits. Headline numbers: merge point a\* ≈ 3.3–3.4, Ω ≈ 0.81, on a
static-Gaussian K4 system with S = {0,1}. Graded SYNTHESIS, CONFIRMED.

**The question.** Could that intersection have come out empty?

This project has now produced three separate results that were written up as findings and turned out
to be forced by construction: the v1.18 benchmark's Möbius sign inversion (forced by gate topology),
the §13 embarrassment condition (a theorem of positive-definite linear algebra, not a contingent
claim), and Figure MW (proxy sensitivities read as causal necessity — your own Q2). A fourth is the
default hypothesis, not a suspicion.

Probe at least these:

1. **Is non-emptiness structural?** Does the K4 topology with S = {0,1} guarantee a non-empty
   well-defined ∩ informative intersection at *any* coupling, for the definitions actually used? If it
   does, the result is a demonstration of self-consistency and must be graded as one.
2. **Is "salvageable" falsifiable as defined?** Identify the predicate. Construct, or show the
   impossibility of constructing, a system in the same class where it fails.
3. **Which coalition set is honest?** The memo reports that the a\* ceiling exists under the full
   min–max interval and at coalition cardinality ≥ 3, and **vanishes entirely** under a small-coalition
   reading (|C| ≤ 2, or sparse sampling) — at which point the mask reads salvageable at every coupling
   tested. The diagnostic commits to the full min–max interval. Is that the honest object or an
   adversarial artifact? Is the headline "bounded above by a redundancy threshold" load-bearing on that
   choice? If so, say what the result reduces to under the other convention.
4. **Probe A's benign reading.** The memo reports merge-only behavior with no inversion, and reads that
   as the mask degrading to "unresolvable" rather than "wrong-signed." Is the absence of inversion
   itself forced by the construction?

**Required exit.**
(a) Genuine could-have-failed result — **name the specific parameter whose change would have emptied
the intersection**, and the value at which it does.
(b) Forced by construction — state the mechanism.

A finding of (b) does not necessarily kill the result; it changes its grade and what may be said about
it. Say which.

---

## Task 2 — Attack the revised Φ_MIP scope wording.

The §4 repair was rewritten after Prime found it asserted cross-normalizer value-robustness while
simultaneously deferring the audit that would establish it. The revised claim is:

- Because Φ_MIP is the value *after* minimizing over cuts, changing the normalizer changes the
  objective and can move **both** the minimizing partition and the minimum value; the normalizer is
  therefore part of the coordinate's declaration wherever Φ_MIP is reported.
- What is stable is *local*: along a coupling ramp at a fixed convention, the two candidate cuts are
  near-degenerate at a relabel crossing, so the minimizing partition flips while the value barely
  moves. Near-degeneracy at the crossing — not robustness across the normalization family.
- Zero-calibration is exact. Gradedness, irreducibility, and one-vs-many ordering are established only
  for the convention actually tested and are not asserted across others pending audit.
- Scope: static Gaussian, fixed candidate system at a fixed grain under a declared MIP normalization
  convention — explicitly **not** "a fixed partition."

Attack all four. In particular: is zero-calibration genuinely normalizer-independent, or only
independent across the normalizers tested? Is near-degeneracy at the crossing generic, or an artifact
of the particular ramp used? Does "the value barely moves" survive a normalizer that is discontinuous
in partition size or cardinality?

Exit (a) sound as scoped / (b) defect, with the site and the reason.

---

## Task 3 — Retroactive sweep under the new standing rule.

A standing rule was adopted today, on the strength of three prior instances:

> Any figure, benchmark, or worked result claiming an outcome "could have come out otherwise" must
> name, before it runs, the specific parameter whose change would have flipped it.

Apply it to the whole master, retroactively. Figure MW and §11b are already being repaired; the v1.18
benchmark and the §13 embarrassment condition are known. **Find the rest.**

Deliver a list: location, the claim as written, and whether a flipping parameter exists. Where one
exists, name it. Where none does, say so — that is the finding.

Do not limit yourself to the literal phrase. The defect is conceptual: "could have failed," "not built
into," "a genuine test," "the result was not guaranteed," "independent confirmation," and unmarked
claims of external validation all belong in scope.

---

## Task 4 — One cold identity read.

P2-5 proposes to shelve "the coupled-Gaussian two-module attempt." The verification memo describes a
static-Gaussian **K4** system with models 1–3. These may be two different computations — the v1.20 E17
mask that P2-5 is pulling, versus the salvage diagnostic that was independently verified.

Read both cold and state whether they are the same object. This matters because if they are different,
the proposed edit attaches one artifact's caveat to another, and "returned to open" would erase
verified work rather than restore an open item.

Answer only. Do not propose the corrected wording — that is Cowork's.

---

## Source documents you will need

Request these from Ben; several are on Drive in `1.0 AOP Canon`. IDs below are second-hand from the
verification memo and should be confirmed to resolve before you rely on them.

- `AOP_MaskSalvage_VERIFICATION_memo_20260721.md`
- `AOP_MaskSalvage_Diagnostic_20260721.md` (`1pS-BhdfUrPsqB7BXbcCGVdJHh9ZGXYvq`)
- `mask_salvage.py` (`1GPcrRSySofAD_yZeCcPkpB_S53IOkrC_`), sha256 `20c02ca1243ca6cb8d4f6a174be13d1b2dd338771078132b658a24c82dbaf062`
- `AOP_v1.22_DecisionPackage_20260722.md` and `AOP_v1.22_VerdictResponse_20260722.md`
- `AOP_CANON_MASTER_v1.22_PROPOSED_ASTER.md` — §4, §11b, §12, §13, §13a, masthead, Data Accessibility
- `AOP_CANON_MASTER_v1.21.md` for the append-only comparison

---

## Out of scope

Not yours this pass: the second completeness grep on concept-synonyms for "fixed partition"
(Cowork); the P2-5 rewrite (Cowork, after Task 4 resolves); the fold decision (Ben).

## Conventions

Grade findings SETTLED / SYNTHESIS / FRONTIER / DEFECT. Use exits (a) sound / (b) defect. Where you
find a defect, state the site, the mechanism, and the minimum repair — not the prose.

Nothing folds on this pass. Live v1.21 stays untouched.
