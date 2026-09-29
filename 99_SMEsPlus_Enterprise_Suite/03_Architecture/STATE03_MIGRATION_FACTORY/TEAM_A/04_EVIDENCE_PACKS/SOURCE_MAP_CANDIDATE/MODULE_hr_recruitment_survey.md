# Source Map (candidate) — `hr_recruitment_survey`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_recruitment_survey` |
| Display name | Hr Recruitment Interview Forms |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `f0f1a53e50c9113e` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_recruitment_survey/` |
| auto_install / application | None / None |

## 2. Dependencies
- Direct dependencies (manifest): `survey`, `hr_recruitment`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources / Surveys
- Inventory of user-facing artifacts (counts): menu items 1, views 8, window actions 1, server actions 0, reports 0, mail templates 1, scheduled jobs 0, wizards 1, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (5): `survey.invite`, `hr.job`, `survey.survey`, `survey.user_input`, `hr.applicant`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `survey.invite`, `hr.job`, `survey.survey`, `survey.user_input`, `hr.applicant`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 0 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 14 (of which company-scoped by text 0); access rows 13

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 52 of 53 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_recruitment_survey (Hr Recruitment Interview Forms)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_recruitment_survey.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.
Note: no `auto_install` key in the manifest (hr_recruitment_survey/__manifest__.py:2-29), so this is an optional module installed by choice, not automatically. It bridges survey and hr_recruitment (hr_recruitment_survey/__manifest__.py:12).

## A. Capabilities / functions
- Interview forms for recruitment: a job position can be linked to a survey used as the interview form; from an applicant one can send it to the candidate, or print the answered (or blank) form (hr_recruitment_survey/__manifest__.py:7-10; hr_recruitment_survey/models/hr_job.py:9-11; hr_recruitment_survey/models/hr_applicant.py:11-12, 14-32, 34-67).
- Adds a survey type "Recruitment", visible to interviewers and survey users (hr_recruitment_survey/models/survey_survey.py:9, 12-18).
- On the job: "Interview Form" selector limited to recruitment surveys; on the job kanban, shortcuts "Interviews" (test form) or "Interview Form" (create new form pre-titled with the job name) (hr_recruitment_survey/views/hr_job_views.xml:8-35; hr_recruitment_survey/models/hr_job.py:13-33).
- On the applicant: "Send Interview" button (active applicants whose job has a form) and "Consult Interview" statistic button when responses exist (hr_recruitment_survey/views/hr_applicant_views.xml:20-35).
- Recruitment-specific "Interviews" configuration menu for recruitment managers, plus a link in the settings screen and a "Go to Recruitment" link on the survey button form for managers (hr_recruitment_survey/views/survey_survey_views.xml:60-90; hr_recruitment_survey/views/res_config_setting_views.xml:8-14; hr_recruitment_survey/views/survey_templates_statistics.xml:4-11).
- Invitation email template "Applicant: Interview" with 15-day default deadline (hr_recruitment_survey/data/mail_template_data.xml:4-35; hr_recruitment_survey/models/hr_applicant.py:57). Demo interview forms and jobs provided (hr_recruitment_survey/__manifest__.py:23-26).

## B. Business objects, relationships, lifecycle
- Job -> one interview form (survey) (hr_recruitment_survey/models/hr_job.py:9); survey knows its job positions (hr_recruitment_survey/models/survey_survey.py:10). Applicant sees the job's form read-only and owns the list of responses (hr_recruitment_survey/models/hr_applicant.py:11-12); each response points back to its applicant (hr_recruitment_survey/models/survey_user_input.py:9).
- Lifecycle of "Send Interview": ensure a contact exists (created from applicant name, email, phone if missing) -> validate form is open -> open invitation dialog prefilled with applicant, form, template, light email layout (hr_recruitment_survey/models/hr_applicant.py:37-58). On confirmation, if no response exists for that form a response is created for the applicant, and a note "survey sent to partner" is posted (hr_recruitment_survey/wizard/survey_invite.py:28-48). (TEST) (hr_recruitment_survey/tests/test_recruitment_survey.py:56-68).
- When the invitation email is produced, its body is also posted in the applicant's chatter and the mail is sent (hr_recruitment_survey/wizard/survey_invite.py:21-26).
- Resend mode counts the applicant as already covered (hr_recruitment_survey/wizard/survey_invite.py:14-19).
- When the candidate finishes, a note "applicant has finished the survey" is posted as the system bot (hr_recruitment_survey/models/survey_user_input.py:11-17).
- Retry of a survey keeps the applicant link (hr_recruitment_survey/controllers/main.py:6-12).
- Print: latest completed response; else latest response; else blank form (hr_recruitment_survey/models/hr_applicant.py:17-32). (TEST) (hr_recruitment_survey/tests/test_recruitment_survey.py:89-101).

## C. Validations, automation, security, multi-company
- Missing applicant name with no linked contact blocks sending (hr_recruitment_survey/models/hr_applicant.py:38-40).
- Survey validity check before sending (hr_recruitment_survey/models/hr_applicant.py:48).
- Form design view for non-survey users is a reduced primary view (hr_recruitment_survey/models/survey_survey.py:20-26; hr_recruitment_survey/views/survey_survey_views.xml:3-19 hides type, send, session, archive buttons).
- Manager views of completed inputs are restricted to recruitment surveys (hr_recruitment_survey/models/survey_survey.py:28-34).
- Security (rules noupdate: hr_recruitment_survey/security/hr_recruitment_survey_security.xml:3; intent summarised in comment lines 4-11):
  - Recruitment managers: full rights on recruitment surveys, questions, answers, responses and lines; create/edit but not delete invites (hr_recruitment_survey/security/ir.model.access.csv:2-6; hr_recruitment_survey/security/hr_recruitment_survey_security.xml:14-73).
  - Recruitment officers: read responses and lines of recruitment surveys that are unrestricted or list them as allowed user; create/edit invites under the same condition (hr_recruitment_survey/security/ir.model.access.csv:8-10; hr_recruitment_survey/security/hr_recruitment_survey_security.xml:77-114).
  - Interviewers: read responses/lines/survey/questions and send invites only where they are interviewer on the applicant or on the job (hr_recruitment_survey/security/ir.model.access.csv:12-16; hr_recruitment_survey/security/hr_recruitment_survey_security.xml:118-188). (TEST) officer and interviewer are refused until named interviewer at job or applicant level; manager may act on recruitment forms but cannot read a non-recruitment survey (hr_recruitment_survey/tests/test_recruitment_survey.py:70-87). (TEST) interviewer has no applicant access for printing; officer needs interviewer assignment (hr_recruitment_survey/tests/test_recruitment_survey.py:96-106).
- Company scoping: none added: UNKNOWN — EVIDENCE INSUFFICIENT.

## D. Handoffs to other modules
- survey: owns forms, questions, responses, invitation wizard, scoring/validity, public access flow (hr_recruitment_survey/models/survey_survey.py:7; hr_recruitment_survey/wizard/survey_invite.py:9).
- hr_recruitment: owns applicants, jobs, interviewer assignments, security groups, configuration menu and settings section (hr_recruitment_survey/views/res_config_setting_views.xml:6, 8; hr_recruitment_survey/views/survey_survey_views.xml:87).
- base contacts (res.partner): created on demand for the applicant (hr_recruitment_survey/models/hr_applicant.py:41-46).
- mail: template and chatter posting (hr_recruitment_survey/wizard/survey_invite.py:24).

## E. Configuration / defaults that change outcomes
- Job's Interview Form selection (default access mode token when creating from job) (hr_recruitment_survey/views/hr_job_views.xml:12).
- Interviewer lists on job and on applicant define who may send/read (hr_recruitment_survey/security/hr_recruitment_survey_security.xml:121-125, 149-152).
- Survey's "restricted users" list limits officers (hr_recruitment_survey/security/hr_recruitment_survey_security.xml:80-83).
- Invitation default deadline 15 days; template optional (falls back to no template if missing) (hr_recruitment_survey/models/hr_applicant.py:49-57).

## F. Effective extension path
- Modules involved: survey (forms/invites), hr_recruitment (applicants/jobs/groups), mail. Extension points: survey type list, invite wizard, response completion, retry controller.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: scoring or pass/fail effect on applicant stage (none found in this module).
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour if a job's form is changed after responses exist.
- UNKNOWN — EVIDENCE INSUFFICIENT: portal/public access risks for access_mode combinations beyond the token default.

