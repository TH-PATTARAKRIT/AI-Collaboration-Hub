> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-01, COR-02`. Governing text where they conflict with the body below: CORR1/C07 (dates); CORR1/C04 NC-01 (fiscal year).
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 01 — LEVEL 1: CORE LEDGER & CLOSING DOMAIN SEMANTIC MAP

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001` · Layer 1 clean-room · cites `EV-0NN`

## 1. What the domain is for

Core Ledger & Closing exists to convert **business events that have already happened** into a
**permanent, ordered, provable financial record**, and then to declare periods of that record
finished so they can be reported on and relied upon.

Everything in Wave A serves one of four purposes:

| Purpose | Question it answers | Wave A functions |
|---|---|---|
| **Classification** | Into what bucket does this value go? | Chart of Accounts, account groups, tags, control accounts |
| **Recording** | What exactly happened, when, in what amount, against whom? | Journals, Journal Entries, Journal Items |
| **Settlement** | Is this obligation still outstanding, and by how much? | Reconciliation, residual, matching |
| **Finalisation** | Is this period still changeable? | Lock dates, period close, opening balances, retained earnings |

Currency cuts across all four: it is not a fifth purpose but a qualifier on the other four.

## 2. Actors and ownership

| Actor | Owns | Cannot own |
|---|---|---|
| Bookkeeper / accounting clerk | data entry, draft entries, proposing matches | the decision that a period is closed |
| Accountant / controller | posting authority, corrections, reconciliation decisions, lock dates | their own review |
| Auditor (internal or external) | assurance over the record | any change to the record |
| The system, acting for a source module | machine-generated accounting events | judgement-based classification |
| Boss / final approver | policy: what is immutable, who may override, how corrections occur | routine transactions |

`INFERENCE:` the sharpest ownership question in the domain is not who may post, but **who may
decide that a fact is final**. Wave A evidence shows the reference model devolves that decision to
configuration (`EV-011`) rather than reserving it to a role. That is a design choice SMEsPlus must
make deliberately rather than inherit.

## 3. The seven core concepts and their true nature

### 3.1 Account
An account is a **classification identity** with a lifetime longer than any code or name it wears.
`EV-001` establishes that the reference system itself concluded this: it moved the account code into
per-company storage so that the same account can carry different codes in different companies. The
code is a *label*, resolved in a context; the account is the *thing*.

This corroborates, from independent evidence, the standing Boss-approved principle that Account
Code / Account Name must not become the sole canonical identity.

### 3.2 Journal
A journal is a **numbering and control domain**, not a container. Its real content is: which kinds of
source transaction may enter here, under which number series, under whose posting authority, with
which default and interim accounts, and whether entries booked here are secured (`EV-005`, `EV-011`).
Two journals differ meaningfully only if one of those answers differs.

### 3.3 Journal Entry
A journal entry is the **accounting representation of a business event** — the unit at which the
ledger asserts "this happened, on this date, in this period". It is the unit of posting, numbering,
locking, hashing and reversal. `EV-016` shows the entry is the *only* durable accounting artefact in
the reference model: there is no period object, no year object, no closing artefact. Everything else
is derived from entries.

### 3.4 Journal Item
A journal item is not a child row. It is the **atomic financial fact**: a signed amount, in a stated
currency, against one account, optionally attributed to a counterparty, a due date, and analytic and
tax dimensions. `EV-013` shows the reference model treats the signed company-currency balance as the
stored primary amount and derives debit/credit from it, while carrying the transaction-currency
amount alongside — two amounts, always, with the currency always explicit.

The item is also the **unit of settlement**: reconciliation matches items, not entries (`EV-014`).

### 3.5 Reconciliation
Reconciliation is a **composite**, not a single kind of thing. `EV-014` establishes three
simultaneous natures: a stored matching record between two items; a derived settlement state
(residual, reconciled, matching marker) computed from those records; and a **conditional emitter of
new accounting events** (exchange difference entries, cash-basis tax entries). Unreconciling emits
events too — it is not an undo.

### 3.6 Lock
A lock is a **date, not a period object**. `EV-008` and `EV-016` together establish that "closed"
has no independent existence: a period is closed exactly to the extent that a lock date covers it.
Crucially `EV-009` establishes that a lock **re-dates** a late document rather than rejecting it.

