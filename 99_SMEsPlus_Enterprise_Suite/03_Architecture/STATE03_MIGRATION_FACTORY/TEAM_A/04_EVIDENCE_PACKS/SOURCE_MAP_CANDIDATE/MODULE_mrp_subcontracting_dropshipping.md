# Source Map (candidate) — `mrp_subcontracting_dropshipping`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_subcontracting_dropshipping` |
| Display name | Dropship and Subcontracting Management |
| Manifest version | 0.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `d03a883da77b8acd` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_subcontracting_dropshipping/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp_subcontracting`, `stock_dropshipping`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / —
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (8): `stock.warehouse`, `stock.replenish.mixin`, `purchase.order`, `stock.move`, `res.company`, `stock.warehouse.orderpoint`, `stock.picking`, `stock.rule`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.warehouse`, `stock.replenish.mixin`, `purchase.order`, `stock.move`, `res.company`, `stock.warehouse.orderpoint`, `stock.picking`, `stock.rule`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 28 of 28 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: mrp_subcontracting_dropshipping

Source revision: 19.0.post20260921 (Odoo 19 Community). Pointers relative to the addons root. `(TEST)` = test-derived. Neutral business language; no code copied.

## 1. Capabilities
- Bridge between subcontracting and dropshipping (`mrp_subcontracting_dropshipping/__manifest__.py:9-11`); depends on `mrp_subcontracting` and `stock_dropshipping` (`:12`); auto-installs (`:18`) - conditional bridge, only useful when both features are enabled.
- Two scenarios: (A) vendor delivers components straight to a subcontractor ("dropship to subcontractor"); (B) a subcontractor ships the finished product straight to the customer ("subcontract + dropship").
- Data on install: per company sequence, "Dropship Subcontractor" operation type and rule, and enabling resupply on all warehouses (`data/mrp_subcontracting_dropshipping_data.xml:5-12`).

## 2. Business objects and lifecycle
- Operation type "Dropship Subcontractor" (vendor location -> company subcontracting location), sequence prefix DSC/, no warehouse, one per company (`models/res_company.py:12-45`); company keeps a pointer to it (`:10`). Buy rule from vendor to subcontracting location on the dropship route (`models/res_company.py:47-70`).
- Warehouse route rule: pull from subcontracting location to production on the dropship route, make-to-order, using the subcontracting operation type (`models/stock_warehouse.py:66-89`); archived/unarchived with the "Resupply Subcontractors" warehouse flag (`:22-51`); route and picking type activated only if an active pull rule exists (`:53-64`).
- Purchase order aimed at a subcontracting location: destination address auto-set to the single subcontractor of that location (`models/purchase.py:11-25`); warning shown on change of operation type (`:27-32`); delivery destination is that partner's subcontractor location (`:34-38`).
- Procurement: if no partner given and the destination is a subcontracting location, the PO partner is the production's subcontractor (`models/stock_rule.py:10-17`); PO reuse is restricted by destination address (`:19-23`). Reorder rules inherit the location's single subcontractor as partner (`models/stock_orderpoint.py:10-14`).
- A picking from vendor into a subcontracting location is flagged as dropship (`models/stock_picking.py:11-14`). Production for a subcontract move tied to a sales line uses the sales order's warehouse (`:16-19`); with no warehouse (customer or subcontracting destination) the first company warehouse's subcontracting type is used (`:21-34`).
- Dropship route is excluded from manual replenishment choices (`models/stock_replenish_mixin.py:10-12`).

## 3. Actions, gating, security
- No new groups, ACLs or record rules (manifest data: sequence/type/rule data and one PO view, `__manifest__.py:13-16`). Portal subcontractor recording during dropship is exercised (TEST `tests/test_purchase_subcontracting.py:423`).
- Company scoping: sequence, picking type and rule are created per company (`models/res_company.py:12-70`); missing ones back-filled for all companies (`:72-93`); creation hooks for new companies (`:95-106`).

## 4. Accounting / inventory / dropship handoffs
- Dropship classification: a move is "dropshipped" also when it goes subcontractor location -> customer, or vendor -> subcontractor location (`models/stock_move.py:14-35`); returns from customer into the subcontractor are dropship returns (`:37-43`) and purchase returns (`:10-12`). Effect: such moves are unvalued in company stock (TEST `tests/test_anglo_saxon_valuation.py:41`: product is valued at fee + component cost as produced, dropship move unvalued, on-hand value stays zero).
- Bill-price revaluation for subcontracted + dropshipped goods: the receipt's bill lookup is delegated to the production's finished move so the fee follows the vendor bill (`models/stock_move.py:45-50`); the fee logic itself belongs to `mrp_subcontracting_purchase` (`mrp_subcontracting_purchase/models/stock_move.py:14-38`) and the fee-on-production to `mrp_subcontracting_account`. (TEST `tests/test_purchase_subcontracting.py:507`: fee 5 + component 2 = 7 at delivery; after a bill at 10 the cost becomes 12.)
- Ownership summary: dropship routing/flagging = this module; fee from bill/PO = `mrp_subcontracting_purchase` and `mrp_subcontracting_account`; component valuation = `stock_account`/`mrp_account`; landed costs = `mrp_subcontracting_landed_costs` (not touched here). Landed cost combined with dropship: UNKNOWN - EVIDENCE INSUFFICIENT.
- Other tests: kit BoM dropship valuation (TEST `tests/test_anglo_saxon_valuation.py:99,194`), single PO for several subcontracted products (TEST `tests/test_purchase_subcontracting.py:476`), shared PO from a sale (TEST `:360`), partner not overwritten (TEST `:328`), sale delivered quantities for kit with dropship (TEST `tests/test_sale_dropshipping.py:19-411`).

## 5. Configuration that changes outcomes
- Warehouse "Resupply Subcontractors" flag controls dropship subcontractor rules and the picking type (`models/stock_warehouse.py:22-64`).
- Subcontractor location must belong to a single partner for auto destination address / reorder partner (`models/purchase.py:22-24`, `models/stock_orderpoint.py:12`).
- PO operation type choice (dropship-to-customer vs dropship-to-subcontractor) changes destination and warning (`models/purchase.py:27-38`).
- Costing method of the finished product (FIFO/average/standard) changes how the bill adjusts value (TEST `tests/test_anglo_saxon_valuation.py:41`, `tests/test_purchase_subcontracting.py:507`).

## 6. Effective extension path
Models extended: `res.company`, `stock.warehouse`, `stock.rule`, `stock.move`, `stock.picking`, `purchase.order`, `stock.warehouse.orderpoint`, `stock.replenish.mixin`. Neighbouring modules: `mrp_subcontracting`, `mrp_subcontracting_purchase`, `mrp_subcontracting_account`, `stock_dropshipping`, `purchase_stock`.

## 7. By-products
No by-product handling in this module. Subcontract BoMs refuse by-product lines (`mrp_subcontracting/models/mrp_bom.py:24-27`). Manual by-products in a dropshipped subcontract flow: UNKNOWN - EVIDENCE INSUFFICIENT.

## 8. UNKNOWN items
- Landed costs applied to dropshipped subcontract receipts: UNKNOWN - EVIDENCE INSUFFICIENT.
- Multi-warehouse selection when a PO to a customer has no warehouse context (first company warehouse used per `models/stock_picking.py:32`): whether that always matches business intent: UNKNOWN - EVIDENCE INSUFFICIENT.
- Multi-company dropship behaviour beyond per-company rule/type creation: UNKNOWN - EVIDENCE INSUFFICIENT.

