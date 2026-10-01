# C01 - Order-to-cash chain - Neutral Knowledge

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source family: Odoo 19 Community. Date: 2026-10-02.
> Plain business and process statements only. Each statement carries an identifier that links to the restricted evidence layer.
> This unit studies how the order, delivery, invoice, payment, return, cancellation and valuation documents work together; no coverage, level, gate or approval claim is made.

## CAP-C01-01 Happy path end-to-end (quotation to paid invoice)

### WHAT

- [N-C01-001] An order can be confirmed from the internal confirm action or from the customer portal after signature or payment; every path ends in the same confirmation routine, which then launches the follow-up documents.
- [N-C01-002] Confirming an order of goods asks the warehouse process to plan supply for every goods line in one run; if no supply rule exists for a line, the whole confirmation fails and nothing is saved.
- [N-C01-003] Delivery movements are created with system rights regardless of the confirming user, are confirmed at once, and the resulting delivery transfers are confirmed so that the scheduler can react.
- [N-C01-004] Validating a delivery turns planned movements into completed ones: the system checks the transfer, asks the backorder question for shortfalls, processes each line, records the completion date and then informs the order and the valuation process.
- [N-C01-005] Validation removes the goods from warehouse stock and books them at the customer location, so stock on hand falls at validation and not at confirmation.
- [N-C01-006] The create-invoice action of an order produces a regular invoice for everything billable; invoices made from the user interface are always final, so earlier down payments are deducted and a negative balance becomes a credit note.
- [N-C01-007] Posting an invoice is a deliberate, separate action: the system validates the document, moves its accounting date out of locked periods, creates analytic entries, records the posted state and raises the customer activity counter.
- [N-C01-008] Registering a payment creates the payment, posts it and reconciles it with the open item, in that order, and links the payment to the invoice.
- [N-C01-009] A confirmed payment creates its own posted journal entry that holds the money on an intermediate outstanding account until it is matched to the bank.
- [N-C01-010] An invoice becomes paid as soon as its open amount reaches zero through a payment, a bank line or another settlement; the separate in-payment status cannot occur in this edition.

### WHY

- [N-C01-011] The chain separates commitment, physical fulfilment, billing, ledger recognition and settlement, so that each step can be controlled, audited and assigned to a different role.

### BUSINESS RULE

- [N-C01-012] The order receives its reference when it is created as a quotation and keeps it; a delivery transfer is numbered when it is generated; an invoice, credit note or payment entry is numbered only when posted, so unposted invoices have no number.
- [N-C01-013] An order is a quotation, a sent quotation, a sales order or cancelled; there is no completed status.
- [N-C01-014] Only quotations and sent quotations can be confirmed, and every product line must have a product; confirming an already confirmed order is refused.
- [N-C01-015] Confirmation sets the order status to sales order and overwrites the order date with the confirmation moment.
- [N-C01-016] Only goods lines of a confirmed, unlocked order generate delivery work; service lines never do.
- [N-C01-017] The quantity sent to the warehouse is the ordered quantity minus what is already covered by non-cancelled outgoing movements, net of counted returns.
- [N-C01-018] Related delivery documents are grouped under a stock reference record created from the order, which replaces the older procurement group concept.
- [N-C01-019] When the operation type reserves at confirmation, goods are reserved while the order is being confirmed, so a delivery is ready immediately if stock is available.
- [N-C01-020] Delivered quantity of a goods line is the sum of completed outgoing movements minus counted returns; movements not yet completed count for nothing.
- [N-C01-021] The quantity billable on a confirmed line is ordered minus invoiced for ordered-basis products and delivered minus invoiced for all others.
- [N-C01-022] A new invoice takes customer, delivery address, fiscal position, payment term, salesperson, sales team, company, currency and reference from the order, and uses a specific journal only if the order names one.
- [N-C01-023] Lines with positive billable quantity are invoiced, negative ones only in a final run; sections appear only when a line beneath them is billed, and down payment deductions come last.
- [N-C01-024] Each invoice line carries a link to its order line; this link is the only connection between billing and ordering and is what makes progressive billing possible.
- [N-C01-025] A draft invoice already counts as invoiced quantity, so an order line shows as billed when the draft is created and not when it is posted.
- [N-C01-026] Each created invoice carries a note naming the order it came from.
- [N-C01-027] If the invoice date falls inside a locked period, posting moves the accounting date to the first open date instead of refusing.
- [N-C01-028] When an invoice is posted, payments that came from the customer online transactions on the same order are matched with it automatically.
- [N-C01-029] Every delivered movement gets a stored cost value at validation, whatever the valuation mode.
- [N-C01-030] With the default setup a customer delivery creates no journal entry; one arises only for perpetual products moving to or from a location that has a valuation account.
- [N-C01-031] Cost of goods sold is not posted at delivery: with perpetual valuation it is added to the customer invoice when that invoice is posted, and with periodic valuation it is posted by the period closing entry.
- [N-C01-032] Payments can be registered only on posted invoices, never on miscellaneous entries and never on invoices blocked for payment.
- [N-C01-033] A payment smaller than the open amount leaves the invoice partly paid by default; marking a difference as fully paid needs a chosen difference account, except for early-payment discounts where full payment is the default.
- [N-C01-034] A posted payment is in process, or paid at once when its outstanding account is of cash type; it becomes paid when its invoices are all paid, even without bank matching.
- [N-C01-035] When an invoice becomes paid, the related order receives a note saying so; the order itself does not change status.
- [N-C01-036] The order has no paid status: its paid amount counts online payment transactions only, so payments registered on invoices never alter the order.

