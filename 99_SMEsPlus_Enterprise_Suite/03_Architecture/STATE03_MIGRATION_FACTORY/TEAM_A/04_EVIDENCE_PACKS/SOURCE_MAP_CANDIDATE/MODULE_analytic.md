# Source Map (candidate) — `analytic`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `analytic` |
| Display name | Analytic Accounting |
| Manifest version | 1.2 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `74112ba1b9696a67` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/analytic/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `mail`, `uom`
- Direct dependents in 300-module list (3): `account`, `hr_timesheet`, `project`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (2): `base_accounting_kit` — LGPL-3, `smesplus_account` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / —
- Inventory of user-facing artifacts (counts): menu items 0, views 15, window actions 6, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (7): `account.analytic.distribution.model` (Analytic Distribution Model); `account.analytic.plan` (Analytic Plans); `account.analytic.applicability` (Analytic Plan's Applicabilities); `account.analytic.account` (Analytic Account); `analytic.mixin` (Analytic Mixin); `analytic.plan.fields.mixin` (Analytic Plan Fields); `account.analytic.line` (Analytic Line)
- Objects extended from other modules (3): `ir.config_parameter`, `res.config.settings`, `mail.thread`
- Company-dependent settings introduced: 1 field(s); company-consistency auto-check declared on 4 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `account.analytic.distribution.model` ← Community: `account`; open-license custom/third-party scanned: —
- `account.analytic.plan` ← Community: `stock_account`; open-license custom/third-party scanned: —
- `account.analytic.applicability` ← Community: `account`, `hr_expense`, `hr_timesheet`, `mrp_account`, `project_stock_account`, `purchase`, `sale`; open-license custom/third-party scanned: —
- `account.analytic.account` ← Community: `account`, `hr_expense`, `mrp_account`, `project`, `purchase`, `stock_account`; open-license custom/third-party scanned: `base_account_budget`, `om_account_budget`
- `analytic.mixin` ← Community: `account`, `hr_expense`, `l10n_account_withholding_tax`, `mrp_account`, `purchase`, `purchase_requisition`, `sale`; open-license custom/third-party scanned: `account_asset_management`, `account_payment_multi_deduction`, `base_accounting_kit`, `om_account_asset`
- `analytic.plan.fields.mixin` ← Community: `project`; open-license custom/third-party scanned: —
- `account.analytic.line` ← Community: `account`, `hr_timesheet`, `mrp_account`, `project_stock_account`, `project_timesheet_holidays`, `sale`, `sale_timesheet`, `website_timesheet`; open-license custom/third-party scanned: `scgl_timesheet_grid`
- This module's own extension of other modules' objects: `ir.config_parameter`, `res.config.settings`, `mail.thread`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 3 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`group_analytic_accounting`); record rules 4 (of which company-scoped by text 4); access rows 5

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 30 of 30 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: analytic
Source revision: 19.0.post20260921 | Path base: odoo/addons | Method: static source read (no execution)

## A. Capabilities
- Foundation for cost/revenue tracking outside the general ledger: analytic accounts, plans, lines, distribution models, mixin for percentage splits. Depends on base, mail, uom (analytic/__manifest__.py:8). Not marked application, not auto_install (manifest lines 4-48). Core dependency of accounting-side modules (account/models/account_analytic_account.py:7 extends it).
- Analytic account: name, reference, customer, company, active flag, plan; shows debit/credit/balance derived from analytic lines converted into the current company currency, filterable by date context (analytic/models/analytic_account.py:20-93, 162-203).
- Plans in a tree; each root plan becomes its own column on analytic lines; the "Project" plan uses the fixed account_id column, others get generated columns; sub-plans get read-only grouping fields (analytic/models/analytic_plan.py:104-121, 314-374; analytic/data/analytic_data.xml:9-17).
- Multi-plan line: one analytic line carries one account per plan; an "analytic_distribution" view of a line can be split into several lines with percentages (analytic/models/analytic_line.py:11-31, 227-267). Message "N analytic lines created" is sent (line 264-267).
- Plan applicability: optional / mandatory / unavailable, per plan default (company-dependent) plus per-company, per-business-domain override rules scored by best match (analytic_plan.py:77-92, 246-268, 408-458). Base domain shipped here: "general" only; other domains added by other modules (see F).
- Distribution models: automatic prefill of analytic distribution by partner, partner category, company; multiple matching models are combined unless plan already covered (analytic/models/analytic_distribution_model.py:18-99). (TEST) analytic/tests/test_analytic_account.py:79 and :94.
- Analytic mixin for documents: JSON percentage distribution, searchable by account names/ids, groupable (only for tables listed: journal items, purchase lines, assets, expenses) (analytic/models/analytic_mixin.py:16-30, 80-160). Value precision uses decimal setting "Percentage Analytic", 2 digits (analytic/data/analytic_data.xml:4-7).
- Access is granted through a group switch "Analytic Accounting" in general settings (analytic/models/res_config_settings.py:10; analytic/security/analytic_security.xml:35-37). Conditional on that group.

