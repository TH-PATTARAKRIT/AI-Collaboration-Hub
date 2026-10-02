# U204 — account.move.line: Journal Item Model Fields, Debit/Credit, Reconciliation, Analytic Distribution

**Research unit**: U204  
**Addon**: `account`  
**Primary source file**: `account/models/account_move_line.py` (3 833 lines)  
**Supporting files**:
- `account/models/account_partial_reconcile.py`
- `account/models/account_full_reconcile.py`
- `account/models/account_move.py`

---

## 1. Model Identity

**File**: `account/models/account_move_line.py:20-26`

```python
class AccountMoveLine(models.Model):
    _name = 'account.move.line'
    _inherit = ["analytic.mixin"]
    _description = "Journal Item"
    _order = "date desc, move_name desc, id"
    _check_company_auto = True
```

The model inherits `analytic.mixin` (defined in `analytic/models/analytic_mixin.py`), which provides the `analytic_distribution` JSON field.

---

## 2. Key Accounting Fields

### 2.1 debit / credit / balance

**File**: `account/models/account_move_line.py:116-131`

```python
debit = fields.Monetary(
    compute='_compute_debit_credit', inverse='_inverse_debit', store=True, precompute=True,
    currency_field='company_currency_id',
)
credit = fields.Monetary(
    compute='_compute_debit_credit', inverse='_inverse_credit', store=True, precompute=True,
    currency_field='company_currency_id',
)
balance = fields.Monetary(
    compute='_compute_balance', store=True, readonly=False, precompute=True,
    currency_field='company_currency_id',
    tracking=True,
)
```

The primary stored field is **`balance`** (positive = debit, negative = credit). `debit` and `credit` are derived:

**File**: `account/models/account_move_line.py:747-754`

```python
@api.depends('balance')
def _compute_debit_credit(self):
    for line in self:
        if not line.is_storno:
            line.debit = line.balance if line.balance > 0.0 else 0.0
            line.credit = -line.balance if line.balance < 0.0 else 0.0
        else:
            line.debit = line.balance if line.balance < 0.0 else 0.0
            line.credit = -line.balance if line.balance > 0.0 else 0.0
```

**DB constraint**: `account/models/account_move_line.py:483-485`

```python
_check_credit_debit = models.Constraint(
    "CHECK(display_type IN ('line_section', 'line_subsection', 'line_note') OR credit * debit=0)",
    'Wrong credit or debit value in accounting entry!',
)
```

Debit and credit cannot both be non-zero simultaneously (except for storno accounting).

**Inverse methods**: `account/models/account_move_line.py:1425-1439`

```python
@api.onchange('debit')
def _inverse_debit(self):
    for line in self:
        line.is_storno = line.debit < 0
        if line.debit:
            line.credit = 0
        line.balance = line.debit - line.credit

@api.onchange('credit')
def _inverse_credit(self):
    for line in self:
        line.is_storno = line.credit < 0
        if line.credit:
            line.debit = 0
        line.balance = line.debit - line.credit
```

### 2.2 amount_currency / currency_id

**File**: `account/models/account_move_line.py:142-151`

```python
amount_currency = fields.Monetary(
    compute='_compute_amount_currency', inverse='_inverse_amount_currency', store=True, readonly=False, precompute=True,
)
currency_id = fields.Many2one(
    comodel_name='res.currency',
    compute='_compute_currency_id', store=True, readonly=False, precompute=True,
    required=True,
)
```

**Sign constraint**: `account/models/account_move_line.py:487-490`

```python
_check_amount_currency_balance_sign = models.Constraint(
    "CHECK(... (balance <= 0 AND amount_currency <= 0) OR (balance >= 0 AND amount_currency >= 0) ...)",
    'The amount expressed in the secondary currency must be positive when account is debited...',
)
```

`amount_currency` follows the sign of `balance`. When `currency_id == company_currency_id`, `amount_currency == balance`.

### 2.3 account_id / partner_id

**File**: `account/models/account_move_line.py:94-105, 153-158`

- `account_id`: computed+stored+writable, `check_company=True`, `ondelete='restrict'`
- `partner_id`: computed from `move_id.partner_id.commercial_partner_id`, stored, inversible

---

## 3. move_type — Denormalized vs. Related

**File**: `account/models/account_move_line.py:91`

```python
move_type = fields.Selection(related='move_id.move_type')
```

`move_type` on the move line is a **non-stored related field** — it delegates to `move_id.move_type` at runtime. It is NOT stored in `account_move_line` table, no denormalization. The canonical definition is on `account.move`:

**File**: `account/models/account_move.py:143-160`

