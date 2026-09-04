# 01 — P05 PROCESS MAP + BUSINESS EVENT REGISTER

`LAYER 2 — AUDIT QUARANTINE`
Session `SMEPLUS-26-09-04-ACC-P05-E2P-REV2-001`

## 1. Scope Bounding (`EC-01`)

### 1.1 Declared Path Set

| Root ID | Path | Modules |
|---|---|---|
| `ENT18` | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons` | 790 |
| `ARC18` | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons_archive` | 959 |
| `CUSTOM` | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/EXTRA MODULE/smeplus-custom/addons` | 68 entries |
| `LEGACY14` | `/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo14/addons` | 127 entries |

**Denominator command (reproducible):**
`find "<ENT18 parent>" -name '__manifest__.py' | wc -l` → `1753`
`find "<ENT18 parent>" -name '__manifest__.py' | sed 's|/[^/]*/__manifest__.py$||' | sort | uniq -c`
→ `959 addons_archive`, `790 addons`, `3 odoo/`, `1 point_of_sale/tools/posbox/...`

**UNIT** = one directory containing a `__manifest__.py`.
**PATTERN** = literal filename `__manifest__.py`, no name filtering.
**INDEPENDENCE CAVEAT — DISCHARGED, WITH A DEFECT FOUND.** The path set above was chosen by this
session, so it was not independent of the claims it bounds. AAS-03 Expert 2 re-derived it with its own
patterns and confirmed the module counts, while finding three defects in the primary research's
enumeration: (i) **no UNIT was declared**, so its file counts were not comparable to anyone else's;
(ii) `find -name '__manifest__.py'` returns 791 for `addons`, not 790, because of an embedded copy at
`point_of_sale/tools/posbox/.../addons`; (iii) `CUSTOM` has **65** manifests against 68 directory
entries. Most importantly, Expert 2 established that a negative claim the primary research had bounded
to `ENT18/addons` is **contradicted by `addons_archive`** — a root inside its own declared path set
(`21 NC-E-05`). Corrected populations and units are carried in `21 §1`.

### 1.2 P05 Material Module Population

Selection pattern, declared:
`P1` = `grep -rlE "_name *= *['\"](hr\.expense)" <root>/*/models/*.py`
`P2` = `grep -rlE "'hr_expense'" <root>/*/__manifest__.py`
`P3` = `ls <root> | grep -E "^hr_expense"`
`P4` = `grep -rilE "petty[ _-]?cash|cash[ _-]?advance|withhold|\bwht\b|advance" <root> --include='*.py' --include='*.xml'`

| Module | Root | Role in P05 | Installed? |
|---|---|---|---|
| `hr_expense` | ENT18 | Expense capture, report, approval, GL creation | Assumed — `UNKNOWN / D` |
| `hr_expense_extract` | ENT18 | OCR receipt ingestion | `UNKNOWN / D` |
| `hr_expense_predict_product` | ENT18 | Category prediction | `UNKNOWN / D` |
| `sale_expense` | ENT18 | Re-invoice expense to customer | `UNKNOWN / D` |
| `project_hr_expense` | ENT18 | Project analytic link | `UNKNOWN / D` |
| `hr_payroll_expense` | ENT18 | Reimbursement via payroll | `UNKNOWN / D` |
| `documents_hr_expense` | ENT18 | Document workflow | `UNKNOWN / D` |
| `account` | ENT18 | Move, payment, reconciliation, lock dates | Required |
| `account_payment` | ENT18 | Payment method lines | Required |
| `account_disallowed_expenses` | ENT18 | Non-deductible % treatment | `UNKNOWN / D` — see `07` |
| `hr_expense_petty_cash` | CUSTOM | Adds `petty_cash` payment mode | `UNKNOWN / D` |
| `hr_expense_sequence` | CUSTOM | Expense report numbering | `UNKNOWN / D` |
| `scgl_advance_expense_request` | CUSTOM | Employee advance request + liquidation | `UNKNOWN / D` |
| `scgl_purchase_advance_payment` | CUSTOM | Vendor advance payment | `UNKNOWN / D` |
| `l10n_th_withholding_tax` (+`_multi`,`_cert`,`_cert_form`,`_report`) | CUSTOM | Thai WHT | `UNKNOWN / D` |
| `account_payment_multi_deduction` | CUSTOM | Multi-deduction payment register | `UNKNOWN / D` |
| `multi_level_approval` (+`_configuration`,`_hr`) | CUSTOM | Sequential multi-level approval | `UNKNOWN / D` |
| `full_payment_custom`, `print_voucher_request`, `print_payment_remittance_adviec` | CUSTOM | Settlement documents | `UNKNOWN / D` |

> **`GATING UNKNOWN U-01`** — Which of the above are actually deployed is not determinable from any
> source tree. Three near-identical copies of the custom addon set exist at differing version strings
> (`smeplus-custom`, `Odoo18/t8master/custom/addons`, `CLAUDE AI/MIGRATION/ODOO18/18.0.4_smeplus_v2`).
> Every finding in this package is therefore **conditional on the installed module set**. Routed to
> `20_P05_UNRESOLVED_REGISTER.md` as `U-01`, and it is **gating** for any statement about the
> as-operated system (as opposed to the as-written source).

## 2. Business Event Register

`BE-nn` = a fact that happens in the business. `ONE FACT → ONE EVENT OWNER → ONE ACCOUNTING EFFECT`
is asserted per row; violations are flagged and carried to `11_CONTRADICTION_REGISTER`.

| ID | Business Event | Event Owner (single) | Trigger | Accounting Effect | Owner Integrity |
|---|---|---|---|---|---|
| `BE-01` | Expense Request raised (pre-spend authorisation) | `advance.expense.request` (CUSTOM) | User submits request | **NONE** at request | OK |
| `BE-02` | Expense Request approved | `advance.expense.request` | Named approver acts | **NONE** at approval | OK |
| `BE-03` | Advance disbursement authorised | `advance.expense.request` | `button_post_bill` | Creates + posts a vendor bill | **VIOLATION** — see `EX-01` |
| `BE-04` | Advance paid to employee | `account.payment` | Payment registration | Settles employee payable | OK |
| `BE-05` | Employee incurs cost, obtains evidence | `hr.expense` | Manual / e-mail / OCR | **NONE** at capture | OK |
| `BE-06` | Expenses grouped into a claim | `hr.expense.sheet` | Submit | **NONE** at submit | OK |
| `BE-07` | Claim approved | `hr.expense.sheet` | `_do_approve` | **Creates the journal entry (draft)** | **VIOLATION** — see `EX-02` |
| `BE-08` | Claim posted | `account.move` / `account.payment` | `action_sheet_move_post` | Posts the entry | OK |
| `BE-09` | Employee reimbursed | `account.payment` | Payment registration | Settles employee payable | OK |
| `BE-10` | Company-paid cost logged | `account.payment` (one per line) | `_do_approve` | Outstanding-account credit | **VIOLATION** — see `EX-03` |
| `BE-11` | Petty cash float replenished | `account.move` (`is_petty_cash`) | Manual bill | Debits petty cash account | OK |
| `BE-12` | Petty cash spent | `hr.expense` `payment_mode='petty_cash'` | Claim approval | **DISPUTED** — see `EX-04` | **VIOLATION** |
| `BE-13` | Advance liquidated against actual cost | `advance.request.reconcile` wizard | Manual | Offsets advance vs vendor bill | OK |
| `BE-14` | Unused advance returned in cash | `advance.expense.clear.wizard` | Manual | DR cash / CR advance line-0 account | **VIOLATION** — see `EX-05` |
| `BE-15` | WHT withheld at settlement | `account.payment.register` | Payment registration | Write-off line to WHT account | OK |
| `BE-16` | WHT certificate issued | `withholding.tax.cert` | Manual | **NONE** (document only) | OK — pending `16 §4` |
| `BE-17` | Claim refused after approval | `hr.expense.sheet._do_refuse` | Approver | **Deletes the draft entry** | **VIOLATION** — see `EX-06` |
| `BE-18` | Claim reset to draft after posting | `hr.expense.sheet.action_reset_expense_sheets` | User with reset right | Reverses, then **detaches** entries | **VIOLATION** — see `EX-07` |
| `BE-19` | Advance request reset / rejected after billing | `advance.expense.request` | Requester / approver | **Direct `state='cancel'` write on moves** | **VIOLATION** — see `EX-08` |
| `BE-20` | Expense line edited after posting | `hr.expense.write` | Any editor | **No propagation to the posted entry** | **VIOLATION** — see `EX-09` |

## 3. Single-Owner Violations (`EX-nn`)

| ID | Violation | Evidence | Severity |
|---|---|---|---|
| `EX-01` | The advance request is simultaneously the requisition document, the approval document **and** the accounting document. It creates AND posts a vendor bill from its own button with no separate accounting event owner and no state assertion in Python. | `CUSTOM/scgl_advance_expense_request/models/advance_expense_request.py:239-273` | HIGH |
| `EX-02` | The accounting event is emitted by the **approval** transition, not by a posting transition. `_do_approve` calls `_do_create_moves()` before `approval_state` is written, under `sudo()`, explicitly so that approvers without accounting rights can create entries. | `ENT18/hr_expense/models/hr_expense_sheet.py:711-721`, `746-760` | HIGH |
| `EX-03` | One claim produces **N** accounting objects on the company-paid branch — the loop is over `expense_line_ids`, not over sheets. Cardinality of the accounting fact does not equal cardinality of the business fact. | `ENT18/hr_expense/models/hr_expense_sheet.py:763-767` | MEDIUM |
| `EX-04` | Petty cash claims are routed through the employee-reimbursement branch; the only code that would redirect the credit to the petty cash account targets a method absent from this platform version. **Upheld on four independent lines by AAS-03 Expert 2 — see `05 §6`.** A **second** dead path exists in the same module: the holder's journal never reaches the bill either (`E2-01`). | `CUSTOM/hr_expense_petty_cash/models/hr_expense_sheet.py:96`; `.../hr_expense.py:72-79`; token absent from `ENT18` — see `21 NC-03` | **TOLERANCE-ZERO** |
| `EX-05` | Cash returned by an employee is credited to `line_ids[0].account_id` — the first advance line's account — regardless of how many lines with how many accounts the advance had. | `CUSTOM/scgl_advance_expense_request/wizard/advance_request_reconcile.py:73` | HIGH |
| `EX-06` | Refusal after approval `unlink()`s the draft entry. The accounting artefact of an approved-then-refused claim leaves no trace. | `ENT18/hr_expense/models/hr_expense_sheet.py:733-734` | MEDIUM |
| `EX-07` | Reset clears the sheet↔entry link entirely (`Command.clear()`), and `_reverse_moves` nulls `expense_sheet_id` on the original. Both the original and its reversal become orphans of the claim. | `ENT18/hr_expense/models/hr_expense_sheet.py:602-604`; `ENT18/hr_expense/models/account_move.py:87-90` | HIGH |
| `EX-08` | Advance reset / rejection writes `state='cancel'` straight onto every linked entry instead of calling the cancel transition. | `CUSTOM/scgl_advance_expense_request/models/advance_expense_request.py:214-215`; `wizard/advance_request_rejected.py:14-15` | **TOLERANCE-ZERO** — scope settled by `16 §4` Expert 3 |
| `EX-09` | Amount, currency, date, product and quantity on an expense line remain writable after its entry is posted, and no override propagates the change. The claim total and the ledger total can diverge silently. | `ENT18/hr_expense/models/hr_expense.py:613-643` (gate covers only `tax_ids`, `analytic_distribution`, `account_id`) | HIGH |

## 4. Full Trace — `Module → Model → Field → Function → Event → Runtime → DB → Operational Truth → Accounting Event → Journal → Payable/Settlement → Reconciliation → Report/Close`

### 4.1 Trace A — Employee-paid expense (`own_account`)

| Stage | Artefact | Citation |
|---|---|---|
| Module | `hr_expense` | `ENT18/hr_expense/__manifest__.py` |
| Model | `hr.expense` → `hr.expense.sheet` | `models/hr_expense.py:17`, `models/hr_expense_sheet.py:29` |
| Field | `payment_mode='own_account'` (default) | `models/hr_expense.py:170-179` |
| Function | `_do_approve` → `_check_can_create_move` → `_do_create_moves` → `_prepare_bills_vals` | `models/hr_expense_sheet.py:711,686,746,824` |
| Event | **Approval** | `models/hr_expense_sheet.py:711-721` |
| Runtime | `sudo()` creation; approver need not hold accounting rights | `models/hr_expense_sheet.py:747-749, 760` |
| DB | one `account.move` `move_type='in_invoice'`, `expense_sheet_id` set | `models/hr_expense_sheet.py:829-842`; `models/account_move.py:12` |
| Operational truth | The employee is owed money | — |
| Accounting event | Vendor bill against the employee's work contact | `models/hr_expense_sheet.py:834-835` |
| Journal | DR expense account per line / CR payable of the work contact. **Note (AAS-03 Expert 2):** the credit is produced by core `_compute_needed_terms` (`ENT18/account/models/account_move.py:1232`), **not** by `_get_expense_account_destination` — hr_expense's override of `_compute_needed_terms` is gated on `company_account` (`hr_expense/models/account_move.py:62`). | `models/hr_expense.py:1004-1019`; `ENT18/account/models/account_move.py:1232`; `ENT18/account/models/account_move_line.py:547` |
| Payable | Vendor AP account of the employee's partner — **not a distinct employee-payable account** | `ENT18/account/models/account_move_line.py:547`; cf. `models/hr_expense_sheet.py:895-899` (the company-paid analogue) |
| Settlement | `action_register_payment` → `account.payment.register` on the move's lines | `models/hr_expense_sheet.py:606-614` |
| Reconciliation | Standard AP reconciliation; `_reconcile_payments` flips the sheet to `done` at zero residual | `wizard/account_payment_register.py:33-41` |
| Report / Close | `accounting_date` derived by `_calculate_default_accounting_date`, which consults the fiscal lock | `models/hr_expense_sheet.py:798-822` |

### 4.2 Trace B — Company-paid expense (`company_account`)

| Stage | Artefact | Citation |
|---|---|---|
| Field | `payment_mode='company_account'` | `models/hr_expense.py:170-179` |
| Function | `_do_create_moves` → per-line `_prepare_payments_vals` | `models/hr_expense_sheet.py:763-782`; `models/hr_expense.py:887-968` |
| Event | **Approval** (same as A) | — |
| DB | **N** `account.move` + **N** `account.payment`, one pair per expense line | `models/hr_expense_sheet.py:764-773` |
| Journal | DR expense / CR outstanding-payments account (or the method line's `payment_account_id`) | `models/hr_expense.py:936-943`; `models/hr_expense_sheet.py:876-894` |
| Partner | `vendor_id` — an unconstrained optional field; `partner_type` is nevertheless `'supplier'` | `models/hr_expense.py:180, 923, 942, 950-951` |
| Date | `date = expense.date`, **no fiscal-lock consultation on this branch** | `models/hr_expense.py:959` vs `models/hr_expense_sheet.py:814` |
| Control | `_check_payable_receivable` is **switched off** for this branch | `models/account_move_line.py:14-16` |
| Report / Close | `date_maturity` = `accounting_date or today`, but `accounting_date` is only auto-populated on branch A | `models/account_move.py:62-76` vs `models/hr_expense_sheet.py:758-759` |

### 4.3 Trace C — Employee advance (CUSTOM)

| Stage | Artefact | Citation |
|---|---|---|
| Model | `advance.expense.request` / `.line` | `advance_expense_request.py:16`; `advance_expense_request_line.py:14` |
| Approval | `button_approved` — single named approver, resolved through a One2many | `advance_expense_request.py:222-225`, `:63` |
| Accounting event | `button_post_bill` creates **and posts** an `in_invoice` | `advance_expense_request.py:239-273` |
| Journal | DR **product expense account** / CR employee payable. **No advance/receivable asset account.** | `advance_expense_request.py:248-257` (no `account_id` passed); `advance_expense_request_line.py:131` |
| Date | Python `date.today()`, not context date | `advance_expense_request.py:263-264` |
| Tax | `'tax_ids': []` — VAT and WHT both stripped | `advance_expense_request.py:255` |
| Liquidation path 1 | Offset against a vendor bill: DR bill AP / CR advance line-0 account, then `js_assign_outstanding_line` | `models/account_move.py:58-114`; `wizard/advance_request_reconcile.py:35-49` |
| Liquidation path 2 | Cash returned: DR journal default account / CR advance line-0 account | `wizard/advance_request_reconcile.py:62-92` |
| Reconciliation | `move_lines_cleared` m2m on the request; `is_clear` when `amount_toclear == 0` | `advance_expense_request.py:119, 140-149` |

### 4.4 Trace D — Petty cash (CUSTOM)

| Stage | Artefact | Citation |
|---|---|---|
| Model | `petty.cash` — holder, account, limit, computed balance | `petty_cash.py:7-49` |
| Float top-up | `account.move.is_petty_cash` single-line bill to the petty cash account | `hr_expense_petty_cash/models/account_move.py:12, 90-111` |
| Limit control | `limit − balance` ceiling at post time | `.../account_move.py:55-88` |
| Claim | `payment_mode='petty_cash'` (selection_add) | `.../hr_expense.py:11-14` |
| Balance control | Sheet constraint compares claim to holder balance | `.../hr_expense_sheet.py:55-83` |
| Routing | Grouped with `own_account` in the forked `_do_create_moves` | `.../hr_expense_sheet.py:96` |
| **GL redirection** | `_get_account_move_line_values` override — **method absent from this platform version**; byte-identical to its v14 ancestor | `.../hr_expense.py:72-79`; `21 NC-03` |
| **Journal routing** | **Also dead.** `journal_id` is a stored compute **without `readonly=False`** (`ENT18/hr_expense/models/hr_expense_sheet.py:212-217`), and `_compute_journal_id` (`:273-279`) consults `payment_method_line_id` only for `company_account`. The custom module's `default=_default_journal_id` on a stored computed field is inert. **The holder's journal never reaches the bill**, and the field is `invisible` for non-own-account sheets so it cannot be corrected in the UI. | `hr_expense_petty_cash/models/hr_expense_sheet.py:13-33, 51-52`; `E2-01` |
| **Test coverage** | **Zero effective coverage on v18.** The test module is byte-identical to its v14 ancestor and `setUp` fails at line 19 on a v14-only xmlid. | `E2-01` |
| Company scope | `petty.cash` has no `company_id`, no record rule, and a **global** `unique(partner_id)` | `petty_cash.py:12-36` |

## 5. Approval Topology

| Path | Approver derivation | Server-side enforcement | Citation |
|---|---|---|---|
| Expense claim | `expense_manager_id` ∪ `parent_id.user_id` ∪ `department_id.manager_id.user_id` ∪ `user_id`; HR admin bypasses all | `_check_can_approve` raises on `action_approve_expense_sheets` | `hr_expense_sheet.py:342-368, 672-675` |
| Self-approval | Blocked for non-HR-admin (`"It is your own expense"`) — **but the HR-admin branch is evaluated first and skips the check entirely** | Partial | `hr_expense_sheet.py:354-362` |
| Advance request | Single `ae_approver` on the employee record, reached through a One2many | `button_approved` compares `assigned_to.id` to `env.uid` | `advance_expense_request.py:63, 222-225` |
| Multi-level | `multi_level_approval` exists in CUSTOM but no dependency links it to `hr.expense` or `advance.expense.request` | — | `21 NC-06` |

## 6. Cross-references

Recognition timing → `03`. GL lines → `05`. Payables → `04`. Tax → `07`.
Settlement → `08`. Edge cases → `10`. Everything disputed → `11`, `16`, `20`, `21`.
