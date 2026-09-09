# SA_AR_R2_03 — BOSS RULING ON `BOSS-ROUTE-01`

Session `[SMEPLUS-26-09-09-PHASE-SA-AUTHORITY-RESOLUTION-001]` — round 2 (delta)
Ruling received 2026-09-10, after the Terminal B report at `b1f07939`.
**This records a Boss ruling. It approves no decision family, discharges no veto, and closes no phase.**

---

## 1. The ruling

```
BOSS-ROUTE-01 = SC
SC track MUST consume afe664c6 (AR-F-01, AR-F-02) as input = YES
```

## 2. What it settles

The canonical Phase SA line is `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`, on branch
`architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`.

- `afe664c6` — this session's Boss Decision Gate Pack — is **an input to that track, not the pack**.
  It is **not withdrawn**; its findings stand and its lineage is preserved.
- The 24 decisions, 5 acts and `FG-F-06` are **not put to Boss now**. They return only through
  `SC-06`, after the §4 scrub, the §5 `F3` bounded re-read and the §7 SMT dispositions.
- The blocker named at Terminal B — `0 of 8` SMT dispositions and the unperformed `F3` re-read —
  is now routed to its owner rather than left open.

## 3. What it does not settle

`F1`–`F8` remain **undecided on their merits**. `FG-F-06` remains `READY — UNANSWERED`. Six vetoes
remain active and none is discharged. Structurally independent passes remain **0**.

## 4. Binding intake for the `SC` track

Boss ruled intake **YES**. The `SC` track forks at `b8666f14`, does not contain `afe664c6`, and names
`9d5bc2db` as its parent. Before deriving `F1`–`F8` it **must** consume:

| Finding | What it corrects | Consequence if skipped |
|---|---|---|
| **`AR-F-01`** | the parent's *"26 surviving Boss decisions"* counts `F5` by identifier while `F5`'s own card counts by decision. Corrected on two agreeing shapes: **30 candidates → 24 decisions** | the `F5` count-by-identifier error repeats a **fourth** time |
| **`AR-F-02`** | the single Phase SA citation of `SMEPLUS-DR-EXIT-8C-001` applies **§9** (`PROVISIONAL / NON-CANONICAL`), not §4 or `EC-07` | `FG-F-06` Reading A is presented stronger than the evidence supports |
| `CP-SA-AR-00` re-measurement | PMO closure verified at head `a20db7a3`, not `3f5d915a` | a stale mainline SHA is inherited |
| `AR-I-01` · `AR-I-02` · `AR-R2-I-01` · `AR-R2-I-02` | four published instrument failures and their controls | the same sweep defects recur |

## 5. Terminal state of this session

# `CLOSED — ROUTED`

`[SMEPLUS-26-09-09-PHASE-SA-AUTHORITY-RESOLUTION-001]` ends here. Its Terminal B blocker is routed to
the `SC` track under Boss's ruling. **Execution continues on the `SC` branch under the `SC` session
identifier**, not under this one.
