# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_project Module Bridge MVQ Bank

**Document ID:** GMVQ-G08-SALE_PROJECT-MVQ48-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_project`
**Wave:** W2
**Author Cell:** P-S7 (GMVQ Question Factory — Production Team P-S7)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `sale_project`, the first and lowest-arity link
in the G08 order-project-stock-ledger chain (`sale_project` -> `sale_project_stock` ->
`sale_project_stock_account`), and a two-participant bridge in its own right against
`sale_purchase_project`. Per the GMVQ Bridge Module Rule V1.00, every question here fails only at
the seam between a commercial order and the project record it creates or feeds: creation timing and
idempotency, ownership and authority split between sales and delivery, budget and scope derivation
and drift, lifecycle coupling and decoupling on cancellation/closure/hold, multi-company and
permission boundaries, and billing-trigger reconciliation between the two documents. No question
here concerns a physical goods movement or a ledger posting — those seams belong to
`sale_project_stock` and `sale_project_stock_account` respectively — and no question restates a pure
order behaviour (`sale`) or a pure delivery-management behaviour (`project`) in isolation; each was
tested against the bridge removal test (would this question still make sense with the order and the
project used entirely apart?) before being kept.

## Control

**Arity owned: TWO-PARTICIPANT (order + project) only.** Every question below requires both an
order and a project to exist in relation to each other; none requires goods movement or ledger
posting to be material, and none is answerable, or even meaningful, from the order alone or the
project alone.

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a concrete failure
  state, never a restatement of its own hypothesis.
- No padding: these 48 questions test 48 distinct material seam hypotheses; none was trimmed or
  stretched to hit the count.
- Question text is source-neutral: no vendor or product name, no technical identifier (table,
  field, method, XML ID, API path), and the module's own metadata name never appears outside the
  `MODULE:` field.
- No question concerns a physical stock movement or an accounting/ledger entry; those seams are
  reserved to `sale_project_stock` and `sale_project_stock_account`.
- Every question passed the bridge removal test before being kept.
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
  Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G08-SALE_PROJECT-Q001

```yaml
QID: G08-SALE_PROJECT-Q001
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Confirming an order creates exactly one linked project even if the confirming action is triggered twice in quick succession.
WHY_IT_MATTERS: >
  Two projects for one confirmed order would split scope, budget and reporting for a single sold commitment.
DISCONFIRMING_OBSERVATION: >
  Confirming the same order twice in rapid succession results in two separate linked projects instead of one.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Prepare a quotation, trigger its confirmation action twice in close succession, and check how many projects are linked afterward.
```

## G08-SALE_PROJECT-Q002

```yaml
QID: G08-SALE_PROJECT-Q002
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  Whether a project is created at order confirmation or only once the first fulfilment activity begins is a single fixed rule, not one that varies unexplained between similar orders.
WHY_IT_MATTERS: >
  Inconsistent creation timing would make it unpredictable when project-based planning can actually begin.
DISCONFIRMING_OBSERVATION: >
  Two otherwise-identical confirmed orders have their linked project created at different lifecycle points with no configuration difference explaining it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Confirm two similarly configured orders and record the exact lifecycle point at which each one's project first appears.
```

## G08-SALE_PROJECT-Q003

```yaml
QID: G08-SALE_PROJECT-Q003
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Cancelling an order after its linked project has already begun receiving work does not silently delete or hide the project.
WHY_IT_MATTERS: >
  Silently losing a project record would erase the record of work already committed and performed.
DISCONFIRMING_OBSERVATION: >
  Cancelling the order removes the project from view or deletes it, even though work had already been logged against it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order, log work against its linked project, cancel the order, and check whether the project and its logged work remain visible.
```

## G08-SALE_PROJECT-Q004

```yaml
QID: G08-SALE_PROJECT-Q004
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  An order with several lines each configured to spawn its own project either creates all of them or clearly reports which ones failed, never silently fewer with no indication.
WHY_IT_MATTERS: >
  A partial, unreported creation would leave part of a sold scope with no tracked project and no one aware of it.
