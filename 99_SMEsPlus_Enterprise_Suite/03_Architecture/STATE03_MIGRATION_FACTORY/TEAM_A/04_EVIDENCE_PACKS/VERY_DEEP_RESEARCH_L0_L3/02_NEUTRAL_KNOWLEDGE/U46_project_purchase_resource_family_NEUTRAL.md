# U46 project / purchase / rating / resource / rpc family — Neutral Knowledge

> Source basis: Odoo 19 Community. Neutral layer: no technical identifiers.
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

## Capability 01: Project definition and lifecycle

### WHAT

- [N-U46-871] Purpose of the capability, inferred from the project manifest and the lifecycle, template, stage and role claims in this section (see claims for project model, stage and template behaviour): it lets a team define a body of work with an owner, a stage, a schedule and reusable templates.

### WHY

- [N-U46-872] Rationale inferred from the same manifest and the model claims: a defined project gives tasks, finances and reporting a common container and gives managers a place to control who participates.

### BUSINESS RULE

- [N-U46-002] post init hook is project post init; the uninstall hook is project uninstall hook.
- [N-U46-004] The customer link is tracked and its picker is limited to partners of the same company or without company.
- [N-U46-005] company id is a stored computed field with an inverse and stays writable.
- [N-U46-006] The analytic account link is not copied on duplication and is set to null if the account is deleted.
- [N-U46-007] The project manager defaults to the creating user and is tracked.
- [N-U46-008] Visibility is a required selection of four values (followers, invited users, employees, portal) tracked on change, with default portal.
- [N-U46-009] Start date and expiration date are not copied on duplication; expiration date is indexed and tracked.
- [N-U46-010] Three per-project feature toggles (task dependencies, milestones, recurring tasks) each have an inverse that maintains a matching global feature group.
- [N-U46-013] A project can be a template (is template boolean, never copied as such unless duplicating a template).
- [N-U46-015] Task counters count tasks of the project excluding template tasks, and ignore archived tasks unless any project in the set is itself active.
- [N-U46-016] Marking a project as favorite uses elevated rights so ordinary project users can do it; favorite is a per-user many2many link.
- [N-U46-017] The working-time calendar of a project is the project company calendar, or the current company calendar if none.
- [N-U46-018] Project currency is the company currency, with the current company as fallback.
- [N-U46-024] Archiving or unarchiving a project propagates the active flag to all its tasks, including already archived ones.
- [N-U46-026] Subscribing to a project propagates changed subtypes only to tasks and updates the partner already follows; it does not subscribe the partner to existing tasks.
- [N-U46-027] A project owns a mail alias whose target model is the task model and whose defaults carry the project id.
- [N-U46-028] The portal URL of a project is the "my projects" path with the project id.
- [N-U46-031] Notification emails of a project hide the access button for portal groups when visibility is not invited users or portal.
- [N-U46-033] Sharing a project opens the share wizard with the project-sharing mail template and light layout preselected.
- [N-U46-034] The task action for a project passes active, create-permission, milestone and dependency flags into the context; for a template project it hides pivot and graph views.
- [N-U46-035] The rating action for a project filters consumed ratings of that project from the last 30 days and opens the single rating directly when only one exists.
- [N-U46-036] Base profitability hooks are stubs: items, labels, sequences and already-included invoice lines return empty values; extension modules supply data.
- [N-U46-037] get panel data returns nothing to non-project-users; for users it returns buttons, currency, milestone data and, when profitability is shown, sorted revenue and cost items.
- [N-U46-038] The profitability report is only available to project administrators; margin equals revenues plus costs (costs are negative); margin percentage is margin over absolute costs, zero when costs are zero.
- [N-U46-039] Changing visibility to invited users or portal subscribes the project customer and task customers as followers; changing away from them unsubscribes portal-user followers from project and tasks and clears the access token of the project and its tasks.
- [N-U46-150] A project role is a named, colour-coded, archivable label used on template tasks; its colour defaults to a random value and copying appends a copy suffix.
- [N-U46-208] The create-from-template wizard pre-lists one mapping row per project role used by tasks of the template.
- [N-U46-209] Only name, start date, end date, alias name and alias domain from the wizard feed the new project's values.
- [N-U46-210] The wizard shows date inputs only if the template defines both start and end dates.
- [N-U46-211] Creation delegates to the template's create-from-template action with the whitelist values and the role-to-users mapping.
- [N-U46-228] The customer ratings menu is hidden from users who are not project managers.
- [N-U46-235] Four project stages are seeded: To Do (10), In Progress (15), Done (20, folded), Cancelled (25, folded).

### STATE

- [N-U46-003] project project inherits portal mixin, mail alias mixin, rating parent mixin, mail activity mixin, mail tracking duration mixin and analytic plan mixin; default order is sequence, name, id; the stage field is duration-tracked.
- [N-U46-011] The project stage field is restricted to the stages feature group, ondelete restrict, tracked, not copied, default is the first stage by sequence, with group expansion to all stages.
- [N-U46-012] The project status is one of on track, at risk, off track, on hold, to define, done; it is stored, computed from the latest update, writable, required, default to define.
- [N-U46-019] Enabling dependencies sets open tasks that depend on open tasks to the waiting state; disabling it sets waiting tasks back to in progress; the global group is synchronised and the two waiting message subtypes are shown or hidden.
- [N-U46-020] Duplicating a project copies top-level tasks including archived ones with in-progress state, the new project and company, then re-parents the copied subtasks to the new project.
- [N-U46-021] A project created by typing only its name gets a default stage named New.
- [N-U46-022] On create, a blank task-label is replaced with the word for tasks; when the stages feature is on the lowest-sequence stage that is company-free or matches the project company is assigned; a favorite flag in values becomes a favorite link.
- [N-U46-023] Project write: forces an access token to empty unless visibility is invited users or portal; re-selects a stage when the company changes under the stages feature; routes favorite writes through elevated rights; turns a status change into a status-update record; applies privacy changes; keeps start and end dates both set or both cleared.
- [N-U46-030] When the stage changes and the new stage has a mail template, the template is sent as a note message with a light layout, and the log is not kept after auto-delete.
- [N-U46-032] The burndown action is opened for the project and passes the project stage names and sequences into its context.
- [N-U46-173] Archiving a project stage archives all its projects.
- [N-U46-174] Deleting a project stage goes through a wizard.
- [N-U46-175] Unarchiving a project stage with archived projects opens a wizard.
- [N-U46-201] The project-stage deletion wizard counts projects (including archived) in the selected stages.

### OPTIONALITY

- [N-U46-025] Deleting a project removes its per-user embedded action settings and all its tasks (including archived), then deletes the analytic account if it has no analytic lines.
- [N-U46-171] Project stages are ordered by sequence (default 50), have an optional email template, a fold flag meaning closed, an optional company and a colour.
- [N-U46-202] Archive option archives all projects in the stages and the stages themselves instead of deleting.
- [N-U46-203] The delete option unlinks the stages directly after the user confirms.
- [N-U46-230] Settings offer timesheet installation (task logs) and a project-stages feature group.
- [N-U46-867] The restored database has 56 access rows and 31 record rules owned by the project module, of which 30 are active, plus the groups user, administrator, milestone, stages, recurring tasks and task dependencies.
- [N-U46-868] The restored database holds 21 subtypes and 2 mail templates owned by project, 19 menu entries, one project record and four task records in total; contents were not read.

### DEPENDENCY

- [N-U46-001] The project app depends on analytic, base setup, mail, portal, rating, resource, web, web tour and digest, and is flagged as an application with a post-install hook and an uninstall hook.

### CONSTRAINT

- [N-U46-014] A database constraint requires the end date to be on or after the start date.
- [N-U46-029] A constraint rejects a project whose stage has a company different from the project company (separate messages for project with and without company).
- [N-U46-040] Project sharing is refused unless visibility is invited users or portal; a portal user needs a collaborator row; an internal user always qualifies.
- [N-U46-172] Changing a project stage's company is refused if it contains projects of another company.

### RISK

None recorded.

### UNKNOWN

None recorded.

## Capability 02: Project access control and sharing

### WHAT

- [N-U46-873] Purpose inferred from the visibility, record rule, access list and collaborator claims in this section: it limits who may see and change projects and tasks, and lets outside parties take part through a restricted shared view.

### WHY

- [N-U46-874] Rationale inferred from the same claims: work often involves confidential items and external contacts, so visibility needs several levels and portal sharing needs a bounded set of actions.

### BUSINESS RULE

- [N-U46-041] Collaborators are added only for partners that are share-type partners and not already collaborators, with a limited-access flag.
- [N-U46-042] Project User group implies the base internal user group; Project Administrator implies Project User and the canned-response admin group, and is seeded with the root and admin users.
- [N-U46-043] Four feature groups with no implications of their own exist: Use Stages on Project, Use Recurring Tasks, Use Task Dependencies, Use Milestones.
- [N-U46-045] Project administrators see all projects (rule domain always true) — but the global multi-company rule still applies.
- [N-U46-046] Internal users see projects whose visibility is employees or portal, or projects where they are followers.
- [N-U46-047] Internal users read tasks of visible projects (employees or portal visibility, or followed project), or tasks they follow or are assigned to; this rule is read-only because write, create and unlink are switched off.
- [N-U46-049] Portal users see projects whose visibility is invited users or portal and where their commercial partner or a child is a follower.
- [N-U46-050] A portal write or create task rule exists for the project-sharing feature but is shipped inactive (active = 0).
- [N-U46-051] Project updates are company-scoped through the parent project; internal users see updates of visible projects or those they authored or manage; administrators see all.
- [N-U46-052] Milestone visibility mirrors project visibility with the project manager as an alternative; a separate portal rule gives collaborators read access.
- [N-U46-053] The task analysis report is visible to project users by project visibility or following; administrators see all; the burndown report follows the same pattern.
- [N-U46-054] Project administrators can manage activity plans and plan templates, but only those targeting projects or tasks.
- [N-U46-055] Project model access: project users read only; administrators full; all internal users read via a base-group row; portal read.
- [N-U46-151] A collaborator links a partner to a non-template project with invited-users or portal visibility; both links are read-only after creation.
- [N-U46-153] Creating the first collaborator switches on the portal write access row and record rule for tasks.
- [N-U46-193] The project sharing wizard extends the generic portal share wizard and is restricted to the project model.
- [N-U46-194] When opened from a collaborator record, the wizard resolves the project from a default project context value.
- [N-U46-195] The wizard exposes a public link that gives anyone read access in portal mode.
- [N-U46-196] Creating the wizard immediately applies the collaborator list to the project, without waiting for a confirm button: collaborators absent from the list are removed.
- [N-U46-197] Submitting with no collaborator rows does nothing.
- [N-U46-198] Sharing a task through the generic share wizard also subscribes the recipients as followers of that task.
- [N-U46-199] A collaborator row offers read, edit with limited access, or edit; read lets the partner view tasks only, limited edit lets them edit tasks they follow, and edit lets them edit all tasks and choose which to follow.
- [N-U46-200] The invitation flag turns on when the partner is not yet a project follower, or when edit access is picked for a non-collaborator; it is otherwise left at its previous value and can be overridden by the user.
- [N-U46-212] Portal home counters show project and task counts only if the user has read access to the model; task count counts tasks that have a project.
- [N-U46-213] The portal project list excludes template projects.
- [N-U46-214] A single project page is reachable by public authentication using an access token or by a logged-in user with access.
- [N-U46-215] The sharing interface uses the project's company, falling back to the user's company, and exposes only that company as allowed.
- [N-U46-216] A task page within a project is reachable by public authentication using the project token.
- [N-U46-217] A subtasks page lists descendants of a task excluding the task itself.
- [N-U46-219] The default portal task search matches the name or the numeric id text.
- [N-U46-220] Portal task lists always exclude tasks that belong to a template.
- [N-U46-222] A project-sharing image upload route (POST, login required) attaches an image to a task.
- [N-U46-223] The sharing chatter validates the project token, requires the record to be a task of the shared project and the user to hold sharing access, otherwise Forbidden.
- [N-U46-233] A non-manager user opening a project inherits the project manager's embedded action layout for the actions they have not customised.

