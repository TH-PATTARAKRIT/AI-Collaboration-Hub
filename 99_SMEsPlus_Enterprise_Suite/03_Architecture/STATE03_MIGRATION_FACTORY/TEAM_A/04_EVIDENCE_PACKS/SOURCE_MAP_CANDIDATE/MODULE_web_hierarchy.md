# Source Map (candidate) — `web_hierarchy`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `web_hierarchy` |
| Display name | Web Hierarchy |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `49a5c8c845d3422a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/web_hierarchy/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `web`
- Direct dependents in 300-module list (1): `hr_org_chart`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `base`, `ir.ui.view`, `ir.actions.act_window.view`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `base`, `ir.ui.view`, `ir.actions.act_window.view`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 26 of 26 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — web_hierarchy
Source revision: 19.0.post20260921 | Module: "Web Hierarchy" (web_hierarchy/__manifest__.py:4), category Hidden (:5), LGPL-3 (:29). Framework/UI module (brief note). Basis: static reading of the three server files, manifest, and view-parser / model excerpts.

## A. Capabilities and optionality
- A1. Adds a new screen type, "Hierarchy", which draws records as an organisation chart (tree of cards linked by a parent/child relation); intended for structures such as the employee organisation chart. web_hierarchy/__manifest__.py:9-14
- A2. Any list-of-records screen definition can declare this type; the view supports a card template ("hierarchy-box"), fields, optional icon, and flags for create/edit/delete, drag-and-drop and default order. web_hierarchy/models/ir_ui_view.py:7-20; web_hierarchy/static/src/hierarchy_arch_parser.js:28-56,68-70
- A3. Drag-and-drop (when the view enables it) re-parents a record by writing its parent field, i.e. an ordinary edit under the user's normal rights. web_hierarchy/static/src/hierarchy_model.js:1013-1024; web_hierarchy/static/src/hierarchy_arch_parser.js:50-52
- A4. Server support: every model gains a read method returning the searched records with their parent (and siblings/children when a single record is selected), with child ids attached if no explicit child field is defined. web_hierarchy/models/models.py:6-41
- A5. "Hierarchy" is registered as an allowed view mode of window actions and shown with a small icon in the view switcher. web_hierarchy/models/ir_actions.py:6-9; web_hierarchy/models/ir_ui_view.py:26,56-57
- A6. Optionality: not auto_install, not an application; depends on web; installed only when another module depends on it. web_hierarchy/__manifest__.py:15. Direct dependents (manifest scan): hr_org_chart only (auto_install on that side).

## B. Objects and relationships
- B1. No business object or table of its own. Extends: every model (base abstract), the view definition model (ir.ui.view), and the action-view mapping (ir.actions.act_window.view). web_hierarchy/models/models.py:6-7; web_hierarchy/models/ir_ui_view.py:23-26; web_hierarchy/models/ir_actions.py:6-9
- B2. The parent field must be a many-to-one to the same model; the child field a one-to-many to the same model (client-side checks; error otherwise). web_hierarchy/static/src/hierarchy_arch_parser.js:28-48
- B3. Lifecycle: none.

## C. Validations, security, automation
- C1. Definition-time validation: only field entries and one templates block are allowed inside a hierarchy view; only whitelisted attributes are accepted; otherwise the view definition is rejected with an error. web_hierarchy/models/ir_ui_view.py:31-54
- C2. The view is treated as template-based (qweb) for validation purposes. web_hierarchy/models/ir_ui_view.py:28-29
- C3. Missing card template raises a client error. web_hierarchy/static/src/hierarchy_arch_parser.js:68-70
- C4. Security: no groups, rules, or access rows; read goes through the normal search and record-read path, so the caller's access rights and record rules apply to displayed records (the module calls search and web_read as the current user, not elevated). web_hierarchy/models/models.py:13,36; skeleton: groups, rules, access none.
- C5. No company scoping of its own; the domain in the action and standard rules decide what appears. UNKNOWN — EVIDENCE INSUFFICIENT for any company filter default (none in module).
- C6. No audit: re-parenting is a normal write, so only whatever tracking the target model has records it (e.g., chatter on the model) — not verified for hr models.

## D. Handoffs
- D1. Owner of the concrete org-chart views (department, employee, public employee): hr_org_chart. hr_org_chart/views/hr_department_views.xml:8 (draggable on); hr_org_chart/views/hr_views.xml:73 (draggable on); hr_org_chart/views/hr_employee_public_views.xml:24 (draggable off); hr_org_chart/__manifest__.py:16
- D2. Client view framework (registry, controllers, ORM service): web. web_hierarchy/static/src/hierarchy_view.js:1-29
- D3. Data ownership of the hierarchy (department/employee parent fields): hr. UNKNOWN — EVIDENCE INSUFFICIENT for field names (not read; defined in hr).

## E. Configuration/defaults that change outcomes
- E1. Per-view attributes: parent_field, child_field, draggable (default false), icon, default_order, create/edit/delete. web_hierarchy/models/ir_ui_view.py:7-20; web_hierarchy/static/src/hierarchy_arch_parser.js:12,50-55
- E2. No system parameters or settings.

## F. Effective extension path (module names only)
- Uses of the hierarchy view type in Community: hr_org_chart (grep of view definitions). The base abstract model is extended by many modules (base_import, base_sparse_field, hr, html_editor, mail, phone_validation, sms, transifex, web, website); this module's read method is available to all models but only hr_org_chart calls it through views.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: pagination/limits of the hierarchy read for large trees (not analysed).
- UNKNOWN — EVIDENCE INSUFFICIENT: drag-and-drop cycle protection (parent loops) — handled by hr models if at all.
- UNKNOWN — EVIDENCE INSUFFICIENT: tests: JS unit tests exist (web_hierarchy/static/tests/hierarchy_view.test.js) but were not read; no Python tests.

