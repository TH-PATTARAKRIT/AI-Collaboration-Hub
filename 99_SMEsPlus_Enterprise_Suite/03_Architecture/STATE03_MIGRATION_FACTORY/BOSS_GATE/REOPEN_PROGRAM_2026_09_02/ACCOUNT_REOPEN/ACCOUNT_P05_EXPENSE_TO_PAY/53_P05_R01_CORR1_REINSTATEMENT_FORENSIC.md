# 53 — P05 `R-01` CORR1 REINSTATEMENT FORENSIC

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E14`

## 1. Lineage

| Stage | Position |
|---|---|
| **Original finding** (`P05#01`, `04 §4`) | `hr.expense.vendor_id` is an unconstrained optional Many2one — no `required`, no `default`, no `compute`, **no `check_company`** — yet it is written to four places and the payment is hard-coded `partner_type='supplier'`. Framed as: *"no gate at any layer"*. |
| **CORR1 withdrawal** (`P05#02`, `22 §3 R-01`) | **WITHDRAWN as a scope defect.** Reasoning: `res.partner` is TENANT-scoped; `REFERENCE SCOPE ≠ FINANCIAL SCOPE`; therefore a company-owned entry may legitimately reference a tenant-owned partner and `check_company` is over-constraint. |
| **Reinstatement** (`P05#03`, AAS-03 Expert 4) | **The withdrawal was wrong.** |

## 2. Why the Withdrawal Was Invalid

Two source facts refute its premise:

1. **`res.partner` is not purely tenant-scoped.** It carries its own optional `company_id`
   (`ENT18/base/models/res_partner.py:294`, `_onchange_company_id` at `:549`). Odoo's model lets a
   partner be shared (`company_id = False`) **or hard-restricted to one company**. `22 §2`'s row
   classifying it "TENANT — Tenant only" was **incomplete**, and that mischaracterisation is what let
   the withdrawal through.
2. **Odoo core applies `check_company=True` to partner references for exactly this case** — e.g.
   `account.move.partner_id` (`ENT18/account/models/account_move.py:372-380`). The
   *"reference scope ≠ financial scope"* argument was **contradicted by the platform's own design
   pattern**.

> **The instructive part:** the withdrawal was produced by the *scope-correction round*, whose purpose
> was to stop the author asserting requirements instead of deriving them. It then asserted a
> **non**-requirement instead, from a characterisation of `res.partner` it had not read.
> **Applying a rule correctly to unverified facts is still an error.** `RE-18`.

## 3. Correct Scope-Aware Interpretation

| Axis | Determination |
|---|---|
| Ownership scope of `res.partner` | **TENANT by default, COMPANY-restrictable** via its optional `company_id` |
| Reference scope of `vendor_id` | TENANT — a company entry may reference a tenant partner |
| **Financial scope** of the resulting entry | **COMPANY** |
| Required context | Tenant; **Company where the reference is company-constrained** |

## 4. Current Status — `R-01'`, reinstated and narrowed

> **Missing early `check_company` validation on the expense line's `vendor_id`. Enforcement exists
> only downstream**, at move creation/posting, via `account.move.partner_id` with
> `_check_company_auto = True` — and `_check_company` runs inside `create()`/`write()`, so **`sudo()`
> does not bypass it**.

**The defect is late failure, not absence of a gate.** An invalid cross-company vendor can be saved on
a draft or submitted expense and only errors at posting.

This **also corrects the original finding in the opposite direction**: `04 §4`'s *"no gate at any
layer"* was wrong for the cross-company case. Both the original and its withdrawal were wrong, in
opposite directions; the reinstated form is narrower than either.

| Aspect | Class |
|---|---|
| Late-failure scope defect | **FACT VERIFIED**, class **A** within the files read |
| Identity-completeness defect (`vendor_id` may be empty while `partner_type='supplier'`) | **FACT VERIFIED** — unchanged throughout, never withdrawn |
| Exposure on the v18 target | **LIVE — CONFIGURED/REACHABLE** (`hr_expense` installed, 993 expenses) |
