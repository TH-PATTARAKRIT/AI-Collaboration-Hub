# U193 — stock_barcode: Barcode Scanning for Picking / Receipt / Inventory
## STATE03 VDR — Restricted Technical Evidence (L3)

**Unit:** U193  
**Group:** G06 | Priority: P2  
**Status:** COMPLETE  
**Source base:** `/Volumes/iMacSys/CLAUDE AI/SMEsPlus/SMEsPlus19/SOURCE_CODE /01_ADDONS_COMMUNITY/addons/stock_barcode/`  
**Secondary (GS1):** `.../odoo/addons/barcodes_gs1_nomenclature/`  
**License:** OEEL-1 (Enterprise/Odoo Enterprise Edition License)

---

## 1. Module Identity & Dependencies

**Manifest path:** `stock_barcode/__manifest__.py`

```
'name': "Barcode"
'category': 'Inventory/Inventory'
'depends': ['barcodes', 'stock', 'web_tour']
'application': True
'license': 'OEEL-1'
```

**Claim C01:** `stock_barcode` declares exactly three hard dependencies: `barcodes`, `stock`, and `web_tour`. It does NOT depend on `stock_picking_wave`, `stock_picking_batch`, or any MRP module. Batch-barcode integration is delivered via a separate sibling module `stock_barcode_picking_batch`.

---

## 2. Server Model Layer: `stock_picking.py`

**File:** `stock_barcode/models/stock_picking.py`  

The file extends two models in one file: `StockMoveLine` (top section) and `StockPicking` (main body).

### 2.1 `StockMoveLine` Barcode Extension

**Claim C02:** `StockMoveLine` inherits from both `stock.move.line` and `barcodes.barcode_events_mixin`. It adds:
- `product_barcode` — `Char` related field on `product_id.barcode` (used for client-side display without a round-trip)
- `location_processed` — `Boolean` flag that tracks whether a destination-location scan has already committed this line
- `dummy_id` — computed `Char` with no-op inverse; used as a client-side virtual key to track unsaved lines before their ORM id is assigned

### 2.2 `StockPicking` Client Action Method

**Claim C03:** `_get_client_action(picking_id)` (not `_get_client_action_params`) constructs the fullscreen `ir.actions.client` dict. It uses the XML id `stock_barcode.stock_barcode_picking_client_action`, sets `target='fullscreen'`, and embeds `params={'model': 'stock.picking', 'picking_id': picking_id}`. The public entry point `open_picking_client_action()` checks `ir.config_parameter` key `stock_barcode.use_form_handler`; if truthy, the standard form view is returned instead.

### 2.3 `get_barcode_view_state()`

**Claim C04:** `get_barcode_view_state()` is the primary server-to-client serializer. It:
1. Calls `_get_picking_fields_to_read()` to retrieve picking-level fields (move_line_ids, picking_type_id, location_id, location_dest_id, name, state, picking_type_code, company_id, immediate_transfer).
2. Calls `_get_move_line_ids_fields_to_read()` for line-level fields (product_id, location_id, location_dest_id, qty_done, product_uom_qty, product_uom_id, product_barcode, owner_id, lot_id, lot_name, package_id, result_package_id, dummy_id).
3. Enriches each picking dict with group flags (`group_tracking_lot`, `group_production_lot`, `group_uom`, `group_stock_multi_locations`, `group_tracking_owner`) and picking-type settings (`use_create_lots`, `use_existing_lots`, `show_entire_packs`) fetched from `stock.picking.type`.
4. Appends `usable_packages` (via `stock.quant.package.get_usable_packages_by_barcode()`) only when `group_tracking_lot` is active.
5. Includes `nomenclature_id` if `company.nomenclature_id` is set, enabling GS1 parsing on the client.

### 2.4 `on_barcode_scanned()` — Main Scan Dispatch

**Claim C05:** `on_barcode_scanned(barcode)` on `StockPicking` handles two code-paths:

**Path A — No nomenclature:**
Resolution order:
1. Product by `barcode` or `default_code` (limit 1)
2. Product packaging by `barcode` (then route to product with packaging qty)
3. Source package by name, child-of `location_id`
4. Destination package by name, child-of `location_dest_id`
5. Location by name or barcode field, child-of `location_dest_id`

If nothing matches, returns a `{'warning': {...}}` dict with a "Wrong barcode" title.

**Path B — With nomenclature:**
Calls `nomenclature_id.parse_barcode(barcode)` and branches on `parsed_result['type']`: `weight`, `product`, `package`, `location`. Product packaging is also checked against `parsed_result['code']` after type branches.

### 2.5 Product Increment: `_check_product()`

**Claim C06:** `_check_product(product, qty=1.0)` locates a candidate `stock.move.line` for the scanned product by filtering lines not yet having a result package and not having `location_processed=True`. It increments `qty_done` in-place if a candidate exists. If no candidate is found, it creates a **new** move line via `self.move_line_ids.new({...})` (unsaved ORM record). For tracked products (`tracking != 'none'`) when the picking type has lot support enabled (`use_create_lots or use_existing_lots`), the new line is created with `qty_done=0.0`, deferring quantity confirmation until a lot barcode is scanned.

