# Source Map (candidate) — `project_mrp_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_mrp_account` |
| Display name | MRP Account Project |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `452ecbf9b890aac5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_mrp_account/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp_account`, `project_mrp`
- Direct dependents in 300-module list (1): `project_mrp_stock_landed_costs`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Monitor MRP account using project
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `stock.move`, `stock.rule`, `mrp.production`, `project.project`, `mrp.workorder`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.move`, `stock.rule`, `mrp.production`, `project.project`, `mrp.workorder`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 35 of 35 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project_mrp_account (revision 19.0.post20260921)
Scope: Odoo Community read-only study. Pointers `module/path:LINE`; (TEST) = test-derived. Cost attribution: manufacturing consumption and work time charged to a project's analytic accounts.

## A. Capabilities and activation
- Books manufacturing costs (component consumption and work-centre time) of a manufacturing order onto the analytic accounts of its linked project, and shows them as a cost line in project profitability (project_mrp_account/__manifest__.py:6,8; project_mrp_account/models/project_project.py:30-55).
- Glue module: depends on mrp_account and project_mrp; auto_install so it activates when both are installed (project_mrp_account/__manifest__.py:8,12). mrp_account and project_mrp are themselves auto_install (mrp_account/__manifest__.py:21,41; project_mrp/__manifest__.py:9,16).
- Conditional on data: nothing happens for a manufacturing order without a project, or a project without analytic accounts (project_mrp_account/models/stock_move.py:10-12; project_mrp_account/models/mrp_production.py:10-16).

## B. Objects, relationships, lifecycle
- Project link (from project_mrp): a bill of materials can carry a project; a manufacturing order takes the project of its BOM unless created from the project screen, and stays editable; procurements from an MO pass its project to child manufacturing orders (project_mrp/models/mrp_bom.py:9; project_mrp/models/mrp_production.py:9-15; project_mrp/models/stock.py:9-23; project_mrp_account/models/stock_rule.py:9-13).
- Consumption cost: component stock moves of an MO use the project's analytic distribution (all project accounts at 100%) in preference to the standard one, and the resulting analytic entries are tagged category "Manufacturing Order" (project_mrp_account/models/stock_move.py:10-18; category value added by mrp_account/models/analytic_account.py:79-90).
- Work-centre time: when a work order records cost/hours, an extra analytic entry set is created from the project distribution and attached to the work order, next to the standard work-centre entries (project_mrp_account/models/mrp_workorder.py:9-14; mrp_account/models/mrp_workorder.py:10,42-59).
- Changing the project on a started (non-draft) MO regenerates analytic entries of its raw-material moves and work orders (project_mrp_account/models/mrp_production.py:28-34) (TEST: project_mrp_account/tests/test_analytic_account.py:173-227).
- Profitability: sums analytic entries of category "Manufacturing Order" on the project's accounts, converts to project currency, and shows them as billed cost with sequence 12; a jump link to manufacturing orders is offered to manufacturing users when one project is viewed. The ordinary analytic-cost line excludes this category to avoid double counting (project_mrp_account/models/project_project.py:14-55) (TEST: project_mrp_account/tests/test_project_profitability.py:17-63).
- Smart button on MO to view the project's analytic accounts, shown when any exist (project_mrp_account/models/mrp_production.py:10-26).
- Behaviours covered by tests: consumed-quantity changes update amounts, backorders, component quantity set to zero deletes entries, mixed work-centre/MO accounts, cross-plan distribution, BOM-level project generation on work-order done without duplicates on MO done (TEST: project_mrp_account/tests/test_analytic_account.py:68-172,267-428,457-495).

## C. Validations, security, multi-company
- Confirming an MO is blocked if its project lacks an analytic account on any plan that is "mandatory" for the manufacturing-order business domain (relevance may depend on the produced product's category) (project_mrp_account/models/mrp_production.py:36-56) (TEST: project_mrp_account/tests/test_analytic_account.py:429-456).
- A second check at analytic-entry creation raises if mandatory plans are missing on the project (project_mrp_account/models/stock_move.py:20-33).
- Entries are created with elevated rights so users without accounting rights can still consume/scrap (stock_account/models/stock_move.py:223-227; project_mrp_account/models/mrp_workorder.py:14) (TEST: project_mrp_account/tests/test_analytic_account.py:497-535, skipped if timesheet_grid absent).
- Plans are looked up in the MO's company (project_mrp_account/models/mrp_production.py:39-43). Project field excludes templates (project_mrp/models/mrp_production.py:9). Cross-company handling of profitability: values converted with the project's company (project_mrp_account/models/project_project.py:41-42); further cross-company behaviour: UNKNOWN — EVIDENCE INSUFFICIENT
- No access-control or record-rule files in this module (manifest lists only demo data, project_mrp_account/__manifest__.py:9-11). Stat buttons for BOMs/MOs on the project show only to manufacturing users (project_mrp/models/project_project.py:64-66).

## D. Handoffs (owner)
- Inventory moves and production: mrp / stock. Analytic line creation and distribution engine: stock_account / analytic (stock_account/models/analytic_account.py:33). Category selection: mrp_account. Project profitability panel: project / project_account. General-ledger (valuation) postings of manufacturing: mrp_account / stock_account, unchanged by this module. Purchase: none.

## E. Configuration that changes outcomes
- Analytic plans' applicability (mandatory/optional, business domain "manufacturing order", product category) (project_mrp_account/models/mrp_production.py:39-47). Project analytic accounts per plan (analytic/models/analytic_line.py:61-73). Project on BOM or MO.

## F. Extension path
- Extends mrp.production, mrp.workorder, project.project, stock.move, stock.rule (project_mrp_account/models/*.py). Dependent module: project_mrp_stock_landed_costs (manifest grep). Upstream: project_mrp extends mrp.bom, mrp.production, project.project, stock.rule, stock.move.

## G. Not verified
- Timing rule for when raw-material entries are posted (on consumption vs completion) beyond test titles: UNKNOWN — EVIDENCE INSUFFICIENT
- Interaction with landed costs: UNKNOWN — EVIDENCE INSUFFICIENT
- Currency/company edge cases in multi-company projects: UNKNOWN — EVIDENCE INSUFFICIENT

