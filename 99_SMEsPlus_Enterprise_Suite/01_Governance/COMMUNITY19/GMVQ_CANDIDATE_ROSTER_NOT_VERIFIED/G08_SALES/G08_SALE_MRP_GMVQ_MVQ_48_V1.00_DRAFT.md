# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_mrp Module Bridge MVQ Bank

**Document ID:** GMVQ-G08-SALE_MRP-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_mrp`
**Wave:** W2
**Author Cell:** P-S6 (GMVQ Question Factory — Wave W2 Acceleration, 25-Team Programme)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_mrp` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00, seam: a customer order line whose fulfilment is not stock but a
production run started because of that line. The base order's own invariants (quotation versus
confirmation, pricing, price-list precedence, invoicing policy, cancellation of a line with no
production involvement) belong to the `sale` base bank and are deliberately not re-asked here.
Neither does this bank re-ask a pure production-scheduling invariant that would hold with no
customer commitment attached — that ground belongs to the production capability itself. Every
question here fails only where a customer commitment and a production run must agree: the
committed date's derivation from real production lead time and what happens when that schedule
slips; a quantity changed after production has already started; cancellation with production
part-complete and who owns the resulting work; a run yielding less than ordered; one run serving
several orders and how a shortfall is allocated between them; a customer-specific configuration
orphaned by a later cancellation; a quality failure discovered after the customer was already
promised; an item substituted in production with no visible disclosure; and traceability from a
delivered unit back to the order and run that caused its production. No question here concerns
procurement of a purchased component — that ground is already covered on the procurement side of
the group by the existing `purchase_mrp` bank — and no question restates a `purchase_requisition`
or `purchase_requisition_sale`/`purchase_requisition_stock` invariant. Coverage spans business
capability, business rule, state transition, configuration dependency, role and permission,
exception path, cancellation, reversal, negative case, cross-module dependency, optional
behaviour, auditability, tenant/company boundary, concurrency and ordering, runtime reachability,
configuration reachability, and source/runtime contradiction potential.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material seam hypotheses; none was
  trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field.
- Every question passed the bridge removal test: if it would read equally well with no customer
  commitment in the picture, it was cut as belonging to the production capability alone.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$G07_DIR"/*.md | sort`
  was run against the existing `purchase_mrp`, `purchase_requisition_sale` and
  `purchase_requisition_stock` banks before authoring. Those banks cover the procurement-triggered
  side of the seam (demand consolidation, minimum-order rounding, requisition award authority,
  automatic-requisition review) — none of it is order-triggers-production ground, and no hypothesis
  or disconfirming observation below restates one of theirs with the direction reversed.
  `grep -h 'HYPOTHESIS' "$G08_DIR"/*.md | sort` returned nothing: no sibling G08 bank existed yet
  at authoring time.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_MRP-Q001

```yaml
QID: G08-SALE_MRP-Q001
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The delivery date committed to the customer on a line that triggers production is derived from
  that line's actual computed production lead time, not from a fixed default interval applied
  regardless of what is being produced.
WHY_IT_MATTERS: >
  A date that ignores the real production lead time promises delivery the business has no way to
  meet, and the gap is only discovered after the customer is already relying on it.
DISCONFIRMING_OBSERVATION: >
  Two confirmed lines for products with materially different production lead times receive an
  identical committed delivery date with no reference to either lead time.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm two customer order lines for made-to-order items whose configured production lead times
  differ substantially, then compare the committed delivery dates offered.
```

## G08-SALE_MRP-Q002

```yaml
QID: G08-SALE_MRP-Q002
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the production supplying a confirmed order line falls behind the schedule that produced the
  customer's committed date, that slip is surfaced as a visible exception rather than absorbed
  with no trace.
WHY_IT_MATTERS: >
  An unnoticed slip removes the only opportunity to warn the customer before the promised date is
  already missed.
DISCONFIRMING_OBSERVATION: >
  Production for a line is rescheduled to a materially later completion point and the order shows
  no flag, indicator, or altered state distinguishing it from an order still on schedule.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order line that triggers production, delay the resulting production run's schedule,
  and check the order for any resulting exception indicator.
```

## G08-SALE_MRP-Q003

