# U106 — Neutral Knowledge Layer: Stock Replenishment

**ALL CONTENT: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION**

> This layer describes concepts in plain language. No technical identifiers, file references, code keywords, or dotted names appear below. Cross-references to restricted evidence use the N-U106-xxx keys.

---

## N-U106-001: The Minimum Inventory Rule Record Type
The system uses a dedicated record type to represent minimum stock rules. Each record of this type tracks a product at a specific storage location and defines the thresholds and settings that govern when and how that product is replenished.

## N-U106-002: Trigger Mode
Each minimum stock rule carries a mode selector with two options. In automatic mode the background scheduler processes the rule on its regular cycle. In manual mode the rule is only acted on when a user explicitly requests replenishment from the interface.

## N-U106-003: Minimum Stock Level
Each minimum stock rule stores a lower threshold quantity. When the forecasted stock level at the location falls below this value, a replenishment order becomes necessary.

## N-U106-004: Target Stock Level
Each minimum stock rule also stores a target quantity. After replenishment is executed, the order quantity is sized to bring the forecasted level up to this target.

## N-U106-005: Quantity to Order — Effective Field
The replenishment rule exposes a single effective order quantity field. This value is what drives the actual procurement. It may come from an automatic computation or be manually entered by a planner.

## N-U106-006: Quantity to Order — Computed Value
The system maintains a stored computed version of the order quantity. This version is recalculated whenever the forecasted level or the configured thresholds change.

## N-U106-007: Quantity to Order — Manual Override
A planner may enter an order quantity directly. When a manual value is present and non-zero, it takes priority over the computed value. Removing the manual entry reverts to the computed quantity.

## N-U106-008: Preferred Route
A minimum stock rule may nominate a specific replenishment route. When set, this route is used during rule selection instead of the default routes associated with the product or its category.

## N-U106-009: Applicable Rules
The minimum stock rule automatically resolves the set of logistics rules that apply, based on the storage location, any preferred route, and the product configuration. This computed set drives lead time calculation and procurement routing.

## N-U106-010: Deadline Date
The system computes the latest date by which an order must be placed to prevent a stockout, accounting for the expected lead time. This date is stored on the rule record and updated on each scheduler cycle.

## N-U106-011: Snooze Capability
A manually triggered replenishment rule may be snoozed until a chosen date, hiding it from the replenishment interface until then. This capability is restricted to manually triggered rules; automatically triggered rules may instead be archived.

## N-U106-012: Trigger Condition for Computed Quantity
The system only calculates a positive order quantity when the forecasted stock level is strictly below the minimum threshold. No order is generated when the forecast is at or above the minimum, even if it is below the target.

## N-U106-013: Order Quantity Formula
The quantity to order is calculated as the larger of the minimum and target levels minus the forecasted available quantity. The forecasted figure includes stock already on hand plus expected arrivals from open orders, adjusted for committed demand.

## N-U106-014: Manual-versus-Computed Resolution
The effective order quantity is the manually entered value when one exists, otherwise it is the computed value. This logic is evaluated on every read of the effective field.

## N-U106-015: User-Initiated Replenishment
A user may trigger immediate replenishment on one or more rules from the interface. This action creates procurement records and dispatches them for fulfilment using the same underlying mechanism as the scheduler.

## N-U106-016: Positive-Quantity Guard
Only rules with a positive order quantity at the time of processing result in a procurement being created. Rules with zero or negative quantities are silently skipped during both manual and scheduled runs.

## N-U106-017: Procurement Record Construction
For each qualifying rule a structured procurement record is assembled. It contains the product identity, the quantity and unit of measure, the destination location, an internal reference name, an external origin reference, the company, and a set of contextual values for routing and timing.

## N-U106-018: Procurement Dispatch
Assembled procurement records are passed to the logistics rule engine for fulfilment. The engine receives a flag indicating that the procurements originate from minimum stock rules, allowing extending modules to vary their behaviour accordingly.

## N-U106-019: Post-Processing Hook
After a batch of procurements is successfully processed a post-processing step is invoked on the batch. This step is intentionally designed as an extension point; the base system performs no action here.

## N-U106-020: Scheduler Task Sequence
The background scheduler executes a fixed sequence of tasks: it searches for qualifying rules, recomputes their order quantities and deadlines, triggers procurement creation, attempts to assign available stock to confirmed movements, and consolidates duplicate inventory records.

## N-U106-021: Orderpoint Domain Construction
The scheduler begins by constructing a filter that selects which replenishment rules to process. This filter is applied before any quantity calculations or procurement actions.

## N-U106-022: Batch Quantity Recomputation
The scheduler forces a fresh calculation of the stored order quantity for every qualifying rule before generating procurements. This ensures orders are based on the most current forecasted data.

