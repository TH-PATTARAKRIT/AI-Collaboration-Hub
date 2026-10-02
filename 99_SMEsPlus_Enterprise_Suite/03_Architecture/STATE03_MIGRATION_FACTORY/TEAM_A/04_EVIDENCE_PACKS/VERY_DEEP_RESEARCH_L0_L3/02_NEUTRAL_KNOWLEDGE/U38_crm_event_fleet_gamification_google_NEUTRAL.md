# U38 — CRM, events, fleet, gamification and Google integrations — Neutral Knowledge

> Clean-room layer. Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source product: Odoo 19 Community.
> No file names, technical names, code, SQL or line numbers appear below. Runtime behaviour was not observed; items marked as risk or unknown require a run.

## CAP-U38-01 Predictive lead scoring

### WHAT
- [N-U38-001] Purpose: rank open opportunities by their likelihood of being won, learning from the company's own history of won and lost leads, separately per sales team, without manual rules.

### WHY
- [N-U38-002] Rationale: the history table is kept current by small increments at every win or loss, and rebuilt in one pass only when the scoring criteria or the reference date change, which limits recomputation cost.

### BUSINESS RULE
- [N-U38-003] Predictive lead scoring computes a lead probability from the history of won and lost leads; a frequency table stores, per field and value pair, how many won and how many lost leads carried that value.
- [N-U38-006] In batch mode only active leads of the given set with pending won status are read, in one grouped read; without a batch filter each lead is read record by record instead.
- [N-U38-010] A combined bucket sums the frequencies of every team and is used for leads without a team or whose team has no frequency rows.
- [N-U38-013] For the stage variable the won and lost denominators are the team-level totals; for other variables they are the per-variable totals.
- [N-U38-014] The won score starts at the team prior and is multiplied by each variable value's won share; the lost score is built the same way from lost shares. Values never seen in the table are ignored for that lead.
- [N-U38-023] Probabilities are computed in chunks of 50000 leads and written in chunks of 5000.
- [N-U38-024] Scores are written with a direct bulk update that sets the automated probability and replaces the manual probability only when it was equal to the automated one or empty; leads are grouped by identical new probability to reduce round trips.
- [N-U38-027] A rebuild covers every won or lost lead created on or after the start date and every team including archived teams, plus the no-team bucket.
- [N-U38-032] Team won and lost totals are read from the first team-independent stage by sequence because every won lead increments all stages and every lost lead increments at least the first.
- [N-U38-036] The probability tooltip recomputes the score, restricts to the lead's own team frequencies when present, and returns the three highest and three lowest factors that sit on the right side of 0.5.
- [N-U38-037] Opening the tooltip writes the recomputed automated probability on the lead (and the visible probability when it was automated), so a read-like action modifies data.
- [N-U38-038] When no score can be computed the tooltip shows fixed sample factors instead of real ones.
- [N-U38-039] Tooltip factors for email and phone quality that contradict their label are hidden as nonsense in small data sets.
- [N-U38-042] A frequency row holds variable name, value text, won and lost counts as decimals with one digit, and an optional team that cascades on team deletion.

### STATE
- [N-U38-007] Leads currently sitting in a stage flagged as won are collected and receive probability 100 without any Bayes computation.
- [N-U38-011] A lead without a stage gets probability 0 and skips the computation.
- [N-U38-012] When the relevant team bucket has zero won or zero lost history, the lead is skipped and receives no new automated probability; the existing stored value is left unchanged.
- [N-U38-018] Live increment adjusts the frequency table at the moment a lead reaches or leaves a won or lost state: step +1 when a target state is given, -1 when leaving a state.
- [N-U38-019] The won and lost routine applies the increment in four ways (reach won, leave won, reach lost, leave lost) before the new values are written.
- [N-U38-033] A won lead increments the won count of every stage; a lost lead increments the lost count only of its current and earlier stages by sequence.

### OPTIONALITY
- [N-U38-017] The variables used are stage, team and the configured fields; tags are read separately with a left join through the tag relation table.
- [N-U38-020] The scheduled recompute rebuilds the frequency table then recomputes all pending lead scores and logs its duration.
- [N-U38-021] The scoring start date is read from a text parameter and validated as a date before being used; an invalid or missing value returns false, which makes both the rebuild and the recompute do nothing.
- [N-U38-041] Creating, changing or deleting the scoring-fields parameter refreshes the lead definition immediately so that the list of fields that trigger a recomputation is rebuilt.
- [N-U38-043] A catalog model lists which lead fields administrators may choose for scoring, each a required link to a lead field with a random colour.
- [N-U38-045] The manual update wizard stores the chosen fields and start date into parameters and runs the rebuild-and-recompute only for administrators; for other users the action silently does nothing.
- [N-U38-046] If the start-date parameter is empty or malformed the settings screen shows today minus 8 days, and the stage label is always shown as a scoring factor.
- [N-U38-048] Seven catalog entries are seeded: state, country, phone quality, email quality, source, language and tags; the parameter seed lists the same seven.

### DEPENDENCY
- [N-U38-004] Frequencies are split by sales team so one team's history does not influence another team's scores; a lead whose team has no frequency rows is scored against all teams combined.
- [N-U38-008] All frequency rows for the variables present on the leads are loaded in one search regardless of team, ordered by team then id; the lead team restriction is applied later per lead.
- [N-U38-030] Frequency writes and creations run with elevated rights so any salesperson's won or lost action can update the shared table.
- [N-U38-035] Batch value extraction searches leads without access rules and with archived records included; scoring therefore reads every company's leads.
- [N-U38-040] The stored probability fields depend on stage, team and the configured scoring fields through a dynamic dependency declaration, so changing the configuration changes which edits recompute the score.
- [N-U38-044] Deleting a team folds its frequency rows into the no-team rows: counts are rounded, summed, and floored at 0.1; unmatched rows are created for the no-team bucket.

### CONSTRAINT
- [N-U38-005] Zero-frequency problems are avoided by seeding every new frequency with 0.1 on both won and lost counts; the authors note that adding 1 would weigh too much on small data sets.
- [N-U38-009] A tag frequency row is ignored when its won plus lost count is below 50, so a rarely used tag cannot dominate the score.
- [N-U38-015] The probability is rounded to two decimals and clamped between 0.01 and 99.99, so scoring alone can never produce 0 or 100.
- [N-U38-022] The recompute targets leads with a stage, created on or after the start date, that are neither won nor lost.
- [N-U38-026] Live increment counts only leads created on or after the start date; a lead older than that never changes the table.
- [N-U38-028] A lead with several tags produces one frequency record per tag, each carrying the lead outcome.
- [N-U38-029] When a frequency is decremented it is floored at 0.1 so counts never reach zero or negative.
- [N-U38-031] Configured scoring field names that are not fields of the lead are dropped before use, which protects the direct database queries built from the parameter.
- [N-U38-034] Empty values are skipped for scoring except the email and phone quality labels, whose empty state counts as its own value.
- [N-U38-047] Frequency rows and the field catalog are read-only for salespersons and system administrators; only the update wizard is writable and it is limited to the ERP manager group.

### RISK
- [N-U38-016] On empty input the scoring routine returns a bare empty list-like result while every caller expects a pair of results; an empty-input path would therefore fail when the caller unpacks it. Whether this path is reachable in normal operation is not established.
- [N-U38-025] Each update batch runs inside a try block that logs a warning and counts failures instead of re-raising; a database error is swallowed. No rollback is issued in this block, so later batches in the same transaction may also fail until the transaction ends.

### UNKNOWN
- [N-U38-049] Statistical quality of scores on real data, behaviour under very large lead volumes and concurrent updates cannot be determined from source; the restored database holds no leads and no frequency rows. Needs a runtime run with seeded won and lost history.

## CAP-U38-02 Lead and opportunity assignment engine

### WHAT
- [N-U38-050] Purpose: distribute unassigned leads fairly across sales teams in proportion to their capacity, then across each team's members according to their remaining daily capacity and personal filters.

### WHY
- [N-U38-051] Rationale: allocating one lead at a time by weighted random draw lets teams with overlapping filters all receive leads in proportion to their size, instead of the first matching team taking everything.

### BUSINESS RULE
- [N-U38-061] Duplicates are searched once per candidate lead before the main loop so that the database is not flushed at every assignment.
- [N-U38-062] A commit is issued after data fetching and then every bundle of leads and at the end, so a failure part-way keeps what was already allocated.
- [N-U38-063] In each iteration the chosen team's remaining leads exclude those already handled; a team with none left leaves the draw.
- [N-U38-064] Only the first remaining lead of the chosen team is processed per draw; the lead and its duplicates are classified as assigned, merged or removed duplicates.
- [N-U38-068] Quotas are computed for all members of the selected teams up front, and leads per team are read grouped as id arrays so only one team's leads are in memory at a time.
- [N-U38-069] For each lead the first member in the list whose personal domain accepts it is chosen; a lead accepted by nobody is simply left unassigned.
- [N-U38-070] Eligible members (not paused, quota above zero) are ordered by remaining quota descending with random tie-breaking, so assignment starts with the least loaded member.
- [N-U38-071] Members with a preferred domain get first pick of leads that match both their domain and their preferred domain, ordered by probability descending, before any other lead is assigned.
- [N-U38-072] A second loop distributes the remaining leads, again by probability descending, to members whose assignment domain accepts them.

