# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_loyalty Module Adversarial MVQ Bank (BRIDGE)

**Document ID:** GMVQ-G08-SALE_LOYALTY-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_loyalty`
**Wave:** W2
**Author Cell:** TEAM P-S2 (GMVQ Question Factory — Production Cell P-S2, Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This is a BRIDGE module per the Bridge Module Rule (V1.00): it owns almost no behaviour of its own and
exists only where a reward or coupon (the `loyalty` capability) is applied to a commercial order (the
`sale` capability) and the two must agree. Every question below fails the bridge test only at the seam —
each one would stop making sense if the reward were removed and the order stood alone, or if the reward
were evaluated with no order to apply it to. Ground covered: the discount line's tax treatment and which
lines it reduces; recomputation when the order changes after the reward was applied; a reward valid at
quotation but not at confirmation; margin after a reward and its visibility to the salesperson; a reward's
value on a partially delivered or partially invoiced order; reversal of a reward on cancellation and
whether points or coupons come back; and two rewards competing for one line.

This bank does not re-ask `loyalty`'s own ground (the programme, its rates, its liability, its expiry
policy, its cross-company scoping, its merge behaviour) or `delivery`'s own ground (the commercial shipping
charge on its own terms) — both authored separately in this same batch. It also does not encroach on
`sale_loyalty_delivery`'s ground: where a reward's target is shipping specifically, that narrower seam is
this bridge's own child bridge, authored separately.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  capability, business rule, state transition, configuration dependency, role/permission, exception path,
  cancellation, reversal, negative case, auditability, concurrency and ordering.
- Bridge Module Rule §5 pre-authoring check: `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md` was run
  against `G08_DELIVERY_GMVQ_MVQ_48_V1.00_DRAFT.md` and `G08_LOYALTY_GMVQ_MVQ_48_V1.00_DRAFT.md`, both
  authored earlier in this same batch. No question below restates either base bank's ground; each one
  requires both an order and a reward to exist simultaneously and interact.
- Bridge Module Rule §2 test applied to every question: if the reward were removed and the order stood
  alone, or the reward existed with no order to apply to, would the question still make sense? Every
  question below fails that test — it is a seam question.
- LAYER is mostly `PROCESS` for this bridge, since almost all seam behaviour is runtime interaction; the
  small number of precedence/allocation configuration questions are tagged `LAYER: BASE`.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a
  Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_LOYALTY-Q001

```yaml
QID: G08-SALE_LOYALTY-Q001
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Whether a reward's discount is applied before or after tax computation on the lines it reduces is a
  defined, consistent rule, not a behaviour that differs by which reward happens to be involved.
WHY_IT_MATTERS: >
  A tax basis that shifts depending on which reward is in play produces a tax figure that cannot be
  defended as following one consistent rule.
DISCONFIRMING_OBSERVATION: >
  Two comparable rewards applied to comparable orders reduce the tax basis of their target lines
  differently, before tax in one case and after in the other, with no configuration explaining why.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Apply two different rewards, each to a comparable order and line, and compare whether the tax basis is
  reduced before or after tax in each case.
```

## G08-SALE_LOYALTY-Q002

```yaml
QID: G08-SALE_LOYALTY-Q002
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a reward's discount targets specific lines or the order total generally is determined by the
  reward's own configuration and is reflected consistently in how the discount is allocated on the order.
WHY_IT_MATTERS: >
  An untargeted allocation for a reward configured to target specific lines misrepresents which goods
  actually carried the discount, which matters for any later per-line reconciliation.
DISCONFIRMING_OBSERVATION: >
  A reward configured to target specific lines is instead allocated as a generic reduction across the whole
  order total with no relationship to the targeted lines.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a reward to target specific lines, apply it to a multi-line order, and inspect how the discount
  is actually allocated.
```

## G08-SALE_LOYALTY-Q003

```yaml
QID: G08-SALE_LOYALTY-Q003
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a reward's discount is allocated proportionally across multiple lines, the tax on each line is
  recomputed to reflect its share of the discount, not left showing the pre-discount tax amount.
WHY_IT_MATTERS: >
  Tax left uncorrected after a proportional discount overstates the tax due on each affected line, an
  exposure that scales with every order the reward touches.
DISCONFIRMING_OBSERVATION: >
  A reward allocated proportionally across several lines leaves each line's tax amount identical to what it
  was before the discount was allocated.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a reward that allocates proportionally across multiple taxed lines and inspect the tax amount on
  each line before and after.
