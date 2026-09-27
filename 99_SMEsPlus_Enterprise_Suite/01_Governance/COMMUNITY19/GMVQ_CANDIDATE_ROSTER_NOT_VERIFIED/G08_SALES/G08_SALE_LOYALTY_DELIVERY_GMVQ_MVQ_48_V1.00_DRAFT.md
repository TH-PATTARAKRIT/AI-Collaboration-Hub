# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_loyalty_delivery Module Adversarial MVQ Bank (BRIDGE OF A BRIDGE)

**Document ID:** GMVQ-G08-SALE_LOYALTY_DELIVERY-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_loyalty_delivery`
**Wave:** W2
**Author Cell:** TEAM P-S2 (GMVQ Question Factory — Production Cell P-S2, Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This is a BRIDGE of a bridge per the Bridge Module Rule (V1.00), narrower than `sale_loyalty`: it is the
three-way seam where a reward pays for SHIPPING SPECIFICALLY, requiring an order, a reward or coupon
targeting shipping, and the commercial shipping-charge computation to all exist together. A question
belongs here only if it survives none of the three simplifications: with the reward removed (then it is
`delivery`'s ground), with shipping removed and the reward acting on merchandise instead (then it is
`sale_loyalty`'s ground), or with the order removed (then there is nothing to apply anything to). Ground
covered: a free-shipping reward applied before the shipping charge is known; the charge changing after the
reward was applied; a reward covering only part of the charge and who pays the rest; free shipping on an
order later split into several shipments; a shipping-targeted reward's interaction with a general
free-shipping threshold the order also qualifies for (the double-benefit case); the reward's effect on a
return where shipping is not refundable; and tax on a shipping line reduced to zero by a reward.

This bank does not restate `delivery`'s ground (the commercial shipping charge computed and behaving on its
own, with no reward involved) or `sale_loyalty`'s ground (a reward's general interaction with an order's
lines, tax, margin, partial delivery/invoicing, or with a second competing reward, none of it
shipping-specific). Every question below requires all three legs of the seam simultaneously.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, exception path, cancellation,
  reversal, negative case, auditability, and ordering/timing.
- Bridge Module Rule §5 pre-authoring check: `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md` was run
  against `G08_DELIVERY_GMVQ_MVQ_48_V1.00_DRAFT.md`, `G08_LOYALTY_GMVQ_MVQ_48_V1.00_DRAFT.md` and
  `G08_SALE_LOYALTY_GMVQ_MVQ_48_V1.00_DRAFT.md`, all authored earlier in this same batch. No question below
  restates any of the three; each one requires the reward, the order and the shipping-charge computation to
  interact simultaneously, and none of it is `sale_loyalty`'s general-reward ground with the word "shipping"
  substituted in for a merchandise line — the shipping charge's own distinctive properties (computed by a
  separate module, potentially zero or absent, splittable across shipments, subject to its own
  non-refundable-by-default policy) are what each question actually turns on.
- Bridge-of-a-bridge test applied to every question: does it survive with the reward removed (delivery
  alone)? Does it survive with shipping removed and the reward acting on merchandise instead (sale_loyalty
  alone)? Every question below fails both simplifications.
- LAYER is mostly `PROCESS`; the handful of questions about configurable coverage or precedence rules are
  tagged `LAYER: BASE`.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_LOYALTY_DELIVERY-Q001

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q001
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping reward applied at a stage before the shipping method and its charge have been determined
  waives whatever charge is eventually computed, rather than waiving only a charge that already existed at
  the moment the reward was applied.
WHY_IT_MATTERS: >
  If the reward can only waive a charge that already exists, applying it before a method is chosen would
  silently fail to deliver the free-shipping benefit the customer was promised.
DISCONFIRMING_OBSERVATION: >
  A free-shipping reward applied before any shipping method is selected fails to waive the charge once a
  method is subsequently chosen and its charge computed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a free-shipping reward to an order before selecting a shipping method, then select a method and
  inspect whether its charge is waived.
```

## G08-SALE_LOYALTY_DELIVERY-Q002

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q002
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If no shipping method has yet been selected when a free-shipping reward is applied, the reward's effect
  is not silently lost once a method and its charge are chosen afterward.
WHY_IT_MATTERS: >
  A reward silently forgotten once its target finally exists costs the customer a benefit they were told
  applied, discovered only when they are unexpectedly charged for shipping.
DISCONFIRMING_OBSERVATION: >
  A free-shipping reward recorded as applied while no shipping method existed is no longer present or
  effective once a method is later added to the order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a free-shipping reward with no shipping method on the order yet, then add a method later and check
  whether the reward is still in effect.
