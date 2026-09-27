# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_gelato Module MVQ Bank

**Document ID:** GMVQ-G08-SALE_GELATO-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_gelato`
**Wave:** W2
**Author Cell:** GMVQ PRODUCTION TEAM P-S10
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This bank supplies the module-specific MVQ set for `sale_gelato`, the commercial and production
relationship between a confirmed sales order and an external on-demand production and fulfilment
provider. Per the G08 SALES group brief this module is a bridge: it owns almost no behaviour of
its own, and every question below fails only at the seam between a normal commercial commitment
and the defining condition of on-demand production — the item does not exist until the customer
buys it, and a third party makes it, prices it, and ships it. Ground covered includes price
commitment timing against the provider's own catalogue cost, the customer's artwork or
personalisation once it leaves your systems, production failure after payment has been captured,
the honesty of the delivery date promised against what the provider actually estimates, the sunk
cost of a personalised item cancelled mid-production, delivery evidence you do not independently
control, returns on a made-to-order item, attribution of a provider's own quality failure,
catalogue volatility while orders sit open, per-company credential and cost isolation, invoice
reconciliation against the provider, and the privacy basis for disclosing a customer's address to
a third party. Every question passes the seam test: if the item were instead an ordinary stocked
product sold and fulfilled entirely within the business, the question would no longer make sense;
a question that would still make sense either way was cut during authoring rather than included.
Coverage is spread across business capability, business rule, state transition, configuration
dependency, role and permission, exception path, cancellation, reversal, negative case,
cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency
and ordering, runtime reachability, configuration reachability, and source/runtime contradiction
potential. This bank supplements the 55-question Standard bank; combined research depth for this
module is 55 + 48 = 103.

This module is deliberately distinguished from the existing `stock_dropshipping` bank in the same
programme: dropshipping concerns an already-existing catalogue item shipped from a third-party
supplier's own stock, with no personalisation and no manufacturing step. This module's defining
condition is that the item does not exist in any form until the order is placed, is typically
personalised with customer-supplied content, cannot be resold once production starts, and the
provider relationship is a production relationship, not a stock-sourcing relationship. No question
in this bank restates a dropshipping question with the noun changed; the sibling bank's
HYPOTHESIS lines were read in full before authoring and none is duplicated here.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses; none was
  trimmed or stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field — "the external on-demand production and fulfilment provider" (or "the
  provider" once established within a question) stands in for it throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_GELATO-Q001

```yaml
QID: G08-SALE_GELATO-Q001
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once a customer order for a made-to-order line is confirmed at a stated price, a later change in what the external on-demand production and fulfilment provider charges for producing that same catalogue item does not retroactively alter the price already committed to the customer.
WHY_IT_MATTERS: >
  If the confirmed customer price can move with the provider's own price list, the business commitment made at the moment of sale is not actually fixed, and the customer can be charged an amount they never agreed to.
DISCONFIRMING_OBSERVATION: >
  A confirmed order's customer-facing price changes after confirmation solely because the provider's cost for producing the item changed, with no separate commercial action by anyone on your side causing it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm a made-to-order line at a known price, then simulate or observe a change in the provider's stated cost for that same catalogue item, and check whether the confirmed order's price moves.
```

## G08-SALE_GELATO-Q002

```yaml
QID: G08-SALE_GELATO-Q002
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The price shown to the customer for a made-to-order catalogue item at the moment of quotation reflects a defined, current synchronization point with the external on-demand production and fulfilment provider's own pricing, rather than an indefinitely stale figure that was fetched once and never refreshed.
WHY_IT_MATTERS: >
  If the quoted price is based on catalogue pricing that is never refreshed, a business could unknowingly quote well below or above the provider's real current cost for an extended period, with no defined mechanism to catch it.
DISCONFIRMING_OBSERVATION: >
  The price shown for a made-to-order catalogue item stays fixed at an old value with no defined refresh point, even though the provider's own price for that item is known to have changed some time ago.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Identify what, if anything, triggers a re-read of the provider's catalogue pricing, and check how long a stale price can persist before it is next refreshed.
```

## G08-SALE_GELATO-Q003

```yaml
QID: G08-SALE_GELATO-Q003
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A confirmed made-to-order sale whose eventual provider cost turns out to exceed the price already charged to the customer is surfaced somewhere as a loss-making transaction, rather than disappearing into the accounts with no distinguishing signal from a normally profitable one.
WHY_IT_MATTERS: >
  Without a signal, a business cannot tell how often its assumed pricing for on-demand items is failing to cover the external on-demand production and fulfilment provider's actual charge, and cannot correct the pricing before it recurs at scale.
DISCONFIRMING_OBSERVATION: >
  A transaction where the provider's actual charge exceeded the price the customer paid is recorded and reported identically to a transaction where it did not, with nothing distinguishing the two afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a made-to-order transaction where the provider's actual charge is known to exceed the price charged, then inspect the resulting record and any report that would ordinarily surface margin.
