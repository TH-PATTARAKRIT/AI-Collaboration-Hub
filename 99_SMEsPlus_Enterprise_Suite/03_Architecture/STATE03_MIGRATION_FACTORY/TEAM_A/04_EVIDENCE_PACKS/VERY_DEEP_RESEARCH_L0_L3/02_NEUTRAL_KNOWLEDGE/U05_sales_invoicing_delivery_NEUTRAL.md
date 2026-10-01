# U05 - Sales invoicing and delivery - Neutral Knowledge

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source family: Odoo 19 Community. Date: 2026-10-02.
> Plain business and process statements only. Each statement carries an identifier that links to the restricted evidence layer.
> No coverage, level, gate or approval claim is made.

## CAP-U05-01 Invoicing policy (ordered vs delivered quantities)

### WHAT

- [N-U05-001] The system lets each sellable product declare whether the customer is billed for the quantity ordered or for the quantity actually delivered.
- [N-U05-002] The chosen billing basis drives how much of each order line is billable at any moment, and therefore when an order shows as ready to bill.

### WHY

- [N-U05-003] Businesses that ship goods usually want to bill only what left the warehouse, while businesses selling services or prepaid items want to bill at the moment of sale; one switch per product serves both.

### BUSINESS RULE

- [N-U05-004] Only two billing bases exist: bill what was ordered, or bill what was delivered.
- [N-U05-005] For a line billed on ordered quantity, the billable quantity is the ordered quantity minus the quantity already billed; for a line billed on delivered quantity it is the delivered quantity minus the quantity already billed.
- [N-U05-006] A line has a billable quantity only while its order is confirmed; on a quotation or a cancelled order the billable quantity is zero.
- [N-U05-007] Changing a product's billing basis later does not retroactively recompute lines already on existing orders until those lines are otherwise recalculated.
- [N-U05-008] For goods billed on delivered quantity, once every stock movement of the line is finished and some quantity was delivered, the line shows as fully billed after nothing is left to bill, even if less than the ordered quantity was delivered (supports goods sold by weight).
- [N-U05-009] The amount still to bill for a line is computed on the delivered quantity when the product is delivered-basis and on the ordered quantity otherwise, while an order-level balance figure always uses the ordered quantity minus the posted billed quantity.
- [N-U05-010] When an order is paid in full online and automatic invoicing is on, the billable quantity is forced to follow the ordered basis for every confirmed line regardless of the product setting.
- [N-U05-011] When a completed delivery contains a product that is not on the order, the order receives a new line with ordered quantity zero and the delivered quantity recorded; its price follows an existing line of the same product when that product is billed on delivered quantity and is zero when billed on ordered quantity.

### STATE

- [N-U05-012] A line with a non-zero billable quantity shows as to bill; a line with nothing left to bill whose billed quantity has reached the ordered quantity shows as fully billed; a line billed on ordered quantity with nothing left to bill whose delivered quantity exceeds the ordered quantity shows as an upselling opportunity; any other line shows as nothing to bill.

### OPTIONALITY

- [N-U05-013] A company-wide default billing basis can be set in the sales settings and is applied to newly created products; each product can override it.
- [N-U05-014] For goods, the billing basis is reset to the ordered basis whenever the product type is recalculated; for other product types it is set to ordered only when empty.
- [N-U05-015] Service products may choose among prepaid fixed price, delivered quantity set manually, delivered by milestones, or delivered by timesheets; these map onto the two basic billing bases.
- [N-U05-016] Turning the default billing basis to anything other than ordered switches automatic invoicing off, and the automatic-invoicing option is only offered when the default is ordered and online payment is required for confirmation.

### DEPENDENCY

- [N-U05-017] Delivered quantity of goods lines comes from completed stock movements, so the delivered basis depends on the warehouse module being active; without it delivered quantity is entered by hand or derived from analytic records.
- [N-U05-018] Discount lines created from company settings, and discount lines created from promotion rewards, are required to use the ordered basis.

### CONSTRAINT

- [N-U05-019] The billing basis is mandatory for every sellable product that is not a combination product and is hidden for combination products.
- [N-U05-020] Changes of a product's billing basis are tracked in the product history.

### RISK

- [N-U05-021] Because the billing basis is read live from the product when billable quantity is computed, switching it on a product that already has partly billed orders can change what the next invoice contains without any change to the order itself.
- [N-U05-022] Nothing prevents billing an ordered-basis goods line before it ships; the only signal is the upselling status after over-delivery, so premature billing is a policy decision rather than a system block.

### UNKNOWN

- [N-U05-023] Whether the product form hides or locks the billing basis for particular product types in the runtime user interface beyond what the view definition declares is not confirmed without running the system.
- [N-U05-024] The effective default billing basis observed by a new product at runtime depends on stored defaults in the live database; the restored database holds no stored default for it.

## CAP-U05-02 Invoice creation from an order and order invoicing status

### WHAT

- [N-U05-025] From a confirmed order the system creates one or more draft customer invoices containing the order lines that are currently billable, and keeps a link between each invoice line and the order line it came from.
- [N-U05-026] Each order carries an invoicing status of nothing to bill, to bill, fully billed or upselling opportunity, derived from the status of its lines.

