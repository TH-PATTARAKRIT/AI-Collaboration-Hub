# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / delivery Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-DELIVERY-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `delivery`
**Wave:** W2
**Author Cell:** TEAM P-S2 (GMVQ Question Factory — Production Cell P-S2, Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This is one of the four base capabilities of G08 SALES and receives the deep treatment the Group Brief
reserves for base modules. Its ground is shipping method and cost ON THE COMMERCIAL DOCUMENT: how a
shipping charge is determined at quotation time, how it is presented, taxed, split, reduced, corrected and
refunded on the sales side. It is distinct from G05 INVENTORY's `stock_delivery`, which owns the physical
movement seam (carrier booking, labels, tracking, parcel-level state, carrier feed reconciliation). This
bank deliberately does not re-ask any of `stock_delivery`'s questions; where the same real-world fact
(for example, a variance between quoted and actual carrier cost) is touched, this bank asks only about its
consequence on the commercial document and the customer-facing communication of it, never about the
internal shipment record.

Questions cover: the rate basis at quotation and its behaviour when the underlying order changes; the
free-shipping threshold's evaluation basis relative to discounts; the shipping line as a tax subject; the
customer-facing consequence of a cost correction; a method losing availability between quotation and
confirmation; one charge against several shipments; partial cancellation and partial return; multi-currency
and multi-company scoping; manual override and its permission and audit trail; precedence against
customer-specific terms; quotation validity; the boundary between a price-list-level promotion and a
separately issued reward; and the general negative, configuration and concurrency cases a commercial
charge must survive.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, cross-module dependency, auditability, tenant/company boundary,
  concurrency and ordering, and runtime/configuration reachability.
- This module carries both a configuration layer (rate basis, tax rule, per-company scoping, promotion and
  term precedence) and a runtime process layer (recomputation, cancellation, return, override); each
  question is tagged `LAYER: BASE` or `LAYER: PROCESS` accordingly.
- Pre-authoring sibling check (Bridge Module Rule §5): `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G05_INVENTORY/*.md`
  and, specifically, the full HYPOTHESIS set of `G05_STOCK_DELIVERY_GMVQ_MVQ_48_V1.00_DRAFT.md`, were read
  before authoring, to keep this bank off that module's ground (carrier booking, labels, tracking, parcel
  state, carrier-feed reconciliation, per-shipment period accounting). No G08 SALES bank existed on disk at
  authoring time, so there were no G08 siblings to check.
- This module is a base module, not a bridge, per the G08 Group Brief; it is authored for full depth on its
  own ground rather than restricted to seam-only questions. `sale_loyalty_delivery` (also authored in this
  batch) is the bridge that asks what happens to this module's charge when a loyalty reward pays for it;
  this bank does not pre-empt those questions and this module's own reward-free ground is kept separate.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-DELIVERY-Q001

```yaml
QID: G08-DELIVERY-Q001
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The shipping charge shown on a quotation is computed from the specific weight, volume, value or
  destination of the lines quoted at that moment, not from a fixed default that ignores what is actually
  being quoted.
WHY_IT_MATTERS: >
  A charge that ignores the real basis produces systematically wrong quotes, either under-recovering
  shipping cost across many orders or overcharging customers on light or local orders.
DISCONFIRMING_OBSERVATION: >
  Two quotations built with materially different weight, volume, value or destination on their lines
  produce the identical shipping charge with no computation basis shown.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Build two quotations for the same shipping method with deliberately different line weight, volume,
  value or destination and compare the computed charge.
```

## G08-DELIVERY-Q002

```yaml
QID: G08-DELIVERY-Q002
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When the goods on an order change after the shipping charge was first computed but before the order is
  confirmed, the charge is recomputed against the new lines rather than carried forward from the original
  computation.
WHY_IT_MATTERS: >
  A stale charge left over from an earlier version of the order either under-recovers cost when the order
  grew or overcharges the customer when it shrank, and neither is visible without a recompute.
DISCONFIRMING_OBSERVATION: >
  Lines are added or removed on a quotation after the shipping charge was first computed, and the charge
  shown afterward is identical to the original, un-updated figure.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Compute a shipping charge on a quotation with an initial set of lines, then materially add or remove
  lines and re-open the charge without invoking any explicit recompute action.
```

## G08-DELIVERY-Q003

