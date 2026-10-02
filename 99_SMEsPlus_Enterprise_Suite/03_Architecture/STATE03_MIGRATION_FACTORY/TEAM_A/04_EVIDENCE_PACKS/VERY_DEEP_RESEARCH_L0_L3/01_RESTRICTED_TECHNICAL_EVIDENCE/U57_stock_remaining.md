# U57 — stock remaining: lot/serial, forecast, replenishment, batch/wave picking, procurement rules (restricted technical evidence)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
- Unit: U57
- Modules: stock (remaining unread areas), stock_picking_batch
- Source revision: 19.0.post20260921 (Odoo 19 Community only)
- Date: 2026-10-02
- Scope notes: DELTA-FIRST — U08/U09 covered stock.move/picking/quant/warehouse; this unit covers lot/serial, forecast report, replenishment orderpoints, batch/wave, procurement rules, move lines (detailed operations), scrap, and config extensions. Source evidence only; RT flags for runtime unknowns.

---

## CAP-U57-01 Lot/Serial Number Tracking (stock.lot)

### D1 — Model Definition and Core Fields

The `stock.lot` model (formerly `stock.production.lot`) inherits `mail.thread` and `mail.activity.mixin`, providing chatter and activity tracking on every lot or serial number record. The model carries `_check_company_auto = True` ensuring multi-company field checks are enforced. The `name` field is a computed, stored, editable `Char` with `precompute=True`, backed by the product's sequence if one is configured. A trigram index is applied to `name` for efficient partial-match searches. A `ref` field provides an optional internal reference distinct from the manufacturer's lot number. The `product_id` Many2one field is restricted to products with `tracking != 'none'` and `is_storable = True`.

### D2 — Lot Name Generation and Serial Increment

The `_compute_name` method calls `product_id.lot_sequence_id.next_by_id()` when a sequence is assigned to the product; otherwise, `name` remains unset until the user provides it. The `generate_lot_names` class method takes a starting lot name and count, extracts the last numeric segment via regex, pads it, and returns a list of sequential names as dicts with key `lot_name`. The `_get_next_serial` class method searches the last existing lot for the product (across company boundaries) and calls `generate_lot_names(..., 2)[1]` to produce the next name.

### D3 — Uniqueness Constraint

The `_check_unique_lot` constraint uses `_read_group` with groupby `['company_id', 'product_id', 'name']` and `__count`. A cross-company check is performed when any lot has no `company_id`: the queryset is elevated to `sudo()` to bypass record rules, and duplicates between no-company and company-specific lots raise `ValidationError`.

### D4 — Historical Quantity Calculation

`_product_qty` applies `@api.depends_context` on `owner_id`, `package_id`, `to_date`, `location`, `warehouse_id`, and `allowed_company_ids`. When `to_date` is in the past, it subtracts in-moving lines and adds out-moving lines created after the date, providing a historical snapshot. Current quantity is a `_read_group` sum on `stock.quant` filtered by `lot_id` and location domain.

### D5 — Traceability: Delivery Lookup

`_find_delivery_ids_by_lot_iterative` builds a BFS-style traversal. It iterates a queue of lot IDs, searching `stock.move.line` for done outgoing lines. Lines with `produce_line_ids` represent manufactured outputs (produce lines); these add child lots to the queue via `produce_line_ids.lot_id`. Lines without `produce_line_ids` (barren lines) contribute `picking_id` directly. A `parent_map` propagates picking IDs from child lots back to parent lots.

### D6 — Single Location Tracking and Relocation

`_compute_single_location` filters `quant_ids` where `quantity > 0` and sets `location_id` only when all positive quants share exactly one location; otherwise False. The inverse `_set_single_location` calls `quants.move_quants(location_dest_id=..., message="Lot/Serial Number Relocated")` and handles the `unpack` flag if the lot's package contains other quants.

### D7 — Write Protections

The `write` override prevents changing `company_id` if the lot resides in a location owned by a different company. It also prevents changing `product_id` if `stock.move.line` records already exist for the lot on the old product, to avoid stock inconsistencies.

### D8 — Partner Traceability (Search)

`_search_partner_ids` finds lots by searching `stock.move.line` for done outgoing lines (using `_get_outgoing_domain`) filtered by partner. The field `partner_ids` is computed as the partners of sorted delivery pickings by `date_done` descending.

---

## CAP-U57-02 Reorder Point / Orderpoint (stock.warehouse.orderpoint)

### D1 — Model Definition

`StockWarehouseOrderpoint` (`_name = 'stock.warehouse.orderpoint'`, `_description = "Minimum Inventory Rule"`) implements minimum stock rules. A SQL uniqueness constraint `_product_location_check` enforces that a single active replenishment rule exists per `(product_id, location_id, company_id)` triple.

### D2 — Trigger Modes

The `trigger` field selection is `[('auto', 'Auto'), ('manual', 'Manual')]` with default `'auto'`. Auto-triggered orderpoints are processed by the scheduler; manual ones are created by the replenishment report action or user interaction and are cleaned up after procurement.

### D3 — Min/Max Quantity Fields

`product_min_qty` is the stock level at or below which replenishment triggers. `product_max_qty` is the target replenishment level. `_compute_product_max_qty` auto-sets `product_max_qty = product_min_qty` if `product_max_qty < product_min_qty` or is zero. The `_check_min_max_qty` constraint raises `ValidationError` if min > max.

### D4 — Forecast and On-Hand Computation

`_compute_qty` batches orderpoints by context key (combining `location`, `to_date`), reads `qty_available` and `virtual_available` from `product.product` in bulk, then adds `_quantity_in_progress()` to the virtual qty. `qty_on_hand` is `qty_available`; `qty_forecast` is `virtual_available + qty_in_progress`.

### D5 — Qty to Order Computation

`_compute_qty_to_order` returns `qty_to_order_manual` if non-zero, else `qty_to_order_computed`. `_compute_qty_to_order_computed` calls `_get_qty_to_order` only when `qty_forecast < product_min_qty`. `_get_qty_to_order` computes: `max(product_min_qty, product_max_qty) - qty_forecast_with_visibility`, then rounds up via `_get_multiple_rounded_qty`.

### D6 — Replenishment UoM Rounding

`_get_multiple_rounded_qty` uses `replenishment_uom_id` (or the alternative from `_get_replenishment_multiple_alternative`) to convert `qty_to_order`, round up to 0 decimal places via `fields.Float.round(..., rounding_method="UP")`, and convert back to product UoM.

### D7 — Deadline Date Computation

`_compute_deadline_date` first checks if `qty_on_hand < product_min_qty` (immediate deadline = today). For remaining orderpoints it retrieves all confirmed/assigned moves up to `horizon_date`, accumulates quantities day by day, and finds the first date where `qty_on_hand_at_date < product_min_qty`, then subtracts `lead_days` to get the deadline.

### D8 — Lead Days Computation

`_compute_lead_days` calls `rule_ids._get_lead_days(product_id, **values)`, which sums `delay` on all delaying rules and adds `horizon_time`. The result feeds `lead_horizon_date = today + total_delay + horizon_time` and `lead_days = total_delay`.

### D9 — Procurement Context and Date

`_get_product_context` returns `{'location': location_id, 'to_date': datetime.combine(lead_horizon_date, time.max)}`. `_get_orderpoint_procurement_date` localises `datetime.combine(lead_horizon_date, time(12))` to the company partner timezone and converts to UTC.

### D10 — Procure Orderpoint Confirm

`_procure_orderpoint_confirm` processes orderpoints in batches of 1000. For each orderpoint with `qty_to_order > 0`, it builds a `Procurement` named tuple and calls `stock.rule.run(procurements, raise_user_error=False)` inside a `cr.savepoint()`. Failed procurements accumulate and log `mail.mail_activity_data_warning` activities on the product template. If `use_new_cursor=True`, commits each batch and closes the cursor.

### D11 — Orderpoint Action / Replenishment Report

`_get_orderpoint_action` scans products with `is_storable=True` and moves, computes `virtual_available` per product-location over lead horizon, subtracts `qty_in_progress` and existing `qty_to_order`, and creates manual orderpoints (as SUPERUSER) for products still negative. It removes previously auto-created orderpoints that have been fulfilled via `_unlink_processed_orderpoints`.

### D12 — Snooze

`snoozed_until` is a Date field. Writing `snoozed_until` on an auto-triggered orderpoint raises `UserError`; snooze is only permitted on manual orderpoints.

### D13 — Horizon Days

`get_horizon_days` returns the global horizon from context key `global_horizon_days`, else `company_id.horizon_days`, else `env.company.horizon_days`.

### D14 — Unwanted Replenish Warning

`_compute_unwanted_replenish` computes `after_replenish_qty = virtual_available + qty_to_order` and sets `unwanted_replenish = True` when `after_replenish_qty > product_max_qty`, alerting that the order would overshoot the maximum.

---

## CAP-U57-03 Procurement Rules (stock.rule)

### D1 — Rule Model and Action Field

`StockRule` (`_name = 'stock.rule'`, `_description = "Stock Rule"`) defines routing for procurement. `action` is a required Selection: `[('pull', 'Pull From'), ('push', 'Push To'), ('pull_push', 'Pull & Push')]`, defaulting to `'pull'`. Rules are ordered by `sequence, id`.

### D2 — Supply Method (procure_method)

`procure_method` selection: `make_to_stock` (take from stock), `make_to_order` (trigger another rule), `mts_else_mto` (take from stock; if unavailable, trigger another rule). `_run_pull` translates `mts_else_mto` to `make_to_stock` for the move values created.

### D3 — Auto Transparent vs Manual