DISCONFIRMING_OBSERVATION: >
  Confirming a multi-line order that should create several projects results in fewer projects than expected, with no indication that any failed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Configure several lines on one order each set to create a separate project, confirm the order, and count the resulting projects against the expected number.
```

## G08-SALE_PROJECT-Q005

```yaml
QID: G08-SALE_PROJECT-Q005
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When several separate orders feed one shared project, cancelling one of those orders does not corrupt or remove the contribution already made by another, still-active order.
WHY_IT_MATTERS: >
  One customer's cancelled order should not damage the tracked scope or budget contributed by a different, still-live order to a shared project.
DISCONFIRMING_OBSERVATION: >
  Cancelling one of several orders feeding a shared project also removes or corrupts the contribution of another, uncancelled order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Link two separate orders to one project, cancel one, and check whether the other order's contribution to the project is still intact.
```

## G08-SALE_PROJECT-Q006

```yaml
QID: G08-SALE_PROJECT-Q006
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A project's budget, once derived from an order's value at project creation, follows one documented rule for whether it later updates with the order's value or stays fixed, applied consistently rather than drifting between the two for similar orders.
WHY_IT_MATTERS: >
  An unpredictable mix of updating and frozen budgets would make project financial tracking unreliable for planning.
DISCONFIRMING_OBSERVATION: >
  Two similarly configured projects respond differently when their source orders' value is changed by the same amount after creation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create two projects from two similarly priced orders, change each order's value by the same amount afterward, and compare whether both project budgets respond the same way.
```

## G08-SALE_PROJECT-Q007

```yaml
QID: G08-SALE_PROJECT-Q007
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Scope changes recorded only on the project do not automatically alter the linked order's committed lines or value without a separate, visible action on the order itself.
WHY_IT_MATTERS: >
  Silent scope creep flowing from the project into the commercial document would let costed work escape the customer's actual agreed order.
DISCONFIRMING_OBSERVATION: >
  Adding a new task or scope item directly on the project changes the linked order's committed lines or total value with no separate action taken on the order.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Add a new task directly on a project linked to a confirmed order, and check whether the order's lines or value changed as a result.
```

## G08-SALE_PROJECT-Q008

```yaml
QID: G08-SALE_PROJECT-Q008
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Ownership of the order and ownership of the project can legitimately be two different people, and the system does not silently force one to match the other.
WHY_IT_MATTERS: >
  Sales and delivery are commonly different roles; forcing them to match would misrepresent who is actually accountable for each side.
DISCONFIRMING_OBSERVATION: >
  Setting a project's manager to someone other than the order's owner is blocked, reverted, or silently overwritten back to match the order's owner.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Confirm an order, assign the linked project's manager to a different person than the order's owner, and check whether that assignment holds.
```

## G08-SALE_PROJECT-Q009

```yaml
QID: G08-SALE_PROJECT-Q009
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project can be closed while its linked order still has unfulfilled lines, and doing so does not silently mark the order itself as fulfilled or closed.
WHY_IT_MATTERS: >
  Treating an unrelated project closure as proof the customer's order was fulfilled would misstate what was actually delivered.
DISCONFIRMING_OBSERVATION: >
  Closing a project whose linked order still has undelivered lines causes the order's own fulfilment status to change to fulfilled or closed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order with more than one line, deliver only some, close the linked project, and check the order's fulfilment status afterward.
```

## G08-SALE_PROJECT-Q010

```yaml
QID: G08-SALE_PROJECT-Q010
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  An order being marked fully fulfilled does not automatically close or complete a linked project that still has open tasks.
WHY_IT_MATTERS: >
  A project can legitimately still be finishing internal work after commercial delivery; auto-closing it would hide unfinished work.
DISCONFIRMING_OBSERVATION: >
  Marking the order's lines as fully delivered automatically closes or completes the linked project despite open, unfinished tasks.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order, leave open tasks on its linked project, mark all order lines as delivered, and check the project's status afterward.