```yaml
QID: G08-DELIVERY-Q003
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The charge that was computed and agreed at quotation is distinguishable, on the confirmed order, from a
  charge that would be computed if the same order were quoted fresh today, so a change to the underlying
  rate basis after confirmation does not silently rewrite what the customer already agreed to.
WHY_IT_MATTERS: >
  If confirmation does not freeze the charge, a rate table update made for unrelated reasons could
  retroactively change what a customer is billed for an order they already committed to.
DISCONFIRMING_OBSERVATION: >
  After an order is confirmed, changing the underlying rate basis (for example a general rate table)
  causes the already-confirmed order's shipping charge to change without any explicit action on that
  order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm an order with a computed shipping charge, then alter the general rate basis the charge was
  computed from, and re-open the confirmed order.
```

## G08-DELIVERY-Q004

```yaml
QID: G08-DELIVERY-Q004
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Whether a free-shipping threshold is evaluated against the order's value before or after line discounts
  are applied is a defined, consistent rule, not a behaviour that differs depending on which discount
  mechanism produced the reduction.
WHY_IT_MATTERS: >
  An inconsistent basis lets two orders of identical net value qualify for free shipping differently
  depending on how their discount was applied, which is unexplainable to a customer.
DISCONFIRMING_OBSERVATION: >
  Two orders with an identical final payable value, one discounted through one mechanism and one through
  another, are evaluated differently against the same free-shipping threshold.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Construct two orders that reach the same net value through different discounting paths, both near a
  configured free-shipping threshold, and compare whether each qualifies.
```

## G08-DELIVERY-Q005

```yaml
QID: G08-DELIVERY-Q005
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A free-shipping threshold is evaluated against a defined basis (for example merchandise value before or
  after tax) that is documented and applied the same way every time, rather than silently including or
  excluding the shipping charge itself in its own qualifying total.
WHY_IT_MATTERS: >
  If the shipping charge counts toward its own waiver threshold inconsistently, the qualifying point moves
  in a way nobody configured on purpose.
DISCONFIRMING_OBSERVATION: >
  An order's qualification for a free-shipping threshold changes state purely because the shipping charge
  itself was added to or removed from the order, with the underlying merchandise value unchanged.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Build an order at the threshold boundary, then add or remove only the shipping charge line, and check
  for a change in qualification without any line-value change.
```

## G08-DELIVERY-Q006

```yaml
QID: G08-DELIVERY-Q006
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order that qualifies for a free-shipping threshold at quotation time but no longer qualifies once
  lines are removed before confirmation loses the waiver rather than retaining it as a stale grant.
WHY_IT_MATTERS: >
  An unrevoked waiver on an order that no longer earns it is an unrecovered cost repeated across every
  order edited downward before confirmation.
DISCONFIRMING_OBSERVATION: >
  Lines are removed from a quotation, dropping its value below the free-shipping threshold, and the
  waived shipping charge remains at zero with no re-evaluation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Qualify a quotation for free shipping, then remove lines to bring it below the threshold, and re-open
  the shipping charge.
```

## G08-DELIVERY-Q007

```yaml
QID: G08-DELIVERY-Q007
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  The shipping charge is treated as its own taxable line with a determinable tax rate, rather than being
  silently excluded from tax computation or defaulting to no tax without a stated rule.
WHY_IT_MATTERS: >
  An untaxed or wrongly taxed shipping line is a tax compliance exposure that accumulates silently across
  every order with a shipping charge.
DISCONFIRMING_OBSERVATION: >
  An order containing a nonzero shipping charge shows no tax rate at all against that line, with no
  configuration marking it deliberately tax-exempt.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create an order with a taxable shipping charge on a jurisdiction/tax setup that taxes goods, and inspect
  the tax rate applied to the shipping line specifically.
```

## G08-DELIVERY-Q008

```yaml
QID: G08-DELIVERY-Q008
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  The tax rate applied to the shipping charge follows a defined, configurable rule for how it relates to
  the tax treatment of the goods on the order, rather than an unexplained default.
WHY_IT_MATTERS: >
  An order mixing goods taxed at different rates needs a defensible, consistent answer for what rate
  governs the shipping line, or the tax filing built from it is unreliable.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical orders, differing only in which goods tax rate is predominant among their
  lines, produce a shipping-line tax rate that cannot be traced to any configured rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Build two orders with different predominant goods tax rates but the same shipping charge, and compare
  the tax rate the shipping line receives against the configured rule.
```

## G08-DELIVERY-Q009

```yaml
QID: G08-DELIVERY-Q009
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing the tax treatment of the goods on an order after the shipping charge and its tax were first
  computed triggers a re-evaluation of the shipping line's own tax, rather than leaving it fixed to
  whatever was computed first.
WHY_IT_MATTERS: >
  A stale shipping-line tax rate left over from an earlier tax configuration produces a tax figure that no
  longer matches the rule in force, which is a discrepancy at filing time.
DISCONFIRMING_OBSERVATION: >
  The tax configuration governing the order's goods is changed after the shipping charge's tax was first
  computed, and the shipping line's tax rate is unchanged when the order is reopened.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compute a shipping charge and its tax on an order, then change the applicable tax configuration for the
  goods, and re-open the order.
```

