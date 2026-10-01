# U08 — Stock Transfers — Neutral Knowledge (clean-room layer)

> Status: `DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION`
> Source product basis: Odoo 19 Community (named here once, in the header only).
> This file states what an inventory transfer, warehouse routing, reservation, replenishment, shipping and drop-shipping capability must do and why, in business language. It contains no source paths, object names, field names or code.

Section key: WHAT, WHY, BUSINESS RULE, STATE, OPTIONALITY, DEPENDENCY, CONSTRAINT, RISK, UNKNOWN. Each statement carries an identifier of the form N-U08-nnn that is referenced from the restricted technical evidence file.

## CAP-U08-01 Warehouse and routing configuration (neutral)

### WHAT
- [N-U08-001] A warehouse is a company-owned stock site. Its receipt flow and its delivery flow are each configured as one, two or three steps, and the system derives the locations, operation types, routes and rules of the warehouse from those two choices.
- [N-U08-002] Receipts run in one step (vendor to stock), two steps (vendor to an input area, then storage into stock) or three steps (input, quality control, then stock). Deliveries run in one step (stock to customer), two steps (pick, then ship) or three steps (pick, pack, then ship).
- [N-U08-003] A route is a named bundle of rules. A rule says how goods move from one location to another, with which operation type, with what lead time, and whether it is a pull (triggered by a need), a push (triggered by arrival) or both.

### WHY
- [N-U08-004] Step choices let a business add handling stages such as inspection, packing and staging without changing documents by hand: each stage becomes its own transfer with its own operation type and number sequence.

### BUSINESS RULE
- [N-U08-005] In a receipt route the first leg is a pull from the vendor location; every later leg is a push that fires automatically when goods reach the previous location. In a delivery route the first leg is a pull from stock toward the customer and later legs are pushes from the staging areas, ending at the customer.
- [N-U08-006] Inside a generated route the first rule draws from goods on hand, and each following rule waits for the previous leg to finish (the supply method of later rules is make-to-order).
- [N-U08-007] Cancellation propagates along a generated receipt chain except from its final step, so that cancelling an early step never cancels goods that already belong in stock.
- [N-U08-008] To satisfy a need, the system looks for a pull rule starting at the requested destination and then at its parent locations. Routes named in the need come first, then routes of the packaging unit, then routes on the product and on its product category, then the default routes of the warehouse.
- [N-U08-009] Among candidate routes, routes assigned directly to the product rank before the others and then the route order applies; inside one route the rule order applies; a rule bound to the right warehouse beats a rule that is not bound to any warehouse.
- [N-U08-010] To find a push rule the system starts at the location where goods arrived and moves up through parents. Preferred routes on the movement and routes of the package type are considered first; a push rule may carry an applicability condition that the movement must satisfy, otherwise the next candidate is tried.
- [N-U08-011] A push rule either replaces the destination of the movement being processed (no step added) or creates a follow-up movement that waits for the first one (manual operation). A return of a return is exempt, so that goods sent back are not pushed on again.
- [N-U08-012] A pull rule must name a source location; otherwise the need fails with an error. Movements created from a pull rule are dated at the planned date minus the rule lead time, and their final destination is the location that expressed the need.
- [N-U08-013] If no rule can be found the need is refused with an instruction to verify the routes configured on the product. Needs for non-physical products and needs of zero quantity are skipped without error.

### STATE
- [N-U08-014] A warehouse can be archived only when no unfinished movement uses its operation types and no operation type outside it uses its locations. Archiving also archives its operation types, its locations, its rules and the routes dedicated to it; unarchiving re-applies the step configuration.

### OPTIONALITY
- [N-U08-015] The replenish-on-order (make-to-order) route is optional. It is shipped switched off and is toggled from the inventory settings. In the studied database it is switched on.
- [N-U08-016] Multi-step routing needs the push-and-pull setting. With one warehouse and one-step flows the intermediate locations and operation types still exist but are archived.
- [N-U08-017] Resupply of one warehouse from another is optional per warehouse; enabling it generates a route through a transit location, which is the company transit location inside one company and the shared inter-company transit location across companies.

### DEPENDENCY
- [N-U08-018] Changing the number of steps rewrites dependent objects: locations are activated or archived, operation types are activated or archived, routes are renamed and rules are archived or created. Previously archived rules are reused rather than duplicated.
- [N-U08-019] Other installed modules extend the warehouse with their own routes, rules and operation types (purchasing, manufacturing, repair, subcontracting). The initial vendor pull rule of the receipt route is archived in the studied database because purchasing takes over that leg.

### CONSTRAINT
- [N-U08-020] A warehouse name and a warehouse short code must each be unique within a company, and a warehouse cannot be moved to another company after creation.
- [N-U08-021] A route and all its rules must belong to the same company; a route that has no company is shared by all companies.

### RISK
- [N-U08-022] Rule resolution depends on route order values and on where the rule destination sits in the location tree. Two competing routes, or a rule defined on a parent site, can silently choose a different supplier or step than the one intended, so routing must be reviewed after each configuration change.

### UNKNOWN
- [N-U08-023] Why the replenish-on-order route is switched on in the studied database cannot be determined from configuration alone; it needs the installation history or a runtime check.

## CAP-U08-02 Transfer and movement state machine (neutral)

### WHAT
- [N-U08-030] A transfer is a document that groups the movements of products between two locations for one operation type. Each movement has its own status, and the status of the transfer cannot be edited directly: it is derived from the statuses of its movements.
- [N-U08-031] Movement statuses are: new, waiting for another movement, waiting for stock, partially available, available, done and cancelled. Transfer statuses are: draft, waiting for another operation, waiting, ready, done and cancelled; a transfer never shows partially available.

