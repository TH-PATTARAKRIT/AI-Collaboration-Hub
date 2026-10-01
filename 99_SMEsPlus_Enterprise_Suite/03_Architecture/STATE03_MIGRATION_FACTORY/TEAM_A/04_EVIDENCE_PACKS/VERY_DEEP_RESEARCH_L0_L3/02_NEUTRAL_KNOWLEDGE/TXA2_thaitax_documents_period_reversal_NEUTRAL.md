# TXA2 — Tax documents, dates, periods, reversal and cross-module triggers — Neutral Knowledge

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Clean-room knowledge layer for Thai Tax Core unit TXA2 (study of Odoo 19 Community behaviour).
> Describes what a ledger system does with tax documents, dates, locks, corrections, numbering, access, audit and hand-offs from business events. It states system behaviour only; statutory requirements are validated elsewhere and nothing here is a legal conclusion.
> No V-level, no Complete, no coverage percentage, no Gate PASS.

## CAP-TXA2-01 Tax document types, states and issuing identity

### WHAT
- [N-TXA2-001] The ledger distinguishes seven kinds of journal document: ordinary journal entry, customer invoice, customer credit note, vendor bill, vendor credit note, sales receipt and purchase receipt. A debit note is not one of them in the studied configuration.
- [N-TXA2-002] Every document is in exactly one of three states: draft, posted or cancelled. Payment progress is a separate derived indicator that never changes the document state.

### WHY
- [N-TXA2-003] A single ledger document model covers entries, invoices, bills, credit notes and receipts so that every tax document is subject to the same posting, numbering, locking and audit rules.

### BUSINESS RULE
- [N-TXA2-004] A document is always created in draft; it can become posted only through the posting action, never by direct creation.
- [N-TXA2-005] A credit note is produced by reversing a posted customer invoice or vendor bill: the reversal creates an opposite document of the matching credit-note type linked back to the original. Receipts reverse to credit notes of the same side.
- [N-TXA2-006] Sales receipts are available only when a setting is on (it is on in the studied database); purchase receipts are always available. Receipts take the same taxes, journal type and posting flow as invoices and bills and, as inferred from the numbering logic, share the number series of the invoices of their journal.
- [N-TXA2-007] Posting enforces completeness: a customer on invoices, a date on vendor documents, a non-negative total, at least one non-note line, an active journal and accounts, and accounts that belong to the document company tree. Receipts are validated by the same routine but, as inferred from the validation logic, are not asked for a customer.

### STATE
- [N-TXA2-008] A posted or cancelled document can be reset to draft and a draft can be cancelled; cancelling a posted document first resets it. Reset is refused for secured (hashed) documents, exchange-difference and cash-basis entries and where a localization demands a cancellation request.
- [N-TXA2-009] Cancelling an invoice removes its reconciliations but does not cancel the payments that settled it; those payments stay posted and become unreconciled.

### OPTIONALITY
- [N-TXA2-010] Sales receipts, the dedicated credit-note number series, the abnormal-document confirmation and the debit-note module are all optional; none of them is switched on by the tax localization for Thailand.

### DEPENDENCY
- [N-TXA2-011] The kind of document decides the journal type that can hold it, the numbering series, the default taxes and the print layout.

### CONSTRAINT
- [N-TXA2-012] The kind of a document can be switched between invoice and credit note only while it has never been numbered; the same action is refused for ordinary entries.

### RISK
- [N-TXA2-013] Receipts and reset-to-draft carry weaker controls than invoices: no customer is required on receipts (inferred) and resetting a posted document to draft needs only the invoicing role.

### UNKNOWN
- [N-TXA2-014] Whether a sales receipt printed from the form shows any document title, and how receipts are counted in order invoicing quantities, cannot be settled without running the system.

## CAP-TXA2-02 Tax-relevant dates: invoice date, accounting date, due date, supply and delivery dates

### WHAT
- [N-TXA2-015] Four dates matter on a tax document: the document (invoice or bill) date, the accounting date that places the entry in a period, the payment due date, and optional supply and delivery dates. Only the first two drive posting, locks and tax reporting; the other two are informational.

### WHY
- [N-TXA2-016] Dates are derived by rule so that numbers keep increasing with time and each document lands in an identifiable period.

### BUSINESS RULE
- [N-TXA2-017] The accounting date of an invoice or receipt is derived from the invoice date, not typed independently; customer documents keep the invoice date until posting, while vendor documents are moved at entry time to a date that keeps the number series increasing.
- [N-TXA2-018] At posting, an empty invoice date on a customer document is set to today; a vendor document without a bill date is refused. After posting, the invoice date and the accounting date cannot be edited.
- [N-TXA2-019] A delivery date is copied onto customer invoices created from sales orders when the delivery module is installed (it is): it is the completion date of the first customer delivery of the order. It is shown and printed only when set and is not used for locks, numbering or the accounting date.
- [N-TXA2-020] The Thai localization neither overrides nor adds any date field, date default or date validation; Thai documents use the generic date logic.
- [N-TXA2-021] The due date follows the payment term; without a term it defaults to the later of the existing value and today.
- [N-TXA2-022] A draft whose date falls inside a locked period shows a warning stating that it will be accounted on a later date when posted.

### STATE
- [N-TXA2-023] The date fields are free while the document is in draft, are frozen at posting, and the accounting date can still move during posting if a lock is violated.

### OPTIONALITY
- [N-TXA2-024] Delivery and supply dates are optional, informational and only filled by a module or a person; no switch makes them drive the accounting date for Thailand.

### DEPENDENCY
- [N-TXA2-025] The date logic depends on the sequence pattern of the journal (monthly for vendor journals, yearly for customer journals by default), on company lock dates and, for foreign-currency documents, on the rate of the invoice date.

### CONSTRAINT
- [N-TXA2-026] A vendor bill needs a bill date to be posted, a posted document cannot change its dates, and a number that no longer matches the date blocks re-posting until the number is cleared.

### RISK
- [N-TXA2-027] Two different dates can exist on a posted customer invoice (printed invoice date and ledger date) after a lock shift, and a vendor bill dated earlier in the current period is accounted on the posting day rather than on the bill date; any statutory tax-point rule must be checked against these defaults.

### UNKNOWN
- [N-TXA2-028] Which date is the statutory tax point for Thailand, and whether the generic defaults satisfy it, is a statutory question for the statutory lane; the exact accounting date chosen for each lock and numbering combination needs execution.

## CAP-TXA2-03 Lock dates, tax lock, cut-off and the absence of a tax-period object

### WHAT
- [N-TXA2-029] Five company-level lock dates freeze closed periods: a global (fiscal year) lock, a tax-return lock, a sales lock, a purchase lock and an irreversible hard lock. There is no period or tax-return object; a period is only a date range chosen when a report is run.

### WHY
- [N-TXA2-030] Locks exist so that closed periods, and tax statements already issued, are not silently changed; postponement keeps documents recordable.

