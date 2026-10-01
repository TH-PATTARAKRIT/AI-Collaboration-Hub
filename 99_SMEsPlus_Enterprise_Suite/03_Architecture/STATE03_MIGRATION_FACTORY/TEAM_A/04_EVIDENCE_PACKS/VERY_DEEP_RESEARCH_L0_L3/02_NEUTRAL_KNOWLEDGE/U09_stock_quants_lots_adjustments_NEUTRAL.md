# U09 Neutral Knowledge — On-hand stock, counting, lots, packages and scrap

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION
> Layer: NEUTRAL KNOWLEDGE (clean-room). Source basis: Odoo 19 Community, revision 19.0.post20260921. Written as business and process rules only; each statement is tagged with an id that links to its evidence in the restricted layer.
> Scope: unit U09 — on-hand quantity records, physical counting and adjustments, cycle counts, reversal, financial hooks, lots and serial numbers, packages, scrap, product quantity computations and history views, roles and scheduled behaviour.

## CAP-U09-01 On-hand quantity records and quantity integrity

### WHAT
- [N-U09-001] The system keeps an on-hand record for every distinct combination of product, storage location, lot or serial number, package and stock owner. Each record holds an on-hand quantity and a reserved quantity, and the free quantity of a record is on-hand minus reserved.

### WHY
- [N-U09-002] On-hand records give one location-accurate source of truth for stock, so that availability, counting, valuation and traceability all read the same figures.

### BUSINESS RULE
- [N-U09-003] On-hand and reserved quantities cannot be typed in by ordinary users. They change only when a stock movement is completed, when a reservation is created or released, or when a physical count is applied.
- [N-U09-004] When a reserved quantity is reduced, it never falls below zero.
- [N-U09-005] Only stockable products can have on-hand records. Consumable-type items and services cannot.
- [N-U09-006] On-hand records cannot be copied by users.
- [N-U09-007] In counting mode, a user may create a new on-hand line only by supplying a restricted set of attributes, and may never change the product, location, lot, package or owner of an existing line. Attempts to manually edit a line held in an inventory-loss location are silently ignored.
- [N-U09-008] Deleting an on-hand record is reserved to the inventory administrator or the system. When an administrator deletes one, the system first books a movement that brings its quantity to zero.
- [N-U09-009] Negative on-hand quantity is not blocked by the movement engine. A completed movement can drive a record below zero, and a dedicated filter lists negative stock. When a completed movement leaves too little free stock, reservations held by other not-yet-picked operations on the same item are released to compensate.
- [N-U09-010] The order in which on-hand records are consumed follows the removal strategy of the product category, else of the nearest parent location, else oldest-first. The strategies are oldest-first, newest-first, closest location and fewest packages, plus first-expiry-first-out when the expiry extension is installed.

### STATE
- [N-U09-011] An on-hand record is created at the first receipt, count or adjustment of a combination, is updated by movements and reservations, and is removed by a maintenance routine once it is empty and not assigned to a counter. Duplicates created by concurrent activity are merged by the same routine, which also re-synchronises reservations with open operations.

### OPTIONALITY
- [N-U09-012] Counting mode is available only to users of the inventory user group. The maintenance routine runs from the daily scheduler and when counting or stock screens are opened, and a system parameter can switch off the screen-triggered runs.
- [N-U09-013] With the expiry extension, quantities past their removal date are excluded from free quantity. With the manufacturing extension, kit products cannot hold on-hand records. With the accounting extension, each record exposes a monetary value for managers.

### DEPENDENCY
- [N-U09-014] On-hand records are maintained by the transfer engine described in another study unit. This capability covers only the record side of reservation and quantity updates.

### CONSTRAINT
- [N-U09-015] A serial-numbered item cannot be on hand more than once within the same location tree.
- [N-U09-016] A location of virtual type cannot hold goods, and a lot or serial number on a record must belong to the same product as the record.

### RISK
- [N-U09-017] Concurrent updates can transiently create two records for the same combination. Correctness then depends on the later merge routine, which silently logs and skips if its statement fails.
- [N-U09-018] Because negative stock is not blocked, availability figures can disagree with physical reality until a count corrects them.

### UNKNOWN
- [N-U09-019] Real behaviour of row locking and duplicate creation under heavy concurrent load is not confirmed by the source alone and needs a runtime test.

