# Source Map (candidate) — `stock_landed_costs`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `stock_landed_costs` |
| Display name | WMS Landed Costs |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `7fd4bb783d4d145a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/stock_landed_costs/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock_account`, `purchase_stock`
- Direct dependents in 300-module list (3): `mrp_landed_costs`, `mrp_subcontracting_landed_costs`, `project_stock_landed_costs`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Landed Costs
- Inventory of user-facing artifacts (counts): menu items 1, views 4, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (3): `stock.landed.cost` (Stock Landed Cost); `stock.landed.cost.lines` (Stock Landed Cost Line); `stock.valuation.adjustment.lines` (Valuation Adjustment Lines)
- Objects extended from other modules (9): `account.move`, `account.move.line`, `purchase.order.line`, `stock.move`, `res.company`, `product.template`, `res.config.settings`, `mail.thread`, `mail.activity.mixin`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `stock.landed.cost` ← Community: `mrp_landed_costs`, `mrp_subcontracting_landed_costs`; open-license custom/third-party scanned: —
- `stock.valuation.adjustment.lines` ← Community: `project_mrp_stock_landed_costs`, `project_stock_landed_costs`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `account.move`, `account.move.line`, `purchase.order.line`, `stock.move`, `res.company`, `product.template`, `res.config.settings`, `mail.thread`, `mail.activity.mixin`

## 6. Actions / states / validation / automation / security
- State fields found: `stock.landed.cost` → ['draft', 'done', 'cancel']
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 1); access rows 3

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 94 of 94 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: stock_landed_costs

- Source revision: `19.0.post20260921` (Odoo 19.0 Community, addons root). All pointers are `module/path:LINE` relative to the addons root.
- Mode: read-only, neutral business language, no code copied. `(TEST)` = claim derived from a test, not from production code.
- Manifest title "WMS Landed Costs", category Supply Chain/Inventory, depends on stock_account and purchase_stock, not auto-installed, not flagged as an application (stock_landed_costs/__manifest__.py:5,13).

## 1. Capabilities (core / optional / conditional)

| Capability | Class | Pointer |
|---|---|---|
| Landed cost document with cost lines, apportionment and posting | Core of this module | stock_landed_costs/models/stock_landed_cost.py:20-270 |
| Module is switched on by an Inventory setting "Landed Costs" (module install toggle) | Optional (not auto-installed) | stock_account/models/res_config_settings.py:7-8; stock_account/views/res_config_settings_views.xml:11-12 |
| Company default journal for landed cost entries | Optional config, shown only when module is installed | stock_landed_costs/models/res_company.py:10; stock_landed_costs/views/res_config_settings_views.xml:9-17 |
| Create a landed cost from a vendor bill (button on bill) | Conditional: bill must contain lines flagged as landed cost, and no landed cost already linked | stock_landed_costs/models/account_move.py:13-19, 21-40 |
| Per-product "Is a Landed Cost" flag and default split method | Conditional: field only visible on service-type products | stock_landed_costs/models/product.py:12-15; stock_landed_costs/views/product_views.xml:10-11 |
| Flag propagates from purchase order line to bill line | Conditional on product flag | stock_landed_costs/models/purchase.py:7-10 |
| Landed cost value appears in the stock move value (and its description) | Core, automatic once a landed cost is Posted | stock_landed_costs/models/stock_move.py:14-40 |
| Target = manufacturing orders | Not here; added by mrp_landed_costs | mrp_landed_costs/models/stock_landed_cost.py:10-12 |
| Chatter/notification on validation; auto numbering "LC/<year>/nnnn" | Core | stock_landed_costs/models/stock_landed_cost.py:92-95; stock_landed_costs/data/stock_landed_cost_data.xml:5-17 |

Menu: Inventory > Operations/Adjustments > "Landed Costs" (list, form, kanban) (stock_landed_costs/views/stock_landed_cost_views.xml:197-212).

## 2. Business objects and lifecycle

### 2.1 Landed cost document (stock.landed.cost)
- Header data: date (required, default today), target type ("Transfers" only in this module), selected transfers, journal (required), company (required, default current), optional vendor bill link, free description, total amount (sum of cost line amounts, stored) (stock_landed_costs/models/stock_landed_cost.py:31-74).
- States: Draft, Posted (internal value `done`), Cancelled; default Draft, read-only, not copied on duplicate (stock_landed_costs/models/stock_landed_cost.py:54-58).
- Transitions found in this module:
  - Draft -> Posted via Validate (stock_landed_costs/models/stock_landed_cost.py:103-153).
  - Draft -> Cancelled via Cancel; Posted cannot be cancelled (message advises entering a negative landed cost to reverse) (stock_landed_costs/models/stock_landed_cost.py:97-101).
  - Deleting a record first runs cancel, so a Posted record cannot be deleted (stock_landed_costs/models/stock_landed_cost.py:88-90).
  - Validate and Cancel buttons are visible only in Draft (stock_landed_costs/views/stock_landed_cost_views.xml:12-13).
  - Cancelled -> Draft (reopen): no such method in this module. UNKNOWN — EVIDENCE INSUFFICIENT (for other modules).
