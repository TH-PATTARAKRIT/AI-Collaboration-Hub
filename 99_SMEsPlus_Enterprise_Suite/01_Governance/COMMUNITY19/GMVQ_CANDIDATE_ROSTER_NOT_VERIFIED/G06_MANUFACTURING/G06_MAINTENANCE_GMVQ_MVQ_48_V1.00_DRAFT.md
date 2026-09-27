# SMEsPlus ENTERPRISE SUITE
## GMVQ — G06 MANUFACTURING / maintenance Module Adversarial MVQ Bank

**Document ID:** GMVQ-G06-MAINTENANCE-MVQ48-V1.00
**Group:** G06 MANUFACTURING
**Module Metadata:** `maintenance`
**Wave:** W2
**Author Cell:** P10
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) questions for `maintenance` — equipment
availability, preventive and corrective work. Unlike the other two banks in this delivery,
`maintenance` is NOT a bridge module per GMVQ_BRIDGE_MODULE_RULE_V1.00: it is a capability of its
own, and this bank therefore gives it the deeper, standalone treatment a base-like module earns,
rather than restricting coverage to a seam against a second capability.

Coverage deliberately spans: preventive scheduling by calendar versus by usage and where usage is
actually sourced from; the distinct lifecycle of a request, a scheduled intervention, and an
unplanned breakdown; equipment committed to an operation while being declared out of service;
parts and labour consumed against an intervention; equipment shared across teams, locations, and
companies; an intervention closed without the work being done; history surviving archival,
replacement, or transfer; who may declare equipment serviceable; capacity plans that silently
ignore maintenance windows; and the audit trail linking an operational failure back to equipment
state at that moment.

The question text is source-neutral. It does not name any vendor or product, any technical
identifier (model, table, field, method, XML ID, API path), or the module's own metadata name —
`maintenance` appears only in the `MODULE:` field of each question block, never in question text.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` — a concrete result that
  would prove the paired `HYPOTHESIS` wrong, not a restatement of it.
- No padding: each of the 48 questions tests a materially distinct hypothesis; no two share a
  disconfirming observation or reduce to a variation of another question in this bank.
- `LAYER: BASE` marks questions about equipment master data, schedule and category configuration.
  `LAYER: PROCESS` marks questions about behaviour during a live request, intervention, or
  breakdown event. Both layers exist for this module and are tagged throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/observation
  from the relevant lane.
- `MODULE + QID` is a Research Evidence Join Key only. No coverage or compliance status is
  derived from the existence of a question.
- This document is PREPARED ONLY / NOT FROZEN. It carries no Boss approval and authorizes no
  merge, release, or gate closure.

## G06-MAINTENANCE-Q001

```yaml
QID: G06-MAINTENANCE-Q001
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where a piece of equipment has both a calendar-based and a usage-based preventive schedule
  configured at the same time, exactly one defined rule governs which one actually triggers the
  next intervention, rather than both silently generating independent, possibly conflicting due
  dates.
WHY_IT_MATTERS: >
  Two independent triggers can create duplicate work, or worse, let the later of the two silently
  suppress an earlier due date that should have driven action first.
DISCONFIRMING_OBSERVATION: >
  Equipment with both a calendar and a usage-based schedule reaches its usage threshold and its
  calendar date at different times, and both independently generate separate, unreconciled due
  interventions.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure both a calendar-based and a usage-based preventive schedule on one piece of equipment,
  and observe what happens as each threshold is reached at a different time.
```

## G06-MAINTENANCE-Q002

```yaml
QID: G06-MAINTENANCE-Q002
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A usage-based preventive schedule's usage count is sourced from a defined, documented origin —
  and a reading from that origin that is delayed, missing, or manually entered is distinguishable
  from one automatically captured, rather than all readings being trusted identically regardless
  of source.
WHY_IT_MATTERS: >
  If a manually entered reading is trusted the same as an automatically captured one with no way
  to tell them apart, a single mistaken manual entry can silently reset or corrupt the schedule's
  whole basis.
DISCONFIRMING_OBSERVATION: >
  A manually entered usage reading is indistinguishable, in the schedule's own record, from a
  reading captured through the equipment's normal usage-tracking source.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enter a usage reading manually alongside one captured through the equipment's normal
  usage-tracking source, and compare how each is recorded against the schedule.
```

## G06-MAINTENANCE-Q003

```yaml
QID: G06-MAINTENANCE-Q003
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Raising a service request against equipment that is currently mid-operation logs the request
  without itself altering the equipment's current usability — raising a request and declaring
  equipment out of service are two distinct actions, not one implied by the other.
WHY_IT_MATTERS: >
  If merely raising a request silently pulls equipment out of service, a routine, non-urgent
  request could unexpectedly halt work still legitimately in progress.
