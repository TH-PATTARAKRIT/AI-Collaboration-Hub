# U224 — account.tax: Tax Computation Engine

**Unit**: U224  
**Module**: account_tax  
**Source file**: odoo/addons/account/models/account_tax.py  
**SHA fingerprint** (sha256 prefix): 1d149b925dfc  
**Lines**: 5382  
**Date researched**: 2026-10-02  
**Researcher**: STATE03 VDR Worker (Claude Sonnet 4.6)

---

## 1. Model Structure: AccountTax (line 71)

### 1.1 amount_type field (line 84–95)

```python
amount_type = fields.Selection(
    default='percent',
    selection=[
        ('group', 'Group of Taxes'),
        ('fixed', 'Fixed'),
        ('percent', 'Percentage'),
        ('division', 'Percentage Tax Included'),
    ],
)
```

**v19 NOTE**: `'code'` (Python-formula tax) is NOT present in the selection list. It is still referenced in `_can_be_discounted` at line 3159 but cannot be created via UI. This is a **migration flag**: any existing code-type taxes must be migrated.

### 1.2 price_include (lines 137–140, 322–329)

`price_include` is a **computed field** in v19, not a stored Boolean:

```python
price_include = fields.Boolean(
    compute='_compute_price_include',
    search='_search_price_include',
)
```

Computed by `_compute_price_include` (line 322–329):
```python
def _compute_price_include(self):
    for tax in self:
        tax.price_include = (
            tax.price_include_override == 'tax_included'
            or (tax.company_price_include == 'tax_included'
                and not tax.price_include_override)
        )
```

**v19 MIGRATION FLAG**: In prior versions `price_include` was a stored Boolean. In v19 it is derived from:
- `price_include_override` (per-tax override, selection: `tax_included`/`tax_excluded`)
- `company_price_include` (company-wide default via `company_id.account_price_include`)

### 1.3 price_include_override (lines 142–147)

**NEW in v19**:
```python
price_include_override = fields.Selection(
    selection=[('tax_included', 'Tax Included'), ('tax_excluded', 'Tax Excluded')],
    string='Included in Price',
)
```
Overrides the company default. If not set, company default applies.

### 1.4 include_base_amount (lines 148–149)

```python
include_base_amount = fields.Boolean(
    string='Affect Base of Subsequent Taxes',
    default=False,
)
```
When True, this tax's computed amount is added to the base for all subsequent taxes that have `is_base_affected=True`.

### 1.5 is_base_affected (lines 150–154)

```python
is_base_affected = fields.Boolean(
    string="Base Affected by Previous Taxes",
    default=True,
)
```
When True, this tax's base can be increased by preceding taxes that have `include_base_amount=True`.

### 1.6 tax_group_id (lines 156–161)

```python
tax_group_id = fields.Many2one(
    comodel_name='account.tax.group',
    compute='_compute_tax_group_id', readonly=False, store=True,
    required=True, precompute=True,
    domain="[('country_id', 'in', (country_id, False))]"
)
```

### 1.7 invoice_repartition_line_ids / refund_repartition_line_ids (lines 175–196)

```python
invoice_repartition_line_ids = fields.One2many(
    comodel_name="account.tax.repartition.line",
    compute='_compute_invoice_repartition_line_ids', store=True, readonly=False,
    inverse_name="tax_id",
    domain=[('document_type', '=', 'invoice')],
)
refund_repartition_line_ids = fields.One2many(
    comodel_name="account.tax.repartition.line",
    compute='_compute_refund_repartition_line_ids', store=True, readonly=False,
    inverse_name="tax_id",
    domain=[('document_type', '=', 'refund')],
)
repartition_line_ids = fields.One2many(
    comodel_name='account.tax.repartition.line',
    inverse_name="tax_id",
    copy=True,
)
```

Default creation in `_compute_invoice_repartition_line_ids` (line 488–494):
```python
tax.invoice_repartition_line_ids = [
    Command.create({'document_type': 'invoice', 'repartition_type': 'base', 'tag_ids': []}),
    Command.create({'document_type': 'invoice', 'repartition_type': 'tax', 'tag_ids': []}),
]
```

### 1.8 has_negative_factor (lines 214, 505–509)

```python
has_negative_factor = fields.Boolean(compute='_compute_has_negative_factor')

def _compute_has_negative_factor(self):
    for tax in self:
        tax_reps = tax.invoice_repartition_line_ids.filtered(
            lambda x: x.repartition_type == 'tax'
        )
        tax.has_negative_factor = bool(
            tax_reps.filtered(lambda tax_rep: tax_rep.factor < 0.0)
        )
```

