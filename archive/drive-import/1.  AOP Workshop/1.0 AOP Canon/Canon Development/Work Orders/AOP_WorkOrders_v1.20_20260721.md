# AOP — Parallel Work Orders (post-v1.20 push)

**Issued by Prime, 21 July 2026.** Canon baseline: `AOP_CANON_MASTER_v1.20.md` (Canon folder
`1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J`, 201,962 bytes). Four lanes, one mission each, on separate
objects so no two agents touch the same artifact. Governing rule: builder proposes → a different
party checks → critic attacks → Ben decides. Nobody grades their own homework.

All deliverables land in **Canon Development** (`1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4`) as PROPOSALS.
Nothing folds to the Canon master without Prime verification + Ben sign-off.

## Lane assignment

| Agent | Layer / object | Mission | Deliverable (Canon Development) | Status |
|---|---|---|---|---|
| **Claude Science** | syntactic layer (Φ_MIP) | Build the time-extended moving-MIP, analytically | `AOP_MovingMIP_Build_proposal_20260721.md` + `phaseE_movingMIP.py` | ISSUED |
| **Cowork** | semantic layer (mask) | Mask-salvage diagnostic: does the well-defined region overlap the informative region | `AOP_MaskSalvage_Diagnostic_20260721.md` + `mask_salvage.py` | ISSUED |
| **OAI (ChatGPT)** | integrity red-team | Attack star reconciliation, D→I / arXiv:2410.13375 dependency, and the "one item left" self-assessment | `AOP_RedTeam_v1.20_20260721.md` (Ben places if OAI can't write Drive) | ISSUED |
| **Prime** | coordination + verification | Provenance audit of lost-parameter numbers; two-master diff; 14:14 touch; integrate all outputs | `AOP_ProvenanceAudit_v1.20_20260721.md` | IN PROGRESS |

Independence check: moving-MIP (syntactic) and mask salvage (semantic) are independent objects,
neither gates the other → Science and Cowork run fully parallel. OAI attacks existing canon only,
touches neither build. Provenance stays with Prime (verification lane), not OAI.

## Prime housekeeping flags (open)
- Two v1.20 masters: clean copy in Canon folder (201,962 B) vs staging copy in dev tree
  `1_9tnN03DpwbF9MMb_dMWxFq3DOK6BwTm` (201,844 B). 118-byte diff — handoff's "byte-identical"
  claim is false. Diff before trusting. Do NOT fold from the staging copy.
- Canon master modifiedTime 14:14 21 Jul, later than all other deposits — confirm whether content
  edit or metadata touch.

## Verbatim prompts issued (durable record for anti-drift)

### Claude Science
See response of 21 Jul. Mission: analytic time-extended moving-MIP. Charter discipline applies:
cite don't claim, verify primary, analytic over estimated, grade every claim, no retired-framework
vocabulary. Output is a proposal; Prime verifies before any fold.

### Cowork
See response of 21 Jul. Mission: mask-salvage overlap diagnostic. Same charter discipline. Output
is a proposal; Prime verifies.

### OAI
See response of 21 Jul. Mission: red-team the three conceptual soft spots. Find holes, fix nothing.

## Status protocol
Prime checks Canon Development on Ben's prompt. An artifact counts as "delivered" only when it is on
Drive with the specified filename. Not on Drive = does not count.
