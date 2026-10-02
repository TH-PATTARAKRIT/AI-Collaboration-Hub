# U213 — stock_warehouse: Warehouse Model, Route Creation, Company Binding, Multi-Step Routing

**Research Unit**: U213  
**Module**: stock (addons/stock/models/stock_warehouse.py)  
**Source SHA-256**: 11acf902d663ccd2dabee8d51978d92c732dd837a183928f704945c03ea224f8  
**Source lines**: 1164  
**Odoo version**: 19.0.post20260921 (Community)  
**Researcher**: STATE03 VDR Worker (Claude Sonnet 4.6)  
**Date**: 2026-10-02  
**Classification**: RESTRICTED TECHNICAL EVIDENCE

---

## 1. Model Declaration and Class-Level Attributes

**File**: `odoo/addons/stock/models/stock_warehouse.py`

```
line 23: class StockWarehouse(models.Model):
line 24:     _name = 'stock.warehouse'
line 25:     _description = "Warehouse"
line 26:     _order = 'sequence,id'
line 27:     _check_company_auto = True
line 28:     # namedtuple used in helper methods generating values for routes
line 29:     Routing = namedtuple('Routing', ['from_loc', 'dest_loc', 'picking_type', 'action'])
```

- `_check_company_auto = True` enforces automatic domain filtering on all relational fields marked `check_company=True`.
- The `Routing` namedtuple (fields: `from_loc`, `dest_loc`, `picking_type`, `action`) is used as the core data structure in `get_rules_dict()` and all rule-generation helpers.

---

## 2. Key Fields — Definitions and Constraints

### 2.1 Identity Fields

| Field | Type | Line | Notes |
|-------|------|------|-------|
| `name` | Char | 35 | required, default=`_default_name` (company name or incremented label) |
| `code` | Char(5) | 50 | required, size=5, unique per company |
| `active` | Boolean | 36 | default=True |
| `sequence` | Integer | 89 | default=10, orders warehouse list |

Constraints (new-style `models.Constraint` in v19):
```
line 91: _warehouse_name_uniq = models.Constraint('unique(name, company_id)', ...)
line 95: _warehouse_code_uniq = models.Constraint('unique(code, company_id)', ...)
```
Both constraints are scoped per company, not globally.

### 2.2 Company and Partner

```
line 37-40: company_id = fields.Many2one(
    'res.company', 'Company', default=lambda self: self.env.company,
    readonly=True, required=True, ...)
line 41: partner_id = fields.Many2one('res.partner', 'Address', ..., check_company=True)
```

`company_id` is `readonly=True` at field level. The `write()` override (lines 187-190) raises `UserError` if caller attempts to change `company_id` on an existing record.

### 2.3 Location Fields

All location fields carry `check_company=True` (enforced by `_check_company_auto`):

| Field | Line | Usage | Active condition |
|-------|------|-------|-----------------|
| `view_location_id` | 42-45 | view | always |
| `lot_stock_id` | 46-49 | internal | always (main stock location) |
| `wh_input_stock_loc_id` | 68 | internal | reception_steps != 'one_step' |
| `wh_qc_stock_loc_id` | 69 | internal | reception_steps == 'three_steps' |
| `wh_output_stock_loc_id` | 70 | internal | delivery_steps != 'ship_only' |
| `wh_pack_stock_loc_id` | 71 | internal | delivery_steps == 'pick_pack_ship' |

The `view_location_id` domain enforces `[('usage','=','view'), ('company_id','=',company_id)]` (line 44).

### 2.4 Picking Type Fields (Many2one to stock.picking.type)

```
line 73: pick_type_id
line 74: pack_type_id
line 75: out_type_id
line 76: in_type_id
line 77: int_type_id
line 78: qc_type_id      # quality control step (new dedicated type in v19)
line 79: store_type_id   # storage step (new dedicated type in v19)
line 80: xdock_type_id   # cross dock (new in v19)
```

All carry `check_company=True, copy=False`.

### 2.5 Route Fields