### STATE
- [N-U38-058] The engine has two phases: first allocate unassigned leads to teams, then distribute each team's allocated leads to its members, converting them to opportunities.
- [N-U38-060] A team's candidate pool is leads with no team, no salesperson, not won, created before now minus the delay, matching the team domain, and newer than the window when the window is positive.
- [N-U38-066] Allocating a lead to a team only writes the team; no salesperson is set in this phase.
- [N-U38-067] Member distribution takes leads of the team that have no salesperson and no assignment date.
- [N-U38-076] Conversion skips archived and won leads, writes the opportunity values, then applies salesperson and team assignment only when either is supplied.

### OPTIONALITY
- [N-U38-052] Two team flags show whether assignment is enabled and whether it runs automatically; both are computed from the rule-based parameter and the activation state of the assignment schedule.
- [N-U38-056] The scheduled assignment run covers every team that uses leads or opportunities and is not opted out, with the default seven-day creation window and no forced quota.
- [N-U38-077] Settings show manual or repeated mode from the schedule activation, and its interval and next execution; when rule-based assignment is off they fall back to manual, one day.
- [N-U38-079] Toggling the lead menu group on save sets the team lead flag on all teams that use opportunities and rewrites every team mail alias creation values.
- [N-U38-081] Changing the leads or pipeline flags on a team rewrites its mail alias name and defaults.

### DEPENDENCY
- [N-U38-054] Team statistics count leads without a salesperson and sum member 30-day counts, flagging the team when the month count exceeds the capacity.
- [N-U38-059] The result message distinguishes merged duplicates, no capacity, no domain match for the team, and no domain match for members.
- [N-U38-075] Bulk assignment with several salespersons deals leads round robin by slice (first to the first user, and so on); with a team but no users only the team is written.
- [N-U38-082] The team leader gets a leader suffix in formatted user names when a team is in the context.

### CONSTRAINT
- [N-U38-053] A team's monthly capacity is the sum of its members' capacities; a team with zero capacity is skipped by allocation.
- [N-U38-057] Only sales managers or system administrators may run the assignment engine; other users get an error.
- [N-U38-065] A lead is treated as having duplicates when the duplicate search returns more than itself; the group is merged only after the team is set on the head, and merge ignores the five-record cap.
- [N-U38-074] Lead ids are re-checked for existence before use because earlier commits may have deleted merged duplicates.
- [N-U38-078] The repeat number must be positive and below 100, and changing interval recomputes the next run from now.
- [N-U38-080] Team and member domains are validated by evaluating them literally and running a one-record search on leads; any failure raises a validation error naming the team or the user and team.

### RISK
- [N-U38-055] A member's 24-hour and 30-day lead counts group leads by assignment date, salesperson and team, including archived leads; lost leads are only excluded from the 24-hour help text, not from the query.
- [N-U38-073] The ordering key combines negative probability with a language built-in rather than the lead identifier, so leads with equal probability keep an unspecified but stable relative order.

### UNKNOWN
- [N-U38-083] The weighted random draw is not reproducible and commits partway; effects of a crash between commits, of concurrent manual and scheduled runs, and of very large lead volumes are not observable from source. The restored database holds no leads and the schedule is inactive.

## CAP-U38-03 Lead intake channels and enrichment

### WHAT
- [N-U38-084] Purpose (manifest summaries): bring leads in from outside sources and complete them: enrichment fills missing company data from the email domain, mining buys new company leads by country, industry and size, live chat and the mail add-in turn conversations and emails into leads, and SMS buttons support follow-up.

### WHY
- [N-U38-085] Rationale: capture interest at the moment it appears and keep the conversation as lead notes so a salesperson has context; costs of external data are protected by credit checks and notices rather than by hard limits.

### BUSINESS RULE
- [N-U38-086] The manual enrich button is hidden for archived leads, leads without an email, leads with an incorrect email, leads already enriched, leads that came from a reveal or mining source, and leads at 100 percent probability.
- [N-U38-098] Returned company data fills only empty lead fields: company name, reveal reference, street, city and zip; phone takes the first returned number; country and state are matched by code.
- [N-U38-105] State filters are offered only for a whitelist of ten countries because the service lacks state data elsewhere.
- [N-U38-106] The payload sends lead count, target, countries with their chosen state codes, optional size range, industries flattened from comma-separated reveal ids, and contact filters by role or seniority.
- [N-U38-107] The call also sends the reveal references of every existing lead that has one so the service can avoid returning companies already held; the search runs with the caller's rights.
- [N-U38-111] Each returned company becomes a lead with the request's type, team, tags and salesperson, the reveal reference from the business id or the clearbit id, name, address, website built from the domain, phone, first email, country and state by code.
- [N-U38-117] A chat command creates a lead from the conversation: bare command shows usage help, with a title it creates the lead and tells the operator by a transient message.
- [N-U38-118] The customer for a command-created lead is the first non-internal chat participant; if a public visitor is in the chat the lead is left without a customer.
- [N-U38-119] A command-created lead carries the channel as origin, the typed title, the conversation history as notes, the operator name as referrer, a live chat source, and no salesperson or team.
- [N-U38-122] The create-lead step reads the visitor's email and phone (public visitors) or links the signed-in partner, builds the lead with the conversation history, then assigns an unassigned lead to its team leader when rule-based assignment is off.
- [N-U38-123] The lead name is the visitor's first free-text answer cut to 100 characters, or a default title; the script's source is stamped; the step's team is dropped if its company differs from the visitor partner's company; type follows the team's lead flag; no salesperson is set.
- [N-U38-124] Create-and-forward finds candidate teams (not opted out, with capacity and a domain matching the lead) when none is set, restricts them by company, and builds the list of members who are not paused, have quota left and whose domain accepts the lead.
- [N-U38-125] Forwarding asks for an available operator among assignable members; if a new operator takes the chat the lead is assigned to that operator and the team that contains them, and a transient message links the lead.
- [N-U38-128] The live chat channel report gains a leads-created count per channel through a lateral join to leads.
- [N-U38-134] The mail add-in lead endpoint checks the partner exists (else returns a partner-not-found error), creates a lead in the partner's company with the email subject as name and the body as notes, and returns the lead id.
- [N-U38-136] Partner lead listings for the add-in return up to five leads with revenue formatted in the lead currency and probability, plus recurring revenue and plan only for users in the recurring revenue group.
- [N-U38-145] The meeting calendar for an opportunity opens in week mode on the first relevant meeting, or month mode when relevant meetings span more than one week; only unfinished meetings count if any exist.
- [N-U38-146] The activity analysis is a database view over messages on leads that carry an activity type, joined to the lead for owner, team, stage, country and status.
- [N-U38-152] A lost reason shows how many leads (archived included) use it; the lead link opens a list with creation disabled; the lead field blocks deletion of a used reason.
- [N-U38-153] A recurring revenue plan has a name, a month count that cannot be negative, a sequence and an archive flag.
- [N-U38-154] Three signed-link routes mark a lead won, lost or converted: each requires a logged-in user, validates the link token against the record, performs the action, and on any error logs and redirects to the record.
- [N-U38-155] Mass conversion with deduplication merges leads that share a customer or email (not including lost ones), keeps selection order, then converts the remainder with the chosen salespersons.
- [N-U38-156] Mass mode adds an option that reuses a matching customer or creates one per lead, and chooses a team from the first selected salesperson.

### STATE
- [N-U38-089] Leads without an email are skipped silently; leads at 100 percent or already enriched are skipped.
- [N-U38-090] An email that cannot be normalised marks the lead as enriched and posts a note that the address does not look valid, with no external call.
- [N-U38-100] A successful enrichment posts an internal note with the company card; an empty result posts a not-found note, and both mark the lead as enriched.
- [N-U38-109] Submitting assigns a number from the mining sequence if still new, performs the request, creates leads and marks done; a request in error can be retried and a done request can be reset to draft which renames it to new.
- [N-U38-120] A lead can open its originating chat window from the lead form by sending a bus message to the user.
- [N-U38-143] Creating a meeting linked to an opportunity without an activity posts a note with time, subject link and duration on the lead.