```

## G08-SALE_LOYALTY_DELIVERY-Q003

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q003
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping reward applied before the charge is known does not prevent the underlying commercial
  shipping charge from still being computed and recorded at its full, undiscounted value, so the value the
  reward is waiving remains visible.
WHY_IT_MATTERS: >
  Without the full underlying charge on record, no one can later say how much the free-shipping reward was
  actually worth to the customer or cost the business.
DISCONFIRMING_OBSERVATION: >
  An order with a free-shipping reward applied shows no record of what the shipping charge would have been
  absent the reward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a free-shipping reward, allow the shipping charge to compute, and inspect whether the undiscounted
  figure remains on record.
```

## G08-SALE_LOYALTY_DELIVERY-Q004

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q004
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Selecting a different shipping method after a free-shipping reward was already applied does not require
  the reward to be re-applied manually; it continues to waive whatever charge the newly selected method
  produces.
WHY_IT_MATTERS: >
  A reward that must be manually re-applied after every method change is easy to forget, silently
  reinstating a charge the customer was told was waived.
DISCONFIRMING_OBSERVATION: >
  Changing the shipping method after a free-shipping reward was applied reinstates a charge for the newly
  selected method until the reward is manually re-applied.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a free-shipping reward, then change the selected shipping method, and inspect whether the new
  method's charge is still waived.
```

## G08-SALE_LOYALTY_DELIVERY-Q005

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q005
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping reward applied before the destination is finalised still resolves correctly once the
  destination is set, even where the destination affects which shipping methods, and therefore charges, are
  even available.
WHY_IT_MATTERS: >
  A reward that cannot follow a destination change into a different set of available methods leaves the
  customer uncovered the moment their delivery address is corrected or confirmed.
DISCONFIRMING_OBSERVATION: >
  Setting or changing the destination after a free-shipping reward was applied, in a way that changes which
  shipping methods are available, leaves the reward failing to cover the method eventually chosen.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a free-shipping reward before the destination is set, then set a destination that changes the
  available methods, and inspect the reward's coverage.
```

## G08-SALE_LOYALTY_DELIVERY-Q006

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q006
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  If the eventual shipping charge computation determines that no charge would have applied anyway, a
  destination with a genuinely free base rate, the reward's own record still shows that it was applied,
  rather than looking retroactively as though it was never needed.
WHY_IT_MATTERS: >
  If the reward's record disappears whenever it turns out to have been unnecessary, the customer's coupon or
  points could be reported as unused and available again despite having genuinely been consumed at the time.
DISCONFIRMING_OBSERVATION: >
  A free-shipping reward applied to an order that turns out to have a zero base shipping charge shows no
  record that the reward was ever applied.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a free-shipping reward to an order whose destination carries a genuinely free base shipping rate and
  inspect the reward's own record afterward.
```

## G08-SALE_LOYALTY_DELIVERY-Q007

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q007
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A free-shipping reward that requires a minimum order value evaluates that minimum against the order's own
  merchandise value, independent of whatever the shipping charge itself later turns out to be, so the
  shipping charge does not itself contribute to meeting its own waiver's threshold.
WHY_IT_MATTERS: >
  If the shipping charge could count toward its own waiver's qualifying minimum, the threshold becomes
  self-referential and easier to reach than the business intended.
DISCONFIRMING_OBSERVATION: >
  Adding a shipping charge to an order changes whether it meets a shipping-targeted reward's own minimum
  order value condition.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Build an order near a shipping-targeted reward's minimum value threshold and check whether adding the
  shipping charge itself changes qualification.
```

## G08-SALE_LOYALTY_DELIVERY-Q008

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q008
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When the underlying commercial shipping charge is recomputed after a free-shipping reward was applied,
  for example because the order's lines changed, the reward continues to waive the newly recomputed charge
  rather than being left waiving only the original, stale figure.
WHY_IT_MATTERS: >
  A reward stuck waiving a stale figure either leaves a new, larger charge partly unwaived and unexplained,
  or continues waiving a smaller figure than what is now due.
DISCONFIRMING_OBSERVATION: >
  Changing an order's lines after a free-shipping reward was applied causes the recomputed shipping charge
  to be only partly waived, or not re-waived at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a free-shipping reward, change the order's lines so the shipping charge recomputes, and inspect
  whether the new charge is fully waived.
```

## G08-SALE_LOYALTY_DELIVERY-Q009

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q009
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping reward that waives a charge which is later revised upward continues to cover the revised
  amount, not only the smaller amount that existed when the reward was applied.
WHY_IT_MATTERS: >
  A reward capped at the original, smaller figure leaves the customer paying the increase on a shipment
  they were told was free.
DISCONFIRMING_OBSERVATION: >
  A shipping charge revised upward after a free-shipping reward was applied leaves the increase
  unwaived and payable by the customer.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a free-shipping reward, then revise the shipping charge upward, and inspect whether the full,
  revised amount remains waived.
```

