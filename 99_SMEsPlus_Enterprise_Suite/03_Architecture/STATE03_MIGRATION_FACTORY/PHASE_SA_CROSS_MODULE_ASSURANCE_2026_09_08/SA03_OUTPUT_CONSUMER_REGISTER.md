# SA03 — OUTPUT AND DOWNSTREAM CONSUMER REGISTER

Status: **HOLD** — outputs and consumers mapped for the evidenced spine; three outputs have no
identified consumer and one consumer has no identified producer.
Governing law: master prompt §5.

---

## 1. The mandatory test

> `UPSTREAM OUTPUT  =  DOWNSTREAM REQUIRED INPUT`

Where the two are not semantically compatible, the row is marked `CROSS-MODULE INTEGRATION GAP`.

---

## 2. Sales outputs

| Output | Timing | Consumer(s) | Compatibility with consumer input | Status |
|---|---|---|---|---|
| Commercial commitment state (4 values) | on confirmation | Inventory, Accounting | Matches Inventory's demand trigger and Accounting's eventual recognition | `COMPATIBLE` |
| Fulfilment demand | on confirmation, **indirectly via the rule engine** | Inventory | Matches, but asynchronously — see `SA02-F-03` | `COMPATIBLE — latency asymmetry` |
| Billable-now quantity | on fulfilment or on order, per product policy | Accounting | Consumed **verbatim** as the billing line quantity | `COMPATIBLE` |
| Header fulfilment progress (4 values) + first-fulfilment date | on movement completion | Sales itself | Re-derived independently from Inventory's own transfer status — *a separate, independently-computed fact, not a pass-through* | `COMPATIBLE — duplicate derivation` |
| Cancellation instruction | on cancellation | Inventory | Cancels not-yet-completed transfers, spares completed ones | `COMPATIBLE` |
| Commercial-terms freeze flag (freezes 8 named line fields) | on lock | **none** | — | **`NO CONSUMER IDENTIFIED`** |
| Auto-created draft buy commitment (subcontract-service configuration) | on line confirmation | Purchase | Bypasses the human demand-request step entirely | `COMPATIBLE — control bypass, see SA03-F-02` |

## 3. Purchase outputs

| Output | Timing | Consumer(s) | Status |
|---|---|---|---|
| Commitment state (**5 values** — one more than the sell side, incl. pending-approval) | lifecycle | Inventory, Accounting | `COMPATIBLE` |
| Approval-completed timestamp | on approval | audit | `COMPATIBLE` — but see `SA02-F-02`, the recording half is unexercised |
| Physical receipt expectation | on confirmation, **directly and synchronously** | Inventory | `COMPATIBLE` |
| Vendor registration into vendor-supply master | side effect of confirmation | Vendor master | `COMPATIBLE` |
| Received quantity (with return / direct-ship netting) | on movement completion | Accounting | `COMPATIBLE` |
| Billable-now quantity | per product policy | Accounting | `COMPATIBLE` |
| Cancellation cascade, state-partitioned by receipt scenario | on cancellation | Inventory | `COMPATIBLE` |
| Multi-vendor comparison outcome (winner / losers) | on award | Purchase | `COMPATIBLE` |
| Direct-to-customer routing (destination substitution) | on line configuration | Inventory / customer | **`CROSS-MODULE INTEGRATION GAP`** — this is the dropship route, and `SA05` BN-05 is `HOLD` |

## 4. Inventory outputs

| Output | Consumer(s) | Status |
|---|---|---|
| The single physical-movement ledger for the whole suite | all domains extend it rather than keeping separate ledgers | `COMPATIBLE` — a strong architectural fact for SMEsPlus to preserve |
| Six non-conflatable quantity concepts — On-Hand, Reserved, Available, Incoming, Outgoing, Forecasted | Sales (advisory), Purchase (advisory) | `COMPATIBLE` |
| Completed-movement event | Sales delivered qty; Purchase received qty | `COMPATIBLE` |
| Transfer state, derived from child movements | Sales (re-derived independently) | `COMPATIBLE — duplicate derivation` |
| Remaining-supply record (partial fulfilment) | **neither Sales nor Purchase read it** | **`NO CONSUMER IDENTIFIED`** — recorded by Group A as a genuine non-consumption, not silence |
| Return transfer — the only correction route after a completed movement | Sales, Purchase (both re-stamp links, **neither initiates**) | `COMPATIBLE` |
| Replenishment procurement need | Purchase (one-way reflective dependency) | `COMPATIBLE` |
| Destination sub-location resolution | Inventory-internal only | **`NO CONSUMER IDENTIFIED`** — by design |

