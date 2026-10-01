# U07 Purchase Receiving - Neutral Knowledge (Odoo 19 Community, clean-room layer)

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Source revision 19.0.post20260921. Scope: goods receipt from purchase orders, received-quantity tracking, returns, valuation effects, replenishment-to-purchase, direct-to-customer purchasing, light links to requisitions, manufacturing and repair. Statements describe what the system must do and why, in generic business terms. Each statement is tagged with an identifier and is backed by one or more claims in the restricted technical file.

## CAP-U07-01 Receipt creation from a purchase order

### WHAT
- [N-U07-001] When a purchase order that contains physical goods is approved, the system automatically creates an inbound receipt document with one planned movement for every goods line on the order.
- [N-U07-002] An order that contains only services creates no receipt and no planned stock movement.
- [N-U07-003] Every planned movement stays linked to the order line that justified it, and the receipt, the movements and the order share the same set of cross-document references, so any document can be traced to the others.

### WHY
- [N-U07-004] Automatic receipt creation gives warehouse staff a worklist that mirrors what was ordered, and gives the buyer a live view of what has arrived, without re-keying the order.

### BUSINESS RULE
- [N-U07-005] The receipt is produced at the moment the order becomes approved, not when a buyer submits it for approval. An order that is waiting for a manager's approval has no receipt yet.
- [N-U07-006] The receipt operation type defaults to the company's standard inbound type. The selectable types are limited to those of a warehouse belonging to the order's company, or types not tied to any warehouse. Changing the company of the order re-selects a suitable type.
- [N-U07-007] The receipt takes the vendor's own vendor location as its source. If the vendor has no vendor location, the system refuses to create the receipt and tells the user to define one.
- [N-U07-008] The receipt destination is the default destination of the operation type. For a direct-to-customer type with a delivery address, the destination is that customer's location. The final destination of each movement is resolved inside the warehouse stock hierarchy, so a deeper storage location is kept when the type's default sits beneath the main stock location.
- [N-U07-009] Each planned movement takes its planned date and deadline from the order line's planned date, falling back to the order's planned date.
- [N-U07-010] Each movement carries the ordered quantity in the line's unit of measure (converted to the product's own unit where required) and a unit price derived from the order line: price after discount, net of taxes that have a tax account, converted to the product's unit, converted to company currency at the order date, and rounded to the product price precision. Taxes without a tax account stay in the cost.
- [N-U07-011] When an unfinished receipt already exists for the order, new movements are added to it instead of creating another receipt. A newly created receipt that ends up with no movement is deleted again.
- [N-U07-012] After approval, adding a goods line or increasing a line quantity adds a movement for the difference to an open receipt of the order. If no receipt is open, a new receipt is created, but only when the line's ordered quantity exceeds the quantity already received.
- [N-U07-013] After approval, decreasing a line quantity is sent to the transfer engine as a negative adjustment. The engine first reduces the planned quantity of an unfinished movement of the same receipt; any part that cannot be absorbed, because it was already received, becomes a planned return movement to the vendor. In addition the system records a warning note or activity on the affected receipts and responsible people.
- [N-U07-014] Changing a line's price updates the unit price on its unfinished movements, and changing a line's planned date updates the deadline of its unfinished movements. Movements already completed keep their data, except that completed movements are re-valued when price, quantity or unit change.
- [N-U07-015] Lines of an approved order cannot be deleted under the base ordering rules. When a line is removed from an order that is not yet approved, any unfinished movement linked to it is cancelled and the downstream demand that was waiting on it is cancelled or reset to be served from stock, depending on the line's cancellation-propagation flag.
- [N-U07-016] Where a quantity adjustment produces a movement with negative quantity, the vendor is set as the partner of that movement.

### STATE
- [N-U07-017] An order's receipt status is derived from its receipts: not set when there are no receipts or all are cancelled; fully received when every receipt is completed or cancelled; partially received when at least one receipt is completed but not all are finished; otherwise not received. The status is based on the state of the documents, not on quantities.
- [N-U07-018] The order's arrival date is the earliest completion date among its completed receipts that do not go to a vendor location. An order is flagged as shipped when it has receipts and all of them are completed or cancelled.

