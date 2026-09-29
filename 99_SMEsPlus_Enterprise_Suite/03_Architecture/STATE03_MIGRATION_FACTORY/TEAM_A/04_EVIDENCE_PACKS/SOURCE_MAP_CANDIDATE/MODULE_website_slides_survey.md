# Source Map (candidate) — `website_slides_survey`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `website_slides_survey` |
| Display name | Course Certifications |
| Manifest version | 1.0 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G08 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `bf684858c8a75313` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/website_slides_survey/` |
| auto_install / application | True / None |

## 2. Dependencies
- Direct dependencies (manifest): `website_slides`, `survey`
- Direct dependents in 300-module list (0): —
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (1): `test_website_slides_full`
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Website/eLearning / Add certification capabilities to your courses
- Inventory of user-facing artifacts (counts): menu items 1, views 12, window actions 2, server actions 0, reports 0, mail templates 1, scheduled jobs 0, wizards 0, web routes 2
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (0): —
- Objects extended from other modules (6): `slide.slide.partner`, `slide.slide`, `slide.channel.partner`, `slide.channel`, `survey.user_input`, `survey.survey`
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
- No direct extension (`_inherit`) of this module's own objects found in Community modules or in open-license custom/third-party modules scanned (`ABSENCE`; text-pattern scan, not MRO analysis; closed-license modules not readable). NOTE: modules listed as dependents in section 2 may still hook into behavior through other modules' objects — dependency is not the same as extension.
- This module's own extension of other modules' objects: `slide.slide.partner`, `slide.slide`, `slide.channel.partner`, `slide.channel`, `survey.user_input`, `survey.survey`

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 0 declarative constraint method(s), 2 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 0 (—); record rules 5 (of which company-scoped by text 0); access rows 5

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 45 of 46 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: website_slides_survey (Course Certifications)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/website_slides_survey.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests. Manifest summary: adds certification capabilities (graded surveys) to eLearning courses (website_slides_survey/__manifest__.py:4-5).

## A. Capabilities / functions
- Conditional: depends on website_slides and survey with `auto_install` (website_slides_survey/__manifest__.py:11, 13); also selectable via a settings toggle (website_slides_survey/views/res_config_settings_views.xml). Uninstalling neutralises the certification badge goal (website_slides_survey/__init__.py:7-10).
- Core: a new lesson kind "Certification" linked to a survey; it has a trophy icon, is never a free preview, and cannot be marked complete by hand (website_slides_survey/models/slide_slide.py:49-79, 87-98; website_slides_survey/controllers/slides.py:85-88).
- Core: participants launch the certification from the lesson; the system creates or reuses the person's attempt: members get an attempt tied to their membership, non-members get a test attempt (website_slides_survey/models/slide_slide.py:132-171; website_slides_survey/controllers/slides.py:18-29).
- Core: from the course page, an authorised teacher can create a new certification survey with default settings or link an existing one (website_slides_survey/controllers/slides.py:31-37, 43-81).
- Core: success on the survey completes the lesson and, through completion recomputation, marks the member as "Certified" for the course; course shows number of certifications and certified attendees, with a shortcut list (website_slides_survey/models/slide_slide.py:11-42; website_slides_survey/models/slide_channel.py:12-54).
- Core: failing the last allowed attempt removes the person from the course and sends an email suggesting re-enrolment (website_slides_survey/models/survey_user.py:27-63; website_slides_survey/data/mail_template_data.xml:4).
- Core: certification badge is published by default; certification badges and courses appear in a separate section of the ranks/badges page; profile shows certification attempts; user list shows certification counts (website_slides_survey/data/gamification_data.xml:3-11; website_slides_survey/controllers/slides.py:97-163; website_slides_survey/controllers/website_profile.py:9-37).
- Core: survey end-page and retry keep the course context (website_slides_survey/controllers/survey.py:7-22).
- Backend: survey form shows linked courses; menus/views for certifications, attempts and members (website_slides_survey/models/survey_survey.py:13-67; website_slides_survey/views/website_slides_menu_views.xml).

## B. Business objects, relationships, lifecycle
- Lesson (slide.slide, owned by website_slides) 0..1 -> survey (survey.survey, owned by survey); member progress row (slide.slide.partner) 1..n -> survey attempts (survey.user_input) (website_slides_survey/models/slide_slide.py:10, 55; website_slides_survey/models/survey_user.py:9-13).
- Lifecycle of an attempt: created on first view of the lesson by a member (TEST) (website_slides_survey/tests/test_course_certification_failure.py, assertion "user input created automatically upon slide view") -> answered -> pass (lesson completed, certified flag set) or fail with attempts left (stays a member) or fail with none left (membership removed, email sent) -> re-enrolment starts a new pool of attempts (attempt counters restart) (TEST) (website_slides_survey/tests/test_course_certification_failure.py:60-120 assertions on membership archived/unarchived and attempt numbering).
- When a person leaves a course, past attempts are detached from the membership so attempts allowed are counted only from the latest enrolment (website_slides_survey/models/slide_channel.py:22-36).
- Badge/challenge category of the certification badge switches between "certification" and "slides" depending on whether a course lesson uses the survey (website_slides_survey/models/slide_slide.py:121-130; website_slides_survey/models/survey_survey.py:73-75).

## C. Validations, automation, security, multi-company
- A certification lesson must have a survey and can never be a preview (database checks) (website_slides_survey/models/slide_slide.py:60-67).
- A survey used as a course certification cannot be deleted; message lists the courses (TEST) (website_slides_survey/models/survey_survey.py:28-45; website_slides_survey/tests/test_course_certification_unlink.py:18-41).
- Creating a survey from a course requires survey create right; linking an existing one requires read access to it; otherwise an error is returned and no lesson is made (website_slides_survey/controllers/slides.py:48-71).
- Certification routes require a logged-in user (website_slides_survey/controllers/slides.py:18, 31); unknown or inaccessible lessons give not-found (website_slides_survey/controllers/slides.py:20-28).
- Access: eLearning officers get read-only access to surveys, questions, answers, attempts and lines, restricted by record rules to certification surveys (website_slides_survey/security/ir.model.access.csv:2-6; website_slides_survey/security/website_slides_survey_security.xml:6-73). The rule conditions beyond the certification flag are not extracted here: UNKNOWN — EVIDENCE INSUFFICIENT.
- Profile certification tab is shown only to the user themself or to survey managers; attempts are found by contact or by email (website_slides_survey/controllers/website_profile.py:12-27). Certificate counts for the leaderboard use elevated reads and count only fully successful ones (website_slides_survey/controllers/slides.py:115-128).
- Automated notification uses the standard light mail layout (website_slides_survey/models/survey_user.py:51-53).
- Multi-company/website: no dedicated scoping; inherits course and survey scoping. Tests for failure flow, stats, unlink exist (TEST) (website_slides_survey/tests/test_course_certification_failure.py:8; website_slides_survey/tests/test_course_certification_stats.py:48; website_slides_survey/tests/test_course_certification_unlink.py:18).

## D. Handoffs to other modules
- website_slides (owner of courses, lessons, membership, profile hooks); survey (owner of surveys, attempts, scoring, certificate email/badge, attempt limits); gamification (badge/challenge) ; website_profile (profile pages); mail (failure email).
- Payment/enrolment for paid courses is website_sale_slides; certification re-purchase intent is documented in the code comment (website_slides_survey/models/survey_user.py:33-35).

## E. Configuration / defaults that change outcomes
- Default survey created from a course: one question per page, 1 attempt, not time-limited, scoring without answers shown, certification on, pass mark 70 %, standard certification email template (website_slides_survey/controllers/slides.py:54-64).
- Attempt limit and pass mark on the survey decide whether a failure removes the member (website_slides_survey/models/survey_user.py:47-49; TEST attempts limit 2 and pass mark 100 in test data (website_slides_survey/tests/test_course_certification_failure.py:10-19)).
- Certification badge visibility (published) and goal definition come from data (website_slides_survey/data/gamification_data.xml).

## F. Effective extension path (module names only)
- survey.survey: hr_recruitment_survey, hr_skills_survey, survey, survey_crm, website_slides_survey. survey.user_input: hr_recruitment_survey, hr_skills_survey, survey_crm, website_slides_survey. slide.slide and slide.slide.partner: website_slides_survey (in this tree). slide.channel.partner: hr_skills_slides, website_slides_survey. slide.channel: hr_skills_slides, mass_mailing_slides, website_sale_slides, website_slides_forum, website_slides_survey.

## G. Not verified
- Certificate PDF generation and email content: UNKNOWN — EVIDENCE INSUFFICIENT (owned by survey).
- Behaviour with several certifications in one course beyond the tests listed: UNKNOWN — EVIDENCE INSUFFICIENT.

