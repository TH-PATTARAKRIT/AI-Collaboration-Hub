> GROUP A — Sales + Inventory + Purchase Integrated Backbone | TEAM B Corrective Rework (CORR-010)

# 30 — CORR-010 EVENT RACE AND RESERVATION ATOMICITY CLOSURE

Session: `SMEPLUS-26-08-31-MIG-B-GRPA-SIP-CORR-010`

This deliverable records the full closure evidence for `FV006-EVT-004` (CORR10-01) and `FV006-EVT-005`
(CORR10-02), per the governing prompt §4 minimum closure criteria.

---

## CORR10-01 — `FV006-EVT-004` Ordering Race

### Original finding reproduced

`FV006-EVT-004` (`FV_006/05_EVENT_FLOW_VERIFICATION_MATRIX.md` §4, Major, `GAP FOUND`, Blocking: Yes): a user
confirming a Commercial Commitment and then immediately editing the line's Ordered quantity fires two
Sales-originated events — `Commercial Fulfillment Requested` and `Commercial Line Quantity Changed` — in quick
succession, with no stated ordering guarantee between them; out-of-order processing could leave a Movement
Instruction silently retaining the pre-edit quantity. Formal IBPV RV-009 Deliverable 06 independently confirmed
this remained open and unresolved after CORR-008, and additionally found that CORR-008's own new ordering clause
(`09`§00A) was internally self-contradictory for exactly this case — asserting, in the same breath, that a line's
own events are FIFO regardless of type, and that no ordering guarantee holds across different event types.

### Closure decision

