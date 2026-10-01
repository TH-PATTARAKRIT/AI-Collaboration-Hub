# U11 — Journal entry, invoice and bill lifecycle — Neutral knowledge (Odoo 19 Community)
> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room layer: business and process statements only.
> Unit U11 — covers posting, validation, numbering and integrity protection, period locks, reversal, scheduled posting, line computation, journals, audit and access control, company scope.
> Each statement carries an identifier in square brackets that is linked to the restricted technical evidence file.

## CAP-U11-01 Entry lifecycle and state transitions

**WHAT**

- [N-U11-001] A journal entry, including customer invoices, vendor bills, credit notes and receipts, passes through three lifecycle states: draft, posted and cancelled.
- [N-U11-002] Invoices and bills carry a second, derived indicator describing payment progress, separate from the lifecycle state.
- [N-U11-003] Posting is the act that turns a prepared document into a ledger-affecting record: it assigns the official number, fixes the accounting date against period locks, creates analytic postings and starts the integrity protection where the journal requires it.

**WHY**

- [N-U11-004] The draft and posted split lets people prepare and review documents freely while guaranteeing that only validated documents change the books.

**BUSINESS RULE**

- [N-U11-005] New entries are always created as drafts; creating an entry directly in the posted state is refused.
- [N-U11-006] Only users holding the invoicing role, or the system itself running an automated process, may post entries.
- [N-U11-007] Only a draft entry can be posted; an entry that is already posted or cancelled cannot be posted again.
- [N-U11-008] An entry that contains no accounting line, other than titles or notes, cannot be posted.
- [N-U11-009] A manual post action posts at once, even when the accounting date lies in the future, unless the entry is flagged for automatic posting; an entry flagged for automatic posting with a future date cannot be posted manually without first being released from that flag.
- [N-U11-010] When posting is requested in the lenient (soft) mode, an entry dated in the future is not posted; it is flagged to be posted automatically on its accounting date and a note is logged on the document.
- [N-U11-011] Resetting to draft is allowed only from the posted or cancelled states, and is refused for entries needing a formal cancellation request, exchange-difference entries, tax cash-basis entries and entries protected by the integrity hash.
- [N-U11-012] Resetting to draft deletes the entry's analytic postings, deletes the next recurrence if it is still a draft, clears the pending-send marker and detaches stored printable documents of sales documents so that they can be regenerated.
- [N-U11-013] Cancelling a posted entry first resets it to draft, then removes its reconciliations, switches off automatic posting and sets the cancelled state; only drafts can be cancelled.
- [N-U11-014] Posting a customer or vendor document increases the commercial-relationship ranking counters of the partner, and a posted invoice with a zero total triggers the same follow-up as a fully paid invoice.

**STATE**

- [N-U11-015] Lifecycle: draft -> posted by posting; draft -> draft flagged for scheduled posting when soft-posting a future-dated entry; posted -> draft by reset; cancelled -> draft by reset; draft -> cancelled by cancel; posted -> cancelled only through an intermediate reset to draft.
- [N-U11-016] The payment indicator of an invoice is derived, never typed in: not paid, in payment, paid, partially paid or reversed, depending on reconciliation with payments, bank transactions and credit notes.
- [N-U11-017] A user may mark an unpaid invoice as blocked for payment and later unblock it; a paid or in-payment invoice cannot be blocked.
- [N-U11-018] Entries that are not invoices keep the indicator at not paid; a draft invoice with a non-zero total is also evaluated like a posted one.

**OPTIONALITY**

- [N-U11-019] The user interface asks for confirmation before posting entries that are future-dated or belong to a journal with integrity protection, and offers to force immediate posting.
- [N-U11-020] Warnings about unusual amounts or dates can interpose a confirmation step, but only when abnormal-document detection is explicitly switched on for the call.

**DEPENDENCY**

- [N-U11-021] Installed sales, purchasing, stock valuation, electronic-document, fleet, expense, timesheet, intercompany and e-mail modules each extend posting, reset or cancel with their own side effects, for example cost-of-sales lines, electronic-document records and vehicle service logs.

