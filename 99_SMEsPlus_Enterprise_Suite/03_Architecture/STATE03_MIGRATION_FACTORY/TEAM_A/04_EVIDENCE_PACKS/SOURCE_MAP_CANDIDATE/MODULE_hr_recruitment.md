# Source Map (candidate) — `hr_recruitment`

> **STATUS:** CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION · source revision `19.0.post20260921` · **MODULE-LIST HASH MISMATCH — PENDING BASELINE RECONCILIATION** (module list from on-disk register; not a confirmed denominator) · not runtime proof · Community-core finding = CONDITIONAL ON EFFECTIVE INSTALLED EXTENSION SET

**Trace level:** S2-CANDIDATE (delegated trace note in section 10; not independently verified)

## 1. Identity / classification / provenance
| Field | Value |
|---|---|
| Technical name | `hr_recruitment` |
| Display name | Recruitment |
| Manifest version | 1.1 |
| License (manifest) | LGPL-3 |
| Classification | Odoo Community (Core/Optional split not assigned by this session) |
| Register group / mapping | COMM-G07 / MAPPED-CANDIDATE (register on-disk; unverified baseline) |
| Manifest sha256 (16) | `6a0a55775393c793` |
| Restricted pointer | `RESTRICTED:Odoo Community/odoo-19.0.post20260921/odoo/addons/hr_recruitment/` |
| auto_install / application | None / True |

## 2. Dependencies
- Direct dependencies (manifest): `hr`, `calendar`, `utm`, `attachment_indexation`, `web_tour`, `digest`
- Direct dependents in 300-module list (4): `hr_recruitment_skills`, `hr_recruitment_sms`, `hr_recruitment_survey`, `website_hr_recruitment`
- Direct dependents outside 300 (Community; `DISCOVERED SUPPORTING MODULE — OUTSIDE 300-MODULE DENOMINATOR` if traced) (0): —
- Custom / third-party modules that declare a dependency (name — license only) (0): —

## 3. Capabilities / functions
- Manifest category / summary: Human Resources/Recruitment / Track your recruitment pipeline
- Inventory of user-facing artifacts (counts): menu items 27, views 46, window actions 27, server actions 2, reports 0, mail templates 4, scheduled jobs 0, wizards 6, web routes 0
- Core/optional/conditional behavior and business meaning of each capability: see section 10

## 4. Business objects (neutral names) and configuration
- Objects introduced (12): `applicant.send.mail` (Send mails to applicants); `job.add.applicants` (Add applicants to a job); `talent.pool.add.applicants` (Add applicants to talent pool); `applicant.get.refuse.reason` (Get Refuse Reason); `hr.recruitment.degree` (Applicant Degree); `hr.applicant.category` (Category of applicant); `hr.recruitment.stage` (Recruitment Stages); `hr.talent.pool` (Talent Pool); `hr.applicant` (Applicant); `hr.recruitment.source` (Source of Applicants); `hr.applicant.refuse.reason` (Refuse Reason of Applicant); `hr.job.platform` (Job Platforms)
- Objects extended from other modules (26): `mail.composer.mixin`, `mail.activity.schedule`, `digest.digest`, `mail.activity.plan`, `ir.attachment`, `hr.department`, `mail.alias.mixin`, `hr.job`, `mail.activity.mixin`, `utm.source`, `ir.ui.menu`, `calendar.event`, `res.company`, `hr.employee`, `mail.thread`, `res.users`, `res.config.settings`, `utm.campaign`, `mail.thread.cc`, `mail.thread.main.attachment`, `mail.thread.blacklist`, `mail.thread.phone`, `utm.mixin`, `mail.tracking.duration.mixin`, `utm.source.mixin` … (+1)
- Company-dependent settings introduced: 0 field(s); company-consistency auto-check declared on 0 object(s)

