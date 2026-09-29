# Source Map (candidate) — `hr_recruitment_skills`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_recruitment_skills` |
| Display name | Recruitment - Skills Management |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `305a28b2565792d7` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_recruitment_skills/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `hr_skills`, `hr_recruitment`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Recruitment / Manage skills of your employees
- Inventory of user-facing artifacts (counts): menu items 1, views 8, window actions 1, server actions 1, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (1): `hr.applicant.skill` (Skill level for an applicant)
- Objects extended from other modules (3): `hr.job`, `hr.individual.skill.mixin`, `hr.applicant`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `hr.job`, `hr.individual.skill.mixin`, `hr.applicant`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 46 of 47 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_recruitment_skills (Recruitment - Skills Management)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_recruitment_skills.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge between Skills Management and Recruitment: applicants carry skills (with levels and, for certifications, validity dates); jobs already carry required skills and an expected degree from hr_skills; the module scores how well an applicant matches a job (hr_recruitment_skills/__manifest__.py:5-10; hr_recruitment_skills/models/hr_applicant.py:11-31).
- Depends on hr_skills and hr_recruitment; `auto_install` true (hr_recruitment_skills/__manifest__.py:10, 27).
- Matching output per applicant: matching skills, missing skills and a 0-100 score (hr_recruitment_skills/models/hr_applicant.py:21-31, 46-76). Shown as a "Skills" tab with a gauge and as a list column when non-zero (hr_recruitment_skills/views/hr_applicant_views.xml:9-34, 60-90 region).
- "Matching Positions" action on an applicant lists jobs with a score for that applicant; "Search Matching Applicants" action on a job lists applicants from other jobs that hold at least one required skill (hr_recruitment_skills/views/hr_applicant_views.xml:39-47; hr_recruitment_skills/models/hr_job.py:14-44, 46-66; hr_recruitment_skills/views/hr_job_views.xml:27-34).
- "Add to job" moves an applicant to the chosen job and to the first stage (hr_recruitment_skills/models/hr_applicant.py:135-144). (TEST) (hr_recruitment_skills/tests/test_recruitment_skills.py:521-553).
- Hire flow: skills of the applicant are copied onto the new employee (hr_recruitment_skills/models/hr_applicant.py:78-92). (TEST) (hr_recruitment_skills/tests/test_recruitment_skills.py:555).
- Search by skill and group by skill on applicants; menu "Skill Types" under recruitment configuration (hr_recruitment_skills/views/hr_applicant_views.xml:54-57, 60-72; hr_recruitment_skills/views/hr_applicant_skill_views.xml:38-44).
- Demo data provides sample skills (hr_recruitment_skills/__manifest__.py:23-25).

## B. Business objects, relationships, lifecycle
- New object "applicant skill" (skill, level, category, optional validity range), owned by one applicant and deleted with it (hr_recruitment_skills/models/hr_applicant_skill.py:7-19). Built on the shared individual-skill mixin from hr_skills (hr_recruitment_skills/models/hr_applicant_skill.py:9).
- Applicant keeps all skill rows (copied on duplicate) and a "current" view; stored list of distinct skills is derived for searching (hr_recruitment_skills/models/hr_applicant.py:11-20, 39-42).
- Current skills: expired rows are hidden; for a certification with only expired rows, the most recent one is kept (hr_recruitment_skills/models/hr_applicant_skill.py:24-36).
- Score: each required job skill counts by its level; an applicant skill counts up to twice the required level; degree adds weight only when the job expects a degree with positive weight; score = applicant total / job total, rounded percent, zero when the job has no skills and no degree (hr_recruitment_skills/models/hr_applicant.py:47-76). (TEST) job with no skills and zero-score degree (hr_recruitment_skills/tests/test_applicant_skills.py:497).
- Talent pool: when an applicant linked to a talent (pool) record has skills changed, the same change is mirrored on the talent record (created, updated or removed by matching skill); changes on the talent do not flow down to applicants (hr_recruitment_skills/models/hr_applicant.py:94-133, 155-166). (TEST) copy, add, update, delete cases (hr_recruitment_skills/tests/test_recruitment_skills.py:106-516).
- Creating a new (non-duplicate) applicant merges the "current" and full skill lists so duplicates/talent copies keep skills (hr_recruitment_skills/models/hr_applicant.py:146-153). (TEST) (hr_recruitment_skills/tests/test_recruitment_skills.py:602).
- Skill de-duplication and certification date handling are inherited from hr_skills and exercised here: identical skills collapse before creation, expired duplicate certifications are not created, same certification with different levels and identical dates can coexist (TEST) (hr_recruitment_skills/tests/test_applicant_skills.py:409-495); archive-vs-delete behaviour for skills and certifications (TEST) (hr_recruitment_skills/tests/test_applicant_skills.py:315-407).

