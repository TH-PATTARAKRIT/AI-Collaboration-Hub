# Source Map (candidate) — `sale_stock`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_stock` |
| Display name | Sales and Warehouse Management |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `c59149306a5efbf1` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_stock/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale`, `stock_account`
- Direct dependents in 300-module list (8): `repair`, `sale_gelato_stock`, `sale_mrp`, `sale_project_stock`, `sale_purchase_stock`, `sale_stock_margin`, `sale_stock_product_expiry`, `stock_delivery`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `l10n_in_sale_stock`, `website_sale_stock`
- Custom / third-party modules that declare a dependency (name — license only) (3): `19_bhpro_master_data` — OPL-1, `sale_job_type` — LGPL-3, `courier_type` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Quotation, Sales Orders, Delivery & Invoicing Control
- Inventory of user-facing artifacts (counts): menu items 0, views 14, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 6, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (23): `stock.return.picking`, `stock.return.picking.line`, `stock.rules.report`, `account.accrued.orders.wizard`, `account.move`, `account.move.line`, `sale.order`, `sale.order.line`, `product.template`, `stock.route`, `stock.move`, `stock.move.line`, `stock.rule`, `stock.picking`, `stock.lot`, `stock.reference`, `res.company`, `res.users`, `res.config.settings`, `stock.forecasted_product_product`, `report.stock.report_stock_rule`, `sale.report`, `stock_account.stock.valuation.report`
- Company-dependent settings introduced: 1 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.return.picking`, `stock.return.picking.line`, `stock.rules.report`, `account.accrued.orders.wizard`, `account.move`, `account.move.line`, `sale.order`, `sale.order.line`, `product.template`, `stock.route`, `stock.move`, `stock.move.line`, `stock.rule`, `stock.picking`, `stock.lot`, `stock.reference`, `res.company`, `res.users`, `res.config.settings`, `stock.forecasted_product_product`, `report.stock.report_stock_rule`, `sale.report`, `stock_account.stock.valuation.report`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 2 (of which company-scoped by text 0); access rows 16

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 108 of 110 source pointers resolve to an existing file and in-range line (2 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note — `sale_stock`
Source revision: Odoo Community `19.0.post20260921` (paths relative to addons root). Read-only trace; neutral business language; no code copied.
Markers: (TEST) = derived from module tests only. `UNKNOWN — EVIDENCE INSUFFICIENT` = not verified.

## 1. Capabilities and classification
- Manifest: "Sales and Warehouse Management"; depends on `sale` and `stock_account`; auto_install true (installs automatically once both dependencies are present); not an application (`sale_stock/__manifest__.py:5,22,46-47`).
- Core (always active once installed): confirming a sales order launches delivery procurement for goods lines; delivered quantity derives from completed stock moves; order shows deliveries, delivery status, effective date, warehouse; invoice/COGS handoff to stock accounting (`sale_stock/models/sale_order.py:213-215`, `sale_stock/models/sale_order_line.py:183-220,385-424`, `sale_stock/models/sale_order.py:83-103`).
- Optional / setting-driven:
  - Shipping policy default (ship as available with backorders vs ship all at once) — company-level default for new orders (`sale_stock/models/res_config_settings.py:15-18`).
  - Sales safety days ("security lead"): toggle plus per-company days; switching the toggle off resets days to 0 (`sale_stock/models/res_config_settings.py:10-23`, `sale_stock/models/res_company.py:10-15`).
  - Incoterm and location on order, copied to invoice (`sale_stock/models/sale_order.py:17-20,298-302`, `sale_stock/models/account_move.py:129-137`).
  - Per-line routes: only routes flagged "selectable on sales order line"; the make-to-order route is flagged by module data (`sale_stock/models/stock.py:10-12`, `sale_stock/data/sale_stock_data.xml:4-6`); the route field on the line is shown only to advanced-location users (`sale_stock/views/sale_order_line_views.xml:46`).
  - Per-user default warehouse (`sale_stock/models/res_users.py:10-19`).
- Conditional (data-dependent): lot/serial numbers printed on invoices for tracked goods (`sale_stock/models/account_move.py:31-114`); Anglo-Saxon COGS behaviour only when stock valuation accounting applies (`sale_stock/models/account_move.py:139-144,157-201`).
- Portal: customers may download delivery slip and return slip PDFs (`sale_stock/controllers/portal.py:23-41`).
- Dead code candidate: `sale_stock/wizard/stock_picking_return.py` (return-line sale-link propagation, picking sale link) is not imported by `sale_stock/wizard/__init__.py:3-5` nor referenced elsewhere in the module; effect of its absence on returns: UNKNOWN — EVIDENCE INSUFFICIENT.

## 2. Business objects, relationships, lifecycle
- Sales order (from `sale`) gains: warehouse, shipping policy, transfers list, delivery status, effective date, late-availability flag, stock references (`sale_stock/models/sale_order.py:17-57`).
- Order line gains: routes, stock moves, warehouse, delivered-quantity method "stock moves", forecast/availability figures, customer lead time (`sale_stock/models/sale_order_line.py:15-30`).
- Stock move gains a link to its order line; transfer (picking) gets a stored link to its sales order derived from its moves; lots list the orders they were delivered against (`sale_stock/models/stock.py:15-17,187-195,327-349`). Stock reference groups sales orders with transfers (`sale_stock/models/stock_reference.py:4-9`).
- Delivery status of order (derived, not settable): none when no or only cancelled transfers; Fully Delivered when all transfers done/cancelled; Partially Delivered when some done and some quantity delivered; Started when some done with no delivered quantity; else Not Delivered (`sale_stock/models/sale_order.py:90-103`). Effective date = earliest completion of a done transfer going to a customer (`sale_stock/models/sale_order.py:83-88`).
- What moves it:
  - Order confirmed -> procurement per goods line -> transfers created and confirmed (`sale_stock/models/sale_order.py:213-215`, `sale_stock/models/sale_order_line.py:385-424`). Goods = product type "consu"; service and combo lines skipped; locked orders skipped (`sale_stock/models/sale_order_line.py:397`).
  - Line quantity raised or line added on a confirmed order -> additional procurement for the difference (`sale_stock/models/sale_order_line.py:248-263,317-327,399-413`). (TEST) editing quantity after full delivery creates a second delivery (`sale_stock/tests/test_sale_stock.py:1178-1202`).
  - Transfer validated -> done moves raise line delivered quantity (outgoing minus returned) (`sale_stock/models/sale_order_line.py:199-220`); a delivery of a product not on the order adds a zero-ordered line with the delivered quantity (`sale_stock/models/stock.py:37-87,237-282`).
  - Order cancelled -> all non-done transfers cancelled, with a note to the responsible users about decreased quantities (`sale_stock/models/sale_order.py:252-267,304-321`). Done transfers are left untouched.
  - Order quantity decreased -> note logged on impacted transfers; cannot go below delivered quantity (`sale_stock/models/sale_order.py:154-197`, `sale_stock/models/sale_order_line.py:426-431`).

## 3. Actions, gates, constraints, automation, security
- Gates:
  - Warehouse required: for a non-draft, non-cancelled order with goods lines and no warehouse, the save is refused ("set a warehouse") when the company has warehouses; a line route from another company needs a warehouse in that company (`sale_stock/models/sale_order.py:130-152`).
  - Ordered quantity cannot be reduced below delivered quantity; returns must be used instead (`sale_stock/models/sale_order_line.py:426-431`).
  - Product on a line cannot be changed when any non-cancelled move exists (`sale_stock/models/sale_order_line.py:265-270`).
  - Delivery address change on the order does not update transfers automatically: onchange warning, and an activity on open transfers (`sale_stock/models/sale_order.py:160-171,234-247`); context switch propagates the new address to transfers (`sale_stock/models/sale_order.py:160-162`).
  - Delivery date (commitment date) change propagates as deadline to open outgoing moves (`sale_stock/models/sale_order.py:173-181`); customer-lead change propagates deadline when no commitment date (`sale_stock/models/sale_order_line.py:278-282`).
  - Shipping policy read-only after quotation stage (`sale_stock/views/sale_order_views.xml:29`); warehouse read-only once confirmed (`sale_stock/views/sale_order_views.xml:26`).
  - Returnability: a transfer tied to a sales order can be returned (`sale_stock/models/stock.py:322-323`).
- Constraints: only the warehouse check above (Python); no SQL constraints in this module (`sale_stock/models/sale_order.py:130`).
- Automation: no crons, no server actions (`sale_stock/__manifest__.py:15-45` lists data files; none define crons). Log notes/activities on quantity exceptions (`sale_stock/models/stock.py:284-320`, `sale_stock/data/mail_templates.xml:4-40`).
- Security (added to the roles from `sales_team`/`stock`):
  - Salesperson: read/write/create transfers and moves; read warehouses, locations, orderpoints, routes, package types; Administrator: full on moves/transfers/routes rules; portal: read transfers (`sale_stock/security/ir.model.access.csv:2-17`).
  - Stock user: read/write orders and lines (no create/delete) and read-all rule on order lines (`sale_stock/security/ir.model.access.csv:5-6`, `sale_stock/security/sale_stock_security.xml:13-22`).
  - Portal record rule: transfers where the customer is the transfer partner or the order's customer (`sale_stock/security/sale_stock_security.xml:6-11`). (TEST) portal access test: `sale_stock/tests/test_sale_stock_access_rights.py:17`.
  - Stock managers get write on partial reconciliation and journal (for valuation postings) (`sale_stock/security/ir.model.access.csv:12-13`).
- Multi-company: warehouse default is resolved per order company (company default, else salesperson's company-specific warehouse, else first warehouse of company) (`sale_stock/models/sale_order.py:222-232`, `stock/models/res_users.py:9-13`; column initialisation `sale_stock/models/sale_order.py:59-81`); user warehouse is company-dependent and company-checked (`sale_stock/models/res_users.py:10`); safety days are per company (`sale_stock/models/res_company.py:10`). (TEST) per-company warehouse resolution (`sale_stock/tests/test_sale_stock_multicompany.py:33-82`); inter-company transfer and delivered-quantity tests exist (`sale_stock/tests/test_sale_stock_multicompany.py:110,180`). Final delivery location may be overridden for inter-company flows (`sale_stock/models/sale_order_line.py:312-315`).

## 4. Cross-module handoffs (owner in brackets)
- Sales -> Inventory [stock owns transfers/moves/rules/reservation]: procurement request per goods line with origin = order name, planned date = promised date minus company safety days, deadline = commitment date or line expected date, warehouse, routes, delivery address, final location = customer location (`sale_stock/models/sale_order_line.py:284-310,379-383`). Procurement run creates moves via pull rules (`sale_stock/models/sale_order_line.py:414-415`); newly created transfers are confirmed immediately (`sale_stock/models/sale_order_line.py:417-424`). Rule-created moves carry the order-line link, partner, sequence, refund flag (`sale_stock/models/stock.py:175-181`).
- Inventory -> Sales: completed moves feed delivered quantity (`sale_stock/models/sale_order_line.py:195-220`); base `sale` then turns delivered quantity into invoiceable quantity for "delivered" policy products (`sale/models/sale_order_line.py:1057-1084`). Trigger point: move completion calls the order-sync hook (`stock/models/stock_move.py:2316-2320`, implemented `sale_stock/models/stock.py:37-87`); a second, similar creation of extra lines also runs on transfer completion (`sale_stock/models/stock.py:237-282`) — interaction of the two: UNKNOWN — EVIDENCE INSUFFICIENT.
- Line invoice status special case: goods with "delivered" policy whose moves are all finished (at least one done) and delivered quantity non-zero become "fully invoiced" even if delivered < ordered (`sale_stock/models/sale_order_line.py:222-246`). (TEST) cancelling deliveries with lock enabled yields "nothing to invoice" (`sale_stock/tests/test_sale_stock.py:1043-1069`).
- Returns [stock]: returned goods reduce delivered quantity only when flagged "to refund" or a return of a customer delivery; drop-ship receipts excluded (`sale_stock/models/sale_order_line.py:199-220,329-371`). Return wizard uses order-line procurement values for re-delivery when a line exists (`sale_stock/wizard/stock_return_picking.py:9-13`). (TEST) returns with/without refund: `sale_stock/tests/test_sale_stock.py:667-737`.
- Sales/Stock -> Accounting [account/stock_account own posting]: invoice inherits incoterm and delivery date (`sale_stock/models/sale_order.py:298-302`, `sale_stock/models/account_move.py:116-127`); customer invoice lines locate the done customer-bound stock moves (and refund equivalents) for cost-of-goods entries (`sale_stock/models/account_move.py:14-29,160-164`); posted COGS quantities/values on previously posted invoices are netted when computing new COGS (`sale_stock/models/account_move.py:170-190`); credit notes without a reversed entry look up COGS lines of the order's invoices (`sale_stock/models/account_move.py:192-201`); down-payment invoices flagged for Anglo-Saxon pricing (`sale_stock/models/account_move.py:139-144`). Stock move -> related posted invoices link (`sale_stock/models/stock.py:95-103`). Re-invoice of costs excluded for COGS and journal-entry lines (`sale_stock/models/account_move.py:166-168`).
- Accruals/reporting [account / stock_account]: accrued-orders wizard uses stock-valuation accounts for storable real-time-valued products (`sale_stock/wizard/accrued_orders.py:6-17`); "goods delivered not invoiced" valuation report override (`sale_stock/report/stock_valuation_report.py:5-8`); sales analysis adds warehouse (`sale_stock/report/sale_report.py:4-19`); forecast report and stock-rule report add sales context (`sale_stock/report/stock_forecasted.py`, `sale_stock/report/report_stock_rule.py`).
- Product master [stock/product]: customer lead time (`sale_delay`) comes from the stock module product (`stock/models/product.py:853-855`); storable goods force re-invoice policy "no" and service tracking "manual" (`sale_stock/models/product_template.py:10-18`).
- Audit/events: notes on order/transfer for quantity decreases, cancellation exceptions, under-delivered quantities; origin link note on newly assigned transfers (`sale_stock/models/sale_order.py:304-321`, `sale_stock/models/stock.py:114-124,284-320`). No approval step in this module.

## 5. Configuration / defaults / computed behaviour that changes outcomes
- Shipping policy on order defaults to "as soon as possible"; setting changes company-wide default (`sale_stock/models/sale_order.py:21-26`, `sale_stock/models/res_config_settings.py:15-18`). Policy drives (a) expected date: earliest lead time for "as soon as possible", latest for "when all ready" (`sale_stock/models/sale_order.py:125-128`), (b) transfer completion policy: transfers tied to orders take "direct" if any linked order is direct, else "one" (`sale_stock/models/stock.py:197-206`). (TEST) policy on picking type does not override the order's policy: `sale_stock/tests/test_sale_stock.py:2159`.
- Line lead time = product's customer lead time; company safety days move procurement date earlier but not the promised deadline (`sale_stock/models/sale_order_line.py:272-276,292-293`).
- Line warehouse = order warehouse unless a selected route has a pull rule sourcing from another warehouse (`sale_stock/models/sale_order_line.py:32-52`); route on line overrides product routes for that line (TEST `sale_stock/tests/test_sale_stock.py:2622`).
- Availability widget: shown for storable goods still to deliver; make-to-order detection depends on route and warehouse (`sale_stock/models/sale_order_line.py:54-65,156-181`).
- Goods that are not storable still trigger delivery (procurement condition is product type only) (`sale_stock/models/sale_order_line.py:397`); expense lines excluded from delivered-quantity via stock (`sale_stock/models/sale_order_line.py:183-193`).
- Locked orders (auto-lock setting in `sale`) skip additional procurement; confirmation launches procurement before auto-lock is applied (`sale_stock/models/sale_order_line.py:397`, `sale/models/sale_order.py:1192-1193`).
- Moves are merged only when they share the same order line (`sale_stock/models/stock.py:89-93`).

## 6. Effective extension path (module names only)
- Extending `sale.order`: sale_stock is itself an extension; other sale.order extenders that sit on stock context: delivery, stock_delivery, stock_dropshipping, repair, sale_mrp, sale_purchase_stock, website_sale_stock, website_sale_collect, pos_sale (from `_inherit` scan of the addons root).
- Extending `sale.order.line` alongside stock: stock_delivery, stock_dropshipping, repair, sale_mrp, sale_project_stock, sale_gelato_stock, sale_stock_margin, sale_stock_product_expiry, website_sale_stock, pos_repair.
- Extending `sale.report`: sale_stock (this module), sale_margin, sale_project, pos_sale, pos_sale_margin, website_sale.
- Direct dependents of `sale_stock` (all auto-install): l10n_in_sale_stock, sale_gelato_stock, sale_mrp, sale_project_stock, sale_purchase_stock, sale_stock_margin, sale_stock_product_expiry, stock_delivery, website_sale_stock; not auto-install: repair (manifest scan).

## 7. UNKNOWN items
- Behaviour when a done delivery exists and the order is then cancelled (no return created; only non-done transfers cancelled): business consequence for invoicing/valuation beyond this code: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether the two "add line for extra delivered product" mechanisms (`sale_stock/models/stock.py:37-87` and `sale_stock/models/stock.py:237-282`) can both fire for the same move: UNKNOWN — EVIDENCE INSUFFICIENT.
- Effect of the unimported return-line/picking file `sale_stock/wizard/stock_picking_return.py`: UNKNOWN — EVIDENCE INSUFFICIENT.
- Internals of the stock procurement/rule engine (route selection, MTO, reservation) and stock valuation postings: owned by `stock` / `stock_account`, not traced here: UNKNOWN — EVIDENCE INSUFFICIENT.
- Accuracy of delivery-status semantics for multi-step (2/3-step) delivery beyond code reading (statuses depend on all linked transfers): UNKNOWN — EVIDENCE INSUFFICIENT.
- Views, delivery-slip and portal templates content: entry points only listed; UNKNOWN — EVIDENCE INSUFFICIENT.

