# Source Map (candidate) — `project_hr_skills`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_hr_skills` |
| Display name | Project - Skills |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e47e5add8de742e5` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_hr_skills/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `project`, `hr_skills`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Project skills
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `res.users`, `project.task`, `report.project.task.user`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.users`, `project.task`, `report.project.task.user`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 14 of 14 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — project_hr_skills
Source revision: 19.0.post20260921 | Module: "Project - Skills" (project_hr_skills/__manifest__.py:4) | depends: project, hr_skills (:11) | License LGPL-3 (:17)
Basis: static reading of all 4 python files and 1 view; no tests exist in this module.

## A. Capabilities and optionality
- A1. Lets a user search project tasks by the skills of the people assigned to them (task search box gains a "Skills" term). project_hr_skills/views/project_task_views.xml:8-10; project_hr_skills/__manifest__.py:6-10
- A2. Conditional: bridge module, installed automatically when both project and hr_skills are present (auto_install true). project_hr_skills/__manifest__.py:12
- A3. Skill information is also exposed on the task analysis report (read-only related list of skills of the report's assignees). project_hr_skills/report/report_project_task_user.py:9
- A4. No settings, no menus, no new groups, no data files beyond the one search-view extension. project_hr_skills/__manifest__.py:13-15

## B. Business objects, relationships, lifecycle
- B1. A user (res.users, owner base) gets a read-only shortcut to the skills of its linked employee record (skills owned by hr_skills). project_hr_skills/models/res_users.py:7
- B2. A task (project.task, owner project) gets a read-only list of skills, collected across all its assigned users. project_hr_skills/models/project_task.py:9
- B3. No state or lifecycle of its own; skills are derived, not stored copies (related, no stored flag). project_hr_skills/models/project_task.py:9
- B4. Search rule: a task matches a skill text if it has no assignee at all, or if any assignee has a skill whose name matches (case-insensitive partial). project_hr_skills/views/project_task_views.xml:9

## C. Validations, security, multi-company
- C1. No constraints, no automation. (none found in module)
- C2. No access rules, groups or record rules added; visibility follows whatever project and hr_skills grant on tasks, users and employee skills. project_hr_skills/__manifest__.py:13-15 (no security file listed)
- C3. Multi-company: no explicit handling in this module. UNKNOWN — EVIDENCE INSUFFICIENT for whether a task reader can see skill rows of an assignee belonging to another company (depends on hr_skills rules, not read here).

## D. Handoffs
- D1. Skills master data, levels and employee-skill rows: hr_skills. Tasks, assignees, search view: project. This module only links them for display and search.
- D2. No accounting, inventory, sales or analytic handoff. (none found in module)

## E. Configuration/defaults that change outcomes
- E1. None. Behaviour is fixed once installed; the tasks with no assignee always show up in a skill search (B4), which is a default effect to be aware of in resource planning views.

## F. Effective extension path (grep of _inherit)
- F1. This module extends: res.users, project.task, report.project.task.user. project_hr_skills/models/res_users.py:5; project_hr_skills/models/project_task.py:7; project_hr_skills/report/report_project_task_user.py:7
- F2. No other module in the Community tree lists project_hr_skills as a dependency (reverse dependency index shows none).

## G. Not verified
- G1. UNKNOWN — EVIDENCE INSUFFICIENT: runtime behaviour of the search when an assignee has no employee record.
- G2. UNKNOWN — EVIDENCE INSUFFICIENT: multi-company skill visibility (see C3).
- G3. UNKNOWN — EVIDENCE INSUFFICIENT: any test-derived behaviour (module has no tests).

