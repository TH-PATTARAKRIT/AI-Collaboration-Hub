# SMEsPlus ENTERPRISE SUITE
## GMVQ — G07 PURCHASE / purchase_requisition_sale Module Adversarial MVQ Bank

**Document ID:** GMVQ-G07-PURCHASE_REQUISITION_SALE-MVQ48-V1.00
**Group:** G07 PURCHASE
**Module Metadata:** `purchase_requisition_sale`
**Wave:** W2
**Author Cell:** P18 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `purchase_requisition_sale` — a BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00, seam: an internal purchase requisition raised from a CUSTOMER
COMMITMENT. The requisition's own invariants (selection, award mechanics, agreement validity and
exhaustion, approval authority over the award in general) belong to the `purchase_requisition`
family base and are deliberately NOT re-asked here. This bank asks only what happens at the seam
where a real, waiting customer and a margin quoted before cost was known interact with a
requisition's own lifecycle: an award landing above the quoted price and who owns the difference;
the customer order changing, reducing, or cancelling while the tender or award is in flight;
apportionment when several customer orders feed one requisition; traceability from commitment
through to receipt and bill; the customer's committed date against vendor lead time; a
customer-specific requirement constraining vendor selection; margin visibility and its permission
boundary; and vendor cancellation charges attributable to a customer cancellation. Every question
was tested against the bridge rule: if it would read equally well with no customer commitment in
the picture, it was cut.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: purchase_requisition_sale`
appears only in the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses at the seam.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam between a
  customer commitment and the requisition it seeds. None restates a `purchase_requisition` award,
  selection, or agreement-validity invariant that holds with no customer commitment present, and
  none is a `sale` invariant restated with this module's name attached.
- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' <G07 siblings>/*.md | sort`
  was run against the existing `purchase` (base) and `purchase_edi_ubl_bis3` banks before authoring.
  No overlap found; those banks cover order/receipt/bill tolerance, currency, approval thresholds,
  duplicate detection, and vendor lifecycle — none of it origin-of-demand ground.

## G07-PURCHASE_REQUISITION_SALE-Q001

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q001
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the vendor award price causes the landed cost to exceed a price already quoted to the
  waiting customer, the difference is surfaced to whoever can act on it, not resolved by silently
  accepting a reduced or negative margin.
WHY_IT_MATTERS: >
  Undisclosed margin erosion at the moment of award removes the commercial decision from the
  people accountable for it, and repeats unnoticed at scale.
DISCONFIRMING_OBSERVATION: >
  An award is recorded above the price already quoted to the customer and the requisition or its
  onward document shows no indicator, flag, or required acknowledgement of the shortfall anywhere
  a reviewer would see it.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Quote a customer a price, raise the requisition, and carry a vendor response priced above that
  quote through to award.
```

## G07-PURCHASE_REQUISITION_SALE-Q002

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q002
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A cost variance between the customer-quoted price and the awarded vendor price is attributable
  to a specific, recorded party or decision, not left as an unassigned difference discovered later
  at billing.
WHY_IT_MATTERS: >
  An unattributed variance cannot be reviewed, challenged, or learned from, and tends to be
  written off silently.
DISCONFIRMING_OBSERVATION: >
  The variance between quote and award exists in the numbers but no record ties it to who accepted
  it or under what decision.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create the variance as above and search for a record of acceptance or attribution.
```

## G07-PURCHASE_REQUISITION_SALE-Q003

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q003
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Award authority sufficient to close an ordinary requisition does not, by itself, prove
  sufficient to accept an award that creates negative or reduced margin against an existing
  customer commitment — a distinct check may be required.
WHY_IT_MATTERS: >
  If the seam quietly reuses ordinary requisition award authority for a commercially different
  decision, exposure gets approved by someone with no visibility of the commercial consequence.
DISCONFIRMING_OBSERVATION: >
  A user whose authority was granted only to approve requisition awards within an ordinary spend
  limit is able to accept an award that pushes an already-quoted customer sale into loss, with no
  separate gate.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Set an approver with ordinary award authority only, then present an award that would erode a
  quoted customer margin.
