# Source Map (candidate) — `project`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `project` |
| Display name | Project |
| Manifest version | 1.4 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G06 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `7d722c5109276ff8` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/project/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `analytic`, `base_setup`, `mail`, `portal`, `rating`, `resource`, `web`, `web_tour`, `digest`
- Direct dependents in 300-module list (9): `hr_timesheet`, `project_account`, `project_hr_skills`, `project_mail_plugin`, `project_mrp`, `project_sms`, `project_stock`, `project_todo`, `website_project`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (1): `purchase_request` — LGPL-3

## 3. Capabilities / functions
- Manifest category / summary: Services/Project / Organize and plan your projects
- Inventory of user-facing artifacts (counts): menu items 19, views 112, window actions 39, server actions 5, reports 0, mail templates 3, scheduled jobs 1, wizards 9, web routes 9
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (20): `project.template.create.wizard` (Project Template create Wizard); `project.template.role.to.users.map` (Project role to users mapping); `project.share.collaborator.wizard` (Project Sharing Collaborator Wizard); `project.project.stage.delete.wizard` (Project Stage Delete Wizard); `project.share.wizard` (Project Sharing); `task.share.wizard` (Task Sharing); `project.task.type.delete.wizard` (Project Task Stage Delete Wizard); `project.update` (Project Update); `project.collaborator` (Collaborators in project shared); `project.project.stage` (Project Stage); `project.task.recurrence` (Task Recurrence); `project.task.stage.personal` (Personal Task Stage); `project.task.type` (Task Stage); `project.tags` (Project Tags); `project.task` (Task); `project.project` (Project); `project.role` (Project Role); `project.milestone` (Project Milestone); `project.task.burndown.chart.report` (Burndown Chart); `report.project.task.user` (Tasks Analysis)
- Objects extended from other modules (19): `portal.share`, `digest.digest`, `mail.thread.cc`, `mail.activity.mixin`, `account.analytic.account`, `res.users.settings`, `ir.ui.menu`, `res.users`, `portal.mixin`, `rating.mixin`, `mail.tracking.duration.mixin`, `html.field.history.mixin`, `res.config.settings`, `mail.alias.mixin`, `rating.parent.mixin`, `analytic.plan.fields.mixin`, `mail.message`, `res.partner`, `mail.thread`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `project.template.create.wizard` ← Community: `sale_project`; open-license custom/third-party scanned: —
- `project.update` ← Community: `hr_timesheet`, `sale_project`; open-license custom/third-party scanned: —
- `project.collaborator` ← Community: `hr_timesheet`; open-license custom/third-party scanned: —
- `project.project.stage` ← Community: `project_sms`; open-license custom/third-party scanned: —
- `project.task.recurrence` ← Community: `sale_project`; open-license custom/third-party scanned: —
- `project.task.type` ← Community: `project_sms`, `sale_project`; open-license custom/third-party scanned: —
- `project.task` ← Community: `hr_timesheet`, `project_hr_skills`, `project_sms`, `project_timesheet_holidays`, `project_todo`, `sale_project`, `sale_timesheet`, `website_project`; open-license custom/third-party scanned: —
- `project.project` ← Community: `hr_timesheet`, `project_account`, `project_hr_expense`, `project_mrp`, `project_mrp_account`, `project_purchase`, `project_sale_expense`, `project_sms`, `project_stock`, `project_stock_account` … (+3); open-license custom/third-party scanned: —
- `project.milestone` ← Community: `sale_project`; open-license custom/third-party scanned: —
- `report.project.task.user` ← Community: `hr_timesheet`, `project_hr_skills`, `sale_project`, `sale_timesheet`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `portal.share`, `digest.digest`, `mail.thread.cc`, `mail.activity.mixin`, `account.analytic.account`, `res.users.settings`, `ir.ui.menu`, `res.users`, `portal.mixin`, `rating.mixin`, `mail.tracking.duration.mixin`, `html.field.history.mixin`, `res.config.settings`, `mail.alias.mixin`, `rating.parent.mixin`, `analytic.plan.fields.mixin`, `mail.message`, `res.partner`, `mail.thread`