DISCONFIRMING_OBSERVATION: >
  Raising a service request against equipment currently mid-operation changes that equipment's
  availability state with no separate, explicit out-of-service action taken.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Raise a service request against equipment that is actively in use, and check whether its
  availability state changes as a side effect of the request alone.
```

## G06-MAINTENANCE-Q004

```yaml
QID: G06-MAINTENANCE-Q004
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Declaring equipment out of service while an operation still holds a commitment against it (for
  example, a reserved future use) surfaces that conflict explicitly to whoever holds the
  commitment, rather than leaving the commitment silently unaffected and undetected until the
  operation actually tries to proceed.
WHY_IT_MATTERS: >
  A silent, undetected conflict means the disruption is only discovered at the worst possible
  moment — when the committed operation is already trying to start.
DISCONFIRMING_OBSERVATION: >
  Equipment already committed to a future operation is declared out of service with no flag or
  notice raised against that existing commitment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Commit equipment to a future operation, then declare that equipment out of service, and check
  whether the existing commitment is flagged.
```

## G06-MAINTENANCE-Q005

```yaml
QID: G06-MAINTENANCE-Q005
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A request (raised, not yet scheduled), a scheduled intervention (planned in advance), and an
  unplanned breakdown (reactive) are tracked as three genuinely distinct lifecycle categories,
  each with its own defined state progression, rather than being collapsed into one record type
  distinguished only by a label that does not affect how it behaves.
WHY_IT_MATTERS: >
  Collapsing the three into one behaviourally identical type makes it impossible to separately
  measure, for example, how often planned work slips versus how often equipment breaks down
  unplanned — the two have very different governance implications.
DISCONFIRMING_OBSERVATION: >
  A scheduled intervention and an unplanned breakdown, once created, follow identical state
  progressions and available actions with no behavioural difference tied to their category.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create one scheduled intervention and one unplanned breakdown record, and compare the state
  progression and available actions each one actually supports.
```

## G06-MAINTENANCE-Q006

```yaml
QID: G06-MAINTENANCE-Q006
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Parts consumed against an intervention are tracked through a stock-consumption mechanism that
  correctly reduces available inventory and attributes the cost to that intervention, rather than
  being recorded as a free-text note with no effect on stock or cost.
WHY_IT_MATTERS: >
  A free-text-only record of parts used means inventory counts silently drift from reality every
  time service consumes stock, and equipment running cost is understated.
DISCONFIRMING_OBSERVATION: >
  Recording a part as consumed against an intervention leaves the part's available stock quantity
  unchanged and posts no cost attributable to that intervention.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a part as consumed against an intervention, then check whether stock quantity and cost
  attribution actually reflect that consumption.
```

## G06-MAINTENANCE-Q007

```yaml
QID: G06-MAINTENANCE-Q007
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Labour recorded against an intervention is captured with enough structure (who, how long, on
  what) to attribute a cost, rather than existing only as an unstructured note that cannot be
  totalled or attributed.
WHY_IT_MATTERS: >
  Unstructured labour notes mean the true cost of maintaining a piece of equipment can never be
  reliably totalled across interventions.
DISCONFIRMING_OBSERVATION: >
  Labour recorded against a completed intervention has no structured time or cost attribution
  derivable from it, only free text.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record labour against a completed intervention and check whether it yields a structured,
  attributable cost figure.
```

## G06-MAINTENANCE-Q008

```yaml
QID: G06-MAINTENANCE-Q008
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When equipment is shared across multiple teams, a service action initiated by one team is
  visibly surfaced to the other teams currently relying on that equipment, rather than being
  visible only within the initiating team's own view.
WHY_IT_MATTERS: >
  A team with no visibility into another team's service action on shared equipment can plan
  work against equipment that is about to become unavailable with no warning.
DISCONFIRMING_OBSERVATION: >
  A service action initiated by one team against shared equipment produces no visible change
  or notice in another team's own view of that same equipment's availability.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Initiate a service action on equipment shared by two teams, from one team's context, and
  check whether the other team's view reflects it.
```

## G06-MAINTENANCE-Q009

```yaml
QID: G06-MAINTENANCE-Q009
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Equipment shared across multiple physical locations carries its service history and current
  availability state with it as it moves, rather than that state remaining attached to the
  location it was originally associated with.
WHY_IT_MATTERS: >
  History or availability tied to the wrong location means whoever now has physical custody of the
  equipment cannot rely on the system's record of its actual condition.
DISCONFIRMING_OBSERVATION: >
  Moving equipment to a new location leaves its service history or current availability state
  displayed only under its original location, not the current one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Move a piece of equipment with existing service history to a new location, and check where
  that history and current state are displayed afterward.
```

## G06-MAINTENANCE-Q010

```yaml
QID: G06-MAINTENANCE-Q010
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Equipment shared across multiple companies has its service record visibility correctly
  scoped per company, and a service action taken under one company does not silently change
  availability as seen by a different company sharing that equipment.
