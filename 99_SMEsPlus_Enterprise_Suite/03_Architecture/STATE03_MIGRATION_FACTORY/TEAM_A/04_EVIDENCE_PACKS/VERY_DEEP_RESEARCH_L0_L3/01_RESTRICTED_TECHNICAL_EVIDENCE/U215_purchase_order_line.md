# U215 — purchase.order.line: Bill Control, qty_received, qty_invoiced, date_planned, analytic_distribution

**Research Unit**: U215  
**Module**: purchase (purchase_order_line.py) + purchase_stock extension  
**Source SHA**: 4bba13d6759802a57b771e1d52c094ceb7e114691949d205b491efc8cf343f2f  
**Source Path**: `addons/purchase/models/purchase_order_line.py`  
**Gate**: GREEN  
**Date**: 2026-10-02

---

## 1. Model Declaration

**File**: `purchase/models/purchase_order_line.py` line 13–17

```python
class PurchaseOrderLine(models.Model):
    _name = 'purchase.order.line'
    _inherit = ['analytic.mixin']
    _description = 'Purchase Order Line'
    _order = 'order_id, sequence, id'
```

`analytic.mixin` (from `analytic/models/analytic_mixin.py` line 12) provides the `analytic_distribution` JSON field (line 16–21). **No `analytic_account_id` field exists on this model in v19.**

---

## 2. Core Fields (with exact pointers)

### 2.1 product_id
- **Line 44**: `product_id = fields.Many2one('product.product', string='Product', domain=[('purchase_ok', '=', True)], change_default=True, index='btree_not_null', ondelete='restrict')`
- Domain filters to purchasable products only.

### 2.2 product_qty
- **Line 23**: `product_qty = fields.Float(string='Quantity', digits='Product Unit', required=True)`
- Raw ordered quantity in the PO line's UoM.

### 2.3 price_unit
- **Lines 46–48**: `price_unit = fields.Float(string='Unit Price', required=True, min_display_digits='Product Price', aggregator='avg', compute="_compute_price_unit_and_date_planned_and_name", readonly=False, store=True)`
- Computed from selected seller price via `_compute_price_unit_and_date_planned_and_name()`.

### 2.4 price_subtotal
- **Line 54**: `price_subtotal = fields.Monetary(compute='_compute_amount', string='Subtotal', store=True)`
- Computed at lines 123–133: uses `AccountTax._add_tax_details_in_base_line()` → `base_line['tax_details']['total_excluded_currency']`.

### 2.5 qty_invoiced
- **Line 66**: `qty_invoiced = fields.Float(compute='_compute_qty_invoiced', string="Billed Qty", digits='Product Unit', store=True)`

### 2.6 qty_received
- **Line 72**: `qty_received = fields.Float("Received Qty", compute='_compute_qty_received', inverse='_inverse_qty_received', compute_sudo=True, store=True, digits='Product Unit')`

### 2.7 qty_to_invoice
- **Lines 74–75**: `qty_to_invoice = fields.Float(compute='_compute_qty_invoiced', string='To Invoice Quantity', store=True, readonly=True, digits='Product Unit')`

### 2.8 date_planned
- **Lines 25–28**: `date_planned = fields.Datetime(string='Expected Arrival', index=True, compute="_compute_price_unit_and_date_planned_and_name", readonly=False, store=True, help="Delivery date expected from vendor...")`

### 2.9 tax_ids
- **Lines 34–41**: `tax_ids = fields.Many2many(comodel_name='account.tax', relation='account_tax_purchase_order_line_rel', column1='purchase_order_line_id', column2='account_tax_id', string='Taxes', context={'active_test': False, 'hide_original_tax_ids': True})`

### 2.10 analytic_distribution
- Inherited from `analytic.mixin` (`analytic/models/analytic_mixin.py` line 16).
- `fields.Json('Analytic Distribution', compute="_compute_analytic_distribution", store=True, copy=True, readonly=False)`
- Overriding `_compute_analytic_distribution()` at lines 368–379 in purchase_order_line.py queries `account.analytic.distribution.model` using product, product category, partner, and company.

