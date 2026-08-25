# AOP — Handoff: v1.22 adjudication → v1.23 (23 July 2026, chat seat / prime)

**Read the Charter (v1.2) and the current canon before working; note versions in the startup block.**
This session adjudicated the proposed v1.22 consolidation and produced an apply-ready change set. It did
**not** edit the master (per discipline, the 200k master is placed manually by Ben).

## Startup / currency
- **Live canon: v1.21** (`AOP_CANON_MASTER_v1.21.md`, id `1UGmWG3b7FME1CRZOFAX3A8ew48uGePIP`, in Canon folder
  `1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J`).
- **v1.22 PROPOSED** (`AOP_CANON_MASTER_v1.22_PROPOSED_ASTER.md`, id `1BPO2R0H8v4oYyUpYSdAJxJHsPr1JB-SA`,
  same folder) — Aster's corrective consolidation. Adjudicated this session.
- Note: `read_file_content` does NOT support text/markdown for these files directly, but it **does** dump the
  body to `/mnt/user-data/tool_results/…json` ("too large for context, stored at…") which you then grep. That
  is the way past the gate the Cowork/SC seats hit. Clean extracted body was saved to `canon_v122.txt`.

## Verdict: ADOPT v1.22 + two pre-red-team repairs → v1.23
Independently verified this session (re-run / cross-checked, not read over):
- **Retraction is correct.** Re-ran `phaseD1_levelselect.py`: it computes only the whole-system MIP and its
  relabel as inter-module coupling rises; it never coarse-grains and never compares Φ across grains. The
  v1.20/1.21 "level-selection closure" was narration the code does not support. **F2 open in both halves.**
- Retraction propagated cleanly (§4, §9a, §13, §13a, Table 3, Data Accessibility). Stray `Zhang 2025` /
  `npj Complexity` / `closing the level-selection` strings survive ONLY in the historical v1.20 changelog entry
  (correct to preserve).
- All six v1.22 coherence repairs landed in the live body.
- Both freshly-swapped citations verified against **primary** this session:
  - Ptaszyński & Esposito, *PRL* **135**, 057401 (2025); arXiv:2410.13375 — matches D→I feasibility wording +
    permutation-invariant scoping. Load-bearing; solid.
  - Liu, Yuan & Zhang, *Entropy* **26**(8):618 (2024); arXiv:2405.09207 — authors/venue/year correct; the old
    "Zhang 2025 / npj Complexity" cite was genuinely wrong. Context-only.

Two residual defects **predating** v1.22 (its audit missed them), both repaired in the change set:
- **R1 (§11b header):** "The result that could have come out otherwise" contradicted the section's own
  "forced by the construction / competence check, not a discovery." Renamed → "The dissociation a one-axis
  reading inverts." Cheap.
- **R2 (§13 embarrassment condition) — the substantive one.** Computed check this session: both clauses of the
  stated falsifier are **forced by the model's positive-definite structure** (max-VIF monotone in coupling for
  both topologies over the full range; chain out-blurs mean-field at every matched mean-correlation, never
  flipping — max-VIF is governed by λ_min of the precision). "Could have come out otherwise / would falsify"
  claims a testability the linear algebra doesn't supply. Replaced with: resolvability limit = structural
  self-consistency; genuine exposure relocated to the **carving** (taxonomic; completeness/minimality held
  open, §2); named the synthesis standard the paper asks to be judged against. Brings §13 into line with the
  not-a-falsifiable-test posture the rest of the paper (Figures MW, LT, R★) already holds.
  - **Headline for the red team:** after R2, AOP has **no novel falsifiable prediction**, and is now internally
    consistent about that. Defensible as a synthesis (unifies settled results; preserves distinctions a
    single-axis account loses). Judge on Lakatos/Kuhn adoption terms, not Popperian falsification.

## Deliverable (apply-ready)
- **Change set:** `AOP_Canon_ChangeSet_v1.22_to_v1.23_R1R2.md`, deposited in Canon Development
  (`1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`), id **`1VCfcaCdugoJTBAtToVjWGURy1ukD2Hwb`** (10,922 bytes, byte-verified).
  Contains verbatim OLD→NEW for R1 and R2, a v1.23 changelog stub, and carried debt.
- **Cleanup:** a 62-byte DUD from a bad first write sits in the same folder, id
  `14v4FufKQH1S9hdUrrMmtEjgLf5YVz6EP` — **delete it.**

## Open work (next seat)
1. **Apply R1 + R2** to the v1.22 body → save as **v1.23** (adopted, red-team-ready). Master edit = manual.
   Then delete the dud.
2. **Then red-team the whole document as one** (outside critic / OAI), or clear reference debt first — Ben's call.
3. **Carried before-final debt (submission-gating, NOT red-team blockers):** full-text reads still `~` (Maes
   2020, Schnakenberg 1976, Bouchet–Reygner 2016, Oono–Paniconi 1998 — nothing load-bearing rests on these
   alone); ⚠ pagination/DOI (DiFrisco 2018, Joyce 1994 foreword, Ashby 1960, Hoel 2016 venue/DOI, Bialek–
   Nemenman–Tishby DOI, Pearl 1988, Hatano–Sasa / Speck–Seifert DOIs).
4. **Optional cosmetic:** v1.12 changelog entry still states Φ_MIP "robust across minimum-partition
   normalizations" flatly (the claim v1.22 scopes) — historical, one annotating clause would help.

## Cross-project (Ladder) note
The Ladder 2.0 seat is **holding** — it will not fold its me/we build toward canon until AOP currency clears
and §9a/§11a wording is confirmed full-body. **Both are now cleared:** v1.22 adjudicated, and the §9a/§11a
body wording read in full this session. Precise answer to its open ledger row ("we's in-AOP vs cloud decided
by Φ_MIP at the partition"): the **fixed-partition** one-vs-many call is UNTOUCHED; what v1.22 withdrew is
(a) selecting which nested level is the individual, and (b) reading a MIP *relabel* as an individuation event.
The Ladder row stands if it means "at a declared partition, we-or-cloud"; it moved if it picks the
individuated level via Φ_MIP-max or treats a relabel as we→me. Adopting v1.23 unblocks the Ladder.

## Cautions
- Don't run two threads executing the plan at once (fork risk).
- Don't re-upload the 200k master via create_file (transcription-corruption risk); deliver for manual
  placement. Small notes/change-sets are fine to write directly — use **base64Content** (textContent with a
  shell `$(...)` does NOT expand; that produced the 62-byte dud above).
