# U18 — crm_marketing_events — Neutral Knowledge (clean-room layer)

> Odoo 19 Community — study of customer relationship management, marketing communications, events, surveys, short-message and prepaid external-service functions.
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Every statement is tagged with an identifier and is backed by one or more claims in the restricted technical file. Statements describe what the system must do and why, not how it is built.


## Capability 01: Lead and opportunity lifecycle

### WHAT
- [N-U18-001] A single pipeline record represents either an unqualified lead or a qualified opportunity; it carries customer contact data, expected revenue, priority, tags, team, salesperson, notes and a conversation history, and its time spent in each stage is tracked.
- [N-U18-026] Winning a record in the interface shows a celebratory message whose wording depends on recent results of the user, team, source and country; it has no business effect.

### WHY
- [N-U18-002] Separating lead from opportunity lets a business qualify raw inquiries before committing sales effort; whether the lead step exists at all is a feature choice, and when it is off every new record starts as an opportunity.

### BUSINESS RULE
- [N-U18-003] A new record goes to the first open stage available to its team; stages may be shared by all teams or limited to chosen teams; any stage change is time-stamped so that stagnation can be measured.
- [N-U18-004] Marking a stage as the won stage immediately sets every record in that stage to full probability; un-marking it hands probability back to the automatic score.
- [N-U18-007] Expected and recurring revenue are tracked per record; recurring revenue is converted to a monthly amount through a recurring plan, and prorated values multiply by probability; recurring figures are shown only to users who enabled that feature and are cleared when duplicating for other users.
- [N-U18-008] Probability of winning is a number between zero and one hundred; it normally follows an automatic score derived from past wins and losses and from the stage, but a person can overwrite it, after which the automatic score no longer moves it until restored.
- [N-U18-010] The date of assignment is stamped when a salesperson is set or changed and cleared when the salesperson is removed, which lets reports measure time to assign.
- [N-U18-011] Each time a record becomes won or lost, or leaves those states, the scoring statistics are updated immediately; one record can never be both won and lost.
- [N-U18-013] Losing a record archives it, sets its probability to zero and stores the chosen reason; a closing comment can be logged in the conversation history at the same time.
- [N-U18-014] Restoring a lost record reactivates it, clears the lost reason and returns its probability to the automatic score.
- [N-U18-015] Marking a record won moves it to the won stage that follows its current stage in sequence (or the nearest earlier won stage) and sets probability to full.
- [N-U18-016] Converting a lead to an opportunity records the conversion date, optionally links or creates the customer and assigns salespersons; archived or won leads are skipped and closed leads cannot be converted through the dialog.
- [N-U18-017] When no customer exists, conversion creates one from the lead: a company record if a company name exists, and a contact person under it; the new customer inherits the salesperson, notes, phone, email, address, website and language of the lead.
- [N-U18-018] Duplicates may be merged into the most reliable record, chosen by activity, type, stage, probability and age; text is concatenated, tags are united, the richest address is kept, and messages, activities, attachments and meetings move to the survivor; at most five records can be merged by an ordinary user.
- [N-U18-020] Potential duplicates are detected by business email domain (or the full address for free mail providers), by identical phone, or by belonging to the same customer company; the search deliberately ignores access rules and archive status so that managers see the counter, and is abandoned for a criterion that matches twenty-one or more records.
- [N-U18-022] Email and phone are labelled correct or incorrect from format checks; the labels are advisory, do not block saving, and are used as inputs of the automatic score.

### STATE
- [N-U18-009] A record is won when it sits in a won stage at full probability and lost when it is archived at zero probability; otherwise it is pending; a won record cannot be lost without first moving it to another stage, and closing dates are set and cleared automatically.
- [N-U18-025] Creation, stage change, won, lost and restore events post to the conversation history with specific event types so followers can subscribe to them; deleting a record detaches its meetings instead of deleting them.

### OPTIONALITY
- [N-U18-005] A new system starts with four stages: new, qualified, proposition and a won stage; businesses add, rename or limit stages by team.
- [N-U18-006] A short list of lost reasons is supplied (price, missing skills, missing stock) and can be extended; choosing a reason when losing is encouraged by the dialog but the record can be lost without one.
- [N-U18-012] A periodic job that rebuilds all scoring statistics and recomputes automatic probabilities exists but is switched off by default; the fields used for scoring and the earliest creation date considered are configurable parameters.

