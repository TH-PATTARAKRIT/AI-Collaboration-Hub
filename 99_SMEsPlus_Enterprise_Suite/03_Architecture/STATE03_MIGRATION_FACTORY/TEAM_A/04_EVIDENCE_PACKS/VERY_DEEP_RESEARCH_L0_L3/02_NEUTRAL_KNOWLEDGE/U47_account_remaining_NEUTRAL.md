# U47 neutral knowledge — account remaining (bank reconcile, currency, accrued orders, payment register)

> Neutral knowledge layer. Derived from Odoo 19 Community source study; status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Statements describe what a business system must do and why. No vendor implementation structure, no snake case identifiers, no file paths, no code.

---

## CAP-U47-01 Bank Statement Line Reconciliation

[N-U47-001] A bank statement line represents a single transaction imported or manually entered from a bank. Each such line begins in an unreconciled state and must be matched to one or more accounting entries before it can be marked as reconciled. Until matching is complete, the unmatched portion is held temporarily in a suspense account so that the bank account balance remains accurate in the general ledger.

[N-U47-002] The system must be able to identify at any time which bank statement lines are unreconciled. A running balance must be computable for each line by finding the nearest prior statement's opening balance as a fixed starting point, then accumulating posted transaction amounts forward from that anchor. This avoids recalculating the entire history every time.

[N-U47-003] Each bank statement line carries a sort key that encodes the transaction date, a reversed sequence number, and an internal record identifier. This key enables efficient ordering and range queries without compound database indexes spanning columns across different data tables.

[N-U47-004] When a bank statement line is created, its corresponding accounting entry is posted immediately and automatically. The entry always contains exactly one line to the bank or cash account and one counterpart line, initially pointing to the suspense account until reconciliation assigns a real account.

[N-U47-005] Undoing a bank reconciliation removes all matching relationships between the bank line and its counterpart entries and deletes any automatically generated payment records that were created during that reconciliation. The line returns to an unreconciled state with the suspense account restored as counterpart.

[N-U47-006] Deletion of a bank statement line is blocked when the parent bank statement has been validated and closed. A confirmed, complete statement serves as a permanent record; its individual lines must not be removed without first removing the statement itself.

[N-U47-007] When a company uses a restrictive audit trail, removing a bank statement line requires first cancelling the underlying accounting entry rather than deleting it outright, preserving the audit record.

[N-U47-008] The system may optionally auto-create a partner bank account record when reconciling a bank line that carries a bank account number but whose partner does not yet have that account registered. A configuration switch can disable this automatic creation.

---

## CAP-U47-02 Multi-Currency Rate Tables for Reporting

[N-U47-004] When preparing financial reports that aggregate amounts across multiple companies with different home currencies, the system must convert all amounts to a common reporting currency. Three conversion rate types are needed: the current rate (most recent rate at the report date), the historical rate (the rate in effect on the date of each individual transaction), and the average rate for a period (weighted by the number of days each rate was in effect).

[N-U47-009] For a single-currency environment where all companies share the same currency, the system optimises by using a fixed conversion factor of one without creating any database temporary structures.

[N-U47-010] In a multi-currency environment, a temporary in-memory rate table is assembled at the start of each reporting operation and discarded when the database transaction ends. This table stores the applicable rate per company, per period, per rate type, enabling reports to join against it uniformly regardless of whether one or all three rate types are needed.

[N-U47-011] The average rate calculation divides the period into segments wherever either the home currency's rate or the foreign currency's rate changes. Each segment is weighted by its number of days. The result is the day-weighted mean conversion factor for the full period.

[N-U47-012] The system prevents reducing the number of decimal places of a currency that has already been used in accounting entries. Doing so would cause existing records to round differently and invalidate historical balances.

---

## CAP-U47-03 Payment Registration from Invoices

[N-U47-005] The payment registration process takes one or more outstanding receivable or payable invoice lines and converts them into one or more payment records. The system groups lines by partner, account, currency, and bank account. Groups that belong to the same partner and have the same bank details in both directions can be merged into a single payment.

[N-U47-013] Payment amounts can be computed in several ways depending on installment schedules: the full outstanding balance, only the overdue amount, the next single installment, or all installments falling before a specified future date.

[N-U47-014] When an early payment discount applies — where paying before a certain date entitles the payer to a reduced amount — the system pre-populates the payment amount at the discounted level and automatically generates write-off lines to close the remaining tax or full balance.

