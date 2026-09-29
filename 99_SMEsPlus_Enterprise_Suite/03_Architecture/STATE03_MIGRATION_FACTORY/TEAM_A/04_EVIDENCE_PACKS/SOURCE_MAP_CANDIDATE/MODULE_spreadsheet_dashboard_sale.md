# Source Map (candidate) — `spreadsheet_dashboard_sale`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_dashboard_sale` |
| Display name | Spreadsheet dashboard for sales |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `196b3707d5e1ce27` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_dashboard_sale/` |
| auto_install / application | ['sale'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet_dashboard`, `sale`
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 9 of 11 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: spreadsheet_dashboard_sale
Revision 19.0.post20260921 | Dashboard bridge: Spreadsheet Dashboards <-> Sales (sale) | data-only module (no Python models)

## A. Capabilities (core / optional / conditional)
- Delivers two published dashboards, "Sales" and "Product" (spreadsheet_dashboard_sale/data/dashboards.xml:4-13 and 15-24). Depends on spreadsheet_dashboard and sale (spreadsheet_dashboard_sale/__manifest__.py:9).
- Auto-install: when sale is installed (spreadsheet_dashboard_sale/__manifest__.py:13). No settings, models, record rules or access CSV (data list: :10-12).
- Both sit in the Sales dashboard group; Sales at sequence 100, Product at 200; visible only to the sales manager group (spreadsheet_dashboard_sale/data/dashboards.xml:8-10, 19-21). Each has a sample dashboard file for empty-data display (:7, :18).
- Main data model registered for both: sales orders (spreadsheet_dashboard_sale/data/dashboards.xml:6,17).

## B. Business objects and lifecycle
- Read-only reporting on the sales analysis report (line-level, order-based) plus two order lists; no state changes. Report grain: order lines grouped, dated by order date, in company currency (sale/report/sale_report.py:21,132,191).
- "Sales" dashboard: scorecards Quotations, Orders, Revenue, Average Order each compared "since last period" (spreadsheet_dashboard_sale/data/files/sales_dashboard.json:334-404); monthly revenue line chart (json ~419-454); "Top Countries" and "Top Categories" carousels (json:517,578); top-10 lists of quotations and of orders by untaxed amount with customer and salesperson (json lists at :1484+; list names Quotations by Untaxed Amount / Sales Orders by Untaxed Amount).
- Pivots by category, customer, country, product, sales team, salesperson, source, medium (sales_dashboard.json:910+).
- "Product" dashboard: revenue and units bar charts by product, Best Seller and Best Category scorecards, "Best Selling Categories" carousel (spreadsheet_dashboard_sale/data/files/product_dashboard.json, Data sheet :350-357).

## C. Validations, automation, security
- Access: sales manager group only (spreadsheet_dashboard_sale/data/dashboards.xml:10,21). Company scoping follows the sales report's company field and currency table joined per company (sale/report/sale_report.py:137,191); dashboard file adds no explicit company filter: UNKNOWN — EVIDENCE INSUFFICIENT for multi-company toggling behaviour.
- Automation: none.

## D. Handoffs
- sale owns orders and the sales analysis report; sales_team owns teams and manager group; crm.team, utm (source, medium), product.category, res.country supply filters/groupings; spreadsheet_dashboard owns the container and group "Sales".

## E. Measures and revenue basis (business level)
- Revenue basis is the untaxed total of order lines, converted to company currency using each order's currency rate (and the company currency table), quantity in product unit of measure (sale/report/sale_report.py:99-119). It is not invoiced revenue and not margin/cost based; the report also carries an "invoiced" untaxed amount but the dashboards use the untaxed order total (sales_dashboard.json Data sheet :788,796 use price_subtotal).
- Quotations = number of orders in draft plus sent state; Orders = number in confirmed ("sale") state; Revenue = untaxed total of confirmed orders; Average Order = Revenue / Orders (sales_dashboard.json:783-788,B8 formula on Data sheet; pivot domain draft/sent/sale in the "so stats" pivots). Note "Total orders" uses the same confirmed count (json:786-787).
- Leaderboards (category, customer, country, product, team, salesperson, source, medium) exclude draft, sent and cancelled orders and rows with an empty grouping key (sales_dashboard.json pivot domains at :910+). Top-10 order list excludes draft, sent, cancelled; quotation list includes draft and sent only (json lists).
- Time filter "Period" defaults to last 90 days on Sales and last 30 days on Product (sales_dashboard.json:1420-1425; product_dashboard.json filters). "Previous" figures use the preceding equal period (sales_dashboard.json:791-796).
- Other filters: Country, Product, Customer, Category, Sales Team, Salesperson, Source, Medium (sales_dashboard.json:1430-1480); Product dashboard filters: Period, Product, Category.
- Best Seller / Best Category = top row when ranked by untaxed revenue (product_dashboard.json:453-456, 496-499; Data sheet :350-357).

## F. Effective extension path
- sale, sales_team, spreadsheet_dashboard (module names only). Other sale bridges may add pivots via separate dashboards: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- Whether "locked" (done) orders are counted as confirmed: confirmation state used is "sale"; handling of locked flag: UNKNOWN — EVIDENCE INSUFFICIENT.
- Sample-dashboard trigger conditions: UNKNOWN — EVIDENCE INSUFFICIENT (owned by spreadsheet_dashboard).
- Exact ordering/tie-handling of Best Seller: UNKNOWN — EVIDENCE INSUFFICIENT.

