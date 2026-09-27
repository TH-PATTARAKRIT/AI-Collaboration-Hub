# SMEsPlus ENTERPRISE SUITE
## GMVQ — G11 EVENTS / event_booth_sale Module Adversarial MVQ Bank

**Document ID:** GMVQ-G11-EVENT_BOOTH_SALE-MVQ50-V1.00
**Group:** G11 EVENTS
**Module Metadata:** `event_booth_sale`
**Wave:** W2
**Author Cell:** P-E3 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 50 = 105
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded
**Date authored:** 2026-09-27

## Purpose

This bank authors the module-specific MVQ set for `event_booth_sale` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00, seam: an individually identified, non-fungible booth (the
`event_booth` domain) sold through a commercial order (the sales-document domain). Every question
was tested against the bridge rule of GMVQ_BRIDGE_MODULE_RULE_V1.00 §2: if the question would
still make sense with the commercial-order capability removed and the booth simply allocated
directly, it was cut. None restates an `event_booth` allocation-lifecycle invariant that holds
with no order in the picture (that ground belongs to the `event_booth` bank), and none restates a
plain commercial-order invariant with this module's name attached. The bank covers: order
confirmation against allocation, in both directions; what document and for how long holds a
specific booth during quotation; specific-booth versus category entitlement and when the specific
booth is decided; a changed booth reference after confirmation; price by category versus by named
booth; cancellation against physical occupancy and the resulting refund policy; revenue
recognition timing; a sale against a withdrawn booth; duplicate sale of one named booth; invoicing
of attached services; and the ordering customer differing from the exhibiting company.

Sibling-distinction note (routing brief, Wave W2): because a booth is a specific, individually
identified space rather than an interchangeable seat, this bank's ground is built around the
consequences of that identity — which specific booth a customer is entitled to, whether a booth
reference can silently change, and whether a category entitlement is ever conflated with a
specific-booth one (Q003, Q009, Q048, Q049 address this directly). This is structurally different
ground from a fungible-seat sale (`event_sale`), where the seam is a quantity against a capacity
pool rather than an identity against a named resource.