## 6. Actions / states / validation / automation / security
- State fields found: `project.update` → ['on_track', 'at_risk', 'off_track', 'on_hold', 'done']; `project.task.burndown.chart.report` → ['01_in_progress', '1_done', '04_waiting_normal', '03_approved', '1_canceled', '02_changes_requested']; `report.project.task.user` → ['01_in_progress', '1_done', '04_waiting_normal', '03_approved', '1_canceled', '02_changes_requested']
- Validation: 11 declarative constraint method(s), 6 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Project Stage: Send rating every ? days
- Security: groups declared 9 (`group_project_user`, `group_project_manager`, `group_project_stages`, `group_project_recurring_tasks`, `group_project_task_dependencies`, `group_project_milestone` … (+3)); record rules 31 (of which company-scoped by text 6); access rows 55

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 118 of 119 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: project (Project, application)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/project.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.
Depends on analytic, base_setup, mail, portal, rating, resource, web, web_tour, digest (project/__manifest__.py:11-21). Standalone application; not auto-installed (project/__manifest__.py:67).

## A. Capabilities / functions
- Core: projects with tasks, kanban stages per project, assignees (many per task), tags, priority (4 levels), deadlines, allocated hours, chatter/activities, email-to-task, favorites, task analysis report, burndown chart (project/models/project_task.py:151-330; project/models/project_project.py:23-36; project/report/project_report.py:9-13).
- Core: private tasks (no project) as a personal to-do list with per-user personal stages (Inbox/Today/This Week/This Month/Later/Done/Cancelled), created for every new internal user (project/models/project_task.py:466-476; project/models/res_users.py:11-27). Personal stages cannot be attached to projects (project/models/project_task_type.py:218-221).
- Core: sub-tasks (hierarchy, cycle refused), project updates (status posts with progress and default write-up), customer ratings per stage, project sharing with portal collaborators, portal pages (/my/projects, /my/tasks) (project/models/project_task.py:248-249, 589-592; project/models/project_update.py:21-63; project/controllers/portal.py:69,110,507).
- Optional features, each a per-project switch that also toggles a global feature group: task dependencies, milestones, recurring tasks (project/models/project_project.py:145-147, 404-442, 785-818; project/security/project_security.xml:31-41). The global group is added to all internal users while at least one project uses the feature and removed when none does (project/models/project_project.py:798-810).
- Optional: project stages (project pipeline, groups projects by stage, default seed To Do/In Progress/Done/Cancelled) enabled in settings (project/models/res_config_settings.py:11; project/data/project_data.xml:4-24; project/models/project_project.py:158-159).
- Optional/conditional: templates for projects and tasks (convert, create from template, role-to-user dispatch) (project/models/project_project.py:1318-1460; project/models/project_task.py:2031-2115; project/wizard/project_template_create_wizard.py:4-47).
- Conditional: "Task Logs" setting installs hr_timesheet (project/models/res_config_settings.py:10; project/views/res_config_settings_views.xml:21-25).
- Daily job sends periodic rating requests for stages set to periodic (project/data/ir_cron_data.xml:3-9; project/models/project_task_type.py:227-238). Digest KPI "Open Tasks" for project users (project/models/digest_digest.py:11-22).

## B. Business objects, relationships, lifecycle
- Project -> tasks (one-to-many); task -> optional parent task; task -> assignees, tags, milestone, recurrence, dependencies (blocked-by/blocks) (project/models/project_task.py:161-300).
- Project <-> task stages are many-to-many: a stage can be shared across projects; a task's stage must be one of its project's stages (project/models/project_task.py:161-164; project/models/project_task_type.py:26-29). When a task lands in a stage not yet on its project, the stage is added to the project (project/models/project_task.py:1090-1097, 1208-1209).
- Project -> customer (contact), manager (default: creator), analytic account (optional), collaborators (portal), updates, milestones (project/models/project_project.py:94-116, 154, 163, 175).
- Task state values: In Progress, Changes Requested, Approved, Waiting, Done, Cancelled; Done and Cancelled are "closed" (project/models/project_task.py:84-87, 168-175). Default state In Progress.
- Waiting is system-driven: with dependencies enabled, a task with any non-closed blocker is forced to Waiting (unless already closed); when blockers close it returns to In Progress (project/models/project_task.py:385-399). A closed task may be forced Done despite open blockers, but reopening it falls back to Waiting (project/models/project_task.py:1366-1372). (TEST) (project/tests/test_task_state.py:24-65).
- Disabling dependencies on a project releases its Waiting tasks to In Progress; re-enabling re-blocks tasks with open blockers (project/models/project_project.py:404-431, 679-680). (TEST) (project/tests/test_task_dependencies.py:96; project/tests/test_task_state.py:205-215).
- Moving a task to another project resets open non-waiting tasks to In Progress; changing parent does not reset state (project/models/project_task.py:426-429, 1373-1378). (TEST) (project/tests/test_task_state.py:67,173).
- Closing a task: moving into a folded stage stamps an end date, leaving clears it; last stage-change date always stamped (project/models/project_task.py:1289-1294, 1412-1416).
- Assignment date is stamped on first assignee and cleared when all assignees removed (project/models/project_task.py:1355-1360).
- Recurrence: closing the latest task of a recurrence creates the next occurrence with deadline shifted by the interval; respects an end date; deleting the last occurrence dissolves the recurrence (project/models/project_task.py:443-446, 1401-1410; project/models/project_task_recurrence.py:62-88, 90-122). (TEST) (project/tests/test_project_recurrence.py:196-211).
- Project status (On Track/At Risk/Off Track/On Hold/Complete) comes only from the latest update; setting it on the project creates an update record with a default write-up and task counts snapshot (project/models/project_project.py:166-173, 650-658; project/models/project_update.py:87-97).
- Milestone: reached flag with reached date; "can mark done" only if all linked tasks closed and at least one exists; deadlines exceeded flagged; milestones copy with project only if the feature is on (project/models/project_milestone.py:37-40, 65-88; project/models/project_project.py:494-511).
- Archiving a project archives all its tasks and vice versa on restore; archiving a stage archives its tasks (or projects, for project stages) (project/models/project_project.py:685-687; project/models/project_task_type.py:112-114; project/models/project_project_stage.py:60-61).
- Deleting a project deletes its tasks and its analytic account if that account has no analytic lines (project/models/project_project.py:700-713).

