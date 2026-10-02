# U134 — l10n_th WHT PND Form Generation L3 Deep (GAP-046, P0 TH)

**Unit:** U134 | **Gap:** GAP-046 | **Priority:** P0 | **Date:** 2026-10-02

## Research Scope

Deep technical investigation of Thai withholding tax (WHT) PND form generation in Odoo 19.0
Community, covering all applicable L1–L12 layers.

---

## L1 — Manifest / Dependencies

**Module:** `l10n_th` (only Thai localization module present)

File: `l10n_th/__manifest__.py:16-19`
```
'depends': ['account_qr_code_emv', 'account'],
```
- `l10n_th` has NO dependency on `l10n_account_withholding_tax`
- `l10n_account_withholding_tax` is a SEPARATE community module with no Thai-specific ties
- No `l10n_th_withholding_tax` module exists in community addons
- `auto_install: ['account']` — installs automatically when account is installed for TH country
- Data loaded: `data/account_tax_report_data.xml`, `views/report_invoice.xml`
- CSV templates loaded via chart template mechanism

File: `l10n_account_withholding_tax/__manifest__.py:7`
```
'depends': ['account'],
```
No Thai dependency whatsoever.

---

## L2 — Models / Fields / ORM

### l10n_th Models

**account_move.py** (`l10n_th/models/account_move.py:4-11`)
- Inherits `account.move`
- Only override: `_get_name_invoice_report()` — returns `'l10n_th.report_invoice_document'` when company fiscal country = TH
- NO WHT-specific fields added to `account.move` by `l10n_th`
- No `l10n_th_withholding_tax_id`, no `l10n_th_withholding_tax_base_amount` fields

**res_partner.py** (`l10n_th/models/res_partner.py:9-18`)
- Adds computed field `l10n_th_branch_name` on `res.partner`
- Derives from `company_registry` for TH companies — "Branch {code}" or "Headquarter"
- Used in invoice QWeb report only

**template_th.py** (`l10n_th/models/template_th.py:9-43`)
- Abstract model `account.chart.template` with `@template('th')`
- Sets default accounts for AR, AP, stock valuation, cash, income, expense
- Sets default sale tax = `tax_output_vat`, purchase tax = `tax_input_vat`

**res_bank.py** (`l10n_th/models/res_bank.py`)
- Thai QR payment proxy types: `ewallet_id`, `merchant_tax_id`, `mobile`
- No WHT relevance

### WHT Tax Templates (12 templates)

File: `l10n_th/data/template/account.tax-th.csv`

**PND53 Company WHT (4 templates):**
- `tax_wht_co_1`: 1% WHT Company Transportation — `type_tax_use=purchase`, `amount=-1.0`, tag=`Income PND53`/`PND53`, credit account=`l10n_th_account_213302`, `use_in_tax_closing=False`
- `tax_wht_co_2`: 2% WHT Company Advertising — same structure, credit `213302`
- `tax_wht_co_3`: 3% WHT Company Service — same structure, credit `213302`
- `tax_wht_co_5`: 5% WHT Company Rental — same structure, credit `213302`

**PND3 Personal WHT (4 templates):**
- `tax_wht_pers_1`: 1% WHT Personal Transportation — `type_tax_use=purchase`, tag=`Income PND3`/`PND3`, credit account=`l10n_th_account_213301`
- `tax_wht_pers_2`: 2% WHT Personal Advertising — same structure, credit `213301`
- `tax_wht_pers_3`: 3% WHT Personal Service — same structure, credit `213301`
- `tax_wht_pers_5`: 5% WHT Personal Rental — same structure, credit `213301`

**Income WHT / Receivable (4 templates — seller-side):**
- `tax_wht_income_1/2/3/5`: Withholding Income Tax 1/2/3/5% — `type_tax_use=sale`, debit account=`l10n_th_account_114300` (WHT Creditable asset), no PND tag

**CRITICAL FINDING:** None of the 12 WHT templates set `is_withholding_tax_on_payment=True`. They use standard invoice-time tax calculation, NOT the `l10n_account_withholding_tax` payment-time mechanism.