**CONSTRAINT**

- [N-U11-022] Resetting a reviewed entry to draft may be limited to users allowed to review; in a configuration with the base accounting application only, nobody is restricted.

**RISK**

- [N-U11-023] Because manual posting does not defer future-dated, unflagged entries, a document can be recorded ahead of its accounting date.
- [N-U11-024] The cancellation shortcut and the reset path remove reconciliations, so downstream payment and statement matching can be undone silently.

**UNKNOWN**

- [N-U11-025] Whether cancelling an entry leaves its already assigned number reserved in every numbering configuration needs observation on a running system.

## CAP-U11-02 Posting validation and the balance rule

**WHAT**

- [N-U11-026] Before an entry is saved or posted the system verifies that it is balanced, that its mandatory content is present, that its journal and type match, that currencies and taxes are coherent and that dates respect locks.

**WHY**

- [N-U11-027] These checks protect the double-entry invariant and the consistency of tax, currency and period reporting before any figure reaches the ledger.

**BUSINESS RULE**

- [N-U11-028] Every entry must balance: total debits equal total credits in company currency, rounded to the currency precision; an unbalanced entry is refused with a message naming the entries involved when several are affected.
- [N-U11-029] The balance check is applied whenever an entry or its lines are created, changed or deleted.
- [N-U11-030] For entries that involve taxes and are not yet posted, the system adds an automatic balancing line instead of refusing, so that such entries can be saved.
- [N-U11-031] A line may carry a debit or a credit but not both; the signs of the amount in the document currency and of the company-currency amount must agree; an accountable line must have an account; section, subsection and note lines must carry no amount and no account.
- [N-U11-032] A sales document must sit in a sales journal and a purchase document in a purchase journal.
- [N-U11-033] Taxes on the lines must be compatible with the fiscal country of the company or of the selected fiscal position.
- [N-U11-034] For invoices in a foreign currency the exchange rate must be strictly positive.
- [N-U11-035] A vendor document flagged for automatic posting must carry a bill date.
- [N-U11-036] At posting a customer invoice, vendor bill or receipt must not have a negative total, must have a partner, and vendor documents must have a bill date; a sales document without an invoice date receives today as its date.
- [N-U11-037] At posting the system refuses entries in archived journals, entries using archived accounts, archived analytic accounts or inactive currencies, entries using accounts of another company, and invoices whose recipient bank account is archived or, for company accounts, not trusted.
- [N-U11-038] All posting problems found on the selected entries are collected and reported together rather than one at a time.
- [N-U11-039] Entries using accounts of the off-balance category must use only such accounts, with no taxes and no reconciliation; sales documents may not use payable accounts and purchase documents may not use receivable accounts, and a line on a receivable or payable account must be the payment-term line.
- [N-U11-040] Two posted entries in the same journal may not share the same number.
- [N-U11-041] The accounting date of a posted entry and its number may not be edited into a locked period; editing a posted entry's date, partner, currency, fiscal position, lines or payment terms is refused.

**OPTIONALITY**

- [N-U11-042] The balance check can be suspended for a block of work by a processing switch, intended for programmatic flows that build entries in several steps.
- [N-U11-043] When the invoice quick-encoding mode is on, a posted invoice must match the total the user typed.

**DEPENDENCY**

- [N-U11-044] Tax coherence and currency rate rules rely on tax, fiscal-position and currency configuration owned by the taxation and currency capabilities.

**CONSTRAINT**

- [N-U11-045] The database itself enforces the line-level rules (one-sided amounts, sign agreement, mandatory account, empty section lines) and uniqueness of posted numbers per journal.

**RISK**

- [N-U11-046] A suspended balance check makes the safeguard depend entirely on the caller restoring balance; a software component that suspends it and fails midway can leave an unbalanced entry.
- [N-U11-047] Rules that evaluate dates and amounts on stored derived values may not see up-to-date figures in the middle of an update, so the balance test is deliberately computed directly from stored amounts.

**UNKNOWN**

- [N-U11-048] Behaviour of the balance check and of the automatic balancing line under concurrent edits and in multi-currency edge cases needs observation on a running system.

