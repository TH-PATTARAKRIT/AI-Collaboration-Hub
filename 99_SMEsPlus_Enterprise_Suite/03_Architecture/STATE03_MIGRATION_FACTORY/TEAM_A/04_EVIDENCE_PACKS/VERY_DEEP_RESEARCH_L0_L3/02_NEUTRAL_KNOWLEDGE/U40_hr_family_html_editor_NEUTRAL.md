# U40 hr_family_html_editor — NEUTRAL KNOWLEDGE

> Status: **DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**. Source product: Odoo 19 Community (named once here only).
> Clean-room layer: plain business statements about what the system must do and why. No vendor structure, names, paths or code. Personal data is described by structure and rule only.

## CAP-U40-01 Time-off request lifecycle, approval and calendar effect

### WHAT
- No statement was identified in the source studied for this heading.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-001] Duration is computed from the employee's working schedule and the type's counting unit: whole-day types round up, half-day types count halves, hour types use the chosen hours, flexible-schedule employees use the raw time span, and public holidays are either excluded or included according to a type setting; the computed duration is the figure charged to the balance.
- [N-U40-002] An employee cannot hold two open requests that overlap in time, unless the type is explicitly flagged to allow requests on top; the user sees a warning listing the conflicting periods and the save is refused.
- [N-U40-003] For types that need an allocation, a request is accepted only if the employee's allocation covers it, allowing a configured negative margin where the type permits; cancellations and refusals are never blocked by the balance check.
- [N-U40-004] Approval depends on the type's validation mode: none (approved at creation), by the employee's approver, by a time-off officer, or by both in two steps. The first approver and second approver are recorded, nobody may give a first approval unless they are the employee's approver, and the second step requires officer rights.
- [N-U40-005] An employee cancels an approved or refused request through a dialog that asks for a reason; the reason is recorded and the relevant approver is informed according to the validation mode; cancelling frees the balance, removes the calendar entry and archives the event.
- [N-U40-006] A request can be split around a date interval into up to two requests that keep the original state, used when an employee leaves, when bulk absences are created or when a working schedule changes.
- [N-U40-007] A request can be refused from to-approve, second approval or approved; refusing notifies the employee and, for requests already validated by the first step, the approver, and archives the calendar event.
- [N-U40-008] Each employee has a time-off approver, by default the manager's user; changing the manager moves the approver only if it followed the manager; the approver user receives the responsible role automatically and loses it when no longer anyone's approver; changes of manager or department flow to pending requests and allocations.
- [N-U40-009] Mandatory days are company-wide or restricted by schedule, department hierarchy and job position; the calendar shows them with colour and public holidays alongside, and ordinary employees cannot request time off on them.

