# U09 — stock_quants_lots_adjustments — Restricted Technical Evidence (L2/L3)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

- Unit: U09 — short name `stock_quants_lots_adjustments`
- Modules owned: `stock` (quants, inventory counting/adjustments, lots/serials/tracking, packages/package types, scrap, inventory-loss locations, product quantity fields, move-history/stock reports), `product_expiry` (light). `stock_fleet` and `stock_sms` were checked and skipped: they extend only stock.picking / picking type / warehouse / batch / settings and contain no quant, lot, scrap, package or inventory logic (grep of both modules for stock.quant, stock.lot, stock.scrap, stock.package, inventory returned nothing).
- Source revision: `19.0.post20260921` (Community only; `Extra_Thailand`, `Extra_Module_scgl`, Enterprise code not opened)
- Date: 2026-10-02
- Method: static source read (read-only), DB queried only for structure/configuration. No Odoo start, no AWT/L5 claims; anything needing execution is flagged `RT`.
- Prior structural extract (`~/STATE03_RESTRICTED_LOCAL/sourcemap/stock.json`) was consulted for groups/rules/cron lists; all facts below were re-read in source.

## Discovered supporting modules (read only as far as needed)
- `stock_account` (quant accounting_date/value, location valuation_account_id, move accounting, lot valuation) — hand-off to U10.
- `mrp` (kit constraint on quants, scrap extension, lot traceability via produce_line_ids), `mrp_subcontracting` (portal ACL/rules on lots and move lines, is_subcontract quant filter) — only the lines cited were read.
- `stock_delivery` (extends stock.package and stock.package.type), `sale_stock`, `purchase_stock`, `stock_dropshipping`, `repair` (extend stock.lot / stock.move.line) — located by grep, NOT analysed.

## Contradictions with prior evidence (summary; each is also flagged CONTRA in the claims table where claim-level)
- IAV-F05 prior: annual date applies where frequency is unset. Source: `min(location next date, company annual date)`; the annual date also caps a cyclic date [VDR-U09-C100].
- IAV-F03 prior (documentation-tier): balance sheet updates as soon as counts are applied, unqualified. Source: any entry requires real_time valuation and a valuation account on the loss location; restored DB is periodic with no location account, so no entry at apply time [VDR-U09-C144, VDR-U09-C143].
- IAV-F02 prior UNKNOWN (does single-line Apply capture a reason?): resolved from source — the row Apply button bypasses the reason wizard; the reason is defaulted and optional even in the bulk path [VDR-U09-C067, VDR-U09-C064, VDR-U09-C068].
- IAV-F01 prior UNKNOWN (counts by lot/serial?): resolved — counts are per quant (lot, package, owner) and count requests include sibling lots of tracked products [VDR-U09-C082, VDR-U09-C040].
- IAV-F06 prior (documentation-tier): a native Revert Inventory Adjustment exists — CONFIRMED in source; additionally it is repeatable (no already-reverted check), applies to relocation moves, not to scrap [VDR-U09-C116, VDR-U09-C118, VDR-U09-C119].
- Package model name: this revision uses `stock.package` (nested) not `stock.quant.package` [VDR-U09-C189].

## Consolidated RT (runtime/AWT required) list
- Concurrency: lock-skip + duplicate quant creation + merge (VDR-U09-C021, VDR-U09-C023, VDR-U09-C029); negative-stock reservation netting.
- Conflict/warning wizard access for non-manager stock users (ACL manager-only).
- Revert after later movements/counts; scrap of kits; deep package nesting; past-date quantity performance; perpetual-valuation entries for counts/scrap.

## CAP-U09-01 Quant model and quantity integrity

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no existing Function-ID covers the on-hand record as such; RCN-F01 relates only as a reader of quants, see CAP-U09-09)

### D1 Business purpose and process semantics
A quant (stock.quant) is the system's on-hand truth for one product at one location, split by lot/serial, package and owner. It carries quantity and reserved_quantity and derives available = quantity - reserved. Users must not edit these quantities freely: they change only through completed stock moves, reservation maintenance, or the *inventory mode* (counting) path. The business purpose is one location-exact figure that availability, counting, valuation, expiry and traceability all read. Negative stock is tolerated by the engine (no hard block), and a maintenance routine merges duplicates, re-aligns reservations and deletes empty quants. VDR-U09-C001, VDR-U09-C002, VDR-U09-C003, VDR-U09-C004, VDR-U09-C299

### D2 Architecture, data and object relationships
Model stock.quant (stock/models/stock_quant.py). Identity key = (product_id, location_id, lot_id, package_id, owner_id); company_id is a stored related of the location company (VDR-U09-C005); product_id is required/restricted (VDR-U09-C006). Relations: product.product (stock_quant_ids), stock.location (quant_ids), stock.lot (quant_ids), stock.package (quant_ids), res.partner owner, stock.move.line (reserved quantity must equal sum of open lines, enforced by VDR-U09-C034). Extensions when installed: stock_account (value, currency_id manager-only, accounting_date, cost_method) VDR-U09-C048; product_expiry (expiration_date, removal_date, available_quantity override, FEFO order) VDR-U09-C045, VDR-U09-C046; mrp (kit constraint, _should_bypass_product) VDR-U09-C047; mrp_subcontracting (is_subcontract search filter, not analysed). There is NO unique database constraint on the identity key; uniqueness is application-level plus periodic merge (VDR-U09-C027, DB observation below).

### D3 Source, technical and workflow logic
Entry points: (a) transfer engine -> stock.move.line._action_done -> _synchronize_quant -> quant._update_available_quantity / _update_reserved_quantity VDR-U09-C037, VDR-U09-C036; (b) counting/inventory mode (CAP-U09-02); (c) maintenance _quant_tasks from the daily scheduler and when quant screens open VDR-U09-C030, VDR-U09-C031, VDR-U09-C032. _update_available_quantity runs as sudo, gathers quants with strict key, locks the first one (try_lock_for_update) and adds the delta, else creates a new quant VDR-U09-C020, VDR-U09-C021, VDR-U09-C022, VDR-U09-C023. Reservation sizing uses _get_reserve_quantity/_get_available_quantity with negative-quant netting VDR-U09-C025, VDR-U09-C301. Removal strategy decides which quants are consumed first VDR-U09-C038, VDR-U09-C039.
State diagram (quant lifecycle):
- (none) -> created [first positive/negative delta with no lockable quant, or inventory-mode create]
- created -> updated [move line done / reservation / inventory apply]
- updated -> duplicated [concurrent create path, RT]
- duplicated -> merged [_merge_quants]
- updated -> empty [quantity, reserved, inventory_quantity all 0]
- empty -> deleted [_unlink_zero_quants when user_id is NULL]
- any -> zeroed -> deleted [manager unlink triggers _apply_inventory with inventory_quantity 0]
Override chain: base stock.quant + stock_account (_apply_inventory, _get_inventory_move_values, _get_inventory_fields_write, value) + product_expiry (_compute_available_quantity, _get_removal_strategy_order, _get_gs1_barcode, _set_view_context) + mrp (_check_kits, _should_bypass_product) + mrp_subcontracting (is_subcontract).

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Completed move lines call _synchronize_quant: source is decremented, destination incremented, reservation on source is released first. VDR-U09-C037, VDR-U09-C022, VDR-U09-C024 |
| 2 Reversal/cancel/negative | No cancel of quants. Negative on-hand is allowed; over-consumption releases other unpicked reservations (VDR-U09-C036). A manager delete books a zeroing adjustment (VDR-U09-C019). Reservations are floored at 0 (VDR-U09-C022). Over-unreserving raises (VDR-U09-C295). |
| 3 Multi-company / scope | company_id derives from location; locations with no company give no-company quants; rule company_ids + [False] (VDR-U09-C005, VDR-U09-C284). Merge groups by company (VDR-U09-C027). Relocation requires a single company (VDR-U09-C050). A product cannot change company while quants exist in another company (VDR-U09-C259). |
| 4 Side effects / cross-module | Valuation value is computed per quant (VDR-U09-C048); expiry zeroes available quantity after removal date and offers FEFO (VDR-U09-C045, VDR-U09-C046); kits cannot hold quants (VDR-U09-C047); serial duplicate check re-run after done moves (VDR-U09-C044). |
| 5 Configuration / optionality | Inventory mode needs group_stock_user (VDR-U09-C042, VDR-U09-C043); config parameter stock.skip_quant_tasks skips screen-triggered maintenance (VDR-U09-C032); product storable flag required (VDR-U09-C008). |
| 6 Validation / constraints | storable-only, serial qty <=1, no view location, lot-product match, copy forbidden, restricted create/write fields (VDR-U09-C008, VDR-U09-C009, VDR-U09-C010, VDR-U09-C011, VDR-U09-C007, VDR-U09-C012, VDR-U09-C013, VDR-U09-C015). |
| 7 Roles / permissions | ACL stock user 1110, all users read; unlink only superuser or manager; record rule company_ids + [False] (VDR-U09-C278, VDR-U09-C018, VDR-U09-C284). DB confirms both ACL rows and a global rule. |
| 8 Scheduled / automated | Daily cron Procurement: run scheduler ends with _quant_tasks (merge, clean reservations, unlink zero) (VDR-U09-C030, VDR-U09-C031, VDR-U09-C292). |
| 9 Exceptions / failure | UserError/ValidationError paths listed above; merge SQL failure is swallowed and only logged (VDR-U09-C029); lock-skip may create duplicates (VDR-U09-C023, RT). |
| 10 Accounting / audit / compliance | quant has no chatter (VDR-U09-C124); history via move lines only; value (manager-only) comes from stock_account and is zero under periodic valuation with no loss-location accounts (VDR-U09-C048, VDR-U09-C143). |

### DB reconciliation (configuration/structure only)
Restored DB: stock_quant has 0 rows; only the primary-key index exists (no unique index on the identity key); rule 'stock_quant multi-company' is global (no groups) with domain company_id in company_ids + [False]; ACL rows access_stock_quant_user (1110) and access_stock_quant_all (1000) present; no ir_config_parameter stock.skip_quant_tasks; the daily cron 'Procurement: run scheduler' is active. Installed Community extensions relevant: stock_account, product_expiry, mrp, mrp_subcontracting.

### Unknown / Runtime list
- RT: behaviour of try_lock_for_update and duplicate-quant creation under concurrent validations; effectiveness of _merge_quants SQL.
- RT: exact outcome of reservation netting with negative quants across lots/packages.
- UNKNOWN: GS1 barcode helpers (_get_gs1_barcode, get_aggregate_barcodes at stock_quant.py:1353-1456) are present but not analysed here.

## CAP-U09-02 Inventory counting and adjustment application

**Function-ID(s):** IAV-F01 (Physical count recording), IAV-F02 (Applying the adjustment)

### D1 Business purpose and process semantics
Users enter a counted quantity against a quant (or add a new counted line in inventory mode), compare it with on-hand, and apply it either row by row or in bulk. Bulk/header apply asks for an optional reason (default 'Physical Inventory') and a counting date; the row Apply button skips both. Applying books a done stock move between the quant's location and the inventory-loss location so that on-hand equals the counted quantity, then reschedules the next count. A conflict dialog protects against on-hand movements between count and apply. Managers can request counts (assign counter and due date). VDR-U09-C051, VDR-U09-C060, VDR-U09-C063, VDR-U09-C064, VDR-U09-C067, VDR-U09-C069, VDR-U09-C081

### D2 Architecture, data and object relationships
Objects: stock.quant (inventory_quantity 'Counted', inventory_diff_quantity stored, inventory_date, inventory_quantity_set, is_outdated, user_id, inventory_quantity_auto_apply, last_count_date) VDR-U09-C051, VDR-U09-C052, VDR-U09-C053, VDR-U09-C054, VDR-U09-C087; transient wizards stock.inventory.adjustment.name (reason + counting_date), stock.inventory.conflict, stock.inventory.warning, stock.request.count, stock.quant.relocate; stock.move/stock.move.line with is_inventory and inventory_name; stock.location.last_inventory_date. Counterpart location = product.property_stock_inventory (company-dependent) else the ir.default VDR-U09-C076. Product form on-hand edit is an inverse of qty_available that creates and applies a quant VDR-U09-C085.

### D3 Source, technical and workflow logic
Flow: write inventory_quantity (inventory mode) -> compute inventory_quantity_set True and diff = counted - quantity VDR-U09-C052, VDR-U09-C053 -> Apply: action_apply_inventory checks is_outdated; if any, opens conflict wizard VDR-U09-C060, VDR-U09-C061, VDR-U09-C062; else _apply_inventory builds one move per quant (diff>0 from loss location, else to loss location, zero included) VDR-U09-C069, VDR-U09-C072, creates moves with inventory_mode=False, completes with _action_done(ignore_dest_packages) VDR-U09-C073, optionally overwrites move date VDR-U09-C074, triggers assignment VDR-U09-C077, stamps last_inventory_date and next inventory_date VDR-U09-C075, then clears counts. Header Apply / Apply All -> stock.inventory.adjustment.name.action_apply (only quants with inventory_quantity_set) VDR-U09-C063, VDR-U09-C065. The shortcut field inventory_quantity_auto_apply (inverse) applies immediately VDR-U09-C078, VDR-U09-C079.
State diagram (per quant count):
- not counted -> counted [enter figure / Set / create with counted / request count]
- counted -> outdated [on-hand changes after count]
- counted -> not counted [Apply]
- outdated -> not counted [Apply via conflict choice keep counted or keep difference]
- counted -> not counted [Clear]
Override chain: base stock.quant + stock_account (_apply_inventory groups by accounting_date and forces period date; _get_inventory_move_values naming) VDR-U09-C137, VDR-U09-C138 + product_expiry (view context only).

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Enter counted figure, review difference, Apply (with reason/date via header or bulk), move done, on-hand equals counted, next count rescheduled. VDR-U09-C060, VDR-U09-C069, VDR-U09-C073, VDR-U09-C075 |
| 2 Reversal/cancel/negative | Clear resets a count (VDR-U09-C057); outdated lines require a choice (VDR-U09-C062); applied counts are corrected by revert or a further count (CAP-U09-04). |
| 3 Multi-company / scope | quants belong to location company; company rule company_ids + [False]; relocation/relocate wizard single-company; accounting date per company journal (VDR-U09-C284, VDR-U09-C050). |
| 4 Side effects | Done inventory move may create accounting entry (stock_account, CAP-U09-05); assigns waiting moves (VDR-U09-C077); relocation moves are also inventory-flagged (VDR-U09-C118); product-form inverse path (VDR-U09-C085, VDR-U09-C086). |
| 5 Configuration / optionality | Reason wizard fields default; expected-quantity visibility is a system parameter (VDR-U09-C083); lot/package/owner columns by feature groups (VDR-U09-C082). |
| 6 Validation / constraints | Counting mode restricts create/write fields (VDR-U09-C015, VDR-U09-C013); reason is not required (VDR-U09-C064); counted lines limited to internal/transit (VDR-U09-C088). |
| 7 Roles / permissions | Apply/Set/Clear row actions need inventory mode (stock user); header Clear, Request a Count, Set to 0, Relocate are manager only (VDR-U09-C066, VDR-U09-C059, VDR-U09-C282); conflict/warning wizard ACL is manager-only (VDR-U09-C091, RT). |
| 8 Scheduled / automated | No automatic creation of counts; due dates only surface via filters (VDR-U09-C107, VDR-U09-C090). |
| 9 Exceptions / failure | Conflict wizard path; warning wizard when counts already set (VDR-U09-C056); creation/write restrictions raise UserError; unknown ACL effect for non-manager users (VDR-U09-C093). |
| 10 Accounting / audit | Reason optional and absent on row Apply; reference text is the only audit field on moves; move.reference defaults 'Product Quantity Updated (user)' (VDR-U09-C068, VDR-U09-C304); accounting date and entry creation are valuation-side (VDR-U09-C136). |

### DB reconciliation (configuration/structure only)
Restored DB: no quants/moves exist; ACL rows for conflict, warning, request count, relocate are manager-only (1110) and for the reason wizard user+manager; annual inventory month/day on the company = 12/31; no location has a frequency. Group tracking (lots, packages, multi-locations) is implied by base.group_user, so lot/package/owner columns would show.

### Unknown / Runtime list
- RT: whether a non-manager stock user can open the conflict/warning dialogs when applying (ACL create is manager-only).
- RT: stock.request.count._get_values_to_write line 59 builds a tuple for user_id (trailing comma) - confirm the assignee is saved.
- RT: behaviour of the counted_quantity_widget / inventory_report_list JS in the browser (not analysed, static JS not in scope).
- UNKNOWN: approval gating of adjustments by Enterprise/other modules is out of scope (Community only).

## CAP-U09-03 Cycle counts and scheduling

**Function-ID(s):** IAV-F05 (Cycle count scheduling - Inventory Frequency)

### D1 Business purpose and process semantics
Locations carry an optional counting frequency (days); companies carry an annual count month/day (default 31 December). Quants of internal/transit locations receive a scheduled inventory_date; the To Count filter and highlighting show what is due. Applying a count at a location stamps last_inventory_date and recomputes the location's next planned date and the applied quants' dates. Nothing is generated automatically; users or managers must create or request counts. VDR-U09-C095, VDR-U09-C097, VDR-U09-C100, VDR-U09-C107

