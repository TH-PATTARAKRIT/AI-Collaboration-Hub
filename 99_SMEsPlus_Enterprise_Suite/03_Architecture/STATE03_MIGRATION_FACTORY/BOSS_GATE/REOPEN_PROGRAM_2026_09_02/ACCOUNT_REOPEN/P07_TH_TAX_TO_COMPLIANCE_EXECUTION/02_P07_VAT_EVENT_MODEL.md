# P07 — VAT EVENT MODEL

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-04`

## 1. The Canonical Chain Required by the Constitution

    Source Business Event
      -> Tax Trigger
      -> Tax Base
      -> Tax Calculation
      -> Tax Document
      -> Tax Accounting Event
      -> Journal
      -> Tax Report
      -> Filing / Adjustment / Close

with the invariant:

    ONE TAX FACT -> ONE CANONICAL TAX EVENT -> ONE ACCOUNTING EFFECT

This file traces that chain for VAT twice: as the statute requires it (§2), and as the
declared source set implements it (§3). §4 states where the two diverge and §5 states
where the invariant is broken.

## 2. Statutory VAT Event Chain

| Link | Statutory content | Source |
|---|---|---|
| Source business event | Sale of goods; provision of services; importation | `S-01` `S-02` `S-03` |
| Tax trigger (tax point) | **Goods**: delivery, or earlier of ownership transfer / payment / tax-invoice issuance. **Services**: receipt of payment, or earlier of tax-invoice issuance / use of service. **Import**: payment of import duty or Customs entry. Special classes by Ministerial Regulation. | `S-01` `S-02` `S-03` `S-04` |
| Tax base | Total value received or receivable, including excise, excluding output tax | `S-05` |
| Tax calculation | Rate per s.80 (10%, reduced to 7% by Royal Decree); zero rate per s.80/1; exempt per s.81 | `S-06` `S-07` `S-35` |
| Tax document | Tax invoice with own serial number, issued **immediately at the tax point**; abbreviated tax invoice for retail; debit note; credit note | `S-19` `S-20` `S-22` `S-23` `S-24` |
| Tax accounting event | Output tax charged to the purchaser at the tax point; input tax recorded on receipt of a compliant tax invoice | `S-10` `S-11` |
| Journal | Not prescribed by the Revenue Code; governed by accounting standard | — |
| Tax report | Output tax report and input tax report, entered within 3 working days | `S-25` |
| Filing / adjustment / close | Monthly return by the 15th of the following month, **per place of business**; net = output − input for the tax month; credit/debit notes adjust in the month issued or received; excess credit carried forward or refunded | `S-15` `S-09` `S-13` `S-14` `S-18` |

## 3. Implemented VAT Event Chain in the Declared Source Set

| Link | Implementation | Evidence |
|---|---|---|
| Source business event | Customer invoice / vendor bill / miscellaneous entry | base application |
| Tax trigger | **None.** The trigger is document posting; the period attribute is the move's accounting date. A tax-point-bearing field exists but does not drive selection. | `smesplus_tax_period_date/models/tax_period.py:23`, `:36`; `smesplus_account_reports/models/account_generic_tax_report.py:26` |
| Tax base | Repartition-engine base (`tdr.base_amount`) on the main reports; `account_move_line.balance` on the zero-rate reports; `price_subtotal` in the withholding path | `account_generic_tax_report.py:49`, `:250`, `:420` |
| Tax calculation | Base application tax engine, driven by `account.tax` template rows | `l10n_th/data/template/account.tax-th.csv` |
| Tax document | Print-time title substitution to the literal `Tax Invoice`; no document object, no number, no issuance event | `l10n_th/views/report_invoice.xml:14-16`; `l10n_th/models/account_move.py:7-11` |
| Tax accounting event | Tax line on the accounting move, tagged with the report tags carried by the tax's repartition lines | base application; tags from `account.tax-th.csv` |
| Journal | Output tax to the VAT payable account, input tax to the VAT receivable account, per template | `account.tax.group-th.csv` (`tax_payable_account_id`, `tax_receivable_account_id`) |
| Tax report | **Two parallel implementations** of the s.87 books — see §6 | `l10n_th_reports`, `l10n_th_reports_ext`, `smesplus_account_reports` |
| Filing / adjustment / close | One `account.return.type` record; no branch filing unit; credit notes netted by sign; no original-invoice reference | `l10n_th_reports/data/account_return_data.xml:4-8`; `account_generic_tax_report.py:87` |

## 4. Divergence Table

| # | Statutory link | Implemented as | Consequence |
|---|---|---|---|
| `V-D-01` | Tax point is an **event**, distinct from the accounting date | Accounting date | A supply whose tax point falls in month M but which is booked in month M−1 is reported in M−1. The system cannot represent the difference even though it stores a field for it. |
| `V-D-02` | Services: tax point is **receipt of payment** | Posting of the invoice | Service supplies are systematically reported on an accrual basis where the statute prescribes a payment basis, unless cash-basis tax exigibility is configured on every service tax. The reports do honour `tax_exigible` (`account_generic_tax_report.py:59`), so cash-basis configuration is the only available mechanism; whether it is applied is a configuration question, recorded as `P07-U-16`. |
| `V-D-03` | Tax invoice is a numbered statutory document issued at the tax point | Print rendering of the accounting document | No issuance timestamp, no serial number distinct from the journal sequence, no copy, no reissue, no cancellation of a document (only reversal of an accounting entry). |
| `V-D-04` | Credit / debit note adjusts in the month **issued / received**, referencing the original tax invoice | Reversal entry netted by sign in the same report population | The adjustment is not identifiable as an adjustment, is not linked to the original tax invoice, and is placed by accounting date rather than by note date. |
| `V-D-05` | Filing is **per place of business** | Per company, optionally grouped across companies as a tax unit | The statutory filing unit is not representable. |
| `V-D-06` | Zero-rated (s.80/1) and exempt (s.81) are distinct classes | Both selected by `amount_tax = 0` at **move** level | On a mixed-rate invoice the zero-rated and exempt portions appear on neither the main report (excluded by the group-name predicate) nor the zero report (excluded because the move's total tax is non-zero). |

## 5. Where `ONE TAX FACT -> ONE CANONICAL TAX EVENT -> ONE ACCOUNTING EFFECT` Is Broken

| # | Break | Evidence |
|---|---|---|
| `V-I-01` | **One tax fact, two report implementations.** The same statutory output/input tax books are produced by two independent code paths with different selection logic, different column semantics and different branch sources: the vendor XLSX generator as overridden by SMEsPlus, and the SMEsPlus dynamic reports. Neither is declared canonical. | `l10n_th_reports/models/tax_report_vat.py:58` vs `l10n_th_reports_ext/models/tax_report_vat.py:11` vs `smesplus_account_reports/models/account_generic_tax_report.py:23` |
| `V-I-02` | **One tax fact, two period attributes.** The period a supply belongs to is determined by the accounting date, while a second period attribute is stored on the move and shown next to it on the same report row. A reader of that report sees two dates and no rule for which governs. | `account_generic_tax_report.py:26` (selection) vs `:38`, `:102-108` (display) |
| `V-I-03` | **One canonical event, two base amounts.** The main reports take the base from the tax repartition detail; the zero-rate reports take it from the raw line balance and take the tax from the **move header** `amount_tax`. A move with several zero-rated lines repeats the header tax amount on every line. | `account_generic_tax_report.py:49-50` vs `:250-251`, `:420-423` |
| `V-I-04` | **Row inclusion depends on a mutable label rather than on the tax fact.** A row reaches the statutory report only if its tax group's English name is exactly `VAT 7%`. The predicate is a company-mutable, translatable label standing in for "is this a standard-rated Thai VAT supply". | `account_generic_tax_report.py:88` |

## 6. The Two Parallel Report Implementations

| Attribute | Vendor generator (+ SMEsPlus override) | SMEsPlus dynamic reports |
|---|---|---|
| Entry point | XLSX export buttons on the Thai tax report | Dedicated `account.report` records |
| Selection | `strict_range` + membership of the report's base/tax tags | `strict_range` + tax-detail query + literal tax-group-name equality |
| Partner handling | Partnerless rows retained with the caption `Selling goods or providing services` | Partnerless rows **dropped** by an inner join on `res_partner` |
| Branch source | `l10n_th_branch_name` (from `company_registry`), plus `partner.branch` added by the override | `company_registry` |
| Tax-point column | none (override adds "Bill Date" = invoice date, relabels the selection date "Accounting Date") | "Tax Period Date" column, not used for selection |
| Zero / exempt | Included if the tags match | Excluded from the main report; separate report keyed on move-level `amount_tax = 0` |
| Licence of the inherited base | `OEEL-1` (Enterprise) | inherits `account_reports` (Enterprise) |

Both are in the declared source set and both are installable. Selecting between them is a
design decision that has not been recorded anywhere in the declared set.

## 7. Negative Claims Made in This File

| ID | Claim | Class | Boundary |
|---|---|---|---|
| `P07-N-06` | No tax-point determination logic for VAT was found. | `B — NOT FOUND IN SEARCHED SCOPE` | PATH SET of `13 §2`; patterns of `13 §4`; all 15 modules of `13 §5` read for tax-date handling |
| `P07-N-07` | No import tax point and no s.78/3 special tax point were found. | `B — NOT FOUND IN SEARCHED SCOPE` | as above |
| `P07-N-08` | No self-assessed VAT mechanism (s.83/6) was found in the Thai modules. | `B — NOT FOUND IN SEARCHED SCOPE` | Thai module population only; the base application's reverse-charge facilities were **not** examined |

None of these is stated as "does not exist".
