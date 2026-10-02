# U110 — Neutral Knowledge Layer: Lot and Serial Traceability with Accounting Impact
## DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

---

### N-U110-01 — Lot and Serial Record as First-Class Object

The inventory system maintains lot and serial records as independent entities, not mere labels on transactions. Each record participates in the messaging and activity framework, allowing notes, followers, and scheduled reminders to be attached directly to a lot or serial unit. This design supports traceability workflows where a lot must carry a history independent of any single transfer.

---

### N-U110-02 — Three-Way Tracking Mode on the Product

Every storable product declares one of three traceability modes. In the first mode the product is tracked by batch lot, meaning a named group of units share an identity. In the second mode each individual unit receives its own unique serial number. In the third mode no identity is assigned and stock is managed purely by counted quantity. The mode is set once per product template and inherited by all its variants.

---

### N-U110-03 — One-Unit Rule for Serial Numbers

When a product is placed in serial-number mode, the system enforces a hard limit of exactly one physical unit per serial record at all times. This constraint is checked when quantities are moved and when inventory is adjusted. Exceeding one unit for a serial raises a blocking error before any database record is committed.

---

### N-U110-04 — Lot Creation Restricted to Tracked Storable Products

A lot or serial record may only be created for a product that is both storable and already configured for lot or serial tracking. Attempting to create a lot for a product in quantity-only mode or for a consumable service is rejected at the selection-field domain level before the form is even submitted.

---

### N-U110-05 — Company-Scoped Uniqueness of Lot Names

Within a single company, the combination of product and lot name must be unique. A cross-company check additionally prevents a company-agnostic lot from duplicating a name already used by any company-specific lot for the same product. This uniqueness rule is enforced by a Python method that runs on every creation or modification of a lot record.

---

### N-U110-06 — Stock Position Tracked Per Lot in the Quant Layer

The inventory system records on-hand quantities at the granularity of a five-way key: product, location, lot, package, and owner. The lot slot in this key is an indexed foreign reference with a deletion-protection policy, meaning a lot record cannot be removed from the system while any physical quantity is recorded against it anywhere in the warehouse.

---

### N-U110-07 — Custom Properties on Lots Visible Through the Quant

A product's lot property definitions can extend the lot record with additional fields. Those custom properties are exposed on the quant record as a read-only related attribute, making them accessible in quant-level views and searches without requiring a separate join to the lot record at the application layer.

---

### N-U110-08 — Duplicate Serial Detection on the Quant

Each quant that belongs to a serial-tracked product carries a computed indicator that becomes true when more than one quant for the same serial number holds positive physical quantity across internal and transit locations. This flag does not block the record but surfaces a data quality warning in the inventory interface.

---

### N-U110-09 — Lot Must Match Product at the Quant Level

The quant layer enforces a consistency rule at the database constraint level: the product referenced by the lot record must match the product referenced by the quant. This prevents a lot created for one product from being accidentally applied to a different product's quant, which would corrupt traceability.

---

### N-U110-10 — Removal Strategy Resolution Order

When the system needs to choose which physical units to consume for a demand, it resolves the removal strategy by first inspecting the product's category, then walking up the location tree from the source location. If no strategy is found anywhere in that chain, first-in-first-out is applied by default. The strategy is resolved fresh for each gather operation, so different locations or categories can have different strategies for the same product.

---

### N-U110-11 — First-In-First-Out Consumes Oldest Stock

Under the first-in-first-out strategy, quants are presented to the reservation engine in ascending order of their incoming date. The unit that arrived earliest is reserved first. When two quants share the same incoming date, internal record order serves as the tiebreaker.

---

### N-U110-12 — Last-In-First-Out Consumes Newest Stock

Under the last-in-first-out strategy, quants are presented in descending order of incoming date, causing the most recently received units to be reserved before older ones.

---

### N-U110-13 — First-Expired-First-Out Consumes Soonest-Expiring Stock

The expiry module introduces a fourth strategy that orders quants by the date on which each lot is scheduled for removal, consuming the lot with the nearest removal deadline before those expiring later. When two lots share the same removal date, incoming date is used as the secondary sort criterion. This strategy is available only when the product-expiry capability is installed.

---

### N-U110-14 — Four Expiry Dates on Each Lot Record

When the product-expiry capability is active, each lot or serial record gains four date fields: the expiration date marking when the goods become unsafe, the best-before date indicating when quality begins to deteriorate, the removal date determining when stock should be withdrawn from saleable inventory, and an alert date that triggers a notification in advance of expiry.

