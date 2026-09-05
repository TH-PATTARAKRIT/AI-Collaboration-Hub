# P01 — RECEIPT / LIABILITY / CUT-OFF MODEL

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**

Answers directive §8: does the deployed system have a receipt-to-liability bridge, what owns
it, what creates it, what clears it — and if it has none, how is receive-before-bill
represented?


> ### ⚠ CORRECTED — `ERR-P01-19`
>
> This document previously stated that **no valuation account resolves** in the series-19 estate,
> citing per-category counts of 0 of 37. **That was a false zero.** Company-dependent values also
> resolve from a company-level defaults table, which holds **44 rows for the valuation account,
> 43 carrying a real account** — the account **is** configured.
>
> **The conclusion stands; the cause is different.** The valuation entry takes its journal from
> the **company's stock journal**, which is unset on **44 of 44** companies in that estate — so no
> entry can be created. In the *other* series-19 deployment that journal **is** configured, and
> the absence of entries there is a usage fact, not a configuration one.
>
> Read every "0 of 37" and "no account resolves" statement below as superseded by this note.

---

## 1. THE ANSWER, PER DEPLOYMENT

| | `D3` — v16, operating | `D1` / `D2` — v19, as configured |
|---|---|---|
| Bridge exists? | **Yes** | **No** |
| Owned by | the **item category's** goods-received clearing account | would be the **location's** valuation account — none is set |
| Created by | the goods receipt | nothing |
| Cleared by | the vendor bill, which is silently re-pointed at the same account | nothing |
| Matched by | reconciliation of that account — **only if it is flagged reconcilable** | n/a |
| Evidence it runs | 57,863 valuation layers carry a journal-entry link; 1,267 carry a bill-line link | 0 of 14,441 movements carry a journal-entry link |

---

## 2. HOW RECEIVE-BEFORE-BILL IS REPRESENTED WHERE THERE IS NO BRIDGE

**Operationally only.**

| Layer | State after a receipt in the v19 deployments |
|---|---|
| Quantity | increased |
| Valuation | computed and stored **on the movement** — 3,680 movements carry a value |
| General ledger | **nothing** |
| Balance sheet | **no asset** |
| Liability | **none** |
| Any accrual or clearing balance | **none** |

So the obligation to the vendor and the asset received both come into existence, for accounting
purposes, **only when the vendor bill is posted**.

---

## 3. THE THREE-DAY TEST

Receive day 5 · consume or sell day 6 · vendor bill day 7.

| | `D3` v16 | `D1`/`D2` v19 as configured |
|---|---|---|
| Day 5 | Inventory ↑, clearing obligation ↑ | — |
| Day 6 | Inventory ↓, cost recognised | — |
| Day 7 | Clearing discharged, payable ↑ | Expense or inventory ↑, payable ↑ |
| Ledger position at close of day 6 | asset and obligation both present | **neither present** |
| If the period closes on day 6 | the purchase is in the period the goods arrived | **the purchase is absent from the period in which the goods arrived and were consumed** |

**The last row is a cut-off failure by construction.** It is not caused by late data entry; it
is caused by there being no accounting event at receipt at all.

Classification: **SUPPORTED INTERPRETATION.** It follows necessarily from the verified
configuration and the verified gate, but **has not been executed**. It is the first runtime
test to run.

---

## 4. THE FOUR TRUTHS, AND WHERE EACH LIVES

Directive §24 requires that receipt, bill, liability and journal are not collapsed into one
event. In the v19 deployments they are collapsed — into the bill.

| Fact | Original truth | Where it lives (v16 deployed) | Where it lives (v19 deployed) |
|---|---|---|---|
| A purchase was committed | purchase order | order | order |
| Goods physically arrived | goods receipt | movement + valuation layer | movement only |
| The goods have a value | valuation event | layer, and the ledger | **the movement only — never the ledger** |
| An obligation to the vendor exists | vendor bill | ledger, from receipt onward via clearing | **ledger, from the bill onward only** |
| The obligation is measured | vendor bill | bill | bill |

**Derived vs original:** the payable is *original* truth at the bill in both generations. The
inventory asset is *original* truth at the receipt in v18 and **has no ledger representation at
all** in the v19 deployments. That asymmetry is the finding.

---

## 5. CONSEQUENCES THAT BELONG TO OTHER PROCESSES

Routed, not decided here.

| Consequence | Owner | Route |
|---|---|---|
| Inventory value is absent from the balance sheet between receipt and bill | Inventory + P08 Record-to-Report | `HO-07` |
| Period comparatives are affected by billing latency rather than by activity | **P08** | `HO-08` |
| Any received-not-invoiced report has no ledger source in the v19 deployments | **P08**, P11 | `HO-09` |
| Whether the accrual of received-not-billed belongs to P01 or to P10's accrual kernel | **P10** | `HO-10` — P10 records this as an unassignable boundary and offers two designs; P01 supplies the evidence, not the choice |
| Price-difference account scope | **Inventory ↔ P01**, held open by P11 as `DEP-06` | `HO-11` |
| Landed-cost ownership | **Inventory ↔ P01**, held open by P11 as `DEP-07` with an audit veto retained | `HO-12` |

---

## 6. WHAT THIS MODEL DOES NOT CLAIM

- It does not claim the v19 software cannot bridge. It claims these deployments are not
  configured to, and shows the four unset account populations that cause it.
- It does not claim the v19 deployments are wrong to be configured this way — that is a
  business determination. It claims the configuration is **internally contradictory**, because
  perpetual valuation is declared while no posting destination exists.
- It does not report executed behaviour. Nothing was run.
