# U33 — Core Invoicing and Accounting Remainder — NEUTRAL KNOWLEDGE

> Source basis: Odoo 19 Community

> Status: DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION

> Clean-room layer: statements describe what the system must do and why, in generic business language. No file paths, class names or code appear here.

## Capability 01 — Bank transactions, statements and running balances

### WHAT

- [N-U33-001] A bank transaction line is stored as a posted journal entry that carries its own bank-specific attributes: label, partner, amount, optional foreign currency and amount, the statement it belongs to, and the payments that were generated while matching it.
- [N-U33-002] A bank statement is a grouping of transaction lines. It has no journal of its own (it takes it from its lines), a name made of the journal code and its date, and the date of its last posted line.
- [N-U33-003] The dashboard card of a bank, cash or credit-card journal summarises how many transactions wait to be matched, how many are still to be reviewed, how many miscellaneous postings sit on the bank account outside any statement, the outstanding payments not yet seen at the bank and the current balance.
- [N-U33-004] A periodic indicator counts, per journal type, the entries that need attention: drafts, posted entries not yet reviewed and posted bank entries without a matched transaction.

### WHY

- [N-U33-005] Transactions must be shown in the order in which they occurred at the bank. A single stored ordering key combining date, a reversed sequence number and identifier makes that ordering and the look-up of earlier lines cheap.
- [N-U33-006] A balance after each transaction lets the accountant compare the books with the bank report line by line without recomputing the whole history each time.

### BUSINESS RULE

- [N-U33-007] Creating a transaction always produces a miscellaneous entry that is posted immediately: one line on the bank account and one counterpart line on the suspense account (or on an explicitly chosen counterpart account). The journal may be inferred from the statement.
- [N-U33-008] The suspense account of the journal is mandatory for creating a transaction. The bank-side amount is expressed in the journal currency, the counterpart carries the opposite amount, and the company-currency amount is converted at the transaction date when currencies differ.
- [N-U33-009] The lines of the entry are classified as bank-account lines, suspense lines and other lines; when the bank account is not found by journal setting, cash-type and credit-card-type accounts are used instead.
- [N-U33-010] A foreign currency on a transaction must differ from the journal currency, and the foreign currency and the foreign amount must be given together. When no foreign amount is entered it is proposed from the exchange rate of the transaction date.
- [N-U33-011] A transaction counts as matched when what remains on its suspense line is zero (or when it has no suspense line). Until the entry has been marked as reviewed, the whole amount is treated as still open.
- [N-U33-012] The running balance starts from the starting balance of the latest statement at or before the line, adds only posted transactions, restarts at the first line of every statement, and covers the journal company and its child companies.
- [N-U33-013] A statement starting balance is the real ending balance of the previous statement plus any intervening posted transactions that belong to no statement; the computed ending balance adds the posted lines; the real ending balance can be typed in.
- [N-U33-014] A statement is complete when the computed and the real ending balances agree, and valid when its starting balance equals the real ending balance of the previous statement of the same journal (the first statement is always valid). A problem description explains which test fails.
- [N-U33-015] Changes made directly on the entry flow back to the transaction: label and partner from the bank-side line, amount from the bank-side line, and the foreign currency from the suspense line. The entry must keep exactly one bank-side line and at most one suspense line.
- [N-U33-016] Changes made on the transaction (label, amount, currencies, partner) rewrite the bank-side and suspense lines of the entry and delete every other line, so earlier matching on that entry is discarded.
- [N-U33-017] A transaction cannot be deleted from a valid and complete statement. Where the restrictive audit trail is enabled, deleting a transaction cancels its entry instead of removing it.
- [N-U33-018] Undoing a match removes the partial matches, deletes the payments generated for it and restores the two default lines. A reviewed and matched entry can be undone only by someone holding the review right, which in this edition is everyone.
- [N-U33-019] The bank's own implied exchange rates, derived from the amounts on the bank-side line, can be used to convert amounts into the transaction currency; they are read from the suspense line only when it is the sole counterpart.
- [N-U33-020] The set of candidate items offered for matching a transaction contains posted (optionally also partnered draft) items on reconcilable accounts, from the same or child companies, not already matched, not part of the transaction itself and, for receivable or payable accounts, not belonging to a payment.
- [N-U33-021] A new transaction defaults its journal to the first journal of the requested type and its date to that of the latest posted transaction (or its statement); the default statement is offered only while it is incomplete.
- [N-U33-022] A statement can be started from a selection of lines or from a split point: the selection must come from one journal and be contiguous, ignoring cancelled lines in between.
- [N-U33-023] Attachments added to a statement are linked to that statement.
- [N-U33-024] A system setting can stop the matching step from creating partner bank accounts automatically, leaving it to look up existing ones.
- [N-U33-025] The only bank-feed source offered is a placeholder meaning not yet defined; this edition provides no statement import or online synchronisation source.

### STATE

- [N-U33-026] A transaction moves between unmatched and matched according to the amount left on its suspense line; matched transactions can be returned to unmatched by undoing the match, and deleting is a separate end state restricted as described above.

### OPTIONALITY

- [N-U33-027] Automatic creation of bank accounts during matching is on by default and can be switched off by a system setting.

### DEPENDENCY

- [N-U33-028] The configured database holds no statements, transactions or entries; the observations here describe behaviour read from the rules, not recorded results.

### CONSTRAINT

- [N-U33-029] Statements are not workflow documents; they act as integrity checkpoints on the sequence of transactions, and the first statement of a journal has nothing to be checked against.

### RISK

- [N-U33-030] Writing attachments on several statements at once drops the attachment change silently.
- [N-U33-031] Editing a transaction that was already matched silently removes the matching lines from its entry, without warning.

### UNKNOWN

- [N-U33-032] The behaviour of the running balance with several statements per day, reordered or deleted lines, branch companies and multi-currency journals was not executed and remains to be confirmed in a test database.

## Capability 02 — Reconciliation presets and matching support

