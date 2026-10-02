# U39 Employee records, attendance and Google integrations (part A) — NEUTRAL KNOWLEDGE

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room layer: plain business and process language only (platform: Odoo 19 Community, named once here).
> Each statement carries an identifier in square brackets that links it to restricted technical claims. No file, module, field or code names appear below.
> Scope of this layer: how calendars, mail servers and public forms connect to outside services; how employees, their dated records and contracts are kept; how attendance and extra hours are captured, calculated and approved; and three small bridges to calendars, company vehicles and recognition badges. Personal data is described only as structure and rules. No completeness, coverage or approval is asserted.

## CAP-U39-01 Linking a user's external calendar account and controlling synchronization

### WHAT
- [N-U39-001] Opening the calendar triggers a synchronization request whose answer is one of: administrator configuration needed, user authorisation needed, refresh needed, nothing new, paused, or stopped. Only members of the settings-manager role are offered the shortcut to the configuration screen.

### WHY
- [N-U39-002] The system lets each person see their own Google events next to internal ones and keeps one calendar per user link, so changing the linked calendar discards the old links instead of mixing two calendars.

### BUSINESS RULE
- [N-U39-003] Each user's Google access credential, renewal credential, expiry, change marker and calendar identifier are kept in that user's private settings, readable only by system administrators, never copied with the record, and kept out of the information sent to the browser. A credential counts as usable only if at least one minute of life remains.
- [N-U39-004] Before every Google call the access credential is renewed if it is missing or nearly expired. If Google rejects the renewal as invalid, the stored renewal credential is deleted immediately so the user must reconnect, and the user is advised to check the application identifier and secret.
- [N-U39-005] Authorisation requests full read and write calendar access, offline, with forced consent. Google sends the browser back to a public address on this system with a code that is exchanged for credentials stored on the visiting user. Outgoing requests may only go to Google hosts and the secret is masked in logs.
- [N-U39-006] An administrator-only reset wizard decides what happens to the events a user owns (leave untouched, delete in Google, delete locally, or both) and whether the next synchronization resends all events or only new ones; it always ends by clearing the user's credentials so a fresh authorisation is needed.
- [N-U39-007] A scheduled job runs every twelve hours for every connected, non-stopped user, one user at a time, saving after each and logging a failure without stopping the others. A comment in the job mentions a minimum-delay setting that no code reads.
- [N-U39-008] Each time a user opens the calendar the browser starts a synchronization but waits at most one second before showing local data; a manual button restarts and synchronizes, and sends the user to Google's consent page when authorisation is missing.

### STATE
- [N-U39-009] A user can stop their own synchronization; this only sets a flag and touches nothing in Google. Restarting clears the flag and marks all of that user's calendar items to be sent again.
- [N-U39-010] Synchronization status is one of: missing credentials, active, paused, stopped. A user who never connected is first reported active by the basic check and only shown as stopped by the status the user sees.

### OPTIONALITY
- [N-U39-011] An administrator enters one Google application identifier and one secret for the whole database; the secret is hidden on screen. Without both values nobody can connect their calendar, and users are told an administrator must configure it.
- [N-U39-012] In the studied database the synchronization job exists and is active, but no Google credentials are configured and nobody is connected, so synchronization is idle.

### DEPENDENCY
- [N-U39-013] Calendar synchronization with Google needs only the generic Google sign-in helper and the calendar feature.

### CONSTRAINT
- [N-U39-014] When a copy of the database is prepared for testing, all Google credentials are cleared and every user is marked stopped so the copy cannot write to real calendars.

### RISK
- [N-U39-015] A single switch pauses synchronization for every user at once. Whether an ordinary user could flip that switch through a direct call is not settled by the code and needs a runtime check.

### UNKNOWN
- [N-U39-016] Whether the live Google consent, renewal and rate-limit behaviour works as the code suggests, and whether ordinary users can pause synchronization for everybody through a direct call, was not tested and needs a runtime check.

## CAP-U39-02 Two-way synchronization of calendar events with an external calendar service

### WHAT
- [N-U39-017] Every synchronizable record carries a Google identifier, a needs-sending flag (true by default) and an active flag. Editing any synchronized field marks it for sending unless the editing user stopped synchronization, and after an edit the change is sent immediately with a short timeout when synchronization is not paused.

### WHY
- [N-U39-018] Google calls are deferred until the local change is saved so that Google only ever sees changes that really happened, and so a failed creation is not duplicated in Google.