WHY_IT_MATTERS: >
  A cross-company leak on shared equipment means one tenant's service decision can
  unexpectedly affect another tenant's operations with no boundary enforced between them.
DISCONFIRMING_OBSERVATION: >
  A service action taken on equipment under one company changes the availability state visible
  to a different company that also has access to that equipment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Share equipment across two companies, take a service action under one company's context, and
  check whether the other company's view of availability is affected.
```

## G06-MAINTENANCE-Q011

```yaml
QID: G06-MAINTENANCE-Q011
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Closing an intervention as done requires, or at minimum flags the absence of, some indication
  that the actual work was performed (such as a recorded outcome, parts, or labour) — closure
  alone, with no such indication, does not by itself imply the work was actually completed.
WHY_IT_MATTERS: >
  If closure alone is treated as proof the work was done, equipment can be declared fit for use
  based on a record that never actually confirms any work occurred.
DISCONFIRMING_OBSERVATION: >
  An intervention with no recorded outcome, parts, or labour is closed as done with no flag or
  distinction from an intervention that recorded genuine work.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close an intervention as done with no recorded outcome, parts, or labour attached, and check
  whether that is flagged or treated identically to a fully documented closure.
```

## G06-MAINTENANCE-Q012

```yaml
QID: G06-MAINTENANCE-Q012
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Archiving a piece of equipment leaves its service history fully queryable, rather than
  archival severing access to the historical record.
WHY_IT_MATTERS: >
  A later audit, warranty claim, or incident review does not stop needing an archived asset's
  service history just because the asset itself is no longer active.
DISCONFIRMING_OBSERVATION: >
  Archiving a piece of equipment makes its prior service history inaccessible or
  unrecoverable through normal means.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Build up service history on a piece of equipment, archive it, and check whether that history
  remains queryable afterward.
```

## G06-MAINTENANCE-Q013

```yaml
QID: G06-MAINTENANCE-Q013
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When one physical unit of equipment is replaced by another under the same equipment record, the
  service history correctly splits between the old and new physical unit, rather than
  blending both units' history as though they were one continuous piece of equipment.
WHY_IT_MATTERS: >
  Blended history after a physical replacement misattributes wear, failures, and interventions to
  a unit that never actually experienced them.
DISCONFIRMING_OBSERVATION: >
  After a physical unit is replaced under the same equipment record, an intervention performed on
  the old unit and one performed on the new unit are indistinguishable in the combined history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Build history on an equipment record, replace the physical unit behind that record, add further
  history, and check whether old-unit and new-unit history are distinguishable.
```

## G06-MAINTENANCE-Q014

```yaml
QID: G06-MAINTENANCE-Q014
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Transferring equipment to a different department or owner gives the receiving party full
  visibility of the equipment's prior service history, rather than the transfer resetting or
  hiding history accumulated under the previous owner.
WHY_IT_MATTERS: >
  A receiving party with no visibility into prior history cannot make an informed judgement about
  the equipment's actual condition or upcoming service needs.
DISCONFIRMING_OBSERVATION: >
  After equipment is transferred to a new department or owner, its prior service history is no
  longer visible under the new ownership.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Build service history on equipment under one owner, transfer it to a different department or
  owner, and check whether the prior history remains visible.
```

## G06-MAINTENANCE-Q015

```yaml
QID: G06-MAINTENANCE-Q015
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Declaring equipment serviceable again after an intervention requires a role distinct from the
  role that merely performed the repair work itself, so the same actor is not automatically both
  the one who did the work and the one who certifies it.
WHY_IT_MATTERS: >
  Without that separation, the only check on whether repaired equipment is actually safe to use
  again is the say-so of the same person who just worked on it.
DISCONFIRMING_OBSERVATION: >
  A user holding only the role that performs repair work is able to declare the equipment
  serviceable again with no additional role or check required.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user holding only repair-execution rights, attempt to declare repaired equipment
  serviceable and observe whether an additional role is required.
```

## G06-MAINTENANCE-Q016

```yaml
QID: G06-MAINTENANCE-Q016
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A capacity or production plan that would use a piece of equipment checks that equipment's
  current and scheduled service state before committing it to the plan, rather than allowing a
  plan to be created that silently double-books equipment already blocked for a service
  window.
WHY_IT_MATTERS: >
  A plan built with no awareness of a scheduled service window discovers the conflict only when
  the equipment is actually needed and unavailable, disrupting whatever else was scheduled around
  it.
DISCONFIRMING_OBSERVATION: >
  A capacity plan is created and confirmed that assigns equipment to a period during which a
  service window is already scheduled, with no warning raised at plan-creation time.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Schedule a service window on a piece of equipment, then attempt to build a capacity plan
  that assigns the same equipment during that window, and check for a warning.