```yaml
QID: G08-SALE_MRP-Q003
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Responsibility for telling the customer about a slipped commitment date is assignable to a
  specific role or person, not left as an implicit expectation with nobody recorded as owning it.
WHY_IT_MATTERS: >
  An exception with no owner is one that nobody is accountable for actually acting on before the
  customer is affected.
DISCONFIRMING_OBSERVATION: >
  A detected schedule slip on a customer-committed line produces no assignable owner, recipient,
  or task distinguishable from an ordinary status update.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Trigger a production slip on a line with a customer-committed date and inspect whether any owner
  or actionable assignment results.
```

## G08-SALE_MRP-Q004

```yaml
QID: G08-SALE_MRP-Q004
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A customer-facing committed date, once communicated, does not change to a less favorable value
  as a side effect of a production reschedule without a recorded reason and actor.
WHY_IT_MATTERS: >
  An unexplained date change is indistinguishable from carelessness and undermines every other
  date the business commits to afterward.
DISCONFIRMING_OBSERVATION: >
  The committed date on a confirmed line changes value following a production delay with no
  reason, actor, or timestamp captured against the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record the committed date on a confirmed line, delay the underlying production schedule, and
  inspect whatever record exists of the resulting date change.
```

## G08-SALE_MRP-Q005

```yaml
QID: G08-SALE_MRP-Q005
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where several production stages sit between confirmation and delivery, a delay introduced at any
  stage capable of affecting completion changes the customer-facing date, not only a delay at one
  nominally watched stage.
WHY_IT_MATTERS: >
  Watching the wrong stage lets a genuine delay run unnoticed while an irrelevant stage's
  punctuality is reported as reassuring.
DISCONFIRMING_OBSERVATION: >
  A delay introduced at a stage other than the one nominally tracked leaves the customer-facing
  date unchanged, while an equivalent delay at the tracked stage changes it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Introduce an equivalent delay at two different stages of a multi-stage production sequence
  feeding the same order line and compare the resulting customer-facing dates.
```

## G08-SALE_MRP-Q006

```yaml
QID: G08-SALE_MRP-Q006
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the customer is notified automatically of a slipped date, or notification is left to
  manual staff action, is a deliberate and discoverable configuration choice, not an unstated
  default that differs without explanation.
WHY_IT_MATTERS: >
  An unstated default risks alarming customers over routine reschedules in one setup while leaving
  genuinely late orders silently unnotified in another.
DISCONFIRMING_OBSERVATION: >
  Two comparably configured environments show different auto-notification behaviour on an
  identical slip event, with no discoverable setting accounting for the difference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Reproduce an identical schedule slip in two separately configured environments and compare
  whether customer notification occurs and whether a setting explains any difference.
```

## G08-SALE_MRP-Q007

```yaml
QID: G08-SALE_MRP-Q007
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reducing the ordered quantity after its production has already started leaves the excess
  already-committed production work visibly flagged, rather than silently discarded or silently
  kept with no reconciling record.
WHY_IT_MATTERS: >
  An unflagged excess after a quantity cut is either wasted work nobody accounts for or inventory
  quietly created with no order behind it.
DISCONFIRMING_OBSERVATION: >
  Reducing the quantity of a line whose production has already begun leaves no visible indicator
  distinguishing the excess already-produced or already-committed amount from the new, smaller
  requirement.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Start production against a confirmed line, then reduce the ordered quantity, and inspect whether
  the resulting excess is flagged anywhere.
```

## G08-SALE_MRP-Q008

```yaml
QID: G08-SALE_MRP-Q008
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Increasing the ordered quantity after production has started generates the additional production
  requirement needed to cover the increase rather than assuming the existing, smaller run already
  covers it.
WHY_IT_MATTERS: >
  Assuming an already-started run silently covers an increase leaves a real shortfall the customer
  will eventually feel with nothing in the record explaining why.
DISCONFIRMING_OBSERVATION: >
  Increasing a line's quantity after production has started leaves the underlying production
  requirement unchanged, with no additional requirement generated for the increase.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Start production against a confirmed line, increase the ordered quantity, and check whether
  additional production requirement results.
```

## G08-SALE_MRP-Q009

```yaml
QID: G08-SALE_MRP-Q009
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Changing a line's quantity after production has started requires an authority distinct from
  ordinary order editing, given that the change now carries a committed production cost that a
  simple quantity edit elsewhere would not.
WHY_IT_MATTERS: >
  Treating a post-start quantity change as an ordinary edit lets someone commit or waste
  production cost without anyone accountable for that specific decision.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary order-editing permission is able to change the quantity of a line
  whose production has already started with no additional approval invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with only ordinary order-edit permission, attempt to change the quantity of a line
  whose production has already started.
```