### OPTIONALITY
- [N-U38-087] The enrichment schedule picks active leads with an email, not yet enriched, without a reveal reference, below 100 percent probability and created within the last 24 hours, then enriches them in batches of 50.
- [N-U38-088] In automatic mode creating leads triggers an immediate run of the enrichment schedule rather than waiting for the daily slot.
- [N-U38-096] In scheduled runs progress is committed per batch; an unexpected batch error rolls that batch back, is logged, and processing continues; a time-budget exhaustion ends the run.
- [N-U38-097] In manual runs each batch is committed so a later failure does not lose credits already spent.
- [N-U38-101] On installation the enrichment schedule is activated only if the mode parameter is automatic; the settings screen reads and writes the schedule activation as the mode.
- [N-U38-102] The restored database has the enrichment schedule active every 24 hours, the mode parameter set to automatic, two server actions, and four views; no access rows or rules are declared by this module.
- [N-U38-113] Requests are numbered from a sequence with prefix LMR and three-digit padding, company independent.
- [N-U38-115] The restored database holds the five access rows, one mail template for the no-credit notice, one sequence, two menus, one action, nine views and seeded catalogues of 23 industries, 22 roles and 3 seniority levels; request rows do not exist.
- [N-U38-129] A sample lead-generation chatbot is seeded: ask what brings the visitor, forward to an operator, apologise if none available, ask for an email, then create a lead.
- [N-U38-133] The restored database has the two rules, one source record, one chatbot sample script with five steps, four views and no access rows for this module.
- [N-U38-138] Several routes (log single mail, leads by partner, create form redirect, open lead) are retained only for old add-in versions.
- [N-U38-141] The restored database has one access row, one rule, two actions and two views for this bridge.
- [N-U38-148] Digest emails gain two indicators, new leads and opportunities won (probability 100, by closing date); computing them raises an access error for users outside the salesperson group so those users skip the data.
- [N-U38-160] The restored database holds 32 access rows, 8 rules, 2 groups, 2 schedules, 26 menus, 30 window actions and 57 views for this module, matching the declared counts of 32 rows, 8 rules and 2 groups; three sales teams and four stages exist and no leads.

### DEPENDENCY
- [N-U38-091] One request per batch sends a map of lead id to email domain to the enrichment service and expects a map of lead id to company data or false.
- [N-U38-092] The enrichment call adds the reveal-service account token and the database unique id to the parameters and posts to the configured enrichment endpoint (default the vendor service) with a 300 second timeout.
- [N-U38-093] The service client posts a remote-call payload, raises an insufficient-credit error when the service names it, turns timeouts and transport failures into access errors that include the address, and always refuses to call out when running in test mode.
- [N-U38-103] The bridge adds an indexed reveal reference on leads that is carried by merges.
- [N-U38-112] A shared routine emails all creators of the records when credits run out and records a parameter to avoid repeating the mail; the mining feature itself never calls it, only the website reveal bridge does, so mining shows the error in the form only.
- [N-U38-114] Leads keep a link to the request that created them, preserved by merges, and a modal action opens a new request from the pipeline.
- [N-U38-121] Chatbot scripts gain two step types: create a lead, and create a lead and forward to a human operator; the latter counts as an operator forwarding step.
- [N-U38-131] The client store learns whether the user may create leads from the salesperson group.
- [N-U38-132] Live chat session data includes customers' linked opportunities only when the user can read leads.
- [N-U38-135] Add-in routes use a special authentication method: a bearer token is required and checked as a scoped access key, and the request then runs as the key owner; missing or invalid tokens are rejected.
- [N-U38-140] The SMS bridge adds SMS composer actions and buttons to lead views; it has no Python.
- [N-U38-142] Meeting defaults link the meeting to the opportunity when created from a lead and keep the generic record link and the opportunity link in sync.
- [N-U38-144] Creating a calendar event from an activity on an opportunity reuses the opportunity meeting defaults and the activity start date.
- [N-U38-149] The digest links point to the pipeline action, or to the all-leads action for users with the lead menu group.
- [N-U38-150] Campaigns show a lead count that includes archived leads and a link to a leads or opportunities list filtered by campaign.
- [N-U38-151] A partner's opportunity count includes archived records and rolls child contacts up to their parents; it is zero for non-salespersons.
- [N-U38-157] In mass mode the salesperson list replaces the single salesperson when allocating, so leads are dealt round robin across the chosen users.

### CONSTRAINT
- [N-U38-094] On insufficient credit the batch logs, sends a no-credit notification only for manual runs, and re-raises so the caller stops further batches.
- [N-U38-095] Batches take a row lock on the leads; if every remaining lead is locked the run logs an error, re-triggers itself five minutes later and stops.
- [N-U38-099] Results are applied by searching the returned ids so leads deleted while the call ran are ignored.
- [N-U38-104] Form limits clamp lead count to 1-200, contacts to 1-5, and keep minimum size at least 1 and not above maximum; these are interface rules, not database constraints.
- [N-U38-108] A credit error sets the request to error with type credits; an empty response sets the type to no result and spends no credit; any raised exception is converted into a user error quoting the cause.
- [N-U38-116] Creating or updating a lead with a live chat origin requires read access to that channel, otherwise an access error is raised.
- [N-U38-127] Sales users may read channels and channel members that belong to a lead (members also create), through two rules on the channel and the member records; a stored flag on the channel marks it as having a lead.
- [N-U38-130] A script's generated lead count is the number of leads (including archived) carrying the script's source.
- [N-U38-137] Lead information, mail logging on leads and translations are exposed to the add-in only when the user may create leads.
- [N-U38-147] Activity analysis rows are filtered like leads: own or unowned for salespersons, all for the all-leads group, and by company.
- [N-U38-158] The module also grants sales roles access to partner, tag, calendar event and event type, activity type, activity plan and plan template records.
- [N-U38-159] Managers can manage activity plans and plan templates only for the lead model, via two rules that exclude read.

### RISK
- [N-U38-110] The lead-values routine always passes an empty contact list, so contact name, email and title from a people search are never copied onto the lead by this routine; the contact data only appears in the note.
- [N-U38-126] The assignment of team and salesperson after forwarding picks the next match without a default, so an operator who is not in any candidate team would raise an error; reachability depends on how the operator list is built and is not established.
- [N-U38-139] The legacy log route posts a message on a lead id supplied by the caller without an existence check in this code, so access depends on the record rules of the key owner.

### UNKNOWN
- [N-U38-161] External service behaviour (credit pricing, answer content, outages), the sale-confirmation add-in client, live chat operator availability and SMS gateway delivery cannot be observed statically; the mail add-in client code and the website reveal bridge were not read.

## CAP-U38-04 Event definition, capacity and registration

### WHAT
- [N-U38-162] Purpose: plan events, sell or collect registrations, confirm attendees automatically and record attendance, with a back-office desk that scans attendee badges.

### WHY
- [N-U38-163] Rationale: automatic acknowledgement and reminder messages reduce manual work for organizers and give attendees their ticket, while seat limits and ticket sale windows protect capacity.

### BUSINESS RULE
- [N-U38-170] Changing the template re-syncs the question list but keeps any question that already has attendee answers; with no template and no answers the default questions are loaded.
- [N-U38-182] Availability for a slot and ticket pair is the event limit (per slot for multi-slot events) combined with the ticket limit, taking the smaller; unlimited is represented as none.
- [N-U38-189] Registration start and end dates come from the slot when present, else from the event; searches on them are built as a union of the two cases.
- [N-U38-196] The default email subject is the event name with the attendee name, or the registration number when unnamed.
- [N-U38-206] A template without seat limit has its maximum reset to zero.
- [N-U38-214] A public ticket download requires the event, registration list and an HMAC hash compared in constant time; any missing or mismatching input returns not-found; output is a PDF of badges or tickets or a responsive HTML page.

### STATE
- [N-U38-171] For multi-slot events registrations are open if there is at least one slot and either no tickets or a launched, non-expired ticket with availability on some slot.
- [N-U38-172] The event's sale start is the earliest start of its non-expired tickets, and is empty unless every such ticket has a start date.
- [N-U38-173] An event is sold out when its seat limit is reached, or when every ticket is sold out (every slot and ticket combination for multi-slot events).
- [N-U38-174] Ongoing means start not later than now and end after now; finished means end is not after the current time in the event timezone; the registration desk uses finished to refuse badge scans.
- [N-U38-177] Changing the stage resets the kanban state to in-progress unless the event is cancelled.
- [N-U38-188] The attended date is stamped the first time the registration reaches done; the code only sets or clears it while it is still empty, so it is not cleared if the registration later leaves done.
- [N-U38-192] A badge scan reports cancelled, unconfirmed, event ended, needs manual confirmation (ticket for another event), confirmed (and marks attended), or already registered; the summary includes slot, ticket, answers, badge format and whether attendance was recorded today.
- [N-U38-207] A stage can be flagged as an end stage, into which finished events are moved automatically.

