# SA09 — EXCEPTION AND REVERSAL MATRIX
## CP-SA-60 — EXCEPTION INTEGRITY

Status: **HOLD**
Evidence: Group A exception/partial/return/cancellation matrix (`8b0993d8` file 10),
its corrective cycle (`e4418644`), independent re-verification RV-011 (`77e93d44`),
and the Account P-series reversal findings.

---

## 1. Exception classes required by master prompt §16

`cancel` · `return` · `reverse` · `correction` · `partial` · `retry` · `duplicate` ·
`timing mismatch`

---

## 2. Matrix

| Class | Position established | Status |
|---|---|---|
| **Partial fulfilment (sell)** | Remaining obligation tracked; a self-referential remaining-supply record, not a separate object | `ESTABLISHED` |
| **Partial receipt (buy)** | Same structure | `ESTABLISHED` |
| **Cancel before commitment** | Both sides | `ESTABLISHED` |
| **Cancel after commitment** | Sell side established; buy side originally recorded `EVIDENCE_MISSING`, **closed** by the corrective cycle and confirmed *provably symmetric-in-effect* | `ESTABLISHED — via correction` |
| **Cancel after reservation** | Cancels not-yet-completed movements, spares completed ones | `ESTABLISHED` |
| **Cancel after partial movement** | State-partitioned by receipt scenario | `ESTABLISHED` |
| **Correction after completed movement** | **The only route is a return.** Recorded as an exhaustive negative claim across all phases | `ESTABLISHED` |
| **Customer return** | One of the two most fully evidenced findings in the programme | `ESTABLISHED` |
| **Vendor return** | Structurally identical | `ESTABLISHED` |
| **Retry / duplicate** | An expected-and-handled concurrent-write race in the bin ledger; idempotency invariant now explicitly names the reservation trigger as covered | `ESTABLISHED` |
| **Reversal (accounting)** | BD-ACC-01: a reversal creates a **new** event referencing the original; same-event retry is idempotent | `ESTABLISHED — as a ruling` |
| **Timing mismatch** | Ordering-independent-by-design: any event whose effect depends on a value-bearing field is *a trigger to reconcile, never a carrier of the value to apply*; the consumer re-reads authoritative values at processing time | `ESTABLISHED — and this is a strong SMEsPlus principle to keep` |
| **Wrong item / wrong quantity** | — | **`NOT ESTABLISHED`** (`NOT OBSERVED / EVIDENCE_MISSING`) |
| **Late supply / delivery breach** | Forecast and deadline computed; no breach handling | **`NOT ESTABLISHED`** |
| **Missing or late documents** | — | **`NOT ESTABLISHED`** |
| **Broader transaction-failure recovery** | One narrow case established; the general case not | **`NOT ESTABLISHED`** |
| **Over / under receipt** | Established **as a negative** — genuinely unguarded, blocked nowhere | `ESTABLISHED AS A NEGATIVE` |
| **Approval rejection** | Native path established; a second mechanism's disposition resolved by the corrective cycle | `ESTABLISHED — via correction` |

### 2.1 Count

| Status | Count |
|---|---|
| `ESTABLISHED` (incl. via correction, incl. as a negative) | 14 |
| `NOT ESTABLISHED` | 4 |

---

## 3. SA09-F-01 — an exception register that is stale against its own programme's corrections

The Group A exception matrix (file 10) is the **only** one of its programme's six registers
carrying **no corrective-update section**. As a result it still publishes `EVIDENCE_MISSING`
for two items that sibling registers in the same programme record as closed, and its own
cross-cutting note still names one of them *"the single highest-value follow-up read"*.

Phase SA does **not** inherit those two rows as open. They are recorded above as
`ESTABLISHED — via correction`, sourced from the registers that carry the corrections and from
the independent re-verification that confirmed them.

**Class.** This is a revision-log defect: the correction was made in the programme and never
edited into the register that publishes the claim. It is the same defect class that SMEsPlus
governance has met before, and it is recorded here so that the next reader of file 10 is not
misled by it. Routed to `SA14` as `XD-04` and to the PMO lineage items.

## 4. SA09-F-02 — six invariants that are *not* enforced, recorded as facts

Group A's invariant register records six invariants that a reader would assume hold and which
the evidence shows do not:

1. delivered/received never exceeds ordered — **does not hold**;
2. stock never goes negative — no database constraint; application-layer only, bypassable;
3. one row per bin key — **no unique index**; reconciled after the fact by a merge routine that
   exists precisely because concurrent writers violate it;
4. commitment state holds only declared values — no database-level constraint on any of the
   four state columns;
5. a confirmed order is gated by available stock or credit — **both advisory only**;
6. billed never exceeds ordered — no constraint ties the quantities together.

**These are learning, not a specification.** Master prompt §22 requires SMEsPlus to have an
independent rationale for what it adopts. Phase SA's position: items 1, 2, 4 and 6 are
**integrity invariants SMEsPlus should own in its own core**, because BD-ACC-01 makes the
accounting event depend on quantities these invariants bound. Item 3 is an implementation
concern for a later gate. Item 5 is the design position already raised as `SA02-F-01`.

Recording an unenforced invariant as a *fact about the reference estate* and then deciding
independently whether SMEsPlus enforces it is exactly the clean-room discipline required — the
alternative, inheriting the absence by default, is source-copying by omission.

## 5. SA09-F-03 — the exception classes that are missing share a shape

The four `NOT ESTABLISHED` classes — wrong item, late supply, missing documents, general
failure recovery — are all **exceptions raised by the world outside the system**, not by a user
action inside it. Every established class is triggered by an in-system act (confirm, cancel,
deliver, return, retry).

SMEsPlus is therefore evidenced on exceptions it causes and unevidenced on exceptions that
happen to it. For an SME ERP this is the wrong way round: the supplier who ships late and the
box that arrives with the wrong item are the daily case.

Routed to `SA16` as a scoping input to TVDR-01 and to `SA17` as a Pre-Test priority.

---

`CP-SA-60 — HOLD`. Fourteen of eighteen exception classes are established; four are not, and
they share one shape.

Boss remains the sole Final Approver.
