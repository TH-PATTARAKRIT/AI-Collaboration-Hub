# U29 Residual Bridges - Neutral Knowledge (Odoo 19 Community, clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source revision 19.0.post20260921. Scope: small bridge features that were not claimed by any earlier unit - bundle-cost margin, expiry-aware availability, dispatch planning with vehicles and docks, text-message contact and marketing bridges, portal and public-website bridges, course certifications, management dashboards, and editor, email layout and social account helpers.

## CAP-U29-01 Sales margin on bundled (kit) products - cost bridge

### WHAT
- [N-U29-001] The module intended to handle component-based prices for sales margin contains no business logic of its own; it only declares two prerequisite features and ships automated tests.
- [N-U29-002] Each sales order line carries a cost and a margin, and each order carries a total margin and a margin percentage; these are visible only to internal users.
- [N-U29-003] The cost of a product sold as a bundle (several component items delivered for one sold line) is derived from the components, not from a cost recorded on the bundle itself; the tests expect multi-level bundles and bundles sold in packs to be costed by exploding the composition.
- [N-U29-004] The stated purpose of the module is to handle composition-based prices so that the sales margin of bundles can be computed.

### WHY
- [N-U29-005] Management needs the margin shown on an order to reflect the true cost of what was delivered, including for bundles that are sold as one line but leave the warehouse as several items.

### BUSINESS RULE
- [N-U29-006] Until a delivery movement that is neither draft nor cancelled exists, the line cost is the product standard cost converted to the line unit of measure and the order currency.
- [N-U29-007] Line margin equals the untaxed line subtotal minus cost times ordered quantity; for a line added after delivery with no ordered quantity, margin is computed from unit price and delivered quantity. The percentage is zero when the subtotal is zero.
- [N-U29-008] When the product category does not use standard costing and something has been delivered, the line cost becomes a quantity-weighted blend of the delivered unit cost and the standard cost for the quantity still to deliver.
- [N-U29-009] When the category uses standard costing, a delivery does not overwrite an existing line cost; only lines added from a delivery with no ordered quantity use the base calculation.
- [N-U29-010] The delivered unit cost of a bundle is the sum, over its components, of component unit cost times component quantity per bundle, divided by the bundle quantity basis and then by the delivered quantity; dropshipped components are priced at the vendor-supplied cost.
- [N-U29-011] Only outgoing delivery movements and dropshipped movements enter the delivered cost of a sale line; manufacturing movements are ignored, and dropshipped and regular movements are combined by weighted average.
- [N-U29-012] When a customer invoice is posted for a bundle, the cost-of-goods unit amount is the quantity-weighted sum of the storable components' cost-of-goods prices divided by the bundle quantity basis; for a credit note under standard or average costing the original invoice's amount is reused.

### STATE
- [N-U29-013] The line cost is recomputed whenever the line's movements, their values or the delivery state change; before the first valued movement it is the standard cost, afterwards it follows the delivered-cost rules above.

### OPTIONALITY
- [N-U29-014] The module is not installed automatically with its prerequisites, whereas the two prerequisite features are; since the module has no logic, removing it would change no behavior.
- [N-U29-015] In the reference configuration the module is installed and contributes no permissions, rules, scheduled jobs, screens or data.

### DEPENDENCY
- [N-U29-016] Behavior depends on the sales-manufacturing bridge and on the delivered-cost margin bridge; the bundle cost chain also relies on manufacturing accounting and stock accounting being present.

### CONSTRAINT
- [N-U29-017] Cost and margin fields may be read only by internal users; portal and public users cannot see them. The cost field can be edited manually.

### RISK
- [N-U29-018] If the composition of a bundle is changed between delivery and invoice posting, the cost used on the invoice may differ from the cost at delivery.
- [N-U29-019] In the reference configuration all explicitly configured product categories use standard costing, so the delivered-cost blending rule is dormant there.