### STATE
- [N-U40-010] A time-off request moves through to-approve, second approval, approved, refused and cancelled; the allowed moves depend on who acts (the employee, the employee's approver, or a time-off officer), on the type's validation mode and on whether the start date has passed. Resetting a request to to-approve is not offered to ordinary users; they must cancel or delete and create a new request.
- [N-U40-011] An employee counts as absent today only while an approved request of an absence-kind type covers the current moment; the return date is the next working moment, and chat presence indicators and employee cards show on-leave variants.

### OPTIONALITY
- [N-U40-012] A daily scheduled job checks requests starting within the next month that draw on accrual-based allocations and cancels those whose accrued balance no longer covers them, with an internal note giving the reason.
- [N-U40-013] When creating a request the first type that needs no allocation or has a valid one is proposed, and changing the employee clears a type the new employee cannot use.

### DEPENDENCY
- [N-U40-014] Approving a request creates an absence entry in the resource calendar (and, when the type asks for it, a confidential calendar event); moving the request out of the approved state, changing its dates, or deleting it removes or rewrites that entry so planning, work entries and balances stay consistent.
- [N-U40-015] Creating or advancing a request schedules approval tasks for the responsible approver (the employee's approver, else the employee's manager, else the type's officers), with a deadline before the start date, notifies the employee on approval or refusal, and clears tasks once decided.

### CONSTRAINT
- [N-U40-016] A request must have a start not after its end, a non-negative duration, a working schedule that is the same across the whole period, an employee, and must not fall on a mandatory day unless the requester is an officer; a request already approved cannot have its dates or employee changed, and a request cannot be duplicated unless refused or cancelled.
- [N-U40-017] The free-text description of a request is private: only officers, the owner and the employee's approver see it; everyone else sees a masked value, and writes by others are silently not stored.
- [N-U40-018] Employees may delete only their own future requests in early states; officers may delete only cancelled or to-approve ones; only administrators may delete the rest.
- [N-U40-019] Ordinary users can request time off only for themselves or for employees whose approver they are, among active employees of their allowed companies.

### RISK
- [N-U40-020] Changing an employee's working schedule rewrites the schedule of all future requests, recomputes their dates and recreates calendar entries; if the new schedule leaves the balance insufficient the change is refused with an explanatory message.
- [N-U40-021] Creating, changing or deleting a public holiday recalculates every open request of the company that overlaps it: durations change, employees are told whether days were returned or extra days were deducted, and requests that no longer fit the balance are refused automatically; overlapping public holidays for the same schedule are not allowed.
- [N-U40-022] Changing an employee's contract period or working schedule splits or reassigns approved and pending requests along the new version boundaries, refuses requests starting before the new version, and fails with an explanation if the split requests would no longer be covered by the allocation.

### UNKNOWN
- [N-U40-023] How request dates behave around timezone edges and daylight-saving changes cannot be confirmed from the source alone and needs execution.

## CAP-U40-02 Time-off types, allocations, accrual plans, balances and overtime exchange

### WHAT
- [N-U40-024] A time-off type defines how a kind of absence behaves: counting unit (days, half-days, hours), validation mode for requests and for allocations, whether an allocation is required, negative balance allowance, public-holiday treatment, supporting-document need, calendar display, notification subtypes, colour, and the working-time kind used for accrual.
- [N-U40-025] The balance shown to users per type is employee-specific and date-specific: remaining, requested, approved, accrual bonus, expiring amount and date, excess, and negative-cap figures, ordered so that the types most useful to the employee come first.
- [N-U40-026] An allocation's description is generated from the type and amount unless a custom text was typed.
- [N-U40-027] Future accrual is projected on a throw-away copy of the allocation so previews and expiry dates never change stored data, and an accrual allocation form simulates the plan from its start date.
- [N-U40-028] An accrual plan lists levels in time order and may be generic or tied to one type; its settings include transition mode, gain time, worked-time basis, unit and carry-over; a plan used by an active allocation cannot be deleted.
- [N-U40-029] Plan carry-over time is start of year, allocation anniversary or a custom day and month.
- [N-U40-030] Level frequency may be hourly, daily, weekly, twice a month, monthly, twice a year or yearly, with configurable days and months; the next and previous period dates are derived from the frequency, and an unknown frequency is an error.
- [N-U40-031] Dashboards and balances are shown for the employee named in context, else the default employee, else the current user's own employee.
- [N-U40-032] An analysis report compares expected hours, worked hours and approved leave per employee and day over the last year, excluding public holidays; it is visible only to users who are both attendance managers and time-off officers.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-033] A type has a valid allocation for an employee on a date when it needs none, or when an approved allocation covers the date and is accrual-based or has positive balance above the permitted excess.
- [N-U40-034] Allocations are measured in the unit of their type (or of their accrual plan); hours are converted to days with the employee's hours per day, and a change of working schedule preserves accrued hours.
- [N-U40-035] An accrual allocation grows over time according to its plan: each level starts after an offset from the allocation start, accrues a fixed amount at a chosen frequency, may prorate by worked time, can gain time at the start or end of each period, and is capped per year or overall; level changes happen immediately or at the end of the running period.
- [N-U40-036] At the plan's carry-over date unused accrued days are kept, limited to a maximum, or lost; carried-over days may expire after a validity period, and only the carried-over days not used by then are removed.
- [N-U40-037] When a plan does not permit carry-over, unused accrued time is lost, with unlimited option and no validity period.
- [N-U40-038] Balances are computed by consuming allocations in a fixed order (those ending soonest first, then open-ended accrual, then open-ended regular), counting requests in to-approve, second approval and approved states as virtual use and only approved ones as real use; future requests against accrual allocations are re-checked against what will be accrued by then, and unabsorbed time is recorded as excess.
- [N-U40-039] Overtime flagged as compensable becomes a balance of hours that can be spent on deductible time-off types; requests or allocations of such types are refused when the balance would go negative, the balance is shown to the employee, and absence entries or public holidays changing recalculate overtime of affected attendance records.

### STATE
- [N-U40-040] An allocation has to-approve, second approval, approved and refused states; types with no validation approve automatically; employees cannot approve or refuse their own allocations unless the type needs no validation or they are administrators; reset is not offered.

### OPTIONALITY
- [N-U40-041] A daily scheduled job brings every approved accrual allocation up to date, adding the days earned since the last run.
- [N-U40-042] The overtime bridge installs itself automatically when both attendance and time off are present and lets extra hours be exchanged for time off.
- [N-U40-043] Accrual levels can accrue per hour worked, based on attendance records, except when time is gained at the start of the period.

### DEPENDENCY
- [N-U40-044] Allocation requests schedule approval tasks and notifications like time-off requests, using two dedicated task types, and subscribe the employee, manager and approvers.

### CONSTRAINT
- [N-U40-045] Types may belong to one company or to none and carry a country; a company's country cannot change while requests or allocations of a type bound to another country exist.
- [N-U40-046] A regular allocation must be positive; validity start must not follow validity end; an allocation cannot be reduced below what the employee has already taken, and cannot be deleted while validated requests drew on it.
- [N-U40-047] Employees may request allocations only of types flagged as employee-requestable and officers manage all; non-officers may only name employees they approve for.
- [N-U40-048] Level amounts must be positive, caps and limited carry-over require positive maxima, twice-a-month levels need an ascending day pair, weekly levels need a weekday, and a level cannot start in the past relative to its own milestone setting.

### RISK
- No statement was identified in the source studied for this heading.

### UNKNOWN
- [N-U40-049] How multi-level accrual plans with carry-over, expiry and level transitions behave over many years cannot be confirmed without execution.

## CAP-U40-03 Time-off access control, reports, bulk generation, departure handling and seed configuration

### WHAT
- [N-U40-050] Three time-off roles form a chain: responsible (approves for people they manage), officer (manages all requests) and administrator (configures everything); the system users are made administrators at installation.
- [N-U40-051] A mandatory day is a dated range for a company, optionally limited to a working schedule, departments and job positions.
- [N-U40-052] Departments show the number of requests and allocations waiting for approval and how many employees are absent today, with shortcuts to the filtered lists.
- [N-U40-053] Reports cover requests and allocations together, a calendar of requests with limited detail for non-officers, a first-in-first-out view of taken, left and planned time per employee and type for administrators, and a printable sixty-day summary that treats Saturday and Sunday as non-working.
- [N-U40-054] Time-off types are seeded once: global types (paid time off, sick, unpaid, compensatory, extra time off, extra hours) and many types tied to other countries; no type for Thailand is seeded.
- [N-U40-055] In the reference database the time-off feature has its roles, 27 access rows, 26 record rules and two active daily jobs matching the source, 73 types of which 6 are global, and no requests, allocations, plans or mandatory days.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-056] Employees read their own requests and allocations; approvers read and decide for the people they approve for; officers read all and write all except their own approved requests; administrators have no restriction; deletion rights are narrower than write rights.
- [N-U40-057] Registering an employee's departure shortens requests that span the departure date, cancels approved requests after it without notifying approvers, deletes the others, and shortens or deletes allocations.
- [N-U40-058] Officers can create time off or allocations for many employees at once by employee, company, department or tag; ordinary approvers may only choose employees; bulk time off is created approved for officers or when no validation is needed, skips employees with no working days, refuses overlap with hour-based requests, and splits or refuses overlapping day requests.