### WHAT

- [N-U33-033] A reconciliation preset describes the counterpart entries to propose when a bank transaction is matched. Each preset has a name, an order, an active flag, a trigger (manual or automated), and optional follow-up activity, and is tracked in the history.
- [N-U33-034] Applicability can be narrowed by journal, by amount (at most, at least, or between two bounds), by the transaction label (contains, does not contain, or a pattern) and by partner; leaving a condition empty means any.
- [N-U33-035] Each preset has one or more lines. A line may name an account, a partner, a label, taxes and an analytic distribution, and computes its amount as a fixed value, a percentage of the remaining balance, a percentage of the transaction, or a number extracted from the label by a pattern.
- [N-U33-036] Loading a chart of accounts creates two manual presets: one for internal transfers and one for bank fees recognised by a label containing the words bank fees.

### WHY

- [N-U33-037] Items created by a preset remember which preset created them, so that the preset can show the entries it has produced and so that its effect can be audited.

### BUSINESS RULE

- [N-U33-038] When the label condition is a pattern, it must be a valid pattern; otherwise the preset cannot be saved.
- [N-U33-039] The amount-type change handler also tests a value that this edition does not offer, which indicates a dead branch kept for an add-on that is not present.
- [N-U33-040] A preset with a label condition and a single line that names only a partner (no account) acts as a partner mapping for transactions whose label matches; such a preset is not proposed as an entry template.
- [N-U33-041] Duplicating a preset gives it a copy name, repeating the suffix until unique.
- [N-U33-042] A tax that is referenced by a preset line is regarded as in use.
- [N-U33-043] Reloading a chart of accounts leaves existing presets unchanged.
- [N-U33-044] The read-only accounting role can read presets; the invoicing role can read and create them; the basic accounting role has full access; presets are restricted to the user's companies and their ancestors.

### STATE

- [N-U33-045] A preset is either manual or automated; switching is by explicit buttons on the preset.

### OPTIONALITY

- [N-U33-046] Presets are reachable only through a link on bank journal cards for users with at least the basic accounting role; the whole preset concept is optional.

### DEPENDENCY

- [N-U33-047] Nothing in the studied source applies presets to transactions or offers a matching screen; a search of all Community modules finds only configuration, chart data for some countries, and demonstration data.

### CONSTRAINT

- [N-U33-048] Amounts must not be zero for fixed, balance-percentage and transaction-percentage lines, and a label-based amount must be a valid pattern.

### RISK

- [N-U33-049] The configured database holds two manual presets with a single full-percentage line each and no partner or pattern preset, so configuration would need review before any matching tool is introduced.

### UNKNOWN

- [N-U33-050] How the automated trigger and the label, amount and partner conditions are evaluated is not in the studied source and cannot be determined without an add-on or the web client implementation.

## Capability 03 — Duplicate, unusual-amount, unusual-date and credit warnings on documents

### WHAT

- [N-U33-051] Customer and vendor documents are checked for possible duplicates against other drafts and posted documents; other journal entries are never checked.
- [N-U33-052] Draft vendor documents with a non-zero total are compared with the vendor's history to flag an unusual amount or an unusually early invoice date.
- [N-U33-053] Draft customer invoices show a warning when the customer's total exposure would exceed the credit limit, if the company uses credit limits.
- [N-U33-054] A document shows a set of alerts: tax lock date and credit warnings for accounting users, informational notes for scheduled or recurring posting, a suggestion to remove empty lines on vendor bills, a note when sending is in progress, and the unusual-amount and unusual-date messages for everyone.

### WHY

- [N-U33-055] Users need to see immediately when the same bill or invoice may have been entered twice, and to tell a strict match from a loose one.
- [N-U33-056] Days sales outstanding gives credit control a simple indicator of how slowly a customer pays.

### BUSINESS RULE

- [N-U33-057] A candidate duplicate must be in the same company with the same document type and currency; it must share the same main partner, except that a document with no partner is compared with drafts of any partner.
- [N-U33-058] For customer documents a duplicate has the same partner, type and currency, the same total and the same invoice date; the reference is ignored.
- [N-U33-059] For vendor documents a duplicate is either the same reference (when a date is missing or both dates fall in the same calendar year) or a different reference with the same partner, the same non-zero total and the same invoice date.
- [N-U33-060] Documents that are being created or edited are compared using their current on-screen values rather than saved ones.
- [N-U33-061] Only duplicates the user is allowed to read are listed.
- [N-U33-062] A document is an exact duplicate when it is a vendor document and another document has the same non-empty reference, type, partner, date and total. The duplicate list is recomputed on screen when the identifying values change.
- [N-U33-063] An exact duplicate is shown as a red alert and other possible duplicates of drafts as a yellow warning; when a duplicate is a draft, the user can delete the duplicate or duplicates with one action.
- [N-U33-064] Automatic posting of bills from a trusted vendor is skipped, with a note, when a possible duplicate exists.
- [N-U33-065] The vendor history is the posted documents of the same partner, type, company and currency dated on or before the current one; statistics use the latest ten to thirty of them: the average and sample standard deviation of the gap in days between invoices and of the totals.
- [N-U33-066] With fewer than ten earlier documents there is not enough history and no unusual-pattern warning is raised.
- [N-U33-067] When the average gap is over 25 days the tolerance is widened by one day for month-length differences. The date warning appears only if the invoice arrives earlier than the average gap minus two deviations after the previous invoice; late invoices are never flagged.
- [N-U33-068] The amount warning appears when the total is outside the average plus or minus two deviations, higher or lower.
- [N-U33-069] Each vendor can be set, per company, to ignore the date check or the amount check.
- [N-U33-070] The confirmation step before posting appears only when the detection is explicitly switched on, which interactive posting buttons do; automated flows are never interrupted.
- [N-U33-071] In the confirmation step the user can choose to ignore future warnings for the vendor, post future-dated documents immediately and include documents of hashed journals; confirming posts the documents.
- [N-U33-072] Both unusual-pattern messages are shown to every user as warnings on the document.
- [N-U33-073] An unusual amount also stops automatic posting of a trusted vendor's bill; an unusual date does not.
- [N-U33-074] Exposure is the customer receivable balance, plus credit still to be invoiced (zero in this module and supplied by the sales module), plus the current document total. No limit, or exposure not above the limit, produces no message; the warning does not block posting.

