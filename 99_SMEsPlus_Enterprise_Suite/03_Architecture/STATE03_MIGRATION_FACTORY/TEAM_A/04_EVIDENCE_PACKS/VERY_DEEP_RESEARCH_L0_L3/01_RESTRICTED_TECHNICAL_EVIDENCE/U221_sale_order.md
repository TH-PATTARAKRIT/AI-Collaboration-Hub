# U221 — sale.order: Restricted Technical Evidence
**Unit:** U221  
**Module:** sale / sale_order  
**Source SHA256:** c2e51afe8919f3de53ad6504477a01fbebf4bb58cfd56836aa65d001a1734514  
**Research date:** 2026-10-02  
**Gate:** GREEN

---

## 1. State Machine

### 1.1 SALE_ORDER_STATE constant
**File:** `sale/models/sale_order.py` **Lines:** 26–31

```python
SALE_ORDER_STATE = [
    ('draft', "Quotation"),
    ('sent', "Quotation Sent"),
    ('sale', "Sales Order"),
    ('cancel', "Cancelled"),
]
```

Four states only. No `done` state exists in Community v19. The field declaration:

```python
state = fields.Selection(
    selection=SALE_ORDER_STATE,
    ...
    default='draft')
```
**Line:** 71–77

### 1.2 action_draft()
**Lines:** 1060–1067 — Resets `draft` from `cancel` or `sent`. Clears `signature`, `signed_by`, `signed_on`.

### 1.3 action_quotation_sent()
**Lines:** 1158–1166 — Sets `state='sent'` only from `draft`. Raises `UserError` otherwise.

### 1.4 action_confirm()
**Lines:** 1168–1198 — Primary confirmation entry point.

Key chain:
1. `_confirmation_error_message()` — validates `state in {'draft', 'sent'}` (line 1208)
2. `order_line._validate_analytic_distribution()` — validates analytic before write (line 1182)
3. `write(self._prepare_confirmation_values())` — sets `state='sale'` and `date_order=now()` (line 1184)
4. `self._action_confirm()` — extension hook, **empty in base sale** (line 1192, 1233–1237)
5. Locks order if `sale.group_auto_done_setting` is enabled (line 1193)
6. Sends email if `send_email` context key present (line 1195–1196)

**Critical finding:** `_action_confirm()` is a no-op in the base `sale` module. Stock moves and POs are created by overrides in `sale_stock` and `purchase_stock` respectively — not here.

### 1.5 _prepare_confirmation_values()
**Lines:** 1220–1231

```python
return {
    'state': 'sale',
    'date_order': fields.Datetime.now()
}
```

### 1.6 action_cancel()
**Lines:** 1326–1335 — Raises `UserError` if locked. Cancels draft invoices, writes `state='cancel'`.

### 1.7 DB Constraint: date_order required on confirmed SO
**Lines:** 42–45

```python
_date_order_conditional_required = models.Constraint(
    "CHECK((state = 'sale' AND date_order IS NOT NULL) OR state != 'sale')",
    ...
)
```

---

## 2. invoice_status Field

### 2.1 INVOICE_STATUS constant
**Lines:** 19–24

```python
INVOICE_STATUS = [
    ('upselling', 'Upselling Opportunity'),
    ('invoiced', 'Fully Invoiced'),
    ('to invoice', 'To Invoice'),
    ('no', 'Nothing to Invoice')
]
```

Note: four values. There is **no** `'no_need'` value — the value is `'no'` (not `'no_need'`).

### 2.2 _compute_invoice_status() on SaleOrder
**Lines:** 619–665  
Dependencies: `state`, `order_line.invoice_status`

Logic:
- Non-`sale` orders → `'no'`
- Any line `'to invoice'` (with guard for special-only lines) → `'to invoice'`
- All lines `'invoiced'` → `'invoiced'`
- All lines `'invoiced'` or `'upselling'` → `'upselling'`
- Otherwise → `'no'`

Down-payment lines (`is_downpayment=True`) and display lines (`display_type`) are **excluded** from the aggregation domain (line 633):
```python
lines_domain = [('is_downpayment', '=', False), ('display_type', '=', False)]
```

Uses `_read_group` (line 636–640) for efficient batch computation.

### 2.3 _compute_invoice_status() on SaleOrderLine
**File:** `sale/models/sale_order_line.py` **Lines:** 1086–1115  
Dependencies: `state`, `product_uom_qty`, `qty_delivered`, `qty_to_invoice`, `qty_invoiced`

Logic:
- `state != 'sale'` → `'no'`
- Down-payment with `untaxed_amount_to_invoice == 0` → `'invoiced'`
- `qty_to_invoice != 0` → `'to invoice'`
- `invoice_policy == 'order'` and `qty_delivered > product_uom_qty` → `'upselling'`
- `qty_invoiced >= product_uom_qty` → `'invoiced'`
- Else → `'no'`

---

## 3. commitment_date and expected_date

