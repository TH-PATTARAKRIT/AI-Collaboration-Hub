> GROUP A — Sales + Inventory + Purchase Integrated Backbone | EXPERT IBPV — Formal Re-Verification RV-011

# 05 — `FV006-EVT-005` RESERVATION-CLAIM ATOMICITY RE-VERIFICATION (RV11-02)

Document ID: `SMEPLUS-26-08-31-IBPV-GRPA-SIP-RV-011-D05`

## 00 — Original Finding, Independently Re-Read

`FV006-EVT-005` (`FV_006/05_EVENT_FLOW_VERIFICATION_MATRIX.md` §4, Moderate, `GAP FOUND`, Blocking: No),
reproduced from RV-009 Deliverable 06 §04: the Stock Position bin's enforced write-time uniqueness (`05`§02,
`12`§11) protects against a duplicate row *insert* but does not extend to the Reservation *claim* step (`05`§04)
— two simultaneous claims against the same Available quantity could each evaluate a stale figure if the claim
itself is not atomic/serialized, a distinct concurrency property from idempotency (safe repetition of the *same*
claim).

## 01 — Corrected Text, Independently Read

`05_INVENTORY_CORE_CANONICAL_DESIGN.md` §04, current state (read directly): a new "Reservation-claim atomicity"
paragraph states — canonical owner of claim truth is Inventory exclusively; the precondition for a valid claim is
the bin's Available quantity *at the moment of commitment*, not an earlier read; the atomicity invariant is
stated as an observable outcome ("the sum of every claim committed against a bin may never exceed that bin's
On-Hand quantity at the time each claim is evaluated, as if every simultaneous claim... had been evaluated one at
a time, in some order"); outcomes are full/partial/zero, mutually exclusive; the tie-break policy when two claims
together exceed Available is explicitly left open (not invented); scope is per-bin, within one Company within one
Tenant; retry/idempotency composes via `12`§11, which now explicitly names `Stock Reserved` as a covered trigger.

## 02 — Independent Concrete Oracle Test

**Setup** (the governing prompt's own oracle, independently applied): bin On-Hand = 10. Two simultaneous claims,
6 units each.

Per the stated invariant, the two claims must be resolvable "as if... evaluated one at a time, in some order" —
i.e., the design requires that whichever serialization order is chosen by an eventual implementation, the sum
committed can never exceed 10:

- If Claim A (6) is evaluated first: it fully succeeds (Available drops from 10 to 4).
- Claim B (6) is then evaluated against Available = 4: it cannot fully succeed. Per the "partial reservation is a
  valid outcome, not an error" rule (also stated in `05`§04, restated from the pre-existing Reservation model),
  Claim B receives a **partial** outcome (4), not a silent full grant.
- **Total committed: 6 + 4 = 10.** Never 6 + 6 = 12.

Symmetrically, if B is evaluated first, A receives the partial outcome — the invariant does not depend on which
claim is "first"; it depends only on the sum never exceeding On-Hand at each evaluation point. **Independently
confirmed: the stated invariant, if honored, cannot produce the double-allocation outcome the original finding
warned about.** This is the correct level of verification for a design document (business-observable guarantee),
not an implementation proof — consistent with the governing prompt's explicit instruction not to prescribe a
locking/CAS/transaction mechanism at this review level.

## 03 — Checklist (Governing Prompt §5, RV11-02)

| # | Question | Independent finding |
|---|---|---|
| 1 | Inventory is canonical owner of reservation truth | Confirmed, `05`§04, unchanged from `10`§01's pre-existing ownership table |
| 2 | Evaluation uses authoritative Available truth at commit point, not stale pre-read | Confirmed — "evaluated at the moment the claim is committed (not at some earlier read the claim may have started from)" |
| 3 | Two simultaneous claims cannot jointly commit beyond available quantity | Confirmed by the oracle trace in §02 |
| 4 | Full/partial/zero outcomes are observable | Confirmed — "each claim... receives a definite, mutually-exclusive... outcome (full, partial, or zero)" |
| 5 | No claim silently disappears | Confirmed — "no claim's outcome is silently dropped: a claim that receives less than requested (including zero) still produces the observable... condition on its own Movement Instruction" |
| 6 | Same-business-identity retries cannot double-commit | Confirmed — `12`§11's idempotency invariant now explicitly names `Stock Reserved` as a covered trigger (independently read in `12`§11's operative text: "(c) commits a Reservation claim (`Stock Reserved` — **CORR-010 addition**...)"); a retried claim for the same instruction exposes the already-recorded outcome, never re-evaluates |
| 7 | Release/cancel restores availability only for later evaluation | Confirmed — "Releasing a Reservation... increases Available for the *next* claim's evaluation; it never retroactively reopens or invalidates a claim already committed" |
| 8 | Tenant/Company/bin scope is explicit | Confirmed — "the bin key is always resolved within one Company (via Location)... within one Tenant... the atomicity invariant never needs to, and does not, reach across a Company or Tenant boundary" |
| 9 | No database-lock/CAS/queue mechanism is prescribed as architecture fact | Confirmed by direct read — "No lock, compare-and-swap, serializable-transaction, or queue mechanism is prescribed — only this business-observable guarantee" |

## 04 — Tie-Break Policy — Correctly Left Open, Not Invented

The design explicitly declines to decide which claim is favored when two together exceed Available ("first-
evaluated, priority, or any other tie-break... is a business-policy question, not a structural one"). Independently
confirmed this is registered, not silently dropped: `18`§07 item `N12`, read directly, states `CONTROLLED
CARRY-FORWARD`, "not a structural gap — the atomicity invariant (N11) holds regardless of which claim is
favored." This is the correct disposition — the atomicity guarantee (no over-allocation) and the tie-break policy
(who wins a contested claim) are genuinely separable questions, and conflating them would either invent an
unevidenced business policy or wrongly block the structural closure on an unrelated open question.

## 05 — Registration Check

`18`§07 item `N11`, read directly: `CLOSED BY TEAM B CORRECTION (CORR-010)`, citing `05`§04 and the exact
invariant text. Independently confirmed accurate against the corrected artifact, not merely present as a claim.

## 06 — Verdict

**`VERIFIED`.** The design-level atomicity invariant independently satisfies the governing prompt's own concrete
oracle (On-Hand=10, two simultaneous claims of 6 → committed total never exceeds 10) by direct trace, addresses
all nine required elements, is technology-neutral, and correctly separates the structural guarantee (closed) from
the tie-break policy default (correctly left open and registered as N12, not invented). No counterexample to the
stated invariant was found.

**Gate impact**: this finding no longer independently blocks Development. It was Moderate severity, non-blocking
even in its original FV-006 disposition; RV-009 (D11 item C2) escalated it to narrowly blocking Team C only
because of the mistracking pattern, which is independently confirmed corrected (§05 above) alongside the
underlying design gap (§01–§03 above).