## CAP-U11-03 Numbering, sequences and inalterability

**WHAT**

- [N-U11-049] Every posted entry carries an official number built from a journal prefix, an optional year or month part and an increasing counter, and journals can additionally chain entries with a cryptographic fingerprint so later edits are detectable.

**WHY**

- [N-U11-050] Gap-free, ordered numbering and tamper evidence are legal and audit requirements in many jurisdictions and give auditors confidence that no document disappeared or was altered.

**BUSINESS RULE**

- [N-U11-051] A number is allocated only when the entry is posted; drafts do not consume numbers.
- [N-U11-052] Numbers follow the pattern of the previous entry in the same journal; the counter restarts monthly, yearly, per fiscal year, per fiscal year and month, or never, according to the pattern detected from the previous number.
- [N-U11-053] When there is no earlier number a starting pattern is generated: journal code, year, then month and a zero-padded counter; sales, bank, cash and card journals restart yearly and other journals monthly; a company with a non-calendar fiscal year uses a year-range style.
- [N-U11-054] Credit notes and payments receive their own prefix and counter when the journal is configured with dedicated sequences, and buyer-issued invoicing journals number per partner.
- [N-U11-055] Allocation of the next number is serialised against concurrent users: the system locks the candidate number through the uniqueness guarantee and retries with the next number if it is taken.
- [N-U11-056] The date of a posted entry must be consistent with the period embedded in its number; a mismatch is refused, and users are told to clear the number or resequence.
- [N-U11-057] Entries can be renumbered by an administrator with a resequence tool; renumbering by accounting date is refused for journals protected by the integrity hash.
- [N-U11-058] Changing the journal of an entry that has been posted once or has a real number is refused unless the number is cleared first, because it would open a gap.
- [N-U11-059] Deleting an entry that holds a number is allowed for ordinary users only if it is the last one of its chain; administrators and fiduciary-mode companies may delete with a warning.
- [N-U11-060] The system flags the first entry after a break in numbering, and journals show an irregularity indicator for gaps after the latest lock date.
- [N-U11-061] In a journal with integrity protection, posting fingerprints every not-yet-fingerprinted posted entry of the same numbering chain up to the one being posted, in numeric order, each fingerprint covering the previous one plus the number, date, journal, company and line amounts, accounts, labels and partners.
- [N-U11-062] Fingerprinting refuses to run across a gap in the numbering, across entries with unreconciled bank transactions, or when nothing is eligible.
- [N-U11-063] Once an entry is fingerprinted its protected fields and its lines cannot be edited or deleted, it cannot be reset to draft, and it cannot be deleted.
- [N-U11-064] Protection can be applied on demand to all unprotected posted entries up to a chosen date, including in journals that do not require it, and doing so reveals the inalterability features to invoicing and read-only users.
- [N-U11-065] Protection cannot be switched off on a journal that already contains fingerprinted entries.
- [N-U11-066] An integrity report recomputes the chain per journal and numbering prefix and reports corrupted entries; it is limited to users with the full accounting role.

**STATE**

- [N-U11-067] An entry is unprotected until fingerprinted; after fingerprinting it is permanently locked against change.

**OPTIONALITY**

- [N-U11-068] Integrity protection is a per-journal setting, off in the seeded configuration; a journal may also override the numbering pattern with a custom expression, after which only administrators may enter non-conforming numbers.

**DEPENDENCY**

- [N-U11-069] The numbering pattern depends on the company fiscal-year end and on the journal type and dedicated-sequence settings.

**CONSTRAINT**

- [N-U11-070] A numbering prefix used in a journal must match the period of the entry unless a historical cut-over date parameter exempts older entries.

**RISK**

- [N-U11-071] An older counter field for a gap-free sequence still exists on entries but is not populated by the current posting path; only legacy data or localization add-ons would use it.
- [N-U11-072] Allowing administrators to delete or renumber unprotected entries means numbering continuity relies on the integrity-protection setting for strong guarantees.

**UNKNOWN**