## CAP-U09-02 Inventory counting and applying adjustments

### WHAT
- [N-U09-020] Users record a counted quantity against each on-hand line, review the difference to the system quantity, and then apply the counts, one line at a time or in bulk. Applying a count completes a stock movement against an inventory-loss location so that the on-hand quantity equals the counted quantity.

### WHY
- [N-U09-021] Physical stock must be reconciled to the system records while keeping the correction itself a traceable stock movement rather than a silent overwrite of the quantity.

### BUSINESS RULE
- [N-U09-022] Recording a count is separate from applying it. Entering a counted figure only stores the figure and the difference, and has no stock effect until the count is applied.
- [N-U09-023] The difference is counted quantity minus system on-hand quantity, and it is shown only while a count has been set on the line. A line whose on-hand quantity has changed since the count was entered is flagged as outdated.
- [N-U09-024] Applying an outdated line forces the user to choose between keeping the counted quantity (the difference is recomputed) and keeping the original difference (the counted quantity is shifted by it), or to discard and resolve manually.
- [N-U09-025] Applying in bulk, or with the header Apply button, asks for a reason, whose default text is Physical Inventory, and a counting date, which defaults to now. Only lines that currently carry a counted figure are applied. The reason is not enforced as mandatory.
- [N-U09-026] Applying a single line from its own row button skips the reason and date prompt. The resulting movement then receives an automatic reference reading Product Quantity Updated, or Product Quantity Confirmed when the difference is zero, followed by the name of the user who created it.
- [N-U09-027] A positive difference books a movement from the inventory-loss location into the counted location. A zero or negative difference books a movement from the counted location to the inventory-loss location. A zero difference still books a zero-quantity confirmation movement that is kept as history.
- [N-U09-028] The adjustment movement is created already picked and is completed immediately. It carries the lot, package and owner of the counted line, and is restricted to the owner when the line has one. The movement is flagged as an inventory adjustment so that it can be filtered and reversed.
- [N-U09-029] The counting date typed by the user becomes the date of the movement and its lines. The date on which each location was last counted is stamped with the application date, and the next scheduled count date of the applied lines is recomputed.
- [N-U09-030] Editing the inventoried-quantity shortcut field applies the change immediately with no separate apply step, and creating a line in counting mode with a counted figure sets the counter and the scheduled date to the creating user and today.
- [N-U09-031] A manager can request counts on selected lines, giving a due date and optionally an assigned counter. For tracked items all sibling lots in the same location are included. Whether the counter may see the expected quantity is a single system-wide setting.
- [N-U09-032] Clearing a count resets the counted figure, the difference, the set flag and the assignee. The Set action copies the on-hand quantity into the counted figure and assigns the current user. Setting a count to zero is reserved to administrators.
- [N-U09-033] Editing the on-hand quantity directly on a product form creates and applies an adjustment in the stock location of the first warehouse of the current company, only for stockable products whose entered quantity is not negative.

### STATE
- [N-U09-034] A line goes from not counted to counted when a figure is entered, when the Set action is used or when a count is requested. A counted line becomes outdated if its on-hand quantity moves, and returns to not counted once applied or cleared.

### OPTIONALITY
- [N-U09-035] Apply is available to every inventory user. Requesting counts, clearing, setting to zero and relocating are administrator actions. The lot, package and owner columns appear only when the matching features are enabled. With the accounting extension an accounting date can be set on a line.

### DEPENDENCY
- [N-U09-036] Applying a count depends on the transfer engine completing the generated movement, on the inventory-loss location configured for each product and company, and on the valuation extension for any accounting effect.

### CONSTRAINT
- [N-U09-037] Counting screens list on-hand lines located in internal or transit locations only. Counting mode, and therefore counting edits, is limited to users of the inventory user group.

### RISK
- [N-U09-038] The row-level Apply path has no reason, so an audit trail relying on every adjustment carrying a reason would be incomplete. The reason itself is optional even in the bulk path.
- [N-U09-039] The conflict and warning dialogs are granted only to administrators, so an ordinary inventory user may be blocked when applying outdated lines or re-setting counts.

### UNKNOWN
- [N-U09-040] It is not confirmed from source whether an ordinary inventory user can open the conflict and warning dialogs, nor how the counted-quantity widget behaves in the browser; both need a runtime test.

