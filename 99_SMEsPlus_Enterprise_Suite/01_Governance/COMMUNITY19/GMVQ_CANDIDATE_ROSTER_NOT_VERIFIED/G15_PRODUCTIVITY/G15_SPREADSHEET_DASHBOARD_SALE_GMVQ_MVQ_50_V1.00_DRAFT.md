# SMEsPlus ENTERPRISE SUITE
## GMVQ — G15 PRODUCTIVITY / spreadsheet_dashboard_sale Module Bridge MVQ Bank

**Document ID:** GMVQ-G15-SPREADSHEET_DASHBOARD_SALE-MVQ50-V1.00
**Group:** G15 PRODUCTIVITY (Wave W4)
**Module Metadata:** `spreadsheet_dashboard_sale`
**Wave:** W4
**Author Cell:** P15-2 (GMVQ Question Factory — Wave W4 Acceleration, Cell P15-2)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 50 = 105
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `spreadsheet_dashboard_sale` — a 2-way BRIDGE per
GMVQ_BRIDGE_MODULE_RULE_V1.00 and GROUP_BRIEF_G15_PRODUCTIVITY.md, seam: a live collaborative
dashboard drawing revenue, pipeline, and performance rollups from sales-order data it does not
itself own. The underlying order's own quotation, confirmation, and invoicing mechanics belong to
the sales base family and are deliberately NOT re-asked here. This bank asks only what becomes true
or uncertain **because a dashboard layer sits on top of** that data: staleness of cached or
scheduled revenue rollups against a live, still-changing pipeline; aggregation that exposes
individual-level rep or customer detail through small-team rollups, rankings, or drill-down;
real-time versus batch-refresh mismatch; currency, fiscal-period, and company-boundary handling
that can differ between the source and the reporting layer; and whether dashboard access itself is
mistaken for, or grants, an order action the source module gates behind its own permission model.
Every question was tested against the bridge rule: if it would read equally well with no dashboard
in the picture at all — i.e. it is really a question about quoting, confirming, or invoicing an
order on its own — it was cut. This bank is also deliberately distinct from a
sale-plus-timesheet dashboard variant (a different bridge's subject, covering time-based rollup
exposure specifically): here the concern is general order/revenue dashboard exposure and
staleness, never time-logging-specific rollup behaviour.

