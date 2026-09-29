# Source Map (candidate) — `hr_skills`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_skills` |
| Display name | Skills Management |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f6a8579e869c5832` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_skills/` |
| auto_install / application | True / True |

## 2. Dependencies
- Direct dependencies (manifest): `hr`
- Direct dependents in 300-module list (5): `hr_recruitment_skills`, `hr_skills_event`, `hr_skills_slides`, `hr_skills_survey`, `project_hr_skills`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Employees / Manage skills, knowledge and resume of your employees
- Inventory of user-facing artifacts (counts): menu items 9, views 36, window actions 8, server actions 2, reports 1, mail templates 0, scheduled jobs 1, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (10): `hr.employee.cv.wizard` (Print Resume); `hr.skill.type` (Skill Type); `hr.job.skill` (Skills for job positions); `hr.resume.line.type` (Type of a resume line); `hr.individual.skill.mixin` (Skill level); `hr.resume.line` (Resume line of an employee); `hr.skill` (Skill); `hr.employee.skill` (Skill level for employee); `hr.skill.level` (Skill Level); `report.hr_skills.report_employee_cv` (Employee Resume)
- Objects extended from other modules (4): `hr.employee.public`, `hr.job`, `hr.employee`, `resource.resource`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.individual.skill.mixin` ← Community: `hr_recruitment_skills`; open-license custom/third-party scanned: —
- `hr.resume.line` ← Community: `hr_skills_event`, `hr_skills_slides`, `hr_skills_survey`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `hr.employee.public`, `hr.job`, `hr.employee`, `resource.resource`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 5 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: Skills: Add an activity to employees with missing or expiring certifications every 1 days
- Security: groups declared 0 (—); record rules 11 (of which company-scoped by text 1); access rows 20

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 71 of 72 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_skills (Skills Management)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_skills.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Records what each employee knows and has done: skills with levels, dated certifications, and a resume (education, experience, training) per employee; also lists required skills per job position. Depends on hr only (hr_skills/__manifest__.py:16).
- Conditional + application: flagged as an application and auto_install true (hr_skills/__manifest__.py:47-48), so it comes with HR by default. No settings screen. Optional bridges in this tree that add sources of resume/skill data: hr_skills_survey (certifications), hr_skills_event (training events), hr_skills_slides (completed courses), all auto_install with their parent app; project_hr_skills (project skills, auto_install) and hr_recruitment_skills (applicant skills, auto_install) (each module's manifest; e.g. hr_skills_survey/__manifest__.py:15, 21; hr_recruitment_skills/__manifest__.py:10, 27).
- Skill catalogue: skill types (with levels 0-100 % and a default level; a type may be flagged as "certification"), skills within types (hr_skills/models/hr_skill_type.py:9-24; hr_skills/models/hr_skill_level.py:12-15; hr_skills/models/hr_skill.py:12-15). Seeded types: Languages and Soft Skills with a language list (hr_skills/data/hr_skill_data.xml:4-9, 15-101).
- Employee skills with validity dates; current-skill and certification lists on the employee form; public profile shows the same (hr_skills/models/hr_employee.py:17-24; hr_skills/models/hr_employee_public.py:9-14).
- Resume lines by section type (seeded: Other Experience, Education, Training [course]); optional certificate file, external link, dated (hr_skills/models/hr_resume_line.py:13-37; hr_skills/data/hr_resume_data.xml:4-17). Read-only computed job-history entries built from the employee's dated versions (hr_skills/models/hr_employee.py:153-209).
- Job position skill requirements, valid-dated (hr_skills/models/hr_job_skill.py:6-24; hr_skills/models/hr_job.py:8-24).
- Reports: skills inventory, certifications, skill history over time, department skill log action, all read-only SQL views (hr_skills/report/hr_employee_skill_report.py:6-45; hr_skills/report/hr_employee_certification_report.py:6-47; hr_skills/report/hr_employee_skill_history_report.py:6-68; hr_skills/data/ir_actions_server_data.xml:2-11). Printable resume (PDF) through a wizard with colour and section choices (hr_skills/wizard/hr_employee_cv_wizard.py:9-44; hr_skills/controllers/main.py:15-55).
- Menus: Skill Types (HR officers), Learning > Certifications and Training Attendances (HR officers), Reports > Skills, Resume sections in technical mode (hr_skills/views/hr_views.xml:597-628, 338-350; hr_skills/report/hr_employee_certification_report_views.xml:66-69; hr_skills/report/hr_employee_skill_report_views.xml:89-92).
- Automation: a daily job creates an "upload a certification" to-do (activity) for employees whose job requires a certification they lack or that expires within 3 months (hr_skills/data/ir_cron_data.xml:3-10; hr_skills/models/hr_employee.py:60-143; activity type hr_skills/data/mail_activity_type_data.xml:4-12).

## B. Business objects, relationships, lifecycle
- Employee skill / job skill / (applicant skill in hr_recruitment_skills) share one behaviour mixin: skill type, skill, level, validity start (default today) and stop (hr_skills/models/hr_individual_skill_mixin.py:47-57; hr_skills/models/hr_employee_skill.py:8-16; hr_recruitment_skills/models/hr_applicant_skill.py:10-24). Default skill is the first of the type; default level is the type's default-level flag else first (hr_skills/models/hr_individual_skill_mixin.py:231-246).
- History-preserving rules (documented in the code): only one active skill per skill for a person; changing skill/level/type never overwrites - the previous entry gets an end date of yesterday and a new entry starts today; removing a skill deletes it only if it started within about a day or has already ended, otherwise it is end-dated; certifications may coexist with the same skill and level if their validity windows differ, and can be deleted at any time (hr_skills/models/hr_individual_skill_mixin.py:69-87, 257-294, 296-415, 417-479, 481-537). (TEST) add/edit/remove scenarios: edit level -> new entry and previous end-dated to yesterday (hr_skills/tests/test_employee_skill.py:148-159); editing only the stop date of a certification updates in place (hr_skills/tests/test_employee_skill.py:161-172); recent entries deleted, older ones archived (hr_skills/tests/test_employee_skill.py:281-325); expired certification removal deletes it (hr_skills/tests/test_employee_skill.py:327-348); duplicates deduplicated before creation (hr_skills/tests/test_employee_skill.py:391-447).
- Job skills follow the same rules but their certification validity period cannot be edited (hr_skills/models/hr_job_skill.py:23-24).
- "Current" skills = validity stop empty or in the future; a certification type with only expired entries keeps the latest expired one visible (hr_skills/models/hr_employee_skill.py:18-32; hr_skills/models/hr_job.py:26-31).
- Skill types are archivable; inactive types disappear from employee/job lists (hr_skills/models/hr_employee.py:18-19; hr_skills/models/hr_job.py:12). Copying a skill type copies its skills (renamed "(copy)"), colour reset (hr_skills/models/hr_skill_type.py:63-73).
- Resume lines: cascade with the employee; type decides whether it is a "course" (hr_skills/models/hr_resume_line.py:13, 22-23).

## C. Validations, automation, security, multi-company
- A skill type must have at least one skill and one level (hr_skills/models/hr_skill_type.py:26-35); level progress must be 0-100 (hr_skills/models/hr_skill_level.py:23-26); only one default level per type (hr_skills/models/hr_skill_level.py:33-45); skill must belong to the chosen type and level must belong to the type (hr_skills/models/hr_individual_skill_mixin.py:206-218); stop date not before start date (hr_skills/models/hr_individual_skill_mixin.py:195-204); no overlapping or identical entries for the same person and skill, with the certification exception above (hr_skills/models/hr_individual_skill_mixin.py:65-109). Resume line start not after end (hr_skills/models/hr_resume_line.py:39-42).
- ACL: HR officers full on catalogue, resume, employee skills, job skills; every internal user may read the catalogue and add new skills to it (create allowed on skills) but not on types/levels (hr_skills/security/ir.model.access.csv:2-13, 19-20); internal users have create/write/delete rights on resume and employee-skill models, narrowed by rules to their own record, while everybody can read all resumes and skills (hr_skills/security/hr_skills_security.xml:4-52). Job requirements are read-only for ordinary users (hr_skills/security/ir.model.access.csv:19-20). Recruitment officers/interviewers get extra rights on job skills and applicant skills via the recruitment bridge (hr_recruitment_skills/security/ir.model.access.csv:2-3).
- Reports: HR officers see all; other users only rows of their department reports/subordinates (hr_skills/security/hr_skills_security.xml:54-80); skill report multi-company rule (hr_skills/security/hr_skills_security.xml:82-86). Access for the internal-user report ACL is read-only (hr_skills/security/ir.model.access.csv:14-18).
- Printing resume: internal users only, and non-HR users may print only their own employee record (hr_skills/controllers/main.py:17-23).
- Resume history endpoint refuses users who cannot read the public employee profile (hr_skills/models/hr_employee.py:153-160).
- Multi-company: catalogue has no company field; resume lines expose employee company/department as related fields (hr_skills/models/hr_resume_line.py:14-16); only the skill report carries an explicit company rule. The skill catalogue models define no company field, so the catalogue appears shared across companies (structure evidence: hr_skills/models/hr_skill_type.py:17-24, hr_skills/models/hr_skill.py:12-15); runtime confirmation: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Accounting / payroll / analytic handoffs
- None to accounting, payroll or analytic. Cost of time is elsewhere (hr_hourly_cost). Workforce planning use of skills (project staffing, matching) belongs to bridges: project_hr_skills (project side) and hr_recruitment_skills (applicant matching score against job skills and degree; copies applicant skills onto the created employee) (hr_recruitment_skills/models/hr_applicant.py:45-75, 78-89).
- Resume auto-feeds from other apps: surveys (certification), events (training), e-learning (courses) via their bridges (manifests above); the content mapping is not read: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration / defaults that change outcomes
- Certification flag on a skill type switches validity, overlap rules, reporting bucket, and the certification tab visibility (hr_skills/models/hr_skill_type.py:24; hr_skills/models/hr_employee.py:42-43; hr_skills/report/hr_employee_certification_report.py:42).
- Job position skills flagged as certifications drive the daily certification reminders; responsible person = employee's user, else manager's user, else the job's responsible user (hr_skills/models/hr_employee.py:81-92, 120-124).
- Skill report counts only active, non-certification entries that have no end date (hr_skills/report/hr_employee_skill_report.py:43). Certification report marks entries active when valid today (hr_skills/report/hr_employee_certification_report.py:36).
- Wizard defaults: colours from company branding, all three sections on (hr_skills/wizard/hr_employee_cv_wizard.py:15-20).

## F. Effective extension path (module names only)
- Extends: hr (employee, public employee, job, department views), resource (resource skills link). Dependents/bridges: hr_recruitment_skills, hr_skills_survey, hr_skills_event, hr_skills_slides, project_hr_skills (manifest grep).

## G. Not verified
- Bridge mappings for survey/event/e-learning resume lines: UNKNOWN — EVIDENCE INSUFFICIENT.
- Internal-user write access to other people's skill via ORM (rule blocks by employee user; specific HR-manager case): UNKNOWN — EVIDENCE INSUFFICIENT.
- Front-end skills widget behaviour: UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; nothing asserted as universal.

