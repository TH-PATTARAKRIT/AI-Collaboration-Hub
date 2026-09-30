> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: l10n_th_withholding_tax

- Module: l10n_th_withholding_tax
- License (confirmed in manifest): AGPL-3 (l10n_th_withholding_tax/__manifest__.py:8)
- Author (manifest): Ecosoft, Odoo Community Association (OCA) (l10n_th_withholding_tax/__manifest__.py:7)
- Version (manifest): 19.0.1.4 (l10n_th_withholding_tax/__manifest__.py:6); development status Beta (manifest:22). Model code carries a local "Refactored by SMEsPlus" note (l10n_th_withholding_tax/models/account.py:3), so the copy differs from a pure upstream copy.
- Path: addons_Extramodule/addons_extra/l10n_th_withholding_tax
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Thai withholding tax (WHT): separate master list of withholding rates linked to normal tax records flagged as WHT, with a designated liability account and tax-report grids (models/account.py:12-26, 48-99; models/account_withholding_tax.py:7-32).
- WHT can be chosen per invoice/bill line (defaults from the product: customer-side or supplier-side WHT) and the document shows a total WHT amount (models/account_move.py:9-28, 105-117; models/product.py:6-10).
- Payment registration reduces the amount paid by the WHT, books the difference to the WHT account and copies the tax grids (wizard/account_payment_register.py:16-26, 38-72).
- Thai PND withholding report rows are rebuilt from tax lines plus line-level WHT of paid documents, with a type label by rate (transport, advertising, service, rental) (models/tax_report_pnd.py:7-99).
- Selectable taxes and WHT on a bill are filtered by partner type (company versus individual) using words in tag names (models/account_move.py:39-103).

## 2. Attachment to CORE
- `account.tax` (core:account/models/account_tax.py): ADDS flag "Withholding Tax". Overrides `create` and `write` (ADDS behavior after core: keeps the WHT master in sync; BLOCKS saving a WHT-flagged tax whose first tax repartition line has a non-WHT account, models/account.py:28-37, 74-81). ALTERS CORE CONTROL: tax master-data validation. `write` runs the sync on every tax write, WHT or not. `toggle_active` override syncs archive state (models/account.py:101-109).
- `account.tax._add_accounting_data_to_base_line_tax_details` (core:account/models/account_tax.py:2369): ADDS behavior after core: appends the WHT tax's base-line tags to the base line (models/account_tax.py:7-22). ALTERS CORE CONTROL: tax-report tagging of journal items.
- `account.tax._prepare_base_line_grouping_key` (core:account/models/account_tax.py:2297): ADDS the line's WHT to the grouping key (models/account_tax.py:24-33). Effect on tax-line generation not run.
- `account.account`: ADDS flag "WT Account" (models/account.py:12-16). `account.move.line`: ADDS stored, editable `wt_tax_id` computed from product or payment; recomputed when product or account changes, which can overwrite a manual choice (models/account_move.py:9-28). `account.move`: ADDS stored `wht_amount` and non-stored lists used in domains (models/account_move.py:34-37). `account.payment`: ADDS `wt_tax_id` (models/account_payment.py:9-13). `product.template`: ADDS two WHT links (models/product.py:9-10).
- `account.payment.register` (core:account/wizard/account_payment_register.py):
  - `_create_payment_vals_from_wizard` (core:...:993): ADDS behavior after core: passes WHT and grid tags onto write-off lines when difference handling is reconcile (wizard/account_payment_register.py:16-26).
  - `_compute_amount` (core:...:741): ADDS behavior after core: lowers the default payment amount by the computed WHT, sets write-off account/label and the WHT (wizard/account_payment_register.py:38-72). ALTERS CORE CONTROL: default payment amount and write-off posting.
  - `_compute_payment_difference_handling` (core:...:862): REPLACES core behavior (no call to the core method; only sets reconcile when a WHT is chosen, wizard/account_payment_register.py:89-93). Core sets reconcile for early-payment-discount mode, open otherwise, or blank when the wizard is not editable. ALTERS CORE CONTROL: payment difference handling default.
  - `default_get` override only calls core (wizard/account_payment_register.py:74-87).