```

## G08-SALE_PROJECT-Q011

```yaml
QID: G08-SALE_PROJECT-Q011
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Applying a project template's default tasks at creation, then later changing the order's line quantity, does not retroactively rewrite the already-applied tasks without a visible, separate step.
WHY_IT_MATTERS: >
  Silent retroactive rewriting would make it impossible to trust that a project's task list reflects what was actually planned and possibly already started.
DISCONFIRMING_OBSERVATION: >
  Increasing the order's line quantity after project creation silently changes or regenerates the template-derived tasks already established on the project.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a project from an order using a template with default tasks, then increase the order's line quantity, and check whether the existing tasks changed.
```

## G08-SALE_PROJECT-Q012

```yaml
QID: G08-SALE_PROJECT-Q012
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Billing milestones defined on the project and the invoicing policy defined on the order are reconciled to one documented rule for which one actually triggers an invoice, rather than each triggering independently and inconsistently.
WHY_IT_MATTERS: >
  Two independent, un-reconciled triggers could invoice the customer twice for the same milestone, or never invoice it at all.
DISCONFIRMING_OBSERVATION: >
  Reaching a project milestone and separately reaching the order's own invoicing trigger both generate an invoice for the same scope of work.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a project milestone and an order invoicing policy that could both apply to the same scope, reach both conditions, and check how many invoices result.
```

## G08-SALE_PROJECT-Q013

```yaml
QID: G08-SALE_PROJECT-Q013
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Duplicating a confirmed order does not cause the copy to inherit a live, active reference to the original order's already-created project.
WHY_IT_MATTERS: >
  A duplicate quotation pointing at someone else's already-underway project would misattribute new commercial activity to existing delivery work.
DISCONFIRMING_OBSERVATION: >
  Duplicating a confirmed order produces a copy that still references the original order's project as its own.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order so a project is created, duplicate the order, and check whether the duplicate shows a link to the original project.
```

## G08-SALE_PROJECT-Q014

```yaml
QID: G08-SALE_PROJECT-Q014
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Locking an order after invoicing does not also lock or prevent legitimate ongoing edits to its linked project's tasks and schedule.
WHY_IT_MATTERS: >
  Locking the commercial document should not stop the delivery team from continuing to manage the work that document paid for.
DISCONFIRMING_OBSERVATION: >
  Locking the order after invoicing also blocks editing of tasks or schedule on its linked project.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Confirm and invoice an order to the point it becomes locked, then attempt to edit a task on its linked project.
```

## G08-SALE_PROJECT-Q015

```yaml
QID: G08-SALE_PROJECT-Q015
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Deleting a project that still has a live linked order does not leave the order pointing at a broken or missing reference with no indication to a viewer.
WHY_IT_MATTERS: >
  A silently broken reference would make an order look like it has no delivery vehicle at all, with no trace of what happened.
DISCONFIRMING_OBSERVATION: >
  Deleting a project linked to a live order leaves the order referencing a project that no longer exists, with no visible notice.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Where permitted, delete a project linked to a confirmed order, and inspect the order for any broken reference or lack of notice.
```

## G08-SALE_PROJECT-Q016

```yaml
QID: G08-SALE_PROJECT-Q016
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  When an order's company and a project's company differ in a multi-company setup, the system either blocks that combination or clearly designates which company is authoritative for the linked record.
WHY_IT_MATTERS: >
  An ambiguous cross-company link could let one company's financial and delivery data become mixed with another's without proper separation.
DISCONFIRMING_OBSERVATION: >
  An order in one company links to a project recorded under a different company with no indication of which company's records govern it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  In a multi-company setup, confirm an order under one company configured to link to a project under a different company, and observe how the assignment is handled.
```

## G08-SALE_PROJECT-Q017

```yaml
QID: G08-SALE_PROJECT-Q017
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Changing the customer on a confirmed order after its project already exists either updates the project's customer reference to match or is blocked, rather than leaving the two silently disagreeing.
WHY_IT_MATTERS: >
  An order and its project disagreeing about the customer would misdirect communication, invoicing, and delivery to the wrong party.
