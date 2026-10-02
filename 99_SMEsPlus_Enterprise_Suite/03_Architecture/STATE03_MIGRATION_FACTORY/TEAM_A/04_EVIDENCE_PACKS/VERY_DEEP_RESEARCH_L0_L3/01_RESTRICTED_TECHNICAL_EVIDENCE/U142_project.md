# U142 project — Restricted Technical Evidence (L3)

**RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION**

- Status: `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION`
- Unit: U142 `project — project/task/stage management deep L3`
- G Group: G10 | Priority: P2
- Modules owned: `project` (primary), cross-module evidence from `hr_timesheet`
- Source revision: `19.0.post20260921` (Odoo Community only; `odoo-19.0.post20260921/odoo/addons`)
- Date: 2026-10-02
- Claim ids `VDR-U142-C###`; neutral ids `N-U142-###` (see `02_NEUTRAL_KNOWLEDGE/U142_project_NEUTRAL.md`).

## 0. Method, scope and honesty notes

**Files read in full:**
- `project/__manifest__.py` (lines 1–251)
- `project/models/project_project.py` (lines 1–310, 860–900, 1188–1220)
- `project/models/project_task.py` (lines 1–450)
- `project/models/project_task_type.py` (lines 1–239)
- `project/models/project_task_recurrence.py` (lines 1–105)
- `project/models/project_project_stage.py` (lines 1–84)
- `project/models/project_milestone.py` (lines 1–84)
- `project/models/account_analytic_account.py` (lines 1–44)
- `project/data/ir_cron_data.xml` (lines 1–10)
- `project/report/project_report.py` (lines 1–161)
- `project/report/project_task_burndown_chart_report.py` (lines 1–253)
- `hr_timesheet/models/project_task.py` (lines 1–60)
- `hr_timesheet/models/project_project.py` (lines 13–296)

**Not read:** `project/views/`, `project/security/`, `project/wizard/`, `project/controllers/`, `project/models/project_collaborator.py`, `project/models/project_role.py`, `project/models/project_tags.py`, `project/models/project_update.py`, `project/models/res_config_settings.py`, `project/models/project_task_stage_personal.py`, `project/models/res_partner.py`, `project/models/res_users.py`, `project/models/digest_digest.py`, all view XML, security XML, and JS assets.

**No execution.** All claims are source-static. Runtime-required items tagged AWT.

## VDR Claims Table

