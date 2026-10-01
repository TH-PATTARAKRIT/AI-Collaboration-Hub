# U17 Human Resources, Time Off, Attendance, Work Entries, Recruitment, Skills, Fleet and Calendar — NEUTRAL KNOWLEDGE

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room layer: plain business and process language only (platform: Odoo 19 Community, named once here).
> Each statement carries an identifier in square brackets that links it to restricted technical claims. No file, module, field or code names appear below. Personal data of employees is described by structure and rule only; no values are recorded.

## CAP-U17-01 Employee master record and dated versions

### WHAT
- [N-U17-001] An employee record holds a person's working relationship with the company: name, work contact details, company, department, job, manager, coach, working schedule, work location and tags, plus personal, banking and identification data that only HR staff may see.
- [N-U17-002] Contract-like terms (contract start and end, pay structure, working schedule, department, job) are not stored on the person but in dated versions of the employee record. The version with the latest effective date that is not in the future is the current one; a daily job refreshes which version is current.
- [N-U17-003] A contract period is a run of versions that share the same contract start and end dates. Starting a new contract creates a version at the chosen date, or writes the dates onto a version that already exists on that date.
- [N-U17-004] An employee can be linked to a system user, at most one per company. Users can be created from employees (singly or in bulk) and employees can be created from users; name, picture, timezone and work email are kept in step.
- [N-U17-005] Registering a departure archives the employee, records the reason, free text and date, optionally closes the current contract on that date and optionally archives the linked user.

### WHY
- [N-U17-006] Dated versions keep the history of role, schedule and pay terms without overwriting past facts. Leave durations, work entries and overtime rules read the version that was in force on the relevant date.

### BUSINESS RULE
- [N-U17-007] An employee must always keep at least one active version. The last version cannot be deleted, archived or moved to another employee.
- [N-U17-008] Two active versions of one employee cannot share an effective date. Contract periods of one employee may not overlap, a contract end needs a start, and the start may not be after the end.
- [N-U17-009] Creating a version on a date that already has one returns the existing version. Otherwise the new version is a copy of the version in force on that date with the requested changes applied. Changing contract dates on one version propagates to all versions of the same contract; changing dates of several different contracts at once is refused.
- [N-U17-010] Changing a version-held field through the employee writes it onto the version in force (or the one chosen by the caller), stamps who changed it and when, and leaves a note in the employee log.
- [N-U17-011] The badge identifier must be unique, alphanumeric and at most eighteen characters; the kiosk PIN must contain digits only; one user cannot be linked to two employees of the same company.
- [N-U17-012] Archiving an employee clears that person as manager or coach on other employees. Changing a department's manager re-points the members who reported to the previous manager.
- [N-U17-013] The departure date cannot precede the start of the current contract. The linked user is archived only if every employee record of that user is part of the departure.
- [N-U17-014] A work contact is created automatically when missing. Bank accounts attached to an employee are re-pointed to a new work contact, and the payment-trust flag of a moved account is cleared.
- [N-U17-015] The HR responsible of a version is a mandatory internal user who belongs to the HR officer group of the company; it defaults to the person creating the record.

### STATE
- [N-U17-016] Employee: active, then archived with departure data, then active again; unarchiving clears the departure data.

### OPTIONALITY
- [N-U17-017] Contract expiry and work permit expiry reminders use per-company notice periods. After creation the log suggests an onboarding activity plan. Bulk user creation warns that new users may increase the subscription cost.

### DEPENDENCY
- [N-U17-018] Each employee delegates scheduling, timezone and picture to a resource record; deleting the employee deletes the resource, and the resource schedule follows the schedule of the current version.

### CONSTRAINT
- [N-U17-019] The department hierarchy cannot be cyclic. A job position name must be unique within a department and company, and the planned number of recruits cannot be negative.

### RISK
- [N-U17-020] Changing the company of an existing employee is warned against because contracts and leaves would become inaccessible; a separate employee in the new company is recommended. Bulk user creation skips employees with missing, invalid, duplicate or already-used work email addresses and reports them.

### UNKNOWN
- [N-U17-021] Contract templates, salary structure types, country-specific personnel rules and payroll integration were not studied in depth.

## CAP-U17-02 Employee data access scoping, manager hierarchy and company boundaries

