# Source Map (candidate) — `hr_skills_survey`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_skills_survey` |
| Display name | Skills Certification |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `e785a5eabf00cb12` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_skills_survey/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_skills`, `survey`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Employees / Add certification to resume of your employees
- Inventory of user-facing artifacts (counts): menu items 0, views 2, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (3): `survey.user_input`, `survey.survey`, `hr.resume.line`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `survey.user_input`, `survey.survey`, `hr.resume.line`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 30 of 31 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_skills_survey (Skills Certification)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_skills_survey.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge between Employee Skills (resume) and Survey: when an employee passes a survey configured as a certification, a resume entry "Internal Certification" is created or refreshed automatically (hr_skills_survey/__manifest__.py:6-11; hr_skills_survey/models/survey_user.py:13-55).
- Depends on hr_skills and survey; `auto_install` true (hr_skills_survey/__manifest__.py:12, 22).
- Adds a "Validity (months)" setting to certification surveys, 0 meaning never expires (hr_skills_survey/models/survey_survey.py:9-12; hr_skills_survey/views/survey_survey_views.xml:9-11 shown only when the survey is a certification).
- Adds resume line fields: linked certification survey, department (stored copy from employee), and expiration status valid / expiring / expired (hr_skills_survey/models/hr_resume_line.py:11-16).
- Adds resume line type "Internal Certification", flagged as non-course (hr_skills_survey/data/hr_resume_data.xml:4-8). Manual resume lines of that type show a certification selector limited to certification surveys (hr_skills_survey/views/hr_templates.xml:9-18).
- Demo data: valid, expiring and expired sample certifications (hr_skills_survey/data/hr_resume_demo.xml:5-29).

## B. Business objects, relationships, lifecycle
- Resume line -> survey (certification) many-to-one, read-only by default, editable in the form for the certification type (hr_skills_survey/models/hr_resume_line.py:12; hr_skills_survey/views/hr_templates.xml:10-13).
- Lifecycle on completion of a response: only responses of certification surveys that scored as successful, whose participant maps to an employee via the user's contact, are processed (hr_skills_survey/models/survey_user.py:21-24). For each: start date = today, end date = today + validity months (none when validity is 0/empty), name = survey title, description = plain text of survey description, type = Internal Certification, survey linked (hr_skills_survey/models/survey_user.py:38-50). If the employee already has a line for that survey it is overwritten (dates reset), else a new line is created; done in batch (hr_skills_survey/models/survey_user.py:51-55). (TEST) creation, re-taking updates the same line with new validity/description, batch with two certifications (hr_skills_survey/tests/test_certification_flow.py:41-103).
- Expiration status recalculated from end date: expired on/after end date; expiring within 3 months before end; else valid; no end date means valid (hr_skills_survey/models/hr_resume_line.py:18-26).
- Duplicating a resume line adds "(copy)" to its name (hr_skills_survey/models/hr_resume_line.py:28-30).

## C. Validations, automation, security, multi-company
- Automation: triggered at response completion (hr_skills_survey/models/survey_user.py:13-19). Failed attempts create nothing (success filter, hr_skills_survey/models/survey_user.py:21).
- Missing "Internal Certification" type (if data deleted) still creates the line, without a type (hr_skills_survey/models/survey_user.py:33, 48).
- Employee matching: employee whose user's contact equals the response contact; participants without employee (public users) are ignored (hr_skills_survey/models/survey_user.py:23-24, 37-38). Employees are searched with the acting rights; the test note says completion runs elevated from the survey controller: (TEST) (hr_skills_survey/tests/test_certification_flow.py:45-46).
- No new groups, access entries or record rules (skeleton "access": [], "rules": []). Resume line security follows hr_skills.
- Company scoping: none added: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- survey: owns certification flag, scoring, success threshold, completion flow (hr_skills_survey/models/survey_user.py:21; hr_skills_survey/models/survey_survey.py:7).
- hr_skills: owns resume lines and line types (hr_skills_survey/models/hr_resume_line.py:9; hr_skills_survey/views/hr_templates.xml:6).
- hr: owns employee, department (hr_skills_survey/models/hr_resume_line.py:11).
- (Related, outside this module) certification skill levels in hr_skills use separate individual-skill records; not touched here: UNKNOWN — EVIDENCE INSUFFICIENT.

## E. Configuration / defaults that change outcomes
- Survey: certification flag, success percentage, validity months; test used 3 months and 85% pass mark (TEST) (hr_skills_survey/tests/test_certification_flow.py:21-30).
- Fixed 3-month "expiring" window (hr_skills_survey/models/hr_resume_line.py:25).

## F. Effective extension path
- Modules involved: survey (completion, scoring), hr_skills (resume), hr. Extension point: response completion hook and resume-line type data.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: whether a passed certification also updates skill level records (not in this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: recalculation of status over time without edits (stored field depends only on end date, hr_skills_survey/models/hr_resume_line.py:18); a scheduled refresh was not found in this module.
- UNKNOWN — EVIDENCE INSUFFICIENT: employees with several users/companies.