### STATE

- [N-U33-075] A document is a potential duplicate, an exact duplicate or clear at any moment; this is derived, never stored, and changes as values are edited.

### OPTIONALITY

- [N-U33-076] Unusual-pattern detection can be switched off per vendor and per check, and by a context setting that is off by default for automated flows.
- [N-U33-077] The credit limit feature is optional per company; a customer limit differing from the company default activates a partner-specific limit.

### DEPENDENCY

- [N-U33-078] Credit still to be invoiced comes from the sales module; without it the exposure ignores confirmed but uninvoiced orders.

### CONSTRAINT

- [N-U33-079] Credit figures and limit switches are visible only to the invoicing and read-only accounting roles.

### RISK

- [N-U33-080] Deleting duplicates is a single action that removes every listed duplicate, so a wrong match could remove wanted documents.
- [N-U33-081] New or infrequent vendors with fewer than ten earlier documents are never checked, and amount tolerance is two sample deviations in both directions, so thin histories give weak protection.
- [N-U33-082] The configured company has the credit limit feature enabled with a default limit of zero, which means no effective limit.

### UNKNOWN

- [N-U33-083] The unusual-pattern warnings were not executed; the treatment of ties, mixed currencies and vendors with several companies needs a test with synthetic vendor history.

## Capability 04 — Quick encoding, review flag and trusted vendor auto-posting

### WHAT

- [N-U33-084] A company can switch on quick encoding for customer invoices, for vendor bills, or for both. It then applies to documents of sale or purchase journals accordingly.
- [N-U33-085] Posted entries carry a reviewed flag. It is set automatically for entries of miscellaneous journals and for entries posted by someone who has the review right (everyone in this edition), and can be set by a list action for accounting users.
- [N-U33-086] Vendors have an auto-post setting (always, ask after three validations without edits, or never). Bills created from uploaded or emailed documents for a vendor set to always are posted automatically.
- [N-U33-087] A Confirm Entries action posts selected drafts, asking for confirmation only for future-dated drafts or documents of journals whose entries are protected by a hash chain.
- [N-U33-088] A document can be switched between invoice and credit note while it still has no sequence number.
- [N-U33-089] A document's payment can be blocked or unblocked.

### WHY

- [N-U33-090] The accountant types the tax-included total and the system proposes one line, saving encoding time for simple documents.
- [N-U33-091] The quick encoding mode and the administrator role are allowed to delete numbered documents even when this leaves a gap in the number sequence.

### BUSINESS RULE

- [N-U33-092] The proposed line uses the account and taxes most used for that partner over the last two years (income accounts for customer documents, expense accounts for vendor documents); without history it uses the journal default account and its taxes, then the company default tax, mapped through the fiscal position.
- [N-U33-093] The frequency lookup counts the partner's journal items by account and tax set and takes the most common combination, ignoring access restrictions.
- [N-U33-094] With an early-payment discount computed in mixed mode and a single percentage tax, the untaxed price is derived from the typed total using the discounted tax factor; otherwise it is derived from the tax-included remainder.
- [N-U33-095] A line is created from the suggestion only when the total has been typed and the document has no lines.
- [N-U33-096] A rounding difference between the typed and the computed total is absorbed by adjusting the tax amount so that the document equals the typed total.
- [N-U33-097] The invoice date is suggested from the latest dated posted document of the journal and company, adjusted to respect lock dates, otherwise today.
- [N-U33-098] A document cannot be posted if the typed total differs from the computed total.
- [N-U33-099] Quick encoding relaxes number-sequence discipline: no out-of-order warning, no number reset on journal change, no ban on changing the journal of a numbered document, no date-versus-sequence check on posted documents, and deletion that would leave a gap is permitted.
- [N-U33-100] The trust question is asked only after posting one imported vendor bill whose vendor setting is ask, when the company has bill auto-posting on, the journal has no hash protection and the bill was not edited by hand; it appears after three consecutive unedited bills and offers always, ask later or never.
- [N-U33-101] Automatic posting is skipped when the company switch is off, the journal is hash-protected, or the document has an unusual-amount warning or a possible duplicate.
- [N-U33-102] A document counts as manually modified once it is changed by hand after creation; posting, import and mail-alias creation do not count as modification.
- [N-U33-103] The confirmation wizard defaults to the draft entries of the selection or of a journal that have lines, and raises an error when there is nothing to post.
- [N-U33-104] Switching type is refused for entries and for documents already posted once and numbered; for a negative total it flips the sign of product quantities.
- [N-U33-105] A paid document cannot be blocked; unblocking recomputes the payment status.
- [N-U33-106] Setting the reviewed flag or resetting a reviewed entry to draft requires the review right.

### STATE

- Not applicable: the reviewed flag and the blocked payment status are simple states described above; no further workflow exists.

### OPTIONALITY

- [N-U33-107] Quick encoding is off by default; the vendor auto-post setting defaults to ask and the company bill auto-posting switch defaults to on.

### DEPENDENCY

- [N-U33-108] The review right is always granted in this edition because a stricter rule would come from an enhanced accounting add-on that is not part of it.

- [N-U33-109] The configured company has no quick encoding mode, has bill auto-posting on, and every vendor has the auto-post setting populated; no document exists, so none of these flows has run.

### CONSTRAINT

- [N-U33-110] Quick encoding applies only to sale and purchase journals.

### RISK

- [N-U33-111] Because everyone holds the review right, the reviewed flag provides no segregation of duties in this edition.

### UNKNOWN

