# P08_PERIOD_CLOSE_MODEL

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1

## 1. The calendar

| ID | Statement | Class |
|---|---|---|
| `PC-01` | Two independent fiscal-year definitions exist: a company-level day/month pair, and an **optional** table of named year records used to describe irregular years. Where a record covers a date it wins; otherwise the boundaries are arithmetic. | FACT VERIFIED |
| `PC-02` | The year record carries a name, a start, an end and an owner — **and nothing else**. No state, no closed marker, no lock, no link to any entry. | FACT VERIFIED |
| `PC-03` | **The two definitions can disagree, and different subsystems consult different ones.** Entry numbering uses the day/month pair exclusively; statements consult the year-record table first. An irregular year record whose boundaries differ from the pair therefore numbers entries over one window and presents them over another. | FACT VERIFIED (static divergence); `D UNKNOWN` whether it manifests in a given deployment |
| `PC-04` | **No accounting-period entity exists.** | **A VERIFIED ABSENCE, scope = the declared 22-root set** (`RS-A-02`) |
| `PC-05` | A transaction has no period attribute. Its period is its accounting date, and every period grouping downstream is a date-range predicate. | FACT VERIFIED |
| `PC-06` | The year-end parameters are delegated to the **root** of the company tree, so a subsidiary cannot hold its own year-end. | FACT VERIFIED |

`PC-06` read scope-aware is an over-constraint: a fiscal year is a legal attribute of a legal entity, so its scope is `COMPANY`. Recorded as `P08-CONTRA-09`.

## 2. Lock control

`PC-07` — **Five** cut-off dates bind postings: a general cut-off, a tax-return cut-off, a sales-document cut-off, a purchase-document cut-off, and an irrevocable cut-off. The first four are relaxable; the fifth is not. Five further computed fields are per-user projections of these, not independent controls. `FACT VERIFIED`. Denominator declared: 32 date fields whose name contains a lock or closing token exist across the target root; **5** of them bind a posting.

`PC-08` — Hierarchy handling is **asymmetric**: the four relaxable cut-offs are evaluated per ancestor and may be relaxed per ancestor; the irrevocable cut-off is the strictest value across the whole ancestor chain and cannot be relaxed at any level. `FACT VERIFIED`.

`PC-09` — The effective cut-off for an entry is journal-type dependent. The tax cut-off is enforced separately and only for items that affect the tax return. `FACT VERIFIED`.

## 3. The exception mechanism — control-critical

`PC-10` — An exception lowers **exactly one** relaxable cut-off, for one named user or for **everyone**, for one of five preset durations of which the longest is **unlimited**. It cannot target the irrevocable cut-off. A justification may be entered and **is not required**. `FACT VERIFIED`.

`PC-11` — **The most permissive grant on the form produces no exception record at all.** Unlimited duration applying to every user is handled as an ordinary cut-off change written directly to the company. Every narrower grant produces a discrete, inspectable record; the widest does not, and its only trace is a field-change entry in the company's activity log. `FACT VERIFIED`. This is the control-critical finding of this file.

`PC-12` — An exception cannot be antedated, but **the depth of the window it opens is unbounded** — the cut-off may be lowered to any date, including one in a prior year. A five-minute grant can expose an arbitrarily deep history. `FACT VERIFIED`.

`PC-13` — Whenever a relaxable cut-off moves, every live exception against it is **automatically re-issued** as a new record and the previous one withdrawn, so a single continuing grant appears in the trail as a chain of withdraw/issue pairs. `FACT VERIFIED`.

`PC-14` — **No screen lists the exceptions granted.** `B NOT FOUND IN SEARCHED SCOPE`, scope = every view and menu definition in the target root. Individual records are reachable only by following a link.

`PC-15` — Each exception offers a button listing the transactions touched during its validity — **which depends on a company-level change-log switch that has no default and must be enabled before any transaction exists.** If it was never enabled, the exception's own audit button has nothing to show. `FACT VERIFIED`.

`PC-16` — Granting and revoking are **the same authority**. `FACT VERIFIED`, corroborating the prior programme finding.

## 4. Close

`PC-17` — **Closing a month is the movement of a cut-off date. It is not a state transition, because there is no object to transition.** Three mutually confirming grounds: no period entity exists at 22-root scope; the year record has no state; and the close routine's entire effect is a write of the new cut-off onto the company. The code's own definition of "the period being closed" is the span between the old and the new cut-off. `FACT VERIFIED`.

Consequences, all `FACT VERIFIED`: a soft close is **reversible** by writing an earlier value; the audit artefact is a field-change entry and nothing more; and **no field anywhere answers "is month M closed?"** — only "is date D at or before cut-off L, for this user".

`PC-18` — Pre-close validation is thin and asymmetric: unposted entries in the period block only the **irrevocable** cut-off, not an ordinary month close, which merely shows a warning; unreconciled bank lines block the general and irrevocable cut-offs; the irrevocable cut-off may never decrease; and no cut-off may be set in the future. `FACT VERIFIED`.

`PC-19` — Moving a cut-off **materialises the then-current values of designated statement lines as stored figures**, and pre-existing stored figures are never overwritten. This is the benchmark's only statement-snapshot mechanism, and it is a side effect of a lock change rather than an act of issuance. `FACT VERIFIED`.

