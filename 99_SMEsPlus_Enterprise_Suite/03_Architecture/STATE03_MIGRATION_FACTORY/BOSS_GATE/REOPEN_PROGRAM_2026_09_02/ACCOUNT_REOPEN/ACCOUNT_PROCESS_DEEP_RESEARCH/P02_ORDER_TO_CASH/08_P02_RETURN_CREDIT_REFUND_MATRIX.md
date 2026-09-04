# 08 — P02 RETURN / CREDIT NOTE / REFUND MATRIX

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-REV2-001`
Underlying evidence: `L2_AUDIT_QUARANTINE/T1_RETURN_CREDIT_REFUND_EVIDENCE.md`

## 0. The Directive's Question

> **How do returns reverse original economic truth, and how does a credit note differ from a physical
> return?**

## 1. The Three Are Different Events

| Event | What it asserts | What it reverses | Owner |
|---|---|---|---|
| **PHYSICAL RETURN** | *the goods came back* | inventory quantity and value | the inbound movement |
| **CREDIT NOTE** | *the customer no longer owes this* | revenue, receivable, tax **and** cost of sales | the accounting document |
| **REFUND** | *we gave the money back* | the cash position | the payment |

**`FACT VERIFIED` — P02-F-39 (HEADLINE).** In the reference process **all three are independent.** None
triggers, requires, or validates against any other. Proof in T1 §4.

## 2. The Independence Proof, Condensed

### 2a. A credit note with **no** physical return is fully reachable

| Step | Finding | Evidence |
|---|---|---|
| Creation | The reversal wizard checks only that the source is posted. It contains no inventory reference at all. | T1 §4a.1 |
| Posting | The posting routine performs no inventory check. The inventory-accounting override **adds** lines; it does not block. | T1 §4a.2 |
| Cost reversal | Cost-of-sales eligibility is a **product property only**. The generator never inspects whether anything came back. **The cost reversal is posted regardless.** | T1 §4a.3 |
| Inventory | No valuation layer is created. Quantity and value are **unchanged**. | T1 §4a.4 |
| Clearing account | The matching routine looks only for movements **out of the customer location** — i.e. returns. With no return it skips, and **the debit sits open forever.** | T1 §4a.5 |
| Valuation | The reversal is valued at the **current standard price on the day the credit note is posted**. | T1 §3(c), §4a.6 |

**Net effect:** revenue reversed, receivable reversed, **expense credited at a price unrelated to what
shipped**, an unmatched debit parked in the outbound stock account, **and inventory untouched**.

### 2b. A physical return with **no** credit note is the ordinary case

| Step | Finding | Evidence |
|---|---|---|
| The return wizard | Creates a picking and opens it. **It never touches an accounting document.** | T1 §4b.1 |
| The only coupling that exists | A refund-intent flag on the movement. Its **entire** effect is on the *delivered quantity* — it is a quantity signal, **not** a document trigger. | T1 §4b.2 |
| Its visibility | **Defaults on, and is rendered only in developer mode.** | T1 §4b.3, C4 |
| With the flag off | The return restores inventory and **does not even reduce delivered quantity**. | T1 §4b.2 |
| With the flag on | Billable quantity goes negative; a negative line is invoiced **only if a human ticks the final-invoice option**, and the resulting draft is then flipped to a credit note. **Nothing calls this from the return.** | T1 §4b.4 |

## 3. Return → Revenue Consequence, By Invoice Policy

**`FACT VERIFIED` — P02-F-40.** Whether a physical return has *any* revenue consequence is determined by
the **invoice policy of the product**, a setting that has nothing to do with returns.

| Invoice policy | Refund-intent flag | Effect of a physical return on billable quantity | Revenue consequence |
|---|---|---|---|
| **delivery** | on (default) | delivered quantity falls, billable goes **negative** | a credit note becomes *available*, if a human asks for it |
| **delivery** | off | **nothing** | **none** |
| **order** | on | **nothing** — billable is ordered minus invoiced | **none** |
| **order** | off | **nothing** | **none** |

**Three of the four combinations produce no revenue consequence whatsoever from goods physically coming
back.** And the platform default for physical goods is invoice-on-order (`EV-P02-048`), i.e. row 3.

## 4. Credit-Note Cost Basis — The Four Branches

**`FACT VERIFIED` — P02-F-41.** A credit note's cost of sales is valued by one of **four** different rules,
selected by conditions the user is not shown.

| # | Condition | Cost basis | Evidence |
|---|---|---|---|
| 1 | Full reversal (reverse-and-modify, dated **today or earlier**) | **exact original cost**, copied verbatim from the source document's cost lines and sign-flipped | T1 §3(a) |
| 2 | Plain credit note, **no** order-line link | the **source document's own cost unit price**, else the product's current standard price | T1 §3(b) |
| 3 | Plain credit note, order-line link present, **a physical return exists** | the **return layer's value** — which is itself the original cost under FIFO/average | T1 §3(c) |
| 4 | Plain credit note, order-line link present, **no physical return** | **the product's CURRENT standard price on the day the credit note is posted** | T1 §3(c) |

Three consequences, each material:

**`FACT VERIFIED` — T1-C2 (DATE-DEPENDENT COST BASIS).** A **future** reversal date silently downgrades
branch 1 to branch 3 or 4. *The cost basis of a "full reversal" depends on whether the user picked today
or tomorrow.*

**`FACT VERIFIED` — T1-C3 (LINKING MAKES IT WORSE).** Branch 3/4 **overwrites** the branch-2 answer
whenever an order line is linked. The original-cost lookup is **dead code for every order-originated
credit note.** Linking a credit note to its order line makes its cost *less* anchored to the original
invoice, not more.

**`SUPPORTED INTERPRETATION` — T1-C7 (COMPOUNDING).** Under average costing, a physical return
**re-weights the moving average downward**, and that re-weighted average is then the standard-price
fallback for any *subsequent* branch-4 credit note. The two failure modes compound.

## 5. Return Valuation — Two Incompatible Definitions Of "Return"

**`CONTRADICTED` — T1-C1.** Two different predicates decide whether a movement is a return:

- **valuation** asks whether the movement carries an originating-move link;
- **accounting** asks whether the source location is the customer location.

A manually created inbound picking from the customer location with **no** originating-move link is
therefore **booked with the return account pair and the storno flag while being valued at current
standard price**. The journal entry says *return*; the valuation layer says *receipt*.

## 6. The Invoiced-Quantity Counter — Deliberately Lossy

**`FACT VERIFIED` — T1-C9.** The counter that says how much of an order has been billed subtracts a credit
note **only when the credit-note line carries the order-line link**. The in-code documentation states this
is deliberate — an unlinked refund must not automatically re-open the order to re-invoicing.

Complete enumeration of the writers of that link (T1 §5, four rows, denominator declared):

| Route | Link set? | Consequence |
|---|---|---|
| Reversal wizard, either mode | **yes** | order re-opens for invoicing; cost re-derives (branch 3/4) |
| Order-driven final invoicing of a negative line | **yes** | intended path |
| **Credit note created by hand in Accounting** | **no** | **revenue reversed, but the order still reads as fully invoiced** |
| Arbitrary copy of an invoice | **no** | — |

**`FACT VERIFIED` — P02-F-42.** A hand-made credit note reverses the money and leaves the commercial
record saying the order is fully billed. There is no reconciliation between the two.

## 7. Refund — The Money

A refund is a **payment in the opposite direction**, matched against the credit note. It is governed by
the settlement machinery in `09_P02_PAYMENT_RECONCILIATION_MATRIX.md`, not by the return or credit-note
machinery. Its independence from both is the third leg of P02-F-39.

**`FACT VERIFIED`.** A credit note can be posted and **never** refunded — it simply sits as an
unapplied credit in the receivable control account, and the customer's balance is net. There is no
event, no ageing and no report distinguishing "credit issued, refund owed" from "credit issued, applied
against the next invoice".

## 8. Reversing A Delivery

**`FACT VERIFIED` — T1 §6.** A completed delivery **cannot be cancelled or reversed.** The system directs
the user to create a return. This is a genuine, well-designed immutability control and is the **strongest
single control found anywhere in P02**.

But three things weaken it:

| # | Weakness | Evidence |
|---|---|---|
| 1 | The **quantity** of a completed movement **can** be corrected, producing new correction layers and a new journal entry — the immutability is of the *record*, not of the *number*. | T1 §6 |
| 2 | Correction entries are dated **today**, not on the movement they correct. A correction made on the 30th books in a different period from the movement. | T1 §6, C8 |
| 3 | The order line's delivered quantity is **writable at the data layer** and bypasses the movement ledger; for service lines it is the *only* source, and for goods it is reachable programmatically. See `05` §3a. | `EV-P02-002`, `EV-P02-070` |

## 9. SMEsPlus Design Positions (all `DESIGN CANDIDATE`, none approved)

| # | Position |
|---|---|
| DC-08-01 | A physical return and a commercial credit must be **two declared events with an explicit, recorded relationship** — *linked*, *deliberately unlinked with a reason*, or *pending*. Silent independence is not acceptable, and neither is silent coupling. |
| DC-08-02 | The cost basis of a reversal must be **one rule**: the cost of the specific units being reversed, taken from the outflow that relieved them. Never a re-derivation, never a current master-data price, and never a rule that changes because the user picked a different date. |
| DC-08-03 | "Is this movement a return?" must have **one definition**, used by valuation and by accounting alike. |
| DC-08-04 | A credit note raised outside the order path must be **impossible to post silently**: either it consumes from the same obligation ledger as the order, or it is explicitly recorded as a non-order credit with a reason. |
| DC-08-05 | *Credit issued but not refunded* must be a **named, aged position**, not a net balance. |
| DC-08-06 | The refund-intent decision must be **visible and explicit at the moment of the return**, never a developer-mode default. |
| DC-08-07 | Correction of a completed outflow must be dated on **the movement it corrects**, with the period consequence of that date made explicit rather than resolved by the system clock. |

## 10. Open Items Carried Forward

| ID | Item | Status |
|---|---|---|
| T1-N7 | Whether a residual is left in the outbound stock account when a credit note's re-derived cost differs from the return layer's value. | `UNRESOLVED — EVIDENCE REQUIRED` — needs a runtime reproduction; the exact scenario is specified in T1 §9. |
| T1-N8 | Whether the two layer-consumption strategies can diverge for the same credit note. | `UNRESOLVED — EVIDENCE REQUIRED` — needs the path set extended to the manufacturing-accounting layers. |
| T1-N9 | Whether the vendor-return path shows the same independence. | `DEPENDENCY OPEN` — this is P01's question, not P02's. |