- [N-U33-112] The rounding adjustment, mixed discount derivation, frequent-account suggestion and the three-bills trust prompt were not executed and need a test with sample documents.

## Capability 05 — Adjusting entries, account transfers, renumbering and securing of entries

### WHAT

- [N-U33-113] Accounting users can select posted journal items and either shift them to another period (cut-off) or move them to another account; a preview shows what would be created before it is confirmed.
- [N-U33-114] Accounting administrators can renumber a set of entries of a single journal, either keeping the current order or ordering by accounting date.
- [N-U33-115] Accounting administrators can secure (seal with a verification code) all entries up to a chosen date; periods of a journal that still contain unmatched bank transactions are left out and reported.
- [N-U33-116] This edition has no deferral model of its own; deferral automation is not present, only the cut-off wizard described here and the accrual wizard covered elsewhere.

### WHY

- [N-U33-117] The cut-off wizard treats a credit-balance selection as revenue and a debit-balance selection as expense, so that the right accrued account carries the amount between periods.
- [N-U33-118] Securing helps prove that entries were not altered after a date; the wizard proposes the latest date up to which everything can be secured.

### BUSINESS RULE

- [N-U33-119] The wizard works only on journal items of posted entries that are not matched, all belonging to one company tree; the period shift is offered only when all selected items are on accounts of the same type.
- [N-U33-120] For a period shift the percentage must be above zero and at most one hundred; the shifted amount and the percentage drive each other, and the percentage is capped at one hundred.
- [N-U33-121] The accrued accounts and the journal chosen in the wizard are remembered as company defaults; the journal must be a miscellaneous journal.
- [N-U33-122] A period shift produces one entry at the new date plus, for each original accounting date, an entry that cancels the chosen share at the original date against the accrued account; all link back to the original documents.
- [N-U33-123] The chosen date must not fall in a locked period of any original entry, and original dates inside a lock period are moved to the first allowed date.
- [N-U33-124] Generated entries are posted at once; mirror lines on matchable accounts are matched with each other without exchange differences or cash-basis effects, and explanatory notes are left on the original and generated documents.
- [N-U33-125] An account transfer builds one entry that reverses each source line and posts the total to the destination account, grouped by partner and currency, with analytic distributions carried pro rata and currency converted when the destination account has its own currency; source and destination lines are matched when the accounts allow it.
- [N-U33-126] The preview lists at most four entries and states how many more would be created.
- [N-U33-127] New numbers are computed period by period according to the numbering pattern; only the last period starts at the first number typed by the user, and two proposals (by number and by date) are always prepared.
- [N-U33-128] Reordering by date is not allowed for hash-protected journals; numbers are blanked and flushed before being reassigned to avoid duplicate-name conflicts.
- [N-U33-129] The user is warned about draft entries before the date, entries that cannot be sealed, sequence gaps that sealing would create and entries after the chosen date that would also be sealed.
- [N-U33-130] Sealing requires a date and accepts gaps in the sequence.

### STATE

- Not applicable: the wizards are transient and create ordinary entries; the entries then follow their normal life cycle.

### OPTIONALITY

- [N-U33-131] In the configured database no accrued account or default adjusting journal is set and no entry exists; the two cut-off and transfer actions and the securing menu exist as configured.

### DEPENDENCY

- [N-U33-132] The securing wizard depends on the hash settings of journals, on lock dates and on bank transaction matching state.

### CONSTRAINT

- [N-U33-133] Renumbering is restricted to the accounting administrator.
- [N-U33-134] Securing is restricted to the accounting administrator.

### RISK

- [N-U33-135] Sealing is irreversible by design; sealing entries after the chosen date, or creating a gap in the sequence, cannot be undone by the user.

### UNKNOWN

- [N-U33-136] Multi-currency, analytic, partial-percentage and lock-date combinations in the wizards, and the hash results of sealing, were not executed.

## Capability 06 — Sending invoices by email or download

### WHAT

- [N-U33-137] Customer documents can be generated as official PDFs and sent by email or downloaded, one at a time through a dialog or in bulk through a background job; other modules call the same entry point.
- [N-U33-138] The single-document dialog lets the user pick the sending method, the invoice layout, the mail template, language, recipients, subject, body and attachments, save the text as a new template, and download the files when the manual method is used.
- [N-U33-139] The bulk dialog summarises how many documents go by each method and sends them in the background.
- [N-U33-140] A scheduled job runs daily and on demand; each run processes up to ten queued documents in date order and records progress.
- [N-U33-141] After a successful send, an optional list of subscribers on the journal is notified by email with a signed unsubscribe link.

### WHY

- [N-U33-142] The official invoice PDF is stored once and reused so that the legal document is the same every time it is sent or downloaded.

### BUSINESS RULE

- [N-U33-143] The default sending method comes from the customer's main partner and otherwise is email; the layout is the partner's preferred report, then the journal's preferred report, then the generic invoice report; if none is available sending fails. Extra electronic formats are not provided by this module.
- [N-U33-144] A queued run rebuilds its settings from data saved on the document when it was queued; mail content and the attachments widget are prepared only when email is selected.
- [N-U33-145] A customer without an email address is a warning in bulk mode and a blocking error in single mode; an archived sending job produces a bulk warning with a link for those allowed to open it; only error-level alerts block.
- [N-U33-146] Recipients come from the mail template (to, cc, partners) and document defaults, creating partners from bare addresses when needed, and are limited to those with an email address.
- [N-U33-147] Attachments are the invoice PDF, the template's dynamic reports other than the invoice itself, stored invoice attachments and the template's static attachments; stored and template attachments cannot be removed in the dialog.
- [N-U33-148] Only posted customer documents (invoices, credit notes, receipts) can be sent, and the chosen layout must be an invoice report available for the document.
- [N-U33-149] When generation fails, an optional fallback attaches a proforma PDF; otherwise the error stops an interactive send, or is written on the document and notified to the sender in the background; a failed background item is retried only when flagged.
- [N-U33-150] Steps before and after PDF rendering and before and after calling an external service are empty extension points; any external call belongs to add-on modules.
- [N-U33-151] An email is sent only when the partner has an address or recipients are given; its attachments are moved from the document to the message to avoid duplicates; the sender follows the template.
- [N-U33-152] The mail template depends on the document type (invoice, credit note, or the buyer-issued billing variants), and the invoice and credit-note templates cannot be deleted.
- [N-U33-153] Bulk sending is refused when the sending job is archived: administrators are redirected to the job, others get an error.
- [N-U33-154] Both dialogs are available to the invoicing role with full permissions.
- [N-U33-155] Downloading uses a route that checks read access and serves one file or a zip.

