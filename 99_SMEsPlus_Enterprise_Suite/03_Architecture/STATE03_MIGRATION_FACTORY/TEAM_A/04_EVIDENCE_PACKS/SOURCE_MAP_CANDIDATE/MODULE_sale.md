# Source Map (candidate) — `sale`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale` |
| Display name | Sales |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `349c8a4ac364eac0` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `sales_team`, `account_payment`, `utm`
- Direct dependents in 300-module list (12): `delivery`, `partnership`, `sale_crm`, `sale_edi_ubl`, `sale_gelato`, `sale_loyalty`, `sale_management`, `sale_product_matrix`, `sale_purchase`, `sale_sms`, `sale_stock`, `spreadsheet_dashboard_sale`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (9): `l10n_br_sales`, `l10n_din5008_sale`, `l10n_ec_sale`, `l10n_fi_sale`, `l10n_in_sale`, `l10n_it_edi_doi`, `l10n_it_edi_sale`, `mass_mailing_sale`, `website_sale`
- Custom / third-party modules that declare a dependency (name — license only) (20): `d_product_brand` — OPL-1, `nthub_binary_field_preview` — LGPL-3, `scgl_product_image` — no-license, `cr_effective_date_entries` — AGPL-3, `scgl_so_section_bydivision` — LGPL-3, `odoo19_uom_ext` — no-license, `product_3d_viewer` — LGPL-3, `19_bhpro_master_data` — OPL-1, `sale_productinfo_ext` — no-license, `scgl_sol_global_discount` — LGPL-3, `scgl_import_product_images` — no-license, `sale_gross_profit_record` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Sales internal machinery
- Inventory of user-facing artifacts (counts): menu items 37, views 57, window actions 30, server actions 3, reports 2, mail templates 4, scheduled jobs 2, wizards 6, web routes 8
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (6): `sale.order.discount` (Discount Wizard); `sale.mass.cancel.orders` (Cancel multiple quotations); `sale.advance.payment.inv` (Sales Advance Payment Invoice); `sale.order` (Sales Order); `sale.order.line` (Sales Order Line); `sale.report` (Sales Analysis Report)
- Objects extended from other modules (29): `base.document.layout`, `res.config.settings`, `payment.link.wizard`, `payment.provider`, `crm.team`, `account.move`, `utm.mixin`, `payment.transaction`, `ir.actions.report`, `portal.mixin`, `product.catalog.mixin`, `mail.thread`, `mail.activity.mixin`, `account.document.import.mixin`, `account.move.line`, `analytic.mixin`, `product.document`, `product.template`, `product.product`, `product.attribute.custom.value`, `res.company`, `ir.config_parameter`, `utm.campaign`, `account.analytic.line`, `account.analytic.applicability` … (+4)
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 4 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `sale.order.discount` ← Community: —; open-license custom/third-party scanned: `scgl_sol_global_discount`, `smesplus_sol_global_discount`
- `sale.advance.payment.inv` ← Community: `l10n_in_sale`, `sale_timesheet`; open-license custom/third-party scanned: —
- `sale.order` ← Community: `delivery`, `delivery_mondialrelay`, `event_booth_sale`, `event_sale`, `l10n_br_sales`, `l10n_ec_sale`, `l10n_fi_sale`, `l10n_in_sale`, `l10n_it_edi_doi`, `l10n_it_edi_sale` … (+33); open-license custom/third-party scanned: `auto_gen_job_type`, `base_accounting_kit`, `bh_parent_company`, `courier_type`, `delivery_split`, `product_brand_sale`, `sale_gross_profit_record`, `sale_job_type` … (+5)
- `sale.order.line` ← Community: `delivery`, `event_booth_sale`, `event_sale`, `pos_repair`, `pos_sale`, `pos_sale_loyalty`, `repair`, `sale_expense`, `sale_expense_margin`, `sale_gelato` … (+25); open-license custom/third-party scanned: `delivery_split`, `order_line_sequence`, `product_3d_viewer`, `product_brand_sale`, `sale_gross_profit_record`, `sale_order_line_price_history`, `scgl_so_section_bydivision`, `scgl_sol_global_discount` … (+2)
- `sale.report` ← Community: `pos_sale`, `pos_sale_margin`, `sale_margin`, `sale_project`, `sale_stock`, `website_sale`; open-license custom/third-party scanned: `delivery_split`, `product_brand_sale`
- This module's own extension of other modules' objects: `base.document.layout`, `res.config.settings`, `payment.link.wizard`, `payment.provider`, `crm.team`, `account.move`, `utm.mixin`, `payment.transaction`, `ir.actions.report`, `portal.mixin`, `product.catalog.mixin`, `mail.thread`, `mail.activity.mixin`, `account.document.import.mixin`, `account.move.line`, `analytic.mixin`, `product.document`, `product.template`, `product.product`, `product.attribute.custom.value`, `res.company`, `ir.config_parameter`, `utm.campaign`, `account.analytic.line`, `account.analytic.applicability` … (+4)

