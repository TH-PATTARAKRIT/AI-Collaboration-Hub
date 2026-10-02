# U212 — account.payment.term: Payment Terms, Installment Computation, Early Payment Discount

**Unit**: U212  
**Module**: account (account_payment_term)  
**Source file**: `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/account/models/account_payment_term.py`  
**SHA-256**: `9a7bc9c1cec9a76c3046311d8c10a4df92d80de6e90215a9b3b459aa700e12c5`  
**Date researched**: 2026-10-02  
**Researcher**: STATE03 VDR Worker (Claude Sonnet 4.6)

---

## 1. Model: `account.payment.term` (line 11)

**Class**: `AccountPaymentTerm`  
**_name**: `account.payment.term`  
**_order**: `sequence, id` (line 14)  
**_check_company_domain**: `models.check_company_domain_parent_of` (line 15)

### Key Fields

| Field | Type | Line | Notes |
|-------|------|------|-------|
| `name` | `Char` | 23 | Required, translate=True |
| `active` | `Boolean` | 24 | Default True; archivable |
| `note` | `Html` | 25 | Description on invoice, translate=True |
| `line_ids` | `One2many` → `account.payment.term.line` | 26 | `payment_id` FK; copy=True; default=`_default_line_ids` |
| `company_id` | `Many2one` → `res.company` | 27 | Optional (blank = all companies) |
| `sequence` | `Integer` | 29 | Default 10; drives ordering |
| `currency_id` | `Many2one` → `res.currency` | 30 | Computed from company or env.company |
| `display_on_invoice` | `Boolean` | 32 | "Show installment dates", default True |
| `discount_percentage` | `Float` | 39 | Early Payment Discount %; default 2.0 |
| `discount_days` | `Integer` | 40 | Days before early-pay window closes; default 10 |
| `early_pay_discount_computation` | `Selection` | 41-45 | `included` / `excluded` / `mixed`; computed from country |
| `early_discount` | `Boolean` | 46 | Master switch for early discount feature |

### Default line (line 17-18)
```python
def _default_line_ids(self):
    return [Command.create({'value': 'percent', 'value_amount': 100.0, 'nb_days': 0})]
```
Creates a single 100% balance-due-immediately line on new terms.

---

## 2. Model: `account.payment.term.line` (line 281)

**Class**: `AccountPaymentTermLine`  
**_name**: `account.payment.term.line`  
**_order**: `id`

### Key Fields

| Field | Type | Line | Notes |
|-------|------|------|-------|
| `value` | `Selection` | 286-289 | `percent` or `fixed` (no `balance` type in v19) |
| `value_amount` | `Float` | 291-293 | For percent: 0–100; digits='Payment Terms'; computed+stored |
| `delay_type` | `Selection` | 294-299 | `days_after` / `days_after_end_of_month` / `days_after_end_of_next_month` / `days_end_of_month_on_the` |
| `nb_days` | `Integer` | 307 | Number of days offset; computed+stored |
| `days_next_month` | `Char` | 301-306 | Day-of-month for `days_end_of_month_on_the`; size=2, default '10' |
| `payment_id` | `Many2one` → `account.payment.term` | 308 | cascade delete |

**NOTE**: In v19 the `value` selection has only `percent` and `fixed`. There is no separate `balance` type — the last line in `_compute_terms()` is implicitly treated as the balance line regardless of its `value` type (line 227: `on_balance_line = i == len(self.line_ids) - 1`).

---

## 3. `_compute_terms()` — Installment Date / Amount Computation (lines 171–256)

**Signature**:
```python
def _compute_terms(self, date_ref, currency, company, tax_amount, tax_amount_currency,
                   sign, untaxed_amount, untaxed_amount_currency, cash_rounding=None)
```

### Algorithm

1. **Rate calculation** (line 190): `rate = abs(total_amount_currency / total_amount)` — used to convert fixed amounts from invoice currency to company currency.

