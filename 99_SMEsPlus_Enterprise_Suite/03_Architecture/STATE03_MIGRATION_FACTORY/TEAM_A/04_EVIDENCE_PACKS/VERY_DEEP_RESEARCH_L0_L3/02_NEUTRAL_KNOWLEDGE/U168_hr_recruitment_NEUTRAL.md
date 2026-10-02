# U168 — hr_recruitment: Hiring/Applicant Workflow — NEUTRAL KNOWLEDGE
**Unit**: U168 | **Group**: G09 | **Priority**: P2 | **Module Status**: PRESENT
**Odoo Version**: 19.0 Community | **Date**: 2026-10-02

---

## PURPOSE SUMMARY

The recruitment module manages the full lifecycle of attracting and evaluating job candidates. It provides a pipeline view where applicants move through configurable stages, from initial application through interviews to a final hiring decision. The module connects with the calendar system for interview scheduling, the email system for candidate communications, and the employee module when a successful candidate is converted to a staff record.

---

## NEUTRAL CLAIMS (22)

| # | Claim ID | Boundary | Plain-Language Description |
|---|----------|----------|---------------------------|
| 1 | U168-N01 | Module scope | The recruitment module depends on the base human-resources module, the calendar module for meeting scheduling, and the UTM tracking framework for source attribution. It does not depend on payroll or accounting modules; salary figures stored on application records are informational only. |
| 2 | U168-N02 | Applicant record | Each applicant record carries the candidate's display name as its primary identifier, not a system-generated code. The name is also used as the email reply-to label when the system communicates with the candidate. |
| 3 | U168-N03 | Applicant record | An applicant must be linked to a job position. The job position drives the applicant's default department, the responsible recruiter, and which pipeline stages appear in the kanban board for that record. |
| 4 | U168-N04 | Pipeline stages | Pipeline stages can be defined as globally available (visible for all job positions) or job-specific (visible only for designated jobs). When an applicant's job position is set, the system shows only that job's specific stages plus any globally shared stages. |
| 5 | U168-N05 | Applicant rating | Each applicant can be rated on a four-level scale: Normal, Good, Very Good, or Excellent. Higher-rated applicants appear first within the same kanban column. |
| 6 | U168-N06 | Kanban progress state | Independently of pipeline stage, each applicant carries a progress indicator: In Progress, Ready for Next Stage, Waiting, or Blocked. This indicator resets to "In Progress" whenever the applicant moves to a different pipeline stage. |
| 7 | U168-N07 | Hired stage | Each pipeline stage can be marked as the "hired" stage. When an applicant reaches such a stage, the system automatically records a hire date and decrements the job position's open recruitment target by one. Moving an applicant back out of a hired stage reverses this decrement. |
| 8 | U168-N08 | Recruitment target | Each job position carries a numeric target indicating how many new hires are expected. This target is defined in the core human-resources module and decremented by the recruitment module as applicants reach the hired stage. A database constraint prevents the target from going negative. |
| 9 | U168-N09 | Hired employee count | The job position also maintains a computed count of all applicants who received a hire date, covering both currently active and archived applicant records. This count is stored and updates automatically. |
| 10 | U168-N10 | Employee conversion | A recruiter can convert an accepted applicant into a full employee record. The conversion copies the candidate's personal contact details, links the new employee to the same job and department, and transfers attachments (such as a CV) from the applicant record to the employee record. This action is blocked for users with only interviewer-level access. |
| 11 | U168-N11 | Email-to-applicant gateway | Each job position has an email alias. Emails sent to that alias automatically create a new applicant record. The system parses the sender's name and email address to populate the candidate's contact details, and places the new applicant at the first pipeline stage for that job. |
| 12 | U168-N12 | Job board platform parsing | The module can be configured with job board email addresses (such as those used by LinkedIn or Indeed). When an application email arrives from a recognised job board address, the system applies a regular expression to the email subject or body to extract the actual candidate's name, rather than treating the job board as the applicant. |
| 13 | U168-N13 | Candidate communication | Applicant records participate fully in the email chatter system. Replies to messages posted on an applicant are automatically routed back through the job position's email alias, so the conversation thread is maintained centrally on the applicant record. |
| 14 | U168-N14 | Stage-triggered email | Each pipeline stage can have an email template attached. When an applicant is moved into that stage, the system automatically sends the templated message to the candidate. |
| 15 | U168-N15 | Refusal workflow | To refuse an applicant, a recruiter opens a wizard that requires selecting a refuse reason. The wizard optionally sends a refusal email to the candidate using a template associated with the refuse reason. On confirmation, the applicant record is archived and the refusal reason and date are recorded. |
| 16 | U168-N16 | Refuse reason configuration | Refuse reasons are configurable records with a name, an optional email template, and a display order. They can be archived when no longer relevant. |
| 17 | U168-N17 | Duplicate refusal | When refusing an applicant, the recruiter is shown a count of other active applications from the same person (matched by email address, phone number, or LinkedIn profile). The recruiter can choose to refuse all of those duplicate applications in the same action, with an automatic note linking each duplicate to the original. |
| 18 | U168-N18 | Security model | Access is divided into three privilege levels. Interviewers can view and interact with applicants in jobs or applications where they are named, and can refuse applicants and schedule meetings, but cannot create or delete applicant records. Officers can see and manage all applicants. Administrators inherit officer rights and can additionally configure activity plans for the recruitment process. |
| 19 | U168-N19 | Meeting scheduling | Applicant records are linked to calendar meetings. The applicant form shows a summary of upcoming or past meetings and provides a button to schedule a new meeting. When a meeting is created from an applicant, applicant attachments are copied to the meeting for easy access during the interview. |
| 20 | U168-N20 | UTM source tracking | Every applicant record carries optional attribution fields for the marketing campaign, medium, and source that generated the application. These fields are cleared automatically if the related campaign, medium, or source record is deleted. |
| 21 | U168-N21 | Talent pool | The module introduces a talent pool concept where applicant records can be grouped into named pools for future consideration. An applicant is considered to belong to a pool if they are directly linked to it or if another application from the same email address, phone number, or LinkedIn profile is linked. |
| 22 | U168-N22 | No payroll or analytic integration | In the Community edition, the recruitment module has no connection to payroll processing or financial cost tracking. The salary expectation and proposal fields on applicant records are informational text fields visible only to recruitment officers, with no feed into any payslip or accounting entry. |

---

## MIGRATION IMPACT NOTES

1. **State field removed**: Odoo 19 Community does not expose a `state` field (open/recruit) on hr.job as existed in older versions. If migrating from Odoo 14/16, any customisation referencing `hr.job.state` must be replaced with application count or hired_stage logic.

2. **Employee creation method renamed**: The method previously known as `action_get_created_employee()` is `create_employee_from_applicant()` in Odoo 19. Any button XML or controller reference must be updated.

3. **Talent pool is new**: `hr.talent.pool`, `pool_applicant_id`, `is_pool_applicant`, and related fields are new in Odoo 19 and do not exist in earlier versions. If migrating data, these can be ignored unless the new feature is adopted.

4. **Kanban state expanded**: The kanban_state selection now includes a `waiting` value in addition to the older normal/done/blocked values.

5. **Salary fields are floats**: `salary_proposed` and `salary_expected` are stored Float fields (with avg aggregation); `salary_proposed_extra` and `salary_expected_extra` are Char fields for free-text benefit descriptions.