## G08-DELIVERY-Q010

```yaml
QID: G08-DELIVERY-Q010
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The shipping amount stated to the customer on the order or invoice is a fixed, agreed figure once
  communicated, and a later-discovered difference against the actual cost of fulfilling it does not
  silently alter what was already presented to the customer.
WHY_IT_MATTERS: >
  A commercial document whose stated charge moves on its own after the fact undermines the customer's
  trust, independent of who ultimately absorbs the internal cost difference.
DISCONFIRMING_OBSERVATION: >
  The shipping figure on an already-issued invoice or confirmed order changes value with no new invoice
  line, credit note or explicit customer-facing document recording the change.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Issue an invoice carrying a shipping charge, then supply a different actual fulfilment cost for the
  same order, and re-open the original invoice.
```

## G08-DELIVERY-Q011

```yaml
QID: G08-DELIVERY-Q011
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a later-discovered shipping cost difference is passed on to the customer at all, it appears as a
  distinct, identifiable additional line or credit note on the commercial document, not as a silent edit
  to the original shipping line's amount.
WHY_IT_MATTERS: >
  A customer-facing correction that cannot be told apart from the original charge removes the audit trail
  a customer or an auditor would need to understand what changed and why.
DISCONFIRMING_OBSERVATION: >
  A shipping cost correction reaches the customer as a rewritten value on the original line, with no
  separate line, note or document identifying it as a correction.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a shipping cost correction that is passed to the customer, and inspect whether it appears as its
  own identifiable entry or as an edit to the original line.
```

## G08-DELIVERY-Q012

```yaml
QID: G08-DELIVERY-Q012
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a shipping cost difference is ever passed on to the customer at all, versus always absorbed
  internally, is a defined business rule reflected consistently on the commercial document, not a decision
  made ad hoc per order with no configured basis.
WHY_IT_MATTERS: >
  An ad hoc pass-on decision applied inconsistently across customers is both a fairness exposure and
  something no policy could defend if questioned.
DISCONFIRMING_OBSERVATION: >
  Two orders with an equivalent shipping cost shortfall, under the same configuration, are resolved
  differently on their commercial documents with no order-specific reason recorded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reproduce an equivalent shipping cost shortfall on two comparable orders under identical configuration
  and compare how each is resolved on its commercial document.
```

## G08-DELIVERY-Q013

```yaml
QID: G08-DELIVERY-Q013
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A shipping method selected at quotation that has since become unavailable for the order's destination is
  caught and flagged before or at confirmation, rather than allowed to confirm silently with a method that
  cannot actually be fulfilled.
WHY_IT_MATTERS: >
  An order confirmed with a dead method reaches fulfilment only to fail there, after the customer has
  already been told their order is confirmed.
DISCONFIRMING_OBSERVATION: >
  An order confirms successfully carrying a shipping method that is, at the moment of confirmation, no
  longer configured as available for that destination, with no warning raised.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Quote an order with a shipping method available for its destination, remove that method's availability
  for the destination, then attempt to confirm the order.
```

## G08-DELIVERY-Q014

```yaml
QID: G08-DELIVERY-Q014
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a previously selected shipping method becomes unavailable before confirmation, the commercial
  document offers a defined resolution path (an alternative method, or an explicit hold) rather than
  leaving the order unconfirmable with no indication of why.
WHY_IT_MATTERS: >
  A silent dead end at confirmation, with no guidance on what to do next, stalls the order and pushes the
  customer to the same discovery a second time.
DISCONFIRMING_OBSERVATION: >
  Confirmation of an order with a now-unavailable shipping method fails with no indication of which method
  is at fault or what alternatives exist.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Reproduce a method-unavailable-at-confirmation state and inspect what the order presents as the next
  step.
```

## G08-DELIVERY-Q015

```yaml
QID: G08-DELIVERY-Q015
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A shipping method's availability for a given destination is a configuration fact that can be checked
  independently of any specific order, so that whether a method would be rejected at confirmation is
  knowable in advance rather than only discoverable by attempting to confirm.
WHY_IT_MATTERS: >
  Without an independently checkable availability fact, diagnosing why a batch of orders is failing to
  confirm requires reproducing the failure order by order.
DISCONFIRMING_OBSERVATION: >
  There is no way to determine, other than by attempting confirmation, whether a given shipping method is
  currently available for a given destination.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt to determine a shipping method's availability for a specific destination through configuration
  alone, without creating or confirming an order.
```

## G08-DELIVERY-Q016

