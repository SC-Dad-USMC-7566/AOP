# AOP — v1.22 proposed-master reconciliation diff

**Executed by:** Cowork (execution seat), 22 July 2026, on work order `AOP_WorkOrder_v1.22_ReconciliationDiff_20260722.md` (issued by the chat seat).
**Standing instruction honored:** nothing folded, neither master edited, report only. No `create_file` re-upload of either master; both were read (downloaded and decoded), never rewritten.

---

## Verification record (what this diff actually rests on)

Both masters and the changeset were downloaded with `download_file_content`, base64-decoded to disk, and checked against Drive metadata before any diffing.

| File | id | Drive bytes | Decoded bytes | Match |
|---|---|---|---|---|
| v1.21 live master | `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP` | 208,518 | 208,518 | ✓ exact |
| v1.22 proposed | `1BPO2R0H8v4oYyUpYSdAJxJHsPr1JB-SA` | 215,226 | 215,226 | ✓ exact |
| Retraction changeset | `1rJJppdn6ARzkFlMQD5k6bAVPCFJhHv-Q` | 28,064 | 28,063 | −1 byte (see note) |

The changeset decoded one byte short of its Drive size (28,063 vs 28,064), reproduced identically on two independent downloads (sha256 `e34b9cbe…6270a0` both times). The decoded text is complete and coherent — it opens on a clean `# AOP Canon` heading and closes on a complete sentence with no trailing newline. Most likely the master carries a trailing newline the base64 export drops; it is not a transcription loss on our side and does not affect any finding below. Both masters decoded byte-exact, so the line-level diff is trustworthy.

The diff is a clean `diff -U1`: **19 hunks, 57 changed lines.** Small enough that every changed line was inspected by eye, not sampled. Line numbers below are from the decoded files and are advisory; every claim was matched on text, per the work order's own caution.

---

## Headline finding

Every one of the changeset's edits **R1–R8 is present** in v1.22 (Task 1 list 3 — "specified but not applied" — is empty). But R1–R8 account for only a minority of the diff. The proposed master also carries a **large second body of edits that no change record documents** — the "four coherence repairs" the summary described — plus **two edits that the changeset actively contradicts or forbids**: the Marshall author-list discharge (changeset §7 lists it as still-open debt) and an in-place edit to the frozen v1.21 version-history entry (R7 declares that entry append-only).

So the work order's framing is confirmed on the harder horn: the proposed master contains substantive edits with no logged change record, and in two places the master and its sole change record disagree.

---

## Task 1 — line-level diff mapped to R1–R8

### 1. Mapped (changed lines that trace to a specific logged edit)

| Master location (≈v1.22 line) | Change | Maps to |
|---|---|---|
| §4 Φ_MIP intro (~143) | normalization-robustness claim struck and scoped to magnitude-at-fixed-partition; adds b≈0.33 raw-vs-normalized relabel | **R3** |
| §9a FRONTIER cell (~414) | v1.20 seam-narrowing withdrawn; "open in both halves" | **R5** (verbatim to R5 NEW) |
| §12 Φ_MIP status-table row (~636) | "normalization-robust" → magnitude robust / identity not; "nested level-selection (a v1.20 closure **retracted in v1.22**)" | **R4** (verbatim to R4 NEW) |
| §13a level-selection paragraph (~778–787) | full RETRACT AND REPLACE; grade `[SYNTHESIS]` → `[OPEN; retracted in v1.22]` | **R1** |
| §13a moving-partition paragraph (~789–797) | "half-closed / principal open problem is the time-extended moving partition" → "Adiabatic moving partition … kink marks an exchange of optimizers, not an individuation event … open in both halves" | **R2** |
| Data-accessibility, phaseD1 listing (~798) | appends "computes the MIP of a single fixed graph … does **not** compute a cross-grain comparison … retained as the record" | **R8** (verbatim to R8 ADD) |
| References, Liu/Zhang entry (~976) | "Zhang J, Zhao K … *npj Complexity* (2025)" → "Liu K, Yuan B, Zhang J … *Entropy* 26(8), 618 (2024). doi:10.3390/e26080618 … not unique" | **R6** (verbatim to R6 NEW) |
| Masthead running summary (~15) | prepends a v1.22 clause ahead of the v1.21 clause; retraction content | **R7** (intent) — see caveat |

