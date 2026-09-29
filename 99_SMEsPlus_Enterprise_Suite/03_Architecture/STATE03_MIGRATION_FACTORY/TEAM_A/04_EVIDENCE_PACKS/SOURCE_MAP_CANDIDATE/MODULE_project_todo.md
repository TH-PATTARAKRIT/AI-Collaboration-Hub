# Source Map (candidate) — `project_todo`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project_todo` |
| Display name | To-Do |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `185fb7af8b87a2ef` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project_todo/` |
| auto_install / application | True / True |

## 2. Dependencies
- Direct dependencies (manifest): `project`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Productivity/To-Do / Organize your work with memos and to-do lists
- Inventory of user-facing artifacts (counts): menu items 1, views 9, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `mail.activity.todo.create` (Create activity and todo at the same time)
- Objects extended from other modules (2): `res.users`, `project.task`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `res.users`, `project.task`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 1 (of which company-scoped by text 0); access rows 4

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 44 of 45 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project_todo (To-Do)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/project_todo.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Personal to-do / memo application for every internal user, built on the project task record without a project ("private task"). Depends on project only (project_todo/__manifest__.py:10-12).
- Conditional + application: flagged as an application (project_todo/__manifest__.py:23) with its own top-level menu "To-do" (project_todo/views/project_todo_menus.xml:3-8) and auto_install true (project_todo/__manifest__.py:13), so it is installed automatically whenever project is present. Not configurable through settings.
- To-do screen (kanban default, plus form, list, calendar, activity) showing only tasks assigned to the current user that have no project and no parent task; defaults to "Open" filter, grouped by the user's personal stage (project_todo/views/project_task_views.xml:277-290, 11, 61; help text stating to-dos are private by default and can be shared by adding assignees: :293-296).
- Quick-create form with keyword shorthand in the title: `#` for tags, `@` for assignees, `!` `!!` `!!!` for priority (project_todo/views/project_task_views.xml:136-158). (TEST) valid/invalid expressions produce expected name/tag/assignee/priority; an unmatched user handle stays in the title; empty title is refused; keywords only recognised in the documented format (project_todo/tests/test_todo_quick_create.py:9-45).
- Auto-naming: a task created with no name, no project and no parent takes its name from the first line of its description (cut to 100 characters with ellipsis), or "Untitled to-do" when empty (project_todo/models/project_task.py:11-22).
- Convert to task: from a to-do the user picks a project (required), assignees and tags; conversion sets the task company from the chosen project (project_todo/models/project_task.py:24-32; view project_todo/views/project_task_views.xml:162-195).
- Wizard to create a to-do and a linked activity in one step (title, due date, assignee defaulting to current user, note) (project_todo/wizard/mail_activity_todo_create.py:6-38). (TEST) creates one to-do and one activity with matching title, user and deadline (project_todo/tests/test_mail_activity_todo_create.py:16-29).
- Systray activity counter separates "To-Do" activities from "Task" (project) activities, counting at most one per task, with today/overdue/planned buckets (project_todo/models/res_users.py:12-89). (TEST file exists for counters: project_todo/tests/test_mail_activity_systray_counter.py; contents not read: UNKNOWN — EVIDENCE INSUFFICIENT.)
- Welcome/onboarding to-do created for each new internal user, and for existing internal users at install (project_todo/models/res_users.py:91-115; project_todo/__init__.py:5-6; template project_todo/data/todo_template.xml:4). (TEST) exactly one onboarding to-do for a new internal user, none for portal/public, and it stays project-less even if a default project is in context (project_todo/tests/test_todo_onboarding_for_users.py:10-45).
- Helper to return the ids of the module's five main views for the client (project_todo/models/project_task.py:34-48).

## B. Business objects, relationships, lifecycle
- Object: task (owned by project) in its "private" form: no project, no parent, assigned to one or more users (domain project_todo/views/project_task_views.xml:281; rule project_todo/security/project_todo_security.xml:9).
- Personal stages (per-user): Inbox, Today, This Week, This Month, Later, Done (folded), Cancelled (folded), created for each new internal user (project/models/project_task.py:467-475; created via project/models/res_users.py:16-27; extended here to add the onboarding to-do: project_todo/models/res_users.py:91-94).
- Task state values owned by project: In Progress, Changes Requested, Approved, Done, Cancelled, Waiting (project/models/project_task.py:168-174); closed = done or cancelled (project/models/project_task.py:84-88, 402-404). To-do views use a check-mark widget to toggle done and fade closed cards (project_todo/views/project_task_views.xml:31, 46, 66).
- Lifecycle: create (private) -> optionally share by adding assignees -> optionally convert to a project task (project becomes set, so it leaves the To-do list) -> done/cancelled or archived. Conversion is one-way in this module; reverse move: UNKNOWN — EVIDENCE INSUFFICIENT.
- Activities on tasks are counted for the systray by whether the task has a project (task) or not (to-do) (project_todo/models/res_users.py:28, 54-61).

## C. Validations, automation, security, multi-company
- Convert form requires a project (project_todo/views/project_task_views.xml:181-183).
- Security ACL: every internal user gets full rights on task, task stages and tags at model level (project_todo/security/ir.model.access.csv:2-4) and create/read/write on the combined-creation wizard, no delete (project_todo/security/ir.model.access.csv:5). Effective narrowing comes from rules.
- Record rules: an internal user gets full access only to private tasks assigned to them and without parent (project_todo/security/project_todo_security.xml:6-11, installed as no-update data :4). Project's own rule hides private tasks from project users unless assigned (project/security/project_security.xml:166-176). (TEST) another internal user cannot read, write or delete someone else's private task (project_todo/tests/test_access_rights.py:8-20).
- Onboarding creation is done with superuser rights and without notification to followers (project_todo/models/res_users.py:115); skipped if the welcome template is missing (project_todo/models/res_users.py:106-107).
- Multi-company: no company field added by this module; conversion sets the task company from the project (project_todo/models/project_task.py:26). Company of a project-less private task: UNKNOWN — EVIDENCE INSUFFICIENT.
- Systray computation runs a direct data query scoped to the current user's own activities only (project_todo/models/res_users.py:26-42).

## D. Accounting / payroll / analytic handoffs
- None directly. Once converted into a project task, downstream timesheet/analytic behaviour belongs to project and hr_timesheet; the conversion form deliberately carries the company field so timesheet's project filter works without a bridge module (project_todo/views/project_task_views.xml:171-173).

## E. Configuration / defaults that change outcomes
- Action context forces new to-dos to have no project and hides task options (project_todo/views/project_task_views.xml:284-289).
- Default assignment: the wizard assigns to the acting user (project_todo/wizard/mail_activity_todo_create.py:12); due date defaults to today (line 11).
- Default kanban ordering by state, priority, deadline (project_todo/views/project_task_views.xml:17).
- Language of the onboarding text follows the user's language (project_todo/models/res_users.py:99).

## F. Effective extension path (module names only)
- Extends: project (task, user onboarding, activity groups), mail (activity), base users. The conversion form is aimed at hr_timesheet (comment in project_todo/views/project_task_views.xml:171-173). Manifest dependents of project_todo: none found in this tree.

## G. Not verified
- Front-end widgets (check-mark, editor, mail helper) and tours: UNKNOWN — EVIDENCE INSUFFICIENT.
- Systray counter test content: UNKNOWN — EVIDENCE INSUFFICIENT.
- Company assignment for private tasks; reverse conversion: UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; not asserted as universal.

