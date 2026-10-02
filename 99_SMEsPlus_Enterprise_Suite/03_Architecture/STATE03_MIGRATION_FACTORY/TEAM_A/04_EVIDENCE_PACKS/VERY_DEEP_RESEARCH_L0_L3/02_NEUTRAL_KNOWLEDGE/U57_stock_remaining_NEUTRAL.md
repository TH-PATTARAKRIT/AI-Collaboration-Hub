# U57 — Inventory Management: Lot Tracking, Reorder Rules, Procurement Routing, Batch Picking, and Supporting Features (neutral knowledge layer)

> NEUTRAL KNOWLEDGE — Plain English. No file paths, no dotted model names, no code keywords, no backticks, no snake_case identifiers.
> Unit: U57 | Module scope: inventory management remaining areas (delta from units U08/U09)
> Date: 2026-10-02

---

## [N-U57-001] Lot and Serial Number Tracking

Every physical batch of goods that needs traceability carries a lot or serial number. These identifiers are created, stored, and tracked throughout the system. When a product is configured with a sequence template, the system can generate the next number automatically: it reads the last-used number, extracts the numeric part at the end, adds one, and pads it back to the same width. This means warehouse staff do not need to type lot numbers manually — they appear automatically when items are received. For serial numbers the system goes further and searches the most recently created serial to determine what the next one should be.

Uniqueness is enforced across the organisation. Two records cannot share the same lot name for the same product within the same legal entity. The system also checks across entities when some lots have no company assignment, upgrading its own permissions to look across all companies for potential conflicts.

Products with lot tracking can also carry custom property fields defined per product family, enabling structured recording of quality, batch, or origin data beyond the standard fields.

---

## [N-U57-002] Lot Traceability — Delivery Lookup

The system can answer the question "which deliveries used this lot?" even when the lot was consumed in manufacturing and the resulting output lot was then sold. The traceability algorithm works as a breadth-first search: it starts with the original lot, finds all outgoing movements that used it, and checks whether any of those movements were production consume lines. If they were, the output lots produced by those manufacturing runs are queued for the same search. The algorithm accumulates delivery identifiers at every level and maps child lots back to their originating parent lots so the full chain is reported. This means a lot that passed through multiple manufacturing steps is fully traceable to its ultimate destination.

---

## [N-U57-003] Minimum Stock Rules (Reorder Points)

A minimum stock rule pairs a product with a storage location and defines a lower threshold (the minimum) and an upper threshold (the maximum). When the system detects that the projected stock will fall below the minimum, it calculates how much to order: it takes the maximum quantity and subtracts the projected stock at the end of the planning horizon. The resulting quantity is rounded up to the nearest approved replenishment multiple, which may be a supplier packaging unit. The rounded-up order quantity is then placed.

Two trigger modes exist. Automatic mode means the scheduler runs without user intervention: it evaluates all products for which an automatic rule is active and raises purchase or manufacturing orders as needed. Manual mode creates a rule record that a planner must review and confirm. After the order is placed, manual rules created automatically by the system (rather than by a user) are cleaned up.

The system also warns planners when an order would push the stock above the maximum. This "unwanted replenishment" flag appears when the projected stock after ordering exceeds the ceiling, giving the planner a chance to adjust the quantity.

Rules can be snoozed. A planner can defer action for one day, one week, one month, or a custom date. Only manually triggered rules can be snoozed; automatically triggered rules cannot.

Replenishment UoM multiples allow the system to round an order up to the nearest whole package or pallet. The allowed rounding units can include supplier packaging units from active purchase agreements, so the system aligns with supplier constraints automatically.

---

## [N-U57-004] Orderpoint Procurement Execution

When the scheduler runs, it batches qualifying reorder rules into groups of one thousand. For each group it builds procurement requests and submits them together. A database savepoint wraps each group so that if one product's procurement fails, the rest of the group are unaffected. Failures are recorded as activity warnings on the product record for the planner to investigate.

The procurement date calculation takes into account the total lead time of the sourcing chain (the sum of all rule delays) plus a company-defined planning horizon. The result is the date by which the goods must be ordered to arrive before the minimum is breached. This date is localised to the company's timezone and converted to UTC for internal storage.

Auto-generated manual orderpoints that have had their order fulfilled (quantity to order has dropped to zero) are removed automatically by a background vacuum process.

---

## [N-U57-005] Procurement Rules and Routing

