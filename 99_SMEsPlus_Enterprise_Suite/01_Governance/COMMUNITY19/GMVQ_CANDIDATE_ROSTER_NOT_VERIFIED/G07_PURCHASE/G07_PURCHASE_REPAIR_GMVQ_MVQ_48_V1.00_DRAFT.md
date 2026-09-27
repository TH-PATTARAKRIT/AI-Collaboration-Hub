# SMEsPlus ENTERPRISE SUITE
## GMVQ — G07 PURCHASE / purchase_repair Module Adversarial MVQ Bank

**Document ID:** GMVQ-G07-PURCHASE_REPAIR-MVQ48-V1.00  
**Group:** G07 PURCHASE  
**Module Metadata:** `purchase_repair`  
**Wave:** W2  
**Author Cell:** P16 (GMVQ Question Factory — Production Team P16)  
**Review Cell:** PENDING  
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN  
**actual_mvq_count:** 48  
**Standard bank reference:** 55 (shared, not reproduced here)  
**Research depth:** 55 + 48 = 103  
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded  

## Purpose

This bank authors the module-specific MVQ set for `purchase_repair` — procurement driven by a repair need. It is a BRIDGE module per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question below fails only at the seam between a repair's specific, time-critical need and the procurement raised to satisfy it, and would not make sense if either capability were used without the other. Buying for a repair differs from buying for stock: the need is discovered late, is specific to one item (often one serial), and the repair is blocked until the part arrives. Ground covered: a part purchased for one repair being consumed by another; a repair waiting on a part with no visibility of the resulting delay; a part arriving after its item was scrapped or its repair cancelled; where a part's cost lands among the repair, the item, and a customer charge; an urgent single-unit purchase bypassing normal approval or vendor selection; a part that is also ordinary stock and whether it is reserved or pooled; a warranty claim versus a purchase for the same need; returning an unused part after completion; serial-to-serial traceability between a purchased part and the item it was fitted to; and the repair's promised date against the vendor's actual lead time.

The question text is source-neutral and does not expose vendor model names, field names, methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE: purchase_repair` appears only in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- Bridge module: every question targets the seam between a repair's own need and the procurement raised to satisfy it only, per GMVQ_BRIDGE_MODULE_RULE_V1.00 §2. Removing either the repair context or the purchase makes the question meaningless — that is the test applied before inclusion.

## G07-PURCHASE_REPAIR-Q001

```yaml
QID: G07-PURCHASE_REPAIR-Q001
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A part purchased and received against one specific repair must not be automatically
  consumable by a different repair without an explicit reassignment action being recorded.
WHY_IT_MATTERS: >
  Silent consumption by a different repair leaves the original repair's need looking met
  when the part it was actually purchased for never arrived.
DISCONFIRMING_OBSERVATION: >
  A part received against one repair's purchase is drawn by a different repair with no
  reassignment action recorded, and the original repair still shows the part as received.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Order and receive a part against one specific repair, then attempt to consume that same
  received part on a different repair's work.
```

## G07-PURCHASE_REPAIR-Q002

```yaml
QID: G07-PURCHASE_REPAIR-Q002
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reassigning a received part from the repair it was purchased for to a different repair
  must leave a visible link back to the original repair's now-unfulfilled need, not
  silently close it as satisfied.
WHY_IT_MATTERS: >
  Losing the trail back to the original repair hides that it still needs a part, even
  though something was received in its name.
DISCONFIRMING_OBSERVATION: >
  After a received part is reassigned to a different repair, the original repair's record
  shows no indication that its part need is still open.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive a part against one repair, reassign it to a different repair, and check the
  original repair's status.
```

## G07-PURCHASE_REPAIR-Q003

```yaml
QID: G07-PURCHASE_REPAIR-Q003
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two repairs waiting on the same purchased part, where only enough was ordered for one,
  must make explicit which repair the arriving quantity is allocated to, rather than
  allocating it first-come to whichever repair happens to check first.
WHY_IT_MATTERS: >
  Both repairs believing an insufficient incoming quantity fully covers them leads to one
  being blocked with no warning once the shortfall becomes apparent.
DISCONFIRMING_OBSERVATION: >
  Two repairs each show the same incoming, insufficient quantity as fully satisfying their
  need, with no indication of which one it is actually allocated to.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Raise two repairs each needing more of a part than a single incoming order line will
  deliver in total, and check each repair's expected fulfilment.
```

## G07-PURCHASE_REPAIR-Q004

```yaml
QID: G07-PURCHASE_REPAIR-Q004
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A repair whose procurement is delayed beyond the vendor's originally committed date must
  surface that delay against the repair itself, not require someone to separately check
  the purchase order's status.