```yaml
QID: G08-DELIVERY-Q016
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When one order's shipping charge is quoted as a single figure but its goods are ultimately sent out in
  several shipments, the commercial document still reflects one coherent charge whose relationship to each
  shipment is traceable, rather than the original figure becoming meaningless once fulfilment splits.
WHY_IT_MATTERS: >
  A charge that cannot be related to how the order was actually fulfilled cannot be checked, disputed or
  explained to the customer.
DISCONFIRMING_OBSERVATION: >
  An order's goods are sent out in multiple shipments and the single quoted shipping charge has no
  recorded relationship to either shipment, or to the split itself.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Quote an order with one shipping charge, fulfil it in more than one shipment, and inspect what the
  charge's record shows about that split.
```
## G08-DELIVERY-Q017

```yaml
QID: G08-DELIVERY-Q017
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Splitting one order's fulfilment into several shipments does not, on its own, multiply the single
  quoted shipping charge into several full charges on the commercial document.
WHY_IT_MATTERS: >
  A charge that duplicates itself per shipment purely because fulfilment happened to split overcharges the
  customer for a single quoted service.
DISCONFIRMING_OBSERVATION: >
  An order quoted with one shipping charge shows that charge's full amount billed more than once after its
  fulfilment is split into multiple shipments.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Quote an order with one shipping charge, split its fulfilment into multiple shipments, and inspect the
  total shipping amount billed to the customer.
```

## G08-DELIVERY-Q018

```yaml
QID: G08-DELIVERY-Q018
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether an order that will foreseeably ship in multiple parts is charged as one combined shipping figure
  or as a charge per part is a defined, configurable business rule, rather than being decided implicitly
  by however fulfilment happens to unfold.
WHY_IT_MATTERS: >
  Without a stated rule, the customer-facing charge for a multi-part order is unpredictable from one order
  to the next, and cannot be explained if questioned.
DISCONFIRMING_OBSERVATION: >
  Two orders known in advance to require multiple shipments, otherwise comparable, are charged shipping
  under two different bases with no configuration distinguishing them.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Construct two comparable orders both known to require multiple shipments and compare how each is
  charged under the same configuration.
```

## G08-DELIVERY-Q019

```yaml
QID: G08-DELIVERY-Q019
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When part of an order is cancelled before fulfilment, the shipping charge already quoted is re-evaluated
  against what remains, rather than staying fixed at the figure computed for the original, larger order.
WHY_IT_MATTERS: >
  A shipping charge left over from a cancelled portion of the order either overcharges the customer for
  goods they are no longer receiving, or leaves an under-recovered charge invisible to review.
DISCONFIRMING_OBSERVATION: >
  A material portion of an order's lines is cancelled before fulfilment, and the shipping charge shown
  afterward is identical to the figure computed for the original, uncancelled order.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Quote an order's shipping charge against its full line set, cancel a material portion of those lines
  before fulfilment, and re-open the shipping charge.
```

## G08-DELIVERY-Q020

```yaml
QID: G08-DELIVERY-Q020
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a partial cancellation re-evaluates the shipping charge from scratch or simply prorates the
  original figure is a defined, consistent rule, not a behaviour that varies by which lines happen to be
  cancelled.
WHY_IT_MATTERS: >
  An unstated, inconsistent recomputation basis means the resulting charge cannot be predicted or defended
  for any given partial cancellation.
DISCONFIRMING_OBSERVATION: >
  Two partial cancellations that remove an equivalent proportion of value from otherwise comparable orders
  leave two different shipping charges with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Perform two comparable partial cancellations, removing an equivalent proportion of order value each
  time, and compare the resulting shipping charges.
```

## G08-DELIVERY-Q021

```yaml
QID: G08-DELIVERY-Q021
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping waiver granted on the full order is re-evaluated if a partial cancellation drops the
  remaining order below the qualifying threshold, rather than the waiver surviving on a remainder that
  would not itself have qualified.
WHY_IT_MATTERS: >
  An unrevoked waiver surviving a downward cancellation is an unrecovered cost that recurs every time an
  order is cancelled down past the threshold.
DISCONFIRMING_OBSERVATION: >
  An order granted free shipping is partially cancelled to below the qualifying threshold, and the waiver
  remains in effect on what is left.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Qualify an order for free shipping, partially cancel it to below the threshold, and re-open the shipping
  charge.
```

## G08-DELIVERY-Q022

