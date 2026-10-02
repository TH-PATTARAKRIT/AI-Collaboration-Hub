# U164 — sale_purchase Neutral Knowledge
**Unit:** U164 | **Module:** sale_purchase | **G-Group:** G05/G08 | **Priority:** P1
**Date:** 2026-10-02 | **Researcher:** DeepSeek STATE03

---

## Module Overview

The sale_purchase module bridges the Sales and Purchase applications. It enables service outsourcing by automatically generating purchase orders (or requests for quotation) whenever certain service products are sold via a sales order. The module auto-installs whenever both the sales and purchase applications are active.

---

## Claims Table (18 claims, 9-column VDR format)

| # | Claim | Source File | Evidence Type | Confidence | Migration Risk | Odoo 17 Delta | Functional Area | Neutral Ref |
|---|-------|-------------|---------------|------------|----------------|---------------|-----------------|-------------|
| C1 | The module automatically installs when both the sale and purchase apps are present | `__manifest__.py` | Declarative | HIGH | LOW | None expected | Module lifecycle | Auto-install flag is set; no manual activation required |
| C2 | A boolean field on the product controls whether selling that service triggers an automatic purchase request | `product_template.py` | Field definition | HIGH | LOW | None expected | Product configuration | Products of service type can be flagged to auto-generate a supplier request when sold |
| C3 | The auto-generate flag is company-dependent, allowing different behaviour per company in a multi-company setup | `product_template.py` | Field attribute | HIGH | MEDIUM | None expected | Multi-company | Each company can independently enable or disable the auto-generation for the same product |
| C4 | When a sales order is confirmed, the system iterates all its lines and triggers purchase generation for qualifying service lines | `sale_order.py` | Method override | HIGH | LOW | None expected | Order confirmation flow | Confirmation of a sales order causes the system to inspect each line and create supplier requests where appropriate |
| C5 | A guard prevents duplicate purchase lines from being created if the sales line already generated one in a prior confirmation cycle | `sale_order_line.py` | Business logic guard | HIGH | LOW | None expected | Idempotency | The system checks whether a purchase line already exists before creating a new one, supporting cancel/reconfirm workflows |
| C6 | Each purchase order line carries a direct reference back to the originating sales order line | `purchase_order.py` | Field definition | HIGH | LOW | None expected | Traceability | A foreign key on the purchase line stores which sales line originated it; the field is database-indexed for performance |
| C7 | A computed relational field on the sales order line holds all purchase lines generated from it | `sale_order_line.py` | Field definition | HIGH | LOW | None expected | Traceability | The sales line exposes all its generated purchase lines as a one-to-many relationship |
| C8 | A count of generated purchase lines is maintained on the sales order line for use in business logic and display | `sale_order_line.py` | Computed field | HIGH | LOW | None expected | UI/logic | The count is computed via an efficient grouped database query rather than loading all records |
| C9 | The sales order header carries a count of distinct purchase orders generated from its lines, visible only to purchase users | `sale_order.py` | Computed field | HIGH | LOW | None expected | UI smart button | The sales order form shows a smart button leading to the generated purchase orders, restricted by access group |
| C10 | The purchase order header carries a count of originating sales orders and a boolean flag for whether any exist | `purchase_order.py` | Computed field | HIGH | LOW | None expected | UI smart button | A purchase order can navigate back to the sales orders that caused its creation |
| C11 | The system attempts to reuse an existing draft purchase order for the same supplier and sales order before creating a new one | `sale_order_line.py` | Business logic | HIGH | LOW | None expected | PO consolidation | Multiple lines for the same supplier on the same sales order are consolidated into one purchase order |
| C12 | If a confirmed sales line's ordered quantity is increased, the system updates the quantity on the existing draft purchase line or creates a new one for the difference if the purchase was already confirmed | `sale_order_line.py` | Write hook | HIGH | LOW | None expected | Quantity synchronisation | Quantity increases on a live sales line propagate to the corresponding purchase, either by updating or by creating a supplemental purchase line |
| C13 | If a confirmed sales line's ordered quantity is decreased, the system schedules an activity warning on the purchase order rather than automatically reducing the purchase quantity | `sale_order_line.py` | Write hook | HIGH | LOW | None expected | Quantity synchronisation | Decreases are not auto-applied to the purchase; a human is expected to review and act manually |
| C14 | When a sales order is cancelled, the system schedules a warning activity on any open purchase orders that were generated from it | `sale_order.py` | Cancellation hook | HIGH | LOW | None expected | Lifecycle coordination | Cancelling a sales order does not automatically cancel its generated purchase orders; instead it alerts the purchaser |
| C15 | When a purchase order is cancelled, the system schedules a warning activity on the originating sales orders | `purchase_order.py` | Cancellation hook | HIGH | LOW | None expected | Lifecycle coordination | Cancelling a purchase order alerts the sales person on the relevant sales orders; no automatic SO update occurs |
| C16 | When a new sales order line is added to an already-confirmed sales order, the purchase generation fires immediately at line creation time | `sale_order_line.py` | Create hook | HIGH | LOW | None expected | Post-confirmation additions | Adding a qualifying service line to a live sales order generates its purchase immediately without requiring a separate action |
| C17 | If all purchase orders linked to a sales order share the same shipping address from that sales order, the purchase order inherits that shipping address | `purchase_order.py` | Computed override | MEDIUM | LOW | None expected | Delivery address | Purchase orders generated from a single-destination sales order automatically reflect the sales delivery address |
| C18 | No wizard exists in this module for manually linking a sales order line to a purchase order line; all links are system-generated | Source tree inspection | Absence finding | HIGH | LOW | None expected | Manual override capability | The module provides no user-facing wizard for creating or overriding the SO→PO link; the association is always automated |

---

## Architecture Summary

### Data Model Relationships

```
sale.order (1)
    └── sale.order.line (N)  [purchase_line_ids One2many, purchase_line_count Integer]
            └── purchase.order.line (N)  [sale_line_id Many2one → sale.order.line]
                    └── purchase.order (1)  [sale_order_id related via line.sale_order_id]
```

The chain is: SO header → SO lines → PO lines → PO header. Navigation in both directions is provided.

### Trigger Conditions

A PO is auto-generated for an SO line when ALL of the following are true:
1. Product type is `service`
2. Product's `service_to_purchase` flag is True (for the ordering company)
3. Product has at least one vendor defined
4. SO line state is `sale` (confirmed)
5. SO line is not an expense line (`is_expense == False`)
6. SO line has not yet generated a PO line (`purchase_line_count == 0`)

### Scope Limitation

This module handles **service outsourcing only** (type = service). Physical product replenishment via make-to-order routes is handled by the `sale_stock` and `purchase_stock` modules through the procurement/route/orderpoint mechanism, which is outside this module's scope.

### No Wizard

There is no manual linking wizard. The SO→PO association is exclusively automated.
