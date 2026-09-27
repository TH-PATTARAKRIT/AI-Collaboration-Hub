# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / project_purchase_stock Module MVQ Bank

**Document ID:** GMVQ-G12-PROJECT_PURCHASE_STOCK-MVQ48-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `project_purchase_stock`
**Wave:** W3
**Author Cell:** P12-4 (GMVQ Question Factory — Production Cell P12-4)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

Per the Group Brief, `project_purchase_stock` is treated as a 2-way bridge: project on one side,
and the already-integrated procure-to-receive capability (purchasing fulfilled through a physical
stock receipt) on the other, treated as a single unit rather than three independent domains. Every
question below fails the seam test with a NO — each depends on the receiving/procurement process
actually being tied to a project's task, site, or schedule.

This bank is deliberately silent on any customer-facing sale, delivery, or order. Where the goods
flow toward a *customer* via a project-linked order, that seam belongs to `sale_project_stock`
(G08) and is out of scope here — this bank covers material procured to supply a project's own
internal or cost-center need, received through the ordinary purchase-to-stock process.

Question text is source-neutral: no vendor or product name, no technical identifier, and no
reference to the module's own metadata name.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material hypothesis.
- Pre-authoring check performed: `grep -h HYPOTHESIS` across `G07_PURCHASE_STOCK` (the pure
  purchase+stock base bank, no project) and `G08_SALE_PROJECT_STOCK` (sale+project+stock, framed
  around delivery to a *customer*) confirmed neither uses a project-as-material-consumer framing
  with no customer order in the loop. No overlap found; this bank stays anchored on project-only
  consumption of procured, received material.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PROJECT_PURCHASE_STOCK-Q001

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q001
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A purchase order raised specifically to supply a project task records the project link at the
  point of order, not only inferred after the goods are received.
WHY_IT_MATTERS: >
  A link inferred only from a later receipt cannot be relied on if two tasks could plausibly have
  ordered the same item, leaving attribution ambiguous until goods physically arrive.
DISCONFIRMING_OBSERVATION: >
  The purchase order's project-task reference exists only once a receipt is recorded against it, not
  at the point the order itself was raised.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Raise a purchase order explicitly against a project task and inspect its record before any receipt
  occurs.
```

## G12-PROJECT_PURCHASE_STOCK-Q002

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q002
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Receiving the ordered quantity against a project-linked purchase order updates the project's own
  material-readiness view through the same recorded event as it updates the order's own
  received-quantity, not through two independently derived updates.
WHY_IT_MATTERS: >
  Two independently derived updates can drift apart, leaving the project believing material has
  arrived when the purchase-side record disagrees, or the reverse.
DISCONFIRMING_OBSERVATION: >
  The purchase order shows the quantity as received while the project's own readiness view for that
  task still shows the material as outstanding, or the reverse.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Receive the full ordered quantity against a project-linked purchase order and compare the order's
  own received status with the project task's material-readiness indicator.
```

## G12-PROJECT_PURCHASE_STOCK-Q003

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q003
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A partial receipt against a project-linked purchase order leaves the project's outstanding-material
  expectation reduced only by the quantity actually received, not by the full ordered quantity.
WHY_IT_MATTERS: >
  Clearing the full outstanding expectation on a partial receipt masks a genuine shortfall that could
  block the dependent task.
DISCONFIRMING_OBSERVATION: >
  After receiving less than the full ordered quantity, the project's outstanding-material indicator
  for that task shows nothing still outstanding.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive a partial quantity against a project-linked purchase order and check the project task's
  remaining outstanding-material figure.
```

## G12-PROJECT_PURCHASE_STOCK-Q004

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q004
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Goods received against a project-linked purchase order but not yet issued to any task remain
  visibly distinct, in the project's own tracking, from goods actually consumed by the project.
WHY_IT_MATTERS: >
  Conflating received-but-unused with consumed overstates the project's true progress and can
  trigger a premature completion claim.
DISCONFIRMING_OBSERVATION: >
  Goods received but never issued to a task appear in the project's own tracking as already
  consumed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive goods against a project-linked order without issuing them to any task, and check the
  project's own consumption view.
```

