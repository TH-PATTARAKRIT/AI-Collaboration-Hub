# SMEsPlus ENTERPRISE SUITE
## GMVQ — G07 PURCHASE / purchase_requisition Module Adversarial MVQ Bank

**Document ID:** GMVQ-G07-PURCHASE_REQUISITION-MVQ50-V1.00
**Group:** G07 PURCHASE
**Module Metadata:** `purchase_requisition`
**Wave:** W2
**Author Cell:** P17 (GMVQ Question Factory — Internal Production Team 17, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50

## Purpose

`purchase_requisition` is the FAMILY BASE for the requisition family within G07 (Group Brief G07 PURCHASE). It
owns an internal demand gathered and put out to one or more vendors before an order exists: blanket agreements,
calls for tender, vendor selection and award. Two bridge modules, `purchase_requisition_sale` and
`purchase_requisition_stock`, are being authored in parallel by another cell and own where the demand CAME FROM
(a customer commitment, or a stock replenishment rule) and what happens when that origin changes after the
requisition is under way. This bank owns the requisition's OWN invariants only: its lifecycle, the selection and
award decision, blanket-agreement quantity and price and validity, competitive integrity, and the approval
authority over the award itself — never the demand's origin. See Control for the exact exclusion list.

## Control

- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$DIR"/*.md | sort` was run before
  writing a single question. At authoring time the only sibling bank on disk in this group was the BASE module
  bank `G07_PURCHASE_GMVQ_MVQ_62_V1.00_DRAFT.md` (Author Cell P14, 62 questions, order confirmation, quantity
  ordered/received/billed and tolerance, price and tax timing, three-way match). Its ground is entirely about an
  order that already exists; nothing in it addresses demand gathered before an order exists, vendor selection,
  or blanket agreements, so no overlap was found. Neither `purchase_requisition_sale` nor
  `purchase_requisition_stock` existed on disk at authoring time to check against.
- **Exclusion list (demand-origin questions owned by the sibling bridge banks, deliberately NOT asked here):**
  - How a customer commitment creates, sizes, or modifies a requisition or a requisition line.
  - How a stock replenishment rule creates, sizes, or modifies a requisition or a requisition line.
  - Behavior when the originating customer order is changed, reduced, or cancelled after the requisition it fed
    is already under way (response collection, award, or agreement).
  - Behavior when the originating stock rule's trigger condition changes, or no longer applies, after the
    requisition it fed is already under way.
  - Recalculation of demand quantity on the requisition driven by a change at the customer-order or stock-rule
    origin, and reconciling that recalculated demand against responses or an award already recorded.
  - Any question whose disconfirming observation would require reading, replaying, or altering a sale order or a
    stock replenishment rule rather than the requisition itself.
  This bank instead treats the requisition's demand quantity as a given input and asks only about what the
  requisition does with it once it has it: gathering responses, selecting and awarding, and governing a blanket
  agreement's own quantity, price, and validity.
- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong, and the
  disconfirming observation is a distinct event for every question — no two questions share one failure event.
- No padding: 50 questions exist because they test 50 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, auditability, tenant/company boundary, and concurrency (Authoring
  Standard §5).
- This module carries one layer; the `LAYER` field is omitted throughout.
- Clean-room compliance: no vendor or product name, no technical identifier (model, table, field, method, XML
  ID, API path), and no implementation shape appears anywhere in question text; the module's own metadata name
  appears in the `MODULE:` field only.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a Research
  Evidence Join Key only; no Formal Coverage is derived from this bank. Lane A / Lane B: NOT STARTED for this
  module until rolling batch freeze is recorded.
- Coverage map: lifecycle states and what each permits Q001-Q006 · multiple vendor responses, award basis, and
  who may award Q007-Q011 · award to a non-best response and reason recorded Q012-Q014 · blanket agreement
  quantity versus quantity ordered, and exhaustion Q015-Q019 · price agreed at award versus price on the
  resulting order Q020-Q023 · agreement validity period expiring with orders still placed Q024-Q027 ·
  requisition changed after responses received Q028-Q031 · response visibility and competitive integrity
  Q032-Q034 · requisition closed with demand unfulfilled Q035-Q037 · several orders against one requisition and
  the running balance Q038-Q041 · awarded vendor archived or merged Q042-Q044 · approval authority over the
  award distinct from approval of the resulting order Q045-Q048 · concurrency and tenant/company boundary
  Q049-Q050.

## G07-PURCHASE_REQUISITION-Q001

```yaml
QID: G07-PURCHASE_REQUISITION-Q001
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A requisition in a draft state cannot be sent to any vendor for a response; only a requisition that has been
  deliberately advanced to an active state can receive vendor responses.
WHY_IT_MATTERS: >
  Vendors receiving a solicitation for a requisition still in draft could commit to terms on demand the business
  had not actually finalized asking for.
DISCONFIRMING_OBSERVATION: >
  A requisition still in its draft state is sent to a vendor and a vendor response is recorded against it.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to send a requisition to a vendor while it remains in the draft state.
```

## G07-PURCHASE_REQUISITION-Q002

```yaml
QID: G07-PURCHASE_REQUISITION-Q002
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once a requisition has been closed (an award decision made, or explicitly closed without award), it cannot
  silently receive a new vendor response as though it were still open.
WHY_IT_MATTERS: >
  A response accepted into a closed requisition undermines the finality of the closure decision and can confuse
  who actually won.
DISCONFIRMING_OBSERVATION: >
  A vendor response submitted after the requisition has been closed is accepted and recorded exactly as an
  in-time response would be.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Close a requisition, then attempt to record a new vendor response against it.
```

## G07-PURCHASE_REQUISITION-Q003

```yaml
QID: G07-PURCHASE_REQUISITION-Q003
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A cancelled requisition is distinguishable in its own right from a closed one; cancellation represents the
  demand no longer being pursued, not a synonym for having reached an award decision.
WHY_IT_MATTERS: >
  Conflating cancellation with closure-by-award would misrepresent, in later reporting, how much demand was
  actually satisfied versus abandoned.
DISCONFIRMING_OBSERVATION: >
  A requisition cancelled with no award recorded appears, in any downstream status or report, indistinguishable
  from one closed with an award made.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a requisition with no award and compare its resulting state and reporting classification against one
  closed by award.
```

## G07-PURCHASE_REQUISITION-Q004

```yaml
QID: G07-PURCHASE_REQUISITION-Q004
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The set of actions available on a requisition (inviting a vendor, recording a response, awarding, closing,
  cancelling) is governed consistently by its current lifecycle state, not left available regardless of state
  and merely producing an error if attempted out of order.
WHY_IT_MATTERS: >
  Actions that remain visibly available but silently fail out of state create confusion about what a user is
  actually allowed to do next.
DISCONFIRMING_OBSERVATION: >
  An action that is not valid for the requisition's current state (for example, recording a response on a
  cancelled requisition) is presented identically to a valid action rather than being unavailable or clearly
  disabled.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Move a requisition to a state where a given action is invalid, and inspect whether that action is still
  presented as available.
```

## G07-PURCHASE_REQUISITION-Q005

```yaml
QID: G07-PURCHASE_REQUISITION-Q005
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening a closed or cancelled requisition, if permitted at all, is a distinct, auditable action rather than
  something achieved as a side effect of an unrelated edit.
WHY_IT_MATTERS: >
  An accidental reopening as a side effect of an edit would let responses or awards accumulate against a
  requisition the business considered settled.
DISCONFIRMING_OBSERVATION: >
  An unrelated edit to a closed or cancelled requisition's data causes it to revert to an open, response-accepting
  state with no distinct reopening action having been taken.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Make an unrelated data edit to a closed or cancelled requisition and check whether its lifecycle state changes
  as a side effect.
```

## G07-PURCHASE_REQUISITION-Q006

```yaml
QID: G07-PURCHASE_REQUISITION-Q006
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The authority required to cancel a requisition is not lower than the authority required to have opened it in
  the first place.
WHY_IT_MATTERS: >
  If cancellation requires less standing than creation, a low-privilege user could unilaterally abandon a
  sourcing effort someone with more authority deliberately started.
DISCONFIRMING_OBSERVATION: >
  A user without the permission to create or open a requisition is nonetheless able to cancel one that is already
  open.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare the permission required to open a requisition against the permission required to cancel one that is
  already open.
```

## G07-PURCHASE_REQUISITION-Q007

```yaml
QID: G07-PURCHASE_REQUISITION-Q007
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When more than one vendor has responded to the same requisition, awarding it to one response is a distinct,
  recorded decision, not simply whichever response happens to be converted into an order first.
WHY_IT_MATTERS: >
  If award is just "whoever gets ordered first," there is no actual selection decision on record, defeating the
  purpose of collecting competing responses.
DISCONFIRMING_OBSERVATION: >
  With multiple vendor responses recorded, an order can be created from any of them without any of the responses
  having been marked as the chosen, awarded one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record two or more vendor responses on one requisition and attempt to generate an order without first
  designating an award.
```

## G07-PURCHASE_REQUISITION-Q008

```yaml
QID: G07-PURCHASE_REQUISITION-Q008
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The ability to award a requisition to a chosen vendor response is governed by a defined permission, separate
  from the ability merely to record or view vendor responses.
WHY_IT_MATTERS: >
  Without a separate award permission, anyone able to enter a vendor's quote could also unilaterally decide the
  outcome of a competitive process.
DISCONFIRMING_OBSERVATION: >
  Any user able to record a vendor response is, by that same permission alone, also able to make the award
  decision.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare the permission needed to record a vendor response against the permission needed to award the
  requisition.
```

## G07-PURCHASE_REQUISITION-Q009

```yaml
QID: G07-PURCHASE_REQUISITION-Q009
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An award decision references which specific vendor response it is based on, so that the basis for the award
  (the terms actually agreed to) remains traceable rather than the award existing as a bare vendor selection
  disconnected from the response that justified it.
WHY_IT_MATTERS: >
  An award with no link to the response it came from cannot later be checked against what was actually offered,
  undermining any audit of whether the award was reasonable.
DISCONFIRMING_OBSERVATION: >
  The recorded award identifies only the chosen vendor, with no retained link to the specific response (its
  terms, quantity, price) that the award was based on.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Award a requisition among several responses, then check whether the award record retains a link to the
  specific response terms.
```

## G07-PURCHASE_REQUISITION-Q010

```yaml
QID: G07-PURCHASE_REQUISITION-Q010
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Vendor responses not selected in the award are retained on record after the award is made, rather than being
  removed or overwritten once one response is chosen.
WHY_IT_MATTERS: >
  Discarding the losing responses destroys the evidence needed to justify, or challenge, why a particular vendor
  was chosen.
DISCONFIRMING_OBSERVATION: >
  After an award is made, the responses that were not selected are no longer retrievable in their original form.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Award a requisition with multiple responses, then attempt to retrieve the full detail of the responses that
  were not chosen.
```

## G07-PURCHASE_REQUISITION-Q011

```yaml
QID: G07-PURCHASE_REQUISITION-Q011
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a requisition can be awarded to more than one vendor at once (a split award) is an explicit, deliberate
  configuration or action, not something that happens implicitly by generating more than one order from the same
  requisition.
WHY_IT_MATTERS: >
  An implicit split award with no deliberate decision behind it could satisfy the same demand from two vendors
  without anyone intending to split it.
DISCONFIRMING_OBSERVATION: >
  Generating a second order from a requisition already awarded to one vendor is possible with no distinct action
  or record indicating a deliberate split-award decision.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Award a requisition to one vendor, then attempt to generate a further order against it from a different
  vendor's response.
```

## G07-PURCHASE_REQUISITION-Q012

```yaml
QID: G07-PURCHASE_REQUISITION-Q012
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The system permits awarding a requisition to a vendor response that is not the lowest-priced or otherwise most
  favorable one on record; the award decision is not mechanically forced onto whichever response scores best on
  a single measure.
WHY_IT_MATTERS: >
  Real sourcing decisions legitimately weigh factors like reliability, quality, or lead time that outrank price
  alone, and a system that forces price-only selection distorts the business's actual purchasing judgment.
DISCONFIRMING_OBSERVATION: >
  The system blocks, or silently overrides, an attempt to award to a response other than the one with the best
  value on whatever single measure it compares.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to award a requisition to a vendor response that is not the best on price or the system's default
  comparison measure.
```

## G07-PURCHASE_REQUISITION-Q013

```yaml
QID: G07-PURCHASE_REQUISITION-Q013
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the award goes to a response other than the apparent best one on record, a reason can be captured and
  retained against that award decision.
WHY_IT_MATTERS: >
  Without a captured reason, an award that departs from the obvious best offer is indistinguishable, on later
  review, from an unexplained or improper decision.
DISCONFIRMING_OBSERVATION: >
  Awarding to a non-best response provides no way to record or retain a reason for that choice.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Award a requisition to a response other than the apparent best one and attempt to record a reason for the
  decision.
```

## G07-PURCHASE_REQUISITION-Q014

```yaml
QID: G07-PURCHASE_REQUISITION-Q014
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Recording a reason for a non-best award, where the capability exists, is available at the moment of award, not
  something that can only be added well after the order already exists and the original context has faded.
WHY_IT_MATTERS: >
  A reason captured long after the fact is far less reliable evidence of the actual decision than one captured
  at the time.
DISCONFIRMING_OBSERVATION: >
  The only opportunity to record a reason for a non-best award is after an order has already been generated from
  it, not at the point the award itself is made.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to record a reason for a non-best award at the point of awarding, before any order is generated from
  it.
```

## G07-PURCHASE_REQUISITION-Q015

```yaml
QID: G07-PURCHASE_REQUISITION-Q015
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The running total of quantity already ordered against a blanket agreement is tracked against the quantity
  agreed, so that the remaining, un-ordered balance is always determinable rather than requiring a manual tally
  across every order raised against it.
WHY_IT_MATTERS: >
  Without a tracked running balance, no one can reliably tell how much of a blanket commitment remains before
  placing the next order.
DISCONFIRMING_OBSERVATION: >
  After several orders have been placed against a blanket agreement, there is no single figure or view showing
  the remaining un-ordered quantity without manually summing every order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place several orders against one blanket agreement and look for a maintained figure representing the remaining
  balance.
```

## G07-PURCHASE_REQUISITION-Q016

```yaml
QID: G07-PURCHASE_REQUISITION-Q016
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An attempt to order a quantity against a blanket agreement that would exceed the quantity actually agreed is
  either blocked or requires an explicit override, rather than being accepted silently as though the agreement
  had no limit.
WHY_IT_MATTERS: >
  Silently exceeding an agreed quantity limit removes the entire point of having negotiated a capped commitment
  in the first place.
DISCONFIRMING_OBSERVATION: >
  An order quantity that would push the cumulative total beyond the agreed quantity is accepted with no block,
  warning, or required override.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Place orders against a blanket agreement until the agreed quantity would be exceeded by the next one, and
  attempt that next order.
```

## G07-PURCHASE_REQUISITION-Q017

```yaml
QID: G07-PURCHASE_REQUISITION-Q017
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A blanket agreement whose agreed quantity has been fully consumed by orders already placed is recognizable as
  exhausted, distinct from one that still has balance remaining, wherever the business would look to choose
  which agreement to order against.
WHY_IT_MATTERS: >
  An exhausted agreement that looks identical to an active one invites a new order to be placed against a
  commitment that no longer has any capacity left.
DISCONFIRMING_OBSERVATION: >
  A fully consumed blanket agreement presents no differently, in any listing or selection a buyer would use,
  from one that still has remaining balance.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Fully consume a blanket agreement's agreed quantity through orders, then view it alongside an agreement that
  is not yet exhausted.
```

## G07-PURCHASE_REQUISITION-Q018

```yaml
QID: G07-PURCHASE_REQUISITION-Q018
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an order that had been placed against a blanket agreement restores the corresponding quantity to
  the agreement's remaining balance, rather than leaving that quantity permanently counted as consumed.
WHY_IT_MATTERS: >
  A cancelled order that permanently consumes agreement balance would make a business appear to have used up an
  agreement it never actually drew on.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order placed against a blanket agreement leaves the agreement's remaining balance unchanged, as
  though the order still stood.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place an order against a blanket agreement, note the resulting remaining balance, then cancel the order and
  re-check the balance.
```

## G07-PURCHASE_REQUISITION-Q019

```yaml
QID: G07-PURCHASE_REQUISITION-Q019
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether partial receipt or partial billing against an order raised under a blanket agreement affects the
  agreement's tracked balance (which is driven by quantity ordered, not quantity received or billed) is a
  defined, documented behavior rather than an incidental side effect of how receipt or billing happens to be
  recorded.
WHY_IT_MATTERS: >
  An undocumented, incidental link between receipt or billing progress and agreement balance can make the
  balance appear to move for reasons no one intended.
DISCONFIRMING_OBSERVATION: >
  Recording a partial receipt or partial billing against an order changes the blanket agreement's tracked
  remaining balance, with no documented rule describing that this should happen.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a partial receipt or partial billing against an order placed under a blanket agreement and check
  whether the agreement's remaining balance changes as a result.
```

## G07-PURCHASE_REQUISITION-Q020

```yaml
QID: G07-PURCHASE_REQUISITION-Q020
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The price carried onto an order generated from an awarded response matches the price actually recorded in that
  award, and is not independently re-derived from whatever the vendor's general pricing happens to be at the
  moment the order is created.
WHY_IT_MATTERS: >
  Re-deriving price from general vendor pricing instead of the awarded terms would silently substitute a
  different price than the one the business actually agreed to in the sourcing process.
DISCONFIRMING_OBSERVATION: >
  An order generated from an awarded response carries a price that differs from the price recorded in the award,
  matching instead some other, more general pricing source.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set the vendor's general pricing to a different value than the price recorded in the award, generate an order
  from the award, and compare the order's price to the award's price.
```

## G07-PURCHASE_REQUISITION-Q021

```yaml
QID: G07-PURCHASE_REQUISITION-Q021
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If a user changes the price on an order generated from an award, that departure from the awarded price is
  visible on the order rather than silently blending in as though it had always been the awarded price.
WHY_IT_MATTERS: >
  An undetectable departure from the awarded price defeats the purpose of having captured the awarded price as a
  reference in the first place.
DISCONFIRMING_OBSERVATION: >
  Changing the price on an order that came from an award leaves no indication, anywhere on the order, that it now
  differs from what was actually awarded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate an order from an award, change the order's price, and check whether the departure from the awarded
  price is visible.
```

## G07-PURCHASE_REQUISITION-Q022

```yaml
QID: G07-PURCHASE_REQUISITION-Q022
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a blanket agreement fixes a price for its duration, an order placed against it late in the agreement's
  life still carries that fixed price rather than picking up a price that has since changed elsewhere.
WHY_IT_MATTERS: >
  A price that silently drifts away from what a blanket agreement actually fixed defeats the commercial point of
  having locked the price in advance.
DISCONFIRMING_OBSERVATION: >
  An order placed against a blanket agreement, near the end of its validity period, carries a price different
  from the price the agreement fixed, with no explicit renegotiation having occurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place an order against a blanket agreement late in its validity period, after some other pricing source has
  changed, and compare the order's price to the agreement's fixed price.
```

## G07-PURCHASE_REQUISITION-Q023

```yaml
QID: G07-PURCHASE_REQUISITION-Q023
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Overriding the awarded price on a resulting order requires the same standing, at minimum, as approving the
  order itself, rather than being something any order-entry user can quietly do.
WHY_IT_MATTERS: >
  An unauthorized price override on an order undoes the value of having gone through a controlled award process
  at all.
DISCONFIRMING_OBSERVATION: >
  A user without order-approval authority is able to change the price on an order away from the awarded price
  with no additional permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare the permission needed to approve an order against the permission needed to change its price away from
  the awarded value.
```

## G07-PURCHASE_REQUISITION-Q024

```yaml
QID: G07-PURCHASE_REQUISITION-Q024
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An attempt to place an order against a blanket agreement after its validity period has ended is either blocked
  or requires an explicit override, rather than being accepted as though the agreement were still in force.
WHY_IT_MATTERS: >
  Silently honoring an expired agreement extends commercial terms the business never actually agreed to keep
  beyond their term.
DISCONFIRMING_OBSERVATION: >
  An order is placed against a blanket agreement after its stated validity period has ended, with no block or
  override required.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Attempt to place an order against a blanket agreement whose validity period has already passed.
```

## G07-PURCHASE_REQUISITION-Q025

```yaml
QID: G07-PURCHASE_REQUISITION-Q025
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An agreement approaching the end of its validity period with unconsumed balance remaining is distinguishable,
  wherever a buyer would look to select an agreement, from one with plenty of time and balance left.
WHY_IT_MATTERS: >
  A buyer with no visibility into an approaching expiry may fail to use up a remaining commitment in time, or may
  fail to plan the next agreement before a gap opens.
DISCONFIRMING_OBSERVATION: >
  An agreement close to expiry with remaining balance presents identically, in any listing a buyer uses, to one
  far from expiry.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Compare how an agreement nearing expiry with remaining balance is presented against one with substantial time
  left.
```

## G07-PURCHASE_REQUISITION-Q026

```yaml
QID: G07-PURCHASE_REQUISITION-Q026
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order already placed and confirmed against a blanket agreement before it expired is not affected by the
  agreement's subsequent expiry; the order's own validity does not depend on the agreement still being within
  its period.
WHY_IT_MATTERS: >
  An order that becomes retroactively invalid because its parent agreement later expired would create confusion
  for orders already committed to and possibly received.
DISCONFIRMING_OBSERVATION: >
  An order placed while the agreement was valid shows a changed status or becomes blocked from further progress
  once the agreement's validity period later ends.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place and confirm an order against a blanket agreement while it is valid, then let the agreement expire and
  check whether the order's own status is affected.
```

## G07-PURCHASE_REQUISITION-Q027

```yaml
QID: G07-PURCHASE_REQUISITION-Q027
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an order placed shortly before expiry, but not received or billed until after, remains linked to the
  (now-expired) agreement's terms for tolerance and reconciliation purposes is a defined, documented behavior.
WHY_IT_MATTERS: >
  An undocumented answer here means receiving and billing staff have no rule to fall back on when the order's
  timing straddles the agreement's expiry.
DISCONFIRMING_OBSERVATION: >
  No documented rule addresses how receipt or billing tolerance is determined when the order was placed under
  the agreement but processed after the agreement expired.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Place an order against a blanket agreement just before it expires, process receipt or billing after the
  expiry, and check for a documented rule governing that case.
```

## G07-PURCHASE_REQUISITION-Q028

```yaml
QID: G07-PURCHASE_REQUISITION-Q028
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing the requisition's requested terms (quantity, specification, required date) after vendor responses
  have already been recorded does not silently reinterpret those existing responses as though they had been made
  against the new terms.
WHY_IT_MATTERS: >
  Treating old responses as if they answered a changed request would compare offers that were never actually
  made on the same basis.
DISCONFIRMING_OBSERVATION: >
  After the requisition's terms are changed, the previously recorded vendor responses are presented as though
  comparable to the new terms with no flag that they predate the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record vendor responses on a requisition, change its requested terms, and inspect how the existing responses
  are then presented.
```

## G07-PURCHASE_REQUISITION-Q029

```yaml
QID: G07-PURCHASE_REQUISITION-Q029
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to the requisition after responses have been received is itself a visible, retained event,
  distinguishing "the ask changed mid-process" from a requisition whose terms were never altered.
WHY_IT_MATTERS: >
  Without a visible record of the change, no one reviewing the award later can tell whether all vendors were
  actually responding to the same request.
DISCONFIRMING_OBSERVATION: >
  Changing the requisition's terms after responses exist leaves no retained indication that a change occurred at
  that point in the process.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a requisition's terms after responses exist and check for a retained record of that change and when it
  occurred.
```

## G07-PURCHASE_REQUISITION-Q030

```yaml
QID: G07-PURCHASE_REQUISITION-Q030
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Vendors who have already responded are not silently excluded from consideration by a change to the
  requisition; the system does not quietly narrow the field to only those who respond again after the change.
WHY_IT_MATTERS: >
  Silently dropping earlier respondents from consideration after a change could unfairly exclude a vendor from a
  process they engaged with in good faith.
DISCONFIRMING_OBSERVATION: >
  After a requisition change, an earlier response becomes unselectable for award with no explicit action having
  withdrawn or invalidated it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Change a requisition's terms after a response exists, then attempt to award based on that earlier response.
```

## G07-PURCHASE_REQUISITION-Q031

```yaml
QID: G07-PURCHASE_REQUISITION-Q031
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a requisition can be changed at all once responses exist, and what level of change is permitted, is
  governed by a defined rule rather than being unrestricted right up until an award is actually made.
WHY_IT_MATTERS: >
  Unrestricted changes right up to the moment of award make it difficult to ensure every vendor was actually
  competing over the same request.
DISCONFIRMING_OBSERVATION: >
  A requisition already carrying vendor responses can have any of its terms changed with no restriction,
  warning, or distinction from editing a requisition with no responses yet.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the ability to edit a requisition's terms before any response exists against after one or more
  responses have been recorded.
```

## G07-PURCHASE_REQUISITION-Q032

```yaml
QID: G07-PURCHASE_REQUISITION-Q032
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A vendor's response to a requisition is not visible to another vendor who is also responding to the same
  requisition.
WHY_IT_MATTERS: >
  One vendor seeing another's terms during an active competitive process undermines the entire basis for
  soliciting independent competing offers.
DISCONFIRMING_OBSERVATION: >
  A vendor, through any portal or communication path available to them, can see the terms of a response
  submitted by a different vendor to the same requisition.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Record responses from two different vendors on the same requisition and check whether either vendor has any
  means of viewing the other's response.
```

## G07-PURCHASE_REQUISITION-Q033

```yaml
QID: G07-PURCHASE_REQUISITION-Q033
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Internal visibility into vendor responses before an award is made is limited to those with a legitimate role
  in the sourcing decision, not open to every user who can see the requisition exists.
WHY_IT_MATTERS: >
  Broad internal visibility into competing terms before award increases the chance that a decision, or a leak,
  is influenced by something other than the responses on their merits.
DISCONFIRMING_OBSERVATION: >
  Any user able to see that a requisition exists can also see the full detail of every vendor's response before
  an award decision has been made.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Compare the permission needed to see that a requisition exists against the permission needed to see the detail
  of vendor responses on it before award.
```

## G07-PURCHASE_REQUISITION-Q034

```yaml
QID: G07-PURCHASE_REQUISITION-Q034
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once an award has been made, visibility into the losing responses' detail is not automatically extended to the
  awarded vendor.
WHY_IT_MATTERS: >
  Exposing competitors' terms to the winning vendor after the fact, even unintentionally, damages the trust
  other vendors place in the process for future requisitions.
DISCONFIRMING_OBSERVATION: >
  The vendor who won an award is able to see, through any means, the detailed terms of a response submitted by a
  losing vendor on the same requisition.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Make an award among multiple responses and check whether the winning vendor has any means to view a losing
  vendor's response detail.
```

## G07-PURCHASE_REQUISITION-Q035

```yaml
QID: G07-PURCHASE_REQUISITION-Q035
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Closing a requisition without having awarded and ordered the full requested quantity is possible, but leaves a
  visible record that some demand went unfulfilled, rather than the closure looking identical to one where
  everything requested was actually obtained.
WHY_IT_MATTERS: >
  A closure that hides unfulfilled demand can leave a real business need silently unmet with no one aware it was
  never actually satisfied.
DISCONFIRMING_OBSERVATION: >
  A requisition closed with less than the full requested quantity awarded and ordered shows no distinguishable
  indication of the shortfall compared to one fully satisfied.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a requisition after awarding and ordering only part of the requested quantity, and compare its resulting
  record against a fully satisfied requisition.
```

## G07-PURCHASE_REQUISITION-Q036

```yaml
QID: G07-PURCHASE_REQUISITION-Q036
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The requisition's own record retains what quantity was actually requested versus what was ultimately awarded
  and ordered, so the shortfall, if any, can be computed after closure rather than being lost once the
  requisition is no longer active.
WHY_IT_MATTERS: >
  Losing the original requested quantity after closure would make it impossible to later assess how well the
  sourcing process actually served the original need.
DISCONFIRMING_OBSERVATION: >
  After a requisition is closed, the originally requested quantity is no longer retrievable to compare against
  what was actually awarded and ordered.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a partially fulfilled requisition, then attempt to retrieve both the original requested quantity and the
  quantity actually awarded and ordered.
```

## G07-PURCHASE_REQUISITION-Q037

```yaml
QID: G07-PURCHASE_REQUISITION-Q037
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Closing a requisition with demand still outstanding requires no less authority than closing one that was fully
  satisfied; a partial or empty-handed closure is not something that happens to require less oversight than a
  successful one.
WHY_IT_MATTERS: >
  If an unsuccessful closure needs less approval than a successful one, there is less scrutiny exactly where the
  process most needs a second look.
DISCONFIRMING_OBSERVATION: >
  A requisition can be closed with significant unfulfilled demand by a user who would not have the authority to
  close a fully satisfied requisition of the same value.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare the authority required to close a requisition with unfulfilled demand against the authority required
  to close a fully satisfied one of comparable value.
```

## G07-PURCHASE_REQUISITION-Q038

```yaml
QID: G07-PURCHASE_REQUISITION-Q038
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When more than one order has been raised against the same requisition (whether from a split award or from a
  blanket agreement it produced), the requisition's own record reflects the combined progress of all of them,
  not just the most recently created one.
WHY_IT_MATTERS: >
  A requisition that only reflects its latest order would silently lose track of everything ordered before it,
  understating the actual demand already committed.
DISCONFIRMING_OBSERVATION: >
  After a second order is raised against a requisition that already had one, the requisition's tracked progress
  reflects only the second order, with no trace of the first.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Raise two separate orders against the same requisition and inspect whether the requisition's own record
  reflects both.
```

## G07-PURCHASE_REQUISITION-Q039

```yaml
QID: G07-PURCHASE_REQUISITION-Q039
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling one of several orders raised against the same requisition updates that requisition's tracked
  progress to reflect the cancellation, rather than the requisition continuing to count the cancelled order as
  fulfilled demand.
WHY_IT_MATTERS: >
  A requisition that keeps counting a cancelled order as fulfilled would understate how much demand is actually
  still open.
DISCONFIRMING_OBSERVATION: >
  Cancelling one of several orders against a requisition leaves the requisition's tracked fulfilled quantity
  unchanged, still counting the cancelled order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Raise two orders against a requisition, cancel one, and check whether the requisition's tracked progress
  reflects the cancellation.
```

## G07-PURCHASE_REQUISITION-Q040

```yaml
QID: G07-PURCHASE_REQUISITION-Q040
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Each order raised against a requisition retains its own link back to that requisition individually, so that
  the specific set of orders behind a given requisition's total can be enumerated, not just a running number
  with no traceable detail behind it.
WHY_IT_MATTERS: >
  A bare running total with no enumerable detail cannot be checked or explained if the number itself is ever
  questioned.
DISCONFIRMING_OBSERVATION: >
  The requisition shows a combined total from multiple orders but provides no way to list which specific orders
  make up that total.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise several orders against one requisition and attempt to enumerate, from the requisition, exactly which
  orders contribute to its total.
```

## G07-PURCHASE_REQUISITION-Q041

```yaml
QID: G07-PURCHASE_REQUISITION-Q041
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether raising an additional order against a requisition that already has one is permitted at all (versus
  requiring a fresh requisition) is a defined, documented rule connected to how the requisition was awarded (a
  single award versus an agreement intended for repeat use), not an incidental side effect of what the interface
  happens to allow.
WHY_IT_MATTERS: >
  An undocumented, incidental answer here means the difference between "one requisition, one order" and "one
  requisition, many orders" is a technical accident rather than a deliberate business rule.
DISCONFIRMING_OBSERVATION: >
  No documented rule explains why a second order can or cannot be raised against a given requisition, and the
  behavior differs between comparable requisitions with no traceable reason.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to raise a second order against two comparable requisitions, one from a single-vendor award and one
  from an agreement intended for repeat use, and compare the outcomes against any documented rule.
```

## G07-PURCHASE_REQUISITION-Q042

```yaml
QID: G07-PURCHASE_REQUISITION-Q042
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Archiving the vendor record that an active blanket agreement or an in-progress requisition award depends on
  does not silently remove the ability to raise further orders against that still-valid agreement or award.
WHY_IT_MATTERS: >
  An agreement or award that becomes unusable the moment its vendor record is archived for an unrelated reason
  could block legitimate ordering activity with no warning of why.
DISCONFIRMING_OBSERVATION: >
  Archiving the vendor record tied to a still-valid blanket agreement causes orders against that agreement to
  fail or become unavailable, with no clear explanation connecting the failure to the archiving.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Archive the vendor record behind an active blanket agreement and attempt to raise a further order against that
  agreement.
```

## G07-PURCHASE_REQUISITION-Q043

```yaml
QID: G07-PURCHASE_REQUISITION-Q043
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When two vendor records are merged and one of them holds an awarded response or an active agreement, the
  merged result retains that award or agreement rather than it being silently lost in the merge.
WHY_IT_MATTERS: >
  Losing an award or agreement in a vendor merge would erase a real, still-binding commercial commitment with no
  record of what happened to it.
DISCONFIRMING_OBSERVATION: >
  After merging two vendor records, an award or agreement that belonged to the vendor being absorbed is no
  longer retrievable under either the surviving or the absorbed vendor identity.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge two vendor records where one holds an award or active agreement, then check whether that award or
  agreement survives the merge.
```

## G07-PURCHASE_REQUISITION-Q044

```yaml
QID: G07-PURCHASE_REQUISITION-Q044
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A requisition response or award tied to a vendor that is later archived or merged retains an identifiable link
  to which vendor identity it was actually awarded to at the time, even if that identity later changes.
WHY_IT_MATTERS: >
  Losing the historical vendor identity behind an old award would make it impossible to later verify who
  actually won a given requisition.
DISCONFIRMING_OBSERVATION: >
  After the awarded vendor's record is archived or merged, the historical award no longer shows which original
  vendor identity it was actually made to.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive or merge a vendor holding a historical award, then check whether the award still shows the original
  vendor identity it was made to.
```

## G07-PURCHASE_REQUISITION-Q045

```yaml
QID: G07-PURCHASE_REQUISITION-Q045
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Approval of the award decision on a requisition and approval of the resulting order are tracked as separate
  approvals, so that an order generated from an awarded requisition still passes through the order's own
  approval requirement rather than inheriting approval from the award alone.
WHY_IT_MATTERS: >
  Treating award approval as if it were also order approval could let an order with different value or terms
  than the award slip through with no independent check.
DISCONFIRMING_OBSERVATION: >
  An order generated from an awarded requisition is created in an already-approved state with no separate
  order-approval step having occurred.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Award a requisition through its approval process, generate an order from it, and check whether the order still
  requires its own approval step.
```

## G07-PURCHASE_REQUISITION-Q046

```yaml
QID: G07-PURCHASE_REQUISITION-Q046
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an order generated from an award differs from the awarded terms (for example, a changed quantity or
  price), that order's approval requirement reflects the order's own actual value and terms, not the value that
  was originally approved at award.
WHY_IT_MATTERS: >
  An order re-approved based on stale award-time figures rather than its own current terms could pass an
  approval threshold it should not actually clear.
DISCONFIRMING_OBSERVATION: >
  An order whose value has increased beyond what was awarded is approved using the original award-time approval,
  with no reassessment against the order's own higher value.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Award a requisition, generate an order with a higher value or different terms than awarded, and check whether
  the order's approval requirement is reassessed.
```

## G07-PURCHASE_REQUISITION-Q047

```yaml
QID: G07-PURCHASE_REQUISITION-Q047
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The approval limit that governs who may approve an award decision is configured independently of the approval
  limit that governs who may approve the resulting order, so the two thresholds can legitimately differ.
WHY_IT_MATTERS: >
  If the two approval limits cannot be set independently, the business cannot apply different oversight to the
  sourcing decision itself versus the financial commitment of the order.
DISCONFIRMING_OBSERVATION: >
  The system has no way to configure a different approval threshold for awarding a requisition than for
  approving the order it produces; the two always share one setting.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Attempt to configure a different approval threshold for requisition award than for order approval and check
  whether the system allows the two to differ.
```

## G07-PURCHASE_REQUISITION-Q048

```yaml
QID: G07-PURCHASE_REQUISITION-Q048
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user's authority to approve a requisition award does not, by itself, also grant them authority to approve
  the resulting order if the order's value exceeds what that user's order-approval authority would separately
  allow.
WHY_IT_MATTERS: >
  Allowing award authority to silently double as order-approval authority would let someone approve a financial
  commitment beyond what they are actually entrusted to approve.
DISCONFIRMING_OBSERVATION: >
  A user is able to approve an order whose value exceeds their own order-approval limit, solely because they
  were the one who approved the requisition's award.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Have a user with award-approval authority but a lower order-approval limit attempt to approve an order,
  generated from that award, whose value exceeds their order-approval limit.
```

## G07-PURCHASE_REQUISITION-Q049

```yaml
QID: G07-PURCHASE_REQUISITION-Q049
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two users concurrently attempting to award the same requisition to two different vendor responses cannot both
  succeed; a safeguard ensures only one award decision is finalized.
WHY_IT_MATTERS: >
  A race between two simultaneous award actions could otherwise leave a requisition with two conflicting award
  decisions, or silently let the second overwrite the first with no record of the conflict.
DISCONFIRMING_OBSERVATION: >
  Two users triggering an award decision on the same requisition to different vendor responses at nearly the
  same time both succeed, or the second silently overwrites the first with no conflict indicated.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Arrange for two users to attempt awarding the same requisition to different responses at nearly the same time
  and observe the outcome.
```

## G07-PURCHASE_REQUISITION-Q050

```yaml
QID: G07-PURCHASE_REQUISITION-Q050
MODULE: purchase_requisition
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A requisition, its vendor responses, and any blanket agreement it produces are scoped to the company (and,
  where applicable, branch) that raised the requisition, and are not visible or usable for ordering by an
  unrelated company sharing the same environment.
WHY_IT_MATTERS: >
  Cross-company visibility or use of a requisition and its agreements would let one legally separate business
  draw on a commitment another company negotiated for itself.
DISCONFIRMING_OBSERVATION: >
  A requisition, response, or blanket agreement created under one company is visible, selectable, or usable for
  ordering from a different company in the same environment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create a requisition and an agreement under one company, then check whether they are visible or usable when
  working under a different company.
```

---
## GMVQ Internal QA Checklist

- [x] 50 distinct MVQ records; no padding — every record targets a distinct hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`, and no two records share one failure event.
- [x] Demand-origin exclusion honored throughout: no question here depends on reading, replaying, or altering a
      customer order or a stock replenishment rule; those grounds are left entirely to `purchase_requisition_sale`
      and `purchase_requisition_stock` (see Control).
- [x] Pre-authoring sibling check performed against the only bank on disk at authoring time (`purchase`, P14,
      62 questions); no overlap found.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or the module's
      own metadata name appears in question text.
- [x] Lifecycle states and permitted actions represented (Q001-Q006).
- [x] Multiple vendor responses, award basis, and award authority represented (Q007-Q011).
- [x] Award to a non-best response and reason recorded represented (Q012-Q014).
- [x] Blanket agreement quantity versus quantity ordered, and exhaustion, represented (Q015-Q019).
- [x] Price agreed at award versus price on the resulting order represented (Q020-Q023).
- [x] Agreement validity period expiring with orders still placed represented (Q024-Q027).
- [x] Requisition changed after responses received represented (Q028-Q031).
- [x] Response visibility and competitive integrity boundary represented (Q032-Q034).
- [x] Requisition closed with demand unfulfilled represented (Q035-Q037).
- [x] Several orders against one requisition and the running balance represented (Q038-Q041).
- [x] Awarded vendor archived or merged represented (Q042-Q044).
- [x] Approval authority over the award distinct from approval of the resulting order represented (Q045-Q048).
- [x] Concurrency represented (Q049). Tenant/company boundary represented (Q050).
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