### 2.6 Destination Splitting: `_check_destination_location()`

**Claim C07:** `_check_destination_location(location)` splits a move line when `qty_done < product_uom_qty`. It creates a second line carrying the original reservation values (qty_done=0), sets `location_processed=True` and updates `location_dest_id` on the original processed line. This preserves the reservation for any un-processed remainder.

### 2.7 `StockPickingType` Extension

**Claim C08:** `StockPickingType` adds only one method: `get_action_picking_tree_ready_kanban()` which returns `_get_action('stock_barcode.stock_picking_action_kanban')`. The kanban action view is filtered to `code in ('incoming', 'outgoing', 'internal')`, confirming that all three standard operation types (receipt, delivery, internal) are first-class citizens in the barcode UI.

---

## 3. HTTP Controller: `controllers/main.py`

**File:** `stock_barcode/controllers/main.py`

**Claim C09:** Route `/stock_barcode/scan_from_main_menu` (JSON, auth=user) is the main-menu barcode entry point. It attempts in order:
1. `try_open_picking(barcode)` — searches `stock.picking` by name
2. `try_open_picking_type(barcode)` — searches `stock.picking.type` by barcode; if found, creates a new picking of that type
3. `try_new_internal_picking(barcode)` — searches `stock.location` by barcode, usage=internal; creates an immediate-transfer internal picking with `action_confirm()` (only when user has `stock.group_stock_multi_locations`)

**Claim C10:** Route `/stock_barcode/get_set_barcode_view_state` supports both read and write in one call. When `mode != 'read'`, it writes `{write_field: write_vals}` to the record before returning `get_barcode_view_state()`. The company context is derived from the `cids` cookie via `_get_allowed_company_ids()`, not `request.env.company`, to respect the company switcher selection.

---

## 4. Product Barcode Cache: `models/product_product.py`

**File:** `stock_barcode/models/product_product.py`

**Claim C11:** `get_all_products_by_barcode()` preloads the client barcode cache. It:
1. Fetches up to 10,000 products from recent `stock.move` records where `product_id.barcode != None`
2. Supplements with products whose `barcode != None` and `type != 'service'`
3. Merges product packaging barcodes — packaging entries take the product's data and append `qty` field
4. Returns a dict keyed by barcode string

**Claim C12:** `read_product_and_package(lot_ids, fetch_product)` is a targeted RPC method called during lot-step processing. It returns product fields (`display_name`, `uom_id`, `tracking`) and/or quant-based package/owner data. The quant search is restricted to `location_id.usage = 'internal'` to avoid finding packages in transit or virtual locations.

---

## 5. Location Cache: `models/stock_location.py`

**Claim C13:** `get_all_locations_by_barcode()` preloads the locations cache. Returns only locations where `barcode != None`, including `display_name`, `barcode`, and `parent_path`. `parent_path` is required by the client to implement `isChildOf()` checks in JavaScript without further round-trips.

---

## 6. Lot Wizard: `wizard/stock_barcode_lot.py`

**File:** `stock_barcode/wizard/stock_barcode_lot.py`

**Claim C14:** Wizard model `stock_barcode.lot` inherits `barcodes.barcode_events_mixin`. `on_barcode_scanned(barcode)` finds a matching `stock_barcode.lot.line` (matched by `lot_name == barcode` or by an empty lot_name slot) and increments its `qty_done`. For serial-tracked products, scanning the same number twice raises a `UserError` ("You cannot scan two times the same serial number").

**Claim C15:** `validate_lot()` commits scanned lot lines to `stock.move.line` records. The creation logic has three branches:
- If `use_create_lots` and NOT `use_existing_lots`: writes `lot_name` (string) directly without a database lookup — the lot is deferred and will be created on picking validation.
- Otherwise: calls `get_lot_or_create(barcode)` which searches `stock.production.lot` by name+product, creating a new lot record if not found.
- If no `move_line_id` reference exists: creates a new `stock.move` + embedded `stock.move.line` on-the-fly.

This confirms **auto-creation**: an unknown lot scanned in a picking with `use_create_lots=True` is created immediately in the database by `get_lot_or_create()`.

---

## 7. GS1 Nomenclature Integration: `barcodes_gs1_nomenclature`

**Source:** `odoo/addons/barcodes_gs1_nomenclature/`

**Claim C16:** GS1 Application Identifiers defined in `data/barcodes_gs1_rules.xml`:
| AI | Rule name | Pattern | Type | Content type |
|---|---|---|---|---|
| 01 | GTIN (Global Trade Item Number) | `(01)(\d{14})` | product | identifier |
| 10 | Batch or lot number | `(10)([!"%-/0-9:-?A-Z_a-z]{0,20})` | lot | alpha |
| 17 | Expiration date (YYMMDD) | `(17)(\d{6})` | expiration_date | date |
| 37 | Count of trade items | `(37)(\d{0,8})` | quantity | measure |