### WHY

- [N-U05-027] Sales staff must be able to bill progressively and partially, and finance must be able to trace every invoiced amount back to its order line.
- [N-U05-028] The order-level status gives a worklist of orders waiting to be billed and flags orders where more was delivered than sold.

### BUSINESS RULE

- [N-U05-029] A line is included in an invoice only if its billable quantity is positive, or negative when the invoice is a final one; lines with zero billable quantity are skipped and notes are carried along.
- [N-U05-030] Section and subsection headings are copied onto the invoice only when at least one billable line sits beneath them.
- [N-U05-031] Down payment lines are moved to the end of the invoice under their own heading so that previously billed advances appear as deductions.
- [N-U05-032] An invoice line copies the quantity to bill, unit price, discount, taxes, product, unit of measure, description and analytic distribution of the order line; combination products appear as a heading with the quantity.
- [N-U05-033] The invoice header copies from the order the customer reference or order name, the notes, the currency, the campaign, medium and source, the sales team, the invoicing contact, the delivery contact, the payment terms, the preferred payment method, the salesperson, the payment reference and any pending or unreconciled online payments.
- [N-U05-034] The invoice uses the fiscal position of the order, or if the order has none the fiscal position derived for the invoicing contact.
- [N-U05-035] The invoice goes into the invoicing journal chosen on the order; when none is chosen the sales journal with the lowest sequence is used.
- [N-U05-036] Several orders are merged into one invoice when they share company, invoicing contact, delivery contact, currency and fiscal position, unless the user asked for one invoice per order; merged invoices carry the combined origins and references, and the payment reference only if all orders agree.
- [N-U05-037] If a final invoice would have a negative total it is converted into a credit note and the link to the earlier invoice is set only when exactly one earlier invoice shares the order lines and local rules require a reference to the original.
- [N-U05-038] An order's billed quantity counts every non-cancelled invoice line including drafts, so a second invoice cannot double-bill quantities already sitting on a draft invoice.
- [N-U05-039] Invoices are created with elevated rights so that a salesperson without accounting rights can bill from an order but cannot create an invoice from scratch.
- [N-U05-040] Each created invoice gets a note pointing back to its source order, and cancelling an order cancels its draft invoices.

### STATE

- [N-U05-041] An order that is not confirmed always shows nothing to bill.
- [N-U05-042] A confirmed order shows to bill when any billable line has something to bill, except that if the only billable lines are discount, delivery or reward lines the order shows nothing to bill.
- [N-U05-043] A confirmed order shows fully billed when all its counted lines are fully billed, and upselling opportunity when its counted lines are all fully billed or upselling; down payment lines and headings are not counted.
- [N-U05-044] When an order becomes upselling opportunity, a to-do activity is scheduled for the salesperson, or for the customer's account manager when there is no salesperson.

### OPTIONALITY

- [N-U05-045] The user chooses between billing all billable lines (regular invoice) and a percentage or fixed advance; for several orders at once only the regular invoice is offered, with a switch for one invoice per customer or one per order.
- [N-U05-046] The invoicing journal on the order is optional and empty by default, so the company's default sales journal logic applies unless someone picks one.
- [N-U05-047] With the timesheet module a billing period can be given so that only time recorded in that period is billed; with the warehouse module the invoice also carries the shipping terms and the delivery date.

### DEPENDENCY

- [N-U05-048] Invoice documents, taxes, journals and posting belong to the accounting module; the order only prepares the draft and its links.
- [N-U05-049] With the warehouse module the invoice carries the date of the first completed customer delivery of the order and the order's shipping terms and location.

### CONSTRAINT

- [N-U05-050] If no line is billable the system refuses with an explanatory message unless the caller asked to ignore the situation, and the message explains the two product settings that decide billability.
- [N-U05-051] If the user lacks both permission to create invoices and permission to modify the order, nothing is created and no error is shown.
- [N-U05-052] When an invoice is copied for correction, the copy keeps its link to the same order lines so the order's billing history stays consistent.

### RISK

- [N-U05-053] The final-invoice switch that deducts advances is not offered in the standard billing form, so every regular invoice created from the form behaves as a final invoice and may turn out as a credit note when quantities went down.
- [N-U05-054] Merging requires identical invoicing contact, delivery contact, currency and fiscal position, so two orders of the same customer with a different delivery address produce separate invoices even when a single invoice was expected.
- [N-U05-055] The upselling activity is created as a side effect of recalculating status, so bulk recalculation may schedule many activities at once.

### UNKNOWN

- [N-U05-056] Which sales journal is picked when several exist and none is chosen on the order is decided in the accounting module and not confirmed here.
- [N-U05-057] Behavior when the invoicing contact or the delivery contact belongs to a different company than the order is governed by company-check rules at save time and was not exercised.

## CAP-U05-03 Down payments and advance invoices

### WHAT

- [N-U05-058] The system lets a user bill a customer in advance for a confirmed order, either as a percentage of the order total or as a fixed amount, before anything is delivered or fully billed.
- [N-U05-059] An advance is recorded on the order as special lines under a dedicated heading, and the advance invoice is created as a draft with its own advance line.