- [N-U11-073] The behaviour of numbering under heavy concurrent posting, and the exact output of the starting pattern for the local calendar and fiscal year configuration, require observation on a running system.

## CAP-U11-04 Period locks and lock exceptions

**WHAT**

- [N-U11-074] The company can set five period locks: a global lock, a tax-return lock, a sales lock, a purchase lock and a hard lock; each blocks or redirects accounting activity dated on or before the lock date.

**WHY**

- [N-U11-075] Locks freeze closed periods so reported figures, filed tax returns and issued statements cannot silently change.

**BUSINESS RULE**

- [N-U11-076] A global lock covers every journal; a sales lock covers sales journals; a purchase lock covers purchase journals; a tax-return lock covers only entries that affect the tax report; the hard lock covers everything and admits no exception.
- [N-U11-077] When an entry is posted with an accounting date inside a lock, the system does not reject it but moves its accounting date to the first open date after the lock, adjusted to the numbering period, and informs the user.
- [N-U11-078] Changing the date or number of an already posted entry, moving a posted entry back out of the posted state, or changing amounts, accounts, currencies, partners or journals on posted lines inside a locked period is refused with a message naming the locks.
- [N-U11-079] Changing taxes or tax-relevant amounts on posted lines, or creating or deleting lines that affect the tax report, inside a tax-return lock is refused because it would alter an issued return.
- [N-U11-080] A posted entry dated inside a lock cannot be deleted; an entry dated after the lock and not protected may be deleted when permitted.
- [N-U11-081] Copying or reversing an entry dated inside a lock proposes a date one day after the user's effective lock date.
- [N-U11-082] A lock exception temporarily relaxes one soft lock for one user or for everyone, for a stated reason and optionally until a given moment; the exception sets an earlier date for that lock only.
- [N-U11-083] Creating an exception is recorded on the company history with the old and new lock date, the beneficiary, expiry and reason; exceptions cannot be copied and can be revoked only by an administrator or the system.
- [N-U11-084] Every exception can show the audit trail of changes made during its validity to entries in the excepted period.
- [N-U11-085] When a lock date is changed on the company, all active exceptions on the changed lock are revoked and recreated against the new lock date.
- [N-U11-086] The hard lock date can only move forward, never be removed or reduced, and cannot be set while draft entries exist in the period; any global or hard lock requires that no unreconciled bank transactions remain in the period.
- [N-U11-087] A company inherits the locks of its parent companies; for the hard lock the latest date among the company and its parents applies, and for soft locks exceptions are evaluated per parent.

**STATE**

- [N-U11-088] Each soft lock is either unset, set to a date, or relaxed for a user by an active exception; an exception is active, expired or revoked.

**OPTIONALITY**

- [N-U11-089] All five lock dates are unset in the seeded configuration and no exception exists; the community application provides no screen of its own to maintain locks, so setting them requires a company record edit by a user with company administration rights.

**DEPENDENCY**

- [N-U11-090] Lock behaviour interacts with numbering periods, bank-transaction reconciliation, tax reporting and the integrity hash.

**CONSTRAINT**

- [N-U11-091] Soft locks and the global lock use the effective user date, so an exception for one user does not relax the lock for others.

**RISK**

- [N-U11-092] Because posting inside a lock silently moves the date rather than refusing, the recorded accounting date can differ from the document date and period-end reports may place the document in a later period than the user expects.
- [N-U11-093] Anyone allowed to edit the company record can set or lower soft locks; only the hard lock is protected against reduction, and exceptions can be created by any holder of the administrator role of the accounting application.

**UNKNOWN**

- [N-U11-094] No Community source was found that sets the tax-return lock automatically, although its help text says it is set when the tax closing entry is posted; that behaviour is likely supplied by an add-on application and needs confirmation.
- [N-U11-095] How the date shift interacts with the integrity hash and with branch companies in a live multi-company setup needs observation on a running system.

## CAP-U11-05 Reversal and credit notes

**WHAT**

- [N-U11-096] A posted entry is corrected by reversing it: the system creates an opposite entry, linked to the original, and for invoices produces a credit note; a customer credit note reverses an invoice and a vendor credit note reverses a bill.

