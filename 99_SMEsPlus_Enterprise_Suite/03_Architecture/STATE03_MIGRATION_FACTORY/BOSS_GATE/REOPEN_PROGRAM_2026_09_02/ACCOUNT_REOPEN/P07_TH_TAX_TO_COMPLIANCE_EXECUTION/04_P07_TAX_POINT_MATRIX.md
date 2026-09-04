# P07 — TAX POINT MATRIX

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. Definitions Kept Separate

| Term | Meaning in this package |
|---|---|
| **Tax point** | The statutory moment at which the tax liability arises (`S-01`…`S-04`, `S-30`) |
| **Tax date** | The date attribute the system uses to place a fact in a tax period |
| **Accounting date** | The date the ledger entry belongs to for accounting purposes |
| **Document date** | The date printed on the document (invoice date, note date, certificate date) |

The Thai statute makes the tax point primary and lets the other three follow. The declared
source set makes the **accounting date** primary. The whole of this matrix is a
consequence of that inversion.

## 2. Statutory Tax Point by Transaction Class

| # | Class | Statutory tax point | Source | System attribute that actually places the fact | Match |
|---|---|---|---|---|---|
| `TP-01` | Sale of goods, general | Delivery, or earlier of ownership transfer / payment / tax-invoice issuance | `S-01` | move accounting date | **NO** |
| `TP-02` | Sale of goods on consignment | Earlier of consignee delivery or ownership transfer / payment / tax-invoice issuance | `S-01` (as published) | move accounting date | **NO** |
| `TP-03` | Provision of services | Receipt of payment, or earlier of tax-invoice issuance / use of service | `S-02` | move accounting date, unless the tax is configured cash-basis, in which case the tax becomes exigible on payment and the reports honour `tax_exigible` | **CONFIGURABLE** — `P07-U-16` |
| `TP-04` | Importation | Payment of import duty, or Customs entry where duty-exempt | `S-03` | not modelled | **NOT FOUND IN SEARCHED SCOPE** |
| `TP-05` | Incorporeal goods, vending machines, credit-card sales, prescribed contracts | Per Ministerial Regulation | `S-04` | not modelled | **NOT FOUND IN SEARCHED SCOPE** |
| `TP-06` | Debit note | The tax month in which the **note is issued** | `S-13` `S-23` | accounting date of the reversal/adjustment entry | **NO** |
| `TP-07` | Credit note | The tax month in which the **note is issued** (issuer) / **received** (recipient) | `S-14` `S-24` | accounting date of the reversal entry; the recipient side has no receipt-date attribute | **NO** |
| `TP-08` | Input tax on a purchase | The tax month of the tax invoice, subject to the deferred-claim rule held at `U-03` | `S-09` `S-11` | move accounting date of the bill | **PARTIAL** — the deferral the rule permits is precisely what `account.move.tax_period` was built to express, and that field does not drive selection |
| `TP-09` | Withholding tax | **The moment of payment** | `S-30` | the **invoice's** accounting date, via the second UNION branch of the PND query | **NO** |
| `TP-10` | Self-assessed VAT on foreign services | On remittance under s.83/6 | `S-17` | not modelled | **NOT FOUND IN SEARCHED SCOPE** |
| `TP-11` | **Hire purchase / instalment sale** where ownership does not pass on delivery | **Each instalment due date**, with a tax invoice issued on each | `S-38` | not modelled; the acquisition path itself is absent from the reference estate per P04 | **NOT FOUND IN SEARCHED SCOPE** — `P07-F-59` |
| `TP-12` | **Supply without consideration** — donation, scrapping, application to a non-business purpose, stock shortfall, goods on cessation | The act itself is a sale; no consideration is required | `S-36` `S-37` | not modelled; no output-tax event and no document | **NOT FOUND IN SEARCHED SCOPE** — `P07-F-58`; extent held at `U-23` |

## 3. The Three Date Attributes Available, and What Reads Them

