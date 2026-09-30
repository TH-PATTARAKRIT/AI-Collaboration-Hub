> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Trace: scgl_advance_expense_request

Module: scgl_advance_expense_request
License (confirmed in manifest): LGPL-3 (scgl_advance_expense_request/__manifest__.py:6)
Author (manifest): SCGL (__manifest__.py:5)
Version (manifest): 19.0.1.0.0 (__manifest__.py:3)
Path: addons_Extramodule/addons/scgl_advance_expense_request
Source revision studied: workspace on-disk copy (not verified against upstream)
Note: file headers are mixed. Python init files state AGPL-3.0 (__init__.py:1; models/__init__.py:1) and product/sequence files cite ForgeFlow copyright with LGPL (models/product_template.py:1-2; data/advance_request_sequence.xml:2-3). Wording such as "purchase request" appears in code (models/advance_expense_request_line.py:136,140,159). Origin is not documented; see section 6.

## 1. Business capability
- Employee cash-advance workflow: an employee raises a request with lines (product flagged as advance, quantity, requested amount); states Draft, To be approved, Approved, Rejected, Done (models/advance_expense_request.py:6-12, 219-238).
- The approver is the "Advance Expense Approver" set on the requester's employee record (models/hr_employee.py:7; models/advance_expense_request.py:52-65). Only that user can approve (lines 223-226).
- A manager then creates a vendor bill payable to the requester and posts it (lines 240-274). After the advance is paid, the employee clears it with a payment-method entry (wizard/advance_request_reconcile.py:52-92) or offsets it against another vendor bill (same file, lines 6-49; models/account_move.py:45-114).
- Computed amounts: amount due, amount to clear, bill status, cleared flag (models/advance_expense_request.py:116-150, 313-334).
- Sequence prefix "AE", 5 digits (data/advance_request_sequence.xml:5-10).

## 2. Attachment to CORE
- core:hr, hr.employee: added approver field and form placement after work location (models/hr_employee.py:7; views/hr_employee_view.xml:7-11).
- core:product, product.template: added checkbox "advance_expense_ok" (models/product_template.py:10-12; the label keyword is capitalised `String`, so the label likely is not applied); form placement in options block (views/product_template_view.xml:7-14).
- core:account, account.move: added fields (advance link, reconcile-advances link, can-reconcile flag) and new methods `can_advance_reconcile_compute`, `action_reconcile_advance`, `_prepare_own_account_transfer_move_vals` (models/account_move.py:10-114). No core method overridden. This method name was not found in core account or hr_expense.
- core:account, account.move.line: added links to the advance and advance line (models/account_move.py:121-122).
- Views: account.view_move_form gets hidden fields and a "Reconcile to Advance" button (views/account_move_views.xml:5-19).
- Overrides of core methods by name: none. Behaviors that touch core controls (all done by calling or writing core objects):
  - Bill creation and posting: `button_post_bill` creates an in_invoice for the requester's partner with no taxes, dated today, then calls core action_post immediately (models/advance_expense_request.py:249-273). Posting date follows core lock-date handling (core:account/models/account_move.py:5702-5706). The method has no state or group check in Python; only the form view hides the button (views/advance_expense_request_view.xml:9-15). `ALTERS CORE CONTROL` (creates and posts accounting documents outside the normal bill entry path, approval enforced only in UI).
  - Bill cancellation by direct write: reset (models/advance_expense_request.py:215-216) and the reject wizard (wizard/advance_request_rejected.py:14-15) write state "cancel" on the related bills directly. Core button_cancel additionally cancels payments, removes reconciliations and clears auto-post (core:account/models/account_move.py:6384-6396); this path skips those steps. Core write-level lock checks on a posted-to-not-posted change still apply (core:account/models/account_move.py:3953-3956). `ALTERS CORE CONTROL` (bypasses the cancel/reset-to-draft workflow and leaves paid bills with reconciliations in place; runtime outcome UNKNOWN).
  - Advance offset: `apply` builds a journal entry in the first general journal of the bill's company, credit on the advance account of the first request line and debit on the bill's payable account, posts it, then assigns it to the bill via core js_assign_outstanding_line (wizard/advance_request_reconcile.py:35-49; models/account_move.py:62-114; core:account/models/account_move.py:6239). Posting side effect on a vendor bill. Journal choice is arbitrary (TODO comment at models/account_move.py:61).
  - Clearing: `apply_payment` posts an entry: debit the chosen journal's default account, credit the first line's account, amount typed by the user with no validation against the amount to clear (wizard/advance_request_reconcile.py:62-92; view field at wizard/advance_request_reconcile_view.xml:27).