## 6. Actions / states / validation / automation / security
- State fields found: `sale.order` → ['draft', 'sent', 'sale', 'cancel']
- Validation: 7 declarative constraint method(s), 5 database-level uniqueness/check declaration(s) (declared in code)
- Automation: automatic invoicing: send ready invoice every 1 days; Sales: Send pending emails every 1 days
- Security: groups declared 4 (`group_auto_done_setting`, `group_discount_per_so_line`, `group_warning_sale`, `group_proforma_sales`); record rules 27 (of which company-scoped by text 3); access rows 39

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 135 of 135 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map Trace Note — `sale`
Source revision: Odoo Community `19.0.post20260921` (paths relative to addons root). Read-only trace; neutral business language; no code copied.
Markers: (TEST) = derived from module tests only. `UNKNOWN — EVIDENCE INSUFFICIENT` = not verified.

## 1. Capabilities and classification
- Manifest: label "Sales internal machinery"; depends on sales_team, account_payment (which brings account, payment, portal) and utm; NOT flagged application, NOT auto_install; installable (`sale/__manifest__.py:4,11-15,63`; no application/auto_install keys present).
- Core (always on once installed): quotation/sales-order document with lines, sections/notes, pricing (pricelist, taxes, discount), invoicing from order, customer portal view/sign/pay/decline, payment-transaction linkage, sales analysis report, salesperson/team assignment, product invoicing-policy flag (`sale/models/sale_order.py:34-330`, `sale/models/sale_order_line.py:12-330`, `sale/controllers/portal.py:106-450`).
- Optional feature groups (off until enabled in settings; no implied group in group definition): Lock Confirmed Sales, Discount on lines, Sale warnings on partner/product, Pro-forma invoices (`sale/security/res_groups.xml:4-18`; toggles `sale/wizard/res_config_settings.py:20-28`).
  - Lock: after confirmation the order is auto-locked (`sale/models/sale_order.py:1193,1200-1203`).
  - Discount: per-line discount display and pricelist "percentage" discount shown separately (`sale/models/product_pricelist_item.py:8-16`, `sale/models/sale_order_line.py:794-825`); enabling it forces pricelist group on (`sale/wizard/res_config_settings.py:87-90`).
  - Warnings: text assembled only for users in the warning group (`sale/models/sale_order.py:830-845`).
- Optional add-on modules offered via settings toggles (installation not performed by `sale` itself): delivery carriers, sale_amazon, commission, gelato, loyalty, margin, pdf quote builder, product matrix, shopee, product_email_template (`sale/wizard/res_config_settings.py:62-83`).
- Conditional company features: online signature (default on), online payment with prepayment percent (default off/100%), quotation validity 30 days (0 disables expiry), discount product, down-payment account (`sale/models/res_company.py:16-58`).
- Deferred outputs (crons) shipped INACTIVE; activated only by config parameters (`sale/data/ir_cron.xml:12,23`, `sale/const.py:4-7`, `sale/models/ir_config_parameter.py:27-45`, `sale/__init__.py:13-24`).

