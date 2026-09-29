# Source Map (candidate) — `mrp_subcontracting`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_subcontracting` |
| Display name | MRP Subcontracting |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `5a97021e19cf476e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_subcontracting/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp`
- Direct dependents in 300-module list (5): `mrp_subcontracting_account`, `mrp_subcontracting_dropshipping`, `mrp_subcontracting_landed_costs`, `mrp_subcontracting_purchase`, `mrp_subcontracting_repair`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Manufacturing / Subcontract Productions
- Inventory of user-facing artifacts (counts): menu items 0, views 20, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 4, web routes 3
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (18): `change.production.qty`, `stock.return.picking`, `stock.return.picking.line`, `mrp.production.serials`, `stock.location`, `mrp.production`, `stock.warehouse`, `stock.move.line`, `stock.quant`, `stock.move`, `res.company`, `stock.picking`, `product.supplierinfo`, `product.product`, `stock.rule`, `res.partner`, `mrp.bom`, `report.mrp.report_bom_structure`
- Company-dependent settings introduced: 1 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `change.production.qty`, `stock.return.picking`, `stock.return.picking.line`, `mrp.production.serials`, `stock.location`, `mrp.production`, `stock.warehouse`, `stock.move.line`, `stock.quant`, `stock.move`, `res.company`, `stock.picking`, `product.supplierinfo`, `product.product`, `stock.rule`, `res.partner`, `mrp.bom`, `report.mrp.report_bom_structure`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 2 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 13 (of which company-scoped by text 0); access rows 17

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 79 of 79 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: mrp_subcontracting

Source revision: 19.0.post20260921 (Odoo 19 Community). All pointers are `module/path:LINE` relative to the addons root. `(TEST)` marks claims derived from the module's own tests. Neutral business language; no code copied.

## 1. Capabilities and activation
- Purpose: let a company send components to an external subcontractor and receive the finished product back; receiving the finished product drives the production record. Manifest `depends` only on Manufacturing (`mrp_subcontracting/__manifest__.py:10`).
- Core vs optional: it is an OPTIONAL module (no auto-install in its manifest; grep of `mrp_subcontracting/__manifest__.py` finds none). It is switched on from the Manufacturing settings page via the "Subcontracting" checkbox (`mrp/models/res_config_settings.py:16`, `mrp/views/res_config_settings_views.xml:32-33`).
- Conditional behaviour keyed on BoM type: a new BoM type "Subcontracting" is added (`mrp_subcontracting/models/mrp_bom.py:11-13`); nothing happens for a receipt unless a matching subcontract BoM is found (`mrp_subcontracting/models/stock_move.py:150-152`).
- Bridge modules that auto-install when their partners are present: `mrp_subcontracting_account` (with mrp_account), `mrp_subcontracting_purchase` (with purchase_mrp), `mrp_subcontracting_dropshipping` (with stock_dropshipping), `mrp_subcontracting_landed_costs` (with stock_landed_costs), `mrp_subcontracting_repair` (with repair) - each manifest carries an auto-install flag (e.g. `mrp_subcontracting_account/__manifest__.py:13`).
- Uninstall clean-up: archives subcontracting locations, operation types, unlinks routes if unused (`mrp_subcontracting/__init__.py:9-26`, registered `mrp_subcontracting/__manifest__.py:142`).
- Portal for subcontractors (external vendors log in and record production): pages `/my/productions...` (`mrp_subcontracting/controllers/portal.py:23,76,85`).