WHY_IT_MATTERS: >
  A delay visible only on the purchase order, and not on the repair, means whoever is
  managing the repair, and the customer, finds out too late.
DISCONFIRMING_OBSERVATION: >
  A part's delivery has passed the vendor's originally committed date, and the repair it
  is for shows no delay or exception.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Let a purchase order's committed delivery date pass unmet while a repair depends on it,
  and check the repair's own status.
```

## G07-PURCHASE_REPAIR-Q005

```yaml
QID: G07-PURCHASE_REPAIR-Q005
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A repair blocked on an awaited part must be distinguishable, in its own status, from a
  repair blocked for any other reason, so the cause of the wait is not lost.
WHY_IT_MATTERS: >
  Conflating a procurement wait with any other kind of hold makes it impossible to tell
  who or what is actually responsible for the delay.
DISCONFIRMING_OBSERVATION: >
  A repair blocked on an awaited part shows the same generic waiting status as a repair
  blocked for an unrelated reason.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Put one repair on hold for an awaited part and another on hold for a different reason,
  and compare their recorded status.
```

## G07-PURCHASE_REPAIR-Q006

```yaml
QID: G07-PURCHASE_REPAIR-Q006
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to the purchase order's expected arrival date after the repair began waiting
  must propagate to whatever the repair reports as its own expected resumption, not leave
  the repair showing a resumption date the procurement no longer supports.
WHY_IT_MATTERS: >
  A repair still promising a resumption date the procurement no longer supports sets a
  false expectation for whoever is tracking it.
DISCONFIRMING_OBSERVATION: >
  The vendor's expected arrival date changes on the purchase order, but the repair
  continues to show its original, now-unsupported resumption date.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Change the expected arrival date on a purchase order linked to a waiting repair, and
  check whether the repair's reported resumption date updates.
```

## G07-PURCHASE_REPAIR-Q007

```yaml
QID: G07-PURCHASE_REPAIR-Q007
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A part arriving after the repair it was purchased for has been cancelled must not be
  automatically consumed by that repair's closure process; its disposition must be an
  explicit decision.
WHY_IT_MATTERS: >
  Automatically absorbing an arriving part into a cancelled repair's closure hides that
  the part exists and is available for another use.
DISCONFIRMING_OBSERVATION: >
  A part arrives and is received after its repair was cancelled, and the closure process
  consumes or writes it off without an explicit decision being recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a repair with an open purchase for a part specific to it, then receive that part,
  and observe what happens to it.
```

## G07-PURCHASE_REPAIR-Q008

```yaml
QID: G07-PURCHASE_REPAIR-Q008
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A part arriving after the item under repair has been scrapped must leave the part
  available for other use, not be written off automatically as a consequence of the item's
  disposal.
WHY_IT_MATTERS: >
  Automatically writing off a usable part because the item it was meant for is gone wastes
  stock that could serve another repair.
DISCONFIRMING_OBSERVATION: >
  A part arrives after the item it was purchased for has been scrapped, and it is written
  off automatically rather than remaining available.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Scrap an item mid-repair while a part for it is still on order, then receive the part,
  and check its resulting availability.
```

## G07-PURCHASE_REPAIR-Q009

```yaml
QID: G07-PURCHASE_REPAIR-Q009
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a repair that has an open purchase for a part specific to it must trigger a
  review of that purchase, rather than leaving an order the repair no longer needs to
  complete unnoticed.
WHY_IT_MATTERS: >
  An order the repair no longer needs, left unnoticed, either wastes the purchase or
  arrives with nobody expecting or wanting it.
DISCONFIRMING_OBSERVATION: >
  A repair is cancelled while it has an open, part-specific purchase outstanding, and
  nothing flags that purchase for review.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Place a part-specific purchase for a repair, then cancel the repair before the part
  arrives, and check whether the purchase is flagged.
```

## G07-PURCHASE_REPAIR-Q010

```yaml
QID: G07-PURCHASE_REPAIR-Q010
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The cost of a part purchased for a repair must be attributable to exactly one of the
  repair's own cost, the item's accumulated cost, or a charge to the customer, according
  to one explicit rule, not left ambiguous between them.
WHY_IT_MATTERS: >
  An ambiguous cost destination means the true cost of the repair, the item's value, or
  what the customer owes can each be wrong.
DISCONFIRMING_OBSERVATION: >
  A part purchased for a repair has its cost recorded, but it cannot be determined which
  of the repair, the item, or a customer charge it was actually attributed to.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Purchase a part for a repair and trace where its cost lands among the repair's own cost,
  the item's accumulated cost, and any customer charge.