### Tax Groups (WHT)

File: `l10n_th/data/template/account.tax.group-th.csv`
- `tax_group_1/2/3/5`: WHT 1/2/3/5%, `tax_payable_account_id=l10n_th_account_213500`, `tax_receivable_account_id=l10n_th_account_114401`

### WHT-Related Accounts

File: `l10n_th/data/template/account.account-th.csv`
- `114300`: WHT Creditable (asset_current) — prepaid tax, seller side, claimable against CIT
- `114401`: WHT Receivable (asset_receivable) — tax closing account for WHT credits
- `213301`: Tax Withheld - PND 3 (liability_current) — monthly remittance via PND3 form
- `213302`: Tax Withheld - PND 53 (liability_current) — monthly remittance via PND53 form
- `213500`: WHT Payable (liability_payable) — consolidated WHT for lump-sum revenue payment

### l10n_account_withholding_tax Models

**account_tax.py** (`l10n_account_withholding_tax/models/account_tax.py:13-23`)
- Adds `is_withholding_tax_on_payment` Boolean field to `account.tax`
- Adds `withholding_sequence_id` Many2one to `ir.sequence`
- Constrains: WHT-on-payment taxes cannot use group/division amount types
- Mutually exclusive with cash basis tax exigibility

**account_withholding_line.py** (`l10n_account_withholding_tax/models/account_withholding_line.py:10-556`)
- Abstract model `account.withholding.line` — core WHT logic
- Fields: `tax_id`, `base_amount`, `amount`, `account_id`, `name` (sequence number)
- Computes paid factor for partial payments, installments, early payment discounts
- `_prepare_withholding_amls_create_values()` creates 4 AML entries per WHT line

**account_payment_withholding_line.py** (`l10n_account_withholding_tax/models/account_payment_withholding_line.py`)
- Concrete model `account.payment.withholding.line` — persisted WHT on payment
- Linked to `account.payment` via `payment_id`

**account_payment.py** (`l10n_account_withholding_tax/models/account_payment.py`)
- Extends `account.payment` with `withholding_line_ids`, `should_withhold_tax`
- `_prepare_move_withholding_lines()` creates WHT journal items when payment is confirmed

**res_company.py** (`l10n_account_withholding_tax/models/res_company.py:12-15`)
- Adds `withholding_tax_base_account_id` to `res.company`

---

## L3 — Workflow / State Machine

### PND Report as account.report Framework Records

File: `l10n_th/data/account_tax_report_data.xml:227-353`

**PND53 Report** (`id=tax_report_pnd53`, `model=account.report`):
- Lines: Total Income (`INCOME_PND53`, engine=tax_tags, formula=`Income PND53`)
- Lines: Total Remittance (`P53`, engine=tax_tags, formula=`PND53`)
- Lines: Surcharge (`S53`, engine=tax_tags, formula=`SUR53`)
- Lines: Total = `P53.balance + S53.balance`

**PND3 Report** (`id=tax_report_pnd3`, `model=account.report`):
- Lines: Total Income (`INCOME_PND3`, engine=tax_tags, formula=`Income PND3`)
- Lines: Total Remittance (`P3`, engine=tax_tags, formula=`PND3`)
- Lines: Surcharge (`S3`, engine=tax_tags, formula=`SUR3`)
- Lines: Total = `P3.balance + S3.balance`

**CRITICAL GAP FINDING:**
1. PND3 and PND53 exist ONLY as summary `account.report` records — they are financial reports showing totals, NOT form-generating workflows with per-vendor detail lines.
2. There is NO PND-1 (monthly employment income WHT) report defined anywhere in community.
3. There is NO per-vendor WHT certificate model. No `account.wht.cert` or equivalent.
4. There is NO wizard to generate/print PND forms with vendor detail.
5. There is NO statutory form layout (the Revenue Department requires specific field layout).
6. PND forms as implemented show only: Total Income, Total Remittance, Surcharge, Total. Missing: payee name, tax ID, income type, income amount per payee, payment date per line.