### UNKNOWN
- [N-U29-020] Numeric results of the bundle cost chain were not executed and remain unverified at runtime.
- [N-U29-021] Whether cost-of-goods lines are generated on invoices for bundle sales under the reference periodic valuation is not determined.

## CAP-U29-02 Expiry-aware stock forecast on sales order lines

### WHAT
- [N-U29-022] On a sales order line, the stock availability shown to the salesperson counts only fresh stock: quantities that will already be removed because of expiry are excluded.
- [N-U29-023] Whether a line is treated this way depends on a per-product flag stating that the product has an expiration date.
- [N-U29-024] For such products the screen labels change to 'fresh forecasted stock' and 'fresh available' and a caption states that the available figure is for today.

### WHY
- [N-U29-025] Promising stock to a customer that will expire before delivery would cause failed or spoiled shipments, so the order screen must show what will still be usable at the promised date.

### BUSINESS RULE
- [N-U29-026] The forecast at the delivery date excludes unreserved stock whose removal date falls on or before that delivery date.
- [N-U29-027] The free quantity is on hand minus reserved minus expired unreserved quantity, and the forecast quantity also subtracts the expired unreserved quantity.
- [N-U29-028] Today's date is the reference for expiry in every quantity computation made by the expiry feature.
- [N-U29-029] The shown free quantity for expiry-tracked lines is re-read as of today for the warehouse, not as of the delivery date.
- [N-U29-030] The free-quantity re-read is triggered when any line in the same computation batch has an expiring product, and it then replaces the free quantity for all products of that batch.
- [N-U29-031] Quantities are read per warehouse and scheduled date, where the scheduled date is the order commitment date or the expected delivery date.
- [N-U29-032] Quantities already consumed by earlier lines for the same product are subtracted from what later lines are shown.

### STATE
- (no statement in this section)

### OPTIONALITY
- [N-U29-033] The feature is installed automatically when the sales-delivery and product-expiry features are both present and is delivered to the back-office interface only.
- [N-U29-034] The availability display appears only for storable products with a quantity still to deliver on quotations and confirmed orders.

### DEPENDENCY
- [N-U29-035] It depends on the sales-delivery feature for the availability display and on the product-expiry feature for removal dates and the expiry flag.
- [N-U29-036] The screen widget loads the expiry flag with each line as an extra dependency.

### CONSTRAINT
- [N-U29-037] The feature changes display only; it does not reserve stock, alter removal strategy or block selling expiring stock.

### RISK
- [N-U29-038] Pairing of re-read quantities with the base results relies on both lists following the same product order.
- [N-U29-039] In the reference configuration the feature is installed but no orders or lots exist, so no figure can be observed.

### UNKNOWN
- [N-U29-040] Screen behavior with real lots and expiry dates was not executed.

## CAP-U29-03 Transport dispatch on batch transfers (vehicle, driver, dock, capacity)

### WHAT
- [N-U29-041] Transfers can be grouped into dispatch batches that are assigned a vehicle or a third-party carrier category, a driver and a dock location; the screens show shipping weight and volume and the operations overview gains transport entries.
- [N-U29-042] Dispatch management is switched on by default for receipt and delivery operation types and, depending on the delivery steps, for picking or packing types; warehouse reconfiguration keeps this setting.

### WHY
- [N-U29-043] Warehouses that ship with own fleets or carriers need to plan loads against vehicle capacity, assign docks and know the stop order for drivers.