- Validate requires Draft state and at least one target move (stock_landed_costs/models/stock_landed_cost.py:248-254).
- Duplicating copies the cost lines but not transfers, vendor bill, journal entry or state (stock_landed_costs/models/stock_landed_cost.py:41-46, 58, 62, 67).

### 2.2 Cost line (stock.landed.cost.lines)
- Fields: description, cost product (required), amount (required), split method (required), optional account (stock_landed_costs/models/stock_landed_cost.py:277-293).
- Defaults when the product is picked: description = product name; split method = product default, else previous value, else Equal; amount = product's standard cost; account = product's expense account (stock_landed_costs/models/stock_landed_cost.py:295-301).
- The picker only offers products flagged "Is a Landed Cost" (stock_landed_costs/views/stock_landed_cost_views.xml:46, 61).
- Amount sign is not restricted: negative amounts are accepted and reverse the effect (stock_landed_costs/models/stock_landed_cost.py:282, 383-384; and see 4.1). (TEST) negative cost on an incoming shipment (stock_landed_costs/tests/test_stock_landed_costs_purchase.py:168-).

### 2.3 Valuation adjustment line (stock.valuation.adjustment.lines)
- One line per (eligible stock move x cost line). Holds: cost line, stock move, product, quantity (product UoM), weight, volume, original value, additional landed cost, new value (= original + additional) (stock_landed_costs/models/stock_landed_cost.py:304-343; creation at :194-197).
- Users cannot create these by hand in the form (list has create disabled) but may edit the additional amount (stock_landed_costs/views/stock_landed_cost_views.xml:91-101).
- Original value captured at compute time = the move's current value including earlier Posted landed costs (stock_landed_costs/models/stock_landed_cost.py:169; stock_account/models/stock_move.py:363-441).

### 2.4 Target documents and eligible moves
- Target in this module: transfers (pickings). All moves of the selected transfers are candidates (stock_landed_costs/models/stock_landed_cost.py:245-246).
- Move is skipped if: product cost method is neither FIFO nor Average; move is cancelled; move quantity is zero (stock_landed_costs/models/stock_landed_cost.py:161-162). Standard-cost products are therefore excluded.
- If no move remains, a user error says landed costs apply only to FIFO or average costing (stock_landed_costs/models/stock_landed_cost.py:175-177).
- UI restricts the transfer picker to same-company transfers having moves flagged incoming or outgoing (valued) (stock_landed_costs/views/stock_landed_cost_views.xml:27-29). These flags are true only for done moves (stock_account/models/stock_move.py:72-77). Server code itself has no explicit "transfer must be done" check in this module (stock_landed_costs/models/stock_landed_cost.py:245-254). Behaviour of server-side callers bypassing the UI: UNKNOWN — EVIDENCE INSUFFICIENT.
- Quantity is converted to the product's own UoM (stock_landed_costs/models/stock_landed_cost.py:163). (TEST) different-UoM receipt (stock_landed_costs/tests/test_stockvaluationlayer.py:278-292).

### 2.5 Split methods and apportionment (Compute button / automatic on Validate)
- Methods: Equal, By Quantity, By Current Cost, By Weight, By Volume (stock_landed_costs/models/stock_landed_cost.py:11-17). Help text: :287-291.
- Compute first deletes all existing adjustment lines of the document, then rebuilds (stock_landed_costs/models/stock_landed_cost.py:180-197). Validate auto-computes only when the document has no adjustment lines (:105-107). The Compute button is visible in Draft only (stock_landed_costs/views/stock_landed_cost_views.xml:73); the method itself has no state check (stock_landed_costs/models/stock_landed_cost.py:180-243).
- Basis per method (each cost line is spread independently across the eligible moves):
  - Quantity: move share of total quantity (:213-215). Weight: product weight x quantity (:170, 216-218). Volume: product volume x quantity (:171, 219-221). Current Cost: move's original value share, totals rounded per line (:203-204, 224-226). Equal: cost / number of moves (:222-223).
  - Fallback: if the chosen basis totals zero (e.g. no weight recorded) the cost is spread equally (:227-228). (TEST) expected splits 5 / 50 / 100 / 50 / 200 / 5 / 15 (stock_landed_costs/tests/test_stock_landed_costs_purchase.py:54-118).