### DEPENDENCY
- [N-U18-027] The pipeline lifecycle itself posts nothing to accounting or stock; financial effects begin only when a quotation is created and confirmed from the opportunity.
- [N-U18-028] When the email marketing bridge is installed, leads can be selected as mailing recipients, subject to the global exclusion list.

### CONSTRAINT
- [N-U18-023] A record belongs to at most one company, chosen coherently from its team, salesperson and customer; users see records of their own companies and records with no company.
- [N-U18-024] Sales managers have full control; salespersons can read, change and create records but not delete them; the own-documents salesperson sees only records assigned to them or unassigned, while the all-documents salesperson sees everything; stages and lost reasons can be changed only by managers.

### RISK
- [N-U18-019] Merging permanently deletes the absorbed records using elevated rights, so a merge is not reversible and the absorbed records' creator, audit trail and exact original field values are lost.
- [N-U18-021] Editing the email or phone of a lead that is linked to a customer silently rewrites the customer record as well, which can change contact data used by other documents.

### UNKNOWN
- Not applicable to this capability.

## Capability 02: Lead intake and assignment

### WHAT
- [N-U18-029] A sales team groups salespersons, may use leads, opportunities or both, owns an email alias that turns incoming mail into leads, and can be excluded from automatic assignment.
- [N-U18-040] Mail sent to a team address creates a lead whose name is the subject, whose sender is the contact, and whose salesperson is deliberately left empty so that assignment rules decide; a later reply to a recipient can link that recipient as customer to every open lead with the same address.
- [N-U18-041] A chat bot step can create a lead from the visitor's contact data and conversation transcript, or create it and hand the chat to an available salesperson of an eligible team.
- [N-U18-042] A mail-client add-in can create a lead for a known customer from the subject and body of an email, within the customer's company.
- [N-U18-043] Survey answers marked as lead-generating create opportunities for the survey's team, assigned to the survey owner if a member of that team and otherwise to the team leader.
- [N-U18-044] Event registration rules create leads with a preset type, team, salesperson and tags.

### WHY
- Not applicable to this capability.

### BUSINESS RULE
- [N-U18-030] Each team member has a capacity expressed as an average number of leads per thirty days, optional filters describing which leads they accept or prefer, and a pause switch.
- [N-U18-033] A manager can also run assignment on demand from a team; the on-demand run ignores today's already assigned count, considers all leads regardless of age, and writes a summary note on the team.
- [N-U18-036] Leads with neither team nor salesperson are first allocated to teams by a random draw weighted by team capacity; teams without capacity are skipped; possible duplicates of an allocated lead are merged and the absorbed copies are deleted.
- [N-U18-037] Within a team, unassigned leads go to members round by round: members with remaining daily quota and a matching filter, preferred leads first, higher probability first; assigned leads become opportunities and members drop out once their quota is used.

### STATE
- Not applicable to this capability.

### OPTIONALITY
- [N-U18-031] Two assignment styles exist: simple mode gives a new unassigned lead to the team leader; rule-based mode distributes leads according to team and member capacity and filters; rule-based mode is off by default and is switched on by a configuration parameter.
- [N-U18-032] Rule-based assignment can run on a schedule; the scheduled job is created inactive and is activated or retimed from the settings page together with its repeat interval.
- [N-U18-035] System parameters allow a waiting period before new leads are eligible and a commit batch size for large runs.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- [N-U18-034] Only sales managers and administrators may start automatic assignment.
- [N-U18-038] Assignment filters of teams and members must be valid search expressions or saving is refused.
- [N-U18-045] Lead mining configuration and requests are restricted to sales managers.

### RISK
- [N-U18-039] Large assignment runs save their work in batches, so an interruption leaves the earlier batches applied and cannot be rolled back as a whole.

### UNKNOWN
- Not applicable to this capability.

## Capability 03: Opportunity to quotation hand-off and membership grading

