# P01 — RETURN / REFUND / REVERSAL MATRIX

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

`§2.13` requires that historical economic truth is never silently overwritten. This matrix
reports how each correction path in procure-to-pay actually behaves against that rule.

---

## 1. THE CORRECTION PATHS

| Path | Preserves history? | What actually happens | Class |
|---|---|---|---|
| Return goods to vendor | **Yes** | A new outgoing movement is valued and posted, crediting inventory and debiting the clearing account. The original receipt stands. | FACT VERIFIED (`R1`) |
| Vendor credit note | **Yes**, structurally | A reversing document with its own identity, linked to the original | SUPPORTED INTERPRETATION — the price-difference engine has an explicit refund branch keyed to the reversed entry |
| Reverse a journal entry | **Yes** | A counter-entry is created | FACT VERIFIED (`R1`) |
| **Reset a posted bill to draft** | **No** | Interim and price-difference journal items are **deleted**. Still-draft assets created from the bill are **deleted**. | FACT VERIFIED `EV-P01-11`, `EV-P01-19` |
| **Cancel a posted bill** | **No** | Same deletion of derived journal items | FACT VERIFIED `EV-P01-11` |
| **Duplicate a journal entry** | n/a | Derived journal items are stripped from the copy | FACT VERIFIED `EV-P01-12` |
| **Reset a purchase order to draft** | **No control at all** | A bare status write. No state test, no test for existing receipts or bills, no group restriction — in **both** generations. Reachable regardless of what has already happened downstream. | FACT VERIFIED `EV-P01-43` |
| **Posting into a locked period** | **No** — and worse | The lock does **not** refuse the posting. It **rewrites the entry's date** to a permitted one and posts it. | FACT VERIFIED `EV-P01-48` |
| Manual inventory revaluation | Yes, as a new entry | Creates a journal entry restating the value of previously received goods | FACT VERIFIED `EV-P01-22` |
| Custom effective-date correction | **No** | Resets a posted entry to draft, blanks its number, re-dates and re-posts it, then rewrites the valuation record's creation timestamp by direct SQL | SUPPORTED INTERPRETATION — expert finding, not yet re-derived by this session |

---

## 2. THE THREE FINDINGS THAT MATTER

### 2.1 Correction by deletion

Five of the ten paths above do not preserve history. The most serious is the pair at the top of
the "No" list: **resetting or cancelling a posted vendor bill deletes derived journal items
rather than reversing them.** The original amounts are not recoverable from the documents.

`CONTRA-P01-01` — **rejected as a transfer candidate.**

### 2.2 The lock that is not a lock

This is the single most counter-intuitive finding in the package and it deserves plain
statement:

> A soft period lock does not stop a posting. It **moves the posting's date** into an open
> period and lets it through.

`EV-P01-48`. The consequence for a purchase process is direct: a bill or receipt entered
against a closed period does not fail — it silently appears in a later one. **Cut-off testing
performed on the entry's own date will therefore always look clean**, because the date it
inspects is the date the system chose to make it clean.

The Code & UI Architect expert additionally reported, and this session has **not** re-derived,
that the *purchase-specific* lock never protects goods receipt at all, because the lock is
selected by journal type and the inventory valuation journal is a general journal. If that
holds, the receipt leg of a purchase is protected only by the global and hard locks.

### 2.3 An order can be un-committed after the fact

`EV-P01-43`: reset-to-draft on a purchase order has **no guard of any kind**, while cancel is
guarded. So the guarded path is the one a user is offered and the unguarded path is the one
that is reachable programmatically. A purchase order with completed receipts and posted bills
can be returned to draft, after which its own quantity and price fields are editable — and the
accounting-invoicing group has write access to exactly those fields (`EV-P01-44`).

Chained, that is: **the party that receives the invoice can make the commitment agree with the
invoice.** No single one of those three facts is a finding; their composition is.

Classification: each component **FACT VERIFIED**; the composition **SUPPORTED INTERPRETATION**,
runtime confirmation required (edge case 45 and the reset-to-draft case in
`P01_EDGE_CASE_TEST_MATRIX.md`).

---

## 3. RETURN-SPECIFIC BEHAVIOUR

| Case | Behaviour | Class |
|---|---|---|
| Return before billing | Outgoing movement debits the clearing account, reducing the received-not-billed balance | FACT VERIFIED |
| Return after billing | Requires a vendor credit note to clear the payable; the goods leg and the money leg are separate events | SUPPORTED INTERPRETATION |
| Return of a previously returned item | The source contains a **special case** that substitutes the order price for the layer price to avoid double-impacting valuation | FACT VERIFIED (`R1`) |
| Refund for a returned quantity | The price-difference engine explicitly skips this case | FACT VERIFIED (`R1`) |

The special case in row 3 is itself the finding: **the general algorithm does not handle
re-receipt of returned goods, and a hand-written exception was added instead.** A clean-room
design should treat the existence of that exception as a signal that the underlying model is
under-specified, not copy the exception.

---

## 4. WHAT IS NOT ESTABLISHED

- Vendor credit-note behaviour end-to-end — **class C**, partially assigned to experts.
- Whether reset-to-draft on a bill is itself blocked by lock dates in practice — depends on
  §2.2 and is **class C** for this document.
- The custom effective-date correction path — **SUPPORTED INTERPRETATION**, expert-reported,
  not re-derived by this session.
- Withholding reversal after a certificate has been issued — **class C**, and gated on
  `DEP-P01-03` and `DEP-P01-04`.
