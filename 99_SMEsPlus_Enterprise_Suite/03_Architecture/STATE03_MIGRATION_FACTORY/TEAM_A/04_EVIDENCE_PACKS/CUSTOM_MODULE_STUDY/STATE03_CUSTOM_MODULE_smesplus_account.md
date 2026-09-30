> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_account

Module: smesplus_account ("SMEsPlus - Accounting")
License (confirmed in manifest): LGPL-3 (smesplus_account/__manifest__.py:8)
Author (manifest): SMEsPlus
Version (manifest): 17.0.1.0.0 (manifest still carries the 17.0 series; the workspace is the 19 build)
Path: addons_smeplus/smesplus_account
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_06): Company Extra/Custom. Declared as an application (__manifest__.py:34). Manifest depends: account, account_accountant, analytic, mail (:9-14).

## 0.1 State of the module on disk (important)
- The Python side has four model files: account_account.py (144 lines), account_move.py (391), account_move_line.py (250), account_journal.py (151).
- models/__init__.py imports six files, but account_tax.py and res_company.py do not exist on disk (models/__init__.py:5-6). The package would fail at import as it stands.
- __init__.py imports a wizard package (smesplus_account/__init__.py:2) but the wizard folder is empty (no __init__.py).
- Manifest lists 10 data files and 2 asset files (__manifest__.py:15-31): security/security.xml, security/ir.model.access.csv, data/account_data.xml, five view files, wizard view, report file, SCSS and JS. The folders security/, data/, views/, wizard/, report/, static/src/js and static/src/scss exist but are EMPTY. So the module has no menus, views, groups, access-control lines, record rules, reports or dashboard front-end on disk. Only the Python model layer is present.
- Consequence: what the module "adds" below is described from Python code; UI and security behavior cannot be derived.

## 1. Business capability (from Python code)
- Thai chart-of-accounts helpers: a 4-level account classification derived from code length (1 digit category, 3 group, 5 control, others sub-account), a Thai-standard flag, a code-must-be-numeric check for flagged accounts, a live balance readout (smesplus_account/models/account_account.py:8-88).
- Thai VAT and withholding indicators on entries: VAT-7% flag and amount, withholding amount, net after withholding, Thai document-type label (models/account_move.py:14-43, 90-127).
- Posting stamp: who posted and when (models/account_move.py:45-57, 138-152).
- Deferred (prepaid expense / unearned revenue) recognition, "mirroring Enterprise logic": lines carry start and end dates; on posting the module generates monthly recognition entries and a full-deferral entry (models/account_move.py:63-84, 158-297; models/account_move_line.py:8-23).
- Dashboard and fast-read services: per-journal dashboard figures (draft, overdue, to-pay, bank balance, 30-day count), chart-of-accounts with balances, aged receivable/payable buckets, trial balance, unreconciled-lines batch, a bulk create-and-post helper, and a debit=credit checker (models/account_journal.py:27-151; models/account_account.py:112-144; models/account_move_line.py:85-247; models/account_move.py:303-377). No caller for these helpers exists in the module (front-end files absent).
- Journal dashboard settings: colour, sequence, show/hide flag (models/account_journal.py:8-20).

## 2. Attachment to CORE
- account.account (core:account/models/account_account.py): new fields smesp_account_level (stored, from code), smesp_balance_cache, company_currency_id (related to company; note the relation is to a single company field, but core 19 accounts are multi-company via company_ids, core:account/models/account_account.py:97), smesp_is_thai_standard (models/account_account.py:9-35). Constraint on code format for flagged accounts (:79-88). New action helpers (:90-110). No core method overridden.
- account.move (core:account/models/account_move.py): new fields (smesp_*), deferred relations via an own relation table (models/account_move.py:64-84). Override of _post (core:account/models/account_move.py:5569):
  - models/account_move.py:138-152. ADDS behavior after core: calls core posting first, then stamps the poster (first time only) and, for each posted move having deferral dates, generates deferral entries.
  - ALTERS CORE CONTROL (posting): the generation step raises an error when the company lacks a deferred journal or deferred account (:194-197), which aborts the whole posting transaction. So a user posting a document with deferral dates is BLOCKED unless those company settings exist. The settings are fields of res.company that are not defined in Community account (core:account only references them in l10n templates, e.g. core:l10n_nl/models/template_nl.py); they belong to Enterprise account_accountant (assumed).
  - Generated entries are created with auto-post at date (:219) and posted in one batch with the soft-post mode (:274): entries dated in the future stay unposted until their date. Zero-amount entries are deleted (:268-273). Rounding: last period takes the remainder (:231-235).
  - The full-deferral entry carries the source document date (:220); period entries are dated at each period end (:236). They pass through core posting checks (lock dates: core:account/models/account_move.py:2823) as ordinary ORM calls; no bypass code found.
  - Note: the code creates the deferral lines in a separate step after creating the headers (:252-265); core's balance and dynamic-line synchronization (core:account/models/account_move_line.py:1781-1800) applies as usual; not tested.
