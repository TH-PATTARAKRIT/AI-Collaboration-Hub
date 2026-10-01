# U06 purchase_order - Neutral Knowledge (clean-room layer)

> Status: `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION`. Source basis: Odoo 19 Community, studied read-only. Written as business and process rules; no technical identifiers.

## CAP-U06-01 Quotation and purchase order lifecycle (states, transitions, locking)

### WHAT
- [N-U06-001] A purchase document passes through five states: draft quotation, quotation sent, awaiting approval, confirmed order, and cancelled. There is no distinct closed or done state in the order lifecycle; completion is expressed only through receipt status and billing status.
- [N-U06-002] Locking is an independent marker on a confirmed order and is not a lifecycle state.

### WHY
- [N-U06-003] The states separate negotiation with a vendor (a quotation that creates no commitment) from the binding commitment (a confirmed order), so that approval, communication, receiving and billing are controlled at the right moment.

### BUSINESS RULE
- [N-U06-004] Sending the quotation to the vendor, either by composing the email or by printing the quotation, moves a draft quotation to the sent state; other states are not changed by sending.
- [N-U06-005] Confirmation applies only to quotations in draft or sent state; orders in any other state are silently skipped.
- [N-U06-006] After confirmation an order either becomes a confirmed order immediately or waits for approval, depending on the company approval policy and the user.
- [N-U06-007] Approving an order marks it confirmed and records the confirmation date and time; if the company policy locks confirmed orders, the order is locked at that moment.
- [N-U06-008] An order can be deleted only after it has been cancelled.
- [N-U06-009] The vendor acknowledgement marker can be set at any time on the order, by the buyer or by the vendor through the shared link, and does not depend on the state.
- [N-U06-010] Duplicating an order always produces a new draft quotation without confirmation date, lock or acknowledgement, and expected arrival dates are recalculated from vendor lead times.

### STATE
- [N-U06-011] Draft quotation to quotation sent: by sending or printing. Draft or sent to awaiting approval: by confirmation when the approval policy requires a manager. Draft, sent or awaiting approval to confirmed order: by confirmation (when permitted) or by manager approval. Draft, sent, awaiting approval or confirmed to cancelled: by cancellation. Cancelled to draft: by reset. Locked is toggled independently on confirmed orders.
- [N-U06-012] The interface offers each button only in the states for which it is meant (for example approve only while awaiting approval, reset only while cancelled, cancel only while not locked), but the underlying approve, reset and cancel operations themselves do not check the current state.

### OPTIONALITY
- [N-U06-013] Sending the quotation is optional: a draft quotation can be confirmed directly without being sent.
- [N-U06-014] Automatic locking after confirmation is a company-level choice; the manual lock action is offered in the interface only when that policy is on.

### DEPENDENCY
- [N-U06-015] When the inventory integration is installed, approving an order creates the expected receipts, and cancelling an order cancels open receipts and related stock movements; when the sales integration is installed, cancelling an order that was generated from a sales order schedules a warning activity on that sales order.
- [N-U06-016] Status changes, lock changes, acknowledgement, buyer, vendor and untaxed amount are tracked in the order history, and each state change posts a message with a state-specific subtype.

### CONSTRAINT
- [N-U06-017] Non-note lines of a confirmed order cannot be deleted, whether or not the order is locked.
- [N-U06-018] When an order is locked, the lines, payment terms and fiscal position become read-only in the interface and cancellation is refused on the server.

### RISK
- [N-U06-019] Lock enforcement for edits appears to exist only in the user interface; programmatic or import-based edits of a locked order may not be refused (runtime check required).
- [N-U06-020] Because approve, reset and cancel do not verify the current state, a programmatic call can move an order between states the interface would not allow (runtime check required).
- [N-U06-021] Some dashboards and the vendor portal still reference a closed state and a quotation key that no longer exist, so counts and report selection for those cases may be wrong or empty.
- [N-U06-022] Acknowledgement is recorded when the vendor link is merely opened with the acknowledge parameter, so a link preview or crawler could mark an order acknowledged.