## 5. Effective extension / override path
Objects introduced here that are extended by other modules (module names only):
- `hr.applicant` ← Community: `hr_recruitment_skills`, `hr_recruitment_sms`, `hr_recruitment_survey`, `website_hr_recruitment`; open-license custom/third-party scanned: —
- `hr.recruitment.source` ← Community: `website_hr_recruitment`; open-license custom/third-party scanned: —
- This module's own extension of other modules' objects: `mail.composer.mixin`, `mail.activity.schedule`, `digest.digest`, `mail.activity.plan`, `ir.attachment`, `hr.department`, `mail.alias.mixin`, `hr.job`, `mail.activity.mixin`, `utm.source`, `ir.ui.menu`, `calendar.event`, `res.company`, `hr.employee`, `mail.thread`, `res.users`, `res.config.settings`, `utm.campaign`, `mail.thread.cc`, `mail.thread.main.attachment`, `mail.thread.blacklist`, `mail.thread.phone`, `utm.mixin`, `mail.tracking.duration.mixin`, `utm.source.mixin` … (+1)

## 6. Actions / states / validation / automation / security
- State fields found: none detected by static scan
- Validation: 1 declarative constraint method(s), 4 database-level uniqueness/check declaration(s) (declared in code)
- Automation: no scheduled job declared
- Security: groups declared 6 (`group_hr_recruitment_interviewer`, `group_hr_recruitment_user`, `group_hr_recruitment_manager`, `group_applicant_cv_display`, `base.group_user`, `base.default_user_group`); record rules 8 (of which company-scoped by text 1); access rows 31

## 7. Cross-module handoffs
- Derived from dependents that extend this module's objects (section 5) and from declared dependencies (section 2). Business meaning of each handoff: see section 10.

## 8. Schema-only confirmation
- Module-specific schema check: **NOT PERFORMED** for this module in this round (general schema findings are in the DB-schema documents; absence of a structure is not proof of absence of a module or its effect).

## 9. Evidence level / V-level / Unknowns
- Actual V-level: **not assigned by this session** (static source evidence only; no runtime).
- Unknown / limitation: effective installed extension set; closed-license extensions; runtime configuration; residual unknowns listed in section 10.

## 10. Trace note (S2 candidate)
> Authored by a delegated read-only research sub-agent; **CLAUDE-REPORTED / PENDING INDEPENDENT VERIFICATION**. Automated check: 98 of 99 source pointers resolve to an existing file and in-range line (1 unresolved) — this checks pointer existence only, not that each line supports its claim. Limited spot verification by the session only. Treat as a research lead.

# Source Map trace note: hr_recruitment (Recruitment)

Source revision: `19.0.post20260921` (Odoo 19 Community, read-only study; neutral business language; no code copied).
Skeleton used for orientation: sourcemap/hr_recruitment.json. Pointers are `module/path:LINE`; (TEST) = derived from module tests.

## A. Capabilities / functions
- Recruitment pipeline application: job positions with a recruiter and interviewers, applications (applicants) moving through configurable stages, interviews scheduled on the calendar, refusals with reasons and optional e-mails, talent pools for candidates not tied to a job, and hand-off of a hired applicant to an employee record. Depends on hr, calendar, utm, attachment indexation, web tour and digest (hr_recruitment/__manifest__.py:11-18).
- Optional application: flagged as an application, no auto_install (hr_recruitment/__manifest__.py:52). Settings screen offers three optional add-ons: online job posting on the website, interview forms (surveys), and CV digitisation (OCR; upgrade-type option) (hr_recruitment/models/res_config_settings.py:9-11; hr_recruitment/views/res_config_settings_views.xml:12-30). The settings block is shown to recruitment administrators only (hr_recruitment/views/res_config_settings_views.xml:11).
- Auto-installed bridges in this tree: skills matching (hr_recruitment_skills, auto_install on hr_skills + hr_recruitment: hr_recruitment_skills/__manifest__.py:10, 27), SMS to applicants (hr_recruitment_sms: hr_recruitment_sms/__manifest__.py:8, 12), website careers (website_hr_recruitment, auto_install when website_mail is present: website_hr_recruitment/__manifest__.py:11, 26). Survey bridge is manual (hr_recruitment_survey/__manifest__.py:12).
- Inbound e-mail creates applications: each job position gets a mail alias whose defaults set job, department, company and recruiter (hr_recruitment/models/hr_job.py:274-285; view hr_recruitment/views/hr_job_views.xml:243-250). New mail applications start at the job's first stage (hr_recruitment/models/hr_applicant.py:951-953, 972-973; hr_recruitment/models/hr_job.py:217-222). Mail from a registered job-board sender is not linked to a contact, carries no e-mail address, and takes the candidate name from a pattern in subject/body; seeded boards: LinkedIn, Jobsdb, Indeed (hr_recruitment/models/hr_applicant.py:960-969; hr_recruitment/data/hr_recruitment_data.xml:103-121); (TEST) hr_recruitment/tests/test_recruitment_process.py:112-140.
- Sources: per-job tracked source with its own mail alias for attribution by channel (hr_recruitment/models/hr_recruitment_source.py:27-47).
- Communications: send-mail wizard to applicants (hr_recruitment/wizard/applicant_send_mail.py:20-63); stage e-mail templates posted automatically on stage entry (hr_recruitment/models/hr_applicant.py:884-898); seeded templates Refuse, Interest, Application Acknowledgement, Not interested anymore (hr_recruitment/data/mail_template_data.xml:5, 54, 143, 218).
- Reporting: analysis action, job kanban counters (new, open, hired, activities), department counters, digest KPI "New Employees" (hr_recruitment/views/menuitems.xml:50-60; hr_recruitment/models/hr_job.py:44-53; hr_recruitment/models/hr_department.py:9-35; hr_recruitment/models/digest.py:11-26; hr_recruitment/data/digest_data.xml:4-6).