### BUSINESS RULE
- [N-TXA2-031] Posting inside a locked period does not fail: the entry date is moved to the first date that no applicable lock blocks, and posting continues. This applies equally to documents created from other modules and to valuation and closing entries.
- [N-TXA2-032] Which locks apply depends on the document: the global and hard locks always; the sales lock only on customer journals; the purchase lock only on vendor journals; the tax lock only when the document touches the tax report.
- [N-TXA2-033] Editing an already posted document inside a locked period is refused: changing its date or number, resetting it to draft, changing amounts, accounts, partner or taxes, deleting its lines. The tax lock additionally protects every item that affects the tax report, even when the global lock is open.
- [N-TXA2-034] A soft lock can be relaxed for one user or for everyone by a time-limited, audited exception created by an accounting administrator and revocable by an administrator. The hard lock cannot be relaxed and cannot be lowered or removed.
- [N-TXA2-035] Copies and reversals of documents dated inside a fiscal lock are dated on the day after the user's fiscal lock; reversal of cash-basis and exchange entries when payments are undone keeps the original period unless it is locked.
- [N-TXA2-036] The tax lock date is not set by any Community routine: its help text says it is set automatically when a tax closing entry is posted, but no tax closing entry or tax return object exists in Community, so no automatic maintenance exists and no menu or setting for maintaining it was found.

### STATE
- [N-TXA2-037] A period is open until a lock date covers it; a locked period reopens for chosen users through an exception unless the hard lock covers it.

### OPTIONALITY
- [N-TXA2-038] All locks and exceptions are optional; the Thai localization sets none and the studied database has none set. The stock-valuation closing period and the audit-trail mode are separate company options.

### DEPENDENCY
- [N-TXA2-039] Locks interact with numbering (the shifted date can open a new number period), bank statement reconciliation, the hash chain and every module that creates entries; branch companies inherit the locks of their parents.

### CONSTRAINT
- [N-TXA2-040] Setting a hard lock requires that no draft document and no unreconciled bank line remains in the period; a lock never shifts a document at editing time, only at posting.

### RISK
- [N-TXA2-041] Postponing instead of refusing means a late document silently lands in a later period, which changes the tax period of its tax lines; the tax lock help text overpromises automation that does not exist; without an in-product way to maintain locks or exceptions they depend on technical access.

### UNKNOWN
- [N-TXA2-042] Whether the tax lock date can or should be maintained by users for Thailand, the exact date chosen when several locks overlap, and the effect of a shifted date on numbering, hash chains and period reports need execution and the statutory lane.

## CAP-TXA2-04 Correction of posted tax documents: reset, cancel, reverse, re-issue, copy and debit note

### WHAT
- [N-TXA2-043] To correct a posted tax document the base offers: reset to draft and edit, cancel, reverse into a credit note (optionally cancelling the original immediately and opening a new draft copy), duplicate, and, only with an optional module, a debit note. There is no native 'replacement' or 're-issued document' concept linking a new document to the one it replaces.

### WHY
- [N-TXA2-044] Corrections are made by new documents or controlled resets so that history stays traceable.

### BUSINESS RULE
- [N-TXA2-045] Resetting a posted document to draft keeps its number; the document can be edited and posted again with the same number. Reset is refused for secured documents, in a locked period and where a localization requires a cancellation request. No guard was found that refuses reset because the document is paid (inferred; to be confirmed by execution).
- [N-TXA2-046] Cancelling takes a document out of the ledger but keeps its number; cancelled documents can be reset to draft again.
- [N-TXA2-047] The reversal wizard has two buttons: 'Reverse', which creates a draft credit note to be edited and posted (partial credit by editing its lines), and 'Reverse and Create Invoice', which posts the credit note at once, reconciles it with the original and opens a new draft copy of the original lines.
- [N-TXA2-048] An invoice or bill that comes out negative when created from an order can be turned into a credit note, but only before it has ever been numbered.
- [N-TXA2-049] Duplicating a posted document creates a new draft with no link to the original and a new number at posting.
- [N-TXA2-050] A debit note, an upward correction linked to the corrected document, exists only in an optional module that is not installed: it copies a posted invoice or credit note into a new draft invoice of the matching direction, links it to the origin, and gives it its own number series with a distinguishing prefix.

### STATE
- [N-TXA2-051] Correction paths map to states as follows: a posted document goes back to draft by reset, becomes cancelled by cancel, or stays posted while an opposite credit note is created; a hashed document can only use the credit-note path.

### OPTIONALITY
- [N-TXA2-052] The abnormal-document warning, the cancel-request hook, the debit-note module and the dedicated credit-note series are optional; the immediate-cancel reversal needs a reversal date that is not in the future.

### DEPENDENCY
- [N-TXA2-053] Corrections depend on lock dates, the hash option, reconciliation state of the document, and on the order, purchase and stock links that must be unwound separately.
- [N-TXA2-054] Installed modules extend posting, resetting, cancelling and reversing with side effects on orders, timesheets, expenses, electronic documents, cost lines, emails and vehicle logs; none of these side effects is specific to Thailand.

### CONSTRAINT
- [N-TXA2-055] Only posted documents can be reversed, all documents of one reversal must share a company, the reversal journal must be of the same type as the original, and a posted document cannot be deleted before it is reset to draft.

### RISK
- [N-TXA2-056] Without a replacement link, an auditor cannot navigate from a cancelled tax document to the one that replaced it except through the number reuse, chatter and references; reset-to-draft and re-posting keeps the same number, which hides the correction unless the audit trail is read.

### UNKNOWN
- [N-TXA2-057] The effect of resetting a paid document, of cancelling a cash-basis-tax document and of reversing multi-currency originals needs execution; whether Thai practice needs a replacement concept is a statutory question.

## CAP-TXA2-05 Numbering, sequences, gaps and inalterability of tax documents

### WHAT
- [N-TXA2-058] Numbers are assigned when a document is posted, per journal, by a pattern deduced from the previous number of the same journal. Optional per-journal hashing makes posted documents tamper-evident. There is no configurable sequence object for documents in Community.

### WHY
- [N-TXA2-059] Continuous numbering and optional tamper evidence let a reviewer detect missing or altered documents.

### BUSINESS RULE
- [N-TXA2-060] Customer and vendor journals keep invoices and credit notes in separate series by default; bank journals keep payments in a separate series. Self-billing journals number per partner. Receipts and invoices share one series.
- [N-TXA2-061] The numbering period (monthly, yearly, year-range or never) is deduced from the previous number; the sequence resets accordingly and a posted number must agree with its date.
- [N-TXA2-062] A number is never given to another document after posting, so cancelling or deleting a numbered document, or leaving it in draft, leaves an irregularity that the system flags; ordinary users cannot delete a numbered document that is not the last of its series.
- [N-TXA2-063] A journal can be set to secure posted entries with a hash chain: when an entry is posted, all earlier unhashed entries of its chain are hashed. A hashed entry can no longer be reset, cancelled, deleted or altered in its integrity fields. The hash covers number, date, journal, company and, per line, label, amounts, account and partner; it does not cover taxes, tax tags, invoice date or document type.
- [N-TXA2-064] A journal can carry a custom number format expression; non-administrators must then respect it when typing a number.

