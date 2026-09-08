# SA07 — ACCOUNTING RECONCILIATION MATRIX
## CP-SA-50 — ACCOUNTING RECONCILIATION

Status: **HOLD**
Governing law: master prompt §7.2 — every material business flow must reconcile to accounting
semantics. This does **not** mean every flow posts a journal entry; it means the recognition
question must be explicitly answered for every flow, including with "no posting by design".

Governing ruling: **BD-ACC-01** — Source Module owns the Business Fact; Accounting Core owns
the canonical immutable Accounting Event Identity; Posting Engine owns Ledger Posting. Event
identity is distinct from source document number, journal number and reconciliation matching
number. Same-event retry is idempotent. Reversal creates a new event referencing the original.
Identity and posting are Tenant + Company bounded.

---

## 1. Matrix

`REQUIRED` = recognition exists · `NO POSTING BY DESIGN` = deliberate determination that none
arises · `UNKNOWN` = the recognition question cannot be answered on current evidence.

| # | Business flow | Accounting impact | Recognition point | Status |
|---|---|---|---|---|
| AR-01 | Sales delivery of stocked goods | `REQUIRED` — revenue, AR, tax, COGS | delivery / billing per product policy | `RECONCILED` |
| AR-02 | Customer billing | `REQUIRED` — AR, revenue, tax | posting | `RECONCILED` |
| AR-03 | Customer receipt | `REQUIRED` — bank/cash, AR clearing | settlement | `RECONCILED` (P06 `a533fe92`) |
| AR-04 | Purchase receipt | `REQUIRED` — inventory/expense, accrual | receipt | `RECONCILED` |
| AR-05 | Vendor billing | `REQUIRED` — AP, expense/asset/inventory, tax | posting | `RECONCILED` |
| AR-06 | Supplier payment | `REQUIRED` — AP clearing, bank/cash | settlement | `RECONCILED` |
| AR-07 | Commercial commitment (order confirmed, nothing delivered) | **`NO POSTING BY DESIGN`** | — | `RECONCILED` — a commitment is not a transaction; recorded as a determination, not an omission |
| AR-08 | Commercial-terms freeze | **`NO POSTING BY DESIGN`** | — | `RECONCILED` |
| AR-09 | Stock reservation | **`NO POSTING BY DESIGN`** | — | `RECONCILED` — reservation moves no value |
| AR-10 | Internal transfer (same company) | **`NO POSTING BY DESIGN`** under a single valuation policy | — | `PARTIAL` — depends on BD-ACC-03A Periodic vs Perpetual at Product Category |
| AR-11 | Manufacturing consumption + FG receipt | `REQUIRED` — WIP, COGS inputs | production events | `PARTIAL` — fixed-overhead elements have no injection path (P03) |
| AR-12 | Scrap / variance | `REQUIRED` | production close | `PARTIAL` |
| AR-13 | Sales return | `REQUIRED` — reversal event referencing the original, per BD-ACC-01 | return | `RECONCILED — as a ruling` |
| AR-14 | Purchase return | `REQUIRED` — same | return | `RECONCILED — as a ruling` |
| AR-15 | Asset capitalization | `REQUIRED` | posted vendor bill (P04) | `RECONCILED` |
| AR-16 | Depreciation | `REQUIRED` | period | `RECONCILED` |
| AR-17 | Asset derecognition / disposal | `REQUIRED` | disposal | `PARTIAL` — P04 recorded a derecognition-entry defect |
| AR-18 | Employee expense | `REQUIRED` | approval → payable | `PARTIAL` — P05 terminal HOLD |
| AR-19 | Time-based / subscription recognition | `REQUIRED` | schedule period | `PARTIAL` — P10 terminal HOLD; recognition event collapsed into the posting act |
| AR-20 | Period / year close | `REQUIRED` | close | `PARTIAL` — P08 terminal state; no year-close entry recorded in Wave A findings |
| AR-21 | Analytic dimension attribution | `REQUIRED` — dimension, not a separate posting (Boss `fa57d10f`) | at posting | `PARTIAL` — P09 recorded the analytic dimension as schema rather than data |
| AR-22 | Tax determination and register | `REQUIRED`, **Company-scoped** (BD-ACC-02) | posting | `PARTIAL` — P07 terminal HOLD |
| AR-23 | **Sell-side commitment cancellation** | **`UNKNOWN`** — whether an accounting fact blocks it is the open question | — | **`NOT RECONCILED` — `XD-01`** |
| AR-24 | Dropship | **`UNKNOWN`** — title passage without own movement | — | **`NOT RECONCILED`** |
| AR-25 | Kit / bundle | **`UNKNOWN`** — which level carries cost | — | **`NOT RECONCILED`** |
| AR-26 | Service completion | **`UNKNOWN`** — what evidence triggers recognition | — | **`NOT RECONCILED`** |
| AR-27 | Project | **`UNKNOWN`** — derived vs held financial truth | — | **`NOT RECONCILED`** |
| AR-28 | Quality hold | **`UNKNOWN`** — effect on cost recognition timing | — | **`NOT RECONCILED`** |
| AR-29 | Maintenance cost | **`UNKNOWN`** — production cost, period expense, or asset carrying amount | — | **`NOT RECONCILED`** |