### D2 Architecture, data and object relationships
stock.location: cyclic_inventory_frequency, last_inventory_date, next_inventory_date (stored computed) VDR-U09-C095; res.company: annual_inventory_month (default '12'), annual_inventory_day (default 31) VDR-U09-C102; stock.quant: inventory_date (stored computed from location_id, editable) VDR-U09-C103; stock.request.count writes inventory_date/user_id VDR-U09-C109.

### D3 Source, technical and workflow logic
location._compute_next_inventory_date: remaining = frequency - days since last; <=0 -> tomorrow; >0 -> last+frequency; never counted -> today+frequency VDR-U09-C097. location._get_next_inventory_date returns min(location next, company annual) or whichever exists; annual date clamps day and rolls to next year VDR-U09-C100, VDR-U09-C101. Quant inventory_date computed only when empty and only on location_id change VDR-U09-C103; on apply it is recomputed VDR-U09-C104.
State diagram (per quant scheduling):
- scheduled -> due [today >= inventory_date]
- due -> counted [user enters counted figure]
- counted -> scheduled [Apply: next date recomputed from location cadence or annual date]
Override chain: base only; no override found in installed Community modules (grep of cyclic_inventory_frequency/_get_next_inventory_date outside stock found none).

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Set frequency on an internal location; apply counts; next date = last + frequency; To Count filter lists due lines. VDR-U09-C097, VDR-U09-C104, VDR-U09-C105 |
| 2 Reversal/cancel/negative | No cancel. Overdue location gets tomorrow (VDR-U09-C097); negative frequency refused (VDR-U09-C096); overflow refused (VDR-U09-C098). |
| 3 Multi-company / scope | Cyclic date only for locations with a company; annual date is per company (VDR-U09-C099, VDR-U09-C102). |
| 4 Side effects | Application of counts updates last_inventory_date (VDR-U09-C075); no notifications. |
| 5 Configuration / optionality | Per-location frequency; company annual date can be disabled by no month (VDR-U09-C102); cyclic section shown only for internal/transit with company (VDR-U09-C108). |
| 6 Validation / constraints | frequency >= 0 SQL check; OverflowError converted to UserError (VDR-U09-C096, VDR-U09-C098). |
| 7 Roles / permissions | Location master data manager-only (ACL stock.location manager 1111); quant dates editable by stock users in inventory mode; annual date in settings visible to managers (VDR-U09-C280). |
| 8 Scheduled / automated | No cron creates counts; the only stock cron is the procurement scheduler (VDR-U09-C107, VDR-U09-C292). |
| 9 Exceptions / failure | Only the overflow UserError; a missed date has no consequence (VDR-U09-C307). |
| 10 Accounting / audit | None; scheduling is not an accounting event. |

### DB reconciliation (configuration/structure only)
Restored DB: company annual inventory 12/31 (defaults); 0 locations with frequency > 0; no cron related to counting; the Procurement scheduler cron is active daily.

### Unknown / Runtime list
- UNKNOWN: any Community extension adding automated counting tasks was not found by grep (none) but non-stock modules were not exhaustively read.
- RT: effect of changing a frequency on already-stored quant dates (inferred as no rewrite).

## CAP-U09-04 Reversal and correction of an applied adjustment

**Function-ID(s):** IAV-F06 (Reversal / correction of an applied adjustment)

### D1 Business purpose and process semantics
Applied counts are not deleted or edited. The documented 'Revert Inventory Adjustment' action exists in source as stock.move.line.action_revert_inventory (server action bound to the move line list). It creates and completes an opposite inventory move per selected inventory line. A new count can also correct the figure. VDR-U09-C111, VDR-U09-C113, VDR-U09-C115, VDR-U09-C117

### D2 Architecture, data and object relationships
stock.move.line (is_inventory related to move.is_inventory), stock.move (is_inventory, inventory_name), server action action_revert_inventory_adjustment bound to stock.move.line VDR-U09-C117. Revertible lines include stock relocations because move_quants builds inventory-flagged moves VDR-U09-C118; scrap moves are not inventory-flagged VDR-U09-C119.

### D3 Source, technical and workflow logic
action_revert_inventory: for each selected line with is_inventory and non-zero quantity build reversal move values (swap locations and package roles, same lot/owner, name '<reference> [reverted]') VDR-U09-C113, VDR-U09-C114, create and _action_done them VDR-U09-C115, return a list view; if none qualified return a danger notification VDR-U09-C112. No marker is written on the original, so repeated reversal is possible VDR-U09-C116.
State diagram:
- applied (done inventory move) -> applied [revert adds a second done move; original unchanged]
- applied -> corrected [new count/apply on same quant]
Override chain: base stock.move.line only; stock_account adds valuation to the new move through _action_done (VDR-U09-C311).

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Select inventory move lines in Moves History, run Revert Inventory Adjustment; reversal completes at once. VDR-U09-C111, VDR-U09-C115 |
| 2 Reversal/cancel/negative | Reversal is the only reversal; cancel of a done inventory-destination move is a no-op; done lines cannot be deleted (VDR-U09-C121, VDR-U09-C120); desktop move line form is read-only (VDR-U09-C122). |
| 3 Multi-company / scope | Reversal uses the original line's company (VDR-U09-C113); move line rule company_ids + [False] (VDR-U09-C288). |
| 4 Side effects | New move is valued/posted like any adjustment (VDR-U09-C311); quants change by the engine. |
| 5 Configuration / optionality | None configurable; the server action has no group restriction (VDR-U09-C117). |
| 6 Validation / constraints | Only is_inventory lines with non-zero quantity qualify (VDR-U09-C111); no duplicate-reversal check (VDR-U09-C116). |
| 7 Roles / permissions | Table ACL on stock.move.line allows all internal users; completing the reversal creates stock.move so needs stock user (VDR-U09-C125). |
| 8 Scheduled / automated | None. |
| 9 Exceptions / failure | Notification when nothing qualifies (VDR-U09-C112); other failures follow the engine (rounding, negative quantity: VDR-U09-C297, VDR-U09-C296). |
| 10 Accounting / audit | Original and reversal both remain in Moves History; link is by reference text only (VDR-U09-C309, VDR-U09-C124); unlimited double reversal is a control gap (VDR-U09-C312). |

### DB reconciliation (configuration/structure only)
Restored DB: no move lines exist, so the revert action cannot be exercised; the ACL row access_stock_move_line_all gives base.group_user 1111 on stock.move.line; stock.move user access is 1110.

### Unknown / Runtime list
- RT: reversal after later movements or counts (quant merging, negative stock) and the rendered list result.
- UNKNOWN: approval/lock-date gating of reversal belongs to accounting modules (U10) and is not examined.

## CAP-U09-05 Financial hooks of adjustments and scrap

**Function-ID(s):** IAV-F03 (Financial posting of the adjustment), IAV-F04 (Scrap / Inventory Loss location + Loss Account) - stock-side facts only; accounting mechanics belong to U10

### D1 Business purpose and process semantics
Counts and scrap both end in an inventory-loss location. The stock module chooses the locations and passes an optional accounting date; any journal entry is created by stock_account when the product uses real_time valuation and the loss location has a valuation account. VDR-U09-C127, VDR-U09-C128, VDR-U09-C130, VDR-U09-C133, VDR-U09-C134

### D2 Architecture, data and object relationships
stock.location.usage = inventory (Inventory Loss) with optional stock_account field valuation_account_id ('Stock Valuation Account') VDR-U09-C132; per company locations 'Inventory adjustment' and 'Scrap' VDR-U09-C127, VDR-U09-C128; product.template.property_stock_inventory (company-dependent) VDR-U09-C130; stock.scrap.scrap_location_id (lowest-id inventory location) VDR-U09-C131; stock.quant.accounting_date VDR-U09-C136; stock.move.account_move_id link (VDR-U09-C315).

### D3 Source, technical and workflow logic
Count path: _apply_inventory -> moves with the loss location as counterpart -> stock_account._action_done -> _create_account_move when _should_create_account_move is true VDR-U09-C133, VDR-U09-C313; entry lines: if source has account debit product stock_valuation / credit source account, else debit destination account / credit stock_valuation VDR-U09-C134; account.move dated force_period_date or today, posted VDR-U09-C135, VDR-U09-C315. Accounting date: quants grouped by accounting_date -> force_period_date context -> inventory_name suffix VDR-U09-C137, VDR-U09-C138. Scrap path: scrap move to scrap_location_id completes via the same _action_done VDR-U09-C230. Valued perimeter: internal/transit locations with company VDR-U09-C139.
State diagram:
- move done -> account entry created and posted [stock_account installed, real_time, location account set]
- move done -> no entry [periodic valuation or no location account]
Override chain: base stock (locations, accounting-neutral move values VDR-U09-C140) + stock_account (location account, quant accounting_date, move accounting).

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Count or scrap completes; under real_time with a loss-location account an entry is posted at the same time. VDR-U09-C133, VDR-U09-C134, VDR-U09-C315 |
| 2 Reversal/cancel/negative | Revert (CAP-U09-04) creates a second move valued the same way; scrap has no reversal (VDR-U09-C311, VDR-U09-C119). |
| 3 Multi-company / scope | One loss location per company; default property per company; location change of company forbidden (VDR-U09-C127, VDR-U09-C130, VDR-U09-C141). |
| 4 Side effects | Journal entry and analytic lines (stock_account); no entry under periodic valuation (VDR-U09-C143). |
| 5 Configuration / optionality | Valuation mode per category/company; valuation account per location; per-product override of adjustment location (VDR-U09-C130, VDR-U09-C132). |
| 6 Validation / constraints | Usage change blocked while stock exists; scrap location cannot be a manufacturing destination (VDR-U09-C141, VDR-U09-C142). |
| 7 Roles / permissions | Accounting entries created as sudo by stock_account; location master data manager-only; quant value manager-only (VDR-U09-C283). |
| 8 Scheduled / automated | Period-closing entries are a stock_account cron (not in scope; U10). |
| 9 Exceptions / failure | No entry (silently) when conditions fail (VDR-U09-C133); CONTRA with the prior unconditional claim (VDR-U09-C144). |
| 10 Accounting / audit | In the restored DB nothing is posted at apply time (periodic, no location account) (VDR-U09-C143); adjustment and scrap share one loss location unless a second is configured (VDR-U09-C129, VDR-U09-C131). |

### DB reconciliation (configuration/structure only)
Restored DB: res_company.inventory_valuation = periodic, inventory_period = manual; stock_location has exactly one inventory-usage location ('Inventory adjustment') and ir.default property_stock_inventory points to it; no stock_location row has valuation_account_id set; no valuation-layer table.

### Unknown / Runtime list
- UNKNOWN: valued-flag semantics, entry amounts and period-closing entries for counts/scrap are outside this unit (U10).
- RT: behaviour under perpetual (real_time) valuation requires enabling the flag and executing, not done.

## CAP-U09-06 Lots, serial numbers and tracking

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no existing Function-ID for lot/serial tracking)

### D1 Business purpose and process semantics
Storable products choose tracking none/lot/serial. Lots/serials are master records (stock.lot) unique per product within a company, created at receipt, manufacture or manually, required on tracked movements except counts/scrap/manual moves, and traced through move lines to deliveries and manufactured goods. With product_expiry, lots also carry expiration, best-before, removal and alert dates. VDR-U09-C146, VDR-U09-C152, VDR-U09-C163, VDR-U09-C175, VDR-U09-C180

### D2 Architecture, data and object relationships
stock.lot (name, product_id, company_id, quant_ids, product_qty computed, location_id computed/stored with inverse, partner_ids, delivery_ids, lot_properties) VDR-U09-C151, VDR-U09-C173, VDR-U09-C174; product.template tracking, lot_sequence_id, serial_prefix_format VDR-U09-C146, VDR-U09-C156; picking type use_create_lots/use_existing_lots VDR-U09-C160, VDR-U09-C161; stock.move.line lot_id/lot_name; quant lot_id and sn_duplicated VDR-U09-C169; product_expiry adds expiration_date, use_date, removal_date, alert_date, product_expiry_alert, product_expiry_reminded on lots and removal_date on quants/move lines VDR-U09-C180, VDR-U09-C187. Extensions of stock.lot: sale_stock, purchase_stock, stock_dropshipping, mrp, repair, stock_account (lot valuation), product_expiry (discovered, only product_expiry read).

### D3 Source, technical and workflow logic
Creation: at done, stock.move.line._action_done classifies tracked lines: exempt (inventory adjustment, scrap, or picking type with both switches off) / lot name found -> assign / name unknown with use_create_lots -> create via _create_and_assign_production_lot / otherwise error VDR-U09-C162, VDR-U09-C163, VDR-U09-C165, VDR-U09-C166, VDR-U09-C164; _prepare_new_lot_vals sets company VDR-U09-C167; names default from sequence and series generator VDR-U09-C155, VDR-U09-C157, VDR-U09-C158. Uniqueness: constrains name/product/company (python) VDR-U09-C152, VDR-U09-C153, VDR-U09-C154. Serial integrity: onchange warnings and post-done check_quantity VDR-U09-C168, VDR-U09-C009, VDR-U09-C044. Tracking change: only an onchange warning VDR-U09-C148, VDR-U09-C149. Expiry: dates computed on lot; scheduler alert; validation wizard; FEFO VDR-U09-C180, VDR-U09-C182, VDR-U09-C183, VDR-U09-C184, VDR-U09-C185. Traceability: report and delivery graph VDR-U09-C175, VDR-U09-C177.
State diagram:
- (none) -> created [receipt with new lot name / manual create / count of a new lot / manufacture]
- created -> on hand [done move into internal location]
- on hand -> delivered [done outgoing line]
- (expiry) fresh -> alert -> expired [dates reached; product_expiry_alert at expiration_date]
Override chain: base stock.lot + sale_stock/purchase_stock/stock_dropshipping/repair/mrp/stock_account (not analysed) + product_expiry (fields, display name, _alert_date_exceeded).

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Receipt with typed lot names creates lots at validation; delivery uses existing lots; traceability shows both. VDR-U09-C165, VDR-U09-C166, VDR-U09-C175 |
| 2 Reversal/cancel/negative | Lots can be deleted by stock users (ACL 1111) but quants restrict deletion; product change after moves refused; negative lot stock compensated from untracked stock (VDR-U09-C178, VDR-U09-C170, VDR-U09-C188). |
| 3 Multi-company / scope | Lot company from product/line; uniqueness across no-company vs company; rule company_ids + [False]; company change vs location (VDR-U09-C152, VDR-U09-C171, VDR-U09-C285). |
| 4 Side effects | Expiry alert activities; expiry wizard at validation; lot valuation (stock_account); manufacturing consumption chain in traceability (VDR-U09-C182, VDR-U09-C184, VDR-U09-C318). |
| 5 Configuration / optionality | Feature group, picking type switches, per-product sequence prefix, expiry module; disabling lots blocked if tracked products exist (VDR-U09-C179, VDR-U09-C160, VDR-U09-C150). |
| 6 Validation / constraints | Unique constraint (python), lot-product match, serial qty, product storable domain, create-lot guard (VDR-U09-C152, VDR-U09-C011, VDR-U09-C009, VDR-U09-C159). |
| 7 Roles / permissions | stock.lot ACL stock user 1111, no all-users ACL; manager n/a; portal for subcontractors via mrp_subcontracting (VDR-U09-C178). |
| 8 Scheduled / automated | Daily scheduler calls _alert_date_exceeded (product_expiry) (VDR-U09-C183). |
| 9 Exceptions / failure | Missing lot error, duplicate error, create-lot guard, serial warnings (VDR-U09-C164, VDR-U09-C152, VDR-U09-C159, VDR-U09-C168). |
| 10 Accounting / audit / compliance | Traceability reports; lot-valued products handled by stock_account (not analysed); adjustments and scrap bypass lot requirement (VDR-U09-C162). |

### DB reconciliation (configuration/structure only)
Restored DB: stock_lot has 0 rows and no unique index besides the primary key; group stock.group_production_lot is implied by base.group_user and base.group_portal (feature enabled); product_expiry installed; picking types create/existing flags as listed; sequence stock.lot.serial (empty prefix, padding 7) exists; removal strategies include FEFO.

### Unknown / Runtime list
- RT: lot creation at receipt with mixed typed names; tracking change on products with existing untracked stock.
- UNKNOWN: effects of sale_stock, purchase_stock, repair, stock_dropshipping extensions of stock.lot were not read (discovered supporting modules).
- RT: JS generation of lot series (action_generate_lot_line_vals) not analysed.

## CAP-U09-07 Packages and package types

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no existing Function-ID for packages)

### D1 Business purpose and process semantics
In this revision packages are stock.package records (not stock.quant.package): nested containers that hold quants. They are created by putting move lines in a pack, receiving packed goods or manually; a package type defines dimensions, weights, barcode, reusable/disposable use. Operations: put in pack, remove from transfer, unpack, manual relocation, destination container application at done, and package history. VDR-U09-C189, VDR-U09-C199, VDR-U09-C203, VDR-U09-C197, VDR-U09-C211

### D2 Architecture, data and object relationships
stock.package (name, complete_name, quant_ids, contained_quant_ids, package_type_id, location_id/company_id computed stored, owner_id computed, parent_package_id/child_package_ids tree, package_dest_id/child_package_dest_ids, move_line_ids and picking_ids computed) VDR-U09-C195, VDR-U09-C196; stock.package.type (dimensions, weights, barcode, package_use, sequence_id) VDR-U09-C209, VDR-U09-C208, VDR-U09-C210; stock.package.history VDR-U09-C212; transient stock.put.in.pack and stock.package.destination wizards; quant.package_id VDR-U09-C190. stock_delivery extends package and type (not analysed) VDR-U09-C216.