## G08-SALE_MRP-Q010

```yaml
QID: G08-SALE_MRP-Q010
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A quantity change on a line already in production is attributable to a specific recorded actor
  and reason, not left as an unexplained difference between the original and current requirement.
WHY_IT_MATTERS: >
  An unexplained quantity change on an in-progress run leaves no way to determine afterward
  whether it was a genuine customer request or an error.
DISCONFIRMING_OBSERVATION: >
  The quantity on a line already in production differs from its original value with no recorded
  actor or reason for the change anywhere in the order's history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the quantity of a line already in production and inspect the order's change history for
  the actor and reason.
```

## G08-SALE_MRP-Q011

```yaml
QID: G08-SALE_MRP-Q011
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a quantity reduction after production start leaves work in progress that cannot be reduced
  to match, the difference is treated as an exception requiring a decision, not silently absorbed
  into a cost or inventory figure with no visible trace.
WHY_IT_MATTERS: >
  An invisibly absorbed difference hides a real cost or inventory consequence from whoever is
  accountable for pricing or stock decisions.
DISCONFIRMING_OBSERVATION: >
  A quantity reduction leaving un-reducible work in progress produces a changed cost or inventory
  figure with nothing indicating that a decision point was reached or resolved.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Reduce a line's quantity after production has advanced past the point where the reduction can be
  matched, and inspect for any resulting decision record.
```

## G08-SALE_MRP-Q012

```yaml
QID: G08-SALE_MRP-Q012
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an order whose production is already part-complete leaves the work already performed
  in a state that is explicitly owned by someone, rather than left with no owning record at all.
WHY_IT_MATTERS: >
  Unowned partial work is cost nobody is accountable for recovering, reworking, or writing off.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order with production already part-complete leaves the resulting work in progress
  with no assigned owner, status, or disposition anywhere in the record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Advance production on a confirmed line partway, cancel the order, and inspect the resulting
  state of the partially completed work.
```

## G08-SALE_MRP-Q013

```yaml
QID: G08-SALE_MRP-Q013
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling an order with production part-complete distinguishes, in the resulting record,
  between work that can still be salvaged for another use and work that is specific enough to the
  cancelled order to be a loss.
WHY_IT_MATTERS: >
  Treating all partial work as equally lost, or equally salvageable, misstates the actual
  financial consequence of the cancellation.
DISCONFIRMING_OBSERVATION: >
  A cancellation with part-complete production produces a single undifferentiated write-off or
  disposition regardless of whether the partial work could plausibly serve another order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel an order with production part-complete on an item usable elsewhere, and separately on a
  customer-specific item, and compare the resulting disposition records.
```

## G08-SALE_MRP-Q014

```yaml
QID: G08-SALE_MRP-Q014
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Cancelling an order whose production has already started requires an authority distinct from
  cancelling one that has not yet entered production, given the committed cost already at stake.
WHY_IT_MATTERS: >
  Treating both cancellations identically lets a low-authority action discard a cost that a higher
  approval would ordinarily have to sign off on.
DISCONFIRMING_OBSERVATION: >
  A user whose authority permits cancelling an unstarted order is able to cancel an order with
  production already part-complete with no additional approval required.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with ordinary cancellation permission, attempt to cancel an order whose production has
  already started.
```

## G08-SALE_MRP-Q015

```yaml
QID: G08-SALE_MRP-Q015
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The decision to cancel an order with production part-complete is attributable to a specific
  recorded actor, distinguishing it from a cancellation of an order that never began production.
WHY_IT_MATTERS: >
  Without that distinction, nobody can later tell which cancellations actually destroyed committed
  work and which were free.
DISCONFIRMING_OBSERVATION: >
  The order's history records a cancellation with no way to tell, from the record itself, whether
  production had already started at the time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel an order with production part-complete and inspect whether the record distinguishes it
  from a pre-production cancellation.
```

## G08-SALE_MRP-Q016

```yaml
QID: G08-SALE_MRP-Q016
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether cancelling a part-complete order automatically halts the underlying production activity
  or leaves it running until manually stopped is a deliberate, discoverable configuration
  behaviour, not an unstated default.
WHY_IT_MATTERS: >
  An unstated default risks wasted further production on a cancelled order, or an unexpected halt
  disrupting other work sharing the same production activity.
DISCONFIRMING_OBSERVATION: >
  Two comparably configured environments behave differently on whether cancellation halts
  in-progress production, with no discoverable setting explaining the difference.
EXPECTED_SURFACE: S3,S7,S8
PRECONDITIONS: >
  Cancel a part-complete order in two separately configured environments and compare whether the
  underlying production activity halts.
```

