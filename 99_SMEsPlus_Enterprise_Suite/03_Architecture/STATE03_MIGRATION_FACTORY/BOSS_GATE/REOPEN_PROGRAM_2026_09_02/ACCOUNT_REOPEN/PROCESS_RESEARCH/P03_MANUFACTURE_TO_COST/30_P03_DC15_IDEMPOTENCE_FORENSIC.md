# 30 — P03 DC-15 IDEMPOTENCE FORENSIC

**LAYER 2 — AUDIT QUARANTINE.**

---

## 1. Authoritative definition

`DC-15`, from `25` §3: `_post_labour` writes the resulting entry line onto every
contributing time log — `mrp_account/models/mrp_production.py:106` —
`workorders[line.account_id].time_ids.write({'account_move_line_id': line.id})` — and
**never reads it back as a guard.**

## 2. What prevents a second post — every candidate control, tested

| Candidate control | Present? | Evidence |
|---|---|---|
| Idempotency key | **No** | no such field on the production, work-order or time-log model |
| Posted flag on the manufacturing order | **No** | `_post_labour` tests no flag of its own |
| Accounting-event identity | **No** | Account Wave A already records *no event identity* as a core-ledger gap; it recurs here |
| Journal link read as a guard | **Written, never read** | `account_move_line_id` — 4 occurrences: 1 declaration (`mrp_account/models/mrp_workcenter.py:27`), 1 write (`:106`), **2 reads, both in `tests/`** |
| Database unique constraint | **No** | the field is a plain many2one; no `_sql_constraints` on the productivity model reference it |
| Runtime guard in the function | **Two, but neither is idempotence** | `:74` valuation-mode test; `:86` zero-amount test |
| State guard at the call site | **Yes — and this is the only real control** | `mrp_account/models/mrp_production.py:110` — `self.filtered(lambda mo: mo.state == 'done')._post_labour()` |

## 3. The only control that exists, and what it is worth

`_post_labour` is invoked from exactly one place: `_post_inventory`, filtered to orders in
state `done`.

So a second post requires an order to pass through `done` twice. That is a **state-machine
property of the manufacturing order, not an idempotence control on the accounting entry.**
The distinction is the whole finding:

> The entry is protected by where it happens to be called from, not by anything about
> itself. Any future call site — a partial-completion accrual, a re-post utility, a data
> fix, a migration script — inherits **no protection at all**, and the marker that would
> have provided it is already being written and ignored.

## 4. Reachability — executed, and bounded

| Scenario | Result |
|---|---|
| Same order processed twice | Requires re-entry to `done`. Not demonstrated from the code read; **not disproved either** |
| Retry after failure | The entry is created and posted inside the same transaction as `_post_inventory`; a rollback removes both. **Not a duplication route** |
| Concurrent call | No advisory lock and no unique constraint were found; concurrency is `UNRESOLVED` — it needs runtime tracing, which this session may not perform |
| Post after partial completion | Backorders are **separate order records** with their own work orders, so each posts its own entry. Not a duplicate |
| Post after reversal | No reversal path for the labour entry exists at all — `07` §4 |
| **Post at all, in any readable deployment** | **NO.** `workcenter_cost` is zero on every order in every readable database, so `:86` `is_zero → continue` fires and the entry is **never created** |

## 5. Disposition

The directive requires exactly one status. The code question and the deployment question
have different answers, and collapsing them would misreport one of them, so the primary
classification is stated on the durable property and the bounded one is recorded beneath
it.

> **`DC-15` — NO IDEMPOTENCE CONTROL VERIFIED.**
>
> A marker sufficient to provide idempotence is written on every contributing time log and
> is never read. The only protection is the caller's state filter, which is a property of
> the call site and not of the entry. `FACT VERIFIED` as to the absence.

**Bounded sub-result, recorded separately and not merged into the above:**

> **Second post UNREACHABLE in all three readable deployments** — not because a control
> prevents it, but because the entry is never created in the first place (`26` §3).
> Reachability in a deployment that actually uses work centres remains **UNRESOLVED —
> RUNTIME EVIDENCE REQUIRED** (`UNR-P03-06`).

**Why not "SECOND POST UNREACHABLE — VERIFIED".** That status would be read as *the system
prevents duplication*. It does not. It currently has nothing to duplicate. Reporting an
absent control as a verified safeguard is the precise error
`smeplus-deep-research-negative-claim-standard` exists to prevent.

## 6. Requirement generated

`R-16`: **every accounting entry SMEsPlus generates from a business event must carry an
event identity that is written *and read* as the duplication guard.** `DESIGN CANDIDATE`.
This is the manufacturing instance of the Account Wave A *no event identity* gap and must
be solved once, at the ledger, not per process. Routed to P08 — `41` §4.