## B. Objects and lifecycle
- account.analytic.plan (self-parenting, cascade delete of children) -> account.analytic.account -> account.analytic.line (analytic_plan.py:29-36,58-62; analytic_account.py:38-59). No workflow states; accounts use an active flag only (analytic_account.py:32-37).
- Changing an account's plan moves existing line references to the new plan column; blocked with a redirect warning if that would overwrite data already in the target column (analytic_account.py:205-243). (TEST) analytic/tests/test_analytic_account.py:220, :235, :248.
- Changing a plan's parent has equivalent migration logic (analytic_plan.py:381-405). (TEST) test_analytic_account.py:264, :288, :303.
- Deleting a plan removes its generated column; deletion refused while views still use the column (TEST) analytic/tests/test_plan_operations.py:60. Renaming re-syncs column labels (analytic_plan.py:123-127; TEST test_plan_operations.py:36).
- Changing which plan is the "Project" plan (system parameter analytic.project_plan) is only accepted for a valid root plan and triggers rebuild of dynamic columns (analytic/models/ir_config_parameter.py:11-28). (TEST) test_analytic_account.py:360.

## C. Validations, security, multi-company
- An analytic line must have at least one account across all plans (analytic_line.py:93-98).
- Account company cannot be changed if lines already exist outside the new company hierarchy (analytic_account.py:95-102).
- Distribution model: accounts tied to a specific company cannot appear in a model that is shared or belongs to another company (analytic_distribution_model.py:39-58).
- Mandatory-plan check on documents: only enforced when caller sets a validation context flag; requires 100 percent per mandatory root plan, otherwise error "One or more lines require a 100% analytic distribution" (analytic_mixin.py:182-196). Caller in accounting: account/models/account_move_line.py:2069, 3188-3224.
- Access: all five analytic models (account, line, plan, applicability, distribution model) are full-access for the Analytic Accounting group only (analytic/security/ir.model.access.csv:2-6). (TEST) a user with only this group can create a plan (analytic/tests/test_analytic_account.py:192).
- Global company rules: accounts, applicability, distribution models visible when company empty or a parent of an allowed company; analytic lines visible only for allowed companies (analytic_security.xml:5-31). Accounts and models use parent-of company checks (analytic_account.py:16-17; analytic_distribution_model.py:15-16).
- Line company is required and read-only, defaults to current company (analytic_line.py:204-210).

## D. Handoffs (owner in brackets)
- Ledger postings create analytic lines [account]: account/models/account_analytic_line.py:9,49 (move-line link; adds invoice and vendor bill categories); business domains invoice/bill [account]: account/models/account_analytic_plan.py:10-13.
- Sales order, purchase order, expense, timesheet, manufacturing, stock picking domains [sale, purchase, hr_expense, hr_timesheet, mrp_account, project_stock_account]: sale/models/analytic.py:16-18; purchase/models/analytic_applicability.py:10-12; hr_expense/models/analytic.py:13-15; hr_timesheet/models/analytic_applicability.py:10-12; mrp_account/models/analytic_account.py:86-88; project_stock_account/models/analytic_applicability.py:10-12.
- Projects and timesheets [project, hr_timesheet]: project/models/account_analytic_account.py:9; hr_timesheet/models/hr_timesheet.py:17.
- Inventory valuation account link to plans [stock_account]: stock_account/models/analytic_account.py:6,31.
- Analytic distribution field embedded on documents [account, sale, purchase, purchase_requisition, hr_expense, mrp_account, l10n_account_withholding_tax] via the mixin (see F).
- No approval flow or cron in this module.

## E. Configuration that changes outcomes
- Plan default applicability (per company) and applicability rules (analytic_plan.py:77-92, 408-458); system parameter analytic.project_plan; percentage precision setting; distribution model priority (sequence) and criteria; Analytic Accounting group toggle.
- Context keys: from_date/to_date for balances (analytic_account.py:173-176); validate_analytic for mandatory check (analytic_mixin.py:183).

## F. Effective extension path (module names only)
- account.analytic.account: account, purchase, project, hr_expense, mrp_account, stock_account. account.analytic.line: account, sale, mrp_account, hr_timesheet, project_timesheet_holidays, project_stock_account, sale_timesheet, website_timesheet. account.analytic.applicability: account, sale, purchase, hr_expense, hr_timesheet, mrp_account, project_stock_account. account.analytic.distribution.model: account. account.analytic.plan: stock_account.
- analytic.mixin users: account, sale, purchase, purchase_requisition, hr_expense, mrp_account, l10n_account_withholding_tax.
- Direct manifest dependents (exact match): account, project, hr_timesheet.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: client-side widgets for distribution editing (static JS not analysed).
- UNKNOWN — EVIDENCE INSUFFICIENT: migration script behaviour (analytic/migrations/1.2/pre-migrate.py not analysed).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether analytic lines are ever created here outside of user or downstream-module actions; this module has no own posting logic.

