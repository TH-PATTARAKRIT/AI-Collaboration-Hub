# U81 Neutral Knowledge — Payment and Bank Reconciliation
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U81-001 | The payment registration wizard is a transient model (disappears after use) whose purpose is to collect payment details and create one or more payment records from one or more invoices. |
| NR-U81-002 | The primary action on the payment wizard creates payments and, if successful, opens a view of the newly created payment records. |
| NR-U81-003 | Payment creation proceeds in three ordered steps: (1) create payment records, (2) post them to activate journal entries, (3) reconcile the payment journal items with the invoice journal items. |
| NR-U81-004 | Payment records are created with a context flag that suppresses invoice synchronization during creation, to avoid premature triggering of dependent logic. |
| NR-U81-005 | Posting a payment transitions its status from draft to an active state and causes the underlying journal entry to become posted. |
| NR-U81-006 | Reconciliation between a payment and an invoice is performed by selecting the journal items from both that share the same account, then calling the standard reconciliation method on the combined set. |
| NR-U81-007 | After reconciliation, the invoice is linked to the payment through a many-to-many relationship tracking matched payments. |
| NR-U81-008 | The payment value dictionary includes the destination account (receivable or payable of the partner) taken from the first invoice line being paid. |
| NR-U81-009 | A payment record is a standalone object with its own status tracking and chatter; it references its underlying journal entry via a link field. The payment and the journal entry are separate database records. |
| NR-U81-010 | A payment has five possible statuses: draft, in-process (equivalent to "posted" in earlier versions), paid, canceled, and rejected. There is no status named "posted" in Odoo 19. |
| NR-U81-011 | The payment record and its journal entry are separate records linked by a reference field; they are not the same database row. |
| NR-U81-012 | The core business fields on a payment are: amount, direction (inbound/outbound), partner classification (customer/vendor), partner, journal, currency, memo, and payment reference. |
| NR-U81-013 | Each payment has an outstanding account — the in-transit account where money sits between the payment being posted and the bank statement confirming receipt. This account is determined by the payment method configuration. |
| NR-U81-014 | The outstanding account on a payment is set from the payment method line's dedicated account, which is configured per journal and payment method combination. |
| NR-U81-015 | Each payment has a destination account — the partner's receivable or payable account — which is where the payment is matched against the invoice. |
| NR-U81-016 | Posting a payment transitions it to active status; the exact state depends on the type of outstanding account configured. |
| NR-U81-017 | When the outstanding account is a cash account, the payment moves directly to "paid" status upon posting (no bank statement matching required). |
| NR-U81-018 | For non-cash outstanding accounts (e.g. bank), the payment transitions to "in-process" status upon posting, awaiting bank statement confirmation. |
| NR-U81-019 | The payment status is recomputed whenever reconciliation events occur: it checks if the outstanding account line's residual amount is zero and/or if all linked invoices are fully paid. |
| NR-U81-020 | A payment transitions from "in-process" to "paid" when the residual amount on its outstanding account line becomes zero — which happens when a bank statement line is reconciled against it. |
| NR-U81-021 | A payment method line is an intermediary record connecting a payment method to a journal; its key role is specifying which account to use for outstanding amounts. |
| NR-U81-022 | The outstanding account on a payment method line determines what account is debited/credited for the in-transit portion of a payment journal entry. |
| NR-U81-023 | The bank statement model still exists in Odoo 19 Community; it serves as a grouping container for statement lines and holds opening and closing balances. |
| NR-U81-024 | A bank statement contains multiple statement lines via a one-to-many relationship; lines can also exist without being attached to any statement. |
| NR-U81-025 | Each bank statement line inherits all fields of a journal entry through delegation inheritance — the line IS backed by a journal entry record, created automatically. |
| NR-U81-026 | The journal entry backing a bank statement line is required, read-only, and cascades deletion — deleting the statement line deletes the entry. |
| NR-U81-027 | A statement line's link to a statement is optional; orphan statement lines (not in any statement) are a valid state. |
| NR-U81-028 | A statement line holds a list of auto-generated payments created during reconciliation, tracked through a many-to-many link. |
| NR-U81-029 | Core fields on a bank statement line include: amount, label, partner, partner name, transaction type, bank account number, foreign currency, amount in foreign currency, and a reconciled indicator. |
| NR-U81-030 | When a bank statement line is created, its underlying journal entry is automatically posted — no manual posting step is needed for statement lines. |
| NR-U81-031 | The suspense account for a bank statement line is taken from the journal's suspense account configuration; it serves as the temporary counterpart account until the line is matched. |
| NR-U81-032 | Creating a bank statement line fails if the journal has no suspense account configured and no explicit counterpart account is provided. |
| NR-U81-033 | A helper method dispatches the statement line's journal entry lines into three categories: liquidity lines (on the bank/cash account), suspense lines (on the suspense account), and other lines (reconciled counterparts). |
| NR-U81-034 | A journal entry line is classified as a suspense line when its account matches the journal's configured suspense account. |
| NR-U81-035 | The reconciled status of a statement line is determined by checking whether the suspense lines have zero residual amount. |
| NR-U81-036 | The default journal entry for a new statement line has two lines: one on the bank/cash account (liquidity) and one on the suspense account (counterpart). |
| NR-U81-037 | The liquidity line of a bank statement entry is always posted to the journal's bank or cash account. |
| NR-U81-038 | The counterpart (suspense) line is posted to the suspense account, where it sits until matched to a payment or invoice. |
| NR-U81-039 | The undo-reconciliation action on a statement line removes all partial reconciliation records on the line's journal items and deletes any auto-generated payments. |
| NR-U81-040 | Undoing reconciliation works by calling the standard remove-reconciliation method on the statement line's journal items. |
| NR-U81-041 | The invoice payment status is computed via a SQL query that looks at partial reconciliation records, tracing from the invoice's receivable/payable lines through to counterpart moves and their associated payments. |
| NR-U81-042 | An invoice's payment status becomes "paid" when its residual amount is zero AND all matching payments have their "is matched" flag set to true. |
| NR-U81-043 | If not all payments are yet matched to a bank statement (outstanding account not cleared), a hook method is called to determine the in-between state — in Community this also returns "paid". |
| NR-U81-044 | In Community edition, the in-payment hook always returns "paid" — there is no separate "in payment" state visible on invoices in Community. |
| NR-U81-045 | The "all payments matched" flag is computed via a conditional aggregate: it checks that every counterpart move associated with a payment has its payment "is matched" flag set. |
| NR-U81-046 | The payment status recomputation checks if the liquidity account line's residual is zero; when it is, the payment becomes "paid". |
| NR-U81-047 | The "is matched with bank statement" flag on a payment is stored and recomputed based on whether the payment's liquidity lines have zero residual. |
| NR-U81-048 | The "is matched" computation checks the residual in either the company currency or the payment currency depending on which is applicable. |
| NR-U81-049 | The liquidity journal entry line of a payment is prepared on the outstanding account (in-transit account) of the payment method. |
| NR-U81-050 | The counterpart journal entry line of a payment is prepared on the partner's receivable or payable account. |
| NR-U81-051 | Reconciling journal items proceeds through the same reconciliation plan mechanism confirmed in earlier research — it creates partial reconciliation records. |
| NR-U81-052 | The reconciliation step in payment creation filters to only posted, valid-type, unreconciled lines before attempting reconciliation. |
| NR-U81-053 | Reconciliation between payment and invoice iterates per shared account: for each account in the payment's counterpart lines, it combines those lines with the matching invoice lines and calls reconcile. |
| NR-U81-054 | The domain for finding matching journal items during bank reconciliation restricts to: posted state, non-reconciled, on reconcilable accounts, and excluding lines from the same statement. |
| NR-U81-055 | The matching domain allows outstanding payment account lines (which are not receivable/payable) to be matched against statement lines, while excluding payment receivable/payable lines from direct matching. |
| NR-U81-056 | A synchronization method keeps the bank statement line fields in sync with its underlying journal entry when key fields change. |
| NR-U81-057 | Bank statement lines always generate journal entries of the "entry" (generic) type, never invoice or bill type. |
| NR-U81-058 | In Community edition, the valid payment states for determining invoice status include both "in-process" and "paid" states, because there is no distinction between them at the invoice level. |
| NR-U81-059 | Delegation inheritance on the statement line means that journal entry fields accessible on the line are actually read from and written to the underlying journal entry record, not stored separately on the line. |
| NR-U81-060 | A bank statement is considered complete when the algebraic sum of its lines equals the difference between its opening and closing balances. |
