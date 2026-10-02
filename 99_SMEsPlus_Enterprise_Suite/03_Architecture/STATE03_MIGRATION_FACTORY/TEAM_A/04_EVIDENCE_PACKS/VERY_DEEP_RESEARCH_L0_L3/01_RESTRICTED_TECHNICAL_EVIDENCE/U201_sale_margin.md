# U201 — sale_margin: Margin Computation and Cost Method Interface
## STATE03 VDR — Restricted Technical Evidence

**Unit:** U201  
**Module:** sale_margin  
**Research date:** 2026-10-02  
**Gate:** GREEN  
**Source tree:** /Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons  
**Security:** READ-ONLY. No Odoo process started. No Enterprise/Extra_Thailand/OEEL files read.

---

## 1. Module Structure

**`sale_margin/__manifest__.py`** (lines 1-24)
- Version: `1.0`, category: `Sales/Sales`
- Depends: `['sale_management']` only — no stock, no purchase, no accounting dependency
- License: LGPL-3
- Data: `views/sale_order_views.xml`
- Demo: `data/sale_margin_demo.xml`

**Models directory** (`sale_margin/models/__init__.py` lines 4-5):
- Imports `sale_order` and `sale_order_line`

---

## 2. Fields on `sale.order.line` — `sale_margin/models/sale_order_line.py`

### 2.1 `margin` field (line 10-12)
```python
margin = fields.Float(
    "Margin", compute='_compute_margin',
    min_display_digits='Product Price', store=True, groups="base.group_user", precompute=True)
```
- **Type:** Float
- **Computed:** yes, by `_compute_margin`
- **Stored:** yes
- **Precompute:** yes (computed at record creation before save)
- **Access:** `base.group_user` only (hidden from portal/public)
- **Display precision:** follows `Product Price` decimal setting

### 2.2 `margin_percent` field (line 13-14)
```python
margin_percent = fields.Float(
    "Margin (%)", compute='_compute_margin', store=True, groups="base.group_user", precompute=True)
```
- **Type:** Float (ratio, e.g. 0.30 = 30%)
- **Computed:** yes, by `_compute_margin` (same compute method as `margin`)
- **Stored:** yes
- **Precompute:** yes

### 2.3 `purchase_price` field (line 15-18)
```python
purchase_price = fields.Float(
    string="Cost", compute="_compute_purchase_price",
    min_display_digits='Product Price', store=True, readonly=False, copy=False, precompute=True,
    groups="base.group_user")
```
- **Type:** Float, string label "Cost"
- **Computed:** yes, by `_compute_purchase_price`
- **Stored:** yes
- **readonly=False:** user CAN manually override the computed cost
- **copy=False:** when SO is duplicated, purchase_price is NOT copied — it is recomputed from current product standard_price
- **Precompute:** yes

---

## 3. `_compute_purchase_price()` — `sale_order_line.py` lines 20-36

```python
@api.depends('product_id', 'company_id', 'currency_id', 'product_uom_id')
def _compute_purchase_price(self):
    for line in self:
        if not line.product_id:
            line.purchase_price = 0.0
            continue
        line = line.with_company(line.company_id)

        # Convert the cost to the line UoM
        product_cost = line.product_id.uom_id._compute_price(
            line.product_id.standard_price,
            line.product_uom_id,
        )

        line.purchase_price = line._convert_to_sol_currency(
            product_cost,
            line.product_id.cost_currency_id)
```

**Trigger dependencies:** `product_id`, `company_id`, `currency_id`, `product_uom_id`

**Logic flow:**
1. If `product_id` is False: set `purchase_price = 0.0`, skip
2. Execute under `line.with_company(line.company_id)` to read company-dependent `standard_price` in the correct company context
3. **Step 1 — UoM conversion:** `product_id.uom_id._compute_price(standard_price, product_uom_id)` — converts standard_price from product's native UoM to the SO line's UoM
4. **Step 2 — Currency conversion:** `_convert_to_sol_currency(product_cost, product_id.cost_currency_id)` — converts from product company currency to SO currency

**AVCO/FIFO/Standard behaviour:**
- `standard_price` is `company_dependent=True` (product_product.py lines 62-68)
- For AVCO: standard_price is automatically updated by the valuation layer each time stock moves occur
- For FIFO: standard_price reflects the last known cost (but valuation uses actual lots/layers)
- For Standard: standard_price is manually set
- In all cases, `purchase_price` on the SO line is a **snapshot** of `standard_price` at the time `_compute_purchase_price` runs — it is NOT automatically updated by subsequent inventory movements

---

## 4. `_compute_margin()` — `sale_order_line.py` lines 38-48

