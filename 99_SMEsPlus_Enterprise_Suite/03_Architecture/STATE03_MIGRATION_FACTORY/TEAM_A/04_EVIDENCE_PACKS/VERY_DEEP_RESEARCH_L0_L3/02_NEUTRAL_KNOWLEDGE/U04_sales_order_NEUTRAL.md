# U04 — Sales order — Neutral Knowledge (clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Source platform: Odoo 19 Community (named here once only)

Each statement is tagged with an identifier and is backed by one or more evidence claims in the restricted layer. Language is business and process language; no technical names are used.

## CAP-U04-01 Order state machine

### WHAT
- [N-U04-001] A sales document has four lifecycle states: quotation, quotation sent, confirmed sales order and cancelled. A separate lock indicator, independent of the state, marks a confirmed order as frozen against edits.
- [N-U04-002] The document is presented to users as a quotation in every state except confirmed, where it is presented as a sales order.

### WHY
- [N-U04-003] The state tells the business whether the document is a negotiable offer, a binding customer commitment or an abandoned offer, and it governs editing, invoicing, delivery and reporting behaviour.

### BUSINESS RULE
- [N-U04-004] A quotation becomes sent when a user explicitly marks it as sent, when it is emailed to the customer through the sending dialogue with the standard template, or when the customer starts an online payment that stays pending.
- [N-U04-005] Only a quotation or a sent quotation may be confirmed; confirmation moves the document to a confirmed sales order and stamps the confirmation moment as the order date.
- [N-U04-006] A quotation, a sent quotation or a confirmed order may be cancelled; the standard cancel action refuses to act on a locked order, so a locked order must be unlocked first.
- [N-U04-007] A cancelled document, and in code also a sent quotation, can be reset to a plain quotation; the reset removes any recorded customer signature.
- [N-U04-008] Only a plain quotation or a cancelled document may be deleted; sent or confirmed documents must be cancelled first.
- [N-U04-009] The pricelist of a confirmed order cannot be changed.
- [N-U04-010] Locking and unlocking are simple switches. The interface offers the lock action only when the lock feature is enabled and offers lock and unlock only to the sales administrator role; the underlying actions themselves perform no role check and no state check.
- [N-U04-011] Running any state action needs change access to the order; no separate approval role or amount threshold exists for state transitions.

### STATE
- [N-U04-012] State flow: quotation to sent; sent to confirmed; quotation, sent and confirmed each to cancelled; cancelled and sent back to quotation. There is no separate completed state; completion is represented only by the lock indicator.
- [N-U04-013] Leaving the confirmed state resets the order invoicing status to nothing-to-invoice and the line quantities to invoice to zero, and a cancelled order has no expected delivery date.
- [N-U04-014] State changes are tracked in the order chatter; the sent and confirmed changes use dedicated notification categories, and tracking of edits made on a quotation from the product catalogue is suppressed.

### OPTIONALITY
- [N-U04-015] Automatic locking after confirmation exists only when the lock feature is switched on; it is an installation-wide switch, not a per-company one.
- [N-U04-016] Quotation expiry does not change the state; an expired quotation merely cannot be signed or paid online.

### DEPENDENCY
- [N-U04-017] No scheduled job changes the document state; every transition comes from a user action, a customer action on the portal, or an incoming payment status.
- [N-U04-018] Other installed applications attach follow-up behaviour to confirmation and cancellation; they are listed in the confirmation and cancellation capabilities.

### CONSTRAINT
- [N-U04-019] A confirmed order must carry an order date; the database enforces this.

### RISK
- [N-U04-020] Mass cancellation and customer decline cancel orders without the lock check, so a locked order can be cancelled by those two routes.
- [N-U04-021] The state value is not guarded by business code against direct writes from integrations; only the interface marks it read-only.
- [N-U04-022] The lock action does not check the state, so a quotation or a cancelled order can be marked locked through an integration.

### UNKNOWN
- [N-U04-023] Whether a direct integration write of the state value is rejected at runtime by a generic access layer is not established by the source and needs runtime confirmation.
- [N-U04-024] Which individual users currently hold the roles needed to confirm or cancel was not inspected.

## CAP-U04-02 Quotation to sales order confirmation

### WHAT
- [N-U04-025] Confirming a quotation turns an offer into a binding sales order, sets the order date to the confirmation moment, and starts every follow-up process that the installed applications attach to confirmation.

### WHY
- [N-U04-026] Confirmation is the point at which fulfilment, invoicing preparation, projects and procurement begin, so its pre-checks protect downstream processes from incomplete orders.

