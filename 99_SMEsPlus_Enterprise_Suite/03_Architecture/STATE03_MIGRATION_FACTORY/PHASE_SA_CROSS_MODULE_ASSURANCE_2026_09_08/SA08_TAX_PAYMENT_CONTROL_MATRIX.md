# SA08 — TAX, PAYMENT AND CONTROL MATRIX

Status: **HOLD**
Governing rulings: **BD-ACC-02** — statutory tax is Company-scoped; SMEsPlus performs no
consolidation accounting for statutory tax filing. Multi-company informational reporting may
aggregate without creating cross-company statutory posting, offsetting or filing.

---

## 1. Tax impact by flow

| Flow | Tax impact | Owner | Status |
|---|---|---|---|
| Customer billing | Output tax; Thai VAT register | shared tax engine — **neither commercial module computes tax itself** | `PARTIAL` — P07 terminal HOLD; statutory VAT registers found empty on a Thai-language install |
| Vendor billing | Input tax; withholding where applicable | shared tax engine | `PARTIAL` — P07 recorded Thai withholding implemented twice (P05 lineage) |
| Tax substitution (fiscal position) | Determines which tax applies to which counterparty/place | — | **`EVIDENCE-INSUFFICIENT`** — Group A open item #4, recorded as *a black box in this evidence set* |
| Zero-rated / exempt supply | Determines register placement | — | `PARTIAL` — P07 recorded zero/exempt settling to a withholding group |
| Cross-company transaction | **No cross-company statutory posting, offsetting or filing** (BD-ACC-02) | Company | `RECONCILED — as a ruling` |
| Thai statutory form codes | Statutory correctness | Revenue authority | **`EVIDENCE-INSUFFICIENT`** — Group A open item #18 records that no authoritative government source was consulted |

### SA08-F-01 — the tax determination rule set is the least-owned input on the accounting path

Both commercial modules are evidenced as **not** computing tax; they consume a shared
determination. That is architecturally correct and it means the determination is a single point
of dependence. Its own rule base is recorded as unavailable in one programme and its statutory
currency is unverified in another.

Under BD-ACC-02, tax is Company-scoped — so this single dependence is replicated per Company,
and an error in it is a statutory error, not a reporting error.

**Statutory claims remain `HOLD / EVIDENCE REQUIRED`.** This register makes no claim about Thai
statutory compliance and asserts no certification.

---

## 2. Payment impact by flow

| Flow | Payment impact | Status |
|---|---|---|
| Customer receipt | Bank/cash in; AR clearing | `RECONCILED` (P06 `a533fe92`) |
| Supplier payment | AP clearing; bank/cash out | `RECONCILED` |
| Advance receipt / payment | Controlled advance accounts (Boss decision `e6504225`) | `PARTIAL` |
| Payment batch | Grouped settlement | `PARTIAL` |
| Bank reconciliation | Statement ↔ ledger matching | `PARTIAL` — P06 terminal position: counts reproduced, completeness failed in 5 of 9 classes, independence not provable |
| Petty cash / employee advance | Settlement | `PARTIAL` — P05 recorded both as structurally broken |

Boss decision `e6504225` separates **Finance** (receipts, payments, cash, bank, batches, cash
position) from **General Ledger** (meaning, debit/credit, posting, reconciliation, close) and
from **Invoicing**, and requires the three to be mutually traceable and reconcilable:

> BUSINESS DOCUMENT -> ACCOUNTING POSTING -> MONEY SETTLEMENT -> RECONCILIATION -> FINANCIAL REPORT

**Phase SA position:** this chain is the payment-side statement of BD-ACC-01. It is achievable
only if the Accounting Event Identity is carried on every link — which is `XD-06`, the ruling
without a contract. The traceability requirement and the event-identity contract are the same
obligation seen from two ends, and neither is discharged.

---

## 3. Control and approval impact

| Control | Where enforced | Status |
|---|---|---|
| Buy-side amount-threshold approval | hard, test-confirmed | `ESTABLISHED` |
| Demand-request approval before conversion | hard gate | `ESTABLISHED` |
| Sell-side credit control | **advisory only** | `ESTABLISHED AS A NEGATIVE` — `XD-02` |
| Sell-side availability control | **advisory only** | `ESTABLISHED AS A NEGATIVE` |
| Self-approval exclusion (SoD) | identity-based; requester/approver distinguishable | `ESTABLISHED — as an interface requirement` |
| Rejection with mandatory reason | required output of an approval capability | `ESTABLISHED — as an interface requirement` |
| Record that approval occurred | — | **`NOT EVIDENCED`** — `XD-03`, 0 of 27,874 rows |
| Approval on a cross-module auto-created document | — | **`NOT ESTABLISHED`** — `SA03-F-02` |
| Period lock | — | `PARTIAL` — P04 recorded locked-period entries silently re-dated |

### SA08-F-02 — the four approval interface facts are a usable SMEsPlus contract

Independent re-verification confirmed four facts an approval capability must satisfy,
unchanged through the corrective cycle:

1. the submitted fact — commitment total value, or a configured N-level requirement;
2. the required output — approved/rejected, actor, timestamp, and a mandatory rejection reason;
3. the source-module state/event consequence, designed independently of any engine's internals;
4. the segregation-of-duties requirement — identity-based self-approval exclusion, with
   requester and approver distinguishable.

**Phase SA adopts these four as the SMEsPlus approval contract boundary**, with independent
rationale: they are stated without reference to any engine, they are testable, and item 2 is
precisely the evidence half that `XD-03` shows was never produced in the reference estate.
Adopting item 2 as mandatory is SMEsPlus doing something *differently*, not copying.

---

## 4. Convergence check

Every row in §1 and §2 carries an accounting consequence, consistent with `SA07`. No flow in
this matrix is left with a blank tax or payment determination; where the answer is unknown it
is written `EVIDENCE-INSUFFICIENT` and routed, not left empty.

---

`SA08 — HOLD`. Tax determination carries two evidence-insufficient inputs and no statutory
claim is made. Payment traceability depends on the same undischarged contract as `XD-06`. The
approval contract boundary is adopted; the evidence half of approval is unestablished.

Boss remains the sole Final Approver.
