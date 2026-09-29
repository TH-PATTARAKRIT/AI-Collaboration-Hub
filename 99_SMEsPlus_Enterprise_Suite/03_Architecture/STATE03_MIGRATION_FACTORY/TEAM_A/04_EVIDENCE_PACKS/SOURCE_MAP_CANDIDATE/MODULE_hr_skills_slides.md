# Source Map (candidate) — `hr_skills_slides`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_skills_slides` |
| Display name | Skills e-learning |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `b91a0735fb140dfd` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_skills_slides/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_skills`, `website_slides`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Employees / Add completed courses to resume of your employees
- Inventory of user-facing artifacts (counts): menu items 2, views 8, window actions 1, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `hr.employee.public`, `slide.channel.partner`, `slide.channel`, `hr.resume.line`, `hr.employee`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.employee.public`, `slide.channel.partner`, `slide.channel`, `hr.resume.line`, `hr.employee`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 23 of 23 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_skills_slides
Revision 19.0.post20260921 | Bridge: Employee Skills/Resume (hr_skills) <-> eLearning (website_slides)

## A. Capabilities (core / optional / conditional)
- Adds completed eLearning courses to the employee resume ("Skills e-learning", summary: completed courses added to resume) (hr_skills_slides/__manifest__.py:5,7). Depends on hr_skills and website_slides (:15).
- Auto-install: yes (hr_skills_slides/__manifest__.py:26). No settings toggle; no new access rights or record rules (data list is views/demo only: :16-25).
- Adds a "Courses" smart button on the employee form showing completed/subscribed counts, visible only to eLearning officers and only when the employee has a linked user and at least one subscribed course (hr_skills_slides/views/hr_employee_views.xml:10-18; models/hr_employee.py:11-27).
- Adds a Learning > Courses > eLearning menu with an eLearning courses list (hr_skills_slides/views/hr_views.xml:3-14; views/slide_channel_views.xml:3-39).
- Resume line gets a new course type "eLearning" and a link to the course (hr_skills_slides/models/hr_resume_line.py:10-19), plus a course URL on employee and public employee cards (views/hr_employee_views.xml:28-31,39-42).

## B. Business objects and lifecycle
- Employee resume line (owner hr_skills) can point to an eLearning course (channel); duration defaults to the course total time and stays editable; name pre-fills from course name if empty; link cleared when type is not eLearning (hr_skills_slides/models/hr_resume_line.py:15,21-35). Colour distinct for eLearning lines (:37-41).
- Lifecycle: when a course membership is marked completed, an employee linked to that member's user gets a resume line of type "Training", dated today, with course name and plain-text course description; if the employee already has a line for that course, none is added (hr_skills_slides/models/slide_channel.py:12-52). (TEST) Completion adds exactly one line linked to the course (hr_skills_slides/tests/test_hr_skills_slides.py:39-49); a deleted line is not re-added on recompute (:51-74).
- Chatter on employee: subscription, leaving and completion of a course post a message with course link (hr_skills_slides/models/slide_channel.py:55-64,70-106). Employee matched by user, and same company as the partner when the partner has a company (:101-103).

## C. Validations, automation, security
- Creation of resume lines and chatter messages run with elevated rights, so the learner needs no HR access (hr_skills_slides/models/slide_channel.py:23,27,106).
- The completion notice posts on the current user's employee (not the learner) when the current user has one (hr_skills_slides/models/slide_channel.py:55-64); which user triggers it: UNKNOWN — EVIDENCE INSUFFICIENT.
- Courses button restricted by eLearning officer group (hr_skills_slides/views/hr_employee_views.xml:10,13). Public employee card exposes only completion text and flag; opening courses allowed only if the employee is a user (hr_skills_slides/models/hr_employee_public.py:9-15).
- Opening courses navigates to the employee's website profile page (hr_skills_slides/models/hr_employee.py:29-35).
- Company scoping: only through the same-company check for chatter (hr_skills_slides/models/slide_channel.py:102). Resume line creation matches every employee tied to the user's partner, no company filter (:23-24).

## D. Handoffs
- hr_skills owns resume lines, line types (Training), skills; website_slides owns courses, memberships, completion, website profile; hr owns employee.
- Training line type reference comes from hr_skills (hr_skills_slides/models/slide_channel.py:28).

## E. Configuration that changes outcomes
- Course description and name are copied to the resume line at completion time (hr_skills_slides/models/slide_channel.py:44-46).
- Course total time sets default duration (hr_skills_slides/models/hr_resume_line.py:24).
- If the Training resume type is absent, line created without a type (hr_skills_slides/models/slide_channel.py:28-29,47): resulting behaviour UNKNOWN — EVIDENCE INSUFFICIENT.

## F. Effective extension path
- hr_skills, website_slides, hr (module names only).

## G. Not verified
- Skills awarded by courses (hr skill levels from certification): UNKNOWN — EVIDENCE INSUFFICIENT (not in this module's models).
- Demo resume line effects (hr_skills_slides/data/hr_resume_line_demo.xml): UNKNOWN — EVIDENCE INSUFFICIENT (not opened). Frontend widget under static/src/fields: UNKNOWN — EVIDENCE INSUFFICIENT.