### BUSINESS RULE
- [N-U39-019] Calls to Google are made only after the local database transaction has committed, so Google never sees a change that was rolled back; a failure in that late step is logged and swallowed, and a context flag can switch outgoing synchronization off for a single operation.
- [N-U39-020] Outgoing selection covers events the user attends within a window of one year back and one year ahead (adjustable by a system parameter), excluding instances that follow their series, and sends at most 200 records per run; the remainder is sent by later runs.
- [N-U39-021] Incoming changes are split into new, cancelled and changed items: new ones are created without being sent back, cancelled ones are cancelled locally, and a rescheduled instance of a series replaces the stale local record.
- [N-U39-022] When Google refuses a change (bad request or no permission), the event gets an internal note explaining that it will not sync until it is edited again; for a series, all its events stop syncing so one failure does not spread.
- [N-U39-023] When Google already handles an event, the application does not send its own status-update emails or its own email reminders for it, and guest notification from Google is requested only if the event is not already over.
- [N-U39-024] Identifiers for instances of a recurring series are the series identifier plus the original start time in compact form; events inserted without an identifier get a random one generated locally.
- [N-U39-025] A single event turned into a series keeps an inactive copy carrying the old identifier so the next synchronization deletes it in Google; incoming changes to a series' first event time or to its rule rebuild the instances; series deletion is sent as one request so only one notification is mailed.
- [N-U39-026] Events are translated field by field: title, description, location, all-day or timed start and end, reminders, attendees that have an email, organiser, guest permission, privacy and free-or-busy; an all-day event coming from Google is shown from 08:00 to 18:00 with Google's exclusive end date handled; attendee emails without a matching contact are skipped and attendees missing in Google are removed.
- [N-U39-027] Remote calls for an event use the organiser's credentials when the organiser has them, otherwise the current user's; sending is blocked when the organiser differs from the sender so Google shows the right organiser; attendee accept, decline and tentative answers are pushed to Google, and a cancellation by Google deletes only the organiser's copy while others see a declined answer.
- [N-U39-028] A synchronization run first tries to lock the user and silently skips if another run holds the lock; it is a full download when no change marker is stored, otherwise incremental, follows Google's paging, and repeats as a full download if Google says the marker is no longer valid.
- [N-U39-029] Google items are matched to local records first by stored identifier and then by the local identifier hidden in their extended properties, considering only local records without a Google identifier; cancelled items carry no series information, so their kind is resolved by lookup.
- [N-U39-030] Birthday-type Google events are ignored on import.

### STATE
- [N-U39-031] A record that has a Google identifier is never really deleted locally at first; it is archived, which sends a cancellation to Google, and it is removed locally only when the cancellation comes back. A remote deletion that Google reports as already gone counts as success.

### OPTIONALITY
- [N-U39-032] A new event with no location and no video link asks Google to create a video-conference link; an existing event without a link sends an empty conference.

### DEPENDENCY
- (no statement recorded for this section)

### CONSTRAINT
- [N-U39-033] Guests may not change synchronized fields of an event whose Google permissions restrict editing to the organiser; the check is skipped when restarting synchronization, resetting an account, or changing unsynchronized fields. Because of a coding detail the check runs on every write, not only when the writer differs from the organiser.

### RISK
- [N-U39-034] When the same item changed on both sides, the newer update wins, comparing Google's update time with the local write time captured before applying changes; the code itself warns this is unreliable if the two servers' clocks differ.
- [N-U39-035] Attendee email addresses arriving from Google are matched to contacts with a find-or-create helper, so unknown addresses may create new contacts in the address book.

### UNKNOWN
- [N-U39-036] The recurring-event engine of the calendar feature itself and the effect of clock differences on the newer-update-wins rule were not examined; only the Google-specific additions were.

## CAP-U39-03 Connecting incoming and outgoing mail servers to Gmail with delegated sign-in

### WHAT
- [N-U39-037] Any mail server record can carry an active flag, a renewal credential, an access credential and an expiry; the credentials are visible only to system administrators and are not copied with the record.

### WHY
- [N-U39-038] Mail credentials are protected from being replaced or disconnected by an outsider who tricks an administrator into following a link, which is the purpose of the signed value in the consent request.

### BUSINESS RULE
- [N-U39-039] Linking a server is an explicit button rather than an automatic redirect, so the record is saved first and its identifier can be carried in the consent request. The request asks for full mail access (sending and reading), offline, with forced consent; the action requires an administrator environment and a valid email address on the server.
- [N-U39-040] Credential requests go to Google with a five-second timeout and any failure becomes a generic message. An access credential is renewed ten seconds before expiry and saved with its new expiry whenever mail is sent or fetched.
- [N-U39-041] The return address after consent requires a signed-in user, checks the record kind, existence and signed value, saves and activates the credentials, and sends administrators back to the server form or personal users to their preferences.
- [N-U39-042] Choosing Gmail authentication on an outgoing server prefills host, secure mode and port; it must have no password, secure mode and a username; the sending filter is set to that address so only a matching sender can use it unless a default-sender parameter widens it; sending authenticates with the token instead of a password.
- [N-U39-043] Incoming Gmail servers prefill host, secure connection and port, require a secure connection, always use the mailbox protocol with token-based login and then open the inbox.
- [N-U39-044] Internal users can link their own address as a personal outgoing server: an inactive server is created, the Gmail connect step runs with elevated rights so ordinary users can finish it, and unfinished or orphaned personal servers are removed by an automatic cleanup.
- [N-U39-045] Connect buttons and the token-valid badge are shown only to system administrators, and failures show a simple warning page with a link back.