## G08-SALE_LOYALTY_DELIVERY-Q010

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q010
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping reward that waives a charge which is later revised downward does not leave a residual,
  unexplained credit once the smaller charge is waived in full.
WHY_IT_MATTERS: >
  A leftover credit from waiving a now-smaller charge, if not resolved, could be mistaken for a separate,
  unrelated balance owed to the customer.
DISCONFIRMING_OBSERVATION: >
  A shipping charge revised downward after a free-shipping reward was applied leaves a credit on the order
  beyond simply waiving the smaller, revised charge.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a free-shipping reward, then revise the shipping charge downward, and inspect the order for any
  residual credit.
```

## G08-SALE_LOYALTY_DELIVERY-Q011

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q011
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If the shipping method itself becomes unavailable and a different method with a different charge is
  substituted after a free-shipping reward was applied, the reward is re-evaluated against the new method's
  charge rather than silently continuing to reference the original, now-obsolete method.
WHY_IT_MATTERS: >
  A reward left referencing a method that no longer exists on the order cannot be trusted to actually waive
  whatever the customer ends up being charged.
DISCONFIRMING_OBSERVATION: >
  A shipping method substitution after a free-shipping reward was applied leaves the reward still referring
  to the original method, with the new method's charge left unwaived.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a free-shipping reward, force the original shipping method to become unavailable so a different
  method is substituted, and inspect the reward's coverage.
```

## G08-SALE_LOYALTY_DELIVERY-Q012

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q012
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A change to the general shipping rate configuration after a free-shipping reward was applied to an order,
  but before that order is confirmed, is reflected in what the reward actually waives at confirmation.
WHY_IT_MATTERS: >
  A reward that continues to reference a pre-change rate could waive less, or more, than the charge the
  order will actually be confirmed with.
DISCONFIRMING_OBSERVATION: >
  Changing the general shipping rate configuration between applying a free-shipping reward and confirming
  the order leaves the reward waiving an amount that does not match the charge in force at confirmation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply a free-shipping reward, change the general shipping rate configuration, and confirm the order,
  inspecting what the reward actually waived.
```

## G08-SALE_LOYALTY_DELIVERY-Q013

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q013
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The waived amount recorded against a free-shipping reward is always traceable to the specific shipping
  charge computation it waived, even after that computation has since been superseded by a newer one.
WHY_IT_MATTERS: >
  Without that trace, a reviewer cannot verify, after several recomputations, that the reward's recorded
  waived value ever actually matched a real charge that existed at some point.
DISCONFIRMING_OBSERVATION: >
  After a shipping charge is recomputed more than once, the free-shipping reward's recorded waived amount
  cannot be traced to any specific charge computation it corresponds to.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger more than one shipping charge recomputation on an order carrying a free-shipping reward and
  attempt to trace the reward's recorded waived amount to a specific computation.
```

## G08-SALE_LOYALTY_DELIVERY-Q014

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q014
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping reward applied to an order whose shipping charge is later manually overridden waives the
  overridden figure, not the figure the system would otherwise have computed.
WHY_IT_MATTERS: >
  If the reward waives only the system-computed figure while a higher manual override stands, the customer
  is left paying the difference despite holding a reward meant to cover shipping in full.
DISCONFIRMING_OBSERVATION: >
  A shipping charge manually overridden to a higher figure after a free-shipping reward was applied leaves
  the override amount, or part of it, unwaived and payable.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a free-shipping reward, manually override the shipping charge to a different figure, and inspect
  whether the override is fully waived.
```

## G08-SALE_LOYALTY_DELIVERY-Q015

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q015
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a shipping-targeted reward can cover only part of the shipping charge, leaving a remainder
  payable by the customer, is a defined, configurable behaviour of the reward, not assumed to always be
  all-or-nothing.
WHY_IT_MATTERS: >
  A rigid all-or-nothing assumption cannot express a genuinely common commercial offer, such as a fixed
  shipping discount that does not always cover the full charge.
DISCONFIRMING_OBSERVATION: >
  A shipping-targeted reward configured to cover only a fixed portion of the charge instead waives the
  charge completely, or not at all, with no partial outcome available.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a shipping-targeted reward intended to cover only part of the charge and apply it to an order
  whose charge exceeds that partial coverage.
```

## G08-SALE_LOYALTY_DELIVERY-Q016

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q016
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where a shipping-targeted reward covers only part of the charge, the remainder payable by the customer is
  shown as its own identifiable amount, distinguishable from the portion the reward covered.
WHY_IT_MATTERS: >
  A customer who cannot see the split between what the reward covered and what they still owe cannot verify
  the charge is correct.
DISCONFIRMING_OBSERVATION: >
  A partially covered shipping charge shows only a single net figure, with no breakdown of the
  reward-covered portion versus the customer-payable remainder.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a partially covering shipping reward and inspect whether the order shows the covered and remaining
  portions separately.