**Purpose**: Detects reverse-charge taxes that have a repartition line with `factor < 0`. Used throughout computation to create a paired "is_reverse_charge" entry.

### 1.9 Validation: factor sum constraints (lines 588–594)

```python
total_pos_factor = sum(tax_reps.filtered(lambda r: r.factor > 0.0).mapped('factor'))
if float_compare(total_pos_factor, 1.0, precision_digits=2):
    raise ValidationError(...)
total_neg_factor = sum(tax_reps.filtered(lambda r: r.factor < 0.0).mapped('factor'))
if total_neg_factor and float_compare(total_neg_factor, -1.0, precision_digits=2):
    raise ValidationError(...)
```

Positive factors must sum to exactly 100% (+1.0), negative factors (if any) must sum to exactly -100%.

---

## 2. Tax Computation Engine

### 2.1 _flatten_taxes_and_sort_them (lines 895–921)

```python
def _flatten_taxes_and_sort_them(self):
    def sort_key(tax):
        return tax.sequence, tax.id or None
    group_per_tax = {}
    sorted_taxes = self.env['account.tax']
    for tax in self.sorted(key=sort_key):
        if tax.amount_type == 'group':
            children = tax.children_tax_ids.sorted(key=sort_key)
            sorted_taxes |= children
            for child in children:
                group_per_tax[child.id] = tax
        else:
            sorted_taxes |= tax
    return sorted_taxes, group_per_tax
```

Expands group taxes to children. Group sequence used for children ordering (e.g. `[G, B([A, D, F]), E, C]` → `[A, D, F, C, E, G]`).

### 2.2 _batch_for_taxes_computation (lines 923–974)

Groups adjacent taxes into batches. Taxes belong to the same batch if:
- Same `amount_type`
- Same `price_include` (unless `special_mode` is set)
- Same `include_base_amount`
- Not separated by a tax that has `include_base_amount=True` and the current is `is_base_affected`

Iteration is in **REVERSE** order to build batches.

### 2.3 _propagate_extra_taxes_base (lines 976–1080)

Handles cross-tax base propagation. Key scenarios:

**price_include=True, special_mode=False or 'total_included'** (line 1020–1029):
- If `include_base_amount`: propagate negative to `other_tax` after (skip if `!is_base_affected`)
- Otherwise: propagate negative to ALL taxes after
- Propagate negative to ALL taxes before

**price_include=True, special_mode='total_excluded'** (line 1044–1048):
- If `include_base_amount`: add positive to taxes after that have `is_base_affected`

**price_include=False, special_mode=False or 'total_excluded'** (line 1052–1057):
- If `include_base_amount`: add positive to taxes after that have `is_base_affected`

**price_include=False, special_mode='total_included'** (line 1075–1080):
- If `not include_base_amount`: propagate negative to ALL after
- Propagate negative to ALL taxes before

### 2.4 Tax amount computation methods

#### _eval_tax_amount_fixed_amount (lines 1082–1095)
```python
if self.amount_type == 'fixed':
    sign = -1 if evaluation_context['price_unit'] < 0.0 else 1
    return sign * evaluation_context['quantity'] * self.amount
```

#### _eval_tax_amount_price_included (lines 1097–1115)
For **percent** (price-included):
```python
total_percentage = sum(tax.amount for tax in batch) / 100.0
to_price_excluded_factor = 1 / (1 + total_percentage) if total_percentage != -1 else 0.0
return raw_base * to_price_excluded_factor * self.amount / 100.0
```
For **division** (price-included):
```python
return raw_base * self.amount / 100.0
```

#### _eval_tax_amount_price_excluded (lines 1117–1135)
For **percent** (price-excluded):
```python
return raw_base * self.amount / 100.0
```
For **division** (price-excluded):
```python
total_percentage = sum(tax.amount for tax in batch) / 100.0
incl_base_multiplicator = 1.0 if total_percentage == 1.0 else 1 - total_percentage
return raw_base * self.amount / 100.0 / incl_base_multiplicator
```

### 2.5 _get_tax_details — Main Computation (lines 1137–1335)

**Parameters**: `price_unit`, `quantity`, `precision_rounding`, `rounding_method`, `product`, `product_uom`, `special_mode`, `filter_tax_function`