```

## G07-PURCHASE_REPAIR-Q011

```yaml
QID: G07-PURCHASE_REPAIR-Q011
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where the repair's cost is later charged to a customer, a part purchased at other-than-
  standard cost, such as an urgent-purchase premium, must have that actual cost, not an
  assumed standard cost, flow through to the customer charge.
WHY_IT_MATTERS: >
  Charging the customer a standard cost while an urgent premium was actually paid either
  overcharges or undercharges them relative to what was really spent.
DISCONFIRMING_OBSERVATION: >
  A part bought at an urgent-purchase premium has only its standard cost reflected in the
  customer charge for the repair.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Purchase a part for a chargeable repair at an above-standard urgent price, and check
  what cost the customer charge reflects.
```

## G07-PURCHASE_REPAIR-Q012

```yaml
QID: G07-PURCHASE_REPAIR-Q012
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A part purchased for a repair that is subsequently covered by warranty must not have its
  cost land on the same target, whether the repair, the item, or the customer, that a non-
  warranty repair's part cost would.
WHY_IT_MATTERS: >
  Charging a customer, or the repair's own cost, for a part the vendor actually covered
  under warranty misstates who really bore the cost.
DISCONFIRMING_OBSERVATION: >
  A part purchased for a repair later covered by warranty still has its cost attributed
  exactly as it would be for a non-warranty repair.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Purchase a part for a repair, have the repair's warranty coverage confirmed afterward,
  and check where the part's cost is attributed.
```

## G07-PURCHASE_REPAIR-Q013

```yaml
QID: G07-PURCHASE_REPAIR-Q013
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An urgent purchase raised directly from a repair's need must still be attributable to an
  accountable approver, even where the normal approval sequence is bypassed for speed.
WHY_IT_MATTERS: >
  A purchase nobody is accountable for, made in the name of speed, removes the very
  oversight an approval step exists to provide.
DISCONFIRMING_OBSERVATION: >
  An urgent purchase raised directly from a repair's need is recorded with no identifiable
  approver, even though the normal approval sequence was bypassed.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Raise an urgent purchase directly from a repair's need through whatever expedited path
  exists, and check who it records as accountable.
```

## G07-PURCHASE_REPAIR-Q014

```yaml
QID: G07-PURCHASE_REPAIR-Q014
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Bypassing the normal vendor-selection path for an urgent repair part must be recorded as
  a deliberate exception, not indistinguishable from an order that went through ordinary
  vendor selection.
WHY_IT_MATTERS: >
  An unrecorded bypass looks identical to an order that went through proper vendor
  selection, hiding that a control was skipped.
DISCONFIRMING_OBSERVATION: >
  An urgent repair part purchase that skipped normal vendor selection is indistinguishable
  in the record from one that went through it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise an urgent repair part purchase bypassing normal vendor selection, and check
  whether that bypass is recorded.
```

## G07-PURCHASE_REPAIR-Q015

```yaml
QID: G07-PURCHASE_REPAIR-Q015
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An urgent single-unit purchase raised from a repair must not be exempted from a
  spending-limit control that would otherwise apply to a purchase of that value.
WHY_IT_MATTERS: >
  Exempting urgency from a spending limit creates an easy route around a control meant to
  catch high-value purchases regardless of how they arose.
DISCONFIRMING_OBSERVATION: >
  An urgent single-unit purchase raised from a repair exceeds the normal spending limit
  for its value without triggering the control that would otherwise apply.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Raise an urgent repair-driven purchase above the normal spending-limit threshold, and
  check whether the control is triggered.
```

## G07-PURCHASE_REPAIR-Q016

```yaml
QID: G07-PURCHASE_REPAIR-Q016
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A part purchased for a specific repair, where that same part is also carried as general
  stock, must be distinguishable as reserved to that repair rather than silently pooled
  with general stock availability, unless the business has explicitly chosen pooling.
WHY_IT_MATTERS: >
  Silent pooling lets an unrelated demand consume a part a repair is specifically counting
  on, without anyone realizing the reservation was never real.
DISCONFIRMING_OBSERVATION: >
  A part purchased for a specific repair, also carried as general stock, shows as
  available general stock with no indication it is reserved to that repair.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Purchase a part for a specific repair where that same part is also stocked generally,
  and check how its availability is represented.
```

## G07-PURCHASE_REPAIR-Q017

```yaml
QID: G07-PURCHASE_REPAIR-Q017
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If a part reserved to a repair is drawn instead to satisfy an unrelated stock demand,
  the repair's need for that part must remain visibly open, not appear satisfied by
  inventory that was actually consumed elsewhere.
