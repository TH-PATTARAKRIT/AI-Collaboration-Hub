# U174 — project: Milestone, Stage, Rating, Personal Stages
**Unit**: U174 | **Module**: project | **G-Group**: G10 | **Priority**: P2
**Date**: 2026-10-02 | **Status**: GATE-PASS

## Module Overview

The base `project` add-on defines four core models relevant to this unit: `project.project`, `project.milestone`, `project.task.type` (stages), and `project.task.recurrence`. A separate bridge model `project.task.stage.personal` manages each user's personal stage assignment per task.

## Project Fields

`project.project` inherits `analytic.plan.fields.mixin` (providing `analytic_distribution`), `portal.mixin`, `rating.parent.mixin`, and four other mixins. Key fields covered by this unit:

- **`milestone_ids`**: One2many to `project.milestone`; `copy=True` so milestones duplicate with the project.
- **`partner_id`**: Customer, Many2one to `res.partner`; `bypass_search_access=True` for portal resolution; tracked in chatter.
- **`privacy_visibility`**: Four choices — `followers` (invited internal users only), `invited_users` (invited internal and portal users), `employees` (all internal users), `portal` (all internal users and invited portal users). Default is `portal`.
- **`last_update_status`**: Mirrors `project.update.status` and adds `to_define` (default); becomes the project's displayed health indicator.
- **`allow_milestones`**: Boolean feature flag; inverse triggers `_inverse_allow_milestones`.
- **`allow_recurring_tasks`**: Boolean feature flag for recurring task support.

## Milestone Model

`project.milestone` inherits `mail.thread`. Default ordering: `sequence, deadline, is_reached desc, name` (unreached milestones surface first within each date bucket).

| Field | Type | Notes |
|---|---|---|
| `deadline` | Date | Tracked, not copied on duplication |
| `is_reached` | Boolean | Default False; manually toggled; not copied |
| `reached_date` | Date (computed) | Set to today when `is_reached` becomes True |
| `task_ids` | One2many → project.task | Inverse of `task.milestone_id` |
| `can_be_marked_as_done` | Boolean (computed) | True when all tasks are closed and at least one exists |
| `is_deadline_exceeded` | Boolean (computed) | True when deadline is past and milestone not reached |

## Stage Model (project.task.type)

`project.task.type` serves double duty as both project stages and personal stages within the same model:

- **`sequence`**: Integer, default `1` (unusually low; most Odoo sequences default to 10); ordering is `sequence, id`.
- **`project_ids`**: Many2many to `project.project`; a stage can be shared across multiple projects.
- **`mail_template_id`**: Sends an automatic customer email when a task reaches the stage (domain: `project.task` model).
- **`rating_template_id`**: Sends a rating request email; used by `_send_task_rating_mail`.
- **`rating_status`**: `stage` (send on stage entry) or `periodic` (send on schedule via `rating_status_period`).
- **`auto_validation_state`**: When True, customer rating response automatically sets task state to Approved or Changes Requested.

### Personal vs Project Stages

A stage is personal when `user_id` is set and `project_ids` is empty. An ORM constraint (`_check_personal_stage_not_linked_to_projects`) prevents any stage from having both `user_id` and `project_ids`. The `_compute_user_id` method automatically clears `user_id` when `project_ids` is set.

The `project.task.stage.personal` model (backed by `project_task_user_rel` table) is a junction storing `(task_id, user_id, stage_id)` with a unique constraint per (task, user) pair.

## Task Stage Assignment

`_compute_stage_id` (depends on `project_id`) reassigns the task's stage when its project changes: if the current stage is not in the new project's stages, it finds the first non-folded stage via `stage_find`; if there is no project, stage is set to False.

## Rating

`project.task` directly inherits `rating.mixin`. `_send_task_rating_mail` sends a rating request using the stage's `rating_template_id` when a `partner_id` is present, the partner is not the current user, and the task is not a template. A daily scheduler (`_send_rating_all`) handles periodic rating delivery.

## Closed States and Date Tracking

Two states are considered closed at module level: `1_done` (Done) and `1_canceled` (Cancelled). There is no `closed_date` field in the base project module. `date_last_stage_update` (Datetime, readonly, not copied) records when the state or stage last changed.

## Project Status Updates

`project.update` records status snapshots with five possible values: `on_track`, `at_risk`, `off_track`, `on_hold`, `done`. The `to_define` sentinel appears only on `project.project.last_update_status` as its default before any update is posted.

## Analytic Distribution

`analytic_distribution` is provided to `project.project` via `analytic.plan.fields.mixin`. The base `project.task` model contains no analytic field definitions; analytic distribution on tasks is provided by optional modules (e.g. `project_timesheet_holidays` or `analytic`-aware extensions).

## Recurring Tasks

`project.task.recurrence` stores the recurrence schedule: `repeat_interval` (default 1), `repeat_unit` (day/week/month/year, default week), `repeat_type` (forever/until, default forever), `repeat_until` (Date end). Tasks link to this model via `recurrence_id` and proxy the fields as computed read-write fields. The `allow_recurring_tasks` flag on `project.project` gates this feature.