```

## G08-SALE_LOYALTY_DELIVERY-Q017

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q017
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A shipping-targeted reward with a capped monetary value, applied to a shipping charge that exceeds the
  cap, leaves the excess as a customer-payable amount rather than silently waiving the whole charge
  regardless of the cap.
WHY_IT_MATTERS: >
  Silently waiving beyond the configured cap gives away more discount than the promotion was ever designed
  to cost.
DISCONFIRMING_OBSERVATION: >
  A capped shipping-targeted reward applied to a charge exceeding its cap waives the charge in full, with no
  customer-payable excess recorded.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a capped shipping-targeted reward to a shipping charge that exceeds the cap and inspect the
  resulting customer-payable amount.
```

## G08-SALE_LOYALTY_DELIVERY-Q018

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q018
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A shipping-targeted reward with a capped monetary value, applied to a shipping charge below the cap, does
  not carry the unused portion of the cap forward to reduce anything else on the order.
WHY_IT_MATTERS: >
  A cap that bleeds into reducing unrelated parts of the order gives away value the reward was never
  configured to cover.
DISCONFIRMING_OBSERVATION: >
  Applying a capped shipping-targeted reward to a charge below its cap reduces some other, unrelated amount
  on the order by the unused portion of the cap.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a capped shipping-targeted reward to a shipping charge below the cap and inspect whether any other
  part of the order is reduced by the unused portion.
```

## G08-SALE_LOYALTY_DELIVERY-Q019

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q019
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The customer-payable remainder of a partially covered shipping charge is taxed according to the same rule
  that would govern the full shipping charge's tax, not treated as an untaxed residual purely because a
  reward is also involved.
WHY_IT_MATTERS: >
  An untaxed remainder purely because a reward touched the charge is a tax compliance exposure with no
  policy basis behind it.
DISCONFIRMING_OBSERVATION: >
  The customer-payable remainder of a partially covered shipping charge shows no tax, while the same charge
  would have been taxed had no reward been involved.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a partially covering shipping reward to a taxable shipping charge and inspect the tax on the
  customer-payable remainder.
```

## G08-SALE_LOYALTY_DELIVERY-Q020

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q020
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether the reward or the customer is deemed to bear a subsequently discovered variance between the
  estimated and actual shipping cost, on a charge the reward only partially covered, is a defined rule
  distinguishing the reward's fixed contribution from the customer's variable remainder.
WHY_IT_MATTERS: >
  Without a defined rule, a discovered variance on a partially covered charge has no basis for deciding
  whether it changes the reward's contribution, the customer's remainder, or both.
DISCONFIRMING_OBSERVATION: >
  A shipping cost variance discovered after a partially covering reward was applied is resolved with no
  documented rule for whether it affects the reward's fixed contribution or the customer's remainder.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Apply a partially covering shipping reward, then discover an actual cost variance against the estimate,
  and inspect how the variance is allocated.
```

## G08-SALE_LOYALTY_DELIVERY-Q021

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q021
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A partially covering shipping reward applied to an order with more than one shipping-charged line or
  shipment allocates its coverage across them according to a defined, consistent rule, not an arbitrary
  split.
WHY_IT_MATTERS: >
  An arbitrary split cannot be reproduced or explained if a customer or auditor asks how the reward's
  coverage was divided among several shipping charges.
DISCONFIRMING_OBSERVATION: >
  A partially covering shipping reward applied to an order with more than one shipping charge splits its
  coverage between them with no rule that can be reproduced for a comparable order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply a partially covering shipping reward to an order carrying more than one shipping-charged line and
  inspect how its coverage is allocated.
```
## G08-SALE_LOYALTY_DELIVERY-Q022

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q022
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping reward applied to an order that is ultimately fulfilled through several shipments
  continues to waive the shipping charge across all of them, not only the first shipment dispatched.
WHY_IT_MATTERS: >
  A reward that only covers the first shipment leaves the customer unexpectedly charged for every
  subsequent one, despite having been told shipping was free for the order.
DISCONFIRMING_OBSERVATION: >
  An order fulfilled through several shipments has its free-shipping reward waive only the first shipment's
  charge, with later shipments charged in full.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a free-shipping reward to an order, fulfil it through several shipments, and inspect the charge on
  each.
```

## G08-SALE_LOYALTY_DELIVERY-Q023

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q023
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If splitting an order into several shipments would, absent any reward, produce more than one shipping
  charge, a free-shipping reward waives the combined total rather than only one of the several charges that
  would otherwise apply.
WHY_IT_MATTERS: >
  Waiving only one of several charges leaves the customer paying for the rest despite the reward being
  understood to cover shipping for the order as a whole.
DISCONFIRMING_OBSERVATION: >
  An order that would incur more than one shipping charge across its shipments, absent any reward, has its
  free-shipping reward waive only one of those charges.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a free-shipping reward to an order that would otherwise incur more than one shipping charge across
  its shipments and inspect which charges are waived.
```