### 2.11 invoice_lines
- **Line 63**: `invoice_lines = fields.One2many('account.move.line', 'purchase_line_id', string="Bill Lines", readonly=True, copy=False)`

---

## 3. qty_received Computation

### Base module (purchase only — consu/service products)

**Lines 225–231** (`_compute_qty_received_method`):
```python
if line.product_id and line.product_id.type in ['consu', 'service']:
    line.qty_received_method = 'manual'
else:
    line.qty_received_method = False
```

**Lines 233–238** (`_compute_qty_received`):
```python
def _compute_qty_received(self):
    received_qties = self._prepare_qty_received()
    for line in self:
        if not line.qty_received or line in received_qties:
            line.qty_received = received_qties[line]
```

**Lines 251–258** (`_prepare_qty_received`):
```python
def _prepare_qty_received(self):
    received_qties = defaultdict(float)
    for line in self:
        if line.qty_received_method == 'manual':
            received_qties[line] = line.qty_received_manual or 0.0
        else:
            received_qties[line] = 0.0
    return received_qties
```

**Base module result**: For `service` products, `qty_received_method = 'manual'` and qty comes from `qty_received_manual`. For storable products (`consu`), qty is 0 in base — stock moves override this.

### purchase_stock extension (storable products)

**File**: `purchase_stock/models/purchase_order_line.py` line 37–41:
```python
def _compute_qty_received_method(self):
    super(PurchaseOrderLine, self)._compute_qty_received_method()
    for line in self.filtered(lambda l: not l.display_type):
        if line.product_id.type == 'consu':
            line.qty_received_method = 'stock_moves'
```

**Lines 51–79** (`_prepare_qty_received` override):
For `stock_moves` method, iterates `line._get_po_line_moves()` (filtered `stock.move` records in `done` state). Adds `move.product_uom._compute_quantity(move.quantity, line.product_uom_id, rounding_method='HALF-UP')` to total. Handles purchase returns (`to_refund`) by subtracting. Dependency declared at line 51: `@api.depends('move_ids.state', 'move_ids.product_uom', 'move_ids.quantity')`.

---

## 4. qty_invoiced Computation

**Lines 171–184** (`_compute_qty_invoiced`):
```python
@api.depends('invoice_lines.move_id.state', 'invoice_lines.quantity', 'qty_received', 'product_uom_qty', 'order_id.state')
def _compute_qty_invoiced(self):
    invoiced_quantities = self._prepare_qty_invoiced()
    for line in self:
        line.qty_invoiced = invoiced_quantities[line]
        # compute qty_to_invoice
        if line.order_id.state == 'purchase':
            if line.product_id.purchase_method == 'purchase':
                line.qty_to_invoice = line.product_qty - line.qty_invoiced
            else:
                line.qty_to_invoice = line.qty_received - line.qty_invoiced
        else:
            line.qty_to_invoice = 0
```

**Lines 197–207** (`_prepare_qty_invoiced`):
- Iterates `line.invoice_lines` (account.move.line records with `purchase_line_id = line`).
- For `in_invoice` moves (vendor bills): **adds** `inv_line.product_uom_id._compute_quantity(inv_line.quantity, line.product_uom_id)`.
- For `in_refund` moves (vendor credit notes): **subtracts**.
- Excludes cancelled moves (unless `payment_state == 'invoicing_legacy'`).

---

## 5. Bill Control: purchase_method

**File**: `purchase/models/product.py` lines 14–29:
```python
purchase_method = fields.Selection([
    ('purchase', 'On ordered quantities'),
    ('receive', 'On received quantities'),
], string="Control Policy", compute='_compute_purchase_method', precompute=True, store=True, readonly=False, ...)

@api.depends('type')
def _compute_purchase_method(self):
    default_purchase_method = self.env['product.template'].default_get(['purchase_method']).get('purchase_method', 'receive')
    for product in self:
        if product.type == 'service':
            product.purchase_method = 'purchase'
        else:
            product.purchase_method = default_purchase_method
```

