# U219 — stock.move.line: Detailed Move Line Model, Lot Tracking, Package Handling, Done Quantities

**Source**: `odoo/addons/stock/models/stock_move_line.py`
**SHA256**: `bdab636fdc5ef1377242ec66c25a3a48a1aafcbd2da3859f5a55ba838733cf88`
**Lines**: 1244
**Odoo version**: 19.0.post20260921 (Community)
**Research date**: 2026-10-02

---

## 1. Model Declaration

**File**: `stock/models/stock_move_line.py:15-19`

```python
class StockMoveLine(models.Model):
    _name = 'stock.move.line'
    _description = "Product Moves (Stock Move Line)"
    _rec_name = "product_id"
    _order = "result_package_id desc, id"
```

The default sort order prioritises lines with a `result_package_id` (descending), then by `id`.

---

## 2. Key Fields

### 2.1 Relational Identity Fields

| Field | Type | Pointer | Notes |
|---|---|---|---|
| `picking_id` | Many2one `stock.picking` | line 21-25 | `bypass_search_access=True`; `index=True` |
| `move_id` | Many2one `stock.move` | line 26-28 | `index=True` |
| `company_id` | Many2one `res.company` | line 29 | `readonly=True`, `required=True`, `index=True` |
| `product_id` | Many2one `product.product` | line 30 | `ondelete="cascade"`; domain excludes service products |

### 2.2 Quantity Fields

**File**: `stock/models/stock_move_line.py:37-42`

```python
quantity = fields.Float(
    'Quantity', digits='Product Unit', copy=False, store=True,
    compute='_compute_quantity', readonly=False)
quantity_product_uom = fields.Float(
    'Quantity in Product UoM', digits='Product Unit',
    copy=False, compute='_compute_quantity_product_uom', store=True)
```

- `quantity`: The done/reserved quantity in `product_uom_id`. This is the single quantity field on a move line in v16+. In Odoo 15 and earlier this was split into `qty_done` (done quantity) and `product_uom_qty` / `reserved_uom_qty` (reserved quantity). Both were merged into `quantity` in Odoo 16.
- `quantity_product_uom`: Stored computed — quantity converted to the product's base UoM. Line 167-170: computed via `product_uom_id._compute_quantity(quantity, product_id.uom_id)`.

**MIGRATION FLAG**: `qty_done` does not exist in Odoo 19. Any external code or migration script referencing `qty_done` on `stock.move.line` must use `quantity` instead. `product_uom_qty` on the move LINE (formerly reserved qty) is also gone; use `quantity` or `quantity_product_uom`.

### 2.3 Lot/Serial Number Fields

**File**: `stock/models/stock_move_line.py:48-51`

```python
lot_id = fields.Many2one(
    'stock.lot', 'Lot/Serial Number',
    domain="[('product_id', '=', product_id)]", check_company=True, index=True)
lot_name = fields.Char('Lot/Serial Number Name')
```

- `lot_id`: Reference to an existing `stock.lot` record.
- `lot_name`: Free-text name used when the picking type has `use_create_lots=True`. During `_action_done` the system searches for an existing lot with this name; if not found, a new `stock.lot` is created and written back to `lot_id`.

### 2.4 Package Fields

**File**: `stock/models/stock_move_line.py:44-56`

```python
package_id = fields.Many2one(
    'stock.package', 'Source Package', ondelete='restrict',
    check_company=True,
    domain="[('location_id', '=', location_id)]")
result_package_id = fields.Many2one(
    'stock.package', 'Destination Package',
    ondelete='restrict', required=False, check_company=True,
    domain="['|', '|', ('location_id', '=', location_dest_id), ...]",
    help="If set, the operations are packed into this package")
```

- `package_id`: The package products are taken FROM. Domain restricts to packages at `location_id`.
- `result_package_id`: The package products are placed INTO at the destination. Used by putaway logic and quant updates.

### 2.5 Location Fields

**File**: `stock/models/stock_move_line.py:68-72`

