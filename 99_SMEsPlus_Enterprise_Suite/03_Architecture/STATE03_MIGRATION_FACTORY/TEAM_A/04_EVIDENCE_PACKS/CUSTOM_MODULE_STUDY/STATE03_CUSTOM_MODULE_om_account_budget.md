> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 custom module trace: om_account_budget

Module: om_account_budget · License (confirmed in manifest): LGPL-3 (om_account_budget/__manifest__.py:11)
Author (manifest): Odoo Mates, Odoo SA (manifest:3) · Version (manifest): 1.0.4 (manifest:5; name string says "Odoo 19 Budget Management", manifest:2)
Path: addons_Extramodule/addons_extra/om_account_budget
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Budgeting to compare planned versus actual revenue and cost. A "budgetary position" groups ledger accounts; a budget has a period, a responsible user, a company and a status flow draft / confirmed / validated / done / cancelled (om_account_budget/models/account_budget.py:9-78).
- Budget lines pair a budgetary position and/or an analytic account with a period and a planned amount (positive for revenue, negative for cost). Each line shows a practical amount, a time-proportional theoretical amount, an achievement ratio and an "above budget" flag (account_budget.py:80-267; computes at 188-259).
- Practical amount source: analytic lines of the analytic account when one is given; otherwise posted ledger lines on the position's accounts within the budget company (account_budget.py:188-226).
- Users can drill from a line to the underlying analytic entries or journal items (account_budget.py:268-289). Demo data included (manifest:20).

## 2. Attachment to CORE
- Depends on core `account` only (manifest:10).
- `account.analytic.account` (models/account_analytic_account.py:4-9): ADDS a one-to-many field listing budget lines; no method override.
- Reads (no writes) core `account.analytic.line` and `account.move.line`; uses analytic plan column naming `plan_id._column_name()` (account_budget.py:197) and reads only posted entries (`parent_state`) on the ledger path (:214-219). No override of posting, lock dates, valuation, approvals, numbering. Budget status transitions are plain status writes with no check against real accounting data (account_budget.py:64-78). No `ALTERS CORE CONTROL` item found.
- Core client-side aggregation hooks overridden on the module's own budget line model: `fields_get`, `formatted_read_group`, `formatted_read_grouping_sets` (account_budget.py:110-170): ADD behavior after core - the non-stored amounts are summed by hand per group and advertised as summable. They do not change core models' behavior.
- View changes on core: adds a tab to the analytic account form (views/account_analytic_account_views.xml:7-11, `analytic.view_account_analytic_account_form`); REMOVES the core Accounting settings block `account_budget`, which in core is a switch for installing a separate budget module (views/res_config_settings_views.xml:7-9; core:account/views/res_config_settings_views.xml:359-362).
- Menus under core `account.account_account_menu` and `account.account_reports_management_menu` (views/account_budget_views.xml:34-36, 250-255, 368-372).

## 3. New objects, security, automation, external calls
- Models: account.budget.post, crossovered.budget (mail.thread with tracked status), crossovered.budget.lines (account_budget.py:9, 42, 80).
- ACLs (security/ir.model.access.csv:2-7): Accountant (`account.group_account_user`) full rights on positions, budgets and lines; Manager full on lines, read-only on positions and budgets. Odd: the Manager group has weaker rights than the Accountant group on budgets/positions; effective rights depend on group implication (in core the Manager group implies the Accountant group: not verified here).
- Record rules: three global multi-company rules on positions, budgets, lines, `noupdate` (security/security.xml:5-24). Practical amount queries also restrict by the line's company (account_budget.py:197-219).
- Validations: position must have at least one account (account_budget.py:21-40); line requires a position or analytic account (:261-266); line dates must lie inside the budget period (:291-303).
- No crons, no server actions, no external calls.

## 4. Odoo 19 compatibility (grep against Community 19)
- Found in core: `formatted_read_group` and `formatted_read_grouping_sets` (core:odoo/addons/web/models/models.py:802, 702, i.e. defined by the web module), `_column_name` (core:analytic/models/analytic_plan.py:120), `general_account_id` (core:account/models/account_analytic_line.py:19), `parent_state` (core:account/models/account_move_line.py:69), `Domain` import (core:odoo/orm/domains.py:196), actions `analytic.account_analytic_line_action_entries` (core:analytic/views/analytic_line_views.xml:145) and `account.action_account_moves_all_a` (core:account/views/account_move_views.xml:1854), setting id `account_budget` (core:account/views/res_config_settings_views.xml:359).
- No mismatch found in the checked references. The code comments explicitly refer to 19.0 behavior (account_budget.py:206, comment on deprecated read_group). Tests exist (tests/test_account_budget.py) but were not executed.

## 5. Custom-to-custom dependencies
- None.

## 6. UNKNOWN - EVIDENCE INSUFFICIENT
- Whether core Community 19 also offers a `module_account_budget` install switch that this module hides, and what module it names: UNKNOWN - EVIDENCE INSUFFICIENT.
- Whether the Accountant/Manager ACL inversion on budget and position models is intentional or produces surprises for pure Manager users: UNKNOWN - EVIDENCE INSUFFICIENT.
- Whether budget status (validated/done) restricts editing of lines: no such check found in the module code; view-level read-only conditions in views/account_budget_views.xml were not analysed: UNKNOWN - EVIDENCE INSUFFICIENT.
