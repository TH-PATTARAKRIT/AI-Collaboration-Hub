# Source Map (candidate) — `project_stock_landed_costs`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_stock_landed_costs` |
| Display name | Project Stock Landed Costs |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `3722146b4b19d173` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_stock_landed_costs/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `project_stock_account`, `stock_landed_costs`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Inventory / Technical Bridge
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `stock.valuation.adjustment.lines`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.valuation.adjustment.lines`

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

# Source Map trace note: project_stock_landed_costs
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- "Technical bridge": copies the project's analytic (cost-tracking) allocation onto the journal lines produced when a landed cost is posted against transfers. project_stock_landed_costs/__manifest__.py:6,8
- Conditional: installs automatically only when project_stock_account and stock_landed_costs are both installed. project_stock_landed_costs/__manifest__.py:8-9
- No settings, groups, views, data, security records, tests. project_stock_landed_costs/__manifest__.py:3-12

## B. Business objects and relationships
- Extends the valuation-adjustment line (one row per stock movement receiving a share of landed cost; owned by stock_landed_costs). project_stock_landed_costs/models/stock_landed_costs.py:6-7; stock_landed_costs/models/stock_landed_cost.py:304-305
- Rule: when the landed cost targets "Transfers", the generated accounting line gets an analytic distribution derived from the project set on the movement's transfer. project_stock_landed_costs/models/stock_landed_costs.py:9-13
- Project link on transfers is owned by project_stock (transfer has a project reference, templates excluded). project_stock/models/stock_picking.py:9
- The project's distribution is one analytic account at 100 percent, or empty if the project has no account. analytic/models/analytic_line.py:71-73 (project inherits this mixin: project/models/project_project.py:26)
- Lifecycle is entirely that of landed cost (draft/posted/cancelled), owned by stock_landed_costs. stock_landed_costs/models/stock_landed_cost.py:54-58

## C. Validations / security / multi-company
- No validation of its own. If the transfer has no project, the distribution assigned is empty, i.e. any default analytic value from the base line values is overwritten with an empty result (as read from the source; not exercised by tests). project_stock_landed_costs/models/stock_landed_costs.py:11-12
- Security and company scoping inherited from landed costs: manager group only; company record rule. stock_landed_costs/security/ir.model.access.csv:2-4; stock_landed_costs/security/stock_landed_cost_security.xml:4-8

## D. Handoffs
- Accounting: analytic split lands on the landed-cost journal entry lines [stock_landed_costs creates the entry; account/analytic own the analytic model]. stock_landed_costs/models/stock_landed_cost.py:112-137,360-365
- Project ownership of analytic account: [project / analytic]. analytic/models/analytic_line.py:71-73
- Contrast: the regular stock-movement bridge applies project distribution only when the operation type has "analytic costs" enabled; this landed-cost bridge has no such condition in its own code. project_stock_account/models/stock_move.py:11-15; project_stock_landed_costs/models/stock_landed_costs.py:11-12

## E. Configuration that changes outcomes
- Which project is set on the transfer; landed cost "Apply On" must be Transfers (other targets, e.g. manufacturing, are handled by the sibling bridge). project_stock_landed_costs/models/stock_landed_costs.py:11; project_mrp_stock_landed_costs/models/stock_landed_costs.py:11

## F. Effective extension path (other Community modules extending stock.valuation.adjustment.lines)
- project_stock_landed_costs, project_mrp_stock_landed_costs. Others: none found.

## G. Not verified
- Whether the missing operation-type "analytic costs" check is intentional: UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour with multiple transfers from different projects in one landed cost (each line reads its own move's transfer per code, no test): UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour when the project's analytic account belongs to a different company: UNKNOWN — EVIDENCE INSUFFICIENT