## G08-SALE_MRP-Q017

```yaml
QID: G08-SALE_MRP-Q017
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the part-complete work belongs to a production run also serving other orders, cancelling
  one order does not remove or reduce the shared run's progress attributable to the other,
  still-active orders.
WHY_IT_MATTERS: >
  A cancellation bleeding into a shared run's other orders would delay or short unrelated
  customers who did nothing wrong.
DISCONFIRMING_OBSERVATION: >
  Cancelling one order sharing a production run with other still-active orders reduces the
  recorded progress or output attributable to those other orders.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cancel one order drawing from a production run that also serves at least one other still-active
  order, and inspect the effect on the other order's recorded progress.
```

## G08-SALE_MRP-Q018

```yaml
QID: G08-SALE_MRP-Q018
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a production run yields less than the quantity it was started to produce, the resulting
  shortfall against the order it was meant to satisfy is surfaced as a visible exception, not
  silently treated as the order having been fulfilled.
WHY_IT_MATTERS: >
  A silently accepted shortfall leaves the customer short without anyone deciding whether to
  re-run, part-ship, or renegotiate.
DISCONFIRMING_OBSERVATION: >
  A production run yielding less than its target quantity leaves the order it supplies marked as
  fully covered, with no shortfall indicator.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a production run at a quantity below its target, and inspect the state of the order it
  was intended to satisfy.
```

## G08-SALE_MRP-Q019

```yaml
QID: G08-SALE_MRP-Q019
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A yield shortfall on a run serving a specific order line offers a distinguishable path to either
  re-run the missing quantity or adjust the order, rather than only ever being resolvable by
  manually recreating the demand from scratch.
WHY_IT_MATTERS: >
  Forcing a manual recreation on every shortfall increases the chance a real shortfall is simply
  missed under time pressure.
DISCONFIRMING_OBSERVATION: >
  The only available response to a yield shortfall against an order line is to manually create
  replacement demand with no assisted path referencing the original shortfall.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Produce a yield shortfall against an order line and examine the available actions for resolving
  it.
```

## G08-SALE_MRP-Q020

```yaml
QID: G08-SALE_MRP-Q020
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The quantity actually delivered to the customer reflects what was actually produced and passed
  any required inspection, not the quantity that was originally ordered or originally planned.
WHY_IT_MATTERS: >
  Recording the planned quantity instead of the real one hides a shortfall inside a record that
  looks, on its face, complete.
DISCONFIRMING_OBSERVATION: >
  The delivered quantity recorded against the order matches the original order quantity even
  though the actual production yield fell short of it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Produce a yield below the ordered quantity, deliver what was actually produced, and check the
  delivered quantity recorded on the order.
```

## G08-SALE_MRP-Q021

```yaml
QID: G08-SALE_MRP-Q021
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a yield shortfall below a configured tolerance is treated as acceptable without
  escalation, versus always raising an exception regardless of size, is a deliberate, visible
  configuration setting.
WHY_IT_MATTERS: >
  An unstated default either buries small, immaterial shortfalls in escalations nobody needs, or
  lets a real shortfall slip through as within an assumed tolerance nobody actually set.
DISCONFIRMING_OBSERVATION: >
  Two comparably configured environments handle an identical small yield shortfall differently,
  with no discoverable tolerance setting explaining the difference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Reproduce an identical small yield shortfall in two separately configured environments and
  compare whether an exception is raised.
```

## G08-SALE_MRP-Q022

```yaml
QID: G08-SALE_MRP-Q022
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a yield shortfall affects a run serving several orders at once, the shortfall's impact on
  each contributing order is individually visible, not reported only as a single aggregate
  shortfall against the run.
WHY_IT_MATTERS: >
  An aggregate-only shortfall gives no basis for deciding which specific customer commitments are
  actually now at risk.
DISCONFIRMING_OBSERVATION: >
  A yield shortfall on a run serving several orders is reported only as one aggregate figure, with
  no visibility into how it affects any individual order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a yield shortfall on a run serving more than one order and inspect whether the impact on
  each individual order is visible.
```

## G08-SALE_MRP-Q023