### WHAT
- [N-U18-046] From an opportunity a salesperson creates a quotation prefilled with the customer, campaign, medium, source, origin, team, salesperson, company and tags; if the opportunity has no customer a short dialog offers to create one, link an existing one, or continue without one.

### WHY
- Not applicable to this capability.

### BUSINESS RULE
- [N-U18-048] When a linked order is confirmed, the opportunity's expected revenue is increased to the order's amount excluding tax if that is greater, but only when the order is in the company currency; the increase is logged in the opportunity's history and is never reduced afterward.
- [N-U18-051] A product can grant a customer a membership level; confirming an order for it sets that level on the customer's company, which also switches the customer to the level's price list; one order may not grant two different levels and a price list cannot be assigned both directly and through a level.

### STATE
- [N-U18-049] An opportunity shows how many quotations (draft or sent) and orders (confirmed or later) it has and the summed untaxed amount converted to company currency; merged opportunities bring their orders with them.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- [N-U18-054] Email marketing reports count quotations, invoiced amounts and opportunities by campaign source using elevated rights, so mailing users see aggregates that exceed their own document access; orders can also be chosen as a mailing audience, excluding cancelled orders by default.

### CONSTRAINT
- [N-U18-047] A quotation can reference one opportunity of the same company, so quotations roll up to their opportunity.
- [N-U18-053] Salespersons can use the customer dialog and create membership levels; sales managers and administrators have full control; internal users may read levels.

### RISK
- [N-U18-050] Confirming an order does not mark the opportunity won and cancelling it does not mark it lost, so pipeline status and sales status can diverge unless users maintain both.
- [N-U18-052] No rule withdraws a membership level or its price list when the granting order is cancelled or refunded, so the pricing benefit can outlive the sale.

### UNKNOWN
- Not applicable to this capability.

## Capability 04: Event registration, seat limits, tickets and attendee communications

### WHAT
- [N-U18-055] An event has dates, a venue, an organizer, a stage, optional seat limits, optional ticket types with their own sale windows and limits, optional time slots, questions and an automated communication schedule; each attendee seat is one registration with the attendee's name, email, phone, company and answers.

### WHY
- Not applicable to this capability.

### BUSINESS RULE
- [N-U18-057] Registered and attended seats are counted against limits set on the event, on each ticket and, for events with slots, on each slot and ticket combination; an over-sold change is refused with a message listing the missing seats.
- [N-U18-058] An event accepts registrations only while it is not cancelled, the end date has not passed, sales have started, seats remain and at least one ticket, if tickets exist, is on sale.
- [N-U18-060] At the entrance a desk user scans the ticket code: the system refuses unknown codes, cancelled or unconfirmed registrations and finished events, asks for manual confirmation when the ticket belongs to another event, reports already scanned tickets, and otherwise marks the attendee as attended.
- [N-U18-061] Each registration gets a random unique ticket code; ticket download links are protected by a signature over the event and registrations so that guessing identifiers is not enough.
- [N-U18-062] Communications are scheduled relative to registration, event start or event end; they go only to registered or attended people, are sent in batches by a daily job and by on-demand triggers, skip attendees who were cancelled in the meantime, and failures are reported on the event without stopping other communications.

### STATE
- [N-U18-056] A registration is unconfirmed, registered, attended or cancelled; the system accepts any change of state without a fixed path, records the attendance date and note when someone is marked attended, and refreshes communication schedules when a registration becomes registered.
- [N-U18-065] Events progress through stages (new, booked, announced, ended); ended events are moved to the end stage automatically after their end date.

### OPTIONALITY
- [N-U18-063] When the short-message bridge is installed a communication step can be a text message instead of an email.

### DEPENDENCY
- [N-U18-064] When the email marketing bridge is installed, an event's attendees or all contacts can be selected as the audience of a marketing mailing.
- [N-U18-068] When ticket selling is installed, the registration state is computed from the sales order instead of being set directly.

