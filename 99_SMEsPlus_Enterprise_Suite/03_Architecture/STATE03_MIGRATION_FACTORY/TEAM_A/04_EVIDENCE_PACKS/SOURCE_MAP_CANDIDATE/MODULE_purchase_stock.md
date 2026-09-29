# Source Map (candidate) — `purchase_stock`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `purchase_stock` |
| Display name | Purchase Stock |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G03 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `de5da87768887382` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/purchase_stock/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock_account`, `purchase`
- Direct dependents in 300-module list (5): `purchase_mrp`, `purchase_repair`, `purchase_requisition_stock`, `sale_purchase_stock`, `stock_landed_costs`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `l10n_in_purchase_stock`, `test_main_flows`
- Custom / third-party modules that declare a dependency (name — license only) (3): `19_bhpro_master_data` — OPL-1, `bh_purchase_receipt_all` — LGPL-3, `purchase_request` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Purchase / Purchase Orders, Receipts, Vendor Bills for Stock
- Inventory of user-facing artifacts (counts): menu items 0, views 22, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 5, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `vendor.delay.report` (Vendor Delay Report)
- Objects extended from other modules (27): `product.replenish`, `stock.replenishment.info`, `stock.replenishment.option`, `stock.replenish.mixin`, `account.move.line`, `purchase.order.line`, `purchase.order`, `stock.picking`, `stock.warehouse`, `stock.return.picking`, `stock.warehouse.orderpoint`, `stock.lot`, `account.move`, `stock.move`, `stock.reference`, `res.company`, `product.template`, `product.product`, `product.supplierinfo`, `stock.rule`, `stock.route`, `res.config.settings`, `res.partner`, `stock.forecasted_product_product`, `purchase.report` … (+2)
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `product.replenish`, `stock.replenishment.info`, `stock.replenishment.option`, `stock.replenish.mixin`, `account.move.line`, `purchase.order.line`, `purchase.order`, `stock.picking`, `stock.warehouse`, `stock.return.picking`, `stock.warehouse.orderpoint`, `stock.lot`, `account.move`, `stock.move`, `stock.reference`, `res.company`, `product.template`, `product.product`, `product.supplierinfo`, `stock.rule`, `stock.route`, `res.config.settings`, `res.partner`, `stock.forecasted_product_product`, `purchase.report` … (+2)

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 14

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 92 of 94 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note: `purchase_stock`

- Source revision: `19.0.post20260921` (Odoo 19 Community, addons root `odoo/addons`)
- Method: read-only static reading of source + bundled tests. No code copied. No runtime executed.
- Pointer convention: `path:LINE` relative to the addons root. `(TEST)` = derived from a bundled test.
- Companion: `purchase.md` (base PO / bill logic). Skeleton used for orientation only: `sourcemap/purchase_stock.json`.

## 1. Capabilities and classification

| Capability | Class | Pointer |
|---|---|---|
| Module glue between `purchase` and `stock_account` (which brings stock). `auto_install: True`, so it is installed automatically once both dependencies are present | CORE (when stock + purchase co-installed) | purchase_stock/__manifest__.py:10,36 |
| Receipt (incoming picking) generation from a confirmed PO | CORE | purchase_stock/models/purchase_order.py:179-182,377-412 |
| Received quantity driven by validated stock moves (replaces manual entry for goods) | CORE | purchase_stock/models/purchase_order_line.py:37-93 |
| Receipt status and arrival date on PO; late-order filter | CORE | purchase_stock/models/purchase_order.py:55-81,266-270 |
| "Buy" replenishment route and rule per warehouse, creating RFQs from procurements and reordering rules | CORE (route active per warehouse flag `buy_to_resupply`, default True) | purchase_stock/models/stock_rule.py:15-165; purchase_stock/models/stock.py:45-112; purchase_stock/data/purchase_stock_data.xml:9-21 |
| Return-to-vendor and refund handling in received quantity | CORE | purchase_stock/models/purchase_order_line.py:55-93; purchase_stock/models/stock.py:125-137 |
| Anglo-Saxon price-difference journal lines on vendor bill posting | CONDITIONAL: company `anglo_saxon_accounting` on, product cost method = standard | purchase_stock/models/account_invoice.py:12-50,113-117 |
| Stock valuation from posted vendor bills, else from PO price | CORE (used by stock valuation of receipts) | purchase_stock/models/stock_move.py:157-243 |
| Grouping of auto-generated RFQs per vendor policy (`group_rfq`: on order / daily / weekly / always) | CONDITIONAL: per-vendor setting | purchase_stock/models/res_partner.py:21-40; purchase_stock/models/stock_rule.py:358-395 |
| Days to purchase (lead time added to replenishment) | CONDITIONAL: company setting `days_to_purchase` | purchase_stock/models/res_company.py:9-12; purchase_stock/models/stock_rule.py:211-243 |
| Dropshipping | OPTIONAL: `module_stock_dropshipping` setting installs `stock_dropshipping` | purchase_stock/models/res_config_settings.py:10; purchase_stock/views/res_config_settings_views.xml:13-15 |
| Vendor on-time delivery rate, vendor delay report, OTD dashboard tile | CORE reporting | purchase_stock/models/res_partner.py:41-71; purchase_stock/report/vendor_delay_report.py:8-60; purchase_stock/models/purchase_order.py:241-264 |
| Suggested order quantity (vendor-based demand suggestion in catalog/PO) | CONDITIONAL: per-vendor `suggest_*` fields | purchase_stock/models/purchase_order.py:131-177; purchase_stock/models/res_partner.py:18-20; purchase_stock/models/product.py:39-46 |
| Incoterm location copied to bill | CORE | purchase_stock/models/account_invoice.py:129-137; purchase_stock/models/purchase_order.py:289-292 |

## 2. Business objects, relationships, lifecycle

- New PO fields: destination operation type (`picking_type_id`, required, default = company incoming type), receipts (`picking_ids`), `receipt_status`, `effective_date` (arrival), `dest_address_id`, `incoterm_location`, `reference_ids` (purchase_stock/models/purchase_order.py:17-40).
- New line fields: `move_ids` (receipt moves), `move_dest_ids` (downstream demand), `orderpoint_id`, `propagate_cancel`, `location_final_id` (purchase_stock/models/purchase_order_line.py:26-32).
- `stock.move.purchase_line_id` and `created_purchase_line_ids` tie moves to PO lines (purchase_stock/models/stock_move.py:15-19).
- PO state machine is unchanged; behavior is added around transitions:

| PO transition | Added stock behavior | Pointer |
|---|---|---|
| Approve (to purchase) | Receipt(s) created and confirmed after base approval; happens on direct confirm too, since confirm calls approve | purchase_stock/models/purchase_order.py:179-182; purchase/models/purchase_order.py:637 |
| Confirm while `to approve` | No receipt yet (created only at approval) | purchase_stock/models/purchase_order.py:179-182 |
| Cancel | Non-done moves and open receipts are cancelled; done receipts get a note; downstream moves either cancelled (propagate on) or switched to make-to-stock and recomputed; then base cancel checks (lock, active bills) run | purchase_stock/models/purchase_order.py:188-235; purchase/models/purchase_order.py:641-649 |
| Line qty increased on confirmed PO | Extra move added to open receipt (or a new receipt created if none open and qty > received) | purchase_stock/models/purchase_order_line.py:101-122,169-204 |
| Line qty decreased on confirmed PO | Chatter/activity warning on impacted receipts | purchase_stock/models/purchase_order.py:94-107,298-325 |
| Line price/qty/UoM change | Open moves get new unit price; valued moves are re-valued | purchase_stock/models/purchase_order_line.py:112-122 |
| Line date planned change | Open move deadlines updated | purchase_stock/models/purchase_order_line.py:101-103,157-166 |
| Line delete | Moves cancelled; downstream moves cancelled or reset to make-to-stock according to propagate flag | purchase_stock/models/purchase_order_line.py:139-155 |
| Receipt validated (picking done) | PO auto-acknowledged (vendor-acknowledgement flag set) | purchase_stock/models/stock.py:40-42 |

- Receipt status (computed): none/False if no receipts or all cancelled; `full` if all done or cancelled; `partial` if some done; else `pending` (purchase_stock/models/purchase_order.py:69-79).
- Arrival date = earliest done date among done receipts not going to a vendor location (purchase_stock/models/purchase_order.py:55-58).
- A receipt is created only if at least one line product is of goods type (`consu`) (purchase_stock/models/purchase_order.py:379-381); service-only orders create none.
- Receiving a product on a receipt linked to a PO with no matching line adds a new zero-qty PO line carrying the received qty (unit price zero for "bill on ordered" products) (purchase_stock/models/stock_move.py:61-96).
- Returns: return moves to vendor subtract from received qty (only if refund is requested, or if not linked to an origin move); return of a return does not double count; dropship-return edge case ignored (purchase_stock/models/purchase_order_line.py:55-93).

## 3. Actions, constraints, automation, security

Gates and validations
- Receipt creation requires the vendor to have a vendor location set, else user error (purchase_stock/models/purchase_order.py:360-364).
- Reordering-rule warehouse must be consistent with the PO operation type else user error (purchase_stock/models/purchase_order_line.py:277-281).
- Destination: dropship operation type with a delivery address -> customer location of that address; otherwise operation type's default destination; final location resolved from warehouse stock (purchase_stock/models/purchase_order.py:327-343).
- Operation-type default per company: incoming type of company warehouse, fallback to warehouse-less incoming type (purchase_stock/models/purchase_order.py:346-352; onchange 83-88).
- Merge RFQs additionally requires same operation type (purchase_stock/models/purchase_order.py:184-186).
- Buy rule and route hidden for products without vendors (`_filter_warehouse_routes`, `_is_valid_resupply_route_for_product`) (purchase_stock/models/stock_rule.py:167-172,405-411).
- Warning shown if a product with the Buy route is flagged not purchasable (purchase_stock/models/product.py:16-30).
- Double validation scenario (TEST): with two-step on, purchase user's confirm yields `to approve`; after manager approval state is `purchase` (purchase_stock/tests/test_create_picking.py:96-112).

Procurement to RFQ ("Buy" rule) (purchase_stock/models/stock_rule.py:59-165)
- Vendor chosen from explicit supplier info, or the reordering rule's vendor, else product vendor selection by qty/date/UoM; fallback to first company-compatible vendor (stock_rule.py:174-206).
- If no vendor: from reordering rules -> error listing the product; otherwise chained demand is cancelled or set to make-to-stock and responsible people notified (hook implemented by `sale_purchase_stock`, `purchase_mrp`) (stock_rule.py:70-80,208-209).
- Existing draft RFQ reused when same vendor, operation type, company, buyer, currency (+ reference or date bucket by vendor grouping policy); else new RFQ created as superuser with vendor defaults (payment term, fiscal position, currency, buyer) (stock_rule.py:358-395,326-356,113-115).
- Order line merge candidates depend on propagate-cancel flag, reordering rule, description variants, UoM (purchase_stock/models/purchase_order_line.py:372-410).
- Lead time: vendor delay + company `days_to_purchase`; missing vendor adds 365 days (stock_rule.py:211-243).

Automation
- Reminder cron of `purchase` is narrowed: no reminders for POs with a validated receipt (arrival date set) (purchase_stock/models/purchase_order.py:440-443).
- Install hook creates Buy rules for warehouses lacking one (purchase_stock/__init__.py:9-15). Data function recomputes received-qty method on legacy non-confirmed lines (purchase_stock/data/purchase_stock_data.xml:5; purchase_stock/models/purchase_order_line.py:427-430).
- Warehouse rename updates Buy rule name (purchase_stock/models/stock.py:118-121).
- Date-change activity on PO gets receipt information appended (purchase_stock/models/purchase_order.py:414-438).

Security
- ACL: stock users read PO and PO lines; purchase users read locations and warehouses, read/write/create/delete pickings (manager same plus moves delete), read/write/create moves; orderpoint access for purchase roles; vendor-delay report readable by purchase roles (purchase_stock/security/ir.model.access.csv:2-15).
- No record rules defined in this module (no security XML in manifest data list): multi-company scoping relies on `purchase` rules and `stock` rules. Receipts carry the PO company (purchase_stock/models/purchase_order.py:371; purchase_stock/models/purchase_order_line.py:311). Picking created as superuser (purchase_stock/models/purchase_order.py:386).
- Multi-company effect: operation-type domain restricts to warehouses of the PO company (purchase_stock/models/purchase_order.py:24); procurement PO created in the rule/procurement company (purchase_stock/models/stock_rule.py:113-115).

## 4. Handoffs (with owning module)

| Handoff | Owner | Pointer |
|---|---|---|
| PO approval -> receipt creation and reservation | `purchase_stock` (uses `stock` pickings/moves) | purchase_stock/models/purchase_order.py:179-182,377-412 |
| Validated receipt -> received qty on PO line -> qty to invoice (when bill policy = received) | qty compute in `purchase_stock`; qty-to-invoice and bill status in `purchase` | purchase_stock/models/purchase_order_line.py:55-93; purchase/models/purchase_order_line.py:176-182 |
| Bill control policy ("ordered" vs "received") | `purchase` (product field) | purchase/models/product.py:14-30 |
| Vendor bill posting -> price-difference lines (standard cost, Anglo-Saxon) | `purchase_stock` adds lines on `account.move` posting; posting owned by `account` | purchase_stock/models/account_invoice.py:113-117,12-108 |
| Bill line -> stock moves link used by stock valuation and bill/receipt cross-reference | `purchase_stock` | purchase_stock/models/account_move_line.py:32-33; purchase_stock/models/account_invoice.py:119-127 |
| Stock valuation of receipt (bill value if posted, else quotation price incl. discount/tax/currency) | `purchase_stock` implements hooks called by `stock_account` | purchase_stock/models/stock_move.py:157-243; purchase_stock/models/purchase_order_line.py:239-262 |
| Re-valuation when price/qty/UoM edited | `purchase_stock` triggers `stock_account` valuation update | purchase_stock/models/purchase_order_line.py:120-122 |
| Goods-received-not-invoiced figure | deprecated helper (marked TODO remove) in `purchase_stock` | purchase_stock/report/stock_valuation_report.py:6-30 |
| Landed cost line marking on bill lines | `stock_landed_costs` (extends `_prepare_account_move_line`) | stock_landed_costs/models/purchase.py:5-11 |
| Bill line balance prefilled for accounting | `purchase_stock` | purchase_stock/models/purchase_order_line.py:316-330 |
| Procurement -> RFQ (MTO, reordering, resupply) | `purchase_stock` rule action `buy` on `stock` engine | purchase_stock/models/stock_rule.py:59-165 |
| Sales-driven procurement notifications, dropship, subcontract, MRP demand | `sale_purchase_stock`, `stock_dropshipping`, `purchase_mrp`, `mrp_subcontracting_*` (extend `stock.rule`/PO) | see section 6 |
| Audit trail | chatter notes on PO (qty edits, extra lines, receipt origin link, cancel of done receipt) | purchase_stock/models/purchase_order.py:188-200,298-325; purchase_stock/models/purchase_order.py:404-411 |
| Approval / event | no approval logic in this module; approval owned by `purchase` | purchase/models/purchase_order.py:1251-1259 |

## 5. Configuration and computed behavior that changes outcomes

- Warehouse: `buy_to_resupply` toggles the Buy route/rule (active flag); Buy rule's cancel propagation depends on reception steps (one step -> no propagate) (purchase_stock/models/stock.py:45-98).
- Company `days_to_purchase`: extends lead time for orderpoints and replenishment (purchase_stock/models/res_company.py:9-12; purchase_stock/models/stock.py:180-190).
- Product: type goods (`consu`) triggers receipts and stock-move based received qty; services stay manual; bill policy from `purchase` decides billing basis (purchase_stock/models/purchase_order_line.py:37-40,206-209).
- Product cost method + company Anglo-Saxon flag decide whether bill posting yields price-difference lines (purchase_stock/models/account_invoice.py:37,44).
- Vendor: `group_rfq` and `group_on` grouping; `suggest_*` parameters; `on_time_rate` uses lookback from parameter `purchase_stock.on_time_delivery_days` (default 365) (purchase_stock/models/res_partner.py:16-71).
- Line price for stock move: discounted price, tax-excluded (where tax not included in cost), UoM to product UoM, converted to company currency at move date (purchase_stock/models/purchase_order_line.py:239-262).
- Locations from partner: vendor location `property_stock_supplier` required (purchase_stock/models/purchase_order.py:360-364).

## 6. Effective extension path (module names only)

- `purchase.order`: purchase_stock plus (in addition to base extenders) purchase_requisition_stock, stock_dropshipping, mrp_subcontracting_dropshipping, mrp_subcontracting_purchase, sale_purchase_stock, purchase_mrp, purchase_repair (to be confirmed per module for each override; only `_inherit` presence verified).
- `purchase.order.line`: purchase_stock, purchase_requisition_stock, stock_dropshipping, sale_purchase_stock, purchase_mrp, stock_landed_costs.
- `stock.rule`: purchase_stock, purchase_requisition_stock, stock_dropshipping, mrp_subcontracting_purchase, mrp_subcontracting_dropshipping, project_purchase_stock, purchase_mrp, sale_purchase_stock.
- `purchase.report`: purchase_stock. `stock.picking.type`: stock_dropshipping.
- Manifests that depend on `purchase_stock`: l10n_in_purchase_stock, test_main_flows, purchase_requisition_stock, stock_dropshipping (via sale_purchase_stock), purchase_repair, purchase_mrp, sale_purchase_stock, stock_landed_costs.

## 7. UNKNOWN items

- UNKNOWN — EVIDENCE INSUFFICIENT: full override behavior of each downstream module on `_run_buy`/PO methods (only `_inherit` presence verified, not bodies).
- UNKNOWN — EVIDENCE INSUFFICIENT: behavior of the stock valuation engine itself (owned by `stock_account`, not read here); only the hooks in `purchase_stock` were traced.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether price-difference lines apply to average-cost / FIFO products (code filters to standard cost only; method reported for FIFO/AVCO in valuation is in `stock_account`).
- UNKNOWN — EVIDENCE INSUFFICIENT: currency/UoM edge behavior of `_get_value_from_account_move` beyond the traced partial-billing logic.
- UNKNOWN — EVIDENCE INSUFFICIENT: interaction of receipt creation with `to approve` orders when approval is granted by a different company user (approval runs per order; company not re-scoped beyond `with_company`).
- Observation: cancel processing in `purchase_stock` cancels moves/receipts before the base checks for lock/active bills run, so a blocked cancel relies on transaction rollback (purchase_stock/models/purchase_order.py:188-235 vs purchase/models/purchase_order.py:641-649). Not verified at runtime.

