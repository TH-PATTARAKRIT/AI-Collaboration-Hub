# P01 — SOURCE TO ACCOUNTS PAYABLE TRACE

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

The question `§2.12` demands: **what business event created the financial fact?**
This document answers it for every payable that P01 can produce.

---

## 1. THE ONE PATH FOUND THAT CREATES A PAYABLE

```
Vendor Bill posting
    → Payable recognised
```

Nothing else in the searched scope creates a trade payable to a vendor. Order confirmation
does not (`EV-P01-01`). Goods receipt does not — it creates a *clearing* obligation, which is
an internal bridge, not a vendor payable (`EV-P01-07`).

Classification: **FACT VERIFIED**, scope = journal-entry creation-site population C over `R1`
(declared in the evidence base §2.3, with its false-negative modes). Negative claim class
**B** for "no other path exists": the population is a floor, not a total.

---

## 2. WHAT THE PAYABLE IS OFFSET AGAINST

The offset differs by item shape. This is the crux of P01 and the reason the same document
type cannot be reasoned about as a single accounting pattern:

| Offset | When | Meaning |
|---|---|---|
| Goods-Received Clearing | storable + continuous valuation + clearing model | the bill *discharges* an obligation that receipt already raised |
| Item Expense | anything else | the bill *creates* the cost for the first time |
| Asset | bill line's ledger account carries the asset flag | the bill *capitalises* |

---

## 3. THE BRIDGE, AND HOW IT CAN FAIL SILENTLY

For the clearing case the bridge closes by matching the receipt's credit against the bill's
debit in the clearing account. Three failure modes were verified:

| # | Failure | Symptom | Evidence |
|---|---|---|---|
| F1 | The clearing account is not flagged as reconcilable | Receipt and bill both post there and are never matched. The balance grows. **No error is raised.** | `EV-P01-10` |
| F2 | The item has no expense account | Price difference on already-consumed quantity is **not posted at all**. Value silently disappears. | `EV-P01-14` |
| F3 | The storage location carries an account override | Two receipts of the same item credit two different accounts; the bill debits only the category account | `EV-P01-07` |

F1 and F2 are **silent**: nothing in the observed code writes a warning, raises an exception,
posts to a suspense account, or flags the document.

---

## 4. THE PRICE-DIFFERENCE MATCHING RULE — AND ITS DEPENDENCY ON A NON-ACCOUNTING RECORD

To decide which receipt layer a bill line settles, the engine replays the history of the
order line's receipts and bills, ordered by **the audit-log tracking entries of each bill's
status field**, falling back to the record's creation timestamp where no tracking entry
exists. `EV-P01-13`.

Consequences, stated plainly:

1. **The financial result depends on data that is not an accounting record.** Audit-log
   tracking rows are housekeeping; they are routinely vacuumed, they can be disabled, and they
   are not covered by any accounting control.
2. **Migrated history has none of them.** Every imported bill falls to the creation-timestamp
   branch. A migration that reproduces documents faithfully can still reproduce *different*
   valuation outcomes from the same documents.
3. **It is not reproducible from the documents alone.** Two systems holding identical orders,
   receipts and bills can compute different layer matching.

Classification: **FACT VERIFIED**, scope `R1`. This is the strongest single argument in this
package for **not** transferring the reference pattern.

**Cross-generation note:** the routine containing this engine is 358 lines in `R1` and 33
lines in `R3`; the replay engine, the interim-account override and the interim reconciliation
are absent from the corresponding `R3` files. `EV-P01-25`. The vendor did not merely refactor
it — the whole approach changed between the two generations present in this workspace.

---

## 5. THE PAYABLE'S SETTLEMENT

| Step | Effect | Condition |
|---|---|---|
| Payment created | **no accounting effect** unless an outstanding-payments account is configured (`EV-P01-20`) | conditional |
| Payment posted | Payable debited, Outstanding Payments credited | as above |
| Bank statement matched | Outstanding Payments cleared to Bank | — |
| Reconciliation | Payable extinguished; **FX difference recognised here, at settlement** (`EV-P01-21`) | multi-currency |

---

## 6. TRACE INTEGRITY: CAN THE PAYABLE BE TRACED BACK TO ITS BUSINESS EVENT?

| From | To | Traceable? | Note |
|---|---|---|---|
| Payable line | Vendor bill | Yes | same document |
| Bill line | Order line | Yes | explicit link |
| Bill line | Receipt / valuation layer | **Indirectly** | via the order line and the replay engine, not by a direct link |
| Bill line | The specific receipt it settles | **Not from the documents alone** | depends on audit-log ordering (`EV-P01-13`) |
| Order | Its order-stage accrual entry | **No link at all** | the accumulator that would record it is dead in both generations (`EV-P01-17`) |
| Asset | The bill line that created it | Yes | explicit link |
| Cross-company auto-generated bill | The originating document in the other company | By a chatter message only; no structured link field observed | `EV-P01-28` |

Two of these rows — bill-to-receipt and order-to-accrual — mean that **`§2.12`'s question
cannot be answered from the data in the general case.** That is the finding.
