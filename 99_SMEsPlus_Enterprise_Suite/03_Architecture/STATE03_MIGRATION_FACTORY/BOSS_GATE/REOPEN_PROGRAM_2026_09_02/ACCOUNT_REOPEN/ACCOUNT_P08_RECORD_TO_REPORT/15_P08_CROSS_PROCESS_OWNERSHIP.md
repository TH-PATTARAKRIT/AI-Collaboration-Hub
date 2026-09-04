# P08_CROSS_PROCESS_OWNERSHIP

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1 · scope model per `SMEPLUS-26-09-04-ACC-REV2-CORR1`

## 1. The process series as it stands at P08's close

| Process | Name | Execution branch | Committed output at P08 close |
|---|---|---|---|
| P01 | Procure-to-Pay | `research/account-p01-procure-to-pay-2026-09-04-001` | none |
| P02 | Order-to-Cash | `research/account-p02-order-to-cash-2026-09-04-001` | none |
| P03 | Manufacture-to-Cost | `research/account-p03-manufacture-to-cost-2026-09-04-001` | none |
| P04 | Acquire-to-Retire | `research/account-p04-acquire-to-retire-2026-09-04-001` | none |
| P05 | Expense-to-Pay | `research/account-p05-expense-to-pay-2026-09-04-001` | none |
| P06 | Bank-to-Reconcile | `research/account-p06-bank-to-reconcile-2026-09-04-001` | none |
| P07 | TH Tax Compliance | `research/account-p07-th-tax-compliance-2026-09-04-001` | none |
| **P08** | **Record-to-Report** | `research/account-p08-record-to-report-2026-09-04-001` | **this package** |
| P09 | Plan-to-Analyze | `research/account-p09-*` | none |
| P10 | — | not observed at P08 close | — |
| P11 | Cross-process reconciliation | not observed at P08 close | — |

`FACT VERIFIED` at P08 bootstrap: every peer branch existed with no commit beyond the canonical tip. P08 therefore **records the interface and does not wait**, per the correction's cross-process rule.

## 2. What P08 owns

| Owned by P08 | Not owned by P08 |
|---|---|
| the accounting kernel — event, instruction, entry, item, settlement, period, statement | any producer's posting pattern (debit/credit per business event) |
| chart-of-accounts semantics and account identity | tax computation and tax reporting semantics — P07 |
| the posting engine and its controls | asset lifecycle — P04 |
| period, lock, close, reopen | bank statement flow and payment instruments — P06 |
| reconciliation as a ledger mechanism | inventory valuation method — P03 |
| currency and measurement **as applied to a posting** | procurement and sales document lifecycle — P01/P02 |
| the statement layer and its derivability | analytic/management accounting — P09 |
| the ledger contract every producer must satisfy | cross-process reconciliation of scope semantics — P11 |

## 3. The ledger contract — P08's outbound obligation to every peer

Stated once, in `12_P08_BUSINESS_EVENT_REGISTER.md` §4 as `BE-RQ-01`..`BE-RQ-08`. Every peer process must satisfy all eight. Four of them (`BE-RQ-01`..`04`) cannot be satisfied against the benchmark, because the carriers do not exist — which is why `K2` and `K3` of the kernel model are the highest-leverage single change in the whole package.

## 4. Handoff elements P08 requires from peers

| ID | From | Element | State |
|---|---|---|---|
| `XP-01` | P01, P02 | the recognition point for each document event, distinct from document date and posting date | `PEER DEPENDENCY OPEN` |
| `XP-02` | P03 | the valuation-to-ledger handoff: what is a ledger fact and what is an inventory fact | `PEER DEPENDENCY OPEN` — and see the prior programme's unresolved COGS dependency |
| `XP-03` | P04 | the depreciation charge's period attribution rule, and the day-convention question already recorded in the Asset track | `PEER DEPENDENCY OPEN` |
| `XP-04` | P05 | whether an expense claim's ledger effect is owned by the claimant's company or the paying company | `PEER DEPENDENCY OPEN` |
| `XP-05` | P06 | the settlement event's own date — P08 requires one and the benchmark has none | `PEER DEPENDENCY OPEN` |
| `XP-06` | P07 | the tax point, as a carrier distinct from the accounting date; and every statutory statement layout | `PEER DEPENDENCY OPEN` + `HOLD / EVIDENCE REQUIRED` for the statutory half |
| `XP-07` | P09 | whether an analytic dimension is a fact or an attribution — this decides membership of the immutable core | `PEER DEPENDENCY OPEN`, and `P08-BD-09` |
| `XP-08` | P01/P02 boundary | whether intercompany settlement within one tenant is in scope, and which company owns the matching record | `PEER DEPENDENCY OPEN` |
| `XP-09` | P11 | reconciliation of the `PLATFORM`/`TENANT`/`COMPANY` scope assignments across all processes | `PEER DEPENDENCY OPEN` — P08's assignments are in `01_P08_SCOPE_OWNERSHIP_MATRIX.md` and are offered for that reconciliation |

## 5. Scope assignments P08 offers to P11

P08's full assignment set is `01_P08_SCOPE_OWNERSHIP_MATRIX.md`. The three splits P11 should test hardest, because they are the ones the benchmark does not make and other processes will meet the same way:

1. **Account definition (`TENANT`) versus account number in a set of books (`COMPANY`).**
2. **Rate observation (`PLATFORM`) versus rate policy (`TENANT`) versus rate applied to a posting (`COMPANY`).**
3. **Counterparty master (`TENANT`) versus counterparty as a component of a posted fact (`COMPANY`).**

The third generalises to the rule P08 believes is the single most transferable output of this session:

> **A tenant-scope mutation may never rewrite a company-scope posted fact. It may only add a new company-scope fact.**

Every process will encounter that boundary. P08 recommends P11 adopt it as a cross-process invariant, and records that P08 cannot adopt it on P11's behalf.