### BUSINESS RULE
- [N-U29-044] Each operation type with dispatch enabled may list dock locations; for multi-step delivery the warehouse output location is linked automatically as the dock of the delivery type.
- [N-U29-045] Batches are ordered by the postal code of the transfer partner: stop sequence is the position in postal-code order, and transfers without a postal code come first. Sequencing runs when a batch is created.
- [N-U29-046] Placing a transfer into a batch with a dock, or setting a dock on a batch, moves the planned location of the transfer's movements to the dock; placing it in a batch without a dock restores the original location.
- [N-U29-047] Restoring location resets only movements whose destination lies outside the transfer's own destination tree.
- [N-U29-048] Choosing a vehicle fills the vehicle category and the driver, both of which remain editable so that a third-party carrier can be described by category alone.
- [N-U29-049] The dock of a batch is chosen automatically when all its transfers start from one common location that is an allowed dock.
- [N-U29-050] The batch end time defaults to one hour after the scheduled time and is pushed forward if it would fall earlier.
- [N-U29-051] Weight and volume utilisation are the batch estimated weight and volume as a percentage of the capacity of the chosen vehicle category; with no capacity the percentage is zero.
- [N-U29-052] For internal and incoming types the dock becomes the destination of the movements; for other types such as deliveries it becomes the source. No movement status is checked before the change.
- [N-U29-053] Merging batches keeps the vehicle and dock of the merged batch.
- [N-U29-054] Vehicle categories carry maximum weight and volume capacities, shown in the category name using the system-wide weight and volume units.
- [N-U29-055] Batches can be filtered as own fleet when a vehicle is set, or third-party carrier when only a category is set.
- [N-U29-056] The printed batch document shows dock, vehicle, category and the stop sequence for each transfer.

### STATE
- (no statement in this section)

### OPTIONALITY
- [N-U29-057] Dispatch fields and the dock list appear only when the operation type has dispatch enabled; dock editing additionally needs the multi-location option.

### DEPENDENCY
- [N-U29-058] The feature needs batch transfers and the vehicle fleet feature; shipping weight and volume come from the base inventory feature.
- [N-U29-059] Batch weight, volume and transfer shipping weight are computed in the base inventory and batch features, not here.

### CONSTRAINT
- [N-U29-060] A dock must be an internal location of the same warehouse as the operation type and must be among that type's docks.
- [N-U29-061] Docks are cleared when the operation type of a batch or the warehouse of an operation type changes.
- [N-U29-062] When a location is edited from a dock list its usage cannot be changed.
- [N-U29-063] The feature adds no permissions of its own; access to batches follows the inventory user permission set, with full rights.

### RISK
- [N-U29-064] The vendor marks two date filters (tomorrow and next seven days) as incorrect in the search definition.
- [N-U29-065] In the reference configuration dispatch is enabled on two operation types, but no docks, vehicles or batches exist, so none of the dispatch behavior is exercised.

### UNKNOWN
- [N-U29-066] The consequences of rewriting movement locations after reservation or on completed transfers are not determined.

## CAP-U29-04 Visitor and event-attendee SMS contact bridges

### WHAT
- [N-U29-067] Staff can text a website visitor straight from the visitor list, card or form when a mobile number is known, and event organisers can choose between email and text message when mass-mailing attendees or inviting contacts.

### WHY
- [N-U29-068] Reaching a visitor or attendee on the channel that works shortens follow-up; the bridges remove the need to copy numbers into a separate tool.

### BUSINESS RULE
- [N-U29-069] A visitor can be texted when its linked contact has a phone number.
- [N-U29-070] The message is addressed to the contact record, in single-recipient comment mode, using the contact's phone.
- [N-U29-071] The composer accepts the name of the record field that holds the number and uses it to find the recipient number.
- [N-U29-072] If the visitor has no contact or no number, the action stops with a user error; otherwise a message composer opens as a dialog.
- [N-U29-073] When the contact has no phone but the visitor is linked to sales leads, the visitor can still be texted if a lead carries the visitor's number; the best-ranked lead is preferred.
- [N-U29-074] Leads are ranked by being active first, opportunity over lead, higher stage, higher win probability, then most recent.
- [N-U29-075] A lead becomes the addressee only when the visitor has no contact at all.
- [N-U29-076] From an event, both the attendee mailing and the invitation mailing open a form where the user can pick email or text message.
- [N-U29-077] The mixed form shows the mailing type and is not the default form used elsewhere.
- [N-U29-078] The attendee mailing targets registrations of the event that are neither cancelled nor draft; the invitation mailing targets contacts.