### STATE

- [N-U46-044] Project, project stage, task, update, milestone and task-analysis records are company-scoped through global rules that admit records with no company.
- [N-U46-048] Project administrators see all stage records; other users see stages that are shared or owned by them; project users may write, create and delete their own personal stages.
- [N-U46-218] Portal task sorting offers newest, title, stage, status, priority, deadline and last stage update; project sorting only outside a single project; milestone sorting only when milestones exist.

### OPTIONALITY

None recorded.

### DEPENDENCY

None recorded.

### CONSTRAINT

- [N-U46-152] Constraint: one collaborator row per project and partner.
- [N-U46-221] The base task report action always raises nothing to report; timesheet extension is expected to override it.

### RISK

None recorded.

### UNKNOWN

None recorded.

## Capability 03: Task lifecycle

### WHAT

- [N-U46-875] Purpose inferred from the task model claims in this section: it carries a unit of work through stages, assignment, dependencies, recurrence, closing, duplication and time-related computed values.

### WHY

- [N-U46-876] Rationale inferred from the same claims: teams need a consistent record of who does what and by when, and reusable repetition for recurring work.

### BUSINESS RULE

- [N-U46-057] Default task ordering is priority descending, then sequence, then deadline ascending, then id descending.
- [N-U46-059] Default customer of a task comes from the parent task first, then from the project.
- [N-U46-062] Priority has four levels (low, medium, high, urgent), default low, indexed and tracked.
- [N-U46-065] A task without a project is labelled Private; project is computed, stored, tracked and precomputed.
- [N-U46-068] Task company is computed, stored, editable and copied on duplication.
- [N-U46-070] Four stored averaged metrics record working hours and days between creation and assignment or closing.
- [N-U46-071] The portal conversation history shows email, comment, outgoing and automatic comment messages only.
- [N-U46-072] Milestone is computed, stored, editable, tracked and limited to the project's milestones.
- [N-U46-074] Recurrence fields are Recurrent flag, recurrence link and a computed repeat interval, unit (day, week, month, year), type (forever, until) and end date.
- [N-U46-075] The title supports quick-create shortcuts: hash for tags, at-sign for assignee, and one to three exclamation marks for priority.
- [N-U46-076] A task can be flagged as a template; template ancestry is a stored recursive computed flag.
- [N-U46-077] A fixed list of readable task fields and a fixed list of writable fields is exposed for project-sharing portal users.
- [N-U46-078] The description is version-tracked (html history mixin).
- [N-U46-083] A task not displayed in its project inherits the parent task's project when they differ.
- [N-U46-085] The closed flag is searchable only for membership tests and maps to the two closed states or all other states.
- [N-U46-086] Rotting (stalled-record) logic excludes closed tasks.
- [N-U46-089] Default personal stages for a user are seven: Inbox, Today, This Week, This Month, Later, Done (folded), Cancelled (folded).
- [N-U46-090] Following a task with no explicit notification types inherits the project follower's notification preferences (parents of project subtypes plus internal or default ones).
- [N-U46-092] A recurrence is valid when the interval is positive and, for an until-type, the end date is in the future.
- [N-U46-093] Blocker counts (total and closed) are zero when the project does not allow dependencies.
- [N-U46-095] Task attachments list excludes those that belong to messages.
- [N-U46-096] Portal URL of a task is the my-tasks page by id.
- [N-U46-097] Sub-task allocated time is the sum of direct children's allocated hours.
- [N-U46-098] Sub-task counts include closed count and exclude template sub-tasks unless the parent is a template.
- [N-U46-099] Task contact number mirrors the customer's phone and writing it updates the customer's phone with elevated rights.
- [N-U46-100] Assignee names for sharing views are read in elevated mode so portal viewers see all assignees.
- [N-U46-101] The parent-task link is shown only if the viewer can read the parent.
- [N-U46-103] Copy from a template clears the template flag on tasks (unless the source is a project template) and strips a blacklist of
- [N-U46-104] A new task can never default to Waiting; it is reset to In Progress.
- [N-U46-105] Import applies default recurrence values when a task is flagged recurring without recurrence
- [N-U46-106] Creating a task with assignees stamps the assignment date.
- [N-U46-108] Portal-created tasks are created without change tracking, and without auto-subscribing the creator.
- [N-U46-109] Assignees other than the creator are subscribed and notified about the new task.
- [N-U46-110] After creation, CC email addresses that match a partner who is not exclusively a portal user are notified with an invitation and subscribed as followers.
- [N-U46-111] Tasks created in invited-users or portal projects get a portal access token.
- [N-U46-112] Writing a milestone on a task resets it when the milestone does not belong to the task's project (or the target project).
- [N-U46-114] Moving a task to another project notifies project followers subscribed to new-task events with a transferred-from message.
- [N-U46-116] Deleting a task also deletes all its sub-tasks; if it is the last task of a recurrence, the recurrence is removed and remaining tasks are unflagged.
- [N-U46-120] Task creation posts a new-task message differentiating tasks in a project from private ones.
- [N-U46-121] Notification recipients are grouped; project users get an extra group, and portal or invited recipients get an access button only if the project is invited-users or portal visibility.
- [N-U46-122] Replies to task notifications are addressed to the project's mail alias when the task has a project.
- [N-U46-123] A task created from an incoming email takes subject as title (or No Subject), zero allocated hours, author as customer (creating the partner if absent), no default assignee.
- [N-U46-125] A hook defines which tasks can make a project billable: those with a customer.
- [N-U46-126] A portal user opening a parent task in another project is sent to the sharing page if the parent project is shareable, else the portal task page if the button is displayed, else nothing.
- [N-U46-128] Archiving a task also archives sub-tasks that are not displayed separately in the project.
- [N-U46-129] On privacy change, portal-user followers can be unsubscribed from a task.
- [N-U46-130] Calendar unusual days (non-working) come from the current company's working calendar.
- [N-U46-131] Mention suggestions for sharing users are limited to followers of the task or its project.
- [N-U46-132] Task stages are ordered by sequence then id, and may be linked to many projects so that a workflow can be shared across projects.
- [N-U46-146] A recurrence has an interval (default 1), unit (day, week, month, year; default week), type (forever or until) and end date.
- [N-U46-148] The last task of a recurrence is the one with the highest id.
- [N-U46-168] Tags are ordered by name, have a random colour from one to eleven, and are linked to projects and tasks.
- [N-U46-170] In project context, tag search looks first at tags used on the project's latest one thousand tasks and then fills from a regular search.
- [N-U46-176] Partners show linked projects, tasks and a task count including child partners.
- [N-U46-178] A deprecated helper creates portal users for partners without users from a template.
- [N-U46-179] The partner's tasks action includes tasks of child partners and opens the form when there is one or none.
- [N-U46-205] When the stages belong to at most one project the archive proceeds directly; with several projects a confirmation form is shown first.
- [N-U46-206] Confirming archives every task in the stages and the stages themselves.
- [N-U46-231] Users hold a personal list of favorite projects through a relation table that is not copied.
- [N-U46-232] Creating internal users automatically creates default personal task stages for them using the user's language, with elevated rights.
- [N-U46-238] A task acknowledgment email template named Project: Request Acknowledgment is provided.

### STATE

- [N-U46-056] A task combines portal access, email thread with CC tracking, activities, customer rating, stage-duration tracking and html-description history mixins.
- [N-U46-058] Time spent in each stage is tracked through the duration-tracking mixin on the stage field.
- [N-U46-060] Default stage applies only when a default project is in context, using the first stage by fold, sequence, id.
- [N-U46-061] Default assignee is the current user only when a personal-stage default appears in context.
- [N-U46-063] Task state is one of In Progress, Changes Requested, Approved, Done, Cancelled, Waiting; default In Progress; stored, computed with an inverse and tracked.
- [N-U46-064] Stage is computed, stored, writable; deletion of a stage in use is restricted.
- [N-U46-066] Assignees are internal active users (non-share) held in a relation table that also stores each assignee's personal stage.
- [N-U46-067] Personal stage is stored on the same assignee relation row, restricted to stages owned by the current user.
- [N-U46-087] In the form, changing the project resets the state to In Progress unless Waiting or closed; a task without project and assignee is assigned to the current user.
- [N-U46-088] When the last task of a recurrence reaches a closed state, the next occurrence is created.
- [N-U46-102] Duplicating a task clears both dependency directions, keeps stage, restores archived tasks to active (unless copying a whole project) and appends a copy suffix to the title (except in project copy or template copy).
- [N-U46-107] On create with a stage, the end date follows folded-stage logic and the last stage update date is stamped.
- [N-U46-115] When a task enters a stage with rating enabled and status per stage, a rating request email is sent immediately.
- [N-U46-118] Notification emails include a subtitle showing the project and stage names.
- [N-U46-119] Entering a stage with an email template sends it as a note unless the task is a template.
- [N-U46-133] A stage created outside a project context is owned by the current user, making it a personal stage.
- [N-U46-134] A stage can reference an email template to notify the customer when a task reaches it.
- [N-U46-135] A stage can be folded; folded stages mark tasks as ended when entered.
- [N-U46-136] A stage can automatically change the task state from the customer's rating: good feedback approves, neutral or bad requests changes.
- [N-U46-137] A stage has a staleness threshold in days; zero disables it.
- [N-U46-138] Customer rating requests per stage are sent either on reaching the stage or periodically; the period is daily, weekly, twice a month, monthly, quarterly or yearly, default monthly.
- [N-U46-139] Deleting a stage opens a wizard listing every project that has tasks in it (including archived tasks) or is linked to it.
- [N-U46-140] Archiving a stage archives all tasks in it.
- [N-U46-141] Enabling rating on the first stage, or disabling it on the last stage that has it, shows or hides the rating message types and makes them default.
- [N-U46-142] Copying a stage appends a copy suffix to its name.
- [N-U46-144] Unarchiving a stage that contains archived tasks opens a wizard offering what to do with those tasks.
- [N-U46-145] A daily job sends rating requests for tasks in stages set to periodic rating when the deadline is due, then recomputes the deadline and commits per stage.
- [N-U46-149] The personal stage model shares its storage with the assignee relation: one row per task and assignee, carrying the stage.
- [N-U46-204] The task-stage deletion wizard counts tasks including archived ones in the stages to delete.
- [N-U46-234] A scheduled job named Project Stage: Send rating runs a stage-level rating dispatch, with a daily interval (the interval number is a default).
- [N-U46-236] A saved export template named Tasks exports id, project, name, assignees, stage, state and tags.
- [N-U46-237] The task message types seeded are created, stage changed, in progress, changes requested, approved, cancelled, done, waiting and rating; none is default-on, and created, waiting and rating are hidden.

### OPTIONALITY

- [N-U46-084] With task dependencies enabled, a non-closed task with any open blocker becomes Waiting.
- [N-U46-117] A task is flagged when milestones are enabled and its milestone is unreached with deadline today or earlier.
- [N-U46-207] The delete option unlinks the stages directly.

### DEPENDENCY

None recorded.

### CONSTRAINT

- [N-U46-069] A parent task must itself have a project and must not be a descendant of the task.
- [N-U46-073] Task dependencies are a many-to-many relation (Blocked By and its inverse Block), not copied on duplication, tracked and limited to tasks with a project and not itself.
- [N-U46-079] Database check: a recurring task cannot have a parent.
- [N-U46-080] Database check: a task without a project cannot have a parent.
- [N-U46-081] Constraint: if both the customer and the task have a company, they must match.
- [N-U46-082] Constraint: a task without project cannot have sub-tasks.
- [N-U46-091] Constraint: dependency cycles are forbidden.
- [N-U46-094] Constraint: recursive sub-task hierarchy forbidden.
- [N-U46-113] Error: setting a stage without a project is only allowed for private-task personal stages.
- [N-U46-127] Converting to sub-task is refused for private tasks with an error notice.
- [N-U46-143] Deleting a personal stage moves its tasks to the nearest remaining stage of the same user, preferring a lower sequence, and raises an error if an active internal user would be left with none.
- [N-U46-147] Constraint: recurrence interval must be positive.
- [N-U46-169] Constraint: tag names are unique (case sensitive at the database level).
- [N-U46-177] Constraint: a partner's company cannot differ from its projects' company, nor from its tasks' company.

