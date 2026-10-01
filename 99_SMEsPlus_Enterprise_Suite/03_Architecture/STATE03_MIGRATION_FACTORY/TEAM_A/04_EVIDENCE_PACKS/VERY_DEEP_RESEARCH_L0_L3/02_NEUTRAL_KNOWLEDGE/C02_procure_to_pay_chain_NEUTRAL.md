# C02 procure-to-pay chain - Neutral Knowledge (clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source product: Odoo 19 Community (named once, here). Written as business and process knowledge; no technical identifiers.
> Linked to the restricted evidence file through the statement identifiers in square brackets.
> Scope: the chain from request for quotation to settled vendor bill across purchasing, receiving, valuation, invoicing and payment, as configured and as a rule set.


## CAP-C02-01 Happy path from request for quotation to a settled vendor bill

### WHAT

- [N-C02-001] The procure-to-pay chain runs from a request for quotation to a settled vendor bill: a binding purchase order, then a receipt of goods, then a vendor bill, then a payment, then the reconciliation of that payment to the bill. Each document stays linked to the order line it came from.

### WHY

- [N-C02-002] Each hand-off keeps the order line as the common reference so that what was ordered, what arrived, what was billed and what was paid can be compared line by line.

### BUSINESS RULE

- [N-C02-003] A new request for quotation receives its reference from a company-independent numbering series at creation time.
- [N-C02-004] Sending or printing a request marks a draft request as sent; this step is optional because a draft request can also be confirmed directly.
- [N-C02-005] Confirming a quotation refuses any product line that has no product, validates the analytic distribution only when the confirm button asks for it, and silently skips orders that are not in the request or request-sent state.
- [N-C02-006] Confirming an order registers the vendor in the product's vendor list when that vendor is not yet listed and the product has at most ten vendors; the new vendor line takes the order price, a minimum quantity of one and a lead time of zero days, and is written regardless of the user's own rights.
- [N-C02-007] With single-step approval every confirmed order is approved immediately. With two-step approval an order is approved immediately when its total including taxes is strictly below the company threshold or when the confirming user holds the purchasing administrator role; otherwise it waits in a to-approve state.
- [N-C02-008] Approval writes the purchase-order state and the confirmation date, and locks the order when company policy says confirmed orders are not editable.
- [N-C02-009] A receipt is created when the order is approved, not when it is confirmed, and only if at least one line is a goods product; orders that contain only services create no receipt.
- [N-C02-010] The receipt is created under the system identity, one planned move per goods line carrying the order line link, the order price converted to the company currency, the planned date, the order references and the vendor location as source.
- [N-C02-011] Receipt moves are confirmed and made ready at once, because stock coming from a vendor location needs no reservation, and the receipt shows ready to process.
- [N-C02-013] Validating the receipt marks its moves done, flags the purchase order as acknowledged by the vendor, records the received quantity on each order line from the done moves, and refreshes the quantity still to bill and the order's billing and receipt statuses.
- [N-C02-014] With periodic valuation and standard cost, validating a receipt stores a value on the move but books no journal entry, because entries at validation require perpetual valuation and a valuation account on a stock location.
- [N-C02-015] A vendor bill is created from order lines with the quantity to bill as its quantity, the order price converted to the bill currency, the order taxes, the discount, and a link to each order line; bills are grouped by company, vendor and currency.
- [N-C02-016] Bills can be created from the list of orders through a create-bills action, from an uploaded vendor document, from the auto-complete selector on a vendor bill, or from the bill matching screen; the order form itself offers an upload action and a matching screen but no create-bill button in this revision.
- [N-C02-017] When the bill created from an order has a negative total it is converted to a vendor credit note.
- [N-C02-018] Under periodic valuation a bill line is booked to the product's expense account; under perpetual valuation a bill line for a tracked goods product is booked to the stock valuation account.
- [N-C02-019] Posting a bill requires the invoicing role, a bill date, a vendor, no archived account or journal and a non-negative total; a posting date inside a locked period is moved to the first open date rather than refused.
- [N-C02-020] Posting a bill assigns its number, creates its journal entry and tax lines, raises the vendor's rank, and re-values receipts linked to the same order lines from the posted bill.
- [N-C02-021] A payment can be registered only for a posted bill that is not blocked; the wizard creates the payment, posts its journal entry on an outstanding payments account and reconciles it to the payable line of the bill.
- [N-C02-023] The purchase order has no payment status: settling the bill changes neither its status nor its quantities.

### STATE

- [N-C02-022] In this edition a bill fully matched by a posted payment shows paid immediately, with no separate in-payment status; the payment moves from in process to paid once all bills it settles are paid.
- [N-C02-024] Order states in sequence are request, request sent, to approve, purchase order and cancelled; locking is a separate yes-or-no flag and not a state.
- [N-C02-025] After the receipt is validated the receipt is done and the order shows partially or fully received; after bill creation the bill is a draft that already counts as billed; after posting it is posted and not paid; after payment and reconciliation it is paid and the order shows fully billed once nothing remains to bill.

### OPTIONALITY

