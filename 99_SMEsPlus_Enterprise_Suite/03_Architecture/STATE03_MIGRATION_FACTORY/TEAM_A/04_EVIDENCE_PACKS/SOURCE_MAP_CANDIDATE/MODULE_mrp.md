# Source Map (candidate) — `mrp`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp` |
| Display name | Manufacturing |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `fa9632ee3a09caca` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `product`, `stock`, `resource`
- Direct dependents in 300-module list (8): `mrp_account`, `mrp_landed_costs`, `mrp_product_expiry`, `mrp_repair`, `mrp_subcontracting`, `project_mrp`, `purchase_mrp`, `sale_mrp`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `pos_mrp`, `test_main_flows`
- Custom / third-party modules that declare a dependency (name — license only) (5): `scgl_inventory_lot_filter` — LGPL-3, `19_bhpro_master_data` — OPL-1, `import_bridge_axis` — OPL-1, `smesplus_inventory_lot_filter` — LGPL-3, `scgl_dashboard_logistics` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Manufacturing / Manufacturing Orders & BOMs
- Inventory of user-facing artifacts (counts): menu items 21, views 85, window actions 39, server actions 11, reports 6, mail templates 0, scheduled jobs 0, wizards 15, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (26): `stock.warn.insufficient.qty.unbuild` (Warn Insufficient Unbuild Quantity); `change.production.qty` (Change Production Qty); `mrp.consumption.warning` (Wizard in case of consumption in warning/strict and more component has been used for a MO (related to the bom)); `mrp.consumption.warning.line` (Line of issue consumption); `mrp.production.split.multi` (Wizard to Split Multiple Productions); `mrp.production.split` (Wizard to Split a Production); `mrp.production.split.line` (Split Production Detail); `mrp.production.backorder.line` (Backorder Confirmation Line); `mrp.production.backorder` (Wizard to mark as done or create back order); `mrp.production.serials` (Assign serial numbers to production order); `mrp.unbuild` (Unbuild Order); `mrp.routing.workcenter` (Work Center Usage); `mrp.production.group` (Production Group); `mrp.production` (Manufacturing Order); `mrp.workorder` (Work Order); `mrp.bom` (Bill of Material); `mrp.bom.line` (Bill of Material Line); `mrp.bom.byproduct` (Byproduct); `mrp.workcenter` (Work Center); `mrp.workcenter.tag` (Add tag for the workcenter); `mrp.workcenter.productivity.loss.type` (MRP Workorder productivity losses); `mrp.workcenter.productivity.loss` (Workcenter Productivity Losses); `mrp.workcenter.productivity` (Workcenter Productivity Log); `mrp.workcenter.capacity` (Work Center Capacity); `report.mrp.report_mo_overview` (MO Overview Report) … (+1)
- Objects extended from other modules (31): `product.replenish`, `stock.warn.insufficient.qty`, `picking.label.type`, `stock.replenishment.info`, `mail.thread`, `mail.activity.mixin`, `ir.attachment`, `stock.warehouse`, `stock.warehouse.orderpoint`, `stock.replenish.mixin`, `stock.scrap`, `stock.move.line`, `stock.quant`, `product.document`, `stock.move`, `stock.reference`, `res.company`, `stock.picking.type`, `stock.picking`, `stock.traceability.report`, `product.template`, `product.product`, `stock.rule`, `stock.route`, `res.config.settings` … (+6)
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 7 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `change.production.qty` ← Community: `mrp_subcontracting`; open-license custom/third-party scanned: —
- `mrp.production.serials` ← Community: `mrp_subcontracting`; open-license custom/third-party scanned: —
- `mrp.production` ← Community: `mrp_account`, `mrp_product_expiry`, `mrp_repair`, `mrp_subcontracting`, `mrp_subcontracting_account`, `project_mrp`, `project_mrp_account`, `purchase_mrp`, `sale_mrp`; open-license custom/third-party scanned: —
- `mrp.workorder` ← Community: `mrp_account`, `project_mrp_account`; open-license custom/third-party scanned: —
- `mrp.bom` ← Community: `mrp_subcontracting`, `project_mrp`, `purchase_mrp`, `sale_mrp`; open-license custom/third-party scanned: —
- `mrp.bom.line` ← Community: `purchase_mrp`; open-license custom/third-party scanned: —
- `mrp.workcenter` ← Community: `mrp_account`; open-license custom/third-party scanned: —
- `mrp.workcenter.productivity` ← Community: `mrp_account`; open-license custom/third-party scanned: —
- `report.mrp.report_mo_overview` ← Community: `mrp_account`, `purchase_mrp`; open-license custom/third-party scanned: —
- `report.mrp.report_bom_structure` ← Community: `mrp_subcontracting`, `mrp_subcontracting_purchase`, `purchase_mrp`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `product.replenish`, `stock.warn.insufficient.qty`, `picking.label.type`, `stock.replenishment.info`, `mail.thread`, `mail.activity.mixin`, `ir.attachment`, `stock.warehouse`, `stock.warehouse.orderpoint`, `stock.replenish.mixin`, `stock.scrap`, `stock.move.line`, `stock.quant`, `product.document`, `stock.move`, `stock.reference`, `res.company`, `stock.picking.type`, `stock.picking`, `stock.traceability.report`, `product.template`, `product.product`, `stock.rule`, `stock.route`, `res.config.settings` … (+6)

