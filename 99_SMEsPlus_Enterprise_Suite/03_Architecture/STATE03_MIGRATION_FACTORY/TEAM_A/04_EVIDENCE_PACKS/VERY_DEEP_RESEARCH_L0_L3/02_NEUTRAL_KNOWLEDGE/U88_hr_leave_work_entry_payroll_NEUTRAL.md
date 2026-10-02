# U88 Neutral Knowledge — HR Leave Work Entry Payroll
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U88-001 | A time off request has five possible statuses: To Approve (the entry state), Refused, Second Approval, Approved, and Cancelled. There is no separate Draft status; all new requests begin in the To Approve state. |
| NR-U88-002 | The To Approve status is the default state for every newly created time off request; this is also the state to which approvers can return a previously approved request. |
| NR-U88-003 | The Second Approval status is an intermediate state used only when the leave type requires dual authorisation; a first approver advances the request to this state before a second approver grants final approval. |
| NR-U88-004 | When a time off request reaches the Approved status, the system immediately creates a resource calendar absence entry for the employee, marking the dates as off-work in the scheduling system. |
| NR-U88-005 | The Cancelled status removes the associated resource calendar absence entry, making those dates available again in the employee work schedule. |
| NR-U88-006 | Approval routing distinguishes single-approval and dual-approval paths at the moment the approve action is triggered; single-approval cases go directly to Approved while dual-approval cases advance to Second Approval first. |
| NR-U88-007 | The final approval step validates the request, records the approving employee, and then triggers resource calendar leave and optional calendar event creation in a single chained call. |
| NR-U88-008 | Writing the Approved status occurs before creating any downstream records; this ensures the leave is marked valid before attendance and work records are adjusted. |
| NR-U88-009 | Approval calls the leave request validation method, which creates the resource calendar absence record and optionally schedules a calendar meeting for the relevant dates. |
| NR-U88-010 | The leave request validation routine creates a resource calendar absence record and, if the leave type is configured for it, creates a corresponding entry in the organisation calendar so colleagues can see the absence. |
| NR-U88-011 | Resource calendar absence creation is limited to leave requests that have an employee assigned; requests without an employee are skipped. |
| NR-U88-012 | Resource calendar absences are created in bulk from prepared value dictionaries, with the link back to the originating leave request stored in each absence record. |
| NR-U88-013 | Each resource calendar absence record carries a reference to the originating time off request, enabling the system to find and remove those absences when the leave is refused or cancelled. |
| NR-U88-014 | Refusing a leave requires the request to be in To Approve, Approved, or Second Approval status; refusal archives the associated calendar meeting but does not directly remove the resource calendar absence — that removal is handled by the write interceptor. |
| NR-U88-015 | Attempting to refuse a leave that is not in one of the three permitted states raises a user-facing error preventing the operation. |
| NR-U88-016 | When any write operation on a leave changes the status away from Approved, the system automatically identifies which previously approved leaves are affected and removes their resource calendar absences. |
| NR-U88-017 | Resource calendar absence removal is embedded in the general write handler so that any route that changes the status away from Approved — refuse, cancel, back-to-approval — consistently cleans up absence records. |
| NR-U88-018 | The absence removal method searches for all resource calendar absence records linked to the given time off requests and deletes them. |
| NR-U88-019 | Cancellation clean-up includes both archiving the calendar meeting and removing resource calendar absences; this same routine is invoked during record deletion. |
| NR-U88-020 | A leave type's approval mode is one of: no approval required, by a Time Off Officer, by the employee's own manager, or by both manager and officer in sequence. |
| NR-U88-021 | Leave types may require a pre-approved allocation before an employee can submit a request; this requirement is controlled by a Boolean flag on the leave type and defaults to True. |
| NR-U88-022 | Leave types are categorised as either an Absence or Worked Time; this category is used when computing how accrual plan periods are credited and is stored on the resource calendar absence record. |
| NR-U88-023 | Leave duration may be measured in full days, half-days, or hours depending on the leave type configuration; this setting governs how start and end datetimes are calculated from the employee's request. |
| NR-U88-024 | Time off allocations follow the same four-status approval workflow as leave requests: To Approve, Refused, Second Approval, and Approved. |
| NR-U88-025 | Allocations are either regular (a fixed number of days granted at once) or accrual-based (days accumulate over time according to a plan). |
| NR-U88-026 | An accrual allocation references an accrual plan that contains one or more milestones; each milestone specifies a rate and period for incrementally adding days to the allocation balance. |
| NR-U88-027 | An allocation's days-taken value is a computed field derived from the employee's consumed-leave data; it decreases the available balance as each approved leave request deducts from the allocation. |
| NR-U88-028 | The available balance on a leave type is the sum of all valid allocations minus all approved and requested leave; the approved-leave portion is subtracted when each leave request reaches the Approved status. |
| NR-U88-029 | A work entry record represents a single employee's time on a single working day; it stores the employee, the employee record version, the date, a duration in hours, the work entry type, and a status. |
| NR-U88-030 | Work entry statuses are: New (not yet reviewed), In Conflict (validation error detected), In Payslip (validated for payroll processing), and Cancelled. |
| NR-U88-031 | Unlike the leave request which uses a datetime range, each work entry covers exactly one calendar date; duration is expressed as a number of hours on that date. |
| NR-U88-032 | Validating a work entry first runs all error checks; only if no errors are found is the status promoted to In Payslip. |
| NR-U88-033 | The error-check sequence examines three independent conditions: whether a work entry type is missing, whether the total daily hours conflict, and whether a validated entry already exists for that employee and day. |
| NR-U88-034 | Conflict detection is performed by a database query that groups work entries by employee and date; any day where the total duration is zero or negative or exceeds 24 hours is flagged as conflicting. |
| NR-U88-035 | The conflict threshold is strict: a total daily duration greater than 24 hours or less than or equal to zero marks all entries for that employee-day as In Conflict. |
| NR-U88-036 | A work entry type marked as a time off type represents an absence; it is mutually exclusive with the working time flag on the same record. |
| NR-U88-037 | Each work entry type carries a payroll code; this code is referenced by salary rules in external payroll modules, so changing it can silently break computations in those modules. |
| NR-U88-038 | Work entry types carry a pay rate multiplier (defaulting to 1.0); a rate of 2.0 means the hours are counted at double the normal pay, enabling overtime or premium-rate configurations. |
| NR-U88-039 | Work entry generation for an employee is delegated to the employee's associated version records, which hold the contract and calendar information needed to produce the entries. |
| NR-U88-040 | A scheduled job runs regularly to generate missing work entries for the current and following month; it processes versions in batches of 100 and re-triggers itself if more remain. |
| NR-U88-041 | The scheduled job generates entries from the first day of the current month through the last day of the following month, providing roughly two months of forward coverage at all times. |
| NR-U88-042 | Work entry generation reads resource calendar absence records for the target period; validated time off requests produce these absence records, which then shape the attendance versus absence split in the generated work entries. |
| NR-U88-043 | The version-level work entry calculation reads calendar absences and splits the employee's theoretical attendance schedule into attendance segments and absence segments; each segment becomes one work entry record. |
| NR-U88-044 | The leaves-to-work-entry integration module adds a work entry type reference to each leave type, establishing the payroll category that will be used when a leave is converted into a work entry record. |
| NR-U88-045 | When a validated leave creates a resource calendar absence record, the integration module injects the corresponding work entry type identifier so that subsequent work entry generation produces correctly typed leave entries. |
| NR-U88-046 | On leave validation, the integration module first calls the standard resource calendar absence creation, then immediately creates work entry records for the leave period and reconciles any overlapping attendance entries. |
| NR-U88-047 | Creating work entries for a validated leave involves: generating leave-typed work entry values for the leave dates, then archiving any existing attendance work entries that fall entirely within the leave interval. |
| NR-U88-048 | Leave work entry creation is guarded: entries are only created if the leave period overlaps with dates that have already been generated for the employee's version; leaves outside the generated window are picked up by the next scheduled generation run. |
| NR-U88-049 | Refusing a leave (via the integration module) archives the associated leave work entries and regenerates attendance work entries for the same dates, effectively reversing the impact of the original approval. |
| NR-U88-050 | The regeneration on refusal sets leave work entries to inactive, then uses the employee version's work-value calculator to produce replacement attendance entries for each affected working day. |
| NR-U88-051 | The integration module adds a reference field on work entry records linking each leave-typed entry back to its originating time off request; this enables bidirectional navigation between the two records. |
| NR-U88-052 | Cancelling a leave work entry (setting it to the Cancelled status) automatically triggers a refusal of the linked time off request, keeping work entries and leave requests in a consistent state. |
| NR-U88-053 | The payroll module is not present in Odoo 19 Community Edition; it is an Enterprise-only feature. There are no payslip, salary rule, or payslip generation objects in Community. |
| NR-U88-054 | In Community 19, the In Payslip status on a work entry is the formal payroll boundary: it marks a day as finalised for payroll purposes even though no payslip generation occurs within Community; downstream payroll processing requires the Enterprise module. |
| NR-U88-055 | Work entry generation accepts a force flag; when enabled, all non-validated entries in the target period are nullified before new entries are created, allowing a full regeneration of the work schedule. |
| NR-U88-056 | If a validated work entry already exists for an employee on a given day, any new work entry created for that same employee-day combination is immediately marked as In Conflict, preventing double-counting for payroll. |
