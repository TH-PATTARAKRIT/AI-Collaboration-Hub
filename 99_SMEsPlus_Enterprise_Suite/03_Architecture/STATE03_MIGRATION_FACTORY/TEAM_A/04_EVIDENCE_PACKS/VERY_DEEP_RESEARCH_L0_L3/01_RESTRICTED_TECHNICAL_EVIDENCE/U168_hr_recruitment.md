# U168 — hr_recruitment: Hiring/Applicant Workflow — RESTRICTED TECHNICAL EVIDENCE
**Unit**: U168 | **Group**: G09 | **Priority**: P2 | **Module Status**: PRESENT
**Odoo Version**: 19.0.post20260921 | **Module Version**: 1.1
**Researcher**: DeepSeek Worker | **Date**: 2026-10-02

---

## MODULE MANIFEST

**File**: `hr_recruitment/__manifest__.py`
**Category**: Human Resources/Recruitment
**Dependencies**: `hr`, `calendar`, `utm`, `attachment_indexation`, `web_tour`, `digest`
**Application**: True (standalone app, appears in app menu)
**License**: LGPL-3
**No payroll, account.analytic, or hr_payroll dependency** — Community edition is purely a recruitment pipeline tool with no compensation management.

---

## VDR CLAIMS TABLE — 22 Claims

| # | Claim ID | Boundary | Model/Object | Field/Method | Evidence Source | Certainty | L-Level | Notes |
|---|----------|----------|--------------|--------------|-----------------|-----------|---------|-------|
| 1 | U168-C01 | Module dependency | `__manifest__` | `depends` | `__manifest__.py:8-15` | HIGH | L2 | Depends on: hr, calendar, utm, attachment_indexation, web_tour, digest. No payroll/accounting dependency in Community. |
| 2 | U168-C02 | hr.applicant model | `hr.applicant` | `_inherit` | `hr_applicant.py:27-34` | HIGH | L3 | Inherits: mail.thread.cc, mail.thread.main.attachment, mail.thread.blacklist, mail.thread.phone, mail.activity.mixin, utm.mixin, mail.tracking.duration.mixin |
| 3 | U168-C03 | hr.applicant field | `hr.applicant` | `partner_name` | `hr_applicant.py:44` | HIGH | L3 | `Char("Applicant's Name")` — primary display name (`_rec_name = "partner_name"`) |
| 4 | U168-C04 | hr.applicant field | `hr.applicant` | `job_id` | `hr_applicant.py:93` | HIGH | L3 | Many2one to hr.job, domain filtered by company_id, tracked, indexed. Drives stage, department, user_id computations. |
| 5 | U168-C05 | hr.applicant field | `hr.applicant` | `stage_id` | `hr_applicant.py:77-81` | HIGH | L3 | Many2one to hr.recruitment.stage, computed via `_compute_stage`, domain: `['|', ('job_ids','=',False), ('job_ids','=',job_id)]`, ondelete='restrict', tracked, group_expand via `_read_group_stage_ids`. |
| 6 | U168-C06 | hr.applicant field | `hr.applicant` | `priority` | `hr_applicant.py:92` | HIGH | L3 | Selection field: 0=Normal, 1=Good, 2=Very Good, 3=Excellent. Default '0'. Used for kanban ordering (`_order = "priority desc, sequence, id desc"`). |
| 7 | U168-C07 | hr.applicant field | `hr.applicant` | `kanban_state` | `hr_applicant.py:107-112` | HIGH | L3 | Selection: normal(In Progress), done(Ready for Next Stage), waiting(Waiting), blocked(Blocked). Default 'normal'. Reset to 'normal' on stage change via `write()`. |
| 8 | U168-C08 | hr.applicant field | `hr.applicant` | `refuse_reason_id` | `hr_applicant.py:117` | HIGH | L3 | Many2one to hr.applicant.refuse.reason, tracked. Set by `applicant.get.refuse.reason` wizard. Drives `application_status = 'refused'`. |
| 9 | U168-C09 | Stage machine | `hr.recruitment.stage` | `job_ids` | `hr_recruitment_stage.py:20-22` | HIGH | L3 | Many2many to hr.job. `job_ids=False` means stage is global (all jobs); job_ids set = stage is job-specific. `_read_group_stage_ids` shows global + job-specific stages in kanban. |
| 10 | U168-C10 | Stage machine | `hr.recruitment.stage` | `hired_stage` | `hr_recruitment_stage.py:29-30` | HIGH | L3 | Boolean. When applicant enters a stage with hired_stage=True: `date_closed` auto-set (datetime.now), `no_of_recruitment` on hr.job decremented. Inverse: `no_of_recruitment` incremented on exit. |
| 11 | U168-C11 | Stage machine | `hr.recruitment.stage` | `template_id` | `hr_recruitment_stage.py:23-25` | HIGH | L3 | Many2one to mail.template. Auto-sends email to applicant when stage changes to this stage via `_track_template()`. |
| 12 | U168-C12 | Employee creation | `hr.applicant` | `create_employee_from_applicant()` | `hr_applicant.py:1003-1032` | HIGH | L3 | NOT named `action_get_created_employee` in Odoo 19. Creates hr.employee via `_get_employee_create_vals()`. Copies attachments. Populates name, job_id, department, work_email, work_phone, private address. Blocked for Interviewer-only users. |
| 13 | U168-C13 | Mail integration | `hr.applicant` | `message_new()` | `hr_applicant.py:943-978` | HIGH | L3 | Email gateway creates applicants from incoming email to job alias. Parses sender name/email. Detects hr.job.platform (e.g. job boards) and applies regex to extract candidate name from subject. Sets stage to first stage of the job. |
| 14 | U168-C14 | Mail integration | `hr.applicant` | `_notify_get_reply_to()` | `hr_applicant.py:912-919` | HIGH | L3 | Replies to applicant messages are directed to the job's email alias. |
| 15 | U168-C15 | Refuse workflow | `applicant.get.refuse.reason` | `action_refuse_reason_apply()` | `wizard/applicant_refuse_reason.py:90-111` | HIGH | L3 | Writes refuse_reason_id, sets active=False, sets refuse_date=now(). Optionally sends refusal email via template. Supports bulk-refuse of duplicate applications (same email/phone/linkedin). |
| 16 | U168-C16 | Refuse model | `hr.applicant.refuse.reason` | fields | `hr_applicant_refuse_reason.py:1-18` | HIGH | L3 | Fields: name (Char, required, translate), template_id (Many2one mail.template, domain model=hr.applicant), sequence (Integer), active (Boolean). |
| 17 | U168-C17 | Security | `res.groups` | Group hierarchy | `security/hr_recruitment_security.xml` | HIGH | L2 | 3 groups under "Recruitment" privilege: Interviewer (read-only access limited to assigned applicants) → Officer/group_hr_recruitment_user (all applicants) → Administrator/group_hr_recruitment_manager. Admin implied_ids includes Officer. |
| 18 | U168-C18 | Security | `ir.rule` | `hr_applicant_interviewer_rule` | `security/hr_recruitment_security.xml` | HIGH | L2 | Interviewer rule: `['\|', ('job_id.interviewer_ids','in',user.id), ('interviewer_ids','in',user.id)]`. No create/unlink rights. Officer rule: domain `[(1,'=',1)]` (all). |
| 19 | U168-C19 | Meeting integration | `hr.applicant` | `meeting_ids` | `hr_applicant.py:118` | HIGH | L3 | `One2many('calendar.event', 'applicant_id', 'Meetings')`. CalendarEvent gains `applicant_id = Many2one('hr.applicant')` FK via `models/calendar.py`. `_compute_meeting_display()` computes display text (Next Meeting / Last Meeting / 1 Meeting / No Meeting). |
| 20 | U168-C20 | hr.job fields | `hr.job` | `no_of_recruitment` | `hr/models/hr_job.py:21-22` (base); `hr_applicant.py:668-671` | HIGH | L3 | Integer "Target" in base hr module. Decremented when applicant reaches hired_stage; incremented when leaving hired_stage. DB constraint: no_of_recruitment >= 0. |
| 21 | U168-C21 | hr.job fields | `hr.job` | `no_of_hired_employee` | `hr_recruitment/models/hr_job.py` | HIGH | L3 | Computed field (stored): counts hr.applicant records with date_closed != False for this job. Includes both active and inactive applicants. |
| 22 | U168-C22 | No payroll integration | `hr_recruitment` | account.analytic / payroll | Manifest + grep of hr_applicant.py | HIGH | L3 | No account.analytic.line, no payroll/hr_payroll integration exists in Community hr_recruitment. Salary fields (salary_proposed, salary_expected as Float) exist on hr.applicant but are informational only, restricted to group_hr_recruitment_user. |