**Effect on qty_to_invoice** (purchase_order_line.py lines 178–184):
- `purchase_method == 'purchase'` → `qty_to_invoice = product_qty - qty_invoiced` (based on ordered quantity)
- `purchase_method == 'receive'` (default for non-service) → `qty_to_invoice = qty_received - qty_invoiced` (based on received quantity)
- When `order_id.state != 'purchase'` → `qty_to_invoice = 0` always

---

## 6. invoice_status on purchase.order

**File**: `purchase/models/purchase_order.py` lines 46–68:
```python
@api.depends('state', 'order_line.qty_to_invoice')
def _get_invoiced(self):
    for order in self:
        if order.state != 'purchase':
            order.invoice_status = 'no'
            continue
        if any(not float_is_zero(line.qty_to_invoice, ...) for line in order.order_line.filtered(...)):
            order.invoice_status = 'to invoice'
        elif all(float_is_zero(line.qty_to_invoice, ...) ...) and order.invoice_ids:
            order.invoice_status = 'invoiced'
        else:
            order.invoice_status = 'no'
```

**Field** (line 127–131): `invoice_status = fields.Selection([('no','Nothing to Bill'),('to invoice','Waiting Bills'),('invoiced','Fully Billed')], ...)`

---

## 7. date_planned Computation

**Lines 350–366** (`_get_date_planned`):
```python
@api.model
def _get_date_planned(self, seller, po=False):
    date_order = po.date_order if po else self.order_id.date_order
    if date_order:
        return date_order + relativedelta(days=seller.delay if seller else 0)
    else:
        return datetime.today() + relativedelta(days=seller.delay if seller else 0)
```

`seller.delay` is the `product.supplierinfo.delay` field (delivery delay in days). Called from `_compute_price_unit_and_date_planned_and_name()` at line 427:
```python
line.date_planned = line._get_date_planned(line.selected_seller_id).strftime(DEFAULT_SERVER_DATETIME_FORMAT)
```

---

## 8. _prepare_account_move_line()

**Lines 628–647**:
```python
def _prepare_account_move_line(self, move=False):
    self.ensure_one()
    aml_currency = move and move.currency_id or self.currency_id
    date = move and move.date or fields.Date.today()
    res = {
        'display_type': self.display_type or 'product',
        'name': ...,
        'product_id': self.product_id.id,
        'product_uom_id': self.product_uom_id.id,
        'quantity': -self.qty_to_invoice if move and move.move_type == 'in_refund' else self.qty_to_invoice,
        'discount': self.discount,
        'price_unit': self.currency_id._convert(self.price_unit, aml_currency, self.company_id, date, round=False),
        'tax_ids': [(6, 0, self.tax_ids.ids)],
        'purchase_line_id': self.id,
        'is_downpayment': self.is_downpayment,
    }
    if self.is_downpayment and self.invoice_lines:
        res['account_id'] = self.invoice_lines.account_id[:1].id
    return res
```

Note: `qty_to_invoice` is used as the quantity on the bill line. For refunds, quantity is negated.

**purchase_stock override** (purchase_stock/models/purchase_order_line.py lines 316–330): adds `balance` key using tax-excluded amount converted to company currency.

---

## 9. analytic_distribution on purchase line

**Lines 368–379** (purchase_order_line.py):
```python
@api.depends('product_id', 'order_id.partner_id')
def _compute_analytic_distribution(self):
    for line in self:
        if not line.display_type:
            distribution = self.env['account.analytic.distribution.model']._get_distribution({
                "product_id": line.product_id.id,
                "product_categ_id": line.product_id.categ_id.id,
                "partner_id": line.order_id.partner_id.id,
                "partner_category_id": line.order_id.partner_id.category_id.ids,
                "company_id": line.company_id.id,
            })
            line.analytic_distribution = distribution or line.analytic_distribution
```

