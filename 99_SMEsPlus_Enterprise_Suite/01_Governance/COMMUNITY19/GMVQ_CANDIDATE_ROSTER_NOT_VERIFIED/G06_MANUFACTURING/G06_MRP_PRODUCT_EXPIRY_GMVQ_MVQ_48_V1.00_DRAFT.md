# SMEsPlus ENTERPRISE SUITE
## GMVQ — G06 MANUFACTURING / mrp_product_expiry Module Adversarial MVQ Bank

**Document ID:** GMVQ-G06-MRP_PRODUCT_EXPIRY-MVQ48-V1.00
**Group:** G06 MANUFACTURING
**Module Metadata:** `mrp_product_expiry`
**Wave:** W2
**Author Cell:** P10
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) questions for `mrp_product_expiry`, a BRIDGE
module per GMVQ_BRIDGE_MODULE_RULE_V1.00: it exists only to make shelf-life tracking and
production behave correctly when used together, and owns almost no behaviour of its own.

Every question below was tested against the bridge rule: "if this capability were removed and
shelf-life tracking and production were used entirely apart, would the question still make
sense?" A question that survives that test is not in this bank. Every question here fails only
at the seam — the point where a component's date and an output's date can legitimately disagree
and something has to decide which governs, when, and what happens to what was already committed
under the other answer.

Coverage spans the seam categories from the bridge rule: ordering, partiality, ownership, timing,
reversal, quantity and money, lifecycle mismatch, error asymmetry, and authority, applied across
the concrete grounds in the group brief — date derivation and precedence, expiry occurring between
reservation and consumption, blocking policy, output/component date inversion, multi-day runs,
rework and unbuild, mid-flight rule changes, backward traceability, and write-down of committed
but unconsumed stock.

The question text is source-neutral. It does not name any vendor or product, any technical
identifier (model, table, field, method, XML ID, API path), or the module's own metadata name —
`mrp_product_expiry` appears only in the `MODULE:` field of each question block, never in
question text.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` — a concrete result that
  would prove the paired `HYPOTHESIS` wrong, not a restatement of it.
- No padding: each of the 48 questions tests a materially distinct hypothesis; no two share a
  disconfirming observation or reduce to a variation of another question in this bank.
- `LAYER: BASE` marks questions about the seam's own configuration (which rule governs, whether
  it can be disabled, who may change it). `LAYER: PROCESS` marks questions about behaviour during
  a live production, rework, or reversal event. Both layers exist for this seam and are tagged
  throughout.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/observation
  from the relevant lane.
- `MODULE + QID` is a Research Evidence Join Key only. No coverage or compliance status is
  derived from the existence of a question.
- This document is PREPARED ONLY / NOT FROZEN. It carries no Boss approval and authorizes no
  merge, release, or gate closure.

## G06-MRP_PRODUCT_EXPIRY-Q001

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q001
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  There is exactly one governing rule for the output's date at the moment of production —
  either derived from the shortest-dated component consumed, or from a fixed rule of the
  output's own — and the two are never both applied to the same production event.
WHY_IT_MATTERS: >
  If both rules can apply to the same event, the output's date becomes whichever one a given
  path happened to compute last, and no one downstream can say which basis actually governed.
DISCONFIRMING_OBSERVATION: >
  The same production event yields two different candidate output dates — one from the shortest
  component date, one from the output's own fixed rule — with no recorded resolution of which
  one was actually applied.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A product with its own fixed shelf-life rule configured, produced from components that also
  carry dates; trace which value the finished lot actually receives.
```

## G06-MRP_PRODUCT_EXPIRY-Q002

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q002
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A component that is not itself date-tracked is excluded from the computation of the output's
  date, rather than being silently treated as having no expiry (and therefore as the latest
  possible date, skewing the result).
WHY_IT_MATTERS: >
  If an untracked component is treated as "never expires," it can never be the shortest date, so
  its presence quietly widens the computed output date beyond what the tracked components justify.
DISCONFIRMING_OBSERVATION: >
  Adding an untracked component to an order changes the computed output date compared to the same
  order without it, even though the untracked component contributes no date information.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  An order mixing date-tracked and non-tracked components; compute the output date with and
  without the non-tracked component present and compare.
```

## G06-MRP_PRODUCT_EXPIRY-Q003

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q003
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A component's date passing after it is reserved to an order but before it is actually consumed
  is detected at the moment of consumption, not only at the moment of reservation.
WHY_IT_MATTERS: >
  A check performed only at reservation time lets a component age past its date, undetected,
  for the entire time it sits reserved, and lets it flow into the output regardless.
DISCONFIRMING_OBSERVATION: >
  A component reserved while still within date is consumed after its date has passed, and the
  system's expiry check shows no evaluation at the consumption event itself.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reserve a component within date, hold the order open until the component's date passes, then
  consume it; check whether a fresh evaluation occurs at consumption.
```

