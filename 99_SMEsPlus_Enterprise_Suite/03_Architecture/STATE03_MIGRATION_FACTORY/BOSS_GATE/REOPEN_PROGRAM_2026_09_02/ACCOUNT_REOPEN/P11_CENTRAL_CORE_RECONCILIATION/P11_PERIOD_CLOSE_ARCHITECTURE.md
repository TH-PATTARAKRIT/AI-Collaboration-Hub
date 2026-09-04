# P11 — UNIFIED PERIOD CLOSE ARCHITECTURE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Model 11 of 15 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Position

> ## There is no period close. There is a moved date.
>
> **No closer, no close date, no basis, no artefact** — only a lock date advanced. Nothing posts.
> The year's result is **computed at report time** against a current-year-earnings account and is
> **never posted**. The fiscal-year record is a **calendar override, fully mutable, with no state, no
> close and no link to any entry**.

Two of the eight facts are therefore degenerate at close: `F6` finality exists only as a date, and
`F7` provenance does not exist at all.

## 2. What close must reconcile, per process

| Process | What must be true at close | Status today |
|---|---|---|
| `P01` | Received-not-invoiced cleared or disclosed; late bills have a home | **`JT-06` open — no prior-period attribution mechanism exists** |
| `P02` | Delivered-not-invoiced and invoiced-not-delivered disclosed; cost released consistently with revenue | **`JT-04` `NOT DECIDABLE`** |
| `P03` | WIP valued; absorbed vs actual variance recognised | **`UAE-31` absent; `JT-09` open** |
| `P04` | Depreciation run for the period; absorption posted; unabsorbed overhead expensed | **`BLK-07` `HOLD`; absorption path does not exist** |
| `P05` | Unapproved expenses accrued or disclosed | **producer contract `UNKNOWN`** |
| `P06` | **Bank reconciliation complete — this already gates locking, and is the one good pattern in the area** | **works; adopt and generalise** |
| `P07` | Tax return posted; tax lock set (**automatically today, as a side effect**) | `TX-02` |
| `P08` | Draft entries cleared (**a hard lock is blocked by drafts**); statements produced; result transferred | **result transfer `UAE-27` does not exist** |
| `P09` | Analytic subledger agrees with the ledger | **cannot be asserted — analytic is not a subledger of record** |
| `P10` | All schedules released for the period; remaining balance reconciled | **producer contract `UNKNOWN`** |
| Inventory | Valuation summary agrees with the GL **at the closing boundary**, with the posture disclosed | **holds at the boundary only, not continuously** |

**Two of eleven are in a state where close can be asserted.** `P06`'s precondition works;
Inventory's boundary agreement works with a disclosure.

## 3. Close-time defects that cross processes

| id | Defect | Consequence |
|---|---|---|
| `PC-01` | **Generated consequences relocate to the current period when their own period is locked** — `UAE-01` exchange difference, `UAE-03` cash-basis tax | `CONTRA-04`. `UAE-03` **can cross a fiscal year** |
| `PC-02` | **A reversal is re-dated into the first open period if the original's period is locked** — original and reversal can sit in different **years** | Net-zero across two entries becomes non-zero within each year |
| `PC-03` | **Soft locks move backward freely, with no distinct authority required** | Finality is revocable by whoever set it |
| `PC-04` | **The lock exception is granted and revoked by the same role**, optionally scoped to **every** user | `T0-10` `UNRESOLVED`, *wider than registered* |
| `PC-05` | **The hard lock cascades from every parent, irreversibly** | Narrowed by `RV-04` to related companies inside one tenant; still a coupling |
| `PC-06` | **Retroactive cost compensation is sequenced by record creation order, not effective date** | Back-dated entry attributes cost to the wrong period (`L13-01`) |
| `PC-07` | **The fiscal year is keyed to root companies only; child companies are refused** | A company cannot declare its own legal period — a **scope violation** under `SC-04` |

## 4. Positions

| id | Position | Basis |
|---|---|---|
| `PCP-01` | **Period close is a first-class accounting event** (`UAE-26`) with an actor, a date, a stated basis, a checklist result and an immutable artefact | §1 |
| `PCP-02` | **Year-end result transfer is posted** (`UAE-27`), not computed at report time. Retained earnings acquires provenance | §1 |
| `PCP-03` | **Finality is an object, not a date.** Reopening is a separate authorised event with its own record | `PC-03` |
| `PCP-04` | **Granting and revoking a finality exception are separated by authority**, and neither may be scoped to all users | `PC-04` |
| `PCP-05` | **No event is silently re-dated across a period boundary. Denied, or routed to an explicit prior-period attribution event** (`UAE-32`) | `PC-01`, `PC-02`, `TB-04` |
| `PCP-06` | **The close checklist is cross-process and evidence-bearing**: every producing process asserts its own completeness, and the close artefact records which assertions were satisfied | §2 |
| `PCP-07` | **Fiscal year is `COMPANY`-scoped.** Every company declares its own | `PC-07`, `SC-04` |