```

## G07-PURCHASE_REQUISITION_SALE-Q004

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q004
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the vendor award price changes the landed cost after a customer price was already quoted,
  the system does not silently rewrite the customer-facing price or margin figure to make the
  books appear consistent.
WHY_IT_MATTERS: >
  A silent retroactive rewrite would hide the very event the seam exists to expose, defeating
  oversight.
DISCONFIRMING_OBSERVATION: >
  The customer-quoted price or margin value changes on its own after the award is recorded, with
  no user action and no visible reason.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record an award above the quoted price, then re-open the originating customer commitment to
  check whether its price or margin figure moved.
```

## G07-PURCHASE_REQUISITION_SALE-Q005

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q005
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If the customer order backing a requisition is reduced in quantity after the tender has already
  gone to vendors but before award, the requisition's outstanding demand reflects the reduction
  rather than continuing to solicit or award the original quantity.
WHY_IT_MATTERS: >
  Awarding and receiving against demand that no longer exists ties up cash and stock for nothing a
  customer will take.
DISCONFIRMING_OBSERVATION: >
  The requisition proceeds to award the full original quantity after the linked customer order has
  been reduced, with no adjustment and no exception raised.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reduce the quantity on the customer order after the tender has been sent but before any award is
  made, then continue the requisition to award.
```

## G07-PURCHASE_REQUISITION_SALE-Q006

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q006
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling the customer order that seeded a requisition, after the tender has gone out but
  before any vendor has responded, surfaces that change to whoever will select a vendor rather
  than letting selection proceed as though the demand still exists.
WHY_IT_MATTERS: >
  Selecting and committing to a vendor for demand that has already disappeared is an avoidable
  cost with a clear window to prevent it.
DISCONFIRMING_OBSERVATION: >
  A vendor response is accepted and awarded on a requisition whose originating customer order was
  already cancelled, with nothing in the award flow surfacing that fact.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Cancel the customer order after the tender is issued, then bring in a vendor response and
  proceed toward award.
```

## G07-PURCHASE_REQUISITION_SALE-Q007

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q007
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A change to a customer-specified requirement (such as a required brand or specification) after
  the tender has already been sent is handled as an explicit exception — reissuing or flagging the
  tender — rather than silently leaving vendors responding against a requirement the customer no
  longer has.
WHY_IT_MATTERS: >
  An award made against a stale requirement can produce goods the customer will refuse to accept.
DISCONFIRMING_OBSERVATION: >
  The customer's requirement changes after the tender is sent, and the requisition proceeds to
  award against the original, now-superseded requirement with no flag.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Change the customer-specific requirement on the originating commitment after the tender has
  already gone to vendors.
```

## G07-PURCHASE_REQUISITION_SALE-Q008

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q008
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether a vendor's response arrives before or after the customer order is cancelled produces a
  materially, and correctly, different outcome for the requisition — not the same outcome
  regardless of the order the two events happened in.
WHY_IT_MATTERS: >
  If the ordering of the two events makes no difference to the outcome, the seam is not actually
  looking at the customer side at all.
DISCONFIRMING_OBSERVATION: >
  The requisition behaves identically whether the vendor response arrived before or after the
  customer order was cancelled.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Run the scenario twice, once with vendor response before cancellation and once after, and
  compare the requisition's resulting state.
```

## G07-PURCHASE_REQUISITION_SALE-Q009

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q009
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the customer order is cancelled after award but before the purchase order is created, that
  cancellation blocks or holds automatic progression to a purchase order rather than letting the
  commitment be placed with the vendor unexamined.
WHY_IT_MATTERS: >
  Placing a vendor order for demand that is already known to be gone commits real money to
  nothing.
DISCONFIRMING_OBSERVATION: >
  A purchase order is created from an awarded requisition after the linked customer order was
  already cancelled, with no hold or warning at the point of creation.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Cancel the customer order in the window after award but before the purchase order step, then
  attempt to proceed.
```

## G07-PURCHASE_REQUISITION_SALE-Q010

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q010
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a customer order is cancelled after its requisition has already been awarded, there is a
  defined way to cancel or reduce the award itself, rather than the award standing as a commitment
  nothing can act on.
WHY_IT_MATTERS: >
  An award with no cancellation path becomes an orphaned commitment that someone eventually has to
  resolve by hand outside the system.
DISCONFIRMING_OBSERVATION: >
  After the customer order is cancelled post-award, no action in the requisition or award record
  allows reducing or cancelling that award — the only options assume the demand still stands.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Cancel the customer order after award, then attempt to reduce or cancel the award through
  ordinary means.
```

