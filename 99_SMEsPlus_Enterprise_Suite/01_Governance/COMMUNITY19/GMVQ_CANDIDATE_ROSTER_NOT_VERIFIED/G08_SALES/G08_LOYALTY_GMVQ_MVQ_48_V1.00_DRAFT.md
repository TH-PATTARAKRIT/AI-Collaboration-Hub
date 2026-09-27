# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / loyalty Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-LOYALTY-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `loyalty`
**Wave:** W2
**Author Cell:** TEAM P-S2 (GMVQ Question Factory — Production Cell P-S2, Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This is one of the four base capabilities of G08 SALES and receives the deep treatment the Group Brief
reserves for base modules. Its ground is the reward/discount programme itself — rules, points, coupons and
their validity — considered independently of any specific order it is later applied to. Questions cover:
points earned on an order later cancelled or returned; points as a recognised liability and its recognition
and de-recognition timing; a programme rule changed while balances already exist; expiry of points and the
notice a customer receives; a coupon redeemed twice or concurrently; a coupon restricted to one customer
used under another; stacking of several rewards and the order in which they are applied; a reward whose
face value exceeds the order it is used on; programme membership and balance-sharing across companies;
transferring or merging balances when customer records merge; and the audit trail of a manual balance
adjustment.

This bank deliberately stays off the seam with the order itself — what a reward does to an order's total,
its tax treatment, and its behaviour across partial delivery, partial invoicing or cancellation of the
order it was applied to belong to `sale_loyalty`, authored separately as a bridge in this same batch. This
bank asks only about the programme and the reward/coupon/point object considered on its own terms.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, cross-module dependency, auditability, tenant/company boundary,
  concurrency and ordering, and runtime/configuration reachability.
- This module carries both a configuration layer (earn/redemption rates, stacking and precedence rules,
  cross-company sharing, expiry policy) and a runtime process layer (accrual, redemption, expiry,
  cancellation reversal, merge); each question is tagged `LAYER: BASE` or `LAYER: PROCESS` accordingly.
- Pre-authoring sibling check (Bridge Module Rule §5): `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md`
  was run before authoring. At authoring time this bank and `G08_DELIVERY` were being produced in the same
  batch by the same cell; this bank's ground (the programme and its objects) and `delivery`'s ground (the
  commercial shipping charge) do not overlap, and both were kept off `sale_loyalty` and
  `sale_loyalty_delivery`'s seam ground, authored separately in this same batch.
- This module is a base module, not a bridge, per the G08 Group Brief; it is authored for full depth on its
  own ground rather than restricted to seam-only questions.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-LOYALTY-Q001

```yaml
QID: G08-LOYALTY-Q001
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Points credited when an order is placed are reversed if that order is fully cancelled before completion,
  rather than remaining on the customer's balance for an order that was never fulfilled.
WHY_IT_MATTERS: >
  Uncancelled points on a cancelled order are a liability the business never actually earned the right to
  grant, accumulating unnoticed across every cancelled order.
DISCONFIRMING_OBSERVATION: >
  An order is fully cancelled before completion and the points it credited remain on the customer's
  balance with no reversal.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place an order that credits points, cancel it fully before completion, and inspect the customer's point
  balance afterward.
```

## G08-LOYALTY-Q002

```yaml
QID: G08-LOYALTY-Q002
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Points credited for an order are recalculated, not simply left untouched, when the order is partially
  returned, so the balance reflects only what was actually kept.
WHY_IT_MATTERS: >
  A balance left at its original, pre-return level over-rewards a customer for goods they no longer have,
  repeated across every partial return.
DISCONFIRMING_OBSERVATION: >
  A partial return of an order's goods leaves the customer's point balance from that order completely
  unchanged from what it was before the return.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place an order that credits points, process a partial return against it, and inspect the resulting point
  balance.
```

## G08-LOYALTY-Q003

```yaml
QID: G08-LOYALTY-Q003
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Points already redeemed by a customer before their originating order is cancelled are handled by a
  defined rule (clawback, negative balance, hold) rather than left unresolved with no recorded consequence.
WHY_IT_MATTERS: >
  An unresolved case lets a customer keep the value of points earned on an order that never completed,
  with no policy governing the outcome.
DISCONFIRMING_OBSERVATION: >
  A customer redeems points earned from an order, that order is then cancelled, and nothing in the
  customer's balance or history reflects any consequence of the cancellation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Earn and redeem points from a given order, then cancel that order, and inspect what happens to the
  balance and history.
```

## G08-LOYALTY-Q004

```yaml
QID: G08-LOYALTY-Q004
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The reversal of points tied to a cancelled or returned order is itself a traceable event on the
  customer's point history, not an invisible adjustment that changes the balance with no explanation.
WHY_IT_MATTERS: >
  An untraceable reversal is indistinguishable from an error or an unauthorised adjustment when a customer
  disputes their balance.
DISCONFIRMING_OBSERVATION: >
  A point reversal caused by an order cancellation changes the customer's balance with no corresponding
  entry in their point history explaining the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a point reversal through an order cancellation and inspect the customer's point history for a
  corresponding entry.
```

## G08-LOYALTY-Q005

```yaml
QID: G08-LOYALTY-Q005
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Points issued to a customer are recognised as an outstanding programme liability at the moment they are
  granted, not only when, or if, they are eventually redeemed.
WHY_IT_MATTERS: >
  A liability recognised only on redemption understates the business's true outstanding obligation at any
  point where a customer holds unredeemed points, misstating financial exposure.
DISCONFIRMING_OBSERVATION: >
  A batch of points is granted to customers and no outstanding liability figure changes until some of those
  points are actually redeemed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Grant points to a customer and inspect whether an outstanding liability figure changes immediately, prior
  to any redemption.
```

## G08-LOYALTY-Q006

```yaml
QID: G08-LOYALTY-Q006
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  The monetary value assigned to an unredeemed point balance for liability purposes is a defined,
  documented rate, not an implicit assumption that differs depending on which report is run.
WHY_IT_MATTERS: >
  Two different valuations of the same outstanding balance, produced by different reports, cannot both be
  right, and neither can be defended without a documented rate.
DISCONFIRMING_OBSERVATION: >
  Two different reports valuing the same customer's outstanding point balance at the same moment produce
  two different monetary figures with no documented rate reconciling them.
EXPECTED_SURFACE: S2,S7
PRECONDITIONS: >
  Produce two different reports that value the same outstanding point balance and compare the rate each
  applies.
```

## G08-LOYALTY-Q007

```yaml
QID: G08-LOYALTY-Q007
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Points that expire unredeemed are removed from the outstanding liability at the moment they expire,
  rather than remaining counted as a future obligation indefinitely.
WHY_IT_MATTERS: >
  An outstanding liability that never de-recognises expired points overstates the business's real
  obligation more and more with every expiry cycle that passes unrecorded.
DISCONFIRMING_OBSERVATION: >
  A batch of points passes its expiry date and the outstanding liability figure is unchanged from before
  the expiry.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Let a batch of granted points reach its expiry date and inspect the outstanding liability figure before
  and after.
```

## G08-LOYALTY-Q008

```yaml
QID: G08-LOYALTY-Q008
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  The liability figure for outstanding points can be produced for a given point in time, a period-end cut,
  not only as a live, unrepeatable snapshot that cannot be reconciled after the fact.
WHY_IT_MATTERS: >
  Without a reproducible point-in-time figure, a closed period's stated liability can never be
  independently checked once time has moved on.
DISCONFIRMING_OBSERVATION: >
  Attempting to reproduce a previously reported period-end outstanding liability figure at a later date
  produces a different result with no way to reconcile the two.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a period-end outstanding liability figure, then attempt to reproduce that same figure at a later
  date and compare.
```

## G08-LOYALTY-Q009

```yaml
QID: G08-LOYALTY-Q009
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A change to the earn rate applies only to activity from the point of the change forward, not
  retroactively recalculating points already credited under the previous rate.
WHY_IT_MATTERS: >
  A retroactive recalculation changes what a customer was already told they earned on a completed order,
  which they have no way to anticipate or agree to.
DISCONFIRMING_OBSERVATION: >
  Changing the earn rate causes points already credited on orders placed before the change to be
  recalculated to a different amount.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Credit points to a customer under one earn rate, change the earn rate, and re-inspect the previously
  credited amount.
```

## G08-LOYALTY-Q010

```yaml
QID: G08-LOYALTY-Q010
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A change to the redemption rate is applied consistently to a customer's whole existing balance rather
  than the same balance being worth two different amounts depending on when each portion was earned.
WHY_IT_MATTERS: >
  A balance that redeems at two different values depending on its earn date cannot be explained to a
  customer as a single, coherent number of points.
DISCONFIRMING_OBSERVATION: >
  A single customer balance redeems at two different monetary values depending on which portion of the
  balance is drawn down, purely because of when each portion was earned.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Accumulate a balance across an earn-rate or redemption-rate change and redeem portions of it, comparing
  the value applied.
```

## G08-LOYALTY-Q011

```yaml
QID: G08-LOYALTY-Q011
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Tightening a programme rule, for example a new minimum redemption amount, does not strand an existing
  balance that was valid to redeem under the prior rule, leaving the customer with no way to use it.
WHY_IT_MATTERS: >
  A stranded balance is an unresolved customer-facing liability that the business granted in good faith and
  then made unusable by its own rule change.
DISCONFIRMING_OBSERVATION: >
  A customer's existing balance, valid to redeem before a rule tightening, becomes entirely unredeemable
  afterward with no transition or grandfathering provision.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Hold a balance valid to redeem under current rules, tighten a redemption rule, and attempt to redeem the
  existing balance.
```

## G08-LOYALTY-Q012

```yaml
QID: G08-LOYALTY-Q012
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A programme rule change is recorded with an effective date that is itself retrievable, so that a
  balance's history can be explained against the rule that was actually in force at each point.
WHY_IT_MATTERS: >
  Without a retrievable effective date, a disputed balance from months ago cannot be checked against the
  rule that genuinely applied at the time.
DISCONFIRMING_OBSERVATION: >
  A programme rule that has changed more than once has no retrievable record of when each version took
  effect.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change a programme rule more than once over time and attempt to retrieve when each version became
  effective.
```

## G08-LOYALTY-Q013

```yaml
QID: G08-LOYALTY-Q013
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Points that carry an expiry are tracked with enough granularity, per batch earned rather than only a
  single balance figure, that the correct portion actually expires rather than an arbitrary or the entire
  balance being affected.
WHY_IT_MATTERS: >
  Without batch-level tracking, expiry can only be applied to the whole balance or not at all, neither of
  which matches a genuine per-batch expiry policy.
DISCONFIRMING_OBSERVATION: >
  A customer with points earned at different times, only some of which have reached their expiry date, has
  either the whole balance or none of it affected when expiry runs.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Accrue points for a customer in more than one batch with different expiry dates and run expiry when only
  one batch has matured.
```

## G08-LOYALTY-Q014

```yaml
QID: G08-LOYALTY-Q014
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A customer due to lose points to expiry receives some form of advance notice before the expiry takes
  effect, rather than the balance silently dropping with no warning.
WHY_IT_MATTERS: >
  A silent drop in balance is the single most common driver of reward-programme complaints and erodes the
  trust the programme exists to build.
DISCONFIRMING_OBSERVATION: >
  A customer's points expire with no notice of any kind issued before the expiry took effect.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Let a customer's points approach their configured expiry date and check for any notice issued beforehand.
```

## G08-LOYALTY-Q015

```yaml
QID: G08-LOYALTY-Q015
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Redeeming points draws down the portion nearest to expiry first, or another defined order, rather than an
  undefined order that could cause points to expire that the customer could otherwise have used.
WHY_IT_MATTERS: >
  An undefined draw-down order can expire points a customer would have preferred to spend, which they had
  no way to prevent since they cannot control which batch is consumed.
DISCONFIRMING_OBSERVATION: >
  A customer holding both soon-to-expire and long-dated points redeems some, and the batch consumed is not
  the one nearest to expiry, nor any other documented order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Hold both soon-to-expire and long-dated point batches for one customer, redeem a partial amount, and
  inspect which batch was drawn down.
```

## G08-LOYALTY-Q016

```yaml
QID: G08-LOYALTY-Q016
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A change to the programme's expiry policy, for example extending or removing expiry, applies to existing
  balances according to a stated rule, rather than leaving it ambiguous whether already-aging points are
  covered.
WHY_IT_MATTERS: >
  Ambiguity about whether a policy change reaches existing balances leaves both the business and the
  customer unable to say what will actually happen to points already held.
DISCONFIRMING_OBSERVATION: >
  Changing the programme's expiry policy produces no determinable answer for whether an existing,
  already-aging balance is covered by the new policy or the old one.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Hold an aging balance under one expiry policy, change the policy, and determine which policy governs
  that balance going forward.
```

## G08-LOYALTY-Q017

```yaml
QID: G08-LOYALTY-Q017
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A single-use coupon that has already been redeemed on one order cannot be applied a second time on a
  different order for the same customer.
WHY_IT_MATTERS: >
  A coupon that can be reused defeats its own configured limit, and any promotion that relies on single use
  cannot be trusted to cost what it was designed to cost.
DISCONFIRMING_OBSERVATION: >
  A single-use coupon already redeemed on one completed order is successfully applied again to a second
  order for the same customer.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Redeem a single-use coupon on one order, then attempt to apply the same coupon to a second order for the
  same customer.
```

## G08-LOYALTY-Q018

```yaml
QID: G08-LOYALTY-Q018
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two orders for the same customer, each attempting to apply the same single-use coupon at effectively the
  same time, result in exactly one order successfully carrying the discount, not both.
WHY_IT_MATTERS: >
  A race condition that lets a single-use coupon apply twice under concurrent load costs the business the
  discount's full value on an order it was never configured to cover.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous orders for the same customer both successfully apply the same single-use coupon.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit two near-simultaneous orders for the same customer, both attempting to apply the same single-use
  coupon, and inspect the outcome of each.
```

## G08-LOYALTY-Q019

```yaml
QID: G08-LOYALTY-Q019
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A coupon consumed by an order that is later cancelled before completion is returned to a usable state, or
  explicitly not per a defined rule, rather than being left in an ambiguous state that is neither usable
  nor recorded as spent.
WHY_IT_MATTERS: >
  An ambiguous coupon state after cancellation leaves neither the customer nor support staff able to say
  whether the coupon can still be used.
DISCONFIRMING_OBSERVATION: >
  A coupon consumed by a subsequently cancelled order shows a state that is neither usable nor recorded as
  consumed, with no rule governing which it should be.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Consume a coupon on an order, cancel that order before completion, and inspect the coupon's resulting
  state.
```

## G08-LOYALTY-Q020

```yaml
QID: G08-LOYALTY-Q020
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A multi-use coupon's usage count is decremented in a way that is safe against being applied by several
  concurrent orders at once, so that its configured usage limit is not exceeded through concurrent
  redemption.
WHY_IT_MATTERS: >
  A usage limit that concurrency can bypass is not really a limit, and a promotion capped for cost-control
  reasons could be redeemed well past its intended ceiling.
DISCONFIRMING_OBSERVATION: >
  Several near-simultaneous orders redeeming the same multi-use coupon, together exceeding its configured
  usage limit, all succeed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Configure a multi-use coupon with a small usage limit and submit more near-simultaneous redemptions than
  the limit allows.
```
## G08-LOYALTY-Q021

```yaml
QID: G08-LOYALTY-Q021
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A coupon issued specifically to one customer cannot be successfully applied to an order placed by a
  different customer.
WHY_IT_MATTERS: >
  A customer-restricted coupon that anyone can redeem defeats the purpose of targeting it, and any cost
  control or personalised offer built on that restriction fails silently.
DISCONFIRMING_OBSERVATION: >
  A coupon restricted to one customer is successfully applied to an order placed by a different customer.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Issue a coupon restricted to one customer, then attempt to apply it to an order placed by a different
  customer.
```

## G08-LOYALTY-Q022

```yaml
QID: G08-LOYALTY-Q022
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A coupon with no customer restriction at all is distinguishable, in its configuration, from one restricted
  to a specific customer, so the two cannot be confused when a coupon code is shared or guessed.
WHY_IT_MATTERS: >
  If the two configurations look the same, staff cannot tell, when investigating a complaint, whether a
  coupon was ever supposed to be restricted in the first place.
DISCONFIRMING_OBSERVATION: >
  Inspecting a coupon's configuration gives no indication of whether it was ever intended to be restricted
  to a specific customer.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure one unrestricted coupon and one customer-restricted coupon and compare what each configuration
  shows.
```

## G08-LOYALTY-Q023

```yaml
QID: G08-LOYALTY-Q023
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An attempt to apply a customer-restricted coupon under the wrong customer produces a visible rejection
  rather than silently ignoring the coupon with no explanation of why the discount did not apply.
WHY_IT_MATTERS: >
  A silent rejection leaves the person applying the coupon unable to tell a restriction failure apart from
  an unrelated configuration or data problem.
DISCONFIRMING_OBSERVATION: >
  Applying a customer-restricted coupon to the wrong customer's order produces no discount and no visible
  indication of why it was not applied.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Attempt to apply a customer-restricted coupon to an order for a different customer and observe what is
  shown.
```

## G08-LOYALTY-Q024

```yaml
QID: G08-LOYALTY-Q024
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A coupon code's restriction to a specific customer survives that customer's account being edited, such as
  their name or contact details changing, without the restriction silently loosening or being lost.
WHY_IT_MATTERS: >
  A restriction that can be lost through an unrelated, routine account edit is not a reliable control at
  all.
DISCONFIRMING_OBSERVATION: >
  Editing a customer's name or contact details causes a coupon previously restricted to that customer to
  become usable by others, or to lose its restriction.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Issue a customer-restricted coupon, edit that customer's account details, and re-check the coupon's
  restriction.
```

## G08-LOYALTY-Q025

```yaml
QID: G08-LOYALTY-Q025
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When more than one reward or coupon could apply to the same order, whether they are allowed to stack is a
  defined, configurable rule, not an unstated default that differs by which two rewards happen to be
  involved.
WHY_IT_MATTERS: >
  An unstated stacking default produces unpredictable, uncontrolled discount combinations that no one
  configured on purpose and that can silently exceed intended promotional cost.
DISCONFIRMING_OBSERVATION: >
  Two different pairs of rewards, both eligible on comparable orders, are allowed to stack in one case and
  blocked in another with no configuration distinguishing the two pairs.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure two different pairs of simultaneously eligible rewards and compare whether each pair is allowed
  to stack.
```

## G08-LOYALTY-Q026

```yaml
QID: G08-LOYALTY-Q026
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Where stacking is allowed, the order in which multiple rewards are applied to the order's total is
  defined and consistent, since applying a percentage reward before or after a fixed-amount reward produces
  different results.
WHY_IT_MATTERS: >
  An undefined application order makes the final discounted total unpredictable and unreproducible for the
  same combination of rewards from one order to the next.
DISCONFIRMING_OBSERVATION: >
  The same combination of a percentage reward and a fixed-amount reward, applied to comparable orders,
  produces different final totals depending on an application order that is not documented or consistent.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply the same combination of a percentage reward and a fixed-amount reward to two comparable orders and
  compare the resulting totals.
```

## G08-LOYALTY-Q027

```yaml
QID: G08-LOYALTY-Q027
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where stacking is not allowed, an order eligible for more than one reward resolves to exactly one applied
  reward through a defined precedence rule, not an arbitrary or unrecorded pick.
WHY_IT_MATTERS: >
  An unrecorded pick among competing rewards means the outcome cannot be explained to a customer who asks
  why one reward, and not a more valuable one, was applied.
DISCONFIRMING_OBSERVATION: >
  An order eligible for more than one non-stacking reward has one applied with no record of the precedence
  rule that selected it over the alternatives.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Construct an order eligible for more than one non-stacking reward and inspect what the order records
  about which one was selected and why.
```

## G08-LOYALTY-Q028

```yaml
QID: G08-LOYALTY-Q028
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A reward or coupon rejected because stacking is not allowed is reported to the person applying it, with
  the reason, rather than silently failing to apply with no indication that another reward already in
  effect is the cause.
WHY_IT_MATTERS: >
  A silent stacking rejection looks identical to an unrelated failure, wasting time chasing the wrong cause
  and leaving the customer unclear about why a coupon "did not work".
DISCONFIRMING_OBSERVATION: >
  Attempting to apply a second, non-stackable reward to an order that already carries one produces no
  discount and no indication that a stacking rule, rather than something else, is the reason.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Apply one reward to an order, then attempt to apply a second, non-stackable reward, and observe what is
  reported.
```

## G08-LOYALTY-Q029

```yaml
QID: G08-LOYALTY-Q029
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward whose face value exceeds the value of the order it is applied to is handled by a defined rule,
  capped at the order value or a partial value forfeited, rather than producing a negative order total.
WHY_IT_MATTERS: >
  A negative order total is not a coherent commercial state and would corrupt anything computed downstream
  from the order's value.
DISCONFIRMING_OBSERVATION: >
  Applying a reward whose face value exceeds the order's value produces an order total below zero.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a reward with a face value greater than the order's total value and inspect the resulting order
  total.
```

## G08-LOYALTY-Q030

```yaml
QID: G08-LOYALTY-Q030
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether the unused portion of a reward that exceeds the order's value is forfeited or preserved for a
  future order is a defined, configurable rule, not an unstated default.
WHY_IT_MATTERS: >
  An unstated default for the unused portion cannot be communicated to the customer as a promise one way or
  the other, and could be applied inconsistently between customers.
DISCONFIRMING_OBSERVATION: >
  Two customers, each applying an equivalent oversized reward to a comparably small order, are left with
  different outcomes for the unused portion with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply an equivalent oversized reward for two customers on comparably small orders and compare what
  happens to each unused portion.
```

## G08-LOYALTY-Q031

```yaml
QID: G08-LOYALTY-Q031
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward capped down to fit an order's value records what the reward's full face value actually was, not
  only the capped amount actually applied, so the difference is not lost from the record.
WHY_IT_MATTERS: >
  Without the original face value on record, no one can later tell how much of the reward's value was
  actually forfeited to the cap versus genuinely used.
DISCONFIRMING_OBSERVATION: >
  A reward capped down to an order's value shows only the capped, applied amount on the order's record,
  with the reward's original face value not retrievable anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply an oversized reward that gets capped to an order's value and inspect whether the original face
  value remains retrievable.
```

## G08-LOYALTY-Q032

```yaml
QID: G08-LOYALTY-Q032
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a customer's programme membership and point balance are shared across companies in a multi-company
  setup, or held separately per company, is a defined, configurable rule, not an implicit behaviour that
  differs by which report is consulted.
WHY_IT_MATTERS: >
  Two different answers to "what is this customer's balance" depending on which report is used makes the
  programme's own numbers internally inconsistent.
DISCONFIRMING_OBSERVATION: >
  Two different reports on the same customer's balance in a multi-company setup disagree on whether
  activity from a second company is included, with no configuration explaining which is correct.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  In a multi-company setup, accrue points for a customer under more than one company and compare what two
  different balance views report.
```

## G08-LOYALTY-Q033

```yaml
QID: G08-LOYALTY-Q033
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Points earned under one company's programme are not silently redeemable against an order raised under a
  different company unless the configuration explicitly allows cross-company sharing.
WHY_IT_MATTERS: >
  Unintended cross-company redemption lets one company's promotional cost be paid by another company's
  order without either company having agreed to that arrangement.
DISCONFIRMING_OBSERVATION: >
  A customer redeems points earned under one company against an order raised under a different company, with
  no configuration explicitly permitting cross-company sharing.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Earn points for a customer under one company, then attempt to redeem them against an order raised under a
  different company with cross-company sharing not configured.
```

## G08-LOYALTY-Q034

```yaml
QID: G08-LOYALTY-Q034
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A customer's single combined point balance, where cross-company sharing is configured, is still
  decomposable by which company's activity earned each portion, for reconciliation between companies.
WHY_IT_MATTERS: >
  Without decomposability, two companies sharing one reward programme cannot reconcile which of them is
  responsible for which portion of the outstanding liability.
DISCONFIRMING_OBSERVATION: >
  A customer's combined balance across companies cannot be broken down by which company's activity earned
  each portion.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Accrue a combined, cross-company-shared balance for a customer and attempt to decompose it by
  earning company.
```

## G08-LOYALTY-Q035

```yaml
QID: G08-LOYALTY-Q035
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Disabling the reward programme for one company in a multi-company setup does not silently affect the balance or
  activity a customer has accrued under a different, still-active company.
WHY_IT_MATTERS: >
  A cross-company side effect from disabling one company's programme punishes customers of an unrelated,
  still-active company for a decision that had nothing to do with them.
DISCONFIRMING_OBSERVATION: >
  Disabling the reward programme for one company changes the balance or accrual behaviour recorded under a different,
  still-active company for a shared customer.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Accrue balances for a customer under two companies, disable the reward programme for one company, and inspect the
  other company's balance and accrual afterward.
```

## G08-LOYALTY-Q036

```yaml
QID: G08-LOYALTY-Q036
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When two customer records are merged into one, the resulting record's point balance is the deliberate
  sum, or other defined outcome, of both prior balances, not simply whichever record happened to survive
  the merge.
WHY_IT_MATTERS: >
  A merge that silently discards one side's balance takes value away from the customer with no decision
  behind it other than which record identifier happened to be kept.
DISCONFIRMING_OBSERVATION: >
  Merging two customer records, each holding a nonzero point balance, produces a surviving balance equal to
  only one side's original balance with no accounting for the other.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Give two customer records nonzero, distinguishable point balances, merge them, and inspect the resulting
  balance.
```
## G08-LOYALTY-Q037

```yaml
QID: G08-LOYALTY-Q037
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Merging two customer records with an active coupon issued to each preserves both coupons' usability under
  the surviving record, rather than silently dropping one.
WHY_IT_MATTERS: >
  A dropped coupon after a routine data-hygiene merge removes value the customer was entitled to for a
  reason unrelated to the coupon itself.
DISCONFIRMING_OBSERVATION: >
  Merging two customer records, each holding a distinct active coupon, leaves only one of the two coupons
  usable under the surviving record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Issue a distinct active coupon to each of two customer records, merge the records, and check the
  usability of both coupons afterward.
```

## G08-LOYALTY-Q038

```yaml
QID: G08-LOYALTY-Q038
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A merge of two customer records is itself a traceable event in the point history, distinguishable from
  an ordinary balance adjustment, so a reviewer can see that a balance changed because of a merge and not
  some other cause.
WHY_IT_MATTERS: >
  A balance change that cannot be told apart from an ordinary adjustment is indistinguishable, on later
  review, from an error or an unauthorised change.
DISCONFIRMING_OBSERVATION: >
  A customer's point history shows a balance change resulting from a record merge with no indication that a
  merge, rather than an ordinary adjustment, was the cause.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge two customer records with nonzero balances and inspect the resulting entry in the surviving
  record's point history.
```

## G08-LOYALTY-Q039

```yaml
QID: G08-LOYALTY-Q039
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  If the two merged customers' balances carry point batches with different expiry dates, the surviving
  record preserves each batch's own original expiry rather than collapsing them to one date that changes
  when some of the points actually expire.
WHY_IT_MATTERS: >
  Collapsing distinct expiry dates into one either expires points early that the customer should still have
  had, or extends points that should already have lapsed, in neither case matching the original grant.
DISCONFIRMING_OBSERVATION: >
  Merging two customer records whose point batches carry different expiry dates results in a surviving
  record where all points now share a single expiry date.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Give two customer records point batches with distinct expiry dates, merge them, and inspect the expiry
  dates on the surviving record.
```

## G08-LOYALTY-Q040

```yaml
QID: G08-LOYALTY-Q040
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A manual adjustment to a customer's point balance is a distinct, logged action, attributable to the
  person who made it, rather than indistinguishable from balance changes that occur through ordinary order
  activity.
WHY_IT_MATTERS: >
  A manual adjustment that looks the same as an ordinary earn or redemption entry cannot be singled out for
  review, audit, or investigation of a disputed balance.
DISCONFIRMING_OBSERVATION: >
  A manual balance adjustment appears in a customer's point history with no indication that it was manual,
  nor of who made it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform a manual adjustment to a customer's point balance and inspect the resulting history entry.
```

## G08-LOYALTY-Q041

```yaml
QID: G08-LOYALTY-Q041
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A manual adjustment to a customer's point balance requires a stated reason to be recorded alongside it,
  rather than being possible with no explanation retrievable later.
WHY_IT_MATTERS: >
  A reasonless adjustment cannot be defended to a customer or an auditor who asks why their balance changed
  outside of ordinary order activity.
DISCONFIRMING_OBSERVATION: >
  A manual balance adjustment is successfully recorded with no reason field populated or required.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Attempt a manual balance adjustment without supplying a reason and observe whether it is accepted.
```

## G08-LOYALTY-Q042

```yaml
QID: G08-LOYALTY-Q042
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  The ability to manually adjust a customer's point balance is governed by a permission distinct from the
  permission needed to process ordinary orders, rather than available to anyone who can view a customer's
  account.
WHY_IT_MATTERS: >
  Unrestricted adjustment ability lets any order-taker grant themselves or others value with no
  accountability distinct from ordinary order handling.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary order-processing permission is able to manually adjust a customer's point
  balance with no separate permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user holding only ordinary order-processing permission, attempt a manual point balance adjustment.
```

## G08-LOYALTY-Q043

```yaml
QID: G08-LOYALTY-Q043
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A manual balance adjustment can itself be reversed or corrected through a further traceable action,
  rather than the only way to undo a mistaken adjustment being an untracked second adjustment
  indistinguishable from the first.
WHY_IT_MATTERS: >
  Without a traceable reversal path, correcting a mistaken adjustment leaves behind a history that looks
  like two unrelated, unexplained changes rather than one mistake and its fix.
DISCONFIRMING_OBSERVATION: >
  Correcting a mistaken manual adjustment leaves no record connecting the correction to the adjustment it
  was meant to fix.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Make a manual balance adjustment, then correct it, and inspect whether the correction is linked to the
  original adjustment in the record.
```

## G08-LOYALTY-Q044

```yaml
QID: G08-LOYALTY-Q044
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A coupon code that has been deliberately deactivated or has reached its overall usage limit is rejected at
  the point of application with a clear reason, rather than accepted and only failing silently to produce
  any discount.
WHY_IT_MATTERS: >
  A silent failure to discount, with the coupon apparently accepted, misleads the customer or operator into
  believing the coupon should have worked.
DISCONFIRMING_OBSERVATION: >
  A deactivated or usage-exhausted coupon code is accepted as entered, with no discount applied and no
  reason given for its absence.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Deactivate a coupon, or exhaust its usage limit, and attempt to apply it to a new order.
```

## G08-LOYALTY-Q045

```yaml
QID: G08-LOYALTY-Q045
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two concurrent redemptions of points from the same customer's balance, for example from two devices or
  two open sessions, cannot together draw the balance below zero.
WHY_IT_MATTERS: >
  A balance that can go negative through concurrent redemption grants a customer more value than they ever
  actually held, at the business's cost.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous redemptions against the same customer's balance, together exceeding what the
  balance held, both succeed and leave the balance negative.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit two near-simultaneous point redemptions for the same customer that together exceed the available
  balance, and inspect the outcome.
```

## G08-LOYALTY-Q046

```yaml
QID: G08-LOYALTY-Q046
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A customer's own visibility into their point balance and history is available without requiring
  staff-level access to the underlying programme configuration.
WHY_IT_MATTERS: >
  Tying ordinary balance visibility to staff-level configuration access either exposes configuration to
  customers or denies them a basic view of their own balance.
DISCONFIRMING_OBSERVATION: >
  A customer attempting to view their own point balance and history is unable to do so without also being
  granted access to programme configuration.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  As a customer with no staff-level access, attempt to view your own point balance and history.
```

## G08-LOYALTY-Q047

```yaml
QID: G08-LOYALTY-Q047
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Viewing another customer's point balance or coupon history requires a permission distinct from the
  permission needed to process that customer's order, so that balance visibility is not an incidental side
  effect of ordinary order handling.
WHY_IT_MATTERS: >
  If order-processing access alone reveals a customer's full point balance and coupon history, every staff member who ever
  takes an order gains visibility never intended for that role.
DISCONFIRMING_OBSERVATION: >
  A user with only order-processing permission for a customer is also able to view that customer's full
  point balance and coupon history with no separate permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user holding only order-processing permission for a given customer, attempt to view that customer's
  point balance and coupon history.
```

## G08-LOYALTY-Q048

```yaml
QID: G08-LOYALTY-Q048
MODULE: loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A coupon's validity window, its start and end date, is enforced consistently regardless of the channel or
  interface through which it is applied, so the same coupon does not appear valid on one channel and
  invalid on another at the same moment.
WHY_IT_MATTERS: >
  Inconsistent enforcement across channels lets the same coupon be exploited through whichever channel
  enforces its window more loosely.
DISCONFIRMING_OBSERVATION: >
  The same coupon, at the same moment, is accepted as valid through one channel or interface and rejected
  as expired or not-yet-valid through another.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Attempt to apply the same coupon, near its validity window boundary, through two different channels or
  interfaces at the same moment.
```