### STATE

- [N-U33-156] A document is queued for sending while it carries saved sending data; it becomes sent when its PDF is stored; resetting it to draft clears the queue and detaches the PDF.

### OPTIONALITY

- [N-U33-157] PDFs are rendered in batches of 80 by default, controlled by a system parameter; the fallback proforma option and the save-as-template option are optional.

### DEPENDENCY

- [N-U33-158] Electronic invoice formats, external services and outgoing mail servers are outside this module and are needed for those features to do anything.

### CONSTRAINT

- [N-U33-159] The sender, not the system, is recorded as author of the email; the job runs as the system user.

### RISK

- [N-U33-160] When the template uses default recipients, the copy address is read from the same value as the to address, which looks like an authoring slip and may confuse recipient selection.
- [N-U33-161] The configured database has the seven shipped templates and an active daily job, and nothing has been sent yet.

### UNKNOWN

- [N-U33-162] Mail delivery, outgoing server behaviour, rendering failures, push notifications and electronic format extensions were not executed.

## Capability 07 — Document import, customer portal, downloads, layout and protection of stored documents

### WHAT

- [N-U33-163] Uploaded or emailed files are turned into draft documents: one record per group of files, with the files attached and a note naming them, and the highest-priority decoder, if any, fills in the content. Without an electronic-invoice add-on the base module decodes nothing.
- [N-U33-164] An email sent to a journal address creates a draft document; the sender is matched to a partner (internal users forwarding a mail are looked through to the addresses in the body), the subject is placed as a heading in the body and the source address is kept.
- [N-U33-165] Files dropped on a dashboard create documents in the sale or purchase journal chosen from the context, and files added to an existing document trigger the same decoding for internal users.
- [N-U33-166] The customer portal lists the user's posted documents with sorting and filters for overdue items, shows each document on a page reachable by token or login, and offers the stored legal PDF (zipped with any electronic file) or a proforma PDF.
- [N-U33-167] Download routes serve one or several invoice files, or all attachments of selected entries, as a single file or a zip with duplicate names made unique.
- [N-U33-168] A public page shows the company terms when the terms feature is on and the terms are stored as a web page.
- [N-U33-169] The document layout dialog includes the company's QR option, VAT number and bank account number and marks the layout onboarding step as done.
- [N-U33-170] Invoice reports refuse to print plain journal entries; an original vendor bill report prints the stored original file with a banner.

### WHY

- [N-U33-171] Official invoice PDFs and electronic files, and the history of accounting records, must survive for audit; under a restrictive audit trail deletion is replaced by detaching and renaming, and edits are blocked.

### BUSINESS RULE

- [N-U33-172] Decoding runs between two database commits and is rolled back on failure; failures are logged and written in the document history instead of being raised, and a decoder may return a reason that is posted as a not-imported note.
- [N-U33-173] Files arriving by email are grouped so that several files of the same type create several documents while files of different types join one document, preferring the group with the most similar file name.
- [N-U33-174] XML files are parsed with entity resolution disabled and comments removed.
- [N-U33-175] Files embedded in a PDF are extracted recursively and treated as part of the same upload; a malformed PDF is logged.
- [N-U33-176] A portal user can read posted invoices and refunds of their main partner and its children, and their lines.
- [N-U33-177] Unsubscribing from journal notifications requires a signed token for the journal and address and a confirming submission; old unsigned links work only for authenticated users with write access.
- [N-U33-178] Under a restrictive audit trail, history notes on entries, on accounts used in entries, on taxes, on partners and on companies with entries cannot be deleted and their content, subject, type and subtype cannot be changed; the partner merge flow has a private bypass.

### STATE

- Not applicable: these services do not hold their own state beyond the documents they create.

### OPTIONALITY

- [N-U33-179] The configured database has six accounting report actions (one flagged as an invoice report), plain-text company terms, and the electronic-invoice and QR modules installed; there are no documents.

### DEPENDENCY

- [N-U33-180] The product catalog section routes operate on any record type named by the client and rely on ordinary access rights.
- [N-U33-181] A test-support route writes a system parameter under the caller's rights and so is effectively limited to administrators.

### CONSTRAINT

- [N-U33-182] Seven master accounting reports cannot be deleted because the PDF engine relies on them.

### RISK

- [N-U33-183] The portal controller lists receipts as well as invoices and refunds while the portal access rule covers only invoices and refunds, so a receipt listed in the portal may not be readable.
- [N-U33-184] Changing the bank number in the layout dialog rewrites the existing bank account and re-enables its permission for outgoing payments without a separate validation step.
- [N-U33-185] A QR code failure is hidden in the on-screen preview but stops the PDF from being produced.

### UNKNOWN

- [N-U33-186] Mail intake, decoder extensions of the electronic-invoice modules, portal tokens and QR failures were not executed.

## Capability 08 — Invoice analysis reporting and the absence of ledger and aging reports

### WHAT

- [N-U33-187] Invoice analysis is a read-only reporting dataset with one row per product line of every customer or vendor invoice, credit note and receipt, in any state (draft, posted or cancelled); it is computed when queried and has no stored table.
- [N-U33-188] Two analysis screens (customer invoices and vendor bills, each with graph and pivot views grouped by month) and five shipped saved filters (by salesperson, product, product category, credit note and country) present it, reachable from the Reporting menu and from journal cards.
- [N-U33-189] The Invoiced figure on a partner is the sum of the untaxed analysis amounts of posted customer invoices and credit notes for the partner and its contacts, in the company currency.
- [N-U33-190] Two print-report providers supply the invoice PDF templates with and without payment lines, including QR code addresses.
- [N-U33-191] A hash-integrity PDF report runs the company integrity check each time it is rendered.

