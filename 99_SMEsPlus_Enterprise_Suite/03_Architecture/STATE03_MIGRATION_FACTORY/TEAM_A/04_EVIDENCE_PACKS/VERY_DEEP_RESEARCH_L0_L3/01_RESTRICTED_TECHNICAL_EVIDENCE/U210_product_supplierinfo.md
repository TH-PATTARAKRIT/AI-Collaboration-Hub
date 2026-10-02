# U210 — product.supplierinfo: Vendor Pricelist Model
## STATE03 VDR — Restricted Technical Evidence

**Unit**: U210  
**Module**: product_supplierinfo  
**Addons**: `product`, `purchase`  
**Research depth**: L0–L3  
**Gate**: GREEN

---

## 1. Model Definition

**File**: `product/models/product_supplierinfo.py`  
**Class**: `ProductSupplierinfo`  
**`_name`**: `product.supplierinfo`  
**`_description`**: "Supplier Pricelist"  
**`_order`**: `sequence, min_qty DESC, price, id`  (line 10)  
**`_rec_name`**: `partner_id`

---

## 2. Field Inventory (v19)

| Field | Type | Line | Notes |
|---|---|---|---|
| `partner_id` | Many2one `res.partner` | 13 | required, `ondelete='cascade'`, `check_company=True` |
| `product_name` | Char | 17 | Vendor-specific product name for RFQ printing |
| `product_code` | Char | 20 | Vendor-specific product code for RFQ printing |
| `sequence` | Integer | 23 | default=1; priority ordering across vendor entries |
| `product_uom_id` | Many2one `uom.uom` | 25 | computed+stored, `readonly=False`; defaults to product UoM |
| `min_qty` | Float | 27 | default=0.0, required; qty threshold to trigger price |
| `price` | Float | 30 | `min_display_digits='Product Price'`; base unit price |
| `price_discounted` | Float | 32 | computed = `price * (1 - discount/100)` converted to product UoM |
| `company_id` | Many2one `res.company` | 33 | default=current company; `index=1` |
| `currency_id` | Many2one `res.currency` | 36 | required; defaults to company currency |
| `date_start` | Date | 40 | validity window start |
| `date_end` | Date | 41 | validity window end |
| `product_id` | Many2one `product.product` | 42 | variant-level override; computed+stored, `readonly=False` |
| `product_tmpl_id` | Many2one `product.template` | 47 | required, `index=True`, `ondelete='cascade'` |
| `product_variant_count` | Integer | 50 | related from template |
| `delay` | Integer | 51 | default=1; lead time days; used to compute `date_planned` |
| `discount` | Float | 54 | `digits='Discount'`; percentage discount applied to `price` |

### Fields NOT present in v19 (migration note)
- There is NO standalone `name` field — vendor product identity is split into `product_name` and `product_code`.
- No `base_price`, no `pricelist_id` — this model does not extend pricelist logic.

---

## 3. Computed Field: `_compute_price_discounted`

**File**: `product/models/product_supplierinfo.py` line 70–74

```python
@api.depends('discount', 'price')
def _compute_price_discounted(self):
    for rec in self:
        product_uom = (rec.product_id or rec.product_tmpl_id).uom_id
        rec.price_discounted = rec.product_uom_id._compute_price(rec.price, product_uom) * (1 - rec.discount / 100)
```

`price_discounted` converts `price` from supplier UoM to product base UoM, then applies discount.

---

## 4. Variant vs Template Level

- `product_tmpl_id` — required; applies vendor price to **all variants** of a template
- `product_id` — optional; restricts vendor price to a **specific variant** (`product.product`)
- `_get_filtered_supplier()` (line 118–119) excludes entries where `s.product_id` is set but does not match the requested variant:

```python
def _get_filtered_supplier(self, company_id, product_id, params=False):
    return self.filtered(lambda s:
        (not s.company_id or s.company_id.id == company_id.id)
        and (s.partner_id.sudo().active
             and (not s.product_id or s.product_id == product_id)))
```

---

## 5. Multi-Company Isolation

