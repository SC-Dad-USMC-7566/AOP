# AOP Charter Reconciliation — 21 July 2026

**Prepared by:** the Conductor seat. **For:** Ben's sign-off. **Scope:** governance only — this memo touches no science. **Deliverables:** `AOP_Charter_v1_1.md` (one reconciled charter) + this memo.

---

## Bottom line

The three "charter-lineage" artifacts had not forked on governance. They had drifted on **filing and naming**. Only one of the three is actually a project charter; the other two are a misfiled canon-designation document and an empty shell. So the reconciliation is a de-duplication and re-identification, not a merge — and that is a direct dividend of the charter's founding principle, *the charter is not the canon*: because the charter owns no claims, a diverging paper could not fork it.

**`AOP_Charter_v1_1.md` preserves v1.0's governance verbatim** and supersedes all three artifacts. It is paste-ready for the instruction field. Nothing was cut from v1.0. Nothing scientific was folded in — there was nothing eligible to fold.

There is **one decision for you** (a proposed *addition*, not a conflict) and a short list of **housekeeping / archive recommendations**, below.

---

## What each source is, and what it contributed

| Artifact (Drive id) | What it actually is | Contributed to v1.1 |
|---|---|---|
| **The v1.0 governance charter** — `AOP_Charter_v1_0.md`, id `1aXfDUSYsnWIW4mLLALwacaZ7oRt-vsc2` (currently in the charter folder's `Archive` subfolder; this is the clean-reset lineage that is live in the project instructions) | The real, complete AOP project charter. | **Everything.** v1.1 is this document, preserved in full. |
| **"V6"** — `AOP_Charter_(V6).md`, id `1V9C5H7Vl3tvbLnCjtadL4-I0GJnc92Rv` (in `0.0 AOP Charter`) | **Not a charter.** Its content is the **AOP Canon *designation*** — the document that names what the canon is, fixes the current paper version, and states how canon changes. By resolve-by-identity (content governs over filename), it is canon-lineage, not charter-lineage. | **Nothing** — correctly. Folding it in would violate *the charter is not the canon* (see below). |
| **OAI "Maximal Execution Charter"** — `REV_OAI_..._v1_0_20260717`, id `1xltR8AqQ6vw0D4NgWZDl5cXmtnM0E47IGsym5Zoz0cI` (Google Doc, in the canon working folder) | **Empty.** The document body is a single UTF-8 byte-order mark and nothing else (1 KB, zero text, no comments). | **Nothing** — there is nothing in it. Its intended substance went into the *canon*, not governance (see below). |

## The governing test, applied clause by clause

The test: *does the clause own a scientific claim, or restate anything that belongs in the canon?* If yes, it does not stay in the charter.

- **v1.0's clauses all pass.** The four dimension **names** (Boundary, Drive, Memory, Integration) appear, but as *pointers* — their definitions as relative entropies live in the canon, and the charter says so. The retired-vocabulary blacklist names forbidden terms without restating their science. The epistemic mode is method, not claim. Nothing in v1.0 restates canon content. Kept in full.
- **The "V6" canon-designation content fails the test — as charter content.** It names specific canonical claims and a specific current version (v1.16). That is exactly right for a canon designation and exactly forbidden for a charter: a charter that names the current paper version drifts stale the moment the paper moves (and this one already had — it says v1.16 while the canon is v1.20). So none of it is folded into v1.1. It is not *dropped* either: it is a legitimate document that has simply been misnamed and misfiled. See archive recommendations.
- **The OAI shell has nothing to test.** For completeness: the OAI review's real output was a re-architecture of the *paper*, and it is already in the canon — folded at **canon v1.18** (the six "P0 stop-ship" repairs, the declaration tuple, the four measurement panels, the §11b non-triviality benchmark). That is science/canon work, correctly placed. No governance content exists to reconcile.

**Accreted science cut from the charter: none** — because none had accreted into the real charter. The v1.0 design held. The apparent accretion was two non-charter documents sitting in the lineage, not science leaking into the charter itself.

## Version label

**Recommended: v1.1.** The governance content is v1.0 preserved intact; the change is reconciliation and re-identification, not a rewrite, so a minor bump is the honest signal. It also refuses to dignify "V6" as a real prior charter version — the true charter lineage is v1.0 → v1.1; the "6" was a number on a misnamed canon-designation copy, never a charter.

If you would rather the supersession read louder — a single unambiguous "this is now THE charter" marker that visually clears the old numbering — bump it to **v2.0** instead. I lean v1.1 on content-honesty grounds; either is defensible, and the archive step below is what actually removes the numbering confusion.

## One decision for you (a proposed addition — not a conflict)

The empty OAI doc was evidently *meant* to encode an agent-orchestration protocol — the "maximal execution" of the four-role team that the AOP handoffs already run in practice: **builder proposes → prime verifies by independent re-run → OAI (outside critic) attacks → Ben decides**, on the rule that *nobody grades their own homework*. This is genuine governance (how we work), it is non-violating (owns no claim), and it is real, evidenced project practice.

I did **not** silently install it, for two reasons: its source document is empty (so I would be sourcing a charter section from handoff inference), and whether the role protocol is *charter* material or *operational-handoff* material is a genuine judgment call that is yours, not mine. Per the "flag, don't pick a winner" discipline, here it is as a ready-to-paste section you can approve (it would fold as v1.2) or decline:

> **The working roles.** AOP is built by an adversarial team in which no one grades their own homework. A *builder* proposes work; a *prime* verifies it by independent re-run, not by inspection; an *outside critic* attacks it, prompted to refute rather than confirm; and Ben decides. A claim advances only after it has survived a role that was trying to break it. This is a discipline on how confidence is earned, not a statement of what is true — the canon still holds every claim and its grade.

Say the word and I'll cut a v1.2 with this in; otherwise v1.1 stands as-is and the protocol stays in the handoffs where it lives now.

## Archive / housekeeping recommendations (you move; the connector is create-and-read only)

Nothing deleted. Recommendations, by id:

1. **Archive the misnamed canon-designation copy** — `AOP_Charter_(V6).md`, id `1V9C5H7Vl3tvbLnCjtadL4-I0GJnc92Rv`. It is not a charter and should not sit in `0.0 AOP Charter` under a charter name. Its *content* (the canon designation) is valuable but belongs to the canon lineage and is stale (points at v1.16 vs. canon v1.20). Best path: move it out of the charter folder, and let a canon change-run refresh the live canon designation to v1.20. This dovetails with the **pointer fork** the 2026-07-21 AOP handoff already flagged — the fixed-name pointer `AOP_Canon_v1_0.md` is forked into ~4 copies with stale version lines; collapsing those to one live designation pointing at v1.20 is the same job.
2. **Archive the empty OAI shell** — `REV_OAI_AOP_Maximal_Execution_Charter_v1_0_20260717`, id `1xltR8AqQ6vw0D4NgWZDl5cXmtnM0E47IGsym5Zoz0cI`. It has no content; its real output is already in the canon (v1.18). Nothing is lost by retiring the empty title.
3. **Supersede the live v1.0 charter with v1.1** — `AOP_Charter_v1_0.md`, id `1aXfDUSYsnWIW4mLLALwacaZ7oRt-vsc2`. Keep it as the retained record (it is already in the `Archive` subfolder); paste v1.1 into the AOP instruction field. The v1.0 → v1.1 supersession is the only content change; every governance line is preserved.

Net end state: `0.0 AOP Charter` holds exactly one live charter (`AOP_Charter_v1_1.md`) and its `Archive`. The canon designation and the OAI shell leave the charter folder for their correct homes.

## What to paste where

The AOP Claude instruction field takes `AOP_Charter_v1_1.md` in place of the current v1.0 text. As always, the paste is your action — the connector reaches the Drive tree, not the instruction field. Once pasted, the next AOP startup check should read Charter v1.1 as highest and confirm the swap landed.