## G12-PROJECT_PURCHASE_STOCK-Q005

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q005
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A receiving location specified as the project's own site, rather than a general warehouse, is
  honored consistently by both the purchase order's delivered-status and the project's
  material-readiness view.
WHY_IT_MATTERS: >
  Inconsistent honoring of the site as the destination can make the project believe material is on
  site when it is actually sitting in a general warehouse, or vice versa.
DISCONFIRMING_OBSERVATION: >
  A receipt recorded at the project's own site is shown by the purchase order as delivered but by the
  project's own readiness view as still awaiting arrival, or the reverse.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set a project site as the receiving location on a purchase order, record the receipt there, and
  compare the order's and the project's own status.
```

## G12-PROJECT_PURCHASE_STOCK-Q006

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q006
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a single purchase order's receipt is meant to supply two different tasks within the same
  project, the split of the received quantity between the two tasks is a documented, visible
  allocation rather than an implicit assumption.
WHY_IT_MATTERS: >
  An implicit split can silently assign all received material to whichever task happens to be
  checked first, leaving the other task believing it still has nothing.
DISCONFIRMING_OBSERVATION: >
  A receipt meant to supply two tasks shows the full received quantity credited to only one of them,
  with no visible allocation record for the split.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure one purchase order to supply two project tasks, receive the goods, and check how the
  received quantity is allocated between the two tasks.
```

## G12-PROJECT_PURCHASE_STOCK-Q007

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q007
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A quality or inspection hold placed on goods destined for a project task blocks the project's own
  indication that the material is ready for use, not only the purchase order's own received-status.
WHY_IT_MATTERS: >
  A project team unaware of a quality hold may proceed to use material that has not actually cleared
  inspection, creating a safety or rework risk.
DISCONFIRMING_OBSERVATION: >
  Goods under an active quality hold are shown by the project's own material-readiness view as ready
  for use.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Place a quality hold on goods received against a project-linked purchase order, and check the
  project task's readiness indicator.
```

## G12-PROJECT_PURCHASE_STOCK-Q008

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q008
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a project task after its funding purchase order's goods have already been received
  results in those goods being flagged for review or reallocation rather than remaining an
  unexplained, orphaned receipt.
WHY_IT_MATTERS: >
  An unflagged, orphaned receipt is money already spent on physical goods that no longer serve any
  documented purpose.
DISCONFIRMING_OBSERVATION: >
  A project task is cancelled after its funding purchase order's goods are already received, and no
  flag or review prompt appears against the now-unused goods.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a project task after goods against its funding purchase order have already been received,
  and check whether the receipt is flagged.
```

## G12-PROJECT_PURCHASE_STOCK-Q009

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q009
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A return of previously received, project-destined goods back to the vendor carries a traceable
  link back to both the original receipt and the project task it was meant to supply.
WHY_IT_MATTERS: >
  Losing the link to the originating task makes it impossible to later understand why that task's
  material never actually arrived.
DISCONFIRMING_OBSERVATION: >
  A return-to-vendor of project-destined goods exists with no traceable link back to either the
  original receipt or the project task it was meant to supply.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Return previously received, project-linked goods to the vendor and trace the return back to the
  original receipt and task.
```

## G12-PROJECT_PURCHASE_STOCK-Q010

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q010
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Putting a project on hold after a linked purchase order's goods have already been received does
  not silently release those goods back to general, unrestricted stock without an explicit action.
WHY_IT_MATTERS: >
  A silent release lets already-purchased, project-earmarked material be consumed by an unrelated
  need while the project itself is merely paused, not cancelled.
DISCONFIRMING_OBSERVATION: >
  Placing the project on hold changes the earmarked status of already-received goods to freely
  available with no explicit release action taken.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Put a project on hold after goods against a linked purchase order are already received, and check
  whether those goods remain earmarked.
```

## G12-PROJECT_PURCHASE_STOCK-Q011

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q011
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A backorder on the unreceived remainder of a project-linked purchase order is visible on the
  project's own schedule or readiness indicator, not only on the purchase order itself.
WHY_IT_MATTERS: >
  Confining a backorder signal to the purchase order leaves the project team unaware a dependent
  task's material is now delayed.
