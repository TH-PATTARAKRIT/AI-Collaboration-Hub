# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_mrp_margin Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE_MRP_MARGIN-MVQ48-V1.00  
**Group:** G08 SALES  
**Module Metadata:** `sale_mrp_margin`  
**Wave:** W2  
**Author Cell:** P-S3 (GMVQ Question Factory — Wave W2 Production)  
**Review Cell:** PENDING  
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN  
**actual_mvq_count:** 48  
**Standard bank reference:** 55 (shared, not reproduced here)  
**Research depth:** 55 + 48 = 103  
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded  

## Purpose

This bank authors the module-specific MVQ set for `sale_mrp_margin` — the margin figure computed on
a commercial order line where the cost is a production outcome, known only after the order has
actually been made, and subject to variance the customer never sees. Per the GMVQ Bridge Module Rule
and the Five-Margin Problem in the G08 Group Brief, this is the least knowable of the three sibling
cost bases this cell owns: the figure a customer's price was set against is a planned cost, and the
figure that actually happens is a production outcome that can diverge from it in either direction,
sometimes long after the sale is invoiced. Ground covered: a quotation margin derived from a planned
cost that production then misses; whether a recognized production variance ever actually reaches the
originating order's margin; a production overrun discovered after the sale is already invoiced; scrap
and yield loss landing in the causing order's margin or nowhere; one production run serving several
sales orders and how its cost is apportioned between them; a production order cancelled and remade;
a bill of materials changed between quotation and production; a contract-fixed customer price while
the underlying production cost moves; and who may see a manufacturing variance on a commercial
document. This bank deliberately does not re-author the general cost-basis, recompute-versus-restate,
or reconciliation questions already covered for derived margin figures elsewhere in the programme,
nor the pre-sale standing-cost or delivery-valuation grounds owned by this cell's sibling banks; it
targets only the ground specific to a cost that is a production outcome, known solely after the fact.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: sale_mrp_margin` appears only in
the structured metadata field, never inside question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- Authored under the GMVQ Bridge Module Rule V1.00 Five-Margin Problem: this bank's ground is the
  production-outcome cost only; siblings own the pre-sale standing-cost, delivery-valuation,
  third-party-invoice and recorded-labour cost grounds.

## G08-SALE_MRP_MARGIN-Q001

```yaml
QID: G08-SALE_MRP_MARGIN-Q001
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A quotation margin derived from a planned or estimated production cost is marked as resting on a
  planned figure rather than presented identically to a margin resting on a cost already incurred.
WHY_IT_MATTERS: >
  A planned figure presented as fact overstates the certainty of a number that production has not yet
  actually confirmed.
DISCONFIRMING_OBSERVATION: >
  A quotation margin derived from a planned production cost displays with no indication that the cost
  is a plan rather than an incurred fact.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Quote an order whose margin depends on a planned production cost and inspect whether the figure is
  marked as planned.
```

## G08-SALE_MRP_MARGIN-Q002

```yaml
QID: G08-SALE_MRP_MARGIN-Q002
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the actual production cost later becomes known and differs from the planned cost used at
  quotation, the order's recorded margin is updated to reflect the actual cost rather than remaining
  frozen at the original planned estimate.
WHY_IT_MATTERS: >
  A margin frozen at a since-disproven estimate misstates the real outcome of a deal whose true cost
  is now known.
DISCONFIRMING_OBSERVATION: >
  An order's recorded margin still matches the original planned production cost after the actual
  production cost, which differs from the plan, has become known.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete production for an order at a cost different from what was planned at quotation, then
  compare the order's recorded margin to both the planned and actual cost.
```

## G08-SALE_MRP_MARGIN-Q003

```yaml
QID: G08-SALE_MRP_MARGIN-Q003
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The quotation margin discloses whether the planned cost it rests on came from a general
  should-cost figure or from a specific estimate obtained for that exact order, since the two carry
  different reliability.
WHY_IT_MATTERS: >
  Treating a rough standard figure and a specific production estimate as equally reliable can lead a
  salesperson to price a deal with more confidence than the estimate actually supports.
DISCONFIRMING_OBSERVATION: >
  A quotation margin gives no way to tell whether its planned cost came from a general standard
  figure or an order-specific production estimate.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Quote an order and attempt to determine, from what is displayed, whether the planned cost behind
  the margin is a general standard or an order-specific estimate.
```

## G08-SALE_MRP_MARGIN-Q004

```yaml
QID: G08-SALE_MRP_MARGIN-Q004
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  For an order quoted well before production is scheduled, the planned-cost figure behind its margin
  can be refreshed against updated planning assumptions as the production date approaches, rather
  than remaining frozen at its original quotation-time value.