### WHY
- [N-U08-032] Deriving the transfer status from its movements keeps the header honest about what can actually be processed, and the shipping policy decides how strict that header status is.

### BUSINESS RULE
- [N-U08-033] A transfer with no movements, or with at least one new movement, is draft. A transfer whose movements are all cancelled is cancelled. A transfer whose movements are all done or cancelled is done, except that when every done movement went to the inventory-loss location and some other movement was cancelled it is shown as cancelled. A transfer left with no movement after cancellation is set to cancelled.
- [N-U08-034] For a transfer with open movements, the least advanced movement drives the status under the policy of releasing only when all products are ready, whereas under the policy of shipping as soon as possible the transfer is ready as soon as any movement has been reserved, even partially. Open movements with zero demand that are already available are ignored.
- [N-U08-035] A transfer whose source location never needs reservation (vendor, customer, inventory loss or production) and whose movements all draw from stock is ready immediately whatever its movement statuses.
- [N-U08-036] Confirming a transfer acts only on its new movements: a movement that depends on a previous movement becomes waiting for another movement; a make-to-order movement raises its own need and becomes waiting; any other movement becomes waiting for stock. Afterwards the system checks automatic reordering for open movements.
- [N-U08-037] Checking availability on a draft transfer first confirms it. Open movements are then processed by urgency, then by earliest deadline, then by date. If there is nothing open to check the user is told so.
- [N-U08-038] A done movement is final and always counts as picked; cancellation of a movement is possible only before it is done (with the exception of movements that went to the inventory-loss location).
- [N-U08-039] After a quantity change, a movement status is recomputed from its quantities: reserved at least the demand makes it available; some reserved quantity makes it partially available; nothing reserved makes it waiting for another movement if it is make-to-order without a source movement or has an unfinished predecessor, and waiting for stock otherwise.
- [N-U08-040] A movement added to a transfer after the transfer was confirmed is flagged as additional and is confirmed automatically when saved; a movement added to a transfer that is already done is created directly as done and picked.
- [N-U08-041] The transfer reference is taken from the number sequence of its operation type when the transfer is created and must be unique within a company. The scheduled date is written after the movements exist so the outcome is deterministic.

### STATE
- [N-U08-042] A batch of transfers is draft, in progress, done or cancelled. It is cancelled automatically when all its transfers are cancelled and done when all its non-cancelled transfers are done.

### OPTIONALITY
- [N-U08-043] The shipping policy defaults from the operation type and can be changed on each transfer; it changes only how partial availability maps onto the transfer status.
- [N-U08-044] When reservation happens (at confirmation, manually, or shortly before the scheduled date) decides when waiting movements can become available.

### DEPENDENCY
- [N-U08-045] A movement waiting for another movement becomes available only after the predecessor is done and reservation is run again for it. Manufacturing, repair and subcontracting add their own document statuses on top of these.

### CONSTRAINT
- [N-U08-046] The operation type of a transfer cannot be changed once it is done or cancelled; changing it earlier gives the transfer a new reference and resets its locations to the type defaults.
- [N-U08-047] A draft transfer is not reserved and shows no availability; reservation applies only after confirmation.

### RISK
- [N-U08-048] Because the transfer status is a stored derived value, any code that writes a movement status without the standard methods can leave the header out of date, and the ready status under the as-soon-as-possible policy can hide shortages on the remaining lines.

### UNKNOWN
- [N-U08-049] Which transitions can be triggered from user screens and which only from actions of other documents needs runtime confirmation.

## CAP-U08-03 Reservation and availability (neutral)

### WHAT
- [N-U08-060] Reservation sets aside available stock of a product in a source location for a movement and creates detailed lines (location, lot, package, owner, quantity) that say exactly where the goods will be taken from. A single quantity on each detailed line serves both as the reserved quantity and, once marked as picked, as the processed quantity.
- [N-U08-061] Reservation can be partial: when only part of the demand is available, the movement becomes partially available and keeps what could be reserved.

### WHY
- [N-U08-062] Reservation prevents the same stock being promised twice and tells pickers where to go; availability is on-hand quantity minus what is already reserved.

### BUSINESS RULE
- [N-U08-063] Reservation is attempted only for movements that are confirmed, waiting for another movement or partially available and that are not yet picked. The quantity still to reserve is the demand minus what the movement already holds.
- [N-U08-064] Locations that stand for outside parties or counterparts (vendor, customer, inventory loss, production) and products that are not stock-tracked never reserve stock: detailed lines are created without touching stock levels and the movement is available at once.
- [N-U08-065] For a movement with no predecessor the system reserves from the stock of the source location and its sub-locations, up to the available quantity; a make-to-order movement with no predecessor reserves nothing and waits for its need to be fulfilled. If the full need is covered the movement becomes available, otherwise partially available.
- [N-U08-066] For a movement fed by predecessor movements, only what the predecessors actually brought (done lines) and that sibling movements have not already taken can be reserved, and it is reserved on the exact characteristics (location, lot, package, owner) of those lines.
- [N-U08-067] Which stock is taken first follows the removal strategy. A strategy forced on the product category wins; otherwise the first strategy found on the source location or on its parents; otherwise first-in-first-out. First-in-first-out takes the oldest stock, last-in-first-out the newest, closest location the nearest in the location tree, and least packages favours the fewest packages.
- [N-U08-068] A reservation never exceeds the available quantity (on hand minus already reserved), is rounded so that the unit of measure of the movement is not exceeded, and for serial-numbered products can only be a whole number.
- [N-U08-069] When a product category requires full-packaging reservation, the reserved quantity is rounded down to whole packages.
- [N-U08-070] The moment of reservation is a setting of the operation type: at confirmation, manually, or before the scheduled date (a configured number of days earlier, with another number of days for urgent transfers). The setting is hidden for receipts, which never need reservation.
- [N-U08-071] When incoming or internal transfers are done, waiting movements for the same product in the receiving location tree are reserved automatically, urgent first and then earliest first, unless automatic reservation is switched off globally. The daily scheduler also retries every confirmed or partially available movement that is due.
- [N-U08-072] Releasing a reservation removes the unpicked detailed lines of a movement and recomputes its status. Picked lines stay. A done movement cannot be released, except movements that went to the inventory-loss location, which are ignored.
- [N-U08-073] Forcing a quantity: when a user processes a quantity that is not available in a location, the system frees the same stock from other unpicked reservations (first those of the current transfer, then those of the latest scheduled transfers), removes the link with predecessors for those movements and reruns reservation for them.
- [N-U08-074] Lowering the quantity of a movement releases detailed lines in reverse order of creation, so that the stock reserved last under the removal strategy is released first.
- [N-U08-075] Raising the demand of an open movement keeps its reservation and shows it as partially available, except for receipts, where reservation is rerun immediately. Lowering the demand below the reserved quantity releases the excess.
- [N-U08-076] Under the policy of releasing only when everything is ready, a transfer stays waiting while any movement is not fully reserved; under the policy of shipping as soon as possible it becomes ready when anything is reserved.

