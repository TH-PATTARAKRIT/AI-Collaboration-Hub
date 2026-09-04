# P08_ACCOUNTING_EVENT_REGISTER

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1

**Definition used:** an accounting event is an occurrence after which the ledger asserts something it did not assert before.

**The finding that governs this whole register:** the benchmark has **no accounting-event object** — `A VERIFIED ABSENCE, scope = the declared 22-root set` (`RS-A-01`). Every event below is therefore *inferred from the posting it produces*, not read from a carrier. That is itself the point: the register can be written, and the system cannot.

## 1. Events the ledger emits on its own account

These are the ones no user asks for. They are the dangerous ones, and P08 owns all of them.

| ID | Event | Trigger | Visible at the moment it occurs? | Reversible | Class |
|---|---|---|---|---|---|
| `AE-01` | **Accounting date relocated at posting** | the requested date falls in a locked period | **no** — the posted record carries no trace that its date was moved, and the originally requested date is retained nowhere | not applicable | FACT VERIFIED |
| `AE-02` | **Accounting date recomputed on a document-date change** | the document date of a non-sale document changes | **no** | not applicable | FACT VERIFIED |
| `AE-03` | **Settlement difference posted** | a match is made whose two sides were measured differently | yes — a separate entry | by un-matching, which reverses rather than removes | FACT VERIFIED |
| `AE-04` | **Cash-basis tax entry posted** | the same match | partly | partly | FACT VERIFIED |
| `AE-05` | **Cash-basis tax entry dated to the system clock** | the matched documents predate the lock | **no** | not applicable | FACT VERIFIED — **can cross a year boundary** |
| `AE-06` | **Settlement matches destroyed** | an entry is returned to unposted, or reversed | **no** — no confirmation, no ledger record of what was removed | not at all | FACT VERIFIED |
| `AE-07` | **Cost allocations destroyed** | an entry is returned to unposted | **no** | not at all | FACT VERIFIED |
| `AE-08` | **Posted history restated by an account re-code or re-classification** | an account's code or classification is written | **no** | not applicable | FACT VERIFIED |
| `AE-09` | **Posted history restated by an account merge** | administrative merge | **no** — the operation writes no record of any kind | not at all | FACT VERIFIED |
| `AE-10` | **Counterparty on posted items rewritten across every company** | commercial-partner re-parenting, available to a contacts role | **no** — logged on the counterparty, not on the entries | not at all | FACT VERIFIED |
| `AE-11` | **Tax cut-off advanced** | a tax return entry is posted | yes | only by the narrow tax-specific path | FACT VERIFIED |
| `AE-12` | **Statement figures materialised as stored values** | a cut-off date is moved, in either direction | **no** | pre-existing values are never overwritten | FACT VERIFIED |
| `AE-13` | **Entry number reallocated** | administrative renumbering, or a custom re-dating utility | partly | not at all | FACT VERIFIED |
| `AE-14` | **Posted entry line detail deleted and recreated** | unattended automatic bank matching | a note written after the fact | not at all | FACT VERIFIED |
| `AE-15` | **Stored open amounts overwritten out of step with the matches** | matching enabled on an account already carrying matches | **no** | not at all | SUPPORTED INTERPRETATION |

**Ten of fifteen are invisible at the moment they occur.** Six of the fifteen are not reversible by any mechanism.

## 2. Events the ledger recognises but does not carry

| ID | Event | Carrier in the benchmark |
|---|---|---|
| `AE-16` | Period closed | **none** — a cut-off date moves |
| `AE-17` | Period reopened | **none** |
| `AE-18` | Statement issued | **none** — an ordinary attachment with no reference to the data state |
| `AE-19` | Year result appropriated | **none** — computed at read time |
| `AE-20` | A business fact was recognised as having an accounting consequence | **none** |
| `AE-21` | A posting rule was applied, in a given version | **none** |

## 3. The events register versus the benchmark's own scope

The register above is complete **against the mechanisms this session searched**, and that scope is declared in `19_P08_SOURCE_LINK_REGISTER.md`. It is **not** declared complete as a class list. The programme's own experience is that a taxonomy's empty cells mean *unsearched*, not *absent*, with a two-of-two record of a verified defect emerging on first search of a previously empty class. This register therefore carries no empty cells: every row is an instance, and the classes with no instance found are named in §2 with their carrier stated as absent.

`P08-U-AE-01` (Class C) — the class list itself has not been tested for completeness. Events emitted by modules outside the accounting dependency closure were not swept.

## 4. What P08 requires

`AE-RQ-01` — Every event in §1 must become **visible at the moment it occurs**, or must not occur.
`AE-RQ-02` — Every event in §2 must acquire a carrier. `AE-16`, `AE-17` and `AE-18` are the close model's requirements; `AE-19` is `P08-BD-06`; `AE-20` and `AE-21` are the kernel's `K2` and `K3`.
`AE-RQ-03` — No event may be emitted by an operation whose stated purpose is something else. `AE-06`, `AE-07`, `AE-08` and `AE-10` all are.