### STATE
- (no statement recorded for this section)

### OPTIONALITY
- [N-U39-046] Direct linking is used only when the Gmail application identifier and secret are both set in the settings; the secret is hidden on screen.
- [N-U39-047] Without own credentials, a hosted broker service can mediate the link, but in the free Community edition the connect action refuses and asks for credentials, while the renewal step still falls back to the broker when no credentials exist; the broker path is therefore only usable in Enterprise.
- [N-U39-048] In the studied database no mail server of either kind exists and no Gmail credentials are set, so no Gmail connection is configured.

### DEPENDENCY
- [N-U39-049] The Gmail connection feature depends only on the mail feature and installs itself automatically whenever the mail feature is present.

### CONSTRAINT
- [N-U39-050] For personal servers and for connections made by non-administrators, the Gmail account actually authorised must have a verified email equal to the server's address, otherwise an error page is shown and nothing is saved.

### RISK
- [N-U39-051] The consent request carries a signed value derived from the record kind and number, intended to stop an outsider from making an administrator replace or disconnect mail credentials; the value does not include the user or session, so anyone holding the link for a record has a valid value for it.

### UNKNOWN
- [N-U39-052] The hosted broker path, actual acceptance of token-based login by Gmail, and the schedule of mail fetching were not examined and need a runtime check.

## CAP-U39-04 Bot protection of public forms with an external risk-scoring service

### WHAT
- [N-U39-053] For a state-changing request on a protected form, the server removes the token from the request, asks Google to rate it with the secret and the visitor's address, and raises a validation error for an invalid secret or token, a user error for time-out or malformed request, and a generic suspicious-activity error for bots or a wrong action.

### WHY
- [N-U39-054] The check exists to keep automated bots from spamming public forms such as sign-up and contact forms.

### BUSINESS RULE
- [N-U39-055] The public site key is added to the information sent to the browser only when it exists and the feature is on.
- [N-U39-056] Any route that declares a protection action is checked on every non-safe request method; sign-up, password reset, the generic website form and the forum follow form declare one, and without the feature installed the check does nothing.
- [N-U39-057] The login page checks the protection only for password credentials, and a context flag can bypass it.
- [N-U39-058] A successful answer is classed as a bot when its score is below the configured minimum; a missing score counts as zero, and a missing minimum would raise an error because it is read without a default.
- [N-U39-059] The action name returned by Google is compared with the expected action for the form, and a mismatch is refused.
- [N-U39-060] In the browser, forms with a protection attribute load Google's script with the site key, fetch a token for the form's action and attach it as a hidden field before submitting; if no token can be obtained the form is still submitted without one, and a short legal notice linking to Google's terms is available.

### STATE
- (no statement recorded for this section)

### OPTIONALITY
- [N-U39-061] Settings hold an on-off flag (on unless explicitly off), a public site key, a secret key and a minimum score (default 0.7); all are visible to system administrators only, and the settings text states that without keys no checks are made.

### DEPENDENCY
- [N-U39-062] The bot-protection feature depends on the base settings screen, from which it is installed by ticking a box.

### CONSTRAINT
- [N-U39-063] Preparing a test copy of the database empties both reCAPTCHA keys, so verification switches off in the copy.

### RISK
- [N-U39-064] When no secret key is set the result is treated as success, so protection is silently off; the studied database is in this state.
- [N-U39-065] If Google does not answer within two seconds, or answers badly, the request is refused, so a Google outage blocks the protected forms rather than letting them through.
- [N-U39-066] Failure log lines include the submitted token and the visitor's address, and one log message uses a wrong format placeholder for the action name.

### UNKNOWN
- [N-U39-067] Real scoring responses, the effect of proxies on the visitor address, and which public forms a deployment protects were not examined.

## CAP-U39-05 Employee master record, dated versions, contracts and the linked user and contact

### WHAT
- [N-U39-068] An employee's personal, work and contract data are kept in dated versions; the same kind of record with no employee attached serves as a reusable contract template.

### WHY
- [N-U39-069] Fields that only exist on the full employee record are limited to HR officers so that users without that access never load them, protecting personal and contract data.