DISCONFIRMING_OBSERVATION: >
  A backorder exists on a project-linked purchase order's remaining quantity and the project's own
  schedule shows no corresponding risk indicator.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Generate a backorder on the unreceived remainder of a project-linked purchase order and check the
  project's own schedule view.
```

## G12-PROJECT_PURCHASE_STOCK-Q012

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q012
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the purchase order's promised delivery date and the project task's own need date disagree,
  which one governs the schedule-risk indicator shown to the project is one documented, consistent
  rule.
WHY_IT_MATTERS: >
  An inconsistent choice of governing date means the schedule-risk signal cannot be trusted from one
  task to the next.
DISCONFIRMING_OBSERVATION: >
  Two comparable project tasks, each with a disagreement between the order's promised date and the
  task's need date, show risk indicators governed by different dates with no documented reason.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set up two project tasks each with a purchase order whose promised date disagrees with the task's
  need date, and compare which date governs the shown risk indicator in each case.
```

## G12-PROJECT_PURCHASE_STOCK-Q013

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q013
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Goods received under a company entity different from the one holding the project, in a
  multi-company setup, become visible to the project's material tracking only once the required
  inter-company step has completed.
WHY_IT_MATTERS: >
  Visibility before the inter-company step completes lets a project rely on material whose ownership
  has not actually transferred between the two entities.
DISCONFIRMING_OBSERVATION: >
  Goods received under a different company entity than the project's own appear in the project's
  material tracking before any inter-company step has occurred.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Receive goods under one company entity against a purchase order feeding a project owned by a
  different entity, and check when the project's tracking reflects them.
```

## G12-PROJECT_PURCHASE_STOCK-Q014

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q014
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A lot- or serial-tracked item received against a project-linked purchase order retains that
  tracked identity through to the point the project logs its consumption, rather than the identity
  being dropped once the purchase-side receipt validates.
WHY_IT_MATTERS: >
  Losing tracked identity at the project's own point of use defeats traceability exactly where a
  defect or recall investigation would need it most.
DISCONFIRMING_OBSERVATION: >
  A lot- or serial-tracked item's identity is present on the receipt but absent once the project logs
  its own consumption of the item.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive a lot- or serial-tracked item against a project-linked order, log its consumption on the
  project task, and check whether the tracked identity carried through.
```

## G12-PROJECT_PURCHASE_STOCK-Q015

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q015
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two receiving events processed concurrently against the same project-linked purchase order do not
  result in the project's own received-quantity view double-counting one of them.
WHY_IT_MATTERS: >
  Double-counting a concurrent receipt overstates how much material the project actually has on
  hand, risking a false all-clear to proceed with a task.
DISCONFIRMING_OBSERVATION: >
  After two concurrent receiving events against the same order, the project's received-quantity
  figure exceeds the sum of the two actual receipts.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Process two receiving events at nearly the same time against one project-linked purchase order,
  and check the project's resulting received-quantity total.
```

## G12-PROJECT_PURCHASE_STOCK-Q016

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q016
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A discrepancy identified during receiving (short, over, or damaged) against a project-linked order
  is traceable back to the specific project task the goods were meant to supply, not left as a note
  disconnected from the project.
WHY_IT_MATTERS: >
  A discrepancy disconnected from its task leaves the project team unaware their own material need
  has been affected.
DISCONFIRMING_OBSERVATION: >
  A short, over, or damaged receipt against a project-linked order is recorded with no traceable link
  to the specific task it was meant to supply.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a short, over, or damaged receipt against a project-linked purchase order, and trace the
  discrepancy record back to the specific task.
```

## G12-PROJECT_PURCHASE_STOCK-Q017

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q017
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Closing a project while its funding purchase order still has an unreceived, outstanding balance
  either blocks closure or leaves that balance explicitly flagged against the closed project.
WHY_IT_MATTERS: >
  A closed project with a silently unresolved receiving balance leaves outstanding vendor goods with
  no active owner tracking their eventual arrival.
DISCONFIRMING_OBSERVATION: >
  A project closes with an outstanding, unreceived balance on its funding purchase order and no flag
  appears on the closed project.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to close a project with an unreceived, outstanding balance on its funding purchase order,
  and observe the outcome.