The `auto` field: `[('manual', 'Manual Operation'), ('transparent', 'Automatic No Step Added')]`. In `_run_push`, `transparent` modifies the move's `location_dest_id` in place and calls `_push_apply()` recursively. `manual` copies the move and creates a new one chained via `move_dest_ids`.

### D4 — Push Rule Execution

`_run_push` computes `new_date = move.date + relativedelta(days=self.delay)`. For transparent mode: updates move's `location_dest_id` and move line destinations to putaway result. For manual mode: calls `_push_prepare_move_copy_values` and `move.sudo().copy(...)`. The new move gets `procure_method='make_to_order'`. If source location bypasses reservation, the method sets `procure_method='make_to_stock'`.

### D5 — Pull Rule Execution

`_run_pull` calls `_get_stock_move_values` for each procurement, groups moves by company, creates them as `SUPERUSER` via `stock.move.sudo().create(moves_values)`, and calls `_action_confirm()` on them. Procurements are sorted so negative quantities (refunds) are processed last.

### D6 — Stock Move Values from Rule

`_get_stock_move_values` builds a move values dict including: `location_id = rule.location_src_id`, `location_final_id = location_dest_id`, `date = date_planned - relativedelta(days=rule.delay)`, `orderpoint_id`, `route_ids` (cleared then re-linked), `procurement_values` (serialized via `_serialize_procurement_values`). When `location_dest_from_rule=True`, `location_dest_id` is taken from the rule rather than from the picking type.

### D7 — Lead Days Accumulation

`_get_lead_days` iterates self (all rules in a chain), sums `delay` for pull/pull_push rules, then adds `global_horizon_days` from the orderpoint context. Returns `(delays_dict, delay_description)` where `delays_dict` contains keys `total_delay` and `horizon_time`.

### D8 — Rule Lookup: `_get_rule`

`_get_rule` walks the location hierarchy from `location_id` to root. Calls `_search_rule_for_warehouses` once to build a dict `(location_dest_id, route_id) -> {warehouse_id -> rule}`. Then iterates from `location_id` upward, checking product routes, category routes, and warehouse routes in priority order. An inter-company location shortcut is handled via `_check_intercomp_location`.

### D9 — Rule Search Hierarchy

`_search_rule` first tries `route_ids` specified in the procurement, then `packaging_uom_id.package_type_id.route_ids`, then `product.route_ids | category.total_route_ids`, then `warehouse.route_ids`, returning the first matching active rule ordered by `route_sequence, sequence`.

### D10 — Scheduler Tasks

`_run_scheduler_tasks` performs three steps: (1) compute and confirm auto-trigger orderpoints (`_compute_qty_to_order_computed`, `_compute_deadline_date`, `_procure_orderpoint_confirm`); (2) assign confirmed moves in batches of 1000 ordered by `reservation_date, priority desc, date asc`; (3) merge duplicate quants via `_quant_tasks`. With `use_new_cursor=True`, commits after each step and logs progress.

### D11 — Procurement Exception Handling

`ProcurementException` is raised inside `run` when rule lookup fails or `_run_*` raises it. `run` collects all errors and raises either `UserError` (when `raise_user_error=True`) or `ProcurementException` with all accumulated `procurement_exceptions`. The method dispatches to `_run_pull`, `_run_push`, or other `_run_<action>` methods via `getattr`.

### D12 — Procurement NamedTuple

`Procurement` is a `NamedTuple` with fields: `product_id`, `product_qty`, `product_uom`, `location_id`, `name`, `origin`, `company_id`, `values` (dict). The `values` dict carries route_ids, date_planned, warehouse_id, orderpoint_id, and custom fields from `_get_custom_move_fields`.

### D13 — Push Rule Lookup

`_get_push_rule` walks up the location hierarchy from `location_dest_id`. At each level it searches rules with `action in ('push', 'pull_push')` and `location_src_id = location`. An optional `domain` in `values` is applied additionally.

### D14 — Scheduler Entry Point and Domain

`run_scheduler` wraps `_run_scheduler_tasks` in a try/except, logging errors. `_get_orderpoint_domain` returns `[('trigger', '=', 'auto'), ('product_id.active', '=', True)]` with optional company filter.

---

## CAP-U57-04 Move Lines — Detailed Operations (stock.move.line)

### D1 — Model and Key Fields

`StockMoveLine` (`_name = 'stock.move.line'`, `_description = "Product Moves (Stock Move Line)"`) is ordered by `result_package_id desc, id`. Key fields: `quantity` (computed from `quant_id` selection, stored), `quantity_product_uom` (computed from `quantity` in product UoM), `picked` (Boolean, auto-True when move is done or context `auto_pick_move_lines`), `lot_id` (Many2one `stock.lot`), `lot_name` (Char for new-lot creation during validation), `result_package_id` (destination package).

### D2 — Database Index

A partial index `_free_reservation_index` on `(id, company_id, product_id, lot_id, location_id, owner_id, package_id)` WHERE state NOT IN ('cancel','done') AND quantity_product_uom > 0 AND picked IS NOT TRUE is defined directly on the model class to optimise free-reservation queries.

### D3 — Lot/Product Constraint

`_check_lot_product` constraint raises `ValidationError` when `lot_id.product_id != line.product_id`, preventing a lot from being used on the wrong product's move line.

### D4 — Serial Number Onchange

`_onchange_serial_number` auto-sets `quantity = 1` for serial-tracked products when a lot is selected. It warns if the same `lot_name` appears more than once in sibling move lines (Counter check). For existing `lot_id` selections, it calls `stock.quant._check_serial_number` and, if a recommended location is returned, auto-corrects `location_id`.

### D5 — Putaway Strategy Application

`_apply_putaway_strategy` groups move lines by `result_package_id.outermost_package_id`. For packages with a `package_type_id`, a single best location is computed. For packages without a type, each move line gets a putaway location, but if more than one location results, all lines fall back to the move's `location_dest_id`. For unpacked lines, each line independently gets its putaway location.

### D6 — Action Done: Lot Creation and Quant Movement

`_action_done` first validates rounding on `quantity`. For tracked products without `lot_id`, it collects `lot_name` values and searches existing lots; missing ones are flagged for `_create_and_assign_production_lot`. Lines with zero quantity and not inventory adjustments are unlinked. The method then builds a `quants_cache` for all product/location combinations, iterates move lines calling `_synchronize_quant(-qty, location_id, "reserved")` then `_synchronize_quant(-qty, location_id)` (available), then `_synchronize_quant(qty, location_dest_id, package=result_package_id, in_date=...)`. If `available_qty < 0`, `_free_reservation` is called.

### D7 — Quant Synchronization

`_synchronize_quant` calls either `_update_available_quantity` (action="available") or `_update_reserved_quantity` (action="reserved") on `stock.quant`. When `available_qty < 0` and a lot is set, it attempts to compensate from untracked quants by transferring the shortfall from lot_id=False to the current lot.

### D8 — Free Reservation

`_free_reservation` finds other non-done move lines reserving the same product/lot/location/owner/package combination (excluding self and `ml_ids_to_ignore`). It cancels them, resetting `procure_method='make_to_stock'` and clearing `move_orig_ids`, then calls `_action_assign` on affected moves.

### D9 — Lot Creation from lot_name

`_create_and_assign_production_lot` deduplicates lots by `(product_id, lot_name)` key, creates `stock.lot` records in bulk, and writes `lot_id` back to the move lines. For lot-tracked (not serial) products, multiple move lines with the same `lot_name` share one lot record.

### D10 — Quantity Update Logic on Create

In `create`, if `quantity_product_uom > 0` and reservation is required (product is storable and location does not bypass reservation), `_update_reserved_quantity` is called immediately. If the move line is created in `done` state, quant updates are performed directly.

### D11 — Write Restrictions

`write` prevents changing `product_id` on non-draft lines. For changes to `lot_id`, `location_id`, `location_dest_id`, `package_id`, `result_package_id`, `owner_id`, or `product_uom_id` on reserved lines, it first unreserves the old characteristics then re-reserves the new ones. On done-line edits, it reverses and re-applies quant movements, calling `_action_assign` on downstream moves.

### D12 — Put in Pack

`_put_in_pack` creates a `stock.package` (with optional `package_type_id`) and writes `result_package_id` to the move lines. A single-line pack also applies putaway to `location_dest_id`. `_post_put_in_pack_hook` auto-prints a label if `picking_type_id.auto_print_package_label` is set.

### D13 — Aggregated Product Quantities

`_get_aggregated_product_quantities` aggregates done quantities across move lines by a composite key of `product_id + display_name + description + uom_id + packaging_uom_id`. Backorder move lines are included. Empty moves (confirmed, no lines, non-zero demand) contribute to `qty_ordered` but show `quantity=False`.

---

## CAP-U57-05 Replenishment Wizards

### D1 — Product Replenish Wizard (product.replenish)

`ProductReplenish` (`_name = 'product.replenish'`, inherits `stock.replenish.mixin`) is a transient wizard. `launch_replenishment` calls `stock.rule.run([Procurement(...)])` with the warehouse's `lot_stock_id` as the destination location. `_get_date_planned` sums `rule.delay` across all rules in `route_id.rule_ids` and adds to `fields.Datetime.now()`. Notifications are displayed linking to the created picking.

### D2 — Replenish Mixin (stock.replenish.mixin)

Abstract model providing `route_id` Many2one `stock.route` and `allowed_route_ids`. `_get_allowed_route_domain` excludes inter-company routes and requires `rule_ids.location_dest_id.warehouse_id != False`. The domain combines `product_selectable=True` with warehouse-specific resupply route IDs.

