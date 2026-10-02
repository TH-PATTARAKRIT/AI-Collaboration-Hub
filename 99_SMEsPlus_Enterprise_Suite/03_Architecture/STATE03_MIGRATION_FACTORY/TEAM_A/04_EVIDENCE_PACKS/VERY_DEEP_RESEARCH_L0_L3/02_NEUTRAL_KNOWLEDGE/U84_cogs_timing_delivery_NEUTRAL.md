# U84 Neutral Knowledge — COGS Timing at Delivery
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks, no CamelCase, no dotted names

| NR-ID | Statement |
|---|---|
| NR-U84-001 | The delivery validation action is a synchronous call; no background job queue is used |
| NR-U84-002 | Pre-validation checks may pause execution to present the user with a backorder or lot-confirmation dialog before inventory and accounting records are finalized |
| NR-U84-003 | Once pre-validation checks pass, delivery confirmation proceeds synchronously in a single database transaction |
| NR-U84-004 | Confirmation of a delivery transfer delegates the inventory state change to each associated movement record |
| NR-U84-005 | The cost value of outgoing movements is computed before the movement records are marked as completed |
| NR-U84-006 | The completed status is written to movement records before the accounting entry for cost of goods sold is created |
| NR-U84-007 | The cost of goods sold accounting entry is created after the movement records reach completed status, within the same transaction |
| NR-U84-008 | A single accounting document is created to cover all valued movements in a delivery batch |
| NR-U84-009 | The accounting date on the cost of goods sold entry is the current calendar date at the moment of validation, not the delivery scheduled or completion date; backdated deliveries still receive today as the accounting date unless an override is present |
| NR-U84-010 | The cost of goods sold accounting entry is posted immediately upon creation; it is never left in draft status |
| NR-U84-011 | An accounting entry for inventory movement is only created when the product is storable, the movement has a valued direction, at least one location involved carries a valuation account, the quantity is non-zero, and the product uses real-time automated costing |
| NR-U84-012 | For a standard outbound delivery, the cost of goods sold debit account is taken from the valuation account configured on the destination customer location |
| NR-U84-013 | For a standard outbound delivery, the inventory credit account is taken from the stock valuation account linked to the product category |
| NR-U84-014 | Under the average-cost method, the cost assigned to an outbound movement equals the product standard cost at the moment of validation multiplied by the quantity shipped |
| NR-U84-015 | Under the first-in first-out method, the cost assigned to an outbound movement is drawn from the oldest cost layers on the product; when multiple outbound movements are validated together, each layer draw accounts for quantities already consumed by earlier movements in the same batch |
| NR-U84-016 | If the accounting date for a cost of goods sold entry falls within a locked period, the system automatically advances the date to the next open day rather than raising an error |
| NR-U84-017 | Each delivery movement record carries a direct reference to the originating sales order line, establishing traceability from the physical movement back to the commercial document |
| NR-U84-018 | Each valued delivery movement is linked to its cost of goods sold accounting document; the accounting document itself does not carry a direct reference back to the sales order |
| NR-U84-019 | In the base inventory-accounting configuration, cost of goods sold accounting lines do not carry analytic distribution; analytic cost tracking uses a separate analytic cost record, not a field on the accounting line |
| NR-U84-020 | When sales order lines carry analytic distribution, that distribution is forwarded to replenishment movements created through procurement rules for make-to-order paths, but it does not automatically populate the analytic dimension on cost of goods sold accounting lines |
| NR-U84-021 | Analytic cost entries for delivery movements are created as standalone analytic records linked to the movement, not as analytic distribution attributes on the inventory accounting document lines |