### STATE

- [N-C01-037] A delivery transfer is draft, waiting, ready, done or cancelled; its status is derived from its movements and is never edited directly.
- [N-C01-038] An order line is to invoice while anything is billable, upselling when an ordered-basis line was over-delivered, invoiced when billed quantity has reached ordered quantity, and otherwise nothing to invoice.
- [N-C01-039] The order shows to invoice if any counted line is to invoice, invoiced if all are, upselling if all are invoiced or upselling, and otherwise nothing to invoice; outside the sales order status it is always nothing to invoice.
- [N-C01-040] The order delivery status is absent without transfers, otherwise not delivered, started, partially delivered or fully delivered, derived from its transfers and delivered quantities; the effective date is the earliest completion of a delivery to a customer.
- [N-C01-041] Locking is a separate flag on the order and not a status; it is on or off independently of confirmation.

### OPTIONALITY

- [N-C01-042] Sending the quotation is optional because confirmation accepts both draft and sent quotations.
- [N-C01-043] The confirmation e-mail is sent only when confirmation comes from the portal or from a payment; the internal confirm button does not send it.
- [N-C01-044] A product is valued periodically or perpetually according to its category setting or else the company setting.
- [N-C01-045] In the studied configuration every operation type reserves at confirmation and asks about backorders, and delivery runs in one step from Stock to Customers.
- [N-C01-046] In the studied configuration valuation is periodic with manual closing period, cost method is standard, the accounting-style flag is off and no stock journal is set on the company.
- [N-C01-047] With periodic valuation the stock account is reconciled to stock value by a closing entry, triggered manually or by the daily job, which processes only companies set to daily or monthly closing.
- [N-C01-048] With perpetual valuation the customer invoice also carries cost lines that credit the stock account and debit expense for the cost not yet booked. Runtime proof is required.
- [N-C01-049] With perpetual valuation a stock journal entry is created at validation when a valued movement touches a location with a valuation account. Runtime proof is required.

### DEPENDENCY

- [N-C01-050] Locking, when the company feature is on, happens after all follow-up documents are launched, so confirmation still creates delivery work for the locked order.
- [N-C01-051] Invoice creation from an order runs with system rights so that salespeople without billing rights can generate draft invoices; a user with neither right gets an empty result without error.
- [N-C01-052] Only users with invoicing rights can post an invoice; the sales user role alone does not include them.

### CONSTRAINT

- [N-C01-053] If nothing is billable the invoice action stops with an explanatory message about the product invoicing policy.

### RISK

- [N-C01-054] Validation does not appear to stop when stock is insufficient, so stock can go negative; runtime proof is required.
- [N-C01-055] Several follow-up modules act on confirmation; whether stock, project or purchase work is launched first depends on module load order and cannot be read from the rules, so interdependent effects need runtime proof.

### UNKNOWN

- [N-C01-056] How the perpetual path behaves end to end with partial deliveries, returns and several invoices is unconfirmed without running the system; the studied database uses the periodic path and holds no transactions.