WHY_IT_MATTERS: >
  A repair appearing satisfied by inventory that actually went to a different demand hides
  a real, ongoing shortage from whoever is tracking the repair.
DISCONFIRMING_OBSERVATION: >
  A part reserved to a repair is consumed by an unrelated stock demand, and the repair's
  need still shows as satisfied.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a part to a repair, then have a different demand consume that same part, and
  check the repair's status afterward.
```

## G07-PURCHASE_REPAIR-Q018

```yaml
QID: G07-PURCHASE_REPAIR-Q018
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a part is deliberately pooled rather than reserved, a shortage caused by another
  repair or order consuming the shared stock must be visible as a cause of this repair's
  delay.
WHY_IT_MATTERS: >
  Not showing the real cause of a shortage leaves whoever manages the repair unable to
  explain or resolve the delay.
DISCONFIRMING_OBSERVATION: >
  A repair is delayed because pooled stock was consumed by a different repair or order,
  and nothing in the delayed repair's record shows that cause.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Pool a part across repairs deliberately, consume the shared stock through one repair,
  and check what the other, now-delayed repair shows as the reason.
```

## G07-PURCHASE_REPAIR-Q019

```yaml
QID: G07-PURCHASE_REPAIR-Q019
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A part obtained through a vendor warranty claim must be distinguishable in the repair's
  record from a part obtained by ordinary purchase, so the true cost and vendor recovery
  are not conflated.
WHY_IT_MATTERS: >
  Conflating a warranty-obtained part with a purchased one hides the true cost of the
  repair and any amount still owed to or by the vendor.
DISCONFIRMING_OBSERVATION: >
  A part obtained through a vendor warranty claim is recorded on the repair identically to
  a part obtained by ordinary purchase, with no way to tell them apart.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Obtain one part for a repair through a warranty claim and another through ordinary
  purchase, and compare how each is recorded.
```

## G07-PURCHASE_REPAIR-Q020

```yaml
QID: G07-PURCHASE_REPAIR-Q020
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Pursuing a warranty claim for a part after a purchase for that same part has already
  been placed must reconcile the two so the repair does not end up with both an unresolved
  purchase and an unresolved claim for the same need.
WHY_IT_MATTERS: >
  Leaving both an unresolved purchase and an unresolved claim for the same need risks
  double-fulfilling it or double-counting its cost.
DISCONFIRMING_OBSERVATION: >
  A warranty claim is pursued for a part after a purchase for that same need was already
  placed, and both remain open with no reconciliation.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place a purchase for a part, then pursue a warranty claim for the same need before the
  purchase resolves, and check whether the two are reconciled.
```

## G07-PURCHASE_REPAIR-Q021

```yaml
QID: G07-PURCHASE_REPAIR-Q021
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A warranty claim that is ultimately rejected after a part was already fitted to the item
  under an assumption of no cost must convert cleanly to a chargeable purchase, not leave
  the part's cost unaccounted for.
WHY_IT_MATTERS: >
  A part fitted on the assumption of no cost, whose claim then fails, leaves the actual
  cost unaccounted for if nothing converts it to a real purchase.
DISCONFIRMING_OBSERVATION: >
  A warranty claim for an already-fitted part is rejected, and no chargeable purchase is
  created to account for that part's cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Fit a part to an item under an assumed warranty claim, have the claim subsequently
  rejected, and check whether a chargeable purchase results.
```

## G07-PURCHASE_REPAIR-Q022

```yaml
QID: G07-PURCHASE_REPAIR-Q022
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A part purchased for a repair but left unused when the repair completed must be
  returnable to the vendor or to general stock through an explicit action, not remain
  attached to a closed repair indefinitely.
WHY_IT_MATTERS: >
  A part permanently attached to a closed repair is neither available for other use nor
  properly returned, wasting its value indefinitely.
DISCONFIRMING_OBSERVATION: >
  A repair completes with an unused part still purchased for it, and the part remains
  attached to the closed repair with no path to return or reuse it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Complete a repair leaving one purchased part unused, and check what options exist for
  that part afterward.
```

## G07-PURCHASE_REPAIR-Q023

```yaml
QID: G07-PURCHASE_REPAIR-Q023
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Returning an unused part to the vendor after the repair closed must correctly reverse
  whatever cost had already been attributed to the repair, the item, or a customer charge
  for that part.
WHY_IT_MATTERS: >
  A return that doesn't reverse the cost already attributed leaves the repair, item, or
  customer charged for something that was actually given back.