```

## G06-MAINTENANCE-Q017

```yaml
QID: G06-MAINTENANCE-Q017
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An operational failure or defect recorded elsewhere in the system can be explicitly linked back
  to the service state that equipment was actually in at the moment of the failure, rather than
  that link being obtainable only through manual cross-referencing of separate timestamps.
WHY_IT_MATTERS: >
  Without an explicit link, establishing whether a failure was foreseeable from the equipment's
  service state requires reconstructing the timeline by hand, which is slow and error-prone
  exactly when speed and accuracy matter most.
DISCONFIRMING_OBSERVATION: >
  An operational failure record has no queryable link to the service state of the equipment
  involved at the time of the failure, requiring manual timestamp comparison to establish one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record an operational failure involving a piece of equipment with a known service state at
  that moment, and check whether the failure record links explicitly to that state.
```

## G06-MAINTENANCE-Q018

```yaml
QID: G06-MAINTENANCE-Q018
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A preventive schedule's next due date or usage threshold is recalculated automatically once the
  triggering intervention is completed, rather than requiring a separate manual reset that can be
  forgotten and leave the schedule silently drifting out of date.
WHY_IT_MATTERS: >
  A schedule dependent on manual reset will, sooner or later, be forgotten once, and from that
  point on the next due date no longer reflects when the work was actually last performed.
DISCONFIRMING_OBSERVATION: >
  Completing a preventive intervention leaves the schedule's next due date or usage threshold
  unchanged until a separate manual action resets it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Complete a preventive intervention and check, without any further manual action, whether the
  schedule's next due point is automatically recalculated.
```

## G06-MAINTENANCE-Q019

```yaml
QID: G06-MAINTENANCE-Q019
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Two preventive schedules on the same equipment triggering at different times are merged into a
  single due intervention rather than generating two independent, potentially conflicting open
  records that could each separately mark the equipment serviceable.
WHY_IT_MATTERS: >
  Two independent open records for the same underlying need can be closed independently of each
  other, letting one closure mask that the other's work was never actually done.
DISCONFIRMING_OBSERVATION: >
  Two preventive schedules on the same equipment, triggering close together in time, produce two
  separate, independently closable intervention records rather than one merged record.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure two preventive schedules on one piece of equipment set to trigger close together, and
  observe whether one merged or two independent records result.
```

## G06-MAINTENANCE-Q020

```yaml
QID: G06-MAINTENANCE-Q020
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A service request raised against equipment that has since been decommissioned is
  automatically closed or clearly flagged as orphaned, rather than remaining open indefinitely as
  though the equipment were still active.
WHY_IT_MATTERS: >
  An indefinitely open request against decommissioned equipment pollutes open-work reporting with
  work that can never actually be performed.
DISCONFIRMING_OBSERVATION: >
  A request raised against equipment that is later decommissioned remains open, with no automatic
  closure or flag, indistinguishable from a request against still-active equipment.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Raise a request against equipment, decommission that equipment while the request is still open,
  and check the request's resulting state.
```

## G06-MAINTENANCE-Q021

```yaml
QID: G06-MAINTENANCE-Q021
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two users attempting, at the same time, to set contradictory availability states on the same
  equipment (one declaring it serviceable, one declaring it out of service) resolve to a single,
  consistent final state with the conflict detectable afterward, rather than an unresolved or
  silently overwritten result.
WHY_IT_MATTERS: >
  An undetected conflict here means whichever action happened to be processed last silently wins,
  with no one aware that a contradictory action was ever attempted.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous, contradictory availability declarations on the same equipment leave no
  trace that a conflict occurred, and the final state cannot be explained by either action alone.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Trigger two contradictory availability declarations on the same equipment at nearly the same
  time, repeated across multiple trials, and inspect the resulting state and any conflict record.
```

## G06-MAINTENANCE-Q022

```yaml
QID: G06-MAINTENANCE-Q022
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An intervention whose actual duration significantly overruns its expected completion produces
  some visible escalation or flag, rather than the record simply remaining open with no
  distinction from an intervention still comfortably within its expected window.
WHY_IT_MATTERS: >
  A silent overrun means equipment stays unavailable, and the reason unresolved, for longer than
  anyone realizes, because nothing distinguishes a minor delay from a serious one.
DISCONFIRMING_OBSERVATION: >
  An intervention running well beyond its expected completion date shows no visible difference
  from one still within its expected window.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Leave an intervention open well past its expected completion date and check whether that state
  is visibly distinguished from a normally progressing one.
```

## G06-MAINTENANCE-Q023

```yaml
QID: G06-MAINTENANCE-Q023
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The choice between calendar-based and usage-based preventive scheduling is configurable
  independently per piece of equipment, rather than fixed as a single choice applied uniformly
  across the whole programme.