**Computation order** (lines 1248–1267):
1. **Pass 1** (reverse): fixed taxes (`_eval_tax_amount_fixed_amount`)
2. **Pass 2** (reverse): price-included taxes (`_eval_tax_amount_price_included`)
3. **Pass 3** (forward): price-excluded taxes (`_eval_tax_amount_price_excluded`)

**Base computation** (lines 1278–1302):
```python
base = raw_base + tax_data['extra_base_for_base']
if tax_data['price_include'] and special_mode in (False, 'total_included'):
    base -= total_tax_amount
tax_data['base'] = base
```

**has_negative_factor handling** (lines 1184–1186):
```python
if tax.has_negative_factor:
    reverse_charge_taxes_data[tax.id]['tax_amount'] = -taxes_data[tax.id]['tax_amount']
```
A parallel `reverse_charge_taxes_data` entry is created with negated amount.

**Returns**:
```python
{
    'total_excluded': float,
    'total_included': float,
    'taxes_data': [
        {
            'tax': record,
            'taxes': recordset,    # subsequent taxes (from include_base_amount)
            'group': recordset,
            'batch': recordset,
            'tax_amount': float,
            'price_include': bool,
            'base_amount': float,
            'is_reverse_charge': bool,
        }
    ]
}
```

**special_mode values** (lines 1160–1168):
- `False`: normal mode
- `'total_excluded'`: input treated as untaxed base (price-included taxes extracted as if given tax-exclusive)
- `'total_included'`: input is total-with-tax (price-excluded taxes treated as price-included)

### 2.6 prepare_tax_extra_data — has_negative_factor overrides price_include (lines 1201–1216)

```python
if tax.has_negative_factor:
    price_include = False
elif special_mode == 'total_included':
    price_include = True
elif special_mode == 'total_excluded':
    price_include = False
else:
    price_include = tax.price_include
```

**Key**: Reverse-charge taxes (`has_negative_factor=True`) are ALWAYS treated as price-excluded, regardless of `price_include` setting or `special_mode`.

---

## 3. compute_all (lines 4975–5091)

The legacy API wrapper. Delegates to `_get_tax_details` + `_add_accounting_data_to_base_line_tax_details`.

```python
def compute_all(self, price_unit, currency=None, quantity=1.0, product=None,
                partner=None, is_refund=False, handle_price_include=True,
                include_caba_tags=False, rounding_method=None):
```

**special_mode mapping** (lines 5029–5034):
```python
if 'force_price_include' in self.env.context:
    special_mode = 'total_included' if self.env.context['force_price_include'] else 'total_excluded'
elif not handle_price_include:
    special_mode = 'total_excluded'
else:
    special_mode = False
```

Uses `compute_all_use_raw_base_lines=True` context to get unrounded amounts (line 5047–5048).

Returns (line 5085–5091):
```python
{
    'base_tags': list[int],
    'taxes': [{
        'id', 'name', 'amount', 'base', 'sequence', 'account_id',
        'analytic', 'use_in_tax_closing', 'is_reverse_charge',
        'price_include', 'tax_exigibility', 'tax_repartition_line_id',
        'group', 'tag_ids', 'tax_ids'
    }],
    'total_excluded': float,
    'total_included': float,
    'total_void': float,
}
```

`total_void` accumulates amounts for repartition lines without an `account_id` (line 5078–5079).

---

## 4. AccountTaxRepartitionLine (lines 5314–5382)

```python
class AccountTaxRepartitionLine(models.Model):
    _name = 'account.tax.repartition.line'
    _order = 'document_type, repartition_type, sequence, id'
```

### Fields (lines 5321–5344)

| Field | Type | Details |
|-------|------|---------|
| `factor_percent` | Float | default=100, digits=(16,12), % factor |
| `factor` | Float (computed) | `factor_percent / 100.0` |
| `repartition_type` | Selection | `('base', 'Base')` or `('tax', 'of tax')` |
| `document_type` | Selection | `('invoice', 'Invoice')` or `('refund', 'Refund')` |
| `account_id` | Many2one | Account for tax posting |
| `tag_ids` | Many2many | `account.account.tag` with `applicability='taxes'` |
| `tax_id` | Many2one | Parent tax (cascade delete) |
| `sequence` | Integer | Ordering within document_type |
| `use_in_tax_closing` | Boolean (computed) | `repartition_type=='tax' and account_id and account not in (income, expense)` |

**v19 MIGRATION FLAG**: `tag_ids` (tax grids) live on repartition lines, NOT on the tax record itself. Any migration code that read tags from the tax directly must be updated to read from repartition lines.

### _get_aml_target_tax_account (lines 5373–5382)