```

## G08-SALE_LOYALTY-Q004

```yaml
QID: G08-SALE_LOYALTY-Q004
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A reward targeted at one specific line does not silently reduce the price or tax basis of untargeted
  lines on the same order.
WHY_IT_MATTERS: >
  A reward that bleeds into lines it was never configured to touch gives away margin on goods the
  promotion was never meant to cover.
DISCONFIRMING_OBSERVATION: >
  Applying a reward targeted at one specific line changes the price or tax basis of a different, untargeted
  line on the same order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a reward targeted at one specific line on a multi-line order and inspect whether any other line's
  price or tax basis changed.
```

## G08-SALE_LOYALTY-Q005

```yaml
QID: G08-SALE_LOYALTY-Q005
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  When a reward reduces the order total generically on an order whose lines carry different tax rates, how
  the reduction is allocated across those differently-taxed lines for tax purposes is a defined,
  documented rule.
WHY_IT_MATTERS: >
  An undefined allocation across mixed tax rates produces a tax result that cannot be reproduced or
  defended, since the same total discount could be split in many different ways with different tax
  outcomes.
DISCONFIRMING_OBSERVATION: >
  Applying the same generic-total reward to two orders with an identical total but a different mix of tax
  rates across lines produces tax allocations that cannot be traced to any documented rule.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Apply a generic order-total reward to two orders with the same total value but different tax-rate line
  mixes and compare the resulting tax allocation.
```

## G08-SALE_LOYALTY-Q006

```yaml
QID: G08-SALE_LOYALTY-Q006
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The discount from a reward is shown as a distinct commercial line item, not folded silently into a
  modified list price on the lines it reduces, so the original list price remains visible.
WHY_IT_MATTERS: >
  A silently modified list price hides from the customer and from internal review what was actually
  charged versus what the reward actually gave away.
DISCONFIRMING_OBSERVATION: >
  Applying a reward changes a line's displayed unit price with no separate discount line, so the original
  list price is no longer visible anywhere on the order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a reward to an order line and inspect whether the original list price and the discount remain
  separately visible.
```

## G08-SALE_LOYALTY-Q007

```yaml
QID: G08-SALE_LOYALTY-Q007
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A line reduced to zero by a reward is distinguishable, on the order, from a line that was genuinely
  priced at zero independent of any reward.
WHY_IT_MATTERS: >
  Indistinguishable zero-price lines make it impossible to later audit how many zero-value lines actually
  originated from a reward versus a deliberate free-goods pricing decision.
DISCONFIRMING_OBSERVATION: >
  A line reduced to zero by a reward and a line independently priced at zero show identically, with no way
  to tell them apart on the order's own record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create one line reduced to zero by a reward and one line independently priced at zero, and compare their
  records.
```

## G08-SALE_LOYALTY-Q008

```yaml
QID: G08-SALE_LOYALTY-Q008
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a line the reward's discount was allocated to is removed after the reward was applied, the reward
  re-evaluates rather than leaving a discount allocated to a line that no longer exists.
WHY_IT_MATTERS: >
  A discount left attached to a deleted line either vanishes without accounting for it or persists as an
  orphaned reduction the order can no longer explain.
DISCONFIRMING_OBSERVATION: >
  Removing the line a reward's discount was allocated to leaves the order's total reduced by that discount
  with no remaining line it is attributed to.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a reward targeted at a specific line, remove that line from the order, and inspect the reward's
  state and the order total.
```

## G08-SALE_LOYALTY-Q009

```yaml
QID: G08-SALE_LOYALTY-Q009
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Adding new lines to an order after a reward has been applied does not silently expand the reward's
  effect onto goods that were not present when the reward was evaluated for eligibility.
WHY_IT_MATTERS: >
  An expanding reward that reaches goods added after the fact gives away discount on items the promotion
  was never evaluated against.
DISCONFIRMING_OBSERVATION: >
  Adding a new line to an order after a reward was applied causes that new line to also receive the
  reward's discount with no fresh eligibility check.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a reward to an order, then add a new line, and inspect whether the new line receives the reward's
  effect.
```

## G08-SALE_LOYALTY-Q010

```yaml
QID: G08-SALE_LOYALTY-Q010
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If removing lines drops the order below a reward's minimum qualifying condition, the reward is removed or
  flagged, not left applied to an order that would no longer qualify for it.
WHY_IT_MATTERS: >
  A reward that survives past the point where the order no longer earns it is an unrecovered promotional
  cost repeated across every order edited downward.