### OPTIONALITY
- [N-U38-165] A new event defaults its start to the next half hour and its end to one day later.
- [N-U38-166] The kiosk address of an event points to the registration desk page of the application; the desk uses the attendee barcode flow.
- [N-U38-167] An event may be created from a template that auto-fills tickets, communications, questions, tags, note, timezone, seat limit and ticket instructions.
- [N-U38-168] The event display timezone comes from its template, else the user's timezone, else UTC; it drives sale windows, slot hours, closing checks and the calendar file.
- [N-U38-169] Barcode use is controlled by a system parameter compared to the text value True.
- [N-U38-175] Re-syncing communications from a template keeps lines already sent or with attendee logs, removes others and adds template lines not already present as exact copies.
- [N-U38-176] Re-syncing tickets from a template removes only tickets without registrations and copies sequence, name, description and seat limit from the template.
- [N-U38-180] A duplicated event is named with a copy suffix.
- [N-U38-204] Three default questions are seeded: name and email (mandatory) and phone.
- [N-U38-205] New templates and new events default to three communications: an immediate message after each registration (subscription template), a reminder one hour before and one three days before.
- [N-U38-211] Disabling the map option clears the stored key and secret, and saving a secret that is not valid base64 raises an error.
- [N-U38-213] A public route returns an event calendar file, optionally for one slot; an unknown slot or missing file returns not-found.
- [N-U38-215] A signed-in-only route supplies the barcode interface with event name, country, city and company, or generic values when no event is given.
- [N-U38-217] The restored database has 37 access rows, 3 rules, 3 groups, 1 schedule, 3 mail templates, 12 menus, 15 window actions and 65 views owned by this module; no events or registrations exist.

### DEPENDENCY
- [N-U38-181] Registration desk users may post messages on events because the post operation is mapped to a read-level permission.
- [N-U38-185] Descriptions for external calendars are shortened to 1900 characters and prefixed with a link to the event share address.
- [N-U38-187] Attendee name, email, phone and company are pre-filled from the booking partner's contact address only when still empty.
- [N-U38-193] Scheduler refresh is skipped during module installation because rendering during server start could hang.
- [N-U38-194] A send-badge action opens the mail composer with the badge template for the selected registration.
- [N-U38-195] When the default recipient equals the registration email, the registration name is attached to the recipient; the registration email takes priority over a shared booking partner.
- [N-U38-208] A partner's event count includes events booked by its child contacts and is visible only to the registration desk group.
- [N-U38-210] The map signature is an HMAC-SHA1 of the request path with the base64-decoded secret; a bad secret yields no map.
- [N-U38-212] Deleting a mail template deletes every event and template communication that points to it; the template selector can be filtered to attendee templates through a context key.

### CONSTRAINT
- [N-U38-164] At most 30 tickets can be ordered on one line at a time (constant used by the ticket limit check).
- [N-U38-178] The online URL is cleared when a venue exists, must have a scheme and host, and gets a secure scheme added on change when missing.
- [N-U38-179] Lowering the seat limit below current registrations only warns that the event will be sold out while extra registrations remain.
- [N-U38-183] The seat verification raises one validation error listing each slot, ticket or event that is missing seats.
- [N-U38-184] A relative date label (today, tomorrow, in N days, next week, next month, or a medium date) is computed in the event timezone.
- [N-U38-190] A ticket must belong to the registration's event; a slot must too and is mandatory on multi-slot events.
- [N-U38-191] Phone numbers are formatted on entry and at creation using the partner country, else the event country, else the company country; an unparseable number is kept as typed.
- [N-U38-197] Slot hours must be between 0:00 and 23:59 and the end must be later than the start.
- [N-U38-198] A slot must lie within the event dates; its datetimes are computed from the slot date and hours in the event timezone converted to UTC.
- [N-U38-199] Slot seats available are the event's maximum minus the slot's registered and attended attendees, read from a direct count.
- [N-U38-200] A slot with registrations cannot be deleted.
- [N-U38-201] A default question must be reusable and cannot be deleted.
- [N-U38-202] A question's type cannot change once any attendee answered it, and an answered question or a selected answer cannot be deleted; archiving is the alternative.
- [N-U38-203] Every attendee answer needs either a chosen suggested answer or a non-empty text; its display name is the chosen answer for selection questions and the text otherwise.
- [N-U38-216] Source declares 37 access rows across Registration Desk (read, plus write and create on registrations and answers), Event User (create and change events, tickets, slots, tags, schedulers) and Event Administrator (full); the restored database holds 37.

### RISK
- [N-U38-186] Calendar file generation returns an empty result when the optional iCalendar library is absent; with the library it writes start, end, summary, description and venue in the event timezone. Whether the library exists on the server is not observed.
- [N-U38-209] A signed static map address is built from the partner address when both a key and a secret parameter exist, and its validity is checked by a live web request with a 2 second timeout on each computation; any failure or a warning header marks it invalid. Network behaviour is not observed.

### UNKNOWN
- [N-U38-218] Behaviour under concurrent registrations at the seat limit (the limit is checked after saving, with no explicit lock), the ticket and badge print templates, the website registration flow and the registration desk client code were not read or run.

## CAP-U38-05 Event automated communications

### WHAT
- [N-U38-219] Purpose: automatically send messages to attendees at defined moments relative to registration, event start or event end, with a periodic job picking up what is due.

### WHY
- [N-U38-220] Rationale: registering for an event is treated as consent to event messages such as the ticket, so the general opt-out list does not apply to them.

### BUSINESS RULE
- [N-U38-222] The scheduled time is anchored on the event creation date for after-registration rules, the event start for start-based rules and the event end for end-based rules, with a negative sign for the before options.
- [N-U38-230] For multi-slot events the engine creates a per-slot schedule row for each slot lacking one and runs the event-based logic per slot.

### STATE
- [N-U38-224] A communication shows error if an error time is set, cancelled if the event is cancelled and not yet sent, running for after-registration rules, sent when done, otherwise scheduled.
- [N-U38-226] A successful execution clears the stored error time.
- [N-U38-228] Event-based sending walks registrations in id order after the last contacted one and marks done when none remain; progress is stored on the communication or its slot row.
- [N-U38-231] After-registration rules first create one log row per eligible attendee not yet logged, up to twice the limit, then send for logged rows that are due and not yet sent.
- [N-U38-233] The sent counter for after-registration rules counts log rows marked sent; for event-based rules it counts non-draft, non-cancelled attendees up to the last contacted one and marks done when that reaches the seats taken.

### OPTIONALITY
- [N-U38-221] Offsets are hours, days, weeks (seven days), months, or immediately (zero).
- [N-U38-223] Computing a scheduled time asks the scheduling engine to run the mail schedule at that time, so schedules do not wait for the 24 hour slot.
- [N-U38-236] Only interval, unit, trigger and template are copied between template lines and event lines.
- [N-U38-243] Template pickers on communication lines can be restricted to templates for attendees by a context setting; the same applies to SMS templates.
- [N-U38-244] Communications gain an SMS channel; the channel is derived from the chosen template kind.
- [N-U38-245] After-registration SMS rows are sent per scheduler and marked sent before the mail path handles the remaining rows.
- [N-U38-246] Template communication lines support the same SMS channel.
- [N-U38-249] The restored database has the mail schedule active at 24 hour intervals and three mail templates owned by the event module; no communications or logs exist.

### DEPENDENCY
- [N-U38-235] The sender is the organizer if it has an email, else the company, else the current user, else the system user; the mail goes through the mass composer, not forced out immediately, and the template sender is used when set.
- [N-U38-240] The due time of an after-registration message is the attendee creation time plus the offset; log rows are due when unsent, dated, and not in the future.
- [N-U38-241] Event messages ignore the mass-mailing exclusion list because registering implies subscribing to event messages.
- [N-U38-242] The per-attendee log entry has a deprecated direct run action that re-filters to open or attended attendees.
- [N-U38-247] Deleting an SMS template deletes every communication line pointing to it.

### CONSTRAINT
- [N-U38-225] A start-based communication is not sent once the event has ended, even if it was scheduled before the event; the guard applies to slots too.
- [N-U38-227] Per run the engine handles at most the configured render limit (default 1000) recipients, in batches of the configured mail batch size (default 50); when more remain it re-triggers itself.
- [N-U38-229] Each batch commits and clears working memory so a crash does not resend already contacted attendees.
- [N-U38-234] A communication whose template is missing or of the wrong kind is skipped with a warning log.
- [N-U38-237] A failure posts a note to the organizer, the responsible and the template author at most once an hour, quoting the template link and the render or run error.
- [N-U38-238] The scheduled run selects communications of active, non-cancelled events that are due and not done, and after-registration ones until the event ends.
- [N-U38-239] Each communication runs in its own protected block; an error clears working memory, warns on the event and the loop continues; a commit follows each success in automatic mode.
- [N-U38-248] Event administrators may create, change and delete SMS templates only for events and registrations, through an access row and a rule that excludes read.

### RISK
- [N-U38-232] The log-row creation loop splits attendees into chunks of 500 but builds each create call from the whole attendee set instead of the chunk, so with more than 500 new attendees in one run duplicate log rows would be created. Recipients are de-duplicated when sending, so mail duplication is not shown; reachability is not observed.

### UNKNOWN
- [N-U38-250] Actual mail and SMS delivery, template rendering failures per attendee and the interaction with the mail queue and the SMS provider are not observable statically; the mass composer is covered by the marketing unit.