## G07-PURCHASE_REQUISITION_SALE-Q011

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q011
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a customer cancellation arrives after a vendor has already been notified of an award, any
  compensating communication or action toward the vendor is recorded against the requisition, not
  left to happen outside the system with no trace.
WHY_IT_MATTERS: >
  An untracked compensating action leaves no evidence of what was actually told to the vendor,
  which the business will need if a dispute follows.
DISCONFIRMING_OBSERVATION: >
  A vendor is known to have been told about a cancellation, but the requisition record shows no
  trace that any compensating action occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a post-award customer cancellation and perform whatever compensating vendor action the
  process calls for, then inspect the requisition record.
```

## G07-PURCHASE_REQUISITION_SALE-Q012

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q012
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When several customer orders feed one requisition and the awarded or received quantity is less
  than the combined demand, there is a defined, visible basis for apportioning what was received
  among the contributing orders, rather than an arbitrary or undocumented split.
WHY_IT_MATTERS: >
  An undocumented split leaves some customers silently under-served with no traceable reason why.
DISCONFIRMING_OBSERVATION: >
  A shortfall against combined demand is divided among the contributing customer orders with no
  recorded rule, and two runs of the same shortfall scenario divide it differently.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Feed two or more customer orders into one requisition, award or receive less than the total, and
  inspect how the shortfall is divided.
```

## G07-PURCHASE_REQUISITION_SALE-Q013

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q013
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A partial receipt against a requisition serving multiple customer orders allocates to those
  orders by a deterministic, repeatable rule rather than by whichever order happens to be
  processed first at that moment.
WHY_IT_MATTERS: >
  A non-deterministic allocation makes the outcome depend on incidental timing rather than
  business priority, and cannot be explained after the fact.
DISCONFIRMING_OBSERVATION: >
  Repeating the same partial-receipt scenario with the same contributing orders produces a
  different allocation between them on separate occasions with nothing having changed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Set up multiple customer orders on one requisition, trigger a partial receipt, and repeat the
  scenario under matched conditions.
```

## G07-PURCHASE_REQUISITION_SALE-Q014

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q014
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If one of several customer orders contributing to a shared requisition is cancelled before
  award, the requisition's total requested quantity reduces accordingly rather than continuing to
  solicit and award the cancelled portion on behalf of no one.
WHY_IT_MATTERS: >
  Awarding quantity for a cancelled contributor leaves stock that arrives with no order behind it.
DISCONFIRMING_OBSERVATION: >
  One contributing customer order is cancelled before award, and the requisition still proceeds to
  award the full combined quantity including the cancelled portion.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Cancel one of several contributing customer orders before the requisition is awarded, then check
  the awarded quantity.
```

## G07-PURCHASE_REQUISITION_SALE-Q015

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q015
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cost variance between quote and award on a requisition serving several customer orders is
  distributed across those orders by a defined basis, rather than charged in full to whichever
  order is processed or invoiced first.
WHY_IT_MATTERS: >
  Charging the whole variance to one customer's order because of processing order, rather than a
  fair basis, misstates that order's margin for no business reason.
DISCONFIRMING_OBSERVATION: >
  The full cost variance from one shared award lands against a single contributing customer order
  rather than being distributed, with no rule explaining why that order was chosen.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a variance on a requisition serving multiple customer orders and inspect where the
  variance is recorded.
```

## G07-PURCHASE_REQUISITION_SALE-Q016

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q016
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A specific customer commitment can be traced forward through the requisition it generated, the
  award, the resulting purchase order, and the eventual receipt as one unbroken chain.
WHY_IT_MATTERS: >
  A break anywhere in that chain removes the ability to tell a customer, mid-fulfillment, exactly
  where their order stands.
DISCONFIRMING_OBSERVATION: >
  Starting from the customer commitment, the chain of links to the requisition, award, purchase
  order, or receipt is missing at some point, even though the underlying documents exist.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Carry one customer commitment through requisition, award, purchase order, and receipt, then
  attempt to trace the full chain from the original commitment.
```

## G07-PURCHASE_REQUISITION_SALE-Q017

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q017
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If the originating customer commitment is later archived or otherwise made inactive after
  fulfillment, the trace linking it to the requisition and receipt still resolves rather than
  leaving the receipt looking unexplained.
