# 01 — P02 ORDER-TO-CASH PROCESS MAP

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`

## 1. Mandated Forensic Trace

```
Module -> Model -> Field Relationship -> Function -> Business Event -> Runtime
  -> DB Evidence -> Operational Truth -> Accounting Event -> Journal -> Subledger
  -> Settlement/Reconciliation -> Reporting -> Close
```

This map walks the O2C spine stage by stage. Each stage answers four questions:

1. What business fact occurs?
2. Which record is the canonical owner of that fact?
3. What accounting effect (if any) is produced, and by which trigger?
4. Where does the fact become mutable again after it has been asserted?

Question 4 is the forensic question. A fact that stays mutable after it has produced an
accounting effect is the root of every double-recognition class in `12_P02_CONTRADICTION_REGISTER.md`.

## 2. The Spine

```
  [S1] QUOTATION
     |                                (no accounting effect)
     v
  [S2] SALES ORDER CONFIRMATION      <-- commercial commitment
     |                                (no accounting effect)
     |--> [S3] RESERVATION / PROCUREMENT   (no accounting effect)
     |         |
     |         v
     |    [S4] DELIVERY (physical outflow)
     |         |
     |         +--> [S5] INVENTORY VALUATION EVENT   <== FIRST accounting effect
     |                    Dr  Interim "Goods Delivered, Not Invoiced"
     |                    Cr  Inventory Valuation
     |
     |--> [S6] CUSTOMER INVOICE (draft)     (no accounting effect)
               |
               v
          [S7] INVOICE POST                 <== SECOND and THIRD accounting effects
               |    (revenue)  Dr Accounts Receivable / Cr Revenue / Cr Output VAT
               |    (cost)     Dr Cost of Sales / Cr Interim "Goods Delivered, Not Invoiced"
               v
          [S8] INTERIM ACCOUNT RECONCILIATION  (automatic, best-effort)
               |
               v
          [S9] CUSTOMER RECEIPT                <== FOURTH accounting effect
               |    Dr Outstanding Receipts / Cr Accounts Receivable
               v
          [S10] BANK RECONCILIATION            <== FIFTH accounting effect
               |    Dr Bank / Cr Outstanding Receipts
               v
          [S11] REPORTING  ->  [S12] PERIOD CLOSE
```

Two independent *return* paths hang off this spine and are analysed in
`08_P02_RETURN_CREDIT_REFUND_MATRIX.md`:

```
  [R1] PHYSICAL RETURN   (inventory back in, cost restored)   -- operational path
  [R2] CREDIT NOTE       (revenue and AR reversed)            -- accounting path
