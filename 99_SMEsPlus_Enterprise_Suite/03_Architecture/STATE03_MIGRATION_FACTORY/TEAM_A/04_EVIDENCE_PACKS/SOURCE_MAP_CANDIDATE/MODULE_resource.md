# Source Map (candidate) — `resource`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `resource` |
| Display name | Resource |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G01 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `324dbc78d4819615` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/resource/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `base`, `web`
- Direct dependents in 300-module list (7): `base_automation`, `crm`, `digest`, `hr_holidays`, `mrp`, `project`, `resource_mail`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (2): `point_of_sale`, `test_resource`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / —
- Inventory of user-facing artifacts (counts): menu items 4, views 12, window actions 7, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (5): `resource.calendar` (Resource Working Time); `resource.calendar.attendance` (Work Detail); `resource.calendar.leaves` (Resource Time Off Detail); `resource.resource` (Resources); `resource.mixin` (Resource Mixin)
- Objects extended from other modules (2): `res.company`, `res.users`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `resource.calendar` ← Community: `hr`, `hr_holidays`, `hr_work_entry`; open-license custom/third-party scanned: —
- `resource.calendar.attendance` ← Community: `hr_work_entry`, `point_of_sale`; open-license custom/third-party scanned: —
- `resource.calendar.leaves` ← Community: `hr`, `hr_holidays`, `hr_holidays_attendance`, `hr_work_entry`, `project_timesheet_holidays`; open-license custom/third-party scanned: —
- `resource.resource` ← Community: `hr`, `hr_holidays`, `hr_skills`, `resource_mail`; open-license custom/third-party scanned: —
- `resource.mixin` ← Community: `hr`, `mrp`, `test_resource`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `res.company`, `res.users`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 3 declarative constraint method(s), 1 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 5 (of which company-scoped by text 2); access rows 8

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 45 of 45 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — resource
Source revision: 19.0.post20260921 | Module: "Resource" (resource/__manifest__.py:5), version 1.1 (:6), category Hidden (:7), LGPL-3 (:39). Depends on base, web (:16). Basis: static reading of all models, security, data, menus, and test names (tests not run).

## A. Capabilities and optionality
- A1. Defines things that can be scheduled (a person, a machine/work centre) and gives each a working calendar plus time off; other modules ask it "how many working hours/days between two dates", "when does work start/end", "plan N hours/days from a date". resource/__manifest__.py:12-14; resource/models/resource_calendar.py:803-943
- A2. Working-time calendar (resource.calendar): named, per company, with a time zone and a weekly list of work periods; two schedule types: fully fixed (days/periods with times) or flexible (only an amount of hours per week). resource/models/resource_calendar.py:60-79,83-93
- A3. Optional variants of a fixed calendar: two-week alternating pattern (first/second week sections, week parity counted from year 1 so it stays consistent across years) and "duration based" (hours centred on noon; lunch breaks not allowed). resource/models/resource_calendar.py:78-80,262-289; resource/models/resource_calendar_attendance.py:40-46,61-75,82-96
- A4. Work periods (resource.calendar.attendance) carry day of week, from/to hours, period (morning / break / afternoon / full day) and duration in hours and days; a break counts zero. resource/models/resource_calendar_attendance.py:14-39,77-106
- A5. Time off (resource.calendar.leaves): a generic company/calendar closure (public holiday) when no resource is set, or an individual absence when a resource is set; type "Time Off" or "Other" (other = counted as work time, e.g., training). resource/models/resource_calendar_leaves.py:35-51
- A6. Summaries computed per calendar: average hours per day and per week, work-time rate versus the full-time reference (hours needed to count as full time) and a full-time flag, number of resources using the calendar. resource/models/resource_calendar.py:81-102,193-208
- A7. Resource (resource.resource): type Human or Material, optional user link, company, timezone, working time calendar (no calendar means fully flexible), efficiency factor (used to estimate work-order duration at a work centre). resource/models/resource_resource.py:29-54,218-231
- A8. Reusable mixin that gives another business record (e.g. employee, work centre) its own resource, company, calendar and time zone, and day/hour counting helpers. resource/models/resource_mixin.py:10-30,80-140
- A9. Optionality: core dependency with no auto_install and no settings switch; installed whenever a dependent module is installed. resource/__manifest__.py:16; direct dependents (manifest scan): base_automation, crm, digest, hr_holidays, mrp, point_of_sale, project, resource_mail (auto_install), test_resource; hr reaches it through resource_mail.
- A10. Back-office screens under Settings > Technical > Resource: Working Times, Time Off details, Resources. resource/views/menuitems.xml:2-16

