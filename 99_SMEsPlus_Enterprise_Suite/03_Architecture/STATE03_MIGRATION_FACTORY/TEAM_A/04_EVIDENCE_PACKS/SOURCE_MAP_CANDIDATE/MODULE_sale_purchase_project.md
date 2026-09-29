# Source Map (candidate) — `sale_purchase_project`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_purchase_project` |
| Display name | Sale Purchase Project |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a6ea169a269c3ae3` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_purchase_project/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_purchase`, `project_purchase`, `sale_project`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales / Technical Bridge
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `sale.order.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `sale.order.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 10 of 10 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_purchase_project
Source revision: 19.0.post20260921 | Module: "Sale Purchase Project" (sale_purchase_project/__manifest__.py:5), summary "Technical Bridge" (:6) | depends: sale_purchase, project_purchase, sale_project (:10) | auto_install true (:11) | LGPL-3 (:8)
Basis: static reading of manifest and the single model file; the one test read.

## A. Capabilities and optionality
- A1. When a service sold on an order is subcontracted through a purchase order (service-to-purchase), the purchase line inherits the project's analytic distribution and the purchase order is linked to the project. sale_purchase_project/models/sale_order_line.py:9-20
- A2. Automatic bridge when the three parents are present. sale_purchase_project/__manifest__.py:10-11

## B. Objects, relationships, lifecycle
- B1. Purchase line preparation: if the sales line has no analytic distribution of its own and the order's project defines one, the purchase line takes the project's. sale_purchase_project/models/sale_order_line.py:9-14
- B2. Purchase order preparation: the created purchase order records the sales order's project. sale_purchase_project/models/sale_order_line.py:16-20
- B3. Trigger: confirmation of an order in state "sale" containing service products flagged "service to purchase" (owner sale_purchase); the RFQ is created in draft. sale_purchase/models/sale_order_line.py:27,122,174 (owner of the two hooks)
- B4. (TEST) Two orders sharing a project whose analytic account is set: confirming both creates two draft POs, one PO line per order; the line whose sales line has no distribution gets the project's account at 100%; the line whose sales line already has its own distribution keeps that one. sale_purchase_project/tests/test_sale_purchase_project.py:10-43

## C. Validations, security, multi-company
- C1. No constraints, groups, ACLs or rules. sale_purchase_project/ (file list)
- C2. Project analytic lookup runs on the order's project record; access behaviour for users without project rights: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. Purchase order and line creation: purchase / sale_purchase. Project cost tracking: project_purchase (purchase orders/bills on the project). Analytic distribution mechanics: analytic/project (owner project, sale_project).
- D2. No inventory logic.

## E. Configuration that changes outcomes
- E1. Product "service to purchase" setting on the service product and its vendor list. sale_purchase/models/sale_order_line.py:27; (TEST) sale_purchase_project/tests/test_sale_purchase_project.py:25
- E2. The order's project and its analytic account/plan distribution. sale_purchase_project/models/sale_order_line.py:11-13

## F. Effective extension path (modules)
- Depended on by: none (grep of manifests). Overrides hooks _purchase_service_prepare_line_values (also in sale_purchase) and prepares order values.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: multi-project orders; effect of the project-on-PO field on later bill/cost reporting (owned by project_purchase, not opened).