DISCONFIRMING_OBSERVATION: >
  Changing the order's customer after project creation leaves the project still showing the previous customer, with no update or block.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order and create its project, then change the order's customer, and check whether the project's customer reference changed too.
```

## G08-SALE_PROJECT-Q018

```yaml
QID: G08-SALE_PROJECT-Q018
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A project template's own default billing type and the linked order's invoicing policy are reconciled to one governing rule rather than both silently attempting to control invoicing independently.
WHY_IT_MATTERS: >
  Two competing billing rules could generate conflicting or duplicate invoices for the same delivered work.
DISCONFIRMING_OBSERVATION: >
  Applying a project template with one billing type to an order carrying a conflicting invoicing policy results in both rules independently generating invoices.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply a project template with a distinct billing type to an order whose own invoicing policy conflicts with it, and observe which rule actually governs invoicing.
```

## G08-SALE_PROJECT-Q019

```yaml
QID: G08-SALE_PROJECT-Q019
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Issuing a credit note against an order after its linked project has already been marked complete does not silently reopen the completed project.
WHY_IT_MATTERS: >
  A commercial adjustment after the fact should not automatically undo a project team's own record that the work was finished.
DISCONFIRMING_OBSERVATION: >
  Issuing a credit note against the order changes the already-completed project's status back to open or in-progress.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Complete a project linked to an order, issue a credit note against that order, and check whether the project's status changed.
```

## G08-SALE_PROJECT-Q020

```yaml
QID: G08-SALE_PROJECT-Q020
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Where one order's several lines each create their own project, later merging two of those lines does not silently merge, orphan, or duplicate the two already-created projects without a documented rule.
WHY_IT_MATTERS: >
  An undocumented merge outcome could leave one project's already-logged work stranded or duplicated under the surviving project.
DISCONFIRMING_OBSERVATION: >
  Merging two order lines that each had their own linked project results in one project being silently orphaned, duplicated, or having its history lost.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two order lines each generating their own project, merge the lines, and observe what happens to the two previously separate projects.
```

## G08-SALE_PROJECT-Q021

```yaml
QID: G08-SALE_PROJECT-Q021
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  A project's stage being set to on-hold does not, by itself, block or restrict further changes to the linked order.
WHY_IT_MATTERS: >
  The delivery team pausing internal work should not stop the sales side from managing the underlying commercial agreement.
DISCONFIRMING_OBSERVATION: >
  Putting the linked project on hold blocks a normally permitted edit to the order.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set a project to a paused or on-hold stage, then attempt a normally permitted edit to its linked order.
```

## G08-SALE_PROJECT-Q022

```yaml
QID: G08-SALE_PROJECT-Q022
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  The order's expected delivery date and the project's own planned end date, once they disagree, do not silently overwrite one another with no way to see they diverged.
WHY_IT_MATTERS: >
  Silently collapsing two independently meaningful dates into one would hide a real scheduling conflict from whoever needs to resolve it.
DISCONFIRMING_OBSERVATION: >
  Changing the project's planned end date silently overwrites the order's expected delivery date, or vice versa, with no record of the prior value.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set differing dates on an order and its linked project, change one of them, and check whether the other silently changed to match.
```

## G08-SALE_PROJECT-Q023

```yaml
QID: G08-SALE_PROJECT-Q023
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A draft project created early, during quotation before confirmation, is not left as an orphaned, still-active record when that quotation is lost or cancelled rather than confirmed.
WHY_IT_MATTERS: >
  An orphaned active project from a deal that never closed would misrepresent actual won business and consume tracking attention for nothing.
DISCONFIRMING_OBSERVATION: >
  Cancelling or losing a quotation that had already spawned a draft project leaves that project active and unflagged as belonging to unconfirmed business.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Configure early project creation at quotation stage, cancel the quotation instead of confirming it, and check the resulting project's status.
