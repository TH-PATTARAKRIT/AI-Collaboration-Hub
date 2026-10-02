# U114 — Neutral Knowledge: Journal Locking and Sequence Integrity
## Date: 2026-10-02
## Classification: Neutral — Business Language Only

---

## Overview

Odoo 19 Community edition enforces two distinct but related controls over journal entries: lock dates that prevent modification of entries in closed accounting periods, and sequence integrity rules that ensure journal entry numbers are assigned without gaps or inconsistencies.

---

## Lock Date Architecture

The system provides five distinct lock date types at the company level:

**Global Lock Date (Fiscal Year Lock)**: Prevents all journal entries from being posted on or before this date. Applies across all journal types unless overridden by a more specific lock.

**Tax Return Lock Date**: Restricts modification of entries that affect the tax report. This date is set automatically when the tax period closing entry is posted. It only blocks entries where tax-report-affecting lines are present.

**Sales Lock Date**: Applies specifically to sales-type journals. Entries dated on or before this date cannot be modified in sales journals.

**Purchase Lock Date**: Applies specifically to purchase-type journals. Operates identically to the sales lock date but for purchase journals.

**Hard Lock Date**: An unconditional and irreversible lock. Unlike the other four lock dates, it cannot be bypassed by any user exception mechanism. Once set, no entry on or before that date can be modified under any circumstances.

### How Lock Dates Are Evaluated

The effective lock date for any given entry is the maximum of all applicable lock dates for the entry's journal type. For a sales journal entry, the system compares the global lock date, the sales lock date, and the hard lock date, then applies the highest. For purchase journals, the purchase lock date is substituted for the sales lock date.

Lock date violations are checked at two distinct points in the entry lifecycle:
1. When an entry is being written (including when the date or sequence number changes on a posted entry).
2. When an entry transitions out of posted status (such as being reset to draft).

After these checks pass, a final post-write validation confirms that the resulting posted state has not introduced a lock date violation.

A special bypass mechanism exists using an object-identity sentinel in the execution context, allowing automated system processes to bypass lock date checks when required for internal operations.

---

## Sequence Numbering Architecture

Journal entry sequence numbers are assigned per journal, with the journal acting as the sequence boundary. Each journal maintains its own independent sequence stream.

**Sequence Format**: The system recognises five sequence patterns:
- Fixed sequences with no date component
- Yearly sequences embedding the year
- Monthly sequences embedding year and month
- Year-range sequences embedding a start and end year
- Year-range monthly sequences embedding start year, end year, and month

The system automatically detects which format is in use by analysing the format of the most recent entry in the journal.

**Dedicated Sub-Sequences**: Journals can be configured to maintain separate sequence streams for different entry types:
- Sales and purchase journals default to a dedicated sequence for credit notes, keeping invoice and credit note numbers separate.
- Bank, cash, and credit card journals default to a dedicated sequence for payments, keeping payment numbers separate from bank transaction numbers.

**Custom Sequence Format**: A journal can be configured with a custom regular expression that overrides the system's automatic format detection, enabling non-standard numbering schemes.

**Sequence Validation**: A constraint enforces that the date embedded in a sequence number must match the actual entry date. This constraint applies only to posted entries and not to entries in quick-edit mode. The check can be globally suppressed for dates before a configurable start date, allowing legacy data to be maintained without triggering validation failures.

---

## Sequence Gap Detection

The system maintains a flag on each entry indicating whether that entry created a gap in its sequence. A gap is defined as a case where consecutive entries in the same journal and sequence prefix do not have numerically adjacent sequence numbers.

Gap detection runs whenever:
- A sequence-related field on an entry changes (such as the sequence number, sequence prefix, journal, or name).
- An entry is unlinked.

The gap check examines both the immediately preceding and following entries within the same journal and prefix. A gap is also flagged when a draft entry follows a posted entry in the sequence, as this represents a potential hole.

---

## Hash Chain Integrity

When a journal is configured with the "Secure Posted Entries" option enabled, each entry receives an irreversible cryptographic hash upon posting.

**Hash Computation**: The hash for each entry is computed as a SHA-256 digest of the prior entry's hash combined with a JSON representation of the current entry's key fields (sequence number, date, journal, company, and the amounts and accounts on each line). This creates a chain where any tampering with an entry would invalidate the hashes of all subsequent entries.

**Hash Versioning**: The system supports multiple hash algorithm versions for backward compatibility. The current default version embeds the version number as a prefix in the stored hash value.

**Retroactive Hashing**: When an entry is posted, the system hashes not just the new entry but all preceding unhashed entries in the same sequence prefix chain, starting from the last previously hashed entry.

**Sequence Gap Blocks Hashing**: Before computing hashes, the system verifies that the sequence of entries to be hashed is contiguous. If a gap is detected in the sequence numbers within the chain, hashing is blocked and an error is raised. This ensures the hash chain cannot be applied over an incomplete sequence.

**Hash Protection of Fields**: Once an entry carries a hash, any attempt to modify its integrity-protected fields (sequence number, date, journal, company, and line amounts/accounts) is blocked with an error message. The entry becomes immutable.

**Journal Restriction vs Forced Hash**: Hash protection is optional and controlled per journal. An entry can also be hashed independently of journal settings via an administrative function that forces hashing regardless of journal configuration.

---

## Relationship Between Locking and Sequence Integrity

Lock dates and sequence integrity are complementary controls that operate at different levels:

- Lock dates prevent any modification to entries within a closed period, including preventing creation of new entries back-dated into that period.
- Sequence integrity ensures that the numbering of entries within any sequence remains contiguous and that the embedded date in the sequence matches the entry date.
- Hash chain integrity adds a third layer of tamper-evidence by cryptographically linking entries within a sequence prefix, ensuring that no entry can be modified or removed without detection.

When an entry is posted, all three controls activate: the entry date is checked against all applicable lock dates, the sequence number is assigned and its format validated against the entry date, and (if the journal is configured for hash protection) a hash is computed and stored.