### BUSINESS RULE
- [N-U04-027] Before confirming, every order line that is not a section, a note or a down payment must carry a product, and the analytic distribution rules of the lines still in quotation stage are validated.
- [N-U04-028] The order reference is allocated when the quotation is created, from a sequence that can be specific to the company, and is not renamed at confirmation; a quotation and its sales order share the same number.
- [N-U04-029] At confirmation the order date is overwritten with the current moment; the promised delivery date entered by the user and the quotation expiry date are not changed by confirmation.
- [N-U04-030] A confirmation email goes out only when the confirmation was triggered by the customer (signature or payment) or explicitly requested; a back-office confirmation sends nothing unless the quotation template defines a confirmation email.
- [N-U04-031] An online signature confirms the order immediately after a valid signature is recorded, unless an online payment is also required, in which case confirmation waits for the payment.
- [N-U04-032] A customer may sign only while the document is a quotation or sent quotation, is not expired, requires a signature and has none yet; a missing signature image is rejected, and the signed document is archived as a PDF attached to a chatter message.
- [N-U04-033] An online payment confirms the quotation only when exactly one quotation is linked to the transaction, no signature is still pending, and the paid amount reaches the required prepayment, which is a percentage of the order total.
- [N-U04-034] A customer-chosen payment amount below the required prepayment is refused for a document that is not yet confirmed.
- [N-U04-035] The sales applications contain no amount-based approval or double-validation step; the only blocks at confirmation are the state, a missing product, and checks added by extension applications. A credit limit overrun only shows a warning text.
- [N-U04-036] After all follow-up processes have run, the order is locked automatically when the lock feature is enabled.
- [N-U04-037] With the stock integration installed, confirmation launches procurement for lines selling goods, producing delivery orders or supply requests; later quantity changes on confirmed unlocked lines launch further procurement.
- [N-U04-038] With the project integration installed, confirmation creates the projects or tasks required by service products, unless task generation is disabled for that call.
- [N-U04-039] With the service-purchase integration installed, confirmation creates purchase orders for services bought in order to fulfil sold services.
- [N-U04-040] With the delivery integration installed and a pickup point chosen, confirmation creates or reuses a delivery address for that pickup point and sets it on the order.
- [N-U04-041] With the repair integration installed, confirmation creates repair orders for repair-service lines.
- [N-U04-042] With the event integration installed, confirmation requires every event line to be configured and then creates attendee registrations, opening the registration dialogue when a single order is confirmed; booth lines need pending booths and are then booked.
- [N-U04-043] With the loyalty integration installed, confirmation validates coupons and reward points (a negative balance blocks it), applies point changes, records loyalty history and sends reward coupon emails.
- [N-U04-044] With the pipeline integration installed, confirmation updates the revenue of the linked opportunity from the order.
- [N-U04-045] With the partnership integration installed, confirmation assigns the partner grade carried by the sold product to the customer commercial entity.
- [N-U04-046] With the print-on-demand connector installed, confirmation requires a complete shipping address and then creates the order at the external provider.
- [N-U04-047] With the relay-point delivery integration installed, confirmation is refused when the delivery method and the delivery address do not both belong to that network or both lie outside it.
- [N-U04-048] With quotation templates installed, a back-office confirmation sends the template confirmation email when the template defines one.

### STATE
- [N-U04-049] Confirmation moves a quotation or sent quotation to confirmed; the follow-up processes run while the order is already in the confirmed state and before the lock is applied.

### OPTIONALITY
- [N-U04-050] The requirements for online signature and online payment, and the prepayment percentage, default from company settings (signature on, payment off in the shipped defaults) and are copied onto each new order, where they can be changed individually; a quotation template can override them.
- [N-U04-051] Confirmation and payment emails are queued for asynchronous sending only when an installation parameter is on and the scheduled sending job is active; otherwise they are sent immediately.
- [N-U04-052] Which follow-up processes occur depends entirely on which integrations are installed; the core sales application alone confirms with no follow-up beyond the email and the lock.

### DEPENDENCY
- [N-U04-053] Payment-driven confirmation depends on the payment application post-processing a transaction and on an enabled payment provider.
- [N-U04-241] Invoice creation starts either from the create-invoice action on a confirmed order, which opens the invoicing dialogue, or from online payment post-processing; the content, grouping and posting of invoices belong to the invoicing unit and are not described here.
- [N-U04-242] Delivered quantities on lines are manual or analytic-based in the core sales application; the stock and project integrations replace this with delivery-based or timesheet-based figures, which belong to their own units.

### CONSTRAINT
- [N-U04-054] When online payment is required the prepayment percentage must be above zero and at most one hundred percent, on the order, the company and the quotation template alike.

### RISK
- [N-U04-055] Follow-up processes run inside the same operation as confirmation, so a failure in any integration (for example an unconfigured event line or an incomplete shipping address) aborts the whole confirmation.
- [N-U04-056] A customer confirms through a secret link without logging in, and the confirmation runs with elevated rights; link secrecy is the only protection.

### UNKNOWN
- [N-U04-057] The runtime interaction when several integrations each return a follow-up screen on one confirmation (loyalty reward notice, event registration dialogue) is not established.
- [N-U04-058] Whether the accounting application blocks confirmation for a partner over the credit limit beyond the warning text is not established by the sales source.

## CAP-U04-03 Cancellation and reset to draft

### WHAT
- [N-U04-059] Cancelling abandons a quotation or a confirmed order while keeping the record; resetting to quotation reopens a cancelled or sent document for editing.

### WHY
- [N-U04-060] Cancellation preserves the history while stopping further fulfilment and invoicing, and reset allows a corrected offer without recreating the document.

