> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE — account_asset_management

Module: account_asset_management
License (confirmed in manifest): AGPL-3 (account_asset_management/__manifest__.py:9)
Author (manifest): Noviat, Odoo Community Association (OCA) (manifest:14)
Version (manifest): 19.0.1.0.3 (manifest:8); development_status "Mature" (manifest:12)
Path: Extra_Module_scgl/_REQUIRED_OCA_DEPENDS/account_asset_management
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Fixed-asset register: asset profiles (accounts, journal, depreciation method/period/time, prorata, salvage), assets, asset groups, and a depreciation board of scheduled lines. (account_asset_management/models/account_asset_profile.py:9-170; models/account_asset.py:26; models/account_asset_line.py:10)
- Assets are created automatically when a posted vendor bill/journal line carries an asset profile; the line label is required. (models/account_move.py:99-135)
- Scheduled depreciation lines are turned into posted journal entries (depreciation vs expense accounts) on demand via "Compute Assets" wizard up to a chosen date; errors are logged per asset. (models/account_asset.py:1182-1237; models/account_asset_line.py:265-294; wizard/account_asset_compute.py:23-51)
- Asset removal wizard: early removal/sale with gain-loss or residual-value posting regime, chosen by company country. (wizard/account_asset_remove.py:137-231)
- Entry reversal wizard for a posted depreciation entry. (wizard/wiz_asset_move_reverse.py)
- Splits a multi-quantity line into one line per unit when the profile asks for it. (models/account_move.py:268-276)
- Excel asset report wizard (report/account_asset_report_xls.py; wizard/wiz_account_asset_report.py).

## 2. Attachment to CORE
- Depends on core `account`; also `report_xlsx_helper` (non-core) and Python `dateutil`; `excludes` the Enterprise `account_asset` module (manifest:10-13).
- `account.account` (core:account/models/account_account.py): adds default asset profile with a constraint that the profile's asset account equals this account (models/account_account.py:11-30).
- `account.move.line`: adds asset profile (computed from account) and asset link (models/account_move.py:184-205). Override `create` and `write` (models/account_move.py:215-266; core:account/models/account_move_line.py): ALTERS CORE CONTROL — BLOCKS linking an asset to non-sales entries unless created by the asset engine, and BLOCKS edits of amount, account, journal, date on any item linked to an asset (non-sales documents). Also ADDS splitting of quantity lines after core.
- `account.move`: overrides `write` (models/account_move.py:72-86): ALTERS CORE CONTROL — BLOCKS changing journal or date on an entry linked to a depreciation line. Override `unlink` and an `ondelete` guard (lines 41-70; core:account/models/account_move.py:4079): BLOCKS deleting entries linked to assets (unless deleted from the asset), and detaches the asset line when it is allowed. Override `action_post` (line 99; core:...:6180): ADDS behavior after core — creates assets for profile lines and posts a chatter note. Override `button_draft` (line 137; core:...:6269): ALTERS — for purchase documents it DELETES the linked assets before resetting to draft.
- Override `_reverse_move_vals` (models/account_move.py:143): core 19 has no such method (grep of core:addons: none); the override cannot be reached by core reversal flow, so the "delete asset when reversing its creation entry" behavior appears inactive — inferred, not run.
- Depreciation entry creation (models/account_asset_line.py:265-294): creates and posts journal entries programmatically via core create/action_post; core lock-date checks on posting still apply (nothing found that bypasses them). The module reads the company fiscal-year lock date to mark board lines as "initial balance" entries not to be posted (models/account_asset.py:579-614, 1032-1092; core:account/models/company.py:76).
- ALTERS CORE CONTROL (numbering/audit trail): "Delete entry" on a depreciation line resets the entry to draft and force-deletes it with the core's `force_delete` context when the profile does not allow reversal (models/account_asset_line.py:314-340 (force delete at 335-336)). In core, that context skips the sequence-gap guard and the restrictive audit-trail guard (core:account/models/account_move.py:4054-4076) and the posted-line delete guard (core:account/models/account_move_line.py:1962).
- Uses `company.compute_fiscalyear_dates` and reads an optional `record` key (models/account_asset.py:1125-1132; core:account/models/company.py:1115): works with core and with the custom `account_fiscal_year` override.
- Views inherit core account, move, move-line forms/lists and search (views/account_account.xml:6,16; views/account_move.xml:6; views/account_move_line.xml:6,20). Menus not inspected.

## 3. New objects, security, automation
- New models: account.asset, .asset.line, .asset.profile, .asset.group, .asset.recompute.trigger; wizards for compute, remove, report, reverse (security/ir.model.access.csv:2-19).
- ACLs: billing group (account_invoice) has full rights on assets and asset lines; profiles read for invoice/user, full for managers; wizards to account users/read-only (csv:2-19).
- Record rules: global multi-company rules for profile, asset, group using allowed companies (security/account_asset_security.xml:3-20).
- Automation: cron "Asset Management: Generate assets", daily, shipped inactive (data/cron.xml:3-12). Runs the compute wizard as root user when enabled.
- Many lookups on `account.asset.line` use elevated rights inside move overrides (models/account_move.py:46,63,76), so guards work for users lacking asset access.
- No external calls.

## 4. Odoo 19 compatibility
- MISMATCH: `_reverse_move_vals` (models/account_move.py:143) not present in core 19 (see section 2).
- `with_context(check_move_validity=False)` used (models/account_move.py:271; models/account_asset_line.py:268): flag still referenced in core:account/models/account_move.py:2786 in a different form; effect unknown.
- Present in core: `force_delete` context (core:account/models/account_move.py:4026-4070), `is_sale_document/is_purchase_document` (core:...:6580,6587), `tax_line_id` (core:account/models/account_move_line.py:212), `analytic.mixin`, view refs `account.view_move_line_form`, `view_account_form`, `view_account_list` (core:account/views/*).
- Not checked: `report_xlsx_helper` API compatibility; XML view xpaths.

## 5. Custom-to-custom dependencies
- Declared: `report_xlsx_helper` (not in Community tree; not in this batch).
- Implicit soft link to `account_fiscal_year` (company fiscal-year `record` key, models/account_asset.py:1127-1131).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: accounting correctness of depreciation amounts and the removal postings by country (runtime not observed; 1300-line engine only partially read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the `_reverse_move_vals` logic is replaced elsewhere.
- UNKNOWN — EVIDENCE INSUFFICIENT: effect of unsupported `check_move_validity` flag under core 19.
- UNKNOWN — EVIDENCE INSUFFICIENT: XLSX report contents and menu structure (files not read).
