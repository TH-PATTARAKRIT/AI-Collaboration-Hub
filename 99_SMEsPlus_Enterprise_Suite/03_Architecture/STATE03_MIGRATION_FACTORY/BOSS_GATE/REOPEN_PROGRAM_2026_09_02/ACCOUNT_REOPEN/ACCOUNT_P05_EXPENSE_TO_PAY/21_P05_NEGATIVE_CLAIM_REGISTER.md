# 21 — P05 NEGATIVE CLAIM REGISTER

`LAYER 2 — AUDIT QUARANTINE`
Issued under the SMEsPlus Deep Research Negative Claim Control (`DR-NC-01`..`DR-NC-06`) and `EC-06`.

> `NO EVIDENCE FOUND ≠ FUNCTION DOES NOT EXIST.`

**Classes:** `A` verified absence *within a stated scope* · `B` not found in searched scope ·
`C` not yet searched · `D` unknown · `E` contradicted.
**`B`/`C`/`D` are never converted to `A`** — not by restatement, citation, or elapsed time.
Class `A` always travels with its scope. Every row states **PATH SET + PATTERN + UNIT**.

## 1. Declared Roots

| ID | Path | Population |
|---|---|---|
| `R1` | `ENT18/addons` | 790 modules (791 `__manifest__.py`; the extra is an embedded posbox copy) / ~16 680 py+xml+csv files |
| `R2` | `ENT18/addons_archive` | 959 modules / ~15 513 files. **Every module appears twice** (`X` and `X__dup_20260515_145439`); any count not de-duplicated is inflated ~2×. |
| `R3` | `CUSTOM/smeplus-custom/addons` | 65 `__manifest__.py` (68 directory entries) / ~854 files |
| `R4` | `LEGACY14/Odoo14/addons` | 127 modules / ~1935 files |

**UNIT** is declared per row. The primary research did not declare a unit on its first pass; Expert 2
raised that as a defect and it is corrected here.

## 2. Register

