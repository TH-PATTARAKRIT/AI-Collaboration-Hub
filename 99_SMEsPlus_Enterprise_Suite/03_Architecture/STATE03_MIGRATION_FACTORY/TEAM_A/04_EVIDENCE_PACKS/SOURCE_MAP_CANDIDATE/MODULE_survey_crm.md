# Source Map (candidate) — `survey_crm`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `survey_crm` |
| Display name | Survey CRM |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G09 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `a21f568fb37e32da` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/survey_crm/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `survey`, `crm`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Marketing/Surveys / Generate leads from surveys
- Inventory of user-facing artifacts (counts): menu items 0, views 4, window actions 0, server actions 0, reports 0, mail templates 0, scheduled jobs 0, wizards 0, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (6): `crm.team`, `survey.survey`, `survey.question`, `survey.user_input`, `crm.lead`, `survey.question.answer`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `crm.team`, `survey.survey`, `survey.question`, `survey.user_input`, `crm.lead`, `survey.question.answer`

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
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 42 of 43 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: survey_crm (Survey CRM)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/survey_crm.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Bridge between Survey and CRM: a survey submission can create a CRM opportunity when the participant picks an answer flagged as "lead creating" (survey_crm/__manifest__.py:5-10).
- Depends on survey and crm; `auto_install` true, so it activates automatically when both are installed (survey_crm/__manifest__.py:11,21).
- Flag on each suggested answer ("Lead creation") decides whether choosing it creates a lead (survey_crm/models/survey_question_answer.py:7).
- Question-level and survey-level "lead generating" indicators are computed: a question qualifies if it is single-choice, multiple-choice or matrix and has at least one flagged answer (survey_crm/models/survey_question.py:12-16); a survey qualifies if its type is survey, live session or custom and any question qualifies (survey_crm/models/survey_survey.py:16-20).
- Surveys get a sales team to assign leads to, a lead counter and a shortcut to see the leads created (survey_crm/models/survey_survey.py:10-14, 42-51).
- A "Lead Qualification" starter template is added to the survey template picker (email question, then key-answer questions) (survey_crm/models/templates/survey_survey.py:8-17, 25-33).
- Conditional: nothing happens unless at least one answer is flagged; the "Create Leads" column only shows for survey types survey, live session, custom (survey_crm/views/survey_question_views.xml:11). Other survey types (e.g. assessments) do not create leads: see filter (survey_crm/models/survey_user_input.py:25-27).

## B. Business objects, relationships, lifecycle
- Survey response (survey) keeps a link to at most one lead (survey_crm/models/survey_user_input.py:9).
- Lead carries its originating survey; if the survey is deleted the link is cleared, not the lead (survey_crm/models/crm_lead.py:8).
- Sales team lists the surveys assigned to it (survey_crm/models/crm_team.py:8-10). Survey's team link is cleared if the team is deleted (survey_crm/models/survey_survey.py:12-14).
- Lifecycle: on completion of a response, leads are created for responses that chose flagged answers (survey_crm/models/survey_user_input.py:11-28, 30-46). For live/custom sessions, completion of the session creates leads for responses received since the session start (survey_crm/models/survey_survey.py:34-40).
- Lead created is always of "opportunity" type, assumed sufficiently qualified (survey_crm/models/survey_user_input.py:65).
- Lead title uses participant name (partner, nickname, email, or "New") and "survey" or "live session" (survey_crm/models/survey_user_input.py:74-80). Lead description is a formatted list of question/answer pairs, skipped questions marked (survey_crm/models/survey_user_input.py:97-216).
- Lead is tied to the known contact if the response has an active partner; otherwise the email answer (email-validated text question) is stored as the lead email (survey_crm/models/survey_user_input.py:88-93, 147-148). Nickname question fills the contact name (survey_crm/models/survey_user_input.py:145-146, 78).
- Lead is tagged with medium "Survey" and a source named after the survey title (survey_crm/models/survey_user_input.py:61-63).
- (TEST) Logged-in participant: lead linked to their partner; anonymous participant: no partner, email taken from the answer (survey_crm/tests/test_survey_crm.py:116,120).

## C. Validations, automation, security, multi-company
- Automation: lead creation is triggered by response completion (not during answering) and by ending a live session (survey_crm/models/survey_user_input.py:22-28; survey_crm/models/survey_survey.py:34-40). Comment explains the two paths are deliberately separate (survey_crm/models/survey_user_input.py:12-20).
- Lead creation runs with elevated rights, so public/portal participants and session-ending users without CRM access still produce leads (survey_crm/models/survey_user_input.py:44, 53-54).
- Salesperson assignment: survey responsible if a member of the assigned team; else team leader; else none (survey_crm/models/survey_user_input.py:51-58). (TEST) team case: responsible assigned; no team, none (survey_crm/tests/test_survey_crm.py:117).
- Lead counter only computed for users with read access to leads, else zero (survey_crm/models/survey_survey.py:25,32).
- Security UI: "Leads" stat button visible only to the sales salesperson group (survey_crm/views/survey_survey_views.xml:12). The "see leads" action opens the lead list restricted to this survey with manual creation disabled (survey_crm/models/survey_survey.py:45-51).
- No new access-control entries, groups or record rules (skeleton "access": [], "rules": []; no security folder in manifest survey_crm/__manifest__.py:12-16).
- Company scoping: no company field added; lead created without an explicit company: UNKNOWN — EVIDENCE INSUFFICIENT for combined multi-company behaviour.

## D. Handoffs to other modules
- survey: owns surveys, questions, answers, responses, completion flow, template picker (extended at survey_crm/models/survey_survey.py:7, survey_crm/models/survey_user_input.py:7).
- crm: owns leads/opportunities, sales teams, lead list action (survey_crm/models/survey_survey.py:45; survey_crm/models/survey_user_input.py:221).
- utm (via crm): owns medium and source records reused for lead attribution (survey_crm/models/survey_user_input.py:61-63).
- No accounting, sale or mail-plugin handoff in this module.

## E. Configuration / defaults that change outcomes
- Per answer: lead creation flag (default off) (survey_crm/models/survey_question_answer.py:7).
- Per survey: assigned sales team (only shown when the survey is lead generating) and survey type (survey_crm/views/survey_survey_views.xml:22).
- Lead-qualification template defaults: type survey, one question per page, progression by number (survey_crm/models/templates/survey_survey.py:27-31).
- Demo data provides a lead qualification survey and sample answers (survey_crm/__manifest__.py:17-20).

## F. Effective extension path
- Modules involved: survey (base flows), crm (lead, team), utm (attribution). Extension points used: response completion, session end, template picker, survey/question/answer forms.

## G. Not verified
- UNKNOWN — EVIDENCE INSUFFICIENT: behaviour of the "Create Leads" flag for answers on question types other than choice/matrix (computed indicator only lists those types; answer flag itself is unrestricted, survey_crm/models/survey_question_answer.py:7).
- UNKNOWN — EVIDENCE INSUFFICIENT: duplicate-lead protection if the same response is completed twice.
- UNKNOWN — EVIDENCE INSUFFICIENT: multi-company assignment of created leads.