### CONSTRAINT
- [N-U18-059] Slots and tickets must belong to the event; slots must lie within the event dates; the end cannot precede the start; ticket sale dates and per-order limits must be coherent; a ticket that has registrations cannot be deleted; a ticket product must be flagged as an event registration product.
- [N-U18-066] Registration desk staff can read events and tickets and register attendees; event users can additionally edit events, tickets and schedules; event administrators have full control; deletion of registrations is administrator-only.
- [N-U18-067] Events, registrations and tickets are visible only for the user's companies or when no company is set; the scheduler runs for all companies.

### RISK
- Not applicable to this capability.

### UNKNOWN
- Not applicable to this capability.

## Capability 05: Event ticket and booth sales, payment hooks and lead generation

### WHAT
- [N-U18-069] Tickets and booths are sold as ordinary products on sales orders; each order line for a ticket names the event, the ticket type and, when applicable, the time slot, and each booth line lists the desired booths.

### WHY
- Not applicable to this capability.

### BUSINESS RULE
- [N-U18-070] Confirming an order for tickets requires every ticket line to be fully configured, then creates one registration per ticket ordered (minus those already existing and not cancelled); for a single order confirmed by a user, paid tickets start unconfirmed so attendee details can be filled in before the final registration.
- [N-U18-072] When the customer on an order changes, every attendee registration of that order is moved to the new customer.
- [N-U18-073] Booths are reserved when the order is confirmed: all selected booths must still be available, they become unavailable and record the renter, and every other customer's order that had selected any of the same booths is cancelled automatically with a message; a booth is marked paid when the related invoice becomes paid.
- [N-U18-078] Lead generation rules create a lead for each attendee or for each order when registrations are created, registered or marked attended; rules can be filtered by event, event type, company and attendee conditions, carry a lead type, team, salesperson and tags, skip registrations already converted by the same rule, and can be rerun by an event administrator, in batches of two hundred through a daily job for large events.

### STATE
- [N-U18-071] A registration is cancelled when its order is cancelled, free and registered when the order total is zero, sold and registered when the order is confirmed, and otherwise unconfirmed and awaiting payment; the status depends on order confirmation only, not on the customer having paid.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- [N-U18-075] Payment-dependent actions are triggered from the accounting module when an invoice is posted with a zero total or when reconciliation brings it to paid or in-payment status; an error in such an action would interrupt that accounting step.

### CONSTRAINT
- [N-U18-076] Ticket lines need event, ticket type and slot where required; booths of one order line must belong to one event; a booth linked to an order cannot be deleted.
- [N-U18-077] Salespersons configure ticket and booth lines and can edit attendees; they also hold registration-desk rights; event users manage booths and booth registrations; event administrators manage rules and can regenerate leads for an event; the event sales report is readable only by event administrators.

### RISK
- [N-U18-074] Nothing reverses a booth reservation or its paid mark when an invoice is credited, cancelled or unpaid, and cancelling competing orders happens with elevated rights regardless of whether they were already invoiced or paid.
- [N-U18-079] Attendee names, emails and phone numbers are copied into leads and into lead descriptions by rules that run with elevated rights, so attendee personal data becomes visible to salespersons and follows the lead's retention.

### UNKNOWN
- Not applicable to this capability.

## Capability 06: Marketing email campaigns: sending, tracking and links

### WHAT
- [N-U18-080] A marketing mailing combines an email design, a sender, an audience and a schedule; every recipient gets a delivery record whose status moves through outgoing, sent, opened, replied, bounced, failed or cancelled.
- [N-U18-092] Marketing cards are personalised images that recipients can share; the image and preview pages are public and identified only by a number or slug, share and visit are counted when crawlers or visitors open them, old cards are deleted after sixty days, and a mailing is blocked until all cards are up to date.

### WHY
- Not applicable to this capability.

### BUSINESS RULE
- [N-U18-081] The audience is chosen from mailing lists or from a saved search on any mailable record type (contacts, customers, leads, orders, event attendees, course members); an unreadable search yields an empty audience; people already mailed in the same mailing are not mailed again, and an split-test test mails a random percentage of people not yet mailed in the campaign.
- [N-U18-083] Queued mailings are sent by a periodic job and by triggers at their scheduled time; the job commits as it goes, sets the sent date, and a statistics email is sent to the responsible person one to five days after the first send when the reports option is on; sending with no recipient is refused.
- [N-U18-087] An address that bounces at least five times within thirteen weeks, with the first and last bounce more than a week apart, is automatically added to the global exclusion list.
- [N-U18-088] Every link in a mailing is replaced by a short tracked link that carries the campaign, medium and source; unsubscribe, view and card links are left unchanged; creating a tracked link may make the server fetch the target page to read its title.