## G08-SALE_LOYALTY_DELIVERY-Q024

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q024
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping reward's total waived value, once an order splits into several shipments, does not exceed
  what a single combined shipping charge for the whole order would have been.
WHY_IT_MATTERS: >
  A waived total that exceeds what a single combined charge would have cost gives the reward more value
  than it was ever configured to be worth, purely as an artefact of how fulfilment happened to split.
DISCONFIRMING_OBSERVATION: >
  The sum of shipping charges waived across an order's several shipments exceeds what a single combined
  shipping charge for the whole order would have amounted to.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compare the total shipping charge waived across an order's multiple shipments against what one combined
  charge for the whole order would have been.
```

## G08-SALE_LOYALTY_DELIVERY-Q025

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q025
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When an order splits into shipments at different times, a free-shipping reward that has since expired
  does not retroactively fail to cover a shipment that was already dispatched while the reward was still
  valid.
WHY_IT_MATTERS: >
  Retroactively withdrawing coverage from an already-dispatched shipment charges the customer, after the
  fact, for something the reward genuinely covered at the time it was dispatched.
DISCONFIRMING_OBSERVATION: >
  A shipment dispatched while a free-shipping reward was still valid is later charged after the reward
  expires, because a later shipment on the same order is invoiced after the expiry.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Dispatch one shipment of a multi-shipment order while a free-shipping reward is valid, let the reward
  expire, then invoice a later shipment and inspect the earlier shipment's charge.
```

## G08-SALE_LOYALTY_DELIVERY-Q026

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q026
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A free-shipping reward applied to an order later split into shipments remains traceable, from any one
  shipment's invoice, back to the single reward that is waiving its portion of the charge.
WHY_IT_MATTERS: >
  Without that trace, reconciling how much of a reward's value has been used across a multi-shipment order
  requires piecing together evidence the record does not directly provide.
DISCONFIRMING_OBSERVATION: >
  A shipment's invoice showing a waived shipping charge has no link back to the originating free-shipping
  reward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a free-shipping reward to an order split into shipments and inspect whether each shipment's invoice
  traces back to the reward.
```

## G08-SALE_LOYALTY_DELIVERY-Q027

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q027
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  If a partially covering, not fully free, shipping reward is applied to an order split into several
  shipments, its capped coverage is allocated across the shipments by a defined rule, not fully consumed by
  whichever shipment happens to be invoiced first.
WHY_IT_MATTERS: >
  A cap fully consumed by the first shipment leaves every later shipment paying full shipping, an outcome
  that depends only on dispatch order rather than on any actual rule.
DISCONFIRMING_OBSERVATION: >
  A partially covering shipping reward's entire capped value is consumed by the first shipment invoiced on
  a multi-shipment order, leaving none for later shipments regardless of a defined allocation rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply a capped, partially covering shipping reward to an order split into several shipments and inspect
  how the cap is allocated across them.
```

## G08-SALE_LOYALTY_DELIVERY-Q028

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q028
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling one of several shipments on an order that carries a free-shipping reward re-evaluates the
  reward's waived amount against what remains to be shipped, rather than leaving it fixed against a
  shipment plan that no longer exists in full.
WHY_IT_MATTERS: >
  A waived amount left fixed against a cancelled shipment plan can misstate what the reward is actually
  covering once part of the plan no longer exists.
DISCONFIRMING_OBSERVATION: >
  Cancelling one shipment of a multi-shipment order leaves the free-shipping reward's recorded waived amount
  unchanged from what it was against the original, larger shipment plan.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel one shipment of a multi-shipment order carrying a free-shipping reward and inspect whether the
  reward's waived amount is re-evaluated.
```

## G08-SALE_LOYALTY_DELIVERY-Q029

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q029
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  An order that both carries a shipping-targeted reward and independently qualifies for a general
  free-shipping threshold does not have its shipping charge waived twice, once by each mechanism, in a way
  that produces a negative or double-counted benefit.
WHY_IT_MATTERS: >
  A double waiver that goes negative or double-counts corrupts the order total and cannot represent any
  coherent commercial outcome.
DISCONFIRMING_OBSERVATION: >
  An order qualifying for both a shipping-targeted reward and a general free-shipping threshold shows a
  shipping-related credit or negative amount beyond simply waiving the charge to zero once.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct an order that both holds a shipping-targeted reward and independently qualifies for a general
  free-shipping threshold, and inspect the resulting shipping charge.
```

