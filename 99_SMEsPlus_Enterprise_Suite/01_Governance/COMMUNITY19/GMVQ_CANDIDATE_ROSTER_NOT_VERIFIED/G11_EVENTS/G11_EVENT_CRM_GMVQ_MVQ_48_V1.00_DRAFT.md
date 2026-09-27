# SMEsPlus ENTERPRISE SUITE
## GMVQ — G11 EVENTS / event_crm Module MVQ Bank

**Document ID:** GMVQ-G11-EVENT_CRM-MVQ48-V1.00
**Group:** G11 EVENTS
**Module Metadata:** `event_crm`
**Wave:** W2
**Author Cell:** P-E4 (GMVQ Question Factory — Bridge Module Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose
This bank supplies the module-specific research questions for `event_crm` — the seam between an
event registration and the sales opportunity it may generate. It covers the two-way case only:
registration to opportunity. The three-way case, where the registration itself originated from a
commercial order, belongs to a sibling bank and is out of scope here. It is written for a blind
two-lane study: Lane A reads reference source, Lane B observes a running system, and neither sees
the other's answers. Question text is source-neutral throughout and never names the module.

## Control
- `event_crm` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Every question below passes the
  seam test: if the sales-opportunity capability were removed and event registration ran without
  it, the question would no longer make sense.
- Out of scope by design: registration capacity, waiting-list promotion, ticket pricing mechanics,
  and any question that would still make sense with event registration and sales opportunities used
  entirely apart from each other — those belong to the base event bank or to the sibling three-way
  bank, not here.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` distinct from every other
  question's; no two questions share a disconfirming event.
- No padding: 48 questions test 48 distinct hypotheses spread across cancellation and refund of the
  source registration, one person across multiple registrations, opportunity ownership versus event
  ownership, an attendee who is already a known contact, expected value with no commercial signal,
  registration versus attendance as the trigger, personal data and consent, bulk post-event
  generation and its audit trail, an event cancelled after opportunities exist, and cross-company
  routing.
- This bank is DRAFT authoring output only. Not approved, not frozen, not verified.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived here.

---

## G11-EVENT_CRM-Q001

```yaml
QID: G11-EVENT_CRM-Q001
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling the registration that produced an opportunity leaves a recorded, inspectable link
  between the cancellation and whatever happens next to that opportunity, rather than the two
  events becoming unconnected in the record.
WHY_IT_MATTERS: >
  Without that link, nobody reviewing the opportunity later can tell whether its originating
  registration is still valid, which makes the opportunity's own numbers unreliable.
DISCONFIRMING_OBSERVATION: >
  The registration is cancelled and the opportunity it produced shows no trace, anywhere,
  connecting the two events.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a registration that generates an opportunity, cancel the registration, and check whether
  any record connects the cancellation to the opportunity's subsequent state.
```

## G11-EVENT_CRM-Q002

```yaml
QID: G11-EVENT_CRM-Q002
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A refund of the registration's payment does not, by itself, cause the opportunity it originated
  from to be silently deleted or hidden from the pipeline it is otherwise visible in.
WHY_IT_MATTERS: >
  A silently vanished opportunity understates the sales pipeline and hides the fact that a
  commercial signal existed at all, even one that was later refunded.
DISCONFIRMING_OBSERVATION: >
  Refunding the registration's payment causes the opportunity to disappear from the pipeline view
  without an explicit close or cancel action having been taken on it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate an opportunity from a paid registration, refund the registration's payment, and check
  whether the opportunity remains visible in the pipeline.
```

## G11-EVENT_CRM-Q003

```yaml
QID: G11-EVENT_CRM-Q003
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether a cancelled registration's opportunity is automatically moved to a lost or cancelled
  outcome, or is left open and unaffected, follows one explicit, consistently applied rule rather
  than varying by circumstance.
WHY_IT_MATTERS: >
  An inconsistent rule means two identical cancellations can leave the sales team with two
  different pictures of the same kind of event, undermining any reporting built on the outcome.
DISCONFIRMING_OBSERVATION: >
  Two registrations cancelled under the same circumstances leave their respective opportunities in
  different outcome states with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Cancel two comparable registrations that each produced an opportunity, under the same
  configuration, and compare the resulting opportunity outcomes.
```

## G11-EVENT_CRM-Q004

```yaml
QID: G11-EVENT_CRM-Q004
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A registration that is cancelled and then re-created for the same person and the same event is
  distinguishable afterward, in whatever opportunity trail exists, from a registration that was
  never cancelled at all.
WHY_IT_MATTERS: >
  Without that distinction, a sales reviewer cannot tell a straightforward booking from one that
  was cancelled and retried, which can misstate how firm the underlying interest actually is.
DISCONFIRMING_OBSERVATION: >
  A cancelled-then-recreated registration's opportunity trail is identical, field for field, to a
  registration that was never cancelled.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a registration, recreate an equivalent one for the same person and event, and compare the
  resulting opportunity trail against one from a registration with no cancellation history.
```

## G11-EVENT_CRM-Q005

```yaml
QID: G11-EVENT_CRM-Q005
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a registration is cancelled after the opportunity it produced has already moved further
  along the pipeline than its initial stage, the opportunity's disposition afterward is an explicit
  decision rather than an unresolved inconsistency between an advanced opportunity and a cancelled
  source.
WHY_IT_MATTERS: >
  An opportunity that has visibly advanced, sitting on a source that no longer exists, misrepresents
  the state of the deal to whoever is managing it next.
DISCONFIRMING_OBSERVATION: >
  An opportunity that has already advanced past its initial stage is left with no explicit
  resolution after its source registration is cancelled, and nothing flags the inconsistency.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Advance an opportunity generated from a registration past its initial stage, cancel the source
  registration, and check whether the opportunity's disposition is explicitly addressed.
```

## G11-EVENT_CRM-Q006

```yaml
QID: G11-EVENT_CRM-Q006
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  One person registering for two different events produces two separate opportunities, or an
  explicit rule determines when they are combined into one, rather than an unpredictable mix of the
  two outcomes.
WHY_IT_MATTERS: >
  Sales handling depends on knowing whether one deal or two is in play; an unpredictable mix means
  the pipeline count itself cannot be trusted.
DISCONFIRMING_OBSERVATION: >
  The same person registering for two different events sometimes yields one opportunity and
  sometimes two, with no configuration or rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Register the same person for two distinct events under identical configuration and observe how
  many opportunities result, repeating to check for consistency.
```

## G11-EVENT_CRM-Q007

```yaml
QID: G11-EVENT_CRM-Q007
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  One person registering twice for the same event does not automatically produce two independent
  opportunities for what is, commercially, the same seat.
WHY_IT_MATTERS: >
  Two independent opportunities for one seat overstates the pipeline and can lead two different
  salespeople to separately pursue the same person for the same event.
DISCONFIRMING_OBSERVATION: >
  A single person's duplicate registration for one event produces two opportunities with no link
  or merge between them.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Register the same person twice for the same event and check whether one or two opportunities
  result, and whether any link exists between them if two.
```

## G11-EVENT_CRM-Q008

```yaml
QID: G11-EVENT_CRM-Q008
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether two opportunities arising from one person's registrations to two different events are
  ever automatically linked or rolled up under that person is a deliberate, documented behavior
  rather than an incidental side effect.
WHY_IT_MATTERS: >
  An accidental rollup could merge two genuinely separate deals, while an accidental failure to
  link them could hide a pattern a salesperson would want to see.
DISCONFIRMING_OBSERVATION: >
  Opportunities from the same person's separate event registrations are found linked or rolled up
  with no rule or configuration governing when that happens.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Generate opportunities from the same person's registrations to two different events and check
  whether any linkage exists and whether it is governed by an explicit rule.
```

## G11-EVENT_CRM-Q009

```yaml
QID: G11-EVENT_CRM-Q009
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A second registration's resulting commercial signal does not silently overwrite fields on a
  still-open opportunity that came from a first, unrelated registration for a different event.
WHY_IT_MATTERS: >
  Overwriting an unrelated open opportunity's data destroys the salesperson's existing work on that
  separate deal without any warning.
DISCONFIRMING_OBSERVATION: >
  Creating a second registration for a different event silently changes field values on an
  already-open, unrelated opportunity from an earlier registration.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an open opportunity from one registration, then create a second, unrelated registration
  for a different event by the same person, and check whether the first opportunity's fields
  changed.
```

## G11-EVENT_CRM-Q010

```yaml
QID: G11-EVENT_CRM-Q010
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If opportunities from the same person across multiple events are ever consolidated into one, the
  consolidated record retains a trace of which original registrations fed into it.
WHY_IT_MATTERS: >
  Without that trace, a consolidated opportunity cannot be unwound or audited back to the
  individual commercial signals that produced it.
DISCONFIRMING_OBSERVATION: >
  A consolidated opportunity exists with no retrievable trace of which original registrations
  contributed to it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger whatever consolidation behavior exists for one person's multiple registrations, then
  attempt to trace the consolidated opportunity back to its contributing registrations.
```

## G11-EVENT_CRM-Q011

```yaml
QID: G11-EVENT_CRM-Q011
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two registrations submitted by the same person within a short window against two different
  events do not race into a state where only one of the two opportunities actually gets created.
WHY_IT_MATTERS: >
  A lost opportunity from a race condition is invisible until a salesperson notices a deal that
  should exist does not, by which point the commercial moment may have passed.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous registrations by the same person for two different events produce only one
  opportunity where two were expected.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Submit two registrations for the same person against two different events in close succession
  and verify both expected opportunities are created.
```

## G11-EVENT_CRM-Q012

```yaml
QID: G11-EVENT_CRM-Q012
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The salesperson or team assigned to a newly generated opportunity is determined by an explicit,
  inspectable rule rather than an unexplained default.
WHY_IT_MATTERS: >
  An opaque assignment rule leaves nobody able to say why a given opportunity landed with a given
  salesperson, which undermines accountability for following it up.
DISCONFIRMING_OBSERVATION: >
  A newly generated opportunity's assigned owner cannot be traced back to any inspectable rule or
  configuration.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Generate an opportunity from a registration and attempt to trace its assigned owner back to the
  rule or configuration that produced that assignment.
```

## G11-EVENT_CRM-Q013

```yaml
QID: G11-EVENT_CRM-Q013
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the event's own responsible organizer and the opportunity's assigned owner turn out to be
  different people, that difference is an intended, visible outcome rather than an unnoticed
  mismatch nobody decided on.
WHY_IT_MATTERS: >
  An unnoticed mismatch could mean the wrong person is following up a sales conversation nobody
  informed them was theirs.
DISCONFIRMING_OBSERVATION: >
  The event organizer and the opportunity owner differ with no visible indication that the
  difference was an intended assignment outcome.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Generate an opportunity where the event organizer and the natural opportunity owner would differ,
  and check whether that outcome is visibly explained.
```

## G11-EVENT_CRM-Q014

```yaml
QID: G11-EVENT_CRM-Q014
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing the event's responsible organizer after registrations have already produced
  opportunities does not retroactively reassign those already-existing opportunities.
WHY_IT_MATTERS: >
  Retroactive reassignment could silently move an active deal to a different salesperson mid-
  conversation with no notice to either party.
DISCONFIRMING_OBSERVATION: >
  Changing the event's organizer causes already-existing opportunities from earlier registrations
  to be reassigned without a separate, explicit action.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate an opportunity from a registration, change the event's responsible organizer, and check
  whether the existing opportunity's ownership changed as a result.
```

## G11-EVENT_CRM-Q015

```yaml
QID: G11-EVENT_CRM-Q015
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The permission required to reassign an opportunity that originated from a registration is the
  same permission that governs reassigning any other opportunity, not a separate, weaker or
  stronger rule tied specifically to its origin.
WHY_IT_MATTERS: >
  A separate hidden rule for registration-sourced opportunities creates a permission gap that could
  let someone reassign deals they should not be able to touch, or block someone who should.
DISCONFIRMING_OBSERVATION: >
  Reassigning an opportunity that originated from a registration is possible, or blocked, for a
  person whose permission would give the opposite result on an opportunity created any other way.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare the permission required to reassign a registration-sourced opportunity against the
  permission required to reassign an otherwise identical opportunity created through a different
  path.
```

## G11-EVENT_CRM-Q016

```yaml
QID: G11-EVENT_CRM-Q016
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An opportunity's assigned sales team can legitimately differ from the event's own company or
  department without the assignment being blocked or silently overridden to match.
WHY_IT_MATTERS: >
  Forcing the two to match would prevent a legitimate cross-team handoff that the business may
  specifically want, such as a marketing-run event feeding a separate sales team.
DISCONFIRMING_OBSERVATION: >
  Assigning an opportunity to a team different from the event's own company or department is
  blocked, or is silently reset to match, with no configuration allowing the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Generate an opportunity from an event run by one department and attempt to assign it to a sales
  team belonging to a different one.
```

## G11-EVENT_CRM-Q017

```yaml
QID: G11-EVENT_CRM-Q017
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Organizing or running an event does not, by itself, grant standing access to the commercial
  detail of the opportunities that event produced, absent a separate, explicit permission grant.
WHY_IT_MATTERS: >
  Automatic access would let anyone who can organize an event see sales pipeline detail they may
  have no business reason to see.
DISCONFIRMING_OBSERVATION: >
  A person able to organize or edit an event can see the commercial detail of opportunities it
  produced with no separate permission having been granted for that access.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a person permission to organize an event only, generate opportunities from its
  registrations, and check whether that person can view the opportunities' commercial detail.
```

## G11-EVENT_CRM-Q018

```yaml
QID: G11-EVENT_CRM-Q018
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An attendee who is already a known contact with an existing open opportunity does not
  automatically receive a second, fully independent opportunity with no distinguishable signal that
  a possible duplicate exists.
WHY_IT_MATTERS: >
  An unflagged duplicate means two salespeople could unknowingly pursue the same contact for what
  may be the same underlying interest.
DISCONFIRMING_OBSERVATION: >
  A registration from a contact with an existing open opportunity produces a second, fully
  independent opportunity with no signal anywhere that a possible duplicate exists.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Register a contact who already has an open opportunity for an event, and check whether the new
  opportunity carries any signal connecting it to the existing one.
```

## G11-EVENT_CRM-Q019

```yaml
QID: G11-EVENT_CRM-Q019
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a new registration's commercial signal is merged into an existing open opportunity or
  always produces a new one is a single, consistently applied rule, not one that varies
  unpredictably by registration.
WHY_IT_MATTERS: >
  An inconsistent merge rule means the sales pipeline's opportunity count has no stable meaning
  across otherwise similar situations.
DISCONFIRMING_OBSERVATION: >
  Two comparable registrations from contacts with existing open opportunities are handled
  differently, one merged and one not, with no configuration difference explaining why.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Register two comparable contacts who each already have an open opportunity, under identical
  configuration, and compare whether their new registrations are merged or kept separate.
```

## G11-EVENT_CRM-Q020

```yaml
QID: G11-EVENT_CRM-Q020
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two different people who happen to share one identifying contact detail, such as a shared phone
  number or email address, are not silently collapsed into a single shared opportunity.
WHY_IT_MATTERS: >
  Collapsing two different people into one opportunity misattributes one person's registration or
  interest to somebody else entirely.
DISCONFIRMING_OBSERVATION: >
  Two distinct people sharing one contact detail have their separate registrations combined into a
  single opportunity as though they were one person.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Register two distinct people who share one identifying contact detail for the same or different
  events, and check whether they are treated as one contact for opportunity purposes.
```

## G11-EVENT_CRM-Q021

```yaml
QID: G11-EVENT_CRM-Q021
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A merge or link decision between a new registration's signal and an existing opportunity, once
  made, is inspectable afterward — which existing opportunity absorbed the new signal, and on what
  basis.
WHY_IT_MATTERS: >
  An unexplainable merge decision cannot be reviewed or challenged if it later turns out to have
  combined things that should have stayed separate.
DISCONFIRMING_OBSERVATION: >
  A registration is found to have been merged into an existing opportunity, but no record shows
  which opportunity absorbed it or why.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a merge between a new registration's signal and an existing opportunity, then attempt to
  determine which opportunity absorbed it and on what basis.
```

## G11-EVENT_CRM-Q022

```yaml
QID: G11-EVENT_CRM-Q022
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Matching an attendee to an existing contact record for opportunity purposes uses a defined
  identity rule, rather than an ad hoc match that could reasonably attach the registration to the
  wrong person.
WHY_IT_MATTERS: >
  An ad hoc match risks attaching a stranger's registration to an existing contact's history,
  corrupting both records' commercial picture.
DISCONFIRMING_OBSERVATION: >
  An attendee is matched to an existing contact record by criteria too weak to reliably distinguish
  that contact from a different person with similar details.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Register an attendee whose identifying details closely but not exactly resemble an existing
  contact, and check what identity rule governs whether they are matched.
```

## G11-EVENT_CRM-Q023

```yaml
QID: G11-EVENT_CRM-Q023
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A registration for an event with no listed price is not automatically assigned a nonzero
  expected monetary value in the opportunity it produces.
WHY_IT_MATTERS: >
  An invented monetary value on a free registration overstates the pipeline's real commercial worth
  to anyone relying on those figures.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated from a free event's registration carries a nonzero expected value with
  no commercial basis for that number.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate an opportunity from a registration to a free event and check the expected value assigned
  to it.
```

## G11-EVENT_CRM-Q024

```yaml
QID: G11-EVENT_CRM-Q024
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an expected value is assigned to an opportunity from registration data, the source of that
  number is inspectable rather than an opaque default nobody can trace.
WHY_IT_MATTERS: >
  An untraceable value cannot be trusted for forecasting, since nobody can confirm what it was
  actually derived from.
DISCONFIRMING_OBSERVATION: >
  An opportunity's expected value cannot be traced back to any specific registration data or rule
  that produced it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate an opportunity carrying a nonzero expected value from a registration and attempt to
  trace that value back to its source.
```

## G11-EVENT_CRM-Q025

```yaml
QID: G11-EVENT_CRM-Q025
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to the event's own price after an opportunity has already been created from an earlier
  registration does not silently retroactively alter that opportunity's already-set expected value.
WHY_IT_MATTERS: >
  A silently shifting value undermines any pipeline forecast taken at a point in time, since the
  same opportunity would report different figures at different times for no new reason.
DISCONFIRMING_OBSERVATION: >
  Changing the event's price after an opportunity was created causes that already-existing
  opportunity's expected value to change without any explicit action on the opportunity itself.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an opportunity from a registration to an event, change the event's price, and check
  whether the existing opportunity's expected value changed.
```

## G11-EVENT_CRM-Q026

```yaml
QID: G11-EVENT_CRM-Q026
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an opportunity is created at all for a registration carrying zero commercial signal is a
  deliberate, configurable decision rather than an accidental byproduct of the same path used for
  paid registrations.
WHY_IT_MATTERS: >
  An accidental opportunity for a registration with no commercial signal clutters the pipeline with
  deals that were never really deals.
DISCONFIRMING_OBSERVATION: >
  An opportunity is created for a registration carrying zero commercial signal with no configuration
  that governs whether that should happen.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure the opportunity-generation behavior for registrations with no commercial signal and
  verify the configured choice is actually respected.
```

## G11-EVENT_CRM-Q027

```yaml
QID: G11-EVENT_CRM-Q027
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two ticket types for the same event carrying different prices, both feeding the same
  opportunity-generation path, produce distinguishably different expected values rather than one
  flat default applied to both.
WHY_IT_MATTERS: >
  A flat default across differently priced ticket types makes the resulting pipeline figures
  meaningless as a measure of commercial size.
DISCONFIRMING_OBSERVATION: >
  Registrations under two differently priced ticket types for the same event produce opportunities
  with identical expected values.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Register attendees under two differently priced ticket types for the same event and compare the
  expected values of the resulting opportunities.
```

## G11-EVENT_CRM-Q028

```yaml
QID: G11-EVENT_CRM-Q028
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an opportunity is generated at the moment of registration or only once attendance is
  actually recorded is an explicit, consistently applied configuration choice, not an unpredictable
  one.
WHY_IT_MATTERS: >
  An unpredictable trigger point means the sales team cannot know when to expect a new opportunity
  to appear, undermining timely follow-up.
DISCONFIRMING_OBSERVATION: >
  Two comparable registrations under the same configuration produce opportunities at different
  trigger points, one at registration and one at attendance, with no explanation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure the trigger point for opportunity generation and verify two comparable registrations
  under that configuration both trigger at the same point.
```

## G11-EVENT_CRM-Q029

```yaml
QID: G11-EVENT_CRM-Q029
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A person who registered but is later marked a no-show does not have their already-created
  opportunity silently disappear, when the configured trigger point was registration rather than
  attendance.
WHY_IT_MATTERS: >
  A vanished opportunity for a real registrant hides genuine commercial interest just because that
  person did not physically show up.
DISCONFIRMING_OBSERVATION: >
  Marking a registered attendee as a no-show causes their already-existing, registration-triggered
  opportunity to disappear from the pipeline.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure registration as the trigger, generate an opportunity, mark that attendee as a no-show,
  and check whether the opportunity remains.
```

## G11-EVENT_CRM-Q030

```yaml
QID: G11-EVENT_CRM-Q030
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A person who attends without any prior registration on record is handled by a defined, deliberate
  rule for whether an opportunity is created for them at all.
WHY_IT_MATTERS: >
  Without a defined rule, walk-in attendees either always slip past the sales pipeline or are
  handled inconsistently from one event to the next.
DISCONFIRMING_OBSERVATION: >
  A walk-in attendee with no prior registration sometimes produces an opportunity and sometimes
  does not, with no rule explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record attendance for a person with no prior registration and check whether opportunity
  generation for that case follows a defined, consistent rule.
```

## G11-EVENT_CRM-Q031

```yaml
QID: G11-EVENT_CRM-Q031
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When attendance is the configured trigger, marking attendance after the event's own scheduled end
  date still produces the expected opportunity rather than silently failing because the event is
  considered closed.
WHY_IT_MATTERS: >
  A late attendance correction that fails to trigger an opportunity loses a genuine commercial
  signal simply because of when the data entry happened.
DISCONFIRMING_OBSERVATION: >
  Marking attendance after the event's scheduled end date fails to produce an opportunity that an
  equivalent on-time attendance record would have produced.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure attendance as the trigger, mark an attendee's attendance after the event's scheduled
  end date, and check whether the expected opportunity is still generated.
```

## G11-EVENT_CRM-Q032

```yaml
QID: G11-EVENT_CRM-Q032
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A registration later corrected from attended to not-attended does not leave an opportunity
  already created from that attendance as the only surviving record of an event participation that,
  per the corrected data, did not occur.
WHY_IT_MATTERS: >
  An uncorrected opportunity misrepresents what actually happened at the event to anyone relying on
  it after the correction.
DISCONFIRMING_OBSERVATION: >
  Correcting an attendance record from attended to not-attended leaves the already-created
  opportunity unchanged and unflagged, with no indication the underlying attendance was reversed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate an opportunity from a recorded attendance, correct that attendance record to
  not-attended, and check whether the opportunity reflects or flags the correction.
```

## G11-EVENT_CRM-Q033

```yaml
QID: G11-EVENT_CRM-Q033
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The attendee's personal contact information carried into the resulting opportunity is limited to
  what the attendee's registration consented to being used for commercial contact, not the full
  detail captured for event logistics.
WHY_IT_MATTERS: >
  Carrying logistics-only data into a sales channel the attendee never consented to exceeds what
  they agreed to when they registered.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated from a registration contains personal contact detail the attendee's
  registration only consented to for event logistics, not commercial contact.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Register an attendee who consents only to logistics use of their data, generate the resulting
  opportunity, and check what personal detail it actually carries.
```

## G11-EVENT_CRM-Q034

```yaml
QID: G11-EVENT_CRM-Q034
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Withdrawing consent for commercial contact after registering does not leave an already-created
  opportunity as an untouched channel that ignores the withdrawal.
WHY_IT_MATTERS: >
  An opportunity that keeps being acted on after consent is withdrawn continues a form of contact
  the person explicitly said they no longer agree to.
DISCONFIRMING_OBSERVATION: >
  An attendee withdraws consent for commercial contact and the already-existing opportunity remains
  fully active with no flag or restriction reflecting the withdrawal.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Generate an opportunity from a registration, withdraw the attendee's consent for commercial
  contact, and check whether the opportunity reflects that withdrawal.
```

## G11-EVENT_CRM-Q035

```yaml
QID: G11-EVENT_CRM-Q035
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An attendee who explicitly declined commercial contact at the point of registration does not have
  an opportunity generated for them through the same automatic path used for attendees who
  consented.
WHY_IT_MATTERS: >
  Generating an opportunity anyway directly contradicts a choice the attendee explicitly made at
  the moment they registered.
DISCONFIRMING_OBSERVATION: >
  An attendee who explicitly declined commercial contact at registration has an opportunity
  generated for them regardless.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Register an attendee who explicitly declines commercial contact and check whether an opportunity
  is generated for them regardless.
```

## G11-EVENT_CRM-Q036

```yaml
QID: G11-EVENT_CRM-Q036
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The recorded basis for why a given attendee's data was permitted to flow into the sales pipeline
  is retrievable after the fact, rather than merely assumed from the existence of the opportunity
  itself.
WHY_IT_MATTERS: >
  Without a retrievable basis, nobody can answer a later question about why that person's data
  ended up in a sales channel at all.
DISCONFIRMING_OBSERVATION: >
  An opportunity exists carrying an attendee's personal data with no retrievable record of the
  basis on which that flow was permitted.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate an opportunity from a registration and attempt to retrieve the recorded basis for why
  that attendee's data was permitted to flow into it.
```

## G11-EVENT_CRM-Q037

```yaml
QID: G11-EVENT_CRM-Q037
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When opportunities are raised in bulk after an event concludes, each created opportunity retains
  a traceable link back to the specific registration that produced it.
WHY_IT_MATTERS: >
  Without that link, a bulk-generated opportunity cannot be checked against the registration data
  it is supposed to represent.
DISCONFIRMING_OBSERVATION: >
  A bulk post-event opportunity-generation pass produces at least one opportunity with no traceable
  link to the registration that produced it.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Run a bulk opportunity-generation pass over a finished event's registrations and check whether
  each resulting opportunity traces back to its source registration.
```

## G11-EVENT_CRM-Q038

```yaml
QID: G11-EVENT_CRM-Q038
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Running the same bulk opportunity-generation pass twice over the same finished event does not
  produce a second, duplicate opportunity for a registration the first pass already processed.
WHY_IT_MATTERS: >
  A duplicate opportunity from a re-run pass doubles the apparent pipeline for the same underlying
  registrations without any new commercial signal.
DISCONFIRMING_OBSERVATION: >
  Running the bulk generation pass a second time over the same event produces a duplicate
  opportunity for a registration the first run already processed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Run the bulk opportunity-generation pass over a finished event, then run it again over the same
  event, and check for duplicate opportunities against already-processed registrations.
```

## G11-EVENT_CRM-Q039

```yaml
QID: G11-EVENT_CRM-Q039
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a bulk opportunity-generation pass is interrupted partway through, the registrations it
  already processed and the registrations still pending are distinguishable afterward, rather than
  that boundary being lost.
WHY_IT_MATTERS: >
  A lost boundary means nobody can safely resume or re-run the pass without risking either
  duplicates or registrations that never get an opportunity at all.
DISCONFIRMING_OBSERVATION: >
  After an interrupted bulk generation pass, there is no way to determine which registrations were
  already processed and which were not.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Interrupt a bulk opportunity-generation pass partway through and attempt to determine which
  registrations were processed before the interruption.
```

## G11-EVENT_CRM-Q040

```yaml
QID: G11-EVENT_CRM-Q040
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The person or process that triggered a bulk opportunity-generation run is identifiable in the
  audit trail, not inferred only from the resulting opportunities themselves.
WHY_IT_MATTERS: >
  Without an identifiable trigger, a bulk run that produces a bad batch of opportunities cannot be
  traced back to who or what initiated it.
DISCONFIRMING_OBSERVATION: >
  A completed bulk opportunity-generation run leaves no record of who or what actually triggered
  it.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Trigger a bulk opportunity-generation run and check whether the audit trail identifies who or
  what initiated it.
```

## G11-EVENT_CRM-Q041

```yaml
QID: G11-EVENT_CRM-Q041
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling an event after opportunities have already been generated from its registrations does
  not leave those opportunities in a state indistinguishable from opportunities tied to a
  still-active event.
WHY_IT_MATTERS: >
  An indistinguishable state means a salesperson could keep pursuing a deal tied to an event that
  no longer exists, without any warning that the underlying event was cancelled.
DISCONFIRMING_OBSERVATION: >
  After the source event is cancelled, its already-generated opportunities show nothing
  distinguishing them from opportunities tied to a still-active event.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate opportunities from an event's registrations, cancel the event, and check whether the
  opportunities show any distinguishable indication of the cancellation.
```

## G11-EVENT_CRM-Q042

```yaml
QID: G11-EVENT_CRM-Q042
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an event does not automatically delete the opportunities already created from its
  registrations in a way that destroys the record of the commercial activity that already took
  place.
WHY_IT_MATTERS: >
  Deleting the record erases evidence of real commercial interest that existed regardless of what
  later happened to the event.
DISCONFIRMING_OBSERVATION: >
  Cancelling the event deletes the opportunities already generated from its registrations, leaving
  no retrievable record of them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate opportunities from an event's registrations, cancel the event, and check whether the
  opportunities remain retrievable afterward.
```

## G11-EVENT_CRM-Q043

```yaml
QID: G11-EVENT_CRM-Q043
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reinstating a previously cancelled event, where that is possible at all, does not automatically
  restore or reactivate opportunities that were explicitly closed out because of the cancellation.
WHY_IT_MATTERS: >
  Automatically resurrecting a deliberately closed deal could hand a salesperson an opportunity
  they had already been told, correctly, was over.
DISCONFIRMING_OBSERVATION: >
  Reinstating a cancelled event automatically reopens opportunities that had been explicitly closed
  as a result of the cancellation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel an event, explicitly close the opportunities tied to it, reinstate the event, and check
  whether the closed opportunities reopen automatically.
```

## G11-EVENT_CRM-Q044

```yaml
QID: G11-EVENT_CRM-Q044
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Cancelling an event forces an explicit decision about its already-created opportunities, rather
  than proceeding as an action entirely independent of whatever opportunities already exist.
WHY_IT_MATTERS: >
  Treating the two as fully independent leaves a gap where nobody is ever prompted to decide what a
  cancellation should mean for the commercial pipeline it already produced.
DISCONFIRMING_OBSERVATION: >
  Cancelling an event with existing opportunities completes with no decision point, prompt, or rule
  addressing what happens to those opportunities.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Cancel an event that already has opportunities generated from its registrations and observe
  whether the cancellation process addresses those opportunities in any way.
```

## G11-EVENT_CRM-Q045

```yaml
QID: G11-EVENT_CRM-Q045
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An opportunity generated from a registration to an event owned by one company is not, by default,
  assigned into a different company's sales pipeline without an explicit routing rule permitting
  that.
WHY_IT_MATTERS: >
  An unintended cross-company assignment exposes one company's commercial activity to a separate
  company's sales organization with no deliberate decision behind it.
DISCONFIRMING_OBSERVATION: >
  An opportunity from an event owned by one company lands in a different company's pipeline with no
  routing rule explaining the assignment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Generate an opportunity from a registration to an event owned by one company and verify which
  company's pipeline it is assigned to and why.
```

## G11-EVENT_CRM-Q046

```yaml
QID: G11-EVENT_CRM-Q046
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A person registering for an event hosted by a company other than the one that otherwise holds
  their existing contact record has the resulting opportunity's company assignment resolved by an
  explicit rule, not left ambiguous.
WHY_IT_MATTERS: >
  An ambiguous assignment could leave the opportunity effectively orphaned between two companies'
  pipelines, owned fully by neither.
DISCONFIRMING_OBSERVATION: >
  A registration where the event's company and the attendee's existing contact company differ
  produces an opportunity with no clear, rule-based company assignment.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Register a person, whose existing contact record belongs to one company, for an event hosted by a
  different company, and check how the resulting opportunity's company assignment is resolved.
```

## G11-EVENT_CRM-Q047

```yaml
QID: G11-EVENT_CRM-Q047
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Cross-company opportunity routing, where it exists, does not expose the underlying registration's
  attendee data to sales users of the receiving company beyond what the routing rule itself
  intends.
WHY_IT_MATTERS: >
  Excess exposure beyond the routing rule's intent hands one company's sales staff personal data
  about an attendee that the routing decision never meant to share with them.
DISCONFIRMING_OBSERVATION: >
  A cross-company-routed opportunity exposes attendee data to the receiving company's sales users
  beyond what the routing rule intends to share.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Trigger cross-company opportunity routing and check exactly what attendee data becomes visible to
  the receiving company's sales users.
```

## G11-EVENT_CRM-Q048

```yaml
QID: G11-EVENT_CRM-Q048
MODULE: event_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An attempted cross-company routing outcome that would violate the intended company boundary, such
  as an opportunity landing where the source event's company has no relationship at all with the
  receiving company, is something the design can detect or prevent, rather than something it
  silently allows.
WHY_IT_MATTERS: >
  A silent boundary violation could scatter one company's commercial activity to an unrelated
  company with nothing in the system flagging that the boundary was ever crossed incorrectly.
DISCONFIRMING_OBSERVATION: >
  An opportunity is found routed to a company with no defined relationship to the source event's
  company, with nothing in the system having detected or blocked that outcome.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Attempt to produce a cross-company routing outcome where the receiving company has no defined
  relationship with the source event's company, and check whether the system detects or prevents
  it.
```