## CAP-U09-03 Cycle counting and scheduling

### WHAT
- [N-U09-041] Each internal or transit location of a company can carry a counting frequency in days, and each company can carry an annual counting date. From these, every on-hand line receives a scheduled date on which it is due for counting.

### WHY
- [N-U09-042] Different storage areas deserve different counting cadences, and a company-wide yearly count acts as the safety net for areas without their own cadence.

### BUSINESS RULE
- [N-U09-043] A location frequency of zero means no cyclic counting for that location. A negative frequency is refused, and a frequency so large that the resulting date cannot be represented is refused.
- [N-U09-044] The next planned count date of a location is today plus the frequency when the location has never been counted, the last count date plus the frequency while that date is still in the future, and tomorrow when the location is already overdue.
- [N-U09-045] The scheduled date of an on-hand line is the earlier of its location next planned date and the company annual date. When the location has no cyclic date the company annual date applies, and when neither exists the line has no scheduled date.
- [N-U09-046] The company annual date is a month and a day, defaulting to 31 December. A day of zero or less is read as the first of the month, a day beyond the month end is read as the last day of the month, and once the date of the current year has passed the next year is used. Choosing no month switches the annual date off.
- [N-U09-047] A line scheduled date is computed only when the line is created or its location changes. Changing a location frequency later does not rewrite dates already stored on existing lines, but applying a count reschedules the applied lines.
- [N-U09-048] Nothing is created automatically when a scheduled date arrives. Due lines are only surfaced through a To Count filter and highlighted in the counting list. People must request or enter the counts.

### STATE
- [N-U09-049] A line is scheduled, becomes due when its date is reached, is counted and applied, and is then rescheduled from the location cadence or the company annual date.

### OPTIONALITY
- [N-U09-050] The frequency is optional per location and the annual date can be disabled. The cyclic counting section appears only for internal or transit locations that belong to a company. The location screens are reachable only when the storage locations feature is enabled.

### DEPENDENCY
- [N-U09-051] Rescheduling depends on counts being applied (the counting capability). The annual date lives in company settings visible to administrators.

### CONSTRAINT
- [N-U09-052] Frequency must be zero or positive. Locations that belong to no company never receive a cyclic date.

### RISK
- [N-U09-053] A missed scheduled date has no system consequence: no blocking, no notification and no automatic task. Cyclic counting therefore depends entirely on people watching the To Count list.

### UNKNOWN
- [N-U09-054] Whether any additional installed extension adds automatic count tasks or notifications is not covered by the base stock module and is not confirmed here.

## CAP-U09-04 Reversal and correction of applied adjustments

### WHAT
- [N-U09-055] An applied count is never erased. The system offers a Revert action on adjustment movement lines that books an opposite completed movement, and a later count can also correct quantities again.

### WHY
- [N-U09-056] Mistaken counts must be correctable while the original movement stays in the history, so that the audit trail shows both the error and its correction.

### BUSINESS RULE
- [N-U09-057] A completed movement line cannot be deleted. It can only be compensated by a further movement. Desktop users cannot edit completed movement lines.
- [N-U09-058] The Revert action works on selected movement lines that are flagged as inventory adjustments and have a non-zero quantity. If none of the selected lines qualify, the user receives an error notice and nothing is booked.
- [N-U09-059] A reversal books a new completed adjustment movement with source and destination swapped, the same quantity, lot and owner, and the package roles swapped. Its reference reads the original reference followed by the word reverted.
- [N-U09-060] The original line is not marked as reverted, and the system does not check whether a reversal already exists, so the same line can be reverted more than once.
- [N-U09-061] Stock relocations booked by the system as adjustment-type movements, such as quantity, lot or package relocation and unpacking, are flagged like counts and therefore can be reverted with the same action. Scrap movements are not flagged as adjustments and cannot.
- [N-U09-062] Asking to cancel a completed movement whose destination is an inventory-loss location has no effect, and a completed scrap order cannot be deleted.

### STATE
- [N-U09-063] Applied adjustment stays completed. A revert adds a second completed adjustment. There is no separate reversed status on the original.

### OPTIONALITY
- [N-U09-064] Revert is a standard action in the movement history list and needs no configuration. No approval step is configurable in the base module.

