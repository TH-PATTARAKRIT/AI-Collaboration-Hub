# Source Map (candidate) — `mrp_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `mrp_account` |
| Display name | Accounting - MRP |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `22c4678ad509b87d` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/mrp_account/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp`, `stock_account`
- Direct dependents in 300-module list (2): `mrp_subcontracting_account`, `project_mrp_account`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Manufacturing / Analytic accounting in Manufacturing
- Inventory of user-facing artifacts (counts): menu items 0, views 9, window actions 1, server actions 2, reports 1, mail templates 0, scheduled jobs 0, wizards 2, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (2): `mrp.account.wip.accounting.line` (Account move line to be created when posting WIP account move); `mrp.account.wip.accounting` (Wizard to post Manufacturing WIP account move)
- Objects extended from other modules (17): `account.move`, `account.move.line`, `stock.move`, `res.company`, `product.template`, `product.product`, `product.category`, `mrp.production`, `mrp.workorder`, `account.analytic.account`, `account.analytic.line`, `account.analytic.applicability`, `mrp.workcenter`, `analytic.mixin`, `mrp.workcenter.productivity`, `report.mrp.report_mo_overview`, `stock_account.stock.valuation.report`
- Company-dependent settings introduced: 1 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `account.move`, `account.move.line`, `stock.move`, `res.company`, `product.template`, `product.product`, `product.category`, `mrp.production`, `mrp.workorder`, `account.analytic.account`, `account.analytic.line`, `account.analytic.applicability`, `mrp.workcenter`, `analytic.mixin`, `mrp.workcenter.productivity`, `report.mrp.report_mo_overview`, `stock_account.stock.valuation.report`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 6

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 106 of 108 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: mrp_account

- Source revision: `19.0.post20260921` (Odoo 19.0 Community, addons root). All pointers are `module/path:LINE` relative to the addons root. Read-only, neutral business language, no code copied. `(TEST)` = derived from a test, not from production code.
- Manifest: title "Accounting - MRP", summary "Analytic accounting in Manufacturing", depends on `mrp` and `stock_account`, auto-install, post-install hook re-loads the category "Production Account" from the chart template when present (mrp_account/__manifest__.py:5,8,21,41,42; mrp_account/__init__.py:8-16).
- The module has no scheduled jobs, no groups, no record rules of its own (files inspected: mrp_account/security/ir.model.access.csv:1-7; models listed in mrp_account/models/__init__.py:2-9).
- Valuation base (value on stock move, product value history, closing) is documented in the stock_account note; here only manufacturing additions are traced.

## 1. Capabilities (core / optional / conditional)

| Capability | Class | Pointer |
|---|---|---|
| Finished-product and by-product unit cost computed at Done from consumed component values + work-center cost + extra unit cost, less by-product cost share | Conditional on cost method (only FIFO/Average take the computed cost; Standard keeps product cost) | mrp_account/models/mrp_production.py:57-94 |
| Extra unit cost on the manufacturing order (copied to backorders) | Core field, but no visible input found in this module's views | mrp_account/models/mrp_production.py:13,96-99; mrp_account/views/mrp_production_views.xml:28 |
| Value of a Done finished/by-product move taken from the production cost (hook for the value chain) | Core | mrp_account/models/stock_move.py:11-23 |
| Work-center labour expense posted when the order is Done | Conditional: finished product perpetual AND production location has a valuation account AND no time entry already posted | mrp_account/models/mrp_production.py:101-144 |
| Work-center "Expense Account" (fallback product expense account) | Optional config | mrp_account/models/mrp_workcenter.py:12-13; mrp_account/views/mrp_workcenter_views.xml:8-10 |
| WIP accounting wizard (manual WIP entry with automatic reversal) | Optional/manual; needs company WIP accounts | mrp_account/wizard/mrp_wip_accounting.py:38-146; mrp_account/wizard/mrp_wip_accounting.xml:37-44 |
| Compute product cost from Bill of Materials (button on product, list action) | Optional/manual; hidden for perpetual+FIFO, needs a BoM, MRP manager only | mrp_account/models/product.py:28-99; mrp_account/views/product_views.xml:10-19 |
| Kit (phantom BoM) products excluded from stock valuation and from the closing product domain | Core rule | mrp_account/models/product.py:101-112; mrp_account/models/res_company.py:7-8 |
| Kit unit cost = sum of component unit costs per kit (used by sale/POS/scrap flows) | Core helper | mrp_account/models/stock_move.py:33-47 |
| Category "Production Account" (property) and exposure through product accounts | Optional config | mrp_account/models/product.py:10-26,115-122 |
| Cost-of-production block in the Inventory Valuation report | Conditional: only if some production location has a valuation account | mrp_account/report/stock_valuation_report.py:9-47 |
| Manufacturing overview report: unit cost of Done moves from actual move value | Core | mrp_account/report/mrp_report_mo_overview.py:10-14 |
| Analytic lines from components and work centers (manufacturing-order category, plan applicability) | Conditional on analytic distribution set on work center/BoM | mrp_account/models/mrp_workorder.py:10-59; mrp_account/models/analytic_account.py:76-91 |
| Kit-aware invoiced quantities (kit replaced by components) | Core helper | mrp_account/models/account_move.py:51-67 |
| Demo data | Demo only | mrp_account/data/mrp_account_demo.xml (not analysed) |

## 2. Business objects and lifecycle

### 2.1 Manufacturing order completion sequence (where costs are fixed)
1. Consumed component moves are validated first, so each has its own value (mrp/models/mrp_production.py:1907-1917, the raw-move completion is at 1917).
2. Finished-move quantities are distributed, missing work-order durations default to expected duration (mrp/models/mrp_production.py:1925-1947).
3. Cost calculation hook runs (mrp/models/mrp_production.py:1948 -> mrp_account/models/mrp_production.py:57-94).
4. Finished and by-product moves are validated with the computed unit price (mrp/models/mrp_production.py:1949-1951); stock_account values them via the production-cost step of the value chain (stock_account/models/stock_move.py:409-414; mrp_account/models/stock_move.py:11-23).
5. When the order reaches Done, labour is posted (mrp_account/models/mrp_production.py:141-144).
(TEST: total = components + extra cost: mrp_account/tests/test_mrp_account.py:16-49, expected 738.75 in that fixture.)

### 2.2 Finished / by-product cost rule (verified independently)
- Considered only: finished moves of the order's main product that are not Done/cancelled and have positive quantity (mrp_account/models/mrp_production.py:64-66). If none, nothing is computed (line 67).
- Total cost = sum of consumed component move values + work-center cost (sum of each work order's cost) + extra unit cost x produced quantity in product unit (mrp_account/models/mrp_production.py:68-74).
- Work-order cost = hours x hourly cost (order's own rate, else work-center rate); hours are expected duration when cost mode is "estimated" and the order is In Progress/Done, otherwise the summed recorded time intervals (mrp/models/mrp_workorder.py:638-655,900-902) (TEST: mrp_account/tests/test_mrp_account.py:576-588).
- By-products (Not Done, positive qty): each contributes its cost share to a running total (line 81). If the by-product's own cost method is FIFO or Average: unit price = total cost x share% / by-product quantity in its unit; a share of 0 leaves price unset (lines 82-86). Otherwise (Standard): unit price = its own product cost (line 88).
- Main product: if its cost method is FIFO or Average, unit price = total cost x (1 - sum of by-product shares) / quantity (line 93); if Standard, price = its product cost, so work-center and extra costs do NOT enter its inventory value (lines 90-91).
- Consequence: the share is deducted from the main product even when a by-product is Standard-valued at its own cost, so total inventory value created may differ from total cost incurred (mrp_account/models/mrp_production.py:81,88,93) (TEST: mrp_account/tests/test_valuation_operation.py:83-108 asserts prices, main value and the deduction).
- Share ranges: each share must be non-negative; sum must not exceed 100, checked on the BoM (per variant) and again on the order (mrp/models/mrp_bom.py:205-210; mrp/models/mrp_production.py:980-985). Fields: mrp/models/mrp_bom.py:871-874; mrp/models/stock_move.py:56-58.
- Multiple by-product lines with different units are converted to product unit (TEST: mrp_account/tests/test_valuation_operation.py:13-47 shows 1% of 8 units and 12% of 1 dozen).

### 2.3 Labour posting (work-center cost posting)
- Runs only after the order is Done (mrp_account/models/mrp_production.py:141-144).
- Skips when: finished product valuation is not perpetual; production location has no valuation account; any work-order time entry already carries a posted line (prevents duplicates, also on backorders) (mrp_account/models/mrp_production.py:103-108) (TEST: mrp_account/tests/test_mrp_account.py:603-648).
- Amount per work order = its cost rounded to company currency; grouped by the work center's expense account, fallback the finished product's expense account (lines 113-117). Zero total = no entry (lines 119-120).
- Entry: credit each expense account, debit the production location's valuation account for the total; dated today; journal = the finished product's category Stock Journal; ref "<MO> - Labour"; posted immediately; time entries are linked to their line (lines 122-139) (TEST: mrp_account/tests/test_mrp_account.py:333-349,512-544,546-574).
- Standard-cost finished products: labour stays on the production location account after completion (nothing offsets it) - stated by the category account help text (mrp_account/models/product.py:120-122); Average/FIFO: finished-move value includes labour, offsetting the account (TEST: mrp_account/tests/test_mrp_account.py:546-574).

### 2.4 WIP wizard (manual)
- Opened from the Manufacturing Order action menu (binding), restricted to accounting users (mrp_account/wizard/mrp_wip_accounting.xml:37-44).
- Only orders in Confirmed, In Progress or To Close count; draft, cancelled and Done selected orders are ignored; with none left the wizard becomes a "Manual Entry" (mrp_account/wizard/mrp_wip_accounting.py:43-56) (TEST: mrp_account/tests/test_mrp_account.py:360-372,474-482).
- Default journal = company default of the category Stock Journal (may be empty; journal is required) (mrp_account/wizard/mrp_wip_accounting.py:48-51,62).
- Proposed lines: (1) credit "WIP - Component Value" = picked component quantities up to the chosen date x CURRENT product cost (lot cost for lot-valued products), on the default category stock valuation account; (2) credit "WIP - Overhead" = work-order cost up to the chosen date, on company WIP overhead account, fallback category production account; (3) debit "Manufacturing WIP - <orders>" = sum, on company WIP account (lines 76-103). Lines are editable; no line may hold both debit and credit (lines 20-23).
- Posting: total debit must equal total credit; reversal date must be after posting date (default next day); the entry is posted, then automatically reversed and posted at the reversal date, both linked to the orders (lines 105-146; mrp_account/models/account_move.py:11-15). Orders show a WIP entry counter (mrp_account/models/mrp_production.py:15-25,37-55).
- (TEST) Behaviour: six lines per run (3 + reversal), zero amounts when nothing consumed or when the chosen date precedes the work, aggregated over several orders (mrp_account/tests/test_mrp_account.py:360-510).

### 2.5 Compute-cost-from-BoM
- Sum of operation costs + component costs (child BoM recomputed recursively if selected for recompute) x quantities, minus total by-product share, divided by BoM quantity and converted to product unit; if the product is only a by-product of another BoM, cost = total x its share / its quantity (mrp_account/models/product.py:63-99) (TEST: mrp_account/tests/test_mrp_account.py:322-331,351-358).
- Result is written to the product cost, hence creating a cost-history record (stock_account/models/product.py:286-296) - see stock_account note.

## 3. Validations, automation, security, multi-company

- Validations owned elsewhere but affecting this flow: by-product share limits (see 2.2). Local SQL check: a WIP line cannot be both debit and credit (mrp_account/wizard/mrp_wip_accounting.py:20-23); balance and reversal-date checks (lines 122-125).
- Automation: none of its own (no cron); labour and cost calculation are triggered by the order completion sequence.
- Access rows: accounting read-only and accounting invoice groups can READ BoM and BoM lines (so cost documents can be read without manufacturing rights); accounting manager group has read/write/create on the WIP wizard, plus delete on its lines (mrp_account/security/ir.model.access.csv:2-7) (TEST: mrp_account/tests/test_mrp_account.py:51-64,260-263).
- The WIP action itself is offered to the accounting-user group (mrp_account/wizard/mrp_wip_accounting.xml:42) whereas the wizard's access rows name the accounting-manager group. Whether the two groups nest so that the action works for accounting users: UNKNOWN — EVIDENCE INSUFFICIENT.
- Buttons: compute-from-BoM only for manufacturing managers (mrp_account/views/product_views.xml:10,31,53); WIP counter on orders for accounting users (mrp_account/views/mrp_production_views.xml:11-13); WIP counter on entries for manufacturing users (mrp_account/views/account_move_views.xml:8).
- Multi-company: labour and cost are evaluated in the order's company, not the user's current company (mrp_account/models/mrp_production.py:103-104) (TEST: mrp_account/tests/test_valuation_layers.py:365-374 and branch case :406-453). A kit defined in another company does not zero valuation (TEST: mrp_account/tests/test_valuation_layers.py:376-404). Work-center expense account has company check (mrp_account/models/mrp_workcenter.py:12). Wizard uses the CURRENT company's WIP accounts and currency (mrp_account/wizard/mrp_wip_accounting.py:69-70,101,17) - cross-company use is UNKNOWN — EVIDENCE INSUFFICIENT.
- Company-dependent field introduced: category Production Account (mrp_account/models/product.py:118-122).

## 4. Accounting handoffs (trigger, accounts, owner)

| Trigger | Entry | Accounts and their source | Owner | Pointer |
|---|---|---|---|---|
| Component consumption move validated (production location has valuation account, perpetual component) | Credit stock valuation, debit production location account, amount = component move value | Category stock valuation account; production location valuation account | stock_account | stock_account/models/stock_move.py:229-249,659-667 (TEST: mrp_account/tests/test_valuation_layers.py:304-322) |
| Finished/by-product move validated (same condition) | Debit stock valuation, credit production location account, amount = computed value (includes labour for Average/FIFO) | same | stock_account with mrp_account value | as above (TEST: mrp_account/tests/test_mrp_account.py:520-544) |
| Order Done | Labour entry: credit work-center/product expense, debit production location account | Work-center expense account or product expense; production location account; category stock journal | mrp_account | mrp_account/models/mrp_production.py:101-144 |
| Manual WIP wizard | WIP entry + dated reversal | Category default stock valuation, company WIP overhead, company WIP | Accounting user | mrp_account/wizard/mrp_wip_accounting.py:76-146 |
| Compute cost from BoM | No journal entry; cost-history record only | - | Manufacturing manager | mrp_account/models/product.py:51-61 |
| Closing / valuation report | Cost-of-production block and location reclassification for periodic products | Production location account vs stock valuation account | stock_account | mrp_account/report/stock_valuation_report.py:13-41; stock_account/models/res_company.py:180-236 |

- The category "Production Account" is exposed as the product's production account but, in the scanned Community code, its only consumer is the WIP wizard overhead fallback (mrp_account/wizard/mrp_wip_accounting.py:74). Move-level and labour entries use the PRODUCTION LOCATION's valuation account, not the category account (stock_account/models/stock_move.py:230-235; mrp_account/models/mrp_production.py:103,123). Chart templates set the category account for several localizations (e.g. l10n_au/models/template_au.py:14; l10n_kr/models/template_kr.py:16); only l10n_ec_stock was found setting a location account (l10n_ec_stock/models/account_chart_template.py:28-34). In a default install without a location account, no production entries and no labour posting occur.
- Subcontracting hook: for subcontract receipts, the journal amount is reduced by the extra unit cost when the product is not Standard-valued (mrp_subcontracting_account/models/stock_move.py:9-17).
- Kit sale/POS: sale/POS COGS uses component costs per kit (sale_mrp/models/stock_move.py:25-69; pos_mrp/models/stock_move.py:9-16).

## 5. Configuration and defaults that change outcomes

- Company: Production WIP Account, Production WIP Overhead Account (fields live in stock_account: stock_account/models/res_company.py:16-17; loaded from chart templates: stock_account/models/account_chart_template.py:11-25).
- Category: Production Account; cost method (decides whether labour/extra cost reach product value); valuation mode (decides whether labour is posted).
- Production location: valuation account ("Cost of Production") - gate for every production journal entry (stock_account/views/stock_location_views.xml:11-15).
- Work center: hourly cost, analytic distribution, expense account (mrp_account/models/mrp_workcenter.py:9-13).
- Operation cost mode "estimated" vs actual (mrp/models/mrp_workorder.py:900-902).
- BoM: by-product cost share; kit type (excluded from valuation).
- Order: extra unit cost (no visible input in this module; set by other flows, e.g. mrp_subcontracting_account/models/mrp_production.py:19-21). UI for manual entry: UNKNOWN — EVIDENCE INSUFFICIENT.

## 6. Effective extension path (module names only)

- Depend on mrp_account: mrp_subcontracting_account (journal amount, extra cost from receipts/bills), project_mrp_account, project_mrp_stock_landed_costs (manifests).
- Modules hooking the same valuation points: stock_account (base chain), mrp (order completion sequence, cost share fields), sale_mrp and pos_mrp (kit cost), mrp_subcontracting_purchase (extra cost from bills), purchase_mrp (kit share on bill value: purchase_mrp/models/stock_move.py:48-51), mrp_landed_costs (landed cost targets finished/by-product moves; see its note).
- res.company / product / stock.move extensions in this module: mrp_account/models/res_company.py:7; mrp_account/models/product.py:7-26,39-112; mrp_account/models/stock_move.py:8-47. No other Community module was found overriding these three methods.

## 7. DISAGREEMENT WITH PRIOR

- Prior text for WIP and by-product cost share was not supplied. Located prior artifact: trace/mrp_subcontracting.md:68 cites the cost-share logic at mrp_account/models/mrp_production.py:79-93. My independent range is 76-93 (total cost at 74, by-product loop starts at 80, share addition at 81). Content consistent; no disagreement.
- records/MODULE_mrp_account.md section 5 states no Community extension of this module's objects; manifests show mrp_subcontracting_account, project_mrp_account and project_mrp_stock_landed_costs depend on it. Not contradictory for the objects listed (they extend stock_account's move method, not mrp_account's), but the dependency exists.
- Watch-point: any prior claim that the category "Production Account" receives the production entries would DISAGREE (see section 4, entries use the production location's account).
- Watch-point: any prior claim that work-center cost always enters product cost would DISAGREE for Standard-cost finished products (mrp_account/models/mrp_production.py:90-91).

## 8. UNKNOWN items

- Effective access of accounting-user versus accounting-manager to the WIP wizard: UNKNOWN — EVIDENCE INSUFFICIENT.
- UI to enter the order's extra unit cost: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether WIP entries should use FIFO/Average actual cost instead of current product cost: design intent UNKNOWN — EVIDENCE INSUFFICIENT (code uses current product/lot cost: mrp_account/wizard/mrp_wip_accounting.py:81-84).
- Unbuild valuation and scrap of manufactured goods: tests exist (mrp_account/tests/test_mrp_account.py:120-168; mrp_account/tests/test_valuation_layers.py:62-105) but production-side rules were not traced: UNKNOWN — EVIDENCE INSUFFICIENT.
- Behaviour with closed-license or custom manufacturing extensions: UNKNOWN — EVIDENCE INSUFFICIENT.