```

## G08-SALE_GELATO-Q004

```yaml
QID: G08-SALE_GELATO-Q004
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  For an order placed before a stated change in the external on-demand production and fulfilment provider's catalogue price takes effect, but not yet sent into production at the moment the change takes effect, the system applies one defined, documented rule for which price governs the transaction rather than the outcome depending on unpredictable timing.
WHY_IT_MATTERS: >
  Without one defined rule, otherwise-identical orders that happen to sit in the queue at the moment of a provider price change could be costed inconsistently, undermining any trust in the reported margin for that period.
DISCONFIRMING_OBSERVATION: >
  Two orders placed under the same price and sent to production on either side of a provider price change end up costed by two different, undocumented rules with no single stated policy governing either.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place an order shortly before a known provider catalogue price change takes effect, allow production hand-off to occur after the change, and trace which cost value the transaction is ultimately costed against.
```

## G08-SALE_GELATO-Q005

```yaml
QID: G08-SALE_GELATO-Q005
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Customer-supplied artwork or personalisation content submitted to the external on-demand production and fulfilment provider for a made-to-order line remains attached to, and retrievable against, that specific order line for as long as the record needs to be traced, rather than existing only transiently at the moment the order was placed.
WHY_IT_MATTERS: >
  If the personalisation content cannot later be retrieved against the order it belongs to, a dispute, a reprint, or a quality investigation has no way to confirm what was actually supposed to be produced.
DISCONFIRMING_OBSERVATION: >
  An order for a personalised item can be located weeks later with no way to retrieve or view the specific artwork or personalisation content that was submitted for it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Place a personalised order with distinct customer-supplied content, allow time to pass, then attempt to retrieve that specific content against the order record.
```

## G08-SALE_GELATO-Q006

```yaml
QID: G08-SALE_GELATO-Q006
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the external on-demand production and fulfilment provider rejects a customer's submitted personalisation content as unusable after the order has already been confirmed and paid, the order is surfaced as an exception requiring a decision rather than silently proceeding as though production had started.
WHY_IT_MATTERS: >
  If a rejected-content order continues to look normal, the business will not learn that the customer needs to resupply content, or that a refund decision is needed, until the customer complains.
DISCONFIRMING_OBSERVATION: >
  An order whose personalisation content was rejected by the provider as unusable remains indistinguishable in status from an order proceeding normally through production.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Submit personalisation content known to be rejectable by the provider on a paid, confirmed order, and observe what status or notice, if any, results.
```

## G08-SALE_GELATO-Q007

```yaml
QID: G08-SALE_GELATO-Q007
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  What happens to a customer's personalisation content once it has been sent to the external on-demand production and fulfilment provider and the item it was used to produce has shipped — whether it is retained, for how long, or deleted — is an explicit, documented behaviour rather than an unstated assumption nobody in the business could answer if a customer asked.
WHY_IT_MATTERS: >
  Personalisation content can include a customer's own image or likeness; not knowing whether or for how long it persists after the transaction is finished is a real exposure the business cannot currently answer for.
DISCONFIRMING_OBSERVATION: >
  No one and nothing in the system can state, for a completed personalised order, whether the submitted content still exists anywhere, has been deleted, or was ever retained past production.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Complete a personalised order through to shipment, then determine whether the submitted content's post-production retention or deletion behaviour is documented or observable anywhere.
```

## G08-SALE_GELATO-Q008

```yaml
QID: G08-SALE_GELATO-Q008
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A customer reordering a previously purchased personalised item that was produced by the external on-demand production and fulfilment provider is offered a single, defined source of truth for the personalisation content to reuse — either your own retained copy or a fresh resubmission — rather than the reorder path being free to silently mix stale and fresh content across attempts.
WHY_IT_MATTERS: >
  If the source of reused personalisation content is undefined, a reorder can unknowingly reproduce an outdated or already-superseded version of what the customer actually wants this time.
DISCONFIRMING_OBSERVATION: >
  Reordering the same personalised item twice in immediate succession, with no stated change by the customer, produces two orders referencing personalisation content from two different, unexplained sources.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Place a personalised order, then place a reorder of the same item shortly after, and trace which personalisation content source each order actually references.
```

## G08-SALE_GELATO-Q009

```yaml
QID: G08-SALE_GELATO-Q009
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external on-demand production and fulfilment provider is unable to produce an order after it has already been confirmed and paid, the order moves into an explicit exception state requiring resolution rather than remaining presented to staff and the customer as proceeding normally.
WHY_IT_MATTERS: >
  An order that silently stays "in progress" after production has actually failed leaves the business unaware that a paid customer is owed either a resolution or a refund.
DISCONFIRMING_OBSERVATION: >
  A confirmed, paid order that the provider has declined to produce shows the same status as one currently and genuinely in production, with nothing distinguishing the two.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Trigger or simulate a production decline from the provider on a confirmed, paid order and inspect the resulting order status as seen by staff and by the customer.