## 2. Business objects and lifecycle
- Subcontract BoM: BoM type plus a "Subcontractors" list of partners (`mrp_subcontracting/models/mrp_bom.py:14`); form shows the field only for that type and requires it (`mrp_subcontracting/views/mrp_bom_views.xml:9`); consumption policy field hidden for this type (`views/mrp_bom_views.xml:11-13`). Lookup honours the partner hierarchy (a child contact matches a parent subcontractor) (`models/mrp_bom.py:16-22`).
- Subcontractor location: each partner has a company-dependent "Subcontractor Location" (`models/res_partner.py:10-13`); each company gets one default "Subcontracting" internal location, stored on the company and set as the default for partners (`models/res_company.py:22-35`). Subcontracting locations must be internal type and the company default cannot be altered (`models/stock_location.py:12-18`). Subcontracting stock is therefore real, valued-eligible internal stock, not a virtual location.
- Resupply of components: per warehouse flag "Resupply Subcontractors" (default on) (`models/stock_warehouse.py:11-12`) creates a "Resupply Subcontractor" operation type (internal transfer, warehouse stock -> subcontracting location) (`models/stock_warehouse.py:143-153,186-192`), a warehouse route (`:66-88`) and two make-to-order pull rules (`:90-130`); the global route "Resupply Subcontractor on Order" is seeded (`data/mrp_subcontracting_data.xml:7-14`). The delivery picking to the subcontractor gets the subcontractor's location as destination (`models/stock_picking.py:23-33`). The route can be set to "stock else trigger another rule" (TEST `tests/test_subcontracting.py:1499`).
- Receipt that triggers production: when a receipt (supplier -> internal) line for a product with a matching subcontract BoM is confirmed, the line is flagged as a subcontract receipt and its source becomes the subcontractor's location (`models/stock_move.py:146-162`). After confirmation one production order per line is created and confirmed (`models/stock_picking.py:143-182`), sourced and finished in the subcontractor location, with subcontractor = the receipt partner's commercial partner, planned start = receipt date minus BoM manufacturing lead time (`models/stock_picking.py:105-135`). The production's finished move feeds the receipt line (`models/stock_picking.py:178-181`).
- Production states (inherited from Manufacturing): Draft, Confirmed, In Progress, To Close, Done, Cancelled (`mrp/models/mrp_production.py:177-190`). The subcontract production view shows the bar Draft/Confirmed/Done (`mrp_subcontracting/views/mrp_production_views.xml:14`).
- Receipt validation closes the production automatically with component-consumption checks skipped (`models/stock_picking.py:45-58`, `models/mrp_production.py:106-109`); production stock moves are back-dated one second before the receipt (`models/stock_picking.py:51-56`).
- Backorders: partial receipts split the production so component reservations follow (`models/stock_picking.py:147-160`); backorder without cancel does not re-trigger component procurement (`models/stock_picking.py:137-140`) (TEST `tests/test_subcontracting.py:601,651,699`).
- Tracked (lot/serial) products: one production per lot/serial on the receipt; quantities and orphan productions are kept in sync when receipt lines change (`models/stock_move.py:230-293`, `models/stock_move_line.py:22-40`) (TEST `:1141,1244,804`).

## 3. Actions, gating, constraints, automation
- Constraint: a subcontract BoM cannot have operations or by-product lines (`models/mrp_bom.py:24-27`). Workorders are disabled for subcontractor productions (`models/mrp_production.py:114-118`).
- Blocked actions: merge of subcontract productions (`models/mrp_production.py:101-104`); unbuild of a subcontracted production (`models/mrp_unbuild.py:10-14`) (TEST `tests/test_subcontracting.py:994`).
- Cancelling a subcontract receipt line cancels its open productions (`models/stock_move.py:127-141`). Reserving subcontract receipt lines is bypassed (`models/stock_move.py:199-207`). Push rules never propagate the subcontract flag (`models/stock_rule.py:11-14`); pull-rule assignment skips subcontract moves (`models/stock_rule.py:23-25`).
- Changing receipt date moves the production dates; changing production quantity is not pushed to the receipt when it is a subcontract (`models/stock_move.py:63-70`, `wizard/change_production_qty.py:10-13`).
- Splitting a production for lot/serial capture (`models/mrp_production.py:126-143`); serial-number bulk entry (`wizard/mrp_production_serial_numbers.py:9-48`).
- Returns: returning a subcontract receipt sends goods back to the subcontractor location and clears the subcontract flag on the return (`wizard/stock_picking_return.py:10-25`) (TEST `tests/test_subcontracting.py:1050,1095`).
- Portal write limits: subcontractor users may write only component lines, lot, produced quantity and product quantity on productions (`models/mrp_production.py:56-60,123-124`); may not create or set moves to Done (`models/stock_move.py:213-216`).
- Stock rule sets the partner on component moves from the production's subcontractor (`models/stock_rule.py:16-21`); lead-time report and BoM overview add a subcontracting line and use the subcontracting location's stock (`report/mrp_report_bom_structure.py:22-33,101-117,119-133`) (TEST `tests/test_subcontracting.py:565`).