## 2. Business objects, relationships, lifecycle
- Sales order (`sale.order`), states: Quotation (draft) -> Quotation Sent (sent) -> Sales Order (sale) | Cancelled (cancel) (`sale/models/sale_order.py:26-31`). There is no "done" state in this revision; "locked" is a separate flag (`sale/models/sale_order.py:78-82`). A leftover reference to a `done` state exists in the mass-cancel wizard helper (`sale/wizard/mass_cancel_orders.py:28`).
- Order line (`sale.order.line`): product line, section, subsection, note; down-payment line; expense line; combo parent/child links (`sale/models/sale_order_line.py:63-81,139-159`). Line state mirrors the order's state (`sale/models/sale_order_line.py:56-59`).
- Order -> invoices via line-to-invoice-line link; invoice_ids derived from lines, includes refunds made from invoices (`sale/models/sale_order.py:570-579`; link table `sale/models/sale_order_line.py:257-261`; reverse link `sale/models/account_move_line.py:12-16`).
- Order <-> payment transactions (many-to-many) (`sale/models/sale_order.py:258-263`, `sale/models/payment_transaction.py:14`).
- Per-line quantity ledger: ordered, delivered, invoiced, to-invoice; line invoice status: nothing / to invoice / upselling / fully invoiced (`sale/models/sale_order_line.py:230-262,1057-1115`). Order status is a roll-up of line statuses, excluding down-payment and display lines (`sale/models/sale_order.py:619-665`).
- State movers:
  - draft -> sent: mark-as-sent action, or sending the quotation by email, or a pending payment transaction (`sale/models/sale_order.py:1158-1166,1716-1720`, `sale/models/payment_transaction.py:47-54`).
  - draft/sent -> sale: confirm action (backend), portal signature, or sufficient payment (`sale/models/sale_order.py:1168-1198`, `sale/controllers/portal.py:318-345`, `sale/models/payment_transaction.py:108-133`).
  - any of draft/sent/sale -> cancel: cancel action (hidden when locked), portal decline, mass cancel (`sale/models/sale_order.py:1326-1335`, `sale/controllers/portal.py:368-398`, `sale/wizard/mass_cancel_orders.py:31-32`, button visibility `sale/views/sale_order_views.xml:359-364`).
  - cancel/sent -> draft: reset action; clears signature (`sale/models/sale_order.py:1060-1067`).
  - locked flag: lock/unlock actions; UI restricts both to sales Administrator (`sale/models/sale_order.py:1320-1324`, `sale/views/sale_order_views.xml:348-353,370-377`); the methods themselves carry no group check.

