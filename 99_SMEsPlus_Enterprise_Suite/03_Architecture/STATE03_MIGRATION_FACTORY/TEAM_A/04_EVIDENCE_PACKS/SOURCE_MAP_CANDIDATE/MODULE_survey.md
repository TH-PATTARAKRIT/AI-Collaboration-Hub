# Source Map (candidate) — `survey`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `survey` |
| Display name | Surveys |
| Manifest version | 3.7 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `639e58b8349cc66a` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/survey/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `auth_signup`, `http_routing`, `mail`, `web_tour`, `gamification`
- Direct dependents in 300-module list (4): `hr_recruitment_survey`, `hr_skills_survey`, `survey_crm`, `website_slides_survey`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Surveys / Send your surveys or share them live.
- Inventory of user-facing artifacts (counts): menu items 7, views 23, window actions 6, server actions 1, reports 1, mail templates 2, scheduled jobs 0, wizards 1, web routes 22
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (6): `survey.invite` (Survey Invitation Wizard); `survey.survey` (Survey); `survey.question` (Survey Question); `survey.question.answer` (Survey Label); `survey.user_input` (Survey User Input); `survey.user_input.line` (Survey User Input Line)
- Objects extended from other modules (8): `mail.composer.mixin`, `res.lang`, `ir.http`, `gamification.badge`, `mail.thread`, `mail.activity.mixin`, `gamification.challenge`, `res.partner`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `survey.invite` ← Community: `hr_recruitment_survey`; open-license custom/third-party scanned: —
- `survey.survey` ← Community: `hr_recruitment_survey`, `hr_skills_survey`, `survey_crm`, `website_slides_survey`; open-license custom/third-party scanned: —
- `survey.question` ← Community: `survey_crm`; open-license custom/third-party scanned: —
- `survey.question.answer` ← Community: `survey_crm`; open-license custom/third-party scanned: —
- `survey.user_input` ← Community: `hr_recruitment_survey`, `hr_skills_survey`, `survey_crm`, `website_slides_survey`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.composer.mixin`, `res.lang`, `ir.http`, `gamification.badge`, `mail.thread`, `mail.activity.mixin`, `gamification.challenge`, `res.partner`

## 6. Actions / states / validation / automation / security
- State fields found: `survey.user_input` → ['new', 'in_progress', 'done']
- Validation: 5 declarative constraint method(s), 21 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 1 (`base.default_user_group`); record rules 12 (of which company-scoped by text 0); access rows 22

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 69 of 69 source pointers resolve to an existing file and in-range line (0 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note — survey
Source revision: 19.0.post20260921 | Module: "Surveys" (survey/__manifest__.py:4) | version 3.7 (:5) | category Marketing/Surveys (:6) | application (:59) | LGPL-3 (:113)
Basis: static reading of the four main models, security, wizard, main and session controllers (route lists and key routines), seeds; views and demo data by file name; tests by title.
## A. Capabilities and optionality
- A1. Build surveys and quizzes, collect answers from the public, invited people or logged-in users, view statistics, print answers, run live (presentation-style) sessions, and issue certifications with optional badge. survey/__manifest__.py:8-17; survey/models/survey_survey.py:39-170
- A2. Application module (own menu "Surveys" for the Survey User group); depends on auth_signup, http_routing, mail, web_tour, gamification; no auto_install. survey/__manifest__.py:19-24,59; survey/views/survey_menus.xml:4-8
- A3. Survey types: Survey (feedback), Live session, Assessment (certification-style), Custom; selecting a type applies defaults: Survey = no scoring, no time limit, not certification; Live session = public access, no attempts/time limit, one page per question, scoring with answers, no going back; Assessment = invited-only, scoring with answers. survey/models/survey_survey.py:39-44,393-416
- A4. Conditional features: certification requires scoring; certification badge requires login required + certification; live session available only for types Live session/Custom and not certification; attempts limit meaningful only when not anonymous public access. survey/models/survey_survey.py:357-376,379-382,285-290
- A5. Sample surveys can be loaded per type. survey/models/templates/survey_survey.py:19-56,120,214,289
## B. Objects, relationships, lifecycle
- B1. Survey (survey.survey): title, type, languages (empty = all installed), responsible, optional restriction to specific users, layout (one page per question / per section / single page), question selection (all or randomized per section), progress display, access mode, login requirement, go-back option, scoring, attempts limit, time limit, certification, live-session fields, end message. survey/models/survey_survey.py:39-170
- B2. Section/page and Question share one model (survey.question, flag "is page"); a question belongs to the section that precedes it by sequence. survey/models/survey_question.py:11-33,301-314
- B3. Question types: single choice, multiple choice, multi-line text, single-line text, number, scale (0-10), date, datetime, matrix (one or many per row); options for comments, mandatory answer, length/value/date validation, time limit, save answer as respondent e-mail or nickname. survey/models/survey_question.py:87-160
- B4. Suggested answer (survey.question.answer): text and/or image, correct flag, score (matrix rows/columns also use it). survey/models/survey_question.py:835-870
- B5. Response header (survey.user_input): survey, respondent (partner/e-mail/nickname), access token, invite token, state New / In Progress / Completed, start/end, deadline, language, test flag, predefined question list, score, pass flag, session flag. survey/models/survey_user_input.py:20-64
- B6. Response line (survey.user_input.line): one answer to one question (typed value or chosen suggestion), skipped flag, computed score and correctness. survey/models/survey_user_input.py:693-756
- B7. Conditional questions: a question can be triggered by chosen answers of earlier single/multiple-choice questions; invalid triggers hide the question; inactive questions' answers are cleared. survey/models/survey_question.py:171-182; survey/models/survey_survey.py:716-743; survey/models/survey_user_input.py:572-603
- B8. Response lifecycle: created at start (New) -> first page shown (In Progress, start time) -> submitted page by page -> Completed on last page or time out; on completion followers of the survey are notified, a certification e-mail is sent on success, badge goals refreshed. survey/models/survey_user_input.py:229-267; survey/controllers/main.py:490-605
- B9. Live session lifecycle: survey session state Ready -> In Progress -> ended; ending marks all responses Completed and notifies participants via the bus. survey/models/survey_survey.py:1139-1175
- B10. Extended objects: badge and challenge (certification category) from gamification, partner certification counters, language deactivation guard. survey/models/badge.py:7-16; survey/models/challenge.py:7-12; survey/models/res_partner.py:7-32; survey/models/res_lang.py:10-27
## C. Validations, constraints, automation, security
- C1. Database-level checks on survey: unique access token and session code; certification only with scoring; pass mark between 0 and 100; positive time limit if time-limited; positive attempts if limited; one badge per survey; speed reward needs positive time limit. survey/models/survey_survey.py:173-205
- C2. Scoring after each page cannot be combined with going back. survey/models/survey_survey.py:437-445
- C3. A restricted survey's responsible must still have access. survey/models/survey_survey.py:447-463
- C4. Question checks: length, value, date ranges consistent; score not negative; scored date/datetime need a correct answer; scale range 0-10 increasing; time-limited needs positive limit; pages have no question type. survey/models/survey_question.py:184-232,234-237
- C5. Sending/opening rules ("check validity"): survey must have questions; scored survey must offer positive points; per-section layout needs non-empty sections; survey must be active. survey/models/survey_survey.py:1024-1042
- C6. Answer-creation rules: test entries need read access; closed surveys refuse tokens; attempts left checked; the code also references access modes "authentication" and "internal" although the field only offers Public and Invited-only in this revision. survey/models/survey_survey.py:92-95,597-619 — effect of the leftover branches UNKNOWN — EVIDENCE INSUFFICIENT.
- C7. Runtime access checks on the public route: unknown survey/token, login required for public user, closed survey, void survey, past deadline, respondent mismatch; invited-only survey needs a token. survey/controllers/main.py:45-96
- C8. Submission safeguards: completed responses refuse further input; attempts recounted at submit; timer cheating guard (10 s survey / 3 s question grace); page-by-page validation returns per-question errors. survey/controllers/main.py:521-571
- C9. Answer validation per type (email format, text length, numeric range, date range, mandatory, matrix, scale, choices). survey/models/survey_question.py:450-567
- C10. Scoring: choice questions use suggestion scores; number/date/datetime score when equal to the correct value; total possible score sums positive scores; pass when percentage reaches required score; live-session speed reward halves then scales points after 2 seconds. survey/models/survey_user_input.py:67-91,758-816
- C11. Attempts: counted per partner or e-mail and invite token among completed non-test responses; limit applies only when access is invited-only or login is required. survey/models/survey_survey.py:667-698
- C12. Groups: Survey User and Survey Administrator (Administrator implies User; administrators and root by default). survey/security/survey_security.xml:11-24
- C13. ACLs: no rights for other internal or anonymous users on surveys, questions, answers, responses; Survey User full on survey, question, suggested answer, response; response lines read-only for User, full for Administrator; invites read/write/create; Survey User may edit badges. survey/security/ir.model.access.csv:2-23
- C14. Record rules: Administrator sees all surveys; User sees surveys with no restricted-user list or where they are listed (same for questions, answers, invites, responses and lines); responses/lines rules limit to the four non-specialised survey types. survey/security/survey_security.xml:27-172
- C15. Public access is by token URLs with server-side elevated access after validity checks; results, test, print-preview and certification pages require login. survey/controllers/main.py:156,209,662,686,704,731; survey/controllers/survey_session_manage.py:39-166
- C16. Live-session management restricted to Survey Users; anyone can join with a numeric session code (4 to 9 digits, unique). survey/models/survey_survey.py:1139-1175,1284-1309; survey/controllers/survey_session_manage.py:166-192
- C17. Certification document download requires the caller's own passed response. survey/controllers/main.py:704-729
- C18. Company scoping: no company field on any survey object and no multi-company rules. survey/models/survey_survey.py:39-170 (no company_id); UNKNOWN — EVIDENCE INSUFFICIENT for how e-mail sender company is chosen.
- C19. External service implications: invitations and certification e-mails go through the database mail server; optional live sessions use the bus. survey/wizard/survey_invite.py:223-255; survey/models/survey_survey.py:1174
- C20. Invite wizard: needs at least one valid recipient; when login is required, external e-mails are refused unless signup allowed; resend re-uses the latest response per recipient; each recipient gets a personal token and optional deadline; sender e-mail must exist. survey/wizard/survey_invite.py:113-143,180-286
- C21. Respondent cookie keeps the answer token for one day. survey/controllers/main.py:248-251
- C22. Cannot delete questions of a survey while its live session is in progress. survey/models/survey_question.py:437-445
- C23. Certification badge automation: enabling creates a goal (count of passed responses per partner) and a once-only challenge granting the badge; disabling archives the badge and deletes challenge/goals; archiving a survey archives its badge. survey/models/survey_survey.py:1230-1282,523-530
## D. Handoffs
- D1. Badges, goals, challenges (karma > 0 required in challenge scope): gamification. survey/models/survey_survey.py:1230-1262
- D2. E-mail invitations and certification mail: mail (templates "Survey: Invite" and "Survey: Certification Success"). survey/data/mail_template_data.xml:4-5,49-50
- D3. Sign-up policy for external respondents: auth_signup. survey/models/survey_survey.py:225-228
- D4. Lead generation from answers (answer/question flags, team, lead origin survey): survey_crm (auto_install bridge with crm). survey_crm/models/survey_question_answer.py:7; survey_crm/models/crm_lead.py:8; survey_crm/__manifest__.py
- D5. Recruitment interview forms per job/applicant: hr_recruitment_survey. hr_recruitment_survey/models/hr_job.py:9-23
- D6. Skills/resume line from passed certification: hr_skills_survey (auto_install). hr_skills_survey/models/survey_user.py:11-36; hr_skills_survey/__manifest__.py:15,21
- D7. E-learning certification slides: website_slides_survey (auto_install; a certification slide must have a survey). website_slides_survey/models/slide_slide.py:55-61; website_slides_survey/__manifest__.py:9,11
- D8. Frontend routing/language handling: http_routing and survey language guard. survey/models/ir_http.py:24-37
- D9. No accounting entries or stock effects.
## E. Configuration that changes outcomes
- E1. Access mode (anyone with link / invited only), login required, go back, attempts limit, time limit, pagination and question selection. survey/models/survey_survey.py:75-124
- E2. Scoring type (none / with answers after each page / with answers at end / without answers) and required score (default 80%). survey/models/survey_survey.py:108-114
- E3. Survey languages restrict which languages may be used; deactivating a language used by a survey is blocked or unlinks it. survey/models/res_lang.py:10-27
- E4. Sections with "random questions count" in randomized mode. survey/models/survey_question.py:82-86; survey/models/survey_survey.py:621-645
- E5. Restricted-users list narrows Survey User visibility. survey/security/survey_security.xml:38-48
## F. Extension path (module names)
- survey_crm, hr_recruitment_survey, hr_skills_survey, website_slides_survey (all depend on survey). Front-end/website integration of surveys is inside this module (routes in survey/controllers).
## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: statistics/report computation details, print and certification PDF layouts (survey/views/survey_templates_statistics.xml, survey/report not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: front-end script behaviour (survey/static/src not read).
- UNKNOWN — EVIDENCE INSUFFICIENT: data retention or anonymisation of responses (no purge job found in read files).
- UNKNOWN — EVIDENCE INSUFFICIENT: effect of the "authentication"/"internal" access-mode branches (see C6).