### WHY

- [N-U33-192] A search of this source tree finds no partner ledger, aged receivable or aged payable report, and the only report definitions seeded are generic tax report definitions; the only reporting dataset owned by the module is the invoice analysis.

### BUSINESS RULE

- [N-U33-193] Quantities and amounts are signed: customer invoices count positive and vendor bills, vendor receipts and customer credit notes count negative.
- [N-U33-194] The company-currency untaxed amount is the negated line balance multiplied by the current rate of the currency table, while the amount including tax is converted at the document's own stored rate, so for foreign-currency documents the two company-currency measures may rest on different rate bases.
- [N-U33-195] The currency table covers the user's allowed companies: rate one when they share one currency, otherwise rates at today's date.
- [N-U33-196] An average price over a group is total untaxed amount divided by total quantity, not the average of row averages.
- [N-U33-197] Margin exists for customer documents only: untaxed amount minus quantity times the company cost of the product, sign-reversed for credit notes.
- [N-U33-198] Inventory value is quantity times unit ratio times company cost times the rate, with the opposite sign convention.
- [N-U33-199] Quantities are converted into the unit of the product record, which is also the unit shown.
- [N-U33-200] The main-partner column holds the line's partner and the partner column the document's partner; the country is the line partner's country, else the document's main partner's country.
- [N-U33-201] The read-only accounting, invoicing and administrator roles can read the analysis and nobody can write it; rows are limited to the user's allowed companies.

### STATE

- Not applicable: the dataset is derived and read-only.

### OPTIONALITY

- [N-U33-202] Which companies and currencies are included depends on the user's allowed companies selection.

### DEPENDENCY

- [N-U33-203] Costs come from the product cost per company; units from the unit table; rates from the currency table.

### CONSTRAINT

- [N-U33-204] No create, edit or delete is possible on analysis rows.

### RISK

- [N-U33-205] The configured database has no analysis rows and no stored object for it; five saved filters exist.

### UNKNOWN

- [N-U33-206] Rate-basis differences, margin with company-keyed costs and the temporary currency table were not executed.

## Capability 09 — Ledger groups, account groups, account code mapping and account merging

### WHAT

- [N-U33-207] A ledger group (shown as multi-ledger) is a named reporting filter with an optional company, a display order and a list of excluded journals; a ledger includes every journal of the company hierarchy that is not excluded. Names are unique per company, and entries can be filtered by ledger.
- [N-U33-208] An account group covers a range of account code prefixes of equal length, forms a hierarchy in which each group's parent is the most specific wider range, and classifies accounts by the longest matching prefix of their code for the company tree.
- [N-U33-209] The code mapping is a virtual list showing, for one account, one code per company; editing a row writes the account code for that company, and it can be reached only through the chart of accounts.
- [N-U33-210] The account root is a virtual two-character grouping of account codes used to group the chart of accounts, with parent-of relations by dropping the last character.
- [N-U33-211] The merge dialog combines several accounts into one: it groups candidates by type, trade or non-trade nature, currency, matchable flag and active flag (optionally also by name), excludes bank and cash accounts, re-points every reference to the survivor, merges translated names, deletes the others and gives the survivor the union of companies and codes. Unmerge splits a shared account back into one account per company.

### WHY

- [N-U33-212] After the direct deletion the registry cache is cleared so that stale identifier lookups for deleted accounts disappear.

### BUSINESS RULE

- [N-U33-213] Ledger groups are visible for companies that are empty or ancestors of the user's companies; invoicing and read-only roles read them, the administrator role manages them, and the menu is shown to the read-only accounting role.
- [N-U33-214] A new account proposes one code per company of the user; duplicating gives each company a fresh code by incrementing until free; uniqueness of codes across a company tree is verified after writes unless deferred during data loading.
- [N-U33-215] Two accounts of the same company cannot be merged, and only one account with sealed entries may be merged per group, which becomes the survivor so that sealed references stay valid; the generic record merge is disabled for accounts.
- [N-U33-216] Both merge dialog models are restricted to the accounting administrator.

### STATE

- Not applicable: groups, mappings and roots carry no workflow.

### OPTIONALITY

- [N-U33-217] The configured database has 147 accounts (32 matchable), no account groups and no ledger groups; the multi-ledger menu exists and no merge has been run.

### DEPENDENCY

- [N-U33-218] Account groups depend on the root company, and the group of an account depends on the company context in use because codes are company-specific.

### CONSTRAINT

- [N-U33-219] Groups of the same prefix length and company cannot overlap, and start and end prefixes must have the same length.

### RISK

- [N-U33-220] The virtual code mapping encodes the company in the identifier with a fixed offset of ten thousand, so company identifiers at or above that value would collide.
- [N-U33-221] The merge uses direct database updates and deletion, bypassing normal checks, and cannot be undone except by unmerge into separate accounts.

### UNKNOWN

- [N-U33-222] The direct-database merge and unmerge for company-dependent references, sealed entries and shared accounts across branches, and identifier collisions above ten thousand, were not executed.

## Capability 10 — Payment method framework

### WHAT

- [N-U33-223] A payment method is a named way of paying or being paid (inbound or outbound), unique per code and direction; creating a method that may be used several times automatically adds a method line to every compatible journal.
- [N-U33-224] A method line attaches a method to a journal with its own display name and an optional outstanding account; it is shown as its name followed by the journal name; a line used by any payment is detached from its journal rather than deleted.
- [N-U33-225] Partners can carry a default inbound and outbound method line per company, limited to active journals of the right direction in the company tree.

### WHY