```

## G12-PROJECT_PURCHASE_STOCK-Q018

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q018
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reversing an already-validated receipt against a project-linked purchase order, after the project
  has already logged consumption from it, produces a visible variance on the project's own
  consumption record rather than a silently stale figure.
WHY_IT_MATTERS: >
  A silently stale consumption figure leaves the project reporting material as used that has since
  been reversed out of stock, misstating actual progress and cost.
DISCONFIRMING_OBSERVATION: >
  A receipt is reversed after the project already logged consumption drawn from it, and the
  project's consumption record shows no resulting variance.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Log project consumption from a validated receipt, then reverse that receipt, and check the
  project's own consumption record for a variance.
```

## G12-PROJECT_PURCHASE_STOCK-Q019

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q019
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A substitute item received in place of the one actually ordered, due to a vendor stock-out, is
  flagged on the project's material-readiness view as a substitution rather than silently treated as
  satisfying the original need.
WHY_IT_MATTERS: >
  An unflagged substitution can leave a project task proceeding with a different item than what its
  own plan or specification actually required.
DISCONFIRMING_OBSERVATION: >
  A substitute item received against a project-linked order is shown on the project's readiness view
  as if the originally ordered item had arrived, with no substitution flag.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Receive a substitute item in place of the originally ordered one against a project-linked purchase
  order, and check the project's readiness view for a flag.
```

## G12-PROJECT_PURCHASE_STOCK-Q020

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q020
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where goods for a project are ordered from a vendor and drop-shipped directly to the project's
  site bypassing the company's own warehouse, that receipt is still subject to the same three-way
  match evaluation as an ordinarily warehoused receipt.
WHY_IT_MATTERS: >
  Exempting a drop-shipped receipt from the match creates a route where quantity and price agreement
  is never actually verified before the vendor is paid.
DISCONFIRMING_OBSERVATION: >
  A drop-shipped receipt directly to a project site is matched against the vendor's invoice with a
  materially different level of scrutiny than a warehoused receipt for a comparable order.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Arrange a drop-shipped receipt direct to a project site for one order and a warehoused receipt for
  a comparable order, and compare the resulting three-way match evaluation.
```

## G12-PROJECT_PURCHASE_STOCK-Q021

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q021
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A duplicated project, created to plan a similar future engagement, does not inherit a live
  reference to goods already received and consumed under the original project's purchase order.
WHY_IT_MATTERS: >
  A live reference in the duplicate would make a brand-new, unstarted project appear to already have
  material on hand or already consumed.
DISCONFIRMING_OBSERVATION: >
  The duplicated project shows the original project's already-received or already-consumed goods as
  its own current material state.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Duplicate a project that already has received and consumed material against a purchase order, and
  inspect the duplicate's own material state.
```

## G12-PROJECT_PURCHASE_STOCK-Q022

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q022
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Excess quantity received beyond what a project-linked purchase order actually specified is either
  blocked or requires an explicit action to accept, and is never silently counted as satisfying a
  different, unrelated task's need.
WHY_IT_MATTERS: >
  Silently applying an unplanned excess to an unrelated task misattributes cost and material that
  neither task actually ordered.
DISCONFIRMING_OBSERVATION: >
  A quantity received beyond the ordered amount is automatically applied to a different project task's
  need with no explicit action taken.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive a quantity beyond what a project-linked purchase order specified, and observe how the
  excess is treated relative to other project tasks.
```

## G12-PROJECT_PURCHASE_STOCK-Q023

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q023
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When the purchasing unit on a project-linked order has no valid configured conversion to the
  stock-keeping unit used at receiving, the receipt is blocked or explicitly flagged rather than
  assumed at a default rate that could misstate what the project actually received.
WHY_IT_MATTERS: >
  An assumed default conversion rate can silently misstate how much material the project actually has
  on hand relative to what it thinks it ordered.
DISCONFIRMING_OBSERVATION: >
  A receipt proceeds using an assumed one-to-one unit conversion with no configured conversion
  actually defined, and no flag alerts anyone to the assumption.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to receive against a project-linked order whose purchasing unit has no configured
  conversion to the stock-keeping unit, and observe the outcome.