- [N-C02-026] Two-step approval, order locking, vendor reminders, the bill-control policy per product and the valuation mode are configuration choices; the restored configuration uses two-step approval above five thousand with locking on confirmation, one-step receiving, periodic valuation and standard cost.
- [N-C02-027] The restored configuration holds only service products, so no receipt would be created for any existing product and received quantities would be entered manually.
- [N-C02-032] Under perpetual valuation the picture changes: bills are booked to the stock valuation account, receipts and deliveries create entries only where a stock location carries a valuation account, and standard-cost price differences arise only when the anglo-saxon switch is on; none of this is active in the restored configuration.

### DEPENDENCY

- [N-C02-028] The chain depends on purchasing, inventory, inventory valuation, invoicing and payment functions together; a service-only order needs only purchasing and invoicing.

### CONSTRAINT

- [N-C02-012] Receipt creation is refused when the vendor has no vendor stock location configured, which aborts the approval step.

### RISK

- [N-C02-029] Approval, receiving, billing and payment are open to overlapping roles, so one person can carry an order from request to payment unless roles are kept apart by configuration.
- [N-C02-030] Nothing in the chain forces the bill to wait for the receipt: the order's billing status is informational and bill posting does not consult the order.

### UNKNOWN

- [N-C02-031] The complete sequence, its amounts and its final states were derived by reading source only and have not been executed.
- [N-C02-033] Amounts and journal entries under perpetual valuation were not executed and require a runtime test.

## CAP-C02-02 Bill control variants: billing on ordered quantity versus received quantity

### WHAT

- [N-C02-034] Bill control decides how much of an order line may be billed before the goods have arrived: on the quantity ordered or on the quantity received. The choice is made per product by a purchasing administrator.

### WHY

- [N-C02-035] The policy lets a business pay promptly for services and pre-agreed deliveries while holding goods billing back until receipt, and it keeps one billable quantity figure per order line for both document flows.

### BUSINESS RULE

- [N-C02-036] Services always default to billing on ordered quantity; goods default to billing on received quantity unless the company default is changed, and the policy can be edited per product by the purchasing administrator role only.
- [N-C02-037] The quantity still to bill is the ordered quantity minus the billed quantity under the ordered policy, or the received quantity minus the billed quantity under the received policy, and it is zero while the order is not in the purchase-order state.
- [N-C02-038] The billed quantity adds every bill line of every non-cancelled bill, including draft bills, and subtracts every credit-note line, converted to the order line's unit.
- [N-C02-040] Nothing blocks creating or posting a bill before goods are received: under the ordered policy the whole ordered quantity is billable from approval, and under the received policy a bill created before receipt simply carries zero quantities.
- [N-C02-041] Auto-completing a bill from an order copies every order line not yet on the bill without testing the quantity to bill, so lines with zero billable quantity appear on the bill.
- [N-C02-042] Receiving more than ordered is not blocked and the received quantity is not capped at the ordered quantity; under the received policy the quantity to bill can therefore exceed the ordered quantity.
- [N-C02-043] Receiving less than ordered raises a backorder question when the operation type asks for it: a follow-up receipt is created for the remainder, or the remainder is cancelled when the type never creates backorders or the user declines.
- [N-C02-044] The order's receipt status follows only the states of its receipts, so an order whose short receipt was closed without a backorder shows fully received although less than the ordered quantity arrived.
- [N-C02-045] Bill lines are tied to order lines and not to individual receipts, so alignment between a particular receipt and a particular bill exists only through cumulative quantities on the order line.
- [N-C02-046] The bill matching screen lists purchase-order lines that still have quantity to bill and unlinked draft or posted vendor-bill lines of the same vendor; matching links a bill line to an order line, or creates a draft bill from selected order lines, without comparing prices or quantities.
- [N-C02-047] Incoming electronic or scanned vendor bills are matched to open orders by order reference or vendor reference and by total within a tolerance of two hundredths of a currency unit, or by vendor and total as a last resort.
- [N-C02-048] When the ordered quantity of a goods line is reduced below the quantity already billed, an activity is logged on the first bill suggesting a refund request to the vendor.
- [N-C02-049] Once any quantity is billed, the order line's price and discount become read-only in the form and automatic price re-derivation is skipped for that line.

### STATE

- [N-C02-039] The order's billing status is nothing to bill unless the order is a purchase order; it is waiting for bills when any line has a non-zero quantity to bill, and fully billed when all lines are zero and at least one bill exists.

### OPTIONALITY

- [N-C02-051] The policy is a per-product choice; the restored configuration holds only service products, all on the ordered policy, so every bill would be billable in full from approval.

### DEPENDENCY

- [N-C02-055] Per-receipt billing alignment, the bill-before-receipt anomaly and cross-receipt quantity reconciliation are only partly delivered: the system keeps cumulative quantities per order line and informational statuses, with no anomaly flag.

### CONSTRAINT

- [N-C02-050] The strict control that refuses payment until goods are received is an optional extension that is not part of the Community distribution; only the bill-control policy and the matching screens are available.

### RISK

- [N-C02-052] A payable can be recognised before any goods arrive, a bill can be posted for more than was received, and over-receipt inflates the billable quantity under the received policy; the control must be procedural unless the optional extension is added.
- [N-C02-053] Zero-quantity bills can be produced from orders with nothing received; whether the form lets users post them was not verified.

### UNKNOWN