### 1.1 Count

| Status | Count | **CORR2** |
|---|---|---|
| `RECONCILED` (incl. `NO POSTING BY DESIGN`) | 13 | **15** |
| `PARTIAL` | 9 | **14** |
| `NOT RECONCILED` (`UNKNOWN`) | 7 | **0** |
| **Total material business flows** | **29** | **29** |

> ### SUPERSEDED BY CORR2 — `SA_CORR2_06` §2.1
> **All seven `UNKNOWN` rows (`AR-23`…`AR-29`) are re-adjudicated. None remains unanswered.**
> Master prompt §7 is satisfied in the sense it requires — every material flow has an explicitly
> determined accounting semantic — which is a weaker claim than *reconciled*, and fourteen carry a
> named open element.

---

## 2. SA07-F-01 — no flow in SMEsPlus is accounting-irrelevant, and four are deliberately non-posting

Four flows are determined `NO POSTING BY DESIGN` (AR-07 to AR-10). Recording them is the point
of §7.2: a blank in an accounting matrix is indistinguishable from an unexamined flow, whereas
a deliberate "no posting arises here, and this is why" is an assurance statement.

## 3. SA07-F-02 — nine `PARTIAL` rows, and every one traces to an already-recorded Phase S terminal state

AR-10, AR-11, AR-12, AR-17, AR-18, AR-19, AR-20, AR-21, AR-22 each carry an open item that its
own Phase S package already recorded and published as a terminal HOLD or defect. **Phase SA is
not discovering these; it is confirming they survived into the cross-module view.**

That distinction matters for the Boss pack: these nine do not need re-research. They need the
dispositions their own packages already requested. Re-opening them would be a reset, which is
prohibited.

## 4. SA07-F-03 — the seven `UNKNOWN` rows are the same seven business natures

~~AR-23 to AR-29 map one-to-one onto the seven `HOLD` business natures … Three instruments … now
agree on the same seven-item set.~~ **WITHDRAWN IN FULL BY CORR2 (`C2-F-16`, `SA_CORR2_06` §1).**

`SA18-F-01` found the three instruments were not independent — all three inherit `SA01`'s
classification and `SA05`'s nature list. **CORR2 found it is worse: they shared an *undeclared
pattern*.** `SA00` §6 states the rule *"MENTION = blob contains any **declared** term"* and the
package declares no term anywhere. **Three registers agreed because they were three views of one
unpublished search.** The seven-item set no longer exists (§1.1 above).

## 5. Accounting event identity — contract status

BD-ACC-01 is a **ruling**, and rulings are not contracts. `SA04` R-20 shows what happens when a
ruling has no contract behind it: Sales needs a customer-invoice lifecycle fact, Accounting owns
it, and no interface publishes it. Phase SA's position is that BD-ACC-01 requires a published
cross-domain contract before Functional Design — carried to `SA17`.

---

`CP-SA-50 — HOLD`. Thirteen of twenty-nine material flows are reconciled to accounting semantics,
nine are partial against already-recorded Phase S positions, and seven are unknown.

Boss remains the sole Final Approver.
