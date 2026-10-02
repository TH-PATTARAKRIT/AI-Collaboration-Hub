# U216 — mrp.production: Manufacturing Order Model
## STATE03 VDR Restricted Technical Evidence

**Source file (READ-ONLY):**
`/Volumes/iMacSys/SMEsPlus ENTERPRISE SUITE/02_SOURCE_CODE/SMEsPlus19/SOURCE_CODE/Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp/models/mrp_production.py`
SHA-256 prefix: `da02f2761908`
Total lines: 3215

---

## 1. Model Declaration

- **Line 38–43**: `class MrpProduction(models.Model)` — model `mrp.production`, description "Manufacturing Order"
- **Line 42**: `_date_name = 'date_start'` — calendar date anchor is `date_start`
- **Line 43**: `_inherit = ['mail.thread', 'mail.activity.mixin', 'product.catalog.mixin']`
- **Line 44**: `_order = 'priority desc, date_start asc, id'`

---

## 2. State Machine

### State Field Declaration (lines 177–191)
```python
state = fields.Selection([
    ('draft', 'Draft'),
    ('confirmed', 'Confirmed'),
    ('progress', 'In Progress'),
    ('to_close', 'To Close'),
    ('done', 'Done'),
    ('cancel', 'Cancelled')], string='State',
    compute='_compute_state', copy=False, index=True, readonly=True,
    store=True, tracking=True, ...)
```

### `_compute_state` Method (lines 573–603)
The state is fully computed (not a plain stored field set by direct writes except in limited overrides):

| Condition evaluated (in order) | Resulting state |
|---|---|
| No state OR no product_uom_id OR no id | `draft` |
| state == 'cancel' OR all move_finished_ids are cancelled | `cancel` |
| state == 'done' OR all raw+finished moves in done/cancel | `done` |
| All workorders in done/cancel states | `to_close` |
| No workorders AND qty_producing >= product_qty | `to_close` |
| Any workorder in progress/done OR qty_producing > 0 OR any move_raw picked | `progress` |

Implicit fallback: remains at `confirmed` (set explicitly by `action_confirm` line 1666).

### State Transitions via Action Methods

| Method | From state | To state | Line |
|---|---|---|---|
| `action_confirm()` | draft | confirmed | 1666 |
| `action_start()` | confirmed | progress | 3067–3070 |
| `_compute_state` | progress/confirmed | to_close | 594–597 |
| `button_mark_done()` → write | to_close/progress | done | 2251–2256 |
| `action_cancel()` → `_action_cancel()` | any (not done) | cancel | 1842–1848 |

`action_start()` at line 3067 performs a direct state write `self.state = "progress"` when current state is `confirmed`.

---

## 3. Key Field Declarations

### `product_qty` (line 112–115)
```python
product_qty = fields.Float(
    'Quantity To Produce', digits='Product Unit',
    readonly=False, required=True, tracking=True, precompute=True,
    compute='_compute_product_qty', store=True, copy=True)
```
Computed in draft from BOM's `product_qty`. In confirmed+ state, editable by user.

### `qty_producing` (line 123)
```python
qty_producing = fields.Float(string="Quantity Producing", digits='Product Unit', copy=False)
```
Plain stored float. Records quantity currently being produced. Used in state transitions.

### `qty_produced` (line 239)
```python
qty_produced = fields.Float(compute="_get_produced_qty", string="Quantity Produced")
```
Computed at line 700–704 from finished moves that are `picked`.

### `lot_producing_ids` (lines 120–122) — MIGRATION FLAG
```python
lot_producing_ids = fields.Many2many(
    'stock.lot', string='Lot/Serial Number', copy=False,
    domain="[('product_id', '=', product_id)]", check_company=True)
```
**V19 change**: This is a Many2many (`lot_producing_ids`, plural). Previous versions used a Many2one `lot_producing_id` (singular). Constraint at line 987–991 limits lot-tracked products to 1 lot.