### WHY

- [N-U05-060] Customers are often asked to prepay part of a large order; the order must remember what was prepaid so that the final invoice deducts it exactly.

### BUSINESS RULE

- [N-U05-061] An advance requires a strictly positive percentage or amount; zero or negative values are refused when the user confirms the creation.
- [N-U05-062] An advance can be created for one order at a time only.
- [N-U05-063] The advance amount is computed on the whole order at ordered quantities, split across the distinct tax combinations of the order lines so that tax amounts add up exactly to the requested total; taxes that cannot be discounted are folded into the base.
- [N-U05-064] One advance line is added to the order for each tax combination, with ordered quantity zero and the advance price; a single heading for all advances is created if missing.
- [N-U05-065] The advance invoice reuses the order's header information, and each advance line is invoiced with quantity one, labelled either as a percentage advance or as a plain down payment.
- [N-U05-066] The income account of the advance is the company's down payment account when one is configured (after mapping through the fiscal position); otherwise the account of the underlying product is used.
- [N-U05-067] An advance line counts as billed once its non-cancelled invoice lines carry a non-zero net balance, and as not billed when they net to zero.
- [N-U05-068] On the final invoice each advance line appears with quantity minus one, deducting what was prepaid; advances are never deducted on an invoice that is not a final one.
- [N-U05-069] When an advance invoice is posted, cancelled or reset to draft, the advance line on the order refreshes its description and, on posting, its price and taxes from the posted advance invoices, unless the order is locked.
- [N-U05-070] The advance line description reads as draft with the creation date, cancelled, or the payment reference and date of the posted advance invoice.
- [N-U05-071] Deleting a draft advance invoice also deletes the order's advance lines that only it referenced, and advance lines never invoiced may be removed from a confirmed order while all other confirmed lines may not.
- [N-U05-072] Advance lines are not copied when an order is duplicated and their product cannot be changed.

### STATE

- [N-U05-073] An advance line counts as billed while an advance invoice, even a draft, carries it, and as settled again once a final invoice, even a draft, deducts it so that the net is zero.
- [N-U05-074] Advance lines and the advance heading are ignored when computing the order-level billing status, so an order with only advances billed still shows as nothing to bill or to bill according to its real lines.

### OPTIONALITY

- [N-U05-075] The company can name a down payment account; a chart-of-accounts template may pre-fill it at module installation.
- [N-U05-076] A percentage advance button is also shown on a confirmed order whose billing status is nothing to bill, which lets users take an advance before delivery on delivered-basis orders.

### DEPENDENCY

- [N-U05-077] The tax split and rounding of the advance is performed by the accounting tax engine; the order only passes its lines and receives the resulting advance lines.
- [N-U05-078] Online payment flows can create a fixed-amount advance invoice automatically when a customer pays part of the order and automatic invoicing is on.

### CONSTRAINT

- [N-U05-079] The database allows an order line without a product only if it is an advance line, a heading or a note; headings and notes must carry no product, price, quantity or unit of measure.
- [N-U05-080] On a locked order, changes to posted advance invoices are not forwarded to the order's advance lines.

### RISK

- [N-U05-081] No upper limit on the percentage or the fixed amount was found in the creation step, so an advance larger than the order total may be accepted and must be caught by review or by accounting controls.
- [N-U05-082] The advance amount is computed on ordered quantities for the whole order including other advance lines and reward lines, not on delivered or billable quantities.
- [N-U05-083] The positivity check runs only when the user confirms the form; the automatic creation path from online payments bypasses it.
- [N-U05-084] Because a draft final invoice already nets the advance to zero in the order's billed quantity, a final invoice left in draft hides the advance as settled.

### UNKNOWN

- [N-U05-085] Which income account is used when no company down payment account is set, because the tax engine returns lines without a product, was not determined from the source and needs execution.
- [N-U05-086] Behavior when the order mixes taxes that cannot be discounted with percentage advances needs execution against sample orders.

## CAP-U05-04 Credit notes, refunds and returns feeding back into the order

### WHAT

- [N-U05-087] When goods or services already invoiced are credited or returned, the order lines move their billed quantity and delivered quantity accordingly, so the order again shows what remains to bill.
- [N-U05-088] There are two separate routes: a customer return in the warehouse that lowers the delivered quantity, and a credit note that lowers the billed quantity; either route can be used alone or together.

### WHY

- [N-U05-089] Finance needs the order to stay consistent with invoices and shipments after a correction, and sales needs to know whether the customer will be billed again.

### BUSINESS RULE