```

## G08-SALE_GELATO-Q010

```yaml
QID: G08-SALE_GELATO-Q010
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When payment has already been captured from the customer for an order the external on-demand production and fulfilment provider then fails to produce, a defined refund or credit path is triggered rather than the captured payment simply remaining recorded as revenue for goods that were never made.
WHY_IT_MATTERS: >
  Recognising revenue for an item that was never produced overstates the business's actual income and leaves an obligation to the customer that nothing is tracking.
DISCONFIRMING_OBSERVATION: >
  An order the provider failed to produce still shows the customer's payment recognised as completed revenue with no linked refund, credit, or other resolving obligation recorded against it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Capture payment on an order, then have the provider fail to produce it, and trace what happens to the recognised payment and whether any offsetting obligation is created.
```

## G08-SALE_GELATO-Q011

```yaml
QID: G08-SALE_GELATO-Q011
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A production failure reported by the external on-demand production and fulfilment provider on a confirmed order results in a customer-facing notice or an assigned internal follow-up action, rather than the failure being recorded only as an internal state with nothing surfaced to anyone responsible for telling the customer.
WHY_IT_MATTERS: >
  A production failure that never reaches a human responsible for the customer relationship will surface only when the customer asks where their order is, after the business had the information all along.
DISCONFIRMING_OBSERVATION: >
  A production failure is recorded on an order with no notification, task, or assignment generated for any person or process responsible for the customer relationship.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Trigger a production failure on a confirmed order and check whether any notification, task, or customer-facing communication is generated as a result.
```

## G08-SALE_GELATO-Q012

```yaml
QID: G08-SALE_GELATO-Q012
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an order contains several made-to-order lines and the external on-demand production and fulfilment provider fails to produce only one of them, the failure is tracked at the level of that specific line rather than forcing the entire order into the same exception state as the lines that are producing normally.
WHY_IT_MATTERS: >
  If a single-line failure is only representable at the whole-order level, staff cannot tell which part of a multi-item order actually needs attention, and the customer's other items may be delayed or confused unnecessarily.
DISCONFIRMING_OBSERVATION: >
  A multi-line order where only one made-to-order line failed production shows the same all-or-nothing exception state as if every line in the order had failed, with no way to see that the other lines are unaffected.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Place a multi-line order with more than one made-to-order item, cause only one line to fail production, and inspect whether the exception is represented at the line level or the whole-order level.
```

## G08-SALE_GELATO-Q013

```yaml
QID: G08-SALE_GELATO-Q013
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The production and shipping timeframe presented to the customer for a made-to-order item is drawn from a stated, current estimate supplied by the external on-demand production and fulfilment provider, rather than from a generic internal assumption that is not actually tied to what the provider currently expects.
WHY_IT_MATTERS: >
  If the promised date is not actually linked to the provider's own current estimate, the business is making a commitment to the customer that nothing behind the scenes is actually tracking or capable of honouring.
DISCONFIRMING_OBSERVATION: >
  The date presented to the customer for a made-to-order item does not change even when the provider's own stated production and shipping estimate for that item is known to have changed.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Identify where the customer-facing commitment date originates, and compare it against a known change in the provider's own stated estimate for the same item.
```

## G08-SALE_GELATO-Q014

```yaml
QID: G08-SALE_GELATO-Q014
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order whose production is running later than the date already promised to the customer is surfaced to staff as an at-risk order before the promised date passes, rather than only becoming visible once the customer has already complained.
WHY_IT_MATTERS: >
  Learning about a broken delivery promise only from the customer's complaint means the business has already lost the chance to manage the situation proactively.
DISCONFIRMING_OBSERVATION: >
  An order that is behind the external on-demand production and fulfilment provider's own estimate relative to the date promised to the customer generates no internal visibility of any kind before the promised date has already passed.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Place an order and allow or simulate the provider's production running later than the promised date, then check what, if anything, becomes visible to staff before that date passes.
```

## G08-SALE_GELATO-Q015

```yaml
QID: G08-SALE_GELATO-Q015
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Any margin added on top of the external on-demand production and fulfilment provider's own estimate before the date is shown to the customer is an explicit, adjustable setting rather than a fixed assumption buried with no visible control.
WHY_IT_MATTERS: >
  A business operating across product types or seasons may need to adjust how much buffer it adds to a provider's estimate, and cannot do so if that buffer is not exposed as something it can actually change.
DISCONFIRMING_OBSERVATION: >
  The gap between the provider's own stated estimate and the date shown to the customer is a fixed value with no setting anywhere that controls or explains it.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Locate any configuration governing the difference between the provider's estimate and the customer-facing promised date, and determine whether it is adjustable or fixed.