## 3. Actions, gates, constraints, automation, security
### Validation gating each action
- Confirm: order must be draft/sent; every non-section, non-down-payment line must have a product; analytic-distribution rules validated for draft/sent lines (`sale/models/sale_order.py:1205-1218,1182`; `sale/models/sale_order_line.py:1580-1586`). Confirmation stamps order date = now (`sale/models/sale_order.py:1220-1231`). No credit-limit hard block in this module: credit limit yields a warning text only (`sale/models/sale_order.py:786-797`). No approval / double-validation workflow found in module (no approval code in `sale/`; search returned nothing).
- Cancel: refused if order locked (`sale/models/sale_order.py:1328-1329`); cancels only draft invoices of the order, posted invoices untouched (`sale/models/sale_order.py:1332-1335`). Mass-cancel and portal decline call the inner cancel directly, bypassing the locked check (`sale/wizard/mass_cancel_orders.py:32`, `sale/controllers/portal.py:376`).
- Delete: only draft or cancelled orders (`sale/models/sale_order.py:1034-1040`); confirmed-order lines cannot be removed (set quantity to 0), except uninvoiced down-payment lines (`sale/models/sale_order_line.py:1464-1485`).
- Pricelist change blocked on confirmed order (`sale/models/sale_order.py:1042-1045`). On a locked order, product, description, price, unit, quantity, taxes, analytic and discount cannot be edited (`sale/models/sale_order_line.py:1413-1441`). Product change blocked once delivered/invoiced/locked/down-payment (`sale/models/sale_order_line.py:1261-1274,1391-1396`).
- Portal signature: allowed only for draft/sent, unexpired, signature-required, unsigned order; payment still required afterwards if configured (`sale/models/sale_order.py:1896-1937`, `sale/controllers/portal.py:318-345`). Decline needs a message and a still-signable order (`sale/controllers/portal.py:368-398`).
- Auto-confirm by payment: exactly one quotation per transaction, no pending signature, prepayment amount reached (`sale/models/payment_transaction.py:108-133`, `sale/models/sale_order.py:2105-2132`). (TEST) payment does not confirm when signature still pending (`sale/tests/test_payment_flow.py:332-339`); partial payment below prepayment leaves order draft (`sale/tests/test_payment_flow.py:318-330`).
- Invoicing: nothing-to-invoice raises an error unless suppressed; invoiceable lines are those with positive to-invoice quantity (negative only on "final") plus notes/sections; down payments grouped at the end (`sale/models/sale_order.py:1501-1544,1616-1617`). Down-payment amount must be positive (`sale/wizard/sale_make_invoice_advance.py:112-117`). Discount percent <= 100% (`sale/wizard/sale_order_discount.py:32-39`).
### Constraints
- DB: confirmed order requires order date (`sale/models/sale_order.py:42-45`); line: accountable line needs product+unit unless section/down-payment; non-accountable line must be zero-valued (`sale/models/sale_order_line.py:20-27`); company validity days >= 0 (`sale/models/res_company.py:11-14`).
- Python: order lines' products must belong to the order's company or its accessible branches (`sale/models/sale_order.py:849-864`); prepayment percent within (0,1] when payment required (`sale/models/sale_order.py:866-870`, `sale/models/res_company.py:60-64`); combo item must match the linked combo line (`sale/models/sale_order_line.py:1305-1321`); product cannot be restricted to a company if already sold in another company (`sale/models/product_template.py:108-132`).
### Automation
- Cron "Sales: send pending emails" (daily, inactive by default): sends queued confirmation/payment mails; queue is used only when `sale.async_emails` is true and cron active (`sale/data/ir_cron.xml:15-24`, `sale/models/sale_order.py:1259-1317`).
- Cron "automatic invoicing: send ready invoice" (daily, inactive by default): sends posted, unsent invoices of paid transactions from the last 2 days; also triggered when an invoice becomes ready (`sale/data/ir_cron.xml:4-13`, `sale/models/payment_transaction.py:180-199`, `sale/models/account_move.py:147-156`).
- Config parameters toggle those crons on write/create/delete; module install re-syncs them (`sale/models/ir_config_parameter.py:12-37`, `sale/__init__.py:18-21`).
- Upsell activity scheduled for the salesperson when order status turns "upselling" (`sale/models/sale_order.py:1966-1992`).
- Email templates: quotation, confirmation, payment executed, pro-forma (`sale/models/sale_order.py:1125-1156,1248-1257`); default templates held in config parameters (`sale/data/ir_config_parameter.xml:4-17`).
- Chatter subtypes for sent / confirmed / viewed (`sale/data/mail_message_subtype_data.xml:4-21`).
### Security
- Roles come from sales_team (own documents / all documents / administrator); `sale` defines no role groups, only the four feature groups (`sales_team/security/sales_team_security.xml:9-32`, `sale/security/res_groups.xml`).
- Order access: portal read-only; accountant readers read; invoicing users read/write; salesperson create/write (no delete); Administrator full (`sale/security/ir.model.access.csv:28-33`). Line: salesperson may also delete (`sale/security/ir.model.access.csv:35-39`).
- Record rules: company scoping on order, line, report (`sale/security/ir_rules.xml:5-21`); salesperson sees own or unassigned orders/lines; "all documents" role sees all (`sale/security/ir_rules.xml:44-83`); portal sees orders of its commercial partner tree (`sale/security/ir_rules.xml:24-40`); salespeople get widened invoice, invoice-line, payment transaction/token visibility (`sale/security/ir_rules.xml:85-144`).
- (TEST) role matrix tests exist: `sale/tests/test_access_rights.py:34-190`.
### Multi-company
- Company-scoped rules and `_check_company_auto` on order/line/company (`sale/models/sale_order.py:39`, `sale/models/sale_order_line.py:18`). Sequence, note terms, pricelist, team, journal, payment term all resolved per order company (`sale/models/sale_order.py:1012,382-395,443-452,491-505`). Credit-to-invoice for partner is computed for the current company only (`sale/models/res_partner.py:83-113`).

