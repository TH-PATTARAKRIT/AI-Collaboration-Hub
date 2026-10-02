# U64 — POS Core and Extension Modules
**Modules:** point_of_sale, pos_account_tax_python, pos_edi_ubl, pos_event, pos_hr, pos_loyalty, pos_mrp, pos_online_payment, pos_repair, pos_sale, pos_sale_margin, pos_self_order, pos_sms, spreadsheet_dashboard_pos_hr, spreadsheet_dashboard_pos_restaurant, spreadsheet_dashboard_website_sale, spreadsheet_dashboard_website_sale_slides, test_discuss_full, test_event_full, test_mail_full
**Revision:** 19.0.post20260921
**Status:** DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION

---

## CAP-U64-01 POS Session Lifecycle

### D1 — State Machine and Transitions

The session lifecycle is governed by a four-state machine defined at class level. States progress from `opening_control` through `opened` to `closing_control` to `closed`. Each transition corresponds to a specific method.

### D2 — Key Methods

**action_pos_session_open** (line 372): Opens sessions in `opening_control` state. If cash control is enabled and not a rescue session, it reads the balance from the last session to set `cash_register_balance_start`.

**action_pos_session_closing_control** (line 388): Transitions state to `closing_control`, checks for draft orders, and — if no cash control — calls close directly. For rescue sessions with cash control, computes total cash from payments plus opening balance.

**_validate_session** (line 424): Core validation method. Calls `_check_if_no_draft_orders`, `_check_invoices_are_posted`, optionally creates a picking at session end, then calls `_create_account_move`. Posts the resulting journal entry and reconciles account move lines. Sets state to `closed` on success.

**_create_account_move** (line 872): Creates an `account.move` keyed to `config_id.journal_id`, then pipes through accumulate/create helpers for receivables, bank payments, cash statements, invoice receivables, and stock valuation lines.

**load_data** (line 157): Iterates all models returned by `_load_pos_data_models` and calls `_load_pos_data_search_read` on each to build the initial data bundle sent to the POS client.

### D3 — Constraints and Guards

`_check_pos_config` (line 312): Prevents more than one non-rescue open session per `pos.config`. `_check_start_date` (line 322): Validates session start date against company lock dates on the journal. `_check_invoices_are_posted` (line 332): Blocks closing if any linked invoice is not in `posted` state. `_check_if_no_draft_orders` (line 1859): Raises `UserError` if any orders are still in `draft` state.

---

## CAP-U64-02 POS Order Processing

### D1 — Happy Path

`_process_order` (line 60): Receives order dict from UI. Validates session state; if session is `closing_control` or `closed`, calls `_get_valid_session` to find an open replacement. Sets `company_id` from session config if not present. Creates or updates the `pos.order` record, then calls `_process_payment_lines` and `_process_saved_order`.

`_process_saved_order` (line 156): If not a draft, calls `action_pos_order_paid`, `_create_order_picking`, and `_compute_total_cost_in_real_time`. If `to_invoice` is set and state is `paid`, triggers invoice generation.

`action_pos_order_paid` (line 874): Verifies payment amount matches order total (with optional cash rounding tolerance). Sets order state to `paid`.

### D2 — Cancel and Edge Cases

`_get_valid_session` (line 34): If the order's session is closed, searches for an open session on the same config. Raises `UserError` if none found.

`_process_order` (line 86): If `company_id` not in order dict, defaults to `pos_session.config_id.company_id.id`, establishing multi-company isolation at order creation.

`_process_payment_lines` (line 178): Recomputes `amount_paid` server-side, ignoring the client-submitted value. Adds a change/return payment entry for the cash method if amount_return is non-zero.

### D3 — Multi-Company Handling

`_process_order` (line 100): After create, calls `pos_order.with_company(pos_order.company_id)` to ensure all subsequent computations run in the correct company context. Line 152 applies the same `with_company` before payment processing.

---

## CAP-U64-03 POS Configuration

### D1 — Key Fields

`picking_type_id` (line 76): Many2one to `stock.picking.type`, domain-restricted to outgoing operations of the current company's warehouse. Required, defaults to the warehouse's POS-specific picking type.

`available_pricelist_ids` (line 141): Many2many of `product.pricelist`, listing all pricelists selectable at the POS terminal.

`company_id` (line 143): Many2one to `res.company`, required, defaults to `env.company`. Used as the company scope for all config-level constraints.

`payment_method_ids` (line 170): Many2many of `pos.payment.method`, defaults via `_default_payment_methods` which filters by company and currency compatibility.

### D2 — Constraint Methods

`_check_company_payment` (line 478): Raises `ValidationError` if any payment method belongs to a different company than the config's `company_id`.

`_check_currencies` (line 484): Validates that all available pricelists, payment methods, and journals share a consistent currency with the config.

`_check_payment_method_ids` (line 501): Raises `UserError` if the config has no payment methods configured.

`_check_companies` (line 517): Ensures no pricelist scoped to a different company is included in `available_pricelist_ids`.

### D3 — Company Scoping

`_check_company_auto = True` (line 23): Class attribute that enables automatic company-domain filtering on all Many2one and Many2many fields with `check_company=True`. `journal_id` (line 83) and `invoice_journal_id` (line 90) both carry `check_company=True`.

---

## CAP-U64-04 POS Payment Methods

### D1 — Payment Method Model