### BUSINESS RULE
- [N-U04-061] Cancelling an order also cancels its invoices that are still drafts; posted invoices are left unchanged and must be handled through the accounting process.
- [N-U04-062] No cancellation reason is requested and no cancellation dialogue exists for a single order; the interface shows only a confirmation prompt. The bulk cancel action shows an extra warning when confirmed orders are among the selection.
- [N-U04-063] A customer may decline a quotation online only while it still has to be signed and only by supplying a message; the order is then cancelled and the message is posted in its chatter, otherwise the customer is told the quotation cannot be rejected.
- [N-U04-064] Resetting to quotation reopens editing and removes the signature details; it does not reverse or recreate any follow-up document and does not change the lock indicator.
- [N-U04-065] A locked order must be unlocked by the sales administrator before it can be cancelled with the standard action; the bulk cancel action and the customer decline route do not enforce this.
- [N-U04-066] After cancellation the lines can no longer change product, quantities to invoice drop to zero and the invoicing status becomes nothing-to-invoice.
- [N-U04-067] With the stock integration installed, cancelling a confirmed order cancels its open delivery orders (completed deliveries stay) and logs a note about the decreased ordered quantity to the responsible people.
- [N-U04-068] With the service-purchase integration installed, cancelling an order leaves an activity on the purchase orders it generated without cancelling them.
- [N-U04-069] With the loyalty integration installed, cancelling a previously confirmed order deletes its loyalty history and reverses the point changes it had applied.
- [N-U04-070] With the repair integration installed, cancelling an order cancels the repair orders created from it.
- [N-U04-071] With the project integration installed, cancelling an order detaches projects from its sales lines.
- [N-U04-072] The standard cancel and reset actions add no explicit chatter message of their own; their trace is the tracked state change, while a customer decline additionally posts the customer message.

### STATE
- [N-U04-073] Cancelled is reachable from quotation, sent and confirmed; reset leads only back to quotation, from which normal confirmation is possible again.

### OPTIONALITY
- [N-U04-074] The follow-up reversals exist only for the integrations that are installed; the core sales application alone reverses nothing except draft invoices.

### DEPENDENCY
- [N-U04-075] Cancellation calls the invoice cancel routine for draft invoices; the accounting side then refreshes down-payment lines on orders that are not locked. Invoice handling is described in the invoicing unit.

### CONSTRAINT
- [N-U04-076] Bulk cancel is available to anyone who may change orders, and each user can see only the bulk-cancel dialogue records they created.

### RISK
- [N-U04-077] Bulk cancel and customer decline skip the lock check, so a locked and possibly delivered or invoiced order can be cancelled by them.
- [N-U04-078] Resetting a cancelled order and confirming it again launches follow-ups a second time while the earlier ones were only partly reversed, which can duplicate external documents such as purchases, projects or partner-side orders.
- [N-U04-079] Cancellation does not void or refund authorised or captured online payments; these need separate handling.
- [N-U04-080] The bulk-cancel warning tests for an obsolete completed state alongside confirmed; the obsolete value cannot occur, so the warning still works for confirmed orders.

### UNKNOWN
- [N-U04-081] Behaviour of cancellation for orders with posted invoices, partly delivered goods or captured online payments was not traced beyond the sales application and needs runtime or accounting review.

## CAP-U04-04 Pricing

### WHAT
- [N-U04-082] Each order line receives a unit price from the customer's pricelist, product taxes are mapped through the fiscal position, and an optional percentage discount can apply; the order carries its own currency and conversion rate.

### WHY
- [N-U04-083] Prices and tax treatment must be consistent and auditable per customer, currency and date, while sales staff may still override a price deliberately.

### BUSINESS RULE
- [N-U04-084] A quotation takes its pricelist from the customer's configured pricelist, or the default one, while it is still a quotation; the pricelist is not re-derived after the quotation stage.
- [N-U04-085] Changing the pricelist on a quotation affects only lines added afterwards; the user can request a full update that recomputes every priced line (not sections or notes), resets the discount to what the pricelist rules give and logs a note.
- [N-U04-086] The applicable pricelist rule is the first matching rule for the product, its variant or category, the quantity expressed in the product base unit, and the order date; the price is fixed, percentage-based or formula-based, the formula allowing rounding, a surcharge and minimum or maximum margins.
- [N-U04-087] A price edited manually on a line is kept when quantity or unit change later; a price is also never recomputed once anything has been invoiced on the line, nor for re-invoiced expense lines priced at cost, and global discount and down-payment lines keep their own prices.
- [N-U04-088] The order currency is the pricelist currency, falling back on the company currency; prices expressed in another currency are converted at the rate valid on the order date, and the order stores a conversion rate that is recomputed whenever the currency, the order date or the company changes.
- [N-U04-089] A line discount shown separately exists only when the discount feature is enabled; where a percentage pricelist rule applies, the discount is the difference between the base price and the pricelist price, and surcharges, which are negative discounts, are folded into the price instead of being shown.
- [N-U04-090] No upper limit on a line discount is enforced by the line itself; the order discount dialogue caps percentage discounts at one hundred percent but sets no limit on a fixed amount.
- [N-U04-091] The order discount dialogue can apply a percentage to all lines, add global discount lines for a percentage, or add fixed-amount discount lines; discount lines use a dedicated company discount product, created on first use when the user has the rights and otherwise refused with a message to ask an administrator.
- [N-U04-092] Line taxes come from the product's sales taxes of the order company mapped through the order fiscal position; combo lines carry no tax. The fiscal position follows the customer and delivery address, and a changed fiscal position only prompts the user to update taxes.
- [N-U04-093] A manual action recomputes taxes on all priced lines with the current fiscal position and logs a note on the order.
- [N-U04-094] Unit prices are adjusted so that a tax-inclusive product price stays consistent when the fiscal position replaces its included taxes with different ones.
- [N-U04-095] After confirmation the pricelist cannot be changed and the update-prices button is hidden, but prices, discounts and taxes of lines can still be edited until the order is locked; once a line has invoiced quantity the interface blocks editing its price and taxes, while the discount stays editable there.