## 4. Cross-module handoffs (owner in brackets)
- To Accounting [account, owner of invoice/posting]: invoice creation from order lines; grouped by company, customer, delivery address, currency, fiscal position (`sale/models/sale_order.py:1413-1452,1483-1484,1552-1694`); created in elevated mode so salespeople without billing rights can invoice (`sale/models/sale_order.py:1546-1550`). Final invoice with negative total becomes a credit note (`sale/models/sale_order.py:1683-1686`).
- From Accounting: posting/cancelling/resetting a down-payment invoice refreshes the order's down-payment line price/tax/description unless the order is locked (`sale/models/account_move.py:83-118`); deleting a draft down-payment invoice removes its order line (`sale/models/account_move.py:26-31`); invoice paid posts a note on the order (`sale/models/account_move.py:135-145`); invoiced quantity follows invoice lines, credit notes reduce it, cancelled invoices ignored (`sale/models/sale_order_line.py:1007-1026`). Credit notes reduce the invoiced quantity of linked order lines (`sale/models/sale_order_line.py:1022-1025`); the source comment says this is intended for refunds generated from the order (`sale/models/sale_order_line.py:984-990`), and copied invoice lines keep their order-line link (`sale/models/account_move_line.py:36-39`); resulting effect for refunds raised directly from an invoice: UNKNOWN — EVIDENCE INSUFFICIENT.
- Down payments: wizard creates hidden order lines and a down-payment invoice; account from company setting, else product accounts; fiscal-position mapped (`sale/wizard/sale_make_invoice_advance.py:138-251`).
- Payment [payment/account_payment owns transaction]: post-processing of transactions confirms orders, sends status mails, and (if `sale.automatic_invoice`) creates a final invoice for fully paid orders or a down-payment invoice for partly paid ones, then posts and mails it (`sale/models/payment_transaction.py:40-107,201-227`). Posting an invoice auto-reconciles it with the linked payments (`sale/models/account_move.py:120-133`). Automatic invoicing forced off when default invoicing policy is not "ordered" (`sale/wizard/res_config_settings.py:123-126`).
- Analytics/expenses [analytic, account]: vendor-bill cost lines can generate re-invoice order lines on a confirmed, unlocked order; draft/sent/cancelled/locked target raises error (`sale/models/account_move_line.py:48-119`); delivered quantity for expense lines from analytic entries (`sale/models/sale_order_line.py:883-981`).
- CRM/teams [sales_team, crm]: team invoiced-this-month and order count; team deletion blocked at >=5 active orders (`sale/models/crm_team.py:22-84`). Campaign/UTM statistics (`sale/models/utm_campaign.py:18-59`).
- Inventory [stock]: none in `sale` (delivered quantity is manual/analytic only here); stock behaviour is added by `sale_stock` (`sale/models/sale_order_line.py:883-896` comment).
- Audit: tracked fields (customer, pricelist, salesperson, team, state, amounts) with chatter; draft-order tracking suppressed from catalog edits (`sale/models/sale_order.py:65-72,196-235,1698-1714`); quantity changes on confirmed orders logged (`sale/models/sale_order_line.py:1443-1462`).
- Events/integration: EDI order import from attachment (`sale/models/sale_order.py:1876-1892`); payment link wizard (`sale/models/sale_order.py:1855-1872`).