### OPTIONALITY
- [N-U07-019] The number of reception steps is a warehouse setting (one, two or three steps). With one step, goods go directly from the vendor to stock. With more steps, further internal transfers are generated automatically by routing rules after the first receipt.
- [N-U07-020] In multi-step receiving the purchase-side logic generates only the first receipt; the later transfers are created by the transfer engine's routing rules and are confirmed together with the receipt when the order is approved.

### DEPENDENCY
- [N-U07-021] Creating, confirming, reserving and chaining the transfers is carried out by the inventory transfer engine; the purchase side only prepares the data and triggers it. Order approval rules and the bill-control policy belong to the purchase ordering function.

### CONSTRAINT
- [N-U07-022] The receipt is created under a privileged system identity so that a purchasing user who lacks warehouse rights still obtains a receipt.
- [N-U07-023] If the destination of an order line's reordering rule belongs to a different warehouse than the order's operation type, the system refuses to prepare the movement and asks the user to change the operation type or cancel the request for quotation.

### RISK
- [N-U07-024] Decreasing an order line after goods were already received produces a planned return to the vendor that nobody asked for explicitly; the buyer and the warehouse must review it.
- [N-U07-025] Approval triggers receipt creation for every order in the batch, but orders that are still pending approval remain without receipts; the buyer must not expect a receipt before approval.

### UNKNOWN
- [N-U07-026] Runtime behaviour of the full flow (approval, receipt, partial validation, later increase) has not been executed and remains to be confirmed by a runtime pass.

## CAP-U07-02 Received quantity and order line status

### WHAT
- [N-U07-027] For goods lines, the received quantity is calculated automatically from completed stock movements linked to the line; it is not typed in by hand. For service lines it is a manually entered number.
- [N-U07-028] The received quantity is the sum of completed movements, converted to the line's unit of measure with half-up rounding, minus quantities returned to the vendor.

### WHY
- [N-U07-029] A single source of truth for what has physically arrived allows the buyer to see progress and allows billing to follow actual receipts when the product is bought on received quantities.

### BUSINESS RULE
- [N-U07-030] Only completed movements count. Draft, waiting, reserved and cancelled movements do not add to the received quantity.
- [N-U07-031] Only movements whose product equals the product on the order line count; component movements of a bundled product are excluded and handled by the bundle logic.
- [N-U07-032] A movement that goes back to the vendor reduces the received quantity when it has no original movement or when its refund option is on. If the option is off, the return is ignored.
- [N-U07-033] A return of a return, that is a movement coming again from the vendor after a return, is not subtracted twice and is counted again only when the refund option is on.
- [N-U07-034] When a direct-to-customer shipment is returned to stock instead of to the vendor, the quantity is deliberately not added to the received quantity, to avoid counting goods that never entered the warehouse.
- [N-U07-035] A change of the received quantity on an approved order posts a note in the order's history.
- [N-U07-036] If a user receives a product on a receipt linked to an order that has no line for that product, the system adds a new order line with zero ordered quantity and the received quantity; its price is zero when the product is billed on ordered quantities.
- [N-U07-037] When goods are received that are already linked to a product line of the same order, the movement is attached to that existing line.

### STATE
- [N-U07-038] Partial receipt: validating a receipt for less than the planned quantity leads, depending on the operation type's backorder setting, to asking the user, to always creating a backorder for the remainder, or to never creating one and cancelling the remainder.
- [N-U07-039] The backorder keeps its link to the original order line, so the received quantity accumulates across all receipts of the line.
- [N-U07-040] After receipt, the quantity to bill is the received quantity minus the quantity already billed when the product is controlled on received quantities, or the ordered quantity minus the quantity billed when the product is controlled on ordered quantities. The quantity to bill can become negative after returns.

