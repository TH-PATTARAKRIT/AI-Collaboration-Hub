# 24 — P03 CORE ACCOUNTING RECONCILIATION HANDOFF PACK

**LAYER 1 — CLEAN ROOM.** No reference-product model, field, path, menu or file citation
appears in this file. Every claim here is supported by Layer 2 evidence in `01`–`23` of
this package, which is Boss / PMO / AI-Audit only.

Session `SMEPLUS-26-09-04-ACC-P03-M2C-REV2-001` · Process P03 — Manufacture-to-Cost.

---

## 1. What Core Accounting Reconciliation is receiving

A statement of **how a manufacturing conversion cost behaves**, what it does to the ledger,
and the five reconciliation queries that detect each failure. Nothing here authorises a
design or closes a question.

## 2. The one formula that matters

The unit cost handed from manufacturing to inventory, and thence to cost of sales, is:

```
FG unit cost = ( materials consumed, at their inventory value
               + conversion cost measured on the work order
               + a manually entered or subcontract-derived unit cost )
               × ( 1 − by-product cost share )
               ÷ quantity produced
```

**It excludes, entirely:** equipment depreciation, factory building depreciation,
right-of-use asset depreciation, planned maintenance, energy and utilities, indirect
factory labour, and fixed production overhead of every kind.

That exclusion list is the single most important thing in this pack. Under the accounting
standard adopted by this project's asset lineage, most of those elements **belong in**
conversion cost. Inventory produced under this model is therefore understated by
construction, and cost of sales is understated with it.

## 3. The nine behaviours Core Accounting must expect

| # | Behaviour | Ledger consequence |
|---|---|---|
| 1 | Machine time is costed on a head-count-dependent base | Where two people work one machine, machine cost is charged twice. Inventory is **overstated** |
| 2 | A manually entered unit cost is capitalised but never relieved | A permanent credit residue on the production account |
| 3 | For standard-costed goods, conversion cost is relieved but never capitalised | A permanent debit residue on the same account |
| 4 | Behaviours 2 and 3 **net against each other** in one account | A small production-account balance is **not** evidence that costing is correct |
| 5 | The conversion-cost relief defaults to a cost-of-sales account | Cost of sales is credited in a period in which nothing was sold. A **period-attribution** error that reverses when the batch sells |
| 6 | The relief entry is dated when it is posted, not when the work happened | Capitalisation and relief of one event can fall in different periods |
| 7 | Work orders with no recorded time are costed at their **expected** duration | An estimate is recorded indistinguishably from a measurement, and the variance is structurally zero |
| 8 | Work-in-progress on the balance sheet is a **reversing accrual**, valued on a different basis from the consumption it accrues for, with no order-level detail, and editable before posting | The period-end WIP figure cannot be substantiated order by order |
| 9 | Conversion cost is company-scoped, but the accounts for its entry are resolved against the **acting user's** company | In a multi-company group, entries can reach the wrong legal entity's accounts |

Behaviours 1 and 9 are designated `Tolerance = 0`. So are six further boundaries listed in
§6.

## 4. The five reconciliation queries

Each detects one behaviour above. **No result for any of these has been inferred,
estimated or assumed anywhere in this package.**

| ID | Query | Detects |
|---|---|---|
| `RQ-01` | Production-account balance by company and period, decomposed by manufacturing order | Behaviours 2, 3, 4 |
| `RQ-02` | Conversion-cost relief entries whose credit lands on a cost-of-sales account | Behaviour 5 |
| `RQ-03` | Relief entries whose date differs from the corresponding finished-goods receipt date | Behaviour 6 |
| `RQ-04` | Work orders whose costed hours exceed their overlap-merged elapsed hours | Behaviour 1 |
| `RQ-05` | Entries whose company differs from the originating order's company | Behaviour 9 |

`RQ-01` is the priority: it is the only query that separates two defects which otherwise
conceal each other.

## 5. What is **not** reconcilable, and why

| Pair | Reconcilable? |
|---|---|
| Inventory value vs production-account movement | **No** — the account additionally carries the relief entry and both residues |
| Production-account movement vs analytic cost | **No** — analytic uses a different elapsed-time basis **and** omits the labour component |
| Absorbed labour vs posted payroll | **No bridge was found.** The rate is a standing parameter; payroll is an actual; nothing reconciles the difference, and the system recognises no labour rate variance |

Core Accounting should not spend effort attempting these three reconciliations before the
underlying model changes. That is the practical value of this pack.

## 6. Tolerance-zero boundaries handed forward

Financial-integrity boundaries that must not be averaged into an overall defect rate:

1. Machine-hours costed equal machine-hours occupied.
2. Conversion cost capitalised equals conversion cost relieved, per order.
3. The relief credit never lands on a cost-of-sales account.
4. Company-dependent accounts resolve in the transaction's own company.
5. Capitalisation and relief of one event share a period.
6. Analytic conversion cost reconciles to ledger conversion cost.
7. An unmeasured cost is distinguishable from a measured one.
8. A full by-product cost share does not silently zero the main product's cost.

## 7. Open items Core Accounting must not treat as settled

| Item | Owner | Status |
|---|---|---|
| The allocation denominator for fixed overhead — normal capacity or actual hours | **Boss** | **HOLD**, from the asset lineage. Nothing downstream can be specified without it |
| Planned vs unplanned maintenance split | **Boss** | **HOLD**, from the asset lineage |
| Cost of sales | COGS track | **Terminal HOLD** |
| Whether manufacturing variance is recognised at all | **Boss** | **Decision required** |
| Ownership of the joint / co-product cost model | **Boss** | **Unowned by any track today** |
| Admission of manufacturing to the target process and specification baseline | **Boss / PMO** | Manufacturing appears in none of the existing end-to-end processes or module specifications |
| Cross-process scope reconciliation | **P11** | **Peer dependency open** |

## 8. Scope statement

Every negative finding in this pack — "no path exists", "no bridge was found", "no such
object" — is bounded by the source material this session examined. **The configuration of
the running system was not available to this session.** Establishing it is a priority-1
open query on the asset lineage, and it caps every negative claim made here.

Nothing in this pack is a design, a specification, a gate closure, or an authorisation to
implement.
