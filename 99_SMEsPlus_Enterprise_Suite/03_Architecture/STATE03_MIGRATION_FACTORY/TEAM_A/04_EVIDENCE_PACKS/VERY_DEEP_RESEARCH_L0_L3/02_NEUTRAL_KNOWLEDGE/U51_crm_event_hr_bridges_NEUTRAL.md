# U51 neutral knowledge — CRM, event, HR and gamification bridge integrations

> Neutral knowledge layer. DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION.
> Unit: U51
> Date: 2026-10-02
> Scope: Bridge and extension modules connecting CRM, event management, HR, gamification and IAP services.

---

[N-U51-001] A lead mining service allows sales teams to generate new CRM leads or opportunities by querying a cloud-based company database. Users configure filters such as target countries, industry sectors, company size range, and preferred contact roles or seniority levels. Each company lookup costs one service credit, and contact identification costs an additional credit per contact. A single request can generate up to two hundred leads. Requests store the error state when credits are exhausted or no results are found.

[N-U51-002] A mail plugin bridge extends the email sidebar add-in to show CRM leads associated with the contact currently being viewed in the email client. When the user has permission to create leads, the sidebar displays the five most recent leads by default. A dedicated route allows the add-in to create a new lead from the current email subject and body, linked to the identified contact. Several older routes remain active purely for compatibility with older plugin versions.

[N-U51-003] An event booth management extension introduces the concept of physical exhibition spaces within events. Each booth belongs to a category that carries an image, a description, and a sequence order. Booth templates are defined on the event type, and when an event is created from that type, the available booths are generated automatically. Each booth records the renting partner's name, email, and phone. When a booth is confirmed as reserved, the event's discussion thread receives a notification message. A booth is either available or unavailable.

[N-U51-004] When event registrations originate from a sale order, a bridge module groups those registrations by sale order when checking whether to create or update a CRM lead according to configured lead rules. This means all registrations on the same order are treated as one group rather than generating separate leads per registration.

[N-U51-005] Event tickets are linked to a product in the product catalogue. Each ticket type requires a product configured for event registration service tracking. The ticket price is taken from the product's list price by default, and tax-inclusive prices are computed from the ticket's applicable taxes. A product linked to an event ticket cannot have a different service tracking type; the system enforces this with a validation error. Registrations carry a sale status field indicating whether the ticket is unpaid, paid, or free.

[N-U51-006] An SMS notification extension allows event organizers to schedule SMS messages to attendees alongside email notifications. The notification type on a scheduled communication can be set to SMS, in which case a linked SMS template is used. When the scheduled date arrives, the system sends the SMS to all matching registrations in a mass send. Deleting an SMS template that is referenced in an event communication also removes that communication record.

[N-U51-007] A gamification data module provides ready-made goal definitions and challenge templates for sales and CRM activity metrics. It contains no custom business logic and installs automatically when both gamification and the sales-CRM bridge are present.

[N-U51-008] The core HR module introduces a versioned approach to employee contracts. Each version record holds the employee's personal information, work schedule, job, department, wage, and contract dates. An employee must always have at least one active version. Two active versions for the same employee cannot share the same effective date, and contract periods must not overlap. A version can be created from a contract template that pre-fills a defined set of fields. Work locations define where employees are based, with types of home, office, or other. Discussion channels can be configured to automatically add all members of one or more departments as subscribers. Activity plans targeted at employee records can assign task responsibility to the employee's coach, direct manager, or the employee themselves, with automatic fallback up the reporting hierarchy if the designated person has no linked user account.

[N-U51-009] A module combining leave management with work location tracking adjusts the employee presence icon so that an absent employee on holiday shows a holiday-specific icon rather than the usual work location indicator.

[N-U51-010] A work location extension lets HR managers and employees record where each person works on each day of the week as a standing schedule, and also record one-off exceptions for specific dates. The schedule covers all seven days. The employee's current-day location is derived from the exception for today if one exists, otherwise from the standing weekly schedule. The calendar and list views dynamically substitute the correct day field based on the current weekday at the time the view is loaded. The employee presence icon in the messaging system reflects the current location type. The user's instant messaging status string incorporates a location prefix. Employees and their managers can read and update their own day-of-week location preferences through their user preferences. Deleting a work location that is in use by any employee is blocked.

[N-U51-011] A calendar integration module exposes a method that returns a structured summary of where an employee is working on each day within a given date range, combining the standing weekly schedule with any date-specific exceptions. Partners linked to employees as work contacts can call this method directly. A wizard allows setting a location for a chosen date either as a one-time exception or as the new standing default for that day of the week.

[N-U51-012] An hourly cost module adds a single monetary field to the employee record that stores the employee's hourly cost rate, visible to HR users and tracked for change history.

[N-U51-013] A maintenance integration module links maintenance equipment and requests to employees and departments. Equipment can be assigned to a specific employee, a department, or neither. When equipment is assigned, the relevant employee's user or the department manager's user is automatically added as a follower of the equipment record. Maintenance requests default to the current user's employee. When an employee departs, the departure wizard offers an option to unassign all equipment from that employee, which is enabled by default.

[N-U51-014] A recruitment SMS module adds a button to applicant records that opens the mass SMS composition wizard, allowing recruiters to send text messages to one or more applicants at once.

[N-U51-015] A bridge between HR skills and events allows an employee's resume to include onsite training courses that are represented as event records. When a new event is created in a context that identifies it as an onsite course, the system automatically registers the relevant employee as an attendee. Onsite course resume lines display in a distinctive purple color.

[N-U51-016] A bridge between HR skills and the learning platform records completed online courses on the employee's resume. When an employee finishes a course, a training resume line is created automatically if one does not already exist for that course. The system also posts messages on the employee's chatter when the employee enrols in or leaves a course. Employees can view their course completion progress from their profile. Online learning resume lines display in a teal color.

[N-U51-017] A bridge between HR skills and the survey tool enables certification surveys to automatically create or update an employee's resume when a certification is passed. Each certification survey can specify a validity period in months; after that period the certification is considered expired. Resume lines show an expiration status of valid, expiring soon (within three months), or expired.

[N-U51-018] A timesheet and attendance comparison report combines raw attendance clock records with timesheet entries into a single view showing total attendance hours, total timesheet hours, the difference between them, and the cost equivalent of each using the employee's hourly rate. The report is filtered by project-linked timesheets only and is accessible only to users with timesheet permissions. Attendance dates are converted to the employee's own work calendar timezone before grouping.

[N-U51-019] The HTML builder module at this revision is a front-end-only module providing a visual page editing experience. It contributes no server-side business models.

[N-U51-020] An IAP-CRM bridge adds a technical identifier field to lead records that stores the unique identifier returned by the company intelligence cloud service. This field is carried forward when two leads are merged.

[N-U51-021] An IAP mail bridge enriches the IAP account model with messaging capabilities, adding follower tracking and change history to the account record. It also enables real-time browser notifications when an IAP service completes successfully, fails, or runs out of credits, with the no-credit notification including a direct link to purchase more credits.