## C. Validations, automation, security, multi-company
- Rules: project end date not before start date (project/models/project_project.py:186-189); dates cleared together (project/models/project_project.py:662-675); tag names unique (project/models/project_tags.py:25-28); one collaborator per partner per project (project/models/project_collaborator.py:15-18); one personal stage per task per user (project/models/project_task_stage_personal.py:17-20); recurring task cannot have parent; private task cannot have parent or sub-tasks (project/models/project_task.py:331-338, 349-354); recurrence interval > 0 and end date in the future (project/models/project_task_recurrence.py:29-38); "two tasks cannot depend on each other" (project/models/project_task.py:507-510).
- Access groups: Project User (implies internal user) and Project Administrator (implies User plus canned-response admin) (project/security/project_security.xml:10-25). Users may read projects and manage tasks; only Administrators create/edit/delete projects, project stages, tags, collaborators, task-stage config and see reports/ratings menu (project/security/ir.model.access.csv:2-3,10,22,31; project/models/ir_ui_menu.py:12-13).
- Visibility per project: four levels (invited internal; invited internal+portal; all internal; all internal+invited portal), default "all internal + invited portal" (project/models/project_project.py:119-139). Internal users see projects unless follower-only, in which case they must follow; Administrators see all (project/security/project_security.xml:57-72). Task rule mirrors this and also lets assignees/followers in; Administrators see all project tasks plus own private tasks (project/security/project_security.xml:80-109, 147-176). (TEST) private tasks readable/writable only by their assignee (project/tests/test_access_rights.py:347-413).
- Portal: portal users see projects only for the two portal-enabled visibility levels and where their company contact follows; task read requires follow or non-limited collaboration; edit rights via project-sharing rules that are switched on only while at least one collaborator exists (project/security/project_security.xml:179-241; project/models/project_collaborator.py:25-58; project/security/ir.model.access.xml:6-15). Changing visibility away from portal removes portal followers and voids access tokens (project/models/project_project.py:1215-1234). (TEST) (project/tests/test_portal.py:13-84).
- Portal write is limited to a whitelist of task fields (title, description, contact, deadline, tags, stage, state, parent...) (project/models/project_task.py:67-82, 1061-1071).
- Multi-company: projects, project stages, tasks, updates, milestones and task analysis are visible only for the user's allowed companies plus company-less records (project/security/project_security.xml:45-55, 74-78, 135-139, 243-247, 313-317). Company on project derives from analytic account, else customer; task company follows project (or parent) (project/models/project_project.py:245-252; project/models/project_task.py:680-685). Customer company must equal project company and task company (project/models/project_project.py:266-273; project/models/project_task.py:342-347); partner company cannot be changed away from its projects/tasks (project/models/res_partner.py:17-27). Project stage company must equal project company, and a stage cannot be moved to another company while it holds projects of a different one (project/models/project_project.py:763-776; project/models/project_project_stage.py:45-58). (TEST) (project/tests/test_project_stage_multicompany.py:39-80; project/tests/test_multicompany.py:196-217).
- Task stages (`project.task.type`) carry no company field; visibility is by owner (personal) or project link (project/models/project_task_type.py:23-79; project/security/project_security.xml:118-133).
- Mail gateway: each project owns an email alias creating tasks; sender becomes customer, recipients matching internal users become assignees, others go to cc; first email body fills description with signature stripped (project/models/project_project.py:755-761; project/models/project_task.py:1735-1769, 1787-1817).
- Notifications: assignees notified on assignment; stage email template; rating request on entering a stage or periodically; new-task notifications to followers when a task moves project (project/models/project_task.py:1365, 1617-1625, 1322-1398; project/models/project_task_type.py:30-46).