### DEPENDENCY
- [N-U09-065] The reversal movement is itself valued and posted by the valuation extension in the same way as any adjustment, and it changes on-hand quantities through the normal transfer engine.

### CONSTRAINT
- [N-U09-066] Only users able to create stock movements can complete a reversal, in practice inventory users.

### RISK
- [N-U09-067] Double reversal is possible, the link between original and reversal is only the reference text, and a reversal after later movements can push on-hand negative without any block.
- [N-U09-068] On-hand records carry no change history of their own, so the audit trail of a count lives only in the movement lines and their references.

### UNKNOWN
- [N-U09-069] Behaviour of a reversal applied after later counts or movements on the same line, and any approval gating by extensions, is not confirmed and needs a runtime test.

## CAP-U09-05 Financial hooks of adjustments and scrap

### WHAT
- [N-U09-070] Counts and scrap both move goods to an inventory-loss location. Any accounting effect is created by the valuation extension, from the product valuation mode and from an account held on the location. The stock module itself only chooses the locations, passes an optional accounting date, and exposes values.

### WHY
- [N-U09-071] Stock corrections and write-offs should appear in the books as a loss or gain, optionally under their own account, instead of being blended into ordinary stock movements.

### BUSINESS RULE
- [N-U09-072] When a company is created it receives an inventory-loss location named Inventory adjustment, which becomes the default adjustment counterpart for all its products, and a second inventory-loss location named Scrap. A product may override the adjustment counterpart per company.
- [N-U09-073] Counts use the adjustment counterpart of the product. Scrap orders propose the lowest-numbered inventory-loss location of the company, which the user may change. When a company has only one inventory-loss location, counts and scrap share it and cannot be told apart by location.
- [N-U09-074] A location can carry a valuation account used to re-qualify goods that leave stock for that location. This is optional: without it, no accounting entry is created for movements to or from the location.
- [N-U09-075] An accounting entry for a stock movement is created only if the product is stockable, the movement counts as valued, the product uses perpetual valuation, the quantity is not zero and either the source or the destination location carries a valuation account.
- [N-U09-076] When the source location has an account, the entry debits the product stock valuation account and credits the location account. Otherwise it debits the destination location account and credits the stock valuation account, for the movement value.
- [N-U09-077] A count line may carry an accounting date. When present it dates the accounting entries of that count and is appended to the movement reference as accounted on that date. The date is cleared after the count is applied.
- [N-U09-078] A location belongs to the company valuation only when it is internal or transit and has a company. Inventory-loss locations are outside valuation, so a count or scrap changes the valued stock.

### STATE
- [N-U09-079] A count or scrap completes first as a stock movement; the accounting entry, if any, is created and posted in the same step at completion and is linked to the movement.

### OPTIONALITY
- [N-U09-080] Whether any entry is created depends on periodic or perpetual valuation per product category or company and on whether the loss location has an account. The restored configuration uses periodic valuation and no location has an account, so neither a count nor a scrap creates an entry at application time.

### DEPENDENCY
- [N-U09-081] The accounting treatment is owned by the valuation study unit; this capability documents only the stock-side hooks: locations, accounting date, and the exposure of values.

### CONSTRAINT
- [N-U09-082] A location cannot be switched to or from a type while it holds stock, a location cannot be marked as a scrap location while it is the destination of a manufacturing operation type, and goods cannot be placed in virtual locations.

### RISK
- [N-U09-083] Documentation that states the books are updated as soon as a count is applied holds only for perpetual valuation with an account on the loss location. Under periodic valuation the effect appears only at period closing.

### UNKNOWN
- [N-U09-084] The exact value and the closing entries produced for counts and scrap under periodic valuation belong to the valuation unit and are not confirmed here.

## CAP-U09-06 Lots, serial numbers and tracking

### WHAT
- [N-U09-085] Stockable products can be tracked by lot, by unique serial number, or not tracked. A lot or serial number is a master record belonging to one product, which gives traceability from receipt through storage to delivery and into manufactured goods.

### WHY
- [N-U09-086] Lot and serial traceability supports recalls, warranty and expiry control, and answers where a given batch came from and to whom it was sent.

