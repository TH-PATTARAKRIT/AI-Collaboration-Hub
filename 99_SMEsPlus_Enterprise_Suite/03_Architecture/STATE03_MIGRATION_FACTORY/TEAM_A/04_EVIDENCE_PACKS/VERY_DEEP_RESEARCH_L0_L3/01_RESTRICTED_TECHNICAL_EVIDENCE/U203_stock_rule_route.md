# U203 — stock.rule and stock.route: Route Propagation, Push Rules, _push_apply Chain
**Classification:** RESTRICTED TECHNICAL EVIDENCE  
**Unit:** U203  
**Module:** stock (Community)  
**Source tree:** odoo-19.0.post20260921  
**Date:** 2026-10-02  

---

## 1. stock.rule Model — Fields Inventory

**File:** `odoo/addons/stock/models/stock_rule.py`

| Field | Type | Line | Notes |
|---|---|---|---|
| `action` | Selection('pull','push','pull_push') | 63-65 | Default='pull'; required; index=True |
| `picking_type_id` | Many2one('stock.picking.type') | 87-91 | required; check_company; domain from `picking_type_code_domain` |
| `location_dest_id` | Many2one('stock.location') | 70 | required; check_company; index=True |
| `location_src_id` | Many2one('stock.location') | 71 | optional; check_company; index=True |
| `location_dest_from_rule` | Boolean | 72-75 | NEW v19: when True, dest location on move comes from rule not picking type |
| `route_id` | Many2one('stock.route') | 76 | required; ondelete='cascade'; index=True |
| `route_sequence` | Integer | 86 | related='route_id.sequence'; stored; used for sort ordering |
| `procure_method` | Selection | 78-85 | 'make_to_stock', 'make_to_order', 'mts_else_mto' |
| `auto` | Selection('manual','transparent') | 104-109 | Controls push behaviour: manual=new move, transparent=overwrite dest |
| `push_domain` | Char | 111 | Optional domain filter; push only applies when move matches this domain |
| `propagate_cancel` | Boolean | 97-99 | Default=False on rule; copies to move |
| `propagate_carrier` | Boolean | 100-102 | Default=False; propagates carrier on delivery rules |
| `delay` | Integer | 92 | Lead time days added to move date |
| `warehouse_id` | Many2one('stock.warehouse') | 103 | check_company; index=True |
| `sequence` | Integer | 66 | Default=20; used with route_sequence for ordering |

---

## 2. stock.route Model — Fields Inventory

**File:** `odoo/addons/stock/models/stock_location.py` lines 517-595

| Field | Type | Line | Notes |
|---|---|---|---|
| `name` | Char | 523 | required; translate=True |
| `sequence` | Integer | 525 | Default=0; controls route priority |
| `rule_ids` | One2many('stock.rule','route_id') | 526 | copy=True |
| `supplied_wh_id` | Many2one('stock.warehouse') | 531 | Supplied (destination) warehouse for resupply |
| `supplier_wh_id` | Many2one('stock.warehouse') | 532 | Supplying (source) warehouse for resupply |
| `product_ids` | Many2many('product.template') | 537-539 | M2M via stock_route_product table |
| `categ_ids` | Many2many('product.category') | 540 | M2M via stock_route_categ table |
| `warehouse_ids` | Many2many('stock.warehouse') | 542-544 | M2M via stock_route_warehouse table |
| `product_selectable` | Boolean | 527 | Default=True; show on product inventory tab |
| `product_categ_selectable` | Boolean | 528 | Show on product category |
| `warehouse_selectable` | Boolean | 529 | Show on warehouse |
| `package_type_selectable` | Boolean | 530 | Show on package types |
| `company_id` | Many2one('res.company') | 533-536 | Optional; shared across companies when False |

**MIGRATION FLAG — packaging_ids ABSENT:** The field `packaging_ids` on stock.route appears only in i18n PO files (`stock/i18n/es_CL.po:5167` and many others) as `field_stock_route__packaging_ids` but does NOT exist in the Python model `StockRoute` in stock_location.py. The v19 implementation instead uses `package_type_selectable` on stock.route and `route_ids` Many2many on `stock.package.type` (stock_package_type.py:39). Stale translation strings confirm the field was present in an earlier version and removed.

---

## 3. _push_apply() Chain

**File:** `odoo/addons/stock/models/stock_move.py` lines 1214-1264

### Call point in _action_done
`_action_done()` at line 2249 writes moves to state 'done' at line 2290, then:
```
moves_to_push = moves_todo.filtered(lambda m: not m._skip_push())
if moves_to_push:
    moves_to_push._push_apply()    # line 2297-2299
```
After push, destination moves get `_action_assign()` called (line 2303).

Also called in `_action_confirm()` for negative quantity moves (line 1752).

### _skip_push() logic (line 2234-2240)
Skips push if:
- `is_inventory` is True, OR
- `move_dest_ids` exist and any dest move's `location_id` is a child-of or parent-of `location_dest_id`