| Claim-ID | Function-ID | Pointer | Anchor | Class | Condition | Flags | Technical statement | Neutral-ref |
|---|---|---|---|---|---|---|---|---|
| VDR-U142-C001 | FUNCTION MAPPING REQUIRED | project/__manifest__.py:11-20 | `depends` | C1 | Always | C1 | The project module declares 8 direct dependencies: analytic, base_setup, mail, portal, rating, resource, web, web_tour, and digest; it does NOT depend on account, stock, or hr | N-U142-001 |
| VDR-U142-C002 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:119-126 | `privacy_visibility` | C1 | Always | C1 | The privacy_visibility field on project.project is a required Selection with four values: followers (invited internal users only), invited_users (invited internal and portal users), employees (all internal users), and portal (all internal plus invited portal users); default is 'portal' | N-U142-002 |
| VDR-U142-C003 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:126 | `default='portal'` | C1 | On project creation | C1 | New projects default to the broadest portal visibility, meaning all internal users and any portal users who are added as followers can see the project | N-U142-003 |
| VDR-U142-C004 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:158-159 | `stage_id` | C1 | When group_project_stages enabled | C1 | The project itself has a stage_id field pointing to project.project.stage (not project.task.type), gated by the group_project_stages security group; this is a separate pipeline from task stages | N-U142-004 |
| VDR-U142-C005 | FUNCTION MAPPING REQUIRED | project/models/project_project_stage.py:18-19 | `fold` | C1 | Always | C1 | The project.project.stage model has a fold boolean field; stages with fold=True are displayed as collapsed in kanban and list views and are treated as closed by the UI; there is no is_closed field on this model | N-U142-005 |
| VDR-U142-C006 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:98 | `account_id` | C1 | Always | C1 | The project.project model has an account_id Many2one to account.analytic.account (not required, ondelete set null); the base project module stores the reference but does not auto-create the analytic account — that logic is added by hr_timesheet | N-U142-006 |
| VDR-U142-C007 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:84-87 | `CLOSED_STATES` | C1 | Always | C1 | CLOSED_STATES is a module-level dict constant with exactly two keys: '1_done' (Done) and '1_canceled' (Cancelled); this constant is imported by other models including project_project and project_milestone to determine task completion | N-U142-007 |
| VDR-U142-C008 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:168-175 | `state` | C1 | Always | C1 | The task state field is a computed stored Selection with 6 values: 01_in_progress, 02_changes_requested, 03_approved, 1_done, 1_canceled, and 04_waiting_normal; it has a custom inverse and is tracked for chatter history | N-U142-008 |
| VDR-U142-C009 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:386-399 | `_compute_state` | C1 | When allow_task_dependencies is True | C1 | The state compute method sets the task to 04_waiting_normal when any blocking task (depend_on_ids) is not in CLOSED_STATES; once all blockers close the task reverts to 01_in_progress; tasks already in a closed state are not re-opened by blocking changes | N-U142-009 |
| VDR-U142-C010 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:161-164 | `stage_id` | C1 | Always | C1 | The task stage_id is a Many2one to project.task.type; it is computed+stored (compute='_compute_stage_id'), readonly=False, with domain restricting to stages assigned to the task's project; the task type model is shared across multiple projects | N-U142-010 |
| VDR-U142-C011 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:205-206 | `user_ids` | C1 | Always | C1 | Task assignees are stored in user_ids, a Many2many to res.users via project_task_user_rel; domain restricts to non-portal active users (share=False, active=True); falsy_value_label shows 'Unassigned' when empty | N-U142-011 |
| VDR-U142-C012 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:183 | `date_deadline` | C1 | Always | C1 | The task date_deadline is a Datetime field (not Date) with index and tracking; it is copied to successive recurring task instances by project.task.recurrence._get_recurring_fields_to_postpone | N-U142-012 |
| VDR-U142-C013 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:166 | `tag_ids` | C1 | Always | C1 | Task tags are stored in tag_ids, a Many2many to project.tags (no relation table named explicitly, uses default); tags are multi-project global, not per-project | N-U142-013 |
| VDR-U142-C014 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:153 | `description` | C1 | Always | C1 | The task description is stored as an Html field with sanitize_attributes=False; it is version-tracked via the html.field.history.mixin inherited at the model level and is included in PROJECT_TASK_WRITABLE_FIELDS for portal write access | N-U142-014 |
| VDR-U142-C015 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:281-288 | `depend_on_ids` | C1 | When allow_task_dependencies is True | C1 | Task blocking dependencies are stored in depend_on_ids (Many2many, relation task_dependencies_rel, column1 task_id, column2 depends_on_id); the inverse side dependent_ids uses the same relation with columns reversed; copy=False on both sides | N-U142-015 |
| VDR-U142-C016 | FUNCTION MAPPING REQUIRED | project/models/project_task.py:297-312 | `recurring_task` | C1 | When allow_recurring_tasks is True on the project | C1 | Recurring task configuration is stored on the task as a boolean recurring_task flag, a Many2one recurrence_id to project.task.recurrence, and four computed/relayed repeat_* fields (repeat_interval, repeat_unit, repeat_type, repeat_until) | N-U142-016 |
| VDR-U142-C017 | FUNCTION MAPPING REQUIRED | project/models/project_task_recurrence.py:10-27 | `ProjectTaskRecurrence` | C1 | Always | C1 | The project.task.recurrence model stores recurrence configuration: repeat_interval (integer, must be > 0), repeat_unit (selection: day/week/month/year, default week), repeat_type (forever or until), and repeat_until (date end); task_ids One2many back-references all tasks in the recurrence | N-U142-017 |
| VDR-U142-C018 | FUNCTION MAPPING REQUIRED | project/models/project_task_recurrence.py:67-88 | `_create_next_occurrences` | C1 | When a recurring task is closed | C1 | The method _create_next_occurrences creates the next task in a recurrence by copying the original task via copy_data, applying field-by-field overrides from _get_recurring_fields_to_copy and _get_recurring_fields_to_postpone (which returns date_deadline), and filtering out tasks beyond repeat_until | N-U142-018 |
| VDR-U142-C019 | FUNCTION MAPPING REQUIRED | project/models/project_task_type.py:36 | `fold` | C1 | Always | C1 | The project.task.type (task stage) model has a fold boolean field; task stages with fold=True appear as collapsed columns in the kanban view; there is NO is_closed field on the stage model — closure is determined by the state field on the task itself | N-U142-019 |
| VDR-U142-C020 | FUNCTION MAPPING REQUIRED | project/models/project_task_type.py:47-48 | `rotting_threshold_days` | C1 | Always | C1 | Task stages carry a rotting_threshold_days integer (default 0 = disabled); when positive, tasks in this stage that have not been updated within that many days are flagged as stale/rotting; changing this value does not retroactively update the rotting status of already-stale tasks | N-U142-020 |
| VDR-U142-C021 | FUNCTION MAPPING REQUIRED | project/models/project_task_type.py:43-46 | `auto_validation_state` | C1 | When customer rating is enabled on the stage | C1 | The auto_validation_state boolean on a task stage enables automatic state changes based on customer rating feedback: good feedback sets state to 03_approved, neutral or bad feedback sets it to 02_changes_requested | N-U142-021 |
| VDR-U142-C022 | FUNCTION MAPPING REQUIRED | project/data/ir_cron_data.xml:3-9 | `ir_cron_rating_project` | C1 | Always (daily schedule) | C1 | A single cron record named 'Project Stage: Send rating' is defined on model project.task.type with interval_type days; it calls _send_rating_all which queries all stages with periodic rating active and a past deadline, sends ratings, and recomputes the deadline | N-U142-022 |
| VDR-U142-C023 | FUNCTION MAPPING REQUIRED | project/report/project_report.py:9-161 | `ReportProjectTaskUser` | C1 | Always | C1 | The Tasks Analysis report is a non-stored SQL view model (report.project.task.user, _auto=False) ordered by name desc and project; it exposes task analytics including working_days_open/close, working_hours_open/close, delay_endings_days, rating_last_value, and rating_avg joined from rating.rating; records exclude tasks without a project_id | N-U142-023 |
| VDR-U142-C024 | FUNCTION MAPPING REQUIRED | project/report/project_task_burndown_chart_report.py:10-14 | `ProjectTaskBurndownChartReport` | C1 | Always | C1 | The Burndown Chart is an abstract SQL model (project.task.burndown.chart.report, _auto=False) that uses a CTE reading mail_message and mail_tracking_value to reconstruct stage history for each task; it generates a time-series of task counts per stage per date interval using generate_series; requires both date and stage_id (or is_closed) in the group-by or raises UserError | N-U142-024 |
| VDR-U142-C025 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/project_task.py:45 | `timesheet_ids` | C1 | When hr_timesheet is installed | C1 | The hr_timesheet module adds timesheet_ids as a One2many to account.analytic.line (keyed on task_id) to the task model; effective_hours, total_hours_spent, subtask_effective_hours, progress, overtime, and remaining_hours are computed from this relation | N-U142-025 |
| VDR-U142-C026 | FUNCTION MAPPING REQUIRED | hr_timesheet/models/project_project.py:13-14 | `allow_timesheets` | C1 | When hr_timesheet is installed | C1 | The hr_timesheet module adds allow_timesheets as a computed+stored Boolean to project.project; when allow_timesheets is toggled to True on a project that has no account_id and is not a template, the module automatically creates an analytic account named after the project via _create_analytic_account | N-U142-026 |
| VDR-U142-C027 | FUNCTION MAPPING REQUIRED | project/models/project_project.py:1188-1192 | `_create_analytic_account` | C1 | When called by hr_timesheet | C1 | The base _create_analytic_account method on project.project creates an account.analytic.account record using the project name and company, then assigns it to account_id; it reads name, company_id, and partner_id from the project for the account batch creation values | N-U142-027 |
| VDR-U142-C028 | FUNCTION MAPPING REQUIRED | project/models/project_milestone.py:12-35 | `ProjectMilestone` | C1 | When allow_milestones is True on the project | C1 | The project.milestone model (inheriting mail.thread) stores name, project_id (required, cascading), deadline (Date), is_reached (Boolean default False, copy=False), and reached_date (computed stored from is_reached); tasks link to a milestone via a Many2one milestone_id | N-U142-028 |

