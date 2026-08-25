# Handoff — AOP prime seat, 1–3 August 2026

**Document ID:** `AOP_Handoff_Prime_20260803.md`
**From:** prime (chat seat), session of 1–3 August 2026
**To:** the next prime session
**Purpose:** resume without re-reading anything. Everything load-bearing is here or pointed at.

---

## Read this first

You are the chat seat. You think, decide, and grade. You do not build. Ben owns the project and makes all decisions; **do not route him decisions the seats can make.** The design constraint he stated explicitly: the workflow must not be so complex it breaks at its weakest link, which is the number of things queued on one person.

**Nobody grades their own homework.** Builder proposes, a different seat checks, OAI attacks, Ben rules. This applies to your own governance work too — the freeze this session got its hash independently confirmed by another seat before it counted.

**Verify against Drive, not against memory or pasted artifacts.** Two separate corruptions were found this session by hashing files nobody had hashed. Size matching is not hash verification. Do the startup block properly; it is a forcing function, not a formality.

**Ben's style:** terse when satisfied, direct, wants pushback. No flattery. If his idea is weak, say so before helping. He uses voice-to-text, so phrasing garbles sometimes — read for intent.

---

## Where things stand

### The live fork — this is what's waiting on Ben

The life-criterion falsification arc was designed, frozen, run through system selection, adjudicated, and attacked by OAI. It produced a three-arm experimental design: KaiABC for the state-memory prediction, an engineered EnvZ/OmpR cycle for the excluded-system attack, and a physical antithetic controller for the ratio sweep.

**None of those experiments exists in the literature. All three require a wet lab. Ben does not have one.**

So the arc cannot deliver a test. Prime's recommendation, argued to Ben on 3 August and not yet ruled on: **pivot from testing the life criterion to publishing the discriminator.** The state-versus-parameter test runs on published closed-form models with no lab, discriminated cleanly across fourteen systems, and answers a question four separate fields are independently stuck on. The life criterion becomes a stated conjecture with a published design for settling it.

The cost, which must not be smoothed over: the life claim stays untested. If Ben rules against the pivot, the alternative is collaborators, which is a different kind of project.

**Do not proceed past this fork without his ruling.**

### What the arc found, and it is more than the arc was for

1. **Canon §11a's discriminator does no work.** Zero of fourteen system rejections turned on subspace autonomy. What discriminated every time was **target-as-state versus target-as-parameter** — does the slow variable appear in the closed-form expression for the regulated target, or is the target a ratio of rate constants? This is a canon change proposal against §11a and it is the most valuable output of the exercise.
2. **Sontag's internal-model theorem cuts against §11a's current wording.** Strictly read, "autonomous with respect to the regulated coordinates" excludes integral feedback — which a published theorem identifies as necessary for adaptation. Prime ruled Reading B; OAI countered with a better **Reading C** (autonomous *zero dynamics*, plus separate intervention, causal readout, viability relevance) and prime conceded. Reading C is the current position. `[Sontag primary not read by prime — verify before folding]`
3. **The criterion's positive class may not contain the cell.** Among well-characterised molecular regulators, the only state-target found was a circadian clock — which stores external time, not a viable set. Prime's dissent from the builder is recorded. Note: prime originally cited "13 of 14" and **OAI audited that count down to roughly six parameter targets, one state target, one undetermined, several never reached.** The substance survives; the base was overstated. Prime inherited the number without auditing it. Don't repeat that.
4. **AOP's distinction is prior art under four names** — settling point, balance point, equilibrium point, absence of an internal model. This is the "don't create when you can cite" outcome the charter asks for, and it is the strategic asset.

### Two canon defects, both open, neither blocking

- **The tracking-relation slot does not exist.** v1.26 §1 (L43) says the tracking relation "enters as part of the declaration **D**, §12″." §12″ enumerates D exactly once, at L592: (S, E, F, P, δt, τ, R, V, I, N). Ten slots, no tracking relation. The one sentence AOP retains of the whole diachronic question points at a slot the canon never defines. Found by prime, 1 August, from the hash-verified master.
- **The v1.27 candidate on Drive is corrupt.** Certified at 255,684 bytes / md5 `998aa87e…` / 851 lines. Actual: 255,885 / `70da21ff…` / 853. Three of Ben's local Downloads paths are spliced into the masthead at line 13, destroying 1,108 characters — including the clause recording the relocation of the life block. The ten content edits are present and correct at their stated lines; damage is confined to the masthead. **Do not place it.** Stripping the three paths should recover the certified build; that has not been done.

### Also open

