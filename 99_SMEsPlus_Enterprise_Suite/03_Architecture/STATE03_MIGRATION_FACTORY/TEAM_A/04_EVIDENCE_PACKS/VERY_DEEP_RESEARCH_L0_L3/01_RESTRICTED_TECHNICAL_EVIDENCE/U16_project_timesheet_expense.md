# U16 - project_timesheet_expense - Restricted Technical Evidence (L2/L3)

> RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Unit: U16 `project_timesheet_expense` | Date: 2026-10-02 | Source revision: `19.0.post20260921` (Community only)
> Modules owned: `project`, `project_account`, `project_purchase`, `project_purchase_stock`, `project_stock`, `project_stock_account`, `project_stock_landed_costs`, `project_hr_expense`, `project_sale_expense`, `project_todo`, `project_sms`, `project_mail_plugin`, `project_hr_skills`, `project_timesheet_holidays`, `hr_timesheet`, `hr_timesheet_attendance`, `hr_expense`, `sale_expense`, `sale_timesheet`, `sale_timesheet_margin`, `sale_project` (`sale_project_stock` belongs to U22 and was not studied).
> Read-only on source; restored DB queried for configuration only (counts of seeded configuration rows, group closure, product seed flags). No V-level, coverage %, denominator, Gate or Clean-Room statement is made. No Odoo execution; anything needing execution is flagged `RT`.

## Scope, method and honest limits
- Focus on service-revenue and cost flows that touch accounting: employee expense lifecycle (capture, approve, post, reimburse), re-invoicing of expenses, timesheet cost and billing, project analytic links and project profitability, project purchase/stock/landed-cost links.
- Source files read in full: `hr_expense/models/hr_expense.py`, all other `hr_expense` Python models, wizards, security, data and cron; `sale_expense`, `project_hr_expense`, `project_sale_expense`, `project_account`, `project_purchase`, `project_purchase_stock`, `project_stock`, `project_stock_account`, `project_stock_landed_costs` Python; `hr_timesheet/models/hr_timesheet.py`, `project_project.py`, `res_company.py`, security and data; `sale_timesheet` models, wizard, security and data; `sale_project` `sale_order.py`, `sale_order_line.py`, `product_template.py`, `account_move_line.py`, `project_task.py` (first 200 lines), `project_milestone.py` and the profitability part of `project_project.py` (lines 14-200 and 514-853); `project_timesheet_holidays` `hr_leave.py`, `account_analytic.py`, `res_company.py`, `resource_calendar_leaves.py` (lines 1-288); `hr_timesheet_attendance`, `project_sms`, `project_mail_plugin`, `project_hr_skills`, `project_todo` (models, report SQL, controllers, security).
- NOT read (honest gaps): the QWeb/XML views and report templates of all modules except the form-button and menu lines cited; `hr_expense/views/product_product_views.xml`, `hr_expense_report.xml`; `hr_timesheet/models/project_task.py`, `project_update.py`, `controllers/*`, portal pages; `sale_timesheet` portal controller and `project_task` beyond line 120; `sale_project` project template wizard, milestone portal, `project_project.py` lines 200-514 (action views, sale-order-item query); `project` module beyond the analytic, profitability, security and ACL parts cited (6.8k lines, most not read); tests other than `hr_expense/tests/test_expenses_states.py` lines 60-112; migrations; i18n; static JS.
- The prior structural extracts (`~/STATE03_RESTRICTED_LOCAL/sourcemap/*.json`) and candidate source-map records were NOT used as a basis (no DELTA-FIRST pass); one cross-check was made against `MODULE_hr_expense.md` (see Contradictions).
- Hand-offs (not studied here): quotation/pricing (U04), order invoicing engine and down payments (U05), purchase order lifecycle (U06/U07), stock valuation engine and landed costs (U10), entry posting/reversal engine (U11), payment and reconciliation engine (U12), taxes and chart (U13), analytic plans (U02), `sale_project_stock` (U22).

## Vocabulary and version facts used by this unit
- Odoo 19: `hr.expense` is a single object (no expense report/sheet); states `draft, submitted, approved, posted, in_payment, paid, refused`; `in_payment` is unreachable without the accounting app (hook returns `paid`, aligned with U12).
- Timesheets are `account.analytic.line` rows with `project_id`; there is no timesheet approval or lock state in the Community modules read.
- `res.groups._is_feature_enabled` tests the superuser's groups (used by the milestone feature).

## DISCOVERED SUPPORTING MODULES (read only as far as needed)
`account` (move/payment/analytic-line hooks, `_get_invoice_in_payment_state`), `sale` (re-invoice engine in `account_move_line.py`, `expense_policy`, analytic delivered quantity, `_prepare_analytic_account_data`), `stock_account` (`_create_analytic_move` and analytic amount), `hr_hourly_cost` (employee hourly cost), `hr_holidays`/`resource` (time-off leave and public-holiday calendar leaves), `hr_attendance`, `sms`/`mail_plugin` (named only), `purchase`/`stock`/`stock_landed_costs` (named only), `analytic` (mandatory plans, distribution model, not read). Found by grep and NOT read: `project_mrp`, `project_mrp_account`, `sale_project_stock` (U22), localisation modules extending expenses (`l10n_fr_account`, `l10n_din5008_expense` mentioned by prior record, not verified here), `spreadsheet_dashboard_hr_expense`. Enterprise modules named in settings (`hr_expense_extract`, `hr_expense_stripe`, `hr_payroll_expense`) are not in the Community addons path and were not studied.

## Contradictions / corrections with prior evidence
1. The unit brief speaks of an expense report state machine (submit/approve/post/reimburse). In this revision no report object exists; each expense is the unit (VDR-U16-C002, VDR-U16-C001) - flagged CONTRA against report-based terminology. This agrees with the prior candidate record `MODULE_hr_expense.md`.
2. `_track_subtype` in `hr_expense` matches a state value `cancel` that is not in the state selection (VDR-U16-C087); dead branch; not recorded in the one prior record cross-checked.
3. `action_reset` contains a reversal branch that its own pre-check makes unreachable (VDR-U16-C068).
4. `sale_timesheet._is_updatable_timesheet` references a method without calling it (VDR-U16-C272).
5. `sale_timesheet` narrows two core accounting analytic-line rules to entries without a project (VDR-U16-C240, VDR-U16-C241); this is a cross-module security effect not visible from `account` alone.
6. Two project-profitability extensions reuse section id `other_costs` (VDR-U16-C374, VDR-U16-C387).

## Runtime/AWT list (RT) - all unresolved items
VDR-U16-C016; VDR-U16-C042; VDR-U16-C075; VDR-U16-C089; VDR-U16-C154; VDR-U16-C158; VDR-U16-C161; VDR-U16-C162; VDR-U16-C163; VDR-U16-C202; VDR-U16-C203; VDR-U16-C296; VDR-U16-C414; VDR-U16-C418; VDR-U16-C419; VDR-U16-C422. Plus: mail gateway real-time behaviour, SMS gateway delivery, mail add-in authentication, outstanding-account auto-creation on non-standard charts, partial credit notes on timesheet invoices, billing-accountant record visibility on expenses.

## Capability derivation (6-10 business capabilities)
D1/D2/D3 below mean the three L3 dimensions (business purpose, architecture/data, source/workflow logic) were written for the capability; they are not V-levels.

| Capability | Name | Main modules | L3 dimensions | Function-ID |
|---|---|---|---|---|
| CAP-U16-01 | Employee expense capture and categories | hr_expense, project_hr_expense | D1, D2, D3 | FUNCTION MAPPING REQUIRED |
| CAP-U16-02 | Expense approval workflow | hr_expense | D1, D2, D3 | FUNCTION MAPPING REQUIRED |
| CAP-U16-03 | Expense accounting entry creation (employee-paid and company-paid) | hr_expense, sale_expense, project_sale_expense | D1, D2, D3 | FUNCTION MAPPING REQUIRED |
| CAP-U16-04 | Employee reimbursement and expense settlement status | hr_expense (+ account hooks) | D1, D2, D3 | FUNCTION MAPPING REQUIRED |
| CAP-U16-05 | Re-invoicing expenses to customers | sale_expense, project_sale_expense, project_hr_expense (+ sale) | D1, D2, D3 | FUNCTION MAPPING REQUIRED |
| CAP-U16-06 | Timesheet recording, cost valuation and analytic linkage | hr_timesheet, project, project_account, hr_hourly_cost (support) | D1, D2, D3 | FUNCTION MAPPING REQUIRED |
| CAP-U16-07 | Billing services and timesheets from sales orders | sale_timesheet, sale_project, sale_timesheet_margin | D1, D2, D3 | FUNCTION MAPPING REQUIRED |
| CAP-U16-08 | Sale-to-project generation and project analytic distribution | sale_project, project_purchase, sale_timesheet | D1, D2, D3 | FUNCTION MAPPING REQUIRED |
| CAP-U16-09 | Project profitability and project cost links (purchase, stock, landed cost, expense, time) | project_account, project_purchase, project_purchase_stock, project_stock, project_stock_account, project_stock_landed_costs, project_hr_expense, project_sale_expense, sale_timesheet, sale_project | D1, D2, D3 | FUNCTION MAPPING REQUIRED |
| CAP-U16-10 | Time-off, attendance comparison and project collaboration extensions | project_timesheet_holidays, hr_timesheet_attendance, project_sms, project_mail_plugin, project_hr_skills, project_todo | D1, D2, D3 | FUNCTION MAPPING REQUIRED |

## CAP-U16-01 Employee expense capture and categories

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no existing Function-ID names employee expense capture; closest adjacency RTG-F02 consumable expense timing is about stock and is not claimed).

### D1 - Business purpose and process semantics
An employee records a business expense as one record that carries a category (a product flagged expensable), an amount (typed or derived from quantity times category cost), a date, a currency, the payer (employee or company), optional customer-order and cost-allocation links, and receipts. Capture channels: manual entry, receipt-file upload, and email to an alias. In Odoo 19 Community there is no expense report or sheet object: every expense is submitted, approved and posted by itself (VDR-U16-C001, VDR-U16-C002).

### D2 - Architecture / data / object relationships
- `hr.expense` (stored fields: employee, product, quantity, price_unit, total_amount_currency, total_amount, tax_ids, account_id, analytic_distribution, payment_mode, payment_method_line_id, vendor_id, approval_state, state, account_move_id).
- `product.template.can_be_expensed` + `purchase_ok` (VDR-U16-C003, VDR-U16-C033, VDR-U16-C034); six seeded categories (VDR-U16-C035, VDR-U16-C036).
- `ir.attachment` guard on `hr.expense` (VDR-U16-C028, VDR-U16-C029); `hr.expense.split.wizard` + `hr.expense.split` transient models (VDR-U16-C024, VDR-U16-C025).
- Mail alias `expense` bound to the model (VDR-U16-C021); employee resolution from the sender (VDR-U16-C017, VDR-U16-C043).
- Support: `hr_hourly_cost` is not involved here; employee filter in `hr.employee` (VDR-U16-C039).

### D3 - Source / technical / workflow logic
Entry points: expense form, list, upload (create_expense_from_attachments), mail gateway (message_new), split wizard.

```
message_new -> _get_employee_from_email -> _parse_expense_subject(_parse_product, _parse_price) -> create(vals) -> _send_expense_success_mail   VDR-U16-C016 VDR-U16-C019 VDR-U16-C042
create_expense_from_attachments -> product EXP_GEN fallback -> create(price 0) -> attach as main attachment   VDR-U16-C022
compute chain: product -> uom, tax_ids, account_id, price_unit -> total_amount_currency -> currency_rate -> total_amount -> tax_amount/untaxed_amount   VDR-U16-C005 VDR-U16-C006 VDR-U16-C009 VDR-U16-C011 VDR-U16-C012
```
State: a new expense has `state = draft` (computed from approval_state/move; see CAP-U16-02/04). Inheritance: base `hr.expense` + `project_hr_expense` (default distribution from project context), `project_sale_expense` (distribution merge), `sale_expense` (sale_order_id, split values).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Create expense -> choose category -> amount/taxes/account computed -> receipt attached -> ready to submit (VDR-U16-C005, VDR-U16-C009, VDR-U16-C010). |
| 2 | Reversal / cancel / negative | Draft, submitted and refused expenses can be deleted; approved and later cannot (VDR-U16-C030); zero totals only allowed in draft (VDR-U16-C013). Receipts frozen after approval (VDR-U16-C028, VDR-U16-C029). |
| 3 | Multi-company / data scope | Company is a required readonly field defaulted from the environment; taxes and accounts are filtered to the expense company (VDR-U16-C009); email capture picks the employee's company (VDR-U16-C043); employee picker limited by group (VDR-U16-C039). |
| 4 | Side effects & cross-module | Category cost change rewrites draft expenses (VDR-U16-C031, VDR-U16-C032); mail success note or email (VDR-U16-C042); analytic defaults from distribution models and project context (VDR-U16-C040, VDR-U16-C200). |
| 5 | Configuration & optionality | Mail gateway parameter and alias (VDR-U16-C020, VDR-U16-C021); category flags (VDR-U16-C033); six seeded categories (VDR-U16-C035); OCR/card/payroll toggles point to absent modules (VDR-U16-C041). |
| 6 | Validation & constraints | Non-zero total after draft (VDR-U16-C013); employee required unless approver (VDR-U16-C037); split sum equality (VDR-U16-C025); category domain (VDR-U16-C003). |
| 7 | Roles & permissions | ACL: base users full CRUD at ACL level (VDR-U16-C038); row scope by rules (CAP-U16-02: VDR-U16-C081, VDR-U16-C083, VDR-U16-C084). |
| 8 | Scheduled / automated | None for capture; the mail gateway is event driven (VDR-U16-C016). |
| 9 | Exception & failure | No expensable category on upload raises (VDR-U16-C023); unknown sender produces an expense without employee data (VDR-U16-C018); mail failures are runtime (VDR-U16-C042). |
| 10 | Accounting / audit / compliance | No ledger effect at capture; receipt evidence and tracked fields give an audit trail (employee, product, amounts, payment mode are tracked on the model); duplicate and shared-receipt warnings are the only control against double claims (VDR-U16-C014, VDR-U16-C015, VDR-U16-C044). |

### DB reconciliation (configuration only)
OBSERVATION: VDR-U16-C036 six expense products present (all service, expensable, purchasable; mileage cost 1.0 per km). VDR-U16-C020 parameter hr_expense.use_mailgateway = True. DB shows hr.expense model plus five transient models (approve-duplicate, posting wizard, refuse wizard, split, split wizard) for `hr_expense`; zero expense rows (no business data).

### Unknown / Runtime list
- UNKNOWN: OCR, card feeds, payroll reimbursement (VDR-U16-C041).
- RT: mail gateway behaviour and confirmation email delivery (VDR-U16-C016, VDR-U16-C042).

## CAP-U16-02 Expense approval workflow

**Function-ID(s):** FUNCTION MAPPING REQUIRED (approval is not covered by an existing Function-ID).

### D1 - Business purpose and process semantics
The employee submits an expense; the responsible approver (employee-specific approver, department head, or direct manager) approves or refuses it; accountants then post approved expenses (CAP-U16-03). Approval is a field (`approval_state`) on the expense, and the visible state is derived from it unless an accounting entry exists. When nobody can approve, the expense is approved automatically (VDR-U16-C051, VDR-U16-C052).

### D2 - Architecture / data / object relationships
- Fields: `approval_state` (submitted/approved/refused), `approval_date`, `manager_id`, security booleans `is_editable`, `can_approve`, `can_reset`.
- Groups: team approver -> all approver -> administrator (VDR-U16-C079); record rules (VDR-U16-C081, VDR-U16-C082, VDR-U16-C083, VDR-U16-C084, VDR-U16-C085).
- Activity type `hr_expense.mail_act_expense_approval` (VDR-U16-C088); weekly cron (VDR-U16-C073).
- Wizards: refuse wizard (reason) (VDR-U16-C063), duplicate-approval wizard (VDR-U16-C058).

### D3 - Source / technical / workflow logic
```
action_submit -> [category required, permission] -> manager default (VDR-U16-C053) -> autovalidate? -> approval_state=submitted | _do_approve   VDR-U16-C050 VDR-U16-C051
action_approve -> _check_can_approve -> duplicates? -> wizard | _do_approve(validate analytic plans, manager=user, approval_date)   VDR-U16-C057 VDR-U16-C055 VDR-U16-C056
action_refuse -> wizard -> _do_refuse(reason) -> draft entries deleted / posted entry blocks   VDR-U16-C062 VDR-U16-C064 VDR-U16-C065
action_reset -> _check_can_reset_approval -> _do_reset_approval   VDR-U16-C067 VDR-U16-C069
```
State transitions (stored `state`, computed VDR-U16-C047):
- draft -> submitted [action_submit]
- draft/submitted -> approved [approve or auto-approval]
- submitted/approved -> refused [refuse wizard]
- approved/submitted/refused -> draft [action_reset]
- approved -> posted / paid [posting; CAP-U16-03/04]
Override chain: only `hr_expense` defines these methods; `sale_expense.action_post` and `project_sale_expense.action_post` extend posting, not approval.

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Employee submits -> activity to manager (VDR-U16-C071) -> manager approves -> activity done (VDR-U16-C072) -> state approved (VDR-U16-C056). |
| 2 | Reversal / cancel / negative | Refuse with reason (VDR-U16-C062, VDR-U16-C063); blocked if posted entry exists (VDR-U16-C064); reset clears approval (VDR-U16-C069) but is blocked for posted entries (VDR-U16-C067); dead reversal branch (VDR-U16-C068). |
| 3 | Multi-company / data scope | Global company rule (VDR-U16-C085); approver must have the expense company among allowed companies (VDR-U16-C060). |
| 4 | Side effects & cross-module | Activity scheduling and feedback (VDR-U16-C071, VDR-U16-C072); analytic mandatory-plan check at approval (VDR-U16-C055); chatter messages on state change (VDR-U16-C087). |
| 5 | Configuration & optionality | Approver per employee/department/manager (VDR-U16-C053, VDR-U16-C054); cron weekly (VDR-U16-C073, VDR-U16-C074). |
| 6 | Validation & constraints | Category required to submit (VDR-U16-C049); permission to submit for others (VDR-U16-C048); own-expense approval blocked (VDR-U16-C059); write guard on sensitive fields (VDR-U16-C078). |
| 7 | Roles & permissions | Rights matrix (VDR-U16-C045); three groups (VDR-U16-C079, VDR-U16-C080); rules (VDR-U16-C081, VDR-U16-C083, VDR-U16-C084, VDR-U16-C086); is_editable logic (VDR-U16-C077). |
| 8 | Scheduled / automated | Weekly cron sends one mail per manager listing submitted expenses (VDR-U16-C073, VDR-U16-C075); the inline mail branch is version gated and not taken at manifest version 2.1 (VDR-U16-C076). |
| 9 | Exception & failure | UserError on missing category, missing permission, own expense, posted entry (VDR-U16-C049, VDR-U16-C059, VDR-U16-C064); missing company email skips the reminder (see VDR-U16-C075). |
| 10 | Accounting / audit / compliance | Segregation of duties: approver cannot approve own expense unless administrator (VDR-U16-C059) but auto-approval exists (VDR-U16-C051, VDR-U16-C090); approval stamps approver and date (VDR-U16-C056); no ledger entry yet. |

### DB reconciliation (configuration only)
OBSERVATION: VDR-U16-C086 14 ACL rows, 12 record rules, 3 groups, 1 privilege record; VDR-U16-C080 group member counts (administrator 2 direct users; all-approver and team-approver 0 direct users); VDR-U16-C074 cron active weekly; mail activity type, 6 message subtypes, 1 alias, 1 sequence present for `hr_expense`.

### Unknown / Runtime list
- UNKNOWN: billing-accountant visibility (VDR-U16-C089, VDR-U16-C084).
- RT: reminder email delivery (VDR-U16-C075).

## CAP-U16-03 Expense accounting entry creation (employee-paid and company-paid)

**Function-ID(s):** FUNCTION MAPPING REQUIRED (adjacent but not matching: PDT-F02 per-receipt billing alignment is about purchase receipts).

### D1 - Business purpose and process semantics
An accountant posts approved expenses. For expenses the employee paid, the system builds one vendor receipt per employee (credit: employee payable; debit: expense account and input tax) and posts it immediately (VDR-U16-C102, VDR-U16-C103, VDR-U16-C101). For expenses the company paid, it builds an outgoing payment and its entry so a later bank statement line can be matched; the expense is then paid at once (VDR-U16-C117, VDR-U16-C120, VDR-U16-C140).

### D2 - Architecture / data / object relationships
- Objects: `hr.expense` -> `account.move` (`account_move_id`, `expense_ids`), `account.move.line.expense_id`, `account.payment` (company-paid) via `origin_payment_id`.
- Wizard `hr.expense.post.wizard` (journal, accounting date) (VDR-U16-C096, VDR-U16-C100).
- Company fields `expense_journal_id`, `company_expense_allowed_payment_method_line_ids` (VDR-U16-C132, VDR-U16-C131).
- Employee work contact and primary bank account (VDR-U16-C104, VDR-U16-C106); payable account of the work contact (VDR-U16-C111).
- Tax engine hooks: `account.tax._prepare_*` with `expense_id` grouping (VDR-U16-C123); `account.move.line._compute_totals` force_price_include (VDR-U16-C122).