Every procurement request passes through a routing engine that decides how and from where the goods should be sourced. The engine searches for a matching rule by walking up the location hierarchy: it tries the requested destination first, then the parent location, then grandparent, and so on. At each level it checks whether any route assigned to the product, its category, or the warehouse produces a match.

Rules come in three action types. A pull rule creates a movement from a source location to a destination — for example, moving from a warehouse to a delivery area. A push rule creates a chained movement triggered when goods arrive at a given location — for example, automatically moving from a receiving dock to a storage zone. The combined pull-and-push type does both.

The sourcing method on a pull rule controls where the goods come from: take from existing stock, trigger another rule (make to order), or try stock first and fall back to triggering another rule only if stock is insufficient.

Push rules operate in two modes. Transparent mode modifies the in-flight movement's destination invisibly, adding no visible transfer step. Manual mode creates a new, separate transfer chained to the original, which the warehouse team must explicitly process.

When a rule has a configured lead time (in days), the system subtracts that delay from the planned date when creating the movement, so upstream operations are scheduled early enough to meet the downstream delivery date.

The scheduler processes all auto-triggered reorder rules, then assigns stock to confirmed movements in batches of one thousand, ordered by reservation date, priority, and planned date. Finally it merges duplicate inventory records.

---

## [N-U57-006] Procurement Failures

When a procurement cannot be fulfilled (for example, no matching rule is found), the system raises a structured exception that carries a list of failed procurement requests along with their error messages. The calling code can choose to surface this as a user-readable error or to collect and handle the failures programmatically. This means batch processing can tolerate partial failures: failed items are logged while successful ones proceed.

---

## [N-U57-007] Detailed Operations — Move Lines

Each stock transfer line records the actual quantity moved, the lot or serial number, the source location, the destination location, the package, and the owner. These detailed lines are the ground truth for inventory: changes to them directly drive inventory balance updates.

When a product is serial-tracked (one unit per serial number), selecting a serial auto-sets the line quantity to one and warns if the same serial appears more than once in the same picking. The system also checks whether the serial is already in stock somewhere and can suggest the correct source location automatically.

Putaway strategies determine where goods are stored when they arrive. The engine groups move lines by package. For packages with a defined type, a single best storage location is computed for the whole package. For unlabelled packages or loose items, each line gets its own putaway location. If a package's contents would be split across more than one location, the system falls back to the default destination.

When a transfer is validated, the system first confirms that all tracked products have lot or serial assignments. New lot names typed during validation are matched against existing lots in the system; only genuinely new names result in new lot records, preventing accidental duplicates. Line quantities are then checked against UoM rounding precision. After these checks, the inventory balances are updated: the source location loses the reserved quantity, then the available quantity, and the destination gains the available quantity. If at any point the available balance would go negative, the system searches for other reservations of the same goods and releases them so the current transfer can proceed.

A partial DB index is maintained to make these free-reservation searches fast. It covers all non-cancelled, non-done lines that have reserved stock and have not yet been picked.

When goods cannot be validated because available quantity is insufficient, the system opens a warning dialog rather than silently accepting an invalid transaction.

Package consolidation ("put in pack") groups one or more move lines into a labelled package. When only one line is packed, putaway is applied to find the best destination location. After packing, labels can be printed automatically if the operation type is configured for it. The put-in-pack action first processes unpacked lines, then wraps existing loose packages, chaining the operations as needed.

For reporting, move lines are aggregated by product, display name, description, and unit of measure. Backorder lines are included. Lines on confirmed transfers that have no associated detail lines (demand-only records) contribute to the ordered quantity but show no fulfilled quantity.

---

## [N-U57-008] Replenishment Wizards

Two replenishment workflows exist for initiating orders interactively:

The manual replenishment wizard allows a user to select a product, quantity, route, and warehouse, then trigger a procurement immediately. The planned date is calculated by summing the lead times across all rules in the selected route. After the order is created, a notification with a link to the resulting transfer appears.

The replenishment information wizard is attached to a reorder rule and shows the planner a supply-demand graph. The graph models a sawtooth pattern: stock rises when an order arrives (up to the maximum) and falls as demand consumes it (down to the minimum). Daily demand is calculated from actual outgoing movements in a selected historical period (options range from seven days to the same quarter of the prior year), adjusted by a percentage factor the planner can tune. The graph shows how many days between orders based on this demand rate, and also shows the lead time.