### 3.1 commitment_date field
**Lines:** 88–92

```python
commitment_date = fields.Datetime(
    string="Delivery Date", copy=False,
    help="This is the delivery date promised to the customer. "
         "If set, the delivery order will be scheduled based on "
         "this date rather than product lead times.")
```

Not required, not computed. Manual entry. No `store=True` dependency chain on state.

### 3.2 date_order field
**Lines:** 93–97

```python
date_order = fields.Datetime(
    string="Order Date",
    required=True, copy=False,
    ...
    default=fields.Datetime.now)
```

Stores creation date for draft/sent; overwritten to `now()` on confirmation (see `_prepare_confirmation_values()`).

### 3.3 expected_date computed field
**Lines:** 302–305

```python
expected_date = fields.Datetime(
    string="Expected Date",
    compute='_compute_expected_date', store=False,  # Note: can not be stored since depends on today()
    help="Delivery date you can promise to the customer, computed from the minimum lead time of the order lines.")
```

**_compute_expected_date()** — Lines 737–757:
- Skips cancelled orders
- Filters `order_line` to `product_id.type == 'consu'`, non-display, non-delivery
- Maps `line._expected_date()` (= `date_order + timedelta(customer_lead)`)
- Takes the minimum via `_select_expected_date()` (line 755–757)

### 3.4 _onchange_commitment_date() warning
**Lines:** 885–895 — Warns if `commitment_date < expected_date`.

### 3.5 _expected_date() on SaleOrderLine
**File:** `sale_order_line.py` **Lines:** 1496–1502

```python
def _expected_date(self):
    ...
    if self.state == 'sale' and self.order_id.date_order:
        order_date = self.order_id.date_order
    else:
        order_date = fields.Datetime.now()
    return order_date + timedelta(days=self.customer_lead or 0.0)
```

---

## 4. qty_delivered_method on SaleOrderLine

### 4.1 Field Declaration
**File:** `sale_order_line.py` **Lines:** 217–229

```python
qty_delivered_method = fields.Selection(
    selection=[
        ('manual', "Manual"),
        ('analytic', "Analytic From Expenses"),
    ],
    ...
    compute='_compute_qty_delivered_method',
    store=True, precompute=True,
    ...)
```

Only two values in base `sale`: `manual` and `analytic`. The `stock_moves` selection value is added by `sale_stock`. The `timesheet` value is added by `sale_timesheet`.

### 4.2 _compute_qty_delivered_method()
**Lines:** 882–896

```python
def _compute_qty_delivered_method(self):
    for line in self:
        if line.is_expense:
            line.qty_delivered_method = 'analytic'
        else:  # service and consu
            line.qty_delivered_method = 'manual'
```

Dependencies: `is_expense`

### 4.3 _compute_qty_delivered()
**Lines:** 898–913  
Calls `_prepare_qty_delivered()` which handles `analytic` method lines by summing `account.analytic.line.unit_amount`.

---

## 5. analytic_distribution on SaleOrderLine

### 5.1 Field Source
`SaleOrderLine` inherits `analytic.mixin` (line 14, `sale_order_line.py`).  
`analytic_distribution` defined in `analytic/models/analytic_mixin.py` **line 16**:

```python
analytic_distribution = fields.Json(
    'Analytic Distribution',
    compute="_compute_analytic_distribution",
    search="_search_analytic_distribution",
    store=True, copy=True, readonly=False,
)
```

**Type: Json field.** Keys are analytic account IDs (comma-separated for multi-plan), values are percentage weights (0–100).

### 5.2 _compute_analytic_distribution() override in SaleOrderLine
**File:** `sale_order_line.py` **Lines:** 1248–1259

```python
@api.depends('order_id.partner_id', 'product_id')
def _compute_analytic_distribution(self):
    for line in self:
        if not line.display_type:
            distribution = line.env['account.analytic.distribution.model']._get_distribution({
                "product_id": line.product_id.id,
                "product_categ_id": line.product_id.categ_id.id,
                "partner_id": line.order_id.partner_id.id,
                "partner_category_id": line.order_id.partner_id.category_id.ids,
                "company_id": line.company_id.id,
            })
            line.analytic_distribution = distribution or line.analytic_distribution
```

Populated from distribution models (automatic rules), **not from a legacy `analytic_account_id` field.**

### 5.3 MIGRATION FLAG: analytic_account_id ABSENT
The field `analytic_account_id` does **not exist** on `sale.order.line` in v19 Community. The sole analytic mechanism is `analytic_distribution` (Json).

### 5.4 _validate_analytic_distribution()
**Lines:** 1580–1586 — Called from `action_confirm()` and `action_quotation_send()`. Calls `_validate_distribution()` with `business_domain='sale_order'`.

### 5.5 analytic_distribution in _get_protected_fields()
**Lines:** 1432–1441 — `analytic_distribution` is a protected field on locked orders (prevents write).

### 5.6 _set_analytic_distribution() propagation to invoice line
**Lines:** 1569–1571

