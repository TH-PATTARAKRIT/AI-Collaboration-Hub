# P07 — CROSS-PROCESS OWNERSHIP

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Purpose

The session directive requires P07 to research its relationship with P01 Purchase,
P02 Sales, P05 Expense, P06 Payment, P08 GL/Close and P10 Deferred Recognition. This file
states, for each shared fact, **which process owns it**, which processes consume it, and
what P07 requires of the owner. Peer processes were executing in parallel; per the
Scope-Aware Correction §7, unresolved peer positions are recorded as
`PEER DEPENDENCY OPEN` and did not stop this session.

## 2. Ownership Principle Applied

A fact is owned by the process in which it is **created and first becomes true**, not by
the process that reports it. P07 owns the tax determination and the statutory
representation; it owns almost none of the inputs.

## 3. Ownership Table

| # | Shared fact | Owner | P07 consumes it for | P07 requirement on the owner | Status |
|---|---|---|---|---|---|
| `X-01` | Vendor bill and its line detail | P01 | Input VAT base, purchase-side WHT base and default | The line must carry the tax point, not only the accounting date (`TPR-01`) | `PEER DEPENDENCY OPEN` |
| `X-02` | Vendor identity: taxpayer id, legal personality, branch | P01 / master data | PND3 vs PND53 determination, branch column | Legal personality must be a **typed attribute**, not `is_company` (`W-K-03`); branch must be one field with one meaning (`P07-F-06`) | **BLOCKING for P07** |
| `X-03` | Customer invoice and its line detail | P02 | Output VAT base, sales-side WHT | Tax point per `S-01`/`S-02`; the tax-invoice document identity that P07 cannot supply (`D-01`) | `PEER DEPENDENCY OPEN` |
| `X-04` | Delivery / transfer of ownership event | P02 (and Inventory) | The **goods tax point** under `S-01` | P07 cannot determine a goods tax point without a delivery fact carried onto the tax fact | **BLOCKING for P07** |
| `X-05` | Service performance / utilisation event | P02 / P05 | The **services tax point** under `S-02` where the service is used before payment | Same | **BLOCKING for P07** |
| `X-06` | Expense claim and employee-borne expenditure | P05 | Input VAT on expenses; the non-deductible categories of `S-11` | A deductibility classification must exist at the expense line | `PEER DEPENDENCY OPEN` |
| `X-07` | Payment event, date, currency, amount | P06 | **The WHT tax point** (`S-30`) and the cash-basis VAT tax point | The payment date must be the anchor of the withholding fact; today the PND reports the invoice date instead (`W-C-01`) | **BLOCKING for P07** |
| `X-08` | Partial payment / allocation | P06 | Proportional withholding | The allocation must be visible to the withholding computation; today the whole invoice's WHT is taken on the first payment (`W-C-02`) | **BLOCKING for P07** |
| `X-09` | Payment reversal / cancellation | P06 | Reversal of a withholding fact | A reversal must not silently remove a row from an already-filed period (`A-09`) | **BLOCKING for P07** |
| `X-10` | Foreign-currency rate and conversion | P06 / P08 | WHT base conversion; VAT on foreign-currency invoices | A single conversion policy; today `price_subtotal` in document currency is subtracted from a payment amount with no conversion (`W-M-02`) | `PEER DEPENDENCY OPEN` |
| `X-11` | Accounting date, period, lock date | P08 | Every tax report's selection predicate today | If P07's tax point becomes the selector, P08 must accept that a tax fact and its accounting entry can fall in different periods | **DESIGN DEPENDENCY** |
| `X-12` | Period close and lock | P08 | The only control that currently protects filed figures (`A-14`) | A tax-period state distinct from the accounting period close | `PEER DEPENDENCY OPEN` |
| `X-13` | Tax settlement / closing entry to `213400`, `213500`, `114400`, `114401` | P08 | Month-end consolidation described in the chart but not traced here (`P07-N-13`) | P08 must confirm which mechanism performs it | `PEER DEPENDENCY OPEN` |
| `X-14` | Deferred revenue and deferred expense recognition | P10 | VAT tax point is **not** the accounting recognition point; deferral must not move the tax fact | An explicit rule that deferral affects P&L timing only, never tax-period membership | **BLOCKING for P10, not for P07** |
| `X-15` | Scope semantics across processes | P11 | The tenant containment of the cross-company tax-unit grouping (`P07-U-14`) | P11 must reconcile scope across P01–P10 | `PEER DEPENDENCY OPEN` |

## 4. Facts P07 Owns

| # | Fact | P07 owns because |
|---|---|---|
| `O-01` | Tax trigger determination per transaction class | It is a statutory determination, not a business event |
| `O-02` | Tax base composition and rate selection | `S-05` `S-06` `S-07` |
| `O-03` | Tax-period membership of a tax fact | `S-09` `S-15` — and this is the fact the system currently derives from P08's accounting date |
| `O-04` | Statutory document identity and particulars | `S-19` `S-20` `S-31` |
| `O-05` | Statutory report content and filing representation | `S-25` `S-33` |
| `O-06` | Correction, credit/debit note and adjustment semantics | `S-13` `S-14` `S-23` `S-24` |
| `O-07` | Withholding classification (form, income type, condition) | `S-30` `S-31` `S-33` |

`O-03` is the crux of the whole P07 surface: **P07 owns tax-period membership, and the
implementation delegates it to P08's accounting date.** Every tax-point finding in this
package is a consequence of that inversion of ownership.

## 5. Duplicate Ownership Risks

| # | Risk | Processes | Evidence |
|---|---|---|---|
| `DUP-01` | The withholding fact is created in P06 (payment) but reported from a P01 artefact (the bill line). Two processes hold a claim on one tax fact. | P06, P01, P07 | `03 §3` |
| `DUP-02` | The sales-side withholding fact is created in P06 when a customer pays us, is posted to a P08 asset account, and is claimed by no reporting process at all. | P06, P08, P07 | `W-K-08` |
| `DUP-03` | Two withholding frameworks can both act on one P06 payment event. | P06, P07 | `P07-F-16` |
| `DUP-04` | Two implementations of the s.87 books can both be installed and can return different totals for the same company and month. | P07 internal | `07 §5` |

## 6. Minimum Handoff P07 Requires

Stated as a data contract for the core accounting reconciliation, in neutral terms.

| # | From | Element | Why |
|---|---|---|---|
| `H-01` | P01 / P02 | Tax point per line, typed by transaction class | `S-01` `S-02` |
| `H-02` | P02 / Inventory | Delivery and ownership-transfer timestamps | `S-01` |
| `H-03` | P06 | Payment date, amount, currency, allocation per invoice, reversal linkage | `S-30` `S-32` |
| `H-04` | Master data | Payee legal personality as a typed attribute | `W-K-03` |
| `H-05` | Master data | One branch attribute, with an explicit scope (`TENANT` counterparty vs `COMPANY` filing unit) | `P07-F-06`, `20 §6` |
| `H-06` | P08 | Confirmation of the tax settlement mechanism and its timing | `P07-N-13` |
| `H-07` | P11 | Tenant containment ruling for the cross-company tax-unit grouping | `P07-U-14` |