### STATE
- [N-TXA2-065] A document has no number in draft, receives it at its first posting, keeps it through reset, cancellation and reposting, and may additionally become secured.

### OPTIONALITY
- [N-TXA2-066] Dedicated credit-note and payment series, billing on behalf of the vendor, the regex override and the hash option are per-journal options; none of them is enabled by the Thai localization, and the studied database has only the default credit-note and payment series.

### DEPENDENCY
- [N-TXA2-067] Numbering depends on the accounting date, which depends on locks and the invoice date; and on the company fiscal-year end for staggered years.

### CONSTRAINT
- [N-TXA2-068] Numbers are unique among posted documents of a journal; a posted number must agree with its date; documents cannot move to another journal after numbering without clearing the number.

### RISK
- [N-TXA2-069] Because the hash omits taxes, tags and invoice date, a secured document can still have its tax classification touched by tools that bypass the normal record checks; the statutory Thai tax-invoice numbering rules (continuity, per-branch or per-point-of-sale series, separate series by document type) are not modelled and must be validated separately.

### UNKNOWN
- [N-TXA2-070] The first number generated for a Thai company's journals and the exact reuse behaviour after cancellation need execution; statutory numbering requirements belong to the statutory lane.

## CAP-TXA2-06 Tax journal entries: tax lines, tags, cash basis, withholding, reversal and re-tagging

### WHAT
- [N-TXA2-071] Tax lines and their tax-report tags are created while a document is in draft, are frozen when it is posted, and are changed afterwards only by reversal or by an optional administrator tool. Posting itself does not create tax lines. Payments create tax lines only for cash-basis taxes and for the optional payment-time withholding module.

### WHY
- [N-TXA2-072] Tags on tax lines are what places each amount in the tax report; freezing them at posting makes reports reproducible.

### BUSINESS RULE
- [N-TXA2-073] Each tax line and each taxed base line receives the tax-report tags of the tax distribution that matches the document (invoice or credit note); tags are taken only when the tax is due on the invoice or cash-basis tags are requested.
- [N-TXA2-074] Once posted, a tax line cannot be changed or deleted by hand; changing taxes needs a reset to draft (refused in a locked period) or a reversal.
- [N-TXA2-075] Cash-basis taxes are an optional per-tax mode: the tax sits on a transition account until the document is reconciled with a payment, when a cash-basis entry moves it to the real tax account and keeps the tax base. They are not used by any Thai tax in the studied configuration.
- [N-TXA2-076] An optional module, not installed here, lets withholding be registered at payment: the withholding tax then ignores document computation and is booked on the payment entry as a withholding line with a mandatory withholding number, a base pair and a reduced cash amount.
- [N-TXA2-077] Reversal of a taxed document recomputes tax lines with the credit-note distribution of the same taxes; reversal of an ordinary entry with taxes negates amounts directly. Reversal does not copy stock or cost-of-sales lines unless it is the cancelling reversal.
- [N-TXA2-078] An optional administrator tool, not installed here, rewrites the tax-report tags on existing journal items from a chosen date so that they match the current tax configuration. It is irreversible, bypasses the normal write checks and the lock dates, leaves no log, and refuses configurations where a child tax has several parents.

### STATE
- [N-TXA2-079] Tax lines go through: created in draft, fixed at posting, mirrored by the credit note, moved at reconciliation (cash-basis only), re-tagged by the optional tool.

### OPTIONALITY
- [N-TXA2-080] Cash basis, payment-time withholding and the re-tagging tool are all optional; the Thai localization uses ordinary negative-percentage taxes booked at posting for withholding.

### DEPENDENCY
- [N-TXA2-081] Tax lines depend on the taxes of the lines (product, account or fiscal position), the repartition configuration, the price-included setting, rounding and currency rate, and the lock dates.

### CONSTRAINT
- [N-TXA2-082] A posted item cannot change taxes; a tax line cannot be deleted by hand; cash-basis taxes need a reconcilable transition account; payment-time withholding needs a positive base and a number.

### RISK
- [N-TXA2-083] The re-tagging tool and any direct database change alter tax history without trace; withholding booked at posting is recognised before payment; no tax closing entry exists to settle the tax accounts.

### UNKNOWN
- [N-TXA2-084] Numeric tax results with rounding and currency, tag polarity on credit notes, and behaviour of cash-basis entries on reversal need execution; whether bank-statement reconciliation models can add taxed lines is not read.

## CAP-TXA2-07 Multi-company isolation, access groups and record rules for tax and fiscal records

### WHAT
- [N-TXA2-085] Tax and fiscal configuration and documents are isolated by company: documents by the company of their journal, configuration records by the company tree, so a branch may use the configuration of its parent. Access is split between an invoicing role, an administrator role, read-only roles and operational roles in sales and purchasing.

### WHY
- [N-TXA2-086] Roles and company boundaries limit who can create, post, correct and configure tax records.

### BUSINESS RULE
- [N-TXA2-087] With the accounting application alone only two roles are meant to be used: Invoicing (create, edit, post, pay) and Administrator (configuration and exceptions); the other accounting groups give shallow read access.
- [N-TXA2-088] Record rules narrow what operational roles see: salespeople see only customer invoices and credit notes (their own unless they have the all-leads right), purchasing users only vendor documents (including purchase receipts), invoicing users everything, portal users their own non-draft invoices and bills but not receipts.
- [N-TXA2-089] Posting needs the invoicing role, but reset to draft and cancel carry no role check in code, only in the view; documents created from sales orders are created with elevated rights so that a salesperson need not hold the invoicing role.
- [N-TXA2-090] Community contains no automatic inter-company invoice or order mirroring; the only inter-company mechanism found is the payment-clearing add-on, which posts clearing entries when a payment taken by one company settles an invoice of another.

### STATE
- [N-TXA2-091] Not applicable as a state machine; visibility changes with company selection, role and record-rule combination.

### OPTIONALITY
- [N-TXA2-092] Multi-company behaviour exists only when more than one company or branch is configured; the studied database has one company.

### DEPENDENCY
- [N-TXA2-093] Lock dates and exceptions are inherited down the branch tree; tax and journal configuration is shared up the tree; sequences are per journal and hence per company.

### CONSTRAINT
- [N-TXA2-094] A document, its journal, accounts, fiscal position and taxes must belong to the same company tree; accounts of another tree block posting.

### RISK
- [N-TXA2-095] Several additive record rules apply to one user (invoicing see-all plus sales or purchase rules); a role with no read rule for receipts (sales) may not see them; segregation between creating, posting, resetting and cancelling documents is weak because only posting is enforced in code.

### UNKNOWN
- [N-TXA2-096] Effective visibility for users holding several roles, branch and parent behaviour, and cross-company reporting cannot be observed in a single-company database.