### OPTIONALITY
- [N-U07-041] The product's bill-control policy (ordered quantities or received quantities) decides which quantity drives the quantity to bill. This policy is owned by the purchase ordering function.
- [N-U07-042] If the stock-linked behaviour is removed, lines previously computed from movements are frozen into manual entries with their last received value.

### DEPENDENCY
- [N-U07-043] The number of billable units and the invoice status of the order are computed by the purchase ordering and billing function from the received quantity supplied here.
- [N-U07-044] Links between a receipt and a vendor bill exist only through the order line: bill lines point to order lines, movements point to order lines. There is no direct link between one receipt and one bill and no shared reference field enforced by this function.

### CONSTRAINT
- [N-U07-045] The received-quantity field is read-only on the order form for goods lines and editable for service lines.

### RISK
- [N-U07-046] The order-level receipt status says fully received as soon as all receipts are finished, even if a receipt was validated for a smaller quantity and the remainder was cancelled. Reading the status alone can therefore overstate completeness.
- [N-U07-047] Because rounding and unit conversion are applied per movement, order lines whose receipts use another unit of measure can differ slightly from a naive sum.

### UNKNOWN
- [N-U07-048] The behaviour with multiple units, lots and mixed returns on one line has not been executed; confirmation requires a runtime pass.

## CAP-U07-03 Billing before receiving, over-receiving and under-receiving

### WHAT
- [N-U07-049] The system permits receiving more than the ordered quantity: no limit on received quantity versus ordered quantity is enforced by the receipt or the order logic in the examined code.
- [N-U07-050] The system permits receiving less than ordered. The unreceived remainder is either left as a backorder or cancelled, according to the operation type setting.
- [N-U07-051] The examined code does not block the creation or posting of a vendor bill before any goods have been received, whichever bill-control policy is set.

### WHY
- [N-U07-052] Real deliveries rarely match orders exactly, so the process tolerates both shortfalls and excesses and relies on later reconciliation rather than stopping the warehouse.

### BUSINESS RULE
- [N-U07-053] With a bill-control policy on received quantities and nothing received, the billable quantity is zero. A bill can still be started from the order and carries lines with zero quantity; the system does not refuse it.
- [N-U07-054] With a bill-control policy on ordered quantities, the billable quantity is the full ordered quantity from approval onward, so billing before receipt is by design.
- [N-U07-055] A receipt cannot be validated if it is empty, if it has no quantity at all, or if a tracked product lacks a lot or serial number; these are the only hard stops at validation.
- [N-U07-056] If an order line's ordered quantity is reduced below the quantity already billed, the system schedules a warning activity on the first vendor bill of that line suggesting that a refund be requested.
- [N-U07-057] Over-receipt raises the received quantity above the ordered quantity; when the policy is received quantities, the billable quantity follows the received quantity and rises above the ordered quantity.

### STATE
- [N-U07-155] The billing status of an order is derived only from the quantity still to be billed: nothing to bill, to be billed, or fully billed. Whether a receipt exists influences this status only through the bill-control policy, never as a separate condition.

### OPTIONALITY
- [N-U07-058] A stricter matching control, where the goods must be received before a bill can be paid, is offered only as a separate optional extension that is not part of the open-source code base examined; in this edition the control is informational at most.

### DEPENDENCY
- [N-U07-156] Creating and posting vendor bills belongs to the purchase ordering and billing function. This function only supplies the received quantity, and it reacts to a posted bill by re-valuing the matching received goods.

### CONSTRAINT
- [N-U07-059] No numeric tolerance or percentage threshold for over-receipt or under-receipt is configured in the examined modules.

### RISK
- [N-U07-060] The earlier community report of a bill being created before receipt is consistent with the code: the bill-control policy shapes the suggested quantity but is not a hard gate. Anyone relying on it as a control would be mistaken.
- [N-U07-061] Over-receipt combined with the received-quantity policy can lead to paying for more than was ordered without any system warning.
- [N-U07-062] A bill posted before receipt under the ordered-quantity policy creates a payable for goods not yet in stock; the stock value is later aligned when the receipt is completed.

