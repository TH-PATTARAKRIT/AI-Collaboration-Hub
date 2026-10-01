# U12 — Payments, Reconciliation, Payment Terms and Payment Providers — NEUTRAL KNOWLEDGE

> Source basis: Odoo 19 Community

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

> Clean-room layer: statements describe what the system must do and why, in generic business language.


## Capability 01 — Payment lifecycle

### WHAT

- [N-U12-001] A payment is the record of money received from a customer or sent to a vendor. Confirming it creates and posts a journal entry in the chosen bank or cash journal.
- [N-U12-002] A payment carries a direction (receive or send), a partner type (customer or vendor), an amount, a currency, a date, a memo, a journal, a payment method and, optionally, the recipient bank account.

### WHY

- [N-U12-003] Keeping the payment as its own record lets users prepare, confirm, hand over, cancel and review a money movement separately from the accounting entry, while the system keeps the entry synchronised with the payment.

### BUSINESS RULE

- [N-U12-008] Confirming a payment that has no entry generates the entry: one money-side line on an intermediate account and one counterpart line on the partner's receivable or payable account, and then posts it.
- [N-U12-009] A receipt debits the intermediate account and credits the counterpart; a payment does the opposite. Any settlement-difference or withholding lines are carried as extra lines so that the entry stays balanced.
- [N-U12-010] The payment amount is converted to company currency at the payment date unless the caller forces a specific balance.
- [N-U12-011] The intermediate account comes from the payment method line of the journal. If none is configured, the system falls back to the chart's outstanding receipts or outstanding payments account, then to the company transfer account, and refuses to create the payment if none exists. This fallback applies only in the base edition, without the enhanced accounting add-on.
- [N-U12-012] The counterpart account defaults to the partner's receivable account for customers or payable account for vendors. Without a partner, the first receivable or payable account of the company is used.
- [N-U12-013] A payment amount is never negative; the direction expresses whether money comes in or goes out.
- [N-U12-014] A payment takes its number from its journal entry once confirmed; a draft payment has no number.
- [N-U12-015] While the entry is still draft, changes to date, amount, direction, partner, accounts, bank account or journal are pushed into the entry. Once the entry is posted, the payment no longer rewrites it.
- [N-U12-016] Possible duplicates, meaning draft or in-process payments with the same partner, company, direction, date and amount, are flagged to the user.
- [N-U12-017] A sent payment by a method that requires a recipient bank account can be confirmed only if that bank account has been validated as trusted. In the base setup no method requires it.
- [N-U12-030] State changes, partner, amount, date and method of a payment are tracked in its history, and status messages of the entry are forwarded to the payment.

### STATE

- [N-U12-004] A payment is in one of five statuses: draft, in process, paid, canceled or rejected. A new payment starts as draft.
- [N-U12-005] Confirming a draft payment moves it to in process. If the intermediate account is a cash-type account, it moves directly to paid.
- [N-U12-006] A payment in process becomes paid when the money-side line of its entry has no open amount left, or when that line sits on an account that cannot be matched, or when every invoice it settled has become paid. The status is recomputed whenever matching changes.
- [N-U12-007] Validate, reject, cancel and reset-to-draft are explicit actions that set the status to paid, rejected, canceled and draft. Cancel removes a still-draft entry or cancels a posted one. Reset-to-draft also resets the entry to draft.
- [N-U12-021] A payment is marked matched when its money-side lines have no open amount, or when it is posted directly to the bank account; it is marked reconciled when its counterpart lines have no open amount.

### OPTIONALITY

- [N-U12-025] The payment methods offered depend on the journal, and other extensions can filter them (for example, hiding electronic methods).

### DEPENDENCY

- [N-U12-022] Deleting a payment first resets its entry to draft and deletes it, and then recalculates the payment status of the invoices it had settled.
- [N-U12-023] Cancelling an entry from the journal entry side marks its linked payments as canceled.
- [N-U12-024] Bank, cash and credit-card journals use a dedicated payment number sequence by default, separate from bank transactions.

### CONSTRAINT

- [N-U12-018] A payment that is neither draft nor canceled and that has an intermediate account must have a journal entry.
- [N-U12-019] A payment must have a payment method, and the method must belong to the payment's journal.
- [N-U12-020] The amount cannot be changed on a payment whose entry has several money-side lines.

### RISK

- [N-U12-026] A rejected payment keeps its posted entry and any settlement it already produced. No step in the studied scope reverses them.
- [N-U12-027] A payment can be reset to draft while its entry is already matched with an invoice. No step in the studied scope removes that matching on reset; only cancel and delete do.

### UNKNOWN

- [N-U12-028] Whether a paid status is reached immediately or only after bank matching for a standard bank payment needs execution to confirm, because the status also flips to paid once all settled invoices are paid.
- [N-U12-029] A field links two payments as an internal transfer pair, but no process creating such a pair was found in the studied scope.


