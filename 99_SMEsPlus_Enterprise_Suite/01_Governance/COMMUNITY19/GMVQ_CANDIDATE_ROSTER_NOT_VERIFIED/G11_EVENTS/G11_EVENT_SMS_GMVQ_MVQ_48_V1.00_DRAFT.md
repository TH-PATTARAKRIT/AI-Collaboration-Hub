# SMEsPlus ENTERPRISE SUITE
## GMVQ — G11 EVENTS / event_sms Module MVQ Bank

**Document ID:** GMVQ-G11-EVENT_SMS-MVQ48-V1.00
**Group:** G11 EVENTS
**Module Metadata:** `event_sms`
**Wave:** W2
**Author Cell:** P-E4 (GMVQ Question Factory — Bridge Module Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose
This bank supplies the module-specific research questions for `event_sms` — the seam between
outbound messaging and an event's registration or event-level state. The module name carries an
outbound-channel abbreviation that is never used in question text; question text refers throughout
to "the outbound messaging channel" or "a message". It is written for a blind two-lane study: Lane A
reads reference source, Lane B observes a running system, and neither sees the other's answers.
Question text is source-neutral throughout and never names the module.

## Control
- `event_sms` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Every question below passes the
  seam test: if outbound messaging were removed and event registration ran without it, the question
  would no longer make sense.
- A sibling bank for a generic outbound-messaging seam already exists in G05 INVENTORY (the
  `stock_sms` bank) and is not repeated here. That bank is anchored to a reversible document-state
  transition: reversal and re-triggering of a movement's own state, per-transition idempotency
  across more than one triggering path, and content resolved at trigger time versus send time. This
  bank is anchored instead to the one property a document transition does not have: a fixed,
  external, real-world moment. Every cluster below turns on the event's own date — a reminder
  outliving a date change or a cancellation, timing computed against a real clock and a real time
  zone, a registration transfer changing who the fixed moment's message is actually for, and a rate
  limit racing a deadline that, unlike a document state, cannot be moved to accommodate it. No
  hypothesis or disconfirming observation below duplicates one in the sibling bank.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` distinct from every other
  question's; no two questions share a disconfirming event.
- No padding: 48 questions test 48 distinct hypotheses spread across a message outliving a moved or
  cancelled event date, a message sent to a since-cancelled registration, timing computed in whose
  time zone, duplicate firing for one transition, a recipient who transferred their registration
  away, content disclosing other attendees or their pricing, delivery failure and whether
  registration waits on it, an irreversible send against a reversible registration, per-company
  sender identity and cost attribution, a rate limit racing an immovable deadline, and the audit
  record of what was actually sent versus what the current content would produce.
- This bank is DRAFT authoring output only. Not approved, not frozen, not verified.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived here.

---

## G11-EVENT_SMS-Q001

```yaml
QID: G11-EVENT_SMS-Q001
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A message already scheduled relative to an event's date is recalculated, or withheld, when that
  date changes before the message is actually sent, rather than going out carrying the original
  date.
WHY_IT_MATTERS: >
  A message describing the wrong date for a fixed, real-world event can cause a recipient to miss
  it, or to show up for a date that no longer applies.
DISCONFIRMING_OBSERVATION: >
  A scheduled message still goes out referencing the event's original date after that date has
  already been changed and before the message was sent.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Schedule a message relative to an event's date, change that date before the message's send time,
  and observe what date the message actually carries when it goes out.
```

## G11-EVENT_SMS-Q002

```yaml
QID: G11-EVENT_SMS-Q002
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message already sent before the event's date changed is followed, in some form, by an
  indication to its recipient that the date it referred to has since moved.
WHY_IT_MATTERS: >
  Without any follow-up, the recipient's only information remains the now-incorrect date, with
  nothing correcting it.
DISCONFIRMING_OBSERVATION: >
  An event's date changes after a message referencing the original date was already sent, and no
  further communication of any kind reaches that recipient about the change.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Send a message referencing an event's date, change the event's date afterward, and check whether
  the recipient receives any further communication about the change.
```

## G11-EVENT_SMS-Q003

```yaml
QID: G11-EVENT_SMS-Q003
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message already queued but not yet sent is updated to reflect a changed event date, or held
  back, rather than being dispatched carrying stale date content.
WHY_IT_MATTERS: >
  A queued message is still interceptable in principle, so sending it unchanged after the date it
  depends on has already moved is an avoidable error.
DISCONFIRMING_OBSERVATION: >
  A message queued before a date change is sent out afterward with the stale date, when it could
  still have been updated or held.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Queue a message referencing an event's date, change the date before the queued send time, and
  observe whether the message is updated, held, or sent unchanged.
```

## G11-EVENT_SMS-Q004

```yaml
QID: G11-EVENT_SMS-Q004
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An event cancelled before a scheduled message's send time results in that message not going out
  for a date that will no longer occur.
WHY_IT_MATTERS: >
  A message about an event that has already been called off wastes the recipient's attention and
  can create confusion about whether the event is actually still happening.
DISCONFIRMING_OBSERVATION: >
  A message scheduled for an event still goes out after that event has already been cancelled and
  before the message's send time.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Schedule a message for an event, cancel the event before the message's send time, and check
  whether the message is still sent.
```

## G11-EVENT_SMS-Q005

```yaml
QID: G11-EVENT_SMS-Q005
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message already sent before an event was cancelled is followed, in some form, by notice to its
  recipient that the event no longer takes place.
WHY_IT_MATTERS: >
  A recipient holding only the original message has no way to know the event they were reminded
  about has since been called off.
DISCONFIRMING_OBSERVATION: >
  An event is cancelled after a message about it was already sent, and no further communication of
  any kind reaches that recipient about the cancellation.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Send a message for an event, cancel the event afterward, and check whether the recipient receives
  any further communication about the cancellation.
```

## G11-EVENT_SMS-Q006

```yaml
QID: G11-EVENT_SMS-Q006
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When several messages are scheduled at different fixed offsets before one event's date, a change
  to that date recalculates all of them consistently, not only the offset nearest to the change.
WHY_IT_MATTERS: >
  Recalculating only the nearest offset leaves the others silently pointing at the wrong moment
  relative to the real, moved date.
DISCONFIRMING_OBSERVATION: >
  After an event's date changes, one scheduled offset is recalculated correctly while another,
  still pending, offset for the same event is not.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Schedule messages at more than one fixed offset before an event's date, change the date, and
  check whether every still-pending offset is recalculated consistently.
```

## G11-EVENT_SMS-Q007

```yaml
QID: G11-EVENT_SMS-Q007
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a registration after a message addressed to it was already dispatched does not
  retroactively alter the retained record of what was actually sent.
WHY_IT_MATTERS: >
  A retroactively altered record of a past send makes it impossible to later confirm what a
  recipient genuinely received before they cancelled.
DISCONFIRMING_OBSERVATION: >
  Cancelling a registration changes the retained record of a message already sent to it before the
  cancellation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message to a registration, cancel that registration afterward, and check whether the
  retained record of the earlier send changed.
```

## G11-EVENT_SMS-Q008

```yaml
QID: G11-EVENT_SMS-Q008
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A message still queued for a registration that is cancelled before its send time is withheld,
  rather than sent to someone who is no longer registered.
WHY_IT_MATTERS: >
  Sending a message about an event to someone who has already cancelled wastes their attention and
  can cause confusion about whether they are still expected.
DISCONFIRMING_OBSERVATION: >
  A message queued for a registration still goes out after that registration was cancelled before
  the message's send time.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Queue a message for a registration, cancel the registration before the send time, and check
  whether the message is still sent.
```

## G11-EVENT_SMS-Q009

```yaml
QID: G11-EVENT_SMS-Q009
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A person who cancels their registration immediately after receiving a message does not receive a
  further message for the same event under the same, now-cancelled registration.
WHY_IT_MATTERS: >
  A further message under a cancelled registration continues contacting someone about an event they
  have already opted out of attending.
DISCONFIRMING_OBSERVATION: >
  A person receives an additional message for an event after already cancelling the registration
  that the message is tied to.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cancel a registration immediately after it receives a message, and check whether any further
  message for the same event still reaches that person.
```

## G11-EVENT_SMS-Q010

```yaml
QID: G11-EVENT_SMS-Q010
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reinstating a previously cancelled registration, where that is possible, does not silently skip a
  message that a continuously-held registration would have received at the same point before the
  event.
WHY_IT_MATTERS: >
  A silently skipped message leaves a reinstated registrant less informed than someone whose
  registration was never interrupted, with no indication anything was missed.
DISCONFIRMING_OBSERVATION: >
  A reinstated registration passes a scheduled message point with no message sent, where a
  continuously-held registration at the same point would have received one.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cancel and then reinstate a registration before a scheduled message point, and compare the
  outcome against a continuously-held registration at the same point.
```

## G11-EVENT_SMS-Q011

```yaml
QID: G11-EVENT_SMS-Q011
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The offset used to time a message relative to the event's date is computed against one
  consistently defined time reference, rather than left ambiguous between the event's own location
  and wherever the sending process happens to run.
WHY_IT_MATTERS: >
  An ambiguous reference means the same configured offset could resolve to different actual send
  times depending on incidental factors nobody deliberately chose.
DISCONFIRMING_OBSERVATION: >
  The same configured offset before the same event resolves to different actual send times
  depending on where the sending process happens to be running.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Configure a message offset relative to an event's date and verify what time reference that offset
  is actually computed against.
```

## G11-EVENT_SMS-Q012

```yaml
QID: G11-EVENT_SMS-Q012
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An event held in a time zone different from the sender's own operating location has its messages
  timed relative to the event's own local time, or an explicit, documented choice of a different
  reference, rather than an unexamined default.
WHY_IT_MATTERS: >
  An unexamined default could time a message hours off from what the recipient actually expects
  relative to the event they are attending.
DISCONFIRMING_OBSERVATION: >
  A message for an event in a different time zone from the sender's operating location is timed
  against a reference that is neither the event's local time nor a documented alternative.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Configure an event in a time zone different from the sending process's own location and check
  what time reference its messages are actually timed against.
```

## G11-EVENT_SMS-Q013

```yaml
QID: G11-EVENT_SMS-Q013
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A recipient in a third time zone, different from both the event's own and the sender's operating
  location, still receives a message timed by a reference that is explicit and consistent, not
  whichever zone happens to be computationally convenient.
WHY_IT_MATTERS: >
  An inconsistent reference for a third-zone recipient could time their message far earlier or
  later, relative to the event, than intended.
DISCONFIRMING_OBSERVATION: >
  A recipient in a third time zone receives a message timed by a reference that changes depending
  on incidental factors rather than a fixed, explicit rule.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Register a recipient in a time zone different from both the event's own and the sender's
  operating location, and check what reference their message timing is actually resolved against.
```

## G11-EVENT_SMS-Q014

```yaml
QID: G11-EVENT_SMS-Q014
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an event's date and its time zone are both changed together, the recalculated message timing
  correctly reflects the combined change rather than only one of the two.
WHY_IT_MATTERS: >
  Reflecting only one of the two changes leaves the message timed correctly by the old date's zone
  or the new zone's old date, neither of which matches reality.
DISCONFIRMING_OBSERVATION: >
  After an event's date and time zone are both changed, a still-pending message is recalculated
  correctly for one of the two changes but not the other.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Change both an event's date and its time zone together, and check whether a still-pending
  message's recalculated timing reflects both changes.
```

## G11-EVENT_SMS-Q015

```yaml
QID: G11-EVENT_SMS-Q015
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message scheduled at a fixed offset before the event that crosses a seasonal clock change
  between scheduling and send still lands at the intended real-world offset from the event, rather
  than shifting by the clock-change amount.
WHY_IT_MATTERS: >
  A shift by the clock-change amount could send a message an hour earlier or later relative to the
  event than was actually intended.
DISCONFIRMING_OBSERVATION: >
  A message scheduled across a seasonal clock change arrives at a real-world offset from the event
  that differs from the intended offset by the clock-change amount.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Schedule a message at a fixed offset before an event so that a seasonal clock change falls
  between scheduling and send, and check the actual real-world offset it lands at.
```

## G11-EVENT_SMS-Q016

```yaml
QID: G11-EVENT_SMS-Q016
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A single change to the event's date or status produces at most one recalculation outcome for a
  given already-scheduled message, not a duplicate message alongside the original.
WHY_IT_MATTERS: >
  A duplicate message from one underlying change contacts the recipient twice about the same thing,
  which reads as a mistake even when the content is accurate.
DISCONFIRMING_OBSERVATION: >
  A single change to an event's date or status results in two messages going out for what was one
  scheduled message.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Change an event's date or status once and check how many messages are triggered for a single
  already-scheduled message affected by that change.
```

## G11-EVENT_SMS-Q017

```yaml
QID: G11-EVENT_SMS-Q017
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two people independently correcting the same event detail in close succession do not each
  independently trigger a separate recalculation that results in two messages going out where one
  was intended.
WHY_IT_MATTERS: >
  An uncoordinated double trigger from two near-simultaneous edits sends the recipient a duplicate
  they have no reason to expect.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous corrections to the same event detail by two different people each
  independently trigger a message, producing two where one was expected.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have two people correct the same event detail in close succession and check how many messages are
  triggered as a result.
```

## G11-EVENT_SMS-Q018

```yaml
QID: G11-EVENT_SMS-Q018
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message that has already fired is not fired a second time merely because the event record it
  relates to is saved again with no substantive change.
WHY_IT_MATTERS: >
  A re-save triggering a repeat message treats an incidental administrative action as though it
  were a genuine change worth notifying the recipient about.
DISCONFIRMING_OBSERVATION: >
  Saving an event record again with no substantive change causes a message that had already fired
  to fire a second time.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Let a scheduled message fire, then save the related event record again with no substantive
  change, and check whether the message fires again.
```

## G11-EVENT_SMS-Q019

```yaml
QID: G11-EVENT_SMS-Q019
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a registration is transferred to a different person, a message still queued against that
  registration is redirected to the new registrant's own contact detail rather than continuing to
  target the person who transferred it away.
WHY_IT_MATTERS: >
  Continuing to target the original person after a transfer reaches someone no longer attending,
  while the person who will actually attend receives nothing.
DISCONFIRMING_OBSERVATION: >
  After a registration transfer, a still-queued message continues to target the original
  registrant's contact detail rather than the new one.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Queue a message against a registration, transfer that registration to a different person before
  the send time, and check which contact detail the message actually targets.
```

## G11-EVENT_SMS-Q020

```yaml
QID: G11-EVENT_SMS-Q020
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A person who has transferred their registration away does not continue to receive messages for an
  event they are no longer registered to attend.
WHY_IT_MATTERS: >
  Continued messages to someone no longer attending misinform them about their own status and may
  also reveal event detail to someone with no further stake in it.
DISCONFIRMING_OBSERVATION: >
  A person who transferred their registration away continues to receive messages about the event
  afterward.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Transfer a registration away from its original holder and check whether that original person
  continues to receive messages about the event.
```

## G11-EVENT_SMS-Q021

```yaml
QID: G11-EVENT_SMS-Q021
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The new registrant who receives a transferred registration receives whatever messages remain
  scheduled before the event, rather than being silently excluded because the schedule was
  originally fixed to the prior registrant.
WHY_IT_MATTERS: >
  A silently excluded new registrant misses information the event organizer intended every
  registrant to receive before the event.
DISCONFIRMING_OBSERVATION: >
  A new registrant who received a transferred registration receives none of the messages still
  scheduled before the event.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Transfer a registration to a new person with messages still scheduled before the event, and check
  whether the new registrant receives them.
```

## G11-EVENT_SMS-Q022

```yaml
QID: G11-EVENT_SMS-Q022
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message already sent before a registration transfer took place is not retroactively rewritten,
  but the record of the transfer is inspectable alongside it so a later reviewer can explain the
  mismatch between recipient and current registrant.
WHY_IT_MATTERS: >
  Without an inspectable transfer record, a reviewer seeing a message sent to someone no longer
  registered has no way to understand why, and might mistake it for an error.
DISCONFIRMING_OBSERVATION: >
  A message sent before a registration transfer, and the transfer itself, cannot both be found in a
  way that lets a reviewer connect the mismatch to its cause.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message, transfer the registration afterward, and check whether both the earlier message
  and the transfer record are retrievable together.
```

## G11-EVENT_SMS-Q023

```yaml
QID: G11-EVENT_SMS-Q023
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A message sent to one registrant does not include the identity of other attendees registered for
  the same event.
WHY_IT_MATTERS: >
  Disclosing other attendees' identities to a registrant who has no entitlement to that information
  breaches what each attendee expects to be shared with anyone else.
DISCONFIRMING_OBSERVATION: >
  A message sent to one registrant names or otherwise identifies a different attendee registered
  for the same event.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Send a message to one registrant of an event with multiple registrants and check whether it
  discloses any other attendee's identity.
```

## G11-EVENT_SMS-Q024

```yaml
QID: G11-EVENT_SMS-Q024
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A message sent to one registrant does not disclose the price or ticket type paid by a different
  attendee of the same event.
WHY_IT_MATTERS: >
  Disclosing another attendee's price exposes commercial detail that attendee has no reason to
  expect shared with anyone else.
DISCONFIRMING_OBSERVATION: >
  A message sent to one registrant discloses the price or ticket type belonging to a different
  attendee of the same event.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Send a message to one registrant of an event where attendees hold different ticket types or
  prices, and check whether it discloses another attendee's pricing detail.
```

## G11-EVENT_SMS-Q025

```yaml
QID: G11-EVENT_SMS-Q025
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A message about an event with more than one ticket type or price tier includes only the content
  relevant to its specific recipient's own registration.
WHY_IT_MATTERS: >
  Including content for tiers the recipient did not register for creates confusion about what they
  themselves actually paid for and are entitled to.
DISCONFIRMING_OBSERVATION: >
  A message sent to a registrant of one ticket type includes content describing a different ticket
  type or price tier that registrant did not register for.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Send a message to a registrant of one ticket type on an event with more than one tier, and check
  whether the content stays limited to that registrant's own tier.
```

## G11-EVENT_SMS-Q026

```yaml
QID: G11-EVENT_SMS-Q026
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A message addressed to a registrant whose own registration was cancelled or refunded does not
  disclose payment detail belonging to a different, still-active registrant for the same event.
WHY_IT_MATTERS: >
  A cancelled registrant has no ongoing stake in the event, and disclosing a different, active
  attendee's payment detail to them has no legitimate basis.
DISCONFIRMING_OBSERVATION: >
  A message reaching a registrant whose own registration was cancelled or refunded discloses
  payment detail belonging to a different, still-active registrant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Cancel or refund one registrant's registration on an event with other active registrants, trigger
  a message to the cancelled registrant, and check what it discloses.
```

## G11-EVENT_SMS-Q027

```yaml
QID: G11-EVENT_SMS-Q027
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether a sent message's content actually stayed within its recipient's own entitlement, rather
  than exceeding it, is something that can be determined afterward from the retained record of what
  was sent.
WHY_IT_MATTERS: >
  Without a retained, checkable record, a disclosure breach could go entirely unnoticed and
  uncorrectable after the fact.
DISCONFIRMING_OBSERVATION: >
  The retained record of a sent message is insufficient to determine afterward whether its content
  actually stayed within the recipient's own entitlement.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message and attempt, from the retained record alone, to verify whether its content stayed
  within the recipient's own entitlement.
```

## G11-EVENT_SMS-Q028

```yaml
QID: G11-EVENT_SMS-Q028
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A failure to deliver a message does not, by itself, block or delay the registration process it
  relates to.
WHY_IT_MATTERS: >
  A blocked registration process over an undelivered message turns a communication failure into a
  transaction failure that should never have depended on it.
DISCONFIRMING_OBSERVATION: >
  A registration process is blocked or delayed because a message related to it failed to deliver.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Force a message delivery failure and check whether the related registration process is blocked or
  delayed as a result.
```

## G11-EVENT_SMS-Q029

```yaml
QID: G11-EVENT_SMS-Q029
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A delivery failure for a message tied to an approaching, immovable event date is surfaced with
  more urgency than a failure with no deadline behind it, rather than being queued identically
  regardless of how close the event is.
WHY_IT_MATTERS: >
  A failure noticed too late to correct before the fixed event moment is effectively the same as a
  failure never noticed at all.
DISCONFIRMING_OBSERVATION: >
  A delivery failure close to an event's fixed date is surfaced with no more urgency than a failure
  for a message with no approaching deadline at all.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Force a delivery failure for a message close to an event's date and compare how it is surfaced
  against a failure with no approaching deadline.
```

## G11-EVENT_SMS-Q030

```yaml
QID: G11-EVENT_SMS-Q030
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message retried repeatedly against an unreachable recipient eventually stops retrying, rather
  than continuing indefinitely as the event's fixed date passes.
WHY_IT_MATTERS: >
  Indefinite retries after the event has already occurred waste effort on a message that can no
  longer serve any purpose.
DISCONFIRMING_OBSERVATION: >
  A message continues retrying against an unreachable recipient after the event's own date has
  already passed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Force repeated delivery failures against one recipient across the event's date and check whether
  retries stop at some point.
```

## G11-EVENT_SMS-Q031

```yaml
QID: G11-EVENT_SMS-Q031
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message that fails permanently and is never delivered leaves a retained record of the attempt,
  distinguishable from a message that succeeded.
WHY_IT_MATTERS: >
  Without a distinguishable record, a permanently failed message looks the same afterward as one
  that actually reached its recipient.
DISCONFIRMING_OBSERVATION: >
  A permanently failed message's retained record is indistinguishable from that of a message that
  was actually delivered.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force a message to fail permanently and compare its retained record against that of a
  successfully delivered message.
```

## G11-EVENT_SMS-Q032

```yaml
QID: G11-EVENT_SMS-Q032
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message type explicitly configured as not required for the registration process to proceed does
  not hold up that process while its own delivery status remains unresolved.
WHY_IT_MATTERS: >
  A message the business has explicitly declared non-essential should never be the reason a real
  registration is held up.
DISCONFIRMING_OBSERVATION: >
  The registration process waits on the resolution of a message type explicitly configured as not
  required for it to proceed.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Configure a message type as not required for the registration process, leave its delivery status
  unresolved, and observe whether the process proceeds regardless.
```

## G11-EVENT_SMS-Q033

```yaml
QID: G11-EVENT_SMS-Q033
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling a registration after a message about it has already been irreversibly sent leaves an
  explicit, inspectable record that the send happened before the cancellation, not merely that both
  events occurred at some point.
WHY_IT_MATTERS: >
  Without an explicit ordering record, nobody can later confirm whether the message went out before
  or after the person actually cancelled.
DISCONFIRMING_OBSERVATION: >
  A registration's cancellation and an earlier, already-sent message about it are both recorded, but
  nothing establishes which happened first.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message, cancel the related registration afterward, and check whether the record
  establishes the actual order of the two events.
```

## G11-EVENT_SMS-Q034

```yaml
QID: G11-EVENT_SMS-Q034
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  There is a way to determine, for any given cancellation, whether it occurred before or after the
  point past which an already-triggered message could still have been stopped.
WHY_IT_MATTERS: >
  Without that determination, nobody can tell whether a message that went out anyway was
  unavoidable or was a failure to act on a cancellation in time.
DISCONFIRMING_OBSERVATION: >
  For a given cancellation, there is no way to determine whether it occurred before or after the
  point past which the related message could still have been stopped.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Cancel a registration at a known point relative to a message's stoppable window, and check whether
  the record allows determining which side of that point the cancellation fell on.
```

## G11-EVENT_SMS-Q035

```yaml
QID: G11-EVENT_SMS-Q035
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A cancellation that occurs with no message ever having been triggered for that registration
  proceeds with no special handling related to messaging at all.
WHY_IT_MATTERS: >
  Applying messaging-related handling to a cancellation that never involved a message would be an
  unnecessary and potentially confusing extra step.
DISCONFIRMING_OBSERVATION: >
  Cancelling a registration for which no message was ever triggered still invokes messaging-related
  handling with nothing for it to act on.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cancel a registration before any message for it has ever been triggered, and check whether any
  messaging-related handling is invoked regardless.
```

## G11-EVENT_SMS-Q036

```yaml
QID: G11-EVENT_SMS-Q036
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The sender identity a recipient sees on a message reflects the specific company or branch actually
  hosting the event, not a shared default that obscures which company the event belongs to.
WHY_IT_MATTERS: >
  A shared, obscuring default leaves the recipient unable to tell which company is actually
  contacting them about the event.
DISCONFIRMING_OBSERVATION: >
  A message's visible sender identity does not reflect the specific company or branch actually
  hosting the event it concerns.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Generate a message for an event hosted by a specific company or branch and check what sender
  identity the recipient actually sees.
```

## G11-EVENT_SMS-Q037

```yaml
QID: G11-EVENT_SMS-Q037
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The cost of sending a message is attributed to the company or branch that owns the event it
  concerns, not pooled indiscriminately across every company sharing the same messaging channel.
WHY_IT_MATTERS: >
  Indiscriminate pooling leaves each company unable to see its own actual cost of messaging its own
  attendees.
DISCONFIRMING_OBSERVATION: >
  The cost of sending a message for one company's event is attributed to a shared pool rather than
  to the company that owns the event.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Send a message for an event owned by a specific company sharing a messaging channel with other
  companies, and check how the cost is attributed.
```

## G11-EVENT_SMS-Q038

```yaml
QID: G11-EVENT_SMS-Q038
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an event is transferred or co-hosted between companies before its date, the sender identity
  used for its messages reflects the current hosting company at send time, not whichever company
  hosted it when the registration was first made.
WHY_IT_MATTERS: >
  A stale sender identity from the original host misrepresents who is actually running the event by
  the time the message is received.
DISCONFIRMING_OBSERVATION: >
  A message sent after an event's hosting company changed still carries the sender identity of the
  original, no-longer-hosting company.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Transfer an event's hosting company after some registrations exist, send a message afterward, and
  check which company's sender identity it carries.
```

## G11-EVENT_SMS-Q039

```yaml
QID: G11-EVENT_SMS-Q039
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A company with a single, unambiguous sender identity and no shared configuration in play
  experiences no cross-company sender ambiguity on its own event messages.
WHY_IT_MATTERS: >
  A company with nothing shared should never see an ambiguous or incorrect sender identity purely as
  an artifact of a multi-company design.
DISCONFIRMING_OBSERVATION: >
  A company with a single, unambiguous sender identity and no shared configuration still sees an
  ambiguous or incorrect sender identity on its own event messages.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a company with a single, unambiguous sender identity and no shared configuration, send a
  message for its own event, and check the sender identity the recipient sees.
```

## G11-EVENT_SMS-Q040

```yaml
QID: G11-EVENT_SMS-Q040
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When outbound volume for messages approaching one event's date exceeds a rate limit, the delayed
  messages are prioritized so as many as possible still arrive before that event's fixed moment,
  rather than being delayed in an order indifferent to the deadline.
WHY_IT_MATTERS: >
  A deadline-indifferent delay order can let messages for an imminent event sit behind messages for
  an event that is still weeks away.
DISCONFIRMING_OBSERVATION: >
  When a rate limit delays outbound messages, a message for an imminent event is delayed behind a
  message for a much later event with no deadline-based prioritization applied.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Exceed the outbound rate limit with messages for events at different distances from their own
  dates, and check the order in which delayed messages are actually sent.
```

## G11-EVENT_SMS-Q041

```yaml
QID: G11-EVENT_SMS-Q041
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A rate limit applied across multiple events sharing the same sending window does not let one large
  event's message volume consume the capacity a different, smaller event's equally time-critical
  messages also need before their own fixed date.
WHY_IT_MATTERS: >
  One event's volume starving another event's capacity means the smaller event's attendees miss
  reminders through no fault connected to their own event at all.
DISCONFIRMING_OBSERVATION: >
  A large event's message volume consumes shared rate-limit capacity to the point that a different,
  smaller event's time-critical messages are delayed past their own event's date.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Run a large event's message volume against a shared rate limit alongside a smaller event's
  time-critical messages, and check whether the smaller event's messages are delayed past its own
  date.
```

## G11-EVENT_SMS-Q042

```yaml
QID: G11-EVENT_SMS-Q042
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message delayed past the event's own date by a rate limit is handled by an explicit rule, such
  as being withdrawn as no longer relevant, rather than being sent late as though the deadline had
  not already passed.
WHY_IT_MATTERS: >
  Sending a message after its own event has already happened, with no rule addressing that case,
  delivers content that no longer makes sense to the recipient.
DISCONFIRMING_OBSERVATION: >
  A message delayed by a rate limit past its own event's date is sent anyway, unchanged, as though
  the date had not already passed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Delay a message past its own event's date using a rate limit, and check whether it is withdrawn or
  sent unchanged once the date has passed.
```

## G11-EVENT_SMS-Q043

```yaml
QID: G11-EVENT_SMS-Q043
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Ordinary message volume, well under the rate limit, is never delayed or queued by the limiting
  mechanism at all.
WHY_IT_MATTERS: >
  A rate limit that delays traffic it was never meant to affect introduces unnecessary risk to
  messages that had no need to be queued in the first place.
DISCONFIRMING_OBSERVATION: >
  Message volume well under the rate limit is still delayed or queued by the limiting mechanism.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Send ordinary message volume well under the configured rate limit and check whether any of it is
  delayed or queued regardless.
```

## G11-EVENT_SMS-Q044

```yaml
QID: G11-EVENT_SMS-Q044
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The retained record of a past message preserves the actual content that was sent, or a faithful
  copy of it, rather than only a reference to a template that may since have changed.
WHY_IT_MATTERS: >
  A reference-only record cannot reconstruct what a recipient actually received once the underlying
  template has since been edited.
DISCONFIRMING_OBSERVATION: >
  The retained record of a past message holds only a reference to its composing template, with no
  way to recover the actual content sent at the time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message, edit its composing content afterward, and check whether the retained record still
  holds the actual content originally sent.
```

## G11-EVENT_SMS-Q045

```yaml
QID: G11-EVENT_SMS-Q045
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message's stored record identifies which version of its composing content actually produced the
  message a recipient received, distinct from whatever the content produces now.
WHY_IT_MATTERS: >
  Without that version identification, a later content edit makes it impossible to tell which
  version actually generated a specific past send.
DISCONFIRMING_OBSERVATION: >
  After a content edit, there is no way to determine which version of the content a previously sent
  message was actually generated from.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Send a message from one version of its composing content, edit the content afterward, and attempt
  to determine which version actually produced the earlier send.
```

## G11-EVENT_SMS-Q046

```yaml
QID: G11-EVENT_SMS-Q046
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Editing the message content or timing rule after some messages for an event have already gone out
  does not retroactively change the retained record of what those earlier messages actually said or
  when they were actually sent.
WHY_IT_MATTERS: >
  A retroactively altered record erases the ability to confirm what recipients genuinely received
  before the edit took effect.
DISCONFIRMING_OBSERVATION: >
  Editing the message content or timing rule changes the retained record of messages that had
  already been sent before the edit.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Send some messages for an event, edit the content or timing rule afterward, and check whether the
  retained record of the earlier messages changed.
```

## G11-EVENT_SMS-Q047

```yaml
QID: G11-EVENT_SMS-Q047
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reconstructing what a specific past message said, after its underlying content has since been
  edited, is possible from the retained record rather than only from the current content.
WHY_IT_MATTERS: >
  If reconstruction is only possible from the current content, a past message can never be verified
  again once its template moves on.
DISCONFIRMING_OBSERVATION: >
  After a content edit, there is no way to reconstruct what a specific past message actually said
  from anything other than the current content.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message, edit its composing content afterward, and attempt to reconstruct the original
  message's actual content from the retained record.
```

## G11-EVENT_SMS-Q048

```yaml
QID: G11-EVENT_SMS-Q048
MODULE: event_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether a discrepancy between a retained past message and what the current content would produce
  for the same inputs reflects an intentional content change or an unintended drift is something the
  retained record makes possible to determine.
WHY_IT_MATTERS: >
  Without that determination, an inconsistency between old and new output looks the same whether it
  was a deliberate improvement or an accidental defect.
DISCONFIRMING_OBSERVATION: >
  A discrepancy is found between a retained past message and what the current content would produce,
  and the retained record gives no way to tell whether that reflects an intentional change or an
  unintended drift.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Compare a retained past message against what the current content would produce for the same
  inputs, and attempt to determine from the record alone whether any discrepancy was intentional.
```