`PC-20` — That snapshot hook fires on a cut-off **decrease** as well as an increase, producing an inverted date range whose downstream behaviour was not established from the code. `SUPPORTED INTERPRETATION` — candidate defect, runtime confirmation required.

## 5. Year close

`PC-21` — **No year-end closing entry is generated.** Four independent search patterns over the target root return no result-appropriation mechanism. Across the declared 22-root set the vocabulary pattern's count varies with build completeness and the matches were not each opened, so the root-set-wide form of this claim is held at `B NOT FOUND IN SEARCHED SCOPE` (`RS-B-01`) rather than promoted. Within the target root, `A VERIFIED ABSENCE`, scope = every Python and configuration file of that root under four declared patterns.

`PC-22` — Retained-earnings carry-forward is a **report-time computation**, defined declaratively: the current year's unallocated result is the income-statement net-result line measured from the start of the fiscal year, plus amounts already booked to the single designated undistributed-result account; prior years are the sum of all revenue and expense balances from inception plus that account's balance, less the current-year figure. `FACT VERIFIED`.

`PC-23` — **The equity section of the balance sheet is derived, not posted.** It follows directly from `PC-21` and `PC-22`. `FACT VERIFIED`.

`PC-24` — Exactly one current-year-result account may exist per company, auto-provisioned on demand with a generated high-numbered code. `FACT VERIFIED`.

`PC-25` — **Consequence for any external consumer.** Because the appropriation is never posted, the ledger of a closed year continues to carry live revenue and expense balances. Any system reading the ledger directly — a warehouse, a statutory export, a third-party consolidation — will not observe the appropriation and must re-implement the report formulas to see it. `SUPPORTED INTERPRETATION`.

## 6. Reopen

`PC-26` — A soft-locked period can be reopened three ways, all requiring the administrator group: permanently by writing an earlier cut-off (which, in the "everyone, forever" form, leaves no exception record); or temporarily for one user; or temporarily for all users. `FACT VERIFIED`.
`PC-27` — An **irrevocably** locked period cannot be reopened by anyone; no override path was found. `FACT VERIFIED` for the three refusal sites; the absence of any other path is `B NOT FOUND IN SEARCHED SCOPE`.
`PC-28` — Reopening leaves **no reopen record**, requires no stated reason, requires no approval, and imposes no obligation to re-close. `FACT VERIFIED`.
`PC-29` — **Reopening does not invalidate issued statements.** Snapshotted figures persist and are explicitly protected from overwrite; nothing marks them stale when the underlying period is reopened and re-posted. The single exception is narrow and tax-only. `FACT VERIFIED`.
`PC-30` — **The one genuinely irreversible control is the entry seal, not the period lock.** A sealed entry cannot be unposted under any circumstance. Period lock and entry seal are complementary: the first makes a span unwritable, the second makes an individual record un-reversible. `FACT VERIFIED`.

## 7. Closing adjustments

`PC-31` — **No adjustment period distinct from the operational months exists, and none is possible**, because no period entity exists. `FACT VERIFIED`, following from `PC-04`.
`PC-32` — Post-close adjustments are made by an accrual routine creating offsetting entries at a user-chosen date against designated deferral accounts in a designated book. The adjustment lands in whatever calendar month its date falls in and is **indistinguishable in the ledger from an operational transaction of that month**; the only separators are the book and the accounts. Entries carry no adjustment marker. `FACT VERIFIED`.
`PC-33` — **The only close-shaped state machine in the system governs the tax return, not the accounting period.** It maintains one unposted return entry per period per registration, dated to the period end, deliberately consuming no number; refuses to proceed if more than one exists; and on posting advances the tax cut-off to its own date and snapshots the return. `FACT VERIFIED`. It is also the benchmark's own demonstration that a period-bound close **can** be a posted, dated, single-instance fact — which is the pattern `P08-RQ-PC-01` asks for.

## 8. Requirements

| ID | Candidate requirement |
|---|---|
| `P08-RQ-PC-01` | A period is a first-class object with state, scoped `COMPANY`. Close is a transition on it, producing a durable artefact naming the closer, the time, the basis and the preconditions satisfied. |
| `P08-RQ-PC-02` | A posting into a closed period is **refused with a named cause**. It is never silently re-dated. |
| `P08-RQ-PC-03` | Close preconditions are enforced uniformly for every close level, not only the irrevocable one, and each refusal routes the operator to the offending records. |
| `P08-RQ-PC-04` | Reopen is a governed event with its own authority, its own artefact and a required reason. Granting and revoking a derogation require **different** authorities. |
| `P08-RQ-PC-05` | Every derogation produces a record. There is no configuration of a derogation that produces none — and the widest grant produces the most evidence, not the least. |
| `P08-RQ-PC-06` | Issuing a statement is itself a fact. Reopening a period after issuance marks every statement issued from it as superseded. |
| `P08-RQ-PC-07` | Whether the year-end result is posted or derived is a `BOSS CONTROLLED DECISION` — `P08-BD-06`. It determines whether a year can be reopened at all. No reference implementation exists either way. |
| `P08-RQ-PC-08` | One fiscal-calendar definition, at `COMPANY` scope, consulted identically by numbering and by reporting. |