## Capability 02 — Payment registration against invoices and bills

### WHAT

- [N-U12-031] Registering a payment lets a user pay or collect one or several open invoices, bills, credit notes or other receivable and payable items in one guided step that creates the payments, confirms them and settles the items.

### WHY

- [N-U12-032] A single guided step avoids creating a payment and then matching it by hand, and lets related items be paid together while respecting differences in partner, currency and recipient bank account.

### BUSINESS RULE

- [N-U12-033] Only posted documents can be paid from the document screens. Miscellaneous entries cannot be paid this way, and documents flagged as blocked cannot be paid.
- [N-U12-034] Only receivable or payable items that still have an open amount are offered. If nothing is open, the user is told there is nothing left to pay.
- [N-U12-035] Items from different top-level companies cannot be paid together, items from sibling companies require access to the parent company, and receivable and payable items cannot be mixed.
- [N-U12-036] Selected items are grouped into batches by partner, account, currency, recipient bank account and partner type. A partner's receipts and payments that each have a single bank account can be netted into one batch whose direction follows the sign of the total.
- [N-U12-037] When there is a single batch the user can edit amount, memo, journal, method, bank account and date. With several batches the screen is read-only and one payment is created per batch or per document.
- [N-U12-038] Grouping several items of one batch into a single payment is offered only when several items are involved and not for a single invoice. By default grouping is on for a single document and off otherwise; without grouping one payment per document is created.
- [N-U12-039] The proposed amount is the amount due now: overdue installments or the next installment for installment terms, the discounted amount when an early payment discount applies, otherwise the full open amount. The user can switch to the full amount or type a custom amount.
- [N-U12-040] A difference between the amount due and the amount entered can be left open, which leaves the item partially paid, or written off to a chosen account with a label. By construction the same mechanism covers an amount above the due amount, with the opposite sign.
- [N-U12-041] The difference section is shown only when a difference exists, no early payment discount is being applied, the screen is editable, the payment is single or grouped, and the method has an intermediate account.
- [N-U12-042] When the amount entered equals the discounted amount, or the full amount, while an early payment discount applies, the difference is written off automatically to the company's cash discount accounts and the manual write-off section is hidden.
- [N-U12-043] When the chosen write-off account is the company's exchange gain or loss account, the settlement is performed with a forced rate so that the difference lands in the exchange difference.
- [N-U12-044] The payment currency defaults to the journal currency, else the currency of the items, else the company currency. Amounts are converted at the payment date. When the payment currency differs from the item currency and the converted amounts match, the exact company-currency balance is forced so no cents remain open.
- [N-U12-045] Only bank, cash and credit-card journals that have a method for the direction are offered. The default journal is that of the document's preferred method, otherwise one matching currency and recipient bank account. The default method is the document's or partner's preferred method, otherwise the first available.
- [N-U12-046] The recipient bank account for receipts is the journal's own bank account; for payments it is one of the partner's accounts valid for the company, defaulting to the one on the document or the first available.
- [N-U12-047] When the method requires a validated bank account, batches whose account is missing or not trusted are skipped, a warning states how many, and if every batch is skipped the user gets an error.
- [N-U12-048] The memo defaults to the document's payment reference, reference or number. For several receipts it comes from a batch sequence, and for several vendor payments it is the list of document references.
- [N-U12-049] Payments created by the guided step are confirmed and then matched against the open items on each account they touch. The settled documents are linked to the payment.
- [N-U12-050] A warning is displayed when payments in process already exist for the selected documents, to prevent paying twice. Possible duplicate payments are also flagged.
- [N-U12-051] Registering a payment on a draft document is possible, but the difference handling is then forced to keep open.

### OPTIONALITY

- [N-U12-055] Grouping, journal, method, recipient bank, amount and difference handling are all user choices with computed defaults; the early payment discount comes from the payment term of the document.

### DEPENDENCY

- [N-U12-052] When electronic payment methods are installed, the guided step also offers a saved payment token for the chosen method and passes it to the payment.

### CONSTRAINT

- [N-U12-053] Only users with the invoicing role, or a role that includes it, can use the guided step.

### UNKNOWN

- [N-U12-054] The behaviour of an overpayment settled through the write-off mechanism, and rounding in foreign-currency settlements, needs execution to confirm.


## Capability 03 — Reconciliation engine

### WHAT

- [N-U12-056] Reconciliation matches debit items against credit items on the same account so that invoices, payments, refunds and bank transactions settle each other. Every pairing is recorded as a partial match with its own amounts.

### WHY

- [N-U12-057] Matching tells the system which receivables and payables are still open and keeps company-currency and foreign-currency balances consistent after each pairing.

### BUSINESS RULE

