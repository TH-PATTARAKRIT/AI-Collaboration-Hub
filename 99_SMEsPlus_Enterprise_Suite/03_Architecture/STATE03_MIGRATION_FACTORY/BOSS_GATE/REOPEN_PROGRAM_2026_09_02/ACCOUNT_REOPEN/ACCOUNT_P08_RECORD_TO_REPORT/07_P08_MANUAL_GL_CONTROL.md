# P08_MANUAL_GL_CONTROL

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1

The directive requires that **manual GL must not silently destroy source provenance**. This file establishes what the benchmark actually permits.

## 1. What a manual entry may do that a document-generated entry may not

| ID | Capability | Class |
|---|---|---|
| `MGL-01` | Set an **arbitrary accounting date**. The period-normalisation applied to source documents short-circuits for any entry without a document date, so a manual entry is never normalised at edit time. | FACT VERIFIED |
| `MGL-02` | Post to **any account, including subsidiary-ledger control accounts**. The rules that keep control accounts aligned to their subsidiary ledgers are gated on the entry being a customer or supplier document; a manual entry is neither, so both branches are skipped and the constraint is a no-op. | FACT VERIFIED, independently reproduced by this session |
| `MGL-03` | Post into **any book**, not only a miscellaneous book. The confinement is a data-entry-screen field domain, not a constraint. Any programmatic, import or automation path may book a manual entry into a sales, purchase, bank, cash or credit book and consume that book's number series. | FACT VERIFIED |
| `MGL-04` | **Claim a source it does not have.** The provenance references are ordinary writable fields with no validation and no deletion guard. | FACT VERIFIED for the field declarations; `B NOT FOUND IN SEARCHED SCOPE` for the absence of a server-side check elsewhere in the stack |
| `MGL-05` | Touch a control account **without a counterparty and without a due date** — the rule requiring both runs only on document entries. | FACT VERIFIED |

## 2. What guards a manual entry actually meets

In order: balance (application-level, suppressible by a caller-supplied parameter, reporting currency only) · cannot be created already posted · book-to-document-type match (sales and purchase documents only, so inapplicable) · tax-country coherence · account not retired (suppressible by a caller-supplied parameter) · account secondary-currency agreement · the account's own book allow-list · the book's own account allow-list, **which is bypassed for that book's default and suspense accounts** · off-balance segregation · at posting: at least one line, active book, active currency, posting right · at posting: lock dates, enforced by **silently moving the date forward**, not by refusal.

The account's own control status confers **no** posting restriction. That is the inversion.

## 3. Provenance destruction — enumerated paths

| ID | Path | What is destroyed | Recorded anywhere? |
|---|---|---|---|
| `MGL-D-01` | Return to unposted | every settlement match the entry participated in; every cost allocation | no ledger record of what was removed |
| `MGL-D-02` | Return to unposted, re-date, re-post | the number-to-period correspondence — the entry keeps its original number while its date moves to another period; the warning designed to catch number changes does not fire on a date-only change | the number/date mismatch is visible only by inspection |
| `MGL-D-03` | Direct in-place edit of a posted item | account, counterparty, label, reference, cost allocation and tax classification are all writable on a posted item from the standard line-listing screen, in bulk, with no reopen and no reversal, whenever the period is open and the item is unmatched | label, due date, reference and cost allocation carry **no check at all** |
| `MGL-D-04` | Administrative renumbering | the entry number of a selection of posted entries | during the operation the rows leave the uniqueness index |
| `MGL-D-05` | Commercial-partner re-parenting | the counterparty recorded on posted items, across every company, with the period lock explicitly suppressed | logged on the counterparty record, not on the affected entries |
| `MGL-D-06` | Custom re-dating utility | the entry number (discarded and reallocated), the date, and — by direct database statement — an inventory valuation timestamp | a debug print statement; no audit record |
| `MGL-D-07` | Custom settings-level erase | the entire ledger, by direct database statement, whole-table, every company, with sequences reset | nothing; the operation never passes through the object layer |

`MGL-D-03` is the headline. **Posting does not make a journal item read-only**, and the correction path most likely to be used in practice is the one with the fewest checks.

## 4. Requirements

| ID | Candidate requirement |
|---|---|
| `P08-RQ-MGL-01` | A manual entry is an accounting event like any other. It carries an event identity, a stated reason, and an actor, and it is subject to every control a generated entry is subject to. |
| `P08-RQ-MGL-02` | Control-account status is a **declared property that carries its own posting restriction**, evaluated on every entry regardless of its type. Posting to a control account outside its subsidiary process is refused, not merely discouraged. |
| `P08-RQ-MGL-03` | The provenance reference on a posted fact is immutable and is set only by the process that produced it. A manual entry has none, and that absence is itself the record. |
| `P08-RQ-MGL-04` | A posted journal item is immutable in every attribute. There is no in-place correction path. |
| `P08-RQ-MGL-05` | No path may write to the ledger outside the object layer. A direct database statement against a ledger table is prohibited by design, not by convention. |
| `P08-RQ-MGL-06` | The accounting date is asserted by the preparer, validated, and either accepted or refused. It is never silently moved. |