```python
move_type = fields.Selection(
    selection=[
        ('entry', 'Journal Entry'),
        ('out_invoice', 'Customer Invoice'),
        ('out_refund', 'Customer Credit Note'),
        ('in_invoice', 'Vendor Bill'),
        ('in_refund', 'Vendor Credit Note'),
        ('out_receipt', 'Sales Receipt'),
        ('in_receipt', 'Purchase Receipt'),
    ],
    ...
    default="entry",
)
```

---

## 4. Tax Fields

### 4.1 tax_ids

**File**: `account/models/account_move_line.py:195-205`

```python
tax_ids = fields.Many2many(
    comodel_name='account.tax',
    relation='account_move_line_account_tax_rel',
    column1='account_move_line_id',
    column2='account_tax_id',
    string="Taxes",
    compute='_compute_tax_ids', store=True, readonly=False, precompute=True,
    ...
)
```

Applied taxes on a **product/base line**. The M2M join table is `account_move_line_account_tax_rel`.

### 4.2 tax_line_id and tax_repartition_line_id

**File**: `account/models/account_move_line.py:212-233`

```python
tax_line_id = fields.Many2one(
    comodel_name='account.tax',
    related='tax_repartition_line_id.tax_id', store=True, precompute=True,
    ondelete='restrict',
    help="Indicates that this journal item is a tax line"
)
tax_repartition_line_id = fields.Many2one(
    comodel_name='account.tax.repartition.line',
    string="Originator Tax Distribution Line",
    ondelete='restrict',
    readonly=True,
    check_company=True,
    help="Tax distribution line that caused the creation of this move line, if any"
)
```

- `tax_line_id` is **derived** from `tax_repartition_line_id.tax_id` (stored, precomputed)
- `tax_repartition_line_id` points to the specific repartition configuration that generated the tax amount line
- A line with `tax_repartition_line_id` populated = a **tax amount line** (not a base line)
- A line with `tax_ids` populated = a **base line** that carries taxes to be applied

### 4.3 tax_base_amount

**File**: `account/models/account_move_line.py:222-226`

```python
tax_base_amount = fields.Monetary(
    string="Base Amount",
    readonly=True,
    currency_field='company_currency_id',
)
```

Tax base amount in company currency for WHT/tax audit reporting.

---

## 5. Reconciliation Fields

### 5.1 amount_residual and reconciled

**File**: `account/models/account_move_line.py:246-258`

```python
amount_residual = fields.Monetary(
    compute='_compute_amount_residual', store=True,
    currency_field='company_currency_id',
)
amount_residual_currency = fields.Monetary(
    compute='_compute_amount_residual', store=True,
)
reconciled = fields.Boolean(compute='_compute_amount_residual', store=True)
```

The `_compute_amount_residual` method (lines 815–880) queries `account_partial_reconcile` table directly via SQL:

```python
@api.depends('debit', 'credit', 'amount_currency', 'account_id', 'currency_id', 'company_id',
             'matched_debit_ids', 'matched_credit_ids')
def _compute_amount_residual(self):
    ...
    line.amount_residual = comp_curr.round(line.balance - debit_amount + credit_amount)
    line.amount_residual_currency = foreign_curr.round(line.amount_currency - debit_amount_currency + credit_amount_currency)
    line.reconciled = (
        comp_curr.is_zero(line.amount_residual)
        and foreign_curr.is_zero(line.amount_residual_currency)
    )
```

**File**: `account/models/account_move_line.py:813-880`

### 5.2 full_reconcile_id / matched_debit_ids / matched_credit_ids

**File**: `account/models/account_move_line.py:259-277`

```python
full_reconcile_id = fields.Many2one(
    comodel_name='account.full.reconcile',
    string="Matching",
    copy=False,
    index='btree_not_null',
    readonly=True,
)
matched_debit_ids = fields.One2many(
    comodel_name='account.partial.reconcile', inverse_name='credit_move_id',
    string='Matched Debits',
    readonly=True,
)
matched_credit_ids = fields.One2many(
    comodel_name='account.partial.reconcile', inverse_name='debit_move_id',
    string='Matched Credits',
    readonly=True,
)
```

Note the inverse_name logic:
- `matched_debit_ids` (on a credit line) → partials where this line = `credit_move_id`
- `matched_credit_ids` (on a debit line) → partials where this line = `debit_move_id`

### 5.3 matching_number

**File**: `account/models/account_move_line.py:304-310`

```python
matching_number = fields.Char(
    string="Matching #",
    copy=False,
    index='btree',
    help="Matching number for this line, 'P' if it is only partially reconcile, or the name of "
         "the full reconcile if it exists.",
)  # can also start with `I` for imports: see `_reconcile_marked`
```

Constraints on this field: `account/models/account_move_line.py:1593-1609` — validated pattern `^((P?\d+)|(I.+))$`.