### BUSINESS RULE
- [N-U39-070] Contract dates, trial end, wage, contract type and salary structure are visible only to HR administrators, while personal, identity and passport details need the HR officer role; the wage is a monthly gross amount.
- [N-U39-071] Creating or loading from a contract template copies only job, department, contract type, salary structure, wage, working hours and HR responsible, and values passed explicitly take priority over the template.
- [N-U39-072] A version's effective start is the later of its own date and the contract start; its end is the earlier of the day before the next version and the contract end. Changing contract dates on one version moves them on every version of the same contract, edits mixing several contracts are refused, and for an employee with a single version the version date follows the contract start.
- [N-U39-073] The hourly equivalent of a wage assumes a monthly salary (wage times twelve divided by fifty-two divided by weekly hours), zero when the schedule has no hours, and the plain wage for employees with no schedule, who are treated as paid by the hour; distances in miles convert to kilometres with a fixed factor.
- [N-U39-074] The working-hours calendar of the current version is mirrored onto the employee's resource, and the time zone of a version is its calendar's zone, otherwise the employee's.
- [N-U39-075] Each version has a required HR responsible, defaulting to the creator and limited to internal HR officers of the company.
- [N-U39-076] When an employee is created, submitted values are split between the employee and its version, and version values the creator may not write are silently dropped.
- [N-U39-077] An employee's salary can be split across several bank accounts, each entry being a percentage or a fixed amount with an order; removing an account moves its percentage to the first account, new accounts share what is unallocated, each percentage lies between 0 and 100 and percentages must total exactly 100; the primary account is the first by order, and its payment trust flag can be toggled. When the work contact changes, accounts move to the new contact and lose their outgoing-payment trust.
- [N-U39-078] An employee counts as newly hired for 90 days after creation, and age is computed in whole years from the birthday.
- [N-U39-079] Employees get a work contact created automatically; work phone and email mirror it only when that contact belongs to at most one employee; the coach follows the manager unless set otherwise; linking a user copies partner, picture and time zone and strips the contact from other user-less employees of the same company that used it.
- [N-U39-080] Creating an employee groups the work by company, creates the work contact and a generated avatar, subscribes the employee to channels of the department and logs a note recommending an onboarding plan; writing unsubscribes an old work contact, copies a changed time zone to the user, records who modified version data and re-subscribes department channels; deleting an employee also deletes its resource.
- [N-U39-081] A daily job creates a to-do for the HR responsible when a contract ends exactly after the company's notice period (default 7 days) or a work permit expires exactly after its notice period (default 60 days). Because it tests equality with one day, a day on which the job does not run gives no notice for that employee.
- [N-U39-082] Bulk user creation skips employees that already have a user, lack a valid work email, share an email with another employee or match an existing user, reports each group, and warns that new users get default rights and may raise the subscription cost.
- [N-U39-083] Expected working time is built from each version in contract using that version's calendar (or the company's) and company leaves; the effective time zone is the working-hours calendar's, then the employee's, then the company calendar's, then UTC.
- [N-U39-084] Editing personal fields from the user side notifies the employee's HR responsible with the labels of the changed fields (not their values); name, email, picture and time zone of a user are also pushed to the linked employee records; users can be created together with, or bound to, an employee, and creating an employee from a user requires access to the active company.
- [N-U39-085] A leave of an employee takes the calendar of the version in effect when it starts, calendar validity for employees who ever had a contract comes from their contracts, and leaves can be moved between calendars from a start date.

### STATE
- [N-U39-086] The current version is the latest version dated today or earlier, or the first if all lie in the future, and a daily job refreshes it. A new version copies the one in force at the chosen date (or returns the existing one if it starts that day), a new contract ends the day before the next future contract, and first-employment dates treat versions separated by four days or more as separate occupations.
- [N-U39-087] Archiving an employee clears manager and coach links on other employees and, for a single employee, opens the departure wizard; unarchiving clears the stored departure reason, description and date; changing an employee's company shows a warning to create a new employee instead.
- [N-U39-088] With login-based presence, an online user is present, an offline user inside working hours is absent, others are off-hours, and archived employees show as archived.

### OPTIONALITY
- [N-U39-089] Users can edit their own private address, phones, emails, emergency contact, bank accounts, badge, PIN and a few other fields from their preferences, and that form is loaded with full rights so restricted fields can be shown for their own data.
- [N-U39-090] In the studied database there is one employee with one version, no departure data, no job positions, twelve contract types, three departure reasons and work locations, and four salary structure types of which two belong to a foreign country.

### DEPENDENCY
- (no statement recorded for this section)

### CONSTRAINT
- [N-U39-091] A contract end needs a contract start; two active versions of one employee cannot share an effective date; contract periods of one employee may not overlap, although versions sharing the same start and end count as one contract; a new contract needs the current one to have an end date; and social security numbers are accepted as any text unless a country feature adds a rule.
- [N-U39-092] Badge identifiers are unique and limited to 18 letters and digits, a PIN must be digits only, and one user can be linked to only one employee in a given company.
- [N-U39-093] Users without read access to the full employee record still get search results, names and lists from a restricted public view containing only non-sensitive columns, requests for private fields raise an access error, a context marker lets such users assign employees in many-to-many fields on other records, and the view is rebuilt whenever the feature is initialised.
- [N-U39-094] A contact linked to an employee cannot be deleted, only archived, and the employee's private address is added to that contact's list of addresses.
- [N-U39-095] Bank accounts of employees are hidden from ordinary internal users and shown to HR officers; where they are listed, ordinary users see them masked except for the first two and last four characters.
- [N-U39-096] A user sees employees of allowed companies and, even outside them, their own record, their own manager and their own direct reports.