[N-U47-015] If the user enters a payment amount that differs from both the full amount and any installment amounts, the system treats this as a custom amount and preserves it even when the currency or date is subsequently changed.

[N-U47-016] A payment difference arises when the user chooses to pay an amount other than the outstanding balance. The system offers two handling options: leave the invoice partially open, or mark it as fully paid by posting the difference to a designated write-off account.

[N-U47-017] When the write-off account is a currency exchange account and the payment uses a different currency than the invoice, the system applies a forced exchange rate so that the difference goes entirely to exchange gain or loss rather than split across rounding.

[N-U47-018] Payments are only allowed when the recipient's bank account has been manually validated as trusted. The system flags untrusted accounts and missing bank accounts before allowing the payment to proceed. Untrusted accounts must be explicitly approved before payment.

[N-U47-019] When a payment is made on behalf of related subsidiary companies (siblings under the same parent), the system operates with elevated access so that the parent company can create payments on behalf of its branches, without exposing the branch's transactions to the current user's normal access scope.

[N-U47-020] A QR code for scanning with a banking application is generated automatically for outbound manual payments when the recipient bank account is trusted and validated.

[N-U47-021] The system checks whether payments in progress already exist for the same partner, amount, and date before allowing registration, surfacing these as a danger-level warning rather than a hard block.

---

## CAP-U47-04 Accrued Orders (Purchase and Sale)

[N-U47-007] An accrual entry wizard allows an accountant to record the financial impact of goods or services that have been received but not yet invoiced (purchase accruals) or delivered but not yet billed (sales accruals) as of a specific date. The entry brings the accounting into alignment with operational reality at period end.

[N-U47-022] Every accrual entry created by this process is immediately accompanied by an automatic reversing entry posted the following day, creating a the record-cancelling pair. The reversal ensures the accrual has no lasting effect in the next period unless renewed.

[N-U47-023] For purchase orders, the accrual amount is based on the difference between the quantity received and the quantity invoiced, valued at the purchase price. For sales orders, it is based on the difference between the quantity delivered and the quantity invoiced, valued at the sales price.

[N-U47-024] The wizard requires that all selected orders belong to the same company and use the same currency. Cross-company or multi-currency selections are rejected.

[N-U47-025] The accrual account used for the offsetting entry differs by direction: for purchase accruals, a current liability account is used; for sales accruals, a current asset account is used.

[N-U47-026] An optional override amount can be specified for a single selected order, replacing the computed quantity-based amount with a manually entered value. This is useful for estimates or rounding corrections.

[N-U47-027] When a product uses perpetual inventory valuation, the system calculates a separate stock variation entry alongside the expense entry to properly split the accrual between the income and expense account and the stock variation account.

[N-U47-028] Analytic distributions from the order lines are proportionally carried into the accrual entry's offsetting line, weighted by each line's share of the total order value.

---

## CAP-U47-05 Journal Entry Reversal

[N-U47-008] A journal entry or invoice can be reversed by creating a mirror entry that exactly offsets all original amounts. The reversal must be dated (either today, a past date, or a future date) and must use a journal of the same type as the original.

[N-U47-029] When the reversal date falls in the future, the system schedules the reversal entry for automatic posting on that date rather than posting it immediately.

[N-U47-030] In amendment mode, the system creates both the reversing entry to cancel the original and a new copy of the original entry for the accountant to edit. Only the product lines and descriptive lines are copied to the new entry; payment terms and computed lines are excluded.

[N-U47-031] For plain journal entries (not invoices) and entries reversed without future dating, the original entry is cancelled at the same time as the reversal is posted. For invoices reversed with a credit note, the original remains open until explicitly reconciled.

[N-U47-032] A message is logged on the original entry after reversal, linking to the new reversing document, providing a visible audit trail.

[N-U47-033] Reversal requires all selected entries to belong to the same company and all to be in posted state. Non-posted or multi-company selections are rejected.

---

## CAP-U47-06 Reconciliation Pairs and Tax Cash Basis

[N-U47-009] Each matching between an unpaid debit journal item and an unpaid credit journal item is recorded as a partial reconciliation pair carrying the matched amount in both the company currency and each line's own currency. When all items in a group are fully matched, a full reconciliation record is created.

[N-U47-034] A matching number is assigned to every journal item involved in a reconciliation. Partially matched items receive a temporary number prefixed to indicate partial status; fully matched items receive the full reconciliation identifier as their number. Matching numbers are updated in bulk via direct database operations for performance.

