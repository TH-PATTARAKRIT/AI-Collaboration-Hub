> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: scgl_pos_payment_ext

## 0. Header
- Module: scgl_pos_payment_ext
- License (confirmed in manifest): LGPL-3 (scgl_pos_payment_ext/__manifest__.py:24)
- Author (manifest): SCGL (scgl_pos_payment_ext/__manifest__.py:7)
- Version (manifest): 19.0.1.0.1 (scgl_pos_payment_ext/__manifest__.py:3)
- Path: addons_Extramodule/addons/scgl_pos_payment_ext
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Adds a Thai PromptPay QR payment option to Point of Sale: a flag on a payment method ("Is Prompt Payment"), a QR code generated locally from the company's PromptPay identifiers, and display of the account holder name on the cashier QR pop-up and the customer-facing display (models/pos_payment_method.py:26-27, :67-125; views/pos_payment_method_view.xml:8-13; static/src/customer_display/customer_facing_qr.xml:5-28; static/src/app/services/pos_store.js:10-61).
- Company gets an extra text field "Account Holder name" (models/res_config_settings.py:8-10; views/res_config_settting_views.xml:9-13).
- Business rule enforced: a PromptPay payment method can only be created/enabled when the current company has a biller identifier, a PromptPay company identifier and a holder name (models/pos_payment_method.py:52-65). The identifier fields are defined outside this module (see section 5).
- The QR payload format follows the PromptPay/EMV convention with amount, currency code THB and country TH (models/pos_payment_method.py:91-109).

## 2. Attachment to CORE
- Depends declared: point_of_sale and invoice_promptpay (manifest:8).
- Core objects extended: `pos.payment.method` (core:point_of_sale/models/pos_payment_method.py), `res.company`, form views `point_of_sale.pos_payment_method_view_form` (core:point_of_sale/views/pos_payment_method_views.xml:3; anchors `payment_method_type` :33 and `qr_code_method` :35) and `base.view_company_form`, POS front-end store and customer display.
- Overrides by name:
  - `_check_payment_method` constraint (models/pos_payment_method.py:37-50): REPLACES the core constraint of the same name (core:point_of_sale/models/pos_payment_method.py:202-212). ALTERS CORE CONTROL: the core requirement "bank account on journal + QR method selected" is skipped for payment methods flagged PromptPay (condition at :40). Non-PromptPay QR methods keep the same checks. (The override refers to `self` instead of the loop record at :47, mirroring the core style at core:point_of_sale/models/pos_payment_method.py:210; multi-record behaviour untested.)
  - `get_qr_code` (models/pos_payment_method.py:67-125): ADDS before core for PromptPay methods (builds its own QR image with the report barcode helper, core:base/models/ir_actions_report.py:688), otherwise calls core (core:point_of_sale/models/pos_payment_method.py:242-253). Core would raise "not configured to generate QR codes" unless method type is QR; PromptPay flag bypasses that check.
  - `write` (:52-56) and `create` (:58-65): ADD a pre-check; they test the CURRENT company of the session, not the method's own company (inference from `self.env.company`), and raise a plain value error rather than a user-facing validation error.
  - `_load_pos_data_fields` (:127-131): ADDS `holder_name` to the data loaded to the POS front end (core list at core:point_of_sale/models/pos_payment_method.py:81-82).
  - Front-end `showQR` on the POS store (static/src/app/services/pos_store.js:10-61): REPLACES the core function (core:point_of_sale/static/src/app/services/pos_store.js:2832) with a copy that adds the holder name in the pop-up data (:44). Drift risk when core changes.
  - Customer display QR component: adds a `holder_name` prop (static/src/customer_display/customer_facing_qr.js:5-10; core component core:point_of_sale/static/src/customer_display/customer_facing_qr.js:4-14) and REPLACES the dialog body of the core template (static/src/customer_display/customer_facing_qr.xml:5-28; core template core:point_of_sale/static/src/customer_display/customer_facing_qr.xml:3).

## 3. New objects, security, automation, external calls
- New fields: `is_promptpay`, `holder_name` (computed, from company for PromptPay and from the journal's bank account otherwise, models/pos_payment_method.py:26-35) on payment method; `holder_name` on company (models/res_config_settings.py:8-10). No new models, ACLs, groups or record rules. Company scoping through the payment method's company.
- Data handling: payment method QR payload uses company-level payee identifiers and per-order text (order name suffix) — no credential or key handling in code. Logs the composed account section of the QR payload at info level (models/pos_payment_method.py:81, :84, :89), i.e. payee identifiers land in the server log (inference from log calls; content depends on configuration).
- Automation: none. External calls: none (local QR image only).

## 4. Odoo 19 compatibility
- Confirmed in Community 19: `qr_code_method`, `payment_method_type`, `_check_payment_method`, `get_qr_code`, `_load_pos_data_fields(config)` (core:point_of_sale/models/pos_payment_method.py:61-63, :81, :202, :242), POS asset bundles `point_of_sale._assets_pos` and `point_of_sale.customer_display_assets` (core:point_of_sale/__manifest__.py:145, :224), `showQR` (core:point_of_sale/static/src/app/services/pos_store.js:2832).
- Absent from the Community 19 tree: an element named `qr_code_right_pane` on the company form (text search of core XML finds none), the anchor used at views/res_config_settting_views.xml:9. It must come from invoice_promptpay; otherwise the company view fails to load.
- Defects visible from reading: (a) the error branch of the Python QR method raises an exception through a library name that is not imported in the file (models/pos_payment_method.py:121; imports at :1-7); (b) the front-end file uses `_t`, `ConnectionLostError` and `AlertDialog` without importing them (static/src/app/services/pos_store.js:26-36 vs imports :1-8), so the error path would fail with a reference error; (c) the file's `holder_name` prop patch on the customer-display component relies on the core static props object; not runtime-tested.

## 5. Custom-to-custom dependencies
- Depends on invoice_promptpay (company fields `biller_id`, `company_promptpay` used at models/pos_payment_method.py:54, :72, :74). That module's source is outside this assignment.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: where the `qr_code_right_pane` company-form anchor is defined (presumably invoice_promptpay).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the QR payload meets the current banking-scheme specification; only the structure was read.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the info-level log lines expose payee identifiers in production logs.