- [N-U33-226] Other modules can filter the list of available lines, for instance to hide lines of inactive payment providers.

### BUSINESS RULE

- [N-U33-227] Each method module declares how its method may be used: once per company, once per company per provider, or any number of times, for which journal types, currencies and country. The base declares only the manual method; check printing is multi-use on bank journals; each payment provider except the neutral ones becomes a once-per-provider method on bank journals.
- [N-U33-228] A method may be restricted to journal types, to journals or companies in given currencies and to companies with a given fiscal country.
- [N-U33-229] On bank, cash and credit-card journals the available methods follow the usage rules; lines are recomputed when journal type or currency changes, keeping existing lines and adding missing default manual methods; other journal types have none.
- [N-U33-230] A journal cannot hold two lines of the same direction, method and name for once-only methods, and a once-per-company method cannot sit on two journals of one company.
- [N-U33-231] The outstanding account of a line must be a current asset or current liability account or the journal account; a helper can fill it from a chart template, but only the Moroccan and Indian templates call it, so the Thai chart leaves it empty and payments use company-level outstanding accounts.
- [N-U33-232] All internal users can read methods and lines; the invoicing role can write and delete methods (not create them) and has full access to lines.

### STATE

- Not applicable: methods and lines carry no workflow.

### OPTIONALITY

- [N-U33-233] Direct-debit methods belong to an add-on that is not part of this edition; the base only offers an empty hook.
- [N-U33-234] The deprecated helper that made a line's account matchable is retained but scheduled for removal.

### DEPENDENCY

- [N-U33-235] Provider-based methods depend on the payment module and on providers being configured.

### CONSTRAINT

- [N-U33-236] Deleting a method deletes its lines first.

### RISK

- [N-U33-237] The configured database has 25 methods but only three method lines, all manual or check on the bank journal and without an outstanding account, so no electronic method is usable until a provider is configured and linked.

### UNKNOWN

- [N-U33-238] Uniqueness behaviour when a provider is configured later, currency changes with existing lines and method creation by module installation were not executed.

## Capability 11 — Onboarding, setup dialogs, settings flow and chart loading

### WHAT

- [N-U33-239] The module ships one onboarding panel for the accounting dashboard with three steps (company data, fiscal periods, chart of accounts) plus two further steps, taxes and document layout, that are not part of any panel; an invoice onboarding that the code refers to does not exist in this edition, so the sales journal card shows none.
- [N-U33-240] Step completion rules: the layout step counts only when the company has a document layout; the company data step only when the company has a street address; the chart step opens the opening-balance list or, once an opening entry is posted, the normal account list.
- [N-U33-241] The fiscal period dialog stores the opening date and the fiscal year end on the company, validates the end day against a leap year, and moves a draft opening entry to the day before the opening date.
- [N-U33-242] The bank setup dialog creates a bank journal owned by the company with the next default code and an undefined statement source, or links the account to an existing unlinked journal, finding or creating the bank from a typed bank identifier.
- [N-U33-243] The settings screen loads a chosen chart template for the active company when saved and then starts onboardings; it blocks switching off cash-basis taxes while any tax is cash basis; it exposes toggles for modules that mostly do not exist in this edition; a button installs the EU one-stop-shop module immediately.
- [N-U33-244] Chart templates are discovered by introspecting chart modules; installing a chart module on a company without a chart loads the first template matching its country (or the generic chart), and uninstalling clears the chart of companies that used it.
- [N-U33-245] Creating a company with a country but no chart guesses and loads a chart template before commit, unless the generic chart applies.
- [N-U33-246] The periodic digest can include a revenue indicator (negative sum of income balances on posted items for the period), computed only for the invoicing role; two account tips are shipped.
- [N-U33-247] The legacy accounting groups are hidden from the user form unless they carry a privilege, and a helper can imply the inalterability group from the read-only and invoicing groups.

### WHY

- [N-U33-248] The sale-receipts setting is exported to the web client so the interface can show or hide receipts.

### BUSINESS RULE

- [N-U33-249] Onboarding progress is created per company only for the dashboard panel, after a chart template is loaded from the settings.
- [N-U33-250] The three company fields of the fiscal dialog are written together to satisfy the company constraint, avoiding the one-field-at-a-time problem of related fields.
- [N-U33-251] Changing a bank account code prefix rewrites the codes of the company's cash and credit-card accounts accordingly.

### STATE

- Not applicable: onboarding steps are simple done or not done markers.

### OPTIONALITY

- [N-U33-252] Sale receipts and many module toggles are optional settings.

### DEPENDENCY

- [N-U33-253] The panel depends on the onboarding module; document layout on the web module; digest on the digest module.

### CONSTRAINT

- [N-U33-254] The cash-basis setting cannot be disabled while cash-basis taxes exist.

### RISK

- [N-U33-255] A probable copy slip makes the bank statement digitization toggle depend on the invoice digitization module state.
- [N-U33-256] The configured database has one onboarding and five steps, one progress record, no invoice onboarding, and the digest with the revenue indicator on and two tips.

### UNKNOWN

- [N-U33-257] Panel rendering, chart auto-load at installation, immediate installation of the EU module and digest delivery were not executed.

## Capability 12 — Analytic accounting hooks inside invoicing

### WHAT

- [N-U33-258] Analytic accounts show a customer invoice counter and a vendor bill counter and buttons that open the related documents; the counters count posted journal items whose distribution names the account, while the buttons list documents.
- [N-U33-259] Analytic lines gain customer-invoice and vendor-bill categories, a financial account, journal and partner taken from the linked journal item, a derived profitability (loss, revenue or uncategorized) and a product-based pricing helper for manual lines.
- [N-U33-260] Plan applicability rules gain two business domains (invoice and vendor bill) and optional conditions on account code prefixes and product category, so a plan can be mandatory, optional or unavailable depending on the line being booked.
- [N-U33-261] Distribution models can be restricted by account code prefix, product and product category to propose a default analytic distribution on new lines.