### STATE
- [N-U04-096] On a locked order the product, description, unit price, unit, quantity, taxes, analytic distribution and discount of lines cannot be changed.

### OPTIONALITY
- [N-U04-097] The pricelist field is shown only when the pricelist feature is enabled and an active pricelist exists; with the feature off the order still carries a default pricelist silently.
- [N-U04-098] The line discount column and the order discount dialogue depend on the discount feature, which is meant to bring the pricelist feature with it.
- [N-U04-099] An installation parameter can disable automatic repricing when a customer changes optional-line quantities on the portal.

### DEPENDENCY
- [N-U04-100] Tax amounts, tax-included price conversion and tax rounding are computed by the accounting application; the sales application only supplies the line data and the fiscal position.
- [N-U04-101] Prices come from the product application's pricelist engine and product sales prices, including conversion between product currency and order currency.

### CONSTRAINT
- [N-U04-102] Prices, discounts and quantities follow configured decimal precisions; amounts are rounded by the tax engine according to the company rounding method.
- [N-U04-103] The pricelist of an order must be shared or belong to the order company.

### RISK
- [N-U04-104] Changing the quantity of a confirmed, unlocked, uninvoiced line may silently reprice it because the recomputation has no state condition.
- [N-U04-105] The update-prices and update-taxes actions have no state check in code; only button visibility restricts them to the quotation stage.
- [N-U04-106] The settings handler meant to switch on the pricelist feature together with discounts is declared as a dependency rather than as a change handler, so the pairing may not happen.

### UNKNOWN
- [N-U04-107] How tax mapping and tax-included price conversion behave for specific fiscal positions is defined in the accounting application and was not traced.
- [N-U04-108] Whether the order conversion rate recomputed at confirmation changes amounts already entered on lines or only reporting figures needs a multi-currency runtime test.

## CAP-U04-05 Order line rules

### WHAT
- [N-U04-109] An order line is a product line, a section, a subsection, a note or a combo line; product lines carry quantity, unit, price, taxes and discount, while sections, subsections and notes only structure and annotate the document. Down-payment, expense, delivery-charge, discount and reward lines are special product lines.

### WHY
- [N-U04-110] Line rules protect what was promised to the customer: once an order is confirmed, delivered or invoiced, lines may change only in controlled ways so that fulfilment and invoicing quantities stay traceable.

### BUSINESS RULE
- [N-U04-111] Sections, subsections and notes can never carry a product, price, quantity, unit or lead time; a line cannot change its type after creation, except that a subsection with no parent section turns into a section.
- [N-U04-112] The product of a line cannot be changed when the order is locked, the line is a down payment, the order is cancelled, or the confirmed line already has delivered or invoiced quantity; installed integrations add cases such as goods already moved, services already linked to projects and lines already bought from vendors.
- [N-U04-113] Changing the quantity of a confirmed line writes a chatter note with the old and new ordered quantity and the delivered and invoiced quantities.
- [N-U04-114] With the stock integration, the ordered quantity of a goods line cannot be decreased below what is already delivered; a return must be created instead.
- [N-U04-115] Once an order is confirmed its product lines cannot be deleted; the quantity must be set to zero so that invoicing and delivery stay traceable. Sections and notes can always be deleted, uninvoiced down-payment lines may be deleted, and delivery charge lines may be deleted when the delivery integration is installed.
- [N-U04-116] A locked order rejects changes to the product, description, unit price, unit, quantity, taxes, analytic distribution and discount of its lines; a down-payment line description may still be refreshed, and the delivery integration may allow a delivery line price update on a locked order.
- [N-U04-117] A confirmed but unlocked order can still receive quantity edits and new lines; each new product line added after confirmation is logged in the chatter, and the stock integration launches procurement for them.
- [N-U04-118] The unit of a line defaults to the product unit and is chosen among the product's allowed units; once the order is confirmed or cancelled the unit can no longer be edited in the interface, and a product whose unit differs from the used lines cannot have its unit changed.
- [N-U04-119] A combo line has a zero price and no tax of its own; the selected combo items become linked lines that copy its quantity and discount, and each item must belong to the combo choices and match its product.
- [N-U04-120] Down-payment lines are created by the invoicing process with zero quantity, are not copied when an order is duplicated, are exempt from the missing-product check, cannot change product or taxes, and follow special deletion and pricing rules handled in the invoicing unit.
- [N-U04-121] Discount lines use the company discount product and cannot be invoiced on their own; customers cannot edit them on the portal.
- [N-U04-122] Expense lines re-invoiced from vendor bills can be added only to a confirmed, unlocked, uncancelled order; they take their delivered quantity from analytic entries and keep their cost-based price.
- [N-U04-123] A warning text defined on a product or customer is shown on the order to users in the warning group.
- [N-U04-124] Every product on an order must belong to the order company or to a company it can access as a branch; archived products are flagged but may remain on existing orders; a product cannot be restricted to a company once it was sold from another company.