### RISK

- [N-U46-124] Cover image auto-selection compares the attachment type to the bare word image rather than a prefix match; an exact match would rarely hold, so the behaviour must be confirmed at runtime.

### UNKNOWN

None recorded.

## Capability 04: Milestones, updates and project reports

### WHAT

- [N-U46-877] Purpose inferred from the milestone, status update, burndown and task analysis claims in this section: it tracks deliverable checkpoints, periodic status reports and progress charts.

### WHY

- [N-U46-878] Rationale inferred from the same claims: stakeholders need a dated view of progress and of how work moves between stages.

### BUSINESS RULE

- [N-U46-155] Reached flag defaults to false and is not copied; the reached date is stored as today's date when flagged.
- [N-U46-156] A milestone is overdue when not reached and its deadline is before today.
- [N-U46-157] Task and done-task counts per milestone are visible only to users with the milestone feature group and count only tasks whose project allows milestones.
- [N-U46-158] A milestone can be marked done when it is not reached, has at least one closed task and no open ones.
- [N-U46-159] The milestone tasks action defaults new tasks to the project and milestone and opens the form when there is one task.
- [N-U46-160] Copying milestones records an old-to-new mapping in context used when copying tasks, only if the project allows milestones.
- [N-U46-165] Creating an update makes it the project's last update and snapshots total and closed task counts.
- [N-U46-166] Deleting an update re-points the project's last update to the newest remaining one by date.
- [N-U46-167] The default update description renders a template with project, profitability figures (if shown) and milestone sections.
- [N-U46-180] The burndown report is an abstract, non-table model whose search builds a SQL common table expression on demand.
- [N-U46-186] The task analysis report is a read-only database view of tasks that belong to a project, ordered by name descending then project.
- [N-U46-188] The last rating is shown only when non-zero and the average rating averages consumed ratings at or above the minimum rating limit.
- [N-U46-189] The late-milestone flag in the analysis view uses less-or-equal against today, so a milestone due today counts as late here.
- [N-U46-190] Days to deadline is the difference between deadline and the current UTC time in days; it is evaluated at query time, not stored.
- [N-U46-191] Working days and hours to open or close come from task fields and zero values are reported as empty.
- [N-U46-192] The view joins the dependency relation so a task blocking others appears with a count of dependents and is grouped by the dependency.
- [N-U46-229] A partial index on message date, record and id for task notification messages supports the burndown history query.

### STATE

- [N-U46-162] Project status values map to colours: on track green, at risk orange, off track red, on hold light blue, complete purple, and a to-define value for projects with no status.
- [N-U46-163] A new update defaults to the project from the active record, the previous progress, a generated description and the project's last status (on track if the project has none).
- [N-U46-164] An update has a required title, required status, tracked progress integer, author defaulting to the current user, date defaulting to today and html description.
- [N-U46-181] Filters on assignment date, deadline, last stage update, state, milestone, customer, project, stage, tags and assignees are applied to the task table first, to limit the subset used for the history computation.
- [N-U46-182] The default grouping is by month and stage; the date interval drives the series step, with quarter equal to three months.
- [N-U46-183] Stage history is reconstructed from the message tracking values of the task stage field; each interval begins at the previous change date or at task creation.
- [N-U46-184] Each stage interval is expanded into one row per date step up to the current date plus one interval.
- [N-U46-187] The analysis flags a task closed when its state is done or cancelled.

### OPTIONALITY

- [N-U46-154] Milestones belong to a non-template project (required, cascade on project deletion), carry an optional tracked deadline and a reached flag, and are ordered by sequence, deadline, reached first, name.
- [N-U46-161] The display name optionally includes the deadline date when requested by context.

### DEPENDENCY

None recorded.

### CONSTRAINT

- [N-U46-185] Reading the burndown report requires grouping by date and by stage or closed status, otherwise an error is raised.

### RISK

None recorded.

### UNKNOWN

None recorded.

## Capability 05: Customer rating

### WHAT

- [N-U46-879] Purpose inferred from the rating model, link and stage-triggered request claims in this section: it collects a satisfaction score from a customer through a tokenised link and aggregates it on the rated record.

### WHY

- [N-U46-880] Rationale inferred from the same claims: service quality needs a simple customer-sourced measure that can be averaged and traced to the person and the record.

### BUSINESS RULE

- [N-U46-241] The rating value is a float averaged on aggregation, defaulting to zero; zero means not yet rated.
- [N-U46-242] Each rating request receives a random token used to submit the rating without logging in.
- [N-U46-243] A rating is only counted once it is marked as filled (consumed).
- [N-U46-244] The internal-only visibility flag is mirrored from the linked chatter message and stored.
- [N-U46-245] The stored resource name is the record's display name read with elevated rights, falling back to model and id.
- [N-U46-246] A face image is chosen by thresholds: five for satisfied, three for neutral, one for unhappy, zero for unrated.
- [N-U46-247] Whenever the rating value or comment is created or written, the rated-on timestamp is set to now.
- [N-U46-248] On create or write with a document, the parent document is looked up from the document's declared parent field.
- [N-U46-249] Deleting a rating also deletes its chatter message.
- [N-U46-251] Partial indexes accelerate lookups of consumed ratings by document and by parent document.
- [N-U46-252] Average-rating bands: at or above 3.66 happy, at or above 2.33 neutral, at or above 1 unhappy, below that not rated.
- [N-U46-253] A mixin adds last value, last feedback, count, average, average text and satisfaction percentage to rated models.
- [N-U46-254] The stored last rating value is the latest consumed rating of the record by modification date, else zero.
- [N-U46-255] Count and average count only consumed ratings with a value of at least one.
- [N-U46-256] Searching by average rating computes averages over all consumed ratings of the model with elevated rights and compares with two-digit float precision.
- [N-U46-257] Satisfaction is the share of great ratings among rated records, and minus one when nothing has been rated.
- [N-U46-258] Renaming a rated record refreshes its ratings' stored names; changing its parent re-points the ratings' parent.
- [N-U46-259] The distribution always lists the values one through five, with unrated excluded; values are rounded to one decimal place.
- [N-U46-260] Publishing rating statistics is off by default and may be overridden.
- [N-U46-261] Rating value, feedback, image and average fields are restricted to internal users while the stored count uses elevated computation.
- [N-U46-262] A parent mixin (used by projects) aggregates ratings of child documents: count, average, average as fraction and satisfaction percentage.
- [N-U46-263] A parent may limit statistics to the last N days; by default all ratings are included.
- [N-U46-264] Parent statistics count only consumed ratings with a value of at least one.
- [N-U46-265] A chatter message can link ratings; the message's rating is the latest consumed one and its value is zero when none.
- [N-U46-266] Deleting any threaded record deletes its ratings, using elevated rights.
- [N-U46-267] By default the rated operator is the record's responsible user partner, and the rating customer is the record's partner.
- [N-U46-268] Asking for a token reuses an unconsumed rating for the customer or creates one, after checking read access, and the rating is created as not internal.
- [N-U46-270] Posting with a rating value creates a consumed rating by the current user's partner, with elevated rights.
- [N-U46-271] Editing a message with a new value updates the rating; clearing the value detaches and deletes the rating.
- [N-U46-273] A logged-in user whose commercial partner differs from the rating's customer sees an invalid-partner page; a public visitor is allowed with the token.
- [N-U46-274] The submit page is rendered in the customer's language, falling back to the visitor's language.
- [N-U46-275] Feedback submission accepts GET and POST but only POST records the rating and comment, using elevated rights and the default message type.
- [N-U46-276] Internal users may read, write and create ratings but not delete; public and portal have no rating access; administrators have full access.

### STATE

None recorded.

### OPTIONALITY

- [N-U46-240] A rating record is ordered by last modification then id, and links to any document by model and id, optionally with a parent document.
- [N-U46-250] Resetting a rating sets value to zero, issues a new token, clears the comment and marks it unconsumed so it can be asked again.
- [N-U46-277] A Ratings menu is placed in the technical menu under discuss configuration.
- [N-U46-869] The restored database holds 4 access rows and 1 menu owned by the rating module; the project rating schedule is active and daily.

### DEPENDENCY

- [N-U46-239] The rating module depends only on the messaging module and ships views, portal templates, message views and access rights.

### CONSTRAINT

- [N-U46-269] Applying a rating raises an error if the value is outside zero to five or the token or rating is invalid.
- [N-U46-272] The public rating link carries a token and a value; only the values five (happy), three (neutral) and one (unhappy) are accepted, others raise an error.

### RISK

None recorded.

### UNKNOWN

None recorded.

## Capability 06: Project cost and revenue bridges

### WHAT

- [N-U46-881] Purpose inferred from the profitability, analytic and bridge claims in this section: it brings costs and revenues of related business documents onto the project as a profitability view.

### WHY

- [N-U46-882] Rationale inferred from the same claims: a project owner needs to compare what was spent and earned against the work delivered.

### BUSINESS RULE