## CAP-TXA2-08 Audit trail for tax-relevant records: tracking, chatter, deletion and attachment rules

### WHAT
- [N-TXA2-097] Tax-relevant changes are traced through field tracking on documents, journal items, taxes, partners, journals and the company, through chatter messages for state changes and reversals, and through guards on deleting records and attachments when the restrictive audit trail option is on.

### WHY
- [N-TXA2-098] An audit trail lets authorities and reviewers reconstruct changes; the restrictive option prevents loss of that record.

### BUSINESS RULE
- [N-TXA2-099] With the restrictive audit trail option a document that has been posted once can no longer be deleted (it can only be cancelled), the audit messages of documents, taxes, partners, accounts and the company cannot be deleted, and invoice PDFs and e-invoice files are detached rather than deleted. The option is off in the studied database and not forced by the Thai localization.
- [N-TXA2-100] State changes and corrections write notes on both documents involved: the reversal on the original and on the copy, the securing of an entry, the creation of a lock exception on the company, and the creation of a debit note or duplicate.
- [N-TXA2-101] No record of who read or printed a tax document is kept by the accounting application, and invoice date, due date, delivery date and fiscal position changes in draft are not tracked.

### STATE
- [N-TXA2-102] Not applicable as a state machine.

### OPTIONALITY
- [N-TXA2-103] Restrictive audit trail, the hash option, tracking-disable contexts and force-delete are the switches that change how much is recorded and protected.

### DEPENDENCY
- [N-TXA2-104] The audit of locks depends on date tracking; the audit of re-tagging does not exist; chatter retention depends on the audit-trail option.

### CONSTRAINT
- [N-TXA2-105] Restricted logs cannot be deleted; hashed entries cannot be altered or deleted; posted items cannot be deleted before the entry is reset.

### RISK
- [N-TXA2-106] Bypass contexts (force delete, tracking disable, bypass of audit, ignore tax lock) exist for code paths and imports; raw SQL tools leave no trace; draft-stage edits of the dates and fiscal position that decide the tax period are not tracked.

### UNKNOWN
- [N-TXA2-107] Retention of chatter in the studied configuration, and the completeness of the log for documents edited through import or external code, need execution.

## CAP-TXA2-09 Cross-module triggers into taxed documents: sales, purchase, inventory, expenses, payments

### WHAT
- [N-TXA2-108] Taxed documents are produced from sales orders, purchase orders, expense claims and (in the periodic valuation used here) from period-end closing. Each source passes currency, fiscal position, partner, payment term, line taxes and analytic distribution, but none passes an invoice date or a tax-point date; the delivery module adds a delivery date.
- [N-TXA2-109] Vendor bills created from purchase orders carry currency, fiscal position, partner, bank account, payment term and the order lines' taxes, with no bill date; the bill date must be entered before posting.

### WHY
- [N-TXA2-110] Taxed documents should be produced from business events with the same taxes, fiscal position and currency the business decided on, not retyped.

### BUSINESS RULE
- [N-TXA2-111] Inventory events create tax-neutral ledger lines. With perpetual valuation, posting a customer invoice adds cost-of-sales lines for eligible products; with periodic valuation (the studied configuration) no cost lines are added at invoicing and cost enters through a period-end closing entry. Neither carries document taxes.
- [N-TXA2-112] Employee expense claims paid by the employee are posted as purchase receipts partnered with the employee, dated today, created and posted with elevated rights; the supplier of the expense is not the partner of the document. Company-paid expenses create payment entries with taxes computed by the engine.
- [N-TXA2-113] The Thai localization sets the default sales and purchase taxes of the company to Output VAT 7% and Input VAT 7%, so documents created without an explicit tax pick them up through the product or account.

### STATE
- [N-TXA2-114] Orders drive documents forward but documents do not drive orders back except through invoiced quantity: a draft invoice already counts as invoiced and a cancelled one does not.

### OPTIONALITY
- [N-TXA2-115] Automatic invoicing after payment, the valuation mode, the anglo-saxon flag and the closing period are company or parameter options; the studied configuration has them off, periodic and manual.

### DEPENDENCY
- [N-TXA2-116] The tax outcome of a sales or purchase document depends on the fiscal position resolved at order level, the taxes stored on order lines at order time, and the date on which the document is posted.

### CONSTRAINT
- [N-TXA2-117] Documents of different fiscal positions or currencies from sales are never merged; vendor bills need a user with create rights; transfers cannot be dated inside a fiscal or hard lock.

### RISK
- [N-TXA2-118] Taxes and fiscal position are copied from the order and are not recomputed when the invoice is posted later or in another period; a delivery in one period and posting in another yields the invoice-date period, not the delivery period; returned goods do not produce a credit note by themselves; online payment can post invoices automatically.

### UNKNOWN
- [N-TXA2-119] Behaviour of manufacturing entries, landed costs, subcontracting and timesheet or expense re-invoicing for taxes was not read; perpetual-valuation cost lines are RT; bank statement reconciliation models that add taxed lines were not read.

## CAP-TXA2-10 Document presentation of tax documents: titles, report selection, stored PDFs

### WHAT
- [N-TXA2-120] A customer invoice prints with a document title that depends on type and state, in the language of the partner. For a company whose fiscal country is Thailand a different print layout is used whose invoice title for posted customer invoices is a fixed text, together with the buyer's branch label; a separate Commercial Invoice print exists for Thai customer-journal documents.

### WHY
- [N-TXA2-121] A tax document must be presentable in the form the local market expects; localization modules may substitute the print layout.

### BUSINESS RULE
- [N-TXA2-122] Core titles: Invoice (posted), Draft Invoice, Cancelled Invoice, Credit Note (posted or draft or cancelled), Vendor Credit Note, Vendor Bill, Self Billing variants; proforma variants when printing a proforma. Receipts have no title branch.
- [N-TXA2-123] In the Thai layout the title of a posted customer invoice is replaced by the fixed text Tax Invoice; draft, cancelled and credit note documents keep their core titles, so a Thai credit note prints Credit Note and a draft invoice prints Draft Invoice. The title text does not depend on any setting and its language follows the partner language only through translation of the fixed source text.
- [N-TXA2-124] A separate Commercial Invoice print is offered for Thai customer-journal documents; it renders the standard invoice document (not the Thai tax-invoice layout) in the partner language and refuses to print documents that are not invoices or receipts.
- [N-TXA2-125] Which print template is used for sending is chosen by partner, then journal, then the default invoice report; a generated PDF is stored on the document and detached when the document is reset to draft.
- [N-TXA2-126] The printed date block shows the invoice date with a type-specific label, the due date for posted customer invoices only, the supply date and delivery date only when set.
- [N-TXA2-127] A payment receipt is a separate printable document with a fixed generic title; it lists the invoices settled, with date, number and amounts, and shows no tax breakdown.

### STATE
- [N-TXA2-128] The title changes with the state: draft, posted and cancelled customer invoices print different titles; the stored PDF follows the posted document.

