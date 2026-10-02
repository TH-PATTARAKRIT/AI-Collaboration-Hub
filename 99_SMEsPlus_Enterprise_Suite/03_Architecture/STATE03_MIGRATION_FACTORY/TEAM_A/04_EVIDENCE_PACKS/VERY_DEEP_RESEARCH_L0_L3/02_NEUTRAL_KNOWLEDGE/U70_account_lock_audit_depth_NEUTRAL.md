# U70 Neutral Knowledge — Account Lock Date and Audit Trail Depth
> NEUTRAL LAYER — no source paths, no class/method names, no file extensions, no snake_case, no backticks

| NR-ID | Statement |
|---|---|
| NR-U70-001 | The system distinguishes four soft period lock types — global, tax return, sales, and purchase — defined as a fixed ordered list used throughout the lock enforcement machinery. |
| NR-U70-002 | The hard period lock is treated distinctly relative to the four soft locks; together they form a set of five period-control dates. |
| NR-U70-003 | The global lock date is an optional date-type field stored on the company record, fully audited via change tracking. |
| NR-U70-004 | The tax return lock date is an optional date-type field on the company record with tracking; the system sets it automatically when a tax-period closing entry is posted. |
| NR-U70-005 | The sales lock date is an optional tracked date on the company record that applies only to entries in sales-type journals. |
| NR-U70-006 | The purchase lock date is an optional tracked date on the company record that applies only to entries in purchase-type journals. |
| NR-U70-007 | The hard lock date is a tracked date on the company record; its documentation states it is irreversible and excepts nobody. |
| NR-U70-008 | Each of the five lock dates has a corresponding computed effective-date field on the company record representing the date actually enforced for the current user after exceptions are considered. |
| NR-U70-009 | The four soft effective lock dates are computed per-user because they carry a user-identity dependency in their computation context; two users logged in simultaneously may see different effective lock dates. |
| NR-U70-010 | The hard effective lock date is computed without user identity as a dependency; it is derived by taking the maximum hard lock date across the company and all its parent companies, so it is the same for every user. |
| NR-U70-011 | When computing the effective soft lock date for a given user, the system first looks for an active exception record targeting that user (or all users) for that lock date field and company; if found, the exception's date is used instead of the company-level date. |
| NR-U70-012 | Lock date enforcement is hierarchical: parent company lock dates propagate to child companies, and the effective lock date is the maximum across all ancestors in the company tree. |
| NR-U70-013 | The fiscal lock date applied to a specific journal entry is the maximum of the global and hard effective lock dates, further raised by the sales or purchase effective lock date when the journal is of that type. |
| NR-U70-014 | The violation-detection routine accepts boolean flags controlling which of the five lock types are evaluated; this allows callers to check only the subset relevant to a given operation. |
| NR-U70-015 | When checking whether a soft lock date is violated, the system first tests against the exception-ignored date to determine if any violation exists at all; only then does it apply user exceptions to determine whether the violation is overridden for this user. |
| NR-U70-016 | The fiscal lock date check on a journal entry is a plain method call, not a database-level constraint; it raises a user-facing error of type user error rather than a validation error. |
| NR-U70-017 | The mechanism that allows internal system code to bypass the fiscal lock check relies on an object-identity comparison against a private sentinel; passing a truthy value that is not that exact sentinel object does not bypass the check. |
| NR-U70-018 | The error message produced when a fiscal lock date is violated includes a formatted list of which lock date fields were violated and their current dates, formatted according to the user's locale. |
| NR-U70-019 | Changing the date or name of a posted entry triggers a pre-write fiscal and tax lock check; the check fires before the ORM write call, acting as a guard rather than a post-write validation. |
| NR-U70-020 | Changing the state of a posted entry to draft or cancelled — moving it out of the posted state — triggers a fiscal and tax lock check; entries in a locked period cannot be unposted. |
| NR-U70-021 | After the write operation completes, a second fiscal lock check runs on all posted records; this catches cases such as a date change on a draft entry that is simultaneously being posted. |
| NR-U70-022 | During the posting operation, if the entry date falls within a locked period, the date is automatically shifted forward to an open period rather than rejecting the post; this is the intended auto-postpone behavior. |
| NR-U70-023 | The auto-postpone calculation sets the starting candidate date to the day after the latest violated lock date, then further advances it to the end of a month or year based on the journal sequence pattern. |
| NR-U70-024 | When an entry is duplicated, if the default or inherited date falls within a locked period, the system advances the copy's date to the day after the effective fiscal lock date. |
| NR-U70-025 | The tax lock check on individual journal lines is more selective than the fiscal lock check: it only applies to lines that affect the tax report, determined by whether the line carries tax codes, tax account links, or relevant tax tags. |
| NR-U70-026 | The error produced by a tax lock violation states the operation would impact an already-issued tax statement and directs the user to change either the entry date or the applicable lock dates. |
| NR-U70-027 | Setting the hard lock date to a value less than its current value, or clearing it after it has been set, is rejected with a user-facing error; the hard lock date is a one-way ratchet. |
| NR-U70-028 | Setting a hard lock date is blocked if any draft entries exist on or before the target date; the error is a redirect warning that opens the list of those draft entries for the user to resolve. |
| NR-U70-029 | Setting a global or hard lock date is blocked if there are unreconciled bank statement lines in the period to be locked; again a redirect warning is shown with the offending lines. |
| NR-U70-030 | When a company's soft lock date is updated, all active exceptions referencing that lock date field are automatically rebuilt to preserve their relative adjustments against the new lock date. |
| NR-U70-031 | The lock exception record type is a regular persistent model, not temporary or abstract. |
| NR-U70-032 | A lock exception has three lifecycle states — active, revoked, and expired — computed at read time rather than stored; revoked means manually deactivated, expired means the end time has passed. |
| NR-U70-033 | A lock exception with no user specified applies to all users of the company; user-specific exceptions narrow the effect to a single user. |
| NR-U70-034 | A lock exception with no end time remains in effect indefinitely unless manually revoked. |
| NR-U70-035 | Lock exceptions can only target the four soft lock date types; the hard lock date cannot have an exception, consistent with its irreversibility guarantee. |
| NR-U70-036 | The lock exception table carries a partial database index on company, user, and end time restricted to active records, ensuring efficient per-user lookup during every lock enforcement call. |
| NR-U70-037 | When multiple active exceptions exist for a user and lock date field, the one with the earliest date is selected, meaning the system applies the least permissive of the available exceptions. |
| NR-U70-038 | An exception with a null date value appears first in the sorted query and, when applied, sets the effective lock date to the minimum possible date value, effectively removing the lock entirely for that user. |
| NR-U70-039 | Each journal entry record carries two immutability-related fields: an integer gapless sequence counter and a character string holding the chained hash value; both are read-only, not copied on duplication, and indexed. |
| NR-U70-040 | Hash chaining is activated at the journal level; when enabled, every post operation retroactively hashes moves in the sequence, working backward to the most recently hashed entry. |
| NR-U70-041 | The current maximum hash version is 4; older versions 1 through 3 are retained only for backward-compatible integrity report generation. |
| NR-U70-042 | Under the current default hash version, the fields hashed at the entry level are the entry name, date, journal, and company; under the legacy version 1, the name is excluded. |
| NR-U70-043 | Under the current default hash version, the fields hashed at the line level are the line description, debit amount, credit amount, account, and partner; version 1 excludes the description. |
| NR-U70-044 | The hash algorithm is SHA-256 applied to the concatenation of the previous entry's hash and a JSON representation of all current entry and line hash fields; the result is prefixed with a version tag in version 4 format. |
| NR-U70-045 | A write operation that would modify any of the hashed fields or the hash value itself on an already-hashed entry is rejected with a user error naming the affected fields. |
| NR-U70-046 | Resetting a hashed entry to draft is unconditionally blocked with a user error; no exception path, manager override, or context flag removes this restriction in the standard community accounting module. |
| NR-U70-047 | The hash computation runs after the state write operation completes and after the entry name is flushed to ensure the name is stable before being included in the hash. |
| NR-U70-048 | The restrictive audit trail setting is a tracked boolean on the company record that controls whether previously-posted entries may be deleted. |
| NR-U70-049 | A localization module may force the restrictive audit trail to remain enabled; attempting to disable it in such a configuration raises a validation error. |
| NR-U70-050 | When the restrictive audit trail is enabled, any attempt to delete a journal entry that has ever been posted raises a user error directing the user to cancel instead; this guard fires during the delete operation, not at confirmation. |
| NR-U70-051 | For users without the billing-administrator role, deleting an entry that is not the last in its sequence chain is blocked unless the fast-edit mode is active or a force-delete context flag is set. |
| NR-U70-052 | The routine that decides whether to delete or reverse an entry applies four tests: whether a hash exists, whether the date is within a locked period, whether the entry is a tax-basis entry, and whether it is an exchange-rate difference entry; failure on any test routes the entry to reversal. |
| NR-U70-053 | An entry is considered protected by the audit trail if it has ever been posted and the company has the restrictive audit trail enabled; entries meeting this test are routed to cancellation rather than deletion in automated flows. |
| NR-U70-054 | The posted-before flag is a non-copyable boolean on the entry record that is set to true on first posting and never reset, not even when the entry is returned to draft; it permanently marks that the entry appeared in the ledger. |
| NR-U70-055 | Once an entry has been posted (even after reset to draft), its journal cannot be changed unless the sequence name is simultaneously cleared; this prevents gaps in the journal sequence caused by reassignment. |
| NR-U70-056 | An entry with a non-trivial sequence number also blocks journal changes even if it has never been posted, for the same gap-prevention reason. |
| NR-U70-057 | The following fields on a posted entry are treated as immutable and cannot be modified unless a context flag is set: invoice lines, all journal lines, invoice date, accounting date, partner, payment terms, currency, fiscal position, and cash rounding. |
| NR-U70-058 | If a journal defines a sequence-format validation pattern, a name change that does not match the pattern is blocked for non-administrator users; an administrator override clears the pattern. |
| NR-U70-059 | The date-shift calculation during posting accepts pre-computed violation results to avoid redundant lock date lookups when violations are already known. |
| NR-U70-060 | The entry-level lock date violation method is a thin delegation wrapper to the company-level implementation; the journal type is passed to determine which journal-specific locks apply. |
| NR-U70-061 | The company-level lock date violation method that accepts a journal and a tax flag produces a chronologically sorted list of all violated lock dates, useful for determining the latest violation for date-shift calculations. |
| NR-U70-062 | A computed message field on the journal entry surfaces a human-readable description when the current accounting date falls within a locked period; this message is displayed as a UI alert in the invoice form. |
| NR-U70-063 | The computed field controlling whether a reset-to-draft action is available in the UI depends on the hash status; a hashed entry never appears as resettable. |
| NR-U70-064 | The hash writing routine logs a chatter notification on each secured entry, creating a visible audit record of when the entry was hashed. |
| NR-U70-065 | Hashing entries in journals without hash mode enabled triggers a group activation step that grants the current user access to the secured-entries functionality. |
| NR-U70-066 | The reset-to-draft action validates state eligibility before checking immutability constraints; only posted or cancelled entries can proceed to the immutability checks. |
| NR-U70-067 | A successful reset to draft removes analytic lines, clears sending state, and may detach certain attachments, but does not clear the posted-before flag or the hash value. |
| NR-U70-068 | Cancelling a posted entry internally first resets it to draft, meaning all reset-to-draft guards — including the hash block — apply before cancellation; a hashed posted entry cannot be cancelled. |
| NR-U70-069 | The lock date bypass sentinel is a private module-level object not exported through the public interface; external or third-party code lacking access to that symbol cannot construct a bypass. |
| NR-U70-070 | The review-ability check in the base accounting module always grants permission, making it a hook reserved for extension by modules that implement accountant-role restrictions. |
| NR-U70-071 | Resetting a reviewed-marked entry to draft passes the same review-ability hook as marking it reviewed; in the base module both operations are always permitted. |
| NR-U70-072 | When an entry with a restrictive audit trail is force-deleted, a structured log message including the entry name, amounts, and per-account balances is written to the server log at informational level, not to a database audit table. |
| NR-U70-073 | Deleting a journal entry always removes reconciliation links on its lines and deletes those lines before removing the entry record itself; reconciliations cannot survive entry deletion. |
| NR-U70-074 | The lock date check within the unlinkability test uses user-aware effective lock dates including exceptions, so a user with an active exception may have entries considered unlinkable for others treated as unlinkable for themselves too. |
| NR-U70-075 | Lock exception state is computed at read time using two fields — whether the record is active and whether the end time has passed — with no persisted state column. |
| NR-U70-076 | The lock exception model references the authoritative list of soft lock date field names defined in the company model, ensuring both components stay in sync if the list ever changes. |