- [N-U12-058] Only items of one account and one top-level company, not already fully matched and not on cancelled entries, can be matched together. The account must allow matching, or be a cash or credit-card account.
- [N-U12-059] Items are paired in a fixed order (due date or date, then currency, then amount); debits and credits are paired off one after the other until one side is exhausted.
- [N-U12-060] Each pairing creates a partial match with a positive amount equal to the smaller of the two open amounts, recorded in company currency and in each item's own currency.
- [N-U12-062] When both items share a foreign currency the match is made in that currency, otherwise in company currency. For invoice items the rate comes from the invoice date; for payment or bank-transaction items the rate already booked on the item is used.
- [N-U12-063] Small rounding differences caused by exchange rates are tolerated so that neither stray cents nor needless exchange entries are produced.
- [N-U12-064] When a fully matched item still has a difference in the other currency, an exchange difference entry is created automatically in the company's exchange journal, using the gain or loss account according to the sign, and that entry is itself matched with the original item.
- [N-U12-065] The exchange difference entry is posted when both matched items are posted. It is dated at the later of the exchange journal's accounting date and the dates of the matched items.
- [N-U12-068] A matching number is either a plain number for full matches, the letter P followed by a number for partial matches, or the letter I followed by free text as a temporary marker used by imports until all marked entries are posted, after which the real match is made.
- [N-U12-071] Removing a match removes the partial matches and their full match record, recomputes matching numbers, reverses (or deletes if still draft) the exchange difference and cash-basis entries linked to the matches, and dates the reversal in the original period unless a lock date forbids it, in which case the day after the lock date is used.
- [N-U12-072] Changing the account, date, amount, balance or currency of a matched item automatically removes its matches. Changing the account is allowed if all items of the match change together. Matched bank transaction lines are returned to their unmatched state when no lock prevents it.
- [N-U12-073] Deleting a journal item or a journal entry first removes its matches.
- [N-U12-074] Users with the full accounting role can unmatch selected items through a list action that removes every match of the matching groups of those items.
- [N-U12-075] On an invoice, posted unreconciled credits or debits of the same partner and account with an open amount are offered and can be applied with one click; an applied match can be removed again from the invoice.

### STATE

- [N-U12-061] The open amount of an item is its original amount minus its matches. An item is reconciled when both its company-currency and foreign-currency open amounts are zero. Items on accounts that cannot be matched never carry an open amount.
- [N-U12-067] When every item in a connected group of matches is fully matched, a full match record is created and all its items receive the same matching number. Items that are only partly matched carry a partial marker followed by a number.

### OPTIONALITY

- [N-U12-076] Exchange differences can be suppressed for technical matches, for instance when the exchange entry itself is matched.

### DEPENDENCY

- [N-U12-069] When the company uses cash-basis taxes, a match also triggers the creation of cash-basis tax entries (owned by the tax unit). They are skipped for matches made while reversing with cancellation or when explicitly disabled, and they need a cash-basis journal.
- [N-U12-070] When an invoice becomes paid, a notification step runs so that other applications can react; for example a sales order records that its invoice was paid.
- [N-U12-077] Edits and deletions that would break a match are subject to lock-date checks owned by the journal entry unit; unmatching moves the reversal date past a lock when needed.

### CONSTRAINT

- [N-U12-066] Creating exchange differences requires the exchange journal and both exchange accounts to be configured; otherwise matching is refused with a configuration error.
- [N-U12-078] Items on off-balance accounts cannot be matched.
- [N-U12-083] Users with the invoicing role can create and delete matches; users with the full accounting role have the same rights; read-only accountants can only view them.

### RISK

- [N-U12-079] A helper that would refuse modification of a posted matched item exists but was not found to be called anywhere in the studied code; the effective protection is the automatic removal of matches on edit.
- [N-U12-080] Resetting a matched entry to draft does not itself remove its matches.

### UNKNOWN

- [N-U12-081] The precise outcome of multi-currency rounding and exchange difference amounts in real combinations needs execution to confirm.
- [N-U12-082] A candidate filter for matching bank transactions exists, but no consumer of it was found in the studied scope.


## Capability 04 — Payment status on invoices

### WHAT

- [N-U12-084] The payment status of an invoice, bill, credit note or receipt tells whether it is unpaid, partly paid, paid, reversed, or blocked from payment.

### WHY

- [N-U12-085] The status drives dashboards, the customer portal pay button, follow-up, expense status and reporting, so it must be derived automatically from the actual settlement of the document.

### BUSINESS RULE

- [N-U12-088] A fully settled document with a payment or bank transaction line among its counterparts is paid once all those payments have been matched to the bank, and otherwise takes the in-payment value defined by the edition.
- [N-U12-090] A payment recorded without any entry and linked to a posted document that still has an open amount gives that document the in-payment value of the edition (paid in the base edition) when the payment is in process or paid.
- [N-U12-092] A user can block a document from payment, which hides the registration of payments for it; unblocking recomputes the real status. A paid or in-payment document cannot be blocked.
- [N-U12-095] The list of payments reconciled with a document merges payments found through matches with payments explicitly linked to the document, filtered by what the user may read.

