# Source Map (candidate) — `stock_fleet`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `stock_fleet` |
| Display name | Stock Transport |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `880d43016ba8eddc` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/stock_fleet/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock_picking_batch`, `fleet`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: None / Stock Transport: Dispatch Management System
- Inventory of user-facing artifacts (counts): menu items 0, views 13, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `stock.picking.batch`, `stock.warehouse`, `fleet.vehicle.model.category`, `stock.picking.type`, `stock.picking`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.picking.batch`, `stock.warehouse`, `fleet.vehicle.model.category`, `stock.picking.type`, `stock.picking`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 34 of 34 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: stock_fleet ("Stock Transport")
Source revision: 19.0.post20260921 (Odoo 19.0 Community). Pointers `module/path:LINE`; (TEST) = test-derived. This module ships no tests.
Manifest: "Stock Transport: Dispatch Management System"; depends stock_picking_batch + fleet; no `auto_install` (installed on demand); has a post-install hook (stock_fleet/__manifest__.py:5,8,22).

## A. Capabilities
1. Transport/dispatch data on batch transfers: vehicle, vehicle category, driver, dock, capacity usage (weight/volume %), end date (stock_fleet/models/stock_picking_batch.py:11-31,59-73). CONDITIONAL per operation type: block shown only if the batch's operation type has "Dispatch Management" ticked (stock_fleet/views/stock_picking_batch.xml:29-30; field stock_fleet/models/stock_picking.py:9-12).
2. Vehicle categories with maximum weight and volume, displayed with units in the name (stock_fleet/models/fleet_vehicle_model.py:7-31; views stock_fleet/views/fleet_vehicle_model.xml:3-25).
3. Dock locations per operation type (stock_fleet/models/stock_picking.py:13-24; form field shown only with dispatch on and group `stock.group_stock_multi_locations`, stock_fleet/views/stock_picking_type.xml:51,57). Assigning a dock to a batch redirects the transfers' stock moves to/from that dock (stock_fleet/models/stock_picking_batch.py:97-104).
4. Sort transfers of a batch by delivery postal code, using a searchable zip on transfers (stock_fleet/models/stock_picking.py:30-33; stock_fleet/models/stock_picking_batch.py:77-95).
5. Extra batch views (pivot, graph), picking-type kanban menu entries (Manage Batches, Dock Dispatching, Batches by Route, Calendar, Statistics) and batch report showing dock/vehicle/category and sequence (stock_fleet/views/stock_picking_batch.xml:2-22; stock_fleet/views/stock_picking_type.xml:14-36; stock_fleet/report/report_picking_batch.xml:2-24). Some views (gantt, calendar) are referenced by action context; their definitions are outside this module.
6. Default enabling: post-install hook turns dispatch on for receipt and delivery types of every existing warehouse, plus pick (2-step) or pack (3-step) types (stock_fleet/__init__.py:4-12); new warehouses get the same defaults, and the delivery type gets the warehouse output location as a dock for multi-step delivery (stock_fleet/models/stock_warehouse.py:7-23).

## B. Objects and behaviour
- Extends stock.picking.batch (owner stock_picking_batch; states Draft / In progress / Done / Cancelled, computed, stock_picking_batch/models/stock_picking_batch.py:40-45), stock.picking, stock.picking.type, stock.warehouse, fleet.vehicle.model.category. Uses fleet.vehicle (owner fleet).
- Relationships: batch -> vehicle (optional; placeholder "Third Party Provider" for external carriers, stock_fleet/views/stock_picking_batch.xml:32); vehicle category defaults from the vehicle, driver defaults from the vehicle's driver, both editable (stock_fleet/models/stock_picking_batch.py:12-14,24-25,40-43,59-62). Dock domain limited to children of the type's allowed docks (:15-17).
- Dock automation: dock auto-set when all batch transfers share one source location that is an allowed dock; cleared when operation type changes (:45-51). On batch create with a dock, or write of the dock, moves are re-pointed: for internal/receipt types the destination becomes the dock, otherwise the source becomes the dock; removing the dock restores each transfer's own destination for moves outside it (stock_fleet/models/stock_picking_batch.py:79-104; stock_fleet/models/stock_picking.py:46-49). Adding/removing a transfer to/from a batch triggers the same logic (stock_fleet/models/stock_picking.py:35-44).
- Capacity %: estimated shipping weight/volume (from stock_picking_batch, stock_picking_batch/models/stock_picking_batch.py:62-64) divided by the vehicle category's maximum; shown only when a maximum is set (stock_fleet/models/stock_picking_batch.py:64-73; views :34-50). Capacity is displayed, not enforced: no validation or block was found (grep of module models).
- End date defaults to scheduled date + 1 hour and is pushed forward if earlier than scheduled date (:33-38).
- Merging batches carries vehicle and dock into the merged batch (:106-113; base stock_picking_batch/models/stock_picking_batch.py:484-490).
- Lifecycle transitions of batches are not changed by this module.

## C. Validations, automation, security, multi-company
- No constraints, no cron. Automations are the compute/write hooks above.
- No ACL file or record rules in this module (no security folder); access follows stock_picking_batch and fleet (fleet has its own security files: fleet/__manifest__.py:32-33). Dock field and dock listing on batch/list are restricted to group `stock.group_stock_multi_locations` (stock_fleet/views/stock_picking_batch.xml:31,68,91; stock_fleet/views/stock_picking_type.xml:51).
- Multi-company: dock domain requires same warehouse and internal usage (stock_fleet/models/stock_picking.py:14-17); picking-type company checks are owned by stock. Vehicle company scoping is owned by fleet (UNKNOWN — EVIDENCE INSUFFICIENT for record rules in fleet).
- Location form: `usage` becomes read-only when opened from the dock context (stock_fleet/views/stock_location.xml:8-10).

## D. Handoffs
- stock owns moves, locations, picking types, warehouses; stock_picking_batch owns batch object, weights/volumes, sequence; fleet owns vehicles, drivers, categories.
- Inventory effect: changing a dock rewrites move source/destination locations (inventory routing), which can change reservations/putaway paths (owner stock). No accounting or approval handoff; no external integration. Carrier/delivery pricing lives in `delivery`/`delivery_stock_picking_batch` (not analysed).

## E. Configuration that changes outcomes
- Dispatch Management flag and dock list per operation type; warehouse delivery steps (defaults at stock_fleet/models/stock_warehouse.py:8-19); weight/volume unit-of-measure system parameters used for labels (stock_fleet/models/stock_picking_batch.py:53-57; stock_fleet/models/fleet_vehicle_model.py:27-31); multi-location group; vehicle category capacities (demo values: truck 44000 / 32, van 7000 / 15, stock_fleet/data/stock_fleet_demo.xml:8-20).

## F. Effective extension path
- Objects extended here that other Community modules also extend: stock.picking.batch -> delivery_stock_picking_batch, l10n_ro_edi_stock_batch. fleet.vehicle.model.category -> no other Community extender found. stock.picking.type dispatch fields -> no other module found using `dispatch_management`/dock fields.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: gantt/calendar/kanban batch views referenced by the kanban menu (defined outside this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour when a batch mixes operation types or when transfers are already reserved/done before a dock change.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether fleet vehicles are company-restricted.