**WHY**

- [N-U11-097] Posted entries cannot be edited, so reversal is the auditable way to cancel or correct a document while keeping history.

**BUSINESS RULE**

- [N-U11-098] Only posted entries can be reversed, and all selected entries must belong to one company; the reversal journal must have the same type as the original journal.
- [N-U11-099] The reversal takes a date, defaulting to today, a reason that is shown as the reference, the original origin document and, for invoices, an invoice date equal to the reversal date; if the reversal date is in the future the reversal is flagged for automatic posting.
- [N-U11-100] Creating a credit note from an invoice yields a draft credit note linked to the original, which the user may edit, for instance to credit only part of the amounts, before posting.
- [N-U11-101] Reversing a plain journal entry, or choosing the cancel-and-rebuild option, posts the reversal immediately and reconciles it with the original; the rebuild option then creates a fresh draft copy of the document's product lines for correction.
- [N-U11-102] When a draft reversal of a posted original is posted later, the reversal's reconcilable and bank lines are reconciled against the original automatically.
- [N-U11-103] For a plain journal entry the reversal flips the sign of every line; for a company using storno accounting the reversal marks lines as storno.
- [N-U11-104] A reversal dated inside a locked period is moved to the first date after the lock.
- [N-U11-105] When reversal is done with cancellation, existing reconciliations of the original are removed first so the original can be matched to its reversal.
- [N-U11-106] Reversal of an invoice releases links to expenses and quantities counted on sales orders, and posting a credit note linked to an invoice releases timesheet billing links, when those modules are installed.

**STATE**

- [N-U11-107] A reversed pair ends fully reconciled; the payment indicator of the original becomes reversed when it is settled only by credit notes.

**OPTIONALITY**

- [N-U11-108] The option to link a credit note to the original is not mandatory in the base configuration; it becomes mandatory only where a localization requires the origin reference.

**DEPENDENCY**

- [N-U11-109] Reversal relies on reconciliation behaviour owned by the payments capability and on lock dates and numbering.

**CONSTRAINT**

- [N-U11-110] The reversal wizard is available to the invoicing role; a reversal of a hash-protected entry creates a new entry and leaves the protected original untouched.

**RISK**

- [N-U11-111] A partial credit is only possible by editing the draft credit note; there is no amount field in the wizard, so partial credits depend on careful editing.
- [N-U11-112] A routine to delete or reverse entries chosen by lock and audit status exists but no caller was found in the community modules, so it may be intended for add-on applications.

**UNKNOWN**

- [N-U11-113] The exact reconciliation outcome for reversals of multi-currency entries and of tax cash-basis entries needs observation on a running system.

## CAP-U11-06 Automatic and recurring posting

**WHAT**

- [N-U11-114] Entries flagged for automatic posting are posted by a scheduled job once their accounting date has arrived; recurring entries create their next occurrence when they are posted.

**WHY**

- [N-U11-115] Scheduled posting lets users prepare future or recurring entries, such as accruals, rent or subscriptions, and rely on the system to post them on time.

**BUSINESS RULE**

- [N-U11-116] The daily job selects draft entries whose accounting date is today or earlier and whose automatic-posting option is not off, and posts them in batches.
- [N-U11-117] If any entry in a batch fails with a business error, the batch is rolled back and the entries are retried one by one; each failing entry gets a note with the reason and has automatic posting switched off so it is not retried every day.
- [N-U11-118] Posting an entry that recurs monthly, quarterly or yearly creates a draft copy dated at the next period, keeping the original day of month where possible and stopping after the stated end date; an existing next occurrence is not duplicated.
- [N-U11-119] Resetting a recurring entry to draft deletes the following occurrence if that one is still a draft.
- [N-U11-120] A vendor bill flagged for automatic posting must carry a bill date; an end date for recurrence is meaningful only for the recurring options and is cleared otherwise.
- [N-U11-121] A journal containing draft entries cannot be archived, and a hard lock cannot be set while drafts exist in the locked period, which forces scheduled drafts to be resolved first.
- [N-U11-122] Vendor bills created from captured documents are posted automatically only when the company and partner allow it, no unusual amount warning exists, no potential duplicate is found and the journal is not integrity-protected.