WHY_IT_MATTERS: >
  Equipment varies in how its wear actually accumulates, and a programme-wide fixed choice forces
  an inappropriate basis onto equipment that does not fit it.
DISCONFIRMING_OBSERVATION: >
  Attempting to set different scheduling bases (calendar versus usage) on two different pieces of
  equipment results in both being forced onto the same basis regardless of the individual setting.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Attempt to configure one piece of equipment for calendar-based and another for usage-based
  preventive scheduling, and check whether each setting actually takes independent effect.
```

## G06-MAINTENANCE-Q024

```yaml
QID: G06-MAINTENANCE-Q024
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a scheduled preventive intervention before it is performed leaves the schedule's
  "next due" calculation correctly still overdue, rather than resetting it as though the work had
  actually been completed.
WHY_IT_MATTERS: >
  A cancellation that resets the schedule the same as a completion would let genuinely
  unperformed preventive work silently disappear from the due list.
DISCONFIRMING_OBSERVATION: >
  Cancelling a scheduled preventive intervention advances the schedule's next-due calculation as
  though the work had been completed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cancel a scheduled preventive intervention before performing it, and check whether the
  schedule's next-due calculation reflects that the work was not actually done.
```

## G06-MAINTENANCE-Q025

```yaml
QID: G06-MAINTENANCE-Q025
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reopening or reversing an intervention previously marked complete correctly reverses the parts
  and labour consumption recorded against it, rather than leaving that consumption in place while
  the intervention's own status reverts.
WHY_IT_MATTERS: >
  An inconsistent reversal leaves stock and cost records reflecting a completion that the
  intervention's own status no longer claims happened.
DISCONFIRMING_OBSERVATION: >
  Reopening a previously completed intervention reverts its status but leaves the parts and
  labour consumption originally recorded against it unchanged.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete an intervention with recorded parts and labour, reopen or reverse it, and check whether
  that consumption is correspondingly reversed.
```

## G06-MAINTENANCE-Q026

```yaml
QID: G06-MAINTENANCE-Q026
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A capacity or scheduling plan elsewhere in the system queries current equipment service
  state before committing that equipment, regardless of whether the service window was
  scheduled before or after the plan itself was created.
WHY_IT_MATTERS: >
  If the check only works for windows scheduled before the plan, a service window added
  afterward can silently conflict with an already-confirmed plan with no warning either way.
DISCONFIRMING_OBSERVATION: >
  A service window scheduled after a capacity plan was already confirmed produces no conflict
  warning against that plan, while the reverse ordering does.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Confirm a capacity plan, then schedule a conflicting service window afterward, and compare
  the result to scheduling the window first and the plan second.
```

## G06-MAINTENANCE-Q027

```yaml
QID: G06-MAINTENANCE-Q027
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Equipment with no preventive schedule configured at all is distinguishable, in its own record,
  from equipment whose schedule is configured but simply not yet due — the absence of a schedule
  is a visible, distinct state, not indistinguishable silence.
WHY_IT_MATTERS: >
  If the two look the same, no one reviewing the equipment list can tell "this needs a schedule
  set up" apart from "this is fine, nothing due yet."
DISCONFIRMING_OBSERVATION: >
  Equipment with no preventive schedule configured presents identically to equipment with a
  configured schedule that simply has no intervention currently due.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the record of a piece of equipment with no preventive schedule configured against one
  with a configured but not-yet-due schedule.
```

## G06-MAINTENANCE-Q028

```yaml
QID: G06-MAINTENANCE-Q028
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A service record moves through a defined sequence of states, and an attempt to skip directly
  from an early state (such as newly raised) to a final state (such as done) without passing
  through the intermediate states is blocked or at minimum recorded as an explicit exception.
WHY_IT_MATTERS: >
  If any state skip is silently allowed, the recorded lifecycle can no longer be trusted to
  reflect what actually happened — a record marked done may never have genuinely been worked.
DISCONFIRMING_OBSERVATION: >
  A service record moves directly from newly raised to done with no intermediate state and no
  flag marking that as an exception.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt to move a newly raised service record directly to a done state, bypassing
  intermediate states, and observe whether that is blocked or flagged.
```

## G06-MAINTENANCE-Q029

```yaml
QID: G06-MAINTENANCE-Q029
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  There is a defined distinction between who may raise a service request (broadly available)
  and who may approve or schedule it as committed work, rather than any user who can raise a
  request also being able to schedule their own request unilaterally.
WHY_IT_MATTERS: >
  Without that distinction, requests bypass any prioritisation or resourcing check, and equipment
  time gets committed purely by whoever happened to raise the request first.
DISCONFIRMING_OBSERVATION: >
  A user with only request-raising rights is able to schedule their own request as committed work
  with no separate approval or scheduling permission required.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with only request-raising rights, raise a request and attempt to schedule it as
  committed work directly.