### STATE
- [N-U08-077] Reservation moves a movement between waiting, partially available and available; releasing moves it back.

### OPTIONALITY
- [N-U08-078] Automatic reservation after receipts can be disabled globally by a system parameter; it is not set in the studied database. The reservation moment is set per operation type and the removal strategy per location and per product category.

### DEPENDENCY
- [N-U08-079] The stock levels per location, lot, package and owner that reservation reads and updates belong to the inventory-level capability. This capability asks that capability to reserve and receives the quantity taken.
- [N-U08-080] Expiry-date handling is a separate module that adds the first-expiry-first-out removal strategy, ordering by earliest removal date.

### CONSTRAINT
- [N-U08-081] A detailed line cannot reserve a negative quantity. Editing the characteristics of a reserved line re-reserves the maximum quantity possible at the new characteristics.

### RISK
- [N-U08-082] Reservation reads live stock when it runs. With negative stock or concurrent processing, the available quantity can be lower than expected and reservations can be partly lost; the forced-quantity logic then repairs this by taking reservations away from other transfers.
- [N-U08-083] When reservation is manual or by date, nothing is reserved until its trigger, so a pipeline that looks ready can in fact be waiting for stock.

### UNKNOWN
- [N-U08-084] Behaviour under concurrent updates, and with lots inside packages, requires runtime tests; the detailed stock-level rules belong to the inventory-level unit and were not studied here.

## CAP-U08-04 Validation of a transfer and backorders (neutral)

### WHAT
- [N-U08-090] Validating a transfer completes it: the processed quantities move from the source to the destination location, the transfer and its movements become done, unprocessed quantities either go to a new follow-up transfer (a backorder) or are cancelled, and downstream steps are triggered.
- [N-U08-091] In this version there is no separate immediate-transfer confirmation step. Validating a transfer that is still draft first confirms it, and any movement that has a demand but no processed quantity receives its full demand as processed quantity.

### WHY
- [N-U08-092] Validation is the point at which stock really changes and at which other applications (orders, shipping, notifications, accounting) learn that goods moved.

### BUSINESS RULE
- [N-U08-093] Before anything else the system rejects an empty transfer, a transfer whose processed quantities are all zero, and a transfer holding tracked products without a lot or serial number when its operation type uses lots. When several transfers are validated together the problems are reported per transfer.
- [N-U08-094] If some movements have a processed quantity but none is marked as picked, all of them are treated as picked; movements going to the inventory-loss location are not counted for that purpose. The check for zero quantity considers only picked movements when at least one is picked.
- [N-U08-095] A backorder question is raised only for operation types set to ask: it applies when a movement with demand is not picked or when its processed quantity is below demand. Types set to always create the backorder without asking; types set to never cancel the remaining quantities.
- [N-U08-096] The backorder question lets the user create a backorder, validate without one (cancelling the rest), or abandon; with several transfers the choice is made per transfer. Declining a backorder logs the shortfall on the transfer and on related documents.
- [N-U08-097] When validating, movements without a processed quantity are cancelled if their demand is zero or if no backorder is wanted; unpicked lines of picked movements are removed; a movement whose processed quantity is below its demand is split and the remainder forms backorder movements.
- [N-U08-098] A backorder is a copy of the transfer with a new reference, linked to the original and keeping any return link; the unprocessed movements are moved into it as not picked and its responsible user is cleared; when its operation type reserves at confirmation an availability check runs at once.
- [N-U08-099] A processed quantity above the demand is not blocked by the validation code; only a shortfall creates a backorder and no extra movement is created for an excess. How such excess is treated by other documents is not established.
- [N-U08-100] A user can also split a transfer manually so that the processed quantities go to a new transfer. This is refused when nothing is processed, when everything is already processed, or when any processed quantity exceeds its demand.
- [N-U08-101] For each detailed line the quantity moves from the source to the destination location. Lines of zero quantity are removed, negative quantities are refused, quantities must respect the rounding of the unit of measure, tracked products require a lot unless the operation type uses neither existing nor new lots, and when the type allows new lots a typed lot name creates the lot.
- [N-U08-102] After the movements are done: onward push rules run, successor movements are reserved, backorders are created, and when an owner is set on the transfer the stock is taken from or assigned to that owner.
- [N-U08-103] The completion date of the transfer is set to the time of validation and its priority returns to normal; the done movements carry that date.
- [N-U08-104] A confirmation email can be sent for delivery transfers; for incoming and internal transfers the reception report can be displayed and slips or labels can be printed automatically according to settings of the operation type.
- [N-U08-105] When packages leave for a transit location belonging to another company and the inter-company unpack setting is on, the packages are unpacked automatically.