### D3 - Source / technical / workflow logic
```
action_post -> _check_can_create_move [approved only] -> split payer modes   VDR-U16-C091 VDR-U16-C092
  company-paid: _create_company_paid_moves -> _prepare_payments_vals -> account.move (+lines) -> account.payment(origin) -> payment.action_post   VDR-U16-C117 VDR-U16-C120
  employee-paid: _post_wizard -> hr.expense.post.wizard.action_post_entry -> _prepare_receipts_vals (per employee) -> account.move in_receipt create (sudo) -> action_post   VDR-U16-C095 VDR-U16-C099 VDR-U16-C101
```
Accounts: base `_get_base_account` (VDR-U16-C110), payable/outstanding `_get_expense_account_destination` (VDR-U16-C111, VDR-U16-C113). Taxes: total-included extraction (VDR-U16-C121, VDR-U16-C122). State: approved -> posted (employee-paid) or approved -> paid (company-paid) via `_compute_state` (CAP-U16-04).
Override chain: `hr_expense.action_post` -> `sale_expense.action_post` (create analytic account for the order, VDR-U16-C168) -> `project_sale_expense.action_post` (project distribution, VDR-U16-C169); `account.payment._compute_outstanding_account_id` override (VDR-U16-C129).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Approved employee-paid expenses -> posting dialog -> receipt posted (VDR-U16-C099, VDR-U16-C101); company-paid -> payment + entry posted together (VDR-U16-C120). |
| 2 | Reversal / cancel / negative | Entry reversal or cancel detaches the expense (CAP-U16-04: VDR-U16-C151, VDR-U16-C152); posted entries cannot be reset by the expense (VDR-U16-C067). |
| 3 | Multi-company / data scope | Employee-paid expenses of different companies cannot be posted together (VDR-U16-C093); journal default climbs parent companies (VDR-U16-C096). |
| 4 | Side effects & cross-module | Analytic distribution and order analytic account (VDR-U16-C134, VDR-U16-C168); outstanding accounts may be created (VDR-U16-C115); attachments copied to the entry (VDR-U16-C107); payment locked against edits (VDR-U16-C128). |
| 5 | Configuration & optionality | Default expense journal and allowed payment methods (VDR-U16-C132, VDR-U16-C131); posting without wizard path (VDR-U16-C135). |
| 6 | Validation & constraints | Approved only (VDR-U16-C091); payer mode set (VDR-U16-C091); SEPA vendor (VDR-U16-C094); one company-paid expense per entry (VDR-U16-C126, VDR-U16-C127); missing work contact (VDR-U16-C112); no payable account ambiguity (VDR-U16-C114); no payment method (VDR-U16-C119). |
| 7 | Roles & permissions | Billing accountants post (form button group, ACL read/write/create); wizard requires create on account.move (VDR-U16-C098); entries created in sudo (VDR-U16-C099); wizard ACL for billing group (VDR-U16-C086 counts). |
| 8 | Scheduled / automated | NOT APPLICABLE: no schedule; posting is user triggered. |
| 9 | Exception & failure | UserErrors cited in the validation row; archived outstanding account redirects (VDR-U16-C116); no expense account found raises (VDR-U16-C110). |
| 10 | Accounting / audit / compliance | Receipt in company currency (VDR-U16-C105); employee payable credit (VDR-U16-C111); tax extraction (VDR-U16-C121); journal-type check waived (VDR-U16-C124, VDR-U16-C125); company-paid vendor optional (VDR-U16-C136); Thai withholding tax effect not traced (VDR-U16-C137); anglo-saxon flag is off in this DB (not used by this capability). |

### DB reconciliation (configuration only)
OBSERVATION: VDR-U16-C132 company row has an expense journal of type purchase (code BILL) and an expense account; chart `th`; sequence hr.expense.invoice seeded but unused by this code (VDR-U16-C138). No expenses, receipts or payments exist.

### Unknown / Runtime list
- UNKNOWN: Thai tax effects (VDR-U16-C137); outstanding-account auto creation with non-standard prefix (VDR-U16-C116).
- RT: none beyond the platform: no network call in posting.

## CAP-U16-04 Employee reimbursement and expense settlement status

**Function-ID(s):** FUNCTION MAPPING REQUIRED (accounts payable settlement is covered by U12; this capability only maps expense status to payment status).

### D1 - Business purpose and process semantics
After posting, the employee is reimbursed by registering a payment on the receipt. The expense mirrors the receipt: posted until paid, then paid; company-paid expenses are paid immediately. Reversing or cancelling the receipt detaches it so the expense can be re-posted (VDR-U16-C139, VDR-U16-C151, VDR-U16-C152).

### D2 - Architecture / data / object relationships
- `hr.expense.state` stored computed field depends on `amount_residual`, `account_move_id.state`, `payment_state`, `approval_state` (VDR-U16-C139, VDR-U16-C145).
- `account.payment.register` override for bank account and expense tagging (VDR-U16-C147, VDR-U16-C148).
- `account.move` overrides for reversal and cancel (VDR-U16-C151, VDR-U16-C153); `account.move.line` partner rule (VDR-U16-C149).
- Edition hook `_get_invoice_in_payment_state` (VDR-U16-C144, aligns with U12).

### D3 - Source / technical / workflow logic
State derivation (VDR-U16-C139):
- no move: approval_state or draft
- move cancelled -> paid (VDR-U16-C142)
- company-paid with move -> paid (VDR-U16-C140)
- move draft or not_paid -> posted (VDR-U16-C141)
- in_payment or partial with residual -> hook value = paid in Community (VDR-U16-C143, VDR-U16-C144)
- otherwise (paid, partial without residual, reversed) -> paid
Transitions: approved -> posted [post]; posted -> paid [register payment]; posted/paid -> approved [entry reversed/cancelled/link cleared] (VDR-U16-C155).
Override chain: `account.move._reverse_moves`/`button_cancel` in `hr_expense`, extended by `sale_expense` reset helper (VDR-U16-C190).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Post receipt -> Register Payment from the expense (VDR-U16-C146) -> bank account prefilled (VDR-U16-C147) -> expense becomes paid (VDR-U16-C139, VDR-U16-C143). |
| 2 | Reversal / cancel / negative | Reverse or cancel clears the link so the expense returns to approved (VDR-U16-C151, VDR-U16-C152, VDR-U16-C155); payment is not undone (VDR-U16-C158, N-U16-092 in the neutral layer). |
| 3 | Multi-company / data scope | NOT APPLICABLE beyond company-specific journals and accounts of the receipt (CAP-U16-03). |
| 4 | Side effects & cross-module | Order line quantity reset when entry is reversed or reset (VDR-U16-C190, VDR-U16-C189); dashboard buckets (VDR-U16-C156, VDR-U16-C157). |
| 5 | Configuration & optionality | Payroll reimbursement and card feeds are absent-module toggles (VDR-U16-C159). |
| 6 | Validation & constraints | Partner forced from receipt on every line (VDR-U16-C149, VDR-U16-C150); payment tagging (VDR-U16-C148). |
| 7 | Roles & permissions | Payment registration is the standard accounting action; billing role needed as for any receipt payment (not expense specific). |
| 8 | Scheduled / automated | NOT APPLICABLE. |
| 9 | Exception & failure | Cancelled move read as paid (VDR-U16-C142, N-U16-091 in the neutral layer); effect of clearing relation unverified (VDR-U16-C154). |
| 10 | Accounting / audit / compliance | Receipts stay as audit trail; reversal creates credit note while expense detaches (VDR-U16-C151); in_payment status unreachable in Community (VDR-U16-C144). |

### DB reconciliation (configuration only)
OBSERVATION: no receipts or expenses exist; the in-payment hook is source-only (VDR-U16-C144). Payment-method lines present in DB: 3 in total (type not split here).

### Unknown / Runtime list
- RT: clearing a one-to-many link (VDR-U16-C154); payment after reversal (VDR-U16-C158).
- UNKNOWN: payroll deduction (VDR-U16-C159).

## CAP-U16-05 Re-invoicing expenses to customers

**Function-ID(s):** FUNCTION MAPPING REQUIRED (no existing Function-ID covers expense re-invoicing).

### D1 - Business purpose and process semantics
An expense posted against a confirmed customer order creates an order line (at cost or sales price) so the next customer invoice bills it. Link is by explicit order on the expense, or by project analytic account when `project_sale_expense` is installed (VDR-U16-C165, VDR-U16-C173, VDR-U16-C174).

### D2 - Architecture / data / object relationships
- `hr.expense.sale_order_id`/`sale_order_line_id` (`sale_expense`), `sale.order.line.expense_ids`, `sale.order.expense_ids` (VDR-U16-C165, VDR-U16-C192).
- Core in `sale`: `account.move.line._prepare_analytic_lines` -> `_sale_can_be_reinvoice` -> `_sale_create_reinvoice_sale_line` (VDR-U16-C170, VDR-U16-C172, VDR-U16-C176).
- Qty source: analytic delivered method (VDR-U16-C188, VDR-U16-C187).
- `project_hr_expense`, `project_sale_expense` for project-key mapping (VDR-U16-C200, VDR-U16-C174, VDR-U16-C201).

### D3 - Source / technical / workflow logic
```
action_post [sale_expense: create AA for order if none] -> account.move posted -> analytic lines prepared (needs distribution) -> _sale_can_be_reinvoice -> _sale_determine_order(expense order, else project) -> state checks -> price (cost|sales_price) -> create sale.order.line(is_expense)   VDR-U16-C168 VDR-U16-C170 VDR-U16-C173 VDR-U16-C176 VDR-U16-C179 VDR-U16-C181
```
Reset path: `_reverse_moves` / `button_draft` / `unlink` -> `_sale_expense_reset_sol_quantities` (VDR-U16-C190, VDR-U16-C189).
Inheritance: `sale._sale_determine_order` ({}), + `sale_project` (project mapping), + `sale_expense` (expense mapping), `project_sale_expense` (merge, expense wins) (VDR-U16-C174).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Expense with order and reinvoiceable category posted -> order line created -> invoice from order bills it (VDR-U16-C172, VDR-U16-C181, VDR-U16-C187). |
| 2 | Reversal / cancel / negative | Reverse/draft/delete resets order line to zero (VDR-U16-C190, VDR-U16-C189); reversal entries never re-invoice (VDR-U16-C171); reimbursement not unwound (VDR-U16-C203). |
| 3 | Multi-company / data scope | Order name search limited to user companies, no record rules (VDR-U16-C193); checks on order state (VDR-U16-C176). |
| 4 | Side effects & cross-module | Creates analytic account/lines, order line, delivered quantity, customer invoice lines later; project mapping (VDR-U16-C174, VDR-U16-C175). |
| 5 | Configuration & optionality | Policy per category (VDR-U16-C164, VDR-U16-C196, VDR-U16-C197); visibility (VDR-U16-C194). |
| 6 | Validation & constraints | Order must be confirmed, not cancelled, not locked (VDR-U16-C176, VDR-U16-C177, VDR-U16-C178); policy forced no for non expensable (VDR-U16-C195). |
| 7 | Roles & permissions | Salesperson name search sudo path (VDR-U16-C193); reset helper checks write access then sudo (VDR-U16-C189). |
| 8 | Scheduled / automated | NOT APPLICABLE. |
| 9 | Exception & failure | UserErrors for draft, cancelled, locked orders (VDR-U16-C176, VDR-U16-C177, VDR-U16-C178); storable-category reset note (VDR-U16-C191). |
| 10 | Accounting / audit / compliance | Customer tax from product not expense (VDR-U16-C182); price at cost uses posted amount (VDR-U16-C180); revenue recognised only on the customer invoice, not at expense posting. |

### DB reconciliation (configuration only)
OBSERVATION: VDR-U16-C197 seeded policies in the DB; no orders or expenses exist.

### Unknown / Runtime list
- RT: reversal of an invoiced expense line (VDR-U16-C202).

## CAP-U16-06 Timesheet recording, cost valuation and analytic linkage

**Function-ID(s):** FUNCTION MAPPING REQUIRED (RTG-F04 service routing is about product routing and is not claimed).

### D1 - Business purpose and process semantics
Employees record time on a project and task; each entry is an analytic line whose amount is minus hours times the employee (or project-specific) hourly cost, attached to the project's analytic account, so project cost can be read without any ledger entry (VDR-U16-C204, VDR-U16-C212, VDR-U16-C219).

### D2 - Architecture / data / object relationships
- `account.analytic.line` extended with `project_id`, `task_id`, `employee_id`, `department_id`, `manager_id` (VDR-U16-C204).
- `project.project.account_id` / `allow_timesheets`; auto-created analytic account (VDR-U16-C220, VDR-U16-C221, VDR-U16-C223).
- `hr.employee.hourly_cost` (`hr_hourly_cost`) (VDR-U16-C215); project employee-rate table cost (VDR-U16-C216).
- Company: internal project, encoding unit, project time unit (VDR-U16-C227, VDR-U16-C229).
- Reports: timesheets analysis SQL view (VDR-U16-C243); `hr_timesheet_attendance` (CAP-U16-10).

### D3 - Source / technical / workflow logic
```
create(vals) -> sudo reads project/task -> company/uom/name defaults -> employee resolution -> analytic account columns from project -> super().create -> _timesheet_postprocess -> amount = -unit_amount * _hourly_cost   VDR-U16-C207 VDR-U16-C209 VDR-U16-C211 VDR-U16-C212
write -> _check_can_write (own entry) -> re-resolve accounts -> super().write -> postprocess   VDR-U16-C233
```
Inheritance: `hr_timesheet` base -> `sale_timesheet` (so_line, billing locks, employee-rate cost VDR-U16-C216) -> `project_timesheet_holidays` (time off locks VDR-U16-C402).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Record time -> entry with project/task/employee/account -> cost computed -> reports (VDR-U16-C207, VDR-U16-C212, VDR-U16-C243). |
| 2 | Reversal / cancel / negative | Edit or delete by owner or approver until invoiced or tied to time off (CAP-U16-07/10); negative quantities give positive amounts (timesheet revenue type in VDR-U16-C261). |
| 3 | Multi-company / data scope | Same-company check (VDR-U16-C218); company from task/project (VDR-U16-C207); report multi-company rule (VDR-U16-C244); internal project per company (VDR-U16-C227). |
| 4 | Side effects & cross-module | Project remaining hours (VDR-U16-C232); analytic accounts auto-created (VDR-U16-C221, VDR-U16-C222); employee delete guard (VDR-U16-C242). |
| 5 | Configuration & optionality | Encoding hours/days and time unit (VDR-U16-C229, VDR-U16-C230, VDR-U16-C231); hourly cost optional (VDR-U16-C214); portal rule inactive (VDR-U16-C239). |
| 6 | Validation & constraints | Private task (VDR-U16-C206); active employee (VDR-U16-C209); same company (VDR-U16-C218); active account (VDR-U16-C217); mandatory plans (VDR-U16-C211); project must have account (VDR-U16-C220). |
| 7 | Roles & permissions | Three groups (VDR-U16-C237); rules (VDR-U16-C234, VDR-U16-C235, VDR-U16-C236); ACL (VDR-U16-C238); hourly cost HR-only (VDR-U16-C247); accountant rules narrowed (VDR-U16-C240, VDR-U16-C241). |
| 8 | Scheduled / automated | NOT APPLICABLE; reminders are settings only (VDR-U16-C231). |
| 9 | Exception & failure | ValidationErrors in validation row; project delete redirect (VDR-U16-C224). |
| 10 | Accounting / audit / compliance | No ledger entry (VDR-U16-C219); cost stored at record time (VDR-U16-C245); not reconciled with payroll (VDR-U16-C249); accountants cannot see project time via accounting rules (VDR-U16-C241); no approval/lock (VDR-U16-C248). |

### DB reconciliation (configuration only)
OBSERVATION: VDR-U16-C228, VDR-U16-C230, VDR-U16-C241. hr_timesheet owns 8 ACL rows, 9 record rules, 3 groups in the DB (equal to source 8/9/3); 2 analytic lines with project exist from install hooks (zero hours).

### Unknown / Runtime list
- UNKNOWN: approval/lock (VDR-U16-C248), payroll link (VDR-U16-C249).
- RT: calendar batch entry and portal rule (VDR-U16-C239).

## CAP-U16-07 Billing services and timesheets from sales orders

**Function-ID(s):** FUNCTION MAPPING REQUIRED (adjacent: SDV-F04 invoicing policy is verified in U05 for goods; the service policies here are an extension and are not claimed under it).

### D1 - Business purpose and process semantics
Services sold on an order are billed according to a service policy (prepaid/fixed, time, manual quantity, milestones). For time-billed lines, recorded time sums to the delivered quantity; creating the customer invoice links the time entries to it and locks them; credit notes release them (VDR-U16-C250, VDR-U16-C251, VDR-U16-C254, VDR-U16-C263, VDR-U16-C273).

### D2 - Architecture / data / object relationships
- `product.template.service_policy` (computed from `invoice_policy`+`service_type`) (VDR-U16-C250, VDR-U16-C251).
- `sale.order.line` qty_delivered_method timesheet/milestones (VDR-U16-C253, VDR-U16-C256), remaining hours (VDR-U16-C278).
- `account.analytic.line.so_line`, `timesheet_invoice_id`, `timesheet_invoice_type` (VDR-U16-C260, VDR-U16-C259).
- `project.sale.line.employee.map` (VDR-U16-C289, VDR-U16-C290), project pricing type (VDR-U16-C293).
- Wizard `sale.advance.payment.inv` extended with date range (VDR-U16-C267); `sale_timesheet_margin` (VDR-U16-C282).

### D3 - Source / technical / workflow logic
```
record time -> _compute_so_line (task/project/employee map) -> qty_delivered (sum unit_amount) -> qty_to_invoice -> invoice wizard (optional dates: _recompute_qty_to_invoice) -> sale.order._create_invoices -> _link_timesheets_to_invoice -> timesheet_invoice_id   VDR-U16-C257 VDR-U16-C254 VDR-U16-C267 VDR-U16-C263 VDR-U16-C265
credit note posted -> action_post releases entries; draft line unlink releases entries; reverse-and-modify relinks   VDR-U16-C273 VDR-U16-C274 VDR-U16-C275
```
Billed state: open -> locked (invoice draft or posted, not cancelled) -> open (cancelled, reversed, deleted) (VDR-U16-C262, VDR-U16-C270, VDR-U16-C271).
Inheritance: `sale` -> `sale_project` (milestones, project fields) -> `sale_timesheet` (timesheet method, invoice link).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Confirm order -> project/task generated (CAP-U16-08) -> time recorded -> invoice from order bills the time and links entries (VDR-U16-C254, VDR-U16-C263). |
| 2 | Reversal / cancel / negative | Credit note releases time (VDR-U16-C273); draft line deletion releases time (VDR-U16-C274); cancelled invoice frees time (VDR-U16-C262). |
| 3 | Multi-company / data scope | Entry company from task/project (CAP-U16-06); employee table lookup respects companies (VDR-U16-C258, uses env companies); orders per company. |
| 4 | Side effects & cross-module | Upsell activity (VDR-U16-C276); remaining hours (VDR-U16-C278); margin (VDR-U16-C282); analysis report revenues (VDR-U16-C284). |
| 5 | Configuration & optionality | Service policy options and milestone feature (VDR-U16-C250, VDR-U16-C252); threshold (VDR-U16-C277); pricing type (VDR-U16-C293); time product seed (VDR-U16-C279, VDR-U16-C280). |
| 6 | Validation & constraints | Billing locks (VDR-U16-C270, VDR-U16-C271); service-only links (VDR-U16-C285, VDR-U16-C286, VDR-U16-C287); unique employee row (VDR-U16-C289); time product protected (VDR-U16-C281). |
| 7 | Roles & permissions | Employee table ACL (VDR-U16-C292); project manager read of service lines (VDR-U16-C291); invoice creation inherits sale invoicing rights (U05). |
| 8 | Scheduled / automated | NOT APPLICABLE; upsell activity is evaluated when invoice status recomputes (VDR-U16-C276). |
| 9 | Exception & failure | UserErrors on locked time (VDR-U16-C270, VDR-U16-C271); misdirected not-billed guard (VDR-U16-C272); partial credit notes unverified (VDR-U16-C296). |
| 10 | Accounting / audit / compliance | Traceable time-to-invoice link (VDR-U16-C265); revenue recognised on the customer invoice only; margin uses actual time cost (VDR-U16-C282); date-range recompute overwrites quantity (VDR-U16-C269). |

### DB reconciliation (configuration only)
OBSERVATION: VDR-U16-C280, VDR-U16-C252 milestone feature off. sale_timesheet owns 2 ACL rows (equal to source) and overrides 2 foreign account rules. No orders or timesheets billed.

### Unknown / Runtime list
- RT: VDR-U16-C296; mixed unit conversion (VDR-U16-C255).

## CAP-U16-08 Sale-to-project generation and project analytic distribution

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 - Business purpose and process semantics
Confirming an order with service products creates the project and task that will carry the work, and propagates the project's analytic account onto order lines, invoice lines and purchase lines so cost and revenue can be matched (VDR-U16-C297, VDR-U16-C301, VDR-U16-C315, VDR-U16-C316, VDR-U16-C319).

### D2 - Architecture / data / object relationships
- Product: `service_tracking`, `project_id`, `project_template_id`, `task_template_id` (VDR-U16-C299, VDR-U16-C300).
- Order: `sale.order.project_id`, `project_ids`; line: `project_id`, `task_id` (VDR-U16-C297, VDR-U16-C302).
- Project: `sale_line_id`, `allow_billable`, `reinvoiced_sale_order_id` (VDR-U16-C305, VDR-U16-C326).
- Analytic: `_prepare_analytic_account_data` (VDR-U16-C304).

