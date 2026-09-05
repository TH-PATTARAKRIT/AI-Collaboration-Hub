# 67 — P02 RECONCILIATION REFRESH

**LAYER 2 — AUDIT QUARANTINE.**
**P02 LAST CONSUMED SHA: `89928aa`.**

---

## 1. The absolute distinction

> **MANUFACTURING COST CREATION ≠ COGS RECOGNITION.**

P03 owns the first: the value written onto a finished-goods move. P02 and the COGS track own
the second: whether and when that value becomes an expense. **Neither may be inferred from
the other.**

## 2. The joint picture in one database

P02 and P03 read the **same** database, `iSMEs`, and independently counted
`account_move_line` = **447,384**. The figures match exactly, which cross-validates both
extraction methods.

| Half | Owner | Finding |
|---|---|---|
| Manufacturing cost creation | **P03** | finished goods carry **material cost only**; conversion cost structurally zero; and 49 completed finished moves carry **no valuation at all** (`P03R-F-02`) |
| COGS recognition | **P02** | **zero COGS lines** — the invoice-side cost mechanism has never run |

> Goods are manufactured at an incomplete cost, and when sold **no cost of sales is
> recognised at all**. Two independent failures, one database, neither session able to see
> both alone.

**Neither closes the other's finding.** P03 does not claim the COGS half.

## 3. Does P02's timing evidence change P03's conclusions?

**No.** P02's findings concern recognition timing at delivery/invoice. P03's conclusions
concern the value written at production. The two are sequential, not overlapping, and
P03's measured inputs (`_cal_price`'s three terms) are unaffected by when the value is
later expensed.

One interaction is recorded and **not resolved**: because COGS never posts, the
material-only carrying value has **never been tested against a sale**. The understatement
is therefore invisible in the income statement and sits entirely in inventory — which is
exactly where `55`'s −48.7 % distortion also sits. **Whether these compound is a joint
P02/P03/Inventory question**, `UNR-P03-16`, routed to P11.

## 4. Handed to P02

| # | Item |
|---|---|
| 1 | The FG unit-cost formula and its **measured** inputs: material only; work-centre cost 0; `extra_cost` 0 of 10,764 |
| 2 | **49 completed finished-goods moves with no valuation record and 280 valued at zero** — these are the units whose COGS, if it ever posted, would be zero for a reason originating **before** P02 |
| 3 | `55` — the valuation ledger carries 30 rows to ±10²¹ that the GL does not. Any future COGS posting drawn from that ledger inherits it |