---

## 6. account.partial.reconcile Model

**File**: `account/models/account_partial_reconcile.py:10-68`

```python
class AccountPartialReconcile(models.Model):
    _name = 'account.partial.reconcile'
    _description = "Partial Reconcile"

    debit_move_id = fields.Many2one(comodel_name='account.move.line', index=True, required=True)
    credit_move_id = fields.Many2one(comodel_name='account.move.line', index=True, required=True)
    full_reconcile_id = fields.Many2one(comodel_name='account.full.reconcile', ...)
    exchange_move_id = fields.Many2one(comodel_name='account.move', ...)
    
    # Amount fields
    amount = fields.Monetary(currency_field='company_currency_id',
        help="Always positive amount concerned by this matching expressed in the company currency.")
    debit_amount_currency = fields.Monetary(currency_field='debit_currency_id',
        help="Always positive amount concerned by this matching expressed in the debit line foreign currency.")
    credit_amount_currency = fields.Monetary(currency_field='credit_currency_id',
        help="Always positive amount concerned by this matching expressed in the credit line foreign currency.")
```

All three amount fields are **always positive**. The `debit_currency_id` and `credit_currency_id` are stored-related from the respective move lines.

---

## 7. account.full.reconcile Model

**File**: `account/models/account_full_reconcile.py:5-61`

```python
class AccountFullReconcile(models.Model):
    _name = 'account.full.reconcile'
    _description = "Full Reconcile"

    partial_reconcile_ids = fields.One2many('account.partial.reconcile', 'full_reconcile_id', ...)
    reconciled_line_ids = fields.One2many('account.move.line', 'full_reconcile_id', ...)
```

Full reconcile is created via `_reconcile_plan_with_sync()` — specifically at line 2966:

```python
self.env['account.full.reconcile'].create(full_reconcile_values_list)
```

**When created**: when ALL lines in the reconciliation batch report `reconciled = True` (zero residual in both company and foreign currency). `AccountFullReconcile.create()` uses direct SQL to set `full_reconcile_id` on move lines and partials for performance (lines 26-43).

---

## 8. Reconcile Method Chain

**File**: `account/models/account_move_line.py:3142-3144`

```python
def reconcile(self):
    """ Reconcile the current move lines all together. """
    return self._reconcile_plan([self])
```

**`_reconcile_plan()`** (line 2797) → **`_reconcile_plan_with_sync()`** (line 2821):

1. `_optimize_reconciliation_plan()` — validates same account, same company, account reconcilable
2. `_prepare_reconciliation_plan()` → `_prepare_reconciliation_amls()` → `_prepare_reconciliation_single_partial()` — iterates debit/credit pairs, computes partial amounts
3. `self.env['account.partial.reconcile'].create(partials_values_list)` — bulk create (line 2866)
4. Exchange difference moves created if needed (line 2876)
5. Cash basis tax entries if applicable (lines 2898-2902)
6. `self.env['account.full.reconcile'].create(full_reconcile_values_list)` — bulk create (line 2966)
7. `all_amls._reconcile_post_hook()` — fires `_invoice_paid_hook()` for invoices moving to `paid` state

**`remove_move_reconcile()`** (line 3146):

```python
def remove_move_reconcile(self):
    (self.matched_debit_ids + self.matched_credit_ids).unlink()
```

Unlinking partials cascades to unlink full reconcile (via `AccountPartialReconcile.unlink()` which reverses CABA entries).

---

## 9. Price Fields on Invoice Lines

**File**: `account/models/account_move_line.py:398-413`

```python
price_unit = fields.Float(
    compute="_compute_price_unit", store=True, readonly=False, precompute=True,
)
price_subtotal = fields.Monetary(
    compute='_compute_totals', store=True,
    currency_field='currency_id',
)
price_total = fields.Monetary(
    compute='_compute_totals', store=True,
    currency_field='currency_id',
)
```

**Computation** (`_compute_totals`, lines 915-932):

```python
@api.depends('quantity', 'discount', 'price_unit', 'tax_ids', 'currency_id', 'amount_currency')
def _compute_totals(self):
    ...
    base_line = line.move_id._prepare_product_base_line_for_taxes_computation(line)
    AccountTax._add_tax_details_in_base_line(base_line, company)
    AccountTax._round_base_lines_tax_details([base_line], company)
    line.price_subtotal = base_line['tax_details']['total_excluded_currency']
    line.price_total = base_line['tax_details']['total_included_currency']
```

`price_subtotal` = tax-excluded total in invoice currency; `price_total` = tax-included total in invoice currency. Both expressed in `currency_id` (not `company_currency_id`).

---

## 10. Analytic Distribution (v17+ Migration Flag)