```python
@api.depends('price_subtotal', 'product_uom_qty', 'purchase_price')
def _compute_margin(self):
    for line in self:
        # Find alternative calculation when line is added to order from delivery
        if line.qty_delivered and not line.product_uom_qty:
            calculated_subtotal = line.price_unit * line.qty_delivered
            line.margin = calculated_subtotal - (line.purchase_price * line.qty_delivered)
            line.margin_percent = calculated_subtotal and line.margin / calculated_subtotal
        else:
            line.margin = line.price_subtotal - (line.purchase_price * line.product_uom_qty)
            line.margin_percent = line.price_subtotal and line.margin / line.price_subtotal
```

**Trigger dependencies:** `price_subtotal`, `product_uom_qty`, `purchase_price`

**Normal branch (product_uom_qty > 0):**
- `margin = price_subtotal - (purchase_price * product_uom_qty)`
- `margin_percent = price_subtotal and margin / price_subtotal` (0.0 when price_subtotal is 0)

**Delivery-added line branch (qty_delivered > 0 AND product_uom_qty == 0):**
- `calculated_subtotal = price_unit * qty_delivered`
- `margin = calculated_subtotal - (purchase_price * qty_delivered)`
- `margin_percent = calculated_subtotal and margin / calculated_subtotal`

**Notes:**
- `price_subtotal` is computed by `sale.order.line._compute_amount` (sale/models/sale_order_line.py:854-864), which is tax-excluded subtotal
- When price_subtotal = 0 and purchase_price = 0: margin = 0, margin_percent = 0
- When price_subtotal > 0 and purchase_price = 0: margin = price_subtotal, margin_percent = 1.0 (100%)
- Negative margin is possible and supported (confirmed by test_negative_margin)

---

## 5. `_convert_to_sol_currency()` — `sale/models/sale_order_line.py` lines 1755-1776

```python
def _convert_to_sol_currency(self, amount, currency):
    self.ensure_one()
    to_currency = self.currency_id or self.order_id.currency_id
    if currency and to_currency and currency != to_currency:
        conversion_date = self.order_id.date_order or fields.Date.context_today(self)
        company = self.company_id or self.order_id.company_id or self.env.company
        return currency._convert(
            from_amount=amount,
            to_currency=to_currency,
            company=company,
            date=conversion_date,
            round=False,
        )
    return amount
```

**Multi-currency behaviour:**
- Source: `product_id.cost_currency_id` = `company_id.currency_id` (product_template.py:264-267)
- Target: SO line's `currency_id` or `order_id.currency_id`
- Exchange date: `order_id.date_order` (order confirmation date) or context_today if not set
- `round=False` preserves precision during conversion

**`cost_currency_id` definition** (product_template.py lines 90-91, 264-267):
```python
cost_currency_id = fields.Many2one('res.currency', 'Cost Currency', compute='_compute_cost_currency_id')
# ...
template.cost_currency_id = template.company_id.sudo().currency_id.id or env_currency_id
```
- Always equals the product's company currency (or environment company currency if product has no company)

---

## 6. `sale.order` Margin Fields — `sale_margin/models/sale_order.py` lines 1-32

### 6.1 Header-level fields
```python
margin = fields.Monetary("Margin", compute='_compute_margin', store=True, groups="base.group_user")
margin_percent = fields.Float(
    "Margin (%)", compute='_compute_margin', store=True, aggregator="avg", groups="base.group_user")
```
- `margin` is `Monetary` (uses `currency_id` of the order)
- `margin_percent` has `aggregator="avg"` — pivot/graph views average the percentage across orders

### 6.2 `_compute_margin()` on sale.order (lines 14-32)
```python
@api.depends('order_line.margin', 'amount_untaxed')
def _compute_margin(self):
    if not all(self._ids):
        for order in self:
            order.margin = sum(order.order_line.mapped('margin'))
            order.margin_percent = order.amount_untaxed and order.margin/order.amount_untaxed
    else:
        grouped_order_lines_data = self.env['sale.order.line']._read_group(
            [('order_id', 'in', self.ids)], ['order_id'], ['margin:sum'])
        mapped_data = {order.id: margin for order, margin in grouped_order_lines_data}
        for order in self:
            order.margin = mapped_data.get(order.id, 0.0)
            order.margin_percent = order.amount_untaxed and order.margin/order.amount_untaxed
```

**Two execution paths:**
- **Onchange / new record** (`not all(self._ids)`): uses Python `mapped('margin')` — works with unsaved records
- **Batch / install recomputation** (`all(self._ids)`): uses `_read_group` SQL aggregation for performance

**`margin_percent` formula at order level:**
- `order.margin / order.amount_untaxed` (not averaged from line percentages)
- `amount_untaxed` is the denominator (tax-excluded total, same basis as price_subtotal on lines)

---

## 7. Sale Analysis Report — `sale_margin/report/sale_report.py` lines 1-18