- account.move.line: new stored dates for deferral (index), WHT flag, Thai account-type label (models/account_move_line.py:9-37, 43-79). Depends on account.tax field smesp_is_wht (models/account_move_line.py:49-54; models/account_move.py:122) which would be defined in the missing account_tax.py - currently undefined on disk.
- account.journal: three dashboard fields, dashboard data method, and action_open_reconcile marked "Override" in its own docstring (models/account_journal.py:129-142). Core 19 Community has no action_open_reconcile on journal or account (searched core:account/models); the target is presumably the Enterprise one. Whether it REPLACES an Enterprise method: UNKNOWN (see 6).
- Numbering, valuation/cost, approvals, multi-company rules, lock dates: no override found in the present files.

## 2.1 What the module assumes from the Enterprise accounting module (account_accountant; not in Community tree)
- An Enterprise window action for posted unreconciled journal items, referenced by external id (models/account_account.py:92-94; models/account_journal.py:140-142).
- The bank-reconciliation widget entry point on bank statement lines, called for bank/cash/credit journals (models/account_journal.py:132-139); not found in Community account.
- Company-level deferred settings: deferred expense journal and account, deferred revenue journal and account (models/account_move.py:186-197).
- The deferral concept and field naming: comments state the deferred date fields mirror account_accountant (models/account_move_line.py:8) and the logic mirrors Enterprise (models/account_move.py:63). Own field names carry the smesp_ prefix, so no direct field collision by design; if Enterprise deferral is also active, double recognition is possible (UNKNOWN).
- Enterprise dependency is hard: manifest lists account_accountant (:11).

## 3. New objects, security, automation, external calls
- New models: none (extensions only); one new many2many relation table for deferrals (models/account_move.py:64-79).
- Security: none present on disk (security folder empty; groups, ACL, rules absent). Company scoping in the code: raw queries filter to the user's allowed companies or a given company (models/account_account.py:69, 130; models/account_journal.py:82-84), but the account-level helpers accept a company id argument without checking user access (models/account_account.py:112-115; models/account_move_line.py:86-92, 138, 193). Raw queries bypass ORM access rules.
- One query builder interpolates filter values into text (journal ids, date bounds) rather than binding parameters (models/account_move.py:316-324) - an injection-risk pattern if reachable from an RPC.
- Public RPC-style endpoints: get_smesp_journal_dashboard_datas (models/account_journal.py:107-127) and model-level helpers named for the dashboard; access depends on ACL that does not exist on disk.
- Cron: none. Server actions: none. External calls: none. Assets: manifest references a JS dashboard and SCSS that are not present.

## 4. Odoo 19 compatibility
- Checked and present in Community 19: execute_query (core:odoo/orm/environments.py:527); account.account company_ids (core:account/models/account_account.py:97) and active (:42); journal type "credit" (core:account/models/account_journal.py:111); account types used in the label map (core:account/models/account_account.py:48-64); _post signature (core:account/models/account_move.py:5569); internal_group (:76).
- Not found in Community 19: res.company deferred_* fields; action_open_reconcile; bank reconciliation widget entry; account.tax.smesp_is_wht (own file missing); files listed in manifest (see 0.1).
- Version series in manifest 17.0 vs 19 build; the naming "mirrors Enterprise" implies a copy from Odoo 17 era.
- account_move_line.py imports defaultdict at file end (line 250) after first use in functions - works at runtime as module level executes before calls; style defect.
- Not run; no test evidence.

## 5. Custom-to-custom dependencies
- None declared. Nothing else in the assigned batches depends on it (searched manifests of addons_extra and Extra_Module_scgl for a dependency on this name; none found).
- Implied sibling (not present): a custom account.tax extension defining the WHT flag.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the empty folders were stripped intentionally (e.g. withheld or lost in copying) or the module is a skeleton; the original manifest content cannot be met by the on-disk tree.
- UNKNOWN - EVIDENCE INSUFFICIENT: which Enterprise methods action_open_reconcile is meant to override, and their behavior.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the deferral generator conflicts with Enterprise deferral if both are installed.
- UNKNOWN - EVIDENCE INSUFFICIENT: the definition of the WHT flag on taxes and how withholding is intended to be configured (missing model file).
- UNKNOWN - EVIDENCE INSUFFICIENT: any Thai statutory report or PND/VAT form logic (none present).
- UNKNOWN - EVIDENCE INSUFFICIENT: who calls the dashboard/trial-balance/aged helpers (front-end asset absent).