## CAP-U142-01 Project Model and Privacy

**D1.** Projects (`project.project`) provide the top-level container. Privacy is controlled by `privacy_visibility` selecting who sees the project and its tasks. The four levels escalate from individual followers only through all internal users.

**D2.** Key fields at `project/models/project_project.py:90-183`: `name`, `description` (Html), `active`, `partner_id` (customer), `company_id` (computed from analytic account company or partner company), `account_id` (analytic account), `privacy_visibility` (default portal), `stage_id` (project pipeline stage, gated by group), `type_ids` (task stages shared with this project), `task_count`, `open_task_count`, `closed_task_count`, `allow_task_dependencies`, `allow_milestones`, `allow_recurring_tasks`, `last_update_status` (on_track/at_risk/off_track/on_hold/to_define/done), `milestone_ids`.

**D3.** `_change_privacy_visibility` at line 1215 handles subscription side effects when visibility changes between portal-accessible and non-portal-accessible. Portal access URLs at `/my/projects/{id}`. Company is computed from account_id.company_id or partner_id.company_id; the inverse enforces that company must match partner and analytic account company.

## CAP-U142-02 Task State Machine

**D1.** Task state is a 6-value computed stored selection. Two of the six values are "closed" (1_done, 1_canceled); four are "open". The state is driven partly by external dependency blocking.