### `move_raw_ids` (lines 203–207)
```python
move_raw_ids = fields.One2many(
    'stock.move', 'raw_material_production_id', 'Components',
    compute='_compute_move_raw_ids', store=True, readonly=False, copy=False,
    domain=[('location_dest_usage', '!=', 'inventory')])
```
Component consumption moves (source → production location).

### `move_finished_ids` (lines 208–211)
```python
move_finished_ids = fields.One2many(
    'stock.move', 'production_id', 'Finished Products', readonly=False,
    compute='_compute_move_finished_ids', store=True, copy=False,
    domain=[('location_dest_usage', '!=', 'inventory')])
```
Finished product moves (production location → destination).

### `workorder_ids` (lines 220–222)
```python
workorder_ids = fields.One2many(
    'mrp.workorder', 'production_id', 'Work Orders', copy=True,
    compute='_compute_workorder_ids', store=True, readonly=False)
```
Linked work orders. Auto-created from BOM operations in draft state (lines 606–660).

### Date Fields (lines 149–156) — MIGRATION FLAG
```python
date_start = fields.Datetime('Start', copy=False, default=_get_default_date_start, ...)
date_finished = fields.Datetime('End', copy=False, default=_get_default_date_finished,
    compute='_compute_date_finished', store=True, ...)
```
`date_start` replaces old `date_planned_start`. `date_finished` replaces old `date_planned_finished`. Both are computed/editable fields in v19.

### `date_deadline` (lines 146–148) — NEW in v19
```python
date_deadline = fields.Datetime('Deadline', copy=False, store=True, readonly=False,
    compute='_compute_date_deadline', ...)
```
Computed from minimum of `move_finished_ids.date_deadline`.

---

## 4. `action_confirm()` — Confirmation Workflow (lines 1625–1667)

1. Calls `_check_company()`
2. For serial-tracked products, normalizes UoM to product's base UoM
3. Calls `move_raws_to_adjust._adjust_procure_method()` (MTO/MTS selection)
4. Calls `moves_to_confirm._action_confirm(merge=False)` for all raw + finished moves
5. Calls `workorder_to_confirm._action_confirm()` and `_set_cost_mode()`
6. Triggers scheduler for raw moves: `self.move_raw_ids._trigger_scheduler()`
7. Line 1666: `self.filtered(lambda mo: mo.state == 'draft').state = 'confirmed'`

No `_action_generate_immediate_transfers()` method found in v19 mrp_production.py. This method name does not exist in this file.

---

## 5. `button_mark_done()` (lines 2219–2339)

Full sequence:
1. Calls `self.pre_button_mark_done()` — runs sanity checks, auto-sets quantities, checks consumption and backorder issues
2. If `mo_ids_to_backorder` context: `productions_to_backorder._split_productions()` splits the MO
3. Calls `self.workorder_ids.button_finish()`
4. Calls `_post_inventory(cancel_backorder=True)` for both sets
5. Triggers assignment on done finished moves
6. Line 2251–2256: Writes `state='done'`, `date_finished=now()`, `priority='0'`, `is_locked=True`

### `pre_button_mark_done()` (lines 2341–2390)

Calls `_get_consumption_issues()` (line 2368) — if issues exist, launches consumption wizard.
Calls `_get_quantity_produced_issues()` (line 2372) — if `qty_producing < product_qty`, checks `picking_type_id.create_backorder` setting:
- `'always'`: backordering is automatic via context
- `'ask'`: launches `_action_generate_backorder_wizard()`

---

## 6. Backorder Mechanism (lines 1820–1840, 1967–2214)

### `_get_quantity_to_backorder()` (lines 2772–2774)
```python
def _get_quantity_to_backorder(self):
    self.ensure_one()
    return max(self.product_qty - self.qty_producing, 0)
```
Returns remaining quantity to backorder.

### `_get_quantity_produced_issues()` (lines 1820–1827)
Loops over orders; if `_get_quantity_to_backorder() > 0`, appends to issues list.