### STATE
- No statement was identified in the source studied for this heading.

### OPTIONALITY
- [N-U40-059] Two scheduled jobs run daily: accrual updates and cancellation of requests no longer covered by accrued time.

### DEPENDENCY
- [N-U40-060] Time-off message subtypes are mirrored automatically at department level so department followers can subscribe to them.

### CONSTRAINT
- [N-U40-061] Requests, allocations, types, plans, mandatory days and reports are limited to the user's allowed companies, and types without company are further limited by country.
- [N-U40-062] Model-level access gives internal users broad rights that the record rules then narrow; administrators manage types and plans, officers read them; bulk wizards need the responsible role; calendar and resource objects are opened to officers so approvals can create calendar entries.

### RISK
- [N-U40-063] Approvers can act from a link in a notification: five signed-in link endpoints approve or refuse a request or an allocation after checking a token, change state through a plain page request, and hide any error behind a generic redirect; the endpoints that say validate and approve perform the same action.

### UNKNOWN
- [N-U40-064] How the printable summaries and reports look and read was not studied.

## CAP-U40-04 Work entry generation, conflict control, validation and time-off synchronisation

### WHAT
- [N-U40-065] A work entry type carries a payroll code, display code, pay rate, working-time or time-off nature and an extra-hours flag; codes must be unique within a country scope, the country of a used type cannot change, and the type choices follow the countries of the selected companies.
- [N-U40-066] In the reference database there are 118 work entry types (9 global, 109 country-specific, 86 time-off kinds), no work entries, and the daily generation job is active.
- [N-U40-067] In the reference database 58 of the 73 time-off types are mapped to work entry types, including the four mapped global ones.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-068] Work entries are generated for each employee version from the working schedule, public holidays and approved time off, in the schedule's timezone and as the system user: leave periods take their type from the leave, entries crossing midnight are split by local day, entries of the same day, type and version are merged, zero-length ones are dropped, and the generated window of each version is tracked so only missing periods are filled.
- [N-U40-069] Validating entries marks them in-payslip only when the whole batch passes the checks; otherwise the offending entries are marked in conflict and validation reports failure.
- [N-U40-070] A work entry of at least one hour can be split into two entries whose durations add up to the original.
- [N-U40-071] Entries can be regenerated for a period: existing non-validated entries are archived and recreated, validated entries and employees with validated entries in the range are never touched, changing the working schedule or source of a version regenerates its entries, and changing the contract dates removes entries outside the new period.
- [N-U40-072] Approving a request creates leave entries for already generated periods and archives work entries it fully covers, never touching validated ones; refusing or cancelling restores attendance entries; cancelling a leave entry refuses the request; a request whose entries are already in a payslip cannot be cancelled by the employee; a sick-leave code is exempt from the non-working-day check.