- [N-C02-054] Whether the bill form accepts posting of zero-quantity lines, and what the interface does on over-receipt, needs a runtime check.

## CAP-C02-03 Return of received goods and vendor refund chain

### WHAT

- [N-C02-056] Returning goods and refunding the vendor are two separate documents: a return receipt sends goods back to the vendor and corrects the received quantity, while a vendor credit note corrects the payable and the billed quantity. Neither creates the other automatically.

### WHY

- [N-C02-057] Keeping the physical correction and the financial correction separate lets a business return goods before it is billed, after it is billed, or take a price refund without any physical return, while the order line keeps one received quantity and one billed quantity.

### BUSINESS RULE

- [N-C02-058] A return can be started only from a completed receipt, one receipt at a time, and needs at least one non-zero quantity; the return is created confirmed and ready, goes back to the vendor location through the operation type's return type, and keeps a link to the receipt it reverses.
- [N-C02-059] Each return line carries a switch named update quantities on the order, on by default: when it is on, or when the return has no originating move, the quantity returned reduces the order line's received quantity once the return is completed; when it is off the received quantity is left unchanged.
- [N-C02-060] The return keeps its link to the purchase order line because the return movement is created as a copy of the receipt movement, and the vendor is carried onto the return when the return type is outgoing; a purchasing-side routine that would walk the movement chain to find the order line exists but cannot be reached in this revision.
- [N-C02-061] A completed return is an outgoing valued movement: it leaves stock at the product's cost under the costing method (standard price, running average or oldest receipts), not at the price on the vendor bill, and with periodic valuation it creates no journal entry.
- [N-C02-062] Under the received-quantity policy, returning goods that were already billed makes the quantity to bill negative, so the order shows waiting for bills; creating the bill then produces a vendor credit note for that quantity.
- [N-C02-063] Returning goods before any bill exists simply lowers the billable quantity under the received policy; nothing negative appears and no credit note is needed.
- [N-C02-064] A credit note can be created from a posted bill with the credit-note wizard, which keeps the order-line links on the copied lines, or from the order through the create-bills action when the quantity to bill is negative.
- [N-C02-065] Credit-note lines subtract from the billed quantity as soon as the credit note exists, even as a draft, so the quantity to bill rises again and the order returns to waiting for bills for that quantity under both policies.
- [N-C02-066] Posting a credit note created by the credit-note wizard reconciles it automatically with the unreconciled payable lines of the original bill; a bill already paid is not touched, so the credit remains open for the vendor relationship; a credit note created from the order has no link to the bill and is not reconciled automatically.
- [N-C02-067] A refund without a return leaves the goods in stock and the received quantity unchanged while lowering the billed quantity; the order therefore shows quantity waiting to be billed that the business does not intend to bill.
- [N-C02-068] A posted credit note lowers the bill-derived value of the receipt; when the credited quantity cancels the billed quantity the receipt value falls back to the order price.

### STATE

- [N-C02-069] A return is a picking of the order, so while it is open an order whose receipts were all done shows partially received, and the arrival date counts only receipts that do not go back to a vendor.
- [N-C02-070] Return flow: completed receipt, then return created and ready, then return completed; the received quantity falls only at the last step and only when the update switch is on; the credit note follows its own draft, posted and reconciled path.

### OPTIONALITY

- [N-C02-071] The update switch per return line, the return type of the receipt type, and the choice between the credit-note wizard and the create-bills action decide which combination of physical and financial correction happens.

### DEPENDENCY

- [N-C02-072] The refund leg depends on purchasing and invoicing; the return leg depends on inventory and, for the update switch and valuation, on inventory valuation.

### CONSTRAINT

- [N-C02-073] The return quantity is not capped at the quantity received by the wizard, and a return of goods from several receipts or lots cannot be done in one return.

### RISK

- [N-C02-074] With the update switch off the order and the stock diverge; a credit note issued afterwards makes the order show quantity waiting for bills; goods returned and credit noted but not linked to the order line are invisible to the order.
- [N-C02-075] A credit note for a bill that was already paid leaves an open vendor credit that must be applied or refunded by a separate action.

### UNKNOWN

- [N-C02-076] Returns across several receipts or lots, a return of a return, a dropship return, and the arithmetic of a credit note created from a partly returned order were not executed and need a runtime test.

## CAP-C02-04 Cancellation at each stage of the chain

### WHAT

- [N-C02-077] Cancellation in the procure-to-pay chain is stage dependent: each module permits or refuses it differently, and each stage leaves its own residue of documents that must be cleaned up separately.

### BUSINESS RULE

