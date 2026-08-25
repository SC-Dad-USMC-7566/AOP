# Change note — AOP Canon v1.27 residual sweep (C-1 / C-3), pre-freeze

**Order:** Ben (chat seat), 2026-08-06 — "make the necessary corrections and then freeze."
**Seat:** Claude Cowork (execution). Built here; not self-certified. The underlying v1.26→v1.27 fold was independently verified earlier this session (separate verification report); these are three residual edits applied on top of that verified fold.
**Status:** PROPOSAL / stamp-ready candidate. **Not stamped.** Ben places and stamps the master per §9.

## Provenance and integrity

| Item | Value |
|---|---|
| Base | `AOP_CANON_MASTER_v1.27.md` (the verified clean fold, "artifact B"), Drive `1mnX6Y8frvAkl8rpH3aP2OR27jriGVel-` |
| Base md5 | `998aa87e0927f84ae6ea1676ebe8ca93` — the changeset-declared v1.27 output; verified this session |
| Base size / lines | 255,684 bytes / 851 lines |
| Output | this candidate (`AOP_CANON_MASTER_v1.27_C1C3swept_stampready_20260806.md`) |
| Output md5 | `43257601e39489f92a03cbcd64165d43` |
| Output size / lines | 255,714 bytes / 851 lines (Δ +30 bytes; no line inserted or deleted — every edit within-line) |
| Method | 4 exact-string, count-asserted replacements across 3 lines; each verified to hit exactly once |

## The edits — all completing the Edit-4 "floor → positivity" correction the fold began in §4

- **L17 (Abstract), instance 1:** `dissipation forces a floor on predictive memory` → `dissipation forces strict positivity of predictive memory`. The word "floor" asserts a lower bound E ≥ f(σ); the fold's §4 correction proved no such bound exists, so the abstract otherwise contradicted §4.
- **L17 (Abstract), instance 2:** `the Drive floor forces no stored time-asymmetry` → `the Drive positivity forces no stored time-asymmetry`. Same result named consistently. The true negative "no floor on stored complexity" later in the same line is correct and was left untouched.
- **L236 (domain-map row):** `predictive-memory floor` → `predictive-memory positivity`.
- **L393 (Figure 5, flame profile) — C-3:** `sharp boundary, negligible memory` → `sharp boundary, shallow, short-lived memory`. Aligns with the fold's L40 flame correction and §11 L395 ("its memory is … not zero … shallow and short-lived").

## Invariants (base vs candidate) — recomputed independently, not taken from prose

- Lines: 851 = 851. Exactly three lines differ: **{17, 236, 393}**.
- References section: **byte-identical** (60,983 bytes).
- Numeric cites `[n]`: 48 = 48. `[deposited]`: 5 = 5. Grade tags theorem/corollary 11, conditionally-forced 10, constructed-counterexample 3 — all unchanged. `[SYNTHESIS]` 1 = 1.
- `floor` substring: 43 → 40 (−3: the two L17 D→M namings + the L236 label; L393 removed "negligible," not "floor").

## Consciously retained (per Ben's "freeze here" ruling, 2026-08-06)

Four further "floor" mentions name the D→M result but sit beside its correct statement (σ>0 ⇒ E>0, or reach-limited-to-E); **none re-assert the disproven magnitude bound.** Left deliberately, recorded here so the frozen record shows they were seen, and carried as cleanup for the Synthesis Draft rebuild:

- **L13** — the changelog line; history describing prior versions, not a live assertion.
- **L194** — "the memory floor E ≥ 0, within its regime"; stale label (a full correction would also flip ≥ to >).
- **L399** — "the D→M floor σ > 0 ⇒ E > 0" (plus two more in-line); label stale, content correct.
- **L594** — "any memory floor derived from it"; generic / hypothetical.
- **L726** — "the D→M memory floor is bounded to predictive memory"; label stale, content correct.

(The TUR "floor-type" edges, the gravitational "Integration floor," the bedrock "hard floor," and every "no floor on X" negative are correct as written and were never in question.)

## Remaining step — Ben, per §9

Stamp the masthead (L13): `version 1.26 · compiled 25 July 2026` → `version 1.27 · compiled 06 August 2026`, and add a v1.27 changelog entry. Proposed entry, edit freely:

> v1.27 completes v1.26's red-team remediation of the D→M edge: strict positivity replaces "memory floor" throughout §4, the abstract, the domain map, and the §11 flame profile (the edge forces non-i.i.d.-ness, not a magnitude bound); the §4 proof is completed; the past–future split convention (present-in-past) is stated and shown necessary; Figure DM(b)'s coarse-graining caption is narrowed to the case computed; and the §1↔§11 flame-memory contradiction is repaired. No new science.

Then place as the frozen master. This candidate's content hash (`43257601…`) will change once the masthead is stamped — expected; **this note is the provenance bridge** from the changeset-declared v1.27 (`998aa87…`) to the frozen record.

## Drive hygiene note

Freezing v1.27 leaves three v1.27 master-named files on Drive. Recommend keeping only the stamped one and trashing the other two to end the proliferation:
- `AOP_CANON_MASTER_v1.27_candidate.md` (`1UaB…yBKG`) — **corrupt** (201-byte stray Finder-path paste in the masthead). Trash.
- `AOP_CANON_MASTER_v1.27.md` (`1mnX…Vel-`, and its duplicate `1jnq…xty_`) — the clean pre-sweep fold; superseded by this swept candidate once stamped.

*Built by Claude Cowork, 2026-08-06. Not self-certified; the three edits are count-asserted and the invariants above are independently recomputed. Authorizes no further canon change beyond the three edits listed.*
