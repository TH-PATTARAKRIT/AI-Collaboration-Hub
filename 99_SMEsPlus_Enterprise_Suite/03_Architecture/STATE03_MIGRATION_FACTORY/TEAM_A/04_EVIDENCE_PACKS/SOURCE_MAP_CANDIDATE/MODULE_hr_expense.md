# Source Map (candidate) — `hr_expense`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_expense` |
| Display name | Expenses |
| Manifest version | 2.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `dce1efe9382aa356` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_expense/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `account`, `web_tour`, `hr`
- Direct dependents in 300-module list (2): `project_hr_expense`, `sale_expense`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `l10n_din5008_expense`
- Custom / third-party modules that declare a dependency (name — license only) (2): `scgl_advance_expense_request` — LGPL-3, `smesplus_advance_expense_request` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Expenses / Submit, validate and reinvoice employee expenses
- Inventory of user-facing artifacts (counts): menu items 11, views 32, window actions 11, server actions 0, reports 2, mail templates 0, scheduled jobs 1, wizards 7, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (6): `hr.expense.refuse.wizard` (Expense Refuse Reason Wizard); `hr.expense.approve.duplicate` (Expense Approve Duplicate); `hr.expense.split.wizard` (Expense Split Wizard); `hr.expense.split` (Expense Split); `hr.expense.post.wizard` (Expense Posting Wizard); `hr.expense` (Expense)
- Objects extended from other modules (19): `account.payment.register`, `analytic.mixin`, `account.tax`, `account.move`, `ir.actions.report`, `mail.thread.main.attachment`, `mail.activity.mixin`, `hr.employee.public`, `ir.attachment`, `account.move.line`, `hr.department`, `product.template`, `product.product`, `account.payment`, `res.company`, `hr.employee`, `res.config.settings`, `account.analytic.applicability`, `account.analytic.account`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 2 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.expense.split` ← Community: `sale_expense`; open-license custom/third-party scanned: —
- `hr.expense` ← Community: `project_hr_expense`, `project_sale_expense`, `sale_expense`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `account.payment.register`, `analytic.mixin`, `account.tax`, `account.move`, `ir.actions.report`, `mail.thread.main.attachment`, `mail.activity.mixin`, `hr.employee.public`, `ir.attachment`, `account.move.line`, `hr.department`, `product.template`, `product.product`, `account.payment`, `res.company`, `hr.employee`, `res.config.settings`, `account.analytic.applicability`, `account.analytic.account`

## 6. Actions / states / validation / automation / security
- State fields found: `hr.expense` → ['draft', 'submitted', 'approved', 'posted', 'in_payment', 'paid', 'refused']
- Validation: 4 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: HR Expense: Send Submitted Expenses Mail every 1 weeks
- Security: groups declared 4 (`group_hr_expense_team_approver`, `group_hr_expense_user`, `group_hr_expense_manager`, `base.default_user_group`); record rules 12 (of which company-scoped by text 1); access rows 14

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 75 of 76 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_expense (Expenses)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton: sourcemap/hr_expense.json. Pointers `module/path:LINE`; (TEST) = test-derived.
Key structural finding: in this revision each expense is its own approval unit. There is no expense-report / sheet container; a leftover integer field "former report" only preserves old grouping data (hr_expense/models/hr_expense.py:282-283). Reports, if re-introduced, are UNKNOWN — EVIDENCE INSUFFICIENT.

## A. Capabilities / functions
- Application "Expenses": employees record expenses (with receipts), approvers approve/refuse, accountants post them to the books, and employees are reimbursed (or the expense is logged as already paid by the company) (hr_expense/__manifest__.py skeleton summary "Submit, validate and reinvoice employee expenses"; hr_expense/models/hr_expense.py:24-45,1127-1216).
- Depends on account, web_tour, hr (skeleton depends); application=true, no auto_install. Core: expense record, approval, posting, reimbursement, categories (products flagged "can be expensed"), split, duplicate warning, attachments, dashboard.
- Optional / conditional: create expenses by emailing an alias (setting "Let your employees record expenses by email", alias default name "expense", accepted senders: employees only) (hr_expense/models/res_config_settings.py:17-18,31-60; hr_expense/data/mail_alias_data.xml:5-9); OCR, Stripe cards and reimbursement-in-payslip are placeholders for modules not present in this tree: hr_expense_extract, hr_expense_stripe, hr_payroll_expense (hr_expense/models/res_config_settings.py:19-21; module folders absent in the addons root: UNKNOWN — EVIDENCE INSUFFICIENT on what they do).
- Weekly reminder email to approvers who have submitted expenses waiting (hr_expense/data/hr_expense_cron.xml:4-11; hr_expense/models/hr_expense.py:1033-1072).
- Seeded categories (Meals, Travel & Accommodation, Mileage, Gifts, Communication, and a no-cost "Expenses" category) (hr_expense/data/hr_expense_data.xml:5-74).
- Menus: My Expenses (all internal users), Reporting (analysis), Configuration > Expense Categories (Administrator only), and "Employee Expenses" under Accounting payables for All Approvers (hr_expense/views/hr_expense_views.xml:632-651).

## B. Business objects, relationships, lifecycle
- Expense: employee, category (product), date, quantity, amounts (in expense currency and company currency, tax amounts), paid-by (Employee to reimburse = default / Company), payment method (company-paid only), vendor, account, taxes, analytic distribution, manager (approver), attachments (hr_expense/models/hr_expense.py:45-266).
- Status is derived, not typed in: Draft -> Submitted -> Approved -> Posted -> In Payment -> Paid, with Refused as a separate end state; once an accounting entry exists the status follows that entry (draft/not paid = Posted; in payment/partial = In Payment; paid or company-paid = Paid; a directly-cancelled entry shows Paid) (hr_expense/models/hr_expense.py:454-488). In practice, cancelling, reversing or deleting the entry returns the expense to Approved because the link to the entry is cleared (hr_expense/models/account_move.py:101-111; (TEST) hr_expense/tests/test_expenses_states.py:67-108).
- Submit: needs an employee owner (or approver right), and a category; sets the approver from defaults if empty; expenses with no approver, or whose approver is the employee themselves, skip "Submitted" and are approved immediately (hr_expense/models/hr_expense.py:1127-1146); (TEST) (hr_expense/tests/test_expenses_states.py:191-196).
- Default approver order: employee's Expense Approver, else the department manager (only if they hold the approver group), else the employee's direct manager's user; never the employee themselves (hr_expense/models/hr_expense.py:1507-1524). Employee's Expense Approver follows the manager automatically unless manually changed (hr_expense/models/hr_employee.py:62-70).
- Approve: checks permission, then, if similar expenses exist (same employee, category, date, amount, currency, company) in submitted/approved/posted/paid state, a confirmation wizard lets the approver approve or refuse as "Duplicate Expense"; on approval the approval date and the approver are stored (hr_expense/models/hr_expense.py:1148-1156,1447-1461,720-744; hr_expense/wizard/hr_expense_approve_duplicate.py:24-30). A same-receipt (identical attachment) warning is computed separately (hr_expense/models/hr_expense.py:697-718).
- Refuse: wizard asks a reason, which is posted on the expense; refusal is blocked if the linked accounting entry is already posted; draft linked entries are deleted (hr_expense/models/hr_expense.py:1158-1161,1467-1484).
- Reset to draft: reverses posted linked entries (cancelling) or deletes draft ones, clears approval data; blocked if the entry is posted and not reversible per the check (hr_expense/models/hr_expense.py:1204-1216,1434-1438).
- Post: only Approved expenses; company-paid: creates a payment and its entry (one entry per expense) and posts them together; employee-paid: wizard creates a vendor receipt per employee (all selected expenses of one employee in one receipt) and posts it (hr_expense/models/hr_expense.py:1163-1196,1440-1445,1531-1575,1577-1605,1607-1628). Only one company at a time for employee-paid batches (hr_expense/models/hr_expense.py:1177-1178). Company-paid expenses using SEPA credit transfer need a vendor (hr_expense/models/hr_expense.py:1180-1187).
- Reimbursement: employee-paid receipt is settled through the standard "Register payment" action; the bank account defaults to the employee's primary bank account, else the contact's first bank account (hr_expense/models/hr_expense.py:1198-1202; hr_expense/wizard/account_payment_register.py:10-19).
- Split: an expense can be split into several (halves by default, editable) while still draft/submitted; new expenses keep employee, approval state and attachments copies, and share an "origin" link (hr_expense/wizard/hr_expense_split_wizard.py:44-71; hr_expense/models/hr_expense.py:1486-1505); (TEST) (hr_expense/tests/test_expenses.py:221-345).
- Activities: a "review this expense" task is scheduled for the approver when submitted and closed on approval, removed on refusal or reset (hr_expense/models/hr_expense.py:1001-1031).

## C. Validations, automation, security, multi-company
- Amount rule: any expense beyond draft must have non-zero amounts (hr_expense/models/hr_expense.py:288-297); (TEST) (hr_expense/tests/test_expenses.py:660-707).
- One expense per payment; a company-paid entry can carry only one expense (hr_expense/models/hr_expense.py:299-303; hr_expense/models/account_move.py:30-35). A payment linked to an expense cannot change amount, date, partner, journal or method (hr_expense/models/account_payment.py:24-32); (TEST) (hr_expense/tests/test_expenses.py:644-658).
- Deletion blocked once approved/posted/in payment/paid (hr_expense/models/hr_expense.py:806-810). Attachments: cannot be added after approval nor deleted after submission except by privileged users (hr_expense/models/ir_attachment.py:10-28). Editing tax, analytic, account or approver fields requires edit rights on the record (hr_expense/models/hr_expense.py:812-822). Cannot delete an analytic account used in an expense or a tax used in transactions (hr_expense/models/analytic.py:27-45; hr_expense/models/account_tax.py skeleton; (TEST) hr_expense/tests/test_expenses.py:936-946).
- Analytic: a new applicability domain "Expense" lets analytic plans be mandatory per category; enforced at approval (also auto-approval at submit) (hr_expense/models/analytic.py:9-24; hr_expense/models/hr_expense.py:1450-1456); (TEST) (hr_expense/tests/test_expenses.py:991-1041).
- Groups: Team Approver (implies internal user) < All Approver < Administrator (root and admin users) (hr_expense/security/hr_expense_security.xml:9-29). Documented permission table in code: employee submits own; officer approves not-own for employees they manage (expense approver, manager, department manager); administrator anything; posting needs the billing accountant (hr_expense/models/hr_expense.py:25-40).
- Approval gate details: the approver must be in the expense's company, must hold approver rights over that employee (approver field, subordinate chain or department), and cannot approve their own expense unless Administrator (hr_expense/models/hr_expense.py:1378-1427); (TEST) own-expense and non-managed cases fail (hr_expense/tests/test_expenses_access_rights.py:73-105).
- Record rules: All Approvers and accountants (Accounting user group) see all; Team Approvers see own, subordinates', department-managed, approver-assigned; employees see own drafts (and, via a second read-only rule, own non-draft ones) and can create/edit/delete only in draft; global company rule (hr_expense/security/ir_rule.xml:4-52). Team approvers get read access to entries/lines linked to expenses (hr_expense/security/ir_rule.xml:54-66). Access lists: employees can create/edit own; billing accountants create/edit but not delete; team approvers read journals/entries and edit analytic lines (skeleton access rows; hr_expense/security/ir.model.access.csv).
- Employee selection is filtered by role: All Approvers any employee in the company tree; team approvers themselves and their reports; ordinary employees only themselves (hr_expense/models/hr_employee.py:33-52).
- Email intake (privacy/security): sender is matched to an employee by work email or user email; unmatched senders fall back to default handling; subject is parsed for category and amount; the new expense is created under that employee, and a confirmation mail is returned (hr_expense/models/hr_expense.py:856-936,1078-1120); (TEST) (hr_expense/tests/test_expenses_mail_import.py:10-104,232). Email sender addresses are not authenticated by this module: UNKNOWN — EVIDENCE INSUFFICIENT.
- Multi-company: expense company, tax and account resolved in the expense's company; post wizard journal must be in the same company, falls back through parent-company journals (hr_expense/wizard/hr_expense_post_wizard.py:9-26); (TEST) (hr_expense/tests/test_expenses.py:871-935,1189-1233).

## D. Accounting / payroll / analytic handoffs
- Owned here: the expense, approval, and the request to create entries. Accounting entries and payments are owned by the account module (models account.move receipt, account.payment) (hr_expense/models/hr_expense.py:1551-1605).
- Employee-paid: vendor receipt to the employee's work contact; expense-account lines (account from expense, else category, else company, else purchase journal default) and taxes (all taxes behave as price-included); credit to the employee's payable account; partner bank account taken from the employee (hr_expense/models/hr_expense.py:1607-1628,1723-1736,1751-1789,1791-1816; hr_expense/models/account_move.py:94-99). Test confirms company partner never overrides the employee as commercial partner (TEST: hr_expense/tests/test_expenses.py:1043-1059).
- Company-paid: an outbound payment plus entry, base and tax lines against the payment method's outstanding account (or default outstanding), reconciled later against the bank; no autobalancing line (hr_expense/models/hr_expense.py:1630-1712; (TEST) hr_expense/tests/test_expenses.py:1149-1170).
- Journals: company "Default Expense Journal" (purchase type) and, for company-paid, allowed payment methods list (hr_expense/models/res_company.py:9-21). Journal type check on entries is relaxed for expense entries (hr_expense/models/account_move.py:58-60).
- Analytic distribution flows from expense lines to the entry lines (hr_expense/models/hr_expense.py:1723-1736). Analytic plan applicability domain "Expense" (see C).
- Payroll reimbursement: setting exists but the payroll module is not in Community: UNKNOWN — EVIDENCE INSUFFICIENT. Re-invoicing to customers and projects is owned by sale_expense / project_hr_expense (dependants found in manifests: sale_expense, project_hr_expense, project_sale_expense).
- Dashboard tile module: spreadsheet_dashboard_hr_expense (found by grep; not read).

## E. Configuration / defaults that change outcomes
- Default paid-by: employee (to reimburse) (hr_expense/models/hr_expense.py:246-254). Currency defaults to company currency; category with a fixed cost forces company currency and unit cost while draft (hr_expense/models/hr_expense.py:309-313,633-659). Updating a category's cost changes all draft expenses using it, with a warning (hr_expense/models/product_product.py:9-50; (TEST) hr_expense/tests/test_expenses.py:753-870).
- Product flagged "can be expensed" only for goods/services that are purchasable; it also turns on "can be purchased" (hr_expense/models/product_template.py:33-41).
- Approver assignment (Expense Approver on employee) controls whether approval is skipped (hr_expense/models/hr_expense.py:1143-1146).
- Payment methods offered on company-paid expenses: the company's allowed list, else any active outbound method line (hr_expense/models/hr_expense.py:666-678).

## F. Effective extension path
- Extended/used by: sale_expense, project_hr_expense, project_sale_expense, spreadsheet_dashboard_hr_expense, l10n_fr_account, l10n_din5008_expense (manifest grep). Enterprise-only modules named in settings are absent.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: multi-expense batch posting edge cases beyond tests read, expense report views and PDF (hr_expense/report), currency-rate computation details, upgrade scripts (hr_expense/migrations).

