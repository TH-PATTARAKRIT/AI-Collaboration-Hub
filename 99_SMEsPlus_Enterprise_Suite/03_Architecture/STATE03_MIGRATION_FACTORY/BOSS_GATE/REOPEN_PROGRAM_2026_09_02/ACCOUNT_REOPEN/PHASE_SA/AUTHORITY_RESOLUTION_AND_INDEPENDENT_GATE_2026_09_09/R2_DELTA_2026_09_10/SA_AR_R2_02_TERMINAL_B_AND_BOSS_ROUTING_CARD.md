# SA_AR_R2_02 — TERMINAL STATE AND BOSS ROUTING CARD

Session `[SMEPLUS-26-09-09-PHASE-SA-AUTHORITY-RESOLUTION-001]` — round 2 (delta)
Branch `architecture/phase-sa-authority-resolution-and-independent-gate-2026-09-09-001`
**Boss is the SOLE FINAL APPROVER. This is not a `PASS`, not a Phase SA closure, and not a decision.**

---

## 1. Terminal state

> # `HOLD — SMEs CORE / SMT — §5 F3 BOUNDED VERIFICATION AND §7 SMT FIRST-LINE CHALLENGE NOT PERFORMED`

Master prompt **Terminal B**. Terminal A was not available: it requires *"material SMEs Core open items
= 0"*, and after the delta that figure is **≥ 3**, not 0 (`SA_AR_R2_01` `AR-R2-F-04`).

**Exact owner:** SMEs Core, with the six named SMTs as first-line challengers.
**Exact blocker:** `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` §5 and §7 make an `F3` bounded
evidence re-read and a per-family SMT disposition **preconditions of any Boss pack**. `0` of `8`
families carry a disposition and the `F3` re-read has not been performed.

**This blocker is not Boss's to clear, and Boss should not be asked to compensate for it** — the current
instruction's own §13 Terminal D names that as an execution failure state.

---

## 2. Why this round did not clear the blocker itself

The work is authorized — but **to the other track, on the other branch, under `SC-*` identifiers**.

This master prompt's §0 authorizes nine items; **SMT first-line challenge and bounded `F3` verification
are not among them**, and §0 closes with *"Do NOT self-declare Phase SA PASS."* Producing `SC-01`,
`SC-02` and `SC-03` here would place another session's deliverables on this branch under the wrong
identifiers and would fork the lineage a third way.

**The standing rule that applies:** never scope a write wider than the read.

---

## 3. The one thing that is genuinely Boss's, and it is not a decision family

Two Boss-authored instructions are live over the same `F1`–`F8` population, and they prescribe
**different routes**:

| | `[…PHASE-SA-AUTHORITY-RESOLUTION-001]` | `[…ACC-PHASE-SA-SMECORE-CONT-001]` |
|---|---|---|
| Boss-authored | `e6d2be32` 2026-09-09 22:46 | `34a46d9b` 2026-09-10 00:34 — **newest in repo** |
| Branch | `architecture/phase-sa-authority-resolution-and-independent-gate-2026-09-09-001` | `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001` |
| Baseline it names | `9d5bc2db` + mainline `3f5d915a` | `9d5bc2db` — **does not contain `afe664c6`** |
| State | **executed, published `afe664c6`, Terminal A** | **authorized, 0 checkpoints executed** |
| Route to Boss | consolidate and escalate `F1`–`F8` now | scrub, verify `F3`, SMT-challenge, *then* escalate |
| Deliverables | `SA_AR_00`–`SA_AR_11` — **complete** | `SC-00`–`SC-06` — **none produced** |

**They are not contradictory on the merits.** The newer one adds two controls the older one does not
require, and defers escalation until they are run. The older one's own §12 already says *"Do not make
Boss answer anything SMEs Core can still close itself"* — the newer one operationalises exactly that.

### `BOSS-ROUTE-01` — which line is canonical?

This is Boss-owned because it is the **scope and sequencing of Boss's own instructions**. No evidence
this session can gather decides it.

| Option | What happens | Cost | Risk |
|---|---|---|---|
| **`ROUTE = SC`** *(SMEs Core recommends)* | Execute `CP-SA-SC-00` → `CP-SA-SC-FINAL` on the scrub branch. `afe664c6` becomes an **input**, not the pack. The `SC` track **must** consume `AR-F-01` (30 → **24**, not 26) and `AR-F-02` (§9, not `EC-07`) or it will re-derive from a superseded baseline | one more round before Boss sees a pack | `F1`–`F8` may **shrink** — `F3` may leave the list entirely |
| **`ROUTE = AR`** | Ratify `afe664c6` as the pack; treat `SC` as withdrawn | Boss decides now | 8 of 8 families reach Boss with **no SMT disposition** and `F3` escalated against §5 — an `SMT Escape` by construction under the newer instruction |
| **`ROUTE = BOTH`** | `SC` executes, then its `SC-06` supersedes `SA_AR_11` at claim level, with lineage preserved | slowest | none identified |

**SMEs Core recommends `ROUTE = SC`**, on three grounds: it is Boss's newest instruction; it is the only
route under which `F3` can leave the Boss list without a Boss decision; and it is the only route that
supplies the SMT disposition the newer instruction makes mandatory.

**Dissent, recorded:** `ROUTE = SC` costs a full round and **may return the same 24 decisions** — the
`SC` scrub tests A–F, and round 1 already executed the closest equivalents (`ALREADY RULED`,
`CLOSABLE BY EXISTING EVIDENCE`) over **189 of 189** refs, one ref per iteration with a positive control,
and closed **0** families that way. The scrub's realistic yield is `F3`, not eight families. A second
dissent: if `ROUTE = SC` is taken, the `SC` track starting from `9d5bc2db` will re-inherit the `F5`
count-by-identifier error that **three rounds have now made**, unless it is directed to consume
`afe664c6` first.

---

## 4. Boss response template

```
BOSS-ROUTE-01 = SC | AR | BOTH
If SC or BOTH: SC track MUST consume afe664c6 (AR-F-01, AR-F-02) as input = YES | NO
```

**Nothing else is asked.** The 24 decisions, 5 acts and `FG-F-06` are **not** re-put to Boss in this
round — they are unchanged at `SA_AR_11` and putting them again without material delta on their merits
would be a repeated Boss question.

---

## 5. Unchanged and carried forward

- **PMO mainline closure `VERIFIED`** — re-measured at head `a20db7a3`, not inherited.
- **Category 3 — PMO `0`, document owner `0`.** SMEs Core is **no longer `0`**.
- **6 vetoes active, 0 discharged, 0 self-discharged.**
- **0 structurally independent passes.** `EC-07` = `0 of 2` if `FG-F-06` = Reading A.
- **`FG-F-06` `READY — UNANSWERED`.** The newer instruction §8 independently requires it to be put
  **last**; holding it is consistent with both tracks.
- `E2E-07` traversable correction preserved · `E2E-04` re-grade remains **withdrawn**.
- No `PASS` / `CERTIFIED` wording. No vendor-copying tokens introduced.