DISCONFIRMING_OBSERVATION: >
  Removing lines drops an order below a reward's minimum qualifying condition, and the reward remains
  applied and in effect.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Qualify an order for a reward with a minimum condition, remove lines to fall below that minimum, and
  re-inspect the reward's state.
```

## G08-SALE_LOYALTY-Q011

```yaml
QID: G08-SALE_LOYALTY-Q011
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Changing a line's quantity after a percentage-based reward was applied recomputes the discount amount
  proportionally, rather than the discount amount staying fixed at its original figure.
WHY_IT_MATTERS: >
  A fixed discount amount left over from a since-changed quantity either overcharges or undercharges the
  customer relative to what the percentage reward was meant to give.
DISCONFIRMING_OBSERVATION: >
  Increasing or decreasing a line's quantity after a percentage-based reward was applied leaves the
  discount amount unchanged from before the quantity change.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a percentage-based reward to a line, then change that line's quantity, and inspect whether the
  discount amount is recomputed.
```

## G08-SALE_LOYALTY-Q012

```yaml
QID: G08-SALE_LOYALTY-Q012
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward re-evaluation triggered by an order change is itself visible on the order as a recorded
  recalculation, not merely a silent number change with no trace of the recompute event.
WHY_IT_MATTERS: >
  A silent recompute is indistinguishable from an unexplained data error when the discount amount on an
  order changes with no visible cause.
DISCONFIRMING_OBSERVATION: >
  A reward's discount amount changes after an order edit, and the order's own record shows no trace that a
  recompute occurred or why.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a reward recomputation through an order edit and inspect the order's record for a trace of the
  recompute event.
```

## G08-SALE_LOYALTY-Q013

```yaml
QID: G08-SALE_LOYALTY-Q013
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When an order change causes a reward to no longer be eligible and it is removed, the order total is
  recalculated without the discount, rather than leaving a phantom net reduction with no reward attached to
  it.
WHY_IT_MATTERS: >
  A phantom reduction with no attached reward silently understates what the customer should be charged, and
  cannot be explained if questioned.
DISCONFIRMING_OBSERVATION: >
  A reward is removed for no-longer-being-eligible, but the order total remains as reduced as it was while
  the reward was still applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cause a reward to become ineligible through an order edit, allow it to be removed, and inspect whether
  the order total is recalculated accordingly.
```

## G08-SALE_LOYALTY-Q014

```yaml
QID: G08-SALE_LOYALTY-Q014
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Two rewards applied to an order that individually would recompute differently on the same line change are
  each recomputed independently and correctly, not only the most recently applied one.
WHY_IT_MATTERS: >
  A recompute that only reaches the most recently applied reward leaves the other silently stale, producing
  a total that reflects neither reward's true, current effect.
DISCONFIRMING_OBSERVATION: >
  A line change that should affect two previously applied rewards' discount amounts only updates the more
  recently applied one, leaving the other unchanged.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply two rewards that each depend on the same line, change that line, and inspect whether both rewards'
  discount amounts are recomputed.
```

## G08-SALE_LOYALTY-Q015

```yaml
QID: G08-SALE_LOYALTY-Q015
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward applied at quotation that has expired by the time the order is confirmed is caught and removed
  or flagged before confirmation, not silently carried through as if still valid.
WHY_IT_MATTERS: >
  An expired reward honoured through confirmation gives away a discount past the point the business intended
  to offer it, with no check catching the lapse.
DISCONFIRMING_OBSERVATION: >
  An order confirms successfully carrying a reward that expired between quotation and confirmation, with no
  flag or removal.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Apply a reward to a quotation, let its validity lapse before confirmation, and attempt to confirm the
  order.
```

## G08-SALE_LOYALTY-Q016

```yaml
QID: G08-SALE_LOYALTY-Q016
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward applied at quotation whose eligibility condition is no longer met at confirmation, because the
  order shrank in between, is re-evaluated rather than honoured on the strength of having once qualified.
WHY_IT_MATTERS: >
  Honouring a reward the order no longer actually earns is an unrecovered promotional cost that recurs
  every time an order is edited down before confirming.
DISCONFIRMING_OBSERVATION: >
  An order that no longer meets a reward's eligibility condition at confirmation, having shrunk since
  quotation, still confirms carrying that reward.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Apply a reward to a quotation, shrink the order below the reward's eligibility condition, and attempt to
  confirm.
```

## G08-SALE_LOYALTY-Q017

```yaml
QID: G08-SALE_LOYALTY-Q017
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A coupon applied at quotation that reaches its own overall usage limit, consumed by a different order,
  before this order confirms is re-checked at confirmation, not assumed still available because it was
  accepted earlier.
