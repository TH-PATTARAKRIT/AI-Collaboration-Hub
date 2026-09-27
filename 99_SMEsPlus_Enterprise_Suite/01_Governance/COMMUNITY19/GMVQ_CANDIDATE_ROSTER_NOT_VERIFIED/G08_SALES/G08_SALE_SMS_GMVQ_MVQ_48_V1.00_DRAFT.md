# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_sms Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE_SMS-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_sms`
**Wave:** W2
**Author Cell:** P-S9 (GMVQ Question Factory — Internal Production Team S9, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

`sale_sms` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Its seam is an outbound notification triggered specifically by ORDER state. Per the Bridge Module Rule, every question in this bank was tested against the seam question: "if this capability were removed and the order and the notification mechanism were used entirely apart, would the question still make sense?" A YES answer means the question belongs to the base `sale` bank or restates generic notification-lifecycle ground already covered elsewhere, and was cut.

A sibling notification bank already exists in a different group and was read in full before authoring: `G05_STOCK_SMS` (48 questions), which thoroughly covers generic notification-lifecycle mechanics — reversal of the triggering state before/after send, duplicate-trigger deduplication across paths, content freshness at compose time, recipient-contact validity and party-change handling, entitlement-based content filtering, delivery-failure escalation and retry limits, send irreversibility and rollback handling, per-tenant sender identity and cost attribution, per-tenant rate limiting, and template versioning. None of that generic ground is repeated here. This bank is built around what is specific to a SALES ORDER's own commitment content and structure: a quoted amount, date, or balance going stale after the order is modified (not reversed); recipient-role selection between the ordering contact and the delivery contact when they differ; opt-out and consent enforcement; the message standing as the sole documentary record of a promised term; selling-company versus fulfilling-company identity in a multi-company sales chain; order-wide aggregate readiness against single-line triggering; time-limited commitments and expiring-offer deadlines; automated and bulk-created orders; customer-specific negotiated commitment terms; order splitting into separate fulfillments; and accidental duplicate order submission.

This bank reaches 48 material, non-overlapping questions, but it is the thinnest of the four in this submission: `event_sms` and `crm_sms` were, per the routing brief, still being authored elsewhere at the time of this session and could not be checked, so ground later found to belong to one of them may require a delta pass on this bank once those banks exist (Authoring Standard §7).

## Control

- Mandatory pre-authoring sibling check performed against `G05_STOCK_SMS_GMVQ_MVQ_48_V1.00_DRAFT.md` (48 questions, a different group but named as the required check by this module's own routing brief). `event_sms` and `crm_sms` did not exist on disk at authoring time and could not be checked; per Bridge Module Rule §5 this is recorded as a known gap rather than assumed clear.
- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong, and the disconfirming observation is a distinct event for every question — no two questions share one failure event.
- No padding: 48 questions exist because they test 48 distinct material hypotheses at the seam. Every one of the 48 questions was tested against `G05_STOCK_SMS`'s covered ground and cut if it restated generic notification-lifecycle mechanics; this is the practical ceiling of order-specific, non-overlapping material found — no question here pads toward a round number.
- This module carries one layer at the seam; the `LAYER` field is omitted throughout.
- Clean-room compliance: no vendor or product name, no technical identifier (model, table, field, method, XML ID, API path, standard or profile name), and no implementation shape appears anywhere in question text.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank. Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.
- Seam dimensions represented (GMVQ_BRIDGE_MODULE_RULE_V1.00 §3): timing (Q001-Q002, Q030-Q032, Q047-Q048), ownership (Q003, Q007-Q010, Q013-Q014, Q017-Q019, Q021-Q022, Q024, Q035, Q038-Q039, Q045-Q046), quantity and money (Q004, Q034, Q036, Q043), partiality (Q005, Q025-Q026, Q029), reversal (Q006, Q028), lifecycle mismatch (Q011, Q015, Q020, Q023, Q033, Q040-Q042, Q044), authority (Q012, Q016), ordering (Q027), error asymmetry (Q037).
- Coverage map: post-send content staling due to order modification Q001-Q006 · recipient role selection between ordering and delivery contacts Q007-Q011 · opt-out and consent enforcement for order-triggered messages Q012-Q016 · the message as sole documentary record of a promised term Q017-Q020 · selling-company vs fulfilling-company identity in a multi-company sales chain Q021-Q024 · order-level aggregate readiness vs single-line triggering Q025-Q029 · time-limited commitment and expiring-offer deadlines Q030-Q034 · automated and bulk-created orders and message-content accuracy discipline Q035-Q038 · customer-specific negotiated commitment terms in generic template content Q039-Q041 · order splitting into multiple separate fulfillments Q042-Q045 · accidental duplicate order submission Q046-Q048

## G08-SALE_SMS-Q001

```yaml
QID: G08-SALE_SMS-Q001
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A confirmation message that quoted a specific total amount for the order is not treated as still accurate
  after the order's price or lines change; the change is recognized as requiring a distinct decision about
  whether the customer needs a corrected communication, rather than the original message being left standing as
  though it still described the current order.
WHY_IT_MATTERS: >
  A customer who received one quoted total and later sees a different final charge, with no communication
  explaining the change, is likely to dispute the difference as an error rather than an intended change.
DISCONFIRMING_OBSERVATION: >
  An order's total is changed after a confirmation message quoting the original total was sent, and nothing in
  the system flags that the sent commitment no longer matches the order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a confirmation message quoting an order's total, then change the order's price after sending, and check
  whether the discrepancy is flagged anywhere.
```

## G08-SALE_SMS-Q002

```yaml
QID: G08-SALE_SMS-Q002
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A confirmation message that quoted a specific promised date is distinguishable, after the order's schedule
  changes, from a message whose quoted date still matches the order, so staff can tell which customers are
  currently holding an outdated date without checking each order individually.
WHY_IT_MATTERS: >
  Without that distinction, discovering which customers were told a now-wrong date requires manually checking
  every order, which does not scale and is likely to be skipped under time pressure.
DISCONFIRMING_OBSERVATION: >
  There is no way to list which sent confirmation messages quoted a date that no longer matches the order's
  current schedule.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send confirmation messages for several orders, change the schedule on some but not others, and attempt to list
  which sent messages are now outdated.
```

## G08-SALE_SMS-Q003

```yaml
QID: G08-SALE_SMS-Q003
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an order is repriced downward after a confirmation message quoted the original higher total, any refund
  calculation tied to that change references the order's own record of what actually changed, not the amount
  quoted in the message, since the message is a communication and not itself the authoritative figure.
WHY_IT_MATTERS: >
  If a downstream refund calculation could reference message text instead of the order's own record, a purely
  textual artifact would end up governing an actual financial outcome.
DISCONFIRMING_OBSERVATION: >
  A refund or credit calculation after a reprice derives its amount from the previously sent message's quoted
  figure rather than from the order's own recorded change.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reprice an order downward after a confirmation message quoted the original total, then trigger a refund
  calculation and check what figure it actually uses.
```

## G08-SALE_SMS-Q004

```yaml
QID: G08-SALE_SMS-Q004
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A balance-due figure quoted in a message is computed from the same order and payment data the order's own
  balance display uses, so the two are never shown differently to two different audiences at the same moment.
WHY_IT_MATTERS: >
  A separately computed balance figure in the message can drift from the order's own display if the two are
  calculated through different logic or at different moments.
DISCONFIRMING_OBSERVATION: >
  The balance-due figure in a sent message differs from the balance shown on the order's own record at the same
  point in time.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compare a balance-due figure quoted in a sent message against the order's own balance display taken at the
  same moment.
```

## G08-SALE_SMS-Q005

```yaml
QID: G08-SALE_SMS-Q005
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Multiple order modifications occurring before any corrective communication is sent are consolidated into one
  corrective message reflecting the net current state, rather than triggering a separate message for each
  individual modification that would leave the customer with several fragmentary, possibly contradictory
  updates.
WHY_IT_MATTERS: >
  A flurry of separate messages for each small change is more likely to confuse a customer than one clear
  statement of where things currently stand.
DISCONFIRMING_OBSERVATION: >
  Three unrelated modifications made to an order in quick succession each trigger their own separate corrective
  message rather than being consolidated into one.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Make several modifications to an order in quick succession and observe whether one consolidated message or
  several separate ones result.
```

## G08-SALE_SMS-Q006

```yaml
QID: G08-SALE_SMS-Q006
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an order after a confirmation message already quoted a specific commitment does not, by itself,
  determine whether the customer is owed anything under that commitment; the quoted commitment is retained as
  evidence for that determination rather than being discarded once the order is cancelled.
WHY_IT_MATTERS: >
  Discarding the quoted commitment on cancellation would remove the one record of what was actually promised,
  right at the point a dispute over that promise is most likely to arise.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order after a confirmation message was sent makes the previously quoted commitment content
  unavailable for review.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a confirmation message quoting a commitment, cancel the order, and attempt to retrieve the previously
  quoted commitment content.
```

## G08-SALE_SMS-Q007

```yaml
QID: G08-SALE_SMS-Q007
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Which contact on an order actually receives a given type of order-triggered message, the person who placed the
  order or the person the goods are being delivered to, is a defined choice per message type, not an incidental
  result of whichever contact field happens to be populated first.
WHY_IT_MATTERS: >
  An undefined choice means the same message type can reach different people on different orders purely by
  accident of data entry order, with no one having decided that should be the rule.
DISCONFIRMING_OBSERVATION: >
  Asked which contact a specific order-triggered message type is meant to reach when the ordering and delivery
  contacts differ, no defined rule exists that answers the question.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure an order with different ordering and delivery contacts and inspect the configuration governing which
  one a given message type targets.
```

## G08-SALE_SMS-Q008

```yaml
QID: G08-SALE_SMS-Q008
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message concerning a financial or account-level matter, such as a balance or a payment obligation, reaches
  the ordering contact specifically, since that is the party with the actual financial relationship, even when a
  different delivery contact is set on the same order.
WHY_IT_MATTERS: >
  Sending a financial commitment only to a delivery contact who has no actual payment relationship with the
  business risks the responsible party never learning of an obligation attributed to them.
DISCONFIRMING_OBSERVATION: >
  A payment-related message for an order is sent to the delivery contact instead of the ordering contact when
  the two differ.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure an order with differing ordering and delivery contacts, trigger a payment-related message, and check
  which contact receives it.
```

## G08-SALE_SMS-Q009

```yaml
QID: G08-SALE_SMS-Q009
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message concerning physical fulfillment, such as a delivery-window notice, reaches the delivery contact
  specifically, since that is the party actually present to receive the goods, even where the ordering contact
  differs.
WHY_IT_MATTERS: >
  Sending a delivery-window notice only to an ordering contact who is not physically present defeats the purpose
  of that specific message type.
DISCONFIRMING_OBSERVATION: >
  A delivery-related message for an order is sent to the ordering contact instead of the delivery contact when
  the two differ.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure an order with differing ordering and delivery contacts, trigger a delivery-related message, and
  check which contact receives it.
```

## G08-SALE_SMS-Q010

```yaml
QID: G08-SALE_SMS-Q010
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where an order specifies more than one legitimately interested contact for the same message type, such as both
  a company's purchasing contact and its receiving contact needing the same notice, the message reaches both
  through a deliberate configuration rather than an accidental duplicate send discovered only by the recipients
  comparing notes.
WHY_IT_MATTERS: >
  An accidental rather than deliberate multi-recipient send suggests the business does not actually control who
  learns of its commitments.
DISCONFIRMING_OBSERVATION: >
  Both an ordering and a delivery contact receive the same message type with no configuration indicating that
  dual delivery was intended.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an order with both contacts populated and trigger a message type, checking whether dual delivery is
  a deliberate, visible configuration.
```

## G08-SALE_SMS-Q011

```yaml
QID: G08-SALE_SMS-Q011
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing the delivery contact on an order after a delivery-related message has already been sent to the
  original delivery contact does not, by itself, resend that same message to the new contact without a
  deliberate decision, since the new contact may not need the same historical information repeated.
WHY_IT_MATTERS: >
  Automatically flooding a newly added contact with every prior message could disclose commitment history to
  someone who was not part of the original relationship.
DISCONFIRMING_OBSERVATION: >
  Changing the delivery contact automatically triggers a resend of a previously sent delivery message to the new
  contact with no deliberate decision to do so.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Send a delivery-related message, then change the order's delivery contact, and observe whether the prior
  message is automatically resent.
```

## G08-SALE_SMS-Q012

```yaml
QID: G08-SALE_SMS-Q012
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A customer who has opted out of this kind of outbound message does not receive an order-triggered message of
  that kind, regardless of which specific order or state transition triggers it.
WHY_IT_MATTERS: >
  Sending to an opted-out customer anyway is both a broken promise to that customer and, depending on the
  jurisdiction, a compliance failure.
DISCONFIRMING_OBSERVATION: >
  An order belonging to a customer who has opted out of this message type still triggers and sends that message.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Opt a customer out of a message type, trigger the order state that would normally send it, and check whether
  the message goes out anyway.
```

## G08-SALE_SMS-Q013

```yaml
QID: G08-SALE_SMS-Q013
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a message type is distinguished as transactional, necessary to inform the customer of something
  concerning a transaction already underway, versus promotional, opt-out enforcement treats the two differently
  according to that distinction, rather than one opt-out setting blocking both indiscriminately or neither.
WHY_IT_MATTERS: >
  Blocking a genuinely transactional notice because of a promotional opt-out could leave a customer uninformed
  about their own live order; failing to block a promotional message under the same setting ignores a stated
  preference.
DISCONFIRMING_OBSERVATION: >
  A customer who opted out of promotional messages only also stops receiving a transactional message concerning
  an order already in progress.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a customer opted out of promotional messages only, trigger a transactional order-state message, and
  check whether it still sends.
```

## G08-SALE_SMS-Q014

```yaml
QID: G08-SALE_SMS-Q014
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An opt-out recorded against a specific contact applies to messages addressed to that contact specifically, and
  does not silently extend to, or get bypassed by, a different contact on the same order who has not opted out.
WHY_IT_MATTERS: >
  Conflating opt-out status across different people on the same order either wrongly silences someone who never
  opted out or wrongly continues messaging someone who did.
DISCONFIRMING_OBSERVATION: >
  An opt-out recorded for one contact on an order also suppresses, or fails to suppress, the same message type
  addressed to a different, non-opted-out contact on that order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Opt out one of two contacts on the same order, trigger a message addressed to each, and check whether opt-out
  status is applied per contact correctly.
```

## G08-SALE_SMS-Q015

```yaml
QID: G08-SALE_SMS-Q015
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A customer's opt-out decision is retained independent of which specific order it was recorded against, so it
  continues to apply to that customer's future orders rather than needing to be re-recorded for every new order.
WHY_IT_MATTERS: >
  An opt-out that silently expires with each new order effectively nullifies the customer's stated preference
  the moment they place their next order.
DISCONFIRMING_OBSERVATION: >
  A customer's prior opt-out no longer suppresses the message type on a newly created order for that same
  customer.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record an opt-out for a customer, then create a new order for that same customer and trigger the message type,
  checking whether the opt-out still applies.
```

## G08-SALE_SMS-Q016

```yaml
QID: G08-SALE_SMS-Q016
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a specific message type is capable of being opted out of at all, as distinct from being mandatory
  regardless of preference, is a defined and documented classification for that message type, not an implicit
  assumption left to whoever configured it.
WHY_IT_MATTERS: >
  Without a documented classification, it cannot be determined afterward whether a given message correctly
  ignored an opt-out because it was genuinely mandatory or incorrectly ignored it by oversight.
DISCONFIRMING_OBSERVATION: >
  Asked whether a specific order-triggered message type honours opt-out at all, no documented classification
  exists that answers the question.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Inspect the configuration for a specific message type to determine whether its opt-out-eligible or mandatory
  classification is explicitly documented.
```

## G08-SALE_SMS-Q017

```yaml
QID: G08-SALE_SMS-Q017
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a specific commitment term is stated only within the body of an order-triggered message and nowhere else
  in the order's own structured fields, such as a one-time condition described in free text, the sent message's
  exact content remains retrievable as the only record of that specific term.
WHY_IT_MATTERS: >
  If the message is not retained, and the term exists nowhere else, the business loses its own only record of
  what it actually promised.
DISCONFIRMING_OBSERVATION: >
  A commitment term stated only in a sent message's free text is not retrievable once the message leaves the
  outbound queue.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Compose a message containing a commitment term with no equivalent structured field on the order, send it, and
  attempt to retrieve the exact sent content afterward.
```

## G08-SALE_SMS-Q018

```yaml
QID: G08-SALE_SMS-Q018
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a dispute concerns a term that exists only in a sent message's content, that content is treated with the
  same evidentiary weight as any other retained business record, not dismissed as merely a notification with no
  bearing on what was actually promised.
WHY_IT_MATTERS: >
  Treating the message as disposable communication rather than a record of commitment leaves the business unable
  to honour, or contest, a promise it actually made.
DISCONFIRMING_OBSERVATION: >
  A dispute referencing a specific term stated only in a sent message is resolved without consulting that
  message's retained content at all.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise a dispute over a term stated only in a previously sent message and check whether that message's content
  is consulted in resolving it.
```

## G08-SALE_SMS-Q019

```yaml
QID: G08-SALE_SMS-Q019
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A message containing a term not reflected anywhere in the order's own structured record is flagged, at the
  time it is composed, as introducing content the order itself does not capture, so the gap between what was
  promised and what is formally recorded is visible rather than silent.
WHY_IT_MATTERS: >
  A silent gap between promised and recorded content means the business may not even know it made a commitment
  outside its own formal record until a customer raises it.
DISCONFIRMING_OBSERVATION: >
  Composing a message containing a term absent from the order's structured record produces no indication that
  the message content exceeds what the order itself formally captures.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Compose a message with a term not present on the order's structured fields and check whether any indication of
  the gap is surfaced.
```

## G08-SALE_SMS-Q020

```yaml
QID: G08-SALE_SMS-Q020
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Deleting or purging a sent message's retained content follows the same retention discipline as other business
  records that could serve as evidence of a customer commitment, not a shorter, unrelated general message-log
  cleanup policy.
WHY_IT_MATTERS: >
  A general log-cleanup policy tuned for storage efficiency was never designed with evidentiary retention of
  specific customer commitments in mind.
DISCONFIRMING_OBSERVATION: >
  A sent message containing a customer commitment term becomes unavailable earlier than the retention period
  applicable to customer commitment evidence would require.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the retention period applied to sent message content against the retention period applicable to
  customer commitment evidence generally.
```

## G08-SALE_SMS-Q021

```yaml
QID: G08-SALE_SMS-Q021
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where an order is contracted through one company but fulfilled through a different company's branch, such as
  in a drop-ship or marketplace arrangement, the sender identity on an order-triggered message reflects the
  contracting company the customer actually transacted with, not the fulfilling company the customer has no
  direct relationship with.
WHY_IT_MATTERS: >
  A message appearing to come from an unfamiliar fulfilling company, rather than the company the customer
  actually placed the order with, is likely to be mistaken for an unrelated or suspicious message.
DISCONFIRMING_OBSERVATION: >
  An order-triggered message for a drop-ship or marketplace-style order identifies the fulfilling company as the
  sender rather than the contracting company.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an order with distinct contracting and fulfilling companies and trigger a message, checking which
  company's identity appears as sender.
```

## G08-SALE_SMS-Q022

```yaml
QID: G08-SALE_SMS-Q022
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the fulfilling company in such an arrangement needs to communicate something only it can speak to, such
  as a specific delivery detail, that message is clearly attributed to the fulfilling party acting on behalf of
  the contracting company, rather than presented ambiguously as though it came from an unspecified sender.
WHY_IT_MATTERS: >
  An ambiguous sender leaves the customer unable to tell who is actually communicating with them or whom to
  contact with a question.
DISCONFIRMING_OBSERVATION: >
  A fulfillment-specific message in a multi-company arrangement gives no indication of the fulfilling party's
  relationship to the contracting company the customer actually ordered from.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Trigger a fulfillment-specific message in a multi-company arrangement and check how the relationship between
  the two companies is communicated to the customer.
```

## G08-SALE_SMS-Q023

```yaml
QID: G08-SALE_SMS-Q023
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to which company fulfills an order after a message has already been sent identifying the original
  fulfilling company does not retroactively alter the sender identity shown on the retained record of that
  already-sent message.
WHY_IT_MATTERS: >
  Rewriting the retained sender identity after the fact would misstate who the customer actually understood
  themselves to be dealing with at the time the message was sent.
DISCONFIRMING_OBSERVATION: >
  Reassigning an order's fulfilling company after a message was sent causes the retained record of that earlier
  message to display the new fulfilling company as sender instead of the original one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message under one fulfilling company, reassign the order's fulfilling company, then inspect the
  retained record of the earlier message for its shown sender.
```

## G08-SALE_SMS-Q024

```yaml
QID: G08-SALE_SMS-Q024
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the contracting company is not fully configured with what a specific message type needs, such as its own
  sender details, the message is blocked or held rather than sent under the fulfilling company's identity as an
  unrequested substitute.
WHY_IT_MATTERS: >
  Substituting the fulfilling company's identity to work around a configuration gap sends a message under an
  identity the customer relationship is not actually with.
DISCONFIRMING_OBSERVATION: >
  A contracting company missing part of its messaging identity configuration still has messages sent to its
  customers under the fulfilling company's identity as a fallback.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Remove part of a contracting company's messaging identity configuration in a multi-company arrangement and
  trigger a message, checking whose identity is used.
```

## G08-SALE_SMS-Q025

```yaml
QID: G08-SALE_SMS-Q025
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message implying the order as a whole is ready, complete, or fulfilled is triggered only once every line of
  that order has actually reached that state, not by the first line to reach it while others remain outstanding.
WHY_IT_MATTERS: >
  Telling a customer their whole order is ready when part of it is not sets an expectation the business cannot
  yet meet, and the customer may act on it, for instance by traveling to collect it.
DISCONFIRMING_OBSERVATION: >
  An order-wide readiness message sends when only one of several lines has actually become ready, with the rest
  still outstanding.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Bring one line of a multi-line order to a ready state while others remain outstanding, and check whether an
  order-wide readiness message sends.
```

## G08-SALE_SMS-Q026

```yaml
QID: G08-SALE_SMS-Q026
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where an order is genuinely being fulfilled in separate parts and the business intends to notify the customer
  of each part's readiness individually, each such message is clearly scoped to the specific lines it actually
  covers, rather than worded as though it concerned the whole order.
WHY_IT_MATTERS: >
  A message worded as covering the whole order, when it actually only covers part of it, could lead a customer
  to believe everything is ready when only a portion is.
DISCONFIRMING_OBSERVATION: >
  A message about one part of a split fulfillment is worded identically to a message about the complete order,
  with nothing distinguishing partial from full readiness.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Configure an order fulfilled in two separate parts, trigger a readiness message for the first part alone, and
  check whether its wording reflects partial rather than full readiness.
```

## G08-SALE_SMS-Q027

```yaml
QID: G08-SALE_SMS-Q027
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once every line of an order has actually reached the ready state, at whatever separate times each one did so,
  an order-wide readiness message triggers exactly once for the order as a whole, not once per line reaching
  that state independently.
WHY_IT_MATTERS: >
  A separate order-wide message firing for every line reaching readiness would send the customer several
  redundant, confusing notifications about what is really one event.
DISCONFIRMING_OBSERVATION: >
  A multi-line order produces a separate order-wide readiness message each time an individual line becomes
  ready, rather than one message once all lines are ready together.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Bring the lines of a multi-line order to readiness at different times and observe how many order-wide
  readiness messages are sent.
```

## G08-SALE_SMS-Q028

```yaml
QID: G08-SALE_SMS-Q028
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a line that had already reached the ready state is later reverted, for instance because a readiness
  determination is corrected, an order-wide readiness message already sent on the strength of that line is not
  left standing unqualified; the reversion is recognized as requiring a decision about informing the customer.
WHY_IT_MATTERS: >
  Leaving an inaccurate readiness claim standing with no follow-up misleads a customer who may act on it before
  discovering the correction independently.
DISCONFIRMING_OBSERVATION: >
  A line's readiness is reverted after an order-wide readiness message was sent, and nothing about that
  reversion is recognized as needing customer communication.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send an order-wide readiness message once all lines are ready, then revert one line's readiness, and check
  whether the reversion is flagged for a decision.
```

## G08-SALE_SMS-Q029

```yaml
QID: G08-SALE_SMS-Q029
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An order with a single line behaves identically, with respect to when an order-wide readiness message fires,
  to a multi-line order where the aggregate logic happens to reduce to the same single-line condition, so
  single-line orders are not handled through a separate, potentially inconsistent code path.
WHY_IT_MATTERS: >
  A second, separately maintained path for the common single-line case is more likely to drift out of
  consistency with the aggregate-condition path over time.
DISCONFIRMING_OBSERVATION: >
  A single-line order's readiness message timing differs from what the aggregate, all-lines-ready condition
  would produce if applied to it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Compare the timing of a readiness message on a single-line order against what the all-lines-ready aggregate
  condition would predict for it.
```

## G08-SALE_SMS-Q030

```yaml
QID: G08-SALE_SMS-Q030
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A message stating that a specific price or offer holds only until a stated deadline continues to honour that
  deadline as stated even if the underlying price list or promotional configuration changes before the deadline
  passes.
WHY_IT_MATTERS: >
  Changing the terms underneath a customer who was explicitly told they had until a certain date breaks the
  specific commitment that message made.
DISCONFIRMING_OBSERVATION: >
  A promotional price configuration change takes effect before a customer's stated deadline has passed, altering
  what they would actually be charged if they act within the window they were promised.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Send a message with a stated deadline for a specific price, change the underlying pricing configuration before
  that deadline, and check what price would actually apply if the customer acted within the stated window.
```

## G08-SALE_SMS-Q031

```yaml
QID: G08-SALE_SMS-Q031
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a customer acts to accept a time-limited commitment before its stated deadline, the order reflects the
  terms as stated in the message at the time it was sent, not whatever terms happen to be configured at the
  moment the customer's acceptance is actually processed.
WHY_IT_MATTERS: >
  Applying terms current at processing time rather than the terms actually promised breaks the commitment even
  when the customer accepted within the window they were given.
DISCONFIRMING_OBSERVATION: >
  A customer accepting before the stated deadline receives an order reflecting different terms than what the
  original message actually promised.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Send a time-limited commitment, change underlying terms before the deadline, then process a customer
  acceptance within the original deadline, and compare the resulting order to what was actually promised.
```

## G08-SALE_SMS-Q032

```yaml
QID: G08-SALE_SMS-Q032
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A time-limited commitment message's stated deadline is computed from a single, defined point in time, such as
  when the message was actually sent, not left ambiguous between several plausible reference points such as when
  it was queued, composed, or delivered.
WHY_IT_MATTERS: >
  An ambiguous reference point for the deadline creates room for genuine disagreement about whether a customer
  actually acted in time.
DISCONFIRMING_OBSERVATION: >
  Asked what specific moment a time-limited commitment's deadline is actually measured from, no single, defined
  reference point is documented.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Inspect the configuration or logic governing a time-limited commitment message's deadline calculation to
  identify its defined reference point.
```

## G08-SALE_SMS-Q033

```yaml
QID: G08-SALE_SMS-Q033
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An expired time-limited commitment is distinguishable, in the record of what was sent, from one still within
  its window, so a later question about whether a customer acted in time can be answered by inspecting the
  record rather than only by asking the customer.
WHY_IT_MATTERS: >
  Without that distinction, resolving a dispute over whether a customer missed a deadline depends entirely on
  the customer's own account rather than the business's own record.
DISCONFIRMING_OBSERVATION: >
  The retained record of a sent time-limited commitment message gives no indication of whether its stated
  deadline has since passed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Retrieve the retained record of a time-limited commitment message after its deadline has passed and check
  whether the expiry is indicated.
```

## G08-SALE_SMS-Q034

```yaml
QID: G08-SALE_SMS-Q034
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two customers each receiving a time-limited commitment tied to the same limited underlying allocation, such as
  a capped promotional quantity, do not both have their acceptance honoured beyond what the allocation can
  actually support, purely because both acted within their individually stated deadlines.
WHY_IT_MATTERS: >
  Honouring both commitments when the underlying allocation cannot support both breaks the promise to whichever
  customer is honoured second, even though they did everything the message asked of them.
DISCONFIRMING_OBSERVATION: >
  Two customers act within their respective stated deadlines for a capped allocation, and both are granted the
  commitment despite the combined amount exceeding what the allocation can support.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Send the same capped-allocation time-limited commitment to two customers and have both accept within their
  deadlines, then check whether the combined honoured amount exceeds the allocation.
```

## G08-SALE_SMS-Q035

```yaml
QID: G08-SALE_SMS-Q035
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order created through an automated or bulk import process triggers its confirmation message only after the
  same commitment-content resolution, such as price and promised date, that a manually created order would go
  through, not a simplified or skipped resolution specific to the automated path.
WHY_IT_MATTERS: >
  A simplified resolution specific to bulk-created orders risks sending customers commitments based on
  incomplete or unresolved data that a manual order's process would have caught.
DISCONFIRMING_OBSERVATION: >
  A bulk-imported order's confirmation message sends with a price or date that was never actually resolved
  through the same logic a manually created order's message would have used.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create an order through a bulk import process and a manually equivalent order, and compare the commitment-
  content resolution each goes through before its confirmation message sends.
```

## G08-SALE_SMS-Q036

```yaml
QID: G08-SALE_SMS-Q036
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A batch of orders created through a single automated import does not each trigger their confirmation messages
  in a way that overwhelms the outbound capacity meant for ordinary, individually placed orders, since a large
  batch is a different operational situation than the steady trickle of manual orders the capacity may have been
  sized for.
WHY_IT_MATTERS: >
  A large batch silently competing with ordinary orders for the same limited sending capacity could delay time-
  sensitive messages for customers who placed orders individually and expect prompt confirmation.
DISCONFIRMING_OBSERVATION: >
  A large batch import's confirmation messages measurably delay confirmation messages for unrelated,
  individually placed orders sent around the same time.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a large batch of bulk-imported orders alongside ordinary individual orders and measure whether the
  individual orders' confirmations are delayed.
```

## G08-SALE_SMS-Q037

```yaml
QID: G08-SALE_SMS-Q037
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An error affecting one order within a bulk-imported batch, such as a resolution failure for its commitment
  content, does not silently suppress or corrupt the confirmation messages for the other, unaffected orders in
  the same batch.
WHY_IT_MATTERS: >
  One bad record in a batch should not be allowed to degrade the correctness of messages for every other
  unrelated order swept up in the same operation.
DISCONFIRMING_OBSERVATION: >
  A single order's resolution failure within a bulk import batch causes other orders in that same batch to also
  fail to send, or to send with incorrect content.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Introduce a resolution failure for one order within a bulk import batch and check whether other orders in that
  batch are affected.
```

## G08-SALE_SMS-Q038

```yaml
QID: G08-SALE_SMS-Q038
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An order created through an automated or bulk import process that lacks a valid recipient contact is handled
  by the same defined exception path that a manually created order with the same gap would follow, not silently
  skipped as an accepted characteristic of the automated channel.
WHY_IT_MATTERS: >
  Treating a missing recipient as an accepted quirk of automation, rather than the same exception a manual order
  would raise, hides a real gap that leaves a customer uninformed of their own order.
DISCONFIRMING_OBSERVATION: >
  A bulk-imported order lacking a valid recipient contact produces no exception or flag, while the same gap on a
  manually created order would.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a bulk-imported order and a manually created order each lacking a valid recipient contact, and compare
  how each is handled.
```

## G08-SALE_SMS-Q039

```yaml
QID: G08-SALE_SMS-Q039
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a customer has an on-file negotiated commitment specific to them, such as a guaranteed delivery window
  different from the standard one, an order-triggered message for that customer reflects their specific
  negotiated term rather than the generic default a standard template would otherwise state.
WHY_IT_MATTERS: >
  Sending the generic default to a customer with a specifically negotiated, different term communicates a
  commitment the business did not actually agree to with that customer.
DISCONFIRMING_OBSERVATION: >
  A customer with an on-file negotiated delivery commitment receives a message stating the generic standard
  commitment instead.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a customer-specific negotiated commitment term, trigger the relevant order message for that customer,
  and check which term the message states.
```

## G08-SALE_SMS-Q040

```yaml
QID: G08-SALE_SMS-Q040
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to a customer's negotiated commitment term does not retroactively alter what a previously sent
  message for that customer is understood to have promised.
WHY_IT_MATTERS: >
  Retroactively reinterpreting an already-sent message under a newly negotiated term would misstate what was
  actually promised to the customer at the time.
DISCONFIRMING_OBSERVATION: >
  After a customer's negotiated term changes, a previously sent message's retained record is now interpreted as
  reflecting the new term rather than the one in force when it was sent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a message reflecting a customer's negotiated term, change that term, then re-inspect the earlier
  message's understood meaning.
```

## G08-SALE_SMS-Q041

```yaml
QID: G08-SALE_SMS-Q041
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a customer's negotiated commitment term has an end date after which the standard default applies again,
  an order-triggered message for an order placed after that end date reflects the standard term, not the expired
  negotiated one, without requiring a manual step to remove the expired arrangement.
WHY_IT_MATTERS: >
  Continuing to apply an expired negotiated term by default extends a benefit beyond what was actually agreed,
  at the business's cost, and requiring manual cleanup makes that error likely.
DISCONFIRMING_OBSERVATION: >
  An order placed after a customer's negotiated term has expired still triggers a message stating the expired
  negotiated term rather than the standard default.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Let a customer's negotiated term expire, place a new order for that customer, and check which term the
  triggered message states.
```

## G08-SALE_SMS-Q042

```yaml
QID: G08-SALE_SMS-Q042
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an order originally quoted as a single commitment is later split into more than one separate
  fulfillment, each resulting part triggers its own accurate message reflecting that specific part, rather than
  the original single-commitment message being left as the only communication despite no longer describing how
  the order will actually be fulfilled.
WHY_IT_MATTERS: >
  Leaving the original single-commitment message standing after a split misrepresents how the order will
  actually arrive, which the customer has no way to know unless told.
DISCONFIRMING_OBSERVATION: >
  An order split into two separate fulfillments produces no message reflecting the split, leaving only the
  original single-commitment message on file.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Split an order into two separate fulfillments after an original single-commitment message was sent, and check
  whether any message reflects the split.
```

## G08-SALE_SMS-Q043

```yaml
QID: G08-SALE_SMS-Q043
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The sum of the commitments described across all the messages for an order's separate split fulfillments
  matches what the order as a whole is actually committed to, so splitting an order into parts never causes the
  total communicated commitment to exceed or fall short of the order's own total.
WHY_IT_MATTERS: >
  A mismatch between the sum of split messages and the order's real total means the customer was told about
  more, or less, than what the business actually intends to provide.
DISCONFIRMING_OBSERVATION: >
  The combined quantities or amounts described across an order's split-fulfillment messages do not match the
  order's own total for the same items.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split an order into separate fulfillments, trigger each part's message, and compare the sum of what they
  describe against the order's own total.
```

## G08-SALE_SMS-Q044

```yaml
QID: G08-SALE_SMS-Q044
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Merging two previously separate fulfillments back into one, where that is possible, triggers a message
  reflecting the merged, single commitment, rather than leaving the customer holding two earlier, now-inaccurate
  separate messages with no update.
WHY_IT_MATTERS: >
  Leaving two now-inaccurate separate messages standing after a merge misrepresents how the order will actually
  now be fulfilled.
DISCONFIRMING_OBSERVATION: >
  Two split fulfillments merged back into one produce no message reflecting the merge, leaving the two original
  separate messages as the only communication.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Merge two previously split fulfillments back into one and check whether a message reflecting the merge is
  triggered.
```

## G08-SALE_SMS-Q045

```yaml
QID: G08-SALE_SMS-Q045
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Each split fulfillment's message is independently attributable to the specific lines and quantities it
  actually covers, so a later question about which physical shipment a specific promised item belongs to can be
  answered from the messages themselves.
WHY_IT_MATTERS: >
  Without that attribution, a customer asking which of several messages concerns a specific item they are still
  waiting for cannot be answered from the record alone.
DISCONFIRMING_OBSERVATION: >
  A split fulfillment's message does not specify which lines or quantities it actually covers, making it
  indistinguishable from another split's message for the same order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Split an order into separate fulfillments, trigger each message, and check whether each specifies the
  particular lines or quantities it covers.
```

## G08-SALE_SMS-Q046

```yaml
QID: G08-SALE_SMS-Q046
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two orders submitted by the same customer within a short window, containing substantively the same content,
  each still trigger their own independent confirmation message, since the messaging mechanism is not the layer
  responsible for judging whether the two orders represent one intended purchase or two.
WHY_IT_MATTERS: >
  Having the messaging mechanism silently suppress a second message on its own guess of duplication risks a
  customer never being told about a second order they genuinely intended to place.
DISCONFIRMING_OBSERVATION: >
  A second, genuinely intended order from the same customer within a short window has its confirmation message
  silently suppressed because it resembles an earlier order.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Submit two genuinely separate but substantively similar orders from the same customer in quick succession and
  check whether both trigger their own confirmation message.
```

## G08-SALE_SMS-Q047

```yaml
QID: G08-SALE_SMS-Q047
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a business process elsewhere in the order flow does identify two orders as likely accidental duplicates
  and holds one for review, the confirmation message for the held order is not sent until that review resolves
  it one way or the other, so the customer is not told a commitment exists for an order that may yet be
  cancelled as a duplicate.
WHY_IT_MATTERS: >
  Confirming a commitment to the customer before the duplicate review resolves risks having to walk back a
  message about an order that turns out not to be real.
DISCONFIRMING_OBSERVATION: >
  An order held for duplicate review still has its confirmation message sent before the review is resolved.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have an order flagged and held for duplicate review, and check whether its confirmation message sends before
  the review concludes.
```

## G08-SALE_SMS-Q048

```yaml
QID: G08-SALE_SMS-Q048
MODULE: sale_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a held order is ultimately determined to be a genuine accidental duplicate and is cancelled, no
  confirmation message is sent for it at all, rather than a message having already gone out that must now be
  followed by a separate cancellation notice for an order the customer may not have even known was confirmed.
WHY_IT_MATTERS: >
  Sending a confirmation and then immediately a cancellation for an order the customer did not realize was ever
  separately confirmed is confusing and looks like an operational error.
DISCONFIRMING_OBSERVATION: >
  An order determined to be an accidental duplicate and cancelled had already had its confirmation message sent
  beforehand.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Determine an order to be an accidental duplicate and cancel it, then check whether a confirmation message had
  already been sent for it beforehand.
```

---
## GMVQ Internal QA Checklist

- [x] 48 distinct MVQ records; no padding — every record targets a distinct seam hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`, and no two records share one failure event.
- [x] Bridge Module Rule seam test applied to every question: removing the second capability and using the base order and that capability apart would make the question meaningless. No question restates base-module (`sale`) behavior with the bridge's name attached.
- [x] Mandatory pre-authoring sibling check performed against `G05_STOCK_SMS_GMVQ_MVQ_48_V1.00_DRAFT.md` (48 questions, a different group but named as the required check by this module's own routing brief). `event_sms` and `crm_sms` did not exist on disk at authoring time and could not be checked; per Bridge Module Rule §5 this is recorded as a known gap rather than assumed clear.
- [x] Questions are behavioral and source-neutral; no vendor/product/standard name, technical identifier, or the module's own metadata name appears in question text.
- [x] Seam dimensions represented: timing (Q001-Q002, Q030-Q032, Q047-Q048), ownership (Q003, Q007-Q010, Q013-Q014, Q017-Q019, Q021-Q022, Q024, Q035, Q038-Q039, Q045-Q046), quantity and money (Q004, Q034, Q036, Q043), partiality (Q005, Q025-Q026, Q029), reversal (Q006, Q028), lifecycle mismatch (Q011, Q015, Q020, Q023, Q033, Q040-Q042, Q044), authority (Q012, Q016), ordering (Q027), error asymmetry (Q037).
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