WHY_IT_MATTERS: >
  Routine archiving of old customer records should not erase the evidence of why stock was
  procured.
DISCONFIRMING_OBSERVATION: >
  After the originating customer order is archived, the link from the requisition or receipt back
  to it can no longer be resolved.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete the fulfillment chain, archive the originating customer order, then attempt to trace
  back from the requisition or receipt.
```

## G07-PURCHASE_REQUISITION_SALE-Q018

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q018
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the requisition is closed while the linked customer order remains open, for example awaiting
  a further partial delivery, the link between them is still usable for status reporting rather
  than disappearing once the requisition side is done.
WHY_IT_MATTERS: >
  A customer service function checking on an open order needs the link even after procurement
  considers its own side finished.
DISCONFIRMING_OBSERVATION: >
  The requisition closes while the customer order remains open, and the customer order's view no
  longer shows any connection to the requisition it came from.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Close the requisition while its originating customer order is still open, then check the
  customer order's own view for the link.
```

## G07-PURCHASE_REQUISITION_SALE-Q019

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q019
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the tender's closing timeline is set from a customer-committed date, a vendor lead time
  that makes that date unreachable is surfaced as a controllable exception rather than the
  requisition silently proceeding as if the date were still achievable.
WHY_IT_MATTERS: >
  Discovering the date is unreachable only after award leaves no time to renegotiate with the
  customer.
DISCONFIRMING_OBSERVATION: >
  A vendor's stated lead time already makes the customer's committed date unreachable at the time
  of response, and the requisition proceeds to award with no exception raised.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Obtain a vendor response whose lead time cannot meet the customer's committed date, then proceed
  through award.
```

## G07-PURCHASE_REQUISITION_SALE-Q020

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q020
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a vendor's lead time cannot meet the customer's committed date, resolving that conflict
  requires a decision by a person with visibility of the customer relationship, rather than the
  system silently substituting a new date on the customer's behalf.
WHY_IT_MATTERS: >
  A silently changed promise to the customer removes their chance to react before it becomes their
  problem.
DISCONFIRMING_OBSERVATION: >
  The customer-facing committed date changes without any recorded decision, following a vendor
  lead time that could not meet the original date.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Create the same lead-time conflict as above and observe whether the customer date changes on its
  own.
```

## G07-PURCHASE_REQUISITION_SALE-Q021

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q021
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the customer's committed date changes after the tender has already closed, whatever weight
  was given to delivery speed in comparing vendor responses is re-evaluated against the new date
  rather than staying keyed to the date that no longer applies.
WHY_IT_MATTERS: >
  Selecting a vendor on outdated timing criteria can favor the wrong response once the real
  deadline has moved.
DISCONFIRMING_OBSERVATION: >
  The customer's committed date changes after tender close, and the vendor comparison or the
  eventual award shows no sign the change was taken into account.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Change the customer's committed date after the tender has closed but before award, then inspect
  the comparison basis.
```

## G07-PURCHASE_REQUISITION_SALE-Q022

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q022
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A customer-specific requirement carried from the originating commitment, such as a required
  brand, constrains which vendor responses are eligible for award, and an award that does not meet
  it is identifiable as an exception rather than passing as an ordinary award.
WHY_IT_MATTERS: >
  Delivering against a customer-specific requirement that was silently dropped produces goods the
  customer can legitimately reject.
DISCONFIRMING_OBSERVATION: >
  An award is made and finalized against a vendor response that does not meet the customer-
  specific requirement carried from the originating commitment, with no exception recorded
  anywhere.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Attach a customer-specific requirement to the originating commitment, then attempt to award a
  vendor response that does not meet it.
```

## G07-PURCHASE_REQUISITION_SALE-Q023

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q023
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Overriding a customer-specific constraint to accept a non-conforming vendor response requires an
  approval distinct from ordinary requisition award authority, given that the exposure is
  commercial and customer-facing rather than purely procurement.
WHY_IT_MATTERS: >
  If ordinary award authority alone can override a customer-specific requirement, the person best
  placed to judge the customer risk never sees the decision.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary requisition award authority is able to override a customer-specific
  requirement and finalize the award, with no separate approval step invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt to override a customer-specific requirement using an account with ordinary award
  authority only.
