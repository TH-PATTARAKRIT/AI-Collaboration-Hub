# 06 — P05 ANALYTIC HANDOFF

`LAYER 2 — AUDIT QUARANTINE`

## 1. Where Analytic Distribution Is Set

| Stage | Mechanism | Citation |
|---|---|---|
| Default | `_compute_analytic_distribution` queries the distribution-model engine with product, product category, the employee's work contact, the contact's categories, the account **code prefix** and the company | `hr_expense.py:516-527` |
| Override | The computed value is kept only if the engine returns nothing: `expense.analytic_distribution = distribution or expense.analytic_distribution` | `hr_expense.py:527` |
| Edit gate | Writing `analytic_distribution` requires `is_editable` | `hr_expense.py:631-633` |
| Validation | `_validate_analytic_distribution` runs at approval, per line, with `business_domain='expense'` | `hr_expense_sheet.py:575, 863-865` |
| Department | `hr_department` carries an analytic account; `analytic.py` (45 lines) and `hr_department.py` (16 lines) extend the plan | `hr_expense/models/analytic.py`, `models/hr_department.py` |

## 2. Where It Reaches the Ledger

| Branch | Debit (expense) line | Tax lines | Credit line |
|---|---|---|---|
| `own_account` | **carried** — `analytic_distribution` in `_prepare_move_lines_vals` | not carried | not carried |
| `company_account` | **carried** — `base_line['analytic_distribution']` | not carried | not carried |
| Advance disbursement | **NOT carried** — `invoice_line_ids` vals contain no `analytic_distribution` | n/a | n/a |
| Advance liquidation (both paths) | **NOT carried** | n/a | n/a |
| Petty cash float top-up | **NOT carried** | n/a | n/a |

Citations: `hr_expense.py:1015`, `hr_expense.py:916`, `advance_expense_request.py:248-257`,
`advance_request_reconcile.py:64-77`, `scgl_advance_expense_request/models/account_move.py:87-106`,
`hr_expense_petty_cash/models/account_move.py:102-110`.

## 3. Findings

| ID | Finding | Class |
|---|---|---|
| `AN-01` | Analytic distribution reaches the ledger on the **expense debit line only**. Tax lines and the payable/outstanding credit line carry none. Any analytic report that sums a full entry will not balance by analytic dimension. | FACT VERIFIED |
| `AN-02` | The whole advance chain — disbursement, both liquidation paths, and the petty cash float — carries **no** analytic dimension at all. A cost funded through an advance is invisible to project/department analytics until (and unless) it is re-entered as an expense claim. Declared boundary: the five files cited in §2, pattern `grep -n "analytic"` → no match in the vals construction. Class **A** (verified absence within the stated files). | FACT VERIFIED |
| `AN-03` | The default distribution keys on `account_id.code` — the **chart code prefix** (`hr_expense.py:524`). Analytic allocation is therefore coupled to chart numbering. Renumbering a chart silently re-routes analytics. | FACT VERIFIED |
| `AN-04` | The default keys on `employee_id.work_contact_id` and its `category_id`, not on the employee record, the department or the cost centre. Employee-driven analytics must be modelled on the contact, not the employee. | FACT VERIFIED |
| `AN-05` | `_validate_analytic_distribution` runs at **approval**, i.e. at the same moment the entry is created. There is no validation at submission, so an invalid distribution is discovered only by the approver. | FACT VERIFIED |
| `AN-06` | `_compute_analytic_distribution` depends on `product_id`, `account_id`, `employee_id` but the engine call also uses `company_id` (`hr_expense.py:525`), which is not in the depends. Changing company does not re-derive the distribution. | FACT VERIFIED |

## 4. Handoff Contract to Core Accounting

For P11 / Core Reconciliation, the analytic handoff supplies:

| Element | Suppliable from P05? | Note |
|---|---|---|
| Cost by department | **Conditional** | Only for costs entered as expense claims; not for advance-funded costs (`AN-02`) |
| Cost by project | **Conditional** | Same condition; `project_hr_expense` presence unverified (`U-01`) |
| Full-entry analytic balance | **NO** | Credit and tax sides carry no distribution (`AN-01`) |
| Analytic on re-invoiced expense | **NOT SEARCHED** | `sale_expense` not examined this round — `20 U-05`, class **C** |