---

### N-U110-15 — Removal Date Stored Directly on the Quant for Performance

To allow the database to efficiently sort quants for the first-expired-first-out strategy without a join, the removal date is copied from the lot record onto the quant record and stored physically in the quant table. This is a denormalisation that must stay synchronised with the lot's removal date.

---

### N-U110-16 — Expired Stock Reported as Unavailable

When a quant's removal date has passed, the system overrides its available quantity to zero. Physical quantity is unchanged, but the reservation logic treats the quant as if it held nothing, preventing expired goods from being automatically included in new outgoing transfers.

---

### N-U110-17 — Non-Strict Gather Accepts Untracked Quants as Fallback

When reserving against a demand that specifies a lot, the non-strict gather mode builds a domain that accepts both quants with the specified lot and quants with no lot at all. This allows the reservation engine to draw from untracked stock when the specifically requested lot's stock is insufficient.

---

### N-U110-18 — Strict Gather Enforces Exact Lot Match

When a strict gather is requested, only quants that exactly match the specified lot or explicitly carry no lot are included. This is used in scenarios such as move-line confirmation where the exact source quant identity must be preserved.

---

### N-U110-19 — Lot-Tagged Quants Prioritised Over Untracked Quants

After the removal-strategy ordering is applied, the gathered result is sorted a second time to ensure that quants with a lot reference appear before untracked quants. This means the lot-specific stock is consumed before any residual untracked stock, even within the same removal-strategy ordering.

---

### N-U110-20 — Lot Reference on Each Move Line

Every detailed operation line in a transfer carries a direct reference to a lot or serial record, constrained by domain to only those lots belonging to the same product as the line. The field is indexed at the database level to support fast lot-based queries across large volumes of historical lines.

---

### N-U110-21 — Serial-Number Lines Reject Non-Unit Quantities

When an operator changes the done quantity on a move line for a serial-tracked product to anything other than exactly one unit of the product's base measure, the system raises a blocking user error before the line can be saved. This enforces the invariant that one serial number corresponds to exactly one physical unit per line.

---

### N-U110-22 — Move Line Lot Must Reference Same Product

A constraint on the move line mirrors the quant-level constraint: if the lot referenced on a line belongs to a product other than the line's own product, a validation error is raised. This fires at the Python constraint layer when the record is written.

---

### N-U110-23 — Lot Mandatory at Validation for Tracked Products

When a transfer is validated, each move line with a positive done quantity is inspected. Lines for products in lot or serial tracking mode must carry a lot reference. If any such line is missing its lot reference and the operation type settings do not explicitly disable lot requirements, validation is blocked with a message listing the affected products.

---

### N-U110-24 — Move Validation Updates Lot-Specific Quant Positions

At the moment a move line is set to done, the quant update calls receive the lot reference from the move line, creating or incrementing a lot-specific quant at the destination and decrementing the lot-specific quant at the source. The lot identity is carried through the entire quant update chain so physical position is tracked per lot.

---

### N-U110-25 — Per-Lot Valuation Mode Controlled by a Product Flag

The accounting valuation module introduces an optional per-lot valuation mode for each product template. When this mode is active, cost calculations, standard-price storage, and average-cost or first-in-first-out computations are performed independently for each lot rather than aggregated across all lots of the product.

---

### N-U110-26 — Per-Lot Valuation Automatically Disabled for Non-Tracked Products

The per-lot valuation flag is forced to false whenever the product's tracking mode is set to none. This dependency is computed automatically, preventing an inconsistent state where lot valuation is claimed to be active but no lots can exist.

---

### N-U110-27 — Average Cost Computed Per Lot When Lot Valuation Is On

For a product using average costing with per-lot valuation enabled, the average cost and total value shown on the lot record are calculated by running the average-cost algorithm with its move search restricted to moves that contain lines referencing that specific lot, isolating the lot's own cost stream from other lots of the same product.

---

### N-U110-28 — First-In-First-Out Stack Built Per Lot When Lot Valuation Is On

For a product using first-in-first-out costing with per-lot valuation enabled, the cost stack is assembled from incoming moves that have at least one move line referencing the requested lot. The valued quantity for each incoming move is taken only from the lines belonging to that lot, not from the full move quantity.

---

### N-U110-29 — Standard Price Stored Directly on Each Lot Record

The accounting module adds a company-dependent monetary field to each lot record. When per-lot valuation is active, this field holds the current cost of one unit for that specific lot. It is updated automatically after incoming moves are posted and can also be set manually to trigger a revaluation.