## CAP-U38-06 Event booths and booth sales

### WHAT
- [N-U38-251] Purpose (manifests): let organizers define bookable booths per event and category, and let customers rent them through sales orders with the booth marked unavailable once confirmed.

### WHY
- [N-U38-252] Rationale: several customers may request the same booth before it is confirmed, so requests are kept separately and the first confirmed order wins and cancels the others.

### BUSINESS RULE
- [N-U38-256] Confirming a booth writes unavailable plus any renter details given; no code path returns a booth to available; the state field itself is not read-only in the model, so a user with edit rights could change it by hand.
- [N-U38-269] Order confirmation raises an error if any pending booth is no longer available, otherwise confirms the registrations with elevated rights; marking booths paid happens only when requested by the payment hook and the line already has confirmed booths.
- [N-U38-270] The line price is the sum of the booths' category prices (reduced price when no discount is shown), converted to the order line currency from the event company currency; the line description lists event and booth names.

### STATE
- [N-U38-253] A booth is either available or unavailable (default available, tracked); renter name, email and phone are pre-filled from the renter partner when empty.
- [N-U38-254] A booth created already unavailable posts a booked message on its event; creation does not subscribe the creator.
- [N-U38-255] Writing state to unavailable on booths that were available posts the booked message on the event; booths already unavailable do not repost.

### OPTIONALITY
- [N-U38-257] Availability is a searchable derived flag from the state.
- [N-U38-258] Changing the event template removes only available booths and creates booths from template lines copying name, category (and with sales, product and price); booked booths are kept.
- [N-U38-260] Booth categories offered for an event are derived from its booths, and the available-category list from available booths only.
- [N-U38-261] A booth template line gets the single existing category by default; a category is required and cannot be deleted while used.
- [N-U38-262] Three booth categories are seeded: standard, premium and VIP; the restored database holds 9 access rows, 2 menus, 4 window actions and 22 views for this module.
- [N-U38-264] Each booth category with sales requires a product with the booth service tracking (default the seeded booth product); a constraint rejects other products.
- [N-U38-265] A category price defaults to the product list price plus extra and may be overridden because products can be shared between categories; tax-included and reduced prices are computed with the product taxes and contextual pricelist discount.
- [N-U38-266] Installing the sales bridge on existing categories assigns the generic booth product, creating a 100-priced service product if it is missing.
- [N-U38-276] Template booth lines carry product and price from the category and copy them to event booths.
- [N-U38-277] The restored database holds 4 access rows, 1 window action and 13 views for the booth sales bridge, matching the four declared rows.

### DEPENDENCY
- [N-U38-259] Event booth counts (total and available) are computed with grouped reads using elevated rights, and by in-memory counts when the record is unsaved.
- [N-U38-271] Confirming an order with booth lines lacking pending booths raises a validation error listing the lines; booth products are hidden from the product catalogue.
- [N-U38-273] Confirming copies order line, partner and contact details from the registration onto the booth.
- [N-U38-275] A configurator wizard for salespersons requires an event, a category and at least one booth, resetting category and booths when the event or category changes.

### CONSTRAINT
- [N-U38-263] Nine access rows: category and booth readable by desk, writable by Event User for booths, full for administrators; two rows with no group and no rights exist for public booth and category models.
- [N-U38-267] A product linked to a booth category cannot change away from the booth tracking at template or variant level; booth tracking forces invoicing on ordered quantity in the product form.
- [N-U38-268] All booths of one order line must belong to a single event; changing event or product on the line clears the pending booths or event accordingly.
- [N-U38-274] A booth linked to an order cannot be deleted.

### RISK
- [N-U38-272] After a booth is confirmed for one order, every other registration for the same booths is deleted and its whole order is cancelled with elevated rights and a message to the salesperson, including any non-booth lines on that order.

### UNKNOWN
- [N-U38-278] Return of a booth to available status, treatment of credit notes and partial payments for booths, and the website booth selection flow are not implemented or not read in this unit.

## CAP-U38-07 Event ticket sales

### WHAT
- [N-U38-279] Purpose: create attendee registrations automatically from confirmed sales orders so that tickets can be priced, invoiced and tracked.

### WHY
- [N-U38-280] Rationale: the order drives the registration state so that unpaid or cancelled orders do not hold seats as confirmed attendees.

### BUSINESS RULE
- [N-U38-304] The attendee editor lists existing non-cancelled registrations per order line and adds blank rows for the remaining quantity, defaulting names and contact details to the order customer.
- [N-U38-305] Saving the editor updates existing registrations or creates new ones, then forces a recomputation of status so seat checks and emails happen immediately.

### STATE
- [N-U38-288] Without an order link the sale status defaults to free and the state to registered; this base logic lives here so that other ordering channels can reuse it.
- [N-U38-290] Registration state and sale status are recomputed when the order state, currency or total changes.
- [N-U38-291] A zero-total order makes its registrations free and registered if they were unset or unconfirmed.
- [N-U38-298] The order attendee count excludes cancelled registrations.
- [N-U38-299] When one order is confirmed in the back office, registrations for priced lines start unconfirmed so attendee details can be filled in, while free ones start registered for seat checks.

### OPTIONALITY
- [N-U38-281] A ticket line takes its price and description from its product when the product has a price or sale description, and the price stays editable.
- [N-U38-283] Installing on existing ticket lines assigns the generic registration product, creating a zero-priced service product if missing.
- [N-U38-284] Product and price are added to the fields copied from template tickets to event tickets.
- [N-U38-289] The product module seeds an events product category and a generic registration product with its template; the restored database holds 0 access rows and 9 views for this module.
- [N-U38-297] Confirming a single order with event lines returns the attendee editing wizard instead of the normal result.
- [N-U38-307] The configurator flags products that have tickets on events not yet ended, and pre-selects the only matching ticket and the only slot when unique.
- [N-U38-310] The restored database holds 4 access rows, 1 rule, 1 menu, 3 window actions and 13 views for the sales bridge; no registrations or orders exist.

### DEPENDENCY
- [N-U38-292] When a computed state change moves registrations from unconfirmed or cancelled to registered, the attendee mail schedulers are refreshed.
- [N-U38-293] Creating or rewriting a registration with an order line copies partner, event, slot, ticket, order and line from that line, avoiding registration of a public user as the customer; a creation note links back to the order.
- [N-U38-294] Changing a registration's slot or ticket after sale schedules a warning activity on the order for the event responsible, else the salesperson, else the current user or administrator.
- [N-U38-295] All registrations of the same event on one order can be listed together, used for ticket downloads.
- [N-U38-296] Changing the order customer rewrites the booking partner on all its registrations with elevated rights.
- [N-U38-301] An order line with a ticket describes itself from the ticket, plus the slot name and variants, and the template name is not reapplied; the product sale description takes priority in the ticket text.
- [N-U38-302] The line price comes from the ticket price (reduced price when no discount is shown), converted from the event company currency; the unit of measure is read-only on event lines.
- [N-U38-303] Event sales total uses current-day exchange rates, not the rate on each order, to avoid one conversion per order.
- [N-U38-308] The sales report is a database view per registration, dividing line totals by the order currency rate and quantity to give per-ticket revenue in company currency; zero quantity gives zero.
- [N-U38-311] The existing lead is found by comparing the order of the lead's source registrations.

### CONSTRAINT
- [N-U38-282] The reduced ticket price applies the pricelist-driven discount from the product; the source comment calls this feature broken by design and limited to display use.
- [N-U38-285] A ticket whose product is archived is not available for sale.
- [N-U38-286] Tax-included ticket prices use only product taxes belonging to the event company and the company currency.
- [N-U38-287] A product used by a ticket must have event registration tracking; event tracking is excluded from the generic service-tracking list.
- [N-U38-300] The line event is cleared when the product is not an event product or not among the event's ticket products; slot and ticket are cleared when they belong to another event.
- [N-U38-309] The sales report is readable by Event Administrators only and filtered by company; salespersons also receive the Registration Desk group by implication.

### RISK
- [N-U38-306] The configurator's error messages contain named placeholders that are never filled in, so a rejected choice would show the placeholder text rather than the ticket or event name.

### UNKNOWN
- [N-U38-312] Interaction with online ticketing and point-of-sale ticketing modules, refunds after attendance and seat checks under concurrent orders were not read or run.

## CAP-U38-08 Lead generation from event registrations

### WHAT
- [N-U38-313] Purpose: turn registrations into sales leads automatically according to configurable rules.

### WHY
- [N-U38-314] Rationale: lead quality is higher once attendees confirm or actually attend, so rules can wait for those moments before creating a lead.

### BUSINESS RULE
- [N-U38-316] A rule can be limited by event templates, one event, a company, and a free domain over registrations; with both event and template set, either matching is enough.
- [N-U38-329] A generated lead carries the rule type, salesperson, team and tags, the event as referrer and source, the registrations, the first campaign, source and medium found, contact data and a numbered participant list.
- [N-U38-330] For a single attendee the registration partner is kept as the lead customer only if its email and phone match the registration; otherwise the lead uses the attendee's own name, email and phone and no partner.
- [N-U38-333] Without a sales bridge, registrations are grouped by event and exact creation time, which approximates a batch booking; updating an existing group lead is not supported there.
- [N-U38-334] The lead description lists each attendee with email and phone, as a numbered or bulleted list under a prefix.

