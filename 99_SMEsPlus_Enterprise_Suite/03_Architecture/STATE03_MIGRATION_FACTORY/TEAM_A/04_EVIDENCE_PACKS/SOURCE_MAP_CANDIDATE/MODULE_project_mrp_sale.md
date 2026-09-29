# Source Map (candidate) — `project_mrp_sale`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_mrp_sale` |
| Display name | MRP Project Sale |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6c557e22ae7057cf` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_mrp_sale/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `project_mrp`, `sale_mrp`, `sale_project`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Technical Bridge
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 8 of 8 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project_mrp_sale (Odoo 19 Community, revision 19.0.post20260921)
## A. Capabilities; core / optional / conditional
- Technical bridge with no models, views, data or security of its own; only a manifest and one test. project_mrp_sale/__manifest__.py:2-11 (summary "Technical Bridge")
- Conditional: installs automatically when manufacturing-project link (project_mrp), sales-manufacturing (sale_mrp) and sale_project are all present. project_mrp_sale/__manifest__.py:7,9
## B. Business objects and lifecycle
- No own objects. Observed outcome (TEST): a manufacturing order created on sale confirmation takes the project of the sale order when no project was set on it beforehand; before confirmation no order exists. project_mrp_sale/tests/test_sale_mrp_account.py:9-17
- Mechanism lies in the parents, not here: the sale order line passes its order's project into procurement values (sale_project/models/sale_order_line.py:489-493); the manufacturing rule copies that project to the manufacturing order (project_mrp/models/stock.py:8-14); manufacturing order project otherwise defaults from its bill of materials (project_mrp/models/mrp_production.py:9-16).
## C. Validations, automation, security, multi-company
- No constraints, rules or access entries in this module: project_mrp_sale (file inventory: only __init__, __manifest__, tests).
- Security and company scoping come from project_mrp (access file project_mrp/__manifest__.py:9) and sale_project; not analysed further: UNKNOWN — EVIDENCE INSUFFICIENT
## D. Accounting / inventory / analytic handoffs
- Manufacturing and stock: mrp / sale_mrp. Project link: project_mrp. Order-to-project: sale_project. This module owns nothing.
- Analytic/cost effect of the project on the manufacturing order: UNKNOWN — EVIDENCE INSUFFICIENT
## E. Configuration
- Project on the sale order (order-level) and on the bill of materials drive the result; no setting in this module. project_mrp/models/mrp_bom.py:9
## F. Extension path
- None: no _inherit in this module. Dependents in tree: none.
## G. Not verified
- Whether the bridge is needed for the flow at all (behaviour may be delivered by parents): UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour with multiple sale lines / several manufacturing orders: UNKNOWN — EVIDENCE INSUFFICIENT