### BUSINESS RULE
- [N-U09-087] Tracking can be chosen only on stockable products. Making a product non-stockable resets its tracking to none.
- [N-U09-088] Changing the tracking of a product that already has stock is not blocked. The user only receives a warning that stock on hand has no lot or serial number and that numbers can be assigned through a count. Switching the lots and serial numbers feature off is refused while any product is still tracked.
- [N-U09-089] A lot or serial number must be unique for a given product within a company. A record with no company clashes with any company-specific record of the same name and product, but two different companies may reuse the same name.
- [N-U09-090] If the name of a new lot is left empty it is taken from the sequence of the product, whose prefix can be customised per product. A series can be generated from a first number by incrementing its last group of digits while keeping the padding, and a next serial number is proposed from the most recent record.
- [N-U09-091] Each operation type has two switches: create new lots or serial numbers, and use existing ones. In the restored configuration receipts create new numbers, deliveries use existing ones, internal transfers use existing ones, manufacturing and repairs allow both, and dropshipping creates only. New lots can be created at completion only when the operation type allows it.
- [N-U09-092] When a movement of a tracked product is completed, a lot or serial number is mandatory, unless the movement is a count adjustment, a scrap, or belongs to an operation type with both switches off. A manual movement with no operation type and no number is refused. A missing number blocks completion with a message listing the products.
- [N-U09-093] When a lot name is typed at completion and no matching lot of the product exists for the company or for no company, a lot is created. For lot-tracked products one lot is created per product and name, while each serial number yields its own record. The company of the lot follows the product company and the line company.
- [N-U09-094] Using a serial number that already exists in an internal, transit or customer location triggers a warning on entry, and when a serial number would be on hand more than once in the same location tree the movement completion is refused.
- [N-U09-095] The product of a lot cannot be changed once movements exist for it, and the company of a lot cannot be changed to one that differs from the company of the location where it currently sits. Copying a lot gives it a name prefixed with copy of.
- [N-U09-096] The on-hand quantity of a lot is read from on-hand records in internal and transit locations, and can be computed as of a past date by backing out later movements. A lot shows a single location when all its stock is in one location, and setting that location books a relocation movement, refused when the lot is spread over several locations.
- [N-U09-097] The traceability report follows a lot upstream and downstream through completed movement lines, either through chained orders or by finding earlier receipts of the same lot into the source location. Deliveries linked to a lot include those reached through manufacturing consumption chains.
- [N-U09-098] With the expiry extension, a lot of a product that uses expiry dates receives expiration, best-before, removal and alert dates computed from durations in days held on the product. A scheduled job logs a to-do for lots with positive internal stock whose alert date has passed, once per lot. Delivering expired or removal-due lots asks the user to confirm, with the option to drop those lines. Turning tracking off on a product also turns expiry off.

### STATE
- [N-U09-099] A lot comes into existence at receipt, manufacture, manual creation or first count. With the expiry extension it moves from fresh to alert to expired by date, and is excluded from fresh quantity from its removal date.

### OPTIONALITY
- [N-U09-100] The lots and serial numbers feature, expiry dates, printing of standard barcodes and display on delivery slips are switches. In the restored configuration the lots and serial numbers feature and the expiry extension are enabled for all internal users.

### DEPENDENCY
- [N-U09-101] Lot creation depends on operation type settings and the transfer engine, expiry depends on the expiry extension and the scheduler, traceability into manufactured goods depends on the manufacturing extension, and valued lots depend on the valuation extension.

### CONSTRAINT
- [N-U09-102] A lot needs a name and a stockable tracked product. Name uniqueness is enforced by application checks, not by a database unique index. A lot cannot be created from a transfer whose operation type forbids creating new numbers.

### RISK
- [N-U09-103] Because tracking can change on products with stock, untracked on-hand quantity can coexist with tracked movements. Counts and scrap bypass the mandatory-number rule, so stock without numbers can be adjusted into existence.

### UNKNOWN
- [N-U09-104] How the system behaves when a lot-tracked product that already holds untracked stock is delivered with a lot, and the results of large series generation, need a runtime test.

## CAP-U09-07 Packages and package types

### WHAT
- [N-U09-105] A package is a physical container record, such as a box or pallet, that holds on-hand records and may itself sit inside another package. It has a reference taken from a sequence, an optional package type, and a location, company and owner derived from its content.

