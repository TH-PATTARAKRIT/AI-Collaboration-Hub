# U87 Neutral Knowledge — Project Timesheet Analytic Chain
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U87-001 | The analytic line record is the canonical store for all analytic entries including timesheets; it is defined in the analytic foundation module, not in the timesheet module. |
| NR-U87-002 | The analytic line model inherits a mixin that dynamically adds one relationship field per active analytic plan, allowing multi-dimensional cost allocation. |
| NR-U87-003 | Every analytic line requires a text description field. |
| NR-U87-004 | Every analytic line requires a date field, which is indexed for performance. |
| NR-U87-005 | Every analytic line carries a monetary amount field that defaults to zero. |
| NR-U87-006 | The quantity field on an analytic line stores a decimal number; in the context of timesheets this quantity represents hours worked. |
| NR-U87-007 | The primary analytic account linkage on an analytic line is a relationship to the analytic account model, coming from the plan mixin. |
| NR-U87-008 | The timesheet module extends the analytic line model by adding timesheet-specific fields; it does not define a separate table or model. |
| NR-U87-009 | A relationship to the task record is added to analytic lines by the timesheet module. |
| NR-U87-010 | A relationship to the project record is added to analytic lines by the timesheet module. |
| NR-U87-011 | A relationship to the employee record is added to analytic lines by the timesheet module. |
| NR-U87-012 | The milestone associated with a timesheet is exposed on the analytic line as a derived field from the task. |
| NR-U87-013 | When a timesheet line is created or updated, the system reads analytic account values from the linked project and injects them into the timesheet record automatically. |
| NR-U87-014 | For every configured analytic plan column, the account identifier is sourced from the project record and written to the timesheet line at persistence time. |
| NR-U87-015 | Cost recomputation on a timesheet is triggered whenever the quantity, the employee, or the analytic account changes. |
| NR-U87-016 | The hourly cost rate is retrieved via a dedicated method that can be overridden by other modules. |
| NR-U87-017 | The monetary amount stored on a timesheet line equals negative quantity multiplied by hourly cost, representing a cost (negative value on the analytic account). |
| NR-U87-018 | The base hourly cost method returns the employee's configured hourly cost, defaulting to zero if not set. |
| NR-U87-019 | The hourly cost on an employee is a monetary field defined in a dedicated hourly cost addon, secured behind the HR user group. |
| NR-U87-020 | The analytic plan model supports a hierarchy with parent and child plans; multiple root plans can coexist. |
| NR-U87-021 | One root plan is designated as the project plan via a system configuration parameter; all other root plans are supplementary. |
| NR-U87-022 | The project plan maps to the primary account column; each supplementary plan generates a dynamically named additional column. |
| NR-U87-023 | The project record holds a direct relationship to an analytic account with a set-null deletion policy. |
| NR-U87-024 | The analytic account model exposes a reverse relationship listing all projects linked to it. |
| NR-U87-025 | Enabling timesheets on a project without an analytic account raises a validation error, preventing the configuration from being saved. |
| NR-U87-026 | When a project is created with timesheets enabled and no analytic account provided, an analytic account is automatically created before any constraint check runs. |
| NR-U87-027 | The auto-creation of the analytic account on project creation happens before the parent create call to avoid the constraint error. |
| NR-U87-028 | When timesheets are later enabled on an existing project that lacks an analytic account, the account is created during the write operation. |
| NR-U87-029 | The allow timesheets flag on a project is a stored boolean computed from the presence of an analytic account, defaulting to true for new projects. |
| NR-U87-030 | For existing projects without an analytic account, the allow timesheets flag is computed as false. |
| NR-U87-031 | The project record provides a collection of all its associated timesheet lines as a reverse relationship. |
| NR-U87-032 | The analytic account balance, debit, and credit figures are computed by aggregating the amount field across all linked analytic lines. |
| NR-U87-033 | The project milestone model exists in the Community edition, defined in the project module. |
| NR-U87-034 | A milestone carries a boolean flag indicating whether it has been reached. |
| NR-U87-035 | The sale timesheet module defines a fixed set of invoice type classifications for timesheet lines: billed on timesheets, billed at fixed price, billed on milestones, billed manually, and non-billable. |
| NR-U87-036 | Each timesheet line carries a stored, computed invoice type classification field. |
| NR-U87-037 | A timesheet line optionally links to the invoice record that was generated from it. |
| NR-U87-038 | A timesheet line carries a stored relationship to the sale order line it contributes to for billing purposes; this field is computed but editable. |
| NR-U87-039 | The sale order line on a timesheet is determined from the task's sale line, the project's sale line, or the employee rate mapping, depending on the project pricing type. |
| NR-U87-040 | The logic resolving which sale order line a timesheet belongs to handles three pricing modes: per-task rate, per-project fixed rate, and per-employee rate. |
| NR-U87-041 | The project pricing type is a computed selection choosing between task rate, project rate, and employee rate. |
| NR-U87-042 | The pricing type is determined by the presence of employee mappings (employee rate), a project-level sale line (fixed rate), or neither (task rate). |
| NR-U87-043 | The sale timesheet module adds a timesheet delivery method to the sale order line, enabling quantity delivered to be calculated from timesheet hours. |
| NR-U87-044 | The timesheet delivery method is assigned to service products whose delivery tracking is set to timesheet. |
| NR-U87-045 | The sale order line exposes a collection of its associated timesheet entries as a reverse relationship, filtered to lines with a project reference. |
| NR-U87-046 | The invoice type classification on a timesheet depends on the product invoice policy and service type of the linked sale order line product. |
| NR-U87-047 | A timesheet with no sale order line is classified as non-billable, unless the project is configured for manual billing. |
| NR-U87-048 | For employee-rate projects, the hourly cost override returns the cost from the employee-to-sale-line mapping entry rather than the employee's default rate. |
| NR-U87-049 | Milestone-based billing in Community is supported through the milestone product service type; the milestone record and billing category both exist in Community. |
| NR-U87-050 | The timesheet create method in the timesheet module validates project and task references, resolves the company, populates analytic accounts from the project, and triggers cost computation after the record is saved. |
| NR-U87-051 | Timesheet analytic lines are created directly by the timesheet module's own create logic; no ORM trigger from the task model creates them. |
| NR-U87-052 | Analytic lines without a project or task reference are not treated as timesheets and bypass timesheet-specific validation and processing. |
| NR-U87-053 | The cost amount stored on the analytic line is converted from the employee's currency to the analytic account's currency at the time of writing. |
