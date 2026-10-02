# U115 — WIP Account Entries from Manufacturing Close: Neutral Knowledge
## Date: 2026-10-02
## Modules: Manufacturing Accounting, Inventory Accounting, Manufacturing

---

## Overview

When a manufacturing order is closed, the system creates a series of journal entries that move costs from intermediate accounts into the finished goods inventory account. This document explains the accounting flow in plain business terms.

---

## WIP Accounting Flow

Work In Progress (WIP) accounting captures the value of partially completed manufacturing orders at a point in time. The system provides two distinct accounting flows: one for recording WIP at period end, and one for closing the manufacturing order and posting the final cost of production.

---

## Component Consumption Entries

When raw materials are consumed during production, they are moved from the warehouse stock location to the production virtual location. If the product uses perpetual inventory valuation, this movement generates a journal entry at the time it happens:

- Debit: Production virtual location account (an intermediate WIP-type account)
- Credit: Stock valuation account

This entry reduces the inventory balance and places the value in the production account, indicating that the material is in active production rather than available stock.

---

## Finished Goods Posting

When the manufacturing order is marked as done, the finished goods are received into inventory. This generates the reverse accounting movement:

- Debit: Stock valuation account (finished goods)
- Credit: Production virtual location account

The value posted to finished goods depends on the product cost method:

- **Standard cost**: Finished goods are posted at the current standard price, regardless of actual production costs.
- **Average cost (AVCO) or First In First Out (FIFO)**: Finished goods are posted at the actual cost of production, calculated as the total component value plus workcenter labour costs plus any extra unit cost, divided by the quantity produced. Byproduct cost shares reduce the finished goods cost proportionally.

---

## Labour Cost Entries

When the manufacturing order closes, if the finished product uses perpetual inventory valuation and the production virtual location has a valuation account configured, an additional journal entry is created for workcenter labour costs:

- Debit: Workcenter expense account (or product expense account if no workcenter account is set)
- Credit: Production virtual location account

This entry posts the labour cost of all workcenters that operated on the manufacturing order. The cost is computed from actual time records multiplied by the workcenter hourly rate. Each individual time record is linked to its journal line for full traceability.

---

## WIP Wizard Purpose and Auto-Reversal

The WIP accounting wizard is used at period end to capture a snapshot of costs in work in progress. It applies only to manufacturing orders that are confirmed, in progress, or ready to close — not to completed or draft orders.

The wizard calculates three amounts:
1. **Component value**: the standard price of all picked components, up to the selected WIP date.
2. **Overhead value**: the workcenter time costs recorded up to the selected WIP date.
3. **WIP debit**: the sum of component and overhead values posted to the WIP balance account.

The journal entry created by the wizard:
- Credits the stock valuation account for component value
- Credits the overhead account for workcenter costs
- Debits the WIP balance account for the total

Immediately upon posting, the system automatically creates and posts a reversal entry dated one day after the WIP date. This ensures the WIP snapshot is automatically unwound at the start of the next period, preventing double-counting when the manufacturing order eventually closes.

---

## Standard vs Weighted-Average Cost Path

The cost method has a direct effect on how the finished goods value is determined at manufacturing close:

| Scenario | Finished goods value |
|----------|---------------------|
| Standard price | Always uses the current standard price; actual production costs are absorbed by the production account |
| Average cost | Actual total production cost divided by quantity; production account balances to zero |
| FIFO | Actual total production cost divided by quantity; each batch carries its specific cost |

Under standard cost, any difference between actual production costs and the standard price remains in the production account as a variance. Under AVCO and FIFO, the production account is cleared by the finished goods entry because the actual cost is transferred to inventory.

---

## Account Configuration Requirements

For manufacturing accounting to function, the following accounts must be configured:

- **Stock valuation account**: set on the product category or at company level
- **Production cost account**: set on the product category; used as the counterpart for component consumption and finished goods entries
- **WIP balance account**: set at company level; used by the WIP wizard for the debit entry
- **WIP overhead account**: set at company level; used by the WIP wizard for overhead credits
- **Workcenter expense account**: optional per workcenter; overrides the product expense account for labour entries
- **Production virtual location valuation account**: must be set on the production location for labour entries to be created

All account fields are company-dependent, supporting multi-company configurations.
