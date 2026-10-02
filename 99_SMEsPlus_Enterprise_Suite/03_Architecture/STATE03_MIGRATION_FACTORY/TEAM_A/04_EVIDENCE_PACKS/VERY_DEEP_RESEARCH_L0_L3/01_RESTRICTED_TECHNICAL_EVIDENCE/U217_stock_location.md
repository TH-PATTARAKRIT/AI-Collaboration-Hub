# U217 — stock.location: Location Model, Types, Hierarchy, Virtual/Scrap Locations

**Unit:** U217  
**Module:** stock (stock_location.py)  
**Source:** `/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/stock/models/stock_location.py`  
**SHA-256:** `3150838412eb5fab47e548aff1817974c43e4650fad8d990dd6483517ab957f9`  
**Secondary source:** `…/odoo/addons/stock_account/models/stock_location.py`  
**Gate:** GREEN  
**Claim count:** 20  

---

## 1. Model Declaration

**File:** `stock/models/stock_location.py` — lines 13–20

```python
class StockLocation(models.Model):
    _name = 'stock.location'
    _description = "Inventory Locations"
    _parent_name = "location_id"
    _parent_store = True
    _order = 'complete_name, id'
    _rec_names_search = ['complete_name', 'barcode']
    _check_company_auto = True
```

- `_parent_store = True` activates Odoo's adjacency-list + `parent_path` optimisation for `child_of` / `parent_of` domain operators.
- `_rec_names_search` includes `barcode` so barcode scanning resolves location records directly (line 19).
- `_check_company_auto = True` triggers automatic company consistency checks on `check_company=True` fields.

---

## 2. Key Fields

### 2.1 name / complete_name
```python
# line 29
name = fields.Char('Location Name', required=True)
# line 30
complete_name = fields.Char("Full Location Name", compute='_compute_complete_name', recursive=True, store=True)
```

`_compute_complete_name` (lines 124–130):
```python
def _compute_complete_name(self):
    for location in self:
        if location.location_id and location.usage != 'view':
            location.complete_name = '%s/%s' % (location.location_id.complete_name, location.name)
        else:
            location.complete_name = location.name
```
**Critical:** When `usage == 'view'`, the location does NOT inherit its parent's complete_name — it acts as a namespace-reset boundary. Only non-view locations walk the parent chain.

### 2.2 usage — Location Type
```python
# lines 32–47
usage = fields.Selection([
    ('supplier', 'Vendor'),
    ('view', 'Virtual'),
    ('internal', 'Internal'),
    ('customer', 'Customer'),
    ('inventory', 'Inventory Loss'),
    ('production', 'Production'),
    ('transit', 'Transit')],
    string='Location Type', default='internal', index=True, required=True, ...)
```

**Exactly 7 usage values in v19.** There is NO `own` usage type and NO `scrap` usage type. Scrap locations use `usage='inventory'`.

### 2.3 location_id (Parent) / child_ids / parent_path
```python
# line 48–50
location_id = fields.Many2one('stock.location', 'Parent Location', index=True, check_company=True, ...)
# line 51
child_ids = fields.One2many('stock.location', 'location_id', 'Contains')
# line 59
parent_path = fields.Char(index=True)
```

`_child_of()` method (lines 464–466):
```python
def _child_of(self, other_location):
    self.ensure_one()
    return self.parent_path.startswith(other_location.parent_path)
```

### 2.4 company_id
```python
# lines 60–63
company_id = fields.Many2one(
    'res.company', 'Company',
    default=lambda self: self.env.company, index=True,
    help='Let this field empty if this location is shared between companies')
```
`company_id = False` → location is **global** (accessible to all companies). The global inter-company transit location `stock.stock_location_inter_company` (xmlid) has `company_id` omitted per `stock_data.xml` line 34.

### 2.5 active
```python
# line 31
active = fields.Boolean('Active', default=True, ...)
```
Archiving cascades to child locations (write method lines 250–260). Cannot archive if warehouse references the location (lines 243–247). Cannot archive if child locations contain stock (lines 252–256).

### 2.6 barcode
```python
# line 79
barcode = fields.Char('Barcode', copy=False)
```
Unique constraint per company (lines 93–96):
```python
_barcode_company_uniq = models.Constraint(
    'unique (barcode,company_id)',
    'The barcode for a location must be unique per company!',
)
```
Included in `_rec_names_search` (line 19) enabling barcode-based scanning lookups.

### 2.7 replenish_location
```python
# line 64–65
replenish_location = fields.Boolean('Replenishments', copy=False, compute="_compute_replenish_location", readonly=False, store=True, ...)
```
`_compute_replenish_location` (lines 180–184): forced to `False` when `usage != 'internal'`. Constraint (lines 186–193) prevents parent/child overlap.

### 2.8 storage_category_id
```python
# line 86
storage_category_id = fields.Many2one('stock.storage.category', string='Storage Category', check_company=True, index='btree_not_null')
```
Used by `_check_can_be_used()` (lines 418–462) for capacity enforcement.

---

## 3. _get_putaway_strategy()

**Lines 297–376**

```python
def _get_putaway_strategy(self, product, quantity=0, package=None, packaging=None, additional_qty=None):
```

**Logic:**
1. Calls `_check_access_putaway()` (line 303) — returns `self` in community.
2. Builds `products` set (line 304–305): context `products` + passed product.
3. Resolves `package_type` from package or packaging (lines 306–311).
4. Walks category hierarchy (lines 313–317) to build `categs` set.
5. Filters `putaway_rule_ids` (lines 319–322): by product, category, package_type.
6. Sorts rules by specificity descending: package_type > product > same categ > any categ (lines 324–328).
7. If `storage_category_id` on any child location, loads current/future qty per location (lines 337–366).
8. Calls `putaway_rules._get_putaway_location(...)` (line 371).
9. **Fallback** (lines 373–375): if no match AND `usage == 'view'` → first child internal location; otherwise → `self`.