## G06-MRP_PRODUCT_EXPIRY-Q004

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q004
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Consuming a component already past its date follows one defined, discoverable policy —
  block, warn-and-allow, or silently proceed — applied consistently for a given product and
  actor, rather than varying by which consumption path is used.
WHY_IT_MATTERS: >
  An undefined or path-dependent policy means the same expired component can be refused in one
  workflow and consumed without comment in another, with no single answer for what should happen.
DISCONFIRMING_OBSERVATION: >
  Consuming the same expired component produces a block in one consumption path and silent
  success in another, for the same product and the same actor.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  An expired component available in stock; attempt to consume it through more than one available
  consumption path and compare the outcome.
```

## G06-MRP_PRODUCT_EXPIRY-Q005

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q005
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  An output is never assigned a computed date earlier than the date already held by a component
  it actually contains — the computation cannot invert the ordering of dates it was given.
WHY_IT_MATTERS: >
  A finished good dated to expire before an ingredient it contains is a value that cannot be
  physically true, and anyone relying on the output's date downstream is relying on a
  contradiction.
DISCONFIRMING_OBSERVATION: >
  A produced output's computed date is earlier than the date of a component actually consumed
  into it.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Produce an output from a component with a known date; compare the output's computed date
  against that component's date.
```

## G06-MRP_PRODUCT_EXPIRY-Q006

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q006
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  For a production run spanning more than one day, the date basis used for the output reflects
  the components' dates as of when they were actually consumed, not as of when they were first
  reserved at the start of the run.
WHY_IT_MATTERS: >
  A long run that locks in dates at reservation time can compute an output date from components
  whose dates had already moved on by the time they were physically used.
DISCONFIRMING_OBSERVATION: >
  A component reserved on day one and consumed on day three drives the output's computed date
  using its day-one date rather than any date basis current at day three.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Start a production order, reserve dated components, delay consumption across more than one day,
  then check which date snapshot the output computation actually used.
```

## G06-MRP_PRODUCT_EXPIRY-Q007

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q007
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Components returned to stock by a rework or unbuild event carry a date consistent with their
  own history (unchanged or a documented adjustment), rather than silently receiving a fresh
  date as if newly received.
WHY_IT_MATTERS: >
  A component that is quietly re-dated on return effectively erases the shelf-life consequence
  of however long it had already been committed, letting genuinely aged stock look fresh again.
DISCONFIRMING_OBSERVATION: >
  A component returned to stock by an unbuild carries a later date than the date it held
  immediately before being consumed, with no documented extension rule behind the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consume a dated component into an order, then unbuild or reverse that order; compare the
  component's date before consumption and after return.
```

## G06-MRP_PRODUCT_EXPIRY-Q008

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q008
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Changing the date-computation rule while production orders are already open applies only to
  orders started after the change, and does not retroactively recompute the date already assigned
  to an in-progress order.
WHY_IT_MATTERS: >
  A retroactive change can silently shift the shelf life of stock already produced or in
  production under the old rule, without anyone having re-evaluated it under the new one.
DISCONFIRMING_OBSERVATION: >
  An order already open when the rule changes shows its computed output date change after the
  rule is edited, with no new production or consumption event having occurred on that order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Open a production order under one date rule, change the rule while the order remains open, and
  check whether the order's already-computed date is altered.
```

## G06-MRP_PRODUCT_EXPIRY-Q009

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q009
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Given an output lot that has expired, the specific component (and its own lot) whose date
  actually drove that computation can be identified after the fact, not merely inferred from
  which components were generally used on the order.
WHY_IT_MATTERS: >
  Without a recorded causal link, a recall or root-cause review can only guess which incoming
  lot was responsible, and cannot isolate the same supplier or batch defect elsewhere.
DISCONFIRMING_OBSERVATION: >
  Tracing an expired output lot backward returns the full list of components used on the order,
  with no way to determine which single one actually set the output's date.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce an output whose date is driven by one specific component among several consumed; after
  the fact, attempt to trace which component actually determined the date.
```

## G06-MRP_PRODUCT_EXPIRY-Q010

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q010
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A component that expires while already committed to an open production order (reserved but not
  yet consumed) is written down through the same valuation event regardless of whether it is
  still attached to that order, and its committed state does not silently permit it to be
  consumed after the write-down.