### STATE

- [N-U12-086] A document that is posted (or a draft one with a non-zero total) is not paid until matched amounts appear; any match that leaves an open amount makes it partly paid; an open amount of zero makes it paid; blocked and legacy values are kept as they are.
- [N-U12-087] A fully settled document is shown as reversed instead of paid when it was settled only by refunds or by miscellaneous entries of the opposite kind and no money payment or bank transaction line took part.
- [N-U12-091] The status is recomputed whenever the open amounts or matches of the document change, when a counterpart payment's matched flag changes, and when a linked payment is deleted.

### OPTIONALITY

- [N-U12-089] The in-payment status is defined by the edition. In the base edition, without the enhanced accounting add-on, it is mapped to paid, so documents show paid as soon as the settling payment is posted, even before the bank match.

### DEPENDENCY

- [N-U12-093] Journal dashboards count only unpaid and partly paid documents, the invoice analysis report carries the status, the portal offers online payment only for unpaid, in-payment or partly paid customer invoices, and expense and sales-team figures read the status.
- [N-U12-094] A transition to paid is announced to followers of the document through a dedicated message subtype.

### CONSTRAINT

- [N-U12-097] The payment status field cannot be edited directly by users; it is read-only and computed.

### RISK

- [N-U12-096] Because a payment becomes paid when all its documents are paid, and a document becomes paid when its payment is posted in the base edition, payment and document statuses can influence each other; the order of recomputation needs execution to confirm.

### UNKNOWN

- [N-U12-098] How a blocked document behaves when it later receives a match through another path, such as a credit note, needs execution to confirm.


## Capability 05 — Bank statements, statement lines and reconcile models

### WHAT

- [N-U12-099] A bank statement groups the bank or cash transaction lines of one journal and acts as a checkpoint: its starting balance, its computed ending balance and the ending balance stated by the bank are compared.
- [N-U12-100] A bank transaction line is an entry in the bank journal: one line on the bank account and a temporary counterpart on a suspense account until the transaction is matched to an invoice, a payment or an account.

### WHY

- [N-U12-101] Statements let accountants check that the book balance of a bank journal agrees with the bank's own statements, and the suspense account keeps every unexplained transaction visible until it is matched.

### BUSINESS RULE

- [N-U12-103] The starting balance of a statement is computed from the previous statement's ending balance plus the transactions in between. The ending balance stated by the bank defaults to the computed one and can be edited.
- [N-U12-104] A statement takes the date of its last posted line and is ordered by the position of its first line, which is derived from date and sequence.
- [N-U12-105] A statement can be created from existing transactions by splitting at a given line, from one line, or from a multiple selection. Selected lines must belong to one journal and be contiguous; cancelled lines in between are ignored.
- [N-U12-106] Creating a transaction line forces its entry to be a miscellaneous entry, creates both its lines and posts it automatically, so users do not manage its posting status.
- [N-U12-107] The counterpart of a new transaction defaults to the suspense account of the journal. Creation without a suspense account is refused unless another counterpart account is given.
- [N-U12-111] Changes to the label, amount, currency, partner or journal of a transaction are written into its entry, and changes of the entry lines are written back to the transaction, so both stay consistent.
- [N-U12-112] When a transaction line is deleted, the company's restrictive audit trail setting turns the deletion into cancellation of the entry. Lines of a statement that is both valid and complete cannot be deleted until the statement itself is removed.
- [N-U12-113] Undoing the reconciliation of a transaction removes its matches, deletes payments that were generated automatically during it and restores the standard bank and suspense lines. Reviewed and matched transactions can only be changed by the accountant role.
- [N-U12-114] A bank account number carried by a transaction can create the partner's bank account when matched, unless a system parameter turns this off, in which case only an existing account is used.
- [N-U12-115] The candidates offered for matching a transaction are posted entries (or draft entries that have a partner when requested) on matchable accounts, not already reconciled, not belonging to the same transaction, excluding payment lines on receivable or payable accounts, within the company and its child companies.
- [N-U12-116] The running balance of transaction lines uses statement starting balances as anchors and counts only posted lines.
- [N-U12-120] Reconcile models are presets describing what to propose or create when matching: a trigger (manual or automated), conditions on journal, amount range, label content or pattern and partner, and one or more entry lines whose amount is fixed, a percentage of the balance, a percentage of the transaction, or extracted from the label.
- [N-U12-122] A model that matches on label and has a single line with a partner and no account is a partner mapping and is not proposed as an ordinary rule.
- [N-U12-123] A model can be switched between manual and automated, and the entries it created can be listed from the model. Copying a model gives it a unique name ending with the word copy.
- [N-U12-124] Two presets are created with the chart: one for internal transfers, whose line uses the company transfer account, and one for bank fees, triggered by the label containing bank fees.
- [N-U12-129] No scheduled job in the studied scope processes statements or applies reconcile models; the only scheduled jobs of the accounting base are automatic posting of draft entries and sending of invoices.

