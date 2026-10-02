# U76 Neutral Knowledge — Full Order-to-Cash Chain
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U76-001 | There is a dedicated public action to confirm a sales order; it validates the current state is either draft or sent before proceeding. |
| NR-U76-002 | When a sales order is confirmed, its internal status transitions from draft (or sent) to an active sale state, and the confirmation timestamp is recorded. |
| NR-U76-003 | After writing the confirmed state, the confirmation action delegates to an internal implementation hook that extensions can override to trigger downstream document creation. |
| NR-U76-004 | The stock extension of the sales module overrides that implementation hook to launch procurement rules on all order lines before calling the base behavior. |
| NR-U76-005 | For each order line with a storable product, a procurement request object is created and submitted to the routing rule engine, which determines whether to pull from stock or buy or manufacture. |
| NR-U76-006 | A procurement request object contains the product, quantity, unit of measure, destination location, order reference, company, and scheduling values but does not itself create any stock transfer. |
| NR-U76-007 | When the routing rule engine processes a pull route, it creates an outgoing stock transfer (delivery order) against the warehouse output location destined for the customer location. |
| NR-U76-008 | Immediately after the routing rules run, any newly created transfers that are not yet confirmed are confirmed automatically so they are available for scheduling and reservation. |
| NR-U76-009 | Confirming a sales order creates no accounting entry; the general ledger is untouched at the confirmation step. |
| NR-U76-010 | The user-facing validate action on a delivery transfer runs sanity checks, pre-validation hooks, and then calls the internal completion action, with or without backorder creation depending on configuration. |
| NR-U76-011 | The completion action can be called with or without a backorder flag; in either case it reaches the same stock-move-level completion logic. |
| NR-U76-012 | The transfer-level completion delegates to move-level completion for all moves in a waiting, partially available, assigned, or confirmed state, and records the completion timestamp. |
| NR-U76-013 | The stock-accounting extension overrides move-level completion to insert inventory valuation and journal-entry creation steps. |
| NR-U76-014 | The accounting override computes the value of outgoing moves before the state change (to capture the current cost stack), then calls the base logic, then computes incoming move values, then creates journal entries. |
| NR-U76-015 | Outgoing moves (leaving company-owned locations toward customer locations) are identified and valued before the move reaches the done state, ensuring the cost is frozen at the moment of dispatch. |
| NR-U76-016 | After base move completion, one inventory valuation journal entry is created for all moves processed in the batch. |
| NR-U76-017 | The inventory valuation entry creation collects accounting line values from each eligible move, builds a single journal entry using the company-level inventory journal, and immediately posts it. |
| NR-U76-018 | The journal used for inventory valuation entries is the company-level inventory valuation journal, which is separate from the sales or purchase journal. |
| NR-U76-019 | The inventory valuation entry is posted in the same database transaction as the transfer validation; it is never left in draft state. |
| NR-U76-020 | The debit and credit accounts for an inventory valuation entry are selected based on whether the source or destination location has an associated expense account configured. |
| NR-U76-021 | For a standard outgoing delivery from warehouse to customer, the debit is posted to the expense account configured on the customer location (the cost-of-goods-sold account), and the credit is posted to the product-category stock valuation account. |
| NR-U76-022 | The reference field of the inventory valuation journal entry is taken from the stock transfer reference (the delivery order name). |
| NR-U76-023 | An inventory valuation entry is only created when the product is storable, the move is valued, the location has an associated account, the quantity is non-zero, and the product category uses real-time (perpetual) valuation. |
| NR-U76-024 | The stock valuation account is the same account regardless of cost method (standard, average, or FIFO); the cost method affects the computed monetary value, not the account used. |
| NR-U76-025 | Creating invoices from a sales order is done with elevated privileges so that salespeople without billing access can still trigger invoicing from the order. |
| NR-U76-026 | The invoice creation helper assembles a list of invoice value dictionaries from the order and each invoiceable line, then passes the list to the accounting document creation routine. |
| NR-U76-027 | The invoice header values include the billing partner, fiscal position, order name as origin reference, payment terms, and optionally a specific journal if one is set on the order. |
| NR-U76-028 | All invoices generated from sales orders have the document type set to outbound customer invoice. |
| NR-U76-029 | A customer invoice defaults to the first active journal of type sales for the company when no specific journal is set on the order. |
| NR-U76-030 | Invoice line accounts for product lines are resolved from the product category income account, applying any fiscal position mapping. |
| NR-U76-031 | The receivable line on a posted customer invoice uses the billing partner's receivable account. |
| NR-U76-032 | Posting an invoice transitions its state to posted and sets a flag recording that the document has been posted at least once. |
| NR-U76-033 | The post action calls the internal posting routine with soft mode disabled, forcing immediate validation without scheduling for a future date. |
| NR-U76-034 | The payment registration wizard entry point calls internal helpers in sequence: initialise payments, post payments, reconcile payments. |
| NR-U76-035 | Reconciliation between the payment and the invoice is always attempted after the payment is posted; it is not a separate user step. |
| NR-U76-036 | The reconciliation helper finds posted, unreconciled payment lines on the valid payment account types, then calls the standard reconcile routine on the combined set of payment and invoice lines. |
| NR-U76-037 | Only lines with the same account identifier are reconciled together, ensuring the receivable lines from the payment and the invoice are matched and no other accounts are affected. |
| NR-U76-038 | The payment value dictionary includes the chosen journal, the invoice receivable account as the destination account, payment type, partner type, and amount. |
| NR-U76-039 | The liquidity line of a payment entry uses the outstanding receipts account from the payment method configuration, which is typically an intermediary bank-clearing account. |
| NR-U76-040 | The counterpart line of a payment entry uses the partner receivable account; for an inbound customer payment the accounting entry is a debit to the outstanding receipts account and a credit to the receivable account. |
| NR-U76-041 | For an inbound payment the amount on the liquidity line is positive, recording the receipt of funds. |
| NR-U76-042 | The outstanding receipts account is derived from the payment method line selected on the bank or cash journal used for the payment. |
| NR-U76-043 | For a customer payment, the destination account is the billing partner's receivable account, which is the same account that carries the invoice receivable line to be cleared. |
| NR-U76-044 | The reconcile action on a set of journal items delegates to the reconciliation plan executor, which is the single entry point for all matching. |
| NR-U76-045 | The reconciliation plan executor optimises the plan and runs it inside a balanced-entry context, ensuring integrity of all affected accounting documents. |
| NR-U76-046 | When a set of lines reaches full zero residual, a full reconciliation record is created that links all partial reconciliation records and all reconciled lines. |
| NR-U76-047 | The reconciled flag on a journal item is a stored computed field that becomes true when the item's residual amount reaches zero. |
| NR-U76-048 | The residual amount on a journal item equals its original balance minus the sum of all matched debit partial amounts plus the sum of all matched credit partial amounts; it reaches zero after a full payment reconciliation. |
| NR-U76-049 | The delivery status on a sales order is computed from the states of its linked transfers; it becomes fully delivered when all transfers are either completed or cancelled. |
| NR-U76-050 | The invoice status on a sales order is computed from the invoice statuses of all non-downpayment, non-section order lines; it becomes fully invoiced only when every such line reports a fully invoiced status. |