## 5. Configuration and computed behaviour that changes outcomes
- Invoicing policy per product (ordered vs delivered): drives quantity to invoice; default from setting (`sale/wizard/res_config_settings.py:10-17`, `sale/models/sale_order_line.py:1057-1084`). Recomputing on product type change resets goods to "ordered" (`sale/models/product_template.py:162-164`).
- Signature / payment / prepayment %: per-company defaults copied onto each order at creation, editable per order (`sale/models/sale_order.py:352-366`).
- Validity date = today + company days; expired quotations cannot be signed/paid (`sale/models/sale_order.py:367-375,759-766`).
- Unit price = pricelist price (tax-inclusive/exclusive handled); a manually edited price is preserved; lines with invoiced quantity are not repriced; "Update prices" forces reprice (`sale/models/sale_order.py:1361-1382`, `sale/models/sale_order_line.py:589-636`).
- Taxes on line derive from product taxes mapped by order fiscal position; fiscal position follows customer + delivery address (`sale/models/sale_order_line.py:544-571`, `sale/models/sale_order.py:411-429`).
- Salesperson defaults from customer, else current user if salesperson; team from salesperson (`sale/models/sale_order.py:477-505`).
- Invoice/delivery addresses default from customer; terms note default from company invoice terms when the invoice-terms parameter is on (`sale/models/sale_order.py:380-409`).
- Discount product auto-created on first global discount if user has rights, else error (`sale/wizard/sale_order_discount.py:101-122`).
- Partner country/VAT cannot be edited once a sent/confirmed order exists (`sale/models/res_partner.py:54-81`).
- Product cannot change type or unit of measure after use in orders (`sale/models/product_product.py:44-51,101-124`).
- Down-payment account default seeded from chart template at install (`sale/__init__.py:24-33`).

## 6. Effective extension path (module names only)
- Extending `sale.order`: delivery, delivery_mondialrelay, event_booth_sale, event_sale, l10n_br_sales, l10n_ec_sale, l10n_fi_sale, l10n_in_sale, l10n_it_edi_doi, l10n_it_edi_sale, l10n_tw_edi_ecpay_website_sale, mass_mailing_sale, partnership, pos_sale, repair, sale_crm, sale_edi_ubl, sale_expense, sale_gelato, sale_loyalty, sale_loyalty_delivery, sale_management, sale_margin, sale_mrp, sale_pdf_quote_builder, sale_product_matrix, sale_project, sale_purchase, sale_purchase_stock, sale_stock, sale_timesheet, stock_delivery, stock_dropshipping, website_event_booth_sale, website_event_sale, website_sale, website_sale_collect, website_sale_gelato, website_sale_loyalty, website_sale_mondialrelay, website_sale_mrp, website_sale_slides, website_sale_stock.
- Extending `sale.order.line`: delivery, event_booth_sale, event_sale, pos_repair, pos_sale, pos_sale_loyalty, repair, sale_expense, sale_expense_margin, sale_gelato, sale_gelato_stock, sale_loyalty, sale_management, sale_margin, sale_mrp, sale_pdf_quote_builder, sale_product_matrix, sale_project, sale_project_stock, sale_purchase, sale_purchase_project, sale_service, sale_stock, sale_stock_margin, sale_stock_product_expiry, sale_timesheet, sale_timesheet_margin, stock_delivery, stock_dropshipping, website_event_booth_sale, website_event_sale, website_sale, website_sale_loyalty, website_sale_slides, website_sale_stock.
- Extending `sale.report`: pos_sale, pos_sale_margin, sale_margin, sale_project, sale_stock, website_sale.
- Direct dependents that auto-install when their dependencies are present: l10n_br_sales, l10n_din5008_sale, l10n_ec_sale, l10n_fi_sale, l10n_in_sale, l10n_it_edi_sale, mass_mailing_sale, sale_crm, sale_edi_ubl, sale_loyalty, sale_purchase, sale_sms, sale_stock, spreadsheet_dashboard_sale (manifest scan of `*/__manifest__.py`).
- Other direct dependents (not auto-install): delivery, l10n_it_edi_doi, partnership, sale_gelato, sale_management, sale_product_matrix, website_sale.

## 7. UNKNOWN items
- Whether `account` blocks or warns on credit limit at confirmation beyond the warning text shown in `sale`: UNKNOWN — EVIDENCE INSUFFICIENT.
- Exact behaviour of the sales analysis report filters beyond "done states = sale" and non-display lines (`sale/report/sale_report.py:16-19,192-196`): views/measures not traced; UNKNOWN — EVIDENCE INSUFFICIENT.
- Portal payment routes, combo/product configurator internals and email template bodies: not traced beyond entry points; UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether any access group is required for customers of type "public" to trigger `action_confirm` via portal beyond token check: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether the leftover `done` reference in the mass-cancel helper has any runtime effect (no such state exists): UNKNOWN — EVIDENCE INSUFFICIENT.

