# SMEsPlus ENTERPRISE SUITE
## GMVQ — G06 MANUFACTURING / mrp_account Module Adversarial MVQ Bank

**Document ID:** GMVQ-G06-MRP_ACCOUNT-MVQ48-V1.00
**Group:** G06 MANUFACTURING
**Module Metadata:** `mrp_account`
**Wave:** W2
**Author Cell:** P09 (GMVQ Question Factory — Internal Production Team P09, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This module is the seam through which production becomes ledger entries: it exists only to translate what a
production order did internally — components it consumed, output it produced, variance between planned and
actual — into posted financial value. Under the bridge-module rule, every question in this bank fails only at
that seam: the value of components consumed against the value assigned to the finished item; the standard-versus-
actual variance and its traceability; where in-process value sits while an order is open and what happens to it
if the order is abandoned; a production run spanning a closed accounting period; splitting one cost across a
primary output and a by-product; where scrap value during production is charged; whether operation or labour
cost is capitalized or expensed; the compensating entry required when a completed, posted order is reversed or
unbuilt; a cost component changed while orders are open; rounding between quantity, unit cost, and posted amount;
per-company valuation on a bill shared across legal entities; and who may adjust a produced item's cost after
the fact, and what trace that leaves.

Every question was tested against the bridge-module seam test: if production and the ledger were used entirely
apart from one another, the question would not make sense. Each one turns on the moment production's internal
state is translated into a posted financial fact — never on a pure production-only invariant (which belongs to
the base manufacturing module) and never on a pure ledger-only invariant (which belongs to the ledger's own
bank).

Question text is source-neutral: no vendor or product name, no technical identifier (model, table, field,
method, XML ID, API path), and no reference to how any specific implementation is built. Language is generic
business/behavioural language throughout.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business
  invariant, exception path, configuration dependency, role/permission, cancellation/reversal, negative case,
  cross-module dependency, auditability, tenant/company boundary, concurrency, and period/runtime reachability.
- This module carries one layer (the production-to-ledger seam only); the `LAYER` field is omitted throughout.
- Checked against the bridge-module rule before authoring: no sibling bank existed on disk for this group at
  authoring time (`G06_MANUFACTURING` had no prior banks), so no existing HYPOTHESIS lines could be duplicated.
  Within this production run, this bank's ground is held strictly to production's own internally generated cost
  reaching the ledger, distinct from the sibling `mrp_landed_costs` bank's ground, which is a later, externally
  arriving cost pushed backward onto units already produced — the two are held apart by design, not by
  coincidence of nouns.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a Research
  Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G06-MRP_ACCOUNT-Q001

```yaml
QID: G06-MRP_ACCOUNT-Q001
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The total value of the components consumed by a production order reconciles to the value assigned to the
  finished item(s) it produces, through a stated and consistent method, rather than the two figures being free
  to diverge without explanation.
WHY_IT_MATTERS: >
  If the value assigned to a finished item can drift away from what was actually consumed to make it, every
  downstream figure that depends on that item's cost is unreliable without anyone being told.
DISCONFIRMING_OBSERVATION: >
  A completed production order's finished-item value differs materially from the value its component consumption
  record shows was used, with no variance entry or documented reason accounting for the gap.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a production order with a known, fixed set of component consumption values and compare the resulting
  finished-item value against the sum of those consumption values.
```

## G06-MRP_ACCOUNT-Q002

```yaml
QID: G06-MRP_ACCOUNT-Q002
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a component is consumed before its own acquisition cost is finally known, the production order's
  resulting cost reflects that gap in a defined way — an estimate later reconciled, or a hold — rather than the
  gap simply disappearing into the posted figure.
WHY_IT_MATTERS: >
  An unresolved valuation gap that quietly disappears into a posted number understates or overstates every order
  that consumed that component, with no way to find or correct it later.
DISCONFIRMING_OBSERVATION: >
  A component is consumed while its own cost is still undetermined, the production order posts a final cost
  anyway, and no later adjustment, flag, or reconciliation step ever revisits that order once the component's
  real cost becomes known.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Consume a component whose incoming cost has not yet been finalized, complete the order, then finalize the
  component's cost afterward and check whether the order's value is revisited.
```

## G06-MRP_ACCOUNT-Q003

```yaml
QID: G06-MRP_ACCOUNT-Q003
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a single production order consumes components that are individually configured under different valuation
  methods, the order's total consumed value is computed by respecting each component's own method, not by
  forcing every component onto one method for that order.
WHY_IT_MATTERS: >
  Silently normalizing every component to one valuation method inside a single order would misstate the true
  consumed value for whichever components use a different method by policy.
DISCONFIRMING_OBSERVATION: >
  A production order that consumes components under two different valuation methods produces a total consumed
  value that could only have been reached if one component's configured method had been ignored.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Set up components with two different valuation-method configurations, consume both on the same order, and
  check whether each component's own method was actually used.
```

## G06-MRP_ACCOUNT-Q004

```yaml
QID: G06-MRP_ACCOUNT-Q004
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A component whose own cost record was never completed cannot be consumed by a production order and silently
  contribute an undetected zero or placeholder value to that order's cost.
WHY_IT_MATTERS: >
  A silent zero-value consumption understates the true cost of every finished item produced from it, and nothing
  about the posted figures would reveal that the understatement happened.
DISCONFIRMING_OBSERVATION: >
  A component with no completed cost record is consumed by a production order, and the order's posted cost shows
  no flag, gap, or zero-value indicator distinguishing that consumption from a normally valued one.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Attempt to consume a component that has no finalized cost record on a production order and inspect how that
  consumption is reflected in the order's cost.
```

## G06-MRP_ACCOUNT-Q005

```yaml
QID: G06-MRP_ACCOUNT-Q005
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A difference between a predetermined (standard) cost and the actual cost realized by a production order is
  recorded as its own identifiable amount, distinct from the finished item's base valuation, rather than being
  blended invisibly into it.
WHY_IT_MATTERS: >
  A variance blended silently into the base valuation hides exactly the signal — over-cost or under-cost
  production — that the standard-cost comparison exists to surface.
DISCONFIRMING_OBSERVATION: >
  A production order with a known, deliberately introduced gap between standard and actual cost completes with
  no separately identifiable variance amount anywhere in its posted records.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Complete a production order where actual consumption cost is deliberately set to differ from the standard
  cost, then look for a distinct variance record.
```

## G06-MRP_ACCOUNT-Q006

```yaml
QID: G06-MRP_ACCOUNT-Q006
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A variance amount can be traced back, without ambiguity, to the specific production order that generated it,
  rather than appearing as an unattributed lump-sum figure.
WHY_IT_MATTERS: >
  An untraceable variance cannot be investigated, challenged, or explained to an auditor, which defeats the
  purpose of separating it out in the first place.
DISCONFIRMING_OBSERVATION: >
  A variance posting exists in the ledger with no retained link back to the production order (or orders) that
  produced it.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Generate a variance from a specific production order and attempt to trace the resulting ledger entry back to
  that order using only the retained evidence.
```

## G06-MRP_ACCOUNT-Q007

```yaml
QID: G06-MRP_ACCOUNT-Q007
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Whether variance is recognized only once at an order's final closure, or incrementally as partial output is
  completed, the total variance recognized across the order's whole life equals the same figure either way.
WHY_IT_MATTERS: >
  A production order completed across several partial deliveries whose variance total does not equal the true
  end-to-end difference would misstate the period's results by an amount nobody would think to look for.
DISCONFIRMING_OBSERVATION: >
  A production order completed in several partial output steps shows a summed variance that differs from the
  variance the same order would show if completed in a single step with identical inputs and outputs.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete one order in a single step and an otherwise-identical order in several partial steps, and compare
  total recognized variance between the two.
```

## G06-MRP_ACCOUNT-Q008

```yaml
QID: G06-MRP_ACCOUNT-Q008
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A production order that consumes components but is never marked complete or explicitly cancelled does not
  carry an indefinitely deferred variance that silently never reaches the ledger.
WHY_IT_MATTERS: >
  An order left open forever would be a standing, invisible way to keep a real cost difference permanently off
  the books.
DISCONFIRMING_OBSERVATION: >
  A production order is left open indefinitely after full component consumption, and after an extended period no
  variance, hold, or exception state has been raised for it anywhere reviewable.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Fully consume components on a production order, leave it open without closing or cancelling it, and check for
  any resulting exception state after a reasonable interval.
```

## G06-MRP_ACCOUNT-Q009

```yaml
QID: G06-MRP_ACCOUNT-Q009
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Value already consumed by a production order that has not yet produced its output is held in a distinct,
  identifiable ledger position — separate from both the raw component's original value and the eventual finished
  item's cost — for as long as the order remains open.
WHY_IT_MATTERS: >
  Without a distinct in-process position, the financial statements at any moment while production is underway
  cannot show what has actually been spent versus what has actually been delivered.
DISCONFIRMING_OBSERVATION: >
  While a production order is open and partway through consuming components, no ledger position anywhere
  reflects the value already consumed by that order as distinct from ordinary raw inventory or a completed
  finished item.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially consume components on an open production order and inspect the ledger for a distinct in-process
  value corresponding to that order.
```

## G06-MRP_ACCOUNT-Q010

```yaml
QID: G06-MRP_ACCOUNT-Q010
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A production order that consumes components and is then abandoned — neither completed nor explicitly cancelled
  — leaves a work-in-progress balance that remains visible as unresolved, rather than being automatically
  absorbed or written off without anyone deciding to.
WHY_IT_MATTERS: >
  Automatic silent write-off of an abandoned order's value would erase a real cost without anyone approving that
  loss; leaving it invisible would understate what is actually still outstanding.
DISCONFIRMING_OBSERVATION: >
  An abandoned production order's consumed value either disappears from the ledger with no compensating entry,
  or remains but is indistinguishable from that of an order still genuinely in progress.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Consume components on a production order, then leave it dormant with no further action, and check both whether
  its value persists and whether it can be distinguished from active orders.
```

## G06-MRP_ACCOUNT-Q011

```yaml
QID: G06-MRP_ACCOUNT-Q011
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Manually writing off or clearing a stranded work-in-progress balance requires a distinct, deliberate action
  separate from ordinary order completion, rather than being an incidental side effect of some other routine
  action.
WHY_IT_MATTERS: >
  If a stranded balance can be cleared as a side effect of an unrelated action, a real, uninvestigated loss can
  leave the books without anyone having actually decided to write it off.
DISCONFIRMING_OBSERVATION: >
  A stranded work-in-progress balance disappears from the ledger as a side effect of an action whose primary
  purpose was something else, with no distinct write-off record created.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Identify a stranded production order's work-in-progress balance and attempt to clear it both through a
  dedicated write-off action and through an unrelated routine action, comparing the results.
```

## G06-MRP_ACCOUNT-Q012

```yaml
QID: G06-MRP_ACCOUNT-Q012
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A financial report generated while a production order is still open reflects that order's accumulated
  work-in-progress value as part of the reported position, rather than the value only becoming visible once the
  order closes.
WHY_IT_MATTERS: >
  A report that ignores open production understates the true financial position at any interim point in time,
  which matters most exactly at a period cut-off.
DISCONFIRMING_OBSERVATION: >
  A financial report run while a production order is open and holding consumed value shows a total position that
  excludes that value entirely, as though it did not exist until the order closes.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate a standard financial report while a production order is open and partially consumed, and check
  whether that order's value contributes to the reported figures.
```

## G06-MRP_ACCOUNT-Q013

```yaml
QID: G06-MRP_ACCOUNT-Q013
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A production order whose components are consumed in one accounting period and whose output is completed in a
  later period is allowed to carry a non-zero in-process value across that period boundary, rather than being
  forced to artificially resolve to zero at the period's end.
WHY_IT_MATTERS: >
  Forcing a false resolution at period end would misstate both the closing and opening period's figures for the
  sake of a boundary that production itself does not respect.
DISCONFIRMING_OBSERVATION: >
  A production order genuinely still open and holding consumed value at a period's end shows a zero or cleared
  value in that period's closing figures, with the value reappearing afterward with no compensating entry
  explaining the gap.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Start a production order in one period, complete it in the following period, and inspect the closing figures
  of the first period for the order's in-process value.
```

## G06-MRP_ACCOUNT-Q014

```yaml
QID: G06-MRP_ACCOUNT-Q014
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When production spans a period boundary, each period's own closing figures are correct without requiring a
  manual, ad-hoc correcting entry to make them balance.
WHY_IT_MATTERS: >
  A structural need for manual correction every time production straddles a period is a standing source of error
  and delay at exactly the moment figures are under the most scrutiny.
DISCONFIRMING_OBSERVATION: >
  A production order spanning a period boundary produces closing figures in either period that only balance
  correctly after a manual correcting entry is added outside the normal posting flow.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Run a production order across a period boundary through to completion and close both periods without any
  manual correcting entries, then check whether both periods' figures are internally consistent.
```

## G06-MRP_ACCOUNT-Q015

```yaml
QID: G06-MRP_ACCOUNT-Q015
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The date used to post a component's consumption value or a finished item's output value follows the actual
  date that event occurred (or a defined period-lock substitution rule), not the date the production order was
  originally created.
WHY_IT_MATTERS: >
  Posting every event under the order's original creation date would place costs in the wrong period whenever
  production takes any real time to complete.
DISCONFIRMING_OBSERVATION: >
  A production order created in one period has its output, completed in a later period, posted under the
  original creation date rather than the date output actually occurred.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Create a production order in one period, complete its output in a later period, and check the posting date
  assigned to the output value.
```

## G06-MRP_ACCOUNT-Q016

```yaml
QID: G06-MRP_ACCOUNT-Q016
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the period a consumption or output event would naturally post to has already been locked, the posting is
  redirected to an open period or explicitly blocked by a defined rule, rather than silently forced into the
  locked period.
WHY_IT_MATTERS: >
  A silent posting into a locked period defeats the purpose of the lock and can invalidate figures that have
  already been reported and relied upon.
DISCONFIRMING_OBSERVATION: >
  A consumption or output event whose natural date falls in an already-locked period posts into that locked
  period without any block, warning, or redirection.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Lock an accounting period, then attempt to post a production consumption or output event whose natural date
  falls inside that locked period.
```

## G06-MRP_ACCOUNT-Q017

```yaml
QID: G06-MRP_ACCOUNT-Q017
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a production order yields both a primary output and a by-product, the amounts actually posted to the
  ledger for each of them follow the same split that production defines between them, rather than the ledger
  independently posting the entire order's value to only one of the two.
WHY_IT_MATTERS: >
  If the posted ledger values do not follow production's own defined split, the general ledger and the
  production record disagree about the same event, and whichever one is relied on for reporting is wrong.
DISCONFIRMING_OBSERVATION: >
  A production order's by-product has a value defined by its own split rule, but the amount actually posted to
  the ledger for the primary output equals the full order cost as though no split existed.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure a production order to yield a by-product under a defined split rule, complete it, and compare the
  ledger's posted primary-output and by-product values against the rule production itself defines.
```

## G06-MRP_ACCOUNT-Q018

```yaml
QID: G06-MRP_ACCOUNT-Q018
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When a by-product is configured with its own independent value rather than a residual method, the ledger posts
  that configured value for the by-product, rather than posting whatever remains after the primary output's cost
  is subtracted.
WHY_IT_MATTERS: >
  If the ledger silently reverts to a residual calculation regardless of configuration, a by-product with a
  genuinely known market value is never reflected correctly in the books.
DISCONFIRMING_OBSERVATION: >
  A by-product configured with an explicit independent value is posted to the ledger at a different amount —
  specifically, whatever residual remains after the primary output is valued first.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a by-product with an explicit independent value, complete the order, and check the amount posted to
  the ledger for the by-product against the configured value.
```

## G06-MRP_ACCOUNT-Q019

```yaml
QID: G06-MRP_ACCOUNT-Q019
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A by-product produced in an unplanned quantity still has its full actual quantity reflected in the amount
  posted to the ledger, rather than only the planned quantity being posted and the excess left with no ledger
  value at all.
WHY_IT_MATTERS: >
  Real output leaving the process with no corresponding ledger value would let inventory silently exist without
  a cost basis, distorting margin whenever it is later sold or used.
DISCONFIRMING_OBSERVATION: >
  A by-product produced in a quantity greater than planned results in a posted ledger value that only accounts
  for the planned quantity, leaving the excess quantity with no corresponding posted value.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete a production order that yields a by-product quantity different from what was planned, and check
  whether the entire actual quantity is reflected in the amount posted to the ledger.
```

## G06-MRP_ACCOUNT-Q020

```yaml
QID: G06-MRP_ACCOUNT-Q020
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The specific split applied between a primary output and its by-product on a given order can be reconstructed
  after the fact from that order's own retained evidence, without needing to re-derive it from an external
  assumption.
WHY_IT_MATTERS: >
  An unreconstructable split cannot be defended to a reviewer or corrected if it is later found to be wrong,
  since there would be no record of how it was reached.
DISCONFIRMING_OBSERVATION: >
  A completed order's evidence shows the final values assigned to primary output and by-product but retains no
  record of the basis or rule used to reach that particular split.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Complete a production order with a by-product split and attempt to reconstruct, from the order's own retained
  records alone, how the split was determined.
```

## G06-MRP_ACCOUNT-Q021

```yaml
QID: G06-MRP_ACCOUNT-Q021
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Material or a partially built item scrapped during production is posted to a defined, identifiable ledger
  destination, rather than its value being folded silently into the amount posted as the finished item's unit
  cost.
WHY_IT_MATTERS: >
  Scrap value silently posted into the finished item's ledger cost hides an operational problem behind what
  looks like a normal posted cost, and makes the true posted cost of good output impossible to see.
DISCONFIRMING_OBSERVATION: >
  A production order with a deliberately introduced scrap event posts a finished-item ledger value higher than
  an otherwise-identical scrap-free order by exactly the scrapped amount, with no separate posted scrap entry
  anywhere.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete two otherwise-identical production orders, one with a deliberate scrap event and one without, and
  compare both the resulting posted ledger values and the presence of any distinct posted scrap entry.
```

## G06-MRP_ACCOUNT-Q022

```yaml
QID: G06-MRP_ACCOUNT-Q022
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Scrap recorded before a production order is marked complete and scrap recorded after completion are both
  posted to the ledger according to the same defined destination rule; the timing of the recording relative to
  completion does not itself change which ledger account receives the value.
WHY_IT_MATTERS: >
  If timing alone changes which ledger account receives scrap value, two operationally identical scrap events
  would be reported completely differently purely because of when someone happened to log them.
DISCONFIRMING_OBSERVATION: >
  An identical scrap quantity and cause is posted to a different ledger account depending solely on whether it
  was recorded before or after the order was marked complete.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record an equivalent scrap event once before an order's completion and once after completion on an
  otherwise-identical order, and compare the ledger destinations.
```

## G06-MRP_ACCOUNT-Q023

```yaml
QID: G06-MRP_ACCOUNT-Q023
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether scrap value is expensed immediately at the time it is recorded, or held within the order's in-process
  value until the order closes, follows one defined, consistent rule rather than depending on which entry path
  was used to record the scrap.
WHY_IT_MATTERS: >
  Inconsistent treatment depending on entry path would let the same real event produce two different financial
  outcomes purely by accident of how someone happened to record it.
DISCONFIRMING_OBSERVATION: >
  The same scrap event, recorded through two different available entry paths, results in the value being
  expensed immediately through one path and held in work-in-progress through the other.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record equivalent scrap events through each available entry path on otherwise-identical orders and compare how
  the value is treated in each case.
```

## G06-MRP_ACCOUNT-Q024

```yaml
QID: G06-MRP_ACCOUNT-Q024
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The ledger destination to which a recorded scrap event's value posts is governed by a configuration or
  authorization distinct from whatever access allows a person to physically record that a scrap event occurred,
  so the two are not bundled into one blanket permission.
WHY_IT_MATTERS: >
  If recording a scrap event and controlling its financial destination are governed by the same single
  permission, a person able to log physical scrap could also freely redirect where a real loss lands in the
  books.
DISCONFIRMING_OBSERVATION: >
  A user holding only the access needed to physically record a scrap event is also able to determine or change
  which ledger destination that scrap's value posts to.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Attempt to influence or select the ledger destination for a scrap event's posted value using an account that
  holds only ordinary scrap-recording access.
```

## G06-MRP_ACCOUNT-Q025

```yaml
QID: G06-MRP_ACCOUNT-Q025
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The cost of an operation or labour tied to a work order is either capitalized into the produced item's cost or
  expensed as a period cost according to one defined, consistent rule, rather than the choice being made ad hoc
  per order.
WHY_IT_MATTERS: >
  An ad hoc choice between capitalizing and expensing the same kind of cost would make unit costs incomparable
  between otherwise-identical orders.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical orders' operation cost is capitalized in one and expensed in the other with no
  configuration difference between them that explains it.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Complete two otherwise-identical orders under identical configuration and compare whether operation cost is
  treated the same way in both.
```

## G06-MRP_ACCOUNT-Q026

```yaml
QID: G06-MRP_ACCOUNT-Q026
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a given operation's cost is capitalized is fixed by configuration set before production starts;
  changing that configuration while an order is already open does not retroactively reclassify cost already
  posted for that order.
WHY_IT_MATTERS: >
  Retroactively reclassifying already-posted cost when a setting changes would make historical figures unstable
  and unreproducible.
DISCONFIRMING_OBSERVATION: >
  Changing the capitalize-or-expense configuration for an operation while an order using it is still open causes
  the cost already posted for that order to change classification without a new posting event.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post some operation cost on an open order, then change the relevant configuration, and check whether the
  already-posted cost's classification changes.
```

## G06-MRP_ACCOUNT-Q027

```yaml
QID: G06-MRP_ACCOUNT-Q027
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An operation's cost rate is fixed at the time the operation is recorded; a later change to that rate does not
  retroactively alter the value already posted for an operation recorded before the change.
WHY_IT_MATTERS: >
  Retroactive rate changes to already-posted work would make completed periods' figures move after the fact for
  reasons unrelated to any new event.
DISCONFIRMING_OBSERVATION: >
  Changing an operation's cost rate after an operation was already recorded and posted causes the previously
  posted value for that operation to change to reflect the new rate.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Record and post an operation at one rate, change the rate afterward, and check whether the original posted
  value changes.
```

## G06-MRP_ACCOUNT-Q028

```yaml
QID: G06-MRP_ACCOUNT-Q028
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An operation recorded with an undefined duration or an undefined rate does not silently register as a
  zero-cost operation; the gap is flagged in a way that is distinguishable from a genuinely zero-cost operation.
WHY_IT_MATTERS: >
  A silent zero indistinguishable from a genuine zero hides missing information that should trigger a
  correction, understating the true cost of the item produced.
DISCONFIRMING_OBSERVATION: >
  An operation recorded with no duration or rate defined posts a zero cost that is indistinguishable in the
  record from an operation that is genuinely and correctly costed at zero.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record an operation with a deliberately undefined duration or rate and inspect whether the resulting posted
  value is distinguishable from a legitimately zero-cost operation.
```

## G06-MRP_ACCOUNT-Q029

```yaml
QID: G06-MRP_ACCOUNT-Q029
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reversing or unbuilding a completed production order after its cost has already been posted produces an
  explicit, separate compensating entry, rather than deleting or silently editing the original posted values.
WHY_IT_MATTERS: >
  Silently editing a posted figure destroys the record of what was actually reported for a period that may
  already have been closed and relied upon by others.
DISCONFIRMING_OBSERVATION: >
  Unbuilding a completed, posted production order changes the original posted values in place, with no separate
  compensating entry created and no trace that the original figures ever existed.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete and post a production order, then reverse or unbuild it, and check whether the original posted entry
  still exists alongside a new compensating entry.
```

## G06-MRP_ACCOUNT-Q030

```yaml
QID: G06-MRP_ACCOUNT-Q030
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Components restored to inventory when an order is unbuilt are restored at the same value they were originally
  consumed at, not at whatever value is current for that component at the time of the unbuild.
WHY_IT_MATTERS: >
  Restoring at a different value than was consumed creates a value out of nowhere (or destroys one), unrelated to
  any real event.
DISCONFIRMING_OBSERVATION: >
  A component's cost has changed since it was consumed by an order; unbuilding that order restores the component
  to inventory at its current value rather than the value it was actually consumed at.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Consume a component at one cost, change that component's cost afterward, then unbuild the order and check the
  value at which the component is restored.
```

## G06-MRP_ACCOUNT-Q031

```yaml
QID: G06-MRP_ACCOUNT-Q031
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When only part of a completed order's output quantity is unbuilt, the posted value for the portion that remains
  un-reversed stays intact and internally consistent, unaffected by the partial reversal.
WHY_IT_MATTERS: >
  A partial reversal that disturbs the untouched remainder's value would make a targeted correction have
  unintended effects on output nobody meant to touch.
DISCONFIRMING_OBSERVATION: >
  Unbuilding only part of a completed order's output quantity changes the posted value associated with the
  remaining, non-reversed portion of that same output.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Complete an order producing more than one unit, unbuild only part of the output quantity, and check whether the
  value of the untouched remainder changed.
```

## G06-MRP_ACCOUNT-Q032

```yaml
QID: G06-MRP_ACCOUNT-Q032
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Both a completed order's original posting and any later reversal of it remain visible in the retained trail,
  linked to each other and to the same order, rather than the reversal replacing or removing the original
  record.
WHY_IT_MATTERS: >
  A reviewer needs to see both what was originally reported and what corrected it; if the original disappears,
  the correction cannot be verified against anything.
DISCONFIRMING_OBSERVATION: >
  After a completed order is reversed, only the reversal's figures remain visible, with the original posted entry
  no longer retrievable from the trail.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Complete, post, and then reverse a production order, and check whether both the original posting and the
  reversal remain independently retrievable afterward.
```

## G06-MRP_ACCOUNT-Q033

```yaml
QID: G06-MRP_ACCOUNT-Q033
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the definition of a cost component (such as a labour or overhead rate) while production orders are
  already open does not retroactively alter the value already posted for consumption that occurred before the
  change.
WHY_IT_MATTERS: >
  Retroactive changes to already-posted values undermine the reliability of any figure reported before the rate
  change took effect.
DISCONFIRMING_OBSERVATION: >
  Changing a cost component's rate while an order is open causes the value already posted for consumption that
  happened before the change to update to reflect the new rate.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Post some consumption under one rate on an open order, change the rate, and check whether the already-posted
  value changes.
```

## G06-MRP_ACCOUNT-Q034

```yaml
QID: G06-MRP_ACCOUNT-Q034
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  For an order open at the moment a cost component's rate changes and completed afterward, the portion of value
  posted before the change uses the old rate and the portion posted after uses the new rate, rather than one
  rate being applied to the whole order regardless of timing.
WHY_IT_MATTERS: >
  Applying one rate to the whole order regardless of when consumption actually happened would misstate the
  order's true cost relative to when the resources were actually used.
DISCONFIRMING_OBSERVATION: >
  An order spanning a rate change posts its entire value — both before and after the change — under a single
  rate, rather than splitting according to when each portion of consumption actually occurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Open an order, post some consumption, change the relevant rate, post further consumption, then complete the
  order and inspect which rate(s) were applied to which portion.
```

## G06-MRP_ACCOUNT-Q035

```yaml
QID: G06-MRP_ACCOUNT-Q035
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A change to a cost component's definition applies according to one documented, consistent scope rule rather
  than the actual scope depending on incidental factors unrelated to that rule.
WHY_IT_MATTERS: >
  An undocumented or inconsistent scope rule makes it impossible to predict, or later explain, which orders were
  affected by a given rate change.
DISCONFIRMING_OBSERVATION: >
  Two orders that should be equally affected by a cost component change under the documented scope rule end up
  treated differently, with no configuration difference between them that explains why.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a cost component's definition and check whether all orders that the documented scope rule says should be
  affected are, in fact, affected consistently.
```

## G06-MRP_ACCOUNT-Q036

```yaml
QID: G06-MRP_ACCOUNT-Q036
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cost component changed to a value that is negative or otherwise nonsensical for that kind of cost is either
  rejected at the point of the change, or, if accepted, its downstream effect on production cost is at minimum
  visibly flagged rather than silently propagated.
WHY_IT_MATTERS: >
  An unnoticed nonsensical rate silently propagating into every subsequent order's cost would corrupt a wide
  range of figures from a single unnoticed data-entry error.
DISCONFIRMING_OBSERVATION: >
  A clearly nonsensical value is accepted as a cost component's definition and subsequently produces production
  order costs reflecting that nonsensical value with no warning or flag anywhere.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Attempt to set a cost component to a deliberately nonsensical value and observe both whether it is accepted and
  what happens to orders that use it afterward.
```

## G06-MRP_ACCOUNT-Q037

```yaml
QID: G06-MRP_ACCOUNT-Q037
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A rounding difference between a component's consumed quantity, its unit cost, and the monetary amount actually
  posted is captured by a defined rule rather than the residual simply being discarded and never appearing
  anywhere.
WHY_IT_MATTERS: >
  A discarded residual, repeated across enough transactions, becomes a real and untraceable leakage of value that
  nobody can account for.
DISCONFIRMING_OBSERVATION: >
  A deliberately chosen quantity and unit cost that do not divide evenly produce a posted amount whose rounding
  difference cannot be found in any record after the posting.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Consume a quantity and unit cost combination chosen to produce a non-trivial rounding difference and search the
  resulting records for where that difference landed.
```

## G06-MRP_ACCOUNT-Q038

```yaml
QID: G06-MRP_ACCOUNT-Q038
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Small rounding differences accumulated across many consumption lines on the same order remain bounded and
  reconciled at the order level, rather than compounding into a materially incorrect order total.
WHY_IT_MATTERS: >
  An unbounded accumulation of small roundings across a high-line-count order could eventually produce a total
  noticeably different from what the true underlying figures support.
DISCONFIRMING_OBSERVATION: >
  An order with a large number of small consumption lines, each individually rounded, produces a total that
  differs materially from the unrounded sum of the same lines.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Construct an order with many small consumption lines chosen to maximize rounding effects, and compare its
  posted total against the unrounded theoretical sum.
```

## G06-MRP_ACCOUNT-Q039

```yaml
QID: G06-MRP_ACCOUNT-Q039
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The precision applied when rounding a posted monetary amount follows the currency's own defined decimal
  precision consistently, rather than following the component's quantity precision or an unrelated default.
WHY_IT_MATTERS: >
  Using the wrong precision basis produces posted amounts that are technically invalid for the currency they are
  recorded in, which can break downstream reconciliation.
DISCONFIRMING_OBSERVATION: >
  A posted monetary amount is rounded to a precision that matches the component's quantity precision rather than
  the currency's own defined decimal precision.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Consume a component whose quantity precision differs from the posting currency's decimal precision, and check
  which precision the posted amount actually follows.
```

## G06-MRP_ACCOUNT-Q040

```yaml
QID: G06-MRP_ACCOUNT-Q040
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The rounded monetary value posted to the ledger for a given consumption or output event and the value shown on
  the production order's own cost record for that same event agree with each other, rather than two different
  figures being reported for the same event in two places.
WHY_IT_MATTERS: >
  Two different numbers reported for the same real event destroys confidence in either figure and makes
  reconciliation between the two views impossible.
DISCONFIRMING_OBSERVATION: >
  The monetary value posted to the ledger for a specific consumption or output event differs from the value shown
  for that same event on the production order's own cost record.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a consumption or output event and compare the value shown in the ledger against the value shown on the
  production order's own record for the identical event.
```

## G06-MRP_ACCOUNT-Q041

```yaml
QID: G06-MRP_ACCOUNT-Q041
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the same bill of materials is used to produce the same item in more than one company or legal entity, each
  entity's own valuation configuration (method and accounts) governs the postings made for production performed
  under that entity, independent of the other entity's configuration.
WHY_IT_MATTERS: >
  If one entity's configuration leaked into another's postings, each entity's financial statements would no
  longer reflect the settings it is actually supposed to operate under.
DISCONFIRMING_OBSERVATION: >
  Two entities configured with different valuation settings, producing the same item from the same shared bill,
  end up with postings that reflect only one of the two configurations for both entities.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure two entities with different valuation settings sharing one bill of materials, produce the item under
  each entity, and compare the resulting postings against each entity's own configuration.
```

## G06-MRP_ACCOUNT-Q042

```yaml
QID: G06-MRP_ACCOUNT-Q042
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A valuation setting changed in one company does not alter the postings already made, or the configuration
  currently in effect, for a different company that happens to share the same bill of materials.
WHY_IT_MATTERS: >
  Cross-entity leakage of a configuration change would let an action taken in one legal entity silently affect
  the books of an entirely separate one.
DISCONFIRMING_OBSERVATION: >
  Changing a valuation setting in one company changes either the postings or the effective configuration observed
  in a different company that shares the same bill.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a valuation setting in one company and check whether a different company sharing the same bill of
  materials is affected.
```

## G06-MRP_ACCOUNT-Q043

```yaml
QID: G06-MRP_ACCOUNT-Q043
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Which company's accounts receive a given production posting is determined unambiguously by the entity actually
  performing that production, not by which company originally authored the shared bill of materials.
WHY_IT_MATTERS: >
  Posting to the wrong entity's accounts based on the bill's origin rather than the producing entity would
  systematically misstate both entities' figures.
DISCONFIRMING_OBSERVATION: >
  A production order run under one company posts to the accounts of a different company — specifically, the
  company that originally authored the shared bill of materials.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Produce an item under a company different from the one that authored the shared bill of materials, and check
  which company's accounts receive the posting.
```

## G06-MRP_ACCOUNT-Q044

```yaml
QID: G06-MRP_ACCOUNT-Q044
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the entity performing production lacks a required valuation account in its own configuration, production
  either blocks with a clearly identifiable gap, or the missing configuration is surfaced, rather than the
  posting silently falling through to an unrelated default account.
WHY_IT_MATTERS: >
  A silent fallback to an unintended account would misplace real financial activity into the wrong place in the
  books with nothing to alert anyone that it happened.
DISCONFIRMING_OBSERVATION: >
  A company missing a required valuation account configuration still completes production, with the resulting
  posting landing in an account that was never actually intended for this purpose, and with no warning raised.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Remove or leave unset a required valuation account for a producing company, attempt to complete a production
  order under that company, and observe what happens.
```

## G06-MRP_ACCOUNT-Q045

```yaml
QID: G06-MRP_ACCOUNT-Q045
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Manually adjusting a produced item's already-posted cost is restricted to a distinct level of authorization,
  separate from the authorization needed to execute ordinary production.
WHY_IT_MATTERS: >
  If ordinary production access is enough to alter an already-posted cost, the control that manual cost
  adjustment is meant to require does not actually exist.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary production-execution access is able to manually adjust a produced item's
  already-posted cost.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Attempt a manual adjustment to a produced item's already-posted cost using an account that holds only ordinary
  production access.
```

## G06-MRP_ACCOUNT-Q046

```yaml
QID: G06-MRP_ACCOUNT-Q046
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A manual adjustment to a produced item's already-posted cost leaves a retained trace identifying who made the
  change, when, and both the value before and the value after.
WHY_IT_MATTERS: >
  Without that trace, a materially changed cost figure cannot be distinguished from an original one, or
  investigated if it turns out to be wrong.
DISCONFIRMING_OBSERVATION: >
  A manual adjustment to a produced item's posted cost is applied, and the retained trail shows only the new
  value, with no record of who made the change, when, or what the prior value was.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  Manually adjust a produced item's already-posted cost and inspect the retained trail for who, when, and the
  before/after values.
```

## G06-MRP_ACCOUNT-Q047

```yaml
QID: G06-MRP_ACCOUNT-Q047
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A manual adjustment made to a produced item's cost after that item has already moved further downstream (sold,
  or consumed as a component in another order) does not silently and automatically alter those downstream
  postings without an explicit, separate decision to propagate the change.
WHY_IT_MATTERS: >
  Silent automatic propagation into downstream figures already reported elsewhere could restate results nobody
  intended to reopen.
DISCONFIRMING_OBSERVATION: >
  Adjusting a produced item's cost after it has already been sold or consumed further downstream causes the
  downstream posting to change automatically, with no distinct, explicit propagation action taken.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Adjust a produced item's cost after it has already moved downstream (sold or consumed further) and check
  whether the downstream posting changes automatically.
```

## G06-MRP_ACCOUNT-Q048

```yaml
QID: G06-MRP_ACCOUNT-Q048
MODULE: mrp_account
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two adjustments to the same produced item's cost occurring at nearly the same time are either resolved
  deterministically (one clearly wins, or both are combined by a defined rule) or the conflict is detected and
  surfaced, rather than one adjustment being silently lost without a trace.
WHY_IT_MATTERS: >
  A silently lost concurrent adjustment would mean an approved change to a financial figure simply never took
  effect, with no indication to anyone that it disappeared.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous adjustments to the same produced item's cost are attempted, and one of them is silently
  discarded with no trace, warning, or conflict indication of any kind.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Attempt two adjustments to the same produced item's cost at nearly the same time and inspect whether both are
  accounted for, deterministically resolved, or one is silently lost.
```

---
## GMVQ Internal QA Checklist

- [x] 48 distinct MVQ records; no padding — every record targets a distinct hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module name
      appears in question text.
- [x] Bridge-module seam test applied to every question: each fails only where production's own internally
      generated cost is translated into a ledger fact; none would still make sense with production and the
      ledger used entirely apart.
- [x] Component consumption value versus finished-item value represented (Q001-Q004).
- [x] Standard-versus-actual variance and its traceability represented (Q005-Q008).
- [x] Work-in-progress position while an order is open, and what strands it, represented (Q009-Q012).
- [x] Period straddle between component consumption and output completion represented (Q013-Q016).
- [x] By-product valuation splitting one cost across two outputs represented (Q017-Q020).
- [x] Scrap during production and its charged destination represented (Q021-Q024).
- [x] Operation/labour cost capitalized versus expensed represented (Q025-Q028).
- [x] Order reversed or unbuilt after posting — compensating entry, not silent edit — represented (Q029-Q032).
- [x] Cost component changed while orders are open represented (Q033-Q036).
- [x] Rounding between quantity, unit cost, and posted amount represented (Q037-Q040).
- [x] Per-company valuation settings on a shared bill represented (Q041-Q044).
- [x] Manual adjustment authority and traceability after the fact represented (Q045-Q048).
- [x] Role/permission boundary represented (Q011, Q024, Q045, Q048).
- [x] Tenant/company boundary represented (Q041-Q044).
- [x] Cancellation/reversal represented (Q029-Q032).
- [x] Concurrency represented (Q048).
- [x] Cross-module dependency represented (Q012, Q027, Q040).
- [x] No specific Thai legal or tax requirement asserted anywhere in this bank.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
