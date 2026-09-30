> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 custom module trace: om_fiscal_year

Module: om_fiscal_year · License (confirmed in manifest): LGPL-3 (om_fiscal_year/__manifest__.py:12)
Author (manifest): Odoo Mates, Odoo SA (manifest:10) · Version (manifest): 1.0.2 (manifest:3; name string says "Odoo 19 Fiscal Year & Lock Date", manifest:2)
Path: addons_Extramodule/addons_extra/om_fiscal_year
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Fiscal-year records per company (name, start, end) with a no-overlap and end-after-start validation (om_fiscal_year/models/account_fiscal_year.py:5-48).
- Accounting Settings section for the fiscal year end (day/month) and an option to define fiscal years of more or less than a year, with a shortcut to the fiscal-year list (views/settings.xml:9-40; models/account_settings.py:28-30).
- A "Lock Dates" wizard letting an Accounting Manager set the hard, all-users, sales, purchase and tax lock dates of the current company (wizard/change_lock_date.py:5-64; menu wizard/change_lock_date.xml:42-47).
- An upgrade script (version 1.0.2) that repairs earlier mis-bound lock-date fields (migrations/1.0.2/post-migrate.py:1-78).

## 2. Attachment to CORE
- Depends on core `account` only (manifest:14).
- `res.company` (models/res_company.py:5-38): defines `_validate_fiscalyear_lock`, a check that draft entries or unreconciled bank statement lines do not exist up to the new fiscal-year lock date, raising a redirect warning or validation error. Nothing in this module calls it (grep of module Python: only the definition at res_company.py:8). Core 19 has no method of that name; its company `write` calls `_validate_locks` instead (core:account/models/company.py:741-742, 552-574). Effect in 19: the module's check is not invoked by core; the equivalent control in core stays in force. Marked here because it targets the lock-date control: ALTERS CORE CONTROL only if a caller is wired, which was not found: UNKNOWN - EVIDENCE INSUFFICIENT.
- `res.config.settings` (models/account_settings.py:4-30): re-exposes company fiscal-year end and five lock dates as settings fields writable from the settings page (related to company). Core res_config_settings.py in `account` declares none of these names (grep, no match).
- Wizard `change.lock.date` write path (wizard/change_lock_date.py:49-64): ALTERS CORE CONTROL (lock dates). It writes the five lock-date fields on `res.company` using elevated rights (sudo) after checking the caller is an Accounting Manager (or the superuser) and that the company is among the caller's companies (:51-55). The write still passes through core company `write` and therefore core `_validate_locks` (core:account/models/company.py:741-742), which per its own docstring refuses removal or reduction of a hard lock date (core:account/models/company.py:553-556, 569-574). The wizard does not set lock exceptions (core has an `account.lock_exception` model, core:account/models/company.py:622, 767; not used here).
- Migration (migrations/1.0.2/post-migrate.py:1-78): on upgrade, copies each company's hard lock date into the tax/sale/purchase lock-date fields when those are empty and logs suspicious companies. ALTERS CORE CONTROL data (lock dates) at upgrade time; it does not clear any hard lock.
- Core view replaced: setting block `fiscalyear` of `account.res_config_settings_view_form` (views/settings.xml:9; core block is invisible, core:account/views/res_config_settings_views.xml:348). Core menus used: `account.menu_finance_entries`, `account.account_account_menu`.
- No override of posting, valuation/cost, approvals or numbering. The module does not itself compute lock-date enforcement on entries; that remains core.

## 3. New objects, security, automation, external calls
- Model account.fiscal.year (persistent); transient change.lock.date.
- Group "Allow to define fiscal years of more or less than a year" auto-assigned to root and admin (security/security.xml:5-8; noupdate="0", so re-applied on upgrade).
- ACLs (security/ir.model.access.csv:2-4): Accountant read/write (no create/delete) on fiscal years; Manager full; lock-date wizard for Manager only.
- Record rule: global multi-company rule on fiscal years (security/security.xml:10-15).
- Menus: Fiscal Year (needs the module's group, views/fiscal_year.xml:48-53); Lock Dates (Manager, wizard/change_lock_date.xml:42-47).
- No crons, no server actions, no external calls. Upgrade script contains direct database statements (not reproduced here).

## 4. Odoo 19 compatibility (grep against Community 19)
- Found in core: lock-date fields on `res.company` (core:account/models/company.py:58-66, 76-97), `fiscalyear_last_day` / `fiscalyear_last_month` (:74-75), `_validate_locks` (:552), `is_reconciled` on bank statement lines (core:account/models/account_bank_statement_line.py:130), views `account.view_account_move_filter`, `account.view_move_tree`, `account.view_move_form` (core:account/views/account_move_views.xml).
- MISMATCH: `_validate_fiscalyear_lock` has no counterpart in core 19 (see section 2); the module override is orphaned.
- Possible overlap: core 19 already ships lock dates, per-user lock dates and lock exceptions (core:account/models/company.py:108-112, 622); this module's wizard and settings duplicate the write path rather than using exceptions. Core has no `account.fiscal.year` model (grep of core account Python: no match).
- Manifest `sequence` is a string (manifest:8): effect not checked.

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Whether core Community 19 exposes the lock dates in its own settings/wizard UI so that this module's settings and wizard create two parallel screens: UNKNOWN - EVIDENCE INSUFFICIENT (core UI files not fully read).
- Whether the fiscal-year records created here influence any core computation (core computes fiscal-year boundaries from company day/month fields; no reference to this model was found in core): UNKNOWN - EVIDENCE INSUFFICIENT.
- Data effect of the 1.0.2 migration on already-live companies: UNKNOWN - EVIDENCE INSUFFICIENT (depends on stored data).