### STATE
- [N-U40-073] A work entry is new, in conflict, validated (in a payslip) or cancelled; archiving and cancelling are kept in step, validated entries cannot be deleted, and reactivating returns an entry to new.

### OPTIONALITY
- [N-U40-074] A daily job generates missing entries for the current month, one company at a time, in batches of one hundred versions with schedule-based ones first, and triggers itself again while more remain.

### DEPENDENCY
- [N-U40-075] Opening the work-entry calendar triggers generation for the displayed period and offers quick replacement and reset of days, so viewing can create data.
- [N-U40-076] Each time-off type may point to a work entry type so approved leave becomes the right kind of entry; when several leaves cover an interval the priority is exception codes first, then public holidays, then personal leave.

### CONSTRAINT
- [N-U40-077] One work entry lasts more than zero and at most twenty-four hours.
- [N-U40-078] Entries are marked in conflict when they have no type, when the day's total for an employee exceeds twenty-four hours, when leave entries fall outside the schedule (except flexible schedules), or when the employee already has validated entries on that day; conflicts clear automatically when their cause is removed.
- [N-U40-079] Entries are limited to allowed companies; HR officers read, create and change entries but only the system administrator may delete them; types are managed by HR managers; the regeneration wizard is for HR managers.

### RISK
- No statement was identified in the source studied for this heading.

### UNKNOWN
- [N-U40-080] Generation for flexible schedules and for attendance or planning sources, and the cost of mass regeneration, are not confirmed.

## CAP-U40-05 Recruitment pipeline: jobs, applications, talent pools, interviews, refusal and hiring