Multi-warehouse replenishment options are shown when a warehouse has configured resupply routes from other warehouses. For each supplying warehouse, the system shows how much of the product is freely available there and what the expected lead time is. A warning appears when the supplying warehouse cannot fulfil the full quantity. The planner can either order everything (accepting the potential shortfall) or cap the order to the available quantity.

Routes allowed for replenishment exclude inter-company internal routes and require that the destination has an associated warehouse.

---

## [N-U57-009] Batch and Wave Transfers

The batch transfer feature (installed as a separate optional module) groups multiple transfers into one task list so a warehouse worker can process them in a single trip. A wave transfer is a variant of a batch transfer: the same underlying record type carries a flag that marks it as a wave rather than a standard batch. Waves and batches receive names from different number sequences.

States follow a straightforward lifecycle: a batch is drafted, confirmed (making it active), completed (when all included transfers are done), or cancelled. State transitions are computed automatically: when every non-cancelled transfer in a batch is done, the batch is marked done; when all transfers are cancelled, the batch is cancelled.

Only transfers in the awaiting-stock, confirmed, or ready-to-process state can be added to a batch. Transfers already completed or cancelled are excluded.

Validating a batch removes transfers with no quantities and performs a combined sanity check across the remaining transfers, treating them as a single unit rather than checking each separately. After validation, each included transfer receives a note in its activity log referencing the batch it was processed in.

Operation types can define maximum line counts and maximum transfer counts for batches. When auto-merging is in effect, a new transfer is only added to an existing batch if neither limit would be exceeded.

Merging two or more batches into one requires that they share the same operation type, the same wave-or-batch designation, and that none of them is completed or cancelled. The earliest scheduled batch absorbs the others' transfers; the others are deleted.

Batch records support custom property fields, defined per operation type, so warehouses can track additional information beyond the standard fields.

---

## [N-U57-010] Scrap Management

Scrapping is the process of removing damaged, expired, or otherwise unusable goods from inventory and recording the loss. A scrap record specifies the product, quantity, lot, package, and source location. The destination must be a virtual inventory-adjustment location, not a regular internal location.

Executing a scrap creates an internal movement, marks it as completed, and updates the inventory balances accordingly. If the planner marked the scrap as requiring replenishment, the system immediately raises a procurement request to replace the scrapped quantity at the same source location.

Before completing a scrap, the system checks whether the requested quantity is actually available in the specified context (location, lot, package, and owner). If it is not, a warning dialog appears showing the actual available quantity, allowing the planner to decide whether to continue.

Scrap reason tags can be attached to scrap records to categorise the cause of loss (for example, damaged, expired, or returned defective). Tag names must be unique. These tags are available for analysis and reporting.

---

## [N-U57-011] Configuration Toggles for Inventory Features

Several inventory features are independently switchable:

Lot and serial number tracking is disabled by default and must be activated for the organisation. Once activated, products can be set to tracking by lot (multiple units per identifier) or by serial number (one unit per identifier). Disabling this feature after activation is blocked if any product still has tracking enabled — the system prevents accidental data loss.

Expiration date tracking is a further optional feature that adds dates for best-before, removal, end-of-life, and alert thresholds to lot records. This is installed as a separate module.

Batch, wave, and cluster transfers are also a separate installable module. The configuration toggle installs or uninstalls the module rather than toggling a permission group.

Multi-step routes (such as a two-step receipt: receive then put away, rather than receiving directly to storage) require multi-location tracking to be active. Enabling multi-step routes automatically enables multi-location tracking. Disabling multi-location tracking automatically disables multi-step routes. When multi-location tracking is enabled, internal operation types for all warehouses are activated.

The "replenish on order" route (make-to-order) is toggled by activating or deactivating the make-to-order route for the first warehouse. This is a computed toggle rather than a standalone flag.

The planning horizon is a company-level number of days that controls how far ahead the scheduler looks when evaluating whether stock will dip below minimums.

---

## [N-U57-012] Forecasted Stock Report

A reporting layer aggregates projected stock figures per product: current on-hand quantity, forecasted (virtual) quantity including all confirmed movements, freely available quantity, incoming quantity from pending receipts, and outgoing quantity from confirmed deliveries. The forecast report also estimates lead times by querying the routing rules for each product and location, summing the delays across the chain. This information feeds the replenishment report to show planners both the current situation and the expected future state.
