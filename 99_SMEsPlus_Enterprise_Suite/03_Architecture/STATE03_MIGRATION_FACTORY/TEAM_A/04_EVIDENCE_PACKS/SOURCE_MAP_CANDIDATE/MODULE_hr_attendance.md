# Source Map (candidate) — `hr_attendance`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_attendance` |
| Display name | Attendances |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `67ba8372e3b71bbb` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_attendance/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `barcodes`, `base_geolocalize`
- Direct dependents in 300-module list (2): `hr_holidays_attendance`, `hr_timesheet_attendance`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Attendances / Track employee attendance
- Inventory of user-facing artifacts (counts): menu items 12, views 22, window actions 7, server actions 3, reports 0, mail templates 0, scheduled jobs 2, wizards 1, web routes 13
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `hr.attendance.overtime.line` (Attendance Overtime Line); `hr.attendance` (Attendance); `hr.attendance.overtime.rule` (Overtime Rule); `hr.attendance.overtime.ruleset` (Overtime Ruleset)
- Objects extended from other modules (8): `hr.version`, `hr.employee.public`, `ir.http`, `res.company`, `hr.employee`, `res.users`, `res.config.settings`, `mail.thread`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.attendance.overtime.line` ← Community: `hr_holidays_attendance`; open-license custom/third-party scanned: —
- `hr.attendance` ← Community: `hr_holidays_attendance`; open-license custom/third-party scanned: —
- `hr.attendance.overtime.rule` ← Community: `hr_holidays_attendance`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `hr.version`, `hr.employee.public`, `ir.http`, `res.company`, `hr.employee`, `res.users`, `res.config.settings`, `mail.thread`

## 6. Actions / states / validation / automation / security
- State fields found: `hr.attendance.overtime.line` → ['to_approve', 'approved', 'refused']
- Validation: 4 declarative constraint method(s), 3 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Attendance: Automatically check-out employees every 4 hours; Attendance: Detect Absences for employees every 4 hours
- Security: groups declared 6 (`group_hr_attendance_own_reader`, `base.group_user`, `group_hr_attendance_officer`, `group_hr_attendance_user`, `group_hr_attendance_manager`, `base.default_user_group`); record rules 10 (of which company-scoped by text 4); access rows 11

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 66 of 67 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_attendance (Attendances)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton: sourcemap/hr_attendance.json. Pointers `module/path:LINE`; (TEST) = test-derived.

## A. Capabilities / functions
- Application "Attendances": check-in/check-out records per employee, worked hours versus expected hours, extra (over/under) hours with approval, and a kiosk for shared-device check-in (hr_attendance/__manifest__.py:4-9; hr_attendance/models/hr_attendance.py:27-60).
- Depends on hr, barcodes, base_geolocalize (hr_attendance/__manifest__.py:18); flagged as an application (hr_attendance/__manifest__.py:38); no auto_install.
- Check-in channels: manual entry by HR, kiosk (badge/RFID scan or manual pick, optional PIN), and "systray" check-in for logged-in users (hr_attendance/models/hr_attendance.py:47-59; hr_attendance/controllers/main.py:181-250; hr_attendance/models/res_company.py:21-35).
- Optional (company settings, off unless noted): extra-hours display, extra-hours approval by manager (default is automatic approval), employee PIN in kiosk, systray check-in (default off), automatic check-out (default off, tolerance 2 h), absence management (default off), device and location tracking (default off) (hr_attendance/models/res_company.py:20-43).
- Overtime engine driven by "rulesets" assigned to employee version records; ships a default ruleset (schedule-based quantity rule and non-working-days rule, both paid) and a UAE ruleset (day-time 125%, night 150% at 22-24 and 0-4, off days 150%) (hr_attendance/data/hr_attendance_overtime_ruleset_data.xml:4-55; hr_attendance/data/hr_attendance_overtime_rule_data.xml:4-21).
- Two scheduled jobs every 4 hours: automatic check-out of forgotten open attendances; absence detection (hr_attendance/data/hr_attendance_data.xml:4-20).

## B. Business objects, relationships, lifecycle
- Attendance (employee, check-in, optional check-out, day, worked hours, extra hours, validated extra hours, overtime status, capture mode in/out, and when device tracking on: location, IP address, browser) (hr_attendance/models/hr_attendance.py:33-64). An open attendance (no check-out) means the employee is "checked in"; latest attendance decides the state (hr_attendance/models/hr_employee.py:194-206). Check-in action creates a record; check-out action closes the open one; missing open record on check-out gives an error (hr_attendance/models/hr_employee.py:208-245).
- Worked hours = time between check-in and check-out minus lunch periods of the employee calendar; flexible-schedule employees have no lunch deduction (hr_attendance/models/hr_attendance.py:163-195).
- Overtime line (extra hours per attendance, with status To Approve / Approved / Refused, encoded duration, pay rate, applied rules) (hr_attendance/models/hr_attendance_overtime.py:12-39). Lines are (re)generated whenever attendances are created, moved or deleted: old lines of the affected days are deleted and rebuilt from the employee's ruleset in force on that date, keeping days where a manual change/pending approval existed marked To Approve (hr_attendance/models/hr_attendance.py:322-395). Employees without a ruleset get no lines (hr_attendance/models/hr_attendance.py:347-350).
- Overtime status gate: initial status is To Approve only when the company setting is "Approved by Manager", otherwise Approved (hr_attendance/models/hr_attendance_overtime.py:61-65). Approve/Refuse actions on a line, or from the attendance (hr_attendance/models/hr_attendance_overtime.py:85-89; hr_attendance/models/hr_attendance.py:595-599). Attendance status aggregates its lines: all approved -> approved; all refused -> refused; otherwise to approve (hr_attendance/models/hr_attendance.py:106-116). Validated hours count only approved lines (hr_attendance/models/hr_attendance.py:123-126); (TEST) refusing resets validated hours to zero (hr_attendance/tests/test_hr_attendance_undertime.py:458-476) and a manually edited duration flags the line To Approve after regeneration (hr_attendance/tests/test_hr_attendance_undertime.py:478-510).
- Employee total extra hours = sum of approved encoded durations (hr_attendance/models/hr_employee.py:112-124).
- Rule types: "quantity" (hours above an expected amount per day or week, expected hours either from the employee schedule or a fixed number) and "timing" (work days, non-work days, employee off, outside a given schedule; with time window) (hr_attendance/models/hr_attendance_overtime_rule.py:77-125). Ruleset combines rates by highest rate or by summing the premium above 100% (hr_attendance/models/hr_attendance_overtime_ruleset.py:18-31). "Regenerate" action rebuilds overtime for attendances since the earliest version using the ruleset (hr_attendance/models/hr_attendance_overtime_ruleset.py:39-51).
- Absence detection: for companies with absence management, employees with a fixed schedule, an active contract-start date before today and no overtime line yesterday get a 1-second technical attendance; if that creates no negative extra hours it is deleted again (hr_attendance/models/hr_attendance.py:660-697).
- Auto check-out: for open attendances of companies with the option, on fixed schedules only, when time worked that day exceeds expected schedule hours plus tolerance, the attendance is closed at the end of the day (reduced by the excess), mode "Automatic Check-Out", and a chatter note is posted (hr_attendance/models/hr_attendance.py:601-658).
- Archiving an employee automatically closes their open attendance at that moment, even for HR users without attendance rights (hr_attendance/models/hr_employee.py:82-91); (TEST) (hr_attendance/tests/test_hr_attendance_process.py:119-130,164-175).

## C. Validations, automation, security, multi-company
- Check-out cannot be earlier than check-in; an employee cannot have overlapping attendances or more than one open attendance (hr_attendance/models/hr_attendance.py:197-247); (TEST) (hr_attendance/tests/test_hr_attendance_constraints.py:24-66). Attendances cannot be duplicated (hr_attendance/models/hr_attendance.py:397-398). Overtime line: stop must be after start; rule time windows must be valid hours; quantity rules need expected hours and period; schedule rules need a schedule (hr_attendance/models/hr_attendance_overtime.py:56-59; hr_attendance/models/hr_attendance_overtime_rule.py:134-165).
- Groups: "User: Read his own attendances" (implied for all internal users), "Officer: Manage attendances" (only for employees who name them Attendance Approver), "Officer: Manage all attendances", "Administrator" (implies the previous, given to root and admin) (hr_attendance/security/hr_attendance_security.xml:9-38).
- Record rules on attendances: global company scope through the employee's company; administrators/all-attendance officers see all; approvers see only attendances of employees they approve; ordinary users read only their own (read-only) (hr_attendance/security/hr_attendance_security.xml:43-87). Same pattern for overtime lines (hr_attendance/security/hr_attendance_security.xml:90-120). Access lists: officers and above create/edit attendances and lines, own-reader read-only, rule/ruleset management only for Attendance Administrators with HR Managers read-only (skeleton access rows; hr_attendance/security/ir.model.access.csv).
- Assigning someone as Attendance Approver adds them to the officer group automatically; removing the last assignment removes them from it (hr_attendance/models/hr_employee.py:56-80; hr_attendance/models/res_users.py:10-16). Changing the employee on an attendance is blocked unless it is the user's own employee, the user is an Administrator, or the user is that employee's approver (hr_attendance/models/hr_attendance.py:376-382); (TEST) (hr_attendance/tests/test_hr_attendance_manager.py:48-72).
- Privacy (business level): approver, last check-in/out, attendance status, hours today and attendance list are visible only to attendance officers and HR officers; ruleset choice on an employee is visible only to HR Managers (hr_attendance/models/hr_employee.py:13-40; hr_attendance/models/hr_version.py:17-23); (TEST) (hr_attendance/tests/test_hr_attendance_rulesets.py:159-174). Location, IP and browser are captured only if device tracking is enabled (hr_attendance/controllers/main.py:57-75).
- Kiosk access control: the public kiosk page and its endpoints are guarded only by a secret company key embedded in the kiosk address; the key can be regenerated by attendance administrators; opening the kiosk from the back office logs out the user if a password is set (hr_attendance/controllers/main.py:15-19,85-95,139-160; hr_attendance/models/res_config_settings.py:50-52). Anyone with the address can list employees by name/department and check them in/out (badge scan, or manual choice which requires PIN only if the PIN option is on) (hr_attendance/controllers/main.py:193-240). Kiosk also exposes badge assignment and quick employee creation via the key (hr_attendance/controllers/main.py:97-131); whether these succeed for a public visitor depends on rights of the public user: UNKNOWN — EVIDENCE INSUFFICIENT.
- Multi-company: company from the kiosk key, or the active company selected in the browser for systray check-in (hr_attendance/controllers/main.py:78-83,241-249); (TEST) (hr_attendance/tests/test_hr_attendance_process.py:177-200 approx.).

## D. Accounting / payroll / analytic handoffs
- Payroll is not in Community: overtime lines carry the pay rate and a "paid" flag on rules, with a code comment stating that work-entry type belongs to payroll and time-off conversion to time off (hr_attendance/models/hr_attendance_overtime.py:35,41-42; hr_attendance/models/hr_attendance_overtime_rule.py:126). The consuming module: UNKNOWN — EVIDENCE INSUFFICIENT (enterprise payroll not in this tree).
- No accounting or analytic entries created here.

## E. Configuration / defaults that change outcomes
- Company settings listed in A; extra-hours validation (automatic vs by manager) determines whether pay-relevant hours need approval (hr_attendance/models/res_company.py:36-40). Auto check-out tolerance default 2 h (hr_attendance/models/res_company.py:41). Kiosk mode default "Barcode / RFID and Manual Selection", scanner source default front camera, kiosk message delay 10 s (hr_attendance/models/res_company.py:21-31).
- Two legacy tolerance fields (in favour of company/employee) still exist and trigger recalculation but are flagged for removal (hr_attendance/models/res_company.py:15-19,73-90); employee/employer tolerance now sits on each rule (hr_attendance/models/hr_attendance_overtime_rule.py:129-130). Effective behaviour: UNKNOWN — EVIDENCE INSUFFICIENT for legacy fields.
- The default ruleset is pre-assigned to new employee versions (hr_attendance/models/hr_version.py:17-23); rulesets and rules are scoped to the company (or global) (hr_attendance/security/hr_attendance_overtime_ruleset_security.xml:4-13).

## F. Effective extension path
- Extends hr (employee, version, public employee, company, settings, presence status: checked-in forces "present", hr_attendance/models/hr_employee.py:277-292). Consumed by: hr_holidays (leave-related overtime timing: UNKNOWN — EVIDENCE INSUFFICIENT), hr_homeworking / website_* kiosk variants not verified.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: full overtime interval maths for each rule type, report views, mobile/systray front end, demo data.

