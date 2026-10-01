# U05 - sales_invoicing_delivery - Restricted Technical Evidence (L2/L3)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Unit: U05 `sales_invoicing_delivery` | Date: 2026-10-02 | Source revision: `19.0.post20260921` (Community only)
> Modules: `sale` (invoicing-related code only), `sale_stock`, `sale_loyalty`, `sale_crm`, `sale_purchase`, `sale_mrp` (light), `sale_timesheet` / `sale_project` (light)
> Read-only on source; restored DB queried for configuration only (no business data). No V-level, coverage %, Gate or Clean-Room statement is made here.

## Scope, method and honest limits
- Capabilities CAP-U05-01 .. CAP-U05-09 studied; every claim below was anchored to a viewed line (see Claims table at the end).
- Hand-offs (not studied): quotation lifecycle/pricing/portal confirmation (U04); transfers engine, backorders, reservation (U08); valuation/COGS (U10); invoice posting/lock/reversal engine (U11).
- Product vocabulary note (Odoo 19): `product.type` = goods (`consu`) / service / combo; "storable" = goods with `is_storable`; sale order states are `draft, sent, sale, cancel` (no `done`); lock is a separate boolean `locked`.

## DISCOVERED SUPPORTING MODULES (read only as far as needed)
`account` (invoice/reversal/tax engine hooks), `stock` (`stock.reference`, backorder, return wizard), `stock_account` (`to_refund` flag), `loyalty` (program/reward model), `delivery` (delivery lines not invoiceable alone), `payment` (transaction post-processing, via `sale/models/payment_transaction.py`), `purchase` (via `sale_purchase`), `project`/`hr_timesheet` (via `sale_project`/`sale_timesheet`), `crm`. Found by grep but NOT read: `sale_purchase_stock`, `sale_purchase_project`, `sale_loyalty_delivery`, `sale_project_stock`, `sale_expense`, localisation overrides `l10n_in_sale`, `l10n_it_edi_sale`, `l10n_it_edi_doi`, `l10n_tw_edi_ecpay_website_sale`, `l10n_ec_sale` (override `_prepare_invoice` / `_create_invoices`).

## Contradictions / corrections with prior evidence
1. Prior `MODULE_sale.md` left "effect for refunds raised directly from an invoice" as UNKNOWN; static chain now resolves it as INFERENCE: reversal copies keep the order-line link, so credit notes DO reduce `qty_invoiced` (VDR-U05-C150); the in-code docstring says otherwise (VDR-U05-C146) - flagged CONTRA.
2. Odoo 19 `sale_stock` has no `procurement.group`; `stock.reference` plays that role (VDR-U05-C191) - flagged CONTRA against generic procurement-group terminology.
3. The UI invoice wizard never exposes `deduct_down_payments`; regular invoices from the UI are always `final=True` (VDR-U05-C038) - prior notes did not state this.
4. DB shows the four sale feature groups (lock, discount, warnings, pro-forma) implied by `base.group_user`, i.e. enabled (VDR-U05-C442) - affects any assumption of default "no lock".

## Runtime/AWT list (RT) - all unresolved items
VDR-U05-C034; VDR-U05-C097; VDR-U05-C141; VDR-U05-C143; VDR-U05-C180; VDR-U05-C239; VDR-U05-C241; VDR-U05-C275; VDR-U05-C341; VDR-U05-C388; VDR-U05-C389; VDR-U05-C445; trigger-while-inactive of the invoice-send cron (VDR-U05-C436).


## CAP-U05-01 Invoicing policy (ordered vs delivered quantities)

**Function-ID(s):** `SDV-F04` (Invoicing policy, C1 - verified in full below). Supporting: `PDT-F01` (see CAP-U05-06).

### D1 - Business purpose and process semantics
Each sellable product carries a two-valued billing basis. For goods it decides whether the order line becomes billable at confirmation (ordered) or only as stock moves complete (delivered). For services Odoo layers a service-policy picker (prepaid/fixed price, manual delivered, milestones, timesheets) that maps onto the two basic values. The value is not snapshotted on the order line: it is read from the product when billable quantity is recomputed (VDR-U05-C008, VDR-U05-C009). Company-level default is only the initial value for new products (VDR-U05-C004, VDR-U05-C031).

### D2 - Architecture / data / object relationships
- `product.template.invoice_policy` (stored selection, tracked) <- default via `res.config.settings.default_invoice_policy` -> `ir.default` (VDR-U05-C001, VDR-U05-C002, VDR-U05-C004).
- `sale.order.line.qty_to_invoice` (stored) = f(state, product policy, qty_ordered, qty_delivered, qty_invoiced) (VDR-U05-C006); `sale.order.line.invoice_status` (stored) = f(state, qty_to_invoice, policy, qty_delivered, qty_invoiced) (VDR-U05-C030); `sale.order.invoice_status` aggregates (CAP-U05-02).
- `qty_delivered` source selected by `qty_delivered_method` (`manual`, `analytic`, `stock_move`, `timesheet`, `milestones`) (VDR-U05-C024, VDR-U05-C025).
- Company `sale_discount_product_id` and loyalty discount products are pinned to policy `order` (VDR-U05-C018, VDR-U05-C019).

### D3 - Source / technical / workflow logic
```
product.invoice_policy -> (read live) -> sale.order.line._compute_qty_to_invoice
   state != sale or display line      -> 0
   combo parent                       -> ordered-invoiced only if some child has qty_to_invoice
   policy == 'order'                  -> product_uom_qty - qty_invoiced
   else (delivery)                    -> qty_delivered - qty_invoiced
-> _compute_invoice_status (line)  -> sale_stock override may flip 'no' -> 'invoiced'
```
State list (line invoice status): `no -> to invoice [qty_to_invoice != 0]`; `to invoice -> invoiced [qty_invoiced >= ordered and qty_to_invoice == 0]`; `* -> upselling [policy order and delivered > ordered and nothing to invoice]`; `invoiced/no -> to invoice [delivered rises (delivery policy) or qty_invoiced falls (refund)]`.
Inheritance chain: `sale` base -> `sale_stock` (`_compute_qty_delivered`, `_compute_invoice_status`) -> `sale_mrp` (kit `_prepare_qty_delivered`) -> `sale_timesheet`/`sale_project` (service methods). Settings: `sale.res.config.settings.set_values` forces `sale.automatic_invoice=False` if default policy != order (VDR-U05-C016).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Set product policy -> confirm order -> `qty_to_invoice` computed per VDR-U05-C006 -> line status `to invoice` (VDR-U05-C030) -> invoice (CAP-U05-02). |
| 2 | Reversal / cancel | Cancelling the order sets lines' `state` to cancel, so `qty_to_invoice`=0 (VDR-U05-C007); credit notes lower `qty_invoiced` and re-open the line (CAP-U05-04). Switching policy later has no automatic back-effect (VDR-U05-C008). |
| 3 | Multi-company | Policy is a plain stored field on `product.template` (company-shared if the product has no company); no per-company value (`company_dependent` absent) (VDR-U05-C002). Default is an `ir.default` which may be company-scoped (DB: none). |
| 4 | Side effects | Drives `sale.order.invoice_status` and upsell activity (CAP-U05-02/06); automatic invoice forced-ordered logic (VDR-U05-C014, VDR-U05-C015); service project/timesheet billing (CAP-U05-08). |
| 5 | Configuration | Product field; company default; service policy mapping (VDR-U05-C020, VDR-U05-C021); automatic invoicing gated by default policy (VDR-U05-C016, VDR-U05-C017). |
| 6 | Validation | Field required on form when sellable and not combo (VDR-U05-C005); discount product domain requires `order` (VDR-U05-C018); no DB constraint. |
| 7 | Roles/permissions | Product edit rights are owned by `product` module (not studied); no sale-specific group on the field (VDR-U05-C005 shows no groups attribute). UNKNOWN beyond view. |
| 8 | Scheduled | None for policy itself. |
| 9 | Exceptions | Nothing billable -> UserError with policy hint (VDR-U05-C023). |
| 10 | Accounting/stock/audit | Policy `delivery` + goods ties invoice quantity to done moves (stock) and COGS (hand-off U10); field tracked (VDR-U05-C002). |

### DB reconciliation (configuration only)
VDR-U05-C031; VDR-U05-C032; VDR-U05-C033. No sale orders exist, so no behavior observation of line status is possible.

### Unknown / Runtime list
- VDR-U05-C034 (RT).
- Whether live recompute of `qty_to_invoice` occurs on stock-move completion for already-invoiced lines depends on ORM dependency evaluation (`qty_delivered` store dependency) - RT.

## CAP-U05-02 Invoice creation from an order (incl. order invoicing status)

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no existing ID names invoice creation from an order). Closest: `SDV-F04`, `PDT-F01`.

### D1 - Business purpose and process semantics
Salespeople or accountants turn the billable part of confirmed orders into draft customer invoices, singly or in bulk. The order exposes a four-value invoicing status used for work lists and upsell alerts. Progressive billing falls out of one rule: quantity already on any non-cancelled invoice line (draft included) is subtracted from what is billable (VDR-U05-C068).

### D2 - Architecture / data / object relationships
- `sale.advance.payment.inv` (transient wizard) -> `sale.order._create_invoices` -> `sale.order._prepare_invoice` + per-line `sale.order.line._prepare_invoice_line` -> `account.move` (+ lines) created in sudo (VDR-U05-C040).
- Link: `sale_order_line_invoice_rel` between `sale.order.line.invoice_lines` and `account.move.line.sale_line_ids` (VDR-U05-C072); `sale.order.invoice_ids` is derived from it and includes credit notes (VDR-U05-C071).
- Order-level status `sale.order.invoice_status` (stored) aggregates `sale.order.line.invoice_status` (VDR-U05-C080).
- Extensions: `sale_stock` (incoterm, delivery date), `sale_timesheet` (timesheet link, period), `sale_project` (analytic distribution in `_prepare_invoice_line`), `delivery`/`sale_loyalty` (`_can_be_invoiced_alone`).

### D3 - Source / technical / workflow logic
```
UI: order form "Create Invoice" / list header -> sale.advance.payment.inv.create_invoices
  method=delivered -> sale.order._create_invoices(final=deduct_down_payments(True), grouped=not consolidated_billing)
     1 access check (VDR-U05-C039)
     2 per order: with_company/lang; _prepare_invoice(); _get_invoiceable_lines(final)
     3 build invoice_line vals (DP section + DP lines at end with qty -1) (VDR-U05-C059)
     4 none -> UserError (unless raise_if_nothing_to_invoice=False) (VDR-U05-C061)
     5 group by (company, partner, partner_shipping, currency, fiscal_position) unless grouped (VDR-U05-C062)
     6 create moves sudo (VDR-U05-C040); if final and amount_total<0 -> switch to out_refund (VDR-U05-C065)
     7 chatter origin note per move (VDR-U05-C067)
```
Order invoice-status machine: `no -> to invoice [any counted line to invoice and not only special lines]`; `to invoice -> invoiced [all counted lines invoiced]`; `invoiced -> upselling [all invoiced or upselling]` etc.; any state `-> no [order not in state sale]` (VDR-U05-C074, VDR-U05-C076, VDR-U05-C077, VDR-U05-C078, VDR-U05-C079).
Override chain for `_create_invoices`: `sale` -> `sale_timesheet` (+ localisation modules l10n_ec_sale, outside scope; DISCOVERED). For `_prepare_invoice`: `sale` -> `sale_stock` (+ l10n_in_sale, l10n_it_edi_sale, l10n_it_edi_doi, l10n_tw_edi_ecpay_website_sale, l10n_ec_sale: found by grep, not read).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Confirm order, deliver (if delivered policy), click Create Invoice -> draft invoice with lines, origin link and chatter note (VDR-U05-C036, VDR-U05-C067). |
| 2 | Reversal/cancel | Order cancel cancels only draft invoices (VDR-U05-C070); posted ones stay; credit notes covered in CAP-U05-04. Deleting an invoice removes its DP lines (VDR-U05-C094). |
| 3 | Multi-company | Per-order `with_company`; company is a grouping key (VDR-U05-C041, VDR-U05-C062); orders of different companies never merge. |
| 4 | Side effects | Upsell activity (VDR-U05-C081); timesheets linked (VDR-U05-C087); invoice paid note on order (VDR-U05-C093); UTM/team copied (VDR-U05-C042). |
| 5 | Configuration | Order `journal_id` optional (VDR-U05-C047); consolidated billing flag; payment term/fiscal position from order (VDR-U05-C045). |
| 6 | Validation | Nothing to invoice -> UserError (VDR-U05-C061); only display lines -> skipped (VDR-U05-C054). |
| 7 | Roles | Wizard ACL for salesman; sudo creation (VDR-U05-C089, VDR-U05-C040); wizard rule own records (VDR-U05-C090); invoice visibility rules by `invoice_user_id` (CAP-U05-09). |
| 8 | Scheduled | No cron in invoice creation itself; automatic-invoice flow is CAP-U05-09. |
| 9 | Exceptions | Silent empty return without rights (VDR-U05-C039); UserError nothing-to-invoice (VDR-U05-C061); missing wizard amount (CAP-U05-03). |
| 10 | Accounting/stock/audit | Draft invoices only: posting/lock/reversal is U11 hand-off; taxes copied as ids (VDR-U05-C055); credit-limit exclusion (VDR-U05-C095); delivery date/incoterm (VDR-U05-C085). |

### DB reconciliation (configuration only)
VDR-U05-C098 ACL rows for `sale.order`, `sale.order.line`, `sale.advance.payment.inv` exist as declared (see CAP-U05-09). Wizard record rule present as a global rule.

### Unknown / Runtime list
- VDR-U05-C097
- Effect of localisation overrides (l10n_* sale modules) on invoice vals: not read; RT/UNKNOWN.
- Rounding/tax recomputation when lines are copied with `extra_tax_data`: account-owned (U11/U07) - not verified here.

## CAP-U05-03 Down payments / advance invoices

**Function-ID(s):** FUNCTION MAPPING REQUIRED. Related: `SDV-F07` (credit effect, CAP-U05-04), `PDT-F01`.

### D1 - Business purpose and process semantics
Prepayment billing before delivery. The order records the advance as service-less "down payment" SO lines (qty 0, price = advance) under a section; the draft advance invoice carries qty 1. The final regular invoice re-lists each advance line at qty -1, deducting it (VDR-U05-C122). Two creation paths: user wizard (VDR-U05-C099) and online payment automation (VDR-U05-C136).

### D2 - Architecture / data / object relationships
- `sale.advance.payment.inv` -> `AccountTax._prepare_down_payment_lines` (account) -> SO lines (`is_downpayment`) + invoice via `order._prepare_invoice()` (VDR-U05-C105, VDR-U05-C111).
- SO line <-> invoice line through `sale_order_line_invoice_rel`; invoice line flag `account.move.line.is_downpayment` (VDR-U05-C072 in CAP-U05-02; VDR-U05-C139).
- Company `downpayment_account_id` (VDR-U05-C115); account.move hooks on post/cancel/draft/unlink (VDR-U05-C125, VDR-U05-C127, VDR-U05-C128, VDR-U05-C130).

### D3 - Source / technical / workflow logic
```
wizard(method percentage|fixed).create_invoices
  -> _check_amount_is_positive (VDR-U05-C101) (button path only VDR-U05-C102)
  -> _create_invoices: ensure_one order (VDR-U05-C103)
     base_lines = all non-display lines at ordered qty (VDR-U05-C104)
     down_payment_base_lines = AccountTax._prepare_down_payment_lines(percent|fixed) (VDR-U05-C105)
     order._create_down_payment_section_line_if_needed(); order._create_down_payment_lines_from_base_lines() (VDR-U05-C108, VDR-U05-C109)
     invoice = account.move.sudo().create(_prepare_down_payment_invoice_values) (VDR-U05-C117)
  later: account.move.action_post -> SO DP lines: name, price_unit, tax_ids refreshed (VDR-U05-C125)
  final invoice: DP lines qty -1 (VDR-U05-C122)
```
DP line state list: `no invoice -> invoiced-on-draft [advance invoice exists, balance != 0] -> settled [final invoice (even draft) nets balance to 0]` (VDR-U05-C120, VDR-U05-C121, VDR-U05-C123).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Percentage advance -> draft advance invoice -> post -> SO DP line shows ref/date -> final invoice deducts (VDR-U05-C129, VDR-U05-C122). |
| 2 | Reversal/cancel | Cancel/reset: names/prices recomputed (VDR-U05-C127, VDR-U05-C128); delete draft: SO DP lines deleted (VDR-U05-C130); credit notes: CAP-U05-04; uninvoiced DP lines deletable on confirmed order (VDR-U05-C131). |
| 3 | Multi-company | Wizard company/currency only when one order (VDR-U05-C100); account mapped via order fiscal position (VDR-U05-C113); post-init per company (VDR-U05-C116). |
| 4 | Side effects | Order chatter note and invoice origin note (VDR-U05-C117); SO line price/tax overwritten on posting (VDR-U05-C125); sale_stock Anglo-Saxon DP context (hand-off U10). |
| 5 | Configuration | Company down payment account (VDR-U05-C115); advance button visibility (VDR-U05-C135). |
| 6 | Validation | Positive amount (VDR-U05-C101); single order (VDR-U05-C103); DB constraints (VDR-U05-C118, VDR-U05-C119); no upper cap found (VDR-U05-C141). |
| 7 | Roles | Wizard ACL salesman (CAP-U05-02 VDR-U05-C089); invoice created sudo (VDR-U05-C117). |
| 8 | Scheduled | None. |
| 9 | Exceptions | UserError non-positive; ValueError on multiple orders (VDR-U05-C103); automatic path unvalidated (VDR-U05-C102). |
| 10 | Accounting/stock/audit | Tax split by tax-engine rounding (VDR-U05-C106); account choice (VDR-U05-C113); locked-order DP freeze (VDR-U05-C126); posting is U11 hand-off. |

### DB reconciliation (configuration only)
VDR-U05-C142

### Unknown / Runtime list
- VDR-U05-C141
- VDR-U05-C143
- Mixed non-discountable taxes with percentage advances: execution needed (RT).

## CAP-U05-04 Credit notes, refunds and returns feeding back into the order

**Function-ID(s):** `SDV-F07` (Return after invoicing, via Credit Note - verified) and interplay with `SDV-F06` (Return via Reverse Transfer, pre-invoice) - stock mechanics handed off to U08/U10.

### D1 - Business purpose and process semantics
Two independent correction routes. (A) Warehouse return: the delivered quantity falls if the return move is flagged `to_refund` (VDR-U05-C163, VDR-U05-C166). On a delivered-basis line `qty_to_invoice` turns negative and a final invoice or credit note settles it (VDR-U05-C158, VDR-U05-C159). (B) Accounting credit note: lowers `qty_invoiced` when its lines still link to order lines (VDR-U05-C144, VDR-U05-C150); on ordered-basis lines the line goes back to `to invoice` (VDR-U05-C157).

### D2 - Architecture / data / object relationships
- `account.move` (`out_refund`) <-> `account.move.line.sale_line_ids` <-> `sale.order.line.invoice_lines`.
- `stock.move.sale_line_id`, `stock.move.to_refund`, `stock.picking.sale_id`, `return_id` for returns.
- `sale.order.line.qty_delivered` (stock source), `qty_invoiced`, `qty_invoiced_posted`, `untaxed_amount_invoiced`, `amount_invoiced`.

### D3 - Source / technical / workflow logic
```
Route A: Return picking (wizard copies sale_line_id, sale_id; to_refund default True)
  -> done incoming move subtracts from qty_delivered (VDR-U05-C163)
  -> qty_to_invoice = delivered - invoiced < 0 (delivery policy)
  -> Create Invoice (final=True always from UI) -> negative lines -> moves_to_switch -> out_refund (VDR-U05-C159, VDR-U05-C038)
Route B: Reverse invoice (account wizard) -> copy with business fields -> sale_line_ids kept -> out_refund lines subtract qty_invoiced (VDR-U05-C149, VDR-U05-C144)
```
State list for a line: `invoiced -> to invoice [refund lowers qty_invoiced (ordered policy) or return lowers qty_delivered (delivered policy)]`; `to invoice -> invoiced [final invoice/credit note posted or drafted]`.
Override chain: base `sale.order.line._prepare_qty_invoiced` (no override found in installed Community modules except `purchase`/`pos_sale` for other models; `pos_sale` not installed) -> `sale_stock._prepare_qty_delivered` -> `sale_mrp` (kits) (VDR-U05-C163).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Invoice, return goods flagged update-quantities, final invoice becomes credit note (VDR-U05-C159). |
| 2 | Reversal/cancel | Cancelled credit note ignored (VDR-U05-C145); draft credit note already counts (VDR-U05-C156). |
| 3 | Multi-company | Credit note follows invoice company; conversion at invoice date to the order currency (VDR-U05-C154). |
| 4 | Side effects | Timesheets released (VDR-U05-C175); COGS lookup (VDR-U05-C178); order chatter none found. |
| 5 | Configuration | Return line flag default True (VDR-U05-C167); localization origin requirement (VDR-U05-C162). |
| 6 | Validation | Cannot lower ordered qty below delivered (VDR-U05-C172); switch guard on numbered docs (VDR-U05-C161). |
| 7 | Roles | Return rights are stock-owned; salesman has write on pickings/moves (CAP-U05-09). Credit note rights account-owned (U11). |
| 8 | Scheduled | None. |
| 9 | Exceptions | UserError on reduce below delivered (VDR-U05-C172); ValidationError switching numbered move (VDR-U05-C161). |
| 10 | Accounting/stock/audit | Posted-only amounts vs draft-inclusive quantities (VDR-U05-C155, VDR-U05-C154); COGS hand-off (VDR-U05-C179). |