## CAP-C01-02 Invoicing-policy variants (ordered vs delivered)

### WHAT

- [N-C01-057] Each sellable product declares whether the customer is billed for the quantity ordered or for the quantity delivered; changes of the setting are tracked in the product history.
- [N-C01-058] Services pick one of four billing styles - prepaid fixed price, delivered quantity entered by hand, delivered by milestones, delivered by timesheets - which map onto the two basic bases; without the warehouse or timesheet modules the delivered quantity of a line is entered by hand or derived from expense records.

### WHY

- [N-C01-059] Businesses shipping goods usually want to bill what left the warehouse, while businesses selling prepaid items or services want to bill at the sale; one product setting serves both.

### BUSINESS RULE

- [N-C01-060] Quotations, cancelled orders and display lines have no billable quantity.
- [N-C01-061] On an ordered-basis goods line the billable quantity exists from confirmation, so the invoice may be issued before the goods ship; nothing in the system forbids it.
- [N-C01-062] On a delivered-basis goods line nothing is billable until a completed outgoing movement counts as delivered; before that the invoice action reports nothing to invoice.
- [N-C01-063] Negative billable quantities appear on an invoice only in a final run, where they produce a credit note.
- [N-C01-064] When the only billable lines are ones that cannot be invoiced alone, such as discount or delivery-cost lines, the order shows nothing to invoice.
- [N-C01-065] With automatic invoicing on, an order paid in full online is invoiced for its ordered quantities whatever each product policy says, and a partial payment produces a down payment invoice; saving a default policy other than ordered switches automatic invoicing off.

### STATE

- [N-C01-066] An ordered-basis line shows as upselling opportunity when nothing is left to bill and more was delivered than ordered.
- [N-C01-067] A line shows invoiced once billed quantity has reached ordered quantity and nothing remains billable; otherwise it shows nothing to invoice.
- [N-C01-068] A delivered-basis goods line whose movements are all finished or cancelled, with some quantity delivered and nothing left to bill, shows as invoiced even if less than the ordered quantity was delivered; this supports goods sold by weight and also covers a declined backorder.
- [N-C01-069] A down payment line shows invoiced when nothing remains to bill on it, and the order status ignores down payment and display lines.

### OPTIONALITY

- [N-C01-070] For goods the billing basis is ordered by default and is reset to ordered whenever the product type is recalculated; the user may switch a product to delivered afterwards.
- [N-C01-071] A default billing basis for new products can be set in the sales settings; it is a stored default and not a per-company product value.
- [N-C01-072] In the studied database no default is stored and all 16 products are services, thirteen billed on ordered and three on delivered quantity; no goods product exists, so the goods variants are unobserved.

### DEPENDENCY

- [N-C01-073] Billing shipment by shipment emerges from cumulative quantities on the order line and not from a link between invoice and delivery; it depends on the warehouse module to supply delivered quantity.

### CONSTRAINT

- [N-C01-074] When nothing is billable the system stops with a message telling the user to deliver first or to switch the product to ordered quantities for goods or prepaid fixed price for services.

### RISK

- [N-C01-075] The billing basis is read live from the product whenever billable quantity is recomputed, so changing it on a product with partly billed orders can change the next invoice without any change on the order.
- [N-C01-076] Three different amounts of what remains to bill coexist - billable quantity by policy counting drafts, amount by policy counting posted documents only, and amount by ordered quantity counting posted documents only - and can disagree while drafts exist.
- [N-C01-077] The short-delivery rule still lists an obsolete product type value; it has no effect today but signals leftover vocabulary.

### UNKNOWN

- [N-C01-078] How the product form shows or locks the billing basis for each product type at runtime, and the effective default seen by a new product, are unconfirmed without running the system.

## CAP-C01-03 Return and credit-note chain

### WHAT

- [N-C01-079] A return is a new transfer made from a completed delivery: locations are reversed, the original and the order line are linked, open downstream movements are released, and the return is confirmed and reserved; quantities start at zero and the user chooses them.
- [N-C01-080] A return can be combined with an exchange that creates the replacement supply at once.
- [N-C01-081] Return before invoice: on delivered basis the delivered quantity falls and the invoice, when issued, covers only what stayed delivered; on ordered basis the returned goods stay billable until the order or invoice is corrected separately.
- [N-C01-082] Return after invoice on delivered basis: delivered minus invoiced turns negative, the line shows to invoice, and the next final invoice carries the negative quantity; because an invoice with a negative total cannot be posted, it is switched to a credit note before posting.