### D3 - Source / technical / workflow logic
```
action_confirm -> _action_confirm -> order_line._timesheet_service_generation()   VDR-U16-C297
  project_only/task_in_project: one project per order (or per template) -> optional task per line -> milestones   VDR-U16-C301 VDR-U16-C306 VDR-U16-C313
  task_global_project: task in the product's/order's project or UserError   VDR-U16-C312
```
Order cancel clears project.sale_line_id (VDR-U16-C314). Linking a project/task to a draft order line confirms the order (VDR-U16-C322).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Confirm order -> project (+task) generated, linked, billable, account created (VDR-U16-C297, VDR-U16-C305, VDR-U16-C303). |
| 2 | Reversal / cancel / negative | Cancel clears project link (VDR-U16-C314); reconfirm reuses (VDR-U16-C302). |
| 3 | Multi-company / data scope | Generation per order company with company context (VDR-U16-C297); partner/company mismatch clears customer (VDR-U16-C324). |
| 4 | Side effects & cross-module | Allocated hours (VDR-U16-C309, VDR-U16-C311); analytic propagation (VDR-U16-C315, VDR-U16-C316, VDR-U16-C317, VDR-U16-C319); default stages (VDR-U16-C307). |
| 5 | Configuration & optionality | Product tracking options and templates (VDR-U16-C299, VDR-U16-C306); skip context (VDR-U16-C298). |
| 6 | Validation & constraints | Product setting constraint (VDR-U16-C300); project required for global task (VDR-U16-C312); billable needs customer (VDR-U16-C324, VDR-U16-C325). |
| 7 | Roles & permissions | Create-project button for project managers (VDR-U16-C320, VDR-U16-C321); project manager read rule (VDR-U16-C327); generation in sudo (VDR-U16-C328). |
| 8 | Scheduled / automated | NOT APPLICABLE. |
| 9 | Exception & failure | UserError when no project (VDR-U16-C312); failure in generation blocks confirm (VDR-U16-C328, neutral risk). |
| 10 | Accounting / audit / compliance | Project account is the key for profitability (CAP-U16-09); shared accounts can cross-assign costs (VDR-U16-C329); auto-confirm of draft orders (VDR-U16-C322). |

### DB reconciliation (configuration only)
OBSERVATION: VDR-U16-C327 sale_project 4 ACL + 1 rule equal source; 1 project (internal) exists, no sale-generated projects.

### Unknown / Runtime list
- UNKNOWN: template duplication details (VDR-U16-C330).

## CAP-U16-09 Project profitability and project cost links (purchase, stock, landed cost, expense, time)

**Function-ID(s):** FUNCTION MAPPING REQUIRED (adjacent GRV-F05 landed cost allocation: only the project allocation of landed cost lines is added here; not claimed under that ID).

### D1 - Business purpose and process semantics
A live project dashboard computes revenue and cost per project by summing sales order lines, customer invoices, vendor bills, purchase orders, expenses, stock transfers and time entries that share the project's analytic account, with margin (VDR-U16-C335, VDR-U16-C338).

### D2 - Architecture / data / object relationships
- Framework in `project` (`_get_profitability_items`, labels, sequences) (VDR-U16-C335).
- Contributors: `project_account` (vendor bills, other analytic lines, VDR-U16-C349, VDR-U16-C351); `sale_project` (order lines, invoices, VDR-U16-C341, VDR-U16-C344); `sale_timesheet` (time, VDR-U16-C383); `project_purchase` (VDR-U16-C354, VDR-U16-C355); `project_stock_account` (VDR-U16-C362, VDR-U16-C363); `project_stock_landed_costs` (VDR-U16-C375); `project_hr_expense`, `project_sale_expense` (VDR-U16-C377, VDR-U16-C381).
- Link fields: `purchase.order.project_id`, `stock.picking.project_id` (VDR-U16-C357, VDR-U16-C361).

### D3 - Source / technical / workflow logic
```
get_panel_data -> _get_profitability_items (override chain: base {} -> project_account aal -> sale_project sol+invoices+purchase hook -> sale_timesheet aal by type -> project_purchase PO+bills -> project_hr_expense / project_sale_expense -> project_stock_account picking costs)   VDR-U16-C335 VDR-U16-C340
stock move done/picked -> _create_analytic_move (project distribution, category picking_entry, amount=value)   VDR-U16-C371 VDR-U16-C372 VDR-U16-C364 VDR-U16-C365 VDR-U16-C368
```
Double-count guards: invoice lines excluded when linked to order lines (VDR-U16-C344) or expenses (VDR-U16-C379, VDR-U16-C382) or purchase lines (VDR-U16-C356); vendor_bill analytic lines skipped (VDR-U16-C383).

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Project with account -> orders, bills, POs, expenses, transfers, time -> dashboard (VDR-U16-C340, VDR-U16-C354, VDR-U16-C377, VDR-U16-C373, VDR-U16-C383). |
| 2 | Reversal / cancel / negative | Credit notes and refunds net into amounts (VDR-U16-C350, VDR-U16-C355); cancelled documents excluded by domain (VDR-U16-C392). |
| 3 | Multi-company / data scope | Amounts converted to project currency (VDR-U16-C390); sudo reads; company of project used for conversion. |
| 4 | Side effects & cross-module | Goods transfers create analytic cost lines (VDR-U16-C371); landed costs carry project (VDR-U16-C375); PO/receipt project propagation (VDR-U16-C358, VDR-U16-C359). |
| 5 | Configuration & optionality | Operation type flag (VDR-U16-C362); mandatory plan (VDR-U16-C366, VDR-U16-C367); billable-only panel (VDR-U16-C339). |
| 6 | Validation & constraints | Mandatory plans on project before transfer entries (VDR-U16-C366). |
| 7 | Roles & permissions | Panel for project users, values for managers, links by role (VDR-U16-C336, VDR-U16-C337, VDR-U16-C388, VDR-U16-C389). |
| 8 | Scheduled / automated | NOT APPLICABLE; computed on demand. |
| 9 | Exception & failure | ValidationError for missing plans (VDR-U16-C366); fragile purchase state filter (VDR-U16-C354). |
| 10 | Accounting / audit / compliance | Management view, not ledger (VDR-U16-C391, neutral risk); draft counted as to invoice/bill (VDR-U16-C345); transfer cost uses stock valuation or standard price estimate (VDR-U16-C368, VDR-U16-C369); section id reuse (VDR-U16-C374, VDR-U16-C387); analytic accounting feature off in DB (VDR-U16-C394). |

### DB reconciliation (configuration only)
OBSERVATION: VDR-U16-C394; no analytic applicability rows (count 0); 1 analytic plan, 1 analytic account; no purchase/stock/expense documents. Seeded config rows by these modules: none (no data records beyond views).

### Unknown / Runtime list
- RT/UNKNOWN: currency conversion differences (VDR-U16-C391); manufacturing cost entries are excluded here (VDR-U16-C351).

## CAP-U16-10 Time-off, attendance comparison and project collaboration extensions

**Function-ID(s):** FUNCTION MAPPING REQUIRED.

### D1 - Business purpose and process semantics
Four auto-installed bridges: time off creates internal-project timesheets; attendance is compared with time entries; stage changes can text the customer; a mail add-in creates tasks; plus skills on tasks and a personal to-do list. Only the time-off and attendance bridges touch analytic cost (VDR-U16-C395, VDR-U16-C409, VDR-U16-C410).

### D2 - Architecture / data / object relationships
- `hr.leave.timesheet_ids`, `resource.calendar.leaves.timesheet_ids`, company `leave_timesheet_task_id` (VDR-U16-C397, VDR-U16-C405, VDR-U16-C408).
- SQL view `hr.timesheet.attendance.report` (VDR-U16-C410).
- `sms.template` link on project stage/task type (VDR-U16-C414).
- Controllers `/mail_plugin/...` (VDR-U16-C419).
- `res.users.employee_skill_ids` (VDR-U16-C423); private tasks (VDR-U16-C424).

### D3 - Source / technical / workflow logic
```
hr.leave._validate_leave_request -> _generate_timesheets -> analytic lines on internal project/task   VDR-U16-C395 VDR-U16-C396 VDR-U16-C397
refuse/cancel/delete -> unlink entries   VDR-U16-C399 VDR-U16-C400 VDR-U16-C429
resource.calendar.leaves create/write -> _generate_public_time_off_timesheets   VDR-U16-C405 VDR-U16-C407
project/task write(stage_id) -> _send_sms -> _message_sms_with_template   VDR-U16-C414 VDR-U16-C415
```

### Ten-dimension table
| # | Dimension | Finding |
|---|---|---|
| 1 | Happy path | Validated leave -> entries on internal project (VDR-U16-C395, VDR-U16-C397). |
| 2 | Reversal / cancel / negative | Refuse, cancel, delete and zero days remove entries (VDR-U16-C399, VDR-U16-C400, VDR-U16-C401, VDR-U16-C429). |
| 3 | Multi-company / data scope | Per-company internal project and task (VDR-U16-C408); report company rule (VDR-U16-C412). |
| 4 | Side effects & cross-module | Cost on internal project (VDR-U16-C409); SMS messages (VDR-U16-C414); tasks from email (VDR-U16-C420). |
| 5 | Configuration & optionality | Needs internal project and time-off task (VDR-U16-C396, VDR-U16-C408); SMS template per stage (VDR-U16-C415). |
| 6 | Validation & constraints | No manual edit/delete of leave entries (VDR-U16-C402, VDR-U16-C403, VDR-U16-C404). |
| 7 | Roles & permissions | Report rules (VDR-U16-C412, VDR-U16-C413); SMS template rule (VDR-U16-C417); to-do rule (VDR-U16-C426, VDR-U16-C427); leave manager ACL (VDR-U16-C428). |
| 8 | Scheduled / automated | NOT APPLICABLE (event driven). |
| 9 | Exception & failure | SMS delivery and add-in auth unverified (VDR-U16-C418, VDR-U16-C422). |
| 10 | Accounting / audit / compliance | Time-off cost inflates internal project cost (VDR-U16-C409); SMS/add-in/skills/to-do have no accounting effect (NOT APPLICABLE). |

### DB reconciliation (configuration only)
OBSERVATION: VDR-U16-C413, VDR-U16-C427, VDR-U16-C428; project_sms 1 ACL + 1 rule, project_timesheet_holidays 1 ACL, project_todo 4 ACL + 1 rule, hr_timesheet_attendance 1 ACL + 4 rules, all equal to source.

### Unknown / Runtime list
- RT: SMS gateway (VDR-U16-C418); add-in authentication (VDR-U16-C422).

## DB reconciliation - configuration rows seeded by the owned modules (source vs restored DB)
Counts are owned records only (identifiers with a foreign module prefix excluded). Source counts parsed from ACL CSV and record declarations (demo and tests excluded); DB counts from the module-data table of the restored database. `rules(foreign)` are rules this module rewrites in another module.

| Module | installed | ACL src | ACL db | Rules src | Rules db | Groups src | Groups db | Cron src | Cron db | Automation src | Automation db | rules(foreign) | B01 declared ids / db ids | B01 new models src / db |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| project | installed | 56 | 56 | 31 | 31 | 6 | 6 | 1 | 1 | 0 | 0 | 0 | 380 / 399 | 20 / 29 |
| project_account | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 9 / 9 | 0 / 1 |
| project_purchase | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 / 3 | 0 / 3 |
| project_purchase_stock | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | 0 / 2 |
| project_stock | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 7 / 7 | 0 / 2 |
| project_stock_account | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 / 1 | 0 / 5 |
| project_stock_landed_costs | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | 0 / 1 |
| project_hr_expense | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 / 2 | 0 / 2 |
| project_sale_expense | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | 0 / 3 |
| project_todo | installed | 4 | 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 24 / 24 | 1 / 3 |
| project_sms | installed | 1 | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 10 / 10 | 0 / 4 |
| project_mail_plugin | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 / 1 | 0 / 0 |
| project_hr_skills | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 / 1 | 0 / 3 |
| project_timesheet_holidays | installed | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 3 / 3 | 0 / 7 |
| hr_timesheet | installed | 8 | 8 | 9 | 9 | 3 | 3 | 0 | 0 | 0 | 0 | 0 | 145 / 155 | 3 / 17 |
| hr_timesheet_attendance | installed | 1 | 1 | 4 | 4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 12 / 12 | 1 / 2 |
| hr_expense | installed | 14 | 14 | 12 | 12 | 3 | 3 | 1 | 1 | 0 | 0 | 0 | 118 / 125 | 6 / 22 |
| sale_expense | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 8 / 8 | 0 / 7 |
| sale_timesheet | installed | 2 | 2 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 2 | 82 / 83 | 1 / 16 |
| sale_timesheet_margin | installed | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 / 0 | 0 / 1 |
| sale_project | installed | 4 | 4 | 1 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 55 / 55 | 0 / 16 |

Result: source-declared owned ACL/rule/group/cron/automation counts equal the restored DB counts for every owned module. `base_automation` is empty in the DB. Cross-module overrides declared by owned modules: `hr_timesheet` adds implied group `hr_timesheet.group_hr_timesheet_approver` to `project.group_project_manager` (VDR-U16-C237); `sale_timesheet` rewrites the domains of `account.account_analytic_line_rule_readonly_user` and `account.account_analytic_line_rule_billing_user` (VDR-U16-C240); `sale_timesheet` data implies `uom.group_uom` for all users.
Other DB observations (config only): the milestone and analytic-accounting feature groups are not held by the superuser closure (VDR-U16-C252, VDR-U16-C394); 6 expense products seeded (VDR-U16-C036); one expense journal set on the company (VDR-U16-C132); internal project, time-off task and hour units set (VDR-U16-C228, VDR-U16-C230); zero analytic applicability rows; payment-method lines: 3 in total.

## Consolidated Unknown / RT list
- UNKNOWN: automatic receipt reading, card feeds, payroll reimbursement (modules absent); Thai tax effect on expense lines; approval/lock of time entries (not in Community); template duplication details.
- RT: mail gateway and reminder email delivery; SMS gateway; mail add-in authentication; clearing of entry link on expense (bundled test asserts it); partial credit notes on timesheet invoices; reversal of already-invoiced expense lines; billing-accountant visibility; outstanding-account auto-creation; foreign currency conversion differences in profitability.

## NEUTRAL-REF TO CLAIM INDEX
- N-U16-001: VDR-U16-C001, VDR-U16-C002
- N-U16-002: VDR-U16-C016, VDR-U16-C022
- N-U16-003: VDR-U16-C430
- N-U16-004: VDR-U16-C003, VDR-U16-C033, VDR-U16-C034
- N-U16-005: VDR-U16-C005, VDR-U16-C006
- N-U16-006: VDR-U16-C007, VDR-U16-C008
- N-U16-007: VDR-U16-C009, VDR-U16-C010
- N-U16-008: VDR-U16-C011, VDR-U16-C012
- N-U16-009: VDR-U16-C014, VDR-U16-C015
- N-U16-010: VDR-U16-C024, VDR-U16-C025, VDR-U16-C026, VDR-U16-C027
- N-U16-011: VDR-U16-C028, VDR-U16-C029
- N-U16-012: VDR-U16-C030
- N-U16-013: VDR-U16-C031, VDR-U16-C032
- N-U16-014: VDR-U16-C431
- N-U16-015: VDR-U16-C017, VDR-U16-C018, VDR-U16-C020, VDR-U16-C021, VDR-U16-C043
- N-U16-016: VDR-U16-C035, VDR-U16-C036
- N-U16-017: VDR-U16-C039, VDR-U16-C040
- N-U16-018: VDR-U16-C013
- N-U16-019: VDR-U16-C023, VDR-U16-C037
- N-U16-020: VDR-U16-C038
- N-U16-021: VDR-U16-C044
- N-U16-022: VDR-U16-C004, VDR-U16-C019
- N-U16-023: VDR-U16-C041
- N-U16-024: VDR-U16-C042
- N-U16-025: VDR-U16-C050, VDR-U16-C056
- N-U16-026: VDR-U16-C071, VDR-U16-C072, VDR-U16-C073, VDR-U16-C088
- N-U16-027: VDR-U16-C432
- N-U16-028: VDR-U16-C045, VDR-U16-C048, VDR-U16-C049
- N-U16-029: VDR-U16-C053, VDR-U16-C054
- N-U16-030: VDR-U16-C051, VDR-U16-C052
- N-U16-031: VDR-U16-C059, VDR-U16-C060, VDR-U16-C061
- N-U16-032: VDR-U16-C055
- N-U16-033: VDR-U16-C057, VDR-U16-C058
- N-U16-034: VDR-U16-C062, VDR-U16-C063, VDR-U16-C064, VDR-U16-C065, VDR-U16-C066
- N-U16-035: VDR-U16-C067, VDR-U16-C069
- N-U16-036: VDR-U16-C046, VDR-U16-C047
- N-U16-037: VDR-U16-C074
- N-U16-038: VDR-U16-C433
- N-U16-039: VDR-U16-C079, VDR-U16-C080
- N-U16-040: VDR-U16-C070, VDR-U16-C077, VDR-U16-C081, VDR-U16-C082, VDR-U16-C083, VDR-U16-C086
- N-U16-041: VDR-U16-C078
- N-U16-042: VDR-U16-C085
- N-U16-043: VDR-U16-C434
- N-U16-044: VDR-U16-C090
- N-U16-045: VDR-U16-C068
- N-U16-046: VDR-U16-C087
- N-U16-047: VDR-U16-C084, VDR-U16-C089
- N-U16-048: VDR-U16-C075, VDR-U16-C076
- N-U16-049: VDR-U16-C092, VDR-U16-C095, VDR-U16-C103
- N-U16-050: VDR-U16-C102
- N-U16-051: VDR-U16-C435
- N-U16-052: VDR-U16-C091
- N-U16-053: VDR-U16-C093
- N-U16-054: VDR-U16-C099, VDR-U16-C100, VDR-U16-C101, VDR-U16-C104, VDR-U16-C106, VDR-U16-C107, VDR-U16-C109
- N-U16-055: VDR-U16-C096, VDR-U16-C097
- N-U16-056: VDR-U16-C110
- N-U16-057: VDR-U16-C111, VDR-U16-C113, VDR-U16-C114, VDR-U16-C129
- N-U16-058: VDR-U16-C108, VDR-U16-C121, VDR-U16-C122, VDR-U16-C123, VDR-U16-C133, VDR-U16-C134
- N-U16-059: VDR-U16-C117, VDR-U16-C118, VDR-U16-C119, VDR-U16-C120
- N-U16-060: VDR-U16-C094
- N-U16-061: VDR-U16-C436
- N-U16-062: VDR-U16-C131
- N-U16-063: VDR-U16-C132
- N-U16-064: VDR-U16-C130
- N-U16-065: VDR-U16-C135
- N-U16-066: VDR-U16-C138
- N-U16-067: VDR-U16-C112
- N-U16-068: VDR-U16-C126, VDR-U16-C127
- N-U16-069: VDR-U16-C128
- N-U16-070: VDR-U16-C098
- N-U16-071: VDR-U16-C124, VDR-U16-C125
- N-U16-072: VDR-U16-C105
- N-U16-073: VDR-U16-C115
- N-U16-074: VDR-U16-C136
- N-U16-075: VDR-U16-C137
- N-U16-076: VDR-U16-C116
- N-U16-077: VDR-U16-C146
- N-U16-078: VDR-U16-C155
- N-U16-079: VDR-U16-C437
- N-U16-080: VDR-U16-C140, VDR-U16-C141, VDR-U16-C145
- N-U16-081: VDR-U16-C143, VDR-U16-C144
- N-U16-082: VDR-U16-C147
- N-U16-083: VDR-U16-C148
- N-U16-084: VDR-U16-C151, VDR-U16-C152, VDR-U16-C153
- N-U16-085: VDR-U16-C156, VDR-U16-C157
- N-U16-086: VDR-U16-C139
- N-U16-087: VDR-U16-C159
- N-U16-088: VDR-U16-C160
- N-U16-089: VDR-U16-C438
- N-U16-090: VDR-U16-C149, VDR-U16-C150
- N-U16-091: VDR-U16-C142
- N-U16-092: VDR-U16-C158
- N-U16-093: VDR-U16-C161, VDR-U16-C162, VDR-U16-C163
- N-U16-094: VDR-U16-C154
- N-U16-095: VDR-U16-C164, VDR-U16-C165
- N-U16-096: VDR-U16-C173, VDR-U16-C174, VDR-U16-C175
- N-U16-097: VDR-U16-C439
- N-U16-098: VDR-U16-C166, VDR-U16-C167, VDR-U16-C172, VDR-U16-C195
- N-U16-099: VDR-U16-C168, VDR-U16-C169, VDR-U16-C199, VDR-U16-C200, VDR-U16-C201
- N-U16-100: VDR-U16-C176, VDR-U16-C177, VDR-U16-C178
- N-U16-101: VDR-U16-C179, VDR-U16-C180
- N-U16-102: VDR-U16-C181, VDR-U16-C183, VDR-U16-C184, VDR-U16-C185, VDR-U16-C186, VDR-U16-C198
- N-U16-103: VDR-U16-C187, VDR-U16-C188
- N-U16-104: VDR-U16-C189, VDR-U16-C190
- N-U16-105: VDR-U16-C170, VDR-U16-C171
- N-U16-106: VDR-U16-C192
- N-U16-107: VDR-U16-C196, VDR-U16-C197
- N-U16-108: VDR-U16-C194
- N-U16-109: VDR-U16-C440
- N-U16-110: VDR-U16-C193
- N-U16-111: VDR-U16-C182
- N-U16-112: VDR-U16-C203
- N-U16-113: VDR-U16-C191, VDR-U16-C202
- N-U16-114: VDR-U16-C204, VDR-U16-C232
- N-U16-115: VDR-U16-C205, VDR-U16-C219, VDR-U16-C243
- N-U16-116: VDR-U16-C441
- N-U16-117: VDR-U16-C206, VDR-U16-C207
- N-U16-118: VDR-U16-C209, VDR-U16-C210
- N-U16-119: VDR-U16-C208
- N-U16-120: VDR-U16-C212, VDR-U16-C213, VDR-U16-C214
- N-U16-121: VDR-U16-C216
- N-U16-122: VDR-U16-C220, VDR-U16-C221, VDR-U16-C222, VDR-U16-C223
- N-U16-123: VDR-U16-C217, VDR-U16-C218
- N-U16-124: VDR-U16-C211
- N-U16-125: VDR-U16-C224, VDR-U16-C225, VDR-U16-C226
- N-U16-126: VDR-U16-C227, VDR-U16-C228
- N-U16-127: VDR-U16-C246
- N-U16-128: VDR-U16-C229, VDR-U16-C230, VDR-U16-C231
- N-U16-129: VDR-U16-C442
- N-U16-130: VDR-U16-C233, VDR-U16-C234, VDR-U16-C235, VDR-U16-C236, VDR-U16-C237, VDR-U16-C238, VDR-U16-C244
- N-U16-131: VDR-U16-C242
- N-U16-132: VDR-U16-C215, VDR-U16-C247
- N-U16-133: VDR-U16-C245
- N-U16-134: VDR-U16-C240, VDR-U16-C241
- N-U16-135: VDR-U16-C249
- N-U16-136: VDR-U16-C248
- N-U16-137: VDR-U16-C239
- N-U16-138: VDR-U16-C250, VDR-U16-C251
- N-U16-139: VDR-U16-C253, VDR-U16-C254
- N-U16-140: VDR-U16-C276, VDR-U16-C278
- N-U16-141: VDR-U16-C443
- N-U16-142: VDR-U16-C257, VDR-U16-C258, VDR-U16-C259, VDR-U16-C290, VDR-U16-C295
- N-U16-143: VDR-U16-C260, VDR-U16-C261, VDR-U16-C294
- N-U16-144: VDR-U16-C263, VDR-U16-C264, VDR-U16-C265, VDR-U16-C266
- N-U16-145: VDR-U16-C270, VDR-U16-C271
- N-U16-146: VDR-U16-C273, VDR-U16-C274, VDR-U16-C275
- N-U16-147: VDR-U16-C267, VDR-U16-C268
- N-U16-148: VDR-U16-C252, VDR-U16-C256
- N-U16-149: VDR-U16-C285, VDR-U16-C286, VDR-U16-C287, VDR-U16-C288
- N-U16-150: VDR-U16-C279, VDR-U16-C280, VDR-U16-C281
- N-U16-151: VDR-U16-C282, VDR-U16-C284
- N-U16-152: VDR-U16-C444
- N-U16-153: VDR-U16-C277, VDR-U16-C283, VDR-U16-C293
- N-U16-154: VDR-U16-C445
- N-U16-155: VDR-U16-C289, VDR-U16-C292
- N-U16-156: VDR-U16-C291
- N-U16-157: VDR-U16-C262
- N-U16-158: VDR-U16-C272
- N-U16-159: VDR-U16-C269
- N-U16-160: VDR-U16-C296
- N-U16-161: VDR-U16-C255
- N-U16-162: VDR-U16-C297, VDR-U16-C331
- N-U16-163: VDR-U16-C332, VDR-U16-C333
- N-U16-164: VDR-U16-C317, VDR-U16-C318, VDR-U16-C319
- N-U16-165: VDR-U16-C446
- N-U16-166: VDR-U16-C299, VDR-U16-C300, VDR-U16-C306, VDR-U16-C313, VDR-U16-C334
- N-U16-167: VDR-U16-C301
- N-U16-168: VDR-U16-C302
- N-U16-169: VDR-U16-C303, VDR-U16-C304, VDR-U16-C305
- N-U16-170: VDR-U16-C308, VDR-U16-C310
- N-U16-171: VDR-U16-C311
- N-U16-172: VDR-U16-C312
- N-U16-173: VDR-U16-C309
- N-U16-174: VDR-U16-C314
- N-U16-175: VDR-U16-C315
- N-U16-176: VDR-U16-C316
- N-U16-177: VDR-U16-C324, VDR-U16-C325
- N-U16-178: VDR-U16-C307, VDR-U16-C326
- N-U16-179: VDR-U16-C298
- N-U16-180: VDR-U16-C447
- N-U16-181: VDR-U16-C320, VDR-U16-C321
- N-U16-182: VDR-U16-C327
- N-U16-183: VDR-U16-C322, VDR-U16-C323
- N-U16-184: VDR-U16-C328
- N-U16-185: VDR-U16-C329
- N-U16-186: VDR-U16-C330
- N-U16-187: VDR-U16-C335, VDR-U16-C338, VDR-U16-C340
- N-U16-188: VDR-U16-C373
- N-U16-189: VDR-U16-C448
- N-U16-190: VDR-U16-C341, VDR-U16-C342, VDR-U16-C344, VDR-U16-C345
- N-U16-191: VDR-U16-C343
- N-U16-192: VDR-U16-C346
- N-U16-193: VDR-U16-C355
- N-U16-194: VDR-U16-C349, VDR-U16-C350, VDR-U16-C356
- N-U16-195: VDR-U16-C377, VDR-U16-C378, VDR-U16-C379, VDR-U16-C380, VDR-U16-C381, VDR-U16-C382
- N-U16-196: VDR-U16-C383, VDR-U16-C384, VDR-U16-C385
- N-U16-197: VDR-U16-C351, VDR-U16-C352, VDR-U16-C353, VDR-U16-C386
- N-U16-198: VDR-U16-C361, VDR-U16-C362, VDR-U16-C363, VDR-U16-C364, VDR-U16-C365, VDR-U16-C370, VDR-U16-C371
- N-U16-199: VDR-U16-C368, VDR-U16-C369, VDR-U16-C372
- N-U16-200: VDR-U16-C375, VDR-U16-C376
- N-U16-201: VDR-U16-C357, VDR-U16-C358, VDR-U16-C359, VDR-U16-C360
- N-U16-202: VDR-U16-C366, VDR-U16-C367
- N-U16-203: VDR-U16-C392
- N-U16-204: VDR-U16-C339, VDR-U16-C394
- N-U16-205: VDR-U16-C393
- N-U16-206: VDR-U16-C336, VDR-U16-C337, VDR-U16-C388, VDR-U16-C389
- N-U16-207: VDR-U16-C347, VDR-U16-C348
- N-U16-208: VDR-U16-C374, VDR-U16-C387
- N-U16-209: VDR-U16-C354
- N-U16-210: VDR-U16-C390
- N-U16-211: VDR-U16-C391
- N-U16-212: VDR-U16-C395
- N-U16-213: VDR-U16-C410, VDR-U16-C411
- N-U16-214: VDR-U16-C423
- N-U16-215: VDR-U16-C449
- N-U16-216: VDR-U16-C396, VDR-U16-C397, VDR-U16-C398
- N-U16-217: VDR-U16-C399, VDR-U16-C400, VDR-U16-C401, VDR-U16-C402
- N-U16-218: VDR-U16-C403, VDR-U16-C405, VDR-U16-C406, VDR-U16-C407
- N-U16-219: VDR-U16-C404
- N-U16-220: VDR-U16-C414, VDR-U16-C415
- N-U16-221: VDR-U16-C420, VDR-U16-C421
- N-U16-222: VDR-U16-C424, VDR-U16-C425
- N-U16-223: VDR-U16-C426, VDR-U16-C427
- N-U16-224: VDR-U16-C429
- N-U16-225: VDR-U16-C408
- N-U16-226: VDR-U16-C428
- N-U16-227: VDR-U16-C412, VDR-U16-C413
- N-U16-228: VDR-U16-C417
- N-U16-229: VDR-U16-C409
- N-U16-230: VDR-U16-C419
- N-U16-231: VDR-U16-C416
- N-U16-232: VDR-U16-C418
- N-U16-233: VDR-U16-C422