### OPTIONALITY
- [N-TXA2-129] The Thai layout depends only on the company fiscal country; the amount-in-words block, the payment QR block, the commercial invoice and the debit-note titles are separate options.

### DEPENDENCY
- [N-TXA2-130] Presentation depends on the company fiscal country, the partner language, the partner company registry and the optional debit-note module.

### CONSTRAINT
- [N-TXA2-131] The Commercial Invoice cannot be printed for entries or non-invoice documents.

### RISK
- [N-TXA2-132] The layout cannot be driven by the language or by document type; Thai statutory presentation (title wording per document kind, original or copy marking, seller branch, abbreviated or combined formats) is not modelled; the Thai text is a translation of a fixed English source string.

### UNKNOWN
- [N-TXA2-133] Rendered output (fonts, Thai text, number-in-words) needs execution; statutory content requirements are for the statutory lane.

## REGISTER: Function Catalog

| Cat-ID | Function (neutral name) | Topic # | Existing Function-ID or FUNCTION MAPPING REQUIRED | Neutral statements | Statutory link | Native status |
|---|---|---|---|---|---|---|
| TXA2-F01 | Issue and post a customer tax document (invoice) | 4, 5 | FUNCTION MAPPING REQUIRED | N-TXA2-004, N-TXA2-007, N-TXA2-018, N-TXA2-108 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F02 | Capture and post a vendor bill | 4, 5 | FUNCTION MAPPING REQUIRED | N-TXA2-004, N-TXA2-007, N-TXA2-018, N-TXA2-017, N-TXA2-109 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F03 | Credit note by reversal (customer and vendor) | 4, 7 | SDV-F07 | N-TXA2-005, N-TXA2-047 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F04 | Reverse and re-issue in one step (cancel with new draft copy) | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-047, N-TXA2-054 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F05 | Debit note issuance and numbering | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-001, N-TXA2-050 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F06 | Sales and purchase receipt document types | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-001, N-TXA2-006, N-TXA2-007, N-TXA2-014, N-TXA2-112 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F07 | Replacement / re-issued tax document concept (cross-referenced replacement) | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-043, N-TXA2-047 | TXS pending (statutory need not derived from system behaviour) | NATIVE GAP / EXTENSION REQUIRED |
| TXA2-F08 | Reset to draft and cancel of a posted document | 4, 7 | FUNCTION MAPPING REQUIRED | N-TXA2-008, N-TXA2-045, N-TXA2-046, N-TXA2-089 | none | NATIVE |
| TXA2-F09 | Derivation of invoice date, accounting date and due date | 5 | PCO-F04 | N-TXA2-015, N-TXA2-017, N-TXA2-018, N-TXA2-021 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F10 | Tax-point (supply or delivery) date handling | 5, 12 | PCO-F04 | N-TXA2-015, N-TXA2-019, N-TXA2-020 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F11 | Company lock dates, lock exceptions and hard lock | 5 | PCO-F01 | N-TXA2-029, N-TXA2-032, N-TXA2-034, N-TXA2-039 | none | NATIVE |
| TXA2-F12 | Postponement of entries that fall inside a locked period | 5, 7 | PCO-F01 | N-TXA2-031, N-TXA2-035, N-TXA2-022, N-TXA2-023 | none | NATIVE |
| TXA2-F13 | Refusal of edits to posted documents inside a locked period | 5, 7 | PCO-F01 | N-TXA2-033, N-TXA2-032 | none | NATIVE |
| TXA2-F14 | Tax period or tax-return period object and period closing | 5 | PCO-F02 | N-TXA2-029, N-TXA2-036 | TXS pending (statutory need not derived from system behaviour) | NATIVE GAP / EXTENSION REQUIRED |
| TXA2-F15 | Tax lock date maintenance (automatic at tax closing) | 5 | PCO-F01 | N-TXA2-036 | TXS pending (statutory need not derived from system behaviour) | NATIVE GAP / EXTENSION REQUIRED |
| TXA2-F16 | Fiscal year configuration for numbering | 5 | PCO-F02 | N-TXA2-029 | none | PARTIAL |
| TXA2-F17 | Cut-off of transfers against fiscal and hard locks | 5, 12 | PCO-F04 | N-TXA2-035 | none | PARTIAL |
| TXA2-F18 | Document numbering per journal, series and period | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-058, N-TXA2-060, N-TXA2-061, N-TXA2-062, N-TXA2-064 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F19 | Sequence gap detection and resequencing | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-062, N-TXA2-063 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F20 | Hash inalterability of posted documents (optional per journal) | 4, 10 | FUNCTION MAPPING REQUIRED | N-TXA2-063, N-TXA2-047 | TXS pending (statutory need not derived from system behaviour) | NATIVE |
| TXA2-F21 | Tax line and tag generation on documents | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-071, N-TXA2-073, N-TXA2-074 | none | NATIVE |
| TXA2-F22 | Cash-basis tax entries at reconciliation | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-075, N-TXA2-073 | none | NATIVE |
| TXA2-F23 | Withholding tax registered at payment time (optional module) | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-076 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F24 | Re-tagging of tax-report tags on existing entries (optional tool) | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-078 | none | PARTIAL |
| TXA2-F25 | Settlement and closing of tax accounts | 7 | FUNCTION MAPPING REQUIRED | N-TXA2-073, N-TXA2-036 | TXS pending (statutory need not derived from system behaviour) | NATIVE GAP / EXTENSION REQUIRED |
| TXA2-F26 | Reversal of tax effects (credit note, unreconcile) | 7 | SDV-F07 | N-TXA2-073, N-TXA2-047, N-TXA2-077, N-TXA2-075 | none | NATIVE |
| TXA2-F27 | Multi-company isolation of tax documents and configuration | 10 | MCT-F03 | N-TXA2-085 | none | NATIVE |
| TXA2-F28 | Access roles and record rules for tax documents | 10 | FUNCTION MAPPING REQUIRED | N-TXA2-087, N-TXA2-088, N-TXA2-089 | none | PARTIAL |
| TXA2-F29 | Audit trail by field tracking and chatter | 10 | RCN-F02 | N-TXA2-097, N-TXA2-100, N-TXA2-103, N-TXA2-028 | none | NATIVE |
| TXA2-F30 | Backdating audit (lock exception audit view) | 5, 10 | RCN-F02 | N-TXA2-100, N-TXA2-034 | none | PARTIAL |
| TXA2-F31 | Restrictive audit trail and attachment protection (optional) | 10 | FUNCTION MAPPING REQUIRED | N-TXA2-099, N-TXA2-101 | none | NATIVE |
| TXA2-F32 | Order-to-invoice hand-off of tax data (sales) | 12 | PDT-F01 | N-TXA2-108, N-TXA2-048 | none | NATIVE |
| TXA2-F33 | Order-to-bill hand-off of tax data (purchase) | 12 | PDT-F02 | N-TXA2-109, N-TXA2-048 | none | NATIVE |
| TXA2-F34 | Inventory-to-ledger triggers (cost lines, closing, date check) | 12 | SDV-F05 | N-TXA2-111, N-TXA2-054 | none | NATIVE |
| TXA2-F35 | Expense-claim receipts and their tax lines | 12 | FUNCTION MAPPING REQUIRED | N-TXA2-112, N-TXA2-054 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F36 | Online-payment driven invoice posting and reconciliation | 12 | FUNCTION MAPPING REQUIRED | N-TXA2-108 | none | NATIVE |
| TXA2-F37 | Return after invoicing: credit note raised separately | 4, 12 | SDV-F07 | N-TXA2-108, N-TXA2-048 | none | PARTIAL |
| TXA2-F38 | Thai tax-invoice print layout, fixed title and buyer branch | 4 | FUNCTION MAPPING REQUIRED | N-TXA2-120, N-TXA2-122, N-TXA2-123, N-TXA2-124, N-TXA2-125, N-TXA2-126, N-TXA2-132 | TXS pending (statutory need not derived from system behaviour) | PARTIAL |
| TXA2-F39 | Inter-company payment clearing | 10, 12 | FUNCTION MAPPING REQUIRED | N-TXA2-090 | none | PARTIAL |
| TXA2-F40 | Side effects of posting, reset, cancel and reversal in installed modules | 12 | FUNCTION MAPPING REQUIRED | N-TXA2-054 | none | NATIVE |

