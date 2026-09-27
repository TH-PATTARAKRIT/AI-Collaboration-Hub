# SMEsPlus ENTERPRISE SUITE
## GMVQ — G11 EVENTS / event_crm_sale Bridge-of-a-Bridge MVQ Bank

**Document ID:** GMVQ-G11-EVENT_CRM_SALE-MVQ48-V1.00
**Group:** G11 EVENTS
**Module Metadata:** `event_crm_sale`
**Wave:** W2
**Author Cell:** P-E2 (GMVQ Question Factory — Internal Production Team E2, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here; not yet authored for G11 as of this run)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `event_crm_sale`, a bridge over a bridge: an
opportunity arising from a registration that itself came from an order. Per the GMVQ Bridge Module
Rule V1.00, a question belongs here only if removing this capability and using the order-to-
registration bridge and the registration-to-opportunity bridge entirely apart from each other would
make the question stop making sense — that is, every question requires all three objects (the
order, the registration, and the opportunity) to be present at once. Ground covered: the chain's
provenance surviving both hops so a reviewer can tell a paid-origin lead from a free one; timing
disagreements between when the opportunity is created and when the order is paid or cancelled;
which party's identity an opportunity attaches to when the payer, the attendee and a possible third
party differ; one order producing several attendees and whether that produces one opportunity or
several; the opportunity's value tracking what was actually paid, including partial payment,
downgrades, discounts, negotiated rates, tax basis and multi-line orders; reversal or state
divergence between the order and its own registration after the opportunity has already progressed;
transfers, swaps, and cross-order attribution reaching the opportunity correctly; ownership and
company assignment when the order's salesperson, the event's owner, and their companies disagree;
asynchronous, delayed order settlement; and the three-part audit trail surviving archival.