DISCONFIRMING_OBSERVATION: >
  An unused part is returned to the vendor after the repair closes, but the cost already
  attributed to the repair, item, or customer charge is not reversed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attribute a part's cost to a repair, then return that unused part to the vendor after
  closure, and check whether the attributed cost is reversed.
```

## G07-PURCHASE_REPAIR-Q024

```yaml
QID: G07-PURCHASE_REPAIR-Q024
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Closing a repair with an unused, uncommitted part still on order must flag that open
  commitment rather than closing the repair as if procurement were fully resolved.
WHY_IT_MATTERS: >
  Closing as if procurement were fully resolved hides an order still outstanding that
  nobody will now think to follow up on.
DISCONFIRMING_OBSERVATION: >
  A repair with an unused part still on order is closed with no flag indicating that
  procurement remains open.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Leave a part still on order, unreceived, for a repair, close the repair, and check
  whether the open order is flagged.
```

## G07-PURCHASE_REPAIR-Q025

```yaml
QID: G07-PURCHASE_REPAIR-Q025
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A serial-tracked part purchased for and fitted to a serial-tracked item must record
  which specific serial of the part went into which specific serial of the item, not just
  that a purchase of that part type occurred.
WHY_IT_MATTERS: >
  Recording only that a part type was purchased, not which specific unit went into which
  specific item, defeats serial traceability at the exact point it matters most.
DISCONFIRMING_OBSERVATION: >
  A serial-tracked part fitted to a serial-tracked item during a repair leaves no record
  of which part serial went into which item serial.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Purchase and receive a serial-tracked part, fit a specific unit of it to a serial-
  tracked item during a repair, and check what traceability is recorded.
```

## G07-PURCHASE_REPAIR-Q026

```yaml
QID: G07-PURCHASE_REPAIR-Q026
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a serial-tracked part purchased for a repair is instead fitted to a different unit
  than the one the repair specifies, that substitution must be traceable, not lost once
  the part leaves receipt.
WHY_IT_MATTERS: >
  An untraceable substitution breaks the chain needed to know exactly what is inside which
  item, undermining any later recall or audit.
DISCONFIRMING_OBSERVATION: >
  A serial-tracked part purchased for one repair's specified unit is instead fitted to a
  different unit, and no record shows the substitution occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Purchase a serial-tracked part intended for a specific unit under a repair, fit it
  instead to a different unit, and check what is recorded.
```

## G07-PURCHASE_REPAIR-Q027

```yaml
QID: G07-PURCHASE_REPAIR-Q027
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A recall or quality hold placed on a specific serial of a purchased part must be
  traceable to every item it was fitted to via a repair, not only to the purchase order
  line it arrived on.
WHY_IT_MATTERS: >
  Being unable to trace a recalled part serial forward to the items it went into leaves
  affected units unidentified.
DISCONFIRMING_OBSERVATION: >
  A recall or quality hold placed on a specific part serial cannot be traced forward to
  the item or items it was fitted to through repairs.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Fit a specific serial of a purchased part to an item via a repair, then place a recall
  or hold on that part serial, and attempt to trace affected items.
```

## G07-PURCHASE_REPAIR-Q028

```yaml
QID: G07-PURCHASE_REPAIR-Q028
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A repair's promised completion date committed to the customer must be checked against
  the actual procurement lead time of a part it depends on, not assumed to be compatible
  by default.
WHY_IT_MATTERS: >
  Committing a completion date without checking whether the needed part can actually
  arrive in time sets an expectation that procurement was never positioned to meet.
DISCONFIRMING_OBSERVATION: >
  A repair's promised completion date is committed to the customer without any check
  against the lead time of a part it depends on.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Commit a promised completion date on a repair that depends on a part with a known vendor
  lead time, and check whether the two are compared.
```

## G07-PURCHASE_REPAIR-Q029

```yaml
QID: G07-PURCHASE_REPAIR-Q029
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A vendor's lead time that would clearly miss the repair's promised date must be surfaced
  at the moment the part is ordered, not discovered only when the promised date has
  already passed.
WHY_IT_MATTERS: >
  Discovering the miss only after the promised date has passed is far too late to manage
  the customer's expectations or find an alternative.
DISCONFIRMING_OBSERVATION: >
  A part is ordered with a vendor lead time that clearly exceeds the repair's promised
  date, and nothing flags the conflict at the time of ordering.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Order a part whose vendor lead time exceeds the time remaining before the repair's
  promised date, and check whether a warning is raised.
```

## G07-PURCHASE_REPAIR-Q030

```yaml
QID: G07-PURCHASE_REPAIR-Q030
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to the vendor's committed delivery date after the order was placed must be re-
  evaluated against the repair's promised date, and any resulting miss must be flagged
  rather than silently absorbed.