### WHAT
- [N-U40-081] A single applicant record represents either an application to a job or a talent in a pool; candidates are not a separate record, and each applicant has evaluation priority, tags, degree, salary figures, stage, recruiter, interviewers and meetings.
- [N-U40-082] Recruitment indicators per job and department include open, new, total and hired application counts, days to open and close, stale-application detection and expected versus hired employees.
- [N-U40-083] A job position gains an interviewer list, a favourite flag, requirements, documents, a source list and an alias; archiving a job archives its applications; changing the recruiter reassigns ongoing applications.
- [N-U40-084] Recruitment sources can create dedicated email aliases that stamp applications with job, campaign, medium and source; campaigns and sources in use cannot be deleted.
- [N-U40-085] Degrees carry a score between zero and one, tags are unique, and platform settings are held in company-level configuration.
- [N-U40-086] Seed data comprises six stages from New to Contract Signed, six refuse reasons, four degrees, four tags, three job platforms and four email templates.
- [N-U40-087] In the reference database recruitment has 30 access rows (plus one row reusing an HR identifier), 8 rules, 4 roles and the seeded stages, reasons and platforms; no jobs or applications exist.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-088] Recruitment has three roles (interviewer, officer, administrator): interviewers see and edit only applications of jobs or applications naming them, with a reduced form and menus; officers see everything and the chatter of every record; salary figures are visible to officers only; applications are limited to the user's companies.
- [N-U40-089] A talent pool holds talents; adding an application to a pool copies it into a job-less talent linked both ways, edits of contact details propagate to the talent, a talent belongs to at least one pool and cannot be duplicated, and applications can be created from existing ones for other jobs at the first stage.
- [N-U40-090] Duplicate applications are recognised by matching email, phone or social profile, or by a shared talent link, and are counted together.
- [N-U40-091] An application takes its company from its department or job, its department from the job and its recruiter from the job.
- [N-U40-092] Naming a user as interviewer on a job or an application grants the interviewer role automatically and removes it when no longer needed; new interviewers are notified.
- [N-U40-093] Creating an employee from an application ensures a contact, builds the employee from the application and contact data, copies attachments, logs the hire and is refused to interviewers.
- [N-U40-094] Refusing an application records a reason, archives it and stamps the date; an email can be sent using the reason's template provided the sender and every applicant have an email; duplicates can be refused together with an automatic note; reset and unarchive bring an application back to the first stage.

### STATE
- [N-U40-095] Applications move through configurable stages that may be job-specific, folded, marked hired and bound to an email template; entering a hired stage sets the hire date and reduces the job's expected new employees, leaving it restores them; each stage change resets the blocking indicator, stamps the time and posts the stage email.
- [N-U40-096] An application is ongoing, hired, refused or archived, derived from the refuse reason, the active flag and the close date.

### OPTIONALITY
- [N-U40-097] Applicant attachments get a text-search index when the database supports it.
- [N-U40-098] Activity plans on applications can assign tasks by department.

### DEPENDENCY
- [N-U40-099] The applicant's email and phone are synchronised with a linked contact, a contact is found or created from the email when a name is present, and messages to a suggested recipient link the contact to open applications.
- [N-U40-100] Interviews are calendar meetings opened from the application with the applicant, department manager and recruiter as attendees; attachments are copied to the meeting and meetings survive the deletion of the application.
- [N-U40-101] Each job has a mail alias that creates applications, with defaults for job, department, company and recruiter; mail from registered job platforms takes the applicant name from a pattern; replies go to the job alias; free emails can be sent to applicants from the application.

### CONSTRAINT
- No statement was identified in the source studied for this heading.

### RISK
- No statement was identified in the source studied for this heading.

### UNKNOWN
- [N-U40-102] The wording of email templates, the screens and menus, and the incoming-mail behaviour of recruitment were not studied.

## CAP-U40-06 Recruitment extensions: skill matching, SMS and interview forms