The question text is source-neutral and does not expose vendor or product names, field names,
methods, schema, XML IDs, API shapes, or implementation algorithms. `MODULE:
spreadsheet_dashboard_sale` appears only in the structured metadata field, never inside question
text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` stating a concrete failure state,
  never a restatement of its own hypothesis.
- No padding: 50 questions exist because they test 50 distinct material hypotheses at the seam
  between a reporting/dashboard layer and sales-order data; none was trimmed or stretched to hit
  count.
- BRIDGE MODULE per GMVQ_BRIDGE_MODULE_RULE_V1.00: every question fails only at the seam. None
  restates a quotation, confirmation, or invoicing invariant that holds with no dashboard layer
  present, and none restates the time-based rollup subject reserved for a sale-plus-timesheet
  dashboard variant.
- Mandatory pre-authoring sibling check performed: `01_QUESTION_BANKS/G15_PRODUCTIVITY/` held this
  cell's own `spreadsheet_dashboard_hr_expense`, `spreadsheet_dashboard_hr_timesheet`, and
  `spreadsheet_dashboard_im_livechat` banks on disk at authoring time (checked directly); their
  HYPOTHESIS text was reviewed and no overlap found. Per GROUP_BRIEF_G15_PRODUCTIVITY.md's
  known-duplicate-risk note, this bank deliberately excludes any time-based rollup question, which
  is reserved for the sibling `spreadsheet_dashboard_sale_timesheet` bank.
- Questions are not evidence. A later ANSWERED state requires an actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G15-SPREADSHEET_DASHBOARD_SALE-Q001

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q001
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A revenue rollup by sales representative does not expose an individual representative's figures to
  a viewer who could not see that representative's own orders directly.
WHY_IT_MATTERS: >
  Individual sales-performance detail is sensitive; a rollup is supposed to protect it behind
  aggregation, not merely relabel it.
DISCONFIRMING_OBSERVATION: >
  A viewer with no direct visibility into a representative's orders can determine that
  representative's individual revenue figure from a rollup because the group is small enough to
  isolate it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a viewer with no rep-level visibility, inspect a small-team revenue rollup and check whether an
  individual representative's figure is isolable.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q002

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q002
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A "confirmed orders" total does not include orders still in a draft or quotation stage that have
  not yet been confirmed.
WHY_IT_MATTERS: >
  Counting unconfirmed quotations as confirmed revenue overstates committed sales before a customer
  has actually agreed to the order.
DISCONFIRMING_OBSERVATION: >
  A "confirmed orders" or equivalent total changes as soon as a draft quotation is created, before it
  has been confirmed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a new quotation and leave it unconfirmed, then check whether a confirmed-orders aggregate
  moved.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q003

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q003
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Drilling from an aggregate revenue figure into the underlying order list enforces the same
  customer or company visibility restriction the source order list enforces, not a broader default
  scope introduced by the reporting layer.
WHY_IT_MATTERS: >
  A reporting layer more permissive than the record it summarizes turns an aggregate tile into a
  backdoor around the source module's own access control.
DISCONFIRMING_OBSERVATION: >
  A viewer restricted to a subset of customers or companies reaches, via drill-down, orders outside
  that restriction.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer with a restricted customer/company scope, drill down from an aggregate tile and inspect
  the full set of orders the resulting list contains.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q004

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q004
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A currency-converted revenue total combines orders using one consistent, disclosed exchange-rate
  basis rather than mixing different rate bases silently across the orders being summed.
WHY_IT_MATTERS: >
  A total built from inconsistent rate bases cannot be reconciled to any single source of truth and
  misstates revenue without any visible sign that it has done so.
DISCONFIRMING_OBSERVATION: >
  Two orders in different currencies placed on different dates are found to have been converted
  using two different, undisclosed rate bases within the same summed total.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Place multi-currency orders on different dates, allow any applicable rate change, and inspect how
  the converted total was derived.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q005

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q005
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An order cancelled after being counted in a snapshot total is removed from later renders of that
  same snapshot's total, rather than the cancelled amount remaining permanently baked into a figure
  presented as current.
WHY_IT_MATTERS: >
  A total that never sheds a cancelled amount silently overstates revenue indefinitely, and no
  reconciliation against the source will ever explain the gap.
DISCONFIRMING_OBSERVATION: >
  A period total computed after an order's cancellation still includes that order's amount when the
  dashboard is reloaded or its scheduled refresh runs again.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Let an order be counted in a period rollup, cancel it, and re-render or re-trigger the rollup for
  the same period.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q006

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q006
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard refreshed on a schedule rather than live visibly discloses the point in time its data
  reflects, so a viewer cannot mistake a batch-refreshed figure for a real-time one.
WHY_IT_MATTERS: >
  A viewer who believes a stale figure is live may make a forecasting or staffing decision on data
  that no longer matches the source.
DISCONFIRMING_OBSERVATION: >
  A dashboard built on a scheduled refresh presents its figures with no visible "as of" marker,
  timestamp, or other indication that they are not current to the moment of viewing.
EXPECTED_SURFACE: S5,S8
PRECONDITIONS: >
  Identify a dashboard widget known to refresh on a schedule and inspect whether its presentation
  discloses the data's effective timestamp.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q007

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q007
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A dashboard combining revenue across more than one company or legal entity does not silently sum
  figures that should remain company-scoped unless the viewer holds explicit cross-company
  visibility.
WHY_IT_MATTERS: >
  Summing across company boundaries without authorization exposes one entity's sales pattern to
  users of another and can misstate figures relied on for entity-level reporting.
DISCONFIRMING_OBSERVATION: >
  A viewer scoped to a single company is shown, or a total silently includes, revenue belonging to a
  different company they hold no cross-company right to see.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  In a multi-company configuration, view a revenue dashboard as a single-company-scoped user and
  check whether any total includes another company's figures.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q008

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q008
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two dashboard widgets built from the same order data but refreshed at different times can disagree,
  and each is distinguishable by its own refresh timestamp rather than implying equal currency to the
  viewer.
WHY_IT_MATTERS: >
  Two disagreeing widgets with no way to tell which is more current leave a viewer unable to decide
  which figure to trust.
DISCONFIRMING_OBSERVATION: >
  Two widgets on the same page show different totals for what should be the same underlying data,
  with no per-widget indication of each one's own refresh time.
EXPECTED_SURFACE: S5,S8
PRECONDITIONS: >
  Place two widgets covering overlapping data on refresh schedules that will drift apart, and compare
  their values and any per-widget timestamp.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q009

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q009
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rollup grouped by sales team does not expose an individual team member's contribution to a
  viewer whose permission is limited to team-level, non-attributed figures.
WHY_IT_MATTERS: >
  A team-grouped view is supposed to protect individual attribution; leaking it defeats the scoping
  the reporting layer was built to provide.
DISCONFIRMING_OBSERVATION: >
  A viewer restricted to team-level visibility can see a named individual's contribution within a
  team-grouped widget.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a team-level-scoped viewer, inspect a team-grouped revenue widget for named individual
  attribution.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q010

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q010
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an order's stage changes after the fact, a stage-based rollup reflects the new stage rather
  than the stage in force when the rollup was last computed.
WHY_IT_MATTERS: >
  A stage rollup that never absorbs a stage change silently misattributes pipeline position
  indefinitely.
DISCONFIRMING_OBSERVATION: >
  An order that has moved to a new stage continues to appear under its old stage in a rollup rendered
  after the stage change.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Advance an already-counted order to a new stage and re-render the stage-based rollup.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q011

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q011
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard widget's aggregate value does not mix pre-edit and post-edit amounts of the same order
  within a single computed number when the order is being edited concurrently with the aggregation.
WHY_IT_MATTERS: >
  A total that partially reflects two different states of the same order is internally inconsistent
  and cannot be reconciled against either state.
DISCONFIRMING_OBSERVATION: >
  A total computed while an order's amount is being edited reflects neither the pre-edit nor the
  saved post-edit amount cleanly, or differs from both on repeated identical recomputation.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a dashboard recomputation at the same time an order's amount is being saved and inspect the
  resulting total for internal consistency.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q012

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q012
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Deactivating a sales representative's user account does not remove that representative's historical
  order contribution from a period-based aggregate that included it before deactivation.
WHY_IT_MATTERS: >
  A closed period's total should not shrink retroactively just because the representative who closed
  the deal has since left.
DISCONFIRMING_OBSERVATION: >
  A closed-period revenue aggregate drops after the contributing representative's account is
  deactivated, with no corresponding change to the underlying orders.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Deactivate a representative whose orders are already reflected in a closed-period aggregate and
  re-render that aggregate.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q013

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q013
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Sharing or exporting a dashboard snapshot does not carry forward access to underlying order detail
  (such as negotiated line-level pricing) that the recipient of the snapshot is not otherwise
  authorized to see.
WHY_IT_MATTERS: >
  A snapshot meant to share summary figures becomes an unintended pricing-leak channel if it also
  hands out access to restricted order detail.
DISCONFIRMING_OBSERVATION: >
  A recipient of a shared or exported dashboard snapshot can see negotiated line-level pricing they
  could not access directly through the source module.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Share or export a dashboard snapshot to a recipient with no direct access to the source orders and
  attempt to see line-level pricing from the snapshot.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q014

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q014
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A partial return or credit against a previously counted order appears as a distinct, visible
  adjustment in any aggregate that had already counted the original order, rather than silently
  overwriting the earlier figure with no trace.
WHY_IT_MATTERS: >
  A silent overwrite makes it impossible to explain, later, why a historical total changed or to
  audit that a return actually occurred.
DISCONFIRMING_OBSERVATION: >
  A revenue total changes after a return with no separate, inspectable record of the return itself
  anywhere in the aggregate's supporting detail.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Process a partial return against a previously counted order and inspect the aggregate before and
  after for a visible adjustment trail.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q015

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q015
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A "top customer" or similar ranking view does not surface a customer's identity to a viewer whose
  permission is limited to non-attributed, aggregate-only figures.
WHY_IT_MATTERS: >
  A ranking is individual-level disclosure by definition; presenting it to a viewer who should only
  see aggregates defeats the access model at the reporting layer.
DISCONFIRMING_OBSERVATION: >
  A viewer restricted to aggregate-only visibility can see a named customer attached to a ranked
  revenue figure.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As an aggregate-only-scoped viewer, open any ranking or "top customer" style widget and check for
  named attribution.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q016

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q016
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When the underlying pricing or discount policy changes, a historical revenue aggregate already
  computed under the prior policy is not silently recomputed as though the new policy had always
  applied.
WHY_IT_MATTERS: >
  Re-baselining history under a policy that did not exist at the time misrepresents what actually
  happened during that period.
DISCONFIRMING_OBSERVATION: >
  A historical period's revenue total changes after a pricing or discount policy change, with no
  order in that period actually re-priced.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a historical revenue figure, change the pricing or discount policy, and re-render the same
  historical period's aggregate.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q017

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q017
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A real-time counter for "orders awaiting my confirmation" only counts records the current viewer is
  actually responsible for, not all pending records system-wide.
WHY_IT_MATTERS: >
  An inflated "my" counter that actually reflects everyone's queue misleads a viewer about their own
  workload and can mask records genuinely needing another person's attention.
DISCONFIRMING_OBSERVATION: >
  Two viewers with disjoint responsibilities are shown the identical "awaiting my confirmation" count,
  or a viewer's count includes records assigned to someone else.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Compare the "awaiting my confirmation" counter across two accounts known to have different assigned
  responsibilities.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q018

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q018
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A period-over-period comparison widget uses the same fiscal period-boundary definition the source
  order records use, not a differing definition introduced independently by the reporting layer.
WHY_IT_MATTERS: >
  A boundary mismatch silently shifts revenue between periods in the report that never actually moved
  in the underlying orders, breaking reconciliation.
DISCONFIRMING_OBSERVATION: >
  An order placed just inside one fiscal period boundary is attributed to the adjacent period by the
  dashboard's comparison widget.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Place an order dated at a fiscal period boundary and compare its period attribution in the source
  record versus the dashboard's period-comparison widget.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q019

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q019
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An order placed in a currency other than the reporting currency retains its original amount and
  currency alongside the converted figure in any drill-down, rather than the aggregate layer
  discarding the original values entirely.
WHY_IT_MATTERS: >
  Losing the original amount and currency makes it impossible to verify the conversion later or to
  reconcile against the customer's actual invoiced currency.
DISCONFIRMING_OBSERVATION: >
  Drilling into a converted total's underlying order shows only the converted amount, with the
  original currency and amount nowhere visible.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Place a foreign-currency order, let it appear in a converted aggregate, then drill down and check
  whether the original amount and currency remain visible.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q020

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q020
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard tile that aggregates by sales team either reflects a team reassignment made after the
  order was recorded, or clearly discloses which basis (original or current assignment) it is using,
  rather than leaving the basis unstated.
WHY_IT_MATTERS: >
  An unstated basis makes a team-level total unverifiable and can silently misattribute revenue to
  the wrong team after a reassignment.
DISCONFIRMING_OBSERVATION: >
  A team-based rollup's basis (original-at-entry versus current assignment) cannot be determined from
  the dashboard, and the two bases would produce different totals for a reassigned order.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reassign an already-counted order's owning team and compare the rollup's behaviour and any
  disclosure of which basis it used.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q021

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q021
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order's visibility is restricted (such as marked confidential to a specific negotiation),
  no aggregate exposes that order's line-level detail to a viewer who could not open the record
  directly.
WHY_IT_MATTERS: >
  A restricted order exists specifically to keep certain detail from certain viewers; an aggregate is
  not exempt from that restriction just because it summarizes rather than displays the record.
DISCONFIRMING_OBSERVATION: >
  A viewer who cannot open a restricted order can nonetheless infer or directly see its amount or
  line-level pricing from a dashboard aggregate.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Mark an order restricted/confidential, include it in a small enough group that its value is
  isolable, and check what an unauthorized viewer's aggregate reveals.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q022

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q022
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard that recalculates on a fixed schedule does not present a partially-updated aggregate,
  mid-refresh, as though it were a complete and internally consistent figure.
WHY_IT_MATTERS: >
  A partial figure presented as final can be acted on as if it were complete, when it actually
  reflects an arbitrary subset of the underlying orders.
DISCONFIRMING_OBSERVATION: >
  A dashboard viewed during a scheduled refresh shows a total that is internally inconsistent with
  its own supporting detail, with no indication a refresh is in progress.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Observe a scheduled refresh in progress (or force one) and compare the aggregate shown mid-refresh
  against its supporting detail.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q023

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q023
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A viewer scoped to a single sales team's dashboard cannot infer another team's pipeline by
  cross-referencing an organization-wide total displayed alongside their own team's figure.
WHY_IT_MATTERS: >
  Placing a restricted-scope figure next to a broader total can let simple subtraction recover data
  the viewer was never meant to see.
DISCONFIRMING_OBSERVATION: >
  A team-scoped viewer can subtract their own team's disclosed total from a displayed org-wide total
  to derive another team's figure with usable precision.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a single-team-scoped viewer, check whether the dashboard also displays an org-wide total
  alongside the team figure, and whether the remainder is derivable.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q024

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q024
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An aggregate figure computed before a bulk correction (such as a batch exchange-rate fix) is
  reconciled to reflect the correction, with the fact that a correction occurred left visible rather
  than the number simply drifting with no explanation.
WHY_IT_MATTERS: >
  An unexplained change to a previously reported figure undermines trust in every other number the
  dashboard has ever shown.
DISCONFIRMING_OBSERVATION: >
  A previously reported aggregate changes value after a bulk correction with no visible indication,
  anywhere in the dashboard, that a correction occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger or identify a bulk correction to previously aggregated order data and check for a visible
  change-disclosure alongside the updated figure.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q025

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q025
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard widget filtered against specific customers or sales representatives does not continue
  silently returning results for those references after the referenced records are deactivated or
  archived.
WHY_IT_MATTERS: >
  A filter silently keeping stale references produces results the configuration owner no longer
  intends and cannot explain by inspecting the current, active configuration.
DISCONFIRMING_OBSERVATION: >
  A widget filtered to a since-deactivated customer or representative still returns data as though
  the filter reference were active, with no warning that the reference is stale.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Build a widget filtered to a specific customer or representative, deactivate that reference, and
  re-render the widget.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q026

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q026
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling an entire order after its individual lines were already counted in an aggregate removes
  all of those lines from the aggregate, not merely the cancelled header record.
WHY_IT_MATTERS: >
  Leaving line-level amounts behind after their parent order is cancelled overstates revenue by
  exactly the amount that was supposed to have been voided.
DISCONFIRMING_OBSERVATION: >
  An aggregate still includes one or more line amounts from a fully cancelled order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cancel a multi-line order already reflected in an aggregate and re-render the aggregate.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q027

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q027
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Access to the dashboard does not itself grant the ability to confirm or modify an order; a viewer
  without order-edit authority cannot change an order's stage from within the dashboard even where
  the dashboard displays stage information.
WHY_IT_MATTERS: >
  A reporting surface that also exposes a live action control bypasses the separation between viewing
  and authorizing that the source module's permission model is built on.
DISCONFIRMING_OBSERVATION: >
  A viewer with dashboard access but no order-edit authority is able to change an order's stage from
  within the dashboard interface.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer with dashboard access but no order-edit authority, attempt to act on a stage-related
  element shown in the dashboard.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q028

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q028
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A drill-down link on an aggregate figure that no longer resolves to any record, because the
  underlying order was deleted, fails visibly rather than silently substituting a default value or a
  zero.
WHY_IT_MATTERS: >
  A silent substitution disguises a broken reference as legitimate data, hiding a data-integrity
  problem from anyone relying on the drill-down.
DISCONFIRMING_OBSERVATION: >
  Following a drill-down link to a deleted order produces a blank, zeroed, or otherwise plausible page
  instead of a visible error or not-found state.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Delete an order already referenced by a dashboard drill-down link and follow that link.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q029

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q029
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Grouping by customer on a dashboard that a non-account-owner can view aggregates revenue without
  exposing which specific customer corresponds to which value.
WHY_IT_MATTERS: >
  A customer-grouped view is individual-level by construction; giving it to a viewer without
  account-ownership rights defeats the point of scoping them to aggregates.
DISCONFIRMING_OBSERVATION: >
  A non-account-owner viewer scoped to aggregate-only visibility can see a named-customer breakdown
  in a customer-grouped widget.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a non-account-owner, aggregate-scoped viewer, attempt to access or construct a customer-grouped
  breakdown.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q030

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q030
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a large discount requires more than one approval stage, a "confirmed revenue" bucket only
  includes orders that have cleared every required approval, not merely the initial submission.
WHY_IT_MATTERS: >
  Counting a partially approved, discounted order as fully confirmed overstates confirmed, committed
  revenue.
DISCONFIRMING_OBSERVATION: >
  An order that has cleared only its first of several required discount approvals appears in a
  "confirmed revenue" total.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  In a multi-stage discount-approval configuration, advance an order through only the first stage and
  check whether it appears in a fully-confirmed revenue aggregate.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q031

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q031
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard that computes average or median deal size does not misrepresent a distribution skewed
  by one unusually large order as if it were typical, and the underlying detail remains reachable to
  a viewer entitled to see it.
WHY_IT_MATTERS: >
  A single outlier can move an average enough to mislead about "typical" deal size unless the
  dashboard surfaces the skew or lets an entitled viewer inspect it.
DISCONFIRMING_OBSERVATION: >
  An average-deal-size figure moves sharply due to one outlier order with no way for an entitled
  viewer to discover or drill into that outlier from the average widget.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Introduce one unusually large order into a group already shown as an average and check whether the
  outlier is discoverable from the average widget.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q032

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q032
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An order re-opened for correction after being marked fully invoiced is reflected in an aggregate in
  a way that is distinguishable from an order that was invoiced and never subsequently touched.
WHY_IT_MATTERS: >
  Treating a reopened-and-corrected record identically to an untouched one hides that an invoiced
  amount was changed after invoicing, which is itself a fact worth being able to see.
DISCONFIRMING_OBSERVATION: >
  A reopened-then-corrected invoiced order appears in every aggregate exactly as an untouched invoiced
  order would, with no visible indication it was reopened.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reopen and correct a previously invoiced order and compare its representation in aggregates against
  an untouched invoiced order.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q033

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q033
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A dashboard shared with a party outside the organization (such as an external partner) does not
  expose more granular data than the sharing configuration intends, even where the aggregate is built
  from orders with individually restricted access.
WHY_IT_MATTERS: >
  External sharing is the highest-consequence disclosure boundary; a leak here reaches parties with
  no organizational relationship to fall back on.
DISCONFIRMING_OBSERVATION: >
  An externally shared dashboard link exposes a filter, drill-down, or export path reaching more
  granular data than the sharing configuration specified.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Configure an external share of a dashboard at a stated granularity and attempt to reach
  finer-grained data through any interactive control the shared view still offers.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q034

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q034
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where two duplicate order records are later merged or one is voided, only one of the pair remains
  represented in any aggregate that had previously counted both.
WHY_IT_MATTERS: >
  A duplicate left counted twice after resolution silently overstates revenue by exactly the
  duplicated amount.
DISCONFIRMING_OBSERVATION: >
  An aggregate still reflects both amounts of a pair after one has been voided or the pair merged
  into one record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a duplicate pair already reflected separately in an aggregate, resolve the duplication, and
  re-render the aggregate.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q035

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q035
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A widget filtered to "this quarter" uses the fiscal-period definition configured for the
  organization, not a generic calendar quarter, when the organization's fiscal calendar differs from
  the calendar quarter.
WHY_IT_MATTERS: >
  A quarter widget built on the wrong calendar silently reports the wrong period to anyone relying on
  the organization's actual fiscal boundaries.
DISCONFIRMING_OBSERVATION: >
  In an organization with a non-calendar fiscal quarter, a "this quarter" widget's boundary dates do
  not match the configured fiscal quarter.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  In an organization configured with a non-calendar fiscal quarter, inspect a "this quarter" widget's
  actual date boundaries.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q036

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q036
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an order's owning sales representative is reassigned, a "my open orders" aggregate updates to
  remove it from the original representative's queue rather than continuing to show it to both.
WHY_IT_MATTERS: >
  Showing a reassigned order to both representatives risks duplicate follow-up or each assuming the
  other will act, leaving nobody actually responsible.
DISCONFIRMING_OBSERVATION: >
  After a representative reassignment, both the original and the new representative see the same
  order in their respective "my open orders" aggregates.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reassign an open order's owning representative and compare "my open orders" aggregates for both the
  original and new representative.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q037

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q037
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard total that blends quotations and confirmed orders together is clearly labeled as doing
  so, rather than presenting a mixed figure as a single unqualified "sales" number.
WHY_IT_MATTERS: >
  An unlabeled blend can be mistaken for confirmed revenue alone, misinforming a forecasting or
  budget decision.
DISCONFIRMING_OBSERVATION: >
  A total combining quotations and confirmed orders carries no label or distinction indicating it is
  a blend of the two.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Locate or configure a total spanning both quotations and confirmed orders and inspect its
  labeling.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q038

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q038
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Concurrent edits by two people confirming different lines of the same order at the same time do not
  produce an aggregate that reflects neither person's final state.
WHY_IT_MATTERS: >
  A lost-update outcome under concurrency can leave an order's confirmed state inconsistent with what
  either person actually decided.
DISCONFIRMING_OBSERVATION: >
  After two concurrent, non-conflicting confirmation actions on the same order, the resulting
  aggregate state matches neither person's individually intended outcome.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have two people concurrently confirm different lines of the same multi-line order and inspect the
  resulting aggregate state.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q039

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q039
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard configured to auto-refresh at a set interval degrades gracefully by clearly marking
  itself stale rather than silently continuing to display data past a failed refresh.
WHY_IT_MATTERS: >
  Silent staleness after a failed refresh is indistinguishable from a genuinely current figure,
  removing the viewer's ability to know they should not trust it.
DISCONFIRMING_OBSERVATION: >
  A dashboard whose scheduled refresh fails continues to present its last-good figures with no
  visible staleness indicator.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Cause or simulate a refresh failure on an auto-refreshing widget and inspect the presentation
  afterward.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q040

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q040
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rollup exposed at a company-wide level does not carry team-level detail fine enough to
  reconstruct near-individual deal figures when a team's headcount is very small.
WHY_IT_MATTERS: >
  Fine-grained detail at the company level defeats the purpose of aggregating in the first place if
  it still lets a viewer reconstruct one representative's figure.
DISCONFIRMING_OBSERVATION: >
  A company-wide rollup's team-level breakdown, combined with known small team headcount, allows
  recovery of an individual representative's figure.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Inspect a company-wide rollup's team-level granularity where at least one team has very few
  members.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q041

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q041
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An order's total corrected after initial entry is reflected using the corrected amount in any
  aggregate computed after the correction, not the original erroneous amount.
WHY_IT_MATTERS: >
  Continuing to report a known-wrong amount after it has been fixed at the source defeats the point
  of allowing the correction at all.
DISCONFIRMING_OBSERVATION: >
  An aggregate rendered after an amount correction still reflects the original, uncorrected amount.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Correct an already-counted order's total and re-render any aggregate that includes it.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q042

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q042
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A viewer's ability to filter the dashboard by customer does not become a way to enumerate the full
  customer list beyond what that viewer would otherwise be authorized to browse.
WHY_IT_MATTERS: >
  A filter control with an unrestricted autocomplete or picklist can leak the full customer roster to
  a viewer who has no browsing right to it.
DISCONFIRMING_OBSERVATION: >
  A viewer with no customer-directory browsing right can enumerate customer names through the
  dashboard's customer filter control.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  As a viewer without directory-browsing rights, use the dashboard's customer filter and check what
  it allows them to enumerate.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q043

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q043
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dashboard tile counting orders "without a signed confirmation" reflects the current confirmation
  state, not the state at whatever time the tile was last cached, if a confirmation is later
  received.
WHY_IT_MATTERS: >
  A stale missing-confirmation count can prompt unnecessary chasing of a customer who has already
  confirmed.
DISCONFIRMING_OBSERVATION: >
  A missing-confirmation tile continues to count an order after a confirmation has been received for
  it, past any stated refresh window.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Record a confirmation for an order already counted as missing one, then reload the tile within its
  refresh window.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q044

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q044
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard that aggregates data as of the last successful scheduled run continues to serve that
  stale data, clearly marked, if a scheduled refresh fails, rather than blanking out or throwing an
  unrecoverable error the viewer cannot interpret.
WHY_IT_MATTERS: >
  A dashboard that goes blank or errors uninformatively on a refresh failure denies the viewer any
  figure at all, when a clearly marked stale figure would still be useful.
DISCONFIRMING_OBSERVATION: >
  Following a refresh failure, the dashboard either shows no data or an uninterpretable error instead
  of the last-known-good figures with a staleness marker.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Simulate a scheduled-refresh failure and observe the dashboard's resulting presentation.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q045

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q045
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Reassigning an order from one sales team to another after it was already reflected in that team's
  historical aggregate is handled by a defined rule — either retroactive reclassification or a
  point-in-time snapshot — rather than being left ambiguous between the two.
WHY_IT_MATTERS: >
  An undefined rule means two people reading the same historical figure at different times can
  legitimately disagree about what it should show, with neither provably wrong.
DISCONFIRMING_OBSERVATION: >
  Reassigning a historical order's owning team produces a change in the historical aggregate that
  matches neither a stated retroactive rule nor a stated point-in-time snapshot rule.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Reassign the owning team of an order already reflected in a historical, closed-period aggregate and
  observe which rule (if either) the resulting change follows.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q046

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q046
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A dashboard combining current-year and prior-year revenue totals for comparison correctly isolates
  each year's figures even where the underlying period-closing process for the prior year happened
  after some current-year data already existed.
WHY_IT_MATTERS: >
  A comparison that bleeds current-year activity into the prior-year figure, or vice versa, misstates
  the year-over-year trend it exists to show.
DISCONFIRMING_OBSERVATION: >
  A year-over-year comparison widget's prior-year figure changes after current-year data is entered,
  or the current-year figure includes activity dated in the prior year.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Enter current-year orders after the prior year has closed and inspect a year-over-year comparison
  widget for cross-year bleed.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q047

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q047
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Exporting the dashboard's underlying order data to a shareable file does not bypass the same
  field-level restrictions (such as a hidden discount or cost field) that apply when viewing the same
  data within the dashboard interface.
WHY_IT_MATTERS: >
  An export path that ignores field-level masking turns a properly restricted on-screen view into an
  unrestricted file the moment it is downloaded.
DISCONFIRMING_OBSERVATION: >
  A field masked or hidden in the dashboard's on-screen view appears unmasked in an exported file of
  the same data.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Identify a field masked or hidden on-screen for the current viewer, export the underlying data, and
  inspect the exported file for that field.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q048

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q048
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A cached dashboard aggregate is invalidated and recomputed when the access-control configuration
  itself changes (such as a viewer's territory scope being reduced), rather than continuing to serve
  a total computed under the viewer's former, broader scope.
WHY_IT_MATTERS: >
  A cache that outlives a permission reduction hands a now-restricted viewer data their new, narrower
  scope should no longer include.
DISCONFIRMING_OBSERVATION: >
  A viewer whose territory or visibility scope has just been reduced still receives a cached
  aggregate reflecting their former, broader scope.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Reduce a viewer's territory/visibility scope after a cached aggregate has been computed for them,
  then reload the dashboard before any unrelated cache expiry.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q049

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q049
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A dashboard comparing actual revenue against a sales target or quota reflects a change to the quota
  configuration made after some revenue was already measured, without silently re-baselining
  already-elapsed periods.
WHY_IT_MATTERS: >
  Re-baselining an already-elapsed period against a quota that did not exist at the time misrepresents
  how the team actually tracked against its target during that period.
DISCONFIRMING_OBSERVATION: >
  A historical period's target-versus-actual comparison changes after the quota configuration is
  updated, for a period that had already elapsed under the old quota.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change a sales quota configuration after a period has elapsed and re-render that period's
  target-versus-actual comparison.
```

## G15-SPREADSHEET_DASHBOARD_SALE-Q050

```yaml
QID: G15-SPREADSHEET_DASHBOARD_SALE-Q050
MODULE: spreadsheet_dashboard_sale
TYPE: MODULE
AUTHOR: P15-2
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A unique-customer count over a period does not inflate when the same customer places a follow-up
  order, unless the dashboard is explicitly measuring order count rather than customer count.
WHY_IT_MATTERS: >
  Conflating repeat orders with new unique customers overstates actual reach and misrepresents how
  much of the volume is repeat business.
DISCONFIRMING_OBSERVATION: >
  A unique-customer count increases when a previously counted customer places a follow-up order in
  the same period, on a widget explicitly labeled as counting unique customers.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have the same customer place two separate orders within the same period and inspect a
  unique-customer aggregate for that period.
```