### _push_apply() algorithm (lines 1214-1264)
1. Per-move loop
2. Handles inter-company: uses `sudo()` if dest company not in env.companies (line 1225-1228)
3. Collects related packages (line 1230) to include `package_type_id.route_ids`
4. Calls `StockRule._get_push_rule()` with `route_ids`, `warehouse_id`, `packaging_uom_id` (line 1232-1234)
5. Loops: if `rule.push_domain` set and move does NOT match — skip rule and retry without it (lines 1236-1242)
6. Skips if return move targets same location (line 1245)
7. Calls `rule._run_push(move)` (line 1246)
8. Updates `move_dest_ids` linkages for propagation (lines 1250-1258)
9. Bulk `_action_confirm()` on all new push moves (line 1262)

---

## 4. _run_pull() — Pull Rule Execution

**File:** `odoo/addons/stock/models/stock_rule.py` lines 289-318

```
@api.model
def _run_pull(self, procurements):
```

- Called from `run()` when `action == 'pull'` (or `'pull_push'` treated as pull) — line 489-499
- Validates `location_src_id` exists on each rule; raises `ProcurementException` if not (line 298-300)
- Sorts procurements so positive qty goes first (line 303)
- For each procurement: calls `_get_stock_move_values()` (line 309) then stores in `moves_values_by_company`
- `mts_else_mto` is simplified to `make_to_stock` at this point (lines 306-307)
- Creates all moves via `env['stock.move'].sudo().create()` grouped by company (line 315)
- Calls `_action_confirm()` on all created moves (line 317)

### _get_stock_move_values() (lines 326-387)
Key fields populated on the new stock.move:
- `location_id` = `rule.location_src_id`
- `location_dest_id` = `rule.location_dest_id` only if `location_dest_from_rule` is True (line 382-383), otherwise procurement's `location_dest_id`
- `location_final_id` = procurement's original `location_dest_id` (line 365) — the final intended destination through chains
- `rule_id` = rule.id
- `propagate_cancel` = rule.propagate_cancel (line 378)
- `reference_ids` = from procurement values (line 368) — REPLACES procurement.group in v19

---

## 5. _run_push() — Push Rule Execution

**File:** `odoo/addons/stock/models/stock_rule.py` lines 222-254

**IMPORTANT:** `_run_push()` is NOT called from `run()`. It is called explicitly from `stock_move._push_apply()` (line 1246). This is documented in the method docstring at line 228-230.

### Transparent auto (lines 233-243)
When `auto == 'transparent'`:
- Overwrites `move.location_dest_id` and `move.date` in place
- Updates move lines' location_dest_id via putaway strategy
- Recursively calls `move._push_apply()[:1]` to check for further push rules (avoids loops via dest change check)

### Manual auto (lines 244-254)
When `auto == 'manual'`:
- Calls `_push_prepare_move_copy_values()` (line 245) to build new move values
- Creates new move via `move.sudo().copy(new_move_vals)` (line 246)
- New move sets `procure_method: 'make_to_order'` (line 285 in _push_prepare_move_copy_values)
- If `_skip_push()` on new move: sets `location_dest_id` to `location_final_id` (line 248-249)
- Links original move to new move via `move_dest_ids` if source location requires reservation (line 252-253)

### _push_prepare_move_copy_values() (lines 256-287)
- Sets `location_id` = original move's `location_dest_id`
- Inherits `propagate_cancel` from rule (line 283)
- Carries `date_deadline` from original move (line 279)

---

## 6. Route Priority — Selection Algorithm

**File:** `odoo/addons/stock/models/stock_rule.py`

### _get_rule() (lines 566-640) — for pull rules
Priority order (higher = checked first):
1. Explicit `route_ids` from procurement values (e.g. from sale order line) — line 605-606
2. Package type routes (from `packaging_uom_id.package_type_id.route_ids`) — lines 607-608
3. Product routes + product category routes (`product_id.route_ids | product_id.categ_id.total_route_ids`) — line 610
4. Warehouse routes (`warehouse_id.route_ids`) — line 611-612

Within each tier: rules sorted by `(route_sequence, sequence)` ascending (line 590, 529, 551).
Within a merged set: product's own routes (in `product_id.route_ids`) come before category routes — sort key `r not in product_id.route_ids` (line 590).

Location hierarchy traversal: starts at exact location, walks up via `location_id` until rule found (line 619-639).

### _get_push_rule() (lines 667-679) — for push rules
- Domain: `location_src_id == location` AND `action in ('push', 'pull_push')` (line 674)
- Uses `_search_rule()` (line 677)
- Walks up location hierarchy on no match (line 678)

---

## 7. propagate_cancel and propagation_stock_picking_id

### propagate_cancel
- On stock.rule: `propagate_cancel = fields.Boolean(default=False)` — stock_rule.py:97-99
- On stock.move: `propagate_cancel = fields.Boolean(default=True)` — stock_move.py:146-148
  - Note: default differs: rule defaults False, move defaults True