```python
class SaleReport(models.Model):
    _inherit = 'sale.report'

    margin = fields.Float('Margin')

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['margin'] = f"""SUM(l.margin
            / {self._case_value_or_one('s.currency_rate')}
            * {self._case_value_or_one('account_currency_table.rate')})
        """
        return res
```

**`_case_value_or_one(value)`** is defined in `sale/report/sale_report.py:169-170`:
```python
def _case_value_or_one(self, value):
    return f"""CASE COALESCE({value}, 0) WHEN 0 THEN 1.0 ELSE {value} END"""
```

The report normalises stored `margin` values (in each SO's currency) to the reporting currency by dividing by the SO's rate and multiplying by the reporting currency rate.

---

## 8. Views — `sale_margin/views/sale_order_views.xml`

**Form view additions (lines 10-31):**
- After `tax_totals`: adds a `margin` / `margin_percent` display block on the order header
- `margin_percent` hidden when `amount_untaxed == 0` (line 16)
- Inline form for order line: `purchase_price` inserted after `price_unit`
- List view for order line: `purchase_price` (optional="hide"), `margin` (optional="hide"), `margin_percent` (optional="hide", invisible when `price_subtotal == 0`)

---

## 9. sale_purchase Integration — `sale_purchase/models/sale_order_line.py`

The `sale_purchase` module adds `purchase_line_ids` (One2many to `purchase.order.line`) on `sale.order.line` for tracking generated POs. **It does NOT add any field or method that writes back to `purchase_price` on the SO line.** There is no trigger or onchange that updates `purchase_price` when the linked PO price changes. The `purchase_price` on the SO line remains the snapshot taken at `_compute_purchase_price` time.

---

## 10. AVCO vs FIFO Impact on Margin

Since `purchase_price` is a snapshot of `standard_price` at SO line creation:
- **AVCO:** `standard_price` is continuously updated by stock valuation. A new SO line picks up the running average cost. Historical SO lines retain their original snapshot.
- **FIFO:** `standard_price` reflects last cost update but actual COGS may differ (FIFO uses stock lots/layers). Margin computation uses `standard_price` snapshot, NOT actual FIFO COGS.
- **Standard:** `standard_price` is fixed manually. All SO lines pick up the same value until manually changed.
- **Migration note:** This snapshot behaviour is unchanged from v16/v17.

---

## 11. Migration Flags (v16/v17 → v19)

1. **`precompute=True`** is present on all three fields (`margin`, `margin_percent`, `purchase_price`). This attribute was introduced more prominently in v16/v17 ORM. Ensure migration scripts do not conflict with precompute behaviour.

2. **`copy=False` on `purchase_price`:** This means SO duplication triggers a fresh recompute from current standard_price. Any migration data copy must explicitly exclude `purchase_price` from direct copy to preserve this semantic.

3. **`min_display_digits='Product Price'`** on `margin` and `purchase_price`: references the decimal precision record named 'Product Price'. Confirm this precision record exists after migration.

4. **`aggregator="avg"` on `sale.order.margin_percent`:** In v17+ ORM, `aggregator` replaces the deprecated `group_operator`. Confirm ORM compatibility.

5. **`sale.order.margin` is `fields.Monetary`** (not Float). In earlier versions it may have been Float. Migration must handle the currency linkage.

6. **Batch path in `_compute_margin`:** Uses `_read_group` with `margin:sum` aggregation syntax. Confirm this syntax is supported in target ORM version.

7. **No `sale_purchase` linkage to `purchase_price`:** Any migration assumption that PO confirmation updates SO line cost is incorrect — it does not.

---

## 12. Thai Localization (THB)

No Thai-specific logic exists in `sale_margin`. THB margins compute identically to any other currency:
- `standard_price` stored in company currency (THB for Thai company)
- If SO is in THB and company is THB: no conversion needed (`_convert_to_sol_currency` returns amount unchanged)
- If SO is in foreign currency: standard `currency._convert` with rate at `date_order`
- No Thai tax or rounding overrides affect margin fields

---

## 13. Test Coverage Summary — `sale_margin/tests/test_sale_margin.py`

| Test | Coverage |
|------|----------|
| `test_sale_margin` | Basic margin and margin_percent on confirmed SO |
| `test_negative_margin` | price_unit < cost; zero-cost line |
| `test_margin_no_cost` | Zero standard_price → 100% margin |
| `test_margin_considering_product_qty` | Multi-line, multi-qty margin aggregation |
| `test_sale_margin_order_copy` | copy=False: purchase_price refreshes to current standard_price on copy |

Key assertion from `test_sale_margin_order_copy` (lines 117-126):
- Original SO: standard_price=500, purchase_price=500, margin=5000 (10 units × (1000−500))
- After standard_price changed to 750 and SO copied: purchase_price=750, margin=2500
- Confirms: `copy=False` + `precompute=True` causes recomputation from current cost on copy

---

*All paths verified by direct Read of source files. No fabrication.*