### D3 — Replenishment Info Wizard (stock.replenishment.info)

Transient model displaying supplier and lead-day information for an orderpoint. `based_on` offers seven historical periods (7 days, 30 days, 3 months, 12 months, same-month-last-year variants, last-year-quarter). `_compute_json_replenishment_graph` computes `daily_demand = (quantity_out - quantity_returned) / period_days * (percent_factor / 100)`. Graph data shows min/max lines and sawtooth demand curve over projected ordering periods.

### D4 — Replenishment Option (stock.replenishment.option)

Transient model per resupply route. `free_qty` reads `product_id.free_qty` with `location=warehouse.lot_stock_id`. `lead_time` calls `stock.rule._get_rule(product, location, {route_ids, warehouse_id})` and retrieves `total_delay`. `_compute_warning_message` warns when `free_qty < qty_to_order`. `order_all` and `order_avbl` set the orderpoint's route and optionally cap the order to available qty.

---

## CAP-U57-06 Batch and Wave Transfers (stock.picking.batch)

### D1 — Model Definition and Wave Flag

`StockPickingBatch` (`_name = 'stock.picking.batch'`, `_description = "Batch Transfer"`) in module `stock_picking_batch` (separate from core `stock`). `is_wave` Boolean distinguishes a wave transfer from a batch transfer. The sequence code used for naming is `'picking.wave'` when `is_wave=True`, else `'picking.batch'`.

### D2 — State Machine

States: `draft`, `in_progress`, `done`, `cancelled`. `_compute_state` automatically transitions to `cancel` when all pickings are cancelled; to `done` when all non-cancelled pickings are done. `action_confirm` calls `picking_ids.action_confirm()` and sets state to `in_progress`.

### D3 — Allowed Pickings

`_compute_allowed_picking_ids` searches pickings in states `['waiting', 'confirmed', 'assigned']` (plus `'draft'` if the batch is in draft), matching `company_id` and optionally `picking_type_id`.

### D4 — Validate Batch (action_done)

`action_done` filters active pickings (not done/cancel). Empty waiting pickings (no quantity) are detached. Remaining pickings are sanity-checked as a batch (`separate_pickings=False`). `button_validate()` is called with context `skip_sanity_check=True` and `pickings_to_detach`. Progress messages are posted to each picking's chatter referencing the batch.

### D5 — Auto-Merge Constraints

`_is_picking_auto_mergeable` checks `batch_max_lines` (move count limit) and `batch_max_pickings` (picking count limit) from the operation type. `_is_line_auto_mergeable` checks both limits for wave building.

### D6 — Merge Action

`action_merge` verifies all selected batches share the same `picking_type_id`, same `is_wave` value, and same state (neither done nor cancelled). The earliest-scheduled batch provides the merged vals. Pickings and move lines are merged into the first batch; other batches are unlinked.

### D7 — Scheduled Date Propagation

`onchange_scheduled_date` propagates the batch's `scheduled_date` to all `picking_ids.scheduled_date`. `_compute_scheduled_date` computes the minimum scheduled date across all pickings.

### D8 — Properties Support

`properties` is a `fields.Properties` backed by `picking_type_id.batch_properties_definition`, allowing configurable custom fields per operation type.

---

## CAP-U57-07 Scrap Management (stock.scrap)

### D1 — Scrap Model

`StockScrap` (`_name = 'stock.scrap'`, inherits `mail.thread`) manages scrapping of consumed or damaged goods. `location_id` must have `usage='internal'`; `scrap_location_id` must have `usage='inventory'`. State: `draft` → `done`.

### D2 — Scrap Execution

`do_scrap` generates a reference via `ir.sequence` code `'stock.scrap'`, calls `_create_scrap_move()` then `move.with_context(is_scrap=True)._action_done()`. After marking `state='done'`, if `should_replenish=True`, calls `do_replenish()`.

### D3 — Optional Replenishment after Scrap

`do_replenish` runs a `Procurement` via `stock.rule.run(...)` for the scrapped `product_id`, `scrap_qty`, `product_uom_id`, and `location_id` (the source location, not the scrap location), allowing automatic reorder after a scrap event.

### D4 — Scrap Reason Tags

`StockScrapReasonTag` (`_name = 'stock.scrap.reason.tag'`) provides a tagging system for categorising scrap reasons with a name (translatable), sequence, and color. A unique constraint `_name_uniq` prevents duplicate tag names.

### D5 — Availability Check

`action_validate` calls `check_available_qty`, which reads `product_id.qty_available` in the strict location/lot/package/owner context. If `available_qty < scrap_qty`, it opens `stock.warn.insufficient.qty.scrap` wizard rather than silently proceeding.

---

## CAP-U57-08 Configuration Settings Extensions (stock)

### D1 — Lot/Serial Number Settings

`group_stock_production_lot` (`implied_group='stock.group_production_lot'`) enables the Lots & Serial Numbers feature globally. Disabling it raises `UserError` if any products still have `tracking != 'none'`. `module_product_expiry` enables expiration date tracking (best before, removal, end of life, alert dates) on lots. `group_stock_lot_print_gs1` enables GS1 barcode printing. `group_lot_on_delivery_slip` shows lots on delivery slips.

### D2 — Batch Transfer Settings

`module_stock_picking_batch` is a Boolean that enables the `stock_picking_batch` addon (Batch, Wave & Cluster Transfers). This is an addon-installation flag, not a group-based toggle.

### D3 — Routing and Location Settings

`group_stock_adv_location` (`implied_group='stock.group_adv_location'`) enables multi-step routes. `group_stock_multi_locations` (`implied_group='stock.group_stock_multi_locations'`) enables storage locations. Enabling multi-step routes auto-enables multi-locations; disabling multi-locations disables multi-step routes. When multi-locations is enabled, internal operation types are activated for all warehouses.

### D4 — Replenish on Order (MTO)

`replenish_on_order` computes as `route_warehouse0_mto.active`. Setting it activates or deactivates the MTO route for all warehouses.

### D5 — Horizon Days

`horizon_days` is a `Float` relayed from `company_id.horizon_days`. This setting controls how many days ahead the scheduler considers when evaluating demand for replenishment.

### D6 — Stock Forecasted Report Model

`stock.forecasted_product_product` (abstract model at `stock/report/stock_forecasted.py:12`) provides `_get_product_quantities` exposing `virtual_available`, `free_qty`, `incoming_qty`, `outgoing_qty` per product. `_get_product_leadtime` retrieves lead time via `product._get_rules_from_location(location)._get_lead_days(product)`. This model is used by the Replenishment Report action.

---

