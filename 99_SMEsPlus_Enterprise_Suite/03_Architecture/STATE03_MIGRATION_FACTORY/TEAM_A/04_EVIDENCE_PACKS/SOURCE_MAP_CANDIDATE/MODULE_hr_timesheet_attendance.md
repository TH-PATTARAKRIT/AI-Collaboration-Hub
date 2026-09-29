# Source Map (candidate) — `hr_timesheet_attendance`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_timesheet_attendance` |
| Display name | Timesheets/attendances reporting |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `2124f7a7f00a3514` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_timesheet_attendance/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_timesheet`, `hr_attendance`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Attendances / —
- Inventory of user-facing artifacts (counts): menu items 1, views 3, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `hr.timesheet.attendance.report` (Timesheet Attendance Report)
- Objects extended from other modules (1): `ir.ui.menu`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `ir.ui.menu`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 4 (of which company-scoped by text 1); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 17 of 17 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_timesheet_attendance
Revision 19.0.post20260921 | Bridge: Timesheets (hr_timesheet) <-> Attendances (hr_attendance) | reporting only

## A. Capabilities (core / optional / conditional)
- Adds one analysis report comparing attendance hours with timesheet hours per employee per day: "Timesheets / Attendance Analysis" (hr_timesheet_attendance/report/hr_timesheet_attendance_report_view.xml:56-58). Module description: links attendance to timesheet app (hr_timesheet_attendance/__manifest__.py:7). Depends on hr_timesheet and hr_attendance (:12).
- Auto-install: yes (hr_timesheet_attendance/__manifest__.py:18). No settings toggle, no new stored business data; the report is a read-only database view (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:9,22).
- Menu lives under the Timesheets reporting menu (hr_timesheet_attendance/report/hr_timesheet_attendance_report_view.xml:85-88); menu is hidden from users lacking the timesheet user group (hr_timesheet_attendance/models/ir_ui_menu.py:9-13).
- Views: graph (monthly time difference) and pivot (monthly attendance, timesheet, difference, costs) (report view xml:29-54,72-83). Search filters: My Team, My Department, week/today/last week, group by employee or date (:10-25).

## B. Business objects and lifecycle
- One report row per employee, date and company combining two sources: attendance records (hours worked) and timesheet lines that belong to a project (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:36-68). Fields: attendance time, timesheet time, difference, plus timesheet/attendance/difference costs (:12-20).
- Attendance is dated by check-in converted to the employee's current working-schedule time zone; timesheet by its own date (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:43-50,62).
- Only records dated today or earlier are included (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:54,67).
- No lifecycle: report is recomputed live from source records.

## C. Validations, automation, security
- Cost basis: employee hourly cost multiplied by hours for each of timesheet, attendance and their difference; zero results shown as empty (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:33-35,39).
- Access: read-only for the timesheet user group (hr_timesheet_attendance/security/ir.model.access.csv:2).
- Record rules: multi-company restriction for everyone (company in allowed companies, or no company) (hr_timesheet_attendance/security/hr_timesheet_attendance_report_security.xml:3-7); timesheet users see only their own employee rows (:9-14); approvers see all (:16-21); timesheet managers see all (:23-28).
- Default sort of grouped results: dates descending (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:74-78).
- (TEST) With one attendance day and 6h timesheet, the report yields 6 timesheet, 7 attendance, difference 1 (hr_timesheet_attendance/tests/test_timesheet_attendance.py:32-34); attendance 7 from an 8-hour check-in/out span is consistent with worked-hours logic owned by hr_attendance (deduction rule itself: UNKNOWN — EVIDENCE INSUFFICIENT here).

## D. Handoffs
- hr_attendance owns attendance records and worked-hours computation; hr_timesheet (with account analytic lines) owns timesheets; hr_employee owns hourly cost and working schedule.
- Rows link back to employee only; drill-through disabled (pivot/graph disable linking: report view xml:33,49).

## E. Configuration that changes outcomes
- Employee hourly cost drives all cost columns (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:39).
- Employee working schedule time zone shifts which day an attendance is counted on (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:46-49).
- Timesheet lines without a project are excluded (hr_timesheet_attendance/report/hr_timesheet_attendance_report.py:66).

## F. Effective extension path
- hr_timesheet, hr_attendance (module names only).

## G. Not verified
- Behaviour for employees with no schedule/time zone or open (no check-out) attendances: UNKNOWN — EVIDENCE INSUFFICIENT.
- Data migration content of upgrade step 1.1: UNKNOWN — EVIDENCE INSUFFICIENT (not opened).