### STATE

- [N-U12-102] A statement has no workflow status. It is described by two checks: complete, when the sum of its lines equals the ending balance minus the starting balance, and valid, when its starting balance equals the ending balance of the previous statement of the same journal. The first statement of a journal is always valid.
- [N-U12-109] A transaction counts as reconciled when no open amount remains on its suspense line, or when its entry no longer has a suspense line. While the entry is not yet reviewed, the open amount is the full transaction amount.

### OPTIONALITY

- [N-U12-117] The source of statements is defined per journal as a bank feed. In this edition only an undefined source exists, so statements are entered manually or supplied by external connectors.

### DEPENDENCY

- [N-U12-118] The journal dashboard counts transactions still to reconcile, shows the last statement and flags journals with invalid or incomplete statements.
- [N-U12-119] Entries of bank transactions are marked as reviewed automatically in this edition, because no review rights are enforced.
- [N-U12-126] An online-payment extension adjusts a partial-amount step of the transaction line that does not exist in the base-edition code, which indicates reliance on a matching screen supplied elsewhere.

### CONSTRAINT

- [N-U12-108] A foreign currency on a transaction must differ from the journal currency, and a foreign amount and a foreign currency must be provided together.
- [N-U12-110] The entry of a transaction must always have exactly one line on the bank account and at most one suspense line; otherwise the change is refused.
- [N-U12-121] Fixed and percentage lines of a reconcile model cannot be zero, and a label pattern must be a valid expression.
- [N-U12-128] Statements and transaction lines are visible and editable only inside the user's allowed companies, and ordinary invoicing users can only read them; reconcile models are limited to the user's companies and their parents.

### RISK

- [N-U12-125] The studied base-edition code holds the reconcile model configuration but contains no engine that applies the models, no automatic reconciliation, no statement import and no bank matching screen; the practical use of the trigger setting is therefore unknown.
- [N-U12-227] The seeded bank fees preset may point to an unsuitable expense account when the chart has no account named for bank fees, because the fallback is the first expense account; the preset should be reviewed before use.

### UNKNOWN

- [N-U12-127] How an accountant matches a bank transaction with an invoice or a payment using only the base-edition code is not determined; no consumer of the candidate filter and no import module were found.
- [N-U12-130] The effect of the automated trigger on a reconcile model cannot be determined from the studied code.


## Capability 06 — Payment terms and early-payment discount

### WHAT

- [N-U12-131] A payment term defines when, and in how many parts, the amount of an invoice or bill falls due, and can optionally offer an early payment discount.

### WHY

- [N-U12-132] Terms make due dates, installments and discounted settlement computed consistently, so customers and vendors are shown the right amount at the right time.

### BUSINESS RULE

- [N-U12-133] A term has one or more lines. Each line is a percentage or a fixed amount, due after a number of days counted from the document date, from the end of the month, from the end of the next month, or on a given day of the following month. The last line always takes the remaining balance whatever its type.
- [N-U12-135] A new term starts with one line of one hundred percent due immediately. A newly added line defaults to thirty days after the previous line, and a new percentage line defaults to the remaining percentage.
- [N-U12-136] Due dates are computed from the document date, the end-of-month variants add the extra days after the month end, and the day-of-month variant moves to that day of the following month, with zero meaning the end of that month.
- [N-U12-137] Applying a term to a document generates one payment line per installment, merged per due date, with amounts in company and document currency. The document due date is the latest installment date. Without a term, the due date typed on the document is the only installment.
- [N-U12-138] Installment amounts are rounded per currency. With cash rounding every installment except the last is rounded and the last takes the rest, so the total does not change.
- [N-U12-139] The default term of a document comes from its partner: the customer term for sales documents and the vendor term for purchase documents, defined per company.
- [N-U12-140] An early payment discount grants a percentage (two percent by default) when payment is made within a number of days (ten by default) of the document date. It is allowed only on terms made of a single one-hundred-percent line, with a positive percentage and a positive number of days.
- [N-U12-141] The discount applies to the whole amount or only to the untaxed part according to the tax reduction setting: reduce taxes when the discount is taken, never reduce taxes, or always reduce taxes on the document itself. The country default is always for Belgium, never for the Netherlands and when taken for all others.
- [N-U12-142] Fixed-amount taxes are excluded from discount adjustments.
- [N-U12-143] A document is eligible for the discount when it is a customer or vendor invoice or receipt in the same currency as the payment, its term offers the discount, the payment date is not after the discount date and nothing has yet been matched against it.
- [N-U12-144] When the discount is taken during payment registration the difference is written off automatically: discount lines go to the company's discount loss account for customer documents or discount gain account for vendor documents, tax lines are adjusted only in the reduce-when-taken mode and only if the document has taxes, exchange differences go to the exchange accounts, and rounding is pushed onto the largest line.
- [N-U12-145] The next-payment information of a document offers the discounted amount with the days left, or the next or overdue installment, and the customer payment link carries the discount information.
- [N-U12-146] The date used to rank what to pay next is the discount date while the discount is still available, otherwise the due date.
- [N-U12-147] Installment dates and discount details are shown on the document only while it is not paid or only partly paid.
- [N-U12-155] Only the always-reduce mode changes the tax base of the document at invoicing; the reduce-when-taken mode adjusts tax only at payment time, and the never mode never adjusts tax.