- [N-U05-090] A credit note that is linked to order lines reduces the billed quantity of those lines by its quantity; a regular invoice increases it; cancelled documents are ignored.
- [N-U05-091] Billed quantity follows documents in draft as well as posted ones, whereas the billed amount and the posted billed quantity follow posted documents only.
- [N-U05-092] Credit notes created by reversing an invoice keep the link to the original order lines, so they reduce the billed quantity just as credit notes produced from the order do.
- [N-U05-093] A credit note linked to an order also appears among the order's invoices.
- [N-U05-094] When a customer return is flagged to update order quantities, the delivered quantity of the order line is reduced by the returned quantity; returns not so flagged leave it unchanged.
- [N-U05-095] Delivered quantity is the sum of completed outgoing movements minus completed returned movements that are flagged to update the order, except that receipts of dropshipped goods that are not returns are ignored.
- [N-U05-096] Once delivered quantity falls below billed quantity on a delivered-basis line, the billable quantity becomes negative; a final invoice then carries negative quantities and, if the total is negative, becomes a credit note.
- [N-U05-097] The return wizard passes the order line link and the sales order to the return movement, so the return belongs to the same order.
- [N-U05-098] A return can be started from any completed delivery that belongs to an order.
- [N-U05-099] Crediting an advance invoice sets the advance line back to not billed once the balances net to zero and keeps the description of the active advance invoice.
- [N-U05-100] With time-based billing, posting a credit note releases the time entries billed on the credited invoice so they can be billed again, and the next billing period computation avoids over-billing when credit notes exist.

### STATE

- [N-U05-101] After a credit note on an ordered-basis line the line returns to to bill because the billed quantity drops below the ordered quantity.
- [N-U05-102] After a return flagged to update the order on a delivered-basis line, the line shows as to bill with a negative quantity until a final invoice or credit note is issued.

### OPTIONALITY

- [N-U05-103] Each return line has a flag, on by default, that decides whether the order's delivered quantity is updated by the return.
- [N-U05-104] The user may reverse an invoice with or without creating a new corrected invoice; corrections made through the reversal keep campaign, medium and source of the original.

### DEPENDENCY

- [N-U05-105] Posting, reversal and cancellation of invoices belong to the accounting module; stock return mechanics and cost valuation belong to the inventory and valuation areas and are only referenced here.
- [N-U05-106] Cost-of-goods quantities on a credit note are looked up through the original invoice, or through the order's invoices when the credit note has no original.

### CONSTRAINT

- [N-U05-107] Ordered quantity on a delivered line cannot be decreased below what has already been delivered; the user must create a return instead.
- [N-U05-108] A localization can require that a credit note references its original invoice; the base system sets this reference only when a single earlier invoice shares the order lines and the localization demands it.

### RISK

- [N-U05-109] The inline note in the order logic says billed quantity falls only for credit notes generated from the order, which contradicts the copy-with-link behavior; creating a credit note directly from an invoice does lower billed quantity and may cause the order to propose billing the same goods again.
- [N-U05-110] A return not flagged to update the order leaves the order showing full delivery, so an ordered-basis or delivered-basis line will not signal that a credit is due.
- [N-U05-111] Credit notes in draft already lower the billed quantity, so a draft credit note that is later cancelled and re-created can briefly make the order propose billing again.

### UNKNOWN

- [N-U05-112] The runtime order status after each combination of invoice, return and credit note was not observed because the restored database holds no orders.
- [N-U05-113] Which accounting entries the credit note produces for stock-valued goods is outside this study and is handed to the valuation and posting areas.

## CAP-U05-05 Delivery from sales orders

### WHAT

- [N-U05-114] Confirming an order that contains physical goods automatically requests the warehouse to deliver them: the system raises delivery requests per goods line, grouped under a reference carrying the order name, and the resulting delivery documents are confirmed immediately.
- [N-U05-115] The order tracks how much of each line has been delivered, an overall delivery status, and the date of the first completed customer delivery.

### WHY

- [N-U05-116] Sales must drive fulfillment without a separate hand-off, and later billing and customer communication need a trustworthy delivered quantity and delivery status.

### BUSINESS RULE

- [N-U05-117] Delivery requests are raised only for goods lines of confirmed orders that are not locked; the quantity requested is the ordered quantity minus the quantity already requested, delivered or returned.
- [N-U05-118] Each delivery request carries the order name as origin, the reference linking it to the order, the order line, the delivery contact, the warehouse, any specific routes of the line, the company, and the customer location as final destination.
- [N-U05-119] The promised date is the order's committed delivery date when set, otherwise the confirmation date plus the line lead time; the planned date is that promised date minus the company's safety days.
- [N-U05-120] Increasing a confirmed line's ordered quantity requests only the extra quantity; decreasing it requests nothing and instead logs a warning on the open deliveries, and cancelling the order cancels all unfinished deliveries and logs the effect.
- [N-U05-121] The warehouse of an order defaults from the stored company default or the salesperson's default warehouse while the order is a quotation; each line may use a different warehouse when a specific route pulls from elsewhere.
- [N-U05-122] The delivered quantity of a goods line is the sum of finished outgoing movements less finished returned movements flagged to update the order, converted to the line's unit of measure.
- [N-U05-123] The shipping policy of the order is either deliver as soon as available with backorders, or deliver everything at once; with all-at-once the promised date uses the longest line lead time and deliveries move together, otherwise the shortest.
- [N-U05-124] Setting or changing the committed delivery date moves the deadline of all open outgoing movements of the order; changing the line lead time does the same when no committed date is set.
- [N-U05-125] Changing the delivery contact of an order warns the user and schedules a reminder activity on open deliveries, but does not change the contact on the deliveries unless the caller asks for propagation.
- [N-U05-126] A delivery that actually ships a product missing from the order adds a line to the order with ordered quantity zero and the shipped quantity as delivered.
- [N-U05-127] When a delivery is validated with less than the expected quantity, a note is logged on the order describing the shortfall.
- [N-U05-128] The delivery address and incoterms entered on the order are carried to invoices; the first completed customer delivery date is shown on the invoice.