```

## G08-SALE_PROJECT-Q024

```yaml
QID: G08-SALE_PROJECT-Q024
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A discount or price change applied to a confirmed order after its project exists does not silently and immediately rewrite the project's already-derived budget figure without any visible trail of the change.
WHY_IT_MATTERS: >
  An untraceable retroactive budget change would make it impossible to explain why a project's budget moved after the fact.
DISCONFIRMING_OBSERVATION: >
  Applying a price change to the confirmed order changes the linked project's budget figure with no visible record of when or why.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a project from an order, apply a price change to the confirmed order, and check whether the project's budget changed and whether that change is traceable.
```
## G08-SALE_PROJECT-Q025

```yaml
QID: G08-SALE_PROJECT-Q025
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Reassigning an order to a different salesperson does not automatically reassign the linked project's manager; the two remain independently assignable roles.
WHY_IT_MATTERS: >
  Sales handoff and delivery ownership are different concerns; coupling them would misassign accountability for the work.
DISCONFIRMING_OBSERVATION: >
  Reassigning the order's salesperson also silently changes who is recorded as the linked project's manager.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reassign the salesperson on a confirmed order with an existing linked project, and check whether the project's manager field changed.
```

## G08-SALE_PROJECT-Q026

```yaml
QID: G08-SALE_PROJECT-Q026
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A concurrent edit to the order's quantity and to its linked project's status at nearly the same time does not result in one change being silently discarded.
WHY_IT_MATTERS: >
  A lost concurrent edit on either side could leave the commercial record and the delivery record disagreeing without anyone noticing.
DISCONFIRMING_OBSERVATION: >
  A concurrent edit to the order and to its linked project results in one of the two changes being silently discarded.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Simulate near-simultaneous edits to an order's quantity and its linked project's status, and check whether both changes are retained.
```

## G08-SALE_PROJECT-Q027

```yaml
QID: G08-SALE_PROJECT-Q027
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  A project being on hold does not, by itself, block or delay scheduled invoicing on its linked order when the order's own invoicing policy is time-based rather than tied to project progress.
WHY_IT_MATTERS: >
  A billing schedule the customer agreed to should not silently stall because of an internal delivery pause, unless that dependency is intended and documented.
DISCONFIRMING_OBSERVATION: >
  Putting the project on hold delays or blocks a time-based invoice on the order that was not actually tied to project progress.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure an order with time-based invoicing independent of project milestones, put the linked project on hold, and check whether the scheduled invoice still occurs.
```

## G08-SALE_PROJECT-Q028

```yaml
QID: G08-SALE_PROJECT-Q028
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Cancelling an order does not, by itself, silently cancel or close its linked project without a separate, visible action recording the cause.
WHY_IT_MATTERS: >
  Ambiguity about whether cancelling the sale also ends the delivery work risks either continuing unpaid work or losing a record of work that should continue.
DISCONFIRMING_OBSERVATION: >
  Cancelling the order changes the linked project's status with no visible record of that action having been the cause.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel a confirmed order with an active linked project, and check the project's resulting status and whether the cause is recorded.
```

## G08-SALE_PROJECT-Q029

```yaml
QID: G08-SALE_PROJECT-Q029
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Someone who can view a project's budget or margin, but has no permission to view the underlying order's financial figures, cannot see order-derived cost or price information through the project.
WHY_IT_MATTERS: >
  A permission boundary that exists on the commercial document must not have a back door through the project view.
DISCONFIRMING_OBSERVATION: >
  A user without rights to view the order's financial figures can see order-derived cost or price data by viewing the linked project instead.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Grant a user project-viewing rights but not order financial-viewing rights, and check whether order-derived financial figures are visible to them through the project.
```

## G08-SALE_PROJECT-Q030

```yaml
QID: G08-SALE_PROJECT-Q030
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Renaming or re-numbering an order after its project exists updates the project's reference display, rather than leaving the project pointing at a stale label.
WHY_IT_MATTERS: >
  A stale reference would make it harder for a delivery team to find or confirm which commercial document actually funds their project.
