# Source Map (candidate) — `delivery_stock_picking_batch`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `delivery_stock_picking_batch` |
| Display name | Delivery Stock Picking Batch |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `63302f47ed93756b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/delivery_stock_picking_batch/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock_delivery`, `stock_picking_batch`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Batch Transfer, Carrier
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `stock.picking.batch`, `stock.picking.type`, `stock.picking`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.picking.batch`, `stock.picking.type`, `stock.picking`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 26 of 27 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: delivery_stock_picking_batch
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- Adds shipping-carrier awareness to automatic batching of transfers: (1) optionally group automatic batches by carrier; (2) optionally cap the total weight of an automatic batch. delivery_stock_picking_batch/models/stock_picking.py:13-16,23-25
- Conditional on three things: modules stock_delivery and stock_picking_batch both installed (auto-install bridge) delivery_stock_picking_batch/__manifest__.py (depends/auto_install as recorded in skeleton); the operation type has "Automatic Batches" ticked; and the individual options are ticked. delivery_stock_picking_batch/views/stock_picking_type_views.xml:9-19
- The batch feature itself is enabled by an inventory setting (module_stock_picking_batch, "Batch, Wave & Cluster Transfers"); stock_picking_batch depends only on stock and is not auto-installed. stock/models/res_config_settings.py:28; stock_picking_batch/__manifest__.py:12

## B. Business objects and relationships
- Extends the operation type with: group-by-carrier flag, maximum weight (integer, 0 = no limit), and a weight-unit label read from the system weight unit parameter. delivery_stock_picking_batch/models/stock_picking.py:13-21
- Carrier group-by is registered as one more "group by" key, so it counts toward the mandatory choice of at least one grouping when Automatic Batches is on. delivery_stock_picking_batch/models/stock_picking.py:23-25; stock_picking_batch/models/stock_picking.py:79-85
- Candidate selection: when grouping by carrier, only transfers with the same carrier (or both without carrier) are considered, and only batches whose transfers have that carrier. delivery_stock_picking_batch/models/stock_picking.py:31-43
- Batch description: carrier name appended to the auto-generated batch description. delivery_stock_picking_batch/models/stock_picking.py:45-49
- Weight limit: a transfer is auto-batchable only if own weight plus the other transfer's weight does not exceed the type's maximum weight; likewise when merging into an existing batch (sum of batch transfers) and for wave-style line merging (sum of move weights). delivery_stock_picking_batch/models/stock_picking.py:51-59; delivery_stock_picking_batch/models/stock_picking_batch.py:10-24
- Weight is computed and stored by stock_delivery on moves and transfers (excluding cancelled moves). stock_delivery/models/stock_move.py:32-39; stock_delivery/models/stock_picking.py:25,67-70
- (TEST) Carrier set after confirmation still leads two transfers with the same carrier into the same batch in a pick-then-ship setup. delivery_stock_picking_batch/tests/test_delivery_picking_batch.py:78-140 (TEST)
- (TEST) Putting the same product of several transfers of a batch into one package sums the weight (3.0 in the test) and the package weight matches after batch completion. delivery_stock_picking_batch/tests/test_delivery_picking_batch.py:46-76 (TEST)
- Lifecycle of batches (draft/in progress/done etc.) and auto-confirm behaviour are owned by stock_picking_batch. stock_picking_batch/models/stock_picking.py:197-232

## C. Validations / security / multi-company
- No constraint added; inherited constraint requires at least one group-by option when automatic batches are on (the carrier option satisfies it). stock_picking_batch/models/stock_picking.py:79-85
- Security: batch users (inventory user) have full rights on batches; multi-company rule on batches by company. stock_picking_batch/security/ir.model.access.csv:2; stock_picking_batch/security/stock_picking_batch_security.xml (multicompany rule record stock_picking_batch_multicompany_rule)
- Settings fields on the operation type are visible only when Automatic Batches is on. delivery_stock_picking_batch/views/stock_picking_type_views.xml:9,10,17

## D. Handoffs
- Carrier, weight and package weight data [stock_delivery / delivery]. stock_delivery/models/stock_picking.py:21-28
- Batch creation/merge engine [stock_picking_batch]. stock_picking_batch/models/stock_picking.py:197-232
- No accounting, valuation or approval handoff.

## E. Configuration that changes outcomes
- Operation type: Automatic Batches, group-by-carrier, other group-by keys, maximum weight, maximum lines/transfers, auto-confirm. stock_picking_batch/models/stock_picking.py:13-32; delivery_stock_picking_batch/models/stock_picking.py:13-16
- System weight unit parameter (label only shown; unit conversion is not performed in this module). delivery_stock_picking_batch/models/stock_picking.py:19-21
- Product weights determine transfer weight. stock_delivery/models/stock_move.py:34-39

## F. Effective extension path
- stock.picking.batch extended by delivery_stock_picking_batch, l10n_ro_edi_stock_batch, stock_fleet. stock.picking.type extended by delivery_stock_picking_batch among others (l10n_ar_stock, l10n_it_stock_ddt, l10n_tr_nilvera_edispatch, mrp, point_of_sale, project_stock_account, repair, stock_account, stock_dropshipping, stock_fleet, stock_picking_batch). Module names only.

## G. Not verified
- Transfers heavier than the cap on their own (behaviour: they cannot join others; whether they still get their own batch): UNKNOWN — EVIDENCE INSUFFICIENT
- Rounding/unit mismatch between weight cap (integer) and product weight unit: UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour when a carrier is changed after a transfer already sits in a batch: UNKNOWN — EVIDENCE INSUFFICIENT