## REGISTER: Business Rules

| BR-ID | Rule (neutral) | Condition / configuration | Neutral statements | Class |
|---|---|---|---|---|
| TXA2-BR-01 | A document is always created in draft and becomes posted only through the posting action by a user with the invoicing role. | always | N-TXA2-004 | FACT |
| TXA2-BR-02 | Posting refuses a negative total, a missing customer on invoices, a missing bill date on vendor documents, documents without lines, archived journals or accounts and accounts of another company tree. | always (receipts are not asked for a customer, inferred) | N-TXA2-007, N-TXA2-018, N-TXA2-085 | FACT |
| TXA2-BR-03 | A credit note is a reversal of a posted invoice or bill, linked to the original, of the matching type; receipts reverse to credit notes of their side. | always | N-TXA2-005 | FACT |
| TXA2-BR-04 | The reversal can be taken as a draft credit note to edit and post, or as an immediately posted and reconciled credit note with a new draft copy of the original. | reversal date not in the future for the immediate option | N-TXA2-047 | FACT |
| TXA2-BR-05 | A reversal of a posted invoice sets the credit note date and invoice date to the date chosen in the wizard. | always | N-TXA2-047 | FACT |
| TXA2-BR-06 | No document or field links a re-issued tax document to the document it replaces. | always (negative search) | N-TXA2-043, N-TXA2-047 | INFERENCE |
| TXA2-BR-07 | A debit note exists only in an optional module that is not installed; when installed it copies a posted document into a linked draft with its own numbering prefix. | optional module installed | N-TXA2-001, N-TXA2-050 | FACT |
| TXA2-BR-08 | Sales receipts need a setting (on in the studied database); purchase receipts are always available; receipts share the number series of invoices and use the same taxes and posting flow. | setting for sales receipts | N-TXA2-006 | FACT |
| TXA2-BR-09 | Receipts print without a document title in the core layout. | core invoice layout | N-TXA2-014 | INFERENCE |
| TXA2-BR-10 | Resetting a posted document to draft keeps its number and is refused for hashed documents, cash-basis and exchange entries, localizations demanding a cancellation request, and locked periods. | always | N-TXA2-008, N-TXA2-033, N-TXA2-045 | FACT |
| TXA2-BR-11 | Cancelling a document keeps its number and removes its reconciliations but leaves the settling payments posted and unreconciled. | always | N-TXA2-008, N-TXA2-046, N-TXA2-009 | FACT |
| TXA2-BR-12 | Reset to draft and cancel carry no role check in code; only the view limits the buttons to the invoicing role. | always | N-TXA2-089, N-TXA2-008, N-TXA2-045 | FACT |
| TXA2-BR-13 | The accounting date of a customer document equals its invoice date until posting; for vendor documents it is derived from the bill date to keep the number series increasing. | always | N-TXA2-017 | FACT |
| TXA2-BR-14 | An empty invoice date on a customer document becomes today at posting; a vendor document needs a bill date. | always | N-TXA2-018 | FACT |
| TXA2-BR-15 | Invoice date, accounting date, partner, lines, payment terms, currency and fiscal position cannot be edited after posting. | always | N-TXA2-018 | FACT |
| TXA2-BR-16 | Delivery date is copied from the first completed customer delivery of the order onto customer invoices when the delivery module is installed and is informational only. | delivery module installed | N-TXA2-019 | FACT |
| TXA2-BR-17 | The supply (tax-point) date field exists but is empty and hidden in the base and in the Thai localization. | always | N-TXA2-015, N-TXA2-019, N-TXA2-020 | FACT |
| TXA2-BR-18 | Posting inside a locked period moves the date to the first date not blocked by the applicable locks instead of refusing. | always | N-TXA2-031 | FACT |
| TXA2-BR-19 | Which locks apply depends on journal type and tax impact: global and hard always, sales on customer journals, purchase on vendor journals, tax only for tax-affecting documents. | always | N-TXA2-032 | FACT |
| TXA2-BR-20 | Editing, resetting, cancelling or deleting a posted document inside a locked period is refused; the tax lock protects tax-affecting items even when the global lock is open. | always | N-TXA2-033 | FACT |
| TXA2-BR-21 | Soft locks can be relaxed per user or for all by time-boxed exceptions created by accounting administrators; the hard lock cannot be relaxed, lowered or removed. | always | N-TXA2-034 | FACT |
| TXA2-BR-22 | The tax lock date is not maintained automatically: no tax closing entry exists to set it. | always | N-TXA2-036 | INFERENCE |
| TXA2-BR-23 | There is no tax period or tax return object; a period is a date range chosen when a report is run. | always | N-TXA2-029 | INFERENCE |
| TXA2-BR-24 | Lock dates and exceptions are not maintained through any menu or setting in the base application. | always (negative search) | N-TXA2-034 | INFERENCE |
| TXA2-BR-25 | Transfers are checked only against the fiscal-year and hard locks. | stock valuation module installed | N-TXA2-035 | FACT |
| TXA2-BR-26 | Numbers are assigned at posting from the previous number of the same journal and series; customer invoices default to a yearly pattern, vendor bills to a monthly pattern. | always | N-TXA2-058, N-TXA2-060 | FACT |
| TXA2-BR-27 | Credit notes and payments get separate series by journal flag, with a distinguishing prefix, defaulting on for customer and vendor journals and bank journals. | journal flags | N-TXA2-060, N-TXA2-058 | FACT |
| TXA2-BR-28 | The Thai localization adds no numbering rule, sequence, journal option or date rule. | always | N-TXA2-060, N-TXA2-020, N-TXA2-010 | FACT |
| TXA2-BR-29 | A posted number must agree with the date period of its pattern; moving a document across periods needs the number cleared. | always | N-TXA2-061, N-TXA2-045, N-TXA2-062 | FACT |
| TXA2-BR-30 | Gaps and irregularities caused by draft, cancelled or deleted numbered documents are flagged on the journal dashboard; deletion of numbered documents that are not last in their series is restricted. | always | N-TXA2-062 | FACT |
| TXA2-BR-31 | An optional per-journal hash chain makes posted documents unalterable in number, date, journal, company and line label, amounts, account and partner; taxes, tags and invoice date are not covered. | journal option on | N-TXA2-063 | FACT |
| TXA2-BR-32 | Tax lines and tags are computed in draft and frozen at posting; taxes of posted items cannot change and tax lines cannot be deleted by hand. | always | N-TXA2-071, N-TXA2-033, N-TXA2-074 | FACT |
| TXA2-BR-33 | Tags follow the tax distribution for invoice or credit note when the tax is due on invoice or cash-basis tags are requested. | always | N-TXA2-073 | FACT |
| TXA2-BR-34 | Withholding in the Thai tax set is an ordinary negative tax booked at posting, not at payment. | Thai chart loaded | N-TXA2-073 | FACT |
| TXA2-BR-35 | Cash-basis taxes sit on a transition account until reconciliation and are then moved by a cash-basis entry; no Thai tax uses this. | tax set to payment basis | N-TXA2-075 | FACT |
| TXA2-BR-36 | Payment-time withholding exists only in an optional module that is not installed; it requires a withholding number and ignores the tax in document computation. | optional module installed | N-TXA2-076 | FACT |
| TXA2-BR-37 | An optional tool rewrites tax tags on existing items from a date, irreversibly, without lock checks or log. | optional module installed | N-TXA2-078 | FACT |
| TXA2-BR-38 | Documents are isolated by company; tax and fiscal configuration is shared up the company tree. | always | N-TXA2-085 | FACT |
| TXA2-BR-39 | Only invoicing and administrator roles are intended with the accounting application alone; operational roles are narrowed by record rules. | always | N-TXA2-087, N-TXA2-088 | FACT |
| TXA2-BR-40 | Documents created from sales orders are created with elevated rights; vendor bills from purchase orders with the user's own rights. | sales or purchasing installed | N-TXA2-089, N-TXA2-109 | FACT |
| TXA2-BR-41 | Field tracking and chatter record document and tax changes; line changes are logged only after the document was posted once. | always | N-TXA2-097 | FACT |
| TXA2-BR-42 | With the restrictive audit trail option, posted-once entries are cancelled rather than deleted and audit messages and attachments are protected; the option is off in the studied database. | option on | N-TXA2-099 | FACT |
| TXA2-BR-43 | Sales and purchase hand-offs copy taxes, fiscal position, currency and analytic distribution from the order but pass no invoice date. | always | N-TXA2-108, N-TXA2-109 | FACT |
| TXA2-BR-44 | Invoices from sales are merged only for the same company, partner, shipping partner, currency and fiscal position; bills from purchases by company, partner and currency. | always | N-TXA2-108, N-TXA2-109 | FACT |
| TXA2-BR-45 | Draft and posted invoices count as invoiced quantity on the order; cancelled ones do not; returns create no credit note. | sales installed | N-TXA2-108 | FACT |
| TXA2-BR-46 | Cost lines and closing entries created from inventory carry no document taxes; with periodic valuation no cost lines are created at invoicing. | stock valuation installed | N-TXA2-111 | FACT |
| TXA2-BR-47 | Online payment confirmation posts the linked draft invoices automatically and reconciles payments; automatic invoicing after payment is off unless a parameter is set. | payment modules installed | N-TXA2-108 | FACT |
| TXA2-BR-48 | Employee-paid expenses are posted as purchase receipts partnered with the employee and dated today. | expense module installed | N-TXA2-112 | FACT |
| TXA2-BR-49 | The Thai print layout is selected by company fiscal country; the title of a posted customer invoice is a fixed text; credit notes and drafts keep core titles; a Commercial Invoice print exists. | company fiscal country is Thailand | N-TXA2-120, N-TXA2-123, N-TXA2-124 | FACT |
| TXA2-BR-50 | The in-payment status is not reachable in the base application. | always | N-TXA2-002 | INFERENCE |