### STATE

- [N-U05-129] Delivery status is not delivered when open deliveries exist and none is finished, started when some delivery is finished but no quantity is delivered, partially delivered when some quantity is delivered and some delivery is open, and fully delivered when every delivery is finished or cancelled; it is empty when there are no deliveries or all are cancelled.
- [N-U05-130] The order becomes cancelled only through the order cancellation action, which cancels unfinished deliveries first; finished deliveries remain and the delivered quantities stay recorded.

### OPTIONALITY

- [N-U05-131] Specific delivery routes can be offered on order lines only if they are marked as selectable on sales orders.
- [N-U05-132] The company may enable safety days for sales, and the default shipping policy is a company-level setting.
- [N-U05-133] A delivery request is raised for every goods line whether or not the product is stock-tracked; stock tracking only controls the availability indicator on the order.

### DEPENDENCY

- [N-U05-134] Movement creation, reservation, backorder splitting and validation are owned by the transfer engine; the sales layer only supplies requests and reads results.
- [N-U05-135] The warehouse delivery chain (one, two or three steps) and the routes themselves are configured in inventory settings; the order only chooses warehouse and optional routes.

### CONSTRAINT

- [N-U05-136] A confirmed or later order that contains goods lines must have a warehouse; if the company owns warehouses the user is told to set one, and a line using a route of another company needs a warehouse in that company.
- [N-U05-137] The product of an order line cannot be changed once it has an active delivery movement, and ordered quantity cannot drop below the delivered quantity.
- [N-U05-138] Locked orders raise no new delivery requests when quantities are later increased.

### RISK

- [N-U05-139] In the restored configuration the lock-on-confirmation feature is switched on for all internal users, so quantity increases on confirmed orders would not be delivered unless the order is unlocked first.
- [N-U05-140] The mass cancellation action cancels orders without checking the lock, which differs from the single cancellation action that refuses locked orders.
- [N-U05-141] Cancelling an order leaves finished deliveries and posted invoices untouched, so cancellation after partial delivery does not reverse goods or billing.
- [N-U05-142] Two separate code paths create the extra line for an unlisted product when a delivery is validated; their joint behavior was not exercised.

### UNKNOWN

- [N-U05-143] How the transfer engine splits requests into one, two or three step chains and when backorders are created is outside this unit and was not confirmed.
- [N-U05-144] Runtime effects of the safety-days setting on the actual delivery dates were not observed.

## CAP-U05-06 Interplay of delivered and invoiced quantities

### WHAT

- [N-U05-145] The order continuously reconciles three quantities per line: ordered, delivered and billed, and from them derives what can be billed now, what is fully billed, and where more was delivered than sold.
- [N-U05-146] Billing can therefore follow shipments one by one: each new invoice covers the quantity delivered since the previous invoice.

### WHY

- [N-U05-147] Finance must avoid billing goods that have not shipped when the policy says so, avoid billing twice, and recover quantities that were delivered but never billed.

### BUSINESS RULE

- [N-U05-148] On a line billed by ordered quantity, billing may happen immediately after confirmation, before any delivery; on a line billed by delivered quantity, only the quantity delivered and not yet billed is billable.
- [N-U05-149] If the billed quantity exceeds the delivered quantity on a delivered-basis line, the billable quantity is negative and is only picked up by a final invoice, which then becomes a credit note when the total is negative.
- [N-U05-150] Nothing in the order logic stops a user from billing more than was delivered on an ordered-basis line; the signal is advisory only, through the upselling status after over-delivery.
- [N-U05-151] Reducing the ordered quantity of a confirmed line is logged on the order but is not blocked by the billed quantity; the delivery module only blocks reductions below the delivered quantity.
- [N-U05-152] The billed quantity is converted to the order line's unit of measure without rounding, so quantities invoiced in another unit still reconcile.
- [N-U05-153] The unit price of a line that already has billed quantity is not recomputed from the pricelist.
- [N-U05-154] The delivered quantity of lines without stock movements is entered by hand, derived from posted analytic records of expenses, from recorded time, from reached milestones, or, for kit products, from the delivery of the kit components.
- [N-U05-155] A combination product line is billable only when at least one of its component lines is billable.
- [N-U05-156] The system can show delivered and billed quantities and the amount to bill as of a past accrual date by considering only movements and invoices dated up to that date.
- [N-U05-157] Finished movements and invoices are tied to the order, not to each other: an invoice does not reference the shipment it covers, and the invoice delivery date shows only the first completed delivery of the order.

### STATE

- [N-U05-158] A line moves to to bill when delivered quantity rises on a delivered-basis line, when billed quantity falls after a credit note, or when ordered quantity rises on an ordered-basis line.
- [N-U05-159] A line moves to fully billed when the billed quantity reaches the ordered quantity, or, for goods billed on delivery, when all movements are finished and something was delivered even if less than ordered.