## 6. Actions / states / validation / automation / security
- State fields found: `mrp.unbuild` → ['draft', 'done']; `mrp.production` → ['draft', 'confirmed', 'progress', 'to_close', 'done', 'cancel']; `mrp.workorder` → ['blocked', 'ready', 'progress', 'done', 'cancel']
- Validation: 14 declarative constraint method(s), 7 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 8 (`group_mrp_user`, `group_mrp_manager`, `group_mrp_routings`, `group_mrp_byproducts`, `group_unlocked_by_default`, `group_mrp_reception_report` … (+2)); record rules 9 (of which company-scoped by text 9); access rows 54

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 158 of 159 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: `mrp` (Manufacturing)

- Source revision: `19.0.post20260921` (Odoo 19.0 Community, addons root = `odoo/addons`).
- Method: static reading only. No code copied, Odoo not run. Pointers are `path:LINE` relative to the addons root.
- Test-derived statements are marked `(TEST)`. Anything unproven is marked `UNKNOWN — EVIDENCE INSUFFICIENT`.
- Skeleton used: `sourcemap/mrp.json` (depends: product, stock, resource; `mrp/__manifest__.py:11`; flagged as an application at `mrp/__manifest__.py:57`).

## 1. Capabilities (Core / Optional / Conditional)

