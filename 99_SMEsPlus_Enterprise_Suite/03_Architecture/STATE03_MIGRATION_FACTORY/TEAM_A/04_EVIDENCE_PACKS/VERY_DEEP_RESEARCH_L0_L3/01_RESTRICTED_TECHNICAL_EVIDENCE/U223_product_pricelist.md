# U223 — product.pricelist: Model, Item Types, compute_price_rule, Version
**Unit**: U223 | **Module**: product (product_pricelist.py + product_pricelist_item.py) | **Gate**: GREEN
**Source tree**: READ-ONLY. Community only. No Enterprise files.

---

## Source Files

| File | SHA-256 (first 16 hex) |
|------|------------------------|
| `odoo/addons/product/models/product_pricelist.py` | `6b815101ef0a086f` |
| `odoo/addons/product/models/product_pricelist_item.py` | (see below) |
| `odoo/addons/product/models/res_partner.py` | (partner pricelist field) |
| `odoo/addons/point_of_sale/models/pos_config.py` | (POS integration) |

**Base path prefix** (omitted from all pointer paths below):
`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/`

---

## 1. product.pricelist — Model Definition

**File**: `product/models/product_pricelist.py`

### Class Header
```
product_pricelist.py:9   class ProductPricelist(models.Model):
product_pricelist.py:10      _name = 'product.pricelist'
product_pricelist.py:11      _inherit = ['mail.thread', 'mail.activity.mixin']
product_pricelist.py:14      _order = "sequence, id, name"
```

### Core Fields
| Field | Type | Key attributes | Line |
|-------|------|----------------|------|
| `name` | Char | required, translate=True | :28 |
| `currency_id` | Many2one(res.currency) | required, default=company.currency_id | :36-41 |
| `company_id` | Many2one(res.company) | optional, default=env.company | :43-47 |
| `item_ids` | One2many(product.pricelist.item) | copy=True, domain filters active products | :58-64 |
| `country_group_ids` | Many2many(res.country.group) | used for partner pricelist assignment by country | :49-56 |
| `active` | Boolean | default=True | :30-33 |
| `sequence` | Integer | default=16 | :34 |

**MIGRATION FLAG**: `discount_policy` field is **NOT PRESENT** in v19 Community. It existed in v13-v14 but was removed. No trace of `discount_policy` in product_pricelist.py or product_pricelist_item.py in v19.

---

## 2. product.pricelist.item — Model Definition

**File**: `product/models/product_pricelist_item.py`

### Class Header
```
product_pricelist_item.py:9    class ProductPricelistItem(models.Model):
product_pricelist_item.py:10       _name = 'product.pricelist.item'
product_pricelist_item.py:11       _order = "applied_on, min_quantity desc, categ_id desc, id desc"
product_pricelist_item.py:12       _check_company_auto = True
```

### applied_on Selection (Rule Scope)
```python
# product_pricelist_item.py:51-61
applied_on = fields.Selection(
    selection=[
        ('3_global', "All Products"),
        ('2_product_category', "Product Category"),
        ('1_product', "Product"),
        ('0_product_variant', "Product Variant"),
    ],
    default='3_global', required=True)
```
The numeric prefix in the selection key drives `_order`. `0_product_variant` sorts FIRST (most specific), `3_global` sorts LAST (least specific).

### compute_price Selection (Pricing Method)
```python
# product_pricelist_item.py:106-114
compute_price = fields.Selection(
    selection=[
        ('percentage', "Discount"),
        ('formula', "Formula"),
        ('fixed', "Fixed Price"),
    ],
    default='fixed', required=True)
```

### base Selection (Price Base for Percentage/Formula)
```python
# product_pricelist_item.py:91-103
base = fields.Selection(
    selection=[
        ('list_price', 'Sales Price'),
        ('standard_price', 'Cost'),
        ('pricelist', 'Other Pricelist'),
    ],
    default='list_price', required=True)
```

### Key Item Fields
| Field | Type | Purpose | Line |
|-------|------|---------|------|
| `date_start` | Datetime | Rule validity start (inclusive) | :34-37 |
| `date_end` | Datetime | Rule validity end (inclusive) | :38-41 |
| `min_quantity` | Float | Minimum qty for rule to apply (in product UoM) | :43-49 |
| `fixed_price` | Float | Price for compute_price='fixed' | :116 |
| `percent_price` | Float | Discount % for compute_price='percentage' | :117-119 |
| `price_discount` | Float | Discount % for formula (positive=discount, negative=markup) | :121-125 |
| `price_surcharge` | Float | Fixed amount added after discount | :132-135 |
| `price_round` | Float | Round to nearest multiple after discount, before surcharge | :126-131 |
| `price_min_margin` | Float | Minimum margin over base (formula only) | :145-148 |
| `price_max_margin` | Float | Maximum margin over base (formula only) | :149-152 |
| `price_markup` | Float | Computed inverse of price_discount (-price_discount) | :137-143 |
| `base_pricelist_id` | Many2one | Other pricelist when base='pricelist' | :104 |

