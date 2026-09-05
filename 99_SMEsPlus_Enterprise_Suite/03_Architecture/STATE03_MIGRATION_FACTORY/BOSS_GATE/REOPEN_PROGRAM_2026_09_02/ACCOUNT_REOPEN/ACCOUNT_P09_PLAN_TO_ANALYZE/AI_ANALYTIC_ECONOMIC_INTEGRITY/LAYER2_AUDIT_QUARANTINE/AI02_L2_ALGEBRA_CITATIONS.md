# AI02-L2 — ALGEBRA CALL CHAIN AND CITATIONS (LAYER 2 — AUDIT QUARANTINE)

**Boss / PMO / AI-Audit only.** Nothing here may be transcribed into a Layer 1 document.
Repository: reference ERP enterprise build `18.0+e.20250608`. Root: `<ref>/odoo/addons/`.

## 1. THE CALL CHAIN

| # | Module | File | Line | Symbol | What it does |
|---|---|---|---|---|---|
| 1 | `account` | `models/account_move.py` | 4939 | inside `_post` | `to_post.line_ids._create_analytic_lines()` — invoked over the entry's **entire** row set, no `filtered()` |
| 2 | `account` | `models/account_move_line.py` | 3149-3159 | `_create_analytic_lines` | calls `_validate_analytic_distribution()` then `for line in self: … _prepare_analytic_lines()`; single batched create at 3159 |
| 3 | `account` | `models/account_move_line.py` | 3116-3147 | `_validate_analytic_distribution` | **line 3118**: `for line in self.filtered(lambda line: line.display_type == 'product')` — the row-type gate, and it gates only the *complaint*, not creation |
| 4 | `analytic` | `models/analytic_mixin.py` | 162-176 | `_validate_distribution` | first statement `if self.env.context.get('validate_analytic', False)` — the context gate |
| 5 | `account` | `models/account_move_line.py` | 3161-3172 | `_prepare_analytic_lines` | **3164** `if self.analytic_distribution:` — the ONLY eligibility test; **3170** `if not self.currency_id.is_zero(line_values.get('amount'))` — zero-amount suppression |
| 6 | `account` | `models/account_move_line.py` | 3174-3206 | `_prepare_analytic_distribution_line` | **3187** `amount = -self.balance * distribution / 100.0`; **3185** the 100 %-completion remainder branch; **3200** `general_account_id = self.account_id.id`; **3202** `move_line_id = self.id` |
| 7 | `account_asset` | `models/account_move.py` | 261-315 | `_prepare_move_for_asset_depreciation` | builds exactly two rows; **277-285** row 1 on `account_depreciation_id`, credit for a positive amount; **286-294** row 2 on `account_depreciation_expense_id`, debit; **295-299** the guard and the assignment of the allocation to **both** rows |

## 2. THE TWO ABSENCES (A1 / A2 IN LAYER 1)

- **A1** — no account-type test on the creation path. Pattern `account_type` over `account/models/account_move_line.py` returns no hit inside `_prepare_analytic_lines`, `_prepare_analytic_distribution_line` or `_create_analytic_lines`. `NOT FOUND IN SCOPE: account/models/account_move_line.py:3149-3206, pattern "account_type"` — class **A** (the three functions read in full).
- **A2** — the row-type test at 3118 lives in the validation routine, which is invoked at 3152 **before** the creation loop at 3154 and does not filter the recordset the loop iterates. Class **A** (both functions read in full).

## 3. THE SOURCE COMMENT AT THE HEART OF THE DEFECT

`account_asset/models/account_move.py:295-296` carries a two-line comment stating that the allocation key is set only when the asset has one, because otherwise it would prevent the computation of the allocation. **The comment explains the `if`; it does not explain why both rows receive it.** No comment anywhere in the function addresses the balance-sheet leg.

## 4. VERIFICATION PERFORMED BY THE LEAD SESSION
All seven chain locations were read directly in this continuation, not inherited from the base package or from the P04 report. The two-row structure and the both-rows assignment were read in one contiguous block (261-315).

## 5. SEARCH BOUNDARY
`awk` range reads of `account_move_line.py:3112-3206`, `account_asset/models/account_move.py:255-320`, `account_budget/reports/budget_report.py:49-95`; `grep -rn "_create_analytic_lines" <root> --include="*.py" | grep -v /tests/` (4 hits, all recorded above or in the base package). No database executed.
