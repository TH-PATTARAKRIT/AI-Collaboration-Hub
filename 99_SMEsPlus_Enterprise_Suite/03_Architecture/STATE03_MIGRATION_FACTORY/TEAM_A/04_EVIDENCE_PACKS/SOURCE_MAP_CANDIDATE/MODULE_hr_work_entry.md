# Source Map (candidate) — `hr_work_entry`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_work_entry` |
| Display name | Work Entries |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `463195313e378a1f` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_work_entry/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`
- Direct dependents in 300-module list (1): `hr_work_entry_holidays`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Employees / Manage work entries
- Inventory of user-facing artifacts (counts): menu items 0, views 19, window actions 4, server actions 1, reports 0, mail templates 0, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (4): `hr.work.entry.regeneration.wizard` (Regenerate Employee Work Entries); `hr.user.work.entry.employee` (Work Entries Employees); `hr.work.entry.type` (HR Work Entry Type); `hr.work.entry` (HR Work Entry)
- Objects extended from other modules (5): `hr.version`, `resource.calendar`, `resource.calendar.attendance`, `resource.calendar.leaves`, `hr.employee`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.work.entry.type` ← Community: `hr_work_entry_holidays`; open-license custom/third-party scanned: —
- `hr.work.entry` ← Community: `hr_work_entry_holidays`, `l10n_fr_hr_work_entry_holidays`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `hr.version`, `resource.calendar`, `resource.calendar.attendance`, `resource.calendar.leaves`, `hr.employee`

## 6. Actions / states / validation / automation / security
- State fields found: `hr.work.entry` → ['draft', 'conflict', 'validated', 'cancelled']
- Validation: 3 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Generate Missing Work Entries every 1 days
- Security: groups declared 0 (—); record rules 3 (of which company-scoped by text 1); access rows 6

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 86 of 87 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_work_entry (Work Entries)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_work_entry.json. Pointers are `module/path:LINE`; (TEST) = derived from tests. "Version" = the dated employment record of an employee (hr.version) that carries schedule and contract dates.

## A. Capabilities / functions
- Foundation for payroll-ready time data: turns each employee's working schedule (and time off) into dated, typed, hour-counted "work entries" that can be reviewed, corrected, and marked as consumed by a payslip. Depends only on hr (hr_work_entry/__manifest__.py:9-11).
- Optional/conditional: not an application, no auto_install of its own (hr_work_entry/__manifest__.py:4-8); it is brought in by explicit installation or by a dependent. In this tree the dependent bridge is Time Off in Payslips, which is auto_install when both hr_holidays and hr_work_entry are present (hr_work_entry_holidays/__manifest__.py:17, 23). No settings screen.
- Sources: only "Working Schedule" exists as a work-entry source in this module (hr_work_entry/models/hr_version.py:27); the help text names attendance- and planning-based sources as requiring other apps (hr_work_entry/models/hr_version.py:31-32). Those apps' bridges are not in this tree: UNKNOWN — EVIDENCE INSUFFICIENT.
- Automatic generation: a daily scheduled job (Generate Missing Work Entries, runs as the superuser) builds entries for the current month for versions whose generated window does not yet cover it, at most 100 versions per run, re-triggering itself for the rest (hr_work_entry/data/ir_cron_data.xml:4-13; hr_work_entry/models/hr_version.py:698-729). Static (calendar-based) versions are processed first (hr_work_entry/models/hr_version.py:725).
- Manual generation and regeneration: employee-level generate call (hr_work_entry/models/hr_employee.py:51-59) and a manager-only regeneration wizard that rebuilds a date range (hr_work_entry/wizard/hr_work_entry_regeneration_wizard.py:97-129).
- Work entry types: seeded catalogue - Attendance (code WORK100), Overtime, Out of Contract, Generic/Compensatory/Home-working/Unpaid/Sick/Paid time off, plus country-specific sets (e.g., UAE overtime rates and holidays, Australian leave types) (hr_work_entry/data/hr_work_entry_type_data.xml:3-71, 75-114, 120-141; about 118 records). Types carry a payroll code, a 3-letter display code, an external export code, a pay-rate multiplier (default 1.0), flags "Time Off", "Working Time", "Added to Monthly Pay" (hr_work_entry/models/hr_work_entry_type.py:11-37).
- Screens: list/form/pivot/calendar for work entries, a "conflict" action pre-filtered on conflicting entries, work-entry-type list/form/kanban, a "Set to Draft" bulk server action (hr_work_entry/views/hr_work_entry_views.xml:6-19, 143-164, 219-231, 306-316). This module defines no menu items (search of the module found none); entry points from Community UI are the employee form "Work Entries" button, visible to HR managers only when entries exist (hr_work_entry/views/hr_employee_views.xml:11-12) and the actions opened by other modules.
- Schedule setup: each schedule line and each global/personal time-off record can carry a work entry type (defaults: Attendance for schedule lines) (hr_work_entry/models/resource_calendar_attendance.py:9-14; hr_work_entry/models/resource_calendar_leaves.py:9-11); schedule lines whose type is a time-off type are not counted as worked hours (hr_work_entry/models/resource_calendar_attendance.py:21-22; hr_work_entry/models/resource_calendar.py:10-15); (TEST) working hours count excludes such a line (hr_work_entry/tests/test_work_entry.py:215-226).
- Personal calendar filter of which employees a user displays (hr_work_entry/models/hr_user_work_entry_employee.py:6-20).

