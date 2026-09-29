# Source Map (candidate) — `spreadsheet_dashboard_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `spreadsheet_dashboard_account` |
| Display name | Spreadsheet dashboard for accounting |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `51a02165618533c1` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/spreadsheet_dashboard_account/` |
| auto_install / application | ['account'] / None |

## 2. Dependencies
- Direct dependencies (manifest): `spreadsheet_dashboard`, `account`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/Dashboard / Spreadsheet
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (0): —
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: —

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 14 of 17 source pointers resolve to an existing file and in-range line (3 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: spreadsheet_dashboard_account (Invoicing dashboard)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/spreadsheet_dashboard_account.json. Pointers are `module/path:LINE`; JSON payload pointers cite the file (no meaningful line numbers). (TEST) = derived from tests; this module ships none.

## A. Capabilities / functions
- Ships one ready-made read-only "Invoicing" dashboard in the Dashboards app, filed under the Finance group (spreadsheet_dashboard_account/data/dashboards.xml:4-9, group defined spreadsheet_dashboard/data/dashboard.xml:4-7).
- Conditional-on-install: depends on the dashboard framework and accounting (spreadsheet_dashboard_account/__manifest__.py:9); auto_install is set on account (spreadsheet_dashboard_account/__manifest__.py:14), so it appears automatically when accounting is installed. Not an application; no settings.
- Dashboard content (from the bundled dashboard definition, spreadsheet_dashboard_account/data/files/invoicing_dashboard.json): headline tiles for "Invoiced", "Average Invoice" and "DSO" (days sales outstanding), a trend line, ranked breakdowns by product category, country, product and salesperson, and a top list of customer invoices ordered by total. Filters: period, country, product category, product, salesperson (same file).
- Sequence 20 among dashboards and published on install (spreadsheet_dashboard_account/data/dashboards.xml:11-12).

## B. Business objects, relationships, lifecycle
- Reads two accounting sources: the journal-entry model (customer invoices list) and the invoice analysis report (all pivots and KPIs) (spreadsheet_dashboard_account/data/files/invoicing_dashboard.json; declared main data model spreadsheet_dashboard_account/data/dashboards.xml:7).
- Population rule for the measures: only invoice/refund documents whose state is neither draft nor cancelled are counted; income covers customer invoices and customer credit notes; "unpaid" filters on payment status "not paid" (invoicing_dashboard.json, data-source filters).
- Empty-data behaviour: an alternative sample dashboard is bundled and used when the main data model has no records (sample path spreadsheet_dashboard_account/data/dashboards.xml:8; emptiness check spreadsheet_dashboard/models/spreadsheet_dashboard.py:66-73; sample loader :59-64).
- No lifecycle of its own: the dashboard record is a static definition; content is computed live from accounting data when opened.

## C. Validations, automation, security, multi-company
- Visibility: restricted to the accounting read-only group and the invoicing group (spreadsheet_dashboard_account/data/dashboards.xml:10). Framework rule: a user sees only dashboards whose group list intersects their groups (spreadsheet_dashboard/security/security.xml:4-9); dashboard managers see all (spreadsheet_dashboard/security/security.xml:31-36).
- Company scoping: dashboard records carry no company restriction here (company field not set in dashboards.xml), and the framework rule lets company-less dashboards through (spreadsheet_dashboard/security/security.xml:11-15). The figures themselves obey the viewer's access to the underlying accounting data (the framework checks read access on the main model and falls back to elevated counting only for the emptiness test: spreadsheet_dashboard/models/spreadsheet_dashboard.py:66-72). Whether cell values are shown to a group lacking accounting read rights: UNKNOWN — EVIDENCE INSUFFICIENT.
- No cron, no constraints.

## D. Accounting / payroll / analytic handoffs
- Owner of all numbers: account (invoice documents and invoice analysis report). This module only presents; it writes no entries and holds no configuration of accounting.
- DSO figure and ratio columns are spreadsheet formulas inside the definition (invoicing_dashboard.json); exact DSO definition: UNKNOWN — EVIDENCE INSUFFICIENT (not traced).
- Currency: framework supplies the viewer company's currency to the sheet (spreadsheet_dashboard/models/spreadsheet_dashboard.py:51-52); multi-currency conversion behaviour of the report: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration / defaults that change outcomes
- Group list on the dashboard record decides who sees it (dashboards.xml:10); admins with dashboard-manager rights can edit assignment.
- Period filter and other filters are viewer-side choices (invoicing_dashboard.json filters).

## F. Effective extension path (module names only)
- Extends: spreadsheet_dashboard (record types and groups), account (data). Peer dashboard modules in the same family: spreadsheet_dashboard_hr_expense, spreadsheet_dashboard_stock_account, spreadsheet_dashboard_hr_timesheet, spreadsheet_dashboard_event_sale, spreadsheet_dashboard_pos_restaurant, spreadsheet_dashboard_sale_timesheet, spreadsheet_dashboard_im_livechat (manifest grep).
- Manifest dependents on spreadsheet_dashboard_account: none found.

## G. Not verified
- DSO definition and multi-currency treatment: UNKNOWN — EVIDENCE INSUFFICIENT.
- Data exposure to users lacking accounting rights: UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; no universal rule asserted.