## B. Objects and relationships
- B1. Company owns many calendars and one default calendar (cannot be deleted while referenced). resource/models/res_company.py:10-13
- B2. Calendar has many work periods (deleted with the calendar) and many time-off lines; company-wide time-off ("global") are kept on the calendar and copied when the company changes. resource/models/resource_calendar_attendance.py:33; resource/models/resource_calendar.py:45-46,150-155
- B3. A time-off line belongs to a calendar and optionally a resource; if a resource is given the calendar follows the resource's calendar; company follows the calendar (or current company). resource/models/resource_calendar_leaves.py:53-61
- B4. User -> resources (one-to-many) with a convenience "default working hours" pointing at the first resource's calendar. resource/models/res_users.py:10-14
- B5. Lifecycle: calendars/resources are active/archived only; no approval states. New company automatically receives a calendar named "Standard 40 hours/week" (if none given). resource/models/res_company.py:15-45; resource/data/resource_data.xml:4-17
- B6. Default 40-hour week: Mon-Fri, morning 08:00-12:00, break 12:00-13:00, afternoon 13:00-17:00 — used when the company calendar has no periods; otherwise the company calendar's periods are copied to new calendars. resource/models/resource_calendar.py:744-772

## C. Validations, security, automation
- C1. Work periods of a calendar (per week in two-week mode) cannot overlap; contiguous periods are allowed. resource/models/resource_calendar.py:615-625,66-80 (TEST) resource/tests/test_resource_calendar.py:109-195
- C2. Two-week mode requires periods to sit under week sections and forbids deleting the section between weeks. resource/models/resource_calendar.py:66-72,124-130
- C3. A break period is refused on a duration-based calendar. resource/models/resource_calendar_attendance.py:61-65
- C4. Time-off start must be earlier than end (check on save); default range is the current day; end date defaults to end of the local day. resource/models/resource_calendar_leaves.py:20-33,63-78
- C5. Resource efficiency factor must be strictly positive (database check). resource/models/resource_resource.py:56-59
- C6. Work-hour inputs are clamped to 0-24 and ordered on screen entry. resource/models/resource_calendar_attendance.py:50-59
- C7. Time-off rules (record-level): internal users can read company-wide time-off and their own individual time-off; can change only their own individual entries; Access Rights administrators can change company-wide entries. resource/security/resource_security.xml:4-28
- C8. Multi-company: resource and time-off records are limited to the user's allowed companies plus records with no company. resource/security/resource_security.xml:30-40. The calendar and work-period models have NO record rule (all internal users may read every company's calendars). resource/security/ir.model.access.csv:2-5; skeleton: rules only for resource.resource and resource.calendar.leaves.
- C9. Access rows: calendars and work periods — internal users read, Settings administrators full; resources — read only for internal users and administrators (creation of resources goes through the owning business record); time off — internal users full (limited by C7) and administrators full. resource/security/ir.model.access.csv:2-9
- C10. When the Administrator sets their time zone at first login, the default calendar's zone is updated accordingly. resource/models/res_users.py:16-27
- C11. Copies get "(copy)" suffix; company-change on a calendar replaces its periods and time-off with the new company's defaults. resource/models/resource_calendar.py:151-156,177-183
- C12. No audit/tracking or chatter on these models in this module.