WHY_IT_MATTERS: >
  A stale planned figure that never refreshes becomes progressively less useful the further out
  production is, exactly when a refresh would matter most.
DISCONFIRMING_OBSERVATION: >
  An order's planned-cost-derived margin shows no mechanism to refresh as updated planning
  assumptions become available closer to the production date.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Quote an order for production scheduled well in the future, update the planning assumptions closer
  to that date, and check whether the order's margin reflects the update.
```

## G08-SALE_MRP_MARGIN-Q005

```yaml
QID: G08-SALE_MRP_MARGIN-Q005
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Confirming an order does not gate solely on a planned cost figure that is already known, at the
  moment of confirmation, to be stale relative to more current planning information.
WHY_IT_MATTERS: >
  Confirming a commercial commitment against a figure already known to be outdated locks in a
  potentially wrong profitability expectation that a simple check could have caught.
DISCONFIRMING_OBSERVATION: >
  An order is confirmed using a planned-cost margin that more current planning information already
  contradicted at the moment of confirmation, with no check or flag raised.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Update planning information to contradict an open quotation's planned cost, then confirm the order
  and check whether the contradiction was flagged.
```

## G08-SALE_MRP_MARGIN-Q006

```yaml
QID: G08-SALE_MRP_MARGIN-Q006
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a planned cost turns out to have been understated and the quotation margin was consequently
  overstated, that discrepancy is discoverable before the order reaches a point where reversing the
  commercial terms becomes impractical.
WHY_IT_MATTERS: >
  A discrepancy only discoverable after the commercial terms are locked in removes any chance to act
  on the information while it still matters.
DISCONFIRMING_OBSERVATION: >
  An understated planned cost that overstated an order's margin is discoverable only after the order
  has already reached a point where its terms can no longer practically be revisited.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Trace how and when an understated planned cost's effect on margin becomes discoverable relative to
  the order's commercial lifecycle.
```

## G08-SALE_MRP_MARGIN-Q007

```yaml
QID: G08-SALE_MRP_MARGIN-Q007
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a production run reports a cost variance against its planned cost, that variance flows through
  to the margin of the specific sales order that caused the production, rather than disappearing into
  an undifferentiated production-cost pool.
WHY_IT_MATTERS: >
  A variance that never reaches the order it belongs to leaves that order's margin permanently based
  on a plan rather than what actually happened.
DISCONFIRMING_OBSERVATION: >
  A production run reports a cost variance, but the sales order that caused the production shows no
  change to its margin as a result.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a production run with a recorded cost variance against its plan and check whether the
  causing sales order's margin reflects it.
```

## G08-SALE_MRP_MARGIN-Q008

```yaml
QID: G08-SALE_MRP_MARGIN-Q008
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a production variance is, by deliberate design, recognized at the production level without
  being attributed to any specific sales order, that non-attribution is an explicit, disclosed
  design choice rather than a silent, undocumented gap.
WHY_IT_MATTERS: >
  An undocumented gap in variance attribution looks, from a reviewer's seat, indistinguishable from a
  defect, and nobody can tell whether the behaviour is intended.
DISCONFIRMING_OBSERVATION: >
  Production variance is not attributed to the sales order that caused it, and no documentation or
  configuration setting indicates that this is an intended design choice.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Check whether the non-attribution of production variance to a sales order is stated anywhere as an
  intended behaviour rather than being discovered only by its absence.
```

## G08-SALE_MRP_MARGIN-Q009

```yaml
QID: G08-SALE_MRP_MARGIN-Q009
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A favorable production variance, where actual cost is lower than planned, flows through to increase
  an order's margin with the same rigor that an unfavorable variance would flow through to decrease
  it, rather than only one direction actually reaching the order.
WHY_IT_MATTERS: >
  A system that only propagates bad news and silently absorbs good news systematically understates
  the profitability of every order it touches.
DISCONFIRMING_OBSERVATION: >
  An unfavorable production variance visibly reduces an order's margin, but an equivalent favorable
  variance on a comparable order does not visibly increase it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce one order with an unfavorable variance and a comparable order with a favorable variance and
  compare whether both flow through to their respective order margins.
```

## G08-SALE_MRP_MARGIN-Q010

```yaml
QID: G08-SALE_MRP_MARGIN-Q010
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a production run serves both a specific sales order and general inventory beyond that order's
  quantity, the variance attributed to the order reflects only the order's own share of the run,
  not the run's entire variance.
WHY_IT_MATTERS: >
  Assigning an entire run's variance to one order that only consumed part of the run overstates or
  understates that order's true profitability.