**R7 caveat.** The masthead does carry a v1.22 retraction clause, so R7 is applied *in substance*. But (a) the wording is not R7's specified ADD text — the master folds the four undocumented coherence repairs into the same masthead clause; and (b) R7's own stipulation, "version history below the masthead is append-only and the v1.20/v1.21 entries are **not** edited," is **breached** (Task 3b). R7 is therefore "applied, but not as specified, and self-contradicted."

### 2. Unmapped — changed lines that trace to no logged edit *(the deliverable that matters)*

These are real, substantive edits. None appears in R1–R8. They are the "four coherence repairs" (five, if Energy-hub and the non-energy triangle are counted separately, which they are in Task 2), spread across the document:

| Master location (≈v1.22 line) | Unmapped change | Theme |
|---|---|---|
| PROPOSED banner blockquote (~5) | new "**PROPOSED / NON-CANONICAL — Aster synthesis for Ben's review**" line | (integrity self-label; not in changeset) |
| Masthead running summary (~15) | "four live coherence defects" sentence embedded in the v1.22 clause | all four repairs |
| Abstract (~19) | "lifetime is lengthened" → "can be altered or stabilized"; adds measure-preserving-current sign sentence; "Energy is the hub" → "principal organizing hub [SYNTHESIS]"; mask split into Figure MW proxy-ablation + §11b competence check | Drive sign · Energy-hub · Figure MW |
| "The claim, in one paragraph" (~50) | "four ways to raise the same quantity" → "act on"; adds "Nor is every intervention pro-persistence: the sign must be stated for the declared regime" | Drive sign |
| "No master quantity" (~56) | "the common form is what makes them commensurable" → "makes them expressible in one vocabulary; it does **not** make their raw magnitudes commensurable … requires the declarations in §12″" | Commensurability |
| Figure MW section (~122–126) | whole paragraph rewritten into "two deliberately different demonstrations": Figure MW = internal-edge proxy-ablation diagnostic; §11b = viability-grounded finite-horizon competence check | Figure MW / §11b |
| "Energy is the hub" (~129) | prepends "**[SYNTHESIS / organizing description of the current ledger.]**"; "not a theorem that energy is structurally privileged in every persister" | Energy-hub |
| Non-energy triangle paragraph (~145) | "where the genuine open work sits / contingent and dissociable" → "need two grades": model-level dissociable vs general modal status unidentified | Non-energy triangle |
| Status-table mask row (~624) | "computed on the Figure DM ring … a demonstration of self-consistency" → "Figure MW is a proxy-ablation diagnostic … §11b is the viability-grounded competence check … not external validation" | Figure MW / §11b |
| Table 2 non-energy-triangle row (~651) | "open / measure-dependent; the real remaining work" → "model-level dissociable; general modal status unidentified / Gaussian VAR counterexamples … no universal coupling law" | Non-energy triangle |
| "Semantic mask, two-layer move" table row (~754) | appends "+ proxy diagnostic (Figure MW) + analytic competence check (§11b); external validation open" | Figure MW / §11b |
| "A fourth exposure" paragraph (~773) | "Drive does have direct leverage — … forced-edge structure (Drive acts through Memory and Boundary)" → "Drive has **direct anti-persistence leverage** in this declared regime … must not be described as indirect action through those edges … A positive pro-persistence role … is not established" | Drive sign |
| Data-accessibility, Figure MW sentence (~790) | "scramble-and-re-run … three present-tense viability functionals" → "three dynamical proxies … reported as proxy sensitivities, not finite-horizon survival weights. The viability-grounded finite-horizon mask is … §11b" | Figure MW / §11b |
| **References, Marshall entry (~974)** | "Marshall W, et al. … [⚠ confirm full author list]" → "Marshall W, Findlay G, Albantakis L, Tononi G … doi:10.1093/nc/niag013 … prior ⚠ discharged" | **contradicts changeset §7** |
| **Changelog, v1.21 entry (~988)** | Ptaszyński/Esposito citation edited in place: full author first-names inserted, "now" and "[Authors TBD]" removed (2,575 → 2,582 bytes) | **violates R7 append-only** |
| Changelog, v1.22 entry (~990–995) | new appended entry — the append itself is legitimate structure, but its coherence-repair content is undocumented | all four repairs |