### STATE
- (no statement in this section)

### OPTIONALITY
- [N-U29-079] All three bridges are installed automatically when their parent features are present.
- [N-U29-080] The SMS buttons on the visitor screens are shown only when the visitor has a mobile number; the number comes from the contact, or from the newest lead when the contact gives none.

### DEPENDENCY
- [N-U29-081] The bridges depend on the website, SMS, CRM, event and SMS-marketing features; actual sending depends on the SMS gateway and credits.
- [N-U29-082] The visitor mobile number is computed from the contact's phone and, with the CRM feature, falls back to the newest lead phone.

### CONSTRAINT
- [N-U29-083] The link from a visitor to leads is visible only to sales staff; the text buttons themselves are not restricted to a group.

### RISK
- [N-U29-084] The lead path passes the number-field name in a form that differs from the contact path, so it may be ignored by the composer.
- [N-U29-085] In the reference configuration these bridges add screen and field extensions only; no permissions, rules or scheduled jobs belong to them.
- [N-U29-086] Permissions that decide who can see visitors and use the composer come from the base features, not from the bridges.

### UNKNOWN
- [N-U29-087] Delivery of the text message, gateway credits and failure handling were not exercised.

## CAP-U29-05 SMS marketing campaign bridges (split-test winner metrics, SMS newsletter subscription)

### WHAT
- [N-U29-088] An SMS split test can pick its winner by the number of sales leads generated by each variant.
- [N-U29-089] An SMS split test can also pick its winner by the number of quotations or by the invoiced revenue generated by each variant.
- [N-U29-090] Website visitors can subscribe to a mailing list with a mobile number through a new newsletter block variant and a matching option in the website builder.

### WHY
- [N-U29-091] Click rate alone does not show commercial value; selecting the winner by leads, quotations or revenue ties the choice to business outcomes, and the SMS block lets visitors opt in on the channel the company will use.

### BUSINESS RULE
- [N-U29-092] SMS split tests have their own winner criterion, separate from the email one, with manual selection and highest click rate built in and click rate as the default.
- [N-U29-093] Automatic winner selection sorts the sent variants in descending order of the chosen metric and takes the first; the sort uses elevated rights so metrics from other applications can be read.
- [N-U29-094] If no variant has been sent yet the selection fails with a validation message, and a completed split test cannot be run again.
- [N-U29-095] The winner is duplicated as a final mailing addressed to all remaining recipients and launched, and the campaign records it as the winner.
- [N-U29-096] For text-message mailings the criterion and the competing variants are those of the campaign's text-message tests.
- [N-U29-097] The scheduled job picks campaigns past the scheduled date with an automatic criterion, and the text-message extension sends the text winner only when at least one text variant has been sent.
- [N-U29-098] Lead metric: the count of leads, archived ones included, that carry the same tracking source as the mailing.
- [N-U29-099] Quotation metric: the count of sales orders with at least one line that carry the same tracking source as the mailing.
- [N-U29-100] Revenue metric: the sum of untaxed signed amounts of accounting documents that are neither draft nor cancelled and carry the same tracking source; it is kept as a whole number, and the summed amounts are in the company currency of each document.
- [N-U29-101] The mobile field of mailing contacts is allowed to be filled from website forms; the permission is applied by an installation step that only a website designer may perform.
- [N-U29-102] For a mobile subscription the number is prefilled from the logged-in user's contact phone, or from the value remembered in the visitor session, and the mobile field of the contact is used for matching.
- [N-U29-103] A public check tells visitors whether the entered value is already an active subscriber of the list.
- [N-U29-104] Subscribing first requires a successful bot-protection check; failure returns a visible error message instead of subscribing.
- [N-U29-105] Subscribing creates a contact and subscription when none match, re-activates an opted-out subscription, and for mobile subscribers uses the number as the contact name and stores it without normalisation.

### STATE
- [N-U29-106] A subscription is active once created, and returns from opted-out to active when the same value subscribes again.

