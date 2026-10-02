# U142 Project Management — Neutral Knowledge (clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Baseline: Odoo 19 Community (named once, here only)
> Scope: project and task lifecycle, stage management, privacy visibility, task state machine, recurring tasks, analytic account linking, timesheets cross-module, and built-in reporting
> Each statement is tagged with an id that links to technical claims held in the restricted layer.
> Statements describe what the system must do and why; no implementation names appear here.

## CAP-U142-01 Project Container and Visibility

### WHAT
- [N-U142-001] The project module depends on eight other modules: the analytics foundation, the base setup module, the messaging and activity framework, the portal access layer, the customer rating framework, the resource scheduling foundation, the web client framework, the guided tour framework, and the digest notification framework.
- [N-U142-002] A project has a visibility setting that controls who may see the project and its tasks; there are four options forming a spectrum from narrowest to broadest.
- [N-U142-003] When a new project is created its visibility defaults to the broadest option, which grants access to all internal staff and to any portal users who are explicitly added as followers.
- [N-U142-004] Projects have their own pipeline of stages that are separate from the per-task stages; project-level stages are only visible and usable when the corresponding feature group is activated.

### WHY
- [N-U142-005] Visibility controls protect commercially sensitive work from being seen by staff or customers who have no involvement in it, while the broad default ensures that newly created projects are not accidentally hidden.

### BUSINESS RULE
- [N-U142-006] A project stage displayed in the folded position in the board view is considered closed by the interface; there is no separate closed field on the stage record itself.
- [N-U142-007] A project may be linked to one analytic account; the link is optional in the base configuration but becomes mandatory when timesheet recording is enabled.
- [N-U142-008] The company assigned to a project is derived automatically from the analytic account or the customer record linked to the project; changing the company is refused if it would conflict with the linked analytic account that is already shared with other projects or has posted entries.

### DEPENDENCY
- [N-U142-009] Portal access to project records uses the standard portal URL path; the portal mixin provides the URL computation.
- [N-U142-010] Timesheet recording on a project is a feature added by a separate timesheet module; the base project module only stores the reference to the analytic account without enforcing its presence.

## CAP-U142-02 Task Model and Fields

### WHAT
- [N-U142-011] A task belongs to a project; tasks without a project are private tasks visible only to their assignees.
- [N-U142-012] Task assignees are stored as a list of internal active users; portal users may not be assignees.
- [N-U142-013] A task has a deadline expressed as a date and time, not just a date; the deadline carries over to successor tasks when the task recurs.
- [N-U142-014] A task has multi-value tags drawn from a shared catalogue; the same tag may be used on tasks belonging to different projects.
- [N-U142-015] The task description is a rich-text field with version history tracking; the history allows recovery of earlier descriptions.
- [N-U142-016] A task has a numeric priority with four levels: low, medium, high, and urgent.

### STATE
- [N-U142-017] A task has six possible workflow states: in progress, changes requested, approved, done, cancelled, and waiting; the done and cancelled states are the two closing states.
- [N-U142-018] The waiting state is set automatically when the task has one or more open blocking tasks; it clears automatically when all blocking tasks reach a closing state.
- [N-U142-019] The stage of a task is the kanban column it sits in; the stage is separate from the workflow state and either one may change independently.
- [N-U142-020] A task stage with its fold flag set is displayed as a collapsed column in the board view; a task may be in such a stage while still being in an open workflow state.

## CAP-U142-03 Task Dependencies and Blocking

### WHAT
- [N-U142-021] Task dependencies allow one task to block another; a blocked task is held in the waiting state until all its blocking tasks reach a closing state.

### BUSINESS RULE
- [N-U142-022] Task dependency tracking is an opt-in feature that must be enabled individually on each project; tasks in projects without this feature cannot be linked as dependencies.

### OPTIONALITY
- [N-U142-023] When dependency tracking is not enabled, the waiting state is never automatically set; the task state machine simplifies to the remaining five states.

## CAP-U142-04 Task Stages

### WHAT
- [N-U142-024] Task stages are shared records that may be assigned to multiple projects simultaneously; creating a stage in one project makes it available to any other project that chooses to use it.
- [N-U142-025] Stages have a sequence that determines their left-to-right order in the board view.
- [N-U142-026] Each stage may carry an optional staleness threshold expressed in days; tasks that remain in the stage without activity for longer than this threshold are marked as stale.
- [N-U142-027] Each stage may be configured to automatically adjust the task workflow state when a customer rating response is received; a favourable rating advances the state, an unfavourable one requests changes.

### STATE
- [N-U142-028] A stage has a personal variant that belongs to a single user; a personal stage is never linked to any project and is not visible to other users; every active internal user must have at least one personal stage at all times.

## CAP-U142-05 Recurring Tasks

### WHAT
- [N-U142-029] Recurring tasks are an opt-in feature that must be enabled on the project; a task may be made recurrent with a configurable interval expressed in days, weeks, months, or years.
- [N-U142-030] A recurrence record stores the interval, the unit, whether the recurrence runs forever or until a given end date, and the end date itself; a positive interval is required.
- [N-U142-031] When a recurring task is closed the system creates a successor task as the next occurrence; the deadline of the successor is the original deadline offset by one recurrence interval.

### CONSTRAINT
- [N-U142-032] A recurrent task cannot be converted into a sub-task; a private task (one without a project) cannot be made recurrent.
- [N-U142-033] The recurrence end date must be in the future when the recurrence is set to end on a specific date.

## CAP-U142-06 Milestones

### WHAT
- [N-U142-034] Milestones are an opt-in feature that must be enabled on the project; a milestone has a name, an optional deadline date, and a reached flag.
- [N-U142-035] When a milestone is marked as reached the system records the date it was reached.
- [N-U142-036] Tasks may be linked to a milestone; a milestone is considered overdue when its deadline has passed and it has not yet been reached.

## CAP-U142-07 Analytic Account and Timesheets (cross-module)

### WHAT
- [N-U142-037] When the timesheet module is installed, each project gains a timesheets-enabled toggle; enabling timesheets on a project that has no analytic account causes the system to create an analytic account automatically using the project name and company.
- [N-U142-038] When the timesheet module is installed, each task gains a list of timesheet entries; spent time, total spent time including sub-task time, progress percentage, and overtime are computed from these entries.
- [N-U142-039] A project with timesheets enabled must have an analytic account; the constraint is enforced on save and on enabling timesheets.

### DEPENDENCY
- [N-U142-040] The analytic account creation uses the project name, company, and customer as the account values; the base project module provides the creation method, and the timesheet module triggers it.

## CAP-U142-08 Scheduled Activity and Rating

### WHAT
- [N-U142-041] A scheduled job runs daily to dispatch periodic customer rating requests; it looks for task stages that have periodic rating active and whose next rating deadline has passed, sends the rating emails, and advances the deadline to the next period.

## CAP-U142-09 Built-in Reports

### WHAT
- [N-U142-042] The task analysis report is a database view that aggregates task records with rating data and milestone data; it exposes metrics including working days and hours to first assignment, working days and hours to closure, days remaining to deadline, and average customer rating.
- [N-U142-043] The burndown and burnup chart report reconstructs the history of task movements between stages by reading the audit trail of stage-field changes; it generates a time series showing how many tasks (and their total allocated time) were in each stage at each point in time.
- [N-U142-044] The burndown chart requires the query to be grouped by both a date interval and either the stage or the closed indicator; grouping by date alone is refused with an explanatory message.
