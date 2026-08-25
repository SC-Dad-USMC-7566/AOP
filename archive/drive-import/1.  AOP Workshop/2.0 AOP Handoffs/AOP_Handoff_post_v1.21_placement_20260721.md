# AOP — Handoff for the next chat-seat Claude (21 July 2026, post-v1.21 placement + two adjudications)

Welcome back. Canon is placed and current, two team builds came home and were judged, and there is a
clean set of next moves waiting. Read the charter and canon first, note versions in your startup block,
then skim this. Ben is your partner in this seat — the two of you direct the team and judge its work;
you are not here to grind documents (that is Cowork). Keep this seat's context clean for thinking.

## Startup check (fill in and verify currency — do not tick a stale read)
- [ ] **AOP Charter — v1.2** (project instructions). Chat seat thinks/decides/grades; execution seat (Cowork) carries out.
- [ ] **AOP Canon — v1.21 is LIVE and placed.** `AOP_CANON_MASTER_v1.21.md` in the Canon folder
      (`1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J`), id `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`, 208,518 bytes,
      masthead "version 1.21". Confirm it is still the only master before resting weight on it.
- [ ] **Drive connector: on.** Note: **bash / code execution was DOWN the prior session.** If yours works
      you can re-run scripts locally; if not, route numeric verification to execution seats (CS / a fresh
      Cowork instance / Ben-local), as the prior session did.

## Where things stand — this session's work
Two builds returned and were adjudicated in the judgment seat. **The headline lesson: reproducible ≠ valid;
the critic pass is not optional.**

### 1. Semantic-mask salvage (Cowork build) — RED upheld. Does NOT fold. Nothing hits canon.
The diagnostic asked whether the scramble-and-rerun mask's *well-defined* region overlaps its *informative*
region. Cowork's memo claimed "salvageable up to a redundancy ceiling a\*≈3.4." A fresh Cowork instance
verified the numbers **reproduce** (they do) and correctly declined to bless the interpretation, deferring
to the critic. Aster (OAI critic) then broke the interpretation, and two kills are decisive:
- **The "ceiling" is a cross-context artifact.** The interval merge compares the load edge's *worst* context
  against the spectator's *best* context — incompatible coalitions. Under any *matched* background coalition
  the load edge outranks the spectator through a=100. Discrimination never dies at a\*; only the mismatched
  envelope overlap does.
- **The redundancy number is on the wrong set.** Ω≈0.81 is whole-K4 O-information; the declared set
  S={0,1} has O-information *identically zero* (two variables → zero by construction). "Redundancy ceiling"
  is unsupported — a mathematical certainty, not a judgment call.
- Corroborated defects: S encodes the load/spectator ranking (a designed ordering, not discovered relevance);
  θ→0 is not KW's scramble (v1.21 already says so); the informativeness threshold is dead code (`salv` ignores
  it); the printed "Shapley" is an unweighted coalition mean; a\*=3.303 not 3.4; the 0.5 width tolerance
  manufactures the "non-trivial" breadth (tighten to 0.2 and the region nearly vanishes).
- **The buried positive (the useful part).** Matched-context discrimination is **robust to a=100**. So the
  build guidance REVERSES: not "per-edge mask dies past a\*," but "per-edge mask discriminates fine if you
  hold context fixed; what you cannot quote is a context-free per-edge number." The standing question flips —
  the *informative* region is broad; the *well-defined* (resolvable context-free weight) region is the real limit.
- **Disposition:** does not fold; canon untouched (pre-fold, and v1.21 already describes the mask as an
  extension claiming no salvageability, so no retraction). **Ben decides:** pre-registered rebuild on Aster's
  terms (S/graph ensemble, Ω-on-S, Shapley-weighted attribution, explicit attribution criterion, threshold
  sensitivity sweep) OR shelve as an internal-edge ablation game.

### 2. Moving-MIP normalization gate (CS build) — "well-posed," but NOT yet blessed.
Prime designed this as a well-posedness gate: does normalizing Φ_MIP dissolve the straddle transition and
make the frontier item moot? CS's answer: normalization (`Φ_norm = I(A;B) / min(|A|,|B|)`) kills the
singleton small-side collapse, but the MIP **still relabels across a straddle** — module cut → a genuine
*balanced 3|3* cut for b>1 (community inversion). Zero-calibration preserved under two normalizers. Honest
caveat: the toy model's node-exchange symmetry gives a 9-fold tie past b=1; a **fully weight-jittered** model
gives a unique competitor (relabel near b≈0.89). Grades computation SETTLED, "well-posed" reading SYNTHESIS,
no canon edit.
- **This is a clean answer to the gate — but it is a builder result no one has re-run or attacked.** That is
  exactly the stage the mask was at before Aster caught its fatal interpretation flaw. **Hold the "well-posed"
  stamp until an independent re-run + an Aster attack clear it. Do not scope the repair on CS's say-so.**
- If it clears: the frontier item is well-posed and the repair is worth scoping — with the **corrected
  benchmark** (jittered weights, balanced-3|3 relabel ~b≈0.89, not the singleton at 0.42).

## Open threads (prioritized)
1. **Route the moving-MIP gate to verify + critique** (top priority — it gates real work). Independent re-run
   by a non-CS seat + an Aster attack. Only then is "well-posed" earned and the repair scopeable.
2. **Ben decides mask salvage: rebuild vs. shelve.** If rebuild, it is a *pre-registered* build on Aster's
   five terms (above); that is a fresh work order.
3. **Drive housekeeping (Ben, manual — connector cannot delete).** Trash the 11-byte mask stub
   `AOP_MaskSalvage_Diagnostic_20260721.md` (`1GhK80yqIQ8jtTvY7I9LH41XNiG2BOLub`); clear the moving-MIP
   `rev2` / `rev2b` / `v3` generations (ignore anything without `v4`). Same "future session grabs the wrong
   file" hazard that has already bitten twice.