### RISK
- [N-U39-097] Nationality, identification, social security and passport numbers, private address, marital status and dependants are all change-tracked, so every edit stays in the version's history; the data is personal and its retention follows the message history.
- [N-U39-098] Two helper routines default their date argument to the day the code was loaded rather than to the current day, so a caller omitting the date after midnight would use a stale day.

### UNKNOWN
- [N-U39-099] The full employee form and card views, the behaviour of the restricted public employee access under limited roles, and any country-specific identity-number rules were not examined.

## CAP-U39-06 Employee departure, onboarding and offboarding plans, and related notification hooks

### WHAT
- [N-U39-100] Registering a departure records a reason, an optional description and a contract end date, which may not precede the start of any selected employee's current contract; employees are archived by the wizard only in a termination context, otherwise only the departure data is stored; officers can also set the end date on the current contract.

### WHY
- [N-U39-101] The departure checks make sure a user account is not removed while other employee records still depend on it.

### BUSINESS RULE
- [N-U39-102] Onboarding and offboarding plans assign activities to the employee's coach, manager or the employee; if that person has no user the activity climbs the management chain to the first manager who has one, otherwise it falls to the person launching the plan with a warning, and a management loop without any user gives an error. For employees the default plan date is thirty days away when the earliest start date is past or closer than thirty days.
- [N-U39-103] Group channels can automatically subscribe all active users of chosen departments, refused for direct and group chats, and re-applied when employees join a department or the list changes.

### STATE
- (no statement recorded for this section)

### OPTIONALITY
- [N-U39-104] An Onboarding plan (set up IT materials, plan training, training) and an Offboarding plan (knowledge transfer, take back materials) are seeded for the main company.

### DEPENDENCY
- (no statement recorded for this section)

### CONSTRAINT
- [N-U39-105] A user is archived with the departing employee only if every employee linked to that user is part of the wizard, otherwise the user stays active and a warning names the user.
- [N-U39-106] HR administrators may edit activity plans and plan activities for employees only.

### RISK
- [N-U39-107] A mail address can be restricted so that only senders linked to registered employees may write to it; the sender is matched by a contains-style comparison on the From header alone, so a forged or partial address could pass.

### UNKNOWN
- [N-U39-108] The underlying activity scheduling engine used by plans and the behaviour of the employee-restricted mail alias with real inbound mail were not examined.

## CAP-U39-07 Organisation structure, reference lists, menus and payment-account splitting

### WHAT
- [N-U39-109] Departments form a tree without cycles with a stored path, take the company of their parent, and changing a department's manager moves employees who reported to the old manager to the new one; users without full employee access see only the departments they manage and their descendants, and a hierarchy view lists parent, department and children with counts.

### WHY
- [N-U39-110] Employee bank accounts exist to pay salaries, which is why the salary can be split across them and why their trust and visibility are controlled.

### BUSINESS RULE
- [N-U39-111] The allocation wizard shows one line per bank account from the employee's distribution, errors if an account is missing, rounds amounts down to cents on saving, updates each account's trust flag and requires percentages to total exactly 100.
- [N-U39-112] Applying a contract template writes only the whitelisted values onto the employee and remembers the template on the current version; selectable templates are those of the active company with no employee.
- [N-U39-113] A printable badge shows company logo, picture, name, job title and a barcode of the badge identifier; a digest tip embeds an image from an external vendor host, so rendering that email contacts the host; a department-manager filter limits report rows to the user's own record and managed departments.

### STATE
- (no statement recorded for this section)

### OPTIONALITY
- [N-U39-114] Twelve contract types without country, three work locations and four salary structure types are seeded in the base feature, of which two (for one foreign country) are sample data not meant for this deployment.
- [N-U39-115] Company settings choose how presence is determined (login, email count, IP address, attendance) and define extra employee properties.
- [N-U39-116] Officers get a full employee list, every internal user gets a restricted directory and a departments menu, administrators get configuration and contract templates, the contract types menu is inactive by default, the settings entry is limited to system administrators, and the attendance checkbox in settings is bound to a company flag.

### DEPENDENCY
- [N-U39-117] The employee feature depends on base settings, digest, phone validation, resource mail and the web client, and is an application.

### CONSTRAINT
- [N-U39-118] A job position name is unique per company and department, the recruitment target cannot be negative, and forecast headcount equals current employees plus the target; the recruiter defaults to the creator and is visible to HR officers only.
- [N-U39-119] Contract types and departure reasons can be tied to a country and are visible only if untied or matching a country of the user's companies; a contract type's code defaults to its name; the three seeded departure reasons cannot be deleted; work locations have a type and a required address; tags have unique names.

### RISK
- (no statement recorded for this section)

### UNKNOWN
- [N-U39-120] No payroll consumer of the salary split exists in the free edition, and the department and job screens and the organisation chart were not examined.