| ID | Negative claim | Roots | Pattern | Result | Class |
|---|---|---|---|---|---|
| `NC-01` | No petty-cash / imprest construct of any kind | `R1` | `petty\|imprest\|cash[ _-]?float\|float[ _-]?fund\|revolving[ _-]?fund`, `grep -rilE`, `*.py *.xml *.csv`, unit = file | 0 files | **B** |
| `NC-02` | Petty-cash tokens in `R2` are **chart-of-accounts template data only, no process model** | `R2` | as `NC-01` | 40 files across 15 l10n modules (each ×2 via `__dup_`), all `account.account`/`account.group` template CSVs plus one `res.city` row | **A** for "these hits are account-template data"; **B** for "no process model in `R2`" |
| `NC-03` | The petty-cash GL-redirection hook `_get_account_move_line_values` has no caller | `R1`+`R2` | literal token, all file types; variants also tried: `_get_account_move_line`, `account_move_line_values`, `move_line_values`, `_prepare_account_move_line`, `_prepare_move_line*` | 0 in `R1`+`R2`; present in `R4` in 3 modules | **A** for "no caller in the declared roots"; **B** for "no caller anywhere" |
| `NC-04` | No corporate-card **process model** (card master, statement import mapped to a card, cardholder allocation, clearing) | `R1`–`R4` | `corporate[ _-]?card\|company[ _-]?card\|purchas(ing)?[ _-]?card\|p[-_]card\|card[ _-]?clearing\|liability_credit_card`, unit = file | 22 / 26 / 0 / 0 — all `R1` hits are `liability_credit_card` account-type usages; all `R2` hits are l10n SAF-T/FEC/1099 exporters | **B** |
| `NC-05` | No module other than `hr_expense_petty_cash` touches `petty.cash`; no `ir.rule` for it anywhere; zero `company_id`/`check_company` in the module | `R3` | `_inherit\|_name = ["']petty\.cash`; `model_petty_cash`; `-i petty` ∩ `-i rule` over `*.xml`; `company_id` and `check_company` within the module. Unit = file over 5087 files | no other module; no rule; zero | **A** within `R3` |
| `NC-06` | `multi_level_approval` is not linked to `hr.expense` or `advance.expense.request` | `R3` | `grep -rn "multi_approval\|multi.approval"` in the two consuming modules; and the approval modules' `depends` | no dependency in either direction | **B** |
| `NC-07` | No cash-advance / expense-request construct in `R1`; advance constructs are **custom-only and absent from `R4`** — so `scgl_advance_expense_request` is net-new SMEsPlus code, not an OCA port | `R1`,`R3`,`R4` | `cash[ _-]?advance\|employee[ _-]?advance\|travel[ _-]?advance\|staff[ _-]?advance\|advance[ _-]?request\|expense[ _-]?request\|employee[ _-]?loan`, unit = file | 0 / 16 / **0** | **B** for `R1`; **A** for "absent from `R4`" |
| `NC-08` | No prepaid-expense mechanism in the P05 surface | `hr_expense`, `hr_expense_petty_cash`, `scgl_advance_expense_request` | `grep -rniE "prepaid\|prepay\|deferred"` over `*.py` | 0 | **B** |
| `NC-09` | No accrued-expense mechanism in the P05 surface | same three modules | `grep -rniE "accru"` over `*.py` | 0 | **B** |
| `NC-10` | Neither advance-clearing move builder handles currency | `scgl_advance_expense_request/models/account_move.py`, `wizard/advance_request_reconcile.py` | `grep -n "currency"`; both files also read in full | no match | **A** within those two files |
| `NC-11` | No close / cut-off routine in the P05 modules | `hr_expense`, `hr_expense_petty_cash`, `scgl_advance_expense_request` | `grep -rinE "close\|cutoff\|cut_off\|period_end"` over `*.py` | none functional | **B** |
| `NC-12` | No required-attachment (missing-receipt) control | `ENT18/addons/hr_expense` | `grep -rnE "attachment_ids"` and `grep -rniE "required.*receipt\|no.*receipt\|missing.*receipt"` | only duplicate detection and main-attachment selection | **B** |
| `NC-13` | `hr_expense` contains no WHT reference | `ENT18/addons/hr_expense` | `grep -rn "wt_tax\|withhold"` over `*.py *.xml` | 0 | **A** within the module |
| `NC-14` | No payment/move cancellation or reversal hook in any WHT module | the six WHT/deduction modules in `R3` | `grep -rn "def action_draft\|def action_cancel\|def button_cancel\|def button_draft\|_reverse_moves\|def unlink\|def action_reverse" --include='*.py'` | only the certificate's own buttons | **A** |
| `NC-15` | `wt_cert_cancel` is used nowhere as a constraint or cancellation guard | `R3` | `grep -rn "wt_cert_cancel" --include='*.py' --include='*.xml'`, `.git` excluded | 11 hits, all definition/compute/domain/`invisible="1"` | **A** |
| `NC-16` | Nothing validates that the payment difference equals the computed WHT | `l10n_th_withholding_tax/wizard/account_payment_register.py` | `grep -n "payment_difference"` | 0 | **A** within the file |
| `NC-17` | `full_payment_custom` prints no withholding disclosure | `CUSTOM/full_payment_custom/report` | `grep -nEi "wt_tax\|wht\|withhold"` over `*.xml` | 0 | **A** within the module |
| `NC-18` | `account_disallowed_expenses` writes nothing to the GL | `ENT18/addons/account_disallowed_expenses` | full read of `models/` + `report/`; `grep -n "def create\|def write\|def _post\|_prepare_.*_line"` | no write path to any journal | **A** |
| `NC-19` | `account_disallowed_expenses` has no connection to `hr_expense` | `ENT18/addons/hr_expense`, `hr_expense_extract` | `grep -rn "disallowed"` | 0 | **A** |
| `NC-20` | No disallowed-expense code in `R3` | `R3` | `grep -rlEi 'disallowed'` over `*.py *.xml *.csv` | 0 | **B** — spellings `non_deductible`, `add_back` and Thai-language tokens **not searched** (**C** for those) |
| `NC-21` | No model-level guard exists for `approval_state` | `R1` | `grep -rn "approval_state"` over `*.py *.xml`, i18n excluded, all 13 hits enumerated | none is a guard | **A** within `R1` |
| `NC-22` | No `@api.constrains` or `_sql_constraints` gates `currency_id`/`total_amount_currency`/`date`/`quantity`/`product_id` on `hr.expense` | the six `hr_expense*`/`sale_expense`/`project_hr_expense`/`hr_payroll_expense` modules | `grep -n "@api.constrains\|def _check"` + `grep -rn "_sql_constraints"` over `*.py` | none | **A** within those six; **B** for the rest of `R1` |
| `NC-23` | The advance module contains no `@api.constrains`, no `_sql_constraints`, no `check_company` | `scgl_advance_expense_request` | `grep -rn --include='*.py' -E "api\.constrains\|_sql_constraints\|check_company"` | 0 | **A** |
| `NC-24` | No `@api.depends` in the advance module references any `account.move` field or `move_lines_cleared` | `scgl_advance_expense_request` | `grep -rn --include='*.py' "@api.depends"` → 7 decorators, each inspected. Unit = decorator | none does | **A** |
| `NC-25` | `deduct_down_payments` has no live consumer | `R3` | `grep -rn --include='*.py' --include='*.xml' "deduct_down_payments"` | 4 hits; the sole consumer is commented out | **A** |
| `NC-26` | No live `hr_expense` integration in `scgl_advance_expense_request` | that module | `grep -rn --include='*.py' --include='*.xml' --include='*.csv' -E "hr\.expense\|hr_expense"` | manifest dependency + 2 commented imports + 1 comment | **A** |
| `NC-27` | No test in the WHT modules exercises `in_receipt`/`out_receipt`; no test exercises the shipped `active_model == 'account.move.line'` branch | the two WHT test files | `grep -nE "receipt\|move_type"`; `grep -n "active_model"` → 7 hits, **all** `"account.move"` | none / none | **A** within those two files |
| `NC-28` | `sale_expense` contains no `check_company` and no constraint | `ENT18/addons/sale_expense` | `grep -rnE "check_company\|@api\.constrains\|def _check_" --include='*.py'` | 0 | **A** within the module |
| `NC-29` | Only three `_alias_get_error` implementations exist; `alias_contact=='employees'` is handled solely by `hr/models/models.py:11-21` | `R1` | `grep -rn "def _alias_get_error" --include='*.py'` | 3 hits | **A** within `R1` |
| `NC-30` | No override re-imposes `_check_payable_receivable` for company-paid expense moves | the five `hr_expense`-family modules | `grep -rn "_check_payable_receivable" --include='*.py'` | none | **B** — `R2` not swept |
| `NC-31` | No test asserts immutability of expense amount after approval | `ENT18/addons/hr_expense/tests` | `grep -n "def test_"` across 6 files + full read of `test_expenses_access_rights.py:32-121` | none found | **B** — test bodies read selectively |
| `NC-32` | `sample` appears in no view file | `ENT18/addons/hr_expense_extract` | `grep -rn "sample"` over `*.py *.xml`, i18n and tests excluded | 0 in views | **A** within the module |
| `NC-33` | No Thai petty-cash account template | `R1` | `NC-01` pattern ∩ `l10n_th*` | 0 | **B** |