### WHY
- [N-U09-106] Packages let goods be moved, counted and shipped as units, with nested containers and a history of how each package travelled.

### BUSINESS RULE
- [N-U09-107] A package reference defaults from the sequence of its type, else from the global package sequence with prefix PACK. Emptying the reference of an existing package regenerates it. References are not required to be unique.
- [N-U09-108] The location of a package is derived from its first positive on-hand content, else from its first child package. Its company is set only when all its content shares one company, and its owner only when all its content shares one owner.
- [N-U09-109] Changing the location of a package by hand books a relocation movement of all its positive contents. This is refused for an empty package, and clearing the location is refused for a package that has content.
- [N-U09-110] Putting items into a pack creates a package of the chosen type, or reuses one, and makes it the destination container of the selected operation lines. A dialog asks for the type when the operation type requires it. Packages that end up with no remaining lines lose their destination, and putaway rules are re-evaluated for the new outermost package.
- [N-U09-111] A package cannot take one of its own contained packages as its destination container.
- [N-U09-112] When a transfer is completed, destination containers are applied. It is refused if packages placed in the same container end up in different locations, or if the container already holds content in another location, or if the same package content is moved more than once or split between two locations in the same transfer.
- [N-U09-113] Unpacking detaches contained packages and moves the loose on-hand lines out of the package by a relocation movement, then merges duplicate on-hand records. Removing a package from a transfer deletes the lines when the whole package is moved, otherwise it only clears the destination package.
- [N-U09-114] A package type holds dimensions, weight, maximum weight, a barcode, a reusable or disposable use, optional routes, storage capacity and its own sequence, created on demand. The barcode must be unique, and height, width, length and maximum weight must not be negative.
- [N-U09-115] Reusable package types are emptied and reused for batches and are not automatically promoted to destination container when all their children are added. Disposable ones are.
- [N-U09-116] When movement lines complete, a history record is kept for each package movement with origin and destination location, containers and transfers. Package weight is the base weight of its type plus the weight of its content and contained packages.

### STATE
- [N-U09-117] A package is empty, becomes filled by receipt or packing, may be assigned a destination container while a transfer is in progress, and then takes its new container and location at completion. Unpacking empties it.

### OPTIONALITY
- [N-U09-118] The packages feature, package types and reusable use are optional, and the screens appear when the feature is enabled. It is enabled for all internal users in the restored configuration.

### DEPENDENCY
- [N-U09-119] Packing depends on the transfer engine, on putaway rules, and, for shipping weight and carriers, on the delivery extension which also extends packages and package types.

### CONSTRAINT
- [N-U09-120] Package type barcode must be unique and dimensions must be non-negative. A package on an on-hand record must sit at the same location as that record, or be empty and without location.

### RISK
- [N-U09-121] Package references are not unique, packages can be partly moved, and destination containers must be consistent in location; inconsistent nesting is detected only when a transfer is completed.

### UNKNOWN
- [N-U09-122] Behaviour of deeply nested packages in large transfers and in the extensions for shipping is not covered and needs a runtime test.

## CAP-U09-08 Scrap orders

### WHAT
- [N-U09-123] A scrap order removes a quantity of a goods product, optionally of a given lot, package and owner, from a stock location into an inventory-loss location. It may carry reason tags and may trigger replenishment of the scrapped quantity.

### WHY
- [N-U09-124] Write-offs of damaged, expired or lost goods must leave stock immediately, be traceable to a reason and, if wanted, be replaced.

