# Source Map (candidate) — `hr_calendar`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_calendar` |
| Display name | Display Working Hours in Calendar |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `be59960252478951` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_calendar/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `calendar`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Employees / —
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `calendar.event`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `calendar.event`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 0 (of which company-scoped by text 0); access rows 0

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 34 of 35 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_calendar (Display Working Hours in Calendar)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton: sourcemap/hr_calendar.json. Pointers `module/path:LINE`; (TEST) = test-derived.

## A. Capabilities / functions
- Bridge between employees (hr) and the shared calendar: shows attendees' working hours as an overlay on the calendar and flags meeting attendees who are not available during a meeting (hr_calendar/models/calendar_event.py:14-30; hr_calendar/models/res_partner.py:88-97).
- Conditional: installs automatically when hr and calendar are both present (hr_calendar/__manifest__.py:7-8); no application, no settings.
- Calendar view is switched to show "unusual days" (days outside the user's own working schedule) (hr_calendar/views/calendar_views_calendarApp.xml:8-10), fed by the current user's employee record (hr_calendar/models/calendar_event.py:32-34; hr/models/hr_employee.py:1733-1760).
- Attendee picker in the calendar gains a "My Team" filter: contacts who are employees of departments managed by the current user (hr_calendar/views/res_partner_views.xml:9-11).
- Front-end assets (calendar overlay widgets) are bundled into the backend (hr_calendar/__manifest__.py:13-19).

## B. Business objects, relationships, lifecycle
- No new stored objects or states; it only computes on existing calendar events and contacts (hr_calendar/models/*.py).
- Link between a calendar attendee (contact) and an employee is the employee's "work contact"; only employees of the active companies are considered (hr_calendar/models/res_partner.py:16-23).
- An attendee's schedule = union of the working periods of all employees linked to that contact, each employee using the working-time calendar that applies in each period; employees with no calendar on a period (fully flexible) fall back to the company calendar (hr_calendar/models/res_partner.py:25-86, esp. 51 and 69).
- Periods are taken only where the employee has a valid contract-type record ("check contract" default) (hr/models/hr_employee.py:1641-1646; hr/models/hr_employee.py:1608-1615); (TEST) an employee without a contract yields a fully grey week (hr_calendar/tests/test_working_hours.py:413-423), and contract start/stop dates bound the overlay (hr_calendar/tests/test_working_hours.py:330-368).
- The "everyone" overlay is the intersection of all selected attendees' schedules (only times when all are working) (hr_calendar/models/res_partner.py:97); if no attendee is an employee the overlay is empty; if the intersection is empty a sentinel makes the whole week grey (hr_calendar/models/res_partner.py:95-96, 105-111).
- Overlay times are displayed in the viewing user's time zone (fallback UTC) (hr_calendar/models/res_partner.py:99-104); (TEST) different-timezone cases (hr_calendar/tests/test_working_hours.py:86, 387).
- Meeting availability: an attendee is "unavailable" when the meeting time is not fully covered by that attendee's working schedule; the check is additive to the base calendar's busy-slot check (hr_calendar/models/calendar_event.py:15-30, 74-80; base at calendar/models/calendar_event.py:519-527). All-day meetings are measured against the company calendar's work intervals; an all-day meeting containing a company-closed day yields no interval and therefore no employee-availability flag (hr_calendar/models/calendar_event.py:36-72). (TEST) (hr_calendar/tests/test_event_interval.py:45, 68).
- Leaves recorded as calendar-level absences (resource leaves) reduce the schedule and therefore flag attendees as unavailable (TEST: hr_calendar/tests/test_working_hours.py:272-305). Whether approved time-off from hr_holidays feeds this the same way: UNKNOWN — EVIDENCE INSUFFICIENT in this module.

## C. Validations, automation, security, multi-company
- No constraints, no record rules, no access lists in this module (hr_calendar/__manifest__.py:9-12; skeleton rules/access empty).
- Privacy implication (business level): employee schedules are read with elevated rights when computing the overlay (hr_calendar/models/res_partner.py:23 uses privileged search of employees; hr/models/hr_employee.py:1645 uses privileged reading), so any calendar user can see (as shaded time) when other attendees are working or not, without needing access to the employee records. Only a time overlay is returned, not employee details (hr_calendar/models/res_partner.py:99-111).
- Company scoping: only employees of currently selected companies count; the meeting-day baseline uses the current company's calendar (hr_calendar/models/res_partner.py:18; hr_calendar/models/calendar_event.py:46); (TEST) multi-company selection cases (hr_calendar/tests/test_working_hours.py:111-250, 453).

## D. Accounting / payroll / analytic handoffs
- None.

## E. Configuration / defaults that change outcomes
- Results depend on each employee's working-time calendar (hr) and the company default calendar; a fully flexible employee is treated as following the company calendar for this overlay (hr_calendar/models/res_partner.py:51, 69). (TEST) mixed flexible / default (hr_calendar/tests/test_working_hours.py:485).
- Period-specific calendars are designed to plug in: the code states other modules may override the calendar-periods provider (hr_calendar/models/res_partner.py:26-30).

## F. Effective extension path
- Extends: hr (employee/version calendars), calendar (events, attendees), res.partner. Other modules override the calendar-periods provider (per docstring at hr_calendar/models/res_partner.py:27-29; specific overriders: UNKNOWN — EVIDENCE INSUFFICIENT).

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: interaction with public holidays per employee in hr_holidays; behaviour with recurring events beyond the tests read.