### UNKNOWN
- [N-U07-063] Whether the optional matching extension adds a hard block cannot be determined from the examined code base; it is not present in the installed database either.

## CAP-U07-04 Returns of received goods and refunds

### WHAT
- [N-U07-064] A user can return all or part of a completed receipt to the vendor. The system creates a reverse transfer from the stock location back to the vendor location, linked to the original movement.
- [N-U07-065] The reverse transfer remembers which order line the goods came from, found by walking back through the chain of linked movements, and sets the vendor as its partner.

### WHY
- [N-U07-066] Returns correct the received quantity and the stock without erasing history, so the original receipt stays in the audit trail.

### BUSINESS RULE
- [N-U07-067] Each returned line carries an option, on by default, to update the quantities on the order. When on, the completed return reduces the received quantity on the order line; when off, the order line is unchanged.
- [N-U07-068] After a return with the option on, under the received-quantity policy the quantity to bill falls below the quantity already billed and can become negative, which leads the buyer to request a vendor credit note.
- [N-U07-069] A bill whose total turns out negative is automatically converted into a vendor credit note. Credit note lines reduce the billed quantity of the order lines they point to.
- [N-U07-070] For receipts, the user can choose an exchange: a return to the vendor plus a new independent receipt of the replacement goods that is not linked to the original movement.
- [N-U07-071] The return destination is the return type's default destination if it is an inbound type, otherwise the original source location of the receipt.
- [N-U07-072] A completed return that goes to a vendor location does not count as the order's arrival date.

### STATE
- [N-U07-073] A return is a new transfer that starts as a draft, is confirmed and reserved immediately, and then follows the normal transfer states; the original receipt stays completed.

### OPTIONALITY
- [N-U07-074] Cancelling an order does not reverse completed receipts: the system leaves them untouched and posts a note on each completed receipt saying the order was cancelled.

### DEPENDENCY
- [N-U07-075] Creating and validating the reverse transfer belongs to the transfer engine; the credit note itself belongs to the billing function. The purchase-stock link only supplies the order line and vendor, and defines how returned quantities enter the received quantity.
- [N-U07-076] The valuation effect of the return, and the stock-versus-payable entries of the credit note, belong to the valuation and accounting functions.

### CONSTRAINT
- [N-U07-077] When a vendor bill is itself a credit note, the quantity taken from the order line is carried with the opposite sign so that credit note lines show positive quantities.

### RISK
- [N-U07-078] With the update-quantities option off, the received quantity on the order can exceed the physical stock without any warning, because the physical return is not reflected on the order.
- [N-U07-079] If a vendor credit note is not raised after a return, the payable remains overstated; the system suggests the credit note only indirectly through the negative quantity to bill.

### UNKNOWN
- [N-U07-080] The exact behaviour for returns spanning several receipts, lots, or units has not been executed.

## CAP-U07-05 Valuation and price-difference behaviour

### WHAT
- [N-U07-081] Every movement created from an order line carries a unit price, in company currency, derived from the order line; this price is the first estimate of the value of the goods received.
- [N-U07-082] When goods are valued, the system prefers actual vendor-bill amounts if bills have been posted, then the order price, and otherwise the product's cost.

### WHY
- [N-U07-083] Valuing at the order price at receipt and refining with the real bill when it arrives lets stock be valued promptly and corrected to the actual invoiced cost.