```

## G12-PROJECT_PURCHASE_STOCK-Q024

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q024
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A vendor's delivery covering lines for more than one project under the same purchase order
  attributes each project's own received quantity separately, rather than merging into one
  undifferentiated total.
WHY_IT_MATTERS: >
  Merging quantities across projects makes it impossible to know how much of a combined delivery
  actually belongs to each project's own need.
DISCONFIRMING_OBSERVATION: >
  A single delivery covering two different projects' lines results in one combined received figure
  with no per-project breakdown.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive one vendor delivery covering purchase order lines for two different projects, and check
  whether the received quantity is attributed separately to each.
```

## G12-PROJECT_PURCHASE_STOCK-Q025

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q025
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening a closed project to record a late-arriving receipt against an old purchase order is a
  recorded action — who reopened it and when — rather than an unaudited change.
WHY_IT_MATTERS: >
  An unaudited reopening of a closed project undermines closure as a control checkpoint and hides
  who decided to revisit it.
DISCONFIRMING_OBSERVATION: >
  A closed project is reopened to record a late receipt and no audit entry shows who reopened it or
  when.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Reopen a closed project to record a late-arriving receipt against an old purchase order, and check
  the audit trail.
```

## G12-PROJECT_PURCHASE_STOCK-Q026

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q026
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A project task marked complete does not, by itself, retroactively change a linked purchase order's
  own received-quantity record if the underlying physical receipt was never actually finalized.
WHY_IT_MATTERS: >
  Letting a task's completion state fabricate a receipt record would let a purchase order appear
  fulfilled when the actual physical goods were never confirmed received.
DISCONFIRMING_OBSERVATION: >
  Marking the project task complete changes the linked purchase order's received-quantity figure
  with no corresponding physical receipt having been finalized.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Mark a project task complete while its funding purchase order still has an unfinalized receipt,
  and check whether the order's received figure changes.
```

## G12-PROJECT_PURCHASE_STOCK-Q027

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q027
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Emergency reallocation of goods already received and earmarked for one project's task, to cover an
  unrelated urgent need elsewhere, results in a visible change to that project's own
  material-readiness indicator.
WHY_IT_MATTERS: >
  A reallocation with no visible change to the losing project's readiness leaves that project falsely
  believing it still has material it no longer actually holds.
DISCONFIRMING_OBSERVATION: >
  Goods earmarked for a project task are reallocated elsewhere and the project's own
  material-readiness indicator for that task shows no resulting change.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reallocate goods already received and earmarked for a project task to cover an unrelated urgent
  need, and check the project's readiness indicator afterward.
```

## G12-PROJECT_PURCHASE_STOCK-Q028

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q028
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a project spans multiple physical destination locations, each fed by its own receipt against
  the same purchase order, the project's overall material-readiness reflects the combination of all
  site-level partial receipts.
WHY_IT_MATTERS: >
  Showing only one site's receipt while ignoring others understates the project's true overall
  material position.
DISCONFIRMING_OBSERVATION: >
  A project fed by receipts at more than one site shows an overall readiness figure reflecting only
  one site's receipt, ignoring the others.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive goods for one project at more than one destination site against the same purchase order,
  and check the project's overall readiness figure.
```

## G12-PROJECT_PURCHASE_STOCK-Q029

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q029
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A physical destination location tied to a project that is archived or deactivated after the
  purchase order is confirmed, but before goods are received, does not cause the receipt to be
  silently redirected to an unrelated active location with no visible resolution.
WHY_IT_MATTERS: >
  A silent redirection can send project-destined material to a location no one associated with the
  project is watching.
DISCONFIRMING_OBSERVATION: >
  Goods are received and silently redirected to a different, active location after the original
  project destination was archived, with no flag or resolution step shown.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive a project's destination location after a purchase order confirms but before goods arrive,
  then process the receipt and observe where it lands.