DISCONFIRMING_OBSERVATION: >
  Renaming or re-numbering the order leaves the project still displaying the order's previous identifier with no update.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Rename or re-number a confirmed order that already has a linked project, and check whether the project's displayed reference updates.
```

## G08-SALE_PROJECT-Q031

```yaml
QID: G08-SALE_PROJECT-Q031
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A project's completion percentage being edited downward after it already triggered a milestone invoice does not silently generate a corrective invoice or credit without an explicit, separate action.
WHY_IT_MATTERS: >
  An automatic silent reversal of billing tied to a progress correction could surprise the customer or misstate revenue without anyone deciding it should happen.
DISCONFIRMING_OBSERVATION: >
  Lowering the project's completion percentage after a milestone invoice was issued automatically triggers a corrective invoice or credit with no separate action taken.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Reach a milestone that triggers an invoice, then edit the project's completion percentage downward, and check whether any billing document is generated automatically.
```

## G08-SALE_PROJECT-Q032

```yaml
QID: G08-SALE_PROJECT-Q032
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Two separate orders configured to each create a project of the same name for the same customer do not get silently merged into one project record.
WHY_IT_MATTERS: >
  Merging two distinct sales into one tracked project would understate what has actually been sold and make it impossible to bill each correctly.
DISCONFIRMING_OBSERVATION: >
  Confirming two separate orders that would each create a similarly named project for the same customer results in only one project representing both.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm two separate orders for the same customer configured to create similarly named projects, and check whether one or two projects result.
```

## G08-SALE_PROJECT-Q033

```yaml
QID: G08-SALE_PROJECT-Q033
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Deleting an order outright, where deletion is permitted as distinct from cancellation, does not leave its already-created project with no explanation that its originating order is gone.
WHY_IT_MATTERS: >
  A project with an unexplained missing origin would be impossible to audit or justify later.
DISCONFIRMING_OBSERVATION: >
  Deleting the order leaves its linked project with no visible indication that the originating order no longer exists.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Where order deletion is permitted, delete a confirmed order with a linked project, and inspect the project for any indication of the missing origin.
```

## G08-SALE_PROJECT-Q034

```yaml
QID: G08-SALE_PROJECT-Q034
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A project manager who has no access to view the underlying order still sees a clearly bounded reference that a paying order exists, rather than either full order detail or a completely invisible link.
WHY_IT_MATTERS: >
  Complete invisibility would make the project team unaware their work is commercially funded at all; full detail would breach the order's own access boundary.
DISCONFIRMING_OBSERVATION: >
  A project manager without order-viewing rights sees either the order's full commercial detail or no indication that a linked order exists at all.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Restrict a project manager's access to the underlying order, and check what level of reference to that order they can see from the project.
```

## G08-SALE_PROJECT-Q035

```yaml
QID: G08-SALE_PROJECT-Q035
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When the order's delivery date is pushed out after the project's schedule was derived from the original date, the project's schedule either recomputes or is flagged as stale, never silently unchanged with no flag.
WHY_IT_MATTERS: >
  An unflagged stale schedule would let a team keep planning against a date the customer commitment no longer reflects.
DISCONFIRMING_OBSERVATION: >
  Changing the order's delivery date leaves the project's schedule unchanged with no flag that it may now be based on outdated information.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Change a confirmed order's delivery date after its project's schedule was set from the original date, and check whether the project's schedule reflects or flags the change.
```

## G08-SALE_PROJECT-Q036

```yaml
QID: G08-SALE_PROJECT-Q036
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Retrieving a project's budget when the order's currency differs from the project's own reporting currency uses one documented rate and moment consistently, not different ones depending on which screen or report is used.
WHY_IT_MATTERS: >
  Inconsistent currency conversion between views of the same figure would make budget reporting numerically unreliable.
DISCONFIRMING_OBSERVATION: >
  Two different views of the same project's budget, converted from the order's currency, show different converted figures for the same underlying amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a project from an order priced in a different currency than the project's reporting currency, and compare the converted budget figure shown in two different places.