## REGISTER: State and Reversal

| Document or entity | State or event | Trigger | Reversal, cancel or correction path | Blocked when | Neutral statements |
|---|---|---|---|---|---|
| Customer invoice | draft -> posted | Post / Confirm by invoicing user; online payment confirmation; auto-post cron | Reset to draft (if allowed) or credit note | negative total; no customer; vendor needs bill date; inactive journal or account; hashed or locked states block later reversal only | N-TXA2-004, N-TXA2-007, N-TXA2-108 |
| Customer invoice | posted -> draft | Reset to Draft | Repost keeps the same number | hash; cash-basis or exchange entry; cancel-request localization; date inside fiscal or sale or hard lock or tax lock for tax items | N-TXA2-008, N-TXA2-033, N-TXA2-045 |
| Customer invoice | posted -> cancelled | Cancel (via reset to draft) | Reset to draft again | same as reset; payments stay posted | N-TXA2-008, N-TXA2-009, N-TXA2-046 |
| Customer invoice | posted + credit note | Reverse / Credit Note button | Credit note is itself reversible; replacement via new draft copy | original not posted; selection spans companies; journal type mismatch | N-TXA2-005, N-TXA2-055 |
| Vendor bill | draft -> posted | Post; auto-complete from purchase order | Reset to draft or vendor credit note | bill date missing; negative total; locked period shifts date | N-TXA2-018, N-TXA2-048, N-TXA2-031 |
| Customer / vendor credit note | draft -> posted (+ reconcile with original) | Post of reversal draft or immediate-cancel reversal | Reset to draft (not hashed); new invoice | negative total; lock shift; original not posted | N-TXA2-047 |
| Sales / purchase receipt | draft -> posted | Post | Reversal through the wizard from a list (no Credit Note button); reset or cancel as invoices | receipt customer not enforced (inference); no title on print | N-TXA2-006, N-TXA2-014, N-TXA2-007, N-TXA2-005 |
| Debit note (optional module) | draft linked to origin -> posted | Debit Note wizard then Post | Reverse via credit note; debit of debit refused | module not installed in studied database; origin not posted or already debited | N-TXA2-001, N-TXA2-050 |
| Journal entry with taxes | posted -> reversed | Reverse Entry (wizard); cancel or immediate reversal | Reversal entry posted and reconciled | hash; locked period | N-TXA2-077, N-TXA2-047, N-TXA2-008 |
| Hashed document | secured | Hash on post or on demand | Only credit note or reversal | reset, cancel, delete, hash-field edit, line deletion | N-TXA2-063, N-TXA2-008, N-TXA2-047 |
| Cash-basis tax entry | created / reversed | Reconcile / unreconcile payment | Reversal created automatically on unreconcile | cannot be reset to draft | N-TXA2-075, N-TXA2-008 |
| Company lock date | set / lowered / removed | Company record update (programmatic) | Soft lock: exception or lowering; hard lock: none | hard lock lowering or removal; hard lock with drafts; fiscal or hard lock with unreconciled statement lines | N-TXA2-034, N-TXA2-029 |
| Lock exception | create / revoke / expire | Created programmatically by an accounting administrator; revoked by an administrator | Revoke; expires automatically | more than one lock field; copy; non-manager revoke | N-TXA2-034 |
| Numbered document | delete | Delete by user | Reverse instead; administrators may delete with warning | not last in chain for non-administrators; posted lines; audit trail on; hashed | N-TXA2-062, N-TXA2-055, N-TXA2-099, N-TXA2-033 |
| Draft dated inside a lock | post | Post | Date shifted instead of refused | none (shift) ; edits afterwards refused | N-TXA2-031, N-TXA2-022 |
| Stock closing entry | create / post | Manual action or valuation cron | Reverse by dated entry or cancel | fiscal or hard lock shifts the date; cron skips manual-period companies | N-TXA2-111, N-TXA2-031 |
| Order invoiced quantity | draft invoice counted; cancelled invoice not counted | Invoice create / cancel | Credit note lowers invoiced quantity | receipts not counted (inference) | N-TXA2-108, N-TXA2-014 |
| Expense receipt | create and post | Expense approval | Cancel or reversal clears the expense link | none specific | N-TXA2-112, N-TXA2-054 |
| Tax tags on existing items | rewritten | Optional re-tag tool | None (irreversible) | only multi-parent child taxes block; no lock check | N-TXA2-078 |
| Payment-time withholding (optional) | registered on payment | Payment register | Payment cancel or unreconcile (behaviour unknown) | negative-or-zero base; missing number | N-TXA2-076 |