## 5. Accounting outputs

| Output | Consumer(s) | Status |
|---|---|---|
| Posted customer-billing lines | Sales (read backward for already-billed) | `COMPATIBLE` — declared round-trip |
| Posted supplier-billing lines | Purchase (read backward) | `COMPATIBLE` — declared round-trip |
| Tax determination | Sales, Purchase (neither computes tax itself) | `COMPATIBLE` |
| Customer-invoice lifecycle state (posted / locked / reconciled / reversed) | **Sales cancellation gate requires it; no producer contract exists** | **`CROSS-MODULE INTEGRATION GAP` — the A1 contradiction, `XD-01`** |
| Canonical Accounting Event Identity (BD-ACC-01) | all source modules | `COMPATIBLE` — ruled, not yet contracted |

---

## 6. SA03-F-01 — three outputs with no consumer, one input with no producer

| Direction | Item | Meaning for SMEsPlus |
|---|---|---|
| Output → nobody | Commercial-terms freeze flag | A control that changes nothing outside its own module is either an internal-only concern or an unwired control. SMEsPlus must decide which; it must not carry it forward unexamined. |
| Output → nobody | Remaining-supply (partial fulfilment) record | Neither commercial side reads the fact that supply is outstanding. Commercial "how much is still coming" is therefore re-derived rather than read. |
| Output → nobody | Sub-location resolution | Legitimately internal. Recorded so the register's zero is a determination, not an omission. |
| Nobody → input | Customer-invoice lifecycle state for the sell-side cancellation gate | The `XD-01` contradiction. A required downstream input with no upstream producer contract. |

A register in which every output has a consumer is usually a register that has not been
checked. These four rows are the evidence that this one was.

## 7. SA03-F-02 — one boundary write, and it bypasses a hard control

Group A records exactly **one** write across a module boundary in the whole backbone: the
sell side creates a buy-side commitment line directly, for subcontract-service configured
products, *"with no human RFQ step"*.

Everywhere else the pattern is read-only observation. This single exception:

- bypasses the demand-request approval gate that `SA02` §3 records as a **hard** gate on every
  other purchase;
- is the mechanism underlying the dropship / buy-to-order natures (`SA05` BN-05, BN-06), both
  of which are `HOLD` or `PARTIAL`.

**Determination for SMEsPlus:** an automatic cross-module document creation must not be able
to enter a downstream module below that module's own control floor. If a purchase requires
approval when a human raises it, a purchase raised by a sale requires an equivalent control.
This is stated as a Phase SA design position with independent rationale — it is not inherited,
and the reference behaviour is the counter-example that prompted it.

## 8. SA03-F-03 — duplicate derivation is the suite's recurring integration shape

Two independent rows above are marked `COMPATIBLE — duplicate derivation`: sell-side header
fulfilment progress and sell-side transfer status are each **re-computed** from movement facts
rather than read from Inventory's own derived state.

This is not wrong, and it is not free. Two derivations of one fact can disagree — after a
partial cancellation, a return, or a correction. SMEsPlus must either (a) publish one derived
fact and have consumers read it, or (b) keep independent derivations and add a reconciliation
that proves they agree. Carried to `SA16`-adjacent design work and to `SA13`.

---

`SA03 — HOLD`. Outputs and consumers are mapped for the evidenced spine. Two
`CROSS-MODULE INTEGRATION GAP` rows and three unconsumed outputs are open.

Boss remains the sole Final Approver.
