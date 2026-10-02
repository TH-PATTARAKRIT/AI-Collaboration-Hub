# U209 — stock.scrap: Scrap Order Model, Valuation Impact, Accounting Entry Creation
**Unit**: U209  
**Module**: stock (stock_scrap.py), stock_account (stock_move.py), mrp (stock_scrap.py)  
**Source SHA** (file hash, no git): `6c4dce9644e0bd2e0d891b7a6bfedc8e7b968c57`  
**Odoo version**: 19.0.post20260921  
**Restricted-evidence level**: L0–L3  

---

## 1. Model Definition

**File**: `odoo/addons/stock/models/stock_scrap.py`  
**Class**: `StockScrap` (`stock.scrap`)  
**Line 10–59**

```
_name = 'stock.scrap'
_inherit = ['mail.thread']
_order = 'id desc'
```

### 1.1 Core Fields (stock addon)

| Field | Type | Line | Notes |
|---|---|---|---|
| `name` | Char | 16 | Sequence reference, default='New', copy=False |
| `company_id` | Many2one(res.company) | 19 | Required, `default=lambda self: self.env.company` |
| `origin` | Char | 20 | Source Document (free text) |
| `product_id` | Many2one(product.product) | 21–23 | domain `[('type','=','consu')]`, required, check_company |
| `allowed_uom_ids` | Many2many(uom.uom) | 24 | computed |
| `product_uom_id` | Many2one(uom.uom) | 25–28 | computed from product, store=True, precompute=True |
| `tracking` | Selection | 29 | related to product_id.tracking |
| `lot_id` | Many2one(stock.lot) | 30–32 | domain filters by product_id, check_company |
| `package_id` | Many2one(stock.package) | 33–35 | check_company |
| `owner_id` | Many2one(res.partner) | 36 | check_company |
| `move_ids` | One2many(stock.move, 'scrap_id') | 37 | **v19: One2many, NOT Many2one** |
| `picking_id` | Many2one(stock.picking) | 38 | check_company |
| `location_id` | Many2one(stock.location) | 39–42 | domain `usage='internal'`, computed, store, precompute |
| `scrap_location_id` | Many2one(stock.location) | 43–46 | domain `usage='inventory'`, computed, store, precompute |
| `scrap_qty` | Float | 47–49 | digits='Product Unit', computed from move_ids, default=1.0 |
| `state` | Selection | 50–53 | `[('draft','Draft'),('done','Done')]`, default='draft' |
| `date_done` | Datetime | 54 | set in `do_scrap()` |
| `should_replenish` | Boolean | 55 | NEW in v19: triggers `stock.rule.run` replenishment |
| `scrap_reason_tag_ids` | Many2many(stock.scrap.reason.tag) | 56–59 | NEW in v19: reason tagging |

### 1.2 MRP Extension Fields (mrp addon)

**File**: `odoo/addons/mrp/models/stock_scrap.py`  
**Class**: `StockScrap(_inherit='stock.scrap')`, lines 7–113

| Field | Type | Line | Notes |
|---|---|---|---|
| `production_id` | Many2one(mrp.production) | 10–13 | Manufacturing Order link, index='btree_not_null' |
| `workorder_id` | Many2one(mrp.workorder) | 14–17 | Work Order link, informative only |
| `product_is_kit` | Boolean | 18 | related to product_id.is_kits |
| `product_template` | Many2one | 19 | related to product_id.product_tmpl_id |
| `bom_id` | Many2one(mrp.bom) | 20–23 | Kit BoM link, phantom type only |

---

## 2. Scrap Account Resolution

**There is NO `_get_scrap_account()` method in v19 community.**

The scrap expense account is resolved indirectly via:

1. `scrap_location_id.valuation_account_id` — field added by `stock_account` to `stock.location` at `/addons/stock_account/models/stock_location.py:11–14`
2. This field is typed as `Many2one('account.account')` with help text: *"Expense account used to re-qualify products removed from stock and sent to this location"*
3. The stock valuation account is resolved in `product._get_product_accounts()['stock_valuation']` at `/addons/stock_account/models/product.py:130–140`: priority is `categ_id.property_stock_valuation_account_id` then company fallback `account_stock_valuation_id`.

---

## 3. `action_validate()` Flow

**File**: `odoo/addons/stock/models/stock_scrap.py:211–234`

```python
def action_validate(self):
    self.ensure_one()
    if self.product_uom_id.is_zero(self.scrap_qty):
        raise UserError(_('You can only enter positive quantities.'))
    if self.check_available_qty():
        return self.do_scrap()
    else:
        # Returns wizard: stock.warn.insufficient.qty.scrap
        ...
```

**`check_available_qty()` at line 196–209**: uses `_should_check_available_qty()` (True for storable products, line 194). Checks `product_id.qty_available` at the source `location_id` with filters for lot/package/owner.