DISCONFIRMING_OBSERVATION: >
  An order that consumed only part of a production run's output is attributed the full variance of
  the entire run rather than its proportional share.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Run production that serves one order plus additional general inventory, and check whether the
  order's attributed variance reflects only its own share.
```

## G08-SALE_MRP_MARGIN-Q011

```yaml
QID: G08-SALE_MRP_MARGIN-Q011
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The timing of variance recognition, whether at production completion or at a later costing pass,
  is applied consistently for every order drawing from the same production run, rather than leaving
  some orders' margins stale relative to others by the accident of when each is checked.
WHY_IT_MATTERS: >
  Inconsistent timing across orders sharing one run means two equally situated orders can show
  different margins purely because one was looked at sooner than the other.
DISCONFIRMING_OBSERVATION: >
  Two orders drawing from the same production run show variance reflected in one order's margin but
  not yet in the other's, with no indication that one is pending a later pass.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Complete a production run serving two orders and compare when each order's margin reflects the
  run's variance.
```

## G08-SALE_MRP_MARGIN-Q012

```yaml
QID: G08-SALE_MRP_MARGIN-Q012
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a production variance is recognized after its related sales order has already been archived,
  closed, or otherwise made inactive, the variance still finds its way into that order's historical
  margin record rather than becoming unattributable.
WHY_IT_MATTERS: >
  A variance that cannot attach to a closed order simply vanishes from the historical record of what
  that deal actually cost.
DISCONFIRMING_OBSERVATION: >
  A production variance is recognized after its related sales order is closed, and no update reaches
  that order's historical margin record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Close a sales order, then recognize a production variance related to it afterward, and check
  whether the order's historical margin record reflects it.
```

## G08-SALE_MRP_MARGIN-Q013

```yaml
QID: G08-SALE_MRP_MARGIN-Q013
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a production order overruns its planned cost after the corresponding sale has already been
  invoiced, the resulting cost variance is still recorded against that already-invoiced order's
  margin rather than the invoice's finality preventing any attribution.
WHY_IT_MATTERS: >
  An overrun that can never reach an already-invoiced order's margin means the business permanently
  loses visibility into deals that turned out worse than believed.
DISCONFIRMING_OBSERVATION: >
  A production overrun discovered after invoicing produces no change anywhere to the already-invoiced
  order's recorded margin.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice a sale, then let its production overrun its planned cost afterward, and check whether the
  order's recorded margin reflects the overrun.
```

## G08-SALE_MRP_MARGIN-Q014

```yaml
QID: G08-SALE_MRP_MARGIN-Q014
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a variance is recorded against an already-invoiced order, that recording lands in an
  identifiable, current accounting period rather than reopening or silently altering the period the
  original invoice belonged to.
WHY_IT_MATTERS: >
  Silently altering a closed period's figures undermines the finality a period close is supposed to
  represent.
DISCONFIRMING_OBSERVATION: >
  A post-invoice production variance changes the margin recorded in the original invoice's already-
  closed accounting period rather than landing in a new, identifiable period.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a production variance against an order after its invoice's accounting period has closed and
  check which period the correction lands in.
```

## G08-SALE_MRP_MARGIN-Q015

```yaml
QID: G08-SALE_MRP_MARGIN-Q015
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An overrun discovered after invoicing triggers a visible flag or reconciliation item rather than
  the business simply losing visibility into the fact that the deal was actually less profitable
  than the invoice implied.
WHY_IT_MATTERS: >
  A silent loss of visibility means nobody ever learns that a specific deal underperformed, even
  though the data to know that exists somewhere in the system.
DISCONFIRMING_OBSERVATION: >
  A post-invoice production overrun exists in the system with no flag or reconciliation item ever
  surfacing it to anyone.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a post-invoice production overrun and search for any flag or reconciliation item raised as
  a result.
```

## G08-SALE_MRP_MARGIN-Q016

```yaml
QID: G08-SALE_MRP_MARGIN-Q016
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a production overrun is large enough to turn an order's true margin negative, that fact is
  discoverable somewhere in the system even though the customer-facing invoice and its stated terms
  never change.
WHY_IT_MATTERS: >
  A loss-making deal that is undiscoverable anywhere in the system cannot be learned from or factored
  into future pricing decisions.
DISCONFIRMING_OBSERVATION: >
  An order whose true margin has turned negative due to a production overrun shows no discoverable
  indication of that anywhere in the system.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce an overrun large enough to turn an order's true margin negative and search the system for
  any discoverable indication of the loss.