### OPTIONALITY
- [N-U29-107] All three bridges are installed automatically when their parent features are present.

### DEPENDENCY
- [N-U29-108] The criteria depend on lead and quotation tracking features and on text-message marketing; the subscription block depends on the newsletter block.
- [N-U29-109] The newsletter feature depends on the bot-protection integration for subscription checks.
- [N-U29-110] The scheduled jobs that process queues and split tests belong to the base mass mailing feature and are active in the reference configuration.

### CONSTRAINT
- [N-U29-111] The text subscription layout template is limited to internal users; public subscription calls are open to everyone and write with elevated rights.

### RISK
- [N-U29-112] In the reference configuration the form permission for the mobile field is in place and no bridge-owned permissions, rules or jobs exist.
- [N-U29-113] Subscribing by text uses the raw typed number without normalisation, and the files show no confirmation step or consent wording, so duplicates and consent gaps are possible.
- [N-U29-114] The scheduled job selects campaigns by the email winner criterion, so a text-message winner is sent automatically only when the campaign's email criterion is also set to automatic.

### UNKNOWN
- [N-U29-115] The behavior of the bot-protection check when it is not configured was not determined.
- [N-U29-116] Sorting variants by computed metrics at scheduled-job time was not executed.

## CAP-U29-06 Website bridges: portal timesheet visibility switch and public mail-group subscription block

### WHAT
- [N-U29-117] When the customer portal timesheet entry is hidden, timesheet information is also hidden on other portal pages, for tasks, sales orders and invoices.
- [N-U29-118] A discussion group can open its public page from a button on the group form.
- [N-U29-119] Website editors can place a Discussion Group block with an email field and subscribe and unsubscribe buttons tied to a chosen group.

### WHY
- [N-U29-120] Companies that decide not to show timesheets to customers need one switch that applies everywhere, otherwise hours and employee details leak through other portal pages.
- [N-U29-121] Public mailing lists need an entry point on the website so visitors can join without back-office help.

### BUSINESS RULE
- [N-U29-122] The portal decision to show timesheets follows whether the portal home timesheet customisation is active.
- [N-U29-123] When a website is selected the website-specific version of that customisation prevails over the generic one; without a website only the generic one counts. A missing customisation hides the information.
- [N-U29-124] Task pages, confirmed sales order pages and invoice pages in the portal show timesheet sections only when the decision allows and timesheets exist.
- [N-U29-125] The portal home timesheet entry is a customisable item that site editors can switch on or off.
- [N-U29-126] Mailing list menus are placed under the website configuration menu.
- [N-U29-127] A public check reports whether an email address is a member of a given group.
- [N-U29-128] If an access token is supplied it must match the group's token, in which case the check is made with elevated rights; without a token the caller must be allowed to read the group.
- [N-U29-129] The group access token is a keyed hash of the group identity and authorises subscribe and unsubscribe links.
- [N-U29-130] For logged-in users the check uses their own email and contact instead of the supplied address; membership is looked up with elevated rights.
- [N-U29-131] Dropping the block uses the first existing group or asks for a name and creates a group, and the drop is cancelled when no group is chosen.
- [N-U29-132] The public widget asks the server about membership when the page loads and removes itself if the answer is empty.

### STATE
- [N-U29-133] Portal timesheet information is shown while the customisation is active and hidden while it is inactive.

### OPTIONALITY
- [N-U29-134] Both bridges are installed automatically when their parent features are present.
- [N-U29-135] The Discussion Group block is optional website content and its install placeholder disappears once the feature is installed.

### DEPENDENCY
- [N-U29-136] The timesheet bridge depends on the website and timesheet features; the base timesheet feature documents that this bridge overrides its decision.
- [N-U29-137] Without the bridge the portal always shows timesheet information.
- [N-U29-138] The discussion group block depends on the mail group and website features.