```python
def _set_analytic_distribution(self, inv_line_vals, **optional_values):
    if self.analytic_distribution and not self.display_type:
        inv_line_vals['analytic_distribution'] = self.analytic_distribution
```

Propagates distribution to created invoice lines.

---

## 6. _create_invoices() — SO lines → invoice lines

### 6.1 Method Signature
**Lines:** 1552–1694

```python
def _create_invoices(self, grouped=False, final=False, date=None):
```

### 6.2 Grouping Keys
**Lines:** 1483–1484

```python
def _get_invoice_grouping_keys(self):
    return ['company_id', 'partner_id', 'partner_shipping_id', 'currency_id', 'fiscal_position_id']
```

When `grouped=False` (default), multiple SOs sharing the same five keys are merged into one invoice.

### 6.3 Invoiceable Lines
**_get_invoiceable_lines()** — Lines 1501–1544. Filters by `qty_to_invoice != 0` (or `final=True` for negative qty). Down-payment lines collected separately, placed at end of invoice.

### 6.4 Invoice Line Creation
**Lines:** 1608–1609 — Calls `line._prepare_invoice_lines_vals_list()` for each invoiceable line.

`_prepare_invoice_line()` — Lines 1522–1567: populates `product_id`, `product_uom_id`, `quantity=qty_to_invoice`, `price_unit`, `tax_ids`, `sale_line_ids=[link(self.id)]`.

### 6.5 Negative-total refund conversion
**Lines:** 1683–1686 — After creation, if `final=True` and move total < 0, `action_switch_move_type()` converts to refund.

### 6.6 _create_account_invoices()
**Lines:** 1546–1550 — Creates via sudo (salesperson can invoice without billing rights).

---

## 7. action_confirm() — what triggers

### 7.1 Base module: _action_confirm() is empty
**Lines:** 1233–1237

```python
def _action_confirm(self):
    """ Implementation of additional mechanism of Sales Order confirmation.
        This method should be extended when the confirmation should generated
        other documents. In this method, the SO are in 'sale' state (not yet 'done').
    """
```

Body is empty (docstring only). No stock move creation here.

### 7.2 Stock moves: sale_stock module (NOT present in scope)
Stock move creation would be in `sale_stock/models/sale_order.py` override of `_action_confirm()`. Not part of this base `sale` module analysis.

### 7.3 PO creation: sale_purchase module (NOT present in scope)
Purchase order creation would be in `sale_purchase` module override. Not in base `sale`.

---

## 8. company_id Enforcement (Multi-Company)

### 8.1 company_id field
**Lines:** 61–64 — Required, index, default=current company.

### 8.2 _check_company_auto = True
**Line:** 39 — Enables ORM-level company field validation on related fields.

### 8.3 check_company=True on partner_id
**Line:** 70 — Customer must be accessible from order company.

### 8.4 _check_order_line_company_id constraint
**Lines:** 849–864 — Validates product `company_id` must be accessible from order `company_id` via `_accessible_branches()`.

### 8.5 Sequence namespaced per company
**Lines:** 1012–1013 — `ir.sequence.with_company(company_id).next_by_code('sale.order')`.

### 8.6 FK duplicate detection scoped by company
**Line:** 718–721 — SQL join filters `sale_order.company_id = duplicate_order.company_id`.

---

## 9. qty_to_invoice and Billing Policy

### 9.1 _compute_qty_to_invoice()
**File:** `sale_order_line.py` **Lines:** 1056–1084

```python
if line.product_id.invoice_policy == 'order':
    line.qty_to_invoice = line.product_uom_qty - line.qty_invoiced
else:
    line.qty_to_invoice = line.qty_delivered - line.qty_invoiced
```

- `invoice_policy='order'` → billed on ordered qty
- `invoice_policy='delivery'` (default for storable/consumable) → billed on delivered qty

### 9.2 _force_lines_to_invoice_policy_order()
**Lines:** 1799–1809 — Forces `qty_to_invoice = product_uom_qty - qty_invoiced` for all `sale` state lines regardless of product invoice_policy. Used for automatic full invoicing after online payment.

---

## 10. Summary of Migration Flags

| Flag | Detail |
|------|--------|
| `analytic_account_id` ABSENT | Field does not exist on `sale.order.line` in v19. Use `analytic_distribution` (Json). |
| `invoice_status='no'` (not `'no_need'`) | The "nothing to invoice" value is `'no'`, not `'no_need'` as in some older versions. |
| `state='done'` ABSENT | No `done` state in v19 Community. State machine is draft→sent→sale→cancel. |
| `_action_confirm()` is a hook | Base implementation is empty; downstream modules extend it. |
| `commitment_date` renamed | In v17+ it remains `commitment_date` but the UI label is "Delivery Date". No rename from v16→v19. |
| `date_order` overwritten on confirm | On confirmation, `date_order` is **replaced** with `now()` (not preserved as creation date). |
