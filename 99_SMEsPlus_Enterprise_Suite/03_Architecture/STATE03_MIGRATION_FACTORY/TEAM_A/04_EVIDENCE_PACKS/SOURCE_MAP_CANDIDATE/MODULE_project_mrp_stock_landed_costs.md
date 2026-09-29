# Source Map (candidate) — `project_mrp_stock_landed_costs`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_mrp_stock_landed_costs` |
| Display name | Project MRP Landed Costs |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G04 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `7a37481799a08bb0` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_mrp_stock_landed_costs/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `project_mrp_account`, `mrp_landed_costs`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Supply Chain/Manufacturing / Technical Bridge
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 17 of 17 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project_mrp_stock_landed_costs
Source revision: 19.0.post20260921 (Odoo 19 Community). Read-only trace; neutral business language; no code copied.

## A. Capabilities / activation
- "Technical bridge": when landed costs are applied to manufacturing orders, the project's analytic allocation is copied onto the resulting journal lines. project_mrp_stock_landed_costs/__manifest__.py:6,8
- Conditional: auto-installs when project_mrp_account and mrp_landed_costs are both installed. project_mrp_stock_landed_costs/__manifest__.py:8-9
- No settings, groups, views, data, security, tests of its own. project_mrp_stock_landed_costs/__manifest__.py:3-12

## B. Business objects and relationships
- Extends the valuation-adjustment line (one row per stock movement receiving landed cost, owned by stock_landed_costs). project_mrp_stock_landed_costs/models/stock_landed_costs.py:6-7
- Rule: when the landed cost's "Apply On" is Manufacturing Orders, the accounting line's analytic distribution is taken from the project set on the manufacturing order that produced the movement. project_mrp_stock_landed_costs/models/stock_landed_costs.py:9-13
- The manufacturing order's project defaults from its bill of materials' project (editable, stored). project_mrp/models/mrp_production.py:9-15
- The "Manufacturing Orders" target option is added by mrp_landed_costs; only finished-goods movements (and by-products that carry a cost share) are targeted. mrp_landed_costs/models/stock_landed_cost.py:10-14,23-28
- Lifecycle owned by stock_landed_costs (draft/posted/cancelled). stock_landed_costs/models/stock_landed_cost.py:54-58

## C. Validations / security / multi-company
- No validation of its own; for a manufacturing order without project, the distribution is empty (read from source, not tested). project_mrp_stock_landed_costs/models/stock_landed_costs.py:11-12
- Security inherited: managers only, company record rule. stock_landed_costs/security/ir.model.access.csv:2-4; stock_landed_costs/security/stock_landed_cost_security.xml:4-8
- The manufacturing-order selector on the landed cost is restricted to the stock manager group. mrp_landed_costs/models/stock_landed_cost.py:12-14

## D. Handoffs
- Accounting entry creation [stock_landed_costs]; manufacturing target [mrp_landed_costs]; project/analytic source [project_mrp / project_mrp_account / analytic]. stock_landed_costs/models/stock_landed_cost.py:112-137; mrp_landed_costs/models/stock_landed_cost.py:23-28
- Sibling for transfer targets is project_stock_landed_costs. project_stock_landed_costs/models/stock_landed_costs.py:11-12

## E. Configuration that changes outcomes
- Project on the manufacturing order (and on its BoM as default). project_mrp/models/mrp_production.py:9-15
- Landed-cost "Apply On" value. project_mrp_stock_landed_costs/models/stock_landed_costs.py:11

## F. Effective extension path (other Community modules extending stock.valuation.adjustment.lines)
- project_mrp_stock_landed_costs, project_stock_landed_costs. Others: none found.

## G. Not verified
- Interaction with the manufacturing-side analytic handling in project_mrp_account for the same movements: UNKNOWN — EVIDENCE INSUFFICIENT
- Behaviour where the manufacturing order has no project but a default analytic value exists on the base line: UNKNOWN — EVIDENCE INSUFFICIENT
- Case where a landed cost mixes transfers and manufacturing orders: UNKNOWN — EVIDENCE INSUFFICIENT

