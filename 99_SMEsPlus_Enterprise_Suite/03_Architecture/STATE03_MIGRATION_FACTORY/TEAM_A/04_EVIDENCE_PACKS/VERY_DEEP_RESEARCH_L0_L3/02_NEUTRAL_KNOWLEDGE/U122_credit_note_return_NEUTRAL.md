# U122 — Credit Note Return Immutability: Neutral Knowledge
## Date: 2026-10-02
## Gap: GAP-028

---

## How Credit Notes Are Created from Invoices

When a business needs to cancel or partially reduce a posted invoice, it issues a credit note (also called a reversal document). In the system, a credit note is simply another document of type "Customer Credit Note" (for sales) or "Vendor Credit Note" (for purchases). The two document types are mirror images: a customer invoice becomes a customer credit note, a vendor bill becomes a vendor credit note.

The creation process starts with the reversal wizard. A user opens a posted invoice and clicks "Reverse". The wizard requires:
- A reversal date (defaults to today)
- A journal (must be the same type as the original)
- An optional reason text

The wizard refuses to proceed if the source invoice is not in the posted state. It also refuses if multiple invoices from different companies are selected at once.

When confirmed, the wizard calls the core reversal method. That method copies the original invoice, assigns the reversal date, inserts the original invoice's reference in the reversal's ref field, and records a permanent link back to the source (the "reversal of" pointer). The copy is then modified: for plain journal entries and cost-of-goods-sold lines, all monetary amounts are sign-flipped; for regular invoice lines, the sign-flip is not needed because the document type itself carries the reversed meaning.

---

## Partial vs Full Reversal

Every reconciliation in the system is represented as a partial reconciliation record. That record holds a pointer to one debit-side journal item and one credit-side journal item, plus three monetary amounts: the matched amount in company currency, the matched amount in the debit line's currency, and the matched amount in the credit line's currency. This structure naturally supports partial matching (the credit note covers only part of the original invoice's open balance).

When a credit note fully offsets an invoice, an additional full-reconciliation record is created automatically, linking all the contributing partial matches into one group. The matched documents are then marked as fully paid and their residual amount drops to zero.

If only part of the invoice is reversed, no full-reconciliation record is created, the invoice remains partially open, and both documents continue to show a residual balance.

---

## Reconciliation Linkage

When the wizard creates a credit note with the "cancel" option (used for plain journal entry reversal or the "modify" workflow), reconciliation happens immediately inside the same transaction: the method first strips any existing partial matches from the source move's lines, creates the reverse, posts it immediately, and then reconciles each matching pair of lines grouped by account and currency. This is the "hard cancel" path.

For invoice reversals without the cancel flag (the standard credit note path), reconciliation is deferred to the moment the credit note is posted. At posting time, the system looks for any newly posted move whose reversal-of pointer targets an invoice that is still in the posted state. It then calls the reconciliation method on that pair, attempting to match each account group.

The link between the original invoice and its credit note is bidirectional at the object level: the credit note carries a "reversal of" pointer to the original, and the original carries a collection of all credit notes that point back to it. This means querying in either direction is efficient.

---

## Immutability After Reconciliation

Once a credit note (or any journal entry) is posted on a journal with hash-table security enabled, the system computes a SHA-256 hash of that entry's key fields (document name, date, journal, company, and all line amounts and accounts) chained from the previous entry's hash in the same journal sequence. This hash is written to the entry's inalterable hash field and cannot be changed afterwards.

An entry with a non-empty inalterable hash is permanently immutable in the following ways:

1. Any attempt to reset it to draft is blocked. The draft-reset button is hidden from the user interface when a hash is present, and even if the button were somehow invoked, the internal check raises an error with the message "You cannot reset to draft a locked journal entry."

2. Any attempt to modify the fields covered by the hash (document name, date, journal, company) through a record write is blocked with an error naming the violated fields.

3. Any attempt to delete the entry is blocked because the deletion eligibility check requires the hash to be absent.

4. The only way to "undo" a hash-secured entry is to create a new reversal of it — which itself will be hashed when posted, extending the chain rather than breaking it.

An entry without a hash (on a journal where hash security is not enabled) can still be reset to draft, but only if: its date is not within a locked fiscal period, it is not an exchange difference entry, it is not a cash basis tax entry, and (when the company's restrictive audit trail is on) no government cancellation request is required.

---

## Hash Chain Interaction with Credit Notes

The hash chain works sequentially within each journal and sequence prefix. When a credit note is posted on the same journal as the original invoice (which is the normal case), the credit note receives its own hash that chains from the last previously hashed entry in that sequence. The credit note's hash does not depend on or reference the original invoice's hash directly — it depends only on the previous entry in the numeric sequence.

Because the chain is sequential, inserting or removing entries would break it. Resetting a hashed credit note to draft and then deleting it would create a gap in the hash sequence for that journal. The system prevents this by blocking the draft reset entirely for hashed entries.

If a credit note is created but the journal does not use hash security, the credit note is not hashed and can be reset to draft (subject to fiscal lock date and audit trail checks). Once the journal's hash setting is enabled and a manual hash operation is run (or the next posting occurs), all previously unhashed posted entries in that journal's sequence are hashed together in one pass.

---

## Sale Return and Stock Integration

When a sale credit note is created as a return, the stock valuation module navigates from the credit note back to the original sale invoice via the reversal-of pointer to collect the original outbound stock moves. This ensures that the cost reversal uses the exact same stock movements as the original delivery, giving correct COGS values.

For credit notes that were created manually (without a reversal-of pointer), a fallback path searches for COGS lines on invoices linked through the same sale order lines, maintaining correct cost accounting even without the formal reversal link.

---

## Summary of Immutability Rules

| Condition | Can reset to draft? | Can delete? | Can modify hash fields? |
|-----------|--------------------|-----------|-----------------------|
| Has inalterable hash | No (hard block) | No | No (hard block) |
| Date in fiscal lock period | No | No | No |
| Exchange difference entry | No | No | No |
| Cash basis entry | No | No | No |
| Need government cancellation | No | No | Yes (allowed) |
| None of the above | Yes | Yes | Yes |
