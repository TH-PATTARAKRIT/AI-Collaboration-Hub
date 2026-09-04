# 13 — P03 PERIOD CLOSE AND TOLERANCE BOUNDARIES

**LAYER 2 — AUDIT QUARANTINE.** Very Expert extension: *Period Close*.

---

## 1. What a manufacturing period close must achieve

1. Every MO open at period end carries a WIP value on the balance sheet.
2. Every MO closed in the period has relieved WIP entirely.
3. The production account nets to zero, or its balance is explained.
4. Unallocated fixed overhead is expensed in the period incurred — TAS 2 ¶13, and Boss
   decision `BD-02` as recorded in `ASSET_DR_CONTINUATION/22` §2.

## 2. What the reference product achieves

| # | Achieved? | Why |
|---|---|---|
| 1 | **Partly, and transiently** | Only if the WIP wizard is run, with a correct date, on a correct MO selection. The entry reverses the next day — `03` §3 |
| 2 | **No** | `DC-03` and `DC-04` leave residues by construction |
| 3 | **No** | And worse: the two residues have opposite signs and net in one account — `10` §4 |
| 4 | **Not possible** | No overhead pool exists — `07` §5 |

**Manufacturing period close is not achievable from the reference product's own outputs.**
`FACT VERIFIED`.

## 3. The close-blocking properties, ranked

| # | Property | Effect on close |
|---|---|---|
| 1 | The production account carries two opposite-signed residues from unrelated causes | A near-zero balance is not evidence of correctness — `10` §4 |
| 2 | The labour entry uses the posting date, not the event date | Cut-off cannot be enforced — `DC-09` |
| 3 | WIP is a reversing accrual with no MO detail | The WIP balance cannot be substantiated MO by MO — `03` §3 |
| 4 | The WIP accrual values components at standard while consumption is FIFO/average | The accrual does not predict the reversal it accrues for |
| 5 | The WIP wizard's amounts are user-editable with no record of the edit | `08` §3 |
| 6 | Re-running the wizard for one date creates a second entry | `06` §4 |

## 4. Close procedure implied by the above — `DESIGN CANDIDATE`

Stated as what SMEsPlus must be able to do, not as a design:

| # | Requirement |
|---|---|
| `R-11` | WIP must be a **derived, MO-level, queryable position**, not a manually posted accrual |
| `R-12` | Conversion cost must post to the **event's** period, not the operator's |
| `R-13` | The production account must reconcile to zero at close, with any balance decomposed by cause |
| `R-14` | Unallocated fixed overhead must be identified and expensed — which requires the absorption model, which requires `BLK-07` |

## 5. Tolerance boundaries — `Tolerance = 0`

Per `PROJECT_CONSTITUTION.md` v1.4 principles 11 and 13, financial-integrity boundaries may
be designated `Tolerance = 0` and must not be averaged into an overall defect percentage.
P03 designates the following, each with the evidence that makes it a boundary:

| ID | Boundary | Tolerance | Evidence |
|---|---|---|---|
| `TZ-01` | Machine-hours costed must equal machine-hours occupied | **0** | `DC-01` |
| `TZ-02` | Conversion cost capitalised must equal conversion cost relieved, per MO | **0** | `DC-03`, `DC-04` |
| `TZ-03` | The absorption credit must never land on a COGS account | **0** | `DC-07` |
| `TZ-04` | Company-dependent accounts must resolve in the transaction's company | **0** | `DC-11` |
| `TZ-05` | Capitalisation and relief of one economic event must share a period | **0** | `DC-09` |
| `TZ-06` | Analytic conversion cost must reconcile to ledger conversion cost | **0** | `DC-05` |
| `TZ-07` | A cost with no measurement must be distinguishable from a measured cost | **0** | `DC-08` |
| `TZ-08` | By-product cost shares summing to 100 must not silently zero the main product's cost | **0** | `09` §3 |

**Eight tolerance-zero boundaries.** None is currently met by the reference product; that
is a statement about the reference product, and a specification of what any SMEsPlus
manufacturing costing design must satisfy before it can be considered.

## 6. Performance / speed budget

`PROJECT_CONSTITUTION.md` principles 14–16 require a performance budget for every
applicable controlled flow. **P03 declares none**, and states why: no SMEsPlus
manufacturing flow exists to budget for, and `01` §6 establishes that manufacturing is
absent from the target process and specification baseline entirely.

Recorded as `UNR-P03-03`: *the performance budget for P03 flows cannot be set until the
process is admitted to the target baseline.* This is a gap in the P03 package and is
declared rather than papered over.
