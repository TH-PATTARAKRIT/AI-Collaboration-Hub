# U225 — purchase.order: State Machine, Receipt Status, Invoice Status, Bill IDs, Approval Flow

**Unit**: U225  
**Module**: purchase (purchase_order.py, purchase_order_line.py, purchase_stock extension)  
**Source SHA-256**: eace3e4e961951e7caaa1ab5c0834d73365b40b606c0d8d4205ebf81f451a030  
**Source file**: `odoo/addons/purchase/models/purchase_order.py` (1417 lines)  
**Supplementary**: `odoo/addons/purchase/models/purchase_order_line.py`, `odoo/addons/purchase_stock/models/purchase_order.py`, `odoo/addons/purchase/models/account_invoice.py`, `odoo/addons/purchase/models/res_company.py`  
**Research date**: 2026-10-02  
**Gate**: GREEN

---

## 1. State Machine

### 1.1 State Field Definition

**File**: `purchase/models/purchase_order.py`  
**Lines**: 105–111

```python
state = fields.Selection([
    ('draft', 'RFQ'),
    ('sent', 'RFQ Sent'),
    ('to approve', 'To Approve'),
    ('purchase', 'Purchase Order'),
    ('cancel', 'Cancelled')
], string='Status', readonly=True, index=True, copy=False, default='draft', tracking=True)
```

Five valid states. No 'done' state on the purchase.order model itself — the model never transitions to 'done' in v19 Community base purchase module. State is tracked for chatter.

### 1.2 State Transitions

| From | To | Method | File:Line |
|------|----|--------|-----------|
| draft | sent | `message_post()` with context `mark_rfq_as_sent=True` or `print_quotation()` | purchase_order.py:480-482, 611-613 |
| draft/sent | to approve | `button_confirm()` when `_approval_allowed()` returns False | purchase_order.py:625-639 |
| draft/sent | purchase | `button_confirm()` → `button_approve()` when `_approval_allowed()` returns True | purchase_order.py:635-636, 615-619 |
| to approve | purchase | `button_approve()` | purchase_order.py:615-619 |
| purchase/draft/sent/to approve | cancel | `button_cancel()` | purchase_order.py:641-649 |
| cancel | draft | `button_draft()` | purchase_order.py:621-623 |

**Note**: The `locked` field (boolean) prevents edit but is NOT a state value. When `lock_confirmed_po == 'lock'`, PO is locked on approval at line 618.

### 1.3 `button_confirm()` Flow

**File**: `purchase/models/purchase_order.py`  
**Lines**: 625–639

```python
def button_confirm(self):
    for order in self:
        if order.state not in ['draft', 'sent']:
            continue
        error_msg = order._confirmation_error_message()
        if error_msg:
            raise UserError(error_msg)
        order.order_line._validate_analytic_distribution()
        order._add_supplier_to_product()
        # Deal with double validation process
        if order._approval_allowed():
            order.button_approve()
        else:
            order.write({'state': 'to approve'})
    return True
```

Steps:
1. Guard: only processes `draft` or `sent` orders
2. Validates no lines are missing products (`_confirmation_error_message()`)
3. Validates analytic distribution on all lines
4. Attempts to add vendor to product supplier list
5. Calls `_approval_allowed()` to decide single vs. two-step flow

### 1.4 `button_approve()` Method

**File**: `purchase/models/purchase_order.py`  
**Lines**: 615–619

```python
def button_approve(self, force=False):
    self = self.filtered(lambda order: order._approval_allowed())
    self.write({'state': 'purchase', 'date_approve': fields.Datetime.now()})
    self.filtered(lambda p: p.lock_confirmed_po == 'lock').write({'locked': True})
    return {}
```

Sets `state = 'purchase'` and `date_approve = now()`. Optionally locks if company setting requires it.

**purchase_stock override** (`purchase_stock/models/purchase_order.py:179-182`):
```python
def button_approve(self, force=False):
    result = super(PurchaseOrder, self).button_approve(force=force)
    self._create_picking()
    return result
```
The stock extension triggers picking creation on approval.

---

## 2. `invoice_status` Computed Field

**File**: `purchase/models/purchase_order.py`  
**Lines**: 46–68, 127–131

```python
invoice_status = fields.Selection([
    ('no', 'Nothing to Bill'),
    ('to invoice', 'Waiting Bills'),
    ('invoiced', 'Fully Billed'),
], string='Billing Status', compute='_get_invoiced', store=True, readonly=True, copy=False, default='no')
```

**Compute method** `_get_invoiced()` (lines 46–68):
- Depends on: `state`, `order_line.qty_to_invoice`
- If `state != 'purchase'` → `'no'`
- If any non-display line has non-zero `qty_to_invoice` → `'to invoice'`
- If all non-display lines have zero `qty_to_invoice` AND `invoice_ids` exist → `'invoiced'`
- Otherwise → `'no'`