### 3.7 Currency
Currency is a chain of four distinct facts that the domain must keep separate:
transaction fact (what was agreed, in what currency) → currency fact (the rate applied, on what date)
→ valuation fact (the company-currency amount recorded) → settlement fact (what was actually
received or paid, and the difference that arose). `EV-018` shows the reference carrier is one scalar
rate per currency per day per company group, with no rate-type dimension — which is sufficient for
the first three links and insufficient for revaluation and closing-rate presentation.

## 4. Accounting principles the domain represents

| Principle | Where it lives in Wave A | Evidence position |
|---|---|---|
| Double entry | balanced entry invariant | `VERIFIED FACT` that amounts are modelled as signed balance plus derived debit/credit (`EV-013`); **where the balance invariant is enforced is examined at Level 11** |
| Accrual and period attribution | accounting date vs document date | `EV-009` shows these legitimately diverge under lock |
| Historical cost / measurement date | rate applied at transaction date | `EV-018` |
| Realisation | exchange difference on settlement | `EV-014` |
| Matching / open-item management | residual and partial reconciliation | `EV-014` |
| Consistency and comparability | account identity surviving code change | `EV-001`; contradicted by merge behaviour `EV-004` |
| Completeness and non-repudiation | numbering, hashing, audit trail | `EV-005`, `EV-006`, `EV-010`, `EV-011` — all conditional, none unconditional |
| Going-concern period reporting | retained earnings, opening balances | `EV-016`, `EV-017` |

## 5. Source of truth — Level 1 statement

At Level 1 the domain's source-of-truth claim is stated in outline and proved at Level 5:

- The **source document** owns what was agreed with the outside world.
- The **accounting event** owns what the business recognised, and when.
- The **journal entry** is the *representation* of the accounting event — and in the reference model
  it is also, in practice, its only durable record.
- The **journal item** owns the atomic financial fact.
- **Reconciliation records** own settlement.
- Everything else in Wave A — residual, payment state, matching marker, trial balance, current-year
  earnings, ageing — is **derived** and must be reconstructible.

`EV-016` is the sharpest Level 1 result: current-year earnings, which most practitioners think of as
a posted closing entry, is in the reference model a **report-time computation** with no journal
entry behind it at all.

## 6. Relationship to other accounting functions

Wave A is the **consumer of recognition decisions made elsewhere** and the **producer of the record
everything else reads**. It does not decide when revenue is earned, when a cost is incurred, or what
tax is due; it decides how those decisions become permanent, and when they stop being changeable.
Detailed producer/consumer tracing is at Level 4.

## 7. Terminology discipline established for this Wave

| Term | Used in this package to mean | Not to be confused with |
|---|---|---|
| Business event | something that happened in the business | its document |
| Accounting event | the recognition of a business event in the ledger | the entry that represents it |
| Posted | the accounting event is asserted as fact | immutable — `EV-011` shows these differ |
| Locked | dated on or before an effective lock date | closed as a period object — no such object exists (`EV-016`) |
| Closed | a governance state SMEsPlus must define | locked |
| Reconciled | residual is zero and a full match record exists | paid |
| Secured / hashed | covered by a chained integrity hash | complete — `EV-010` shows the coverage is partial |
| Deprecated account | flagged as no longer to be chosen | archived — no archive state exists (`EV-003`) |

## 8. CHECKPOINT L1

| Item | Record |
|---|---|
| Scope completed | Domain purpose, actors, seven core concepts, principles, outline source-of-truth, terminology |
| Evidence inspected | `EV-001`, `EV-003`, `EV-005`, `EV-008`, `EV-009`, `EV-010`, `EV-011`, `EV-013`, `EV-014`, `EV-016`, `EV-017`, `EV-018`; bootstrap layer `EV-023` |
| Verified findings | Account identity is not the code; the journal entry is the only durable accounting artefact; there is no period or year object; reconciliation is a composite; lock re-dates rather than rejects |
| Contradictions | Account identity stability (`EV-001`) versus destructive merge (`EV-004`) — carried to `CONTRA-03` |
| Unknowns | Whether posting to a deprecated account is blocked (`EV-003`); three bootstrap filenames absent (`GAP-B01`) |
| Risks | Terminology conflation of *posted / locked / closed / immutable* is the dominant modelling risk for this Wave |
| Expert disagreements | Deferred to Level 12 consolidation |
| Audit challenges | Independent challenge unit commissioned against the evidence base |
| Next research target | Level 2 — field and configuration forensic |

`CHECKPOINT L1 RECORDED — CONTINUING AUTOMATICALLY.` This checkpoint is not Boss approval.