```

## G08-SALE_GELATO-Q016

```yaml
QID: G08-SALE_GELATO-Q016
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The specific date once presented to a customer as the delivery commitment for an order fulfilled by the external on-demand production and fulfilment provider is preserved as a retrievable record, even after later internal recalculation moves the working estimate, so that what was actually promised can still be established afterward.
WHY_IT_MATTERS: >
  Without preserving what was actually promised, a customer complaint about a missed date cannot be checked against the truth, and the business cannot tell whether it kept its own commitment.
DISCONFIRMING_OBSERVATION: >
  After an internal estimate changes, the date originally shown to the customer for that order can no longer be retrieved or reconstructed from the record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Note the date shown to a customer at order time, allow the internal estimate to change, and attempt to retrieve what was originally promised.
```

## G08-SALE_GELATO-Q017

```yaml
QID: G08-SALE_GELATO-Q017
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An attempt to cancel a made-to-order line after the external on-demand production and fulfilment provider has already started producing it is met with an explicit warning or gate reflecting that the item cannot be resold, rather than being processed identically to cancelling an order that has not yet entered production.
WHY_IT_MATTERS: >
  Treating a post-production cancellation the same as a pre-production one hides a real, often non-recoverable cost from whoever is approving the cancellation.
DISCONFIRMING_OBSERVATION: >
  Cancelling a made-to-order line after production has started completes with the identical confirmation and consequence as cancelling one that has not yet started.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Attempt to cancel an order line at two points — before and after the provider has started production — and compare what the system presents and permits in each case.
```

## G08-SALE_GELATO-Q018

```yaml
QID: G08-SALE_GELATO-Q018
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a personalised item is cancelled after the external on-demand production and fulfilment provider has already committed cost to producing it, that sunk cost is recorded as a loss against the transaction rather than disappearing from the accounts as though the order had never incurred any cost at all.
WHY_IT_MATTERS: >
  If the sunk production cost is not recorded, the business cannot see how much money post-production cancellations are actually costing it over time.
DISCONFIRMING_OBSERVATION: >
  A cancelled order for which the provider had already committed production cost shows no cost or loss recorded anywhere against that transaction.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel an order after production has started with the provider, and check whether the resulting record shows any recorded cost or loss for the item that can no longer be resold.
```

## G08-SALE_GELATO-Q019

```yaml
QID: G08-SALE_GELATO-Q019
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Cancelling a made-to-order line after production has started requires an authorisation distinct from the authorisation needed to cancel an order that has not yet entered production, reflecting the real cost difference between the two actions.
WHY_IT_MATTERS: >
  Without a distinct authorisation, any staff member able to cancel an ordinary order can also unknowingly commit the business to a sunk-cost loss with no extra check.
DISCONFIRMING_OBSERVATION: >
  The same role or permission that can cancel a not-yet-started order can cancel a post-production order with no additional check or approval step required.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare what permission or approval, if any, is required to cancel an order before production starts versus after it has started with the external on-demand production and fulfilment provider.
```

## G08-SALE_GELATO-Q020

```yaml
QID: G08-SALE_GELATO-Q020
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A made-to-order line carries a distinct, visible state once the external on-demand production and fulfilment provider has accepted it into production, separate from the state it held while still awaiting that acceptance, so that whether cancellation is still consequence-free can be determined before attempting it.
WHY_IT_MATTERS: >
  Without a visible distinction, staff have no way to know in advance whether attempting a cancellation is safe or costly, and must find out only by trying it.
DISCONFIRMING_OBSERVATION: >
  A made-to-order line shows an identical status before and after the provider has accepted it into production, with nothing to indicate the change.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Track a made-to-order line's visible status across the point where the provider accepts it into production, and check whether that transition is represented.
```

## G08-SALE_GELATO-Q021

```yaml
QID: G08-SALE_GELATO-Q021
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order marked delivered based solely on a claim from the external on-demand production and fulfilment provider is distinguishable in the record from an order your own operation directly confirmed as delivered, rather than the two being presented with identical confidence.
WHY_IT_MATTERS: >
  Presenting a third party's unverified claim with the same confidence as your own confirmed delivery hides the fact that you have no independent way to confirm the customer actually received the item.
DISCONFIRMING_OBSERVATION: >
  A delivery confirmed only by the provider's own claim and a delivery your own operation directly witnessed are recorded and displayed in an identical way, with nothing distinguishing the source of the confirmation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark an order as delivered based on the provider's own report and inspect whether the record shows the source of that confirmation.
```

## G08-SALE_GELATO-Q022

```yaml
QID: G08-SALE_GELATO-Q022
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a customer disputes ever receiving an order marked delivered on the strength of the external on-demand production and fulfilment provider's own claim, the record retains enough about that claim's origin to support or contest the dispute, rather than the delivered status being final and unexaminable.
WHY_IT_MATTERS: >
  If nothing about the underlying claim can be examined after the fact, the business is left unable to investigate a delivery dispute on a made-to-order item at all.