## B. Business objects, relationships, lifecycle
- Work entry: employee, version ("Employee Record", required), date, duration in hours (default 8), type, pay rate, company (read-only, filled from the employee), department (stored copy), state, active flag (hr_work_entry/models/hr_work_entry.py:23-50). One entry is one day / one type / one version; generation merges same-day, same-type, same-employee, same-version, same-company pieces and drops zero-duration pieces (hr_work_entry/models/hr_version.py:608-624).
- Version is chosen automatically from employee and date when not supplied (hr_work_entry/models/hr_work_entry.py:93-99, 242); (TEST) entries before/after a new version pick the matching version (hr_work_entry/tests/test_hr_work_entry.py:166-185). Pay rate is copied from the type at creation unless given (hr_work_entry/models/hr_work_entry.py:245-250).
- States: New (draft), In Conflict, In Payslip (validated), Cancelled (hr_work_entry/models/hr_work_entry.py:39-44). Transitions: create -> draft (or conflict if a check fails: hr_work_entry/models/hr_work_entry.py:258); validate -> validated only if no error (109-120); setting state to draft re-activates and to cancelled deactivates (263-267); changing the active flag forces draft/cancelled (270-271).
- Generation window per version: "Generated From/To" dates and last generation date, all HR-officer only and tracked (hr_work_entry/models/hr_version.py:20-26). A new employee version starts with an empty window set to today (hr_work_entry/models/hr_employee.py:28-34). Generation only extends the window outward, so periods already generated are not duplicated (hr_work_entry/models/hr_version.py:472-483); (TEST) repeated generation creates no duplicates (hr_work_entry/tests/test_work_entry.py:55-60).
- Generation content: schedule attendance minus time off (per employee resource and calendar-level global time off), leaves become entries of the leave's type, a generic time-off type is used when a leave has none, pieces spanning midnight in the schedule timezone are split by local day (hr_work_entry/models/hr_version.py:139-143, 71-82, 233-339, 543-557). Fully flexible schedules use employee timezone and average-hours logic for multi-day leaves (hr_work_entry/models/hr_version.py:192, 237-252). A version without a schedule produces zero-duration leave pieces that are then dropped (hr_work_entry/models/hr_version.py:581-584, 611-612).
- Regeneration ("force"): non-validated entries in the window are deactivated and rebuilt; validated ones are never touched (hr_work_entry/models/hr_version.py:462-470, 489-491; deactivation field hr_work_entry/wizard/hr_work_entry_regeneration_wizard.py:94-95); (TEST) new version dated before the month causes January entries to be re-attached to it (hr_work_entry/tests/test_hr_work_entry.py:145-164).
- Split: an entry of at least 1 hour can be split into two, the split part strictly shorter than the original (hr_work_entry/models/hr_work_entry.py:122-136).

