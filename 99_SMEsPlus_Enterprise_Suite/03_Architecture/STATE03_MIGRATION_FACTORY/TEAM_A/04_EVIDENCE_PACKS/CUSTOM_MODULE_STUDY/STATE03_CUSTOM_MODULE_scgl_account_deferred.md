> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_account_deferred

Module: scgl_account_deferred
License (confirmed in manifest): LGPL-3 (scgl_account_deferred/__manifest__.py:9)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (__manifest__.py:10)
Version (manifest): 19.0.1.0.0 (__manifest__.py:7)
Path: Extra_Module_scgl/scgl_account_deferred
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Deferred revenue / prepaid expense: the user enters a start and end date on an invoice/bill line; after posting, the module moves the whole line amount from the P&L account to a balance-sheet holding account and then releases it back to P&L month by month (scgl_account_deferred/PROVENANCE.txt:11-13; models/deferred_schedule.py:3-6).
- Per-company settings: prepaid-expense account, unearned-revenue account, deferred journal, split method (by days or equal per month), generation mode (on post, or manual button) (models/res_company.py:9-26; views/res_config_settings_views.xml:10-36).
- Schedule tracking model with period lines, list/form views and pivot "reports" for revenue and expense (models/deferred_schedule.py:16-218; views/deferred_schedule_views.xml:105-152).
- Provenance note states clean-room rewrite, no OEEL-1 code read (PROVENANCE.txt:4-8). Self-declared, not verified.

## 2. Attachment to CORE
- core:account, account.move (models/account_move.py):
  - Added fields: link to a schedule, entry kind (deferral/recognition/reversal), schedule list, counters (lines 10-16). Added actions: open schedules, generate entries (lines 33-40).
  - Override `_post` : ADDS behavior AFTER core posting. For each just-posted move whose company mode is "on post" and which is not itself a module-generated entry, it creates schedules and journal entries for deferrable lines (lines 45-49). Core signature: core:account/models/account_move.py:5569. Side effect: posting an ordinary invoice/bill silently creates additional posted journal entries plus draft future entries. Marked `ALTERS CORE CONTROL` (posting side effects, numbering: consumes sequence numbers in the deferred journal).
  - Override `button_draft` : ADDS behavior BEFORE core. Deletes/reverses the schedule's entries first, then calls core (lines 51-53). Core: core:account/models/account_move.py:6269.
  - Override `button_cancel` : same pattern as button_draft (lines 55-57). Core: core:account/models/account_move.py:6384.
  - Marked `ALTERS CORE CONTROL` for both: reset-to-draft/cancel of a source document now also reverses posted accounting entries in the deferred journal.
- core:account, account.move.line: adds start date, end date, schedule link; constraint requires both dates or neither and end not before start (models/account_move_line.py:10-22). Deferrable = has both dates, product line, expense or income account group, non-zero balance (lines 34-37).
- core:account, res.company / res.config.settings: added fields only (models/res_company.py, models/res_config_settings.py:9-13).
- Views: invoice form gets a "Deferred" stat button, a "Generate Deferred Entries" button (group account.group_account_invoice) and optional date columns on invoice lines (views/account_move_views.xml:9-24).
- Posting side effects detail (models/deferred_schedule.py):
  - Step 1: one deferral entry dated the source accounting date, posted immediately (lines 135-144).
  - Step 2: one recognition entry per calendar month dated the period end; entries with period end on/before today are posted at once, later ones stay draft with auto-post at date (lines 148-163).
  - Amounts: company-currency balance only, absolute value; last period absorbs rounding (lines 110, 79-90). Foreign currency amounts are not carried on the entries (lines 139-140, 156-158).
  - Undo (lines 165-181): draft entries deleted (auto-post cleared first); posted entries reversed with cancel=True dated today; then the schedule and lines are deleted. Uses core `_reverse_moves` (core:account/models/account_move.py:5495).
- Tax closing / lock-date interaction:
  - The module never reads or writes any company lock date field (no reference in module files).
  - Core soft-post moves an entry's date forward to after the violated lock date when posting with hard post (core:account/models/account_move.py:5702-5706; action_post uses soft=False at :6198). Therefore a deferral or recognition entry whose intended date falls in a locked period is re-dated by core, not rejected; schedule period lines keep the original period end (models/deferred_schedule.py:163). Business effect: schedule dates and entry dates can diverge.
  - Deferred journal type must be "general" (models/res_company.py:19), so sale/purchase lock dates do not apply to these entries; fiscal-year and hard lock dates do (core:account/models/company.py:723-737). Tax lock date does not apply because the entry lines carry no tax (core:account/models/account_move_line.py:1522-1524).
  - Reset-to-draft of the source invoice runs the undo before core's own checks. If core then refuses (for example a lock violation, core:account/models/account_move.py:3953-3956), the outcome depends on the surrounding database transaction being rolled back. UNKNOWN - EVIDENCE INSUFFICIENT for runtime behavior.

## 3. New objects, security, automation, external calls
- New models: scgl.deferred.schedule, scgl.deferred.schedule.line (models/deferred_schedule.py:16,197).
- ACL: group account.group_account_invoice has full CRUD; account.group_account_readonly read-only (security/ir.model.access.csv:2-5). No record rules and no company check on the schedule models (no ir.rule found in module). Company field exists on schedule (models/deferred_schedule.py:21).
- Menus under core Accounting entries and Management reports, read-only group (views/menus.xml:4-9).
- Cron / server actions: none own. Relies on the core auto-post cron (core:account/data/service_cron.xml:3-9; core:account/models/account_move.py:6460). A fallback button "Post Due Entries" posts due recognition entries directly (models/deferred_schedule.py:183-188; views/deferred_schedule_views.xml:33).
- External calls: none found. Reporting viewer bridge is a separate module named in PROVENANCE.txt:13-14 (not studied here).

## 4. Odoo 19 compatibility (checked against Community 19 tree)
- Exist in core 19: account.move._post (:5569), button_draft (:6269), button_cancel (:6384), _reverse_moves(default_values_list, cancel) (:5495), is_invoice(include_receipts) (:6567), auto_post value at_date (:294-298), account.account.internal_group (core:account/models/account_account.py:76), account types used in domains (:49-55), move line balance (core:account/models/account_move_line.py:126), company_currency_id (:60), settings anchor app "account" (core:account/views/res_config_settings_views.xml:23), menus account.menu_finance_entries and account.account_reports_management_menu (core:account/views/account_menuitem.xml:24,40).
- No mismatches found in the fields, methods and view anchors checked. Report menu targets need `account_reports_management_menu`, which exists in Community.

## 5. Custom-to-custom dependencies
- Manifest: only core account (__manifest__.py:12). A companion viewer module (scgl_report_viewer_deferred) is referenced in comments only (views/deferred_schedule_views.xml:112; PROVENANCE.txt:13-14). Not a declared dependency.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: multi-company isolation of schedules (no record rule; only the company field).
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior for credit notes, foreign-currency lines and lines with partial payment (tests/test_deferred.py covers revenue, expense, reset and config errors only: lines 58, 91, 102, 122, 132).
- UNKNOWN - EVIDENCE INSUFFICIENT: what happens when a posted recognition entry is later reversed or deleted manually outside the source document (no guard found).
- UNKNOWN - EVIDENCE INSUFFICIENT: interaction with the journal hash / inalterability setting on the deferred journal.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether other installed modules also override `_post`, button_draft or button_cancel with conflicting ordering.