WHY_IT_MATTERS: >
  Skipping the re-check lets a usage-limited coupon be honoured on more orders than its limit allows,
  purely because of the order in which two quotations happened to confirm.
DISCONFIRMING_OBSERVATION: >
  A coupon that has reached its usage limit through a different order confirms successfully on this order,
  which applied it earlier at quotation, with no re-check at confirmation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Apply a usage-limited coupon at quotation on order A, exhaust its limit through order B, then attempt to
  confirm order A.
```

## G08-SALE_LOYALTY-Q018

```yaml
QID: G08-SALE_LOYALTY-Q018
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Confirmation of an order carrying a reward that is no longer valid produces a visible resolution path,
  either dropping the reward or blocking confirmation, rather than confirming silently with an invalid
  reward still applied.
WHY_IT_MATTERS: >
  A silent confirmation with an invalid reward leaves both the customer and the business unaware that the
  applied discount should never have gone through.
DISCONFIRMING_OBSERVATION: >
  Confirming an order carrying a now-invalid reward proceeds with no indication that the reward's validity
  was ever in question.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Reproduce a reward-invalid-at-confirmation state and inspect what the order presents at confirmation.
```

## G08-SALE_LOYALTY-Q019

```yaml
QID: G08-SALE_LOYALTY-Q019
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward that becomes invalid between quotation and confirmation, and is consequently removed, leaves a
  retrievable record that it was once applied and why it was removed.
WHY_IT_MATTERS: >
  Without a retrievable record, a customer asking why a discount they saw at quotation is missing at
  confirmation cannot be given an explanation from the order itself.
DISCONFIRMING_OBSERVATION: >
  A reward removed between quotation and confirmation for having become invalid leaves no trace on the
  order that it was ever applied or why it was removed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Let a reward applied at quotation become invalid before confirmation, allow it to be removed, and inspect
  the order's record for a trace.
```

## G08-SALE_LOYALTY-Q020

```yaml
QID: G08-SALE_LOYALTY-Q020
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Re-quoting an order after a reward has lapsed offers a currently valid alternative reward, if the
  customer still qualifies for one, rather than simply dropping the benefit with no indication a substitute
  might exist.
WHY_IT_MATTERS: >
  Silently dropping the benefit with no substitute offered loses a commercial opportunity the business may
  still have wanted to extend to a qualifying customer.
DISCONFIRMING_OBSERVATION: >
  Re-quoting an order after its reward has lapsed drops the discount entirely with no check for, or mention
  of, any currently valid alternative the customer might still qualify for.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Let a reward lapse on an order that still qualifies for a different, currently valid reward, then requote
  the order.
```

## G08-SALE_LOYALTY-Q021

```yaml
QID: G08-SALE_LOYALTY-Q021
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A price list or general promotion's own end date is checked again at confirmation time even when it was
  already checked once at quotation time, so a promotion that ended in between does not survive into a
  confirmed order.
WHY_IT_MATTERS: >
  Checking a promotion's end date only once, at quotation, lets an order confirm on terms the business
  already withdrew before the order was actually committed.
DISCONFIRMING_OBSERVATION: >
  A promotion that ends between quotation and confirmation still applies to the order at confirmation
  because it was only checked once, at quotation.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Apply a promotion at quotation, let it end before confirmation, and attempt to confirm the order.
```
## G08-SALE_LOYALTY-Q022

```yaml
QID: G08-SALE_LOYALTY-Q022
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The margin figure computed for an order that carries a reward reflects the discounted realised revenue,
  not the pre-reward list price, since the business's actual margin is what it actually recovers.
WHY_IT_MATTERS: >
  A margin figure computed against the list price overstates profitability on every order carrying a reward,
  misleading anyone who relies on it to judge the business's real performance.
DISCONFIRMING_OBSERVATION: >
  An order carrying a reward shows a margin figure computed against its pre-reward list price rather than
  the actual discounted amount realised.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a reward to an order and compare the resulting margin figure against both the list price and the
  actual discounted realised revenue.
```

## G08-SALE_LOYALTY-Q023

```yaml
QID: G08-SALE_LOYALTY-Q023
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Whether a salesperson can see the margin impact of a reward they are applying is governed by a permission
  distinct from the permission needed to apply the reward itself, so a reward can be applied without
  necessarily exposing margin data to that role.
WHY_IT_MATTERS: >
  Tying margin visibility to the ability to apply a reward at all either blocks ordinary reward use for
  roles that should not see margin, or exposes margin to every role that can apply a discount.