### STATE
- NOT APPLICABLE or no statement recorded for this section.

### OPTIONALITY
- [N-U08-106] The backorder policy is set per operation type (ask, always, never). Internal callers may skip the sanity checks, and lot checks apply only to operation types that use lots.

### DEPENDENCY
- [N-U08-107] Several installed modules extend validation: a pre-validation notice for text messages and one for expired lots, order lines created for extra delivered quantity, acknowledgement of the vendor order, valuation entries, subcontracting, carrier shipping, and removal of the transfer from a batch.
- [N-U08-108] When a carrier with the create-shipment integration level is set and the operation type prints labels, validating a delivery sends the shipment to the carrier and records tracking and cost.

### CONSTRAINT
- [N-U08-109] Validation cannot be undone: a done transfer can be reversed only by a return, and the carrier call that follows validation cannot roll it back.
- [N-U08-114] The validate action is offered only to inventory users and administrators, and the stock user permission is also needed on the transfer itself.

### RISK
- [N-U08-110] If a carrier call fails after other transfers in the same validation were already shipped, a warning is recorded instead of failing, so manual follow-up is needed.
- [N-U08-111] Because always and never policies skip the backorder question, a wrong policy on an operation type leads either to unwanted backorders or to silently cancelled remainders.

### UNKNOWN
- [N-U08-112] Whether a processed quantity above demand is intentionally accepted, and how downstream documents treat it, needs runtime confirmation.
- [N-U08-113] A hook meant to make returns ignore the backorder policy exists but no caller was found, so returns appear to follow the operation type policy.

## CAP-U08-05 Returns and reverse transfers (neutral)

### WHAT
- [N-U08-125] A return reverses goods already delivered or received by creating a new transfer in the opposite direction, linked to the original transfer and to its movements. It is created from a done transfer by a wizard that lists each movement and a quantity to return.

### WHY
- [N-U08-126] The original stock movement is never edited or deleted after it is done; the reverse flow is a new document, which keeps the audit trail and lets other applications (refund, reorder) follow it.

### BUSINESS RULE
- [N-U08-127] Only a done transfer can be returned (with sales installed a transfer linked to a sales order is also accepted), only one transfer at a time, and cancelled movements and movements that went to the inventory-loss location are not offered. A return can also be started from scratch with no original transfer.
- [N-U08-128] The wizard proposes every movement with a quantity of zero; the user types quantities, or uses the return-all action that proposes the delivered quantity minus what was already returned.
- [N-U08-129] The return uses the operation type configured as the return type of the original type (deliveries and receipts point at each other by default). If that type is a receipt the destination is its default destination, otherwise the original source; the return's source is the original destination. The return is a draft copy linked to the original, with its responsible user cleared, and it keeps locations it was given instead of recomputing them from the type.
- [N-U08-130] Each returned movement is a draft copy of the original with opposite locations, taken from stock (make-to-stock), linked as returned-from the original movement, without the original final destination, carrying the same references, and keeping the partner for outgoing returns.
- [N-U08-131] The returned movement is also linked into the chain of the original: it becomes a successor of the original movement and of equivalent siblings, so that a multi-step return follows the original path through staging areas.
- [N-U08-132] Before the return is created, pending successor movements of the returned movements are released from reservation so the returned goods can be re-planned.
- [N-U08-133] If no quantity is entered the return is refused. Otherwise the new return is confirmed and reserved immediately.
- [N-U08-134] Exchange: the wizard creates the return and then, for receipts, an exchange transfer built directly from the return and independent of the original movements, and for deliveries a replenishment need for the same products at the original destination.
- [N-U08-135] Push rules are not applied to a movement that is itself a return when the rule destination equals the original destination, so returned goods are not sent through the original steps again.
- [N-U08-136] A backorder created from a return keeps the link to the original transfer.
- [N-U08-137] Refund hand-off: when the accounting-linked inventory module is installed the wizard lines carry an update-quantities-on-the-order flag, on by default, copied to the returned movement; sales and purchasing then reduce the delivered or received quantity of the order lines for flagged returns only.
- [N-U08-138] When sales is installed the returned movement keeps the order line link and the return transfer keeps the order link.

### STATE
- [N-U08-139] A return follows the ordinary transfer states: it starts as draft, then becomes waiting or ready after confirmation and reservation.

### OPTIONALITY
- [N-U08-140] The return operation type, the refund flag and the exchange action are optional. A movement with a negative demand is an alternative expression of a return and is turned into a reversed movement on confirmation.

### DEPENDENCY
- [N-U08-141] Refund flags, order links and purchase-side data come from other modules; the purchasing module's return extension does not match the signature of the base method, so its runtime effect is uncertain.

### CONSTRAINT
- [N-U08-142] A done movement cannot be cancelled, so reversal is possible only by a return.

### RISK
- [N-U08-143] Returns of returns and multi-step returns depend on link rules between sibling movements; mislinked chains can double count quantities or push goods twice.

### UNKNOWN
- [N-U08-144] Whether a quantity larger than what was delivered can be returned is not established: no upper bound was found on the wizard line, and the purchasing extension may not run.

## CAP-U08-06 Cancellation, unreserve, edit restrictions and date propagation (neutral)

### WHAT
- [N-U08-150] Cancelling stops a transfer or a movement before it is done: reservations are released, linked follow-up movements may be cancelled or released, and the document becomes cancelled. After completion, changes are restricted by a lock regime and reversal is done by a return.