### STATE
- [N-U18-082] A mailing is draft, queued, sending or done; launching or scheduling queues it, cancelling returns it to draft, and retrying failed deliveries removes failed sends and queues the mailing again.
- [N-U18-085] Delivery results are written back to each recipient's record; cancelled mail records are purged after six months unless configured otherwise.

### OPTIONALITY
- [N-U18-084] A campaign can run an split-test test; the winner is chosen by opens, clicks, replies, or, when bridges are installed, by leads, quotations or revenue.
- [N-U18-089] Options include a dedicated outgoing mail server for marketing, keeping archives, 24-hour statistics emails, split-test testing activation, and whether tracking parameters are added to links that leave the company's own site; personal mail servers are never used for mass mailings.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- [N-U18-090] The split-test percentage must be between zero and one hundred; an split-test mailing needs a campaign; a saved filter must match the audience type; each combination of link, campaign, medium, source and label is unique; a card campaign mailing must target the card's record type.
- [N-U18-091] Anyone in the email marketing group can create, change and delete mailings, lists, contacts, traces, subscriptions and the exclusion list; administrators have full access; tracked links and clicks are readable by internal users.

### RISK
- [N-U18-086] Opens are detected with an invisible image and clicks with redirect links that store the visitor's network address and country; click links do not verify who is clicking, so anyone holding a link code can add clicks or opens to statistics, and behavioural tracking occurs without a consent check in the system.

### UNKNOWN
- Not applicable to this capability.

## Capability 07: Marketing consent, unsubscribe and exclusion lists

### WHAT
- Not applicable to this capability.

### WHY
- Not applicable to this capability.

### BUSINESS RULE
- [N-U18-093] Marketing sends exclude every address on a global blocked-address list and every phone number on a blocked-number list, as long as the exclusion option is on; the option is on by default and the interface warns to switch it off only when absolutely necessary; addresses and numbers are normalised, kept unique, and removing one archives it so its history stays.
- [N-U18-094] At send time each recipient is classified in a fixed order: blocked, missing or invalid address, opted out, already mailed, identical content already sent to the same address; the reason is stored on the delivery record so exclusions can be audited; opt-out and duplicate checks still apply when the exclusion option is switched off.
- [N-U18-095] A contact opts out of individual mailing lists with a date and a reason; a mailing to several lists excludes the contact only if opted out of every involved list where the same address is not opted in elsewhere; opt-out reasons are configurable and one reason asks for free feedback.
- [N-U18-096] Each marketing email carries personal links protected by a signature over the mailing, the record and the address, so recipients can act without logging in; the signature never expires.
- [N-U18-097] Following the unsubscribe link opts the recipient out of the lists of that mailing, or, when the audience is not a mailing list (customers, leads, attendees, orders), places the address on the global blocked list; one-click unsubscribe from mail programs is supported and performs the change immediately.
- [N-U18-100] Text-message marketing can append a stop link with a short random code; the recipient must enter their number, which must match the stored delivery record, and is then opted out of the lists or placed on the blocked-number list; the stop link option is off by default on the mailing but on in the standalone composer.

### STATE
- Not applicable to this capability.

### OPTIONALITY
- [N-U18-098] Recipients can open a preferences page to re-join public lists, leave lists, add or remove their own address on the blocked list, and leave a reason and comment; logged-in users can open the page for their own address without a signature; the blocked-list buttons can be hidden by a setting, but the underlying actions are not disabled by that setting.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- [N-U18-101] Anyone in the email marketing group can edit the global blocked-address list and subscriptions, although ordinary access to that list is administrator-only elsewhere; the blocked-number list is administrator-only; public unsubscribe pages perform their changes with elevated rights after token checks.
- [N-U18-102] A subscription is unique per contact and list; invalid addresses and numbers cannot be blocked; a list used by an unfinished mailing cannot be archived.