DISCONFIRMING_OBSERVATION: >
  A role permitted to apply rewards is, purely by that permission, also able to see the order's margin
  figure with no separate permission governing that visibility.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a role permitted to apply rewards but not to view margin, apply a reward and attempt to view the
  resulting margin figure.
```

## G08-SALE_LOYALTY-Q024

```yaml
QID: G08-SALE_LOYALTY-Q024
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward's cost to margin is attributable specifically to the reward, distinguishable in the record from
  margin variance caused by any other pricing mechanism on the same order.
WHY_IT_MATTERS: >
  An unattributed margin reduction cannot be traced back to the reward that caused it when several pricing
  mechanisms act on the same order.
DISCONFIRMING_OBSERVATION: >
  An order's margin reduction from a reward cannot be distinguished, in the record, from margin variance
  caused by a different pricing mechanism also acting on the same order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Apply a reward alongside a different pricing mechanism on the same order and attempt to attribute the
  margin reduction to each individually.
```

## G08-SALE_LOYALTY-Q025

```yaml
QID: G08-SALE_LOYALTY-Q025
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Stacking two rewards on one order attributes the combined margin impact in a way that each reward's
  individual contribution to the margin reduction remains identifiable, not only a single combined figure.
WHY_IT_MATTERS: >
  A combined-only figure prevents evaluating whether either individual reward is, on its own, costing more
  margin than intended.
DISCONFIRMING_OBSERVATION: >
  Two stacked rewards on one order produce only a single combined margin-impact figure with no way to
  attribute the reduction between the two.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Stack two rewards on one order and attempt to identify each one's individual contribution to the margin
  reduction.
```

## G08-SALE_LOYALTY-Q026

```yaml
QID: G08-SALE_LOYALTY-Q026
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A role permitted to apply rewards but not to view margin can still see that a reward was applied and its
  face value, without that necessarily revealing the underlying cost basis the margin figure depends on.
WHY_IT_MATTERS: >
  If seeing a reward's face value is impossible without margin access, a role handling ordinary orders
  cannot even confirm which discount they applied.
DISCONFIRMING_OBSERVATION: >
  A role denied margin visibility is also unable to see the face value of a reward it applied to an order.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  As a role permitted to apply rewards but not view margin, apply a reward and attempt to see its face
  value on the order.
```

## G08-SALE_LOYALTY-Q027

```yaml
QID: G08-SALE_LOYALTY-Q027
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The margin visible to a salesperson, where permitted, at quotation time before a reward is finally
  confirmed as applied, is a live figure that reflects the reward's actual eventual impact, not a stale
  estimate calculated before the reward was chosen.
WHY_IT_MATTERS: >
  A stale margin estimate can mislead a salesperson into believing an order is more or less profitable than
  it will actually be once the reward the customer is asking for is applied.
DISCONFIRMING_OBSERVATION: >
  A salesperson's visible margin figure at quotation does not change after a reward is selected and
  applied, remaining at its pre-reward estimate.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  As a salesperson permitted to view margin, apply a reward at quotation and check whether the visible
  margin figure updates.
```

## G08-SALE_LOYALTY-Q028

```yaml
QID: G08-SALE_LOYALTY-Q028
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward applied and later reversed removes its effect from the margin figure to the same degree it once
  reduced it, not leaving a residual, unexplained margin discrepancy after the reversal.
WHY_IT_MATTERS: >
  A residual discrepancy after reversal means the order's margin can never fully return to what it should
  be once the reward is gone, corrupting any later profitability analysis of that order.
DISCONFIRMING_OBSERVATION: >
  Reversing a reward that reduced an order's margin leaves the margin figure short of what it would be had
  the reward never been applied at all.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a reward that reduces an order's margin, reverse the reward, and compare the resulting margin
  figure against the order's original, reward-free margin.
```

## G08-SALE_LOYALTY-Q029

```yaml
QID: G08-SALE_LOYALTY-Q029
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A reward applied to an order that is only partially delivered is allocated to the invoice in a way that is
  proportional to what was actually delivered and invoiced, not applied in full against a partial invoice
  for goods not yet shipped.
WHY_IT_MATTERS: >
  A reward applied in full against a partial invoice gives away more discount, sooner, than the order as a
  whole was ever meant to receive.
DISCONFIRMING_OBSERVATION: >
  A partial delivery and its corresponding partial invoice carry the reward's full, un-prorated value rather
  than a portion proportional to what was actually delivered.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a reward to an order, deliver and invoice only part of it, and inspect what portion of the reward's
  value the partial invoice carries.