**STATE**

- [N-U11-123] An entry flagged for scheduled posting waits as a draft until its date, then becomes posted; a failure returns it to a normal draft with the flag off.

**OPTIONALITY**

- [N-U11-124] The scheduled job is active in the seeded configuration and runs daily with system privileges; the frequency is a configuration choice of the administrator.

**DEPENDENCY**

- [N-U11-125] Recurring and scheduled posting use the standard posting rules, so locks, numbering, validation and integrity protection apply as for manual posting.

**RISK**

- [N-U11-126] Only business errors are caught per entry; an unexpected technical error aborts the run for the whole batch and could stall later entries until fixed.
- [N-U11-127] The automatic-posting switch is turned off on failure, so a failed recurring entry silently stops its recurrence until a user intervenes.

**UNKNOWN**

- [N-U11-128] The behaviour of the job under concurrent manual posting, the effect of time zones on the selection date, and the progress-reporting behaviour of the scheduler need observation on a running system.

## CAP-U11-07 Entry-line computation and generated lines

**WHAT**

- [N-U11-129] An entry consists of lines; each line carries an account, a label, a partner, an amount in company currency (debit or credit), an amount in the line currency and a line type that tells what the line is for.

**WHY**

- [N-U11-130] Keeping the company-currency and document-currency amounts, and the debit and credit sides, synchronised guarantees consistent ledgers and reports in every currency.

**BUSINESS RULE**

- [N-U11-131] Line types are product, cost of goods sold, tax, discount, rounding, payment term, section, subsection, note, early-payment discount and three non-deductible types; only product and informational lines are typed in by users on invoices.
- [N-U11-132] The signed balance of a line is the master amount; debit and credit are derived from it, with the sides swapped for storno lines; typing a debit or credit sets the balance.
- [N-U11-133] Where the line currency equals the company currency the document-currency amount equals the balance; otherwise the amount in company currency is derived from the document-currency amount and the rate, rounded to currency precision, unless the user set it.
- [N-U11-134] For invoices the line currency follows the document currency and the rate comes from the document; for other entries the rate comes from the currency table at the invoice date or entry date.
- [N-U11-135] Whenever invoice lines, taxes, terms or amounts change, the system recomputes the dynamic lines in a fixed order: payment-term lines, automatic balancing line for entries, rounding line, discount lines, tax lines, non-deductible lines, early-payment-discount lines, and partner propagation.
- [N-U11-136] Dynamic lines are recomputed only when what is needed has changed; lines that already exist and are unchanged are left alone, and dynamic lines the user created manually are not overwritten.
- [N-U11-137] Dynamic lines cannot be deleted by hand while they are still required: a tax line cannot be removed while taxed lines exist and a receivable or payable line cannot be removed while payment terms need it.
- [N-U11-138] Lines of an invoice take the commercial partner of the document; changing the partner updates all lines.
- [N-U11-139] The label of the payment-term line follows the payment reference and the number of payment installments; the account of the payment-term line follows an existing term line, otherwise the partner or company receivable or payable setting, mapped through the fiscal position.

**OPTIONALITY**

- [N-U11-140] Section and note lines are display aids; they carry no amounts and can hide composition or prices on printed documents.

**DEPENDENCY**

- [N-U11-141] The detailed rules for tax lines and cash-rounding belong to the taxation capability, and the rules for payment-term lines and early-payment discounts to the payments capability.

**CONSTRAINT**

- [N-U11-142] The balance, debit, credit and document-currency amounts are validated by database rules so no application path can store an inconsistent line.

**RISK**

- [N-U11-143] Because many fields recompute one another, programmatic writes that set only one of the paired amounts rely on synchronisation hooks and may yield unexpected amounts if those hooks are suppressed.

**UNKNOWN**

- [N-U11-144] Rounding results for multi-currency invoices with taxes included in prices and cash rounding need observation with real data.

## CAP-U11-08 Journals

**WHAT**