### D3 Source, technical and workflow logic
Put in pack: package.action_put_in_pack / move_line.action_put_in_pack -> pre-hook may open wizard VDR-U09-C200, VDR-U09-C201 -> create/reuse package, set package_dest_id, clear unused dests, re-run putaway VDR-U09-C199. At done: package history rows VDR-U09-C211, quants moved, then result_package._apply_dest_to_package checks location consistency and writes parent_package_id VDR-U09-C204, VDR-U09-C320; stock.move._action_done verifies single location VDR-U09-C205. Unpack: relocation move + quant clean-up VDR-U09-C203. Manual relocation VDR-U09-C197. Cycle guard VDR-U09-C198.
State diagram:
- empty -> filled [receipt or pack of quants]
- filled -> destination-assigned [put in pack: package_dest_id set]
- destination-assigned -> contained [transfer done: parent_package_id := dest]
- filled -> empty [unpack / all content moved out]
Override chain: base stock.package + stock_delivery (shipping extensions, not analysed).

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Put picked lines into a new package of a type, validate transfer; package takes its location from content. VDR-U09-C199, VDR-U09-C195, VDR-U09-C204 |
| 2 Reversal/cancel/negative | Remove package from transfer; unpack; cannot move empty package (VDR-U09-C202, VDR-U09-C203, VDR-U09-C197). |
| 3 Multi-company / scope | Package company from content; rule company_ids + [False]; owner common-or-empty (VDR-U09-C195, VDR-U09-C196, VDR-U09-C286). |
| 4 Side effects | Putaway re-applied; history rows; relocation inventory moves (VDR-U09-C199, VDR-U09-C211). |
| 5 Configuration / optionality | Packages feature group; package use reusable/disposable; type sequence (VDR-U09-C213, VDR-U09-C207, VDR-U09-C208). |
| 6 Validation / constraints | Cycle check, location consistency, barcode unique, dimension checks (VDR-U09-C198, VDR-U09-C204, VDR-U09-C205, VDR-U09-C209). |
| 7 Roles / permissions | Package: all users read; stock users CRUD; types: manager CRUD, user read (VDR-U09-C214). |
| 8 Scheduled / automated | None; unpack triggers _quant_tasks synchronously (VDR-U09-C203). |
| 9 Exceptions / failure | UserErrors on location mismatches, empty relocation, same package twice (VDR-U09-C204, VDR-U09-C197, VDR-U09-C205). |
| 10 Accounting / audit | Package history is the audit trail of package movements (VDR-U09-C212); no accounting effect. |

### DB reconciliation (configuration/structure only)
Restored DB: stock_package and stock_package_type have 0 rows; sequence stock.package (prefix PACK, padding 7) exists; group stock.group_tracking_lot implied by base.group_user; ACL rows as listed (package all users 1000, stock user/manager 1111; type user 1000 manager 1111 plus a sale_stock own-documents read row).

### Unknown / Runtime list
- RT: deep nesting, entire-pack automation and reusable totes in batch picking (stock_picking_batch not analysed).
- UNKNOWN: carrier and shipping weight integration lives in stock_delivery (discovered, not read).

## CAP-U09-08 Scrap

**Function-ID(s):** IAV-F04 for the loss-location aspects; FUNCTION MAPPING REQUIRED for the scrap order state machine

### D1 Business purpose and process semantics
A scrap order moves a quantity of a goods product (optionally lot, package, owner) from an internal location to an inventory-loss location. It is drafted, then validated; validation checks availability, books and completes one picked move, and optionally triggers replenishment. Reason tags are optional; scrap can be started from a transfer and, with mrp, from manufacturing orders. VDR-U09-C230, VDR-U09-C229, VDR-U09-C225, VDR-U09-C226, VDR-U09-C233, VDR-U09-C236

### D2 Architecture, data and object relationships
stock.scrap (name, company_id, product_id, product_uom_id, lot_id, package_id, owner_id, picking_id, location_id, scrap_location_id, scrap_qty, state, date_done, should_replenish, scrap_reason_tag_ids, move_ids) VDR-U09-C217, VDR-U09-C218; stock.scrap.reason.tag VDR-U09-C234; stock.move.scrap_id and reference VDR-U09-C232; stock.warn.insufficient.qty.scrap wizard VDR-U09-C227; mrp extension (production_id, workorder_id, bom_id) VDR-U09-C240. Sequence 'stock.scrap' prefix SP/ VDR-U09-C220.

### D3 Source, technical and workflow logic
action_validate: zero check -> check_available_qty (strict on location, lot, package, owner) -> do_scrap or warning wizard VDR-U09-C224, VDR-U09-C225, VDR-U09-C226. do_scrap: company check, name from sequence, create move (picked, scrap_id, loss location), _action_done(is_scrap), state done, date_done, optional do_replenish VDR-U09-C230, VDR-U09-C229, VDR-U09-C231, VDR-U09-C233. Wizard confirm calls do_scrap with cleaned context; discard unlinks draft VDR-U09-C227.
State diagram:
- draft -> done [action_validate / do_scrap]
- draft -> deleted [unlink by user/manager or wizard discard]
- done -> (none) [no cancel, delete refused]
Override chain: base stock.scrap + mrp (location, kit explode, unpick lots, replenish group) VDR-U09-C240.

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Create, validate; move completes; stock leaves source location to loss location. VDR-U09-C230, VDR-U09-C229 |
| 2 Reversal/cancel/negative | No cancel or reverse; done scrap cannot be deleted; over-scrap allowed after warning, giving negative stock (VDR-U09-C219, VDR-U09-C226, VDR-U09-C227, VDR-U09-C228). |
| 3 Multi-company / scope | company_id required, check_company, rule company_ids only (VDR-U09-C241, VDR-U09-C287). |
| 4 Side effects | Procurement for replenishment; accounting through loss location (stock_account); transfers with all moves scrapped become cancelled/done accordingly (VDR-U09-C233, VDR-U09-C239). |
| 5 Configuration / optionality | should_replenish, reason tags, lot required in form only with lots feature (VDR-U09-C235). |
| 6 Validation / constraints | Zero quantity, availability warning, consumable product domain (VDR-U09-C224, VDR-U09-C221). |
| 7 Roles / permissions | stock user create/write, manager delete; picking action Scrap without group (VDR-U09-C241, VDR-U09-C237). |
| 8 Scheduled / automated | None. |
| 9 Exceptions / failure | UserErrors for zero and delete; wizard cancel unlinks draft (VDR-U09-C224, VDR-U09-C219, VDR-U09-C227). |
| 10 Accounting / audit | Chatter on scrap, reference and origin on move; accounting via loss location valuation account; scrapped lines excluded from returns (VDR-U09-C217, VDR-U09-C232, VDR-U09-C238, VDR-U09-C133). |

### DB reconciliation (configuration/structure only)
Restored DB: stock_scrap 0 rows, scrap reason tags 0; ACL rows user 1110/manager 1111; company rule present; sequence stock.scrap SP/ padding 5 exists; the only inventory-usage location is 'Inventory adjustment' so scrap defaults to the same location as counts.

### Unknown / Runtime list
- RT: scrap of kit products, multi-step transfers and wizard discard behaviour.
- UNKNOWN: link of scrap to returns beyond the return wizard skipping inventory-destination moves (no other link found in stock).

## CAP-U09-09 Stock quantity computations and history views

**Function-ID(s):** RCN-F01 (Stock Moves History / Stock Report) for the history/report side; quantity computations map to RCN-F01 only partially

### D1 Business purpose and process semantics
Product on-hand, free, incoming, outgoing and forecast quantities are computed on demand from quants and open moves, scoped by companies, warehouse, location, lot, owner, package and date through context. History views (Moves History, quant history, stock-at-date, stock quantity report, replenishment report) expose the same data. VDR-U09-C244, VDR-U09-C245, VDR-U09-C252, VDR-U09-C261, VDR-U09-C269

### D2 Architecture, data and object relationships
product.product computed fields with stock_quant_ids/stock_move_ids (VDR-U09-C244, VDR-U09-C326); product.template sums variants VDR-U09-C257; report.stock.quantity SQL view VDR-U09-C269, VDR-U09-C270, VDR-U09-C271; stock.quantity.history wizard VDR-U09-C268; stock.forecasted_product_product/template abstract reports VDR-U09-C273, VDR-U09-C274; stock.move.line views and filters VDR-U09-C261, VDR-U09-C262, VDR-U09-C263; product_expiry context with_expiration VDR-U09-C255, VDR-U09-C256.

### D3 Source, technical and workflow logic
_compute_quantities -> _compute_quantities_dict: locations from context (_get_domain_locations: warehouse/location/default company warehouses, strict option, final destination for undone moves) VDR-U09-C247, VDR-U09-C248, VDR-U09-C249, VDR-U09-C250; quant sums and move sums by state VDR-U09-C251; past dates back out later done moves VDR-U09-C253, VDR-U09-C254; formulas VDR-U09-C252; searches use quants only when no date VDR-U09-C258; services zero VDR-U09-C246. Report view built in init from quants and moves for a period VDR-U09-C271.
State diagram: NOT APPLICABLE - quantities are derived, not stateful; (report view) rebuilt at module init/upgrade.
Override chain: base + product_expiry (_compute_quantities_dict context, help text) + stock_account (value) + others not analysed.

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Open product: on-hand/forecast computed in context of selected companies; Moves History lists done lines. VDR-U09-C252, VDR-U09-C261 |
| 2 Reversal/cancel/negative | Past-date quantities back out later done moves; negative on-hand shown as is (VDR-U09-C254). |
| 3 Multi-company / scope | Scope = warehouses of env.companies; report rule company_ids; product company change guard (VDR-U09-C247, VDR-U09-C272, VDR-U09-C259). |
| 4 Side effects | Making product storable books history-matching adjustments (VDR-U09-C260); expired stock subtracted (VDR-U09-C255). |
| 5 Configuration / optionality | Context keys, report period parameter, strict option (VDR-U09-C245, VDR-U09-C271, VDR-U09-C249). |
| 6 Validation / constraints | Services zero; strict scope; date end-of-day rounding (VDR-U09-C246, VDR-U09-C253). |
| 7 Roles / permissions | Reporting menu manager-only; report model read for all users; move line ACL broad (VDR-U09-C265, VDR-U09-C272, VDR-U09-C125). |
| 8 Scheduled / automated | Report view recreated at init only; no cron. |
| 9 Exceptions / failure | None specific; performance risk for past dates (RT). |
| 10 Accounting / audit | Moves History is the audit view of all done lines incl. inventory/scrap (VDR-U09-C261, VDR-U09-C263). |

### DB reconciliation (configuration/structure only)
Restored DB: no moves/quants, so reports render empty; report period parameter not set (default 3 months); product_expiry installed (with_expiration active); one company, one warehouse.

### Unknown / Runtime list
- RT: numeric results of forecast, back-dating and report view on populated data.
- UNKNOWN: JS-rendered Replenishment report layout and stock_forecasted_product_template details not exhaustively read.

## CAP-U09-10 Roles, record rules, ACL, scheduled behaviour and failure paths

**Function-ID(s):** FUNCTION MAPPING REQUIRED (security and scheduling of the unit)

### D1 Business purpose and process semantics
Two roles - Inventory User and Inventory Administrator - govern counting, scrap, lots, packages and reports; company record rules scope data; the daily procurement scheduler performs quant maintenance and expiry alerts. VDR-U09-C276, VDR-U09-C278, VDR-U09-C292

### D2 Architecture, data and object relationships
res.groups stock.group_stock_user / group_stock_manager and hidden feature groups (multi-locations, lots, packages, owners...); ir.model.access rows in stock/security/ir.model.access.csv; ir.rule rows in stock/security/stock_security.xml; cron ir_cron_scheduler_action; server actions with group_ids VDR-U09-C282.

### D3 Source, technical and workflow logic
Access: ACL rows decide table rights VDR-U09-C278, VDR-U09-C279, VDR-U09-C280, VDR-U09-C281; ir.rules scope companies VDR-U09-C284, VDR-U09-C285, VDR-U09-C286, VDR-U09-C287, VDR-U09-C288, VDR-U09-C289, VDR-U09-C290; code guards add finer limits (unlink, inventory mode) VDR-U09-C018, VDR-U09-C042. Scheduler: cron -> stock.rule.run_scheduler -> tasks incl. _quant_tasks; extension product_expiry adds alert task VDR-U09-C292, VDR-U09-C293, VDR-U09-C183.
State diagram: NOT APPLICABLE (roles/rules are static; cron is a recurring job).
Override chain: base stock + mrp_subcontracting (portal rules/ACL) + product_expiry (ACL for expiry wizard, group) + stock_account (field groups).

### Ten-dimension analysis

| Dimension | Finding (claim refs) |
|---|---|
| 1 Happy path | Stock user counts and scraps; manager administers; all internal users read availability. VDR-U09-C278, VDR-U09-C280 |
| 2 Reversal/cancel/negative | Deletion limits: quants (manager), scrap (manager), lots (user ACL) (VDR-U09-C018, VDR-U09-C219, VDR-U09-C178). |
| 3 Multi-company / scope | Rules with and without the no-company clause as listed (VDR-U09-C284, VDR-U09-C287, VDR-U09-C289). |
| 4 Side effects | Manager actions change counts and location structure (VDR-U09-C282). |
| 5 Configuration / optionality | Feature groups implied for internal users in the restored DB (VDR-U09-C179, VDR-U09-C213, VDR-U09-C331). |
| 6 Validation / constraints | Code guards listed in CAP-01..08. |
| 7 Roles / permissions | Confirmed against restored DB for stock.quant, stock.lot, stock.scrap, stock.package, stock.package.type, wizards, report; global rules; 2 administrators, 0 explicit users (VDR-U09-C277, VDR-U09-C278). |
| 8 Scheduled / automated | One daily cron; product_expiry hooks; no count cron (VDR-U09-C292, VDR-U09-C183, VDR-U09-C107). |
| 9 Exceptions / failure | Scheduler logs and re-raises; listed UserErrors; wizard ACL uncertainty (VDR-U09-C293, VDR-U09-C294, VDR-U09-C298). |
| 10 Accounting / audit / security | Broad table rights on move lines (code-guarded); value fields manager-only; no chatter on quants (VDR-U09-C294, VDR-U09-C125, VDR-U09-C283). |

### DB reconciliation (configuration/structure only)
Restored DB: ACL and rule rows match the declared source (queried by model); rules are global; Administrator group has 2 members and User group 0 explicit members (counts only); cron 'Procurement: run scheduler' daily active; stock.barcode_separator is the only stock config parameter set; hidden feature groups multi-locations, lots/serials, packages, push/pull flows, owners, partner warnings and reception report are implied by base.group_user.