WHY_IT_MATTERS: >
  If commitment to an open order exempts a component from write-down, expired value goes
  unrecognised for as long as the order stays open, and if it is still consumable after
  write-down, a value already recognised as lost re-enters the finished good regardless.
DISCONFIRMING_OBSERVATION: >
  A component held in an open order's reservation is skipped by the expiry write-down process,
  or is written down and then successfully consumed into the order afterward with no override
  event.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reserve a dated component to an open order, allow it to pass its date without consuming it,
  and check both whether it is written down and whether it can still be consumed afterward.
```

## G06-MRP_PRODUCT_EXPIRY-Q011

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q011
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A component that expires while reserved to one open order is released from that reservation (or
  otherwise flagged) rather than remaining silently reserved and unavailable to any other order
  indefinitely.
WHY_IT_MATTERS: >
  Silent, permanent reservation of now-worthless stock hides real availability from planning and
  can leave a written-down quantity looking, on paper, like it is still earmarked for use.
DISCONFIRMING_OBSERVATION: >
  A component's date passes while reserved to an order that never consumes it, and the
  reservation remains in place with no flag or release, indefinitely.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reserve a dated component to an order, let it pass its date without consumption or
  cancellation, and observe the reservation's state over time.
```

## G06-MRP_PRODUCT_EXPIRY-Q012

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q012
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A by-product generated at the same operation as the main output receives its date through the
  same documented computation as the main output, rather than an independent and differently
  sourced default.
WHY_IT_MATTERS: >
  A by-product whose date is computed differently from its sibling output can be materially wrong
  relative to what actually went into it, since both came from the same consumed components.
DISCONFIRMING_OBSERVATION: >
  The main output and a by-product from the same operation receive different computed dates even
  though both were generated from the same set of consumed components.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Run an operation that yields both a main output and a by-product from shared dated components;
  compare the date each one receives.
```

## G06-MRP_PRODUCT_EXPIRY-Q013

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q013
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Components consumed through an automatic (backflush-style) consumption path are evaluated for
  expiry status by the same rule as components consumed through a manually confirmed step.
WHY_IT_MATTERS: >
  If automatic consumption skips the check that manual consumption applies, the seam's protection
  quietly disappears for every order that happens to use the automatic path.
DISCONFIRMING_OBSERVATION: >
  An expired component consumed automatically produces no block or warning, while the same
  component consumed through a manual step is blocked or warned.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure a component for automatic consumption and let its date pass; compare the outcome to
  manually consuming an equally expired component on another order.
```

## G06-MRP_PRODUCT_EXPIRY-Q014

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q014
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where an order's components are consumed in more than one step over time, the output's final
  date basis is re-evaluated across all consumption events for that order, not fixed by whichever
  component happened to be consumed first.
WHY_IT_MATTERS: >
  Locking the output's date to the first partial consumption ignores a later component that may
  carry an earlier date, understating the real shelf-life risk of the finished output.
DISCONFIRMING_OBSERVATION: >
  A component consumed later in the order, with an earlier date than everything consumed before
  it, does not change the output's already-computed date.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Consume components on an order in two separate steps, with the later step's component carrying
  an earlier date than the first; check whether the output date updates.
```

## G06-MRP_PRODUCT_EXPIRY-Q015

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q015
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Scrapping a partially built item that had already absorbed dated components preserves, in the
  scrap event's own record, which components' dates were involved, rather than recording only a
  generic scrap quantity with no link back to those components.
WHY_IT_MATTERS: >
  Without that link, a pattern of scrap caused by components nearing their date is invisible to
  anyone reviewing scrap events after the fact.
DISCONFIRMING_OBSERVATION: >
  Scrapping a partially built item that contained dated components produces a scrap record with
  no reference to which component lots, or their dates, were consumed into it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Partially consume dated components into an order, scrap the in-progress item, and inspect the
  resulting scrap record for a link back to the consumed components.
```

## G06-MRP_PRODUCT_EXPIRY-Q016

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q016
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling a production order after partial consumption returns the consumed components to a
  state consistent with their actual physical condition — an already-expired component is not
  silently returned to stock as though it were still within date.
WHY_IT_MATTERS: >
  A reversal that ignores elapsed time can put stock back into circulation as usable when it has
  in fact expired since it was originally consumed.
DISCONFIRMING_OBSERVATION: >
  Cancelling an order returns a component to available stock with its pre-consumption date
  intact even though that date has since passed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Consume a dated component into an order, let its date pass while the order remains open, then
  cancel the order and inspect the returned component's date and availability state.