### STATE
- [N-U38-320] For order-based rules, an existing group lead gets an appended list of the new registrations and a link to them instead of a new lead; new groups produce one lead per event.
- [N-U38-323] The background job processes each pending request in batches of 200 registrations after a stored cursor, commits after each batch, re-triggers itself while any request is unfinished, and deletes finished requests.
- [N-U38-324] Only one open generation request can exist per event and the table keeps no access log.
- [N-U38-326] When a registration with leads changes contact or description fields, the old values are captured, and after saving the linked attendee leads are updated with elevated rights.
- [N-U38-327] A partner change on a registration refreshes name, email and phone before comparing, because these are computed.
- [N-U38-328] Order-based leads are updated only on a partner change: contact data is refreshed and the description is rebuilt or appended.

### OPTIONALITY
- [N-U38-315] A rule triggers when attendees are created, registered, or attended; it creates one lead per attendee or one per order or batch.
- [N-U38-317] Choosing a team on a rule pre-fills the salesperson with the team leader.
- [N-U38-321] Running a rule manually applies it to the rule's event or to every unfinished event.
- [N-U38-322] Regeneration for up to 200 non-draft, non-cancelled registrations runs at once and reports the number of leads created; larger sets create a request record and trigger the background job.
- [N-U38-325] A context flag and the data import path skip rule application so bulk loads do not create leads.
- [N-U38-337] The restored database has the generation schedule active daily, 5 access rows, 1 rule, 1 menu, 5 window actions and 9 views for this module; no rules or requests exist.

### DEPENDENCY
- [N-U38-331] The public partner is never used as lead customer; the first non-public partner among grouped registrations is used.
- [N-U38-332] The lead name is the event name plus the contact name, falling back to the attendee name or email.
- [N-U38-335] Merging leads also merges their source registrations (with elevated rights) and keeps the rule and event references.
- [N-U38-336] A button on a suggested answer opens a new rule pre-filled with a domain on that answer.

### CONSTRAINT
- [N-U38-318] All rules whose conditions match are applied, so several leads can arise from one registration by design.

### RISK
- [N-U38-319] The registration filter is parsed at run time with no validation on save (unlike the sales team domains), so a malformed filter would raise an error when the rule runs, inside registration creation.

### UNKNOWN
- [N-U38-338] Lead creation under concurrent registrations and rule changes, and the effect on salesperson workload of many generated leads, are not observable statically; no rules exist in the restored database.

## CAP-U38-09 Fleet vehicles, contracts and costs

### WHAT
- [N-U38-339] Purpose: keep a register of vehicles with driver history, contracts, services and odometer readings, warn before contracts expire and analyse costs.

### WHY
- [N-U38-340] Rationale: contracts such as leasing or insurance must be renewed on time, so a daily job creates one reminder per expiring contract and a reporting view totals costs over time.

### BUSINESS RULE
- [N-U38-344] The vehicle name is brand, model and license plate separated by slashes, with a placeholder when there is no plate.
- [N-U38-345] The CO2 unit follows the range unit: per kilometre or per mile.
- [N-U38-359] The contract name is the cost type name plus the vehicle name.
- [N-U38-365] The recurring cost and frequency are stored on the contract and used by the cost analysis view; no code in this module creates cost lines from them, despite the schedule's name.
- [N-U38-374] A model defines vehicle type car or bike, brand, category, defaults for technical data, fuel (default electric), drive type, power and range units and a property definition that vehicles inherit.
- [N-U38-375] Models are found by name or brand name, and the display name is brand slash model.
- [N-U38-376] A search on the vehicle count loads every model to filter in memory.
- [N-U38-377] The brand model count compares the active flag with the text value true; the count of active models is stored and refreshed when model active flags change.
- [N-U38-382] The cost analysis is a database view that builds a monthly series per vehicle from the first service or acquisition month to next month and sums service amounts per month (excluding cancelled and archived) and contract amounts per month.
- [N-U38-383] Contract cost per month adds one-off amounts dated that month, daily recurring cost times days covered, monthly recurring cost for each month inside the contract, and yearly recurring cost in the month of the contract date.
- [N-U38-385] Service and contract costs are combined with a row number per vehicle; the view uses only active vehicles and no company rule is applied inside it, the company rule is on the report model.
- [N-U38-386] The odometer analysis interpolates monthly readings per vehicle: keeps the highest reading per date, adds a zero reading at the acquisition date when earlier, fills months without readings by linear interpolation and apportions mileage deltas across months by days.

### STATE
- [N-U38-348] The reminder flags use the latest expiration among non-closed contracts: overdue if past, due soon if within the delay, and the contract state shown is that of the latest one.
- [N-U38-349] The overdue search lists vehicles with an open or expired contract past its expiry that have no open or incoming contract still running.
- [N-U38-350] The due-soon search finds vehicles with an open or expired contract expiring after today and before the delay limit.
- [N-U38-352] Creating a vehicle with a future driver flags that driver's existing vehicles of the same type as planned to change; writing a future driver does the same unless the vehicle is in the waiting-list or new-request state.
- [N-U38-353] Changing the driver creates a history line and schedules a to-do for the fleet manager (or current user) to set the end date for the previous driver; clearing the driver creates no history.
- [N-U38-358] A new contract starts today, expires one year later, defaults to running, with a monthly recurring cost frequency and the vehicle's manager as responsible when opened from a vehicle.
- [N-U38-360] Days left is the days to expiry for running or expired contracts (zero if overdue) and minus one otherwise; a today flag marks expiry today.
- [N-U38-361] Writing the start or expiration date re-derives the state: new if starting in the future, running if today is within the dates or there is no expiry, expired if past; closed contracts are left alone.
- [N-U38-368] A service moves through new, running, done and cancelled without code-enforced transitions; the cost report excludes cancelled services.

### OPTIONALITY
- [N-U38-341] A vehicle copies transmission, year, assistance, colour, seats, doors, hitch, CO2 and standard, fuel, power, horsepower, tax horsepower, category, range and units from its model, only when the model value is set and the vehicle field is being computed.
- [N-U38-342] Each of those copies depends on the model only, so they refresh when the model changes but remain editable on the vehicle afterwards.
- [N-U38-351] The waiting-list state is referenced by code but seeded only in demo data; without it the guards treat every state as not waiting. The restored database has four states and none is waiting list.
- [N-U38-363] The daily schedule creates one renewal activity per running contract that expires within the delay, has a responsible user and has no renewal activity yet.
- [N-U38-364] It then marks as expired every contract not expired or closed whose expiry is past, marks as new those not new or closed whose start is in the future, and marks as running new contracts whose start has come.
- [N-U38-367] A service requires a service type; the default points to a demo-only type, and the seeded service types are contract types only, so in the restored configuration the field starts empty; the model declares no category restriction (views, not read, may add one).
- [N-U38-378] The restored database holds 67 brands, no models and no vehicles, four vehicle states, two contract service types and no service-category types.
- [N-U38-381] The wizard can save the typed message as a reusable template for vehicles and moves the user's own attachments to it.
- [N-U38-389] The restored database holds 24 access rows, 9 rules, 2 groups, 1 daily schedule (active), 21 menus, 14 window actions and 51 views for this module, matching the source counts for rows, rules and groups.

### DEPENDENCY
- [N-U38-347] Counters show odometer logs, history lines, services and contracts; contract counts exclude closed contracts and services and contracts follow the vehicle's active flag.
- [N-U38-355] A vehicle service-activity flag shows overdue or today based on activities on its service logs, ignoring planned ones.
- [N-U38-356] Changes of driver or future driver post with a dedicated chatter subtype.
- [N-U38-362] Changing the expiration date or the responsible reschedules the open renewal activities with the new deadline and user.
- [N-U38-371] The service driver defaults to the vehicle's current driver, and brand, model and manager are stored from the vehicle.
- [N-U38-373] The driver history stores start and end dates; only the start is written by code.
- [N-U38-390] The renewal activity type is registered as protected master data of the activity type model: its target model cannot be changed and it cannot be deleted.

### CONSTRAINT
- [N-U38-346] Entering a new odometer on a vehicle creates a log dated today with the current driver, and a zero value creates nothing; writing a lower value is rejected.
- [N-U38-357] The fleet manager field offers only internal users of the vehicle's company who belong to the fleet officer group.
- [N-U38-366] A contract requires a vehicle and checks company consistency; it carries cost type, amount, date, vendor, reference, terms and included services.
- [N-U38-369] Entering an odometer on a service creates an odometer log on the service date and links it; clearing it is refused; zero is dropped at creation.
- [N-U38-372] An odometer log has date, value (grouped by maximum), vehicle and driver defaulting to the vehicle's driver; its name is vehicle and date.
- [N-U38-379] Sending mail to drivers is refused with a notification listing drivers without an email, and no message is sent at all if any is missing.
- [N-U38-388] Source declares 24 access rows; officers have full rights on vehicles, contracts, odometer logs and driver history and read-only on models, brands, categories, states, tags, service types and service logs; administrators have full rights on master data and logs, read on the cost report, create and edit but not delete on the mail wizard, and full rights on the odometer analysis.