```

## G06-MAINTENANCE-Q030

```yaml
QID: G06-MAINTENANCE-Q030
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A part consumed against an intervention that is itself lot- or serial-tracked has that specific
  lot or serial preserved in the intervention's own record, not reduced to an untracked quantity.
WHY_IT_MATTERS: >
  Losing the specific lot or serial defeats any later attempt to trace a defective part back to
  the specific equipment it was installed in.
DISCONFIRMING_OBSERVATION: >
  Consuming a lot- or serial-tracked part against an intervention records only a quantity, with no
  reference to which specific lot or serial was actually used.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consume a lot- or serial-tracked part against an intervention, and inspect the intervention's
  record for that specific lot or serial reference.
```

## G06-MAINTENANCE-Q031

```yaml
QID: G06-MAINTENANCE-Q031
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A breakdown logged after the fact (equipment already informally fixed before being recorded) is
  distinguishable from a breakdown logged in real time as it occurred, so that downtime and
  response-time reporting is not skewed by after-the-fact entries presenting as though logged live.
WHY_IT_MATTERS: >
  Indistinguishable after-the-fact logging corrupts response-time metrics with entries that never
  actually reflect a real-time response.
DISCONFIRMING_OBSERVATION: >
  A breakdown record created well after the equipment was already informally fixed carries no
  marker distinguishing it from one logged at the actual moment of failure.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Log a breakdown well after the equipment was already fixed informally, and inspect the record
  for a marker distinguishing it from a real-time log.
```

## G06-MAINTENANCE-Q032

```yaml
QID: G06-MAINTENANCE-Q032
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A corrective intervention can be logged standalone with no link back to a preceding request or
  breakdown, and that standalone status is itself visible, distinguishing it from a corrective
  action that does trace back to why it was needed.
WHY_IT_MATTERS: >
  If standalone corrective work looks identical to work with a documented trigger, the true
  proportion of service driven by proactive versus reactive causes cannot be measured.
DISCONFIRMING_OBSERVATION: >
  A corrective intervention logged with no linked request or breakdown appears identical to one
  that does have such a link, with no visible distinction between the two.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Log one corrective intervention with a linked request and one with none, and compare their
  records for a visible distinction.
```

## G06-MAINTENANCE-Q033

```yaml
QID: G06-MAINTENANCE-Q033
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Equipment declared out of service while it is mid-way through an operation already using it
  produces an explicit interruption or flag on that operation, rather than the operation being
  silently allowed to continue and complete as though nothing had changed.
WHY_IT_MATTERS: >
  Letting an operation continue unflagged on equipment just declared out of service means the
  declaration achieved nothing for the work already underway, defeating its purpose.
DISCONFIRMING_OBSERVATION: >
  An operation already using equipment continues to completion with no interruption or flag after
  that equipment is declared out of service mid-operation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Start an operation using a piece of equipment, declare that equipment out of service while the
  operation is still running, and observe the operation's outcome.
```

## G06-MAINTENANCE-Q034

```yaml
QID: G06-MAINTENANCE-Q034
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Equipment marked out of service is actually prevented from being selected for a new operation,
  not merely shown with an advisory note that a user can disregard.
WHY_IT_MATTERS: >
  A merely advisory out-of-service state is easy to miss under time pressure, and equipment
  genuinely unfit for use can still be selected and run.
DISCONFIRMING_OBSERVATION: >
  A new operation is successfully started using equipment currently marked out of service, with
  only an advisory note and no actual block.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Mark equipment out of service, then attempt to select it for a brand-new operation, and observe
  whether the attempt is actually blocked.
```

## G06-MAINTENANCE-Q035

```yaml
QID: G06-MAINTENANCE-Q035
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The full sequence of who declared equipment out of service, who performed the work, and who
  declared it serviceable again is preserved as three distinct, individually attributable audit
  events, rather than compressed into a single "resolved" record that loses who did what.
WHY_IT_MATTERS: >
  A compressed record cannot answer a basic accountability question after the fact — whether the
  person who declared equipment fit for use again was actually different from the one who
  repaired it.
DISCONFIRMING_OBSERVATION: >
  Reviewing a resolved service event shows only a single combined record, with no way to
  separately identify who declared it out of service, who performed the work, and who declared it
  serviceable again.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Take a piece of equipment through out-of-service declaration, repair work, and a serviceable
  declaration by up to three different actors, then review the resulting audit trail.
```

## G06-MAINTENANCE-Q036

```yaml
QID: G06-MAINTENANCE-Q036
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The total cost of an intervention (parts plus labour) has a defined, discoverable attribution —
  to the equipment's own running cost history, to a general account, or configurably to either —
  rather than an attribution that varies unpredictably between otherwise similar interventions.
