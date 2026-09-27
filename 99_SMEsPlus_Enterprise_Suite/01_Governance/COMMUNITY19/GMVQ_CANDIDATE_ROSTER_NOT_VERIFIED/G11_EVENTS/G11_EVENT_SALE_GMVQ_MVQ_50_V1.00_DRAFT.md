# SMEsPlus ENTERPRISE SUITE
## GMVQ — G11 EVENTS / event_sale Module Bridge MVQ Bank

**Document ID:** GMVQ-G11-EVENT_SALE-MVQ50-V1.00
**Group:** G11 EVENTS
**Module Metadata:** `event_sale`
**Wave:** W2
**Author Cell:** P-E2 (GMVQ Question Factory — Internal Production Team E2, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Standard bank reference:** 55 (shared, not reproduced here; not yet authored for G11 as of this run)
**Research depth:** 55 + 50 = 105
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `event_sale`, the bridge where a
registration is created by a commercial order rather than by direct sign-up. Per the GMVQ Bridge
Module Rule V1.00, every question here fails only at the seam between the order side and the
registration side: the point at which capacity is actually consumed, whether the two records stay
consistent through confirmation, cancellation and reversal, how a paid order line's identity,
quantity and price map onto one or more attendee registrations, which side's cancellation and
refund policy governs when the two disagree, revenue recognition timing, cross-company and
cross-currency settlement, and the audit trail from a seat back to the sale that paid for it. No
question here concerns pure event mechanics (capacity, dates, waiting lists) considered on their
own, and no question restates a pure order-processing behaviour in isolation; each was tested
against the bridge rule's removal test before being kept. This is the first bank authored for G11
EVENTS, so no sibling `event_crm_sale` HYPOTHESIS lines existed on disk at the time of authoring;
this bank was written first, precisely so that `event_crm_sale` (the bridge-over-a-bridge) could be
checked against it. Coverage spans business capability, business rule, state transition,
configuration dependency, role and permission, exception path, cancellation, reversal, negative
case, cross-module dependency, optional behaviour, auditability, tenant/company boundary,
concurrency and ordering, runtime reachability, configuration reachability, and source/runtime
contradiction potential.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 50 questions exist because they test 50 distinct material seam hypotheses; none was
  trimmed or stretched to hit a target count, and none was cut to land on a round number.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field.
- No question concerns event mechanics in isolation (capacity rules, dates, waiting lists as such);
  every question requires the order side and the registration side both to be present to make sense.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G11-EVENT_SALE-Q001

```yaml
QID: G11-EVENT_SALE-Q001
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A commercial order's confirmation and the corresponding registration's existence are kept as a single consistent fact: an order confirmed as complete never leaves the seat it paid for without a matching registration record, and a registration credited to an order never survives that order's own confirmation being undone.
WHY_IT_MATTERS: >
  If the two facts can drift apart, a paying customer can hold a confirmed seat with no registration a coordinator can see at the door, or a registration can exist and hold capacity for an order that was never actually completed.
DISCONFIRMING_OBSERVATION: >
  An order shows full confirmation while the seat it corresponds to has no registration record at all, or a registration remains in place after the order that was supposed to create it reverts to an unconfirmed state.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm a commercial order for a seat, then separately check for a matching registration; also revert an order's confirmation and check whether an already-created registration survives.
```

## G11-EVENT_SALE-Q002

```yaml
QID: G11-EVENT_SALE-Q002
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an order is cancelled and its own registration is independently cancelled through the event side at close to the same time, the two records converge on the same final cancelled state rather than settling into two different states that disagree about whether the seat is available.
WHY_IT_MATTERS: >
  A registration and its originating order in different states leaves capacity, refund, and attendance decisions built on whichever side happens to be checked, rather than on one governing fact.
DISCONFIRMING_OBSERVATION: >
  After both the order and its registration have been independently cancelled, the seat still counts as held according to one of the two records while the other reports it as released.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel a registration directly and cancel its originating order independently within a short window, then check the availability status each side reports for the same seat.
```

## G11-EVENT_SALE-Q003

```yaml
QID: G11-EVENT_SALE-Q003
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The event's capacity is consumed at one identifiable, consistent point in the order's lifecycle (for example: when the order is placed, when it is confirmed, or when it is paid) rather than shifting between orders for the same event depending on how each one happens to be processed.
WHY_IT_MATTERS: >
  If capacity is consumed inconsistently, two orders processed differently can both believe they hold the same seat, and the event can be oversold without any single step ever being wrong on its own.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical orders for the same event, taken to different lifecycle stages (one merely placed, one fully paid), are found to have consumed the event's capacity at different stages rather than the same one.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place one order and leave it unconfirmed, fully pay a second order for the same event, and compare at which stage each order's seat was actually deducted from remaining capacity.
```

## G11-EVENT_SALE-Q004

```yaml
QID: G11-EVENT_SALE-Q004
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Between an order being placed for a seat and the registration record actually being created, the seat is held against the event's capacity for a bounded, observable period rather than being simultaneously available to a second buyer.
WHY_IT_MATTERS: >
  A gap where the seat is neither reserved nor yet registered is exactly the window in which the same seat can be sold twice with neither sale doing anything wrong individually.
DISCONFIRMING_OBSERVATION: >
  A seat that has already been placed on one order, but for which no registration has yet been created, can still be placed on a second order for the same specific seat or ticket type at the same time.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Place an order for a seat but stop short of whatever step creates its registration, then attempt to place a second order for the same seat or the same limited ticket type before the first order's registration is created.
```

## G11-EVENT_SALE-Q005

```yaml
QID: G11-EVENT_SALE-Q005
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Increasing an order line's quantity after registrations already exist for that line adds the correct number of new registration records rather than creating too many, too few, or none.
WHY_IT_MATTERS: >
  A mismatch here means the number of registrations for an order silently stops corresponding to what the customer actually paid to attend.
DISCONFIRMING_OBSERVATION: >
  Increasing an order line's quantity by a known amount after registrations already exist produces a different number of additional registrations than the increase itself.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an order line with an initial quantity and let its registrations be created, then increase the line's quantity by a known amount and count how many additional registrations appear.
```

## G11-EVENT_SALE-Q006

```yaml
QID: G11-EVENT_SALE-Q006
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Decreasing an order line's quantity after registrations already exist for it results in a deliberate, identifiable choice about which specific registration is removed, rather than an arbitrary or unrecorded one.
WHY_IT_MATTERS: >
  If it is not clear which attendee's seat was actually withdrawn when the line is reduced, an already-confirmed attendee can silently lose their seat with no record of why.
DISCONFIRMING_OBSERVATION: >
  Reducing an order line's quantity when several registrations already exist for it removes a registration without leaving any indication of which one was chosen for removal or on what basis.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create several registrations against one order line, then reduce that line's quantity by one, and check whether the removed registration is identifiable and the basis for the choice is recorded.
```

## G11-EVENT_SALE-Q007

```yaml
QID: G11-EVENT_SALE-Q007
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an order after attendance has already been recorded for the registration it produced does not silently erase or overwrite the fact that the person actually attended.
WHY_IT_MATTERS: >
  Losing the attendance record on cancellation would make it impossible to later show that someone who did attend an event is nonetheless shown never to have been there.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order whose registration already carries a recorded attendance causes that attendance record to be deleted or reset as though the person never attended.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record attendance for a registration produced by an order, then cancel that order, and check whether the attendance fact still exists afterward.
```

## G11-EVENT_SALE-Q008

```yaml
QID: G11-EVENT_SALE-Q008
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a single order line covers several seats, each individual attendee, once named, is tracked as their own distinct registration record rather than several people sharing one combined record that cannot distinguish them.
WHY_IT_MATTERS: >
  Without individual records, attendance, transfers, and cancellations for one person on a shared line cannot be handled without affecting the others on the same line.
DISCONFIRMING_OBSERVATION: >
  Naming two different attendees against one multi-seat order line results in a single combined registration record that cannot show which specific person is which, or one attendee's cancellation also removes the other's seat.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place an order line for more than one seat, name two different attendees against it, and check whether each has an independently addressable registration record.
```

## G11-EVENT_SALE-Q009

```yaml
QID: G11-EVENT_SALE-Q009
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A seat whose attendee is named only after the order is confirmed continues to be held against capacity throughout the period before the name is supplied, rather than lapsing back into available inventory while unnamed.
WHY_IT_MATTERS: >
  If an unnamed paid seat can silently lapse, a customer who paid in full can arrive to find their seat was released to someone else through no fault of their own.
DISCONFIRMING_OBSERVATION: >
  A seat on a confirmed, paid order line whose attendee has not yet been named is found to have been released back into available capacity and sold to someone else before the name was supplied.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Confirm and pay an order line for a seat without naming the attendee, wait, and then check whether that seat can still be taken by a different, unrelated order.
```

## G11-EVENT_SALE-Q010

```yaml
QID: G11-EVENT_SALE-Q010
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A registration whose attendee is never named settles into one clearly identifiable, permanent state (for example, remaining a named-pending placeholder indefinitely) rather than drifting into an ambiguous state that reporting treats inconsistently as either a real attendee or a phantom one.
WHY_IT_MATTERS: >
  An indefinitely unnamed registration that is sometimes counted as an attendee and sometimes not corrupts headcounts, capacity reporting, and check-in expectations.
DISCONFIRMING_OBSERVATION: >
  A registration whose attendee was never named is counted as an actual attendee in one report or view and excluded as though it does not exist in another, with no single governing state to explain the difference.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Leave a paid registration's attendee unnamed indefinitely, and compare how it is represented across the event's headcount, check-in list, and capacity views.
```

## G11-EVENT_SALE-Q011

```yaml
QID: G11-EVENT_SALE-Q011
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an order is cancelled and refunded, the refund actually applied follows one governing policy consistently, either the order's own standard return terms or the event's own stated cancellation and refund policy, rather than whichever one happens to be checked first producing a different outcome than the other.
WHY_IT_MATTERS: >
  Two different, unreconciled refund rules operating on the same cancellation can produce two different correct-looking refund amounts for the same event, with no way to tell a customer which one is authoritative.
DISCONFIRMING_OBSERVATION: >
  Cancelling the same kind of paid registration produces a refund amount consistent with the order's general return terms in one case and a different amount consistent with the event's own stated policy in another, with no recorded reason for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set an event's own cancellation and refund terms to differ from the order side's general return terms, cancel a paid registration, and check which figure the actual refund follows.
```

## G11-EVENT_SALE-Q012

```yaml
QID: G11-EVENT_SALE-Q012
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Revenue from an order-derived registration is recognised at one defined, consistent point in time, either when the sale happens or when the event itself takes place, and that point does not silently vary between two otherwise identical registrations for the same event.
WHY_IT_MATTERS: >
  Recognising the same kind of revenue at different times for different registrations of the same event would misstate financial results for whichever period is being reported.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical paid registrations for the same event have their revenue recognised in different accounting periods relative to the sale and the event date, with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create two comparable paid registrations for one event whose sale date and event date fall in different accounting periods, and compare when each one's revenue is actually recognised.
```

## G11-EVENT_SALE-Q013

```yaml
QID: G11-EVENT_SALE-Q013
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the order's paying customer is a different party from the individually named attendee, it is the attendee's own identity, not the paying customer's, that determines who is treated as the registered person for check-in, attendance, and event-day permission purposes.
WHY_IT_MATTERS: >
  If the payer's identity leaks into decisions that should belong to the attendee, someone who never paid could be denied entry, or a payer who never intends to attend could inherit attendance-related standing.
DISCONFIRMING_OBSERVATION: >
  Check-in, attendance recording, or event-day access for a registration is found to be governed by the paying customer's identity rather than the separately named attendee's, when the two are different people.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Place an order where the paying customer and the named attendee are two different people, and check whose identity governs check-in and event-day permissions.
```

## G11-EVENT_SALE-Q014

```yaml
QID: G11-EVENT_SALE-Q014
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The same specific seat cannot end up sold on two separate, independent orders at the same time; a second order attempting to take an already-committed seat is blocked or flagged rather than silently succeeding alongside the first.
WHY_IT_MATTERS: >
  Two independently successful sales of the same seat is a direct overselling failure that surfaces only when both customers arrive expecting the same place.
DISCONFIRMING_OBSERVATION: >
  Two separate orders, placed independently, both succeed in registering the same specific seat or last remaining capacity unit for the same event, with neither one being blocked or flagged.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reduce an event or ticket type to its last available seat, then place two separate orders for that same seat at close to the same time, and check whether both are allowed to succeed.
```

## G11-EVENT_SALE-Q015

```yaml
QID: G11-EVENT_SALE-Q015
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the event behind an order is cancelled entirely after the order was placed, the order's own state moves to reflect that in a defined, consistent way (cancellation, credit, or an equivalent outcome) rather than the order continuing to sit as though the event it references still exists.
WHY_IT_MATTERS: >
  An order left pointing at an event that no longer exists can keep charging or keep showing a valid seat for something that will never happen.
DISCONFIRMING_OBSERVATION: >
  An event is cancelled entirely, and an order placed against it beforehand is still shown as a normal, unaffected active order with no indication that its event no longer exists.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Place an order for an event, cancel the event entirely afterward, and check what state the order and its registration move to.
```

## G11-EVENT_SALE-Q016

```yaml
QID: G11-EVENT_SALE-Q016
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A refund issued on an order after the event's own date has already passed is either specifically permitted under a defined late-refund rule or is blocked, but it is not processed as an ordinary, unremarked refund with no distinction from a pre-event one.
WHY_IT_MATTERS: >
  Treating a post-event refund identically to a pre-event one hides the fact that the obligation the payment was for has, in the ordinary case, already been delivered.
DISCONFIRMING_OBSERVATION: >
  A refund requested and processed after the event's date has passed goes through with no distinction, flag, or different handling from a refund requested before the event took place.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Let an event's date pass with a paid registration still on record, then request a refund on the underlying order and check whether it is handled any differently from a pre-event refund.
```

## G11-EVENT_SALE-Q017

```yaml
QID: G11-EVENT_SALE-Q017
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an order covering several seats receives only a partial payment, the number of registrations actually confirmed reflects that partial payment in a defined way (for example, proportionally, or none until full payment) rather than all seats being fully confirmed on a partial payment with no accounting for the shortfall.
WHY_IT_MATTERS: >
  Fully confirming every seat on a partial payment would let a customer hold a full block of seats while having paid for only part of them, without that gap being tracked anywhere.
DISCONFIRMING_OBSERVATION: >
  An order for several seats that has received a clearly partial payment shows every one of its seats as fully confirmed, with no record distinguishing the paid portion from the unpaid one.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place a multi-seat order, pay less than the full amount due, and check how many of the order's seats are shown as confirmed relative to what was actually paid.
```

## G11-EVENT_SALE-Q018

```yaml
QID: G11-EVENT_SALE-Q018
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When one order is split across more than one invoice, whether a registration is treated as confirmed follows a defined rule about the order as a whole, rather than each invoice independently confirming its own share of registrations with no coordination between them.
WHY_IT_MATTERS: >
  Independent per-invoice confirmation can let some seats be confirmed while sibling seats on the same original order remain in limbo with no clear owner for reconciling the difference.
DISCONFIRMING_OBSERVATION: >
  Splitting one order into two invoices results in each invoice confirming its own registrations independently with no visible link back to the fact that both came from a single original order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place a multi-seat order, split it into two separate invoices, settle one and not the other, and check how registration confirmation is decided across the two.
```

## G11-EVENT_SALE-Q019

```yaml
QID: G11-EVENT_SALE-Q019
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling a registration directly, without going through the order it came from, produces a consistent, traceable effect on that order (for example, a documented credit or an explicit record of the mismatch) rather than leaving the order looking fully intact as though nothing changed.
WHY_IT_MATTERS: >
  An order that still looks entirely normal after one of its seats was cancelled elsewhere hides a real change in what the customer is owed or entitled to.
DISCONFIRMING_OBSERVATION: >
  Cancelling a registration directly on the event side leaves its originating order showing full, unchanged value and quantity with no trace of the cancellation anywhere on the order.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel a registration directly through the event side rather than through its order, then check whether the order reflects that cancellation in its own value or record.
```

## G11-EVENT_SALE-Q020

```yaml
QID: G11-EVENT_SALE-Q020
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing an order line's ticket type after a registration already exists for it produces one defined outcome, either the registration updates to match, a new registration replaces it, or the change is blocked, rather than leaving the original registration in place still pointing at the ticket type that no longer matches the line.
WHY_IT_MATTERS: >
  An orphaned registration that no longer matches its own order line's ticket type creates a silent mismatch between what was billed and what will actually be granted at the event.
DISCONFIRMING_OBSERVATION: >
  Changing an order line's ticket type after its registration was created leaves that registration referencing the original, now-superseded ticket type with no update, replacement, or block.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a registration from an order line, then change that line's ticket type, and check what happens to the existing registration.
```

## G11-EVENT_SALE-Q021

```yaml
QID: G11-EVENT_SALE-Q021
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  For an event that recurs across several dates, a single order line maps to one specific date's own capacity rather than drawing indistinguishably against a shared pool that spans every date of the recurring event.
WHY_IT_MATTERS: >
  If capacity for a recurring event is not tracked per actual date, one heavily booked date can silently borrow room from another date's separate capacity, or appear full when it is not.
DISCONFIRMING_OBSERVATION: >
  An order line for one specific date of a recurring event is found to reduce the remaining capacity of a different date of the same recurring series.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set up a recurring event with more than one date and a limited per-date capacity, place an order for a specific date, and check which date's capacity is actually reduced.
```

## G11-EVENT_SALE-Q022

```yaml
QID: G11-EVENT_SALE-Q022
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A waiting-list position, once an event is full, is assigned by a consistent rule (for example, purely by the time the interest was recorded) regardless of whether that interest arrived through an order or through direct sign-up, rather than one path being systematically favoured over the other.
WHY_IT_MATTERS: >
  If one entry path is quietly favoured for waiting-list position, people are not actually served in the order they asked to be, without anyone being told that a preference exists.
DISCONFIRMING_OBSERVATION: >
  An order-derived and a directly signed-up waiting-list entry, recorded at effectively the same time for a full event, are placed in a waiting-list order that does not correspond to when each interest was actually recorded.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Fill an event to capacity, then record one waiting-list interest through an order and another through direct sign-up at close to the same time, and check whether their relative waiting-list position matches the order in which interest was recorded.
```

## G11-EVENT_SALE-Q023

```yaml
QID: G11-EVENT_SALE-Q023
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Re-addressing an order to a different paying customer does not, on its own, silently reassign the named attendee on an already-created registration to that new customer.
WHY_IT_MATTERS: >
  Changing who is being billed for an order should not be able to quietly hand someone else's seat, and the personal standing that goes with it, to the new billing party without a deliberate act.
DISCONFIRMING_OBSERVATION: >
  Changing the billing customer on an order automatically changes the named attendee on its existing registration to the new billing customer, with no separate action to transfer the seat.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create an order with a named attendee, then re-address the order's billing customer to someone else, and check whether the attendee on the existing registration changes as a result.
```

## G11-EVENT_SALE-Q024

```yaml
QID: G11-EVENT_SALE-Q024
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the order's own operating company differs from the company that owns the event being registered for, the registration is still created correctly and attributed to the event's own company, rather than being silently attributed to the order's company or blocked without explanation.
WHY_IT_MATTERS: >
  Misattributing a cross-company registration would move a transaction's ownership to an entity that does not actually run the event, breaking that company's own reporting boundary.
DISCONFIRMING_OBSERVATION: >
  An order placed under one company for an event that belongs to a different company results in a registration attributed to the order's company rather than the company that actually owns the event.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set up an order under one company for an event owned by a different company in the same multi-company setup, and check which company the resulting registration is attributed to.
```

## G11-EVENT_SALE-Q025

```yaml
QID: G11-EVENT_SALE-Q025
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When an order's currency differs from the currency the event's price is normally listed in, the amount actually recorded against the registration reflects a defined, consistent conversion rather than an arbitrary or unrecorded figure.
WHY_IT_MATTERS: >
  An unrecorded or inconsistent currency conversion between the order and the event's own listed price makes it impossible to verify that a registration was actually paid for at the correct rate.
DISCONFIRMING_OBSERVATION: >
  An order placed in a currency different from the event's normal listing currency produces a recorded registration amount that does not correspond to any documented conversion rate.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place an order in a currency different from the event's usual listing currency, and check whether the resulting registration amount reflects a documented, consistent conversion.
```

## G11-EVENT_SALE-Q026

```yaml
QID: G11-EVENT_SALE-Q026
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A seat held by an unconfirmed order (a quotation that has not been followed through) is released back to available capacity after a defined period, rather than being held indefinitely against an order that may never be completed.
WHY_IT_MATTERS: >
  An indefinitely held seat behind an order nobody ever finishes silently locks capacity away from people who would actually complete a purchase.
DISCONFIRMING_OBSERVATION: >
  A seat held by an unconfirmed order remains unavailable to other buyers indefinitely, with no defined point at which it is released back into available capacity.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Place an order for a seat and leave it unconfirmed for an extended period, then check whether and when that seat becomes available to other orders again.
```

## G11-EVENT_SALE-Q027

```yaml
QID: G11-EVENT_SALE-Q027
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two separate unconfirmed orders both include what is, at the moment of confirmation, the same single last available seat, only one of them is allowed to actually confirm that seat; the second is blocked or redirected rather than both succeeding.
WHY_IT_MATTERS: >
  Two quotations both quietly holding the same last seat is only a problem the moment both try to close, and if both are allowed through, the event is oversold by exactly the amount nobody caught.
DISCONFIRMING_OBSERVATION: >
  Two separate orders, each referencing the same last remaining seat, are both successfully confirmed for that same seat at close to the same time.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reduce a ticket type to exactly one remaining seat, place two separate unconfirmed orders each referencing it, and attempt to confirm both at close to the same time.
```

## G11-EVENT_SALE-Q028

```yaml
QID: G11-EVENT_SALE-Q028
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A deposit or down payment on an order that is less than the full price has a defined, consistent effect on the registration (for example: it creates the registration but leaves it unconfirmed, or it does not create one at all), rather than a deposit sometimes producing a fully confirmed registration and sometimes not for otherwise identical orders.
WHY_IT_MATTERS: >
  If a partial deposit sometimes fully confirms a seat and sometimes does not, two customers who paid the identical deposit amount can end up with different standing for reasons nobody can explain.
DISCONFIRMING_OBSERVATION: >
  Two orders that received an identical deposit amount, with the remaining balance still outstanding on both, end up with different registration confirmation states.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place two comparable orders, pay the same partial deposit amount on each, and compare the resulting registration state on both.
```

## G11-EVENT_SALE-Q029

```yaml
QID: G11-EVENT_SALE-Q029
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A registration created from an order can be traced back to the specific order and order line that produced it, so that a reviewer can identify which commercial transaction is responsible for a given seat.
WHY_IT_MATTERS: >
  Without that traceability, a coordinator or auditor cannot connect a seat at the event back to the sale that paid for it, undermining any check on revenue against actual attendance.
DISCONFIRMING_OBSERVATION: >
  A registration known to have come from an order cannot be traced back to which specific order, or which specific line on that order, actually produced it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a registration from a specific order line, and check whether that origin can be reconstructed by looking at the registration alone.
```

## G11-EVENT_SALE-Q030

```yaml
QID: G11-EVENT_SALE-Q030
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an event's date or location changes after an order for it has already been confirmed and paid, the change is surfaced to that existing order or registration in some defined way, rather than the paid registration continuing to reference the original date or location with no indication that anything changed.
WHY_IT_MATTERS: >
  A paying customer who is never told their event's date or place moved has effectively been sold a seat to something that no longer matches what they agreed to.
DISCONFIRMING_OBSERVATION: >
  An event's date or location is changed after a paid order exists for it, and the existing registration continues to display the original, now-incorrect date or location with no update or notice.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm and pay an order for an event, then change that event's date or location, and check what the existing registration shows afterward.
```

## G11-EVENT_SALE-Q031

```yaml
QID: G11-EVENT_SALE-Q031
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An order placed by a group or company account before individual attendees are named creates registration records in a defined, consistent way (for example, one placeholder per paid seat) rather than either creating no trace of the seats at all or creating a number of registration records that does not match what was actually paid for.
WHY_IT_MATTERS: >
  If the number of registration records does not match the number of seats paid for before names are known, there is no reliable way to know how many actual seats still need names, or whether the count is even right.
DISCONFIRMING_OBSERVATION: >
  A group order paying for a specific number of seats, placed before any individual attendees are named, results in a number of registration records that does not match the number of seats paid for.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place a group order for a specific number of seats without naming any attendees, and count the resulting registration records against the number actually paid for.
```

## G11-EVENT_SALE-Q032

```yaml
QID: G11-EVENT_SALE-Q032
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the order side's own general cancellation and return process would produce a different outcome than the event's own stated cancellation policy for the same cancellation, one of the two is the one that actually governs, consistently, rather than whichever process happens to be invoked first deciding the outcome by accident.
WHY_IT_MATTERS: >
  A cancellation whose outcome depends on which of two systems happened to process it first is not a governed outcome at all; it is a coin flip dressed up as policy.
DISCONFIRMING_OBSERVATION: >
  Cancelling the same kind of registration through the order side's general process and through the event's own stated cancellation policy produces two different outcomes, with no rule establishing which one prevails.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set the order side's general return terms to differ from the event's own stated cancellation policy, cancel a registration through each path separately for comparable cases, and check which outcome actually governs.
```

## G11-EVENT_SALE-Q033

```yaml
QID: G11-EVENT_SALE-Q033
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When both a specific ticket type and the overall event carry their own separate capacity limits, an order-derived registration is checked against both limits, so that filling one does not silently allow the other to be exceeded.
WHY_IT_MATTERS: >
  Checking only one of the two limits would let a popular ticket type oversell its own allotment while the event as a whole still looks like it has room, or vice versa.
DISCONFIRMING_OBSERVATION: >
  An order succeeds in registering a seat under a ticket type that has already reached its own separate capacity limit, solely because the overall event still has room.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a ticket type's own capacity lower than the overall event's capacity, fill the ticket type's limit, and attempt to place another order for that same ticket type while the event overall still has room.
```

## G11-EVENT_SALE-Q034

```yaml
QID: G11-EVENT_SALE-Q034
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A registration created through an order and a separate direct sign-up using the same person's identifying details for the same event are detected as potentially the same attendee, rather than being silently accepted as two entirely unrelated registrations with no cross-check between the two entry paths.
WHY_IT_MATTERS: >
  An undetected duplicate person registered twice through two different paths overstates the real headcount and can create two conflicting entitlements to the same seat.
DISCONFIRMING_OBSERVATION: >
  The same person's identifying details are used to register for the same event once through an order and once through direct sign-up, and both registrations are accepted with no flag or cross-check linking them as potentially duplicate.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Register the same person's details for the same event once via an order and once via direct sign-up, and check whether anything flags the two as potentially the same attendee.
```

## G11-EVENT_SALE-Q035

```yaml
QID: G11-EVENT_SALE-Q035
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order is voided or deleted outright, rather than formally cancelled, after registrations already exist for it, those registrations move to a defined state (for example, automatically cancelled) rather than remaining as active, seemingly valid registrations with no order behind them at all.
WHY_IT_MATTERS: >
  An active-looking registration left behind after its own order was deleted is a seat nobody can account for, held by nothing, that can still be treated as confirmed by anyone who does not check further.
DISCONFIRMING_OBSERVATION: >
  An order is voided or deleted outright after producing registrations, and those registrations remain fully active and confirmed with no order record behind them at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create registrations from an order, then void or delete that order outright rather than cancelling it normally, and check what state the orphaned registrations end up in.
```

## G11-EVENT_SALE-Q036

```yaml
QID: G11-EVENT_SALE-Q036
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A discount or sales commission applied at the order level is reflected consistently in whatever amount is later recognised as revenue for the registration it produced, rather than the recognised revenue figure ignoring a discount that was actually granted, or ignoring a commission's effect on the net amount.
WHY_IT_MATTERS: >
  Recognising revenue that does not reflect an actual discount misstates what the event genuinely earned from that seat.
DISCONFIRMING_OBSERVATION: >
  A registration produced by an order that carried a specific discount has its recognised revenue calculated as though the full, undiscounted price had been paid.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a known discount to an order line for a seat, complete the order, and check whether the recognised revenue for the resulting registration reflects the discounted amount.
```

## G11-EVENT_SALE-Q037

```yaml
QID: G11-EVENT_SALE-Q037
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  For an event whose price changes depending on how close to the event date the order is placed, the price actually locked in for a registration is the one in effect when the order was placed, and does not silently shift to a different price in effect later if payment happens afterward.
WHY_IT_MATTERS: >
  A price that moves between order placement and eventual payment, without a defined rule for which one counts, means the amount owed for the same seat is not actually fixed at the moment the customer committed to it.
DISCONFIRMING_OBSERVATION: >
  An order placed while one price tier is active ends up billed at a different, later price tier that only came into effect after the order was placed but before it was paid.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Place an order for a seat while one time-based price tier is active, allow the price to move to a later tier before payment is completed, and check which price the order is actually billed at.
```

## G11-EVENT_SALE-Q038

```yaml
QID: G11-EVENT_SALE-Q038
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the entity that issues the order's invoice is different from the entity that operates the event itself, the settlement of funds between the two is handled through a defined path, rather than the registration or the revenue simply being attributed with no record of which entity actually received the money.
WHY_IT_MATTERS: >
  Without a defined settlement path, money collected by one entity for an event run by another can go unreconciled, leaving one side effectively unpaid for an obligation it delivered.
DISCONFIRMING_OBSERVATION: >
  An order invoiced by one legal entity for an event operated by a different one produces a registration with no recorded path showing how, or whether, funds move between the two entities.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Set up an order invoiced under one company entity for an event operated by a different entity, complete the order, and check whether any settlement path between the two entities is recorded.
```

## G11-EVENT_SALE-Q039

```yaml
QID: G11-EVENT_SALE-Q039
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a paid seat's attendee is substituted for a different named person, the original attendee's own record and history are preserved alongside the new attendee's registration, rather than the substitution overwriting the original person's data as though they had never been named.
WHY_IT_MATTERS: >
  Erasing the original attendee's record on substitution destroys the ability to later show who was originally meant to attend, which matters for refund disputes, no-show tracking, and personal data requests alike.
DISCONFIRMING_OBSERVATION: >
  Substituting a new named attendee onto a paid seat overwrites the original attendee's own record entirely, leaving no trace that a different person was originally named.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Name an attendee on a paid registration, substitute a different named person onto the same seat, and check whether the original attendee's record still exists anywhere afterward.
```

## G11-EVENT_SALE-Q040

```yaml
QID: G11-EVENT_SALE-Q040
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a payment is declined or reversed shortly after it provisionally created a registration, that registration is rolled back or clearly flagged as unconfirmed, rather than remaining as an apparently valid, confirmed registration with no payment actually behind it.
WHY_IT_MATTERS: >
  A confirmed-looking registration left in place after its payment failed lets someone hold a seat, and possibly attend, without the event ever actually being paid for it.
DISCONFIRMING_OBSERVATION: >
  A payment that provisionally created a registration is then declined or reversed, and the registration remains shown as fully confirmed with no flag indicating the payment behind it failed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Trigger a payment that provisionally creates a registration, then have that payment decline or reverse, and check the registration's resulting confirmation state.
```

## G11-EVENT_SALE-Q041

```yaml
QID: G11-EVENT_SALE-Q041
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An unconfirmed order left abandoned before completion (a quotation nobody ever finished) does not hold the event's capacity against it for longer than a defined period, and that period is applied consistently rather than varying unpredictably between similar abandoned orders.
WHY_IT_MATTERS: >
  An abandoned quotation with no defined release point behaves exactly like a genuinely sold seat for as long as anyone leaves it sitting there, indefinitely narrowing real availability.
DISCONFIRMING_OBSERVATION: >
  Two comparably abandoned, unconfirmed orders for the same event end up holding their referenced seats against capacity for two different lengths of time, with no configuration difference to explain it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create two similar unconfirmed orders for the same event and leave both abandoned, then compare how long each one continues to hold its seat against capacity before release.
```

## G11-EVENT_SALE-Q042

```yaml
QID: G11-EVENT_SALE-Q042
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An order that combines an event ticket line together with unrelated, non-event product lines can have its event-related line cancelled or refunded on its own, without that action also cancelling or refunding the unrelated lines, and without cancelling the unrelated lines also silently affecting the registration.
WHY_IT_MATTERS: >
  Treating a mixed order as one indivisible unit for cancellation purposes forces an all-or-nothing outcome onto a customer who only wanted to change one part of what they bought.
DISCONFIRMING_OBSERVATION: >
  Cancelling or refunding only the event-related line on a mixed order also cancels or refunds the unrelated, non-event lines on the same order, or the reverse, with no way to act on one without the other.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place one order containing both an event ticket line and an unrelated product line, cancel or refund only the event line, and check whether the unrelated line is affected.
```

## G11-EVENT_SALE-Q043

```yaml
QID: G11-EVENT_SALE-Q043
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Duplicating an order to plan a similar future purchase does not cause the copy to inherit a live reference to the registrations that were actually created under the original order.
WHY_IT_MATTERS: >
  A duplicated order that appears to already have real registrations attached would misrepresent a brand-new, unpaid transaction as one that already has confirmed attendees.
DISCONFIRMING_OBSERVATION: >
  An order duplicated from one that already produced registrations shows those original registrations as though they belong to the new copy as well.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an order that produces registrations, duplicate that order, and check whether the duplicate shows any of the original's registrations as its own.
```

## G11-EVENT_SALE-Q044

```yaml
QID: G11-EVENT_SALE-Q044
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When registrations are added manually beyond the quantity an order line originally specified, the order line's own recorded quantity is reconciled to reflect the actual number of registrations, rather than a silent, permanent mismatch persisting between what the order says and what actually exists.
WHY_IT_MATTERS: >
  A persistent mismatch between an order line's stated quantity and its real registration count means the order can never again be trusted at face value for how many seats it actually represents.
DISCONFIRMING_OBSERVATION: >
  Adding a registration manually beyond an order line's original quantity leaves that line's recorded quantity unchanged and permanently out of step with the number of registrations that actually exist under it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an order line with a set quantity, manually add one more registration beyond that quantity, and check whether the order line's own recorded quantity is reconciled afterward.
```

## G11-EVENT_SALE-Q045

```yaml
QID: G11-EVENT_SALE-Q045
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  For an event that requires a minimum number of attendees to actually run, an order placed before that minimum is reached, in the event the event is later called off for that reason, is handled by a defined refund and record outcome, rather than being treated identically to a customer-initiated cancellation with no distinction for whose decision it actually was.
WHY_IT_MATTERS: >
  Treating an organiser-driven cancellation for insufficient attendance the same as an ordinary customer cancellation can shift the consequence of the organiser's own decision onto the customer's own cancellation terms.
DISCONFIRMING_OBSERVATION: >
  An event called off because it never reached its minimum attendance threshold processes existing orders' refunds and records identically to an ordinary customer-requested cancellation, with nothing distinguishing who or what caused it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Set an event's required minimum attendance, leave it unmet by the cutoff, call the event off for that reason, and check how existing orders' refunds and records are handled compared with an ordinary customer cancellation.
```

## G11-EVENT_SALE-Q046

```yaml
QID: G11-EVENT_SALE-Q046
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the salesperson credited on the order differs from the person designated as the event's own coordinator or owner, the rights each of them has to edit the combined order-and-registration record are defined and distinct, rather than either one having unrestricted edit rights over the other's side by default.
WHY_IT_MATTERS: >
  Without distinct edit rights, a salesperson could alter event-side details they have no standing over, or an event coordinator could alter commercial terms on an order they do not own.
DISCONFIRMING_OBSERVATION: >
  A salesperson credited on an order is able to freely edit event-side details of the registration, or an event coordinator is able to freely edit the order's own commercial terms, with no boundary between the two roles.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Set up an order with a credited salesperson different from the event's designated coordinator, and check what each of them is able to edit on the combined record.
```

## G11-EVENT_SALE-Q047

```yaml
QID: G11-EVENT_SALE-Q047
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the order was placed or confirmed in a different time zone from the event's own local time, whatever cutoff determines before or after the event (for cancellation terms, refund eligibility, or similar) is evaluated consistently in one defined time zone, rather than shifting depending on which side's clock happens to be used.
WHY_IT_MATTERS: >
  A cutoff that can fall on either side of midnight depending on whose time zone is used can make the same real request valid under one clock and too late under the other.
DISCONFIRMING_OBSERVATION: >
  A cancellation or refund request that falls within the allowed window under the event's own local time zone is rejected as late when evaluated under the order's own different time zone, or the reverse.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place an order from a time zone different from the event's own, submit a cancellation request timed to fall on different sides of the cutoff depending on which time zone is used, and check which one actually governs.
```

## G11-EVENT_SALE-Q048

```yaml
QID: G11-EVENT_SALE-Q048
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Locking an accounting period that contains the order's own transaction date does not prevent an active registration for an event still in the future from being updated, transferred, or cancelled on the event side.
WHY_IT_MATTERS: >
  If closing an accounting period accidentally freezes the operational registration as well as the financial transaction, ordinary event-day changes for something that has not happened yet become impossible for purely financial reasons.
DISCONFIRMING_OBSERVATION: >
  Locking the accounting period containing an order's transaction date also prevents its still-upcoming, unrelated registration from being updated, transferred, or cancelled on the event side.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Lock the accounting period containing an order's transaction date while its event is still in the future, and check whether the registration can still be updated, transferred, or cancelled.
```

## G11-EVENT_SALE-Q049

```yaml
QID: G11-EVENT_SALE-Q049
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two separate orders each reference the same specific, individually assigned resource (such as an assigned seat or table) for the same event, only one of them is allowed to actually hold that specific assignment; the second is blocked, redirected to a different assignment, or flagged, rather than both quietly resolving to the same specific assignment.
WHY_IT_MATTERS: >
  Two customers both holding a confirmed claim to the identical assigned resource is a conflict that surfaces only at the event itself, when it is far too late to resolve cleanly.
DISCONFIRMING_OBSERVATION: >
  Two separate orders both succeed in being confirmed against the identical, individually assigned resource for the same event, with neither being blocked, redirected, or flagged.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Set up an event with individually assigned resources, place two separate orders each requesting the same specific assignment, and check whether both are allowed to hold it.
```

## G11-EVENT_SALE-Q050

```yaml
QID: G11-EVENT_SALE-Q050
MODULE: event_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an order line for a base seat also carries a separately priced add-on (such as optional merchandise or a workshop slot), cancelling only the add-on portion does not disturb the base seat's own registration, and cancelling the base seat is handled with a defined outcome for the add-on rather than leaving it as an orphaned charge for something that no longer has a seat behind it.
WHY_IT_MATTERS: >
  An add-on left billed and unresolved after its underlying seat is cancelled, or a base seat wrongly disturbed by cancelling only an add-on, both misrepresent what the customer actually still holds.
DISCONFIRMING_OBSERVATION: >
  Cancelling only the separately priced add-on portion of an order line also invalidates or alters the base seat's own registration, or cancelling the base seat leaves the add-on charge standing with no defined resolution.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place an order line combining a base seat with a separately priced add-on, cancel only the add-on, then separately test cancelling only the base seat, and check how each affects the other.
```