## C. Validations, automation, security, multi-company
- Duration must be more than 0 and at most 24 hours (hr_work_entry/models/hr_work_entry.py:55-59); (TEST) zero duration is rejected (hr_work_entry/tests/test_hr_work_entry.py:86-96).
- Conflict rules (automatic, re-run after create/write/unlink of relevant fields): (1) missing type; (2) total per employee per day not above 24h (and not zero); (3) time-off entries completely outside the schedule (skipped for flexible or missing schedules); (4) any employee-day that already has a validated entry marks the other entries of that day as conflicting (hr_work_entry/models/hr_work_entry.py:138-229, 261-277, 292-328). (TEST) missing type -> conflict, then draft when fixed; 8h + 17h same day -> both conflict, 8h + 16h -> both draft (hr_work_entry/tests/test_hr_work_entry.py:56-125); (TEST) validation refuses an entry without type and passes once fixed (hr_work_entry/tests/test_work_entry.py:71-83).
- Validated entries cannot be deleted; deletion is otherwise routed through the same conflict re-check (hr_work_entry/models/hr_work_entry.py:279-287). Form makes validated entries read-only (hr_work_entry/views/hr_work_entry_views.xml:85-87, 99-111).
- Type integrity: payroll code unique within a country or against country-less types (hr_work_entry/models/hr_work_entry_type.py:46-59); country of Attendance type is locked and country of any type used by entries cannot change (hr_work_entry/models/hr_work_entry_type.py:39-44).
- Schedule/contract changes: changing the schedule or source on a version regenerates its already generated period; if the version's employee has validated entries in the range the whole regeneration is skipped for them (hr_work_entry/models/hr_version.py:665-696; hr_work_entry/wizard/hr_work_entry_regeneration_wizard.py:109-114; (TEST) hr_work_entry/tests/test_hr_work_entry.py:187-217). Changing contract start/end or version date removes entries that fall outside the period (hr_work_entry/models/hr_version.py:626-644, 669-670); deleting a version deletes its non-validated entries (hr_work_entry/models/hr_version.py:646-663, 680-682). Interaction of the outside-period removal with validated entries (delete guard above): UNKNOWN — EVIDENCE INSUFFICIENT.
- Wizard guards: needs employees and dates; dates must lie within the generated range; refuses when every selected employee has validated entries in the range (hr_work_entry/wizard/hr_work_entry_regeneration_wizard.py:97-113). A timezone missing on schedule, employee schedule and company schedule aborts generation (hr_work_entry/models/hr_version.py:518-520).
- ACL: HR officers can read/write/create entries but not delete; system administrators have full rights; types are read-only for officers, full for HR managers; the regeneration wizard is HR-manager only; the personal filter is officer-level (hr_work_entry/security/ir.model.access.csv:2-7). Employee-specific fields (source, has-entries) are gated to HR manager/officer groups (hr_work_entry/models/hr_employee.py:10-12; hr_work_entry/models/hr_version.py:22, 33).
- Multi-company: entries limited to the user's allowed companies; types limited to countries of allowed companies plus country-less; selectable type list also narrows to the companies' countries (hr_work_entry/security/hr_work_entry_security.xml:14-24; hr_work_entry/models/hr_work_entry.py:330-333). Entry company follows the employee, not the acting user (hr_work_entry/models/hr_work_entry.py:251-256); (TEST) (hr_work_entry/tests/test_hr_work_entry.py:42-54). The cron handles one company per pass (hr_work_entry/models/hr_version.py:713-717). Personal filter rule: own rows only (hr_work_entry/security/hr_work_entry_security.xml:3-12).

