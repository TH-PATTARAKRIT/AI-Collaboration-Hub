# U169 — stock: Physical Inventory Count and Quant Adjustment — RESTRICTED TECHNICAL EVIDENCE
**Unit**: U169 | **Group**: G06/G01 | **Priority**: P1 | **Module Status**: PRESENT
**Odoo Version**: 19.0.post20260921 | **Module Version**: 0.1
**Researcher**: DeepSeek Worker (STATE03 VDR) | **Date**: 2026-10-02

---

## MODULE MANIFEST

**Primary file**: `stock/models/stock_quant.py`
**Valuation overlay**: `stock_account/models/stock_quant.py`, `stock_account/models/stock_move.py`
**Location model**: `stock/models/stock_location.py`
**Company setup**: `stock/models/res_company.py`

The physical inventory count and quant adjustment mechanism is embedded directly in `stock.quant`. There is **no separate inventory order model** in Odoo 19 Community; counts are performed inline on quant records via an `inventory_mode` context flag.

---

## VDR CLAIMS TABLE — 22 Claims

| # | Claim ID | Boundary | Model/Object | Field/Method | Evidence Source | Certainty | L-Level | Notes |
|---|----------|----------|--------------|--------------|-----------------|-----------|---------|-------|
| 1 | U169-C01 | Count initiation | `stock.quant` | `action_view_inventory()` | `stock_quant.py:402-431` | HIGH | L3 | Opens "Physical Inventory" editable list view. Sets `inventory_mode=True` via `_set_view_context()`. Domain: `[('location_id.usage', 'in', ['internal','transit'])]`. No `_action_start_inventory()` method exists in Odoo 19 Community. |
| 2 | U169-C02 | Inventory mode gate | `stock.quant` | `_is_inventory_mode()` | `stock_quant.py:1231-1236` | HIGH | L3 | `return self.env.context.get('inventory_mode') and self.env.user.has_group('stock.group_stock_user')`. Both conditions required. Context flag + user group. |
| 3 | U169-C03 | Count field | `stock.quant` | `inventory_quantity` | `stock_quant.py:97-99` | HIGH | L3 | `Float('Counted', digits='Product Unit')`. User-entered physical count. No domain filter, no compute — plain editable field. Accessible only inside inventory_mode. |
| 4 | U169-C04 | Count flag | `stock.quant` | `inventory_quantity_set` | `stock_quant.py:113` | HIGH | L3 | `Boolean(store=True, compute='_compute_inventory_quantity_set', readonly=False)`. Becomes True the moment `inventory_quantity` is written. Cleared on apply. Marks which quants are participating in an active count. |
| 5 | U169-C05 | Difference field | `stock.quant` | `inventory_diff_quantity` | `stock_quant.py:105-108,185-191` | HIGH | L3 | `Float('Difference', compute='_compute_inventory_diff_quantity', store=True, readonly=True)`. Formula: `inventory_quantity - quantity` if `inventory_quantity_set`, else 0. Negative diff = shrinkage; positive = surplus. |
| 6 | U169-C06 | Outdated detection | `stock.quant` | `is_outdated` | `stock_quant.py:114,197-202` | HIGH | L3 | `Boolean(compute='_compute_is_outdated')`. True when `quantity` has changed since count was entered (a real stock move happened during count). Triggers conflict resolution. |
| 7 | U169-C07 | Apply action | `stock.quant` | `action_apply_inventory(date=None)` | `stock_quant.py:433-450` | HIGH | L3 | Entry point for applying count. Checks `is_outdated` quants; if any exist, opens `stock.inventory.conflict` wizard (via act_window). Otherwise calls `_apply_inventory(date)` then sets `inventory_quantity_set = False`. |
| 8 | U169-C08 | Core adjustment | `stock.quant` | `_apply_inventory(date=None)` | `stock_quant.py:996-1035` | HIGH | L3 | Private method. Resolves `inventory_location` = `product_id.property_stock_inventory` per company. For diff > 0: creates move `inventory_location → quant.location_id`. For diff < 0: creates move `quant.location_id → inventory_location`. Both use `package_id`/`lot_id`. Calls `moves._action_done()` immediately. Updates `last_inventory_date` and `inventory_date`. |
| 9 | U169-C09 | Move structure | `stock.quant` | `_get_inventory_move_values()` | `stock_quant.py:1253-1292` | HIGH | L3 | Returns dict for `stock.move.create()`. Fields: `product_id`, `product_uom`, `product_uom_qty`, `location_id`, `location_dest_id`, `is_inventory=True`, `picked=True`, `state='confirmed'`. Inline `move_line_ids` with `lot_id`, `package_id`, `owner_id`. |
| 10 | U169-C10 | Inventory loss location | `stock.location` | `usage='inventory'` | `stock_location.py:37,44-45` | HIGH | L3 | Selection value: `('inventory', 'Inventory Loss')`. Help: "Virtual location serving as the counterpart for inventory operations done to correct stock levels (Physical inventories)". `should_bypass_reservation()` returns True for this usage type. Per-company, created by `res_company._create_inventory_loss_location()`. |
| 11 | U169-C11 | Inventory loss pointer | `product.template` | `property_stock_inventory` | `product.py:849-852` | HIGH | L3 | `Many2one('stock.location', company_dependent=True, domain=[('usage','=','inventory')])`. Points to the company's inventory loss/adjustment location. Used by `_apply_inventory()` to identify the counterpart location. Default set via `ir.default` per company. |
| 12 | U169-C12 | SVL / JE: valuation trigger | `stock_account/stock_move` | `_action_done()` override | `stock_account/stock_move.py:177-191` | HIGH | L3 | Calls `_set_value()` for `is_out` moves (COGS-style) and `is_in` moves. Calls `_create_account_move()` after. Inventory adjustment moves are `is_in` (positive diff, source=non-valued inventory_loss, dest=valued internal) or `is_out` (negative diff). |
| 13 | U169-C13 | SVL: journal entry condition | `stock_account/stock_move` | `_should_create_account_move()` | `stock_account/stock_move.py:659-667` | HIGH | L3 | Returns True only if: `product.is_storable AND is_valued AND (location_dest_id.valuation_account_id OR location_id.valuation_account_id) AND qty != 0 AND valuation='real_time'`. Requires `valuation_account_id` on at least one location. |
| 14 | U169-C14 | SVL: account assignment | `stock_account/stock_move` | `_get_account_move_line_vals()` | `stock_account/stock_move.py:229-249` | HIGH | L3 | If `location_id.valuation_account_id`: debit=`product._get_product_accounts()['stock_valuation']`, credit=`location_id.valuation_account_id`. Else: debit=`location_dest_id.valuation_account_id`, credit=`stock_valuation`. For inventory increase: debit=stock_valuation (asset up), credit=inventory_loss.valuation_account_id (expense). |
| 15 | U169-C15 | SVL: accounting_date override | `stock_account/stock_quant` | `_apply_inventory(date=None)` | `stock_account/stock_quant.py:80-87` | HIGH | L3 | Override groups quants by `accounting_date` field. For quants with a specific accounting_date, calls `super()._apply_inventory()` with `force_period_date=accounting_date` in context, then clears `accounting_date`. Enables cross-period corrections. |
| 16 | U169-C16 | SVL: accounting name | `stock_account/stock_quant` | `_get_inventory_move_values()` | `stock_account/stock_quant.py:89-101` | HIGH | L3 | Override adds `inventory_name` to move dict when `force_period_date` context is set. Name: "Product Quantity Updated [Accounted on {date}]" (or "Product Quantity Confirmed" if qty=0). Includes user's display_name. |
| 17 | U169-C17 | Stock_valuation account | `stock_account/product` | `_get_product_accounts()` | `stock_account/product.py:130-142` | HIGH | L3 | Returns `accounts['stock_valuation']` = `categ.property_stock_valuation_account_id` or company fallback `account_stock_valuation_id`. This is the balance-sheet stock asset account used as one side of the inventory adjustment JE. |
| 18 | U169-C18 | Lot-level counts | `stock.quant` | `lot_id` + quant uniqueness | `stock_quant.py:64-67; _apply_inventory():1282-1283` | HIGH | L3 | Each stock.quant is unique per (product, location, lot, package, owner). Physical count is therefore inherently lot-level. `_get_inventory_move_values()` includes `lot_id` in the move_line. Users count separately per lot in the inventory view. |
| 19 | U169-C19 | Cycle count: location-level | `stock.location` | `cyclic_inventory_frequency` | `stock_location.py:81,141-153` | HIGH | L3 | `Integer("Inventory Frequency", default=0)`. When non-zero, drives `next_inventory_date` computation. Formula: `last_inventory_date + cyclic_inventory_frequency (days)`. Applies only to internal/transit locations. |
| 20 | U169-C20 | Cycle count: annual | `res.company` | `annual_inventory_month`, `annual_inventory_day` | `res_company.py:24-43` | HIGH | L3 | Company-level annual count date. `_get_next_inventory_date()` in stock_location returns min(cyclic date, annual date). No cron job auto-triggers counts; these fields only set the `inventory_date` reminder on quants. |
| 21 | U169-C21 | Conflict resolution | `stock.quant` | `stock.inventory.conflict` | `stock_quant.py:437-448` | HIGH | L3 | When outdated quants are found, `action_apply_inventory()` opens wizard `stock.inventory.conflict` (target='new') passing `default_quant_ids` and `default_quant_to_fix_ids`. User resolves conflicts before applying. |
| 22 | U169-C22 | Auto-apply path | `stock.quant` | `inventory_quantity_auto_apply` | `stock_quant.py:100-104,225-237` | HIGH | L3 | Computed Float with inverse `_set_inventory_quantity`. Used by `action_set_inventory_quantity_zero()` and barcode-driven fast paths. Inverse immediately calls `action_apply_inventory()` — skips staging, applies directly. Restricted to `stock.group_stock_user`. |