### WHAT
- [N-U40-103] An application holds a list of skills with levels; the current list excludes expired ones, keeping the most recent certification.
- [N-U40-104] In the reference database the skills bridge has 2 access rows and 2 rules, equal to source.
- [N-U40-105] In the reference database the message bridge adds one action and no security or schedule.
- [N-U40-106] A job can be linked to an interview form; applicants' answers are stored against the application and shown in print; a recruitment survey type exists.
- [N-U40-107] In the reference database the interview-form bridge has 13 access rows and 14 rules equal to source and one email template.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-108] A matching score compares an applicant's current skills and degree with the job's required skills and expected degree: each skill counts up to twice the required level, the result is a rounded percentage, matching and missing skills are listed, and applicants of other jobs sharing a required skill can be found and moved to the job.
- [N-U40-109] Skill edits on an application are mirrored on its talent record.
- [N-U40-110] An interview form is sent to an applicant by email with a fifteen-day default deadline, creating the contact, the answer record and chatter notes; the invitation text is also posted on the application; a completion note is posted when the applicant finishes; retries keep the applicant link.

### STATE
- No statement was identified in the source studied for this heading.

### OPTIONALITY
- No statement was identified in the source studied for this heading.

### DEPENDENCY
- [N-U40-111] Hiring an applicant copies the application's skills onto the new employee.
- [N-U40-112] Text messages can be sent to selected applicants through the shared message composer, with a log in the application; delivery depends on the message gateway of the base platform.

### CONSTRAINT
- [N-U40-113] Interviewers manage skills of applications they are named on, and recruitment officers manage skills required by jobs.
- [N-U40-114] Administrators have full control of recruitment surveys and answers, officers read answers (respecting survey restrictions) and manage invitations, and interviewers read answers and send invitations only for applications they are named on.

### RISK
- No statement was identified in the source studied for this heading.

### UNKNOWN
- [N-U40-115] Delivery of text messages and interview forms is handled by other features and was not studied.

## CAP-U40-07 Employee skills, resume, certifications and learning bridges

### WHAT
- [N-U40-116] One shared skill model serves employees, job positions and applicants: each entry ties a skill, a level and a type with a validity start and optional stop.
- [N-U40-117] A job lists required skills with levels; certification validity is not editable on jobs.
- [N-U40-118] An employee's current skills exclude expired ones, keeping the latest expired certification visible; saving merges skills, certifications and current skills into one history-preserving change.
- [N-U40-119] Resume lines belong to employees with a section type, dates (end optional), description, certificate file and type-specific properties; start must not follow end.
- [N-U40-120] Job-title history is rebuilt from employee versions for users who may read the public profile, merging consecutive versions with the same title.
- [N-U40-121] Skills, certification and skill-history reports are database views over current non-certification skills, active certifications and a time series of levels; the certification report fixes today's date when it is created.
- [N-U40-122] Seed data comprises language and soft-skill types with levels and three resume section types: experience, education and training.
- [N-U40-123] In the reference database the skills feature has 20 access rows and 11 rules equal to source, one active daily job, two skill types, 36 skills, 11 levels, three section types and no employee skills or resume lines.
- [N-U40-124] In the reference database the events bridge has 2 models and 3 views and no security or schedule.
- [N-U40-125] In the reference database the e-learning bridge has 5 models and 8 views and no security or schedule.
- [N-U40-126] In the reference database the certification bridge has 3 models, 2 views and one section type and no security or schedule.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-127] Skills keep history: changing a level archives the old entry by setting its stop date to yesterday and creates a new one; removing an entry deletes it only if it is very recent or already ended; certifications may coexist with different validity ranges.
- [N-U40-128] A resume can be printed as a document for one or several employees with chosen colours and sections; HR officers may print any, other users only their own.
- [N-U40-129] Every internal user can read all resume lines and skills of all employees but edit only their own, can add new skills to the catalogue, and sees reports only for people they manage; HR officers manage everything.

### STATE
- No statement was identified in the source studied for this heading.

### OPTIONALITY
- [N-U40-130] A daily job schedules an upload-certification task for employees in jobs requiring certifications that are missing or expire within three months, assigned to the employee, else the manager, else the job's recruiter, and skips duplicates.