**Format**: JSON dict mapping analytic account ID(s) (as string keys, comma-separated for multi-plan) to percentage values. Example: `{"1": 60.0, "2": 40.0}` or `{"1,3": 100.0}` for multi-plan.

**Bill line propagation** (purchase/models/account_invoice.py lines 549–553):
```python
def _related_analytic_distribution(self):
    vals = super()._related_analytic_distribution()
    if self.purchase_line_id:
        vals |= self.purchase_line_id.analytic_distribution or {}
    return vals
```

---

## 10. taxes_id / tax_ids Resolution

**Lines 153–159** (`_compute_tax_id`):
```python
def _compute_tax_id(self):
    for line in self:
        line = line.with_company(line.company_id)
        fpos = line.order_id.fiscal_position_id or line.order_id.fiscal_position_id._get_fiscal_position(line.order_id.partner_id)
        taxes = line.product_id.supplier_taxes_id._filter_taxes_by_company(line.company_id)
        line.tax_ids = fpos.map_tax(taxes)
```

Source: `product.product.supplier_taxes_id` (Many2many `account.tax`), filtered by company, then mapped through fiscal position. Field renamed from `taxes_id` in older versions to `tax_ids` in v19 (field declaration line 34).

---

## 11. MIGRATION FLAGS

### FLAG-001: analytic_account_id ABSENT
- v16/v17 had `analytic_account_id = fields.Many2one('account.analytic.account', ...)` on purchase.order.line.
- In v19: **ABSENT**. Replaced by `analytic_distribution` (JSON) from `analytic.mixin`. Migration scripts must map `analytic_account_id → analytic_distribution` (e.g., `{"<old_id>": 100.0}`).

### FLAG-002: product_packaging_id and product_packaging_qty NOT in base purchase module
- i18n files reference `field_purchase_order_line__product_packaging_id` and `field_purchase_order_line__product_packaging_qty` (purchase/i18n/en_AU.po lines 1695, 1700) but these fields are NOT defined in the Python source of `purchase/models/purchase_order_line.py` in v19.
- No Python file in the community source defines these fields on `purchase.order.line`. This is a confirmed absence in v19 community.

### FLAG-003: taxes_id renamed to tax_ids
- v14/v15 used `taxes_id`. v19 uses `tax_ids` (line 34, relation table `account_tax_purchase_order_line_rel`).

### FLAG-004: qty_to_invoice computed from purchase_method
- `purchase_method == 'purchase'` (on_order): `qty_to_invoice = product_qty - qty_invoiced` — always bills ordered qty regardless of receipt.
- `purchase_method == 'receive'` (on_delivery): `qty_to_invoice = qty_received - qty_invoiced` — bills only what was received.
- State guard: `qty_to_invoice = 0` when `order_id.state != 'purchase'`.

### FLAG-005: qty_received_method selection extended by purchase_stock
- Base: `[('manual', 'Manual')]`
- purchase_stock adds: `selection_add=[('stock_moves', 'Stock Moves')]`
- For `consu` products with purchase_stock: `qty_received_method = 'stock_moves'` (done stock moves sum).
- For `service` products: `qty_received_method = 'manual'` (always, even with purchase_stock installed).

---

## 12. Constraint Definitions

**Lines 105–112**:
```python
_accountable_required_fields = models.Constraint(
    'CHECK(display_type IS NOT NULL OR is_downpayment OR (product_id IS NOT NULL AND product_uom_id IS NOT NULL AND date_planned IS NOT NULL))',
    'Missing required fields on accountable purchase order line.',
)
_non_accountable_null_fields = models.Constraint(
    'CHECK(display_type IS NULL OR (product_id IS NULL AND price_unit = 0 AND product_uom_qty = 0 AND product_uom_id IS NULL AND date_planned is NULL))',
    'Forbidden values on non-accountable purchase order line',
)
```

`date_planned` is **required** for non-section/subsection/note lines (accountable lines).