### WHY
- [N-U08-151] The restrictions after completion protect stock history and the documents that depend on it, since reversing a done movement would undo everything triggered after it.

### BUSINESS RULE
- [N-U08-152] A done movement cannot be cancelled, except movements that went to the inventory-loss location. The refusal tells the user to create a return.
- [N-U08-153] Cancelling a movement clears its picked marker, releases its reservation, sets it to cancelled, removes its links to predecessors and resets its supply method to take-from-stock.
- [N-U08-154] Cancellation propagates forward only when the movement is set to propagate (on by default for a movement, off by default for a rule). The next movement is then cancelled when all its other predecessors are also cancelled, it belongs to the same destination and it is not done; other next movements become independent and are served from stock. Without propagation, next movements are only unlinked once all siblings are done or cancelled.
- [N-U08-155] An optional system parameter makes a cancellation also cancel predecessors that are not done. It is not set in the studied database.
- [N-U08-156] Cancelling a transfer cancels all its movements and locks it; a transfer that has no movement is set to cancelled directly.
- [N-U08-157] Deleting a transfer first cancels its movements; movements linked to other operations cannot be deleted unless draft or cancelled; detailed lines of done or cancelled movements cannot be deleted, and the user is advised to set the processed quantity to zero instead.
- [N-U08-158] The quantity of a cancelled movement cannot be changed, and the unit of measure of a done movement cannot be changed.
- [N-U08-159] Changing the demand of an open, non-draft movement posts a note on the transfer; lowering it below the reserved quantity releases the surplus reservation.
- [N-U08-160] Transfers are locked by default. A locked, done transfer cannot have its processed quantities or dates edited and a locked transfer cannot have the initial demand of non-draft movements changed. Only inventory administrators have the lock and unlock action; unlocking a done transfer allows editing its processed quantities.
- [N-U08-161] Editing the processed quantity of a done line reverses the original stock effect and applies the new one, posts a note, and releases and reruns the reservation of the successor movements.
- [N-U08-162] The scheduled date of a transfer is the earliest date of its open movements under the as-soon-as-possible policy and the latest under the all-at-once policy. Setting it manually writes that date on all open movements; it is refused for cancelled transfers and ignored for done ones.
- [N-U08-163] The deadline of a transfer is likewise the earliest or latest movement deadline, and a transfer is flagged as late when its deadline is earlier than its scheduled date.
- [N-U08-164] Deadlines propagate along the chain of linked open movements: changing one shifts the others by the same difference, and a note is posted on the affected documents when a deadline moves because of a delay upstream.
- [N-U08-165] A delay alert is raised on a movement when the latest date among its open predecessors is later than its own date.
- [N-U08-166] Lead times: a movement created by a pull rule is dated at the planned date minus the rule lead time; a movement created by a push rule is dated at the previous date plus the rule lead time. The planned date of a need raised from a movement comes from the movement date and the lead times of the rules on the path; reordering needs use the lead-time horizon (total lead days plus the company horizon) at midday in the company time zone.
- [N-U08-167] The company replenishment horizon defaults to 365 days.
- [N-U08-168] Writing the completion date on a done transfer propagates it to its movements, and the date of a done movement propagates to its lines.

### STATE
- [N-U08-169] A warehouse can be archived only when there are no unfinished movements for its operation types and no foreign operation type uses its locations.

### OPTIONALITY
- [N-U08-170] Lock and unlock, the cancel-predecessors parameter and the company horizon are optional settings; in the studied database the horizon is 365 days and the parameter is not set.

### DEPENDENCY
- [N-U08-171] Manufacturing, repair and subcontracting extend movement cancellation, and the batch module removes cancelled transfers from their batch.

### CONSTRAINT
- [N-U08-172] The type of a location cannot be changed to a virtual one when it holds stock, an internal location that holds stock cannot be converted or archived, and a location used by a warehouse cannot be archived.

### RISK
- [N-U08-173] When a head movement is cancelled without propagation, downstream movements are switched to take-from-stock and unlinked silently, which can leave later steps waiting for stock that no longer arrives.

### UNKNOWN
- [N-U08-174] The effect of editing processed quantities of an unlocked done transfer on downstream accounting and valuation was not traced and needs runtime and U10 confirmation.

## CAP-U08-07 Procurement, scheduler and replenishment (neutral)

### WHAT
- [N-U08-180] Replenishment turns a need for a product at a location into movements, purchase orders or manufacturing orders through rules. Needs come from sales, from chained make-to-order movements, from reordering rules, from exchanges and from manual replenishment.
- [N-U08-181] A need is described by product, quantity, unit of measure, destination location, origin text, company and a set of values: planned date, preferred routes, warehouse, priority, references and the originating reordering rule.
- [N-U08-182] In this version, needs and the movements they generate are tied together by reference records linked to movements; there is no separate procurement-group record.

### WHY
- [N-U08-183] Automatic replenishment keeps stock between a minimum and a maximum without manual ordering, and chaining make-to-order operations makes supply follow demand.