### DEPENDENCY
- [N-U40-131] Onsite courses link resume lines to events; creating the event from the course field registers the employee as attendee.
- [N-U40-132] Completing an e-learning course adds a training resume line once per employee and course, and subscribing or leaving posts notes in the employee's chatter.
- [N-U40-133] Passing a certification survey adds or refreshes an internal certification resume line with a validity end set by the survey; the expiry status is recalculated only when the end date changes.

### CONSTRAINT
- [N-U40-134] Entries for the same person and skill may not overlap or duplicate each other, stop dates cannot precede start dates, and the skill and level must belong to the chosen type.
- [N-U40-135] A skill type needs at least one skill and one level; level progress lies between zero and one hundred percent; only one level per type is the default; certification types are marked and copies duplicate skills and levels.

### RISK
- No statement was identified in the source studied for this heading.

### UNKNOWN
- [N-U40-136] The layout of the resume document and the skill screens in the browser were not studied, and two suspected defects need execution to confirm.

## CAP-U40-08 Presence control and remote-work location

### WHAT
- [N-U40-137] Each employee has a default work location for each weekday and an optional dated exception; today's effective location sets the presence icon, name and type, and the chat status is prefixed with home, office or other.
- [N-U40-138] In the reference database the remote-work feature has 6 models, 2 access rows and 2 rules and the calendar bridge 3 models, 1 access row and 2 rules; no schedules.
- [N-U40-139] By default presence follows the user's online status: online is present, offline during working hours is absent, archived is archived, otherwise off-hours.
- [N-U40-140] In the reference database the hourly presence job is active, login-based presence is on and IP and message criteria are off.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-141] A calendar wizard sets the location for a date either as a one-off exception or as the new weekly default; a weekly default for an employee without a user account is not saved.
- [N-U40-142] With IP control an employee counts as connected if any address recorded today for their user is in the company's list; internal users' addresses are logged once a day on presence updates.
- [N-U40-143] HR managers can set an employee present or absent manually, which overrides automatic criteria until the next hourly reset, log a note, send a reminder text, or create an unplanned absence; five actions are offered in the employee views.

### STATE
- [N-U40-144] An employee is present if working now and counted by any enabled criterion, absent if working now, on approved leave and not counted, otherwise off-hours; nothing changes when neither criterion is enabled.

### OPTIONALITY
- [N-U40-145] An hourly job refreshes presence flags from IP addresses and message counts for the current company when those criteria are enabled, and saving settings with them enabled runs it immediately.

### DEPENDENCY
- [N-U40-146] The home-working calendar shows weekly defaults plus dated exceptions for the visible range per employee contact in the current company, and deleting an entry confirms first.
- [N-U40-147] The presence view can open a single time-off request or the bulk wizard for several employees with an unplanned absence label.

### CONSTRAINT
- [N-U40-148] Only one exception per employee and date is allowed.
- [N-U40-149] Internal users manage only their own exceptions; HR officers manage all.
- [N-U40-150] HR managers may create, change and delete message templates limited to employee templates.

### RISK
- [N-U40-151] With message control an employee counts as present after authoring a configured number of messages today; the count includes every message type, not only emails.
- [N-U40-152] The reminder text uses a built-in default when the seeded template cannot be found, because the action looks it up under a different identifier than the seeded one; delivery depends on the message gateway.

### UNKNOWN
- [N-U40-153] Real-time presence updates, address logging and text-message delivery need runtime confirmation.

## CAP-U40-09 Employee-linked bridges: hourly cost, timesheet-attendance report, org chart, equipment, live chat