```

## G08-SALE_MRP_MARGIN-Q017

```yaml
QID: G08-SALE_MRP_MARGIN-Q017
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an overrun ever reaches an order's recorded margin does not depend on the accidental timing
  gap between invoicing and production completion, so that an order invoiced before production
  finishes is not structurally excluded from ever seeing its own variance.
WHY_IT_MATTERS: >
  If the invoice-first sequence structurally excludes an order from ever recording a variance, then
  an entire class of orders is permanently blind to their own true cost outcome.
DISCONFIRMING_OBSERVATION: >
  An order invoiced before its production completes never receives a variance update regardless of
  how its production actually turns out, while an order invoiced after production does.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compare variance attribution for one order invoiced before production completion and one invoiced
  after, both experiencing an overrun.
```

## G08-SALE_MRP_MARGIN-Q018

```yaml
QID: G08-SALE_MRP_MARGIN-Q018
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Scrap or yield loss generated by a production run attributable to a specific sales order is
  reflected in that order's margin, rather than being absorbed into a general overhead or write-off
  with no link back to the order that caused it.
WHY_IT_MATTERS: >
  Scrap absorbed anonymously into overhead means the order that actually caused the loss never bears
  its own true cost.
DISCONFIRMING_OBSERVATION: >
  Scrap generated by a production run tied to a specific sales order shows no effect on that order's
  margin.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate scrap in a production run tied to a specific sales order and check whether the order's
  margin reflects it.
```

## G08-SALE_MRP_MARGIN-Q019

```yaml
QID: G08-SALE_MRP_MARGIN-Q019
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Yield loss within a normal, expected tolerance is distinguished, in its margin impact, from yield
  loss that exceeds tolerance, rather than both cases affecting the order identically with no signal
  that something abnormal occurred.
WHY_IT_MATTERS: >
  Treating routine and abnormal loss identically means an order with a genuine production problem
  looks no different from one that behaved exactly as expected.
DISCONFIRMING_OBSERVATION: >
  An order affected by yield loss well beyond normal tolerance shows a margin impact indistinguishable
  from one affected by ordinary, within-tolerance loss.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Compare the margin impact of within-tolerance yield loss to well-beyond-tolerance yield loss on
  otherwise comparable orders.
```

## G08-SALE_MRP_MARGIN-Q020

```yaml
QID: G08-SALE_MRP_MARGIN-Q020
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Scrap generated partway through a production run serving multiple orders is apportioned across
  those orders in a defined way, rather than landing entirely on whichever order happens to be
  recorded first or last in the run.
WHY_IT_MATTERS: >
  An apportionment based on recording order rather than actual cause produces margin figures that
  reflect bookkeeping sequence rather than reality.
DISCONFIRMING_OBSERVATION: >
  Scrap from a production run serving several orders is attributed entirely to one order based on its
  position in the recording sequence rather than a defined apportionment rule.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate scrap partway through a production run serving several orders and check how it is
  apportioned among them.
```

## G08-SALE_MRP_MARGIN-Q021

```yaml
QID: G08-SALE_MRP_MARGIN-Q021
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When scrapped material is itself recovered for value through rework or resale, that recovered
  value offsets the loss reflected in the affected order's margin, rather than the order absorbing
  the full scrap cost with no credit for what was recovered.
WHY_IT_MATTERS: >
  Charging an order for a loss that was subsequently, at least partly, recovered overstates how much
  that order actually cost the business.
DISCONFIRMING_OBSERVATION: >
  An order's margin reflects the full cost of scrap that was later recovered through rework or
  resale, with no offsetting credit for the recovered value.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate scrap for an order, recover part of its value through rework or resale, and check whether
  the order's margin reflects the recovery.
```

## G08-SALE_MRP_MARGIN-Q022

```yaml
QID: G08-SALE_MRP_MARGIN-Q022
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scrap or yield event large enough to matter is individually traceable to the specific production
  run and order it affected, rather than disappearing into a period-level aggregate with no
  order-level attribution.
WHY_IT_MATTERS: >
  An untraceable large loss event cannot be investigated, explained to a customer, or used to improve
  future production planning.
DISCONFIRMING_OBSERVATION: >
  A significant scrap or yield event cannot be traced back to the specific production run and order
  it affected, appearing only in a period-level aggregate.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a significant scrap or yield event and attempt to trace it to the specific run and order it
  affected.
```

## G08-SALE_MRP_MARGIN-Q023

```yaml
QID: G08-SALE_MRP_MARGIN-Q023
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a production run generating scrap has no sales order linked to it at all, such as production
  made for general stock, that scrap is correctly excluded from every sales order's margin rather
  than being mistakenly attributed to an unrelated order.
WHY_IT_MATTERS: >
  Misattributing unrelated production scrap to an order that had nothing to do with it charges that
  order for a cost it never actually caused.