### BUSINESS RULE
- [N-U08-184] For a make-to-order movement, confirmation raises a need for the movement's source location; the movement created to satisfy that need is linked as its predecessor. Errors are shown to the user except when the need comes from a reordering rule, where they are collected.
- [N-U08-185] For take-from-stock-else-order rules, only the shortfall (demand minus free stock, after what other such movements already take) is requested, and the movement itself is created as take-from-stock.
- [N-U08-186] A reordering rule names a product, a location and warehouse, a minimum, a maximum, a trigger (automatic or manual), an optional route and an optional replenishment multiple. There is one rule per product, location and company, the minimum must not exceed the maximum, and the maximum defaults to the minimum.
- [N-U08-187] Quantity to order: when the forecast (on hand plus incoming minus outgoing up to the lead horizon, plus quantities already in progress) is below the minimum, order up to the larger of minimum and maximum minus the forecast, rounded up to the replenishment multiple; otherwise nothing. A quantity typed by the user on a manual rule overrides the computed one.
- [N-U08-188] Automatic rules are processed by the scheduler and also when a movement leaving the location is confirmed (unless switched off by a parameter); manual rules appear in the replenishment list and are processed by a user action. Snoozing exists only for manual rules.
- [N-U08-189] The scheduler runs daily: it recomputes quantities and deadlines of automatic rules, raises the needs, retries reservation of every due movement and merges duplicate stock records; with expiry dates installed it also raises lot expiry alerts.
- [N-U08-190] Reordering rules are processed in batches of one thousand. Failures are collected per rule and recorded as warning activities on the product, without stopping the other rules, and each batch is committed when the scheduler uses its own transaction.
- [N-U08-191] The procurement date of a reordering rule is its lead-horizon date at midday in the company time zone, moved earlier by the global horizon when one is set.
- [N-U08-192] The rule path is chosen with the route on the reordering rule if any, otherwise the routes of the product and its category; when no rule is found the rule is flagged with a supply warning and the replenishment fails with a message.
- [N-U08-193] A reordering rule belongs to a warehouse; its location choices are limited to that warehouse and to locations outside any warehouse. Locations flagged for replenishment are the ones the replenishment view manages, and a parent and a child cannot both be flagged.
- [N-U08-194] Manual replenishment can force the quantity up to the maximum or run the quantity in the list; manual rules created by the system are removed automatically when nothing remains to order.
- [N-U08-195] The make-to-order route makes a delivery wait for an upstream need; resupply between warehouses uses make-to-order rules, and the set of such rules is rebuilt when the number of delivery steps changes.
- [N-U08-196] A chain of rules that loops back on itself is detected and reported as an invalid configuration.

### STATE
- [N-U08-197] A reordering rule is active or archived, automatic or manual, and manual rules may be snoozed until the next scheduler run. In the studied database the scheduler is active and runs every day; no reordering rule exists.

### OPTIONALITY
- [N-U08-198] Purchasing, manufacturing, subcontracting and drop-shipping add rule actions (buy, manufacture) and extend needs; supplier lead times feed the lead days. Without them only stock-move rules exist.

### DEPENDENCY
- NOT APPLICABLE or no statement recorded for this section.

### CONSTRAINT
- [N-U08-199] A reordering rule cannot change company, automatic rules cannot be snoozed, and the minimum cannot exceed the maximum.

### RISK
- [N-U08-200] Because the scheduler runs once a day and the company horizon defaults to 365 days, shortages may be detected late unless confirmation triggers the check, and orders may be raised far ahead of need.

### UNKNOWN
- [N-U08-201] The behaviour of the scheduler across several companies and at a given time of day, and the processing of real reordering rules, needs runtime confirmation; the studied database has no reordering rules.

## CAP-U08-08 Operation types, numbering, default locations, location types and removal strategies (neutral)

### WHAT
- [N-U08-215] An operation type defines a kind of transfer (receipt, delivery, internal, and further kinds added by other modules such as manufacturing, repair and drop-shipping): its numbering, default source and destination locations, reservation moment, backorder policy, shipping policy, lot rules, label and print settings, and its warehouse.
- [N-U08-216] A location is a place that holds or counts stock. Location types are: vendor, virtual (a grouping parent that cannot hold goods), internal, customer, inventory loss, production and transit.
- [N-U08-217] Removal strategies decide in which order stock is taken, and putaway rules decide where arriving goods are stored; each strategy is a named record with a method.

### WHY
- [N-U08-218] Location types give logistics and accounting meaning to places: outside parties and counterpart locations let movements balance without holding stock.

### BUSINESS RULE
- [N-U08-219] Each operation type owns a number sequence. A transfer reference is built from the warehouse code, the type code and a five-digit counter; types without a warehouse use the type code alone. A new type without a sequence gets one automatically, and renaming the type code rewrites the prefix.
- [N-U08-220] Default locations: receipts take from the vendor location and deliver into the warehouse stock (or its input area); deliveries take from stock (or its output area) and go to the customer location; other types use the warehouse stock. A new transfer copies the defaults of its type, and a partner's own customer or vendor location overrides them.
- [N-U08-221] Locations on a transfer pass down to its movements. A movement's destination is replaced by the final destination when the final destination lies inside it, and the intermediate destination is kept for chains whose final target is elsewhere (for example inter-company deliveries).
- [N-U08-222] A warehouse creates eight operation types: Receipts, Delivery Orders, Pick, Pack, Quality Control, Storage, Internal Transfers and Cross Dock, with codes IN, OUT, PICK, PACK, QC, STOR, INT and XD; they are activated according to the steps, and internal transfers are active only when multiple locations are enabled.
- [N-U08-223] By default receipts may create new lots, deliveries use existing lots, and delivery types generate shipping labels.
- [N-U08-224] Locations form a tree with a full name built from the parent chain; barcodes are unique per company; a location without a company is shared; changing the company is forbidden; the inter-company transit location cannot be deleted, only archived.
- [N-U08-226] Vendor, customer, inventory-loss and production locations do not hold reservable stock.
- [N-U08-227] For every company the system creates an inter-warehouse transit location (archived until needed), an inventory adjustment location with the product default property, a production location, a scrap location when no inventory-loss location exists, and a scrap number sequence.
- [N-U08-228] Shipped seed data includes the vendor and customer locations, the inter-company transit location (archived), default partner locations, a main warehouse with short code WH, the removal strategies first-in-first-out, last-in-first-out, closest location and least packages, and number sequences for reordering rules, internal transfers, serial numbers and packages.
- [N-U08-229] Putaway rules pick a sub-location inside the arrival location by product, category or package type, in order of specificity; a storage category can limit what a location accepts by weight, capacity and product mix.