### WHAT
- [N-U17-022] Employee data is exposed through two views of the same person: a full private view for HR officers and a reduced public view for every other internal user. The public view is a read-only projection holding only name, department, job, work contact, location, manager, coach, presence and a few flags.
- [N-U17-023] Four levels of access exist for employees: any internal user (public view only), HR officer (all employees, create and edit), HR administrator (contract terms and configuration) and system administrator (read-only on the private view).

### WHY
- [N-U17-024] The split lets the company publish an internal directory and organisation chart to everyone while keeping identification numbers, private contacts, bank accounts, pay and family data inside HR.

### BUSINESS RULE
- [N-U17-025] Users without access to the private view who search or open an employee are transparently served from the public view; asking for a private field fails with an access error that names the public profile limitation.
- [N-U17-026] Personal and identification fields carry the HR officer group; pay and contract-term fields carry the HR administrator group; so they are hidden from all other users even when the record itself is reachable.
- [N-U17-027] A company boundary rule applies to every user: an employee is visible if the company is among the user's active companies, or the user is the manager of the employee, or the employee is the user's own manager, or it is the user's own record.
- [N-U17-028] Contract versions are visible only for the user's active companies, and administrators see all.
- [N-U17-029] Bank accounts of employees are hidden from all internal users except HR officers.
- [N-U17-030] An employee may edit a short list of their own contact and preference fields through the personal preferences screen, and HR is notified when such personal information changes.
- [N-U17-031] The organisation chart shows managers upwards and direct or indirect subordinates, reads from the public view, tolerates cycles such as a chief executive who sits in a department managed by someone they manage, and limits the chain length.

### STATE
- [N-U17-032] Not applicable: access scoping carries no state machine of its own; the manager link, the user link and group membership drive it.

### OPTIONALITY
- [N-U17-033] The organisation chart and the hourly cost field are optional add-ons. The hourly cost is visible to HR officers only.

### DEPENDENCY
- [N-U17-034] Many other modules rely on a special context marker that lets them link to employees in relations even when the acting user cannot read the private view.

### CONSTRAINT
- [N-U17-035] Company scoping of employees is permissive for managers: a manager can still see a subordinate who belongs to a company outside the manager's active companies.

### RISK
- [N-U17-036] Any module that reads a private field without the right group, or that searches employees as an administrator and returns names to ordinary users, can leak data across the public and private boundary. The kiosk, the presence report and the calendar availability helper use elevated reads and were reviewed only at source level.

### UNKNOWN
- [N-U17-037] Portal or external access to employee records and the effect of multi-company switching in the web client were not exercised at runtime.

## CAP-U17-03 Time-off request lifecycle and approval

### WHAT
- [N-U17-038] An employee asks for time off of a configured type for a date range, half days or hours. The system computes duration in days and hours from the working schedule, public holidays and the type's rules, and routes the request for approval according to the type.
- [N-U17-039] A time-off type decides who approves: nobody, an HR time-off officer, the employee's approver, or the approver first and then an officer. Types also decide whether an allocation is required, the unit of measure, supporting documents, paid or unpaid kind, whether public holidays count, whether negative balances are allowed and whether a calendar entry is created.
- [N-U17-040] Approval produces an absence entry on the employee's working calendar (so schedules and presence reflect it) and optionally a private calendar meeting for the employee.

### WHY
- [N-U17-041] The goal is controlled absence: balances are protected, approvers are notified, and approved absences reduce planned availability across attendance, work entries and calendars.