```

## G06-MRP_PRODUCT_EXPIRY-Q017

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q017
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  An order mixing a date-tracked component with a component carrying no date at all still
  produces a defined, documented output date (or a defined absence of one), rather than an
  undefined or inconsistent result depending on which component happens to be evaluated first.
WHY_IT_MATTERS: >
  An undefined mixed-input case is exactly the kind of edge condition that behaves differently
  across similar orders depending on incidental factors like component order or timing.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical orders, each mixing a dated and an undated component, produce different
  output dates with no difference in the actual components consumed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Produce from a mix of dated and undated components on two separate, otherwise identical orders,
  and compare the resulting output dates.
```

## G06-MRP_PRODUCT_EXPIRY-Q018

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q018
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A manual override of a computed output date is recorded distinctly from a system-computed date,
  so that later review can tell whether a given lot's date was calculated or entered by hand.
WHY_IT_MATTERS: >
  Without that distinction, a hand-entered date looks identical to a computed one, and a mistaken
  or intentionally lenient manual entry cannot be told apart from a genuine computation.
DISCONFIRMING_OBSERVATION: >
  A finished lot whose date was manually overridden displays and stores identically to a lot
  whose date was system-computed, with no marker distinguishing the two.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce one lot with a system-computed date and one lot where the date is manually overridden;
  compare the two lots' stored records for a distinguishing marker.
```

## G06-MRP_PRODUCT_EXPIRY-Q019

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q019
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Each production event computes its own output date independently from its own components,
  rather than one production run's shorter computed date leaking into a shared, product-level
  default applied to unrelated later runs of the same product.
WHY_IT_MATTERS: >
  A leaked product-level default would make one bad batch's short date silently apply to an
  entirely different, unrelated batch that never contained the offending component.
DISCONFIRMING_OBSERVATION: >
  Producing the same product a second time, from components with a longer date than the first
  run, still yields the first run's shorter computed date.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Produce the same product twice on different days with different component date profiles;
  compare each run's independently computed output date.
```

## G06-MRP_PRODUCT_EXPIRY-Q020

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q020
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where the date-computation rule for a product can be set per company or tenant, two companies
  sharing the same product definition can hold independently configured rules without one
  company's setting silently governing the other's production.
WHY_IT_MATTERS: >
  A shared setting masquerading as tenant-specific would let one company's shelf-life policy
  silently override another's on shared product data, defeating the tenant boundary.
DISCONFIRMING_OBSERVATION: >
  Changing the date-computation rule for a shared product under one company changes the computed
  output date for the same product produced under a different company.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Two companies or tenants sharing one product definition, each with an independently set date
  rule; change one company's rule and check whether the other company's production is affected.
```

## G06-MRP_PRODUCT_EXPIRY-Q021

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q021
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a component's own date is extended (requalified) after it is reserved but before it is
  consumed, an order still relying on the earlier date reflects the updated date at consumption
  time, rather than keeping a stale provisional value.
WHY_IT_MATTERS: >
  A stale provisional value understates the true shelf life of the output, potentially triggering
  unnecessary write-downs or an artificially short output date.
DISCONFIRMING_OBSERVATION: >
  A component's date is extended after reservation, and the order's provisional output date
  remains based on the original, now-superseded date through to actual consumption.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Reserve a component to an order, extend that component's own date before consumption, then
  consume it and check which date the order's computation actually used.
```

## G06-MRP_PRODUCT_EXPIRY-Q022

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q022
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Changing the date-computation rule for a product requires a permission distinct from the
  permission needed to run ordinary production on that product.
WHY_IT_MATTERS: >
  If any production operator can also change the shelf-life computation rule, a single actor can
  quietly reshape how every future batch's date is derived with no separate authorisation step.
DISCONFIRMING_OBSERVATION: >
  A user holding only ordinary production execution rights is able to change the product's
  date-computation rule with no additional permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with production-execution rights only, attempt to change the date-computation rule
  for a product and observe whether it is permitted.
```

## G06-MRP_PRODUCT_EXPIRY-Q023

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q023
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a production event consumes two lots of the same component with different dates, the
  earlier of the two dates is the one that governs the output's computed date, and both lots'
  identities remain individually recorded rather than collapsing into one undifferentiated
  consumption entry.
WHY_IT_MATTERS: >
  Averaging, ignoring, or recording only one of two differently dated lots either overstates the
  output's real shelf life or destroys the traceability needed to isolate a defective lot later.
DISCONFIRMING_OBSERVATION: >
  Consuming two differently dated lots of the same component produces an output date that is
  later than the earlier of the two lots' dates, or a consumption record naming only one lot.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Consume two lots of one component, with different dates, into a single production event; check
  the output's computed date and the consumption record's lot-level detail.
```