### STATE
- [N-U08-231] An operation type is active or archived; types not needed by the chosen steps are archived.

### OPTIONALITY
- [N-U08-232] The Storage Locations setting enables internal transfer types and manual location creation; the Multi-Step Routes setting enables push and pull rules; consignment owners, packages and lots are separate optional settings.

### DEPENDENCY
- [N-U08-233] Other modules extend the list of operation type kinds; in the studied database manufacturing, repair and drop-shipping kinds exist.

### CONSTRAINT
- [N-U08-234] The company of an operation type cannot be changed, and a location cannot be turned into a scrap location while a manufacturing operation type delivers into it.

### RISK
- [N-U08-235] Renaming a warehouse code rewrites the sequence prefix for future transfers only, so references of existing documents keep the old code and may look inconsistent.

### UNKNOWN
- [N-U08-236] Real numbering behaviour with several warehouses or companies (counter ranges, padding changes) was not observable because the studied database has no transfers.

## CAP-U08-09 Batch transfers, carriers and shipping, drop-shipping (neutral)

### WHAT
- [N-U08-245] A batch groups several transfers of the same operation type and company so that one person can process them together. A wave is a batch built from detailed lines of transfers; when only part of a transfer is taken, the transfer is split.
- [N-U08-257] A delivery method (carrier) defines how shipping is priced and sent: a fixed price, price rules, or an external connector type. It carries a delivery product, country, state and postal-code filters, weight and volume limits, product tag filters, a margin, a free-shipping threshold, an integration level and a tracking link template.
- [N-U08-268] Drop-shipping delivers goods directly from a vendor to a customer: a purchase triggers a transfer from the vendor location to the customer location with no warehouse stock involved.

### WHY
- NOT APPLICABLE or no statement recorded for this section.

### BUSINESS RULE
- [N-U08-247] Transfers that can be in a batch must be waiting, confirmed or ready (draft ones only while the batch itself is draft), belong to the batch company and share its operation type; adding or changing them is checked against this.
- [N-U08-248] Confirming a batch requires at least one transfer and confirms them. Validating a batch validates its transfers together after one joint check; empty waiting transfers are taken out of the batch without being cancelled, and a note records on each transfer that it was transferred by the batch.
- [N-U08-249] Cancelling a batch cancels it and detaches its transfers; an in-progress batch left with no transfer is cancelled automatically; a done batch cannot be deleted.
- [N-U08-250] Batch and wave names come from their own number sequences combined with the operation type code.
- [N-U08-251] When automatic batching is enabled on an operation type, a ready transfer is placed in a compatible open batch, or a new batch is formed with another compatible ready transfer, or with the transfer alone. Compatibility is judged on contact, destination country, source location or destination location, and carrier when the delivery batching module is installed, within limits on lines, transfers and weight.
- [N-U08-252] Enabling automatic batching requires at least one grouping option; new automatic batches are confirmed automatically by default.
- [N-U08-253] Automatic waves group detailed lines by product, category or location when their transfers are ready; taking only some lines of a transfer splits the transfer, and waves are never reused as targets of ordinary transfer grouping.
- [N-U08-254] Validating a transfer that belongs to a batch with other unfinished transfers detaches it first, to keep the states of the batch consistent; backorders then re-enter automatic batching.
- [N-U08-255] The responsible user of a batch is copied to its transfers. Batches can be merged only if they have the same operation type, the same kind and the same state and are not done or cancelled.
- [N-U08-258] A carrier is available for an order or transfer when the address matches its country, state and postal prefix filters, the required tags are present and the excluded tags absent, and weight and volume are within limits; a rule-based carrier must in addition produce a price.
- [N-U08-259] Rating depends on the carrier type: fixed uses the delivery product price from the order pricelist; rule-based uses the first price rule whose condition on price, weight, volume or quantity holds, or fails with not available. The price is then adjusted for taxes by the fiscal position and margins (percentage plus fixed, except for fixed price), and made free above the threshold (not for rule-based carriers).
- [N-U08-260] On a sales order the user chooses the method in a wizard that rates it and then adds a delivery line, replacing the previous one unless it was already invoiced; a pickup point selected on the order becomes a delivery address on confirmation.
- [N-U08-261] The carrier follows the goods: a carrier selected on the order is set on pending deliveries; transfers created by a rule that propagates the carrier inherit the carrier and tracking reference of the previous transfer; moves of orders with different carriers are not combined in one transfer; the carrier can also bring its own routes.
- [N-U08-262] At delivery validation, if the carrier integration level is rate-and-ship, the operation type prints labels and no tracking reference exists, the shipment is sent to the carrier; the returned cost is stored on the transfer, the tracking reference is copied across the whole chain of transfers, and the shipment is logged.
- [N-U08-263] The invoicing policy is estimated (the customer is charged the estimate) or real (the order line is created at zero price with the estimate in its name and its price is replaced by the real cost after shipping).
- [N-U08-264] The generic fixed and rule-based carriers have a tracking link template and no shipment cancellation (cancelling raises not implemented); cancelling a shipment clears the tracking reference.
- [N-U08-265] Products shipped with different carriers cannot be put in the same package; the shipping weight of a package is stored, and the weight of a transfer is the sum of its movements.
- [N-U08-266] A return label can be generated on delivery or offered on the portal for carriers that support it.
- [N-U08-269] For each company the system creates a drop-ship operation type with no warehouse (vendors to customers), its number sequence and a buy rule on a drop-ship route that can be selected on sales lines, products and categories; the route is excluded from manual replenishment.
- [N-U08-270] A transfer is a drop-ship when it goes from a vendor (or a company-less transit) to a customer (or a company-less transit); drop-ship transfers are counted separately from deliveries on the sales order and from receipts on the purchase order, and are linked to the sale through the references.
- [N-U08-271] On the sales side drop-ship lines are treated as make-to-order, the quantity to procure is the purchase quantity and the line cannot be re-edited once purchased; on the purchase side the delivery address is set, and when one vendor order covers several sales orders one transfer per sales order is created.
- [N-U08-272] Purchase lines linked to different sales lines are not merged, so that delivered quantities can be computed per sale; the drop-ship route does not set a vendor address on the rule.