```

## G08-SALE_PROJECT-Q037

```yaml
QID: G08-SALE_PROJECT-Q037
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Applying a project template whose milestones are percentages of the order's value, then adding a new line to the order, either extends the milestones to cover the new line's value or documents that it does not.
WHY_IT_MATTERS: >
  Value added to the order that no milestone ever covers would mean that portion of the sale is never billed through the project's own billing mechanism.
DISCONFIRMING_OBSERVATION: >
  Adding a new line to the order after template milestones were set leaves that line's value with no milestone ever covering it, and nothing flags the gap.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Apply a percentage-of-value milestone template, add a new line to the order afterward, and check whether the milestones account for the new line's value.
```

## G08-SALE_PROJECT-Q038

```yaml
QID: G08-SALE_PROJECT-Q038
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Where the order's invoicing policy already bills a line as fully invoiced ahead of the project's own view of that scope as delivered, the project's own reporting does not silently claim the work is done because it was billed.
WHY_IT_MATTERS: >
  Conflating "billed" with "actually completed" would give a false picture of real delivery progress to anyone relying on the project view.
DISCONFIRMING_OBSERVATION: >
  The project's own status or reporting shows a scope of work as complete solely because the order already invoiced it, without independent confirmation of the work itself.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Configure an order that invoices ahead of delivery, confirm it, and check whether the project's own reported progress reflects the invoice rather than actual work state.
```

## G08-SALE_PROJECT-Q039

```yaml
QID: G08-SALE_PROJECT-Q039
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Several projects each drawing scope from separate phases of one master order operate on clearly separated portions of that order's lines, such that one project finishing does not mark a different phase's still-unstarted lines as complete too.
WHY_IT_MATTERS: >
  Cross-attributing completion between unrelated phases would falsely report progress on work that has not actually started.
DISCONFIRMING_OBSERVATION: >
  Completing one phase's project marks a different phase's still-unstarted order lines as complete as well.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Split one order's scope across two separate projects for two phases, complete one project, and check the status of the other phase's order lines.
```

## G08-SALE_PROJECT-Q040

```yaml
QID: G08-SALE_PROJECT-Q040
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  The order's assigned sales team and the project's own assigned team can legitimately differ, and reporting rollups attribute the commercial figure to one and the delivery figure to the other rather than conflating them.
WHY_IT_MATTERS: >
  Misattributing delivery work to the sales team, or vice versa, would distort performance reporting for both teams.
DISCONFIRMING_OBSERVATION: >
  A reporting rollup attributes the project's delivery activity to the order's sales team, or the order's sale to the project's delivery team, rather than each to its own.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Assign different teams to an order and its linked project, and check how each team's reporting rollup attributes the activity.
```

## G08-SALE_PROJECT-Q041

```yaml
QID: G08-SALE_PROJECT-Q041
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  A quotation template that pre-attaches a draft project before the customer has even accepted the quotation does not leave that draft project as a persistent, unresolved record if the customer rejects the quotation instead.
WHY_IT_MATTERS: >
  An unresolved draft project from rejected business would clutter tracking with work that was never actually committed to.
DISCONFIRMING_OBSERVATION: >
  Rejecting the quotation leaves its pre-attached draft project active and unflagged as belonging to business that did not close.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Use a quotation template that pre-creates a draft project, reject the quotation rather than confirming it, and check the resulting project's status.
```

## G08-SALE_PROJECT-Q042

```yaml
QID: G08-SALE_PROJECT-Q042
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A negative line added to an order after its linked project has been marked complete and archived either reopens the project in a documented way or is recorded separately, never vanishing into a budget correction with no visible link.
WHY_IT_MATTERS: >
  An untraceable post-archive correction would make it impossible to reconcile why a closed project's numbers later changed.
DISCONFIRMING_OBSERVATION: >
  Adding a return or correction line to the order after project archival changes a figure associated with the project with no visible trace connecting the two.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete and archive a project, add a return or correction line to its linked order afterward, and check whether any project-associated figure changes and whether it is traceable.
