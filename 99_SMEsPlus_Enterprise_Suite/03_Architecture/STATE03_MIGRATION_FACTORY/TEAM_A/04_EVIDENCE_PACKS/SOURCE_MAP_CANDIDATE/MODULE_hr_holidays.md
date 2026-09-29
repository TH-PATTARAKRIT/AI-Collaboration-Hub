# Source Map (candidate) — `hr_holidays`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_holidays` |
| Display name | Time Off |
| Manifest version | 1.6 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e91f5a076d268b83` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_holidays/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `calendar`, `resource`
- Direct dependents in 300-module list (5): `hr_holidays_attendance`, `hr_holidays_homeworking`, `hr_presence`, `hr_work_entry_holidays`, `project_timesheet_holidays`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (3): `l10n_fr_hr_holidays`, `l10n_in_hr_holidays`, `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Time Off / Allocate time off and follow leave requests
- Inventory of user-facing artifacts (counts): menu items 19, views 70, window actions 24, server actions 1, reports 1, mail templates 0, scheduled jobs 2, wizards 5, web routes 5
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (14): `hr.leave.generate.multi.wizard` (Generate time off for multiple employees); `hr.holidays.summary.employee` (HR Time Off Summary Report By Employee); `hr.leave.allocation.generate.multi.wizard` (Generate time off allocations for multiple employees); `hr.holidays.cancel.leave` (Cancel Time Off Wizard); `hr.leave` (Time Off); `hr.leave.accrual.plan` (Accrual Plan); `hr.leave.accrual.level` (Accrual Plan Level); `hr.leave.allocation` (Time Off Allocation); `hr.leave.type` (Time Off Type); `hr.leave.mandatory.day` (Mandatory Day); `hr.leave.report.calendar` (Time Off Calendar); `hr.leave.report` (Time Off Summary / Report); `hr.leave.employee.type.report` (Time Off Summary / Report); `report.hr_holidays.report_holidayssummary` (Holidays Summary Report)
- Objects extended from other modules (19): `hr.departure.wizard`, `hr.mixin`, `hr.version`, `mail.thread.main.attachment`, `mail.activity.mixin`, `hr.employee.public`, `mail.activity.type`, `mail.message.subtype`, `hr.department`, `resource.calendar.leaves`, `resource.calendar`, `resource.resource`, `res.company`, `hr.employee`, `mail.thread`, `calendar.event`, `res.users`, `res.partner`, `hr.manager.department.report`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.leave` ← Community: `hr_holidays_attendance`, `hr_work_entry_holidays`, `l10n_fr_hr_holidays`, `l10n_in_hr_holidays`, `project_timesheet_holidays`; open-license custom/third-party scanned: —
- `hr.leave.accrual.level` ← Community: `hr_holidays_attendance`; open-license custom/third-party scanned: —
- `hr.leave.allocation` ← Community: `hr_holidays_attendance`; open-license custom/third-party scanned: —
- `hr.leave.type` ← Community: `hr_holidays_attendance`, `hr_work_entry_holidays`, `l10n_in_hr_holidays`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `hr.departure.wizard`, `hr.mixin`, `hr.version`, `mail.thread.main.attachment`, `mail.activity.mixin`, `hr.employee.public`, `mail.activity.type`, `mail.message.subtype`, `hr.department`, `resource.calendar.leaves`, `resource.calendar`, `resource.resource`, `res.company`, `hr.employee`, `mail.thread`, `calendar.event`, `res.users`, `res.partner`, `hr.manager.department.report`

## 6. Actions / states / validation / automation / security
- State fields found: `hr.leave` → ['confirm', 'refuse', 'validate1', 'validate', 'cancel']; `hr.leave.allocation` → ['confirm', 'refuse', 'validate1', 'validate']; `hr.leave.report.calendar` → ['cancel', 'confirm', 'refuse', 'validate1', 'validate']; `hr.leave.report` → ['cancel', 'confirm', 'refuse', 'validate1', 'validate']; `hr.leave.employee.type.report` → ['cancel', 'confirm', 'refuse', 'validate1', 'validate']
- Validation: 15 declarative constraint method(s), 11 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Accrual Time Off: Updates the number of time off every 1 days; Time Off: Cancel invalid leaves every 1 days
- Security: groups declared 4 (`group_hr_holidays_responsible`, `group_hr_holidays_user`, `group_hr_holidays_manager`, `base.default_user_group`); record rules 26 (of which company-scoped by text 7); access rows 27

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 70 of 73 source pointers resolve to an existing file and in-range line (3 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_holidays (Time Off)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton: sourcemap/hr_holidays.json. Pointers `module/path:LINE`; (TEST) = test-derived.

## A. Capabilities / functions
- Application "Time Off": employees request time off, HR/managers approve, entitlements (allocations, regular or accruing over time) fund the balance, public holidays and mandatory days shape durations, and validated time off feeds calendars and presence (skeleton summary "Allocate time off and follow leave requests"; hr_holidays/models/hr_leave.py:34-70; hr_holidays/models/hr_leave_allocation.py:18-24).
- Depends on hr, calendar, resource (skeleton depends); application=true, no auto_install. Core: time-off types, requests, allocations, approvals, accrual plans, public holidays via resource calendar, dashboard, reports. Conditional: calendar meeting per leave (per leave type flag), supporting documents (per type), negative balance (per type), mandatory days, country-specific leave types.
- Time-off types with behaviour switches: validation (none / Time Off Officer / employee's approver / both), whether an allocation is required, whether employees may request extra allocation, unit (day / half-day / hours), unpaid flag, public holidays counted or not, worked-vs-absence kind, negative cap, supporting document, calendar display, accrual eligibility (hr_holidays/models/hr_leave_type.py:53-127).
- Seeded types (once, noupdate): Paid Time Off (allocation required, leave approved by approver then officer, allocation by officer), Sick Time Off (no allocation, supporting document), Compensatory Days (approver only, employees may request allocation), Unpaid (hours, both approvals), Extra Time Off (no validation), Extra Hours (approver); plus country-specific sets (UAE, Belgium, others) tied to the company's country (hr_holidays/data/hr_leave_type_data.xml:2-93 and following).
- Accrual plans with levels (start after N days/months/years, rate, hourly to yearly frequency, caps per balance and per year, carry-over rules and expiry) (hr_holidays/models/hr_leave_accrual_plan.py:10-75; hr_holidays/models/hr_leave_accrual_plan_level.py:13-140).
- Two daily scheduled jobs: accrual update; cancel time off that an accrual balance can no longer cover (hr_holidays/data/ir_cron_data.xml:4-22).
- Bulk creation wizards for time off and allocations by employee / department / tag / company (hr_holidays/wizard/hr_leave_allocation_generate_multi_wizard.py:109-140 and skeleton), mandatory days (company-wide or by department / job / calendar) blocking ordinary requests (hr_holidays/models/hr_leave.py:540-571,806-858), one-click approve/refuse links from emails (hr_holidays/controllers/main.py:10-58).

## B. Business objects, relationships, lifecycle
- Time-off request (employee, type, dates or hours, half-day periods, duration in days and hours, status, first and second approver, optional calendar meeting) (hr_holidays/models/hr_leave.py:70-232). Statuses: To Approve -> (Second Approval) -> Approved; Refused; Cancelled (hr_holidays/models/hr_leave.py:76-83).
- Allocation (employee, type, validity period, days or hours, regular or accrual, accrual plan, status To Approve / Second Approval / Approved / Refused) (hr_holidays/models/hr_leave_allocation.py:58-135). Balance for a type = approved allocations minus taken and pending time off (help text hr_holidays/models/hr_leave_type.py:59-66).
- Who is the "approver" of an employee: the "Time Off Approver" user, defaulting to the employee's manager's user and following manager changes; assigning someone adds them to the Time Off Responsible group and unassigned users are removed from it (hr_holidays/models/hr_employee.py:19-24,162-169,195-234; hr_holidays/models/res_users.py:48-60).
- Request flow by validation type (leave type setting): none -> approved immediately on creation with a system note; approver-only; officer-only; both (approver first = Second Approval, then officer) (hr_holidays/models/hr_leave.py:923-963,1188-1203,1276-1301). Refusal allowed from To Approve / Second Approval / Approved; nothing can move a cancelled request (hr_holidays/models/hr_leave.py:1303-1322,1458-1470).
- State matrix (documented in code): officers may move between most states including reset to To Approve and re-approve refused; the employee's approver may approve/refuse only for validation types that include the approver; the employee may cancel own approved/second-approval/refused requests (only future ones unless officer) (hr_holidays/models/hr_leave.py:1412-1456). Plain employees cannot reset: "cancel or delete and create another" (hr_holidays/models/hr_leave.py:1481-1482).
- Approval writes first/second approver identities; validation creates a calendar-level absence entry for the employee (resource leave) and, if the type asks, a calendar meeting; the employee is notified (hr_holidays/models/hr_leave.py:1051-1129,1276-1301). Any move away from Approved deletes that entry and meeting (hr_holidays/models/hr_leave.py:975-978,1397-1399).
- Cancel by the employee goes through a wizard with an optional reason; responsible approvers are notified depending on how far approval had gone (hr_holidays/wizard/hr_holidays_cancel_leave.py:11-27; hr_holidays/models/hr_leave.py:1342-1395). Refusal notifies the approver in some cases (hr_holidays/models/hr_leave.py:1324-1340).
- Allocation flow: creation always starts To Approve; auto-approved if the type needs no validation; otherwise approver / officer / both, with the same next-state logic; refusal possible from any open state (hr_holidays/models/hr_leave_allocation.py:812-834,899-936,713-751). Own allocation requests can be approved only by an Administrator (except types needing no validation) (hr_holidays/models/hr_leave_allocation.py:942-946); (TEST) (hr_holidays/tests/test_allocation_access_rights.py:152-194).
- Accrual: daily job processes validated accrual allocations whose next run date has come; adds days per level and frequency, prorating for partial periods and, when the plan is "based on worked time" or frequency is hourly, by attendance-eligible time versus absences; applies caps, yearly cap, carry-over with limit and expiry (hr_holidays/models/hr_leave_allocation.py:335-440,676-687,317-334). Level chosen by time since allocation start; transition immediate or after current period (hr_holidays/models/hr_leave_allocation.py:352-380). (TEST) (hr_holidays/tests/test_accrual_allocations.py, test_expiring_leaves.py:52-760, test_past_accruals.py: named cases; individual figures not summarised).
- Balance protection: creating or changing a request re-checks the balance; without an allocation (or exceeding the negative cap) the request is refused with an error (hr_holidays/models/hr_leave.py:806-857); the daily job cancels next-31-days requests that an accrual balance can no longer cover, with a note (hr_holidays/models/hr_leave.py:1682-1716). (TEST) negative balance rules (hr_holidays/tests/test_negative.py:44).
- Public holidays (company-level calendar absences): adding or changing them recalculates overlapping requests, gives days back or takes extra days from balances, and refuses requests that no longer fit the balance (except sick time off for extra days) (hr_holidays/models/resource.py:53-100). A request on a day where the employee is not working (zero days) cannot be approved (hr_holidays/models/hr_leave.py:1214-1215,1279-1286). (TEST) (hr_holidays/tests/test_global_leaves.py:68-260).
- Contract/version changes: creating or changing employee versions that alter the working schedule splits, refuses or returns to draft overlapping requests, with an error if balances no longer cover the recalculated durations (hr_holidays/models/hr_version.py:22-101). A request across two versions with different schedules is rejected (hr_holidays/models/hr_leave.py:433-462). (TEST) (hr_holidays/tests/test_multi_contract.py: file present).
- Departure: registering a departure truncates requests that span the date, cancels approved future ones, deletes others, deletes allocations starting after the date and ends others on the date (hr_holidays/wizard/hr_departure_wizard.py:9-70); (TEST) (hr_holidays/tests/test_hr_departure_wizard.py:28-110).
- Approval tasks are scheduled for the responsible person and cleared upon decision; responsible = approver, else employee's manager, else the type's "Notify HR" users (hr_holidays/models/hr_leave.py:1539-1553; hr_holidays/models/hr_leave_allocation.py:1026-1041). Quirk observed: the allocation task creation tests the leave validation setting, not the allocation validation setting of the type (hr_holidays/models/hr_leave_allocation.py:1051).

## C. Validations, automation, security, multi-company
- Dates: start not after end; days not negative; allocation duration > 0 for regular allocations; validity start not after end (hr_holidays/models/hr_leave.py:235-247; hr_holidays/models/hr_leave_allocation.py:128-140). Overlaps/warnings surface as blocking errors on the request (hr_holidays/models/hr_leave.py:788-796; message computation at :298).
- Type rules: negative cap needs a maximum >= 1; "Allow request on top" cannot be used with Absence kind; worked-time kind always eligible for accrual; public-holiday counting cannot change while affected leaves exist; allocation requirement cannot change once leaves exist (hr_holidays/models/hr_leave_type.py:130-133,170-181,182-215,248-252).
- Mandatory days: ordinary users cannot request time off on them; officers can (hr_holidays/models/hr_leave.py:845-847).
- Deleting: ordinary users only in To Approve / Second Approval / Cancelled and never in the past; officers only To Approve / Cancelled; Administrators anything (hr_holidays/models/hr_leave.py:1014-1029). Allocations deletable only when To Approve / Refused and with no taken time (hr_holidays/models/hr_leave_allocation.py:875-885).
- Editing an already-started request needs officer rights unless the user is that employee's approver (hr_holidays/models/hr_leave.py:966-971).
- Groups: Time Off Responsible (implied for any employee-approver, auto-granted), Officer: Manage all requests (implies Responsible and HR Officer of hr), Administrator (root and admin) (hr_holidays/security/hr_holidays_security.xml:9-31).
- Request record rules: employee reads own; can create/edit own unless second-approved/approved; approver/responsible reads and edits their reports' requests; officers read and edit all except own approved ones and may act on everyone else's; Administrator all; global company scope through the request's company (hr_holidays/security/hr_holidays_security.xml:34-138). Employee delete only own in To Approve/Second Approval (hr_holidays/security/hr_holidays_security.xml:61-70). Allocation rules mirror requests (own/approver read; own can edit only while To Approve; officers read all, edit others') plus company and type-company scope (hr_holidays/security/hr_holidays_security.xml:139-236). Public-holiday (resource) entries readable by all internal users, editable by officers only, with a code note that this may need tightening (hr_holidays/security/hr_holidays_security.xml:238-255). Types scoped by company or by the country of the user's companies (hr_holidays/security/hr_holidays_security.xml:256-268). Reports visible to all approvers or to department managers (hr_holidays/security/hr_holidays_security.xml:281-312).
- Privacy (business level): all employees can see everyone's time off in the calendar/reports; the free-text description of others' requests is restricted to responsibles/officers (code specification hr_holidays/models/hr_leave.py:34-45; private description field group at hr_holidays/models/hr_leave.py:128). Status "absent today" appears in employee presence for authorised viewers (hr_holidays/models/hr_employee.py:60-66,152-159). Email approval links require login and a token (hr_holidays/controllers/main.py:10-38).
- Company: changing a company's country is blocked when country-specific leave types are used by its leaves/allocations (except tests) (hr_holidays/models/res_company.py:8-25).
- Access lists: internal users create requests/allocations (record rules restrict), read types; officers read accrual plans; Administrators manage types, plans, mandatory days (skeleton access rows; hr_holidays/security/ir.model.access.csv).

## D. Accounting / payroll / analytic handoffs
- None in this module; unpaid and worked/absence flags are exported on the calendar absence entry for downstream use (hr_holidays/models/hr_leave.py:1051-1064). Work entries and payroll are owned by hr_work_entry_holidays (dependant present in tree) and enterprise payroll (UNKNOWN — EVIDENCE INSUFFICIENT: not read). Timesheets: project_timesheet_holidays depends on hr_holidays (manifest grep). No accounting or analytic entries.

## E. Configuration / defaults that change outcomes
- Per leave type: validation type (default "By Time Off Officer"), allocation required (default yes), employee requests (default no), unit (default day), public holidays counted (default no), negative cap (default off), calendar display (default on) (hr_holidays/models/hr_leave_type.py:53-127).
- Approver on the employee (default: manager's user) decides who acts first (hr_holidays/models/hr_employee.py:19-24).
- Accrual plan: gain at start or end of period (default end), transition mode (default immediate), carry-over date and unused-time action (lost by default) (hr_holidays/models/hr_leave_accrual_plan.py:26-44; hr_holidays/models/hr_leave_accrual_plan_level.py:115-124).
- Company calendar holidays and mandatory days change durations and permitted requests (see B/C).
- Hour-based allocations are re-derived when an employee's working hours per day change (hr_holidays/models/hr_version.py:100-118).

## F. Effective extension path
- Dependants in tree: hr_holidays_attendance, hr_holidays_homeworking, hr_presence, hr_work_entry_holidays, project_timesheet_holidays, l10n_fr_hr_holidays, l10n_fr_hr_work_entry_holidays, l10n_in_hr_holidays (manifest grep). hr_calendar consumes employee working-time calendars (not leaves): see hr_calendar note.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: dashboard data methods, reports and their SQL views, upgrade scripts, exact accrual arithmetic per frequency, half-day and hourly duration edge cases, demo data.