## B. Business objects, relationships, lifecycle
- Objects: Job position (extends the HR job), Applicant/application, Stage, Refuse reason, Degree, Tag, Talent pool, Source, Job platform (hr_recruitment/models/hr_job.py:13; hr_recruitment/models/hr_applicant.py:24; hr_recruitment/models/hr_recruitment_stage.py:8; hr_recruitment/models/hr_applicant_refuse_reason.py:8; hr_recruitment/models/hr_talent_pool.py:8; hr_recruitment/models/hr_recruitment_source.py:8; hr_recruitment/models/hr_job_platform.py:8).
- Applicant links: contact (auto-created/updated from name, e-mail, phone: hr_recruitment/models/hr_applicant.py:234-258), job, department (defaults from job), company (from department/job, else current: :563-576), recruiter (defaults from the job: :593-596), interviewers, meetings, attachments, employee (once created), tags, talent pools (hr_recruitment/models/hr_applicant.py:43-138).
- Stage: name, sequence, optional job restriction, requirements, e-mail template, folded flag, "Hired Stage" flag, rotting threshold in days (0 disables), kanban legend labels (hr_recruitment/models/hr_recruitment_stage.py:13-36). Seeded pipeline: New (acknowledgement template), Qualification, First Interview, Second Interview, Contract Proposal, Contract Signed (folded, hired) (hr_recruitment/data/hr_recruitment_data.xml:43-69). Stages are deletion-restricted while applicants use them (hr_recruitment/models/hr_applicant.py:77).
- Status is derived: Refused (refuse reason set), Archived (inactive), Hired (hire date set), else Ongoing (hr_recruitment/models/hr_applicant.py:513-523).
- Moves: default stage is the first unfolded stage valid for the job (hr_recruitment/models/hr_applicant.py:578-591). On any stage change the previous stage, the stage-change date and a reset "In Progress" kanban state are recorded (:660-666). Entering a hired stage stamps the hire date (:603-609); it also lowers the job's open-target by one when the target is above zero, and moving back out restores it (:667-671); (TEST) hr_recruitment/tests/test_recruitment.py:275-302.
- Refuse: wizard records reason and refuse date and archives the application; optionally e-mails the applicant (needs sender and applicant addresses) and may refuse duplicate applications found by same normalised e-mail, phone or LinkedIn (hr_recruitment/wizard/applicant_refuse_reason.py:25-143). Wizard pre-fills template from the reason (hr_recruitment/wizard/applicant_refuse_reason.py:86-92). (TEST) refusing with duplicates removes the duplicate but not unrelated applicants (hr_recruitment/tests/test_recruitment.py:315-340).
- Restore/unarchive: puts the application back at the first stage and clears the refuse reason (hr_recruitment/models/hr_applicant.py:1079-1101).
- Hire: "Create Employee" button appears only for an active application that has a hire date and no employee, and only for HR officers (hr_recruitment/views/hr_applicant_views.xml:92-93). It creates the employee with name, contact, job, job title, department, private address fields from the contact, company address, work e-mail/phone defaults, links the application, and copies non-duplicate attachments (hr_recruitment/models/hr_applicant.py:1003-1058). Creation posts a "hired" log on the application (hr_recruitment/models/hr_employee.py:18-27).
- Duplicates/talent: application count matches on normalised e-mail (case-insensitive), sanitised phone and LinkedIn (hr_recruitment/models/hr_applicant.py:260-304); (TEST) hr_recruitment/tests/test_recruitment.py:39-57. Talent = a jobless copy attached to one or more pools; original applications point to it; talents cannot be duplicated and must keep at least one pool (hr_recruitment/wizard/talent_pool_add_applicants.py:23-50; hr_recruitment/models/hr_applicant.py:148-152, 711-714); (TEST) hr_recruitment/tests/test_recruitment_talent_pools.py:326-352. A talent can be turned into new applications for several jobs, each starting at that job's earliest unfolded stage (hr_recruitment/wizard/job_add_applicants.py:11-31).
- Job effects: archiving a job archives its applications (hr_recruitment/models/hr_job.py:302-303); changing the job's recruiter re-assigns ongoing applications of the previous recruiter (hr_recruitment/models/hr_job.py:310-326); hired count is derived from hire dates including archived ones (hr_recruitment/models/hr_job.py:88-101).