```python
def _get_aml_target_tax_account(self, force_caba_exigibility=False):
    if not force_caba_exigibility and self.tax_id.tax_exigibility == 'on_payment' \
            and not self.env.context.get('caba_no_transition_account'):
        return self.tax_id.cash_basis_transition_account_id
    else:
        return self.account_id
```

For cash-basis taxes (`tax_exigibility='on_payment'`), the transition account is used instead of the repartition account until payment reconciliation.

---

## 5. Repartition Line Usage in Accounting (_add_accounting_data_to_base_line_tax_details, lines 2368–2502)

Selection of repartition lines based on document type (lines 2393–2396):
```python
if is_refund:
    repartition_lines_field = 'refund_repartition_line_ids'
else:
    repartition_lines_field = 'invoice_repartition_line_ids'
```

For reverse-charge (is_reverse_charge), use negative-factor lines (line 2416–2421):
```python
if tax_data['is_reverse_charge']:
    tax_reps = tax[repartition_lines_field].filtered(
        lambda x: x.repartition_type == 'tax' and x.factor < 0.0
    )
    tax_rep_sign = -1.0
else:
    tax_reps = tax[repartition_lines_field].filtered(
        lambda x: x.repartition_type == 'tax' and x.factor >= 0.0
    )
    tax_rep_sign = 1.0
```

Amount per repartition line (lines 2434–2438):
```python
tax_rep_data = {
    'tax_amount_currency': currency.round(tax_amount_currency * tax_rep.factor * tax_rep_sign),
    'tax_amount': company_currency.round(tax_data['tax_amount'] * tax_rep.factor * tax_rep_sign),
    'account': tax_rep._get_aml_target_tax_account(...) or base_line['account_id'],
}
```

Base-line tags from base-repartition lines (line 2413):
```python
base_line['tax_tag_ids'] |= tax[repartition_lines_field].filtered(
    lambda x: x.repartition_type == 'base'
).tag_ids
```

---

## 6. _prepare_tax_lines (lines 3051–3144)

Converts tax_details into journal entry diff:
- Uses `tax_rep_data['grouping_key']` as the key for aggregating
- `sign * tax_data['base_amount']` → `tax_base_amount` on the tax line
- `sign * tax_rep_data['tax_amount_currency']` → `amount_currency`
- Returns `{tax_lines_to_add, tax_lines_to_delete, tax_lines_to_update, base_lines_to_update}`

---

## 7. Thai WHT Interaction

Thai WHT taxes work via negative `factor_percent` on a repartition line. A typical reverse-charge structure:

- Invoice repartition: base +100%, tax +100%, tax −100%
- Since `has_negative_factor=True`, the engine creates a paired reverse-charge entry
- The negative factor line creates a negative tax amount on a separate account (WHT payable)
- The positive factor line creates the normal tax entry

**Key**: The `has_negative_factor` detection at line 214 enables this via the parallel `reverse_charge_taxes_data` path in `_get_tax_details`. The `_add_accounting_data_to_base_line_tax_details` at line 2416 then splits positive-factor and negative-factor repartition lines into separate accounting entries.

---

## 8. amount_type='code' Status

`'code'` is NOT in the `amount_type` selection (line 84–85). However:
- Line 3159: `return self.amount_type not in ('fixed', 'code')` still references it in `_can_be_discounted`
- This means the type was once supported but removed from UI in v19
- **MIGRATION FLAG**: Existing code-type taxes (if any exist in source system) cannot be mapped 1:1 to v19 and must be re-implemented using Python expression in description or workarounds

---

## 9. Rounding Methods

Two methods supported (used in `_get_tax_details` and `_add_tax_details_in_base_line`):
- `round_per_line`: round each line independently using `precision_rounding`
- `round_globally`: aggregate raw amounts across all lines, then round total once with smart delta distribution

Company default: `company.tax_calculation_rounding_method` (line 1762).

---

## 10. Key Method Call Chain

```
compute_all()
  └─ _prepare_base_line_for_taxes_computation()
  └─ _add_tax_details_in_base_line()
       └─ _get_tax_details()
            └─ _batch_for_taxes_computation()
                 └─ _flatten_taxes_and_sort_them()
            └─ Pass 1: fixed taxes (reversed)
            └─ Pass 2: price-included taxes (reversed)
            └─ Pass 3: price-excluded taxes (forward)
            └─ _propagate_extra_taxes_base()
  └─ _add_accounting_data_to_base_line_tax_details()
       └─ _get_aml_target_tax_account()
```