## D. Handoffs to other modules
- Analytic/accounting: project holds an optional link to an analytic account and a project-plan column per analytic plan; owner of accounts, lines, plans is analytic (project/models/project_project.py:32, 98, 1178-1192; project/__init__.py:36-37). Project itself never auto-creates the account: helper exists, callers live in hr_timesheet (hr_timesheet/models/project_project.py:142-147). Changing project company is refused if the account has analytic lines or serves more than one project (project/models/project_project.py:276-279); account deletion is refused while its projects have tasks (project/models/account_analytic_account.py:22-29); project rename renames a sole-project account (project/models/project_project.py:688-697). (TEST) (project/tests/test_multicompany.py:221-333).
- Profitability panel: project defines empty hooks (revenues/costs) and the analytic-line filter; content supplied by project_account, sale_project, sale_timesheet, project_purchase, project_hr_expense, project_stock_account and others (project/models/project_project.py:987, 1052-1059, 1128-1169; project_account/models/project_project.py:127; sale_project/models/project_project.py:768; sale_timesheet/models/project_project.py:501). (TEST) empty in base module (project/tests/test_project_profitability.py:55-63).
- Sale: hook selects projects that can be billed (customer set); sales-order link fields live in sale_project (project/models/project_project.py:1194-1195; sale_project/models/project_project.py:28,849).
- Timesheet: allow_timesheets, timesheet lines and account creation owned by hr_timesheet; project only exposes the install switch (hr_timesheet/models/project_project.py:13,25; project/models/res_config_settings.py:10).
- Rating and mail: rating and discuss/alias/portal infrastructure owned by rating, mail, portal (project/models/project_task.py:94-101). Resource calendar for working-hours stats owned by resource (project/models/project_task.py:604-631).

## E. Configuration / defaults that change outcomes
- Settings: Project Stages on/off (also shows/hides the "project stage changed" subtype and menus), Task Logs (project/models/res_config_settings.py:10-18; project/models/ir_ui_menu.py:14-20).
- Per-project: visibility (default portal), feature switches, label for "tasks", working time from company calendar (project/models/project_project.py:105-106, 126, 254-258).
- New project defaults: manager = creator, first project stage by sequence honouring company (when stages enabled), stage "New" auto-added on quick-create (project/models/project_project.py:116, 581-587, 598-616).
- New task defaults: customer from parent else project; company from project; first non-folded stage of project; creator subscribed; for a private task the creator is added to the assignees when assignees are supplied (form default also assigns the user) (project/models/project_task.py:112-118, 430-431, 1141-1146, 1162-1170, 1215-1216).
- Per-stage: email template, rating template and mode (on entering or periodic), auto-set task state from rating, fold, rotting threshold (project/models/project_task_type.py:30-48; project/models/project_task.py:2163-2166).
- Duplicating a project copies tasks, followers, milestones only if enabled; template creation drops the customer (project/models/project_project.py:454-519, 1425-1432).

## F. Effective extension path
- Modules that extend project models: hr_timesheet, sale_project, sale_timesheet, project_account, project_purchase, project_hr_expense, project_stock, project_stock_account, project_mrp, project_mrp_account, project_sms, project_sale_expense, sale_project_stock, project_todo, project_mail_plugin, website_project, project_hr_skills (grep of `_inherit = 'project.project'` and manifests across the addons root).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: exact effect of the "See private tasks" rule for tasks without a project beyond what tests show (project/security/project_security.xml:166-176).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether task-level analytic distribution exists in this module (no such field found in project/models/project_task.py; owned by extensions if any).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end (owl) behaviour under project/static, burndown-chart query correctness, demo data effects.
- UNKNOWN — EVIDENCE INSUFFICIENT: how portal token links behave for each visibility combination beyond controllers read (project/controllers/portal.py:110-124, 176-191).