- `company_id` on `product.supplierinfo` (line 33): default = current company, `index=1`
- `check_company=True` on both `partner_id` (line 16) and `product_id` (line 43)
- `_get_filtered_supplier` base impl: filters `s.company_id.id == company_id.id` OR `not s.company_id`
- Purchase addon override (purchase/models/product.py line 151–154): when `params['order_id']` has a company, that company overrides the passed `company_id`:

```python
def _get_filtered_supplier(self, company_id, product_id, params=False):
    if params and 'order_id' in params and params['order_id'].company_id:
        company_id = params['order_id'].company_id
    return super()._get_filtered_supplier(company_id, product_id, params)
```

---

## 6. Currency: Partner-Driven Default

Purchase addon (`purchase/models/product.py` line 147–149):

```python
@api.onchange('partner_id')
def _onchange_partner_id(self):
    self.currency_id = self.partner_id.property_purchase_currency_id.id or self.env.company.currency_id.id
```

When partner is changed, `currency_id` is set to partner's purchase currency property (if set), else company default. This drives multi-currency vendor pricing.

---

## 7. `seller_ids` on `product.template`

**File**: `product/models/product_template.py` line 126–127

```python
seller_ids = fields.One2many('product.supplierinfo', 'product_tmpl_id', 'Vendors', depends_context=('company',))
variant_seller_ids = fields.One2many('product.supplierinfo', 'product_tmpl_id')
```

- `seller_ids` has `depends_context=('company',)` — Odoo caches this per-company context, ensuring different companies see their filtered vendor lists without re-querying unnecessarily.
- `variant_seller_ids` is the unfiltered version (no context dependency), used internally.

---

## 8. Seller Selection Algorithm: `_prepare_sellers` and `_select_seller`

**File**: `product/models/product_product.py`

### `_prepare_sellers` (line 1019–1021)
```python
def _prepare_sellers(self, params=False):
    sellers = self.sudo().seller_ids._get_filtered_supplier(self.env.company, self, params)
    return sellers.sorted(lambda s: (s.sequence, -s.min_qty, s.price, s.id))
```
Initial sort: `(sequence ASC, min_qty DESC, price ASC, id ASC)`.

### `_get_filtered_sellers` (line 1023–1050)
Applies per-seller filtering:
1. Date range: skip if `date_start > date` or `date_end < date`
2. UoM: if `force_uom` param set, skip mismatched UoM entries
3. Partner: skip if `seller.partner_id not in [partner_id, partner_id.parent_id]` (supports contact-of-partner)
4. Quantity: skip if `quantity_uom_seller < seller.min_qty` (converts qty to seller UoM first)
5. Variant: skip if `seller.product_id` set and does not match the requested product

### `_select_seller` (line 1052–1074)
```python
def _select_seller(self, partner_id=False, quantity=0.0, date=None, uom_id=False, ordered_by='price_discounted', params=False):
    sort_key = ('price_discounted', 'sequence', 'id')
    if ordered_by != 'price_discounted':
        sort_key = (ordered_by, 'price_discounted', 'sequence', 'id')
    ...
    sellers = self._get_filtered_sellers(...)
    res = self.env['product.supplierinfo']
    for seller in sellers:
        if not res or res.partner_id == seller.partner_id:
            res |= seller
    return res and res.sorted(sort_function)[:1]
```

Key behaviors:
- **Partner grouping**: collects all entries with the same `partner_id`, then picks the best one by discounted price
- **Final sort key**: `price_discounted` converted to company currency, then `sequence`, then `id`
- **`ordered_by` param**: allows callers to override primary sort key (e.g., `sequence` for replenishment rules)
- **Returns single record** (`:1` slice)

---

## 9. Price Resolution on PO Line

**File**: `purchase/models/purchase_order_line.py`

### `_compute_price_unit_and_date_planned_and_name` (line 420–483)

Guard: skips if `technical_price_unit != price_unit` (user manually changed price).

When `selected_seller_id` is set (line 479–483):
```python
price_unit = env['account.tax']._fix_tax_included_price_company(
    line.selected_seller_id.price, product.supplier_taxes_id, line.tax_ids, company_id)
price_unit = line.selected_seller_id.currency_id._convert(
    price_unit, line.currency_id, line.company_id,
    line.date_order or fields.Date.context_today(line), False)
line._reset_price_unit(
    line.selected_seller_id.product_uom_id._compute_price(price_unit, line.product_uom_id))
line.discount = line.selected_seller_id.discount or 0.0
```