WHY_IT_MATTERS: >
  Unpredictable cost attribution makes it impossible to reliably compare the true running cost of
  one piece of equipment against another.
DISCONFIRMING_OBSERVATION: >
  Two otherwise similar interventions, with no stated configuration difference, post their total
  cost to different attributions (one to equipment history, one to a general account).
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Complete two comparable interventions under the same configuration and compare where each one's
  total cost is actually attributed.
```

## G06-MAINTENANCE-Q037

```yaml
QID: G06-MAINTENANCE-Q037
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A service team's own capacity (how many interventions it can actively handle at once) is
  accounted for when new interventions are scheduled onto it, rather than an unlimited number of
  interventions being schedulable onto one team regardless of its actual capacity.
WHY_IT_MATTERS: >
  Ignoring team capacity produces a schedule that looks complete on paper but is impossible to
  actually deliver, silently pushing real completion dates later than promised.
DISCONFIRMING_OBSERVATION: >
  A number of interventions well beyond a team's stated or historical capacity is scheduled onto
  that team for the same period with no warning raised.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Schedule a number of interventions onto one team clearly beyond its normal capacity for the same
  period, and check for any warning or capacity check.
```

## G06-MAINTENANCE-Q038

```yaml
QID: G06-MAINTENANCE-Q038
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where equipment is itself composed of nested pieces of equipment (such as several machines
  forming one line), declaring a nested piece out of service propagates a visible availability
  consequence to the parent grouping, rather than the parent continuing to show as fully available
  while a piece it depends on is actually down.
WHY_IT_MATTERS: >
  A parent grouping that looks fully available while a critical nested piece is down can be
  committed to work it cannot actually perform.
DISCONFIRMING_OBSERVATION: >
  A nested piece of equipment is declared out of service, and the parent grouping it belongs to
  continues to show as fully available with no visible consequence.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Declare a nested piece of equipment within a larger grouping out of service, and check whether
  the parent grouping's own availability reflects that.
```

## G06-MAINTENANCE-Q039

```yaml
QID: G06-MAINTENANCE-Q039
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Manually triggering a calendar-based preventive intervention early, ahead of its normal due
  date, correctly resets the calendar cycle from the new, actual completion date rather than
  leaving the original due date still in force.
WHY_IT_MATTERS: >
  A cycle that ignores an early completion will demand the next intervention too soon relative to
  when the work was actually last done, or too late if the original date is simply kept.
DISCONFIRMING_OBSERVATION: >
  Completing a calendar-based preventive intervention ahead of its due date leaves the next
  due date calculated from the original schedule rather than from the actual completion date.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a calendar-based preventive intervention early, complete it, and check which date the
  next cycle is calculated from.
```

## G06-MAINTENANCE-Q040

```yaml
QID: G06-MAINTENANCE-Q040
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where service record categories or types are configurable per company or tenant, a
  custom-defined type remains compatible with the standard distinction between a request, a
  scheduled intervention, and an unplanned breakdown, rather than bypassing that distinction
  entirely.
WHY_IT_MATTERS: >
  A custom type that bypasses the standard distinction can generate records that no
  cross-programme reporting relying on that distinction can correctly classify.
DISCONFIRMING_OBSERVATION: >
  A custom-defined service type cannot be classified as a request, a scheduled intervention, or
  an unplanned breakdown by anything relying on that standard distinction.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Define a custom service record type under one company's configuration, and check whether it
  remains classifiable under the standard request/intervention/breakdown distinction.
```

## G06-MAINTENANCE-Q041

```yaml
QID: G06-MAINTENANCE-Q041
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Parts consumed against an intervention are drawn from stock scoped to the same company or
  tenant as the equipment itself, and an intervention cannot silently consume parts belonging to a
  different company or tenant.
WHY_IT_MATTERS: >
  A cross-tenant stock leak on service parts moves value and inventory between companies with
  no authorised transfer ever having taken place.
DISCONFIRMING_OBSERVATION: >
  An intervention on equipment under one company successfully consumes parts held in stock
  belonging to a different company or tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to consume, against an intervention on equipment under one company, a part held in stock
  scoped to a different company, and observe whether that is permitted.
```

## G06-MAINTENANCE-Q042

```yaml
QID: G06-MAINTENANCE-Q042
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A breakdown recorded on equipment while a preventive intervention for that same equipment is
  already pending resolves through a single coordinated outcome — merged, explicitly superseding
  one another, or both kept open with an explicit link between them — rather than two entirely
  independent open records that could each separately mark the equipment serviceable.
WHY_IT_MATTERS: >
  Two independently closable open records on the same equipment let one get closed while the
  other's underlying issue remains genuinely unresolved, with the equipment shown as fine either
  way.