## G06-MRP_PRODUCT_EXPIRY-Q024

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q024
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Force-completing a production order (marking all quantities done outside the normal step
  sequence) still leaves a discoverable record of whether an expired component was consumed
  during that operation.
WHY_IT_MATTERS: >
  If a forced completion bypasses the same evidence trail as an ordinary completion, an expired
  consumption event can vanish from the record entirely rather than merely being unblocked.
DISCONFIRMING_OBSERVATION: >
  A production order force-completed with an expired component consumed mid-operation leaves no
  trace, in any log or record, that an expired component was involved.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Let a reserved component expire mid-operation, force-complete the order rather than following
  the normal step sequence, and check for any surviving record of the expired consumption.
```

## G06-MRP_PRODUCT_EXPIRY-Q025

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q025
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The output's date is not finalized until after the last component consumption event for that
  order has actually been recorded, so no operator action can lock in a date ahead of the
  consumption it is supposed to be based on.
WHY_IT_MATTERS: >
  A date finalized before the last consumption is recorded can be based on incomplete
  information, silently ignoring a later, possibly shorter-dated component.
DISCONFIRMING_OBSERVATION: >
  The output's date is marked final while a component consumption event for the same order is
  still pending or recorded afterward.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  On a multi-step order, mark the output's quality or date status before the final component
  consumption step completes, and check whether that status is treated as final.
```

## G06-MRP_PRODUCT_EXPIRY-Q026

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q026
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  An output moved out of production before its date computation is finalized is visibly marked
  provisional wherever it appears downstream, rather than presenting an unmarked value
  indistinguishable from a finalized date.
WHY_IT_MATTERS: >
  An unmarked provisional date can be acted on downstream (sold, shipped, promised) as if it were
  final, and then change underneath a commitment already made against it.
DISCONFIRMING_OBSERVATION: >
  A receiving process downstream of production displays a provisional output date with no
  indication that it is not yet final.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Move a produced output to a receiving location before its date computation is finalized, and
  inspect how that date is presented at the receiving end.
```

## G06-MRP_PRODUCT_EXPIRY-Q027

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q027
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Reworking a batch whose date was previously set by manual override results in a defined,
  documented outcome — either the override is explicitly preserved or explicitly replaced by a
  fresh computation — rather than an outcome that depends on which rework path is used.
WHY_IT_MATTERS: >
  An undefined outcome means the same rework action can silently discard a deliberate manual
  correction in one case and preserve it in another, with no way to predict which.
DISCONFIRMING_OBSERVATION: >
  Reworking two batches that both started from a manually overridden date produces a preserved
  override in one case and a recomputed date in the other, with no documented rule explaining
  the difference.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Manually override the date on two comparable batches, rework each one, and compare whether the
  override survives the rework in both cases.
```

## G06-MRP_PRODUCT_EXPIRY-Q028

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q028
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Substituting a component mid-order, after a provisional output date has already been computed
  from the original component, triggers a recomputation using the substitute's own date rather
  than leaving the original provisional value in place.
WHY_IT_MATTERS: >
  A provisional date left stale after a substitution can be based on a component that was never
  actually consumed, misrepresenting what is really inside the output.
DISCONFIRMING_OBSERVATION: >
  Substituting a component with a different date, after a provisional output date is set, leaves
  that provisional date unchanged through to completion.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Compute a provisional output date from an original component, substitute a different-dated
  component before consumption completes, and check whether the provisional date is recomputed.
```

## G06-MRP_PRODUCT_EXPIRY-Q029

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q029
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A reserved component that is itself approaching or has passed its date, while the production
  order that reserved it remains open and unconsumed, is surfaced to the planner as a visible
  warning rather than remaining silent until someone happens to notice at consumption time.
WHY_IT_MATTERS: >
  Silence here turns a preventable loss into a surprise discovered only when the order finally
  moves, by which point the write-down and any schedule disruption are already unavoidable.
DISCONFIRMING_OBSERVATION: >
  A component reserved to an order that stays open long enough for the component's date to pass
  generates no warning visible to planning before the order is eventually touched.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reserve a component to an order, leave the order open without consuming, and monitor whether
  any warning becomes visible as the component's date approaches and passes.
```