| Capability | Tier | What the source shows |
|---|---|---|
| Bill of Materials, two types: "Manufacture this product" and "Kit" | Core | Type choice and default: `mrp/models/mrp_bom.py:27-30` |
| BoM per product template or per single variant | Core | `mrp/models/mrp_bom.py:31-40`; matching order: variant BoM first, then template BoM, ordered by sequence: `mrp/models/mrp_bom.py:385-417` |
| Components with quantity, unit, sequence, "consumed in operation" | Core | `mrp/models/mrp_bom.py:684-712`; zero-quantity lines are allowed (used as optional lines): `mrp/models/mrp_bom.py:719-722` |
| Component/operation/by-product applied only to chosen variants ("Apply on Variants") | Core | `mrp/models/mrp_bom.py:701-705`, filter at `mrp/models/mrp_bom.py:762`; cannot be combined with a variant-specific BoM: `mrp/models/mrp_bom.py:187-189` |
| By-products with a cost-share percentage | Core in data model; UI page only for group "Produce residual products" | Model `mrp/models/mrp_bom.py:846-870`; page gated by group at `mrp/views/mrp_production_views.xml:482` and `mrp/views/mrp_bom_views.xml:150`; group defined `mrp/security/mrp_security.xml:31` |
| Operations (routing lines) and work centers | Optional, group "Manage Work Order Operations" | Group `mrp/security/mrp_security.xml:27`; setting `mrp/models/res_config_settings.py:16-17`; MO Work Orders page gated `mrp/views/mrp_production_views.xml:476` |
| Operation dependencies (blocked-by) | Optional, needs routings on plus its own group | Group `mrp/security/mrp_security.xml:43`; setting `mrp/models/res_config_settings.py:20`; BoM flag `mrp/models/mrp_bom.py:86-88`; setting depends on routing setting `mrp/views/res_config_settings_views.xml:22` |
| Operation duration: fixed or computed from last N work orders | Conditional (per operation) | `mrp/models/mrp_routing.py:27-37` |
| Work center: hourly cost, setup/cleanup time, efficiency, alternative work centers, per-product capacity, OEE, blocking with loss reasons | Core when routings on | `mrp/models/mrp_workcenter.py:21-82`, capacity lookup `mrp/models/mrp_workcenter.py:427-437`, loss categories `mrp/data/mrp_data.xml:25-70` |
| Work orders (start, pause, finish, block, plan, replan) | Optional (follows routings) | `mrp/models/mrp_workorder.py:656-775`, `mrp/models/mrp_workorder.py:938-945` |
| Manufacturing orders (MO) | Core | `mrp/models/mrp_production.py:38` |
| Backorders on partial completion | Core; behaviour set on the operation type (Ask / Always / Never) | Operation-type setting is owned by stock: `stock/models/stock_picking.py:133-138`; used at `mrp/models/mrp_production.py:2374-2390` |
| Split MO / merge MOs | Core (both only in draft or confirmed) | Split `mrp/models/mrp_production.py:2518-2532`; merge `mrp/models/mrp_production.py:2534-2601`; gate `mrp/models/mrp_production.py:2897-2921` |
| Change quantity of an open MO | Core (wizard) | `mrp/wizard/change_production_qty.py:48-92` |
| Scrap from an MO or work order | Core (scrap object is owned by stock, extended here) | `mrp/models/mrp_production.py:2409-2422`, `mrp/models/stock_scrap.py:10-36` |
| Unbuild (disassemble a finished product, from an MO or from the BoM) | Core | `mrp/models/mrp_unbuild.py:1-342` |
| Flexible consumption policy: Allowed / Allowed with warning / Blocked | Core; set per BoM, copied to MO at confirmation | BoM `mrp/models/mrp_bom.py:70-84`; MO copy `mrp/models/mrp_production.py:261-268` and `mrp/models/mrp_production.py:1632-1633` |
| Batch size (automatic MOs cut into batches) | Conditional (per BoM tick-box, normal BoM only) | `mrp/models/mrp_bom.py:96-97`; UI `mrp/views/mrp_bom_views.xml:190-193`; splitting `mrp/models/stock_rule.py:93-100` |
| Kit (phantom) BoM: exploded into components on sales/transfers, kit stock shown from components | Core | `mrp/models/stock_move.py:374-407`, kit quantities `mrp/models/product.py:271-290`, procurement explosion `mrp/models/stock_rule.py:40-71` |
| Replenishment through the Manufacture route (reordering rules, MTO, procurement) | Core | `mrp/models/stock_rule.py:10-16`, `mrp/models/stock_rule.py:81-122` |
| Multi-step manufacturing: 1 step / pick components then manufacture / pick, manufacture, store | Conditional (warehouse setting) | `mrp/models/stock_warehouse.py:31-38`, routing keys `mrp/models/stock_warehouse.py:57-69`, `:99-101` |
| BoM structure/cost report and MO overview report (planned vs. actual cost, availability, replenishment lines) | Core | `mrp/report/mrp_report_bom_structure.py:12-`, `mrp/report/mrp_report_mo_overview.py:12-`; BoM cost uses the product standard price: `mrp/report/mrp_report_bom_structure.py:337` |
| Allocation (reception) report for MOs | Optional, group | `mrp/security/mrp_security.xml:39`, `mrp/models/res_config_settings.py:19` |
| "Unlock Manufacturing Orders" default | Optional, group | `mrp/security/mrp_security.xml:35`; effect on MO lock: `mrp/models/mrp_production.py:77-78` |
| Master Production Schedule, PLM, Quality toggles | Not available in this Community tree | Settings use upgrade-style toggles `mrp/views/res_config_settings_views.xml:39,62`; no such module directory exists under the addons root (directory listing) |
| Subcontracting toggle | Optional module | `mrp/models/res_config_settings.py:16`; module `mrp_subcontracting` |

## 2. Business objects and lifecycle

### 2.1 Objects
- BoM `mrp.bom` (lines `mrp.bom.line`, by-products `mrp.bom.byproduct`, operations `mrp.routing.workcenter`): `mrp/models/mrp_bom.py:12,674,846`, `mrp/models/mrp_routing.py`.
- Work center `mrp.workcenter`, time logs `mrp.workcenter.productivity`, loss reasons, capacity: `mrp/models/mrp_workcenter.py:21,440-646`.
- MO `mrp.production` and a "production group" that links parent/child/backorder MOs: `mrp/models/mrp_production.py:24-38`.
- Work order `mrp.workorder`: `mrp/models/mrp_workorder.py:15`. Unbuild `mrp.unbuild`: `mrp/models/mrp_unbuild.py`.
- Stock moves carry the MO link (raw material moves = components, finished moves = product and by-products). MOs do not hold quantities themselves; stock owns the moves (see section 4).