- [N-U46-224] An analytic account lists the projects linked to it and a project count.
- [N-U46-226] The analytic account projects action opens the form directly when there is a single project and disables creation.
- [N-U46-279] The drill-down action on the cost section is offered only to users in the invoicing or the accounting read-only group.
- [N-U46-280] The bill domain covers vendor bills and vendor credit notes only.
- [N-U46-281] Only draft and posted entries count; cancelled entries are excluded. Draft lines feed the to-bill column, posted lines feed the billed column.
- [N-U46-282] Lines whose subtotal is zero are excluded.
- [N-U46-283] Bill lines already counted by another profitability source are excluded to avoid double counting.
- [N-U46-284] Bill lines are searched with elevated rights, so the cost figures do not depend on the viewer's accounting access.
- [N-U46-285] A bill line belongs to the project when its analytic distribution contains the project's analytic account.
- [N-U46-286] Each line balance is converted from the company currency to the project currency at the line date.
- [N-U46-287] A line's contribution is scaled by the sum of the percentages given to the project's account in its distribution, so shared lines count proportionally.
- [N-U46-288] Costs are expressed with the sign inverted from the balance, so a vendor bill appears as a positive cost and a vendor credit note reduces it.
- [N-U46-289] The section is omitted when both billed and to-bill totals are zero, for example when a bill is fully offset by a credit note.
- [N-U46-290] The section is labelled Vendor Bills and given display sequence 11.
- [N-U46-291] Two further labels are registered for other revenues and other costs taken from analytic lines.
- [N-U46-292] Display sequences are 11 for vendor bills, 14 for other revenues and 15 for other costs.
- [N-U46-293] Drill-down for other revenues or costs opens the analytic entries list, with a pivot and graph view when several records and a form when one.
- [N-U46-294] Drill-down for vendor bills opens the vendor bill list filtered to the contributing entries, or a single form when only one.
- [N-U46-295] Unknown section names are delegated to the next module in the chain.
- [N-U46-296] The domain for analytic lines without an accounting entry is split out so a timesheet module may extend it.
- [N-U46-297] Other revenues and costs come from analytic lines on the project account that are not linked to an accounting entry line.
- [N-U46-298] Analytic lines in the manufacturing-order and picking-entry categories are excluded from the other items, since those are reported by their own sections.
- [N-U46-299] Analytic lines are read with elevated rights.
- [N-U46-300] Negative analytic amounts count as costs and non-negative amounts count as revenues.
- [N-U46-301] Totals are converted per line currency into the project currency using the project's company and the current date.
- [N-U46-303] The drill-down on the other items requires the accounting read-only group.
- [N-U46-304] A project can open the analytic entries filtered to its analytic account, with the account pre-set as default and creation allowed only from an embedded action.
- [N-U46-305] Analytic items are exposed as embedded actions on the project, visible only to the analytic accounting group.
- [N-U46-307] When an expense is created or computed within a project context, its analytic distribution defaults to the project's analytic distribution unless one is already set.
- [N-U46-308] Without a project in the context the standard distribution computation applies unchanged.
- [N-U46-309] On creation the project distribution is applied only when it is non-empty, and an explicitly supplied distribution wins.
- [N-U46-310] The expense drill-down returns nothing when neither a filter nor a list of expense ids is given.
- [N-U46-311] The expense list opened from a project carries the project in its context so new expenses inherit the project's analytic distribution.
- [N-U46-312] A single expense opens directly in a form unless the action was launched from an embedded action.
- [N-U46-313] Vendor bill lines that originate from an expense are excluded from the vendor-bill cost section so expenses are not counted twice.
- [N-U46-314] A project can open expenses whose analytic distribution contains its analytic account.
- [N-U46-315] The expenses section is labelled Expenses and placed at sequence 13 in profitability.
- [N-U46-316] Purchase orders and expenses paid by an employee both create vendor bills, so the profitability report makes the two sources exclusive.
- [N-U46-317] A project with no analytic account has no expense section.
- [N-U46-318] The expense drill-down is shown only to users in the expense team-approver group.
- [N-U46-320] Expenses are grouped by currency and summed on the untaxed amount, so taxes are excluded from project cost.
- [N-U46-321] Each currency subtotal is converted into the project currency using the project company.
- [N-U46-322] Expense totals are reported as a negative amount in the billed column; nothing is placed in to-bill.
- [N-U46-323] Analytic lines tied to an entry line that came from an expense are excluded from the other-items analytic domain, to avoid duplication with the expense section.
- [N-U46-324] The expense section is appended to the cost data and its totals are added to the project cost totals.
- [N-U46-327] Revenue is taken only from confirmed sales order lines flagged as expense lines.
- [N-U46-329] An order line counts only if its product also appears among that order's expenses on this project.
- [N-U46-330] A revenue entry for expenses appears only when at least one expense was re-invoiced; the cost entry is always produced.
- [N-U46-331] Re-invoiced to-invoice and invoiced amounts are converted per currency into the project currency.
- [N-U46-332] Invoice lines of the sales orders that carry project expenses are marked as already included so they are not counted twice as other revenues.
- [N-U46-334] If the project's analytic accounts belong to plans not yet present on the expense, both distributions are kept combined; if a plan overlaps, the project distribution takes priority.
- [N-U46-335] When an expense linked to a sales order with a project is posted and has no distribution, the project's distribution is applied first.
- [N-U46-336] If the project has no analytic account yet, posting such an expense creates one.
- [N-U46-337] For entry lines created from expenses, the sales order is determined from both the project analytic mapping and the expense's own order, with the expense mapping taking precedence.
- [N-U46-339] A purchase line's analytic distribution is recomputed when its product, the order's vendor or the order's project changes.
- [N-U46-340] Only real product lines are affected; section and note lines are skipped. A project can come from the order or from the context.
- [N-U46-341] If the line already has a distribution, the project's analytic accounts are appended only for analytic plans not yet used on the line; existing percentages are kept.
- [N-U46-342] A line with no distribution takes the project's distribution wholesale.
- [N-U46-343] After creation the distribution is explicitly recomputed so the project rule applies to lines created in bulk.
- [N-U46-344] The purchase-order count on a project is visible only to purchasing users.
- [N-U46-345] Orders linked directly to the project count only if they have at least one line.
- [N-U46-346] Orders reached only through a line distribution naming the project's account are counted in addition to directly linked orders, without double counting.
- [N-U46-347] A project without an analytic account counts only the orders directly linked to it.
- [N-U46-348] Opening the project's orders finds orders by either line distribution or direct project link, and pre-sets the project as default on new orders.
- [N-U46-349] A single matching order opens directly in a form unless the action comes from an embedded action.
- [N-U46-350] The profitability drill-down on purchase orders is read-only: creating and editing are disabled in its context.
- [N-U46-351] A Purchase Orders statistic button, hidden when the count is zero and positioned at sequence 36, appears only for purchasing users.
- [N-U46-352] Analytic lines whose entry line came from a purchase line are excluded from the other-items domain so purchase costs are not duplicated.
- [N-U46-353] The base vendor-bill step is switched off here and replaced by a combined purchase-order step in the profitability calculation.
- [N-U46-354] The Purchase Orders cost section is placed at sequence 10.
- [N-U46-355] Cost lines are purchase order lines whose distribution contains the project's analytic account.
- [N-U46-357] The drill-down is offered to purchasing users, invoicing users and accounting read-only users.
- [N-U46-358] Each line's untaxed subtotal is converted to the project currency and scaled by the project's share in the line distribution.
- [N-U46-359] Linked bill lines that are not cancelled and that carry the project's account are used to determine what has been billed.
- [N-U46-360] Refund lines count as negative cost; only non-refund lines count toward the billed-so-far figure used to compute the unbilled remainder.
- [N-U46-361] Posted bill lines go to the billed column and draft ones to to-bill.
- [N-U46-362] The unbilled remainder equals the ordered amount minus the non-refund billed amount and is added to to-bill.
- [N-U46-363] A line with no linked bill counts its whole ordered amount as to-bill.
- [N-U46-364] After purchase orders, remaining vendor bill lines with the project's account that are not already counted are reported through the shared bill-cost step.
- [N-U46-365] All purchase profitability logic runs only when the project has an analytic account.
- [N-U46-366] When the product catalog is updated for an order line, a project passed by the caller is added to the request context so new lines inherit the project's analytic distribution.
- [N-U46-367] Receipts generated from a purchase order carry the order's project when one is set.
- [N-U46-368] Purchase orders generated by replenishment rules take the project from the procurement values.
- [N-U46-369] When looking for an existing draft order to merge into, the project must match, so demand for different projects is never merged into the same order.
- [N-U46-371] A project can open its outgoing deliveries, incoming receipts or all transfers, filtered by the project reference.
- [N-U46-372] Delivery and receipt views are restricted to the matching operation type and new transfers are pre-set to the project.
- [N-U46-373] A new delivery opened from a project defaults its partner to the project's customer.
- [N-U46-374] The activity view is offered for receipts and all-transfers but not for deliveries.
- [N-U46-376] When a landed cost targets transfers, each journal line of the cost adjustment takes the analytic distribution of the project of the related transfer.
- [N-U46-378] The order's project is recomputed from its bill of materials whenever the bill of materials changes.
- [N-U46-379] When orders are opened from a project's own action the project is not recomputed from the bill of materials, so the project's default is preserved.
- [N-U46-380] Generating a bill of materials from an order carries the order's project over as the default.
- [N-U46-381] An order can open its project's form directly.
- [N-U46-383] A manufacturing order created by a replenishment rule takes the project from the procurement values.
- [N-U46-385] The bill-of-materials and manufacturing-order counts on a project are visible only to manufacturing users.
- [N-U46-386] The counts are read-grouped per project; a project with none receives an empty value rather than zero.
- [N-U46-387] The bill of materials list opened from a project is filtered by the project and new bills default to it.
- [N-U46-388] A single bill opens directly in a form unless launched from an embedded action.
- [N-U46-389] The manufacturing order action is filtered by the project and flags itself as coming from a project action.
- [N-U46-390] Two statistic buttons, Bills of Materials at sequence 35 and Manufacturing Orders at sequence 46, appear only for manufacturing users and only when the count is positive.
- [N-U46-391] Project users receive read-only access to bills of materials and their lines.
- [N-U46-392] The project field on manufacturing orders and bills is shown only to project users.
- [N-U46-393] Bills of materials and manufacturing orders are exposed as embedded actions on the project, both in the task area and on the dashboard.
- [N-U46-395] Analytic lines created from component moves of a manufacturing order are categorised as manufacturing order costs.
- [N-U46-397] The accounting bridge repeats the project propagation onto manufacturing orders created by replenishment rules.
- [N-U46-398] A manufacturing order records whether its project has any analytic account, and can open those accounts.
- [N-U46-399] Changing the project of an order that is no longer draft re-creates its component analytic moves and work-order analytic entries.
- [N-U46-400] Relevant analytic plans for the manufacturing business area, filtered by the produced product, are evaluated per order at confirmation.
- [N-U46-402] The mandatory-plan validation runs before the standard confirmation.
- [N-U46-403] Work-order labour cost is also distributed across the project's analytic accounts, producing additional analytic lines attached to the work order.
- [N-U46-404] A Manufacturing Orders cost section appears in profitability at sequence 12.
- [N-U46-405] Manufacturing analytic lines are excluded from the generic other-items domain since they have their own section.
- [N-U46-406] The manufacturing cost is the sum of analytic lines in the manufacturing category on the project's account, grouped by currency and converted to the project currency.
- [N-U46-407] The drill-down link to manufacturing orders is offered only for a single project and to manufacturing users.
- [N-U46-408] The total is shown in the billed column, taken as the signed analytic amount (costs are negative); to-bill stays zero.
- [N-U46-410] When a landed cost targets manufacturing orders, each journal line takes the analytic distribution of the project of the related order.

### STATE

- [N-U46-302] Because billing status is unknown for analytic lines, all of it is shown as billed or invoiced; the to-bill and to-invoice amounts stay zero.
- [N-U46-328] Only orders in the confirmed state count toward re-invoiced expense revenue.

### OPTIONALITY

- [N-U46-278] Project profitability gains a vendor-bill cost section that is built from vendor bill lines tagged with the project's analytic account.
- [N-U46-326] Expenses are grouped by sales order, product and currency so each re-invoiced item can be matched to the order line that bills it.
- [N-U46-333] For an expense linked to a sales order outside a project context, the analytic distribution is recomputed to merge in the order project's distribution.
- [N-U46-338] A purchase order gains an optional project reference that excludes project templates.
- [N-U46-370] A transfer gains an optional project reference that excludes project templates.
- [N-U46-377] A manufacturing order has an optional project reference, stored, computed from the bill of materials and editable by hand; templates are excluded.
- [N-U46-382] A bill of materials has an optional project reference that excludes templates.
- [N-U46-384] Procurement values for component moves inherit the project only when the procurement group is linked to exactly one manufacturing order.
- [N-U46-394] For component moves of a manufacturing order, the analytic distribution comes from the order's project, falling back to the standard source when the project has none.

### DEPENDENCY

- [N-U46-306] A bridge module adds the number of expenses linked to a project's analytic account to the project form; it is installed automatically when project accounting and expenses are both present.
- [N-U46-325] The sale-expense bridge adds full traceability of re-invoiced expenses to the profitability report and is installed automatically with its three dependencies.
- [N-U46-375] The landed-cost bridge depends on a project stock-accounting bridge that is outside this unit's assignment.
- [N-U46-409] This module is a technical bridge with no code of its own; it only ensures the manufacturing, sale-manufacturing and sale-project modules cooperate.

### CONSTRAINT

- [N-U46-225] An analytic account cannot be deleted while any project linked to it has tasks (the check is skipped at module uninstall).
- [N-U46-396] Before analytic lines are generated for such a move, every analytic plan mandatory for manufacturing must be set on the project; otherwise a validation error names the missing plans and the project.
- [N-U46-401] Confirming an order is blocked when its project lacks a distribution for any mandatory analytic plan.

### RISK

- [N-U46-319] Only expenses in the posted, in-payment or paid state are counted; the expense state list includes an in-payment value that must be confirmed against the expense model in this version.
- [N-U46-356] The state filter on purchase lines uses a plain string rather than a list; only confirmed orders are intended, and the effective matching of the string operand needs runtime confirmation.

### UNKNOWN

None recorded.

## Capability 07: Collaboration extensions

### WHAT

- [N-U46-883] Purpose inferred from the claims of the small extension modules in this section: they add personal tasks, text message notifications on stage change, a mail add-in action, skill search and a resource calendar link.

### WHY

- [N-U46-884] Rationale inferred from the same claims: individual users and teams want light channels into the same task data without separate tools.

### BUSINESS RULE