## CAP-U39-08 Attendance recording, kiosk, automatic check-out and absence detection

### WHAT
- [N-U39-121] An attendance has a check-in, an optional check-out, a local-day date, worked hours, overtime hours, validated hours and a status; regular hours are worked minus overtime; closed attendances over 16 hours or technical entries, and open ones older than a day, are flagged; only attendance managers get their own employee by default; overtime lines belong to an attendance through employee and exact check-in time.

### WHY
- [N-U39-122] The absence job exists so that a full day of unjustified absence can still produce negative extra hours, which is only possible if there is an attendance record to attach them to.

### BUSINESS RULE
- [N-U39-123] Installing attendance makes companies that control presence by sign-in also control it by attendance, and uninstalling reverses this, for the companies the installer can see.
- [N-U39-124] Every creation, deletion, or change of employee, check-in or check-out regenerates the overtime lines of the affected days, widened to whole weeks when weekly rules apply, padded by a day for time zones, using the rule set of the employee version valid at check-in; attendances whose version has no rule set get no overtime lines.
- [N-U39-125] When device tracking is on, each check-in and check-out stores a location text, coordinates, the visitor's address and browser, falling back to the visitor's approximate location; the location text comes from the approximate location or from a reverse lookup that sends the coordinates to a public map service; with tracking off only the mode is stored; map buttons open an external map page.
- [N-U39-126] The kiosk is opened through a secret key in a public address that is unique per company and can be regenerated by attendance managers; a password-protected session is logged out when opening it, a trial or password-less session opens the settings mode, and the page lists departments with counts; a demo loader and a trial button exist for administrators.
- [N-U39-127] Employee grouping in the attendance list is limited to managed employees for officers, the attendance tab appears for managers, approvers and the employee themselves, and the presence icon follows company presence settings.
- [N-U39-128] Overtime totals are the sum of approved lines' encoded durations; approving or refusing an attendance acts on all its lines; editing a line recomputes the linked attendance; a database rule against overlapping lines exists only as commented code.
- [N-U39-129] Every four hours a job closes forgotten open attendances of employees with a fixed schedule in companies that enabled it: when elapsed time plus earlier hours that day minus a tolerance exceeds the expected hours, check-out is set to the end of the local day minus the excess (never before one second after check-in), the exit mode is marked automatic and a note is posted. The comparison uses a time conversion that assumes the server runs in UTC.
- [N-U39-130] Every four hours a job looks at the previous day (by server date) for employees of companies with absence management, with a fixed schedule, a started contract and no overtime line that day; it creates a one-second technical attendance so the engine can produce negative overtime, keeps it only if an overtime line results, and posts an explanatory note; employees who worked part of the day are skipped.
- [N-U39-131] Attendance times are localised to the time zone of the version valid on the check-in date, and an attendance spanning midnight is cut per local day and per week for quantity rules.
- [N-U39-132] Each employee can have an attendance approver who must be an internal user of the company; naming one adds the user to the attendance officer role in elevated rights, and removing the last approval removes the role.
- [N-U39-133] Month-to-date and today's hours are computed in the employee's time zone, counting only closed attendances for the month and including the open one for today.
- [N-U39-134] For regeneration the system builds, per employee and per dated version, the leave, work and lunch intervals from the version's calendar and treats versions without calendar as fully flexible.
- [N-U39-135] A rule set can be chosen on a version only if it has no country or its country matches an active company; each date is mapped to the latest version starting on or before it because end dates are not stored.
- [N-U39-136] Session loading adds the user's attendance payload for the top bar; kiosk employee answers add name, picture, overtime balances, overtime logged today and display options.

### STATE
- (no statement recorded for this section)

### OPTIONALITY
- [N-U39-137] A demo scenario loader creates sample employees, schedules and about a month of generated attendances, and refuses to run if sample data already exists.
- [N-U39-138] Company settings include kiosk delay (10 seconds), PIN identification, clock-in from the top bar, overtime validation mode, automatic check-out with a two-hour tolerance, absence management and device tracking, all off by default except the delay, the kiosk mode and the barcode source.
- [N-U39-139] In the studied database both attendance jobs are active every four hours, the company has automatic check-out, absence management, device tracking, PIN identification and kiosk mode all switched on, no attendance exists yet, and the only employee version has no overtime rule set.

### DEPENDENCY
- [N-U39-140] Attendance needs the employee feature, the barcode scanning feature and the geolocation feature.

### CONSTRAINT
- [N-U39-141] An employee may not have two open attendances, overlapping attendances, or an attendance nested inside another; check-out cannot precede check-in.
- [N-U39-142] Every internal user can read their own attendances; officers see and edit only employees they approve, the user role sees all, and administrators have full access; the company rule on attendances admits employees without a company while the rule on overtime lines does not, and officers see overtime lines of managed employees without the own-employee clause.