```

## G07-PURCHASE_REQUISITION_SALE-Q024

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q024
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a customer-specific requirement is removed or changed while vendor responses are already in
  flight, the requisition applies the change consistently to all responses rather than enforcing
  the old requirement against some and the new one against others depending on when each response
  happened to arrive.
WHY_IT_MATTERS: >
  An inconsistently applied requirement produces an award decision that cannot be defended as
  having used one consistent rule.
DISCONFIRMING_OBSERVATION: >
  After the customer-specific requirement changes mid-tender, some already-received vendor
  responses are evaluated against the old requirement and others against the new one, within the
  same tender.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Change the customer-specific requirement after some vendor responses are already in, and before
  the tender closes.
```

## G07-PURCHASE_REQUISITION_SALE-Q025

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q025
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the margin between the customer-quoted price and the vendor award cost is visible to the
  person awarding the requisition is governed by their role, not shown or hidden the same way to
  everyone regardless of what they are otherwise permitted to see.
WHY_IT_MATTERS: >
  Uniform exposure of commercial margin to every awarder regardless of role either leaks pricing
  information too broadly or denies visibility to someone who needs it to decide responsibly.
DISCONFIRMING_OBSERVATION: >
  Two users with materially different roles and permission scopes are shown identical margin
  information at the point of award, or an authorized commercial role is denied the figure a
  lower-permission role can see.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Compare what margin information is visible to two accounts with different role-based permissions
  at the point of award.
```

## G07-PURCHASE_REQUISITION_SALE-Q026

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q026
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The ability to see the margin figure at award is a separately controllable permission from the
  ability to approve the award itself, so an organization can grant one without the other.
WHY_IT_MATTERS: >
  Tying margin visibility to award permission removes an organization's ability to let junior
  staff process awards without exposing commercial pricing to them.
DISCONFIRMING_OBSERVATION: >
  There is no way to grant award permission without also granting visibility of the margin figure,
  or vice versa — the two are bundled with no independent control.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Attempt to configure award permission and margin visibility independently of one another for a
  role.
```

## G07-PURCHASE_REQUISITION_SALE-Q027

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q027
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  In a multi-company setup, a margin figure derived by combining a customer-side price recorded in
  one company with a vendor-side cost recorded in another does not become visible to a user who
  has access to only one of those two companies.
WHY_IT_MATTERS: >
  A derived figure is an easy way for information to cross a company boundary that direct access
  controls were built to enforce.
DISCONFIRMING_OBSERVATION: >
  A user with access limited to one company can see the combined margin figure that depends on
  data belonging to a different company they do not have access to.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Set up the customer side and vendor side of one requisition in two different companies, then
  check what a single-company user can see.
```

## G07-PURCHASE_REQUISITION_SALE-Q028

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q028
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a customer order is cancelled after award and the vendor imposes a cancellation charge as a
  result, that charge is captured as attributable to the specific customer cancellation that
  caused it, rather than recorded as an unattached cost with no traceable origin.
WHY_IT_MATTERS: >
  An unattributed cancellation charge cannot be recovered from or reported against the decision
  that caused it.
DISCONFIRMING_OBSERVATION: >
  A vendor cancellation charge exists in the records with no link back to the customer order
  cancellation that triggered the vendor cancellation.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel a customer order after award such that a vendor cancellation charge results, then check
  whether that charge is linked to the cancellation.
```

## G07-PURCHASE_REQUISITION_SALE-Q029

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q029
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  There is a defined way to record a vendor cancellation charge against the requisition it arose
  from, rather than the charge only being recordable through an unrelated, generic entry with no
  connection to the requisition.
WHY_IT_MATTERS: >
  Without a defined path, whether the charge gets recorded at all depends on someone remembering
  to do it manually and correctly.
DISCONFIRMING_OBSERVATION: >
  The only way to record a vendor cancellation charge is a general entry with no field or
  mechanism connecting it back to the originating requisition.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to record a vendor cancellation charge arising from a cancelled requisition-originated
  award.