### `_split_productions()` (lines 1981–2214)
Main backorder creation method:
- Accepts `amounts` dict, `cancel_remaining_qty`, `set_consumed_qty` params
- Renames current production with backorder suffix (e.g., `WH/MO/00001-001`)
- Creates new `mrp.production` records via `self.env['mrp.production'].create(backorder_vals_list)`
- Splits `stock.move` records proportionally between original and backorders
- Splits `stock.move.line` reservations
- Calls `backorders._action_confirm_mo_backorders()` to confirm new workorders

### `_get_backorder_mo_vals()` (lines 1967–1979)
Returns vals for backorder: same `production_group_id`, `reference_ids`, clears `lot_producing_ids`, sets `state='confirmed'`.

---

## 7. `_post_inventory()` — Stock Posting (lines 1907–1955)

1. Loops over `move_raw_ids` — moves with `picked=True` go to `moves_to_do`; unpicked go to `moves_to_cancel`
2. Calls `moves_to_do._action_done(cancel_backorder=cancel_backorder)`
3. For each order's finish moves: sets `lot_ids = order.lot_producing_ids.ids` (line 1930)
4. Sets `move.quantity` from `qty_producing - qty_produced` (line 1935)
5. Calls `moves_to_finish._action_done()` (line 1951)
6. Links consume move lines to finished move lines (line 1954)

---

## 8. Work Orders Auto-Creation (lines 606–660)

`_compute_workorder_ids()` runs in draft state. Logic:
- If BOM has `operation_ids`, creates one workorder per operation
- Each workorder gets: `name`, `production_id`, `workcenter_id`, `operation_id`, `state='ready'`
- Existing workorders for the same operation are updated, not duplicated
- `_compute_workorder_ids` is triggered by changes to `bom_id`, `product_id`, `product_qty`, `product_uom_id`

### Workorder linking in `_link_workorders_and_moves()` (lines 1669–1701)
- If BOM `allow_operation_dependencies`: builds dependency graph from `operation.blocked_by_operation_ids`
- Otherwise: chains workorders sequentially by sequence+id
- Links raw/finished moves to their workorder via `move.workorder_id`

---

## 9. Analytic Fields — MIGRATION FLAG

**No `analytic_account_id` field found in v19 `mrp.production`.** Search returned zero results for `analytic` in the entire file. The `analytic_account_id` field present in older Odoo versions (14/15/16) has been removed from `mrp.production` in v19 Community. Any analytic distribution is handled externally (e.g., via `account_analytic` extension or not at all in Community).

---

## 10. `availability` Field — MIGRATION FLAG

**The old `availability` field (Selection: none/assigned/partially_available/waiting) is NOT present in v19.** It has been replaced by:
- `reservation_state` (line 192–201): Selection `confirmed/assigned/waiting`
- `components_availability` (line 274): Char field with human-readable status
- `components_availability_state` (line 277): Selection `available/expected/late/unavailable`

---

## 11. `production_group_id` (line 94)

New in v19: `production_group_id = fields.Many2one('mrp.production.group', ...)`. The `mrp.production.group` model (lines 24–35) tracks backorder families via `production_ids` and parent/child `Many2many` relations. Backorder count computed from `production_group_id.production_ids` (line 328).

---

## 12. `_compute_move_raw_ids` (lines 819–843)

Only runs in draft state (`if production.state != 'draft': continue`). Calls `_get_moves_raw_values()` which explodes the BOM via `production.bom_id.explode(...)`. Skips phantom BOM lines and non-consumable products (`product_id.type != 'consu'`).

---

## 13. Consumption Enforcement (lines 1761–1818)

`_get_consumption_issues()` compares actual consumed qty vs. expected qty (from BOM explosion scaled by `qty_producing / product_qty`). Returns list of `(order, product_id, consumed_qty, expected_qty)` tuples. Behavior controlled by `consumption` field (flexible/warning/strict). If `consumption == 'flexible'` or no BOM: no check.