DISCONFIRMING_OBSERVATION: >
  A breakdown and an already-pending preventive intervention on the same equipment exist as two
  entirely independent records, either of which can be closed to mark the equipment serviceable
  with no link between them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise a breakdown on equipment that already has a pending preventive intervention, and check
  whether the two records are linked or can be closed entirely independently.
```

## G06-MAINTENANCE-Q043

```yaml
QID: G06-MAINTENANCE-Q043
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Equipment retired or scrapped is distinguishable in its own record from equipment merely
  archived for being temporarily idle, so that a service history review can tell the two
  apart rather than treating both as equally gone from active use for the same reason.
WHY_IT_MATTERS: >
  Conflating retirement with temporary idling can cause equipment that is only paused to be
  excluded from active tracking as though it were permanently gone, or vice versa.
DISCONFIRMING_OBSERVATION: >
  A retired or scrapped piece of equipment and a temporarily idled, archived piece of equipment
  present identically in the equipment record, with no distinguishing status.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Retire one piece of equipment and archive another as temporarily idle, and compare their
  resulting records for a distinguishing status.
```

## G06-MAINTENANCE-Q044

```yaml
QID: G06-MAINTENANCE-Q044
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Requesting service work and later declaring that same work complete and the equipment
  serviceable are actions that can be required to involve two different people (separation of
  duties), rather than the same individual always being permitted to do both unilaterally with no
  option to enforce a second party.
WHY_IT_MATTERS: >
  With no way to enforce separation, an actor can raise, perform, and self-certify service
  work entirely alone, removing any independent check on whether the equipment is genuinely fit for
  use again.
DISCONFIRMING_OBSERVATION: >
  There is no configuration or control available anywhere that can require a service request
  and its serviceable declaration to involve two different individuals.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Search the available configuration for any control enforcing separation of duties between
  requesting and certifying service work, and attempt to enable it.
```

## G06-MAINTENANCE-Q045

```yaml
QID: G06-MAINTENANCE-Q045
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A service intervention can be recorded with no linked equipment at all (for example, general
  facility work), and when it is, it is tracked with a clearly reduced but still coherent set of
  fields, rather than either being disallowed entirely or forced to reference equipment that was
  not actually involved.
WHY_IT_MATTERS: >
  Forcing every intervention to reference equipment when none was actually involved corrupts that
  equipment's own service history with unrelated work.
DISCONFIRMING_OBSERVATION: >
  Attempting to record an intervention with no linked equipment is either rejected outright, or
  succeeds only by being forced to reference an equipment record that was not actually involved.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to record a service intervention describing general facility work with no equipment
  involved, and observe whether that is possible without a forced equipment reference.
```

## G06-MAINTENANCE-Q046

```yaml
QID: G06-MAINTENANCE-Q046
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When equipment currently shown as under service and a completed intervention record already
  marking it serviceable disagree, one clearly defined state is authoritative and displayed
  consistently everywhere, rather than different views of the same equipment showing different
  answers.
WHY_IT_MATTERS: >
  Two different answers to "is this equipment usable right now" depending on which screen or
  report is consulted can lead someone to use equipment believed available that is not, or the
  reverse.
DISCONFIRMING_OBSERVATION: >
  One view of a piece of equipment shows it as under service while another view of the same
  equipment, at the same moment, shows it as serviceable.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a situation where an equipment's availability flag and its latest completed intervention
  record could disagree, and compare what different views of that equipment show at that moment.
```

## G06-MAINTENANCE-Q047

```yaml
QID: G06-MAINTENANCE-Q047
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Whether a capacity plan was built before or after a conflicting service window was scheduled
  does not change whether the resulting conflict is actually caught — the check is applied
  consistently regardless of which one existed first.
WHY_IT_MATTERS: >
  If the check only catches the conflict in one ordering, planners who happen to schedule
  service second will get no warning that an existing plan is now compromised.
DISCONFIRMING_OBSERVATION: >
  A conflict between a capacity plan and a service window is caught when the plan is built
  first, but not caught when the service window is scheduled first, or vice versa.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create the conflicting plan and service window in one order and check for a warning, then
  repeat with the reverse order and compare.
```

## G06-MAINTENANCE-Q048

```yaml
QID: G06-MAINTENANCE-Q048
MODULE: maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Given a specific point in time in the past, the equipment's actual serviceability state at that
  moment (in service, out of service, or under service) can be reconstructed from history,
  rather than only the current or latest state being retrievable.
WHY_IT_MATTERS: >
  Without the ability to reconstruct a past state, an investigation into an incident that occurred
  at a specific past moment cannot establish what the equipment's true condition actually was at
  that time.
DISCONFIRMING_OBSERVATION: >
  Attempting to determine equipment's serviceability state as of a specific past point in time
  returns only its current state, with no way to reconstruct the historical value.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a piece of equipment's serviceability state more than once over time, then attempt to
  determine what its state was at a specific earlier point.
```