### STATE
- [N-U04-125] Line edit freedom decreases along the lifecycle: free on a quotation, restricted by delivered, invoiced and linked-document quantities after confirmation, and frozen when the order is locked or cancelled.

### OPTIONALITY
- [N-U04-126] Delivery, discount, loyalty, expense, project, purchase and stock integrations each add line types or rules; the core application itself knows product, section, subsection, note, combo, down-payment and expense lines.
- [N-U04-127] Quantities can also be edited from the product catalogue; on a quotation a zero quantity removes the line, on a confirmed order it only sets the quantity to zero.

### DEPENDENCY
- [N-U04-128] Down-payment lines depend on the invoicing process and on invoice posting, which refreshes their price, tax and description when the order is not locked; deleting a draft down-payment invoice removes its line.

### CONSTRAINT
- [N-U04-129] A product line needs a product and a unit unless it is a down payment; sections, subsections and notes must have no product, no unit, and zero price, quantity and lead time; the database enforces both rules.
- [N-U04-130] A combo item must be among the choices of its linked combo line and its product must equal the item product.
- [N-U04-131] Quantities use the configured unit-of-measure decimal precision, and the quantity field has no sign or limit restriction.

### RISK
- [N-U04-132] Only changes to existing lines are blocked on a locked order; adding a new line to a locked order is not blocked in code and is prevented only because the interface makes the lines read-only.
- [N-U04-133] No minimum, maximum or sign restriction on quantities exists in the sales application, so negative or zero quantities are accepted on product lines.

### UNKNOWN
- [N-U04-134] How the product and combo configurators and the portal optional-line editing behave beyond their entry points was not traced.

## CAP-U04-06 Order-level amounts and taxes

### WHAT
- [N-U04-135] The order total is computed from its priced lines as an untaxed amount, a tax amount and a total, with a detailed tax summary by tax group; further read-only figures show the amount invoiced, the amount still to invoice, the amount paid online and the amount before discount.

### WHY
- [N-U04-136] One consistent set of totals in the order currency is needed on the document, on the customer portal, for the prepayment test and for the hand-off to accounting.

### BUSINESS RULE
- [N-U04-137] Totals are computed by the shared tax engine from the priced lines only (sections and notes excluded); rounding follows the company rounding method and can be per line or global. Totals are stored and recomputed when line subtotals, currency, company or payment term change.
- [N-U04-138] When the payment term has an early-payment discount computed on the mixed basis, extra tax base lines for the discounted amount are included, so taxes are based on the discounted untaxed amount.
- [N-U04-139] Global discount lines and down-payment lines are treated as special lines in the tax computation, and the amount before discount excludes them.
- [N-U04-140] The un-invoiced balance of a line is its total per unit times the ordered quantity less the posted invoiced quantity; the order figure is the sum over lines. The invoiced amount sums posted invoice lines (credit notes counting negatively) converted at the invoice date.
- [N-U04-141] The amount paid is the sum of the authorised or done online transactions linked to the order; an order counts as paid when this reaches the order total.
- [N-U04-142] All order amounts are stored in the order currency; the stored order conversion rate converts to company currency, for example in the credit warning, and invoiced amounts convert at the invoice date.
- [N-U04-143] For credit control, the customer's amount to invoice sums the un-invoiced balance of confirmed orders converted to company currency, for the current company only and only when the company uses credit limits; the credit warning on a quotation adds the quotation total converted by the order rate.
- [N-U04-144] The tax summary shown on the portal and the printed report comes from a view that installed country packages may replace.

### STATE
- [N-U04-145] Totals are computed in every state; the un-invoiced balance figure carries no state condition, so it already shows the full amount on a quotation, whereas the untaxed amount to invoice is zero outside the confirmed state.

### OPTIONALITY
- [N-U04-146] Credit warnings and the credit amount to invoice appear only when the company uses credit limits.

### DEPENDENCY
- [N-U04-147] Tax detail, rounding and the tax summary come from the accounting application's tax engine; invoiced amounts and quantities come from the invoices described in the invoicing unit; the paid amount comes from the payment application's transactions.

### CONSTRAINT
- [N-U04-148] Order amount fields are read-only computed values; only the line data and header settings can be edited.
- [N-U04-149] Untaxed amount and total changes are tracked in the chatter.

### RISK
- [N-U04-150] Because the un-invoiced balance has no state condition, reports reading it without filtering on confirmed orders will overstate what is to be invoiced.

### UNKNOWN
- [N-U04-151] Rounding differences between order totals and later invoice totals under per-line versus global rounding were not tested.

## CAP-U04-07 Roles and record-level security