## D. Accounting / payroll / analytic handoffs
- Payroll (owner: a payroll module, not present in this Community tree): the state name "In Payslip", the payroll code, pay-rate multiplier, "Added to Monthly Pay" flag and external code exist to feed payroll (hr_work_entry/models/hr_work_entry.py:42; hr_work_entry/models/hr_work_entry_type.py:13-14, 31-37). How payslips consume entries and set state to validated: UNKNOWN — EVIDENCE INSUFFICIENT.
- Time Off (owner: hr_holidays, via bridge hr_work_entry_holidays): leave types map to work entry types (hr_work_entry_holidays/models/hr_leave.py:9-12); approved leaves write the type onto the resource time-off record (hr_work_entry_holidays/models/hr_leave.py:18-21) and, when a leave is validated, create leave entries for the part of the leave already inside the generated window and archive the non-validated attendance entries they fully cover (hr_work_entry_holidays/models/hr_leave.py:23-88, 127-130); refusing/cancelling a leave regenerates the attendance entries (hr_work_entry_holidays/models/hr_leave.py:132-165); cancelling a work entry refuses its leave (hr_work_entry_holidays/models/hr_work_entry.py:15-18). Every leave create/write runs the conflict check over the affected period (hr_work_entry_holidays/models/hr_leave.py:89-121).
- Accounting/analytic: none in this module. Timesheets: none (uses separate hr_timesheet). Attendance-based overtime: extension hook only (hr_work_entry/models/hr_version.py:341-343); bridge not in tree: UNKNOWN — EVIDENCE INSUFFICIENT.
- Cost of time (hourly cost) is separate: see hr_hourly_cost; work entries do not read it.

## E. Configuration / defaults that change outcomes
- Which schedule and which timezone a version uses decides entry boundaries and day splits (hr_work_entry/models/hr_version.py:404-409, 518).
- Per-line type on schedule and on global time off decides the type of generated entries; unset leave type falls back to the generic time-off type (hr_work_entry/models/hr_version.py:82, 57-58).
- Defaults: entry duration 8 hours (hr_work_entry/models/hr_work_entry.py:29); default type is the first type found (hr_work_entry/models/hr_work_entry.py:33); Attendance is the fallback for intervals without type (hr_work_entry/models/hr_version.py:44-47, 139-143); new types get rate 1.0 (hr_work_entry/models/hr_work_entry_type.py:33).
- Context switches change behaviour: no-check flag (hr_work_entry/models/hr_work_entry.py:305) and skip-validation flag for the wizard (hr_work_entry/wizard/hr_work_entry_regeneration_wizard.py:99).
- Cron interval one day, active on install (hr_work_entry/data/ir_cron_data.xml:9-12); batch size 100 (hr_work_entry/models/hr_version.py:719).
- Wizard default range is the month of "From" (hr_work_entry/wizard/hr_work_entry_regeneration_wizard.py:28-31).

## F. Effective extension path (module names only)
- Extends hr (employee, version), resource (calendar, attendance, leaves). Dependents in tree: hr_work_entry_holidays, then l10n_fr_hr_work_entry_holidays (auto_install on hr_work_entry_holidays: l10n_fr_hr_work_entry_holidays/__manifest__.py:12; it extends the work entry model). Extension hooks intended for other bridges: extra values per interval, bypass codes, fields that trigger recompute (hr_work_entry/models/hr_version.py:61-69, 694-696). Payroll/planning/attendance-source modules: not in tree.

## G. Not verified
- "Set to Draft" bulk action calls a method that is not defined in this module or in hr_work_entry_holidays and was not found anywhere in the Community tree (hr_work_entry/views/hr_work_entry_views.xml:306-316); provider: UNKNOWN — EVIDENCE INSUFFICIENT.
- Payslip consumption and validated-state setting by payroll: UNKNOWN — EVIDENCE INSUFFICIENT.
- Front-end calendar/gantt behaviour (static assets): UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; nothing asserted as universal.