### WHY

- [N-C01-083] Completed deliveries are never rewritten; goods come back through a return transfer and money through a credit note, and the two legs are independent and handled by different roles.

### BUSINESS RULE

- [N-C01-084] Each returned line carries an update-quantities flag, on by default, that decides whether the delivered quantity of the order falls.
- [N-C01-085] Completed return movements flagged to update quantities reduce the delivered quantity of the order line; unlinked non-return receipts such as dropship receipts are ignored.
- [N-C01-086] A return with the flag cleared moves stock back but leaves delivered quantity, billable quantity and invoice status unchanged.
- [N-C01-087] A credit note linked to order lines lowers invoiced quantity at once, even as a draft, so the line returns to to invoice and could be re-invoiced by mistake; a credit note without a stock return changes accounting and invoiced quantity only.
- [N-C01-088] A credit note created by the reversal action keeps the links to the order lines, so it reduces invoiced quantity like a credit note generated from the order.
- [N-C01-089] A credit note generated from the order is not linked to its original invoice in this edition, because the origin link is set only when a localisation demands it.
- [N-C01-090] With perpetual valuation a credit note reverses cost of goods sold at the unit cost of the original invoice for standard or average cost products, finding the original through order-line links when no reversal link exists; a reversal posted with the cancel option negates the original lines instead. Runtime proof is required.
- [N-C01-091] A customer return is valued as an incoming movement at the value of the original outgoing movement.
- [N-C01-092] Credit notes are numbered from a separate sequence on sale and purchase journals; the studied sales journal has it enabled.

### STATE

- [N-C01-093] Posting a credit note linked to a posted invoice reconciles the two; the invoice shows reversed when only credit notes or entries settle it and paid if a payment also contributed.

### OPTIONALITY

- [N-C01-094] In the studied database the delivery operation type names Receipts as its return type, so a delivery return is created as an incoming-type transfer from Customers to Stock.

### DEPENDENCY

- [N-C01-095] The return keeps the order line and the order so that it appears on the order and can affect its quantities; this needs the sales-stock module.
- [N-C01-096] A return follows the backorder policy of its own operation type, because the helper meant to ignore the policy for returns has no caller.

### CONSTRAINT

- [N-C01-097] By the base rule only completed transfers can be returned.

### RISK

- [N-C01-098] When the sales-stock module is installed, a transfer linked to an order can enter the return step in any state, contradicting the completed-only rule; the effect of returning an unfinished transfer is unconfirmed.
- [N-C01-099] A code comment says only credit notes generated from the order change invoiced quantity, but credit notes made by reversal do too; behaviour follows the code.

### UNKNOWN

- [N-C01-100] The maximum returnable quantity, the effect of returning unfinished transfers and the combined stock, billing and valuation arithmetic of partial returns are unconfirmed without running the system.

## CAP-C01-04 Cancellation chain

### WHAT

- [N-C01-101] Cancelling an order cancels its draft invoices and marks the order cancelled; posted invoices, payments and completed deliveries are left untouched.
- [N-C01-102] Cancelling a confirmed order also cancels its unfinished delivery transfers, releases reservations, propagates cancellation to chained movements and logs the withdrawn quantity; completed transfers stay, and the cancelled order keeps its delivered record.
- [N-C01-103] Cancelling a posted invoice first resets it to draft, so the reset guards apply: no cancellation request pending, no exchange or cash-basis entry, no hash and no locked period.
- [N-C01-104] Cancelling a payment cancels or deletes its entry and recomputes the payment state of the invoices it settled; deleting a payment resets and deletes its entry.

### WHY

- [N-C01-105] Cancelled and posted documents are kept for history; open work is withdrawn, while completed deliveries and posted invoices are corrected by returns and credit notes.

### BUSINESS RULE