```yaml
QID: G08-SALE_MRP-Q023
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When one production run's output falls short of the combined demand from several orders it was
  meant to satisfy, the available units are allocated among those orders by a defined, repeatable
  rule.
WHY_IT_MATTERS: >
  An undefined allocation means the same shortfall scenario could favor a different customer every
  time it happens, with no way to justify or predict who is short.
DISCONFIRMING_OBSERVATION: >
  Repeating an identical shortfall scenario against the same set of contributing orders produces a
  different allocation between them on separate occasions with no rule explaining the difference.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Run an identical shortfall scenario against the same set of orders sharing one production run
  more than once and compare the resulting allocations.
```

## G08-SALE_MRP-Q024

```yaml
QID: G08-SALE_MRP-Q024
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The allocation rule used when a shared run falls short is applied consistently regardless of the
  order in which the contributing orders happen to have been confirmed or entered.
WHY_IT_MATTERS: >
  An allocation that depends on entry order rather than a deliberate rule effectively rewards
  accidents of timing over any real business priority.
DISCONFIRMING_OBSERVATION: >
  Reordering the sequence in which otherwise identical contributing orders were entered changes
  which of them receives the shortfall under an identical shared-run shortfall.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create identical contributing orders in two different entry sequences against the same
  shared-run shortfall scenario and compare allocation outcomes.
```

## G08-SALE_MRP-Q025

```yaml
QID: G08-SALE_MRP-Q025
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether priority customers or priority orders receive preferential allocation from a shared
  run's shortfall is a deliberate, visible configuration behaviour, not an undocumented side
  effect of some unrelated setting.
WHY_IT_MATTERS: >
  An undocumented preferential effect makes it impossible to explain to a disadvantaged customer,
  or to a regulator, why they were the one left short.
DISCONFIRMING_OBSERVATION: >
  One order consistently receives preferential allocation from shared-run shortfalls with no
  discoverable priority setting or rule accounting for the preference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Create a shared-run shortfall scenario involving one flagged priority order among otherwise
  equivalent orders and inspect the resulting allocation and its stated basis.
```

## G08-SALE_MRP-Q026

```yaml
QID: G08-SALE_MRP-Q026
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When one of several orders sharing a production run is cancelled before the run completes, the
  units that would have gone to it are released to the remaining orders through a visible
  reallocation, not left assigned to a cancelled order indefinitely.
WHY_IT_MATTERS: >
  Units stranded against a cancelled order are units unavailable to fulfil real, still-active
  customer commitments for no reason.
DISCONFIRMING_OBSERVATION: >
  Cancelling one of several orders sharing an in-progress production run leaves its allotted units
  unavailable to the remaining, still-active orders even after the cancellation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel one order among several sharing an in-progress production run and check whether its
  allotted units become available to the others.
```

## G08-SALE_MRP-Q027

```yaml
QID: G08-SALE_MRP-Q027
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The specific orders contributing to a shared production run, and each one's share of its output,
  remain individually identifiable after the run completes, not merged into an undifferentiated
  pooled output.
WHY_IT_MATTERS: >
  Losing the individual breakdown after completion makes it impossible to later verify that each
  customer received what they were actually owed from that run.
DISCONFIRMING_OBSERVATION: >
  After a shared production run completes, there is no way to determine which orders contributed
  to it or what share of the output belongs to each.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a production run serving several orders and inspect whether each order's contribution
  and share remain identifiable afterward.
```

## G08-SALE_MRP-Q028

```yaml
QID: G08-SALE_MRP-Q028
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Deciding how a shared run's shortfall is allocated across competing customer orders is an action
  available to a role with visibility of all the affected orders, not something a single order's
  own staff can decide unilaterally against orders they cannot see.
WHY_IT_MATTERS: >
  Letting one order's handler decide the split unilaterally hands them power over other customers'
  commitments they have no visibility into.
DISCONFIRMING_OBSERVATION: >
  A staff member with access limited to a single one of the contributing orders is able to
  determine or change the allocation affecting the other orders they cannot see.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with access to only one of several orders sharing a run, attempt to influence the
  shortfall allocation affecting the others.
```

## G08-SALE_MRP-Q029

```yaml
QID: G08-SALE_MRP-Q029
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order for a customer-specific configuration is cancelled after production has already
  produced that configuration, the resulting inventory is flagged as not generally sellable,
  rather than returned to ordinary stock indistinguishable from standard items.
WHY_IT_MATTERS: >
  Silently treating customer-specific output as ordinary stock overstates what the business can
  actually resell and hides a real loss.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order for a customer-specific configuration after production leaves the resulting
  units recorded as ordinary, freely sellable stock with no flag noting their custom origin.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Produce a customer-specific configuration, cancel the order after production completes, and
  inspect how the resulting units are recorded.
```