## G06-MRP_PRODUCT_EXPIRY-Q030

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q030
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A downstream delivery commitment already made against an expected output date is flagged when
  the underlying component situation later changes what that output date will actually be.
WHY_IT_MATTERS: >
  An unflagged, silently stale commitment lets a customer-facing promise stand on a date that
  production can no longer actually meet.
DISCONFIRMING_OBSERVATION: >
  A change to the components driving an order's expected output date leaves an already-made
  downstream delivery commitment referencing the original date with no flag raised.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Make a downstream commitment against an order's expected output date, then change a component
  on that order in a way that shifts the computed date, and check for a resulting flag.
```

## G06-MRP_PRODUCT_EXPIRY-Q031

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q031
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  The write-down cost of a component that expired while committed to a specific open order is
  attributable back to that order, rather than posting as an undifferentiated loss with no order
  reference.
WHY_IT_MATTERS: >
  Without an order reference, the true cost of holding stock too long against a particular job
  cannot be measured, and repeated losses on the same order type go unnoticed.
DISCONFIRMING_OBSERVATION: >
  A component write-down for stock committed to a specific open order posts with no reference
  back to that order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Let a component committed to a specific open order expire and be written down; inspect the
  write-down record for an order reference.
```

## G06-MRP_PRODUCT_EXPIRY-Q032

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q032
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When two open orders each provisionally depend on the same limited-dated component lot before
  either has actually consumed it, only the order that actually consumes the lot carries its date
  into a finalized output — the other order's provisional dependency does not silently become a
  second, contradictory claim on the same lot.
WHY_IT_MATTERS: >
  Two orders both treating the same not-yet-consumed lot as theirs can each compute a provisional
  date from it, and if both proceed, one of them is relying on stock it will never actually get.
DISCONFIRMING_OBSERVATION: >
  Two open orders both show a finalized output date derived from the same single lot of a
  limited-dated component that only one of them actually consumed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reserve the same limited lot of a component to two open orders, consume it on one, and check
  whether the other order's output still finalizes a date as though it had received that lot.
```

## G06-MRP_PRODUCT_EXPIRY-Q033

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q033
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When a produced lot is unbuilt and then rebuilt with a different composition of components, the
  traceability record correctly reflects the new components' dates rather than retaining the
  original build's now-irrelevant component-to-date links.
WHY_IT_MATTERS: >
  Stale traceability from a prior composition would point any later investigation at components
  that are no longer actually inside the current lot.
DISCONFIRMING_OBSERVATION: >
  After an unbuild and rebuild with different components, tracing the resulting lot's date basis
  still returns the original build's components rather than the ones actually used the second
  time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Build a lot, unbuild it, rebuild it from a different set of dated components, and trace the
  final lot's date basis back to the components actually used.
```

## G06-MRP_PRODUCT_EXPIRY-Q034

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q034
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where a setting exists to disable date propagation from components to the output entirely (so
  the output uses only its own fixed rule), that setting is discoverable through normal
  configuration and applies uniformly regardless of which type of component is involved.
WHY_IT_MATTERS: >
  A setting that is hard to find or applies inconsistently by component type creates a false
  sense of control over which rule actually governs a given product's output date.
DISCONFIRMING_OBSERVATION: >
  With component-to-output date propagation disabled for a product, the output's computed date
  still varies depending on which component was consumed.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Disable component-to-output date propagation for a product, then produce it from components
  with differing dates, and check whether the output's date is affected by which one was used.
```

## G06-MRP_PRODUCT_EXPIRY-Q035

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q035
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  When no component in an order carries a date at all, the output either receives a clearly
  defined default date or explicitly no date, and the outcome is consistent every time the same
  condition occurs, rather than failing unpredictably.
WHY_IT_MATTERS: >
  An unpredictable outcome for the fully-untracked case means the same class of product can end
  up with or without a date purely by chance of which run it went through.
DISCONFIRMING_OBSERVATION: >
  Two separate production runs, neither using any date-tracked component, produce outputs where
  one receives a date and the other does not, with no configuration difference between them.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Produce a product twice using only non-date-tracked components each time, and compare whether
  each output consistently receives (or consistently lacks) a computed date.
```

## G06-MRP_PRODUCT_EXPIRY-Q036

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q036
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The actual basis used to set a given output's date — which rule applied, and which component
  or lot governed if applicable — is permanently recorded against that output, not something
  that can only be re-derived, possibly incorrectly, from current data after the fact.
WHY_IT_MATTERS: >
  If the basis is not preserved, a later audit or recall investigation can only guess at what
  actually determined a lot's date, and that guess can be wrong if the source data has since
  changed.
