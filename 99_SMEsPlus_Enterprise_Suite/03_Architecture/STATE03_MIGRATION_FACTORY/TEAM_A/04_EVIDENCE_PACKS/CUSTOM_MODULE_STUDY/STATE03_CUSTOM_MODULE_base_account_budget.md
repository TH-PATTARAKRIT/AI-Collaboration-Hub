> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 CUSTOM MODULE TRACE — base_account_budget

Module: base_account_budget
License (confirmed in manifest): LGPL-3 (base_account_budget/__manifest__.py:47)
Author (manifest): Cybrosys Techno Solutions (manifest:34)
Version (manifest): 19.0.1.0.1 (manifest:24)
Path: addons_Extramodule/base_accounting_kit-19.0.3.3.1/base_account_budget
Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Budget planning by analytic account: define "Budgetary Positions" (named groups of ledger accounts), create budgets with a period and per-analytic-account lines carrying a planned amount. (base_account_budget/models/account_budget.py:26-38, 47-67, 85-108)
- Each line shows planned, "practical" (actual analytic amount in the period) and "theoretical" (planned amount pro-rated by elapsed time, or by paid date) plus an achievement percentage. (account_budget.py:99-105, 110-203)
- Budget workflow states: draft, confirmed, validated ("Approve" button), done, cancelled; buttons simply set the state, no checks. (account_budget.py:57-82; views/account_budget_views.xml:73-84)
- Budget lines are also shown as a "Budget Items" tab on the analytic account form. (views/account_analytic_account_views.xml:11-42)

## 2. Attachment to CORE
- Depends on core `base`, `account` (manifest:38); uses `mail.thread` (account_budget.py:50).
- `account.analytic.account` (core analytic): adds a one-to-many "Budget Lines" (base_account_budget/models/account_analytic_account.py:25-32); inherits core analytic form view (views/account_analytic_account_views.xml:4-7; core:analytic/views/analytic_account_views.xml:3), tab visible to accounting users only (xml:11).
- `account.account`: only referenced as a many-to-many target in budgetary positions (account_budget.py:33); core object is not modified.
- Menus added under core menus `account.menu_finance_entries` ("Budgets", accounting users) and `account.account_reports_management_menu` (views/account_budget_views.xml:280-284, 347-349; core:account/views/account_menuitem.xml:24,40).
- No override of any core method. No effect on posting, lock dates, valuation/cost, or numbering. Approval buttons belong only to the module's own budget object; the budget is NOT connected to purchase/bill approval or spending blocks (no such hook found). No `ALTERS CORE CONTROL` from method overrides.
- One install-time effect on core security: `post_init_hook` (base_account_budget/__init__.py:25-30, registered manifest:45) adds the core group "analytic accounting" to every internal (non-portal) user; the security data file also adds it to the root user (security/account_budget_security.xml:26-28). Business effect: analytic fields become visible to all internal users. Treat as ALTERS CORE CONTROL (security groups) at install time only.

## 3. New objects, security, automation
- New models: `account.budget.post` (Budgetary Position), `budget.budget`, `budget.lines` (account_budget.py:28, 48, 86).
- ACLs (security/ir.model.access.csv:2-7): account manager and accountant groups full rights on budgets, positions, lines; a line-level rule grants all internal users read/write/create (no delete) on budget lines (csv:7).
- Record rules: three global multi-company rules limit visibility to the user's current company hierarchy (security/account_budget_security.xml:5-24). Rule uses the user's main company rather than the set of allowed companies (xml:9): effect for multi-company sessions UNKNOWN.
- Constraint: a budgetary position must have at least one ledger account (account_budget.py:40-44).
- The "practical amount" is computed with a direct database query on analytic lines, filtered by analytic account, date range and the position's accounts (account_budget.py:117-129). Not company-filtered in that query; the query column is the "Project Account" column of analytic lines in core (core:analytic/models/analytic_line.py:16-22), so actuals for accounts of other analytic plans may read as zero (analytic plans use separate columns, core:analytic/models/analytic_plan.py:120) — inferred, not run.
- No crons, server actions or external calls. Chatter/tracking on budget state (account_budget.py:64).

## 4. Odoo 19 compatibility
- `group_ids` on res.users (base_account_budget/__init__.py:30) matches Community 19 (core:base/models/res_users.py:257).
- `analytic.group_analytic_accounting` exists (core:analytic/security/analytic_security.xml:35).
- `general_account_id` on analytic line exists (core:account/models/account_analytic_line.py:19). `analytic.view_account_analytic_account_form` and xpath group `main` exist (core:analytic/views/analytic_account_views.xml:3,28).
- `user.company_id` inside rule domain: not checked. `groups="account.group_account_user"`/menus exist. No mismatch found for what was checked; views file only partly read.

## 5. Custom-to-custom dependencies
- None declared in manifest. The module sits inside bundle folder `base_accounting_kit-19.0.3.3.1` next to sibling folders `base_accounting_kit` and `cybrosys_support_client` (directory listing only; relation not established).

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether any other module consumes budget data to block or warn on spending.
- UNKNOWN — EVIDENCE INSUFFICIENT: actual-vs-plan figures for analytic accounts outside the project plan (runtime not observed).
- UNKNOWN — EVIDENCE INSUFFICIENT: multi-company behaviour of the record rules and the raw query.
- UNKNOWN — EVIDENCE INSUFFICIENT: relation of this module to sibling bundle folders.