Two of these are worse than merely undocumented:

- **Marshall discharge contradicts the sole change record.** Changeset §7 ("Open items this change set does **not** close") lists, verbatim: "Carried verification debt, unchanged: Marshall et al. 2026 (Neurosci. Conscious. niag013) author list." The proposed master discharges exactly that debt, rewriting the entry to the full four-author list and stamping "prior ⚠ discharged." This is the specific summary↔changeset contradiction the work order predicted (Task 2 item that the changeset flags on a sixth point). The discharge may well be *correct* — the changeset's own "Already closed" block in the work order verifies the Marshall author list against primary — but it is recorded in the master with no changeset edit authorizing it, and against a change record that says the opposite.
- **The v1.21 version-history entry was edited in place.** R7 is explicit that version history is append-only and the v1.20/v1.21 entries are not touched. The v1.20 entry is untouched (byte-identical, below). The v1.21 entry is **not** — its Ptaszyński/Esposito line was rewritten. Small in content, but it breaks the append-only discipline the same file's R7 asserts.

### 3. Specified but not applied

**None.** All eight logged edits R1–R8 appear in v1.22.

---

## Task 2 — the five undocumented claims: present / absent

All five are **present** in v1.22, and **none** is documented in changeset R1–R8. (Locations are the primary site plus corroborating sites; line numbers advisory, matched on text.)

| # | Claim | Status | Where in v1.22 |
|---|---|---|---|
| 1 | **Drive's lifetime sign** — measure-preserving current can only shorten/leave-unchanged; "anti-persistence"; sign must be declared | **PRESENT** | Abstract (~19); "The claim, in one paragraph" (~50); "A fourth exposure" (~773, the load-bearing statement: "direct anti-persistence leverage in this declared regime"); masthead (~15) |
| 2 | **Commensurability** — shared relative-entropy form is common vocabulary, not commensurability of magnitudes | **PRESENT** | "No master quantity" (~56); masthead (~15) |
| 3 | **Energy-hub claim** — labelled SYNTHESIS / ledger organization, not a structural theorem | **PRESENT** | Abstract "principal organizing hub [SYNTHESIS]" (~19); "Energy is the hub" section head "[SYNTHESIS / organizing description of the current ledger]" (~129) |
| 4 | **Non-energy triangle** — split into model-level dissociable vs general modal status unidentified | **PRESENT** | Non-energy triangle paragraph (~145); Table 2 row (~651) |
| 5 | **Figure MW regraded to proxy-ablation diagnostic; §11b retained as the finite-horizon viability competence check** | **PRESENT** | Figure MW section (~122–126); status-table mask row (~624); "Semantic mask, two-layer move" row (~754); data-accessibility (~790); abstract (~19) |

The proposed master's own masthead counts these as "four live coherence defects" by bundling Energy-hub and the non-energy triangle together; the work order splits them, giving five. Either way, the set is fully present and fully undocumented by any change record.

---

## Task 3 — integrity checks

**(a) Does v1.22 self-label PROPOSED / NON-CANONICAL?** — **Yes.** Two independent labels: a masthead banner blockquote ("**PROPOSED / NON-CANONICAL — Aster synthesis for Ben's review.** This file does not replace `AOP_CANON_MASTER_v1.21.md` …") and the running-summary version tag "version 1.22 (PROPOSED / NON-CANONICAL)". The appended v1.22 history entry and the closing line ("suggestion only; Ben decides after independent review") reinforce it.

**(b) Are the v1.20 and v1.21 version-history entries byte-identical between the two files (R7 append-only)?**

- **v1.20 entry — YES, byte-identical.** 3,910 bytes in both, md5 `ba594816…9339fe` in both.
- **v1.21 entry — NO.** 2,575 bytes (v1.21 master) → 2,582 bytes (v1.22), md5 `634aa390…d3b35d` → `62035b8e…018382`. The single change is the Ptaszyński/Esposito citation inside that entry: `Ptaszyński & Esposito … — now line-checked … discharging the v1.20 ⚠ [Authors TBD]` became `Krzysztof Ptaszyński & Massimiliano Esposito … — line-checked … discharging the v1.20 ⚠` (full first-names added; "now" and "[Authors TBD]" removed). **R7's append-only stipulation is violated for the v1.21 entry.** A new v1.22 history entry is also appended (legitimate).

