> **CUSTOM / THIRD-PARTY MODULE STUDY — separate from Odoo Community results.** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · sub-agent authored, license-gated (manifest opened first), read-only, static · workspace on-disk copy (not verified against upstream) · effective installed set unknown · not runtime proof.

# STATE03 Custom Module Study: scgl_timesheet_grid

## 0. Header
- Module: scgl_timesheet_grid
- License (confirmed in manifest): LGPL-3 (scgl_timesheet_grid/__manifest__.py:24)
- Author (manifest): SCG Legacy (Thailand) Co., Ltd. (scgl_timesheet_grid/__manifest__.py:25)
- Version (manifest): 19.0.1.2.0 (scgl_timesheet_grid/__manifest__.py:22)
- Path: Extra_Module_scgl/scgl_timesheet_grid
- Source revision studied: workspace on-disk copy (not verified against upstream)

## 1. Business capability
- Weekly/monthly grid view for timesheets with a START/STOP timer; a Community counterpart of an Enterprise grid (manifest:4-21).
- Approval-like behaviour (validation lock): timesheet approvers can "validate" timesheets, which locks them for everyone else, and a per-employee "validated until" date locks all earlier days. Reset to draft is available to approvers (models/account_analytic_line.py:23-55, :86-118; manifest:17-20).
- Who approves: users in the core group "User: all timesheets" (technical name timesheet approver group; core:hr_timesheet/security/hr_timesheet_security.xml:18-23), referenced at models/account_analytic_line.py:13, :27-29. This is a single level, no per-employee manager routing.
- What is blocked: for non-approvers, creating, editing or deleting a timesheet that is validated, or dated on/before the employee's last validated date, raises an error (models/account_analytic_line.py:42-51, :63-83). Setting the validated flag or resetting it by a non-approver is refused (:53-55, :65-66, :72-75).
- Bypass observations (code reading, not executed): (a) code running with elevated access (sudo) skips the lock and approver checks (`self.env.su`, lines 43, 54, 72), so automations or other modules using elevation can edit validated lines; (b) the lock applies only to timesheets that have a project (lines 35-36, 90); (c) approvers themselves are never locked (:43, :59, :72); (d) reset-to-draft moves each employee's locked date back to the latest remaining validated line (:114-117), so resets are not confined to the selected period.
- Timer: one running timer per user, stored server-side; stop creates a timesheet line with minimum duration and rounding from two system parameters (defaults 15 and 15) (models/account_analytic_line.py:316-411; data/config.xml:4-11; models/timesheet_timer.py:5-17). Timer records are visible only to their owner (security/security.xml:4-8).
- Grid API: read, update cell, validate period, all with a 62-day period cap and 500-row cap (models/account_analytic_line.py:15-16, :197-313).

## 2. Attachment to CORE
- Depends declared: hr_timesheet (manifest:27).
- Core objects extended: `account.analytic.line` (timesheet lines), `hr.employee`, `ir.ui.view` (new view type), `ir.actions.act_window.view` (new view mode); core timesheet actions, menus and views (references at views/grid_views.xml:26, :32; views/validation_views.xml:10, :22, :40; menu root `hr_timesheet.timesheet_menu_root`, core:hr_timesheet/views/hr_timesheet_menus.xml:3; actions core:hr_timesheet/views/hr_timesheet_views.xml:398, :484).
- Overrides by name:
  - `_is_readonly` on timesheet lines (models/account_analytic_line.py:57-61): ADDS to core hook (core:hr_timesheet/models/hr_timesheet.py:112-115, which is documented as an extension hook returning false) — validated lines show read-only to non-approvers. Extends a core extension point; no ALTERS CORE CONTROL, though it changes editability.
  - `create` (:63-69), `write` (:71-79), `unlink` (:81-83) on timesheet lines: BLOCKS-ALTERS core behaviour for non-approvers on validated periods. ALTERS CORE CONTROL (adds a new refusal condition on core timesheet create/edit/delete; core tables of rights otherwise unchanged).
  - `_get_view_info` (models/ir_ui_view.py:13-14): ADDS to the web view registry (core:web/models/ir_ui_view.py:22). Selection add of view type on views and act-window views (models/ir_ui_view.py:11; models/ir_actions.py:8). Custom validator `_validate_tag_scgl_grid` (models/ir_ui_view.py:16-32) relies on the core view-error helper (core:base/models/ir_ui_view.py:821).
- Menus: adds "To Validate" menu with Last Period / All Timesheets, restricted to the approver group (views/validation_views.xml:97-101); adds list-action entries "Validate" and "Reset to Draft" restricted to the approver group (:105-121). Existing menus are not hidden; the grid becomes the first (default) view of My Timesheets and All Timesheets (views/grid_views.xml:22-33).

## 3. New objects, security, automation, external calls
- New models: `scgl.timesheet.timer` (models/timesheet_timer.py:5-17; constraint one timer per user via the new 19 constraint style, :17). New fields: `validated` on timesheet lines (indexed, read-only, models/account_analytic_line.py:23-24); `last_validated_timesheet_date` on employee, readable only by the approver group (models/hr_employee.py:8-11).
- ACL: timer model — timesheet user group, full CRUD (security/ir.model.access.csv:2); record rule limits to the user's own timer (security/security.xml:4-8). No new groups.
- Elevated-access reads: working-hours calendar (models/account_analytic_line.py:171-173), employee last validated date (:235), lock evaluation (:34), employee date update (:103-105), system parameters (:383). These reads are needed because the validated-date field is group-restricted; they do not grant edit rights.
- Company scoping: inherits core timesheet rules; the module adds none. Grid domain neutralises date conditions from the search view and requires a project (:152-158).
- Automation: none (no cron). External calls: none.

## 4. Odoo 19 compatibility
- Confirmed in Community 19: `_is_readonly` (core:hr_timesheet/models/hr_timesheet.py:112), approver group (core:hr_timesheet/security/hr_timesheet_security.xml:18), `Domain.map_conditions` (core:odoo/orm/domains.py:400 and following), `models.Constraint` (core:odoo/orm/table_objects.py:79), `group_ids` on server actions (core:base/models/ir_actions.py:661), `binding_view_types` (:79), `allocated_hours` / `remaining_hours` on projects (core:hr_timesheet/models/project_project.py:32-35), `get_work_hours_count` (core:resource/models/resource_calendar.py:803), view-error helper (core:base/models/ir_ui_view.py:821).
- The grid view type is a custom view mode registered by this module's front end (static/src/grid/grid_view.js, 674 lines, not fully read); compatibility with the 19 web client is by design intent of the manifest, not verified here.
- Names not verified individually: the `project.task` fields used in the timer clean-up (models/account_analytic_line.py:344-349).

## 5. Custom-to-custom dependencies
- None declared.

## 6. UNKNOWN — EVIDENCE INSUFFICIENT
- UNKNOWN — EVIDENCE INSUFFICIENT: whether other installed modules create or edit timesheet lines under elevated access, and thereby bypass the validation lock.
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end behaviour of the grid and timer (JavaScript and templates were only sampled by their file list, not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the "User: all timesheets" group in the deployed system is granted more widely than the people intended to validate.