### WHT at Invoice vs. at Payment

**l10n_th approach (invoice-time):**
- WHT is a standard purchase tax with negative amount
- Applied when vendor bill is posted
- No payment-time deduction mechanism
- No wizard to manage WHT at payment time

**l10n_account_withholding_tax approach (payment-time):**
- Requires `is_withholding_tax_on_payment=True` on tax
- Shows WHT tab on payment register wizard
- Creates 4 journal entries at payment: Outstanding, Tax withheld, WHT base, WHT base counterpart
- Has sequence number mechanism for WHT certificate numbers
- NOT used by l10n_th templates — they are completely separate

### State Summary for WHT PND

| State | Present? | Notes |
|-------|----------|-------|
| Draft WHT certificate | ABSENT | No WHT certificate model |
| Confirmed WHT certificate | ABSENT | No WHT certificate model |
| PND form wizard | ABSENT | No PND generation wizard |
| Per-vendor WHT lines | ABSENT | Only aggregate report lines |
| WHT certificate printout | ABSENT | No QWeb template for Thai WHT certificate |
| Revenue Dept filing status | ABSENT | No filing state tracking |
| PND-1 (salary) | ABSENT | Not in community at all |

---

## L4 — Cross-Module Dependencies

- `l10n_th` + `l10n_account_withholding_tax` are INDEPENDENT community modules
- No bridge/glue module connecting them
- Thai WHT templates use standard invoice taxes, not `is_withholding_tax_on_payment`
- To get payment-time WHT for Thailand, manual configuration required:
  1. Install `l10n_account_withholding_tax`
  2. Enable `is_withholding_tax_on_payment` on Thai WHT taxes manually
  3. Set up `withholding_tax_base_account_id` on company
  4. Configure sequences for WHT certificate numbering
- Even after manual config, there are still no PND form generation wizards or certificates

---

## L5 — Views / Wizards / Reports

### l10n_th Views

**report_invoice.xml** (`l10n_th/views/report_invoice.xml`)
- Inherits `account.report_invoice_document` — adds `l10n_th_branch_name` after VAT number
- Creates `report_commercial_invoice` QWeb PDF action
- Bound to `account.move` model for TH country, sale journal
- This is ONLY for sales invoices — NOT for PND or WHT certificates

**No WHT-specific views in l10n_th:**
- No PND form views
- No WHT certificate views
- No wizard views for PND generation

### l10n_account_withholding_tax Views

**account_payment_views.xml** — Adds withholding tab to payment form
**account_tax_views.xml** — Adds `is_withholding_tax_on_payment` field to tax form
**report_payment_receipt_templates.xml** (`l10n_account_withholding_tax/views/report_payment_receipt_templates.xml:1-37`)
- Adds WHT lines table to payment receipt printout
- Shows: Tax name, Withholding number, Base, Amount
- This is a GENERIC payment receipt, not a Thai PND statutory form
**wizards/account_payment_register_views.xml** — Adds withholding lines to payment register wizard

---

## L6 — Access / Record Rules / sudo

- `l10n_account_withholding_tax/security/ir.model.access.csv` — access rules for `account.payment.withholding.line` and `account.payment.register.withholding.line`
- No Thai-specific record rules for WHT
- No sudo escalation for PND generation

---

## L7 — Config Prerequisites

For WHT to function at all (invoice-time, l10n_th only):
- Install `l10n_th` module (auto-installs with account for TH)
- Chart of accounts loads WHT tax templates and accounts

For payment-time WHT (requires additional setup):
- Install `l10n_account_withholding_tax`
- Set `withholding_tax_base_account_id` on company (Setting > Accounting > Default Accounts)
- Manually enable `is_withholding_tax_on_payment` on Thai WHT taxes
- Create `ir.sequence` records for WHT certificate numbering

Neither configuration produces statutory-compliant PND forms.

---

## L8 — Immutability / Audit

- No Thai-specific audit trail for WHT records
- Standard journal entry locking applies after accounting close
- No WHT certificate lock/immutability enforcement
- `use_in_tax_closing=False` for all WHT taxes — they bypass the standard tax closing reconciliation

