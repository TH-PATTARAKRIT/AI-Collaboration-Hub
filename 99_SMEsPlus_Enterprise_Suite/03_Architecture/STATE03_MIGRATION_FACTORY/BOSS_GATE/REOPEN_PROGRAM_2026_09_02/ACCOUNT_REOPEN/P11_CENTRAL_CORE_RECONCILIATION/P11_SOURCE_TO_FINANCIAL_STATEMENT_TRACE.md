# P11 — SOURCE-TO-FINANCIAL-STATEMENT TRACE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Unified model 3b — the trace the Boss Gate Pack's item 18 depends on.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. The trace, and where each lane breaks

Read left to right. The first **✘** in a lane is where that lane stops being provable.

| Lane | Business source | Operational fact | Valuation | Accounting event | Journal effect | Subledger | Statement line | First break |
|---|---|---|---|---|---|---|---|---|
| Purchase | ✔ | ✔ | **✘ `JT-02`/`JT-03`** | ✔ interface | ✘ `UNK` | ✔ AP | inventory / expense | **valuation** |
| Sales revenue | ✔ | ✔ | ✔ | ✔ interface | ✘ `UNK` | ✔ AR | revenue | **journal effect** |
| Cost of sales | ✔ | ✔ | **✘ `JT-04` `NOT DECIDABLE`** | ✘ | ✘ | n/a | cost of sales | **recognition timing** |
| Returns | ✔ | ✔ | **✘ `JT-05` `NOT DECIDABLE`** | ✘ | ✘ | AR/AP | revenue / COGS | **cost basis** |
| Manufacturing conversion | ✔ | **✘ links 5, 7, 8, 11 `ABSENT`** | ✘ | ✘ | ✘ | WIP `HOLD` | inventory | **the machine dimension** |
| Depreciation — expense | ✔ | ✔ | **✘ `CV-09` two day conventions, one untracked setting** | ✔ | ✔ | asset register | expense | **measurement** |
| Depreciation — absorbed | ✔ | ✔ | **✘ `BLK-07` `HOLD`** | ✘ **path does not exist** | ✘ | inventory | inventory | **the whole path** |
| Employee expense | ✔ | ✔ | ✔ | **✘ contract `UNKNOWN`** | ✘ | AP | expense | **producer contract** |
| Cash settlement | ✔ | ✔ | ✔ | ✔ | ✔ `M-02` | bank | cash / FX | **`T0-05` over-reconciliation unguarded** |
| Tax on document | ✔ | n/a | ✔ | ✔ interface | ✘ `UNK` | tax, **unprotected** | tax liability | **journal effect** |
| Cash-basis tax | ✔ | n/a | ✔ | ✔ `M-03` | ✔ | tax | tax liability | **`DC-07` unmatch reversal unstated** |
| Deferred release | ✔ | n/a | ✘ | **✘ contract `UNKNOWN`** | ✘ | `UNKNOWN` | revenue / expense | **producer contract** |
| Opening position | ✔ | ✔ | ✔ | ✔ `M-01` | ✔ | all | balance sheet | **element 14 — no migration identity** |
| Analytic / management | ✔ | ✔ | derived | derived | n/a | **✘ not a subledger of record** | management reports only | **subledger status** |
| Period result | derived | n/a | n/a | **✘ `UAE-27` no result transfer** | **✘ nothing posts** | n/a | retained earnings | **the close event** |

**15 lanes. By the table's own ✘ test, 3 carry no ✘** — cash settlement, opening position and
cash-basis tax. **By the unresolved-break test, 0 are clear**, because each of those three terminates
in an open tolerance-zero or contract failure. *Corrected per `X4-F12` / `P11-E-07`. **Superseded text, retained so its erasure is detectable:** ~~15 lanes. 2 reach a statement line without an unresolved break~~. The earlier
sentence asserted both at once.* The two named below are — cash settlement and opening
position — and each carries an open tolerance-zero or contract failure at the end of the lane.

## 2. The statement layer's own defect

Even where a lane is complete, the **report definition object** through which it reaches a statement is
scope-mismatched: one undifferentiated model serves `PLATFORM` standard reports and `TENANT`-authored
reports, has **no record rule in any of 6 roots**, and grants **full create/write/unlink** to the
accounting-manager role (`SC-02`, `MCU-04` `CLOSED — VERIFIED DEFECT`). Its sibling model in the same
security file **is** company-scoped — the divergence is inside one module. `filter_multi_company`
**reads as a company control and is a rendering option — the source comment says so** (`T0-09`, third
instance, floor of 30 declarations across 4 files, **never bounded**).

## 3. Statutory presentation constraint

**Off-balance amounts have no statutory presentation surface** — an exhaustive text search of all four
prescribed statements under **ประกาศกรมพัฒนาธุรกิจการค้า แบบ 2** returns no off-balance / memorandum /
*นอกงบดุล* line item (`BLK-04` `CLOSED — EVIDENCE VERIFIED`).

**Consequence for `P04`:** the fully-depreciated-asset internal-usage model (`BD-01` — no cap, no
cut-off, no reduction of residual book value) must not rely on an off-balance presentation. Its
memorandum ledger's bookkeeping standing under the Accounting Act remains `TX-H03`, held.