| Attribute | Defined at | Written by | Read by |
|---|---|---|---|
| `account.move.date` (accounting date) | base application | posting | **every** tax report's period filter in the declared set |
| `account.move.invoice_date` (document date) | base application | user | one display column, added by the SMEsPlus override of the vendor XLSX report (`l10n_th_reports_ext/models/tax_report_vat.py:175`, header "Bill Date") |
| `account.move.tax_period` (tax point) | `smesplus_tax_period_date/models/tax_period.py:23` | user, on the move form | one display column on the SMEsPlus Sale/Purchase VAT reports (`smesplus_account_reports/models/account_generic_tax_report.py:38`, `:92-108`, `:415`, `:475-489`) |
| `account.move.line.tax_period_date` | `smesplus_tax_period_date/models/tax_period.py:36` | `create()` only, and only for lines that already carry `tax_line_id` at create time | **no report, compute, domain or SQL.** Its sole reader is a readonly, `optional="hide"` list column (`smesplus_tax_period_date/views/view_tax_period.xml:30`) — class `A`, boundary: PATH SET of `13 §2`, all file types, `__pycache__` excluded |

## 4. The Removed Substitution

The single most consequential change traced in this session is a deletion, established by
a file-level diff rather than a token check.

Predecessor file, `smesplus_account_reports/models/account_generic_tax_report.py_bkp:29-30`:

    # Correction on code to accept tax_period as default date by mlf ACC-8
    where_clause = where_clause.replace('"account_move_line"."date"',
        'COALESCE(account_move_line__move_id.tax_period, account_move_line.date)')

Current file, same method, same position: the substitution is **absent**, and the period
predicate is taken unmodified from `report._get_report_query(options, 'strict_range')`
(`account_generic_tax_report.py:26`). In the same migration the `tax_period` **display**
column was **added** (`:38`, `:92-108`).

Net effect: the tax point was demoted from a selector to a decoration, and a column was
added that shows the reader a date the report did not use. The change carries an
issue reference in the deleted comment (`ACC-8`), so the substitution was a deliberate
prior correction; its removal has no recorded rationale in the declared source set.

| Property | Predecessor | Current |
|---|---|---|
| Period predicate | `COALESCE(tax_period, date)` | `date` |
| `tax_period` shown to the user | no | yes |
| Behaviour when `tax_period` is empty | falls back to `date` — safe | irrelevant, never read for selection |
| Behaviour when `tax_period` differs from `date` | fact moves to the tax period | fact stays in the accounting period, and the report displays the other date beside it |

## 5. Failure Cases Produced by the Inversion

Each is a concrete, reproducible statement of what a user would observe.

| # | Case | Observed result |
|---|---|---|
| `TPF-01` | A service invoice is posted 28 September and paid 3 October; the tax is configured accrual. | Output tax is reported in September. Under `S-02` the tax point is the October payment. |
| `TPF-02` | A vendor tax invoice dated 30 September is received on 10 October; the user sets Tax Period Date to October to claim input tax in October. | The bill is selected into the **September** report; the October report omits it; the September report row displays "October" in the Tax Period Date column. |
| `TPF-03` | A credit note is issued on 5 October against a September tax invoice, and the accountant back-dates the accounting entry to September to match the original. | The reduction lands in September. Under `S-14` it belongs to October. |
| `TPF-04` | A bill dated 25 September is partially paid on 2 October with 3% withholding. | The whole invoice's withholding is reported on the **September** PND, because the PND branch is dated by the invoice and gated on `payment_state != 'not_paid'`. The October PND, covering the month in which tax was actually withheld and in which remittance falls due under `S-32`, contains nothing for it. |
| `TPF-05` | A customer withholds 3% when paying our sales invoice. | The withholding is posted to `114300 WHT Creditable` and appears on no tax report at all, because the income-side tax templates carry no tax tags (`W-K-08`). |

## 6. What Would Have To Be True for the Model to Be Correct

Stated as evidence requirements for the next round, not as a design.

| # | Requirement on the model | Blocked by |
|---|---|---|
| `TPR-01` | A tax point attribute must exist on the **tax fact**, be mandatory, and be the sole selector for tax-period membership. | `P07-F-02`, `P07-F-03` |
| `TPR-02` | The tax point must be derivable per transaction class (goods / services / import / note), not entered as one free date on the document header. | `TP-01`…`TP-07` |
| `TPR-03` | The withholding tax point must be the payment, and the reported fact must be the posted withholding line. | `P07-F-11` |
| `TPR-04` | Credit and debit notes must carry their own note date and the original tax invoice reference, and be placed by note date. | `P07-F-07` |
| `TPR-05` | The legal basis for a deferred input-tax claim must be established before a purchase-side tax point that differs from the invoice date can be designed. | `U-03` — `HOLD — STATUTORY EVIDENCE REQUIRED` |
