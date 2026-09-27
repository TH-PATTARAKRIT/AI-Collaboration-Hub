# SMEsPlus ENTERPRISE SUITE
## GMVQ — G11 EVENTS / event_product Module Bridge MVQ Bank

**Document ID:** GMVQ-G11-EVENT_PRODUCT-MVQ50-V1.00
**Group:** G11 EVENTS
**Module Metadata:** `event_product`
**Wave:** W2
**Author Cell:** P-E1 (GMVQ Question Factory — Production Team P-E1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50

## Purpose

`event_product` is a BRIDGE module of Group G11 EVENTS, per the GMVQ Bridge Module Rule V1.00. It
exists only where a sellable catalogue item's own model of an item — generally available,
independently priced, sellable until deliberately withdrawn — disagrees with the occasion's model
of a finite, dated thing: a seat that runs out, a ticket type with its own allotment, and a fixed
moment after which the whole premise of "still sellable" needs a deliberate answer rather than a
default one.

No question in this bank restates a registration-mechanics invariant owned by the `event` base
bank — concurrency at the point of registration itself, waiting-list promotion order, the general
cancellation-and-refund path, or attendance recording are that bank's questions. Every question
here was checked against the bridge removal test in the GMVQ Bridge Module Rule V1.00 before being
kept: if the catalogue item and the occasion were used entirely apart from each other, would the
question still make sense? A question that survives that test does not belong in this bank.

Before authoring, this bank's hypotheses were checked against the sibling `event` base bank's own
authored questions on disk, per the Bridge Module Rule's mandatory pre-authoring step, to avoid
restating an invariant that bank already owns directly.

Question text is source-neutral: no vendor or product name, no technical identifier (model, table,
field, method, XML ID, API path), and the module's own metadata name never appears outside the
`MODULE:` field. Generic business language is used throughout — "the occasion", "the catalogue
item", "the ticket type" — rather than any reference to how a specific implementation represents
the seam.

## Control

- Every question fails only at the seam between a catalogue item's own model of a sellable thing
  and the occasion's model of a finite, dated thing, and was checked against the bridge removal
  test before being kept.
- Every question carries a concrete `DISCONFIRMING_OBSERVATION` describing a genuine failure
  state, never a restatement of its own hypothesis.
- No padding: 50 questions exist because they test 50 distinct material seam hypotheses; none was
  trimmed or stretched to hit the count.
- Cross-checked against the `event` base bank's authored questions on disk at authoring time
  (`grep -h 'HYPOTHESIS' G11_EVENTS/*.md`) to avoid restating its invariants.
- Coverage follows the Bridge Module Rule's seam categories: ordering, partiality, ownership,
  timing, reversal, quantity and money, lifecycle mismatch, error asymmetry, and authority.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this
  bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G11-EVENT_PRODUCT-Q001

```yaml
QID: G11-EVENT_PRODUCT-Q001
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A catalogue item whose own configuration marks it as always orderable does not remain purchasable
  once the occasion it is linked to has actually reached its capacity — the catalogue's own
  "always available" setting does not override the seam's finite state.
WHY_IT_MATTERS: >
  A buyer who successfully purchases an item that promises a seat that no longer exists, because
  the catalogue side never checked the linked occasion's own capacity, has paid for something that
  cannot be delivered.
DISCONFIRMING_OBSERVATION: >
  The linked occasion has reached its configured capacity, and its catalogue item can still be
  purchased as if it had unlimited availability.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure a catalogue item marked always orderable and link it to a finite, dated occasion,
  bring that occasion to full capacity, and attempt to purchase the item.
```

## G11-EVENT_PRODUCT-Q002

```yaml
QID: G11-EVENT_PRODUCT-Q002
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where a catalogue item carries its own price independently of the ticket type it represents, the
  amount a buyer is actually charged is the one governing figure for that purchase, and it is not
  possible for the two to silently disagree so that the buyer pays one figure while the occasion
  records a different one as owed for that ticket type.
WHY_IT_MATTERS: >
  A silent mismatch between what was charged and what the occasion believes was charged corrupts
  reconciliation between the sale and the seat it is supposed to represent.
DISCONFIRMING_OBSERVATION: >
  A purchase completes at one price on the catalogue side while the occasion's own record of what
  was paid for that ticket type shows a different figure.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a catalogue item's price to differ from its linked ticket type's own configured price,
  complete a purchase, and compare the amount charged against what the occasion records as paid.
```

## G11-EVENT_PRODUCT-Q003

```yaml
QID: G11-EVENT_PRODUCT-Q003
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A catalogue item does not remain purchasable once the occasion's fixed date has already passed;
  the catalogue side's own sale window is not allowed to outlive the finite thing it is supposed to
  represent.
WHY_IT_MATTERS: >
  Selling access to something whose fixed date has already passed produces a paying buyer with no
  possible way to receive what they paid for.
DISCONFIRMING_OBSERVATION: >
  The occasion's fixed date has passed, and its catalogue item can still be purchased through the
  ordinary sale path.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Let an occasion's fixed date pass without closing its catalogue item, then attempt an ordinary
  purchase of that item.
```

## G11-EVENT_PRODUCT-Q004

```yaml
QID: G11-EVENT_PRODUCT-Q004
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Archiving a catalogue item in the catalogue does not silently strand the registrations already
  created from earlier purchases of it — those registrations remain intact and traceable back to
  the item that produced them, even after the item itself is no longer offered for sale.
WHY_IT_MATTERS: >
  A registrant whose seat traces back to an item that has since vanished from the catalogue could
  find their own record broken by a change made for an entirely unrelated catalogue-management
  reason.
DISCONFIRMING_OBSERVATION: >
  Archiving a catalogue item breaks the link, the display, or the integrity of registrations that
  were already created from earlier purchases of it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Purchase a catalogue item to create a registration, archive that catalogue item, and check
  whether the existing registration remains intact and traceable.
```

## G11-EVENT_PRODUCT-Q005

```yaml
QID: G11-EVENT_PRODUCT-Q005
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  One catalogue item cannot be mapped to two different ticket types at the same time without an
  explicit rule governing which ticket type a given purchase actually produces; the mapping is not
  allowed to be ambiguous at the moment of purchase.
WHY_IT_MATTERS: >
  An ambiguous mapping means the seat a buyer actually receives depends on an internal tie-break
  nobody decided, which can silently misassign people to the wrong ticket type's price, capacity,
  and privileges.
DISCONFIRMING_OBSERVATION: >
  A catalogue item mapped to two different ticket types produces a purchase where which ticket
  type was actually granted cannot be determined, or is determined inconsistently across purchases.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure one catalogue item mapped to two different ticket types on the same occasion, complete
  a purchase, and determine which ticket type the resulting registration actually received.
```

## G11-EVENT_PRODUCT-Q006

```yaml
QID: G11-EVENT_PRODUCT-Q006
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where one ticket type is represented by two different catalogue items, for example under two
  different sale channels, a purchase through either item draws against the same underlying
  allotment, and the two items never behave as though each owned a separate, independent capacity.
WHY_IT_MATTERS: >
  If each catalogue item silently tracked its own capacity for what is actually one ticket type,
  the combined sales across both items could oversell the type's true allotment without either
  item ever individually appearing full.
DISCONFIRMING_OBSERVATION: >
  Two catalogue items both mapped to the same ticket type each report their own independent
  remaining capacity rather than sharing one figure drawn from the ticket type's true allotment.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Map two different catalogue items to the same ticket type, purchase against each, and compare
  the remaining capacity each one reports against the ticket type's actual remaining allotment.
```

## G11-EVENT_PRODUCT-Q007

```yaml
QID: G11-EVENT_PRODUCT-Q007
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where the catalogue item and the occasion could each independently determine the tax treatment
  of a sale — a general catalogue tax classification against a treatment appropriate to the
  occasion's own location — the seam resolves this to a single, explicit governing choice rather
  than silently applying whichever one happens to be evaluated last.
WHY_IT_MATTERS: >
  An unresolved conflict between the two tax treatments could apply the wrong rate to real
  transactions with no one having actually decided which rule should win.
DISCONFIRMING_OBSERVATION: >
  A purchase's applied tax treatment changes depending on incidental processing order rather than
  a single documented rule for which side, catalogue or occasion, governs it.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a catalogue item and its linked occasion with differing tax treatments and complete a
  purchase, checking which treatment is actually applied and whether that choice is documented.
```

## G11-EVENT_PRODUCT-Q008

```yaml
QID: G11-EVENT_PRODUCT-Q008
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where the catalogue item's own income attribution and the occasion's own revenue-recognition
  timing could each independently govern where and when a sale's value lands, the seam applies a
  single explicit rule rather than letting the catalogue side's ordinary sale-recognition timing
  silently override the occasion's own fixed-date-based timing.
WHY_IT_MATTERS: >
  If the catalogue side recognizes value at the moment of sale while the occasion's own accounting
  expects it recognized at or around the fixed date, the same sale could be reported as earned
  twice, in two different periods, or in neither correctly.
DISCONFIRMING_OBSERVATION: >
  The value from one sale of the catalogue item is reflected under two different recognition
  timings depending on which side's report is consulted.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a purchase of the catalogue item well before the occasion's fixed date and compare when
  its value is recognized under the catalogue's own reporting against the occasion's own
  reporting.
```

## G11-EVENT_PRODUCT-Q009

```yaml
QID: G11-EVENT_PRODUCT-Q009
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Where the catalogue's own general mechanism for item variants is used to offer a choice that is
  meant to correspond to distinct ticket types, selecting a given variant reliably and
  deterministically produces the ticket type it is meant to represent, never a different one.
WHY_IT_MATTERS: >
  A variant that is supposed to mean one ticket type but occasionally produces another would
  silently misassign buyers to the wrong price, capacity pool, or privileges without either side
  noticing.
DISCONFIRMING_OBSERVATION: >
  Selecting a specific catalogue variant produces a registration under a ticket type other than
  the one that variant is configured to represent.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure catalogue item variants each meant to correspond to a distinct ticket type, purchase
  each variant, and verify which ticket type each purchase actually produces.
```

## G11-EVENT_PRODUCT-Q010

```yaml
QID: G11-EVENT_PRODUCT-Q010
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two catalogue items that were created as independent listings but both point at the same
  underlying finite allotment are recognized by the seam as sharing that allotment; a sale through
  one is reflected in what the other reports as remaining, rather than each drawing down a private
  copy of a count that is actually singular.
WHY_IT_MATTERS: >
  Two duplicated listings each silently tracking their own copy of what is really one finite count
  is a direct path to overselling that allotment without either listing ever individually
  appearing exhausted.
DISCONFIRMING_OBSERVATION: >
  A sale through one of two catalogue items pointing at the same underlying allotment is not
  reflected in what the other item reports as remaining.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create two catalogue items independently configured to point at the same underlying finite
  allotment, purchase through one, and check whether the other's reported remaining availability
  changes accordingly.
```

## G11-EVENT_PRODUCT-Q011

```yaml
QID: G11-EVENT_PRODUCT-Q011
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Purchasing more than one unit of the catalogue item in a single order line reliably produces the
  correct number of individual registrant slots, one per unit purchased, rather than one shared
  registration record standing in for several seats or several registrations drawing against only
  one seat.
WHY_IT_MATTERS: >
  A mismatch between units purchased and seats actually created either strands paid-for seats that
  never materialize as registrations, or hands out more seats than were actually paid for.
DISCONFIRMING_OBSERVATION: >
  A purchase of more than one unit of the catalogue item produces a number of registration slots
  that does not match the quantity actually purchased.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Purchase a quantity greater than one of a catalogue item linked to a ticket type in a single
  order line, and count the resulting registration slots against the quantity purchased.
```

## G11-EVENT_PRODUCT-Q012

```yaml
QID: G11-EVENT_PRODUCT-Q012
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Turning off a catalogue item's own "available for sale" toggle only closes that specific sale
  path; it does not, by itself, also close direct registration against the ticket type it
  represents through a path that does not go through the catalogue at all.
WHY_IT_MATTERS: >
  If the catalogue toggle were mistaken for a control over the ticket type itself, an organizer
  trying to pause catalogue sales specifically could unintentionally also block direct
  registrations, or could believe direct registration was blocked when it was not.
DISCONFIRMING_OBSERVATION: >
  Disabling the catalogue item's availability for sale also prevents, or fails to prevent, direct
  registration against the ticket type in a way that does not match what the toggle is documented
  to control.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Disable a catalogue item's availability for sale while leaving its linked ticket type otherwise
  open, and attempt both a catalogue purchase and a direct registration against that ticket type.
```

## G11-EVENT_PRODUCT-Q013

```yaml
QID: G11-EVENT_PRODUCT-Q013
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where the catalogue item carries its own sale start and end window separate from the occasion's
  own registration open and cutoff window, whichever window is more restrictive at any given moment
  is the one that actually governs whether a purchase can succeed.
WHY_IT_MATTERS: >
  If the catalogue's own window is looser than the occasion's actual registration window, a buyer
  could complete a purchase for a ticket type whose registration is already closed, and be left
  holding a payment for something that can no longer be honored.
DISCONFIRMING_OBSERVATION: >
  A purchase succeeds through the catalogue item during a period when the linked ticket type's own
  registration window is already closed.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure a catalogue item's own sale window to extend beyond the linked ticket type's
  registration cutoff, and attempt a purchase in the gap between the two.
```

## G11-EVENT_PRODUCT-Q014

```yaml
QID: G11-EVENT_PRODUCT-Q014
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Returning a purchased catalogue item's order line through the catalogue's own ordinary return
  path correctly cancels the registration it created and frees the seat it held, rather than
  reversing only the money while leaving the registration itself confirmed and the seat still
  occupied.
WHY_IT_MATTERS: >
  A return that only touches the money leaves a seat held by someone who has, from the
  organization's own accounting perspective, been refunded and is no longer a paying registrant.
DISCONFIRMING_OBSERVATION: >
  A catalogue-side return of the item's order line completes and the registration it originally
  created remains confirmed, with its seat still counted as held.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Purchase a catalogue item to create a registration, return the order line through the ordinary
  catalogue return path, and check whether the registration is cancelled and the seat freed.
```

## G11-EVENT_PRODUCT-Q015

```yaml
QID: G11-EVENT_PRODUCT-Q015
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When the registration created by a catalogue purchase is cancelled directly, on the occasion
  side rather than through a catalogue return, the originating order line reflects that
  cancellation rather than continuing to show as an ordinary completed, fulfilled sale.
WHY_IT_MATTERS: >
  An order line that still looks fully completed and fulfilled, after the seat it paid for was
  cancelled on the other side of the seam, misrepresents what was actually delivered and could
  block a legitimate later refund claim from being recognized.
DISCONFIRMING_OBSERVATION: >
  A registration created by a catalogue purchase is cancelled directly, and the originating order
  line shows no reflection of that cancellation, continuing to appear as an ordinary completed
  sale.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Purchase a catalogue item to create a registration, cancel that registration directly rather
  than through a catalogue return, and check whether the originating order line reflects the
  cancellation.
```

## G11-EVENT_PRODUCT-Q016

```yaml
QID: G11-EVENT_PRODUCT-Q016
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a catalogue-side checkout completes and the buyer is charged, but creating the corresponding
  registration afterward fails, the seam does not leave the buyer charged with no registration and
  no automatic remedy — either the charge is reversed or the registration creation is retried to
  completion.
WHY_IT_MATTERS: >
  A buyer who paid and received nothing in return, with no automatic path back to being made
  whole, is a direct customer-facing failure with a financial dimension attached.
DISCONFIRMING_OBSERVATION: >
  A completed, charged catalogue checkout exists with no corresponding registration ever created,
  and no automatic reversal or retry mechanism addresses the gap.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Complete a catalogue checkout and charge the buyer, then force the subsequent registration
  creation step to fail, and check whether the charge is reversed or the registration is retried.
```

## G11-EVENT_PRODUCT-Q017

```yaml
QID: G11-EVENT_PRODUCT-Q017
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a registration is created successfully but the catalogue-side order fails to finalize
  afterward, the resulting registration is surfaced as an exception rather than standing as an
  ordinary confirmed registrant with no corresponding paid order behind it.
WHY_IT_MATTERS: >
  A registration with no completed paid order behind it is an entitlement the organization is
  honoring for free, and if it looks identical to a normally paid registration, no one will ever
  notice it happened.
DISCONFIRMING_OBSERVATION: >
  A registration exists whose originating catalogue order never finalized, and nothing
  distinguishes that registration from an ordinary, fully paid one.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create a registration through the catalogue purchase path, force the order finalization step to
  fail afterward, and check whether the resulting registration is flagged as an exception.
```

## G11-EVENT_PRODUCT-Q018

```yaml
QID: G11-EVENT_PRODUCT-Q018
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Changing the mapping between a catalogue item and the ticket type it represents, once purchases
  already exist against that mapping, requires an authority distinct from ordinary catalogue item
  editing, and does not retroactively change what those already-completed purchases are understood
  to have bought.
WHY_IT_MATTERS: >
  Someone with only ordinary catalogue-editing authority should not be able to silently redefine
  what a whole set of already-paid purchases actually represents by simply re-pointing the mapping.
DISCONFIRMING_OBSERVATION: >
  An account with only ordinary catalogue item editing authority is able to change the ticket-type
  mapping of an item with existing purchases, and those existing purchases' recorded meaning
  changes as a result.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  With purchases already completed against a catalogue item's mapping to a ticket type, attempt to
  change that mapping using an account with only ordinary catalogue-editing authority, and check
  the effect on the existing purchases.
```

## G11-EVENT_PRODUCT-Q019

```yaml
QID: G11-EVENT_PRODUCT-Q019
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If the occasion itself is deleted or fully cancelled, its catalogue item does not continue to
  exist as an ordinarily purchasable listing with no indication that the thing it represents is
  gone.
WHY_IT_MATTERS: >
  A catalogue item that quietly keeps selling after the thing it represents has been removed
  entirely produces purchases for something that provably cannot ever be delivered.
DISCONFIRMING_OBSERVATION: >
  An occasion is deleted or fully cancelled, and its catalogue item remains purchasable through the
  ordinary sale path with no indication of the underlying removal.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Delete or fully cancel an occasion that has a linked catalogue item, and attempt an ordinary
  purchase of that item afterward.
```

## G11-EVENT_PRODUCT-Q020

```yaml
QID: G11-EVENT_PRODUCT-Q020
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Deleting a catalogue item while active registrations created from it still exist does not break
  the link those registrations rely on for reporting; the registrations remain attributable to
  what they were originally purchased as, even after the catalogue listing itself is gone.
WHY_IT_MATTERS: >
  Reporting that silently loses the connection between a registration and the item it was sold
  through corrupts any sales or channel analysis built on that connection, without ever surfacing
  the loss.
DISCONFIRMING_OBSERVATION: >
  Deleting a catalogue item causes existing registrations created from it to lose their
  attribution to what they were originally purchased as.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Purchase a catalogue item to create a registration, delete that catalogue item, and check
  whether the registration's attribution to its original purchase is preserved.
```

## G11-EVENT_PRODUCT-Q021

```yaml
QID: G11-EVENT_PRODUCT-Q021
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A promotional discount applied at the catalogue level to the item is reflected consistently in
  what the occasion considers the registrant to have actually paid, so the two sides never disagree
  about the true amount received for that seat.
WHY_IT_MATTERS: >
  If the occasion's own record of what was paid ignores a catalogue-level discount, any
  reconciliation, refund calculation, or reporting built on that figure will be wrong by exactly
  the discount amount.
DISCONFIRMING_OBSERVATION: >
  A catalogue-level discount is applied to a purchase, and the occasion's own record of what was
  paid for the resulting seat does not reflect that discount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a catalogue-level discount to a purchase of the item, and compare the amount the occasion
  records as paid for the resulting registration against the actual discounted amount charged.
```

## G11-EVENT_PRODUCT-Q022

```yaml
QID: G11-EVENT_PRODUCT-Q022
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where two catalogue items, each mapped to a different ticket type on the same occasion, are
  purchased together in one order, each line draws down its own mapped ticket type's own
  allotment, and neither line is ever credited against the wrong ticket type's count.
WHY_IT_MATTERS: >
  A combined order is exactly the situation most likely to expose a mapping bug where one line's
  effect leaks onto the other's allotment, since the two lines are processed together rather than
  in isolation.
DISCONFIRMING_OBSERVATION: >
  A combined order purchasing two catalogue items mapped to two different ticket types results in
  one ticket type's allotment being drawn down incorrectly, or the wrong ticket type being credited
  for one of the lines.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place a single order containing two catalogue items mapped to two different ticket types on the
  same occasion, complete the purchase, and verify each ticket type's allotment was drawn down
  correctly.
```

## G11-EVENT_PRODUCT-Q023

```yaml
QID: G11-EVENT_PRODUCT-Q023
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  In a multi-line order where one line is the catalogue item tied to a ticket type and a separate,
  unrelated catalogue line in the same order fails, the ticket-type-linked line's registration is
  still created correctly regardless of the other line's outcome.
WHY_IT_MATTERS: >
  An unrelated line failure should not be able to prevent, corrupt, or delay a seat that the buyer
  otherwise successfully paid for in the same order.
DISCONFIRMING_OBSERVATION: >
  A multi-line order in which an unrelated catalogue line fails results in the ticket-type-linked
  line's registration also failing, being delayed, or not being created, despite that line
  otherwise succeeding.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Place an order combining a ticket-type-linked catalogue item with an unrelated catalogue item,
  force the unrelated line to fail, and check whether the ticket-type-linked line's registration
  is still created correctly.
```

## G11-EVENT_PRODUCT-Q024

```yaml
QID: G11-EVENT_PRODUCT-Q024
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Where the catalogue item's own stated currency and the occasion's own configured currency could
  differ, the seam applies one single, explicit governing currency for the actual charge, rather
  than leaving it to whichever side's currency setting happens to be read at checkout.
WHY_IT_MATTERS: >
  A buyer charged in an unexpected currency because of an unresolved conflict between the two
  sides has a legitimate billing dispute the organization created for itself.
DISCONFIRMING_OBSERVATION: >
  A purchase of the catalogue item is charged in a currency that matches neither a single,
  documented governing rule for which side's currency should apply.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a catalogue item and its linked occasion under differing currencies, complete a
  purchase, and check which currency the charge actually used against any documented rule.
```

## G11-EVENT_PRODUCT-Q025

```yaml
QID: G11-EVENT_PRODUCT-Q025
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Purchasing the catalogue item while capacity is available, where the checkout's own finalize step
  completes only after some delay, still honors the seat that was available at the moment the
  purchase began, rather than being silently re-evaluated against capacity as it stands at the
  later finalize moment.
WHY_IT_MATTERS: >
  A buyer who began a purchase while a seat was genuinely open should not lose it purely because
  someone else's purchase finalized first during the delay, unless the seam explicitly and
  consistently defines finalize-time as the moment that governs.
DISCONFIRMING_OBSERVATION: >
  Two buyers begin a purchase while more than one seat is available, the finalize step for one is
  delayed, and that buyer's already-begun purchase is refused for a seat that was available when
  they started, with no documented rule explaining that the finalize moment, not the start moment,
  governs.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Begin two purchases of the catalogue item while capacity is available, delay one purchase's
  finalize step until the other has consumed the remaining capacity, and observe the delayed
  purchase's outcome.
```

## G11-EVENT_PRODUCT-Q026

```yaml
QID: G11-EVENT_PRODUCT-Q026
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a catalogue item purchase after the linked occasion's fixed date has already passed is
  recognized by the seam as a distinct case from an ordinary pre-date return, with its own
  explicit handling, rather than being processed identically to any other return.
WHY_IT_MATTERS: >
  Treating a post-date cancellation exactly like an ordinary return ignores that the organization's
  own costs and obligations for that occasion are typically already committed by that point.
DISCONFIRMING_OBSERVATION: >
  A catalogue item purchase cancelled after the occasion's fixed date has passed is processed
  through the identical path, with an identical outcome, as a return submitted well before the
  date.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Let an occasion's fixed date pass, then submit a return for a catalogue item purchase tied to
  it, and compare the handling to an equivalent return submitted before the date.
```

## G11-EVENT_PRODUCT-Q027

```yaml
QID: G11-EVENT_PRODUCT-Q027
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A discount authorized at the catalogue or order level that would reduce the ticket type's
  effective price below a floor configured for that ticket type is either blocked or requires
  authority beyond ordinary catalogue-discount authority; the ticket type's own configured floor is
  not silently overridable by a catalogue-side discount.
WHY_IT_MATTERS: >
  If any catalogue discount can push a ticket type's price below its own configured floor with no
  additional check, the floor configured on the occasion side is meaningless.
DISCONFIRMING_OBSERVATION: >
  A catalogue or order-level discount reduces a purchase's effective price below the linked ticket
  type's configured floor with no additional authorization required.
EXPECTED_SURFACE: S2,S4,S7
PRECONDITIONS: >
  Configure a price floor on a ticket type, then apply a catalogue or order-level discount large
  enough to push the effective price below that floor, and observe whether it is blocked or
  requires added authorization.
```

## G11-EVENT_PRODUCT-Q028

```yaml
QID: G11-EVENT_PRODUCT-Q028
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where the catalogue item is offered only as part of a larger bundled kit rather than as a
  standalone line, purchasing the kit still reliably creates the individual registration that the
  ticket-type mapping requires, rather than the mapping being silently skipped because the item was
  not purchased as its own line.
WHY_IT_MATTERS: >
  A buyer who bought a kit including what is meant to be a ticket, and never receives a
  registration because the mapping only fires for standalone lines, has paid for a seat that
  quietly never materializes.
DISCONFIRMING_OBSERVATION: >
  Purchasing a bundled kit containing the ticket-type-mapped catalogue item does not produce the
  corresponding registration that an equivalent standalone purchase of that item would produce.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure the catalogue item as part of a bundled kit, purchase the kit, and check whether the
  expected registration is created.
```

## G11-EVENT_PRODUCT-Q029

```yaml
QID: G11-EVENT_PRODUCT-Q029
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing the catalogue item's price while purchases are actively being placed against it does not
  retroactively alter what a buyer who already completed a purchase at the earlier price is
  considered to have paid.
WHY_IT_MATTERS: >
  Retroactively repricing an already-completed purchase, purely because a later price change
  happened to land while it was still processing, would charge or credit a buyer for a decision
  made after their own transaction was already done.
DISCONFIRMING_OBSERVATION: >
  A price change to the catalogue item, made while other purchases are actively in progress,
  results in an already-completed purchase's recorded amount being altered to match the new price.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a purchase of the catalogue item at one price, then change that item's price, and check
  whether the already-completed purchase's recorded amount changes.
```

## G11-EVENT_PRODUCT-Q030

```yaml
QID: G11-EVENT_PRODUCT-Q030
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Archiving a specific catalogue variant does not leave a ticket type that is still open for
  registration mapped to a listing a buyer can no longer actually reach — the seam either keeps the
  variant reachable while the ticket type remains open, or closes the ticket type in step with the
  variant's archival.
WHY_IT_MATTERS: >
  A ticket type that is nominally still open for registration but whose only catalogue path has
  been archived silently cuts off buyers who would have registered through the catalogue, with
  nothing visibly wrong to explain why.
DISCONFIRMING_OBSERVATION: >
  A catalogue variant mapped to a ticket type is archived while that ticket type still shows as
  open for registration, and no path exists any longer to purchase it through the catalogue.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Map a catalogue item variant to a ticket type, archive that variant while leaving the ticket type
  open, and check whether a buyer can still reach it through any catalogue path.
```

## G11-EVENT_PRODUCT-Q031

```yaml
QID: G11-EVENT_PRODUCT-Q031
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Two independently created catalogue items that are both mapped to the very same ticket type both
  draw down that one shared allotment consistently; purchasing through either one is reflected in
  what the other reports as remaining, so the type's true capacity cannot be exceeded by splitting
  sales across the two listings.
WHY_IT_MATTERS: >
  If each of the two listings silently tracked its own separate count for what is actually one
  ticket type, splitting sales across both would let the true allotment be oversold without either
  listing ever individually appearing exhausted.
DISCONFIRMING_OBSERVATION: >
  Purchases split across two catalogue items mapped to the same ticket type together exceed that
  ticket type's true configured allotment.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Map two independently created catalogue items to the same ticket type with a small allotment,
  purchase across both listings up to and past that allotment, and check whether the true
  allotment was exceeded.
```

## G11-EVENT_PRODUCT-Q032

```yaml
QID: G11-EVENT_PRODUCT-Q032
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Where the catalogue tracks a nominal stock or availability figure for the item separately from
  the ticket type's own actual remaining allotment, the figure shown to a prospective buyer
  reflects the ticket type's true remaining allotment, not a separately tracked catalogue figure
  that could disagree with it.
WHY_IT_MATTERS: >
  A buyer shown a catalogue-side availability figure that disagrees with the ticket type's actual
  remaining allotment is being told something that is not true about whether a seat actually
  exists for them.
DISCONFIRMING_OBSERVATION: >
  The catalogue's own displayed availability figure for the item differs from the ticket type's
  actual remaining allotment at the same moment.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Bring the ticket type's actual remaining allotment to a known figure and compare it against
  whatever availability figure the catalogue item itself displays to a prospective buyer at the
  same moment.
```

## G11-EVENT_PRODUCT-Q033

```yaml
QID: G11-EVENT_PRODUCT-Q033
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Registering directly, without going through the catalogue, and purchasing through the mapped
  catalogue item both draw against the same ticket type's allotment consistently; there is no
  separate count that only one of the two paths actually updates.
WHY_IT_MATTERS: >
  If direct registration and catalogue purchase updated two different counts, the type could be
  oversold by the combination of both paths while each one, looked at alone, still appeared to have
  room.
DISCONFIRMING_OBSERVATION: >
  Registering directly against a ticket type and purchasing the same ticket type through its
  mapped catalogue item are not both reflected in the same remaining-allotment figure.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Register directly against a ticket type that also has a mapped catalogue item, then purchase
  through the catalogue item, and check whether both actions are reflected in the one shared
  remaining-allotment figure.
```

## G11-EVENT_PRODUCT-Q034

```yaml
QID: G11-EVENT_PRODUCT-Q034
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Unpublishing the catalogue item from public sale, while staff retain the ability to register
  directly against the same ticket type, still keeps the ticket type's own capacity correctly
  shared between the two paths — unpublishing is a sale-channel decision, not a capacity-pool
  split.
WHY_IT_MATTERS: >
  If unpublishing accidentally created a separate capacity pool for the staff-only path, the
  organization could oversell the ticket type by combining what it believes are two smaller,
  independent pools.
DISCONFIRMING_OBSERVATION: >
  Unpublishing the catalogue item from public sale results in the staff-only direct registration
  path drawing against a different remaining-allotment figure than the one the catalogue item
  itself would have used.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Unpublish a catalogue item from public sale while leaving staff-side direct registration open
  against its mapped ticket type, and compare the remaining allotment each path would use.
```

## G11-EVENT_PRODUCT-Q035

```yaml
QID: G11-EVENT_PRODUCT-Q035
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A catalogue-side price correction or credit note issued after the linked occasion's fixed date
  has already passed does not reopen, reprocess, or otherwise disturb anything on the already
  concluded occasion side beyond the financial correction itself.
WHY_IT_MATTERS: >
  A purely financial correction that inadvertently reopens or reprocesses a concluded occasion
  record risks corrupting a record that should, by that point, be settled and final.
DISCONFIRMING_OBSERVATION: >
  Issuing a catalogue-side price correction after the occasion's fixed date has passed causes some
  effect on the occasion side beyond the financial correction itself, such as reopening the
  registration or altering its non-financial state.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Let an occasion's fixed date pass, then issue a catalogue-side price correction or credit note
  against a purchase tied to it, and check for any effect on the occasion side beyond the
  financial correction.
```

## G11-EVENT_PRODUCT-Q036

```yaml
QID: G11-EVENT_PRODUCT-Q036
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Someone with authority to edit ordinary catalogue items, but no authority over the occasion
  itself, cannot use that catalogue-editing authority to indirectly change the mapped ticket type's
  own price or capacity.
WHY_IT_MATTERS: >
  If catalogue-editing authority can reach through the mapping to change what the occasion side
  considers the ticket type's price or capacity to be, the separation between the two authorities
  is only nominal.
DISCONFIRMING_OBSERVATION: >
  An account with only catalogue-item editing authority is able to change the mapped ticket type's
  effective price or capacity by editing the catalogue item alone.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Using an account with only catalogue-item editing authority and no authority over the occasion,
  attempt to change the catalogue item in a way that would alter the mapped ticket type's own price
  or capacity, and observe whether it succeeds.
```

## G11-EVENT_PRODUCT-Q037

```yaml
QID: G11-EVENT_PRODUCT-Q037
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where the catalogue item's own configured income account and the occasion's own accounting
  configuration could each independently claim the value of a sale, the seam resolves this to one
  explicit governing account rather than letting the value land wherever whichever side's
  configuration happens to be evaluated first sends it.
WHY_IT_MATTERS: >
  Value from the same sale silently landing against two different possible accounts, depending on
  incidental evaluation order, corrupts financial reporting for whichever side loses the race.
DISCONFIRMING_OBSERVATION: >
  The income account that actually receives the value of a sale differs from run to run of an
  otherwise identical purchase, with no documented rule for which side's configuration governs.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure differing income account attribution on the catalogue item and the occasion's own
  accounting, complete a purchase, and check which account actually receives the value.
```

## G11-EVENT_PRODUCT-Q038

```yaml
QID: G11-EVENT_PRODUCT-Q038
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  If the catalogue's own general stock-tracking mechanism is applied to the item and shows it as
  temporarily unavailable, while the linked ticket type still has open allotment, that catalogue
  stock state does not block a purchase that the ticket type's own allotment would otherwise allow.
WHY_IT_MATTERS: >
  A catalogue mechanism meant for physical stock has no real relationship to a ticket type's
  allotment, and letting it block an otherwise-valid purchase turns an unrelated inventory quirk
  into a lost sale for a seat that genuinely still exists.
DISCONFIRMING_OBSERVATION: >
  The catalogue item shows as out of stock under the catalogue's own general stock mechanism while
  the linked ticket type still has open allotment, and a purchase attempt is blocked because of the
  stock state.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Mark the catalogue item as out of stock under the catalogue's own general stock mechanism while
  its linked ticket type still has open allotment, and attempt a purchase.
```

## G11-EVENT_PRODUCT-Q039

```yaml
QID: G11-EVENT_PRODUCT-Q039
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A catalogue order line associated with the item that is marked complete or fulfilled, in whatever
  general sense the catalogue applies to a deliverable good, is not marked that way unless the
  registration it was supposed to produce actually exists.
WHY_IT_MATTERS: >
  A line marked fulfilled with nothing actually delivered on the occasion side hides exactly the
  failure this seam exists to catch, behind a status that tells everyone looking at the order that
  everything went fine.
DISCONFIRMING_OBSERVATION: >
  An order line for the catalogue item is marked complete or fulfilled while no corresponding
  registration exists on the occasion side.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Force the registration-creation step to fail after an order line for the catalogue item is
  otherwise processed, and check whether that line is still marked complete or fulfilled.
```

## G11-EVENT_PRODUCT-Q040

```yaml
QID: G11-EVENT_PRODUCT-Q040
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A catalogue item duplicated to create a look-alike listing for a separate promotional channel,
  with both listings pointing at the same underlying allotment, draws sales through either listing
  against the one true remaining count, so the combination of the two cannot oversell it.
WHY_IT_MATTERS: >
  A promotional duplicate is exactly the kind of catalogue-management convenience that could
  silently create a second, independently tracked count for what is really one finite allotment,
  reopening the same overselling risk in a new guise.
DISCONFIRMING_OBSERVATION: >
  Sales combined across the original catalogue item and its promotional duplicate exceed the true
  underlying allotment they both point at.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Duplicate a catalogue item for a separate promotional channel, pointing the duplicate at the same
  underlying allotment, sell through both listings up to and past that allotment, and check whether
  it was exceeded.
```

## G11-EVENT_PRODUCT-Q041

```yaml
QID: G11-EVENT_PRODUCT-Q041
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A catalogue item owned by one company cannot be mapped to a ticket type belonging to an occasion
  owned by a different company without that combination being flagged as an authority conflict
  requiring resolution — the seam does not silently accept a cross-company mapping as an ordinary,
  fully coherent configuration.
WHY_IT_MATTERS: >
  A cross-company mapping with nobody having decided whose accounting, whose permissions, and
  whose tax rules govern the resulting sale is exactly the kind of unresolved authority gap that
  produces incorrect financial attribution across a multi-company boundary.
DISCONFIRMING_OBSERVATION: >
  A catalogue item owned by one company is mapped to a ticket type belonging to an occasion owned
  by a different company, and the configuration is accepted with no flag, warning, or required
  resolution of which company's rules govern the resulting sale.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Attempt to map a catalogue item owned by one company to a ticket type belonging to an occasion
  owned by a different company, and observe whether the configuration is flagged or silently
  accepted.
```

## G11-EVENT_PRODUCT-Q042

```yaml
QID: G11-EVENT_PRODUCT-Q042
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Where the catalogue item's own configured sale end date is set later than the ticket type's own
  registration cutoff, a purchase attempted in the gap between the two dates is refused rather than
  succeeding against a ticket type whose registration should already be closed.
WHY_IT_MATTERS: >
  A misconfigured gap between the two dates would let a buyer purchase something the occasion side
  itself no longer considers open for registration, producing a paid buyer for a seat the
  organization believes it already stopped selling.
DISCONFIRMING_OBSERVATION: >
  A purchase attempted after the ticket type's own registration cutoff, but before the catalogue
  item's later configured sale end date, succeeds.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure a catalogue item's sale end date later than its linked ticket type's registration
  cutoff, and attempt a purchase in the gap between the two dates.
```

## G11-EVENT_PRODUCT-Q043

```yaml
QID: G11-EVENT_PRODUCT-Q043
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Removing a ticket type from its occasion while a catalogue item is still actively mapped to it
  also stops that catalogue item from continuing to sell against a ticket type that no longer
  exists.
WHY_IT_MATTERS: >
  A catalogue item that keeps selling after the ticket type behind it has been removed produces
  purchases for something with no defined price, capacity, or terms left to honor them against.
DISCONFIRMING_OBSERVATION: >
  A ticket type is removed from its occasion, and its mapped catalogue item continues to accept
  purchases through the ordinary sale path afterward.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Remove a ticket type from its occasion while a catalogue item remains mapped to it, and attempt
  an ordinary purchase of that catalogue item afterward.
```

## G11-EVENT_PRODUCT-Q044

```yaml
QID: G11-EVENT_PRODUCT-Q044
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A partial refund issued on the catalogue side, for less than the full amount of the order line,
  leaves the underlying registration in a state that correctly reflects the partial nature of the
  refund, rather than either remaining fully confirmed as if nothing were refunded or being
  cancelled outright as if the whole amount were returned.
WHY_IT_MATTERS: >
  A partial refund silently treated as either a full refund or no refund at all leaves the payment
  side and the registration side disagreeing about what was actually settled for that seat.
DISCONFIRMING_OBSERVATION: >
  A partial refund is issued against the order line, and the underlying registration's own state
  does not reflect that the refund was partial rather than full or absent.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Purchase the catalogue item, issue a partial refund against its order line, and check whether
  the underlying registration's state correctly reflects a partial rather than a full or absent
  refund.
```

## G11-EVENT_PRODUCT-Q045

```yaml
QID: G11-EVENT_PRODUCT-Q045
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where the catalogue records its own note of which company or channel a sale came through, that
  attribution correctly identifies the occasion's own owning company for the resulting
  registration, rather than defaulting to whichever company happens to own the catalogue item
  itself when the two differ.
WHY_IT_MATTERS: >
  Misattributed channel or company reporting on the catalogue side would misstate which part of the
  organization actually generated the resulting registration and its revenue.
DISCONFIRMING_OBSERVATION: >
  A sale's recorded company or channel attribution on the catalogue side does not match the
  occasion's own owning company for the resulting registration.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a purchase where the catalogue item's owning company and the occasion's owning company
  are configured to differ, and compare the sale's recorded attribution against the occasion's own
  owning company.
```

## G11-EVENT_PRODUCT-Q046

```yaml
QID: G11-EVENT_PRODUCT-Q046
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where the catalogue item allows a buyer to select add-ons or options that have no equivalent
  concept on the ticket type it maps to, completing such a purchase produces a clear, resolvable
  outcome — either the unsupported option is rejected at the point of sale, or it is recorded
  without silently being assumed to affect the registration in some undefined way.
WHY_IT_MATTERS: >
  An option the occasion side has no way to represent, silently accepted anyway, creates an
  expectation for the buyer that the registration itself has no means of fulfilling.
DISCONFIRMING_OBSERVATION: >
  A purchase completes with an add-on or option selected that the linked ticket type has no
  equivalent concept for, and the resulting registration shows no resolution of what became of that
  selection.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure the catalogue item with an add-on or option that the linked ticket type has no
  equivalent for, complete a purchase selecting it, and check how the resulting registration
  resolves that selection.
```

## G11-EVENT_PRODUCT-Q047

```yaml
QID: G11-EVENT_PRODUCT-Q047
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Where the catalogue item is configured to be sellable on more than one occasion at once, sharing
  the item across occasions does not cause a purchase to be misattributed to the wrong occasion's
  ticket type when more than one occasion is currently active for sale.
WHY_IT_MATTERS: >
  A shared catalogue listing that cannot reliably tell which occasion a given purchase was actually
  for would silently register buyers against the wrong occasion, with no way for either buyer or
  staff to notice until the wrong seat, or no seat, shows up.
DISCONFIRMING_OBSERVATION: >
  With the same catalogue item configured for more than one currently active occasion, a purchase
  is attributed to a different occasion's ticket type than the one the buyer actually selected.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure one catalogue item as sellable for more than one currently active occasion, complete a
  purchase specifying one of them, and verify which occasion's ticket type actually received the
  registration.
```

## G11-EVENT_PRODUCT-Q048

```yaml
QID: G11-EVENT_PRODUCT-Q048
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where a buyer abandons a catalogue checkout after a provisional hold on the ticket type's
  allotment was already placed, that hold is released back to available allotment within a bounded
  time, rather than continuing to hold a seat against a purchase that was never actually completed.
WHY_IT_MATTERS: >
  An abandoned checkout that keeps a seat held indefinitely denies that seat to every other
  prospective buyer for something that was never actually paid for.
DISCONFIRMING_OBSERVATION: >
  A provisional hold placed by an abandoned, never-completed catalogue checkout remains against the
  ticket type's allotment well beyond any reasonable bounded release period.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Begin a catalogue checkout for the item, causing a provisional hold on the linked ticket type's
  allotment, abandon the checkout before completion, and check how promptly the hold is released.
```

## G11-EVENT_PRODUCT-Q049

```yaml
QID: G11-EVENT_PRODUCT-Q049
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A catalogue item's own general-purpose description or image content is not the place the seam
  relies on to convey capacity, date, or eligibility information that has since changed on the
  occasion side; the figures a buyer actually sees at the point of purchase come from the current
  state of the occasion, not from static catalogue content that could have gone stale.
WHY_IT_MATTERS: >
  A buyer relying on stale catalogue description text for capacity or date information, while the
  live checkout figures differ, is being given two different and contradictory pictures of the
  same purchase at the same time.
DISCONFIRMING_OBSERVATION: >
  The catalogue item's own description or listing content states capacity, date, or eligibility
  information that contradicts the occasion's actual current state at the point of purchase, with
  nothing in the purchase flow reconciling the two.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Change an occasion's capacity or date after its catalogue item's description content was
  written, leave the description unchanged, and check whether the purchase flow shows the buyer the
  current occasion state or the stale description.
```

## G11-EVENT_PRODUCT-Q050

```yaml
QID: G11-EVENT_PRODUCT-Q050
MODULE: event_product
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Where an order containing the catalogue item is cancelled by the buyer before checkout completes,
  any provisional hold that order had placed on the ticket type's allotment is released promptly,
  rather than surviving the cancelled order as an orphaned hold against a purchase that no longer
  exists.
WHY_IT_MATTERS: >
  An orphaned hold left behind by a cancelled-before-completion order denies a seat to other
  buyers for a purchase the buyer themselves already withdrew.
DISCONFIRMING_OBSERVATION: >
  An order containing the catalogue item is cancelled before checkout completes, and a provisional
  hold it had placed on the ticket type's allotment remains in place afterward.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Begin an order for the catalogue item that places a provisional hold on the linked ticket type's
  allotment, cancel the order before checkout completes, and check whether the hold is released.
```