DISCONFIRMING_OBSERVATION: >
  For an already-produced lot, no stored record indicates which rule or component actually
  determined its date — the answer is only obtainable by recomputing from current, possibly
  changed, source data.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Produce a lot, then change the source data that originally fed its date computation, and check
  whether the lot's own record still correctly states its original basis.
```

## G06-MRP_PRODUCT_EXPIRY-Q037

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q037
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When two users act on the same order at the same time — one consuming a dated component, one
  substituting a different-dated component — the order's final output date reflects a single,
  consistently determined outcome rather than a race whose result depends on which action's
  effect happened to be recorded last.
WHY_IT_MATTERS: >
  A silent race condition here produces a date that is not reproducible and cannot be explained
  after the fact, undermining confidence in every output date the seam produces under load.
DISCONFIRMING_OBSERVATION: >
  Repeating the same concurrent consume-and-substitute scenario yields different final output
  dates across repeated trials with identical inputs.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a component consumption and a component substitution on the same order at
  approximately the same time, repeated across multiple trials, and compare the resulting output
  dates.
```

## G06-MRP_PRODUCT_EXPIRY-Q038

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q038
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Consuming only part of a dated component's reserved quantity propagates the same date to the
  output as consuming the full reserved quantity would — the date basis does not depend on how
  much of the component was actually used.
WHY_IT_MATTERS: >
  If partial consumption were treated differently, the same physical component could yield two
  different output dates purely based on quantity split, with no principled reason for either.
DISCONFIRMING_OBSERVATION: >
  Consuming half of a dated component's reserved quantity produces a different output date than
  consuming the full reserved quantity of the same component would have.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Consume a partial quantity of a reserved dated component into one order, and the full reserved
  quantity of an equivalent component into a comparable order; compare output dates.
```

## G06-MRP_PRODUCT_EXPIRY-Q039

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q039
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Discovering, after an output has already shipped, that its date was computed incorrectly due to
  a component mixup is corrected through a defined, auditable path (such as a new corrective
  record), rather than by editing the original lot's stored date in place.
WHY_IT_MATTERS: >
  Editing a shipped lot's date in place destroys the record of what was actually communicated to
  whoever received it, and erases the evidence trail a correction should instead preserve.
DISCONFIRMING_OBSERVATION: >
  Correcting a shipped output's incorrect date is done by altering the original lot's stored date
  directly, with no separate corrective record and no trace of the original value.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Identify a shipped output with an incorrect date due to a component mixup, and attempt to
  correct it through whatever mechanism the seam provides.
```

## G06-MRP_PRODUCT_EXPIRY-Q040

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q040
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A co-product generated at the same operation as the main output, from the same consumed
  components, receives its date through a computation consistent with the main output's, rather
  than an independently and differently sourced value.
WHY_IT_MATTERS: >
  Two products from one shared set of components should not diverge in their shelf-life basis
  purely because one is labelled the main output and the other a co-product.
DISCONFIRMING_OBSERVATION: >
  A co-product and the main output from the same operation, sharing the same consumed
  components, receive dates computed by visibly different rules.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Run an operation yielding a main output and a co-product from the same dated components;
  compare the computation basis each one actually used.
```

## G06-MRP_PRODUCT_EXPIRY-Q041

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q041
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  The output's date exists in a clearly provisional state while the production order is still in
  progress, and is only marked final at a defined completion state — the transition from
  provisional to final is a distinct, observable event rather than an implicit side effect of an
  unrelated status change.
WHY_IT_MATTERS: >
  If finalization is an implicit side effect, no one can point to the moment a date became
  trustworthy, and an order could be treated as final prematurely by an unrelated status change.
DISCONFIRMING_OBSERVATION: >
  The output's date is treated as final by some downstream process while the production order
  itself is still shown as in progress, with no explicit finalization event having occurred.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Track a production order's state alongside its output date's provisional/final status across
  the order's full lifecycle, and identify the exact transition point.
```

## G06-MRP_PRODUCT_EXPIRY-Q042

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q042
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where a policy exists to prioritise consumption of the nearer-dated lot of a component (over a
  fresher lot of the same component), that policy is applied consistently across repeated
  production runs rather than left to incidental factors that produce different picks each time.
WHY_IT_MATTERS: >
  Inconsistent picking makes the output's computed date unpredictable across otherwise identical
  runs and defeats any attempt to plan around expected shelf life.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical production runs, drawing from the same available lots of a component,
  consume different lots and yield different output dates with no configuration change between
  them.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Make two lots of the same component available with different dates, run two otherwise identical
  production orders, and compare which lot each one actually consumes.