### WHAT
- [N-U04-152] Access to sales documents is controlled by three nested sales roles (own documents, all documents, administrator), by accounting roles with limited access to orders, by a portal role for customers, by five installation-wide feature switches, and by record rules that scope documents by company, salesperson and customer.

### WHY
- [N-U04-153] Sales staff should see their own pipeline by default, managers see everything, customers see only their own documents, and every user sees only the companies they work in.

### BUSINESS RULE
- [N-U04-154] The own-documents role includes the basic internal user role; the all-documents role includes the own-documents role; the administrator role includes the all-documents role and canned-response administration. In the restored data the two administrative users hold the administrator role.
- [N-U04-155] A salesperson with only the own-documents role sees orders, order lines and sales analysis rows on which they are the salesperson or on which no salesperson is set; the all-documents role removes that restriction.
- [N-U04-156] Orders, lines and analysis rows are restricted to the user's allowed companies for every user; sales teams, quotation templates and quotation headers or footers are restricted to the allowed companies but may be shared across companies.
- [N-U04-157] Table-level access: salespeople may read, change and create orders and may also delete order lines, but may not delete orders; the administrator may do everything; accounting read-only users may read; invoicing and accountant users may read and change orders; portal users may read only.
- [N-U04-158] Pricelists are readable by salespeople and fully managed by the administrator; quotation templates and sales teams follow the same pattern; quotation headers and footers are readable by all internal users and managed by the administrator; team membership data is readable by internal users and managed by the administrator.
- [N-U04-159] A portal customer lists sent quotations and confirmed orders belonging to their company tree; an order page can also be opened without logging in using the document secret token, and signing, declining, paying and editing optional lines then run with elevated rights after the token or access check.
- [N-U04-160] The secret token is generated on demand when a link is shared and is then reused; anyone holding it can open the document, sign, decline or pay.
- [N-U04-161] The lock, discount, warning, pro-forma and quotation-template features are installation-wide switches implemented as groups implied by the basic internal user role; they are not per user or per company.
- [N-U04-162] Payment transaction data on the order is visible only to invoicing roles, tags only to salespeople, and margin figures to all internal users.
- [N-U04-163] A salesperson can be assigned only among internal users of the order company who hold a sales role.
- [N-U04-164] The invoice-creation and bulk-cancel dialogues expose only the records created by the current user.
- [N-U04-165] Salespeople are given wider visibility of invoices, invoice lines, payment transactions and payment tokens so that they can follow documents linked to their orders; the all-documents role removes the own-invoice restriction.
- [N-U04-243] A user sees a record only when it satisfies every rule that applies to everybody (such as the company restriction) and at least one of the rules attached to the roles the user holds; role rules therefore widen visibility only inside the company restriction.

### STATE
- [N-U04-166] Role permissions on orders do not vary by order state in the access tables or rules; state-dependent restrictions are implemented in business actions and in the interface.

### OPTIONALITY
- [N-U04-167] The feature switches are off until enabled in settings; in the restored installation all five are on, implied by the basic internal user role.

### DEPENDENCY
- [N-U04-168] Portal access relies on the portal application; payment and invoice visibility rules rely on the payment and accounting applications; the stock and project integrations add their own read rules on order lines.

### CONSTRAINT
- [N-U04-169] Counts in the restored data match the declared access rows and rules: the sales application declares 39 access rows, 27 rules and 4 groups, quotation management 5, 1 and 1, the PDF builder 4, 1 and none, sales teams 9, 2 and 3.

### RISK
- [N-U04-170] The portal personal-document rule grants write and delete permission on the order record; in practice this is limited because the portal role has read-only table access and portal actions run in elevated mode.
- [N-U04-171] Role checks for locking, unlocking and feature-dependent actions exist only in the interface; any user who can change orders can call the underlying actions through an integration.
- [N-U04-172] Document access by secret token is not tied to a customer identity, so a forwarded link grants the same rights as the customer has.

### UNKNOWN
- [N-U04-173] Effective membership of individual users in the sales roles beyond the two administrators was not inspected, and how multi-company users see mixed-company orders needs a runtime test.

## CAP-U04-08 Scheduled and automated behaviour

### WHAT
- [N-U04-174] The sales applications seed two scheduled jobs, both inactive by default: one sends queued order status emails and one sends ready invoices after online payment. The PDF quote builder seeds a third, once-only repair job. Other automated behaviours are an upsell reminder activity, a quotation-viewed note and a digest figure.

### WHY
- [N-U04-175] Deferring emails keeps customer-facing actions fast and gives retry and batching, while automatic invoicing removes manual steps for prepaid orders.