---

## 3. _compute_price_rule() — Matching Algorithm

**File**: `product/models/product_pricelist.py:169-236`

### Signature
```python
def _compute_price_rule(
    self, products, quantity, *, currency=None, uom=None, date=False, compute_price=True, **kwargs
):
```
Returns `dict{product_id: (price, suitable_rule_id)}`

### Algorithm (lines 191-236)
1. **Currency fallback** (:193): `currency = currency or self.currency_id or self.env.company.currency_id`
2. **Date default** (:199-201): If no date, use `fields.Datetime.now()`
3. **Fetch rules** (:204): `rules = self._get_applicable_rules(products, date, **kwargs)` — single ORM search call
4. **Per-product loop** (:207):
   - Convert qty to product UoM if target_uom differs (:215-219)
   - Iterate rules in ORDER order; call `rule._is_applicable_for(product, qty_in_product_uom)` (:222-224)
   - **First matching rule wins** — `break` at :225
   - If `compute_price=True`: call `suitable_rule._compute_price(...)` (:227-229)
   - If no rule matched: `suitable_rule` is empty recordset; `_compute_price()` falls through to `_compute_base_price()` which returns `list_price`
5. Returns `{product.id: (price, suitable_rule.id)}` (:234)

### Rule Sort Order (critical for tie-breaking)
`_order = "applied_on, min_quantity desc, categ_id desc, id desc"` (product_pricelist_item.py:11)
- `0_product_variant` < `1_product` < `2_product_category` < `3_global` — so variant rules are evaluated first
- Within same `applied_on`, higher `min_quantity` evaluated first (largest qty break wins)
- Then `categ_id desc` (higher categ ID, i.e., more recently created category first)
- Then `id desc` (more recently created rule first)

---

## 4. _get_applicable_rules_domain() — Domain Filter

**File**: `product/models/product_pricelist.py:248-264`

```python
return [
    ('pricelist_id', '=', self.id),
    '|', ('categ_id', '=', False), ('categ_id', 'parent_of', products.categ_id.ids),
    '|', ('product_tmpl_id', '=', False), templates_domain,
    '|', ('product_id', '=', False), products_domain,
    '|', ('date_start', '=', False), ('date_start', '<=', date),
    '|', ('date_end', '=', False), ('date_end', '>=', date),
]
```
All conditions are AND-joined. Date filters use `<=` for start and `>=` for end (both inclusive). Category uses `parent_of` operator (hierarchical match — category or any ancestor).

---

## 5. _is_applicable_for() — Per-Rule Check

**File**: `product/models/product_pricelist_item.py:526-568`

Checks in order:
1. `min_quantity` — if set, `qty_in_product_uom < self.min_quantity` → False (:541)
2. `applied_on == '2_product_category'` — checks `product.categ_id.parent_path.startswith(self.categ_id.parent_path)` (:544-549)
3. Product template rules (:551-558): checks product_id, product_tmpl_id match
4. Product variant rules (:560-566): checks product_id exact match

---

## 6. _compute_price() — Item Price Computation

**File**: `product/models/product_pricelist_item.py:570-626`

Three branches on `compute_price`:

### Fixed (`compute_price='fixed'`)
```python
# :601-602
price = convert(self.fixed_price)
```
UoM conversion applied to `fixed_price`. No currency conversion here (fixed_price is in pricelist currency).

### Percentage (`compute_price='percentage'`)
```python
# :603-605
base_price = self._compute_base_price(...)
price = (base_price - (base_price * (self.percent_price / 100))) or 0.0
```

### Formula (`compute_price='formula'`)
```python
# :606-622
base_price = self._compute_base_price(...)
discount = self.price_discount if self.base != 'standard_price' else -self.price_markup
price = base_price - (base_price * (discount / 100))
if self.price_round:
    price = float_round(price, precision_rounding=self.price_round)
if self.price_surcharge:
    price += convert(self.price_surcharge)
if self.price_min_margin:
    price = max(price, price_limit + convert(self.price_min_margin))
if self.price_max_margin:
    price = min(price, price_limit + convert(self.price_max_margin))
```
Note: `price_discount` is used for `list_price`/`pricelist` bases; `-price_markup` (i.e. `price_discount` sign-flipped) is used when `base='standard_price'`.

### Empty self (fallback)
```python
# :623-624  No matching rule
price = self._compute_base_price(product, quantity, uom, date, currency, **kwargs)
```
Falls back to `list_price` of the product.

---