TEAM B does not attempt to assert an enforceable ordering guarantee across an asynchronous, at-least-once
transport (doing so would require prescribing a specific messaging/queue technology, which is out of scope for
this design). Instead, TEAM B removes the underlying reason ordering matters: it makes same-line processing order
**immaterial to correctness** by requiring that any event whose consuming effect depends on a value-bearing field
be treated purely as a *trigger to reconcile against current authoritative state*, never as a *carrier of the
value to apply*. See the full invariant text in
[09_CANONICAL_BUSINESS_EVENT_CATALOG.md](../09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §00A.

### Minimum closure criteria — addressed

1. **Business identity/ordering scope**: the originating document line (Commercial or Supply Commitment line) is
   the scope; the rule applies to `Commercial Fulfillment Requested`, `Commercial Line Quantity Changed`, and
   `Supply Commitment Line Quantity Changed`.
2. **Ordering across event types on the same line**: explicitly answered — **not required**, because the
   reconciliation rule makes it unnecessary. This directly resolves the self-contradiction (the old clause tried
   to answer this question with an ordering guarantee; the new clause answers it by making the question moot).
3. **Contradictory wording eliminated**: the old two-clause self-contradiction is replaced by one rule. Verified
   by direct re-read of the corrected `09`§00A text.
4. **Observable truth on out-of-order arrival/replay**: stated explicitly — whichever event is processed first,
   the Movement Instruction is created/adjusted by reading the line's *then-current* Ordered quantity, never a
   value frozen in an earlier event's payload; a reconciling event arriving before any instruction exists is a
   safe no-op, since the eventual instruction creation itself reads current state.
5. **Idempotency and unresolved-handoff behavior preserved**: the rule explicitly composes with, rather than
   replaces, the `FV006-INT-001` idempotency invariant ([12](../12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md)
   §11) and the `FV006-INT-002` `Handoff Unresolved` mechanism (§03A) — a total non-delivery of the first handoff
   remains a distinct failure mode, caught by `Handoff Unresolved`, not by this ordering rule.
6. **No technology prescription**: no lock, queue, compare-and-swap, or messaging mechanism is named anywhere in
   the corrected text — only the business rule that consumption re-derives from current authoritative state.
7. **Cross-references updated**: `09`§00A's self-citation of a nonexistent `§04A` is corrected to `§03A`
   (independently found during this session's regression sweep, matching a defect RV-009 Deliverable 10 also
   found); the false "tracked in file 18" claim is corrected to point at the actual registration (§07 of file 18,
   added by this session).
8. **Registered in file 18**: yes — see
   [18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md](../18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md) §07,
   item N10.

### Exact changed sections

`09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §00A (full ordering-clause rewrite, self-citation fix, false-claim
correction, new `§03A` reference for the Reservation-atomicity closure below); §03A citation of
`12`§13 corrected to `12`§13A (regression-sweep finding, same defect class as B3). `18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md`
new §07.

---

## CORR10-02 — `FV006-EVT-005` Reservation-Claim Atomicity Race

### Original finding reproduced

`FV006-EVT-005` (`FV_006/05_EVENT_FLOW_VERIFICATION_MATRIX.md` §4, Moderate, `GAP FOUND`, Blocking: No): the
Stock Position bin's enforced write-time uniqueness ([05](../05_INVENTORY_CORE_CANONICAL_DESIGN.md) §02,
[12](../12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §11) protects against a duplicate *row insert*
but does not extend to the Reservation *claim* step ([05](../05_INVENTORY_CORE_CANONICAL_DESIGN.md) §04): two
simultaneous claims against the same Available quantity could each evaluate a stale figure if the claim itself is
not atomic/serialized. Formal IBPV RV-009 Deliverable 06 independently confirmed this remained open and was not
addressed by any CORR-008 correction — the general idempotency invariant covers *repetition* of the *same* claim,
not *concurrency* between two *different* simultaneous claims, a distinct property.

### Closure decision

TEAM B adds a canonical per-bin evaluate-then-commit atomicity invariant, stated as a business-observable
guarantee rather than a locking/transaction mechanism. Full text in
[05_INVENTORY_CORE_CANONICAL_DESIGN.md](../05_INVENTORY_CORE_CANONICAL_DESIGN.md) §04.

### Minimum closure criteria — addressed

1. **Canonical owner of claim/reservation truth**: Inventory, exclusively — unchanged, restated explicitly.
2. **Business precondition for a valid claim**: the bin's Available quantity, evaluated at the moment of
   commitment (not an earlier read), must cover the amount actually committed.
3. **Invariant preventing double allocation/over-claim**: the sum of every claim committed against a bin may never
   exceed that bin's On-Hand quantity at evaluation time — stated as if every simultaneous claim were evaluated
   one at a time, in some order; no specific mechanism prescribed.
4. **Observable loser/outcome of competing claims**: each claim receives a definite, mutually-exclusive outcome
   (full/partial/zero); which claim is favored when two together exceed Available is explicitly left as an open
   business-policy question (registered as N12 in file 18), not invented — the invariant's guarantee (no
   over-allocation, no silent drop) holds regardless of which policy is later chosen.
5. **State/event/audit consequences**: no new event type required — the existing `Stock Reserved` event
   ([09](../09_CANONICAL_BUSINESS_EVENT_CATALOG.md) §03) already carries the shape; the idempotency invariant
   ([12](../12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md) §11) is extended to name `Stock Reserved`
   explicitly as a covered trigger (this also closes the B2 residual precision gap in the same edit).
6. **Tenant + Company scoping explicit**: the bin key is scoped within one Company (via Location) within one
   Tenant (the outermost boundary); the atomicity invariant is stated as never needing to cross either boundary.
7. **Technology-neutral**: no lock, compare-and-swap, serializable-transaction, or queue mechanism is prescribed.
8. **Partial reservation, release/cancel, retry compatibility**: explicitly addressed — partial claims remain a
   valid outcome; releasing a Reservation increases Available for the *next* evaluation without retroactively
   reopening an already-committed claim; a retried/redelivered claim for the same Movement Instruction's business
   identity is governed by the (now-extended) idempotency invariant, never re-evaluated and committed twice.
9. **Registered in file 18**: yes — see file 18 §07, items N11 (closure) and N12 (the genuinely open tie-break
   policy question, carried forward rather than invented).

### Exact changed sections

`05_INVENTORY_CORE_CANONICAL_DESIGN.md` §04 (new "Reservation-claim atomicity" bullet, full invariant).
`12_EXCEPTION_PARTIAL_CANCEL_RETURN_CORRECTION_MODEL.md` §11 (idempotency invariant's covered-trigger list
extended to name the fulfillment/receipt-reconciliation trigger and the Reservation claim explicitly).
`09_CANONICAL_BUSINESS_EVENT_CATALOG.md` §00A (closing cross-reference to `05`§04 and file 18 §07).
`18_UNKNOWN_CONFLICT_AND_CARRY_FORWARD_REGISTER.md` new §07.

---

## Future-Verifiable Test Oracles (Both Closures)

- **CORR10-01 oracle**: given a confirmed line with Ordered=10, when `Commercial Line Quantity Changed` (to 15)
  is processed strictly before `Commercial Fulfillment Requested` for the same line, then the resulting Movement
  Instruction's planned quantity is 15 — not 10 — regardless of processing order.
- **CORR10-02 oracle**: given a bin with On-Hand=10 and two simultaneous claims for 6 each, then the sum of both
  claims' committed outcomes never exceeds 10 (e.g., 6 full + 4 partial, or 5 + 5, or any split that sums to ≤10)
  — never 6 full + 6 full.

Both oracles are statable and checkable without naming any implementation mechanism, satisfying the governing
prompt's "future-verifiable" requirement.