```

## G08-SALE_LOYALTY-Q030

```yaml
QID: G08-SALE_LOYALTY-Q030
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When an order's invoicing policy invoices ahead of delivery, a reward's allocation across the invoices
  raised over time sums, across all of them, to the reward's originally agreed value, neither more nor
  less.
WHY_IT_MATTERS: >
  A reward that over- or under-allocates across a sequence of invoices either gives away more discount than
  agreed or shortchanges the customer relative to what was promised.
DISCONFIRMING_OBSERVATION: >
  The sum of a reward's allocated value across every invoice eventually raised on an order does not equal
  the reward's originally agreed value.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a reward to an order invoiced ahead of delivery across several invoices and sum the reward's
  allocated value across all of them.
```

## G08-SALE_LOYALTY-Q031

```yaml
QID: G08-SALE_LOYALTY-Q031
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a partially delivered order is never fully delivered, for example the remainder is cancelled, the
  reward's allocation to what was actually invoiced is settled to its correct final value rather than left
  based on an assumption of full future delivery.
WHY_IT_MATTERS: >
  A reward allocation left assuming a delivery that never happens either overcharges or undercharges the
  customer for what they actually received, and never gets corrected without an explicit settlement step.
DISCONFIRMING_OBSERVATION: >
  An order partially delivered and then permanently reduced by cancelling the remainder leaves its reward
  allocation still based on the originally planned full delivery.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially deliver and invoice an order carrying a reward, cancel the undelivered remainder, and inspect
  whether the reward's allocation is resettled.
```

## G08-SALE_LOYALTY-Q032

```yaml
QID: G08-SALE_LOYALTY-Q032
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward allocated proportionally across several partial invoices is traceable, from any one invoice,
  back to the single originating reward, rather than each partial allocation looking like an unrelated,
  independent discount.
WHY_IT_MATTERS: >
  An untraceable allocation makes it impossible to reconcile, from any single invoice, whether the reward's
  total agreed value has been correctly accounted for across the order.
DISCONFIRMING_OBSERVATION: >
  A partial invoice carrying a portion of a reward's value shows that portion with no link back to the
  originating reward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Allocate a reward across several partial invoices and inspect whether each invoice traces back to the
  originating reward.
```

## G08-SALE_LOYALTY-Q033

```yaml
QID: G08-SALE_LOYALTY-Q033
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The order in which partial invoices are raised does not change the total reward value eventually
  recognised across all of them, whichever invoice happens to be raised first.
WHY_IT_MATTERS: >
  A total reward value that depends on invoice sequencing is not a stable, predictable commercial figure and
  cannot be reconciled independent of operational timing.
DISCONFIRMING_OBSERVATION: >
  Raising the same set of partial invoices in a different order for two otherwise identical orders produces
  a different total reward value recognised across them.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Raise the same set of partial invoices in two different sequences on two comparable orders and compare
  the total reward value recognised.
```

## G08-SALE_LOYALTY-Q034

```yaml
QID: G08-SALE_LOYALTY-Q034
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A reward tied to a specific line is allocated only against invoices that actually include that line's
  delivered quantity, not spread across unrelated lines' partial invoices.
WHY_IT_MATTERS: >
  A reward that leaks onto unrelated lines' invoices misrepresents which goods actually carried the
  discount the reward was configured for.
DISCONFIRMING_OBSERVATION: >
  A reward tied to one specific line appears allocated against a partial invoice that does not include any
  quantity of that line.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a reward to one specific line on a multi-line order, invoice a different line's partial delivery,
  and inspect whether the reward is allocated there.
```

## G08-SALE_LOYALTY-Q035

```yaml
QID: G08-SALE_LOYALTY-Q035
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Rounding differences arising from allocating one reward's value across several partial invoices are
  resolved by a defined rule, for example adjusted on the final invoice, rather than silently accumulating
  an unexplained residual.
WHY_IT_MATTERS: >
  An unexplained residual left over from rounding is a small but permanent discrepancy that accumulates
  across every order invoiced in several parts.
DISCONFIRMING_OBSERVATION: >
  Allocating a reward's value across several partial invoices leaves a rounding residual with no defined
  rule accounting for where it is resolved.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Allocate a reward whose value does not divide evenly across several partial invoices and inspect how the
  rounding residual is resolved.
```

## G08-SALE_LOYALTY-Q036

```yaml
QID: G08-SALE_LOYALTY-Q036
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after a coupon was applied to it returns that coupon to a usable state, consistent
  with the loyalty programme's own single-use or multi-use rule, rather than leaving it permanently consumed
  for an order that never completed.
