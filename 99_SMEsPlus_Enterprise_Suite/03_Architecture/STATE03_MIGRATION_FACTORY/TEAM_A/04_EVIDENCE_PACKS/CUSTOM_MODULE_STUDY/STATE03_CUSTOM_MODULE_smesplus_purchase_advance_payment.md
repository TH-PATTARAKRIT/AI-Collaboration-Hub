> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_purchase_advance_payment

Module: smesplus_purchase_advance_payment ("Purchase Advance Payment")
License (confirmed in manifest): LGPL-3
Author (manifest): SMEsPlus
Version (manifest): 1.0.0 (no Odoo series prefix)
Path: addons_Extramodule/addons_extra/smesplus_purchase_advance_payment
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_07): Company Extra/Custom

## 1. Business capability
- From a confirmed purchase order, lets purchasing/accounting raise a vendor bill for an advance (down payment) instead of billing received goods: either a percentage of the order or a fixed amount (smesplus_purchase_advance_payment/wizard/purchase_advance.py:44-51, 113-122; wizard/view_purchase_adv_wizard.xml:14-36).
- The advance is recorded on the purchase order itself under a "Down Payments" section with a down-payment line, so it shows against the order (wizard/purchase_advance.py:97-111, 124-148, 194-201).
- The vendor bill is created in draft, with a chatter note pointing back to the purchase order (wizard/purchase_advance.py:203-211; wizard/view_purchase_adv_wizard.xml:9-11).
- A default "advance payment product" (service) can be set in Purchase settings; if none is set the wizard creates a "Down payment" service product and remembers it (models/res_config_settings.py:7-12; wizard/purchase_advance.py:186-191).
- Only one order at a time can be processed (wizard/purchase_advance.py:181; the regular-bill option is commented out at :45).

## 2. Attachment to CORE
- Core module depended on: purchase (__manifest__.py:1-18). Also relies on account objects that purchase brings in (account.move, account.tax, account.account).
- purchase.order.line (core:purchase/models/purchase_order_line.py): field is_downpayment is REDECLARED (models/purchase_order_line.py:7-10) although core 19 already has it (core:purchase/models/purchase_order_line.py:102). Effect: label/help text replaced only.
- purchase.order.line method _prepare_invoice_line (models/purchase_order_line.py:12-37): in Community 19 no method of this name exists; the bill-line builder is _prepare_account_move_line (core:purchase/models/purchase_order_line.py:628-646), which the standard "create bill" action uses (core:purchase/models/purchase_order.py:760-790). So this is a NEW method used only by the wizard (wizard/purchase_advance.py:167), not an override of an active core path.
- purchase.order form (core:purchase/views/purchase_views.xml:110): the view replaces the FIRST button whose technical name contains "invoice" or "bill" with a "Create Advance Bill" button (view/purchase_view.xml:10-14). In the Community 19 form the first match in document order appears to be the "Bill Matching" smart button (core:purchase/views/purchase_views.xml:167-172); an inference from document order, not confirmed at runtime. A second button is added before "Send RFQ" (view/purchase_view.xml:18-22). The visibility conditions of the two buttons overlap on invoice_status; not analysed further.
- Purchase settings form: adds a "Down Payments" setting into the Invoicing block (view/res_config_settings_views.xml:9-12; core:purchase/views/res_config_settings_views.xml:41); help link points to a 16.0 sales document (:10).
- Bill creation: creates the vendor bill with elevated rights and then returns it under the user (wizard/purchase_advance.py:203-205). This lets a user who can open the wizard create an account.move regardless of their own create right on it - ALTERS CORE CONTROL (security/access on bill creation). Post is not done by the module (bill stays draft), so posting controls, lock dates and numbering are untouched here.
- Core purchase already ships its own down-payment support (core:purchase/models/purchase_order.py:724-758 and core:purchase/wizard/bill_to_po_wizard.py:68) that this module does not use; overlap not analysed.

## 3. New objects, security, automation, external calls
- New models: purchase.advance.payment.bill (transient wizard) (wizard/purchase_advance.py:7-9). Setting: config parameter purchase.advance_default_product_id.
- ACL: full read/write/create/delete on the wizard for every internal user (security/ir.model.access.csv:2). No groups created; no record rules; company handled by taking the order's company (wizard/purchase_advance.py:66-76).
- The expense-account field on the wizard is restricted to the accounting manager group in the view (wizard/view_purchase_adv_wizard.xml:42-45) but the same user can still trigger the flow.
- Cron, server actions, external calls: none. Config parameter written with elevated rights (wizard/purchase_advance.py:190-191).

## 4. Odoo 19 compatibility - mismatches
- Domain on account.account uses field deprecated (wizard/purchase_advance.py:60); Community 19 account.account has an active flag (core:account/models/account_account.py:42) and no such field (only a stale mention at :1075).
- Product creation values use invoice_policy (wizard/purchase_advance.py:91), a field defined by the sale module (core:sale/models/product_template.py:35), while this module depends only on purchase.
- Expense account default calls the product-accounts helper on a possibly empty product (wizard/purchase_advance.py:22): would fail when no default product is set. Not run.
- The section line is created with product_uom_qty and product_qty zero (wizard/purchase_advance.py:102, 106); both exist on purchase.order.line in 19 (core:purchase/models/purchase_order_line.py:23-24), consistent.
- Order line list attribute check for `order_line==[]` in view (view/purchase_view.xml:21): not verified against 19 attribute syntax.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: how the advance is netted against the final bill (the "deduct down payments" option is only shown for a disabled regular-bill mode; wizard/view_purchase_adv_wizard.xml:17-23).
- UNKNOWN - EVIDENCE INSUFFICIENT: which button of the core PO form is actually replaced at runtime.
- UNKNOWN - EVIDENCE INSUFFICIENT: tax treatment of the advance (VAT/withholding) beyond copying supplier taxes of the product (wizard/purchase_advance.py:25-26, 94).