### BUSINESS RULE
- [N-U04-176] Order confirmation and payment emails are queued, and sent by the job, only when the asynchronous email parameter is on and the job is active; otherwise they are sent at once. After queuing, the job is triggered immediately; the job clears the queue marker after each send and stops when its time budget is used.
- [N-U04-177] Turning the asynchronous-email parameter or the automatic-invoice parameter on or off activates or deactivates the linked job automatically; deleting a parameter deactivates its job; module installation re-synchronises both jobs from the current parameter values.
- [N-U04-178] When automatic invoicing is on, a done online payment creates a final invoice for fully paid confirmed orders, or a down-payment invoice for partly paid ones; the sending job emails posted invoices that were not ready at posting time, looking back two days. The setting is forced off when the default invoicing policy is not ordered quantities.
- [N-U04-179] No scheduled job expires quotations or sends reminders for them; expiry is evaluated only when it is read, for example when a customer tries to sign or pay.
- [N-U04-180] When an order's invoicing status turns to upselling opportunity, a to-do activity is scheduled for the order salesperson or the customer's salesperson, replacing earlier to-do activities, unless activity automation is suppressed.
- [N-U04-181] The first view of a quotation by a logged-out or portal customer each day posts an internal chatter note; link previews are excluded.
- [N-U04-182] With quotation management installed, a digest figure for confirmed sales is available to users with the all-documents role.
- [N-U04-183] The PDF quote builder seeds a job with a far-future interval that assigns form fields to headers, footers and product documents after an upgrade; it is active.
- [N-U04-184] The sales applications seed no automation rules; the restored installation holds none.

### STATE
- [N-U04-185] In the restored installation both seeded sales jobs are inactive, the asynchronous-email parameter is off and the automatic-invoice parameter does not exist.

### OPTIONALITY
- [N-U04-186] Activation needs the matching configuration parameter to be switched on, available through settings for automatic invoicing and through system parameters for asynchronous emails; each job's default interval is daily.

### DEPENDENCY
- [N-U04-187] Invoice sending relies on the accounting application's invoice sending service and on the default invoice email template parameter; order emails rely on the mail templates for quotation, confirmation and payment.

### CONSTRAINT
- [N-U04-188] The invoice-sending job considers only done transactions that were post-processed, have a posted unsent invoice and a confirmed order, and changed state within the last two days.

### RISK
- [N-U04-189] If the job is deactivated by hand while the asynchronous parameter stays on, emails are simply sent immediately, and orders queued before the deactivation stay marked until the job next runs.

### UNKNOWN
- [N-U04-190] Runtime timing of triggered job runs and failure handling in the outgoing mail gateway were not tested.

## CAP-U04-09 Quotation templates and options, margin, PDF quote builder, sales teams

### WHAT
- [N-U04-191] Four optional capabilities extend quotations: reusable quotation templates with optional lines, margin tracking, a PDF quote builder that merges header, product and footer documents into the quotation PDF, and sales teams that group salespeople and receive orders.

### WHY
- [N-U04-192] Templates speed up quotation creation and standardise terms, margin shows profitability, the PDF builder produces polished customer documents, and teams route and report sales.

### BUSINESS RULE
- [N-U04-193] Choosing a template on a quotation replaces all existing lines with the template lines (sections, notes, products with quantity and unit) and positions the first line so that later reordering keeps pages together; this is a form action, and the template field is read-only on confirmed or cancelled orders.
- [N-U04-194] A template can supply terms and conditions, signature and payment requirements, prepayment percentage, validity duration, an invoicing journal and a confirmation email; where set they override company defaults on the order.
- [N-U04-195] A company can name a default template that new quotations pick up automatically, except orders created through the online shop; archiving a template removes it as company default, and switching the template feature off clears every company default.
- [N-U04-196] Sections can be flagged optional; products inside an optional section appear on the customer portal as options that the customer can add, change or remove while the quotation is open; combo lines and discount lines are not customer-editable.
- [N-U04-197] A template shared across companies cannot contain products restricted to one company, and a company-restricted template cannot contain products of inaccessible companies; template lines cannot be combo or non-saleable products and cannot change type after creation.
- [N-U04-198] The margin of a line is its untaxed subtotal minus unit cost times ordered quantity, or minus cost times delivered quantity when a line was added from a delivery with no ordered quantity; the cost is the product cost converted to the line unit and order currency, is editable on the line, and the order margin is the sum of line margins with a percentage over the untaxed total.
- [N-U04-199] With the stock margin integration installed, the cost of lines with delivered goods and a non-standard cost method is taken from the valuation of the deliveries, mixed with the standard cost for the undelivered part.
- [N-U04-200] Margin is also available in sales analysis, converted to the reporting currency.
- [N-U04-201] When the PDF quote builder is installed, the quotation PDF is assembled from selected header documents, product documents marked inside the quote, the quotation pages and selected footer documents, in that order; form fields in those PDFs are filled from order data or from values typed in by the salesperson.
- [N-U04-202] The merged PDF is produced for quotations and sent quotations; for confirmed orders it is produced only when an installation parameter forces inclusion.
- [N-U04-203] Only unencrypted PDF files can serve as headers, footers or inside-quote product documents; headers and footers can be tied to specific quotation templates and can be added by default.
- [N-U04-204] Product documents can also be attached to the quotation or to the confirmed order for customer download on the portal; a customer can download only documents attached to their own order.
- [N-U04-205] A sales team has a leader, members, an optional company and a colour; a salesperson normally belongs to one team, because creating or reactivating a membership archives the others unless multiple memberships are enabled by a parameter.
- [N-U04-206] A new order takes its salesperson from the customer's salesperson, then the customer entity's salesperson, then the current user if that user is a salesperson; its team is then chosen from the teams the salesperson belongs to or leads in the order company, else the default in context, else any team of the company.
- [N-U04-207] A team with five or more active orders cannot be deleted and should be archived instead; the default website and point-of-sale teams cannot be deleted at all.
- [N-U04-208] A team shows the current month's invoiced revenue from paid or in-payment posted invoices, an invoicing target, and the count of its non-cancelled orders.