- [N-C01-106] The cancel button refuses a locked order but accepts quotations, sent quotations and confirmed orders alike; no status check exists.
- [N-C01-107] Orders can be deleted only as draft or cancelled; lines of a confirmed order cannot be deleted, their quantity is set to zero instead.
- [N-C01-108] Resetting or cancelling an invoice removes its cost lines together with the revenue entry.
- [N-C01-109] Cancelling or resetting a down payment invoice recomputes the down payment line of the order for unlocked orders.
- [N-C01-110] Cancelling an invoice removes it from invoiced quantity, so its lines return to to invoice while the order is still confirmed.

### STATE

- [N-C01-111] After cancellation lines show nothing to invoice, nothing is billable and the order invoice status is nothing to invoice.

### OPTIONALITY

- NOT APPLICABLE - cancellation has no configuration switch of its own; only the order lock feature matters and it is stated under constraints.

### DEPENDENCY

- [N-C01-112] Cancelling an order warns buyers of generated service purchases through an activity and detaches generated projects, but does not cancel those purchases or projects.

### CONSTRAINT

- [N-C01-113] A completed delivery cannot be cancelled; it can only be reversed by a return.
- [N-C01-114] A posted invoice dated in a locked accounting period cannot be reset or cancelled.
- [N-C01-115] On a locked order, changing product, description, price, unit, quantity, taxes, analytic distribution or discount of a line is refused, down payment prices are not refreshed and re-invoiced costs are refused.

### RISK

- [N-C01-116] Mass cancellation and customer decline from the portal bypass the lock check, so a locked order can be cancelled.
- [N-C01-117] Cancelling a paid invoice removes its reconciliations; the payments stay posted and become unallocated credit of the customer.
- [N-C01-118] A cancelled or sent order can be reset to quotation, which keeps the lock flag and clears signature data; re-confirming launches the full quantity again, which can duplicate deliveries or purchases. Runtime proof is required.

### UNKNOWN

- [N-C01-119] The effect of cancelling an order whose online payment is authorized or captured was not traced and needs a runtime test in a payment provider test mode.
- [N-C01-120] The valuation and cost effect of cancelling an invoice after a combination of partial delivery and return needs runtime proof.

## CAP-C01-05 Partial flows (delivery, invoicing, payment)

### WHAT

- [N-C01-121] A partial delivery completes the picked quantity and creates a backorder transfer, with its own number, holding the remaining movements; the original transfer is done.

### WHY

- [N-C01-122] Partial flows let goods, bills and money move in the amounts that actually happen: partial shipments, progressive or advance billing and part payments.

### BUSINESS RULE

- [N-C01-123] A down payment is created for one order at a time as a percentage or a fixed amount; it adds down payment lines, a draft invoice and notes, counts as quantity one once invoiced, refreshes its price and taxes when posted on unlocked orders, disappears when its draft invoice is deleted, and is deducted by the final invoice as negative lines.
- [N-C01-124] A payment smaller than the open amount leaves the invoice partly paid and still payable; marking the difference as fully paid books it to a chosen account.
- [N-C01-125] Several orders of the same customer, delivery address, currency, fiscal position and company can be billed on one invoice unless grouped per order.

### STATE

- [N-C01-126] After a partial delivery the order shows partially delivered until the backorder is completed or cancelled, then fully delivered.

### OPTIONALITY

- [N-C01-127] Each operation type decides what happens to short quantities: ask the user, always create a backorder, or never and cancel the remainder; a backorder is needed when a line was not fully picked.

### DEPENDENCY

- [N-C01-128] Quantities across documents: ordered quantity on the line, delivered quantity from completed movements, invoiced quantity including drafts, a separate posted-only invoiced quantity and posted-only amounts.

### CONSTRAINT

- [N-C01-129] The down payment amount or percentage must be positive.

### RISK

- [N-C01-130] Declining the backorder cancels the remainder and logs the shortfall on the order; the line then shows invoiced once the delivered part is billed although billed quantity is below ordered quantity.

### UNKNOWN

- [N-C01-131] Over-delivery above demand, the two ways extra order lines are created from done movements, and over-payment behaviour are unconfirmed without running the system.

## CAP-C01-06 Dropship and service variants

### WHAT