### BUSINESS RULE
- [N-U07-084] The conversion to company currency uses the order date when the movement is created and the movement's own date when the order price is used for valuation.
- [N-U07-085] The value from bills uses only posted bills. Credit-note quantities and amounts reduce the value. Billed quantities are allocated to receipts in date order, so earlier receipts consume billed quantity first, and later receipts are valued at the order price for any quantity not yet billed.
- [N-U07-086] Changing price, quantity or unit on an approved order line updates unfinished movements and re-values movements that are already valued.
- [N-U07-087] A value is stored on received movements even when the company's inventory valuation is periodic. Journal entries for stock are created at movement completion only when valuation is automated for the product and valuation accounts are defined on the locations.
- [N-U07-088] On posting a vendor bill, for products costed at standard price and when the company uses anglo-saxon style accounting, the system adds two extra journal lines for any difference between the billed unit price and the product's standard cost: one to the price-difference account of the product category and one correcting the original line.
- [N-U07-089] No price-difference lines are produced when the category has no price-difference account, when the computed difference is zero, when the product is not stockable, or when the goods were shipped directly to the customer.
- [N-U07-090] Bill lines are marked as landed-cost lines when the product is flagged for landed costs; applying landed costs to receipts is possible only for products costed at first-in first-out or average cost, never for standard cost.

### STATE
- [N-U07-091] The recorded value of a movement is refreshed when its source data changes: when a bill is posted that touches the line, when a landed cost is validated, or when the order line's price, quantity or unit changes.

### OPTIONALITY
- [N-U07-092] Price-difference lines depend on three switches together: the company-level anglo-saxon style setting, the product's standard costing method, and a configured price-difference account.
- [N-U07-093] The inventory valuation mode (periodic or automated) is a company-wide default that can be overridden per product category. In the examined database it is periodic, costing is standard, the anglo-saxon style is off, and no location carries a valuation account, so none of the extra entries above would be produced as configured.

### DEPENDENCY
- [N-U07-094] The valuation engine, costing methods and journal entry creation belong to the valuation function; this function only supplies the order price, the bill-based value and the movement linkage.

### CONSTRAINT
- [N-U07-095] Landed costs can be validated only for products with first-in first-out or average costing; otherwise the system refuses with a message.

### RISK
- [N-U07-096] Under standard costing without the anglo-saxon style, bill-versus-receipt price differences are not recorded as separate lines; the difference is absorbed elsewhere and must be reviewed.
- [N-U07-097] A guard that appears intended to skip bill lines with a discount compares a price with itself and therefore never excludes anything, so discounted lines are not reliably skipped; the discount is however already reflected in the compared price.

### UNKNOWN
- [N-U07-098] The accounting entries themselves were not executed; amounts and accounts remain to be proven in a runtime pass with automated valuation enabled.

## CAP-U07-06 Replenishment to purchase

### WHAT
- [N-U07-099] Each warehouse has a buy route and a buy rule that, when a need for a product arises, creates a request for quotation to the best matching vendor instead of an internal transfer.
- [N-U07-100] The need can come from a reordering rule (minimum and maximum), a manual replenishment, a customer order on make-to-order, a manufacturing demand, or a similar procurement.

### WHY
- [N-U07-101] Linking needs to vendor requests automatically keeps stock available while letting the buyer review and approve the order before it is committed.

### BUSINESS RULE
- [N-U07-102] The buy route is offered for a product only if the product has at least one vendor price list line.
- [N-U07-103] When a buy rule is triggered, the warehouse's receipt route is added so that the follow-on receiving steps apply.
- [N-U07-104] The vendor is chosen in this order: the vendor given explicitly in the request, the vendor set on the reordering rule, otherwise the best vendor for the product by quantity, date and unit of measure. If the best vendor has no matching price, the first vendor compatible with the company is used.
- [N-U07-105] If no vendor is found: a failed reordering rule is reported with an explanatory message; any other need is detached from purchasing, downstream demand flagged to propagate cancellation is cancelled and the rest is switched to be served from stock, and the product responsible and the sales or manufacturing owners are notified.
- [N-U07-106] The request reuses an existing draft order when it has the same vendor, operation type, company, buyer and currency, plus a grouping condition set on the vendor: on order (same references only), daily, weekly (optionally aligned to a chosen weekday), or always.
- [N-U07-107] A new draft order takes the vendor's buyer, payment terms, fiscal treatment and currency, and an order date set to the earliest needed date minus the vendor lead time.
- [N-U07-108] Within the order, a line is reused for the same product when its unit, cancellation propagation, reordering rule and description match; then quantity is added and the price is recomputed from the vendor price list for the new total quantity, converting currency at today's rate.
- [N-U07-109] A request with a negative quantity reduces an existing line but never creates a new line.
- [N-U07-110] The order date is moved earlier when a new line's needed-by date minus the vendor lead time falls before the current order date.
- [N-U07-111] The replenishment lead time is the vendor's delivery delay plus the company's days to purchase; when no vendor exists a year of delay is assumed.
- [N-U07-112] The quantity already requested on draft orders counts as supply in progress, so reordering rules do not order twice for the same need.
- [N-U07-154] The buyer can ask the system to suggest order quantities per product, based on recent demand over a chosen number of days and period, or on the forecast shortfall, net of stock on hand and incoming quantities; the parameters chosen are remembered per vendor, and the suggestion replaces earlier quantities on the order.