### CONSTRAINT
- [N-U29-139] The moderation rules menu is limited to mail group managers.
- [N-U29-140] Public and portal users can read discussion groups; internal users have full access to them.

### RISK
- [N-U29-141] In the reference configuration the controlling customisation exists once, generic and active, so timesheets are currently shown; the bridge owns no permissions or rules.
- [N-U29-142] The public membership check reveals whether an address is a member of a readable group, so enumeration depends on group access settings and throttling that were not examined.
- [N-U29-143] In the reference configuration three menus and four website templates come with the bridge; no discussion group, permission or rule exists.

### UNKNOWN
- [N-U29-144] Website editor behavior for the block was read for logic only and not executed.

## CAP-U29-07 Course certifications (survey-based certification slides in e-learning)

### WHAT
- [N-U29-145] A course can contain a Certification step linked to a scored survey; certifications appear in their own menu and as a content type with a trophy icon.
- [N-U29-146] The learner's slide record holds the learner's certification attempts, and each slide may link one survey.

### WHY
- [N-U29-147] Training providers need proof that learners mastered the material; tying a passed assessment to completion, certification status, badges and profile removes manual follow-up.

### BUSINESS RULE
- [N-U29-148] A slide that is given a survey becomes a certification slide automatically.
- [N-U29-149] A certification created from the website starts with one attempt, one question per page, no time limit, scoring that does not reveal answers, a 70 percent pass mark and the standard certification email.
- [N-U29-150] Creating a survey from the website requires the right to create surveys and linking an existing one requires the right to read it; otherwise an error is returned and the slide is not created.
- [N-U29-151] Success of a certification is stored on the learner's slide record and is derived from the learner's answers with a successful score.
- [N-U29-152] A successful certification marks the slide as completed for that learner.
- [N-U29-153] Learners cannot mark certification slides complete or incomplete themselves; the website refuses such a request.
- [N-U29-154] When a learner passes any certification of a course, the learner is flagged as certified in that course.
- [N-U29-155] A certification slide without a name takes the survey title as its name.
- [N-U29-156] The challenge category of the certification badge is set so that the badge appears with course certifications while a survey is linked to a slide, and is reset when no slide uses it.
- [N-U29-157] Starting a certification as a member continues the latest attempt or creates a new one with its own invitation token; non-members get a test entry that is not counted.
- [N-U29-158] Starting a certification requires a logged-in user; for members the slide is marked as viewed.
- [N-U29-159] When a learner finishes an attempt unsuccessfully and has no attempts left, a failure email is sent and the learner is removed from the course and must enrol again; with attempts left nothing happens.
- [N-U29-160] Attempt limits are enforced only for surveys with limited attempts that require login or are not public.
- [N-U29-161] Retrying an attempt keeps the link to the course slide and membership.
- [N-U29-162] The failure email tells the participant that they failed, are no longer a member of the course and may enrol again.
- [N-U29-163] The number of certified members of a course is the number of memberships flagged certified.
- [N-U29-164] Certificates shown on a learner's profile and in user lists are finished certification answers with successful scoring and a successful slide record.
- [N-U29-165] The ranks and badges page lists certification badges separately, ordered by number of users granted, limited to badges used in courses.
- [N-U29-166] On removal of the feature the certification badge goal is reset to a condition that is never true.
- [N-U29-167] On installation the certification badge is published and its goal counts certification slides with a successful score.

### STATE
- [N-U29-168] Learner progress runs from not completed to completed once the certification is passed, and from member to removed after a final failed attempt.

### OPTIONALITY
- [N-U29-169] The feature is installed automatically with e-learning and surveys; each course decides whether it contains certifications.

### DEPENDENCY
- [N-U29-170] The feature depends on the e-learning and survey features; scoring, attempt counting and badge granting belong to them.