## 7. _compute_base_price() — Currency Conversion

**File**: `product/models/product_pricelist_item.py:628-659`

```python
rule_base = self.base or 'list_price'
if rule_base == 'pricelist' and self.base_pricelist_id:
    price = self.base_pricelist_id._get_product_price(...)   # recursive
    src_currency = self.base_pricelist_id.currency_id
elif rule_base == "standard_price":
    src_currency = product.cost_currency_id
    price = product._price_compute(rule_base, uom=uom, date=date)[product.id]
else:  # list_price
    src_currency = product.currency_id
    price = product._price_compute(rule_base, uom=uom, date=date)[product.id]

if src_currency != currency:
    price = src_currency._convert(price, currency, self.env.company, date, round=False)
```
Currency conversion via `res.currency._convert()` at line 657 — converts to pricelist currency when source differs. This handles the case where `product.currency_id != pricelist.currency_id`.

---

## 8. _get_partner_pricelist_multi() — Partner Assignment

**File**: `product/models/product_pricelist.py:334-375`
**Partner field**: `product/models/res_partner.py:14-45`

### Priority Chain
1. `partner.specific_property_product_pricelist` — company-dependent field, explicitly saved on partner (:360-362)
2. Fallback by country: `_get_country_pricelist_multi(country_ids)` — finds pricelist whose `country_group_ids` contains partner's country (:365-373)
3. Country fallback (:309-321): first pricelist with no country groups, then ir.config_parameter `res.partner.property_product_pricelist_{company_id}`, then `res.partner.property_product_pricelist`, then first active pricelist

### Feature Gate
```python
# product_pricelist.py:348-350
if not self.env['res.groups']._is_feature_enabled('product.group_product_pricelist'):
    return defaultdict(lambda: ProductPricelist)
```
When pricelists are disabled (feature flag off), all partners get empty pricelist.

### Partner Field
```python
# res_partner.py:14-22
property_product_pricelist = fields.Many2one(
    comodel_name='product.pricelist',
    compute='_compute_product_pricelist',
    inverse="_inverse_product_pricelist",
    company_dependent=False,  # behave like company dependent but is NOT
    ...
)
```
The inverse (`_inverse_product_pricelist`) saves to `specific_property_product_pricelist` only if the value differs from the country default.

---

## 9. MIGRATION FLAGS

### product.pricelist.version — REMOVED
No `product.pricelist.version` model exists in v19 Community source. Confirmed by:
- No Python file named `product_pricelist_version.py` found in product addon models
- No class `ProductPricelistVersion` anywhere in community addons
- In v13/v14, version had `date_start`/`date_end` scoping at version level; in v15+ this was collapsed into item-level `date_start`/`date_end` fields directly on `product.pricelist.item`

### discount_policy — REMOVED
The `discount_policy` field (`'without_discount'` / `'discount'`) on `product.pricelist` is **not present** in v19 Community. This field governed whether the pricelist discount was shown as a line discount vs. absorbed into price_unit. Its removal means:
- No `discount` column toggle on SO lines driven by pricelist in Community v19
- Migration scripts from v14/v15 databases that carry `discount_policy` data must handle the field's absence

### _compute_price_before_discount() — Present but Context Changed
Method at `product_pricelist_item.py:661-684` traverses chained pricelists to find the "lowest" pricelist rule with `compute_price='percentage'`. Without `discount_policy`, this method is only called by modules that extend the pricelist (e.g., website_sale).

---

## 10. POS Integration

**File**: `point_of_sale/models/pos_config.py:139-142`

```python
pricelist_id = fields.Many2one('product.pricelist', string='Default Pricelist',
    help="The pricelist used if no customer is selected or if the customer has no Sale Pricelist configured if any.")
available_pricelist_ids = fields.Many2many('product.pricelist', string='Available Pricelists', ...)
use_pricelist = fields.Boolean("Use a pricelist.")  # :153
```

**Constraint**: All available pricelists must share the same currency as the company currency:
```python
# pos_config.py:494-495
if config.use_pricelist and any(
    config.available_pricelist_ids.mapped(lambda p: p.currency_id != config.currency_id)
):
    raise ValidationError(...)
```
POS order carries `pricelist_id` field (`pos_order.py:324`). POS preset also carries `pricelist_id` (`pos_preset.py:13`).

---

## 11. Recursion Guard

**File**: `product/models/product_pricelist_item.py:321-352`

DFS-based cycle detection (`_check_pricelist_recursion`). When a rule uses `base='pricelist'`, the constraint ensures no circular chain exists between pricelists.

Deletion guard: `_unlink_except_used_as_rule_base` (`product_pricelist.py:393-405`) prevents deletion of a pricelist that is referenced as `base_pricelist_id` in another pricelist's items.
