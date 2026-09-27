# SMEsPlus ENTERPRISE SUITE
## GMVQ — G05 INVENTORY / stock_maintenance Module MVQ Bank

**Document ID:** GMVQ-G05-STOCK_MAINTENANCE-MVQ48-V1.00
**Group:** G05 INVENTORY
**Module Metadata:** `stock_maintenance`
**Wave:** W2
**Author Cell:** P07 (GMVQ Question Factory — Bridge Module Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose
This bank supplies the module-specific research questions for `stock_maintenance` — the seam
between equipment maintenance state and warehouse stock operations. It is written for a blind
two-lane study: Lane A reads reference source, Lane B observes a running system, and neither
sees the other's answers. Question text is source-neutral throughout and never names the module.

## Control
- `stock_maintenance` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Every question below
  passes the seam test: if the equipment/maintenance capability were removed and stock operations
  ran without it, the question would no longer make sense.
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` distinct from every other
  question's; no two questions share a disconfirming event.
- No padding: 48 questions test 48 distinct hypotheses spread across scheduling-vs-availability
  conflict, mid-operation maintenance interruption, stock physically committed to out-of-service
  equipment, spare-parts consumption and its valuation, retroactive fault discovery, capacity
  planning against maintenance windows, cross-company/warehouse equipment sharing, the audit link
  between a stock discrepancy and an equipment fault, and the authority to return equipment to
  service.
- This bank is DRAFT authoring output only. Not approved, not frozen, not verified.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived here.

---

## G05-STOCK_MAINTENANCE-Q001

```yaml
QID: G05-STOCK_MAINTENANCE-Q001
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An operation already scheduled against a specific piece of equipment is re-evaluated for
  feasibility if that equipment becomes unavailable before the operation executes, rather than
  proceeding as though nothing had changed.
WHY_IT_MATTERS: >
  Executing against equipment that is actually unavailable produces a result the business cannot
  rely on and may not discover until much later.
DISCONFIRMING_OBSERVATION: >
  The operation executes, or is allowed to be marked ready, with no check of the equipment's
  current availability state at that moment.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Schedule an operation against a specific piece of equipment, then mark that equipment
  unavailable before the operation's execution time, then attempt to proceed with the operation.
```

## G05-STOCK_MAINTENANCE-Q002

```yaml
QID: G05-STOCK_MAINTENANCE-Q002
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When equipment an operation depends on becomes unavailable after scheduling, a notice reaches
  the person responsible for that operation, not only an internal technical record nobody is
  expected to read.
WHY_IT_MATTERS: >
  A change that only exists in a log nobody watches is, for practical purposes, a change nobody
  was told about.
DISCONFIRMING_OBSERVATION: >
  The unavailability is recorded only in an internal record, with no notice surfaced to whoever
  owns the pending operation.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Schedule an operation against equipment, mark that equipment unavailable, and check what, if
  anything, the operation's responsible party is shown before or at the operation's start time.
```

## G05-STOCK_MAINTENANCE-Q003

```yaml
QID: G05-STOCK_MAINTENANCE-Q003
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Two operations scheduled against the same equipment for overlapping windows cannot both proceed
  unexamined; something decides which one may go ahead and what happens to the other.
WHY_IT_MATTERS: >
  Unresolved double-booking of a physical resource produces a conflict discovered only when both
  operations try to use the same equipment at once.
DISCONFIRMING_OBSERVATION: >
  Both overlapping operations are allowed to proceed as scheduled with no detection of the
  overlap, or the second silently overwrites the first's assignment.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Schedule two separate operations against the same equipment with windows that overlap, before
  either has started, and observe whether the conflict is detected.
```

## G05-STOCK_MAINTENANCE-Q004

```yaml
QID: G05-STOCK_MAINTENANCE-Q004
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where an equipment-availability check can be disabled by configuration, an operation completed
  while that check was off carries a visible trace that the check was not applied.
WHY_IT_MATTERS: >
  A silent bypass of a safety check is indistinguishable, later, from the check having correctly
  passed — which misleads anyone reviewing the result.
DISCONFIRMING_OBSERVATION: >
  An operation completed while the availability check was disabled shows no trace, anywhere in
  its record, that the check was off.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Disable the equipment-availability check by configuration, complete an operation against
  equipment that would otherwise have failed the check, and inspect the operation's record.
```

## G05-STOCK_MAINTENANCE-Q005

```yaml
QID: G05-STOCK_MAINTENANCE-Q005
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where recording equipment against an operation is optional, an operation with no equipment
  recorded is not reported or treated the same way as one that passed a confirmed
  equipment-availability check.
WHY_IT_MATTERS: >
  Conflating "no equipment recorded" with "equipment confirmed available" hides the difference
  between an unmonitored operation and a verified one.
DISCONFIRMING_OBSERVATION: >
  An operation with no equipment recorded is reported identically to one whose equipment passed
  an availability check.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Complete one operation with no equipment recorded and a second, comparable operation with
  equipment recorded and confirmed available, then compare how each is reported.
```

## G05-STOCK_MAINTENANCE-Q006

```yaml
QID: G05-STOCK_MAINTENANCE-Q006
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an equipment scheduling conflict forces an operation to a later time, the stock demand or
  promise date that operation was meant to satisfy moves with it rather than staying fixed against
  a time the operation can no longer meet.
WHY_IT_MATTERS: >
  A promise date left unchanged while the work behind it slips silently misleads whoever relies on
  that date downstream.
DISCONFIRMING_OBSERVATION: >
  The operation's time is deferred because of an equipment conflict but the stock reservation or
  promise date tied to it is left unchanged.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Force an equipment conflict that defers a scheduled operation, then inspect the stock demand or
  promise date the operation was originally meant to satisfy.
```

## G05-STOCK_MAINTENANCE-Q007

```yaml
QID: G05-STOCK_MAINTENANCE-Q007
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A preventive-maintenance schedule that comes due while equipment is already mid-operation does
  not silently take effect in a way that interrupts the operation already in progress.
WHY_IT_MATTERS: >
  An operation cut off mid-way by an unrelated background schedule can leave stock in an
  inconsistent, half-completed state.
DISCONFIRMING_OBSERVATION: >
  The maintenance state change takes effect immediately, and the in-progress operation is left
  pointing at equipment now marked unavailable with no reconciliation.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Start an operation against equipment, let a preventive-maintenance schedule come due against
  that same equipment while the operation is still in progress, and observe the outcome.
```

## G05-STOCK_MAINTENANCE-Q008

```yaml
QID: G05-STOCK_MAINTENANCE-Q008
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Overriding a due preventive-maintenance schedule so an in-progress operation can finish first is
  a distinct, attributable action, not an unrecorded side effect of letting the operation continue.
WHY_IT_MATTERS: >
  An unrecorded override of a maintenance safeguard removes the ability to know later who decided
  to run equipment past its due maintenance point.
DISCONFIRMING_OBSERVATION: >
  The in-progress operation continues past the maintenance due point with no record of who
  authorized continuing.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Let a preventive-maintenance schedule come due while an operation is in progress, allow the
  operation to continue to completion, and check the record for an authorizing action.
```

## G05-STOCK_MAINTENANCE-Q009

```yaml
QID: G05-STOCK_MAINTENANCE-Q009
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Actual equipment usage recorded through operations feeds the calculation of when the next
  preventive maintenance falls due, rather than that calculation running purely on a fixed
  calendar interval blind to how much the equipment actually worked.
WHY_IT_MATTERS: >
  A calendar-only schedule under-maintains heavily used equipment and over-maintains lightly used
  equipment, in either case for reasons the record does not reflect.
DISCONFIRMING_OBSERVATION: >
  Heavy actual usage recorded through operations has no observable effect on when the next
  maintenance falls due.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Record substantially heavier operational usage against one piece of equipment than another
  otherwise-identical piece, and compare how each one's next maintenance due date responds.
```

## G05-STOCK_MAINTENANCE-Q010

```yaml
QID: G05-STOCK_MAINTENANCE-Q010
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Postponing or skipping a due maintenance event leaves the equipment's record visibly distinct
  from equipment that was never due for maintenance at all.
WHY_IT_MATTERS: >
  Equipment running on deferred maintenance and equipment with nothing due look identical to
  anyone relying on its availability, unless the deferral is flagged.
DISCONFIRMING_OBSERVATION: >
  Postponing due maintenance leaves the equipment in a state indistinguishable from equipment that
  was never due.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Let a maintenance event come due, postpone or skip it, and compare the equipment's resulting
  state against otherwise-identical equipment with nothing due.
```

## G05-STOCK_MAINTENANCE-Q011

```yaml
QID: G05-STOCK_MAINTENANCE-Q011
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A scheduled background pass that advances equipment toward a maintenance-due state checks
  whether an operation is currently mid-flight on that equipment before changing its state.
WHY_IT_MATTERS: >
  An unattended background process that changes equipment state without regard to live operations
  can strand an operation already under way.
DISCONFIRMING_OBSERVATION: >
  The background pass changes the equipment's state with no check of current operation activity,
  observable as a state flip while an operation is actively referencing that equipment.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Start an operation against equipment approaching its maintenance due point, let the scheduled
  background pass run while the operation is still active, and observe the equipment's state.
```

## G05-STOCK_MAINTENANCE-Q012

```yaml
QID: G05-STOCK_MAINTENANCE-Q012
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where an operation depends on more than one piece of equipment, one of them becoming due for
  maintenance mid-operation is reflected in the operation's status rather than silently absorbed
  as if the full combined requirement were still met.
WHY_IT_MATTERS: >
  Treating a partially unavailable set of equipment as fully available overstates what the
  operation can actually still deliver.
DISCONFIRMING_OBSERVATION: >
  With several equipment records attached to one operation, one becoming due for maintenance
  produces no observable change to the operation's status.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Attach more than one piece of equipment to a single operation, bring one of them to its
  maintenance due point mid-operation, and observe the operation's status.
```

## G05-STOCK_MAINTENANCE-Q013

```yaml
QID: G05-STOCK_MAINTENANCE-Q013
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Stock physically committed to equipment that is then taken out of service is surfaced as
  at-risk, rather than continuing to show as ordinary available or reserved stock with no link to
  the equipment's changed state.
WHY_IT_MATTERS: >
  Stock that looks routinely available while it actually sits on out-of-service equipment can be
  promised or picked against in error.
DISCONFIRMING_OBSERVATION: >
  Equipment moves to out-of-service while stock remains recorded against it, and the stock record
  shows no distinguishing flag or hold.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Commit stock to a piece of equipment, take that equipment out of service, and inspect the
  stock's record for any resulting flag or hold.
```

## G05-STOCK_MAINTENANCE-Q014

```yaml
QID: G05-STOCK_MAINTENANCE-Q014
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Equipment cannot be marked out of service while operations are still open against it without
  those operations ending up in a distinctly flagged state, rather than continuing to look normal.
WHY_IT_MATTERS: >
  An open operation pointing at equipment that no longer exists in a usable state is a gap between
  what the record says and what is physically true.
DISCONFIRMING_OBSERVATION: >
  Equipment is set out of service with open operations still pointing at it, and those operations
  remain in a normal, unflagged state.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Open one or more operations against a piece of equipment, mark that equipment out of service
  while those operations remain open, and inspect their resulting state.
```

## G05-STOCK_MAINTENANCE-Q015

```yaml
QID: G05-STOCK_MAINTENANCE-Q015
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reassigning stock away from out-of-service equipment to alternate equipment or a location
  carries a reference back to the equipment fault that forced it, rather than reading as an
  ordinary, uneventful change.
WHY_IT_MATTERS: >
  Without that link, a reviewer cannot later tell why the stock moved or connect the move to the
  equipment issue that caused it.
DISCONFIRMING_OBSERVATION: >
  The reassignment record carries no reference connecting it to the equipment's out-of-service
  event.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Take equipment with committed stock out of service, reassign that stock elsewhere, and inspect
  the reassignment record for a link back to the equipment event.
```

## G05-STOCK_MAINTENANCE-Q016

```yaml
QID: G05-STOCK_MAINTENANCE-Q016
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Equipment shared across more than one company or warehouse shows the same out-of-service state
  to every party with stock committed to it, at the same time, rather than letting one party see
  it as available while another has already flagged it out.
WHY_IT_MATTERS: >
  Disagreement about a shared physical resource's state between the parties that depend on it
  produces exactly the physically-impossible outcome a shared record is supposed to prevent.
DISCONFIRMING_OBSERVATION: >
  Two owning contexts show different availability states for what is recorded as the same
  equipment at the same moment.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Share one piece of equipment across two companies or warehouses, take it out of service from one
  context, and compare what the other context sees at the same moment.
```

## G05-STOCK_MAINTENANCE-Q017

```yaml
QID: G05-STOCK_MAINTENANCE-Q017
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An out-of-service transition for equipment that had no stock committed to it at the time does
  not raise the same hold or notice as one that had live commitments, since nothing was actually
  at stake in the first case.
WHY_IT_MATTERS: >
  Uniform escalation regardless of actual exposure trains people to ignore the notice, including
  the times it matters.
DISCONFIRMING_OBSERVATION: >
  An out-of-service transition raises the identical hold or notice regardless of whether any stock
  was actually committed to that equipment at the time.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Take one piece of equipment with no committed stock out of service, and a second, comparable
  piece with committed stock out of service, and compare the resulting notices.
```

## G05-STOCK_MAINTENANCE-Q018

```yaml
QID: G05-STOCK_MAINTENANCE-Q018
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where equipment can run in a degraded or limited capacity rather than being fully out of
  service, that intermediate state is distinguishable, for stock already committed to it, from
  either fully available or fully out of service.
WHY_IT_MATTERS: >
  Collapsing a degraded state into a binary available/unavailable answer either overstates or
  understates what the equipment can actually still do.
DISCONFIRMING_OBSERVATION: >
  The system recognizes only two states, available or not available, with no way to represent or
  react to a degraded-capacity condition even where one is declared.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Declare equipment in a degraded or limited-capacity condition rather than fully out of service,
  and observe how stock committed to it is treated relative to the two extreme states.
```

## G05-STOCK_MAINTENANCE-Q019

```yaml
QID: G05-STOCK_MAINTENANCE-Q019
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A spare part consumed by a maintenance action against equipment is removed from stock through
  the same valuation path as any other stock consumption, not a parallel, unaccounted path.
WHY_IT_MATTERS: >
  A quantity that leaves stock with no corresponding cost movement understates the true cost of
  keeping equipment running.
DISCONFIRMING_OBSERVATION: >
  A part consumed for maintenance disappears from stock quantity with no corresponding
  valuation or cost movement recorded anywhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a maintenance action that consumes a stocked spare part, and inspect whether a
  valuation or cost movement accompanies the resulting quantity reduction.
```

## G05-STOCK_MAINTENANCE-Q020

```yaml
QID: G05-STOCK_MAINTENANCE-Q020
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The cost attributed to a spare part consumed for maintenance traces to that part's stock
  valuation at or near the moment of consumption, not a value fixed earlier or asserted without
  reference to actual stock cost.
WHY_IT_MATTERS: >
  A cost figure disconnected from actual stock valuation misstates the true cost of the
  maintenance action and of the equipment it kept running.
DISCONFIRMING_OBSERVATION: >
  The cost attributed to the consumed part does not trace to any stock valuation figure for that
  part at or near the consumption moment.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Consume a spare part for maintenance, then trace the cost attributed to that consumption back to
  the part's stock valuation at the time.
```

## G05-STOCK_MAINTENANCE-Q021

```yaml
QID: G05-STOCK_MAINTENANCE-Q021
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling or correcting a maintenance action that consumed a spare part reverses that part's
  stock quantity and valuation cleanly, rather than leaving the consumption standing as
  irreversible once recorded.
WHY_IT_MATTERS: >
  An uncorrectable consumption leaves stock permanently wrong for an event that never actually
  happened, or happened differently than recorded.
DISCONFIRMING_OBSERVATION: >
  Cancelling the maintenance action leaves the consumed quantity and its cost impact unreversed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a maintenance action that consumes a spare part, then cancel or correct that action, and
  inspect the part's resulting stock quantity and valuation.
```

## G05-STOCK_MAINTENANCE-Q022

```yaml
QID: G05-STOCK_MAINTENANCE-Q022
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A spare part under lot or serial control retains that specific identity in the record when
  consumed for maintenance, rather than the maintenance consumption bypassing whatever identity
  tracking an equivalent stock consumption would otherwise require.
WHY_IT_MATTERS: >
  Losing lot or serial identity on consumption breaks traceability for the very parts most likely
  to need it, such as those under recall or warranty tracking.
DISCONFIRMING_OBSERVATION: >
  A lot- or serial-controlled part consumed for maintenance leaves no traceable identity in the
  record of what was actually used.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consume a lot- or serial-controlled spare part for a maintenance action, and inspect the
  resulting record for that specific lot or serial identity.
```

## G05-STOCK_MAINTENANCE-Q023

```yaml
QID: G05-STOCK_MAINTENANCE-Q023
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A maintenance action recorded with no spare parts consumed leaves stock and valuation completely
  untouched, rather than generating a stock movement with no real substance behind it.
WHY_IT_MATTERS: >
  Phantom movements with no real quantity or value behind them clutter the stock record and make
  genuine movements harder to trust.
DISCONFIRMING_OBSERVATION: >
  A parts-free maintenance action still generates a stock movement record with nothing behind it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a maintenance action that consumes no spare parts, and inspect whether any stock movement
  was generated as a result.
```

## G05-STOCK_MAINTENANCE-Q024

```yaml
QID: G05-STOCK_MAINTENANCE-Q024
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When equipment shared across companies consumes a spare part for maintenance, an explicit
  ownership rule determines which company's stock and books absorb the cost, rather than it
  defaulting to whichever company happens to be recording the action.
WHY_IT_MATTERS: >
  Cost landing on whichever party happened to click the button, rather than on the party that
  should bear it, misstates each company's own books.
DISCONFIRMING_OBSERVATION: >
  The cost of a consumed part lands on a company determined only by which user or session recorded
  the action, not by an explicit ownership rule.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Consume a spare part for maintenance on equipment shared by two companies, recording the action
  from each company in turn, and compare which company absorbs the cost each time.
```

## G05-STOCK_MAINTENANCE-Q025

```yaml
QID: G05-STOCK_MAINTENANCE-Q025
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When two concurrent maintenance actions on different equipment both need the same spare part and
  stock on hand covers only one, a resolution rule decides which gets it rather than both being
  allowed to record consumption against the same limited quantity.
WHY_IT_MATTERS: >
  Letting both actions succeed against a quantity that only covers one drives stock negative for a
  part that both maintenance actions now falsely appear to have used.
DISCONFIRMING_OBSERVATION: >
  Both concurrent maintenance actions are allowed to record consumption of the same limited
  quantity, driving the part's stock negative with no resolution rule applied.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reduce a spare part's stock to a quantity that can satisfy only one of two concurrent maintenance
  actions on different equipment, and attempt to record both.
```

## G05-STOCK_MAINTENANCE-Q026

```yaml
QID: G05-STOCK_MAINTENANCE-Q026
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A part returned after a maintenance action, whether unused or replaced under core credit,
  retains a reference to the maintenance context it came from, rather than re-entering stock
  indistinguishably from any unrelated return.
WHY_IT_MATTERS: >
  Losing the link between a returned part and the maintenance event that produced it makes the
  return unexplainable later.
DISCONFIRMING_OBSERVATION: >
  A part returned after a maintenance action re-enters stock indistinguishably from any unrelated
  return, losing the link to the maintenance event that produced it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Return a part to stock following a maintenance action that consumed it, and inspect the
  resulting stock record for a reference back to that maintenance event.
```

## G05-STOCK_MAINTENANCE-Q027

```yaml
QID: G05-STOCK_MAINTENANCE-Q027
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a breakdown is logged against equipment after operations using it were already marked
  complete, a mechanism exists to flag those already-completed operations as suspect, rather than
  leaving them to stand permanently as clean.
WHY_IT_MATTERS: >
  Operations that were actually affected by a fault, but nothing ever revisits them, leave bad
  results permanently indistinguishable from good ones.
DISCONFIRMING_OBSERVATION: >
  A breakdown logged with a fault-onset time earlier than several completed operations produces no
  flag, hold, or review trigger on any of them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete several operations against a piece of equipment, then log a breakdown against that
  equipment with a fault-onset time earlier than those completions, and observe the effect.
```

## G05-STOCK_MAINTENANCE-Q028

```yaml
QID: G05-STOCK_MAINTENANCE-Q028
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A breakdown record can distinguish the actual fault-onset time from the moment the fault was
  discovered, so operations between the two can be identified retroactively.
WHY_IT_MATTERS: >
  Without an onset time distinct from discovery time, retroactively identifying which operations
  might be affected is impossible even in principle.
DISCONFIRMING_OBSERVATION: >
  There is no field or means to record an onset time distinct from discovery time, making
  retroactive identification of affected operations impossible even in principle.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Log a breakdown for equipment and attempt to record a fault-onset time earlier than the
  discovery time, and check whether the two are represented as distinct facts.
```

## G05-STOCK_MAINTENANCE-Q029

```yaml
QID: G05-STOCK_MAINTENANCE-Q029
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Reopening or annotating an already-completed operation because a later-discovered equipment
  fault implicates it is recorded as distinct from an ordinary correction, with the authority
  behind it identifiable.
WHY_IT_MATTERS: >
  A fault-driven reopening that looks like a routine edit hides the real reason the operation was
  ever revisited.
DISCONFIRMING_OBSERVATION: >
  Reopening a completed operation for this reason is indistinguishable, in the record, from any
  routine correction.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Reopen or annotate a completed operation because a later-discovered equipment fault implicates
  it, and compare the resulting record against an ordinary, unrelated correction.
```

## G05-STOCK_MAINTENANCE-Q030

```yaml
QID: G05-STOCK_MAINTENANCE-Q030
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Logging a breakdown for equipment with no completed operations in the relevant window does not
  retroactively flag operations on other equipment or outside that window.
WHY_IT_MATTERS: >
  An unbounded flagging response buries the genuinely affected operations in noise and wastes
  review effort on operations that were never at risk.
DISCONFIRMING_OBSERVATION: >
  Logging the breakdown flags operations on other equipment, or operations clearly outside the
  relevant time window.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Log a breakdown for a piece of equipment with unrelated equipment and out-of-window operations
  also present in the system, and observe what gets flagged.
```

## G05-STOCK_MAINTENANCE-Q031

```yaml
QID: G05-STOCK_MAINTENANCE-Q031
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A stock discrepancy recorded during a window later implicated by an equipment fault becomes
  cross-referenced to that fault once both are known, rather than the two facts remaining
  permanently unconnected in the record.
WHY_IT_MATTERS: >
  An unexplained stock discrepancy and its actual cause sitting unconnected in the system means
  neither record helps explain the other.
DISCONFIRMING_OBSERVATION: >
  A stock discrepancy from the affected window and the later-logged equipment fault exist in the
  system with no cross-reference connecting them even after both are known.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a stock discrepancy during a window later found to overlap a logged equipment fault, and
  check whether the two records become cross-referenced.
```

## G05-STOCK_MAINTENANCE-Q032

```yaml
QID: G05-STOCK_MAINTENANCE-Q032
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A breakdown discovered in one warehouse's context reaches operations run against the same
  shared equipment in another warehouse during the suspect window, rather than stopping at the
  boundary of wherever the discovery was logged.
WHY_IT_MATTERS: >
  A fault that only propagates within the warehouse that found it leaves identically affected
  operations elsewhere completely unreviewed.
DISCONFIRMING_OBSERVATION: >
  Operations run against the same equipment in a different warehouse during the suspect window are
  left untouched purely because the fault was logged from elsewhere.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Run operations against shared equipment from two different warehouses during the same window,
  log a breakdown for that equipment from one warehouse's context, and check the other's operations.
```

## G05-STOCK_MAINTENANCE-Q033

```yaml
QID: G05-STOCK_MAINTENANCE-Q033
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once a breakdown that caused operations to be flagged is itself resolved, that resolution
  attaches back to the flagged operations rather than leaving their flag open-ended with no
  closing reference.
WHY_IT_MATTERS: >
  A flag that never closes loses its meaning and either gets ignored or blocks work long after the
  underlying issue is fixed.
DISCONFIRMING_OBSERVATION: >
  Resolving the equipment fault has no observable effect on the status of operations that were
  flagged because of it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Resolve a logged breakdown that previously caused operations to be flagged, and check whether
  those operations' flagged status changes as a result.
```

## G05-STOCK_MAINTENANCE-Q034

```yaml
QID: G05-STOCK_MAINTENANCE-Q034
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A capacity or throughput figure used to plan operations against equipment accounts for scheduled
  maintenance windows already known at planning time, rather than assuming the equipment is
  available every hour it is nominally installed.
WHY_IT_MATTERS: >
  A capacity figure blind to known maintenance windows commits the business to work the equipment
  cannot actually perform.
DISCONFIRMING_OBSERVATION: >
  A known, already-scheduled maintenance window has no effect on the capacity figure offered at
  planning time for that same period.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Schedule a maintenance window for a piece of equipment, then request a capacity or throughput
  figure for that equipment covering the same period, and inspect the figure returned.
```

## G05-STOCK_MAINTENANCE-Q035

```yaml
QID: G05-STOCK_MAINTENANCE-Q035
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Adding or changing a maintenance window after operations were already planned into that time
  triggers a re-evaluation of the affected plans, rather than letting the planning figure go stale.
WHY_IT_MATTERS: >
  Plans left standing against a since-changed maintenance window are silently wrong from the
  moment the window changed.
DISCONFIRMING_OBSERVATION: >
  Changing a maintenance window after the fact produces no re-evaluation of operations already
  planned across that window.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Plan operations across a time window, then add or change a maintenance window overlapping that
  same period, and observe whether the existing plans are re-evaluated.
```

## G05-STOCK_MAINTENANCE-Q036

```yaml
QID: G05-STOCK_MAINTENANCE-Q036
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Capacity figures for equipment with no maintenance schedule configured and for otherwise
  identical equipment with a heavy maintenance schedule come out visibly different, rather than
  the two being treated identically.
WHY_IT_MATTERS: >
  If maintenance load has no visible effect on capacity at all, the capacity figure is not
  actually accounting for maintenance in any meaningful sense.
DISCONFIRMING_OBSERVATION: >
  Capacity figures for equipment with no maintenance schedule and equipment with a heavy one come
  out identical.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure one piece of equipment with no maintenance schedule and an otherwise identical piece
  with a heavy one, and compare the capacity figure produced for each.
```

## G05-STOCK_MAINTENANCE-Q037

```yaml
QID: G05-STOCK_MAINTENANCE-Q037
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A maintenance window added immediately before a planning attempt is reflected as a live check at
  the moment of planning, rather than the capacity figure being computed once and cached in a way
  that misses a window added shortly before.
WHY_IT_MATTERS: >
  A cached capacity figure that misses a just-added maintenance window plans work against
  equipment that everyone else already knows will be unavailable.
DISCONFIRMING_OBSERVATION: >
  A maintenance window added immediately after a capacity figure was produced has no effect on a
  second planning attempt made moments later.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Produce a capacity figure for equipment, immediately add a maintenance window over the same
  period, and request a second planning attempt moments later.
```

## G05-STOCK_MAINTENANCE-Q038

```yaml
QID: G05-STOCK_MAINTENANCE-Q038
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  For equipment shared across companies, a maintenance window scheduled by one company affects the
  capacity assumption computed for the other company sharing the same equipment.
WHY_IT_MATTERS: >
  A capacity figure that ignores a sharing party's own maintenance schedule commits equipment that
  is not actually going to be available.
DISCONFIRMING_OBSERVATION: >
  A maintenance window scheduled by one company against shared equipment has no effect on the
  capacity figure computed for the other company's plan.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Share equipment between two companies, schedule a maintenance window from one company's context,
  and request a capacity figure for the same equipment from the other company's context.
```

## G05-STOCK_MAINTENANCE-Q039

```yaml
QID: G05-STOCK_MAINTENANCE-Q039
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Forcing a plan through against a known, maintenance-derived capacity reduction is recorded as an
  override distinct from a plan made when no reduction applied.
WHY_IT_MATTERS: >
  An unrecorded override of a capacity warning removes the ability to know later that the plan was
  made in spite of a known constraint.
DISCONFIRMING_OBSERVATION: >
  A plan forced through against a known capacity reduction is stored identically to one made with
  no reduction in effect, with no trace of the override.
EXPECTED_SURFACE: S4,S6,S7
PRECONDITIONS: >
  Force a plan through against equipment carrying a known maintenance-derived capacity reduction,
  and compare the resulting record against a plan made with no reduction in effect.
```

## G05-STOCK_MAINTENANCE-Q040

```yaml
QID: G05-STOCK_MAINTENANCE-Q040
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Shared equipment has a declared owning company or warehouse distinct from the parties that use
  it, and a change made by a non-owning user is attributable as such, not indistinguishable from a
  change made by the owner.
WHY_IT_MATTERS: >
  Without a distinguishable owner, no party can be held accountable for changes made to a resource
  everyone shares.
DISCONFIRMING_OBSERVATION: >
  A user from a non-owning company or warehouse can change the shared equipment's core state with
  no distinguishable trace from a change made by the owner.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Change the core state of a piece of equipment shared across companies from both a non-owning and
  an owning context, and compare the resulting records.
```

## G05-STOCK_MAINTENANCE-Q041

```yaml
QID: G05-STOCK_MAINTENANCE-Q041
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A fault logged by one company or warehouse against shared equipment is visible to every other
  party sharing that equipment, rather than being scoped so another party continuing to operate
  against it cannot see it.
WHY_IT_MATTERS: >
  A party unaware of a fault another owner already knows about will keep using equipment believed
  faulty by someone else with equal claim to it.
DISCONFIRMING_OBSERVATION: >
  A fault logged by one owning context against shared equipment is not visible to another context
  that continues operating against the same equipment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Log a fault against shared equipment from one owning context, and check whether another context
  sharing that equipment can see the fault before continuing to operate it.
```

## G05-STOCK_MAINTENANCE-Q042

```yaml
QID: G05-STOCK_MAINTENANCE-Q042
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reassigning equipment from one warehouse to another resolves any open, in-flight commitment the
  originating warehouse held against it, rather than allowing the equipment to relocate while the
  original warehouse still shows live commitments referencing it.
WHY_IT_MATTERS: >
  A warehouse that still believes it has a live commitment against equipment that has physically
  moved elsewhere is working from a record that no longer matches reality.
DISCONFIRMING_OBSERVATION: >
  The equipment's location changes while the originating warehouse retains unresolved stock or
  operation commitments referencing it as if it were still there.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Establish live stock or operation commitments against equipment in one warehouse, relocate that
  equipment to another warehouse, and inspect the originating warehouse's commitments afterward.
```

## G05-STOCK_MAINTENANCE-Q043

```yaml
QID: G05-STOCK_MAINTENANCE-Q043
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a given piece of equipment is single-owner or shared across companies or warehouses is
  itself a determinable fact from the equipment's own record, not something that can only be
  inferred after the fact from where problems happen to show up.
WHY_IT_MATTERS: >
  If sharing status cannot be read from the record, every equipment issue must be investigated as
  though it might be a cross-boundary one, whether or not it actually is.
DISCONFIRMING_OBSERVATION: >
  There is no way to tell, from the record itself, whether a given piece of equipment is
  single-owner or shared.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Inspect the record of a piece of equipment known to be single-owner and of one known to be
  shared, and compare what each record itself discloses about its sharing status.
```

## G05-STOCK_MAINTENANCE-Q044

```yaml
QID: G05-STOCK_MAINTENANCE-Q044
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an equipment fault is identified as the explanation for a stock discrepancy, that causal
  link is itself a recorded, queryable fact within the system, not something that exists only in a
  conversation or a reviewer's memory outside it.
WHY_IT_MATTERS: >
  A causal explanation that lives only outside the system cannot be audited, searched, or relied
  on once the people who knew it have moved on.
DISCONFIRMING_OBSERVATION: >
  There is no field, reference, or link by which a stock discrepancy record and an equipment fault
  record can be connected within the system itself.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Identify an equipment fault as the explanation for a specific stock discrepancy, and attempt to
  record that causal connection within the system itself.
```

## G05-STOCK_MAINTENANCE-Q045

```yaml
QID: G05-STOCK_MAINTENANCE-Q045
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  More than one stock discrepancy can be linked to the same equipment fault without a second
  linkage displacing or overwriting the first.
WHY_IT_MATTERS: >
  A single equipment fault can plausibly explain several discrepancies at once; losing earlier
  links when a new one is added destroys evidence that was already correctly captured.
DISCONFIRMING_OBSERVATION: >
  Linking a second discrepancy to an already-linked equipment fault removes or overwrites the
  first discrepancy's link.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Link a first stock discrepancy to an equipment fault, then link a second, different discrepancy
  to the same fault, and check whether the first link still holds.
```

## G05-STOCK_MAINTENANCE-Q046

```yaml
QID: G05-STOCK_MAINTENANCE-Q046
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A stock discrepancy with no plausible equipment involvement can be closed without being forced
  through an equipment-fault linking step.
WHY_IT_MATTERS: >
  Forcing an irrelevant link onto every discrepancy manufactures false causal connections and
  wastes the time of whoever has to pick something to satisfy the requirement.
DISCONFIRMING_OBSERVATION: >
  Closing an unrelated stock discrepancy requires selecting some equipment-fault reference even
  when none applies.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to close a stock discrepancy that has no plausible connection to any equipment fault, and
  observe whether an equipment-fault reference is nonetheless required.
```

## G05-STOCK_MAINTENANCE-Q047

```yaml
QID: G05-STOCK_MAINTENANCE-Q047
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The authority to return equipment from an out-of-service or faulted state to serviceable is
  distinct from, and narrower than, the authority to merely operate the equipment day to day, and
  that distinction is enforced.
WHY_IT_MATTERS: >
  If anyone who can run the equipment can also declare it fixed, the fault-clearance step provides
  no real check on whether the equipment is actually safe to use again.
DISCONFIRMING_OBSERVATION: >
  Any user able to run an ordinary operation against the equipment is equally able to flip it back
  to serviceable, with no separate permission checked.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempt to return faulted equipment to serviceable status using an account that is only
  authorized for ordinary day-to-day operation of that equipment.
```

## G05-STOCK_MAINTENANCE-Q048

```yaml
QID: G05-STOCK_MAINTENANCE-Q048
MODULE: stock_maintenance
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Declaring equipment serviceable again automatically resumes, or at least clearly re-surfaces, the
  operations and stock commitments that were held or flagged during its out-of-service window,
  rather than leaving each one to require separate manual attention with nothing prompted by the
  declaration itself.
WHY_IT_MATTERS: >
  Held work that never gets revisited once the equipment is fixed sits stalled indefinitely with no
  trigger to remind anyone it is waiting.
DISCONFIRMING_OBSERVATION: >
  Declaring the equipment serviceable again has no observable effect on any operation or stock
  commitment that was held because of its earlier state.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Hold operations and stock commitments against equipment while it is out of service, then declare
  it serviceable again, and observe whether those held items are affected.
```