### CONSTRAINT
- [N-U29-171] A certification slide must link a survey.
- [N-U29-172] A certification slide cannot be offered as a free preview.
- [N-U29-173] A survey that is used as a course certification cannot be deleted, and the message lists the courses concerned.
- [N-U29-174] Course officers can see the courses that a survey certifies.
- [N-U29-175] The certification tab of a profile is visible only to the user concerned or to a survey manager.
- [N-U29-176] Course officers get read-only access to certification surveys, their questions, answer options and answers, limited to certification surveys that are not restricted to other users.
- [N-U29-177] Only survey users are offered the button to add a certification from a course.

### RISK
- [N-U29-178] When several failing answers are processed together only the last one's course removal appears to be applied, because the collection is reset inside the loop.
- [N-U29-179] In the reference configuration permissions and rules equal the source, the badge is published with its goal overridden, and no course, slide or answer exists.

### UNKNOWN
- [N-U29-180] Whether the certified flag is ever cleared, and the end-to-end flow, were not executed.
- [N-U29-181] Profile, course and lesson page templates were not read in detail.

## CAP-U29-08 Management dashboards (events, expenses, project tasks, timesheets, live chat, warehouse metrics)

### WHAT
- [N-U29-182] Six managed bridges add dashboards to the Dashboards area: events, expenses, project tasks, timesheets, two live chat boards and warehouse metrics.
- [N-U29-183] Events dashboard: numbers of events, attendees and sales revenue (untaxed and taxed), events by venue, template, tag and organizer, registrations by state and events by stage; filtered by date (default last twelve months), venue, template, tags and organizer.
- [N-U29-184] Expenses dashboard: total amounts of expenses waiting to be reported, to be validated and to be reimbursed, monthly totals by product, rankings by product, employee and re-invoiced order; filtered by period (default last twelve months), product, order and employee.
- [N-U29-185] Project dashboard: tasks, hours logged, time to assign and time to close, by assignee, project, tag and customer, with task stage and status charts; filtered by period (default last thirty days), assignee, project, tag and customer.
- [N-U29-186] Timesheet dashboard: billable hours, non-billable hours and billable rate by project, task, department and employee, and hours by billing type; filtered by period (default last thirty days), project, task, department and employee.
- [N-U29-187] Live chat dashboard: sessions, duration, time to respond, messages per session, rating, calls, handling by bot or agent, escalation, outcome, and rankings by agent, country, language, expertise and chatbot answer path; agents that operate chatbots are excluded from agent rankings.
- [N-U29-188] Ongoing sessions board: counts of sessions without an end time by handler, escalation and calls, with five menus listing ongoing sessions; the all-sessions list is limited to live chat channels.
- [N-U29-189] Warehouse dashboard: stock quantity, reserved share by quantity and value, stock value and negative stock lines for internal locations, with the ten worst negative products; filtered by warehouse, location, product category, product and lot or serial number.

### WHY
- [N-U29-190] Managers need an at-a-glance, filterable view per business area without building reports; sample content shows what the board will look like before data exists.

### BUSINESS RULE
- [N-U29-191] When any main data model of a dashboard has no readable or countable record and a sample exists, the sample is shown instead of live figures and is marked as sample.
- [N-U29-192] A shared dashboard link works only with its random token and only while the person who shared it can still read the dashboard.
- [N-U29-193] The project dashboard has no sample and no declared main data model, so it never switches to sample content.
- [N-U29-194] A dashboard group provided with the product cannot be deleted by users.
- [N-U29-195] Allowed companies for the figures come from the user's company selection; dashboards may be limited to companies, and those of the reference configuration are not.

### STATE
- (no statement in this section)

### OPTIONALITY
- [N-U29-196] Each dashboard is installed automatically when its business feature is present: event sales, sales-linked expenses, timesheets, timesheet invoicing, live chat and stock accounting.

### DEPENDENCY
- [N-U29-197] Each dashboard depends on the Dashboards platform and on the data of its business feature; figures are read live from those features when the dashboard is opened.