### BUSINESS RULE
- [N-U17-042] A request needs an employee. When the type needs no validation the request is approved at once, with a system note; otherwise a task is scheduled for the responsible approver (the employee's approver, else the manager, else the officers listed on the type).
- [N-U17-043] Requests of the same employee may not overlap unless the type allows requests on top; the overlap message lists the conflicting requests.
- [N-U17-044] For types that need an allocation, creation or change is refused when there is no allocation, or when the remaining balance would fall below the permitted negative limit; the check is repeated when the request is approved or dates change.
- [N-U17-045] Ordinary users cannot request time off on a mandatory day; officers can.
- [N-U17-046] A request cannot span two versions of the employee that have different working schedules. A request that falls entirely on days when the employee is not scheduled to work cannot be approved.
- [N-U17-047] Who may move a request between states follows a matrix: officers can move between nearly all states; the employee's approver can approve or refuse only for types that include approver validation; the employee can cancel own requests (future ones unless an officer); nobody can reset a request, and a cancelled request cannot be changed.
- [N-U17-048] Approved or second-approval requests that are refused, cancelled or returned to approval remove the calendar absence and the meeting. Cancelling gives an optional reason and notifies the relevant approvers depending on how far approval had progressed.
- [N-U17-049] Deletion is limited: ordinary users may delete only their own requests that are not yet approved and not in the past; officers only requests awaiting approval or cancelled; administrators any.
- [N-U17-050] A started request can be edited by an officer or by the employee's approver only; copies of active requests are refused.
- [N-U17-051] Approval and refusal links in notification messages act through plain links that carry a security token and require a signed-in user.
- [N-U17-052] Changes to public holidays, to company calendar absences, and to the employee's working schedule trigger recomputation of overlapping requests: balances are refunded or charged, requests that no longer fit are refused, and requests across a schedule change are split or returned for review.
- [N-U17-053] On departure, approved future requests are cancelled, other future requests are deleted and requests spanning the departure date are truncated.
- [N-U17-054] A daily job cancels requests starting in the next thirty-one days when an accruing balance can no longer cover them, with an explanatory note.

### STATE
- [N-U17-055] Time-off request: awaiting approval, then second approval (two-level types only), then approved; refused from awaiting approval, second approval or approved; cancelled by the employee or system; no transition leaves cancelled.

### OPTIONALITY
- [N-U17-056] Calendar meeting creation, supporting documents, half-day or hourly units, negative balance and overtime-based deduction are controlled per time-off type.

### DEPENDENCY
- [N-U17-057] Work entries are re-evaluated whenever a request is approved, refused, cancelled or returned to approval; an approved request that is already part of validated work entries cannot be cancelled. Overtime-deductible types additionally require enough compensable extra hours.
- [N-U17-058] The approver of an employee defaults to the manager's user and follows manager changes; being named approver grants the time-off responsible group, which is removed when the user no longer approves anyone.

### CONSTRAINT
- [N-U17-059] Start must not be after end, durations cannot be negative, and the allocation requirement of a type cannot change once any request exists for it. A company's country cannot change while country-specific time off exists.

### RISK
- [N-U17-060] Public-holiday edits silently change durations of many approved requests and can refuse requests after approval; refunds and extra charges are notified by message only. State-changing approval links are plain links, so their safety rests entirely on the token.
- [N-U17-061] An overtime-deduction override that refers to a base reset action which does not exist in the studied source would fail if invoked; no caller was found.

### UNKNOWN
- [N-U17-062] Behaviour with external calendar synchronisation, email approval inbound handling and the generation wizards for bulk time off was not read in detail.

## CAP-U17-04 Time-off allocations, accrual plans and balances

### WHAT
- [N-U17-063] An allocation grants an employee a number of days or hours of one time-off type for a validity period. It is either regular (a fixed amount) or accrued over time according to an accrual plan.
- [N-U17-064] An accrual plan has ordered levels. A level starts after a delay from the allocation start and adds an amount at a frequency from hourly to yearly, with optional caps per balance and per year, a carry-over policy and an optional expiry of carried-over time.
- [N-U17-065] The balance of a type is approved allocations minus taken and pending time off, and the system warns or refuses when a request would exceed it.

### WHY
- [N-U17-066] Accruals let entitlements grow with service time or worked time instead of being granted in one block, and carry-over rules enforce use-it-or-lose-it policies.

### BUSINESS RULE
- [N-U17-067] A new allocation always starts awaiting approval; if the type needs no validation it is approved at once. Approval tiers mirror requests; an employee cannot approve or refuse their own allocation unless they are a time-off administrator and the type needs validation.
- [N-U17-068] A regular allocation must be longer than zero, and validity start cannot be after end. An allocation duration cannot be reduced below what the employee already took.
- [N-U17-069] An allocation can be deleted only while awaiting approval or refused, and never if time taken exists.
- [N-U17-070] A daily job processes approved accrual allocations whose next run date has come, replaying all missed periods up to today. On first run it initialises the next run date and logs that later configuration changes will not affect the days already given.
- [N-U17-071] Per period the amount equals the level's amount, prorated for partial periods; levels based on worked time or with hourly frequency prorate by eligible worked time versus absences; hour amounts are converted to days using the employee's hours per day.
- [N-U17-072] Caps apply per period: the yearly cap limits the amount accrued in a year, and the balance cap limits the total including time already taken.
- [N-U17-073] The carry-over date is the start of the year, the allocation anniversary or a chosen date. At that date unused time is lost, or limited to a maximum carried amount; carried time can expire after a delay and only the unused part expires.
- [N-U17-074] Level transitions take effect immediately or after the current period ends, per plan; the level in force is chosen by time since allocation start.
- [N-U17-075] A plan cannot be deleted while it is used by an allocation. Levels must start in the future of the allocation and must add more than zero; a level based on worked time is not allowed when time is accrued at the start of the period.

### STATE
- [N-U17-076] Allocation: awaiting approval, then second approval (two-level types), then approved; refused from any open state; no cancelled state; accrual allocations additionally track last and next run dates.

### OPTIONALITY
- [N-U17-077] Accrual by worked hours needs the attendance module. Extra hours can be made deductible from time off, creating a pseudo-balance from approved compensable overtime.

### DEPENDENCY
- [N-U17-078] Accrual proration uses working schedule intervals, absence entries marked eligible for accrual and, for the worked-hours frequency, attendance records. Changing an employee's schedule recomputes the stored amount of hour-based allocations so accrued hours are preserved.
- [N-U17-079] Changes of an employee's manager or department propagate to allocations that are still awaiting approval.

### CONSTRAINT
- [N-U17-080] A negative cap needs a maximum excess of at least one; worked-time types are always eligible for accrual; absence types cannot allow requests on top of existing ones.

### RISK
- [N-U17-081] The accrual replay loop is long and depends on many stored dates; editing an allocation after its first run does not change days already given. Overtime-balance checks use elevated reads and sum several pools; incorrect pool classification would let negative balances through. The decision to schedule an approval task for an allocation reads the validation setting meant for time-off requests instead of the one meant for allocations, so tasks can be missing or unneeded.

### UNKNOWN
- [N-U17-082] Exact numeric results of accrual cases were not simulated; they require execution.

## CAP-U17-05 Attendance recording, kiosk and overtime

### WHAT
- [N-U17-083] Employees check in and out from the web client, a kiosk screen or a badge scanner. Each pair of times is an attendance with optional location, address of origin and browser details.
- [N-U17-084] Overtime is derived from attendances by company-configured rulesets attached to the employee's version. Rules measure extra time either by quantity per day or week or by timing (non-working days, a time window, a schedule), may be paid at a rate and may be convertible to time off.
- [N-U17-085] Daily jobs close forgotten attendances automatically and, when absence management is on, create technical attendances so that unjustified absences produce negative extra hours.

### WHY
- [N-U17-086] The module gives a verifiable record of presence for payroll, overtime compensation and workforce analysis.

### BUSINESS RULE
- [N-U17-087] Check-out cannot be before check-in; an employee can have at most one open attendance; attendances of one employee cannot overlap.
- [N-U17-088] Worked hours exclude lunch intervals for fixed schedules and are the plain difference for flexible schedules.
- [N-U17-089] Checking in creates an attendance; checking out closes the open one; if no open attendance is found an explanatory error asks the user to contact HR.
- [N-U17-090] Archiving an employee closes any open attendance at that moment.
- [N-U17-091] Any create, edit or delete of attendances regenerates the overtime lines of the affected days (or weeks for weekly rules), while keeping lines already edited by hand or awaiting approval.
- [N-U17-092] Overtime lines are approved automatically or require manager approval depending on a company setting; approving or refusing updates the attendance status; the combined pay rate of overlapping rules is the maximum or the sum of extra rates per ruleset.
- [N-U17-093] The automatic check-out job closes an open attendance when elapsed time plus time already worked that day exceeds scheduled hours by more than the company tolerance, marking it as automatic and logging a note.
- [N-U17-094] Changing which employee an attendance belongs to is allowed only to the attendance owner, the attendance administrator or the employee's attendance approver.
- [N-U17-095] The kiosk is reached by a company-specific secret address; badge scans and manual selection identify employees without a signed-in session, with an optional PIN, and act with elevated rights.
- [N-U17-096] When device tracking is on, the check records location (from coordinates or an external geocoding service, or "Unknown" when it fails), network address and browser.

### STATE
- [N-U17-097] Attendance: open then closed; overtime line: awaiting approval, approved or refused.

### OPTIONALITY
- [N-U17-098] Kiosk mode, systray check-in, PIN, device tracking, display of extra hours, overtime approval, automatic check-out and absence management are company settings.
- [N-U17-099] Time off and public holidays affect overtime when the time-off bridge is installed: creating or changing company absences recomputes overtime for affected attendances.

### DEPENDENCY
- [N-U17-100] Overtime needs the working schedule of the version in force, public holiday data and, for deduction, the time-off module. Presence states can follow attendances.

### CONSTRAINT
- [N-U17-101] Overtime line stop must be after start; rules need valid schedule or hour bounds; expected hours and period must be consistent.

### RISK
- [N-U17-102] The kiosk key is a bearer secret in a link; anyone with it can act for any employee of that company, and PIN use is optional. External geocoding can fail or be slow; failure is swallowed and shown as unknown.
- [N-U17-103] Full regeneration of overtime on every attendance change can be heavy for large histories, and the absence job creates and deletes technical records daily.

### UNKNOWN
- [N-U17-104] Exact overtime splitting for complex mixes of rules, and the legal acceptability of kiosk evidence, need runtime tests and local counsel.

## CAP-U17-06 Work entry generation, conflict control and validation

### WHAT
- [N-U17-105] A work entry is a dated amount of hours of one type for one employee under one version, produced from the working schedule and absences, and later consumed by payroll as validated entries.
- [N-U17-106] A daily job generates missing entries for the current month in batches; entries can also be generated or regenerated on demand for employees and date ranges.

### WHY
- [N-U17-107] Work entries turn schedules, absences and public holidays into a payroll-ready, auditable timeline and flag contradictions early.

### BUSINESS RULE
- [N-U17-108] Duration must be greater than zero and at most twenty-four hours. The total per employee per day may not exceed twenty-four hours; offending entries become conflicts.
- [N-U17-109] Validation succeeds only when no entry has an undefined type, a daily excess, a leave outside the schedule or a date already covered by validated entries; otherwise the offending entries are marked in conflict.
- [N-U17-110] Entries are generated only inside contract periods, are recorded by version, and generation tracks already generated bounds so only new ranges are produced; forcing regeneration deactivates non-validated entries in range.
- [N-U17-111] Entries of the same day, type, employee and version are merged; entries spanning midnight in the schedule timezone are split by day.
- [N-U17-112] Validated entries cannot be deleted; cancelling an entry deactivates it, reactivating returns it to new; employees with validated entries in the range are excluded from regeneration.
- [N-U17-113] Changing the schedule or the entry source of a version recomputes entries for its generated range; changing contract dates removes entries outside the new period; deleting a version cancels its non-validated entries.
- [N-U17-114] An entry can be split into two if it is at least one hour and the split part is shorter than the original.
- [N-U17-115] Approved time off creates leave entries that replace overlapping attendance entries; refusal, cancellation or return to approval deactivates the leave entries and regenerates attendance entries. Cancelling a leave work entry refuses the time off. A time off that is part of validated entries cannot be cancelled.
- [N-U17-116] When both public holidays and employee time off cover an interval, the type is chosen by priority: configured bypass types first, then public holiday, then employee time off.

### STATE
- [N-U17-117] Work entry: new, in conflict, validated (in payslip) or cancelled; conflict returns to new when the cause disappears; validated is final.

### OPTIONALITY
- [N-U17-118] In the studied edition the only entry source is the working schedule; attendance-based and planning-based sources are described in help text but not available.
- [N-U17-119] Entry types are country-specific or global and carry payroll codes, rate and flags; a code cannot repeat for the same country.

### DEPENDENCY
- [N-U17-120] Generation reads working schedules, company calendar absences and, with the time-off bridge, employee time off. A payroll module, which is not part of this edition, is the consumer.

### CONSTRAINT
- [N-U17-121] The country of an entry type cannot be changed once entries use it; the default attendance type has a fixed country.

### RISK
- [N-U17-122] Generation runs with superuser rights across versions and raises an error when no timezone can be found for a version; very long ranges or mass regeneration can be heavy.

### UNKNOWN
- [N-U17-123] Interaction with payroll slip generation and localisation-specific entry types was not studied.

## CAP-U17-07 Recruitment pipeline

### WHAT
- [N-U17-124] A job position collects applications. Each application moves through ordered stages, has a recruiter, interviewers, meetings, attachments, tags and optional talent pool membership, and ends as hired, refused or archived.
- [N-U17-125] Applications can be created by hand or from inbound email to a job's address; mail from registered job boards takes the candidate name from a pattern in subject or body and is not linked to a contact.
- [N-U17-126] A hired application can be turned into an employee, copying private address, job, department, work email, phone, attachments and, with the skills bridge, skills.

### WHY
- [N-U17-127] The pipeline gives hiring teams one place to track candidates, decisions and the hand-off to HR.

### BUSINESS RULE
- [N-U17-128] A new application with a job takes the first non-folded stage that applies to that job; the stage can have an email template, a hired flag and a rotting threshold.
- [N-U17-129] Entering a hired stage sets the hire date and decrements the job's remaining planned recruits (not below zero); leaving it restores the count and clears the hire date.
- [N-U17-130] Application status is refused when a reason is set, archived when inactive, hired when a hire date exists, otherwise ongoing.
- [N-U17-131] Refusing opens a wizard: a reason is required, the application is archived with a refusal date, an email can be sent when both sender and recipient addresses exist, and duplicates (same email, phone or profile link) can be refused together with a note.
- [N-U17-132] Unarchiving or resetting puts the application back in the first stage and clears the refusal.
- [N-U17-133] Interviewers get the interviewer group automatically, and lose it when they are no longer interviewer on any job or application; interviewers can read and edit assigned applications but cannot create them or create employees.
- [N-U17-134] Creating an employee requires an applicant name, creates a contact when missing and posts a hired note on the employee.
- [N-U17-135] Recruiters (officers) see all applications and all chatter messages; recruitment administrators manage stages, platforms and surveys; the job position rights of officers are widened by this module.
- [N-U17-136] A talent must belong to at least one talent pool; talent data is mirrored from linked applications.

### STATE
- [N-U17-137] Application: ongoing (stage progression) to hired, or to refused or archived; reset returns it to ongoing in the first stage.

### OPTIONALITY
- [N-U17-138] SMS to applicants, interview surveys, skills matching and online job posting are optional bridges; stages can be shared across jobs or limited to specific jobs.
- [N-U17-139] A skills bridge scores applicant skills and degree against the job's required skills and levels.
- [N-U17-140] Interview surveys are sent after validity checks, with a default deadline of fifteen days, and the applicant is notified of completion in a message authored by the system bot.

### DEPENDENCY
- [N-U17-141] Calendar meetings link to applications; mail aliases create applications; mass SMS uses the platform's SMS gateway.

### CONSTRAINT
- [N-U17-142] The planned number of recruits cannot be negative; job names are unique per department; a stage cannot lose its hired flag silently while applications sit in it (a warning is shown).

### RISK
- [N-U17-143] Because recruitment officers read all chatter messages, sensitive messages on any document become visible to them. Email-created applications and platform patterns depend on external formatting.

### UNKNOWN
- [N-U17-144] Website careers publication, applicant document digitisation and external job-board feeds were not studied.

## CAP-U17-08 Skills, resumes and certifications

### WHAT
- [N-U17-145] Employees have resume lines (experience, education, courses, certifications) and skills tagged with a skill type, skill and level; certifications carry validity dates.
- [N-U17-146] Learning and event modules add resume lines automatically: onsite events register the employee, finished online courses add training lines, passed certification surveys add certification lines with an expiry.

### WHY
- [N-U17-147] A shared skills catalogue helps staffing, training and recruitment matching, and expiry tracking reminds the company when certifications lapse.

### BUSINESS RULE
- [N-U17-148] A regular skill allows only one active record per skill, and history is kept by ending the old record rather than editing; a certification can coexist with others of the same skill if the validity ranges differ; exact duplicates are refused.
- [N-U17-149] Validity end cannot be before start; the skill must belong to the chosen type and the level to the type; a skill type needs at least one skill and one level.
- [N-U17-150] Removing a skill that is older than a day ends it yesterday instead of deleting it, unless that would create a conflict, in which case it is deleted.
- [N-U17-151] A daily job opens a task for the responsible person when an employee lacks a certification required for their job, or it expires within three months.
- [N-U17-152] A resume line has start not after end; expiration status is expired, expiring within three months, or valid.
- [N-U17-153] Every internal user can read all resumes and skills; employees can create, edit and delete only their own; HR officers manage all; reports are visible to HR and to managers of the departments concerned.

### STATE
- [N-U17-154] Individual skill: active while valid-to is empty or in the future, then ended; certification: valid, expiring, expired.

### OPTIONALITY
- [N-U17-155] The event, e-learning and survey bridges are installed automatically when their parent modules exist; certification types are optional.

### DEPENDENCY
- [N-U17-156] Resume automation depends on completion callbacks of event, course and survey modules and uses elevated rights to write lines for the employee.

### CONSTRAINT
- [N-U17-157] Employees can create new skills in the shared catalogue (create right without write), so catalogue hygiene depends on HR review.

### RISK
- [N-U17-158] Employee-visible resumes may expose personal history to all colleagues; certification reminders depend on the job-to-skill mapping and on an existing responsible user.

### UNKNOWN
- [N-U17-159] Job-to-skill mapping screens and the resume printing wizard were not read in detail.

## CAP-U17-09 Fleet vehicles, contracts, services and driver assignment

### WHAT
- [N-U17-160] The fleet registry holds vehicles with model, state, plate, driver, future driver, odometer history, service logs, contracts and a driver assignment history.
- [N-U17-161] The human resources bridge links the driver to an employee through the employee's work contact and lets HR see vehicles with assigned employees.

### WHY
- [N-U17-162] The aim is to track company vehicles, contract renewals and who drives what.

### BUSINESS RULE
- [N-U17-163] The odometer of a vehicle is the highest logged value; entering a lower value is refused; entering a value logs a new reading dated today.
- [N-U17-164] Changing the driver adds a history line starting today and creates a task for the fleet manager asking for the end date of the previous assignment; accepting a driver change moves the future driver into place and clears other vehicles of that type held by that person.
- [N-U17-165] Archiving a vehicle archives its contracts and services.
- [N-U17-166] A contract is new, running, expired or cancelled; changing its dates moves it to the matching state; a daily job reminds the responsible user before expiry, expires overdue contracts and starts contracts whose start date has arrived.
- [N-U17-167] Renewal alerts use a configurable lead time that defaults to thirty days; vehicles show due-soon and overdue flags.
- [N-U17-168] A work contact cannot be removed from an employee who is linked to a vehicle; changing the work contact updates the vehicle's driver.

### STATE
- [N-U17-169] Contract: new, running, expired, cancelled. Service: new, running, done, cancelled. Vehicle states are configurable lists seeded with request, order and waiting stages.

### OPTIONALITY
- [N-U17-170] The recurring cost fields exist on contracts but the studied source does not generate cost lines; the scheduled job that carries a cost-generation name actually runs the expiry and reminder logic.
- [N-U17-171] An onboarding plan step can assign the fleet manager as responsible for employee plans.

### DEPENDENCY
- [N-U17-172] Vehicles belong to a company; costs reporting and accounting integration are outside this module set.

### CONSTRAINT
- [N-U17-173] Services cannot clear the odometer value; vehicle model is required; the assignment history end date is never filled by the studied source.

### RISK
- [N-U17-174] Assignment history can show overlapping or open-ended periods because the end date is manual. The mislabelled scheduled job may lead operators to expect cost generation.

### UNKNOWN
- [N-U17-175] Cost generation, accounting links and mobility-card use outside the studied modules are unknown.

## CAP-U17-10 Calendar events, attendees, invitations and reminders

### WHAT
- [N-U17-176] Calendar events have an organiser, attendees (partners), time or all-day span, location, optional recurrence, alarms and privacy level. Time off, interviews and other modules create events through it.
- [N-U17-177] Attendees receive an invitation message with a calendar file; they accept, decline or mark tentative from email links or the web client.
- [N-U17-178] Alarms of type email, notification or text message remind attendees before the start.

### WHY
- [N-U17-179] The calendar coordinates availability and keeps participants informed, and HR bridges mark attendees unavailable when outside working time.

### BUSINESS RULE
- [N-U17-180] Employees can read all events, but a private event seen by someone who is not organiser or attendee shows only a busy label and no attendee or detail; editing someone else's private event is refused.
- [N-U17-181] Portal users see only events where they are attendees; portal users have no attendee table access.
- [N-U17-182] The organiser's own attendance is accepted automatically; adding attendees requires write access to the event.
- [N-U17-183] Invitation links use a per-attendee token; a signed-in user whose contact differs from the invited one is refused, and invalid tokens are refused.
- [N-U17-184] Invitation emails are sent only for events in the future and not to the acting user; a system parameter can block all calendar mail; sending is immediate only under a configured batch limit.
- [N-U17-185] Moving a future event notifies existing attendees and resets the organiser acceptance if another user changed the time; recurrence edits distinguish this event, following events and all events.
- [N-U17-186] Reminders are scheduled as timed triggers of a cron job at creation or change; when the job runs it handles alarms due since the last call, skips declined attendees and past events, and re-arms the next occurrence for recurring events; alarms created after their due time are skipped on purpose.
- [N-U17-187] When the company-hours bridge is installed, attendees whose employee schedule does not cover the event interval are flagged unavailable; all-day events on non-working company days produce no interval.

### STATE
- [N-U17-188] Attendee: needs action, accepted, declined, tentative. Event: active or archived; recurrences hold a base event.

### OPTIONALITY
- [N-U17-189] Text message reminders and a bulk SMS action need the SMS bridge and an SMS gateway; video call links and external calendar synchronisation are optional.

### DEPENDENCY
- [N-U17-190] Reminder timing relies on the scheduler and mail queue; text messages rely on an external gateway whose failure behaviour is not visible in this source.

### CONSTRAINT
- [N-U17-191] Attendees cannot be duplicated; duplicated events get fresh attendees.

### RISK
- [N-U17-192] Invitation accept and decline links act with elevated rights using only the token and can be called by anyone holding the link. Default privacy comes from a system parameter and per-user setting; mistakes expose event titles to all employees.

### UNKNOWN
- [N-U17-193] External calendar sync, appointment booking and delivery receipts of reminders were not studied.

## ANCILLARY MODULES — secondary coverage

### WHAT
- [N-U17-194] Presence reporting computes whether employees are present, absent or off-hours from login activity, optionally from network address or sent messages, and lets HR administrators override it and notify absentees by text message or a log note.
- [N-U17-195] Home-working adds a default location per weekday and dated exceptions per employee, with a calendar wizard; a time-off bridge shows absence before location in the presence icon.
- [N-U17-196] Equipment maintenance has requests, stages, teams and equipment; an HR bridge assigns equipment to employees or departments.
- [N-U17-197] Gamification has challenges, goals, badges and ranks, with HR extensions for badge granting and goal visibility.
- [N-U17-198] Small bridges: a hourly cost field, an organisation chart, resource colour and presence status, chat bot and live chat HR views, a CRM challenge example set.

### BUSINESS RULE
- [N-U17-199] The presence job evaluates only the current company of its running user; manual presence marks need an HR administrator.
- [N-U17-200] One exceptional location per employee per day; weekly location changes are written through the user record, so employees without a user would have no effect; the location deletion guard may be too weak.
- [N-U17-201] A maintenance request closing on a preventive recurring request creates the next one; the HR bridge makes every HR officer an equipment manager.
- [N-U17-202] Python goal definitions run restricted code; challenge updates look only at goals of recently active users; rewards are granted at period end or in real time.
- [N-U17-203] HR officers can see all goals; every internal user can grant badges and edit or delete the ones they granted.

### OPTIONALITY
- [N-U17-204] All ancillary modules install automatically with their parents except home-working and presence which are explicit.

### DEPENDENCY
- [N-U17-205] Presence depends on time off and SMS; maintenance bridge depends on HR; gamification bridges depend on sales CRM or HR.

### RISK
- [N-U17-206] Presence only covers the first company when run by the scheduler in a multi-company set-up; the home-working guard and wizard have latent defects; coupling HR officers to equipment management widens their authority.

### UNKNOWN
- [N-U17-207] These ancillary modules were read at a lighter depth than the ten capabilities above.