## N-U106-023: Scheduler Procurement Trigger
After quantity recomputation the scheduler triggers procurement confirmation for all qualifying rules, forwarding information about database cursor strategy and company scope.

## N-U106-024: Public Scheduler Entry Point
The publicly accessible scheduler method wraps the task sequence in error handling and is designed to operate across all companies simultaneously using elevated system privileges.

## N-U106-025: Automatic-Trigger Filter
The scheduler domain restricts processing to rules in automatic mode. Manually triggered rules are excluded from the scheduled run entirely.

## N-U106-026: Active-Product Filter
The scheduler domain also excludes rules for archived products, ensuring that replenishments are not generated for products no longer in active use.

## N-U106-027: Pull-Push Action Resolution
When the logistics rule engine encounters a rule configured for both pull and push behaviour, it treats the rule as a pull action for the purposes of procurement dispatch. Push behaviour is handled separately through a different pathway.

## N-U106-028: Dynamic Handler Dispatch
The rule engine verifies that a handler method exists for the rule action before invoking it. This check enables extending modules to register support for additional custom action types.

## N-U106-029: Move Creation by Pull Rule
When a pull rule processes its procurements, it creates stock movement records for each procurement using elevated system privileges and scoped to the relevant company.

## N-U106-030: Immediate Move Confirmation
Newly created stock movement records are confirmed immediately after creation. Confirmation triggers evaluation of any chained downstream logistics rules, propagating demand through the supply chain.

## N-U106-031: Rule Action Types
A logistics rule carries an action selector. The three options are: move goods from a source to a destination on demand (pull), move goods from one location to another when they arrive (push), and a combination of both directions.

## N-U106-032: Supply Method on a Rule
A logistics rule carries a supply method selector with three options: take available goods from stock at the source location; always trigger another logistics rule to bring goods to the source first; or take from stock but trigger another rule if stock is insufficient.

## N-U106-033: Rule Lead Time
Each logistics rule stores a lead time expressed in whole days. This value is subtracted from the demand date to compute the planned date of the resulting movement.

## N-U106-034: Cumulative Lead Time Calculation
The total lead time for a replenishment chain is the sum of the individual lead times of all applicable pull-type rules in the chain.

## N-U106-035: Planning Horizon Addition
The company may configure a planning horizon period. When set, this horizon is added to the cumulative rule lead time, causing the system to look ahead and anticipate future demand when deciding whether to replenish.

## N-U106-036: Warehouse Make-to-Order Rule Reference
Each warehouse record holds a direct reference to its make-to-order pull rule. This link is used to update the rule when the warehouse delivery configuration changes.

## N-U106-037: Make-to-Order Supply Method Setting
The make-to-order pull rule is always created with the supply method set to demand-trigger mode, meaning it never takes from stock and always requires an upstream rule to supply the source location.

## N-U106-038: Global MTO Route Assignment
The make-to-order pull rule is assigned to a route shared across the entire system rather than a warehouse-specific route. If this global route does not yet exist for the company it is created at the time the warehouse is configured.

## N-U106-039: MTO Rule Action Type
The make-to-order pull rule is created as a pull-type rule, meaning it responds to downstream procurement demand rather than pushing goods proactively on arrival.

## N-U106-040: Hierarchical Rule Lookup
When a procurement needs a logistics rule, the system starts at the demand location and walks up through parent locations until it finds a matching rule or exhausts the hierarchy.

## N-U106-041: Batched Rule Pre-fetch
Rule candidates are pre-fetched in a single database query grouped by destination location, warehouse, and route. This avoids repeated individual lookups during bulk procurement processing.

## N-U106-042: In-Progress Quantity Extension Point
The base minimum stock rule system reports zero for quantities already in progress. Extending modules such as purchase management override this to report quantities on open purchase requisitions, ensuring they are deducted from the order quantity to avoid duplication.

## N-U106-043: Minimum-Maximum Consistency Constraint
The system enforces that the minimum quantity cannot exceed the maximum quantity on any replenishment rule. Attempting to save a rule that violates this raises a validation error.

## N-U106-044: Stale Auto-Created Rule Cleanup
Temporary replenishment rules created automatically during the replenishment report view are removed when their order quantity reaches zero or below. This prevents accumulation of spent placeholder records.

## N-U106-045: Availability-First Move Preparation
When a rule uses the stock-with-demand-fallback supply method, the initial movement record is created as if stock is available. Availability is evaluated at a later stage; if stock is insufficient, the movement is converted to demand-trigger mode automatically.

---

*Neutral-ref count: 45 entries (N-U106-001 through N-U106-045)*
