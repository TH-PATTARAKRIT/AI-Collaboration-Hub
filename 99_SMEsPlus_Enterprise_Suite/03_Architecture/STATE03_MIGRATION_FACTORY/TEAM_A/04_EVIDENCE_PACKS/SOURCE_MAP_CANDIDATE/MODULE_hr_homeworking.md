# Source Map (candidate) — `hr_homeworking`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_homeworking` |
| Display name | Remote Work |
| Manifest version | 2.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `802caaf5b5d242c9` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_homeworking/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`
- Direct dependents in 300-module list (2): `hr_holidays_homeworking`, `hr_homeworking_calendar`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_discuss_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Remote Work / —
- Inventory of user-facing artifacts (counts): menu items 0, views 5, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `hr.employee.location` (Employee Location)
- Objects extended from other modules (5): `hr.employee.public`, `hr.work.location`, `hr.employee`, `res.users`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.employee.public`, `hr.work.location`, `hr.employee`, `res.users`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 2 (of which company-scoped by text 0); access rows 2

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 41 of 42 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_homeworking (Remote Work)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_homeworking.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Records where each employee usually works on each weekday (home / office / other), supports one-off exceptions for a specific date, and surfaces "today's location" in the employee list/grouping, the presence icon and the chat presence indicator. Depends on hr only (hr_homeworking/__manifest__.py:7).
- Conditional-on-install: auto_install true (hr_homeworking/__manifest__.py:15), so it is added automatically whenever hr is installed. Not an application; no settings.
- Seven weekday location fields on the employee (Mon-Sun), each pointing to a work location (hr_homeworking/models/hr_employee.py:11-17); mirrored on the public employee profile (hr_homeworking/models/hr_employee_public.py:7-13). Employees edit their own on the user Preferences/profile form and HR edits them on the user and employee forms (hr_homeworking/views/res_users.xml:9-16, 26-33; hr_homeworking/views/hr_employee_views.xml:18-27).
- "Exceptional" one-day location record per employee and date (hr_homeworking/models/hr_homeworking.py:8-17); the employee's "Current" exceptional location is looked up for today's date only (hr_homeworking/models/hr_employee.py:18-21, 44-53).
- Effective "current location" = today's exceptional location if any, else the weekday location; drives the employee's work-location name, work-location type and the presence icon (hr_homeworking/models/hr_employee.py:55-78). (TEST) weekday location used by default, exceptional overrides it, changing the weekday setting changes today's result (hr_homeworking/tests/test_hr_employee.py:54-82); a Sunday with none set yields empty (hr_homeworking/tests/test_hr_employee.py:48-52).
- Presence icon gains "At Home / At Office / At Other" states (hr_homeworking/models/hr_employee.py:22-24, 63-64). Chat presence status of users/partners is prefixed with the location type when a weekday location is defined for today and the base status is online/away/busy/offline (hr_homeworking/models/res_users.py:29-38; hr_homeworking/models/res_partner.py:9-18); (TEST) "home_offline" on Monday, "office_offline" on Tuesday (hr_homeworking/tests/test_hr_employee.py:84-90). Front-end icon rendering is in static assets (hr_homeworking/static/src/im_status_patch.xml:1-20).
- Employee search view gains "Work location" grouping by today's location, with the view text rewritten on each fetch to point at the current weekday's field (hr_homeworking/views/hr_employee_views.xml:8-10; hr_homeworking/models/hr_employee.py:31-42). Employee list shows work-location name and hides the base column (hr_homeworking/views/hr_employee_views.xml:37-42).

## B. Business objects, relationships, lifecycle
- Work location (owned by hr): name, company (required), type Home/Office/Other, work address (hr/models/hr_work_location.py:13-19).
- Employee -> up to 7 usual locations; Employee -> many dated exceptions (hr_homeworking/models/hr_homeworking.py:15, cascade delete with the employee).
- Exception object: location (required), employee (defaults to the current user's employee, required), date. At most one exception per employee per date (hr_homeworking/models/hr_homeworking.py:12-23).
- Lifecycle: no states. A usual-location change takes effect immediately for "today"; an exception affects only its date. Deleting a work location is blocked when any employee uses it as a usual location; dated exceptions pointing at it are removed silently instead (hr_homeworking/models/hr_work_location.py:12-19).

## C. Validations, automation, security, multi-company
- Constraint: one exception per employee and day (hr_homeworking/models/hr_homeworking.py:20-23).
- No cron; presence-related fields are computed on read.
- Access to exceptions: HR officers have full rights and every internal user has full CRUD rights (hr_homeworking/security/ir.model.access.csv:2-3), narrowed by a rule: ordinary users see/change only their own employee's rows; HR officers see all (hr_homeworking/security/security.xml:4-18). The rules are installed as no-update data (hr_homeworking/security/security.xml:3).
- Users may read and write their own weekday locations on their profile via the self-service field lists (hr_homeworking/models/res_users.py:18-27); location fields sync from user to employee (hr_homeworking/models/res_users.py:18-19, 10-16).
- The "Current" exceptional location field is HR-officer only (hr_homeworking/models/hr_employee.py:21); presence icon reads it with elevated rights so ordinary users still get the icon (hr_homeworking/models/hr_employee.py:60).
- Company scoping: work locations carry a required company (hr/models/hr_work_location.py:14) and address check-company (line 19); this module adds no company rule for exceptions. Cross-company use of a location on an employee: UNKNOWN — EVIDENCE INSUFFICIENT.
- "Today" is the server's current date, with no user-timezone adjustment in this module (hr_homeworking/models/hr_employee.py:29, 45).

## D. Accounting / payroll / analytic handoffs
- None. No accounting, payroll or analytic link; the data is presence/planning information.

## E. Configuration / defaults that change outcomes
- Locations must exist first (work-location master data from hr); their type decides icon and status prefix (hr_homeworking/models/hr_employee.py:63; hr_homeworking/models/res_users.py:33-38).
- Weekday fields empty = "Unspecified" and no override; then base presence logic applies (hr_homeworking/models/hr_employee.py:61-62; views placeholder hr_homeworking/views/hr_employee_views.xml:20-26).
- Weekday field names are fixed as a seven-item list (hr_homeworking/models/hr_homeworking.py:5); weekend days are included.
- Exception record's employee defaults to the acting user's employee (hr_homeworking/models/hr_homeworking.py:15).

## F. Effective extension path (module names only)
- Extends: hr (employee, public employee, work location, user, partner presence). Manifest dependents: hr_homeworking_calendar (calendar UI and wizard writing exceptions), hr_holidays_homeworking, test_discuss_full (test scaffold). Exceptions are also read/written from hr_homeworking_calendar models/wizard (hr_homeworking_calendar/models/hr_employee.py:31; hr_homeworking_calendar/wizard/homework_location_wizard.py:32-57).

## G. Not verified
- Behaviour when the same exceptional record is edited by a non-officer for another employee's date (rule blocks by employee; UI not traced): UNKNOWN — EVIDENCE INSUFFICIENT.
- Timezone effect of "today" for remote teams: UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; not asserted as universal.

