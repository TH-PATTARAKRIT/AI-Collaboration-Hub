> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: smesplus_advance_expense_request

Module: smesplus_advance_expense_request ("Employee Advance Expense Request")
License (confirmed in manifest): LGPL-3 (source headers also state AGPL-3.0 at smesplus_advance_expense_request/__init__.py:1 and models/__init__.py:1, and a ForgeFlow LGPL-3 notice at models/product_template.py:1-2 and data/advance_request_sequence.xml:2-3; manifest is taken as the operative license)
Author (manifest): SMEsPlus
Version (manifest): 19.0.1.0.0
Path: addons_Extramodule/addons_extra/smesplus_advance_expense_request
Source revision studied: workspace on-disk copy (not verified against upstream)
Classification (batch_07 list): Company Extra/Custom. Note: manifest depends on hr_expense, purchase and account_asset (__manifest__.py:1-23); the batch file did not list account_asset.

## 1. Business capability
- Employee cash-advance workflow: an employee requests money in advance, a designated approver approves, accounting creates a vendor bill to the employee, the bill is paid, and the advance is later cleared (against expenses or a refund) (models/advance_expense_request.py:6-12, 283-374; views/advance_expense_request_view.xml:9-50).
- States: draft, to be approved, approved, rejected, done (models/advance_expense_request.py:6-12). A bill-status and clear-status are derived from the bills (:118-137, 158-232).
- Approver per employee: each employee record gets an "Advance Expense Approver" user (models/hr_employee.py:7; views/hr_employee_view.xml:9-11). The request takes its approver from the requester's employee record (models/advance_expense_request.py:60-66).
- Products flagged "advance request" pick the eligible item on request lines (models/product_template.py:10-12; models/advance_expense_request_line.py:19-20, 92-98).
- Two wizards: reject with a reason (wizard/advance_request_rejected.py:5-16) and reconcile/clear (wizard/advance_request_reconcile.py:5-90).
- Vendor bill offset: on a vendor bill a "Reconcile to Advance" button lets the user offset the bill against advances of the same user that are paid but not yet cleared (models/account_move.py:20-52; views/account_move_views.xml:11-19).

## 2. Attachment to CORE
- Core modules: hr_expense (product fields, e.g. can_be_expensed used in demo, demo/advance_request_demo.xml:17), hr (employee form, views/hr_employee_view.xml:7), purchase (declared, use not found), account (bills, entries), product, mail (chatter mixins, models/advance_expense_request.py:18). Non-Community: account_asset (Enterprise; used by demo field create_asset, demo/advance_request_demo.xml:9).
- account.move: new fields advance_expense_id, advance_ids_reconcile, can_advance_reconcile (models/account_move.py:9-18); new methods only, no core method overridden. account.move.line: fields advance_id_reconcile, advance_expense_line_id (models/account_move.py:110-115).
- hr.employee: field ae_approver. product.template: field advance_expense_ok (see 1).
- Postings created (ordinary ORM, posted with the core post action):
  - Create Bill: vendor bill to the requester's partner, no taxes, dated today, posted immediately, request set to done (models/advance_expense_request.py:312-357). Core posting checks (lock dates, numbering) therefore apply as normal (core:account/models/account_move.py:6180).
  - Clear: manual entry debiting the chosen payment journal's default account and crediting the advance account, posted immediately (wizard/advance_request_reconcile.py:60-90).
  - Offset: entry from the advance account to the bill's payable account, posted, then reconciled through the core outstanding-line assign (models/account_move.py:54-104; wizard/advance_request_reconcile.py:33-47; core:account/models/account_move.py:6239).
- ALTERS CORE CONTROL: Reset (button_draft) and Reject write the cancel state directly on all related vendor bills (models/advance_expense_request.py:283-291; wizard/advance_request_rejected.py:14-15) instead of calling the core cancel action (core:account/models/account_move.py:6384-6396), which first resets to draft, removes reconciliations and cancels linked payments. Core write still applies lock-date checks when a posted move changes state (core:account/models/account_move.py:3948-3951), but the unreconcile / payment-cancel steps are skipped; consequences for paid bills were not observed.
- Approval control (new, module-local, not core): only the designated approver can approve (models/advance_expense_request.py:297-300); the approve, reject, reset and create-bill buttons additionally require the module's Manager group (views/advance_expense_request_view.xml:9-15, 23-50).

## 3. New objects, security, automation, external calls
- New models: advance.expense.request and advance.expense.request.line (chatter/activity enabled) (models/advance_expense_request.py:15-18; models/advance_expense_request_line.py:12-17); transient wizards advance.request.rejected, advance.request.reconcile, advance.expense.clear.wizard.
- Sequence "AE" 5 digits (data/advance_request_sequence.xml:5-10). Menus under own app root (views/advance_expense_request_view.xml:361-384).
- Groups: Advance Expense Request User (implies internal user) and Manager (implies User) (security/advance_request_security.xml:8-20).
- ACLs: request and line - User group full rights; the three wizards - no group, so all users (security/ir.model.access.csv:2-6).
- Record rules: user sees/changes own requests (requested_by = current user), followers can read, managers unrestricted (no domain) (security/advance_request_security.xml:39-104). Two "multi-company" rules are declared with both a group and the global flag (:21-38); in core the global flag is derived from groups, so with a group set the rule is a group rule (core:base/models/ir_rule.py:53-56), and group rules are OR-ed with the per-user rules. Inference: company scoping may not act as a global restriction and may widen what internal users can read within their allowed companies. Not run.
- Automation: none (no cron, no server action); external calls: none.
- Data not loaded: mail subtypes file exists (data/advance_request_data.xml:4-27) but is not in the manifest data list; demo file IS in the data list, so demo account code 555555 and product are created on every install (__manifest__.py:8-18; demo/advance_request_demo.xml:3-23, noupdate).

## 4. Odoo 19 compatibility
- Checked and present: js_assign_outstanding_line (core:account/models/account_move.py:6239); work_location_id anchor (core:hr/views/hr_employee_views.xml:169); options container in product form (core:product/views/product_views.xml:43); account.move ref field in move form (core:account/views/account_move_views.xml:1038).
- Mismatches / risks: create override takes a single values dictionary with the single-record decorator (models/advance_expense_request.py:249-257) while core create is multi-record (core:odoo/orm/models.py:4616-4617); list input breaks it. Field parameter written "String" (capital) (models/product_template.py:11) is logged as unknown parameter (core:odoo/orm/fields.py:529-535). Old-style group-count read (models/advance_expense_request.py:223; core:odoo/orm/models.py:2755, still present). Delete guard tests a "clear" state that is not in the state list (:269; :6-12). demo/data references account_asset field create_asset (Enterprise) - not verifiable here. Three transient models declare no description.

## 5. Custom-to-custom dependencies
- None declared among SMEsPlus modules. Depends on Enterprise-only account_asset.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- UNKNOWN - EVIDENCE INSUFFICIENT: whether ForgeFlow/OCA purchase-request code was reused (copyright notices exist; derivation not established).
- UNKNOWN - EVIDENCE INSUFFICIENT: the effect of the group-plus-global record rules on cross-user visibility (inferred from core, no runtime).
- UNKNOWN - EVIDENCE INSUFFICIENT: what account_asset contributes beyond the demo field; whether the module installs without it.
- UNKNOWN - EVIDENCE INSUFFICIENT: how the "clear" step handles partial repayments and foreign currency.