## C. Validations, automation, security, multi-company
- Form warns when the end date is not after the start date (hr_recruitment_skills/views/hr_applicant_skill_views.xml:30-32); enforcement itself is in the shared mixin: UNKNOWN — EVIDENCE INSUFFICIENT.
- Security: interviewers get full rights on applicant skills (hr_recruitment_skills/security/ir.model.access.csv:2) limited by rule to applicants whose job or application lists them as interviewer (hr_recruitment_skills/security/hr_recruitment_skills_security.xml:4-13); recruitment officers see all (hr_recruitment_skills/security/hr_recruitment_skills_security.xml:15-20). Rules load once (noupdate) (hr_recruitment_skills/security/hr_recruitment_skills_security.xml:2).
- Recruitment officers also get full rights on job-required skills (hr_recruitment_skills/security/ir.model.access.csv:3).
- The job matching score field is visible only to interviewers and above (hr_recruitment_skills/models/hr_job.py:11-12); the job form's current-skill list is hidden from HR officers and interviewers in that view variant (hr_recruitment_skills/views/hr_job_views.xml:21-23). (TEST) interviewer can read matching skills of applicants they interview (hr_recruitment_skills/tests/test_recruitment_skills.py:584-600). Access-error case (TEST) (hr_recruitment_skills/tests/test_recruitment_skills.py:77).
- Company scoping: no company field or rule added; follows hr_recruitment: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- hr_skills: owns skills, levels, types, individual-skill mixin, job required skills, expected degree, skill type menu action (hr_recruitment_skills/models/hr_applicant_skill.py:9; hr_recruitment_skills/views/hr_applicant_skill_views.xml:41).
- hr_recruitment: owns applicant, job, stages, talent pool fields, interviewer group, degree type, employee creation values (hr_recruitment_skills/models/hr_applicant.py:64; hr_recruitment_skills/security/hr_recruitment_skills_security.xml:12).
- hr (employee): receives skills at hire (hr_recruitment_skills/models/hr_applicant.py:80).

## E. Configuration / defaults that change outcomes
- Job's required skills and levels, expected degree with its score, and applicant's degree type determine the score (hr_recruitment_skills/models/hr_applicant.py:56-68).
- Context selecting a target job changes the job used for scoring (hr_recruitment_skills/models/hr_applicant.py:44-50).
- Certification validity dates decide what counts as current and the warning colours (muted expired, red within 7 days, orange within a month) (hr_recruitment_skills/views/hr_applicant_views.xml:18-20; hr_recruitment_skills/models/hr_applicant_skill.py:29).

## F. Effective extension path
- Modules involved: hr_skills (mixin, job skills), hr_recruitment (applicant, talent pool). Extension points: skill commands on write, match scoring, employee creation values.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: how the mixin de-duplicates and validates dates (hr_skills, not read here).
- UNKNOWN — EVIDENCE INSUFFICIENT: whether the score influences stage or automated actions (none found in this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end gauge and skills widget behaviour.