### STATE
- [N-U08-246] A batch is draft, in progress, done or cancelled. Confirming a batch moves it to in progress; it becomes cancelled when all its transfers are cancelled and done when all non-cancelled transfers are done.

### OPTIONALITY
- [N-U08-256] Batching is an optional module. New warehouses enable automatic batching by contact on their receipt and delivery types; in the studied database that option is not set on any operation type because the warehouse existed before installation.

### DEPENDENCY
- [N-U08-267] Delivery methods depend on sales, not on inventory; the link to transfers is made by a separate bridge module. Connector modules for external carriers are separate and were not studied.

### CONSTRAINT
- NOT APPLICABLE or no statement recorded for this section.

### RISK
- [N-U08-273] No accounting or valuation behaviour specific to drop-shipping is declared in this module; how the simultaneous receipt and delivery is valued belongs to the valuation unit and was not read.

### UNKNOWN
- [N-U08-274] Runtime effects of shipments and drop-ship flows (carrier errors, multi-sale vendor orders) are not observable in the studied database, which has no orders or transfers.

## CAP-U08-10 Roles, record rules and multi-company or warehouse scope (neutral)

### WHAT
- [N-U08-290] Access to inventory is governed by two roles, inventory user and inventory administrator (the administrator includes the user), plus hidden feature groups that switch screens and features on, and company rules that confine documents to the companies a user may work in.
- [N-U08-291] The hidden feature groups cover multiple locations, multiple warehouses, lots and serial numbers, GS1 lot barcodes, lot display on delivery slips, packages, push and pull flows, stock owners, partner warnings, signatures on deliveries and the reception report.

### WHY
- NOT APPLICABLE or no statement recorded for this section.

### BUSINESS RULE
- [N-U08-293] All internal users may read warehouses, locations, operation types, rules, routes, stock levels, removal strategies and packages, and have full rights on detailed movement lines. Inventory users may create, edit and delete transfers; administrators fully manage warehouses, locations, operation types, routes, rules, putaway rules and reordering rules, which inventory users can only read. Any internal user may create references between documents.
- [N-U08-294] Inventory users may read, write and create movements but not delete them; administrators may also delete them.
- [N-U08-295] The return, backorder, replenishment, stock history and rule report wizards are available to inventory users.
- [N-U08-296] Every document family is confined to the user's allowed companies by rules that apply to everybody. Transfers, operation types, movements, reordering rules, warehouses, scrap and the forecast report are strictly per company; locations, routes, rules, detailed lines, stock levels, packages, lots and storage categories also include records that have no company.
- [N-U08-297] No rule or group links a user to a warehouse: the only warehouse default for a user is the first warehouse of the current company. Warehouse-level restriction of what an inventory user may process is therefore not provided by these modules.
- [N-U08-298] Batches are managed by inventory users and confined to the company. Delivery methods are readable by salespeople and inventory users, managed by sales managers and inventory administrators, and confined to allowed companies or shared. The drop-shipping module declares no access rights or rules of its own.
- [N-U08-302] Inter-company flow uses a shared transit location without company. It is archived until a second company is created; creating a company activates it and makes it the customer and vendor location of the partners of the other companies in both directions. Rules that deliver to it also use the customer delivery rules, moves pushed into another company run with elevated rights, packages can be unpacked on arrival, and drop-shipping treats a company-less transit as an outside party.
- [N-U08-303] Each company has its own inter-warehouse transit location, and the partner of a warehouse gets it as customer and vendor location, so that resupply between warehouses is not treated as a sale or a purchase.

### STATE
- [N-U08-292] In the studied database all internal users are given the groups for multiple locations, push and pull flows, packages, lots, owners, partner warnings and the reception report; the multiple-warehouse group is not given because there is a single warehouse, and only two users are inventory administrators.
- [N-U08-299] The counts of declared access rights, rules and groups match the studied database: 77 access rows, 16 rules and 13 groups for the core inventory module, 3 rows and 1 rule for batches, 10 rows and 1 rule for delivery methods, and 7 rows for the shipping bridge.

### OPTIONALITY
- [N-U08-306] The multiple-warehouse group is added to or removed from all internal users automatically according to whether any company has more than one active warehouse.

### DEPENDENCY
- NOT APPLICABLE or no statement recorded for this section.

### CONSTRAINT
- [N-U08-300] Some buttons are shown at view level to all internal users (confirm, cancel, return) while the model rights still require an inventory user, and validation and lock actions are restricted to inventory users and administrators respectively.
- [N-U08-301] The company of warehouses, locations, operation types and reordering rules cannot be changed, and confirmation and validation check that all records belong to a consistent company.

### RISK
- [N-U08-304] Transfers and movements are limited to allowed companies but not to warehouses, so any inventory user can process any warehouse of the company; and every internal user holds full model rights on detailed movement lines, so protection relies on the parent document rights and on view-level restrictions.

### UNKNOWN
- [N-U08-305] Whether other installed modules (sales, purchasing, portal) add rules or rights that widen or narrow access to transfers was not studied.