- Ben must manually trash: the duplicate work order (`1WPywfir9ywmjL6qVXG5qLdK0X6ifRe_h`), the v0_1/v0_2 interim deliverables, and the 62-byte dud in Canon Development (`14v4FufKQH1S9hdUrrMmtEjgLf5YVz6EP`). The connector cannot delete.
- Claude Science's project context carries **Charter v1.0**; Drive carries **v1.2**. Refresh it.
- Cowork is queued for an independent bibliographic pass over the Gate 1 deliverables. Two author bylines were fabricated and five unsourced surname strings caught in total. Science disclosed rather than repaired silently — correct behaviour — but the base rate is not zero and these files were about to become a freeze substrate.
- **P2's reassignment off KaiABC is an amendment, not a reading.** Prime initially filed it as a declared reading; OAI correctly pointed out the selection order requires clearing all four screens. Record it properly, pre-data.
- The AOP→Ladder brief of 1 August is deposited and answered. The Ladder may import the decoupled-reference *architecture* as a floor (canon, synthesis grade); it may **not** import the life *criterion* (frontier, non-canon draft). That distinction is the whole point of the brief.

---

## Drive — verified this session

| Object | ID | Bytes |
|---|---|---|
| Canon master v1.26 | `1MN7rhZExgNSv3mv2h92GqSjUzHSzgpWn` | 254,046 — md5 `54ceb3772e29f25c6e139b703d550d59`, 851 lines ✓ |
| v1.27 candidate (**corrupt**) | `1UaBvTmUYUmIXY6AkVfh2JgexAQIHyBKG` | 255,885 — md5 `70da21ff9be7720a41fee7b1dfb0c880` |
| Life-architecture follow-on (non-canon) | `1pP-phsxzzrSIT5GmjCxi7iYmyBr9tyKR` | 38,799 |
| **Disposition rule, FROZEN** | `1-HkXf58z-UWnYVkT1mcNR3_y2hIi3PAy` | 6,824 — md5 `b7eebcfd5a371a78b33a5fe230d52554`, frozen 2026-08-01 19:52:57 −0700 |
| Work order | `11YYUfUeisfzS3Wjv5sXG9TACmf5O6csQ` | 9,321 |
| Selection order | `1pqmKxzablE53V4IXpW8inq-1EgT8rXfH` | 8,083 |
| Selection report v1.0 | `1TMyzJW7TPYQ_uq8fHmysTdc4jXf9KKUJ` | 42,145 |
| Rejection log v1.0 | `1G30cFWNA5VeAmbDkx0Lu69hi5RSewxIo` | 6,686 |
| Prime's adjudication | `16Ev9APq8gKDClQwbwhRXv4dQUD-JgK-h` | 10,896 |
| OAI attack | `13NjxqrOHXzDn99ElGQ2zkCaVk0XzvmwD` | 22,836 |
| AOP→LAD brief | `1vmLE0r0FAd4dkoj5ukhf8tnkPgcNl5yL` | 13,888 |

**Folders:** canon master `1V_ufLQWTXVrUmVVGVth2ExFqXrBahw_J` · Canon Development `1Yta-E7kdOS69IboXR3_CT5-aLcxB8XA4` · Work Orders `10S59I_-xmcP1rdCV1xMygwJDB0ZALRTr` · AOP Handoffs `1iWT8I1b-56QXlXRR3CngpdfNNfhaV7bM`

---

## Tool notes that will save you an hour

- Large Drive downloads land at `/mnt/user-data/tool_results/*.json`. Decode: `json.loads(d[0]['text'])` → `base64.b64decode(inner['content'])` → write to `/home/claude/` → hash. Files under ~40 KB come back inline as base64 you cannot decode without pasting — use `read_file_content` for those instead, which returns plain text.
- `create_file` works reliably with `textContent` + `disableConversionToGoogleType: true` + `contentMimeType: text/markdown`. Verify by comparing the returned `fileSize` to your local byte count. Shell `$(cat ...)` expansion in tool parameters does **not** work.
- `read_file_content` returns empty for some markdown written with conversion disabled — fall back to `download_file_content`.
- Folder listing: `parentId = '[id]'` with `excludeContentSnippets=True`.
- `fullText contains` loose-matches badly. Never use it as an existence test inside a large document; download and diff.
- Line counts: `str.split("\n")`, not `wc -l`, for comparability with existing change sets.

---

## A note to the next session

Ben has been running this project for weeks with real discipline, and the discipline is what produced everything above. The corruption, the missing slot, the discriminator that discriminated nothing — none of that was found by being clever. It was found by hashing files somebody assumed were fine and reading text somebody assumed said what it said.

He will tell you when you are wrong, and he means it kindly. Do the same for him. He does not want agreement; he has said so directly and repeatedly. The most useful thing you can do in your first hour is pull the live canon and confirm it by hash, because at least three sessions have opened on a stale assumption.

Good luck. It's genuinely good work.

---

*End of `AOP_Handoff_Prime_20260803.md`.*
