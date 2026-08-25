# AOP — Handoff for the next chat-seat Claude (21 July 2026, post-v1.21)

Welcome back. You're picking up a project in good shape and a team that's working. Read the charter and
canon first, note versions in your startup block, then skim this. Ben is your partner in this seat — the
two of you direct the team and judge its work; you are not here to grind documents (that goes to Cowork —
see "How we work"). Keep this seat's context clean for thinking.

## Startup check (fill in and verify currency — don't tick a stale read)
- [ ] AOP Charter — **v1.2** (project instructions). Adds "The working roles": chat seat thinks/decides/
      grades; execution seat (Cowork) carries out. Note: a Conductor pass may have reconciled the three
      charter artifacts (v1.2 vs the Drive `AOP_Charter_(V6)` vs the OAI "Maximal Execution Charter") —
      check `0.0 AOP Charter` (`1jq7woDxadusLPT_Et9mA8Rte4vKpdJwl`) for `AOP_Charter_Reconciliation_20260721.md`.
- [ ] AOP Canon — **check which is live.** As of this handoff, `AOP_CANON_MASTER_v1.21.md` was folded,
      verified, and delivered to Ben for manual placement, but **may not yet be on Drive as the master.**
      If it's in the Canon folder (`1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J`), canon = **v1.21**. If not, v1.20
      is still live and v1.21 sits in this session's outputs + `AOP_v1.21_ApplyRecord_20260721.md`
      (Canon Development). **Confirm before doing anything that rests on canon.**
- [ ] Drive connector: on.

## Where things stand (this session's work)
The four-collaborator machine ran a full cycle and it worked. Highlights:
- **Red-team → corrections → fold.** Aster (OAI critic) found three premature closures in v1.20. Prime
  concurred, drafted fixes, routed the contested one back through Aster twice (it caught real defects
  both times, including one where Prime's own fix introduced a new error), then folded v1.20→**v1.21**:
  the star's "fusion lengthens life" claim de-scoped to a declared open item; Drive→Integration re-graded
  from a "tendency" to a model-scoped feasibility constraint; the shaky citation line-checked and upgraded
  (arXiv:2410.13375 = **Ptaszyński & Esposito, Phys. Rev. Lett. 135, 057401 (2025)**). Full record:
  `AOP_v1.21_ApplyRecord_20260721.md` (Canon Development).
- **In flight (dispatched, not yet back):** Claude Science building the time-extended moving-MIP (the one
  genuine frontier); Cowork running the semantic-mask salvage diagnostic (does the mask's well-defined
  region overlap its informative region at all); the Conductor reconciling the charter.

## Open threads (prioritized)
1. **Place v1.21** (Ben) → then update the startup block's canon version everywhere.
2. **D3 — planning-doc only.** The "1 of 15 genuine new work" score correction applies to the gap plan
   and `AOP_FourAxis_Combined_Report.md`, NOT the canon (verified: no such tally in the master). Small.
3. **Propagation-bus note** — the Drive→Integration re-grade + star de-scope move the hub inventory; post
   an AOP→Ladder note to `2.0 AOP Handoffs`.
4. **Collect the in-flight builds** — moving-MIP (Science), mask salvage (Cowork), charter (Conductor).
   Each is a *proposal*; verify independently before it counts.
5. **2410.13375 full-text proposition-number check** before journal submission (authors/venue/scope done).
6. **D4 — PARKED, noted:** the paired stellar counterfactual (does fusion actually lengthen stellar
   lifetime — declared intervention + exit set + counterfactual). Recorded as a §13 open item. Revisit
   after the moving-MIP clears. Do not start without Ben.

## How we work (Ben's recommendation, 21 July — the operating model)
- **This chat thread = the partnership seat.** Ben + Claude think, decide, grade (settled/synthesis/
  frontier), write the prompts, and *evaluate* what the team produces. Big thoughts and direction live
  here. Protect this seat's context — don't fill it with mechanical assembly.
- **Cowork = the execution seat.** Same model, same project, same standards — but context-abundant, so it
  does the heavy assembly: document builds, large-file folds, Drive housekeeping, multi-step runs. When a
  deliverable needs "putting the documents together," that's a Cowork job, handed down from this seat.
- **Claude Science = builder** (drafts, code, models). **Aster/OAI = outside critic** (attacks, finds
  holes). **The Conductor = governance** (charter/reconciliation).
- **The one rule that doesn't bend: nobody grades their own homework.** Builder proposes → a *different*
  seat verifies by re-doing/re-checking, not re-reading → critic attacks → Ben decides.

  **One refinement this session earned:** keep *build* and *verify* on different seats. Cowork should
  *assemble*; this seat (or another agent) should *verify the assembly against ground truth*. If Cowork
  both builds and blesses its own output, the check collapses. The v1.21 fold happened to be built AND
  verified in the chat seat this time — that's fine for a Prime-run correction, but for anything Cowork
  assembles, the verification comes back here.

## Hard-won discipline that paid for itself this session (don't relearn these)
- **Verify against the *live* master before editing, always.** This session that caught (a) a changeset
  instruction to "fix" a Table 2 tag that didn't exist — the live table already read correctly, and the
  *body* was the overstated side; and (b) inline citations updated while the bibliography still said
  "[Authors TBD]" — an internal contradiction that would have shipped. Version stamps and changeset
  quotes are not the master.
- **Byte-precise folds.** Download → decode → edit programmatically: slice every OLD span *from the live
  file* (never retype — the master uses curly quotes, em-dashes, →, −, μ₊, ń), assert each replacement
  matches exactly once, then `diff` to confirm only the intended regions moved. Script pattern in
  `apply_v121.py` logic (recorded in the apply record).
- **Version history is append-only.** Correct the body in place; bump the masthead + add a changelog
  entry; leave prior-version lineage clauses and changelog entries byte-intact as history. Confirmed the
  v1.20 entry survived identical.
- **Never write the ~200k master back through the create_file tool** (transcription-corruption risk on a
  file that size). Build locally, deliver via present_files, Ben places. Small files (notes, changesets,
  scripts) are fine to write to Drive directly.
- **Two-master hazard:** the clean canon lives in `1V_ufL…`; a near-identical staging copy lives in the
  dev tree `1_9tnN03…` (was 118 bytes off v1.20). Do not fold from the staging copy.
- **Drive download decode pattern:** large downloads land at `/mnt/user-data/tool_results/…json`; load the
  outer JSON → the item's `text` field is a JSON string → parse it → base64-decode its `content` key.

## Tools / IDs
- Canon folder `1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J` · Canon Development `1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`
- Charter folder `1jq7woDxadusLPT_Et9mA8Rte4vKpdJwl` · Handoffs `1iWT8I1b-56QXlXRR3CngpdfNNfhaV7bM`
- Ladder folder `1sSZHZHgdpwfAYENt2KJkVZfey34LzCYt`
- This session's Canon Development deposits: WorkOrders, Prime_RedTeam_Review, ChangeSet rev1/rev2,
  ApplyRecord. Aster's red-team memo: `AOP_RedTeam_v1.20_20260721.md`.
- OpenAlex API key exists (Ben has it) — good for citation metadata + adversarial prior-art search; it
  does NOT give theorem text, so it never substitutes for a primary-source line-check.

## A note on tone
Ben wants a real partner, not an echo — push back when something's off, grade honestly, no flattery, and
protect the science over the momentum. He brings precise, well-sourced thinking; meet it. The best moments
this session were the ones where the loop caught a mistake *before* it shipped. Keep that loop tight.

— Prime, end of session, 21 July 2026.