AI01 (GTIN) encodes a 14-digit product identifier with a check digit validated via `get_barcode_check_digit`. AI10 (lot) is variable-length alphanumeric, up to 20 chars. AI17 (expiry) is a 6-digit YYMMDD date resolved to a century using the GS1 century determination algorithm. AI37 (quantity) is a unitless integer count with no decimal usage.

**Claim C17:** `gs1_decompose_extended(barcode)` in both the Python model and the JS patch processes a GS1-128 extended barcode by iterating sequentially through all rules with encoding `gs1-128`. Each matched segment is consumed from the string and appended to a results list. Multiple AIs (e.g., AI01+AI10+AI17+AI37 in one scan) are thus all returned in a single parse call as an ordered list of dicts — each dict containing `type`, `ai`, `string_value`, and `value`. The FNC1 separator (`\x1D`) and configured alternative separators delimit variable-length fields.

---

## 8. JavaScript Client Action Architecture

**Files:** `static/src/js/client_action/abstract_client_action.js` (1976 lines), `picking_client_action.js` (760 lines), `inventory_client_action.js` (260 lines)

**Claim C18:** The scan flow is state-machine driven via `stepsByName`. All methods starting with `_step_` are auto-registered into `stepsByName`. The default step is `source`. Steps in sequence:

- `_step_source` → tries to match a source location; in `receipt` mode or `no_multi_locations` mode this step is bypassed and falls through to `_step_product`
- `_step_product` → resolves barcode to product via local cache (`productsByBarcode`), then increments; if product is tracked and `requireLotNumber=true`, advances step to `lot`
- `_step_lot` → resolves barcode as a lot via `searchRead` against `stock.production.lot`; if `use_create_lots && !use_existing_lots` it bypasses the DB search and sets `lot_name` directly; if both flags are true and lot is not found, calls `create()` RPC
- `_step_destination` → bypassed in `delivery` mode and `inventory` mode; updates `location_dest_id` on processed lines

**Claim C19:** `PickingClientAction` (JS) maps `picking_type_code` to mode: `incoming` → `receipt`, `outgoing` → `delivery`, anything else → `internal`. Mode `no_multi_locations` is set when `group_stock_multi_locations` is false. Modes `done` and `cancel` freeze the action. `requireLotNumber` is `use_create_lots || use_existing_lots` from the picking type settings, not from product tracking alone.

**Claim C20:** Quantity confirmation model: scans directly increment `qty_done` — no explicit confirm button per scan. The operator validates the entire operation via the `O-BTN.validate` command (keyboard shortcut) or the on-screen Validate button, both triggering `button_validate` on `stock.picking`. An immediate-transfer picking (`immediate_transfer=True`) is created when scanning from the main menu into a new picking type.

---

## 9. Inventory Adjustment (Physical Inventory)

**Claim C21:** `StockInventory.action_client_action()` launches `stock_barcode_inventory_client_action` (fullscreen `ir.actions.client`). `get_barcode_view_state()` on `stock.inventory` serializes `line_ids` with fields including `theoretical_qty`, `product_qty`, `prod_lot_id`, `package_id`, and `partner_id`. The inventory client action defaults to `inventory` mode; it falls back to `no_multi_locations` when the multi-location group is inactive.

---

## 10. Configuration Settings

**Claim C22:** `ResConfigSettings` extension (`models/res_config_settings.py`) exposes:
- `barcode_nomenclature_id` — related to `company_id.nomenclature_id`; if set, all scan dispatches use GS1 parsing instead of direct string matching
- `group_barcode_keyboard_shortcuts` — optional group for keyboard shortcut UI (implied group assigned to all users by default in `stock_barcode_security.xml`)
- `keyboard_layout` — selection (qwerty/azerty/alphabetical) on `res.company`; TODO-marked for removal in master

---

## Source Evidence Summary

| File | Key Methods | Evidence Level |
|---|---|---|
| `models/stock_picking.py` | `get_barcode_view_state`, `on_barcode_scanned`, `_check_product`, `_check_destination_location`, `_get_client_action` | L3 — direct read |
| `controllers/main.py` | `/scan_from_main_menu`, `/get_set_barcode_view_state`, `try_open_picking*` | L3 — direct read |
| `models/product_product.py` | `get_all_products_by_barcode`, `read_product_and_package` | L3 — direct read |
| `wizard/stock_barcode_lot.py` | `on_barcode_scanned`, `validate_lot`, `get_lot_or_create` | L3 — direct read |
| `models/stock_inventory.py` | `action_client_action`, `get_barcode_view_state` | L3 — direct read |
| `barcodes_gs1_nomenclature/models/barcode_nomenclature.py` | `gs1_decompose_extended`, `parse_gs1_rule_pattern` | L3 — direct read |
| `barcodes_gs1_nomenclature/data/barcodes_gs1_rules.xml` | AI01, AI10, AI17, AI37 rule definitions | L3 — direct read |
| `static/src/js/client_action/abstract_client_action.js` | `_step_source/product/lot/destination`, `_onBarcodeScanned` | L3 — direct read |
| `static/src/js/client_action/picking_client_action.js` | `mode` assignment, `_validate`, `requireLotNumber` | L3 — direct read |