Before writing a single question here, this cell read the sibling `event_sale` bank's authored
HYPOTHESIS lines on disk (the only sibling bank in this group at the moment `event_sale` itself was
frozen). During this same run, five other cells concurrently authored the base `event` bank and the
`event_product`, `event_booth`, `event_booth_sale`, `event_crm` and `event_sms` bridge banks into
this same group directory; those appeared on disk before this bank was frozen. A second pass was
therefore run specifically against `event_crm`'s authored HYPOTHESIS lines, since `event_crm_sale`
is in the same bridge family and item 4 of the Bridge Module Rule names exactly that risk (two
bridge banks in one family differing only by the named third capability). That pass found four
questions that were in fact answerable via `event_crm` alone with the order merely decorative
(duplicate-person registrations, zero-value registrations, and background-pass retry idempotency
are `event_crm`'s own ground, already covered there) and one question worded too close to
`event_crm`'s own cancellation-after-pipeline-advancement question; all five were replaced, not
dropped, with questions that require the order specifically — a promotional discount revocation, a
tax-basis consistency check, an order/registration state divergence, cross-order sales credit for
one attendee named on two orders, and a delayed asynchronous settlement — so the bank was held at
48 material questions rather than shortened. This second pass was scoped to the two directly
bridged siblings (`event` and `event_crm`); a full line-by-line comparison against all six sibling
banks now on disk was not performed in this authoring pass and remains Review Cell / independent
RED TEAM audit work, not self-certified here. Coverage spans business capability, business rule,
state transition, configuration dependency, role and permission, exception path, cancellation,
reversal, negative case, cross-module dependency, optional behaviour, auditability, tenant/company
boundary, concurrency and ordering, runtime reachability, configuration reachability, and
source/runtime contradiction potential.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material three-object seam
  hypotheses; none was trimmed or stretched to hit the floor.
- Every question requires the order, the registration, and the opportunity to all be present; a
  question answerable with only two of the three was cut per the bridge-over-bridge removal test
  and, where material, folded into a note that it belongs to `event_sale` or `event_crm` instead.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field.
- Cross-checked at authoring time against the sibling `event_sale` bank's authored HYPOTHESIS lines
  on disk; no overlap was found, and none is expected structurally because this bank's ground is
  the third-object seam that `event_sale` cannot address on its own.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G11-EVENT_CRM_SALE-Q001

```yaml
QID: G11-EVENT_CRM_SALE-Q001
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An opportunity's link back to the registration that produced it, and onward to the order that produced that registration, remains intact through both hops, so that whether the originating registration was paid for or was free can still be determined from the opportunity alone.
WHY_IT_MATTERS: >
  Without an intact two-hop link, a reviewer cannot tell a warm lead that came from someone who already paid to attend apart from one that came from a free sign-up, undermining any qualification based on that distinction.
DISCONFIRMING_OBSERVATION: >
  An opportunity produced by the chain can be traced back only as far as its immediate registration, with no way to determine from the opportunity whether that registration came from a paid order or a free sign-up.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an opportunity from a registration that itself came from a paid order, then check whether the opportunity record alone reveals that the registration was order-derived and paid.
```

## G11-EVENT_CRM_SALE-Q002

```yaml
QID: G11-EVENT_CRM_SALE-Q002
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An opportunity created from a registration before the underlying order has actually been paid is distinguishable, in its own state or value, from one created after the order was fully paid, rather than the two being indistinguishable once created.
WHY_IT_MATTERS: >
  Treating a lead backed only by an unpaid order identically to one backed by a completed sale overstates how qualified the earlier lead actually is.
DISCONFIRMING_OBSERVATION: >
  An opportunity created while the underlying order is still unpaid is indistinguishable in state or value from one created after the same kind of order was fully paid.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create one opportunity from a registration whose order is still unpaid and another from a registration whose order is fully paid, and compare the two opportunities' state and value.
```

## G11-EVENT_CRM_SALE-Q003

```yaml
QID: G11-EVENT_CRM_SALE-Q003
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the order behind a registration is already cancelled by the time the opportunity-generation step would normally run, no opportunity is created from that cancelled chain, rather than one being created anyway and left for someone to notice and clean up later.
WHY_IT_MATTERS: >
  Generating leads from transactions that never actually happened wastes sales effort chasing an opportunity that was never real to begin with.
DISCONFIRMING_OBSERVATION: >
  An opportunity is created from a registration whose underlying order was already cancelled before the opportunity was generated, with no distinction from an opportunity generated from a live order.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Cancel an order before its registration would normally trigger opportunity generation, then check whether an opportunity is still created from it.
```

## G11-EVENT_CRM_SALE-Q004

```yaml
QID: G11-EVENT_CRM_SALE-Q004
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the order's paying customer and the individually named attendee are different people, which one of the two the resulting opportunity is linked to as its contact is decided consistently, rather than sometimes attaching to the payer and sometimes to the attendee for comparable cases.
WHY_IT_MATTERS: >
  An opportunity attached to the wrong party sends a sales follow-up to whichever person happens to have been picked, rather than to whoever is actually the qualified lead.
DISCONFIRMING_OBSERVATION: >
  Two comparable chains, each with a paying customer different from the named attendee, produce opportunities attached to different parties (one to the payer, one to the attendee) with no distinguishing factor between the two cases.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create two comparable chains where the paying customer and the named attendee differ, and compare which party each resulting opportunity is linked to as its contact.
```

## G11-EVENT_CRM_SALE-Q005

```yaml
QID: G11-EVENT_CRM_SALE-Q005
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When one order registers several separate named attendees for the same event, the chain generates one opportunity per attendee rather than either collapsing several real, distinct people into a single shared opportunity or generating no opportunity at all for the additional attendees.
WHY_IT_MATTERS: >
  Collapsing several real leads into one opportunity, or dropping the additional attendees entirely, understates the actual number of qualified people the sales team should be following up with.
DISCONFIRMING_OBSERVATION: >
  An order registering three separately named attendees for the same event results in a number of resulting opportunities that does not match the number of named attendees.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place one order registering several separately named attendees for the same event, and count the resulting opportunities against the number of attendees named.
```

## G11-EVENT_CRM_SALE-Q006

```yaml
QID: G11-EVENT_CRM_SALE-Q006
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When two different attendees registered under the same order each produce their own opportunity, the two opportunities carry a visible link to each other or to their shared originating order, rather than appearing to a salesperson as two entirely unrelated leads with no indication they came from the same transaction.
WHY_IT_MATTERS: >
  A salesperson unaware that two leads share the same originating order may unknowingly duplicate outreach or miss a chance to handle the two relationships together.
DISCONFIRMING_OBSERVATION: >
  Two opportunities known to have come from the same originating order show no link, reference, or indication to each other or to the shared order when viewed independently.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Place one order registering two separate named attendees, let each produce its own opportunity, and check whether the two opportunities show any link to each other or to the shared order.
```

## G11-EVENT_CRM_SALE-Q007

```yaml
QID: G11-EVENT_CRM_SALE-Q007
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The monetary value carried on an opportunity generated by the chain reflects the amount actually paid on the originating order at the time the opportunity was created, rather than a figure entered independently that can silently diverge from what was actually paid.
WHY_IT_MATTERS: >
  An opportunity value untethered from the real payment misleads pipeline and forecast figures with a number that was never actually collected.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated from a registration shows an expected value that does not match the amount actually paid on the originating order at the time of creation, with no explanation for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an opportunity from a registration tied to an order with a known paid amount, and compare the opportunity's recorded value against that amount.
```

## G11-EVENT_CRM_SALE-Q008

```yaml
QID: G11-EVENT_CRM_SALE-Q008
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order is refunded or cancelled but, because of an unresolved divergence between the two, its own registration remains showing as still active rather than also cancelled, an opportunity that had already advanced to a later pipeline stage bases its own continued status on the registration's still-active state, rather than silently adopting the order's cancelled state as though the registration had been cancelled too.
WHY_IT_MATTERS: >
  If the opportunity quietly adopts the order's cancelled state despite the registration itself still standing active, real, unresolved event capacity keeps being reported as free even though no coordinated cancellation of the actual seat has taken place.
DISCONFIRMING_OBSERVATION: >
  An order is refunded or cancelled while its registration remains, unresolved, in an active state, and the opportunity that had already advanced to a later pipeline stage is nonetheless marked lost or reversed as though the registration itself had been cancelled too.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Cancel or refund an order while leaving its registration in an active, uncancelled state (an unresolved divergence), with the resulting opportunity already advanced to a later pipeline stage, and check which of the two conflicting states the opportunity's own status actually follows.
```

## G11-EVENT_CRM_SALE-Q009

```yaml
QID: G11-EVENT_CRM_SALE-Q009
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a registration is transferred to a different named person after an opportunity was already created for the original attendee, the opportunity's own contact either follows the transfer to the new attendee or is explicitly retained with the original one under a documented rule, rather than silently continuing to reference a person who no longer holds the seat with no rule governing which should happen.
WHY_IT_MATTERS: >
  An opportunity left attached to someone who no longer holds the seat directs sales effort at the wrong person while the actual current attendee goes unrecognised as a lead.
DISCONFIRMING_OBSERVATION: >
  Transferring a registration to a new named person leaves its associated opportunity referencing the original attendee with no update, note, or documented rule explaining why the contact was not changed.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create an opportunity from a registration, transfer that registration to a different named person, and check what happens to the opportunity's own contact reference.
```

## G11-EVENT_CRM_SALE-Q010

```yaml
QID: G11-EVENT_CRM_SALE-Q010
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the salesperson credited on the originating order and the person designated as the event's own owner are different people, ownership of the resulting opportunity is assigned by a defined, documented rule, rather than defaulting unpredictably to whichever of the two happens to be checked first.
WHY_IT_MATTERS: >
  Undocumented, inconsistent ownership assignment on a chain-generated opportunity leaves no clear person accountable for following it up, and can create disputes over whose pipeline credit it belongs to.
DISCONFIRMING_OBSERVATION: >
  Two comparable chains, each with a different salesperson on the order than the event's own owner, result in opportunities assigned to different sides of that pair with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create two comparable chains where the order's salesperson and the event's own owner differ, and compare who the resulting opportunities are actually assigned to.
```

## G11-EVENT_CRM_SALE-Q011

```yaml
QID: G11-EVENT_CRM_SALE-Q011
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the order's own company and the event's own company are different entities in a multi-company setup, the resulting opportunity is filed under one defined, consistent company rather than the assignment varying unpredictably between comparable chains.
WHY_IT_MATTERS: >
  An opportunity randomly filed under whichever company happens to be picked breaks that company's own pipeline reporting boundary and can expose one company's leads to another's sales team.
DISCONFIRMING_OBSERVATION: >
  Two comparable chains, each with the order under one company and the event under a different company, result in opportunities filed under different companies with no rule explaining the difference.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set up two comparable chains where the order's company and the event's company differ from each other, and compare which company each resulting opportunity is filed under.
```

## G11-EVENT_CRM_SALE-Q012

```yaml
QID: G11-EVENT_CRM_SALE-Q012
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When one order carries a line for the event alongside a separate, unrelated line, cancelling only the unrelated line does not remove or alter the opportunity generated from the event-related registration on the same order.
WHY_IT_MATTERS: >
  An unrelated cancellation on the same order silently disturbing an otherwise-unaffected lead would remove a genuine opportunity for a reason that has nothing to do with it.
DISCONFIRMING_OBSERVATION: >
  Cancelling an unrelated line on a multi-line order also removes or alters the opportunity generated from a separate, unaffected event-registration line on the same order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place a multi-line order with one event-related line and one unrelated line, let the event line generate an opportunity, cancel only the unrelated line, and check the effect on that opportunity.
```

## G11-EVENT_CRM_SALE-Q013

```yaml
QID: G11-EVENT_CRM_SALE-Q013
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a payment fails shortly after having provisionally created both a registration and an opportunity from it, the two are rolled back or flagged together, rather than one of the two surviving as though the payment had actually succeeded while the other is reversed.
WHY_IT_MATTERS: >
  A surviving opportunity or a surviving registration left behind after a failed payment misrepresents either a lead or an attendee as real when the transaction that was supposed to create it never actually completed.
DISCONFIRMING_OBSERVATION: >
  A payment that provisionally created both a registration and an opportunity fails, and one of the two remains in place as though nothing happened while the other is reversed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Trigger a payment that provisionally creates both a registration and an opportunity, then fail that payment, and check whether both are affected consistently.
```

## G11-EVENT_CRM_SALE-Q014

```yaml
QID: G11-EVENT_CRM_SALE-Q014
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a discount or promotional code applied on the order is later found to be invalid or is revoked after the resulting opportunity was already created, the opportunity's own recorded value is revisited to reflect the corrected amount actually owed, rather than continuing to reflect the value calculated under the now-revoked discount with no update.
WHY_IT_MATTERS: >
  An opportunity left showing a value based on a discount that has since been revoked misstates the real amount the sale is actually worth once the correction is applied.
DISCONFIRMING_OBSERVATION: >
  Revoking a promotional discount applied to the order after its resulting opportunity was created leaves that opportunity's value unchanged, still reflecting the amount calculated under the now-invalid discount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an opportunity from a registration whose order applied a promotional discount, revoke that discount as invalid afterward, and check whether the opportunity's value is revisited.
```

## G11-EVENT_CRM_SALE-Q015

```yaml
QID: G11-EVENT_CRM_SALE-Q015
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the same attendee places a second, later order for the same event (for example, an upgrade), the resulting chain either continues the existing opportunity already open for that attendee or deliberately opens a distinct new one, following one consistent rule, rather than the outcome being arbitrary between comparable cases.
WHY_IT_MATTERS: >
  An arbitrary choice between continuing and duplicating the opportunity leaves the sales pipeline showing either an inflated lead count or a lost record of genuine repeat interest, depending on which way it happened to fall.
DISCONFIRMING_OBSERVATION: >
  Two comparable second orders placed by attendees who already had an open opportunity from a first order result in one case continuing that opportunity and, in the other, opening an entirely disconnected new one, with no rule explaining the difference.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have the same attendee place a second order for the same event while an opportunity from a first order is still open, repeat this for a second comparable attendee, and compare how each case is handled.
```

## G11-EVENT_CRM_SALE-Q016

```yaml
QID: G11-EVENT_CRM_SALE-Q016
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When the attendee is not yet known at the time the order is confirmed and is named only afterward, opportunity generation waits until the attendee is actually known rather than generating an opportunity against a placeholder that later has to be silently re-pointed once a real name is supplied.
WHY_IT_MATTERS: >
  An opportunity generated against a placeholder identity, later re-pointed to a real person, can leave behind stale activity history that reads as belonging to someone who was never actually involved.
DISCONFIRMING_OBSERVATION: >
  An opportunity is generated before the attendee is named, referencing a placeholder identity, and is later silently re-pointed to the real attendee once named, carrying forward history that was originally recorded against the placeholder.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order without yet naming its attendee, check whether an opportunity is generated before the name is known, then name the attendee later and check what happens to that opportunity's identity reference.
```

## G11-EVENT_CRM_SALE-Q017

```yaml
QID: G11-EVENT_CRM_SALE-Q017
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Whether an opportunity generated by the chain is eventually closed as won or lost is a one-directional outcome that does not, on its own, feed back to alter the underlying registration or order's own recorded state.
WHY_IT_MATTERS: >
  An opportunity's own sales outcome flowing backward to silently change a real transaction's record would let a sales-side decision override a fact about what the customer actually did.
DISCONFIRMING_OBSERVATION: >
  Closing an opportunity generated by the chain as lost causes the underlying registration or order's own recorded state to change as a direct result of that closure.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Close an opportunity generated by the chain as lost, and check whether the underlying registration or order's own state changes as a result.
```

## G11-EVENT_CRM_SALE-Q018

```yaml
QID: G11-EVENT_CRM_SALE-Q018
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A registration that came from a free direct sign-up and one that came from a paid order for the same event remain distinguishable from each other after each has produced its own opportunity, so a reviewer looking only at the two opportunities can tell which chain type produced which.
WHY_IT_MATTERS: >
  If that distinction is lost once the opportunity exists, a warm, already-paying lead becomes indistinguishable from someone who has made no financial commitment at all.
DISCONFIRMING_OBSERVATION: >
  An opportunity from a free direct sign-up and one from a paid order, for the same event, cannot be told apart by looking at the opportunities alone.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create one opportunity from a free, direct sign-up and one from a paid order for the same event, and check whether the two remain distinguishable from opportunity information alone.
```

## G11-EVENT_CRM_SALE-Q019

```yaml
QID: G11-EVENT_CRM_SALE-Q019
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Duplicating an order that already produced a registration and, from it, an opportunity does not cause the new order's own fresh registration to inherit a live reference to that already-existing opportunity.
WHY_IT_MATTERS: >
  A brand-new, unpaid registration that appears to already have an established opportunity behind it misrepresents a new lead as further along than it actually is.
DISCONFIRMING_OBSERVATION: >
  Duplicating an order that already produced a registration and an opportunity results in the duplicate's new registration referencing the same, already-existing opportunity as though it belonged to the new transaction.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an order whose registration produced an opportunity, duplicate that order, and check whether the duplicate's own new registration references the existing opportunity.
```

## G11-EVENT_CRM_SALE-Q020

```yaml
QID: G11-EVENT_CRM_SALE-Q020
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the event referenced by the chain is rescheduled or has its capacity changed after an opportunity was already created from an order-derived registration for it, the opportunity's own record of the event's details stays current with the change rather than continuing to show the original, now-outdated information with no indication anything changed.
WHY_IT_MATTERS: >
  A salesperson working from stale event details on an opportunity may promise, or fail to warn about, a date or capacity that no longer applies.
DISCONFIRMING_OBSERVATION: >
  An event is rescheduled or has its capacity changed after an opportunity was created for it, and the opportunity continues to display the original, now-incorrect details with no update or flag.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an opportunity from a chain tied to a specific event, reschedule that event or change its capacity, and check whether the opportunity's own displayed event details update.
```

## G11-EVENT_CRM_SALE-Q021

```yaml
QID: G11-EVENT_CRM_SALE-Q021
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the same attendee is found to be named on two separate orders for the same event, placed under two different customer accounts, the sales credit reflected on the resulting opportunity is resolved to one specific order and account by a defined rule, rather than merging or splitting credit between the two with no documented basis.
WHY_IT_MATTERS: >
  Undocumented, arbitrary credit-splitting or merging between two real but separate commercial transactions for the same person misrepresents which sale, and whose sales effort, actually produced the qualified lead.
DISCONFIRMING_OBSERVATION: >
  The same attendee named on two separate orders, placed under two different accounts, for the same event results in sales credit on the resulting opportunity that cannot be traced to either specific order and account by any documented rule.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Register the same attendee under two separate orders placed under two different customer accounts for the same event, generate the resulting opportunity or opportunities, and check whether sales credit is resolved to a specific, documented order and account.
```

## G11-EVENT_CRM_SALE-Q022

```yaml
QID: G11-EVENT_CRM_SALE-Q022
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the salesperson credited on the order changes after an opportunity has already been created and assigned to the originally credited salesperson, the opportunity's own ownership follows a defined, documented rule about whether it reassigns or stays put, rather than the outcome varying unpredictably between comparable reassignments.
WHY_IT_MATTERS: >
  Undocumented, inconsistent behaviour here creates disputes over which salesperson is actually entitled to credit for a lead that has already been generated.
DISCONFIRMING_OBSERVATION: >
  Two comparable order salesperson reassignments, occurring after their respective opportunities were already created and assigned, result in one opportunity reassigning and the other staying with the original salesperson, with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reassign the credited salesperson on an order after its opportunity was already created and assigned, repeat for a comparable case, and compare whether the opportunity's ownership follows the reassignment consistently.
```

## G11-EVENT_CRM_SALE-Q023

```yaml
QID: G11-EVENT_CRM_SALE-Q023
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When only a partial deposit on the order was enough to create the registration, but not to fully confirm it, the resulting opportunity's own information reflects that the underlying payment is only partial, rather than presenting the transaction as though it were already fully secured.
WHY_IT_MATTERS: >
  An opportunity that overstates a partially paid transaction as fully secured overstates real, closed revenue to anyone using the pipeline to forecast.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated from a registration created by a partial deposit presents the underlying transaction as fully paid, with no indication that only a partial amount was actually received.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a registration using a partial deposit insufficient for full confirmation, let it generate an opportunity, and check whether that opportunity reflects the partial nature of the payment.
```

## G11-EVENT_CRM_SALE-Q024

```yaml
QID: G11-EVENT_CRM_SALE-Q024
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When revenue attribution to a salesperson or channel is credited through the chain, a full refund on the originating order at some later point reverses that attribution consistently, rather than the credited revenue remaining permanently counted regardless of the later refund.
WHY_IT_MATTERS: >
  Permanently crediting revenue that was later fully refunded overstates a salesperson's or channel's real, retained contribution indefinitely.
DISCONFIRMING_OBSERVATION: >
  A full refund on the order behind an attributed chain does not reverse or adjust the revenue attribution that was credited through that chain, leaving the credited figure permanently unchanged.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attribute revenue through the chain to a salesperson or channel, fully refund the originating order afterward, and check whether that attribution is reversed or adjusted.
```

## G11-EVENT_CRM_SALE-Q025

```yaml
QID: G11-EVENT_CRM_SALE-Q025
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an opportunity generated by the chain is manually merged into a separate, pre-existing opportunity for the same contact, the merged record preserves the link back to the originating registration and order, rather than silently severing that traceability once the merge happens.
WHY_IT_MATTERS: >
  A merge that quietly drops the chain's own provenance leaves no way to later show that part of a merged opportunity's history actually came from a real, paid registration.
DISCONFIRMING_OBSERVATION: >
  Merging a chain-generated opportunity into a separate pre-existing one drops the link back to the originating registration and order, leaving the merged record with no trace of that provenance.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge an opportunity generated by the chain into a separate, pre-existing opportunity for the same contact, and check whether the merged record retains the link back to the originating registration and order.
```

## G11-EVENT_CRM_SALE-Q026

```yaml
QID: G11-EVENT_CRM_SALE-Q026
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a registration's attendance is recorded after its own opportunity has already been closed, that later attendance fact is still reachable in some way from the closed opportunity's own record, rather than the chain going permanently silent the moment the opportunity closes.
WHY_IT_MATTERS: >
  A permanently frozen chain after closure discards a genuinely useful, later fact (that the person actually showed up) that could matter for future outreach or win/loss analysis.
DISCONFIRMING_OBSERVATION: >
  Attendance recorded for a registration after its opportunity was already closed leaves no trace reachable from the closed opportunity's own record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close an opportunity generated from a registration, then record that registration's attendance afterward, and check whether that later fact is reachable from the closed opportunity.
```

## G11-EVENT_CRM_SALE-Q027

```yaml
QID: G11-EVENT_CRM_SALE-Q027
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a company or organisational account places an order registering an unspecified number of attendees who are named only later, opportunities are generated per eventual named individual rather than a single opportunity being generated for the account as a whole regardless of how many individuals are later named.
WHY_IT_MATTERS: >
  One opportunity standing in for an unknown number of individuals understates the real number of distinct people a sales team should actually be following up with once names are known.
DISCONFIRMING_OBSERVATION: >
  A company account order that eventually names several distinct individual attendees results in only a single opportunity for the whole account, with no separate opportunity per named individual.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place a company-account order for an unspecified number of attendees, name several distinct individuals against it over time, and count the resulting opportunities against the number of named individuals.
```

## G11-EVENT_CRM_SALE-Q028

```yaml
QID: G11-EVENT_CRM_SALE-Q028
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the order's currency differs from the currency ordinarily used to track opportunity value, the expected value carried onto the opportunity reflects a defined, documented conversion rather than the original figure being copied across currencies unconverted.
WHY_IT_MATTERS: >
  An unconverted figure silently copied across currencies misstates the opportunity's real value by the entire exchange-rate difference, with no way to detect it from the number alone.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated from an order in a different currency than the one normally used for opportunity tracking shows a value that is numerically identical to the original amount, with no conversion applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place an order in a currency different from the one ordinarily used to track opportunity value, generate the resulting opportunity, and check whether its value reflects a documented conversion.
```

## G11-EVENT_CRM_SALE-Q029

```yaml
QID: G11-EVENT_CRM_SALE-Q029
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a registration transfer to a new attendee crosses a company or account boundary (the new attendee belongs to a different company account than the original), the opportunity's own company or account association is updated to follow the new attendee consistently, or is deliberately retained under a documented rule, rather than silently continuing to reference the original party's account with no rule governing which should apply.
WHY_IT_MATTERS: >
  An opportunity left filed under the wrong company account after a cross-boundary transfer routes it to a sales team that no longer has any real relationship with the actual current attendee.
DISCONFIRMING_OBSERVATION: >
  Transferring a registration to a new attendee belonging to a different company account leaves the associated opportunity's company or account reference pointing at the original party, with no update or documented rule explaining why.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create an opportunity from a registration, transfer that registration to a new attendee belonging to a different company account than the original, and check what happens to the opportunity's own account association.
```

## G11-EVENT_CRM_SALE-Q030

```yaml
QID: G11-EVENT_CRM_SALE-Q030
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order is cancelled and the same customer later places an unrelated new order for the same event, the new chain opens a fresh opportunity rather than silently reopening or reusing the earlier, now-stale opportunity from the cancelled order.
WHY_IT_MATTERS: >
  Reusing a stale opportunity from a cancelled transaction can carry forward outdated stage, value, or history that has nothing to do with the genuinely new order.
DISCONFIRMING_OBSERVATION: >
  A new, unrelated order placed after an earlier order for the same event was cancelled results in the earlier, cancelled order's stale opportunity being reopened or reused rather than a fresh one being created.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel an order that had already produced an opportunity, place a new, unrelated order for the same event and customer afterward, and check whether a fresh opportunity is created or the old one is reused.
```

## G11-EVENT_CRM_SALE-Q031

```yaml
QID: G11-EVENT_CRM_SALE-Q031
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The expected close date carried on an opportunity generated by the chain bears a meaningful relationship to the event's own date (for example, falling on or before it), rather than being set with no relationship to the event the opportunity actually originated from.
WHY_IT_MATTERS: >
  An expected close date unrelated to the actual event date makes forecasting based on that date meaningless for a transaction that is, by its nature, tied to a fixed real-world moment.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated by the chain carries an expected close date set well after the event it originated from has already taken place, with nothing tying the two dates together.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate an opportunity from a chain tied to an event with a known date, and check whether the opportunity's own expected close date bears any relationship to that event date.
```

## G11-EVENT_CRM_SALE-Q032

```yaml
QID: G11-EVENT_CRM_SALE-Q032
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an order contains a line for the event alongside a separate, unrelated line, the value carried onto the opportunity generated from the event-related registration reflects only the event-related portion of the order, rather than the full order amount including the unrelated line.
WHY_IT_MATTERS: >
  Inflating an opportunity's value with unrelated revenue overstates the real size of that specific lead beyond what the event transaction alone actually represents.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated from the event-related registration on a multi-line order carries a value equal to the full order amount, including the separate unrelated line.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place a multi-line order with one event-related line and one unrelated line of a different amount, generate the opportunity from the event line's registration, and check whether its value reflects only the event portion.
```

## G11-EVENT_CRM_SALE-Q033

```yaml
QID: G11-EVENT_CRM_SALE-Q033
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A refund issued specifically against the event line of a multi-line order, leaving the rest of the order intact, is reflected as a value adjustment on the opportunity generated from that line, rather than the opportunity's value remaining unchanged as though no refund had occurred.
WHY_IT_MATTERS: >
  An opportunity value left unchanged after its own underlying line was actually refunded overstates real revenue behind that specific lead.
DISCONFIRMING_OBSERVATION: >
  A refund issued specifically against the event line of a multi-line order leaves the value on the opportunity generated from that line completely unchanged.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Refund only the event-related line of a multi-line order that already produced an opportunity, and check whether that opportunity's value adjusts to reflect the partial refund.
```

## G11-EVENT_CRM_SALE-Q034

```yaml
QID: G11-EVENT_CRM_SALE-Q034
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a registration is downgraded to a lower-priced ticket type on the same order after its opportunity was already created, the opportunity's own expected value updates to reflect the new, lower amount rather than continuing to reflect the original, now-superseded higher figure.
WHY_IT_MATTERS: >
  An opportunity left showing the original higher value after a downgrade overstates the real remaining revenue behind that lead.
DISCONFIRMING_OBSERVATION: >
  Downgrading a registration to a lower-priced ticket type after its opportunity was created leaves that opportunity's expected value unchanged at the original, now-superseded higher amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an opportunity from a registration at one ticket-type price, downgrade that registration to a lower-priced ticket type on the same order, and check whether the opportunity's value updates.
```

## G11-EVENT_CRM_SALE-Q035

```yaml
QID: G11-EVENT_CRM_SALE-Q035
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A person with visibility restricted to only one side of the chain (able to see the order but not the event side, or the reverse) is correspondingly restricted from the opportunity that spans both, rather than being able to see or edit it in full regardless of which side they actually have access to.
WHY_IT_MATTERS: >
  An opportunity fully visible to someone restricted from one side of the chain that produced it defeats the purpose of restricting that side in the first place.
DISCONFIRMING_OBSERVATION: >
  A person restricted from viewing the event side of a chain, or the order side, is nonetheless able to see or edit the full opportunity generated from that chain without restriction.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Restrict a person's visibility to only one side of the chain (order or event), and check what access they actually have to the opportunity generated from that chain.
```

## G11-EVENT_CRM_SALE-Q036

```yaml
QID: G11-EVENT_CRM_SALE-Q036
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the order's company, the event's company, and the salesperson's own company are three different values in a multi-company setup, exactly one of the three, decided by a defined rule, determines the opportunity's own company assignment.
WHY_IT_MATTERS: >
  With three disagreeing companies and no defined rule, the opportunity's company assignment becomes effectively random, breaking whichever company's reporting boundary the outcome happens to land outside of.
DISCONFIRMING_OBSERVATION: >
  A chain with three disagreeing companies (order, event, and salesperson) produces an opportunity whose company assignment cannot be explained by any single, defined rule among the three.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set up a chain where the order's company, the event's company, and the salesperson's company are three different values, and check which one the resulting opportunity's company assignment actually follows.
```

## G11-EVENT_CRM_SALE-Q037

```yaml
QID: G11-EVENT_CRM_SALE-Q037
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When an order is placed on behalf of a named attendee by a distinct third party (such as an assistant or coordinator) whose own contact record differs from both the paying customer and the attendee, the resulting opportunity attaches to one of the three identities according to a defined, documented rule, rather than the outcome being arbitrary between comparable cases.
WHY_IT_MATTERS: >
  An arbitrarily chosen contact on the opportunity can direct sales follow-up at a coordinator with no buying authority, or miss the actual attendee, or miss the actual payer, depending on which of the three happened to be picked.
DISCONFIRMING_OBSERVATION: >
  Two comparable chains, each involving a distinct third-party orderer, payer, and attendee, produce opportunities attached to different identities among the three with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create two comparable chains where a third party places the order on behalf of a distinct named attendee, and compare which of the three identities each resulting opportunity attaches to.
```

## G11-EVENT_CRM_SALE-Q038

```yaml
QID: G11-EVENT_CRM_SALE-Q038
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When one order is split across two separate invoices, the opportunity generated from its registration reflects the payment status of both invoices together, rather than reacting only to whichever invoice happens to be settled first while ignoring the other.
WHY_IT_MATTERS: >
  An opportunity that reacts to only one of two invoices can show a transaction as fully paid, or as unpaid, when the true picture depends on both.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated from a registration on a split-invoice order updates to reflect full payment once only the first invoice is settled, with no regard for whether the second invoice remains outstanding.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split an order producing a registration across two separate invoices, settle only one, and check what payment status the resulting opportunity reflects.
```

## G11-EVENT_CRM_SALE-Q039

```yaml
QID: G11-EVENT_CRM_SALE-Q039
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a waitlisted registration is later promoted to confirmed after a cancellation elsewhere frees a seat, an opportunity already created while the registration was still waitlisted updates to reflect that promotion rather than remaining permanently marked as it was at the moment of its own creation.
WHY_IT_MATTERS: >
  An opportunity frozen at its original waitlisted state understates a lead's real, current standing once that person has actually secured a seat.
DISCONFIRMING_OBSERVATION: >
  A registration's promotion from waitlisted to confirmed leaves its already-existing opportunity unchanged, still reflecting the original waitlisted state with no update.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an opportunity from a registration still in a waitlisted state, promote that registration to confirmed after a cancellation elsewhere frees a seat, and check whether the opportunity updates.
```

## G11-EVENT_CRM_SALE-Q040

```yaml
QID: G11-EVENT_CRM_SALE-Q040
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a registration is found to be a duplicate of another and one of the two is deleted, the surviving registration's opportunity relationship is resolved to exactly one opportunity, rather than the opportunity being left pointing at nothing, or two duplicate opportunities being left behind after the registrations themselves were deduplicated.
WHY_IT_MATTERS: >
  Leaving an orphaned or duplicated opportunity behind after the underlying registrations were cleaned up undoes the very deduplication that was just performed, one level up in the chain.
DISCONFIRMING_OBSERVATION: >
  Deleting one of two duplicate registrations, each of which had already produced its own opportunity, leaves both opportunities standing independently with neither being resolved into the other.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two duplicate registrations for the same event and person, each producing its own opportunity, then delete one registration as the duplicate, and check what happens to its opportunity and the surviving one's.
```

## G11-EVENT_CRM_SALE-Q041

```yaml
QID: G11-EVENT_CRM_SALE-Q041
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The specific reason an order was cancelled (for example, the customer's own request, a failed payment, or the organiser calling off the event) has some defined bearing on the loss reason eventually recorded against the opportunity it produced, rather than the opportunity's own loss reason being set entirely independently with no connection to why the underlying order actually failed.
WHY_IT_MATTERS: >
  A loss reason on the opportunity that bears no relation to the real cause of the underlying cancellation gives a misleading account of why a lead was actually lost.
DISCONFIRMING_OBSERVATION: >
  Two opportunities whose underlying orders were cancelled for two different, known reasons (for example, customer request versus organiser cancellation) end up recorded with loss reasons that show no connection to either actual cause.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel two comparable orders for two different documented reasons, let each produce an opportunity that is then marked lost, and compare each opportunity's recorded loss reason against its order's actual cancellation reason.
```

## G11-EVENT_CRM_SALE-Q042

```yaml
QID: G11-EVENT_CRM_SALE-Q042
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The expected value carried onto an opportunity generated by the chain consistently reflects the same basis relative to the order's own tax treatment (for example, always the pre-tax amount, or always the tax-inclusive total), rather than varying between the two bases for otherwise comparable orders with no configuration difference to explain it.
WHY_IT_MATTERS: >
  An expected value that sometimes includes tax and sometimes excludes it, with no visible reason, makes the pipeline's total value figure meaningless because two identical-looking numbers can represent two different real amounts.
DISCONFIRMING_OBSERVATION: >
  Two comparable orders, one with tax applied and one without, produce opportunities whose expected values are calculated on different bases relative to tax with no configuration difference between them.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate opportunities from two comparable orders that differ only in whether tax was applied, and compare which basis (pre-tax or tax-inclusive) each opportunity's expected value reflects.
```

## G11-EVENT_CRM_SALE-Q043

```yaml
QID: G11-EVENT_CRM_SALE-Q043
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an order is placed at a specific negotiated rate different from the event's own generic list price, the expected value carried onto the resulting opportunity reflects the actual negotiated amount that was charged, rather than the event's generic list price regardless of what was actually paid.
WHY_IT_MATTERS: >
  An opportunity valued at the generic list price when a lower negotiated rate was actually charged overstates the real revenue behind that specific transaction.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated from an order placed at a negotiated rate below the event's generic list price shows an expected value equal to the generic list price rather than the actual negotiated amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place an order for an event at a rate negotiated below its generic list price, generate the resulting opportunity, and check which figure its expected value actually reflects.
```

## G11-EVENT_CRM_SALE-Q044

```yaml
QID: G11-EVENT_CRM_SALE-Q044
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two attendees on the same order swap their registrations with each other, their respective opportunities follow the swap to the correct corresponding person, rather than remaining matched to whichever registration record each opportunity originally pointed at, now mismatched to the wrong person.
WHY_IT_MATTERS: >
  A swap that leaves opportunities mismatched to the wrong person directs sales follow-up at a person who is no longer the one actually holding that seat.
DISCONFIRMING_OBSERVATION: >
  Swapping two attendees' registrations with each other on the same order leaves each attendee's opportunity still referencing the other, now-mismatched person, rather than following the correct individual.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create opportunities for two attendees on the same order, swap their registrations with each other, and check which person each opportunity ends up referencing.
```

## G11-EVENT_CRM_SALE-Q045

```yaml
QID: G11-EVENT_CRM_SALE-Q045
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the event underlying the chain is merged with, or replaced by, a corrected duplicate event record after an opportunity was already created, the opportunity's own reference to the event updates to the surviving record rather than continuing to point at a record that no longer exists or is no longer current.
WHY_IT_MATTERS: >
  An opportunity left referencing a superseded, no-longer-current event record can mislead a salesperson about the actual, current details of what they are selling.
DISCONFIRMING_OBSERVATION: >
  Merging or replacing an event record after an opportunity was created from a chain tied to it leaves that opportunity referencing the original, now-superseded event record with no update to the surviving one.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an opportunity from a chain tied to a specific event record, merge or replace that event record with a corrected duplicate afterward, and check what the opportunity's own event reference points to.
```

## G11-EVENT_CRM_SALE-Q046

```yaml
QID: G11-EVENT_CRM_SALE-Q046
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order's own confirmation is reversed back to an earlier, unconfirmed state after its registration and opportunity already exist, the downstream registration and opportunity are moved to a consistent, defined state to match, rather than being left in a state that presumes a confirmation which no longer actually holds.
WHY_IT_MATTERS: >
  A registration and opportunity left presuming a confirmation that was actually reversed can let attendance, revenue, or pipeline figures rest on a transaction that, as far as the order itself is concerned, no longer went through.
DISCONFIRMING_OBSERVATION: >
  Reversing an order's own confirmation back to an unconfirmed state leaves its already-created registration and opportunity fully unaffected, still presuming the confirmation that was just undone.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order to the point where a registration and opportunity both exist, reverse the order's own confirmation back to an unconfirmed state, and check what happens to the registration and opportunity.
```

## G11-EVENT_CRM_SALE-Q047

```yaml
QID: G11-EVENT_CRM_SALE-Q047
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an order's payment is settled asynchronously well after the order and registration were first created (for example, a bank transfer that clears several days later), the opportunity generated once that late settlement is confirmed attaches to the registration as it currently stands, rather than to a stale copy of that registration's details as they existed back when the order was first placed.
WHY_IT_MATTERS: >
  An opportunity built from stale, out-of-date registration details, such as an attendee who has since transferred their seat to someone else, misdirects sales effort at information that was already superseded by the time the opportunity was actually generated.
DISCONFIRMING_OBSERVATION: >
  An opportunity generated after a delayed payment settlement reflects the registration's original details from when the order was first placed, even though the registration has since been changed, such as being transferred to a different attendee, before the payment actually cleared.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Place an order whose payment settles asynchronously after a delay, change the resulting registration's details such as transferring it to a different attendee before the payment actually clears, then let the delayed settlement trigger opportunity generation, and check whose details the opportunity reflects.
```

## G11-EVENT_CRM_SALE-Q048

```yaml
QID: G11-EVENT_CRM_SALE-Q048
MODULE: event_crm_sale
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The three-part trail connecting a given opportunity to its specific originating order, registration, and order line remains reconstructable even after the order has since been archived or closed under a later accounting period.
WHY_IT_MATTERS: >
  A trail that becomes unreconstructable once the order is archived removes exactly the evidence a later audit would need, at exactly the point when the transaction is old enough to actually be audited.
DISCONFIRMING_OBSERVATION: >
  An opportunity's specific originating order, registration, and order line can no longer all be identified once the underlying order has been archived or closed under a later accounting period.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive or close the order behind a chain-generated opportunity under a later accounting period, and check whether its originating order, registration, and order line can still all be identified from the opportunity.
```