- [N-U11-145] A journal is a numbered book of entries of one type: sales, purchase, cash, bank, credit card or miscellaneous; it carries a short code used as number prefix, default and suspense accounts and sequence and integrity settings.

**WHY**

- [N-U11-146] Journals separate document families so that each has its own numbering, default accounts, reporting and controls.

**BUSINESS RULE**

- [N-U11-147] The journal code is at most five characters and unique within a company.
- [N-U11-148] Sales documents may only be recorded in sales journals and purchase documents in purchase journals; payments and bank statements use bank, cash or credit card journals; other entries use miscellaneous journals; if no suitable journal exists, creation fails with an explanatory message.
- [N-U11-149] The default account of a sales or purchase journal must not be a receivable or payable account; accounts allowed as default depend on the journal type.
- [N-U11-150] A journal with draft entries cannot be archived, and an entry cannot be posted into an archived journal.
- [N-U11-151] A journal cannot be moved to another company once entries exist, and a bank journal's account holder must be the company.
- [N-U11-152] By default sales and purchase journals use a dedicated credit-note sequence, and bank, cash and card journals use a dedicated payment sequence.
- [N-U11-153] Integrity protection cannot be removed from a journal that has protected entries.
- [N-U11-154] A journal cannot be deleted while entries refer to it, because the link from entries to the journal is protected in the database.
- [N-U11-155] Copying a journal produces a new unique code and a name marked as a copy.
- [N-U11-156] Creating a bank journal can create its bank account and liquidity account automatically; default account and code are proposed when omitted.

**OPTIONALITY**

- [N-U11-157] A journal may carry a custom numbering expression, a currency, an e-mail alias for incoming documents, buyer-issued invoicing mode and a report template.

**DEPENDENCY**

- [N-U11-158] Journals depend on the chart of accounts, payment methods, bank accounts and the company; the seeded configuration has seven journals: sales, purchases, bank and four miscellaneous journals including exchange difference, cash basis taxes and inventory valuation.

**CONSTRAINT**

- [N-U11-159] Journal visibility follows the company hierarchy: users see journals of their companies and of parent companies.

**RISK**

- [N-U11-160] A journal's type drives which documents and accounts are acceptable, so changing configuration of journals after entries exist can strand historical numbering or account assumptions.

**UNKNOWN**

- [N-U11-161] How archiving interacts with scheduled entries that become due after archiving, and delete behaviour for journals without entries but with bank statements, need observation.

## CAP-U11-09 Audit trail, compliance and access control

**WHAT**

- [N-U11-162] The system records who changed what on entries, lines, journals and company lock settings, protects those records from deletion in the strict audit mode, and restricts access to entries and journals through roles, access rights and record rules.

**WHY**

- [N-U11-163] Auditors and regulators require traceable changes, non-deletable history and segregation between people who prepare, post and administer accounting data.

**BUSINESS RULE**

- [N-U11-164] Number, reference, date, state, type, partner, bank account, reviewed flag, payment reference, currency, untaxed amount, payment indicator, salesperson, origin and source e-mail of an entry are tracked in its history; account, label, taxes and balance of lines are tracked, and changes to lines of entries that were posted at least once are logged on the entry.
- [N-U11-165] When the strict audit trail option is on, an entry that has been posted once can only be cancelled, never deleted, and history messages about accounting records cannot be deleted or rewritten; history of draft entries can be removed.
- [N-U11-166] Lines of a posted entry with non-zero amounts cannot be deleted; lines of a protected entry can never be deleted.
- [N-U11-167] Deletion of a posted-once entry by privileged override is logged with user, amounts, accounts and partner.
- [N-U11-168] Entries can be marked as reviewed; only posted entries can be marked, and where an accountant role exists only accountants may mark or unmark them.
- [N-U11-169] The invoicing role may create, change and delete entries and lines; the administrator role inherits the invoicing role; the read-only role may only read; portal users see only posted invoices addressed to their own commercial partner; the lock exception list is readable by all internal users and creatable only by administrators.
- [N-U11-170] Entries and lines are visible only for the companies the user is allowed to work in; journals are visible for those companies and their parents.
- [N-U11-171] Other installed applications add narrower rules: sales users see their own customer invoices, purchase users see vendor documents, and expense approvers see expense documents.
- [N-U11-172] Changing the strict audit option off is refused where a localization forces it on; in the base configuration nothing forces it.