**(c) Is v1.21's modifiedTime still 2026-07-21T19:15:04Z — the live master genuinely untouched?** — **Yes.** Drive metadata for `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP` reports `modifiedTime: 2026-07-21T19:15:04Z`, and the decoded file is byte-exact at 208,518. The live master has not been touched; the proposed master is a separate file.

---

## Task 4 — the missing "top-to-bottom review and rationale"

**It does not exist as a discrete Drive document.** Stated plainly rather than matched to the nearest neighbor, as instructed.

The proposed master's masthead attributes the four coherence repairs to "this top-to-bottom review" / "a top-to-bottom AOP audit." No such document is on Drive. Searches run: the full Canon Development folder listing (`1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`, ~60 items incl. Archive and the v1.16 submission subfolder); the Canon folder contents; every file created since 2026-07-21 (two pages); and a broad full-text sweep for the repairs' distinctive language ("proxy-ablation", "anti-persistence", "commensurability") including non-`AOP*` titles.

What *does* exist is the review apparatus for the **level-selection retraction only** — i.e. the R1–R8 lineage, not the coherence four:

- `AOP_LevelSelection_Adversarial_Memo_rev2_20260721.md` (id `16dLoj3ciS0xxgrCygh6c3ZaLIlbJrHPK`) — Aster's adversarial pass; the source of the six defects (D1–D6) that force the retraction.
- `AOP_LevelSelection_Adversarial_Memo_20260721.md`, `AOP_LevelSelection_Independent_Verification_Memo_20260721.md`, and the paired `.py` recheck/verify scripts.
- `AOP_RedTeam_v1.20_20260721.md` and `AOP_Prime_RedTeam_Review_20260721.md` — the red-team that produced **v1.21's** three corrections, not v1.22's four coherence repairs.
- Older/adjacent: `REV_OAI_AOP_Operational_Definitions_v1_0_20260717` (5 days earlier; operational-definitions scope, not the coherence four).

None of these documents the four coherence defects. The retraction (R1–R8) is backed by a memo; the coherence repairs (the five Task 2 claims) are backed by nothing on Drive — they appear only inside the proposed master itself. If a top-to-bottom review was written, it was not deposited; if it was never written, the coherence edits entered the master without a review of record.

---

## Disposition (for the chat seat and Ben — not acted on here)

Nothing was repaired, per the standing instruction. The reconciliation resolves the work order's central question — "edits with no change record" vs "summary describing unfolded work" — as **both, concretely**:

1. **R1–R8 are fully and faithfully applied** (three of them verbatim). The retraction machinery is intact and mapped.
2. **The four/five coherence repairs are in the master with no change record and no review document.** They are internally plausible and self-consistent, but they fail the standard that every changed line maps to a logged edit.
3. **Two edits break a rule the same file asserts:** the Marshall discharge (changeset §7 says still-open) and the in-place edit of the append-only v1.21 history entry.

The clean split is: the level-selection retraction is a governed, documented movement; the coherence consolidation rode along in the same file without its own changeset or review. Whether to (a) commission the missing review and a coherence changeset before adopting, (b) accept the coherence repairs as correct-but-undocumented and back-fill the record, or (c) reconcile the Marshall contradiction one way or the other, is a chat-seat/Ben decision.

**Flagged, not assigned (passed through from the work order's own open question).** The retraction ring-fences §4 as "one-vs-many at a *fixed* partition." Both the R1 replacement text and the §4 edit re-assert that fixed-partition framing, yet the deposited `phaseD1` computes the *minimum* information partition — the argmin over cuts, i.e. the relabel itself. If §4's coordinate is in practice read at *the* MIP rather than at a declared fixed cut, the argmin instability the retraction confines to level-selection would reach §4, and the retraction would be under-scoped. This diff neither confirms nor refutes that; it is consistent with the concern. Left for the chat seat.

---

*Execution seat (Cowork). Read-only: both masters downloaded and decoded, neither edited, nothing folded, nothing repaired. Deposited to Canon Development. Verify this deposit with `download_file_content`, not a read-back — `read_file_content` returns empty for markdown written with `disableConversionToGoogleType`.*