```yaml
QID: G08-DELIVERY-Q022
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether the original shipping charge is refunded, in full or in part, when goods on the order are
  returned is a defined, configurable business rule reflected on the credit note, not an unstated default
  that differs by who processes the return.
WHY_IT_MATTERS: >
  An unstated refund rule means two operators handling equivalent returns could produce two different
  customer outcomes with no policy to point to.
DISCONFIRMING_OBSERVATION: >
  Two equivalent full returns of otherwise identical orders, processed under the same configuration, are
  refunded the shipping charge differently with no order-specific reason recorded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Process two equivalent full returns under the same configuration and compare whether and how the
  shipping charge is refunded on each.
```

## G08-DELIVERY-Q023

```yaml
QID: G08-DELIVERY-Q023
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A partial return of an order's goods re-evaluates whether the original shipping charge (or a portion of
  it) is still refundable, rather than an all-or-nothing rule that either always keeps or always returns
  the full shipping amount regardless of how much of the order came back.
WHY_IT_MATTERS: >
  An all-or-nothing rule applied to a partial return either denies a reasonable partial shipping refund or
  grants a full refund for goods that were only partly returned.
DISCONFIRMING_OBSERVATION: >
  A partial return of an order's lines produces a shipping refund outcome that does not vary regardless of
  how large a proportion of the order was actually returned.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Process partial returns of differing proportions on comparable orders and compare the shipping refund
  outcome each produces.
```

## G08-DELIVERY-Q024

```yaml
QID: G08-DELIVERY-Q024
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A shipping charge refunded on a return is recorded on the credit note as its own identifiable line,
  distinguishable from the refund of the returned goods themselves, rather than folded invisibly into a
  single combined figure.
WHY_IT_MATTERS: >
  A combined figure that cannot be decomposed into goods and shipping components cannot be checked against
  the return that was actually processed, or reconciled against the earlier charge.
DISCONFIRMING_OBSERVATION: >
  A credit note issued for a return that includes a shipping refund shows only one combined total, with no
  identifiable shipping component.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Process a return that includes a shipping refund and inspect the resulting credit note's line-level
  detail.
```

## G08-DELIVERY-Q025

```yaml
QID: G08-DELIVERY-Q025
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A shipping charge computed for an order in a currency other than the business's own reporting currency
  is recorded in both the order's currency and a determinable reporting-currency equivalent, rather than
  existing only in whichever currency the order happened to be raised in.
WHY_IT_MATTERS: >
  A charge visible in only one currency cannot be rolled up or compared against charges from orders in
  other currencies for any cross-order reporting.
DISCONFIRMING_OBSERVATION: >
  An order raised in a foreign currency carries a shipping charge with no determinable equivalent in the
  business's own reporting currency.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Raise an order in a currency other than the reporting currency, compute its shipping charge, and inspect
  whether a reporting-currency equivalent is available.
```

## G08-DELIVERY-Q026

```yaml
QID: G08-DELIVERY-Q026
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Shipping method and rate configuration can be scoped independently per company, so that one company's
  shipping charge rules are not silently applied to an order raised under a different company.
WHY_IT_MATTERS: >
  A shared configuration where one company cannot control its own shipping rules removes a legitimate
  business boundary and can misstate the charge a given company's customers are shown.
DISCONFIRMING_OBSERVATION: >
  An order raised under one company computes its shipping charge from a rate configuration that belongs to
  a different company, with no company-scoped configuration available.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure distinct shipping rate rules under two different companies and raise an order under each to
  confirm which configuration governs.
```

## G08-DELIVERY-Q027

```yaml
QID: G08-DELIVERY-Q027
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A user without visibility into a given company's orders cannot reach that company's shipping rate
  configuration or charge figures through a cross-company view that was not intended to expose it.
WHY_IT_MATTERS: >
  A leaked cross-company view of pricing rules is a confidentiality exposure between what may be
  commercially distinct business units sharing one system.
DISCONFIRMING_OBSERVATION: >
  A user restricted from one company's orders can nonetheless view or derive that company's shipping rate
  configuration through a report, lookup, or shared reference not scoped by company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user restricted to one company, attempt to reach another company's shipping rate configuration
  through any available report or shared reference.
```

## G08-DELIVERY-Q028

```yaml
QID: G08-DELIVERY-Q028
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Overriding a system-computed shipping charge with a manually entered figure is a distinct, logged
  action, not indistinguishable, once saved, from a figure the system computed on its own.
WHY_IT_MATTERS: >
  An override that cannot be told apart from a computed figure removes any ability to audit why a
  particular order's charge does not match what the configured rule would produce.
DISCONFIRMING_OBSERVATION: >
  A manually overridden shipping charge, once saved, shows no trace distinguishing it from a
  system-computed figure of the same value.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Override a computed shipping charge with a manual figure, save the order, and inspect whether the
  override is identifiable as such.
```

## G08-DELIVERY-Q029