**D2.** The state computation at `project/models/project_task.py:386-399`: if allow_task_dependencies is True and any item in depend_on_ids is not in CLOSED_STATES, the task is forced to `04_waiting_normal`. When all blocking tasks close, it reverts to `01_in_progress`. The inverse `_inverse_state` at line 443 handles recurrence creation when a recurring task is marked done.

**D3.** Stage is separate from state. Stage (`stage_id`) is the kanban column; state (`state`) is a workflow attribute. A task can be in any stage at any state, except the logic at write-time updates `date_last_stage_update` on stage change.

## CAP-U142-03 Task Stages and Rotting

**D1.** Task stages (`project.task.type`) are shared across projects. A project lists its stages via `type_ids` (Many2many). Stages are not per-project; they can be reused across projects.

**D2.** Key stage fields: `name`, `sequence`, `project_ids` (which projects use this stage), `fold`, `rotting_threshold_days`, `auto_validation_state`, `rating_active`, `rating_status` (stage/periodic), `rating_status_period`, `mail_template_id`, `rating_template_id`, `user_id` (personal stage owner — personal stages have user_id set and project_ids empty; constraint enforced).

**D3.** No `is_closed` field on the stage model. Closure of a task is determined by the task's own `state` field being in CLOSED_STATES. Stage `fold` only affects kanban display.

## CAP-U142-04 Recurrence

**D1.** Recurring tasks are enabled per-project via `allow_recurring_tasks`. When a recurring task is closed (its state moves to a CLOSED_STATE), a new task occurrence is created via `_create_next_occurrences`.

**D2.** The recurrence configuration lives on `project.task.recurrence` (separate model). Tasks link via `recurrence_id`. The task carries computed fields relaying repeat_* from the recurrence.

**D3.** `_get_recurring_fields_to_postpone` returns `['date_deadline']` — the deadline of the new task is offset by the recurrence delta. The constraint at line 29-31 enforces repeat_interval > 0. The constraint at line 34-38 enforces repeat_until is in the future.

## CAP-U142-05 Cross-module: Timesheets and Analytic Accounts

**D1.** The base project module defines `account_id` but does not enforce analytic account creation or timesheet logic. The `hr_timesheet` module extends both `project.project` and `project.task` with timesheet-specific fields.

**D2.** When `hr_timesheet` is installed: `allow_timesheets` is added to `project.project`; creating a project with `allow_timesheets=True` auto-creates an `account.analytic.account`. Writing `allow_timesheets=True` on an existing project without an account also triggers `_create_analytic_account`. The constraint at `hr_timesheet/models/project_project.py:98-104` enforces `account_id` is required when `allow_timesheets=True`.

## CAP-U142-06 Reports

**D1.** Two report models are included: a task analysis SQL view and a burndown/burnup chart abstract model.

**D2.** `report.project.task.user` (Tasks Analysis) is a plain SQL view joining `project_task` with rating_rating and milestone. It exposes working-time metrics (days/hours to assign and close), delay to deadline, and rating averages.

**D3.** `project.task.burndown.chart.report` uses a complex CTE that reconstructs stage history from mail tracking values. It uses `generate_series` to produce a time-series row per date interval per stage. Querying it requires both a date group-by and a stage/is_closed group-by; otherwise a UserError is raised at line 222.