### STATE

- [N-U12-153] A term itself has no workflow; installments become overdue by date, which is evaluated when amounts due are read.

### OPTIONALITY

- [N-U12-151] Terms can be copied, with a copy suffix on the name, and show a preview of installments for an example amount and date.

### DEPENDENCY

- [N-U12-148] Online payment transactions apply the early payment discount automatically when the amount paid equals the discounted amount.

### CONSTRAINT

- [N-U12-134] Percentage lines must sum to one hundred and each must be between zero and one hundred. A term needs at least one percentage line. The day-of-month value must be a number between zero and thirty-one.
- [N-U12-149] A payment term referenced by any document cannot be deleted; it must be archived instead.
- [N-U12-150] Terms are visible when they have no company or when their company is an allowed company or its parent; internal users and portal users can read them and only the accounting administrator can change them.

### RISK

- [N-U12-154] In the reduce-always mode the discount lines are created on the document and must stay consistent when taxes are later edited; behaviour after edits needs execution to confirm.

### UNKNOWN

- [N-U12-152] The rounding and tax-line distribution of the discount in the reduce-when-taken mode with several taxes or a foreign currency needs execution to confirm.


## Capability 07 — Check printing

### WHAT

- [N-U12-156] Check printing lets a company pay vendors by printed checks: a payment using the check method is numbered, printed on a layout, marked as sent, and can be voided.

### WHY

- [N-U12-157] Companies paying by paper check need controlled numbering, the amount in words, and a stub listing the paid bills, plus a way to void a spoiled check without losing the numbering trail.

### BUSINESS RULE

- [N-U12-158] The check method is an outgoing method available on bank journals and is added to the default outgoing methods of journals where it is available.
- [N-U12-159] Every journal has its own check numbering sequence without gaps, five digits wide, step one, created with the journal and, at installation, for existing bank journals.
- [N-U12-160] For pre-numbered paper checks, when the journal is not on manual numbering, the user is asked for the number printed on the first paper check, with the highest existing number plus one suggested, and the checks are numbered consecutively from it.
- [N-U12-161] For unnumbered paper checks, when the journal is on manual numbering, the journal sequence numbers each check when the payment is confirmed. The next number can be set on the journal, never lower than the current one and never above the maximum integer, and the padding follows the digits entered.
- [N-U12-163] Printing is allowed only for payments that use the check method and have not already been sent. Several checks printed together must belong to the same journal, and draft payments are confirmed first.
- [N-U12-164] Printing requires a check layout selected on the journal or the company; otherwise the user is redirected to the settings. Printing marks the payments as sent.
- [N-U12-165] A sent check that is still in process can be voided, which resets the payment to draft and then cancels it. A sent check can also be unmarked as sent.
- [N-U12-166] A check shows date, payee, amount, amount in words padded with asterisks, memo and a stub listing the paid bills and refunds. The stub is limited to nine lines unless multi-page stub is enabled, in which case it continues on extra pages that are marked void.
- [N-U12-167] The journal items of a check payment are labelled with the word Checks followed by the check number and the memo.

### OPTIONALITY

- [N-U12-168] The layout is a company setting with an optional per-journal override; page margins, the date label and the multi-page stub are also company settings.

### DEPENDENCY

- [N-U12-169] The base feature provides no layout, and no other part of the studied base-edition source adds one, so printing is blocked until an external layout extension is supplied.
- [N-U12-170] The journal dashboard shows how many in-process, unsent checks are waiting to be printed and links to their list.

### CONSTRAINT

- [N-U12-162] A check number consists of digits only, and the same number cannot be used twice in one journal among posted payments.
- [N-U12-171] The print action and the numbering helper are available to users with the full accounting role.

### RISK

- [N-U12-172] The suggested next number is the highest number found on any payment of the journal regardless of its state, so numbers of voided checks are never reused, and the next number cannot be moved backwards.