---

## L9 — Accounting Postings

### Vendor WHT (buyer withholds from vendor payment)

**At bill posting (l10n_th standard):**
```
DR  Expense / Service account        1,000
    CR  Accounts Payable                       900
    CR  Tax Withheld - PND3 (213301)           100  [personal vendor]
    -- OR --
    CR  Tax Withheld - PND53 (213302)          100  [company vendor]
```

**At payment (l10n_account_withholding_tax, if configured):**
```
DR  Accounts Payable                 1,000
    CR  WHT Base (grouping account)            1,000
    CR  Tax Withheld                             100
    CR  Outstanding (bank)                       900
DR  WHT Base Counterpart             1,000
    CR  WHT Base (counterpart)                 1,000
```

### Seller WHT Receivable (customer withholds from seller)

**At invoice posting:**
```
DR  WHT Creditable (114300)            100
DR  Accounts Receivable                900
    CR  Revenue                                1,000
```

### Tax Closing Transfer (manual/month-end)

WHT payable accounts (213301/213302) transfer to `213500` (WHT Payable) for lump-sum payment.
`tax_group_1/2/3/5` point payable→`213500`, receivable→`114401`.

---

## L10 — Cron / Queue / Import-Export

- No cron job for PND form generation
- No automated WHT certificate generation
- No import/export mechanism for PND data
- No e-filing integration for Revenue Department submission

---

## L11 — API Surface

- No dedicated REST API endpoint for PND generation
- Standard ORM-based access via Odoo JSON-RPC
- No external API for WHT certificate retrieval
- PND3/PND53 `account.report` records accessible via standard report API

---

## L12 — Runtime / AWT

- `l10n_account_withholding_tax/static/src/helpers/*.js` — JavaScript helpers for WHT UI
- No Thai-specific runtime behavior
- WHT lines computed client-side in payment register wizard
- No AWT-specific Thai WHT functionality

---

## GAP-046 Assessment

**FINDING: GAP-046 CONFIRMED — Thai WHT PND form generation is NOT at L3.**

Evidence summary:
1. PND3 and PND53 exist ONLY as `account.report` aggregate summary records — not form-generating wizards
2. PND-1 (salary/employment income) is COMPLETELY ABSENT from community
3. No WHT certificate model with per-vendor detail lines
4. No statutory PND form QWeb templates with Revenue Dept layout
5. WHT taxes use invoice-time mechanism without `is_withholding_tax_on_payment`
6. `l10n_account_withholding_tax` (payment-time WHT) is not linked to Thai templates
7. No filing status tracking, no certificate state machine, no sequence auto-generation

**L3 Gap:** The workflow state machine for generating, confirming, and printing statutory PND forms does not exist. The per-vendor WHT detail required by Thai Revenue Department (payee name, tax ID, income type code, income amount, WHT amount per payee) cannot be produced from community code.

---

## L1–L12 Applicability Matrix

| Layer | Applicable | Status | Notes |
|-------|-----------|--------|-------|
| L1 Manifest | Yes | C1 | l10n_th has no WHT module dependency |
| L2 Models | Yes | C1 | No WHT certificate model, 12 tax templates present |
| L3 Workflow | Yes | GAP | No PND form generation workflow, ABSENT PND-1 |
| L4 Cross-module | Yes | GAP | l10n_th and l10n_account_withholding_tax unlinked |
| L5 Views | Yes | GAP | No PND form views, no WHT certificate view |
| L6 Access | Partial | C1 | Generic access rules only |
| L7 Config | Yes | C2 | Manual steps needed for payment-time WHT |
| L8 Immutability | Partial | C1 | Standard entry locking, no WHT-specific |
| L9 Accounting | Yes | C1 | Double-entry patterns documented |
| L10 Cron | No | ABSENT | No automated PND generation |
| L11 API | No | ABSENT | No dedicated API |
| L12 Runtime | Partial | C1 | JS helpers for payment UI only |
