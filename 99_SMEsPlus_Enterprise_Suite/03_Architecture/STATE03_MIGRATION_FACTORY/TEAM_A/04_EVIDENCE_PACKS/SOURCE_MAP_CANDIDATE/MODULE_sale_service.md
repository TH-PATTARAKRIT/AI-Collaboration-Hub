# Source Map (candidate) — `sale_service`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `sale_service` |
| Display name | Sales - Service |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G02 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a2e80f380312c743` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/sale_service/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `sale_management`
- Direct dependents in 300-module list (1): `sale_project`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Sales/Sales / Interaction between Sales and services apps (project and planning)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 12 of 12 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — sale_service
Source revision: 19.0.post20260921 | Module: "Sales - Service" (sale_service/__manifest__.py:4) | depends: sale_management (:12) | NOT auto_install; LGPL-3 (:14)
Basis: static reading of the manifest and the single model file (no views, security, data, tests).

## A. Capabilities and optionality
- A1. Technical foundation for "service" sales lines used by service apps (project, planning): flags service lines, offers a shared service-line filter, improves how such lines are named and searched. sale_service/__manifest__.py:5-10; sale_service/models/sale_order_line.py:14-84
- A2. Pulled in as a dependency by sale_project (manifest grep); on its own it adds no visible menu or screen. UNKNOWN — EVIDENCE INSUFFICIENT for a stand-alone user-facing effect.

## B. Objects, relationships, lifecycle
- B1. Each sales line gets a stored "is a service" flag, true when the product type is service; recomputed on product type change. sale_service/models/sale_order_line.py:17,35-40
- B2. The flag column is created and back-filled directly during installation to avoid slow ORM recomputation. sale_service/models/sale_order_line.py:42-55
- B3. Shared service-line domain: is service; optionally excluding re-invoiced expense lines (default excluded); optionally only confirmed orders (default state "sale"). Callers switch each check off by keyword. sale_service/models/sale_order_line.py:19-33
- B4. Display name: when the context requests unit prices, several service lines of the same product in one order get their unit price prefixed to the extra name so they can be told apart. sale_service/models/sale_order_line.py:57-73
- B5. Search shortcut: name search filtered on service lines is served directly from the lines (newest orders first) with a supporting index, avoiding a join to orders. sale_service/models/sale_order_line.py:14,75-84

## C. Validations, security, multi-company
- C1. No constraints, groups, ACLs or rules in this module. The flag is computed with elevated rights so it can be stored regardless of the user. sale_service/models/sale_order_line.py:17
- C2. Multi-company: none. UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs
- D1. No accounting, inventory, purchase, or analytic logic. Project/task creation, timesheets and invoicing policy are owned by sale_project / sale_timesheet (F).
- D2. Any consumer of the service-line domain (project sale-item selectors) belongs to sale_project. sale_project/models/project_project.py:17-24

## E. Configuration that changes outcomes
- E1. Product type "service" determines the flag. sale_service/models/sale_order_line.py:40
- E2. Caller context switches (unit price display, hide partner reference). sale_service/models/sale_order_line.py:58-60

## F. Effective extension path (modules)
- Depended on by: sale_project (manifest grep). Extended in practice through sale_project and sale_timesheet on sale.order.line.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: effect of the partial index on database behaviour at scale; any runtime use of the naming feature outside sale_project.