### UNKNOWN

- [N-U12-173] The rendering of the check and of its stub pages could not be determined in this study because no layout exists in the studied source.


## Capability 08 — Inter-company payments and payment-provider transaction framework

### WHAT

- [N-U12-174] Inter-company payment clearing lets a payment recorded in one company be applied to an invoice of another company of the same group, by creating clearing entries in both companies.
- [N-U12-181] The payment provider framework records every online or token payment attempt, and every capture, void or refund, as a transaction with provider, method, amount, currency, partner, state and reference, independent of any invoice or order.

### WHY

- [N-U12-175] When a customer pays one company for an invoice issued by a sister company, each company's books must still show the invoice settled and the money in the right company, with an inter-company balance between the two.
- [N-U12-182] A single transaction record gives a reliable audit trail and lets business documents react to confirmed payments after the provider reports the result.

### BUSINESS RULE

- [N-U12-176] When an invoice is posted and a payment from an online transaction, already in process or paid in another company, is waiting for it, the system creates a clearing entry in the payment's company and a settlement entry in the invoice's company.
- [N-U12-178] In the payment's company the clearing entry moves the amount from the partner's receivable or payable account to the inter-company account and is matched with the payment. In the invoice's company the settlement entry moves the amount between the inter-company account and the invoice's receivable or payable account and is matched with the invoice.
- [N-U12-184] Allowed transitions: pending from draft; authorized from draft or pending; confirmed from draft, pending, authorized or error; canceled from draft, pending or authorized; error from draft, pending or authorized. A request to enter the state already reached is ignored, and a request from a disallowed state is refused with a warning in the log.
- [N-U12-185] Every accepted state change records the message and the time of change and clears the post-processed flag so that the new state is processed again.
- [N-U12-188] Customer details such as name, language, email, address and phone are copied to the transaction at creation so that later changes to the partner do not alter the record.
- [N-U12-189] Data received from a provider is processed by finding the transaction by reference, checking that amount and currency match, applying the provider's updates, and creating a saved payment token if requested when the transaction is authorized or confirmed. A mismatch puts the transaction in error.
- [N-U12-190] Refunds and partial captures or voids create child transactions linked to the source. Refund amounts are negative. When the children account for the whole source amount, the source becomes confirmed, or canceled if all children were canceled.
- [N-U12-191] Capture and void apply only to authorized transactions and refunds only to confirmed ones. The provider must not be disabled. A provider error puts the child transaction in error with the provider's message.
- [N-U12-192] A token ties a partner to a saved payment method at a provider. Tokens are archived rather than deleted, cannot be unarchived when the provider is disabled or the method inactive, can never belong to the public partner, and a transaction cannot be created from an archived token. Archiving all tokens happens when a provider leaves the enabled or test states.
- [N-U12-194] After a final state a transaction is post-processed once, either when the customer's status page polls it or by a scheduled job running every ten minutes for transactions not yet processed within the last four days. Each transaction is committed separately, and failures are logged and rolled back.
- [N-U12-196] When a transaction is confirmed, linked draft invoices are posted, a payment is created and posted if none exists (except for validation transactions and for source transactions whose children are already final) and is matched with the linked invoices, and messages are logged on the invoice and payment. When a transaction is canceled, its payment is canceled.
- [N-U12-197] A payment created from a transaction uses the provider's journal and method, the commercial partner as customer, a positive amount with direction given by the sign, and early payment discount lines when the amount equals the discounted amount.
- [N-U12-198] A payment by saved token confirmed from the back office creates and charges a token transaction and posts the payment only if the transaction is confirmed; it cancels the payment if the transaction did not reach confirmed, pending or authorized.
- [N-U12-199] Customers can pay open customer invoices online only if the feature switch is on, the invoice is posted, unpaid or partly paid with an open amount, is an outgoing customer invoice, and has no pending transaction.
- [N-U12-201] Each provider is linked to a bank journal in which its successful transactions are posted and to a method line created for it. The journal of an active provider cannot be deleted, a method line linked to an enabled or test provider cannot be deleted, and uninstalling a provider is refused while payments with its method exist.
- [N-U12-202] A provider is disabled, enabled or in test mode. Disabling archives its tokens and deactivates methods supported only by disabled providers; enabling activates its default methods.
- [N-U12-207] Customer payment links carry a keyed signature of the amount, partner and currency and are refused when it does not match.

### STATE

- [N-U12-183] A transaction is draft, pending, authorized, confirmed, canceled or in error, and starts as draft.

### OPTIONALITY

- [N-U12-179] Inter-company clearing is optional and configured per company with a clearing journal and two clearing accounts; nothing happens when it is not configured.

### DEPENDENCY

- [N-U12-195] The scheduled post-processing job is switched on only while at least one provider is enabled or in test mode.