- [N-U46-227] The management digest can include an open-task KPI.
- [N-U46-414] A task created with no name, no project and no parent is treated as a to-do and gets a generated name.
- [N-U46-415] The generated name is the first line of the description as plain text with asterisks removed, truncated to 97 characters plus an ellipsis when longer than 100.
- [N-U46-416] With no description either, the name is Untitled to-do.
- [N-U46-418] A helper returns the identifiers of the kanban, list, form, calendar and activity views used by the To-Do application.
- [N-U46-420] Internal users may read, write and create the to-do-with-activity wizard but not delete it.
- [N-U46-422] The private-task rule is protected against overwrite on module update.
- [N-U46-423] The activity summary shown in the systray removes the single task entry and replaces it with separate entries for to-dos and regular tasks.
- [N-U46-424] A task counts as a regular task when it has a project, otherwise as a to-do.
- [N-U46-426] Only activities assigned to the current user are counted, and archived activities are included only when the active filter is off.
- [N-U46-427] The total count shown in the badge sums today and overdue activities only.
- [N-U46-429] When users are onboarded into the project application the onboarding to-do is also generated for them.
- [N-U46-432] The onboarding to-do is titled Welcome plus the user's name, is rendered in the user's language, and is assigned to that user.
- [N-U46-433] The onboarding to-dos are created by the superuser with notification of auto-subscribed followers suppressed.
- [N-U46-434] A quick-create dialog collects summary, required due date (default today), note and an assignee fixed to the current user.
- [N-U46-435] Confirming the dialog creates a to-do task with the user as only assignee and also schedules an activity on it for the same user, deadline and summary.
- [N-U46-436] The activity uses the default activity type for tasks.
- [N-U46-437] A success notification is shown afterward.
- [N-U46-438] The To-dos list shows tasks with no project and no parent that are assigned to the current user.
- [N-U46-440] New items created from the To-dos action default to having no project.
- [N-U46-441] The search view offers open, closed, archived, deadline, activity and group-by filters, and opens by default on open to-dos.
- [N-U46-442] A top-level To-do menu opens the To-dos action.
- [N-U46-443] The onboarding note tells users that to-dos are private by default and become shared when other assignees are added.
- [N-U46-453] The message goes to the project's customer partner only.
- [N-U46-456] A record rule limits project managers' create, update and delete of SMS templates to templates for tasks and projects; the rule has no read permission, so reading is not narrowed by it.
- [N-U46-459] Project features are exposed to the mail add-in only when the current user can create tasks.
- [N-U46-460] The contact card lists up to five tasks of the contact.
- [N-U46-461] Listed tasks are further restricted to projects the user can read.
- [N-U46-462] The contact data tells the add-in whether the user may create projects.
- [N-U46-463] With no contact, the task section is returned empty.
- [N-U46-464] Tasks are added to the whitelist of record types onto which email content may be logged.
- [N-U46-465] This module's translations are added to those served to the add-in.
- [N-U46-466] Project search, task creation and project creation are exposed as JSON endpoints with the add-in authentication method and open cross-origin access.
- [N-U46-467] Project search matches names containing the term, returns up to five by default, and returns partner name and company.
- [N-U46-468] Project details are read with elevated rights after a record-rule-filtered search.
- [N-U46-470] An empty email subject yields the task name Task for plus the partner name.
- [N-U46-471] The task is created in the partner's company, with the email body as description, linked to the partner and project, and with the current user as assignee.
- [N-U46-472] Project creation from the add-in sets only the name; all other values come from defaults.
- [N-U46-474] A dedicated action opens the task form in the main task form view so the add-in can redirect the user to a new task.
- [N-U46-476] A task exposes the skills of all its assignees as a read-through list.
- [N-U46-477] A user exposes the skills of the linked employee.
- [N-U46-478] The task analysis report also exposes the assignees' skills.
- [N-U46-479] The skills search on tasks matches tasks with no assignee as well as tasks whose assignees have matching skills, so unassigned tasks always appear.
- [N-U46-481] A resource's colour defaults to a random number between one and eleven.
- [N-U46-483] The avatar card data for a resource is whatever fields the caller requests, read with the caller's own access.

### STATE

- [N-U46-425] Per task the earliest activity deadline is classed as today, overdue or planned, so each task counts at most once per state.
- [N-U46-439] To-dos are organised by each user's personal stages, grouped by personal stage by default in kanban and list.
- [N-U46-446] A task stage can hold an SMS template restricted to templates for tasks.
- [N-U46-447] A project stage can hold an SMS template restricted to templates for projects.
- [N-U46-448] A task SMS is sent only when the task has a customer, a stage with a template, and is not a template task.
- [N-U46-449] A text message is also sent on task creation when the initial stage has a template.
- [N-U46-450] A text message is sent whenever a task's stage is written; the send runs with elevated rights because the template model is protected.
- [N-U46-451] A project SMS is sent only when the project has a customer and a stage with a template.
- [N-U46-452] A text message is also sent on project creation and whenever the project's stage is written.
- [N-U46-457] An upgrade script rewrites the earlier version of this rule, which targeted stage models, to the current task and project model filter.
- [N-U46-482] A resource exposes the online presence status of its linked user.

### OPTIONALITY

- [N-U46-412] On installation an onboarding to-do is generated for every internal (non-portal, non-public) user.
- [N-U46-413] The post-install hook targets users whose share flag is off, i.e. internal users.
- [N-U46-419] Every internal user receives full create, read, write and delete rights on task stages, tasks and tags at the access-list level; actual task visibility is restricted by record rules.
- [N-U46-421] A record rule gives every internal user full access to a private task that has no project, no parent and lists the user as assignee.
- [N-U46-430] The override does not return the result of the parent call, so a caller that uses the returned users would receive nothing.
- [N-U46-444] The onboarding note describes title shortcuts: hash for tags, at-sign for user, and one to three exclamation marks for medium, high and urgent priority. The parsing itself lives in client scripts that were not read.
- [N-U46-455] Project managers receive full access to SMS templates at the access-list level.
- [N-U46-484] The module adds client-side avatar components for resources whose behaviour was not read.
- [N-U46-870] The restored database holds 4 access rows, 1 record rule and 1 menu owned by the personal tasks module.

### DEPENDENCY

- [N-U46-411] The to-do module depends only on the project module and is installed automatically; it is also an application with its own menu.
- [N-U46-417] Converting a to-do to a task sets the task's company from the chosen project and opens the task form; making it visible to others depends on the project assignment.
- [N-U46-445] The SMS bridge sends a text message to the customer when a project or task reaches a stage that has an SMS template, and is installed automatically with project and sms.
- [N-U46-458] The mail-plugin bridge lets an inbox add-in turn emails into tasks and log their content as internal notes.
- [N-U46-475] The skills bridge lets users search tasks according to the skills of their assignees.
- [N-U46-480] The resource-mail bridge is installed automatically and carries the messaging avatar features over to planning resources instead of users.

### CONSTRAINT

- [N-U46-431] If the onboarding template cannot be rendered the user is skipped silently.
- [N-U46-469] Task creation returns an error value, not an exception, when the partner or project does not exist.

### RISK

- [N-U46-428] The systray split is computed by a hand-written query on the activity and task tables and bypasses record rules; it was not executed.
- [N-U46-454] The write hook triggers on every write containing the stage key even if the stage did not change, so repeated writes of the same stage could resend the message; this was not executed.
- [N-U46-473] The project-creation endpoint performs no explicit permission check of its own, relying on the standard access rules at creation.

### UNKNOWN

None recorded.

## Capability 08: Purchase order management

### WHAT

- [N-U46-885] Purpose inferred from the order, line, vendor bill matching, portal and extension claims in this section: it lets a company request quotations, confirm orders with vendors, receive and bill them, and extend the flow with agreements, repairs, grid entry and electronic documents.

### WHY

- [N-U46-886] Rationale inferred from the same claims: procurement needs controlled commitment to vendors, traceability to bills and receipts, and optional approval steps.

### BUSINESS RULE