```python
location_id = fields.Many2one(
    'stock.location', 'From', ...,
    compute="_compute_location_id", store=True, readonly=False, precompute=True, index=True)
location_dest_id = fields.Many2one('stock.location', 'To', ...,
    compute="_compute_location_id", store=True, index=True, readonly=False, precompute=True)
```

Both are precomputed from `move_id.location_id` / `move_id.location_dest_id` via `_compute_location_id` (lines 136-142). Override allowed (readonly=False).

### 2.6 State, Date, Owner, Picked

**File**: `stock/models/stock_move_line.py:60-67, 83`

```python
date = fields.Datetime(
    'Date', default=fields.Datetime.now, required=True,
    help="Creation date of this move line until updated due to: quantity being increased, 'picked' status has updated, or move line is done.")
owner_id = fields.Many2one(
    'res.partner', 'From Owner',
    check_company=True, index='btree_not_null',
    help="When validating the transfer, the products will be taken from this owner.")
state = fields.Selection(related='move_id.state', store=True)
picked = fields.Boolean('Picked', compute='_compute_picked', store=True, readonly=False, copy=False)
```

- `state`: Related (stored) from parent `move_id.state` — no independent state on the line.
- `date`: Set at creation (default `now`); updated by `write` (line 529) when quantity increases on a picked line; set to `fields.Datetime.now()` in `_action_done` (line 713) after quant moves complete.
- `owner_id`: Partner who owns the inventory. Passed to all `_update_reserved_quantity` / `_update_available_quantity` calls.
- `picked`: Computed (stored) from `move_id.state == 'done'` or context `auto_pick_move_lines`; writable.

---

## 3. quantity vs reserved_qty: Naming History and Current Reality

In Odoo 19 the move line has a single `quantity` field. The parent `stock.move` still has `product_uom_qty` (the demand/ordered quantity). The relationship:

```
stock.move.product_uom_qty   = ordered/demand quantity
stock.move.quantity          = sum of done quantities across move lines (when done)
stock.move.line.quantity     = done (or reserved) quantity for this specific line
stock.move.line.quantity_product_uom = quantity in product's base UoM (stored computed)
```

The comment at line 463 still uses the internal term `reserved_uom_qty` describing the logical concept, but this refers to the `quantity` field:

> "the sum of the move lines `reserved_uom_qty` should always be equal to the sum of `reserved_quantity` on the quants"