### CONSTRAINT

- [N-U12-177] Clearing applies only if the invoice is unpaid, partly paid or in payment, belongs to a different company than the payment, its company has a clearing journal, and both companies have the appropriate inter-company receivable or payable account; the payment must be in process or paid and its company must have a clearing journal.
- [N-U12-186] A transaction can be authorized only for providers that support manual capture.
- [N-U12-187] The transaction reference is unique. It is built from a given prefix, or from the documents involved, or from the time, and gets a numeric suffix when the prefix is already used; refunds and partial captures use dedicated prefixes.
- [N-U12-193] Paying with a token is refused if the commercial partner of the payer does not own the token.
- [N-U12-200] A refund is possible only for payments made through a provider and method that allow refunds, for a positive amount not above the amount still available, which is the payment amount minus refunds already made.
- [N-U12-203] Invoicing users can read, change and create transactions; administrators have full rights; employees can read methods and tokens; only administrators manage providers.
- [N-U12-204] Transactions and tokens are limited to the user's companies, ordinary users see only their own tokens, and invoicing users see all tokens.

### RISK

- [N-U12-205] Post-processing depends on either the customer's status page or the scheduled job; if neither runs, confirmed transactions remain unprocessed and no payment is created.

### UNKNOWN

- [N-U12-180] The behaviour of inter-company clearing with foreign currencies and partially paid invoices needs execution to confirm, and the feature is not configured in the studied database.
- [N-U12-206] Provider-specific behaviour such as webhooks and redirect forms was not studied.


## Capability 09 — Roles, record rules, data scope, exceptions and scheduled jobs

### WHAT

- [N-U12-208] Access to payments, statements, matching and payment terms is controlled by a small set of accounting roles, plus a separate permission to trust recipient bank accounts.

### WHY

- [N-U12-209] Invoicing staff handle documents and payments, accountants control statements, matching and configuration, and read-only auditors can only look, so that duties are separated.

### BUSINESS RULE

- [N-U12-210] There are five accounting roles: read-only, invoicing, basic accountant, full accountant and administrator. The basic role includes invoicing, the full role includes basic and read-only, and the administrator includes invoicing.
- [N-U12-211] The invoicing role can create, change and delete payments, register payments, and create and remove matches; the read-only role can only view payments and matches.
- [N-U12-212] Bank statements and transaction lines can only be viewed by the invoicing and read-only roles and are fully editable from the basic accountant role. Reconcile models are viewable by read-only users, viewable and creatable by invoicing users, and fully editable from the basic accountant role.
- [N-U12-213] Payment terms can be read by every internal user and by portal users, and only the accounting administrator can create, change or delete them.
- [N-U12-214] Every internal user can read payment methods and method lines; the invoicing role can change method lines and methods but cannot create methods.
- [N-U12-215] Trusting a recipient bank account requires a dedicated permission, held by system administrators by default; the automatic system user cannot trust accounts except during installation or tests. Untrusted accounts block payments by methods that require trust.
- [N-U12-216] Payments, statements, statement lines, transactions, tokens, providers, reconcile models and payment terms are limited to the user's allowed companies (and, for providers, models and terms, their parent companies), and these limits apply to every user regardless of role.
- [N-U12-217] Invoicing users see all journal entries and items inside their allowed companies regardless of who created them.
- [N-U12-219] Scheduled jobs relevant here are automatic posting of draft entries (daily), automatic sending of invoices (daily) and post-processing of provider transactions (every ten minutes, active only while a provider is enabled or in test). No job processes payments, statements or matching.
- [N-U12-220] No automation rules exist on payments, statements or matching in the configured database.
- [N-U12-221] Bulk actions are bound to lists: posting payments for invoicing users, unmatching items for full accountants and printing checks for full accountants.
- [N-U12-224] A catalogue of refusals protects each process: payment confirmation, registration, matching, statement entry, payment terms, check printing and provider transactions each refuse invalid states, missing configuration, mixed companies or accounts, and ownership violations with explicit errors.
- [N-U12-226] Ending a payment or matching through the reset and cancel buttons of payments is restricted by role in the screen: reset to draft belongs to the invoicing role, unmatching to full accountants.

### DEPENDENCY

- [N-U12-218] Sales, purchase and stock roles obtain additional read rights, or full rights for stock managers, on matches from their own applications; the sales role can also read payment terms.

### CONSTRAINT

- [N-U12-222] When a company enables the restrictive audit trail, entries that were posted once cannot be deleted and must be cancelled instead, which affects payments and bank transaction lines; the option is off in the studied database.

### RISK

- [N-U12-223] A role label in the access list can mislead: the Administrator label on a matching right comes from the stock manager role, not from an accounting administrator.

### UNKNOWN

- [N-U12-225] The membership of real users in these roles was not examined, since user data is outside the study scope.

