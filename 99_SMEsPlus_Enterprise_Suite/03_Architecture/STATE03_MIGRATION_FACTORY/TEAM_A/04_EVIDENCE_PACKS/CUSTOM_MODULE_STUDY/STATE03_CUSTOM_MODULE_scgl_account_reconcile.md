> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_account_reconcile

Module: scgl_account_reconcile
License (confirmed in manifest): LGPL-3 (scgl_account_reconcile/__manifest__.py:9)
Author (manifest): SCG Legacy (Thailand) Co., Ltd. (__manifest__.py:10)
Version (manifest): 19.0.1.0.0 (__manifest__.py:7)
Path: Extra_Module_scgl/scgl_account_reconcile
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- A "Reconcile" list under Review showing posted, not-yet-reconciled journal items of reconcilable accounts, grouped by account then partner, with residual totals (views/actions.xml:30-40, list at 4-29).
- Button "Reconcile": reconciles the selected items; needs at least two open items, all in one account (models/account_move_line.py:16-24).
- Button "Auto-reconcile": (1) pairs opposite items with exactly equal residual inside the same account, partner and currency, oldest first; (2) if the leftover items of a group net to zero, reconciles the whole group (models/account_move_line.py:26-56). With no selection it works on all open reconcilable items of the user's allowed companies (lines 28-31).
- Provenance: rewritten, states use of Community reconcile and no OEEL-1 code read (PROVENANCE.txt:2-5). Self-declared, not verified.

## 2. Attachment to CORE
- core:account, account.move.line: three added methods `_scgl_reconcilable`, `action_scgl_reconcile_selected`, `action_scgl_auto_reconcile`, plus a notification helper (models/account_move_line.py:12-59). Overrides of core methods by name: none.
- Calls core `reconcile()` (core:account/models/account_move_line.py:3142), so all core reconciliation rules apply, including any exchange-difference entries and lock-date protection of reconciliation. The module adds no lock, approval or ACL check of its own. Not `ALTERS CORE CONTROL`.
- Business risk noted from the code: auto-matching is by equal residual amount only, not by reference, invoice number or payment link (lines 39-50). It can pair unrelated documents of the same partner with the same amount. A failure inside the loop is not caught, so one failing pair aborts the whole run (no exception handling in lines 33-55).
- View: new list view on account.move.line (views/actions.xml:4); reuses core search view account.view_account_move_line_filter (core:account/views/account_move_views.xml:306) and its "group by account/partner" filters (core:account/views/account_move_views.xml:374-375).
- Menu: under core "Review" (views/actions.xml:39; core:account/views/account_menuitem.xml:31), visible to group account.group_account_invoice (line 40).

## 3. New objects, security, automation, external calls
- New models: none. ACLs: none added; access is that of core account.move.line. Record rules: none added; company scoping comes from core move-line rules plus the explicit filter on the user's allowed companies (models/account_move_line.py:30-31).
- Crons / server actions / external calls: none found. The buttons run as the current user, no elevated access found in module files.

## 4. Odoo 19 compatibility (checked against Community 19 tree)
- Fields used exist in core 19: amount_residual (core:account/models/account_move_line.py:246), reconciled (:258), matching_number (:304), parent_state (:69), company_currency_id (:60), reconcile on account (core:account/models/account_account.py:89).
- Search view id and filter names exist (see section 2). Menu parent account_audit_menu exists.
- No mismatches found.

## 5. Custom-to-custom dependencies
- None (depends only on account, __manifest__.py:12).

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: behavior for foreign-currency items where residual in company currency matches but currency amounts differ (grouping is by currency id, lines 34, 46).
- UNKNOWN - EVIDENCE INSUFFICIENT: performance on large ledgers when auto-reconcile runs with no selection (nested loops, lines 42-50).
- UNKNOWN - EVIDENCE INSUFFICIENT: interaction with a reconciliation lock date or exception when items lie in a locked period (module has no handling; outcome depends on core).