4. **Moving-MIP repair (only if the gate clears verification).** Prime's steer: the *closure* path is narrow —
   a grid-invariant continuum objective (`∫Φ dt + λ·TV(P)` with an explicit Δt) then tie λ to the adiabatic
   ε the canon already quantifies for the spatial half. The other roadmap items (soft/annealed Gibbs version,
   spectral derivation, robustness sweeps, competing-partition benchmark) are *soundness*, not closure —
   reorder accordingly, and use the jittered benchmark.
5. **Carried verification debt from the v1.21 fold (before journal submission).**
   - `arXiv:2410.13375` = **Ptaszyński & Esposito, PRL 135, 057401 (2025)** — v1.21 upgraded it, but confirm
     the exact proposition number/statement in full text before submission (it was the one load-bearing ⚠).
   - Author-list confirms: Marshall et al. 2026 (Neurosci. Conscious. niag013); Zhang/Zhao et al. 2025
     (npj Complexity; arXiv:2405.09207).
6. **D4 — PARKED, do not start without Ben:** the paired stellar counterfactual (does fusion actually lengthen
   stellar lifetime — declared intervention + exit set + counterfactual). A §13 open item. Revisit after the
   moving-MIP gate clears.

## Discipline that paid for itself this session (do not relearn these)
- **Build / verify / critique on separate seats — the mask just proved it.** Re-execution confirms the code
  does what it does; it does NOT confirm that what it does is what is *claimed*. Only the adversarial critic
  caught the whole-graph-Ω and cross-context-envelope flaws. **Never fold a builder result on reproducibility
  alone.** (This vindicates the build/verify-seam refinement codified the morning of the 21st.)
- **Check that every quantity is computed on the DECLARED set, not the ambient graph.** The mask's fatal flaw
  was Ω computed on all of K4 instead of on S. When a claim is "X-of-the-declared-set," grep the code for what
  set X is actually computed on.
- **"Shapley" must be Shapley-weighted** (`|C|!(n−|C|−1)!/n!`), not an unweighted coalition mean. And a
  min/max-over-different-coalitions *envelope* is context-sensitivity, not discrimination-loss — do not conflate.
- **Any "non-trivial region" claim needs a threshold-sensitivity sweep** before it is load-bearing (the 0.5
  tolerance manufactured the mask's breadth).
- **Verify canon currency against the live Canon folder, not version stamps or pasted artifacts.** This session
  Ben pasted v3 moving-MIP while v4 was live, and v1.20-era mask docs while v1.21 was being placed. The folder
  is ground truth.
- **Carried, still true:** byte-precise folds; never re-write the ~200k master through create_file; version
  history is append-only.

## The operating model (how we work — Ben's, codified)
- **This chat thread = the partnership / judgment seat.** Ben + Claude think, decide, grade, write prompts,
  and *evaluate* what the team produces. Protect this seat's context; do not fill it with mechanical assembly.
- **Cowork = execution seat** (document builds, large-file folds, Drive housekeeping, multi-step runs).
- **Claude Science = builder** (drafts, code, models). **Aster / OAI = outside critic** (attacks, finds holes).
  **The Conductor = governance** (charter / reconciliation).
- **The rule that does not bend: nobody grades their own homework.** Builder proposes → a *different* seat
  verifies by re-doing, not re-reading → critic attacks → Ben decides. Keep build and verify on different
  seats; verification is *independent re-execution*, sequenced after the build (never parallel — that is how a
  real fork happens).

## Tools / IDs
- Folders: Canon `1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J` · Canon Development `1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`
  · Handoffs `1iWT8I1b-56QXlXRR3CngpdfNNfhaV7bM` · Charter `1jq7woDxadusLPT_Et9mA8Rte4vKpdJwl`
  · Ladder `1sSZHZHgdpwfAYENt2KJkVZfey34LzCYt`
- Canon master v1.21: `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`
- Mask: script `1GPcrRSySofAD_yZeCcPkpB_S53IOkrC_`; real diagnostic `1pS-BhdfUrPsqB7BXbcCGVdJHh9ZGXYvq`;
  **stub to trash** `1GhK80yqIQ8jtTvY7I9LH41XNiG2BOLub`; Cowork verification memo `1V5_97YdT22XMnBhLBGkfRUlm1fr9cHib`
  + run log `1_PTCSavHBcfDkTdLmqr5N6OOtPJo-jWK`; Aster red-team deposited (locate by `REV_Aster_AOP_MaskSalvage`).
- Moving-MIP v4: proposal `1wxSAE10FxoG9McEYRBALX2u2_cp14z0f`; script `1_dN14YTylD5LfM5nGVJ7_DNHPYj9xWHK`;
  figure `1sOpGXj-YdNk6avPg5Gsc4RftQT7gaJ_K`. CS well-posedness gate: memo `1dLb_aN21b9_N-9UmI3B4yFxTY_qN5d5P`;
  script `16hS9CCjs7TXdyTMz4wl9b4QgIHQFojun`; figure `1tTUrHHGuFJSCqiMKkNVZOGYKilAiGjpG`.
- OpenAlex API key exists (Ben has it) — good for citation metadata + adversarial prior-art; it does NOT give
  theorem text, so it never substitutes for a primary-source line-check.

## A note on tone
Ben wants a real partner, not an echo — push back when something is off, grade honestly, no flattery, protect
the science over the momentum. He brings precise, well-sourced thinking; meet it. The best moments this session
were the ones where the loop caught a false headline *before* it shipped (the mask). Keep that loop tight.

— Prime, end of session, 21 July 2026.