WHY_IT_MATTERS: >
  A miss that is silently absorbed rather than flagged leaves the promised date broken
  with nobody aware until the customer notices.
DISCONFIRMING_OBSERVATION: >
  A vendor pushes back its committed delivery date after the order was placed, and the
  resulting conflict with the repair's promised date is not flagged.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Place an order for a repair's part, have the vendor later push back its delivery
  commitment past the repair's promised date, and check for a flag.
```

## G07-PURCHASE_REPAIR-Q031

```yaml
QID: G07-PURCHASE_REPAIR-Q031
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A part received before the repair record it was purchased for has been created must be
  held identifiably against that anticipated need, not absorbed into general stock
  unlinked from any repair.
WHY_IT_MATTERS: >
  An anticipatory purchase that loses its link to the need it was meant for becomes
  indistinguishable from ordinary stock, defeating the reason it was ordered early.
DISCONFIRMING_OBSERVATION: >
  A part ordered in anticipation of a repair not yet logged is received into general stock
  with no identifiable link to the anticipated need.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place a purchase in anticipation of a repair before the repair record exists, receive
  the part, then create the repair, and check whether a link exists.
```

## G07-PURCHASE_REPAIR-Q032

```yaml
QID: G07-PURCHASE_REPAIR-Q032
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A repair cancelled after its part purchase was placed but before the part arrived must
  prevent that arriving part from being received directly onto a repair that no longer
  exists, forcing an explicit redirection.
WHY_IT_MATTERS: >
  Receiving directly onto a repair that no longer exists either fails badly or silently
  attaches the part to nothing meaningful.
DISCONFIRMING_OBSERVATION: >
  A part purchased for a repair that was cancelled before the part arrived is received
  directly against that now-cancelled repair with no redirection step.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel a repair after its part purchase is placed but before the part arrives, then
  receive the part, and check where it lands.
```

## G07-PURCHASE_REPAIR-Q033

```yaml
QID: G07-PURCHASE_REPAIR-Q033
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a repair's part need and a separate stock replenishment need are both satisfied by
  the same incoming purchase line, one explicit rule must decide which need the arriving
  quantity is applied to first.
WHY_IT_MATTERS: >
  An undecided priority between a repair's need and a general replenishment need risks the
  repair being starved by a demand it has no visibility into.
DISCONFIRMING_OBSERVATION: >
  A single incoming purchase line intended to cover both a repair's part need and a
  separate stock replenishment need is applied to one of them with no determinable rule
  for which.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a repair's part need and a stock replenishment need that would both be satisfied
  by the same incoming purchase line, and observe which is served.
```

## G07-PURCHASE_REPAIR-Q034

```yaml
QID: G07-PURCHASE_REPAIR-Q034
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A part's cost used to value a repair must be fixed at the point the repair's cost is
  settled, not silently drift if the vendor's price for that part changes on a later,
  unrelated purchase.
WHY_IT_MATTERS: >
  A repair's already-settled cost changing because of a later, unrelated purchase
  misstates what that specific repair actually cost.
DISCONFIRMING_OBSERVATION: >
  A repair's recorded part cost changes after settlement because the vendor's price for
  that part changed on a later, unrelated purchase.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Settle a repair's cost including a purchased part, then place a later unrelated purchase
  of the same part at a different price, and check the settled repair's cost.
```

## G07-PURCHASE_REPAIR-Q035

```yaml
QID: G07-PURCHASE_REPAIR-Q035
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening a repair after it was closed, where the part purchased for it had already been
  returned or reallocated elsewhere, must not assume that part is still available to
  satisfy the reopened work.
WHY_IT_MATTERS: >
  Assuming a part is still there when it was actually returned or given to another repair
  sets up the reopened work to fail when the part isn't found.
DISCONFIRMING_OBSERVATION: >
  A closed repair is reopened, and it still shows as having its originally purchased part
  available even though that part was returned or reallocated after closure.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Close a repair, return or reallocate the part that was purchased for it, then reopen the
  repair, and check what it shows as available.
```

## G07-PURCHASE_REPAIR-Q036

```yaml
QID: G07-PURCHASE_REPAIR-Q036
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a purchase order for a repair part after the vendor has already begun
  fulfilling it must be reconciled against whatever the repair currently believes is still
  coming, not leave the repair expecting a part procurement no longer intends to deliver.
WHY_IT_MATTERS: >
  A repair left expecting a part that procurement no longer intends to deliver will wait
  indefinitely for something that is never coming.