DISCONFIRMING_OBSERVATION: >
  A customer dispute over a delivery marked complete only by the provider's own claim cannot be investigated because no detail about that original claim was retained.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Mark an order delivered from the provider's own claim, then attempt to investigate a simulated customer dispute over that delivery using only the retained record.
```

## G08-SALE_GELATO-Q023

```yaml
QID: G08-SALE_GELATO-Q023
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A defined mechanism exists for the external on-demand production and fulfilment provider's own delivery confirmation to reach and update the order's status, rather than the order having no route by which that confirmation could ever arrive.
WHY_IT_MATTERS: >
  If there is no route for the provider's confirmation to reach the order, delivery status for provider-shipped orders can never resolve at all, regardless of what actually happens to the shipment.
DISCONFIRMING_OBSERVATION: >
  An order that the provider has genuinely confirmed as delivered shows no change in status because no mechanism exists to receive or apply that confirmation.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Trace whether, and how, a delivery confirmation reported by the provider is capable of reaching and updating the order's own status.
```

## G08-SALE_GELATO-Q024

```yaml
QID: G08-SALE_GELATO-Q024
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whatever specific evidence the external on-demand production and fulfilment provider supplies to support a delivery confirmation is retained alongside the order, rather than only the resulting delivered/not-delivered status being kept with the underlying evidence discarded.
WHY_IT_MATTERS: >
  Keeping only the final status and discarding the supporting evidence means nothing can later verify why an order was considered delivered.
DISCONFIRMING_OBSERVATION: >
  An order shows a delivered status with no retained evidence of any kind explaining what specifically the provider supplied to justify it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have the provider report a delivery confirmation with supporting detail, then check what of that detail, if anything, is retained against the order afterward.
```

## G08-SALE_GELATO-Q025

```yaml
QID: G08-SALE_GELATO-Q025
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A personalised, made-to-order item fulfilled by the external on-demand production and fulfilment provider is governed by a return policy path that is explicitly distinguished from the return path for a normal stocked item, rather than defaulting silently to the same policy that assumes the item can simply be restocked and resold.
WHY_IT_MATTERS: >
  A made-to-order item usually cannot be resold once personalised, so applying the same return assumptions as ordinary stock can commit the business to accepting a return it has no way to recover value from.
DISCONFIRMING_OBSERVATION: >
  Initiating a return for a personalised made-to-order item follows an identical path and identical default outcome as returning an ordinary stocked item.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Initiate a return for a personalised made-to-order item and compare the path and outcome against initiating a return for an ordinary stocked item.
```

## G08-SALE_GELATO-Q026

```yaml
QID: G08-SALE_GELATO-Q026
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a return on a made-to-order item is actually caused by the external on-demand production and fulfilment provider's own production quality, the resolution reflects the provider's own responsibility for that cost rather than the loss falling by default entirely on the business regardless of who caused it.
WHY_IT_MATTERS: >
  If quality-caused returns always land as a pure business cost, there is no mechanism recovering the loss from the party actually responsible for it.
DISCONFIRMING_OBSERVATION: >
  A return caused by a documented quality failure on the provider's side is resolved with the identical financial outcome as a return caused by the customer simply changing their mind.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Process a return attributed to a quality issue on the provider's side and compare its financial resolution against a return attributed to the customer's own change of mind.
```

## G08-SALE_GELATO-Q027

```yaml
QID: G08-SALE_GELATO-Q027
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A physically returned made-to-order item produced by the external on-demand production and fulfilment provider is not, by default, treated as available stock to be resold to another customer, given that it was personalised for the original customer specifically.
WHY_IT_MATTERS: >
  Automatically returning a personalised item to sellable stock risks a future customer receiving an item that was made for someone else.
DISCONFIRMING_OBSERVATION: >
  A returned personalised made-to-order item is placed into a status that marks it as available for sale to another customer with nothing distinguishing it from ordinary returned stock.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Process the physical return of a personalised made-to-order item and check what stock status, if any, it is assigned afterward.
```

## G08-SALE_GELATO-Q028

```yaml
QID: G08-SALE_GELATO-Q028
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A return processed against a made-to-order line remains traceable back to the specific order that the external on-demand production and fulfilment provider originally fulfilled, rather than the link between the return and its originating production being lost once the return is recorded.
WHY_IT_MATTERS: >
  Without that link, a pattern of returns caused by a specific production run or a specific catalogue item cannot be identified at all.
DISCONFIRMING_OBSERVATION: >
  A processed return for a made-to-order item cannot be traced back to the specific original order or production instance it came from.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Process a return for a made-to-order item, then attempt to trace it back to the original order the provider fulfilled.
```

## G08-SALE_GELATO-Q029

```yaml
QID: G08-SALE_GELATO-Q029
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A customer complaint about a made-to-order item can be recorded as attributable to the external on-demand production and fulfilment provider's own production quality, distinct from a complaint attributable to your own order-handling process, so the two causes can be told apart over time.
WHY_IT_MATTERS: >
  If every complaint about a made-to-order item is recorded the same way regardless of cause, the business cannot tell whether it has a provider quality problem or a process problem of its own.