**`do_scrap()` at line 152–163**:

```python
def do_scrap(self):
    self._check_company()
    for scrap in self:
        scrap.name = self.env['ir.sequence'].next_by_code('stock.scrap') or _('New')
        move = scrap._create_scrap_move()
        move.with_context(is_scrap=True)._action_done()
        scrap.write({'state': 'done'})
        scrap.date_done = fields.Datetime.now()
        if scrap.should_replenish:
            scrap.do_replenish()
    return True
```

Key: `move.with_context(is_scrap=True)._action_done()` — the `is_scrap=True` context flag suppresses backorder creation at `stock_move.py:2307`.

---

## 4. `_prepare_move_values()` and Move Creation

**File**: `odoo/addons/stock/models/stock_scrap.py:125–150`

```python
def _prepare_move_values(self):
    self.ensure_one()
    return {
        'origin': self.origin or self.picking_id.name or self.name,
        'company_id': self.company_id.id,
        'product_id': self.product_id.id,
        'product_uom': self.product_uom_id.id,
        'state': 'draft',
        'product_uom_qty': self.scrap_qty,
        'location_id': self.location_id.id,
        'scrap_id': self.id,
        'location_dest_id': self.scrap_location_id.id,
        'move_line_ids': [(0, 0, {
            'product_id': self.product_id.id,
            'product_uom_id': self.product_uom_id.id,
            'quantity': self.scrap_qty,
            'location_id': self.location_id.id,
            'location_dest_id': self.scrap_location_id.id,
            'package_id': self.package_id.id,
            'owner_id': self.owner_id.id,
            'lot_id': self.lot_id.id,
        })],
        'picked': True,
        'picking_id': self.picking_id.id
    }
```

Note: `picked=True` is set at creation time. The move is created via `_create_scrap_move()` at line 165–167.

**MRP override** at `mrp/models/stock_scrap.py:43–51` adds `production_id` or `raw_material_production_id` based on whether the scrapped product is a finished or raw material.

---

## 5. Valuation — No SVL in v19

**Critical v19 migration flag**: `stock.valuation.layer` (SVL) model was present in v16/v17 but does NOT exist in v19 community. Valuation is stored directly as `value` field on `stock.move` (added by stock_account at `/addons/stock_account/models/stock_move.py:24–26`).

### 5.1 `_set_value()` — Outgoing Valuation

**File**: `odoo/addons/stock_account/models/stock_move.py:292–358`

Called from `_action_done()` at line 182 for outgoing moves:

- **AVCO/Standard**: `move.value = move.product_id.standard_price * move._get_valued_qty()` (line 351)
- **FIFO**: `move.value = move.product_id._run_fifo(valued_qty)` (line 348) — pops FIFO layers
- **Lot-valuated**: `move.value = sum(ml.lot_id.standard_price * ml.quantity_product_uom ...)` (lines 338–343)

A scrap move is classified as outgoing (`_is_out()` = True) because:
- Source: `location_id.usage='internal'` → `_should_be_valued()` = True
- Destination: `scrap_location_id.usage='inventory'` → `_should_be_valued()` = False

(`_should_be_valued()` at `/addons/stock_account/models/stock_location.py:36–41`: only True for `usage in ['internal','transit']` with a company_id)

### 5.2 Accounting Entry Creation

**File**: `odoo/addons/stock_account/models/stock_move.py:193–217`

`_create_account_move()` is called from `_action_done()` at line 187.

Gate: `_should_create_account_move()` at line 659–667:
```python
return self.product_id.is_storable and self.is_valued
    and (self.location_dest_id.valuation_account_id or self.location_id.valuation_account_id)
    and not float_is_zero(self.quantity, ...)
    and self.product_id.valuation == 'real_time'
```

**For scrap**: `location_dest_id.valuation_account_id` (scrap location) must be set. Without it, NO accounting entry is created.

`_get_account_move_line_vals()` at line 229–248:
```python
# location_id (source/internal) has NO valuation_account_id
# => else branch:
debit_acc = self.location_dest_id.valuation_account_id  # scrap loss account
credit_acc = self.product_id._get_product_accounts()['stock_valuation']  # stock valuation account

# Journal entry:
# CR Stock Valuation Account  (value)
# DR Scrap Loss Account       (value)
```

This is confirmed by test `test_scrap_valuation_from_done_picking` at `stock_account/tests/test_stockvaluation.py:2843–2846`:
```python
self.assertRecordValues(scrap.move_ids.account_move_id.line_ids, [
    {'account_id': accounts_data['stock_valuation'].id, 'debit': 0.0, 'credit': 20.0},
    {'account_id': self.account_stock_variation.id, 'debit': 20.0, 'credit': 0.0},
])
```