DISCONFIRMING_OBSERVATION: >
  Scrap from a production run with no linked sales order appears reflected in the margin of an
  unrelated sales order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate scrap in a production run made for general stock with no linked sales order, and check
  whether any unrelated order's margin reflects it.
```

## G08-SALE_MRP_MARGIN-Q024

```yaml
QID: G08-SALE_MRP_MARGIN-Q024
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a single production run's output is shared across several sales orders, the run's actual cost
  is apportioned to each order in a defined, disclosed way rather than an arbitrary or undocumented
  split.
WHY_IT_MATTERS: >
  An undocumented apportionment means no two orders sharing a run can be trusted to reflect a fair or
  explainable share of what production actually cost.
DISCONFIRMING_OBSERVATION: >
  Several orders sharing one production run show margins whose implied cost apportionment cannot be
  explained by any documented rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Serve several sales orders from one production run and attempt to trace each order's cost share to
  a documented apportionment rule.
```
## G08-SALE_MRP_MARGIN-Q025

```yaml
QID: G08-SALE_MRP_MARGIN-Q025
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The apportionment method used to split one production run's cost across several sales orders is
  applied consistently for every order drawing from that run, rather than each order's margin
  resting on a different implicit assumption about its own share.
WHY_IT_MATTERS: >
  Inconsistent apportionment logic across orders sharing the same run means the same run produces
  incompatible cost stories depending on which order is examined.
DISCONFIRMING_OBSERVATION: >
  Two orders sharing the same production run show cost apportionments that imply two different,
  incompatible apportionment methods were used.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Serve two orders from the same production run and check whether each order's implied apportionment
  method matches the other's.
```

## G08-SALE_MRP_MARGIN-Q026

```yaml
QID: G08-SALE_MRP_MARGIN-Q026
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When several orders sharing one production run have different quantities, the apportionment of the
  run's cost scales with each order's actual quantity rather than splitting the cost evenly
  regardless of how much each order actually took.
WHY_IT_MATTERS: >
  An even split regardless of quantity systematically overcharges the small order and undercharges
  the large one, or the reverse, misstating both order's true margins.
DISCONFIRMING_OBSERVATION: >
  Two orders of markedly different quantity sharing the same production run are apportioned equal
  shares of the run's cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Serve two orders of different quantities from the same production run and check whether the
  apportioned cost scales with quantity.
```

## G08-SALE_MRP_MARGIN-Q027

```yaml
QID: G08-SALE_MRP_MARGIN-Q027
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If one of several orders sharing a production run is cancelled after the run completes, that
  order's share of the run's cost is reapportioned to the remaining orders rather than simply
  vanishing from every order's margin.
WHY_IT_MATTERS: >
  A vanished cost share understates the true total cost of a run that genuinely happened, spreading a
  cost the business actually incurred across fewer orders than it should.
DISCONFIRMING_OBSERVATION: >
  After one of several orders sharing a completed production run is cancelled, the total cost
  reflected across the remaining orders' margins is less than the run's actual total cost.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel one of several orders sharing a completed production run and check whether its cost share is
  reapportioned to the remaining orders.
```

## G08-SALE_MRP_MARGIN-Q028

```yaml
QID: G08-SALE_MRP_MARGIN-Q028
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a production run's actual cost is not yet fully known at the time the first of several served
  orders is invoiced, that invoice's margin is explicit about resting on a provisional apportionment
  rather than presenting a figure as final.
WHY_IT_MATTERS: >
  A provisional apportionment presented as final misleads the reader of the first invoice into
  believing a settled figure exists when the run's true cost is still open.
DISCONFIRMING_OBSERVATION: >
  The first invoice issued from a production run whose total cost is not yet final shows a margin
  with no indication that its apportionment is provisional.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Invoice the first of several orders served by a production run before the run's total cost is
  finalized, and inspect whether the margin is marked provisional.
```

## G08-SALE_MRP_MARGIN-Q029

```yaml
QID: G08-SALE_MRP_MARGIN-Q029
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When one run's cost is apportioned across several orders, the sum of the resulting order-level
  margins is explainable against, and reconcilable to, an aggregate margin computed for the run as a
  whole.
WHY_IT_MATTERS: >
  An unreconcilable gap between the sum of the parts and the whole means the apportionment logic
  itself cannot be trusted to be internally consistent.
DISCONFIRMING_OBSERVATION: >
  The sum of the margins of all orders sharing one production run does not match an independently
  computed aggregate margin for that run as a whole, with no reconciling explanation.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Sum the margins of all orders sharing one production run and compare the total to an independently
  computed run-level aggregate margin.