## D. Handoffs (owner of downstream processing)
- D1. Employees, contracts, leave requests, work entries, attendance: hr, hr_holidays, hr_work_entry, hr_attendance, hr_holidays_attendance, hr_calendar (they extend resource.resource/leaves/calendar or use resource_calendar_id per grep). Extension scan: calendar extended by hr, hr_holidays, hr_work_entry; leaves by hr, hr_holidays, hr_holidays_attendance, hr_work_entry, project_timesheet_holidays.
- D2. Manufacturing work-centre capacity and planning (efficiency, calendar): mrp (mixin user). Point-of-sale shift/calendar use: point_of_sale. Project planning and task scheduling: project; timesheet-related: hr_timesheet_attendance, sale_timesheet. Digest KPIs: digest. Automation: base_automation.
- D3. Chatter/mail behaviour on resource: resource_mail (auto_install with mail). resource_mail/__manifest__.py:9-10
- D4. Country payroll/leave localisations: l10n_fr_hr_holidays, l10n_fr_hr_work_entry_holidays, l10n_in_hr_holidays.
- D5. Working time computations (hours, days, planning, intervals) are consumed as services; the results feed leave duration, work entries, and scheduling in the owning modules above.

## E. Configuration/defaults that change outcomes
- E1. Calendar type (fixed vs flexible), two-week flag, duration-based flag, time zone — change how hours/days are computed. resource/models/resource_calendar.py:60-80,262-289
- E2. Full-time reference hours on the company default calendar (seed 40) drives the work-time rate and full-time flag of all calendars. resource/models/resource_calendar.py:47-49,120-125; resource/data/resource_data.xml:7
- E3. Time-off type "Other" is excluded from leave counting by default (default leave filter is type "Time Off"); passing another filter changes the outcome. resource/models/resource_calendar.py:507-508,803-820
- E4. Resource without calendar = fully flexible: no attendance intervals, leaves are the only unavailability. resource/models/resource_resource.py:218-231; resource/models/resource_calendar.py:585-604
- E5. Day quantity from hours: day counts use the periods' stored duration in days (morning/afternoon = 0.5, full = 1 default; a period longer than 3/4 of the average day counts as 1); flexible calendars divide hours by hours per day; fallback constant of 8 hours per day exists in helper. resource/models/resource_calendar_attendance.py:98-106; resource/models/resource_calendar.py:640-648; resource/models/utils.py:1-8
- E6. Leave overlap by company: a company-wide time-off applies to a resource only when the resource's company matches the time-off's company. resource/models/resource_calendar.py:526-527

## F. Effective extension path (module names only)
- Extend resource.resource: hr, hr_holidays, hr_skills, resource_mail. Extend resource.calendar: hr, hr_holidays, hr_work_entry. Extend resource.calendar.leaves: hr, hr_holidays, hr_holidays_attendance, hr_work_entry, project_timesheet_holidays. Use resource.mixin: hr, mrp, test_resource. Reference resource_calendar_id: digest, hr, hr_attendance, hr_calendar, hr_holidays, hr_holidays_attendance, hr_timesheet_attendance, hr_work_entry, l10n_fr_hr_holidays, l10n_fr_hr_work_entry_holidays, l10n_in_hr_holidays, mrp, point_of_sale, project, project_timesheet_holidays, sale_timesheet. Direct manifest dependents listed in A9.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: precise interval mathematics for flexible resources and mixed calendars (only skimmed: resource_resource.py:288-406 not read line by line).
- UNKNOWN — EVIDENCE INSUFFICIENT: what test_resource contains (test-support module; not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the missing record rule on calendars is compensated elsewhere (e.g., in hr extensions).
- UNKNOWN — EVIDENCE INSUFFICIENT: the 'plan_hours'/'plan_days' edge behaviour with leaves (signatures read, bodies not).