## G08-SALE_MRP-Q030

```yaml
QID: G08-SALE_MRP-Q030
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Inventory left over from a cancelled customer-specific order remains traceable back to the order
  and customer it was originally produced for, even after being flagged as unsellable in the
  ordinary sense.
WHY_IT_MATTERS: >
  Losing that trace removes any basis for later deciding whether to write it off, salvage it, or
  attempt to recover cost from the customer.
DISCONFIRMING_OBSERVATION: >
  Unsellable inventory resulting from a cancelled customer-specific order can no longer be traced
  back to the order or customer that caused its production.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce and then orphan a customer-specific configuration through order cancellation, and
  attempt to trace the resulting inventory back to its originating order.
```

## G08-SALE_MRP-Q031

```yaml
QID: G08-SALE_MRP-Q031
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A financial write-off or disposition decision for unsellable customer-specific inventory is a
  distinct, visible action, not something that happens automatically and invisibly the moment the
  originating order is cancelled.
WHY_IT_MATTERS: >
  An automatic, invisible write-off removes the deliberate decision point where someone might
  instead choose to salvage, discount-sell, or pursue recovery from the customer.
DISCONFIRMING_OBSERVATION: >
  Cancelling the originating order automatically changes the inventory's value or status with no
  distinct, visible disposition action or record of one having occurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel an order for a customer-specific configuration after production and inspect whether any
  distinct disposition action is required or recorded.
```

## G08-SALE_MRP-Q032

```yaml
QID: G08-SALE_MRP-Q032
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a cancellation charge is applied to the customer when their cancellation leaves the
  business holding unsellable custom inventory is a deliberate, configurable business rule, not an
  inconsistent, ad hoc outcome.
WHY_IT_MATTERS: >
  An ad hoc outcome means the business either absorbs preventable losses or unpredictably charges
  customers with no consistent policy to point to.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical cancellations of customer-specific orders after production result in
  different cancellation-charge outcomes with no discoverable rule or setting explaining the
  difference.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Cancel two comparable customer-specific orders after production in the same environment and
  compare whether any cancellation charge is applied and why.
```

## G08-SALE_MRP-Q033

```yaml
QID: G08-SALE_MRP-Q033
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a customer-specific configuration was already partially delivered before the remainder of
  the order is cancelled, only the undelivered, still-in-production portion becomes unsellable
  inventory — the delivered portion is not double-counted as both delivered and available.
WHY_IT_MATTERS: >
  Double-counting an already-delivered portion overstates both what was shipped to the customer
  and what remains as recoverable stock.
DISCONFIRMING_OBSERVATION: >
  Cancelling the undelivered remainder of a partially delivered customer-specific order results in
  the already-delivered portion also appearing as available, unsellable, or otherwise uncommitted
  inventory.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially deliver a customer-specific order, cancel the remainder, and inspect whether the
  already-delivered portion is also reflected in the resulting inventory record.
```

## G08-SALE_MRP-Q034

```yaml
QID: G08-SALE_MRP-Q034
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a quality failure is discovered in production output already counted toward a customer's
  promised delivery, the promised commitment is revisited rather than left standing as though the
  failed output were still going to fulfil it.
WHY_IT_MATTERS: >
  An unrevisited commitment lets a promise stand on output that no longer exists to deliver,
  guaranteeing a broken promise discovered only at the last moment.
DISCONFIRMING_OBSERVATION: >
  A quality failure is recorded against output already counted toward a customer's committed
  delivery, and the commitment itself shows no resulting change or flag.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a quality failure against production output already counted toward a customer's
  committed delivery and inspect the resulting state of that commitment.
```

## G08-SALE_MRP-Q035

```yaml
QID: G08-SALE_MRP-Q035
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a production order backing an already-communicated customer delivery commitment is
  rescheduled to a later date, that reschedule generates a discoverable exception routed to a role
  able to manage the customer relationship, not merely an internal production log entry.
WHY_IT_MATTERS: >
  A production delay with no routed customer-facing exception leaves the customer relationship
  consequence entirely to chance.
DISCONFIRMING_OBSERVATION: >
  A production order backing an already-communicated delivery commitment is rescheduled to a later
  date, and no exception, alert, or assigned action toward the customer-facing commitment results.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Communicate a delivery commitment to a customer, then reschedule the backing production order to
  a later date, and inspect whether any customer-facing exception results.
```