## C. Validations, automation, security, multi-company
- Constraints: job name unique per department and company, job target not negative (hr/models/hr_job.py:42-49); job-platform e-mail unique (hr_recruitment/models/hr_job_platform.py:17-20); a contact name is required before a contact/employee/meeting can be created from an applicant (hr_recruitment/models/hr_applicant.py:240-241, 752-753, 1009-1010); interviewers cannot create employees (hr_recruitment/models/hr_applicant.py:1060-1062); (TEST) hr_recruitment/tests/test_recruitment_interviewer.py:100-101. Seeded "Job Campaign" tracking campaign cannot be deleted and sources linked to recruitment sources cannot be deleted (hr_recruitment/models/utm_campaign.py:12-19; hr_recruitment/models/utm_source.py:13-23). Unticking "Hired" on a stage that holds hired applicants shows a warning (hr_recruitment/models/hr_recruitment_stage.py:47-54).
- Groups: Interviewer < Officer (manage all applicants) < Administrator (hr_recruitment/security/hr_recruitment_security.xml:17-38). Administrators are default members for the superuser accounts (:37). Interviewer status is granted automatically when a user is set as interviewer on a job or application and revoked when no longer needed anywhere (hr_recruitment/models/res_users.py:10-37; hr_recruitment/models/hr_job.py:292, 305-308; hr_recruitment/models/hr_applicant.py:630, 688-691); (TEST) hr_recruitment/tests/test_recruitment_interviewer.py:32-71.
- Visibility: interviewers see only applications where they are interviewer on the application or its job (rule applies to read/write only) (hr_recruitment/security/hr_recruitment_security.xml:49-60); officers see all applications, jobs, talent pools and all chatter (:62-88); (TEST) unrelated user is refused, interviewer allowed after assignment (hr_recruitment/tests/test_recruitment_interviewer.py:73-101). Interviewers receive a simplified applicant form (hr_recruitment/models/hr_applicant.py:739-744). Menus adapt to role (hr_recruitment/models/ir_ui_menu.py:9-22).
- ACL highlights: interviewers can read/write but not create/delete applicants; officers full on applicants, jobs, talent pools, degrees, refuse reasons, sources; stages are read-only for officers and full for administrators; job platforms and activity plans for administrators only (hr_recruitment/security/ir.model.access.csv:2-14, 17, 26-28). Salary proposed/expected fields and job forecast/requirement fields are limited to officers or interviewer/HR groups (hr_recruitment/models/hr_applicant.py:94-97; hr_recruitment/models/hr_job.py:33-36).
- Multi-company: global rule limits applications to allowed companies (or none) (hr_recruitment/security/hr_recruitment_security.xml:10-15); (TEST) mail applications for jobs of another company are created in that company (hr_recruitment/tests/test_recruitment_process.py:142-156). Recruiter choices are internal users belonging to the application's company (hr_recruitment/models/hr_applicant.py:86-88); (TEST) hr_recruitment/tests/test_recruitment_allowed_user_ids.py:35-70.
- Automation: assignment notifications to new interviewers (hr_recruitment/models/hr_applicant.py:636-651, 693-708); creation and stage-change message subtypes (hr_recruitment/models/hr_applicant.py:900-910); calendar meetings created from the applicant carry the applicant's attachments (hr_recruitment/models/calendar.py:35-53). Rotting (stale) highlight applies to ongoing, not-hired applications by stage threshold (hr_recruitment/models/hr_applicant.py:480-487).