### DB reconciliation (configuration only)
VDR-U05-C181

### Unknown / Runtime list
- VDR-U05-C180
- Effect of `to_refund`=False returns on valuation: U10 hand-off.

## CAP-U05-05 Delivery from sales (`sale_stock`): confirmation to delivery, delivered quantity, status

**Function-ID(s):** `SDV-F01` (routing/warehouse selection - transfer chain steps are U08), `SDV-F02` (delivery execution), `SDV-F03` (partial/backorder), `PDT-F01` (per-shipment invoicing alignment, with CAP-U05-06).

### D1 - Business purpose and process semantics
Confirmation of an order generates delivery requests per goods line; delivered quantities flow back from completed stock moves to the order lines and, through the invoicing policy, to what can be billed. Quantity edits, address and date changes, cancellation, partial deliveries and returns all feed back to the order or log notes/activities on it.

### D2 - Architecture / data / object relationships
- `sale.order` (warehouse_id, picking_policy, stock_reference_ids, picking_ids, delivery_status, effective_date) <- `stock.picking.sale_id` (computed from moves) <- `stock.move.sale_line_id` -> `sale.order.line` (route_ids, warehouse_id, move_ids, qty_delivered) (VDR-U05-C223, VDR-U05-C209).
- `stock.reference` (name, sale_ids, move_ids) replaces the older procurement group concept (VDR-U05-C190, VDR-U05-C191).
- `stock.route.sale_selectable`, `res.company.security_lead`, `res.users.property_warehouse_id` (VDR-U05-C210, VDR-U05-C220, VDR-U05-C206).

### D3 - Source / technical / workflow logic
```
sale.order.action_confirm -> write(state=sale) -> _action_confirm [sale_stock first: order_line._action_launch_stock_rule(), then super; other extenders: sale_project, sale_purchase] -> auto-lock if enabled
_action_launch_stock_rule(line): skip if state!=sale / locked / type!=consu (VDR-U05-C186)
   qty = ordered - _get_qty_procurement (VDR-U05-C188); create stock.reference if absent (VDR-U05-C190)
   Procurement(product, qty, uom, customer location, origin, company, values) (VDR-U05-C192); stock.rule.run (VDR-U05-C196)
   confirm resulting pickings (VDR-U05-C197)
done move -> qty_delivered recompute (VDR-U05-C226) -> qty_to_invoice (CAP-U05-01) -> invoice status
```
Delivery status state list: `none -> pending [pickings exist, none done]`; `pending -> started [a picking done, qty_delivered zero]`; `pending/started -> partial [qty delivered and some open picking]`; `* -> full [all pickings done/cancel]`; `* -> none [all cancelled]` (VDR-U05-C227).
Override chain: `sale` base -> `sale_stock` -> `sale_mrp` (kit quantities; `_get_qty_procurement` kit branch) -> `sale_project`/`sale_purchase` (`_action_confirm` extenders). Stock hooks: `stock.move._action_done` -> `_action_synch_order` (VDR-U05-C231).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Confirm -> procurement -> picking confirmed -> validate -> qty_delivered -> invoice (VDR-U05-C184, VDR-U05-C225). |
| 2 | Reversal/cancel | Cancel unfinished pickings (VDR-U05-C201); mass cancel bypasses lock (VDR-U05-C203); posted invoices/done pickings untouched (VDR-U05-C204); returns: CAP-U05-04. |
| 3 | Multi-company | Warehouse/routes check across companies (VDR-U05-C208); line procurement `with_company` (VDR-U05-C186); user default warehouse company-dependent (VDR-U05-C206). |
| 4 | Side effects | Origin notes on pickings; activities on address change (VDR-U05-C221) and quantity decrease (VDR-U05-C200); extra lines on over-delivery (VDR-U05-C230). |
| 5 | Configuration | Shipping policy, safety days, route selectable flag (VDR-U05-C213, VDR-U05-C220, VDR-U05-C210); DB values (VDR-U05-C240, VDR-U05-C242). |
| 6 | Validation | Warehouse required (VDR-U05-C207); no decrease below delivered (VDR-U05-C237); product locked after moves (VDR-U05-C238). |
| 7 | Roles | Salesman create/write stock.picking and stock.move; manager unlink moves; stock user write on sale order (CAP-U05-09). Portal follower rule. |
| 8 | Scheduled | None in sale_stock (no cron/server action); scheduler is stock-owned. |
| 9 | Exceptions | UserErrors: warehouse missing/other company, decrease below delivered, locked cancel. |
| 10 | Accounting/stock/audit | Delivered qty is audit trail for delivery-basis invoicing; invoice delivery date/incoterm (VDR-U05-C229); valuation/COGS hand-off U10 (VDR-U05-C243, VDR-U05-C236). |

### DB reconciliation (configuration only)
VDR-U05-C240 VDR-U05-C242 VDR-U05-C241

### Unknown / Runtime list
- VDR-U05-C239
- Transfer chain steps, backorder behavior and reservation: U08.
- Interaction of two SO-line creation paths for over-delivery (VDR-U05-C230, VDR-U05-C231): RT.

## CAP-U05-06 Interplay of delivered and invoiced quantities (upselling, reconciliation)

**Function-ID(s):** `PDT-F01` (per-shipment invoicing alignment), `PDT-F04` (cross-shipment quantity reconciliation). Verified for sales side only; purchase counterpart (`PDT-F02/F03`) out of scope.

### D1 - Business purpose and process semantics
The order line is the reconciliation unit: ordered, delivered and billed quantities sit side by side and the invoice policy picks which two drive "what to bill". Shipment-by-shipment billing is an emergent property of cumulative quantities, not an explicit link between invoice and picking (VDR-U05-C255, VDR-U05-C256).

### D2 - Architecture / data / object relationships
`sale.order.line`: `product_uom_qty`, `qty_delivered` (method-dependent source), `qty_invoiced` (drafts included), `qty_invoiced_posted`, `qty_to_invoice`, `invoice_status`; `sale.order`: `invoice_status`, `delivery_status`, `effective_date`. Sources of `qty_delivered`: stock moves (VDR-U05-C225), manual (VDR-U05-C262), analytic (VDR-U05-C264), timesheet (VDR-U05-C266), milestones (VDR-U05-C267), kits (VDR-U05-C265).

### D3 - Source / technical / workflow logic
```
shipment done -> stock.move done -> sale_stock._compute_qty_delivered -> qty_to_invoice recompute (VDR-U05-C247) -> line invoice_status (VDR-U05-C248) -> order invoice_status
policy order: qty_to_invoice = ordered - invoiced (VDR-U05-C245); policy delivery: delivered - invoiced (VDR-U05-C246)
```
State list: `no -> to invoice [new delivery or confirmation]`; `to invoice -> invoiced [qty_invoiced >= ordered or sale_stock closure]`; `invoiced -> upselling [delivered > ordered, policy order]` (not literal state order; see line status priority in CAP-U05-01 VDR-U05-C030).
Inheritance chain: `sale` -> `sale_stock` -> `sale_mrp` -> `sale_timesheet` -> `sale_project` for `_prepare_qty_delivered`.

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Delivery-basis: ship, invoice delivered qty, ship rest, invoice delta (VDR-U05-C255). |
| 2 | Reversal/cancel | Return/credit adjust either side (CAP-U05-04); cancelled invoice drops out (VDR-U05-C145). |
| 3 | Multi-company | Per-order currency conversion for amounts (VDR-U05-C154); no cross-company reconciliation. |
| 4 | Side effects | Upsell activity (CAP-U05-02 VDR-U05-C081); sale_stock closure rule (VDR-U05-C253). |
| 5 | Configuration | Product policy; method by product type (VDR-U05-C262); accrual-date context (VDR-U05-C269). |
| 6 | Validation | No hard constraint billed<=delivered (VDR-U05-C249); decrease below delivered blocked only in stock (VDR-U05-C237). |
| 7 | Roles | Delivered qty editable by roles with write on line (CAP-U05-09); `sale.order.line` ACL. |
| 8 | Scheduled | None. |
| 9 | Exceptions | None specific; UserError nothing-to-invoice (CAP-U05-02). |
| 10 | Accounting/stock/audit | Audit trail through links only at line level (VDR-U05-C256); accruals (VDR-U05-C269); COGS hand-off U10. |

### DB reconciliation (configuration only)
VDR-U05-C274

### Unknown / Runtime list
- VDR-U05-C275
- Large-order recompute performance and ordering of stored recomputes: RT.

## CAP-U05-07 Loyalty / promotion programs (`sale_loyalty`)

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 - Business purpose and process semantics
Programs (8 kinds, VDR-U05-C277) turn order content into: reward lines (discounts, free products, gift-card/wallet payment lines), points on coupons for future orders, or both. The sale order recomputes the whole promotional state after any relevant change (VDR-U05-C286..VDR-U05-C291).

### D2 - Architecture / data / object relationships
- `loyalty.program` -> rules (`loyalty.rule`), rewards (`loyalty.reward`), cards (`loyalty.card`, + `order_id` from sale_loyalty), history (`loyalty.history`) (module `loyalty`, DISCOVERED SUPPORTING).
- Order side: `sale.order.applied_coupon_ids`, `code_enabled_rule_ids`, `coupon_point_ids` (`sale.order.coupon.points`), reward lines on `sale.order.line` (`reward_id`, `coupon_id`, `points_cost`, `reward_identifier_code`) (VDR-U05-C327, VDR-U05-C331).
- Reward discount products: `invoice_policy=order`, no taxes (VDR-U05-C323).

### D3 - Source / technical / workflow logic
```
order change / code / reward wizard -> _update_programs_and_rewards:
  1 load cards  2 update applied programs  3 recompute reward lines  4 apply new automatic programs  5 cleanup
action_confirm: validate points >= 0 -> _update_programs_and_rewards -> history -> drop ghost coupons -> credit/debit coupons -> super().action_confirm -> mail reward coupons
_action_cancel: super (cancel docs) -> delete history -> reverse points -> delete reward lines/coupons
```
State list (coupon points): `created(0) -> earned [order confirmed gives points] -> spent [reward line on confirmed order] -> restored [order cancelled or reward line deleted]` (VDR-U05-C311, VDR-U05-C316, VDR-U05-C314, VDR-U05-C318).
Override chain: `loyalty` base models -> `sale_loyalty` extensions on `sale.order`, `sale.order.line`, `loyalty.card`, `loyalty.program`, `loyalty.reward`, `loyalty.history`, `account.move.line`; `sale_loyalty_delivery` (installed, not read).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Add automatic promotion -> reward line appears -> confirm -> history + points (VDR-U05-C308, VDR-U05-C309). |
| 2 | Reversal/cancel | Cancel removes reward lines and reverses points (VDR-U05-C314, VDR-U05-C315); deleting a reward line gives points back (VDR-U05-C318); reward archived if used (VDR-U05-C324). |
| 3 | Multi-company | Program domain includes parent company (VDR-U05-C283); DB global rules (VDR-U05-C339). |
| 4 | Side effects | Emails of reward coupons (VDR-U05-C313); invoice discount-line classification (VDR-U05-C334); auto invoice of zero-total orders (VDR-U05-C332). |
| 5 | Configuration | Program type/applies/trigger (VDR-U05-C277, VDR-U05-C278, VDR-U05-C279); `sale_ok` (VDR-U05-C282); usage limits (VDR-U05-C281, VDR-U05-C330). |
| 6 | Validation | Negative points -> ValidationError (VDR-U05-C308); nothing to discount (VDR-U05-C299); program error messages (VDR-U05-C297, VDR-U05-C306). |
| 7 | Roles | ACL (VDR-U05-C338); wizards for salesman; portal cannot edit reward lines (VDR-U05-C320). |
| 8 | Scheduled | None found in `sale_loyalty` (no cron data). |
| 9 | Exceptions | ValidationError/UserError messages above; serialization retry on locked program (VDR-U05-C307). |
| 10 | Accounting/stock/audit | Reward lines are real invoice lines (ordered policy, VDR-U05-C323, VDR-U05-C322); discounts split per tax (VDR-U05-C301); history audit (VDR-U05-C326). |

### DB reconciliation (configuration only)
VDR-U05-C340 VDR-U05-C339

### Unknown / Runtime list
- VDR-U05-C341
- Effect of `loyalty.compute_all_discount_product_ids` (not found in sale_loyalty; belongs to `loyalty`/`pos_loyalty`): not studied.
- Behavior of every reward type with mixed taxes: RT.

## CAP-U05-08 Cross-sell and cross-module links (`sale_crm`, `sale_purchase`, `sale_mrp`, `sale_timesheet`, `sale_project`)

**Function-ID(s):** FUNCTION MAPPING REQUIRED. Depth: `sale_crm`, `sale_purchase` full; `sale_mrp`, `sale_timesheet`, `sale_project` light (confirmation/invoicing additions only).

### D1 - Business purpose and process semantics
Order confirmation is an integration event. `sale_crm` feeds opportunity revenue; `sale_purchase` buys subcontracted services; `sale_mrp` links manufacturing and kit delivery; `sale_project`/`sale_timesheet` create delivery containers and time-based billing quantities.

### D2 - Architecture / data / object relationships
`sale.order.opportunity_id -> crm.lead`; `purchase.order.line.sale_line_id -> sale.order.line` (+ `purchase.order.line.sale_order_id` related); `mrp.production.sale_line_id`, `stock.move.sale_line_id`; `sale.order.line.project_id/task_id`, `account.analytic.line.so_line`/`timesheet_invoice_id`; `project.milestone.sale_line_id`.

### D3 - Source / technical / workflow logic
```
action_confirm -> _action_confirm chain (MRO order depends on installed set):
   sale_stock: procurement (CAP-U05-05) | sale_purchase: _purchase_service_generation (sudo) | sale_project: _timesheet_service_generation | sale_crm: _update_revenues_from_so (after super)
purchase: line(product.service_to_purchase and no previous purchase line) -> vendor = first _select_seller -> PO (reuse draft per vendor+SO) -> PO line
```
PO state list: `none -> draft PO line [order confirmed]`; `draft -> updated qty [order qty up, PO draft]`; `purchase/cancel -> new PO line for delta [order qty up]` (VDR-U05-C364); activity-only on decrease/cancel (VDR-U05-C365, VDR-U05-C366).
Override chain `_action_confirm`: `sale` (empty hook) -> `sale_stock` (VDR-U05-C184), `sale_purchase` (VDR-U05-C355), `sale_project` (VDR-U05-C377) -> `sale_timesheet` (no own override read). `action_confirm`: `sale` -> `sale_loyalty` -> `sale_crm` (VDR-U05-C345).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Confirm order: opportunity revenue raised (VDR-U05-C346), PO line for flagged services (VDR-U05-C356), project/task (VDR-U05-C378). |
| 2 | Reversal/cancel | PO activities on SO cancel (VDR-U05-C366), SO activity on PO cancel (VDR-U05-C367); no automatic PO cancellation; project cancel not defined (VDR-U05-C388). |
| 3 | Multi-company | `service_to_purchase` company-dependent (VDR-U05-C351); `_purchase_service_get_company` = line company; PO company from SO line; lead/order company check (VDR-U05-C342). |
| 4 | Side effects | PO origin/activities (VDR-U05-C361); kit delivered qty (VDR-U05-C372); timesheet linking (VDR-U05-C384). |
| 5 | Configuration | Product flag/vendors (VDR-U05-C352); project field (VDR-U05-C379); service policies (VDR-U05-C380). |
| 6 | Validation | Vendor required (VDR-U05-C359); service-only flag (VDR-U05-C352). |
| 7 | Roles | sudo for PO generation (VDR-U05-C368); ACLs (VDR-U05-C350, VDR-U05-C375, VDR-U05-C387); PO count group-limited (VDR-U05-C369). |
| 8 | Scheduled | None in these modules (no cron data found). |
| 9 | Exceptions | Vendor missing; wizard action restriction 'You can only apply this action from a lead' (crm wizard). |
| 10 | Accounting/stock/audit | Analytic distribution to invoice (VDR-U05-C386); timesheets-to-invoice trace (VDR-U05-C384); COGS exclusion for MO moves (VDR-U05-C376). |

### DB reconciliation (configuration only)
VDR-U05-C391

### Unknown / Runtime list
- VDR-U05-C388
- VDR-U05-C389
- DISCOVERED SUPPORTING MODULES here: `sale_purchase_stock`, `sale_purchase_project` (installed, not read), `project`, `hr_timesheet`, `purchase`, `crm`, `mrp`.

## CAP-U05-09 Roles, record rules, multi-company scope and scheduled behavior for invoicing/delivery links

**Function-ID(s):** FUNCTION MAPPING REQUIRED. Confirmed against DB configuration tables (ACL, rules, crons, parameters, groups).

### D1 - Business purpose and process semantics
Defines who may create/read/change orders, bill from them, deliver against them, cancel/lock, and what runs automatically. Salespeople are the working role; accounting roles read/write orders; stock users write orders to record delivery effects; portal customers read only. Automatic invoicing is the only invoicing-related scheduled behavior in `sale`.

### D2 - Architecture / data / object relationships
`ir.model.access` (sale, sale_stock, sale_mrp, sale_loyalty, sale_crm, sale_project, sale_timesheet) + `ir.rule` (sale, sale_stock, sale_project) + `res.groups` feature groups; `ir.cron` (2 in sale) <- `ir.config_parameter` (2 keys) via `sale/models/ir_config_parameter.py`; `res.config.settings` fields.

### D3 - Source / technical / workflow logic
```
Setting automatic_invoice (res.config.settings) -> ir.config_parameter 'sale.automatic_invoice'
   -> ir.config_parameter.create/write/unlink -> _sale_sync_linked_crons -> ir.cron(sale.send_invoice_cron).active  (VDR-U05-C428, VDR-U05-C429)
   module install/upgrade -> post_init_hook -> same sync (VDR-U05-C430)
   default_invoice_policy != order -> set_values forces param False (VDR-U05-C432)
payment.transaction done -> _post_process -> (auto_invoice) _invoice_sale_orders + post + send (immediate or cron-trigger) (VDR-U05-C439, VDR-U05-C437)
cron body: _cron_send_invoice -> search done tx with unsent posted invoices of sale-state orders within 2 days -> _send_invoice (VDR-U05-C433, VDR-U05-C434, VDR-U05-C435)
```
Controlling setting for the inactive DB cron: **`sale.automatic_invoice`** (Settings > Sales > Invoicing > Automatic Invoice; visible only if default invoicing policy is "Invoice what is ordered" and online payment required for confirmation) (VDR-U05-C431, VDR-U05-C017). DB: parameter absent -> cron inactive (VDR-U05-C441).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Salesperson creates/invoices own orders (VDR-U05-C392, VDR-U05-C402, VDR-U05-C398+sudo CAP-U05-02). |
| 2 | Reversal/cancel | Manager-only delete; lock blocks cancel (VDR-U05-C416); mass cancel bypass (VDR-U05-C203). |
| 3 | Multi-company | Global rules (VDR-U05-C401); `with_company`/company grouping (VDR-U05-C426); product-company constraints (VDR-U05-C424, VDR-U05-C425); loyalty rules (VDR-U05-C339). |
| 4 | Side effects | Auto invoice triggers posting/send; cron trigger on ready-to-send (VDR-U05-C436). |
| 5 | Configuration | Feature groups (VDR-U05-C409, VDR-U05-C410); automatic invoice param (VDR-U05-C431); async emails (VDR-U05-C438). |
| 6 | Validation | See exception list below (VDR-U05-C417 ... VDR-U05-C422). |
| 7 | Roles/permissions | CSV ACL (VDR-U05-C392, VDR-U05-C393, VDR-U05-C395, VDR-U05-C396, VDR-U05-C397, VDR-U05-C406, VDR-U05-C407); rules (VDR-U05-C402, VDR-U05-C404, VDR-U05-C405); DB confirmation (VDR-U05-C443, VDR-U05-C444, VDR-U05-C442). |
| 8 | Scheduled | Two inactive sale crons (VDR-U05-C427, VDR-U05-C438); account cron separate and active in DB (VDR-U05-C440, VDR-U05-C441). |
| 9 | Exceptions | List: delete confirmed order (VDR-U05-C417); cancel locked (VDR-U05-C416); pricelist change (VDR-U05-C418); product change (VDR-U05-C419); delete confirmed line (VDR-U05-C420); locked fields (VDR-U05-C421); nothing to invoice (VDR-U05-C061); advance amount (VDR-U05-C101); decrease below delivered (VDR-U05-C237); warehouse (VDR-U05-C207); loyalty invalid reward (VDR-U05-C308); vendor missing (VDR-U05-C359); re-invoice locked/cancelled order (VDR-U05-C422). |
| 10 | Accounting/stock/audit | Salesman cannot write account.move directly (VDR-U05-C398); lock and unlock are tracked changes (VDR-U05-C411); payment transactions fully visible to salesmen (VDR-U05-C405). |

### DB reconciliation (configuration only)
VDR-U05-C441 VDR-U05-C442 VDR-U05-C443 VDR-U05-C444

### Unknown / Runtime list
- VDR-U05-C445
- Whether `_trigger()` runs the cron when its `active` flag is false: RT (VDR-U05-C436).

