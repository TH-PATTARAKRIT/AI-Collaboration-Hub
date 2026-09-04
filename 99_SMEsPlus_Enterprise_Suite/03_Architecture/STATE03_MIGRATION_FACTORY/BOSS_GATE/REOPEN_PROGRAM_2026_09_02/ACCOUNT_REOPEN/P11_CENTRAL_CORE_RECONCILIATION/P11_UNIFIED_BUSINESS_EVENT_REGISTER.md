# P11 — UNIFIED BUSINESS EVENT REGISTER

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Model 1 of 15. Classification per `P11_SOURCE_LINK_REGISTER.md` §2.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. Declared population — read this before using any count in this file

| Dimension | Declaration |
|---|---|
| **POPULATION** | Every business event **named in a `PEER-PUBLISHED` artefact or a `BOSS-APPROVED` control** listed in `P11_SOURCE_LINK_REGISTER.md` §3–§4 |
| **PATTERN** | Extraction from: Wave A `05` §1 producer table (18 rows); Wave A `07` accounting-event register; Wave A `08` Part 2 producer table (15 rows); Inventory R4 `16` handoff map (10 material + 9 `INV-OWNED`); Inventory R4 `17` §4 twelve Joint decisions; Asset `08` 19-link chain; `BC-01` 22-scenario baseline |
| **PATH SET** | The 21 packages at the SHAs in `P11_SOURCE_LINK_REGISTER.md` §4 |
| **UNIT** | One business event — *an occurrence in the business, before any accounting question is asked* |

> ### The denominator is NOT the business.
> This register enumerates **44** business events. That number is a count of what the **published
> evidence names**, not a count of what the business does. The correct denominator — every economic
> occurrence in a Thai SME's operations — is **`UNBOUNDED / NOT YET ENUMERABLE`**, and it will remain
> so until `P01`–`P10` publish their own process maps. Under `EC-01` that keeps the gate blocked.
>
> **This is stated first because the programme's recurring failure mode is exactly the opposite move:
> treating an author-assembled list as a proven denominator.** It is not one here.

---

## 2. Canonical business event register

`Owner` = the **single** process that owns the business fact. `P11` asserts one owner per event; where
the evidence does not determine one, the row says so rather than choosing.

### P01 — Procure-to-Pay

| id | Business event | Owner | Operational fact | Financial fact | Evidence |
|---|---|---|---|---|---|
| `UBE-01` | Purchase order placed | `P01` | committed demand | **none** — a commitment is not a financial fact | `BC-01` §2.1 |
| `UBE-02` | Goods received against a purchase order | **`P01` emits, Inventory owns the stock fact** | quantity on hand increases at a location | inventory value increases; a received-not-invoiced obligation arises | `SL-07` `HO-07`; `BC-01` §2.1 |
| `UBE-03` | Partial receipt | as `UBE-02` | partial quantity | partial value | `BC-01` §2.5 |
| `UBE-04` | Vendor bill received | `P01` | supplier asserts a claim | payable arises; price may differ from receipt | `SL-01` `08` Part 2 |
| `UBE-05` | Vendor bill received **before** the goods | `P01` | none yet | payable arises against no stock fact | `BC-01` §2.2 |
| `UBE-06` | Purchase price differs from receipt valuation | **NOT DETERMINED** — `JT-02` open on price-difference account scope | none | a difference requiring a home | `SL-17` `12_CGS_U03` |
| `UBE-07` | Purchase return to vendor | `P01` + Inventory | quantity leaves | payable reduced; cost basis question | `BC-01` §2.8; `JT-05` |
| `UBE-08` | Landed cost incurred | **NOT DETERMINED** — `JT-08` open, Audit VETO retained | none | cost to be allocated across lines | `SL-07` `HO-14` |
| `UBE-09` | Vendor paid | `P06` | cash leaves the bank | payable discharged | `SL-01` `08` Part 2 |

### P02 — Order-to-Cash