```

## G07-PURCHASE_REQUISITION_SALE-Q030

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q030
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the vendor has already partially fulfilled an award by the time a customer cancellation is
  processed, the requisition distinguishes the already-fulfilled portion from the portion that can
  still be stopped, rather than treating the whole award as either fully stoppable or fully
  committed.
WHY_IT_MATTERS: >
  Treating a partially fulfilled award as fully stoppable risks refusing goods already shipped;
  treating it as fully committed risks accepting goods for a customer who no longer wants them.
DISCONFIRMING_OBSERVATION: >
  A customer cancellation is processed against an award that has already been partially fulfilled,
  and the requisition gives no indication of which portion is still stoppable and which is not.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Partially fulfill a vendor award, then process a customer cancellation against the same
  requisition.
```

## G07-PURCHASE_REQUISITION_SALE-Q031

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q031
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A requisition raised or awarded before the customer order backing it is actually confirmed is
  distinguishable, in the record, from one raised against a firm commitment, so the difference in
  risk is not hidden.
WHY_IT_MATTERS: >
  Treating speculative and firm-commitment procurement identically hides which purchases are
  exposed if the customer never confirms.
DISCONFIRMING_OBSERVATION: >
  A requisition seeded from an unconfirmed customer order looks, in every visible respect,
  identical to one seeded from a confirmed order.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Seed one requisition from an unconfirmed customer order and another from a confirmed one, then
  compare their records.
```

## G07-PURCHASE_REQUISITION_SALE-Q032

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q032
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When only part of the customer order backing a requisition is firm and the rest is still
  tentative, the requisition's progress to vendor selection and award reflects that split rather
  than treating the tentative portion as equally committed.
WHY_IT_MATTERS: >
  Awarding against a tentative portion as if it were firm risks procuring for a sale that may
  never happen.
DISCONFIRMING_OBSERVATION: >
  A requisition proceeds to award the full quantity including a portion of the customer order that
  was still tentative, with nothing distinguishing that portion from the firm part.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a customer order with part firm and part tentative, feed it into a requisition, and
  proceed to award.
```

## G07-PURCHASE_REQUISITION_SALE-Q033

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q033
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If the requested quantity is edited independently on the customer order and on the requisition
  line it seeded, after the seam event, there is a defined rule for which one governs, rather than
  the two being left to silently disagree.
WHY_IT_MATTERS: >
  A silent disagreement between the customer's real demand and what procurement is chasing means
  one of the two numbers is simply wrong, undetected.
DISCONFIRMING_OBSERVATION: >
  The customer order quantity and the requisition line quantity are edited independently after the
  link is made, and the requisition proceeds without reconciling or flagging the mismatch.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Edit the quantity on the customer order and, separately, on the linked requisition line, then
  observe what the requisition does with the mismatch.
```

## G07-PURCHASE_REQUISITION_SALE-Q034

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q034
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the vendor response or award is rejected or fails after a delivery commitment has already
  been shared with the customer, that customer-facing commitment is flagged for revision rather
  than left standing as if nothing changed.
WHY_IT_MATTERS: >
  A customer holding a promise that procurement already knows cannot be kept, with nobody told to
  revise it, becomes an avoidable service failure.
DISCONFIRMING_OBSERVATION: >
  The vendor award fails after a delivery date was already communicated to the customer, and
  nothing in the requisition or the customer order flags that the commitment now needs revision.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Share a delivery commitment with the customer, then cause the vendor award backing it to fail.
```

## G07-PURCHASE_REQUISITION_SALE-Q035

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q035
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the customer commitment is priced in one currency and the vendor award in another, any
  margin or absorption figure calculated across the two is computed at a consistent, recorded rate
  rather than compared as raw numbers in different currencies.
WHY_IT_MATTERS: >
  Comparing unconverted figures across currencies produces a margin number that means nothing and
  can mislead whoever relies on it.
DISCONFIRMING_OBSERVATION: >
  A margin or variance figure is shown or used for a decision that combines a customer-side amount
  and a vendor-side amount in different currencies with no conversion applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set the customer commitment and the vendor award in two different currencies, then inspect any
  combined margin figure.
```

## G07-PURCHASE_REQUISITION_SALE-Q036

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q036
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If the customer order backing a requisition is fully invoiced and closed while the purchase
  order side remains open, for example due to a late vendor delivery, the link between them
  remains available for later reconciliation rather than being lost once the customer side closes.
WHY_IT_MATTERS: >
  Reconciling a late delivery against an already-closed sale requires the link to still exist at
  the time the late goods finally arrive.
DISCONFIRMING_OBSERVATION: >
  The customer order closes and invoices before the purchase order is fulfilled, and once closed,
  the link back to the still-open purchase order can no longer be found.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close and invoice the customer order while the linked purchase order remains open, then attempt
  to trace the link.
```