```

## G12-PROJECT_PURCHASE_STOCK-Q030

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q030
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Damaged goods identified at a project site after receipt but before being logged as consumed are
  attributed to a single documented cause path that determines how a replacement purchase is raised.
WHY_IT_MATTERS: >
  Without a documented cause path, replacement purchases proceed inconsistently and the reason for
  the original loss is lost.
DISCONFIRMING_OBSERVATION: >
  Goods damaged at a project site before being logged as consumed are recorded with no documented
  cause, and a replacement purchase is raised through no consistent, traceable path.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record goods damaged at a project site after receipt but before consumption, and trace what path
  is used to raise a replacement purchase.
```

## G12-PROJECT_PURCHASE_STOCK-Q031

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q031
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Confirming receipt of goods for a project task while another user simultaneously puts that same
  project on hold resolves to one consistent, recorded outcome rather than an unrecorded race.
WHY_IT_MATTERS: >
  An unrecorded race between a receipt and a hold action leaves the system in a state neither user
  actually intended, with no way to reconstruct what happened.
DISCONFIRMING_OBSERVATION: >
  Simultaneously confirming a receipt and placing the same project on hold produces an outcome that
  neither action alone would predict, with no record of how the conflict was resolved.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Simulate confirming a receipt for a project task at the same moment another user places that
  project on hold, and observe the resulting state and any recorded resolution.
```

## G12-PROJECT_PURCHASE_STOCK-Q032

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q032
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a project's task depends on goods sourced through more than one purchase order due to a
  partial vendor shortage, the task's overall readiness reflects the combination correctly rather
  than showing ready once only the first order's goods arrive.
WHY_IT_MATTERS: >
  Showing ready prematurely lets a task proceed before all its actual material need has arrived.
DISCONFIRMING_OBSERVATION: >
  A task fed by two purchase orders shows as materially ready once only the first order's goods
  arrive, while the second order's goods remain outstanding.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Split a task's material need across two purchase orders due to a shortage, receive only the first,
  and check the task's readiness indicator.
```

## G12-PROJECT_PURCHASE_STOCK-Q033

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q033
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A correction to an already-validated receipt quantity against a project-linked order requires a
  distinct corrective action, with the original validated quantity remaining visible rather than
  overwritten in place.
WHY_IT_MATTERS: >
  Overwriting a validated quantity in place destroys the ability to later reconstruct what was
  originally recorded before the correction.
DISCONFIRMING_OBSERVATION: >
  Correcting a previously validated receipt quantity overwrites the original figure with no trace of
  what it was before the correction.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Correct an already-validated receipt quantity on a project-linked order and check whether the
  original figure remains visible in history.
```

## G12-PROJECT_PURCHASE_STOCK-Q034

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q034
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Stock already received and earmarked for one project's task is visible to a later, different task
  in the same project as already committed, rather than appearing freely available.
WHY_IT_MATTERS: >
  Appearing freely available invites a later task to consume material a different task within the
  same project has already claimed, creating an internal shortfall.
DISCONFIRMING_OBSERVATION: >
  Material earmarked for one task within a project appears as freely available stock when a
  different task in the same project checks material availability.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Earmark received material for one project task, then check its availability status from a
  different task within the same project.
```

## G12-PROJECT_PURCHASE_STOCK-Q035

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q035
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A vendor packing or delivery reference captured at receipt for a project-linked order is retained
  on the pairing between the receipt and the project task for later reconciliation, rather than
  discarded once the receipt validates.
WHY_IT_MATTERS: >
  Discarding the vendor's own delivery reference removes a key piece of evidence needed to resolve a
  later dispute with the vendor over what was actually delivered.
DISCONFIRMING_OBSERVATION: >
  The vendor's packing or delivery reference captured at receipt is no longer retrievable once the
  receipt has validated.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Capture a vendor's packing or delivery reference at receipt against a project-linked order, and
  check whether it remains retrievable after validation.
```

## G12-PROJECT_PURCHASE_STOCK-Q036

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q036
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to the vendor's lead time after a project-linked purchase order is confirmed does not
  silently rewrite the project's own expected-material date without an explicit rescheduling action.
WHY_IT_MATTERS: >
  A silently rewritten expected date can leave a project team unaware their own schedule assumption
  has quietly changed underneath them.
DISCONFIRMING_OBSERVATION: >
  The vendor's lead time changes on an already-confirmed order and the project's own expected-material
  date updates with no explicit rescheduling action recorded.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a vendor's lead time on an already-confirmed, project-linked purchase order, and check the
  project's expected-material date and any related audit entry.
```