- [N-C02-078] A request or purchase order can be cancelled from the request, request-sent, to-approve or purchase-order states, unless it is locked or has a bill that is neither draft nor cancelled; the cancel button is hidden while an order is locked, and a bulk cancel action in the list has no role restriction.
- [N-C02-079] Cancelling an order cancels its open receipts and unfinished moves; completed receipts stay completed and only receive a note; downstream demand created for the order is cancelled when the line propagates cancellation, otherwise it is reset to be served from stock.
- [N-C02-080] The stock-side cancellation is performed before the purchasing checks for lock and bills, so a refusal for a locked order or a live bill relies on the whole action being rolled back.
- [N-C02-081] Unlocking an order is offered only to the purchasing administrator role in the form, but the underlying action can be called by any user who can write the order.
- [N-C02-082] Only a cancelled order can be deleted, and a cancelled order can be set back to draft without clearing its lock flag, confirmation date or acknowledgement.
- [N-C02-083] When a cancelled order is set to draft and confirmed again, a new receipt is created for the quantity not already received, because cancelled moves do not count and completed receipts do.
- [N-C02-084] Cancelling an order that was generated for a sales order posts a warning activity on that sales order.
- [N-C02-085] A draft vendor bill does not block cancelling the order: the bill stays linked and keeps counting as billed even though the order is no longer a purchase order and its quantity to bill is zero.
- [N-C02-086] A posted bill blocks cancelling the order; the bill must first be reset to draft and cancelled. Resetting is refused only for hashed, exchange-difference or cash-basis entries, and there is no check for payments, so a paid bill can be cancelled.
- [N-C02-087] Cancelling a bill removes its reconciliations: payments applied to it stay posted but become unapplied vendor credits, and they must be cancelled or re-applied by a separate action; a payment is cancelled as its own document.
- [N-C02-088] A receipt can be cancelled only before it is completed; a completed receipt is reversed only by a return, and a completed move can never be cancelled.
- [N-C02-089] A validated landed cost cannot be cancelled; the way back is a new landed cost with negative amounts.

### STATE

- [N-C02-090] Stage outcomes: request stage cancels freely; to-approve cancels freely with no receipt; approved and unlocked cancels with open receipts cancelled; approved and locked is refused; partly received cancels the open remainder and keeps the received goods; draft bill permits cancel and keeps the bill; posted or paid bill refuses until the bill is cancelled.

### OPTIONALITY

- [N-C02-091] Order locking on confirmation, the propagate-cancel setting on lines and rules, and the restrictive audit-trail option on the company decide how hard cancellation is; in the restored configuration locking is on and the audit-trail option is off.

### DEPENDENCY

- [N-C02-092] A full unwind needs purchasing, inventory, invoicing and payment functions in the right order: payment, then bill, then order, with returns for received goods.

### CONSTRAINT

- [N-C02-093] An order that carries a posted bill or a locked flag cannot be cancelled; a done move cannot be cancelled; a validated landed cost cannot be cancelled.

### RISK

- [N-C02-094] Residue after cancellation includes vendor lines auto-added at confirmation, draft bills still linked to a cancelled order, completed receipts whose order is cancelled, unapplied payments after a bill is cancelled, and landed costs that cannot be undone.
- [N-C02-095] Because the draft bill of a cancelled order keeps its links, posting it later is not prevented by any check that was found; this was not exercised.

### UNKNOWN

- [N-C02-096] Whether the whole cancel action is rolled back when the lock or bill check refuses after the stock side already acted, whether reset-to-draft of an order with cancelled receipts recreates them as inferred, and the effect of cancelling a bill that has applied payments were not executed.

## CAP-C02-05 Partial flows: partial receipt, partial bill, partial payment and changes after approval

### WHAT

- [N-C02-097] Real purchases rarely flow in one piece: goods arrive in several deliveries, bills cover part of an order, payments cover part of a bill, and prices or quantities change after approval. Each partial flow leaves a different combination of states across the order, receipts, bills and payments.

### WHY

- [N-C02-098] The order line keeps cumulative received and billed quantities so that every partial delivery, partial bill or later change can be absorbed without creating a new order.

### BUSINESS RULE

- [N-C02-099] Validating a receipt with less than the demanded quantity asks whether to create a backorder; accepting creates a new receipt for the remainder that keeps the link to the same order line, declining cancels the remainder, and the type can be set to always or never decide.
- [N-C02-100] The received quantity of an order line is the cumulative total of completed receipt moves of that line, so successive backorders add up until the ordered quantity is reached or exceeded.
- [N-C02-102] Partial billing works by editing the quantity on the draft bill or by creating bills repeatedly: each new bill proposes only the remaining quantity to bill, the billed quantity accumulates across bills, and the order stays waiting for bills until nothing remains.
- [N-C02-103] Billing more than ordered or received is not blocked; the quantity to bill then goes negative and the order keeps showing waiting for bills.
- [N-C02-104] A payment smaller than the bill's open amount is accepted with the difference kept open by default; the bill then shows partially paid and the remaining amount stays open until another payment or credit is applied.
- [N-C02-106] After approval the ordered quantity of a line can be changed: an increase adds quantity to the open receipt or creates a new one when none is open and the ordered quantity exceeds the received quantity; a decrease reduces open moves or turns into a planned return, logs an activity for the people downstream, and, if the new quantity is below the billed quantity, logs a refund suggestion on the first bill.
- [N-C02-107] After approval a changed price updates the price of open receipt moves and re-values the value of every valued move of the line, including completed receipts, from the best evidence available: a posted bill first, otherwise the current order price.
- [N-C02-108] No code was found that sends an already approved order back to the to-approve state when its total is raised above the approval threshold, so two-step approval is not applied again after approval.
- [N-C02-109] The lock on a confirmed order is enforced in the interface only; the underlying write was not found to refuse changes to a locked order.
- [N-C02-110] Changing the order price or quantity does not change bills that already exist; the order line's price and discount become read-only in the form once a bill exists, but the quantity does not.
- [N-C02-111] Setting a quantity of zero in the product catalogue on an order that is no longer a request does not delete the line but sets its ordered quantity to zero.
- [N-C02-112] A vendor can propose new delivery dates from the portal: the dates are updated on the order lines and on open receipt moves, an activity is logged for the buyer, and a completed receipt keeps its date.

