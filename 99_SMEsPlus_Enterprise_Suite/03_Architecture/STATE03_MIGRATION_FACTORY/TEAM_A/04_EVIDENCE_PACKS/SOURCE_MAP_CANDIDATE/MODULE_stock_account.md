# Source Map (candidate) — `stock_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `stock_account` |
| Display name | WMS Accounting |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `469205dfa8db47be` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/stock_account/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock`, `account`
- Direct dependents in 300-module list (6): `mrp_account`, `project_stock_account`, `purchase_stock`, `sale_stock`, `spreadsheet_dashboard_stock_account`, `stock_landed_costs`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (6): `l10n_ar_stock`, `l10n_gcc_invoice_stock_account`, `l10n_in_stock`, `l10n_it_stock_ddt`, `l10n_tr_nilvera_edispatch`, `point_of_sale`
- Custom / third-party modules that declare a dependency (name — license only) (2): `19_bhpro_master_data` — OPL-1, `d_tiktok_shop_connector` — OPL-1

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Inventory, Logistic, Valuation, Accounting
- Inventory of user-facing artifacts (counts): menu items 0, views 21, window actions 3, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 3, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `product.value` (Product Value); `stock.avco.report` (Stock AVCO Justifier); `stock_account.stock.valuation.report` (Stock Valuation)
- Objects extended from other modules (21): `stock.return.picking.line`, `stock.inventory.adjustment.name`, `stock.location`, `account.move`, `stock.move.line`, `account.move.line`, `stock.quant`, `stock.picking.type`, `account.account`, `stock.move`, `res.company`, `stock.picking`, `account.chart.template`, `product.template`, `product.product`, `product.category`, `res.config.settings`, `account.analytic.plan`, `account.analytic.account`, `stock.lot`, `stock.forecasted_product_product`
- Company-dependent settings introduced: 7 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `stock_account.stock.valuation.report` ← Community: `mrp_account`, `purchase_stock`, `sale_stock`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `stock.return.picking.line`, `stock.inventory.adjustment.name`, `stock.location`, `account.move`, `stock.move.line`, `account.move.line`, `stock.quant`, `stock.picking.type`, `account.account`, `stock.move`, `res.company`, `stock.picking`, `account.chart.template`, `product.template`, `product.product`, `product.category`, `res.config.settings`, `account.analytic.plan`, `account.analytic.account`, `stock.lot`, `stock.forecasted_product_product`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Stock Account: Inventory Valuation Closing every 1 days
- Security: groups declared 1 (`group_lot_on_invoice`); record rules 2 (of which company-scoped by text 2); access rows 9

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 150 of 151 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: stock_account

- Source revision: `19.0.post20260921` (Odoo 19.0 Community, addons root). All pointers are `module/path:LINE` relative to the addons root. Read-only, neutral business language, no code copied. `(TEST)` = derived from a test, not from production code.
- Manifest: title "WMS Accounting", version 1.1, depends on `stock` and `account`, auto-install, post-install hook runs journal/account setup and seeds initial product cost history (stock_account/__manifest__.py:5,22,46,47; stock_account/__init__.py:10-31,34-86).
- Structural fact for this revision: there is NO stock valuation layer object. Value lives directly on the stock move ("Value"), and cost history lives on a "Product Value" record (stock_account/models/stock_move.py:24-26; stock_account/models/product_value.py:14-37). Remaining quantity/value are computed, not stored (stock_account/models/stock_move.py:44-48, 120-139).

## 1. Capabilities (core / optional / conditional)

| Capability | Class | Pointer |
|---|---|---|
| Cost methods Standard / FIFO / Average (AVCO), chosen per product category, fallback company default | Core; category value overrides company | stock_account/models/product.py:14-22,62-70,741-755; stock_account/models/res_company.py:38-47 |
| Valuation mode Periodic ("at closing") vs Perpetual ("at invoicing"), per category with company fallback | Core; wording of the selection itself says perpetual = at invoicing | stock_account/models/product.py:23-30,72-79,731-740; stock_account/models/res_company.py:29-36 |
| Stock move value set at validation (outgoing at that moment, incoming after transfer done) | Core, automatic | stock_account/models/stock_move.py:177-191,292-358 |
| Incoming value priority: manual adjustment, then posted vendor bills, then production cost, then order (quotation) price, then value of returned original move, then product cost; extra costs added on top unless manually adjusted | Core (chain of hooks; several supplied by other modules) | stock_account/models/stock_move.py:363-448 |
| Lot/serial valuation (per-lot cost) | Optional per product (flag), only for tracked products | stock_account/models/product.py:31-35,54-58; stock_account/views/product_views.xml:49 |
| Product cost history and manual revaluation (product value records; per move, per product, per lot) | Core; access limited to inventory managers | stock_account/models/product_value.py:72-88; stock_account/models/stock_move.py:145-153,164-175; stock_account/security/ir.model.access.csv:4 |
| Inventory Valuation report (opening balance, ending stock, variation, optional inventory-loss block) and "Generate Entry" closing button | Core; PDF/XLSX buttons are stubbed/commented out | stock_account/report/stock_valuation_report.py:28-165; stock_account/static/src/stock_valuation/buttons_bar/buttons_bar.xml:4-17 |
| Closing entry (global variation, location reclassification, continental period variation) | Core; manual button or scheduled | stock_account/models/res_company.py:49-87,119-135,238-320 |
| Scheduled closing per company period (daily/monthly; manual = skipped) | Conditional on company period setting | stock_account/models/res_company.py:19-27,137-150; stock_account/data/stock_account_data.xml:7-18 |
| Cost-of-goods-sold lines added to customer invoices | Conditional: perpetual products only, storable, not dropshipped | stock_account/models/account_move.py:68-161; stock_account/models/account_move_line.py:30-35 |
| Vendor-bill lines default to the stock valuation account for perpetual storable products | Conditional (perpetual) | stock_account/models/account_move_line.py:13-24 |
| Per-move journal entry at transfer validation | Conditional: perpetual product AND source or destination location carries a valuation account (only inventory-loss and production locations expose that field) | stock_account/models/stock_move.py:193-218,659-667; stock_account/views/stock_location_views.xml:11-15 |
| Inventory adjustment with explicit accounting date | Conditional (visible only when a selected product is perpetual) | stock_account/wizard/stock_inventory_adjustment_name.py:7-21; stock_account/models/stock_quant.py:12-16,80-101 |
| Landed costs setting (installs stock_landed_costs) | Optional | stock_account/models/res_config_settings.py:7-8; stock_account/views/res_config_settings_views.xml:11-15 |
| Lot/serial display on invoices | Optional group | stock_account/models/res_config_settings.py:9-10; stock_account/security/stock_account_security.xml:4-6 |
| Average-cost audit report (running cost justification per product) | Core; hidden for standard cost | stock_account/report/stock_avco_audit_report.py:36-134 |
| Analytic lines from stock moves (only when a distribution is supplied by another module) | Conditional; base distribution is empty | stock_account/models/stock_move.py:223-227,255-256,613-657 |
| Block on backdating a validated transfer into a hard-locked fiscal period | Core validation | stock_account/models/stock_picking.py:13-32 |

## 2. Business objects and lifecycle

### 2.1 Stock move value
- Incoming/outgoing status is computed only when the move is Done, from move lines: a line is "in" when source is not a company-valued location and destination is; "out" is the mirror; consigned (owner is not the company) lines are excluded; dropship and returned dropship are tracked separately (stock_account/models/stock_move.py:71-98,525-605; stock_account/models/stock_move_line.py:37-45).
- Valued locations = internal or transit locations that belong to a company (stock_account/models/stock_location.py:36-41).
- On validation, outgoing moves are valued FIRST (before the transfer completes, because the FIFO stack must still be intact); incoming moves and dropships are valued AFTER completion, then per-move journal entries (if eligible) and analytic lines are created (stock_account/models/stock_move.py:177-191).
- Outgoing value: FIFO = consume oldest incoming quantities; Standard and Average = current product cost x quantity; lot-valued = per-lot cost (stock_account/models/stock_move.py:336-351; stock_account/models/product.py:540-581).
- Later edits to quantity, locations, owner or lot on a Done move re-value it (incoming: full recompute; outgoing: proportional correction) (stock_account/models/stock_move_line.py:7-29,47-66).
- A move created already Done is valued at creation (stock_account/models/stock_move.py:155-162) (TEST: stock_account/tests/test_stockvaluation.py:805).
- Value can be manually overridden per move; override suppresses extra costs (landed cost) on that move (stock_account/models/stock_move.py:390-399,145-153) (TEST: stock_account/tests/test_stockvaluation.py:2608-2645).

### 2.2 Cost methods (product cost = the "standard price" field, company-dependent)
- Product cost field is company-dependent (product/models/product_product.py:62-67).
- Standard: value = quantity x current cost; historical value uses the last cost-change record on or before the date (stock_account/models/product.py:393-402,328-357) (TEST: stock_account/tests/test_stockvaluation.py:1914).
- Average: cost recomputed after each incoming move (fast incremental path when no outgoing moves are in the same batch; otherwise full replay of history); replay restarts from the last manual cost record; when stock was zero/negative the last incoming unit price becomes the average (stock_account/models/product.py:636-690,404-524; stock_account/models/stock_move.py:186-189).
- FIFO: no cost written on out; on-hand value = unconsumed slices of the newest incoming moves back-solved from quantity on hand; if more is requested than exists, the last known unit price is extrapolated; product cost is refreshed to total value / quantity (stock_account/models/product.py:540-634,677-684).
- Cost-history records are NOT written for FIFO price changes (stock_account/models/product.py:302-326).
- Changing a category's cost method or moving a product to a category with another method re-derives product cost; no journal entry is made at that instant, the difference surfaces at the next closing (stock_account/models/product.py:81-125,775-787) (TEST: stock_account/tests/test_stockvaluation.py:2647-2695).
- Lot valuation: enabling is refused when valued internal stock exists without lot; every incoming line must then carry a lot (blocking error); lots carry their own company-dependent cost, auto-derived for Average/FIFO (stock_account/models/product.py:91-106; stock_account/models/stock_move.py:315-320; stock_account/models/stock_lot.py:13-19,75-88) (TEST: stock_account/tests/test_lot_valuation.py:132-162,233-239).

### 2.3 Product Value record (cost history / revaluation)
- Fields: product, lot, move, value, company (derived from move, lot or product), date, user, description (stock_account/models/product_value.py:17-37,39-49).
- Meaning of value: unit cost for a product/lot change; total move value for a move adjustment (stock_account/models/product_value.py:7-13).
- Creating one linked to a move re-runs valuation of that move; linked to a lot re-derives product cost (stock_account/models/product_value.py:72-88).
- Product cost edits create such a record automatically (skipped if flag disable_auto_revaluation is passed in context) (stock_account/models/product.py:286-296,302-326).

### 2.4 Closing entry (company level, not a state machine)
- Steps: (a) reclassify value of periodic-product moves that went to/from locations having a valuation account, since last closing; (b) per stock valuation account: physical valuation minus posted accounting balance, booked against the variation account (fallback company expense account); (c) "continental" period variation using the account-level variation/expense pair, only when both are configured (stock_account/models/res_company.py:119-135,180-320).
- Manual run creates the entry in draft and opens it; scheduled run posts it (stock_account/models/res_company.py:49-87,148).
- Guards: cannot date a closing before the last posted closing; error if journal or valuation account missing; "everything is correctly closed" error when nothing to book (stock_account/models/res_company.py:53-67).
- Last ten closing entry identifiers are remembered in system parameters per company (stock_account/models/res_company.py:342-369).
- Closing covers ALL storable products, not only periodic ones (domain = storable) (stock_account/models/res_company.py:152-153,238-272) (TEST: stock_account/tests/test_stockvaluation.py:17-40 - a perpetual standard product still produces a closing entry after a receipt).

## 3. Validations, automation, security, multi-company

- Validation: backdating a Done transfer into a hard-locked fiscal period is refused unless a system parameter skip is set (stock_account/models/stock_picking.py:13-19,27-32) (TEST: stock_account/tests/test_account_move.py:316-378).
- Validation: lot valuation enabling / missing lot on incoming lines (see 2.2). Searching by valuation mode accepts only equality with the two mode values, otherwise an error (stock_account/models/product.py:42-52).
- Automation: one scheduled action "Inventory Valuation Closing", every 1 day, runs as the system user; monthly-period companies close only on the last calendar day; user errors per company are swallowed (skipped) (stock_account/data/stock_account_data.xml:7-18; stock_account/models/res_company.py:137-150) (TEST: stock_account/tests/test_stockvaluation.py:3477-3535, 3602).
- Groups: "Display Serial & Lot Number on Invoices" (stock_account/security/stock_account_security.xml:4-6).
- Record rules (company scoping): Product Value and Stock AVCO report are restricted to allowed companies (stock_account/security/stock_account_security.xml:8-18).
- Access rows: inventory manager reads accounts and journals, full rights on Product Value, read on AVCO report; accounting invoice group read/write/create (no delete) on transfers and stock moves, accounting read-only group read on both (stock_account/security/ir.model.access.csv:2-10).
- Quant "value" and currency are visible only to inventory managers (stock_account/models/stock_quant.py:10-11).
- Closing method itself has no group check inside; who may call it depends on rights to create journal entries. UNKNOWN — EVIDENCE INSUFFICIENT (exact effective group) (TEST: an accounting user can reopen the report after closing: stock_account/tests/test_stockvaluation.py:3326).
- Multi-company: product cost, lot cost, category valuation/cost method/journal/accounts are company-dependent (stock_account/models/product.py:737-766; stock_account/models/stock_lot.py:13-19). Company-wide totals iterate over allowed companies and convert to the selected company's currency (stock_account/models/product.py:201-278). FIFO/average history is searched per company (stock_account/models/product.py:415-419,600-603) (TEST: stock_account/tests/test_stockvaluation.py:3573-3601,3767-3791; stock_account/tests/test_multicompany_lot_valuation.py:41).
- Company-consistency checks are declared on the company accounts and category accounts (stock_account/models/res_company.py:12-17; stock_account/models/product.py:759-766).

## 4. Accounting handoffs (trigger, accounts, owner)

| Trigger | Entry produced | Accounts (source) | Who/what owns it | Pointer |
|---|---|---|---|---|
| Transfer validated, perpetual storable product, one side is a location with valuation account (typically inventory-loss, production) | Move-level entry: debit/credit between product stock valuation account and that location's account, amount = move value | Category stock valuation account (fallback company); location account | stock_account (posted immediately in company stock journal) | stock_account/models/stock_move.py:193-249,659-667; stock_account/models/product.py:130-142 (TEST: stock_account/tests/test_lot_valuation.py:78-101) |
| Receipt of goods from vendor | NO stock-valuation entry at receipt in the default location setup (vendor location has no valuation account field exposed) | - | - | stock_account/views/stock_location_views.xml:11; stock_account/models/stock_move.py:659-667 |
| Vendor bill posted | Bill line already sits on the stock valuation account for perpetual storable products; bill posting then re-values the linked incoming moves from the bill amounts | Stock valuation account | account + purchase_stock (bill), stock_account (re-value) | stock_account/models/account_move_line.py:13-24; stock_account/models/account_move.py:42; purchase_stock/models/stock_move.py:157-215 |
| Vendor bill, standard-cost product, anglo-saxon company | Price-difference lines (bill price vs product cost) | Category price-difference account | purchase_stock | purchase_stock/models/account_invoice.py:12-108; stock_account/models/product.py:158-162 |
| Customer invoice posted | Two extra "cogs" lines: debit expense, credit stock valuation, quantity net of COGS already posted; refund reverses; skipped if dropship | Product expense account (fallback journal default), stock valuation account | account (invoice) with stock_account (amounts) | stock_account/models/account_move.py:68-161; stock_account/models/account_move_line.py:51-95; sale_stock/models/account_move.py:170-190 |
| Invoice set back to draft / cancelled | COGS lines removed | - | stock_account | stock_account/models/account_move.py:46-62 |
| Landed cost validated | Debit stock valuation / credit cost-line (or product expense) account, only for perpetual products and only for the quantity still in stock | see landed cost note | stock_landed_costs | stock_landed_costs/models/stock_landed_cost.py:121-153,345-388 |
| Closing (manual button or daily cron) | Balancing entry(ies): stock valuation account vs variation account, location reclass, period variation | Account-level variation/expense (fallback company expense) | Accounting user (manual) / system (cron) | stock_account/models/res_company.py:119-135,238-340 |
| Inventory adjustment with accounting date | Entry dated at chosen date | as first row | stock_account | stock_account/models/stock_quant.py:80-101 (TEST: stock_account/tests/test_stockvaluation.py:3116-3142) |

- Journal used for move-level entries and closing: company "Stock Journal" (stock_account/models/stock_move.py:209-215; stock_account/models/res_company.py:12,64-65). Category "Stock Journal" is used by other flows (landed cost default, WIP wizard, labour) (stock_account/models/product.py:144-156).
- Partner on move-level entries = accounting partner of the transfer (stock_account/models/stock_move.py:220-221).
- Hook modules (names only): purchase_stock, sale_stock, sale_mrp, mrp_account, stock_landed_costs, mrp_subcontracting_account, mrp_subcontracting_purchase, mrp_subcontracting_dropshipping, purchase_mrp, point_of_sale, pos_mrp.

## 5. Configuration and defaults that change outcomes

- Company fields: Stock Journal, Stock Valuation Account, Production WIP Account, Production WIP Overhead Account, Inventory Period (manual default), Valuation (periodic default), Cost Method (standard default) (stock_account/models/res_company.py:12-47).
- Global defaults on categories: cost method Standard, valuation Periodic (stock_account/data/stock_account_data.xml:4-5). Company values are copied into per-company category defaults when a chart is loaded or the company is set up (stock_account/models/res_company.py:371-377; account/models/company.py:500,763).
- Chart templates (localizations) may preload the company journal/accounts, the variation/expense account pairs, and (WIP accounts for some) (stock_account/models/account_chart_template.py:11-54; l10n_us_account/models/template_us.py:92-93).
- Category: valuation mode, cost method, stock journal, stock valuation account, price-difference account (visible only for Standard + Perpetual), variation account (via valuation account) (stock_account/models/product.py:731-770; stock_account/views/product_views.xml:21-38).
- Location: "Stock Valuation Account" is offered only on inventory-loss ("Loss Account") and production ("Cost of Production") locations (stock_account/views/stock_location_views.xml:11-15). Only one localization module (l10n_ec_stock) was found that sets it automatically (l10n_ec_stock/models/account_chart_template.py:28-34).
- Company anglo-saxon flag gates price-difference lines (purchase_stock/models/account_invoice.py:37).
- UI for the company-level Valuation / Cost Method / Inventory Period fields: none found in stock_account or account views. UNKNOWN — EVIDENCE INSUFFICIENT (where an administrator edits them in the UI).
- Menu entry that opens the Inventory Valuation report: none found in the Community addons. UNKNOWN — EVIDENCE INSUFFICIENT (stock_account/report/stock_valuation_report.xml:3-9 defines the action only).

## 6. Effective extension path (other Community modules; names only)

- Extend stock.move valuation hooks: purchase_stock (bill and order price), stock_landed_costs (extra cost), mrp_account (production cost, kit unit cost, related moves), sale_mrp and pos_mrp (kit price/COGS), mrp_subcontracting_account (journal amount), mrp_subcontracting_purchase and mrp_subcontracting_dropshipping (bill value, dropship detection), purchase_mrp (bill value for kits), sale_stock (related invoices, related moves), point_of_sale (POS COGS, last-step moves). Pointers: purchase_stock/models/stock_move.py:157,229,245; stock_landed_costs/models/stock_move.py:14; mrp_account/models/stock_move.py:11,25,33; sale_mrp/models/stock_move.py:25,31,41; pos_mrp/models/stock_move.py:9; mrp_subcontracting_account/models/stock_move.py:9; mrp_subcontracting_purchase/models/stock_move.py:14; mrp_subcontracting_dropshipping/models/stock_move.py:14,45; purchase_mrp/models/stock_move.py:48 (kit cost share on bill value); sale_stock/models/stock.py:95,126; point_of_sale/models/account_move.py:36,134.
- Extend invoice/COGS hooks: sale_stock, purchase_stock, point_of_sale (last-step stock moves, COGS quantity/value) - sale_stock/models/account_move.py:14,139,170,183; purchase_stock/models/account_invoice.py:119.
- Extend res.company valuation methods: mrp_account only (kits excluded from valuation domain) - mrp_account/models/res_company.py:7-8. No other Community module overrides the closing methods (scan of the addons tree).
- Extend product valuation: mrp_account (kit value forced to zero, category production account) - mrp_account/models/product.py:10-26,101-112.
- Extend the report model: mrp_account (cost of production block); purchase_stock and sale_stock (legacy not-invoiced computations, marked "remove in master", not called by the base report) - mrp_account/report/stock_valuation_report.py:9-47; purchase_stock/report/stock_valuation_report.py:7-8; sale_stock/report/stock_valuation_report.py:7-8.
- Custom/closed-license extensions: UNKNOWN — EVIDENCE INSUFFICIENT.

## 7. DISAGREEMENT WITH PRIOR

- The text of the prior findings on valuation timing was not supplied to this researcher; the only prior artifacts located on disk were the S1 record (records/MODULE_stock_account.md, no behavioural claims) and other trace notes. No direct contradiction can be asserted.
- Reconciliation flag: any prior statement that perpetual valuation posts a stock entry at every receipt/delivery validation DISAGREES with this revision. Evidence: per-move entries require a location valuation account (stock_account/models/stock_move.py:659-667); vendor-side value is booked through the bill (stock_account/models/account_move_line.py:20-24); customer-side through invoice COGS lines (stock_account/models/account_move.py:96-160); wording "at invoicing" (stock_account/models/product.py:26,738-740). Gaps are cleaned up by the closing entry (stock_account/models/res_company.py:238-272).
- Register record lists 1 declarative constraint and 7 company-dependent fields; both agree with this trace (stock_account/models/stock_picking.py:13; count of company-dependent fields at stock_account/models/product.py:37,737,748,756,759,763 and stock_account/models/stock_lot.py:13).

## 8. UNKNOWN items

- Exact effective permission needed to run the closing action: UNKNOWN — EVIDENCE INSUFFICIENT.
- UI location for company-level valuation/cost-method/inventory-period fields: UNKNOWN — EVIDENCE INSUFFICIENT.
- Menu path to the Inventory Valuation report: UNKNOWN — EVIDENCE INSUFFICIENT.
- Which account set a branch company uses at closing: only covered by test names (stock_account/tests/test_stockvaluation.py:3537-3572); rule not traced. UNKNOWN — EVIDENCE INSUFFICIENT.
- Behaviour under closed-license or custom extensions: UNKNOWN — EVIDENCE INSUFFICIENT.
- Performance/volume limits of the average-cost replay (batch size fixed at 50000 moves, memory-driven): stock_account/models/product.py:464 - business impact UNKNOWN — EVIDENCE INSUFFICIENT.