## G08-SALE_LOYALTY_DELIVERY-Q030

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q030
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When an order qualifies for both a shipping-targeted reward and a general free-shipping threshold,
  exactly one of the two is recorded as the operative reason the charge was waived, through a defined
  precedence rule.
WHY_IT_MATTERS: >
  Without a recorded operative reason, no one can later say whether the reward or the threshold is what
  actually saved the business or cost it the shipping charge on that order.
DISCONFIRMING_OBSERVATION: >
  An order qualifying for both a shipping-targeted reward and a general free-shipping threshold shows a
  waived shipping charge with no record of which of the two mechanisms is the operative reason.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Construct an order eligible under both a shipping-targeted reward and a general free-shipping threshold
  and inspect what the order records as the operative reason for the waiver.
```

## G08-SALE_LOYALTY_DELIVERY-Q031

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q031
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A shipping-targeted reward applied to an order that already qualifies for a free-shipping threshold is
  either withheld as redundant, or explicitly recorded as the second, dormant benefit, rather than the two
  silently coexisting with no record of which one is actually in effect.
WHY_IT_MATTERS: >
  Silent coexistence with no record leaves it impossible to tell, after the fact, whether the reward was
  ever genuinely needed or effective on that order.
DISCONFIRMING_OBSERVATION: >
  A shipping-targeted reward applied to an order already covered by a free-shipping threshold shows no
  record of whether it was withheld as redundant or recorded as a dormant second benefit.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a shipping-targeted reward to an order already qualifying for a general free-shipping threshold and
  inspect what the order records about the redundant reward.
```

## G08-SALE_LOYALTY_DELIVERY-Q032

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q032
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  If the order's value later drops below the general free-shipping threshold, an independently held
  shipping-targeted reward can still take over and continue waiving the charge, rather than the order
  suddenly losing free shipping entirely.
WHY_IT_MATTERS: >
  Losing free shipping entirely, when a separately earned reward could still cover it, denies the customer
  a benefit they independently and legitimately hold.
DISCONFIRMING_OBSERVATION: >
  An order's value drops below the general free-shipping threshold, and a separately held, still-valid
  shipping-targeted reward does not take over to keep the charge waived.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Qualify an order for both a free-shipping threshold and an independent shipping-targeted reward, then
  reduce the order below the threshold, and inspect the resulting shipping charge.
```

## G08-SALE_LOYALTY_DELIVERY-Q033

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q033
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  The customer's coupon or reward is not consumed, its usage count decremented or a single-use coupon marked
  spent, on an order where a general free-shipping threshold was already going to waive the charge
  regardless, where the configuration says the reward should not fire when redundant.
WHY_IT_MATTERS: >
  Consuming a reward that was never actually needed takes value away from the customer for a benefit the
  order would have received anyway.
DISCONFIRMING_OBSERVATION: >
  A shipping-targeted coupon configured not to fire when redundant is nonetheless marked consumed on an
  order that already qualified for a general free-shipping threshold.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure a shipping-targeted coupon to not fire when redundant, apply it to an order already qualifying
  for a free-shipping threshold, and inspect whether the coupon is marked consumed.
```

## G08-SALE_LOYALTY_DELIVERY-Q034

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q034
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a redundant shipping-targeted reward is consumed anyway, or preserved for a future order, when a
  free-shipping threshold already covers the charge, is a defined, configurable rule, not an unstated
  default.
WHY_IT_MATTERS: >
  An unstated default for the redundant case cannot be communicated to the customer as a promise about what
  happens to their unused reward.
DISCONFIRMING_OBSERVATION: >
  Two comparable orders, each redundantly holding a shipping-targeted reward alongside a qualifying
  free-shipping threshold, resolve the reward's consumption differently with no configuration explaining
  why.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Reproduce the redundant-reward-plus-threshold condition on two comparable orders and compare whether the
  reward is consumed in each case.
```

## G08-SALE_LOYALTY_DELIVERY-Q035

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q035
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A double-benefit condition, where both a reward and a threshold would independently waive the charge, is
  detectable and reportable, so that the business can review how often it occurs and what it costs, rather
  than being invisible once the single waived outcome is recorded.
WHY_IT_MATTERS: >
  An invisible double-benefit condition prevents the business from ever knowing how often a reward is being
  spent for no additional customer benefit, information it would need to tune the promotion.
DISCONFIRMING_OBSERVATION: >
  There is no way to identify, after the fact, which orders had both a reward and a threshold independently
  qualifying to waive the shipping charge.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce several orders with the double-benefit condition and attempt to identify them collectively through
  any available report.
```

## G08-SALE_LOYALTY_DELIVERY-Q036

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q036
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Returning goods from an order whose shipping charge was fully covered by a reward does not generate a
  shipping refund, consistent with a configured non-refundable-shipping policy, distinct from whether the
  goods themselves are refunded.