### STATE

- [N-C02-101] The order's receipt status is not received while no receipt is completed, partially received once any receipt is completed while another is still open, and fully received when every receipt is completed or cancelled, irrespective of quantities.
- [N-C02-105] Bill payment states in sequence are not paid, partially paid and paid; blocked prevents registering payments, and reversed appears when only credit notes settle the bill.

### OPTIONALITY

- [N-C02-113] The backorder policy of the receiving operation type, the bill-control policy per product, the payment difference handling in the payment wizard and the order lock policy determine how partial flows behave.

### DEPENDENCY

- [N-C02-114] Partial flows depend on inventory for backorders, on purchasing for cumulative quantities and status, and on invoicing and payment functions for partial bills and payments.

### RISK

- [N-C02-115] The order's receipt status can show fully received while the ordered quantity has not arrived, and its billing status can show waiting for bills after an over-bill or a credit note; the statuses summarise documents, not quantities.
- [N-C02-116] Re-valuing completed receipts from a later order-price edit can change the recorded value of goods already received before any bill exists; with standard cost the stock total is unaffected but the move value changes.

### UNKNOWN

- [N-C02-117] Behaviour of repeated backorders with lots or several units of measure, of a quantity decrease below the received quantity, and of the order lock under direct writes needs a runtime check.

## CAP-C02-06 Replenishment-driven procurement, direct shipment and landed costs

### WHAT

- [N-C02-118] A stock need such as a reordering rule, a make-to-order demand, a manual replenishment or a sales order for direct shipment can be turned into a draft request for quotation automatically, either as a new request or by extending an existing one.
- [N-C02-131] A landed cost adds freight, customs or similar charges to the value of goods already received by allocating the charges over the moves of selected receipts.

### WHY

- [N-C02-119] Automatic requests keep stock between planned levels while leaving the commitment to a person: the system proposes, the buyer confirms.

### BUSINESS RULE

- [N-C02-120] The vendor for a need is the one named on the reordering rule or procurement; otherwise the best matching line of the product's vendor list by quantity, date and unit; if none matches, a vendor line without a valid price is used as a fallback.
- [N-C02-121] When no vendor exists, a need coming from a reordering rule fails with a procurement exception and an activity on the product, while any other need is detached: its downstream demand is cancelled or reset to stock and the responsible person is notified.
- [N-C02-122] An existing draft request is extended when it has the same vendor, operation type, company, buyer and currency and passes the vendor's grouping policy: on order groups only needs with the same references, daily and weekly groups by expected arrival, always groups all; direct-shipment needs always group per sales reference.
- [N-C02-123] Needs for the same product, unit, cancel policy and description are merged into one line: the quantity is added and the vendor price is re-selected for the total quantity; otherwise a new line is added with the vendor price, vendor product name, planned date and links to the downstream demand.
- [N-C02-124] The planned receipt date is the need date; the order date is the receipt date minus the vendor's lead time; the company's days-to-purchase setting adds to total lead time, and a product with no vendor adds a year in forecasts; a weekly vendor policy shifts the date to the vendor's preferred weekday.
- [N-C02-125] Replenishment creates only draft requests, under the system identity, so nothing is committed and no receipt exists until a buyer confirms and the order is approved.
- [N-C02-126] Quantities on requests that are draft, sent or waiting for approval count as incoming when a reordering rule decides how much to order, which prevents duplicate requests.
- [N-C02-127] A daily scheduler processes automatic reordering rules in batches, isolating failures per batch and logging activities for failed products, then tries to reserve confirmed moves and merges duplicate stock records.
- [N-C02-129] For direct shipment the operation type is a dropship type, the destination is the customer address, requests are never merged across sales references, and one receipt per sales order is created when a request covers several sales orders; completed direct shipments add to the received quantity but create no stock entry.
- [N-C02-130] Bill lines for direct-shipped goods are not eligible for stock accounts, so they stay on the expense account and no price-difference lines arise.
- [N-C02-132] A landed cost is created from a vendor bill line flagged as a landed cost (negative for credit notes), is split over eligible receipt moves by equal share, quantity, current cost, weight or volume with the rounding remainder on the last allocation, and is validated to be done.
- [N-C02-134] On validation a journal entry is booked only for perpetual-valuation products and only for the share still on hand: the stock valuation account is debited and the cost line's account is credited, reversed for negative amounts; with no such products the cost is done without an entry.
- [N-C02-135] After validation every allocated move is re-valued with the extra cost and the product cost is recomputed; a validated landed cost cannot be cancelled and is corrected by a negative landed cost.

### OPTIONALITY

- [N-C02-137] The restored configuration has no reordering rules, no vendor lines, no landed-cost products, a buy route that does not propagate cancellation under one-step receiving, an active daily scheduler, and an unset days-to-purchase value.