**Critical**: `invoice_status` is only meaningful when `state == 'purchase'`. In all other states it returns `'no'`.

---

## 3. `receipt_status` Computed Field

**IMPORTANT**: `receipt_status` is NOT defined in the base `purchase` module. It is defined in the `purchase_stock` extension module.

**File**: `purchase_stock/models/purchase_order.py`  
**Lines**: 35–42, 68–78

```python
receipt_status = fields.Selection([
    ('pending', 'Not Received'),
    ('partial', 'Partially Received'),
    ('full', 'Fully Received'),
], string='Receipt Status', compute='_compute_receipt_status', store=True, ...)
```

**Compute method** `_compute_receipt_status()` (lines 68–78):
- Depends on: `picking_ids`, `picking_ids.state`
- `False` if no pickings or all pickings are cancelled
- `'full'` if all pickings are in state 'done' or 'cancel'
- `'partial'` if any picking is 'done' (but not all)
- `'pending'` otherwise

**Note**: The base purchase module v19 does NOT have `nothing/to_receive/received` values — those were an older version's design. Current values are `pending/partial/full` from purchase_stock.

---

## 4. `_compute_is_shipped()` Method

**File**: `purchase_stock/models/purchase_order.py`  
**Lines**: 60–66

```python
@api.depends('picking_ids', 'picking_ids.state')
def _compute_is_shipped(self):
    for order in self:
        if order.picking_ids and all(x.state in ['done', 'cancel'] for x in order.picking_ids):
            order.is_shipped = True
        else:
            order.is_shipped = False
```

`is_shipped` is True only when there are pickings AND all are done/cancelled. An order with no pickings returns False.

---

## 5. `_create_invoices()` / `action_create_invoice()`

**File**: `purchase/models/purchase_order.py`  
**Lines**: 760–833

The public method is `action_create_invoice()`. Flow:

1. **Prepare header** via `_prepare_invoice()` (lines 925–945):
   - `move_type = 'in_invoice'`
   - Copies `currency_id`, `partner_id`, `fiscal_position_id`, `payment_term_id`
   - Sets `invoice_origin = self.name` (PO name, NOT partner_ref)
   - Sets `narration = self.note`

2. **Prepare lines**: For each PO line (skipping display-type lines), calls `line._prepare_account_move_line()`.

3. **Group by** `(company_id, partner_id, currency_id)` for batch creation — multiple POs from same vendor in same currency are merged into one bill.

4. **Create** `account.move` records with `move_type='in_invoice'`.

5. **Auto-switch** moves with negative total to refunds via `action_switch_move_type()`.

**Line preparation** `_prepare_account_move_line()` (`purchase_order_line.py:628-647`):
- `quantity` = `qty_to_invoice` (negative for refunds)
- Carries `purchase_line_id` (foreign key to PO line)
- Carries `tax_ids`, `price_unit`, `discount`, `product_id`, `product_uom_id`
- Does NOT carry analytic information at this stage

---

## 6. `qty_received` vs `qty_invoiced` on PO Line

### 6.1 `qty_received`

**File**: `purchase/models/purchase_order_line.py`  
**Lines**: 68–73, 233–258

```python
qty_received_method = fields.Selection([('manual', 'Manual')], ...)
qty_received = fields.Float("Received Qty", compute='_compute_qty_received', inverse='_inverse_qty_received', compute_sudo=True, store=True, ...)
qty_received_manual = fields.Float("Manual Received Qty", ...)
```

In the base `purchase` module, only `manual` method is supported. For stockable products, `purchase_stock` overrides `_compute_qty_received_method` to return 'stock_moves', and overrides `_compute_qty_received` to sum done move quantities.

`_compute_qty_received` (line 233–258): delegates to `_prepare_qty_received()` which reads `qty_received_manual` for manual method or returns 0.0 otherwise.

### 6.2 `qty_invoiced`

**File**: `purchase/models/purchase_order_line.py`  
**Lines**: 66, 171–207

```python
qty_invoiced = fields.Float(compute='_compute_qty_invoiced', string="Billed Qty", digits='Product Unit', store=True)
```

Computed by `_compute_qty_invoiced()` (lines 171–207):
- Depends on `invoice_lines.move_id.state`, `invoice_lines.quantity`, `qty_received`, `product_uom_qty`, `order_id.state`
- Sums `invoice_lines` quantities (via `_prepare_qty_invoiced()`):
  - `in_invoice` lines add to qty
  - `in_refund` lines subtract from qty
  - Excludes cancelled moves unless `payment_state == 'invoicing_legacy'`