2. **Result dict initialised** (lines 192–198): Contains `total_amount`, `discount_percentage`, `discount_date`, `discount_balance`, `line_ids`.

3. **Early discount pre-calculation** (lines 200–214):
   - `discount_date = date_ref + relativedelta(days=discount_days)`
   - For `excluded` or `mixed`: discount applies only to the untaxed portion → `discount_balance = round(total - untaxed * pct)`
   - For `included`: discount applies to total → `discount_balance = round(total * (1 - pct))`
   - Cash rounding adjustment applied to `discount_amount_currency` if applicable.

4. **Line iteration** (lines 219–254):
   - Date: via `line._get_due_date(date_ref)` (delegated to term-line method)
   - Last line (balance): receives `residual_amount` and `residual_amount_currency` directly — ensures total adds up exactly without rounding drift.
   - `fixed` lines: `company_amount = sign * round(value_amount / rate)`; `foreign_amount = sign * round(value_amount)`
   - `percent` lines: `company_amount = round(total * pct/100)`; `foreign_amount = round(total_currency * pct/100)`
   - Cash rounding applied per non-balance line; balance line absorbs remainder.
   - Running `residual_amount` subtracted at each step (lines 252–253).

---

## 4. `_get_due_date()` — Date Computation per Line (lines 310–327)

```python
def _get_due_date(self, date_ref):
```

| `delay_type` | Calculation |
|---|---|
| `days_after` | `date_ref + relativedelta(days=nb_days)` |
| `days_after_end_of_month` | `end_of(date_ref, 'month') + relativedelta(days=nb_days)` |
| `days_after_end_of_next_month` | `end_of(date_ref + relativedelta(months=1), 'month') + relativedelta(days=nb_days)` |
| `days_end_of_month_on_the` | `date_ref + relativedelta(days=nb_days) + relativedelta(months=1, day=days_next_month)` (if days_next_month>0); else `end_of(date_ref + relativedelta(days=nb_days), 'month')` |

---

## 5. Early Payment Discount Fields (lines 39–46, 200–214)

### `early_discount` (Boolean, line 46)
Master on/off switch. When False, no discount is computed.

### `discount_percentage` (Float, line 39)
The percentage discount offered. Default 2.0. Validated: must be >0.0 when `early_discount` is True (line 166–167).

### `discount_days` (Integer, line 40)
Number of days from invoice date within which early payment qualifies. Default 10. Validated: must be >0 when `early_discount` is True (line 168–169).

### `early_pay_discount_computation` (Selection, lines 41–45)
Computed field — driven by `company_id.country_code` (lines 81–90):
- `BE` → `mixed`
- `NL` → `excluded`
- All others → `included`

**Meaning of values**:
- `included` ("On early payment"): discount applies to full invoice total (tax included). `discount_balance = total * (1 - pct)`.
- `excluded` ("Never"): discount applies only to untaxed base; taxes not reduced. `discount_balance = total - untaxed * pct`.
- `mixed` ("Always (upon invoice)"): same formula as `excluded` but discount is applied unconditionally on invoice posting.

### Constraint on early discount (lines 163–169)
- Cannot have `early_discount=True` with more than one `line_ids` entry.
- `discount_percentage` must be strictly positive.
- `discount_days` must be strictly positive.

---

## 6. `_check_lines()` — Validation (lines 156–169)

```python
@api.constrains('line_ids', 'early_discount')
def _check_lines(self):
    round_precision = self.env['decimal.precision'].precision_get('Payment Terms')
    total_percent = sum(line.value_amount for line in terms.line_ids if line.value == 'percent')
    if float_round(total_percent, precision_digits=round_precision) != 100:
        raise ValidationError(...)
```

- Sums all `percent`-type line `value_amount` values.
- Uses `float_round` at 'Payment Terms' decimal precision.
- Raises `ValidationError` if sum ≠ 100%.
- Raises `ValidationError` if `early_discount=True` and `len(line_ids) > 1`.

---

## 7. Currency Rounding in Term Computation