---

### N-U110-30 — Outgoing Move Value Computed from Per-Lot Standard Price

When a product with per-lot valuation is moved out of stock, the total monetary value of the move is calculated by iterating over each move line and multiplying that line's done quantity by the standard price stored on the lot referenced by that line. Lines without a lot reference fall back to the product-level standard price.

---

### N-U110-31 — Missing Lot on Incoming Line Blocks Valuation for Lot-Valuated Products

When posting the value of an incoming move for a product with per-lot valuation, if any move line carries no lot reference, the system raises a blocking error before the value is computed. This enforces that lot-valuated products can never enter stock without a lot identity, which would leave the cost layer ambiguous.

---

### N-U110-32 — Per-Lot Standard Prices Refreshed After Each Receipt

After incoming moves are valued for lot-valuated products, the per-lot standard price on each referenced lot is recalculated using the appropriate costing algorithm scoped to that lot's move history. This keeps the lot's stored cost current with each new receipt.

---

### N-U110-33 — FIFO Stack Filtered to Single Lot by Move-Line Reference

When building the first-in-first-out cost stack for a single lot, the domain searching for incoming moves is narrowed by requiring the move to have at least one move line whose lot reference matches the target lot. This means the stack contains only receipts that contributed physical stock to that lot.

---

### N-U110-34 — Average-Cost Run Filtered to Single Lot by Move-Line Reference

When running average-cost computation for a single lot, the move domain is filtered to include only moves containing lines that reference that lot. The valued quantity for each move in the computation is the sum of line quantities specifically belonging to that lot, not the full move quantity.

---

### N-U110-35 — Changing a Lot on a Move Line Triggers Revaluation

In the accounting override of the move-line write operation, the lot reference is included in the list of fields whose modification triggers a recomputation of the parent move's monetary value. This means correcting a lot assignment after initial creation will cause the system to recalculate costs.

---

### N-U110-36 — Per-Lot Average Cost Stored on the Lot Record

For average-cost products with per-lot valuation, the per-lot standard price field on the lot record is set by executing the average-cost algorithm restricted to that specific lot and assigning the first element of the returned result — the per-unit average cost — to the lot's standard-price field.

---

### N-U110-37 — Enabling Lot Valuation Blocked When Untracked Stock Exists

If a user tries to activate per-lot valuation on a product that already has positive on-hand quantities in valued internal locations recorded without a lot assignment, the activation is rejected with an error. This prevents a situation where existing unvalued stock would have no lot to assign a cost to after the flag is toggled.

---

### N-U110-38 — Expiry Dates Calculated from a Single Reference Date

All four expiry-related dates on a lot record are derived from the expiration date using fixed time offsets configured on the product template. When the expiration date is changed, the other three dates shift by the same delta, preserving the spacing between them.

---

### N-U110-39 — Expiration Date Initialised Automatically at Lot Creation

When a new lot is created for a product that is configured to track expiration dates, the expiration date is populated automatically using the current timestamp plus the product template's configured expiration duration. The operator may override this value before saving.

---

### N-U110-40 — Scheduled Activity Triggered When Alert Date Is Reached

A batch method intended to run as a scheduled task searches for lots whose alert date has passed and whose responsible product still has on-hand stock in internal locations. For each such lot, a to-do activity is scheduled for the product's responsible user. A flag on the lot prevents the same alert from being scheduled twice.

---

### N-U110-41 — GS1 Barcode Includes Expiration Date When Applicable

When a GS1-format barcode is generated for a quant record belonging to an expiry-tracked lot, the system prepends the application-identifier sequence for best-before date and the sequence for expiration date to the barcode string, enabling downstream barcode scanners to read shelf-life data from the printed label.

---

### N-U110-42 — Duplicate Serial Warning on Transfer Entry

When an operator types a serial number on a move line during transfer entry, the system checks all other lines in the same transfer for the same serial. If it appears more than once, a warning is shown. If the serial is known in the system and already has on-hand stock in a location, the system also warns that the serial is not free, helping operators avoid double-use.

---

### N-U110-43 — Lot Reference Absent from Accounting Journal Entry Line

Based on source inspection, the accounting journal entry line model as extended by the inventory accounting module does not carry a direct lot reference field. The monetary impact of a lot-tracked move is recorded through the move's aggregated value without propagating the lot identity into the journal entry. This behaviour is marked as requiring runtime observation to confirm definitively.

---