### 6.3 `qty_to_invoice` — The 3-Way Match Bridge

**File**: `purchase/models/purchase_order_line.py`  
**Lines**: 178–184

```python
if line.order_id.state == 'purchase':
    if line.product_id.purchase_method == 'purchase':
        line.qty_to_invoice = line.product_qty - line.qty_invoiced
    else:
        line.qty_to_invoice = line.qty_received - line.qty_invoiced
else:
    line.qty_to_invoice = 0
```

- `purchase_method = 'purchase'` (ordered): invoice against ordered qty
- `purchase_method = 'receive'` (received): invoice against received qty — this is the 3-way match mode
- Only non-zero when state is 'purchase'

---

## 7. Purchase Approval Flow

### 7.1 `_approval_allowed()` Method

**File**: `purchase/models/purchase_order.py`  
**Lines**: 1251–1260

```python
def _approval_allowed(self):
    """Returns whether the order qualifies to be approved by the current user"""
    self.ensure_one()
    return (
        self.company_id.po_double_validation == 'one_step'
        or (self.company_id.po_double_validation == 'two_step'
            and self.amount_total < self.env.company.currency_id._convert(
                self.company_id.po_double_validation_amount, self.currency_id, self.company_id,
                self.date_order or fields.Date.today()))
        or self.env.user.has_group('purchase.group_purchase_manager'))
```

Returns True (single-step approval allowed) when:
1. Company uses `one_step` validation, OR
2. Two-step mode but amount is below threshold, OR
3. Current user has `purchase.group_purchase_manager` group (bypasses threshold)

### 7.2 Company Configuration

**File**: `purchase/models/res_company.py`  
**Lines**: 16–23

```python
po_double_validation = fields.Selection([
    ('one_step', 'Confirm purchase orders in one step'),
    ('two_step', 'Get 2 levels of approvals to confirm a purchase order')
    ], string="Levels of Approvals", default='one_step', ...)

po_double_validation_amount = fields.Monetary(string='Double validation amount', default=5000, ...)
```

Default: `one_step`. Two-step threshold defaults to 5000 (company currency).

### 7.3 SUPERUSER_ID Usage

**File**: `purchase_stock/models/purchase_order.py`  
**Line**: 386

The `purchase_stock` extension uses `SUPERUSER_ID` when creating stock pickings: `StockPicking.with_user(SUPERUSER_ID).create(res)`. This is a stock-layer bypass, not a purchase approval bypass.

---

## 8. `date_approve`, `date_order`, `effective_date`

### 8.1 `date_approve`

**File**: `purchase/models/purchase_order.py`  
**Lines**: 90, 617

```python
date_approve = fields.Datetime('Confirmation Date', readonly=True, index=True, copy=False)
```

Set exclusively in `button_approve()`: `self.write({'state': 'purchase', 'date_approve': fields.Datetime.now()})`.
Readable from the PO line as a related field (purchase_order_line.py:94).

### 8.2 `date_order`

**File**: `purchase/models/purchase_order.py`  
**Line**: 88

```python
date_order = fields.Datetime('Order Deadline', required=True, index=True, copy=False, default=fields.Datetime.now, ...)
```

The deadline date for RFQ confirmation. Not set by approval, set at creation time (or manually edited).

### 8.3 `effective_date`

**File**: `purchase_stock/models/purchase_order.py`  
**Lines**: 32–33, 54–58

```python
effective_date = fields.Datetime("Arrival", compute='_compute_effective_date', store=True, copy=False,
    help="Completion date of the first receipt order.")
```

Computed: `min(pickings.date_done)` for pickings that are 'done' and destination is not 'supplier'. Defined in `purchase_stock`, not in base `purchase`.

### 8.4 `date_calendar_start`

**File**: `purchase/models/purchase_order.py`  
**Lines**: 206–209

```python
@api.depends('state', 'date_order', 'date_approve')
def _compute_date_calendar_start(self):
    for order in self:
        order.date_calendar_start = order.date_approve if (order.state == 'purchase') else order.date_order
```

Used for calendar/timeline purposes: shows `date_approve` when confirmed, `date_order` otherwise.

---

## 9. MIGRATION FLAG: `analytic_account_id` ABSENT

**CONFIRMED ABSENT**: The `purchase.order.line` model in v19 Community does NOT have an `analytic_account_id` field.

Instead, analytic information is handled via `analytic_distribution` (a JSON dict) through the `analytic.mixin` mechanism:

**File**: `purchase/models/purchase_order_line.py`  
**Line**: 16

```python
class PurchaseOrderLine(models.Model):
    _name = 'purchase.order.line'
    _inherit = ['analytic.mixin']
```