- Rounding: each share is rounded half-up to currency precision; any remaining rounding difference for a cost line is added to the adjustment line with the highest id (stock_landed_costs/models/stock_landed_cost.py:230-240). (TEST) cumulative rounding (stock_landed_costs/tests/test_stock_landed_costs_rounding.py:274-).
- Consistency gate at Validate: the sum of shares must equal the document total and each cost line amount; otherwise error "recompute the landed costs" (stock_landed_costs/models/stock_landed_cost.py:108-109, 256-270). Hand-edited adjustment amounts that break the totals block validation.

## 3. Validation, automation, security, company scoping
- Validation errors: non-draft validate (:249-250); no target (:252-254); no eligible FIFO/average move (:175-177); totals mismatch (:108-109); missing expense account for the cost product when no line account (:355-356); cancel of Posted (:98-100). All in stock_landed_costs/models/stock_landed_cost.py.
- Non-real-time products (manual/periodic valuation) are skipped for journal entries only (:123-125); their value still updates (see 4.2). (TEST) no journal entry created (stock_landed_costs/tests/test_stock_landed_costs_purchase.py:119-166).
- Product guard: cannot change a landed-cost service to non-service, or untick the flag, if used on any bill line; otherwise flag is cleared automatically on type change (stock_landed_costs/models/product.py:17-24).
- Bill line flag: bill line flag is set from the product flag on product change, but a user can only tick it when the product is a service (stock_landed_costs/models/account_move.py:66-76). Column shown on vendor bills/receipts, editable for services only (stock_landed_costs/views/account_move_views.xml:25-28).
- Bill to landed cost: only lines flagged; vendor refund gives negative amounts; amount = line subtotal converted with the bill's currency rate and rounded in company currency; split method from product default else Equal; account = product's expense account; document created in the bill's company (stock_landed_costs/models/account_move.py:26-38). Buttons: "Create Landed Costs" for stock managers who also have the invoicing group (stock_landed_costs/views/account_move_views.xml:21). (TEST) refund yields -20 (stock_landed_costs/tests/test_stock_landed_costs_purchase.py:523-589); multi-currency and multi-company bill flows (stock_landed_costs/tests/test_stockvaluationlayer.py:338, 394).
- Automation: no scheduled jobs or server actions in this module (manifest data list, stock_landed_costs/__manifest__.py:16-24).
- Security: only Inventory Administrator group (`stock.group_stock_manager`) has read/write/create/delete on the three models (stock_landed_costs/security/ir.model.access.csv:2-4). No other group grants access in this module.
- Company scoping: one multi-company record rule on the document only (company must be in the user's allowed companies) (stock_landed_costs/security/stock_landed_cost_security.xml:4-8); no rule on cost lines or adjustment lines in this module. Entry is created and validated under the document's company (stock_landed_costs/models/stock_landed_cost.py:112). (TEST) landed cost from a branch company (stock_landed_costs/tests/test_stock_landed_costs_branches.py:26-57).

## 4. Accounting handoffs

### 4.1 Journal entry posted at Validate (owner: stock_landed_costs, using stock_account accounts)
- One general entry per landed cost, in the document's journal, dated the document date, reference = document name (stock_landed_costs/models/stock_landed_cost.py:114-120). Created only if at least one line results; then posted (:146-151).
- Per adjustment line whose product is real-time valued: a debit to the product's stock valuation account and a credit to the cost line's account, else the cost product's expense account (stock_landed_costs/models/stock_landed_cost.py:121-130, 345-358, 385-386).
- Amount = additional landed cost x (quantity still in stock on that move / move quantity). Only the unsold share is capitalised in the entry; if nothing remains, no lines (stock_landed_costs/models/stock_landed_cost.py:372-378). The docstring states the vendor bill only hits the expense/COGS side and this entry moves the remaining-stock share to the valuation account (:368-369). (TEST) 3 of 10 units sold before the cost: 140 of 200 moved to stock valuation (stock_landed_costs/tests/test_stock_landed_costs_purchase.py:694-769).
- Negative cost: debit and credit swap (stock_landed_costs/models/stock_landed_cost.py:381-384).
- Lines carry the product but zero quantity (stock_landed_costs/models/stock_landed_cost.py:360-365).
- No price-difference/variation account is referenced anywhere in this module. Treatment of the sold share beyond the bill's own expense posting: UNKNOWN — EVIDENCE INSUFFICIENT.
- Default journal: company setting, else the stock journal fallback of product categories (stock_landed_costs/models/stock_landed_cost.py:26-29, 63-65).
- Analytic distribution on these lines is added by project_stock_landed_costs and project_mrp_stock_landed_costs (see 6).

### 4.2 Change in value of already-completed stock moves (owner: stock_account, fed by this module)
- This module adds an "extra value" to the move valuation: sum of additional landed cost of all Posted landed costs on that move, optionally only those dated on/before a reference date; description lists each with its vendor bill (stock_landed_costs/models/stock_move.py:7-40). Base hook is empty in stock_account (stock_account/models/stock_move.py:519-520) and is added on top of bill/production/quotation/return/standard-price value (stock_account/models/stock_move.py:363-441).
- Exception: if the move has a manual value adjustment, extra (landed) cost is not added (stock_account/models/stock_move.py:390-395).
- At Validate, after state becomes Posted, the value of every affected move is recomputed (stock_landed_costs/models/stock_landed_cost.py:149-152) through stock_account (stock_account/models/stock_move.py:292-358). This is why no explicit product-cost write remains in the module (the old direct cost update is commented out, stock_landed_costs/models/stock_landed_cost.py:132-142).
- Remaining-stock value of the receipt moves reflects added cost. (TEST) two landed costs on one receipt accumulate 1000 -> 1100 -> 1150, later sale valued 115 (stock_landed_costs/tests/test_stockvaluationlayer.py:266-276).

### 4.3 Effect on product cost by cost method
| Method | Effect | Pointer |
|---|---|---|
| Standard | Excluded from landed-cost apportionment; product cost is not recalculated by stock_account either | stock_landed_costs/models/stock_landed_cost.py:161; stock_account/models/product.py:651-652 |
| FIFO | Receipt move value rises; product cost set to total inventory value / on-hand quantity when quantity > 0 (else last receipt price) | stock_account/models/product.py:677-684 |
| Average | Product cost recomputed by the stock_account average routine; exact formula not traced. UNKNOWN — EVIDENCE INSUFFICIENT | stock_account/models/product.py:686-690 |
(TEST) FIFO: 10@10 and 10@20, landed 100 on first, then one out: value 380 (stock_landed_costs/tests/test_stockvaluationlayer.py:167-175); Average same total 380 (:302-308); receipt fully sold before landed cost leaves value 0 (:188-194, 321-327); single-unit receipt 10 + 5 gives cost 15 (stock_landed_costs/tests/test_stock_landed_costs_branches.py:56-57).
- Owner of cost/valuation fields (cost method, valuation type) is stock_account (stock_account/models/product.py:14, 23).

## 5. Configuration that changes outcomes
- Product: "Is a Landed Cost" (services only in UI) and "Default Split Method" (stock_landed_costs/models/product.py:12-15; stock_landed_costs/views/product_views.xml:10-11). Without a default split, bill-generated lines use Equal (stock_landed_costs/models/account_move.py:36).
- Product category (stock_account): cost method (standard/FIFO/average) decides eligibility; valuation type (real-time vs other) decides whether a journal entry exists (stock_landed_costs/models/stock_landed_cost.py:124, 161).
- Company: default landed cost journal (stock_landed_costs/models/res_company.py:10).
- Per-document: journal, date (date also filters which landed costs count in "as of date" valuation, stock_landed_costs/models/stock_move.py:9-10), account per cost line.
- Product weight and volume drive By Weight / By Volume; missing values cause equal fallback (stock_landed_costs/models/stock_landed_cost.py:170-171, 227-228).

## 6. Effective extension path (modules extending the key models)
- stock.landed.cost: mrp_landed_costs (manufacturing target), mrp_subcontracting_landed_costs (redirects subcontract receipt moves to their source production moves).
- stock.valuation.adjustment.lines: project_stock_landed_costs, project_mrp_stock_landed_costs (analytic distribution on the posted entry lines).
- Both bridge modules are auto-installed when dependencies exist (project_stock_landed_costs/__manifest__.py:8-9; project_mrp_stock_landed_costs/__manifest__.py:8-9; mrp_subcontracting_landed_costs/__manifest__.py:12,17).
- stock.move, account.move, account.move.line, product.template, purchase.order.line, res.company, res.config.settings are extended by stock_landed_costs itself (files under stock_landed_costs/models/). No other Community module extends stock.move._get_value_from_extra (grep of addons root).

## 7. UNKNOWN items
- Reopen of a Cancelled landed cost: UNKNOWN — EVIDENCE INSUFFICIENT.
- Server-side enforcement that target transfers are Done: UNKNOWN — EVIDENCE INSUFFICIENT.
- Exact average-cost formula after landed cost: UNKNOWN — EVIDENCE INSUFFICIENT.
- Accounting for the already-sold share of landed cost beyond the bill's own expense line: UNKNOWN — EVIDENCE INSUFFICIENT.
- Anglo-Saxon vs continental differences: module has no branch on this; UNKNOWN — EVIDENCE INSUFFICIENT.
- Effect of calling Compute on a Posted landed cost (no state guard in method, :180-243): UNKNOWN — EVIDENCE INSUFFICIENT.