### DEPENDENCY

- [N-C02-138] Replenishment depends on inventory rules and scheduler, purchasing for the request, the product vendor list, and optionally sales for direct shipment and inventory valuation for landed costs.

### CONSTRAINT

- [N-C02-128] The buy route can be used for a product only if the product has at least one vendor line, and the operation type of the order must belong to the warehouse of the reordering rule or downstream demand.
- [N-C02-133] Landed costs can be applied only to receipts of products costed by first-in-first-out or average cost; with standard cost the action fails with an error, so in the restored configuration no landed cost can be applied.
- [N-C02-136] Landed costs are maintained only by the stock administrator role, and the create-landed-cost action on a bill additionally needs the invoicing role; no check ties the landed cost to the bill's posting or to the bill's receipts.

### RISK

- [N-C02-139] System-identity creation hides who triggered the request; a vendor line with no price can produce a quotation with a zero price; landed costs on standard-cost products silently cannot be applied until an error is raised.

### UNKNOWN

- [N-C02-140] Scheduler runs with real rules, grouping policies, vendor fallbacks, multi-sale dropship receipts and the arithmetic of landed-cost allocation were not executed.

## CAP-C02-07 Company data scope and role separation across the chain

### WHAT

- [N-C02-141] Data scope decides which company's documents a user sees and creates along the chain; role separation decides who may create the order, approve it, receive the goods, enter and post the bill and pay it.

### WHY

- [N-C02-142] Company scope keeps ledgers and stock separate, while role separation is the control that stops one person from ordering, receiving, billing and paying the same purchase.

### BUSINESS RULE

- [N-C02-143] Orders, order lines, receipts, moves, bills, journal items and payments are each filtered by the user's allowed companies through company rules, and orders may not contain products that belong to a company outside the order company's branch tree.
- [N-C02-144] Order creation, receipt creation, bill creation and valuation use the order's company explicitly rather than the user's current company, so documents follow the order across companies.
- [N-C02-145] The approval threshold is converted from the currency of the user's current company to the order currency, so an approval performed from a different company than the order's uses that other company's currency.
- [N-C02-146] The purchase order numbering series is shared by all companies, while bill and payment numbers follow each journal; the receiving operation type and its numbering follow the warehouse of the order.
- [N-C02-147] A payment can cover bills of sibling companies only when the user has access to the parent company, and the payment is then made as the parent company; lines of different root companies are refused.
- [N-C02-149] Roles that act on the chain are: purchase user and purchase administrator for orders, stock user and stock administrator for receipts and landed costs, and invoicing, full-accounting and accounting administrator for bills, payments and reconciliation; the administrator roles imply the lower ones.
- [N-C02-150] Only the purchasing administrator may approve an order waiting for approval and unlock a locked order in the interface; the approval check in the system itself requires that role only for orders at or above the threshold.
- [N-C02-151] Confirmation and cancellation of orders are not restricted to a role beyond the ability to write orders; the underlying actions of lock, unlock, approve, cancel and set-to-draft carry no role check.
- [N-C02-152] The validate button on a receipt is offered to the stock user role, but purchase users can create, write and delete receipts and create and write moves, and invoicing users can create and write receipts and moves.
- [N-C02-153] Purchase users can create, edit and delete vendor bills and their lines within the vendor-bill scope, but posting a bill, reversing it, registering a payment and reconciling require the invoicing role.
- [N-C02-154] One role, invoicing, covers entering bills, posting them, registering payments, posting payments and reconciling, with no separate approval step for payments in this edition.
- [N-C02-155] Only the purchasing administrator maintains vendor price lines directly, yet confirming any order adds a missing vendor line under elevated rights.
- [N-C02-156] Merging requests, creating accruals and creating landed costs are offered to different roles: merging to the invoicing role, accrual entries to the full-accounting role, landed costs to the stock administrator together with invoicing.

### OPTIONALITY

- [N-C02-162] The restored configuration has two seeded administrator accounts in each administrator group and no direct members in the user groups, so role separation exists only as configuration to be done.

### DEPENDENCY

- [N-C02-163] Role separation depends on the group structure of purchasing, inventory and accounting together; the groups are defined in three different areas and must be assigned jointly.

### CONSTRAINT

- [N-C02-148] The restored configuration has a single company, so none of the multi-company behaviour can be observed there and every statement about it comes from reading source.

### RISK

- [N-C02-157] Segregation-of-duties gap: a user holding purchase user and invoicing roles can create an order below the approval threshold, trigger its receipt, create and post the bill and pay it; nothing in the chain prevents this combination.
- [N-C02-158] Segregation-of-duties gap: controls on approval, unlock and validation sit mainly in the interface, so any user with write access to the underlying records can call the same actions programmatically.
- [N-C02-159] Segregation-of-duties gap: the invoicing role can edit orders and order lines and create or edit receipts and moves, which lets the person who bills also change what was ordered or received.
- [N-C02-160] Segregation-of-duties gap: a purchasing administrator who creates an order can also approve it, because the threshold is waived for that role.
- [N-C02-161] Records created by the system identity for receipts and replenishment hide the requesting user, and vendor lines added at confirmation bypass the purchasing administrator restriction on vendor data.