### 2.2 MO states (stored, but computed from moves and work orders)
States: Draft, Confirmed, In Progress, To Close, Done, Cancelled (`mrp/models/mrp_production.py:177-191`). The state is a computed field, so it changes as a result of move/work-order events rather than by a free status write (`mrp/models/mrp_production.py:573-604`):
1. Cancelled: state already cancelled, or all finished moves cancelled.
2. Done: already done, or all component and finished moves are done/cancelled.
3. To Close: all work orders are done/cancelled; or, with no work orders, the "quantity producing" has reached the planned quantity.
4. In Progress: any work order in progress/done, or a non-zero quantity producing, or any component marked picked.
5. Draft is the fallback; Confirmed is set explicitly by confirmation (below).

Transitions and gates:
- Draft to Confirmed: `action_confirm` (`mrp/models/mrp_production.py:1625-1667`). Gate: all records must belong to the same allowed company set (`_check_company`, `mrp/models/mrp_production.py:1626`). It copies the BoM consumption policy onto the MO (`:1632-1633`), forces the unit to the product unit for serial-tracked products (`:1635-1645`), confirms component and finished moves and work orders, triggers the stock scheduler for shortages, and only then sets Confirmed for draft MOs (`:1652-1666`).
- Planning: "Plan" confirms a draft MO first and then schedules work orders on the work-center calendars (`mrp/models/mrp_production.py:1708-1744`); "Unplan" is refused once any work order is done or started (`:1746-1759`).
- Readiness (separate from state): Waiting / Ready / Waiting Another Operation, driven by component availability, or, when the BoM says "when components for 1st operation are available", by the first operation only (`mrp/models/mrp_production.py:663-689`, `:1472-1490`; BoM option `mrp/models/mrp_bom.py:56-59`).
- Mark Done: `button_mark_done` (`mrp/models/mrp_production.py:2219-2339`) after `pre_button_mark_done` (`:2341-2390`). Ordered gates:
  1. Company check and serial-number uniqueness (`:2392-2395`, `:2783-2852`).
  2. Tracked finished product with no lot/serial set: an error for several MOs, or the serial-generation wizard for one (`:2343-2358`). The auto path is skipped for tracked products unless quantity is 1 or the reservation state allows it (`:2397-2400`).
  3. Consumption check (skipped only by an explicit context flag) opens the consumption wizard when picked quantities differ from expected (`:1761-1799`, `:2368-2370`).
  4. Quantity check: if produced is less than planned, behaviour follows the operation type (Ask opens the backorder wizard; Always creates a backorder without asking; Never closes and cancels the remainder) (`:2373-2390`; wizard `mrp/wizard/mrp_production_backorder.py:31-43`).
  5. Then work orders are finished, backorders are split off, stock moves are posted, unpicked components are cancelled (not consumed), leftover zero-quantity moves are set done, and the MO is stamped done, locked, priority reset (`:2229-2258`, `:1907-1956`).
- Cancel: `action_cancel` refuses a done MO (`mrp/models/mrp_production.py:1842-1848`). It cancels open work orders, open moves and unstarted linked pickings (`:1850-1898`). Special case: after cancelling, an MO whose BoM policy is "Allowed" and that is neither done nor cancelled is forced to Done (`:1888-1896`). Deleting an MO requires it to be cancelled first and never when done (`:1130-1140`, `:1463-1470`).
- Cancelling all component moves elsewhere cancels the MO (skipped when the flag `skip_mo_check` is set): `mrp/models/stock_move.py:433-439`.
- Lock: a done MO is locked on completion; locked/unlocked default follows the "Unlocked by default" group (`mrp/models/mrp_production.py:77-78`, `:2254`, `:729-735`).

