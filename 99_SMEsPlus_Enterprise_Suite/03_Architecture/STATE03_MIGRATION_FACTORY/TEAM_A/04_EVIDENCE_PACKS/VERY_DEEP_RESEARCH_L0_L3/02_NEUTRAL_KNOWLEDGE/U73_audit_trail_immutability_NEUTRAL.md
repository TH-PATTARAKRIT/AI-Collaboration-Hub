# U73 Neutral Knowledge — Audit Trail Immutability
> NEUTRAL LAYER — no source paths, no class or method names, no file extensions, no snake case identifiers, no backticks

| NR-ID | Statement |
|---|---|
| NR-U73-001 | The accounting system defines a current hash algorithm version number of 4; this version governs how new journal entries are secured and coexists with older versions for backward compatibility during integrity checks |
| NR-U73-002 | For the current hash version, the fields included in the cryptographic fingerprint of a journal entry header are: the entry reference number, the accounting date, the journal identity, and the company identity |
| NR-U73-003 | For the oldest legacy hash version, the entry reference number is excluded from the header fingerprint — only accounting date, journal identity, and company identity were included |
| NR-U73-004 | For the current hash version, the fields included in the cryptographic fingerprint of each journal line are: the line description, the debit amount, the credit amount, the account identity, and the partner identity |
| NR-U73-005 | For the oldest legacy hash version, the line description is excluded from the line fingerprint — only debit, credit, account identity, and partner identity were included |
| NR-U73-006 | The hash input is built by serialising all field values into a deterministically ordered JSON structure; relational fields are represented by their numeric identifiers rather than display names |
| NR-U73-007 | Monetary amounts are formatted to the currency's decimal precision before serialisation for hash versions 3 and 4 — this prevents floating-point rounding variance from producing different hashes for the same logical amount |
| NR-U73-008 | The final hash is produced by the SHA-256 algorithm applied to the concatenation of the previous entry's raw hash and the current entry's JSON string, both encoded as UTF-8 |
| NR-U73-009 | The stored hash value for version 4 entries carries a version marker prefix; when chaining, only the raw hash portion is passed forward — the version marker is stripped before concatenation with the next entry's data |
| NR-U73-010 | Hash chains are independent per journal and per document-number prefix — entries belonging to different journals or different naming sequences never share a chain |
| NR-U73-011 | The locked-entry reference number is stored in a separate integer field that is read-only, never copied, and indexed for efficient lookup — it records the entry's gap-free position within the secured sequence |
| NR-U73-012 | A journal may be set to automatically secure all entries when posted; once at least one entry in that journal carries a cryptographic seal, this setting cannot be reversed — the protection is permanent |
| NR-U73-013 | When a journal entry is posted, the system writes the entry state and the "previously posted" flag in a single operation, making both values atomically consistent |
| NR-U73-014 | The "previously posted" marker on a journal entry is set to true on first posting and is never cleared by any subsequent operation, including resetting the entry to draft |
| NR-U73-015 | Immediately after a journal entry is confirmed as posted, the system computes and stores its cryptographic seal, anchoring it permanently into the hash chain |
| NR-U73-016 | A journal entry that has been cryptographically sealed cannot be moved back to draft under any circumstances; the system enforces this with an explicit error regardless of user permissions |
| NR-U73-017 | Cash-basis tax entries — those generated automatically when a receivable or payable is reconciled — can never be reset to draft, even if they have no cryptographic seal |
| NR-U73-018 | Exchange difference entries generated during reconciliation also cannot be reset to draft |
| NR-U73-019 | When a journal entry is reset to draft, the "previously posted" flag, the reference number (sequence number), and the cryptographic seal are all preserved unchanged; only the workflow state, outbound sending flag, analytic postings, and PDF attachments are affected |
| NR-U73-020 | After a journal entry is posted, the following fields become unmodifiable: the line collection, the invoice date, the accounting date, the partner, the payment terms, the currency, the fiscal position, and the cash rounding setting |
| NR-U73-021 | When a journal entry carries a cryptographic seal, an additional set of fields is blocked from modification: the entry reference number, the accounting date, the journal, the company, the line descriptions, the debit and credit amounts, the accounts, and the partners |
| NR-U73-022 | The journal of a posted entry cannot be changed after first posting unless the reference number is simultaneously cleared; this prevents gaps in the numbering sequence of the original journal |
| NR-U73-023 | Changes to the accounting date, workflow state, and reference number of a journal entry are all individually tracked and recorded in the entry's communication history, providing a tamper-evident log of modifications |
| NR-U73-024 | The company-level setting that prevents deletion of posted journal entries is itself tracked in the audit log, so any activation or deactivation of this protection is recorded |
| NR-U73-025 | A separate company-level flag allows a localization to permanently enforce the audit trail — once set by a localization, the protective setting cannot be disabled |
| NR-U73-026 | When the audit trail protection is active for a company, any journal entry that has been posted at least once cannot be deleted; the system requires cancellation via a reversal instead |
| NR-U73-027 | The system distinguishes three deletion outcomes: entries that can be deleted (no seal, date outside lock period, not a cash-basis or exchange entry); entries protected by audit trail (routed to cancellation); and entries with a seal or structural protection (routed to reversal) |
| NR-U73-028 | At the moment a journal entry receives its cryptographic seal, a note is posted in its communication history recording that the entry has been secured — this creates a timestamp in the audit trail |
| NR-U73-029 | The hash chain computation checks for gaps in the sequence before proceeding; missing entries within the sequence raise an error that prevents hashing until the gap is resolved |
| NR-U73-030 | The hash chain is built incrementally: only entries with no existing seal that fall between the last sealed entry and the current entry's position are included in each hashing batch |
| NR-U73-031 | A localisation hook allows the system to block resetting e-invoices to draft if they have been submitted to a government tax authority — this extends the general immutability rules to regulatory submission contexts |
| NR-U73-032 | The "reset to draft" button is hidden in the user interface for any entry that belongs to a hash-secured journal, carries a seal, or is in a state that does not permit draft reversion — the guard operates both at the data layer and the presentation layer |
| NR-U73-033 | Cash-basis tax entries track their origin through two fields: the reconciliation event that triggered their creation, and the original invoice. Both references are checked when determining whether an entry can be unlocked, to handle cases where the reconciliation was later undone |
| NR-U73-034 | The accounting module in the Community edition contains no separate audit-log sub-module; all immutability and trail logic is embedded within the core accounting module itself |
| NR-U73-035 | Resetting an entry to draft removes its analytic cost postings entirely; those postings are regenerated when the entry is reposted — analytic records do not form part of the permanent audit trail |