DISCONFIRMING_OBSERVATION: >
  There is no way to record or later distinguish a complaint caused by the provider's production quality from one caused by an internal handling error.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a customer complaint known to be caused by the provider's production quality and check whether that attribution is captured anywhere distinguishable from other complaint causes.
```

## G08-SALE_GELATO-Q030

```yaml
QID: G08-SALE_GELATO-Q030
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeated quality-attributed complaints against the same catalogue item fulfilled by the external on-demand production and fulfilment provider accumulate somewhere retrievable, rather than each complaint existing only as an isolated record with no way to see the pattern across orders.
WHY_IT_MATTERS: >
  Without visibility into a pattern, the business has no basis for deciding to stop offering a catalogue item that is repeatedly produced badly.
DISCONFIRMING_OBSERVATION: >
  Several quality-attributed complaints exist against the same catalogue item, but nothing anywhere makes it possible to see that they are related to each other or to that specific item.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record several complaints attributed to provider quality against the same catalogue item, and check whether any view or report reveals the pattern.
```

## G08-SALE_GELATO-Q031

```yaml
QID: G08-SALE_GELATO-Q031
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A disagreement between your business and the external on-demand production and fulfilment provider over whether a quality failure actually occurred is represented as an open, unresolved item requiring a decision, rather than the cost defaulting silently to the business the moment the customer is refunded.
WHY_IT_MATTERS: >
  If the customer-facing refund automatically closes the question of who was at fault, the business loses any leverage or evidence trail to recover the cost from the provider later.
DISCONFIRMING_OBSERVATION: >
  Refunding a customer for a provider-attributed quality issue closes the transaction with no separate, still-open item tracking whether the provider disputes or owes for that failure.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Refund a customer for a quality issue attributed to the provider and check whether a separate, still-open record tracks the unresolved question of the provider's own liability.
```

## G08-SALE_GELATO-Q032

```yaml
QID: G08-SALE_GELATO-Q032
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Attributing a customer complaint to the external on-demand production and fulfilment provider's own fault, as opposed to an internal cause, is an action available only to a defined role, rather than any staff member being able to set that attribution without any check.
WHY_IT_MATTERS: >
  An unchecked attribution could be used to mask an internal handling failure as a provider's fault, distorting any later analysis of where problems are actually coming from.
DISCONFIRMING_OBSERVATION: >
  Any staff member, regardless of role, can set a complaint's attribution to provider fault with no distinct permission or review required.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Attempt to attribute a complaint to provider fault using different staff roles and check whether the action is gated by permission.
```

## G08-SALE_GELATO-Q033

```yaml
QID: G08-SALE_GELATO-Q033
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external on-demand production and fulfilment provider withdraws a catalogue item, your own corresponding sellable product record is prevented from continuing to accept new orders, rather than remaining active and sellable with nothing reflecting that the provider can no longer fulfil it.
WHY_IT_MATTERS: >
  Continuing to sell an item the provider has withdrawn commits the business to promises it now has no way to keep.
DISCONFIRMING_OBSERVATION: >
  A new order is accepted for an item after the provider has withdrawn it from its own catalogue, with nothing on your side having blocked or flagged the sale.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Simulate or observe the provider withdrawing a catalogue item that has a corresponding active sellable product on your side, then attempt to place a new order for it.
```

## G08-SALE_GELATO-Q034

```yaml
QID: G08-SALE_GELATO-Q034
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Orders already placed for a catalogue item before the external on-demand production and fulfilment provider withdraws it, but not yet produced at the moment of withdrawal, are surfaced as an exception requiring resolution rather than being left to proceed as though production could still occur.
WHY_IT_MATTERS: >
  An order left proceeding normally after its item has actually become impossible to produce will eventually fail invisibly, at the worst possible moment for the customer relationship.
DISCONFIRMING_OBSERVATION: >
  An order for a withdrawn catalogue item, placed before the withdrawal, continues to show a normal in-progress status with no exception raised.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Place an order for a catalogue item, simulate the provider withdrawing that item before production, and check the resulting status of the already-placed order.
```

## G08-SALE_GELATO-Q035

```yaml
QID: G08-SALE_GELATO-Q035
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A defined process exists that checks whether a catalogue item currently offered for sale is still actually offered by the external on-demand production and fulfilment provider, rather than a withdrawal on the provider's side only ever being discovered by chance when someone happens to try to produce that item.
WHY_IT_MATTERS: >
  Without any active check, catalogue withdrawals can go unnoticed indefinitely, and the business only discovers the problem when a real customer order fails.
DISCONFIRMING_OBSERVATION: >
  A catalogue item withdrawn by the provider some time ago is still shown as available with no defined process having ever surfaced the discrepancy.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Simulate a provider catalogue withdrawal and determine whether any scheduled or triggered process on your side is capable of detecting it before a new order relies on it.