### WHY

- [N-U33-262] Invoicing users must be able to maintain analytic lines and distribution models while accountants manage plans and accounts; read-only accountants can read everything analytic.

### BUSINESS RULE

- [N-U33-263] Each satisfied condition adds one point to an applicability and any condition that is set but not met rejects it; prefixes are separated by commas or semicolons.
- [N-U33-264] The prefix field is shown only for the general, invoice and vendor bill domains, with an example derived from an existing account code.
- [N-U33-265] A distribution model with a prefix applies only to lines whose account code starts with one of its prefixes; models without prefix apply to any account.
- [N-U33-266] An analytic line linked to a journal item must carry the same financial account as that item.
- [N-U33-267] Creating, editing or deleting analytic lines recomputes the analytic distribution of the affected journal items from the remaining lines.

### STATE

- Not applicable: analytic hooks hold no workflow state.

### OPTIONALITY

- [N-U33-268] Analytic accounting itself is an optional feature enabled by a group; the plans, models and lines in this capability exist only when it is used.

### DEPENDENCY

- [N-U33-269] These hooks depend on the analytic module that owns the base plans, accounts and lines, and on product costs for the manual pricing helper.

### CONSTRAINT

- [N-U33-270] Counters and buttons differ in scope: the counter counts posted items while the button lists documents without a posted filter, and the invoice button excludes receipts which the counter includes.

### RISK

- [N-U33-271] The configured database holds one plan, one account, two analytic lines and no applicabilities or distribution models, so none of these rules has been exercised.

### UNKNOWN

- [N-U33-272] Score ties between applicabilities, prefixes in multi-company charts and counter-versus-list differences were not executed.

## Capability 13 — Configuration inventory of the invoicing module: rights, rules, roles, menus, actions, scheduled jobs and shipped data

### WHAT

- [N-U33-273] The module ships 125 access rows; by area they cover entries and matching, bank and reconciliation, payments and terms, journals and accounts and groups, taxes and fiscal positions, the report engine, invoice analysis, analytic records, a few platform records and the wizards; all internal users can read the accounting reference data; the accounting administrator reads entries but fully manages configuration; the invoicing role has full access to entries, items, matches and payments.
- [N-U33-274] The module ships 31 record rules: company scoping for most records, all-records rules for invoicing and read-only roles on entries, items and send dialogs, rules for portal users, and a rule for billing officers on partner bank accounts.
- [N-U33-275] The module defines ten groups and two privileges: delivery address, read-only, invoicing, basic, full features, administrator, inalterability, cash rounding, partial purchase deductibility and validate bank account; with only invoicing installed just invoicing and administrator are meant to be used.
- [N-U33-276] The module declares 60 window actions, 12 server actions (14 in the database because each scheduled job generates one), 6 report actions and 53 menus, plus exactly two scheduled jobs: daily auto-posting of draft entries and daily sending of queued invoices.
- [N-U33-277] The top menu groups Dashboard, Customers, Vendors, Accounting, Review, Reporting and Configuration; the three report containers for partner, tax and statement reports are empty here because those reports belong to add-ons.
- [N-U33-278] Shipped data: 10 payment terms, 11 trade terms, 3 cash-flow tags, 3 message subtypes, 2 payment methods, 1 payment-term precision, 1 payment sequence, 7 mail templates, 5 saved filters, 2 digest tips, one onboarding with five steps and three generic tax report definitions.

### WHY

- [N-U33-279] The product name similarity threshold, seeded at 0.9, controls how close a product name must be to suggest a match.

### BUSINESS RULE

- [N-U33-280] All internal users can read accounts, taxes, tags, tax groups, repartition lines, fiscal positions, trade terms, payment terms, method lines and analytic accounts.
- [N-U33-281] Portal users can read entries and entry lines, restricted to their own posted documents by portal rules.
- [N-U33-282] The accounting administrator has full access to currencies and currency rates and to the report engine records.
- [N-U33-283] Entries and items have company rules plus all-records rules for invoicing and read-only roles; global rules combine by AND and group rules by OR, so the company rule stays the binding scope for normal users.
- [N-U33-284] Billing officers may access all partner bank accounts, overriding a restriction imposed by the employee module.
- [N-U33-285] The system and admin users belong to the administrator group by shipped data, and the validate-bank-account group is implied by the system administration group.
- [N-U33-286] The auto-post job runs at 02:00 daily from the next day and processes up to 100 entries per batch; sending runs daily as the system user.
- [N-U33-287] Securing of entries sits under Closing and the audit trail under Logs; partner, tax and legal statement report entries do not exist here.
- [N-U33-288] Settings require the system group, Configuration the administrator group, Tax Groups and trade terms need debug mode, cash roundings need their group, multi-ledger needs the read-only role, analytic menus need the analytic group, and no menu exists for reconciliation presets.
- [N-U33-289] Six system parameters are read by the module: product similarity threshold, skip bank-account creation on matching, name in footer, PDF batch size, show sale receipts and use invoice terms.
- [N-U33-290] The payment sequence has prefix PAY and padding five; real payment numbers come from the entry sequence.

### STATE

- Not applicable: this capability is an inventory.

### OPTIONALITY

- [N-U33-291] No automated action rule is defined by the module; the automation module is installed with zero rules.

### DEPENDENCY

- [N-U33-292] Shipped analytic menus and rules depend on the analytic module, partner bank rules on the employee module, and online payment menus on the payment module.

### CONSTRAINT

- [N-U33-293] Several rules carry misleading names (the invoicing all-records rule on entries is called Readonly Move); the effective rights follow the permission flags, not the name.

### RISK

- [N-U33-294] The restored database reports 84 models and 1932 fields owned by the module and 178 views (147 records plus 31 templates); every access row, rule, group, menu, action, job, template and data record checked matches the source by identifier.

### UNKNOWN

- [N-U33-295] The effective rights of real users and the combined effect of several record rules per user were not evaluated because user membership was not queried.
