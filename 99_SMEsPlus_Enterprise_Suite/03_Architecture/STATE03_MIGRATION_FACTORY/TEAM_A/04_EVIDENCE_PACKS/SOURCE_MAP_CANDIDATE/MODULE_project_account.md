# Source Map (candidate) — `project_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_account` |
| Display name | Project - Account |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G05 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `43d3cf8424a2a54b` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_account/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `account`, `project`
- Direct dependents in 300-module list (3): `project_hr_expense`, `project_purchase`, `sale_project`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Accounting/Accounting / project profitability items computation
- Inventory of user-facing artifacts (counts): menu items 0, views 7, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `project.project`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `project.project`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 32 of 32 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project_account
Source revision: 19.0.post20260921 | Path root: odoo/addons | Method: read-only source reading, neutral wording

## A. Capabilities
- Feeds the project "profitability" panel with accounting-derived figures: (1) "Vendor Bills" cost section for vendor bills carrying the project's analytic account, without a purchase order link; (2) "Other Revenues" and "Other Costs" from analytic lines on the project's analytic account not tied to journal items (project_account/models/project_project.py:14-68, 127-172; description project_account/__manifest__.py:`description`).
- Conditional/auto-install: installs automatically when its dependencies `account` and `project` are present (project_account/__manifest__.py:`depends`, `auto_install`).
- Section labels and display order defined here: Vendor Bills (11), Other Revenues (14), Other Costs (15) (project_account/models/project_project.py:77-91).
- Drill-down actions from panel rows: analytic entries (pivot/graph by date) for other revenues/costs; vendor bill list/form for Vendor Bills (project_account/models/project_project.py:70-75, 93-120; views/account_analytic_line_views.xml:3-32). Drill-down links only offered to Invoicing or Accounting read-only users (vendor bills, :16-19) and to Accounting read-only users (analytic lines, :165-167).
- Embedded "Analytic Items" shortcut on project screens for users in the analytic accounting group, only where the project has an analytic account (project_account/views/project_project_views.xml:26-46; action project_account/models/project_project.py:174-183).
- Partner pickers on project/task forms are limited to the customer search mode (project_account/views/project_project_views.xml:4-24; views/project_task_views.xml:4-30; views/project_sharing_project_task_views.xml:4-19).

## B. Business objects / lifecycle
- Extends project (project.project) only; no new object or state (project_account/models/project_project.py:11-12). Link to accounting = the project's analytic account (field owned by `project`: project/models/project_project.py:98).
- Vendor Bills rule: vendor bills/credit notes (in_invoice, in_refund) in draft or posted state, non-zero subtotal, not already counted elsewhere (a shared "already included" list, empty in the base project module: project/models/project_project.py:1032-1035, and extended by project_hr_expense:60-63, project_sale_expense:90-92, and used by project_purchase:146, sale_project:662), whose analytic distribution includes the project's analytic account (project_account/models/project_project.py:22-37).
- Amount rule: balance converted to project currency at line date; multiplied by the share of the distribution assigned to the project account; draft bills go to "to bill", posted to "billed"; sign reversed so costs are shown as negatives; section hidden if both are zero (project_account/models/project_project.py:40-68).
- Other items rule: analytic lines on the project account with no journal-item link, excluding manufacturing-order and stock-picking categories; negative amount = cost, positive = revenue; everything is shown as already billed/invoiced (to bill/to invoice stay 0), converted to project currency at company date (project_account/models/project_project.py:122-172; TEST project_account/tests/test_project_profitability.py:10-87 including lines of another company with foreign currency).
- Lifecycle: figures are recomputed each time the project panel is read; nothing is stored (project/models/project_project.py:998-1013).

## C. Validations / security / multi-company
- No constraints, no ACL file, no record rule in this module (manifest `data` lists only views).
- Data is read with elevated rights (sudo) for bill lines and analytic lines, so figures include records the viewing user may not open; only the drill-down link is gated by accounting groups (project_account/models/project_project.py:34, 132, 16-19, 165). The whole panel requires project user group (project/models/project_project.py:1000-1001).
- Multi-company: analytic lines of other companies on the same analytic account are included and converted into project currency (TEST project_account/tests/test_project_profitability.py:37-64). Currency conversion for bills is per line date; for analytic lines uses the project company (project_account/models/project_project.py:42-44, 156-157).
- Analytic account with several occurrences in one distribution: percentages summed (project_account/models/project_project.py:45-49).

## D. Handoffs
- Panel assembly, project analytic account, actions: owned by `project` (project/models/project_project.py:998-1059).
- Vendor bills / journal items / analytic lines: owned by `account` and `analytic` (project_account/models/project_project.py:34, 95, 112, 132).
- Vendor Bills section is called only by `sale_project` (its profitability step calls the bill step: sale_project/models/project_project.py:787); `project_purchase` replaces the bill step with a no-op and calls the shared cost routine itself for bills not linked to purchase orders (project_purchase/models/project_project.py:126-127, 216). With only `project` + `account` (this module) and no sales/purchase module, the Vendor Bills step has no caller found in this tree; only Other Revenues/Costs appear (inference; grep of callers, not run-tested).
- Extension points used by later modules: `_get_domain_aal_with_no_move_line` (sale_timesheet/models/project_project.py:485-488), `_get_add_purchase_items_domain` (project_hr_expense/models/project_project.py:31-33), picking-entry items (project_stock_account/models/project_project.py:22-31).

## E. Configuration that changes outcomes
- Project must have an analytic account; analytic accounting group affects the Analytic Items shortcut (project_account/views/project_project_views.xml:33, 44).
- Analytic distribution percentages on vendor bill lines; bill state; project currency.
- Installed sibling modules (sale_project, project_purchase, project_hr_expense, sale_timesheet, project_stock_account) change which items are included.

## F. Extension path (module names only)
- Modules with project_account in manifest dependencies: project_hr_expense, project_purchase, sale_project.
- Modules extending the project object (project.project): hr_timesheet, project_account, project_hr_expense, project_mrp, project_mrp_account, project_purchase, project_sale_expense, project_sms, project_stock, project_stock_account, sale_project, sale_project_stock, sale_timesheet.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: exact contents of the "already included" list in each extending module (only located, not analysed).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end rendering of the profitability panel (JS not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour when a project has no analytic account beyond the empty result implied by the domain filters.