### OPTIONALITY

- [N-U05-160] Which source supplies the delivered quantity depends on the product type and the installed modules: warehouse movements, analytic records, timesheets, milestones or manual entry.

### DEPENDENCY

- [N-U05-161] Delivered quantity from warehouse movements depends on the warehouse module; time-based and milestone-based delivered quantities depend on the project and timesheet modules.

### CONSTRAINT

- [N-U05-162] Quantities use the product unit decimal precision when deciding whether anything is left to bill.

### RISK

- [N-U05-163] Because drafts count as billed, a forgotten draft invoice hides billable quantity from the next invoicing run until it is cancelled or posted.
- [N-U05-164] Three different billed measures coexist (including drafts, posted only, and posted amounts), so reports built on different measures can disagree for the same order.
- [N-U05-165] Manual delivered quantity can be edited by users with write access to the line and directly changes what is billable on delivered-basis service lines.

### UNKNOWN

- [N-U05-166] Whether recalculation of billable quantity after a shipment is immediate for stored fields on very large orders, and its performance, was not observed.
- [N-U05-167] The unit of measure rounding behavior when delivered and invoiced units differ was not exercised.

## CAP-U05-07 Loyalty and promotion programs on orders

### WHAT

- [N-U05-168] Promotion and loyalty programs add discount or free-product lines to an order, award points or coupons for future orders, and let customers pay part of an order with a gift card or an electronic wallet.
- [N-U05-169] Eight program kinds exist: coupons, gift cards, loyalty cards, promotions, electronic wallets, discount codes, buy-some-get-some and next-order coupons.

### WHY

- [N-U05-170] Marketing needs rule-based incentives that are applied and withdrawn automatically as the order changes, and finance needs the incentives to appear as ordinary, taxed order lines that flow into invoices.

### BUSINESS RULE

- [N-U05-171] A program applies to an order only if it is active, enabled for sales, belongs to the order's company or its parent company, matches the pricelist, and is within its start and end dates evaluated in the company's timezone.
- [N-U05-172] When payment is already authorised or completed, dates are evaluated at the creation date of the earliest such payment instead of today.
- [N-U05-173] Points are earned per order, per unit or per amount spent, only when the minimum amount (with or without tax) and the minimum quantity of eligible products are met; points can be split into several coupons for future orders.
- [N-U05-174] A reward is claimable only if the coupon holds at least the points the reward requires; points already consumed by reward lines on the same order are deducted, and points the order itself will give are added except for programs that apply to future orders only.
- [N-U05-175] Discount rewards are written as negative lines split per tax combination, never discount fixed taxes, and never exceed the order total or the reward's maximum; a free-product reward becomes a product line with a full discount and quantity based on claimable multiples of the required points.
- [N-U05-176] Gift card and wallet rewards are applied last, as a negative line capped by the discountable amount, and the card's tax treatment follows the discount product.
- [N-U05-177] Only the best of several global discounts is kept: the one granting the larger saving, or the smaller one if both exceed the order amount.
- [N-U05-178] Every change to the order lines, prices or applied codes triggers a full recomputation of points and reward lines; rewards that are no longer valid are removed and coupons created for the order are deleted unless the program is personal to a customer.
- [N-U05-179] Entering a code finds either a rule trigger or an existing coupon; expired, used or invalid codes are refused with a message, and the program's usage limit is checked while the program row is locked against concurrent use.
- [N-U05-180] On confirmation the order is refused if any coupon would end up with negative points; otherwise rewards are refreshed, history entries are written, points are credited and debited on the coupons, empty current-order coupons are discarded and reward coupons are sent by email.
- [N-U05-181] When one order is confirmed while claimable rewards remain unapplied, the user is notified.
- [N-U05-182] Reward lines may not be edited by the customer on the portal, are not copied when an order is duplicated, and are excluded from the sellable line selection.
- [N-U05-183] A reward that has already been used on an order is archived rather than deleted.
- [N-U05-184] A confirmed order with a zero total created only by rewards is invoiced and sent automatically when automatic invoicing is on.

### STATE

- [N-U05-185] A coupon gains points when an order giving points is confirmed and loses points when reward lines on a confirmed order are added; when a confirmed order is cancelled the points movements and history entries are reversed.
- [N-U05-186] A program usage count grows with every order using one of its rewards and, with a usage limit, the program stops applying once the limit is reached.

### OPTIONALITY

- [N-U05-187] Programs are triggered automatically or only after a code is entered; applicability to the current order, future orders or both is a program setting, and some program kinds are personal to a customer.
- [N-U05-188] The user may open a reward wizard or a coupon-code wizard on a quotation; the buttons are disabled once the order is locked or cancelled.

### DEPENDENCY

- [N-U05-189] Program definitions, coupons, rules and rewards belong to the generic loyalty module; the sales module only applies them to orders.
- [N-U05-190] Reward discount products are services billed on ordered quantity, without taxes by default, so reward lines are invoiced together with the order.

### CONSTRAINT