```yaml
QID: G08-DELIVERY-Q029
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The ability to manually override a computed shipping charge is governed by a distinct permission from
  the permission needed merely to create or confirm an order, rather than being available to anyone who
  can touch the order at all.
WHY_IT_MATTERS: >
  Unrestricted override ability lets any order-taker discount shipping at will with no accountability
  distinct from ordinary order handling.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary order-creation permission is able to manually override a computed shipping
  charge with no separate permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user holding only ordinary order-creation permission, attempt to override a computed shipping
  charge.
```

## G08-DELIVERY-Q030

```yaml
QID: G08-DELIVERY-Q030
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A manually overridden shipping charge on a quotation is not silently discarded and replaced by a fresh
  system computation if the order is later re-opened or its lines are touched again, unless the override
  is explicitly cleared.
WHY_IT_MATTERS: >
  An override that reverts on its own undermines the very reason it was entered, and the person who set it
  has no way to know it was lost.
DISCONFIRMING_OBSERVATION: >
  A manually overridden shipping charge reverts to a freshly computed figure after the order is merely
  re-opened or an unrelated line is edited, with no explicit action to clear the override.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Manually override a shipping charge, then re-open the order or edit an unrelated line, and check whether
  the override persists.
```

## G08-DELIVERY-Q031

```yaml
QID: G08-DELIVERY-Q031
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where a price list or customer-specific agreement includes its own shipping term, that term takes
  precedence over the general rate computation in a defined, consistent order, rather than the two
  competing with an unpredictable winner.
WHY_IT_MATTERS: >
  An unpredictable precedence between a negotiated customer term and the general rate produces a charge
  that cannot be defended against what was actually agreed with that customer.
DISCONFIRMING_OBSERVATION: >
  Two orders for the same customer holding a specific shipping term, differing only in unrelated details,
  resolve the precedence between that term and the general rate differently.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Assign a customer a specific shipping term through a price list or agreement, raise more than one order
  for that customer, and compare how each resolves the charge.
```

## G08-DELIVERY-Q032

```yaml
QID: G08-DELIVERY-Q032
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A customer-specific shipping term that has expired or been superseded no longer applies to a new order
  raised after its validity ends, rather than continuing to be honoured because it once applied to that
  customer.
WHY_IT_MATTERS: >
  An expired term that keeps applying is a rate the business no longer intends to offer, silently costing
  margin on every subsequent order for that customer.
DISCONFIRMING_OBSERVATION: >
  An order raised after a customer's specific shipping term has expired still receives that term's rate
  rather than the current general rate.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Let a customer-specific shipping term expire, then raise a new order for that customer and inspect which
  rate applies.
```
## G08-DELIVERY-Q033

```yaml
QID: G08-DELIVERY-Q033
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  When more than one price list or agreement could plausibly supply a shipping term for the same order,
  exactly one governs and which one is a traceable, documented decision, not an unexplained pick among
  candidates.
WHY_IT_MATTERS: >
  An untraceable pick among competing candidates means the resulting charge cannot be explained if the
  customer or an auditor asks why that rate applied.
DISCONFIRMING_OBSERVATION: >
  An order eligible under more than one shipping term shows a resulting charge with no record of which
  term was actually applied or why.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct an order eligible under more than one candidate shipping term and inspect what the order
  records about which one governed.
```

## G08-DELIVERY-Q034

```yaml
QID: G08-DELIVERY-Q034
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A shipping charge computed on a quotation that has since exceeded its own stated validity period is
  flagged for recomputation before the quotation can be confirmed, rather than confirming silently on a
  charge computed under conditions that may no longer hold.
WHY_IT_MATTERS: >
  A charge carried past its own valid window may no longer reflect current rates, and confirming it
  without notice locks in a figure nobody re-checked.
DISCONFIRMING_OBSERVATION: >
  A quotation confirms past its own stated validity period carrying its original shipping charge with no
  flag or recomputation step.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Let a quotation's stated validity period lapse, then attempt to confirm it and observe whether the
  shipping charge is flagged.
```

## G08-DELIVERY-Q035

```yaml
QID: G08-DELIVERY-Q035
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Requoting an order after its shipping charge basis has changed produces a distinguishable new figure
  alongside a trace of what the previous figure was, rather than the previous figure disappearing without
  record once replaced.
WHY_IT_MATTERS: >
  Losing the prior figure removes the ability to show a customer, or an internal reviewer, what changed
  and why between versions of the same quotation.
DISCONFIRMING_OBSERVATION: >
  A quotation is requoted with a changed shipping charge and no trace of the earlier figure remains
  accessible anywhere on the order's own record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Requote an order after changing its shipping charge basis and inspect whether the earlier figure remains
  traceable.
```