### RISK
- [N-U39-143] An older overtime engine and two company tolerance settings remain in the code marked for removal; the engine has no live caller and the tolerance settings are hidden and read by nothing, so they have no effect.
- [N-U39-144] The kiosk key alone, without PIN or badge, returns an employee's name, picture, hours and overtime balances for any employee of the company and lists employees with job and status; the list request does not cap the page size, so the key acts as a bearer secret for that data.

### UNKNOWN
- [N-U39-145] The kiosk screens, the attendance reports, demo data, and the time-zone behaviour of the two scheduled jobs on a server not set to UTC were not examined.

## CAP-U39-09 Overtime rules, rule sets and the overtime ledger

### WHAT
- [N-U39-146] A rule set owns its rules, has an optional company and country, an active flag and a rate combination mode (highest rate, or sum of excesses); a button regenerates overtime for all attendances of employees using it, from the earliest version start among them.
- [N-U39-147] A rule is either quantity-based (hours beyond an amount per day or week, from the schedule or a fixed figure) or timing-based (on non-working days, within a time window, outside a named schedule, or when off); timing hours must lie within a day.

### WHY
- [N-U39-148] Two bases exist because extra hours arise either from exceeding an amount of work per day or week or from working at particular days or times, and the two cannot be expressed by one threshold.

### BUSINESS RULE
- [N-U39-149] Timing windows are built in the employee's time zone from midnight plus the start hour, with a stop of 24 meaning the end of the day.
- [N-U39-150] Quantity rules compare worked time (lunch removed, clipped to the day or week) with expected time (from the schedule, the contract or the rule), allocate the excess as the trailing time of the period starting from the earliest attendance, skip fully flexible employees, evaluate weekly rules over the six days before each day, and cap daily expectation by what remains of a weekly target for flexible schedules.
- [N-U39-151] With absence management on, a shortfall beyond the employee tolerance becomes a single negative entry attached to the last attendance of the period instead of overtime.
- [N-U39-152] Timing rules use precomputed intervals per employee for leave, working days (schedule work minus leave, or whole days for flexible schedules), non-working days as the inverse, and time outside a chosen calendar, over a window padded by a day; windows that wrap midnight are the complement of the interval between the two hours.
- [N-U39-153] Quantity rules are evaluated first, grouped by period, then timing rules; only quantity rules can produce shortfalls.
- [N-U39-154] Where intervals from different rules overlap, they are split into segments each labelled with the set of rules covering it, so that a combined rate is applied per segment.
- [N-U39-155] The line pay rate is zero when no applicable rule is paid; with the highest-rate mode it is the largest paid rate (ties broken by order); with the sum mode it is one plus the sum of each paid rate's excess over one; with the time-off bridge, rules that can be converted to time off add their whole rate in sum mode and the line records that it can be converted.
- [N-U39-156] The rule list shows a short description such as hours per day or week, taken from the employee, or outside a named schedule.

### STATE
- [N-U39-157] One ledger line is produced per attendance, local day and rule combination, with start and stop of the attendance and duration rounded to four decimals; shortfall lines are dated by check-in in the employee's zone and keep only the largest entry per attendance; lines start as to approve or approved depending on the company validation mode.

### OPTIONALITY
- [N-U39-158] A default rule set (a quantity rule based on the schedule and a rule for non-working days, both paid at rate 1.0) and a sample rule set for another country (day overtime 1.25, two night windows and non-working days at 1.5, none flagged paid so their lines would carry rate zero until switched on) are seeded; the sample set is foreign data, not Thai practice.
- [N-U39-159] In the studied database two rule sets and six rules exist, no overtime line exists, and the single employee version has no rule set.

### DEPENDENCY
- (no statement recorded for this section)

### CONSTRAINT
- [N-U39-160] Each rule has an employer tolerance and an employee tolerance in hours: overtime counts only when it strictly exceeds the employer tolerance (for timing rules, the total within one attendance), and a shortfall counts only beyond the employee tolerance.
- [N-U39-161] Rules and rule sets are fully writable only by attendance administrators; HR administrators and attendance officers can read rules, and HR administrators can read rule sets; the record rule meant to bind the manager role is stored as a global rule with no role attached.

### RISK
- [N-U39-162] The older timing engine includes a leave-based branch that is commented as completely untested, and the live engine uses different leave handling, so behaviour differs from what the older code suggests.

### UNKNOWN
- [N-U39-163] The overtime calculations were read but not run: results on real schedules, leaves, time-zone changes and very short intervals need execution to confirm, and no Thai statutory overtime rate is asserted.

## CAP-U39-10 Employee-aware bridges: calendar availability, company vehicles and recognition badges

### WHAT
- [N-U39-164] An attendee who is an employee is flagged unavailable for a meeting when the part of the meeting inside their working schedule is shorter than the meeting, so partial overlap counts as unavailable; only complete events with attendees are checked.
- [N-U39-165] Each vehicle's driver and future driver are also linked to an employee: the employee is found from the driver contact within the same company, and the first one is taken if several match.
- [N-U39-166] A granted badge can carry an employee link which must be one of the receiving user's employee records; an employee's badges are those linked directly or only through the user, colleagues can see them on public profiles, and a badge shows how many employees received it.