```

## G08-SALE_MRP_MARGIN-Q030

```yaml
QID: G08-SALE_MRP_MARGIN-Q030
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a production order is cancelled and a new one is created to fulfill the same sales order, the
  sales order's margin reflects the cost of the production order that actually completed, not any
  cost basis carried over from the cancelled attempt.
WHY_IT_MATTERS: >
  A margin still anchored to a cancelled attempt's assumed cost misrepresents the production that
  actually produced the delivered goods.
DISCONFIRMING_OBSERVATION: >
  After a production order is cancelled and replaced, the sales order's margin still reflects a cost
  basis from the cancelled attempt rather than the replacement that actually completed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel a production order and replace it with a new one at a different cost, then check which cost
  the sales order's margin reflects.
```

## G08-SALE_MRP_MARGIN-Q031

```yaml
QID: G08-SALE_MRP_MARGIN-Q031
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling and remaking a production order leaves a record of any cost already sunk into the
  cancelled attempt, so that cost is not simply lost from the order's margin history with no trace.
WHY_IT_MATTERS: >
  A sunk cost that leaves no trace understates the true resources the business actually spent pursuing
  that order, even if the final delivered cost looks reasonable.
DISCONFIRMING_OBSERVATION: >
  A production order cancelled after incurring real cost leaves no record of that sunk cost anywhere
  once a replacement order is created.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a production order after it has already incurred some cost, then search for a record of that
  sunk cost.
```

## G08-SALE_MRP_MARGIN-Q032

```yaml
QID: G08-SALE_MRP_MARGIN-Q032
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a production order is cancelled after partial work has already consumed materials or labor,
  that partial sunk cost is attributed to the sales order's margin in some defined way, rather than
  disappearing entirely because the production order was never completed.
WHY_IT_MATTERS: >
  Genuine consumed cost that disappears simply because the production order technically never
  finished overstates the order's true profitability.
DISCONFIRMING_OBSERVATION: >
  A production order cancelled after consuming real materials or labor results in no attribution of
  that consumed cost to the related sales order's margin.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel a production order after it has consumed materials or labor, and check whether that
  consumption is attributed to the sales order's margin.
```

## G08-SALE_MRP_MARGIN-Q033

```yaml
QID: G08-SALE_MRP_MARGIN-Q033
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a production order is repeatedly cancelled and remade for the same sales order, each attempt's
  cost remains individually distinguishable rather than collapsing into one figure that cannot be
  decomposed back into what was actually attempted.
WHY_IT_MATTERS: >
  An undecomposable collapsed figure prevents anyone from understanding how many attempts a
  troublesome order actually required and what each one cost.
DISCONFIRMING_OBSERVATION: >
  After several cancel-and-remake cycles for one sales order, the individual cost of each attempt
  cannot be distinguished from the others.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel and remake the production order for one sales order several times and attempt to distinguish
  each attempt's individual cost.
```

## G08-SALE_MRP_MARGIN-Q034

```yaml
QID: G08-SALE_MRP_MARGIN-Q034
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a remade production order uses a different bill of materials or process than the cancelled
  one, the sales order's margin reflects the process that actually produced the delivered goods, not
  the process originally planned before cancellation.
WHY_IT_MATTERS: >
  A margin anchored to a plan that was never actually executed misrepresents the goods the customer
  actually received.
DISCONFIRMING_OBSERVATION: >
  A sales order's margin reflects the bill of materials or process of a cancelled production attempt
  rather than the one that actually produced the delivered goods.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel a production order and remake it under a different bill of materials, then check which
  process the sales order's margin reflects.
```

## G08-SALE_MRP_MARGIN-Q035

```yaml
QID: G08-SALE_MRP_MARGIN-Q035
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the bill of materials for an item changes between the moment a sales order is quoted and the
  moment production actually occurs, the order's margin reflects the cost of the bill of materials
  actually used in production, not the one assumed at quotation.
WHY_IT_MATTERS: >
  A margin based on a bill of materials that was never actually used to produce the delivered goods
  is a figure that describes a product that does not exist.
DISCONFIRMING_OBSERVATION: >
  An order's margin matches the cost of the bill of materials assumed at quotation rather than the
  different one actually used when production occurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Change the bill of materials between quotation and production, then check which version's cost the
  order's margin reflects.
```

## G08-SALE_MRP_MARGIN-Q036

```yaml
QID: G08-SALE_MRP_MARGIN-Q036
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A bill of materials change between quotation and production triggers some comparison or flag
  showing how far the actual production cost diverged from what was assumed when the customer's
  price was set.