`pos.payment.method` (line 5): Central model for POS payment methods. Fields include `journal_id` (line 36, Many2one to `account.journal`, domain restricted to cash or bank journals), `is_cash_count` (line 35, computed boolean, true when type is cash), `split_transactions` (line 47, boolean that forces per-customer journal entry splitting), `type` (line 59, computed selection of cash/bank/pay_later).

`_compute_type` (line 116): Derives type from `journal_id.type`; if journal is cash or bank, type matches; otherwise type is `pay_later`.

### D2 — Payment Record

`pos.payment` (line 7): Records individual payments on a `pos.order`. `pos_order_id` (line 21) links to the order with cascade deletion. `is_change` (line 42) flags change/return payments. `account_move_id` (line 43) links to the split payment journal entry when `split_transactions` is true.

`_check_payment_method_id` (line 67): Validates at save time that the payment method used is listed in the session config's `payment_method_ids`.

### D3 — Cash-In/Cash-Out and Split Payment

`_create_payment_moves` (line 72): For bank/split payments, creates `account.move` entries. Change/cash payments are merged: the change amount is netted against the main cash payment to produce a single move line. `pay_later` type payments skip move creation entirely.

`_accumulate_amounts` in `pos_session.py` (line 899): Separates payments into six receivable buckets — split-cash, combined-cash, split-bank, combined-bank, split-pay-later, combined-pay-later — based on `split_transactions` and `type` values.

---

## CAP-U64-05 POS Extension Modules

### pos_account_tax_python

`AccountTax._load_pos_data_fields` in `pos_account_tax_python/models/account_tax.py:8`: Extends the base tax fields list to include `formula_decoded_info`, loading Python-formula tax details into the POS client data bundle.

The module manifest at `pos_account_tax_python/__manifest__.py:9`: Adds `account_tax_python/static/src/helpers/*.js` to the `point_of_sale._assets_pos` bundle, enabling evaluation of Python-formula taxes in the browser.

### pos_edi_ubl

`PosEdiXmlUBL21._export_pos_order` in `pos_edi_ubl/models/pos_edi_ubl_21.py:12`: Abstract model inheriting `account.edi.xml.ubl_21` that builds a UBL 2.1 XML document for a POS order by assembling supplier, customer, payment-means, tax-total, and line-item nodes.

`PosEdiXmlUBL21._get_pos_order_node` in `pos_edi_ubl/models/pos_edi_ubl_21.py:24`: Orchestrates all sub-builders (_add_pos_order_config_vals, _add_pos_order_base_lines_vals, _add_pos_order_currency_vals, etc.) to produce the full XML document node for the order.

The module manifest at `pos_edi_ubl/__manifest__.py:4`: Declares dependency on `account_edi_ubl_cii` and `point_of_sale`, positioning itself as a pure UBL export helper with no data or views.

### pos_event

`EventRegistration.pos_order_line_id` in `pos_event/models/event_registration.py:11`: Many2one field added to `event.registration` linking it to the POS order line that sold the event ticket; deletion of the order line cascades to the registration.

`PosOrderLine.event_ticket_id` in `pos_event/models/pos_order_line.py:8`: Many2one to `event.event.ticket` placed on POS order lines, enabling ticket-type selection at the point of sale.

`PosSession._load_pos_data_models` in `pos_event/models/pos_session.py:9`: Extends the data-load model list to include `event.event.ticket`, `event.event`, `event.slot`, `event.registration`, `event.question`, and related models, making event data available in the POS client.

### pos_hr

`HrEmployee.get_barcodes_and_pin_hashed` in `pos_hr/models/hr_employee.py:57`: Returns SHA-1 hashed barcode and PIN values for employees, so credentials are never transmitted in plaintext to the POS client.

`HrEmployee._load_pos_data_read` in `pos_hr/models/hr_employee.py:26`: Assigns each employee to a permission role (`basic`, `advanced`, or `minimal`) based on their membership in config-level employee groups, then attaches hashed credentials to the employee dict before returning it to the client.

`HrEmployee._unlink_except_active_pos_session` in `pos_hr/models/hr_employee.py:70`: Blocks deletion of an employee if they are linked to a config with an active POS session, protecting live sessions from losing employee records.

### pos_loyalty

`PosOrder.validate_coupon_programs` in `pos_loyalty/models/pos_order.py:13`: Server-side validation of loyalty point changes and new coupon codes submitted from the UI. Checks coupon balances and raises if points are insufficient or codes already exist.

`PosSession._load_pos_data_models` in `pos_loyalty/models/pos_session.py:10`: Extends the session data load to include `loyalty.program`, `loyalty.rule`, `loyalty.reward`, and `loyalty.card`, making full loyalty configuration available in the POS client bundle.

`PosOrder.add_loyalty_history_lines` in `pos_loyalty/models/pos_order.py:56`: Records point additions and redemptions as loyalty card history lines after the order is processed, maintaining a full audit trail of loyalty transactions.

### pos_mrp

`PosOrderLine._get_stock_moves_to_consider` in `pos_mrp/models/pos_order.py:10`: Overrides stock-move selection for a line by exploding the product's phantom BoM and returning moves whose product matches the kit components rather than the top-level product.

`PosOrder._get_pos_anglo_saxon_price_unit` in `pos_mrp/models/pos_order.py:33`: Extends Anglo-Saxon cost calculation to explode phantom BoMs, computing the weighted average cost across all kit components proportionally.

`StockMove._get_lot_line_qty` in `pos_mrp/models/stock_picking.py:7`: When processing lot-tracked stock moves linked to a BoM line, sums the quantity from all POS order lines for the corresponding kit product template variant.