**STATE**

- [N-U11-173] The strict audit trail is off and no entries exist in the seeded configuration; ten groups, a hundred and twenty-five access rows and thirty-one record rules of the accounting application match the declared source.

**OPTIONALITY**

- [N-U11-174] The strict audit mode, integrity protection and reviewed flag are optional company or journal settings; the integrity features are hidden until used.

**DEPENDENCY**

- [N-U11-175] Role hierarchy differs depending on whether only invoicing, an enterprise accounting application or the full accountant application is present; the community base has invoicing and administrator in use and keeps accountant and read-only roles for compatibility.

**CONSTRAINT**

- [N-U11-176] Company record administration, which carries the lock settings, belongs to the general administration role, not to the accounting roles.

**RISK**

- [N-U11-177] Administrator override flags exist to delete protected records, and removal of history for draft entries is allowed, so the strict audit mode and integrity protection should both be enabled where evidential strength is required.
- [N-U11-178] No dedicated log of who read accounting data was found in the accounting application; read-access auditing, if needed, must come from platform or infrastructure logging.

**UNKNOWN**

- [N-U11-179] The exact visibility of tracked history to read-only roles, and the interplay of the sales and purchase record rules with the invoicing role when several rules apply to one user, need observation with role-based test users.

## CAP-U11-10 Company scope and entry creation from other business processes

**WHAT**

- [N-U11-180] Entries and journals belong to one company; the system keeps related records, accounts, partners and journals consistent with that company, supports branch companies and creates entries automatically from sales, purchasing, stock valuation, expenses, manufacturing, payments and bank statements.

**WHY**

- [N-U11-181] Multi-company isolation prevents cross-contamination of ledgers, and automatic entry creation keeps operational documents and accounting in step.

**BUSINESS RULE**

- [N-U11-182] An entry must have a company; it defaults from the journal company or the current company's first accessible branch, and cannot be left empty.
- [N-U11-183] Related records on an entry, such as journal, partner, bank account and fiscal position, must belong to the entry company or its family of companies; this is enforced by automatic company checks.
- [N-U11-184] Posting is refused if a line uses an account that does not belong to the entry's company or its parents.
- [N-U11-185] Locks, journal visibility and the hard lock date follow the company hierarchy, with the entries of branch companies being locked by their parent.
- [N-U11-186] Customers' payments made on an online transaction for an invoice of another company trigger an intercompany clearing entry between companies when intercompany accounts are configured.
- [N-U11-187] Sales orders produce customer invoices, purchase orders produce vendor bills, stock movements produce valuation entries, expense reports produce receipts and payment entries, manufacturing produces work-in-progress entries, payments produce payment entries and bank statement lines produce bank entries.
- [N-U11-188] Entries created automatically are subject to the same balance, locking, numbering and validation rules as manual ones, and some are created with elevated privileges so that salespeople or approvers need not hold accounting rights.
- [N-U11-189] Bills or invoices can also be created from uploaded documents, from e-mails received by a journal alias and from the opening-balance setup.

**OPTIONALITY**

- [N-U11-190] Intercompany clearing requires installation of the intercompany payment add-on and configuration of clearing accounts and journal on the companies.

**DEPENDENCY**

- [N-U11-191] Several modules outside this scope create entries; they are recorded as supporting modules and not analysed here.

**CONSTRAINT**

- [N-U11-192] Every entry creation path ends in the common entry creation, so the common numbering, balance and locking rules apply regardless of caller.

**RISK**

- [N-U11-193] Entries created in elevated mode bypass user-level access checks, so errors in those callers can create entries the initiating user could not have created.

**UNKNOWN**

- [N-U11-194] Whether record rules and company checks behave identically for users of branch companies in all menus needs observation with multi-company test users; the seeded database has one company.

