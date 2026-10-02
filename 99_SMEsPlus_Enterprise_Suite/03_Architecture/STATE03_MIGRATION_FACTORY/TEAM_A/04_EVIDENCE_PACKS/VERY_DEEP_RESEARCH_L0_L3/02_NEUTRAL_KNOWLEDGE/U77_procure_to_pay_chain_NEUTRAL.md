# U77 Neutral Knowledge — Full Procure-to-Pay Chain

> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U77-001 | When a purchase order in draft or sent status is confirmed, it transitions to either an approved purchase state (direct approval) or a pending-approval state, depending on whether the company requires double validation. |
| NR-U77-002 | The approval step writes the confirmed state and records the date of approval on the purchase order; this state transition is what grants the order legal standing. |
| NR-U77-003 | The stock extension of the purchase module intercepts the approval action and immediately triggers creation of an incoming receipt operation. |
| NR-U77-004 | The receipt creation process builds a warehouse receipt document, attaches stock movement lines for each ordered product, confirms those movements, and reserves available stock. |
| NR-U77-005 | Each receipt document records the vendor's warehouse location as the source and the company's receiving location as the destination; these two locations determine whether accounting entries will be generated at validation time. |
| NR-U77-006 | Each stock movement on the incoming receipt carries a reference back to its originating purchase order line; this reference is the key that drives quantity-received calculation and vendor bill linkage. |
| NR-U77-007 | For products where receipt quantity drives billing, the system counts how many units were received from all completed movements linked to each purchase line; this count becomes the receivable quantity. |
| NR-U77-008 | When a receipt is validated, the system calculates a monetary value for each incoming movement; for products with a linked purchase order, the value is initially derived from the purchase price on the order line. |
| NR-U77-009 | A critical Odoo 19 design point: for standard supplier-to-stock receipts, no accounting journal entry is created at the time of receipt validation. The stock movement captures value in a valuation layer, but the actual bookkeeping entry is deferred to the vendor bill. |
| NR-U77-010 | The condition for creating an accounting entry at receipt is that either the source or the destination warehouse location has a dedicated valuation account configured. Standard supplier locations and internal storage locations do not have such accounts by default. |
| NR-U77-011 | Vendor bills are created from the purchase order using a dedicated action that reads the order lines, converts them into bill line items, and groups results by vendor, currency, and company before creating the bill document. |
| NR-U77-012 | The vendor bill is created with the type "incoming bill" (in contrast to a customer invoice which is outgoing); this type designation controls which accounting rules apply throughout the posting process. |
| NR-U77-013 | For storable products with perpetual (real-time) valuation, the bill line account is automatically set to the product's inventory valuation account at the time the bill line is created or product is changed. |
| NR-U77-014 | The link between the vendor bill and the purchase order is maintained through bill line items that each carry a reference to the specific purchase order line they originated from. |
| NR-U77-015 | The billing status on a purchase order ("To Invoice", "Fully Billed") is calculated by comparing quantity invoiced against quantity receivable (for receive-based billing policy) or quantity ordered (for order-based billing policy). |
| NR-U77-016 | When the vendor bill is posted (confirmed), the system creates the primary accounting journal entry: debit the inventory valuation account and credit the accounts payable account. |
| NR-U77-017 | Posting the vendor bill also triggers an update to the monetary value on the receipt stock movement, so the receipt's recorded value shifts from the purchase price estimate to the actual billed amount. |
| NR-U77-018 | When Anglo-Saxon accounting is enabled and the product uses standard costing, posting a vendor bill creates additional adjustment lines: a debit to a price difference (variance) account and a credit back to the valuation account, to the extent the billed price differs from the standard cost. |
| NR-U77-019 | The price difference adjustment ensures the inventory valuation account reflects only the standard cost value, while the variance account absorbs the difference between the standard cost and the actual invoice price. |
| NR-U77-020 | An outbound vendor payment records a debit to the accounts payable account and a credit to the bank or outstanding payments account; the payment type "outbound" controls the sign of the liquidity line. |
| NR-U77-021 | The destination account on a vendor payment defaults to the vendor partner's payable account (from the partner master record), which must match the payable account used on the vendor bill. |
| NR-U77-022 | Payment registration performs two actions in sequence: first it posts the payment journal entry, then it reconciles the payment's payable line against the bill's payable line. |
| NR-U77-023 | Reconciliation is performed by matching the posted payable journal entries from the payment and the vendor bill; both must share the same account and be in posted state. |
| NR-U77-024 | Full reconciliation eliminates the outstanding payable balance: the residual amount on both the bill and the payment becomes zero, the bill's payment status becomes "Paid", and the purchase order's billing status becomes "Fully Billed". |
| NR-U77-025 | The purchase order's billing status transitions from "To Invoice" to "Fully Billed" when all order lines show zero quantity-to-invoice AND at least one vendor bill exists in a non-cancelled state. |
| NR-U77-026 | Compared to the order-to-cash chain, the procure-to-pay chain is structurally symmetric but reversed in polarity: where O2C uses receivables, P2P uses payables; where O2C credits inventory at delivery, P2P debits inventory at billing; where O2C receives inbound payment, P2P sends outbound payment. |
| NR-U77-027 | A key architectural difference from classic Odoo accounting: in Odoo 19, receipt validation does NOT generate an accounting entry for standard configurations. The bill posting is the singular accounting event for the procure-to-pay chain on the inventory side. |
| NR-U77-028 | The quantity used on the vendor bill line for "receive" billing policy equals the quantity received on the picking (the received quantity field on the purchase order line), not the quantity ordered. |