```
line 81: reception_route_id — Many2one stock.route, ondelete='restrict', copy=False
line 82: delivery_route_id  — Many2one stock.route, ondelete='restrict', copy=False
line 51-55: route_ids — Many2many 'stock.route', through 'stock_route_warehouse', copy=False
```

`route_ids` domain: `[('warehouse_selectable','=',True), '|', ('company_id','=',False), ('company_id','=',company_id)]` (line 54).

### 2.6 MTO and Resupply

```
line 72: mto_pull_id = fields.Many2one('stock.rule', 'MTO rule', copy=False)
line 83-85: resupply_wh_ids = fields.Many2many(
    'stock.warehouse', 'stock_wh_resupply_table', 'supplied_wh_id', 'supplier_wh_id', ...)
line 86-88: resupply_route_ids = fields.One2many('stock.route', 'supplied_wh_id', ...)
```

---

## 3. Reception Steps and Delivery Steps

### 3.1 Field Definitions

```
line 56-61: reception_steps = fields.Selection([
    ('one_step',    'Receive and Store (1 step)'),
    ('two_steps',   'Receive then Store (2 steps)'),
    ('three_steps', 'Receive, Quality Control, then Store (3 steps)')],
    default='one_step', required=True)

line 62-67: delivery_steps = fields.Selection([
    ('ship_only',     'Deliver (1 step)'),
    ('pick_ship',     'Pick then Deliver (2 steps)'),
    ('pick_pack_ship','Pick, Pack, then Deliver (3 steps)')],
    default='ship_only', required=True)
```

### 3.2 Change Triggers in write()

When `reception_steps` or `delivery_steps` appear in `vals` (lines 196-201):

1. **Location activation** (`_update_location_reception` / `_update_location_delivery`):
   - `_update_location_reception` (lines 945-947): activates/deactivates `wh_qc_stock_loc_id` and `wh_input_stock_loc_id`.
   - `_update_location_delivery` (lines 949-951): activates/deactivates `wh_pack_stock_loc_id` and `wh_output_stock_loc_id`.

2. **Resupply MTO rule update** (`_update_reception_delivery_resupply`, lines 863-869): adjusts resupply MTO rules when the delivery step crosses the `ship_only` boundary (i.e., changes between single-step and multi-step).

3. **Route/rule re-creation** (lines 220-229):
   - Collects all `depends` from `_get_routes_values()`.
   - If changed field in deps: calls `_create_or_update_sequences_and_picking_types()` then `_create_or_update_route()`.

4. **Global rules update** (lines 234-238): if global route depends changed, calls `_create_or_update_global_routes_rules()`.

---

## 4. `_get_routes_values()` — Route Creation Configuration

**Lines 526-580**

Returns a dict keyed by route field name on the warehouse. Each entry contains:

| Key | Purpose |
|-----|---------|
| `routing_key` | Current step value used to look up rules in `get_rules_dict()` |
| `depends` | List of warehouse fields; changes trigger route rebuild |
| `route_update_values` | Values written to existing route on step change |
| `route_create_values` | Values used to create route if it does not exist |
| `rules_values` | Extra values applied to each generated rule |

**reception_route_id** entry (lines 542-559):
- `routing_key`: `self.reception_steps`
- `depends`: `['reception_steps']`
- `route_create_values`: `product_categ_selectable=True`, `warehouse_selectable=True`, `product_selectable=False`, `company_id=self.company_id.id`, `sequence=50`
- `rules_values`: `active=True, propagate_cancel=True`

**delivery_route_id** entry (lines 561-579):
- `routing_key`: `self.delivery_steps`
- `depends`: `['delivery_steps']`
- `route_create_values`: `product_categ_selectable=True`, `warehouse_selectable=True`, `product_selectable=False`, `company_id=self.company_id.id`, `sequence=60`
- `rules_values`: `active=True, propagate_carrier=True`

---

## 5. `_create_or_update_route()` — Route Lifecycle

**Lines 473-524**