## G12-PROJECT_PURCHASE_STOCK-Q037

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q037
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a return-to-vendor of project-destined goods exceeds what was actually received under that
  project-linked order, it requires an explicit override rather than proceeding as if the excess had
  genuinely been received.
WHY_IT_MATTERS: >
  Allowing a return to exceed what was ever actually received creates a return record for goods that
  never physically existed on the project's books.
DISCONFIRMING_OBSERVATION: >
  A return-to-vendor quantity for project-destined goods exceeds the quantity ever actually received
  under that order, and proceeds with no override required.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt a return-to-vendor quantity greater than what was actually received against a
  project-linked order, and observe whether an override is required.
```

## G12-PROJECT_PURCHASE_STOCK-Q038

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q038
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A receipt generated with no reference to any project-linked purchase order does not silently
  update a project's own material-readiness view as though it were expected supply for that project.
WHY_IT_MATTERS: >
  An unrelated receipt silently updating a project's readiness would give the project team false
  confidence in material that was never actually meant for them.
DISCONFIRMING_OBSERVATION: >
  A receipt with no project reference changes a project's own material-readiness figure.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Record a receipt with no reference to any purchase order linked to a project and check whether any
  project's readiness view changes.
```

## G12-PROJECT_PURCHASE_STOCK-Q039

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q039
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The three-way match evaluation for a project-linked purchase order's vendor bill uses the receipt's
  actual validated quantity once processed, not the receipt's original expected quantity that
  predates confirmation.
WHY_IT_MATTERS: >
  Matching against the pre-confirmation expected quantity rather than what was actually validated
  can pass a bill that does not actually agree with what physically arrived.
DISCONFIRMING_OBSERVATION: >
  The three-way match for a project-linked order's bill agrees using the receipt's original expected
  quantity even after the validated quantity turned out to differ.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Validate a receipt against a project-linked order at a quantity different from its original
  expectation, then run the three-way match against the vendor's bill.
```

## G12-PROJECT_PURCHASE_STOCK-Q040

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q040
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A movement that is cancelled and replaced by a corrected one, for a project-linked order, is
  matched by the three-way match using only the corrected, currently valid movement.
WHY_IT_MATTERS: >
  Matching against a superseded, cancelled movement lets a bill be approved against a physical
  quantity that no longer represents reality.
DISCONFIRMING_OBSERVATION: >
  The three-way match for a project-linked order still references the cancelled, superseded movement
  rather than its correction.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Cancel and replace a receipt movement against a project-linked order, then run the three-way match
  and check which movement it evaluates.
```

## G12-PROJECT_PURCHASE_STOCK-Q041

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q041
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Goods received against a project-linked purchase order that has already been fully invoiced by the
  vendor are flagged rather than passing through as an ordinary additional receipt, since it changes
  what fully supplied already meant for that project task.
WHY_IT_MATTERS: >
  An unflagged additional receipt after full invoicing can mean the business paid for a quantity that
  now turns out to be less than what was actually delivered, or an unexplained surplus.
DISCONFIRMING_OBSERVATION: >
  A receipt against an already fully invoiced, project-linked order proceeds with no flag
  distinguishing it from an ordinary, expected receipt.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record an additional receipt against a project-linked order after it has already been fully
  invoiced, and check for a flag.
```

## G12-PROJECT_PURCHASE_STOCK-Q042

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q042
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a single physical delivery from one vendor covers goods for more than one project's purchase
  orders, each project's received quantity is attributed to its own order rather than merged into
  one combined figure.
WHY_IT_MATTERS: >
  A merged figure across projects makes it impossible to know how much of a shared delivery actually
  belongs to each project.
DISCONFIRMING_OBSERVATION: >
  A single delivery covering purchase orders for two different projects results in one combined
  received figure rather than a separate figure per project.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Receive one physical delivery covering purchase orders for two different projects, and check
  whether the received quantity is separately attributed to each.
```

## G12-PROJECT_PURCHASE_STOCK-Q043

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q043
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A project's material-readiness report and a separate purchasing department's own receiving report,
  both claiming to show the same project's outstanding expected goods, reconcile to a single
  documented source or their difference is explained.