```

## G08-SALE_GELATO-Q036

```yaml
QID: G08-SALE_GELATO-Q036
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When only a specific variant of a catalogue item is withdrawn by the external on-demand production and fulfilment provider, only that variant is prevented from further sale, rather than the entire product family being blocked or, conversely, the whole family remaining sellable including the withdrawn variant.
WHY_IT_MATTERS: >
  Treating a partial withdrawal as either total or as nothing at all either blocks sales that are still legitimate or continues sales that will fail.
DISCONFIRMING_OBSERVATION: >
  The withdrawal of a single variant results in either the entire product family becoming unsellable or the withdrawn variant itself remaining orderable.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Simulate the provider withdrawing a single variant of a multi-variant catalogue item and check the sellable status of the withdrawn variant versus its siblings.
```

## G08-SALE_GELATO-Q037

```yaml
QID: G08-SALE_GELATO-Q037
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  In a multi-company setup, an order placed under a given company is sent to the external on-demand production and fulfilment provider, and billed, under that specific company's own credentials, rather than a shared or default credential being used regardless of which company the order actually belongs to.
WHY_IT_MATTERS: >
  If orders from different companies are all sent under one shared credential, the provider's own cost billing cannot be correctly attributed back to the company that actually owes it.
DISCONFIRMING_OBSERVATION: >
  An order placed under one company in a multi-company setup is transmitted to the provider under a different company's credentials, or under a credential not specific to either.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  In a multi-company configuration, place orders under two different companies and trace which credentials each order is actually transmitted to the provider under.
```

## G08-SALE_GELATO-Q038

```yaml
QID: G08-SALE_GELATO-Q038
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  In a multi-tenant deployment, no tenant's configured credential with the external on-demand production and fulfilment provider is reachable from, or usable by, a process scoped to a different tenant.
WHY_IT_MATTERS: >
  A credential crossing tenant boundaries could let one tenant's orders be billed to, or fulfilled under, an entirely different customer's account with that provider.
DISCONFIRMING_OBSERVATION: >
  A process or order scoped to one tenant is found to use, or be capable of using, a provider credential configured for a different tenant.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  In a multi-tenant configuration, attempt to trace or trigger use of one tenant's provider credential from a process scoped to a different tenant.
```

## G08-SALE_GELATO-Q039

```yaml
QID: G08-SALE_GELATO-Q039
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The cost the external on-demand production and fulfilment provider charges for a specific order is recorded, in your own accounting, against the same company that owned the customer sale, rather than landing against a different company's books or an unattributed default.
WHY_IT_MATTERS: >
  A misattributed cost overstates one company's margin and understates another's, corrupting the financial picture of both in a multi-company structure.
DISCONFIRMING_OBSERVATION: >
  The provider's cost for an order sold under one company is recorded in the accounts of a different company, or in no company's accounts at all.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete an order under a specific company in a multi-company setup and trace which company's accounts the provider's resulting cost is recorded against.
```

## G08-SALE_GELATO-Q040

```yaml
QID: G08-SALE_GELATO-Q040
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a company's credential with the external on-demand production and fulfilment provider is revoked or expires while orders under that company are still open, those in-flight orders are surfaced as an exception requiring attention rather than silently failing with no visible cause.
WHY_IT_MATTERS: >
  A credential failure that produces no visible signal leaves staff unable to explain why open orders under that company have stopped progressing.
DISCONFIRMING_OBSERVATION: >
  Orders under a company whose provider credential has been revoked remain in a normal in-progress status with no exception or notice raised anywhere.
EXPECTED_SURFACE: S1,S5,S6,S7
PRECONDITIONS: >
  Revoke or expire a company's provider credential while it has open orders, and observe what, if anything, is surfaced about those orders afterward.
```

## G08-SALE_GELATO-Q041

```yaml
QID: G08-SALE_GELATO-Q041
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A periodic invoice received from the external on-demand production and fulfilment provider can be reconciled, order by order, against the specific transactions it is billing for, rather than arriving as a total figure with no traceable link back to individual orders.
WHY_IT_MATTERS: >
  Without a line-by-line link, the business has no way to verify that it is being billed correctly, or to catch a provider billing error before paying it.
DISCONFIRMING_OBSERVATION: >
  A provider invoice's total cannot be broken down or matched against the individual orders it is meant to cover, leaving no way to confirm it is correct.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Receive a periodic invoice from the provider covering a known set of orders, and attempt to reconcile its line items or total against those specific orders.
```

## G08-SALE_GELATO-Q042

```yaml
QID: G08-SALE_GELATO-Q042
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An invoice line from the external on-demand production and fulfilment provider that references an order which was already cancelled, or does not exist, on your side is surfaced as a discrepancy requiring resolution, rather than being accepted and paid without any check against your own order records.
WHY_IT_MATTERS: >
  Paying for orders that were cancelled or never existed on your side is a direct, avoidable financial loss with no other safeguard catching it.