## G07-PURCHASE_REQUISITION_SALE-Q037

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q037
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When two customer orders arrive close together and both would attach to the same in-flight
  requisition or tender, the system resolves the conflict by a defined rule rather than by
  whichever request happens to be processed first with no recorded reason.
WHY_IT_MATTERS: >
  An unresolved race condition on which order attaches, or how both are combined, can silently
  drop or misassign one customer's demand.
DISCONFIRMING_OBSERVATION: >
  Two customer orders submitted at effectively the same time produce an inconsistent or
  unexplained outcome for which one attaches to the in-flight requisition and which does not.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Submit two customer orders in close succession that would both attach to the same in-flight
  requisition.
```

## G07-PURCHASE_REQUISITION_SALE-Q038

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q038
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A requisition seeded from a customer commitment carries a recorded, observable fact of that
  origin, distinct from one seeded any other way, rather than the origin being something that can
  only be inferred by a person reasoning about the surrounding documents.
WHY_IT_MATTERS: >
  If origin is not a recorded fact, no report or control that depends on knowing where demand came
  from can be built reliably.
DISCONFIRMING_OBSERVATION: >
  There is no field, tag, or record on the requisition that identifies it as customer-originated,
  and the only way to tell is to manually trace surrounding documents.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a customer-originated requisition and look for a direct, recorded indicator of that
  origin on the requisition itself.
```

## G07-PURCHASE_REQUISITION_SALE-Q039

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q039
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a customer commitment is allowed to generate a requisition at all is governed by a
  configuration setting, and when that path is disabled, the resulting demand is handled through a
  defined alternative rather than silently disappearing.
WHY_IT_MATTERS: >
  A disabled path that simply drops the demand, with no alternative and no warning, loses a
  customer's order without anyone noticing.
DISCONFIRMING_OBSERVATION: >
  With customer-originated requisitions disabled, a customer commitment that would have needed one
  produces no requisition and no alternative indication that procurement is needed.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Disable the configuration allowing customer-originated requisitions, then create a customer
  commitment that would otherwise trigger one.
```

## G07-PURCHASE_REQUISITION_SALE-Q040

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q040
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The link between a requisition and the customer commitment that generated it cannot be cleared
  or detached through an ordinary edit of the requisition, since the origin is meant to be a
  durable fact rather than an editable field.
WHY_IT_MATTERS: >
  If the link can be casually cleared, every other seam control that depends on knowing the origin
  becomes unreliable.
DISCONFIRMING_OBSERVATION: >
  An ordinary edit to the requisition removes or overwrites the link to its originating customer
  commitment with no special permission or warning required.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to clear or change the customer-origin link on a requisition through ordinary edit
  actions.
```

## G07-PURCHASE_REQUISITION_SALE-Q041

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q041
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A customer order that does not itself require special procurement is not mistakenly tagged as
  the origin of a requisition it happens to be near in time or in the same session, merely by
  coincidence.
WHY_IT_MATTERS: >
  A false origin link misattributes procurement activity to a customer who has nothing to do with
  it, corrupting the traceability the seam is meant to provide.
DISCONFIRMING_OBSERVATION: >
  An unrelated requisition, raised for an unconnected reason, shows a link to a customer order
  that never actually generated it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an unrelated requisition in close time proximity to an unrelated customer order and check
  that no spurious link forms between them.
```

## G07-PURCHASE_REQUISITION_SALE-Q042

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q042
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a requisition that was seeded from a customer commitment produces a visible signal on
  that customer order that its supply is no longer being pursued, rather than the customer order
  being left to look normally in progress.
WHY_IT_MATTERS: >
  Whoever manages the customer relationship needs to know procurement was cancelled before the
  customer asks where their order is.
DISCONFIRMING_OBSERVATION: >
  The requisition is cancelled, and the originating customer order shows no change and no
  indication that the procurement backing it no longer exists.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Cancel a customer-originated requisition and then check the state and any indicators on the
  originating customer order.
```

