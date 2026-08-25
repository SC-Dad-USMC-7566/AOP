# Verification note — K&W 2018 spine claims (R1, R2)

**Date:** 2026-08-06 · **Seat:** Claude Cowork · **Purpose:** clear the two `[UNVERIFIED]` tags in §7 of `AOP_InterventionContract_FourAxis_v0.1` against primary source, before the contract goes to Aster for the §9 falsification pass.
**Source:** Kolchinsky & Wolpert (2018), *Semantic information, autonomous agency and non-equilibrium statistical physics*, Interface Focus 8:20180041.
**Retrieval method — stated honestly:** retrieved via WebFetch of the author's hosted PDF (`artemyk.github.io`); the passages below were extracted and quoted by the fetch pipeline, with specific section/equation/appendix anchors. I did **not** personally render the PDF pages. The anchors are concrete enough (Eq 5.2, Eq 5.14, §5.1.1, §5.2, App. B, a numeric −13.7 bits) to rely on for the contract and the Aster pass; a direct eyeball of those exact lines is a cheap final confirmation before the *paper* cites them.

---

## Claim A — two distinct intervention operations. **CONFIRMED.**

R1 (Memory groups with Drive, not with Boundary/Integration) leans on K&W using two *different* operation types. They do, and they name them.

- **Stored** semantic information — an **initial-state scramble**: `pX0,Y0 ↦ p̂full = pX0 ⊙ pY0` (Eq 5.2), described as "an intervention that destroys all mutual information by transforming the actual initial distribution … to the product initial distribution" (§5.1.1), after which they "run the coupled system–environment dynamics" from both the actual and the product initial distributions.
- **Observed** semantic information — a **dynamics intervention**: "we define interventions in which we perturb the dynamic flow of syntactic information from environment to system, **without modifying the initial system–environment distribution**" (§5.2), via coarse-graining the conditional transition `p̂f(x_{t+1}|x_t,y_t) := p̂f(x_{t+1}|x_t, f(y_t))` (Eq 5.14).
- Explicit distinction: "stored semantic information is derived from the mutual information between system and environment at time t = 0" (§5.1.1) versus "observed semantic information, which is defined via a 'dynamic' intervention" (§5.2).

**Verdict:** confirmed. The contract's two intervention levels are not an analogy imported from elsewhere — they are K&W's own stored/observed split. **Boundary and Integration inherit the stored (initial-state scramble) operation; Memory inherits the observed (dynamic) operation.**

**One nuance the contract must keep (and does).** K&W's *observed* intervention severs the flow from **environment → system** (transfer entropy in). Memory severs the flow from the system's own **past → future**. Same operation *type* (a conditional-dynamics intervention), different channel. The contract's "K&W dynamic-information operation, **adapted**" wording is doing real work — keep the "adapted," and do not claim Memory's estimand is K&W's observed semantic information; it is an adaptation of the *operation*, not the *quantity*.

## Claim B — viability value can be negative. **CONFIRMED.**

R2 (opposite sign does not prove distinct axes; informational scrambles can also raise viability) leans on K&W permitting negative value. They state it directly.

- "The difference can also be negative, which means that the syntactic information decreases the system's ability to exist."
- Worked example: an "anti-chemotactic" bacterium that senses food and swims *away* from it; in App. B its stored value is `ΔV ≈ −13.7 bits`.

**Verdict:** confirmed. An informational correlation can be anti-viable, so scrambling it *raises* viability. Drive does not own the negative side of the sign ledger; sign is an outcome, distinctness is tested by the §5 selectivity matrix.

---

## Effect on the contract

- §7 ledger: **[UNVERIFIED] K&W two operations → VERIFIED** (Eq 5.2/§5.1.1; Eq 5.14/§5.2; stored vs observed).
- §7 ledger: **[UNVERIFIED] K&W signed value → VERIFIED** ("can also be negative"; anti-chemotactic, −13.7 bits).
- R1 and R2 both **hold on primary source.** No structural change to the contract; the grounding is upgraded from recollection to citation, and sharpened by the stored/observed mapping and the past→future-vs-env→system nuance above.
- Remaining source work is Phase-0 prior art (Causal Leverage Density, causal individuality), which is a *novelty* question, not a *correctness* one, and stays open.

*Supersedes the two `[UNVERIFIED]` K&W tags in §7 of the Intervention Contract v0.1. Retrieval via WebFetch extraction; direct page render pending only for the paper's own citation stage.*