### WHY
- [N-U39-167] An all-day event on a day when the company is closed is not judged against individual schedules, because there is no working interval to compare.
- [N-U39-168] The fleet bridge keeps a history of the company cars each employee has driven.
- [N-U39-169] The gamification bridge lets people recognise employees, not just users, with badges that appear on the employee's profile.

### BUSINESS RULE
- [N-U39-170] For all-day events the interval is the working time of the viewer's active company calendar, an all-day event spanning a day with no working time is skipped, and timed events use their own start and stop.
- [N-U39-171] A partner's schedule is the union of the schedules of their employees, each built from the working calendar valid in each dated period, falling back to the company calendar for fully flexible employees; when merged, a time counts only if all employees work.
- [N-U39-172] For day and week views the calendar shades non-working time using the intersection of the selected attendees' working hours in the viewer's time zone, and greys the whole week when there is no common working time.
- [N-U39-173] Setting the driver employee sets the driver contact to that employee's work contact, and setting the driver contact finds the employee only when exactly one employee matches; the same holds for the future driver.
- [N-U39-174] When the driver employee of a vehicle changes, the previous driver and the previous employee's user are unsubscribed from the vehicle's followers.
- [N-U39-175] Employees show a count and history of their cars and a combined license plate with their private plate; the work contact of an employee with linked cars cannot be cleared, and changing it updates driver and future-driver contacts on their vehicles.
- [N-U39-176] Assignment-history rows get a stored employee link and can carry attachments through a dedicated list and upload view.
- [N-U39-177] A vehicle contract, service and odometer log shows the vehicle's driver employee; a service's purchaser defaults to that employee and then to the employee's work contact.
- [N-U39-178] Activity plans for employees can assign work to the fleet manager of the employee's first vehicle, falling back to the launching user with a warning, with an error when the employee has no vehicle; a Take Back Fleet step is added to the offboarding plan.
- [N-U39-179] The departure wizard gains a Release Company Car option, on by default for fleet officers; when ticked, open assignment-history rows of the departing employee's contacts get the departure date as end date and the driver is cleared on every vehicle with those contacts, without an explicit company filter; this is the only code found that ends a history row.
- [N-U39-180] The grant wizard lets the sender pick an employee, determines the user from it, refuses a grant to the sender, creates the grant with the user's employee link (which could differ from the one picked when a user has several employee records) and sends the badge notification.
- [N-U39-181] The badge notification carries a View Your Badge button that opens the employee profile on the badges tab with the badge highlighted, and clicking the notification in the messaging menu does the same.
- [N-U39-182] An employee's goals are the goals of the linked user restricted to challenges in the HR category, visible to HR officers only.
- [N-U39-183] A Badges tab with a Grant a Badge button is added to the employee and public profile forms for employees with a linked user, and a Challenges menu under HR configuration lists badges for everyone with menu access and challenges and goals for HR officers.

### STATE
- (no statement recorded for this section)

### OPTIONALITY
- [N-U39-184] A My Team filter on attendees selects people whose department is managed by the viewer.
- [N-U39-185] The calendar bridge seeds only two views and extends two models in the studied database; it adds no access rows, rules or jobs.
- [N-U39-186] In the studied database no vehicle or assignment history exists; the bridge adds one access row, one record rule and one plan activity.
- [N-U39-187] In the studied database the bridge adds five access rows and four record rules matching the source, four menus, and no cron.

### DEPENDENCY
- [N-U39-188] The calendar bridge depends on the employee and calendar features and installs itself when both are present, so customers do not opt in separately.
- [N-U39-189] The fleet bridge depends on the employee and fleet features and installs itself when both are present.
- [N-U39-190] The gamification bridge depends on the gamification and employee features and installs itself when both are present.

### CONSTRAINT
- [N-U39-191] A mobility card is held on the employee, shown on their vehicles, editable by fleet officers and readable on the public profile; editing it refreshes the cards shown on vehicles.
- [N-U39-192] HR officers may read vehicles that have a driver or future driver employee, by a read-only record rule and access row kept in no-update data, and open the driver's employee record from vehicle and contract forms.
- [N-U39-193] HR officers manage all challenges, badges and grants and may read and edit but not create or delete goals; every internal user can read all grants but change only those they created; all four rules are in no-update data.

### RISK
- [N-U39-194] Attendees are mapped to employees by work contact within the viewer's allowed companies using elevated rights, so any calendar user obtains schedule information for attendees even if employee records are otherwise restricted.

### UNKNOWN
- [N-U39-195] Unusual days shown in the calendar are those of the viewing user's own employee record per dated version; what happens when the calendar sends no end date is not settled by the code and needs a runtime check.
- [N-U39-196] The recognition engine (challenges, ranks), the vehicle cost screens and the calendar shading display were not examined.