## G07-PURCHASE_REQUISITION_SALE-Q043

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q043
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Accepting an award that would cost more than the price already quoted to the customer requires
  an authority distinct from the authority needed to close an ordinary requisition award, because
  the exposure being accepted is commercial rather than purely procurement-related.
WHY_IT_MATTERS: >
  If the two authorities are the same, ordinary procurement staff can unknowingly accept
  commercial losses that should require a commercial decision.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary requisition award authority can finalize an award that costs more than
  the customer-quoted price with no additional approval invoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt to finalize a margin-eroding award using an account that holds only ordinary requisition
  award authority.
```

## G07-PURCHASE_REQUISITION_SALE-Q044

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q044
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a customer order in one company feeds a requisition raised in a different company under a
  shared procurement arrangement, the link to the originating customer commitment is preserved
  across that boundary rather than being dropped once the requisition crosses into the other
  company.
WHY_IT_MATTERS: >
  Losing the link at a company boundary defeats traceability precisely where a cross-company
  arrangement makes it hardest to reconstruct by hand.
DISCONFIRMING_OBSERVATION: >
  A requisition raised in a different company than its originating customer order shows no trace
  of that customer order once viewed from the requisition's own company.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Set up a customer order in one company that feeds a requisition raised in a different company,
  then check the link from the requisition side.
```

## G07-PURCHASE_REQUISITION_SALE-Q045

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q045
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a vendor cannot fulfil an award that was backing a firm customer commitment, the available
  path to re-tender or re-source is at least as fast as the ordinary path, and any difference in
  handling compared to non-customer-originated demand is a deliberate, recorded design choice
  rather than an accidental gap.
WHY_IT_MATTERS: >
  Firm customer demand left to work through the same unprioritized re-tender process as any other
  shortfall risks missing a commitment that was already promised.
DISCONFIRMING_OBSERVATION: >
  A vendor failure on customer-originated demand is re-tendered through exactly the same process,
  with exactly the same timeline, as demand with no waiting customer, and no design record
  explains that as intentional.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Fail a vendor award backing a firm customer commitment and observe the re-tender path taken,
  compared with an equivalent non-customer-originated shortfall.
```

## G07-PURCHASE_REQUISITION_SALE-Q046

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q046
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a customer order is cancelled after receipt against a requisition that served several
  customer orders, reversing that customer's apportioned share does not disturb the shares already
  allocated to the other, still-active customer orders.
WHY_IT_MATTERS: >
  A clumsy reversal that touches unrelated customers' shares turns one cancellation into a
  multi-customer problem.
DISCONFIRMING_OBSERVATION: >
  Cancelling one customer order after receipt changes the quantity or allocation recorded against
  a different, unrelated customer order sharing the same requisition.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Receive against a requisition serving multiple customer orders, then cancel one of them and
  check the others' allocations.
```

## G07-PURCHASE_REQUISITION_SALE-Q047

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q047
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The specific customer commitment that originated a requisition remains traceable through to the
  cost attribution on the eventual vendor bill, not just up to the purchase order with the trail
  ending there.
WHY_IT_MATTERS: >
  Without that final link, the actual cost of serving a specific customer commitment can never be
  reconstructed after the fact.
DISCONFIRMING_OBSERVATION: >
  The trail from customer commitment to purchase order is intact, but the eventual vendor bill's
  cost cannot be traced back to that same originating commitment.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Carry a customer-originated requisition through to a vendor bill and attempt to trace the bill's
  cost back to the originating customer commitment.
```

## G07-PURCHASE_REQUISITION_SALE-Q048

```yaml
QID: G07-PURCHASE_REQUISITION_SALE-Q048
MODULE: purchase_requisition_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the approval threshold or workflow for a requisition differs depending on whether its
  origin is a customer commitment is a deliberate, observable, and consistent answer, not an
  accidental gap where origin happens to change the outcome for reasons nobody decided.
WHY_IT_MATTERS: >
  An accidental difference in approval rigor based on origin either weakens control over
  customer-driven spend or slows it down for no chosen reason.
DISCONFIRMING_OBSERVATION: >
  Two requisitions of identical value and risk, one customer-originated and one not, go through
  different approval thresholds or steps with no configuration or design record explaining the
  difference.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Compare the approval path taken by two otherwise-matched requisitions that differ only in
  whether they are customer-originated.
```