- `l10n_th.pnd.report.handler._rows` (Thai tax-report handler, not in Community): REPLACES the handler's row-building with a direct database read (models/tax_report_pnd.py:4-101). Not reproduced.
- Views: adds WHT column on bill/invoice lines and restricts the tax column domain (views/account_move_view.xml:8-40), account/tax/product/payment-wizard fields (views/account_view.xml, views/product_view.xml, wizard/account_payment_register_views.xml), and a menu "Withholding Tax" under Invoicing (views/account_withholding_tax.xml:67-77).
- Lock dates, valuation/cost, approvals, numbering: no override found. Posting-related effects are those noted above (write-off lines, tags).

## 3. New objects, security, automation, external calls
- New model: account.withholding.tax (models/account_withholding_tax.py:8) with company field required, default current company (line 26).
- ACL: full rights including delete for the invoicing group (security/ir.model.access.csv:2). Record rule: global multi-company rule (security/security.xml:2-7).
- Constraint: selected account must be flagged WHT (models/account_withholding_tax.py:28-32).
- Crons/server actions/external calls: none. Unit tests present (tests/test_withholding_tax.py).

## 4. Odoo 19 compatibility
- Checked by grep in Community tree.
- MISMATCH: manifest depends on `l10n_th_reports` (manifest:11). Community tree has `l10n_th` only (core:l10n_th); no `l10n_th_reports`, no model `l10n_th.pnd.report.handler`, no `_get_report_query` (grep negative). `models/tax_report_pnd.py:5` inherits that missing model; module cannot load on Community alone.
- MISMATCH: tables/fields used by the PND query (`res_partner_company_type`, `partner_company_type_id`, `partner.branch`; models/tax_report_pnd.py:24, 33, 48) not found in Community 19 (core:l10n_th has only `l10n_th_branch_name`, core:l10n_th/models/res_partner.py:9). Their source is UNKNOWN - EVIDENCE INSUFFICIENT.
- MISMATCH: `account.payment.move_line_ids` (wizard/account_payment_register.py:56) not found in Community 19 `account.payment` (core:account/models/account_payment.py; no such field).
- `toggle_active` is deprecated since 19.0 (core:odoo/orm/models.py:5802-5809); archive via the archive action may not run the override (models/account.py:101).
- `_compute_payment_difference_handling` override without core call (see section 2) diverges from core depends (core:account/wizard/account_payment_register.py:860-867).
- Test file imports `SavepointCase` (tests/test_withholding_tax.py:5), not available in Community 19 test tooling; tests not run.
- Present in core 19: hooks `_add_accounting_data_to_base_line_tax_details`, `_prepare_base_line_grouping_key`, `_create_payment_vals_from_wizard`, `_compute_amount`; fields `matched_payment_ids`, payment states canceled/rejected (core:account/models/account_payment.py:41-42), `tax_base_amount`, `tax_line_id`, `payment_id` on journal items; views view_move_form, view_tax_form, view_account_form, payment register form; menu account_invoicing_menu (core:account/views/account_menuitem.xml:59).
- Community 19 also ships its own native withholding module `l10n_account_withholding_tax` (core:l10n_account_withholding_tax/__manifest__.py:3, depends account); overlap with this module not analysed.

## 5. Custom-to-custom dependencies
- No custom-module dependency declared. External non-Community dependency: `l10n_th_reports` (source not present in Community tree).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: what `l10n_th_reports` provides (module not read; not in assigned scope or Community tree).
- UNKNOWN - EVIDENCE INSUFFICIENT: how the grouping-key change affects generated tax lines in Community 19.
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior of the payment wizard when several documents are paid together (compute uses single-record access on the wizard, wizard/account_payment_register.py:40-70).
- UNKNOWN - EVIDENCE INSUFFICIENT: legal correctness of tax-type labels and tag-name matching rules ("pnd3", "pnd53") against current Thai rules (models/account_move.py:70-82; models/tax_report_pnd.py:39-45).