**MIGRATION FLAG**: Any SQL or ORM code referencing `stock_move_line.qty_done` or `stock_move_line.product_uom_qty` (as the RESERVED quantity, not the parent move's demand) must migrate to `quantity`. The term `reserved_uom_qty` was used in intermediate Odoo 16 releases; it is `quantity` in v17+.

---

## 4. lot_name vs lot_id — Auto-Creation Logic

**File**: `stock/models/stock_move_line.py:649-676`

In `_action_done`:

1. For tracked products with `use_create_lots=True`, move lines with `lot_name` but no `lot_id` are collected into `ml_ids_to_check`.
2. A batch search for existing lots by `lot_name` is done (lines 651-655).
3. If found: `lot_id` set to existing lot (line 660).
4. If not found but `lot_name` set: added to `ml_ids_to_create_lot` (line 662).
5. If no `lot_name`: added to `ml_ids_tracked_without_lot` → raises `UserError` (lines 666-673).
6. `_create_and_assign_production_lot()` (lines 756-773): Creates `stock.lot` records in batch from `_prepare_new_lot_vals()` (which uses `lot_name` and `product_id`), then writes `lot_id` back.

**Key**: `lot_name` is a temporary staging field; after `_action_done`, the permanent reference is always `lot_id`.

---

## 5. Package Tracking: package_id vs result_package_id and Putaway

### 5.1 Source vs Destination Package

- `package_id` (source) — which package the products are taken from (restricted to `location_id`).
- `result_package_id` (destination) — which package products end up in at `location_dest_id`.

### 5.2 Putaway Integration

**File**: `stock/models/stock_move_line.py:253-260`

`_onchange_putaway_location` is triggered on `result_package_id`, `product_id`, `product_uom_id`, `quantity`. If multi-locations is enabled and product has quantity, the destination location is resolved via `_get_putaway_strategy(product_id, quantity=quantity, package=result_package_id)`.

**File**: `stock/models/stock_move_line.py:262-293`

`_apply_putaway_strategy`: Groups move lines by `result_package_id.outermost_package_id`. If package has a `package_type_id`, applies a single putaway for the whole package. Otherwise applies per-product putaway, enforcing single-location constraint within a package.

### 5.3 Quant Update with result_package_id

**File**: `stock/models/stock_move_line.py:699-700`

```python
available_qty, in_date = ml._synchronize_quant(-ml.quantity_product_uom, ml.location_id)
ml._synchronize_quant(ml.quantity_product_uom, ml.location_dest_id, package=ml.result_package_id, in_date=in_date)
```

The destination quant is credited with `result_package_id`, so quant tracking uses the destination package, not the source package.

### 5.4 Package History

**File**: `stock/models/stock_move_line.py:691-694, 983-1001`

Before quant moves, `_prepare_package_history_vals()` creates `stock.package.history` records capturing pre-move location and destination for all `result_package_id` packages.

---

## 6. _action_done() — Full Flow

**File**: `stock/models/stock_move_line.py:595-714`

Step-by-step:

1. **Validation loop** (lines 615-647): Check rounding precision, collect tracked-without-lot lines.
2. **Lot resolution** (lines 649-676): Resolve `lot_name` → `lot_id`; collect new lot creation requests.
3. **Lot creation** (line 676): `_create_and_assign_production_lot()` — batch creates `stock.lot`, writes `lot_id`.
4. **Zero-quantity delete** (lines 678-679): Unlinks move lines with `quantity == 0` (unless inventory adjustment).
5. **Package history** (lines 691-694): Creates `stock.package.history` snapshot records.
6. **Quant move loop** (lines 696-706):
   - Unreserve: `_synchronize_quant(-qty, location_id, action="reserved")`
   - Deduct source: `_synchronize_quant(-qty, location_id)` → returns `available_qty, in_date`
   - Credit dest: `_synchronize_quant(qty, location_dest_id, package=result_package_id, in_date=in_date)`
   - If `available_qty < 0`: calls `_free_reservation` to steal reserved qty from other move lines.
7. **Package dest apply** (line 709): `result_package_id._apply_dest_to_package()`
8. **Date stamp** (lines 712-714): `mls_todo.write({'date': fields.Datetime.now()})`

**Note**: SVL (stock valuation layer) creation is NOT triggered inside `_action_done` on move lines. The valuation entries are created in `stock.move._action_done()` which calls `_create_account_move_line()` or similar via `stock_account` module (Enterprise or stock_account addon), not visible in Community `stock_move_line.py`.

---

## 7. _get_aggregated_product_quantities() — Reporting Aggregation

**File**: `stock/models/stock_move_line.py:885-977`

Returns a dict where each key combines `product_id + display_name + description + uom.id + packaging_uom.id` (and `result_package_id.id` if present). Each value contains:
- `quantity`: done quantity in UoM
- `qty_ordered`: from `move_id.product_uom_qty`, adjusted for backorders and other move lines
- `packaging_quantity` / `packaging_qty_ordered`: in packaging UoM
- `product`, `name`, `description`, `product_uom`, `packaging_uom_id`, `move`

Also processes empty moves (cancelled or confirmed with no lines) to include unshipped quantities.

Ignores lots/serial numbers by design (comment line 892): "This function purposely ignores lots/SNs because these are expected to already be properly grouped by line."

---

## 8. owner_id — Inventory Owner Tracking

**File**: `stock/models/stock_move_line.py:64-67`

```python
owner_id = fields.Many2one(
    'res.partner', 'From Owner',
    check_company=True, index='btree_not_null',
    help="When validating the transfer, the products will be taken from this owner.")
```

Passed as `owner_id` parameter in:
- `_update_reserved_quantity` during `create` (line 400)
- `_synchronize_quant` → `_update_available_quantity` with `owner_id=owner` (lines 725-727)
- `_free_reservation` domain filter (line 817)
- `_copy_quant_info` (line 1028): copied from source quant when `quant_id` is set

Enables third-party logistics scenarios where stock is owned by a partner different from the company.

---

## 9. reference Field and stock.reference Model

**File**: `stock/models/stock_move_line.py:89`

```python
reference = fields.Char(related='move_id.reference')
```

The move line itself only has a `reference` (Char, related) — it derives from `move_id.reference`.

**File**: `stock/models/stock_reference.py:4-15`

`stock.reference` model (new in Odoo 16+) replaces the `procurement.group` reference on moves. `stock.move` has `reference_ids` (Many2many to `stock.reference`). The move line does NOT have `reference_ids` — only the parent move does.

**MIGRATION FLAG**: In Odoo 15 and earlier, `stock.move` had `group_id` (Many2one to `procurement.group`). In v16+, this became `reference_ids` (Many2many to `stock.reference`). Move lines only ever had a derived `reference` Char field, never a direct relational link to procurement groups. Any migration referencing `move_line.group_id` or `move_line.procurement_group_id` must be removed.

---

## 10. Index Definitions

**File**: `stock/models/stock_move_line.py:97-98`

```python
_free_reservation_index = models.Index("""(id, company_id, product_id, lot_id, location_id, owner_id, package_id)
    WHERE (state IS NULL OR state NOT IN ('cancel', 'done')) AND quantity_product_uom > 0 AND picked IS NOT TRUE""")
```

Partial index for `_free_reservation` queries — covers non-done, non-cancelled lines with positive reserved qty that are not yet picked.

---

## 11. picked Field and Date Update Logic

**File**: `stock/models/stock_move_line.py:43, 516-529`

`picked` is a stored Boolean computed from `move_id.state == 'done'` or context `auto_pick_move_lines`. It is writable.

The `write` method auto-updates `date` to `now()` without requiring explicit `date` in the write vals when:
- `picked` transitions from False → True, OR
- `quantity` increases on a line that is already picked

**File**: `stock/models/stock_move_line.py:515-529`

```python
if 'date' not in vals and ('product_uom_id' in vals or 'quantity' in vals or vals.get('picked', False)):
    updated_ml_ids = set()
    for ml in self:
        if ml.state in ['draft', 'cancel', 'done']:
            continue
        if vals.get('picked', False) and not ml.picked:
            updated_ml_ids.add(ml.id)
            continue
        if ('quantity' in vals or 'product_uom_id' in vals) and ml.picked:
            ...
            if ml.product_uom_id.compare(old_qty, new_qty) < 0:
                updated_ml_ids.add(ml.id)
    self.env['stock.move.line'].browse(updated_ml_ids).date = fields.Datetime.now()
```

---

## 12. Summary of MIGRATION FLAGS

| Flag | Old (≤v15) | New (v19) | Pointer |
|---|---|---|---|
| Done quantity field | `qty_done` | `quantity` | line 37 |
| Reserved quantity on move line | `product_uom_qty` / `reserved_uom_qty` | `quantity` | line 37 |
| Quantity in base UoM | computed via `qty_done * factor` | `quantity_product_uom` (stored computed) | line 40 |
| Lot/serial number | `lot_id` + `lot_name` | same (unchanged) | lines 48-51 |
| Procurement group reference | `group_id` (on move) | `reference_ids` Many2many `stock.reference` (on move only) | stock_reference.py:9 |
| Move line group reference | N/A | `reference` Char (related) | line 89 |
| Package history | not recorded | `package_history_id` Many2one `stock.package.history` | line 58 |