## G08-SALE_MRP-Q036

```yaml
QID: G08-SALE_MRP-Q036
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Output that has failed quality inspection is not counted as available to satisfy a customer
  commitment, even temporarily, while its disposition is still being decided.
WHY_IT_MATTERS: >
  Temporarily counting failed output as available risks it actually being shipped before anyone
  finishes deciding it should not be.
DISCONFIRMING_OBSERVATION: >
  Output recorded as having failed quality inspection still appears as available or reserved
  against a customer's order while its final disposition remains undecided.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Fail a unit of production output at inspection and check whether it still appears available or
  reserved against the order it was intended for.
```

## G08-SALE_MRP-Q037

```yaml
QID: G08-SALE_MRP-Q037
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a sale-linked production order's bill of materials is changed after production has already
  started, the components already consumed before the change remain recorded against the bill of
  materials version in effect when they were actually consumed, not silently re-attributed to the
  new version.
WHY_IT_MATTERS: >
  Re-attributing already-consumed components to a version they were never actually consumed under
  would misstate the true cost and composition of what was actually produced.
DISCONFIRMING_OBSERVATION: >
  After a mid-production bill of materials change, the components consumed before the change show
  as consumed under the new version rather than the one in effect at the time.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Start production against one bill of materials version, consume some components, change the
  bill of materials version, then inspect which version the already-consumed components are
  recorded against.
```

## G08-SALE_MRP-Q038

```yaml
QID: G08-SALE_MRP-Q038
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a quality failure affects output shared across several customer orders, each affected
  order's exposure is individually visible, not reported only as a single aggregate quality event.
WHY_IT_MATTERS: >
  An aggregate-only report gives no basis for deciding which specific customer commitments are now
  actually at risk of failing.
DISCONFIRMING_OBSERVATION: >
  A quality failure affecting output shared across several orders is recorded only as one
  aggregate event, with no visibility into which individual orders are affected.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Fail a batch of output shared across several orders at inspection and inspect whether each
  affected order's exposure is individually visible.
```

## G08-SALE_MRP-Q039

```yaml
QID: G08-SALE_MRP-Q039
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Substituting the item actually produced for an order line, in place of the item originally
  specified, is recorded as a distinguishable event on that order, not merged invisibly into the
  original line as though nothing changed.
WHY_IT_MATTERS: >
  An invisible substitution leaves nobody able to answer, later, what the customer actually
  received versus what they ordered.
DISCONFIRMING_OBSERVATION: >
  An order line's produced item is substituted for a different one, and the order shows the
  original specification with no record that a substitution occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Substitute the item actually produced for an order line and inspect the order record for any
  indication of the substitution.
```

## G08-SALE_MRP-Q040

```yaml
QID: G08-SALE_MRP-Q040
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Substituting the produced item on a confirmed customer order line requires an authority distinct
  from ordinary production scheduling, given that it changes what the customer will actually
  receive.
WHY_IT_MATTERS: >
  Treating a substitution as a routine scheduling action lets it happen with no one accountable
  for the commercial and disclosure consequence to the customer.
DISCONFIRMING_OBSERVATION: >
  A user whose authority covers only ordinary production scheduling is able to substitute the item
  on a confirmed customer order line with no additional approval invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a user with only ordinary production-scheduling permission, attempt to substitute the
  produced item for a confirmed order line.
```

## G08-SALE_MRP-Q041

```yaml
QID: G08-SALE_MRP-Q041
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a substitution on a customer order line requires customer notification or acknowledgement
  before proceeding is a deliberate, configurable rule, distinguishing customer-facing lines from
  ordinary internal replenishment substitutions.
WHY_IT_MATTERS: >
  Treating a customer commitment the same as an internal stock substitution risks the customer
  never being told their order changed.
DISCONFIRMING_OBSERVATION: >
  A substitution on a confirmed customer order line proceeds through exactly the same path, with
  the same lack of notification requirement, as a purely internal replenishment substitution.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Compare the substitution path for a confirmed customer order line against the substitution path
  for an internal replenishment case in the same environment.
```

## G08-SALE_MRP-Q042

