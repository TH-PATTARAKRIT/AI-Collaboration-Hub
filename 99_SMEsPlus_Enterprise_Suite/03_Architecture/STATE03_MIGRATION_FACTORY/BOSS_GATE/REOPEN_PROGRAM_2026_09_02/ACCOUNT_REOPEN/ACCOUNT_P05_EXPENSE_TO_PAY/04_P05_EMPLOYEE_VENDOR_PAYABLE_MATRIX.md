# 04 — P05 EMPLOYEE / VENDOR PAYABLE MATRIX

`LAYER 2 — AUDIT QUARANTINE`

## 1. Headline

> **The reference does not distinguish an employee payable from a vendor payable at account level.**
> Both resolve to `res.partner.property_account_payable_id`. The distinction exists only in *which
> partner* carries the balance, and that partner is itself resolved through a two-field split that can
> disagree with itself.

## 2. Payable Destination Resolution

`ENT18/hr_expense/models/hr_expense_sheet.py:876-900` — `_get_expense_account_destination`

| Branch | Destination account | Fallback | Failure mode |
|---|---|---|---|
| `company_account` | `payment_method_line_id.payment_account_id` | `journal.company_id.expense_outstanding_account_id` | `RedirectWarning` to settings, or `UserError` if the user cannot write settings (`:884-894`) |
| `own_account` | `work_contact_id.property_account_payable_id` | `work_contact_id.parent_id.property_account_payable_id` | `UserError` if the employee has no work contact (`:896-897`) |
| `petty_cash` | **Falls to the `own_account` branch** — see `EX-04` | as above | as above |

**There is no employee-specific payable account anywhere in this resolution.** The employee's partner
is looked up with `.with_company(self.company_id)` (`:898`), so the *company-dependent* value of the
payable property applies — which is the only company sensitivity in the whole chain.

## 3. The Partner Split — `partner_id` vs `commercial_partner_id`

`ENT18/hr_expense/models/hr_expense_sheet.py:829-842` — `_prepare_bills_vals`

| Field on the bill | Source | Citation |
|---|---|---|
| `partner_id` | `employee_id.sudo().work_contact_id` | `:834` |
| `commercial_partner_id` | `employee_id.user_partner_id` | `:835` |
| `partner_bank_id` | `employee_id.sudo().bank_account_id` | `:827-828` |

These are **three different partner-derived values from three different employee fields**.

`ENT18/hr_expense/models/account_move.py:15-25` then overrides `_compute_commercial_partner_id` for
own-account expense moves, resolving it to `partner_id.commercial_partner_id` unless that equals the
company's own partner, in which case it falls back to `partner_id` itself.

`:38-45` adds `show_commercial_partner_warning`, true when the commercial partner **is** the company's
own partner on an `in_invoice` whose partner has employees — i.e. the platform ships a UI warning for
the case where an employee's contact is mis-parented to the company, which would make the company owe
itself. **The warning is the only control.** Declared boundary: `ENT18/addons/hr_expense`, all files;
Expert 1 independently searched for a block and found none — *"view-level warning only; there is no
block"*. Class **B** beyond that module. `P05-F-27`.

| Consequence | Class |
|---|---|
| AP ageing and partner-ledger reports aggregate by `commercial_partner_id`. Where `work_contact_id` and `user_partner_id` resolve to different commercial parents, one employee's balance splits across two ledger identities. | SUPPORTED INTERPRETATION |
| If the employee has no linked user, `user_partner_id` is empty; the value written to `commercial_partner_id` at create time is then false, before the compute overrides it. | SUPPORTED INTERPRETATION — Expert 1 confirmed the split and the override chain but did not execute this branch; held at `SUPPORTED INTERPRETATION`, closure needs runtime (`20 U-02`) |
| An employee whose contact is a child of the company partner produces a bill on which the company is its own creditor; shipped mitigation is a warning flag only. | FACT VERIFIED |

## 4. Company-Paid Branch — the `vendor_id` Problem

`ENT18/hr_expense/models/hr_expense.py:180`

```
vendor_id = fields.Many2one(comodel_name='res.partner', string="Vendor")
```

No `required`, no `default`, no `compute`, no `check_company`, no domain.

It is nevertheless written to **four** places on the company-paid branch:

| Target | Line |
|---|---|
| base move line `partner_id` | `hr_expense.py:923` |
| outstanding move line `partner_id` | `:942` |
| `account.payment.partner_id` | `:951` |
| `account.move.partner_id` | `:961` |

…while `payment_vals['partner_type']` is hard-coded `'supplier'` (`:950`).

