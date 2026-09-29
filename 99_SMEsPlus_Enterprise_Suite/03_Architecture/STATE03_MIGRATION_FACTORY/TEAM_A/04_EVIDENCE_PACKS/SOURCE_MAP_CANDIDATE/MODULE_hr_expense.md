# Source Map (candidate) — `hr_expense`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S1-STATIC-EXTRACT (candidate; behavior semantics not yet traced)

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
- Core/optional/conditional behavior and business meaning of each capability: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced)

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
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning: `UNKNOWN — EVIDENCE INSUFFICIENT` (not yet traced).

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; behavioral semantics of this module (S1 only).