### 2.3 Consumption policy details
- Default on the BoM is "Allowed with warning" (`mrp/models/mrp_bom.py:79`); the MO copy defaults to Allowed until confirmation (`mrp/models/mrp_production.py:261-268`). No BoM on the MO means no consumption check (`:1773`).
- "Blocked" is enforced by the wizard screen: the Confirm button is hidden and a manager-only force button is shown (`mrp/wizard/mrp_consumption_warning_views.xml:37-39`). The server-side confirm method has no group check (`mrp/wizard/mrp_consumption_warning.py:32-35`). `(TEST)` a manager forcing a Blocked case finishes the MO as Done: `mrp/tests/test_order.py:847-884`.
- Components attached to an operation are "manual consumption" by default, i.e. the operator must pick them; others are auto-picked at completion (`mrp/models/stock_move.py:80-87`, `:669-676`; `mrp/models/mrp_production.py:2360-2364`).

### 2.4 Work order states
Blocked, To Do, In Progress, Finished, Cancelled (`mrp/models/mrp_workorder.py:66-73`).
- Blocked or To Do is recomputed from "quantity ready", which depends on predecessor work orders (`:152-160`, `:248-261`). Without dependencies enabled, each work order is blocked by the previous one in sequence; with dependencies, by the declared operations (`mrp/models/mrp_production.py:1669-1701`).
- Start: refused if the work center is blocked, or the order is done/cancelled; creates a calendar slot and time log, and stamps the MO start (`mrp/models/mrp_workorder.py:656-703`).
- Finish: marks unpicked components/by-products of that operation as picked using the current or planned quantity, closes time logs, sets quantity produced and freezes the hourly cost (`:705-736`). "Mark as done" refuses a blocked work center (`:938-945`).
- Quantity produced cannot be edited on a done/cancelled work order or be negative (`:490-498`); dependencies must not be cyclic (`:298-301`).
- Cost of an operation: expected duration if cost mode is "estimated", otherwise the logged time, times hourly cost (`:638-654`, `:956-959`).

### 2.5 Unbuild
- States: Draft, Done only (`mrp/models/mrp_unbuild.py:79-81`). Quantity must be positive (`:83-86`); done unbuilds cannot be deleted (`:139-141`).
- Gates in `action_unbuild` (`:165-250`): a lot is required for a tracked product; a linked MO must be Done; lots/serials of components need an MO reference.
- With an MO, the unbuild reverses the actual consumed/produced moves proportionally; without an MO it uses the current BoM explosion (`:252-291`).
- Validation compares available quantity at the source location with the unbuild quantity and opens an "insufficient quantity" wizard instead of failing (`:320-342`, `mrp/wizard/stock_warn_insufficient_qty.py`).
- Source and destination locations must be internal locations (`:61-74`); default location follows the company's first warehouse (`:96-104`).
- `UNKNOWN — EVIDENCE INSUFFICIENT`: whether an unbuild larger than the MO's produced quantity is blocked in `mrp` (no check found in `mrp/models/mrp_unbuild.py`; a code comment at `:203` says repeated unbuilds with lots on one MO are not fully handled).

## 3. Validations, automation, security, multi-company

### 3.1 Validations and constraints
- BoM: quantity greater than zero (`mrp/models/mrp_bom.py:99-102`); no cycles between finished product and components, including through sub-BoMs, and re-checked on archive/unarchive/resequence (`:132-182`, `:273-274`); by-product cannot equal the BoM product, cost shares are not negative and total at most 100 per variant (`:184-211`); kit BoM not allowed for a product that has a reordering rule (`:352-357`); batch size must be positive when enabled (`:359-361`); cannot delete a BoM with a running (not done/cancelled) MO (`:363-367`). Editing a BoM flags matching draft/confirmed MOs as "outdated BoM" (`:268-275`, `:487-519`).
- BoM line quantity may be zero but not negative (`mrp/models/mrp_bom.py:719-722`).
- MO: reference unique per company (`mrp/models/mrp_production.py:306-309`); quantity positive (`:310-313`); by-product cost share not negative and at most 100 in total (`:979-985`); only one lot for lot-tracked products (`:987-991`); product cannot change once out of draft (`:994-995`); date changes refused on done/cancelled MO and un-plan a planned MO (`:1043-1049`); split cannot exceed planned quantity (`:2009-2013`); split/merge rules (`:2897-2921`: same product, same BoM, same state, same operation type, no manually added components or by-products, at least two).
- Manufacturing operation type cannot use a scrap-type destination (`mrp/models/stock_picking.py:74-78`).
- Components lots: creating lots for components on an MO is refused unless the operation type allows it (`mrp/models/stock_lot.py:8-17`).
- Kit products: quantity cannot be adjusted directly, only components (`mrp/models/stock_quant.py:4-5`).
- `(TEST)` cycle detection scenarios: `mrp/tests/test_bom.py:2096-2230`.