### UNKNOWN

- [N-C02-164] Effective permissions of individual users, multi-company and branch behaviour, whether the interface hides every action that the underlying action allows, and access rules for transient wizards were not exercised.

## CAP-C02-08 Accounting, stock, audit, tax and compliance implications across the chain

### WHAT

- [N-C02-165] Along the chain, records and entries arise at set events: ordering and approval create no accounting; receiving creates a stock movement and a stored value, and under periodic valuation no journal entry; posting the bill creates the numbered journal entry with expense, input tax and payable; payment creates its own entry and a reconciliation; period end creates the stock closing entry and optional accruals.

### WHY

- [N-C02-166] The chain separates the physical record, the commercial record and the financial record so that each can be audited on its own, and joins them through the order line and shared references.

### BUSINESS RULE

- [N-C02-167] With periodic valuation and standard cost, receiving goods books nothing to the ledger: stock value is carried on the moves, the bill is booked to expense, and the stock account is brought to the inventory value only by the period-end closing entry.
- [N-C02-168] The closing entry compares the inventory value at cost with the ledger balance of the stock valuation accounts and books the difference against a variation account; the company period is manual in the restored configuration, so the daily closing job does nothing and the closing is run on demand.
- [N-C02-170] The amount still to be billed at a chosen date can be accrued through an accrual action on orders, restricted to the full-accounting role: for each line it uses the product's bill-control policy, so the accrued quantity is ordered minus billed under the ordered policy and received minus billed under the received policy; the action posts an accrual entry against a liability account and a reversing entry on a later date, and logs a note on each order.
- [N-C02-171] A vendor bill receives its number when it is posted, from its journal's sequence; draft bills have none; the purchase journal in the restored configuration keeps a separate numbering for credit notes, and the order has its own series.
- [N-C02-172] When a journal restricts posted entries with a hash, each posted entry is added to a hash chain and can no longer be reset to draft or deleted; none of the restored journals uses this protection.
- [N-C02-173] Lock dates for fiscal year, purchases, taxes and a hard lock move the accounting date of a bill, payment or valuation entry to the first open date at posting instead of refusing it, and editing posted entries inside a lock is refused; a receipt's completion date cannot be edited into a locked fiscal period. None of the lock dates is set in the restored configuration.
- [N-C02-174] The company option for a restrictive audit trail forbids deleting entries once they have been posted and offers cancellation instead; the option is off in the restored configuration.
- [N-C02-175] Purchase VAT at seven percent is a tax line on the bill posted to an input-tax account that is flagged for tax closing, with a mirror line for credit notes.
- [N-C02-176] Thai withholding on purchases is modelled as ordinary negative-percentage taxes on the bill, one per rate and per payee type, posted at bill time to a liability account that is not flagged for tax closing; a separate payment-time withholding function exists in the distribution but is not installed.
- [N-C02-177] The bill date and the accounting date, not the receipt date, decide the tax period; no check compares the bill date with the receipt date.
- [N-C02-178] Audit traces include tracked changes on the order's vendor, buyer, status, lock, acknowledgement and untaxed amount, notes for added lines, ordered-quantity changes and received-quantity changes, an origin note on each receipt, a created-from note on each bill, and a value explanation on every valued receipt move that names its evidence: bill, order price, landed cost or manual adjustment.
- [N-C02-179] Analytic distribution on an order line is merged into the matching bill line; stock moves create analytic entries only when another module supplies a distribution.
- [N-C02-180] Under periodic valuation the stock value is quantity times standard cost regardless of the move values, so edits of the order price or the bill price after receipt change move values but not the stock total.

### OPTIONALITY

- [N-C02-181] Hash restriction, lock dates, audit-trail strictness, period type, valuation mode and the withholding function are configuration choices that decide how much of the above applies; the restored configuration leaves hash, locks and audit-trail strictness off.

### DEPENDENCY

- [N-C02-182] The accounting implications depend on invoicing for entries, numbering, lock dates and tax; on inventory valuation for values and closing; and on the Thai localisation for taxes in the restored configuration.

### CONSTRAINT

- [N-C02-169] A closing with something to book fails with an error when the company has no stock journal or no stock valuation account; the restored company has a valuation account but no stock journal.

### RISK

- [N-C02-183] Periodic valuation with expensed bills and no receipt entry leaves inventory unrecognised until the closing entry; cut-off errors arise at period end when goods are received but not billed, or billed but not received, unless the accrual action is used.
- [N-C02-184] With no hash, no lock dates, no strict audit trail and no receipt gate configured, posted entries can be changed or reset and the audit relies on notes and tracking alone.

### UNKNOWN

- [N-C02-185] Entries and amounts for perpetual valuation, sequence formats for the configured fiscal year, the effect of lock-date shifting on numbering and the Thai statutory reporting outcome were not executed or verified.

## CAP-C02-09 Consistency audit of the earlier module studies at their hand-off points

### WHAT

- [N-C02-186] The consistency audit compares what the earlier module studies state at the points where the purchasing, receiving, valuation, entry and payment studies meet, and checks those statements against the source: every disagreement, gap or inconsistent wording is listed with a classification.

### WHY

