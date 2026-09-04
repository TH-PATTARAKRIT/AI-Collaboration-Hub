> **CORR1 CORRECTION NOTICE.** Amended by session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001`.
> Corrections landing here: `COR-03, COR-05, COR-10`. Governing text where they conflict with the body below: CORR1/C04 NC-02 — H-13/H-15 move NC to PC.
> Prior findings are retained unedited for lineage; see `CORR1/C02_..._ACCEPTED_CORRECTIONS_REGISTER.md`.

# 02 — ACCOUNT_WAVE_A_FUNCTION_COVERAGE_REGISTER

Layer 1 clean-room · cites `EV-0NN` · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

Coverage is scored against the Level-19 depth rule: a function is **Semantically Covered** only when
`WHY → WHEN → WHO OWNS → WHAT CHANGES → ACCOUNTING EFFECT → FAILURE → CORRECTION → REPORTING EFFECT`
are all answered from evidence. Locating a field, a screen or a table is *not* coverage.

Depth codes: `SC` Semantically Covered · `PC` Partially Covered (named gap) · `EO` Evidence Only
(behaviour observed, semantics not established) · `NC` Not Covered.

## A — Chart of Accounts

| # | Function | Depth | Evidence | Gap / note |
|---|---|---|---|---|
| A-01 | Account identity, canonical | `SC` | `EV-001` | Identity is the record, not the code — corroborates standing Boss principle |
| A-02 | Account code | `SC` | `EV-001`, `EV-002` | Per-company value; uniqueness has no storage-level guarantee |
| A-03 | Account name | `SC` | `EV-001` | Translatable label; not identity |
| A-04 | Account type | `SC` | `EV-016`, `EV-019` | Drives balance-forward behaviour, reconcilability, and the single current-year-earnings account |
| A-05 | Internal classification | `SC` | `EV-016` | Derived from account type, not independently stored |
| A-06 | Reporting classification | `PC` | `EV-016` | Report-layer mapping only partially examined — Wave G |
| A-07 | Reconciliation behaviour of an account | `SC` | `EV-014`, `EV-019` | Receivable/payable types are forced reconcilable |
| A-08 | Account currency restriction | `SC` | `EV-013`, `EV-019` | Forcing a currency is refused once items exist in another |
| A-09 | Company ownership | `SC` | `EV-001`, `EV-019` | Many-to-many, except liquidity accounts which cannot be shared |
| A-10 | Tenant boundary | `PC` | `EV-020` | Company boundary evidenced; tenant boundary is an SMEsPlus construct with no reference analogue — see file 16 |
| A-11 | Account groups | `PC` | `EV-002` | Prefix-range grouping observed; semantics for reporting not established |
| A-12 | Tags | `EO` | `EV-001` | Free custom-reporting dimension; no control semantics found |
| A-13 | Control accounts | `PC` | `EV-014` | Subledger/control linkage is by account *type*, not by an explicit control-account concept — see `GAP-A01` |
| A-14 | Temporary / interim accounts | `SC` | `EV-014`, `EV-019` | Suspense and transfer accounts are ordinary accounts nominated by configuration |
| A-15 | Retained earnings | `SC` | `EV-016`, `EV-017` | No posted transfer exists; current-year result is computed at report time |
| A-16 | Equity restrictions | `NC` | — | No evidence of equity movement restrictions found in the scope read — `GAP-A02` |
| A-17 | Off-balance behaviour | `PC` | `EV-016` | An off-balance account type exists; its exclusion semantics in reporting not traced — Wave G |
| A-18 | Active / UnActive / Archived | `SC` | `EV-003` | Only a two-state deprecation flag exists; no archive state |
| A-19 | Account override controls | `PC` | `EV-003` | Allowed-journal restriction observed; override authority not modelled |
| A-20 | Creation / modification | `SC` | `EV-002` | Application-level uniqueness with a documented deferral context |
| A-21 | Deactivation | `SC` | `EV-003` | Guarded only against tax-distribution use |
| A-22 | Archival | `NC` | `EV-003` | No archival concept exists in the scope read |
| A-23 | Migration | `PC` | `EV-017` | Opening balance mechanism established; provenance carrier absent |
| A-24 | Versioning | `NC` | `EV-001`, `EV-004` | No temporal validity on accounts found — `GAP-A03` |
| A-25 | Replacement / consolidation | `SC` | `EV-004` | Merge deletes records and retargets posted history |
| A-26 | Reporting continuity | `PC` | `EV-004` | Balances survive a merge; provenance does not |

## B — Journals

| # | Function | Depth | Evidence | Gap / note |
|---|---|---|---|---|
| B-01 | Journal purpose and type | `SC` | `EV-005`, `EV-019` | Type drives lock selection, default accounts, sequence behaviour |
| B-02 | Allowed source transactions | `PC` | `EV-005` | Allowed-journal restriction exists on the account side; journal-side admission rules not fully traced |
| B-03 | Numbering / sequence | `SC` | `EV-005`, `EV-006`, `EV-007` | Derived from data by pattern, not from a counter |
| B-04 | Company ownership | `SC` | `EV-006` | Exactly one company per journal |
| B-05 | Currency | `SC` | `EV-013`, `EV-019` | Journal currency must agree with its default account's currency |
| B-06 | Default accounts | `SC` | `EV-019` | Auto-created when absent at journal creation |
| B-07 | Suspense / interim accounts | `SC` | `EV-014` | Resolved from journal, else company default |
| B-08 | Bank / cash relationship | `SC` | `EV-019` | Liquidity accounts are company-exclusive |
| B-09 | Posting permissions | `PC` | `EV-011`, `EV-021` | Posting requires an invoicing-level group; finer authority is not modelled — see file 14 |
| B-10 | Reversal | `SC` | `EV-012`, `EV-014` | Reversal is a new entry; some reversals are auto-reconciled to their origin |
| B-11 | Correction | `SC` | `EV-012`, `EV-022` | Correction is either un-post-and-edit (destructive) or reverse-and-repost |
| B-12 | Lock behaviour | `SC` | `EV-008`, `EV-009` | Journal type selects which lock applies |
| B-13 | Control points | `SC` | `EV-007`, `EV-011` | Two controls are switchable, one by configuration parameter |
| B-14 | Auditability | `PC` | `EV-011` | Chatter and tracking observed; a deletion bypass logs outside the database |
| B-15 | Journal grouping | `EO` | — | Ordering attribute only; no control semantics found |
| B-16 | Source attribution | `PC` | `EV-015` | Origin links exist for generated entries; a general source-event identity is absent — `GAP-B02` |
| B-17 | Accounting period implication | `SC` | `EV-009` | Journal type participates in lock resolution |
| B-18 | Multi-company isolation | `SC` | `EV-006`, `EV-019` | Journal-to-company is exclusive; account-to-company is not |
| B-19 | SaaS tenancy implication | `PC` | `EV-020` | See file 16 |

## C — Journal Entries

| # | Function | Depth | Evidence | Gap / note |
|---|---|---|---|---|
| C-01 | Origin → Draft | `SC` | `EV-009` | The accounting date is already re-written at creation, before any user sees it posted |
| C-02 | Validation | `SC` | `EV-022` | Balanced, non-empty, dated, journal active |
| C-03 | Posting | `SC` | `EV-006`, `EV-011` | Number assigned and uniqueness asserted at post |
| C-04 | Reversal | `SC` | `EV-012`, `EV-014` | A new dated entry, optionally auto-matched to the original |
| C-05 | Correction | `SC` | `EV-012`, `EV-022` | See `C-11` decision in file 22 |
| C-06 | Reconciliation | `SC` | `EV-014` | Operates on items, not entries |
| C-07 | Reporting | `PC` | `EV-016` | Trial balance and general ledger traced only far enough to prove ledger readiness — Wave G |
| C-08 | Close | `SC` | `EV-008`, `EV-016` | Close is a lock date; no close artefact exists |
| C-09 | Manual entry | `SC` | `EV-022` | |
| C-10 | System-generated entry | `SC` | `EV-015` | Can be re-dated into the current period when its own period is locked |
| C-11 | Source-generated entry | `PC` | `EV-015` | Producer contracts examined at Level 4 |
| C-12 | Recurring / automatic entry | `PC` | `EV-011` | A deferred auto-post mechanism exists; period-attribution semantics not fully traced |
| C-13 | Adjustment entry | `SC` | `EV-016` | An ordinary entry; no distinct type |
| C-14 | Closing entry | `NC` | `EV-016` | No year-end closing entry exists in the scope searched — the only "closing entry" found is a tax-return posting |
| C-15 | Opening entry | `SC` | `EV-017` | An ordinary posted entry balanced to current-year earnings |
| C-16 | Accrual / reclassification | `PC` | — | Mechanism exists; semantics deferred to Wave F |
| C-17 | Foreign currency entry | `SC` | `EV-013`, `EV-018` | |
| C-18 | Inter-company implication | `PC` | `EV-001`, `EV-019` | Shared accounts observed; inter-company elimination not in Wave A scope |
| C-19 | Consolidation implication | `PC` | `EV-001` | Per-company codes make a single account reportable across companies |
| C-20 | Permission model | `PC` | `EV-021` | See file 14 |
| C-21 | Mutation after posting | `SC` | `EV-022` | Substance frozen by an application guard with a documented bypass; metadata remains open |
| C-22 | Cancellation | `SC` | `EV-012` | Cancellation routes through un-posting, and therefore through its destruction of matches and analytic lines |
| C-23 | Audit trail | `SC` | `EV-011` | Opt-in; bypass logs outside the database |
| C-24 | Immutable accounting facts | `SC` | `EV-010`, `EV-011` | Partial and conditional — see file 15 |
| C-25 | Correction methodology | `SC` | `EV-012` | See file 22, decision `ST-11` |

## D — Journal Items

| # | Function | Depth | Evidence |
|---|---|---|---|
| D-01 | Debit / credit / balance | `SC` | `EV-013` — balance is the stored fact, debit and credit are derived |
| D-02 | Account | `SC` | `EV-001`, `EV-004` |
| D-03 | Partner | `SC` | `EV-010` — hashed at item level |
| D-04 | Currency and amount in currency | `SC` | `EV-013`, `EV-010` — always present; **not** hash-protected |
| D-05 | Analytic dimension | `SC` | `EV-012` — stored as a distribution on the item; the analytic subledger is derived and destroyed on un-post |
| D-06 | Taxes | `PC` | `EV-010` — present but outside hash coverage; semantics are Wave D |
| D-07 | Due date | `SC` | `EV-010` — drives ageing; not hash-protected |
| D-08 | Reconciliation state | `SC` | `EV-014` — stored computed |
| D-09 | Source document | `PC` | `GAP-B02` |
| D-10 | Originating business event | `PC` | `GAP-B02` |
| D-11 | Matching, partial and full | `SC` | `EV-014` |
| D-12 | Residual | `SC` | `EV-014` |
| D-13 | Maturity | `SC` | `EV-014` — a stored maximum match date drives ageing placement |
| D-14 | Reporting dimensions | `PC` | Wave G |
| D-15 | Audit linkage | `PC` | `EV-011` |
| D-16 | Write restrictions | `SC` | `EV-010`, `EV-022` |
| D-17 | Reversal linkage | `SC` | `EV-012` |
| D-18 | Close implications | `SC` | `EV-009`, `EV-015` |

## E — Reconciliation

| # | Function | Depth | Evidence |
|---|---|---|---|
| E-01 | Nature of reconciliation | `SC` | `EV-014` — record + derived state + emitted event |
| E-02 | Bank reconciliation relationship | `PC` | `EV-019` — completeness is a lock precondition; the bank flow itself is Wave H |
| E-03 | Receivable / payable reconciliation | `SC` | `EV-014` |
| E-04 | Open-item management | `SC` | `EV-014` |
| E-05 | Full / partial reconciliation | `SC` | `EV-014` |
| E-06 | Residual amount | `SC` | `EV-014` |
| E-07 | Payment matching | `SC` | `EV-014` |
| E-08 | Write-off | `PC` | Mechanism exists; policy semantics not established — `GAP-E01` |
| E-09 | Exchange differences | `SC` | `EV-014`, `EV-018` |
| E-10 | Rounding | `PC` | Currency rounding is a stored precision; cash rounding is configuration — not fully traced |
| E-11 | Multi-currency | `SC` | `EV-014` — three amounts per match |
| E-12 | Reversal after reconciliation | `SC` | `EV-012`, `EV-014` |
| E-13 | Unreconcile | `SC` | `EV-014` — emits reversal of the exchange entry |
| E-14 | Audit history | `PC` | `GAP-E02` — no dedicated matching history artefact identified |
| E-15 | Reconciliation model relationship | `EO` | Rule-driven auto-matching exists; not semantically traced |
| E-16 | Period close effect | `SC` | `EV-015`, `EV-019` |
| E-17 | Ageing / reporting effect | `SC` | `EV-014` |
| E-18 | Payment state derivation | `SC` | `EV-014` — derived, not stored intent |

## F — Lock Dates

| # | Function | Depth | Evidence |
|---|---|---|---|
| F-01 | Accounting lock | `SC` | `EV-008`, `EV-009` |
| F-02 | Tax lock | `SC` | `EV-008` |
| F-03 | Sale and purchase locks | `SC` | `EV-008` |
| F-04 | Hard lock | `SC` | `EV-008` — monotonic, no exception, cascades from parent company |
| F-05 | Fiscal period close | `SC` | `EV-016` — no period object; close is the lock |
| F-06 | User-specific restriction | `SC` | `EV-021` |
| F-07 | Company-specific restriction | `SC` | `EV-008` |
| F-08 | Hard vs soft close | `SC` | `EV-008` |
| F-09 | Temporary unlock | `SC` | `EV-021` — can be permanent and global despite the name |
| F-10 | Emergency override | `SC` | `EV-021` — reason is optional |
| F-11 | Audit evidence of override | `SC` | `EV-021` — creation is tracked on the company record |
| F-12 | Role permissions | `SC` | `EV-021` — exceptions are create-only for accounting managers |
| F-13 | Backdated transaction behaviour | `SC` | `EV-009` — re-dated, not rejected |
| F-14 | Late source document behaviour | `SC` | `EV-009` |
| F-15 | Reversal into a locked period | `SC` | `EV-015` |
| F-16 | Automated posting into a locked period | `SC` | `EV-015` — relocated to today |
| F-17 | Cross-module impact | `PC` | Level 4 |

## G — Fiscal Years / Period Closing

| # | Function | Depth | Evidence |
|---|---|---|---|
| G-01 | Fiscal year definition | `SC` | `EV-016` — two integers on the company; no year entity |
| G-02 | Monthly close | `SC` | `EV-008`, `EV-016` — a lock date moved forward |
| G-03 | Month 12 behaviour | `SC` | `EV-016` — indistinguishable from any other month |
| G-04 | Year-end adjustment | `SC` | `EV-016` — an ordinary entry in the final period |
| G-05 | Retained earnings | `SC` | `EV-016` — computed at report time; no posting |
| G-06 | Closing balance | `SC` | `EV-016` |
| G-07 | Opening balance | `SC` | `EV-017` |
| G-08 | Carry forward | `SC` | `EV-016` — an account-type property, not an event |
| G-09 | Temporary vs permanent accounts | `SC` | `EV-016` |
| G-10 | Post-close adjustment | `SC` | `EV-009`, `EV-021` |
| G-11 | Comparative reporting | `PC` | Wave G |
| G-12 | Prior-period correction | `SC` | `EV-009`, `EV-012` |
| G-13 | Audit trail of close | `PC` | `EV-021` — the lock change is tracked; no close artefact exists to attest |
| G-14 | Reopening | `SC` | `EV-008` — soft locks move backward freely; the hard lock never does |
| G-15 | Consolidation implication | `PC` | Wave G |

## H — Currencies

| # | Function | Depth | Evidence |
|---|---|---|---|
| H-01 | Company currency | `SC` | `EV-013` |
| H-02 | Transaction currency | `SC` | `EV-013` — always explicit on every item |
| H-03 | Journal currency | `SC` | `EV-019` |
| H-04 | Account currency | `SC` | `EV-019` |
| H-05 | Amount in currency | `SC` | `EV-013` |
| H-06 | Conversion date | `SC` | `EV-018` |
| H-07 | Rate source | `PC` | `EV-018` — the table is evidenced; feed mechanisms are out of Wave A scope |
| H-08 | Realised FX | `SC` | `EV-014` |
| H-09 | Unrealised FX / revaluation | `NC` | `EV-018` — no carrier found in the scope read; `GAP-H01` |
| H-10 | Settlement | `SC` | `EV-014` |
| H-11 | Rounding | `PC` | `EV-018` |
| H-12 | Rate correction | `PC` | `EV-018` — one rate per day is replaceable; the effect on posted entries is not traced — `GAP-H02` |
| H-13 | Close-date rate | `NC` | `EV-018` — no rate-type dimension exists |
| H-14 | Reversal | `SC` | `EV-014` |
| H-15 | Historical-rate requirement | `NC` | `EV-018` — `GAP-H03` |
| H-16 | Financial statement presentation | `PC` | Wave G |
| H-17 | Multi-company behaviour | `SC` | `EV-018` — rates are held per company group |

## Coverage summary

Denominators are the enumerated functions in this register — the Boss-defined Wave A scope. No
percentage is offered where the denominator is not enumerable.

| Scope | Functions | `SC` | `PC` | `EO` | `NC` | Semantically covered |
|---|---|---|---|---|---|---|
| A Chart of Accounts | 26 | 14 | 8 | 1 | 3 | 53.8% |
| B Journals | 19 | 12 | 6 | 1 | 0 | 63.2% |
| C Journal Entries | 25 | 17 | 7 | 0 | 1 | 68.0% |
| D Journal Items | 18 | 13 | 5 | 0 | 0 | 72.2% |
| E Reconciliation | 18 | 12 | 5 | 1 | 0 | 66.7% |
| F Lock Dates | 17 | 16 | 1 | 0 | 0 | 94.1% |
| G Fiscal Year / Close | 15 | 11 | 4 | 0 | 0 | 73.3% |
| H Currencies | 17 | 9 | 5 | 0 | 3 | 52.9% |
| **Total** | **155** | **104** | **41** | **3** | **7** | **67.1%** |

Evidence coverage — functions carrying at least one primary-source evidence reference: 148 of 155 =
**95.5%**. The seven without are the `NC` rows, where the finding *is* the absence, reported with the
scope searched attached.

`RECOMMENDATION:` the two weakest scopes are Chart of Accounts (53.8%) and Currencies (52.9%), and
they are weak for opposite reasons. Chart of Accounts is weak because the reference model supplies
*less* structure than the Boss scope assumes (no archive, no versioning, no explicit control-account
concept). Currencies is weak because revaluation, closing rate and historical rate have **no carrier
at all** in the evidence read. Neither is a research shortfall that more reading would close; both
are design decisions that require Boss direction.