### WHAT
- [N-U40-154] An employee has one hourly cost amount, readable and writable only by HR officers, without history or validity period.
- [N-U40-155] In the reference database the cost feature has 1 model, 3 fields and 1 view and no employee has a non-zero cost.
- [N-U40-156] A report compares attendance time and project timesheet time per employee and day and values the difference with the employee's hourly cost.
- [N-U40-157] In the reference database the report has 4 rules, 1 access row, 1 menu and 1 action and no schedule.
- [N-U40-158] The organisation chart derives direct and indirect subordinates and handles cyclic management chains; a subordinate flag is relative to the current user.
- [N-U40-159] In the reference database the organisation chart has 2 models, 7 views and 2 actions and no security or schedule.
- [N-U40-160] In the reference database the equipment bridge has 5 models and 11 views and its own role implication only.
- [N-U40-161] The live chat bridge adds only team filters based on the management hierarchy or department membership; it has no data model, security or server logic.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-162] Three signed-in routes serve the organisation chart: up to five manager levels, subordinate id lists and the employee model the user may open; only readable employees are returned and only public-profile fields are exposed.
- [N-U40-163] Equipment is assigned to an employee, a department or neither; switching clears the other target and stamps the date; owner and followers follow the assignment; employees list their equipment.
- [N-U40-164] Maintenance requests carry an employee and offer only equipment assigned to that employee or unassigned; requests created by email take the employee from the environment user, not the sender.

### STATE
- No statement was identified in the source studied for this heading.

### OPTIONALITY
- [N-U40-165] The organisation chart installs automatically with the HR core.

### DEPENDENCY
- [N-U40-166] Other modules take the employee's hourly cost when valuing timesheet entries, with an override for employee-rate pricing; later cost changes do not restate existing entries.
- [N-U40-167] The departure wizard offers to free the employee's equipment.

### CONSTRAINT
- [N-U40-168] Timesheet users read only their own rows, approvers and timesheet administrators read all, and the cost columns reach readers who could not read the cost field directly.

### RISK
- [N-U40-169] Installing the equipment bridge makes every HR officer an equipment manager.

### UNKNOWN
- [N-U40-170] The browser widgets of the organisation chart and equipment, and the attribution of emailed maintenance requests, need runtime confirmation.

## CAP-U40-10 Generic HTML page builder and editor persistence contracts

### WHAT
- [N-U40-171] The page builder is a client-side component shipped as assets only: the module declares no data, models, security or server code, and it relies on the base editor module and on host applications for persistence.
- [N-U40-172] Images keep their original attachment, formats and ids as page data, and older images are migrated on load.
- [N-U40-173] In the reference database the builder module is installed with no data rows while the base editor module has 24 models, 73 fields and 2 access rows, and the website and mass mailing hosts are installed.

### WHY
- No statement was identified in the source studied for this heading.

### BUSINESS RULE
- [N-U40-174] Editing marks savable zones as modified; saving groups modified zones by record and field, cleans them, escapes text, and sends them to the server one at a time through a single view-saving method, adding website, language and delayed-translation context when a website is present.
- [N-U40-175] The block list is rendered on the server from the host's template; custom blocks can be saved, renamed and deleted through three server methods and are tagged and named by default.
- [N-U40-176] Background and image shapes are stored as addresses of a public shape route with colour, flip and animation parameters, validated so only hexadecimal, rgb or theme colours are accepted.
- [N-U40-177] The server saves a page section by converting embedded fields back to their records with the caller's rights, storing structures as inheriting views, stripping editing attributes, writing a view only when it changed and marking it as protected from upgrade overwrite; custom block saving needs the website feature.
- [N-U40-178] Uploaded and modified media become attachments: public when attached to pages, deduplicated by checksum, checked for format, copied with checks on the source and target records, linked to variants, and removable only when no page uses them; adding an image by address makes the server request that address.

### STATE
- No statement was identified in the source studied for this heading.

### OPTIONALITY
- [N-U40-179] Host models can keep up to three hundred revisions per versioned field, which must be sanitised.

### DEPENDENCY
- [N-U40-180] Fonts come from an external font service or from locally stored attachments.

### CONSTRAINT
- [N-U40-181] Live collaboration channels require read and write access to the document and field and are closed to public users.
- [N-U40-182] The base editor module's own access rows concern test models only.

### RISK
- [N-U40-183] Option plugins can create and rewrite related records through the user's ordinary rights; the pending-record save returns a flag that is always false, and related-record pickers search target models by name.
- [N-U40-184] Three editor features call external services: a media library (download addresses fetched without timeout, files stored as the system user), an AI text service (prompt and history sent with the database identifier) and public link previews fetching caller-supplied addresses.

### UNKNOWN
- [N-U40-185] Most front-end builder options, the host applications' save paths and all browser behaviour were not studied.

