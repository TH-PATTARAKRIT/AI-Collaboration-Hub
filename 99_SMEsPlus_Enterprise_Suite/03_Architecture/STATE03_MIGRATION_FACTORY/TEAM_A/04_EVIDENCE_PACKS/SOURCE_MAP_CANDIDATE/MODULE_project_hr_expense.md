# Source Map (candidate) — `project_hr_expense`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_hr_expense` |
| Display name | Project Expenses |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `db56eae04bb6c264` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_hr_expense/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `project_account`, `hr_expense`
- Direct dependents in 300-module list (1): `project_sale_expense`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/expenses / Project expenses
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `hr.expense`, `project.project`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.expense`, `project.project`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 19 of 19 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project_hr_expense
Revision 19.0.post20260921 | Bridge: Project (project_account) <-> Expenses (hr_expense)

## A. Capabilities (core / optional / conditional)
- Bridge that shows employee expenses on a project through the project's analytic account; manifest description: expenses linked to the analytic account shown on the project form (project_hr_expense/__manifest__.py:10). Depends on project_account and hr_expense (:11).
- Auto-install: yes (project_hr_expense/__manifest__.py:19). No settings toggle, no own groups, no access CSV (data list: :12-14).
- Conditional: profitability lines appear only for projects that have an analytic account (project_hr_expense/models/project_project.py:71-72).
- Expense drill-through buttons visible only to members of the expense team-approver group (project_hr_expense/models/project_project.py:73); the embedded "Expenses" tab on the project needs expense user group (project_hr_expense/views/project_project_views.xml:10,20).

## B. Business objects and lifecycle
- Project (owner project) is tied to expenses via its analytic account: expenses whose analytic distribution includes the project's account are the project's expenses (project_hr_expense/models/project_project.py:44).
- Expense list is opened from the project, with the project passed as context (project_hr_expense/models/project_project.py:19-29); if exactly one expense and not from the embedded tab, opens straight to the form (:26-28).
- Embedded "Expenses" tab added to the project task view and the project updates view (project_hr_expense/views/project_project_views.xml:3-21).
- Only expenses in posted, in-payment or paid states count toward project cost (project_hr_expense/models/project_project.py:77).

## C. Validations, automation, security
- New expenses created while a project is in context inherit the project's analytic distribution unless one is supplied (project_hr_expense/models/hr_expense.py:16-24); computed distribution likewise defaults to the project's but keeps an existing one (:7-14). Test: (TEST) project_hr_expense/tests/test_analytics.py:30-48.
- Project profitability: expenses are added as a cost line (billed = untaxed amount converted to project currency, to-bill = 0, shown negative) in a cost section labelled "Expenses" with sequence 13 (project_hr_expense/models/project_project.py:53-58,90-99).
- Double-counting avoidance: expense-generated vendor-bill lines are excluded from the already-included purchase lines and analytic lines tied to expense moves are excluded from the generic profitability lines; purchase items linked to an expense are excluded from "add purchase items" (project_hr_expense/models/project_project.py:31-35,60-68,108-112). Comment states purchase orders and employee-paid expenses both create vendor bills (:61-62).
- Security: no record rules here; company scoping through currency conversion using project company (project_hr_expense/models/project_project.py:90-94). Expense lookup runs under the reading user's access (:75) while move-line exclusion uses elevated rights (:64).

## D. Handoffs
- project / project_account own project, analytic account, profitability framework; hr_expense owns expense records, states, groups; account owns vendor bills and analytic lines.
- Profitability tests: (TEST) project_hr_expense/tests/test_project_profitability.py:29,127.

## E. Configuration that changes outcomes
- Project analytic account must be set for any expense cost to appear (project_hr_expense/models/project_project.py:71).
- Expense state gate (posted/in payment/paid) determines when cost shows (project_hr_expense/models/project_project.py:77).
- Multi-currency: amounts converted into the project currency (project_hr_expense/models/project_project.py:90-94).

## F. Effective extension path
- project_account, hr_expense, project (module names only); sale_expense/project-sale bridges may further alter profitability: UNKNOWN — EVIDENCE INSUFFICIENT.

## G. Not verified
- Behaviour when analytic distribution splits across several accounts (percentage weighting): UNKNOWN — EVIDENCE INSUFFICIENT (query matches any distribution containing the account, project_hr_expense/models/project_project.py:78).
- Whether expenses in draft/approved states are shown elsewhere: UNKNOWN — EVIDENCE INSUFFICIENT.