### CONSTRAINT
- [N-U29-198] A user sees a dashboard only if they belong to one of its listed groups; dashboard administrators see all.
- [N-U29-199] Reading dashboard data requires a logged-in user.
- [N-U29-200] Internal users can read dashboards and dashboard groups; only dashboard administrators can change them.
- [N-U29-201] Audience by dashboard: events for event managers, expenses for expense managers, project and timesheets for timesheet approvers, live chat boards and ongoing menus for live chat managers, warehouse metrics for stock managers.
- [N-U29-202] Figures are subject to the viewer's own rights on the underlying data: event sales are readable by event managers, stock value only by stock managers, and aggregates follow company rules.

### RISK
- [N-U29-203] Timesheet approvers might lack read rights on the task analysis data behind the project dashboard unless they also hold a project role.
- [N-U29-204] In the reference configuration seven dashboards from these bridges are published in five groups, each with one visibility group and none limited to a company; the project dashboard has no sample.
- [N-U29-205] Sharing a dashboard creates a public frozen copy reachable by token; no share exists in the reference configuration.

### UNKNOWN
- [N-U29-206] Evaluation of every data source as each role was not executed.

## CAP-U29-09 Builder, email theme and social-account bridges

### WHAT
- [N-U29-207] A generic drag-and-drop editor is provided that the website builder and the mass-mailing designer both use; it has tabs for blocks, customisation and theme and supports undo and redo.
- [N-U29-208] Eleven ready-made email layouts are added to the mailing designer: event promotion, newsletter, training, coupon code, coffee break, blogging, magazine, big news, promotion programme and two roadshow variants.
- [N-U29-209] The company record gains eight places to keep social network account addresses so that other features can use them.

### WHY
- [N-U29-210] One editor avoids duplicating editing logic across website and email, ready layouts speed up campaign creation, and one place for social accounts avoids re-entering them.

### BUSINESS RULE
- [N-U29-211] Edit-only styles are kept apart from the main editor styles, and an automated check enforces that none leaks into the main bundle.
- [N-U29-212] The editor opens on the blocks tab unless configured otherwise; customisation shows options for the selected element or a translation panel in translation mode.
- [N-U29-213] Undo and redo are available through keyboard shortcuts.
- [N-U29-214] Only structures bound to a stored view, record field or cover block are savable; modified ones are flagged and saved to their source with website and language context where applicable.
- [N-U29-215] Users can save a block as a custom snippet, rename it or delete it after confirmation; the server stores and removes the snippet together with its entry in the block list.
- [N-U29-216] Option panels can create and update related records of arbitrary types using the editing user's own rights.
- [N-U29-217] Background shapes and image shapes are served as coloured images from a public route.
- [N-U29-218] Two default images for the layouts are registered as public attachments reachable by address.
- [N-U29-219] The eight social account fields are free text and each company keeps its own values.
- [N-U29-220] Each website starts with the main company's account values, so later edits of the company record do not update existing websites.
- [N-U29-221] The website derives the X handle for page metadata from the last part of the company's X address.

### STATE
- (no statement in this section)

### OPTIONALITY
- [N-U29-222] The themes are installed automatically with mass mailing; the builder and social account modules are hard dependencies of website and mass mailing and so are always present with them.

### DEPENDENCY
- [N-U29-223] The editor depends on the base rich-text editor and mail features.
- [N-U29-224] The website feature and the mass mailing feature both depend on the builder and on the social account module.
- [N-U29-225] The themes depend on the mass mailing feature.
- [N-U29-226] The social account module depends only on the base platform.

### CONSTRAINT
- [N-U29-227] The theme list is available to internal users only.
- [N-U29-228] The social account group on the company screen is visible only in developer mode.
- [N-U29-229] The social account fields have no format validation.

### RISK
- [N-U29-230] In the reference configuration the themes and public images are present, no social account is filled, and none of the three modules owns permissions, rules or scheduled jobs.

### UNKNOWN
- [N-U29-231] Most editor plugins and the live editing behavior were not read or executed.
- [N-U29-232] Layout bodies and their rendering in mail clients were not examined.