### 10.1 Field Definition

**File**: `account/models/account_move_line.py:438-440`

```python
analytic_distribution = fields.Json(
    inverse="_inverse_analytic_distribution",
)  # add the inverse function used to trigger the creation/update of the analytic lines accordingly
```

The field is originally defined in `analytic.mixin` (`analytic/models/analytic_mixin.py:16-18`). The account move line overrides it with an `inverse` function.

**JSON structure**: `{"<analytic_account_id>,<analytic_account_id2>": <percentage_float>, ...}`

Example: `{"123": 60.0, "456,789": 40.0}` — comma-separated account IDs map to percentage.

### 10.2 MIGRATION FLAG: analytic_account_id and analytic_tag_ids REMOVED

Confirmed: **`analytic_account_id`** and **`analytic_tag_ids`** do NOT exist on `account.move.line` in v19.

Search across the entire `account/models/account_move_line.py` file shows zero field declarations for these names. The only occurrences of `analytic_account_id` are as a variable name inside Python loops iterating over the JSON keys (lines 1026, 1032).

**Replacement**: `analytic_distribution` (JSON field) replaces both `analytic_account_id` (single account FK) and `analytic_tag_ids` (M2M tags). The JSON format supports multi-plan distribution with percentage allocation.

### 10.3 Inverse — analytic line synchronisation

**File**: `account/models/account_move_line.py:1441-1458`

When `analytic_distribution` changes on a **posted** line, the inverse method:
1. Unlinks old `account.analytic.line` records
2. Re-creates them via `_create_analytic_lines()`

### 10.4 Validation

**File**: `account/models/account_move_line.py:3188-3219`

`_validate_analytic_distribution()` is called on posting. If a product line requires analytic distribution (per company plan rules) and it's missing/incomplete (< 100%), raises `ValidationError` or `RedirectWarning`.

---

## 11. Display Type — Line Classification

**File**: `account/models/account_move_line.py:333-351`

```python
display_type = fields.Selection(
    selection=[
        ('product', 'Product'),
        ('cogs', 'Cost of Goods Sold'),
        ('tax', 'Tax'),
        ('discount', "Discount"),
        ('rounding', "Rounding"),
        ('payment_term', 'Payment Term'),
        ('line_section', 'Section'),
        ('line_subsection', 'Subsection'),
        ('line_note', 'Note'),
        ('epd', 'Early Payment Discount'),
        ('non_deductible_product_total', 'Non Deductible Products Total'),
        ('non_deductible_product', 'Non Deductible Products'),
        ('non_deductible_tax', 'Non Deductible Tax'),
    ],
    ...
)
```

Lines with `display_type IN ('line_section', 'line_subsection', 'line_note')` are exempt from accounting constraints (no account, zero balance). Tax lines have `display_type = 'tax'`; payment term lines have `display_type = 'payment_term'` and always use AR/AP accounts.

---

## 12. Indexes Defined on the Model

**File**: `account/models/account_move_line.py:503-509`

```python
_partner_id_ref_idx = models.Index("(partner_id, ref)")
_date_name_id_idx = models.Index("(date desc, move_name desc, id)")
_unreconciled_index = models.Index("(account_id, partner_id) WHERE reconciled IS NOT TRUE")
_journal_id_neg_amnt_residual_idx = models.Index("(journal_id) WHERE amount_residual < 0")
_account_id_date_idx = models.Index("(account_id, date)")
```

The partial index `_unreconciled_index` is important for performance of reconciliation lookups.

---

## 13. Storno Accounting

**File**: `account/models/account_move_line.py:85-89` and `716-725`

When `is_storno = True` the sign of `debit`/`credit` is **reversed** — negative debit instead of positive credit. This is controlled by `company_id.account_storno` and applies to refund-type moves.

---

## Summary of Migration-Critical Facts

| Item | v16 and earlier | v19 Status |
|------|----------------|------------|
| `analytic_account_id` | FK field on `account.move.line` | **REMOVED** — does not exist |
| `analytic_tag_ids` | M2M field on `account.move.line` | **REMOVED** — does not exist |
| `analytic_distribution` | Not present (or experimental) | **CANONICAL** — JSON field via `analytic.mixin` |
| `balance` as primary | `debit`/`credit` were direct | `balance` is stored master, `debit`/`credit` computed |
| `move_type` on line | Not present | Non-stored related to `move_id.move_type` |
| `tax_line_id` | Direct Many2one | Related-stored from `tax_repartition_line_id.tax_id` |
| `account.partial.reconcile` | Present | Present — `amount`, `debit_amount_currency`, `credit_amount_currency` all positive |
| `account.full.reconcile` | Present | Present — created when all lines fully matched |