## D. Accounting / payroll / analytic handoffs
- Human resources (owner: hr): the only downstream handoff is the employee record (see B). Salary proposed/expected are stored on the application for reference; they are not part of the employee creation values, and no contract/version, wage or payroll object is created by this module (hr_recruitment/models/hr_applicant.py:94-97, 1034-1058). A contract-offer step: UNKNOWN — EVIDENCE INSUFFICIENT (not in this module).
- Accounting/analytic: none. Payroll: none. Timesheets: none.
- Calendar (owner: calendar): interview events reference the applicant (hr_recruitment/models/calendar.py:33). Mail/UTM: templates, aliases, source/medium/campaign attribution (hr_recruitment/models/hr_applicant.py:121-124; hr_recruitment/models/hr_recruitment_source.py:12-17).
- Skills (owner: hr_skills): matching candidate skills to job needs lives in the auto-installed bridge; when that bridge is present, hiring copies the applicant's skills onto the new employee (hr_recruitment_skills/models/hr_applicant.py:78-89); see hr_skills note.

## E. Configuration / defaults that change outcomes
- Stage list, folded and hired flags, job-specific stages and templates decide the pipeline and the hire date (hr_recruitment/models/hr_recruitment_stage.py:15-26).
- Job recruiter defaults to the creating user, target defaults to 1, job address defaults to the last used one else company address (hr/models/hr_job.py:21-22, 24-32; hr_recruitment/models/hr_job.py:17-23).
- Seeded degrees (4), tags (4), refuse reasons (6), platforms (3), campaign (hr_recruitment/data/hr_recruitment_data.xml:5-24, 27-38, 39-41, 72-121).
- Refuse-reason template choice controls whether an e-mail is proposed (hr_recruitment/wizard/applicant_refuse_reason.py:45-49, 86-92).
- Alias domain of the company/job determines whether tracked mail aliases are available (hr_recruitment/models/hr_recruitment_source.py:19-25).
- Stage rotting threshold default 0 (off) (hr_recruitment/models/hr_recruitment_stage.py:27-28).
- Settings toggles installing website/survey/OCR modules (see A).

## F. Effective extension path (module names only)
- Extends: hr (job, employee, department), calendar (event), mail (activity plan, templates), digest, utm, res.users, base settings. Extenders of the applicant model in this tree: hr_recruitment_skills, hr_recruitment_survey, website_hr_recruitment, hr_recruitment_sms. Other dependents: website_hr_recruitment_livechat (manifest grep). Referral/OCR/other add-ons referenced in comments and settings: not in this tree (hr_recruitment/models/hr_job.py:133; hr_recruitment/models/res_config_settings.py:11).

## G. Not verified
- Contract/offer generation, e-signature and referral flows: UNKNOWN — EVIDENCE INSUFFICIENT.
- Front-end kanban behaviours, tours and static assets: UNKNOWN — EVIDENCE INSUFFICIENT.
- Content of mail templates and their language handling: UNKNOWN — EVIDENCE INSUFFICIENT.
- Whether interviewers can move stages (ACL grants write; UI restrictions not traced): UNKNOWN — EVIDENCE INSUFFICIENT.
- Revision `19.0.post20260921`; nothing asserted as universal.