The question text is source-neutral and does not expose vendor names, model names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE: event_booth_sale`
appears only in the structured metadata field, never inside question text. This is a bridge module
per §6 of GMVQ_BRIDGE_MODULE_RULE_V1.00 (one layer only: the seam itself); `LAYER` is therefore
omitted from every question in this bank, consistent with the sibling bridge-bank precedent on
disk (`G07_PURCHASE_REQUISITION_SALE`, 0 LAYER occurrences).

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 50 questions exist because they test 50 distinct material hypotheses at the seam.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- CLEAN ROOM: authored from generic business/behavioural knowledge of commercial space sales.
  No vendor or reference source tree was opened to produce this bank.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam between a
  commercial order and the booth allocation it sells. None restates an `event_booth` structural or
  lifecycle invariant that holds with no order present, and none is a generic sales-order invariant
  restated with this module's name attached.
- Mandatory pre-authoring sibling check performed per GMVQ_BRIDGE_MODULE_RULE_V1.00 §5:
  `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G11_EVENTS/*.md | sort` was run before authoring.
  DISCLOSURE: at authoring time, `01_QUESTION_BANKS/G11_EVENTS/` did not yet exist on disk — this
  cell's two banks are the first committed to that path, and no `event_sale` bank content was
  available to check against. The identified-versus-fungible distinction from `event_sale` was
  ensured by construction against the routing brief, not by a completed sibling-overlap check;
  re-verify once `event_sale` is committed. Recorded as a DEVIATION for RED TEAM / Reconciler
  attention, per §7 of the deviation register discipline.
- POST-AUTHORING SUPPLEMENTARY CHECK: other cells committed the remaining G11_EVENTS banks (including `event_sale` and the base `event` bank) to disk during this same session. `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G11_EVENTS/*.md` and a targeted scan for `booth`/`exhibitor`/`exhibition` leakage into sibling banks were re-run after they landed: no sibling bank uses booth/exhibitor language, and `event_sale`'s ground (seat/registration quantity, attendee naming, capacity consumption timing) does not overlap this bank's specific-named-booth ground. The DEVIATION above is superseded by this supplementary check for the siblings that exist as of this authoring session; it still applies to any G11_EVENTS bank committed after this one.
- This bank was also checked against its own sibling `event_booth` (authored in the same session,
  data above): no question here restates an `event_booth`-only structural or lifecycle hypothesis;
  every question requires the commercial-order layer to make sense.

## G11-EVENT_BOOTH_SALE-Q001

```yaml
QID: G11-EVENT_BOOTH_SALE-Q001
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A commercial order for a booth can be confirmed without the underlying booth actually
  being allocated, and if that is possible, the order does not represent itself as
  fulfilled while no space has actually been reserved.
WHY_IT_MATTERS: >
  A customer who believes their space is secured the moment their order is confirmed can
  arrive to find no booth was ever actually held for them.
DISCONFIRMING_OBSERVATION: >
  An order for a booth reaches a confirmed state and nothing in the order distinguishes
  that from a state where the booth allocation has actually been completed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm a commercial order for a booth without completing the corresponding allocation
  step, and inspect what the order's status communicates.
```

## G11-EVENT_BOOTH_SALE-Q002

```yaml
QID: G11-EVENT_BOOTH_SALE-Q002
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A booth can be allocated to an exhibitor with no commercial order behind it at all, and
  that state is distinguishable from one where an order exists and has simply not yet been
  paid or confirmed.
WHY_IT_MATTERS: >
  Floor staff and finance need to tell apart a space held for a legitimate non-commercial
  reason from one that quietly bypassed the sales process entirely.
DISCONFIRMING_OBSERVATION: >
  A booth shows as allocated with no way to determine whether any commercial order exists
  behind it, or what that order's status is.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Allocate a booth directly with no order reference, then attempt to determine, from the
  allocation alone, whether a commercial order exists behind it.
```

## G11-EVENT_BOOTH_SALE-Q003

```yaml
QID: G11-EVENT_BOOTH_SALE-Q003
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An order line for a booth sold as a specific named space carries a reference to that
  specific booth's identity, not merely a category and a quantity that leaves which
  physical booth unresolved.
WHY_IT_MATTERS: >
  A customer who bought a specific space needs a document that actually says which one,
  not a tally that still requires someone to decide later.
DISCONFIRMING_OBSERVATION: >
  An order line sold against a specific named booth records only a category and quantity,
  with no reference identifying which physical booth was sold.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Sell a specific named booth on an order line and inspect whether the order line
  references that booth's identity or only a category and quantity.
```

## G11-EVENT_BOOTH_SALE-Q004

```yaml
QID: G11-EVENT_BOOTH_SALE-Q004
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  While an order is still only a quotation, a specific booth referenced on it is held
  against being allocated to someone else for a bounded, known period, rather than either
  not being held at all or being held indefinitely with no visible limit.
WHY_IT_MATTERS: >
  An unbounded informal hold silently locks up sellable space, while no hold at all means
  a quoted customer can lose the exact booth they were quoted with no warning.
DISCONFIRMING_OBSERVATION: >
  A specific booth referenced by an open quotation is either allocated to a different
  customer with no conflict raised, or remains held with no visible time limit on that
  hold.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a quotation referencing a specific named booth and observe whether, and for how
  long, that booth is held against competing allocation.
```

## G11-EVENT_BOOTH_SALE-Q005

```yaml
QID: G11-EVENT_BOOTH_SALE-Q005
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If a time-bounded hold on a quoted booth exists, its duration is a visible, configurable
  setting rather than a fixed assumption with no way to inspect or adjust it.
WHY_IT_MATTERS: >
  A hold duration nobody can see or adjust cannot be tuned to the sales cycle of a
  specific event without someone reverse-engineering it first.
DISCONFIRMING_OBSERVATION: >
  A quoted booth's hold expires or persists according to a duration that cannot be located
  or adjusted anywhere in configuration.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Locate the configuration governing how long a quoted booth is held, if any such hold
  exists.
```

## G11-EVENT_BOOTH_SALE-Q006

```yaml
QID: G11-EVENT_BOOTH_SALE-Q006
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two separate orders from two different customers cannot both reach a confirmed state
  referencing the same specific named booth; one is blocked or resolved before both are
  allowed to stand.
WHY_IT_MATTERS: >
  Two paying customers both confirmed against the same physical space is the exact
  commercial failure the whole booth-sale capability exists to prevent.
DISCONFIRMING_OBSERVATION: >
  Two separate orders, each referencing the same specific named booth, both reach a
  confirmed state at the same time.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit two separate orders referencing the same specific named booth in close succession
  and attempt to confirm both.
```

## G11-EVENT_BOOTH_SALE-Q007

```yaml
QID: G11-EVENT_BOOTH_SALE-Q007
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing an order line to reference a different booth after the order was already
  confirmed releases the previously referenced booth as part of that same change, rather
  than leaving the old booth still allocated alongside the new one.
WHY_IT_MATTERS: >
  A silent double allocation left behind by a booth swap wastes space nobody realizes is
  still being held.
DISCONFIRMING_OBSERVATION: >
  An order line's booth reference is changed after confirmation and the previously
  referenced booth remains allocated with no release recorded.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm an order referencing one specific booth, then change the order line to reference
  a different booth, and check the state of the original booth.
```

## G11-EVENT_BOOTH_SALE-Q008

```yaml
QID: G11-EVENT_BOOTH_SALE-Q008
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When price is defined only at the category level but the customer is entitled to a
  specific named booth whose attributes differ from others in that category, the resulting
  mismatch between what was priced and what was delivered is visible to whoever reviews
  the order, not silently absorbed.
WHY_IT_MATTERS: >
  A customer paying a category price for a booth with materially different attributes than
  the category average is a pricing discrepancy someone should be able to see and decide
  about.
DISCONFIRMING_OBSERVATION: >
  A specific named booth with attributes differing from its category is sold at the plain
  category price with no indication anywhere that the two might not match.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Sell a specific named booth whose attributes differ materially from its category's
  typical booth, priced at the category rate, and check whether that is visible anywhere
  on the order.
```

## G11-EVENT_BOOTH_SALE-Q009

```yaml
QID: G11-EVENT_BOOTH_SALE-Q009
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When what was actually sold is a category rather than a specific booth, there is a
  defined document and moment at which the specific named booth the customer will occupy
  is decided, and that decision is recorded somewhere both sides can see.
WHY_IT_MATTERS: >
  Without a defined moment and record, a category-based sale can drift all the way to the
  event date with nobody having actually decided, or recorded, which booth the customer
  gets.
DISCONFIRMING_OBSERVATION: >
  A category-based order reaches the event with no record of when, or by whom, the
  specific named booth was decided for that customer.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Sell a booth by category rather than by specific booth and trace forward to find the
  document and moment recording which specific booth was ultimately assigned.
```

## G11-EVENT_BOOTH_SALE-Q010

```yaml
QID: G11-EVENT_BOOTH_SALE-Q010
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an order for a booth that is already occupied, physically in use at the
  event, does not silently release that booth as if it were still simply reserved, sight
  unseen, and unoccupied.
WHY_IT_MATTERS: >
  Releasing a physically occupied booth back into the available pool while someone is
  standing in it invites a second sale of space that is not actually free.
DISCONFIRMING_OBSERVATION: >
  An order for a booth already occupied at the event is cancelled and the booth is
  released to the available pool with no check against its physical occupancy.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Mark a booth as occupied at the event, then cancel the order behind it, and check
  whether the booth is released without regard to that occupancy.
```

## G11-EVENT_BOOTH_SALE-Q011

```yaml
QID: G11-EVENT_BOOTH_SALE-Q011
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The refund or cancellation policy applied to a physical booth allocation that cannot be
  resold on short notice is a distinct, separately configurable policy from whatever
  generic cancellation rule applies to an ordinary order.
WHY_IT_MATTERS: >
  Applying a generic refund rule meant for resellable goods or services to a specific
  physical space that cannot be resold late exposes the business to refunding money for
  space it can no longer sell to anyone else.
DISCONFIRMING_OBSERVATION: >
  A booth order's cancellation is processed under the same refund rule as an ordinary
  resellable item, with no distinct policy accounting for the booth's non-resellable,
  physically fixed nature.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Locate the refund policy applied to a cancelled booth order and compare it to the policy
  applied to a cancelled order for an ordinary resellable item.
```

## G11-EVENT_BOOTH_SALE-Q012

```yaml
QID: G11-EVENT_BOOTH_SALE-Q012
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where the refund policy on a booth cancellation depends on how close to the event date
  the cancellation happens, that proximity is computed consistently against the event's
  actual current date, not against a date that could be stale if the event was
  rescheduled.
WHY_IT_MATTERS: >
  A refund decision computed against a stale event date after a reschedule can grant or
  deny a refund based on a deadline that no longer reflects reality.
DISCONFIRMING_OBSERVATION: >
  A booth order's refund eligibility is computed against the event's original date after
  the event has been rescheduled to a different date.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reschedule an event's date, then cancel a booth order originally placed against the
  earlier date, and check which date the refund policy is evaluated against.
```

## G11-EVENT_BOOTH_SALE-Q013

```yaml
QID: G11-EVENT_BOOTH_SALE-Q013
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Whether revenue from a booth sale is recognised at the moment of sale or deferred until
  the event date is a deliberate, documented choice, and is applied consistently to every
  booth sale rather than varying by which path the sale happened to take.
WHY_IT_MATTERS: >
  An accidental mix of recognition timing across otherwise identical booth sales misstates
  the business's revenue position in whichever period the inconsistency lands.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical booth sales recognise revenue at different points in time, with
  no documented reason distinguishing them.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Compare the revenue recognition timing of two booth sales made through different paths
  or at different times relative to the same event.
```

## G11-EVENT_BOOTH_SALE-Q014

```yaml
QID: G11-EVENT_BOOTH_SALE-Q014
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If booth-sale revenue recognition timing differs from the recognition timing used for
  other products or services sold on the same platform, that difference is an intentional,
  documented exception rather than an unnoticed inconsistency between two unrelated
  defaults.
WHY_IT_MATTERS: >
  An unnoticed special case in revenue timing is the kind of discrepancy that only
  surfaces during an audit, at the worst possible time to explain it.
DISCONFIRMING_OBSERVATION: >
  Booth-sale revenue is recognised at a different point than the platform's general
  product or service revenue recognition rule, with nothing documenting that as an
  intended exception.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Compare the revenue recognition timing configured for booth sales against the general
  recognition timing configured for other sales.
```

## G11-EVENT_BOOTH_SALE-Q015

```yaml
QID: G11-EVENT_BOOTH_SALE-Q015
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order cannot be completed selling a booth that has already been withdrawn; the sale
  is blocked at or before confirmation rather than proceeding to reference a booth that no
  longer exists on the floor.
WHY_IT_MATTERS: >
  A completed sale of space that has already been withdrawn leaves a paying customer
  holding a document for a booth that will never be there.
DISCONFIRMING_OBSERVATION: >
  An order referencing a booth that was withdrawn before confirmation is nonetheless
  confirmed, invoiced, or otherwise treated as a completed sale.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Withdraw a booth that is referenced by an open, unconfirmed order, then attempt to
  confirm that order.
```

## G11-EVENT_BOOTH_SALE-Q016

```yaml
QID: G11-EVENT_BOOTH_SALE-Q016
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a booth already sold and allocated is subsequently withdrawn, the commercial order
  behind it is put into a state requiring resolution, credit, rebooking, or cancellation,
  rather than remaining exactly as it was as if nothing had happened to the booth it paid
  for.
WHY_IT_MATTERS: >
  An order that still looks fully satisfied after its booth was withdrawn hides a
  commitment the business can no longer honour from everyone who would need to act on it.
DISCONFIRMING_OBSERVATION: >
  A booth allocated under a confirmed, invoiced order is withdrawn, and the order remains
  in its original satisfied-looking state with nothing flagging the need for resolution.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Withdraw a booth already sold and allocated under a confirmed order, and check the
  resulting state of that order.
```

## G11-EVENT_BOOTH_SALE-Q017

```yaml
QID: G11-EVENT_BOOTH_SALE-Q017
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two confirmed orders cannot both reference the same specific named booth as sold; this
  is prevented structurally rather than being something only found later by manually
  comparing orders against each other.
WHY_IT_MATTERS: >
  Relying on manual comparison to catch a double sale means it is only ever caught after
  both customers have already been told the space is theirs.
DISCONFIRMING_OBSERVATION: >
  Two confirmed orders exist, each referencing the same specific named booth as sold,
  discoverable only by manually cross-checking the orders.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to confirm a second order referencing a specific named booth already sold and
  confirmed on a first order.
```

## G11-EVENT_BOOTH_SALE-Q018

```yaml
QID: G11-EVENT_BOOTH_SALE-Q018
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The party who places and pays for a booth order and the party who actually exhibits in
  that booth are modeled as potentially distinct roles, not collapsed into an assumption
  that the payer and the occupant are always the same entity.
WHY_IT_MATTERS: >
  A sponsor, agency, or parent company frequently pays for space that a different
  exhibiting company occupies, and losing that distinction misattributes both the
  commercial relationship and who is actually on the floor.
DISCONFIRMING_OBSERVATION: >
  An order for a booth provides no way to record an exhibiting company different from the
  customer who placed and paid for the order.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Place a booth order where the paying customer differs from the intended exhibiting
  company and check whether both roles can be recorded distinctly.
```

## G11-EVENT_BOOTH_SALE-Q019

```yaml
QID: G11-EVENT_BOOTH_SALE-Q019
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the paying customer and the exhibiting company differ, who is authorised to change
  or cancel the booth allocation is a defined rule, not left to whichever of the two
  parties happens to make the request first.
WHY_IT_MATTERS: >
  An undefined authority split between payer and occupant invites a booth to be cancelled
  or changed by a party the other side never expected to have that power.
DISCONFIRMING_OBSERVATION: >
  Both the paying customer and a distinct exhibiting company can independently change or
  cancel the same booth allocation with no defined rule governing which one's action
  prevails.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  With a paying customer and a distinct exhibiting company both recorded against one booth
  order, have each attempt to change or cancel the allocation.
```

## G11-EVENT_BOOTH_SALE-Q020

```yaml
QID: G11-EVENT_BOOTH_SALE-Q020
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Services attached to a booth are invoiced through the same commercial document path as
  the booth itself, consistently, regardless of whether the service was included with the
  original order or added afterward.
WHY_IT_MATTERS: >
  An inconsistent invoicing path for the same kind of charge depending only on timing
  makes billing unpredictable for both the customer and finance.
DISCONFIRMING_OBSERVATION: >
  A service attached to a booth at the time of the original order is invoiced differently,
  through a different document path, than an equivalent service added afterward.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attach one service to a booth at the time of ordering and an equivalent service after
  the order is already placed, and compare how each is invoiced.
```

## G11-EVENT_BOOTH_SALE-Q021

```yaml
QID: G11-EVENT_BOOTH_SALE-Q021
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A service attached to a booth after its original order has already been invoiced
  produces a deterministic additional billing action, rather than a service that can be
  attached and consumed with no billing path ever triggered for it.
WHY_IT_MATTERS: >
  A service that can be delivered without any billing path being triggered is revenue that
  quietly never gets collected.
DISCONFIRMING_OBSERVATION: >
  A service is attached to a booth after its order was already invoiced, is delivered, and
  no additional invoice or billing action is ever generated for it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attach and deliver a new service on a booth whose order has already been invoiced, and
  check whether any additional billing action follows.
```

## G11-EVENT_BOOTH_SALE-Q022

```yaml
QID: G11-EVENT_BOOTH_SALE-Q022
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When both a category-level price and a specific named-booth override price exist, which
  one actually governs the order line is a documented precedence rule, not an outcome that
  depends on which was entered or edited more recently.
WHY_IT_MATTERS: >
  An undocumented precedence rule means the same combination of category and booth-level
  prices can silently produce different order totals depending on unrelated editing
  history.
DISCONFIRMING_OBSERVATION: >
  An order line's price differs across two otherwise identical setups of category price
  and booth-level override price, with no documented rule explaining which value should
  govern.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set both a category-level price and a differing booth-level override price, then sell
  that booth and check which price the order line actually uses.
```

## G11-EVENT_BOOTH_SALE-Q023

```yaml
QID: G11-EVENT_BOOTH_SALE-Q023
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An order containing several booth lines is not treated as fully confirmed, invoiced, or
  complete while some of those lines still have no specific named booth actually allocated
  behind them.
WHY_IT_MATTERS: >
  Treating a partially fulfilled multi-booth order as complete tells the customer, and
  finance, that space has been secured that in fact has not.
DISCONFIRMING_OBSERVATION: >
  A multi-line booth order is marked confirmed or fully invoiced while one or more of its
  lines have no specific named booth actually allocated.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a multi-line booth order, allocate a specific booth for only some of the lines,
  and check whether the order can still be marked confirmed or complete.
```

## G11-EVENT_BOOTH_SALE-Q024

```yaml
QID: G11-EVENT_BOOTH_SALE-Q024
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the quantity of booths on an order line does not match the number of specific named
  booths actually allocated against it, that mismatch is detectable rather than invoicing
  proceeding purely on the ordered quantity regardless of what was actually fulfilled.
WHY_IT_MATTERS: >
  Invoicing a quantity that was never actually fulfilled charges a customer for space that
  was never delivered, or hides space delivered for free.
DISCONFIRMING_OBSERVATION: >
  An order line's invoiced quantity of booths does not match the number of specific named
  booths actually allocated against it, and nothing in the system surfaces that mismatch.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an order line for a quantity of booths, allocate a different number of specific
  named booths against it, and check whether invoicing reflects the mismatch.
```

## G11-EVENT_BOOTH_SALE-Q025

```yaml
QID: G11-EVENT_BOOTH_SALE-Q025
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A refund cannot be processed for a booth order once the event's occupancy window has
  already begun, without at least an explicit override or flag acknowledging that the
  booth was, or should have been, in use.
WHY_IT_MATTERS: >
  Refunding a booth as if it were never used, after the point at which it was supposed to
  already be occupied, hands back money for space the business had already committed to
  that customer.
DISCONFIRMING_OBSERVATION: >
  A refund for a booth order is processed after the event's occupancy window has begun,
  with no override, flag, or acknowledgement of that timing anywhere in the record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Attempt to process a refund for a booth order after the event's occupancy period has
  already started.
```

## G11-EVENT_BOOTH_SALE-Q026

```yaml
QID: G11-EVENT_BOOTH_SALE-Q026
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a booth's order is cancelled, refunded, and the same booth is resold to a second
  customer for the same event, the second sale's allocation record is independent and
  clean, carrying no leftover reference to the first, cancelled order.
WHY_IT_MATTERS: >
  A second sale that inherits artifacts of a cancelled first sale can confuse who actually
  holds the booth, or attribute the wrong history to the new occupant.
DISCONFIRMING_OBSERVATION: >
  A booth resold after a prior order's cancellation and refund shows the new allocation
  still referencing, or entangled with, the cancelled order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel and refund a booth order, resell the same booth to a different customer, and
  inspect the new allocation for any leftover reference to the first order.
```

## G11-EVENT_BOOTH_SALE-Q027

```yaml
QID: G11-EVENT_BOOTH_SALE-Q027
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  At any point, even after a named booth has passed through multiple reallocations and
  cancellations across different orders, its current occupant can be traced back to
  exactly one currently valid order line, not to several conflicting ones or none at all.
WHY_IT_MATTERS: >
  Losing an unambiguous trace from a booth to its current paying order is exactly what
  turns a billing dispute into something that cannot be resolved.
DISCONFIRMING_OBSERVATION: >
  A named booth's current occupant cannot be traced to exactly one currently valid order
  line after it has passed through several reallocations and cancellations.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Pass a named booth through multiple cancellations and reallocations across different
  orders, then attempt to trace its current occupant back to a single valid order line.
```

## G11-EVENT_BOOTH_SALE-Q028

```yaml
QID: G11-EVENT_BOOTH_SALE-Q028
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the underlying event is cancelled after booth orders were already confirmed and
  invoiced, every affected order is moved through a defined commercial unwind, credit
  note, refund, or equivalent, rather than being left standing as valid invoices against
  an event that will not occur.
WHY_IT_MATTERS: >
  Invoices left standing against a cancelled event either overstate revenue that will
  never be realised or leave customers owed money with no process actually addressing it.
DISCONFIRMING_OBSERVATION: >
  An event is cancelled while booth orders remain confirmed and invoiced against it, and
  no credit note, refund, or equivalent unwind is triggered for those orders.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel an event that has confirmed and invoiced booth orders against it, and check what
  happens to those orders.
```

## G11-EVENT_BOOTH_SALE-Q029

```yaml
QID: G11-EVENT_BOOTH_SALE-Q029
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A customer can confirm an order for a booth sold by category before any specific named
  booth has been identified for allocation, and the order's confirmed state accurately
  reflects that the specific booth is still pending rather than implying it is already
  settled.
WHY_IT_MATTERS: >
  An order that looks fully settled while the actual space is still undetermined misleads
  anyone reading it about how much is actually resolved.
DISCONFIRMING_OBSERVATION: >
  An order for a category-sold booth is confirmed with its status presented identically to
  an order where a specific booth has already been allocated.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Confirm a category-sold booth order with no specific booth yet allocated, and compare
  its presented status to a fully allocated booth order.
```

## G11-EVENT_BOOTH_SALE-Q030

```yaml
QID: G11-EVENT_BOOTH_SALE-Q030
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a partial payment on a booth order is sufficient to place or maintain a hold on
  the booth, as distinct from requiring full payment, is a defined, configurable rule
  rather than an incidental effect of however the payment happens to be recorded.
WHY_IT_MATTERS: >
  An undefined link between partial payment and holding the space leaves both sales staff
  and customers unsure whether a deposit actually protects the booth they want.
DISCONFIRMING_OBSERVATION: >
  Whether a partial payment maintains a hold on a booth varies across otherwise identical
  orders with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Make a partial payment on a booth order and determine whether, and under what documented
  rule, that maintains the booth's hold.
```

## G11-EVENT_BOOTH_SALE-Q031

```yaml
QID: G11-EVENT_BOOTH_SALE-Q031
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order is amended to add further booth quantity to an existing line, the added
  quantity's allocation is tracked independently from the original quantity's allocation,
  rather than merging into a single ambiguous count that can no longer tell which specific
  booths belong to which part of the amendment.
WHY_IT_MATTERS: >
  A merged, ambiguous count after an amendment can no longer answer which specific booths
  belong to the original commitment versus the added one, complicating billing and any
  partial cancellation.
DISCONFIRMING_OBSERVATION: >
  An order line's quantity is increased and the resulting allocation cannot distinguish
  which specific booths correspond to the original quantity versus the added quantity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Amend an order line to increase its booth quantity after the original quantity is
  already allocated, and check whether the two portions remain distinguishable.
```

## G11-EVENT_BOOTH_SALE-Q032

```yaml
QID: G11-EVENT_BOOTH_SALE-Q032
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An order line requesting a booth category that has no remaining available named booths
  is blocked or flagged at the point of entry, rather than being accepted onto the order
  with fulfilment left unresolved.
WHY_IT_MATTERS: >
  Accepting an order for space that provably does not exist sets up a commitment the
  business already knows it cannot keep.
DISCONFIRMING_OBSERVATION: >
  An order line requesting a category with zero remaining available named booths is
  accepted onto the order with no block or flag raised at entry.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Exhaust a category's available named booths, then attempt to add an order line
  requesting that category.
```

## G11-EVENT_BOOTH_SALE-Q033

```yaml
QID: G11-EVENT_BOOTH_SALE-Q033
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the specific booth referenced by an open quotation becomes unavailable, whether
  allocated elsewhere or withdrawn, while the quotation is still open, that quotation is
  automatically flagged or invalidated rather than continuing to reference a booth it no
  longer actually controls.
WHY_IT_MATTERS: >
  A quotation still quoting a booth it no longer holds can be confirmed into an order for
  space that has already gone to someone else.
DISCONFIRMING_OBSERVATION: >
  A quotation's referenced booth becomes unavailable while the quotation remains open, and
  the quotation is neither flagged nor invalidated as a result.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Create an open quotation referencing a specific booth, then make that same booth
  unavailable through a separate action, and check the quotation's resulting state.
```

## G11-EVENT_BOOTH_SALE-Q034

```yaml
QID: G11-EVENT_BOOTH_SALE-Q034
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Every state a booth's commercial ownership passes through, quoted, confirmed, invoiced,
  cancelled, refunded, is attributable to a specific order and a specific timestamp, and
  is not something that can only be reconstructed by inspecting the booth's current field
  values.
WHY_IT_MATTERS: >
  Without an attributable commercial history, a dispute over when a booth was actually
  sold, or to whom, has no record to settle it.
DISCONFIRMING_OBSERVATION: >
  A booth's commercial ownership history cannot be reconstructed to specific orders and
  timestamps, only inferred from its present field values.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Move a booth order through quoted, confirmed, invoiced and cancelled states, then
  attempt to retrieve the order and timestamp behind each transition.
```

## G11-EVENT_BOOTH_SALE-Q035

```yaml
QID: G11-EVENT_BOOTH_SALE-Q035
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the ordering customer's accounting scope, branch or company, differs from the
  event's owning company, the invoice for the booth sale is routed to the accounting
  entity actually responsible for that event, not defaulted to whichever entity happens to
  be attached to the customer.
WHY_IT_MATTERS: >
  An invoice routed to the wrong accounting entity misstates whose books the revenue and
  any associated tax obligation actually belong to.
DISCONFIRMING_OBSERVATION: >
  A booth sale's invoice is routed to the customer's own accounting entity even where the
  event is owned by a different company or branch responsible for that revenue.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Place a booth order where the customer's accounting scope differs from the event's
  owning company, and check which entity the resulting invoice is routed to.
```

## G11-EVENT_BOOTH_SALE-Q036

```yaml
QID: G11-EVENT_BOOTH_SALE-Q036
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Issuing a credit note for a cancelled booth order and releasing the underlying booth
  allocation are linked such that one does not happen without the other, rather than being
  two independent actions that can drift out of step.
WHY_IT_MATTERS: >
  A credit note issued with the booth still held, or a booth released with no credit note
  issued, both leave the commercial and physical records disagreeing about what actually
  happened.
DISCONFIRMING_OBSERVATION: >
  A credit note is issued for a cancelled booth order without the booth allocation being
  released, or the booth is released without a corresponding credit note being issued.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel a booth order and issue its credit note, then separately check whether the booth
  allocation was released as part of the same action or left to drift independently.
```

## G11-EVENT_BOOTH_SALE-Q037

```yaml
QID: G11-EVENT_BOOTH_SALE-Q037
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A discount applied to a booth order can be scoped to apply to the booth line alone
  without automatically applying to its attached services, or vice versa, as a deliberate,
  visible choice rather than an all-or-nothing default nobody actually decided on.
WHY_IT_MATTERS: >
  An accidental all-or-nothing discount either erodes margin on services nobody meant to
  discount, or fails to honour a discount a salesperson believed covered everything.
DISCONFIRMING_OBSERVATION: >
  A discount configured to apply to only the booth line, or only its services, is applied
  to both regardless, with no visible setting controlling the scope.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a discount scoped to only the booth line or only its attached services, and
  check whether that scoping is actually honoured on the order.
```

## G11-EVENT_BOOTH_SALE-Q038

```yaml
QID: G11-EVENT_BOOTH_SALE-Q038
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whether the exhibiting company's own staff can see the commercial details, price and
  payment status, of the order behind their booth is a defined permission boundary, not
  implicitly open to anyone who can see the booth itself.
WHY_IT_MATTERS: >
  Exposing commercial terms to the exhibiting company by default, when the paying customer
  is a different party such as a sponsor, discloses a financial arrangement the payer may
  never have agreed to share.
DISCONFIRMING_OBSERVATION: >
  A user representing the exhibiting company, but not the paying customer, can view the
  order's price or payment status with no separate permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  With a paying customer distinct from the exhibiting company, check whether a user
  representing the exhibiting company can view the order's commercial details.
```

## G11-EVENT_BOOTH_SALE-Q039

```yaml
QID: G11-EVENT_BOOTH_SALE-Q039
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If order confirmation succeeds but the subsequent booth-allocation step fails, that
  failure either rolls the order back or leaves it explicitly flagged as unfulfilled,
  rather than leaving a confirmed order silently standing with no booth ever actually
  allocated behind it.
WHY_IT_MATTERS: >
  A confirmed order silently missing its allocation is discovered only when the customer
  arrives expecting a space that was never actually reserved.
DISCONFIRMING_OBSERVATION: >
  An order remains in a confirmed state after its booth-allocation step fails, with
  nothing distinguishing it from an order that was successfully allocated.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Force the booth-allocation step to fail after an order has already been confirmed, and
  inspect the resulting order state.
```

## G11-EVENT_BOOTH_SALE-Q040

```yaml
QID: G11-EVENT_BOOTH_SALE-Q040
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An amount forfeited under a late-cancellation policy on a booth order is recorded
  distinctly in the accounting entries from revenue recognised on a normally fulfilled
  sale, rather than the two looking identical in the ledger.
WHY_IT_MATTERS: >
  Conflating forfeited cancellation revenue with ordinary fulfilled-sale revenue
  misrepresents how much of the period's revenue actually came from delivered space versus
  cancellation penalties.
DISCONFIRMING_OBSERVATION: >
  A forfeited late-cancellation amount is recorded in the accounting entries with no
  distinction from revenue recognised on a booth that was actually delivered.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  Trigger a late cancellation that forfeits payment under policy, and compare the
  resulting accounting entry to that of a normally fulfilled booth sale.
```

## G11-EVENT_BOOTH_SALE-Q041

```yaml
QID: G11-EVENT_BOOTH_SALE-Q041
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order line's specific booth reference is changed after confirmation, the
  previously referenced booth is retained in the order's own history, not overwritten so
  that only the newest reference is ever visible.
WHY_IT_MATTERS: >
  Losing the record of which booth an order originally referenced removes the ability to
  explain a later billing or allocation dispute back to what was first agreed.
DISCONFIRMING_OBSERVATION: >
  An order line's booth reference is changed after confirmation and no record of the
  previously referenced booth remains retrievable from the order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a confirmed order line's specific booth reference to a different booth, then
  attempt to retrieve the originally referenced booth from the order's history.
```

## G11-EVENT_BOOTH_SALE-Q042

```yaml
QID: G11-EVENT_BOOTH_SALE-Q042
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  For a booth service priced by a consumable unit, such as per day or per staff badge,
  whether the invoice follows the quantity ordered or the quantity actually consumed is a
  defined rule, and any disagreement between the two is flagged rather than the ordered
  figure being invoiced unquestioned regardless of what was consumed.
WHY_IT_MATTERS: >
  Invoicing purely on what was ordered when consumption differed either overcharges or
  undercharges the customer for a unit-priced service with no one noticing.
DISCONFIRMING_OBSERVATION: >
  A unit-priced booth service is invoiced strictly on the ordered quantity even where the
  actually consumed quantity differs, with no flag raised on the mismatch.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Order a unit-priced booth service, record a different actually-consumed quantity, and
  check which quantity the resulting invoice reflects.
```

## G11-EVENT_BOOTH_SALE-Q043

```yaml
QID: G11-EVENT_BOOTH_SALE-Q043
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When one order covers the same exhibitor's booths across multiple sequential editions of
  a recurring event, each edition's booth allocation and invoicing is tracked
  independently, rather than the editions' quantities or charges being conflated under a
  single undifferentiated line.
WHY_IT_MATTERS: >
  Conflated multi-edition billing makes it impossible to tell which edition a given
  charge, allocation, or cancellation actually belongs to.
DISCONFIRMING_OBSERVATION: >
  An order covering an exhibitor's booths across multiple event editions cannot be broken
  down by edition for either allocation or invoicing purposes.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place one order covering an exhibitor's booths across two sequential event editions,
  then attempt to distinguish each edition's allocation and invoicing.
```

## G11-EVENT_BOOTH_SALE-Q044

```yaml
QID: G11-EVENT_BOOTH_SALE-Q044
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling only one booth line of a multi-booth order releases only that specific line's
  booth allocation, leaving the other lines' allocations and their booths completely
  untouched.
WHY_IT_MATTERS: >
  A partial cancellation that accidentally disturbs unrelated lines on the same order
  could release space the customer never intended to give up.
DISCONFIRMING_OBSERVATION: >
  Cancelling one line of a multi-booth order changes the allocation state of a different,
  uncancelled line on the same order.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Cancel one line of a multi-line booth order and check whether the other lines' booth
  allocations remain unaffected.
```

## G11-EVENT_BOOTH_SALE-Q045

```yaml
QID: G11-EVENT_BOOTH_SALE-Q045
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A single paid order line for one booth is never silently satisfied by allocating more
  than one specific named booth against it without an explicit, additional commercial
  document authorising the extra space.
WHY_IT_MATTERS: >
  Allocating extra space against a single paid line without a corresponding charge either
  gives away space for free or hides a billing gap that should have been caught.
DISCONFIRMING_OBSERVATION: >
  A single order line paid for one booth ends up with more than one specific named booth
  allocated against it, with no additional order line or document accounting for the
  extra.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attempt to allocate a second specific named booth against an order line already paid and
  allocated for exactly one booth.
```

## G11-EVENT_BOOTH_SALE-Q046

```yaml
QID: G11-EVENT_BOOTH_SALE-Q046
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The tax treatment applied to a booth sale can be configured independently from the tax
  treatment applied to a general merchandise sale or an event registration, rather than
  inheriting one generic tax rule regardless of what is actually being sold.
WHY_IT_MATTERS: >
  A booth is a distinct kind of commercial transaction that may carry different tax rules
  than merchandise or admission, and forcing one generic rule onto all three risks
  misapplying tax on at least one of them.
DISCONFIRMING_OBSERVATION: >
  A booth sale's tax treatment cannot be configured separately from the tax treatment
  applied to general merchandise sales or event registrations.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Attempt to configure a tax treatment for booth sales that differs from the treatment
  configured for general merchandise or event registration sales.
```

## G11-EVENT_BOOTH_SALE-Q047

```yaml
QID: G11-EVENT_BOOTH_SALE-Q047
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to a booth's allocation made directly on the allocation side after an order is
  confirmed does not leave the order silently disagreeing about who holds that booth; the
  two remain linked and consistent, or the disagreement is flagged.
WHY_IT_MATTERS: >
  An order and its allocation drifting apart with no flag leaves two internal records
  making contradictory claims about the same paid space.
DISCONFIRMING_OBSERVATION: >
  A booth's allocation is changed directly after order confirmation and the order
  continues to reference the prior state with no flag or reconciliation.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Confirm a booth order, then change the underlying allocation directly rather than
  through the order, and check whether the two remain consistent or the mismatch is
  flagged.
```

## G11-EVENT_BOOTH_SALE-Q048

```yaml
QID: G11-EVENT_BOOTH_SALE-Q048
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Because what is sold is a specific identified booth rather than an interchangeable
  quantity, cancelling and re-ordering what the customer considers the same booth never
  silently results in a different physical booth being allocated without an explicit step
  in which the customer or staff acknowledges the change.
WHY_IT_MATTERS: >
  A customer who believes they are simply restoring their original booth, but is silently
  given a different one, discovers the substitution only when they arrive to find it is
  not the space they expected.
DISCONFIRMING_OBSERVATION: >
  A cancelled and re-ordered booth results in a different specific named booth being
  allocated than the one originally held, with no explicit acknowledgement step presented
  to either party.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Cancel an order for a specific named booth and place a new order intended to restore it,
  then check whether the same specific booth is allocated or a different one is
  substituted silently.
```

## G11-EVENT_BOOTH_SALE-Q049

```yaml
QID: G11-EVENT_BOOTH_SALE-Q049
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A category-based sale, where the customer is entitled to any booth within a category
  rather than one named in advance, is never reported or reconciled as if it were a
  specific-booth sale until a specific booth has actually been decided, keeping the two
  kinds of entitlement distinguishable throughout.
WHY_IT_MATTERS: >
  Blurring a category entitlement into a specific-booth entitlement before one is actually
  decided overstates how settled the sale really is, in exactly the way this module exists
  to avoid confusing with an ordinary interchangeable seat sale.
DISCONFIRMING_OBSERVATION: >
  A category-based order is reported, reconciled, or displayed identically to a specific-
  booth order before any specific booth has actually been assigned to it.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Place a category-based booth order with no specific booth yet assigned, and compare its
  reporting and display to a specific-booth order.
```

## G11-EVENT_BOOTH_SALE-Q050

```yaml
QID: G11-EVENT_BOOTH_SALE-Q050
MODULE: event_booth_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A booth's withdrawal reason recorded on the allocation side, such as a venue change, and
  a related order's cancellation reason recorded on the commercial side are reconciled to
  a single, consistent explanation, rather than being able to disagree with each other
  about why the customer no longer holds the booth.
WHY_IT_MATTERS: >
  Two independently recorded, disagreeing reasons for the same lost booth leave no single
  true account of what actually happened, which matters the moment a customer disputes it.
DISCONFIRMING_OBSERVATION: >
  A booth's recorded withdrawal reason and its related order's recorded cancellation
  reason describe two different, unreconciled explanations for the same lost allocation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Withdraw a booth for one stated reason and cancel its related order, checking whether
  the order's cancellation reason is reconciled with, or can contradict, the booth's
  withdrawal reason.
```