## 3. Contradicted Claims (class `E`)

| ID | Claim as originally made | Contradicting evidence | Class |
|---|---|---|---|
| `NC-E-01` | *"Thai WHT is silently skipped when a payment is registered from a vendor bill."* | `ENT18/account/models/account_move.py:5153-5161` → `line_ids.action_register_payment()`; `account_move_line.py:1112-1119` sets `active_model='account.move.line'`. Independently re-tested by Expert 4. | **E** |
| `NC-E-02` | *"`account.withholding.tax` has no ACL and no company rule."* | `security/ir.model.access.csv:2`; `security/security.xml:2-7`, `domain_force` at `:6`. Independently re-tested by Expert 4. | **E** |
| `NC-E-03` | *"A single expense report can mix `own_account` and `company_account` lines."* | `hr_expense_sheet.py:422-427` + `hr_expense.py:539-541` guard both directions. Expert 2 attacked this again from the petty-cash side and it survived. | **E** |
| `NC-E-04` | *"Petty cash, cash advance and corporate card do not exist in this system."* — the zero counts produced by the first, shell-mangled enumeration (`15 RE-06`). | `hr_expense_petty_cash` (15 files by py/xml/csv unit), `scgl_advance_expense_request` (16 files), the five Thai WHT modules — all in `R3`. | **E** |
| `NC-E-05` | *"`NC-01` holds across the whole reference tree."* — the primary research bounded it to `R1` only while declaring `R2` in its own path set. | `R2` yields 40 files across 15 l10n modules. **The claim was contradicted by a root inside its own declared path set.** Restated as `NC-02` it holds. Raised by Expert 2. | **E** |
| `NC-E-06` | *"No corporate-card construct exists."* | `account.journal.type` includes `('credit', 'Credit Card')` with `default_account_id_types['credit'] = 'liability_credit_card'`, auto-provisioning and a lookup (`ENT18/account/models/account_journal.py:98, 379, 767, 844`). Reachable from the company-paid expense path. Raised by Expert 2. Restated as `NC-04` (no *process model*) it holds. | **E** |