### STATE
- [N-U04-209] Template application, team assignment and PDF assembly all operate at the quotation stage; the template field cannot be changed once the order is confirmed or cancelled, and the PDF builder skips confirmed orders unless forced.

### OPTIONALITY
- [N-U04-210] Templates need the template feature switch, which is on in the restored installation, and no template exists yet.
- [N-U04-211] Margin is active whenever its application is installed and has no separate switch; no order exists yet.
- [N-U04-212] The PDF quote builder installs automatically with quotation management and has an effect only when headers, footers or inside-quote product documents exist; none exist yet.
- [N-U04-213] Sales teams exist from installation: one active shared team and two archived ones (online shop and point of sale); the multiple-membership parameter is absent.

### DEPENDENCY
- [N-U04-214] Margin depends on product cost from the product application and on stock, project, expense and manufacturing integrations for delivered cost; the PDF builder depends on quotation management and the report engine; team revenue depends on invoices from the accounting application.

### CONSTRAINT
- [N-U04-215] Quotation headers and footers and inside-quote product documents must be PDF files and not encrypted, and inside-quote product documents must be files rather than links.
- [N-U04-216] PDF form field names must follow a naming pattern and mapped data paths must exist on the order or line.
- [N-U04-217] Team members must be internal users of the team company; one active membership per user and team; only internal users can lead a team.

### RISK
- [N-U04-218] Line cost is captured when the line is created or when product, unit, company or currency change; later product cost changes do not update the margin of existing lines.
- [N-U04-219] Applying a template removes all existing lines of the quotation without a further warning in code.
- [N-U04-220] A PDF whose form fields cannot be mapped may produce blank values in the customer document, and a broken PDF is rejected only at upload.

### UNKNOWN
- [N-U04-221] The visual result of merged PDFs and field filling for unusual PDF form structures was not tested.

## CAP-U04-10 Multi-company and data-scope specifics of orders

### WHAT
- [N-U04-222] Every order and order line belongs to a company, while teams, quotation templates and quotation documents may be shared, and consistency checks keep partners, products, pricelists, fiscal positions, journals and teams in line with the order company.

### WHY
- [N-U04-223] In a multi-company installation documents must not leak between companies and master data of different companies must not be mixed on one document.

### BUSINESS RULE
- [N-U04-224] The order company defaults to the user's current company and cannot be empty; changing the company of a quotation with lines warns that lines and prices may need manual correction, and the quotation template is re-derived only for unsaved orders.
- [N-U04-225] Order lines carry the company of their order, and a line product must belong to the order company or to a company that treats it as an accessible branch.
- [N-U04-226] Customer, invoice and delivery addresses, fiscal position, journal, product, team and pricelist are checked for consistency with the order company when saved; pricelist, payment term and team may also be shared across companies.
- [N-U04-227] The order number comes from a sequence that can be defined per company; the shipped sequence has no company and is therefore shared by all companies.
- [N-U04-228] Signature, payment, prepayment and validity defaults, the discount product and the down-payment account are company settings; payment terms, terms and conditions, preferred payment method and pricelist of a new order are resolved in the order's company.
- [N-U04-229] Default salesperson and team choices are limited to teams of the order company or shared teams, and to users who belong to that company.
- [N-U04-230] A customer's credit exposure counts only orders of the current company.
- [N-U04-231] A product cannot be restricted to a company after it has been sold from a company outside that company's branch tree.
- [N-U04-232] A portal customer can pay an order only when the customer's partner may pay in the order's company; otherwise a company mismatch message is shown.
- [N-U04-233] With the stock integration, the warehouse of an order must belong to the order company, and a confirmed order with goods must have a warehouse when the company has warehouses.
- [N-U04-234] Orders, lines and analysis rows are visible only for the user's allowed companies through a rule that applies to every user, without exception for sales administrators.

### STATE
- No statement for this section.

### OPTIONALITY
- [N-U04-235] The restored installation has a single company, so none of the cross-company behaviours is exercised; the company field appears in the order form only for multi-company users.

### DEPENDENCY
- [N-U04-236] Visibility depends on the allowed companies selected in the user session, and branch relations come from the company hierarchy.

### CONSTRAINT
- [N-U04-237] A line product from an inaccessible company, a team outside the order company and a stock warehouse of another company are each rejected when the order is saved.

### RISK
- [N-U04-238] The salesperson is restricted to company users only by a selection filter and has no consistency check at save time, so an existing assignment is not re-validated if the user later leaves the company.
- [N-U04-239] A single shared sequence produces one global numbering; separate numbering per company requires company-specific sequences to be created.

### UNKNOWN
- [N-U04-240] Behaviour when orders of different companies are confirmed or cancelled together, and whether the company of a confirmed order can be changed in the interface, was not established.