WHY_IT_MATTERS: >
  A coupon permanently lost to a cancelled order takes value away from the customer for a transaction that
  never actually happened.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order that consumed a coupon leaves the coupon permanently marked as used, with no
  restoration consistent with the programme's own reuse rule.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Apply a coupon to an order, cancel the order, and inspect the coupon's resulting usability.
```
## G08-SALE_LOYALTY-Q037

```yaml
QID: G08-SALE_LOYALTY-Q037
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after points were redeemed as a reward on it credits those points back to the
  customer's balance, unless a defined rule says otherwise, rather than leaving the customer's balance
  permanently reduced for a cancelled order.
WHY_IT_MATTERS: >
  A permanently reduced balance for a transaction that never completed takes value from the customer with
  no corresponding order to justify it.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order that redeemed points leaves the customer's balance reduced by that redemption with no
  credit back and no documented rule explaining why not.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Redeem points as a reward on an order, cancel the order, and inspect the customer's balance afterward.
```

## G08-SALE_LOYALTY-Q038

```yaml
QID: G08-SALE_LOYALTY-Q038
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A partial cancellation of an order that consumed a reward re-evaluates only the portion of the reward's
  effect attributable to what was cancelled, rather than an all-or-nothing reversal of the entire reward
  regardless of how much of the order survives.
WHY_IT_MATTERS: >
  An all-or-nothing reversal either strips a reward the surviving portion of the order still deserves, or
  leaves the full reward in effect on an order that has shrunk since it was earned.
DISCONFIRMING_OBSERVATION: >
  A partial cancellation of an order carrying a reward produces the same reward outcome, either fully kept
  or fully reversed, regardless of how much of the order was actually cancelled.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a reward to a multi-line order, partially cancel it, and inspect whether the reward's effect is
  re-evaluated proportionally.
```

## G08-SALE_LOYALTY-Q039

```yaml
QID: G08-SALE_LOYALTY-Q039
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Reversing a reward on cancellation is a traceable event connecting the reversal specifically to the
  cancellation that caused it, not indistinguishable from an unrelated, unexplained balance or coupon-state
  change.
WHY_IT_MATTERS: >
  An untraceable reversal cannot be told apart from an error when a customer or reviewer later asks why a
  balance or coupon state changed.
DISCONFIRMING_OBSERVATION: >
  A reward reversal caused by an order cancellation leaves no record connecting the reversal to that
  specific cancellation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel an order that triggers a reward reversal and inspect whether the reversal is linked to the
  cancellation in the record.
```

## G08-SALE_LOYALTY-Q040

```yaml
QID: G08-SALE_LOYALTY-Q040
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reward reversed because its order was cancelled, where the reward had a defined validity window, is
  returned in a state that respects whether that window has meanwhile lapsed, not restored as freshly valid
  regardless of its own expiry.
WHY_IT_MATTERS: >
  Restoring an already-expired reward as freshly valid extends a promotion past the point the business
  intended it to end, purely as a side effect of an unrelated cancellation.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order restores a reward to a usable state even though that reward's own validity window has
  since lapsed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply a reward with a validity window to an order, let the window lapse, cancel the order, and inspect
  the reward's restored state.
```

## G08-SALE_LOYALTY-Q041

```yaml
QID: G08-SALE_LOYALTY-Q041
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after a reward was applied and already contributed to a computed margin figure
  re-adjusts that margin figure to remove the reward's effect, consistent with the order's own cancellation.
WHY_IT_MATTERS: >
  A margin figure left reflecting a reward on a cancelled order misstates the profitability record of a
  transaction that no longer exists.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order that carried a reward leaves the previously computed margin figure unchanged,
  still reflecting the reward's effect.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Apply a reward that affects margin on an order, cancel the order, and inspect the resulting margin
  figure.
```

## G08-SALE_LOYALTY-Q042

```yaml
QID: G08-SALE_LOYALTY-Q042
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When two rewards were stacked on an order that is then cancelled, each reward's own reversal rule is
  applied to it individually, rather than one combined, undifferentiated reversal being applied to both.
WHY_IT_MATTERS: >
  A combined reversal cannot honour each reward's own distinct rule, for example a coupon that returns to
  usable state and points that do not, if the two are handled as one undifferentiated action.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order with two stacked rewards applies a single, identical reversal outcome to both,
  regardless of each reward's own individually configured reversal rule.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Stack two rewards with different reversal rules on one order, cancel the order, and inspect whether each
  reward is reversed according to its own rule.