- [N-U46-487] A purchase order exposes an on-time delivery rate as a fraction, shown as a percentage; lines mirror the order's value.
- [N-U46-488] The fraction is the on-time rate divided by one hundred, or minus one when the rate is not available, in which case the view hides it.
- [N-U46-489] Choosing an agreement on a purchase order sets the order's receiving operation type from the agreement.
- [N-U46-490] A purchase agreement has a required receiving operation type defaulting to the first incoming type of a warehouse of the current company.
- [N-U46-491] If no incoming type exists the user is redirected with a warning to create a warehouse.
- [N-U46-493] An agreement line can point to a downstream stock move, and a purchase line generated from it is linked to that move.
- [N-U46-494] A purchase order generated by replenishment takes the vendor reference and agreement from the supplier's agreement, and the agreement's currency when set.
- [N-U46-495] When looking for an existing draft order to merge into, orders are matched on the same agreement as well, so supply under different agreements is never merged.
- [N-U46-497] Tracing upstream documents of a stock move reads agreement lines with elevated rights so users without purchase rights can still perform the operation.
- [N-U46-498] The upstream document is the agreement and its responsible user, unless the agreement is done or cancelled.
- [N-U46-499] An alternative quotation created from an order inherits the original order's receiving operation type and its source references.
- [N-U46-500] Alternative lines keep the downstream stock move links of the lines they copy.
- [N-U46-501] Stock managers receive read and create but not write or delete rights on agreements and agreement lines, so downstream stock flows can create them.
- [N-U46-503] The count follows each order line's downstream moves back to the repair orders that required the parts.
- [N-U46-504] The repair action opens the single repair in a form, or a list named Repair Source when several.
- [N-U46-505] A repair order shows how many purchase orders were generated from its parts, visible only to purchasing users.
- [N-U46-506] The count follows the repair's parts moves to the purchase lines created for them.
- [N-U46-507] The purchase button on a repair is hidden when no purchase exists or the repair is still draft.
- [N-U46-508] A single generated purchase order opens in a form, several open in a list.
- [N-U46-510] The matrix is built server-side so very large grids are not truncated by the client's loading limit.
- [N-U46-511] Three technical fields carrying the template, update flag and grid content are not stored.
- [N-U46-512] Selecting a product template builds the matrix for it and marks it as not yet an update to apply.
- [N-U46-513] Edits made through the grid are treated as changes that reset line planned dates.
- [N-U46-514] Applying the grid only acts when the update flag is set.
- [N-U46-515] Only cells whose quantity changed are processed.
- [N-U46-516] Each changed cell creates or finds the matching product variant.
- [N-U46-517] A cell whose quantity equals the current total across existing lines is skipped.
- [N-U46-520] A variant on exactly one line has that line's quantity replaced by the cell value.
- [N-U46-521] A positive cell with no existing line creates a new line from default line values, continuing the last sequence and storing non-variant attribute selections.
- [N-U46-522] After changes, prices and descriptions of new or modified lines are recomputed.
- [N-U46-523] When reopening the grid, each cell is pre-filled with the quantity summed across order lines whose attribute combination matches.
- [N-U46-525] Printed grids omit rows whose quantities are all zero.
- [N-U46-529] The module exports and imports electronic purchase orders in a Peppol ordering format, and the order PDF is embedded inside the exported electronic file so the receiver can retrieve it.
- [N-U46-531] The order registers this format as an additional builder next to those provided by purchase.
- [N-U46-532] An imported file is recognised as this format when its customisation identifier equals the Peppol order transaction identifier.
- [N-U46-533] The decoder for this format is registered with priority 20 and is chosen only when the file was detected as this format.
- [N-U46-534] Import problems are logged as a to-do activity assigned to the importing user on the order, with the message listing what could not be imported.
- [N-U46-535] Lines created from additional values are put at sequence zero so they appear above the real order lines.
- [N-U46-536] Export builds the document tree and serialises it as UTF-8 with an XML declaration.
- [N-U46-537] The document is composed of header, buyer, seller, delivery, payment terms, lines, allowances or charges, tax totals and monetary totals sections, in that order.
- [N-U46-538] Only real order lines are exported; section and note lines are skipped.
- [N-U46-540] Tax details are rounded globally using six digits before being written, in both document and company currency.
- [N-U46-541] For each line the vendor's price-list entry for the product, matching the variant or its template and having a vendor product code or name, supplies the vendor's item name and code.
- [N-U46-542] The buyer is the company's commercial partner and the seller is the order's vendor.
- [N-U46-543] The delivery party is the order's delivery address if set, else the company's first delivery-type child contact, else the company itself.
- [N-U46-544] Amounts are exported in the order currency, not the company currency, and fixed taxes are exported as allowances or charges on lines rather than as taxes.
- [N-U46-545] The header carries the Peppol ordering customisation and profile identifiers, the order name as identifier, the creation date as issue date and order type code 105.
- [N-U46-546] The order note is exported as plain text when present.
- [N-U46-547] The vendor reference is exported as a quotation document reference.
- [N-U46-548] The delivery section drops the actual delivery date and the delivery location.
- [N-U46-549] Payment terms appear as a note with the term's name, only when the order has terms.
- [N-U46-550] Early payment discounts are expressed as allowances or charges at document level.
- [N-U46-551] The legal line-extension total is the sum of the exported line extension amounts.
- [N-U46-552] The monetary total node contains line extension, tax-exclusive, tax-inclusive, allowance or charge, payable rounding and prepaid amounts.
- [N-U46-553] A vendor product name overrides the item name, and a vendor product code is added as the seller's item identification.
- [N-U46-554] Line discount nodes drop the reason, multiplier factor and base amount.
- [N-U46-555] Import resolves the vendor from the seller party of the file and sets it on the order only when a partner is found.
- [N-U46-556] The file's identifier becomes the order's vendor reference and the originator document reference becomes its source document.
- [N-U46-557] The delivery party resolves to the order's delivery address when found.
- [N-U46-558] Deferral dates, which belong to invoice lines, are removed from imported line values.
- [N-U46-560] Document-level allowances and charges are added as extra order lines.
- [N-U46-561] Imported line quantity is renamed to the purchase line's quantity field.
- [N-U46-564] The purchase order is a document with sharing, product catalog, discussion, activity and electronic document import behaviours, ordered by urgency then newest first.
- [N-U46-565] Orders can be found by their reference or by the vendor reference.
- [N-U46-566] Order totals ignore section and note lines and are computed with the shared tax engine, rounded per company rounding method.
- [N-U46-567] Each order stores untaxed, tax and total amounts in the order currency plus the total in the company currency.
- [N-U46-569] A confirmed order is Waiting Bills if any real line has a non-zero quantity still to bill, measured at the unit precision.
- [N-U46-570] A confirmed order is Fully Billed when nothing remains to bill and at least one bill is linked.
- [N-U46-571] The bills of an order are derived from the bill lines linked to its order lines; the bill count is their number.
- [N-U46-572] A new order starts with the placeholder reference New, which is not copied on duplication.
- [N-U46-573] The order date field means the deadline by which a quotation should be confirmed; it defaults to now and is required.
- [N-U46-574] The confirmation date is read-only and is not copied.
- [N-U46-576] An order has five states: RFQ, RFQ Sent, To Approve, Purchase Order and Cancelled, defaulting to RFQ, tracked and read-only to direct editing.
- [N-U46-577] A separate locked flag, tracked and not copied, marks an order as unmodifiable.
- [N-U46-579] A tracked acknowledged flag records that the vendor confirmed receipt of the order.
- [N-U46-581] Expected arrival is stored, editable, and by default equals the earliest planned date over the real lines, or empty if none.
- [N-U46-582] The calendar start date is the confirmation date for confirmed orders and the order date otherwise.
- [N-U46-583] The currency rate is the company-to-order currency rate at the order deadline date, stored on the order.
- [N-U46-584] Order currency is required, stored, precomputed and editable.
- [N-U46-585] The buyer defaults to the creating user and is tracked and company-checked.
- [N-U46-586] The company defaults to the current company and is required.
- [N-U46-589] The portal link of an order points to the vendor portal purchase page.
- [N-U46-592] When the order currency differs from the company currency, the tax summary adds the total in company currency in brackets.
- [N-U46-593] The tax country is the fiscal position's country when it has a foreign tax number, else the company fiscal country.
- [N-U46-594] A comparison indicator shows when the same product appears on confirmed orders other than the current one.
- [N-U46-595] Purchase warnings are shown only to users of the warning group; they combine vendor, parent vendor and line product messages without duplicates.
- [N-U46-596] Duplicate detection applies only to draft RFQs.
- [N-U46-597] An order is a possible duplicate of a non-cancelled order of the same company and vendor whose name equals its source or whose vendor reference matches; orders without vendor reference are skipped.
- [N-U46-598] Changing the expected arrival on the form pushes that date to every real line, but line-driven changes do not loop back.
- [N-U46-599] The late filter supports only equals and not equals.
- [N-U46-600] An order is late when confirmed, planned date is not in the future and at least one line has received less than ordered.
- [N-U46-601] The reference is taken from the order sequence in the order company, using the deadline date, falling back to a slash.
- [N-U46-602] Only cancelled orders can be deleted.
- [N-U46-603] Duplicating an order recomputes each line's planned date from the vendor lead time and drops any default product from the context.
- [N-U46-604] Choosing a vendor sets the fiscal position, the vendor payment terms and, when the vendor has a default buyer, the buyer; clearing the vendor clears the fiscal position.
- [N-U46-605] Order currency is the vendor's purchase currency when set, otherwise the company currency.
- [N-U46-606] Changing fiscal position or company recomputes the taxes on all lines.
- [N-U46-607] Sending a message with the send marker moves draft RFQs to RFQ Sent and notifies the author.
- [N-U46-608] The portal recipient's view button reads View Quotation for RFQs and View Order otherwise, and links to the order confirmation page.
- [N-U46-609] Notification subtitle shows the due date for RFQs and the total amount for confirmed orders, so no price is shown in RFQ mails.
- [N-U46-611] The send action opens an email composer prefilled with the RFQ template if the send rfq flag is in context, otherwise with the confirmed order template.
- [N-U46-612] The composer's description is Request for Quotation for draft or sent and Purchase Order otherwise.
- [N-U46-613] The acknowledge action sets the flag with no further checks.
- [N-U46-614] The comparison action shows the purchase history for the products of the order.
- [N-U46-615] Printing a quotation moves draft orders to RFQ Sent.
- [N-U46-619] Confirmation affects only RFQ and RFQ Sent orders; others are skipped silently.
- [N-U46-621] Confirmation validates the analytic distribution of the lines before proceeding.
- [N-U46-622] Confirmation registers the vendor on the price list of each product it was not yet listed on.
- [N-U46-623] After checks, confirmation approves directly if allowed, else moves the order to To Approve.
- [N-U46-628] A new vendor price-list entry is created with minimum quantity one, the line price, order currency, line discount, zero lead time and a sequence after existing ones.
- [N-U46-629] A contact is never added as vendor; the parent company is used instead.
- [N-U46-630] The vendor is added only if the product has not more than ten vendors already, to avoid clutter on generic products.
- [N-U46-631] The price is converted to the product's own unit before being stored on the vendor entry.
- [N-U46-632] The vendor entry is written with elevated rights so purchase users without product rights can still confirm.
- [N-U46-633] A new entry created for the parent company keeps the vendor product name, code and unit of the selected entry.
- [N-U46-634] Bill matching lists lines for the vendor or its commercial partner, in accessible companies, linked to this order or to none.
- [N-U46-635] Down payments are grouped under a section line titled Down Payments with zero quantity, placed after the last line.
- [N-U46-636] An existing down payment section is reused; otherwise one is created.
- [N-U46-637] Down payment lines are linked rather than concatenated, to avoid recomputing all lines.
- [N-U46-638] Bill creation keeps a section or subsection line only if a real line follows it, using only the last pending section.
- [N-U46-639] Orders selected together are grouped by company, vendor and currency into one bill each; origins are joined with commas.
- [N-U46-640] Bills are created as vendor bills in the order company.
- [N-U46-641] A created bill with a negative rounded total is converted to a vendor credit note.
- [N-U46-642] Uploading a bill file is allowed only when exactly one bill results; attachments are then extracted into the bill, posted in chatter and reassigned to it.
- [N-U46-643] Merging requires at least two orders among RFQ and RFQ Sent and fails if no group of identical vendor, currency, destination, dropship address and agreement has two or more.
- [N-U46-644] Merging keeps the RFQ with the earliest deadline and moves other RFQ lines into it.
- [N-U46-645] A line is combined with an existing one only when product, unit, analytic distribution and discount are equal and planned dates are within 24 hours; otherwise it is moved as is.
- [N-U46-646] If several matching lines already exist in the target, they are first collapsed into the first one by summing quantities.
- [N-U46-647] Source documents and vendor references of merged RFQs are concatenated onto the surviving RFQ.
- [N-U46-648] Merged RFQs are cancelled after a note is posted on both sides, and a hook allows other modules to post-process.
- [N-U46-649] The base grouping key for merging is vendor, currency and dropship address; other modules extend it.
- [N-U46-650] The bill takes the first bank account of the vendor's commercial partner that is company-neutral or of the order company.
- [N-U46-651] Bill header copies note, currency, vendor, fiscal position, payment terms and order name as origin.
- [N-U46-652] Viewing bills opens a list for several, the form for one and closes the window if none.
- [N-U46-653] The dashboard is limited to internal users and requires read access to orders.
- [N-U46-654] Dashboard counts: draft, sent, late quotations whose deadline has passed, not-acknowledged confirmed orders and late receipts, each global and for the current buyer, with an urgent subset.
- [N-U46-656] Average days to order is the mean time between creation and confirmation over confirmed orders created in the last three months.
- [N-U46-660] Automated reminders are posted as comments on the order using the reminder template and responsible signature layout.
- [N-U46-661] A preview sends a sample reminder only to the acting user's own email and reports a toast.
- [N-U46-662] The single reminder variant opens an email composer instead of sending directly, and returns after the first matching order.
- [N-U46-663] The product catalog shows only products allowed for purchase.
- [N-U46-664] The catalog opens prefiltered by the order's vendor name.
- [N-U46-665] Catalog price defaults to the product cost; if a vendor entry applies it uses the discounted vendor price converted to order currency and unit, and shows minimum quantity.
- [N-U46-666] Legacy confirm links for reminder, reception and decline all resolve to the portal acknowledge link.
- [N-U46-668] A user may approve an order if the company uses one-step validation, or two-step validation and the order total is below the company threshold converted to the order currency at the order date, or the user is a purchase manager.
- [N-U46-670] Purchase managers can always approve regardless of amount.
- [N-U46-671] Localised dates use the buyer's time zone, else the company's, else UTC.
- [N-U46-672] A vendor date change creates, or appends to an existing, warning activity for the buyer listing product, old date and new date.
- [N-U46-673] After the activity, each line date is updated.
- [N-U46-674] Catalog quantity zero deletes the line for RFQs but only zeroes the quantity for confirmed orders; a positive quantity on a missing product creates a line.
- [N-U46-675] A catalog-added line takes the vendor entry's price (converted) and discount.
- [N-U46-676] An order is read-only for catalog purposes only when cancelled.
- [N-U46-677] A spreadsheet import template for RFQs is provided.
- [N-U46-678] The base order exposes no electronic document builders; extension modules add them.
- [N-U46-679] Creating orders from attachments fails if none is given, and sets the current user's partner as default vendor on created records.
- [N-U46-680] Order lines are sorted by order, sequence and identifier and carry analytic distribution behaviour.
- [N-U46-681] Quantity is required at product unit precision; a total quantity is stored separately.
- [N-U46-682] A line's expected arrival defaults to the order date plus the vendor lead time, else the order date.
- [N-U46-684] Lines are deleted with their order and are required to belong to one.
- [N-U46-685] A database rule requires real lines to have product, unit and planned date unless they are down payments.
- [N-U46-686] A database rule requires section and note lines to have no product, zero price, zero quantity, no unit and no date.
- [N-U46-687] Lines can be a section, a subsection or a note.
- [N-U46-688] Line subtotal and total come from the shared tax engine in order currency; tax is the difference.
- [N-U46-689] The tax computation uses the order's stored currency rate, vendor, quantity, taxes and line description.
- [N-U46-690] Default taxes are the product's vendor taxes limited to the line company and mapped through the order's fiscal position.
- [N-U46-691] Discounted unit price is price multiplied by one minus discount percent.
- [N-U46-692] Price per product unit is the line price converted to the product's base unit; empty for sections and down payments.
- [N-U46-693] Quantity to bill is zero unless the order is confirmed.
- [N-U46-694] If the product's billing policy is on ordered quantities, to-bill equals ordered minus billed; otherwise received minus billed.
- [N-U46-695] Billed quantity counts bill lines of all non-cancelled bills, drafts included, converted to the line unit.
- [N-U46-696] Vendor credit note quantities are subtracted from the billed quantity.
- [N-U46-697] For accrual reporting at a past date, only bills dated on or before it are counted for billed and received quantities.
- [N-U46-698] A product warning is shown on lines only to users in the warning group.
- [N-U46-699] Without stock integration, goods and services have manual received quantity; other products have none.
- [N-U46-700] For manual lines, received quantity equals the manually entered quantity; otherwise zero.
- [N-U46-701] Writing received quantity on a manual line stores it as manual quantity; on other lines the manual quantity is reset.
- [N-U46-702] The vendor price entry applied to a line is chosen from the product's vendor list by vendor, absolute quantity, order date and unit.
- [N-U46-703] Amount to bill at a date applies the same ordered-versus-received policy and multiplies by the gross unit price in product unit.
- [N-U46-704] Creating a section or note line blanks product, price, quantity, unit and date.
- [N-U46-705] A technical copy of the entered price is kept so later automatic repricing can tell manual prices from computed ones.
- [N-U46-706] Adding a product line to a confirmed order posts a note on the order.
- [N-U46-708] Changing the quantity of a line on a confirmed order posts an internal note on the order.
- [N-U46-709] Writing received quantity triggers a tracking hook for extensions.
- [N-U46-711] Planned date is order date plus the vendor's lead time days, falling back to now when the order has no date.
- [N-U46-712] Analytic distribution is defaulted from distribution models matching product, product category, vendor, vendor tags and company, keeping the previous value if none match.
- [N-U46-713] When the product changes and a source order is given with a quantity, only taxes are recomputed.
- [N-U46-714] Changing the product resets price and quantity, applies the product's own unit, description and taxes, then suggests a quantity.
- [N-U46-715] Allowed units are the product unit, its additional units and the units on its vendor price entries.
- [N-U46-716] Automatic repricing and redescription are skipped when the line has no product or company, already has bill lines, or the price was manually changed.
- [N-U46-717] The description is regenerated only when empty or equal to a default description, so custom descriptions are preserved.
- [N-U46-718] If no vendor entry matches and the vendor has none for the product, an already priced line keeps its manual price; otherwise the product cost is used.
- [N-U46-719] The fallback cost is converted to the line unit, adjusted for tax inclusion and converted from the product cost currency to the order currency at the order date.
- [N-U46-720] When a vendor entry applies, the line price is its price adjusted for tax inclusion, converted to order currency at the order date and to the line unit, and the entry's discount is applied.
- [N-U46-721] Whenever the price is set automatically, a technical copy is set too.
- [N-U46-722] Total quantity is the ordered quantity converted to the product's base unit.
- [N-U46-723] The gross unit price for accrual applies discount, then taxes that are not recoverable (the tax-void total) per unit, then converts to the product unit.
- [N-U46-724] Section hierarchy is derived from line order: subsections belong to the last section and ordinary lines to the last subsection or section.
- [N-U46-725] The suggested quantity is the smallest minimum quantity among the vendor's valid dated entries, else one.
- [N-U46-726] Catalog data for a product spread over several lines sums their quantities in the product unit and is read-only.
- [N-U46-727] A line description is the product name, then its purchase description, then non-variant attribute values, one per line.
- [N-U46-728] A bill line takes the quantity to bill, negated for credit notes, with the line discount, taxes, down payment flag and a link back to the order line.
- [N-U46-729] The bill line price is converted from order currency to bill currency at the bill date without rounding.
- [N-U46-730] A down payment line reuses the account of its first existing bill line.
- [N-U46-731] When a line is created with order and product but without name, price, quantity, unit, taxes or date, the missing values are derived as the form would.
- [N-U46-732] A line created by replenishment selects the vendor entry using the later of the order date and today.
- [N-U46-734] Without a vendor entry the replenishment-created line has price zero, discount zero and the vendor's language description.
- [N-U46-735] A helper converts a date to noon in the buyer's time zone expressed in UTC.
- [N-U46-736] Past-date accrual calculation applies only when the accrual date is in the past.
- [N-U46-737] Received-quantity change notes are suppressed when values are computed for an accrual entry.
- [N-U46-738] A note is posted on a confirmed order when a line's received quantity changes.
- [N-U46-739] Analytic distribution validation uses the purchase order business domain, product and company and skips sections and notes.
- [N-U46-740] Merging two lines sums quantities and keeps the lower unit price.
- [N-U46-741] Vendor selection for a line passes the order and forces the line unit.
- [N-U46-742] For an ordinary line under a subsection, the owning section is the subsection's parent.
- [N-U46-743] Matching a bill total to purchase order amounts allows a tolerance of two hundredths of a currency unit.
- [N-U46-744] A vendor bill form offers non-stored helper fields to auto-complete from a previous bill, credit note or purchase order.
- [N-U46-745] Picking a purchase order on a bill loads its header values and the lines not yet linked to the bill, then clears the helper
- [N-U46-746] The bill keeps its currency if it already has product lines; otherwise the order currency is used.
- [N-U46-747] The bill origin becomes the comma-joined names of the orders of its linked lines.
- [N-U46-748] The bill company is aligned to the order company, which only changes it when the order belongs to a child company.
- [N-U46-749] Changing the vendor on a vendor bill or credit note switches currency to the vendor's purchase currency and picks a purchase journal in that currency if the journal was not fixed by context.
- [N-U46-750] A bill is matched to purchase only when every product line is linked to an order line.
- [N-U46-751] The count of source orders is the number of distinct orders on its lines, and a single order's name is shown only when exactly one.
- [N-U46-752] Purchase warnings on a bill appear only for vendor bills of users in the warning group, combining vendor, parent and product messages.
- [N-U46-753] Purchase matching from a bill lists unmatched lines of the vendor in accessible companies and the bill's company tree.
- [N-U46-754] Viewing source orders opens a list for several, the form for one and closes the window if none.
- [N-U46-755] A newly created bill linked to orders gets a chatter note naming them, except for reversals.
- [N-U46-756] When a write adds new source orders to a bill, a note names the added orders.
- [N-U46-757] Order lines are added to a bill as virtual lines built from order line values for that bill.
- [N-U46-758] Finding order lines adding up to a bill total is a subset-sum search that returns nothing if no or more than one subset fits within tolerance.
- [N-U46-759] The subset search aborts when a time limit is exceeded, logs a warning and returns no match.
- [N-U46-760] Line matching considers bill lines and order lines sorted by price and quantity descending, and aborts the search on timeout with no results.
- [N-U46-761] An order line is a candidate for a bill line when unit prices are equal and the bill quantity does not exceed the order line's remaining unbilled quantity.
- [N-U46-762] Among candidates, the one whose description is most similar to the bill line's is chosen, and each order line is matched only once.
- [N-U46-765] Automated matching first looks for orders whose reference equals a reference found on the bill, then for orders whose vendor reference equals one, and only when both a reference and a total are known.
- [N-U46-766] The remaining amount of an order line is its total times the unbilled fraction of its quantity; lines with zero quantity are ignored.
- [N-U46-767] A total match means the remaining amounts of all referenced orders sum to the bill total within tolerance.
- [N-U46-768] For scanned bills, a subset of lines matching the total is used; otherwise all lines of the referenced orders are returned on reference alone.
- [N-U46-769] For electronic bills, individual bill lines are matched to order lines by price and quantity.
- [N-U46-770] As a last resort, a single order of the vendor tree with a total within tolerance of the bill total is matched.
- [N-U46-771] The default time limit for matching is ten seconds.
- [N-U46-772] For total and reference matches the bill lines are replaced by the order lines.
- [N-U46-773] For subset total matches existing bill lines are kept and unmatched order lines are added with quantity zero.
- [N-U46-774] For subset matches, order lines are loaded but quantity and taxes are taken from the electronic bill lines, then the original matched bill lines are deleted.
- [N-U46-775] Bill lines left unlinked to any order are put under a section titled From Electronic Document.
- [N-U46-776] If no line ends up linked to an order the bill's origin is cleared.
- [N-U46-778] When bill lines are copied as business data, as for reversals, the purchase link is carried over.
- [N-U46-779] Analytic distribution of a bill line is merged with that of its linked order line.
- [N-U46-780] Bill lines can be converted to order line values carrying product, quantity, unit, price and discount.
- [N-U46-781] Bill matching is a read-oriented database view combining order lines and bill lines in one list, with editable quantity and price.
- [N-U46-782] Editing the price in the matching list writes to the bill line if the row is a bill line, otherwise to the order line.
- [N-U46-783] Editing quantity on an order line row restores the previous price afterwards, because changing quantity would otherwise reprice.
- [N-U46-784] Order-side rows are lines of confirmed orders not fully billed or with a non-zero quantity to bill.
- [N-U46-786] Bill-side rows are product lines of draft or posted vendor bills and credit notes not yet linked to an order line.
- [N-U46-787] The view is the union of order-side and bill-side rows, bill rows having negated identifiers.
- [N-U46-788] A bill created from order lines uses their common currency, else the common company currency, else the current company currency.
- [N-U46-789] The match action requires at least one order line; with no bill lines selected it creates a draft vendor bill from the order lines.
- [N-U46-790] Selected lines are paired by product in order; extra bill lines of a product are linked to the last order line of that product.
- [N-U46-791] When the selection belongs to one bill, unmatched selected bill lines are deleted and unmatched order lines are added to that bill.
- [N-U46-792] Adding bill lines to an order requires bill lines of a single vendor and at most one order.
- [N-U46-794] The wizard adds lines to the chosen order or creates a new order for the vendor, then confirms it immediately and links each bill line to its new order line.
- [N-U46-795] The down payment action creates order lines of quantity zero flagged as down payments, priced from the bill line converted to order currency, and links the bill lines to them.
- [N-U46-796] If no order is chosen a new empty order for the vendor is created.
- [N-U46-798] Portal lists sort by newest, name or total and may be filtered by creation date range.
- [N-U46-799] The portal remembers up to one hundred listed order identifiers in the session for next and previous navigation.
- [N-U46-802] The order list route offers filters All, Purchase Order and Cancelled, defaulting to All, which excludes drafts and RFQs.
- [N-U46-803] A single order page is reachable by public visitors with a valid access token, or by users with rights; on failure the visitor is redirected to the portal home.
- [N-U46-806] A public JSON endpoint lets a token holder update expected dates of order lines; invalid line identifiers redirect, invalid dates are skipped.
- [N-U46-807] A submitted date is converted to noon in the buyer's time zone in UTC before saving.
- [N-U46-808] Portal date changes are applied with elevated rights and notify the buyer with a date-updated activity.
- [N-U46-809] A download route exports the order as an electronic file using the first available builder, and redirects home when none is installed.
- [N-U46-810] The electronic file is delivered as an XML attachment named by the builder.
- [N-U46-812] The purchased quantity statistic sums confirmed order lines approved in the last year.
- [N-U46-813] The product purchase history action lists only confirmed order lines, including archived variants for templates.
- [N-U46-814] A product-in-order flag is computed from the order identifier in context and is searchable only with the in operator.
- [N-U46-816] The unit-of-measure change warning also fires when any order line uses the product.
- [N-U46-817] Choosing a vendor on a price line defaults its currency to the vendor's purchase currency or the company currency.
- [N-U46-818] Vendor price filtering uses the order's company when an order is given in the parameters.
- [N-U46-819] The purchase order count on a partner is zero unless the user belongs to the purchase user group.
- [N-U46-820] The count rolls up orders of all child contacts to each ancestor.
- [N-U46-821] Supplier currency, receipt reminder flag and reminder lead days are stored per company on the partner.
- [N-U46-822] A partner may carry a warning message shown on orders.
- [N-U46-824] Enabling grid entry forces product variants on, and disabling variants switches grid entry off.
- [N-U46-827] Each company holds a post-confirmation modification policy, defaulting to editable.
- [N-U46-828] Each company holds an approval policy, defaulting to one step.
- [N-U46-829] The default minimum amount requiring a second approval is five thousand in company currency.
- [N-U46-830] A tax used on any order line is marked as used, which protects it from certain edits.
- [N-U46-831] An analytic account counts orders reached through order lines, bill lines and analytic lines using the plan column.
- [N-U46-832] The analytic account order action opens a form for a single order and a list otherwise.
- [N-U46-833] Analytic plan applicability may be scoped to the purchase order business domain.
- [N-U46-835] Without any builder the PDF is returned unchanged.
- [N-U46-836] Two purchase groups exist: user, implying internal user, and administrator, implying user, with the root and admin users seeded into administrator.
- [N-U46-837] All internal users imply the receipt reminder group on install.
- [N-U46-838] Orders, order lines and the purchase report are limited to the user's allowed companies, and the union view also admits records without a company.
- [N-U46-839] Portal users see orders and lines of their commercial partner hierarchy; the order rule grants write and delete rights at rule level though the access list gives portal read only.
- [N-U46-840] Purchase users reach only vendor bills, refunds and receipts among journal entries and their lines.
- [N-U46-841] Purchase users and administrators have full rights on orders and lines; accounting invoicing users may read and write but not create or delete; accounting read-only users may only read; portal users may read.
- [N-U46-842] Purchase users have full rights on journal entries and create rights on journal items without delete, administrators have full rights on items.
- [N-U46-843] Purchase users read partners, products, taxes and journals; administrators can additionally create and edit partners and fully manage vendor price lines and price list items.
- [N-U46-844] A daily scheduled job named Purchase reminder runs as the root user and sends receipt reminders.
- [N-U46-845] The purchase analysis is a read-only database view over order lines without display type rows, grouped per order, product, unit, price and planned date.
- [N-U46-846] A source comment states the reports are not multi-currency; amounts are converted to the company rate through a simple currency table of the selected companies.
- [N-U46-847] Days to confirm is the age between approval and order date; days to receive is the age between line planned date and order date.
- [N-U46-848] Quantity to be billed is ordered minus billed for ordered-quantity products, otherwise received minus billed.
- [N-U46-849] Average cost is aggregated as a quantity-weighted average when grouped.
- [N-U46-850] Section and note lines are excluded from the analysis; all order states including draft and cancelled are included.
- [N-U46-852] The union display label shows zero amount for orders with nothing to bill.