- [N-C01-132] A dropship line is supplied by a purchase from the vendor shipped straight to the customer: the supply rule buys instead of moving stock, and a dedicated dropship operation type runs from Vendors to Customers with its own numbering.
- [N-C01-133] Confirming an order generates projects or tasks for service lines configured for it, reuses existing ones on reconfirmation, and milestone lines take delivered quantity from reached milestones.
- [N-C01-134] Confirming an order requests a purchase for service products flagged for subcontracting; later quantity changes update a draft purchase, add a new one after confirmation, or only warn when the quantity is lowered.

### WHY

- [N-C01-135] Dropshipping lets the business sell goods it does not handle: the vendor ships directly to the customer.

### BUSINESS RULE

- [N-C01-136] For dropship lines the quantity already procured is the sum of non-cancelled purchase lines, so cancelling the purchase lets the order relaunch.
- [N-C01-137] Dropship movements are neither stock in nor stock out, so neither the customer invoice nor the vendor bill touches the stock account for them; cost is carried by the vendor bill.
- [N-C01-138] Service-only orders create no delivery transfers and show no delivery status; the invoicing chain runs without a delivery.

### STATE

- [N-C01-139] A completed dropship transfer counts as delivery to the customer; a return from customer to vendor reduces delivered quantity when flagged to update quantities.

### OPTIONALITY

- [N-C01-140] In the studied database the dropship route is active and selectable on order lines and two dropship operation types exist; no order or purchase exists.

### DEPENDENCY

- [N-C01-141] The purchase line and its receipt movements keep the order line link, which carries delivered quantity back to the order; a line with generated purchases cannot change product.

### CONSTRAINT

- [N-C01-142] The subcontract-service flag is allowed only on service products and requires a vendor on the product.

### RISK

- [N-C01-143] A purchase serving several orders is split into one transfer per order when confirmed; the delivered quantity mapping for such purchases needs runtime verification.

### UNKNOWN

- [N-C01-144] Multi-order dropship purchases, kits with dropshipped components and returns of dropshipped goods are unconfirmed without running the system.

## CAP-C01-07 Multi-company and data scope across the chain

### WHAT

- [N-C01-145] Every document of the chain belongs to one company: the order, its delivery work, its invoice and journal entry, its payment and its valuation all run under the company of the order and are kept separate per company.

### WHY

- [N-C01-146] Companies keep their ledgers, stock and customers separate while sharing one database.

### BUSINESS RULE

- [N-C01-147] Related records on orders, journals and transfers are checked against the document company automatically, and posting refuses accounts of other companies.
- [N-C01-148] Users see orders, transfers, movements, entries and payments only of the companies they may access; salespeople additionally see invoices only where they are the salesperson or none is set.

### STATE

- NOT APPLICABLE - documents carry no company status; the company of a document is fixed when it is created.

### OPTIONALITY

- [N-C01-149] Lock dates are company settings applied through the company hierarchy: the sales lock applies to sales journals, the purchase lock to purchase journals, and fiscal and hard locks to all.
- [N-C01-150] The studied database has one company, no branches and no inter-company flows, so every multi-company behaviour is read from rules only.

### DEPENDENCY

- [N-C01-151] Payments can be registered for items of one company or of sibling branches of one root company; sibling-branch items need access to the parent company and are paid as the parent with system rights; items of several root companies are refused.
- [N-C01-152] The community edition ships only an inter-company payment module; no automatic order-to-purchase inter-company flow exists, and delivery destination and unpacking offer hooks for such flows.

### CONSTRAINT

- [N-C01-153] An order cannot contain products owned by a company outside its own company branches.
- [N-C01-154] A confirmed order of goods must have a warehouse, and a route belonging to another company needs a warehouse of that company.

### RISK

- [N-C01-155] A salesperson sees invoices of own orders but cannot post them, so visibility and posting rights sit with different people.

### UNKNOWN

- [N-C01-156] Cross-company selection on confirmation and mass cancellation, mixed-company visibility and branch behaviour are unconfirmed without a multi-company database.

## CAP-C01-08 Accounting, stock, audit and compliance implications

### WHAT

- [N-C01-157] Accounting entries arise at five points: invoice posting (the invoice entry, with cost lines in perpetual mode), payment confirmation, reconciliation differences, stock movements touching valued locations in perpetual mode, and the period closing entry; order confirmation and ordinary customer deliveries create none by default.
- [N-C01-158] The audit trail tracks order status and lock, transfer status, invoice number, reference, accounting date, state and type, and payment state; quantity changes on confirmed lines and the links between order, transfer and invoice leave notes.

