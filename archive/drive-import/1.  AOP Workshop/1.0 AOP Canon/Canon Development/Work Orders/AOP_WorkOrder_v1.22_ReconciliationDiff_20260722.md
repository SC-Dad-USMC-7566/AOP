# WORK ORDER — AOP: v1.22 proposed-master reconciliation diff

**Issued by:** chat seat, 22 July 2026.
**Standing instruction: do not fold anything. Do not edit either master. Report only.**

## Why this order exists

A proposed canon master `AOP_CANON_MASTER_v1.22_PROPOSED_ASTER.md` was deposited at
2026-07-22T03:01:29Z. The summary presented to Ben describes eight changes. The only
change record on Drive — `AOP_Canon_ChangeSet_v1.21_to_v1.22_RETRACTION.md`, deposited
17 minutes earlier — documents edits R1–R8, which cover three of them. Five are
undocumented, and the changeset explicitly contradicts the summary on a sixth (Marshall
author list: summary says verified, changeset §7 says still-open debt).

Either the proposed master contains edits no change record documents, or the summary
describes work discussed but not folded. Both break the standard that every changed line
maps to a logged edit. This order resolves which.

Note: the +6,708-byte size difference is consistent with R1–R8 alone and is **not**
evidence of extra edits. The mismatch rests on the text, not the file size.

## Files

| Role | ID | Size | Timestamp |
|---|---|---|---|
| v1.21 live master | `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP` | 208,518 B | modified 2026-07-21T19:15:04Z |
| v1.22 proposed | `1BPO2R0H8v4oYyUpYSdAJxJHsPr1JB-SA` | 215,226 B | created 2026-07-22T03:01:29Z |
| Retraction changeset (sole change record) | `1rJJppdn6ARzkFlMQD5k6bAVPCFJhHv-Q` | 28,064 B | created 2026-07-22T02:44:40Z |

Canon folder `1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J` · Canon Development `1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`

---

## Task 1 — Line-level diff

Download both masters, decode, diff. For every changed, added, or deleted line in v1.22,
map it to one of edits R1–R8 in the changeset.

Produce three lists:

1. **Mapped** — changed lines that trace to a specific edit (cite which).
2. **Unmapped** — changed lines that trace to no logged edit. **This is the deliverable that matters.**
3. **Specified but not applied** — changeset edits with no corresponding change in the master.

## Task 2 — Targeted search for the five undocumented claims

The summary claims five changes the changeset does not contain. For each, search v1.22 and
diff against v1.21. Report present / absent, with line numbers where present.

1. Drive's lifetime sign
2. Commensurability
3. The Energy-hub claim
4. The non-energy triangle
5. Figure MW regraded as a proxy-ablation diagnostic, with §11b retained as the finite-horizon viability competence check

## Task 3 — Integrity checks

- Does v1.22 self-label **PROPOSED / NON-CANONICAL** in its masthead?
- Per R7, version history below the masthead is **append-only**. Confirm the v1.20 and v1.21 entries are byte-identical between the two files.
- Confirm v1.21's modifiedTime is still 2026-07-21T19:15:04Z — i.e. the live master is genuinely untouched.

## Task 4 — Locate the missing review document

A "top-to-bottom review and rationale" was referenced to Ben but is not in the Canon or
Canon Development folders under an AOP title. Search Drive broadly, including recently
created files that do not match `AOP*`. If it does not exist, say so plainly rather than
returning the nearest match.

---

## Cautions

- **Do not re-upload either master via `create_file`.** Transcription-corruption risk at 200k+ characters. Read only.
- **Do not repair anything found.** Findings go in the memo; the chat seat and Ben decide disposition.
- Note that Drive full-text search loose-matches and returns false positives. Do not use it as an existence test; diff the decoded files.

## Deliverable

Deposit as `AOP_v1.22_ReconciliationDiff_20260722.md` in Canon Development
(`1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`).

## Already closed — do not redo

- The R1–R8 numbers are independently reproduced by a third seat, written from specification rather than from the deposited script: MIP relabel b = 0.330221125 (N=8) and 0.420600748 (N=6); module/whole equality at 0.3002367 marginal, 0.2163268 conditional, 0.6295630 isolated; size- and entropy-normalized selectors hold the module boundary through b = 1.0 and move to the balanced cut (0,1,4,5) at b = 1.05.
- Liu K, Yuan B, Zhang J, *Entropy* **26**(8), 618 (2024), doi:10.3390/e26080618 — verified against primary. Optimal coarse-graining is set by the **dynamics parameter matrix**, explicitly non-unique.
- Marshall W, Findlay G, Albantakis L, Tononi G, *Neurosci. Conscious.* **2026**(1), niag013, doi:10.1093/nc/niag013 — full author list verified against primary. Carried ⚠ discharged.

## Open question for the chat seat, not for this order

The retraction ring-fences §4 ("the Φ_MIP axis itself is untouched — one-vs-many at a
*fixed* partition"). If §4's coordinate is in fact evaluated at *the* MIP rather than at a
declared fixed cut, the argmin instability reaches §4 and the retraction is under-scoped.
Flagged, not assigned.