### Unknown / Runtime list
- RT: effective permission of ordinary stock users on administrator-only transient dialogs.
- UNKNOWN: production cron timing and any server-level overrides are not visible in source.

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U09-C001 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:19 | _name = 'stock.quant' | FACT | always | — | Model stock.quant (description Quants) is the on-hand record; _rec_names_search covers location, lot, package, owner. | N-U09-001 |
| VDR-U09-C002 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:78-81 | readonly=True, digits= | FACT | always | — | Field quantity is declared readonly=True; it is not user-editable through the ORM views. | N-U09-003 |
| VDR-U09-C003 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:82-86 | reserved_quantity = fields.Float( | FACT | always | — | Field reserved_quantity is readonly=True, required=True, default 0.0. | N-U09-003 |
| VDR-U09-C004 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:119-122 | quant.quantity - quant.reserved_quantity | FACT | always | — | available_quantity is computed as quantity minus reserved_quantity (no stored column). | N-U09-001 |
| VDR-U09-C005 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:56 | related='location_id.company_id' | FACT | always | — | company_id is stored and related to the location company; a record in a company-less location has no company. | N-U09-001 |
| VDR-U09-C006 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:45-48 | ondelete='restrict', required=True | FACT | always | — | product_id is required, restricted on delete, indexed and check_company; location_id is likewise required and restricted on delete. | N-U09-001 |
| VDR-U09-C007 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:245-246 | cannot duplicate stock quants | FACT | always | — | copy() raises UserError 'You cannot duplicate stock quants.'. | N-U09-006 |
| VDR-U09-C008 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:582-585 | Quants cannot be created for consumables | FACT | always | — | Constraint check_product_id on product_id raises ValidationError unless the product is_storable. | N-U09-005 |
| VDR-U09-C009 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:587-603 | already been assigned | FACT | always | — | check_quantity: for serial-tracked products outside inventory-type locations, if abs(sum of quantity) over the child_of location tree for that lot exceeds 1 it raises 'The serial number has already been assigned'. | N-U09-015 |
| VDR-U09-C010 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:605-609 | usage == 'view' | FACT | always | — | Constraint check_location_id forbids a quant in a location of usage view. | N-U09-016 |
| VDR-U09-C011 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:611-615 | linked to another product | FACT | always | — | Constraint check_lot_id requires lot.product_id to equal quant.product_id. | N-U09-016 |
| VDR-U09-C012 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:346-349 | product_id', 'location_id', 'lot_id | FACT | always | — | _get_forbidden_fields_write returns product_id, location_id, lot_id, package_id, owner_id. | N-U09-007 |
| VDR-U09-C013 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:351-360 | Quant's editing is restricted | FACT | inventory mode and user in stock user group | — | write(): in inventory mode a write containing a forbidden field raises UserError; if any quant in the set is in a location of usage inventory the write returns silently instead. | N-U09-007 |
| VDR-U09-C014 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:355-357 | Do nothing when user tries | FACT | inventory mode | — | A forbidden-field write on a quant located in an inventory-usage location is silently ignored (comment: 'Do nothing when user tries to modify manually a inventory loss'). | N-U09-007 |
| VDR-U09-C015 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:266-269 | creation is restricted | FACT | inventory mode and counted field present | — | create() in inventory mode with inventory_quantity or inventory_quantity_auto_apply refuses any other field outside _get_inventory_fields_create (x_ custom fields are exempt). | N-U09-007 |
| VDR-U09-C016 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1238-1251 | inventory_diff_quantity | FACT | always | — | Allowed create fields are product_id and owner_id plus the write list: inventory_quantity, inventory_quantity_auto_apply, inventory_diff_quantity, inventory_date, user_id, inventory_quantity_set, is_outdated, lot_id, location_id, package_id (stock_account adds accounting_date). | N-U09-007 |
| VDR-U09-C017 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:280-295 | strict=True | FACT | inventory mode create | — | In inventory-mode create the code first _gather()s an existing quant with strict=True and re-uses it (as sudo) instead of creating a duplicate, except during file import where merging is deferred. | N-U09-007 |
| VDR-U09-C018 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:362-366 | ask a stock manager | FACT | not superuser | — | Quant unlink by a user outside stock manager raises UserError 'Quants are auto-deleted when appropriate...'. | N-U09-008 |
| VDR-U09-C019 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:367-369 | self._apply_inventory() | INFERENCE | manager deletes quant | — | For a stock manager the ondelete hook sets inventory_quantity = 0 and calls _apply_inventory() before the row is removed, so a manual delete books an adjustment move (lines 367-369). | N-U09-008 |
| VDR-U09-C020 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1053-1056 | Quantity or Reserved Quantity | FACT | always | — | _update_available_quantity raises ValidationError if neither quantity nor reserved_quantity is passed, then runs as sudo and _gathers with strict=True. | N-U09-003 |
| VDR-U09-C021 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1079-1082 | try_lock_for_update | FACT | always | RT | The first gathered quant is locked with try_lock_for_update(allow_referencing=True, limit=1) (skip-locked semantics per orm/models.py); if no row can be locked a new quant is created. | N-U09-019 |
| VDR-U09-C022 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1084-1090 | max(0, quant.reserved_quantity | FACT | always | — | If a quant was locked, quantity is increased by the signed delta and reserved_quantity is floored at 0 via max(0, reserved + delta). | N-U09-004 |
| VDR-U09-C023 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1091-1104 | self.create(vals) | INFERENCE | no lockable quant found | RT | When no existing quant could be locked, a fresh quant row is created even if a locked one exists for the same key; duplicates are therefore possible under concurrency (lines 1079-1104). | N-U09-017 |
| VDR-U09-C024 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1105 | allow_negative=True | FACT | always | — | _update_available_quantity returns the strict-key available quantity computed with allow_negative=True, i.e. a negative figure is returned, not blocked. | N-U09-009 |
| VDR-U09-C025 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:793-832 | allow_negative | FACT | always | — | _get_available_quantity clamps negative results to 0 unless allow_negative=True; for tracked products it sums positive per-lot buckets only. | N-U09-009 |
| VDR-U09-C026 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1177-1183 | to not rollback | FACT | always | — | _merge_quants docstring states a concurrent create is allowed so transactions do not roll back and duplicates are later deduplicated. | N-U09-017 |
| VDR-U09-C027 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1203 | GROUP BY product_id, company_id | FACT | always | — | Duplicate detection groups stock_quant by product_id, company_id, location_id, lot_id, package_id, owner_id having count>1. | N-U09-011 |
| VDR-U09-C028 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1187-1192 | GREATEST(0, SUM(reserved_quantity)) | FACT | always | — | Merge keeps the lowest id, sums quantity and inventory_quantity, takes min(in_date) and GREATEST(0, SUM(reserved_quantity)), then deletes the other ids. | N-U09-011 |
| VDR-U09-C029 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1217-1222 | error occurred while merging | FACT | always | RT | The merge runs in a savepoint and on a PG error only logs at info level and continues (no user-visible failure). | N-U09-017 |
| VDR-U09-C030 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1224-1228 | self._merge_quants() | FACT | always | — | _quant_tasks runs _merge_quants, _clean_reservations, _unlink_zero_quants in that order. | N-U09-011 |
| VDR-U09-C031 | FUNCTION MAPPING REQUIRED | stock/models/stock_rule.py:722 | _quant_tasks() | FACT | scheduler cron active | — | run_scheduler's _run_scheduler_tasks calls stock.quant._quant_tasks() as its last step (comment: Merge duplicated quants). | N-U09-012 |
| VDR-U09-C032 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:405-406 | stock.skip_quant_tasks | FACT | parameter absent | — | action_view_inventory (and _get_quants_action at 1315-1316) run _quant_tasks() on opening the screen unless config parameter stock.skip_quant_tasks is set. | N-U09-012 |
| VDR-U09-C033 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1130-1137 | AND user_id IS NULL | FACT | always | — | _unlink_zero_quants selects quants whose quantity, reserved_quantity and inventory_quantity all round to zero (or NULL) and user_id IS NULL, then unlinks them as sudo. | N-U09-011 |
| VDR-U09-C034 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1141-1175 | def _clean_reservations | FACT | always | — | _clean_reservations compares sum(reserved_quantity) per key against move-line reserved quantity in states assigned/partially_available/waiting/confirmed and re-aligns the quant via _update_reserved_quantity. | N-U09-011 |
| VDR-U09-C035 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1163-1164 | should_bypass_reservation | FACT | always | — | For locations that bypass reservation (supplier, customer, inventory, production usage) any reserved quantity found on quants is removed. | N-U09-011 |
| VDR-U09-C036 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:698-706 | if available_qty < 0 | FACT | always | — | stock.move.line._action_done moves quants via _synchronize_quant and, if the source available quantity ends negative, calls _free_reservation to release other un-picked reservations; there is no raise for negative on-hand. | N-U09-009 |
| VDR-U09-C037 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:716-736 | not self.product_id.is_storable | FACT | always | — | _synchronize_quant returns (0, False) for non-storable products or zero quantity, otherwise dispatches to _update_available_quantity or _update_reserved_quantity. | N-U09-003 |
| VDR-U09-C038 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:617-628 | return 'fifo' | FACT | always | — | _get_removal_strategy: product category removal_strategy_id, else walks location parents' removal_strategy_id, else defaults to 'fifo'. | N-U09-010 |
| VDR-U09-C039 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:740-748 | in_date ASC, id | FACT | always | — | _get_removal_strategy_order: fifo and least_packages order by in_date ASC, id; lifo by in_date DESC, id DESC; closest returns False; other values raise UserError 'not implemented'. | N-U09-010 |
| VDR-U09-C040 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:760-766 | Domain('location_id', '=', location_id.id) | FACT | strict=True | — | With strict=True _get_gather_domain matches exact lot (or none), package, owner and exact location; non-strict uses child_of location. | N-U09-001 |
| VDR-U09-C041 | FUNCTION MAPPING REQUIRED | stock/views/stock_quant_views.xml:44 | name="negative" | FACT | always | — | The quant search view carries a Negative Stock filter quantity < 0.0. | N-U09-009 |
| VDR-U09-C042 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1230-1236 | has_group('stock.group_stock_user') | FACT | always | — | _is_inventory_mode is true only when context inventory_mode is set AND the user is in stock.group_stock_user. | N-U09-012 |
| VDR-U09-C043 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1302-1305 | inventory_mode=True | FACT | user in stock user group | — | _set_view_context adds inventory_mode=True for stock users; without multi-locations group it also sets default location to the first warehouse lot_stock. | N-U09-012 |
| VDR-U09-C044 | FUNCTION MAPPING REQUIRED | stock/models/stock_move.py:2242-2247 | .check_quantity() | FACT | always | — | After done moves, stock.move._check_quantity re-runs quant.check_quantity() for the product/lot set in the destination location tree. | N-U09-015 |
| VDR-U09-C045 | FUNCTION MAPPING REQUIRED | product_expiry/models/stock_quant.py:30-36 | quant.available_quantity = 0 | FACT | product_expiry installed (observed installed) | — | _compute_available_quantity zeroes available_quantity when use_expiration_date and removal_date <= now. | N-U09-013 |
| VDR-U09-C046 | FUNCTION MAPPING REQUIRED | product_expiry/models/stock_quant.py:24-28 | removal_date, in_date, id | FACT | product_expiry installed | — | FEFO removal strategy orders quants by removal_date, in_date, id. | N-U09-010 |
| VDR-U09-C047 | FUNCTION MAPPING REQUIRED | mrp/models/stock_quant.py:8-11 | components quantity instead | FACT | mrp installed (observed installed) | — | Constraint on product_id raises UserError for kit (is_kits) products: update component quantities instead. Discovered supporting module mrp. | N-U09-013 |
| VDR-U09-C048 | FUNCTION MAPPING REQUIRED | stock_account/models/stock_quant.py:47-65 | def _compute_value | FACT | stock_account installed | — | stock_account adds computed value (manager-only field) = quantity * product (or lot) total_value / qty_available for quants in valued locations. Discovered supporting module stock_account; hand-off to the valuation unit. | N-U09-013 |
| VDR-U09-C049 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1549-1564 | Quantity Relocated | FACT | always | — | move_quants builds an inventory-flagged stock.move per quant (default reference 'Quantity Relocated') and completes it; quants are relocated by moves, not by editing location_id. | N-U09-003 |
| VDR-U09-C050 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:452-454 | single company per relocation | FACT | always | — | action_stock_quant_relocate requires positive quantities, quants all with a company, and a single company in the selection, else UserError. | N-U09-003 |
| VDR-U09-C051 | IAV-F01 | stock/models/stock_quant.py:97-99 | 'Counted' | FACT | always | — | stock.quant.inventory_quantity (label 'Counted') stores the counted figure; it is a plain stored Float. | N-U09-022 |
| VDR-U09-C052 | IAV-F01 | stock/models/stock_quant.py:185-191 | quant.inventory_quantity - quant.quantity | FACT | always | — | inventory_diff_quantity (stored) = inventory_quantity - quantity when inventory_quantity_set, else 0. | N-U09-023 |
| VDR-U09-C053 | IAV-F01 | stock/models/stock_quant.py:193-195 | self.inventory_quantity_set = True | FACT | always | — | _compute_inventory_quantity_set sets inventory_quantity_set to True whenever inventory_quantity is (re)computed/written. | N-U09-023 |
| VDR-U09-C054 | IAV-F01 | stock/models/stock_quant.py:197-202 | quant.is_outdated = True | FACT | always | — | is_outdated is true when inventory_quantity_set and (inventory_quantity - inventory_diff_quantity) differs from current quantity, i.e. on-hand moved since the count. | N-U09-023 |
| VDR-U09-C055 | IAV-F01 | stock/models/stock_quant.py:512-516 | quant.inventory_quantity = quant.quantity | FACT | not from request count | — | action_set_inventory_quantity copies quantity into inventory_quantity (unless context from_request_count), assigns user_id to the current user and sets inventory_quantity_set True. | N-U09-032 |
| VDR-U09-C056 | IAV-F01 | stock/models/stock_quant.py:497-511 | Quantities Already Set | FACT | some selected quants already set | — | If any selected quant already has inventory_quantity_set it opens the stock.inventory.warning wizard instead of setting. | N-U09-039 |
| VDR-U09-C057 | IAV-F01 | stock/models/stock_quant.py:545-549 | self.inventory_quantity_set = False | FACT | always | — | action_clear_inventory_quantity zeroes inventory_quantity and inventory_diff_quantity, unsets the flag and clears user_id. | N-U09-032 |
| VDR-U09-C058 | IAV-F01 | stock/models/stock_quant.py:551-556 | def action_set_inventory_quantity_zero | FACT | always | — | action_set_inventory_quantity_zero sets inventory_quantity 0; in report mode it applies immediately, else only assigns the user. | N-U09-032 |
| VDR-U09-C059 | IAV-F01 | stock/views/stock_quant_views.xml:337-345 | Set to 0 | FACT | always | — | Server action 'Set to 0' (bound to stock.quant list/kanban) is limited to group stock.group_stock_manager; 'Set to quantity on hand' to group_stock_user. | N-U09-035 |
| VDR-U09-C060 | IAV-F02 | stock/models/stock_quant.py:433-450 | self._apply_inventory(date) | FACT | always | — | action_apply_inventory: if any selected quant is_outdated it returns the stock.inventory.conflict wizard; otherwise runs _apply_inventory(date) then unsets inventory_quantity_set. | N-U09-024 |
| VDR-U09-C061 | IAV-F02 | stock/models/stock_quant.py:436-448 | Conflict in Inventory Adjustment | FACT | outdated quants present | — | The conflict dialog is opened with default_quant_ids and default_quant_to_fix_ids (the outdated subset). | N-U09-024 |
| VDR-U09-C062 | IAV-F02 | stock/wizard/stock_inventory_conflict.py:16-24 | action_keep_counted_quantity | FACT | always | — | Keep counted: diff := counted - quantity; keep difference: counted := quantity + diff; both then re-call action_apply_inventory on all selected quants. | N-U09-024 |
| VDR-U09-C063 | IAV-F02 | stock/models/stock_quant.py:518-529 | def action_apply_all | FACT | always | — | action_apply_all takes the context active_domain, searches all matching quants and opens the stock.inventory.adjustment.name wizard with them as default_quant_ids. | N-U09-025 |
| VDR-U09-C064 | IAV-F02 | stock/wizard/stock_inventory_adjustment_name.py:12-13 | Physical Inventory | FACT | always | — | Wizard fields: inventory_adjustment_name (Char, default 'Physical Inventory', not required) and counting_date (Datetime, default now). | N-U09-025 |
| VDR-U09-C065 | IAV-F02 | stock/wizard/stock_inventory_adjustment_name.py:21-23 | filtered('inventory_quantity_set') | FACT | always | — | action_apply applies only quants with inventory_quantity_set, passing inventory_name and counting_date in context and counting_date as the date argument. | N-U09-025 |
| VDR-U09-C066 | IAV-F02 | stock/views/stock_quant_views.xml:280-287 | action_apply_all | FACT | inventory report mode off | — | Inventory list header has Apply All (inventory mode only), Apply (opens the reason wizard), Clear and Request a Count (both manager group). | N-U09-035 |
| VDR-U09-C067 | IAV-F02 | stock/views/stock_quant_views.xml:319 | action_apply_inventory | FACT | always | — | Each editable list row has an Apply button calling action_apply_inventory directly (visible when inventory_quantity_set), bypassing the reason wizard. | N-U09-026 |
| VDR-U09-C068 | IAV-F02 | stock/models/stock_move.py:357-368 | Product Quantity Updated | FACT | always | — | stock.move.reference for is_inventory moves: inventory_name if provided, else 'Product Quantity Confirmed' (zero qty) or 'Product Quantity Updated' plus the creator's display name. | N-U09-026 |
| VDR-U09-C069 | IAV-F02 | stock/models/stock_quant.py:1015-1025 | quant.inventory_diff_quantity | FACT | always | — | _apply_inventory: diff>0 builds move loss_location -> quant location (package_dest = quant package); otherwise builds move quant location -> loss_location with qty -diff (zero included). | N-U09-027 |
| VDR-U09-C070 | IAV-F02 | stock/models/stock_move.py:2262 | not move.is_inventory | FACT | always | — | stock.move._action_done does not cancel zero-quantity moves flagged is_inventory, so zero-difference counts complete as confirmation moves. | N-U09-027 |
| VDR-U09-C071 | IAV-F02 | stock/models/stock_move_line.py:646 | elif not ml.is_inventory | FACT | always | — | stock.move.line._action_done deletes zero-quantity lines except when the move is_inventory. | N-U09-027 |
| VDR-U09-C072 | IAV-F02 | stock/models/stock_quant.py:1265-1276 | 'is_inventory': True | FACT | always | — | _get_inventory_move_values sets state confirmed, is_inventory True, picked True, restrict_partner_id = owner, with one move line carrying lot, package, result package and owner. | N-U09-028 |
| VDR-U09-C073 | IAV-F02 | stock/models/stock_quant.py:1026-1027 | _action_done() | FACT | always | — | Moves are created with inventory_mode=False and completed with _action_done under context ignore_dest_packages=True. | N-U09-028 |
| VDR-U09-C074 | IAV-F02 | stock/models/stock_quant.py:1028-1029 | moves.date = date | FACT | date passed | — | If a counting date is supplied, moves.date is overwritten after completion; stock.move.write propagates a date change on done moves to their lines (stock_move.py:883-884). | N-U09-029 |
| VDR-U09-C075 | IAV-F02 | stock/models/stock_quant.py:1031-1034 | last_inventory_date | FACT | always | — | After apply, each counted location gets last_inventory_date = today (sudo write) and each applied quant inventory_date = location._get_next_inventory_date(). | N-U09-029 |
| VDR-U09-C076 | IAV-F02 | stock/models/stock_quant.py:1012-1013 | property_stock_inventory | FACT | always | — | The counterpart is product.property_stock_inventory (company-dependent) else the ir.default for product.template.property_stock_inventory of the quant company. | N-U09-036 |
| VDR-U09-C077 | IAV-F02 | stock/models/stock_quant.py:1030 | moves._trigger_assign() | FACT | always | — | After completion the applied moves call _trigger_assign() so waiting moves re-check availability. | N-U09-036 |
| VDR-U09-C078 | IAV-F02 | stock/models/stock_quant.py:100-104 | inverse='_set_inventory_quantity' | FACT | group_stock_user for the field | — | inventory_quantity_auto_apply is a computed field with inverse _set_inventory_quantity; writing it (inventory mode) copies it to inventory_quantity and immediately calls action_apply_inventory. | N-U09-030 |
| VDR-U09-C079 | IAV-F02 | stock/models/stock_quant.py:225-237 | quant_to_inventory.action_apply_inventory() | FACT | inventory mode | — | _set_inventory_quantity skips quants whose quantity already equals the value and applies the rest. | N-U09-030 |
| VDR-U09-C080 | IAV-F01 | stock/models/stock_quant.py:297-304 | quant.inventory_date = fields.Date.today() | FACT | inventory-mode create with counted field | — | Create path: if inventory_quantity_auto_apply used, writes it (immediate apply); else sets inventory_quantity, user_id (default current user) and inventory_date today on the found or new quant. | N-U09-030 |
| VDR-U09-C081 | IAV-F01 | stock/wizard/stock_request_count.py:31-35 | inventory_mode=True).write | FACT | manager group | — | action_request_count writes inventory_date and user_id on the selected quants (plus siblings) in inventory mode; it does not create counted quantities. | N-U09-031 |
| VDR-U09-C082 | IAV-F01 | stock/wizard/stock_request_count.py:37-52 | Searches sibling quants | FACT | user in group_production_lot and tracked quants | — | _get_quants_to_count adds all quants of the same product and location when any selected quant is tracked and the user has stock.group_production_lot. | N-U09-031 |
| VDR-U09-C083 | IAV-F01 | stock/wizard/stock_request_count.py:19-29 | stock.show_expected_quantity_count | FACT | always | — | show_expected_quantity is stored as the ir.config_parameter stock.show_expected_quantity_count ('True'/'False'), system-wide not per request. | N-U09-031 |
| VDR-U09-C084 | IAV-F01 | stock/models/stock_quant.py:115-117 | Assigned To | FACT | always | — | quant.user_id ('Assigned To') is limited to users in stock.group_stock_user. | N-U09-031 |
| VDR-U09-C085 | IAV-F02 | stock/models/product.py:280-292 | from_inverse_qty=True | FACT | product type consu, storable, qty>=0 | — | product.product._inverse_qty_available creates a quant in the first warehouse lot_stock of env.company with inventory_quantity = qty_available and calls _apply_inventory(). | N-U09-033 |
| VDR-U09-C086 | IAV-F02 | stock/models/stock_quant.py:1008-1011 | from_inverse_qty | FACT | from product inverse | — | _apply_inventory skips a quant whose diff is zero when context from_inverse_qty is set (no zero move from the product form). | N-U09-033 |
| VDR-U09-C087 | IAV-F01 | stock/models/stock_quant.py:131-177 | 'is_inventory', '=', True | FACT | always | — | last_count_date is computed from the max date of done inventory-flagged move lines touching the quant key (location as source or destination, package as source or result). | N-U09-023 |
| VDR-U09-C088 | IAV-F01 | stock/models/stock_quant.py:418-419 | 'internal', 'transit' | FACT | always | — | action_view_inventory ('Physical Inventory') domain: location usage in internal/transit; non-manager stock users get default filter My Counts (lines 410-411). | N-U09-037 |
| VDR-U09-C089 | IAV-F01 | stock/views/stock_quant_views.xml:4-12 | group_stock_user | FACT | always | — | Server action physical-inventory is limited to group stock.group_stock_user. | N-U09-035 |
| VDR-U09-C090 | IAV-F01 | stock/views/stock_quant_views.xml:39-44 | name="to_apply" | FACT | always | — | Quant search filters: To Count (inventory_date <= today), To Apply (inventory_quantity_set), Conflicts (is_outdated), Negative Stock. | N-U09-034 |
| VDR-U09-C091 | IAV-F02 | stock/security/ir.model.access.csv:66-67 | access_stock_inventory_conflict | FACT | always | RT | ACL rows for stock.inventory.conflict and stock.inventory.warning grant only group stock.group_stock_manager (read/write/create). Whether an ordinary stock user can open them is not shown by source alone. | N-U09-039 |
| VDR-U09-C092 | IAV-F02 | stock/security/ir.model.access.csv:69 | access_stock_inventory_adjustment_name_user | FACT | always | — | The reason wizard stock.inventory.adjustment.name is granted to both stock user and manager. | N-U09-035 |
| VDR-U09-C093 | IAV-F02 | stock/models/stock_quant.py:433-450 | def action_apply_inventory | UNKNOWN | runtime | RT | UNKNOWN: effect of a non-manager stock user hitting the conflict wizard (ACL create is manager-only at ir.model.access.csv:66) needs a runtime test. | N-U09-040 |
| VDR-U09-C094 | IAV-F01 | stock/wizard/stock_request_count.py:58-59 | values['user_id'] = self.user_id.id, | INFERENCE | assignee chosen in request | RT | Line 59 ends with a trailing comma so values['user_id'] is a one-element tuple; whether the ORM many2one conversion accepts it is not shown by source alone (works only if it unwraps the tuple). | N-U09-031 |
| VDR-U09-C095 | IAV-F05 | stock/models/stock_location.py:81-83 | cyclic_inventory_frequency = fields.Integer | FACT | always | — | stock.location fields: cyclic_inventory_frequency (Integer, default 0), last_inventory_date (Date, readonly), next_inventory_date (Date, stored computed). | N-U09-041 |
| VDR-U09-C096 | IAV-F05 | stock/models/stock_location.py:97-100 | check(cyclic_inventory_frequency >= 0) | FACT | always | — | SQL constraint _inventory_freq_nonneg: frequency must be non-negative. | N-U09-043 |
| VDR-U09-C097 | IAV-F05 | stock/models/stock_location.py:141-157 | days_until_next_inventory | FACT | company set, usage internal or transit, frequency > 0 | — | _compute_next_inventory_date: if last_inventory_date exists and the remaining days <= 0 -> today+1; if remaining > 0 -> last+frequency; if never counted -> today+frequency; else (conditions not met) False. | N-U09-044 |
| VDR-U09-C098 | IAV-F05 | stock/models/stock_location.py:154-155 | too far into the future | FACT | date overflow | — | OverflowError during date arithmetic raises UserError 'The selected Inventory Frequency (Days) creates a date too far into the future.'. | N-U09-043 |
| VDR-U09-C099 | IAV-F05 | stock/models/stock_location.py:144 | location.company_id and location.usage in | FACT | always | — | A location without company or of another usage gets next_inventory_date False. | N-U09-052 |
| VDR-U09-C100 | IAV-F05 | stock/models/stock_location.py:405-409 | min(self.next_inventory_date | FACT | always | CONTRA | _get_next_inventory_date returns min(location.next_inventory_date, company annual date) when both exist, annual date alone when only that exists. CONTRA prior IAV-F05 text that the annual date applies only where frequency is unset (0): the annual date also caps a cyclic date. | N-U09-045 |
| VDR-U09-C101 | IAV-F05 | stock/models/stock_location.py:392-404 | max(self.company_id.annual_inventory_day, 1) | FACT | annual_inventory_month set | — | Annual date: day clamped to >=1 and <= month length (leap-year handled); if the date this year is <= today, the next year is used; usage not internal/transit returns False (line 384-385). | N-U09-046 |
| VDR-U09-C102 | IAV-F05 | stock/models/res_company.py:37-41 | default='12' | FACT | always | — | res.company.annual_inventory_month default '12' (December), annual_inventory_day default 31; help text: for products not in a location with a cyclic inventory date; set no month for no annual inventory. | N-U09-046 |
| VDR-U09-C103 | IAV-F05 | stock/models/stock_quant.py:124-129 | @api.depends('location_id') | INFERENCE | always | — | quant.inventory_date is computed only for quants lacking a date in internal/transit locations and depends solely on location_id, so later frequency edits do not recompute stored dates (stock_quant.py:124-129). | N-U09-047 |
| VDR-U09-C104 | IAV-F05 | stock/models/stock_quant.py:1031-1034 | _get_next_inventory_date() | FACT | after apply | — | _apply_inventory sets last_inventory_date on the quant locations and recomputes inventory_date of the applied quants from _get_next_inventory_date(). | N-U09-047 |
| VDR-U09-C105 | IAV-F05 | stock/views/stock_quant_views.xml:39 | name="to_count" | FACT | always | — | A To Count filter (inventory_date <= today) is defined on the quant search view. | N-U09-048 |
| VDR-U09-C106 | IAV-F05 | stock/views/stock_quant_views.xml:308-312 | decoration-bf="inventory_date | FACT | always | — | Inventory list highlights inventory_date <= context_today(); no action is attached. | N-U09-048 |
| VDR-U09-C107 | IAV-F05 | stock/models/stock_rule.py:693-726 | # Merge duplicated quants | INFERENCE | always | — | The only stock scheduler (cron 'Procurement: run scheduler') runs orderpoints, move assignment and quant maintenance; no step creates or notifies counts (stock_sequence_data.xml:46-57 defines the cron). | N-U09-048 |
| VDR-U09-C108 | IAV-F05 | stock/views/stock_location_views.xml:46-51 | Cyclic Counting | FACT | usage internal or transit and company set | — | Location form group 'Cyclic Counting' shows frequency, last and next inventory date; the field itself has no stock.group_stock_multi_locations gate, but the Locations menu does (stock_location_views.xml:172). | N-U09-050 |
| VDR-U09-C109 | IAV-F05 | stock/wizard/stock_request_count.py:54-60 | 'inventory_date': self.inventory_date | FACT | manager group | — | Manual count requests write inventory_date (due date) and user_id onto quants; this is the only count scheduling action besides cyclic dates. | N-U09-051 |
| VDR-U09-C110 | IAV-F05 | stock/models/stock_rule.py:728-731 | return 3 | UNKNOWN | extensions | RT | UNKNOWN: whether any non-stock Community extension adds counting notifications; base stock scheduler has 3 tasks (stock_rule.py:728-731). | N-U09-054 |
| VDR-U09-C111 | IAV-F06 | stock/models/stock_move_line.py:1205-1213 | def action_revert_inventory | FACT | always | — | stock.move.line.action_revert_inventory runs with inventory_mode False and processes only lines with is_inventory and non-zero quantity. | N-U09-058 |
| VDR-U09-C112 | IAV-F06 | stock/models/stock_move_line.py:1214-1222 | no inventory adjustments to revert | FACT | no qualifying line | — | If no line qualifies it returns a danger display_notification 'There are no inventory adjustments to revert.' and creates nothing. | N-U09-058 |
| VDR-U09-C113 | IAV-F06 | stock/models/stock_move_line.py:1178-1190 | [reverted] | FACT | always | — | _get_revert_inventory_move_values: inventory_name '<reference> [reverted]', state confirmed, is_inventory True, picked True, qty = line.quantity, locations swapped. | N-U09-059 |
| VDR-U09-C114 | IAV-F06 | stock/models/stock_move_line.py:1191-1202 | 'result_package_id': self.package_id.id | FACT | always | — | Reversal move line swaps package_id/result_package_id and keeps lot_id and owner_id; location_id = old location_dest_id. | N-U09-059 |
| VDR-U09-C115 | IAV-F06 | stock/models/stock_move_line.py:1223-1224 | moves._action_done() | FACT | always | — | Reversal moves are created then completed immediately with _action_done(); a list view of reverted + original lines is returned. | N-U09-059 |
| VDR-U09-C116 | IAV-F06 | stock/models/stock_move_line.py:1205-1231 | processed_move_line | INFERENCE | always | — | action_revert_inventory never writes to the original line nor searches for an existing reversal, so a second revert of the same line is not blocked (read of lines 1205-1231). | N-U09-060 |
| VDR-U09-C117 | IAV-F06 | stock/views/stock_move_line_views.xml:215-224 | Revert Inventory Adjustment | FACT | always | — | Server action 'Revert Inventory Adjustment' is bound to stock.move.line (list actions) with no group_ids restriction on the action record. | N-U09-064 |
| VDR-U09-C118 | IAV-F06 | stock/models/stock_quant.py:1557-1562 | _get_inventory_move_values | INFERENCE | always | — | move_quants (relocate, unpack, package relocate, lot relocate) builds moves via _get_inventory_move_values which sets is_inventory True, so those moves are also revertible with this action (Q:1274 and 1557). | N-U09-061 |
| VDR-U09-C119 | IAV-F06 | stock/models/stock_scrap.py:125-150 | 'picked': True | INFERENCE | always | — | Scrap _prepare_move_values has no is_inventory key; scrap moves are therefore not selectable by the revert filter. | N-U09-061 |
| VDR-U09-C120 | IAV-F06 | stock/models/stock_move_line.py:562-570 | Deleting product moves after | FACT | always | — | A move line in state done or cancel cannot be unlinked (ondelete UserError). | N-U09-057 |
| VDR-U09-C121 | IAV-F06 | stock/models/stock_move.py:2189-2192 | m.location_dest_usage == 'inventory' | FACT | always | — | _action_cancel: done moves not ending in an inventory-usage location raise; done moves ending in inventory are filtered out of moves_to_cancel, so cancelling them does nothing. | N-U09-062 |
| VDR-U09-C122 | IAV-F06 | stock/views/stock_move_line_views.xml:71 | edit="0" | FACT | desktop form | — | The standard stock.move.line form has create=0 edit=0; only the mobile form (priority 1000) sets edit=1 (stock_move_line_views.xml:109-122). | N-U09-057 |
| VDR-U09-C123 | IAV-F06 | stock/models/stock_move_line.py:500-503 | undo the original move line | FACT | if a done line is written | — | write() on a done storable line first undoes its quant effect (_synchronize_quant) and re-applies the edited values after super().write (lines 533-536). | N-U09-057 |
| VDR-U09-C124 | IAV-F06 | stock/models/stock_quant.py:20-23 | _description = 'Quants' | INFERENCE | always | — | stock.quant defines no mail.thread inheritance, so quant changes have no chatter; counts are traceable only through the move lines (stock_quant.py:19-23). | N-U09-068 |
| VDR-U09-C125 | IAV-F06 | stock/security/ir.model.access.csv:33 | access_stock_move_line_all | OBSERVATION | always | — | ACL access_stock_move_line_all grants base.group_user read/write/create/unlink on stock.move.line (confirmed in restored DB: 1111); stock.move create requires stock user (csv:14). | N-U09-066 |
| VDR-U09-C126 | IAV-F06 | stock/models/stock_move_line.py:1205-1231 | def action_revert_inventory | UNKNOWN | later movements exist | RT | UNKNOWN: result of reverting an old adjustment after later movements/counts (negative stock, quant merge) needs a runtime test. | N-U09-069 |
| VDR-U09-C127 | IAV-F04 | stock/models/res_company.py:73-80 | 'name': 'Inventory adjustment' | FACT | company creation or missing | — | res.company._create_inventory_loss_location creates stock.location 'Inventory adjustment' (usage inventory) per company and sets ir.default product.template.property_stock_inventory for that company. | N-U09-072 |
| VDR-U09-C128 | IAV-F04 | stock/models/res_company.py:91-97 | 'name': 'Scrap' | FACT | company creation (via _create_per_company_locations) | — | _create_scrap_location creates a second location 'Scrap' (usage inventory) per new company; no ir.default is written for it. | N-U09-072 |
| VDR-U09-C129 | IAV-F04 | stock/models/res_company.py:150-154 | companies_having_scrap_loc | INFERENCE | upgrade or install function | — | create_missing_scrap_location creates 'Scrap' only for companies having no usage-inventory location at all, so a company already holding 'Inventory adjustment' is not given a separate Scrap location by the data function (stock_data.xml:96-99). | N-U09-073 |
| VDR-U09-C130 | IAV-F04 | stock/models/product.py:849-852 | property_stock_inventory = fields.Many2one | FACT | always | — | product.template.property_stock_inventory (company_dependent, domain usage inventory) is the per-product adjustment counterpart ('instead of the default one'). | N-U09-072 |
| VDR-U09-C131 | IAV-F04 | stock/models/stock_scrap.py:88-98 | 'usage', '=', 'inventory' | FACT | always | — | scrap_location_id is computed as the lowest id (id:min) stock.location with usage inventory per company; user may override (readonly=False). | N-U09-073 |
| VDR-U09-C132 | IAV-F03 | stock_account/models/stock_location.py:11-14 | valuation_account_id | FACT | stock_account installed | — | stock_account adds stock.location.valuation_account_id ('Stock Valuation Account') described as the expense account used to re-qualify products removed from stock and sent to this location. Discovered supporting module stock_account. | N-U09-074 |
| VDR-U09-C133 | IAV-F03 | stock_account/models/stock_move.py:659-666 | self.product_id.valuation == 'real_time' | FACT | stock_account installed | — | _should_create_account_move requires storable product, is_valued move, a valuation account on source or destination location, non-zero quantity and product valuation real_time. | N-U09-075 |
| VDR-U09-C134 | IAV-F03 | stock_account/models/stock_move.py:228-248 | credit_acc = self.location_id.valuation_account_id | FACT | stock_account installed | — | _get_account_move_line_vals: if source location has an account -> debit product stock_valuation, credit the location account; else debit the destination location account, credit stock_valuation; value = _get_aml_value (move value). | N-U09-076 |
| VDR-U09-C135 | IAV-F03 | stock_account/models/stock_move.py:210-215 | force_period_date | FACT | stock_account installed | — | _create_account_move creates and posts an account.move (journal = company.account_stock_journal_id) dated context force_period_date or today, then links it to the stock moves (account_move_id). | N-U09-077 |
| VDR-U09-C136 | IAV-F03 | stock_account/models/stock_quant.py:12-16 | accounting_date | FACT | stock_account installed | — | stock.quant.accounting_date: date at which accounting entries are created for automated valuation; if empty the inventory date is used. | N-U09-077 |
| VDR-U09-C137 | IAV-F03 | stock_account/models/stock_quant.py:80-87 | force_period_date=accounting_date | FACT | stock_account installed | — | _apply_inventory groups quants by accounting_date and applies with context force_period_date; after the apply it clears accounting_date. | N-U09-077 |
| VDR-U09-C138 | IAV-F03 | stock_account/models/stock_quant.py:89-101 | Accounted on %s | FACT | stock_account installed and no inventory_name | — | _get_inventory_move_values appends ' [Accounted on %s]' to the inventory_name when force_period_date is set. | N-U09-077 |
| VDR-U09-C139 | IAV-F03 | stock_account/models/stock_location.py:36-41 | self.usage in ['internal', 'transit'] | FACT | stock_account installed | — | _should_be_valued: location has a company and usage internal or transit; inventory/scrap locations are not valued, so counts/scrap count as in/out of the valuation perimeter (stock_move.py:545-583). | N-U09-078 |
| VDR-U09-C140 | IAV-F03 | stock/models/stock_quant.py:1253-1263 | def _get_inventory_move_values | FACT | always | — | _get_inventory_move_values (base) contains no account keys; accounts come only from location and category properties via stock_account. | N-U09-081 |
| VDR-U09-C141 | IAV-F04 | stock/models/stock_location.py:226-239 | Internal locations having stock | FACT | always | — | stock.location.write: usage cannot change to view while quants exist, nor change at all while quantity>0 quants exist ('Internal locations having stock can't be converted'). | N-U09-082 |
| VDR-U09-C142 | IAV-F04 | stock/models/stock_location.py:195-199 | as a scrap location | FACT | mrp_operation picking type points at it | — | Constraint: a location of usage inventory cannot be the default destination of a mrp_operation picking type. | N-U09-082 |
| VDR-U09-C143 | IAV-F03 | stock_account/models/stock_location.py:11-14 | valuation_account_id | OBSERVATION | restored DB | — | Restored DB: res_company.inventory_valuation = periodic; no stock_location row has valuation_account_id set (count 0); only one usage-inventory location exists (Inventory adjustment) and ir.default for property_stock_inventory points to it. | N-U09-080 |
| VDR-U09-C144 | IAV-F03 | stock_account/models/stock_move.py:659-666 | real_time | FACT | stock_account installed | CONTRA | CONTRA prior IAV-F03 (documentation: balance sheet updates as soon as counts are applied, unqualified): source makes any entry conditional on valuation real_time and a valuation account on the loss location; under periodic valuation (observed) none is created at apply time. | N-U09-083 |
| VDR-U09-C145 | IAV-F03 | stock_account/models/stock_move.py:545-553 | def _is_in | UNKNOWN | valuation unit | RT | UNKNOWN: value, price source and closing treatment for counts/scrap move to the valuation unit (U10); not examined here. | N-U09-084 |
| VDR-U09-C146 | FUNCTION MAPPING REQUIRED | stock/models/product.py:856-862 | ('serial', 'By Unique Serial Number') | FACT | always | — | product.template.tracking selection: serial / lot / none, required, default none, computed-stored but editable. | N-U09-085 |
| VDR-U09-C147 | FUNCTION MAPPING REQUIRED | stock/models/product.py:1094-1096 | def _compute_tracking | FACT | always | — | _compute_tracking forces tracking 'none' when the product is not storable. | N-U09-087 |
| VDR-U09-C148 | FUNCTION MAPPING REQUIRED | stock/models/product.py:564-570 | no lot/serial number | FACT | onchange | — | Onchange tracking returns a warning only if qty_available > 0 and tracking != none (stock has no lot/serial; assign by inventory adjustment); it does not block. | N-U09-088 |
| VDR-U09-C149 | FUNCTION MAPPING REQUIRED | stock/models/product.py:1129-1160 | clean_inventory = False | INFERENCE | always | — | product.template.write has guards only for company change and is_storable; there is no guard on tracking changes (read of lines 1129-1160). | N-U09-088 |
| VDR-U09-C150 | FUNCTION MAPPING REQUIRED | stock/models/res_config_settings.py:135-137 | Switch off tracking on all | FACT | disabling group_stock_production_lot | — | set_values refuses to switch off Lots & Serial Numbers while any product has tracking != none. | N-U09-088 |
| VDR-U09-C151 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:44-48 | ('tracking', '!=', 'none') | FACT | always | — | stock.lot.product_id: required, check_company, domain tracking != none and is_storable. | N-U09-102 |
| VDR-U09-C152 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:103-126 | must be unique within a company | FACT | always | — | @api.constrains name/product/company: duplicates raise ValidationError; counts duplicates per (company, product, name) and a company lot also clashes with a no-company lot of same product and name. | N-U09-089 |
| VDR-U09-C153 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:108-110 | across other companies | FACT | lot without company | — | If any lot in the set has no company the check runs sudo so duplicates across companies for company-less lots are detected. | N-U09-089 |
| VDR-U09-C154 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:42 | index='trigram' | OBSERVATION | restored DB | — | stock_lot name is trigram-indexed only; restored DB has no UNIQUE constraint or unique index on stock_lot besides the primary key; uniqueness is therefore application-level. | N-U09-102 |
| VDR-U09-C155 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:65-69 | next_by_id() | FACT | name empty | — | _compute_name fills name from product.lot_sequence_id.next_by_id() when empty. | N-U09-090 |
| VDR-U09-C156 | FUNCTION MAPPING REQUIRED | stock/data/stock_sequence_data.xml:26-34 | stock.lot.serial | FACT | always | — | Default sequence 'Serial Numbers' code stock.lot.serial, no prefix, padding 7, global company; product.lot_sequence_id defaults to it (product.py:863-865). | N-U09-090 |
| VDR-U09-C157 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:71-90 | def generate_lot_names | FACT | always | — | generate_lot_names derives a series from the last digit group of the first name, keeping zero padding; appends '0' if the name has no digit. | N-U09-090 |
| VDR-U09-C158 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:92-101 | def _get_next_serial | FACT | tracked product | — | _get_next_serial finds the newest lot (id DESC) of the product (company or no company) and proposes the next generated name. | N-U09-090 |
| VDR-U09-C159 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:128-133 | Create New Lots/Serial Numbers | FACT | context active_picking_id | — | _check_create: when created from a picking whose picking type has use_create_lots False it raises UserError. | N-U09-102 |
| VDR-U09-C160 | FUNCTION MAPPING REQUIRED | stock/models/stock_picking.py:53-60 | use_create_lots = fields.Boolean( | FACT | always | — | picking type use_create_lots and use_existing_lots default True (stored, editable); use_create_lots is forced True for incoming types by compute (stock_picking.py:289-295). | N-U09-091 |
| VDR-U09-C161 | FUNCTION MAPPING REQUIRED | stock/models/stock_warehouse.py:1008-1018 | use_existing_lots | OBSERVATION | restored DB | — | Restored DB picking types (create/existing): Receipts t/f, Delivery f/t, Pick/Pack/QC/Storage/Internal/Cross-dock f/t, Manufacturing and Repairs t/t, Dropship t/f. | N-U09-091 |
| VDR-U09-C162 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:591-593 | self.move_id.scrap_id | FACT | always | — | _exclude_requiring_lot is truthy for lines with a picking type, an inventory adjustment, a lot, or a scrap move. | N-U09-103 |
| VDR-U09-C163 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:626-642 | not ml._exclude_requiring_lot() | FACT | at done | — | At completion qty>0 tracked lines are checked: no operation type exemption -> tracked_without_lot; with picking type and both lots flags off the line may stay without lot; if use_create_lots the lot name is resolved else tracked_without_lot. | N-U09-092 |
| VDR-U09-C164 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:666-674 | You need to supply a | FACT | at done | — | Tracked lines without lot raise UserError listing the products. | N-U09-092 |
| VDR-U09-C165 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:649-660 | ('company_id', '=', False) | FACT | at done with use_create_lots | — | Existing lots are searched by name, product and company (or no company); found lots are assigned, unknown names go to creation. | N-U09-093 |
| VDR-U09-C166 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:756-773 | def _create_and_assign_production_lot | FACT | at done | — | _create_and_assign_production_lot creates one lot per (product, lot_name) for lot-tracked products and one per line for serial tracking, then writes lot_id on the lines. | N-U09-093 |
| VDR-U09-C167 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:746-754 | all_child_ids | FACT | always | — | _prepare_new_lot_vals sets name, product_id and the line company when it is the product company or its child. | N-U09-093 |
| VDR-U09-C168 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:1481-1527 | already used in location(s) | FACT | serial-tracked, onchange/warning | — | _check_serial_number returns a warning (not an error) when a serial exists with quantity !=0 in customer/internal/transit locations, or when it is in another source location (with a recommended location). | N-U09-094 |
| VDR-U09-C169 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:216-223 | sn_duplicated | FACT | always | — | quant.sn_duplicated flags quants of serial products in internal/transit locations with quantity>0 where the same lot appears in more than one quant. | N-U09-094 |
| VDR-U09-C170 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:192-199 | not allowed to change the product | FACT | lot with move lines | — | Changing product_id of a lot is refused if move lines with that lot exist for another product. | N-U09-095 |
| VDR-U09-C171 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:188-191 | cannot change the company | FACT | always | — | Changing company_id is refused if the lot current single location belongs to a different company. | N-U09-095 |
| VDR-U09-C172 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:202-208 | (copy of) | FACT | always | — | copy_data names the copy '(copy of) <name>' when no name is provided. | N-U09-095 |
| VDR-U09-C173 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:210-235 | quant_qty_by_lot | FACT | always | — | stock.lot.product_qty: sum of quant quantity per lot over domain_quant_loc; for a to_date in the past it subtracts later done incoming and adds outgoing move-line quantities. | N-U09-096 |
| VDR-U09-C174 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:167-179 | move a lot/serial to a new | FACT | writing location_id | — | location_id is the single positive-quantity quant location (else False); the inverse relocates via move_quants and raises if more than one location. | N-U09-096 |
| VDR-U09-C175 | FUNCTION MAPPING REQUIRED | stock/report/stock_traceability.py:26-51 | # if MTS | FACT | always | — | _get_move_lines walks upstream: via move_orig_ids (chained) else via done lines of the same product and lot into the source location with earlier date. | N-U09-097 |
| VDR-U09-C176 | FUNCTION MAPPING REQUIRED | stock/report/stock_traceability.py:92-99 | Inventory Adjustment | FACT | always | — | Traceability reference labels adjustment moves 'Inventory Adjustment' and scrap moves with the scrap name. | N-U09-097 |
| VDR-U09-C177 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:369-431 | def _find_delivery_ids_by_lot_iterative | FACT | always | — | Deliveries of a lot are found from done outgoing lines and, through produce_line_ids (mrp), from lots consumed in manufacturing, propagated up the lot graph. | N-U09-097 |
| VDR-U09-C178 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:12 | access_stock_lot_user | OBSERVATION | restored DB | — | stock.lot has one ACL row: stock.group_stock_user read/write/create/unlink (1111); the portal ACL for subcontractors comes from mrp_subcontracting; there is no base.group_user ACL on lots. | N-U09-102 |
| VDR-U09-C179 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:34-36 | Manage Lots / Serial Numbers | OBSERVATION | restored DB | — | Group stock.group_production_lot exists and, in the restored DB, is implied by base.group_user and base.group_portal (feature enabled); expiry extension installed. | N-U09-100 |
| VDR-U09-C180 | FUNCTION MAPPING REQUIRED | product_expiry/models/production_lot.py:58-79 | def _compute_dates | FACT | product_expiry installed | — | Lot use_date, removal_date, alert_date are computed from expiration_date minus product use_time/removal_time/alert_time on create/product change; later edits shift them by the same delta. | N-U09-098 |
| VDR-U09-C181 | FUNCTION MAPPING REQUIRED | product_expiry/models/production_lot.py:50-56 | expiration_time | FACT | product_expiry installed | — | Lot expiration_date defaults to now + product expiration_time days when product.use_expiration_date. | N-U09-098 |
| VDR-U09-C182 | FUNCTION MAPPING REQUIRED | product_expiry/models/production_lot.py:81-107 | Log an activity on internally | FACT | product_expiry installed | — | _alert_date_exceeded schedules a to-do activity (responsible user else superuser) for lots with alert_date<=today, not yet reminded, with quantity>0 in an internal location, then sets product_expiry_reminded. | N-U09-098 |
| VDR-U09-C183 | FUNCTION MAPPING REQUIRED | product_expiry/models/stock_rule.py:8-11 | _alert_date_exceeded | FACT | scheduler cron active | — | stock.rule._run_scheduler_tasks (daily cron) calls stock.lot._alert_date_exceeded after base tasks. | N-U09-098 |
| VDR-U09-C184 | FUNCTION MAPPING REQUIRED | product_expiry/models/stock_picking.py:11-19 | _pre_action_done_hook | FACT | product_expiry installed | — | Validation checks for expired lots (lot alert or line removal_date <= now) and, unless skip_expired, opens the expiry confirmation wizard. | N-U09-098 |
| VDR-U09-C185 | FUNCTION MAPPING REQUIRED | product_expiry/wizard/confirm_expiry.py:46-51 | Remove the expired mls | FACT | user chooses option | — | Wizard option 'process_no_expired' unlinks expired lines and re-validates. | N-U09-098 |
| VDR-U09-C186 | FUNCTION MAPPING REQUIRED | product_expiry/models/product_product.py:56-59 | use_expiration_date'] = False | FACT | tracking set to none | — | Writing tracking='none' on the product template also sets use_expiration_date False. | N-U09-098 |
| VDR-U09-C187 | FUNCTION MAPPING REQUIRED | product_expiry/models/stock_move_line.py:34-61 | expiration_time | FACT | product_expiry installed | — | Move lines compute expiration_date and removal_date from the lot or, when the picking type creates lots, from scheduled date plus product durations and pass expiration_date into new lots. | N-U09-098 |
| VDR-U09-C188 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:728-735 | untracked_qty | UNKNOWN | tracked lot on untracked stock | RT | UNKNOWN: _synchronize_quant moves quantity from untracked quants to the lot when stock goes negative on a lot; real effect on mixed tracked/untracked stock needs runtime confirmation. | N-U09-104 |
| VDR-U09-C189 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:17-18 | _name = 'stock.package' | FACT | always | — | Packages are stock.package (nested via parent_package_id, _parent_store) in this revision; the older model name stock.quant.package does not exist (grep of addons shows no _inherit of it). | N-U09-105 |
| VDR-U09-C190 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:70-73 | The package containing this quant | FACT | always | — | quant.package_id domain: package location equals quant location, or the package has no location and no quants. | N-U09-120 |
| VDR-U09-C191 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:277-287 | _get_next_name_by_sequence | FACT | name not given | — | create() takes the name from complete_name if provided, else package type _get_next_name_by_sequence(). | N-U09-107 |
| VDR-U09-C192 | FUNCTION MAPPING REQUIRED | stock/models/stock_package_type.py:128-131 | next_by_code('stock.package') | FACT | always | — | Type sequence if set, else ir.sequence code stock.package (prefix PACK, padding 7, company-less: stock_sequence_data.xml:36-43). | N-U09-107 |
| VDR-U09-C193 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:289-296 | Recomputes the name according the sequence | FACT | name emptied | — | write() with an empty name regenerates it from the type sequence. | N-U09-107 |
| VDR-U09-C194 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:25 | name = fields.Char( | INFERENCE | always | — | stock.package.name is required and trigram-indexed but the model declares no unique constraint (no Constraint/_sql in the file). | N-U09-121 |
| VDR-U09-C195 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:156-169 | def _compute_package_info | FACT | always | — | location_id from first quant with qty>0 else first child package; company only if all content share one company. | N-U09-108 |
| VDR-U09-C196 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:184-191 | def _compute_owner_id | FACT | always | — | owner_id is the common owner of all quants, else empty. | N-U09-108 |
| VDR-U09-C197 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:297-307 | Package manually relocated | FACT | writing location_id | — | write(location_id): non-empty package required (empty -> UserError), clearing location of non-empty package -> UserError; otherwise move_quants for positive contained quants with message 'Package manually relocated'. | N-U09-109 |
| VDR-U09-C198 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:308-312 | one of its contained packages | FACT | writing package_dest_id | — | write(package_dest_id) raises ValidationError if the dest is among the package's destination descendants. | N-U09-111 |
| VDR-U09-C199 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:347-367 | previous_dest_packages | FACT | always | — | stock.package.action_put_in_pack creates or reuses a package, sets package_dest_id on the packages in self, clears destinations of packages left without move lines and re-applies putaway; the move-line path (stock_move_line.py:1095-1117) instead writes result_package_id. | N-U09-110 |
| VDR-U09-C200 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:332-341 | _should_display_put_in_pack_wizard | FACT | always | — | _pre_put_in_pack_hook returns the put-in-pack wizard when the type requires a package type and none was given. | N-U09-110 |
| VDR-U09-C201 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:1242-1244 | set_package_type | FACT | always | — | _should_set_package is true for a single picking type with set_package_type. | N-U09-110 |
| VDR-U09-C202 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:369-405 | is_entire_pack | FACT | always | — | action_remove_package unlinks move lines of entire packs, clears result_package_id on partial ones, and clears related destination packages. | N-U09-113 |
| VDR-U09-C203 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:316-325 | Quantities unpacked | FACT | always | — | unpack detaches child packages, moves quants out via move_quants(unpack=True) and then runs _quant_tasks. | N-U09-113 |
| VDR-U09-C204 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:494-501 | moved to different locations while | FACT | at done | — | _apply_dest_to_package raises if packages in one container end in different locations, or the container already holds quants in another location. | N-U09-112 |
| VDR-U09-C205 | FUNCTION MAPPING REQUIRED | stock/models/stock_move.py:2277-2286 | cannot move the same package | FACT | at done | — | After completion, a result package with quants in more than one location raises UserError. | N-U09-112 |
| VDR-U09-C206 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:435-470 | def _get_weight | FACT | always | — | Weight = type base_weight + contained package base weights + sum(quant.quantity * product.weight); with picking context uses move lines. | N-U09-116 |
| VDR-U09-C207 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:551-555 | reusable | FACT | always | — | _apply_package_dest_for_entire_packs sets container as destination only when all children are added and the container type is not reusable. | N-U09-115 |
| VDR-U09-C208 | FUNCTION MAPPING REQUIRED | stock/models/stock_package_type.py:31-36 | Reusable Box (totes) | FACT | always | — | package_use selection disposable (default) or reusable; reusable boxes are emptied after batch picking. | N-U09-115 |
| VDR-U09-C209 | FUNCTION MAPPING REQUIRED | stock/models/stock_package_type.py:41-60 | can only be assigned to | FACT | always | — | stock.package.type constraints: unique(barcode); CHECK height, width, packaging_length, max_weight >= 0. | N-U09-114 |
| VDR-U09-C210 | FUNCTION MAPPING REQUIRED | stock/models/stock_package_type.py:93-103 | Package Type Sequence | FACT | sequence_code given | — | create/write build an ir.sequence (padding 7) from sequence_code on demand. | N-U09-114 |
| VDR-U09-C211 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:690-694 | stock.package.history | FACT | not ignore_dest_packages | — | Before moving quants, _action_done creates stock.package.history rows from _prepare_package_history_vals (skipped when context ignore_dest_packages, as in counts). | N-U09-116 |
| VDR-U09-C212 | FUNCTION MAPPING REQUIRED | stock/models/stock_package_history.py:6-23 | Stock Package History | FACT | always | — | stock.package.history stores package name, origin/destination location, origin/destination container, outermost container and transfers. | N-U09-116 |
| VDR-U09-C213 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:46-48 | Manage Packages | OBSERVATION | restored DB | — | Group stock.group_tracking_lot (Manage Packages) is implied by base.group_user in the restored DB; no stock_package or stock_package_type rows exist. | N-U09-118 |
| VDR-U09-C214 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:23-25 | access_stock_package_all | OBSERVATION | restored DB | — | stock.package ACL: base.group_user read-only; stock user and stock manager read/write/create/unlink; stock.package.type: stock user read-only, manager full (csv:60-61, DB-confirmed). | N-U09-120 |
| VDR-U09-C215 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:476-509 | def _apply_dest_to_package | UNKNOWN | nested transfers | RT | UNKNOWN: recursion of _apply_dest_to_package over deep nests and its interaction with putaway needs runtime tests. | N-U09-122 |
| VDR-U09-C216 | FUNCTION MAPPING REQUIRED | stock_delivery/models/stock_package.py:7 | _inherit = "stock.package" | FACT | stock_delivery installed | — | DISCOVERED SUPPORTING MODULE stock_delivery extends stock.package and stock.package.type (shipping data); not analysed here. | N-U09-119 |
| VDR-U09-C217 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:10-14 | _name = 'stock.scrap' | FACT | always | — | stock.scrap inherits mail.thread (chatter), order id desc. | N-U09-123 |
| VDR-U09-C218 | IAV-F04 | stock/models/stock_scrap.py:50-53 | ('draft', 'Draft') | FACT | always | — | state selection draft/done, default draft, readonly, tracked; no cancel state. | N-U09-125 |
| VDR-U09-C219 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:120-123 | cannot delete a scrap which | FACT | always | — | Unlink of a done scrap raises UserError (ACL: only manager has unlink). | N-U09-125 |
| VDR-U09-C220 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:155 | next_by_code('stock.scrap') | FACT | at validation | — | do_scrap assigns name from sequence code stock.scrap (default prefix SP/, padding 5, per company: res_company.py:99-113), else 'New'. | N-U09-126 |
| VDR-U09-C221 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:21-23 | domain="[('type', '=', 'consu')]" | FACT | always | — | product_id domain type consu, required, check_company; check_available_qty applies only when is_storable. | N-U09-128 |
| VDR-U09-C222 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:71-86 | scrap.picking_id.state == 'done' | FACT | always | — | location_id: from picking (dest if done else source) else the first warehouse lot_stock_id of the company. | N-U09-127 |
| VDR-U09-C223 | IAV-F04 | stock/models/stock_scrap.py:88-98 | id:min | FACT | always | — | scrap_location_id: lowest-id usage-inventory location of the company; domain usage inventory; readonly=False. | N-U09-127 |
| VDR-U09-C224 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:211-214 | You can only enter positive quantities | FACT | always | — | action_validate raises 'You can only enter positive quantities.' if scrap_qty is zero (is_zero test). | N-U09-128 |
| VDR-U09-C225 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:196-209 | strict=True | FACT | storable product | — | check_available_qty reads qty_available with context location, lot_id, package_id, owner_id and strict=True and compares to scrap_qty in product UoM. | N-U09-129 |
| VDR-U09-C226 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:217-234 | Insufficient Quantity To Scrap | FACT | not enough stock | — | If insufficient, action_validate returns the stock.warn.insufficient.qty.scrap wizard instead of scrapping. | N-U09-129 |
| VDR-U09-C227 | FUNCTION MAPPING REQUIRED | stock/wizard/stock_warn_insufficient_qty.py:45-46 | scrap_id.do_scrap() | FACT | user confirms | — | Confirm calls do_scrap with cleaned context; Discard unlinks the draft unless not_unlink_on_discard is in context (line 48-53, FIXME in master). | N-U09-129 |
| VDR-U09-C228 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:698-706 | _free_reservation | INFERENCE | confirmed despite insufficient stock | RT | Scrap move completion uses the common _action_done path which does not raise on negative on-hand (lines 698-706), so a confirmed over-scrap leaves a negative quant. | N-U09-139 |
| VDR-U09-C229 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:125-150 | 'scrap_id': self.id | FACT | always | — | _prepare_move_values: move state draft, picked True, source->scrap location, one move line with package, owner, lot, quantity; origin = origin or picking name or scrap name. | N-U09-130 |
| VDR-U09-C230 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:152-163 | is_scrap=True | FACT | always | — | do_scrap: _check_company, name, create move, _action_done under is_scrap=True, state done, date_done now, optional replenishment. | N-U09-130 |
| VDR-U09-C231 | FUNCTION MAPPING REQUIRED | stock/models/stock_move.py:2305-2308 | back order for scrap moves | FACT | is_scrap | — | stock.move._action_done returns early (no backorder) when context is_scrap. | N-U09-130 |
| VDR-U09-C232 | FUNCTION MAPPING REQUIRED | stock/models/stock_move.py:357-362 | move.scrap_id | FACT | always | — | stock.move.reference = scrap name for scrap moves. | N-U09-130 |
| VDR-U09-C233 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:169-181 | Procurement( | FACT | should_replenish | — | do_replenish runs stock.rule.run with a Procurement for product, scrap_qty, uom, location_id, scrap name as name and origin, company. | N-U09-131 |
| VDR-U09-C234 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:246-249 | Tag name already exists | FACT | always | — | stock.scrap.reason.tag has unique name; fields sequence and color; scrap links many2many scrap_reason_tag_ids. | N-U09-132 |
| VDR-U09-C235 | FUNCTION MAPPING REQUIRED | stock/views/stock_scrap_views.xml:60 | required="tracking != 'none'" | FACT | group_production_lot enabled | — | The lot field in the scrap form is required for tracked products and visible only for stock.group_production_lot; the model field is not required. | N-U09-136 |
| VDR-U09-C236 | FUNCTION MAPPING REQUIRED | stock/models/stock_picking.py:1907-1920 | Scrap Products | FACT | always | — | stock.picking.button_scrap opens the scrap form with default_picking_id and product_ids limited to non-draft, non-cancel consumable moves. | N-U09-133 |
| VDR-U09-C237 | FUNCTION MAPPING REQUIRED | stock/views/stock_picking_views.xml:502-510 | records.button_scrap() | FACT | always | — | Server action Scrap is bound to stock.picking form views with no group restriction. | N-U09-133 |
| VDR-U09-C238 | FUNCTION MAPPING REQUIRED | stock/wizard/stock_picking_return.py:121-122 | location_dest_usage == 'inventory' | FACT | return wizard | — | The return wizard skips picking moves whose destination usage is inventory, so scrapped quantities are not returnable. | N-U09-133 |
| VDR-U09-C239 | FUNCTION MAPPING REQUIRED | stock/models/stock_picking.py:839-851 | all_done_are_scrapped | FACT | always | — | Picking state: if all done moves are scrapped and some cancelled moves are not scrapped, picking becomes cancel instead of done. | N-U09-133 |
| VDR-U09-C240 | FUNCTION MAPPING REQUIRED | mrp/models/stock_scrap.py:25-41 | production_id.location_src_id | FACT | mrp installed | — | mrp extends stock.scrap with production_id, workorder_id, bom_id (kit); location from MO source/destination; kit explode in _create_scrap_move (lines 93-97); do_scrap unpicks matching component lots (lines 108-112); replenishment adds production_group_id. Discovered supporting module mrp. | N-U09-134 |
| VDR-U09-C241 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:41-44 | access_stock_scrap_user | OBSERVATION | restored DB | — | stock.scrap ACL: stock user 1110, manager 1111; reason tag same; confirmed in restored DB; record rule 'stock_scrap_company multi-company' domain company_id in company_ids (no False). | N-U09-138 |
| VDR-U09-C242 | FUNCTION MAPPING REQUIRED | stock/models/res_company.py:102-108 | 'code': 'stock.scrap' | OBSERVATION | restored DB | — | Restored DB: stock_scrap has 0 rows, stock_scrap_reason_tag 0 rows, sequence stock.scrap prefix SP/ padding 5 exists. | N-U09-136 |
| VDR-U09-C243 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:193-195 | def _should_check_available_qty | UNKNOWN | kits, multi-step | RT | UNKNOWN: availability check for kit products (mrp override at mrp/models/stock_scrap.py:90-91) and multi-step routes needs runtime tests. | N-U09-140 |
| VDR-U09-C244 | RCN-F01 | stock/models/product.py:52-64 | qty_available = fields.Float( | FACT | always | — | product.product qty_available, virtual_available, free_qty, incoming_qty, outgoing_qty are computed (not stored), compute_sudo False, with inverse only on qty_available. | N-U09-141 |
| VDR-U09-C245 | RCN-F01 | stock/models/product.py:147-151 | 'location', 'warehouse_id', 'allowed_company_ids' | FACT | always | — | _compute_quantities depends on context lot_id, owner_id, package_id, from_date, to_date, location, warehouse_id, allowed_company_ids, is_storable. | N-U09-143 |
| VDR-U09-C246 | RCN-F01 | stock/models/product.py:153-156 | p.type != 'service' | FACT | always | — | Services are excluded and set to 0 for all quantity fields. | N-U09-146 |
| VDR-U09-C247 | RCN-F01 | stock/models/product.py:389-394 | self.env.companies.ids | FACT | no location/warehouse context | — | _get_domain_locations: with no warehouse or location in context, scope = view_location_id of all warehouses of env.companies. | N-U09-143 |
| VDR-U09-C248 | RCN-F01 | stock/models/product.py:376-387 | view_location_id | FACT | warehouse context | — | With warehouse_id context, scope = warehouse view location(s), intersected with an optional location context via parent_path. | N-U09-143 |
| VDR-U09-C249 | RCN-F01 | stock/models/product.py:406-409 | Domain('location_id', 'in', locations.ids) | FACT | context strict | — | With context strict the scope is the exact locations; otherwise descendants via a recursive CTE. | N-U09-145 |
| VDR-U09-C250 | RCN-F01 | stock/models/product.py:438-453 | dest_loc_domain_in_progress | FACT | always | — | For not-done moves the destination used is location_final_id if set, else location_dest_id; done moves use location_dest_id. | N-U09-144 |
| VDR-U09-C251 | RCN-F01 | stock/models/product.py:213-216 | ('waiting', 'confirmed', 'assigned', 'partially_available') | FACT | always | — | Incoming/outgoing move sums use product_qty of moves in states waiting, confirmed, assigned, partially_available. | N-U09-144 |
| VDR-U09-C252 | RCN-F01 | stock/models/product.py:255-266 | res[product_id]['virtual_available'] | FACT | always | — | qty_available = quants sum (or backed out for past dates); free_qty = qty - reserved - expired_unreserved; virtual = qty + incoming - outgoing - expired_unreserved; all rounded to product uom. | N-U09-144 |
| VDR-U09-C253 | RCN-F01 | stock/models/product.py:169-176 | time.max | FACT | to_date given | — | to_date given as date or 10-char string is extended to end of day (time.max); dates in the past trigger back-out via later done moves. | N-U09-145 |
| VDR-U09-C254 | RCN-F01 | stock/models/product.py:225-235 | dates_in_the_past | FACT | to_date in the past | — | Past on-hand = quants sum - done incoming moves after to_date + done outgoing moves after to_date (uom converted). | N-U09-145 |
| VDR-U09-C255 | RCN-F01 | stock/models/product.py:218-222 | with_expiration | FACT | context with_expiration (product_expiry) | — | expired_unreserved quantity is computed from quants with removal_date <= with_expiration and subtracted from free and forecast. | N-U09-144 |
| VDR-U09-C256 | RCN-F01 | product_expiry/models/product_product.py:11-12 | with_expiration=datetime.date.today() | FACT | product_expiry installed | — | product_expiry sets with_expiration=today on every _compute_quantities_dict call. | N-U09-153 |
| VDR-U09-C257 | RCN-F01 | stock/models/product.py:986-1007 | variants_available | FACT | always | — | Template quantities are the sum of the variant quantities. | N-U09-146 |
| VDR-U09-C258 | RCN-F01 | stock/models/product.py:468-479 | _search_qty_available_new | FACT | always | — | qty_available search without from/to date uses quants only (_search_field_by_quants); with dates it loads and filters all products. | N-U09-146 |
| VDR-U09-C259 | RCN-F01 | stock/models/product.py:1130-1147 | as long as there are quantities | FACT | always | — | product.template.write refuses a company change if moves or non-zero quants exist in another company. | N-U09-147 |
| VDR-U09-C260 | RCN-F01 | stock/models/product.py:1149-1160 | templates_to_reset | FACT | is_storable switched on | — | Becoming storable calls _clean_reservations and _reset_inventory; _reset_inventory creates quants matching done move-line history and applies inventory to reset them (lines 1162-1202). | N-U09-147 |
| VDR-U09-C261 | RCN-F01 | stock/views/stock_move_line_views.xml:227-232 | Moves History | FACT | always | — | Moves History action on stock.move.line: default filter done, create 0, pivot measures quantity and count. | N-U09-148 |
| VDR-U09-C262 | RCN-F01 | stock/views/stock_move_line_views.xml:7 | create="0" | FACT | always | — | Move line list view has create=0, duplicate=0, default order id desc; clicking opens the reference document. | N-U09-148 |
| VDR-U09-C263 | RCN-F01 | stock/views/stock_move_line_views.xml:153 | Inventory Adjustments | FACT | always | — | Search filters: To Do, Done, Incoming/Outgoing/Internal, date ranges, Inventory Adjustments (is_inventory), group by product/status/date/transfer/location/category. | N-U09-148 |
| VDR-U09-C264 | RCN-F01 | stock/views/stock_move_line_views.xml:242-245 | stock_move_line_menu | FACT | always | — | Moves History menu is under menu_warehouse_report (Reporting). | N-U09-148 |
| VDR-U09-C265 | RCN-F01 | stock/views/stock_menu_views.xml:36 | group_stock_manager | FACT | always | — | Reporting menu is limited to group_stock_manager. | N-U09-148 |
| VDR-U09-C266 | RCN-F01 | stock/models/stock_quant.py:468-495 | search_default_inventory | FACT | always | — | quant.action_inventory_history opens move lines filtered inventory+done for product, location (source or dest), lot, package, owner. | N-U09-148 |
| VDR-U09-C267 | RCN-F01 | stock/models/stock_quant.py:371-388 | def action_view_stock_moves | FACT | always | — | quant.action_view_stock_moves lists move lines for the location (source or dest), lot and package. | N-U09-148 |
| VDR-U09-C268 | RCN-F01 | stock/wizard/stock_quantity_history.py:27-36 | to_date=self.inventory_datetime | FACT | always | — | The stock-at-date wizard reopens the storable product list with to_date context. | N-U09-149 |
| VDR-U09-C269 | RCN-F01 | stock/report/report_stock_quantity.py:74 | pt.is_storable = true | FACT | always | — | report.stock.quantity is a SQL view over done/open moves of storable products excluding draft/cancel and inter-same-warehouse moves. | N-U09-150 |
| VDR-U09-C270 | RCN-F01 | stock/report/report_stock_quantity.py:157-159 | l.usage = 'internal' AND wh.id | FACT | always | — | Forecast baseline rows come from quants in internal locations of a warehouse or in transit locations, repeated per day in the window. | N-U09-150 |
| VDR-U09-C271 | RCN-F01 | stock/report/report_stock_quantity.py:193 | stock.report_stock_quantity_period | FACT | always | — | Window length is ir.config_parameter stock.report_stock_quantity_period months (default 3) read at view creation (init). | N-U09-153 |
| VDR-U09-C272 | RCN-F01 | stock/security/ir.model.access.csv:48 | access_report_stock_quantity | OBSERVATION | restored DB | — | report.stock.quantity: base.group_user read-only; company rule company_id in company_ids (DB-confirmed). | N-U09-155 |
| VDR-U09-C273 | RCN-F01 | stock/report/stock_forecasted.py:156-172 | def _get_report_data | FACT | always | — | Replenishment report uses the first active warehouse unless warehouse_id in context and reads product quantities plus draft in/out sums. | N-U09-151 |
| VDR-U09-C274 | RCN-F01 | stock/report/stock_forecasted.py:153-154 | def _get_warehouse | FACT | always | — | _get_warehouse = context warehouse_id or the first active warehouse search result. | N-U09-151 |
| VDR-U09-C275 | RCN-F01 | stock/models/product.py:164-168 | def _compute_quantities_dict | UNKNOWN | large data | RT | UNKNOWN: performance and multi-warehouse figures of past-date computations need runtime measurement. | N-U09-157 |
| VDR-U09-C276 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:10-22 | id="group_stock_manager" | FACT | always | — | Groups: stock.group_stock_user (User) implies base.group_user; stock.group_stock_manager (Administrator) implies group_stock_user. | N-U09-160 |
| VDR-U09-C277 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:21 | base.user_root | FACT | always | — | group_stock_manager user_ids are base.user_root and base.user_admin; restored DB: Administrator group has 2 members, stock User group has 0 explicit members (count only). | N-U09-160 |
| VDR-U09-C278 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:21-22 | access_stock_quant_user | OBSERVATION | restored DB | — | stock.quant ACL: stock user read/write/create (1110), base.group_user read-only (1000); no delete right in ACL; DB confirms both rows. | N-U09-161 |
| VDR-U09-C279 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:66-70 | access_stock_request_count | OBSERVATION | restored DB | — | stock.inventory.conflict, stock.inventory.warning, stock.request.count, stock.quant.relocate: stock manager only (1110); stock.inventory.adjustment.name: user and manager (csv:68-69); DB confirms. | N-U09-162 |
| VDR-U09-C280 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:41-44 | access_stock_scrap_manager | OBSERVATION | restored DB | — | stock.scrap and stock.scrap.reason.tag: user 1110, manager 1111; stock.warn.insufficient.qty.scrap and stock.traceability.report: user 1110. | N-U09-162 |
| VDR-U09-C281 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:24-25 | access_stock_package_stock_manager | OBSERVATION | restored DB | — | stock.package: user and manager 1111; stock.package.type: manager 1111, user 1000; stock.package.history: user 1110. | N-U09-162 |
| VDR-U09-C282 | FUNCTION MAPPING REQUIRED | stock/views/stock_quant_views.xml:325-359 | Relocate | FACT | always | — | Server actions: Set to quantity on hand (user), Set to 0 (manager), Relocate (manager), Clear and Request a Count header buttons (manager). | N-U09-163 |
| VDR-U09-C283 | FUNCTION MAPPING REQUIRED | stock_account/models/stock_quant.py:10-11 | groups='stock.group_stock_manager' | FACT | stock_account installed | — | quant value and currency_id fields are readable only by stock managers (stock_account). | N-U09-169 |
| VDR-U09-C284 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:120-124 | stock_quant multi-company | OBSERVATION | restored DB | — | Rule stock_quant: company_id in company_ids + [False]; global (no groups) in the DB, perms 1111. | N-U09-164 |
| VDR-U09-C285 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:90-94 | Stock Production Lot multi-company | OBSERVATION | restored DB | — | Rule stock.lot: company_id in company_ids + [False]; DB shows a second rule 'Stock Lot Subcontractor' from mrp_subcontracting limited to portal group. | N-U09-164 |
| VDR-U09-C286 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:144-148 | stock_package multi-company | OBSERVATION | restored DB | — | Rule stock.package: company_id in company_ids + [False]. | N-U09-164 |
| VDR-U09-C287 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:150-154 | stock_scrap_company multi-company | OBSERVATION | restored DB | — | Rule stock.scrap: company_id in company_ids (no False). | N-U09-164 |
| VDR-U09-C288 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:114-118 | stock_move_line multi-company | OBSERVATION | restored DB | — | Rule stock.move.line: company_id in company_ids + [False]; stock.move rule has no False (lines 108-112). | N-U09-164 |
| VDR-U09-C289 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:102-106 | Location multi-company | OBSERVATION | restored DB | — | Rule stock.location: company_id in company_ids + [False] (shared locations visible to all). | N-U09-164 |
| VDR-U09-C290 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:156-160 | report_stock_quantity_flow multi-company | OBSERVATION | restored DB | — | Rule report.stock.quantity: company_id in company_ids. | N-U09-164 |
| VDR-U09-C291 | FUNCTION MAPPING REQUIRED | mrp_subcontracting/security/mrp_subcontracting_security.xml:108 | Stock Lot Subcontractor | FACT | mrp_subcontracting installed | — | mrp_subcontracting adds a portal record rule for stock.lot (and move lines); discovered supporting module, not analysed further. | N-U09-169 |
| VDR-U09-C292 | FUNCTION MAPPING REQUIRED | stock/data/stock_sequence_data.xml:46-57 | Procurement: run scheduler | OBSERVATION | restored DB | — | Cron 'Procurement: run scheduler' calls stock.rule.run_scheduler(True) as base.user_root every 1 day, active in the restored DB; no other stock cron exists (only stock_account closing and unrelated HR/mail crons). | N-U09-165 |
| VDR-U09-C293 | FUNCTION MAPPING REQUIRED | stock/models/stock_rule.py:739-742 | Error during stock scheduler | FACT | always | — | run_scheduler logs the exception and re-raises, so the cron fails visibly. | N-U09-165 |
| VDR-U09-C294 | FUNCTION MAPPING REQUIRED | stock/models/stock_location.py:240-256 | still contain products | FACT | archiving a location | — | Archiving a location is refused while it (or its internal descendants) holds non-zero quants, or is a warehouse stock/view location. | N-U09-166 |
| VDR-U09-C295 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:878-882 | unreserve more products | FACT | always | — | _get_reserve_quantity raises UserError when asked to unreserve more than is reserved. | N-U09-166 |
| VDR-U09-C296 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:644-645 | No negative quantities allowed | FACT | at done | — | Completing a line with negative quantity raises UserError. | N-U09-166 |
| VDR-U09-C297 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:620-624 | respect the rounding precision | FACT | at done | — | Quantity must respect the UoM rounding, else UserError. | N-U09-166 |
| VDR-U09-C298 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:66-67 | access_stock_inventory_warning | UNKNOWN | non-manager stock user | RT | UNKNOWN: ir.model.access.check (base) has no transient exemption (addons/base/models/ir_model.py:2162-2174 as read), so non-manager inventory users likely cannot open the conflict/warning dialogs; needs a runtime test. | N-U09-172 |
| VDR-U09-C299 | FUNCTION MAPPING REQUIRED | stock/models/product.py:217 | quants_res = {product.id | INFERENCE | always | — | Product quantity fields are aggregated from stock.quant groups (line 217), as are lot quantities and value; the quant is the single source for these reads. | N-U09-002 |
| VDR-U09-C300 | FUNCTION MAPPING REQUIRED | stock/models/stock_move_line.py:698 | action="reserved" | FACT | always | — | stock.move.line._action_done (transfer engine) is the caller that unreserves and moves quants; quant-side methods are only the maintenance API (U08 owns the engine). | N-U09-014 |
| VDR-U09-C301 | FUNCTION MAPPING REQUIRED | stock/models/stock_quant.py:848-849 | avoid quants with negative qty | FACT | always | — | _get_reserve_quantity computes available quantity ignoring negative quants so negatives do not lower availability but are netted against positives before reserving (lines 886-899). | N-U09-018 |
| VDR-U09-C302 | IAV-F02 | stock/models/stock_quant.py:996-1000 | def _apply_inventory | FACT | always | — | _apply_inventory is the single place that turns counted quantities into stock moves (all apply paths funnel into it). | N-U09-020 |
| VDR-U09-C303 | IAV-F02 | stock/models/stock_quant.py:1026-1027 | moves = self.env['stock.move'] | INFERENCE | always | — | Applying a count creates stock.move records and completes them rather than writing quantity directly (lines 1026-1027). | N-U09-021 |
| VDR-U09-C304 | IAV-F02 | stock/views/stock_quant_views.xml:319 | action_apply_inventory | INFERENCE | always | — | Row Apply calls action_apply_inventory without the reason wizard, so inventory_name is not set unless context supplies it (stock_quant.py:1289-1290). | N-U09-038 |
| VDR-U09-C305 | IAV-F05 | stock/models/stock_location.py:81 | automatically set at the defined frequency | FACT | always | — | Help text of cyclic_inventory_frequency states the count date is set automatically at the defined frequency for products stored at the location. | N-U09-042 |
| VDR-U09-C306 | IAV-F05 | stock/models/stock_quant.py:1032-1034 | date_by_location | FACT | after apply | — | After applying a count the quant inventory_date moves to the next date from _get_next_inventory_date (cycle: scheduled, due, counted, rescheduled). | N-U09-049 |
| VDR-U09-C307 | IAV-F05 | stock/models/stock_rule.py:693-726 | # Merge duplicated quants | INFERENCE | always | — | Scheduler tasks do not touch inventory_date or notify counters; a missed date has no system consequence beyond the filter/highlight. | N-U09-053 |
| VDR-U09-C308 | IAV-F06 | stock/models/stock_move_line.py:1225-1231 | Reverted Moves | FACT | always | — | action_revert_inventory returns a list of the reversal and original move lines under the name Reverted Moves. | N-U09-055 |
| VDR-U09-C309 | IAV-F06 | stock/models/stock_move_line.py:1181 | [reverted] | INFERENCE | always | — | The reversal references the original via the reference text only, leaving the original movement intact as history. | N-U09-056 |
| VDR-U09-C310 | IAV-F06 | stock/models/stock_move_line.py:1223-1224 | moves = self.env['stock.move'].create(move_vals) | INFERENCE | always | — | Revert creates new moves and writes nothing on the original lines, so no reversed state exists. | N-U09-063 |
| VDR-U09-C311 | IAV-F06 | stock_account/models/stock_move.py:185-186 | moves._create_account_move() | FACT | stock_account installed | — | stock_account._action_done override calls _create_account_move for all completed moves including reversal moves. | N-U09-065 |
| VDR-U09-C312 | IAV-F06 | stock/models/stock_move_line.py:1205-1213 | move_line.is_inventory and not | INFERENCE | always | — | The filter only checks is_inventory and non-zero quantity; there is no uniqueness or already-reverted check. | N-U09-067 |
| VDR-U09-C313 | IAV-F03 | stock_account/models/stock_move.py:198-199 | _should_create_account_move | FACT | stock_account installed | — | The accounting entry for any completed move, including counts and scrap, is created by stock_account._create_account_move when _should_create_account_move is true. | N-U09-070 |
| VDR-U09-C314 | IAV-F04 | stock_account/models/stock_location.py:14 | Expense account used to re-qualify | FACT | stock_account installed | — | The location account help text: expense account used to re-qualify products removed from stock and sent to this location. | N-U09-071 |
| VDR-U09-C315 | IAV-F03 | stock_account/models/stock_move.py:216-218 | account_move._post() | FACT | stock_account installed | — | The account.move is posted immediately after creation and linked to the stock moves (account_move_id). | N-U09-079 |
| VDR-U09-C316 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:327-331 | def _find_delivery_ids_by_lot | FACT | always | — | Lot form shows the delivery orders and partners linked to the lot (traceability use case). | N-U09-086 |
| VDR-U09-C317 | FUNCTION MAPPING REQUIRED | product_expiry/models/production_lot.py:41-48 | lot.expiration_date <= current_date | FACT | product_expiry installed | — | product_expiry_alert is true when expiration_date <= now; alert_date and removal_date drive the earlier phases. | N-U09-099 |
| VDR-U09-C318 | FUNCTION MAPPING REQUIRED | stock/models/stock_lot.py:319-325 | produce_line_ids | FACT | always | — | _get_outgoing_domain references produce_line_ids (mrp field), so traceability into manufactured goods depends on the manufacturing extension. | N-U09-101 |
| VDR-U09-C319 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:20-23 | _parent_name = 'parent_package_id' | FACT | always | — | stock.package is a nested tree (_parent_store True, parent_package_id) for pallets-in-containers use. | N-U09-106 |
| VDR-U09-C320 | FUNCTION MAPPING REQUIRED | stock/models/stock_package.py:502-505 | 'parent_package_id': container_package.id | FACT | at done | — | At completion _apply_dest_to_package writes parent_package_id and clears package_dest_id (container taken). | N-U09-117 |
| VDR-U09-C321 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:159-162 | do_replenish | FACT | always | — | do_scrap finishes by optionally calling do_replenish; write-off is immediate on validation. | N-U09-124 |
| VDR-U09-C322 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:159 | scrap.write({'state': 'done'}) | FACT | at validation | — | state moves draft to done inside do_scrap after the move is completed. | N-U09-135 |
| VDR-U09-C323 | FUNCTION MAPPING REQUIRED | stock/models/stock_scrap.py:172 | env['stock.rule'].run | FACT | should_replenish | — | do_replenish calls stock.rule.run with a Procurement, relying on the procurement engine. | N-U09-137 |
| VDR-U09-C324 | RCN-F01 | stock/models/product.py:77-88 | Available quantity (computed as | FACT | always | — | Help text of free_qty/virtual_available explains the three planner questions (on hand, free, forecast). | N-U09-142 |
| VDR-U09-C325 | RCN-F01 | stock/report/report_stock_quantity.py:49-51 | drop_view_if_exists | FACT | always | — | report.stock.quantity is recreated as a SQL view on init and holds no stored data; product quantities are computed fields. | N-U09-152 |
| VDR-U09-C326 | RCN-F01 | stock/models/product.py:50-51 | used to compute quantities | FACT | always | — | product.product.stock_quant_ids and stock_move_ids exist to compute quantities. | N-U09-154 |
| VDR-U09-C327 | RCN-F01 | stock/models/product.py:392-394 | Warehouse.search( | INFERENCE | always | — | Default scope is built only from warehouse view locations, so internal locations outside any warehouse tree are excluded from default quantities. | N-U09-156 |
| VDR-U09-C328 | FUNCTION MAPPING REQUIRED | stock/security/stock_security.xml:5-8 | res_groups_privilege_inventory | FACT | always | — | Inventory privilege groups the two roles (User, Administrator) in the supply-chain category. | N-U09-158 |
| VDR-U09-C329 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:21-22 | access_stock_quant_all | INFERENCE | always | — | Read-only quant access for all internal users and write access limited to stock users reflects the stated purpose. | N-U09-159 |
| VDR-U09-C330 | FUNCTION MAPPING REQUIRED | stock/data/stock_sequence_data.xml:46-57 | interval_type | FACT | always | — | The scheduler cron is recurring (interval 1 days) with no state machine. | N-U09-167 |
| VDR-U09-C331 | FUNCTION MAPPING REQUIRED | stock/models/res_config_settings.py:46-47 | implied_group='stock.group_stock_multi_locations' | FACT | always | — | Settings switches imply feature groups (multi-locations, lots, packages, owners) onto internal users. | N-U09-168 |
| VDR-U09-C332 | FUNCTION MAPPING REQUIRED | base/models/ir_model.py:2170 | self._get_allowed_models(mode) | FACT | always | RT | ir.model.access.check tests the model against _get_allowed_models without a visible transient exemption in the lines read (2162-2174), so wizard ACL rows may bind ordinary users. | N-U09-170 |
| VDR-U09-C333 | FUNCTION MAPPING REQUIRED | stock/security/ir.model.access.csv:33 | access_stock_move_line_all | FACT | always | — | base.group_user holds read/write/create/unlink on stock.move.line; deletion of done lines is blocked only by the ondelete guard in code. | N-U09-171 |
