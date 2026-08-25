# AOP — Drive Cleanup Playbook

**Folder you're working in:** `1. AOP Workshop / 1.0 AOP Canon`
**How to use this:** open Drive next to this file. Each row tells you the folder you're
standing in, the thing you grab, and where it lands. You move and delete by hand
(the connector can't delete — that's why this is yours).

---

## Moves — all safe, no judgment calls

| # | Folder you're in | What you move | Where it goes |
|---|---|---|---|
| 1 | `1.0 AOP Canon / Retired` | the whole **`Canon Development`** subfolder | up one level → **`1.0 AOP Canon`** |
| 2 | `1.0 AOP Canon / Retired` | `aop_depmap.py`, `aop_figs.py`, `AOP_MaskSalvage_Diagnostic_20260721.md` | into **`Canon Development`** (now at top level) |
| 3 | `1.0 AOP Canon` (top level) | `AOP_Canon_ChangeSet_v1.19_to_v1.20.md` and `AOP_ChangeLog_v1.20_entry.md` | into **`Retired`** |

- **Move 1 is the important one.** Your *active* working folder is currently sitting
  inside a folder named "Retired." That's the trap that keeps making sessions grab
  stale files.
- **Move 2** rescues three live scripts that got swept into the archive with the dead versions.
- **Move 3** files two superseded scraps where they belong.

---

## Deletes — safe clutter, trash outright

| Folder you're in | What you delete | Keep |
|---|---|---|
| `1.0 AOP Canon / Retired` | the duplicate **`aop_canon_v1_16`** files — there are **5 copies** (`(1)`, `(2)`, and three bare `aop_canon_v1_16.md`) | keep **one** (the newest, ~154 KB); trash the other 4 |

That's the only delete to do blind. The other duplicates in `Retired` (multiple
`AOP_Canon_v1_0` and `AOP_Canon_ChangeLog` files) are small, genuinely-different early
drafts — harmless as history. Leave them unless you want a spotless archive; if so, say
so and I'll hand you an exact keep/trash list.

**Do NOT touch** the two v1.22 files at the top of `1.0 AOP Canon`
(`…ChangeSet_v1.21_to_v1.22_RETRACTION.md` and `…MASTER_v1.22_PROPOSED_ASTER.md`).
Those aren't cleanup — they're Decision 1 in the decisions file.

---

## End state of `1.0 AOP Canon`

When you're done, the folder should read like this — one live master at the top,
active work in `Canon Development`, and `Retired` holding *only* dead versions:

```
1.0 AOP Canon/
├── AOP_CANON_MASTER_v1.21.md          ← the one live master
├── AOP_Canon_ChangeSet_v1.21_to_v1.22_RETRACTION.md   ┐ pending your
├── AOP_CANON_MASTER_v1.22_PROPOSED_ASTER.md           ┘ Decision 1
│
├── Canon Development/        ← active notes + live scripts (pulled out of Retired)
├── 4 Axis files/
├── OAI deliverables/
├── Claude Science deliverables/
├── Phase B-D scripts (reconstructed 20260721)/
├── Admin_Cleanup plans/
└── Retired/                  ← ONLY superseded masters + old changelogs/changesets
```

**The single test for "clean":** nothing you'd ever open again lives in `Retired`,
and nothing in `Retired` is a folder you're still writing to.