### 3.2 Automation and scheduler
- `mrp` defines no scheduled job of its own (no cron records under `mrp/data` or `mrp/views`; only a menu shortcut to stock's scheduler action at `mrp/views/stock_move_views.xml:102`). Automatic MO creation rides on stock's scheduler and procurement.
- After the scheduler has run all reordering rules, draft MOs created by a rule that already have component moves are confirmed in one pass (`mrp/models/stock_orderpoint.py:242-251`).
- Auto-confirm of MOs created by procurement: confirmed at creation when it is a reordering-rule MO without components (BoM-less) or has an MTO chain; MOs with components created by a rule stay draft until the scheduler post-step (`mrp/models/stock_rule.py:35-39`, `:120`).
- Install hooks add the manufacture route/operation type to every existing warehouse (`mrp/__init__.py:18-23`) and pre-create two stock-move columns for speed (`:10-15`).

### 3.3 Security groups
- Manufacturing User implies Inventory User (`mrp/security/mrp_security.xml:11-16`); Administrator implies User and is granted to the root and admin users (`:17-25`).
- Feature groups (not role groups): routings/work orders, by-products, unlocked by default, allocation report, operation dependencies (`:27-46`). These mainly gate screens and menus; the underlying models still exist and operate when the group is off (evidence: gating is in views, e.g. `mrp/views/mrp_production_views.xml:476,482`). One exception: turning routings off archives every operation, and turning it on again reactivates the most recently written archived batch (`mrp/models/res_config_settings.py:23-34`).
- Access: MO, work order, unbuild: User has read/write/create/delete (`mrp/security/ir.model.access.csv:11,23,38`); BoM, lines, by-products, work centers, operations: User read only, Administrator full (`:8-9`, `:12-17`). Inventory users (without Manufacturing) can read MOs and BoMs (`:18`, `:33-34`).
- Deleting an MO is further limited by business rules in section 2.2, not by access rights.

### 3.4 Company scoping and multi-company
- MO, work order, unbuild, time logs: visible only if the company is among the user's allowed companies (`mrp/security/mrp_security.xml:50-59`, `:68-71`, `:98-101`).
- BoM, BoM line, by-product, operation, work center: company-less (empty) records are visible to all allowed companies (`:62-65`, `:74-95`).
- BoM search when procuring restricts to that company plus company-less BoMs (`mrp/models/mrp_bom.py:376-377`).
- Kit status depends on the current company: a kit BoM owned by another company does not make the product a kit (`mrp/models/product.py:42-47`). `(TEST)` `mrp/tests/test_multicompany.py:186-215`.
- The record-rule domain uses all allowed companies, not the single active company, so a multi-company user sees several companies' MOs at once; `action_confirm` and mark-done then check company consistency of the linked records (`mrp/models/mrp_production.py:1626`, `:2393`).
- An unbuild sequence is created per company (`mrp/models/res_company.py:9-34`).
- `UNKNOWN — EVIDENCE INSUFFICIENT`: whether an MO in one company can consume components from another company's warehouse via inter-company flows (no such rule inside `mrp`).

## 4. Handoffs (who owns what)

| Concern | Owner | Evidence in `mrp` |
|---|---|---|
| Stock moves, reservation, quants, lots, locations, scrap object, operation type (backorder policy, reservation method), scheduler, reordering rules | `stock` | `mrp` only extends them: `mrp/models/stock_move.py:9`, `mrp/models/stock_orderpoint.py:10`, `mrp/models/stock_picking.py:10`, `mrp/models/stock_scrap.py`; reservation at confirm vs manual vs by date: `stock/models/stock_picking.py:68-72`; `mrp/models/mrp_production.py:1065-1072` uses it when re-reserving after an operation-type change |
| Component reservation on MO | `stock`, triggered by `mrp` | `action_assign` reserves component moves (`mrp/models/mrp_production.py:1703-1706`); finished output can free waiting moves (`:2239-2241`); backorders reserved after completion only when the operation type reserves at confirmation (`:2259-2265`) |
| Component consumption and finished-goods receipt | `stock` moves, driven by `mrp` | `mrp/models/mrp_production.py:1907-1956`; unpicked component moves are cancelled at completion (`:1911-1914`) |
| Cost of the finished product (component value, work-center cost, extra cost, by-product cost share), WIP and labour journal entries, analytic lines for work orders | `mrp_account` (auto-installed with `mrp` and `stock_account`) | `mrp` leaves an empty hook `_cal_price` (`mrp/models/mrp_production.py:1903-1905`) and freezes the work center hourly cost onto the work order (`mrp/models/mrp_workorder.py:716`); the computation is in `mrp_account/models/mrp_production.py:57-95`, posted after inventory at `:141-144` |
| BoM report costs | `mrp` (uses product standard price); enrichments by `mrp_account`, `purchase_mrp`, `mrp_subcontracting` | `mrp/report/mrp_report_bom_structure.py:337`; extensions exist for reports (files under `mrp_account/report`, `purchase_mrp/report`, `mrp_subcontracting/report`) |
| Make-to-order from sales / purchases of components / dropship | `sale_stock`+`sale_mrp`, `purchase_stock`+`purchase_mrp` | `mrp` receives procurements via the Manufacture rule (`mrp/models/stock_rule.py:81-122`); `sale_mrp` links MO to the sale line and back-order values (`sale_mrp/models/mrp_production.py:41-50`); `purchase_mrp` lists source purchase orders and merge links (`purchase_mrp/models/mrp_production.py:40-52`) |
| Procurement reaching a kit product | `mrp` | `run` on a kit is replaced by procurements of its components (`mrp/models/stock_rule.py:40-71`) |
| Subcontracting | `mrp_subcontracting` (and its `_account`, `_purchase`, `_dropshipping`, `_landed_costs`, `_repair` companions) | `mrp` only offers the settings toggle and a lead-time hint (`mrp/models/res_config_settings.py:16`, `mrp/models/mrp_bom.py:91`); subcontract MOs hide from resupply pickings (`mrp/models/stock_picking.py:159`) |
| Landed costs on MOs | `mrp_landed_costs` | dependency listing only; details `UNKNOWN — EVIDENCE INSUFFICIENT` (not read) |
| Expired lots blocking mark-done | `mrp_product_expiry` | `mrp_product_expiry/models/mrp_production.py:10-33` |

Rules used to create the MO from procurement (all in `mrp/models/stock_rule.py`):
- BoM chosen: explicit BoM in the request, else the reordering rule's BoM, else first normal BoM matching the operation type, else any normal BoM for the company (`:138-146`). If none exists an MO is still created with the requested quantity and no components (`:101-112`, `:171-198`), and the lead-time computation adds 365 days (`:217-222`).
- An existing draft/confirmed, unplanned, unassigned MO for the same product, BoM, operation type, company and source may absorb the new demand by increasing its quantity, unless batch size is on (`:93-112`, `:148-169`); the MPS origin always creates a new MO (`:90-91`).
- Dates: start = required date minus BoM manufacturing lead time (minus 1 hour if lead time is zero); deadline = requested deadline or start plus lead time (`:171-176`, `:200-205`).
- MOs are created with elevated rights so that customers' sales users need no manufacturing rights (`:120`).

## 5. Configuration and defaults that change outcomes

- Consumption policy on the BoM: default "Allowed with warning" (`mrp/models/mrp_bom.py:70-84`). Effect on close: section 2.3.
- Manufacturing Readiness on the BoM: "all components available" (default) vs "components for 1st operation" (`mrp/models/mrp_bom.py:56-59`, effect `mrp/models/mrp_production.py:678-682`).
- Operation type: backorder policy default "Ask" (`stock/models/stock_picking.py:133-138`); reservation method default "At confirmation" (`stock/models/stock_picking.py:68-72`); "Create New Lots/Serial Numbers for Components" default off (`mrp/models/stock_picking.py:26-30`); auto-print options (`:30-56`).
- Warehouse "Manufacture to resupply" default on; manufacturing steps default 1-step; the pick/store operation types and their sequence codes PC / MO / SFP are created per warehouse (`mrp/models/stock_warehouse.py:12-38`, `:246-262`).
- BoM manufacturing lead time and "days to prepare MO" (default 0) feed planned dates and reordering-rule order dates (`mrp/models/mrp_bom.py:89-94`, `mrp/models/stock_orderpoint.py:134-145`).
- Batch size default 1, off (`mrp/models/mrp_bom.py:96-97`).
- MO lock default: locked unless group "Unlocked by default" (`mrp/models/mrp_production.py:77-78`).
- Serial-tracked products: MO forced to product unit at confirmation (`mrp/models/mrp_production.py:1635-1645`).
- Work-center cost mode per operation: Actual time vs Theoretical time (`mrp/models/mrp_routing.py:60-63`).
- Operation dependencies: when off, work orders follow sequence one after another (`mrp/models/mrp_production.py:1691-1701`).
- Switching off "Work Order Dependencies" clears the flag on all BoMs (`mrp/models/res_config_settings.py:36-37`).
- Kit vs Manufacture type decides whether a product is exploded on transfers (Kit) or produced through an MO (`mrp/models/stock_move.py:374-407`, `mrp/models/stock_rule.py:73-79`, `:256-259` for route validity).
- Reordering rules on a manufactured product default to the Manufacture route when a BoM exists (`mrp/models/stock_orderpoint.py:147-154`); quantity in progress counts draft MOs and confirmed MOs that finish after the horizon (`:173-235`).

## 6. Effective extension path (module names only)

Modules with Python models inheriting `mrp.production`, `mrp.bom`, `mrp.bom.line`, `mrp.workorder`, `mrp.workcenter`, `mrp.unbuild` (from a search of `_inherit` across the addons root):
- `mrp.production`: `mrp_account`, `mrp_product_expiry`, `mrp_repair`, `mrp_subcontracting`, `mrp_subcontracting_account`, `project_mrp`, `project_mrp_account`, `purchase_mrp`, `sale_mrp`.
- `mrp.bom` / `mrp.bom.line`: `mrp_subcontracting`, `project_mrp`, `purchase_mrp`, `sale_mrp`.
- `mrp.workorder`: `mrp_account`, `project_mrp_account`.
- `mrp.workcenter`: `mrp_account`.
- `mrp.unbuild`: `mrp_subcontracting`.
- Modules that depend on `mrp` directly (manifests): `mrp_account`, `purchase_mrp`, `sale_mrp`, `mrp_landed_costs`, `mrp_repair`, `pos_mrp`, `project_mrp`, `mrp_product_expiry`, `mrp_subcontracting`, `test_main_flows`. All except `mrp_subcontracting` are marked auto-install in their manifests (auto-install fires when their other dependencies are present).
- Report extensions: `mrp_account`, `purchase_mrp`, `mrp_subcontracting`, `mrp_subcontracting_purchase`.
- Not in this source tree (no directory): manufacturing quality, PLM and MPS modules (toggles in settings are upgrade prompts).

## 7. UNKNOWN items (do not infer)

- `UNKNOWN — EVIDENCE INSUFFICIENT`: exact cost-accounting outcomes for finished goods when inventory valuation is not automated (belongs to `stock_account`/`mrp_account`; only `mrp_account/models/mrp_production.py:57-95` was read).
- `UNKNOWN — EVIDENCE INSUFFICIENT`: effect of `mrp_repair`, `pos_mrp`, `project_mrp_account`, `mrp_landed_costs` on MO outcomes (files not read).
- `UNKNOWN — EVIDENCE INSUFFICIENT`: behaviour when several backorders of one MO have different BoM revisions (BoM "outdated" flag only shown to users: `mrp/models/mrp_bom.py:487-519`, `mrp/models/mrp_production.py:1215-1223`).
- `UNKNOWN — EVIDENCE INSUFFICIENT`: unbuild of more than produced, see 2.5.
- `UNKNOWN — EVIDENCE INSUFFICIENT`: any hard limit on scrapping or consuming components in another company.
- `UNKNOWN — EVIDENCE INSUFFICIENT`: real-world defaults produced by demo data (`mrp/data/mrp_demo.xml`, not read).
- Blocked consumption is proven as a screen-level block only; whether any external API caller (server actions, portal, barcode) bypasses it is `UNKNOWN — EVIDENCE INSUFFICIENT`.

## Decision-relevant summary
1. MO state is computed from moves and work orders; completion is gated in order: company/serial checks, lot requirement, consumption wizard, backorder policy of the operation type (`mrp/models/mrp_production.py:2341-2390`).
2. "Blocked" consumption is only a UI restriction; the server-side confirm has no permission check (`mrp/wizard/mrp_consumption_warning_views.xml:37-39`, `mrp/wizard/mrp_consumption_warning.py:32-35`).
3. Costing lives in `mrp_account`, MTO/sales/purchase links in `sale_mrp`/`purchase_mrp`, subcontracting in `mrp_subcontracting`; `mrp` itself only exposes hooks (`mrp/models/mrp_production.py:1903-1905`).