### STATE
- [N-U07-113] The request starts as a draft order, so it is a quotation to review. It is approved through the normal ordering process, and only then does a receipt appear.

### OPTIONALITY
- [N-U07-114] The warehouse flag buy to resupply switches the buy route on or off per warehouse. Grouping behaviour and weekday alignment are per-vendor settings. Days to purchase is a company setting.
- [N-U07-115] Direct-to-customer ordering is itself a purchase rule bound to a vendor-to-customer operation type; it is installed only with the optional drop-shipping extension.

### DEPENDENCY
- [N-U07-116] The scheduler that evaluates reordering rules is part of the transfer and replenishment engine; the purchase side supplies the vendor choice, grouping, lead time and the creation of the quotation.

### CONSTRAINT
- [N-U07-117] The quotation is created under a privileged system identity so that the requesting user, who may be a customer-facing or portal user, does not become a follower of the order.

### RISK
- [N-U07-118] If the vendor price list has no price valid for the needed quantity and date, the system still falls back to a vendor without a price, so quotations with zero price may be created.
- [N-U07-119] Grouping on the vendor with the always setting can merge unrelated needs into one order, losing traceability of which need justifies which line.

### UNKNOWN
- [N-U07-120] The effect of the scheduled run over a large volume of reordering rules, and the interplay with multiple companies, has not been executed.

## CAP-U07-07 Direct shipping, requisitions, manufacturing and repair links

### WHAT
- [N-U07-121] A direct-to-customer purchase has goods leave the vendor straight to the customer. The receipt document runs from the vendor location to the customer location, belongs to no warehouse, and uses its own numbering.
- [N-U07-122] The order line keeps a link to the customer order line that needed it, and lines for different customer order lines are never merged, so the delivered quantity of each customer line can be computed correctly.
- [N-U07-123] When one purchase covers several customer orders, one direct delivery document is created per customer order.

### WHY
- [N-U07-124] Direct shipping avoids handling goods in the warehouse while keeping the purchase, the customer order and the shipment connected.

### BUSINESS RULE
- [N-U07-125] Completed direct shipments add to the order line's received quantity like normal receipts, because their source is the vendor.
- [N-U07-126] On the customer order side, direct shipments count as delivered goods, and the quantity treated as already procured for a customer line served by direct purchase is taken from its linked purchase lines rather than from stock.
- [N-U07-127] Direct shipments receive a recorded value for margin purposes, but they are not treated as entering or leaving stock, so no stock journal entry is created for them, and price-difference lines are not generated for them.
- [N-U07-128] The purchase order shows separate counts for ordinary receipts and direct shipments.
- [N-U07-129] Purchase agreements: an order created from an agreement takes the agreement's operation type; replenishment against a vendor price list tied to an agreement is grouped per agreement and takes the agreement's currency and reference.
- [N-U07-130] Alternative quotations created from an order inherit the operation type, the references and the downstream demand links of the original.
- [N-U07-131] For a bundled product bought as a kit, received quantity is computed from the components received, and the cost is shared between components by a configured percentage that must total one hundred percent.
- [N-U07-132] Orders and manufacturing orders show each other, and demand for a component of a manufacturing order can be met by a purchase that is linked to that order. Repair orders and purchase orders likewise show their related counterparts.