Journal is `company_id.account_stock_journal_id` (line 212).

---

## 6. `_get_responsible_for_safety_stock()` on Scrap

**Not present**. No method with this name exists on `stock.scrap` in v19 community. Not in `stock_scrap.py`, not in `mrp/models/stock_scrap.py`.

---

## 7. MRP Integration — `production_id`

- `production_id` Many2one(mrp.production) added at `mrp/models/stock_scrap.py:10`
- `_compute_location_id()` overridden at line 25: sets `location_id` from `production_id.location_src_id` or `production_id.location_dest_id` based on state
- `_prepare_move_values()` override at line 43–51: sets `production_id` or `raw_material_production_id` on the created `stock.move` based on whether product is finished good or raw material
- `do_scrap()` override at line 108–112: unpicks raw material move lines with matching lot before calling super

---

## 8. Multi-Company

- `company_id` on scrap (line 19): required, default = `self.env.company`
- `location_id` computed by filtering warehouses per company (line 72–86)
- `scrap_location_id` computed by filtering inventory locations per company (line 88–98)
- All relational fields use `check_company=True` (lot_id, package_id, owner_id, picking_id, production_id, workorder_id)
- `_check_company()` called in `do_scrap()` line 153

---

## 9. Migration Flags (v19 vs v16/v17)

| Flag | Description | Evidence |
|---|---|---|
| **BREAKING: move_id → move_ids** | In v16/v17 `stock.scrap` had `move_id` (Many2one). v19 uses `move_ids` (One2many, scrap_id on stock.move). All code accessing `scrap.move_id` must be updated to `scrap.move_ids[0]` or similar. | `stock_scrap.py:37`, `stock_move.py:139` |
| **BREAKING: SVL removed** | `stock.valuation.layer` model absent in v19. Valuation stored as `value` on `stock.move`. Any custom code writing/reading SVL breaks. | `stock_account/models/stock_move.py:24–26` |
| **NEW: should_replenish** | New field: automatic replenishment trigger after scrap. Not in v16/v17. | `stock_scrap.py:55` |
| **NEW: scrap_reason_tag_ids** | New field: M2M to `stock.scrap.reason.tag` model (new in v19). | `stock_scrap.py:56–59` |
| **CHANGE: product domain** | v19 uses `[('type','=','consu')]` on product_id. In v19, `type='consu'` covers all consumables; `is_storable` is a separate boolean on the product template determining inventory tracking. | `stock_scrap.py:22` |
| **NEW: account entry condition** | Accounting entry requires `valuation_account_id` on scrap location (set manually). No entry created without it. This replaces v16/v17 SVL-based automatic entry creation. | `stock_account/models/stock_move.py:659–667` |
| **date_done: present** | `date_done` field still present in v19 at line 54. | `stock_scrap.py:54` |
| **origin: present** | `origin` field still present in v19 at line 20. | `stock_scrap.py:20` |
| **No undo/return** | No `action_undo_scrap` or return mechanism in v19 community stock. Done scraps cannot be deleted (`_unlink_except_done`). | `stock_scrap.py:120–123` |

---

## 10. Return from Scrap

**No undo or return mechanism exists** for `stock.scrap` in v19 community. Once `state='done'`:
- `_unlink_except_done()` at line 120 prevents deletion
- No `action_revert_scrap` or `_reverse_scrap` method found
- The only way to reverse a scrap is to create a manual stock adjustment or a new inventory move

---

## Source Pointers Summary

| Item | File | Line(s) |
|---|---|---|
| StockScrap model class | `stock/models/stock_scrap.py` | 10–250 |
| `action_validate()` | `stock/models/stock_scrap.py` | 211–234 |
| `do_scrap()` | `stock/models/stock_scrap.py` | 152–163 |
| `_prepare_move_values()` | `stock/models/stock_scrap.py` | 125–150 |
| `_create_scrap_move()` | `stock/models/stock_scrap.py` | 165–167 |
| `_should_create_account_move()` | `stock_account/models/stock_move.py` | 659–667 |
| `_get_account_move_line_vals()` | `stock_account/models/stock_move.py` | 229–248 |
| `_create_account_move()` | `stock_account/models/stock_move.py` | 193–218 |
| `_set_value()` | `stock_account/models/stock_move.py` | 292–358 |
| `_should_be_valued()` | `stock_account/models/stock_location.py` | 36–41 |
| `valuation_account_id` on location | `stock_account/models/stock_location.py` | 11–14 |
| `_get_product_accounts()` | `stock_account/models/product.py` | 130–140 |
| MRP `production_id` extension | `mrp/models/stock_scrap.py` | 7–113 |
| `is_scrap` context suppresses backorder | `stock/models/stock_move.py` | 2305–2308 |
| `scrap_id` on stock.move | `stock/models/stock_move.py` | 139 |
