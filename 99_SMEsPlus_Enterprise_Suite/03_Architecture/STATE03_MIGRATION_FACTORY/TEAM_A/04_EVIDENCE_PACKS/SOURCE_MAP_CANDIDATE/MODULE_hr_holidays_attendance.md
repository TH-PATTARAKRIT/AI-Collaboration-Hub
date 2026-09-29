# Source Map (candidate) — `hr_holidays_attendance`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_holidays_attendance` |
| Display name | HR Attendance Holidays |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `ca15add2b0cc35d8` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_holidays_attendance/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_attendance`, `hr_holidays`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / Attendance Holidays
- Inventory of user-facing artifacts (counts): menu items 1, views 13, window actions 2, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `hr.leave.attendance.report` (Attendance and Leave Analysis Report)
- Objects extended from other modules (10): `hr.leave`, `resource.calendar.leaves`, `hr.attendance.overtime.line`, `hr.leave.accrual.level`, `ir.ui.menu`, `hr.employee`, `hr.leave.allocation`, `hr.attendance`, `hr.leave.type`, `hr.attendance.overtime.rule`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.leave`, `resource.calendar.leaves`, `hr.attendance.overtime.line`, `hr.leave.accrual.level`, `ir.ui.menu`, `hr.employee`, `hr.leave.allocation`, `hr.attendance`, `hr.leave.type`, `hr.attendance.overtime.rule`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 48 of 49 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_holidays_attendance (HR Attendance Holidays)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_holidays_attendance.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge between Attendance and Time Off: converts an employee's approved extra (overtime) hours into usable time-off balance (hr_holidays_attendance/__manifest__.py:6-8, 10).
- Depends on hr_attendance and hr_holidays; `auto_install` true (hr_holidays_attendance/__manifest__.py:10-11).
- Optional per-rule: an overtime rule can be marked "Give back as time off" (default off) (hr_holidays_attendance/models/hr_attendance_overtime_rule.py:11); the resulting overtime lines carry a "compensable" mark (hr_holidays_attendance/models/hr_attendance_overtime.py:10).
- Optional per-leave-type: "Deduct Extra Hours" (default off); a leave type with this flag draws from extra hours (hr_holidays_attendance/models/hr_leave_type.py:10-12). The standard "Extra Hours" leave type is switched on by data, loaded once (noupdate) (hr_holidays_attendance/data/hr_holidays_attendance_data.xml:3-6).
- Two ways to spend hours: (1) a leave type that needs no allocation is drawn directly from the balance (hr_holidays_attendance/models/hr_leave.py:17-20); (2) a manager converts hours into an allocation of an allocation-based type (hr_holidays_attendance/views/hr_employee_views.xml:12-18, hr_holidays_attendance/views/hr_leave_allocation_views.xml:16-47).
- Extra-hours balance shown in leave/allocation forms and appended to the leave type name and allocation summary (hr_holidays_attendance/views/hr_leave_views.xml:7-10; hr_holidays_attendance/models/hr_leave_type.py:16-33, 35-66).
- New accrual frequency "Per Hour Worked" so accruals grow with attendance hours (hr_holidays_attendance/models/hr_leave_accrual_plan_level.py:9-15; hr_holidays_attendance/models/hr_leave_allocation.py:66-85).
- New report/menu "Time Off Ledger" under Attendance reporting comparing expected, worked, approved time off and difference per employee per day (hr_holidays_attendance/report/hr_leave_attendance_report.py:10, 18-27; hr_holidays_attendance/views/hr_leave_attendance_report_views.xml:114-133).
- Overtime recalculation when public/company leave records change (hr_holidays_attendance/models/resource_calendar_leaves.py:53-76).

## B. Business objects, relationships, lifecycle
- Balance per employee = approved compensable overtime lines minus non-refused/non-cancelled leaves of deductible no-allocation types minus pending or approved allocations of deductible types (hr_holidays_attendance/models/hr_employee.py:9-43).
- Employee summary returns compensable, non-compensable and unspent compensable overtime (hr_holidays_attendance/models/hr_employee.py:45-80).
- Leave lifecycle: create/write/approve/reset-to-draft re-check balance (hr_holidays_attendance/models/hr_leave.py:22-34, 56-64). Refusing or cancelling a leave returns the hours because refused/cancelled states are excluded from the deduction (hr_holidays_attendance/models/hr_employee.py:27). (TEST) refusal restores balance (hr_holidays_attendance/tests/test_holidays_overtime.py:142-156).
- Allocation lifecycle: balance checked at creation and on change of duration or type (hr_holidays_attendance/models/hr_leave_allocation.py:39-52, 58-64).
- Report rows are per employee-day, exclude company public-holiday days, use validated leaves only (hr_holidays_attendance/report/hr_leave_attendance_report.py:203-210 region, 295-303).
- Attendance table gets a performance index on check-in/check-out/employee (hr_holidays_attendance/models/hr_attendance.py:7-11).