WHY_IT_MATTERS: >
  Two disagreeing figures for the same outstanding expectation, with no documented reason, leaves
  neither report trustworthy for planning the project's schedule.
DISCONFIRMING_OBSERVATION: >
  The project's material-readiness report and purchasing's own receiving report show different
  outstanding-goods figures for the same project with no documented explanation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Pull a project's outstanding-goods figure from the project's own readiness report and from
  purchasing's receiving report, and compare the two.
```

## G12-PROJECT_PURCHASE_STOCK-Q044

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q044
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An unrelated administrative action elsewhere (merging purchase orders, mass edits) does not
  silently change a project-linked order's already-recorded received quantity without a distinct,
  traceable action explaining the change.
WHY_IT_MATTERS: >
  An untraceable change from an unrelated administrative action makes it impossible to later explain
  why a project's material record no longer matches what was originally recorded.
DISCONFIRMING_OBSERVATION: >
  A mass edit or order merge unrelated to a specific project changes that project's own already
  recorded received quantity with no distinct, traceable explanation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform an administrative mass edit or merge involving a project-linked purchase order, and check
  whether the project's received quantity changed and whether the change is traceable.
```

## G12-PROJECT_PURCHASE_STOCK-Q045

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q045
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where the project's task is restructured and merged into a different task after a purchase order's
  goods have already been received against the original task, the receipt's project-task reference
  updates to the surviving task.
WHY_IT_MATTERS: >
  A reference left pointing at an absorbed task makes the merged task's material position look
  incomplete and the old task's position look like an unexplained orphan.
DISCONFIRMING_OBSERVATION: >
  After two tasks are merged, a receipt originally linked to the absorbed task still references that
  absorbed task rather than the surviving one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge two project tasks where one already has a linked receipt, and check the receipt's task
  reference afterward.
```

## G12-PROJECT_PURCHASE_STOCK-Q046

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q046
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A project archived with a purchase order still showing an unresolved receiving discrepancy (short,
  over, or damaged) retains that discrepancy as visible, unresolved history rather than the
  archival implicitly closing it out.
WHY_IT_MATTERS: >
  Implicitly closing out an unresolved discrepancy through archival lets a genuine shortage or
  damage claim quietly disappear.
DISCONFIRMING_OBSERVATION: >
  A project is archived while a linked purchase order has an unresolved receiving discrepancy, and
  the discrepancy no longer appears as open, unresolved history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Archive a project that has a linked purchase order with an unresolved receiving discrepancy, and
  check whether the discrepancy remains visible.
```

## G12-PROJECT_PURCHASE_STOCK-Q047

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q047
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The date used to judge whether a project's expected material delivery is late is drawn
  consistently from the same one of either the purchase order's promised date or the receipt's own
  scheduled date, not one in the project's own view and a different one in purchasing's view.
WHY_IT_MATTERS: >
  Using two different dates in two different views means a delivery can appear late in one and on
  time in the other, with no way to know which is correct.
DISCONFIRMING_OBSERVATION: >
  The project's own view and purchasing's own view judge the same delivery's lateness using two
  different governing dates.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a case where a purchase order's promised date and a receipt's own scheduled date differ,
  and compare how lateness is judged in the project's view versus purchasing's view.
```

## G12-PROJECT_PURCHASE_STOCK-Q048

```yaml
QID: G12-PROJECT_PURCHASE_STOCK-Q048
MODULE: project_purchase_stock
TYPE: MODULE
AUTHOR: P12-4
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where goods sourced for one project are found, after receipt, to physically match a completely
  different project's outstanding need instead, reassigning them from one project to the other
  leaves a visible record of the reassignment on both projects.
WHY_IT_MATTERS: >
  An untraceable reassignment leaves one project short of material it thinks it has and the other
  project's records unable to explain where its material actually came from.
DISCONFIRMING_OBSERVATION: >
  Goods reassigned from one project to a different project's need show no visible record of the
  reassignment on either project's own history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Reassign already-received goods from their originally intended project to a different project's
  outstanding need, and check both projects' histories for the reassignment.
```
