# P10 → P06 HANDOFF  (Bank-to-Reconcile — next in G02)

Published, not executed. **P10 does not start, research or open P06.**

---

## 1. What P10 Sends

| # | Item | Evidence | Exact question for P06 |
|---|---|---|---|
| `H06-1` | **Recognition never touches cash.** Every P10 mechanism moves an already-invoiced or already-estimated amount between accounts. **No recognition event is settlement-triggered** | All five mechanisms traced; none reads a payment | Does P06's model need any recognition input at all, or is the interface empty? **P10's position: empty — and it should be confirmed rather than assumed** |
| `H06-2` | **Timing effect on the receivable is nil; on the P&L it is total.** A deferral changes when revenue appears, never when the receivable appears or clears | The deferral pair never touches a receivable or payable account | Does P06 reconcile against invoiced value or recognised value? They diverge for the whole window |
| `H06-3` | **The accrual is the one mechanism with a settlement relationship — and it has no link to its settlement** | The accrual's back-link to its source order is dead code; nothing links the estimate to the invoice that supersedes it | When the real invoice arrives, is detecting the superseded accrual P06's problem or P10's? **P10's position: P10's, and P10 has recorded it as a requirement (`F-05`, `AL-6`)** |
| `H06-4` | **A structural reversal is not a correction** | An accrual's next-day reversal is part of the pattern; a corrective reversal is not. The reference does not distinguish them in the ledger | Does P06's matching logic treat the two the same? If so it will match structural pairs and report them as resolved |

## 2. What P10 Does Not Send

No opinion on settlement, outstanding-account separation, write-off behaviour, or multi-deduction. Those are P02's routings to P06 and P10 has not examined them.

## 3. Bounding

Every statement above is scoped to the declared reference root and to four deployed databases in which **the deferral mechanism has never generated an entry**. P06 must not read any of it as deployed-behaviour evidence.
