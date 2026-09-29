# Source Map (candidate) — `hr_skills_event`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_skills_event` |
| Display name | Skills Events |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `5be2ff48be20c466` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_skills_event/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_skills`, `event`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Hidden / Link training events to resume of your employees
- Inventory of user-facing artifacts (counts): menu items 2, views 3, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (2): `event.event`, `hr.resume.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `event.event`, `hr.resume.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 28 of 29 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_skills_event (Skills Events)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_skills_event.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge between Employee Skills (resume) and Events: lets an employee's resume record an on-site training course by linking to an event (hr_skills_event/__manifest__.py:7, 13, 15).
- Depends on hr_skills and event; `auto_install` true (hr_skills_event/__manifest__.py:15, 21). Category hidden (hr_skills_event/__manifest__.py:5).
- Adds course type "Onsite" and an "Onsite Course" event link on resume lines (hr_skills_event/models/hr_resume_line.py:9-18). Course type and event fields become visible on form and list, external link only shown for external courses, event only for onsite (hr_skills_event/views/hr_resume_line_views.xml:8-19, 28-36).
- Event choices on a resume line are limited to events that already have at least one employee registered (hr_skills_event/models/hr_resume_line.py:12).
- New menu "Learning > Courses > Onsite" opening events that have an employee registered, in kanban/calendar/list/form/pivot/graph/activity views (hr_skills_event/views/event_event_views.xml:3-8; hr_skills_event/views/hr_views.xml:3-14). The parent "Courses" menu is declared here and also in hr_skills_slides, so it is shared between the two bridges (hr_skills_slides/views/hr_views.xml:3-7).
- Onsite lines colour (purple) and are highlighted in the kanban (hr_skills_event/models/hr_resume_line.py:31-35; hr_skills_event/views/hr_resume_line_views.xml:45-47).
- Optional/conditional: everything is dormant until a resume line is set to Onsite or an event is created from the Onsite action.

## B. Business objects, relationships, lifecycle
- Resume line (hr_skills) -> event (event) many-to-one; stored, read-only in the model but the views override to editable (hr_skills_event/models/hr_resume_line.py:9-14; hr_skills_event/views/hr_resume_line_views.xml:9, 35).
- Changing course type away from onsite clears the event link (hr_skills_event/models/hr_resume_line.py:25-29).
- Selecting an event with an empty name fills the line name from the event name (hr_skills_event/models/hr_resume_line.py:20-23).
- Creating an event from the resume-line form or the Onsite action (flagged by a context switch) automatically registers the relevant employee's work contact as an attendee: employee from context, else the current user's employee; requires the employee to have a work contact; skips if already registered (hr_skills_event/models/event_event.py:9-25). (TEST) event created from the action gets the current user's employee registered and appears in the Onsite view domain (hr_skills_event/tests/test_onsite.py:20-39).
- Developer comment states a boolean flag on events should replace this heuristic in a later version (hr_skills_event/models/event_event.py:11).
- (TEST) Only events with employees registered are offered in the resume line form (guided tour) (hr_skills_event/tests/test_onsite.py:10-18).

## C. Validations, automation, security, multi-company
- No constraints, groups, access entries or record rules of its own (skeleton "access": [], "rules": []).
- Menu inherits visibility of the Learning menu, restricted to HR officers (hr_skills/views/hr_views.xml:610-615).
- Automatic registration performed with the acting user's rights (no elevation in code): UNKNOWN — EVIDENCE INSUFFICIENT for users lacking event registration rights.
- Company scoping: none added: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- hr_skills: owns resume lines, course type list, resume views, Learning menu (hr_skills_event/views/hr_resume_line_views.xml:6, 26, 43; hr_skills_event/views/hr_views.xml:6).
- event: owns events and registrations (hr_skills_event/models/event_event.py:7, 24).
- hr: owns employee and work contact (hr_skills_event/models/event_event.py:18-19).
- hr_skills_slides: co-owner of the "Courses" menu (hr_skills_slides/views/hr_views.xml:3-7).

## E. Configuration / defaults that change outcomes
- Context switch `hr_skills_event_add_employee` set by the Onsite action and the event field on the resume line controls auto-registration (hr_skills_event/views/event_event_views.xml:8; hr_skills_event/models/hr_resume_line.py:13).
- Color for onsite lines fixed (hr_skills_event/models/hr_resume_line.py:35).

## F. Effective extension path
- Modules involved: hr_skills (resume), event (registration), hr. Extension via resume-line course types and event creation.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: how "completion" of an event (attended/done) affects the resume; link is manual, no completion trigger found in this module.
- UNKNOWN — EVIDENCE INSUFFICIENT: skills granted by attending events (none found).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end tour contents (static test not read).