| id | Business event | Owner | Operational fact | Financial fact | Evidence |
|---|---|---|---|---|---|
| `UBE-10` | Sales order accepted | `P02` | committed supply | **none** | `BC-01` §2.3 |
| `UBE-11` | Goods delivered to customer | **`P02` emits, Inventory owns the stock fact** | quantity leaves | **cost released — timing `NOT DECIDABLE` (`JT-04`)** | `SL-07` `HO-09` |
| `UBE-12` | Partial delivery / backorder | as `UBE-11` | partial | partial | `BC-01` §2.6, §2.7 |
| `UBE-13` | Customer invoice issued | `P02` | customer is billed | revenue recognised; receivable arises | `SL-01` `05` §1 |
| `UBE-14` | Invoice issued **before** delivery | `P02` | none yet | revenue against no delivery fact | `BC-01` §2.4 |
| `UBE-15` | Customer credit note | `P02` | possible return | revenue reduced | `SL-01` `08` Part 2 |
| `UBE-16` | Sales return received | `P02` + Inventory | quantity returns | **cost basis `NOT DECIDABLE` (`JT-05`)** | `SL-07` `HO-10` |
| `UBE-17` | Customer paid | `P06` | cash arrives | receivable discharged | `SL-01` `08` Part 2 |

### P03 — Manufacture-to-Cost

| id | Business event | Owner | Operational fact | Financial fact | Evidence |
|---|---|---|---|---|---|
| `UBE-18` | Raw material issued to production | `P03` + Inventory | quantity moves to WIP | value moves to WIP | `SL-07` `HO-20`; `BC-01` §2.16 |
| `UBE-19` | Machine time consumed on an operation | `P03` | hours logged against a work centre | **conversion cost — link to the machine is `ABSENT` (`SL-13` `08` links 5, 7, 8, 11)** | `SL-13` `08` §1 |
| `UBE-20` | Labour time consumed | `P03` | hours logged | conversion cost | `SL-13` `08` link 9 |
| `UBE-21` | Production order completed | `P03` | finished goods exist | WIP becomes finished-goods value — **only under FIFO/average; under standard costing work-centre cost never enters (`SL-13` `08` §3 Moment A)** | `SL-13` `08` §3 |
| `UBE-22` | Production scrap / rework | `P03` + Inventory | quantity lost | **loss classification has no safe default documented (`R4-F-03`)** | `SL-07` `17` §5 area 7 |
| `UBE-23` | Capacity idle in a period | `P03` | machine did not run | **fixed overhead unallocated — must be period expense under TAS 2 ¶13** | `SL-13` `08` §4 |
| `UBE-24` | Absorbed cost differs from actual cost | **NOT DETERMINED — no variance mechanism exists (`SL-13` `08` link 18)** | none | a variance requiring a home | `SL-13` `08` §1 |

### P04 — Acquire-to-Retire

| id | Business event | Owner | Operational fact | Financial fact | Evidence |
|---|---|---|---|---|---|
| `UBE-25` | Asset acquired (from a vendor bill) | `P04` | asset exists and is in service | capitalised cost | `SL-13` `08` link 1 |
| `UBE-26` | Period depreciation charged | `P04` | asset consumed by one period | **expense — or conversion cost where the asset is a factory asset (TAS 2 ¶12)** | `SL-13` `22` `BLK-03` **CLOSED — EVIDENCE VERIFIED** |
| `UBE-27` | Depreciation absorbed into production | **NOT DETERMINED — `BLK-07` `HOLD — DESIGN DECISION REQUIRED`** | machine ran | part of inventory conversion cost | `SL-13` `22` §3 |
| `UBE-28` | Asset maintained | `P04` | downtime | **planned vs unplanned split is `BLK-08` `HOLD`** | `SL-13` `22` §3 |
| `UBE-29` | Asset used internally after full depreciation | `P04` | still in service | `BD-01`: no cap, no residual reduction | `SL-13` `22` `BLK-05` `CLOSED — BOSS DECISION` |
| `UBE-30` | Asset disposed | `P04` | asset leaves | derecognition; gain or loss | `SL-01` `08` Part 2 |

### P05 — Expense-to-Pay

| id | Business event | Owner | Operational fact | Financial fact | Evidence |
|---|---|---|---|---|---|
| `UBE-31` | Employee incurs a reimbursable expense | `P05` | a cost was incurred | **`UNKNOWN — EVIDENCE REQUIRED`** — Wave A `05` §1 records the producer contract as not established | `SL-01` `05` §1 |
| `UBE-32` | Expense approved | `P05` | approval | payable to the employee | `SL-01` `08` Part 2 |
| `UBE-33` | Employee reimbursed | `P06` | cash leaves | payable discharged | `SL-01` `08` Part 2 |