### UNKNOWN
- [N-U06-023] Whether confirming an order again after reset to draft recreates receipts correctly after earlier cancellation is determined in the inventory integration and was not examined here.

## CAP-U06-02 Order confirmation and approval (double validation, what confirmation writes and triggers)

### WHAT
- [N-U06-024] Confirming an order checks that the order is complete, optionally validates mandatory analytic distribution, registers the vendor on products when needed, and then either approves the order or sends it for approval.

### WHY
- [N-U06-025] Two-level approval lets a company require a manager to authorise large commitments while ordinary buyers can commit smaller ones.

### BUSINESS RULE
- [N-U06-026] Confirmation is refused with an error if any ordinary line (not a note, section or down-payment line) has no product.
- [N-U06-027] Under single-step approval every confirmation is also an approval.
- [N-U06-028] Under two-step approval an order is approved directly only if its total is strictly below the configured threshold, converted from company currency into the order currency at the order date, or if the confirming user belongs to the purchase manager group; otherwise the order goes to the awaiting approval state.
- [N-U06-029] The approval comparison uses the order total including taxes.
- [N-U06-030] The manager approve operation silently ignores orders for which the current user is not allowed to approve rather than raising an error.
- [N-U06-031] On confirmation, for every product line whose vendor (or the vendor's parent company) is not already on the product vendor list, a new vendor price record is added automatically, provided the product has no more than ten vendors; the record uses the line price converted to the product base unit, the line currency and discount, minimum quantity one and lead time zero.
- [N-U06-032] The automatic vendor price record is written with elevated rights so that it is created regardless of the confirming user's access to product data.

### STATE
- [N-U06-033] Confirmation moves draft or sent to confirmed order or to awaiting approval; manager approval moves awaiting approval to confirmed order and stamps the confirmation date.

### OPTIONALITY
- [N-U06-034] Two-step approval, its threshold (default five thousand in company currency) and automatic locking are company settings, editable only by purchase administrators in the settings screen.
- [N-U06-035] Mandatory analytic distribution is validated at confirmation only when the confirm button passes the validation flag, and only for lines whose analytic plans are configured as mandatory.

### DEPENDENCY
- [N-U06-036] When the inventory integration is installed, approval triggers receipt creation; when the agreements module is installed, confirming an order that has open alternative quotations first asks whether to keep or cancel those alternatives.
- [N-U06-037] Confirmation depends on the product's vendor price list, the fiscal and currency rules of the company, and the analytic plan applicability configuration.

### CONSTRAINT
- [N-U06-038] Only the approve button is restricted to purchase managers in the interface; the underlying operation is gated only by the approval rule, so any user with write access can approve an order that falls under the threshold or under single-step approval.

### RISK
- [N-U06-039] The threshold conversion uses the currency of the user's current company as the source rather than the order's own company, which may give a wrong comparison when users work across companies with different currencies (runtime check required).
- [N-U06-040] Bulk confirmation from a list action and automatic confirmation from other wizards do not pass the analytic validation flag, so mandatory analytic distribution may be skipped on those routes.
- [N-U06-041] An order whose total equals the threshold exactly requires manager approval, because the comparison is strict.

### UNKNOWN
- [N-U06-042] Behaviour when the company currency conversion rate is missing for the order date was not traced.

## CAP-U06-03 Cancellation, reset to draft, and lock or unlock

### WHAT
- [N-U06-043] Cancelling stops an order or quotation; resetting returns a cancelled order to draft; locking and unlocking control whether a confirmed order can be edited.

### WHY
- [N-U06-044] Cancellation must not orphan financial documents: an order with posted vendor bills cannot disappear, and a locked order must be consciously unlocked first.

### BUSINESS RULE
- [N-U06-045] A locked order cannot be cancelled until it is unlocked; the refusal names the orders concerned.
- [N-U06-046] An order cannot be cancelled while any linked vendor bill is in a state other than draft or cancelled; the user must first cancel those bills.
- [N-U06-047] Draft vendor bills do not block cancellation and remain linked to the order lines; because billing quantities on a cancelled order are zero, such bills no longer count toward amounts to be billed.
- [N-U06-048] Cancelling cascades to open receipts and related stock movements when the inventory integration is installed, leaves completed receipts untouched with a note, and posts a warning activity on the originating sales order when one exists.
- [N-U06-049] Merging quotations cancels the merged quotations after moving their lines, and posts messages on both the surviving and the cancelled quotations.
- [N-U06-050] Locking is offered in the interface only when the company policy is to lock confirmed orders; unlocking is offered only to purchase managers.
- [N-U06-051] Once bills exist for a line, its unit price and discount become read-only in the interface and automatic price recalculation stops for that line.
- [N-U06-052] When a quantity is changed on a confirmed order, a note is posted in the order history; adding an extra product line to a confirmed order also posts a message.

### STATE
- [N-U06-053] Cancelled to draft by reset; draft to cancelled again by cancellation; locked to unlocked by unlock, which is a precondition for cancellation of a locked order.

### OPTIONALITY
- [N-U06-054] The agreement module additionally cancels draft quotations linked to a cancelled agreement; it does not touch quotations in other states.

### DEPENDENCY
- [N-U06-055] Bill status, receipt status and sales-order warnings all depend on the cancellation sequence in the integrating modules.

### CONSTRAINT
- [N-U06-056] The server refuses cancellation of locked orders and orders with live bills; the manager-only restriction on unlocking exists only in the interface.

### RISK
- [N-U06-057] Reset to draft does not clear the lock marker, the confirmation date or the acknowledgement marker (runtime check required).
- [N-U06-058] Cancellation does not verify the current state, so an already cancelled order can be cancelled again without error.

### UNKNOWN
- [N-U06-059] Whether previously cancelled receipts are recreated when a reset order is confirmed again belongs to the inventory integration.

## CAP-U06-04 Vendor pricing and vendor price list records

### WHAT
- [N-U06-060] On each order line the system selects the best applicable vendor price record for the product, vendor, quantity, unit and date, and uses it to default the unit price, discount, description and expected arrival date.

### WHY
- [N-U06-061] Buyers should not retype negotiated prices, minimum quantities and lead times; the vendor price list is the single source for them.

### BUSINESS RULE
- [N-U06-062] A vendor price record applies only if it belongs to the order company or to no company, its vendor is active, and it is either for the exact variant or for all variants.
- [N-U06-063] A record is ignored if its start date is after, or its end date before, the order date.
- [N-U06-064] A record is ignored if the line quantity, converted to the record's unit, is below the record's minimum quantity.
- [N-U06-065] On purchase lines the record's unit must equal the line unit or the product base unit.
- [N-U06-066] Only records of the order vendor or of the vendor's parent company are considered.
- [N-U06-067] Among eligible records the one with the lowest discounted price, converted to company currency at the order date, wins; ties are resolved by sequence; records of only one vendor are compared at a time.
- [N-U06-068] The line unit price defaults from the selected record converted to the order currency and the line unit; with no record it defaults from the product cost converted by currency and unit.
- [N-U06-069] The expected arrival date of a line defaults to the order date plus the selected record's lead time, or the order date alone if none, and today if no order date.
- [N-U06-070] A price manually typed on a line is preserved: recalculation is skipped when the current price differs from the last automatically proposed price, when bills already exist, or when a conversion-skip flag is set.
- [N-U06-071] Choosing a product proposes the smallest applicable minimum quantity of that vendor and its unit, or one unit if there is none.
- [N-U06-072] The units offered on a line are the product base unit, its additional units, and the units used by its vendor price records.

### STATE
- NOT APPLICABLE — nothing identified for this section in the examined material.

### OPTIONALITY
- [N-U06-073] A vendor price record may be restricted by company, variant and validity dates, all optional.

### DEPENDENCY
- [N-U06-074] Price records created from confirmed blanket orders are visible to price selection only on orders linked to the same agreement.
- [N-U06-075] The same selection logic feeds the product catalogue panel on orders, the automatic replenishment path in the inventory integration, and the agreement-based line pricing.

### CONSTRAINT
- [N-U06-076] Creating or editing vendor price records directly is limited to purchase administrators; ordinary buyers receive records only through confirmation, which writes with elevated rights.

### RISK
- [N-U06-077] Price conversion to company currency for ranking uses the current company, so ranking may differ across companies (runtime check required).
- [N-U06-078] Vendor records auto-created on confirmation use minimum quantity one and lead time zero regardless of what was actually agreed, which can silently distort later pricing and dates.

### UNKNOWN
- [N-U06-079] No vendor price records or purchasable stored products exist in the restored database, so selection behaviour could not be observed in data.

## CAP-U06-05 Vendor bill generation and bill control

### WHAT
- [N-U06-080] A vendor bill can be generated from one or more orders, from selected lines in the bill-matching screen, or by auto-completing a draft bill from an order; bill status on the order and billable quantities on lines are computed from linked bill lines.

### WHY
- [N-U06-081] The bill control policy decides whether the vendor may be paid for what was ordered or only for what has been received, which is the basis of three-way matching between order, receipt and bill.

### BUSINESS RULE
- [N-U06-082] Bill control is set per product: either on ordered quantities or on received quantities; services default to ordered quantities and other products default to received quantities.
- [N-U06-083] The quantity still to bill on a line of a confirmed order is the ordered quantity minus billed quantity under the ordered policy, and the received quantity minus billed quantity under the received policy; for orders not in confirmed state it is zero.
- [N-U06-084] Billed quantity sums non-cancelled vendor bill lines, adding bills and subtracting credit notes, converted to the line unit; draft bills therefore count as billed.
- [N-U06-085] Order billing status is nothing to bill unless the order is confirmed; waiting for bills if any line has a non-zero quantity to bill; fully billed if all quantities to bill are zero and at least one bill exists.
- [N-U06-086] Generated bills copy vendor, currency, fiscal position, payment terms, notes, the vendor's bank account for the company, and the order reference as origin; bill line quantity equals the quantity to bill, price is converted into the bill currency, and section headings are copied only when another line follows them.
- [N-U06-087] Orders selected together are merged into one bill per company, vendor and currency; a bill whose total is negative is converted to a credit note.
- [N-U06-088] Received quantity on lines of services and non-stock goods is entered manually in the purchasing module itself; for stock-managed goods it comes from completed receipts in the inventory integration.
- [N-U06-089] Posting a message on the bill records which orders it was created from or later linked to.
- [N-U06-090] Down-payment lines carry zero ordered quantity and are linked to the bill line that paid them; the section that holds them is created on demand.
- [N-U06-091] Electronic or scanned bills are matched to confirmed orders by order name or vendor reference with a tolerance of two cents on totals, then by line subset or by vendor and total.

### STATE
- [N-U06-092] Order billing status moves nothing to bill, waiting for bills, fully billed purely by computation from the lines; it is not edited directly.

### OPTIONALITY
- [N-U06-093] Strict three-way matching that blocks payment until goods are received is not part of the community edition: the setting offers it as an upgrade, and only the received-quantity policy is available in the base purchasing logic.
- [N-U06-094] Bill control can be changed per product by purchase administrators.

### DEPENDENCY
- [N-U06-095] Received quantity, and therefore per-receipt billing alignment, depends on the inventory integration; the incoterm is copied onto the bill by that integration.

### CONSTRAINT
- [N-U06-096] Uploading an attachment while creating bills for several vendors is refused.
- [N-U06-097] Line matching refuses selections without order lines, with several vendors, or with lines belonging to more than one order.

### RISK
- [N-U06-098] Under the ordered policy a vendor can be billed before any goods are received, and no warning for bill-before-receipt was found in the purchasing module.
- [N-U06-099] Bill creation does not itself refuse orders that are not confirmed; their lines carry zero quantity, so empty bills can result (runtime check required).
- [N-U06-100] Creating a purchase order from vendor bill lines confirms it immediately, so it may land in awaiting approval or be confirmed without prior review.

### UNKNOWN
- [N-U06-101] Accounting entries produced when the bill is posted, and valuation differences between order and bill prices, are outside this unit.

## CAP-U06-06 Order line rules and amounts

### WHAT
- [N-U06-102] Order lines are either billable product lines or non-billable structure lines (section, subsection, note); amounts, taxes and dates are computed per line and rolled up to the order.

### WHY
- [N-U06-103] Structure lines let buyers organise a document without affecting amounts; per-line dates and units reflect vendor delivery terms.

### BUSINESS RULE
- [N-U06-104] Structure lines are stored with no product, no price, no quantity, no unit and no date; ordinary lines require product, unit and expected date unless they are down-payments.
- [N-U06-105] The type of a line can never be changed after creation.
- [N-U06-106] Line subtotal and total are computed by the standard tax engine from quantity, price, discount and taxes, using the order currency and rate; order amounts exclude structure lines.
- [N-U06-107] Taxes on a line default from the product's vendor taxes limited to the order company and mapped through the order's fiscal position; changing the fiscal position or company recomputes them.
- [N-U06-108] The expected arrival date of the order is the earliest line date; changing it on the order pushes that date to all lines.
- [N-U06-109] Default analytic distribution comes from distribution models matching product, product category, vendor, vendor category and company.
- [N-U06-110] The order currency defaults to the vendor's purchase currency, otherwise the company currency; the currency rate is stored from the order date.
- [N-U06-111] Quotations in draft with the same vendor and company are flagged as possible duplicates when the vendor reference matches or when the source equals another order name; cancelled orders are ignored.
- [N-U06-112] Merging selected quotations requires state draft or sent, at least two quotations with equal vendor, currency and delivery address (plus agreement or receipt type with integrations); lines with the same product, unit, analytic distribution, discount and a date within a day are summed, keeping the lower price.
- [N-U06-113] A product's unit of measure cannot be changed once other units were used in purchase lines.

### STATE
- NOT APPLICABLE — nothing identified for this section in the examined material.

### OPTIONALITY
- [N-U06-114] Section, subsection and note lines, additional units of measure and analytic accounting are optional features.

### DEPENDENCY
- [N-U06-115] Line amounts depend on the tax engine, the fiscal position, the vendor price list and the currency rate table.

### CONSTRAINT
- [N-U06-116] An order cannot contain products that belong to a company outside the order's company branch tree.
- [N-U06-117] Products, units and dates on accountable lines are mandatory by database check.

### RISK
- [N-U06-118] Duplicate detection only warns; it does not prevent confirmation.
- [N-U06-119] The header comment in the purchase report states it is not multi-currency while its query uses a currency conversion table, so report amounts should be validated in a multi-currency environment (runtime check required).

### UNKNOWN
- [N-U06-120] Behaviour with negative or zero ordered quantities on confirmed lines beyond the credit-note conversion was not found as a validation.

## CAP-U06-07 Reminders, schedulers and vendor notifications

### WHAT
- [N-U06-121] A daily scheduled job reminds vendors by email shortly before the expected receipt date of confirmed, unacknowledged orders; vendors can acknowledge the order and change scheduled dates through a shared link.

### WHY
- [N-U06-122] Early reminders reduce late deliveries and make vendor commitments visible.

### BUSINESS RULE
- [N-U06-123] The job runs once a day under the system user and is active in the restored database.
- [N-U06-124] An order is eligible only if it is confirmed, has a vendor, is not acknowledged, has the reminder flag on, and does not consist solely of service products.
- [N-U06-125] A reminder is sent when the expected arrival date minus the configured number of days equals today; orders without an expected date are skipped.
- [N-U06-126] The reminder flag and days before receipt on an order default from the vendor's company-specific settings; the default is one day.
- [N-U06-127] The reminder email contains an acknowledgement link; opening it marks the order acknowledged and stops further reminders.
- [N-U06-128] When a vendor changes line dates in the portal, the buyer receives a warning activity listing old and new dates, and the lines are updated.
- [N-U06-129] A buyer can send a sample reminder to themselves, or send a reminder for a single order from the action menu.

### STATE
- NOT APPLICABLE — nothing identified for this section in the examined material.

### OPTIONALITY
- [N-U06-130] Reminders require the receipt reminder feature group, which internal users receive by default and which can be switched off in settings.

### DEPENDENCY
- [N-U06-131] Dates rely on the expected arrival computed from lead times; acknowledgement and date updates rely on the vendor portal access link.

### CONSTRAINT
- [N-U06-132] The reminder routine does nothing if the running user is not in the receipt reminder group.

### RISK
- [N-U06-133] The service-only exclusion compares a list of product types with a single-element list, so an order with two different service products may still be reminded (runtime check required).
- [N-U06-134] The date comparison uses the server's current date rather than the order's time zone, so reminders can be sent a day early or late for distant time zones.
- [N-U06-135] The vendor portal date update does not check order state or role beyond the link token.

### UNKNOWN
- [N-U06-136] Actual mail delivery, template rendering and mail server configuration cannot be confirmed without running the system.

## CAP-U06-08 Purchase agreements (blanket orders, templates, alternative quotations)

### WHAT
- [N-U06-137] A purchase agreement is either a blanket order (a time-bound price commitment with a vendor) or a purchase template (a reusable list of products); competing quotations from different vendors can be linked as alternatives and compared.

### WHY
- [N-U06-138] Blanket orders secure negotiated prices over a period; alternatives support competitive bidding between vendors.

### BUSINESS RULE
- [N-U06-139] Agreement states are draft, confirmed, closed and cancelled; cancelled agreements can be reset to draft.
- [N-U06-140] Confirming an agreement requires at least one product line; blanket orders also require every line to have a price and quantity above zero.
- [N-U06-141] Confirming a blanket order creates a vendor price record per line for that vendor, so the negotiated price is picked up on matching orders.
- [N-U06-142] Closing is refused while any linked quotation is in draft, sent or awaiting approval; closing removes the vendor price records created by the agreement.
- [N-U06-143] Cancelling an agreement removes its vendor price records and cancels draft quotations linked to it.
- [N-U06-144] Choosing an agreement on a quotation fills vendor, payment terms, fiscal position, company, currency, source and notes, sets the order date no earlier than the agreement start, and builds lines only while the quotation is draft; quantity is copied for templates and left zero for blanket orders.
- [N-U06-145] The ordered quantity on an agreement line sums quantities of confirmed orders linked to the agreement for the same product; it is informational and does not cap orders.
- [N-U06-146] Confirming a quotation that has open alternatives opens a decision step: keep the other quotations, or cancel them and confirm.
- [N-U06-147] Creating alternatives copies chosen products and quantities to quotations for selected vendors; comparison highlights the best price, best unit price and earliest date per product, and a button can clear quantities on the other lines.
- [N-U06-148] A blanket order's lines and price changes after confirmation keep the vendor price records in sync; a price of zero or below is refused.

### STATE
- [N-U06-149] Agreement: draft to confirmed by confirm; confirmed to closed by close; draft or confirmed to cancelled; cancelled to draft. Alternatives group: created when a quotation is linked to another and dissolved automatically when only one remains.

### OPTIONALITY
- [N-U06-150] Agreements and alternatives are optional features; agreements are installed by a setting, and alternatives additionally need their own feature group; purchase templates ignore dates and do not use a status bar.

### DEPENDENCY
- [N-U06-151] Agreements depend on vendor price records and order lines; with the inventory integration an agreement also carries a receipt type.

### CONSTRAINT
- [N-U06-152] The end date cannot precede the start date; type and company can change only in draft; only draft or cancelled agreements can be deleted.
- [N-U06-153] A new line on a confirmed blanket order must have a positive price.

### RISK
- [N-U06-154] No check was found that order quantities or dates stay within the agreement quantity and validity period (runtime check required).
- [N-U06-155] Any purchase user can confirm, close or cancel agreements; there is no separate approval for agreements.

### UNKNOWN
- [N-U06-156] Whether agreement vendor prices honour their date range during price selection beyond the standard vendor record dates was not traced separately.
- [N-U06-157] No agreements exist in the restored database; flows were not observed with data.

## CAP-U06-09 Roles and security

### WHAT
- [N-U06-158] Purchasing access is governed by two roles, user and administrator, plus accounting roles that can read or limited-edit orders and a portal role for vendors.

### WHY
- [N-U06-159] Separating routine buying from configuration and approval limits risk; portal access lets vendors see and act on their own orders only.

### BUSINESS RULE
- [N-U06-160] The purchase user role includes the base internal user role; the administrator role includes user, and the built-in system and administrator accounts are members.
- [N-U06-161] Users and administrators have full create, read, update and delete rights on orders and lines; accounting invoice users can read and update but not create or delete; read-only accounting users and portal vendors can only read.
- [N-U06-162] Order and line records are visible only for the user's allowed companies; portal vendors see only orders of their own commercial partner and its contacts, and may not create orders.
- [N-U06-163] Purchase users may work on vendor bills and bill lines of vendor types only, with administrators also able to delete bill lines.
- [N-U06-164] Only administrators can create, edit or delete vendor price records and see the purchase settings screen; the manager approve button and unlock button are administrator only.
- [N-U06-165] Agreements: users have full rights; the administrator row grants read only but is combined with the user role by inheritance.
- [N-U06-166] Optional feature roles exist for purchase warnings, receipt reminders and purchase alternatives.

### STATE
- NOT APPLICABLE — nothing identified for this section in the examined material.

### OPTIONALITY
- [N-U06-167] Warnings and alternatives are opt-in settings; receipt reminders are on by default for internal users.

### DEPENDENCY
- [N-U06-168] Order access relies on the accounting roles and portal role defined elsewhere; vendor portal links also work through an access token for unauthenticated visitors.

### CONSTRAINT
- [N-U06-169] The restored database contains the same counts of access rows and record rules as declared by the modules: thirty-five access rows and eight rules for purchasing, seven access rows and two rules for agreements, plus two additional agreement rows from the inventory integration for the stock administrator.

### RISK
- [N-U06-170] Approval and unlock restrictions rest on interface visibility rather than server checks, so effective control depends on controlling who has write access and who can call operations directly.
- [N-U06-171] Purchase users can create and delete vendor bills through their access to accounting records, which is broad for a buying role.

### UNKNOWN
- [N-U06-172] Effective permissions for specific users and custom roles were not examined; only declared configuration was counted.

## CAP-U06-10 Multi-company scope and failure behaviour

### WHAT
- [N-U06-173] Orders, lines and agreements belong to one company; related records (vendor, buyer, products, fiscal position, payment terms, receipt type) are checked or filtered against that company.

### WHY
- [N-U06-174] Companies in one database must not see or mix each other's purchasing data, taxes and numbering.

### BUSINESS RULE
- [N-U06-175] Visibility rules restrict orders, lines, reports and agreements to the user's allowed companies.
- [N-U06-176] Order numbering uses a single sequence shared by all companies, evaluated with the order's company context at creation.
- [N-U06-177] Vendor price records are filtered to the order company, even when the user's active company differs.
- [N-U06-178] Bills are generated in the order's company context and grouped per company.
- [N-U06-179] Agreements, their lines and the quotations built from them must be in the same company, and an agreement's company cannot change once confirmed.

### STATE
- NOT APPLICABLE — nothing identified for this section in the examined material.

### OPTIONALITY
- [N-U06-180] Multi-company behaviour is only relevant when more than one company exists; the restored database has one company.

### DEPENDENCY
- [N-U06-181] The receipt type on an order must belong to a warehouse of the order company, and recomputes when the company changes, through the inventory integration.

### CONSTRAINT
- [N-U06-182] An order whose lines hold products of a company outside its company tree is rejected with a validation message naming the products.
- [N-U06-183] The following user errors are raised: deleting an order that is not cancelled; confirming with missing products; cancelling locked or billed orders; changing a line type; deleting a confirmed line; merging fewer than two quotations or non-matching ones; creating bills for several vendors with an attachment; closing agreements with open quotations; confirming agreements without lines, prices or quantities; and changing an agreement's type or company after draft.

### RISK
- [N-U06-184] No inter-company order synchronisation exists in the purchasing or agreements modules; it must come from other modules.
- [N-U06-185] Several computations use the user's current company (approval threshold currency, price ranking) instead of the order's company, which matters only in multi-company runtime (runtime check required).

### UNKNOWN
- [N-U06-186] Multi-company paths could not be observed because the restored database has a single company and no transactions.