WHY_IT_MATTERS: >
  Without a flagged comparison, a significant divergence between assumed and actual cost is only
  discoverable by someone who happens to go looking for it.
DISCONFIRMING_OBSERVATION: >
  A bill of materials change between quotation and production that materially changes cost produces
  no comparison or flag against the cost assumed when the price was set.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the bill of materials to materially alter cost between quotation and production, and check
  for a resulting comparison or flag.
```

## G08-SALE_MRP_MARGIN-Q037

```yaml
QID: G08-SALE_MRP_MARGIN-Q037
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A bill of materials substitution driven by a shortage or supply issue is distinguished, in the
  order's margin history, from a routine or planned bill of materials revision.
WHY_IT_MATTERS: >
  Conflating an emergency substitution with a routine planned change hides a supply risk signal that
  the business would otherwise be able to see and act on.
DISCONFIRMING_OBSERVATION: >
  An order's margin history shows a cost change from a bill of materials substitution with no way to
  distinguish it from a routine, planned revision.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Substitute a bill of materials component due to a shortage and check whether the resulting cost
  change is distinguished from a routine revision in the order's history.
```

## G08-SALE_MRP_MARGIN-Q038

```yaml
QID: G08-SALE_MRP_MARGIN-Q038
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a bill of materials changes after some units for an order have already been produced under the
  original version, the order's margin correctly reflects a mix of both versions' costs rather than
  applying one version's cost to the entire order.
WHY_IT_MATTERS: >
  Applying one version's cost to units actually produced under the other version misstates the true
  blended cost of what was actually delivered.
DISCONFIRMING_OBSERVATION: >
  An order fulfilled partly under an original bill of materials and partly under a revised one shows
  a margin computed as if only one version applied to the entire order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce part of an order under one bill of materials version, change the version, produce the rest,
  and check whether the order's margin reflects the mix.
```

## G08-SALE_MRP_MARGIN-Q039

```yaml
QID: G08-SALE_MRP_MARGIN-Q039
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the specific bill of materials version used for a given order can no longer be identified
  after the fact, because only the current version is retained on record, the order's margin remains
  traceable to the cost actually incurred at the time.
WHY_IT_MATTERS: >
  Losing the link between an order and the version actually used to produce it makes any later
  question about that order's true cost unanswerable.
DISCONFIRMING_OBSERVATION: >
  An order's margin cannot be reconciled to any actual, incurred cost because the specific bill of
  materials version used to produce it is no longer identifiable.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Revise a bill of materials so only the current version remains on record, then attempt to trace an
  older order's margin back to the cost actually incurred.
```

## G08-SALE_MRP_MARGIN-Q040

```yaml
QID: G08-SALE_MRP_MARGIN-Q040
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a customer's price is fixed by contract for an extended period while the underlying
  production cost moves during that period, each order's margin reflects the production cost
  actually incurred for that specific order's own production run, not a cost assumed when the
  contract price was originally fixed.
WHY_IT_MATTERS: >
  Using the original contract-time cost assumption for every order under a long contract hides how
  profitability is actually moving as real production costs change.
DISCONFIRMING_OBSERVATION: >
  An order under a long-running fixed-price contract shows a margin computed against the cost
  assumed when the contract was signed rather than the cost actually incurred for that order's own
  production.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Under a fixed-price contract, let production cost move over time, then check whether a later
  order's margin reflects its own actual production cost or the original contract-time assumption.
```

## G08-SALE_MRP_MARGIN-Q041

```yaml
QID: G08-SALE_MRP_MARGIN-Q041
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A contract-fixed-price arrangement provides some visibility into how margin is trending across the
  life of the contract as production costs move, rather than margin being visible only order by
  order with no way to see the trend.
WHY_IT_MATTERS: >
  Without a trend view, a slow, steady erosion of margin across a long contract is invisible until it
  has already become severe.
DISCONFIRMING_OBSERVATION: >
  No available view shows how margin has trended across the orders of a single long-running
  fixed-price contract.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Accumulate several orders under one fixed-price contract with moving production cost, and search
  for a trend view across them.
```

## G08-SALE_MRP_MARGIN-Q042

```yaml
QID: G08-SALE_MRP_MARGIN-Q042
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A sequence of orders under a fixed-price contract whose margins are shrinking or turning negative
  as production costs rise is flagged before the trend becomes severe, rather than being discoverable
  only after the fact by manually reviewing each order.
WHY_IT_MATTERS: >
  A trend only discoverable by manual review after the fact means the business acts on a shrinking
  contract's margin only once the damage is already substantial.