### RISK
- [N-U38-343] A calculation routine exists for the vehicle range but the range field is not set up to use it, so the range is not copied from the model; the model has its own range and unit.
- [N-U38-354] Archiving a vehicle archives its contracts and services; there is no matching restore on unarchive in this module.
- [N-U38-370] The link to the created odometer log is assigned to the whole set of records rather than the current one, so saving several services at once would link all of them to the last log.
- [N-U38-380] For each vehicle the wizard renders subject and body from the template or the typed text and posts a comment on the vehicle addressed to its driver; vehicles without a driver would receive a post with no recipient.
- [N-U38-384] Weekly and no-recurrence frequencies have no join in the view, so weekly recurring costs do not appear in the analysis.
- [N-U38-387] The odometer view query is executed once as a plain statement before the view is created, doing the full computation at install or upgrade.

### UNKNOWN
- [N-U38-391] Cost lines for recurring contracts are not generated by this module (only the analysis view derives them); accounting links, driver payroll links and country-specific vehicle rules live in other modules not read here; the restored database has no vehicles or models.

## CAP-U38-10 Gamification: goals, challenges, badges and ranks

### WHAT
- [N-U38-392] Purpose: motivate users with numerical goals assigned through challenges, with ranking boards and recurring periods, and with badges for non-numerical recognition.

### WHY
- [N-U38-393] Rationale: goals and badges are generic so any module can define its own measurable objectives; onboarding goals help new users configure their profile.

### BUSINESS RULE
- [N-U38-400] A goal ties a user to a definition for a period with a target, a current value, a state, a reminder delay and a last update date.
- [N-U38-402] Completeness is capped at 100 percent for higher-is-better goals; for lower-is-better goals it is either 0 or 100.
- [N-U38-406] For Python goals each goal runs the stored code in the restricted evaluator with the goal, the environment and date helpers, and takes the numeric result; a non-number is logged as an error.
- [N-U38-409] Results are written goal by goal and, when the scheduled run sets the commit flag, committed after each definition.
- [N-U38-410] Every write stamps the last update date; changing the definition or user of a started goal is refused.
- [N-U38-440] A challenge line pairs a goal definition with a required target value and a sequence.
- [N-U38-444] Owner statistics (total, unique users, unique owner list) are computed by a grouped query restricted by the user record rules; monthly statistics count grants since the first of the month.
- [N-U38-448] A user's karma is stored as the latest new value of the user's tracking rows; writing karma directly appends a tracking row for the difference.
- [N-U38-449] Adding karma creates a tracking row with old value, new value, origin and reason (default added manually), through elevated rights.
- [N-U38-450] A tracking row fills a missing old value from the user's current karma, and converts a given gain into a new value.
- [N-U38-451] A monthly schedule consolidates tracking rows from two months ago: for each user it inserts one consolidated row from the oldest old value to the newest new value and deletes the detailed rows, losing their origin and reason.
- [N-U38-453] Rank is recomputed whenever karma changes: each user gets the highest rank whose threshold they meet and the next rank above; users with zero karma only get a next rank; a bulk path is used for large batches; a rank change sends a rank-reached email unless installing.

### STATE
- [N-U38-401] Goal states are draft, in progress, reached, failed and cancelled; goals generated by challenges start in progress.
- [N-U38-403] A new value reaches the goal when it meets the target in the configured direction; reaching does not close the goal because it can still change.
- [N-U38-404] A goal not reached after its end date becomes failed and closed; an unchanged value causes no write at all.
- [N-U38-405] For manual goals the update only sends a reminder to the user when the goal has not been updated for the configured number of days, and flags it for update.
- [N-U38-412] Manual start recomputes the goal; manual reach and fail set the state directly, and cancel returns the goal to in progress, to be reevaluated at the next update.
- [N-U38-415] Recurring challenges use the current day, the current week from Monday to eight days later, the current month, or the current year as goal periods; a non-recurring challenge uses its own start and end dates.
- [N-U38-416] Weekly periods end seven days after the Monday start, so a weekly goal spans eight calendar days inclusive.
- [N-U38-417] A challenge is draft, in progress or done; starting recomputes participants and generates goals, completing triggers rewards, and returning to draft is refused while goals are in progress.
- [N-U38-423] The daily check starts draft challenges whose start date has come, closes in-progress challenges whose end date is past, then updates every running challenge.
- [N-U38-425] After recomputation the engine refreshes participants, generates missing goals, sends due reports and checks rewards.
- [N-U38-428] The manual check deletes in-progress goals of the challenge and regenerates them from scratch.
- [N-U38-429] For each line the engine finds users with goals for the period, deletes goals of users who are no longer participants, and creates a goal for every participant lacking one with the line target, period dates and an initial value set beyond the target so it is computed at least once.

### OPTIONALITY
- [N-U38-394] A goal definition measures progress in one of four ways: entered by hand, count of records, sum of a numeric field, or a stored Python snippet.
- [N-U38-396] The condition says whether higher or lower values are better; the default is higher.
- [N-U38-407] In batch mode goals are grouped by period and one grouped read per period counts or sums records by the distinguishing field, matching each goal to its user value.
- [N-U38-408] Without batch mode the definition's filter is evaluated per user with the date period added, and a count or a sum is taken; a sum on a non-numeric field falls back to a count.
- [N-U38-418] Participants come from a list and an optional user filter evaluated at creation, update, start and each scheduled run; users no longer matching are removed.
- [N-U38-420] A challenge can award one badge to every user who reaches all goals, and separate badges to the first, second and third ranked users; it can also reward the best users even if they failed, and by default rewards in real time.
- [N-U38-421] Visibility is personal (individual goals) or a ranking board; reports can be never, on change, daily, weekly, monthly or yearly with an optional copy to a discussion channel.
- [N-U38-422] The next report date is the last report date plus the frequency offset, and empty for never or on change.
- [N-U38-426] A report is sent when the next report date has arrived; otherwise a final report is sent for goals that closed since the last report.
- [N-U38-454] Creating or editing rank thresholds recomputes the ranks of the affected users; a threshold must be above zero.
- [N-U38-458] The restored database has the daily goal check and the monthly karma consolidation active, 28 access rows, 3 rules, 4 mail templates, 7 menus, 10 window actions and 26 views for this module, matching source counts for rows and rules; five karma ranks, 4 badges, 4 goal definitions and 2 challenges (in progress) are seeded by this module.
- [N-U38-459] Four onboarding goals (timezone, company data, company logo, invite a user) and two onboarding challenges are seeded, one for all internal users and one for ERP managers, non-recurring and personal.
- [N-U38-460] The sales bridge seeds ten goal definitions on invoice reports, leads, opportunities and orders, all in batch mode keyed on the salesperson, plus two monthly ranking challenges (sales targets and lead acquisition) with weekly reports and four lines.
- [N-U38-462] The restored database holds 10 goal definitions, 2 challenges (both draft), and 4 lines owned by the sales bridge, and no goals; other challenges in progress come from the forum and slides modules.

