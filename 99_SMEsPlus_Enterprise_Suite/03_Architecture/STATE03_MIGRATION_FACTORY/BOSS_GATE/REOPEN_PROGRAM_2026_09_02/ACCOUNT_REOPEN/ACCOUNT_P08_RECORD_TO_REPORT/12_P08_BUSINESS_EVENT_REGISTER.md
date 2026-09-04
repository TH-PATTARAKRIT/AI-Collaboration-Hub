# P08_BUSINESS_EVENT_REGISTER

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1

## 1. Scope of this register

P08 owns the ledger, not the producing processes. This register therefore enumerates the **business events that reach the ledger**, names their owning process, and states what the ledger requires of each. The posting pattern of each event — which accounts, which side — belongs to the owning process and is **not** stated here. Filling it from convention would convert inference into apparent fact and would pre-empt the owning process's gate.

## 2. The producer denominator

| Element | Value |
|---|---|
| POPULATION | modules in the target root that create journal entries |
| PATTERN | as declared in `06_P08_SOURCE_TO_GL_TRACE.md` §2 |
| PATH SET | the target root's addon tree |
| UNIT | one module |
| DENOMINATOR | **18 of 790**, a **floor** by declared pattern-boundedness |

## 3. Business events reaching the ledger

| ID | Business event | Owning process | Ledger contract |
|---|---|---|---|
| `BE-01` | Customer invoice issued | P02 Order-to-Cash | creates a receivable open item; sets the settlement anchor |
| `BE-02` | Customer credit note issued | P02 | creates an offsetting receivable open item |
| `BE-03` | Customer payment received | P02 / P06 | settles receivable open items; may emit a difference event |
| `BE-04` | Supplier invoice received | P01 Procure-to-Pay | creates a payable open item |
| `BE-05` | Supplier credit note received | P01 | creates an offsetting payable open item |
| `BE-06` | Supplier payment made | P01 / P06 | settles payable open items; may emit a difference event |
| `BE-07` | Goods received / issued, valuation movement | P03 Manufacture-to-Cost | valuation postings; the inventory-to-ledger handoff |
| `BE-08` | Cost of sales recognised | P03 | recognition postings |
| `BE-09` | Production order completed | P03 | work-in-progress and variance postings |
| `BE-10` | Asset acquired | P04 Acquire-to-Retire | capitalisation posting |
| `BE-11` | Depreciation charged | P04 | periodic charge |
| `BE-12` | Asset disposed | P04 | derecognition and gain/loss |
| `BE-13` | Employee expense claimed and settled | P05 Expense-to-Pay | payable and settlement |
| `BE-14` | Payroll posted | P05 | payroll postings |
| `BE-15` | Bank statement line matched | P06 Bank-to-Reconcile | settles items; clears the suspense leg |
| `BE-16` | Batch payment issued / rejected | P06 | settlement and reversal |
| `BE-17` | Tax return posted | P07 TH Tax Compliance | the only period-bound close-shaped posting in the benchmark; advances the tax cut-off |
| `BE-18` | Withholding tax deducted and certified | P07 | deduction posting; certificate lineage |
| `BE-19` | Loan drawn / repaid / accrued | P08 (accounting-internal) | schedule postings |
| `BE-20` | Deferred revenue or cost released | P08 (accounting-internal) | periodic release |
| `BE-21` | Point-of-sale session closed | P02 | aggregate session postings |
| `BE-22` | Intercompany counterpart document created | P01 / P02 boundary | a document appearing in another company's books without that company's action |
| `BE-23` | Opening balance loaded | migration track | the only posting with no business event behind it |

Twenty-three events, of which **P08 owns two outright** (`BE-19`, `BE-20`), **shares one with the migration track** (`BE-23`, whose ledger form P08 owns and whose data P08 does not), and owns **the ledger contract for the other twenty**. *(Corrected after independent review, which found this file assigning `BE-23` to the migration track in one column and to P08 in the next sentence.)*

## 4. What the ledger requires of every producer

| ID | Requirement on the producing process |
|---|---|
| `BE-RQ-01` | Supply an **event identity** that is unique and derivable, so that the same business fact cannot be posted twice undetected. |
| `BE-RQ-02` | Supply the **recognition point** — the moment the accounting consequence is asserted — distinct from both the document date and the posting date. |
| `BE-RQ-03` | Supply the **rule version** under which the posting instruction was evaluated. |
| `BE-RQ-04` | Supply the **actor**, as a real identity. A system identity is acceptable only where the process genuinely has no human trigger, and must be named as such. |
| `BE-RQ-05` | Supply the **owning company**, and the tenant that owns that company. |
| `BE-RQ-06` | Where a measurement is required, supply it **complete** — rate, date, source, type — or accept refusal. |
| `BE-RQ-07` | Accept that a posting into a closed period is **refused**, and handle the refusal in the process rather than relying on the ledger to relocate the date. |
| `BE-RQ-08` | Correct only by **new fact**. No producer may edit, unpost or delete a posted fact. |

`BE-RQ-01` through `BE-RQ-04` are the four the benchmark supplies for **none** of the twenty-three events, because the carriers do not exist.

## 5. Peer dependencies

Every row above whose owning process is P01–P07 or P09–P10 is a `PEER DEPENDENCY OPEN`. P08 records the ledger contract and does not wait. See `18_P08_DEPENDENCY_REGISTER.md`.