The `analytic.mixin` provides:
- `analytic_distribution` field (JSON dict, format: `{analytic_account_id_str: percentage}`)
- `analytic_distribution_search` for searching

**Automatic distribution** `_compute_analytic_distribution()` (lines 368–379):
- Triggered by `product_id`, `order_id.partner_id`
- Uses `account.analytic.distribution.model._get_distribution()` to auto-populate
- Based on product, product category, partner, company matching rules

**Validation** `_validate_analytic_distribution()` (lines 745–753):
- Called in `button_confirm()` before approval
- Validates against `purchase_order` business domain

**MIGRATION IMPACT**: Any migration from Odoo v16/v17 that had `analytic_account_id` on PO lines must transform to `analytic_distribution` JSON format. The field name `analytic_account_id` does NOT exist in v19.

---

## 10. `partner_ref` (Vendor Reference)

**File**: `purchase/models/purchase_order.py`  
**Lines**: 83–87

```python
partner_ref = fields.Char('Vendor Reference', copy=False,
    help="Reference of the sales order or bid sent by the vendor. "
         "It's used to do the matching when you receive the "
         "products as this reference is usually written on the "
         "delivery order sent by your vendor.")
```

### Propagation to Vendor Bill

`partner_ref` is NOT propagated to the vendor bill's `ref` field automatically by `_prepare_invoice()`.

`_prepare_invoice()` (lines 925–945) sets `invoice_origin = self.name` (the PO reference number), NOT `partner_ref`.

`partner_ref` is used as a **secondary matching key** in `account_invoice.py:_match_purchase_orders()` (lines 386–389):
```python
matching_purchase_orders |= self.env['purchase.order'].search(
    common_domain + [('partner_ref', 'in', po_references)])
```

When a vendor bill is created via EDI/OCR and references a vendor's order number, the system first tries to match by PO name, then falls back to `partner_ref`.

`partner_ref` is also included in `_rec_names_search` (line 25) allowing search by vendor reference.

**Merge behavior** (lines 883–886): When RFQs are merged, `partner_ref` values are concatenated with commas.

---

## 11. `invoice_ids` / `bill_ids` Field

**File**: `purchase/models/purchase_order.py`  
**Lines**: 70–75, 125–126

```python
invoice_ids = fields.Many2many('account.move', compute="_compute_invoice", string='Bills', copy=False, store=True)
invoice_count = fields.Integer(compute="_compute_invoice", string='Bill Count', copy=False, default=0, store=True)
```

Computed by `_compute_invoice()` (lines 70–75):
```python
def _compute_invoice(self):
    for order in self:
        invoices = order.mapped('order_line.invoice_lines.move_id')
        order.invoice_ids = invoices
        order.invoice_count = len(invoices)
```

The linkage is: `purchase.order` → `purchase.order.line.invoice_lines` → `account.move.line.move_id`. The `purchase_line_id` on `account.move.line` is set in `_prepare_account_move_line()`.

**Cancel guard** in `button_cancel()` (lines 646–648): Cannot cancel a PO if any bill is not in draft/cancel state.

---

## 12. `locked` Field and Lock Behavior

**File**: `purchase/models/purchase_order.py`  
**Lines**: 112–117

```python
locked = fields.Boolean(
    help="Locked Purchase Orders cannot be modified.",
    default=False, copy=False, tracking=True)
lock_confirmed_po = fields.Selection(related="company_id.po_lock")
```

- When `company.po_lock == 'lock'`, PO is auto-locked on `button_approve()` (line 618)
- `button_cancel()` blocks cancellation of locked POs (lines 642–644)
- `_is_readonly()` returns True only if `state == 'cancel'` (lines 1380–1388) — the locked field is a UI hint, not a hard readonly gate at model level

---

## Summary of Key Technical Facts

1. State machine has 5 values: draft/sent/to approve/purchase/cancel (no 'done' in v19 Community base)
2. `invoice_status` lives in base `purchase` module; `receipt_status` lives in `purchase_stock` extension
3. `receipt_status` uses pending/partial/full (NOT nothing/to_receive/received)
4. `_approval_allowed()` bypasses threshold for `purchase.group_purchase_manager` users
5. `date_approve` is set by `button_approve()` at exact confirmation moment
6. `effective_date` (first physical receipt) is in `purchase_stock`, not base
7. `analytic_account_id` is ABSENT — replaced by `analytic_distribution` JSON via `analytic.mixin`
8. `partner_ref` is not auto-propagated to bill; used for reverse-matching only
9. `qty_to_invoice` is computed differently based on `purchase_method` ('purchase' vs 'receive')
10. Bill linkage flows through `purchase.order.line → account.move.line.purchase_line_id → account.move`