Lines 204–214 and 233–250 show two-pass rounding:

1. **Per-line rounding**: Each non-balance line's `foreign_amount` is rounded via `currency.round(...)` and `company_amount` via `company_currency.round(...)`.
2. **Cash rounding adjustment**: If `cash_rounding` is provided, `cash_rounding.compute_difference(currency, term_vals['foreign_amount'])` is computed; if non-zero, added to `foreign_amount`, then `company_amount` recomputed from `foreign_amount / rate`.
3. **Balance line absorbs residual**: `residual_amount` accumulates rounding differences; last line takes the entire residual — no rounding is applied to the balance line directly.

---

## 8. `invoice_payment_term_id` on `account.move` and `date_maturity` on `account.move.line`

**Source**: `/account/models/account_move.py`, lines 406–410, 1388–1457

- `invoice_payment_term_id` = `Many2one('account.payment.term')` on `account.move` (line 406). Stored, computed from partner's `property_payment_term_id` / `property_supplier_payment_term_id` (line 1081–1089).

- `_compute_needed_terms()` (lines 1388–1457): Called when `invoice_payment_term_id`, `invoice_date`, `currency_id`, `amount_total_in_currency_signed`, or `invoice_date_due` changes.

- Calls `invoice_payment_term_id._compute_terms(...)` (line 1418) passing `date_ref=invoice.invoice_date`, separated tax/untaxed amounts, `cash_rounding`, and `sign`.

- For each `term_line` in result `line_ids`, creates a `frozendict` key with `date_maturity = fields.Date.to_date(term_line.get('date'))` (line 1432).

- The `discount_date`, `discount_balance`, `discount_amount_currency` from the payment term computation are passed into each `account.move.line` record of `display_type='payment_term'` (lines 1433–1440).

- If no `invoice_payment_term_id` but `invoice_date_due` exists (line 1447–1457): single needed_term entry with `date_maturity=invoice_date_due` and full amount.

---

## 9. Multi-Company: `company_id` on Payment Terms

- `company_id` is optional (`Many2one('res.company')`, no `required=True`) at line 27.
- `_check_company_domain = models.check_company_domain_parent_of` (line 15): enforces that a company-specific term is only used by that company or its children.
- `currency_id` computed as `company_id.currency_id or self.env.company.currency_id` (line 59): falls back to the current user's company if term has no company restriction.
- `early_pay_discount_computation` computed from `company_id.country_code or self.env.company.country_code` (lines 83–84): terms with no company restriction pick up the current user's country context.

---

## 10. MIGRATION FLAGS — Early Payment Discount in v17/v18/v19

The following fields are **confirmed present in v19**:
- `early_discount` (Boolean)
- `discount_percentage` (Float, default 2.0)
- `discount_days` (Integer, default 10)
- `early_pay_discount_computation` (Selection: included/excluded/mixed)
- `_get_amount_due_after_discount()` method
- `_get_last_discount_date()` / `_get_last_discount_date_formatted()` methods
- `discount_date`, `discount_balance`, `discount_amount_currency` on move lines

These fields were **introduced in Odoo 16** (early payment discount feature was added in the v16 cycle). They are **NOT present in v14 or v15**. Any migration from a pre-v16 database will require:
1. Populating `early_discount=False` for all existing payment terms.
2. No data loss risk as the fields are additive.
3. The `early_pay_discount_computation` value is auto-computed per company country — no manual migration needed.

**`delay_type` field** on `account.payment.term.line`: In earlier versions, `day_of_the_month` was a separate integer field. In v19, the `days_end_of_month_on_the` delay_type with `days_next_month` (Char) replaces this pattern. This is a **structural change** for migrators from v14/v15.

**`value` selection change**: In older versions (v14/v15), `value` had `balance`, `percent`, `fixed` options. In v19, `balance` is removed — the last line is implicitly the balance (line 227). **MIGRATION FLAG**: Any v14/v15 data with `value='balance'` lines must be converted to `value='percent'` with `value_amount=100`.