[N-U47-035] When a tax is configured to become due only when payment is received (tax on cash basis), each reconciliation event triggers the creation of a special journal entry proportional to the matched amount. This entry records the portion of the tax that is now reportable. When the reconciliation is reversed, these tax entries are themselves reversed.

[N-U47-036] Cash basis journal entries are only posted when both the invoice and the payment are in posted state. If either side is in draft, the cash basis entry is created but held in draft.

[N-U47-037] The accounting date of cash basis entries respects fiscal lock dates: if the payment or settlement date falls within a locked period, the entry is dated to the first day after the lock.

[N-U47-038] When a reconciliation is removed, any exchange difference entries and cash basis entries that were created as a result are automatically reversed. Payment states that transitioned to paid revert to in-process.

[N-U47-039] The percentage of tax to recognise in each cash basis entry is the proportion of the total invoice balance covered by the current partial payment. For foreign currency invoices, this percentage is computed in the invoice currency; for company-currency invoices, it is computed in the company currency.

---

## CAP-U47-07 Full Reconciliation Completion Record

[N-U47-010] When all outstanding amounts in a reconciliation group reach zero, a completion record is created to formally mark the group as fully reconciled. This record links all the partial matching pairs and all the involved journal items. When this record is removed, matching numbers on surviving items revert to reflect their remaining partial matches.

---

## CAP-U47-08 Bank Statement Matching Rules

[N-U47-011] An accountant can define named rules that the bank reconciliation screen uses to automatically identify and apply matching counterpart entries to incoming bank lines. Each rule specifies conditions the bank line must meet (amount range, label pattern, partner, journal) and one or more counterpart line templates with configurable amounts.

[N-U47-040] Rules can be set to manual mode (only suggest, user must confirm) or automated mode (apply the match and fully reconcile without user confirmation). Automated rules run during the bank reconciliation batch process.

[N-U47-041] Counterpart line amounts can be specified as a fixed value, as a percentage of the outstanding balance, as a percentage of the statement line amount, or as a value extracted from the statement line label using a regular expression pattern.

[N-U47-042] A special rule type called a partner mapping rule assigns a partner to an incoming bank line based on a label pattern match, without creating any counterpart entry. These rules are identified by having exactly one line with a partner set but no account.

[N-U47-043] Analytic distributions can be attached to each reconcile rule line, enabling automatic cost-centre assignment during bank reconciliation.

---

## CAP-U47-09 Payment Terms and Installment Schedules

[N-U47-012] Payment terms define how the total of an invoice is divided across multiple due dates. Each installment can be expressed as a percentage of the total or as a fixed amount. The final installment always receives the remaining balance regardless of rounding, ensuring the sum of all installments equals the invoice total.

[N-U47-044] Due date calculation supports four timing methods: a fixed number of days after the invoice date; a fixed number of days after the end of the invoice month; a fixed number of days after the end of the following month; or a specific day of the next calendar month after a given number of days.

[N-U47-045] Payment terms support an early payment discount: a percentage reduction of the amount due if payment is made within a specified number of days. The discount can apply to the full invoice amount or only to the pre-tax amount, depending on the country's tax regulation. Belgium uses a mixed approach (always deducted upfront); the Netherlands uses an exclusion approach (never reduces tax); all other countries default to reducing the full amount on early payment.

[N-U47-046] A payment term cannot be deleted if any invoice or journal entry still references it. Archiving is the supported way to retire a payment term from active use.

[N-U47-047] When cash rounding is configured on an invoice (for countries where coinage constraints require rounding to a specific precision), the payment term installment amounts are individually adjusted to satisfy both the rounding precision and the requirement that all installments sum to the total.

---

## CAP-U47-10 Cash Rounding

[N-U47-013] Cash rounding allows invoices to be rounded to the nearest physically available coin denomination. The rounding precision, the direction of rounding (always up, always down, or to nearest), and the accounts to use for rounding gains and losses are all configurable.

[N-U47-048] The rounding adjustment on an invoice can be handled in two ways: by adding a separate rounding line that makes the difference explicit, or by adjusting the largest tax amount on the invoice by the rounding difference.

[N-U47-049] The profit and loss accounts for cash rounding differences can be set independently per company, supporting multi-company environments where each entity has its own chart of accounts for rounding entries.