### DEPENDENCY
- [N-U38-411] A change of the current value triggers an immediate progress report for that user when the challenge reports on change, except during creation.
- [N-U38-413] A goal opens the linked action (at the user's own record when an identifier expression is set) or, for manual goals, the update wizard.
- [N-U38-431] Progress is serialized per line: for personal challenges only users whose goal is reached are listed and the report returns nothing if any line is not yet reached; for ranking challenges goals are sorted by completeness then value, and the top positions are padded with empty entries up to three.
- [N-U38-432] A personal report is skipped as soon as one line of the user's challenge is not reached.
- [N-U38-433] Ranking reports are posted on the challenge to all participants and optionally to a channel; personal reports are sent to each user privately, and the last report date is then updated.
- [N-U38-434] A suggested challenge can be accepted by a user, who joins with elevated rights and receives goals, or discarded.
- [N-U38-439] Rewarding creates a badge grant tied to the challenge and notifies the user.
- [N-U38-446] Notification of a received badge is a private message with the badge template and a title naming the badge, without an access button.
- [N-U38-455] Leaderboards rank users by summed karma gain in a period using grouped reads that bypass access rules; badge counts per level are computed with a direct read.
- [N-U38-461] The paid orders goal counts invoice report rows whose payment status is paid or in payment; the in-payment value is part of the payment status selection; whether this edition ever produces it was not read here.

### CONSTRAINT
- [N-U38-395] Count and sum definitions carry a filter that may reference the evaluated user, a date field for the goal period, and an optional batch mode keyed on a distinguishing field and a user expression.
- [N-U38-397] For count and sum definitions the filter is evaluated for the current user and a trial count is run; a syntax or value error raises a user error, other errors are not translated.
- [N-U38-398] Domain validity is checked at creation for count and sum modes and again at write when mode, domain or model changes.
- [N-U38-419] The default participant filter is every active internal user.
- [N-U38-424] Only goals of users who were active in the web client within the session lifetime and whose goal was written before their last activity are recomputed, plus goals reached with an end date no earlier than yesterday; closed goals are skipped.
- [N-U38-435] The everyone reward goes to users whose reached goals equal the number of lines; in real-time mode a user already holding the badge for this challenge is skipped.
- [N-U38-437] Top-three badges and the closing chatter message are produced only when the challenge ended, and use the ranking routine.
- [N-U38-438] The ranking routine orders participants by whether all goals are reached then by summed completeness (can exceed 100), keeps only full achievers unless best-if-failed is set, and pads with empty values to the requested length.
- [N-U38-441] A badge can be grantable by everyone, by listed users, by people holding other badges, or by nobody (reserved for challenges); a monthly sending limit per person can be set.
- [N-U38-442] Administrators may always grant; otherwise the rule is checked and the monthly sending limit compared with the number sent this month by the user.
- [N-U38-443] Refusals give distinct messages: not sendable by users, not in the allowed list, required badges missing, or too many sent this month.
- [N-U38-445] Every badge grant, from the wizard or from a challenge, passes the grant check at creation, so the monthly limit and rules also apply to challenge rewards unless the creator is an administrator.
- [N-U38-447] The grant wizard refuses a user granting a badge to themselves, records the sender and comment, creates the grant and sends the notification.
- [N-U38-452] During consolidation a context flag suppresses recomputation of user karma.
- [N-U38-456] Source declares 28 access rows: employees and portal read definitions, challenges, badges and lines, and read and write goals; employees and portal create badge grants; ERP managers have full rights; public reads badges, grants and ranks; karma tracking is system-only.
- [N-U38-457] One access row has no group and no rights for karma tracking.

### RISK
- [N-U38-399] The field-validity check at creation is applied to definitions whose field link equals the text True, which looks like a mistaken condition; if so the check does not run at creation and only runs on write.
- [N-U38-414] The manual goal update dialog writes an extra key that is not a field of the goal; the base write method raises an invalid-field error for unknown names, so saving a manual goal through the dialog would fail in this edition. Source-derived only.
- [N-U38-427] The final-report search requires goal start on or after the last report date and end on or before it, which can match only goals that start and end on that same day; the intent seems to be goals that ended after it.
- [N-U38-430] The initial value for higher-is-better lines is the smaller of target minus one and zero, so a positive target gives zero; for lower-is-better lines it is the larger of target plus one and zero.
- [N-U38-436] The end-of-period test compares the period end, which is a date-time text for recurring challenges and a date object for non-recurring ones, with a date-only text for yesterday; the types differ, so the test appears never true and end-of-challenge actions run only when forced by closing the challenge. Source-derived, not run.

### UNKNOWN
- [N-U38-463] Stored Python goal code written by administrators is not visible in source and is evaluated at run time; challenges seeded by the forum and slides modules were not read; the manual goal update path and period-end rewards need a runtime check.

## CAP-U38-11 Google account link and address autocomplete

### WHAT
- [N-U38-464] Purpose (manifests): let internal users sign in to external Google services with an administrator-configured application (account link) and type addresses with suggestions and automatic filling of structured address fields.

### WHY
- [N-U38-465] Rationale: the consent flow gives each user's own authorization to the calendar bridge without sharing passwords, and the address lookup is restricted to internal users to protect the paid key.

### BUSINESS RULE
- [N-U38-467] The authorization address carries response type code, client id, scope, redirect address, and optional state, approval prompt and access type.
- [N-U38-468] The code exchange posts the code, client credentials and redirect address to the token endpoint and returns access token, refresh token and lifetime; an HTTP error is logged and replaced by a configuration warning telling the user the code may be invalid or expired.
- [N-U38-469] The refresh call has no error handling of its own, so an HTTP failure propagates to the caller, which in the calendar bridge clears the stored tokens on a 400 or 401 reply.
- [N-U38-483] Google address component types are mapped to country, number, city, street, second street, postal code, state and city with fixed priorities; the first mapping to a field wins.
- [N-U38-486] When Google gives no house number it is guessed from what the user typed after removing postal code, street and city and taking the first comma-separated part.
- [N-U38-491] The detail request fetches address components and a formatted address for a place id, keeps the first known type of each component, sorts by priority and translates to the standard fields.
- [N-U38-492] The street line uses Google's formatted text unless it is shorter than the number plus street built locally, which guards against abbreviated answers.

### STATE
- [N-U38-472] A 204 reply gives an empty response; HTTP errors 204 and 404 return an empty text; all other HTTP errors are logged with the body and re-raised.
- [N-U38-476] A refusal or error from Google redirects back to the return address with an error query value; an unknown outcome redirects with an unknown-error value.
- [N-U38-477] The redirect address used for the code exchange is built from the request's own root address, which must equal the one registered with Google.
- [N-U38-478] In the calendar bridge an access token is treated as valid if it lasts at least one more minute, and a refresh failure clears the stored refresh token and access token and commits that clearing before raising a user error naming Google's error key.
- [N-U38-480] A 410 reply that asks for a full sync raises an invalid sync token signal so the caller can restart without a token; a full sync is limited to a configurable window of 365 days either side.
- [N-U38-487] Suggestions are returned only when the typed text is longer than a configurable minimum (default five, so six characters or more); shorter input returns an empty list without calling Google; the client also checks length above five.
- [N-U38-490] Google-side errors (key denied, quota) are logged only; the suggestion path then returns an empty list and the detail path returns no address.

### OPTIONALITY
- [N-U38-466] The Google service layer uses a 20 second default timeout and fixed token endpoint, authorization endpoint and API base address.
- [N-U38-471] GET and DELETE send parameters in the query; POST, PATCH and PUT send a body with headers; other routines raise an error.
- [N-U38-482] The restored database has no Google client id, secret or Places key parameter; the account module declares no views, rules or access rows and owns three metadata entries; the Google-related schedule belongs to other modules.
- [N-U38-496] The partner form gets the autocomplete input control on street fields only when the city enforcement extension is present; other forms add the control through the module's own views.
- [N-U38-497] The Places key is a system parameter exposed in settings, and neutralisation replaces it with a dummy value.
- [N-U38-500] The restored database has 4 view records, no access rows, rules or schedules for this module and no Places key parameter.

### DEPENDENCY
- [N-U38-474] Tokens are stored on the current user's settings row through a method that is defined only by the calendar bridge, so the account module alone lacks that method.
- [N-U38-479] The calendar sync route returns one status: need admin configuration when no client id exists, need authorization with a consent address, need refresh, no new events, stopped or paused, or success. Runtime sync behaviour is not observed.
- [N-U38-484] The country is looked up by its ISO code, and the state is matched within that country by code or by name, only when exactly one state matches.
- [N-U38-485] A city record is matched by case-insensitive name and country when the city extension is installed, and the state is derived from it if missing; the base implementation does nothing.
- [N-U38-488] The suggestion request sends key, address type, text input, optional country restriction, language and session token to the Google Places autocomplete route and returns description and place id pairs.
- [N-U38-498] The browser keeps one session token generated locally and reuses it for suggestions until a detail call is made, after which it is discarded.
- [N-U38-499] Selecting a suggestion fetches the details and fills the configured address fields (street, second street, city, state, zip, country, city link), and puts unmapped parts into the street field.

### CONSTRAINT
- [N-U38-470] Debug logs mask the client secret to its first four characters.
- [N-U38-473] The server date header is returned as the request time for sync ordering, falling back to local time when it cannot be parsed.
- [N-U38-481] Deleting a Google event treats 410 and 403 replies as already deleted.
- [N-U38-493] The Places key is returned only for internal users; the employee-key flag passed by the client is ignored; public callers get an empty suggestion list and an access error on the detail route.
- [N-U38-494] Two web endpoints exist, suggestions and full detail, both declared public so that website forms can use them, but effectively usable only by internal users.
- [N-U38-495] Each lookup is a billable call on the configured Google project; no per-user rate limit or caching exists in this module; a session token groups the suggestions and the final detail call.

### RISK
- [N-U38-475] The missing-field branch raises the language's built-in warning type rather than a platform user error, so it would surface as a server error.
- [N-U38-489] Timeouts are handled as the language's built-in timeout type and value errors, whereas the HTTP library raises its own timeout and connection exception types, which are not subtypes of that built-in; a real timeout or connection failure would therefore not be caught and would reach the caller as an error. Not run.

### UNKNOWN
- [N-U38-501] Google service availability, quota, answer variations and the actual redirect registration cannot be observed statically; the calendar and recaptcha modules belong to another unit and were read only at call sites.