## G08-DELIVERY-Q036

```yaml
QID: G08-DELIVERY-Q036
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A shipping charge validity period, where configured, is itself a per-method or per-configuration setting
  rather than a single fixed rule applied uniformly regardless of which shipping method or rate basis is
  in play.
WHY_IT_MATTERS: >
  A uniform validity period applied to methods with genuinely different rate volatility either expires
  stable rates needlessly often or leaves volatile ones unchecked for too long.
DISCONFIRMING_OBSERVATION: >
  Two shipping methods with materially different underlying rate volatility are both governed by an
  identical validity period with no configuration distinguishing them.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Inspect the validity period configuration available for two shipping methods with different rate
  characteristics.
```

## G08-DELIVERY-Q037

```yaml
QID: G08-DELIVERY-Q037
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A free-shipping promotion configured at the price list or customer-group level is a distinct
  configuration object from a reward or coupon issued through a separate programme, so the two mechanisms
  can be told apart on an order that happens to qualify for both.
WHY_IT_MATTERS: >
  If the two mechanisms are indistinguishable once applied, resolving which one is responsible for a
  waived charge, or withdrawing one without affecting the other, becomes impossible.
DISCONFIRMING_OBSERVATION: >
  An order qualifying for both a price-list-level free-shipping promotion and a separately issued reward
  shows a single waived charge with no way to tell which mechanism produced it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Configure an order to qualify for both a price-list-level shipping promotion and a separate reward-based
  waiver, and inspect what the resulting charge record shows.
```

## G08-DELIVERY-Q038

```yaml
QID: G08-DELIVERY-Q038
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Ending a price-list-level free-shipping promotion does not retroactively change the charge already
  recorded on orders confirmed while the promotion was active.
WHY_IT_MATTERS: >
  A retroactive change to already-confirmed orders rewrites a commercial commitment the customer already
  relied on.
DISCONFIRMING_OBSERVATION: >
  Ending a price-list-level shipping promotion changes the shipping charge on orders that were already
  confirmed while it was active.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm orders while a price-list-level shipping promotion is active, end the promotion, and re-open
  those orders.
```

## G08-DELIVERY-Q039

```yaml
QID: G08-DELIVERY-Q039
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A price-list-level free-shipping promotion can be scoped to specific customer groups, destinations, or
  order channels rather than being an all-or-nothing setting applied identically to every order regardless
  of who or where it is for.
WHY_IT_MATTERS: >
  An unscoped promotion cannot deliver a targeted commercial offer and either costs more than intended or
  fails to reach the segment it was meant for.
DISCONFIRMING_OBSERVATION: >
  A price-list-level shipping promotion configured for a specific customer group or destination also
  applies to orders outside that group or destination.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a shipping promotion scoped to a specific customer group or destination, then raise an order
  outside that scope and check whether it still qualifies.
```

## G08-DELIVERY-Q040

```yaml
QID: G08-DELIVERY-Q040
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A history of every value a given order's shipping charge has held, whether computed or manually set,
  remains retrievable from the order's own record, rather than only the current value being visible.
WHY_IT_MATTERS: >
  Without a retrievable history, a dispute about what a customer was originally quoted versus what they
  were eventually charged cannot be resolved from the order itself.
DISCONFIRMING_OBSERVATION: >
  An order whose shipping charge has been changed more than once shows only its current value, with no
  earlier value retrievable from the order's own record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change an order's shipping charge more than once across its lifecycle and attempt to retrieve its
  earlier values from the order.
```

## G08-DELIVERY-Q041

```yaml
QID: G08-DELIVERY-Q041
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Attempting to compute a shipping charge for an order with no destination set, or a destination the
  configuration does not recognise, produces a visible exception rather than a silent zero or an arbitrary
  default charge.
WHY_IT_MATTERS: >
  A silent zero for an unrecognised destination looks like a legitimate free-shipping outcome and hides a
  data or configuration gap that should have been surfaced.
DISCONFIRMING_OBSERVATION: >
  An order with no destination set, or an unrecognised destination, computes a nonzero-looking-legitimate
  shipping charge with no exception or flag raised.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to compute a shipping charge for an order with a missing or unrecognised destination and observe
  the result.
```

## G08-DELIVERY-Q042

```yaml
QID: G08-DELIVERY-Q042
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two operators attempting to change the same order's shipping charge or method at effectively the same
  time result in exactly one change taking effect, rather than both succeeding and leaving the order in a
  state that reflects neither operator's actual intent.
WHY_IT_MATTERS: >
  A silently lost concurrent edit means one operator believes their change is in effect when it is not,
  with no indication anything was overwritten.
DISCONFIRMING_OBSERVATION: >
  Two concurrent edits to the same order's shipping charge or method both appear to succeed, but the saved
  order reflects a value that matches neither edit or silently discards one with no notice.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Simulate two near-simultaneous edits to the same order's shipping charge or method from two sessions and
  inspect the resulting saved state.
```