- [N-U05-191] A reward line alone never makes an order billable: when only discount, delivery or reward lines remain to bill the order shows nothing to bill.
- [N-U05-192] A program with a usage limit must have a positive maximum.
- [N-U05-193] Coupon points on an order are unique per order and coupon.

### RISK

- [N-U05-194] Rewards are recalculated on every order change, so a manual edit of reward line price or quantity is overwritten.
- [N-U05-195] Cancelling an order deletes its reward lines and coupon movements, so the discount history of a cancelled order is lost except in the order log.
- [N-U05-196] Because discount lines are split by tax and carry the points cost on only one of them, deleting or editing one of them can leave points inconsistent until the next recomputation.
- [N-U05-197] Rewards apply on ordered quantities and amounts, so a promotional discount is not reduced when goods are returned or credited unless the reward line itself is corrected.

### UNKNOWN

- [N-U05-198] The effect of installed delivery-related reward extensions, such as free shipping rewards, was not studied.
- [N-U05-199] The restored configuration contains only one seeded gift card program and no coupons, so reward application behavior was not observed.

## CAP-U05-08 Cross-sell links to opportunities, purchasing, manufacturing, projects and timesheets

### WHAT

- [N-U05-200] Confirming an order can drive other business areas: it updates the sales opportunity it came from, creates purchase requests for services that are bought from subcontractors, links manufacturing orders, and creates projects, tasks and time-based billing for services.

### WHY

- [N-U05-201] Sales, purchasing, production and project delivery should start from the same confirmed order without re-keying, while each area keeps its own document.

### BUSINESS RULE

- [N-U05-202] An order may be linked to a sales opportunity; opportunities show the number and untaxed total of confirmed orders and the number of open quotations.
- [N-U05-203] When a linked order is confirmed, the opportunity's expected revenue is raised to the order's untaxed amount if that is higher and the order currency equals the company currency, and a note is logged.
- [N-U05-204] Creating a quotation from an opportunity copies campaign, medium, source, tags, team, salesperson, company, title as origin and the customer; if the opportunity has no customer the user may create one, link an existing one or continue without.
- [N-U05-205] Orders of merged opportunities are all attached to the surviving opportunity.
- [N-U05-206] A service product can be flagged to be subcontracted; such a product must be a service and must have at least one vendor defined.
- [N-U05-207] On order confirmation, each service line of a flagged product that has not already generated purchase lines creates a purchase line for the first matching vendor, reusing a draft purchase order of that vendor and that order or else creating one.
- [N-U05-208] The purchase line takes quantity converted to the vendor unit, the vendor price converted to the purchase currency, the vendor's discount, taxes mapped to the vendor's fiscal position, the planned date from the commitment date minus the vendor delay, and the order's analytic distribution.
- [N-U05-209] Raising the ordered quantity updates the purchase line when it is still a draft and otherwise creates an extra purchase line for the difference; lowering it only schedules a warning activity on the purchase order.
- [N-U05-210] Cancelling the order puts a warning activity on each purchase order still open that was generated from it, and cancelling a purchase order puts a warning activity on the originating orders.
- [N-U05-211] Purchase requests are created with elevated rights because salespeople may lack purchasing rights, and lines created from expenses never generate purchase requests.
- [N-U05-212] The purchase order origin lists every order that contributed to it.
- [N-U05-213] For a product sold as a kit, the delivered quantity is derived from the delivery of its components; if no component structure matches the product it is all-or-nothing.
- [N-U05-214] Manufacturing orders raised for an order line keep the link to the order line, finished-product movements are linked to the line, and a backorder of a manufacturing order keeps the link.
- [N-U05-215] Orders display the first-level manufacturing orders that are not cancelled.
- [N-U05-216] On confirmation, service lines tracked as project or task create or link a project and a task; when the order is cancelled, reset and reconfirmed they reuse the existing ones.
- [N-U05-217] Service billing policies map to the two basic billing bases; time-based services take delivered quantity from recorded time on the project, milestone-based ones from reached milestones, and prepaid services raise an upsell activity when time exceeds a threshold of the prepaid quantity.
- [N-U05-218] When invoices are created, recorded time not yet billed in the chosen period is linked to the invoice; posting a credit note releases the time of the credited invoice.
- [N-U05-219] The invoice line for a service inherits the analytic account of its project or task when the order line has no analytic distribution.

### STATE

- [N-U05-220] A purchase request generated from an order starts as a draft purchase line on a draft purchase order and then follows the purchasing process independently.

### OPTIONALITY

- [N-U05-221] The subcontract flag is set per product and per company; without the flag no purchase request is created.
- [N-U05-222] The project field on an order can pre-select the project that receives tasks for lines tracked as task in project.

### DEPENDENCY

- [N-U05-223] The crm, purchase, manufacturing, project and timesheet areas each own their documents; the sales layer only stores links and reacts to events.
- [N-U05-224] Orders for goods that come from vendors by dropshipping or from replenishment need the purchase and warehouse integration module, which was only noted.

### CONSTRAINT

- [N-U05-225] A purchase request cannot be generated when no vendor is defined for the product; the user must define one.
- [N-U05-226] The project selected on an order must allow billing and must not be a template.

### RISK

