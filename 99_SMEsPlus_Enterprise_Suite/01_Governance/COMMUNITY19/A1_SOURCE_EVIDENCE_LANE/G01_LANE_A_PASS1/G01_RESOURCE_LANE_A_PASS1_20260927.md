# G01 PLATFORM_BASE — LANE A PASS-1 — Module `resource`

| Field | Value |
|---|---|
| Lane | LANE A (blind source/static evidence) |
| Slot | T6 (refill) |
| Governed group | G01 PLATFORM_BASE |
| Module | `resource` (roster member per FREEZE_W1-STD.json) |
| Source anchor | `odoo/odoo` branch 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` — `addons/resource/` |
| Retrieval | raw.githubusercontent.com at the anchor commit; files found through the manifest and the `__init__` import chains |
| Date | 2026-09-27 |
| Status | **LANE A PASS-1 COMPLETE — HANDOFF TO A1** (static JS/test assets skipped on purpose, as scoped) |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema or workflow is reproduced. Identifiers appear only as pointers. |
| Question bank | No module-specific bank yet (Standard 55 only). This does not block Lane A. No QIDs are answered here. |

## 1. Evidence Pointer Table (20 blobs; SHA-1 = `git hash-object`)

| Path (addons/resource/…) | git blob SHA-1 | Purpose |
|---|---|---|
| `__manifest__.py` | 72b99e4faad899e6631ba8d1d96698b9c7ff1e0f | Identity, deps, data/demo/assets list |
| `__init__.py` | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | Imports models only |
| `models/__init__.py` | 9778b6b83ca946d2e97b61fe26f6b4eeab8f4ff0 | Model import list (8 modules) |
| `models/resource_calendar.py` | 335a857625070669ad79bd701fb38be03ec5704a | Working-time calendar and the interval computation engine |
| `models/resource_calendar_attendance.py` | d8fb69b117b5c395eedfc213a31e8480f4c79936 | Weekly working slots, week parity, durations |
| `models/resource_calendar_leaves.py` | 841053e65b7f2ea6693f4fa18d3e98eb7e821fe4 | Time-off / closing-day records |
| `models/resource_resource.py` | aad3af2f8b87bff4cc650819abc2856fdb826067 | Schedulable resource (human/material), flexible-hours logic |
| `models/resource_mixin.py` | b68b6a9fd53c7a54d29bd5765018202ee8e2e3f5 | Abstract mixin that attaches a resource to a business record |
| `models/res_company.py` | 3ba30d249a114b80374e146590bc864fd17aa123 | Company default calendar, auto-provisioning |
| `models/res_users.py` | ef4f885919e56161ce218abccbf95e3f69972b0b | User-to-resource link; admin tz propagation |
| `models/utils.py` | 38137c2643e937e853f8e769e4ea520df950a6df | Default hours-per-day constant; domain-filter helper |
| `data/resource_data.xml` | ffe3cf9ee87bf9ca54cc51f0773b62da4b1ecc4c | Standard calendar seed + backfill call (noupdate) |
| `data/resource_demo.xml` | f8865752db6bd2d9708bb5ee9db90801106418d1 | Demo: 35h, 38h and flexible 40h calendars |
| `security/ir.model.access.csv` | 34ca64a5e94929feffacb29fae63b73e78a0b3c7 | Model ACLs (8 rows) |
| `security/resource_security.xml` | 500b70f06c5fb917bd5657bbaaf23843920dae0c | Record rules (5; noupdate) |
| `views/resource_resource_views.xml` | 46b5626f24b6861ea8d24aabf2a14b8c6730cc28 | Resource search/form/list + 2 actions |
| `views/resource_calendar_leaves_views.xml` | d217acd509171c7cf0b400c20e4a1f1172a5da69 | Time-off views + 4 actions |
| `views/resource_calendar_attendance_views.xml` | 658430a4bd6d770a0d3a9f5707573f6793517641 | Attendance list/form |
| `views/resource_calendar_views.xml` | 402890182cb087e7b649f29a42f0aef14e7ae923 | Calendar views, mode-switch buttons, 1 action |
| `views/menuitems.xml` | 44953339ff89449a697025299372321819786c5d | Menu tree |

Probed absences (HTTP 404, not imported → absence, not gap): `controllers/__init__.py`, `wizard/__init__.py`.

## 2. Findings by card section

### 2.1 Manifest / deps / purpose
1. Hidden technical module. Depends only on `base` and `web`. LGPL-3. It models "things that can be scheduled" (people or equipment), gives each one a working calendar, and records their time off. [`__manifest__.py`]
2. It has no application menu of its own. Its surfaces sit under the technical settings area (see 2.5). Other modules consume it mostly through its computation API and `resource.mixin`. [`__manifest__.py`, `views/menuitems.xml`]

### 2.2 Data
3. **Resource** (`resource.resource`): name, active, company (optional), type (human vs material), optional linked user (email/phone/avatar mirrored from that user), efficiency factor, working calendar, timezone (required). The database rejects an efficiency factor that is zero or negative. WHY: the factor scales expected durations. [`models/resource_resource.py`]
4. The resource's calendar is optional. The help text and the `_is_fully_flexible` helper both state that a resource with no calendar is "fully flexible". The calendar selection is limited to calendars of the resource's own company. [`models/resource_resource.py`]
5. **Calendar** (`resource.calendar`): name, active, optional company, timezone (required), schedule type (flexible vs fully fixed, mirrored by a stored flexible flag), duration-based flag, two-week flag, attendances, leaves, stored averages (hours/day, hours/week), full-time reference hours, and a computed work-time rate and "is full time" flag. [`models/resource_calendar.py`]
6. **Attendance** (`resource.calendar.attendance`): weekday, from/to hour as decimal hours, day period (morning / break / afternoon / full day), week type (first/second, used only in two-week mode), section-row marker, sequence, and stored durations in hours and days. It is deleted with its calendar (cascade). [`models/resource_calendar_attendance.py`]
7. **Leave** (`resource.calendar.leaves`): reason, company (computed, read-only), calendar, start/end datetime, optional resource, and a time type ("Time Off" vs "Other"). The help text says an empty resource means a company-wide time off. [`models/resource_calendar_leaves.py`]
8. **Company extension**: a company has calendars and one default calendar. Deleting a calendar that a company uses as its default is blocked (restrict). **User extension**: a user has resources, and exposes an editable default calendar through them. [`models/res_company.py`, `models/res_users.py`]
9. **Mixin** (`resource.mixin`): any business record using it must have a resource (required; deletion restricted). Company, calendar and timezone are stored or related through that resource. [`models/resource_mixin.py`]
10. **Timezone defaults.** Calendar: context tz → user tz → admin user tz → UTC. Resource: context tz → user tz → UTC; on create, a missing tz is taken from the linked user or else from the calendar. Leave default dates cover "today" in the calendar's timezone and are stored as naive UTC. [`resource_calendar.py`, `resource_resource.py`, `resource_calendar_leaves.py`]

### 2.3 Business rules / exceptions
11. **Overlapping attendance validation.** When a calendar's attendances are saved, the slots are checked per weekday and must not overlap. In two-week mode each week is checked on its own. A tiny offset lets back-to-back slots touch without counting as an overlap. Violation → validation error. [`resource_calendar.py` `_check_attendance_ids`/`_check_overlap`]
12. **Two-week calendars.** Every period must sit under a week section, otherwise a validation error is raised. In the form, deleting either week section is blocked, and moving rows re-assigns their week type. Switching mode rebuilds the attendances: into two copied weeks, or back to the company default. [`resource_calendar.py` `_check_attendance_ids`, `_onchange_attendance_ids`, `switch_calendar_type`, `_get_two_weeks_attendance`]
13. **Week parity** is the count of days since a fixed epoch, divided by 7, taken modulo 2. It is not ISO week numbering. WHY: the source comment says this keeps odd and even weeks alternating across 53-week years. RISK: the parity may not match the user-visible ISO week number. [`resource_calendar_attendance.py` `get_week_type`]
14. **Hour bounds.** An onchange clamps start to 0–23.99 and end to 0–24, and keeps end ≥ start. A value of 24:00 is documented as the end of the day. No server-side constraint on hour order was observed. RISK: writes that bypass the form (import, RPC) are unguarded. [`resource_calendar_attendance.py`]
15. **Duration-based calendars** forbid break (lunch) rows; violation → user error. Entering a duration positions the slot around midday. Day-fraction default: break = 0, full day = 1, and morning/afternoon = 0.5 when the slot is at most three quarters of the average day, otherwise 1. [`resource_calendar_attendance.py`]
16. **Averages.** Hours per week and hours per day exclude breaks and section rows. Both are halved in two-week mode. For flexible calendars they are entered by hand, not computed. Full-time reference hours default to the company calendar's hours per week. Work-time rate = own weekly hours ÷ full-time hours; it is 100 when no reference exists. [`resource_calendar.py` compute methods]
17. **Working-interval computation.** Attendance intervals are generated per day for the requested window and localized per resource timezone. Resources are grouped by timezone for efficiency. Leave intervals are then subtracted, giving the effective work intervals. Break rows and section rows are excluded from work. All public entry points require timezone-aware datetimes or convert naive ones to UTC. [`resource_calendar.py` `_attendance_intervals_batch`, `_work_intervals_batch`, `get_work_hours_count`, `get_work_duration_data`]
18. **Global vs resource-specific leaves.** A leave without a resource applies to every resource on the matching calendar (or on no calendar). It applies only when the resource's company equals the leave's company. A leave with a resource applies only to that resource. By default only "Time Off" leaves reduce work; "Other" leaves (for example training) do not. Callers may override this with a domain. [`resource_calendar.py` `_leave_intervals_batch`]
19. **Flexible hours.** On a flexible calendar, synthetic intervals centred on midday are generated day by day, up to the average day and up to the weekly total. Leaves of flexible resources are widened to whole days. A fully flexible resource (no calendar) is treated as available for the whole requested window. For a fully flexible resource, the leave-days helper returns the whole span. [`resource_calendar.py`, `resource_resource.py` `_get_flexible_resource_valid_work_intervals`, `resource_mixin.py` `_get_leave_days_data_batch`]
20. **Planning helpers.** "Plan hours" and "plan days" walk forward or backward in 14-day windows, at most 100 of them. If the target is not reached they return false. RISK: a sparse calendar gives a silent false result after about 1,400 days. [`resource_calendar.py` `plan_hours`, `plan_days`]
21. **Leave dates.** Start must not be after end (validation error). When no valid end date is given, the end defaults to 23:59:59 of the start day in the user's timezone, or else in the company calendar's timezone. A leave takes its calendar from its resource, and its company from its calendar or else from the current company. [`resource_calendar_leaves.py`]
22. **Extension hooks.** Calendar validity per resource spans the whole period by default; the source comment says contract modules are meant to override it. Other overridable hooks: the calendar-at-date lookup and the flexible-leave widening. [`resource_resource.py`, `resource_calendar.py`]
23. **Admin first login.** When the admin user sets a timezone before ever logging in, that timezone is copied to their calendar or to the standard calendar. [`res_users.py` `write`]
24. **Caching.** The weekday-worked lookup is cached per calendar id. No explicit cache invalidation was seen in the fetched files, so the staleness behaviour is not verified. [`resource_calendar.py` `_get_working_hours`]

### 2.4 Security
25. **ACLs.**
    - Calendar and attendance: internal users can read only; system admins have full access.
    - Resource: **read-only for both internal users and system admins**. This module grants no create, write or delete on resources. Creation therefore depends on other modules' ACLs or on elevated contexts (the mixin's create path does not elevate itself in this file).
    - Leaves: full access for both internal users and system admins, narrowed by record rules.
    [`security/ir.model.access.csv`]
26. **Record rules on leaves** (internal users):
    - Read: company-wide leaves, plus leaves whose resource has no user or has the current user.
    - Write/create/delete: only resource-specific leaves whose resource has no user or has the current user.
    - Company-wide leaves: write/create/delete granted to the access-rights manager group (`base.group_erp_manager`).
    RISK: any internal user can modify leaves of resources that have no linked user, for example equipment. [`security/resource_security.xml`]
27. **Multi-company.** Resources and leaves carry a global rule: allowed companies plus records with no company. **No company rule exists on calendars or attendances in this module.** Company scoping for calendars relies only on selection-domain filters: allowed companies, a same-company domain on the resource's calendar field, and a company check on the leave's calendar. RISK: calendars of other companies may be readable by record access. [`security/resource_security.xml`, `resource_calendar.py`, `resource_resource.py`, `resource_calendar_leaves.py`]
28. Some UI elements are gated by group: company fields by the multi-company group, and the calendar's Time Off smart button by the technical/debug group. [views]

### 2.5 UI surfaces (names only)
29. Menus: "Resource" under the technical settings menu, with children for Working Schedules, Resource Time Off and Resources. [`views/menuitems.xml`]
30. Window actions:
    - Working Schedules
    - Resource Time Off (×2, one opened from a calendar)
    - Closing Days
    - Resources Time Off
    - Resources (×2, one opened from a calendar)
    Calendar form buttons: toggle duration-based mode, toggle one/two-week mode. [views]

### 2.6 Jobs / config
31. No scheduled jobs, no settings fields and no controllers.
32. Install data (noupdate) seeds a standard 40-hour calendar for the main company and backfills a calendar for every company that lacks one. Newly created companies get one automatically (elevated). Demo adds 35h, 38h and flexible 40h calendars. [`data/resource_data.xml`, `res_company.py`, `data/resource_demo.xml`]

## 3. Cross-module edges
33. Upstream: `base` (company, user, partner timezone list), `web` (assets). Downstream consumers are implied by the source comments and are not verified here: work-order duration via the efficiency factor, the contract hook, and enterprise planning/forecast use of the unavailable-intervals helper. `resource_mail` extends `resource.resource` (see its own card).
34. `resource.mixin` is the integration contract: consuming models get an auto-created resource, company/calendar/timezone carried on it, duplication of the resource on copy, and work-day, leave-day, per-day work-time and leave-listing helpers.

## 4. Evidence gaps / contradictions
- G1: Static JS (`static/src/**`) and tests were not reviewed (scoped out).
- G2: Resource create/write/delete ACLs are absent here. It is unverified which module grants them.
- G3: The absence of a multi-company rule on calendars and attendances was observed only in this module; `base` and other modules were not checked.
- G4: How the cache in #24 is invalidated was not verified.
- G5: `utils.py` constant and domain helper have no caller in the fetched files, so their use is not established.
- Contradiction candidate: the calendar field help says the rate "should be between 0 and 100 %", but no bound is enforced and the rate can exceed 100.

## 5. Limitations
Source presence ≠ runtime reachability. No runtime proof, no Formal Coverage, no percentages. The findings are a static reading of a single commit.
