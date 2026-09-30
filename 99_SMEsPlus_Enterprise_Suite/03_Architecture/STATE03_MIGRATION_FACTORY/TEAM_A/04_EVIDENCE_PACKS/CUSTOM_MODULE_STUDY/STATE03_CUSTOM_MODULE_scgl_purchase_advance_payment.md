> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_purchase_advance_payment

Module: scgl_purchase_advance_payment
License (confirmed in manifest): LGPL-3 (scgl_purchase_advance_payment/__manifest__.py:17)
Author (manifest): SCGL (scgl_purchase_advance_payment/__manifest__.py:7)
Version (manifest): 1.0.0 (scgl_purchase_advance_payment/__manifest__.py:6)
Path: addons_Extramodule/addons/scgl_purchase_advance_payment
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Lets a purchaser create a DRAFT vendor bill for an advance (down payment) directly from a confirmed purchase order, either as a percentage of the order or as a fixed amount (scgl_purchase_advance_payment/wizard/purchase_advance.py:44-47, 113-122).
- The wizard states the bill is created in draft for review before validation (scgl_purchase_advance_payment/wizard/view_purchase_adv_wizard.xml:8-11). Only one order at a time is supported for this path (scgl_purchase_advance_payment/wizard/purchase_advance.py:181).
- Adds a "Down Payments" section and a down-payment line (quantity zero, price = advance amount) to the order, so the advance is visible on the PO (scgl_purchase_advance_payment/wizard/purchase_advance.py:193-201).
- A purchase setting selects the default "advance product" (service type) (scgl_purchase_advance_payment/models/res_config_settings.py:7-12; scgl_purchase_advance_payment/view/res_config_settings_views.xml:10-12). If none is set, the wizard creates a product named "Down payment" and stores it as the default (scgl_purchase_advance_payment/wizard/purchase_advance.py:186-191).
- The "regular bill" option is commented out (scgl_purchase_advance_payment/wizard/purchase_advance.py:45, 177-179); the "deduct down payments" flag exists but only feeds that dead branch (scgl_purchase_advance_payment/wizard/purchase_advance.py:51, view_purchase_adv_wizard.xml:17-22).

Accounting entries and approvals (business level)
- The module itself posts nothing and creates no journal entry. It creates one draft vendor bill with one line: the advance product, quantity 1, unit price = advance amount, description "Down payment of N%" or "Down Payment", analytic split averaged from the order lines by value (scgl_purchase_advance_payment/wizard/purchase_advance.py:124-173).
- Journal entries arise only when the user posts the bill through core. Which account is debited depends on the advance product's expense account, chosen by default from the product/category/company expense account chain (scgl_purchase_advance_payment/wizard/purchase_advance.py:20-22, 93). The field is labelled "Expense Account" (scgl_purchase_advance_payment/wizard/purchase_advance.py:59). So by default the advance is directed to an expense account, not a prepayment/asset account. The account chosen in the wizard only applies when the wizard creates the product (view hides it once a product exists: view_purchase_adv_wizard.xml:42-45).
- No approval step, approval group or state is added. Buttons appear when the PO is in confirmed state (scgl_purchase_advance_payment/view/purchase_view.xml:13, 21). Core PO approval (state "to approve") happens before that and is unchanged.
- Any internal user may use the wizard (scgl_purchase_advance_payment/security/ir.model.access.csv:2). The bill is created with elevated rights and then handed back to the user (scgl_purchase_advance_payment/wizard/purchase_advance.py:203-205). Effect: a purchaser without accounting rights can create a draft vendor bill. ALTERS CORE CONTROL (bill-creation access; see section 2).