```

## G08-SALE_LOYALTY-Q043

```yaml
QID: G08-SALE_LOYALTY-Q043
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  When two rewards each target the same specific line and stacking is not allowed between them, exactly one
  is applied to that line through a defined precedence rule, not an arbitrary pick that differs from one
  otherwise-identical order to the next.
WHY_IT_MATTERS: >
  An arbitrary pick between two competing rewards for the same line cannot be explained to a customer, or
  reproduced consistently for the same combination on a different order.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical orders, each eligible for the same two non-stackable line-targeted rewards, end up
  with different rewards applied to the line with no configuration explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Construct two otherwise-identical orders eligible for the same two non-stackable line-targeted rewards and
  compare which reward each applies.
```

## G08-SALE_LOYALTY-Q044

```yaml
QID: G08-SALE_LOYALTY-Q044
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When two rewards are both eligible to apply to the same line and stacking is allowed, the combined effect
  on that one line does not reduce it below a defined floor regardless of how the two combine.
WHY_IT_MATTERS: >
  An unbounded combination of two stacked rewards on one line could reduce it to zero or below, an outcome
  no single reward was configured to produce on its own.
DISCONFIRMING_OBSERVATION: >
  Stacking two eligible rewards on the same line reduces that line below the configured floor, or below
  zero, with no bound applied to the combination.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Stack two rewards whose combined face value exceeds a single line's value and inspect the resulting line
  amount against the configured floor.
```

## G08-SALE_LOYALTY-Q045

```yaml
QID: G08-SALE_LOYALTY-Q045
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A reward that targets a specific line and a separate reward that targets the order as a whole can coexist
  on the same order without one silently cancelling or overriding the other's intended scope.
WHY_IT_MATTERS: >
  One reward silently overriding another's scope produces a result neither reward was individually
  configured to produce, and denies the customer a benefit the business intended to grant.
DISCONFIRMING_OBSERVATION: >
  Applying a line-targeted reward alongside a separate order-wide reward causes one of the two to be
  silently dropped rather than both taking effect within their own intended scope.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Apply one line-targeted reward and one order-wide reward to the same order and inspect whether both take
  effect within their own scope.
```

## G08-SALE_LOYALTY-Q046

```yaml
QID: G08-SALE_LOYALTY-Q046
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Removing the higher-precedence of two competing rewards for a line, after the resolution has already been
  made, causes the line to fall back to the next eligible reward rather than being left with no reward at
  all despite one still being eligible.
WHY_IT_MATTERS: >
  Leaving the line with no reward, when a second one remains genuinely eligible, denies the customer a
  benefit the business's own rules say they should still receive.
DISCONFIRMING_OBSERVATION: >
  Removing the higher-precedence reward from a line that had a second, still-eligible reward leaves the line
  with no reward applied at all.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Resolve two competing rewards for a line in favour of one, remove that one, and inspect whether the line
  falls back to the remaining eligible reward.
```

## G08-SALE_LOYALTY-Q047

```yaml
QID: G08-SALE_LOYALTY-Q047
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Two coupons, each restricted to apply only to a specific line, that both target the very same line,
  resolve which one applies through the same defined precedence rule as two general rewards would, rather
  than an unhandled case with an unpredictable result.
WHY_IT_MATTERS: >
  An unhandled case for two coupons is still a real situation a customer can create, and an unpredictable
  result there is no more acceptable than for any other competing-reward scenario.
DISCONFIRMING_OBSERVATION: >
  Two line-targeted coupons both aimed at the same line produce a result that cannot be explained by the
  same precedence rule that governs two competing general rewards.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply two line-targeted coupons to the same line and compare the resolution against the general
  reward-precedence rule.
```

## G08-SALE_LOYALTY-Q048

```yaml
QID: G08-SALE_LOYALTY-Q048
MODULE: sale_loyalty
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  The precedence rule that resolves two rewards competing for one line is applied identically regardless of
  which channel or interface the order was raised through, so the same competing pair does not resolve
  differently depending on where the order originated.
WHY_IT_MATTERS: >
  A precedence outcome that depends on the originating channel is not a real business rule but an accident
  of implementation, and cannot be explained consistently to a customer or auditor.
DISCONFIRMING_OBSERVATION: >
  The same two competing rewards, applied to comparable orders raised through two different channels or
  interfaces, resolve to different winning rewards.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Raise comparable orders through two different channels or interfaces, both eligible for the same two
  competing rewards, and compare which reward each resolves to.
```