```yaml
QID: G08-SALE_MRP-Q042
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The record of a substitution on a delivered order line persists after delivery, remaining
  visible on any later inspection of that order, rather than being available only transiently at
  the moment the substitution occurred.
WHY_IT_MATTERS: >
  A substitution record that disappears after delivery removes the ability to investigate a later
  customer complaint about receiving the wrong item.
DISCONFIRMING_OBSERVATION: >
  A substitution recorded at the time of production is no longer visible when the same order is
  inspected after delivery has completed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Substitute the produced item for an order line, deliver the order, and inspect the order for the
  substitution record after delivery.
```

## G08-SALE_MRP-Q043

```yaml
QID: G08-SALE_MRP-Q043
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the substituted item differs in price or cost from the one originally specified, the
  order's pricing or margin reflects the item actually delivered, not the originally specified
  item that was never produced.
WHY_IT_MATTERS: >
  Pricing or margin based on a phantom item that was never delivered misstates the real commercial
  outcome of the order.
DISCONFIRMING_OBSERVATION: >
  An order line's price or recorded margin remains based on the originally specified item even
  after a substitution to a differently priced or differently costed item.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Substitute the produced item for an order line with a differently priced item, and inspect the
  resulting order pricing or margin figure.
```

## G08-SALE_MRP-Q044

```yaml
QID: G08-SALE_MRP-Q044
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A specific delivered unit produced to satisfy a customer order can be traced back to that order,
  and to the specific production activity that made it, after delivery has completed.
WHY_IT_MATTERS: >
  Losing that trace after delivery removes the ability to investigate a later quality complaint or
  recall back to its actual production origin.
DISCONFIRMING_OBSERVATION: >
  A delivered unit that was produced specifically to satisfy an order cannot be traced back to
  that order or its producing activity once delivery is complete.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver a unit produced for a specific order and attempt to trace it back to both the order and
  the production activity that made it.
```

## G08-SALE_MRP-Q045

```yaml
QID: G08-SALE_MRP-Q045
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a delivered unit was drawn from a production run shared across several orders, its trace
  correctly identifies which run it came from even though the run served more than one order.
WHY_IT_MATTERS: >
  A trace that cannot distinguish a shared run's individual output makes it impossible to isolate
  which customers are affected by a problem found in one part of that run.
DISCONFIRMING_OBSERVATION: >
  A delivered unit's trace back to a shared production run cannot establish which portion of that
  run's output it actually came from.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver a unit from a production run that also served other orders and attempt to trace it to
  the specific run and its share of that run's output.
```

## G08-SALE_MRP-Q046

```yaml
QID: G08-SALE_MRP-Q046
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a production run yields fewer usable units than a linked sale commitment requires, that
  shortfall produces a discoverable exception against the commitment, rather than the commitment
  silently remaining marked as fully sourced from that run.
WHY_IT_MATTERS: >
  A silent shortfall leaves a real under-delivery risk undetected until the customer discovers it
  at the point of delivery.
DISCONFIRMING_OBSERVATION: >
  A production run yielding fewer usable units than its linked sale commitment requires still
  shows that commitment as fully sourced, with no exception recorded.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Run production that yields fewer usable units than a linked sale commitment requires, and check
  whether the shortfall produces a discoverable exception against that commitment.
```

## G08-SALE_MRP-Q047

```yaml
QID: G08-SALE_MRP-Q047
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The trace from a delivered unit back to its originating order survives the order later being
  archived, closed, or otherwise made inactive.
WHY_IT_MATTERS: >
  A trace that breaks once the order is archived defeats the purpose of keeping a trace at all,
  since most real investigations happen well after an order has closed.
DISCONFIRMING_OBSERVATION: >
  A delivered unit's trace back to its originating order no longer resolves once that order has
  been archived or closed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deliver a unit against an order, archive or close that order, and attempt to trace the unit back
  to it afterward.
```

## G08-SALE_MRP-Q048

```yaml
QID: G08-SALE_MRP-Q048
MODULE: sale_mrp
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where lot or batch traceability applies, the specific component lots actually consumed into a
  finished production output can be traced forward from that output's own record, not only
  discoverable by checking each component lot's usage individually.
WHY_IT_MATTERS: >
  Without that forward trace, a recall triggered by a defective component lot has no reliable way
  to identify which finished outputs actually contain it.
DISCONFIRMING_OBSERVATION: >
  A finished production output's own record cannot be used to identify which component lots were
  actually consumed into it, even where lot traceability is otherwise enabled.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Produce a finished output from components under lot traceability, then attempt to identify, from
  the finished output's own record, which component lots were consumed into it.
```