## Claims table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U05-C001 | SDV-F04 | sale/models/product_template.py:35 | invoice_policy = fields.Selection | FACT | sale installed | — | Product template field invoice_policy is a two-value selection: 'order' (Ordered quantities) and 'delivery' (Delivered quantities). | N-U05-004 |
| VDR-U05-C002 | SDV-F04 | sale/models/product_template.py:40 | string="Invoicing Policy" | FACT | sale installed | — | The field is stored, computed with precompute and readonly=False (user-editable) and tracked (tracking=True), so changes are chatter-logged. | N-U05-020 |
| VDR-U05-C003 | SDV-F04 | sale/models/product_template.py:164 | invoice_policy = 'order' | FACT | sale installed | — | _compute_invoice_policy (depends on type) sets 'order' for any template whose type is 'consu' (goods) or whose policy is empty; so recomputing type on goods resets the policy to 'order'. | N-U05-014 |
| VDR-U05-C004 | SDV-F04 | sale/wizard/res_config_settings.py:10 | default_invoice_policy | FACT | sale installed | — | Settings field default_invoice_policy (default 'order', default_model product.template) writes an ir.default so new products get the chosen policy. | N-U05-013 |
| VDR-U05-C005 | SDV-F04 | sale/views/product_views.xml:18 | name="invoice_policy" | FACT | sale installed | — | On the product form invoice_policy is required=1 and invisible when not sale_ok or type == 'combo'. | N-U05-019 |
| VDR-U05-C006 | SDV-F04 | sale/models/sale_order_line.py:1069 | invoice_policy == 'order' | FACT | sale installed | — | _compute_qty_to_invoice: for state=='sale' and non-display lines, policy 'order' gives qty_to_invoice = product_uom_qty - qty_invoiced; otherwise qty_delivered - qty_invoiced. | N-U05-005 |
| VDR-U05-C007 | SDV-F04 | sale/models/sale_order_line.py:1076 | line.qty_to_invoice = 0 | FACT | sale installed | — | For lines of non-sale orders (draft/sent/cancel) or display lines qty_to_invoice is set to 0. | N-U05-006 |
| VDR-U05-C008 | SDV-F04 | sale/models/sale_order_line.py:1055 | no trigger product_id.invoice_policy | FACT | sale installed | — | Source comment states the product policy is deliberately not an @api.depends trigger so existing orders are not retroactively changed; depends list is qty_invoiced, qty_delivered, product_uom_qty, state. | N-U05-007 |
| VDR-U05-C009 | SDV-F04 | sale/models/sale_order_line.py:1069 | line.product_id.invoice_policy | INFERENCE | sale installed | — | Policy is read live from the product inside _compute_qty_to_invoice (line 1069); with no trigger (line 1055-1056), a later policy change affects a line only when one of its listed dependencies is recomputed. | N-U05-021 |
| VDR-U05-C010 | SDV-F04 | sale/models/sale_order_line.py:1181 | uom_qty_to_consider | FACT | sale installed | — | _compute_untaxed_amount_to_invoice uses qty_delivered when policy=='delivery' else product_uom_qty to compute the remaining untaxed amount. | N-U05-009 |
| VDR-U05-C011 | SDV-F04 | sale/models/sale_order_line.py:1216 | qty_to_invoice = line.product_uom_qty - line.qty_invoiced_posted | FACT | sale installed | — | _compute_amount_to_invoice (order-level 'Un-invoiced Balance' source) always uses ordered qty minus posted invoiced qty, independent of policy (comment: ordered quantity is what the customer committed to). | N-U05-009 |
| VDR-U05-C012 | SDV-F04 | sale/models/sale_order_line.py:1108 | line.product_id.invoice_policy == 'order' | FACT | sale installed | — | Line status 'upselling' requires state sale, policy 'order', product_uom_qty >= 0 and qty_delivered > product_uom_qty (after the 'to invoice' test fails). | N-U05-012 |
| VDR-U05-C013 | SDV-F04 | sale_stock/models/sale_order_line.py:239 | line.invoice_status == 'no' | FACT | sale_stock installed | — | sale_stock overrides _compute_invoice_status: a goods line in sale state with status 'no', policy 'delivery', existing moves all done/cancel with at least one done and non-zero qty_delivered is set to 'invoiced' (partial delivery treated as complete). | N-U05-008 |
| VDR-U05-C014 | SDV-F04 | sale/models/sale_order.py:1799 | _force_lines_to_invoice_policy_order | FACT | sale installed | — | _force_lines_to_invoice_policy_order sets qty_to_invoice = product_uom_qty - qty_invoiced on sale-state lines, overriding the product policy for automatic invoicing. | N-U05-010 |
| VDR-U05-C015 | SDV-F04 | sale/models/payment_transaction.py:216 | _force_lines_to_invoice_policy_order | FACT | automatic invoice parameter true | — | In _invoice_sale_orders fully paid orders call _force_lines_to_invoice_policy_order then _create_invoices(final=True); partly paid orders instead get a fixed-amount down payment invoice. | N-U05-010 |
| VDR-U05-C016 | SDV-F04 | sale/wizard/res_config_settings.py:125 | default_invoice_policy != 'order' | FACT | sale installed | — | set_values writes sale.automatic_invoice=False whenever default_invoice_policy is not 'order'. | N-U05-016 |
| VDR-U05-C017 | SDV-F04 | sale/wizard/res_config_settings_views.xml:225 | default_invoice_policy != 'order' | FACT | sale installed | — | The Automatic Invoice setting is invisible unless default_invoice_policy == 'order' and portal_confirmation_pay is set. | N-U05-016 |
| VDR-U05-C018 | SDV-F04 | sale/models/res_company.py:33 | ('invoice_policy', '=', 'order') | FACT | sale installed | — | company.sale_discount_product_id domain requires service products with invoice_policy 'order'. | N-U05-018 |
| VDR-U05-C019 | SDV-F04 | sale_loyalty/models/loyalty_reward.py:15 | 'invoice_policy': 'order' | FACT | sale_loyalty installed | — | Discount products generated for loyalty rewards are created with invoice_policy 'order' (and no taxes). | N-U05-018 |
| VDR-U05-C020 | SDV-F04 | sale_project/models/product_template.py:94 | 'ordered_prepaid': ('order', 'manual') | FACT | sale_project installed | — | Service policies map to (invoice_policy, service_type): ordered_prepaid->(order,manual), delivered_milestones->(delivery,milestones), delivered_manual->(delivery,manual). | N-U05-015 |
| VDR-U05-C021 | SDV-F04 | sale_timesheet/models/product_template.py:14 | 'delivered_timesheet' | FACT | sale_timesheet installed | — | sale_timesheet inserts service policy 'delivered_timesheet' (Based on Timesheets) into the selection and adds service_type 'timesheet'. | N-U05-015 |
| VDR-U05-C022 | SDV-F04 | sale/models/product_template.py:78 | _prepare_invoicing_tooltip | FACT | sale installed | — | Tooltip text: delivery policy on non-goods reads 'Invoice after delivery, based on quantities delivered'; order policy on service reads 'Invoice ordered quantities as soon as this service is sold'. | N-U05-015 |
| VDR-U05-C023 | SDV-F04 | sale/models/sale_order.py:1486 | _nothing_to_invoice_error_message | FACT | sale installed | — | The nothing-to-invoice error text names the product Invoicing Policy: change goods from Delivered to Ordered quantities, or services to Prepaid/Fixed Price, to bill ordered quantities. | N-U05-022 |
| VDR-U05-C024 | SDV-F04 | sale_stock/models/sale_order_line.py:184 | _compute_qty_delivered_method | FACT | sale_stock installed | — | Goods (type 'consu') non-expense lines get qty_delivered_method 'stock_move', so delivered-policy qty comes from stock moves. | N-U05-017 |
| VDR-U05-C025 | SDV-F04 | sale/models/sale_order_line.py:883 | _compute_qty_delivered_method | FACT | sale installed | — | Without stock modules, qty_delivered_method is 'manual' (or 'analytic' for expense lines), so delivered quantity of a delivered-policy line is user-entered or analytic. | N-U05-017 |
| VDR-U05-C026 | SDV-F04 | sale/models/sale_order_line.py:230 | qty_delivered = fields.Float | FACT | sale installed | — | qty_delivered is stored, computed and readonly=False with copy=False, so a user may type a value where the method is manual. | N-U05-017 |
| VDR-U05-C027 | SDV-F04 | sale_stock/models/stock.py:69 | product.invoice_policy == 'delivery' | FACT | sale_stock installed | — | When a picking done creates an SO line for an unlisted product, price_unit is copied from an existing line if policy 'delivery', and forced to 0 if policy 'order'. | N-U05-011 |
| VDR-U05-C028 | SDV-F04 | sale/models/sale_order_line.py:1127 | def _is_discount_line | FACT | sale installed | — | _is_discount_line identifies lines whose product equals company.sale_discount_product_id. | N-U05-018 |
| VDR-U05-C029 | SDV-F04 | sale/models/sale_order_line.py:1064 | combo_lines = set() | FACT | sale installed | — | For combo product lines qty_to_invoice is set to product_uom_qty - qty_invoiced only if some linked combo-item line has a non-zero qty_to_invoice, else 0 (combo parent follows its items). | N-U05-005 |
| VDR-U05-C030 | SDV-F04 | sale/models/sale_order_line.py:1111 | line.invoice_status = 'upselling' | FACT | sale installed | — | Priority order in line status: not sale->'no'; downpayment with zero amount to invoice->'invoiced'; non-zero qty_to_invoice->'to invoice'; upselling test; qty_invoiced>=ordered->'invoiced'; else 'no'. | N-U05-012 |
| VDR-U05-C031 | SDV-F04 | sale/wizard/res_config_settings.py:10 | default_invoice_policy | OBSERVATION | restored DB | — | Restored DB: ir_default holds no row for product.template invoice_policy (only 2 rows exist, both stock location defaults), so new products take the compute-resolved value 'order'. | N-U05-024 |
| VDR-U05-C032 | SDV-F04 | sale/models/product_template.py:35 | invoice_policy = fields.Selection | OBSERVATION | restored DB | — | Restored DB product_template: 13 service products with invoice_policy 'order' and 3 service products with 'delivery'; no other rows (no goods products seeded, no sale orders or order lines). | N-U05-024 |
| VDR-U05-C033 | SDV-F04 | sale/models/payment_transaction.py:92 | sale.automatic_invoice | OBSERVATION | restored DB | — | Restored DB has no ir_config_parameter row for sale.automatic_invoice (rows present: sale.async_emails=False, sale.default_confirmation_template, sale.default_invoice_email_template). | N-U05-016 |
| VDR-U05-C034 | SDV-F04 | sale/views/product_views.xml:18 | name="invoice_policy" | UNKNOWN | runtime | RT | Whether the product form shows or locks invoice_policy differently for services (sale_project/sale_timesheet replace it with service_policy in the view) and for each product type needs the rendered view; only view definitions were read. | N-U05-023 |
| VDR-U05-C035 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:121 | def create_invoices | FACT | sale installed | — | Wizard button create_invoices checks amount positivity then calls _create_invoices(self.sale_order_ids) and opens the resulting invoices via action_view_invoice. | N-U05-045 |
| VDR-U05-C036 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:140 | advance_payment_method == 'delivered' | FACT | sale installed | — | Method 'delivered' (label 'Regular invoice') calls sale_orders._create_invoices(final=self.deduct_down_payments, grouped=not self.consolidated_billing). | N-U05-045 |
| VDR-U05-C037 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance_views.xml:23 | count &gt; 1 | FACT | sale installed | — | Wizard form hides the method radio when more than one order is selected and shows consolidated_billing only when count != 1 (default True). | N-U05-045 |
| VDR-U05-C038 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:31 | deduct_down_payments | INFERENCE | sale installed | — | deduct_down_payments (default True) is never placed in any view (grep of xml shows none), so the UI-created regular invoice always passes final=True; cited lines 31 and 141. | N-U05-053 |
| VDR-U05-C039 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1563 | has_access('create') | FACT | sale installed | — | _create_invoices returns an empty account.move recordset silently if the user cannot create account.move and lacks write access on the order. | N-U05-051 |
| VDR-U05-C040 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1550 | sudo().with_context(default_move_type='out_invoice') | FACT | sale installed | — | _create_account_invoices creates the moves in sudo with default_move_type out_invoice; comment: salesperson must generate invoices without billing rights but not create from scratch. | N-U05-039 |
| VDR-U05-C041 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1575 | order.with_company(order.company_id) | FACT | sale installed | — | Each order is processed with its own company and with the invoicing contact's language. | N-U05-057 |
| VDR-U05-C042 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1429 | 'ref': self.client_order_ref or self.name | FACT | sale installed | — | _prepare_invoice header: ref=client_order_ref or order name, move_type out_invoice, narration=note, currency, campaign/medium/source, team_id. | N-U05-033 |
| VDR-U05-C043 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1437 | 'partner_id': self.partner_invoice_id.id | FACT | sale installed | — | Invoice partner is partner_invoice_id; partner_shipping_id copied; payment term, preferred payment method line, invoice_user_id, payment_reference, company_id and user_id copied from the order. | N-U05-033 |
| VDR-U05-C044 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1421 | txs_to_be_linked | FACT | sale installed | — | Invoice links transactions of the order in state pending/authorized, or done whose payment is not reconciled (transaction_ids Command.set). | N-U05-033 |
| VDR-U05-C045 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1439 | _get_fiscal_position(self.partner_invoice_id) | FACT | sale installed | — | fiscal_position_id = order.fiscal_position_id or the position computed for partner_invoice_id. | N-U05-034 |
| VDR-U05-C046 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1450 | if self.journal_id | FACT | sale installed | — | journal_id is put in the invoice values only if the order has one; otherwise account.move default journal logic applies. | N-U05-035 |
| VDR-U05-C047 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:146 | journal with the lowest sequence | FACT | sale installed | — | Field help on sale.order.journal_id: if set the SO invoices in this journal, otherwise the sales journal with the lowest sequence is used. | N-U05-035 |
| VDR-U05-C048 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:378 | self.journal_id = False | FACT | sale installed | — | _compute_journal_id sets journal_id False in base sale (stored, readonly=False, precompute): journal defaults to empty and is only an extension hook. | N-U05-046 |
| VDR-U05-C049 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1517 | float_is_zero(line.qty_to_invoice | FACT | sale installed | — | _get_invoiceable_lines skips non-note lines with zero qty_to_invoice at Product Unit precision. | N-U05-029 |
| VDR-U05-C050 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1519 | line.qty_to_invoice < 0 and final | FACT | sale installed | — | Lines are taken if qty_to_invoice > 0, or < 0 only when final=True, or are line_note. | N-U05-029 |
| VDR-U05-C051 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1526 | if subsection_line_ids | FACT | sale installed | — | Section and subsection display lines are held and only added when a following product line is invoiceable; notes under a section are collected into it. | N-U05-030 |
| VDR-U05-C052 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1520 | if line.is_downpayment | FACT | sale installed | — | Down payment lines are collected separately and appended last to the invoiceable set. | N-U05-031 |
| VDR-U05-C053 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1591 | order._prepare_down_payment_section_line | FACT | sale installed | — | On invoice build a dedicated line_section 'Down Payments' is inserted before the first down payment line (zero qty/price, no account). | N-U05-031 |
| VDR-U05-C054 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1580 | all(line.display_type for line in invoiceable_lines) | FACT | sale installed | — | An order whose invoiceable set contains only display lines produces no invoice. | N-U05-050 |
| VDR-U05-C055 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1545 | 'display_type': self.display_type or 'product' | FACT | sale installed | — | _prepare_invoice_line maps: sequence, name (journal-item full name), product_id, product_uom_id, quantity=qty_to_invoice, discount, price_unit, tax_ids, sale_line_ids link, is_downpayment, extra_tax_data, collapse flags. | N-U05-032 |
| VDR-U05-C056 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1530 | product_id.type == 'combo' | FACT | sale installed | — | Combo lines are emitted as line_section 'name x qty' with sale_line_ids link instead of a product line. | N-U05-032 |
| VDR-U05-C057 | FUNCTION MAPPING REQUIRED | account/models/account_move_line.py:1244 | related_distribution = line._related_analytic_distribution() | INFERENCE | account installed (supporting) | — | Base _prepare_invoice_line carries no analytic_distribution (helper _set_analytic_distribution at sale_order_line.py:1569 is called only from pos_sale per grep); distribution is computed on the invoice line by _compute_analytic_distribution via _related_analytic_distribution (account_move_line.py:1244), which sale extends with the linked sale line distribution. | N-U05-032 |
| VDR-U05-C058 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:44 | self.sale_line_ids | FACT | sale installed | — | account.move.line._related_analytic_distribution extends the result with the first linked sale line's analytic_distribution. | N-U05-032 |
| VDR-U05-C059 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1604 | optional_values['quantity'] = -1.0 | FACT | sale installed | — | On the invoice, each down payment line is emitted with quantity -1.0 and reversed extra_tax_data, deducting the advance. | N-U05-031 |
| VDR-U05-C060 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1670 | len(invoice_vals_list) < len(self) | FACT | sale installed | — | When grouping reduced the invoice count below the order count, invoice line sequences are renumbered 1..n via _get_invoice_line_sequence. | N-U05-036 |
| VDR-U05-C061 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1616 | raise_if_nothing_to_invoice | FACT | sale installed | — | If no invoice values were produced and context raise_if_nothing_to_invoice is not False, UserError(_nothing_to_invoice_error_message) is raised. | N-U05-050 |
| VDR-U05-C062 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1484 | 'company_id', 'partner_id', 'partner_shipping_id' | FACT | sale installed | — | _get_invoice_grouping_keys = company_id, partner_id, partner_shipping_id, currency_id, fiscal_position_id (partner_id here is the invoice header partner, i.e. partner_invoice_id). | N-U05-036 |
| VDR-U05-C063 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1644 | 'invoice_origin': ', '.join(origins) | FACT | sale installed | — | Grouped invoices concatenate origins, join refs (max 2000 chars) and keep payment_reference only when all merged values are identical. | N-U05-036 |
| VDR-U05-C064 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1620 | if not grouped | FACT | sale installed | — | grouped=True means one invoice per order (no merging); grouped=False merges by grouping keys. | N-U05-036 |
| VDR-U05-C065 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1683 | moves_to_switch | FACT | sale installed | — | With final=True, created moves with amount_total < 0 are switched to credit notes (action_switch_move_type) and _set_reversed_entry is applied. | N-U05-037 |
| VDR-U05-C066 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7388 | def _set_reversed_entry | FACT | account installed (supporting) | — | _set_reversed_entry sets reversed_entry_id on a single out_refund only when exactly one earlier out_invoice shares its order lines and that invoice's _refunds_origin_required() is true (base returns False). | N-U05-037 |
| VDR-U05-C067 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1690 | mail.message_origin_link | FACT | sale installed | — | Each created move gets a mail.message_origin_link note linking the source orders. | N-U05-040 |
| VDR-U05-C068 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1020 | invoice_line.move_id.state != 'cancel' | FACT | sale installed | — | _prepare_qty_invoiced counts lines of every move not in state cancel (drafts included; payment_state invoicing_legacy cancelled moves also counted), adding for out_invoice and subtracting for out_refund. | N-U05-038 |
| VDR-U05-C069 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:95 | 'draft' in invoice_states | FACT | sale installed | — | Wizard computes display_draft_invoice_warning when any order invoice is draft; form text says the new invoice will deduct draft invoices linked to the order. | N-U05-038 |
| VDR-U05-C070 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1334 | inv.button_cancel() | FACT | sale installed | — | _action_cancel cancels draft invoices of the order (invoice_ids filtered state draft) then writes state cancel; posted invoices are untouched. | N-U05-040 |
| VDR-U05-C071 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:577 | move_type in ('out_invoice', 'out_refund') | FACT | sale installed | — | invoice_ids/invoice_count are computed from order_line.invoice_lines.move_id filtered to out_invoice and out_refund, so credit notes are included. | N-U05-025 |
| VDR-U05-C072 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:12 | sale_line_ids = fields.Many2many | FACT | sale installed | — | Link table sale_order_line_invoice_rel joins sale.order.line.invoice_lines to account.move.line.sale_line_ids (readonly, copy=False). | N-U05-025 |
| VDR-U05-C073 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:39 | values['sale_line_ids'] | FACT | sale installed | — | Copies made with include_business_fields keep sale_line_ids so corrected invoices stay linked to the order. | N-U05-052 |
| VDR-U05-C074 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:629 | confirmed_orders = self.filtered | FACT | sale installed | — | _compute_invoice_status: orders whose state is not 'sale' get invoice_status 'no'. | N-U05-041 |
| VDR-U05-C075 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:633 | lines_domain | FACT | sale installed | — | Line statuses considered exclude is_downpayment lines and display lines. | N-U05-043 |
| VDR-U05-C076 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:645 | invoice_status == 'to invoice' | FACT | sale installed | — | Any counted line 'to invoice' makes the order 'to invoice'. | N-U05-042 |
| VDR-U05-C077 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:652 | _can_be_invoiced_alone | FACT | sale installed | — | If some lines are 'no' and every 'to invoice' line is a special line (not _can_be_invoiced_alone) the order is 'no' (discount/delivery/reward lines alone cannot trigger billing). | N-U05-042 |
| VDR-U05-C078 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:660 | all(invoice_status == 'invoiced' | FACT | sale installed | — | All counted lines 'invoiced' -> order 'invoiced'. | N-U05-043 |
| VDR-U05-C079 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:662 | ('invoiced', 'upselling') | FACT | sale installed | — | All counted lines in ('invoiced','upselling') (not all invoiced) -> order 'upselling'; otherwise 'no'. | N-U05-043 |
| VDR-U05-C080 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:246 | invoice_status = fields.Selection | FACT | sale installed | — | sale.order.invoice_status is stored; selection INVOICE_STATUS = upselling, invoiced, to invoice, no; depends on state and order_line.invoice_status. | N-U05-026 |
| VDR-U05-C081 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1966 | def _compute_field_value | FACT | sale installed | — | On recomputation of invoice_status, orders with a salesperson (or partner salesperson) whose previous status was not 'upselling' and are now 'upselling' get _create_upsell_activity (unless mail_activity_automation_skip). | N-U05-044 |
| VDR-U05-C082 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1985 | activity_unlink(['mail.mail_activity_data_todo']) | FACT | sale installed | — | _create_upsell_activity first removes existing todo activities on the order then schedules a todo 'Upsell <order> for customer <partner>' for the salesperson or partner's salesperson. | N-U05-044 |
| VDR-U05-C083 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1125 | self.company_id.sale_discount_product_id.id | FACT | sale installed | — | Base _can_be_invoiced_alone is False only for the company discount product; delivery (delivery module) and reward lines (sale_loyalty) extend it. | N-U05-042 |
| VDR-U05-C084 | FUNCTION MAPPING REQUIRED | delivery/models/sale_order_line.py:16 | not self.is_delivery | FACT | delivery installed (DISCOVERED SUPPORTING MODULE) | — | delivery module marks delivery lines as not invoiceable alone. | N-U05-042 |
| VDR-U05-C085 | FUNCTION MAPPING REQUIRED | sale_stock/models/sale_order.py:300 | 'invoice_incoterm_id' | FACT | sale_stock installed | — | sale_stock _prepare_invoice adds invoice_incoterm_id=order.incoterm and delivery_date=effective_date in the user's timezone. | N-U05-049 |
| VDR-U05-C086 | FUNCTION MAPPING REQUIRED | sale_stock/models/account_move.py:130 | _compute_incoterm_location | FACT | sale_stock installed | — | sale_stock account.move computes incoterm_location from linked orders' incoterm_location and delivery_date from the latest effective_date among linked orders while the move is draft. | N-U05-049 |
| VDR-U05-C087 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order.py:161 | _link_timesheets_to_invoice | FACT | sale_timesheet installed | — | sale_timesheet _create_invoices links timesheets (by context timesheet_start_date/end_date) to the new invoices and resets upsell warning flags. | N-U05-047 |
| VDR-U05-C088 | FUNCTION MAPPING REQUIRED | sale_timesheet/wizard/sale_make_invoice_advance.py:41 | invoicing_timesheet_enabled | FACT | sale_timesheet installed | — | With method delivered and timesheet-billable lines present, the wizard recomputes qty_to_invoice for the chosen date range before creating invoices. | N-U05-047 |
| VDR-U05-C089 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:44 | access_sale_advance_payment_inv | FACT | sale installed | — | ACL on sale.advance.payment.inv: sales_team.group_sale_salesman read/write/create (no unlink); record rule limits to create_uid = user. | N-U05-051 |
| VDR-U05-C090 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:175 | sale_advance_payment_inv_rule | FACT | sale installed | — | Rule sale_advance_payment_inv_rule: domain [('create_uid','=',user.id)] (global). | N-U05-051 |
| VDR-U05-C091 | FUNCTION MAPPING REQUIRED | sale/views/sale_order_views.xml:279 | invisible="invoice_status != 'to invoice'" | FACT | sale installed | — | Order form button 'Create Invoice' (primary) is visible only when invoice_status == 'to invoice'; a second percentage-mode button is visible when invoice_status == 'no' and state == 'sale'. | N-U05-045 |
| VDR-U05-C092 | FUNCTION MAPPING REQUIRED | sale/views/sale_order_views.xml:122 | string="Create Invoices" | FACT | sale installed | — | List-view header button 'Create Invoices' opens the wizard for the selected orders; action is bound to sale.order list/kanban. | N-U05-045 |
| VDR-U05-C093 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:135 | _invoice_paid_hook | FACT | sale installed | — | When an invoice is paid, a message 'Invoice %s paid' is posted on each linked order. | N-U05-040 |
| VDR-U05-C094 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:27 | downpayment_lines | FACT | sale installed | — | Deleting an invoice also deletes the down payment order lines that only that invoice referenced. | N-U05-031 |
| VDR-U05-C095 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:195 | _get_partner_credit_warning_exclude_amount | FACT | sale installed | — | For credit-limit warnings on a draft invoice, the part stemming from linked orders (min of invoiced amount and order amount_to_invoice) is excluded from partner credit to invoice. | N-U05-048 |
| VDR-U05-C096 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order.py:94 | _get_prepaid_service_lines_to_upsell | FACT | sale_timesheet installed | — | sale_timesheet creates the upsell activity when a prepaid service line's delivered qty exceeds ordered qty times service_upsell_threshold and not already warned. | N-U05-055 |
| VDR-U05-C097 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:146 | journal with the lowest sequence | UNKNOWN | runtime | RT | The actual journal chosen when several sale journals exist and none is set on the order is resolved by account.move default logic not read here; needs execution. | N-U05-056 |
| VDR-U05-C098 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:246 | invoice_status = fields.Selection | OBSERVATION | restored DB | — | Restored DB: sale_order and sale_order_line tables are empty (0 rows) and account_move holds 0 out_invoice/out_refund rows, so no state was observed. | N-U05-057 |
| VDR-U05-C099 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:16 | ('percentage', "Down payment (percentage)") | FACT | sale installed | — | advance_payment_method selection: delivered (Regular invoice), percentage, fixed; default 'delivered'. | N-U05-058 |
| VDR-U05-C100 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:34 | amount = fields.Float | FACT | sale installed | — | amount (Float, percentage) and fixed_amount (Monetary) hold the advance size; currency/company computed only when exactly one order is selected. | N-U05-058 |
| VDR-U05-C101 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:114 | wizard.amount <= 0.00 | FACT | sale installed | — | _check_amount_is_positive raises UserError 'The value of the down payment amount must be positive.' for percentage<=0 or fixed<=0. | N-U05-061 |
| VDR-U05-C102 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:122 | self._check_amount_is_positive() | FACT | sale installed | — | The positivity check is called only from create_invoices (button), not from _create_invoices. | N-U05-083 |
| VDR-U05-C103 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:143 | self.sale_order_ids.ensure_one() | FACT | sale installed | — | Percentage/fixed methods call ensure_one on sale_order_ids: more than one order raises. | N-U05-062 |
| VDR-U05-C104 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:148 | not x.display_type | FACT | sale installed | — | Base lines for the advance are built from all non-display order lines at ordered quantity via _prepare_base_line_for_taxes_computation and the tax engine details. | N-U05-082 |
| VDR-U05-C105 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:160 | _prepare_down_payment_lines | FACT | sale installed | — | AccountTax._prepare_down_payment_lines is called with amount_type 'percent' or 'fixed' and computation_key down_payment,<wizard id>. | N-U05-077 |
| VDR-U05-C106 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:4041 | aggregated by taxes | FACT | account installed (supporting) | — | Engine docstring: down payment base lines are aggregated by taxes by default and reduced to exactly match the target amount; non-discountable taxes are wrapped into the base. | N-U05-063 |
| VDR-U05-C107 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3999 | _prepare_base_lines_for_down_payment | FACT | account installed (supporting) | — | _prepare_base_lines_for_down_payment dispatches taxes for which _can_be_discounted is false into base amounts. | N-U05-063 |
| VDR-U05-C108 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:2063 | line.display_type and line.is_downpayment | FACT | sale installed | — | _create_down_payment_section_line_if_needed adds one section line (is_downpayment, line_section) only if none exists. | N-U05-064 |
| VDR-U05-C109 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:2097 | 'is_downpayment': True | FACT | sale installed | — | Each advance SO line: is_downpayment True, product_uom_qty 0.0, price_unit from base line, tax_ids, analytic_distribution, extra_tax_data; created with sale_no_log_for_new_lines. | N-U05-064 |
| VDR-U05-C110 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:2044 | sequence = max(self.order_line.mapped('sequence') | FACT | sale installed | — | Advance lines are sequenced after the current maximum order-line sequence. | N-U05-064 |
| VDR-U05-C111 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:214 | **order._prepare_invoice() | FACT | sale installed | — | _prepare_down_payment_invoice_values starts from order._prepare_invoice() and replaces invoice_line_ids with one line per advance SO line. | N-U05-065 |
| VDR-U05-C112 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:239 | quantity=1.0 | FACT | sale installed | — | Advance invoice lines call so_line._prepare_invoice_line(name, quantity=1.0, account_id) with name 'Down payment of X%' (percentage) or 'Down Payment' (fixed). | N-U05-065 |
| VDR-U05-C113 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:209 | dp_account = self.company_id.downpayment_account_id | FACT | sale installed | — | If company.downpayment_account_id is set it is mapped through the order fiscal position and used for each line; otherwise the line's account from the base line or _get_down_payment_account. | N-U05-066 |
| VDR-U05-C114 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:251 | product_account.get('downpayment') or product_account.get('income') | FACT | sale installed | — | _get_down_payment_account returns the product's 'downpayment' account or else its income account (fiscal-position mapped). | N-U05-066 |
| VDR-U05-C115 | FUNCTION MAPPING REQUIRED | sale/models/res_company.py:50 | downpayment_account_id | FACT | sale installed | — | company.downpayment_account_id: many2one account.account, domain account_type in income, income_other, liability_current, tracked. | N-U05-075 |
| VDR-U05-C116 | FUNCTION MAPPING REQUIRED | sale/__init__.py:30 | downpayment_account_id | FACT | sale installed | — | post_init_hook sets each company's downpayment_account_id from the chart template's template_data when present. | N-U05-075 |
| VDR-U05-C117 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:180 | self.env['account.move'].sudo().create | FACT | sale installed | — | The advance invoice is created in sudo then re-wrapped; a note links the invoice to the order and the order logs 'Down payment invoice has been created'. | N-U05-059 |
| VDR-U05-C118 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:21 | OR is_downpayment | FACT | sale installed | — | DB constraint _accountable_required_fields: display_type NOT NULL OR is_downpayment OR (product_id and product_uom_id NOT NULL); advance lines may have no product. | N-U05-079 |
| VDR-U05-C119 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:25 | display_type IS NULL OR | FACT | sale installed | — | DB constraint _non_accountable_null_fields: display lines must have no product, zero price/qty/lead time and no UoM. | N-U05-079 |
| VDR-U05-C120 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1013 | invoice_lines.filtered(lambda l: l.move_id.state != 'cancel') | FACT | sale installed | — | For advance lines _prepare_qty_invoiced sets qty_invoiced 1 if the sum of balances of its non-cancelled invoice lines is non-zero, else 0. | N-U05-067 |
| VDR-U05-C121 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1104 | line.is_downpayment and line.untaxed_amount_to_invoice == 0 | FACT | sale installed | — | Line status 'invoiced' for an advance line when untaxed_amount_to_invoice == 0. | N-U05-073 |
| VDR-U05-C122 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1603 | if line.is_downpayment | FACT | sale installed | — | On the invoice build advance lines get quantity -1.0; they are selected only when qty_to_invoice<0 and final (sale_order.py:1519). | N-U05-068 |
| VDR-U05-C123 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1072 | line.qty_to_invoice = line.qty_delivered - line.qty_invoiced | INFERENCE | sale installed | — | Advance lines have no product so policy is not 'order': qty_to_invoice = qty_delivered(0 manual) - qty_invoiced(1) = -1; with sale_order.py:1519 this makes them eligible only for final invoices; after the deduction the balances net to 0 so qty_invoiced returns to 0 (line 1013-1018). | N-U05-073 |
| VDR-U05-C124 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:633 | ('is_downpayment', '=', False) | FACT | sale installed | — | Order status aggregation excludes advance lines. | N-U05-074 |
| VDR-U05-C125 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:94 | so_dpl.price_unit = so_dpl._get_downpayment_line_price_unit(real_invoices) | FACT | sale installed | — | On action_post, advance SO lines (of unlocked orders) get price_unit = sum of price_unit of posted invoice lines not in real invoices (credit notes negated) and tax_ids from invoice lines; names recomputed. | N-U05-069 |
| VDR-U05-C126 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:87 | not forwarded to the SO | FACT | sale installed | — | Comment and filter not sol.order_id.locked: locked orders do not receive price/tax updates (names are recomputed regardless). | N-U05-080 |
| VDR-U05-C127 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:107 | def button_cancel | FACT | sale installed | — | button_cancel recomputes advance line names and prices (unlocked orders) after super. | N-U05-069 |
| VDR-U05-C128 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:99 | def button_draft | FACT | sale installed | — | button_draft recomputes advance line names after reset to draft. | N-U05-069 |
| VDR-U05-C129 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:489 | dp_state = self._get_downpayment_state() | FACT | sale installed | — | Description: 'Down Payment: <date> (Draft)', 'Down Payment (Cancelled)', or 'Down Payment (ref: <payment_reference> on <invoice_date>)'; reversed-and-reissued advance keeps the non-reversed invoice. | N-U05-070 |
| VDR-U05-C130 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:27 | line.is_downpayment and line.invoice_lines <= self.mapped('line_ids') | FACT | sale installed | — | account.move.unlink deletes advance SO lines whose only invoice lines are on the deleted moves. | N-U05-071 |
| VDR-U05-C131 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1477 | (line.invoice_lines or not line.is_downpayment) | FACT | sale installed | — | _check_line_unlink: in sale state only non-display lines that have invoice lines or are not advance lines are protected; uninvoiced advance lines may be deleted. | N-U05-071 |
| VDR-U05-C132 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1019 | not l.is_downpayment | FACT | sale installed | — | _get_copiable_order_lines excludes advance lines when duplicating an order. | N-U05-072 |
| VDR-U05-C133 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1266 | line.is_downpayment | FACT | sale installed | — | product_updatable is False for advance lines. | N-U05-072 |
| VDR-U05-C134 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:604 | line.is_downpayment | FACT | sale installed | — | _compute_price_unit skips advance lines, so pricelist recomputation never touches them. | N-U05-072 |
| VDR-U05-C135 | FUNCTION MAPPING REQUIRED | sale/views/sale_order_views.xml:287 | invoice_status != 'no' | FACT | sale installed | — | Percentage-mode Create Invoice button shows when state=='sale' and invoice_status=='no'. | N-U05-076 |
| VDR-U05-C136 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:2134 | _generate_downpayment_invoices | FACT | sale installed | — | _generate_downpayment_invoices creates a fixed-amount wizard per order with amount = context downpayment_fixed_amount or order.amount_paid and calls its _create_invoices (no positivity check). | N-U05-078 |
| VDR-U05-C137 | FUNCTION MAPPING REQUIRED | sale/models/payment_transaction.py:211 | downpayment_invoices | FACT | automatic invoice parameter true | — | Partially paid confirmed orders get down payment invoices of the transaction amount via _generate_downpayment_invoices. | N-U05-078 |
| VDR-U05-C138 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:100 | wizard.amount_invoiced | FACT | sale installed | — | Wizard shows amount_invoiced = order.amount_invoiced (help: only confirmed down payments are considered). | N-U05-059 |
| VDR-U05-C139 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:171 | def _is_downpayment | FACT | sale installed | — | account.move._is_downpayment is true when all linked SO lines are advance lines; account.move.line._get_downpayment_lines resolves advance lines through it. | N-U05-059 |
| VDR-U05-C140 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1013 | l.move_id.state != 'cancel' | INFERENCE | sale installed | — | Draft invoices are included in the balance sum (lines 1013 and 1020), so a draft final invoice carrying the -1 deduction makes the advance line net to zero (qty_invoiced 0) before posting. | N-U05-084 |
| VDR-U05-C141 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:112 | _check_amount_is_positive | UNKNOWN | runtime | RT | No upper bound or order-total cap on percentage/fixed amount was found in wizard or the tax engine call; whether engine clamps at 100% requires execution. | N-U05-081 |
| VDR-U05-C142 | FUNCTION MAPPING REQUIRED | sale/models/res_company.py:50 | downpayment_account_id | OBSERVATION | restored DB | — | Restored DB company: downpayment_account_id is NULL, quotation validity 30 days, portal_confirmation_pay true, prepayment 1.0, sale_discount_product_id NULL; no orders exist so no advance lines. | N-U05-085 |
| VDR-U05-C143 | FUNCTION MAPPING REQUIRED | sale/wizard/sale_make_invoice_advance.py:174 | self._get_down_payment_account | UNKNOWN | runtime | RT | With the DB's empty down payment account, the account comes from base_line['account_id'] or _get_down_payment_account(base_line['product_id']); the tax engine's reduced base lines carry no product, so the effective account needs execution. | N-U05-085 |
| VDR-U05-C144 | SDV-F07 | sale/models/sale_order_line.py:1022 | invoice_line.move_id.move_type == 'out_invoice' | FACT | sale installed | — | _prepare_qty_invoiced adds converted quantity for out_invoice lines and subtracts it for out_refund lines linked to the order line. | N-U05-090 |
| VDR-U05-C145 | SDV-F07 | sale/models/sale_order_line.py:1020 | payment_state == 'invoicing_legacy' | FACT | sale installed | — | Moves in state cancel are ignored unless payment_state is invoicing_legacy; drafts are not ignored. | N-U05-090 |
| VDR-U05-C146 | SDV-F07 | sale/models/sale_order_line.py:987 | only if the refund is generated | FACT | sale installed | CONTRA | Docstring says qty_invoiced decreases only for refunds generated from the SO and that is intentional; code has no such restriction. Prior MODULE_sale record left the invoice-origin refund effect UNKNOWN. | N-U05-109 |
| VDR-U05-C147 | SDV-F07 | sale/models/account_move_line.py:39 | values['sale_line_ids'] = [(6, None, self.sale_line_ids.ids)] | FACT | sale installed | — | _copy_data_extend_business_fields copies sale_line_ids onto copied move lines. | N-U05-092 |
| VDR-U05-C148 | SDV-F07 | account/models/account_move_line.py:2092 | include_business_fields | FACT | account installed (supporting) | — | account.move.line.copy_data calls _copy_data_extend_business_fields only when context include_business_fields is set. | N-U05-092 |
| VDR-U05-C149 | SDV-F07 | account/models/account_move.py:5521 | include_business_fields=True | FACT | account installed (supporting) | — | _reverse_moves copies the move with include_business_fields=True, so credit notes made by reversal carry sale_line_ids. | N-U05-092 |
| VDR-U05-C150 | SDV-F07 | account/models/account_move.py:5521 | include_business_fields=True | INFERENCE | sale installed | — | Combining account_move.py:5521, account_move_line.py:2092 and sale/account_move_line.py:39: a credit note from the standard reversal wizard is linked to the order lines, hence _prepare_qty_invoiced (sale_order_line.py:1022-1025) lowers qty_invoiced; this resolves the prior UNKNOWN. | N-U05-092 |
| VDR-U05-C151 | SDV-F07 | account/wizard/account_move_reversal.py:144 | include_business_fields=True | FACT | account installed (supporting) | — | The reversal wizard's 'modify' path also copies the original with business fields to create the corrected invoice (links preserved). | N-U05-104 |
| VDR-U05-C152 | SDV-F07 | sale/models/account_move.py:77 | 'campaign_id': move.campaign_id.id | FACT | sale installed | — | sale _reverse_moves override copies campaign, medium and source from the original into the reversal defaults. | N-U05-104 |
| VDR-U05-C153 | SDV-F07 | sale/models/sale_order.py:573 | we also search for possible refunds | FACT | sale installed | — | invoice_ids comment: refunds created directly from existing invoices are included because they are linked via lines, not directly to the SO. | N-U05-093 |
| VDR-U05-C154 | SDV-F07 | sale/models/sale_order_line.py:1147 | invoice_line.move_id.move_type == 'out_refund' | FACT | sale installed | — | untaxed_amount_invoiced subtracts posted out_refund price_subtotal (currency converted at invoice date); only posted (or legacy) moves count. | N-U05-091 |
| VDR-U05-C155 | SDV-F07 | sale/models/sale_order_line.py:1039 | invoice_line.move_id.state == 'posted' | FACT | sale installed | — | qty_invoiced_posted counts only posted (or invoicing_legacy) lines, signed by -direction_sign. | N-U05-091 |
| VDR-U05-C156 | SDV-F07 | sale/models/sale_order_line.py:1020 | invoice_line.move_id.state != 'cancel' | INFERENCE | sale installed | — | Because line 1020 filters only cancel, a draft credit note lowers qty_invoiced immediately (cited 1020-1025) whereas amount_invoiced/qty_invoiced_posted wait for posting (1143, 1039). | N-U05-111 |
| VDR-U05-C157 | SDV-F07 | sale/models/sale_order_line.py:1070 | product_uom_qty - line.qty_invoiced | INFERENCE | sale installed | — | Line 1069-1070 (ordered policy) gives qty_to_invoice = ordered - invoiced; with a credit note lowering qty_invoiced (1024-1025) the result becomes positive again and line status returns to 'to invoice'. | N-U05-101 |
| VDR-U05-C158 | SDV-F07 | sale/models/sale_order.py:1519 | line.qty_to_invoice < 0 and final | FACT | sale installed | — | Negative qty_to_invoice lines are invoiced only when final=True. | N-U05-096 |
| VDR-U05-C159 | SDV-F07 | sale/models/sale_order.py:1683 | moves_to_switch | FACT | sale installed | — | A final invoice with negative total is converted to out_refund by action_switch_move_type, which flips product line quantities. | N-U05-096 |
| VDR-U05-C160 | SDV-F07 | account/models/account_move.py:6079 | 'quantity': -line.quantity | FACT | account installed (supporting) | — | action_switch_move_type, when amount_total < 0, negates quantity and extra_tax_data of product lines after toggling the move type. | N-U05-096 |
| VDR-U05-C161 | SDV-F07 | account/models/account_move.py:6060 | existing sequence number | FACT | account installed (supporting) | — | action_switch_move_type refuses documents that already have a sequence number (posted before) and entries. | N-U05-096 |
| VDR-U05-C162 | SDV-F07 | account/models/account_move.py:7388 | def _set_reversed_entry | FACT | account installed (supporting) | — | _set_reversed_entry sets reversed_entry_id only for one credit note when the matching original invoice has _refunds_origin_required() (base False; localizations may override). | N-U05-108 |
| VDR-U05-C163 | SDV-F06 | sale_stock/models/sale_order_line.py:209 | for move in incoming_moves | FACT | sale_stock installed | — | _prepare_qty_delivered subtracts done incoming moves (returns) from outgoing done quantity; unlinked non-return receipts (dropship) are skipped. | N-U05-095 |
| VDR-U05-C164 | SDV-F06 | sale_stock/models/sale_order_line.py:212 | not move.origin_returned_move_id | FACT | sale_stock installed | — | Incoming move is skipped when not done or when it has no origin_returned_move_id, source is not outgoing, ordered qty > 0 and picking has no return_id. | N-U05-095 |
| VDR-U05-C165 | SDV-F06 | sale_stock/models/sale_order_line.py:362 | move.origin_returned_move_id and move.to_refund | FACT | sale_stock installed | — | _get_outgoing_incoming_moves keeps returned outgoing moves only when to_refund and classifies refundable incoming moves by to_refund. | N-U05-094 |
| VDR-U05-C166 | SDV-F06 | stock_account/models/stock_move.py:20 | to_refund = fields.Boolean | FACT | stock_account installed (supporting) | — | stock.move.to_refund 'Update quantities on SO/PO', copy=True, default True: triggers a decrease of delivered quantity in the SO/PO. | N-U05-103 |
| VDR-U05-C167 | SDV-F06 | stock_account/wizard/stock_picking_return.py:10 | to_refund = fields.Boolean | FACT | stock_account installed (supporting) | — | stock.return.picking.line.to_refund default True, copied to the new move. | N-U05-103 |
| VDR-U05-C168 | SDV-F06 | sale_stock/wizard/stock_picking_return.py:12 | vals['sale_line_id'] = self.move_id.sale_line_id | FACT | sale_stock installed | — | Return line wizard copies sale_line_id onto the return move; return picking wizard copies sale_id onto the return picking. | N-U05-097 |
| VDR-U05-C169 | SDV-F06 | sale_stock/models/stock.py:322 | def _can_return | FACT | sale_stock installed | — | StockPicking._can_return is true for pickings linked to a sale_id in addition to base rule. | N-U05-098 |
| VDR-U05-C170 | SDV-F06 | sale_stock/wizard/stock_return_picking.py:9 | def _get_proc_values | FACT | sale_stock installed | — | Return wizard uses the SO line's _prepare_procurement_values when re-delivering. | N-U05-097 |
| VDR-U05-C171 | SDV-F06 | stock/models/stock_rule.py:356 | values['to_refund'] = True | FACT | stock installed (supporting) | — | Procurement with negative quantity marks the move to_refund=True. | N-U05-094 |
| VDR-U05-C172 | SDV-F06 | sale_stock/models/sale_order_line.py:430 | decreased below the amount | FACT | sale_stock installed | — | _update_line_quantity raises UserError when new ordered qty is below max qty_delivered of goods lines, telling the user to create a return. | N-U05-107 |
| VDR-U05-C173 | SDV-F07 | sale/models/sale_order_line.py:502 | A reversed and re-issued down payment | FACT | sale installed | — | Advance line description picks the non-reversed advance invoice when a reversed and re-issued advance links both. | N-U05-099 |
| VDR-U05-C174 | SDV-F07 | sale/models/account_move_line.py:34 | line.company_id.account_storno and line.balance > 0.0 | FACT | sale installed | — | For advance move lines, is_storno is set when storno accounting is on and balance > 0 (reversal lines). | N-U05-099 |
| VDR-U05-C175 | SDV-F07 | sale_timesheet/models/account_move.py:101 | credit_notes | FACT | sale_timesheet installed | — | action_post of a posted credit note that reverses an invoice clears timesheet_invoice_id on timesheets of the reversed invoice for the credited SO lines. | N-U05-100 |
| VDR-U05-C176 | SDV-F07 | sale_timesheet/models/sale_order_line.py:181 | to prevent over-billing | FACT | sale_timesheet installed | — | _recompute_qty_to_invoice caps qty_to_invoice at qty_delivered - qty_invoiced for lines having credit notes. | N-U05-100 |
| VDR-U05-C177 | SDV-F07 | sale_timesheet/models/account_move_reversal.py:7 | def reverse_moves | FACT | sale_timesheet installed | — | With 'modify' reversal, timesheets of the original invoice are re-linked to the new invoice per SO line. | N-U05-100 |
| VDR-U05-C178 | SDV-F07 | sale_stock/models/account_move.py:192 | def _get_lines_from_original_invoice | FACT | sale_stock installed | — | For out_refund without reversed_entry_id, COGS lines are looked up from the order's out_invoices (hand-off U10). | N-U05-106 |
| VDR-U05-C179 | SDV-F07 | sale_stock/models/account_move.py:14 | _stock_account_get_last_step_stock_moves | FACT | sale_stock installed | — | For credit notes the done customer-origin moves are taken from the reversed invoice's lines or from the SO line moves (refunds generated from the SO) (hand-off U10). | N-U05-106 |
| VDR-U05-C180 | SDV-F07 | sale/models/sale_order_line.py:984 | def _compute_qty_invoiced | UNKNOWN | runtime | RT | Observed behavior of qty_invoiced and line status after reversal-wizard credit note requires execution; static chain above is an INFERENCE. | N-U05-112 |
| VDR-U05-C181 | SDV-F07 | sale/models/sale_order_line.py:1007 | def _prepare_qty_invoiced | OBSERVATION | restored DB | — | Restored DB has 0 sale orders and 0 customer invoices/credit notes, so the credit flow cannot be observed. | N-U05-112 |
| VDR-U05-C182 | SDV-F01 | sale_stock/__manifest__.py:22 | 'depends': ['sale', 'stock_account'] | FACT | sale_stock installed | — | sale_stock depends on sale and stock_account and is auto_install (installs when both present). | N-U05-134 |
| VDR-U05-C183 | SDV-F01 | sale_stock/__manifest__.py:47 | 'auto_install': True | FACT | sale_stock installed | — | auto_install is True. | N-U05-134 |
| VDR-U05-C184 | SDV-F01 | sale_stock/models/sale_order.py:213 | _action_confirm | FACT | sale_stock installed | — | SaleOrder._action_confirm calls order_line._action_launch_stock_rule() and then super(). | N-U05-114 |
| VDR-U05-C185 | SDV-F01 | sale/models/sale_order.py:1184 | self.write(self._prepare_confirmation_values()) | FACT | sale installed | — | Base action_confirm writes state 'sale' and date_order=now, calls _action_confirm (extension point) and then auto-locks if setting enabled. | N-U05-114 |
| VDR-U05-C186 | SDV-F01 | sale_stock/models/sale_order_line.py:397 | line.order_id.locked | FACT | sale_stock installed | — | _action_launch_stock_rule skips lines not in state sale, whose order is locked, or whose product type is not 'consu'. | N-U05-117 |
| VDR-U05-C187 | SDV-F01 | sale_stock/models/sale_order_line.py:397 | line.order_id.locked | INFERENCE | sale_stock installed | — | Locking happens after _action_confirm in action_confirm (sale_order.py:1192-1193), so initial confirmation still raises procurements; later quantity increases on a locked order raise none (line 397). | N-U05-138 |
| VDR-U05-C188 | SDV-F01 | sale_stock/models/sale_order_line.py:399 | qty = line._get_qty_procurement | FACT | sale_stock installed | — | Requested quantity = line.product_uom_qty minus _get_qty_procurement (non-cancelled outgoing minus incoming move quantities); equal quantities skip. | N-U05-117 |
| VDR-U05-C189 | SDV-F01 | sale_stock/models/sale_order_line.py:317 | def _get_qty_procurement | FACT | sale_stock installed | — | _get_qty_procurement sums outgoing moves (done: quantity, else product_uom_qty) minus incoming moves converted to the line UoM. | N-U05-117 |
| VDR-U05-C190 | SDV-F01 | sale_stock/models/sale_order_line.py:403 | references = line.order_id.stock_reference_ids | FACT | sale_stock installed | — | If the order has no stock_reference_ids a stock.reference is created with name=order name and sale_ids=[order] (no procurement.group in sale_stock). | N-U05-114 |
| VDR-U05-C191 | SDV-F01 | stock/models/stock_reference.py:5 | _name = 'stock.reference' | FACT | stock installed (supporting) | CONTRA | stock.reference ('Reference between stock documents') replaces the procurement-group role; prior notion of procurement group is absent in Odoo 19 sale_stock (only a stale comment at stock.py:230 mentions group_id). | N-U05-114 |
| VDR-U05-C192 | SDV-F01 | sale_stock/models/sale_order_line.py:294 | values.update({ | FACT | sale_stock installed | — | _prepare_procurement_values sets origin, reference_ids, sale_line_id, date_planned, date_deadline, route_ids, warehouse_id, partner_id (delivery contact), location_final_id, description, company_id, sequence, attribute values, packaging uom. | N-U05-118 |
| VDR-U05-C193 | SDV-F01 | sale_stock/models/sale_order_line.py:292 | date_deadline = self.order_id.commitment_date or self._expected_date() | FACT | sale_stock installed | — | date_deadline = commitment_date or line._expected_date(); date_planned = deadline minus company security_lead days. | N-U05-119 |
| VDR-U05-C194 | SDV-F01 | sale/models/sale_order_line.py:1496 | def _expected_date | FACT | sale installed | — | _expected_date = date_order (when state sale) or now, plus customer_lead days. | N-U05-119 |
| VDR-U05-C195 | SDV-F01 | sale_stock/models/sale_order_line.py:315 | partner_shipping_id.property_stock_customer | FACT | sale_stock installed | — | Final location is the delivery partner's customer location property. | N-U05-118 |
| VDR-U05-C196 | SDV-F01 | sale_stock/models/sale_order_line.py:415 | self.env['stock.rule'].run(procurements) | FACT | sale_stock installed | — | Procurements are executed via stock.rule.run; then non-done non-cancelled pickings of the orders are confirmed to trigger the scheduler. | N-U05-114 |
| VDR-U05-C197 | SDV-F01 | sale_stock/models/sale_order_line.py:423 | pickings_to_confirm.action_confirm() | FACT | sale_stock installed | — | Pickings not cancel/done are confirmed immediately after the run. | N-U05-114 |
| VDR-U05-C198 | SDV-F01 | sale_stock/models/sale_order_line.py:251 | _action_launch_stock_rule() | FACT | sale_stock installed | — | Creating lines already in state sale (e.g. added on a confirmed order) launches procurements. | N-U05-120 |
| VDR-U05-C199 | SDV-F01 | sale_stock/models/sale_order_line.py:262 | previous_product_uom_qty=previous_product_uom_qty | FACT | sale_stock installed | — | Writing product_uom_qty on non-expense sale-state lines launches procurements with the previous quantity. | N-U05-120 |
| VDR-U05-C200 | SDV-F01 | sale_stock/models/sale_order.py:191 | order_line.product_uom_qty, pre_order_line_qty | FACT | sale_stock installed | — | On write of order_line in state sale, quantity decreases are collected and _log_decrease_ordered_quantity logs activities on affected open pickings. | N-U05-120 |
| VDR-U05-C201 | SDV-F02 | sale_stock/models/sale_order.py:258 | action_cancel() | FACT | sale_stock installed | — | _action_cancel cancels all pickings not done (skip_cancel_activity) and logs decreased ordered quantity before super()._action_cancel(). | N-U05-130 |
| VDR-U05-C202 | SDV-F02 | sale/models/sale_order.py:1328 | order.locked | FACT | sale installed | — | action_cancel raises UserError 'You cannot cancel a locked order. Please unlock it first.' for locked orders; cancel button hidden when locked. | N-U05-140 |
| VDR-U05-C203 | SDV-F02 | sale/wizard/mass_cancel_orders.py:32 | _action_cancel | FACT | sale installed | — | action_mass_cancel calls _action_cancel directly on the selected orders, bypassing the locked check and any state check. | N-U05-140 |
| VDR-U05-C204 | SDV-F02 | sale/models/sale_order.py:1333 | self.invoice_ids.filtered | FACT | sale installed | — | Base _action_cancel cancels only draft invoices and sets state cancel; it does not touch posted invoices or done pickings. | N-U05-141 |
| VDR-U05-C205 | SDV-F01 | sale_stock/models/sale_order.py:226 | _get_model_defaults('sale.order').get('warehouse_id') | FACT | sale_stock installed | — | warehouse_id computed (stored, editable): company ir.default else user's property_warehouse_id/default; only recomputed for draft/sent or new. | N-U05-121 |
| VDR-U05-C206 | SDV-F01 | sale_stock/models/res_users.py:10 | property_warehouse_id | FACT | sale_stock installed | — | res.users.property_warehouse_id is company-dependent and checked per company; users can read/write it on themselves. | N-U05-121 |
| VDR-U05-C207 | SDV-F01 | sale_stock/models/sale_order.py:148 | You must set a warehouse | FACT | sale_stock installed | — | _check_warehouse raises UserError for non-draft/cancel orders without warehouse when a consu line exists and the company owns a warehouse (no warehouse -> redirect warning). | N-U05-136 |
| VDR-U05-C208 | SDV-F01 | sale_stock/models/sale_order.py:152 | delivery in different company | FACT | sale_stock installed | — | Raises 'You must have a warehouse for line using a delivery in different company' when a line route belongs to another company with no warehouse. | N-U05-136 |
| VDR-U05-C209 | SDV-F01 | sale_stock/models/sale_order_line.py:35 | line.warehouse_id = line.order_id.warehouse_id | FACT | sale_stock installed | — | Line warehouse defaults to the order's; with line routes it takes the source warehouse of the first matching non-push rule toward the customer location. | N-U05-121 |
| VDR-U05-C210 | SDV-F01 | sale_stock/models/stock.py:12 | sale_selectable | FACT | sale_stock installed | — | stock.route.sale_selectable 'Selectable on Sales Order Line'; line route_ids domain restricts to selectable routes. | N-U05-131 |
| VDR-U05-C211 | SDV-F01 | sale_stock/models/sale_order_line.py:16 | route_ids = fields.Many2many | FACT | sale_stock installed | — | sale.order.line.route_ids many2many to stock.route, domain sale_selectable=True, ondelete restrict. | N-U05-131 |
| VDR-U05-C212 | SDV-F03 | sale_stock/models/sale_order.py:21 | picking_policy = fields.Selection | FACT | sale_stock installed | — | picking_policy: 'direct' (as soon as possible) or 'one' (when all products are ready), required, default 'direct'. | N-U05-123 |
| VDR-U05-C213 | SDV-F03 | sale_stock/models/res_config_settings.py:15 | default_picking_policy | FACT | sale_stock installed | — | Settings default_picking_policy (default model sale.order, required): ship as soon as available with backorders, or all at once. | N-U05-132 |
| VDR-U05-C214 | SDV-F03 | sale_stock/models/sale_order.py:125 | def _select_expected_date | FACT | sale_stock installed | — | expected_date uses min of line dates for direct, max for 'one'. | N-U05-123 |
| VDR-U05-C215 | SDV-F03 | sale/models/sale_order.py:748 | line.product_id.type == 'consu' | FACT | sale installed | — | Base expected_date is computed from goods lines excluding delivery lines; services give False. | N-U05-123 |
| VDR-U05-C216 | SDV-F03 | sale_stock/models/stock.py:203 | so.picking_policy == "direct" | FACT | sale_stock installed | — | Picking move_type is 'direct' if any linked order has policy direct, else 'one'. | N-U05-123 |
| VDR-U05-C217 | SDV-F01 | sale_stock/models/sale_order.py:173 | if 'commitment_date' in values | FACT | sale_stock installed | — | Writing commitment_date sets date_deadline on open (not done/cancel) moves whose final location is customer to commitment or expected date. | N-U05-124 |
| VDR-U05-C218 | SDV-F01 | sale_stock/models/sale_order_line.py:278 | def _inverse_customer_lead | FACT | sale_stock installed | — | Changing customer_lead on a sale-state line without order commitment_date sets move deadlines to date_order + lead days. | N-U05-124 |
| VDR-U05-C219 | SDV-F01 | sale_stock/models/sale_order_line.py:276 | line.customer_lead = line.product_id.sale_delay | FACT | sale_stock installed | — | customer_lead defaults from product sale_delay (stored, editable). | N-U05-119 |
| VDR-U05-C220 | SDV-F01 | sale_stock/models/res_company.py:10 | security_lead | FACT | sale_stock installed | — | company.security_lead 'Sales Safety Days' float, default 0, required; settings expose it with use_security_lead flag. | N-U05-132 |
| VDR-U05-C221 | SDV-F01 | sale_stock/models/sale_order.py:160 | update_delivery_shipping_partner | FACT | sale_stock installed | — | partner_shipping_id change: with context update_delivery_shipping_partner picking partners are updated; otherwise an activity is scheduled on open pickings. | N-U05-125 |
| VDR-U05-C222 | SDV-F01 | sale_stock/models/sale_order.py:241 | res['warning'] | FACT | sale_stock installed | — | Onchange warns to change the partner on open delivery orders. | N-U05-125 |
| VDR-U05-C223 | SDV-F02 | sale_stock/models/stock.py:187 | sale_id = fields.Many2one('sale.order' | FACT | sale_stock installed | — | stock.picking.sale_id stored, computed from reference sale_ids/move sale lines (first order), with inverse writing references. | N-U05-115 |
| VDR-U05-C224 | SDV-F02 | sale_stock/models/sale_order_line.py:193 | line.qty_delivered_method = 'stock_move' | FACT | sale_stock installed | — | Non-expense goods lines get qty_delivered_method 'stock_move'. | N-U05-122 |
| VDR-U05-C225 | SDV-F02 | sale_stock/models/sale_order_line.py:205 | for move in outgoing_moves | FACT | sale_stock installed | — | qty_delivered sums quantity of done outgoing moves (HALF-UP, line UoM) and subtracts done refundable incoming moves. | N-U05-122 |
| VDR-U05-C226 | SDV-F02 | sale_stock/models/sale_order_line.py:195 | move_ids.location_dest_usage | FACT | sale_stock installed | — | _compute_qty_delivered depends on move state, destination usage, quantity and UoM, so it recomputes as moves finish. | N-U05-122 |
| VDR-U05-C227 | SDV-F03 | sale_stock/models/sale_order.py:93 | order.picking_ids or all | FACT | sale_stock installed | — | delivery_status: False when no pickings or all cancelled; 'full' when all done/cancel; 'partial' when some done and some qty_delivered; 'started' when some done but no qty; else 'pending'. | N-U05-129 |
| VDR-U05-C228 | SDV-F02 | sale_stock/models/sale_order.py:86 | x.location_dest_id.usage == 'customer' | FACT | sale_stock installed | — | effective_date = earliest date_done of done pickings to a customer location ('completion date of the first delivery order'). | N-U05-115 |
| VDR-U05-C229 | PDT-F01 | sale_stock/models/sale_order.py:301 | delivery_date | FACT | sale_stock installed | — | Invoices created from the order get delivery_date = effective_date (timezone converted) and incoterm. | N-U05-128 |
| VDR-U05-C230 | SDV-F02 | sale_stock/models/stock.py:237 | def _action_done | FACT | sale_stock installed | — | StockPicking._action_done creates SO lines (qty 0, qty_delivered=moved qty, skip_procurement) for done customer-bound moves without sale_line_id; price copied for delivery policy, 0 for order policy. | N-U05-126 |
| VDR-U05-C231 | SDV-F02 | sale_stock/models/stock.py:37 | def _action_synch_order | FACT | sale_stock installed | — | stock.move._action_synch_order (called from stock.move._action_done, stock_move.py:2316) contains near-identical logic, linking an existing line of the product or creating a new one. | N-U05-142 |
| VDR-U05-C232 | SDV-F03 | sale_stock/models/stock.py:284 | def _log_less_quantities_than_expected | FACT | sale_stock installed | — | Logs an activity/note on the SO for moves validated with less than expected, then calls super. | N-U05-127 |
| VDR-U05-C233 | SDV-F03 | stock/models/stock_picking.py:1599 | def _create_backorder | FACT | stock installed (supporting) | — | Backorder creation (transfer engine) moves non-done non-cancel moves into a new picking; sale_stock does not override it, so remaining quantity stays linked to the same SO lines via sale_line_id. | N-U05-143 |
| VDR-U05-C234 | SDV-F03 | sale_stock/models/stock.py:90 | _prepare_merge_moves_distinct_fields | FACT | sale_stock installed | — | sale_line_id is a distinct field for move merging, so moves of different SO lines are never merged. | N-U05-118 |
| VDR-U05-C235 | SDV-F01 | sale_stock/models/stock.py:180 | 'sale_line_id', 'partner_id', 'sequence', 'to_refund' | FACT | sale_stock installed | — | stock.rule custom move fields include sale_line_id, partner_id, sequence, to_refund so rule-created moves inherit them. | N-U05-118 |
| VDR-U05-C236 | PDT-F01 | sale_stock/models/stock.py:95 | _get_related_invoices | FACT | sale_stock installed | — | StockMove._get_related_invoices returns posted invoices of the picking's order (hand-off U10). | N-U05-134 |
| VDR-U05-C237 | SDV-F02 | sale_stock/models/sale_order_line.py:430 | create a return in your inventory | FACT | sale_stock installed | — | Decreasing ordered qty below the max delivered qty of goods lines raises UserError. | N-U05-137 |
| VDR-U05-C238 | SDV-F02 | sale_stock/models/sale_order_line.py:269 | line.move_ids.filtered(lambda m: m.state != 'cancel') | FACT | sale_stock installed | — | product_updatable is False once the line has any non-cancelled move. | N-U05-137 |
| VDR-U05-C239 | SDV-F01 | sale_stock/models/sale_order_line.py:293 | security_lead | UNKNOWN | runtime | RT | Effective delivery dates with company safety days (DB: security_lead=5, use_security_lead true) need execution against procurement dates. | N-U05-144 |
| VDR-U05-C240 | SDV-F01 | sale_stock/models/sale_order_line.py:33 | def _compute_warehouse_id | OBSERVATION | restored DB | — | Restored DB: 1 warehouse (reception one_step, delivery ship_only = single step); 1 outgoing picking type; 9 stock routes of which 2 sale_selectable=true and 7 not set; no sale.order ir.default rows (no default warehouse/picking policy stored). | N-U05-135 |
| VDR-U05-C241 | SDV-F02 | sale/models/sale_order.py:1203 | _is_feature_enabled('sale.group_auto_done_setting') | OBSERVATION | restored DB | RT | Restored DB: res_groups_implied_rel has base.group_user implying sale.group_auto_done_setting (also discount, warning, pro-forma groups); the superuser's group base.group_system implies base.group_user and thus group 38 (recursive implied chain), so _should_be_locked would be true (confirmation auto-locks); runtime confirmation required. | N-U05-139 |
| VDR-U05-C242 | SDV-F01 | sale_stock/models/res_company.py:10 | security_lead | OBSERVATION | restored DB | — | Restored DB: company security_lead = 5 and ir_config_parameter sale_stock.use_security_lead = True. | N-U05-132 |
| VDR-U05-C243 | SDV-F02 | sale_stock/wizard/accrued_orders.py:8 | _get_product_expense_and_stock_var_accounts | FACT | sale_stock installed | — | Accrued orders wizard picks expense and stock variation accounts for storable real-time valued products (hand-off U10). | N-U05-134 |
| VDR-U05-C244 | SDV-F02 | sale_stock/models/sale_order_line.py:397 | line.product_id.type != 'consu' | FACT | sale_stock installed | — | The launch condition tests product type 'consu' (goods), not is_storable, so non-storable goods are also procured; is_storable only gates the availability widget. | N-U05-133 |
| VDR-U05-C245 | PDT-F01 | sale/models/sale_order_line.py:1069 | line.product_id.invoice_policy == 'order' | FACT | sale installed | — | With policy 'order' qty_to_invoice = product_uom_qty - qty_invoiced from confirmation onwards, with no reference to qty_delivered. | N-U05-148 |
| VDR-U05-C246 | PDT-F01 | sale/models/sale_order_line.py:1072 | line.qty_to_invoice = line.qty_delivered - line.qty_invoiced | FACT | sale installed | — | With policy 'delivery' qty_to_invoice = qty_delivered - qty_invoiced. | N-U05-148 |
| VDR-U05-C247 | PDT-F01 | sale/models/sale_order_line.py:1056 | 'qty_invoiced', 'qty_delivered', 'product_uom_qty', 'state' | FACT | sale installed | — | qty_to_invoice recomputes on changes of qty_invoiced, qty_delivered, product_uom_qty and state. | N-U05-166 |
| VDR-U05-C248 | PDT-F01 | sale/models/sale_order_line.py:1086 | 'qty_delivered', 'qty_to_invoice', 'qty_invoiced' | FACT | sale installed | — | Line invoice_status recomputes on state, product_uom_qty, qty_delivered, qty_to_invoice, qty_invoiced. | N-U05-158 |
| VDR-U05-C249 | PDT-F01 | sale/models/sale_order.py:1517 | float_is_zero(line.qty_to_invoice | INFERENCE | sale installed | — | _get_invoiceable_lines (1517-1519) and _create_invoices contain no check comparing quantity to bill with delivered quantity; under policy 'order' invoicing before delivery is allowed (sale_order_line.py:1069). | N-U05-150 |
| VDR-U05-C250 | PDT-F04 | sale/models/sale_order.py:1519 | line.qty_to_invoice < 0 and final | FACT | sale installed | — | qty_to_invoice < 0 (billed more than delivered under policy delivery) is included only on final invoices. | N-U05-149 |
| VDR-U05-C251 | PDT-F04 | sale/models/sale_order_line.py:1110 | float_compare(line.qty_delivered, line.product_uom_qty | FACT | sale installed | — | Upselling at line level: policy order, ordered >= 0 and delivered > ordered at Product Unit precision when nothing is left to bill. | N-U05-158 |
| VDR-U05-C252 | PDT-F04 | sale/models/sale_order.py:662 | ('invoiced', 'upselling') | FACT | sale installed | — | Order-level upselling when all counted lines are invoiced or upselling. | N-U05-145 |
| VDR-U05-C253 | PDT-F01 | sale_stock/models/sale_order_line.py:244 | not float_is_zero(line.qty_delivered | FACT | sale_stock installed | — | sale_stock marks a delivery-policy goods line 'invoiced' when its moves are all done/cancel and delivered qty is non-zero even if below ordered. | N-U05-159 |
| VDR-U05-C254 | PDT-F04 | sale/models/sale_order_line.py:1112 | float_compare(line.qty_invoiced, line.product_uom_qty | FACT | sale installed | — | 'invoiced' when qty_invoiced >= product_uom_qty. | N-U05-159 |
| VDR-U05-C255 | PDT-F01 | sale/models/sale_order_line.py:1072 | line.qty_delivered - line.qty_invoiced | INFERENCE | sale installed | — | Because qty_to_invoice is cumulative delivered minus cumulative invoiced (line 1072) and qty_invoiced includes every non-cancelled invoice line (line 1020), each invoice covers the delivered quantity added since the previous invoice; no invoice-to-picking link is stored (invoice lines link only to SO lines). | N-U05-146 |
| VDR-U05-C256 | PDT-F01 | sale_stock/models/stock.py:95 | def _get_related_invoices | FACT | sale_stock installed | — | The relation between stock moves and invoices is order-wide: all posted invoices of the picking's order. | N-U05-157 |
| VDR-U05-C257 | PDT-F01 | sale_stock/models/sale_order.py:84 | def _compute_effective_date | FACT | sale_stock installed | — | effective_date is the minimum done-date over customer deliveries, used for every invoice of the order. | N-U05-157 |
| VDR-U05-C258 | PDT-F04 | sale/models/sale_order_line.py:1007 | def _prepare_qty_invoiced | INFERENCE | sale installed | — | Billed quantity exists as qty_invoiced (non-cancelled incl. draft, lines 1020-1025), qty_invoiced_posted (posted only, 1039) and posted amount fields (1143, 1157); they diverge while drafts exist. | N-U05-164 |
| VDR-U05-C259 | PDT-F04 | sale/models/sale_order_line.py:1021 | round=False | FACT | sale installed | — | Invoice line quantity is converted to the SO line UoM with round=False. | N-U05-152 |
| VDR-U05-C260 | PDT-F04 | sale/models/sale_order_line.py:611 | line.qty_invoiced > 0 | FACT | sale installed | — | _compute_price_unit does not recompute price when qty_invoiced > 0. | N-U05-153 |
| VDR-U05-C261 | PDT-F04 | sale/models/sale_order_line.py:1443 | _update_line_quantity | FACT | sale installed | — | Base _update_line_quantity only posts a note with ordered/delivered/invoiced quantity; no check against invoiced quantity. | N-U05-151 |
| VDR-U05-C262 | PDT-F04 | sale/models/sale_order_line.py:896 | line.qty_delivered_method = 'manual' | FACT | sale installed | — | Services and non-stock goods get method 'manual'; qty_delivered field is editable. | N-U05-154 |
| VDR-U05-C263 | PDT-F04 | sale/models/sale_order_line.py:912 | not so_line.qty_delivered or | FACT | sale installed | — | _compute_qty_delivered overwrites qty_delivered only if it is zero or the line has a computed value, so manual values survive recomputation for manual lines. | N-U05-165 |
| VDR-U05-C264 | PDT-F04 | sale/models/sale_order_line.py:931 | _get_delivered_quantity_by_analytic([('amount', '<=', 0.0)]) | FACT | sale installed | — | Expense lines take delivered qty from analytic lines with amount <= 0 grouped by UoM. | N-U05-154 |
| VDR-U05-C265 | PDT-F04 | sale_mrp/models/sale_order_line.py:59 | order_qty = order_line.product_uom_id | FACT | sale_mrp installed | — | Kit (phantom BoM) lines compute delivered qty from component moves via _compute_kit_quantities; if no relevant BoM it is all-or-nothing (full qty only when all moves done to customer). | N-U05-154 |
| VDR-U05-C266 | PDT-F04 | sale_timesheet/models/sale_order_line.py:76 | lines_by_timesheet | FACT | sale_timesheet installed | — | Timesheet-method lines take delivered qty from analytic lines with project_id set. | N-U05-154 |
| VDR-U05-C267 | PDT-F04 | sale_project/models/sale_order_line.py:97 | reached_milestones_per_sol | FACT | sale_project installed | — | Milestone-method lines: delivered = sum(quantity_percentage of reached milestones) x ordered qty. | N-U05-154 |
| VDR-U05-C268 | PDT-F04 | sale/models/sale_order_line.py:1080 | combo_line.linked_line_ids | FACT | sale installed | — | Combo parent qty_to_invoice is non-zero only if some linked combo item line has qty_to_invoice. | N-U05-155 |
| VDR-U05-C269 | PDT-F04 | sale/models/sale_order_line.py:917 | _compute_qty_delivered_at_date | FACT | sale installed | — | qty_delivered_at_date and qty_invoiced_at_date honor context accrual_entry_date, filtering moves and invoice lines to that date; amount_to_invoice_at_date = delivered - invoiced at date x gross price. | N-U05-156 |
| VDR-U05-C270 | PDT-F04 | sale_stock/models/sale_order_line.py:352 | accrual_entry_date | FACT | sale_stock installed | — | Stock move selection in qty delivered honors accrual_entry_date by filtering moves to date <= accrual date. | N-U05-156 |
| VDR-U05-C271 | PDT-F04 | sale/models/sale_order_line.py:1100 | precision_get('Product Unit') | FACT | sale installed | — | Status tests use the 'Product Unit' decimal precision. | N-U05-162 |
| VDR-U05-C272 | PDT-F04 | sale/models/sale_order.py:779 | order.order_line.mapped('amount_to_invoice') | FACT | sale installed | — | Order amount_to_invoice and amount_invoiced are sums of line values (not stored). | N-U05-145 |
| VDR-U05-C273 | PDT-F04 | sale/models/sale_order_line.py:1020 | invoice_line.move_id.state != 'cancel' | INFERENCE | sale installed | — | A draft invoice already deducts its quantity from qty_to_invoice (line 1069-1072 via qty_invoiced) so billable quantity disappears until the draft is cancelled; the wizard displays a draft warning (sale_make_invoice_advance.py:91-95). | N-U05-163 |
| VDR-U05-C274 | PDT-F04 | sale/models/sale_order_line.py:1056 | 'qty_invoiced', 'qty_delivered' | OBSERVATION | restored DB | — | Restored DB has no sale orders, so reconciliation was not observed; stored columns qty_invoiced, qty_to_invoice, invoice_status exist only structurally. | N-U05-166 |
| VDR-U05-C275 | PDT-F04 | sale/models/sale_order_line.py:1021 | _compute_quantity | UNKNOWN | runtime | RT | Rounding differences when delivered qty is computed with HALF-UP (sale_stock) and billed qty with round=False need execution on multi-UoM orders. | N-U05-167 |
| VDR-U05-C276 | FUNCTION MAPPING REQUIRED | sale_loyalty/__manifest__.py:9 | 'depends': ['sale', 'loyalty'] | FACT | sale_loyalty installed | — | sale_loyalty depends on sale and loyalty and is auto_install. | N-U05-189 |
| VDR-U05-C277 | FUNCTION MAPPING REQUIRED | loyalty/models/loyalty_program.py:98 | ('gift_card', "Gift Card") | FACT | loyalty installed (DISCOVERED SUPPORTING MODULE) | — | program_type selection: coupons, gift_card, loyalty, promotion, ewallet, promo_code, buy_x_get_y, next_order_coupons (default promotion). | N-U05-169 |
| VDR-U05-C278 | FUNCTION MAPPING REQUIRED | loyalty/models/loyalty_program.py:119 | Dictates when the points | FACT | loyalty installed | — | applies_on current/future/both: current awards a reward on the same order, future issues a coupon for later orders, both accumulates points claimable now or later. | N-U05-187 |
| VDR-U05-C279 | FUNCTION MAPPING REQUIRED | loyalty/models/loyalty_program.py:135 | trigger = fields.Selection | FACT | loyalty installed | — | trigger auto (eligible automatically) or with_code (code needed). | N-U05-187 |
| VDR-U05-C280 | FUNCTION MAPPING REQUIRED | loyalty/models/loyalty_program.py:254 | program.applies_on == 'both' | FACT | loyalty installed | — | is_nominative = applies_on both, or ewallet/loyalty with applies_on future; payment programs are gift_card and ewallet. | N-U05-187 |
| VDR-U05-C281 | FUNCTION MAPPING REQUIRED | loyalty/models/loyalty_program.py:177 | _check_max_usage | FACT | loyalty installed | — | SQL constraint: limit_usage = False OR max_usage > 0. | N-U05-192 |
| VDR-U05-C282 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/loyalty_program.py:10 | sale_ok = fields.Boolean | FACT | sale_loyalty installed | — | loyalty.program.sale_ok 'Sales' default True gates use on sale orders. | N-U05-171 |
| VDR-U05-C283 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:671 | ('active', '=', True), ('sale_ok', '=', True) | FACT | sale_loyalty installed | — | _get_program_domain: active, sale_ok, company in [order company, parent], pricelist empty or matching, date_from/date_to around the check date. | N-U05-171 |
| VDR-U05-C284 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:690 | def _get_program_timezone | FACT | sale_loyalty installed | — | Timezone is company partner tz or ir.config_parameter loyalty.timezone (default UTC). | N-U05-171 |
| VDR-U05-C285 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:705 | self.sudo().transaction_ids.filtered | FACT | sale_loyalty installed | — | Check date uses the earliest done/authorized transaction create_date converted to the program tz, else today. | N-U05-172 |
| VDR-U05-C286 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1058 | _allow_nominative_programs | FACT | sale_loyalty installed | — | _update_programs_and_rewards step 1 auto-adds the customer's ewallet cards and non-current loyalty cards with points > 0 to applied_coupon_ids. | N-U05-178 |
| VDR-U05-C287 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1075 | 'trigger', '=', 'auto' | FACT | sale_loyalty installed | — | Automatic programs not yet applied (trigger auto, rule mode auto) and not over usage limit are candidates. | N-U05-178 |
| VDR-U05-C288 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1092 | initial_coupons | FACT | sale_loyalty installed | — | Expired applied coupons are removed together with their reward lines. | N-U05-178 |
| VDR-U05-C289 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1105 | pe.coupon_id.partner_id != self.partner_id | FACT | sale_loyalty installed | — | Point entries for coupons owned by another partner are zeroed and removed. | N-U05-178 |
| VDR-U05-C290 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1179 | reward_line_pool | FACT | sale_loyalty installed | — | Step 3 resets existing reward lines (price 0, cost 0), re-derives each reward (payment programs last), reusing lines; non-applicable rewards are dropped. | N-U05-178 |
| VDR-U05-C291 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1224 | order_line_update | FACT | sale_loyalty installed | — | Step 5 deletes obsolete lines, coupons and point entries at the end to avoid cache invalidation. | N-U05-178 |
| VDR-U05-C292 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1335 | rule.reward_point_mode == 'order' | FACT | sale_loyalty installed | — | Points per rule by mode: order (flat), money (rounded down amount paid), unit (per product unit quantity). | N-U05-173 |
| VDR-U05-C293 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1301 | minimum_amount_tax_mode | FACT | sale_loyalty installed | — | Minimum amount compared with untaxed or untaxed+tax of eligible lines; then minimum quantity of eligible products. | N-U05-173 |
| VDR-U05-C294 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1314 | reward_point_split | FACT | sale_loyalty installed | — | For future-order programs with split option, points become one coupon per unit (or per money unit). | N-U05-173 |
| VDR-U05-C295 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1292 | bottomless ewallet | FACT | sale_loyalty installed | — | eWallet programs without trigger products give no points (prevents bottomless spending). | N-U05-173 |
| VDR-U05-C296 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:783 | def _get_real_points_for_coupon | FACT | sale_loyalty installed | — | Real points = coupon points (+ points the order will give unless program applies on future) minus points_cost already used on the order's lines while order not in sale. | N-U05-174 |
| VDR-U05-C297 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:975 | does not have enough points | FACT | sale_loyalty installed | — | _apply_program_reward returns errors: better global discount already applied, coupon only for future orders, not enough points. | N-U05-174 |
| VDR-U05-C298 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:581 | max_discount = min(self.amount_total, max_discount) | FACT | sale_loyalty installed | — | Discount never exceeds order amount_total or converted discount_max_amount; per_point mode limited by claimable points. | N-U05-175 |
| VDR-U05-C299 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:577 | There is nothing to discount | FACT | sale_loyalty installed | — | UserError when discountable is zero (unless a payment reward is present, then a temporary zero line is created). | N-U05-175 |
| VDR-U05-C300 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:312 | t.amount_type != 'fixed' | FACT | sale_loyalty installed | — | Fixed taxes are excluded from the discountable base. | N-U05-175 |
| VDR-U05-C301 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:638 | for tax, price in discountable_per_tax.items() | FACT | sale_loyalty installed | — | Discount lines are created per tax group with name suffix; points cost is assigned to the first line only. | N-U05-196 |
| VDR-U05-C302 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:272 | 'discount': 100 | FACT | sale_loyalty installed | — | Free product reward: product line discount 100, qty = reward_product_qty x claimable multiples, points_cost = multiples x required points (or whole wallet). | N-U05-175 |
| VDR-U05-C303 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:603 | reward_program.is_payment_program | FACT | sale_loyalty installed | — | Gift card/eWallet reward: price_unit = -min(max_discount, discountable); gift_card applies discount product taxes (mapped by fiscal position, price-included handling). | N-U05-176 |
| VDR-U05-C304 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:871 | def _best_global_discount_already_applied | FACT | sale_loyalty installed | — | Compares two global discounts; if both exceed discountable, the smaller wins; otherwise the larger wins. | N-U05-177 |
| VDR-U05-C305 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:980 | def _get_claimable_rewards | FACT | sale_loyalty installed | — | Claimable rewards per coupon excluding expired coupons, self-created future coupons, already applied non-payment discounts and inactive free products, requiring points >= required_points. | N-U05-174 |
| VDR-U05-C306 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1455 | def _try_apply_code | FACT | sale_loyalty installed | — | Code search: rule trigger (with_code) first, else loyalty.card by code; errors for invalid, expired, used, already applied, loyalty/ewallet not applicable by code. | N-U05-179 |
| VDR-U05-C307 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1504 | FOR UPDATE NOWAIT | FACT | sale_loyalty installed | — | The program row is locked FOR UPDATE NOWAIT before the usage check to force serialization failure and retry under concurrency. | N-U05-179 |
| VDR-U05-C308 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:153 | < 0 for coupon in all_coupons | FACT | sale_loyalty installed | — | action_confirm raises ValidationError 'One or more rewards on the sale order is invalid' if any coupon's real points are negative. | N-U05-180 |
| VDR-U05-C309 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:155 | order._update_programs_and_rewards() | FACT | sale_loyalty installed | — | On confirmation each order refreshes programs/rewards and writes loyalty history lines. | N-U05-180 |
| VDR-U05-C310 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:164 | pe.coupon_id.program_id.applies_on == 'current' | FACT | sale_loyalty installed | — | Coupons of current-order programs with no claimed reward are deleted at confirmation (avoid ghost coupons). | N-U05-180 |
| VDR-U05-C311 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:168 | coupon.points += change | FACT | sale_loyalty installed | — | Point changes (earned minus reward costs) are added to coupons when the order is not yet in state sale. | N-U05-185 |
| VDR-U05-C312 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:177 | Rewards Available | FACT | sale_loyalty installed | — | If one order is confirmed with claimable unapplied rewards, a notification 'Rewards Available' is returned. | N-U05-181 |
| VDR-U05-C313 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:234 | def _send_reward_coupon_mail | FACT | sale_loyalty installed | — | Reward coupons for future programs are emailed (force_send) after confirmation. | N-U05-180 |
| VDR-U05-C314 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:185 | def _action_cancel | FACT | sale_loyalty installed | — | Cancel of a confirmed order deletes loyalty history, reverses point changes on coupons, unlinks reward lines, unused non-nominative coupons and coupon point entries. | N-U05-185 |
| VDR-U05-C315 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:202 | is_reward_line | FACT | sale_loyalty installed | — | _action_cancel unlinks all reward lines of the order after super(). | N-U05-195 |
| VDR-U05-C316 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_line.py:87 | line.coupon_id and line.points_cost | FACT | sale_loyalty installed | — | Creating a reward line on a confirmed order debits the coupon and updates history immediately. | N-U05-185 |
| VDR-U05-C317 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_line.py:98 | Update our coupon points | FACT | sale_loyalty installed | — | Changing points_cost or coupon of a confirmed order line adjusts coupon points and history by the delta. | N-U05-185 |
| VDR-U05-C318 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_line.py:134 | Give back the points | FACT | sale_loyalty installed | — | Deleting a reward line also deletes its related lines (same reward, coupon, identifier) and returns points on confirmed orders. | N-U05-196 |
| VDR-U05-C319 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:137 | reward_lines.unlink() | FACT | sale_loyalty installed | — | Duplicating an order removes reward lines from the copy. | N-U05-182 |
| VDR-U05-C320 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_line.py:147 | def _can_be_edited_on_portal | FACT | sale_loyalty installed | — | Reward lines cannot be edited on the portal. | N-U05-182 |
| VDR-U05-C321 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_line.py:142 | def _sellable_lines_domain | FACT | sale_loyalty installed | — | Sellable lines domain adds reward_id = False. | N-U05-182 |
| VDR-U05-C322 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_line.py:55 | def _can_be_invoiced_alone | FACT | sale_loyalty installed | — | Reward lines are not invoiceable alone, feeding the order status rule (sale_order.py:645-657). | N-U05-191 |
| VDR-U05-C323 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/loyalty_reward.py:15 | 'invoice_policy': 'order' | FACT | sale_loyalty installed | — | Reward discount products are created with taxes_id/supplier_taxes_id False and invoice_policy order. | N-U05-190 |
| VDR-U05-C324 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/loyalty_reward.py:19 | def unlink | FACT | sale_loyalty installed | — | Deleting a single reward used on an order line archives it instead. | N-U05-183 |
| VDR-U05-C325 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_line.py:35 | _compute_tax_ids | FACT | sale_loyalty installed | — | Reward line taxes are not recomputed from the product; they are mapped through the order fiscal position. | N-U05-175 |
| VDR-U05-C326 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:100 | _add_loyalty_history_lines | FACT | sale_loyalty installed | — | History rows per coupon with issued (coupon_point_ids) and used (sum of line points_cost). | N-U05-185 |
| VDR-U05-C327 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/loyalty_card.py:9 | order_id = fields.Many2one | FACT | sale_loyalty installed | — | loyalty.card.order_id links a coupon to the sales order that generated it; use_count adds order lines using it. | N-U05-186 |
| VDR-U05-C328 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/loyalty_card.py:49 | def action_archive | FACT | sale_loyalty installed | — | Archiving a card deletes its coupon point entries on draft orders. | N-U05-178 |
| VDR-U05-C329 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/loyalty_program.py:12 | def _compute_order_count | FACT | sale_loyalty installed | — | Program order_count counts each order once per program using its rewards; total_order_count adds it. | N-U05-186 |
| VDR-U05-C330 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1507 | program.total_order_count >= program.max_usage | FACT | sale_loyalty installed | — | Code application refused when usage limit reached; automatic programs filtered by total_order_count < max_usage. | N-U05-186 |
| VDR-U05-C331 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order_coupon_points.py:15 | UNIQUE (order_id, coupon_id) | FACT | sale_loyalty installed | — | sale.order.coupon.points unique per (order, coupon); cascade on order or coupon deletion. | N-U05-193 |
| VDR-U05-C332 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1542 | if self.amount_total or not self.reward_amount | FACT | sale_loyalty installed | — | _validate_order: zero-total order with reward amount and automatic invoicing creates a final invoice, posts and mails it. | N-U05-184 |
| VDR-U05-C333 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:761 | def _recompute_prices | FACT | sale_loyalty installed | — | Recomputing prices re-runs program/reward update when reward lines exist. | N-U05-178 |
| VDR-U05-C334 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/account_move_line.py:9 | def _get_discount_lines | FACT | sale_loyalty installed | — | Invoice lines linked to discount rewards are classified as discount lines for accounting presentation. | N-U05-190 |
| VDR-U05-C335 | FUNCTION MAPPING REQUIRED | sale_loyalty/views/sale_order_views.xml:27 | invisible="locked or state == 'cancel'" | FACT | sale_loyalty installed | — | Coupon Code and Reward buttons are active when order is neither locked nor cancelled; disabled twins otherwise. | N-U05-188 |
| VDR-U05-C336 | FUNCTION MAPPING REQUIRED | sale_loyalty/wizard/sale_loyalty_coupon_wizard.py:19 | status = self.order_id._try_apply_code | FACT | sale_loyalty installed | — | Coupon wizard applies a code, raising ValidationError with the error message, then opens the reward selection wizard. | N-U05-188 |
| VDR-U05-C337 | FUNCTION MAPPING REQUIRED | sale_loyalty/wizard/sale_loyalty_reward_wizard.py:41 | def action_apply | FACT | sale_loyalty installed | — | Reward wizard applies the selected reward with its coupon, updates programs and removes unused coupons. | N-U05-188 |
| VDR-U05-C338 | FUNCTION MAPPING REQUIRED | sale_loyalty/security/ir.model.access.csv:2 | access_program_salesman | FACT | sale_loyalty installed | — | ACL: salesman read on program/rule/reward, read+write on card and history, wizards RWC; manager full on program/rule/reward and coupon points; base loyalty grants internal users no rights. | N-U05-189 |
| VDR-U05-C339 | FUNCTION MAPPING REQUIRED | sale_loyalty/security/ir.model.access.csv:2 | access_program_salesman | OBSERVATION | restored DB | — | Restored DB: loyalty.program/card/reward/rule have global multi-company rules ('company_id in company_ids + [False]' or parent_of) and ACL names match the CSV. | N-U05-189 |
| VDR-U05-C340 | FUNCTION MAPPING REQUIRED | loyalty/models/loyalty_program.py:95 | program_type = fields.Selection | OBSERVATION | restored DB | — | Restored DB: 1 loyalty_program (gift_card, applies_on future, trigger auto), 1 reward, 1 rule, 0 cards, 0 orders; config parameter loyalty.compute_all_discount_product_ids = False. | N-U05-199 |
| VDR-U05-C341 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:128 | _get_no_effect_on_threshold_lines | UNKNOWN | runtime | RT | Installed sale_loyalty_delivery extends threshold exclusions for delivery lines; not read (DISCOVERED SUPPORTING MODULE). | N-U05-198 |
| VDR-U05-C342 | FUNCTION MAPPING REQUIRED | sale_crm/models/sale_order.py:10 | opportunity_id = fields.Many2one | FACT | sale_crm installed | — | sale.order.opportunity_id links to crm.lead (opportunity, company check). | N-U05-202 |
| VDR-U05-C343 | FUNCTION MAPPING REQUIRED | sale_crm/models/crm_lead.py:16 | def _compute_sale_data | FACT | sale_crm installed | — | Lead sale_amount_total (untaxed, confirmed orders converted to company currency), quotation_count (draft/sent), sale_order_count (not draft/sent/cancel). | N-U05-202 |
| VDR-U05-C344 | FUNCTION MAPPING REQUIRED | sale_crm/models/crm_lead.py:75 | ('state', 'not in', ('draft', 'sent', 'cancel')) | FACT | sale_crm installed | — | Confirmed-order domain is state not in draft/sent/cancel. | N-U05-202 |
| VDR-U05-C345 | FUNCTION MAPPING REQUIRED | sale_crm/models/sale_order.py:17 | _update_revenues_from_so | FACT | sale_crm installed | — | action_confirm calls opportunity._update_revenues_from_so(order) for each order after super(). | N-U05-203 |
| VDR-U05-C346 | FUNCTION MAPPING REQUIRED | sale_crm/models/crm_lead.py:106 | order.amount_untaxed | FACT | sale_crm installed | — | Expected revenue is raised only if lower than untaxed amount and order currency equals company currency; log 'Expected revenue has been updated based on the linked Sales Orders'. | N-U05-203 |
| VDR-U05-C347 | FUNCTION MAPPING REQUIRED | sale_crm/models/crm_lead.py:82 | 'default_opportunity_id': self.id | FACT | sale_crm installed | — | Quotation context copies campaign, medium, source, tags, origin (lead name), company, team and salesperson. | N-U05-204 |
| VDR-U05-C348 | FUNCTION MAPPING REQUIRED | sale_crm/wizard/crm_opportunity_to_quotation.py:36 | ('create', 'Create a new customer') | FACT | sale_crm installed | — | crm.quotation.partner wizard offers create customer, link existing, or do not link. | N-U05-204 |
| VDR-U05-C349 | FUNCTION MAPPING REQUIRED | sale_crm/models/crm_lead.py:100 | fields_info['order_ids'] | FACT | sale_crm installed | — | Merging leads re-attaches all orders to the merged lead. | N-U05-205 |
| VDR-U05-C350 | FUNCTION MAPPING REQUIRED | sale_crm/security/ir.model.access.csv:2 | access_crm_quotation_partner | FACT | sale_crm installed | — | Only ACL: crm.quotation.partner for sales_team.group_sale_salesman RWC; no record rules or crons in sale_crm. | N-U05-223 |
| VDR-U05-C351 | FUNCTION MAPPING REQUIRED | sale_purchase/models/product_template.py:11 | service_to_purchase = fields.Boolean | FACT | sale_purchase installed | — | service_to_purchase 'Subcontract Service' is company_dependent, copy=False. | N-U05-221 |
| VDR-U05-C352 | FUNCTION MAPPING REQUIRED | sale_purchase/models/product_template.py:19 | template.type != 'service' | FACT | sale_purchase installed | — | Constraint: flagged products must be type service ('Product that is not a service can not create RFQ') and have vendors. | N-U05-206 |
| VDR-U05-C353 | FUNCTION MAPPING REQUIRED | sale_purchase/models/product_template.py:32 | Please define the vendor | FACT | sale_purchase installed | — | ValidationError if flagged without seller_ids. | N-U05-225 |
| VDR-U05-C354 | FUNCTION MAPPING REQUIRED | sale_purchase/models/product_template.py:36 | p.type != 'service' | FACT | sale_purchase installed | — | Onchange clears the flag when type is not service or re-invoice policy is set. | N-U05-206 |
| VDR-U05-C355 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order.py:23 | _purchase_service_generation | FACT | sale_purchase installed | — | SaleOrder._action_confirm calls order_line.sudo()._purchase_service_generation() after super. | N-U05-211 |
| VDR-U05-C356 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:303 | line.product_id.service_to_purchase and not line.purchase_line_count | FACT | sale_purchase installed | — | Generation only for flagged products with no earlier purchase line (so cancel/reset/reconfirm does not duplicate). | N-U05-207 |
| VDR-U05-C357 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:47 | not line.is_expense | FACT | sale_purchase installed | — | New lines created on a confirmed order generate purchase lines unless they are expense lines. | N-U05-211 |
| VDR-U05-C358 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:224 | suppliers = self.product_id._select_seller | FACT | sale_purchase installed | — | Vendor = first result of product._select_seller for quantity and UoM (partner from _retrieve_purchase_partner, base False); UserError if none. | N-U05-225 |
| VDR-U05-C359 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:226 | There is no vendor associated | FACT | sale_purchase installed | — | UserError 'There is no vendor associated to the product ... Please define a vendor'. | N-U05-225 |
| VDR-U05-C360 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:232 | def _purchase_service_match_purchase_order | FACT | sale_purchase installed | — | Reuses a draft PO of the same vendor and company whose line comes from the same sale order (domain sale_order_id), else creates a PO. | N-U05-207 |
| VDR-U05-C361 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:283 | purchase_order.write({'origin' | FACT | sale_purchase installed | — | The SO name is appended to the PO origin if not present. | N-U05-212 |
| VDR-U05-C362 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:132 | 'partner_id': partner_supplier.id | FACT | sale_purchase installed | — | PO values: vendor, partner_ref, company, vendor purchase currency (or company), origin, vendor payment term, date_order = commitment date (or now) minus supplierinfo delay, vendor fiscal position. | N-U05-208 |
| VDR-U05-C363 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:206 | purchase_line_vals = { | FACT | sale_purchase installed | — | PO line values: name, qty in vendor UoM, product, price from supplierinfo with tax-included fix and currency conversion, date_planned, mapped supplier taxes, sale_line_id, vendor discount, analytic distribution. | N-U05-208 |
| VDR-U05-C364 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:107 | last_purchase_line.state in ['draft', 'sent', 'to approve'] | FACT | sale_purchase installed | — | Quantity increase: update the latest PO line if draft/sent/to approve; if purchase/cancel create a new PO line for the difference. | N-U05-209 |
| VDR-U05-C365 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:75 | def _purchase_decrease_ordered_qty | FACT | sale_purchase installed | — | Quantity decrease only schedules a warning activity on related PO(s); onchange also warns. | N-U05-227 |
| VDR-U05-C366 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order.py:31 | _activity_cancel_on_purchase | FACT | sale_purchase installed | — | Order cancel (sudo) schedules a warning activity on each non-cancelled PO line's PO for service_to_purchase products. | N-U05-210 |
| VDR-U05-C367 | FUNCTION MAPPING REQUIRED | sale_purchase/models/purchase_order.py:57 | _activity_cancel_on_sale | FACT | sale_purchase installed | — | PO button_cancel schedules a warning activity on originating SOs. | N-U05-210 |
| VDR-U05-C368 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order.py:23 | order.order_line.sudo() | FACT | sale_purchase installed | — | Purchase generation runs in sudo; sale_purchase ships no security files (no ACL/rules/crons). | N-U05-229 |
| VDR-U05-C369 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order.py:13 | groups='purchase.group_purchase_user' | FACT | sale_purchase installed | — | purchase_order_count on the SO is visible only to purchase.group_purchase_user. | N-U05-223 |
| VDR-U05-C370 | FUNCTION MAPPING REQUIRED | sale_mrp/models/sale_order.py:20 | stock_reference_ids.production_ids | FACT | sale_mrp installed | — | SO mrp_production_ids = first-level MOs (no parent production group) of the order's stock references, not cancelled, with active picking type. | N-U05-215 |
| VDR-U05-C371 | FUNCTION MAPPING REQUIRED | sale_mrp/models/sale_order_line.py:66 | elif boms | FACT | sale_mrp installed | — | If no relevant phantom BoM matches the sold product, delivered = ordered only when all moves are done to customer, else 0. | N-U05-213 |
| VDR-U05-C372 | FUNCTION MAPPING REQUIRED | sale_mrp/models/sale_order_line.py:60 | _compute_kit_quantities | FACT | sale_mrp installed | — | Kit delivered qty is computed with _compute_kit_quantities from component moves and added to delivered_qties. | N-U05-213 |
| VDR-U05-C373 | FUNCTION MAPPING REQUIRED | sale_mrp/models/mrp_production.py:14 | sale_line_id = fields.Many2one | FACT | sale_mrp installed | — | mrp.production.sale_line_id (origin sale order line); MO confirm links finished moves of the product to that line; backorder MO copies it. | N-U05-214 |
| VDR-U05-C374 | FUNCTION MAPPING REQUIRED | sale_mrp/models/stock_rule.py:9 | values.get('sale_line_id') | FACT | sale_mrp installed | — | stock.rule copies sale_line_id into MO values and bom_line_id into component moves of kit lines. | N-U05-214 |
| VDR-U05-C375 | FUNCTION MAPPING REQUIRED | sale_mrp/security/ir.model.access.csv:3 | access_sale_order_manufacturing_user | FACT | sale_mrp installed | — | mrp users get read/write on sale.order and sale.order.line; salesmen get read on BoMs, RWC on productions. | N-U05-223 |
| VDR-U05-C376 | FUNCTION MAPPING REQUIRED | sale_mrp/models/account_move.py:9 | _get_sale_stock_move | FACT | sale_mrp installed | — | MO finished-goods moves linked to the SO line are excluded from COGS-related sale stock moves (hand-off U10). | N-U05-223 |
| VDR-U05-C377 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order.py:138 | def _action_confirm | FACT | sale_project installed | — | _action_confirm generates project/task for service lines (sudo, per company) unless context disable_project_task_generation, then super. | N-U05-216 |
| VDR-U05-C378 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:336 | def _timesheet_service_generation | FACT | sale_project installed | — | Only service lines with service_tracking project_only/task_in_project/task_global_project and not optional-zero are processed; existing project/task are reused. | N-U05-216 |
| VDR-U05-C379 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order.py:35 | project_id = fields.Many2one | FACT | sale_project installed | — | sale.order.project_id domain allow_billable and not template; used for task generation and analytic reference. | N-U05-226 |
| VDR-U05-C380 | FUNCTION MAPPING REQUIRED | sale_project/models/product_template.py:96 | 'delivered_manual': ('delivery', 'manual') | FACT | sale_project installed | — | Service policy to billing basis map (see CAP-U05-01). | N-U05-217 |
| VDR-U05-C381 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:100 | delivered_qties[line] = reached_milestones_per_sol | FACT | sale_project installed | — | Delivered quantity for milestone lines = reached percentage x ordered qty. | N-U05-217 |
| VDR-U05-C382 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order_line.py:68 | line.qty_delivered_method = 'timesheet' | FACT | sale_timesheet installed | — | Service products with service_type timesheet get delivered quantity from timesheets. | N-U05-217 |
| VDR-U05-C383 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order.py:107 | sol.product_id.service_policy == 'ordered_prepaid' | FACT | sale_timesheet installed | — | Prepaid service lines whose delivered qty exceeds ordered x threshold (default 1.0) and not yet warned raise the upsell activity. | N-U05-217 |
| VDR-U05-C384 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/account_move.py:79 | self.filtered(lambda i: i.move_type | FACT | sale_timesheet installed | — | Timesheets (project set, unbilled, in period) of delivery/timesheet service lines are linked to draft invoice (timesheet_invoice_id). | N-U05-218 |
| VDR-U05-C385 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/account_move.py:107 | timesheets_sudo.write({'timesheet_invoice_id': False}) | FACT | sale_timesheet installed | — | Posting a credit note clears timesheet_invoice_id of the credited invoice's timesheets. | N-U05-218 |
| VDR-U05-C386 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:467 | self.task_id.project_id.account_id | FACT | sale_project installed | — | _prepare_invoice_line adds analytic distribution from the task project, line project, or single project account when line has none. | N-U05-219 |
| VDR-U05-C387 | FUNCTION MAPPING REQUIRED | sale_project/security/ir.model.access.csv:2 | access_sale_order_line_project_manager | FACT | sale_project installed | — | Project managers/users get read on sale.order(.line); rule restricts project managers to confirmed service lines with project or task. | N-U05-223 |
| VDR-U05-C388 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order.py:138 | def _action_confirm | UNKNOWN | runtime | RT | No _action_cancel override was found in sale_project/sale_timesheet models (grep of _action_cancel and cancel returns only sale/sale_stock/sale_purchase/sale_loyalty); effect on projects/tasks of cancelling an order is therefore not defined in these modules. | N-U05-230 |
| VDR-U05-C389 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:227 | return suppliers[0] | UNKNOWN | runtime | RT | Only suppliers[0] is used; criteria behind _select_seller ordering (sequence, min qty, date validity, price) live in purchase/product modules and were not read. | N-U05-231 |
| VDR-U05-C390 | FUNCTION MAPPING REQUIRED | sale_purchase_stock/models/sale_order.py:11 | _compute_purchase_order_count | FACT | sale_purchase_stock installed (DISCOVERED SUPPORTING MODULE) | — | sale_purchase_stock (depends sale_stock, purchase_stock, sale_purchase) extends order/PO counts and procurement-created PO linkage; noted only. | N-U05-224 |
| VDR-U05-C391 | FUNCTION MAPPING REQUIRED | sale_crm/__manifest__.py:28 | 'auto_install': True | OBSERVATION | restored DB | — | Restored DB: sale_crm, sale_purchase, sale_purchase_stock, sale_mrp, sale_project, sale_timesheet, sale_stock, sale_loyalty, sale_management, sale_margin etc. are installed; pos_sale and website_sale are not. | N-U05-223 |
| VDR-U05-C392 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:32 | access_sale_order, | FACT | sale installed | — | sale.order ACL for group_sale_salesman: read, write, create; no unlink. | N-U05-234 |
| VDR-U05-C393 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:33 | access_sale_order_manager | FACT | sale installed | — | sale.order ACL for group_sale_manager: full CRUD. | N-U05-234 |
| VDR-U05-C394 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:39 | access_sale_order_line, | FACT | sale installed | — | sale.order.line ACL for salesman: full CRUD (deletion further gated by _unlink_except_confirmed). | N-U05-234 |
| VDR-U05-C395 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:30 | access_sale_order_invoicing_payments | FACT | sale installed | — | account.group_account_invoice: read, write on sale.order (no create/unlink); same on lines (line 37). | N-U05-236 |
| VDR-U05-C396 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:31 | access_sale_order_accountant | FACT | sale installed | — | account.group_account_user: read, write on sale.order and lines; account.group_account_readonly: read only (lines 29, 36). | N-U05-236 |
| VDR-U05-C397 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:28 | access_sale_order_portal | FACT | sale installed | — | base.group_portal: read only on sale.order and lines (portal rule lists write/unlink flags True but ACL does not grant them). | N-U05-236 |
| VDR-U05-C398 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:8 | access_account_move_salesman | FACT | sale installed | — | Salesman has read-only ACL on account.move, account.move.line, account.partial.reconcile, journals, payment terms, taxes, tax groups, accounts. | N-U05-237 |
| VDR-U05-C399 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:45 | access_sale_mass_cancel_orders | FACT | sale installed | — | sale.mass.cancel.orders wizard: salesman read/write/create; rule restricts to create_uid. | N-U05-239 |
| VDR-U05-C400 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:181 | sale_mass_cancel_orders_rule | FACT | sale installed | — | Global rule: create_uid = user.id for the mass cancel wizard. | N-U05-239 |
| VDR-U05-C401 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:5 | sale_order_comp_rule | FACT | sale installed | — | Global multi-company rule: company_id in company_ids on sale.order, sale.order.line (line 11) and sale.report (line 17). | N-U05-240 |
| VDR-U05-C402 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:44 | sale_order_personal_rule | FACT | sale installed | — | Salesman group rule: user_id = user or no user; all-leads group rule: (1,'=',1) (line 50). Lines use salesman_id (line 71, 78). | N-U05-235 |
| VDR-U05-C403 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:24 | sale_order_rule_portal | FACT | sale installed | — | Portal rule: partner_id child_of user's commercial partner; lines by order partner. | N-U05-236 |
| VDR-U05-C404 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:118 | account_invoice_rule_see_personal | FACT | sale installed | — | Salesman sees account.move of out_invoice/out_refund where invoice_user_id is self or empty; all-leads sees all customer invoices; same pattern on move lines, send wizards and invoice report. | N-U05-235 |
| VDR-U05-C405 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:101 | payment_transaction_salesman_rule | FACT | sale installed | — | Salesman rule resets payment.transaction domain to [(1,'=',1)]; same for payment tokens. | N-U05-244 |
| VDR-U05-C406 | FUNCTION MAPPING REQUIRED | sale_stock/security/ir.model.access.csv:2 | access_stock_picking_salesman | FACT | sale_stock installed | — | Salesman: RWC on stock.picking and stock.move; read on warehouse, location, orderpoint, rule, package type; manager: full on picking/move/rule. | N-U05-238 |
| VDR-U05-C407 | FUNCTION MAPPING REQUIRED | sale_stock/security/ir.model.access.csv:5 | access_sale_order_stock_worker | FACT | sale_stock installed | — | stock.group_stock_user: read/write on sale.order and sale.order.line; rule gives them all lines for read. | N-U05-238 |
| VDR-U05-C408 | FUNCTION MAPPING REQUIRED | sale_stock/security/sale_stock_security.xml:6 | stock_picking_rule_portal | FACT | sale_stock installed | — | Portal followers see pickings where partner is user partner or the order partner. | N-U05-236 |
| VDR-U05-C409 | FUNCTION MAPPING REQUIRED | sale/security/res_groups.xml:4 | group_auto_done_setting | FACT | sale installed | — | sale defines feature groups: Lock Confirmed Sales, Discount on lines, Warning (sale), Pro-forma Invoices; set by settings through implied_group. | N-U05-249 |
| VDR-U05-C410 | FUNCTION MAPPING REQUIRED | sale/wizard/res_config_settings.py:21 | implied_group='sale.group_auto_done_setting' | FACT | sale installed | — | Settings toggles group_auto_done_setting, group_discount_per_so_line, group_warning_sale, group_proforma_sales via implied_group. | N-U05-249 |
| VDR-U05-C411 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:78 | locked = fields.Boolean | FACT | sale installed | — | locked: 'Locked orders cannot be modified.' default False, copy False, tracked. | N-U05-241 |
| VDR-U05-C412 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1203 | _is_feature_enabled('sale.group_auto_done_setting') | FACT | sale installed | — | _should_be_locked tests whether the superuser has the feature group; action_confirm locks if true. | N-U05-241 |
| VDR-U05-C413 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1323 | def action_unlock | FACT | sale installed | — | action_lock/action_unlock simply write locked with no group check in code. | N-U05-255 |
| VDR-U05-C414 | FUNCTION MAPPING REQUIRED | sale/views/sale_order_views.xml:351 | groups="sales_team.group_sale_manager" | FACT | sale installed | — | Unlock (and Lock) buttons restricted to sales managers at view level only. | N-U05-241 |
| VDR-U05-C415 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1439 | 'product_id', 'name', 'price_unit' | FACT | sale installed | — | Protected fields on locked orders: product_id, name, price_unit, product_uom_id, product_uom_qty, tax_ids, analytic_distribution, discount; error lists them. | N-U05-252 |
| VDR-U05-C416 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1329 | You cannot cancel a locked order | FACT | sale installed | — | action_cancel refuses locked orders; mass cancel bypasses (CAP-U05-05 claim d.mass_cancel). | N-U05-254 |
| VDR-U05-C417 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1039 | can not delete a sent quotation | FACT | sale installed | — | Unlink allowed only in draft or cancel state. | N-U05-252 |
| VDR-U05-C418 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1044 | pricelist of a confirmed order | FACT | sale installed | — | write refuses pricelist_id change on orders in state sale. | N-U05-252 |
| VDR-U05-C419 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1396 | modify the product of this | FACT | sale installed | — | write refuses product change when product_updatable is False (invoiced, delivered, locked, advance, service lines with project). | N-U05-252 |
| VDR-U05-C420 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1484 | can't remove one of its lines | FACT | sale installed | — | Deleting a confirmed order line is refused; set quantity to 0 instead. | N-U05-252 |
| VDR-U05-C421 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1426 | forbidden to modify the following | FACT | sale installed | — | Writing protected fields on a locked order raises UserError. | N-U05-252 |
| VDR-U05-C422 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:114 | elif sale_order.locked | FACT | sale installed | — | Expense re-invoicing raises UserError if the target order is draft/sent, cancelled or locked. | N-U05-252 |
| VDR-U05-C423 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:39 | _check_company_auto = True | FACT | sale installed | — | sale.order and sale.order.line enforce company consistency of related records. | N-U05-242 |
| VDR-U05-C424 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:852 | invalid_companies | FACT | sale installed | — | Constraint: products of order lines must belong to the order company (or accessible branches). | N-U05-243 |
| VDR-U05-C425 | FUNCTION MAPPING REQUIRED | sale/models/product_template.py:109 | def _check_sale_product_company | FACT | sale installed | — | Constraint blocks restricting a product to a company if it was used on orders outside that company. | N-U05-243 |
| VDR-U05-C426 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1446 | 'company_id': self.company_id.id | FACT | sale installed | — | Invoice company equals order company; company is a grouping key so no cross-company merge (CAP-U05-02). | N-U05-242 |
| VDR-U05-C427 | FUNCTION MAPPING REQUIRED | sale/data/ir_cron.xml:4 | send_invoice_cron | FACT | sale installed | — | ir.cron 'automatic invoicing: send ready invoice' on model payment.transaction, code model._cron_send_invoice(), every 1 day, active False, user root. | N-U05-245 |
| VDR-U05-C428 | FUNCTION MAPPING REQUIRED | sale/const.py:6 | 'sale.automatic_invoice': 'sale.send_invoice_cron' | FACT | sale installed | — | PARAM_CRON_MAPPING maps config parameter sale.automatic_invoice to the cron and sale.async_emails to the pending-emails cron. | N-U05-245 |
| VDR-U05-C429 | FUNCTION MAPPING REQUIRED | sale/models/ir_config_parameter.py:27 | def _sale_sync_linked_crons | FACT | sale installed | — | On create/write/unlink of the parameters the linked cron's active = str2bool(value) (False on unlink). | N-U05-245 |
| VDR-U05-C430 | FUNCTION MAPPING REQUIRED | sale/__init__.py:21 | str2bool(env['ir.config_parameter'].get_param(param, 'False')) | FACT | sale installed | — | post_init_hook synchronizes crons from parameters (default 'False'). | N-U05-245 |
| VDR-U05-C431 | FUNCTION MAPPING REQUIRED | sale/wizard/res_config_settings.py:38 | config_parameter='sale.automatic_invoice' | FACT | sale installed | — | Settings field automatic_invoice (Boolean) stores config parameter sale.automatic_invoice; help text describes invoice generated and marked paid when payment confirmed. | N-U05-246 |
| VDR-U05-C432 | FUNCTION MAPPING REQUIRED | sale/wizard/res_config_settings.py:126 | sale.automatic_invoice | FACT | sale installed | — | set_values writes sale.automatic_invoice=False when default_invoice_policy != 'order'. | N-U05-246 |
| VDR-U05-C433 | FUNCTION MAPPING REQUIRED | sale/models/payment_transaction.py:184 | if not self.env['ir.config_parameter'].sudo().get_param('sale.automatic_invoice') | INFERENCE | sale installed | — | _cron_send_invoice returns immediately if the parameter is falsy ; get_param returns the stored string, and a stored 'False' string is truthy in Python, so the guard alone would not stop the body (lines 184-185) - the effective switch is the cron active flag set by the sync (ir_config_parameter.py:27-45). | N-U05-250 |
| VDR-U05-C434 | FUNCTION MAPPING REQUIRED | sale/models/payment_transaction.py:190 | self.search([ | FACT | sale installed | — | Searches transactions state done, is_post_processed, with unsent posted invoices, order state sale, last_state_change within 2 days, then _send_invoice(). | N-U05-250 |
| VDR-U05-C435 | FUNCTION MAPPING REQUIRED | sale/models/payment_transaction.py:164 | 'allow_raising': False, 'allow_fallback_pdf': True | FACT | sale installed | — | _send_invoice runs as superuser, marks invoice is_move_sent, uses default template from parameter sale.default_invoice_email_template and account.move.send._generate_and_send_invoices. | N-U05-250 |
| VDR-U05-C436 | FUNCTION MAPPING REQUIRED | sale/models/account_move.py:154 | send_invoice_cron._trigger() | FACT | sale installed | — | account.move._action_invoice_ready_to_be_sent triggers the cron whenever an invoice becomes ready to send. | N-U05-257 |
| VDR-U05-C437 | FUNCTION MAPPING REQUIRED | sale/models/payment_transaction.py:99 | if auto_invoice and not self.env.context.get('skip_sale_auto_invoice_send') | FACT | sale installed | — | In _post_process, with automatic invoice: when sale.async_emails and cron exist the cron is triggered, else _send_invoice is called directly. | N-U05-246 |
| VDR-U05-C438 | FUNCTION MAPPING REQUIRED | sale/data/ir_cron.xml:15 | send_pending_emails_cron | FACT | sale installed | — | Cron 'Sales: Send pending emails' (model sale.order, _cron_send_pending_emails) inactive by default; controlled by sale.async_emails. | N-U05-247 |
| VDR-U05-C439 | FUNCTION MAPPING REQUIRED | sale/models/payment_transaction.py:97 | done_tx._invoice_sale_orders() | FACT | automatic invoice parameter true | — | When automatic invoicing is on, a done transaction creates invoices (final for fully paid, advance for partly paid), posts them in super()._post_process and sends them. | N-U05-246 |
| VDR-U05-C440 | FUNCTION MAPPING REQUIRED | account/data/service_cron.xml:14 | Send invoices automatically | FACT | account installed (supporting) | — | The account module's own cron 'Send invoices automatically' (_cron_account_move_send) is distinct from the sale cron. | N-U05-248 |
| VDR-U05-C441 | FUNCTION MAPPING REQUIRED | sale/data/ir_cron.xml:4 | send_invoice_cron | OBSERVATION | restored DB | — | Restored DB ir_cron: id 22 'automatic invoicing: send ready invoice' active=false (daily); id 23 'Sales: Send pending emails' active=false; id 18 'Send invoices automatically' (account) active=true; ir_config_parameter has no sale.automatic_invoice row and sale.async_emails=False. | N-U05-245 |
| VDR-U05-C442 | FUNCTION MAPPING REQUIRED | sale/security/res_groups.xml:4 | group_auto_done_setting | OBSERVATION | restored DB | — | Restored DB: base.group_user implies sale feature groups 38 (lock), 39 (discount), 40 (warning), 41 (pro-forma) i.e. these settings are enabled; no direct user memberships in them. | N-U05-253 |
| VDR-U05-C443 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:32 | access_sale_order, | OBSERVATION | restored DB | — | Restored DB ACL for sale.order includes: Administrator 1111, User: Own Documents Only 1110, Invoicing 1100, Show Full Accounting 1100, Show Accounting Readonly 1000, Portal 1000, plus rows from other modules (manufacturing/stock user 1100, project user/manager 1000); sale.order.line User: Own Documents Only 1111; matches the CSV. | N-U05-234 |
| VDR-U05-C444 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:5 | sale_order_comp_rule | OBSERVATION | restored DB | — | Restored DB ir_rule rows match XML for sale.order (multi-company, personal, all, portal 1101), sale.order.line (multi-company, personal, all, portal, stock user 1000, project manager 1000), wizard and mass-cancel rules, and account.move personal/all invoice rules. | N-U05-235 |
| VDR-U05-C445 | FUNCTION MAPPING REQUIRED | sale/security/ir.model.access.csv:32 | access_sale_order, | UNKNOWN | runtime | RT | Actual users' memberships were not examined (no user data queried); effective permissions per person cannot be stated. | N-U05-258 |
| VDR-U05-C446 | SDV-F04 | sale/models/product_template.py:47 | Invoice quantities delivered to | FACT | sale installed | — | Field help text defines the two bases: 'Ordered Quantity: Invoice quantities ordered by the customer. Delivered Quantity: Invoice quantities delivered to the customer.' | N-U05-001 |
| VDR-U05-C447 | SDV-F04 | sale/models/sale_order_line.py:1107 | line.invoice_status = 'to invoice' | FACT | sale installed | — | A non-zero qty_to_invoice (derived from the policy) sets the line to 'to invoice', which the order aggregates into its own status. | N-U05-002 |
| VDR-U05-C448 | SDV-F04 | sale/models/product_template.py:80 | Invoice after delivery | FACT | sale installed | — | Tooltip text for delivery policy on non-goods and for order policy on services states the intended business use of each basis. | N-U05-003 |
| VDR-U05-C449 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:12 | sale_line_ids = fields.Many2many | INFERENCE | sale installed | — | The many2many link between invoice lines and order lines (readonly, copy False) is the only traceability from an invoiced amount to its order line; invoice_lines on the order line is the reverse side (sale_order_line.py:257-261). | N-U05-027 |
| VDR-U05-C450 | FUNCTION MAPPING REQUIRED | sale/views/sale_order_views.xml:994 | name="to_invoice" | FACT | sale installed | — | The search view has a 'To Invoice' filter on invoice_status = 'to invoice' and list/form decorations by invoice_status values (lines 155-170), forming the worklist. | N-U05-028 |
| VDR-U05-C451 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1484 | 'partner_shipping_id' | INFERENCE | sale installed | — | Because partner_shipping_id is part of the grouping keys (line 1484), orders of one customer with different delivery contacts stay on separate invoices. | N-U05-054 |
| VDR-U05-C452 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:1588 | def _get_downpayment_line_price_unit | INFERENCE | sale installed | — | The advance line price is rebuilt from posted invoice lines of the advance (signed by move type) excluding other invoices, so the order remembers the prepaid total to deduct (cited with sale/models/account_move.py:93). | N-U05-060 |
| VDR-U05-C453 | FUNCTION MAPPING REQUIRED | account/models/account_tax.py:3999 | _prepare_base_lines_for_down_payment | UNKNOWN | runtime | RT | How percentage advances behave when the order mixes taxes that cannot be discounted (fixed taxes) needs execution; only the dispatching helper was read. | N-U05-086 |
| VDR-U05-C454 | SDV-F07 | sale/models/sale_order_line.py:1024 | elif invoice_line.move_id.move_type == 'out_refund' | INFERENCE | sale installed | — | qty_invoiced falls for out_refund lines (1024-1025) and qty_delivered falls for refundable returns (sale_stock/sale_order_line.py:209-218): both sides move so the order shows what remains. | N-U05-087 |
| VDR-U05-C455 | SDV-F06 | sale_stock/models/sale_order_line.py:209 | for move in incoming_moves | INFERENCE | sale_stock installed | — | Return route lowers qty_delivered (sale_stock) while credit-note route lowers qty_invoiced (sale); the two are independent computations with no cross-check in the lines read. | N-U05-088 |
| VDR-U05-C456 | SDV-F07 | sale/models/sale_order_line.py:1072 | line.qty_delivered - line.qty_invoiced | INFERENCE | sale installed | — | Order stays consistent through the same cumulative formula after either route, which is the business purpose of feeding corrections back. | N-U05-089 |
| VDR-U05-C457 | SDV-F06 | sale_stock/models/sale_order_line.py:212 | not move.origin_returned_move_id | INFERENCE | sale_stock installed | — | After a flagged return on a delivery-basis line qty_delivered drops below qty_invoiced so qty_to_invoice < 0 and the line is 'to invoice' (line status test sale_order_line.py:1106). | N-U05-102 |
| VDR-U05-C458 | SDV-F07 | account/models/account_move.py:5495 | def _reverse_moves | FACT | account installed (supporting) | — | Reversal/credit-note creation is implemented in account (_reverse_moves); sale only extends it for UTM fields (sale/models/account_move.py:71-81). | N-U05-105 |
| VDR-U05-C459 | SDV-F06 | sale_stock/models/sale_order_line.py:364 | elif move.to_refund and | INFERENCE | sale_stock installed | — | Incoming moves count as returns only when to_refund; a return with to_refund False leaves qty_delivered unchanged so no credit signal arises on the order. | N-U05-110 |
| VDR-U05-C460 | SDV-F07 | sale_stock/models/account_move.py:14 | _stock_account_get_last_step_stock_moves | UNKNOWN | runtime | RT | Accounting entries for credit notes on stock-valued goods are produced in stock_account/account (hand-off U10/U11); not studied here. | N-U05-113 |
| VDR-U05-C461 | SDV-F02 | sale_stock/models/sale_order.py:213 | def _action_confirm | INFERENCE | sale_stock installed | — | Procurement is launched inside the confirmation action itself, so sales needs no separate hand-off to warehouse; delivered quantity returns through stored dependencies. | N-U05-116 |
| VDR-U05-C462 | PDT-F01 | sale/models/sale_order_line.py:1020 | invoice_line.move_id.state != 'cancel' | INFERENCE | sale installed | — | Counting all non-cancelled invoice lines in qty_invoiced prevents double billing and, with cumulative qty_delivered, leaves delivered-but-unbilled quantities visible as qty_to_invoice (lines 1069-1072). | N-U05-147 |
| VDR-U05-C463 | PDT-F04 | sale_project/models/sale_order_line.py:85 | def _prepare_qty_delivered | FACT | sale_project installed | — | Source of delivered quantity depends on the line's method (stock_move, analytic, timesheet, milestones, manual) selected from product type and installed modules. | N-U05-160 |
| VDR-U05-C464 | PDT-F04 | sale_timesheet/models/sale_order_line.py:70 | analytic_line_ids.project_id | FACT | sale_timesheet installed | — | Timesheet/milestone delivered quantity compute depends on analytic lines and project data from project/timesheet modules, while stock-move delivered quantity depends on stock moves (sale_stock/sale_order_line.py:195). | N-U05-161 |
| VDR-U05-C465 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1045 | def _update_programs_and_rewards | INFERENCE | sale_loyalty installed | — | Docstring: update points of applied programs, check automatic programs, update applied rewards; together with reward generation methods this is the whole 'add reward lines, give points, pay with gift card' behavior. | N-U05-168 |
| VDR-U05-C466 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:549 | 'product_id': reward_product.id | INFERENCE | sale_loyalty installed | — | Reward lines are ordinary order lines using a discount/free product (with taxes mapped through fiscal position, loyalty_reward.py:12-16), so they reach invoices like any line. | N-U05-170 |
| VDR-U05-C467 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:1206 | _write_vals_from_reward_vals(values_list, reward_line_pool | INFERENCE | sale_loyalty installed | — | Reward lines are reset (price 0) and rewritten from program computation on every update (lines 1179-1206), so manual edits to reward line price/quantity are overwritten (quantity readonly in view sale_order_views.xml:56-60). | N-U05-194 |
| VDR-U05-C468 | FUNCTION MAPPING REQUIRED | sale_loyalty/models/sale_order.py:296 | for line in self.order_line - self._get_no_effect_on_threshold_lines() | INFERENCE | sale_loyalty installed | — | Discountable amounts use order line quantities and totals (product_uom_qty, price_total) not delivered or invoiced quantities, so rewards never adjust to returns or credit notes automatically. | N-U05-197 |
| VDR-U05-C469 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order.py:20 | def _action_confirm | INFERENCE | sale_purchase installed | — | Confirmation hooks (sale_purchase._action_confirm, sale_crm.action_confirm, sale_project._action_confirm, sale_mrp via procurement) let a confirmed order create or update linked documents in other areas. | N-U05-200 |
| VDR-U05-C470 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:43 | def create | INFERENCE | sale_purchase installed | — | Same pattern for lines added after confirmation: purchase generation (line 46-48) and project/task generation (sale_project/sale_order_line.py:134) run on create, avoiding re-keying. | N-U05-201 |
| VDR-U05-C471 | FUNCTION MAPPING REQUIRED | sale_purchase/models/sale_order_line.py:237 | ('state', '=', 'draft') | FACT | sale_purchase installed | — | Only draft purchase orders are matched for reuse; a newly generated purchase line therefore starts on a draft PO and later states belong to purchase. | N-U05-220 |
| VDR-U05-C472 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order.py:35 | project_id = fields.Many2one | FACT | sale_project installed | — | Field help: a task will be created for the project upon confirmation; analytic distribution of the project is the reference for new order lines (optional pre-selection). | N-U05-222 |
| VDR-U05-C473 | FUNCTION MAPPING REQUIRED | sale_crm/models/crm_lead.py:106 | (opportunity.expected_revenue or 0) < order.amount_untaxed | INFERENCE | sale_crm installed | — | Condition is strictly 'lower than', so expected revenue only rises, and the same condition requires equal currency so foreign-currency orders are ignored. | N-U05-228 |
| VDR-U05-C474 | FUNCTION MAPPING REQUIRED | sale/security/ir_rules.xml:44 | sale_order_personal_rule | INFERENCE | sale installed | — | Combination of ACL (CSV), ownership rules, company rules and cron settings defines the whole access/automation scope of order invoicing and delivery links. | N-U05-232 |
| VDR-U05-C475 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1548 | creation of invoices in sudo | FACT | sale installed | — | Source comment: invoices are created in sudo because a salesperson must be able to generate an invoice without billing rights, but cannot create one from scratch. | N-U05-233 |
| VDR-U05-C476 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1563 | has_access('create') | FACT | sale installed | — | If the user cannot create account.move and also lacks write access on the order, _create_invoices returns an empty recordset without raising. | N-U05-251 |
| VDR-U05-C477 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:1550 | sudo().with_context(default_move_type='out_invoice') | INFERENCE | sale installed | — | Because moves are created in sudo, account ACL/record rules do not constrain which lines or taxes a salesperson bills from an order. | N-U05-256 |
