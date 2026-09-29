# Source Map (candidate) — `spreadsheet_dashboard_stock_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_dashboard_stock_account` |
| Display name | Spreadsheet dashboard for stock |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6b158db02a4efceb` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_dashboard_stock_account/` |
| auto_install / application | ['stock_account'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet_dashboard`, `stock_account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Dashboard / Spreadsheet
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 10 of 12 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: spreadsheet_dashboard_stock_account
Revision 19.0.post20260921 | Dashboard bridge: Spreadsheet Dashboards <-> Inventory Valuation (stock_account) | data-only module (no Python models)

## A. Capabilities (core / optional / conditional)
- Delivers one published dashboard "Warehouse Metrics" for warehouse stock quantity, reserved share, and inventory value (spreadsheet_dashboard_stock_account/data/dashboards.xml:4-13). Depends on spreadsheet_dashboard and stock_account (spreadsheet_dashboard_stock_account/__manifest__.py:8).
- Auto-install: when stock_account is installed (spreadsheet_dashboard_stock_account/__manifest__.py:13). No settings, no own models, groups or record rules; module loads only the dashboard record (:9-11).
- Placed in the Logistics dashboard group, sequence 300, visible to inventory managers (spreadsheet_dashboard_stock_account/data/dashboards.xml:8-10). A separate sample dashboard file is registered for empty-data display (:7; sample file: spreadsheet_dashboard_stock_account/data/files/warehouse_metrics_sample_dashboard.json).
- Source data model for the dashboard: stock quants (on-hand stock lines) (spreadsheet_dashboard_stock_account/data/dashboards.xml:6).

## B. Business objects and lifecycle
- Read-only: dashboard content is a saved spreadsheet document; every figure is a live query on stock quants (all pivots use model stock.quant: spreadsheet_dashboard_stock_account/data/files/warehouse_metrics_dashboard.json:1102,1169,1243,1279,1320,1353,1396). No lifecycle or state changes.
- Sheets: main "Dashboard", a "Data" KPI sheet, "Stock location Qty", "Stock location Value" (warehouse_metrics_dashboard.json:6,617,666,793).
- Widgets: scorecards for share of reserved stock quantity, share of reserved stock value, lines with negative stock (warehouse_metrics_dashboard.json chart scorecards on the Dashboard sheet); carousels of top locations/products by quantity and by value, each with stacked reserved vs available; ageing charts of stock quantity and stock value by product and quarter of stock-line creation (json:86-87,181,278); a top-10 products with negative stock list (json:636-639; pivot named "Products").
- Drill-through opens the inventory quants action for each pivot (json:1108,1175,1244,1285,1326,1359,1402).

## C. Validations, automation, security
- Population filter: all pivots and ageing charts include only stock in internal locations (json:193,290,1054,1121,1257,1298); reserved-stock views add reserved quantity > 0 (json:1189-1190); negative-stock view adds quantity < 0 (json:1340-1341).
- Dashboard access: inventory manager group only (spreadsheet_dashboard_stock_account/data/dashboards.xml:10). Inventory value field on quants is itself readable only by stock managers (stock_account/models/stock_quant.py:10). Company scoping is inherited from the quant/valuation access: UNKNOWN — EVIDENCE INSUFFICIENT for explicit multi-company handling inside the dashboard file.
- Automation: none in this module.

## D. Handoffs
- stock (owner of quants, locations, warehouses, reserved quantity, drill action stock.dashboard_open_quants); stock_account (owner of the quant value and valuation method); product (categories); spreadsheet_dashboard (dashboard container, groups Logistics).

## E. Configuration / measures and cost basis
- "Total inventory value" = sum of quant value (json:636). Quant value = quant quantity x (product or lot total valuation / product quantity on hand); only for locations flagged as valued (internal or transit with a company), skipping owner-held stock not owned by the company and zero quantities (stock_account/models/stock_quant.py:48-65; stock_account/models/stock_location.py:36-41).
- Valuation basis is therefore the cost-based inventory valuation of stock_account (lot-level when product valuation by lot is on, otherwise product-level), following the company/category cost method setting (stock_account/models/stock_quant.py:17-35, 59-62). Not a sales-price basis.
- "Share of reserved stock qty" = reserved quantity / on-hand quantity (json:637). "Share of reserved stock value" = reserved value / total value, where reserved value = average unit value (rounded to a whole number) x reserved quantity (json:638,642). Available value = total value - reserved value (Stock location Value sheet, json:841-844).
- Count of negative stock = number of product rows with quantity < 0 in internal locations (json:639,1340-1341).
- Filters offered: Warehouse, Location, Product Category (with children), Product, Lot/Serial (json:1414-1452, field mapping json:~1115-1120).
- Ageing metric groups by the quant creation date quarter, not by receipt or expiry date (json:181-186 groupBy create_date:quarter).

## F. Effective extension path
- stock, stock_account, spreadsheet_dashboard (module names only). Sibling dashboards per app follow the same container.

## G. Not verified
- Exact whole-number rounding effect on reserved value (json:642) at low unit costs: UNKNOWN — EVIDENCE INSUFFICIENT.
- Multi-warehouse/multi-company behaviour of the Warehouse filter beyond field mapping: UNKNOWN — EVIDENCE INSUFFICIENT.
- Sample-mode trigger conditions (owned by spreadsheet_dashboard): UNKNOWN — EVIDENCE INSUFFICIENT.