WHY_IT_MATTERS: >
  A shipping refund generated on a charge the customer never actually paid, because a reward covered it,
  would refund money that was never collected.
DISCONFIRMING_OBSERVATION: >
  Returning goods from an order whose shipping was fully covered by a reward generates a shipping refund
  under a policy that treats shipping as non-refundable.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Return goods from an order whose shipping charge was fully waived by a reward, under a non-refundable-
  shipping policy, and inspect whether a shipping refund is generated.
```
## G08-SALE_LOYALTY_DELIVERY-Q037

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q037
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A shipping-targeted reward consumed on an order that is later returned is handled by a defined reversal
  rule, restored or not per the reward's own type, independent of whether the shipping charge itself is
  refundable.
WHY_IT_MATTERS: >
  Conflating the reward's own reversal with the shipping charge's refundability could wrongly deny the
  customer a coupon's return purely because shipping itself is policy-non-refundable, or vice versa.
DISCONFIRMING_OBSERVATION: >
  A return processed on an order with a shipping-targeted reward resolves the reward's own reversal purely
  based on whether shipping happens to be refundable, with no independent rule for the reward itself.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Consume a shipping-targeted reward on an order under a non-refundable-shipping policy, process a return,
  and inspect whether the reward's own reversal is handled independently of the shipping refund policy.
```

## G08-SALE_LOYALTY_DELIVERY-Q038

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q038
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Where shipping is configured as non-refundable, a partial return of an order whose shipping charge was
  only partially covered by a reward still leaves the customer-payable remainder non-refundable, consistent
  with the same policy that would apply had no reward been involved.
WHY_IT_MATTERS: >
  If the remainder becomes refundable purely because a reward was also involved, the non-refundable policy
  is applied inconsistently depending on an unrelated factor.
DISCONFIRMING_OBSERVATION: >
  A partial return of an order with a partially covered, non-refundable shipping charge refunds the
  customer-payable remainder, unlike an equivalent order with no reward involved.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Process a partial return on an order whose shipping charge was partially covered by a reward, under a
  non-refundable-shipping policy, and inspect the remainder's refund outcome.
```

## G08-SALE_LOYALTY_DELIVERY-Q039

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q039
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A return that triggers no shipping refund, because the shipping charge was already fully waived by a
  reward, still records that outcome as a deliberate application of the non-refundable-shipping policy, not
  indistinguishable from a return where a shipping refund was simply forgotten.
WHY_IT_MATTERS: >
  An indistinguishable outcome cannot be defended to a customer, or checked by an auditor, as a deliberate
  policy application rather than an oversight.
DISCONFIRMING_OBSERVATION: >
  A return on a reward-waived shipping charge shows no shipping refund with no record distinguishing that
  outcome from a return where a shipping refund was simply never processed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Process a return on an order whose shipping was fully waived by a reward and inspect what the return
  record shows about the absent shipping refund.
```

## G08-SALE_LOYALTY_DELIVERY-Q040

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q040
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a return is processed after a free-shipping reward has already been reversed through an earlier,
  related cancellation, the return's own handling of the shipping charge does not attempt to reverse the
  same waiver a second time.
WHY_IT_MATTERS: >
  Reversing the same waiver twice could generate a phantom charge or credit that does not correspond to any
  real, single event.
DISCONFIRMING_OBSERVATION: >
  Processing a return on an order whose free-shipping reward was already reversed by an earlier
  cancellation produces a second, duplicate reversal of the same waiver.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reverse a free-shipping reward through a partial cancellation, then process a return on the same order,
  and inspect whether the reward's waiver is reversed a second time.
```

## G08-SALE_LOYALTY_DELIVERY-Q041

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q041
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A customer disputing why no shipping refund was issued on a return can have the original reward's role in
  waiving that charge shown, so the non-refundable outcome is explainable back to the reward rather than
  looking like an arbitrary denial.
WHY_IT_MATTERS: >
  Without that explanation, support staff have no way to show the customer why no shipping refund is due
  beyond asserting the policy exists.
DISCONFIRMING_OBSERVATION: >
  Investigating a return with no shipping refund on a reward-waived shipping charge gives no way to surface
  the reward's earlier role in waiving that charge.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  As support staff, investigate a return where no shipping refund was issued on a reward-waived shipping
  charge and attempt to surface the reward's role.
```

## G08-SALE_LOYALTY_DELIVERY-Q042

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q042
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether the non-refundable-shipping policy applies identically to a charge the customer actually paid
  versus a charge a reward covered on the customer's behalf is a defined, deliberate rule, not an assumption
  that only literal customer payments are ever refundable.
WHY_IT_MATTERS: >
  An unexamined assumption that only literal payments are refundable could produce a different, unintended
  outcome for reward-covered charges than the policy was actually meant to have.