DISCONFIRMING_OBSERVATION: >
  A purchase order for a repair's part is cancelled after the vendor already began
  fulfilling it, and the repair's expectation of receiving that part is not updated.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a purchase order after the vendor has begun fulfilment, where a repair depends on
  it, and check what the repair still expects.
```

## G07-PURCHASE_REPAIR-Q037

```yaml
QID: G07-PURCHASE_REPAIR-Q037
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Ordering more of a part than the repair actually needs, to meet a vendor's minimum order
  quantity, must leave the surplus explicitly available for other use, not stranded as an
  unexplained cost against the one repair.
WHY_IT_MATTERS: >
  Charging an entire minimum-order quantity to one repair when only a fraction was
  actually needed overstates that repair's true cost and hides usable surplus.
DISCONFIRMING_OBSERVATION: >
  A part ordered above what one repair needs, to satisfy a vendor minimum, has its full
  purchased quantity and cost attributed to that one repair with the surplus left
  unavailable elsewhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Order a part for a repair at a quantity above its actual need because of a vendor
  minimum, receive it, and check how the surplus and its cost are handled.
```

## G07-PURCHASE_REPAIR-Q038

```yaml
QID: G07-PURCHASE_REPAIR-Q038
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A vendor or part discontinued between the time a repair is diagnosed and the time its
  part is actually ordered must be surfaced as a procurement problem for that repair, not
  fail silently at order time with no link back to the waiting repair.
WHY_IT_MATTERS: >
  A silent order-time failure with no link back to the waiting repair leaves the repair
  blocked with no explanation anyone can act on.
DISCONFIRMING_OBSERVATION: >
  A part is discontinued between a repair's diagnosis and its actual ordering, and the
  resulting order failure carries no link back to the repair that needed it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Diagnose a repair needing a specific part, have the vendor discontinue that part before
  the order is placed, attempt the order, and check what the repair shows.
```

## G07-PURCHASE_REPAIR-Q039

```yaml
QID: G07-PURCHASE_REPAIR-Q039
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A purchase placed for a repair that fails to be confirmed by the vendor must leave the
  repair's status reflecting that the need is still unmet, not reflect the optimistic
  state that a part is on the way.
WHY_IT_MATTERS: >
  A repair believing a part is on the way when the vendor never actually confirmed the
  order misleads scheduling and the customer.
DISCONFIRMING_OBSERVATION: >
  A purchase placed for a repair's part is not confirmed by the vendor, yet the repair's
  status shows the part as on the way.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place a purchase for a repair's part, have the vendor fail to confirm it, and check what
  the repair's status shows.
```

## G07-PURCHASE_REPAIR-Q040

```yaml
QID: G07-PURCHASE_REPAIR-Q040
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The authority to approve an urgent repair-driven purchase above a normal spending limit
  must belong to a defined role, not default to whoever happens to be handling the repair
  at the time.
WHY_IT_MATTERS: >
  Letting whoever happens to be handling the repair approve an above-limit purchase by
  default removes the independent check the limit exists to provide.
DISCONFIRMING_OBSERVATION: >
  An urgent repair-driven purchase above the normal spending limit is approved by the
  person handling the repair with no distinct approval role involved.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Raise an urgent above-limit purchase from a repair being handled by a single person, and
  check who approves it.
```

## G07-PURCHASE_REPAIR-Q041

```yaml
QID: G07-PURCHASE_REPAIR-Q041
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A technician authorized to diagnose a repair and identify the needed part must not, by
  that fact alone, also hold authority to commit the purchase, unless the business has
  explicitly combined those roles.
WHY_IT_MATTERS: >
  Merging diagnosis and purchase authority by default removes the separation of duties a
  business may specifically rely on for spending control.
DISCONFIRMING_OBSERVATION: >
  A technician who identified a needed part is able to commit its purchase with no
  separate authorization step, where the business has not explicitly combined those roles.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a technician with diagnostic access but not purchasing authority, attempt to commit a
  purchase for a part identified during diagnosis.
```

## G07-PURCHASE_REPAIR-Q042

```yaml
QID: G07-PURCHASE_REPAIR-Q042
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two repairs raised in quick succession for the same scarce part must not each be told,
  independently, that a single incoming order will cover their need in full.
WHY_IT_MATTERS: >
  Both repairs proceeding on the belief they are fully covered leads to one being blocked
  with no warning once the shared shortfall is discovered.
DISCONFIRMING_OBSERVATION: >
  Two repairs raised in quick succession for the same scarce part each show a single,
  insufficient incoming order as covering their need in full.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Raise two repairs in quick succession needing more of a part than one incoming order
  line will deliver, and check what each is told.
