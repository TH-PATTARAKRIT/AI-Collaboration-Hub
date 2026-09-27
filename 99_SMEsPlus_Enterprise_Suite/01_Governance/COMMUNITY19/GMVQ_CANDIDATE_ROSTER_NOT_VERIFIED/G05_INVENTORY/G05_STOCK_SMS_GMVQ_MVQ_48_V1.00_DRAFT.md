# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / stock_sms Module MVQ Bank

**Document ID:** GMVQ-G05-STOCK_SMS-MVQ48-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `stock_sms`
**Wave:** W2
**Author Cell:** P07 (GMVQ Question Factory — Bridge Module Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose
This bank supplies the module-specific research questions for `stock_sms` — the seam between a
stock movement reaching a given state and an outbound notice sent through the outbound messaging
channel to report it. It is written for a blind two-lane study: Lane A reads reference source,
Lane B observes a running system, and neither sees the other's answers. Question text is
source-neutral throughout, never names the module, and never names the specific outbound
messaging channel itself.

## Control
- `stock_sms` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Every question below passes the
  seam test: if the outbound-notification capability were removed and stock movements ran without
  it, the question would no longer make sense.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` distinct from every other
  question's; no two questions share a disconfirming event.
- No padding: 48 questions test 48 distinct hypotheses spread across a notice surviving a reversal
  or cancellation of its trigger, duplicate firing for one transition, content resolved at trigger
  time versus send time, a recipient no longer related to the document, disclosure beyond the
  recipient's entitlement, delivery failure and whether the business process waits on it, an
  irreversible send outliving a rolled-back transaction, per-tenant sender identity and cost
  attribution, rate limiting turning into missed notices, and the audit record of what was actually
  sent.
- This bank is DRAFT authoring output only. Not approved, not frozen, not verified.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived here.

---

## G05-STOCK_SMS-Q001

```yaml
QID: G05-STOCK_SMS-Q001
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the state that triggered an outbound notice is reversed or cancelled before it is otherwise
  superseded, some mechanism exists that could inform the original recipient the earlier message no
  longer reflects reality.
WHY_IT_MATTERS: >
  A recipient left holding a message describing a transaction that was undone has no way to know
  the business relationship it referred to no longer stands as described.
DISCONFIRMING_OBSERVATION: >
  Reversing the triggering state leaves no mechanism, automatic or manual, that could inform the
  original recipient the earlier message no longer holds.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a notice from a movement reaching a given state, then reverse or cancel that state, and
  check for any mechanism that could reach the original recipient about the change.
```

## G05-STOCK_SMS-Q002

```yaml
QID: G05-STOCK_SMS-Q002
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A notice already triggered but still queued, not yet actually dispatched, can be suppressed by a
  reversal that lands before send time, rather than going out regardless.
WHY_IT_MATTERS: >
  A queued notice is still stoppable in principle; sending it anyway after the underlying state has
  already reversed sends a message that was false from the moment it left.
DISCONFIRMING_OBSERVATION: >
  A notice already queued for a state that is reversed before it is dispatched still goes out
  unchanged.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a notice so that it is queued but not yet sent, reverse the triggering state before
  dispatch, and observe whether the queued notice still goes out.
```

## G05-STOCK_SMS-Q003

```yaml
QID: G05-STOCK_SMS-Q003
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The handling of a reversal that happens after a notice was already delivered is distinguishable
  from the handling of one where the notice was still pending, rather than treating both identically.
WHY_IT_MATTERS: >
  Attempting to recall or resend against an already-delivered message the same way as a still-
  pending one can confuse the recipient with an unexplained second message.
DISCONFIRMING_OBSERVATION: >
  The system treats an already-delivered notice and a still-queued one identically when a reversal
  occurs, with no distinction in how each is handled.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a reversal once against a state whose notice has already been delivered, and once against
  a state whose notice is still queued, and compare the handling.
```

## G05-STOCK_SMS-Q004

```yaml
QID: G05-STOCK_SMS-Q004
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reversal that invalidates an earlier notice leaves a recorded reference connecting the two
  events, rather than the reversal happening with no link back to what notice, if any, it
  affected.
WHY_IT_MATTERS: >
  Without a recorded link, a later reviewer has no way to find which past notices were
  invalidated by which reversal.
DISCONFIRMING_OBSERVATION: >
  A reversal that invalidates an earlier notice leaves no record connecting the two events.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a notice, reverse the state that triggered it, and inspect the record for a link between
  the reversal and the notice it invalidated.
```

## G05-STOCK_SMS-Q005

```yaml
QID: G05-STOCK_SMS-Q005
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When one document goes through trigger, reversal, and re-trigger of the same state within a short
  window, the recipient ends up with a coherent sequence of notices, rather than contradictory
  messages with no way to tell which reflects the current state.
WHY_IT_MATTERS: >
  A recipient holding contradictory messages about the same document with no way to tell which is
  current is worse off than one who received nothing at all.
DISCONFIRMING_OBSERVATION: >
  A rapid trigger-reversal-retrigger sequence produces notices to the recipient with no indication
  of which one reflects the current state.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Drive one document through trigger, reversal, and re-trigger of the same state in quick
  succession, and inspect the sequence of notices the recipient receives.
```

## G05-STOCK_SMS-Q006

```yaml
QID: G05-STOCK_SMS-Q006
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Reversing a state that already produced an outbound notice requires a distinct authority or
  acknowledgement, given its notification consequence, rather than requiring no more than reversing
  a state that produced no notice at all.
WHY_IT_MATTERS: >
  Reversals with an external, customer-facing consequence carry more risk than purely internal ones
  and arguably warrant a higher bar before being allowed.
DISCONFIRMING_OBSERVATION: >
  Reversing a state that already produced an outbound notice requires no different authority or
  acknowledgement than reversing one that produced no notice at all.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempt to reverse a state that already produced a delivered notice, and compare the authority or
  acknowledgement required against reversing a state that produced no notice.
```

## G05-STOCK_SMS-Q007

```yaml
QID: G05-STOCK_SMS-Q007
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A single state transition produces at most one notice for that transition, even if the
  transition is recorded, re-saved, or re-evaluated more than once by whatever watches for it.
WHY_IT_MATTERS: >
  A recipient who receives the same notice twice for one real event is left wondering whether
  something actually happened twice.
DISCONFIRMING_OBSERVATION: >
  Re-saving or re-processing a document already in the triggering state causes a second notice to
  go out for the same transition.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Bring a document into the triggering state, then re-save or re-process it without changing that
  state, and observe whether a second notice goes out.
```

## G05-STOCK_SMS-Q008

```yaml
QID: G05-STOCK_SMS-Q008
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the same transition is reachable through more than one path, such as a direct action and a
  background pass that also lands the document in that state, duplicate triggering across those
  paths is actually prevented.
WHY_IT_MATTERS: >
  Two independent paths that each decide to send with no shared memory of what already went out
  will duplicate notices whenever both paths are exercised for the same event.
DISCONFIRMING_OBSERVATION: >
  Reaching the same state through two different paths produces two separate notices with no
  deduplication between them.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reach the same triggering state once through a direct action and once through whatever
  background pass can also produce it, and check for duplicate notices.
```

## G05-STOCK_SMS-Q009

```yaml
QID: G05-STOCK_SMS-Q009
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two near-simultaneous processes both observing a document cross into the triggering state at
  nearly the same moment are prevented, by a lock or claim, from both independently deciding to
  send.
WHY_IT_MATTERS: >
  A race between two evaluators of the same transition, with nothing serializing the decision, can
  double-send a notice under ordinary operating conditions rather than only in a contrived edge
  case.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous evaluations of the same transition both independently send a notice, with
  nothing serializing the decision.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Force two near-simultaneous evaluations of the same document crossing into the triggering state,
  and observe whether both independently send a notice.
```

## G05-STOCK_SMS-Q010

```yaml
QID: G05-STOCK_SMS-Q010
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document that genuinely re-enters the triggering state as a new, separate business event still
  receives its own notice, rather than being suppressed as a duplicate because deduplication is
  scoped to the state value alone, not the event.
WHY_IT_MATTERS: >
  Deduplication that is too broad silently drops legitimate notices for events that happen to reuse
  the same state value.
DISCONFIRMING_OBSERVATION: >
  A document that genuinely re-enters the triggering state as a new, separate event is suppressed
  as a duplicate because only the state value, not the event, is what is being deduplicated
  against.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cause a document to re-enter the same triggering state as a genuinely new, separate event, and
  observe whether it receives its own notice.
```

## G05-STOCK_SMS-Q011

```yaml
QID: G05-STOCK_SMS-Q011
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a transition ever produces more than one notice, that fact is distinguishable afterward in
  the record from a single correct send, rather than the record showing only that a notice went
  out with no count or history.
WHY_IT_MATTERS: >
  Without a record of how many times a notice actually went out, a duplicate-send incident cannot
  be detected or investigated after the fact.
DISCONFIRMING_OBSERVATION: >
  There is no way, after the fact, to tell from the record whether a given transition produced one
  notice or more than one.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Force a transition to produce more than one notice, and inspect the record afterward for a count
  or history distinguishing that from a single send.
```

## G05-STOCK_SMS-Q012

```yaml
QID: G05-STOCK_SMS-Q012
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The content placed into a notice reflects the document's state at the moment the notice is
  actually composed for sending, not a state captured earlier and reused verbatim if the document
  changed in between.
WHY_IT_MATTERS: >
  A notice describing a state the document no longer holds by the time it is sent tells the
  recipient something that is already wrong.
DISCONFIRMING_OBSERVATION: >
  A change to the document made after the notice was triggered but before it was actually sent has
  no effect on the content that goes out, which still reflects the earlier state.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a notice, change the underlying document before the notice is actually sent, and inspect
  whether the sent content reflects the change.
```

## G05-STOCK_SMS-Q013

```yaml
QID: G05-STOCK_SMS-Q013
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the source document becomes inaccessible or is deleted after triggering but before the notice
  is sent, the send fails safely and visibly, rather than going out with stale or blank content.
WHY_IT_MATTERS: >
  A notice sent with degraded content because its source vanished mid-flight can misinform the
  recipient with no indication anything went wrong.
DISCONFIRMING_OBSERVATION: >
  The notice still sends, with incomplete or stale content, after the source document became
  inaccessible, with no failure surfaced.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a notice, make the source document inaccessible before the notice actually sends, and
  observe the outcome.
```

## G05-STOCK_SMS-Q014

```yaml
QID: G05-STOCK_SMS-Q014
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  There is a defined maximum interval between trigger and actual send beyond which a queued notice
  is treated as too stale to send as-is, requiring re-resolution or cancellation.
WHY_IT_MATTERS: >
  A notice that can sit queued indefinitely and then send with content that no longer matches a
  long-since-changed document carries no real freshness guarantee at all.
DISCONFIRMING_OBSERVATION: >
  There is no staleness threshold or re-resolution step for a notice that sits queued for an
  extended period before actually sending.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Trigger a notice, delay its actual send well beyond an ordinary interval, and check whether any
  staleness threshold or re-resolution applies before it goes out.
```

## G05-STOCK_SMS-Q015

```yaml
QID: G05-STOCK_SMS-Q015
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Every field of a single outgoing notice is resolved against a consistent point in time, rather
  than some fields reflecting the document's state at trigger time and others a later state within
  the same message.
WHY_IT_MATTERS: >
  A message that mixes old and new values internally can describe a state of the document that
  never actually existed.
DISCONFIRMING_OBSERVATION: >
  A single outgoing notice contains some values reflecting the document's state at trigger time and
  others reflecting a later state, with no consistent resolution point across the message.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Change different parts of a document at different points between trigger and send, then inspect
  whether the resulting notice mixes values from different points in time.
```

## G05-STOCK_SMS-Q016

```yaml
QID: G05-STOCK_SMS-Q016
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a notice's content depends on a related record, such as a party's current contact detail or
  status label, that changed between trigger and send, the notice reflects the related record's
  current value rather than one cached from trigger time.
WHY_IT_MATTERS: >
  Using a stale cached value from a related record can put outdated information into a message the
  recipient has every reason to expect is current.
DISCONFIRMING_OBSERVATION: >
  A related record's value used in the notice is taken from a cache captured at trigger time even
  though the related record has since changed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a notice that depends on a related record, change that related record before the notice
  actually sends, and inspect which value the sent notice reflects.
```

## G05-STOCK_SMS-Q017

```yaml
QID: G05-STOCK_SMS-Q017
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The record preserves the actual sent content of a past notice, or a faithful copy of it, so that
  comparing it against what the current template and current data would produce is possible without
  the two being forced to agree merely because both draw on the same template.
WHY_IT_MATTERS: >
  Without a preserved copy of what was actually sent, "what did we tell the customer" can only ever
  be answered by regenerating it from current data, which is not the same question.
DISCONFIRMING_OBSERVATION: >
  The system offers no way to compare a historically sent notice's actual content against what the
  current template and current data would generate today.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Send a notice, later change the underlying data or template, and attempt to compare the notice as
  actually sent against what would be generated now.
```

## G05-STOCK_SMS-Q018

```yaml
QID: G05-STOCK_SMS-Q018
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The recipient contact used for a notice is validated as currently belonging to the party the
  document is actually about at send time, not carried over from an earlier association that may no
  longer hold.
WHY_IT_MATTERS: >
  A notice sent to a contact left over from a superseded association can reach someone who has no
  current relationship to the document at all.
DISCONFIRMING_OBSERVATION: >
  A notice is sent to a contact detail left over from an earlier, now-superseded party association
  on the document, with no check that the association still holds.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Change the party associated with a document after an earlier association had a contact detail
  recorded, trigger a notice, and check which contact detail it uses.
```

## G05-STOCK_SMS-Q019

```yaml
QID: G05-STOCK_SMS-Q019
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the party associated with a document changes after a notice was already triggered but before
  it sends, the recipient updates to match the new party rather than the original, now-wrong
  contact still receiving it.
WHY_IT_MATTERS: >
  A notice sent to the wrong party because the association changed too late to matter can disclose
  the document's content to someone no longer entitled to it.
DISCONFIRMING_OBSERVATION: >
  Reassigning the document's party after triggering has no effect on who actually receives the
  already-triggered notice.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a notice, reassign the document's party before the notice actually sends, and observe who
  receives it.
```

## G05-STOCK_SMS-Q020

```yaml
QID: G05-STOCK_SMS-Q020
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document whose party has never changed resolves its recipient with no extra friction or hold
  introduced by whatever safeguard exists to catch stale associations.
WHY_IT_MATTERS: >
  A safeguard that delays every ordinary, unchanged case degrades routine notices to guard against
  a comparatively rare condition.
DISCONFIRMING_OBSERVATION: >
  A document with a stable, unchanged party still triggers extra validation delay or a hold before
  its notice can send.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Trigger a notice for a document whose party association has never changed, and measure whether
  any extra validation delay or hold applies.
```

## G05-STOCK_SMS-Q021

```yaml
QID: G05-STOCK_SMS-Q021
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system can represent that a contact number's ownership changes over time, independent of
  whatever party record it happens to be stored against, rather than treating the number as a
  permanent, unchanging identifier of its original party.
WHY_IT_MATTERS: >
  A contact number reused for a different party over time can otherwise deliver a document's
  content to whoever currently holds it, not the party it actually concerns.
DISCONFIRMING_OBSERVATION: >
  The system has no way to represent that a contact number's ownership can change over time,
  independent of whatever party record it happens to be stored against.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reassign a contact number from one party to another over time, and check whether the system can
  represent that ownership change independent of any single party record.
```

## G05-STOCK_SMS-Q022

```yaml
QID: G05-STOCK_SMS-Q022
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the same party record and contact number are shared or duplicated across more than one
  company or branch, correcting the contact detail in one context reaches notices subsequently sent
  from the other context.
WHY_IT_MATTERS: >
  A correction that does not propagate leaves one context continuing to send to a contact detail
  the other has already recognised as wrong.
DISCONFIRMING_OBSERVATION: >
  Correcting a contact detail in one company or branch context has no effect on notices subsequently
  sent from another context referencing what is meant to be the same party.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Share the same party record across two company or branch contexts, correct its contact detail in
  one, and send a notice referencing that party from the other.
```

## G05-STOCK_SMS-Q023

```yaml
QID: G05-STOCK_SMS-Q023
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  There is a retained record of which specific contact detail a past notice was actually sent to,
  so a later dispute about who received it can be resolved against the value actually used rather
  than whatever the party record shows now.
WHY_IT_MATTERS: >
  Without a retained value, a dispute about a past notice can only be answered with the party
  record's current contact detail, which may no longer be the one that was actually used.
DISCONFIRMING_OBSERVATION: >
  There is no retained record of the specific contact value a past notice was actually sent to,
  only the current value on the party record.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Send a notice, later change the party's contact detail, and attempt to determine which contact
  value the earlier notice was actually sent to.
```

## G05-STOCK_SMS-Q024

```yaml
QID: G05-STOCK_SMS-Q024
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The content a notice includes is bounded by what its specific recipient is entitled to see, not
  by everything available on the underlying document at the point the content is composed.
WHY_IT_MATTERS: >
  A notice built from the full document with no entitlement filter can disclose detail the
  recipient has no standing right to see.
DISCONFIRMING_OBSERVATION: >
  A notice composed from the full document exposes a detail the named recipient has no standing
  right to see, with nothing filtering it out.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Trigger a notice for a document containing detail the named recipient is not entitled to see, and
  inspect whether that detail appears in the sent content.
```

## G05-STOCK_SMS-Q025

```yaml
QID: G05-STOCK_SMS-Q025
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a document involves more than one party with different entitlements, each party's notice
  content differs according to what they should see, rather than one template being used verbatim
  for every recipient regardless of role.
WHY_IT_MATTERS: >
  A single template sent to every party regardless of role discloses the most-privileged party's
  view to everyone, including parties with no right to it.
DISCONFIRMING_OBSERVATION: >
  Recipients with clearly different entitlements to the document's detail receive identically
  worded notices with the same level of disclosure.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Trigger notices to two parties on the same document with clearly different entitlements, and
  compare the content each receives.
```

## G05-STOCK_SMS-Q026

```yaml
QID: G05-STOCK_SMS-Q026
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A recipient fully entitled to every detail on the document does not have content withheld or
  degraded by an overly broad filtering rule meant for less-trusted recipients.
WHY_IT_MATTERS: >
  Entitlement filtering that is not actually scoped per recipient can withhold information from
  someone who has every right to it, defeating the notice's purpose.
DISCONFIRMING_OBSERVATION: >
  A fully entitled recipient's notice is missing detail they have every right to see, because the
  filtering is not actually scoped to entitlement.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Trigger a notice to a recipient fully entitled to every detail on the document, and inspect
  whether any detail they are entitled to is missing.
```

## G05-STOCK_SMS-Q027

```yaml
QID: G05-STOCK_SMS-Q027
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A later change to a document's sensitivity or classification, after a notice describing it was
  already sent, leaves a record connecting that reclassification to the notices already sent under
  the earlier classification.
WHY_IT_MATTERS: >
  Without that connection, a later reviewer investigating a reclassified document has no way to
  find which past disclosures happened under the earlier, less restrictive rules.
DISCONFIRMING_OBSERVATION: >
  There is no record connecting a later sensitivity reclassification to notices already sent under
  the earlier classification, even for review purposes.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Send a notice describing a document, later reclassify that document's sensitivity, and check for
  a record connecting the reclassification to the earlier notice.
```

## G05-STOCK_SMS-Q028

```yaml
QID: G05-STOCK_SMS-Q028
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A notice about a document that spans more than one company or branch does not disclose the other
  side's internal detail to a recipient who is only entitled to their own side of the transaction.
WHY_IT_MATTERS: >
  Cross-company detail reaching a recipient with no relationship to the other company is a
  disclosure the recipient's own entitlement never covered.
DISCONFIRMING_OBSERVATION: >
  A notice sent to a party on one side of a cross-company transaction includes detail belonging to
  the other company that the recipient has no relationship with.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Trigger a notice for a document spanning two companies, addressed to a party on only one side,
  and inspect whether the other company's internal detail appears.
```

## G05-STOCK_SMS-Q029

```yaml
QID: G05-STOCK_SMS-Q029
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Whether a given sent notice's content stayed within the recipient's entitlement or exceeded it is
  determinable after the fact from the record of what content template and data were used.
WHY_IT_MATTERS: >
  Without that determinability, an over-disclosure that already happened can never be found,
  confirmed, or corrected for after the fact.
DISCONFIRMING_OBSERVATION: >
  There is no way, after sending, to determine whether a given notice's content stayed within the
  recipient's entitlement or exceeded it.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Send a notice, then attempt to determine after the fact, from the record alone, whether its
  content stayed within the recipient's entitlement.
```

## G05-STOCK_SMS-Q030

```yaml
QID: G05-STOCK_SMS-Q030
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A failure to actually deliver a notice does not, by itself, block or delay the underlying business
  transition the notice was reporting on, unless a specific business rule says otherwise.
WHY_IT_MATTERS: >
  Coupling delivery success to the business transition itself means a purely communication-side
  failure can stall real operational work that has nothing to do with messaging.
DISCONFIRMING_OBSERVATION: >
  A delivery failure on the notification side prevents the underlying document from completing or
  advancing its own transition.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Force a delivery failure for a notice tied to a document's transition, and observe whether the
  document's own transition is blocked or delayed by it.
```

## G05-STOCK_SMS-Q031

```yaml
QID: G05-STOCK_SMS-Q031
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A delivery failure is surfaced to a person who can act on it, such as retrying, correcting the
  contact, or escalating, rather than disappearing into a log nobody is expected to read.
WHY_IT_MATTERS: >
  A failure nobody sees leaves the business believing the recipient was informed when they were not.
DISCONFIRMING_OBSERVATION: >
  A delivery failure produces no surfaced notice to any responsible person, only an entry in a
  technical log.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Force a delivery failure for a notice, and check whether it is surfaced to any responsible person
  beyond a technical log entry.
```

## G05-STOCK_SMS-Q032

```yaml
QID: G05-STOCK_SMS-Q032
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A failed notice that is retried has a defined retry limit, after which it is marked as permanently
  failed in a way distinguishable from one still pending retry or one successfully sent.
WHY_IT_MATTERS: >
  A notice retried silently forever, or given up on silently after one attempt, leaves no
  distinguishable state for anyone reviewing whether the recipient was ever actually informed.
DISCONFIRMING_OBSERVATION: >
  A permanently failed notice is left in the same state as one still pending retry, or as one
  successfully sent, with no way to tell which happened.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Force a notice to fail delivery repeatedly until any retry limit is exhausted, and inspect its
  resulting state against a pending and a successfully sent notice.
```

## G05-STOCK_SMS-Q033

```yaml
QID: G05-STOCK_SMS-Q033
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A notice type explicitly configured as non-critical to the business process does not accumulate
  the same escalation handling as one the process genuinely depends on.
WHY_IT_MATTERS: >
  Uniform escalation regardless of configured importance trains responsible people to ignore
  escalations, including the ones that actually matter.
DISCONFIRMING_OBSERVATION: >
  A notice explicitly marked as non-critical triggers the same escalation as one the process
  depends on.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure one notice type as non-critical and another as depended-upon, force both to fail
  delivery, and compare the resulting escalation.
```

## G05-STOCK_SMS-Q034

```yaml
QID: G05-STOCK_SMS-Q034
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A permanently failed notice is linked back to the specific business document or transition it was
  meant to report, findable from that document's own record, rather than sitting only in a general
  delivery log disconnected from it.
WHY_IT_MATTERS: >
  A reviewer checking a specific document for whether its party was ever actually informed needs
  that link; a disconnected delivery log cannot answer the question from the document side.
DISCONFIRMING_OBSERVATION: >
  There is no link from a permanently failed notice back to the specific business document it was
  reporting on, findable from that document's own record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force a notice tied to a specific document to fail permanently, and check whether that document's
  own record links to the failure.
```

## G05-STOCK_SMS-Q035

```yaml
QID: G05-STOCK_SMS-Q035
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Manually marking a failed notice as resolved, without an actual successful send, is distinguishable
  in the record from a genuine delivery confirmation.
WHY_IT_MATTERS: >
  An indistinguishable manual override lets a failed notice be recorded as delivered with no trace
  that the recipient was, in fact, never reached.
DISCONFIRMING_OBSERVATION: >
  Manually clearing a failed notice's status is stored identically to an actual successful delivery
  confirmation, with the override itself invisible.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Force a notice to fail, manually mark it resolved without an actual send, and compare the
  resulting record against a genuine delivery confirmation.
```

## G05-STOCK_SMS-Q036

```yaml
QID: G05-STOCK_SMS-Q036
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once a notice has actually been dispatched to the outbound messaging channel, its irreversibility
  is treated as a real constraint by the surrounding business logic, rather than a later rollback of
  the triggering transaction assuming the message can simply be undone along with it.
WHY_IT_MATTERS: >
  A message already in the recipient's hands cannot be recalled; logic that assumes otherwise
  overstates what a rollback can actually achieve.
DISCONFIRMING_OBSERVATION: >
  Rolling back the triggering transaction is handled as if it also undoes an already-dispatched
  notice, with no acknowledgement that the message itself cannot be recalled.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Dispatch a notice, then roll back the transaction that triggered it, and inspect how the rollback
  is handled with respect to the already-dispatched message.
```

## G05-STOCK_SMS-Q037

```yaml
QID: G05-STOCK_SMS-Q037
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  There is a way to tell, for a given rollback, whether it happened before or after the point past
  which a triggered notice could no longer be stopped.
WHY_IT_MATTERS: >
  Without that distinction, the whole trigger-to-send interval is treated as uniformly reversible
  when part of it is not, understating the real consequence of a late rollback.
DISCONFIRMING_OBSERVATION: >
  The system provides no way to tell, for a given rollback, whether it happened before or after the
  point past which the notice could no longer be stopped.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a notice, roll back its triggering transaction at a known point relative to the actual
  send, and check whether the record reflects which side of that point the rollback fell on.
```

## G05-STOCK_SMS-Q038

```yaml
QID: G05-STOCK_SMS-Q038
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rollback that occurs after an irreversible send leaves an explicit flag that a real recipient
  still holds a message describing a transaction that no longer stands, so a compensating business
  action is at least visible as needed.
WHY_IT_MATTERS: >
  Without that flag, nobody is prompted to follow up with the recipient, and the false message is
  left to stand uncorrected indefinitely.
DISCONFIRMING_OBSERVATION: >
  A rollback after an irreversible send leaves no flag or indicator that a real recipient still
  holds a now-false message.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Dispatch a notice, roll back its triggering transaction afterward, and check for a flag
  indicating the recipient still holds a now-false message.
```

## G05-STOCK_SMS-Q039

```yaml
QID: G05-STOCK_SMS-Q039
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rollback that happens with no notice ever triggered proceeds with no special handling, rather
  than being held up or flagged by the same handling meant for the irreversible-message case.
WHY_IT_MATTERS: >
  Applying the irreversible-message safeguard to every rollback, whether or not a notice was ever in
  play, adds friction to ordinary rollbacks that carry no such risk.
DISCONFIRMING_OBSERVATION: >
  An ordinary rollback with no notice ever triggered is held up or flagged by the same handling
  meant for the irreversible-message case.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Roll back a transaction that never triggered any notice, and observe whether it is held up or
  flagged by the irreversible-message handling.
```

## G05-STOCK_SMS-Q040

```yaml
QID: G05-STOCK_SMS-Q040
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The sender identity a recipient sees on a notice reflects the specific company or branch the
  document actually belongs to, rather than a single shared identity that makes notices from
  different tenants indistinguishable to their recipients.
WHY_IT_MATTERS: >
  A recipient unable to tell which company actually sent a notice cannot verify it against a
  business relationship they recognise.
DISCONFIRMING_OBSERVATION: >
  Notices for documents belonging to different companies or branches all show the same sender
  identity, with no way for a recipient to tell them apart.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Trigger notices for documents belonging to two different companies or branches, and compare the
  sender identity each recipient sees.
```

## G05-STOCK_SMS-Q041

```yaml
QID: G05-STOCK_SMS-Q041
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The cost of sending a notice is attributed to the company or branch whose document actually
  triggered it, rather than landing on whichever tenant owns the shared sending configuration
  regardless of which tenant's business generated the send.
WHY_IT_MATTERS: >
  Cost landing on the wrong tenant misstates each tenant's own operating cost and can subsidise one
  tenant's volume at another's expense.
DISCONFIRMING_OBSERVATION: >
  The cost of a notice triggered by one company's document is attributed to a different company's
  account with no allocation back to the actual trigger.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Trigger a notice from one company's document under a shared sending configuration owned by
  another company, and inspect which company's account absorbs the cost.
```

## G05-STOCK_SMS-Q042

```yaml
QID: G05-STOCK_SMS-Q042
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A tenant with a single, unambiguous sender identity and no shared configuration in play does not
  require resolving a per-tenant sender choice as an extra step before sending.
WHY_IT_MATTERS: >
  Forcing a resolution step with only one possible answer adds latency and complexity for the
  ordinary, single-tenant case with no benefit.
DISCONFIRMING_OBSERVATION: >
  Sending a notice for a tenant with a single, unambiguous sender identity still requires resolving
  a per-tenant choice that has only one possible answer, adding a step with no effect.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Send a notice for a tenant with a single, unambiguous sender identity and no shared configuration,
  and observe whether a per-tenant resolution step still occurs.
```

## G05-STOCK_SMS-Q043

```yaml
QID: G05-STOCK_SMS-Q043
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a tenant's sender identity changes partway through the record's history, past notices remain
  attributed to the sender identity actually in effect when they were sent, rather than history
  being rewritten to show the current identity for everything.
WHY_IT_MATTERS: >
  Rewriting past attribution to the current identity misrepresents what the recipient was actually
  shown at the time the notice was sent.
DISCONFIRMING_OBSERVATION: >
  Changing a tenant's sender identity causes historical notices to display the new identity instead
  of the one actually used at send time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a notice under one sender identity, change the tenant's sender identity afterward, and
  inspect what the historical notice now displays.
```

## G05-STOCK_SMS-Q044

```yaml
QID: G05-STOCK_SMS-Q044
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When outbound volume exceeds a rate limit, the notices that cannot be sent immediately are queued
  and eventually sent or explicitly marked as not sent, rather than being silently dropped with no
  trace.
WHY_IT_MATTERS: >
  A silently dropped notice leaves the business believing a recipient was informed when no message
  was ever sent at all.
DISCONFIRMING_OBSERVATION: >
  A notice that could not be sent immediately because of a rate limit disappears with no queued
  state and no record that it was ever supposed to go out.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Exceed the outbound rate limit so that a notice cannot be sent immediately, and check whether it
  is queued, explicitly marked as not sent, or dropped with no trace.
```

## G05-STOCK_SMS-Q045

```yaml
QID: G05-STOCK_SMS-Q045
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The outbound rate limit is applied per tenant, so one company's high send volume cannot consume
  the sending capacity another company depends on.
WHY_IT_MATTERS: >
  A shared limit with no per-tenant isolation lets one tenant's surge delay or drop another,
  unrelated tenant's routine notices.
DISCONFIRMING_OBSERVATION: >
  One company's high send volume causes another, unrelated company's notices to be delayed or
  dropped by a shared limit with no per-tenant isolation.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Drive one company's send volume high enough to approach the rate limit, and observe whether
  another, unrelated company's notices are affected.
```

## G05-STOCK_SMS-Q046

```yaml
QID: G05-STOCK_SMS-Q046
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Ordinary volume well under the rate limit is never queued or delayed by the limiting mechanism at
  all.
WHY_IT_MATTERS: >
  Throttling that engages even at ordinary volume adds delay to every routine notice for no reason
  tied to actual load.
DISCONFIRMING_OBSERVATION: >
  Notices sent at ordinary, well-under-limit volume are still measurably delayed by the
  rate-limiting mechanism.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Send notices at ordinary volume well under the rate limit, and measure whether the rate-limiting
  mechanism introduces any delay.
```

## G05-STOCK_SMS-Q047

```yaml
QID: G05-STOCK_SMS-Q047
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A notice's stored record identifies which version of its composing template actually produced it,
  distinct from whatever version of the template exists now.
WHY_IT_MATTERS: >
  Without that version reference, a later template edit makes it impossible to tell which version
  actually generated a specific past send.
DISCONFIRMING_OBSERVATION: >
  After a template edit, there is no way to determine which version of the template a previously
  sent notice was actually generated from.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Send a notice from one version of its composing template, edit the template afterward, and
  attempt to determine which version actually produced the earlier send.
```

## G05-STOCK_SMS-Q048

```yaml
QID: G05-STOCK_SMS-Q048
MODULE: stock_sms
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A notice type explicitly configured as not required for the business process to proceed does not
  block or delay that process while its own send status is still pending or unresolved.
WHY_IT_MATTERS: >
  A notice the business explicitly declared non-essential should never be the reason a real
  transaction is held up.
DISCONFIRMING_OBSERVATION: >
  A process waits on the resolution of a notice explicitly configured as not required for it to
  proceed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure a notice type as not required for the business process, leave its send status pending,
  and observe whether the process proceeds regardless.
```