## REGISTER: Accounting Impact

| Event | Entries created or changed | Tax lines, tags and accounts affected | Period, lock and date effect | Reversal effect | Neutral statements |
|---|---|---|---|---|---|
| Draft created or edited (invoice, bill, receipt) | No posted entry; draft items and tax lines synchronised on each edit | Tax lines and tags computed in draft from line taxes; Thai VAT lines to the output or input VAT accounts, withholding lines to the withholding accounts | Date derived from invoice date; lock-shift alert shown for dates that will be moved | Delete or cancel the draft; nothing in ledger | N-TXA2-071, N-TXA2-073, N-TXA2-022 |
| Post customer invoice | Invoice entry (receivable, revenue, tax); cost-of-sales pair only for perpetual valuation (RT; periodic in the studied database) | Output VAT line (account 213200, grid labels 1 and 5); withholding sale lines to 114300; tags frozen | Date = invoice date, shifted if inside a lock; number assigned; hash if journal option | Credit note or reset to draft | N-TXA2-071, N-TXA2-073, N-TXA2-111, N-TXA2-031, N-TXA2-058 |
| Post vendor bill | Bill entry (expense, tax, payable); price-difference lines only with anglo-saxon flag (RT) | Input VAT line (114200, labels 6 and 7); withholding purchase lines to 213302 or 213301 reduce the payable | Accounting date derived from bill date (max with today in period), shifted by locks | Vendor credit note or reset to draft | N-TXA2-073, N-TXA2-017, N-TXA2-111, N-TXA2-031 |
| Post credit note (reversal) | Reversal entry with refund distribution; reconciled with the original | Same VAT or withholding accounts and grid labels as invoices (refund distribution) | Reversal date from wizard; shifted by fiscal lock at copy and by tax or fiscal locks at post | New invoice or reset to draft | N-TXA2-073, N-TXA2-047, N-TXA2-035 |
| Reverse and re-issue | Credit note posted and reconciled; new draft copy of the original lines | Credit note tax lines as above; new draft recomputes taxes | Wizard date for credit note and draft; future date blocks immediate cancel | Cancel the new draft; reverse the credit note by a new invoice | N-TXA2-047 |
| Reset to draft | Posted entry becomes draft; cost-of-sales lines and analytic lines removed; PDF detached | Tax lines remain on the draft and can be edited; tags recomputed on edit | Refused when date or tax items are inside a lock; number kept | Repost | N-TXA2-008, N-TXA2-054, N-TXA2-045, N-TXA2-033 |
| Cancel | Entry leaves the ledger; reconciliations removed; settling payments stay posted | Tax lines no longer in posted ledger; number kept | Same lock refusals as reset | Reset to draft | N-TXA2-008, N-TXA2-009, N-TXA2-046 |
| Register payment on invoice | Payment entry on outstanding account; reconciliation partials; possible exchange difference | No tax lines on the payment (base); cash-basis entry only for payment-basis taxes (none in Thai set); optional withholding module adds tax lines | Payment date; lock checks as any entry; cash-basis entry dated max(settlement, day after lock) | Unreconcile reverses cash-basis and exchange entries; cancel keeps payments posted | N-TXA2-076, N-TXA2-075, N-TXA2-009 |
| Online payment confirmed | Draft invoices linked to the transaction posted; payment created and reconciled | Taxes as on the invoice | Posting date = today unless locked | Credit note | N-TXA2-108 |
| Withholding registered at payment (optional module) | Payment entry with cash net of withholding, tax item, base and counterpart | Tax lines and base lines from the withholding tax tags; number required | Payment date | Payment cancel or unreconcile (unknown) | N-TXA2-076 |
| Tax tag update tool (optional) | No entry; tag links rewritten for items dated on or after the chosen date | Tags replaced with those of current tax configuration | Operates regardless of lock dates (warning only) | Irreversible except from backup | N-TXA2-078 |
| Stock closing entry (periodic valuation) | Entry in the stock journal for valuation and cost variation | No document taxes | Dated at the chosen closing date or today; shifted if inside fiscal or hard lock; cron posts | Reverse by dated entry | N-TXA2-111, N-TXA2-031 |
| Expense claim approved (own account) | Purchase receipt posted, partner = employee | Input tax lines from expense taxes, expense account; supplier not on receipt (inference) | invoice date set to today; accounting date derived | Cancel or reversal clears expense link | N-TXA2-112 |
| Down-payment invoice and final invoice | Down-payment invoice with order taxes; final invoice negates the down-payment lines | Tax lines for down payment and their negation on the final invoice | Dates as invoices | Credit note of either | N-TXA2-108 |
| Secure entries (hash) | No accounting change; hash stored; note logged | None; tags and taxes not hashed | Unreconciled lines or gaps block hashing | None; credit note only | N-TXA2-063 |
| Lock date set or relaxed | No entry; exceptions logged on company | Tax lock protects tax items | Later postings shift; edits refused | Soft: exception or lower; hard: none | N-TXA2-029, N-TXA2-034, N-TXA2-033 |
| Resequence numbers | Names of posted entries rewritten | None | Refused inside lock or for hashed documents sorted by date | Resequence again | N-TXA2-063, N-TXA2-033 |