---

## ADDITIONAL TECHNICAL DETAILS

### hr.applicant — Key Computed Fields
- `application_status`: Selection (ongoing/hired/refused/archived) computed from refuse_reason_id, active, date_closed
- `day_open` / `day_close`: Float — days from create_date to date_open / date_closed
- `delay_close`: Avg days to close (stored, aggregatable)
- `application_count`: Count of applications sharing same email/phone/linkedin (duplicate detection)
- `_track_duration_field = 'stage_id'` — time in each stage is tracked via mail.tracking.duration.mixin

### Talent Pool (New in Odoo 19)
- `hr.talent.pool` model: name, company_id, pool_manager, talent_ids (M2M to hr.applicant), description, color, categ_ids
- `talent_pool_ids` on hr.applicant: M2M to hr.talent.pool
- `pool_applicant_id`: self-referential FK — canonical "talent" record for a person
- `is_pool_applicant`, `is_applicant_in_pool`: computed booleans for pool membership detection
- Indirect pool membership: applications with matching email/phone/linkedin are considered "in pool"

### Job Platform Integration
- `hr.job.platform` model: supports regex-based email parsing for job board application emails (e.g. LinkedIn, Indeed)
- `message_new()` on hr.applicant detects if incoming email is from a known platform and extracts candidate name via regex from subject

### UTM Tracking
- campaign_id, medium_id, source_id — all with `ondelete='set null'` (custom override of utm.mixin defaults)
- medium_id help text: "how the applicant has reached out, e.g. via Email, LinkedIn, Website"

### Interviewer Notifications
- On applicant create/write with interviewer_ids change: auto-notify new interviewers via `message_notify()`
- Interviewers can schedule meetings, refuse applicants, but cannot create/edit/delete applicants (no create/unlink rights)

### No state='open'/'recruit' field in Odoo 19
- Legacy Odoo state field (open/recruit toggle on hr.job) is NOT present in Odoo 19 Community
- Job "status" is implicitly tracked via application counts and no_of_recruitment target vs actuals