DISCONFIRMING_OBSERVATION: >
  A shipping charge paid directly by the customer and an equivalent one covered by a reward are subject to
  different refund outcomes under the same stated non-refundable-shipping policy, with no rule explaining
  the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the return outcome for a directly paid shipping charge against an equivalent reward-covered one
  under the same stated policy.
```

## G08-SALE_LOYALTY_DELIVERY-Q043

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q043
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A shipping line reduced to zero by a shipping-targeted reward is distinguishable, in its tax treatment,
  from a shipping line that was never taxable in the first place.
WHY_IT_MATTERS: >
  Indistinguishable tax treatment between the two cases makes it impossible to later audit how much tax
  revenue was actually foregone specifically because of the reward.
DISCONFIRMING_OBSERVATION: >
  A shipping line reduced to zero by a reward and a shipping line that was never taxable show identically in
  tax records, with no way to tell them apart.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create one shipping line reduced to zero by a reward and one shipping line that was never taxable, and
  compare their tax records.
```

## G08-SALE_LOYALTY_DELIVERY-Q044

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q044
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The tax basis of a shipping charge fully waived by a reward is reduced to match, so tax is not charged on
  an amount the customer no longer actually owes.
WHY_IT_MATTERS: >
  Charging tax on a fully waived amount bills the customer tax on money that changed hands for nothing,
  which is both a compliance and a customer-trust exposure.
DISCONFIRMING_OBSERVATION: >
  A shipping charge fully waived by a reward still shows a nonzero tax amount due on the waived figure.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a shipping-targeted reward that fully waives a taxable shipping charge and inspect the resulting tax
  due on that line.
```

## G08-SALE_LOYALTY_DELIVERY-Q045

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q045
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A shipping charge only partially covered by a reward is taxed on the customer-payable remainder using the
  same tax rate the full charge would have carried, not a rate that changes purely because part of the
  charge was waived.
WHY_IT_MATTERS: >
  A tax rate that shifts purely because of partial coverage cannot be defended as following the jurisdiction's
  actual rate rule for shipping.
DISCONFIRMING_OBSERVATION: >
  The tax rate applied to a partially covered shipping charge's customer-payable remainder differs from the
  rate the full, uncovered charge would have carried.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a partially covering shipping reward to a taxable charge and compare the tax rate on the remainder
  against the rate the full charge would have carried.
```

## G08-SALE_LOYALTY_DELIVERY-Q046

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q046
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing a shipping-targeted reward, for example on cancellation, restores the shipping line's tax to
  what it would have been without the reward, rather than leaving the tax figure based on the waived, zeroed
  amount.
WHY_IT_MATTERS: >
  A tax figure left at zero after the reward that zeroed it is reversed understates the tax now due on a
  charge that has, in effect, been reinstated.
DISCONFIRMING_OBSERVATION: >
  Reversing a shipping-targeted reward that had zeroed a shipping charge leaves the shipping line's tax
  amount at zero even though the charge itself has been reinstated.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a shipping-targeted reward that zeroes a taxable charge, reverse the reward, and inspect the
  resulting tax figure.
```

## G08-SALE_LOYALTY_DELIVERY-Q047

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q047
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The record of a shipping charge waived to zero by a reward retains the original, pre-waiver tax amount as
  a reference, so what would have been due absent the reward remains visible for reconciliation.
WHY_IT_MATTERS: >
  Without that reference, the tax authority-facing impact of the reward programme on shipping tax cannot be
  quantified from the order records themselves.
DISCONFIRMING_OBSERVATION: >
  A shipping charge waived to zero by a reward retains no record of what its tax amount would have been
  absent the reward.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply a shipping-targeted reward that zeroes a taxable charge and inspect whether the original,
  pre-waiver tax amount remains retrievable.
```

## G08-SALE_LOYALTY_DELIVERY-Q048

```yaml
QID: G08-SALE_LOYALTY_DELIVERY-Q048
MODULE: sale_loyalty_delivery
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A jurisdiction's tax rule that taxes a reward's face value itself as a deemed benefit, where applicable,
  is a distinguishable configuration from the ordinary case where the waived shipping tax simply drops to
  zero, so the two are not conflated under one default behaviour.
WHY_IT_MATTERS: >
  Conflating the two cases under one default either wrongly taxes an ordinary waiver as a deemed benefit, or
  misses a genuine deemed-benefit tax obligation where the jurisdiction actually requires it.
DISCONFIRMING_OBSERVATION: >
  There is no distinguishable configuration between a jurisdiction that taxes a shipping reward's face value
  as a deemed benefit and the ordinary case where waived shipping tax simply drops to zero.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Inspect the configuration available for a jurisdiction that taxes a reward's face value as a deemed
  benefit and compare it against the ordinary waived-to-zero configuration.
```
