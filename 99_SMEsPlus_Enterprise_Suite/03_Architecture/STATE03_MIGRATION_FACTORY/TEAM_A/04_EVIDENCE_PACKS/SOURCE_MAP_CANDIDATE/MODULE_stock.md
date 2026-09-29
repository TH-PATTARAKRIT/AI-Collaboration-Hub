# Source Map (candidate) — `stock`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `stock` |
| Display name | Inventory |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d5ae42d03f531579` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/stock/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `product`, `barcodes_gs1_nomenclature`, `digest`
- Direct dependents in 300-module list (7): `mrp`, `product_expiry`, `project_stock`, `stock_account`, `stock_maintenance`, `stock_picking_batch`, `stock_sms`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (4): `l10n_din5008_stock`, `l10n_ec_stock`, `l10n_in_stock`, `l10n_tr_nilvera_edispatch`
- Custom / third-party modules that declare a dependency (name — license only) (19): `scgl_product_image` — no-license, `delivery_split` — AGPL-3, `cr_effective_date_entries` — AGPL-3, `d_product_brand_stock` — OPL-1, `scgl_inventory_lot_filter` — LGPL-3, `19_bhpro_master_data` — OPL-1, `bh_purchase_receipt_all` — LGPL-3, `product_category_filter` — AGPL-3, `sale_job_type` — LGPL-3, `bh_generate_serial_lots` — LGPL-3, `stock_picking_reference_no` — LGPL-3, `import_bridge_axis` — OPL-1

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Manage your stock and logistics activities
- Inventory of user-facing artifacts (counts): menu items 42, views 129, window actions 52, server actions 21, reports 21, mail templates 1, scheduled jobs 1, wizards 23, web routes 1
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (51): `stock.inventory.conflict` (Conflict in Inventory); `product.replenish` (Product Replenish); `stock.orderpoint.snooze` (Snooze Orderpoint); `stock.quantity.history` (Stock Quantity History); `stock.backorder.confirmation.line` (Backorder Confirmation Line); `stock.backorder.confirmation` (Backorder Confirmation); `stock.warn.insufficient.qty` (Warn Insufficient Quantity); `stock.warn.insufficient.qty.scrap` (Warn Insufficient Scrap Quantity); `stock.package.destination` (Stock Package Destination); `stock.inventory.warning` (Inventory Adjustment Warning); `picking.label.type` (Choose whether to print product or lot/sn labels); `stock.return.picking.line` (Return Picking Line); `stock.return.picking` (Return Picking); `stock.put.in.pack` (Put In Pack Wizard); `stock.request.count` (Stock Request an Inventory Count); `stock.replenishment.info` (Stock supplier replenishment information); `stock.replenishment.option` (Stock warehouse replenishment option); `stock.rules.report` (Stock Rules report); `stock.inventory.adjustment.name` (Inventory Adjustment Reference / Reason); `stock.quant.relocate` (Stock Quantity Relocation); `lot.label.layout` (Choose the sheet layout to print lot labels); `stock.location` (Inventory Locations); `stock.route` (Inventory Routes); `stock.package` (Package); `stock.warehouse` (Warehouse) … (+26)
- Objects extended from other modules (14): `product.label.layout`, `ir.actions.report`, `mail.thread`, `res.company`, `mail.activity.mixin`, `barcode.rule`, `res.users`, `product.product`, `product.template`, `product.category`, `uom.uom`, `res.config.settings`, `product.catalog.mixin`, `res.partner`
- Company-dependent settings introduced: 5 field(s); company-consistency auto-check declared on 14 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `product.replenish` ← Community: `mrp`, `purchase_stock`; open-license custom/third-party scanned: —
- `stock.warn.insufficient.qty` ← Community: `mrp`, `repair`; open-license custom/third-party scanned: —
- `picking.label.type` ← Community: `mrp`; open-license custom/third-party scanned: —
- `stock.return.picking.line` ← Community: `mrp_subcontracting`, `sale_stock`, `stock_account`; open-license custom/third-party scanned: —
- `stock.return.picking` ← Community: `mrp_subcontracting`, `purchase_stock`, `sale_stock`, `stock_delivery`; open-license custom/third-party scanned: —
- `stock.put.in.pack` ← Community: `stock_delivery`; open-license custom/third-party scanned: —
- `stock.replenishment.info` ← Community: `mrp`, `purchase_stock`; open-license custom/third-party scanned: —
- `stock.replenishment.option` ← Community: `purchase_stock`; open-license custom/third-party scanned: —
- `stock.rules.report` ← Community: `sale_stock`; open-license custom/third-party scanned: —
- `stock.inventory.adjustment.name` ← Community: `stock_account`; open-license custom/third-party scanned: —
- `stock.location` ← Community: `mrp_subcontracting`, `stock_account`, `stock_maintenance`; open-license custom/third-party scanned: —
- `stock.route` ← Community: `mrp`, `purchase_stock`, `sale_stock`, `stock_delivery`; open-license custom/third-party scanned: —
- `stock.package` ← Community: `stock_delivery`; open-license custom/third-party scanned: —
- `stock.warehouse` ← Community: `mrp`, `mrp_subcontracting`, `mrp_subcontracting_dropshipping`, `point_of_sale`, `purchase_stock`, `repair`, `stock_fleet`, `stock_picking_batch`, `website_sale_collect`; open-license custom/third-party scanned: —
- `stock.replenish.mixin` ← Community: `mrp`, `mrp_subcontracting_dropshipping`, `purchase_stock`, `stock_dropshipping`; open-license custom/third-party scanned: —
- `stock.scrap` ← Community: `mrp`; open-license custom/third-party scanned: `scgl_inventory_lot_filter`, `smesplus_inventory_lot_filter`
- `stock.move.line` ← Community: `mrp`, `mrp_subcontracting`, `product_expiry`, `repair`, `sale_mrp`, `sale_stock`, `stock_account`, `stock_delivery`, `stock_picking_batch`; open-license custom/third-party scanned: `courier_type`, `purchase_request`, `scgl_inventory_lot_filter`, `smesplus_inventory_lot_filter`
- `stock.quant` ← Community: `mrp`, `mrp_subcontracting`, `product_expiry`, `stock_account`; open-license custom/third-party scanned: `courier_type`
- `stock.move` ← Community: `l10n_in_ewaybill_stock`, `l10n_in_purchase_stock`, `l10n_in_sale_stock`, `l10n_in_stock`, `mrp`, `mrp_account`, `mrp_repair`, `mrp_subcontracting`, `mrp_subcontracting_account`, `mrp_subcontracting_dropshipping` … (+20); open-license custom/third-party scanned: `delivery_split`, `order_line_sequence`, `purchase_request`
- `stock.reference` ← Community: `mrp`, `point_of_sale`, `purchase_stock`, `sale_stock`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `product.label.layout`, `ir.actions.report`, `mail.thread`, `res.company`, `mail.activity.mixin`, `barcode.rule`, `res.users`, `product.product`, `product.template`, `product.category`, `uom.uom`, `res.config.settings`, `product.catalog.mixin`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: `stock.scrap` → ['draft', 'done']; `stock.move` → ['draft', 'waiting', 'confirmed', 'partially_available', 'assigned', 'done', 'cancel']; `stock.picking` → ['draft', 'waiting', 'confirmed', 'assigned', 'done', 'cancel']; `report.stock.quantity` → ['forecast', 'in', 'out']
- Validation: 11 declarative constraint method(s), 16 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Procurement: run scheduler every 1 days
- Security: groups declared 17 (`group_stock_user`, `group_stock_manager`, `group_stock_multi_locations`, `group_stock_multi_warehouses`, `group_production_lot`, `group_stock_lot_print_gs1` … (+11)); record rules 16 (of which company-scoped by text 16); access rows 77

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 172 of 173 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note — module `stock` (Inventory)

- Source revision: `19.0.post20260921` (Odoo 19 Community). Pointers are `module/path:LINE` relative to the `odoo/addons` root.
- Skeleton: `/Users/admin/STATE03_RESTRICTED_LOCAL/sourcemap/stock.json`. Read-only study; no code copied, Odoo not run.
- Manifest: application, depends on `product`, `barcodes_gs1_nomenclature`, `digest` (stock/__manifest__.py:10-11). Marker legend: CORE = always on; OPT = needs a setting/group or extra module; COND = depends on data/config.
- Note: `(TEST)` = derived from the module's own test files, not from production logic.

## 1. Capabilities by business area

### 1.1 Warehouses (CORE)
- A warehouse bundles a company, a stock-holding location, a top "virtual" location, a short code (max 5 characters), default routes and step counts (stock/models/stock_warehouse.py:24-70).
- Receipts can run in 1, 2 or 3 steps (receive-and-store; receive then store; receive, quality control, store). Deliveries can run in 1, 2 or 3 steps (deliver; pick then deliver; pick, pack, deliver) (stock/models/stock_warehouse.py:56-67). Default is 1-step in and 1-step out.
- Changing step counts creates or switches on input / quality / output / packing locations and operation types (stock/models/stock_warehouse.py:186-201, 634-675).
- Warehouse name and code must be unique (stock/models/stock_warehouse.py:91-99). Resupply routes between warehouses can be generated (stock/models/stock_warehouse.py:702-740). OPT: the multi-warehouse group is switched on/off automatically depending on whether any company has more than one active warehouse (stock/models/stock_warehouse.py:322-338).

### 1.2 Locations (CORE; hierarchy UI is OPT)
- Location types: vendor, virtual (view), internal, customer, inventory loss, production, transit (stock/models/stock_location.py:32-46). Only internal and transit locations carry counted stock; a "view" location cannot hold or be the source/target of stock (stock/models/stock_quant.py:605-609).
- A location with an empty company is shared across companies (stock/models/stock_location.py:57-59; record rule includes empty company — stock/security/stock_security.xml:103-107).
- Vendor, customer, inventory-loss and production locations never reserve stock ("bypass reservation") (stock/models/stock_location.py:411-413).
- Only one location in any parent/child line can be flagged "Replenishments" and only internal locations qualify (stock/models/stock_location.py:181-193).
- A location cannot be an inventory-loss (scrap) location if a manufacturing operation type delivers into it (stock/models/stock_location.py:195-199).
- The shipped inter-company transit location is protected from deletion (archive only) and is inactive until a second company exists (stock/models/stock_location.py:201-205; stock/data/stock_data.xml:34-39; stock/models/res_company.py:181-208).
- Storage locations UI (create/edit locations) is OPT via group "Manage Multiple Stock Locations" / setting "Storage Locations" (stock/models/res_config_settings.py:46; stock/security/stock_security.xml:26).

### 1.3 Operation types (CORE)
- Kinds: receipt, delivery, internal transfer (stock/models/stock_picking.py:42). Each has default source/destination, sequence prefix, return operation type, reservation method, backorder policy and print/label automation options (stock/models/stock_picking.py:33-140).
- Reservation method: at confirmation, manual, or "before scheduled date" with a day offset (stock/models/stock_picking.py:69-73); hidden for receipts (stock/models/stock_picking.py:249-253).
- Backorder policy per type: ask / always / never (stock/models/stock_picking.py:127-133).
- Lot creation / existing-lot use flags per type; defaults: receipts create lots, deliveries use existing lots (stock/models/stock_picking.py:47-59, 289-301).
- Shipping policy ("as soon as possible" vs "when all products are ready") is inherited from the operation type onto each transfer (stock/models/stock_picking.py:151, 571-575, 720-722).

### 1.4 Transfers (pickings) and moves (CORE)
- A transfer is a header over one or more moves; its state is computed from move states, never set directly (stock/models/stock_picking.py:816-863).
- A move states demand (planned quantity), source/destination, supply method (from stock vs trigger another rule), and links to preceding/following moves (stock/models/stock_move.py:56-64, 131-138).
- Move lines are the detailed, per-lot/package/owner/location records that hold reserved-then-done quantity; they are the only records that change stock (stock/models/stock_move_line.py:595-714).
- Return wizard creates a reverse transfer from a Done transfer; only Done transfers can be returned (stock/models/stock_picking.py:2134-2137; stock/wizard/stock_picking_return.py:107-131, 161-187).
- Exchange (return + new outgoing) is available from the same wizard (stock/wizard/stock_picking_return.py:189-260).

### 1.5 Quants and reservation (CORE)
- Quant = current on-hand quantity and reserved quantity for one product at one location, split by lot, package and owner (stock/models/stock_quant.py:60-135).
- Only products with "Track Inventory" (storable) may have quants (stock/models/stock_quant.py:582-585; stock/models/product.py:839-841).
- Reservation flow is in section 2.3.

### 1.6 Lots / serials / packages
- Product tracking: none, by lot, by unique serial (stock/models/product.py:856-862). Lot/serial UI requires group "Manage Lots / Serial Numbers" (OPT: setting "Lots & Serial Numbers" — stock/models/res_config_settings.py:13-14). Turning the setting off is blocked while any product is tracked (stock/models/res_config_settings.py:135-137).
- Lot name unique per product and company, and also against company-less lots (stock/models/stock_lot.py:103-126).
- Expiry/FEFO dates are OPT via extra module `product_expiry` (stock/models/res_config_settings.py:11; product_expiry/models/stock_quant.py:25-28).
- Packages are a new hierarchical model `stock.package` (packages can nest; also package types) (stock/models/stock_package.py:16-27). OPT: setting "Packages" (stock/models/res_config_settings.py:19-20). Unpack moves contents back to loose quants (stock/models/stock_package.py:316-325).
- Package must not be split across locations within one transfer (stock/models/stock_move.py:2280-2292).

### 1.7 Routes, rules, procurement, replenishment
- Rules: pull, push, or both; supply method: take from stock / trigger another rule / take from stock else trigger another rule; lead time; auto vs manual push step (stock/models/stock_rule.py:53-95).
- Rule search: walks up the destination location tree; prefers route explicitly on the request, then packaging routes, then product / product-category routes, then warehouse routes (stock/models/stock_rule.py:567-641).
- Failure to find a rule raises an error naming the product and location (stock/models/stock_rule.py:481-486).
- Push rules apply after a move is done or when chained; rules can carry a push-applicability filter (stock/models/stock_move.py:1214-1250).
- OPT: multi-step routes (setting "Multi-Step Routes" requires storage locations) (stock/models/res_config_settings.py:23-24, 87-90). OPT: MTO route ("Replenish on Order") can be toggled by the setting (stock/models/res_config_settings.py:56-69).
- Reordering rules (min/max): one per product+location+company; min must not exceed max; trigger auto or manual; multiple-of rounding; snooze (stock/models/stock_orderpoint.py:21-105, 252-256; stock/wizard/stock_orderpoint_snooze.py).
- Quantity to order = max(min,max) minus forecast (incl. lead-time visibility and in-progress supply), only when forecast is below min (stock/models/stock_orderpoint.py:461-476).
- Manual replenishment suggestions are generated per replenish-location for products with negative forecast (stock/models/stock_orderpoint.py:492-560). "Replenish" wizard exists for a single product (stock/wizard/product_replenish.py).

### 1.8 Putaway and removal (CORE with OPT inputs)
- Putaway rules match by package type, product, category; more specific rules win (package type > product > same category > any category) (stock/models/stock_location.py:308-315).
- Storage categories limit capacity by weight, product quantity, package count and "only empty / only same product" policy (stock/models/stock_location.py:418-461). OPT: needs storage locations setting.
- Removal strategies: FIFO, LIFO, closest location, least packages; FEFO added by `product_expiry`. Product-category strategy overrides location strategy; default FIFO (stock/data/stock_data.xml:4-20; stock/models/stock_quant.py:618-628, 741-748).
- Putaway is applied to move lines right after reservation (stock/models/stock_move.py:2185; stock/models/stock_move_line.py:262-293).

### 1.9 Scrap (CORE)
- Scrap creates a done move from an internal location to an inventory-loss location and marks itself done; optionally triggers replenishment (stock/models/stock_scrap.py:152-163, 165-176).
- Product must be a consumable/storable type item (stock/models/stock_scrap.py:22-24). Scrap reason tags exist (stock/models/stock_scrap.py:237-249).

### 1.10 Inventory adjustments / counts (CORE)
- Counts are entered on the quant (counted quantity, difference, assigned user, next count date) then applied (stock/models/stock_quant.py:97-135, 433-451).
- Schedule: per-location cyclic frequency, else company annual month/day (stock/models/stock_location.py:378-409; stock/models/res_company.py:24-43).

### 1.11 Backorders (CORE)
- See 2.2 and 3.1.

### 1.12 Barcode-free flows (CORE)
- All flows above work without scanner; barcode app is OPT `stock_barcode` (setting names the module; the module folder was not found in this addons tree — stock/models/res_config_settings.py:29). Barcode patterns are data-only (stock/data/default_barcode_patterns.xml).
- Delivery methods, batch/wave, dropshipping, SMS, dispatch are OPT modules named in settings (stock/models/res_config_settings.py:28-55).

## 2. Business objects and lifecycle

### 2.1 Move states
Draft ("New") -> Waiting Another Move / Waiting -> Partially Available -> Available (Assigned) -> Done; Cancelled from any non-done state (stock/models/stock_move.py:107-120).
- Confirm: draft moves become "Waiting Another Move" if they have a preceding move or are supply-method "trigger another rule"; otherwise "Waiting" (stock/models/stock_move.py:1688-1760). Trigger-another-rule moves create procurement requests at confirm.
- Negative demand on a move flips it into a return (swaps locations, negates quantity) (stock/models/stock_move.py:1754-1775).
- Assign: after confirm the move is reserved if the location bypasses reservation, the operation type reserves at confirmation, or its reservation date has arrived (stock/models/stock_move.py:1972-1973).
- Done: needs the "picked" flag and positive quantity; moves that are not picked and have zero quantity are cancelled (empty demand) or, if not cancel_backorder, split into a backorder (stock/models/stock_move.py:2249-2318).
- Cancel: refused for Done moves except inventory-loss moves; unreserves; propagates cancel to next moves only if the rule says so and all siblings are cancelled (stock/models/stock_move.py:2189-2229).
- Setting quantity or "picked" on a move is the "done quantity" concept of v19; there is no separate "quantity done" field (stock/models/stock_move.py:121-126, 281-292, 404-483).

### 2.2 Transfer states (computed)
Draft, Waiting Another Operation, Waiting, Ready, Done, Cancelled (stock/models/stock_picking.py:570-590).
- Draft if no moves or any move is draft; Cancelled if all moves cancelled; Done if all moves are done/cancelled (except: all-done-are-scrap plus a cancelled non-scrap move -> Cancelled) (stock/models/stock_picking.py:838-849).
- Otherwise state follows the most relevant move state; with policy "when all products are ready" any partial move keeps the transfer Waiting; with "as soon as possible" partial availability makes it Ready (stock/models/stock_picking.py:850-863; stock/models/stock_move.py:1411-1449).
- If the source location bypasses reservation and all moves take from stock, the transfer is Ready (stock/models/stock_picking.py:851-853).
- Reference is unique per company (stock/models/stock_picking.py:710-713).
- Validate button: confirms drafts; for draft transfers with zero quantity, quantities are set to demand (v19 has no "immediate transfer" wizard); sanity checks; backorder wizard if needed; then done; autoprint and reception report follow (stock/models/stock_picking.py:1420-1481).
- Done actions: assign follow-up moves that were waiting on incoming/internal receipts, optional inter-company auto-unpack, optional confirmation email (stock/models/stock_picking.py:1263-1312).
- Backorder: unfinished moves move to a new transfer linked to the original; reserved automatically if that type reserves at confirmation (stock/models/stock_picking.py:1589-1624).
- Split transfer action: requires some but not all quantity done, and done qty must not exceed demand (stock/models/stock_picking.py:1482-1494).

### 2.3 Quant reservation logic
- Available = on-hand minus reserved, floored at zero when not allowing negative (stock/models/stock_quant.py:793-832).
- Reserve: collect quants under the location tree in removal-strategy order, reserve up to available, honoring rounding of the move unit; serials must be whole units; offsets against negative quants at same lot/package/owner; full-packaging reserve only for categories set to "full" (stock/models/stock_quant.py:834-914).
- Move-level: creates move lines per reserved quant (grouped) or updates an existing line (stock/models/stock_move.py:1917-1962). Chained moves reserve only what predecessors delivered (stock/models/stock_move.py:2135-2168).
- Priority order for batch assign: priority, deadline, date, id (stock/models/stock_picking.py:1208-1216).
- Unreserve removes unpicked lines; picked lines are protected; Done moves error out (stock/models/stock_move.py:1023-1049).
- Cleanup task re-syncs reserved quantities to open move lines and removes zero quants (stock/models/stock_quant.py:1123-1176, 1225-1229).
- On Done, reserved is released, quantity leaves the source quant and enters the destination quant; if the source goes negative, other reservations on that stock are freed (stock/models/stock_move_line.py:706-716).

### 2.4 Adjustment application
- Application creates one inventory-loss counterpart move per quant (positive difference = loss location -> stock; negative = stock -> loss location), marks picked and done, resets the count fields, and records last inventory date and next count date (stock/models/stock_quant.py:996-1036, 1253-1291).
- If the quant on-hand changed since the count ("outdated"), a conflict wizard asks to keep counted quantity or keep the difference (stock/models/stock_quant.py:198-203, 433-441; stock/wizard/stock_inventory_conflict.py:14-22).
- Inverse of the on-hand field on product creates adjustments too (stock/models/stock_quant.py:225-237, 997-1002).
- Making a product storable for the first time rebuilds quants from move history (stock/models/product.py:1129-1160).

## 3. Validations, automation, security

### 3.1 Validations and constraints
- Validate empty transfer: refused ("cannot validate an empty transfer"); zero quantities: refused; missing lot/serial on tracked lines: refused (stock/models/stock_picking.py:1373-1415).
- Lot required only when the operation type is set to create or use lots; if both are off, tracked products may move without lot (stock/models/stock_move_line.py:612-628).
- Lot creation on an operation type that forbids it is blocked (stock/models/stock_lot.py:128-133).
- Move line quantity cannot be negative; must match unit-of-measure rounding at validation (stock/models/stock_move_line.py:182-186, 603-611, 642-645).
- Serial number: a serial can exist only once across the tree of locations; duplicates raise an error at done (stock/models/stock_quant.py:587-603; stock/models/stock_move.py:2242-2247).
- Lot must belong to same product as the line/quant (stock/models/stock_move_line.py:172-180; stock/models/stock_quant.py:611-616).
- Negative stock policy: no company-level setting or hard block exists in this module. Outgoing moves can be forced through; the source quant may go negative, and later receipts/adjustments offset it (stock/models/stock_move_line.py:706-716; (TEST) stock/tests/test_warehouse.py:138-215). Insufficient-quantity warning appears only in scrap and is a wizard that can be confirmed (stock/models/stock_scrap.py:196-234; stock/wizard/stock_warn_insufficient_qty.py:8-48). A general "prevent negative stock" rule: UNKNOWN — EVIDENCE INSUFFICIENT (no global switch found in `stock`).
- Done moves: cannot delete their lines, cannot change UoM or product; cannot be cancelled (except inventory-loss moves) — return instead (stock/models/stock_move_line.py:563-570; stock/models/stock_move.py:2190-2192, 845-846).
- Scrap: quantity must be non-zero; done scraps cannot be deleted; warns when scrap exceeds on-hand at chosen location/lot/package/owner (stock/models/stock_scrap.py:211-234, 121-123).
- Orderpoint: min <= max, one per product/location/company (stock/models/stock_orderpoint.py:101-105, 252-256).
- Barcode: location barcode unique per company; cyclic frequency non-negative (stock/models/stock_location.py:93-99).
- Unlinking a quant by a non-manager is refused; manager delete zeros it via adjustment (stock/models/stock_quant.py:363-369).
- Company change of a product blocked if moves/quants in another company exist (stock/models/product.py:1129-1148).

### 3.2 Automation
- Cron "Procurement: run scheduler": daily, runs as superuser (stock/data/stock_sequence_data.xml:45-57). The scheduler does: (1) auto-trigger reordering rules, (2) assign confirmed/partial moves whose reservation date arrived or at-confirm types, in chunks of 1000, (3) merge duplicate quants and clean reservations (stock/models/stock_rule.py:693-745).
- Reordering: horizon days (default 365) advance triggering (stock/models/res_company.py:44-48; stock/models/stock_orderpoint.py:744-762). Failed procurements post an activity to the product responsible (stock/models/stock_orderpoint.py:773-792).
- Only `trigger = auto` reordering rules run in the scheduler; manual ones require user action (stock/models/stock_rule.py:746-750).
- Follow-up on validate: chained moves and waiting receipts get re-assigned (stock/models/stock_move.py:2296-2306).

### 3.3 Security and multi-company
- Groups: Inventory User and Inventory Administrator; hidden feature groups (lots, packages, locations, warehouses, advanced routes, owners, reception report, signature, warnings) (stock/security/stock_security.xml:5-68).
- Access: every internal user can read warehouses, locations, quants; write access to transfers, moves, scraps needs Inventory User; delete on moves/scrap, warehouse and location edit needs Administrator (stock/security/ir.model.access.csv:2-22, 41-44).
- Record rules (company scoping): transfers, operation types, moves, orderpoints, scraps and warehouses restrict to allowed companies; locations, lots, move lines, quants, rules, routes, packages, storage categories also allow empty company (stock/security/stock_security.xml:72-165).
- Inventory adjustment mode is only for Inventory Users and above (stock/models/stock_quant.py:1231-1237); User without Administrator sees only own assigned counts by default (stock/models/stock_quant.py:411-413).
- Multi-company transit: a shipped inter-company transit location is activated when a second company is created and set as customer/vendor location between the companies' partners (stock/models/res_company.py:181-208). Rule lookup treats transit-to-inter-company like customer delivery (stock/models/stock_rule.py:643-666). OPT: packages auto-unpack in destination when config `stock.intercompany_auto_unpack` is set and Packages group is active (stock/models/stock_picking.py:1291-1302).
- Each company gets its own transit, inventory-loss, production and scrap locations plus scrap sequence (stock/models/res_company.py:53-109).
- Rule/route company consistency enforced (stock/models/stock_location.py:579-591; stock/models/stock_rule.py:121-131). Move lines and moves run `_check_company` on done (stock/models/stock_move.py:1741, 2271).

## 4. Handoffs — who owns what
- stock_account (auto-installs with stock+account): owns valuation. On done of a move it computes value for outgoing before, incoming after, creates the accounting entry when the product is real-time valued and a location has a valuation account, and updates costing for FIFO / lot-valuated average (stock_account/__manifest__.py:22,46; stock_account/models/stock_move.py:177-191, 659-667). Costing method and valuation type are set by product category with company fallback (stock_account/models/product.py:14, 61-80). `stock` itself holds no valuation. In v19 the moves carry the value fields (stock_account/models/stock_move.py:44-46, 121-139).
- purchase_stock: buy rule creates receipts and supplier-based lead times; sets received quantity on purchase lines from done receipts (purchase_stock/models/stock_rule.py:59; purchase_stock/models/purchase_order.py:360-377; purchase_stock/models/purchase_order_line.py:37-53).
- sale_stock: launches delivery procurement from sale lines, computes delivered quantity from done deliveries (sale_stock/models/sale_order_line.py:196, 317-385).
- mrp: adds manufacturing operation type and rules; reserves components and produces finished goods via stock moves (mrp/models/stock_rule.py:12, 124; mrp/models/mrp_production.py:1625, 2219; location rule uses `mrp_operation` code at stock/models/stock_location.py:197).
- stock_dropshipping, stock_delivery, stock_picking_batch, stock_landed_costs, product_expiry, stock_sms, mrp_subcontracting, repair: OPT add-ons (manifests: stock_dropshipping/__manifest__.py:23; stock_delivery:14,33; stock_picking_batch:12; stock_landed_costs:13; product_expiry:5; stock_sms:10,18; mrp_subcontracting:10).
- Handoff of quantity: `stock` owns physical quantity; document totals (ordered/delivered/received) belong to sale/purchase.

## 5. Configuration and defaults that change outcomes
- Operation type: reservation method (default at confirmation), backorder policy (default ask), lots flags (stock/models/stock_picking.py:69-73, 127-133, 47-59).
- Warehouse steps (default 1-step in/out) and MTO route active flag (stock/models/stock_warehouse.py:56-67; stock/models/res_config_settings.py:56-69).
- Product: "Track Inventory" (default off), tracking (default none), responsible, sale lead time, routes (stock/models/product.py:839-842, 856-862, 889-906). A non-storable product never reserves and never creates quants (stock/models/stock_move.py:1967-1970; stock/models/stock_quant.py:582-585).
- Category: removal strategy, packaging reserve method, routes (stock/models/stock_quant.py:618-628; stock/models/product.py:1303-1335).
- Company: horizon days (365), annual inventory month (December)/day (31), email confirmation off, SMS confirmation off (stock/models/res_company.py:24-51).
- Settings groups: Lots, Packages, Consignment (owners), Storage locations, Multi-step routes, Warnings, Signature, Reception report (stock/models/res_config_settings.py:11-59).
- Scheduler cron interval: daily (stock/data/stock_sequence_data.xml:53-56). Skipping quant tasks by config `stock.skip_quant_tasks` (stock/models/stock_quant.py:405).
- Cancel-origin behavior via config `stock.cancel_moves_origin` (stock/models/stock_move.py:2197).
- Return: return-type link on operation type; returns bypass backorder policy (stock/models/stock_picking.py:1520-1523).

## 6. Effective extension path (Community modules extending the models; names only)
- stock.move: l10n_in_ewaybill_stock, l10n_in_purchase_stock, l10n_in_sale_stock, l10n_in_stock, mrp, mrp_account, mrp_repair, mrp_subcontracting, mrp_subcontracting_account, mrp_subcontracting_dropshipping, mrp_subcontracting_purchase, point_of_sale, pos_mrp, product_expiry, project_mrp, project_mrp_account, project_stock_account, purchase_mrp, purchase_requisition_stock, purchase_stock, repair, sale_mrp, sale_project_stock, sale_project_stock_account, sale_purchase_stock, sale_stock, stock_account, stock_delivery, stock_landed_costs, stock_picking_batch.
- stock.picking: delivery_stock_picking_batch, l10n_ar_stock, l10n_in_ewaybill_stock, l10n_in_purchase_stock, l10n_in_sale_stock, l10n_in_stock, l10n_it_stock_ddt, l10n_ro_edi_stock, l10n_ro_edi_stock_batch, l10n_tr_nilvera_edispatch, mrp, mrp_subcontracting, mrp_subcontracting_dropshipping, mrp_subcontracting_purchase, point_of_sale, pos_repair, pos_sale, product_expiry, project_stock, purchase_stock, repair, sale_project_stock, sale_stock, stock_account, stock_delivery, stock_dropshipping, stock_fleet, stock_picking_batch, stock_sms, website_sale_stock.
- stock.location: mrp_subcontracting, stock_account, stock_maintenance.
- stock.quant: mrp, mrp_subcontracting, product_expiry, stock_account.
- Also (for orientation): stock.move.line — mrp, mrp_subcontracting, product_expiry, repair, sale_mrp, sale_stock, stock_account, stock_delivery, stock_picking_batch; stock.rule — mrp, mrp_subcontracting*, point_of_sale, product_expiry, project_mrp*, project_purchase_stock, purchase_mrp, purchase_requisition_stock, purchase_stock, sale_mrp, sale_purchase_stock, sale_stock, stock_dropshipping; stock.warehouse — mrp, mrp_subcontracting, mrp_subcontracting_dropshipping, point_of_sale, purchase_stock, repair, stock_fleet, stock_picking_batch, website_sale_collect; stock.warehouse.orderpoint — mrp, mrp_subcontracting_dropshipping, purchase_stock, sale_mrp; stock.picking.type — delivery_stock_picking_batch, l10n_ar_stock, l10n_it_stock_ddt, l10n_tr_nilvera_edispatch, mrp, point_of_sale, project_stock_account, repair, stock_account, stock_dropshipping, stock_fleet, stock_picking_batch; stock.lot — mrp, product_expiry, purchase_stock, repair, sale_stock, stock_account, stock_dropshipping; stock.scrap — mrp; stock.package — stock_delivery.
- Method: text search of `_inherit` in Community addons tree (excluding `stock` and test files); not a runtime-loaded-module list.

## 7. Evidence for tests (TEST)
- Negative-quant wiping by adjustment and by return: (TEST) stock/tests/test_warehouse.py:138-215.
- Removal strategy behavior (closest, least packages): (TEST) stock/tests/test_quant.py:708-760, 1648-1760.
- Backorder policy and partial picking: (TEST) stock/tests/test_stock_flow.py:1705, 1749, 2215, 2571.
- Multi-company object separation: (TEST) stock/tests/test_multicompany.py:51-400.
- Reordering rules: (TEST) stock/tests/test_stock_order_point.py; replenish: (TEST) stock/tests/test_replenish.py.

## 8. UNKNOWN items
- Global "block negative stock" policy: UNKNOWN — EVIDENCE INSUFFICIENT.
- Exact costing/valuation outcomes of done moves (FIFO/average/standard, landed cost): UNKNOWN — EVIDENCE INSUFFICIENT in `stock` (owned by stock_account; not traced beyond entry points).
- Barcode-app behavior (stock_barcode): UNKNOWN — EVIDENCE INSUFFICIENT (module absent in Community tree).
- Cross-company reservation, owner (consignment) reservation edge cases and exact SQL-level merge/lock behavior of quants: UNKNOWN — EVIDENCE INSUFFICIENT.
- Operation-type-level `move_type` default and full list of print automation side effects: UNKNOWN — EVIDENCE INSUFFICIENT (field seen at stock/models/stock_picking.py:151; default not traced).
- Country/localization variants (l10n_*_stock): UNKNOWN — EVIDENCE INSUFFICIENT (names listed only).
- No universal rule is inferred from one example above; treat each finding as valid for the pointer given only.