### RISK
- [N-U18-099] The system substitutes the personal unsubscribe link only if the design contains the placeholder, and does not verify that every marketing email contains an unsubscribe link, so a modified design can send marketing mail without one.

### UNKNOWN
- [N-U18-103] It is not established whether survey invitations honour the blocked-address list, nor whether contact import preserves opt-out status or records consent; there is no stored proof of when or how a person opted in.

## Capability 08: Text-message sending, delivery status and credit use

### WHAT
- Not applicable to this capability.

### WHY
- Not applicable to this capability.

### BUSINESS RULE
- [N-U18-105] Messages posted on a record are created with elevated rights from the customer's phone number and are sent immediately within the user's own transaction unless queuing is requested; queued messages are sent in batches by a periodic job and by a trigger each time a message is created.
- [N-U18-108] Using the prepaid service sends the message text, destination numbers, message identifiers, the database identifier, the account token and a callback address to the service operator; the operator holds the credit balance and charges per message.
- [N-U18-110] Failures are classified as missing number, wrong format, unsupported country, insufficient credit, server error or unregistered account; an exception while contacting the provider marks the whole batch as server error without telling the user; marketing messages that failed can be retried, and the mailing offers to buy credits; without the phone-number library numbers are not validated.
- [N-U18-113] With Twilio, message text and numbers go to Twilio with the company's credentials and a callback address; a short timeout applies per message; Twilio authentication failures are not given a dedicated failure label.

### STATE
- [N-U18-104] A text message is queued, processing, sent to the operator, delivered, failed or cancelled; a delivery report can only move its status forward, never back; failed messages can be resent.