## G08-DELIVERY-Q043

```yaml
QID: G08-DELIVERY-Q043
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A shipping method that is configured but has been deliberately disabled is prevented from being selected
  on a new quotation, rather than remaining selectable while only failing later at confirmation or
  fulfilment.
WHY_IT_MATTERS: >
  Allowing a disabled method to be selected pushes the failure downstream to confirmation, after the
  customer has already been shown that option.
DISCONFIRMING_OBSERVATION: >
  A shipping method marked disabled in configuration can still be selected on a new quotation.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Disable a shipping method in configuration and attempt to select it on a new quotation.
```

## G08-DELIVERY-Q044

```yaml
QID: G08-DELIVERY-Q044
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Whether a given shipping method is offered to a customer depends on a defined set of eligibility rules
  (destination, order value, goods type) that are evaluated consistently, rather than the same order being
  offered a different set of methods depending on an unrelated factor such as which channel or interface
  raised it.
WHY_IT_MATTERS: >
  An inconsistency across channels means the same order could be quoted a different shipping charge purely
  because of how it was entered, which is not a defensible basis for pricing.
DISCONFIRMING_OBSERVATION: >
  An identical order raised through two different channels or interfaces is offered two different sets of
  shipping methods, with no eligibility rule accounting for the difference.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Raise an equivalent order through two different channels or interfaces and compare the shipping methods
  each is offered.
```

## G08-DELIVERY-Q045

```yaml
QID: G08-DELIVERY-Q045
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A shipping method configuration that is incomplete (missing a required rate basis for the method's own
  pricing model) is prevented from being offered on an order at all, rather than being offered and only
  failing to produce a usable charge once selected.
WHY_IT_MATTERS: >
  An incompletely configured method that reaches the customer as a selectable option, only to fail once
  chosen, is a broken experience that a configuration-time check would have prevented.
DISCONFIRMING_OBSERVATION: >
  A shipping method missing a rate basis required by its own pricing model is offered as selectable on an
  order and only fails, or produces no charge, after being selected.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Configure a shipping method with an incomplete rate basis for its pricing model and attempt to select it
  on an order.
```

## G08-DELIVERY-Q046

```yaml
QID: G08-DELIVERY-Q046
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Deleting or archiving a shipping method that is already referenced by existing confirmed orders does not
  remove or invalidate the charge already recorded on those orders, leaving them with an intact,
  explainable figure even though the method itself is no longer active.
WHY_IT_MATTERS: >
  A retired method that breaks historical orders' records makes past commercial documents unreadable or
  inexplicable after the fact.
DISCONFIRMING_OBSERVATION: >
  Archiving or deleting a shipping method causes existing confirmed orders that reference it to lose or
  corrupt their recorded shipping charge.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order under a given shipping method, then archive or delete that method, and re-open the
  confirmed order.
```

## G08-DELIVERY-Q047

```yaml
QID: G08-DELIVERY-Q047
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A shipping charge is not itself treated as a line eligible for its own further percentage-based line
  discount unless the configuration explicitly says so, so that a general order-wide discount rule does not
  silently apply itself to the shipping line as if it were merchandise.
WHY_IT_MATTERS: >
  An unintended discount silently applied to the shipping line understates recovered shipping cost across
  every discounted order without anyone configuring that outcome on purpose.
DISCONFIRMING_OBSERVATION: >
  A general order-wide percentage discount rule reduces the shipping charge line with no configuration
  explicitly including shipping in that discount's scope.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply a general order-wide percentage discount to an order carrying a shipping charge, under a
  configuration that does not explicitly include shipping, and inspect whether the shipping line was
  reduced.
```

## G08-DELIVERY-Q048

```yaml
QID: G08-DELIVERY-Q048
MODULE: delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A shipping charge line displayed to internal staff can show the underlying computation basis (rate basis
  and inputs used) on demand, distinguishing a charge that can be explained from one that is an opaque
  final figure only.
WHY_IT_MATTERS: >
  Staff who cannot see how a charge was derived cannot answer a customer's question about it, or diagnose
  it when it looks wrong, without escalating to a specialist every time.
DISCONFIRMING_OBSERVATION: >
  There is no way for an authorised internal user to see the computation basis behind a given order's
  shipping charge; only the final figure is ever visible.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  As an authorised internal user, attempt to see the computation basis behind a specific order's shipping
  charge.
```
