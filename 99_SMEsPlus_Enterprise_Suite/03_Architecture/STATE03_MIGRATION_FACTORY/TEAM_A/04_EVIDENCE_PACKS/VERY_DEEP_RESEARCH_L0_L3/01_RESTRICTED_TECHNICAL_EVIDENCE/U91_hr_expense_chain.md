# U91 — HR Expense + Project Expense → Invoice (L3/L4)
**Unit**: U91
**Phase**: Second-Pass Depth Closure — P2 Supporting Domains
**Scope**: hr.expense states, sheet approval, account.move posting, project integration, billable customer invoicing
**Modules**: hr_expense, project_hr_expense, project_sale_expense, sale_expense
**Function-IDs targeted**: NEW:U91-F01 through U91-F20
**L-levels**: L3, L4
**Proof layers**: P4
**Date**: 2026-10-02
**Status**: GATE-PASS
**Predecessor**: U16, U87

---

## Claims

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| U91-001 | U91-F01 | hr_expense/models/hr_expense.py:43 | `_name = 'hr.expense'` | DEF | | | The primary expense record model is named `hr.expense`; it inherits `mail.thread.main.attachment`, `mail.activity.mixin`, `analytic.mixin` | NR-U91-001 |
| U91-002 | U91-F01 | hr_expense/models/hr_expense.py:124 | `state = fields.Selection(` | SCHEMA | | | `hr.expense.state` is a computed stored Selection with values: draft, submitted, approved, posted, in_payment, paid, refused | NR-U91-002 |
| U91-003 | U91-F01 | hr_expense/models/hr_expense.py:145 | `approval_state = fields.Se` | SCHEMA | | | A separate `approval_state` field carries the approval workflow values: submitted, approved, refused; `state` is derived from it | NR-U91-003 |
| U91-004 | U91-F01 | hr_expense/models/hr_expense.py:17 | `EXPENSE_APPROVAL_STATE = [` | CONST | | | The constant `EXPENSE_APPROVAL_STATE` defines the three approval-step values: ('submitted','Submitted'), ('approved','Approved'), ('refused','Refused') | NR-U91-004 |
| U91-005 | U91-F02 | hr_expense/models/hr_expense.py:454 | `def _compute_state(self):` | DEF | | C1 | `_compute_state` derives `hr.expense.state` from `account_move_id.state`, `account_move_id.payment_state`, and `approval_state`; no move → state equals approval_state or 'draft' | NR-U91-005 |
| U91-006 | U91-F02 | hr_expense/models/hr_expense.py:487 | `expense.state = expense.app` | ASSIGN | When account_move_id is False | | When no account move is linked, state is set to `approval_state` or falls back to 'draft' | NR-U91-006 |
| U91-007 | U91-F02 | hr_expense/models/hr_expense.py:474 | `expense.state = 'paid'` | ASSIGN | When payment_mode == 'company_account' and move exists | | Company-paid expenses jump directly to 'paid' state once any account.move is linked | NR-U91-007 |
| U91-008 | U91-F03 | hr_expense/models/hr_expense.py:1127 | `def action_submit(self):` | DEF | | | `action_submit` transitions a draft expense: sets `approval_state = 'submitted'` unless it can be auto-validated, in which case `_do_approve()` is called directly | NR-U91-008 |
| U91-009 | U91-F03 | hr_expense/models/hr_expense.py:1143 | `def _can_be_autovalidated` | DEF | | | An expense can be auto-validated (skip submit step) if the manager_id is absent or equals the employee's own user | NR-U91-009 |
| U91-010 | U91-F04 | hr_expense/models/hr_expense.py:1148 | `def action_approve(self):` | DEF | | | `action_approve` calls `_do_approve()`, which writes `approval_state = 'approved'` and records the approval datetime; duplicate-expense wizard may intercept | NR-U91-010 |
| U91-011 | U91-F04 | hr_expense/models/hr_expense.py:1456 | `'approval_state': 'approved` | ASSIGN | Inside _do_approve | | `_do_approve` writes approval_state='approved', manager_id=current user, and approval_date=now() for every expense in submitted or draft state | NR-U91-011 |
| U91-012 | U91-F05 | hr_expense/models/hr_expense.py:1163 | `def action_post(self):` | DEF | | | `action_post` is the posting entry point; requires state == 'approved' (guard in `_check_can_create_move`); routes to `_create_company_paid_moves` or `_post_without_wizard` based on payment_mode | NR-U91-012 |
| U91-013 | U91-F05 | hr_expense/models/hr_expense.py:1440 | `def _check_can_create_move` | GUARD | | | Guard raises UserError if any expense.state != 'approved'; posting is blocked for non-approved expenses | NR-U91-013 |
| U91-014 | U91-F06 | hr_expense/models/hr_expense.py:1619 | `'move_type': 'in_receipt',` | ASSIGN | Employee-paid expenses (_post_without_wizard) | | Employee-paid expenses create an `account.move` of type `in_receipt` (vendor receipt); partner is employee's work_contact_id | NR-U91-014 |
| U91-015 | U91-F06 | hr_expense/models/hr_expense.py:1727 | `'account_id': self._get_base` | ASSIGN | In _prepare_move_lines_vals | | Expense move line uses `_get_base_account()`: resolves to expense's own account_id, then product expense account, then company expense account | NR-U91-015 |
| U91-016 | U91-F06 | hr_expense/models/hr_expense.py:1805 | `account_dest = partner.prop` | ASSIGN | Employee-paid, _get_expense_account_destination | | For employee-paid expenses, the destination account (payable/outstanding) is `partner.property_account_payable_id`; this is the CR side of the vendor receipt move | NR-U91-016 |
| U91-017 | U91-F07 | hr_expense/models/hr_expense.py:1577 | `def _create_company_paid_m` | DEF | payment_mode == 'company_account' | | Company-paid expenses create an `account.payment` and linked `account.move`; the payment is posted via `origin_payment_id.action_post()` | NR-U91-017 |
| U91-018 | U91-F07 | hr_expense/models/hr_expense.py:1582 | `self.with_context(clean_con` | ASSIGN | In _create_company_paid_moves | | `project_id` is explicitly cleared from context when creating company-paid moves to avoid default project-field injection | NR-U91-018 |
| U91-019 | U91-F08 | hr_expense/models/account_move.py:12 | `expense_ids = fields.One2ma` | SCHEMA | | | `account.move` has a One2many `expense_ids` field pointing back to `hr.expense.account_move_id`; the inverse relation is bidirectional | NR-U91-019 |
| U91-020 | U91-F08 | hr_expense/models/account_move_line.py:10 | `expense_id = fields.Many2on` | SCHEMA | | | `account.move.line` carries a `expense_id` Many2one back to `hr.expense`; used for reinvoice determination and analytic line filtering | NR-U91-020 |
| U91-021 | U91-F09 | project_hr_expense/models/hr_expense.py:4 | `class HrExpense(models.Mode` | INHERIT | | | Module `project_hr_expense` extends `hr.expense`; when `project_id` context is present, `analytic_distribution` is seeded from the project's analytic account | NR-U91-021 |
| U91-022 | U91-F09 | project_hr_expense/models/hr_expense.py:12 | `analytic_distribution = sel` | ASSIGN | context project_id set | | The project's `_get_analytic_distribution()` is used to pre-populate expense analytic_distribution when creating expenses from a project context | NR-U91-022 |
| U91-023 | U91-F10 | project_hr_expense/models/project_project.py:44 | `return self._get_expense_ac` | RETURN | | | Project links to expenses via analytic_distribution containing the project's analytic account id; there is no direct project_id field on hr.expense | NR-U91-023 |
| U91-024 | U91-F10 | project_hr_expense/models/project_project.py:75 | `('analytic_distribution', 'i` | FLOW | In _get_expenses_profitability_items | | Project profitability items for expenses are filtered by matching analytic_distribution to project account_id; state must be in ['posted','in_payment','paid'] | NR-U91-024 |
| U91-025 | U91-F11 | sale_expense/models/hr_expense.py:9 | `sale_order_id = fields.Many` | SCHEMA | | | Module `sale_expense` adds `sale_order_id` Many2one (to `sale.order`) and `sale_order_line_id` Many2one (to `sale.order.line`) to `hr.expense` for billable reinvoicing | NR-U91-025 |
| U91-026 | U91-F11 | sale_expense/models/hr_expense.py:29 | `can_be_reinvoiced = fields.B` | SCHEMA | | | `can_be_reinvoiced` is True when `product_id.expense_policy` is in {'sales_price', 'cost'}; gates availability of the sale_order_id field | NR-U91-026 |
| U91-027 | U91-F11 | sale_expense/models/hr_expense.py:70 | `def action_post(self):` | OVERRIDE | | | `sale_expense` overrides `action_post`: if `sale_order_id` is set but `analytic_distribution` is empty, an analytic account is created from the SO and assigned | NR-U91-027 |
| U91-028 | U91-F12 | sale_expense/models/account_move_line.py:14 | `if self.expense_id:` | GUARD | In _sale_can_be_reinvoice | | The reinvoice check uses `expense_id` on `account.move.line`; reinvoice is enabled when `expense_policy` in {'sales_price','cost'} AND `sale_order_id` is set AND line is a product line | NR-U91-028 |
| U91-029 | U91-F12 | sale_expense/models/account_move_line.py:22 | `mapping_from_expense[move_l` | ASSIGN | In _get_so_mapping_from_expense | | When creating the SO line for reinvoice, the target sale.order is taken directly from `expense_id.sale_order_id` on the move line | NR-U91-029 |
| U91-030 | U91-F12 | sale_expense/models/account_move_line.py:39 | `'expense_ids': [Command.set` | ASSIGN | In _sale_prepare_sale_line_values | | A new `sale.order.line` created for expense reinvoice includes `expense_ids` linking it back to the originating `hr.expense` record | NR-U91-030 |
| U91-031 | U91-F13 | sale_expense/models/sale_order_line.py:9 | `expense_ids = fields.One2ma` | SCHEMA | | | `sale.order.line` gains a One2many `expense_ids` back to `hr.expense.sale_order_line_id`; this is the SOL↔expense link used for re-invoice tracking | NR-U91-031 |
| U91-032 | U91-F14 | sale/models/product_template.py:22 | `expense_policy = fields.Sel` | SCHEMA | | | `expense_policy` on `product.template` has three values: 'no' (no reinvoice), 'cost' (at cost), 'sales_price' (at sales price); default is 'no' | NR-U91-032 |
| U91-033 | U91-F15 | project_sale_expense/models/hr_expense.py:39 | `def action_post(self):` | OVERRIDE | | | Module `project_sale_expense` further overrides `action_post`: if `sale_order_id.project_id` exists but expense has no analytic_distribution, it creates/assigns the project analytic account | NR-U91-033 |
| U91-034 | U91-F15 | project_sale_expense/models/hr_expense.py:31 | `expense.analytic_distributi` | ASSIGN | In _compute_analytic_distribution, project+SO overlap | | When both a project analytic and an expense analytic are present without plan overlap, `project_sale_expense` merges both distributions; project plan takes priority on conflict | NR-U91-034 |
| U91-035 | U91-F16 | hr_expense/models/hr_expense.py:246 | `payment_mode = fields.Selec` | SCHEMA | | | `payment_mode` on `hr.expense` has two values: 'own_account' (employee reimburse) and 'company_account' (company paid); drives the entire posting path fork | NR-U91-035 |