```

## G06-MRP_PRODUCT_EXPIRY-Q043

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q043
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where component consumption and production completion fall on different dates, the seam uses a
  single, documented one of the two (consumption date or completion date) as its basis, applied
  the same way on every order, rather than switching basis depending on incidental timing.
WHY_IT_MATTERS: >
  An undocumented or inconsistent basis means two orders with identical components but different
  elapsed time between consumption and completion produce dates that cannot be compared or
  explained.
DISCONFIRMING_OBSERVATION: >
  Two orders with identical component dates, differing only in the gap between consumption and
  completion, are computed using different bases (one keyed to consumption, one to completion).
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Run two orders with identical component dates but different elapsed time between consumption
  and completion, and compare which date basis each one's output computation actually used.
```

## G06-MRP_PRODUCT_EXPIRY-Q044

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q044
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Where blocking consumption of an expired component is an opt-in setting per product or
  category, a product for which the setting has never been configured defaults to blocking (the
  safer behaviour), not to silently proceeding.
WHY_IT_MATTERS: >
  A silent-proceed default for an unconfigured product means every newly introduced product is
  unprotected until someone remembers to turn the setting on.
DISCONFIRMING_OBSERVATION: >
  A newly created product, with the expiry-blocking setting never touched, allows an expired
  component to be consumed without any block or warning.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Create a new product with the expiry-blocking configuration left at its default, and attempt to
  consume an expired component into it.
```

## G06-MRP_PRODUCT_EXPIRY-Q045

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q045
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Overriding a block on consuming an expired component requires an elevated level of
  authorisation, distinct from the standing permission that lets an operator run ordinary
  production.
WHY_IT_MATTERS: >
  If any operator can override the block unaided, the block is a formality rather than a genuine
  control, and the decision to consume expired stock is never actually escalated.
DISCONFIRMING_OBSERVATION: >
  An operator holding only standard production-execution rights is able to override a block on
  consuming an expired component with no additional authorisation step.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a standard production operator, attempt to override a block on consuming an expired
  component and observe whether an elevated authorisation step is required.
```

## G06-MRP_PRODUCT_EXPIRY-Q046

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q046
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Archiving or deprovisioning a product after it has produced dated output lots leaves those
  lots' already-assigned dates and traceability intact and retrievable, rather than severing
  access to that history.
WHY_IT_MATTERS: >
  A recall or audit does not stop needing an old product's production history just because the
  product itself is no longer active.
DISCONFIRMING_OBSERVATION: >
  Archiving a product makes a previously produced lot's date or its traceability record
  inaccessible or unrecoverable.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce a dated output lot for a product, archive or deprovision the product, and check whether
  the lot's date and traceability remain retrievable.
```

## G06-MRP_PRODUCT_EXPIRY-Q047

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q047
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A component whose date falls on the exact same calendar date as its consumption is treated by
  one clearly defined rule (either already expired, still valid, or an explicit boundary case)
  consistently every time, rather than the outcome depending on incidental factors like time of
  day.
WHY_IT_MATTERS: >
  An ambiguous same-day boundary means the exact same situation can be blocked on one occasion
  and allowed on another with no way to predict which.
DISCONFIRMING_OBSERVATION: >
  Consuming a component on its exact expiry date produces a block in one trial and no block in
  an otherwise identical trial.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Consume a component exactly on its stated date across more than one trial under otherwise
  identical conditions, and compare the outcome.
```

## G06-MRP_PRODUCT_EXPIRY-Q048

```yaml
QID: G06-MRP_PRODUCT_EXPIRY-Q048
MODULE: mrp_product_expiry
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a component lot is recalled or written off after being partly consumed by a now-completed
  order and partly still reserved by a still-open order, the write-off event correctly
  distinguishes the already-consumed portion from the still-reserved portion, rather than
  applying uniformly to the whole original lot quantity regardless of what has already happened
  to it.
WHY_IT_MATTERS: >
  Treating both portions the same either double-counts a loss already absorbed by the completed
  order, or fails to flag the reserved portion still sitting in an order that has not yet
  consumed it.
DISCONFIRMING_OBSERVATION: >
  A write-off of a partially consumed, partially reserved lot posts a single loss figure that
  does not distinguish the consumed portion (already inside a completed output) from the
  still-reserved, unconsumed portion.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Split a single component lot between a completed order (consumed) and a still-open order
  (reserved but unconsumed), then trigger a write-off or recall on that lot and inspect how the
  event treats each portion.
```
