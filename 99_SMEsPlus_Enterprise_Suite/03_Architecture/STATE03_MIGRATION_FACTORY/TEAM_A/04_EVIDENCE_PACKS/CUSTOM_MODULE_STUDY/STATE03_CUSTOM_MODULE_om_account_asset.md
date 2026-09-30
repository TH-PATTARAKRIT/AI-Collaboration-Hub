> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 custom module trace: om_account_asset

Module: om_account_asset · License (confirmed in manifest): LGPL-3 (om_account_asset/__manifest__.py:12)
Author (manifest): Odoo Mates, Odoo SA (manifest:4) · Version (manifest): 1.0.1 (manifest:3; name string says "Odoo 19 Assets Management", manifest:2)
Path: addons_Extramodule/addons_extra/om_account_asset
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Fixed-asset and deferred-revenue management: asset types (categories) hold accounts, journal, depreciation method (linear/degressive), number/length of periods, prorata, and grouping options (om_account_asset/models/account_asset.py:19-108).
- Assets carry gross value, salvage value, a depreciation board, residual value and states draft/running/closed (models/account_asset.py:131-215, 314-379, 467-475).
- Assets are created automatically from vendor-bill or customer-invoice lines that carry an asset type, optionally auto-confirmed (models/account_move.py:114-140; category flag "Auto-Confirm Assets", account_asset.py:87-91).
- Monthly scheduled job and a manual wizard generate depreciation journal entries; disposal, duration modification and an analysis report are provided (data/account_asset_data.xml:6-13; wizard/asset_depreciation_confirmation_wizard.py:16-28; models/account_asset.py:422-462; wizard/asset_modify.py:40-73; report/account_asset_report.py).

## 2. Attachment to CORE
- Depends on core `account` only (manifest:5). Uses `mail.thread`, `mail.activity.mixin`, `analytic.mixin` on its own models (account_asset.py:22, 134).
- `account.move` (models/account.py:7-11 and models/account_move.py:6-11): adds links to depreciation lines and to created assets.
- `account.move.line` (models/account_move.py:55-72): adds asset type per line and computed start date, end date and monthly recurring revenue (stored).
- `product.template` (models/product.py:4-14): adds company-dependent Asset Type and Deferred Revenue Type.
- Core view/menu hooks: `account.view_move_form`, `account.product_template_form_view`, menus `account.account_account_menu`, `account.menu_finance_entries`, `account.account_reports_management_menu` (views/account_move_views.xml:7-17; views/product_views.xml:28-35; views/account_asset_views.xml:231-235; report/account_asset_report_views.xml:81-84).
- Core method overrides (by name):
  - `account.move.action_post` (models/account.py:19-23): ADDS behavior BEFORE core - re-evaluates linked depreciation lines and may close the asset.
  - `account.move.action_post` (models/account_move.py:45-52): ADDS behavior AFTER core - creates assets from posted invoice lines. Both files define the class over the same model; the later-loaded definition order follows models/__init__.py:3-5.
  - `account.move.button_draft` (models/account_move.py:13-23): ALTERS CORE CONTROL (reset to draft) - runs after core, then BLOCKS with an error when any linked asset is no longer draft; otherwise deactivates linked assets with elevated rights and logs "Vendor bill cancelled".
  - `account.move.action_cancel` (models/account_move.py:35-43): ADDS behavior after parent - deactivates assets of the invoice with elevated rights. This method is not defined for account.move in Community 19 (see section 4).
  - `account.move.button_cancel` (models/account.py:13-17): ADDS behavior before core - clears the "posted" flag on depreciation lines of the entry.
  - `account.move._refund_cleanup_lines` (models/account_move.py:25-33): ADDS - blanks the asset type on credit-note lines. Not found in core 19.
  - `account.move.line._inverse_product_id` (models/account_move.py:149-157): ADDS - fills asset type from the product depending on move type (out_invoice / in_invoice only).
  - `account.move.line.default_get` (:74-85), `get_invoice_line_account` (:159-160): default/account selection from asset type; REPLACES the expense/income account choice with the asset account when a category exists (but see section 4).
  - `product.template._get_asset_accounts` (models/product.py:16-22): ADDS/changes the stock input/output account mapping.
- Depreciation entries are posted through core `action_post` on ordinary journal entries (account_asset.py:612-624), so core posting and lock-date checks apply unchanged. No override of lock dates, valuation/cost or numbering found.
- Validation added: a stored computed field raises an error when the selected asset type has zero periods or zero period length (models/account_move.py:95-97).

## 3. New objects, security, automation, external calls
- Models: account.asset.category, account.asset.asset, account.asset.depreciation.line (persistent); asset.modify, asset.depreciation.confirmation.wizard (transient); asset.asset.report (database view, `_auto = False`, report/account_asset_report.py:4-7).
- ACLs (security/ir.model.access.csv:2-14): Accountant (`account.group_account_user`) read-only on categories, assets, lines, report; Manager full; Invoicing group (`account.group_account_invoice`) read on category, read+create on assets and lines (needed when posting invoices); wizards create/write for Accountant.
- Record rules: four global multi-company rules on category, asset, depreciation line (via asset), and report (security/account_asset_security.xml:6-32), all `noupdate`.
- Cron: "Account Asset: Generate asset entries", monthly, runs all open assets across companies and creates (and, for categories with auto-confirm, posts) due depreciation moves (data/account_asset_data.xml:6-13; models/account_asset.py:228-247, 536-543, 612-624).
- Deletion guards: asset cannot be deleted when running/closed or holding entries (account_asset.py:219-226); posted depreciation lines cannot be deleted (:755-762).
- No external network calls found.

## 4. Odoo 19 compatibility (grep against Community 19)
- MISMATCH: `super().action_cancel()` on account.move (models/account_move.py:36); core account.move has no such method (only `button_cancel` at core:account/models/account_move.py:6384; `action_cancel` exists only on payments, core:account/models/account_payment.py:1156).
- MISMATCH: `super()._get_asset_accounts()` (models/product.py:17); not found under core account, stock_account or product.
- MISMATCH: `super()._refund_cleanup_lines` (models/account_move.py:27) and `get_invoice_line_account` (:159-160); no definitions found in core account/stock_account/product.
- Found: `button_draft` (core:account/models/account_move.py:6269), `action_post` (:6180), `button_cancel` (:6384), `_inverse_product_id` (core:account/models/account_move_line.py:1406), `_mail_track` (core:mail/models/models.py:226), `analytic.mixin` (core:analytic/models/analytic_mixin.py:13), and the four view/menu references above.
- Observation (not run): the asset-close check called by `action_post` runs before core posting (models/account.py:19-23 versus account_asset.py:721-733), so the entry being posted is still draft at that moment; effect on when assets reach the closed state: UNKNOWN - EVIDENCE INSUFFICIENT.
- Two identical-named classes both extend account.move across account.py and account_move.py: allowed, but the file `models/account.py` is misleadingly named.

## 5. Custom-to-custom dependencies
- None declared. Note: sibling module om_account_daily_reports depends on `accounting_pdf_reports` (not this module).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Behavior of the Odoo Mates deferred-revenue flows when core Community 19 also ships its own deferral accounts (core test helper mentions a deferred revenue default account, core:account/tests/common.py:369): UNKNOWN - EVIDENCE INSUFFICIENT.
- Whether the three unresolved super-calls raise at runtime in 19 (code not run): UNKNOWN - EVIDENCE INSUFFICIENT.
- Multi-currency and prorata edge cases in the depreciation board (account_asset.py:248-379): UNKNOWN - EVIDENCE INSUFFICIENT (not analysed in depth).