### pos_online_payment

`PosPaymentMethod.is_online_payment` in `pos_online_payment/models/pos_payment_method.py:11`: Boolean field that marks a payment method as web-based. When set, `_compute_type` (line 36) sets the payment type to `online` (added to the selection).

`PosPaymentMethod._get_online_payment_providers` in `pos_online_payment/models/pos_payment_method.py:43`: Returns the allowed payment providers; if none are explicitly set, defaults to all published and enabled providers.

`PosSession._accumulate_amounts` in `pos_online_payment/models/pos_session.py:12`: Extends amount accumulation to collect `online`-type payments into a `split_receivables_online` bucket, which is later reconciled against account payment move lines.

### pos_repair

`SaleOrderLine.is_repair_line` in `pos_repair/models/sale_order_line.py:9`: Computed boolean that is True when any stock move linked to the sale line has an associated `repair_id`, marking lines as repair-related.

`StockPicking._create_move_from_pos_order_lines` in `pos_repair/models/stock_picking.py:9`: Overrides move creation to exclude POS order lines whose linked sale order line is a repair line, preventing duplicate stock movement for repair items.

### pos_sale

`PosOrder.sale_order_count` in `pos_sale/models/pos_order.py:13`: Computed integer field showing how many distinct sale orders are referenced by the POS order lines (via `sale_order_origin_id`).

`PosOrder.action_pos_order_paid` in `pos_sale/models/pos_order.py:64`: Extension that, after calling super, confirms any linked draft/sent sale orders and updates their delivery pickings to reflect quantities paid through the POS.

`PosOrder._prepare_invoice_vals` in `pos_sale/models/pos_order.py:31`: Overrides invoice preparation to inherit partner shipping address, payment terms, and partner invoice ID from the originating sale order when order lines trace back to one.

### pos_sale_margin

`SaleReport._fill_pos_fields` in `pos_sale_margin/report/sale_report.py:10`: Extends the POS contribution to the unified sales report by injecting a `margin` SQL expression that computes gross margin as price subtotal minus total cost, currency-rate adjusted.

The module manifest at `pos_sale_margin/__manifest__.py:5`: Declares dependency on `pos_sale` and `sale_margin`, with `auto_install: True`, meaning it activates automatically when both dependencies are installed.

### pos_self_order

`PosConfig.self_ordering_url` in `pos_self_order/models/pos_config.py:35`: Computed field that constructs the public-facing self-order URL from the server base URL, the config's unique access token, and optional table route segment.

`PosConfig._get_self_order_route` in `pos_self_order/models/pos_config.py:263`: Builds the route string for self-ordering, appending `access_token` as a query parameter to secure QR-code access without requiring customer authentication.

`PosOrder.sync_from_ui` in `pos_self_order/models/pos_order.py:66`: Entry point for customer-submitted orders from the self-order web app; delegates to the core order processing flow after validating the session context.

### pos_sms

`PosOrder.action_sent_message_on_sms` in `pos_sms/models/pos_order.py:7`: Sends an SMS receipt to the customer using the `sms.composer` model, gated on both `module_pos_sms` and `sms_receipt_template_id` being configured on the POS config.

`PosConfig.sms_receipt_template_id` field referenced at `pos_sms/models/pos_config.py`: Stores the SMS template used for receipt delivery, configurable per POS terminal.

The module manifest at `pos_sms/__manifest__.py:3`: Declares dependency on `point_of_sale` and `sms`; includes an SMS template data file and JS assets in the POS bundle.

---

## CAP-U64-06 Spreadsheet Dashboard Modules

### spreadsheet_dashboard_pos_hr

The manifest at `spreadsheet_dashboard_pos_hr/__manifest__.py:8`: Declares dependencies on `spreadsheet_dashboard` and `pos_hr`, with `auto_install: ['pos_hr']`, meaning it installs automatically when `pos_hr` is present. Loads POS HR dashboard definitions from `data/dashboards.xml`.

### spreadsheet_dashboard_pos_restaurant

The manifest at `spreadsheet_dashboard_pos_restaurant/__manifest__.py:8`: Declares dependencies on `spreadsheet_dashboard`, `pos_hr`, and `pos_restaurant`, with `auto_install: ['pos_hr', 'pos_restaurant']`. Provides a pre-built restaurant-specific spreadsheet dashboard in `data/dashboards.xml`.

### spreadsheet_dashboard_website_sale

The manifest at `spreadsheet_dashboard_website_sale/__manifest__.py:7`: Declares dependency on `spreadsheet_dashboard` and `website_sale`, with `auto_install: ['website_sale']`. Delivers a pre-built eCommerce performance spreadsheet dashboard.

### spreadsheet_dashboard_website_sale_slides

The manifest at `spreadsheet_dashboard_website_sale_slides/__manifest__.py:7`: Declares dependency on `spreadsheet_dashboard` and `website_sale_slides`, with `auto_install: ['website_sale_slides']`. Delivers a pre-built eLearning sales spreadsheet dashboard.

---

## CAP-U64-07 Test Modules

### test_discuss_full

`TestDiscussFullPerformance` in `test_discuss_full/tests/test_performance.py:14`: Test class tagged `post_install` and `is_query_count` that verifies Discuss initialization query counts under a full module stack including `hr_holidays`, `hr_homeworking`, `im_livechat`, and CRM.