- [N-C02-187] A procure-to-pay description is only dependable if the hand-off statements of the separate studies agree with each other and with the product; a disagreement at a boundary is where business rules are most likely to be misdescribed.

### BUSINESS RULE

- [N-C02-188] A mechanical re-check of every recorded claim of the six studies found that all of their source pointers and anchor words are valid; the findings below are therefore about meaning, not about broken references.
- [N-C02-189] Confirmed contradiction: one study says that posting an entry dated inside a locked period is refused with an error, including stock closing and landed-cost entries; the entry-lifecycle study and the product both show that posting moves the date to the first open date, and only edits of already posted entries are refused.
- [N-C02-190] Confirmed contradiction: the receiving study lists resetting or cancelling a vendor bill as a trigger that re-values received goods; the product only re-values at posting, and cancelling or resetting a bill removes the stock-related cost lines of that bill but leaves the stored move values unchanged until another trigger occurs.
- [N-C02-191] Unresolved by the studies but resolved by reading: after a cancelled order is set back to draft and confirmed again, a new receipt is created for the quantity not yet received, because cancelled moves are not counted.
- [N-C02-192] Unresolved: the studies describe a create-bill step in the happy path, but the order form has no create-bill button in this revision; bills are created from the order list, from an upload action on the order, from the auto-complete selector in the bill, or from the matching screen, and an interface tour still refers to a button that does not exist.
- [N-C02-193] Unresolved gap: the purchasing study lists acknowledgement by the vendor through the portal or a button, while the receiving study shows that validating any receipt also acknowledges the order; the reminder logic depends on the combined picture.
- [N-C02-194] Unresolved gap: both the receiving and valuation studies describe how earlier receipts absorb billed quantity but omit that the source adds the quantity of earlier outgoing moves with a double negative, which looks like a sign slip whose effect needs a runtime test.
- [N-C02-195] Gap: the traceability from a lot or serial number to the purchase orders that received it is covered by neither the receiving study nor the lots study.
- [N-C02-196] Terminology: the word billed has three meanings across the studies: a billed quantity that counts draft bills, a billed value used for receipt valuation that counts only posted bills, and a paid status that follows reconciliation.
- [N-C02-197] Terminology: valuation wording is mixed across the studies and the control documents: a perpetual-valuation flag, automated valuation, the anglo-saxon switch and the company valuation mode are different things, and only the valuation mode and the product category setting decide whether stock entries exist.
- [N-C02-198] Terminology: the receiving study speaks of goods-received-not-invoiced exposure as if an interim receipt account existed; the valuation study shows there is no such account in this revision, and only a deprecated helper and the accrual action deal with received-not-billed amounts.
- [N-C02-199] Terminology: a retired completed state of the purchase order is still referred to by a dashboard filter, two list filters and the direct-shipment receipt logic; the first study noted one of them and the receiving study another, but none lists all.
- [N-C02-200] Unresolved: the purchasing study states as fact that a refusal by the lock or bill check aborts the cancellation, while the receiving study marks the same point as needing a runtime test because the stock side has already acted.
- [N-C02-201] Terminology: several existing function identifiers are claimed by more than one study for different slices, including reversal of received goods, valuation at receipt, landed cost, partial receipt and replenishment rules, and the partial matches for per-receipt billing and bill-before-receipt are labelled differently by the purchasing and receiving studies.
- [N-C02-202] Unresolved, partly resolved by reading: the payments study leaves open whether a payment reaches paid before bank matching; the source shows the payment becomes paid as soon as every bill it settles is paid, which in this edition is immediately after reconciliation.
- [N-C02-203] Gap: no earlier study owns the accrual action that books the amount still to be billed at a date; the valuation study lists it as a supporting item and the entry study read only its entry-creation calls.
- [N-C02-204] Gap: the price lookup that a vendor bill performs against the product's vendor list when a bill is typed without an order is described by the product study but not by the purchasing study.
- [N-C02-205] Gap: the purchasing study describes broad bill rights for purchase users without stating that posting a bill needs the invoicing role, which the entry study records.
- [N-C02-206] Unresolved, resolved by reading: the purchasing study doubts that the reminder job excludes service-only orders; the source compares a list of product types with a single-item list, so an order with several distinct service products is not excluded.
- [N-C02-207] Confirmed contradiction: the receiving study presents a purchasing-side routine as the way a return acquires its order-line link and vendor; the transfers study doubted it, and reading shows that the routine overrides a method that no longer exists on the return wizard and is never called, so the link comes from copying the receipt movement.
- [N-C02-208] Confirmed contradiction: the receiving study states that extra movements carry the same order-line link, relying on a routine that overrides a method which does not exist in the inventory module of this revision and is never called; over-receipt in this revision stays on the same movement and no extra movement is created.
- [N-C02-209] Unresolved: the receiving and valuation studies describe a return-tagging helper of the valuation module as how returns are classified for valuation, although no code calls it in this revision; returns are in fact classified by the source and destination locations of the movement.

### RISK

- [N-C02-210] Left unresolved, these findings could lead a reader to rely on a lock-date refusal that does not occur, on a re-valuation that does not happen, or on a receipt-before-bill control that does not exist.

### UNKNOWN

- [N-C02-211] Findings classified as unresolved or inferred need a runtime test; no finding was confirmed by execution.
