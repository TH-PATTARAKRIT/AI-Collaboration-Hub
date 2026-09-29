# Source Map (candidate) — `hr_holidays_homeworking`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_holidays_homeworking` |
| Display name | Holidays with Remote Work |
| Manifest version | None |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f298b48f50707a34` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_holidays_homeworking/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_holidays`, `hr_homeworking`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / Manage holidays with remote work
- Inventory of user-facing artifacts (counts): menu items 0, views 0, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (1): `hr.employee`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.employee`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 17 of 18 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_holidays_homeworking (Holidays with Remote Work)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_holidays_homeworking.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests (none in Python; one front-end unit test exists, not read in detail).

## A. Capabilities / functions
- Bridge between Time Off and Remote Work: decides which presence icon an employee shows when both an approved absence and a remote-work location exist for today (hr_holidays_homeworking/__manifest__.py:3-8; hr_holidays_homeworking/models/hr_employee.py:7-17).
- Depends on hr_holidays and hr_homeworking; `auto_install` true (hr_holidays_homeworking/__manifest__.py:5-8, 19).
- Rule order for the icon: (1) absent today -> "holiday" icon variant, "present" variant if the person is nevertheless recorded present, otherwise "absent"; (2) else if a location applies today -> icon by location type; otherwise the base icon stays (hr_holidays_homeworking/models/hr_employee.py:11-17).
- Location for today = one-off exceptional location if set, else the standing location for the weekday (hr_holidays_homeworking/models/hr_employee.py:9, 11; day field selection owned by hr_homeworking/models/hr_employee.py:28-29).
- Front-end: presence-status widget is patched so holiday states show a plane icon, colour green when present or red-ish when absent, and label "..., back on <date>" using the leave end date; location states show home/building/marker icons and the location name or "Unspecified" (hr_holidays_homeworking/static/src/components/hr_presence_status/hr_presence_status.js:9-59). Assets registered at hr_holidays_homeworking/__manifest__.py:9-16.
- No new data models, fields, menus, settings, groups or data files.

## B. Business objects, relationships, lifecycle
- Object touched: employee (owned by hr; presence icon from hr; location fields from hr_homeworking; absence flag from hr_holidays) (hr_holidays_homeworking/models/hr_employee.py:5).
- Lifecycle: icon is recalculated whenever the presence icon is computed; an absence overrides remote-work display only while the employee is flagged absent today (hr_holidays_homeworking/models/hr_employee.py:12-14). The absent flag is true only for validated leaves of a "leave"-type time off type (hr_holidays/models/hr_employee.py:152, 159).
- Base module also defines icon states "holiday absent" and "holiday present" (hr_holidays/models/hr_employee.py:45, 110-114); this bridge sets them when remote work is installed so remote-work icons do not hide them.

## C. Validations, automation, security, multi-company
- No constraints, access entries, record rules or groups (skeleton: "access": [], "rules": []).
- Reads the exceptional location with elevated rights so ordinary viewers still see the icon (hr_holidays_homeworking/models/hr_employee.py:11).
- Company scoping: none added: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- hr_holidays: owns absence status and leave dates (hr_holidays/models/hr_employee.py:42, 152-159).
- hr_homeworking: owns work locations, weekday locations, exceptional locations and location-based icon states (hr_homeworking/models/hr_employee.py:11-29, 44-64).
- hr: owns the presence widget base (hr_holidays_homeworking/static/src/components/hr_presence_status/hr_presence_status.js:4-7).

## E. Configuration / defaults that change outcomes
- Depends on each employee's weekday locations and any per-date exceptions (configured in hr_homeworking / hr_homeworking_calendar).
- Depends on the leave type's classification as "leave" for the absent flag (hr_holidays/models/hr_employee.py:152).

## F. Effective extension path
- Modules involved: hr (presence icon), hr_holidays, hr_homeworking; extension via the employee presence-icon computation and the presence-status front-end widgets.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: the icon for half-day absences or absences not covering the whole day.
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end unit test contents (static/tests file not opened).

