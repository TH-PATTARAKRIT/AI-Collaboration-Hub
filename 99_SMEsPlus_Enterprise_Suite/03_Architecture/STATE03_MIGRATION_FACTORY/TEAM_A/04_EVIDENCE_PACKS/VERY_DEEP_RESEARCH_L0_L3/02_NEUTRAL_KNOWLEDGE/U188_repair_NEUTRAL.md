# U188 Neutral Knowledge — Repair Order Module
**Unit:** U188 | **Group:** G07 | **Level:** L3 — Neutral Reference
**Date:** 2026-10-02

This document presents business-level and conceptual knowledge about the Odoo 19 Community
repair module, expressed without code-level terminology.

---

## VDR Claims Table — 21 Claims

| # | Claim ID | Category | Claim (Plain Prose) | Confidence | Contradictions | SMEsPlus Impact | Source Ref |
|---|----------|----------|---------------------|-----------|----------------|-----------------|------------|
| 1 | U188-C01 | State Lifecycle | A repair order begins in a New state, moves to Confirmed, then to Under Repair, then to Repaired (Done), with a separate Cancelled state reachable from any non-Done state. | HIGH | None observed | Must map all 5 states when migrating RO records | repair.py:42–53 |
| 2 | U188-C02 | State Transition | Starting a repair automatically confirms it if it was still in New state, so callers do not need to separately confirm before starting. | HIGH | None | Workflow logic must not assume two-step confirmation | repair.py:560–565 |
| 3 | U188-C03 | State Transition | Completing a repair requires the order to be in Under Repair state; calling End Repair from any other state raises an error. | HIGH | None | Validation rules must enforce state guard at migration | repair.py:549–551 |
| 4 | U188-C04 | Parts Model | In Odoo 19 there is no separate repair line table. Each part or operation added to a repair is stored as an inventory movement record with a classification field indicating whether the part is being added to the repair, removed from the repaired product, or recycled. | HIGH — breaking change from v16/v17 | Prior version had repair.line model | Migration must re-map legacy repair.line data to stock.move rows | stock_move.py:13–21 |
| 5 | U188-C05 | Parts — Add Type | Parts that are consumed during a repair (new components installed) travel from the component warehouse storage location into a virtual production location when the repair is completed. | HIGH | None | Ensure production virtual location exists per company | stock_move.py:6–10; stock_warehouse.py:28–31 |
| 6 | U188-C06 | Parts — Remove Type | Parts physically removed from the repaired product (e.g. faulty components extracted) are sent to a scrap or inventory-loss location by default when the repair is completed. | HIGH | None | Default may be changed at operation-type level; check client configuration | stock_move.py:6–10; stock_warehouse.py:42–43 |
| 7 | U188-C07 | Parts — Recycle Type | Parts removed from the product that are deemed reusable are directed to a recycling destination location which defaults to the warehouse's own stock area, making them available for future use. | HIGH | None | Confirm recycle location with client; may need separate bin location | stock_move.py:6–10; stock_warehouse.py:44 |
| 8 | U188-C08 | Completion — Stock Moves | When a repair is finished, the system creates an inventory movement for the repaired product itself, moving it from its source storage to its destination storage. All part movements and this product movement are validated together in one operation. | HIGH | None | All moves finalised atomically — partial backorders are cancelled, not created | repair.py:533–542 |
| 9 | U188-C09 | Completion — Traceability | The inventory movement created for the repaired product at completion is linked to all the component movement lines, providing full lot/serial traceability of which parts were consumed in the repair. | HIGH | None | Traceability report must be configured to show repair chains | repair.py:526 |
| 10 | U188-C10 | Invoicing | Odoo 19 does not have a direct invoice-method setting on the repair order. Billing for repair work is managed through a linked Sale Order; an invoice is then generated from that sale order using standard sales invoicing. | HIGH — breaking change | Older versions had invoice_method on repair.order | Migration must create or link SO records for all billed repairs | repair.py:677–710; sale_order.py |
| 11 | U188-C11 | Warranty Flag | A warranty checkbox on the repair order forces the sales price of all added-part lines to zero when enabled, both at time of sale-order line creation and immediately when the flag is toggled on an existing order. | HIGH | None | Warranty repairs must be tested to confirm zero-price on invoice | repair.py:64–66, 669–675 |
| 12 | U188-C12 | Lot/Serial Requirement | If the product being repaired is tracked by lot or serial number, the repair order cannot be completed without specifying the lot or serial. The system raises an error if this information is missing at completion time. | HIGH | None | Data import must ensure lot_id populated for tracked products | repair.py:494–498 |
| 13 | U188-C13 | Lot Auto-Population | When a repair order is created from a customer return picking and that picking contains exactly one lot or serial number, the lot is automatically filled in on the repair order. | HIGH | None | Auto-fill logic reduces data entry errors on return-driven repairs | repair.py:249–255 |
| 14 | U188-C14 | Serial Generation | Users can generate a new serial number for the repaired product directly from the repair order interface using the product's configured serial sequence. | MEDIUM | Only works if product has a lot sequence configured | Document client configuration requirement | repair.py:429–441 |
| 15 | U188-C15 | Multi-Company | The repair order is scoped to one company from creation and that company cannot be changed. The operation type, locations, and responsible user are all filtered to the repair order's company. | HIGH | None | Multi-company migration must assign company_id at import | repair.py:26, 38–41, 103–108 |
| 16 | U188-C16 | Replenishment (MTO) | Each warehouse's repair operation type is wired into a Make-to-Order procurement rule so that when a part is added to a confirmed repair order, the system can automatically trigger stock replenishment if the part is not available. | MEDIUM | MTO route must be active on the part | Confirm MTO route configuration with client | stock_warehouse.py:78–100 |
| 17 | U188-C17 | Stock Valuation Guard | The accounting module prevents the same repair part consumption from being posted to inventory accounts twice — once through the sales invoice path and a second time through the automatic stock valuation — by checking whether an account entry already exists before allowing a follow-on entry. | HIGH | None | COGS posting must be validated in test environment | account_move_line.py:7–10 |
| 18 | U188-C18 | Parts Availability | The system continuously computes whether all parts for a confirmed or in-progress repair are available, showing status indicators for Available, Expected (with forecast date), or Late. Only Add-type parts affect availability; removed and recycled parts are always considered available. | HIGH | None | Availability dashboards rely on forecast fields | repair.py:284–324; stock_move.py:23–29 |
| 19 | U188-C19 | Sale Order Auto-Creation | When a service product with tracking type set to Repair is added to a confirmed sale order, a repair order in Confirmed state is automatically created and linked to that sale order line. Cancelling the sale order line cancels the linked repair order. | HIGH | Requires sale_project or sale module active | Important for order-to-repair automation workflows | sale_order.py:90–119 |
| 20 | U188-C20 | Delivered Quantity Sync | When a repair linked to a sale order is completed, the delivered quantity on the originating sale order line is updated to reflect the completed repair quantity, enabling accurate invoicing based on delivery. | HIGH | None | Must verify qty_delivered calculation in integration test | sale_order.py:53–64; repair.py:489–490 |
| 21 | U188-C21 | Lot Details on Invoice | Lot and serial number information from all repair component lines (add, remove, and recycle types) is included in invoice line details, providing traceability from the customer invoice back to individual part lots. | MEDIUM | Requires relevant accounting/stock modules active | Confirm with client whether lot detail on invoice is desired | stock_move_line.py:9–10 |

---

## Key Business Concepts Summary

### Repair Order as a Work Order
A repair order is a controlled work order with a defined lifecycle. It captures what product
is being repaired, which customer owns it, which components will be consumed, and what the
billing arrangement is. It does not directly produce an invoice; instead it either raises a
sale order (for customer-billed repairs) or simply moves stock (for internal repairs).

### Parts Management Without a Separate Table
The elimination of the separate parts-line table means all quantity and location logic for
repair components shares the same infrastructure as warehouse movements. This simplifies
valuation and traceability but requires anyone migrating data to understand that old
`repair.line` records must become `stock.move` rows.

### Warranty vs. Paid Repairs
The warranty flag is a simple boolean switch rather than a complex rule engine. Any repair
marked as under warranty will have all customer-facing prices zeroed out on the linked
sale order. This keeps the billing flow identical whether warranty or not — the difference
is only in price.

### Invoicing Gap vs. Prior Versions
The removal of the `invoice_method` field is a significant architectural change. Projects
migrating from Odoo 14 or 16 need to build or verify a sale-order-based invoicing workflow.
Repairs that were previously invoiced directly (before or after repair) must now go through
a sale order confirmed before or after the repair, depending on the client's process.