Logic flow:
1. For each `(route_field, route_data)` in `_get_routes_values()`:
   - If route exists: update with `route_update_values`, archive all existing rules (`route.rule_ids.write({'active': False})`).
   - If route does not exist: create with `route_create_values` merged with `route_update_values`.
2. Fetch rules from `get_rules_dict()[self.id][routing_key]`.
3. Call `_find_existing_rule_or_create(rules_list)` to activate archived or create new rules.
4. If route is `warehouse_selectable`: append to returned `route_ids` M2M additions.

---

## 6. Global Routes — MTO Rule

### 6.1 `_create_or_update_global_routes_rules()` — Lines 396-410

Iterates `_get_global_route_rules_values()`. For each rule field:
- If field exists on warehouse: write `update_values`.
- If not: create rule with `create_values` + `{'warehouse_id': self.id}`, assign to warehouse field.

### 6.2 `_generate_global_route_rules_values()` — Lines 444-471

Returns `mto_pull_id` configuration:
- **depends**: `['delivery_steps']`
- **Selects from `get_rules_dict()`**: the rule where `from_loc == self.lot_stock_id` for the current `delivery_steps`.
- **create_values**:
  - `procure_method: 'make_to_order'`
  - `action: 'pull'`
  - `auto: 'manual'`
  - `propagate_carrier: True`
  - `route_id`: found/created global MTO route via `_find_or_create_global_route('stock.route_warehouse0_mto', 'Replenish on Order (MTO)')`
- **update_values**: name, `location_dest_id`, `location_src_id`, `picking_type_id` (derived from current step).

### 6.3 `_find_or_create_global_route()` — Lines 412-425

Finds global route by XML ID or name. If no company-matching route found and `create=True`, copies the data route with `company_id=company.id, rule_ids=False`.

---

## 7. `get_rules_dict()` — Rule Routing Definitions

**Lines 766-791**

Returns dict keyed by `warehouse.id`. Each warehouse entry maps step keys to lists of `Routing` namedtuples:

| Step | Rules |
|------|-------|
| `one_step` | [supplier_loc → lot_stock_id, in_type_id, pull] |
| `two_steps` | [supplier_loc → lot_stock_id pull; wh_input → lot_stock push via store_type_id] |
| `three_steps` | [supplier → lot_stock pull; input → QC push via qc_type_id; QC → stock push via store_type_id] |
| `ship_only` | [lot_stock_id → customer_loc, out_type_id, pull] |
| `pick_ship` | [lot_stock → customer pick pull via pick_type_id; output → customer push via out_type_id] |
| `pick_pack_ship` | [lot_stock → customer pick pull; pack_zone → output push via pack_type_id; output → customer push via out_type_id] |

Note: `store_type_id` handles the final move-to-stock in two_steps and three_steps. `qc_type_id` exclusively handles input→QC in three_steps.

---

## 8. Picking Type Values

### 8.1 `_get_picking_type_update_values()` — Lines 956-996

Updates picking type properties when steps change:

| Picking Type Field | Active condition | default_location_src / dest |
|-------------------|-----------------|----------------------------|
| `in_type_id` | always | dest = input_loc (lot_stock if one_step, else wh_input_stock) |
| `out_type_id` | always | src = output_loc (lot_stock if ship_only, else wh_output) |
| `pick_type_id` | delivery_steps != 'ship_only' | dest = output (pick_ship) or pack_zone (pick_pack_ship) |
| `pack_type_id` | delivery_steps == 'pick_pack_ship' | dest = output_loc |
| `qc_type_id` | reception_steps == 'three_steps' | — |
| `store_type_id` | reception_steps != 'one_step' | src = input (two_steps) or QC (three_steps) |
| `int_type_id` | always | barcode only |
| `xdock_type_id` | reception_steps != 'one_step' AND delivery_steps != 'ship_only' | — |

### 8.2 `_get_picking_type_create_values()` — Lines 998-1081

Creates picking types at warehouse creation with sequence offsets:

| Field | sequence offset | sequence_code |
|-------|----------------|--------------|
| in_type_id | +1 | IN |
| qc_type_id | +2 | QC |
| store_type_id | +3 | STOR |
| int_type_id | +4 | INT |
| pick_type_id | +5 | PICK |
| pack_type_id | +6 | PACK |
| out_type_id | +7 | OUT |
| xdock_type_id | +8 | XD |

Cross-dock default: src=wh_input_stock_loc_id, dest=wh_output_stock_loc_id.

---

## 9. MTO Pull Rule and Inter-Warehouse Resupply

### 9.1 mto_pull_id

The MTO pull rule is a `stock.rule` stored directly on the warehouse (line 72). It is part of the global MTO route (`stock.route_warehouse0_mto`). When `delivery_steps` changes, `write()` triggers `_create_or_update_global_routes_rules()` which updates `mto_pull_id`'s source location and picking type to match the new step (lines 464-470).

### 9.2 resupply_wh_ids — Inter-Warehouse Resupply

**M2M definition** (lines 83-85): `stock_wh_resupply_table` table, columns `supplied_wh_id` / `supplier_wh_id`.

**write() handling** (lines 203-204, 290-311):
- Before super write: snapshot `old_resupply_whs`.
- After write: compute `to_add = new - old`, `to_remove = old - new`.
- `to_add`: try to unarchive existing archived routes; create new routes via `create_resupply_routes()` for remainder.
- `to_remove`: archive routes matching `(supplied_wh_id=warehouse.id, supplier_wh_id IN to_remove.ids)`.

**`create_resupply_routes()`** (lines 702-737):
- Uses `_get_transit_locations()` to get internal or external transit location.
- Cross-company detection: if `supplier_wh.company_id != self.company_id`, use external transit.
- For each supplier warehouse:
  - If supplier delivery = 'ship_only': create extra MTO rule from `lot_stock_id → transit`.
  - Create inter-wh route via `_get_inter_warehouse_route_values()`.
  - Create pull rules: `output_loc → transit` and optionally `lot_stock → output_loc` (multi-step supplier).
  - Create receiving pull rule: `transit → self.lot_stock_id` using `self.in_type_id`.

**`_get_inter_warehouse_route_values()`** (lines 809-818):
- Route company_id = intersection of both warehouses' companies: `(self.company_id & supplier_warehouse.company_id).id`.
- Marks route as `warehouse_selectable=True, product_selectable=True, product_categ_selectable=True`.

---

## 10. Company Enforcement

**Field level** (line 39): `company_id` is `readonly=True`. Default = `self.env.company`.

**write() guard** (lines 187-190):
```python
if 'company_id' in vals:
    for warehouse in self:
        if warehouse.company_id.id != vals['company_id']:
            raise UserError(_("Changing the company of this record is forbidden..."))
```

**`_check_company_auto = True`** (line 27): Odoo framework adds `company_id` domain on all fields with `check_company=True`. Affected fields: `partner_id`, `view_location_id`, `lot_stock_id`, `wh_input_stock_loc_id`, `wh_qc_stock_loc_id`, `wh_output_stock_loc_id`, `wh_pack_stock_loc_id`, `pick_type_id`, `pack_type_id`, `out_type_id`, `in_type_id`, `int_type_id`, `qc_type_id`, `store_type_id`, `xdock_type_id`, `mto_pull_id` (indirectly via picking types).

**route_ids domain** (line 54): `'|', ('company_id','=',False), ('company_id','=',company_id)` — allows global (no company) routes and company-specific routes.

**DB-level constraints**: `unique(name, company_id)` and `unique(code, company_id)` — no cross-company name collisions but identical names allowed across companies.

---

## 11. warehouse create() Flow

**Lines 113-163**:

1. If `company_id` supplied: derive `name`, `code`, `partner_id` from company if not in vals.
2. Create `view_location_id` (usage='view').
3. Call `_get_locations_values(vals)` → create all sub-locations (stock, input, QC, output, pack) with initial `active` status.
4. Call `super().create(vals_list)`.
5. For each warehouse:
   a. `_create_or_update_sequences_and_picking_types()` → create picking types + sequences.
   b. `_create_or_update_route()` → create reception and delivery routes + rules.
   c. `_create_or_update_global_routes_rules()` → create MTO pull rule.
   d. `create_resupply_routes(warehouse.resupply_wh_ids)` → create inter-wh routes if any.
   e. Update partner stock properties.
   f. Assign `warehouse_id` to all child locations.
6. `_check_multiwarehouse_group()` → activate multi-warehouse UI group if >1 warehouse per company.

---

## 12. Multi-Warehouse Group Check

**Lines 322-337** (`_check_multiwarehouse_group`):

Uses `_read_group([('active','=',True)], ['company_id'], aggregates=['__count'])` to count active warehouses per company. If any company has >1 warehouse, enables `stock.group_stock_multi_warehouses` and `stock.group_stock_multi_locations` on base user group.

---

## 13. V19 Migration Flags

### MF-01: New Picking Types — qc_type_id, store_type_id, xdock_type_id

V19 introduces three new dedicated picking type fields on `stock.warehouse`:
- `qc_type_id` (line 78): Quality Control picking type, distinct from generic internal.
- `store_type_id` (line 79): Storage picking type for putaway-to-stock move.
- `xdock_type_id` (line 80): Cross-dock picking type, active when both reception AND delivery are multi-step.

In prior versions, some of these moves were handled by generic `int_type_id`. Migration must create these new picking types and assign them.

### MF-02: models.Constraint (New Constraint Syntax)

Lines 91-98 use `models.Constraint(...)` instead of legacy `_sql_constraints = [...]`. Migrations must not duplicate constraints.

### MF-03: xdock_type_id Active Logic

`xdock_type_id` is active only when `reception_steps != 'one_step' AND delivery_steps != 'ship_only'` (line 993). This is a cross-conditional activation absent in older versions.

### MF-04: _get_receive_rules_dict() / _get_receive_routes_values() Pattern

New pattern (lines 793-807, 582-616) for modules that add purchase-triggered receive rules with `procure_method='make_to_order'`. The base one_step entry returns empty rules list (line 802). Modules extending stock (e.g. purchase) must call these variants instead of `get_rules_dict()` / `_get_routes_values()`.

### MF-05: Cross-Company Transit Location

`_get_transit_locations()` (lines 746-747) returns:
- Internal transit: `company_id.internal_transit_location_id`
- External transit: `env.ref('stock.stock_location_inter_company', raise_if_not_found=False)`

If external transit location does not exist (ref not found), inter-company resupply routes are silently skipped (line 712: `if not transit_location: continue`).

### MF-06: route_ids ondelete=restrict for reception/delivery routes

`reception_route_id` and `delivery_route_id` both have `ondelete='restrict'` (lines 81-82). Deleting a route that is still referenced by a warehouse raises an integrity error.

### MF-07: _default_name uses search_count with active_test=False

Line 32: counts ALL warehouses (including archived) for default name numbering. This prevents duplicate name conflicts on restore/migration.

---

## 14. _get_input_output_locations() Utility

**Lines 742-744**:
```python
return (
    self.lot_stock_id if reception_steps == 'one_step' else self.wh_input_stock_loc_id,
    self.lot_stock_id if delivery_steps == 'ship_only' else self.wh_output_stock_loc_id
)
```

This utility is called throughout route/picking-type creation to determine the effective "entry" and "exit" location for the warehouse step configuration.

---

## 15. _update_reception_delivery_resupply() — Resupply Route Adjustment

**Lines 863-916**

When `delivery_steps` crosses the `ship_only` boundary:
- **Gaining multi-step** (`change_to_multiple=True`): archives MTO rules going to transit from `lot_stock_id`; unarchives or creates pick rules from `lot_stock_id → wh_output_stock_loc_id`.
- **Losing multi-step** (`change_to_multiple=False`): archives pick rules going to output; creates new MTO rules from `lot_stock_id` directly to transit; updates resupply pull rule `location_src_id` to `lot_stock_id`.