### STATE

- [N-U46-568] Billing status is Nothing to Bill unless the order is confirmed.
- [N-U46-580] Billing status has three values: Nothing to Bill, Waiting Bills and Fully Billed.
- [N-U46-610] Tracked state changes emit different message subtypes: approved when moving from To Approve to Purchase Order, confirmed for direct confirmation or entering To Approve, and sent for RFQ Sent.
- [N-U46-616] Approval silently skips orders for which approval is not currently allowed, sets state to Purchase Order and stamps the confirmation date.
- [N-U46-618] Set to draft writes the draft state without any state or lock check in this method.
- [N-U46-627] Lock and unlock simply toggle the flag with no state check.
- [N-U46-764] Only confirmed orders of the bill's company whose billing status is Waiting Bills or Nothing to Bill are considered for automated matching.
- [N-U46-797] Portal home counters show RFQs in Sent state and orders in Purchase or Cancelled state, only for users with read access to orders.
- [N-U46-801] The RFQ list route requires a logged-in user and lists only RFQs in Sent state.
- [N-U46-851] A union view lists posted vendor bills and refunds together with confirmed orders whose invoice status is to invoice or nothing to bill.

### OPTIONALITY

- [N-U46-485] When an alternative quotation is created from a purchase order, each copied line keeps its link to the originating sales order line.
- [N-U46-492] An agreement may also carry an optional warehouse of the same company.
- [N-U46-502] A purchase order shows how many repair orders it originates from, visible only to stock users.
- [N-U46-509] A purchase order has a print-variant-grids flag, on by default, that controls whether grids of configurable products appear on the printed order.
- [N-U46-518] Setting a cell to zero removes the lines of that variant only while the order is draft or sent; in other states their quantity is set to zero instead of deleting them.
- [N-U46-524] The printed order includes a grid only for configurable templates that appear on more than one line.
- [N-U46-526] A purchase line exposes its product template, restricted to purchasable templates, and whether it is configurable.
- [N-U46-527] The print-grid option is visible only in technical mode.
- [N-U46-575] An optional delivery address allows direct delivery from vendor to customer; if empty delivery is to the own company.
- [N-U46-578] Whether confirmed orders lock automatically is a company setting reflected on the order.
- [N-U46-587] Receipt reminder flag and days-before value default from the vendor's company-specific settings and remain editable on the order.
- [N-U46-590] The order expected arrival is the minimum of planned dates of real lines.
- [N-U46-591] The display name is the reference, with the vendor reference in brackets and optionally the total amount when requested by context.
- [N-U46-617] After approval, orders of companies configured to lock are marked locked.
- [N-U46-655] The dashboard filters on a done state that does not exist in the order's state list, so only confirmed orders are matched.
- [N-U46-657] Reminder mails are sent only when the acting user belongs to the reminder group.
- [N-U46-658] A reminder is sent when today equals the expected arrival minus the configured days before receipt.
- [N-U46-659] Orders to remind are confirmed, not acknowledged, with reminders enabled and not made only of services.
- [N-U46-733] Replenishment-created lines read optional procurement values from context, including a flag forcing the requested unit.
- [N-U46-763] Linking orders to a bill runs inside a savepoint, optionally clears existing lines, adds a section per order titled From plus the order name and loads each order's lines.
- [N-U46-777] Bill lines hold an optional link to an order line, which is emptied if the order line is deleted and is not copied on bill duplication by default.
- [N-U46-804] The report choice uses a quotation report when state is a nonexistent value rfq or sent, otherwise the order report; draft orders therefore receive the order report.
- [N-U46-811] The bill control policy defaults to ordered quantities for services and to the configured default (received quantities) for other products.
- [N-U46-823] Settings expose lock-on-confirm, two-step approval with a minimum amount, warnings, three-way matching, agreements and grid entry.
- [N-U46-825] The approval and lock checkboxes are translated to company-level selections when settings are saved.
- [N-U46-826] The receipt reminder option is enabled by default.
- [N-U46-834] When a single order is printed as quotation or order and builders exist, the electronic file from each builder is embedded in the PDF.
- [N-U46-862] The restored database holds 35 access rows owned by the purchase module, matching the 35 data rows of the access file, and 8 record rules all active.
- [N-U46-863] In the restored database the purchase reminder schedule is active, daily, with one order sequence prefixed P, five digits.
- [N-U46-864] The single company in the restored database has the modification policy set to locked after confirmation, two-step approval and a threshold of five thousand, which differ from the source defaults of editable and one step.
- [N-U46-865] The restored database contains the four purchase groups: user, administrator, warnings and reminder.
- [N-U46-866] The portal order and order line rules exist and are active in the restored database.