## 3b. Security (portal-only; no new internal user group)
Access rights: 17 portal-only entries, mostly read, some write/create for stock moves, move lines, lots, consumption warnings (`security/ir.model.access.csv:2-18`). Thirteen record rules, all for the Portal group and keyed on the logged-in user's commercial partner (`security/mrp_subcontracting_security.xml`):
1. Productions (`:4-9`): portal sees only productions where they are the subcontractor.
2. BoMs (`:11-16`): only BoMs listing them as subcontractor.
3. BoM lines (`:18-23`): only lines of those BoMs.
4. Consumption warnings (`:25-30`): only warnings of their productions.
5. Consumption warning lines (`:32-37`): same, line level.
6. Stock moves (`:39-50`): moves produced by, feeding, or consuming for their productions.
7. Stock move lines (`:52-63`): detail lines of those moves.
8. Pickings (`:65-70`): only pickings addressed to their partner.
9. Picking types (`:72-77`): only types used by their pickings/productions.
10. Locations (`:79-98`): their pickings' locations, their production locations and warehouse view roots.
11. Warehouses (`:100-105`): only warehouses of their pickings.
12. Lots (`:107-118`): lots of products in their BoMs (finished or components).
13. Product templates (`:120-131`): products in their BoMs (finished or components).
Sudo use: putaway checks for subcontractor users run with elevated rights (`models/stock_location.py:20-25`); BoM search on receipt runs elevated (`models/stock_move.py:176`); partner "is subcontractor" requires a portal user and a subcontract BoM (`models/res_partner.py:54-63`).
Company scoping: no rule references company; scoping is by partner. Company is applied through the company subcontracting location, BoM company/`check_company` on subcontractors (`models/mrp_bom.py:14`), BoM lookup by company (`models/stock_move.py:176-182`), production creation grouped per company (`models/stock_picking.py:145-176`), and portal session restricted to the picking's company (`controllers/portal.py:92-104`).

## 4. Accounting / inventory / purchase / dropship handoffs (this module)
- Owns: subcontract flag, production creation, component resupply, receipt-triggered production closing. It does NOT set the product cost; cost is set in `mrp_subcontracting_account` (see that note) using `mrp_account`.
- Cost display only: BoM overview adds the vendor price of the subcontractor to BoM cost (`report/mrp_report_bom_structure.py:10-20,30-32`).
- Purchase receipt counting: subcontract-location moves count as received quantity (`models/stock_move.py:209-211`).
- Purchase/dropship linkage lives in the bridge modules, not here.

## 5. Configuration that changes outcomes
- BoM type and subcontractor list; vendor price list entry for the product and subcontractor (`models/product.py:10-26` marks "Subcontracted" and filters sellers by subcontractor list).
- BoM manufacturing lead time drives production start (`models/stock_picking.py:131`); days-to-prepare-MO is used in lead-time reports (`report/mrp_report_bom_structure.py:131-132`).
- Warehouse "Resupply Subcontractors" enables/disables resupply rules and operation type (`models/stock_warehouse.py:36-44,201-216`). Subcontracting operation type is created inactive (`models/stock_warehouse.py:181-185`).
- Partner subcontractor location changes where new receipts source from (TEST `tests/test_subcontracting.py:920`).
- Tracking (none/lot/serial) changes number of productions (see section 2).

## 6. Effective extension path (who inherits key models)
Community modules extending subcontracting models or behaviour: `mrp_subcontracting_account`, `mrp_subcontracting_purchase`, `mrp_subcontracting_dropshipping`, `mrp_subcontracting_landed_costs` (`mrp_subcontracting_landed_costs/models/stock_landed_cost.py:7-18`), `mrp_subcontracting_repair` (bridge only, no models). Base modules reference it only lightly: `mrp` (settings toggle, picking view of productions `mrp/models/stock_picking.py:159`, consumption warning view `mrp/wizard/mrp_consumption_warning_views.xml:41`). `purchase_requisition_sale` mentions subcontracted services in its description only (`purchase_requisition_sale/__manifest__.py:6`).

## 7. By-products
A subcontract BoM cannot carry by-product lines (`mrp_subcontracting/models/mrp_bom.py:24-27`), so no by-product cost-share applies on the BoM path. The generic cost-share logic sits in `mrp_account/models/mrp_production.py:79-93`. Whether a by-product can be added manually to an individual subcontract production after creation: UNKNOWN - EVIDENCE INSUFFICIENT.

## 8. UNKNOWN items
- Behaviour for multi-company shared subcontractors beyond the pointers above: UNKNOWN - EVIDENCE INSUFFICIENT.
- Manual by-products on a live subcontract production: UNKNOWN - EVIDENCE INSUFFICIENT.
- Exact qty-producing assignment path at receipt validation (production quantity is set through the split/sync logic and closing skips consumption checks; the precise field assignment was not traced): UNKNOWN - EVIDENCE INSUFFICIENT.