DISCONFIRMING_OBSERVATION: >
  An invoice line referencing a cancelled or nonexistent order is processed for payment with no discrepancy flagged anywhere.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Introduce a provider invoice line referencing an order that was cancelled or does not exist on your side, and observe whether the mismatch is caught before payment.
```

## G08-SALE_GELATO-Q043

```yaml
QID: G08-SALE_GELATO-Q043
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external on-demand production and fulfilment provider's charge for an order and the customer's own invoice for that same order fall into different accounting periods, the cost and the revenue are still matched to each other for that transaction's margin, rather than each landing in whichever period its own document happened to arrive in.
WHY_IT_MATTERS: >
  Unmatched timing between the provider's cost and the customer's revenue misstates the margin of both accounting periods involved.
DISCONFIRMING_OBSERVATION: >
  The revenue and the provider's cost for the same order are recognised in two different accounting periods with no mechanism matching them to each other for margin purposes.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Arrange for a provider charge and the corresponding customer invoice for the same order to fall into different accounting periods, and trace how the margin for that order is calculated.
```

## G08-SALE_GELATO-Q044

```yaml
QID: G08-SALE_GELATO-Q044
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The outcome of reconciling an invoice from the external on-demand production and fulfilment provider against your own orders — whether it matched cleanly, showed a mismatch, or was disputed — is itself retained as a retrievable record, rather than only the final payment action being visible with the reconciliation work behind it lost.
WHY_IT_MATTERS: >
  Without a retained reconciliation record, a later question about why a particular invoice was or was not disputed has no answer.
DISCONFIRMING_OBSERVATION: >
  A provider invoice that was reconciled and found to contain a mismatch shows no retrievable record of that finding once the invoice itself has been processed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reconcile a provider invoice with a known mismatch, then attempt to retrieve a record of that reconciliation outcome afterward.
```

## G08-SALE_GELATO-Q045

```yaml
QID: G08-SALE_GELATO-Q045
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Only the customer information the external on-demand production and fulfilment provider actually needs to produce and ship the order — such as the delivery address and the order's own content — is transmitted to it, rather than the full customer record being disclosed regardless of whether the provider needs it.
WHY_IT_MATTERS: >
  Disclosing more customer data than a third party needs to fulfil an order is an avoidable privacy exposure with no business purpose behind the extra disclosure.
DISCONFIRMING_OBSERVATION: >
  Customer information unrelated to producing or shipping the specific order — such as unrelated order history or contact details never needed by the provider — is found to be transmitted to it.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trace exactly what customer data is transmitted to the provider for a given order and compare it against what is actually necessary to produce and ship that order.
```

## G08-SALE_GELATO-Q046

```yaml
QID: G08-SALE_GELATO-Q046
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The disclosure of a customer's address to the external on-demand production and fulfilment provider is tied to a documented basis connected to fulfilling that customer's own order, rather than existing as an undocumented default with no stated justification anyone in the business could point to.
WHY_IT_MATTERS: >
  An undocumented basis for disclosing personal data to a third party leaves the business unable to answer a customer or a regulator who asks why that disclosure happened.
DISCONFIRMING_OBSERVATION: >
  Nobody and nothing in the system can point to a documented basis for why the customer's address is disclosed to the provider.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Ask what documented basis governs disclosing the customer's address to the provider and check whether one exists and is retrievable.
```

## G08-SALE_GELATO-Q047

```yaml
QID: G08-SALE_GELATO-Q047
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A customer request to delete their data, made after their order's details have already been sent to the external on-demand production and fulfilment provider, is recognised as only partially actionable and is recorded as such, rather than being processed as if it could fully retract information already outside your own systems.
WHY_IT_MATTERS: >
  Treating a post-disclosure deletion request as though it fully succeeds gives the business and the customer a false sense that data already sent to a third party has actually been recalled.
DISCONFIRMING_OBSERVATION: >
  A data deletion request made after order details were sent to the provider is marked fully completed with no record of the limitation that the provider's own copy is outside your control.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit a data deletion request for a customer whose order has already been sent to the provider, and check how the request's outcome and limitations are recorded.
```

## G08-SALE_GELATO-Q048

```yaml
QID: G08-SALE_GELATO-Q048
MODULE: sale_gelato
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The address transmitted to the external on-demand production and fulfilment provider for a given order is the address that applied to that order at the time it was sent, and is not silently replaced by a later change to the customer's account-level address after the order has already been sent.
WHY_IT_MATTERS: >
  If a later account-level address change could retroactively alter what was already sent to the provider, an order already in production could end up shipping to the wrong address with the record showing the new one as if it had always been correct.
DISCONFIRMING_OBSERVATION: >
  A customer's account-level address is changed after an order has been sent to the provider, and the order's own record of the address sent for that order changes to match the new one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send an order to the provider, then change the customer's account-level address, and check whether the order's own retained record of the address sent is affected.
```