### BUSINESS RULE
- [N-U09-125] A scrap order has two statuses, draft and done. Validating completes it. There is no cancel and no reverse. A done order cannot be deleted, while a draft one can.
- [N-U09-126] The scrap reference is assigned from a company sequence only when the order is validated, and reads New before that.
- [N-U09-127] The source location defaults to the stock location of the first warehouse of the company. When the scrap starts from a transfer it defaults to the source location of that transfer, or its destination when the transfer is already done. The scrap location defaults as described for inventory-loss locations. Both can be changed when several locations are in use.
- [N-U09-128] Scrap orders accept goods-type (consumable) products, and only stockable ones are checked for availability and change on-hand quantities. The quantity must not be zero. For serial-numbered products the interface fixes the quantity at one.
- [N-U09-129] On validation, for stockable products the system compares on-hand stock at the exact location, lot, package and owner with the scrap quantity. If it is insufficient a warning asks the user to confirm anyway, which can drive stock negative, or to discard, which deletes the draft unless it was opened from the order form.
- [N-U09-130] Completing a scrap books one already-picked stock movement from the source to the scrap location, completed at once without backorder. The movement carries lot, package and owner. Its reference is the scrap reference and its origin is the source document, the transfer name or the scrap reference.
- [N-U09-131] If replenishment is ticked, a procurement for the scrapped quantity at the source location is requested after completion, with the scrap reference as origin and without carrying over the user context.
- [N-U09-132] Scrap reason tags are optional labels with unique names. They are visible on the order but do not alter stock or accounting.
- [N-U09-133] A scrap can be started from a transfer by an action, with products limited to those of the transfer. Moves of a transfer that ended in an inventory-loss location are skipped by the return flow, so scrapped lines cannot be returned. A transfer reached by scrap is shown with a scrap smart button.
- [N-U09-134] With the manufacturing extension a scrap can be started from a production order or work order, using the production locations, exploding kit products, resetting the picked flag of matching component lots, and grouping replenishment with the production group.

### STATE
- [N-U09-135] Draft to done when the order is validated and the movement is completed.

### OPTIONALITY
- [N-U09-136] Replenishment on scrap and reason tags are optional. The lot field is required in the form for tracked products only when the lots feature is enabled, but not by the model itself.

### DEPENDENCY
- [N-U09-137] Scrap relies on the transfer engine for the movement, on the procurement engine for replenishment, and on the valuation extension for accounting through the scrap location.

### CONSTRAINT
- [N-U09-138] Scrap orders belong to one company, are visible only to the allowed companies, and need a source location of internal type and a scrap location of inventory-loss type.

### RISK
- [N-U09-139] Because validation can be confirmed despite insufficient stock, scrap can create negative stock. There is no way to undo a scrap other than a new receipt or count.

### UNKNOWN
- [N-U09-140] The behaviour of scrap for kit products and under multi-step routes in transfers is not confirmed and needs a runtime test.

## CAP-U09-09 Stock quantity computations and history views

### WHAT
- [N-U09-141] Each stockable product shows on-hand, free, incoming, outgoing and forecast quantities, derived from on-hand records and open movements, for the group of selected companies, a chosen warehouse or location, and optionally a lot, package, owner or date. History views and reports list completed movements and forecast stock.

### WHY
- [N-U09-142] Planners and warehouse staff need consistent answers to how much is here, how much is free to promise, and how much will be here later.

### BUSINESS RULE
- [N-U09-143] On-hand quantity is the sum of on-hand records in the chosen scope including child locations, rounded to the product unit. Without a chosen location or warehouse the scope is every warehouse of the companies currently selected, so locations outside any warehouse are not counted unless chosen.
- [N-U09-144] Free quantity is on-hand minus reserved minus expired quantity. Incoming is the quantity of not-yet-done movements in waiting, confirmed, assigned or partially available states whose destination, or final destination for undone movements, lies inside the scope while their source lies outside. Outgoing is the opposite. Forecast is on-hand plus incoming minus outgoing minus expired.
- [N-U09-145] A strict option limits the scope to the exact locations without their children. A date in the past backs on-hand out by later completed movements, an ending date can be given to include planned movements, and a date typed without a time is read as the end of that day.
- [N-U09-146] Services always show zero. Quantities of a product with variants are the sum of its variants. Searching on on-hand quantity uses on-hand records only unless a date is given, in which case quantities are computed for every product.
- [N-U09-147] The company of a product cannot be changed while movements or non-zero quantities of it exist in another company. Making a product stockable books adjustments so that its quantities match its past completed movements, and cleans leftover reservations.
- [N-U09-148] The movement history lists completed movement lines by default, is read-only, can be filtered by status, direction, date range and inventory adjustments, grouped by product, status, date, transfer, location and category, and is reached from product buttons, on-hand lines and the reporting menu for administrators.
- [N-U09-149] A stock-at-date screen reopens the product list with a chosen date so that quantities are computed as of that date.
- [N-U09-150] The stock quantity report shows a daily forecast per warehouse for the past and future months of a configurable period, three by default, built from current on-hand records in internal warehouse or transit locations plus planned and recent movements, only for stockable products, with inter-warehouse transfers counted as outgoing for the source and incoming for the destination.
- [N-U09-151] The replenishment report for a product shows its quantities and draft transfers for the first active warehouse unless one is given.