```

**`FACT VERIFIED` — R1 and R2 are structurally independent.** Neither triggers the other. See
`08_P02_RETURN_CREDIT_REFUND_MATRIX.md` §2 for the evidence.

## 3. Stage-by-Stage Analysis

### S1 — QUOTATION

| Aspect | Finding | Tag | Evidence |
|---|---|---|---|
| Canonical owner | The order document itself in its `draft`/`sent` status. There is no separate quotation entity. | `FACT VERIFIED` | `EV-P02-035` |
| Status model | The order has exactly **four** statuses: draft (Quotation), sent (Quotation Sent), sale (Sales Order), cancel. | `FACT VERIFIED` | `EV-P02-035` |
| Accounting effect | None. | `FACT VERIFIED` | — |
| Quotation date | The order-date field holds the quotation date **until confirmation, when it is overwritten with the system clock** (see S2). The original quotation date survives only in the technical record-creation timestamp. | `FACT VERIFIED` | `EV-P02-001` |

**`SUPPORTED INTERPRETATION` — P02-F-01.** Quotation and Sales Order are the same physical record
in two statuses. This is efficient but it means the quotation is not an immutable commercial
artefact: price, quantity, customer, tax position and validity can all be changed after the
quotation is sent, and the sent version is recoverable only from the message log, not from the
data model. For SMEsPlus this is a `DESIGN CANDIDATE` decision: whether a quotation is a versioned
document in its own right or a status of the order.

### S2 — SALES ORDER CONFIRMATION

| Aspect | Finding | Tag | Evidence |
|---|---|---|---|
| Business event | Commercial commitment is created. | `FACT VERIFIED` | `EV-P02-036` |
| Date semantics | Confirmation **writes the order date to the current system timestamp**, destroying the previous value. Confirmation cannot be backdated through this path. | `FACT VERIFIED` | `EV-P02-001` |
| Accounting effect | **None.** No revenue, no AR, no deferred-revenue liability, no commitment note. | `FACT VERIFIED` | — |
| Completion semantics | There is **no terminal "done"/"closed" status**. Completion is expressed by a boolean lock flag which any authorised user can set and unset. | `FACT VERIFIED` | `EV-P02-035`, `EV-P02-037` |

**`FACT VERIFIED` — P02-F-02: order confirmation has no accounting consequence whatsoever.**
This is correct under accrual accounting (an executory contract is not a transaction) but it means
the *entire* financial consequence of P02 rests on two later events — the physical outflow and the
invoice post — and on the quantity counters that connect them.

**`SUPPORTED INTERPRETATION` — P02-F-03.** Because completion is a reversible flag rather than a
state, "this order is finished" is not an assertable, auditable business fact. An order can be
unlocked, re-opened and re-invoiced after it has been reported as complete.

### S3 — RESERVATION / PROCUREMENT

| Aspect | Finding | Tag | Evidence |
|---|---|---|---|
| Trigger | Creating or writing an order line while the order is confirmed launches the procurement/stock rule for that line. Reservation is a consequence of the line, not of the order. | `FACT VERIFIED` | `EV-P02-033` |
| Accounting effect | None. Reservation moves no value. | `FACT VERIFIED` | — |
| Ownership | Ownership ≠ availability. Reserved stock is still owned and still valued by the selling company. | `SUPPORTED INTERPRETATION` | `EV-P02-023` |

**`DEPENDENCY OPEN` — P02-D-01.** Reservation semantics, allocation priority and availability
computation are owned by the Inventory module, not by P02. The Inventory Multi-Tenant Invariant
Set and its ruling-conformance package are the authority. P02 consumes reservation; it does not
define it.

### S4 — DELIVERY (physical outflow)

| Aspect | Finding | Tag | Evidence |
|---|---|---|---|
| Operational truth | The outflow is recorded when the movement reaches `done` with at least one line marked picked. | `FACT VERIFIED` | `EV-P02-022`, `EV-P02-038` |
| **Valuation gate** | Valuation is produced **only if** the movement quantity is non-zero **and at least one movement line carries the `picked` marker**. A movement can reach `done` with no picked line and produce **no valuation and no accounting entry at all**. | `FACT VERIFIED` | `EV-P02-022` |
| Consumable products | Non-storable products produce no valuation entry and no cost effect on outflow. | `FACT VERIFIED` | `EV-P02-023` |
| Owner-restricted stock | Movements restricted to a third-party owner are excluded from valuation. | `FACT VERIFIED` | `EV-P02-025` |
| Movement statuses | draft · waiting · confirmed · assigned · done · cancel — six values. | `FACT VERIFIED` | `EV-P02-039` |

**`FACT VERIFIED` — P02-F-04 (TOLERANCE-ZERO CANDIDATE): operational completion and valuation
completion are governed by two different conditions.** A delivery is operationally complete when
its status is `done`. It is financially complete only when a *separate* per-line marker is set.
The gap between those two conditions is a class of physically-shipped, financially-invisible goods.

For SMEsPlus this is a `DESIGN CANDIDATE`: the outflow event must be **atomic** — either the
operational fact and the valuation fact are both recorded or neither is. A separate boolean
qualifying whether a completed movement counts financially should not exist.

### S5 — INVENTORY VALUATION EVENT (first accounting effect)

| Aspect | Finding | Tag | Evidence |
|---|---|---|---|
| Journal effect | Dr *Interim — Goods Delivered Not Invoiced* / Cr *Inventory Valuation*. | `FACT VERIFIED` | `EV-P02-023`, `EV-P02-024` |
| **This is NOT cost of sales** | The debit is an asset-clearing account, not an expense. Delivery does **not** recognise cost of sales under the split-recognition (anglo-saxon) configuration. | `FACT VERIFIED` | `EV-P02-016`, `EV-P02-023` |
| Configuration dependency | Whether cost of sales is recognised at delivery or at invoice is controlled by a **single company-level boolean**. | `FACT VERIFIED` | `EV-P02-040` |
| Valuation basis | The value relieved is determined by the costing method (standard / average / FIFO) at the moment of outflow. | `FACT VERIFIED` | `EV-P02-032` |

**`FACT VERIFIED` — P02-F-05 (HEADLINE): the outflow always debits the *configured outbound stock
account*; a single company-level boolean decides whether anything ever moves that balance to cost
of sales.**

The precise mechanism, stated exactly:

1. The outflow entry is always `Dr <configured outbound stock account> / Cr <inventory valuation
   account>`. The destination account is not chosen by the boolean — it is read from the product
   category configuration. `EV-P02-024`
2. The boolean controls **only** whether the invoice adds a second pair of lines
   `Dr <expense> / Cr <configured outbound stock account>`. `EV-P02-016`

Therefore three distinct outcomes are configuration-reachable, not two:

| Outbound stock account configured as | Split-recognition boolean | Where cost of sales lands | Recognition event |
|---|---|---|---|
| Interim asset ("goods delivered not invoiced") | ON | Expense, at invoice post | **Invoice** |
| Expense account | OFF | Expense, at outflow | **Delivery** |
| Interim asset | **OFF** | **Nowhere — balance parks in the interim asset indefinitely** | **None** |

The third row is the dangerous one. It is not an error state, it produces no warning, and both of
its ingredients are ordinary configuration values held on different objects (a boolean on the
company, an account on the product category) with no cross-validation between them.

**`FACT VERIFIED` — P02-F-05b (THAILAND-SPECIFIC, HEADLINE).** Against the Thai chart-of-accounts
template the third row is the **default** starting position, for two independent reasons:

- The Thai chart template does **not** set the split-recognition boolean, and the chart-installation
  routine explicitly defaults it to **off**. `EV-P02-042`, `EV-P02-043`
- The Thai chart template defines **27 accounts** and **none of them is a stock-input, stock-output
  or stock-valuation account**. It provides `Inventory` and `Cost of Revenue` and nothing between
  them. `EV-P02-044`

Consequences, each `FACT VERIFIED`:

- Real-time valuation **cannot be switched on at all** until stock input, stock output and stock
  valuation accounts have been set, because a validation constraint on the product category refuses
  the change. `EV-P02-045`
- Those three accounts are **company-dependent properties**, and so is the valuation mode itself.
  The constraint therefore validates only the values visible in the writing company's context.
  `EV-P02-046`. A second, independent runtime guard exists in the outflow routine and raises at
  delivery confirmation if an account still cannot be resolved — `EV-P02-047`. The presence of that
  second guard is itself evidence that the configuration constraint is not considered sufficient.
- Real-time inventory valuation is therefore not reachable under the Thai chart until the
  implementer creates stock interim and valuation accounts by hand, **per company**.
- With valuation left at its manual/periodic default, **the entire O2C process produces no
  automatic cost-of-sales entry at any point**. Cost of sales exists only if somebody posts a
  periodic manual entry outside the process.

**`CONTRADICTED` — P02-C-01.** The common assumption (carried into this session from the general
chart-of-accounts behaviour) that "delivery relieves inventory and posts to an interim account" is
**not** true by default for a Thai company in the reference system. It is true for the generic
chart, which sets both the boolean and the accounts. `EV-P02-042`, `EV-P02-044`. This contradiction
is material: any P02 accounting design that assumes perpetual valuation is assuming a configuration
the Thai localisation does not deliver.

**`FACT VERIFIED` — P02-F-05c (ASYMMETRY).** The Thai chart **does** provide an interim account for
the inbound direction — `Uninvoiced Receipts (2103, liability)` — and provides **no** counterpart
for the outbound direction. The purchase side of the interim mechanism is chart-supported; the
sales side is not. `EV-P02-044`

**`BOSS CONTROLLED DECISION` — P02-B-01.** SMEsPlus must decide whether cost-of-sales timing is a
*policy* (tenant-configurable, versioned, effective-dated, period-locked, and validated against the
chart it depends on) or an *invariant* (one fixed rule for the platform). It may not be an
unversioned boolean whose meaning depends on an unrelated account configuration.

**`HOLD — CROSS-PROCESS RECONCILIATION REQUIRED` — P02-X-01.** This finding is the same underlying
subject as the open Inventory COGS dependency (`ERPPLUS-142` Deep Research, terminal HOLD, headline
"the reference perpetual pattern is unstable across versions") and the Inventory v2.0 hold. P02
does **not** re-adjudicate it. P02 contributes the O2C-side evidence above and routes the decision
to Core Accounting Reconciliation.

### S6 — CUSTOMER INVOICE (draft)

| Aspect | Finding | Tag | Evidence |
|---|---|---|---|
| Accounting effect | None while draft. | `FACT VERIFIED` | `EV-P02-015` |
| **Counter effect** | A **draft** invoice already consumes the order line's invoiceable quantity, because the invoiced-quantity counter includes every non-cancelled invoice regardless of status. | `FACT VERIFIED` | `EV-P02-005` |
| Parallel counter | A second, separate counter exists that includes **only posted** invoices, used for accounting purposes. | `FACT VERIFIED` | `EV-P02-006` |
| Invoice date | Not set at creation. The order-to-invoice entry point accepts a date argument but **the argument is documented as unused**. | `FACT VERIFIED` | `EV-P02-010`, `EV-P02-011` |
| Grouping | By default invoices are **merged across sale orders** by (company, partner, currency). The link back to the originating orders becomes a comma-joined free-text field at header level; the only structural link is per line. | `FACT VERIFIED` | `EV-P02-009`, `EV-P02-010` |

**`FACT VERIFIED` — P02-F-06 (DOUBLE-REVENUE ATTACK, BLOCKED BUT FRAGILE).** Two counters describe
"how much of this order has been invoiced": one counts draft invoices, one does not. The counter
that *prevents a second invoice being raised* is the permissive one (draft counts), so the double-
invoice attack is blocked. The counter that *feeds accounting* is the strict one. The two are
computed by different triggers and can legitimately disagree at any instant. The block therefore
depends on a recompute ordering rather than on a constraint.

**`FACT VERIFIED` — P02-F-07 (ORDER↔INVOICE IDENTITY IS NOT 1:1).** Header-level provenance from
invoice back to sale order is free text. Any reconciliation that joins invoices to orders at header
level is joining on a string.

### S7 — INVOICE POST (second and third accounting effects)

This is the densest control point in P02. Three separate things happen in one transition.

**(a) Revenue and receivable.** Dr Accounts Receivable / Cr Revenue / Cr Output tax.
Revenue account is resolved from the product's income account, then remapped by the fiscal
position. The receivable account is resolved by a fallback chain (partner property → company
partner property → arbitrary first receivable account of the company), then remapped by the fiscal
position. `FACT VERIFIED` `EV-P02-026`.

**(b) Cost of sales** (only when split recognition is enabled). Dr Cost of Sales / Cr Interim.
Detail in `03_P02_DELIVERY_COGS_TRACE.md`. `FACT VERIFIED` `EV-P02-015`, `EV-P02-016`.

**(c) Date resolution.** Two dates exist and they are resolved by different rules:

| Date | Rule | Tag | Evidence |
|---|---|---|---|
| Document date (tax point) | If blank at posting, **silently set to the system's current date** for customer invoices. For vendor bills a blank date is a hard error instead. | `FACT VERIFIED` | `EV-P02-012` |
| Accounting date (GL period) | If it violates a lock date, it is **silently moved forward** to the earliest open period; posting is **not** refused. | `FACT VERIFIED` | `EV-P02-013`, `EV-P02-014` |

**`FACT VERIFIED` — P02-F-08 (TOLERANCE-ZERO CANDIDATE): posting into a locked period does not
fail; it silently relocates the entry to a different period and leaves the document date behind.**

**`FACT VERIFIED` — the tax consequence, corrected by the T3 evidence track.** The tax report keys
on the **accounting date**, not the document date (`EV-P02-056`). The divergence is therefore not
"tax sees one date, the ledger sees another" — it is sharper than that:

> **The printed tax invoice shows the original date. The VAT return declares it in the later
> period. The general ledger books it in the later period. The document itself retains no record
> that the two ever differed.**

The two can fall in different months, different quarters and — because the fallback is capped at
today — different fiscal years. The user is warned in the interface before posting (`EV-P02-057`)
but nothing blocks it, and the warning is not retained on the document.

**`HOLD — STATUTORY EVIDENCE REQUIRED` — P02-S-01.** Whether Thai VAT is due by reference to the
tax-invoice date or to the accounting date, and whether a tax invoice bearing one date but declared
in a later period is permissible, requires Thai Revenue Department evidence. The specific sources to
be read are named in `L2_AUDIT_QUARANTINE/T3_TAX_VAT_WHT_THAI_EVIDENCE.md` §9 row T3-S1. Routed to
the Accounting-Tax track. See also `11_P02_EDGE_CASE_MATRIX.md` §7.

**`FACT VERIFIED` — P02-F-09.** Reset-to-draft of a posted customer invoice **deletes** the
cost-of-sales journal items that posting created. The revenue lines survive the round trip; the
cost lines are destroyed and regenerated. `EV-P02-017`.

**`SUPPORTED INTERPRETATION` — P02-F-10 (DOUBLE-COGS STRUCTURAL EXPOSURE).** Cost-of-sales
generation on posting has **no idempotency guard**: it iterates the product lines and creates a new
pair of cost lines every time the post routine runs, and the generated lines are excluded from the
set it iterates, so they are invisible to it. The only structural protection is that the generator
runs *before* the routine decides which documents actually post. A document that enters the post
routine and is then deferred rather than posted therefore retains cost lines while remaining in
draft, and a subsequent post creates a second pair. The evidence required to convert this to
`FACT VERIFIED` is named in `12_P02_CONTRADICTION_REGISTER.md` C-04.

### S8 — INTERIM ACCOUNT RECONCILIATION

After posting, the system attempts to reconcile the invoice's interim-account line against the
delivery's interim-account line for the same product. `FACT VERIFIED` `EV-P02-041`.

**`FACT VERIFIED` — P02-F-11.** This reconciliation is **best-effort and conditional**. It is
skipped entirely when: the interim account is not flagged reconcilable; the product is not under
real-time valuation; or no completed customer-direction movement is linked to the invoice lines.
When it is skipped, the interim account accumulates an unmatched balance and there is no exception,
no warning and no queue. The residual is discovered only by someone reading the account.

**`DESIGN CANDIDATE` — P02-DC-01.** In SMEsPlus the interim "goods delivered not invoiced" account
must be a **reconciliation-controlled subledger with a mandatory ageing and exception report**, not
an ordinary GL account that happens to get auto-matched when conditions permit.

### S9 — CUSTOMER RECEIPT · S10 — BANK RECONCILIATION

Analysed in `09_P02_PAYMENT_RECONCILIATION_MATRIX.md`. The structural point for the process map is:

**receipt ≠ settlement ≠ reconciliation are three distinct events**, and the reference process
models them as such (an outstanding-receipts clearing account sits between the receivable and the
bank). P02 must preserve that separation. Collapsing "customer paid" into "bank balance changed"
is the single most common SME-ERP error and it destroys bank reconciliation.

### S11 — REPORTING · S12 — PERIOD CLOSE

Analysed in `11_P02_EDGE_CASE_MATRIX.md` §6 and §7 and in the T4 evidence extract under
`L2_AUDIT_QUARANTINE/`.

## 4. Where the Spine Loses Its Invariant

| # | Business fact | Canonical owner (reference) | Second mutable holder of the same fact | Consequence |
|---|---|---|---|---|
| 1 | How much left the warehouse | the movement ledger | the order line's delivered-quantity field, which is **stored and writable at the data layer** — see `05` §3a for the exact reachability | Revenue under delivery-based invoicing can be driven by an asserted number rather than by the outflow ledger — `EV-P02-002`, `EV-P02-070` |
| 2 | How much has been billed | the posted invoice set | a second counter that also counts drafts | Two answers to one question — `EV-P02-005`, `EV-P02-006` |
| 3 | What the goods cost | the valuation layer created at outflow | the cost re-derived at invoice post, with a standard-price top-up when layers run out | Cost of sales ≠ inventory relieved — `EV-P02-019`, `EV-P02-020` |
| 4 | When the sale happened | the document date | the accounting date, silently movable | Tax period ≠ GL period — `EV-P02-013` |
| 5 | Which order an invoice belongs to | per-line link | header free-text | Header-level joins are unsafe — `EV-P02-009` |

Each row is a violation of `ONE BUSINESS FACT -> ONE CANONICAL EVENT OWNER`. Rows 1, 3 and 4 are
`TOLERANCE-ZERO` candidates under EC-04 and are carried to `18_P02_PMO.md`.

## 5. Negative Claims Made In This File

Stated per the SMEsPlus Negative Claim Control (`NO EVIDENCE FOUND != FUNCTION DOES NOT EXIST`):

| Claim | Classification | Search boundary |
|---|---|---|
| Order confirmation produces no accounting entry | `NOT FOUND IN SEARCHED SCOPE` | Confirmation routine and its extension point in the sales module; no accounting-document creation reached. Localisation and third-party extension modules **not** searched. |
| There is no terminal completed status on the order | `VERIFIED ABSENCE` | The status enumeration is a four-value literal in the sales module and is the complete denominator. |
| Reservation produces no accounting entry | `NOT FOUND IN SEARCHED SCOPE` | Valuation is produced only from the movement-completion routine; reservation does not reach it. Scope: inventory-accounting module movement layer only. |
