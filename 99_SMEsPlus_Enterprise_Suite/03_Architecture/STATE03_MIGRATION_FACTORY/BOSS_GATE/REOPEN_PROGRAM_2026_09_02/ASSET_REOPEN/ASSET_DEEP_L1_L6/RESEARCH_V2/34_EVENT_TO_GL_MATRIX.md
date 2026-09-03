# 34 — EVENT-TO-GL MATRIX
**LAYER 2 — AUDIT QUARANTINE**

Required matrix I (§82), §51. Column set as mandated.

| Event | Source module | Source object | Operational effect | Financial effect | Debit | Credit | Analytic | Off-balance | Evidence |
|---|---|---|---|---|---|---|---|---|---|
| **Asset acquisition** | accounting | vendor bill | none | The bill's own entry capitalises the cost | Fixed asset | Payable | From the bill line | No | `FV` `SRC-02` |
| **Asset creation** | asset | asset | none | **none** | — | — | inherited to the asset | No | `FV` `SRC-02` |
| **Asset confirm** | asset | asset | Custom: equipment status flipped | **The entire remaining board is posted** | see Depreciation | see Depreciation | per line | No | `FV` `SRC-01` |
| **Depreciation** | asset | journal entry | none | Expense recognised, carrying amount reduced | **Depreciation expense** | **Accumulated depreciation** | **on both lines** | **Forbidden by field domain** | `FV` `SRC-02` |
| **Deferred-revenue variant** | asset | journal entry | none | Signs inverted | Accumulated | Expense/revenue | both lines | No | `FV` `SRC-02` |
| **Re-evaluate upward** | asset | wizard | none | Carrying amount increased; **a child asset is created and confirmed** | Gross-increase asset account | Counterpart account | copied from parent | No | `FV` `SRC-03` |
| **Re-evaluate downward** | asset | wizard | none | Carrying amount reduced, **as a value change** | Depreciation expense | Accumulated depreciation | inherited | No | `FV` `SRC-03` |
| **Change duration / residual / method** | asset | wizard | none | Catch-up entry, then rebuild | see Depreciation | see Depreciation | inherited | No | `FV` `SRC-03` |
| **Pause** | asset | wizard | none | Catch-up entry to the pause date | Depreciation expense | Accumulated depreciation | inherited | No | `FV` `SRC-01` |
| **Resume** | asset | wizard | none | **No entry.** Calendar shifted, board rebuilt | — | — | — | No | `FV` `SRC-03` |
| **Maintenance request raised** | maintenance | request | Tracked; may block work-centre capacity | **NONE** | — | — | — | — | `FV` `SRC-10` `VG` |
| **Maintenance completed** | maintenance | request | Stage closed; MTTR updated | **NONE** | — | — | — | — | `FV` `VG` |
| **Equipment usage** | — | — | **Not recorded** | **NONE** | — | — | — | — | `VG` |
| **Machine idle** | — | — | **Not recorded** | **NONE** | — | — | — | — | `VG` |
| **Breakdown** | maintenance | request | Corrective request; capacity blocked | **NONE** | — | — | — | — | `FV` `VG` |
| **Work order duration recorded** | manufacturing-acct | work order | Duration logged | Analytic only | — | — | **Analytic line from the work centre's distribution** | No | `FV` `SRC-14` |
| **Manufacturing order completed** | manufacturing-acct | production order | FG received | Work-centre cost absorbed into FG value | Stock valuation / input | **Work centre expense account** (or the product's) | via the moves | No | `FV` `SRC-14` — **real-time valuation only** |
| **FG sold** | stock accounting | delivery + invoice | Goods out | COGS recognised | COGS | Stock valuation | product/partner | No | `FV` |
| **Fully depreciated** | — | — | **No event.** Nothing fires | **NONE** | — | — | — | — | `VG` — `10` §3.2 |
| **Post-depreciation usage** | — | — | **Does not exist** | **NONE** | *(proposed: internal usage cost)* | *(proposed: internal usage offset)* | *(proposed)* | **Both, proposed** | **`DC`** — `10` §3.2 |
| **Asset sale** | asset | wizard + customer invoice | **Equipment intended to deactivate — does not** | Derecognition with proceeds | Accumulated depreciation; proceeds account; **loss** if any | **Fixed asset (full gross cost)**; **gain** if any | on every line | No | `FV` `SRC-01`; equipment `CT` |
| **Asset disposal** | asset | wizard | as above | Derecognition, no proceeds | Accumulated depreciation; loss | Fixed asset (gross) | on every line | No | `FV` `SRC-01` |
| **Asset scrap** | — | — | **No dedicated event** | — | — | — | — | — | `VG` — disposal is the nearest |
| **Asset cancel** | asset | asset | none | **Every posted entry reversed** | Accumulated depreciation | Depreciation expense | reversal inherits | No | `FV` `SRC-01` |

## Observations

1. **Depreciation is the only routine GL event the asset domain produces.**
   Everything else is a one-off at a lifecycle boundary.
2. **Six operational events produce no GL effect at all** — maintenance raised,
   maintenance completed, usage, idle, breakdown, full depreciation. Five of the six
   are not even recorded as data.
3. **Only one row in the whole matrix connects a machine to product cost**, and it
   connects the **work centre**, not the machine, and at a **manually typed rate**.
4. **The off-balance column is empty everywhere except the proposed row**, and the
   product **forbids** off-balance accounts on the three asset accounts (`04` §2.5).
   The Boss's management ledger therefore cannot attach to the asset record and
   needs its own posting mechanism.