- Accounting model as coded: the advance bill is coded to the request line account, whose default is the product's expense account (models/advance_expense_request_line.py:130); demo account 555555 is typed "expense" (demo/advance_request_demo.xml:6). So the advance is booked to a P&L type account until cleared. This is what the code does; whether it is intended is not stated.

## 3. New objects, security, automation, external calls
- New models: advance.expense.request, advance.expense.request.line (mail thread and activity), transient wizards advance.request.reconcile, advance.expense.clear.wizard, advance.request.rejected.
- Groups: Advance Expense Request User (implies base.group_user) and Manager (implies User) (security/advance_request_security.xml:8-20). Category link commented out (lines 11,19).
- ACL: request and line models to the User group full CRUD; the three wizards have an empty group, i.e. every user (security/ir.model.access.csv:2-6).
- Record rules: User sees and edits only own requests; followers may read; Manager rule has no domain, so it is unrestricted (security/advance_request_security.xml:39-71 and 72-104). Two "multi-company" rules are declared with a company domain but assigned to group base.group_user (lines 21-38); an ir.rule with groups is not global by core definition (core:base/models/ir_rule.py:54-56) and group rules are OR-ed (core:base/models/ir_rule.py:84-85). Effect on company isolation for Managers: UNKNOWN - EVIDENCE INSUFFICIENT.
- Menu: own top-level app for the two groups (views/advance_expense_request_view.xml:361-386).
- Crons / server actions: none. External calls: none.
- Files present but not loaded: mail subtypes file data/advance_request_data.xml is missing from manifest data (__manifest__.py:8-20). Conversely, demo/advance_request_demo.xml (a GL account and a product) is listed under data, so it is installed on every install (line 19).
- Debug traces left in code: print statements (wizard/advance_request_reconcile.py:16-18) and info-level log lines (models/account_move.py:20-27).

## 4. Odoo 19 compatibility (checked against Community 19 tree)
- Mismatch: depends on `account_asset` (__manifest__.py:7); no such module in the Community tree. Demo data sets `create_asset` on account.account (demo/advance_request_demo.xml:9); no `create_asset` found in core account, hr_expense or purchase. Install on Community only would fail unless an external module supplies both.
- Present in core 19: hr_expense, purchase, product.can_be_expensed (core:hr_expense/models/product_template.py:18), property_account_expense_id (core:account/models/product.py:57), js_assign_outstanding_line (:6239), move-line product_uom_id (core:account/models/account_move_line.py:376), price_total (:409), journal default_account_id (core:account/models/account_journal.py:126), uom.group_uom (core:uom/security/uom_security.xml:4), hr.view_employee_form target field work_location_id (core:hr/views/hr_employee_views.xml:479), product options block (core:product/views/product_views.xml:43), invoice lines group class (core:account/views/account_move_views.xml:1352).
- Style difference: request create is declared for a single dict (models/advance_expense_request.py:184-185) whereas core hr_expense uses the multi-record form (core:hr_expense/models/hr_expense.py:837-838). Effect on Odoo 19: `not checked`.
- State value "clear" is used in checks and view but not in the state list (models/advance_expense_request.py:204; views/advance_expense_request_view.xml:25,55).

## 5. Custom-to-custom dependencies
- None declared. Dependency `account_asset` is not a Community module; whether it is the OCA asset module, an Enterprise module or a custom one: UNKNOWN - EVIDENCE INSUFFICIENT.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: origin and provenance of the code (mixed AGPL/LGPL headers, ForgeFlow-credited files, no provenance note).
- UNKNOWN - EVIDENCE INSUFFICIENT: tax treatment of the advance bill (taxes are forced empty, line 256) and of clearing.
- UNKNOWN - EVIDENCE INSUFFICIENT: runtime effect of direct state write on paid or reconciled bills.
- UNKNOWN - EVIDENCE INSUFFICIENT: whether the related approver field behaves as intended for users with several employee records (models/advance_expense_request.py:64).
- UNKNOWN - EVIDENCE INSUFFICIENT: no tests folder in the module.