---

## 4. should_bypass_reservation()

**Lines 411–413**

```python
def should_bypass_reservation(self):
    self.ensure_one()
    return self.usage in ('supplier', 'customer', 'inventory', 'production')
```

**Returns True for 4 usage types:** supplier, customer, inventory, production.  
**Returns False for:** internal, transit, view.  
`transit` does NOT bypass reservation — transit locations CAN hold reserved stock.

---

## 5. _check_can_be_used()

**Lines 418–462**

Validates whether a product/package fits at a location given its `storage_category_id` constraints:

- `allow_new_product == "empty"`: rejected if location already has any positive quant (line 426).
- `allow_new_product == "same"`: rejected if existing quant is for a different product, or pending move line for a different product (lines 429–440).
- **Weight check** (lines 441–455): forecast weight + incoming weight must not exceed `storage_category_id.max_weight`.
- **Package capacity check** (lines 449–450): `location_qty >= package_capacity.quantity` → False.
- **Product capacity check** (lines 456–460): `quantity + location_qty > product_capacity.quantity` → False.

---

## 6. Scrap Location (v19 Community)

**No `scrap_location` boolean field exists on `stock.location` in v19.**

Scrap locations are identified solely by `usage == 'inventory'`. They are created per-company by `res.company._create_scrap_location()` (res_company.py lines 91–97):

```python
def _create_scrap_location(self):
    for company in self:
        scrap_location = self.env['stock.location'].create({
            'name': 'Scrap',
            'usage': 'inventory',
            'company_id': company.id,
        })
```

`create_missing_scrap_location()` (lines 150–154) searches by `usage == 'inventory'` to detect existing scrap locations.

`_check_scrap_location` constraint (lines 195–199) prevents assigning an `inventory`-type location as destination for MRP operations.

**stock.scrap model** (`stock_scrap.py` line 43): `scrap_location_id` is resolved by searching `usage == 'inventory'` locations per company.

---

## 7. valuation_account_id (stock_account extension)

**File:** `stock_account/models/stock_location.py` lines 11–14

```python
valuation_account_id = fields.Many2one(
    'account.account', 'Stock Valuation Account',
    domain=[('account_type', 'not in', ('asset_receivable', 'liability_payable', 'asset_cash', 'liability_credit_card'))],
    help="Expense account used to re-qualify products removed from stock and sent to this location")
```

- Used in AVCO/FIFO accounting flows when goods move OUT of valued stock to an external (non-valued) location.
- `_should_be_valued()` (lines 36–41): `bool(self.company_id) and self.usage in ['internal', 'transit']` — only company-bound internal and transit locations hold valuation.

---

## 8. _is_outgoing()

**Lines 468–474**

```python
def _is_outgoing(self):
    self.ensure_one()
    if self.usage == 'customer':
        return True
    inter_comp_location = self.env.ref('stock.stock_location_inter_company', raise_if_not_found=False)
    return self._child_of(inter_comp_location)
```

A location is "outgoing" if it is a customer location OR is a child of the inter-company transit location (xmlid `stock.stock_location_inter_company`).

---

## 9. Data — Location XMLIDs (stock_data.xml)

| XMLID | usage | company_id | Notes |
|---|---|---|---|
| `stock.stock_location_suppliers` | supplier | None (global) | Virtual vendor source |
| `stock.stock_location_customers` | customer | None (global) | Virtual customer destination |
| `stock.stock_location_inter_company` | transit | None (global) | Inter-company/inter-warehouse transit |

Scrap locations: created per-company at install time, NO shared xmlid.

---

## 10. Multi-Company Behaviour

- `company_id = False` on a location → shared across all companies.
- `company_id` set → single-company location; `check_company=True` on `location_id` (parent) enforces same-company constraint.
- `write()` (lines 220–225) **prevents changing `company_id`** after creation; must archive and recreate.
- `_should_be_valued()` returns False for locations without `company_id`, so global transit/supplier/customer locations are never valued in stock accounting.

---

## 11. MIGRATION FLAGS

| Flag | Status | Evidence |
|---|---|---|
| `own` usage type | **NOT PRESENT** in v19 | Selection list lines 32–47 — 7 values only |
| `scrap_location` boolean field | **NOT PRESENT** in v19 | No field declaration; scrap identified by `usage='inventory'` |
| `return_location` boolean field | **NOT PRESENT** in v19 community | No field declaration found |
| `pos_location_id` on location | **NOT PRESENT** in v19 community | Not found in stock addon source |
| `transit` usage type | PRESENT | In selection since v16+; retained in v19 |
| `inventory` usage == scrap | CONFIRMED v19 pattern | res_company.py line 95; stock_scrap.py line 43 |
| `child_internal_location_ids` M2M | v19 uses M2M (not O2M) | Field declaration lines 52–58 |
| `replenish_location` field | PRESENT new in v17+ | Still present line 64 |
| `cyclic_inventory_frequency` | PRESENT | Line 81 — triggers next_inventory_date |

---

## 12. complete_name Hierarchy — View-Type Boundary

```
Physical Locations         ← usage=view, complete_name = "Physical Locations" (no parent prefix)
  └─ WH                    ← usage=view, complete_name = "WH" (resets because usage=view)
       └─ Stock             ← usage=internal, complete_name = "WH/Stock"
            └─ Shelf A      ← usage=internal, complete_name = "WH/Stock/Shelf A"
```

View-type locations do NOT inherit parent complete_name; they reset the path. This means view locations used as structural containers are invisible in child location paths.
