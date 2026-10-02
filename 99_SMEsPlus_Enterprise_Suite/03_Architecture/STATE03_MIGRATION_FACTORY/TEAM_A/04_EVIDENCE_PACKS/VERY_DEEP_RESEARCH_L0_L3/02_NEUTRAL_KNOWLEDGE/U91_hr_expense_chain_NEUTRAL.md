# U91 Neutral Knowledge — HR Expense Chain
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U91-001 | An expense record is the atomic unit of employee expense management. It inherits messaging, activity, and analytic-distribution capabilities from shared mixins. |
| NR-U91-002 | The expense status progresses through seven named states: Draft, Submitted, Approved, Posted, In Payment, Paid, and Refused. |
| NR-U91-003 | A separate approval status field (Submitted / Approved / Refused) drives the pre-accounting portion of the workflow; the display status is derived from both the approval status and the linked journal entry state. |
| NR-U91-004 | The three approval-step values are defined as a module-level constant and reused wherever approval-stage filtering is required. |
| NR-U91-005 | The display status is a computed field that merges information from the linked journal entry payment status and the approval status; if no journal entry exists, the approval status is the sole determinant. |
| NR-U91-006 | When no journal entry has been created yet, the expense status equals the approval status, or falls back to Draft if approval has not started. |
| NR-U91-007 | Expenses paid directly by the company jump to Paid as soon as any journal entry is linked, because the cash has already left the company account. |
| NR-U91-008 | The submit action transitions an expense from Draft: it either sets the approval status to Submitted or bypasses approval entirely (auto-validation) when no separate approver is configured. |
| NR-U91-009 | Auto-validation occurs when the expense has no designated manager or when the designated manager is the employee themselves, removing the need for a separate approval step. |
| NR-U91-010 | The approve action writes the Approved approval status, records the approver identity, and stamps the approval timestamp; a duplicate-expense wizard may intercept the flow. |
| NR-U91-011 | The internal approval helper writes Approved status, records the current user as manager, and stores the current date-time as the approval date for every qualifying expense. |
| NR-U91-012 | The post action is the accounting entry point; it requires Approved status and routes to one of two sub-paths depending on whether the expense was paid by the employee or the company. |
| NR-U91-013 | A pre-check guard raises a user-facing error if any selected expense is not in Approved state, preventing premature journal entry creation. |
| NR-U91-014 | Employee-paid expenses generate a vendor receipt type of journal entry; the partner on the move is the employee's work contact. |
| NR-U91-015 | The debit side of the expense journal entry uses the expense's designated account, resolved through a four-step fallback: expense account, product expense account, company expense account, then purchase journal default account. |
| NR-U91-016 | The credit side of the employee-paid expense journal entry is the employee's payable account (the accounts payable partner property), representing the reimbursement liability to the employee. |
| NR-U91-017 | Company-paid expenses create a payment record alongside the journal entry; both are posted together when the payment is confirmed. |
| NR-U91-018 | When creating company-paid moves, the project identifier is explicitly removed from context to prevent unintended project-related defaults from being injected into the entries. |
| NR-U91-019 | The journal entry model carries a reverse relation to the originating expenses, allowing the entry to navigate back to all expenses it covers. |
| NR-U91-020 | Each journal entry line optionally carries a link to a single originating expense, enabling line-level expense attribution, reinvoice determination, and analytic exclusion in project profitability. |
| NR-U91-021 | A dedicated module bridges projects and expenses: when a new expense is created in a project context, the project's analytic distribution is pre-populated on the expense. |
| NR-U91-022 | The project analytic distribution is sourced from the project record's own analytic distribution method and used as the default on the expense at creation time. |
| NR-U91-023 | Expenses are linked to projects exclusively through analytic distribution: an expense belongs to a project when its analytic distribution contains the project's analytic account identifier. There is no direct project reference field on the expense record. |
| NR-U91-024 | Project profitability reporting for expenses filters by analytic distribution against the project's analytic account and restricts to expenses in Posted, In Payment, or Paid state. |
| NR-U91-025 | A separate module (sale expense) adds two reinvoicing fields to the expense: a reference to the customer sales order and a reference to the resulting sales order line. |
| NR-U91-026 | Whether an expense can be reinvoiced is driven by the product's re-invoice policy; only the "at cost" and "at sales price" values make reinvoicing available. |
| NR-U91-027 | When posting an expense that has a sales order but no analytic distribution, the system auto-creates an analytic account from the sales order and assigns it to the expense, ensuring the reinvoice mechanism can function. |
| NR-U91-028 | A journal entry line is eligible for reinvoicing when its linked expense has a re-invoiceable product policy, a sales order is set on the expense, and the line is a product (not a tax or payment-term) line. |
| NR-U91-029 | The target sales order for reinvoice is sourced directly from the expense record on the journal entry line, overriding any other sales-order determination logic for expense-originated lines. |
| NR-U91-030 | The sales order line created for reinvoice carries a back-reference to the originating expense records, enabling traceability from the customer invoice back to the underlying expense. |
| NR-U91-031 | The sales order line model carries a One2many to expenses, representing all expenses reinvoiced through that line; this is the inverse of the expense's sales order line reference. |
| NR-U91-032 | The product re-invoice policy has three values: no reinvoice, reinvoice at cost, or reinvoice at the product's sales price. The default is no reinvoice. |
| NR-U91-033 | A further module combining project, sales, and expense logic overrides the posting action: when a project is linked to the sales order and no analytic distribution exists on the expense, it creates and assigns the project's analytic account. |
| NR-U91-034 | When a project analytic and an existing expense analytic coexist on different analytic plans, both distributions are merged; when they share the same plan, the project analytic takes priority. |
| NR-U91-035 | The payment mode field on an expense record is the primary fork point of the entire posting workflow: employee-paid expenses create a reimbursable vendor receipt; company-paid expenses create a payment entry marking the cash already disbursed. |
