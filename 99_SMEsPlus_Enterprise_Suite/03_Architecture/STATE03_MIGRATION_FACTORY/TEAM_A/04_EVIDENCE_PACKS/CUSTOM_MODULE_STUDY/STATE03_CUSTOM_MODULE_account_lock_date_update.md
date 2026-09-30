> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE — account_lock_date_update

Module: account_lock_date_update
License (confirmed in manifest): AGPL-3 (account_lock_date_update/__manifest__.py:10)
Author (manifest): ACSONE SA/NV, Odoo Community Association (OCA) (manifest:11)
Version (manifest): 19.0.1.0.0 (manifest:9)
Path: Extra_Module_scgl/_REQUIRED_OCA_DEPENDS/account_lock_date_update
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Gives an accounting adviser a dedicated "Lock Dates" dialog (menu under Accounting) to view and change the company's period lock dates without needing full technical/settings access. (account_lock_date_update/wizards/account_update_lock_date.xml:43-53; manifest summary at __manifest__.py:6-9)
- Dialog shows the four reversible locks (sales, purchase, tax return, global) and the irreversible hard lock. (account_lock_date_update/wizards/account_update_lock_date.xml:13-28)
- Rejects any lock date that is in the future. (account_lock_date_update/wizards/account_update_lock_date.py:71-80)

## 2. Attachment to CORE
- Depends on core `account` only (manifest:14).
- Reads/writes core `res.company` lock-date fields defined in core:account/models/company.py:76-102 (list of fields: core:account/models/company.py:57-67, imported at account_lock_date_update/wizards/account_update_lock_date.py:8).
- ALTERS CORE CONTROL (lock dates / security): the confirm action writes the lock dates on the company using elevated (superuser-level) rights (account_lock_date_update/wizards/account_update_lock_date.py:82), so the person only needs the accounting-manager group (or admin) checked at py:49-53, rather than the rights normally required to edit the company record. Core validations on the lock-date write still run because the write goes through core `res.company` write (core:account/models/company.py:741-743 calls `_validate_locks`, defined at core:account/models/company.py:552-604: hard lock cannot be removed/decreased, draft entries and unreconciled bank lines block locking). The wizard does not itself relax these; whether the elevated write skips any core check: UNKNOWN — see section 6.
- Override of core method `_get_unreconciled_statement_lines_redirect_action` on res.company (account_lock_date_update/models/res_company.py:10; core:account/models/company.py:518): REPLACES core behavior. Core opens the bank-statement-line model; the override opens the underlying journal entries (list/form) instead, with a code comment giving a client-crash/usability reason for v19 (res_company.py:13-23). Business effect: when locking is blocked by unreconciled bank lines, the user lands on journal entries rather than statement lines. Not a control bypass (the block itself remains in core).
- Menu: adds "Lock Dates" under core menu `account.menu_finance_entries` (wizards/account_update_lock_date.xml:51; core:account/views/account_menuitem.xml:24).

## 3. New objects, security, automation
- New transient model `account.update.lock_date` (account_lock_date_update/wizards/account_update_lock_date.py:11-13).
- Defaults: form is pre-filled from the current company's lock dates (py:40-47).
- ACLs: accounting manager full; accounting read-only group read (account_lock_date_update/security/ir.model.access.csv:2-3). Update button restricted to accounting manager group (xml:36).
- No record rules, crons, server actions or external calls found. No audit trail in this module itself; core marks the company lock fields as tracked (core:account/models/company.py:78,84,90,95,100).

## 4. Odoo 19 compatibility
- Imports `LOCK_DATE_FIELDS` from account.models.company: exists (core:account/models/company.py:64).
- Refs used in redirect action: `account.view_account_move_filter` (core:account/views/account_move_views.xml:1625), `account.view_move_tree_multi_edit` (:499), `account.view_move_form` (:697): all exist.
- Group refs `account.group_account_manager`, `account.group_account_readonly` exist (core:account/security/account_security.xml:50 for readonly). Manager group presence: not separately pointer-checked.
- The module's own comment states the core redirect action lacks a "views" key in v19 (res_company.py:13-16); consistent with core:account/models/company.py:526-531 (no "views" key). No mismatches found.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the elevated-rights write skips any lock-exception handling or tracking user attribution in core (core write also touches `account.lock_exception`, core:account/models/company.py:764-770).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether other installed modules also expose a lock-date editor that conflicts with this dialog.
- UNKNOWN — EVIDENCE INSUFFICIENT: on-disk copy vs upstream OCA release.