## CLAIMS TABLE

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U57-C001 | CAP-U57-01-D1 | stock/models/stock_lot.py:25 | `_name = 'stock.lot'` | FACT | always | — | The lot/serial model is named `stock.lot` with `_check_company_auto = True` | N-U57-001 |
| VDR-U57-C002 | CAP-U57-01-D1 | stock/models/stock_lot.py:42 | `name = fields.Char('Lot/Serial Number', required=True, compute='_compute_name', store=True, readonly=False` | FACT | always | — | The `name` field is computed from a product sequence, stored and editable, with a trigram index | N-U57-001 |
| VDR-U57-C003 | CAP-U57-01-D2 | stock/models/stock_lot.py:66-69 | `lot.name = lot.product_id.lot_sequence_id.next_by_id()` | FACT | product has lot_sequence_id | — | `_compute_name` auto-generates a name from the product's linked sequence when available | N-U57-001 |
| VDR-U57-C004 | CAP-U57-01-D2 | stock/models/stock_lot.py:72-90 | `def generate_lot_names(self, first_lot, count):` | FACT | always | — | `generate_lot_names` extracts the last numeric segment via regex, pads it, and returns a list of `count` sequential lot name dicts | N-U57-001 |
| VDR-U57-C005 | CAP-U57-01-D2 | stock/models/stock_lot.py:92-101 | `def _get_next_serial(self, company, product):` | FACT | product.tracking != 'none' | — | `_get_next_serial` searches last serial (order `id DESC`) and calls `generate_lot_names(last.name, 2)[1]` to return the next incremented name | N-U57-001 |
| VDR-U57-C006 | CAP-U57-01-D3 | stock/models/stock_lot.py:103-126 | `def _check_unique_lot(self):` | FACT | always | — | `_check_unique_lot` uses `_read_group` with `__count` and validates uniqueness across company boundaries using sudo when any lot has no company | N-U57-001 |
| VDR-U57-C007 | CAP-U57-01-D4 | stock/models/stock_lot.py:210-235 | `def _product_qty(self):` | FACT | to_date in context | — | When `to_date` is in the past, `_product_qty` adjusts current quant quantity by subtracting in-moves and adding out-moves that occurred after that date | N-U57-001 |
| VDR-U57-C008 | CAP-U57-01-D5 | stock/models/stock_lot.py:369-431 | `def _find_delivery_ids_by_lot_iterative(self):` | FACT | always | — | The iterative delivery lookup uses BFS via a queue, building a `parent_map` to propagate picking IDs from produce lines (manufactured children) upward to parent lots | N-U57-002 |
| VDR-U57-C009 | CAP-U57-01-D6 | stock/models/stock_lot.py:168-178 | `def _compute_single_location(self):` | FACT | always | — | `_compute_single_location` sets `location_id` only when all positive quants for the lot share exactly one location; otherwise it is False | N-U57-001 |
| VDR-U57-C010 | CAP-U57-01-D6 | stock/models/stock_lot.py:173-179 | `def _set_single_location(self):` | FACT | len(quants.location_id) == 1 | — | The inverse `_set_single_location` calls `move_quants` with `message="Lot/Serial Number Relocated"` and sets `unpack` if the lot's package contains other quants | N-U57-001 |
| VDR-U57-C011 | CAP-U57-01-D7 | stock/models/stock_lot.py:187-199 | `def write(self, vals):` | FACT | 'product_id' in vals | — | `write` raises `UserError` if `product_id` is changed and `stock.move.line` records exist for the lot, preventing stock inconsistency | N-U57-001 |
| VDR-U57-C012 | CAP-U57-02-D1 | stock/models/stock_orderpoint.py:22-25 | """ Defines Minimum stock rules. | FACT | always | — | The orderpoint model is `stock.warehouse.orderpoint` with a SQL unique constraint on `(product_id, location_id, company_id)` | N-U57-003 |
| VDR-U57-C013 | CAP-U57-02-D2 | stock/models/stock_orderpoint.py:31-33 | trigger = fields.Selection | FACT | always | — | `trigger` is either `auto` (processed by scheduler) or `manual` (created by replenishment report or user) | N-U57-003 |
| VDR-U57-C014 | CAP-U57-02-D3 | stock/models/stock_orderpoint.py:56-58 | product_min_qty = fields.Float | FACT | always | — | `product_min_qty` is the stock level at or below which replenishment is triggered | N-U57-003 |
| VDR-U57-C015 | CAP-U57-02-D3 | stock/models/stock_orderpoint.py:207-211 | `def _compute_product_max_qty(self):` | FACT | always | — | `_compute_product_max_qty` auto-corrects `product_max_qty` to equal `product_min_qty` when it is lower or zero | N-U57-003 |
| VDR-U57-C016 | CAP-U57-02-D4 | stock/models/stock_orderpoint.py:372-392 | `def _compute_qty(self):` | FACT | always | — | `_compute_qty` groups orderpoints by context (location + to_date), batch-reads `qty_available` and `virtual_available`, and adds `_quantity_in_progress()` to the forecast | N-U57-003 |
| VDR-U57-C017 | CAP-U57-02-D5 | stock/models/stock_orderpoint.py:461-476 | def _get_qty_to_order | FACT | qty_forecast < product_min_qty | — | `_get_qty_to_order` returns `max(product_min_qty, product_max_qty) - qty_forecast_with_visibility`, rounded up to replenishment UoM multiples | N-U57-003 |
| VDR-U57-C018 | CAP-U57-02-D5 | stock/models/stock_orderpoint.py:393-396 | `def _compute_qty_to_order(self):` | FACT | always | — | `_compute_qty_to_order` returns `qty_to_order_manual` when non-zero, otherwise returns `qty_to_order_computed` | N-U57-003 |
| VDR-U57-C019 | CAP-U57-02-D6 | stock/models/stock_orderpoint.py:807-814 | `def _get_multiple_rounded_qty(self, qty_to_order):` | FACT | replenishment_uom_id set | — | `_get_multiple_rounded_qty` converts to the replenishment UoM, rounds UP to 0 decimal places, and converts back, enforcing minimum order multiples | N-U57-003 |
| VDR-U57-C020 | CAP-U57-02-D7 | stock/models/stock_orderpoint.py:123-178 | `def _compute_deadline_date(self):` | FACT | always | — | `_compute_deadline_date` immediately sets today's date when `qty_on_hand < product_min_qty`, then for others simulates daily qty changes against incoming and outgoing moves up to horizon | N-U57-003 |
| VDR-U57-C021 | CAP-U57-02-D7 | stock/models/stock_orderpoint.py:175-177 | `tentative_deadline = move_date - relativedelta.relativedelta(days=orderpoint.lead_days)` | FACT | qty drops below min | — | Deadline = first date qty drops below min minus `lead_days`, giving time to order before stockout | N-U57-003 |
| VDR-U57-C022 | CAP-U57-02-D8 | stock/models/stock_orderpoint.py:180-188 | `def _compute_lead_days(self):` | FACT | product_id and location_id set | — | `_compute_lead_days` calls `rule_ids._get_lead_days(product_id)` and sets `lead_horizon_date = today + total_delay + horizon_time` | N-U57-003 |
| VDR-U57-C023 | CAP-U57-02-D9 | stock/models/stock_orderpoint.py:484-490 | `def _get_product_context(self):` | FACT | always | — | `_get_product_context` returns `{'location': location_id, 'to_date': datetime.combine(lead_horizon_date, time.max)}` for horizon-aware forecast queries | N-U57-003 |
| VDR-U57-C024 | CAP-U57-02-D9 | stock/models/stock_orderpoint.py:798-799 | `def _get_orderpoint_procurement_date(self):` | FACT | always | — | Procurement date is `lead_horizon_date` at noon, localised to the company partner timezone and converted to UTC | N-U57-004 |
| VDR-U57-C025 | CAP-U57-02-D10 | stock/models/stock_orderpoint.py:712-793 | def _procure_orderpoint_confirm | FACT | always | — | Orderpoints are processed in batches of 1000; each batch uses a savepoint; failures log `mail_activity_data_warning` on the product template | N-U57-004 |
| VDR-U57-C026 | CAP-U57-02-D10 | stock/models/stock_orderpoint.py:743-746 | procurements.append | FACT | qty_to_order > 0 | — | A `Procurement` NamedTuple is created per qualifying orderpoint and passed to `stock.rule.run` | N-U57-004 |
| VDR-U57-C027 | CAP-U57-02-D11 | stock/models/stock_orderpoint.py:492-633 | `def _get_orderpoint_action(self):` | FACT | always | — | `_get_orderpoint_action` creates manual orderpoints as SUPERUSER for product-location pairs still negative after accounting for existing orders and orderpoint quantities | N-U57-004 |
| VDR-U57-C028 | CAP-U57-02-D12 | stock/models/stock_orderpoint.py:295-307 | def create(self, vals_list) | FACT | snoozed_until in vals | — | Writing `snoozed_until` raises `UserError` if any orderpoint in self has `trigger='auto'` | N-U57-003 |
| VDR-U57-C029 | CAP-U57-02-D13 | stock/models/stock_orderpoint.py:816-822 | `def get_horizon_days(self):` | FACT | always | — | `get_horizon_days` returns from context `global_horizon_days`, else `company_id.horizon_days`, else `env.company.horizon_days` | N-U57-003 |
| VDR-U57-C030 | CAP-U57-02-D14 | stock/models/stock_orderpoint.py:280-287 | `def _compute_unwanted_replenish(self):` | FACT | qty_to_order > 0 | — | `unwanted_replenish = True` when `virtual_available + qty_to_order > product_max_qty`, warning that the order would exceed the maximum | N-U57-003 |
| VDR-U57-C031 | CAP-U57-03-D1 | stock/models/stock_rule.py:42-47 | class StockRule(models.Model) | FACT | always | — | Procurement rules are ordered by `sequence, id`; the `action` field determines routing type: pull, push, or both | N-U57-005 |
| VDR-U57-C032 | CAP-U57-03-D2 | stock/models/stock_rule.py:78-85 | procure_method = fields.Selection | FACT | always | — | `mts_else_mto` makes stock take precedence; only triggers another rule when stock is insufficient | N-U57-005 |
| VDR-U57-C033 | CAP-U57-03-D3 | stock/models/stock_rule.py:104-109 | auto = fields.Selection | FACT | always | — | Transparent push rules modify the existing move's destination in place; manual push rules create a new chained move | N-U57-005 |
| VDR-U57-C034 | CAP-U57-03-D4 | stock/models/stock_rule.py:222-254 | `def _run_push(self, move):` | FACT | action in ('push','pull_push') | — | In transparent mode, `_run_push` updates `location_dest_id` and calls `_push_apply()` recursively to chain; in manual mode it copies the move with `procure_method='make_to_order'` | N-U57-005 |
| VDR-U57-C035 | CAP-U57-03-D5 | stock/models/stock_rule.py:289-318 | `def _run_pull(self, procurements):` | FACT | action in ('pull','pull_push') | — | `_run_pull` groups move values by company and creates moves as SUPERUSER via `stock.move.sudo().with_company(company_id).create(moves_values)` then confirms them | N-U57-005 |
| VDR-U57-C036 | CAP-U57-03-D6 | stock/models/stock_rule.py:326-387 | def _get_stock_move_values | FACT | always | — | `_get_stock_move_values` builds move fields including `date = date_planned - relativedelta(days=rule.delay)` and `location_final_id = location_dest_id` | N-U57-005 |
| VDR-U57-C037 | CAP-U57-03-D6 | stock/models/stock_rule.py:382-383 | if self.location_dest_from_rule | FACT | location_dest_from_rule=True | — | When `location_dest_from_rule` is True, the rule's own `location_dest_id` overrides the picking type's default destination | N-U57-005 |
| VDR-U57-C038 | CAP-U57-03-D7 | stock/models/stock_rule.py:412-444 | `def _get_lead_days(self, product, **values):` | FACT | always | — | `_get_lead_days` accumulates `delay` from all pull/pull_push rules in self, then adds `global_horizon_days` from the orderpoint context | N-U57-005 |
| VDR-U57-C039 | CAP-U57-03-D8 | stock/models/stock_rule.py:566-640 | `def _get_rule(self, product_id, location_id, values):` | FACT | always | — | `_get_rule` walks the location hierarchy upward, calling `_search_rule_for_warehouses` once and then extracting the best matching rule per location level | N-U57-005 |
| VDR-U57-C040 | CAP-U57-03-D9 | stock/models/stock_rule.py:539-564 | def _search_rule | FACT | always | — | Rule search priority: explicit `route_ids`, packaging UoM routes, product/category routes, then warehouse routes; first match returned ordered by `route_sequence, sequence` | N-U57-005 |
| VDR-U57-C041 | CAP-U57-03-D10 | stock/models/stock_rule.py:693-726 | def _run_scheduler_tasks | FACT | always | — | Scheduler runs three steps: compute/confirm orderpoints; assign confirmed moves in batches of 1000 ordered by `reservation_date, priority desc, date asc`; merge quants | N-U57-006 |
| VDR-U57-C042 | CAP-U57-03-D11 | stock/models/stock_rule.py:453-506 | `def run(self, procurements, raise_user_error=True):` | FACT | always | — | `run` collects all procurement errors and either raises `UserError` (single combined message) or `ProcurementException` with all individual tuples | N-U57-006 |
| VDR-U57-C043 | CAP-U57-03-D11 | stock/models/stock_rule.py:19-27 | `class ProcurementException(Exception):` | FACT | always | — | `ProcurementException.procurement_exceptions` is a list of `(Procurement, error_message)` tuples | N-U57-006 |
| VDR-U57-C044 | CAP-U57-03-D12 | stock/models/stock_rule.py:31-39 | `class Procurement(NamedTuple):` | FACT | always | — | `Procurement` is a NamedTuple with fields `product_id, product_qty, product_uom, location_id, name, origin, company_id, values` | N-U57-006 |
| VDR-U57-C045 | CAP-U57-03-D13 | stock/models/stock_rule.py:667-679 | `def _get_push_rule(self, product_id, location_dest_id, values):` | FACT | always | — | `_get_push_rule` walks up from `location_dest_id` searching for rules with `action in ('push','pull_push')` and matching `location_src_id` | N-U57-005 |
| VDR-U57-C046 | CAP-U57-03-D14 | stock/models/stock_rule.py:746-750 | `def _get_orderpoint_domain(self, company_id=False):` | FACT | always | — | Auto-trigger orderpoint domain: `trigger='auto'` AND `product_id.active=True` | N-U57-004 |
| VDR-U57-C047 | CAP-U57-04-D1 | stock/models/stock_move_line.py:15-19 | class StockMoveLine(models.Model) | FACT | always | — | Move lines are ordered by destination package descending then id; all detailed operations for a transfer are at this model level | N-U57-007 |
| VDR-U57-C048 | CAP-U57-04-D1 | stock/models/stock_move_line.py:37-43 | quantity = fields.Float | FACT | always | — | `quantity` is computed from `quant_id` when selected, then manually editable; `quantity_product_uom` is a stored compute in product UoM | N-U57-007 |
| VDR-U57-C049 | CAP-U57-04-D1 | stock/models/stock_move_line.py:43-44 | `picked = fields.Boolean('Picked', compute='_compute_picked', store=True, readonly=False, copy=False)` | FACT | always | — | `picked` is auto-set to True when the move is done or context `auto_pick_move_lines` is set | N-U57-007 |
| VDR-U57-C050 | CAP-U57-04-D2 | stock/models/stock_move_line.py:97-98 | _free_reservation_index | FACT | always | — | A partial DB index is defined on (id, company_id, product_id, lot_id, location_id, owner_id, package_id) WHERE state not in cancel/done AND quantity_product_uom > 0 AND picked IS NOT TRUE | N-U57-007 |
| VDR-U57-C051 | CAP-U57-04-D3 | stock/models/stock_move_line.py:172-179 | `def _check_lot_product(self):` | FACT | lot_id set | — | Constraint validates `lot_id.product_id == line.product_id`; mismatch raises `ValidationError` | N-U57-007 |
| VDR-U57-C052 | CAP-U57-04-D4 | stock/models/stock_move_line.py:198-240 | `def _onchange_serial_number(self):` | FACT | tracking='serial' | — | Auto-sets `quantity=1` for serial products; warns on duplicate serial in same picking; calls `_check_serial_number` and auto-corrects `location_id` if recommended | N-U57-007 |
| VDR-U57-C053 | CAP-U57-04-D5 | stock/models/stock_move_line.py:262-293 | `def _apply_putaway_strategy(self):` | FACT | move lines have result_package_id or not | — | For packages with type: one best putaway location for all lines; for packages without type: per-line putaway but collapses to move destination if more than one location results | N-U57-007 |
| VDR-U57-C054 | CAP-U57-04-D6 | stock/models/stock_move_line.py:595-715 | `def _action_done(self):` | FACT | always | — | `_action_done` validates rounding, enforces lot presence for tracked products, creates lots from `lot_name` via `_create_and_assign_production_lot`, then moves quants via `_synchronize_quant` | N-U57-007 |
| VDR-U57-C055 | CAP-U57-04-D6 | stock/models/stock_move_line.py:685-688 | ml_ids_to_ignore = OrderedSet() | FACT | always | — | A quants cache is built pre-action across all product/location pairs to reduce per-line DB queries during `_action_done` | N-U57-007 |
| VDR-U57-C056 | CAP-U57-04-D6 | stock/models/stock_move_line.py:699-700 | `available_qty, in_date = ml._synchronize_quant(-ml.quantity_product_uom, ml.location_id)` | FACT | always | — | The sequence is: (1) unreserve source, (2) decrement available at source, (3) increment available at destination with the `in_date` carried forward | N-U57-007 |
| VDR-U57-C057 | CAP-U57-04-D7 | stock/models/stock_move_line.py:716-736 | def _synchronize_quant | FACT | always | — | `_synchronize_quant` dispatches to `_update_available_quantity` or `_update_reserved_quantity`; negative available with a lot triggers compensation from untracked quants at same location | N-U57-007 |
| VDR-U57-C058 | CAP-U57-04-D8 | stock/models/stock_move_line.py:795-857 | def _free_reservation | FACT | available_qty < 0 | — | `_free_reservation` finds outdated reserved move lines sorted with current picking first, reduces or unlinks them, resets `procure_method='make_to_stock'`, and re-assigns freed moves | N-U57-007 |
| VDR-U57-C059 | CAP-U57-04-D9 | stock/models/stock_move_line.py:756-773 | `def _create_and_assign_production_lot(self):` | FACT | lot_name set, no lot_id | — | Deduplicates lots by `(product_id, lot_name)` key; lot-tracked lines sharing the same name reuse a single created lot record | N-U57-007 |
| VDR-U57-C060 | CAP-U57-04-D10 | stock/models/stock_move_line.py:346-427 | `def create(self, vals_list):` | FACT | always | — | On create, if the move line has no `move_id`, it searches for a linkable move; if none or picking is done, a new move is auto-created via `_prepare_stock_move_vals` | N-U57-007 |
| VDR-U57-C061 | CAP-U57-04-D11 | stock/models/stock_move_line.py:429-559 | `def write(self, vals):` | FACT | lot_id/location_id changes on reserved lines | — | Changes to reservation-impacting fields first unreserve the old combination then reserve the new one; done-line edits fully reverse and re-apply quant movements | N-U57-007 |
| VDR-U57-C062 | CAP-U57-04-D12 | stock/models/stock_move_line.py:1095-1117 | `def _put_in_pack(self, package_id=False, package_type_id=False, package_name=False):` | FACT | always | — | `_put_in_pack` creates a `stock.package` and applies putaway for the destination location when packing a single move line | N-U57-007 |
| VDR-U57-C063 | CAP-U57-04-D13 | stock/models/stock_move_line.py:885-977 | `def _get_aggregated_product_quantities(self, **kwargs):` | FACT | always | — | Aggregation groups by `product + display_name + description + uom + packaging_uom`; backorder lines are included; empty confirmed moves contribute to `qty_ordered` only | N-U57-007 |
| VDR-U57-C064 | CAP-U57-05-D1 | stock/wizard/product_replenish.py:91-117 | `def launch_replenishment(self):` | FACT | always | — | `launch_replenishment` creates a Procurement for `warehouse_id.lot_stock_id` as destination, runs `stock.rule.run`, and returns a notification with a link to the created picking | N-U57-008 |
| VDR-U57-C065 | CAP-U57-05-D1 | stock/wizard/product_replenish.py:84-89 | `def _get_date_planned(self, route_id, **kwargs):` | FACT | route_id set | — | `_get_date_planned` sums `rule.delay` across all rules in `route_id.rule_ids` and returns `now + sum_delay` | N-U57-008 |
| VDR-U57-C066 | CAP-U57-05-D2 | stock/models/stock_replenish_mixin.py:26-40 | `def _get_allowed_route_domain(self):` | FACT | always | — | Allowed routes must have `product_selectable=True`, must not include inter-company locations as source or destination, and must have a warehouse on the destination location | N-U57-008 |
| VDR-U57-C067 | CAP-U57-05-D3 | stock/wizard/stock_replenishment_info.py:16-20 | class StockReplenishmentInfo | FACT | always | — | `StockReplenishmentInfo` is a transient model linked to an orderpoint, providing lead-day and demand graph data | N-U57-008 |
| VDR-U57-C068 | CAP-U57-05-D3 | stock/wizard/stock_replenishment_info.py:29-44 | based_on = fields.Selection | FACT | always | — | Seven historical periods are available for demand estimation: 7 days, 30 days, 3 months, 12 months, same-month-last-year, next-month-last-year, last-year-quarter | N-U57-008 |
| VDR-U57-C069 | CAP-U57-05-D3 | stock/wizard/stock_replenishment_info.py:177 | `daily_demand = ((quantity_out - quantity_returned) / (date_to - date_from).days) * (replenishment_report.percent_factor / 100)` | FACT | always | — | Daily demand = (outgoing - returns) / days * (percent_factor / 100); adjustable by a percentage factor | N-U57-008 |
| VDR-U57-C070 | CAP-U57-05-D4 | stock/wizard/stock_replenishment_info.py:196-261 | `class StockReplenishmentOption(models.TransientModel):` | FACT | always | — | `StockReplenishmentOption` compares `free_qty` in the supplying warehouse against `qty_to_order` and warns when supply is insufficient | N-U57-008 |
| VDR-U57-C071 | CAP-U57-05-D4 | stock/wizard/stock_replenishment_info.py:254-257 | `def order_avbl(self):` | FACT | free_qty < qty_to_order | — | `order_avbl` sets both `route_id` and caps `qty_to_order` to `free_qty` on the orderpoint | N-U57-008 |
| VDR-U57-C072 | CAP-U57-06-D1 | stock_picking_batch/models/stock_picking_batch.py:9-13 | class StockPickingBatch(models.Model) | FACT | always | — | `stock.picking.batch` is defined in the separate `stock_picking_batch` Community module, not in the base `stock` module | N-U57-009 |
| VDR-U57-C073 | CAP-U57-06-D1 | stock_picking_batch/models/stock_picking_batch.py:60 | `is_wave = fields.Boolean('This batch is a wave')` | FACT | always | — | The `is_wave` Boolean field distinguishes wave transfers from batch transfers within the same model | N-U57-009 |
| VDR-U57-C074 | CAP-U57-06-D1 | stock_picking_batch/models/stock_picking_batch.py:185-186 | `sequence_code = 'picking.wave' if vals.get('is_wave') else 'picking.batch'` | FACT | on create | — | Naming uses sequence code `'picking.wave'` for waves, `'picking.batch'` for batches | N-U57-009 |
| VDR-U57-C075 | CAP-U57-06-D2 | stock_picking_batch/models/stock_picking_batch.py:40-46 | state = fields.Selection | FACT | always | — | Batch state transitions: draft → in_progress (via action_confirm), → done (auto when all pickings done), → cancelled | N-U57-009 |
| VDR-U57-C076 | CAP-U57-06-D2 | stock_picking_batch/models/stock_picking_batch.py:144-155 | `def _compute_state(self):` | FACT | always | — | All pickings cancelled → batch cancelled; all non-cancelled pickings done → batch done (auto-computed) | N-U57-009 |
| VDR-U57-C077 | CAP-U57-06-D3 | stock_picking_batch/models/stock_picking_batch.py:106-120 | `def _compute_allowed_picking_ids(self):` | FACT | always | — | Allowed pickings must be in `['waiting', 'confirmed', 'assigned']` (plus `'draft'` if batch is draft), matching company and optionally operation type | N-U57-009 |
| VDR-U57-C078 | CAP-U57-06-D4 | stock_picking_batch/models/stock_picking_batch.py:239-281 | `def action_done(self):` | FACT | always | — | `action_done` removes empty waiting pickings from the batch, runs sanity check across all remaining pickings as one, then calls `button_validate` with `skip_sanity_check=True` | N-U57-009 |
| VDR-U57-C079 | CAP-U57-06-D4 | stock_picking_batch/models/stock_picking_batch.py:255-256 | `pickings._sanity_check(separate_pickings=False)` | FACT | always | — | `separate_pickings=False` runs sanity check treating all pickings as a combined batch, not individually | N-U57-009 |
| VDR-U57-C080 | CAP-U57-06-D5 | stock_picking_batch/models/stock_picking_batch.py:449-457 | `def _is_picking_auto_mergeable(self, picking):` | FACT | always | — | `batch_max_lines` (from picking type) limits total move count; `batch_max_pickings` limits total picking count for auto-merge | N-U57-009 |
| VDR-U57-C081 | CAP-U57-06-D6 | stock_picking_batch/models/stock_picking_batch.py:326-361 | `def action_merge(self):` | FACT | at least 2 selected | — | `action_merge` enforces same operation type, same `is_wave` value, same state, and not done/cancelled; merges pickings into the earliest-scheduled batch | N-U57-009 |
| VDR-U57-C082 | CAP-U57-06-D7 | stock_picking_batch/models/stock_picking_batch.py:157-165 | @api.depends('picking_ids | FACT | scheduled_date changed | — | Changing batch `scheduled_date` propagates to all assigned pickings via onchange | N-U57-009 |
| VDR-U57-C083 | CAP-U57-06-D8 | stock_picking_batch/models/stock_picking_batch.py:66 | `properties = fields.Properties('Properties', definition='picking_type_id.batch_properties_definition', copy=True)` | FACT | always | — | Batch transfers support custom property fields defined per operation type | N-U57-009 |
| VDR-U57-C084 | CAP-U57-07-D1 | stock/models/stock_scrap.py:10-13 | class StockScrap(models.Model) | FACT | always | — | `stock.scrap` inherits only `mail.thread` (no activity mixin); `location_id` must have `usage='internal'`; `scrap_location_id` must have `usage='inventory'` | N-U57-010 |
| VDR-U57-C085 | CAP-U57-07-D2 | stock/models/stock_scrap.py:55 | `should_replenish = fields.Boolean(string='Replenish Quantities', help="Trigger replenishment for scrapped products")` | FACT | always | — | `should_replenish` Boolean controls whether a replenishment procurement is automatically triggered after scrap completion | N-U57-010 |
| VDR-U57-C086 | CAP-U57-07-D2 | stock/models/stock_scrap.py:152-163 | `def do_scrap(self):` | FACT | always | — | `do_scrap` gets a sequence reference, creates and executes a scrap move with context `is_scrap=True`, then conditionally calls `do_replenish()` | N-U57-010 |
| VDR-U57-C087 | CAP-U57-07-D3 | stock/models/stock_scrap.py:169-181 | `def do_replenish(self, values=False):` | FACT | should_replenish=True | — | `do_replenish` runs a Procurement for the scrapped product at the source location (not the scrap location), allowing reorder after loss | N-U57-010 |
| VDR-U57-C088 | CAP-U57-07-D4 | stock/models/stock_scrap.py:237-249 | `class StockScrapReasonTag(models.Model):` | FACT | always | — | `stock.scrap.reason.tag` provides tagging for scrap reasons; `name` has a unique constraint; ordered by `sequence, id` | N-U57-010 |
| VDR-U57-C089 | CAP-U57-07-D5 | stock/models/stock_scrap.py:193-208 | `def check_available_qty(self):` | FACT | product is storable | — | Before executing scrap, available qty is checked in the strict lot/package/owner context; insufficient qty triggers the warning wizard | N-U57-010 |
| VDR-U57-C090 | CAP-U57-08-D1 | stock/models/res_config_settings.py:12 | help="Track following | FACT | always | — | Expiry date tracking is a separately installable feature (`module_product_expiry`) not bundled in base stock | N-U57-011 |
| VDR-U57-C091 | CAP-U57-08-D1 | stock/models/res_config_settings.py:13-14 | group_stock_production_lot | FACT | always | — | Lots & Serial Numbers is a group-based feature; disabling raises `UserError` if tracked products still exist | N-U57-011 |
| VDR-U57-C092 | CAP-U57-08-D2 | stock/models/res_config_settings.py:28 | `module_stock_picking_batch = fields.Boolean("Batch, Wave & Cluster Transfers")` | FACT | always | — | Batch, Wave & Cluster Transfers is an addon-installation flag, not a group; requires the `stock_picking_batch` module | N-U57-011 |
| VDR-U57-C093 | CAP-U57-08-D3 | stock/models/res_config_settings.py:23-26 | group_stock_adv_location | FACT | always | — | Enabling multi-step routes auto-enables multi-locations; disabling multi-locations auto-disables multi-step routes | N-U57-011 |
| VDR-U57-C094 | CAP-U57-08-D4 | stock/models/res_config_settings.py:56 | `replenish_on_order = fields.Boolean("Replenish on Order (MTO)", compute='_compute_replenish_on_order', inverse='_inverse_replenish_on_order')` | FACT | always | — | `replenish_on_order` toggles the active state of the `stock.route_warehouse0_mto` route | N-U57-011 |
| VDR-U57-C095 | CAP-U57-08-D5 | stock/models/res_config_settings.py:59 | `horizon_days = fields.Float(related='company_id.horizon_days', readonly=False)` | FACT | always | — | `horizon_days` is a company-level setting controlling how far ahead the scheduler evaluates demand | N-U57-011 |
| VDR-U57-C096 | CAP-U57-08-D6 | stock/report/stock_forecasted.py:12 | `_name = 'stock.forecasted_product_product'` | FACT | always | — | The forecasted product report is an abstract model at `stock/report/stock_forecasted.py` providing demand breakdown | N-U57-012 |
| VDR-U57-C097 | CAP-U57-08-D6 | stock/report/stock_forecasted.py:69-87 | def _get_product_quantities | FACT | always | — | Report exposes `virtual_available`, `free_qty`, `incoming_qty`, `outgoing_qty` per product from `product.product` fields | N-U57-012 |
| VDR-U57-C098 | CAP-U57-08-D6 | stock/report/stock_forecasted.py:98-110 | def _get_product_leadtime | FACT | always | — | Lead time is retrieved per product via `product._get_rules_from_location(location)._get_lead_days(product)` | N-U57-012 |
| VDR-U57-C099 | CAP-U57-01-D8 | stock/models/stock_lot.py:265-291 | `def _search_partner_ids(self, operator, value):` | FACT | operator not in NEGATIVE_OPERATORS | — | `_search_partner_ids` searches done outgoing `stock.move.line` records for partner matches; symmetric `partner_ids` field uses `_find_delivery_ids_by_lot_iterative` | N-U57-002 |
| VDR-U57-C100 | CAP-U57-02-D1 | stock/models/stock_orderpoint.py:101-104 | _product_location_check = models.Constraint | FACT | always | — | SQL-level unique constraint on `(product_id, location_id, company_id)` prevents duplicate orderpoints | N-U57-003 |
| VDR-U57-C101 | CAP-U57-02-D11 | stock/models/stock_orderpoint.py:638-646 | `def _get_orderpoint_values(self, product, location):` | FACT | always | — | Auto-created manual orderpoints are initialised with `product_min_qty=0.0`, `product_max_qty=0.0`, `trigger='manual'` | N-U57-004 |
| VDR-U57-C102 | CAP-U57-03-D1 | stock/models/stock_rule.py:60-61 | active = fields.Boolean | FACT | always | — | Rules can be archived (active=False) without deletion | N-U57-005 |
| VDR-U57-C103 | CAP-U57-03-D6 | stock/models/stock_rule.py:370-374 | `'route_ids': [Command.clear()] + [Command.link(route.id) for route in values.get('route_ids', [])],` | FACT | always | — | Move values clear all existing route links and re-apply from procurement `route_ids` values | N-U57-005 |
| VDR-U57-C104 | CAP-U57-03-D6 | stock/models/stock_rule.py:389-410 | `def _serialize_procurement_values(self, values):` | FACT | always | — | Procurement values are serialized for storage: BaseModel instances become id lists; datetime/date become ISO strings | N-U57-005 |
| VDR-U57-C105 | CAP-U57-04-D6 | stock/models/stock_move_line.py:690-694 | # Prepare package | FACT | result_package_id set | — | Package history records are created before any quant movement unless context `ignore_dest_packages` is set | N-U57-007 |
| VDR-U57-C106 | CAP-U57-06-D2 | stock_picking_batch/models/stock_picking_batch.py:220-228 | `def action_confirm(self):` | FACT | always | — | `action_confirm` raises `UserError` if no pickings are assigned; then calls `picking_ids.action_confirm()` before setting `state='in_progress'` | N-U57-009 |
| VDR-U57-C107 | CAP-U57-02-D9 | stock/models/stock_orderpoint.py:692-709 | `def _prepare_procurement_values(self, date=False):` | FACT | always | — | Procurement values include `date_planned`, `date_order`, `date_deadline`, `warehouse_id`, `orderpoint_id`, and optional `reference_ids` from context origins | N-U57-004 |
| VDR-U57-C108 | CAP-U57-01-D2 | stock/models/stock_lot.py:128-133 | `def _check_create(self):` | FACT | active_picking_id in context | — | `_check_create` raises `UserError` if the active picking's operation type has `use_create_lots=False`, preventing lot creation from disallowed operations | N-U57-001 |
| VDR-U57-C109 | CAP-U57-04-D6 | stock/models/stock_move_line.py:665-674 | if ml_ids_tracked_without_lot | FACT | tracking != none and no lot | — | Tracked products without a lot/serial number at validation time raise `UserError` listing all offending product names | N-U57-007 |
| VDR-U57-C110 | CAP-U57-06-D4 | stock_picking_batch/models/stock_picking_batch.py:248-251 | `empty_waiting_pickings = self.mapped('picking_ids').filtered(lambda p: (p.state in ('waiting', 'confirmed') and has_no_quantity(p)) or (p.state == 'assigned' and is_empty(p)))` | FACT | always | — | Empty waiting/confirmed pickings and assigned empty pickings are automatically detached from the batch during `action_done` | N-U57-009 |
| VDR-U57-C111 | CAP-U57-02-D10 | stock/models/stock_orderpoint.py:363-365 | `self.filtered(lambda o: o.create_uid.id == SUPERUSER_ID and o.qty_to_order <= 0.0 and o.trigger == 'manual').unlink()` | FACT | after replenish | — | Auto-generated manual orderpoints (created by superuser) with zero qty to order are deleted after replenishment is executed | N-U57-004 |
| VDR-U57-C112 | CAP-U57-03-D10 | stock/models/stock_rule.py:709-715 | domain = self._get_moves_to_assign_domain | FACT | always | — | Move assignment in the scheduler processes 1000 moves per chunk, ordered by reservation_date, priority desc, date asc | N-U57-006 |
| VDR-U57-C113 | CAP-U57-03-D10 | stock/models/stock_rule.py:721-722 | `self.env['stock.quant']._quant_tasks()` | FACT | always | RT | `_quant_tasks` merges duplicate quants; specific merge logic is in `stock.quant` (RT: internal quant merge not further read here) | N-U57-006 |
| VDR-U57-C114 | CAP-U57-04-D11 | stock/models/stock_move_line.py:562-588 | @api.ondelete(at_uninstall=False) | FACT | always | — | Unlinking a reserved move line calls `_update_reserved_quantity` to unreserve, then recomputes parent move states; packages are de-destinated if no longer linked to active pickings | N-U57-007 |
| VDR-U57-C115 | CAP-U57-04-D1 | stock/models/stock_move_line.py:51-52 | `lot_name = fields.Char('Lot/Serial Number Name')` | FACT | always | — | `lot_name` is an unsaved Char field allowing users to type a new lot name during validation; it is converted to a `lot_id` record by `_create_and_assign_production_lot` | N-U57-007 |
| VDR-U57-C116 | CAP-U57-01-D1 | stock/models/stock_lot.py:44-48 | product_id = fields.Many2one | FACT | always | — | Lot product domain restricts to storable, tracked products only | N-U57-001 |
| VDR-U57-C117 | CAP-U57-01-D1 | stock/models/stock_lot.py:60-63 | `lot_properties = fields.Properties('Properties', definition='product_id.lot_properties_definition', copy=True)` | FACT | always | — | Lots support custom property fields backed by the product template's `lot_properties_definition` | N-U57-001 |
| VDR-U57-C118 | CAP-U57-02-D3 | stock/models/stock_orderpoint.py:63-66 | allowed_replenishment_uom_ids | FACT | always | — | `replenishment_uom_id` enforces minimum order multiples; if unset, no rounding is applied | N-U57-003 |
| VDR-U57-C119 | CAP-U57-03-D4 | stock/models/stock_rule.py:92 | `delay = fields.Integer('Lead Time', default=0, help="The expected date of the created transfer will be computed based on this lead time.")` | FACT | always | — | Rule `delay` is in days; `_get_push_new_date` adds it to the move date; `_get_stock_move_values` subtracts it from `date_planned` | N-U57-005 |
| VDR-U57-C120 | CAP-U57-03-D5 | stock/models/stock_rule.py:246-253 | `new_move = move.sudo().copy(new_move_vals)` | FACT | auto='manual' push | — | Manual push creates a move copy as sudo with `procure_method='make_to_order'` and chains via `move_dest_ids` unless source location bypasses reservation | N-U57-005 |
| VDR-U57-C121 | CAP-U57-04-D5 | stock/models/stock_move_line.py:253-260 | `def _onchange_putaway_location(self):` | FACT | multi-locations enabled | — | When multi-locations is active and the current destination matches the default, putaway strategy is re-applied on UoM or quantity change | N-U57-007 |
| VDR-U57-C122 | CAP-U57-05-D1 | stock/wizard/product_replenish.py:130-137 | `def _prepare_run_values(self):` | FACT | always | — | `_prepare_run_values` passes `warehouse_id`, `route_ids`, `date_planned`, and `force_uom=True` to the procurement | N-U57-008 |
| VDR-U57-C123 | CAP-U57-06-D3 | stock_picking_batch/models/stock_picking_batch.py:81-103 | `def _compute_estimated_shipping_capacity(self):` | FACT | always | — | Estimated shipping weight and volume aggregate package type dimensions and product weight/volume from move lines, with packages counted once | N-U57-009 |
| VDR-U57-C124 | CAP-U57-07-D1 | stock/models/stock_scrap.py:43-46 | scrap_location_id = fields.Many2one | FACT | always | — | Scrap destination is restricted to `usage='inventory'` locations only | N-U57-010 |
| VDR-U57-C125 | CAP-U57-08-D1 | stock/models/res_config_settings.py:135-137 | if not self.group_stock_production_lot | FACT | disabling group_stock_production_lot | — | Disabling lot/serial tracking raises `UserError` when any product still has `tracking != 'none'` | N-U57-011 |
| VDR-U57-C126 | CAP-U57-02-D4 | stock/models/stock_orderpoint.py:385-392 | products_qty = | FACT | always | — | `qty_forecast` adds procurement-in-progress quantities (from `_quantity_in_progress`) to the product's `virtual_available` | N-U57-003 |
| VDR-U57-C127 | CAP-U57-02-D10 | stock/models/stock_orderpoint.py:748-750 | try | FACT | always | — | Procurement run uses a savepoint so a single orderpoint failure does not roll back the entire batch | N-U57-004 |
| VDR-U57-C128 | CAP-U57-03-D8 | stock/models/stock_rule.py:641-646 | `def _check_intercomp_location(self, locations):` | FACT | transit location in hierarchy | — | `_check_intercomp_location` detects transit → inter-company routing and adds the Customer location to the rule domain to avoid duplicating cross-company rules | N-U57-005 |
| VDR-U57-C129 | CAP-U57-04-D2 | stock/models/stock_move_line.py:182-185 | `def _check_positive_quantity(self):` | FACT | always | — | Constraint prevents any negative quantity on move lines | N-U57-007 |
| VDR-U57-C130 | CAP-U57-04-D6 | stock/models/stock_move_line.py:617-624 | uom_qty = ml.product_uom_id.round | FACT | always | — | Rounding precision is validated at action_done: quantity must match the UoM rounding exactly | N-U57-007 |
| VDR-U57-C131 | CAP-U57-01-D5 | stock/models/stock_lot.py:380-406 | # Prefetch the lines | FACT | manufacturing produce lines exist | — | `_find_delivery_ids_by_lot_iterative` builds `parent_map` mapping child (produced) lot IDs to parent (consuming) lot IDs for upward delivery propagation | N-U57-002 |
| VDR-U57-C132 | CAP-U57-04-D12 | stock/models/stock_move_line.py:1119-1129 | `def _post_put_in_pack_hook(self, package):` | FACT | auto_print_package_label set | — | After packing, `_post_put_in_pack_hook` auto-prints a PDF or ZPL label if `picking_type_id.auto_print_package_label` is True | N-U57-007 |
| VDR-U57-C133 | CAP-U57-06-D6 | stock_picking_batch/models/stock_picking_batch.py:340-347 | target_batch = self[:1] | FACT | merge action | — | Batch merge: all pickings and move lines are assigned to the first (target) batch; other batch records are hard-deleted | N-U57-009 |
| VDR-U57-C134 | CAP-U57-05-D3 | stock/wizard/stock_replenishment_info.py:173-177 | if replenishment_report.product_max_qty | FACT | always | — | Average stock in the replenishment graph is the midpoint between min and max quantities | N-U57-008 |
| VDR-U57-C135 | CAP-U57-07-D1 | stock/models/stock_scrap.py:70-86 | `def _compute_location_id(self):` | FACT | always | — | Scrap `location_id` defaults to the company's first warehouse `lot_stock_id`; if the picking is done, defaults to `picking_id.location_dest_id`, else `picking_id.location_id` | N-U57-010 |
| VDR-U57-C136 | CAP-U57-04-D10 | stock/models/stock_move_line.py:407-426 | for ml in mls | FACT | state='done' on create | — | When a move line is created directly in done state, quant movements are applied immediately in the create method | N-U57-007 |
| VDR-U57-C137 | CAP-U57-03-D3 | stock/models/stock_rule.py:104-109 | auto = fields.Selection | FACT | always | — | The default push step type is manual operation; transparent steps add no visible operation | N-U57-005 |
| VDR-U57-C138 | CAP-U57-02-D12 | stock/models/stock_orderpoint.py:678-690 | `def _unlink_processed_orderpoints(self):` | FACT | autovacuum | — | `_unlink_processed_orderpoints` is decorated with `@api.autovacuum` and removes superuser-created manual orderpoints with `qty_to_order <= 0` | N-U57-004 |
| VDR-U57-C139 | CAP-U57-01-D4 | stock/models/stock_lot.py:237-263 | `def _search_product_qty(self, operator, value):` | FACT | search on product_qty | — | `_search_product_qty` aggregates quant quantities by lot, applies the Python operator, and handles zero-quantity lots via `include_zero = op(0.0, value)` | N-U57-001 |
| VDR-U57-C140 | CAP-U57-04-D11 | stock/models/stock_move_line.py:514-529 | `if 'date' not in vals and ('product_uom_id' in vals or 'quantity' in vals or vals.get('picked', False)):` | FACT | quantity increases on picked lines | — | The move line `date` is auto-updated to `Datetime.now()` when quantity or UoM changes on a picked line, or when `picked` becomes True | N-U57-007 |
| VDR-U57-C141 | CAP-U57-06-D5 | stock_picking_batch/models/stock_picking_batch.py:459-468 | `def _is_line_auto_mergeable(self, num_of_moves=False, num_of_pickings=False, weight=False):` | FACT | wave building | — | `_is_line_auto_mergeable` checks move and picking count limits for wave auto-building (a superset of batch auto-merge logic) | N-U57-009 |
| VDR-U57-C142 | CAP-U57-08-D3 | stock/models/res_config_settings.py:110-112 | `warehouse_obj.with_context(active_test=True).search([]).int_type_id.active = True` | FACT | enabling multi-locations | — | Enabling multi-location activates internal operation types for all warehouses (previously deactivated when multi-locations was off) | N-U57-011 |
| VDR-U57-C143 | CAP-U57-03-D2 | stock/models/stock_rule.py:306-307 | if rule.procure_method == 'mts_else_mto | FACT | mts_else_mto | — | `_run_pull` initially treats `mts_else_mto` as `make_to_stock`; MTO fallback occurs when move assignment fails (separate logic in `_action_confirm`) | N-U57-005 |
| VDR-U57-C144 | CAP-U57-04-D13 | stock/models/stock_move_line.py:1156-1176 | `def _get_lines_and_packages_to_pack(self, picked_first=True):` | FACT | always | — | When `picked_first=True`, only picked move lines are packed; unpicked lines are excluded while at least one picked line exists | N-U57-007 |
| VDR-U57-C145 | CAP-U57-07-D5 | stock/models/stock_scrap.py:211-234 | `def action_validate(self):` | FACT | always | — | `action_validate` gates on `check_available_qty`; if insufficient, returns the `stock.warn.insufficient.qty.scrap` wizard with default qty | N-U57-010 |
| VDR-U57-C146 | CAP-U57-01-D3 | stock/models/stock_lot.py:108-119 | if any(not lot.company_id for lot in self) | FACT | cross-company lots | — | When checking lot uniqueness involving no-company lots, the method elevates to sudo to bypass record rules and check across all companies | N-U57-001 |
| VDR-U57-C147 | CAP-U57-02-D11 | stock/models/stock_orderpoint.py:619-621 | `orderpoint.qty_forecast += product_qty` | FACT | existing orderpoint for product-location | — | When an existing orderpoint already covers the product-location, its `qty_forecast` is updated rather than creating a duplicate | N-U57-004 |
| VDR-U57-C148 | CAP-U57-03-D6 | stock/models/stock_rule.py:344-352 | # when create chained | FACT | inter-warehouse chained moves | — | For chained inter-warehouse moves through transit, the destination warehouse's partner is assigned to both the new move and the origin warehouse's partner to the destination move | N-U57-005 |
| VDR-U57-C149 | CAP-U57-04-D6 | stock/models/stock_move_line.py:708-709 | if not self.env.context.get | FACT | result_package_id set | — | After quant movements, `_apply_dest_to_package` is called on all destination packages to update their location | N-U57-007 |
| VDR-U57-C150 | CAP-U57-05-D3 | stock/wizard/stock_replenishment_info.py:50-56 | `def _compute_wh_replenishment_options(self):` | FACT | resupply_route_ids on warehouse | — | `wh_replenishment_option_ids` creates `StockReplenishmentOption` records for each warehouse resupply route, sorted by `free_qty` descending to show best supply option first | N-U57-008 |
| VDR-U57-C151 | CAP-U57-04-D6 | stock/models/stock_move_line.py:649-662 | for (product, company) | FACT | use_create_lots=True | — | During validation, existing lots are looked up by name before creating new ones, preventing duplicates | N-U57-007 |
| VDR-U57-C152 | CAP-U57-06-D4 | stock_picking_batch/models/stock_picking_batch.py:267-279 | for picking in pickings | FACT | always | — | Each picking validated via a batch gets a chatter message referencing the batch transfer name and ID | N-U57-009 |
| VDR-U57-C153 | CAP-U57-02-D4 | stock/models/stock_orderpoint.py:673-676 | def _quantity_in_progress(self) | FACT | base stock module | — | In base stock, `_quantity_in_progress` returns zero for all orderpoints; it is overridden in `purchase` and `mrp` to include pending POs/MOs | N-U57-003 |
| VDR-U57-C154 | CAP-U57-03-D11 | stock/models/stock_rule.py:495-502 | for action, procurements | FACT | always | — | `run` dispatches to `_run_pull`, `_run_push`, or custom `_run_<action>` methods via dynamic `getattr`; unknown actions are logged as errors | N-U57-006 |
| VDR-U57-C155 | CAP-U57-01-D6 | stock/models/stock_lot.py:174-178 | quants = self.quant_ids.filtered | FACT | multiple locations | — | Attempting to relocate a lot with stock in more than one location raises `UserError`; the user must first consolidate the stock | N-U57-001 |
| VDR-U57-C156 | CAP-U57-08-D1 | stock/models/res_config_settings.py:15-17 | group_stock_lot_print_gs1 | FACT | always | — | GS1 barcode printing for lots is a separate group-based feature toggle | N-U57-011 |
| VDR-U57-C157 | CAP-U57-04-D7 | stock/models/stock_move_line.py:728-735 | if available_qty < 0 and lot | FACT | available_qty < 0 and lot set | — | Negative quants on a lot trigger compensation: untracked available qty is consumed and re-attributed to the lot | N-U57-007 |
| VDR-U57-C158 | CAP-U57-02-D3 | stock/models/stock_orderpoint.py:213-218 | @api.depends('route_id | FACT | buy route active | — | When a buy rule is present, seller purchase UoMs are added to the allowed replenishment UoM options | N-U57-003 |
| VDR-U57-C159 | CAP-U57-07-D1 | stock/models/stock_scrap.py:125-150 | `def _prepare_move_values(self):` | FACT | always | — | Scrap move has `picked=True` from creation; the move line is embedded inline with `quantity=scrap_qty` and lot/package/owner context | N-U57-010 |
| VDR-U57-C160 | CAP-U57-04-D12 | stock/models/stock_move_line.py:1131-1154 | def action_put_in_pack | FACT | always | — | `action_put_in_pack` first processes `move_lines_to_pack` (lines without result_package), then `packages_to_pack` (existing packages without an outer pack), chaining calls if needed | N-U57-007 |
