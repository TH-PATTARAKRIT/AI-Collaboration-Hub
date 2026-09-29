# Source Map (candidate) — `spreadsheet_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_account` |
| Display name | Spreadsheet Accounting Formulas |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `324b9a79276e529a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_account/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet`, `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (1): `scgl_dashboard_finance` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Accounting / Spreadsheet Accounting formulas
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `res.company`, `account.account`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.company`, `account.account`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 36 of 36 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: spreadsheet_account
Source revision: 19.0.post20260921 | Path root: odoo/addons | Method: read-only source reading, neutral wording

## A. Capabilities
- Adds accounting functions to the spreadsheet engine so a sheet can pull ledger figures: ODOO.CREDIT, ODOO.DEBIT, ODOO.BALANCE, ODOO.RESIDUAL, ODOO.PARTNER.BALANCE, ODOO.BALANCE.TAG, ODOO.ACCOUNT.GROUP, ODOO.FISCALYEAR.START / END (spreadsheet_account/static/src/accounting_functions.js:177, 210, 243, 282, 302, 343, 359, 395, 438).
- Server-side data services behind those functions: debit/credit, residual amount, partner balance, balance by account tag, account codes by account type, company fiscal-year dates, and a "Cell Audit" drill-down to the underlying journal items (spreadsheet_account/models/account.py:93-231; spreadsheet_account/models/res_company.py:9-30).
- Auto-install: installs automatically when both `spreadsheet` and `account` are present (spreadsheet_account/__manifest__.py:`depends`, `auto_install`). Front-end pieces are loaded into the spreadsheet bundle (manifest `assets`) and use a plugin registering getters (spreadsheet_account/static/src/plugins/accounting_plugin.js:12-22).
- Account-group auto-complete helper in the formula editor (spreadsheet_account/static/src/account_group_auto_complete.js) - content not analysed.

## B. Business objects / behaviour
- No new stored object and no state. It extends the account (account.account) and company (res.company) objects with read-only query services (spreadsheet_account/models/account.py:12-13; models/res_company.py:6-7).
- Period selection: yearly (company fiscal year, respecting fiscal-year end day/month), monthly, quarterly, or daily (from fiscal year start to that day) (spreadsheet_account/models/account.py:15-42; TEST tests/test_debit_credit.py:332-590).
- Which entries count: balance-sheet accounts (those carrying opening balance) accumulate from the beginning up to period end; profit-and-loss accounts count only within the period (spreadsheet_account/models/account.py:49-58; TEST tests/test_debit_credit.py:145, 289 "do not count future years").
- Which accounts: either by account code prefixes (each code matches accounts starting with it) or by account tags; residual and partner-balance and drill-down default to receivable/payable accounts when no code is given, while debit/credit/balance return nothing without codes (spreadsheet_account/models/account.py:60-81; TEST tests/test_debit_credit.py:891-950).
- Entry state: posted only by default; option "include unposted" adds draft entries but still excludes cancelled ones (spreadsheet_account/models/account.py:83; TEST tests/test_debit_credit.py:765-890, tests/test_partner_balance.py:172).
- Filters: company (explicit id, otherwise current company), optional partner list (spreadsheet_account/models/account.py:45, 87-89; TEST tests/test_partner_balance.py:203). Partner balance returns 0 if no partner given (models/account.py:177-180).
- Results are sums of debit, credit, balance, or residual over the selected journal items (spreadsheet_account/models/account.py:123-131, 149-157, 176-188, 218-229).
- Fiscal-year dates: computed from the company's fiscal-year end setting; unknown company id returns "false" (spreadsheet_account/models/res_company.py:20-29; TEST tests/test_company_fiscal_year.py:88-102).
- Account group service returns codes for each requested account type in request order (spreadsheet_account/models/account.py:190-201; TEST tests/test_account_group.py:41).
- Drill-down: opens a journal-items list with the same domain, titled "Cell Audit" (spreadsheet_account/models/account.py:93-105; TEST tests/test_debit_credit.py:952-1035).

## C. Validations / security / multi-company
- No ACL file, groups, record rules or constraints in this module (manifest has no `data`). Queries run as the calling user through the standard journal-item search, so the user's existing access rights and record rules of `account` apply (spreadsheet_account/models/account.py:127, 153, 185, 227). UNKNOWN — EVIDENCE INSUFFICIENT for exact behaviour when the user has no access to the requested company (record rules not read).
- Most services are marked read-only for the database (safe on read replicas); the partner-balance and balance-by-tag services and account-group service lack that mark (spreadsheet_account/models/account.py:93,107,133 vs 159, 190, 203).
- Company handling: the requested company id is forced into the filter, so one sheet can show several companies side by side even when only one is active (TEST tests/test_debit_credit.py:258-287; spreadsheet_account/models/account.py:85).
- Account group lookup uses only the current company (spreadsheet_account/models/account.py:194).

## D. Handoffs
- Journal items, accounts, tags, fiscal-year settings: owned by `account` (spreadsheet_account/models/account.py:49-81; res_company.py:24-28).
- Spreadsheet engine, function registry, server-data loading: owned by `spreadsheet` (spreadsheet_account/static/src/plugins/accounting_plugin.js:1-30).
- Consumers of this module in Community: none found (manifest dependency grep and Python/JS references outside the module returned none).
- No accounting entry, approval or stock effect; read-only reporting.

## E. Configuration that changes outcomes
- Company fiscal-year end day/month (yearly and daily periods) (spreadsheet_account/models/account.py:23-41).
- Account type "include initial balance" property of each account (balance vs P&L treatment) (spreadsheet_account/models/account.py:50, 54).
- Account codes/tags maintained in `account`; the sheet's formula parameters (codes, date range, offset, company, unposted flag).

## F. Extension path
- Modules with spreadsheet_account as dependency: none found (manifest grep).
- Modules extending the account object (account.account) in general: l10n_de, l10n_dk, l10n_in, l10n_mx, l10n_pt, point_of_sale, spreadsheet_account, stock_account. Company object: not compiled for this note.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether enterprise-side dashboards use these functions (outside this source scope).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end evaluation details (offset handling, caching, error messages) - JS only sampled.
- UNKNOWN — EVIDENCE INSUFFICIENT: performance/limits for large ledgers.