```

## G08-SALE_PROJECT-Q043

```yaml
QID: G08-SALE_PROJECT-Q043
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A project's payment terms, when initially inherited from the linked order, follow one documented rule for whether they stay frozen or follow later renegotiation, applied consistently across similar projects.
WHY_IT_MATTERS: >
  An undocumented choice between frozen and live-following payment terms would make it unclear which terms actually govern billing at any given time.
DISCONFIRMING_OBSERVATION: >
  Renegotiating the order's payment terms produces an unpredictable result on the project's own recorded terms, differing between otherwise similar cases.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a project inheriting payment terms from an order, renegotiate the order's terms afterward, and check whether the project's terms respond consistently.
```

## G08-SALE_PROJECT-Q044

```yaml
QID: G08-SALE_PROJECT-Q044
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A recurring arrangement that repeatedly feeds one persistent project accumulates the project's tracked budget correctly across renewals rather than resetting or double-adding at each renewal event.
WHY_IT_MATTERS: >
  A budget that resets or double-counts on every renewal would make the project's financial tracking meaningless over its lifetime.
DISCONFIRMING_OBSERVATION: >
  A renewal event feeding the same persistent project resets its accumulated budget to zero, or adds the renewal's value twice.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Set up a recurring arrangement feeding one persistent project, trigger two renewal events, and check whether the project's accumulated budget correctly reflects both.
```

## G08-SALE_PROJECT-Q045

```yaml
QID: G08-SALE_PROJECT-Q045
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  An order confirmed through an automated approval path with no human review still creates its linked project through the same documented rule as a manually confirmed order.
WHY_IT_MATTERS: >
  A hidden second code path for automated confirmations could create projects inconsistently or skip checks that manual confirmation applies.
DISCONFIRMING_OBSERVATION: >
  An order confirmed automatically creates its linked project differently, extra, missing, or different, than an equivalent order confirmed manually.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Confirm one order manually and an equivalent order through an automated approval path, and compare how each one's project is created.
```

## G08-SALE_PROJECT-Q046

```yaml
QID: G08-SALE_PROJECT-Q046
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When an order's fulfilment splits into more than one resulting document, the project's single link correctly reflects that the scope now spans more than one fulfilment document, rather than appearing fully resolved by only the first one.
WHY_IT_MATTERS: >
  Treating a partial split as if it were the whole scope would understate what the project still needs to track as outstanding.
DISCONFIRMING_OBSERVATION: >
  After an order's fulfilment splits into more than one document, the linked project shows the scope as fully resolved despite part of it remaining outstanding.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Cause a confirmed order's fulfilment to split into more than one resulting document, and check whether the linked project's tracked scope reflects the remainder as still outstanding.
```

## G08-SALE_PROJECT-Q047

```yaml
QID: G08-SALE_PROJECT-Q047
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A customer viewing their own order through a self-service portal does not see internal project scheduling or task-level detail that was never meant for external visibility.
WHY_IT_MATTERS: >
  Internal delivery planning detail reaching the customer directly could expose sensitive scheduling, staffing, or cost information never intended for them.
DISCONFIRMING_OBSERVATION: >
  A customer viewing their order online can see internal project task or scheduling detail beyond what was explicitly meant to be customer-facing.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  View a confirmed order's project-linked detail through the customer-facing self-service view, and check whether internal project detail is exposed.
```

## G08-SALE_PROJECT-Q048

```yaml
QID: G08-SALE_PROJECT-Q048
MODULE: sale_project
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Two orders independently confirmed at nearly the same moment, each configured to feed into the same not-yet-created shared project, do not race into creating two separate "shared" projects instead of the intended one.
WHY_IT_MATTERS: >
  A creation race under concurrent confirmation would defeat the intended shared tracking and split what should be one project's history into two.
DISCONFIRMING_OBSERVATION: >
  Confirming two orders configured to feed the same not-yet-existing shared project at nearly the same time results in two separate projects being created instead of one.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure two orders to feed one shared, not-yet-created project, confirm them at nearly the same time, and check whether one or two projects result.
```
