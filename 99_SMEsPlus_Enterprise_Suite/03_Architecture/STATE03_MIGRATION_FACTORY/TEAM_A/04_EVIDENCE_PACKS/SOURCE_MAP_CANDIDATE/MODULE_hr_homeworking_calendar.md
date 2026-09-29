# Source Map (candidate) — `hr_homeworking_calendar`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_homeworking_calendar` |
| Display name | Remote Work with calendar |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6e88b870f5c343a3` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_homeworking_calendar/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_homeworking`, `calendar`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Remote Work / —
- Inventory of user-facing artifacts (counts): menu items 0, views 1, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `homework.location.wizard` (Set Homework Location Wizard)
- Objects extended from other modules (2): `hr.employee`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.employee`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 2 (of which company-scoped by text 0); access rows 1

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 32 of 33 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_homeworking_calendar (Remote Work with calendar)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_homeworking_calendar.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge between Remote Work and Calendar: shows each employee's work location (home/office/other) on the calendar and lets users set it per day or weekly (hr_homeworking_calendar/__manifest__.py:4-7; front-end assets under hr_homeworking_calendar/static/src/calendar/common/ listed in hr_homeworking_calendar/__manifest__.py:15-22).
- Depends on hr_homeworking and calendar; `auto_install` true (hr_homeworking_calendar/__manifest__.py:7, 14).
- "Set Location" dialog: choose date, optionally "repeat every <weekday>", and a location; also reachable as a bound action (hr_homeworking_calendar/wizard/homework_location_wizard.xml:3-36).
- Data feed for the calendar: for a list of employees (or for partners of those employees in the current company) returns, per weekday, the standing location, plus dated exceptions in the requested period (hr_homeworking_calendar/models/hr_employee.py:14-50; hr_homeworking_calendar/models/res_partner.py:9-13).
- Conditional: nothing appears if either dependency is missing; the module has no settings switch.

## B. Business objects, relationships, lifecycle
- Wizard record (temporary) holds location, employee (default: current user's employee), weekly flag and date (hr_homeworking_calendar/wizard/homework_location_wizard.py:8-19).
- Standing weekday locations live on the employee/user (owned by hr_homeworking); exceptions are dated employee-location records (hr_homeworking_calendar/models/hr_employee.py:24-29, 31-35).
- Lifecycle of "Set Location" without a date: does nothing (hr_homeworking_calendar/wizard/homework_location_wizard.py:28-29).
  - Weekly ON: removes any exception on that date and changes the standing location for that weekday (hr_homeworking_calendar/wizard/homework_location_wizard.py:38-44). (TEST) weekly option changes the employee's default, creates no exception (hr_homeworking_calendar/tests/test_hr_employee_location.py:16-29).
  - Weekly OFF, same as standing location: existing exception removed, none created (hr_homeworking_calendar/wizard/homework_location_wizard.py:46-48). (TEST) (hr_homeworking_calendar/tests/test_hr_employee_location.py:68-109).
  - Weekly OFF, exception already exists: it is updated, so only one exception per employee/day (hr_homeworking_calendar/wizard/homework_location_wizard.py:50-55). (TEST) (hr_homeworking_calendar/tests/test_hr_employee_location.py:46-66).
  - Weekly OFF, none exists: one exception is created (hr_homeworking_calendar/wizard/homework_location_wizard.py:56-61). (TEST) (hr_homeworking_calendar/tests/test_hr_employee_location.py:31-44).

## C. Validations, automation, security, multi-company
- Location is mandatory in the dialog (hr_homeworking_calendar/wizard/homework_location_wizard.py:12) and so is the employee (hr_homeworking_calendar/wizard/homework_location_wizard.py:15).
- Access: all internal users may use the wizard model (hr_homeworking_calendar/security/ir.model.access.csv:2). Rules: internal users see only their own wizard records; HR officers see all (hr_homeworking_calendar/security/security.xml:4-18; noupdate hr_homeworking_calendar/security/security.xml:3).
- The dialog itself does not check that the acting user may edit the chosen employee beyond the wizard rule and the rights on the final records: UNKNOWN — EVIDENCE INSUFFICIENT (weekly path writes with elevated rights: hr_homeworking_calendar/wizard/homework_location_wizard.py:42).
- Company scoping: partner-based lookup restricts to employees of the current company (hr_homeworking_calendar/models/res_partner.py:10-12).

## D. Handoffs to other modules
- hr_homeworking: owns work locations, weekday fields, day list, exception record, presence icons (hr_homeworking_calendar/models/hr_employee.py:8, 26-35; hr_homeworking_calendar/wizard/homework_location_wizard.py:5).
- calendar: owns the calendar views the front-end extends (hr_homeworking_calendar/__manifest__.py:7).
- hr: HR officer group used in rule (hr_homeworking_calendar/security/security.xml:16).
- (TEST) The list view request for employees swaps the generic location name for the weekday field of the current day (hr_homeworking_calendar/tests/test_hr_employee_location.py:111-122); implementation of that swap is outside this module's Python: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration / defaults that change outcomes
- Weekly flag default off (hr_homeworking_calendar/wizard/homework_location_wizard.py:17).
- Weekday from the chosen date decides which standing location is edited (hr_homeworking_calendar/wizard/homework_location_wizard.py:36-37).
- Contact for the calendar entry: user partner else work contact (hr_homeworking_calendar/models/hr_employee.py:20).

## F. Effective extension path
- Modules involved: hr_homeworking (data), calendar (UI), hr. Extension via the employee work-location feed and the set-location dialog.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end calendar behaviour (renderer, popover, year view) not read in detail.
- UNKNOWN — EVIDENCE INSUFFICIENT: whether managers can set locations for other employees via UI.