### DEPENDENCY

- [N-U46-486] The bridge is installed automatically when purchase agreements and sale-driven purchasing are both present; it has no data files or views.
- [N-U46-530] It depends on purchase and the shared electronic invoicing library and is installed automatically.

### CONSTRAINT

- [N-U46-519] Changing the quantity of a variant that appears on several lines is refused with a validation error.
- [N-U46-539] Item net prices are turned positive to satisfy the European rule that a net price cannot be negative.
- [N-U46-559] A line whose product cannot be found is still imported by name, with a log message naming it.
- [N-U46-562] Grouping or ungrouping invoice lines by tax is refused for an invoice with lines linked to a purchase order.
- [N-U46-588] A constraint forbids lines whose product belongs to a company that is not the order's company or one of its accessible branches, naming the offending products.
- [N-U46-620] Confirmation is refused when a real line, other than a down payment, lacks a product.
- [N-U46-624] Cancelling is refused for any locked order in the set.
- [N-U46-625] Cancelling is refused if any linked bill is neither cancelled nor draft.
- [N-U46-626] Cancelling does not check the current state, so an already cancelled order is rewritten without error.
- [N-U46-683] Only products allowed for purchase can be chosen, and a product cannot be deleted while used on a line.
- [N-U46-707] A line's type cannot be changed once created.
- [N-U46-710] Product lines of a confirmed order cannot be deleted; sections and notes can.
- [N-U46-793] The wizard refuses when no selected bill line has a product.
- [N-U46-815] Changing a product unit of measure is refused when order lines use another unit; otherwise existing lines are re-pointed to the new unit.

### RISK

- [N-U46-496] The order values are read from the first procurement only and assume a supplier key is always present; a procurement without a supplier key would fail, which was not executed.
- [N-U46-528] The dirty-cell payload is parsed from client-supplied JSON without validating that the cell attribute values belong to the chosen template; the product template's own variant creation is expected to enforce this but was not read.
- [N-U46-563] The purchase builder reuses a large set of invoice-side helpers in a shared library outside this unit; the exact output was not generated, so conformance to the published ordering rules is unverified.
- [N-U46-667] A separate compute for the company-currency total divides by the rate but the field is actually computed by the main amount compute, so this method appears unused; runtime check needed.
- [N-U46-669] The threshold conversion starts from the currency of the current environment company but passes the order company to the converter; for orders of another company this could mix currencies.
- [N-U46-785] Down payment lines with a billed quantity are also listed, and because the OR is not inside the confirmed-state condition they are listed regardless of order state; runtime check needed.
- [N-U46-800] The history key test uses a string, not a one-item tuple, so it is a substring test; it still yields the RFQ history for sent and the order history otherwise.
- [N-U46-805] Opening the page with the acknowledge flag sets the acknowledged marker through a read-style request; anyone holding the access link can do it.

### UNKNOWN

None recorded.

## Capability 10: External call interfaces

### WHAT

- [N-U46-887] Purpose inferred from the claims of this section: it exposes the external call interfaces that let outside programs read and write platform data.

### WHY

- [N-U46-888] Rationale inferred from the same claims: integrations need a stable authenticated way to call model operations remotely.

### BUSINESS RULE

- [N-U46-854] The legacy XML and JSON remote procedure endpoints are flagged deprecated with scheduled removal in a later major version, and each call logs a warning.
- [N-U46-855] Before dispatching, the request's database cursor is closed if a database is selected, so the service opens its own.
- [N-U46-856] A public no-auth read-only endpoint returns the server version and version info.
- [N-U46-857] The legacy JSON endpoint requires no session authentication, does not save a session and dispatches a service, method and arguments, relying on in-service authentication.
- [N-U46-858] The first XML endpoint accepts POST only, has CSRF disabled and no session saving, and reports faults with string fault codes for backward compatibility.
- [N-U46-860] Control characters other than tab, newline and carriage return are stripped from strings since XML 1.0 forbids them.
- [N-U46-861] The current JSON interface is a POST to a model and method path, authenticated by a bearer key and not saving a session.

### STATE

None recorded.

### OPTIONALITY

None recorded.

### DEPENDENCY

- [N-U46-853] The RPC module depends only on the base and is installed automatically, providing the standard remote model access endpoints.

### CONSTRAINT

- [N-U46-859] Fault codes: application error one, warning two, access denied three, access error four; these must stay in sync with clients.

### RISK

None recorded.

### UNKNOWN

None recorded.