### OPTIONALITY
- [N-U18-106] Batch sizes are configurable parameters (five hundred by default, ten for the company's own provider); the queue job runs daily and on demand.
- [N-U18-107] Each company chooses between Odoo's prepaid service and its own Twilio account; with Twilio, a sender number per destination country is configured and each message is sent one by one.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- [N-U18-115] Every internal user can open the composer and send text messages to any typed number at the company's cost; message rows and trackers are administrator-only; templates are editable by administrators and, for their own record types, by sales and event managers; Twilio setup is administrator-only.

### RISK
- [N-U18-109] The system keeps no record of credits spent by messages and reads no price from the operator, so consumption can only be audited on the operator's side, and the user is told of exhausted credit only through the failure status and a buy-credits link.
- [N-U18-111] The provider is contacted inside a database transaction, so if the transaction is rolled back after sending, the messages stay queued and a retry can send them a second time, which means duplicate messages and duplicate cost.
- [N-U18-112] Delivery reports from the prepaid service arrive on a public address that is not signed and relies only on the secrecy of long random message identifiers; reports from the company's own Twilio account are authenticated by a signature made with the account token.
- [N-U18-114] Message bodies and numbers are stored until the message is marked for deletion and then purged by a cleanup, while the notification and any logged copy remain; the Twilio authentication token is stored unencrypted though visible only to administrators.

### UNKNOWN
- Not applicable to this capability.

## Capability 09: External data services, prepaid credits and the personal data they transmit

### WHAT
- Not applicable to this capability.

### WHY
- Not applicable to this capability.

### BUSINESS RULE
- [N-U18-116] Vendor-operated services are called with a secret account token and the database identifier; the vendor charges a prepaid balance per use; endpoints default to the vendor's addresses and can be overridden by parameters; the system never calls the vendor during automated tests, and a neutralised database gets disabled tokens.
- [N-U18-118] Lead enrichment looks up the company behind a business email domain for recent, open leads and fills only fields that are empty, then marks the lead as enriched; it runs daily or on demand and can be switched to on-demand only.
- [N-U18-119] Lead mining searches the vendor's company database by country, region, size, industry and optional contact role or seniority, up to two hundred companies and five contacts per company per request, and turns the answer into leads for a chosen team and salesperson.
- [N-U18-120] Enrichment consumes credit only when company data is returned; generic mailboxes and invalid addresses are skipped without cost; mining costs one credit per company plus one per contact; the user is guided to buy credits when the balance is exhausted.
- [N-U18-121] A service failure never blocks the record being worked on: enrichment errors are logged and optionally shown, an exhausted balance stops the batch and shows a purchase link, autocomplete returns an error message instead of suggestions, mining records an error state, and network timeouts become access errors that name the service address; reading a balance that cannot be fetched yields minus one.

### STATE
- [N-U18-117] An account for each service is created on first use, can be tied to one or more companies or be global, shows its balance and status by asking the vendor whenever the account form is opened, and can send low-balance alerts to chosen users; the account token is a secret stored in clear in the database and visible only to administrators.

### OPTIONALITY
- Not applicable to this capability.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- [N-U18-123] Any internal user can read and create accounts but not see the token; administrators manage accounts and services; lead mining is limited to sales managers; accounts are limited to the user's companies or global.

### RISK
- [N-U18-122] Personal and commercial data leaves the database: lead email domains, the existing lead identifiers visible to the requesting user, company names and tax numbers typed on forms, the company's own domain, country and postal code, the language and version of the system, and the email addresses and languages of chosen alert recipients; tax-number lookups can also go to the European VIES service directly; the vendor's full answer is written into the lead history; company enrichment overwrites the company logo.

### UNKNOWN
- [N-U18-124] What the vendor retains, how credits are priced, and whether the typed-text trigger of company autocomplete is rate-limited are not visible in the source.

## Capability 10: Surveys, scoring, certification and survey-driven leads

### WHAT
- Not applicable to this capability.

### WHY
- Not applicable to this capability.

### BUSINESS RULE
- [N-U18-125] A survey is open to anyone with the link or to invited people only, and may additionally require login; every survey route checks that the survey exists, is active and has questions, that the participation's token is valid, that the deadline has not passed and that the person answering is the person invited.
- [N-U18-128] The random token in a participation link or cookie is the only credential for resuming, viewing or changing that participation; tokens are unique and need no login for invited or public surveys.
- [N-U18-129] Attempts can be limited per person (partner or email) and invitation for invited-only or login-required surveys; test entries are not counted; a failed participant can retry if attempts remain, creating a fresh participation.
- [N-U18-130] Scoring compares earned points to the maximum obtainable for the questions shown; a minimum percentage defines passing; scoring modes decide whether correct answers are revealed never, at the end, or after each page; a certification requires scoring.
- [N-U18-131] Time limits are checked on the server with a short grace period; a completed participation sets the end time, notifies followers, emails the certificate to people who passed a certification and may grant a badge; a preview of the certificate creates and removes a temporary participation.
- [N-U18-132] Inviting people sends one email each with a personal link; typed email addresses are matched to existing customers, and for login-required surveys to all customers with that email; invitations skip attempt checks and resending reuses the latest participation.

### STATE
- [N-U18-127] A participation is new, in progress or done; it is created when a visitor starts or when an invitation is prepared, and a random token identifies it.

### OPTIONALITY
- [N-U18-133] Answers can be flagged to generate a lead; when a participation completes (or a live session ends) an opportunity is created for the survey's team, assigned to the survey owner when that person belongs to the team, otherwise to the team leader.

### DEPENDENCY
- Not applicable to this capability.

### CONSTRAINT
- [N-U18-135] Invitations require questions, a positive obtainable score for scored surveys and an active survey; a certification needs scoring and a unique badge; going back is incompatible with after-page scoring.
- [N-U18-136] Survey users and administrators manage surveys; survey officers see only unrestricted surveys or surveys that list them; public participants act only through tokens; certificates can be downloaded by the logged-in customer who passed.

### RISK
- [N-U18-126] The code contains checks for employee-only and authentication-required modes that no longer correspond to any selectable option, so such restrictions cannot be relied upon; only public, invited-only and login-required remain.
- [N-U18-134] Answers, including free text, email and nickname, are copied into lead descriptions; the participation token grants access and can trigger account-claim links for the invited customer when login is required; the 24-hour cookie that stores the token has no explicit security flags in the code read; lead creation by anonymous participants has no rate limit.

### UNKNOWN
- Not applicable to this capability.
