# U85 Neutral Knowledge — POS Session Lifecycle
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U85-001 | The point-of-sale session object is a standard persistent database model with messaging, activity, bus notification, and data-loading capabilities |
| NR-U85-002 | A point-of-sale session moves through four lifecycle states: Opening Control, In Progress, Closing Control, and Closed and Posted |
| NR-U85-003 | Every new session starts in Opening Control state immediately upon creation |
| NR-U85-004 | The transition from Opening Control to In Progress occurs when the cashier confirms the opening cash count; the start timestamp is recorded at that point |
| NR-U85-005 | The Closing Control state is set when the manager initiates the close flow; draft orders block this transition |
| NR-U85-006 | The Closed and Posted state is set after the session journal entry is successfully posted and all reconciliations complete |
| NR-U85-007 | On creation, the session immediately calls the open-session method, which sets the opening cash balance from the previous session if cash control is active |
| NR-U85-008 | Opening the session sets state to In Progress only when it is in Opening Control state; a guard prevents re-opening |
| NR-U85-009 | If cash control is disabled on the configuration, the Closing Control step is bypassed and the session proceeds directly to close |
| NR-U85-010 | The session holds a link to exactly one accounting journal entry created at close; this is the session move |
| NR-U85-011 | The session closing journal entry is created in the accounting journal configured on the point-of-sale configuration (type general or sale) |
| NR-U85-012 | The session closing journal entry is created once at session close, not per individual order; all order amounts are aggregated first |
| NR-U85-013 | The session closing journal entry is posted only after a balance check passes; if imbalanced, the database changes are rolled back and a wizard is shown |
| NR-U85-014 | The amount accumulation step groups payments by method and type (cash or bank, split or combined) and groups sales lines by income account and tax profile |
| NR-U85-015 | Non-reconcilable move lines cover: sales revenue lines, tax lines, stock expense (cost of goods sold) lines, and cash rounding difference lines |
| NR-U85-016 | Income account on each sales line comes from the product's configured income account resolved through the order's fiscal position |
| NR-U85-017 | Tax lines in the session move use the tax repartition account and tag from each applied tax |
| NR-U85-018 | The cash difference at session close (actual counted cash minus theoretical closing balance) creates a bank statement line with a profit or loss counterpart account taken from the cash journal configuration |
| NR-U85-019 | A positive cash difference (more cash than expected) posts to the cash journal profit account; a negative difference posts to the loss account |
| NR-U85-020 | After the session journal entry is posted, reconciliation links cash receivable lines from the session move with cash statement line receivable lines |
| NR-U85-021 | Bank payment methods generate one aggregated accounting payment record per payment method per session (or one per customer when identify-customer mode is enabled) |
| NR-U85-022 | Reconciliation of bank payment lines pairs the session move receivable line with the receivable line of the generated bank payment move |
| NR-U85-023 | Invoice receivable lines from per-order invoices are reconciled with corresponding receivable lines in the session move so the session move closes the invoice receivable |
| NR-U85-024 | After the session journal entry is posted, uninvoiced orders in paid state are advanced to done state |
| NR-U85-025 | An order triggers a per-order invoice (out-invoice or out-refund) only when the order's to-invoice flag is set and an invoice journal is configured; this invoice is created and posted immediately when the order is finalised |
| NR-U85-026 | The order-level invoice is separate from the session-level closing journal entry; both may exist for the same order |
| NR-U85-027 | Uninvoiced orders do not produce any accounting entry at the time of order finalisation; their effect reaches the ledger only through the session closing entry |
| NR-U85-028 | A point-of-sale session can carry multiple payment methods simultaneously; the configuration links to a many-to-many set of payment methods |
| NR-U85-029 | A payment method type is determined by its linked journal: cash journal produces a cash-type method, bank journal produces a bank-type method, and an absent journal produces a customer-account (pay-later) type |
| NR-U85-030 | For bank payment methods, payments are routed through an outstanding (intermediate) account on the payment method before reaching the bank journal account |
| NR-U85-031 | The intermediary receivable account for a payment method can be overridden per method; if not overridden, the company default point-of-sale receivable account is used |
| NR-U85-032 | Stock movements for delivered products are created as outgoing pickings; these can happen at order finalisation (real-time mode) or at session close (batch mode) depending on configuration |
| NR-U85-033 | When stock is updated at session close, a single batch picking is created for all non-invoiced, non-shipped orders that lack a picking |
| NR-U85-034 | For products with real-time perpetual valuation, the session closing journal entry includes stock expense (COGS debit) and stock valuation credit lines derived from the stock moves |
| NR-U85-035 | COGS lines are included in the session move only for storable products with real-time valuation; the amount uses quantity from the stock move and the product price unit at movement time |
| NR-U85-036 | Cash rounding difference lines in the session move use the profit or loss account from the rounding method when the rounded amount is non-zero |
| NR-U85-037 | Cash transactions during the session (cash-in and cash-out) are stored as bank statement lines linked to the session; their receivable side is reconciled with the session move's cash receivable line |
| NR-U85-038 | The session record carries bank payment references for all aggregated bank payment records created at close |
| NR-U85-039 | The session configuration carries two separate journal references: one for the closing journal entry (general or sale type) and one for invoicing (sale type only) |
| NR-U85-040 | The default balance account for an imbalanced session entry is the company default point-of-sale receivable account |