### P06 — Bank-to-Reconcile

| id | Business event | Owner | Operational fact | Financial fact | Evidence |
|---|---|---|---|---|---|
| `UBE-34` | Cash received or paid | `P06` | bank balance moves | liquidity item + counterpart | `SL-01` `05` §1 |
| `UBE-35` | Bank statement line matched to a ledger item | `P06` | bank truth agrees with book truth | settlement fact; possibly a suspense clearing | `SL-01` `05` §1 |
| `UBE-36` | Settlement occurs at a measurement different from recognition | **the ledger owns this — it is emitted, not requested** | none | **exchange difference (`AE-11`)** | `SL-01` `07` `AE-11` |

### P07 — Tax-to-Compliance

| id | Business event | Owner | Operational fact | Financial fact | Evidence |
|---|---|---|---|---|---|
| `UBE-37` | Tax becomes reportable on a document | `P07` | none | tax items on the entry | `SL-01` `05` §1 |
| `UBE-38` | Tax becomes reportable on settlement (cash basis) | **the ledger owns this — emitted by reconciliation** | none | **new posted entries, dated today when the natural period is locked (`AE-13`)** | `SL-01` `07` `AE-13` |
| `UBE-39` | Withholding tax deducted at payment | `P07` | none | tax withheld; certificate obligation | `SL-19` — Account Batch A, statutory items `HOLD` |
| `UBE-40` | Tax return posted | `P07` | filing | an entry, **and the tax lock date is set automatically (`AE-18`)** | `SL-01` `07` `AE-18` |

### P08 — Record-to-Report · P09 — Plan-to-Analyze · P10 — Time-Based Recognition

| id | Business event | Owner | Operational fact | Financial fact | Evidence |
|---|---|---|---|---|---|
| `UBE-41` | Period declared no longer open | `P08` | governance act | **none — closing posts nothing (`M-05`)** | `SL-01` `08` `M-05` |
| `UBE-42` | Opening position established at cutover | `P08` | books begin | an ordinary posted entry balanced to current-year earnings (`AE-14`) | `SL-01` `07` `AE-14` |
| `UBE-43` | Management attribution of a cost or revenue | `P09` | none | **derived from the item's analytic distribution — destroyed and regenerated by an ordinary correction** | `SL-01` `05` §1; `06` §3 |
| `UBE-44` | Revenue or cost spread over time | `P10` | none | periodic reclassification — **`UNKNOWN — EVIDENCE REQUIRED`**, producer contract not established | `SL-01` `05` §1 |

---

## 3. What this register establishes

1. **44 business events, of which 8 have no determined owner.** `UBE-06`, `UBE-08`, `UBE-11` (timing),
   `UBE-16` (basis), `UBE-22`, `UBE-24`, `UBE-27`, and `UBE-19`'s machine link. Every one of the eight
   is blocked on a decision, not on more research — `JT-02`, `JT-04`, `JT-05`, `JT-08`, `BLK-07`, and
   the absent variance mechanism.
2. **Three business events are owned by the ledger itself, not by any producer** — `UBE-36`, `UBE-38`,
   and the reversal half of correction. They are emitted without an operator asking. This is the
   single most important structural fact for `P11`, because *a consumer module that also emits
   accounting events is a producer*, and the invariant `ONE BUSINESS FACT → ONE CANONICAL OWNER`
   cannot be stated for them without saying so.
3. **Two producer contracts are not established at all** — `P05` expense (`UBE-31`) and `P10`
   deferred recognition (`UBE-44`). Wave A recorded both as `UNKNOWN — EVIDENCE REQUIRED` and no
   later package closed either.
4. **`P09` owns no business event that produces a financial fact.** Budget consumes the ledger; it
   does not produce entries. Analytic attribution is derived. This is a finding, not an omission:
   `P09`'s correct accounting relationship is *read-only*, and any `P09` design that emits a posting
   is by construction a double-counting risk. See `P11_DOUBLE_COUNTING_REGISTER.md` `DC-09`.