- [N-U05-227] Lowering ordered quantity never reduces the purchase request, so over-purchase must be corrected manually.
- [N-U05-228] The expected revenue of an opportunity only ever increases from orders and is ignored for orders in a foreign currency.
- [N-U05-229] Because purchase generation runs with elevated rights, a salesperson can trigger vendor purchase documents that the salesperson could not create directly.

### UNKNOWN

- [N-U05-230] The effect of cancelling an order on the generated project, tasks and timesheets was not found in the studied sales logic and is left to the project area.
- [N-U05-231] How the vendor is chosen when several vendors match, beyond taking the first by priority, depends on the purchasing area and was not exercised.

## CAP-U05-09 Roles, record rules, multi-company scope and scheduled behavior

### WHAT

- [N-U05-232] Access to orders, invoicing from orders and delivery links is governed by role-based permissions, ownership rules that limit salespeople to their own orders unless they hold the all-orders role, company isolation rules, and a small set of scheduled jobs.

### WHY

- [N-U05-233] Salespeople must be able to create and bill orders without seeing or editing accounting records they are not responsible for, and each company's orders must stay separate.

### BUSINESS RULE

- [N-U05-234] A salesperson can read, change and create orders and order lines, can delete order lines subject to business checks, but cannot delete orders; a sales manager can delete orders.
- [N-U05-235] By default a salesperson sees only orders assigned to them or to nobody, and only invoices raised for their own orders or without a salesperson; holders of the all-orders role see everything of that kind.
- [N-U05-236] Accountants with invoicing rights may read and change orders and lines but not create them; read-only accounting users may only read; portal customers may only read their own orders.
- [N-U05-237] Salespeople have read-only access to journal entries and journal items, so invoices are created from orders with elevated rights rather than by direct creation.
- [N-U05-238] Warehouse users may read and change orders and lines to record delivery effects; salespeople may create and change transfers and stock movements and read warehouses and locations; sales managers may also delete movements and manage routes and rules.
- [N-U05-239] Billing and mass-cancel helper windows are private to the user who opened them.
- [N-U05-240] Orders and order lines are visible only for the companies the user is currently working in.
- [N-U05-241] Locking confirmed orders is an optional company-wide feature; once an order is locked its key line fields cannot be edited, it cannot be cancelled and no new deliveries are requested, but it can still be billed and delivered; only the sales manager sees the unlock action.
- [N-U05-242] Invoices raised from orders are created for the order's company, and orders of different companies are never merged on one invoice.
- [N-U05-243] A product restricted to one company cannot already be used on orders of another company; products on an order must belong to the order's company or its branches.
- [N-U05-244] Online payment transaction records are fully visible to every salesperson regardless of the payment ownership rules.

### STATE

- [N-U05-245] The automatic invoice-sending job exists but is switched off until the automatic invoicing option is turned on; turning the option off, or removing its stored value, switches the job off again, and installing the sales module re-synchronises it.

### OPTIONALITY

- [N-U05-246] Automatic invoicing creates and posts an invoice when an online payment completes and then emails it; it is offered only when the default billing basis is ordered quantity and online payment is required for confirmation, and switching the default billing basis away from ordered turns it off.
- [N-U05-247] A separate job sends queued order emails and is likewise switched on only by its own option; both options are stored settings rather than job flags edited directly.

### DEPENDENCY

- [N-U05-248] The automatic invoicing job depends on the payment module's transactions and on the invoice sending feature of the accounting module, which has its own always-on job for the general invoice queue.
- [N-U05-249] Roles themselves are defined in the sales, accounting, warehouse, project and purchasing areas; the sales area adds optional feature roles for locking, discounts, warnings and pro-forma invoices.

### CONSTRAINT

- [N-U05-250] The invoice-sending job only considers completed, post-processed transactions of confirmed orders with at least one unsent posted invoice from the last two days, and does nothing if automatic invoicing is not enabled.
- [N-U05-251] Customer invoices cannot be created from an order by a user who has neither the right to create invoices nor the right to change the order; the action then returns nothing without an error.
- [N-U05-252] Errors are raised for deleting a confirmed order, cancelling a locked order, changing the pricelist of a confirmed order, deleting a confirmed order line, changing a line's product after invoicing or delivery, editing protected fields of a locked order, and invoicing with nothing to bill.

### RISK

- [N-U05-253] In the restored configuration the feature roles for locking, line discounts, warnings and pro-forma invoices are enabled for all internal users, which changes day-to-day behavior relative to a default installation.
- [N-U05-254] The mass-cancel action works on any selected order for any user allowed to open it and does not apply the lock check, so a locked order can be cancelled through it.
- [N-U05-255] The unlock and lock actions have no permission check in the logic itself; the restriction to the sales manager exists only in the screen layout.
- [N-U05-256] Because invoice creation from an order uses elevated rights, record rules and field access of the accounting area do not constrain what a salesperson can bill from an order.

### UNKNOWN

- [N-U05-257] Whether triggering the invoice-sending job runs it while it is switched off could not be determined without running the system.
- [N-U05-258] The effective group memberships of real users are outside this study; only the role definitions and the restored configuration were examined.