---

## ADDITIONAL TECHNICAL DETAILS

### Inventory Mode Context Guard
- `inventory_mode=True` in context enables: (1) creating new quants via `create()`, (2) writing `inventory_quantity` on existing quants, (3) `inventory_quantity_auto_apply` inverse triggering immediate apply.
- Without `inventory_mode`, writes to `inventory_quantity` are silently ignored by `_set_inventory_quantity()` (line 229 guard).
- `_get_inventory_fields_write()` lists which fields are editable in mode: `inventory_quantity`, `inventory_quantity_auto_apply`, `inventory_diff_quantity`, `inventory_date`, `user_id`, `inventory_quantity_set`, `is_outdated`, `lot_id`, `location_id`, `package_id`. Extended by `stock_account` to include `accounting_date`.

### No Separate Inventory Order / Session
- Odoo 19 Community has **no `stock.inventory` model** (abolished in Odoo 16+). 
- There is no "inventory session" lifecycle with open/close states.
- The inventory view (`action_view_inventory`) opens directly on `stock.quant` with inventory_mode enabled.
- All state is held in fields on the quant itself (`inventory_quantity_set`, `inventory_quantity`, `inventory_date`, `user_id`).

### inventory_quantity_count Field
- The field `inventory_quantity_count` mentioned in some research scopes does **NOT exist** in Odoo 19 Community `stock.quant`. The count of quants actively being counted is obtained by searching `inventory_quantity_set = True`.

### Cycle Count Scheduling (No Cron)
- No `ir.cron` record for physical inventory in the stock module.
- `cyclic_inventory_frequency` on `stock.location` sets the rotation interval in days.
- `inventory_date` on `stock.quant` is recomputed after each apply from `_get_next_inventory_date()`.
- Users see overdue items in the Physical Inventory view by filtering `inventory_date <= today`.
- A `search_default_my_count` context flag is set for non-manager users to see only their assigned quants.

### Package Support
- `_get_inventory_move_values()` accepts `package_id` and `package_dest_id` parameters.
- Positive diff: `package_dest_id=quant.package_id` (stock arrives in the same package).
- Negative diff: `package_id=quant.package_id` (stock leaves from the package).

### apply_all Wizard Path
- `action_apply_all()` (line 518) uses a `stock.inventory.adjustment.name` wizard to apply all flagged quants in the current domain at once, optionally with a named reference for traceability.