DISCONFIRMING_OBSERVATION: >
  A fixed-price contract's orders show a clear shrinking-margin trend with no flag raised before the
  trend became severe.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Simulate a shrinking-margin trend across several orders under one fixed-price contract and check
  whether a flag is raised before the trend becomes severe.
```

## G08-SALE_MRP_MARGIN-Q043

```yaml
QID: G08-SALE_MRP_MARGIN-Q043
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a contract specifies a price adjustment mechanism tied to a cost index or trigger, an order's
  margin reflects whether that mechanism was actually applied for that specific order, rather than
  assuming the unadjusted base contract price applied uniformly regardless of whether the trigger
  fired.
WHY_IT_MATTERS: >
  Assuming the mechanism applied when it did not, or the reverse, misstates the price actually
  charged and therefore the margin actually realized.
DISCONFIRMING_OBSERVATION: >
  An order's margin is computed as though a contract's price adjustment mechanism applied when it did
  not actually trigger for that order, or the reverse.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a contract price adjustment mechanism, produce an order where the trigger condition is
  not met, and check whether the margin assumes the adjustment applied anyway.
```

## G08-SALE_MRP_MARGIN-Q044

```yaml
QID: G08-SALE_MRP_MARGIN-Q044
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A contract-fixed-price order whose true margin depends on a production cost not yet finalized at
  confirmation carries the same provisional-versus-final distinction as any other order whose cost is
  not yet known, rather than being treated as fully final immediately upon confirmation.
WHY_IT_MATTERS: >
  Treating a genuinely unresolved cost as final the moment the order is confirmed overstates the
  certainty of a figure that has not actually been earned yet.
DISCONFIRMING_OBSERVATION: >
  A contract-fixed-price order is marked as having a final margin at confirmation even though its
  underlying production cost has not yet actually been determined.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm a contract-fixed-price order before its production cost is determined and check whether the
  margin is marked provisional or final.
```

## G08-SALE_MRP_MARGIN-Q045

```yaml
QID: G08-SALE_MRP_MARGIN-Q045
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A manufacturing cost variance never appears, visibly or in underlying data, on a document generated
  for the customer, such as an order confirmation or invoice.
WHY_IT_MATTERS: >
  A customer-facing document carrying internal production variance data exposes commercially
  sensitive information to the one party who should never see it.
DISCONFIRMING_OBSERVATION: >
  A manufacturing cost variance value appears, visibly or in the underlying data, of a document
  generated for the customer.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Generate a customer-facing document for an order with a recorded manufacturing variance and inspect
  its rendered content and underlying data for the variance value.
```

## G08-SALE_MRP_MARGIN-Q046

```yaml
QID: G08-SALE_MRP_MARGIN-Q046
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Visibility into a manufacturing variance is restricted to a role distinct from the general
  margin-visibility role, given that a variance can reveal more about internal production performance
  than a simple margin figure would.
WHY_IT_MATTERS: >
  Bundling variance visibility into the same grant as ordinary margin visibility exposes internal
  production performance to a wider audience than intended.
DISCONFIRMING_OBSERVATION: >
  A user granted only general margin visibility, with no distinct production-variance entitlement, can
  see manufacturing variance data.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user with general margin visibility but no separate variance entitlement, attempt to view
  manufacturing variance data for an order.
```

## G08-SALE_MRP_MARGIN-Q047

```yaml
QID: G08-SALE_MRP_MARGIN-Q047
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A report that combines commercial data such as customer and price with manufacturing variance data
  is subject to the same access control as either data set would be independently, rather than the
  combination creating a broader audience than either was individually intended for.
WHY_IT_MATTERS: >
  A combined report with looser access than its most sensitive component defeats the access control
  applied to that component everywhere else.
DISCONFIRMING_OBSERVATION: >
  A combined commercial-and-variance report is reachable by a user who is not entitled to
  manufacturing variance data on its own.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user without manufacturing-variance entitlement, attempt to reach a report that combines
  commercial data with variance data.
```

## G08-SALE_MRP_MARGIN-Q048

```yaml
QID: G08-SALE_MRP_MARGIN-Q048
MODULE: sale_mrp_margin
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a person's access to production or manufacturing data is separately revoked, a manufacturing
  variance tied to a specific sales order they can still view stops being visible to them through that
  sales order.
WHY_IT_MATTERS: >
  A revocation that only closes one door while leaving the same data reachable through the sales order
  is not a real revocation.
DISCONFIRMING_OBSERVATION: >
  After a user's manufacturing/production data access is revoked, a manufacturing variance for an
  order remains visible to them through their continuing access to the sales order.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Revoke a user's manufacturing/production data access while leaving their sales-order access intact,
  then check whether they can still see a variance figure through the order.
```