> **`P05-F-24` FACT VERIFIED** — a company-paid expense with `vendor_id` unset produces a *supplier*
> payment with **no partner**. Its outstanding line cannot be matched to a vendor, and the entry
> carries no counterparty identity. There is no constraint requiring `vendor_id` on this branch.
> **SETTLED by AAS-03 Expert 1:** the view **confirms rather than guards** — `hr_expense_views.xml:247`
> renders `vendor_id` with no `required` and no `readonly`.
>
> **CORRECTED by AAS-03 Expert 4:** the phrase "no gate at any layer" is **wrong for the
> cross-company case**. `account.move`/`account.move.line` set `_check_company_auto = True` and their
> `partner_id` carries `check_company=True`, and `_check_company` runs inside `create()`/`write()` — so
> `sudo()` does not bypass it. A cross-company vendor is caught, but **late**, at move creation or
> posting rather than at capture. The **presence/identity** defect stands unchanged: `vendor_id` may be
> left empty entirely, and nothing at any layer requires it while `partner_type` is hard-coded
> `'supplier'`.

Note also: `check_company` is absent, so `vendor_id` is not constrained to the sheet's company.

> **SCOPE REVALIDATION (`CORR1`)** — the `check_company` observation is **WITHDRAWN as a scope
> defect** by `22 §3 R-01`: `res.partner` is TENANT-scoped master data and
> `REFERENCE SCOPE ≠ FINANCIAL SCOPE`, so a company-owned entry may legitimately reference a
> tenant-owned partner. The finding above — that `vendor_id` is optional while `partner_type` is
> hard-coded `'supplier'` — is an identity-completeness defect and **stands unchanged**.

## 5. Payable Matrix

| Payable kind | Account used | Partner used | Distinguishable in the ledger? | Reconciles against |
|---|---|---|---|---|
| Employee reimbursement | vendor payable of the employee's work contact | `work_contact_id` (comm. partner overridden) | **Only by partner**, not by account | Outbound payment |
| Employee advance | vendor payable of `requested_by.partner_id` | `requested_by.partner_id` | **Only by partner** | Outbound payment, then a manual clearing entry |
| Petty cash claim | **disputed** — routed to the employee payable, see `EX-04` | `work_contact_id` | No | — |
| Company-paid expense | outstanding-payments account (or method line account) | `vendor_id`, **may be empty** | Yes, by account | Bank statement |
| Vendor service purchase | vendor payable | vendor | **Only by partner** | Outbound payment |

**Three of five kinds land in the same account.** Separating employee payable from vendor AP in a
trial balance requires a partner-level report, not an account-level one. `P05-F-26`.

## 6. Multi-Company Boundary

| Object | Company field | Record rule | Cross-company exposure |
|---|---|---|---|
| `hr.expense` | `company_id`, `_check_company_auto = True` (`hr_expense.py:17`) | `hr_expense/security/ir_rule.xml:23-28` — **enumerated by Expert 1: an employee has read/write/create/unlink on all of their own expenses with NO state clause**, which is what makes `TZ-03` exploitable | Company-constrained, **state-unconstrained** |
| `hr.expense.sheet` | `company_id` required, readonly (`hr_expense_sheet.py:59-65`); `_check_expense_lines_company` constraint (`:440-444`) | as above | Constrained |
| `hr.expense.sheet.employee_journal_id` | `check_company=True` (`:155`) | — | Constrained |
| `hr.expense.vendor_id` | **no `check_company`** | — | **Unconstrained** |
| `petty.cash` | **no `company_id` at all** | **none in module** | **Unconstrained — `TZ-02`** |
| `advance.expense.request` | `company_id` required | `advance_request_security.xml` global rule on `company_ids` | Constrained |
| `advance.expense.request.assigned_to` | related through `requested_by.employee_ids` (a One2many) | — | **First employee record wins; in a multi-company database that is an arbitrary company's approver** — `P05-F-12` |
| `account.withholding.tax` | `company_id` required (`account_withholding_tax.py:26`) | multi-company rule present (`security/security.xml:2-4`) | Constrained |

> **SCOPE REVALIDATION (`CORR1`)** — the `account.withholding.tax` row above recorded
> "Constrained" as if company scoping were self-evidently correct. `22 §3 R-03` finds it
> **over-constrained**: one record conflates PLATFORM statutory reference (rate, form class) with
> COMPANY mapping (GL account), forcing the statutory rate to be duplicated per company with no
> mechanism keeping copies equal. New finding `SC-01`.
>
> The `petty.cash` and `assigned_to` rows are re-derived in `22 §3 R-02` and `R-04`.

## 7. Settlement Bank Account Selection

`ENT18/hr_expense/wizard/account_payment_register.py:13-22` overrides `_get_line_batch_key` so that,
for own-account expense sheets with no `partner_bank_id` on the move, the batch key takes
`employee_id.sudo().bank_account_id` or else the partner's first bank account.

Two observations:
1. `sudo()` is used to read the employee's bank account, so a payment preparer who cannot see the
   employee's banking data still causes it to be selected.
2. The fallback `line.partner_id.bank_ids.ids[0]` is an **arbitrary first** account when the employee
   record carries none. `P05-F-new-02`.
