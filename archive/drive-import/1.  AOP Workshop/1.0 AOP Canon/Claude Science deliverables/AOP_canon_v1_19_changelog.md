# AOP v1.19 — Change Log (delta from v1.18)

**Compiled:** 19 July 2026. Non-canonical record. Baseline: v1.18 (`AOP_canon_v1_18_rebuild.md`, artifact 2b4d666c, version 4a05aae7). One prime-verification finding applied + one structural reorder. No scientific content added or removed.

## Applied from prime verification (`AOP_Prime_Verification_v1_18_20260718.md`)

**§11b overclaim → competence check (the one content fix prime flagged).**
- *Prime's finding:* the §11b "What is and is not claimed" paragraph asserted the strength-vs-viability anti-ranking, the Möbius sign inversion, and the substitution structure were "*not* built in… the actual result." Prime independently re-ran the benchmark and found these are **forced by the construction** — swapping the OR/AND gate topology flips the Möbius signs, and the rate assignments set the strength dissociation. The manuscript's own Table 3′ row already tagged this "forced-by-construction," so the prose contradicted its own ledger.
- *Before:* "What is *not* built in, and is the actual result: that structural strength anti-ranks viability importance, that the Möbius signs invert the naive reading, and that the substitution structure is recoverable…"
- *After:* the ground truth (redundancy/synergy/inert/load-bearing **and** the anti-ranking and Möbius sign pattern that follow from the gate topology + rates) is stated as built in throughout; the benchmark is re-described as a **competence check, not a discovery** — it shows the coalition-aware, viability-anchored method *correctly recovers* designed structure that a strength/correlation reading inverts. A pointer is added to the still-open external-ground-truth benchmark (the system AOP could actually fail). Prose now agrees with the [analytic-model-result; forced-by-construction] tag.

## Structural reorder (monotonic section numbering)

- The three appended architecture sections were sitting after §13. Reordered to monotonic position: **§11b** now follows §11a; **§12′** and **§12″** now follow §12, before §13. Section bodies are byte-identical to v1.18 — only their position moved.
- Resulting order: … §11a → §11b → §12 → §12′ → §12″ → §13 → Data Accessibility → References.

## What was NOT changed
- All six P0 repairs from v1.18 stand unaltered.
- The lifetime primitive, the 5.7× lifetime-vs-occupancy dissociation, §4a/§9a/§11a, the five worked cases, all 52 references (63 markers, verified identical count), and all figures carry over verbatim.
- Panels, declaration tuple, diagnostic-archetype re-grade, and the rival memo are unchanged.
- The §11b **Spearman −0.67** dissociation and Möbius values are unchanged — only their epistemic framing (recovered, not discovered) is corrected.

## Open items carried to Ben (unchanged from v1.18, plus one new)
1. **P0-1 rest-frame wording** — still pending Ben's adjudication (OAI listed it P0 stop-ship; the Claude matrix downgraded it; not yet ruled).
2. **External-ground-truth benchmark** (new open work, Task 2 from Ben's tasking) — a benchmark whose load-bearing structure is established by someone else, that AOP could actually fail. In progress as a separate deliverable.
3. 2 print-only references (Ashby 1960, Parfit 1984); 5 record-only references not yet submission-grade.