```

## G07-PURCHASE_REPAIR-Q043

```yaml
QID: G07-PURCHASE_REPAIR-Q043
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A repair's part purchase and its vendor terms must never be visible to, or draw against,
  a different tenant's stock or purchase commitments, even where the same part is used by
  both.
WHY_IT_MATTERS: >
  Cross-tenant visibility or consumption of a repair's procurement is a direct data-
  isolation and confidentiality failure between unrelated businesses.
DISCONFIRMING_OBSERVATION: >
  A repair's part purchase or vendor terms in one tenant are visible to, or drawn against
  by, a different tenant's stock or purchasing.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set up the same part under two different tenants with a repair-driven purchase in one,
  and check whether the other tenant can see or draw against it.
```

## G07-PURCHASE_REPAIR-Q044

```yaml
QID: G07-PURCHASE_REPAIR-Q044
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a repair is permitted to raise its own purchase at all, as opposed to only
  requesting one through a separate procurement step, must be governed by an explicit
  configuration, and a repair must not silently gain or lose that capability based on
  unrelated settings.
WHY_IT_MATTERS: >
  A capability that appears or disappears based on unrelated settings makes procurement
  behaviour unpredictable and impossible to govern deliberately.
DISCONFIRMING_OBSERVATION: >
  A repair gains or loses the ability to raise its own purchase directly as a side effect
  of an unrelated configuration change, with no explicit setting governing it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change an unrelated configuration setting and check whether a repair's ability to raise
  its own purchase directly changes as a result.
```

## G07-PURCHASE_REPAIR-Q045

```yaml
QID: G07-PURCHASE_REPAIR-Q045
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A part purchased and received for a repair must correctly reduce whatever open demand or
  requisition originally signaled the need, not leave that upstream demand appearing
  unfulfilled after the part has actually arrived.
WHY_IT_MATTERS: >
  An upstream need that still shows as unfulfilled after the part has actually arrived
  leads to unnecessary duplicate ordering or false urgency.
DISCONFIRMING_OBSERVATION: >
  A part is purchased and received for a repair, but the demand or requisition that
  originally signaled the need still shows as open.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Raise a repair's part need through whatever upstream demand mechanism exists, purchase
  and receive the part, and check the upstream demand's status.
```

## G07-PURCHASE_REPAIR-Q046

```yaml
QID: G07-PURCHASE_REPAIR-Q046
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A repair's linked purchase must remain reachable and identifiable from the repair record
  for as long as the repair itself is retained, even after the purchase order it points to
  is closed, archived, or otherwise no longer active.
WHY_IT_MATTERS: >
  Losing the link once the purchase order is no longer active erases the repair's own
  procurement history at exactly the point someone might need to review it.
DISCONFIRMING_OBSERVATION: >
  A repair's linked purchase becomes unreachable or unidentifiable from the repair record
  once the purchase order it points to is closed or archived.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete and archive a purchase order linked to a repair, then attempt to trace that
  purchase from the still-retained repair record.
```

## G07-PURCHASE_REPAIR-Q047

```yaml
QID: G07-PURCHASE_REPAIR-Q047
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A repair with no part requirement at all must never show a phantom procurement step
  waiting on nothing, and a repair that does need a part must never be closeable while
  that purchase remains genuinely open.
WHY_IT_MATTERS: >
  A phantom wait on nothing wastes attention chasing a non-existent procurement step,
  while closing over a genuinely open purchase hides an unresolved commitment.
DISCONFIRMING_OBSERVATION: >
  A repair with no part requirement shows a procurement step still waiting, or a repair
  with a genuinely open purchase is closeable without resolving it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Check the procurement status of a repair with no part requirement at all, and separately
  attempt to close a repair with a purchase still genuinely open.
```

## G07-PURCHASE_REPAIR-Q048

```yaml
QID: G07-PURCHASE_REPAIR-Q048
MODULE: purchase_repair
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A repair's own record of what part it is waiting on and the purchase order's record of
  what it was ordered to fulfil must agree; where a purchase was redirected to a different
  repair or use, the original repair must not continue to claim it as its expected part.
WHY_IT_MATTERS: >
  Two records disagreeing about what a purchase is for means at least one of them is
  acting on wrong information about whether its need is covered.
DISCONFIRMING_OBSERVATION: >
  A purchase originally raised for one repair is redirected to fulfil a different repair
  or use, and the original repair's record continues to show that purchase as its expected
  part.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise a purchase for one repair's part need, redirect that purchase to a different
  repair or use before it completes, and check what the original repair still claims.
```
