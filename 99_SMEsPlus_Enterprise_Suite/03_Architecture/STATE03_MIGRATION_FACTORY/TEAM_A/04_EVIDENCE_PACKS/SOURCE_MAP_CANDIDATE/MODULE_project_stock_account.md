# Source Map (candidate) — `project_stock_account`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_stock_account` |
| Display name | Project Stock Account |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6766bdaabf16960e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_stock_account/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `stock_account`, `project_stock`
- Direct dependents in 300-module list (3): `project_stock_landed_costs`, `sale_project_stock`, `sale_project_stock_account`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Handle analytics in Stock pickings with Project
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `stock.picking.type`, `stock.move`, `project.project`, `account.analytic.applicability`, `account.analytic.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.picking.type`, `stock.move`, `project.project`, `account.analytic.applicability`, `account.analytic.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 27 of 27 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — project_stock_account
Source revision: 19.0.post20260921 | Module: "Project Stock Account" (project_stock_account/__manifest__.py:4) | depends: stock_account, project_stock (:8) | License LGPL-3 (:14)
Basis: static reading of 5 model files, 1 view; 1 test file (3 tests) read.

## A. Capabilities and optionality
- A1. When a stock transfer (picking) linked to a project is validated, the module records the transfer value as analytic cost/revenue lines against the project's analytic accounts, and shows them under project profitability as "Materials". project_stock_account/models/stock_move.py:11-15,24-29; project_stock_account/models/project_project.py:10-14,22-28
- A2. Optional per operation type: a flag "analytic costs" on the picking type; only meaningful for receipts and deliveries (field hidden otherwise) and only visible to analytic accounting users. project_stock_account/models/stock_picking_type.py:9; project_stock_account/views/stock_picking_type_views.xml:9
- A3. Conditional: bridge module, installed automatically when stock_account and project_stock are both present. project_stock_account/__manifest__.py:12
- A4. Adds an analytic-plan applicability domain "Stock Picking" so plans can be made mandatory/optional for transfers. project_stock_account/models/analytic_applicability.py:10-15
- A5. Adds an analytic-line category "Inventory Transfer" used to isolate these lines. project_stock_account/models/account_analytic_line.py:9

## B. Business objects, relationships, lifecycle
- B1. Picking (stock.picking, owner stock) carries the project link, defined in project_stock. project_stock/models/stock_picking.py:9 (project templates excluded)
- B2. Analytic lines are created per stock move at transfer validation, only for moves that either have no picking, or belong to a picking with a project and whose operation type has the flag on. project_stock_account/models/stock_move.py:24-29
- B3. Line label is the picking reference; category is set to "Inventory Transfer". project_stock_account/models/stock_move.py:17-22
- B4. Distribution: if the operation type has the flag on, the project's analytic distribution is used; if the project provides none, the standard distribution logic applies. project_stock_account/models/stock_move.py:11-15
- B5. Sign/amount (TEST): delivery of 3 x cost 100 and 5 x cost 200 produced lines of -300 and -1000; the receipt of same quantities produced +300 and +1000, each tagged with both project plans' accounts. (TEST) project_stock_account/tests/test_analytics.py:43-82,84-129
- B6. Profitability (TEST): after the receipt, project costs showed one "other costs" entry with billed 1300, to_bill 0 and total billed 1300; no revenue. (TEST) project_stock_account/tests/test_analytics.py:131-140
- B7. Lifecycle is that of the picking (confirm, validate); lines are produced at validation. (TEST) project_stock_account/tests/test_analytics.py:70-71

## C. Validations, security, multi-company
- C1. Mandatory-plan check: at line generation, every plan marked mandatory for "Stock Picking" must be set on the picking's project, otherwise validation is blocked with an error naming the missing plans and the project. project_stock_account/models/stock_move.py:31-43 (TEST: tests/test_analytics.py:142-166)
- C2. Profitability search runs with elevated rights (sudo) so any project reader sees the cost total; the drill-down action is offered only to users in the accounting read-only group. project_stock_account/models/project_project.py:32,56-57
- C3. No new access files or record rules. project_stock_account/__manifest__.py:9-11
- C4. Multi-company: costs are converted from each line's currency into the project's currency at the project company's rate. project_stock_account/models/project_project.py:37-51. Cross-company link prevention between picking and project: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Inventory movement and valuation: stock / stock_account (this module hooks their analytic-move creation via super). project_stock_account/models/stock_move.py:27-29
- D2. Analytic accounts, plans, applicability, analytic lines: analytic (account owner of analytic.line). Project-to-analytic account mapping and the profitability panel skeleton: project / project_account (line filter helper at project_account/models/project_project.py:122).
- D3. Re-invoicing of stocked products to customer: help text says products set for re-invoicing are billed to customer; the mechanism is not in this module. project_stock_account/models/stock_picking_type.py:9; owner UNKNOWN — EVIDENCE INSUFFICIENT (likely sale_project_stock_account, see F2).

## E. Configuration/defaults that change outcomes
- E1. Operation-type flag "analytic costs" (default off, no default declared) decides whether any line is created at all. project_stock_account/models/stock_picking_type.py:9
- E2. Mandatory/optional applicability rule for the "Stock Picking" domain decides whether validation may be blocked (C1). project_stock_account/models/analytic_applicability.py:10-15
- E3. Module sets ordering value 12 for the "other costs" section key, but the entry it builds is ordered by the separate key "other_costs_aal" taken from the parent map (test shows 15). project_stock_account/models/project_project.py:16-20,54 (TEST: tests/test_analytics.py:134)

## F. Effective extension path (grep of _inherit)
- F1. This module extends: account.analytic.applicability, stock.move, stock.picking.type, project.project, account.analytic.line. project_stock_account/models/*.py (line 7 or 8 of each)
- F2. Modules depending on project_stock_account: project_stock_landed_costs, sale_project_stock, sale_project_stock_account (reverse dependency index).

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: the base logic of analytic-line creation in stock_account (not read; only overrides seen).
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: where the parent map defines the "other_costs_aal" ordering value (not read; test shows 15).
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: behaviour for return transfers, cancelled/unreserved moves and backorders.
- G4. UNKNOWN — EVIDENCE INSUFFICIENT: sign convention rationale (outgoing negative, incoming positive) beyond what the tests show.