## CLAIMS TABLE
| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U16-C001 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:44 | mail.activity.mixin | FACT | always | — | hr.expense is a standalone model with chatter, activities and analytic distribution; the file defines no report or sheet header model. | N-U16-001 |
| VDR-U16-C002 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:282 | Legacy sheet field | FACT | always | CONTRA | former_sheet_id is an integer kept only as legacy data; there is no expense report object in this revision, which contradicts any terminology that assumes submit/approve works on reports. | N-U16-001 |
| VDR-U16-C003 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:102 | can_be_expensed | FACT | always | — | The Category field on an expense is the product and only products with can_be_expensed are selectable. | N-U16-004 |
| VDR-U16-C004 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:96 | without product via mail alias | FACT | always | — | product_id is not a required column so that a mail-created expense can exist without a category; the form requires it and submission raises an error without one. | N-U16-022 |
| VDR-U16-C005 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:496 | _compute_total_amount_currency | FACT | product has non-zero standard price | — | For expenses whose product has a cost, total_amount_currency is computed as price_unit times quantity with the tax-included total from the tax engine. | N-U16-005 |
| VDR-U16-C006 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:652 | _price_compute | FACT | product has cost and state draft | — | price_unit is read from the product standard_price (converted to the expense unit) while the expense is a draft and the product has a cost; otherwise it is total divided by quantity. | N-U16-005 |
| VDR-U16-C007 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:274 | price-included taxes for expenses | FACT | always | — | Field help states that every tax on an expense behaves as price-included. | N-U16-006 |
| VDR-U16-C008 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1742 | total_included | FACT | always | — | The base line prepared for tax computation forces special_mode total_included so the tax engine extracts tax from the total. | N-U16-006 |
| VDR-U16-C009 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:575 | supplier_taxes_id | FACT | category selected | — | Default taxes are the category's vendor taxes limited to the expense company. | N-U16-007 |
| VDR-U16-C010 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:684 | expense_account_id | FACT | no category | — | Without a category the expense account defaults to the company expense account; with a category it is the product or category expense account. | N-U16-007 |
| VDR-U16-C011 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:394 | _get_conversion_rate | FACT | foreign currency | — | The conversion rate to company currency is read at the expense date through the currency conversion helper. | N-U16-008 |
| VDR-U16-C012 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:549 | custom rate on the expense | FACT | foreign currency | — | Writing total_amount (company currency) through its inverse recomputes tax amounts and stores a derived currency_rate, giving the user a custom rate. | N-U16-008 |
| VDR-U16-C013 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:296 | can have a total of 0 | FACT | state not draft or approval_state set | — | Constraint rejects zero totals once the expense is submitted or in any later state. | N-U16-018 |
| VDR-U16-C014 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:730 | he.date = ex.date | FACT | employee, category and amount set | — | Duplicate detection is raw SQL grouping on employee, product, date, total in currency, company and currency with more than one match. | N-U16-009 |
| VDR-U16-C015 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:706 | checksum | FACT | expense has attachments and is not a split part | — | Shared-receipt detection compares attachment checksums across hr.expense attachments and excludes splits of the same origin. | N-U16-009 |
| VDR-U16-C016 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1078 | def message_new | FACT | mail gateway alias on this model | RT | message_new resolves the employee from the sender address, parses category code and price from the subject and creates the expense with company, currency, taxes and expense account; behaviour of the gateway itself is runtime. | N-U16-002 |
| VDR-U16-C017 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:860 | work_email | FACT | mail gateway | — | The sender is matched on employee work email or linked user email using a case-insensitive pattern; if several employees match, the one in the user's own company is kept. | N-U16-015 |
| VDR-U16-C018 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1083 | super().message_new | FACT | sender not matched to an employee | — | When no employee matches the sender the default mail-thread creation is used and the expense carries no employee data from the message. | N-U16-015 |
| VDR-U16-C019 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:885 | default_code | FACT | mail subject | — | The category is found by treating the first word of the subject as the product internal reference, case-insensitively, among expensable products. | N-U16-022 |
| VDR-U16-C020 | FUNCTION MAPPING REQUIRED | hr_expense/data/hr_expense_data.xml:85 | use_mailgateway | OBSERVATION | DB: parameter hr_expense.use_mailgateway = True | — | The module data sets use_mailgateway true; the restored database holds hr_expense.use_mailgateway = True in system parameters. | N-U16-015 |
| VDR-U16-C021 | FUNCTION MAPPING REQUIRED | hr_expense/data/mail_alias_data.xml:6 | alias_name | FACT | always (noupdate) | — | Default alias name is expense with alias_contact employees, bound to the hr.expense model. | N-U16-015 |
| VDR-U16-C022 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1255 | EXP_GEN | FACT | upload of receipt files | — | Uploading receipts creates one expense per file with the generic category EXP_GEN (or the first expensable product), price 0 and name Untitled Expense. | N-U16-002 |
| VDR-U16-C023 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1257 | at least one category | FACT | upload of receipt files | — | Receipt upload fails with a user error if no expensable category exists. | N-U16-019 |
| VDR-U16-C024 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1488 | half_price | FACT | split wizard | — | Default split halves the amount, rounding one half up and one down so the two parts sum to the original. | N-U16-010 |
| VDR-U16-C025 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_split_wizard.py:42 | compare_amounts | FACT | split wizard | — | split_possible is true only when the sum of split amounts equals the original amount in expense currency. | N-U16-010 |
| VDR-U16-C026 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_split_wizard.py:63 | from_split_wizard | FACT | split wizard | — | Each copied split expense gets a copy of every attachment of the original. | N-U16-010 |
| VDR-U16-C027 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1329 | already posted | FACT | state posted, in_payment or paid | — | Splitting is refused for posted and later states. | N-U16-010 |
| VDR-U16-C028 | FUNCTION MAPPING REQUIRED | hr_expense/models/ir_attachment.py:28 | once it has been approved | FACT | always | — | Attachment creation on hr.expense is allowed only in draft or submitted state for users with write access or the owning employee, or in superuser mode. | N-U16-011 |
| VDR-U16-C029 | FUNCTION MAPPING REQUIRED | hr_expense/models/ir_attachment.py:18 | once it has been submitted | FACT | always | — | Deletion is allowed only while the expense is draft or submitted and the user can write it. | N-U16-011 |
| VDR-U16-C030 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:810 | delete a posted or approved | FACT | state approved, posted, in_payment or paid | — | Deletion is blocked for approved, posted, in-payment and paid expenses. | N-U16-012 |
| VDR-U16-C031 | FUNCTION MAPPING REQUIRED | hr_expense/models/product_product.py:47 | standard_price | FACT | category cost edited | — | Writing standard_price on a product rewrites price_unit on all its draft expenses of the current company, and resets quantity to 1 if the cost becomes zero. | N-U16-013 |
| VDR-U16-C032 | FUNCTION MAPPING REQUIRED | hr_expense/models/product_product.py:24 | Updating the category cost | FACT | draft expenses exist | — | The product form warns when draft expenses exist for that category. | N-U16-013 |
| VDR-U16-C033 | FUNCTION MAPPING REQUIRED | hr_expense/models/product_template.py:35 | can_be_expensed | FACT | always | — | The expensable flag is forced off for combo products and for products that cannot be purchased. | N-U16-004 |
| VDR-U16-C034 | FUNCTION MAPPING REQUIRED | hr_expense/models/product_template.py:41 | purchase_ok | FACT | can_be_expensed is true | — | Setting can_be_expensed switches purchase_ok on for the product. | N-U16-004 |
| VDR-U16-C035 | FUNCTION MAPPING REQUIRED | hr_expense/data/hr_expense_data.xml:35 | expense_product_mileage | FACT | noupdate data | — | Six expense products are seeded (meal, travel and accommodation, mileage, gift, communication, generic EXP_GEN); mileage has standard_price 1.0 and unit km. | N-U16-016 |
| VDR-U16-C036 | FUNCTION MAPPING REQUIRED | hr_expense/data/hr_expense_data.xml:77 | EXP_GEN | OBSERVATION | DB: restored database | — | The restored database contains the six expense products, all of type service, flagged expensable and purchasable; mileage has cost 1.0 per km, the others have no company cost value. | N-U16-016 |
| VDR-U16-C037 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:54 | no related employee | FACT | creating an expense | — | Default employee is the user's employee; if none and the user is not a team approver the creation raises a validation error. | N-U16-019 |
| VDR-U16-C038 | FUNCTION MAPPING REQUIRED | hr_expense/security/ir.model.access.csv:2 | access_hr_expense_employee | FACT | always | — | base.group_user holds read, write, create and unlink ACL on hr.expense; record rules (CAP-U16-02) restrict rows. Team approver and manager groups have the same four rights; accountants (account.group_account_invoice) have read, write, create. | N-U16-020 |
| VDR-U16-C039 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_employee.py:40 | company_id | FACT | user in All Approver group | — | The employee picker accepts every employee of the root company tree for All Approver users; team approvers see their reports and department; others see only themselves. | N-U16-017 |
| VDR-U16-C040 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:753 | account_prefix | FACT | analytic distribution model rules exist | — | Analytic distribution defaults come from the distribution models using product, category, employee work contact, account code prefix and company. | N-U16-017 |
| VDR-U16-C041 | FUNCTION MAPPING REQUIRED | hr_expense/models/res_config_settings.py:20 | module_hr_expense_extract | UNKNOWN | module not in Community tree | — | Setting toggles for OCR (module_hr_expense_extract), card issuing (module_hr_expense_stripe) and payroll reimbursement (module_hr_payroll_expense) point to modules that are not present under odoo/addons in this revision; behaviour unknown. | N-U16-023 |
| VDR-U16-C042 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:960 | email_to | FACT | email capture, employee without linked user | RT | A confirmation email is sent through mail.mail to the original sender when the employee has no user; with a user a chatter note is posted instead. Delivery requires a working mail server. | N-U16-024 |
| VDR-U16-C043 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:866 | e.company_id == e.user_id.company_id | FACT | email matches several employees | — | When several employees share the sender address the employee whose company equals the user's company is chosen. | N-U16-015 |
| VDR-U16-C044 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1318 | action_approve_duplicates | FACT | approver confirms duplicate dialog | — | Confirming that expenses are not duplicates posts a note to each related expense through the root partner; it does not block or mark anything else. | N-U16-021 |
| VDR-U16-C045 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:37 | Billing accountant | FACT | always | — | The class docstring declares the rights matrix: employees submit their own, officers submit/approve/cancel only for their reports and never their own, managers always, billing accountants post approved expenses. | N-U16-028 |
| VDR-U16-C046 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:18 | Submitted | FACT | always | — | state selection is draft, submitted, approved, posted, in_payment, paid, refused and is computed and stored; approval_state selection is submitted, approved, refused. | N-U16-036 |
| VDR-U16-C047 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:487 | approval_state or 'draft' | FACT | no linked journal entry | — | Without a linked entry the state equals approval_state or draft; a linked entry overrides it (see CAP-U16-04). | N-U16-036 |
| VDR-U16-C048 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1131 | can_approve | FACT | action_submit | — | Submission by someone other than the expense employee requires can_approve; otherwise a user error is raised. | N-U16-028 |
| VDR-U16-C049 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1134 | without a category | FACT | action_submit | — | Submission raises when product_id is empty. | N-U16-028 |
| VDR-U16-C050 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1138 | approval_state = 'submitted' | FACT | action_submit | — | Non auto-validated expenses get approval_state submitted; auto-validated ones go directly to _do_approve with validate_analytic context. | N-U16-025 |
| VDR-U16-C051 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1146 | _can_be_autovalidated | FACT | action_submit | — | An expense is auto-validated when it has no manager and the employee has no expense approver, or when the manager is the employee's own user. | N-U16-030 |
| VDR-U16-C052 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1139 | bypass the duplicate check | FACT | auto-approved expense | — | A source comment states auto-approval bypasses the duplicate check. | N-U16-030 |
| VDR-U16-C053 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1516 | department_manager | FACT | action_submit when manager empty | — | Default responsible: employee expense_manager_id (excluding self), then department manager user if in the team-approver group, then the parent manager's user. | N-U16-029 |
| VDR-U16-C054 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1520 | employee_team_leader | FACT | no expense manager and no valid department manager | — | The parent (direct manager) user is returned without a group check. | N-U16-029 |
| VDR-U16-C055 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1453 | business_domain='expense' | FACT | _do_approve | — | Approval validates the analytic distribution against mandatory plans for business domain expense (account, product, company passed). | N-U16-032 |
| VDR-U16-C056 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1458 | manager_id | FACT | _do_approve | — | Approval writes approval_state approved, sets manager_id to the approving user and stamps approval_date. | N-U16-025 |
| VDR-U16-C057 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1151 | duplicate_expense_ids.filtered | FACT | action_approve | — | If duplicates exist in an active state, action_approve returns the duplicate-confirmation wizard instead of approving. | N-U16-033 |
| VDR-U16-C058 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_approve_duplicate.py:29 | Duplicate Expense | FACT | duplicate wizard refuse | — | The duplicate wizard can refuse the listed submitted expenses with the fixed reason Duplicate Expense, or approve them. | N-U16-033 |
| VDR-U16-C059 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1422 | own expense | FACT | approver is not HR administrator | — | An approver who is not an expense administrator cannot approve an expense whose employee is their own user; reasons also cover other companies and non-department expenses. | N-U16-031 |
| VDR-U16-C060 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1406 | neither a Manager nor | FACT | approver outside company scope | — | Approval is refused when the expense company is not among the user's allowed companies. | N-U16-031 |
| VDR-U16-C061 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:827 | _check_can_approve() | FACT | write of state or approval_state to approved | — | Writing approved re-checks approver rights unless the expense is auto-approved (no manager other than the employee and no expense approver). | N-U16-031 |
| VDR-U16-C062 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1161 | hr_expense_refuse_wizard_action | FACT | action_refuse | — | Refusal opens a wizard that requires a reason; the wizard then calls _do_refuse with the reason. | N-U16-034 |
| VDR-U16-C063 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_refuse_reason.py:12 | required=True | FACT | refuse wizard | — | The refusal reason is a required char field. | N-U16-034 |
| VDR-U16-C064 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1471 | linked to a posted journal entry | FACT | _do_refuse | — | Refusal raises if any linked journal entry is not draft. | N-U16-034 |
| VDR-U16-C065 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1474 | lingering moves | FACT | _do_refuse with draft entries | — | Draft entries linked to the expense are deleted when it is refused. | N-U16-034 |
| VDR-U16-C066 | FUNCTION MAPPING REQUIRED | hr_expense/views/hr_expense_views.xml:119 | submitted | FACT | form | — | The Refuse button is visible in submitted and approved states to team approvers. | N-U16-034 |
| VDR-U16-C067 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1438 | reset to draft an expense | FACT | action_reset | — | Reset is refused if any linked entry is not in draft or absent. | N-U16-035 |
| VDR-U16-C068 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1211 | _reverse_moves | INFERENCE | action_reset | — | action_reset calls _reverse_moves on non-draft moves, but _check_can_reset_approval (line cited in claim c02_resetcheck) already refuses any non-draft linked move, so the reversal branch is unreachable through the normal path. | N-U16-045 |
| VDR-U16-C069 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1464 | 'account_move_id': False | FACT | _do_reset_approval | — | Reset clears approval_state, approval_date and the entry link. | N-U16-035 |
| VDR-U16-C070 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:791 | employee_id.user_id == user | FACT | can_reset | — | can_reset is true for All Approver/Administrator users, for the expense approver chain, or for the owning employee while draft or submitted. | N-U16-040 |
| VDR-U16-C071 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1009 | mail_act_expense_approval | FACT | state submitted | — | On submission an Expense Approval activity is scheduled for the manager, else the default responsible, else the current user. | N-U16-026 |
| VDR-U16-C072 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1022 | activity_feedback | FACT | state approved | — | The activity is marked done when approved and unlinked when the expense returns to draft or is refused. | N-U16-026 |
| VDR-U16-C073 | FUNCTION MAPPING REQUIRED | hr_expense/data/hr_expense_cron.xml:10 | weeks | FACT | module installed | — | A scheduled action HR Expense: Send Submitted Expenses Mail runs weekly (interval 1 week) and calls _cron_send_submitted_expenses_mail. | N-U16-026 |
| VDR-U16-C074 | FUNCTION MAPPING REQUIRED | hr_expense/data/hr_expense_cron.xml:5 | Send Submitted Expenses Mail | OBSERVATION | DB: restored database | — | In the restored database this one scheduled action exists and is active with interval 1 week and a next-call value set. | N-U16-037 |
| VDR-U16-C075 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1071 | mail.mail | FACT | cron run with submitted expenses | RT | The cron groups submitted expenses per company and manager and sends one email per manager; sender is the current user, else the company email, else a parent company email; if none exists a warning is logged and nothing is sent. | N-U16-048 |
| VDR-U16-C076 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1029 | parse_version('2.1') | INFERENCE | manifest version 2.1 | — | update_activities_and_mails also sends the reminder mail inline only when the installed module version is below 2.1; the manifest version is 2.1, so with this revision the inline mail branch is not taken. | N-U16-048 |
| VDR-U16-C077 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:356 | edit their own draft expense | FACT | always | — | is_editable: administrators always; own expense only in draft; approvers and designated managers for others' expenses; nobody when state is not draft, submitted or approved (except superuser). | N-U16-040 |
| VDR-U16-C078 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:816 | analytic_distribution | FACT | write | — | Writing taxes, analytic distribution, account or manager requires is_editable or superuser, else a user error. | N-U16-041 |
| VDR-U16-C079 | FUNCTION MAPPING REQUIRED | hr_expense/security/hr_expense_security.xml:23 | group_hr_expense_manager | FACT | always | — | Three groups: Team Approver (implies base user), All Approver (implies Team Approver), Administrator (implies All Approver; root and admin users). | N-U16-039 |
| VDR-U16-C080 | FUNCTION MAPPING REQUIRED | hr_expense/security/hr_expense_security.xml:16 | group_hr_expense_user | OBSERVATION | DB: restored database | — | Restored DB has three expense groups, one privilege record; Administrator group has 2 member users, the other two have 0. | N-U16-039 |
| VDR-U16-C081 | FUNCTION MAPPING REQUIRED | hr_expense/security/ir_rule.xml:29 | state', '=', 'draft' | FACT | base.group_user | — | Rule Employee Expense: base users may read/write/create/delete rows where they are the employee and the state is draft, or where they are the expense approver for the employee and the state is draft, submitted, approved or refused. | N-U16-040 |
| VDR-U16-C082 | FUNCTION MAPPING REQUIRED | hr_expense/security/ir_rule.xml:35 | not in draft state | INFERENCE | base.group_user | — | This second rule has perm_create, write and unlink false so it adds read visibility only for the employee's own non-draft expenses and for approver-designated submitted/approved/refused rows. | N-U16-040 |
| VDR-U16-C083 | FUNCTION MAPPING REQUIRED | hr_expense/security/ir_rule.xml:18 | department_id.manager_id.user_id | FACT | Team Approver group | — | Team approvers see rows of own employee, their department head's reports, their hierarchy, designated approver rows and rows where they are manager. | N-U16-040 |
| VDR-U16-C084 | FUNCTION MAPPING REQUIRED | hr_expense/security/ir_rule.xml:9 | group_account_user | FACT | All Approver or accountant group | — | Rule Manager Expense gives all rows to All Approver and to account.group_account_user; billing accountants (account.group_account_invoice) are not in this rule. | N-U16-047 |
| VDR-U16-C085 | FUNCTION MAPPING REQUIRED | hr_expense/security/ir_rule.xml:51 | company_ids | FACT | global rule | — | A global rule limits hr.expense to the user's allowed companies. | N-U16-042 |
| VDR-U16-C086 | FUNCTION MAPPING REQUIRED | hr_expense/security/ir_rule.xml:4 | ir_rule_hr_expense_manager | OBSERVATION | DB: restored database | — | Restored DB: 14 ACL rows and 12 record rules are owned by hr_expense, matching the 14 CSV data rows and 12 rule records in source. | N-U16-040 |
| VDR-U16-C087 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:989 | case 'cancel' | INFERENCE | always | — | _track_subtype matches state value cancel, which is not in the state selection, so that branch never fires; refusal is tracked through the refused state change instead. | N-U16-046 |
| VDR-U16-C088 | FUNCTION MAPPING REQUIRED | hr_expense/data/mail_activity_type_data.xml:4 | mail_act_expense_approval | FACT | noupdate | — | Activity type Expense Approval is bound to hr.expense and created as noupdate data. | N-U16-026 |
| VDR-U16-C089 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | runtime | RT | Billing-accountant visibility of other employees' approved expenses given the ACL (create/read/write) but absent record-rule row needs runtime proof with a user holding only the billing role. | N-U16-047 |
| VDR-U16-C090 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1146 | employee_id.user_id | INFERENCE | action_submit | — | Because the manager equal to the employee's own user triggers auto-approval, an employee set as their own approver (or the only candidate) is never reviewed by anyone else. | N-U16-044 |
| VDR-U16-C091 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1442 | accounting entry for approved | FACT | action_post | — | _check_can_create_move refuses posting unless every selected expense is in state approved, and refuses an unset payment_mode. | N-U16-052 |
| VDR-U16-C092 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1172 | company_account | FACT | action_post | — | action_post separates company-paid from employee-paid expenses; company-paid ones create payments immediately. | N-U16-049 |
| VDR-U16-C093 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1175 | different companies | FACT | action_post | — | Employee-paid expenses of more than one company in one action raise a user error. | N-U16-053 |
| VDR-U16-C094 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1180 | sepa_ct | FACT | company-paid expense with SEPA method | — | Posting is blocked for a company-paid expense with payment method code sepa_ct when vendor_id is empty. | N-U16-060 |
| VDR-U16-C095 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1531 | _post_wizard | FACT | employee-paid expenses | — | Employee-paid expenses open the Expense Posting Wizard; company-paid expenses are refused by this method. | N-U16-049 |
| VDR-U16-C096 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_post_wizard.py:18 | parent_ids | FACT | wizard default | — | Wizard default journal: company expense journal, else closest parent company's, else first purchase journal of the company. | N-U16-055 |
| VDR-U16-C097 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_post_wizard.py:62 | expense_journal_id | FACT | company has no default | — | If the company has no default expense journal, the one chosen in the wizard is written to the company. | N-U16-055 |
| VDR-U16-C098 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_post_wizard.py:47 | rights to create accounting entries | FACT | wizard action_post_entry | — | The wizard requires create access on account.move before building entries. | N-U16-070 |
| VDR-U16-C099 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_post_wizard.py:56 | sudo().create | FACT | wizard action_post_entry | — | Entries are created in sudo and posted immediately by moves_sudo.action_post(). | N-U16-054 |
| VDR-U16-C100 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_post_wizard.py:52 | accounting_date | FACT | wizard | — | invoice_date of the receipt is the accounting date entered in the wizard (default today). | N-U16-054 |
| VDR-U16-C101 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/hr_expense_post_wizard.py:59 | action_post | FACT | wizard | — | Receipts are posted at creation; no draft stage is offered to the user. | N-U16-054 |
| VDR-U16-C102 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1609 | grouped('employee_id') | FACT | _prepare_receipts_vals | — | Receipts are built per employee: one in_receipt move per employee with one line per expense. | N-U16-050 |
| VDR-U16-C103 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1619 | in_receipt | FACT | employee-paid | — | Employee-paid entries are vendor receipts (in_receipt). | N-U16-049 |
| VDR-U16-C104 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1620 | work_contact_id | FACT | employee-paid | — | The receipt partner is the employee's work contact; commercial_partner_id is the user partner. | N-U16-054 |
| VDR-U16-C105 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1622 | company_currency_id | INFERENCE | employee-paid | — | The receipt currency is the company currency and lines use price_unit (company currency); the original currency stays on the expense only. | N-U16-072 |
| VDR-U16-C106 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1625 | primary_bank_account_id | FACT | employee-paid | — | The receipt carries the employee's primary bank account. | N-U16-054 |
| VDR-U16-C107 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1610 | attachments_data | FACT | employee-paid and company-paid | — | All expense attachments are copied onto the receipt (or the payment's entry). | N-U16-054 |
| VDR-U16-C108 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1729 | price_unit | FACT | _prepare_move_lines_vals | — | A receipt line carries name, account, quantity, price_unit, product, unit, analytic distribution, expense_id link and taxes. | N-U16-058 |
| VDR-U16-C109 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1734 | company_account | FACT | _prepare_move_lines_vals | — | Line partner is the employee contact for employee-paid and empty for company-paid lines. | N-U16-054 |
| VDR-U16-C110 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1783 | had a look at your | FACT | no account found | — | _get_base_account falls back expense account, product account, company account, purchase journal default account, else raises. | N-U16-056 |
| VDR-U16-C111 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1805 | property_account_payable_id | FACT | employee-paid | — | The credit account is the work contact's payable account (or its parent's) in the expense company context. | N-U16-057 |
| VDR-U16-C112 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1800 | No work contact found | FACT | employee-paid | — | Missing work contact raises a user error during posting. | N-U16-067 |
| VDR-U16-C113 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1797 | payment_account_id | FACT | company-paid | — | For company-paid expenses the destination account is the method line's outstanding account, or the chart's outstanding account created if missing. | N-U16-057 |
| VDR-U16-C114 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1813 | several accounts payable | FACT | several expenses on one call | — | More than one distinct destination account in a call raises an error. | N-U16-057 |
| VDR-U16-C115 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1826 | _create_outstanding_accounts | FACT | outstanding account missing | — | If the outstanding account reference is missing the code creates outstanding accounts for the company at posting time. | N-U16-073 |
| VDR-U16-C116 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1830 | is archived | FACT | outstanding account archived | — | An archived outstanding account triggers a redirect warning to reactivate it. | N-U16-076 |
| VDR-U16-C117 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1593 | account.payment | FACT | company-paid | — | A payment record is created in sudo for each company-paid expense and linked back to the move through origin_payment_id. | N-U16-059 |
| VDR-U16-C118 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1692 | outbound | FACT | company-paid | — | Payment values: type outbound, partner type supplier, vendor as partner, expense currency and amount, selected method line. | N-U16-059 |
| VDR-U16-C119 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1636 | payment method on the journal | FACT | company-paid | — | A company-paid expense without a payment method line raises an error naming the journal. | N-U16-059 |
| VDR-U16-C120 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1193 | origin_payment_id.action_post | FACT | company-paid | — | Company-paid entries are posted through the payment's action_post so that entry and payment are posted together. | N-U16-059 |
| VDR-U16-C121 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:97 | own_account | FACT | employee-paid entries | — | For employee-paid lines the entry's tax base line uses special_mode total_included. | N-U16-058 |
| VDR-U16-C122 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move_line.py:38 | force_price_include | FACT | lines with expense_id | — | Totals of expense lines are computed with force_price_include so every tax acts as price-included. | N-U16-058 |
| VDR-U16-C123 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_tax.py:39 | expense_id | FACT | tax lines | — | Tax line grouping keys include expense_id so tax lines stay separate per expense. | N-U16-058 |
| VDR-U16-C124 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:60 | _check_journal_move_type | FACT | moves with expenses | — | Entries linked to expenses skip the journal-move-type check, so employee entries may sit in non-purchase journals. | N-U16-071 |
| VDR-U16-C125 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move_line.py:21 | _check_payable_receivable | FACT | lines of company-paid expenses | — | Payable/receivable account check is skipped for company-paid expense lines. | N-U16-071 |
| VDR-U16-C126 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:35 | distinct and dedicated journal entry | FACT | always | — | Constraint on account.move: a company-paid expense cannot share an entry with another expense. | N-U16-068 |
| VDR-U16-C127 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:302 | particular payment | FACT | always | — | Constraint on hr.expense: a payment may have at most one expense. | N-U16-068 |
| VDR-U16-C128 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_payment.py:31 | linked to an expense | FACT | write on a linked payment | — | Writing date, amount, type, partner, journal, method, memo etc. on a payment linked to an expense raises. | N-U16-069 |
| VDR-U16-C129 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_payment.py:16 | outstanding_account_id | INFERENCE | company-paid | — | The payment's outstanding account is set equal to the expense's destination account, so entry and payment share one account. | N-U16-057 |
| VDR-U16-C130 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_payment.py:22 | require_partner_bank_account | FACT | payment linked to expense | — | Payments linked to expenses never require a partner bank account. | N-U16-064 |
| VDR-U16-C131 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:668 | allowed_method_line_ids | FACT | company-paid | — | Selectable method lines are the company's configured allowed set, otherwise all active outbound method lines of the company's journals. | N-U16-062 |
| VDR-U16-C132 | FUNCTION MAPPING REQUIRED | hr_expense/models/res_company.py:9 | expense_journal_id | OBSERVATION | DB: restored database | — | The restored company row has expense_journal_id set to a purchase-type journal with code BILL; the company has an expense account configured as well. | N-U16-063 |
| VDR-U16-C133 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1548 | validate_analytic | FACT | posting wizard | — | The wizard context carries validate_analytic so the analytic mandatory-plan check also applies at posting. | N-U16-058 |
| VDR-U16-C134 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1660 | analytic_distribution | FACT | company-paid | — | Company-paid entry base lines carry the expense analytic distribution and the tax tag ids from the tax engine. | N-U16-058 |
| VDR-U16-C135 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1551 | _post_without_wizard | FACT | specific flows | — | A second posting path exists that skips the wizard, using the company expense journal or the first purchase journal and today as the date; the docstring says it should never be called except in specific flows. | N-U16-065 |
| VDR-U16-C136 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1667 | vendor_id | INFERENCE | company-paid | — | Company-paid payment and entry lines use vendor_id as partner; when empty, partner is empty (the field is only enforced for SEPA transfer). | N-U16-074 |
| VDR-U16-C137 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1649 | include_caba_tags | UNKNOWN | chart th | — | Cash-basis tax tags are included only for company-paid expenses; Thai withholding or other local tax effects on expense lines were not traced. | N-U16-075 |
| VDR-U16-C138 | FUNCTION MAPPING REQUIRED | hr_expense/data/hr_expense_sequence.xml:7 | hr.expense.invoice | FACT | noupdate | — | A sequence hr.expense.invoice with prefix EXP/ is seeded but not referenced by the entry creation code read (entries are named by the journal sequence on posting). | N-U16-066 |
| VDR-U16-C139 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:454 | _compute_state | FACT | always | — | state is a stored computed field depending on amount_residual, the move state and payment_state, and approval_state. | N-U16-086 |
| VDR-U16-C140 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:473 | Shortcut to paid | FACT | company-paid with entry | — | A company-paid expense with a linked move is paid at once without waiting for the bank statement. | N-U16-080 |
| VDR-U16-C141 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:475 | move.state == 'draft' | FACT | employee-paid | — | A draft receipt or a not-paid receipt gives state posted. | N-U16-080 |
| VDR-U16-C142 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:468 | move.state == 'cancel' | FACT | cancelled entry | — | A cancelled linked move yields paid for the expense. | N-U16-091 |
| VDR-U16-C143 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:483 | _get_invoice_in_payment_state | FACT | payment_state in_payment or partial with residual | — | The in-payment state is taken from the account hook for in_payment or partial payments with a residual. | N-U16-081 |
| VDR-U16-C144 | FUNCTION MAPPING REQUIRED | account/models/account_move.py:7367 | _get_invoice_in_payment_state | FACT | Community without accounting app | — | The hook returns paid (docstring says the accountant module overrides it to enable in_payment); so state in_payment is unreachable here. Aligns with U12. | N-U16-081 |
| VDR-U16-C145 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:193 | amount_residual | FACT | always | — | amount_residual on the expense is related to the entry residual. | N-U16-080 |
| VDR-U16-C146 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1200 | default_partner_bank_id | FACT | action_pay | — | The Register Payment button opens the standard register-payment action on the receipt with the receipt's bank account preselected if unique. | N-U16-077 |
| VDR-U16-C147 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/account_payment_register.py:18 | primary_bank_account_id | FACT | register payment on expense receipt | — | Batch key partner_bank_id is the employee's primary bank account or the first bank of the partner, when the receipt has no bank. | N-U16-082 |
| VDR-U16-C148 | FUNCTION MAPPING REQUIRED | hr_expense/wizard/account_payment_register.py:30 | expense_id | FACT | register payment | — | Payment entry lines are tagged with the first expense id of the paid batch. | N-U16-083 |
| VDR-U16-C149 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move_line.py:17 | employee partner is correctly set | FACT | expense receipts | — | Every line of an expense receipt takes the move partner, preventing wrong bank accounts on payments. | N-U16-090 |
| VDR-U16-C150 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:23 | commercial_partner_id | FACT | own-account expense moves | — | commercial_partner_id keeps the partner's commercial partner unless it equals the company partner. | N-U16-090 |
| VDR-U16-C151 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:103 | Command.clear() | FACT | reversal of entry | — | _reverse_moves clears expense_ids on the moves before calling super, detaching the expenses. | N-U16-084 |
| VDR-U16-C152 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:108 | remove the link with the move | FACT | button_cancel | — | button_cancel also clears expense_ids; the comment explains cancelling the move is not cancelling the expense. | N-U16-084 |
| VDR-U16-C153 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:111 | Command.clear() | FACT | button_cancel | — | Same detach call after super().button_cancel(). | N-U16-084 |
| VDR-U16-C154 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:103 | Command.clear() | UNKNOWN | button_cancel or reversal | RT | Inverse effect on the expense link of a one-to-many clear command was not executed; if the inverse is not nulled the state could remain derived from the cancelled move. | N-U16-094 |
| VDR-U16-C155 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:994 | Reverting state | FACT | state moves back to approved | — | A transition from posted/paid to approved posts a Journal Entry Reset to Draft or Journal Entry Deleted message depending on whether the move still exists. | N-U16-078 |
| VDR-U16-C156 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1315 | state == 'posted' | FACT | dashboard | — | The dashboard shows posted employee-paid expenses under the approved (Waiting Reimbursement) bucket. | N-U16-085 |
| VDR-U16-C157 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1308 | own_account | FACT | dashboard | — | The reimbursement bucket counts only own_account expenses in approved or posted state. | N-U16-085 |
| VDR-U16-C158 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_move.py:106 | button_cancel | INFERENCE | payment already registered | RT | Neither _reverse_moves nor button_cancel in hr_expense touches reconciled payments, so a payment made before reversal stays; the code does not block re-posting. | N-U16-092 |
| VDR-U16-C159 | FUNCTION MAPPING REQUIRED | hr_expense/models/res_config_settings.py:19 | module_hr_payroll_expense | UNKNOWN | module not in Community tree | — | Reimbursement in payslip is a settings toggle for a module absent from the Community addons path. | N-U16-087 |
| VDR-U16-C160 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1350 | action_open_account_move | FACT | form | — | Open Journal Entry opens the receipt for own-account expenses and the payment for company-paid expenses. | N-U16-088 |
| VDR-U16-C161 | FUNCTION MAPPING REQUIRED | hr_expense/tests/test_expenses_states.py:67 | test_expense_state_synchro_1_cancel_move | INFERENCE | bundled test, not executed | RT | Test source asserts that after button_draft and button_cancel on the receipt both expenses are approved with account_move_id False. | N-U16-093 |
| VDR-U16-C162 | FUNCTION MAPPING REQUIRED | hr_expense/tests/test_expenses_states.py:81 | test_expense_state_synchro_1_unlink_move | INFERENCE | bundled test, not executed | RT | Test source asserts the same outcome after unlinking the payment and the move. | N-U16-093 |
| VDR-U16-C163 | FUNCTION MAPPING REQUIRED | hr_expense/tests/test_expenses_states.py:95 | test_expense_state_synchro_1_reverse_move | INFERENCE | bundled test, not executed | RT | Test source asserts the same outcome after _reverse_moves with cancel=True. | N-U16-093 |
| VDR-U16-C164 | FUNCTION MAPPING REQUIRED | sale/models/product_template.py:30 | at either cost or sales price | FACT | sale installed | — | expense_policy on the product has values no, cost, sales_price with help text covering expenses, vendor bills and stock pickings. | N-U16-095 |
| VDR-U16-C165 | FUNCTION MAPPING REQUIRED | sale_expense/models/hr_expense.py:11 | Customer to Reinvoice | FACT | sale_expense installed | — | hr.expense gains sale_order_id (customer to reinvoice) and sale_order_line_id, both stored, domain limited to confirmed orders through name search. | N-U16-095 |
| VDR-U16-C166 | FUNCTION MAPPING REQUIRED | sale_expense/models/hr_expense.py:34 | can_be_reinvoiced | FACT | sale_expense installed | — | can_be_reinvoiced is true only for policies cost or sales_price. | N-U16-098 |
| VDR-U16-C167 | FUNCTION MAPPING REQUIRED | sale_expense/models/hr_expense.py:39 | sale_order_id = False | FACT | category not reinvoiceable | — | For non reinvoiceable categories the order and order line fields are cleared. | N-U16-098 |
| VDR-U16-C168 | FUNCTION MAPPING REQUIRED | sale_expense/models/hr_expense.py:77 | _prepare_analytic_account_data | FACT | expense has order but no distribution | — | action_post creates an analytic account from the order and sets the expense distribution to 100 percent of it because re-invoicing needs analytic entries. | N-U16-099 |
| VDR-U16-C169 | FUNCTION MAPPING REQUIRED | project_sale_expense/models/hr_expense.py:49 | _get_analytic_distribution | FACT | project_sale_expense installed | — | With project_sale_expense, if the order has a project and the expense has no distribution, the project's analytic distribution is used (creating the project account if needed). | N-U16-099 |
| VDR-U16-C170 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:49 | analytic distribution | FACT | sale installed | — | _prepare_analytic_lines is called only for move lines that have an analytic distribution; so re-invoicing exists only for allocated lines. | N-U16-105 |
| VDR-U16-C171 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:64 | not a reversal one | FACT | sale installed | — | Re-invoicing is skipped for move lines of reversal moves and for lines without product. | N-U16-105 |
| VDR-U16-C172 | FUNCTION MAPPING REQUIRED | sale_expense/models/account_move_line.py:16 | expense_policy | FACT | sale_expense installed | — | For expense lines _sale_can_be_reinvoice requires policy cost or sales_price, an order on the expense and display_type product. | N-U16-098 |
| VDR-U16-C173 | FUNCTION MAPPING REQUIRED | sale_expense/models/account_move_line.py:25 | sale_order_id or None | FACT | sale_expense installed | — | The order of an expense line is the expense's sale_order_id, replacing the normal vendor-bill mapping. | N-U16-096 |
| VDR-U16-C174 | FUNCTION MAPPING REQUIRED | project_sale_expense/models/account_move_line.py:16 | mapping_from_project.update | FACT | project_sale_expense installed | — | Project-derived order mapping is computed first and then overwritten by the expense's explicit order. | N-U16-096 |
| VDR-U16-C175 | FUNCTION MAPPING REQUIRED | sale_project/models/account_move_line.py:37 | contains all the same analytic | FACT | sale_project installed | — | A sale.order matches a move line when the order's project analytic accounts cover the move line distribution; among matches, the earliest confirmed one is chosen. | N-U16-096 |
| VDR-U16-C176 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:105 | must be validated before registering | FACT | order in draft or sent | — | A draft or quotation-sent order raises a user error when a re-invoiced expense is posted. | N-U16-100 |
| VDR-U16-C177 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:111 | cancelled Sales Order | FACT | order cancelled | — | A cancelled order raises a user error. | N-U16-100 |
| VDR-U16-C178 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:117 | locked Sales Order | FACT | order locked | — | A locked order raises a user error. | N-U16-100 |
| VDR-U16-C179 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:209 | _get_product_price | FACT | policy sales_price | — | Sales price policy uses the order pricelist price for quantity 1 at the order date. | N-U16-101 |
| VDR-U16-C180 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:223 | abs(amount / unit_amount) | FACT | policy cost and same currency | — | Cost policy price is the absolute entry amount divided by quantity, converted to order currency if needed. | N-U16-101 |
| VDR-U16-C181 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:195 | is_expense | FACT | sale installed | — | The created sale order line is flagged is_expense with the move line's analytic distribution. | N-U16-102 |
| VDR-U16-C182 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:182 | taxes_id | INFERENCE | sale installed | — | The re-invoice line takes customer taxes from the product (mapped by fiscal position), not the taxes of the expense; so billed tax may differ from recovered input tax. | N-U16-111 |
| VDR-U16-C183 | FUNCTION MAPPING REQUIRED | sale_expense/models/account_move_line.py:57 | force_split_lines | FACT | sale_expense installed | — | Each expense line gets its own order line (no reuse of an existing line even for sales-price on delivered policy). | N-U16-102 |
| VDR-U16-C184 | FUNCTION MAPPING REQUIRED | sale/models/account_move_line.py:128 | force_split_lines | FACT | sale installed | — | Only vendor-bill lines for sales-price policy with delivery invoicing may be merged into an existing expense order line; the context flag disables merging. | N-U16-102 |
| VDR-U16-C185 | FUNCTION MAPPING REQUIRED | sale_expense/models/account_move_line.py:42 | expense_ids | FACT | sale_expense installed | — | The new line links the expense, uses the move line name and analytic distribution. | N-U16-102 |
| VDR-U16-C186 | FUNCTION MAPPING REQUIRED | sale_expense/models/account_move_line.py:47 | expense_id.quantity | FACT | sales_price policy and product has cost | — | For sales-price categories with a cost the order line quantity is the expense quantity. | N-U16-102 |
| VDR-U16-C187 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:931 | amount', '<=', 0.0 | FACT | sale installed | — | Delivered quantity of analytic-method lines (expense lines) sums analytic unit_amount of lines with amount <= 0. | N-U16-103 |
| VDR-U16-C188 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:894 | qty_delivered_method | FACT | line is_expense | — | Expense order lines use the analytic delivered-quantity method. | N-U16-103 |
| VDR-U16-C189 | FUNCTION MAPPING REQUIRED | sale_expense/models/hr_expense.py:59 | product_uom_qty | FACT | reverse, set to draft or unlink of the entry | — | _sale_expense_reset_sol_quantities sets order line quantity and delivered quantity to zero and clears expense_ids (in sudo after checking write access). | N-U16-104 |
| VDR-U16-C190 | FUNCTION MAPPING REQUIRED | sale_expense/models/account_move.py:11 | _sale_expense_reset_sol_quantities | FACT | _reverse_moves, button_draft, unlink | — | Reverse, draft reset and delete of the entry all call the reset helper before the base method. | N-U16-104 |
| VDR-U16-C191 | FUNCTION MAPPING REQUIRED | sale_expense/models/hr_expense.py:53 | stored product in an expense | FACT | sale_stock installed and storable category | — | A source note says the reset raises for storable products when the stock sale module is installed and that this is acceptable. | N-U16-113 |
| VDR-U16-C192 | FUNCTION MAPPING REQUIRED | sale_expense/models/sale_order.py:14 | posted', 'in_payment', 'paid' | FACT | sale_expense installed | — | sale.order.expense_ids only lists expenses in posted, in_payment or paid state. | N-U16-106 |
| VDR-U16-C193 | FUNCTION MAPPING REQUIRED | sale_expense/models/sale_order.py:21 | no ir.rule applied | FACT | context sale_expense_all_order | — | Name search with the context flag shows all confirmed orders in the user's companies without applying record rules, for salespeople without all-lead access. | N-U16-110 |
| VDR-U16-C194 | FUNCTION MAPPING REQUIRED | sale_expense/models/product_template.py:35 | group_hr_expense_user | FACT | category is expensable | — | The re-invoice policy field is visible on expensable categories only to All Approver users. | N-U16-108 |
| VDR-U16-C195 | FUNCTION MAPPING REQUIRED | sale_expense/models/product_template.py:43 | expense_policy = 'no' | FACT | category not expensable | — | Non-expensable products force policy to no. | N-U16-098 |
| VDR-U16-C196 | FUNCTION MAPPING REQUIRED | sale_expense/data/sale_expense_data.xml:12 | sales_price | FACT | noupdate data | — | Data file writes: meal sales_price; mileage sales_price with delivery policy; travel cost with delivery policy; communication cost; gifts untouched. | N-U16-107 |
| VDR-U16-C197 | FUNCTION MAPPING REQUIRED | sale_expense/data/sale_expense_data.xml:16 | expense_product_travel_accommodation | OBSERVATION | DB: restored database | — | Restored DB: meal sales_price/order, mileage sales_price/delivery, travel cost/delivery, communication cost/order, gift no/order, generic no/order. | N-U16-107 |
| VDR-U16-C198 | FUNCTION MAPPING REQUIRED | sale_expense/models/hr_expense.py:67 | sale_order_id | FACT | split wizard | — | Splitting an expense keeps the customer order on each part. | N-U16-102 |
| VDR-U16-C199 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1582 | project_id=False | FACT | company-paid posting | — | Company-paid move creation clears the project_id context so a project default does not pollute the payment entry. | N-U16-099 |
| VDR-U16-C200 | FUNCTION MAPPING REQUIRED | project_hr_expense/models/hr_expense.py:12 | _get_analytic_distribution | FACT | project_hr_expense installed, context project_id | — | Creating an expense from a project (context project_id) defaults the distribution to the project's analytic distribution. | N-U16-099 |
| VDR-U16-C201 | FUNCTION MAPPING REQUIRED | project_sale_expense/models/hr_expense.py:30 | keep both analytic distributions | FACT | project_sale_expense installed | — | When an expense has an order with a project the distributions are merged if plans differ, else the project distribution wins. | N-U16-099 |
| VDR-U16-C202 | FUNCTION MAPPING REQUIRED | sale_expense/models/hr_expense.py:48 | _sale_expense_reset_sol_quantities | INFERENCE | invoiced line | RT | If the order line was already invoiced, resetting its quantity to zero changes billed quantity logic of the order; credit-note handling was not traced. | N-U16-113 |
| VDR-U16-C203 | FUNCTION MAPPING REQUIRED | sale_expense/models/account_move.py:14 | button_draft | INFERENCE | payment exists | RT | No override unwinds a reimbursement payment when the entry is set back to draft; the reset helper only touches order lines. | N-U16-112 |
| VDR-U16-C204 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:17 | account.analytic.line | FACT | hr_timesheet installed | — | A time entry is an account.analytic.line with project_id, task_id, employee_id; there is no separate timesheet table. | N-U16-114 |
| VDR-U16-C205 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:248 | It is not a timesheet | FACT | create | — | create skips timesheet processing when neither task nor project is given, so ordinary analytic lines are untouched. | N-U16-115 |
| VDR-U16-C206 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:252 | private task | FACT | create | — | A task without project_id causes a validation error. | N-U16-117 |
| VDR-U16-C207 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:256 | task.company_id or project.company_id | FACT | create | — | Company is taken from task, then project, then the given company. | N-U16-117 |
| VDR-U16-C208 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:265 | project_time_mode_id | FACT | create without unit | — | Unit defaults to the company project time mode. | N-U16-119 |
| VDR-U16-C209 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:299 | active employee in the selected companies | FACT | create | — | Archived employees or employees outside the allowed companies cause a validation error. | N-U16-118 |
| VDR-U16-C210 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:296 | employee_id_per_company_per_user | FACT | create with user only | — | When only the user is given, the employee is chosen by user and company (single company match is used directly). | N-U16-118 |
| VDR-U16-C211 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:432 | required on the project | FACT | create or write | — | All analytic account columns of the project are copied to the entry and mandatory plans for business domain timesheet must be filled on the project. | N-U16-124 |
| VDR-U16-C212 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:474 | timesheet.unit_amount * cost | FACT | unit_amount, employee or account changes | — | The amount is negative quantity times cost, converted to the account currency. | N-U16-120 |
| VDR-U16-C213 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:475 | _convert | FACT | cost recompute | — | Employee currency to account currency conversion uses the entry date and the current company. | N-U16-120 |
| VDR-U16-C214 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:505 | hourly_cost | FACT | no project rate table override | — | _hourly_cost returns the employee hourly cost or zero. | N-U16-120 |
| VDR-U16-C215 | FUNCTION MAPPING REQUIRED | hr_hourly_cost/models/hr_employee.py:9 | Hourly Cost | FACT | hr_hourly_cost installed | — | hourly_cost is a monetary field tracked, default 0, visible to hr.group_hr_user only (supporting module). | N-U16-132 |
| VDR-U16-C216 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:198 | mapping_entry.cost | FACT | sale_timesheet installed, project pricing employee_rate | — | With employee rate pricing the project's mapping cost replaces the employee cost. | N-U16-121 |
| VDR-U16-C217 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:465 | at least an active analytic | FACT | create or write | — | An inactive analytic account blocks recording. | N-U16-123 |
| VDR-U16-C218 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:471 | must belong to the same company | FACT | create or write | — | More than one company among entry, accounts, task and project raises an error. | N-U16-123 |
| VDR-U16-C219 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:477 | update | INFERENCE | unit_amount, employee_id or account_id in values | — | The post-processing writes only the amount field on the analytic line; no account.move is created anywhere in hr_timesheet, so time cost does not reach the ledger. | N-U16-115 |
| VDR-U16-C220 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/project_project.py:104 | you need an analytic account | FACT | allow_timesheets and not template | — | Constraint requires an account on a project with timesheets enabled, naming the project plan. | N-U16-122 |
| VDR-U16-C221 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/project_project.py:133 | Create an analytic account | FACT | project create | — | create makes the account first and passes it to the project. | N-U16-122 |
| VDR-U16-C222 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/project_project.py:147 | _create_analytic_account | FACT | allow_timesheets set to true | — | Enabling timesheets on an existing project without account creates one. | N-U16-122 |
| VDR-U16-C223 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:1185 | plan_id | FACT | project | — | Created account values: project name, company, partner, plan = project plan. | N-U16-122 |
| VDR-U16-C224 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/project_project.py:176 | timesheet entries referencing them | FACT | project unlink | — | Projects with entries cannot be deleted; a redirect to the entries is offered. | N-U16-125 |
| VDR-U16-C225 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:708 | account_id.line_ids | FACT | project unlink | — | The project's analytic account is deleted only when it has no lines. | N-U16-125 |
| VDR-U16-C226 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:279 | company cannot be changed | FACT | project company change | — | Company change blocked when the account has lines or is shared. | N-U16-125 |
| VDR-U16-C227 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/res_company.py:46 | _create_internal_project_task | FACT | company create or module install | — | An Internal project with Training and Meeting tasks is created for each company; the project is stored as company.internal_project_id. | N-U16-126 |
| VDR-U16-C228 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/res_company.py:26 | internal_project_id | OBSERVATION | DB: restored database | — | Restored DB: the single company has an internal project set (one project exists, named Internal) and a time-off task set; install hooks also left analytic lines (count only: 2, zero hours). | N-U16-126 |
| VDR-U16-C229 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/res_company.py:24 | Timesheet Encoding Unit | FACT | company setting | — | Encoding unit defaults to hours; the settings screen offers hours or days. | N-U16-128 |
| VDR-U16-C230 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/res_company.py:25 | _default_timesheet_encode_uom_id | OBSERVATION | DB: restored database | — | Restored DB: encoding unit and project time unit of the company are both Hours. | N-U16-128 |
| VDR-U16-C231 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/res_config_settings.py:12 | Employee Reminder | FACT | settings | — | Settings expose employee and approver reminder flags, project time unit and encoding method. | N-U16-128 |
| VDR-U16-C232 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/project_project.py:78 | allocated_hours - project.effective_hours | FACT | project | — | remaining_hours = allocated minus effective hours (sum of entry quantities); overtime when negative. | N-U16-114 |
| VDR-U16-C233 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:213 | not yours | FACT | write or unlink by non-approver | — | Users outside the all-timesheets role may change only their own entries. | N-U16-130 |
| VDR-U16-C234 | FUNCTION MAPPING REQUIRED | hr_timesheet/security/hr_timesheet_security.xml:54 | user_id | FACT | own-timesheets group | — | Rule account.analytic.line.timesheet.user: own entries on projects visible to employees/portal, where the user is partner or follower. | N-U16-130 |
| VDR-U16-C235 | FUNCTION MAPPING REQUIRED | hr_timesheet/security/hr_timesheet_security.xml:64 | timesheet_line_rule_approver | FACT | all-timesheets group | — | Approver rule: all entries on projects visible to employees/portal, or followed, or where the user is the partner. | N-U16-130 |
| VDR-U16-C236 | FUNCTION MAPPING REQUIRED | hr_timesheet/security/hr_timesheet_security.xml:80 | project_id', '!=', False | FACT | administrator or project manager | — | Manager rule gives all entries with a project to the timesheet administrator and to project managers. | N-U16-130 |
| VDR-U16-C237 | FUNCTION MAPPING REQUIRED | hr_timesheet/security/hr_timesheet_security.xml:25 | group_timesheet_manager | FACT | always | — | Three groups: own timesheets only, all timesheets, administrator (implies approver and hr officer); project manager group implies the approver group. | N-U16-130 |
| VDR-U16-C238 | FUNCTION MAPPING REQUIRED | hr_timesheet/security/ir.model.access.csv:2 | access_account_analytic_line_user | FACT | always | — | Timesheet user group has full CRUD ACL on analytic lines; write on analytic accounts without create. | N-U16-130 |
| VDR-U16-C239 | FUNCTION MAPPING REQUIRED | hr_timesheet/security/ir.model.access.xml:10 | name="active">0 | FACT | noupdate | — | The portal ACL for analytic lines is shipped inactive, as is the portal rule. | N-U16-137 |
| VDR-U16-C240 | FUNCTION MAPPING REQUIRED | sale_timesheet/security/sale_timesheet_security.xml:11 | account_analytic_line_rule_readonly_user | FACT | sale_timesheet installed | — | sale_timesheet rewrites two account rules (readonly user and billing user) so their domain is project_id = False. | N-U16-134 |
| VDR-U16-C241 | FUNCTION MAPPING REQUIRED | sale_timesheet/security/sale_timesheet_security.xml:12 | project_id', '=', False | OBSERVATION | DB: restored database | — | Restored DB: rules account.analytic.line.billing.user and account.analytic.line.readonly.user both hold domain project_id = False and are active. | N-U16-134 |
| VDR-U16-C242 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_employee.py:57 | employees who have timesheets | FACT | non-approver deleting employee | — | Deletion by non-approvers is blocked when the employee has entries and no active employee exists. | N-U16-131 |
| VDR-U16-C243 | FUNCTION MAPPING REQUIRED | hr_timesheet/report/timesheets_analysis_report.py:70 | project_id IS NOT NULL | FACT | report view | — | The timesheet analysis report is an SQL view on analytic lines having project_id. | N-U16-115 |
| VDR-U16-C244 | FUNCTION MAPPING REQUIRED | hr_timesheet/security/hr_timesheet_security.xml:88 | timesheets_analysis_report_comp_rule | FACT | always | — | The analysis report has a multi-company rule plus user/approver/manager rules. | N-U16-130 |
| VDR-U16-C245 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:475 | _convert | INFERENCE | unit_amount or employee changes | — | The cost is stored in amount at write time and recomputed only when unit_amount, employee_id or account_id appears in the written values, so later hourly cost changes do not restate old entries. | N-U16-133 |
| VDR-U16-C246 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:207 | _check_can_write | FACT | write | — | Own-entry check is implemented in _check_can_write which other modules extend (billing lock, time off lock). | N-U16-127 |
| VDR-U16-C247 | FUNCTION MAPPING REQUIRED | hr_hourly_cost/models/hr_employee.py:10 | hr.group_hr_user | FACT | hr_hourly_cost installed | — | The hourly cost is tracked in chatter and restricted to the officer group. | N-U16-132 |
| VDR-U16-C248 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | edition boundary | — | No approval/validation status or period lock on timesheet entries exists in the Community modules read; any such feature in another edition is outside this study. | N-U16-136 |
| VDR-U16-C249 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | design boundary | — | No link between timesheet cost and payroll or ledger labour cost was found; difference between them is not recorded. | N-U16-135 |
| VDR-U16-C250 | FUNCTION MAPPING REQUIRED | sale_project/models/product_template.py:94 | ordered_prepaid | FACT | sale_project installed | — | Service policy to (invoice_policy, service_type) mapping: ordered_prepaid (order, manual), delivered_milestones (delivery, milestones), delivered_manual (delivery, manual). | N-U16-138 |
| VDR-U16-C251 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/product_template.py:74 | delivered_timesheet | FACT | sale_timesheet installed | — | sale_timesheet adds delivered_timesheet (delivery, timesheet) and overrides ordered_prepaid to (order, timesheet). | N-U16-138 |
| VDR-U16-C252 | FUNCTION MAPPING REQUIRED | sale_project/models/product_template.py:18 | group_project_milestone | OBSERVATION | DB: feature group not enabled | — | The Based on Milestones policy appears only when the milestone feature group is enabled; feature-enabled means the superuser holds the group (res.groups._is_feature_enabled); in the restored DB the superuser's group closure contains the project stages and unit-of-measure groups but not the milestone group, so the policy is not offered. | N-U16-148 |
| VDR-U16-C253 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order_line.py:68 | qty_delivered_method = 'timesheet' | FACT | service product with service_type timesheet and not expense | — | Delivered-quantity method is timesheet for such lines. | N-U16-139 |
| VDR-U16-C254 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order_line.py:78 | _get_delivered_quantity_by_analytic | FACT | timesheet method lines | — | Delivered quantity is the converted sum of unit_amount of linked entries with a project (sudo). | N-U16-139 |
| VDR-U16-C255 | FUNCTION MAPPING REQUIRED | sale/models/sale_order_line.py:978 | _compute_quantity | FACT | sale installed | — | Entry quantity is converted from entry unit to order line unit before summing. | N-U16-161 |
| VDR-U16-C256 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:100 | reached_milestones_per_sol | FACT | milestone method lines | — | Milestone line delivered quantity = sum of reached milestone percentages times ordered quantity. | N-U16-148 |
| VDR-U16-C257 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:133 | task_rate | FACT | timesheet with billable task | — | For task_rate and fixed_rate pricing the entry takes the task's sale_line_id. | N-U16-142 |
| VDR-U16-C258 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:127 | map_entry | FACT | employee_rate pricing | — | For employee_rate pricing the mapped line of that employee on the project is used, falling back to task line then project line. | N-U16-142 |
| VDR-U16-C259 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:81 | is_so_line_edited | FACT | dependencies change | — | so_line is recomputed only for entries not manually edited and not billed. | N-U16-142 |
| VDR-U16-C260 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:10 | Billed on Timesheets | FACT | always | — | Billable types: billable_time, billable_fixed, billable_milestones, billable_manual, non_billable, timesheet_revenues, service_revenues, other_revenues, other_costs. | N-U16-143 |
| VDR-U16-C261 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:63 | timesheet_revenues | FACT | service_type timesheet | — | Type for delivery+timesheet lines is billable_time unless amount and quantity are positive (revenue line). | N-U16-143 |
| VDR-U16-C262 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:97 | invoicing_legacy | FACT | always | — | An entry is not billed if it has no invoice, or the invoice is cancelled and not legacy. | N-U16-157 |
| VDR-U16-C263 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order.py:161 | _link_timesheets_to_invoice | FACT | invoice created from order | — | sale.order._create_invoices links entries to the new moves, passing the date range from the wizard context. | N-U16-144 |
| VDR-U16-C264 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/account_move.py:80 | service_type == 'timesheet' | FACT | draft out_invoice | — | Only draft out_invoice lines whose order lines are delivery plus timesheet service products take entries. | N-U16-144 |
| VDR-U16-C265 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/account_move.py:92 | timesheet_invoice_id | FACT | linking | — | Linking writes timesheet_invoice_id on matched entries in sudo. | N-U16-144 |
| VDR-U16-C266 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/account_move_line.py:25 | reversed | FACT | linking | — | Entries taken are those with no invoice, a cancelled non-legacy invoice, or a reversed invoice. | N-U16-144 |
| VDR-U16-C267 | FUNCTION MAPPING REQUIRED | sale_timesheet/wizard/sale_make_invoice_advance.py:42 | _recompute_qty_to_invoice | FACT | method delivered and timesheet lines to invoice | — | The invoicing dialog recomputes quantity to invoice for the chosen date range before creating invoices, with context dates. | N-U16-147 |
| VDR-U16-C268 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order_line.py:183 | max(0.0, min( | FACT | order has posted credit notes | — | With credit notes the quantity to invoice is capped at delivered minus invoiced to prevent over-billing. | N-U16-147 |
| VDR-U16-C269 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order_line.py:192 | qty_to_invoice = qty_to_invoice | INFERENCE | date range recompute | — | The recompute writes qty_to_invoice directly on the line (and preserves invoice_status when empty), bypassing the usual stored computation. | N-U16-159 |
| VDR-U16-C270 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:106 | already invoiced | FACT | delivery product lines with non-cancelled invoice | — | Writing unit_amount, employee_id, project_id, task_id, so_line or date raises on such entries. | N-U16-145 |
| VDR-U16-C271 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:179 | already been invoiced | FACT | invoice posted | — | Deleting entries linked to a posted invoice raises. | N-U16-145 |
| VDR-U16-C272 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:228 | _is_updatable_timesheet | FACT | always | — | The expression references super()._is_updatable_timesheet without calling it; a bound method object is truthy, so only _is_not_billed() decides. | N-U16-158 |
| VDR-U16-C273 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/account_move.py:107 | timesheet_invoice_id | FACT | action_post of out_refund with reversed entry | — | Posting a credit note releases the entries of the reversed invoice that belong to the credited order lines. | N-U16-146 |
| VDR-U16-C274 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/account_move_line.py:57 | protecting | FACT | draft invoice line deleted | — | Deleting a draft invoice line clears the link on its entries while protecting so_line from recomputation so delivered quantity is unchanged. | N-U16-146 |
| VDR-U16-C275 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/account_move_reversal.py:25 | timesheet_invoice_id | FACT | reverse and modify | — | Reverse and modify relinks entries to the new replacement invoice by order line. | N-U16-146 |
| VDR-U16-C276 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order.py:64 | _create_upsell_activity | FACT | order confirmed with salesperson, prepaid line over threshold | — | A salesperson activity is created once per line when delivered quantity exceeds ordered times the product threshold (default 1). | N-U16-140 |
| VDR-U16-C277 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order.py:110 | service_upsell_threshold | FACT | prepaid service line | — | Threshold is the product's service_upsell_threshold, 1.0 if unset. | N-U16-153 |
| VDR-U16-C278 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order_line.py:48 | is_ordered_prepaid | FACT | sale_timesheet | — | remaining_hours_available requires ordered_prepaid and a time unit. | N-U16-140 |
| VDR-U16-C279 | FUNCTION MAPPING REQUIRED | sale_timesheet/data/sale_service_data.xml:4 | time_product | FACT | noupdate | — | Seed product Service on Timesheets: service type, list price 40, hour unit, policy delivered_timesheet. | N-U16-150 |
| VDR-U16-C280 | FUNCTION MAPPING REQUIRED | sale_timesheet/data/sale_service_data.xml:10 | delivered_timesheet | OBSERVATION | DB: restored database | — | Restored DB holds the seeded time product as a non-expensable service, sale_ok, invoicing policy delivery. | N-U16-150 |
| VDR-U16-C281 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/product_template.py:102 | cannot be archived, deleted | FACT | always | — | Archiving, deleting or setting a company on the time product raises. | N-U16-150 |
| VDR-U16-C282 | FUNCTION MAPPING REQUIRED | sale_timesheet_margin/models/sale_order_line.py:29 | amount_sum / unit_amount_sum | FACT | sale_timesheet_margin installed, no product standard price | — | purchase_price of timesheet lines is minus the sum of amounts divided by the sum of hours, else the product standard price. | N-U16-151 |
| VDR-U16-C283 | FUNCTION MAPPING REQUIRED | sale_timesheet_margin/__manifest__.py:13 | sale_margin | FACT | auto_install | — | sale_timesheet_margin installs automatically when sale_margin and sale_timesheet are present. | N-U16-153 |
| VDR-U16-C284 | FUNCTION MAPPING REQUIRED | sale_timesheet/report/timesheets_analysis_report.py:44 | SOL.price_unit | FACT | report view | — | Timesheet revenue is quantity times line price unit (delivery) or prorated subtotal (order policy), zero for manual or milestone lines; margin = revenue plus entry amount. | N-U16-151 |
| VDR-U16-C285 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_project.py:165 | not a service | FACT | project sale_line_id | — | Constraint on project.sale_line_id: must be a service line and not an expense line. | N-U16-149 |
| VDR-U16-C286 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_project.py:167 | expense or a vendor bill | FACT | project sale_line_id | — | Expense or vendor-bill order lines cannot be linked to a billable project. | N-U16-149 |
| VDR-U16-C287 | FUNCTION MAPPING REQUIRED | sale_project/models/project_task.py:150 | re-invoiced expense | FACT | task sale_line_id | — | Same constraint on tasks. | N-U16-149 |
| VDR-U16-C288 | FUNCTION MAPPING REQUIRED | sale_project/models/project_task.py:110 | consistent_partners | FACT | partner change | — | Changing the task customer clears the order and order line if they no longer match. | N-U16-149 |
| VDR-U16-C289 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_sale_line_employee_map.py:42 | UNIQUE(project_id,employee_id) | FACT | always | — | An employee can appear once per project in the line table. | N-U16-155 |
| VDR-U16-C290 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_sale_line_employee_map.py:140 | _update_timesheets_sale_line_id | FACT | map create or write | — | Creating or editing the table re-points existing unedited, unbilled entries of that employee to the mapped line. | N-U16-142 |
| VDR-U16-C291 | FUNCTION MAPPING REQUIRED | sale_project/security/sale_project_security.xml:7 | is_service | FACT | project manager | — | Project managers can only read confirmed service order lines with a project or task. | N-U16-156 |
| VDR-U16-C292 | FUNCTION MAPPING REQUIRED | sale_timesheet/security/ir.model.access.csv:3 | access_project_sale_line_employee_map_manager | FACT | always | — | Employee-to-line table: base users read, project managers full CRUD. | N-U16-155 |
| VDR-U16-C293 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_project.py:86 | employee_rate | FACT | billable project | — | Project pricing type: employee_rate if the table has rows, fixed_rate if the project has an order line, else task_rate; false when not billable. | N-U16-153 |
| VDR-U16-C294 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:59 | billable_manual | FACT | no order line | — | Entries without a line are non-billable unless the project's billing type is billed manually. | N-U16-143 |
| VDR-U16-C295 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:100 | _check_timesheet_can_be_billed | FACT | always | — | _check_timesheet_can_be_billed validates that the entry line is the project table line, task line or project line. | N-U16-142 |
| VDR-U16-C296 | FUNCTION MAPPING REQUIRED | n/a | n/a | UNKNOWN | runtime | RT | Partial credit notes on multi-line time invoices and the legacy invoice payment state were not executed. | N-U16-160 |
| VDR-U16-C297 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order.py:145 | _timesheet_service_generation | FACT | order confirmation | — | _action_confirm generates projects and tasks for all lines in sudo before the base confirmation. | N-U16-162 |
| VDR-U16-C298 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order.py:140 | disable_project_task_generation | FACT | context flag | — | The context flag skips generation (used when orders are created from tasks or from employee mapping). | N-U16-179 |
| VDR-U16-C299 | FUNCTION MAPPING REQUIRED | sale_project/models/product_template.py:24 | task_global_project | FACT | always | — | service_tracking adds task_global_project, task_in_project and project_only to the existing none value. | N-U16-166 |
| VDR-U16-C300 | FUNCTION MAPPING REQUIRED | sale_project/models/product_template.py:125 | should not have a project template | FACT | always | — | Constraint: tracking none cannot have a project or template; global task cannot have a template; project modes cannot have a global project. | N-U16-166 |
| VDR-U16-C301 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:379 | 1 per SO | FACT | service_tracking project_only or task_in_project | — | One generated project per order without template and one per order and template with templates. | N-U16-167 |
| VDR-U16-C302 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:339 | avoid creating a | FACT | reconfirmation | — | Existing project and task links on the lines are reused on reconfirmation. | N-U16-168 |
| VDR-U16-C303 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:389 | _prepare_analytic_account_data | FACT | new project generated | — | The reference analytic account per order is the order project's account or a new account from _prepare_analytic_account_data (name = order name, plan = project plan). | N-U16-169 |
| VDR-U16-C304 | FUNCTION MAPPING REQUIRED | sale/models/sale_order.py:2009 | plan_id | FACT | sale installed | — | Order-derived account values: name, code = customer reference, company, project plan, partner. | N-U16-169 |
| VDR-U16-C305 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:192 | allow_billable | FACT | project generated | — | Generated project values: order name, account, customer, sale line, active, company, billable. | N-U16-169 |
| VDR-U16-C306 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:207 | action_create_from_template | FACT | template is a template project | — | With a project template the project is created from the template, else the template project is copied. | N-U16-166 |
| VDR-U16-C307 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:236 | To Do | FACT | project without stages | — | If the project has no stages, four default task stages are created: To Do, In Progress, Done, Cancelled. | N-U16-178 |
| VDR-U16-C308 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:278 | force non assigned task | FACT | task generated | — | Task values: name, allocated hours, customer, description, project, order line, order, company, no assignee. | N-U16-170 |
| VDR-U16-C309 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order_line.py:136 | allocated_hours | FACT | sale_timesheet installed | — | Project allocated hours sum ordered quantity times unit factor over all lines sharing the template, treating unit as hour. | N-U16-173 |
| VDR-U16-C310 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/sale_order_line.py:101 | _compute_quantity | FACT | task creation | — | Task hours convert order quantity to the company time unit when units share a reference. | N-U16-170 |
| VDR-U16-C311 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:165 | allocated_hours | FACT | write product_uom_qty | — | Writing the ordered quantity updates task allocated hours unless context no_update_allocated_hours. | N-U16-171 |
| VDR-U16-C312 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:432 | A project must be defined | FACT | task_global_project without project | — | If no project is on the order or product a user error stops confirmation. | N-U16-172 |
| VDR-U16-C313 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:440 | delivered_milestones | FACT | milestone lines | — | Milestone products turn on milestones on the project and create or assign a default milestone (percentage 1) per line. | N-U16-166 |
| VDR-U16-C314 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order.py:290 | sale_line_id = False | FACT | order cancelled | — | Cancellation clears project.sale_line_id of every project tied to the order. | N-U16-174 |
| VDR-U16-C315 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:118 | project account is added | FACT | project on product or order | — | The order line distribution gains the project's accounts for roots not already present; if empty it takes the project's distribution. | N-U16-175 |
| VDR-U16-C316 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:468 | analytic_distribution | FACT | invoice line prepared from order line without distribution | — | Invoice lines take the task's project account, else the project account of the line's project, else the single project account found. | N-U16-176 |
| VDR-U16-C317 | FUNCTION MAPPING REQUIRED | sale_project/models/account_move_line.py:23 | _get_analytic_distribution | FACT | context project_id | — | Journal lines created from a project context (not payment lines, not receivable or payable) take the project's distribution. | N-U16-164 |
| VDR-U16-C318 | FUNCTION MAPPING REQUIRED | sale_project/models/account_move_line.py:13 | when a project creates an aml | FACT | lines linked to project order lines | — | Lines whose order line has a project keep their distribution against default-rule recompute. | N-U16-164 |
| VDR-U16-C319 | FUNCTION MAPPING REQUIRED | project_purchase/models/purchase_order_line.py:29 | _get_analytic_distribution | FACT | project_purchase installed, order project set | — | Purchase lines take the order project's distribution (and add the project account to existing distributions). | N-U16-164 |
| VDR-U16-C320 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order.py:173 | must be confirmed or | FACT | action_create_project | — | The create-project button requires a confirmed order without a project and is shown only to project managers. | N-U16-181 |
| VDR-U16-C321 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order.py:63 | is_project_manager | FACT | form | — | show_create_project_button needs project manager role, an order in a confirmed state and no existing project. | N-U16-181 |
| VDR-U16-C322 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:176 | action_confirm | FACT | project or task linked to a draft order line | — | Linking a project to an order line confirms the draft order. | N-U16-183 |
| VDR-U16-C323 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:168 | confirm newly created SOs | FACT | always | — | Comment: orders created from project or task are confirmed immediately on save. | N-U16-183 |
| VDR-U16-C324 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:73 | allow_billable | FACT | project partner compute | — | Non-billable projects or customers of another company have the customer cleared. | N-U16-177 |
| VDR-U16-C325 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:80 | sale_line_id and ( | FACT | partner change | — | A project whose customer no longer matches its order line has the line removed. | N-U16-177 |
| VDR-U16-C326 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:244 | reinvoiced_sale_order_id | FACT | project generated | — | Generated projects point back to the order as reinvoiced_sale_order_id. | N-U16-178 |
| VDR-U16-C327 | FUNCTION MAPPING REQUIRED | sale_project/security/sale_project_security.xml:4 | sale_order_line_rule_project_manager | OBSERVATION | DB: restored database | — | Restored DB: sale_project owns 4 ACL rows and 1 record rule (project manager read of service lines), matching 4 CSV rows and 1 rule in source. | N-U16-182 |
| VDR-U16-C328 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:134 | _timesheet_service_generation | FACT | line created after confirmation | — | Lines added to a confirmed order also trigger generation, in sudo. | N-U16-184 |
| VDR-U16-C329 | FUNCTION MAPPING REQUIRED | project/models/account_analytic_account.py:16 | project_count | INFERENCE | analytic account reused | — | An analytic account can have several projects (project_count), and the order mapping picks the earliest confirmed order among matches, so reuse of one account across projects can cross-assign costs. | N-U16-185 |
| VDR-U16-C330 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:933 | _get_template_default_context_whitelist | UNKNOWN | template flows | — | Template duplication of sub-tasks and recurring tasks was not traced in this unit. | N-U16-186 |
| VDR-U16-C331 | FUNCTION MAPPING REQUIRED | sale_project/models/project_task.py:72 | _compute_sale_order_id | FACT | task billable with line | — | Task order = order of its line, else project order, else project reinvoiced order, only if customers are consistent. | N-U16-162 |
| VDR-U16-C332 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:187 | reinvoiced_sale_order_id | FACT | project created with reinvoiced order | — | A newly created project becomes the project of its order when the order has none. | N-U16-163 |
| VDR-U16-C333 | FUNCTION MAPPING REQUIRED | sale_project/models/sale_order_line.py:145 | project.sale_line_id | FACT | link_to_project context | — | Orders created from a project context set the project's service line and reinvoiced order when empty. | N-U16-163 |
| VDR-U16-C334 | FUNCTION MAPPING REQUIRED | sale_project/models/project_milestone.py:42 | quantity_percentage | FACT | milestone | — | Milestone quantity percentage = milestone quantity over ordered quantity of its line. | N-U16-166 |
| VDR-U16-C335 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:1002 | _show_profitability | FACT | project panel | — | get_panel_data builds profitability_items from _get_profitability_items and sorts sections by sequence. | N-U16-187 |
| VDR-U16-C336 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:822 | group_project_user | FACT | get_panel_data | — | get_panel_data returns empty for non project users; _get_profitability_values needs the project manager group. | N-U16-206 |
| VDR-U16-C337 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:1129 | group_project_manager | FACT | _get_profitability_values | — | Profitability values for the dashboard card require the project manager role. | N-U16-206 |
| VDR-U16-C338 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:1137 | margin = revenues + costs | FACT | _get_profitability_values | — | Margin is revenues plus costs where costs are negative; margin percentage is margin over absolute costs. | N-U16-187 |
| VDR-U16-C339 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:516 | allow_billable | FACT | sale_project installed | — | Profitability shows only for billable projects. | N-U16-204 |
| VDR-U16-C340 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:787 | _add_purchase_items | FACT | sale_project installed | — | Order matters: revenue from order lines, then invoice items, then the purchase items hook. | N-U16-187 |
| VDR-U16-C341 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:500 | 'sale' | FACT | sale_project installed | — | Order line sources require state sale, not expense lines, and either to-invoice or invoiced quantity above zero. | N-U16-190 |
| VDR-U16-C342 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:561 | untaxed_amount_to_invoice | FACT | sale_project installed | — | Revenue amounts are untaxed amounts to invoice and invoiced of order lines grouped by currency, product and down payment flag. | N-U16-190 |
| VDR-U16-C343 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:588 | downpayment_amount_invoiced | FACT | down payment lines | — | Down payment section: invoiced = amount, to_invoice = minus amount. | N-U16-191 |
| VDR-U16-C344 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:758 | excluded_move_line_ids | FACT | sale_project installed | — | Customer invoice lines already linked to the order lines are excluded from the invoice items to avoid double counting. | N-U16-190 |
| VDR-U16-C345 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:723 | parent_state == 'draft' | FACT | invoice items | — | Draft invoice lines add to to_invoice (or to_bill for cost of goods), posted lines to invoiced (or billed). | N-U16-190 |
| VDR-U16-C346 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:708 | display_type | FACT | invoice items | — | Lines with display_type cogs and an expense-group account are costs; all other invoice lines are revenue. | N-U16-192 |
| VDR-U16-C347 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:718 | analytic distribution with different repartition | FACT | invoice and bill items | — | Amounts are weighted by the percentage of the project's account in each line's distribution. | N-U16-207 |
| VDR-U16-C348 | FUNCTION MAPPING REQUIRED | project_account/models/project_project.py:35 | analytic_distribution | FACT | vendor bill items | — | Only move lines whose analytic distribution contains the project account are picked. | N-U16-207 |
| VDR-U16-C349 | FUNCTION MAPPING REQUIRED | project_account/models/project_project.py:25 | in_invoice | FACT | project_account installed | — | Vendor bill items are lines of in_invoice and in_refund moves, draft or posted, with non-zero subtotal, not already counted. | N-U16-194 |
| VDR-U16-C350 | FUNCTION MAPPING REQUIRED | project_account/models/project_project.py:53 | amount_invoiced | FACT | posted vendor bill lines | — | Bill costs are negative: posted lines subtract their weighted balance from billed, draft ones from to_bill. | N-U16-194 |
| VDR-U16-C351 | FUNCTION MAPPING REQUIRED | project_account/models/project_project.py:130 | manufacturing_order | FACT | project_account installed | — | Other analytic lines exclude manufacturing and transfer categories and journal-linked lines. | N-U16-197 |
| VDR-U16-C352 | FUNCTION MAPPING REQUIRED | project_account/models/project_project.py:159 | we dont know what part | FACT | other analytic lines | — | Source comment: all such amounts are placed under billed or invoiced. | N-U16-197 |
| VDR-U16-C353 | FUNCTION MAPPING REQUIRED | project_account/models/project_project.py:146 | aal_amount < 0.0 | FACT | other analytic lines | — | Negative lines are costs, others revenues. | N-U16-197 |
| VDR-U16-C354 | FUNCTION MAPPING REQUIRED | project_purchase/models/project_project.py:144 | 'purchase' | FACT | project_purchase installed | — | Purchase order lines are selected with a membership test against a text value. | N-U16-209 |
| VDR-U16-C355 | FUNCTION MAPPING REQUIRED | project_purchase/models/project_project.py:193 | total_invoiced_amount | FACT | project_purchase installed | — | Unbilled remainder = line allocated amount minus invoiced non-refund amount; refunds only reduce billed amounts. | N-U16-193 |
| VDR-U16-C356 | FUNCTION MAPPING REQUIRED | project_purchase/models/project_project.py:126 | _add_purchase_items | FACT | project_purchase installed | — | project_purchase turns the base vendor-bill hook into a no-op and counts bills directly in _get_profitability_items with already-included invoice lines excluded. | N-U16-194 |
| VDR-U16-C357 | FUNCTION MAPPING REQUIRED | project_purchase/models/purchase_order.py:9 | project_id | FACT | project_purchase installed | — | purchase.order gains a project_id. | N-U16-201 |
| VDR-U16-C358 | FUNCTION MAPPING REQUIRED | project_purchase_stock/models/purchase_order.py:15 | project_id | FACT | project_purchase_stock installed | — | The receipt created for a purchase order with a project carries that project. | N-U16-201 |
| VDR-U16-C359 | FUNCTION MAPPING REQUIRED | project_purchase_stock/models/stock_rule.py:12 | project_id | FACT | project_purchase_stock installed | — | A purchase order created from a replenishment rule inherits the project from the procurement values. | N-U16-201 |
| VDR-U16-C360 | FUNCTION MAPPING REQUIRED | project_purchase_stock/models/stock_rule.py:17 | project_id | FACT | project_purchase_stock installed | — | Existing orders are reused only if they have the same project. | N-U16-201 |
| VDR-U16-C361 | FUNCTION MAPPING REQUIRED | project_stock/models/stock_picking.py:9 | project_id | FACT | project_stock installed | — | stock.picking gains a project_id. | N-U16-198 |
| VDR-U16-C362 | FUNCTION MAPPING REQUIRED | project_stock_account/models/stock_picking_type.py:9 | analytic_costs | FACT | project_stock_account installed | — | Operation type flag analytic_costs: validating pickings generates analytic entries for the selected project. | N-U16-198 |
| VDR-U16-C363 | FUNCTION MAPPING REQUIRED | project_stock_account/models/stock_move.py:25 | analytic_costs | FACT | project_stock_account installed | — | Moves create analytic entries only when the picking has a project and the operation type flag is on; moves without a picking are always processed. | N-U16-198 |
| VDR-U16-C364 | FUNCTION MAPPING REQUIRED | project_stock_account/models/stock_move.py:14 | _get_analytic_distribution | FACT | operation type analytic_costs | — | The move distribution is the project distribution, else the base empty distribution. | N-U16-198 |
| VDR-U16-C365 | FUNCTION MAPPING REQUIRED | project_stock_account/models/stock_move.py:21 | picking_entry | FACT | move with picking | — | Entries are named after the picking and categorised picking_entry. | N-U16-198 |
| VDR-U16-C366 | FUNCTION MAPPING REQUIRED | project_stock_account/models/stock_move.py:40 | linked to the stock picking | FACT | mandatory plans for stock_picking | — | Missing mandatory plans on the project raise a validation error before creating entries. | N-U16-202 |
| VDR-U16-C367 | FUNCTION MAPPING REQUIRED | project_stock_account/models/analytic_applicability.py:12 | stock_picking | FACT | project_stock_account installed | — | A new analytic applicability business domain stock_picking is added. | N-U16-202 |
| VDR-U16-C368 | FUNCTION MAPPING REQUIRED | stock_account/models/stock_move.py:632 | amount = self.value | FACT | move done | — | For done moves the entry amount is the move value and the quantity is the valued quantity. | N-U16-199 |
| VDR-U16-C369 | FUNCTION MAPPING REQUIRED | stock_account/models/stock_move.py:628 | standard_price | FACT | move picked, not done | — | Estimate uses the product standard price; the code comments that exact cost is not required for estimates. | N-U16-199 |
| VDR-U16-C370 | FUNCTION MAPPING REQUIRED | stock_account/models/stock_move.py:636 | amount = -amount | FACT | outgoing move | — | Outgoing moves give a negative amount, which the project reads as a cost. | N-U16-198 |
| VDR-U16-C371 | FUNCTION MAPPING REQUIRED | stock_account/models/stock_move.py:190 | _create_analytic_move | FACT | stock move done | — | Analytic entries for done moves are created at the end of _action_done in sudo. | N-U16-198 |
| VDR-U16-C372 | FUNCTION MAPPING REQUIRED | stock_account/models/stock_move.py:143 | _create_analytic_move | FACT | picked flag changed | — | Marking a move picked also creates (estimate) analytic entries. | N-U16-199 |
| VDR-U16-C373 | FUNCTION MAPPING REQUIRED | project_stock_account/models/project_project.py:31 | picking_entry | FACT | project_stock_account installed | — | Transfer costs on the dashboard are the picking_entry analytic lines of the project account. | N-U16-188 |
| VDR-U16-C374 | FUNCTION MAPPING REQUIRED | project_stock_account/models/project_project.py:54 | other_costs_aal | INFERENCE | project_stock_account installed | — | Transfer costs use section id other_costs but read the sequence of other_costs_aal, while timesheets also define other_costs; the label Materials is reused. | N-U16-208 |
| VDR-U16-C375 | FUNCTION MAPPING REQUIRED | project_stock_landed_costs/models/stock_landed_costs.py:12 | _get_analytic_distribution | FACT | landed cost on pickings | — | Landed cost valuation adjustment lines take the picking project's distribution when the landed cost targets pickings (adjacent to receipt landed-cost allocation; cost allocation itself is another unit). | N-U16-200 |
| VDR-U16-C376 | FUNCTION MAPPING REQUIRED | project_stock_landed_costs/models/stock_landed_costs.py:11 | target_model | FACT | landed cost | — | Applies only to the picking target model. | N-U16-200 |
| VDR-U16-C377 | FUNCTION MAPPING REQUIRED | project_hr_expense/models/project_project.py:77 | posted', 'in_payment', 'paid' | FACT | project_hr_expense installed | — | Expense costs count posted, in-payment and paid expenses whose distribution includes the project account. | N-U16-195 |
| VDR-U16-C378 | FUNCTION MAPPING REQUIRED | project_hr_expense/models/project_project.py:98 | amount_billed | FACT | project_hr_expense installed | — | Expense costs are the untaxed amount converted to the project currency, shown as billed negative. | N-U16-195 |
| VDR-U16-C379 | FUNCTION MAPPING REQUIRED | project_hr_expense/models/project_project.py:65 | expense_id | FACT | project_hr_expense installed | — | Move lines with an expense are excluded from vendor bills and purchase-bill items. | N-U16-195 |
| VDR-U16-C380 | FUNCTION MAPPING REQUIRED | project_hr_expense/models/project_project.py:111 | move_line_id.expense_id | FACT | project_hr_expense installed | — | Analytic lines from expense moves are excluded from the other-analytic items. | N-U16-195 |
| VDR-U16-C381 | FUNCTION MAPPING REQUIRED | project_sale_expense/models/project_project.py:71 | expense_data['revenues'] | FACT | project_sale_expense installed | — | With re-invoiced expenses the revenue side adds the order lines' to-invoice and invoiced amounts for expense products. | N-U16-195 |
| VDR-U16-C382 | FUNCTION MAPPING REQUIRED | project_sale_expense/models/project_project.py:100 | invoice_line_ids | FACT | project_sale_expense installed | — | Invoice lines of orders with project expenses are marked as already included so they are not counted again as customer invoice items. | N-U16-195 |
| VDR-U16-C383 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_project.py:408 | vendor_bill | FACT | sale_timesheet installed | — | Analytic lines of category vendor_bill are skipped, to avoid duplicates with re-invoice policies. | N-U16-196 |
| VDR-U16-C384 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_project.py:414 | # cost | FACT | sale_timesheet installed | — | Time entry negative amounts are costs; positive ones are revenues by billable type. | N-U16-196 |
| VDR-U16-C385 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_project.py:376 | Domain.AND | FACT | sale_timesheet installed | — | Analytic domain is project time entries plus lines tied to the project's order lines. | N-U16-196 |
| VDR-U16-C386 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_project.py:489 | project_id', '=', False | FACT | sale_timesheet installed | — | Other-analytic items in sale_timesheet add project_id = False so timesheets are not counted twice. | N-U16-197 |
| VDR-U16-C387 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/project_project.py:359 | Materials | INFERENCE | sale_timesheet installed | — | sale_timesheet labels other_costs as Materials and project_stock_account does the same with a lazy label; same id used for two sources. | N-U16-208 |
| VDR-U16-C388 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:815 | group_account_readonly | FACT | sale_project installed | — | Invoice and vendor bill stat buttons need accounting read access; sales buttons need sales all-leads access. | N-U16-206 |
| VDR-U16-C389 | FUNCTION MAPPING REQUIRED | project_purchase/models/project_project.py:148 | group_purchase_user | FACT | project_purchase installed | — | Purchase order links appear only for purchase users, accountants or readonly accountants. | N-U16-206 |
| VDR-U16-C390 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:717 | _convert | FACT | invoice items | — | Invoice balances are converted from company currency to project currency at the line date. | N-U16-210 |
| VDR-U16-C391 | FUNCTION MAPPING REQUIRED | project_account/models/project_project.py:43 | to_currency=self.currency_id | UNKNOWN | foreign currency | — | Differences from conversion at line date versus report date were not executed. | N-U16-211 |
| VDR-U16-C392 | FUNCTION MAPPING REQUIRED | project_account/models/project_project.py:50 | parent_state == 'draft' | FACT | vendor bill items | — | Draft bill lines count as to bill; posted ones as billed; cancelled lines are not selected by the domain (draft and posted only). | N-U16-203 |
| VDR-U16-C393 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:98 | ondelete='set null' | FACT | always | — | Deleting an analytic account sets project.account_id to null; panel items then drop out. | N-U16-205 |
| VDR-U16-C394 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:1047 | group_analytic_accounting | OBSERVATION | DB: restored database | — | The helper hint on the profitability panel depends on the analytic accounting group; in the restored DB that group has no direct members and is neither implied by the base user group nor in the superuser's group closure, so the analytic accounting feature is off. | N-U16-204 |
| VDR-U16-C395 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/hr_leave.py:13 | _validate_leave_request | FACT | project_timesheet_holidays installed | — | Leave validation generates timesheets before the base validation. | N-U16-212 |
| VDR-U16-C396 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/hr_leave.py:30 | time_type == 'other' | FACT | leave validation | — | No entry is created if the company has no internal project or time-off task, or the leave type is not counted as time. | N-U16-216 |
| VDR-U16-C397 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/hr_leave.py:81 | holiday_id | FACT | leave validation | — | Generated entries carry holiday_id, employee, project, task, account of the internal project, and hours per day. | N-U16-216 |
| VDR-U16-C398 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/hr_leave.py:40 | flexible_hours | FACT | flexible calendar | — | Flexible calendars use requested hours, half a day of hours-per-day, or a full day of hours-per-day. | N-U16-216 |
| VDR-U16-C399 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/hr_leave.py:103 | refused holidays | FACT | action_refuse | — | Refusal deletes the generated entries (holiday link cleared first). | N-U16-217 |
| VDR-U16-C400 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/hr_leave.py:111 | _action_user_cancel | FACT | user cancel | — | User cancellation also removes the entries; deletion of the leave does too. | N-U16-217 |
| VDR-U16-C401 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/hr_leave.py:131 | number_of_days == 0 | FACT | leave write | — | A leave whose duration becomes zero loses its entries. | N-U16-217 |
| VDR-U16-C402 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/account_analytic.py:46 | linked to time off requests | FACT | write on linked entry | — | Entries linked to leave cannot be written outside superuser; public holiday entries cannot be modified either. | N-U16-217 |
| VDR-U16-C403 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/account_analytic.py:34 | linked to global time off | FACT | unlink | — | Entries linked to public holidays cannot be deleted by hand. | N-U16-218 |
| VDR-U16-C404 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/account_analytic.py:51 | linked to a time off type | FACT | create | — | Manual creation on time-off tasks is refused outside superuser. | N-U16-219 |
| VDR-U16-C405 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/resource_calendar_leaves.py:206 | _generate_public_time_off_timesheets | FACT | public holiday create or edit | — | Public holidays generate entries per employee and working day, skipping days that already have an entry. | N-U16-218 |
| VDR-U16-C406 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/resource_calendar_leaves.py:162 | date_from <= day_date | FACT | global leave lines | — | Days already covered by validated personal leave get no public holiday entry. | N-U16-218 |
| VDR-U16-C407 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/resource_calendar_leaves.py:268 | global_leave_id | FACT | global leave edited | — | Editing dates or calendar of a global leave deletes its entries and regenerates them. | N-U16-218 |
| VDR-U16-C408 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/res_company.py:10 | leave_timesheet_task_id | FACT | always | — | Company field leave_timesheet_task_id (Time Off task) restricted to the internal project; the task is created with the internal project. | N-U16-225 |
| VDR-U16-C409 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:473 | _hourly_cost | INFERENCE | time-off entries | — | Time-off entries are normal timesheet entries on the internal project, so they receive the employee's hourly cost as amount and count in project cost. | N-U16-229 |
| VDR-U16-C410 | FUNCTION MAPPING REQUIRED | hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:33 | emp_cost | FACT | hr_timesheet_attendance installed | — | Report is an SQL view unioning attendances (worked hours at check-in date in the calendar timezone) and project time entries; cost = hours times employee hourly cost. | N-U16-213 |
| VDR-U16-C411 | FUNCTION MAPPING REQUIRED | hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:32 | total_difference | FACT | hr_timesheet_attendance installed | — | Difference is attendance minus timesheet hours; future-dated rows are excluded. | N-U16-213 |
| VDR-U16-C412 | FUNCTION MAPPING REQUIRED | hr_timesheet_attendance/security/hr_timesheet_attendance_report_security.xml:12 | employee_id', '=', user.employee_id.id | FACT | own timesheet group | — | Own rows for the own-timesheet group, all rows for approver and administrator; multi-company rule on the view. | N-U16-227 |
| VDR-U16-C413 | FUNCTION MAPPING REQUIRED | hr_timesheet_attendance/security/ir.model.access.csv:2 | access_hr_timesheet_attendance_report | OBSERVATION | DB: restored database | — | Restored DB: hr_timesheet_attendance owns 1 ACL row and 4 record rules, equal to source. | N-U16-227 |
| VDR-U16-C414 | FUNCTION MAPPING REQUIRED | project_sms/models/project_task.py:13 | _message_sms_with_template | FACT | project_sms installed, task has customer and stage template | RT | A text message is sent to the customer using the stage template on create and on stage change; sent through the mail thread SMS method, whose gateway is outside this module. | N-U16-220 |
| VDR-U16-C415 | FUNCTION MAPPING REQUIRED | project_sms/models/project_project.py:12 | stage_id.sms_template_id | FACT | project_sms installed | — | Same rule for projects, evaluated in sudo. | N-U16-220 |
| VDR-U16-C416 | FUNCTION MAPPING REQUIRED | project_sms/models/project_task.py:29 | sudo()._send_sms() | FACT | stage change | — | The task send runs in sudo because the template model is protected. | N-U16-231 |
| VDR-U16-C417 | FUNCTION MAPPING REQUIRED | project_sms/security/project_sms_security.xml:7 | project.task | FACT | project manager | — | Rule gives project managers create, write, delete on templates for task and project models only (read is not limited by this rule). | N-U16-228 |
| VDR-U16-C418 | FUNCTION MAPPING REQUIRED | project_sms/models/project_task.py:10 | _send_sms | UNKNOWN | SMS gateway | RT | Gateway delivery, credit and failure handling are outside this module and unverified. | N-U16-232 |
| VDR-U16-C419 | FUNCTION MAPPING REQUIRED | project_mail_plugin/controllers/project_client.py:25 | /mail_plugin/task/create | FACT | project_mail_plugin installed | RT | Task creation endpoint uses auth mode outlook and open cross-origin settings. | N-U16-230 |
| VDR-U16-C420 | FUNCTION MAPPING REQUIRED | project_mail_plugin/controllers/project_client.py:42 | user_ids | FACT | task_create | — | Created task has subject as name, body as description, project, partner and the caller as assignee; company comes from the partner. | N-U16-221 |
| VDR-U16-C421 | FUNCTION MAPPING REQUIRED | project_mail_plugin/controllers/project_client.py:49 | project.project | FACT | project_create | — | A project can be created from a name only. | N-U16-221 |
| VDR-U16-C422 | FUNCTION MAPPING REQUIRED | project_mail_plugin/controllers/mail_plugin.py:28 | has_access('create') | UNKNOWN | project_mail_plugin installed | RT | Authentication of the add-in and its rate limits live in the base mail plug-in module and were not traced. | N-U16-233 |
| VDR-U16-C423 | FUNCTION MAPPING REQUIRED | project_hr_skills/models/project_task.py:9 | user_skill_ids | FACT | project_hr_skills installed | — | Skills of assignees are exposed as a related field on tasks and in the task report; no accounting effect. | N-U16-214 |
| VDR-U16-C424 | FUNCTION MAPPING REQUIRED | project_todo/models/project_task.py:14 | not vals.get('project_id') | FACT | project_todo installed | — | A to-do is created with name from the first line of description (max 100 chars) or Untitled to-do. | N-U16-222 |
| VDR-U16-C425 | FUNCTION MAPPING REQUIRED | project_todo/models/project_task.py:24 | action_convert_to_task | FACT | to-do | — | Converting a to-do to a task copies the project company onto the task. | N-U16-222 |
| VDR-U16-C426 | FUNCTION MAPPING REQUIRED | project_todo/security/project_todo_security.xml:9 | project_id', '=', False | FACT | employees | — | Employees get full access only to their own private tasks. | N-U16-223 |
| VDR-U16-C427 | FUNCTION MAPPING REQUIRED | project_todo/security/ir.model.access.csv:3 | access_task_on_partner | OBSERVATION | DB: restored database | — | Restored DB: project_todo owns 4 ACL rows and 1 record rule; base users get full CRUD on tasks, task types, tags and the quick-activity wizard. | N-U16-223 |
| VDR-U16-C428 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/security/ir.model.access.csv:2 | access_account_analytic_account_leaves_manager | OBSERVATION | DB: restored database | — | Restored DB: project_timesheet_holidays owns 1 ACL row letting the time-off manager read analytic accounts. | N-U16-226 |
| VDR-U16-C429 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/hr_leave.py:138 | _unlink_timesheets | FACT | leave deleted | — | Deleting a leave removes its entries and re-checks missing public-holiday entries. | N-U16-224 |
| VDR-U16-C430 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:118 | attachment_ids | INFERENCE | always | — | Receipts are attached to the expense record itself (attachment_ids on hr.expense), so evidence travels with the amount through approval and posting. | N-U16-003 |
| VDR-U16-C431 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:142 | default='draft' | FACT | new expense | — | state defaults to draft on a new expense. | N-U16-014 |
| VDR-U16-C432 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1442 | accounting entry for approved | INFERENCE | action_post | — | Posting is gated on state approved, so accountants act only on approved expenses; approval precedes any ledger entry. | N-U16-027 |
| VDR-U16-C433 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_employee.py:59 | department_id.manager_id.user_id | FACT | approval routing | — | _get_expense_managers combines the expense approver, the parent manager's user and the department manager's user. | N-U16-038 |
| VDR-U16-C434 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1140 | _do_approve | INFERENCE | no approver or self approver | — | Auto-validated expenses go straight to _do_approve at submission, so no human review happens when no approver exists. | N-U16-043 |
| VDR-U16-C435 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1624 | _prepare_move_lines_vals | INFERENCE | employee-paid | — | Posting turns each expense into a receipt line with account, taxes and employee partner, recording cost, input tax and liability at acceptance rather than at payment. | N-U16-051 |
| VDR-U16-C436 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:476 | expense.state = 'posted' | FACT | employee-paid with receipt | — | A linked receipt in draft or not paid gives state posted (company-paid shortcut gives paid, see CAP-U16-04). | N-U16-061 |
| VDR-U16-C437 | FUNCTION MAPPING REQUIRED | hr_expense/models/hr_expense.py:1294 | Waiting Reimbursement | INFERENCE | dashboard | — | The dashboard bucket Waiting Reimbursement exists to show employees what has not been paid back yet. | N-U16-079 |
| VDR-U16-C438 | FUNCTION MAPPING REQUIRED | hr_expense/models/account_payment.py:10 | expense_ids | FACT | always | — | Payments reach the expense through the payment's move, so settlement reuses the payment engine. | N-U16-089 |
| VDR-U16-C439 | FUNCTION MAPPING REQUIRED | hr_expense/__manifest__.py:10 | reinvoice employee expenses | FACT | always | — | Module summary states that expenses are submitted, validated and re-invoiced. | N-U16-097 |
| VDR-U16-C440 | FUNCTION MAPPING REQUIRED | sale_expense/__manifest__.py:16 | sale_management | FACT | always | — | sale_expense depends on sale_management and hr_expense and auto-installs when both are present. | N-U16-109 |
| VDR-U16-C441 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/hr_timesheet.py:72 | hourly cost | FACT | always | — | Field help states the purpose of the hourly cost: to track the cost of time. | N-U16-116 |
| VDR-U16-C442 | FUNCTION MAPPING REQUIRED | hr_timesheet/__manifest__.py:22 | hr_hourly_cost | FACT | always | — | hr_timesheet depends on hr, hr_hourly_cost, analytic, project and uom. | N-U16-129 |
| VDR-U16-C443 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:38 | Invoice created from the timesheet | FACT | always | — | timesheet_invoice_id records which invoice took each time entry, giving the audit trail of what was billed. | N-U16-141 |
| VDR-U16-C444 | FUNCTION MAPPING REQUIRED | sale_timesheet/models/hr_timesheet.py:93 | _is_not_billed | FACT | always | — | An entry is read-only when it is billed (invoice present and not cancelled). | N-U16-152 |
| VDR-U16-C445 | FUNCTION MAPPING REQUIRED | sale_timesheet/__manifest__.py:16 | sale_project | FACT | auto_install | — | sale_timesheet depends on sale_project and hr_timesheet and is auto-installed. | N-U16-154 |
| VDR-U16-C446 | FUNCTION MAPPING REQUIRED | sale_project/models/project_project.py:32 | selected by default on the tasks | FACT | always | — | Project sale_line_id help: the order item is the default for tasks and timesheets of the project. | N-U16-165 |
| VDR-U16-C447 | FUNCTION MAPPING REQUIRED | sale_project/__manifest__.py:12 | project_account | FACT | auto_install | — | sale_project depends on sale_management, sale_service and project_account. | N-U16-180 |
| VDR-U16-C448 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:998 | get_panel_data | INFERENCE | project panel | — | The project panel gathers buttons, milestones and profitability for one project in a single call, so managers read profitability from one place. | N-U16-189 |
| VDR-U16-C449 | FUNCTION MAPPING REQUIRED | project_timesheet_holidays/models/hr_leave.py:18 | generated on leave validation | FACT | always | — | Docstring: time off generates timesheets on the internal project and the leave-timesheet task. | N-U16-215 |
