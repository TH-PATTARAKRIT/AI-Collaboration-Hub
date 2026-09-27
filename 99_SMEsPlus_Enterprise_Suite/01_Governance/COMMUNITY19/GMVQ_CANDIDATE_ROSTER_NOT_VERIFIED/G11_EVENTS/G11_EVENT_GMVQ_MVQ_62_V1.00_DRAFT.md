# SMEsPlus ENTERPRISE SUITE
## GMVQ — G11 EVENTS / event Module Adversarial MVQ Bank

**Document ID:** GMVQ-G11-EVENT-MVQ62-V1.00
**Group:** G11 EVENTS
**Module Metadata:** `event`
**Wave:** W2
**Author Cell:** P-E1 (GMVQ Question Factory — Production Team P-E1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 62

## Purpose

`event` is the BASE module of Group G11 EVENTS and the only module in the group that owns a
genuinely fixed real-world moment: registrants commit money before that moment, and the
organizer's obligation is understood to be discharged at or around it. All seven bridge modules
in this group (`event_product`, `event_sale`, `event_booth`, `event_booth_sale`, `event_crm`,
`event_crm_sale`, `event_sms`) are authored against this bank, so this bank deliberately owns the
group's core invariants directly — capacity as a hard limit under concurrent registration,
ticket-type capacity against overall capacity, waiting-position promotion and its determinism,
what happens when a date, location or capacity changes after people have already registered and
paid, cancellation and refund when the fixed moment has not yet occurred versus after it has
passed, duplicate and transferred registrations, attendance recorded against a registration that
no longer supports it, per-company scoping and cross-company visibility of registrant data, and
the audit trail of a capacity change made while registrations are open — so the bridge banks do
not have to rediscover them piecemeal.

Per the Group Brief, timing is this group's central risk: an occasion is the rare object with a
fixed real-world moment, money is taken before it, and almost every interesting failure is
something arriving on the wrong side of that moment. A majority of the questions in this bank
carry a timing dimension directly in their `HYPOTHESIS` or `DISCONFIRMING_OBSERVATION` for that
reason.

Question text is source-neutral: no vendor or product name, no technical identifier (model,
table, field, method, XML ID, API path), and no reference to how any specific implementation is
built. Question text also avoids this module's own metadata name, using generic business language
("the occasion", "the fixed date", "a seat") throughout; the module's own metadata name appears
only in the `MODULE:` field of each record.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its
  `HYPOTHESIS` wrong, describing a genuine failure state rather than a restatement of the
  hypothesis.
- No padding: 62 questions exist because they test 62 distinct material hypotheses, spread
  across business capability, business rule, state transition, configuration dependency,
  role/permission, exception path, cancellation, reversal, negative case, cross-module dependency,
  optional behaviour, auditability, tenant/company boundary, concurrency/ordering, runtime
  reachability, configuration reachability, and source/runtime contradiction potential.
- `LAYER: BASE` marks a foundation/configuration question (capacity setup, ticket-type
  configuration, company scoping, permission boundaries); `LAYER: PROCESS` marks a
  transactional/operational question (registration, cancellation, payment, attendance,
  waiting-list promotion), since this module carries both layers.
- This bank owns the group's core invariants directly so the seven sibling bridge banks in this
  group can restrict themselves to seam-only questions, per the GMVQ Bridge Module Rule V1.00.
- This bank is DRAFT question content only. Not approved, not frozen, not verified.
  `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this
  bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G11-EVENT-Q001

```yaml
QID: G11-EVENT-Q001
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When exactly one seat remains and two registration attempts are submitted at effectively the
  same moment, the occasion admits exactly one of them and the other is told, at the time it is
  submitted, that no seat is available — neither attempt silently succeeds against a seat that no
  longer exists.
WHY_IT_MATTERS: >
  If both attempts are told they succeeded, one registrant will show up, or be charged, for a
  seat that was never actually reserved for them, and the failure will not surface until it is far
  more costly to fix.
DISCONFIRMING_OBSERVATION: >
  Both concurrent attempts are recorded as successfully holding the same single remaining seat, so
  the count of confirmed or held registrants exceeds the configured capacity by at least one.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Configure an occasion with capacity set so that exactly one seat remains, then submit two
  independent registration requests for that occasion in immediate succession and compare what
  each is told and what the resulting registrant count is.
```

## G11-EVENT-Q002

```yaml
QID: G11-EVENT-Q002
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  When a ticket type's own remaining allotment reaches zero while the occasion's overall capacity
  still has room, a new registration for that specific ticket type is refused even though
  registrations for a different ticket type on the same occasion continue to succeed.
WHY_IT_MATTERS: >
  If the ticket type's own limit is not actually enforced, the occasion can end up with more
  holders of a given ticket type than that type was ever meant to allow, undermining any capacity
  planning attached to that type specifically.
DISCONFIRMING_OBSERVATION: >
  A registration for the ticket type that has already reached its own allotment succeeds anyway,
  producing more confirmed holders of that type than its configured allotment allows.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure an occasion with two ticket types, each carrying its own allotment, bring one type's
  allotment to zero while the occasion overall still has open capacity, then attempt a new
  registration against the exhausted type.
```

## G11-EVENT-Q003

```yaml
QID: G11-EVENT-Q003
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a capacity breach is ever discovered after the fact — more confirmed registrants than seats —
  the occasion surfaces the breach and the excess registrants as an identifiable exception state
  rather than silently truncating the registrant list or accepting the overage as the new normal.
WHY_IT_MATTERS: >
  A silent truncation would remove some registrant's confirmed place without their knowledge or
  any record of why, while silently accepting the overage would let a hard capacity limit be
  routinely meaningless.
DISCONFIRMING_OBSERVATION: >
  A capacity breach exists and nothing in the occasion's state, listing, or logs distinguishes the
  excess registrants or flags that a breach occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force a capacity breach, for example by raising a confirmed count past capacity through a
  manual override, and inspect whether the occasion's state or audit trail records the breach and
  identifies which registrants are in excess.
```

## G11-EVENT-Q004

```yaml
QID: G11-EVENT-Q004
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a seat is freed by a cancellation, the registrant holding the earliest waiting position is
  the one promoted, not a later-queued registrant, and the promotion order does not depend on
  which registrant happens to be looked at or acted on first by staff.
WHY_IT_MATTERS: >
  A non-deterministic promotion order turns a first-come queue into something closer to arbitrary
  favoritism, and a registrant who was skipped over has no way to know it happened.
DISCONFIRMING_OBSERVATION: >
  With more than one registrant on the waiting list, a freed seat is promoted to someone other
  than the registrant holding the earliest waiting position, with no documented exception rule
  explaining why.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Place at least three registrants on the waiting list in a known order, free exactly one seat
  through a cancellation, and check which waiting registrant is promoted.
```

## G11-EVENT-Q005

```yaml
QID: G11-EVENT-Q005
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A waiting registrant is only promoted once the cancellation that freed the seat is itself
  finalized — for example, any required refund step has been resolved — not the instant the
  cancellation request is merely submitted.
WHY_IT_MATTERS: >
  Promoting on a cancellation that is later reversed or fails to complete would double-book the
  seat between the reinstated original registrant and the newly promoted one.
DISCONFIRMING_OBSERVATION: >
  A waiting registrant is promoted into a seat whose freeing cancellation has not yet finished
  processing, and the original registrant's cancellation is later reversed or fails, leaving two
  registrants holding one seat.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Submit a cancellation that has an intermediate unresolved step, and check whether a waiting
  registrant is promoted before that step resolves.
```

## G11-EVENT-Q006

```yaml
QID: G11-EVENT-Q006
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Money is never captured from a registrant before a seat is actually and durably held for them;
  a payment cannot be taken and then discovered, after the fact, to correspond to no reserved seat
  at all.
WHY_IT_MATTERS: >
  Taking money with no corresponding seat inverts the obligation the payment is supposed to
  represent, and unwinding it after the registrant believes they are booked is a worse customer
  outcome than refusing the registration up front.
DISCONFIRMING_OBSERVATION: >
  A registrant's payment is captured and later, no seat is found to be held for them at all — not
  even a held-pending-confirmation seat — with no automatic refund triggered.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Trigger a payment capture for a registration and, before any confirmation step completes,
  inspect whether a seat is actually held against capacity for that registrant.
```

## G11-EVENT-Q007

```yaml
QID: G11-EVENT-Q007
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A registration that is marked confirmed while its payment has not yet settled is distinguishable,
  in the occasion's own records, from a registration that is confirmed and fully paid — the two
  are not merged into one indistinguishable "confirmed" state.
WHY_IT_MATTERS: >
  If a not-yet-paid confirmation looks identical to a paid one, staff at the door and financial
  reporting both act on a promise that has not actually been kept, and a later payment failure has
  no distinguishable record to unwind from.
DISCONFIRMING_OBSERVATION: >
  A registration confirmed with payment still outstanding cannot be distinguished, in any view of
  the occasion, from one that is both confirmed and paid.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a registration whose confirmation step completes before its payment settles, and compare
  its recorded state against a registration that is both confirmed and paid.
```

## G11-EVENT-Q008

```yaml
QID: G11-EVENT-Q008
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A registration whose payment has been captured but which never reaches a confirmed state is
  surfaced as an exception requiring resolution, not left indefinitely in limbo with no visible
  owner or deadline.
WHY_IT_MATTERS: >
  A paid-but-unconfirmed registrant has given money for something the system itself has not
  committed to honoring, and an indefinite silent limbo state means neither the registrant nor
  staff ever learns the seat was never actually secured.
DISCONFIRMING_OBSERVATION: >
  A registration remains paid-but-unconfirmed with no time bound, no flag, and no listing that
  surfaces it as needing resolution.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Capture payment for a registration and deliberately halt before its confirmation step, then
  check whether anything surfaces the resulting limbo state.
```

## G11-EVENT-Q009

```yaml
QID: G11-EVENT-Q009
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing an occasion's date after registrants have already paid produces a visible, attributable
  flag on every affected registration, distinct from registrations made after the date was already
  changed.
WHY_IT_MATTERS: >
  A registrant who paid for one date and was silently moved to another has a claim to a refund or
  reconfirmation that the organizer needs to be able to see and act on, not discover only when the
  registrant complains.
DISCONFIRMING_OBSERVATION: >
  The occasion's date is changed after paid registrations exist, and none of those prior
  registrations carry any indication that the date they paid for is no longer the current one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Register and pay for an occasion, then change its scheduled date, and inspect whether the prior
  registration reflects that a change occurred relative to what was originally paid for.
```

## G11-EVENT-Q010

```yaml
QID: G11-EVENT-Q010
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing an occasion's location after registrants have paid is treated as materially equivalent
  to a date change for notification purposes — it does not silently update with no distinguishable
  trace that anything changed for those already registered.
WHY_IT_MATTERS: >
  A registrant who travels based on a location that was later changed without their knowledge
  experiences a real-world failure the system had every means to prevent by simply flagging the
  change.
DISCONFIRMING_OBSERVATION: >
  The occasion's location changes after paid registrations exist and no record, notice mechanism,
  or flag distinguishes those prior registrants as needing to be told.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Register and pay for an occasion, then change its location, and check whether the system creates
  any trace that existing registrants may need to be informed.
```

## G11-EVENT-Q011

```yaml
QID: G11-EVENT-Q011
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an occasion that has paid registrants in place drives every one of those registrants
  into a state requiring refund resolution; none is left marked simply "cancelled" with its
  payment untouched and unaccounted for.
WHY_IT_MATTERS: >
  A cancelled occasion that leaves paid registrants' money unaddressed is a direct, quantifiable
  financial exposure and almost certainly a legal one.
DISCONFIRMING_OBSERVATION: >
  After cancelling an occasion with paid registrants, at least one paid registration shows a final
  cancelled state with no refund pending, issued, or otherwise recorded against it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create paid registrations against an occasion, cancel the occasion itself, and check the
  resulting state and refund status of each previously paid registration.
```

## G11-EVENT-Q012

```yaml
QID: G11-EVENT-Q012
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When an occasion is cancelled, whatever value was already recognized in the ledger for its
  registrations is reversed at the point of cancellation, not left to stand as if the fixed date
  had actually occurred and the obligation had been discharged.
WHY_IT_MATTERS: >
  Leaving recognized value on the books for something that was cancelled before it happened
  misstates what was actually earned, in whichever period the misstatement lands.
DISCONFIRMING_OBSERVATION: >
  An occasion is cancelled after some portion of its registration value was already recognized,
  and that recognized value is not reversed or otherwise corrected as part of the cancellation.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Reach a point where value from paid registrations has already been recognized, cancel the
  occasion, and check whether that recognized value is reversed.
```

## G11-EVENT-Q013

```yaml
QID: G11-EVENT-Q013
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A registration cannot be cancelled, in the ordinary cancellation path, after attendance has
  already been recorded for it — the two facts are not allowed to coexist without an explicit,
  distinguishable override.
WHY_IT_MATTERS: >
  Someone who is recorded as having attended and is then quietly cancelled creates a record that
  contradicts itself, which corrupts attendance-based reporting and any obligation tied to having
  attended.
DISCONFIRMING_OBSERVATION: >
  A registration with recorded attendance is cancelled through the ordinary path with no distinct
  override step, warning, or trace showing that attendance already existed at the time of
  cancellation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record attendance for a registrant, then attempt to cancel that same registration through the
  standard cancellation action, and observe whether it is blocked, flagged, or silently allowed.
```

## G11-EVENT-Q014

```yaml
QID: G11-EVENT-Q014
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Attendance cannot be recorded for a person who holds no registration for the occasion at all,
  without that attendance record itself being visibly exceptional — for example, requiring a
  distinct walk-in path rather than the ordinary check-in of a registrant.
WHY_IT_MATTERS: >
  If unregistered attendance looks identical to registered attendance, capacity counts,
  revenue-per-attendee figures, and post-occasion reporting all silently absorb people who were
  never accounted for.
DISCONFIRMING_OBSERVATION: >
  A person with no registration record for the occasion is checked in as attended through the same
  path and with the same resulting record as a registered attendee, with nothing distinguishing
  the two.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Attempt to record attendance for a person who has no registration on the occasion, using the
  ordinary check-in action, and compare the resulting record to that of a registered attendee.
```

## G11-EVENT-Q015

```yaml
QID: G11-EVENT-Q015
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When the same person registers for the same occasion a second time, the occasion either
  recognizes the existing registration and does not create a second seat-consuming record, or
  explicitly flags the duplicate for a human decision — it does not silently hold two seats
  against one attendee with no link between the two records.
WHY_IT_MATTERS: >
  An unnoticed duplicate consumes a second seat that another person could have used, and inflates
  both the registrant count and any capacity or revenue figure derived from it.
DISCONFIRMING_OBSERVATION: >
  The same identifiable person is registered twice for the same occasion, consuming two seats,
  with no flag, link, or merge connecting the two records.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Register the same identifiable person for the same occasion twice in separate actions and
  inspect whether the second registration is linked, blocked, or flagged relative to the first.
```

## G11-EVENT-Q016

```yaml
QID: G11-EVENT-Q016
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Transferring a registration to a different person carries forward its payment and seat, and does
  not require or silently trigger a second payment or a second seat allocation for the same
  underlying registration.
WHY_IT_MATTERS: >
  If a transfer is treated as a brand-new registration rather than a change of holder, the
  original payment is left orphaned and the seat may be counted twice against capacity during the
  transition.
DISCONFIRMING_OBSERVATION: >
  Transferring a registration to another person results in either a second payment being requested
  for the same seat, or a second seat being counted against capacity during or after the transfer.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Register and pay for a seat, then transfer that registration to a different named person, and
  check the resulting payment record and capacity count.
```

## G11-EVENT-Q017

```yaml
QID: G11-EVENT-Q017
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Reducing an occasion's configured capacity below the number of registrants already confirmed
  does not retroactively cancel, hide, or silently reclassify any of the registrants already
  holding a seat; the excess relative to the new capacity is surfaced as an exception for a human
  to resolve.
WHY_IT_MATTERS: >
  A registrant who already holds a confirmed seat should not lose it to a configuration change
  made after the fact without anyone actually deciding who, specifically, is affected.
DISCONFIRMING_OBSERVATION: >
  Capacity is reduced below the current confirmed count and one or more previously confirmed
  registrants disappear from the registrant list, or their state changes, with no explicit action
  taken against them individually.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Confirm registrants up to a known count, then reduce the occasion's configured capacity below
  that count, and inspect what happens to the existing registrants and whether an exception is
  raised.
```

## G11-EVENT-Q018

```yaml
QID: G11-EVENT-Q018
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Increasing capacity while a waiting list exists produces automatic promotion of waiting
  registrants up to the newly available seats only where that automatic behavior has been
  explicitly configured; otherwise the newly opened seats and the existing waiting list both
  remain visible and neither is silently discarded.
WHY_IT_MATTERS: >
  A waiting registrant who is owed a seat under a capacity increase but is never promoted, and
  never told a seat opened, has effectively lost their place without any decision being made about
  it.
DISCONFIRMING_OBSERVATION: >
  Capacity is increased while a waiting list exists, and the newly available seats are neither
  offered to the waiting registrants nor left visibly open — they simply vanish from any
  accounting of remaining capacity.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Fill an occasion to capacity with a nonempty waiting list, increase the configured capacity, and
  check whether the newly available seats are reflected anywhere and whether waiting registrants
  are promoted or notified.
```

## G11-EVENT-Q019

```yaml
QID: G11-EVENT-Q019
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A registration attempt submitted at the precise configured cutoff moment is resolved consistently
  to one side of that boundary — either always accepted or always refused at that instant — rather
  than depending on which internal step happens to check the clock first.
WHY_IT_MATTERS: >
  An inconsistent boundary means two registrants submitting at what looks like the same instant
  can receive different outcomes for no reason either of them could explain, and no rule anyone
  could audit against.
DISCONFIRMING_OBSERVATION: >
  Two registration attempts submitted at what is recorded as the same cutoff instant receive
  different outcomes — one accepted, one refused — with no other distinguishing factor between
  them.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Configure a registration cutoff moment, submit registration attempts timed to land exactly at
  that moment from more than one path, and compare the outcomes.
```

## G11-EVENT-Q020

```yaml
QID: G11-EVENT-Q020
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Whether a cancellation submitted exactly at, or immediately after, the occasion's fixed date is
  still eligible for a refund is governed by an explicit, checkable rule, not by whichever
  timestamp a particular process step happens to record.
WHY_IT_MATTERS: >
  A registrant's entitlement to money back should not depend on an implementation accident of
  which internal clock read the time a few seconds earlier or later.
DISCONFIRMING_OBSERVATION: >
  Two cancellations submitted at effectively the same moment relative to the fixed date receive
  different refund-eligibility outcomes with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit cancellations timed to land at and just after the occasion's fixed date and compare the
  refund eligibility each receives against any documented cutoff rule.
```

## G11-EVENT-Q021

```yaml
QID: G11-EVENT-Q021
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The point at which registration revenue is recognized — at payment, at the fixed date, or spread
  across the period between — is a single, consistently applied rule for the occasion, not
  something that varies registrant by registrant depending on when each happened to pay.
WHY_IT_MATTERS: >
  Inconsistent recognition timing across registrants for the same occasion would make the
  occasion's own revenue figures internally incoherent and impossible to reconcile against any
  single accounting policy.
DISCONFIRMING_OBSERVATION: >
  Two registrants who paid at different times for the same occasion have their payments recognized
  under visibly different timing rules, with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Register and pay for the same occasion at two different times relative to its fixed date, and
  compare when each payment's value is recognized.
```

## G11-EVENT-Q022

```yaml
QID: G11-EVENT-Q022
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a merely held, not-yet-confirmed registration is counted against the occasion's
  remaining capacity is a single explicit rule applied uniformly, so that the number of seats
  reported as "remaining" always means the same thing to whoever is looking at it.
WHY_IT_MATTERS: >
  If held and confirmed registrations are counted inconsistently, capacity can appear open when it
  is not, or appear full when seats are actually available, either of which misleads whoever
  relies on that number.
DISCONFIRMING_OBSERVATION: >
  The remaining-capacity figure changes depending on which view or process is asked, because held
  and confirmed registrations are counted differently in different places.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Create a held but unconfirmed registration and compare the remaining-capacity figure reported by
  more than one view or process against the occasion.
```

## G11-EVENT-Q023

```yaml
QID: G11-EVENT-Q023
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a cancellation frees a seat at the same moment a brand-new registration attempt, not from
  the waiting list, is submitted, the waiting list, if one exists, takes priority over the new
  attempt for that freed seat.
WHY_IT_MATTERS: >
  A registrant who has been waiting should not lose their place to someone who happened to submit
  a fresh registration attempt at the exact same instant a seat opened.
DISCONFIRMING_OBSERVATION: >
  A seat freed by cancellation, with a nonempty waiting list in place, is given to a brand-new
  registration attempt submitted at the same time rather than to the earliest waiting registrant.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  With a nonempty waiting list, trigger a cancellation and, at the same moment, submit a new
  registration attempt not drawn from the waiting list, and observe which one receives the freed
  seat.
```

## G11-EVENT-Q024

```yaml
QID: G11-EVENT-Q024
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When several cancellations happen close together and free several seats at once, the resulting
  promotions from the waiting list are each applied exactly once, so the total number of
  registrants promoted equals the number of seats actually freed, never more.
WHY_IT_MATTERS: >
  An off-by-one or duplicated promotion under simultaneous cancellations would either strand an
  owed waiting registrant or oversell the newly freed seats.
DISCONFIRMING_OBSERVATION: >
  Several near-simultaneous cancellations free a known number of seats, and the number of
  registrants actually promoted from the waiting list does not equal that number.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  With several registrants on the waiting list, trigger multiple cancellations in close succession
  and count how many waiting registrants are promoted against how many seats were freed.
```

## G11-EVENT-Q025

```yaml
QID: G11-EVENT-Q025
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A registrant who paid through one channel and cancels through a different channel has that
  cancellation correctly matched back to the original payment, so the refund, if any, is issued
  against the actual amount and method originally collected.
WHY_IT_MATTERS: >
  A mismatch between the channel a payment came in on and the channel a cancellation is processed
  through risks a refund going to the wrong method, the wrong amount, or not being triggered at
  all.
DISCONFIRMING_OBSERVATION: >
  A registrant pays through one channel, cancels through another, and the resulting refund, or its
  absence, does not correctly correspond to the original payment's amount and method.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Register and pay through one available channel, then submit the cancellation through a different
  available channel, and check whether the refund correctly traces back to the original payment.
```

## G11-EVENT-Q026

```yaml
QID: G11-EVENT-Q026
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where ticket types carry their own price, the amount actually charged to a registrant is
  governed by the ticket type they selected, not by an occasion-level default that could silently
  override or be silently overridden by it.
WHY_IT_MATTERS: >
  An unresolved conflict between a ticket type's price and an occasion-level price would mean the
  amount actually charged depends on an internal precedence nobody explicitly decided, rather than
  on what was configured for that specific type.
DISCONFIRMING_OBSERVATION: >
  A registrant selecting a specific ticket type is charged an amount that does not match that
  ticket type's configured price, with no explicit override recorded to explain the difference.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure an occasion-level price alongside a differently priced ticket type, register under
  that ticket type, and check the amount actually charged.
```

## G11-EVENT-Q027

```yaml
QID: G11-EVENT-Q027
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A registrant who never selects a ticket type explicitly cannot be silently assigned to a ticket
  type that has already sold out, purely because the occasion overall still shows open capacity.
WHY_IT_MATTERS: >
  Silently assigning an exhausted ticket type would produce a registrant who believes, and was
  told, they hold a type that no longer has any allotment left, corrupting whatever that type
  controls.
DISCONFIRMING_OBSERVATION: >
  A registration with no explicit ticket-type selection is assigned to a ticket type whose own
  allotment was already exhausted at the time of registration.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Exhaust one ticket type's allotment while the occasion overall retains open capacity, then
  submit a registration without explicitly selecting a ticket type, and check which type it is
  assigned.
```

## G11-EVENT-Q028

```yaml
QID: G11-EVENT-Q028
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether multiple ticket types draw from one shared capacity pool or each holds its own private
  allotment is a single explicit configuration choice for the occasion, and every ticket type on
  that occasion is governed by the same choice rather than a mix of the two behaviors.
WHY_IT_MATTERS: >
  A silent mix of shared and private pools within one occasion would make the meaning of
  "remaining capacity" different for different ticket types on the same occasion, with no way for
  staff to reason about it correctly.
DISCONFIRMING_OBSERVATION: >
  On a single occasion, one ticket type's registrations visibly draw down the overall shared
  capacity while another ticket type's registrations do not, with no configuration documenting why
  they differ.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an occasion with more than one ticket type and register against each, checking whether
  each registration draws down a shared capacity figure or a private one.
```

## G11-EVENT-Q029

```yaml
QID: G11-EVENT-Q029
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Staff associated with one company cannot view the registrant list, contact details, or payment
  status of an occasion that belongs to a different company, in the ordinary listing and detail
  views.
WHY_IT_MATTERS: >
  Registrant lists carry personal and payment information; letting one company's staff see another
  company's registrants without an explicit sharing decision is exactly the kind of cross-tenant
  leakage that turns a multi-company setup into a liability.
DISCONFIRMING_OBSERVATION: >
  Staff scoped to one company can view the registrant list, contact details, or payment status of
  an occasion owned by a different company, with no explicit sharing configured.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create occasions under two different companies with registrants on each, then attempt to view
  one company's occasion registrant list while scoped as staff of the other company.
```

## G11-EVENT-Q030

```yaml
QID: G11-EVENT-Q030
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A person who registers for an occasion belonging to one company does not, by that act alone,
  become visible or reachable as a contact to a different company that person has no other
  relationship with.
WHY_IT_MATTERS: >
  An occasion's registrant list should not become a backdoor for one company in a multi-company
  setup to acquire contacts that belong, by rights, only to the company running that specific
  occasion.
DISCONFIRMING_OBSERVATION: >
  A registrant for one company's occasion appears as an accessible contact to a different company
  that had no other relationship with that person before the registration.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Register a person, who has no prior relationship with any other company, for an occasion owned
  by one specific company, then check whether that person becomes visible as a contact under a
  different company.
```

## G11-EVENT-Q031

```yaml
QID: G11-EVENT-Q031
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Changing an occasion's configured capacity after registrations have already opened requires a
  role or permission distinct from the one needed merely to view or manage individual
  registrations.
WHY_IT_MATTERS: >
  Capacity is the number every other invariant in this bank depends on; letting anyone who can
  process a single registration also silently change the ceiling for everyone else is a
  disproportionate amount of authority handed out by accident.
DISCONFIRMING_OBSERVATION: >
  An account whose role is limited to processing individual registrations is able to change the
  occasion's overall configured capacity once registrations are already open.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  With registrations already open on an occasion, attempt to change its configured capacity using
  an account whose role is scoped only to processing individual registrations.
```

## G11-EVENT-Q032

```yaml
QID: G11-EVENT-Q032
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Issuing a refund for a cancelled or discounted registration requires an explicit authorization
  distinct from the authority to simply record that a registration was cancelled.
WHY_IT_MATTERS: >
  Separating "mark cancelled" from "move money back" is a basic control against a single account
  being able to both create and approve a financial reversal unilaterally.
DISCONFIRMING_OBSERVATION: >
  An account able to cancel a registration can also issue its refund with no additional
  authorization step distinguishing the two actions.
EXPECTED_SURFACE: S4,S2
PRECONDITIONS: >
  Using an account with only cancellation authority, cancel a paid registration and attempt to
  issue its refund, checking whether an additional authorization is required.
```

## G11-EVENT-Q033

```yaml
QID: G11-EVENT-Q033
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether attendance can be recorded at all before the occasion's fixed date has actually arrived
  is governed by an explicit configuration, not an accidental side effect of the check-in action
  having no date guard.
WHY_IT_MATTERS: >
  Attendance recorded before an occasion has even happened is either meaningless or a sign that
  the check-in path has no relationship at all to the occasion's own schedule, either of which
  corrupts any attendance-based figure.
DISCONFIRMING_OBSERVATION: >
  Attendance can be recorded for an occasion whose fixed date has not yet arrived, and nothing in
  configuration or the action itself acknowledges that this is happening early.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to record attendance for a registrant on an occasion whose fixed date is still in the
  future, and check whether the action is guarded, flagged, or silently allowed.
```

## G11-EVENT-Q034

```yaml
QID: G11-EVENT-Q034
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  If a manual override exists to register someone past the occasion's configured capacity, using
  it produces a visible, attributable flag distinguishing that registration from an ordinary
  within-capacity one.
WHY_IT_MATTERS: >
  An override that looks identical to an ordinary registration erases the very distinction —
  deliberate exception versus enforced limit — that the override exists to preserve for later
  audit.
DISCONFIRMING_OBSERVATION: >
  A registration created through a capacity-exceeding override is indistinguishable, in its own
  record, from an ordinary registration made within capacity.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Fill an occasion to its configured capacity, then use whatever override exists to register one
  more person past it, and inspect whether that registration's record differs from an ordinary
  one.
```

## G11-EVENT-Q035

```yaml
QID: G11-EVENT-Q035
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Submitting a cancellation for a registration that is already cancelled has no further effect —
  it does not trigger a second refund, a second freed-seat promotion, or a second audit entry as
  if a new cancellation had genuinely occurred.
WHY_IT_MATTERS: >
  A cancellation action that is not idempotent could double-refund a registrant or promote two
  waiting registrants for the one seat that was actually freed.
DISCONFIRMING_OBSERVATION: >
  Submitting a cancellation a second time against an already-cancelled registration triggers a
  second refund, a second waiting-list promotion, or another materially new effect.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Cancel a paid registration, then submit the same cancellation action against it a second time,
  and observe whether any further refund or promotion effect occurs.
```

## G11-EVENT-Q036

```yaml
QID: G11-EVENT-Q036
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Re-opening an occasion that was previously cancelled does not automatically reinstate the
  registrations that existed at the time of cancellation as if they were still active and
  unaffected by everything that happened in between.
WHY_IT_MATTERS: >
  A registrant who was refunded when the occasion was cancelled should not silently reappear as a
  confirmed, paid attendee the moment the occasion is reactivated, with no new decision made about
  their status.
DISCONFIRMING_OBSERVATION: >
  Re-opening a previously cancelled occasion restores its prior registrations to a confirmed state
  automatically, including ones that had already been refunded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel an occasion that has paid registrations, allow refunds to process, then re-open the
  occasion, and check the resulting state of the previously refunded registrations.
```

## G11-EVENT-Q037

```yaml
QID: G11-EVENT-Q037
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Reverting a confirmed registration back to a draft or pending state releases the seat it was
  holding back to available capacity, rather than leaving the seat counted as held against a
  registration that is no longer confirmed.
WHY_IT_MATTERS: >
  A seat held by a registration that is no longer actually confirmed, but is not released either,
  is capacity that looks full to everyone else while actually representing nothing committed.
DISCONFIRMING_OBSERVATION: >
  A registration reverted from confirmed to draft or pending continues to count against occasion
  capacity as if it were still confirmed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm a registration, then revert it to a draft or pending state, and check whether the
  occasion's counted capacity changes accordingly.
```

## G11-EVENT-Q038

```yaml
QID: G11-EVENT-Q038
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a registrant holding a waiting position withdraws from the waiting list, every registrant
  behind them in the queue moves up by exactly one position, so no gap or ambiguity is left in the
  ordering.
WHY_IT_MATTERS: >
  A gap left in the waiting order, or an ambiguous ordering after a withdrawal, would make the next
  promotion decision arbitrary rather than a continuation of the original first-come order.
DISCONFIRMING_OBSERVATION: >
  After a waiting registrant withdraws, the remaining waiting registrants' relative order shows a
  gap, a duplicate position, or an ambiguity rather than a clean shift of exactly one position.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Place at least three registrants on the waiting list in order, withdraw the one in the middle,
  and inspect the resulting order of the remaining two.
```

## G11-EVENT-Q039

```yaml
QID: G11-EVENT-Q039
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A refund issued against a registration can never exceed the amount actually collected for that
  registration; there is no path by which the refunded figure is computed independently of, and
  larger than, what was actually paid.
WHY_IT_MATTERS: >
  A refund larger than the original payment is a direct, quantifiable loss with no revenue ever
  having existed to justify it.
DISCONFIRMING_OBSERVATION: >
  A refund is issued, or is even permitted to be entered, for an amount greater than what was
  actually collected on the registration it targets.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Attempt to issue a refund larger than the amount actually collected for a specific paid
  registration and observe whether it is blocked or allowed.
```

## G11-EVENT-Q040

```yaml
QID: G11-EVENT-Q040
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A refund issued after the accounting period in which the original charge was recognized has
  already closed is recorded in the current open period as its own distinct entry, rather than
  being silently backdated into the already-closed period.
WHY_IT_MATTERS: >
  Silently altering a closed period's figures to accommodate a later refund would misstate results
  that have already been reported and, in some cases, already relied on.
DISCONFIRMING_OBSERVATION: >
  A refund issued after the original charge's period has closed is recorded as altering that
  already-closed period's figures rather than as a new entry in the current period.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Let the accounting period containing an original paid registration's charge close, then issue a
  refund against that registration, and check which period reflects the refund.
```

## G11-EVENT-Q041

```yaml
QID: G11-EVENT-Q041
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If the commercial transaction that created a registration is itself cancelled upstream, the
  registration reflects that cancellation rather than continuing to show as an active, confirmed
  registrant unrelated to what happened to the transaction that created it.
WHY_IT_MATTERS: >
  A registrant who no longer has any underlying paid or committed transaction, but still shows as
  confirmed, is an entitlement the occasion is honoring for free and without anyone deciding to
  grant it.
DISCONFIRMING_OBSERVATION: >
  The commercial transaction underlying a registration is cancelled, and the registration itself
  continues to show as active and confirmed with no reflection of that cancellation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a registration originating from a commercial transaction, cancel that originating
  transaction, and check whether the registration's own state reflects the cancellation.
```

## G11-EVENT-Q042

```yaml
QID: G11-EVENT-Q042
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Revoking a previously recorded attendance does not, by itself, free the seat back to available
  capacity if the underlying registration is otherwise still confirmed and current — attendance
  and seat-holding are tracked as separate facts.
WHY_IT_MATTERS: >
  If revoking an attendance mark accidentally also frees the seat, a still-registered, still-paid
  attendee could find their seat handed to someone else purely because a check-in was corrected.
DISCONFIRMING_OBSERVATION: >
  Revoking a recorded attendance changes the occasion's counted remaining capacity, even though the
  underlying registration itself was never cancelled.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record attendance for a confirmed registrant, then revoke that recorded attendance without
  cancelling the registration itself, and check whether remaining capacity changes.
```

## G11-EVENT-Q043

```yaml
QID: G11-EVENT-Q043
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Every change to an occasion's configured capacity is captured with who made it and when,
  retrievable after the fact, not merely reflected as a new number with the history of how it got
  there lost.
WHY_IT_MATTERS: >
  Capacity is the number every seat-related invariant in this bank depends on; a capacity change
  with no record of who made it or when defeats any later attempt to explain an overselling
  incident.
DISCONFIRMING_OBSERVATION: >
  An occasion's configured capacity has changed from its original value, and no record exists of
  who changed it or when.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change an occasion's configured capacity through the ordinary path and then attempt to retrieve
  who made the change and when.
```

## G11-EVENT-Q044

```yaml
QID: G11-EVENT-Q044
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When a waiting registrant is promoted into a freed seat, the record of that promotion identifies
  both which registrant was promoted and which cancellation freed the seat they took, so the chain
  can be reconstructed after the fact.
WHY_IT_MATTERS: >
  Without that link, a dispute over who should have gotten a particular seat has no evidence trail
  to resolve it either way.
DISCONFIRMING_OBSERVATION: >
  A waiting registrant is promoted into a freed seat, and no record connects that promotion to the
  specific cancellation that freed the seat.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger a cancellation that promotes a waiting registrant, then attempt to trace, from the
  promotion record alone, which cancellation freed the seat.
```

## G11-EVENT-Q045

```yaml
QID: G11-EVENT-Q045
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Personal data collected from registrants is not retained beyond whatever retention rule the
  organization has configured for it; the occasion having passed does not, by itself, remove or
  reduce access to that data absent an explicit retention decision.
WHY_IT_MATTERS: >
  Registrant personal data kept indefinitely with no policy behind it is exposure with no
  corresponding business purpose, and the longer it sits, the larger that exposure grows.
DISCONFIRMING_OBSERVATION: >
  Registrant personal data remains fully accessible long after the occasion has passed with no
  retention configuration governing it at all, and no distinction from data on a still-upcoming
  occasion.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Locate an occasion whose fixed date passed well in the past and check whether its registrants'
  personal data is still fully accessible and whether any retention configuration applies to it.
```

## G11-EVENT-Q046

```yaml
QID: G11-EVENT-Q046
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A registrant whose registration was cancelled before the occasion ever occurred is not treated,
  for data-exposure purposes, identically to a registrant who actually attended — the fact that
  they never attended is itself recorded and does not disappear.
WHY_IT_MATTERS: >
  Conflating "registered and cancelled" with "attended" in reporting or in what is retained
  overstates who actually took part and misrepresents the occasion's real reach.
DISCONFIRMING_OBSERVATION: >
  A cancelled-before-the-fact registrant appears in attendance-based reporting or exports
  indistinguishably from someone who actually attended.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a registration before the occasion's fixed date arrives, then check whether that person
  appears in any attendance-based report or export as if they had attended.
```

## G11-EVENT-Q047

```yaml
QID: G11-EVENT-Q047
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a registration is cancelled directly, not through its originating transaction, whatever
  created that registration in the first place is made aware of the cancellation rather than
  continuing to believe the registration is still active.
WHY_IT_MATTERS: >
  An originating process that still believes a registration is active, when it has actually been
  cancelled directly, can act on stale information — following up, invoicing, or reporting on
  something that no longer exists.
DISCONFIRMING_OBSERVATION: >
  A registration is cancelled directly, and whatever created it originally continues to show or
  act on it as if it were still active.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a registration through whatever process originates it, cancel the registration directly
  rather than through that originating process, and check whether the originating process reflects
  the cancellation.
```

## G11-EVENT-Q048

```yaml
QID: G11-EVENT-Q048
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An occasion configured with zero seats of capacity refuses every ordinary registration attempt
  outright, rather than accepting registrations into an undefined or negative remaining-capacity
  state.
WHY_IT_MATTERS: >
  A capacity of zero is a legitimate configuration — a placeholder, a not-yet-finalized occasion —
  and registrations silently accepted against it would produce a state that has no honest
  interpretation at all.
DISCONFIRMING_OBSERVATION: >
  An occasion configured with zero capacity accepts an ordinary registration attempt, producing a
  negative or otherwise nonsensical remaining-capacity figure.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an occasion with zero capacity and attempt an ordinary registration against it,
  observing whether it is refused and what the remaining-capacity figure shows.
```

## G11-EVENT-Q049

```yaml
QID: G11-EVENT-Q049
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An occasion configured with exactly one seat of capacity behaves, under simultaneous registration
  attempts, exactly as the general capacity-limit invariant requires at any other size — exactly
  one attempt succeeds, never zero and never two.
WHY_IT_MATTERS: >
  The smallest possible capacity is the sharpest test of the concurrency guarantee the whole bank
  is built around, and a special-case failure at the boundary of one seat would slip past testing
  done only at larger, more forgiving capacities.
DISCONFIRMING_OBSERVATION: >
  An occasion configured with exactly one seat, under simultaneous registration attempts, ends
  with either zero confirmed registrants or more than one.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Configure an occasion with exactly one seat of capacity, submit two or more simultaneous
  registration attempts against it, and count the confirmed outcome.
```

## G11-EVENT-Q050

```yaml
QID: G11-EVENT-Q050
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a freed seat is promoted to the waiting list automatically, or only ever through a
  deliberate staff action, is an explicit configuration choice with a documented default, not an
  unconfigurable, always-on assumption baked into the cancellation path.
WHY_IT_MATTERS: >
  An organization that wants every promotion reviewed by a person before it happens needs the
  ability to actually turn automatic promotion off, or it has no real control over who ends up in a
  seat.
DISCONFIRMING_OBSERVATION: >
  No configuration exists to control whether promotion from the waiting list happens automatically
  on cancellation or requires a deliberate staff action; the behavior is fixed with no documented
  default either way.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Search the occasion's configuration for a setting governing automatic promotion from the waiting
  list, and, if none exists, attempt to determine what the fixed default behavior actually is.
```

## G11-EVENT-Q051

```yaml
QID: G11-EVENT-Q051
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  If sending a cancellation notification to registrants is configurable, disabling it changes only
  whether the notification is sent, not whether the underlying cancellation, refund, and audit
  steps themselves still occur in full.
WHY_IT_MATTERS: >
  An organization that has disabled automatic notifications, intending to contact registrants
  personally instead, still needs the refund and cancellation itself to happen correctly — a
  notification toggle should not be able to silently gate the substance of the cancellation.
DISCONFIRMING_OBSERVATION: >
  With cancellation notifications disabled, the underlying cancellation, its refund step, or its
  audit entry also fails to occur, as if the notification setting controlled more than just the
  notification.
EXPECTED_SURFACE: S1,S2,S6,S7
PRECONDITIONS: >
  Disable cancellation notifications in configuration, cancel a paid registration, and verify
  whether the refund and audit steps still occur despite no notification being sent.
```

## G11-EVENT-Q052

```yaml
QID: G11-EVENT-Q052
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A cancellation submitted after the occasion's fixed date has already passed, for a registrant who
  was never actually recorded as attending, is governed by an explicit rule about refund
  eligibility at that point — it is not automatically treated the same as a cancellation submitted
  well in advance.
WHY_IT_MATTERS: >
  The fixed date passing is the point at which the organization's own costs and obligations are
  typically already committed, so refund policy at that boundary needs to be a decision, not an
  accident of however the cancellation path happens to be built.
DISCONFIRMING_OBSERVATION: >
  A cancellation submitted after the fixed date has passed, for someone never recorded as
  attending, receives the identical refund outcome as one submitted well before the date, with no
  distinguishing rule applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Let an occasion's fixed date pass without recording attendance for a specific paid registrant,
  then submit a cancellation for that registrant and compare the refund outcome to an equivalent
  cancellation submitted before the date.
```

## G11-EVENT-Q053

```yaml
QID: G11-EVENT-Q053
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Whether the organization's obligation to a registrant is considered fulfilled at the moment of
  recorded attendance, or simply at the moment the fixed date passes regardless of attendance, is a
  single explicit rule applied consistently, not something that differs registrant by registrant
  on the same occasion.
WHY_IT_MATTERS: >
  This single decision governs whether a no-show registrant who never attended is still owed
  anything, and inconsistency here means two otherwise identical no-shows could be treated
  completely differently with no rule to point to.
DISCONFIRMING_OBSERVATION: >
  Two registrants who both failed to attend the same occasion are treated as having received their
  obligation under visibly different rules, with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Identify two registrants on the same occasion who did not attend, and compare how each is
  treated with respect to the obligation being considered fulfilled.
```

## G11-EVENT-Q054

```yaml
QID: G11-EVENT-Q054
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Where two ticket types are independently priced and each holds its own capacity pool, the
  occasion's own reported "sold out" state correctly reflects that one type can be exhausted while
  the occasion, and the other type, still have room — it does not report the whole occasion as
  sold out because one type ran out, nor as open because the other still has room.
WHY_IT_MATTERS: >
  A registrant told an occasion is "sold out" when a differently priced type is actually still
  available has been turned away from something they could, in fact, still have bought.
DISCONFIRMING_OBSERVATION: >
  One ticket type's allotment is exhausted while another type on the same occasion still has room,
  and the occasion's overall reported availability does not correctly reflect that mixed state.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Exhaust one ticket type's allotment while a second, differently priced type on the same occasion
  still has room, and check what the occasion's own overall availability indicator reports.
```

## G11-EVENT-Q055

```yaml
QID: G11-EVENT-Q055
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A pending registration that is never confirmed within whatever hold period is configured is
  automatically released back to available capacity at the end of that period, rather than
  continuing to hold a seat indefinitely with no confirmation ever completing.
WHY_IT_MATTERS: >
  A seat held indefinitely by an abandoned, unconfirmed registration is capacity that looks
  unavailable to every other prospective registrant while representing nothing anyone actually
  committed to.
DISCONFIRMING_OBSERVATION: >
  A pending registration remains held against capacity well past the configured hold period with
  no confirmation ever completing and no automatic release occurring.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create a pending registration and allow the configured hold period to elapse without confirming
  it, then check whether the seat is released back to available capacity.
```

## G11-EVENT-Q056

```yaml
QID: G11-EVENT-Q056
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The moment a cancellation is deemed final for the purpose of refund-eligibility rules is the
  moment it is submitted by the registrant, not some later moment at which staff happen to process
  it, so that a delay in processing cannot retroactively worsen the registrant's eligibility.
WHY_IT_MATTERS: >
  If the moment that counts is whenever staff get around to processing the cancellation, a
  registrant's refund eligibility becomes hostage to how busy the organization happens to be,
  rather than to their own timely action.
DISCONFIRMING_OBSERVATION: >
  Two registrants submit cancellations at the same time before a refund-eligibility deadline, but
  one is processed by staff after the deadline and receives a worse refund outcome purely because
  of that processing delay.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Submit a cancellation before a refund-eligibility deadline but arrange for staff processing of it
  to occur after the deadline, and compare the refund outcome to a cancellation processed
  immediately.
```

## G11-EVENT-Q057

```yaml
QID: G11-EVENT-Q057
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A capacity change made while registration is already underway applies only to registrations from
  that point forward; it does not retroactively alter the counted status of registrations already
  committed before the change was made.
WHY_IT_MATTERS: >
  Retroactively recounting already-committed registrants against a changed capacity could turn
  previously confirmed people into an apparent overage purely because of a later configuration
  edit, not anything they did.
DISCONFIRMING_OBSERVATION: >
  A capacity change made mid-window causes previously confirmed registrations, unchanged
  themselves, to be recounted or reclassified as if the new capacity had always applied.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm a set of registrations under one capacity value, change the capacity mid-window, and
  check whether the previously confirmed registrations' own status changes as a result.
```

## G11-EVENT-Q058

```yaml
QID: G11-EVENT-Q058
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a registration's payment fails after it had provisionally held the last available seat, that
  seat is released back to available capacity promptly enough that a competing registrant is not
  kept waiting on a seat that, in substance, was never actually secured.
WHY_IT_MATTERS: >
  A seat held hostage by a failed payment, at exactly the moment the occasion was full, directly
  costs a genuine prospective registrant a place they should have been able to take.
DISCONFIRMING_OBSERVATION: >
  A registration's payment fails after provisionally holding the last seat, and that seat remains
  unavailable to other registrants well beyond any reasonable processing delay.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Bring an occasion to its last available seat, provisionally hold it with a registration whose
  payment is then made to fail, and check how promptly the seat becomes available again.
```

## G11-EVENT-Q059

```yaml
QID: G11-EVENT-Q059
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A registrant holding a waiting position can see that they are on a waiting list, rather than
  being shown a status indistinguishable from a confirmed registration until the moment, if ever,
  they are promoted.
WHY_IT_MATTERS: >
  A registrant who believes they are confirmed, when they are actually only waiting, may make
  real-world plans around a seat they do not actually hold.
DISCONFIRMING_OBSERVATION: >
  A registrant holding only a waiting position is shown a status that does not distinguish their
  state from that of a confirmed registrant.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Place a registrant on the waiting list and check what status is shown to that registrant
  themselves, comparing it against what a confirmed registrant sees.
```

## G11-EVENT-Q060

```yaml
QID: G11-EVENT-Q060
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An occasion created under a specific company inherits that company's own configuration —
  currency, refund policy, notification settings — rather than falling back to a different
  company's configuration or to no configuration at all.
WHY_IT_MATTERS: >
  An occasion silently inheriting the wrong company's settings could charge in the wrong currency,
  apply the wrong refund policy, or send notifications under the wrong organizational identity.
DISCONFIRMING_OBSERVATION: >
  An occasion created under one company shows configuration values — currency, refund policy,
  notification settings — belonging to a different company or to no company at all.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Create occasions under two differently configured companies and compare the effective
  configuration each occasion actually uses against the company it was created under.
```

## G11-EVENT-Q061

```yaml
QID: G11-EVENT-Q061
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The capacity limit holds even when registration is attempted through more than one independent
  entry point — for example, a self-service path and a staff-assisted path — at the same time, not
  only when all attempts arrive through a single, already-serialized path.
WHY_IT_MATTERS: >
  A capacity guarantee that only holds when every registration comes through one path is not
  actually a guarantee once a second legitimate path to register exists, and most real occasions
  have more than one.
DISCONFIRMING_OBSERVATION: >
  With one seat remaining, simultaneous registration attempts through two different legitimate
  entry points both succeed, producing a confirmed count exceeding capacity.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Bring an occasion to exactly one remaining seat, submit simultaneous registration attempts
  through two different legitimate entry points, and check the resulting confirmed count.
```

## G11-EVENT-Q062

```yaml
QID: G11-EVENT-Q062
MODULE: event
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Where configuration states that overselling is disallowed, no path exists — including a manual or
  administrative one — that can add a registrant past capacity without at minimum recording that
  the configured rule was overridden.
WHY_IT_MATTERS: >
  A configuration that claims to forbid something, while an unmarked path exists that quietly does
  it anyway, misrepresents to anyone reading that configuration what the system will actually do.
DISCONFIRMING_OBSERVATION: >
  With overselling disallowed in configuration, a registrant is added past capacity through some
  available path with no record indicating that the configured rule was overridden.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Configure an occasion to disallow overselling, fill it to capacity, then attempt every available
  path, including any administrative one, to add one more registrant, and check whether any success
  is recorded as an override.
```