- Copied from rule to move via `_get_stock_move_values()` (line 378) and `_push_prepare_move_copy_values()` (line 283)
- Cancel propagation logic in `_action_cancel()` — stock_move.py:2203-2207:
  - If `propagate_cancel` is True AND all sibling origin moves are also cancelled: cancels destination moves
  - Otherwise: unlinks dest moves and resets them to `make_to_stock`

### propagation_stock_picking_id
- **NOT PRESENT** in v19 stock community addon. Searched across all Python files in stock — no results. This field does not exist in v19.

---

## 8. Warehouse Routing — _get_routes_values()

**File:** `odoo/addons/stock/models/stock_warehouse.py` lines 526-580

Returns dict with two entries:
- `reception_route_id`: routing_key=`self.reception_steps`; depends=['reception_steps']; rules get `propagate_cancel: True`
- `delivery_route_id`: routing_key=`self.delivery_steps`; depends=['delivery_steps']; rules get `propagate_carrier: True`

### create_resupply_routes() (lines 702-737)
Creates inter-warehouse resupply routes:
1. Identifies transit location (internal if same company, external otherwise) — line 710
2. For `ship_only` delivery steps: creates extra MTO rule — lines 716-721
3. Creates `stock.route` with `supplied_wh_id` and `supplier_wh_id` — lines 723, 815-816
4. Creates pull rules: supplier output → transit → self input — lines 725-737

### _get_all_routes() (lines 1145-1148)
Returns: `warehouse.route_ids | warehouse.mto_pull_id.route_id | routes with supplied_wh_id == warehouse`

---

## 9. stock.move._action_assign() → Procurement Rules Chain

**File:** `odoo/addons/stock/models/stock_move.py` lines 2050-2110+

- Called from: `_action_done()` (line 2303), `_run_scheduler_tasks()` (line 713), `_action_confirm()` (line 1777)
- Reserves stock by creating `stock.move.line` records
- For MTO moves (has `move_orig_ids`, not bypassing reservation): reads from available move lines of origin (line 2088-2103)
- Scheduler calls `_action_assign()` in chunks of 1000 (stock_rule.py:712-713)

### _action_confirm() → Procurement chain (lines 1688-1783)
- `make_to_order` moves trigger procurement via `stock.rule.run()` (line 1728)
- Procurement data passed in `_prepare_procurement_values()` (line 1829-1867) includes:
  - `reference_ids`: the stock.reference chain (replaces procurement.group)
  - `route_ids`, `warehouse_id`, `move_dest_ids`, `packaging_uom_id`

---

## 10. MIGRATION FLAGS — v19 vs v16/v17

### FLAG-1: procurement.group REPLACED by stock.reference
- v16/v17: `procurement.group` model; moves had `group_id` Many2one
- v19: `stock.reference` model (stock_reference.py); moves have `reference_ids` Many2many
- Evidence: stock_move.py:141-142; stock_reference.py:1-15
- Impact: Any custom code referencing `move.group_id` or `env['procurement.group']` will break

### FLAG-2: stock.route.packaging_ids REMOVED
- v16/v17: `packaging_ids` field existed on stock.route
- v19: Field absent from StockRoute model (stock_location.py:517-595). Stale translations still reference it in i18n PO files
- v19 equivalent: `package_type_selectable` on stock.route + `route_ids` on stock.package.type (stock_package_type.py:39)
- Evidence: PO file stock/i18n/es_CL.po:5167; absence in stock_location.py

### FLAG-3: routing_id ABSENT
- No `routing_id` field found anywhere in the stock addon Python files (grep returns zero results)
- This contrasts with mrp.bom where routing_id was removed — same pattern in stock

### FLAG-4: location_dest_from_rule NEW in v19
- New Boolean field on stock.rule (stock_rule.py:72-75)
- When True: move destination set to rule's location_dest_id (not picking type default)
- Important for inter-warehouse resupply rules (stock_warehouse.py:727)

### FLAG-5: push_domain NEW in v19
- `push_domain = fields.Char('Push Applicability')` (stock_rule.py:111)
- Allows conditional push rules; rule only applies when move matches the domain
- Used in _push_apply loop (stock_move.py:1237-1242)

### FLAG-6: procurement_values Json field NEW in v19
- `procurement_values = fields.Json(store=False)` on stock.move (stock_move.py:140)
- Carries serialized procurement context through move chains
- `_serialize_procurement_values()` in stock_rule.py:389-410

### FLAG-7: _run_pull mts_else_mto simplification
- In v19 `_run_pull()`, `mts_else_mto` is immediately set to `make_to_stock` (stock_rule.py:306-307)
- No explicit forecast availability check in base stock; the MTO branch only fires if stock is insufficient at `_action_confirm()` time via the `mts_else_mto` rule flag on the move

### FLAG-8: location_final_id on stock.move (v19 pattern)
- `location_final_id` (stock_move.py:85-90) stores the final intended destination when a move is part of a chain going through intermediate locations
- Used in `_push_apply()` to properly link propagated dest moves (stock_move.py:1253)
- Used in `_get_stock_move_values()` (stock_rule.py:365) as `location_final_id`