The manifest at `test_discuss_full/__manifest__.py:11`: Lists 20+ module dependencies including `calendar`, `crm`, `im_livechat`, `hr_attendance`, `hr_fleet`, and `mail`, ensuring Discuss is tested with all enterprise overrides active.

### test_event_full

`TestEventEvent.test_event_create_wtype` in `test_event_full/tests/test_event_event.py:16`: Tests event creation with a fully typed event configuration, verifying that event ticket, slot, and sub-record defaults propagate correctly when an event type is assigned.

The manifest at `test_event_full/__manifest__.py:6`: Declares dependencies on `event`, `event_booth`, `event_crm`, `event_sale`, `event_sms`, and `payment_demo` to exercise the full event-to-payment pipeline including eCommerce registration.

### test_mail_full

`FullBaseMailPerformance` in `test_mail_full/tests/test_mail_performance.py:11`: Extends the base mail performance suite (`BaseMailPostPerformance`) and adds multi-company, multi-channel, and mass-mailing scenarios to measure query counts at scale.

The manifest at `test_mail_full/__manifest__.py:10`: Depends on `mail`, `mail_bot`, `portal`, `rating`, `mass_mailing`, and `mass_mailing_sms`, ensuring mail routing, bot responses, and SMS fallback are all exercised within performance benchmarks.

---

## Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
| VDR-U64-C001 | POS.session.state_machine | point_of_sale/models/pos_session.py:23 | POS_SESSION_STATE | FACT | always | — | POS session uses a four-state machine: opening_control, opened, closing_control, closed, each mapped to a specific transition method | N-U64-001 |
| VDR-U64-C002 | POS.session.open | point_of_sale/models/pos_session.py:372 | def action_pos_session_open | FACT | always | — | action_pos_session_open filters sessions in opening_control state and, when cash control is active and not a rescue session, pre-sets cash_register_balance_start from the last session's ending balance | N-U64-001 |
| VDR-U64-C003 | POS.session.create | point_of_sale/models/pos_session.py:341 | def create | FACT | always | — | Session create() determines update_stock_at_closing from company config and immediately calls action_pos_session_open, so every new session transitions out of opening_control on creation | N-U64-001 |
| VDR-U64-C004 | POS.session.closing_control | point_of_sale/models/pos_session.py:388 | def action_pos_session_closing_control | FACT | always | — | action_pos_session_closing_control blocks closing if any draft orders exist, writes state to closing_control, and skips the cash-count screen if cash control is disabled | N-U64-002 |
| VDR-U64-C005 | POS.session.validate | point_of_sale/models/pos_session.py:424 | def _validate_session | FACT | always | — | _validate_session checks draft orders and unposted invoices, conditionally creates end-of-session stock pickings, calls _create_account_move, posts the resulting journal entry, and reconciles account move lines | N-U64-002 |
| VDR-U64-C006 | POS.session.validate.stock | point_of_sale/models/pos_session.py:437 | if self.update_stock_at_closing | FACT | when update_stock_at_closing | — | When update_stock_at_closing is True, _validate_session calls _create_picking_at_end_of_session and then computes total cost for orders lacking a total cost value | N-U64-002 |
| VDR-U64-C007 | POS.session.create_account_move | point_of_sale/models/pos_session.py:872 | def _create_account_move | FACT | always | — | _create_account_move creates an account.move on config_id.journal_id, then calls six helpers: _accumulate_amounts, _create_non_reconciliable_move_lines, _create_bank_payment_moves, _create_pay_later_receivable_lines, _create_cash_statement_lines_and_cash_move_lines, _create_invoice_receivable_lines | N-U64-003 |
| VDR-U64-C008 | POS.session.create_account_move.journal | point_of_sale/models/pos_session.py:879 | reconciling cash receivable lines | FACT | always | — | The closing journal entry is created with journal_id taken from config_id.journal_id and ref set to the session name | N-U64-003 |
| VDR-U64-C009 | POS.session.load_data | point_of_sale/models/pos_session.py:157 | def load_data | FACT | always | — | load_data iterates all models returned by _load_pos_data_models and calls _load_pos_data_search_read on each to build the complete JSON bundle sent to the POS UI client | N-U64-004 |
| VDR-U64-C010 | POS.session.load_models | point_of_sale/models/pos_session.py:139 | def _load_pos_data_models | FACT | always | — | _load_pos_data_models returns 36 model names including pos.config, pos.order, pos.payment.method, product.product, account.tax, product.pricelist, and stock.picking.type, defining the POS initial data set | N-U64-004 |
| VDR-U64-C011 | POS.session.notify_close | point_of_sale/models/pos_session.py:96 | aggregated and bank split | FACT | on write with state=closed | — | When session state is set to closed in write(), a CLOSING_SESSION bus notification is dispatched via config_id._notify(), carrying the device_identifier and session_id | N-U64-005 |
| VDR-U64-C012 | POS.session.check_pos_config | point_of_sale/models/pos_session.py:312 | def _check_pos_config | FACT | on create | — | _check_pos_config constrains that only one non-rescue session can be in a non-closed state per pos.config; a second open session raises ValidationError | N-U64-001 |
| VDR-U64-C013 | POS.session.check_start_date | point_of_sale/models/pos_session.py:322 | def _check_start_date | FACT | on create | — | _check_start_date validates session start_at against company accounting lock dates on the config journal; a violation raises ValidationError listing the lock date | N-U64-001 |
| VDR-U64-C014 | POS.session.check_invoices | point_of_sale/models/pos_session.py:332 | def _check_invoices_are_posted | FACT | on closing | — | _check_invoices_are_posted raises UserError if any account.move linked to closed session orders is not in posted state, blocking session close | N-U64-002 |
| VDR-U64-C015 | POS.session.check_draft_orders | point_of_sale/models/pos_session.py:1859 | def _check_if_no_draft_orders | FACT | on closing | — | _check_if_no_draft_orders raises UserError listing order names if any orders in the session remain in draft state at close time | N-U64-002 |
| VDR-U64-C016 | POS.order.process | point_of_sale/models/pos_order.py:60 | def _process_order | FACT | always | — | _process_order validates session state and redirects closed-session orders to an open session via _get_valid_session; sets company_id from session config if absent | N-U64-006 |
| VDR-U64-C017 | POS.order.process.multicompany | point_of_sale/models/pos_order.py:100 | pos_order.with_company | FACT | always | — | After creating the pos.order record, _process_order immediately applies with_company(pos_order.company_id) to ensure all downstream computations run in the order's company context | N-U64-007 |
| VDR-U64-C018 | POS.order.process_saved | point_of_sale/models/pos_order.py:156 | def _process_saved_order | FACT | non-draft orders | — | _process_saved_order calls action_pos_order_paid, _create_order_picking, and _compute_total_cost_in_real_time for non-draft orders; also triggers invoice generation if to_invoice is set | N-U64-006 |
| VDR-U64-C019 | POS.order.paid | point_of_sale/models/pos_order.py:874 | def action_pos_order_paid | FACT | always | — | action_pos_order_paid verifies that amount_paid matches amount_total within rounding tolerance; sets order state to paid or raises UserError if underpaid | N-U64-008 |
| VDR-U64-C020 | POS.order.cancel.session | point_of_sale/models/pos_order.py:34 | def _get_valid_session | FACT | closed session | — | _get_valid_session searches for an open session on the same pos.config when the original session is closed; raises UserError if no open session exists | N-U64-006 |
| VDR-U64-C021 | POS.order.payment_lines | point_of_sale/models/pos_order.py:178 | def _process_payment_lines | FACT | always | — | _process_payment_lines recomputes amount_paid server-side from payment_ids, disregarding the client-submitted value, and adds a change payment line when amount_return is non-zero | N-U64-008 |
| VDR-U64-C022 | POS.order.company_default | point_of_sale/models/pos_order.py:86 | if not order.get | FACT | when company_id absent | — | If the order dictionary contains no company_id, _process_order assigns it from pos_session.config_id.company_id.id, enforcing company isolation without client cooperation | N-U64-007 |
| VDR-U64-C023 | POS.config.picking_type | point_of_sale/models/pos_config.py:76 | picking_type_id = fields.Many2one | FACT | always | — | picking_type_id is a required Many2one to stock.picking.type, domain-restricted to outgoing operations of the current company's warehouse, defaulting to the warehouse's POS-specific picking type | N-U64-009 |
| VDR-U64-C024 | POS.config.pricelists | point_of_sale/models/pos_config.py:141 | available_pricelist_ids = fields.Many2many | FACT | always | — | available_pricelist_ids is a Many2many of product.pricelist listing all pricelists selectable at the terminal; the default pricelist must also appear in this list to be valid | N-U64-009 |
| VDR-U64-C025 | POS.config.company | point_of_sale/models/pos_config.py:143 | string='Company', required=True | FACT | always | — | company_id is a required Many2one to res.company defaulting to env.company; it scopes all constraint checks for payment methods, journals, and pricelists | N-U64-009 |
| VDR-U64-C026 | POS.config.payment_methods | point_of_sale/models/pos_config.py:170 | payment_method_ids = fields.Many2many | FACT | always | — | payment_method_ids is a Many2many of pos.payment.method with a default factory that selects company-compatible cash and non-cash methods; copy=False prevents session duplication from inheriting payment methods | N-U64-009 |
| VDR-U64-C027 | POS.config.check_company_payment | point_of_sale/models/pos_config.py:478 | def _check_company_payment | FACT | on save | — | _check_company_payment constrains that every payment method in payment_method_ids belongs to the same company as the config; a mismatch raises ValidationError | N-U64-009 |
| VDR-U64-C028 | POS.config.check_currencies | point_of_sale/models/pos_config.py:484 | def _check_currencies | FACT | on save | — | _check_currencies validates that all pricelists, journals, and payment methods configured on the pos.config share a consistent currency with the config currency | N-U64-009 |
| VDR-U64-C029 | POS.config.check_company_auto | point_of_sale/models/pos_config.py:23 | _check_company_auto = True | FACT | always | — | The PosConfig class sets _check_company_auto = True, enabling Odoo's automatic company-domain filtering on all Many2one fields marked check_company=True, including journal_id and invoice_journal_id | N-U64-009 |
| VDR-U64-C030 | POS.payment_method.journal | point_of_sale/models/pos_payment_method.py:36 | journal_id = fields.Many2one | FACT | always | — | journal_id on pos.payment.method is restricted to cash or bank journals only; it determines whether the method's type is cash, bank, or pay_later via _compute_type | N-U64-010 |
| VDR-U64-C031 | POS.payment_method.type | point_of_sale/models/pos_payment_method.py:116 | def _compute_type | FACT | always | — | _compute_type sets type to the journal's type (cash or bank) if a journal is linked; otherwise defaults to pay_later, making type entirely derived from the journal linkage | N-U64-010 |
| VDR-U64-C032 | POS.payment_method.is_cash | point_of_sale/models/pos_payment_method.py:35 | is_cash_count = fields.Boolean | FACT | always | — | is_cash_count is a computed, stored Boolean that is True when the payment method type is cash; it drives cash-control activation and cash register logic in pos.session | N-U64-010 |
| VDR-U64-C033 | POS.payment_method.split | point_of_sale/models/pos_payment_method.py:47 | split_transactions = fields.Boolean | FACT | when enabled | — | split_transactions Boolean forces a customer to be selected for this method and splits journal entries per customer; the pos_session.py _accumulate_amounts routes such payments into separate split receivable buckets | N-U64-010 |
| VDR-U64-C034 | POS.payment.check_method | point_of_sale/models/pos_payment.py:67 | def _check_payment_method_id | FACT | on save | — | _check_payment_method_id validates that the payment method used on a pos.payment record is listed in the session config's payment_method_ids; raises ValidationError if not | N-U64-010 |
| VDR-U64-C035 | POS.payment.check_amount | point_of_sale/models/pos_payment.py:61 | def _check_amount | FACT | on edit | — | _check_amount raises ValidationError if a payment amount is modified after the order is in done state or has an account_move, preventing retrospective payment edits | N-U64-010 |
| VDR-U64-C036 | POS.payment.create_moves | point_of_sale/models/pos_payment.py:72 | def _create_payment_moves | FACT | always | — | _create_payment_moves nets cash change payments against the main cash payment to produce a single account.move entry; pay_later type payments are skipped entirely | N-U64-010 |
| VDR-U64-C037 | POS.session.accumulate | point_of_sale/models/pos_session.py:899 | def _accumulate_amounts | FACT | always | — | _accumulate_amounts builds six receivable buckets separating payments by split_transactions flag and type (cash/bank/pay_later) to prepare data for journal entry line creation | N-U64-003 |
| VDR-U64-C038 | POS.tax_python.fields | pos_account_tax_python/models/account_tax.py:8 | def _load_pos_data_fields | FACT | always | — | pos_account_tax_python extends _load_pos_data_fields on account.tax to append formula_decoded_info, loading Python-formula tax computation data into the POS client | N-U64-011 |
| VDR-U64-C039 | POS.edi_ubl.export | pos_edi_ubl/models/pos_edi_ubl_21.py:12 | def _export_pos_order | FACT | on export | — | PosEdiXmlUBL21._export_pos_order builds a UBL 2.1 XML document for a POS order, assembling header, supplier, customer, payment-means, tax-total, and line nodes | N-U64-012 |
| VDR-U64-C040 | POS.edi_ubl.node | pos_edi_ubl/models/pos_edi_ubl_21.py:24 | def _get_pos_order_node | FACT | on export | — | _get_pos_order_node orchestrates all sub-builder methods (config_vals, base_lines_vals, currency_vals, tax_grouping_vals, monetary_totals_vals) before assembling XML nodes | N-U64-012 |
| VDR-U64-C041 | POS.event.registration_link | pos_event/models/event_registration.py:11 | pos_order_line_id = fields.Many2one | FACT | always | — | pos_event adds pos_order_line_id Many2one to event.registration with ondelete=cascade, linking each event registration to the POS order line that sold its ticket | N-U64-013 |
| VDR-U64-C042 | POS.event.order_line | pos_event/models/pos_order_line.py:8 | event_ticket_id = fields.Many2one | FACT | always | — | pos_event adds event_ticket_id Many2one to pos.order.line, allowing the cashier or customer to select an event ticket type on a POS order line | N-U64-013 |
| VDR-U64-C043 | POS.event.session_models | pos_event/models/pos_session.py:9 | def _load_pos_data_models | FACT | always | — | pos_event extends PosSession._load_pos_data_models to include event.event.ticket, event.event, event.slot, event.registration, event.question, event.question.answer, and event.registration.answer | N-U64-013 |
| VDR-U64-C044 | POS.hr.hashed_credentials | pos_hr/models/hr_employee.py:57 | def get_barcodes_and_pin_hashed | FACT | always | — | get_barcodes_and_pin_hashed returns SHA-1 hashed barcode and PIN values for employees so that login credentials are never transmitted in cleartext to the POS client | N-U64-014 |
| VDR-U64-C045 | POS.hr.role_assignment | pos_hr/models/hr_employee.py:26 | def _load_pos_data_read | FACT | always | — | _load_pos_data_read assigns each employee a role (basic, advanced, or minimal) based on config-level employee group membership, then attaches hashed credentials before returning the employee record to the POS client | N-U64-014 |
| VDR-U64-C046 | POS.hr.unlink_guard | pos_hr/models/hr_employee.py:70 | def _unlink_except_active_pos_session | FACT | on unlink | — | _unlink_except_active_pos_session prevents deletion of an employee linked to an active POS session by checking membership in basic_employee_ids, advanced_employee_ids, and minimal_employee_ids | N-U64-014 |
| VDR-U64-C047 | POS.loyalty.validate | pos_loyalty/models/pos_order.py:13 | def validate_coupon_programs | FACT | on order submit | — | validate_coupon_programs server-validates loyalty point changes and new coupon codes; raises if coupon balance is insufficient or if a new code already exists in the loyalty.card table | N-U64-015 |
| VDR-U64-C048 | POS.loyalty.session_models | pos_loyalty/models/pos_session.py:10 | def _load_pos_data_models | FACT | always | — | pos_loyalty extends PosSession._load_pos_data_models to include loyalty.program, loyalty.rule, loyalty.reward, and loyalty.card, making full loyalty configuration available in the POS data bundle | N-U64-015 |
| VDR-U64-C049 | POS.loyalty.history | pos_loyalty/models/pos_order.py:56 | def add_loyalty_history_lines | FACT | post-payment | — | add_loyalty_history_lines records point additions and redemptions as loyalty card history entries after the order is processed, maintaining a full audit trail of loyalty transactions | N-U64-015 |
| VDR-U64-C050 | POS.mrp.bom_moves | pos_mrp/models/pos_order.py:10 | def _get_stock_moves_to_consider | FACT | kit products | — | _get_stock_moves_to_consider explodes a product's phantom BoM and returns only stock moves whose product_id matches a kit component, bypassing the top-level kit product for stock accounting | N-U64-016 |
| VDR-U64-C051 | POS.mrp.cost | pos_mrp/models/pos_order.py:33 | def _get_pos_anglo_saxon_price_unit | FACT | kit products | — | _get_pos_anglo_saxon_price_unit explodes phantom BoMs to compute weighted average Anglo-Saxon cost across all kit components proportional to their BoM quantity ratio | N-U64-016 |
| VDR-U64-C052 | POS.mrp.lot_qty | pos_mrp/models/stock_picking.py:7 | def _get_lot_line_qty | FACT | lot-tracked kit moves | — | _get_lot_line_qty sums POS order line quantities across all lines for the kit product template variant when processing lot-tracked moves linked to a BoM line | N-U64-016 |
| VDR-U64-C053 | POS.online_payment.field | pos_online_payment/models/pos_payment_method.py:11 | is_online_payment = fields.Boolean | FACT | always | — | pos_online_payment adds is_online_payment Boolean to pos.payment.method; when True, _compute_type sets the type to online (a new selection value added by this module) | N-U64-017 |
| VDR-U64-C054 | POS.online_payment.providers | pos_online_payment/models/pos_payment_method.py:43 | def _get_online_payment_providers | FACT | always | — | _get_online_payment_providers returns explicitly configured online_payment_provider_ids; when none are set, falls back to all published and enabled payment providers | N-U64-017 |
| VDR-U64-C055 | POS.online_payment.accumulate | pos_online_payment/models/pos_session.py:12 | def _accumulate_amounts | FACT | online payments | — | pos_online_payment extends _accumulate_amounts to collect online-type payments into a split_receivables_online bucket, later reconciled against account payment receivable lines | N-U64-017 |
| VDR-U64-C056 | POS.repair.is_repair_line | pos_repair/models/sale_order_line.py:9 | is_repair_line = fields.Boolean | FACT | always | — | pos_repair adds computed is_repair_line Boolean to sale.order.line that is True when any linked stock move has a repair_id, marking the line as originating from a repair order | N-U64-018 |
| VDR-U64-C057 | POS.repair.picking_exclusion | pos_repair/models/stock_picking.py:9 | def _create_move_from_pos_order_lines | FACT | on order | — | _create_move_from_pos_order_lines filters out POS order lines whose linked sale order line is_repair_line, preventing duplicate stock movements for repair-billed items | N-U64-018 |
| VDR-U64-C058 | POS.sale.order_count | pos_sale/models/pos_order.py:13 | sale_order_count = fields.Integer | FACT | always | — | pos_sale adds sale_order_count computed Integer to pos.order showing the count of distinct sale orders referenced via sale_order_origin_id on order lines | N-U64-019 |
| VDR-U64-C059 | POS.sale.paid_so | pos_sale/models/pos_order.py:64 | def action_pos_order_paid | FACT | on payment | — | pos_sale overrides action_pos_order_paid to confirm linked draft or sent sale orders and update their delivery pickings to reflect quantities settled through the POS | N-U64-019 |
| VDR-U64-C060 | POS.sale.invoice_vals | pos_sale/models/pos_order.py:31 | def _prepare_invoice_vals | FACT | on invoice | — | pos_sale overrides _prepare_invoice_vals to inherit partner shipping address, payment term, and partner invoice ID from the originating sale order when order lines trace back to one | N-U64-019 |
| VDR-U64-C061 | POS.sale_margin.report | pos_sale_margin/report/sale_report.py:10 | def _fill_pos_fields | FACT | always | — | pos_sale_margin extends SaleReport._fill_pos_fields to inject a margin SQL expression computing gross margin as price subtotal minus total cost, currency-rate adjusted for multi-currency reporting | N-U64-020 |
| VDR-U64-C062 | POS.self_order.url | pos_self_order/models/pos_config.py:35 | self_ordering_url = fields.Char | FACT | always | — | pos_self_order adds self_ordering_url computed field that constructs the public-facing URL from the server base URL plus the config's unique access_token query parameter | N-U64-021 |
| VDR-U64-C063 | POS.self_order.route | pos_self_order/models/pos_config.py:263 | def _get_self_order_route | FACT | always | — | _get_self_order_route appends access_token as a query parameter to the route string to secure QR-code access without requiring customer authentication | N-U64-021 |
| VDR-U64-C064 | POS.self_order.sync | pos_self_order/models/pos_order.py:66 | def sync_from_ui | FACT | on customer order | — | sync_from_ui is the server entry point for customer-submitted orders from the self-order web app, delegating to the core order processing flow after session context validation | N-U64-021 |
| VDR-U64-C065 | POS.sms.send | pos_sms/models/pos_order.py:7 | def action_sent_message_on_sms | FACT | on trigger | — | action_sent_message_on_sms creates an sms.composer record and calls action_send_sms, gated on both module_pos_sms and sms_receipt_template_id being non-empty on the POS config | N-U64-022 |
| VDR-U64-C066 | POS.sms.manifest | pos_sms/__manifest__.py:3 | integrates the Point of Sale | FACT | always | — | pos_sms depends on point_of_sale and sms, registers an SMS template data file, and adds JS assets to the POS bundle to enable in-app SMS dispatch | N-U64-022 |
| VDR-U64-C067 | DASH.pos_hr.manifest | spreadsheet_dashboard_pos_hr/__manifest__.py:4 | Spreadsheet dashboard for point | FACT | always | — | spreadsheet_dashboard_pos_hr auto-installs when pos_hr is present and loads its POS HR spreadsheet dashboard definitions from data/dashboards.xml | N-U64-023 |
| VDR-U64-C068 | DASH.pos_restaurant.manifest | spreadsheet_dashboard_pos_restaurant/__manifest__.py:3 | Spreadsheet dashboard for restaurants | FACT | always | — | spreadsheet_dashboard_pos_restaurant auto-installs when both pos_hr and pos_restaurant are present and loads restaurant-specific dashboard definitions from data/dashboards.xml | N-U64-023 |
| VDR-U64-C069 | DASH.website_sale.manifest | spreadsheet_dashboard_website_sale/__manifest__.py:3 | Spreadsheet dashboard for eCommerce | FACT | always | — | spreadsheet_dashboard_website_sale auto-installs when website_sale is present and delivers a pre-built eCommerce performance spreadsheet dashboard | N-U64-024 |
| VDR-U64-C070 | DASH.website_sale_slides.manifest | spreadsheet_dashboard_website_sale_slides/__manifest__.py:3 | Spreadsheet dashboard for eLearning | FACT | always | — | spreadsheet_dashboard_website_sale_slides auto-installs when website_sale_slides is present and delivers a pre-built eLearning sales spreadsheet dashboard | N-U64-024 |
| VDR-U64-C071 | TEST.discuss_full.perf | test_discuss_full/tests/test_performance.py:14 | class TestDiscussFullPerformance | FACT | post_install | — | TestDiscussFullPerformance is tagged post_install and is_query_count and verifies Discuss initialization query counts across a full module stack including hr_holidays, hr_homeworking, and im_livechat overrides | N-U64-025 |
| VDR-U64-C072 | TEST.discuss_full.manifest | test_discuss_full/__manifest__.py:11 | all possible overrides installed | FACT | always | — | test_discuss_full declares 20-plus module dependencies including calendar, crm, im_livechat, hr_attendance, and hr_fleet to ensure Discuss is tested with all enterprise overrides active | N-U64-025 |
| VDR-U64-C073 | TEST.event_full.create | test_event_full/tests/test_event_event.py:16 | def test_event_create_wtype | FACT | post_install | — | test_event_create_wtype tests event creation with a fully typed event configuration, verifying that ticket, slot, and sub-record defaults propagate correctly when an event type is assigned | N-U64-026 |
| VDR-U64-C074 | TEST.event_full.manifest | test_event_full/__manifest__.py:7 | test the main event flows | FACT | always | — | test_event_full depends on event, event_booth, event_crm, event_sale, event_sms, and payment_demo to exercise the full event-to-payment pipeline including eCommerce registration | N-U64-026 |
| VDR-U64-C075 | TEST.mail_full.perf | test_mail_full/tests/test_mail_performance.py:11 | class FullBaseMailPerformance | FACT | post_install | — | FullBaseMailPerformance extends BaseMailPostPerformance with multi-company, multi-channel, and mass-mailing scenarios to measure mail routing query counts at scale | N-U64-027 |
| VDR-U64-C076 | TEST.mail_full.manifest | test_mail_full/__manifest__.py:8 | performances and tests specific | FACT | always | — | test_mail_full depends on mail, mail_bot, portal, rating, mass_mailing, and mass_mailing_sms to exercise mail routing, bot responses, and SMS fallback within performance benchmarks | N-U64-027 |
| VDR-U64-C077 | POS.session.post_difference | point_of_sale/models/pos_session.py:486 | def _post_statement_difference | FACT | on close | — | _post_statement_difference creates a bank statement line for any cash difference; uses cash_journal_id.loss_account_id for negative differences and profit_account_id for positive ones; raises if the account is not configured | N-U64-003 |
| VDR-U64-C078 | POS.config.cash_control | point_of_sale/models/pos_config.py:324 | config.cash_control = bool | FACT | computed | — | cash_control is computed as True when any payment method in payment_method_ids has is_cash_count=True, automatically enabling opening and closing balance checks | N-U64-009 |
| VDR-U64-C079 | POS.payment.is_change | point_of_sale/models/pos_payment.py:42 | is_change = fields.Boolean | FACT | always | — | is_change Boolean on pos.payment flags change/return cash payments; _create_payment_moves nets change payments against the corresponding main cash payment to avoid double-counting | N-U64-010 |
| VDR-U64-C080 | POS.session.rescue | point_of_sale/models/pos_session.py:84 | rescue = fields.Boolean | FACT | always | — | rescue Boolean marks auto-generated sessions created for orphaned orders; rescue sessions are excluded from the one-session-per-config constraint and follow a simplified closing path | N-U64-005 |