### STATE
- [N-U07-157] A direct-shipping chain runs from the customer order line, to a draft quotation, to an approved order, to one or several direct delivery documents, to a completed delivery that raises both the received quantity on the purchase line and the delivered quantity on the customer line.

### OPTIONALITY
- [N-U07-133] Direct shipping, purchase agreements with stock, kit purchasing and repair links exist only when the corresponding extension modules are installed; in the examined database all of them are installed.

### DEPENDENCY
- [N-U07-134] Customer-side effects of direct shipping belong to the sales delivery function; kit decomposition belongs to the manufacturing function; repair behaviour belongs to the repair function.

### CONSTRAINT
- [N-U07-135] A bundle's component cost shares must be non-negative and total one hundred percent whenever any share is set.

### RISK
- [N-U07-136] The direct-shipping split logic tests for a completed order state that does not exist in this edition; only the approved state is effective, so the extra test is dead.
- [N-U07-137] Some manufacturing-side valuation overrides call functions that no longer exist in the valuation engine and appear unused; they would fail if invoked.

### UNKNOWN
- [N-U07-138] Interaction of direct shipping with returns to customers and with subcontracting has not been executed; it requires a runtime pass.

## CAP-U07-08 Roles, company scope, scheduled behaviour and failure paths

### WHAT
- [N-U07-139] Purchasing users and managers can read, change and create transfers and movements that relate to purchases; managers can also delete movements. Warehouse users can read orders and order lines but not change them.
- [N-U07-140] Replenishment rules and the vendor delay report are readable by purchasing roles; stock requisition managers can read and create purchase agreements.

### WHY
- [N-U07-141] Purchasing staff must be able to follow and trigger receipt documents without full warehouse authority, and warehouse staff must see what was ordered without being able to alter commercial data.

### BUSINESS RULE
- [N-U07-142] This function defines no record-level restrictions of its own; company isolation of orders, lines, transfers, movements, warehouses, locations and operation types comes from restrictions defined by the purchasing and inventory functions, all limiting visibility to the user's allowed companies.
- [N-U07-143] Receipts, movements and quotations created from procurement carry the company of the order or the procurement; the operation type must match that company.
- [N-U07-144] A daily scheduled task evaluates reordering rules and creates quotations; a daily task sends order reminders but, in this function, skips orders that already have a completed receipt.
- [N-U07-145] A completed receipt automatically marks the order as acknowledged by the vendor.
- [N-U07-146] The vendor on-time rate counts, over a rolling window (default one year, adjustable by a system parameter), the quantity received on or before the planned date divided by the quantity ordered; vendors without data show a negative marker.

### STATE
- [N-U07-147] Cancelling an approved order cancels its unfinished movements and receipts; downstream demand is cancelled or reset to be served from stock; completed receipts are untouched with a note. If the order is locked or has active vendor bills, the cancellation is refused by the base ordering logic.

### OPTIONALITY
- [N-U07-148] Reminders require the user group that allows sending reminders; the on-time window, days to purchase, and vendor grouping are configuration, not code.

### DEPENDENCY
- [N-U07-149] Approval thresholds and locking behaviour are owned by the purchase ordering function; only the arrival-dependent parts are described here.

### CONSTRAINT
- [N-U07-150] Failure paths: missing vendor location stops receipt creation; a reordering rule in another warehouse stops movement preparation; no vendor stops a reordering request with a message and creates an activity on the product for the responsible person; no matching rule stops a replenishment with an error message.

### RISK
- [N-U07-151] Cancellation first removes receipts and movements and only then runs the base checks for locks and bills, so a refused cancellation relies on the whole operation being rolled back.
- [N-U07-152] Quotations created from replenishment and from customer orders are created under a privileged identity, so ordinary access rights do not limit who triggers purchases through a customer order or a reordering run.

### UNKNOWN
- [N-U07-153] Whether any vendor-facing portal path changes planned dates through this function is not evidenced beyond the date-update activity note; no runtime check was done.