### STATE
- [N-U09-152] Quantities are recomputed on demand and are not stored. The forecast report is rebuilt as a database view and reflects current data.

### OPTIONALITY
- [N-U09-153] The report period is a system parameter. Warehouse, location, lot, owner, package, date and strictness are chosen through context. Expiry handling is active only with the expiry extension.

### DEPENDENCY
- [N-U09-154] Quantities depend on on-hand records and on open movements maintained by the transfer engine, and on warehouse and location structure. Free quantity depends on the expiry extension for expired stock.

### CONSTRAINT
- [N-U09-155] Report records are visible only for the companies selected, and the stock quantity report is readable by all internal users.

### RISK
- [N-U09-156] Stock held in internal locations outside a warehouse tree is invisible to default quantities, and computing quantities for a date in the past needs scanning of later movements, which may be slow on large histories.

### UNKNOWN
- [N-U09-157] Performance and exact figures of the forecast views on large data and in multi-warehouse set-ups are not confirmed and need a runtime test.

## CAP-U09-10 Roles, record rules, scheduled behaviour and failure paths

### WHAT
- [N-U09-158] Access to on-hand records, counts, scrap, lots, packages and stock reports is governed by two inventory roles, by company scoping rules, and by a daily scheduler that also performs maintenance of on-hand records.

### WHY
- [N-U09-159] Counting and scrap change stock truth and accounting, so write access must be limited to trained roles while every internal user can still read availability.

### BUSINESS RULE
- [N-U09-160] There are two inventory roles: user and administrator. The administrator includes the user role and, in the restored configuration, is held by the two built-in system accounts.
- [N-U09-161] Every internal user can read on-hand records, packages and the stock quantity report. Only inventory users can change on-hand lines in counting mode, create scrap orders, lots and packages, and complete movements.
- [N-U09-162] At table level every internal user has full rights on movement lines, but creating movements needs the inventory user role. Lots, scrap orders, counting dialogs for reasons and packages are granted to inventory users and the more powerful dialogs for conflicts, warnings, count requests and relocation to administrators.
- [N-U09-163] Administrators alone can clear counts, set counts to zero, request counts, relocate on-hand lines, delete scrap orders and package types, change location master data and open the reporting menu.
- [N-U09-164] On-hand records, lots, packages, locations and movement lines are visible for the companies in scope plus records that belong to no company. Scrap orders, movements, transfers and the stock quantity report are visible only for the companies in scope. The company rules apply to all users with no role exceptions.
- [N-U09-165] A daily scheduler, run by the system account, handles reordering rules, assigns waiting movements, merges duplicate on-hand records, removes empty ones and, with the expiry extension, raises expiry alerts. Errors in the scheduler are logged and re-raised.
- [N-U09-166] Typical refusals include editing identity fields of an on-hand line, deleting on-hand records without the administrator role, copying on-hand records, scrapping zero, releasing more reserved stock than is reserved, quantities not respecting the unit rounding, negative done quantities, archiving or converting a location that still holds goods, and completing a transfer that splits a package between locations.

### STATE
- [N-U09-167] Not applicable to roles. Scheduler runs are recurring, not stateful.

### OPTIONALITY
- [N-U09-168] Features such as multiple locations, lots, packages and owners are switches implied for all internal users in the restored configuration. The scheduler frequency is configurable as a scheduled action.

### DEPENDENCY
- [N-U09-169] Manufacturing subcontracting adds portal access rules for lots and movement lines, and the accounting extension limits value fields to inventory administrators.

### CONSTRAINT
- [N-U09-170] Role grants are the declared access rows and record rules. Whether transient dialogs are checked against access rows for ordinary users is not shown by the source alone.

### RISK
- [N-U09-171] All internal users hold delete rights on movement lines at table level, relying on code guards to refuse deleting completed lines, and the administrator-only dialogs may block ordinary inventory users in the count workflow.

### UNKNOWN
- [N-U09-172] Effective permissions of ordinary inventory users on the administrator-only dialogs and the exact run frequency in production need runtime confirmation.