## 4. Unknowns Explicitly Held at `D`

| ID | Claim | Why it is `D` and not `A`/`B` |
|---|---|---|
| `NC-D-01` | The exact `payment_state` and residual outcome of a bill force-cancelled by a raw `state` write, and of a cross-currency clearing reconciliation | Expert 3 declined to trace it into `_compute_payment_state` / `_prepare_reconciliation_partials` and **refused to infer it**. `20 U-03`. |
| `NC-D-02` | Provenance (upstream OCA vs local) of the `l10n_th_withholding_tax_multi` and `account_payment_multi_deduction` defects | Neither module carries a `.git`, so committed and working-tree code cannot be separated. |
| `NC-D-03` | The rendered UI outcome of the certificate's `states=` / `readonly=True` contradiction (`TX-20`) | The code contradiction is class `A`; the rendered behaviour was not executed. |
| `NC-D-04` | Whether `l10n_th_withholding_tax_multi` and `account_disallowed_expenses` are actually installed | Not readable from a source tree. Subsumed by `20 U-01`. |

## 5. Statutory Claims Held

Per Clean Room Learning Directive v2.0, Thai statutory assertions are `HOLD / EVIDENCE REQUIRED` and
routed to the Accounting-Tax track (`12 D-05`). Held items: the statutory consequence of `TX-01`
(two subsystems filling one return), `TX-12`/`TX-13` (certificate lifecycle), `TX-15`/`TX-16`
(report population and void-row convention), `TX-19` (exported text file format), `TX-20`
(certificate date vs filing period), `TX-24` (add-back obligation).
**No statutory rule is asserted anywhere in this package from memory.**

## 6. Compliance Statement

- No `B`, `C` or `D` claim in this register has been upgraded to `A`.
- Every `A` claim states its scope, and the scope travels with it into every summary that cites it.
- Six claims are recorded as **contradicted** (`§3`); four of the six were the primary research's own,
  and two of those were caught only by independent review.
- A mechanical scan for over-scoped negatives was run across the package: see `18 §5`.