## C. Validations, automation, security, multi-company
- Insufficient balance blocks a deductible leave with a message, worded differently for the employee themself vs. someone acting for them (hr_holidays_attendance/models/hr_leave.py:47-54). (TEST) request with no overtime is rejected (hr_holidays_attendance/tests/test_holidays_overtime.py:107-120).
- Insufficient balance blocks a deductible allocation (hr_holidays_attendance/models/hr_leave_allocation.py:58-64).
- Editing allocation duration or type after it has passed draft/confirm requires the time-off officer/administrator (hr_holidays_attendance/models/hr_leave_allocation.py:49-50).
- "Per Hour Worked" accrual cannot be combined with accrual at start of period (hr_holidays_attendance/models/hr_leave_accrual_plan_level.py:17-21); switching to start auto-falls back to hourly (hr_holidays_attendance/models/hr_leave_accrual_plan_level.py:23-27); form hides that option when accrual is at start (hr_holidays_attendance/views/hr_leave_accrual_level_views.xml:9-12).
- Combined rate when rules are summed: compensable-as-leave paid rules count fully, others count only their excess over 1 (hr_holidays_attendance/models/hr_attendance_overtime_rule.py:20-30).
- Security: Time Off Ledger readable (read-only) by attendance managers (hr_holidays_attendance/security/ir.model.access.csv:2); the menu is hidden unless user is both attendance manager and time-off officer (hr_holidays_attendance/models/ir_ui_menu.py:9-15); "Deduct Extra Hours" button needs time-off officer group (hr_holidays_attendance/views/hr_employee_views.xml:16). Balance computations read overtime with elevated rights (hr_holidays_attendance/models/hr_employee.py:12).
- Company scoping: ledger action limited to employees of the user's allowed companies (hr_holidays_attendance/views/hr_leave_attendance_report_views.xml:119). Company holiday matching uses company and calendar (hr_holidays_attendance/models/resource_calendar_leaves.py:32-49).
- No record rules of its own.

## D. Handoffs to other modules
- hr_attendance: owns attendance, overtime lines, overtime rules/rulesets, total overtime, reporting menu (hr_holidays_attendance/views/hr_attendance_overtime_views.xml:6,17; hr_holidays_attendance/views/hr_leave_attendance_report_views.xml:132).
- hr_holidays: owns leaves, allocations, leave types, accrual plans, officer group (hr_holidays_attendance/models/hr_leave.py:12; hr_holidays_attendance/views/hr_leave_allocation_views.xml:5).
- resource / hr (via hr_holidays): calendars, public holidays, employee versions used by the report (hr_holidays_attendance/models/resource_calendar_leaves.py:8).
- Payroll use of overtime rates: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration / defaults that change outcomes
- Overtime rule flag "Give back as time off" (off), leave type flag "Deduct Extra Hours" (off, on for the standard Extra Hours type), accrual frequency "Per Hour Worked".
- Company absence-management setting affects whether under-work yields negative overtime (TEST) (hr_holidays_attendance/tests/test_holidays_overtime.py:131-140); its definition is owned by hr_attendance.
- Ledger default filters: grouped by date and employee, negative-only, last two months (hr_holidays_attendance/views/hr_leave_attendance_report_views.xml:120-125).
- Ledger lookback for linked leaves/attendances: one year to yesterday (hr_holidays_attendance/report/hr_leave_attendance_report.py:33-37).

## F. Effective extension path
- Modules involved: hr_attendance (overtime rules/lines), hr_holidays (leave, allocation, accrual), resource. Extension points: overtime rule combination, leave/allocation balance checks, accrual proration, menu blacklist.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: how overtime lines are generated from rules (owned by hr_attendance).
- UNKNOWN — EVIDENCE INSUFFICIENT: cancellation of an already-consumed allocation returning hours (refusal path only shown as no-op wrapper, hr_holidays_attendance/models/hr_leave_allocation.py:54-56).
- UNKNOWN — EVIDENCE INSUFFICIENT: the removed/unused leave-overtime update helper marked for removal (hr_holidays_attendance/models/hr_leave.py:66-76).

