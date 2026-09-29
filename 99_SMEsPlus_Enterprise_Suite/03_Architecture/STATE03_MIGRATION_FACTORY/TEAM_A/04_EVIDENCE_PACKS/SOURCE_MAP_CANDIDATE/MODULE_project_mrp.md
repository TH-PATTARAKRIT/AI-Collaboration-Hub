# Source Map (candidate) — `project_mrp`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_mrp` |
| Display name | MRP Project |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `59866c52e09d5745` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_mrp/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `mrp`, `project`
- Direct dependents in 300-module list (2): `project_mrp_account`, `project_mrp_sale`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Monitor MRP using project
- Inventory of user-facing artifacts (counts): menu items 0, views 3, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `stock.rule`, `stock.move`, `mrp.production`, `project.project`, `mrp.bom`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `stock.rule`, `stock.move`, `mrp.production`, `project.project`, `mrp.bom`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 24 of 24 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — project_mrp
Source revision: 19.0.post20260921 | Module: "MRP Project" (project_mrp/__manifest__.py:5) | depends: mrp, project (:9) | License LGPL-3 (:18)
Basis: static reading of 5 python files, 3 views, 1 access file; no tests exist in this module.

## A. Capabilities and optionality
- A1. Lets a manufacturing order and a bill of materials be tied to a project, and lets the project show its bills of materials and manufacturing orders as counted shortcuts. project_mrp/models/mrp_bom.py:9; project_mrp/models/mrp_production.py:9; project_mrp/models/project_project.py:64-84
- A2. Conditional: bridge module, installed automatically when mrp and project are both present. project_mrp/__manifest__.py:16
- A3. The project shortcuts appear only for users in the manufacturing user group. project_mrp/models/project_project.py:66; project_mrp/views/project_project_views.xml:10,20,30,40
- A4. Project page gets two embedded tabs (Bills of Materials, Manufacturing Orders) on both the project task action and the project updates action. project_mrp/views/project_project_views.xml:3-41
- A5. Manufacturing order form gets a "Project" button and a project field; BoM form gets a project field; all restricted to the project user group. project_mrp/views/mrp_production_views.xml:19-35; project_mrp/views/mrp_bom_views.xml:8-10

## B. Business objects, relationships, lifecycle
- B1. BoM (mrp.bom, owner mrp) gets an optional project link; templates are excluded from the choice. project_mrp/models/mrp_bom.py:9
- B2. Manufacturing order (mrp.production, owner mrp) gets a project link that is stored, computed, and still editable by the user. project_mrp/models/mrp_production.py:9
- B3. The order's project defaults to the BoM's project whenever the BoM changes; this default is skipped when the order is created from the project's own action. project_mrp/models/mrp_production.py:11-15; project_mrp/models/project_project.py:57
- B4. Follow-on manufacturing orders raised through procurement inherit the project: the move passes the project of its procurement group only when that group has exactly one manufacturing order, and the manufacturing rule writes it onto the new order. project_mrp/models/stock.py:11-12,19-23
- B5. Generating a BoM from an order carries the order's project as the default for the new BoM. project_mrp/models/mrp_production.py:17-20
- B6. No new state machine. Order and BoM states remain those of mrp.
- B7. Project counts are read-grouped totals of BoMs / orders pointing at the project (no company or archived filter added here). project_mrp/models/project_project.py:12-30

## C. Validations, security, multi-company
- C1. No constraints. Only a domain that excludes project templates on both links. project_mrp/models/mrp_bom.py:9; project_mrp/models/mrp_production.py:9
- C2. Access: project users get read-only access to BoM and BoM lines (no write/create/delete), so they can see BoMs linked to projects. project_mrp/security/ir.model.access.csv:2-3
- C3. Counts on the project are visible only to the manufacturing user group (field-level group). project_mrp/models/project_project.py:9-10
- C4. Multi-company: no explicit check that project company equals order/BoM company. UNKNOWN — EVIDENCE INSUFFICIENT for cross-company link prevention (rules live in mrp/project).

## D. Handoffs
- D1. Manufacturing, component moves, valuation: mrp / stock / stock_account. Project only receives a link.
- D2. Project cost/analytic postings of manufacturing: not in this module; extension module project_mrp_account (F2). UNKNOWN — EVIDENCE INSUFFICIENT for what it posts (not read).
- D3. Sales-originated linkage: project_mrp_sale (F2), not read.

## E. Configuration/defaults that change outcomes
- E1. BoM project is the sole default source for the order project (B3); an order with a manually chosen project keeps it only until the BoM is changed again (compute re-runs on BoM change). project_mrp/models/mrp_production.py:11-15
- E2. Context flag from project action suppresses the BoM default so the order keeps the project chosen from the project (B3). project_mrp/models/mrp_production.py:13

## F. Effective extension path (grep of _inherit)
- F1. This module extends: stock.rule, stock.move, mrp.production, project.project, mrp.bom. project_mrp/models/stock.py:7,17; mrp_production.py:7; project_project.py:7; mrp_bom.py:7
- F2. Modules that depend on project_mrp: project_mrp_account, project_mrp_sale (reverse dependency index).

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: whether sub-assembly orders in multi-level BoMs always inherit the project (B4 depends on group having one order).
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: multi-company enforcement (C4).
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: any test-derived behaviour (module has no tests).