## 2. Attachment to CORE
- Depends on core `purchase` only (scgl_purchase_advance_payment/__manifest__.py:9); also uses `account` objects (bill, tax, account) through purchase.
- purchase.order.line: redeclares `is_downpayment` (scgl_purchase_advance_payment/models/purchase_order_line.py:7-10). Core Community 19 already has this field (core:purchase/models/purchase_order_line.py:102), so this only changes label/help text.
- purchase.order.line: adds new method `_prepare_invoice_line` (scgl_purchase_advance_payment/models/purchase_order_line.py:12-37). Core has no method of this name; core's equivalent is `_prepare_account_move_line` (core:purchase/models/purchase_order_line.py:628). ADDS a parallel path used only by this wizard; core method is not overridden.
- res.config.settings: ADDS setting `advance_default_product_id` stored in a config parameter (scgl_purchase_advance_payment/models/res_config_settings.py:7-12); placed inside core block "invoicing_settings_container" (core:purchase/views/res_config_settings_views.xml:41).
- Purchase order form (core:purchase/views/purchase_views.xml): button "Create Advance Bill" REPLACES the first button whose name contains "invoice" or "bill" (scgl_purchase_advance_payment/view/purchase_view.xml:10-14). In the Community 19 form the first such node is the "Bill Matching" stat button (core:purchase/views/purchase_views.xml:168). Business effect: the Bill Matching shortcut is likely removed from the PO form. ALTERS CORE CONTROL (UI entry point to bill matching). A second button is inserted before the first "Send RFQ" button (scgl_purchase_advance_payment/view/purchase_view.xml:18-21).
- No core Python method is overridden (no super calls in module).

## 3. New objects, security, automation, external calls
- New transient model purchase.advance.payment.bill (scgl_purchase_advance_payment/wizard/purchase_advance.py:7-9). ACL: full rights for all internal users (scgl_purchase_advance_payment/security/ir.model.access.csv:2). No record rules, groups, crons or server actions.
- Multi-company: wizard company follows the single selected order (scgl_purchase_advance_payment/wizard/purchase_advance.py:71-76) and bill is created in that company (line 182).
- Bill chatter gets a note linking to the source order (scgl_purchase_advance_payment/wizard/purchase_advance.py:207-211).
- No external calls.

## 4. Odoo 19 compatibility
- Mismatch: wizard field domain uses `deprecated` on account.account (scgl_purchase_advance_payment/wizard/purchase_advance.py:60); Community 19 account.account has `active`, no `deprecated` field (core:account/models/account_account.py:42). Selecting the account may error for account managers.
- Mismatch: product creation sets `invoice_policy` (scgl_purchase_advance_payment/wizard/purchase_advance.py:91); that field is defined by module `sale` (core:sale/models/product_template.py:35), not by purchase/account. The module does not depend on sale, so creating the default product could fail if sale is absent.
- Stale value: state "done" used in button conditions (scgl_purchase_advance_payment/view/purchase_view.xml:13, 21); Community 19 PO states are draft/sent/to approve/purchase/cancel (core:purchase/models/purchase_order.py:106-110).
- Line-section values pass `product_uom_qty` and `product_qty` (scgl_purchase_advance_payment/wizard/purchase_advance.py:102-106); core section rows require zero/empty quantity fields (core:purchase/models/purchase_order_line.py:109-111). Compatible only by value; not run-tested.
- Default amount is the count of selected orders (scgl_purchase_advance_payment/wizard/purchase_advance.py:55), so the percentage defaults to 1 for one order. Behavioral oddity.
- Percentage basis tests the product's customer taxes (`taxes_id`) rather than supplier taxes (scgl_purchase_advance_payment/wizard/purchase_advance.py:116); intent not confirmed.
- Field/method names otherwise present: `_prepare_invoice`, `action_view_invoice`, `qty_to_invoice`, `purchase_line_id`, `is_downpayment` on bill line (core:purchase/models/purchase_order.py:925; core:purchase/models/account_invoice.py:527).
- Documentation link in setting points to Odoo 16 docs (scgl_purchase_advance_payment/view/res_config_settings_views.xml:10). Cosmetic.

## 5. Custom-to-custom dependencies
- None declared. No scgl_* module referenced.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: how the advance is netted against the final vendor bill (module has no deduction logic; core down-payment handling in core:purchase/tests/test_purchase_downpayment.py was not followed through).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the deployed setup points the advance product to a prepayment/asset account instead of expense.
- UNKNOWN - EVIDENCE INSUFFICIENT: tax on the advance bill line (down-payment PO line sets no tax explicitly, scgl_purchase_advance_payment/wizard/purchase_advance.py:137-146).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior of the account default when no default product exists (scgl_purchase_advance_payment/wizard/purchase_advance.py:20-22 is evaluated on an empty product).
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the module installs cleanly on the target database (not run).