### WHY

- [N-C01-159] Posting, numbering and locking exist to give each ledger entry a unique, ordered and tamper-evident record.

### BUSINESS RULE

- [N-C01-160] Posted entries refuse changes to lines, dates, partner, terms, currency and fiscal position; corrections use credit notes or a reset to draft.
- [N-C01-161] Posting a customer invoice checks fiscal, sales, tax and hard lock dates and shifts the date; changing or cancelling a posted invoice checks them again and refuses.
- [N-C01-162] For customer invoices the accounting date follows the invoice date and is moved only by a violated lock, so the tax point is the invoice date and not delivery or payment; the delivery date is shown on the invoice for information only, the taxable supply date is not computed, and cash-basis taxes are switched on for the company but used by no tax.

### STATE

- NOT APPLICABLE - document statuses are described in the happy path and cancellation capabilities; this capability only lists events and controls.

### OPTIONALITY

- [N-C01-163] Hash chaining applies only to journals flagged for it and happens at posting; no journal in the studied database has it.

### DEPENDENCY

- [N-C01-164] With the valuation module, a delivery completion date inside a fiscal or hard locked period is refused unless a system parameter disables the check.

### CONSTRAINT

- [N-C01-165] Roles split the chain: salespeople create orders and draft invoices (read-only on entries), stock users validate deliveries and create returns, invoicing users post invoices and register payments.

### RISK

- [N-C01-166] With periodic valuation and a manual closing period, the cost of delivered goods reaches the ledger only when someone runs the closing by hand.

### UNKNOWN

- [N-C01-167] Tax report impact of date shifts under locks, hash interplay with date shifts and numbering gaps after cancelling posted invoices need runtime proof.

## CAP-C01-09 Consistency audit across the module units

### WHAT

- [N-C01-168] Three hand-offs were verified consistent across units: credit notes keep order-line links and lower invoiced quantity, credit notes generated from the order carry no origin link and take cost from order-line links, and the order status vocabulary is shared.

### WHY

- NOT APPLICABLE - the audit has no business purpose of its own; it only reconciles the module findings.

### BUSINESS RULE

- NOT APPLICABLE - the audit states no rule of the system; rule-like findings are listed under constraint, risk and unknown.

### STATE

- NOT APPLICABLE - the audit describes no document status.

### OPTIONALITY

- NOT APPLICABLE - the audit depends on no configuration switch; configuration facts used are quoted in the findings.

### DEPENDENCY

- [N-C01-169] No unit states at chain level that goods are reserved during order confirmation.
- [N-C01-170] The delivery-date lock check at validation is described in the valuation unit only.

### CONSTRAINT

- [N-C01-171] The word lock covers four different things across units: order lock, transfer lock, accounting lock dates and hashed entries.
- [N-C01-172] Paid means three different things (order online payment, invoice residual zero, payment matched or invoices paid) and cancelled is spelled two ways.
- [N-C01-173] To invoice names three measures with different timing.
- [N-C01-174] Valuation entries is used loosely for stored movement values.
- [N-C01-175] Done is valid for transfers, movements and payments but not for orders; leftover references remain in code.

### RISK

- [N-C01-176] One unit describes returns as limited to completed transfers while its own evidence and the source allow order-linked transfers in any state.
- [N-C01-177] One unit shows an in-payment invoice status as reachable; another unit and the source show it cannot occur in this edition.
- [N-C01-178] One unit calls the invoice delivery date an empty placeholder that only localisations fill; the installed sales-stock module fills it from the order effective date.

### UNKNOWN

- [N-C01-179] A unit credits two hooks with booking cost differences, but no caller of them exists in the community tree.
- [N-C01-180] A unit lists valuation among modules reacting through the order-synchronisation hook; valuation actually reacts through the completion routine.
- [N-C01-181] A unit orders the confirmation follow-ups as if the stock step ran first; the actual order depends on module load order.
- [N-C01-182] Cancelling an invoice is described as cancelling payments; for invoices the payments stay posted and become unreconciled.
- [N-C01-183] Whether number gaps arise when a posted invoice is cancelled, and the effect on gapless numbering compliance, needs runtime proof in a real journal pattern.