Steps:
1. Tax-inclusive fix: extracts tax-excluded price if supplier taxes are tax-included
2. Currency conversion: from `seller.currency_id` → PO `currency_id` at order date rate
3. UoM conversion: from `seller.product_uom_id` → PO line `product_uom_id`
4. Discount propagated from `seller.discount`

When no seller found (line 454–477): falls back to `product.standard_price` converted from cost currency to PO currency.

### `_prepare_purchase_order_line` (line 663–714)

Used by procurement/scheduler to build PO lines programmatically:
```python
seller = product_id.with_company(company_id)._select_seller(
    partner_id=partner_id, quantity=..., date=..., uom_id=...,
    params={'force_uom': values.get('force_uom')})
if price_unit and seller and po.currency_id and seller.currency_id != po.currency_id:
    price_unit = seller.currency_id._convert(
        price_unit, po.currency_id, po.company_id, po.date_order or fields.Date.today())
date_planned = self.order_id.date_planned or self._get_date_planned(seller, po=po)
discount = seller.discount or 0.0
```

---

## 10. Delay → `date_planned` Mapping

**File**: `purchase/models/purchase_order_line.py` line 350–366

```python
@api.model
def _get_date_planned(self, seller, po=False):
    date_order = po.date_order if po else self.order_id.date_order
    if date_order:
        return date_order + relativedelta(days=seller.delay if seller else 0)
    else:
        return datetime.today() + relativedelta(days=seller.delay if seller else 0)
```

`delay` (integer days) is added to `date_order` to produce the expected arrival datetime. If `seller` is `False`/None, delay defaults to 0.

---

## 11. `selected_seller_id` — Technical Field

**File**: `purchase/models/purchase_order_line.py` line 103

```python
selected_seller_id = fields.Many2one('product.supplierinfo',
    compute='_compute_selected_seller_id',
    help='Technical field to get the vendor pricelist used to generate this line')
```

Computed (not stored) from `product_id`, `product_id.seller_ids`, `partner_id`, `product_qty`, `order_id.date_order`, `product_uom_id`. Acts as the bridge between supplier resolution and price/date computation.

---

## 12. `_sanitize_vals` — Data Integrity

**File**: `product/models/product_supplierinfo.py` line 101–116

On `create` and `write`: if `product_id` is provided without `product_tmpl_id`, automatically resolves and sets `product_tmpl_id`. Prevents orphaned variant-level entries.

---

## 13. Migration Flags (v16/v17 → v19)

| Flag | Description |
|---|---|
| `discount` field | Added to `product.supplierinfo` — drives `price_discounted` (new in v17+) |
| `price_discounted` computed | New field; `_select_seller` now sorts by this instead of raw `price` |
| `ordered_by` param on `_select_seller` | New parameter allowing sort-key override |
| `selected_seller_id` on PO line | Technical computed field (new); bridges seller resolution and price compute |
| `technical_price_unit` on PO line | New tracking field; guards against overwriting manually-set prices |
| `_compute_price_unit_and_date_planned_and_name` | Merged compute (was separate methods in v16) |
| `product_uom_id` computed+stored | Was likely simple stored in v16; now computed from `product_id`/`product_tmpl_id` |
| `_get_filtered_supplier` override in purchase | Extracts company from `params['order_id']` (new params contract) |

---

## Source Pointers

| File | Lines | Content |
|---|---|---|
| `product/models/product_supplierinfo.py` | 1–120 | Full model definition |
| `product/models/product_product.py` | 1019–1074 | `_prepare_sellers`, `_get_filtered_sellers`, `_select_seller` |
| `product/models/product_template.py` | 126–127 | `seller_ids`, `variant_seller_ids` |
| `purchase/models/product.py` | 144–154 | Purchase inherit: `_onchange_partner_id`, `_get_filtered_supplier` override |
| `purchase/models/purchase_order_line.py` | 103, 272–283, 350–366, 420–483, 663–714 | Selected seller, price/date compute, `_prepare_purchase_order_line` |
