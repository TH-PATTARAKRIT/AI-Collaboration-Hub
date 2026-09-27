# SALE_CRM QUESTION BANK — G08 SALES
Document ID: GMVQ-QB-G08-SALE_CRM-V1.00
Group: G08 SALES
Module Metadata: sale_crm
Wave: W2
Author Cell: P-S8
Review Cell: PENDING
Status: DRAFT / AUTHORING COMPLETE / NOT FROZEN
actual_mvq_count: 48
Purpose: Seam-only questions for the point where a pipeline opportunity becomes a commercial
order, and where the two records can disagree afterward. Passes the bridge test: every question
here fails only because both an opportunity and an order exist and interact — remove either side
and the question stops making sense.
Control: Produced under GMVQ_AUTHORING_STANDARD_V1.00 and GMVQ_BRIDGE_MODULE_RULE_V1.00. Clean
Room — no vendor or reference source tree was opened for this bank; questions are authored from
generic ERP domain knowledge only. Sibling-bank check performed per Bridge Rule §5: no other G08
bank existed on disk at authoring time (grep of HYPOTHESIS lines returned nothing). Not approved.
Not frozen. Not verified. Not MASTER-ready.

```yaml
QID: G08-SALE_CRM-Q001
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The order's actual value is compared against the opportunity's expected value at the moment
  the order is confirmed, and a material divergence is surfaced rather than silently absorbed.
WHY_IT_MATTERS: >
  If divergence is never surfaced, pipeline forecasts stay wrong even after the deal closes,
  and forecast accuracy cannot be measured against outcomes.
DISCONFIRMING_OBSERVATION: >
  An order confirms at a value far from the linked opportunity's expected value and no
  comparison, flag, or reconciling figure appears anywhere the opportunity is visible.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an opportunity with a stated expected value, convert it to an order, confirm the
  order at a materially different value, then inspect the opportunity record and any pipeline
  report that includes it.
```

```yaml
QID: G08-SALE_CRM-Q002
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A pipeline forecast report restates once the linked order's confirmed value is known, rather
  than continuing to show the opportunity's original estimate indefinitely.
WHY_IT_MATTERS: >
  A forecast that never restates against real outcomes misleads whoever relies on it for
  planning, even though the true value has been known since confirmation.
DISCONFIRMING_OBSERVATION: >
  Weeks after order confirmation, the forecast report still shows only the original
  opportunity estimate with no trace of the confirmed order value.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Convert an opportunity to a confirmed order with a different value, then re-run or refresh
  the forecast report that previously included the opportunity.
```

```yaml
QID: G08-SALE_CRM-Q003
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  There is one defined event — order confirmation, delivery, or payment — that is treated as
  the trigger for marking the linked opportunity won, and the system does not apply more than
  one trigger inconsistently across paths.
WHY_IT_MATTERS: >
  If different paths through the system close the opportunity at different events, win-rate
  and sales-cycle-length metrics become internally inconsistent and cannot be trusted for
  comparison across teams or periods.
DISCONFIRMING_OBSERVATION: >
  Two orders reaching the same lifecycle point (e.g. both confirmed, neither delivered) leave
  their linked opportunities in different states — one won, one still open.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two opportunities, convert each to an order, and drive them through confirmation,
  delivery, and payment in different sequences, checking opportunity state after each step.
```

```yaml
QID: G08-SALE_CRM-Q004
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Between an order's confirmation and whatever later event actually closes the opportunity as
  won, the opportunity sits in a defined, observable intermediate state rather than an
  undefined or contradictory one.
WHY_IT_MATTERS: >
  An undefined intermediate state is where a salesperson's dashboard and the pipeline report
  can disagree about whether a deal is still open.
DISCONFIRMING_OBSERVATION: >
  During the gap between order confirmation and opportunity closure, the opportunity appears
  simultaneously as "open" in one pipeline view and effectively decided in another.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm an order linked to an opportunity, then before delivery or payment occurs, inspect
  every view that surfaces that opportunity's state.
```

```yaml
QID: G08-SALE_CRM-Q005
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order created with no opportunity behind it is identifiable as such in pipeline and
  forecast reporting, rather than being invisible to those reports entirely.
WHY_IT_MATTERS: >
  Revenue that never passed through the pipeline is real revenue the forecast missed; if it
  cannot even be identified after the fact, forecast-versus-actual analysis is permanently
  incomplete.
DISCONFIRMING_OBSERVATION: >
  A confirmed, paid order with no opportunity link cannot be distinguished, in any report, from
  one that came through a fully tracked opportunity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create an order directly, with no opportunity conversion, confirm and pay it, then attempt to
  find it in whatever report is used to reconcile pipeline value against realised revenue.
```

```yaml
QID: G08-SALE_CRM-Q006
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An order created without an opportunity can later be attached to one retroactively, and doing
  so updates the opportunity's value and stage rather than leaving them stale.
WHY_IT_MATTERS: >
  Sales teams routinely enter orders before the CRM catches up; if retroactive linking is either
  impossible or a no-op, the pipeline record can never be corrected after the fact.
DISCONFIRMING_OBSERVATION: >
  An unlinked order is manually attached to an existing opportunity and the opportunity's value,
  stage, or expected-close data does not change at all.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create an order with no opportunity, create a separate opportunity for the same deal, then use
  whatever mechanism exists to link the two after the fact.
```

```yaml
QID: G08-SALE_CRM-Q007
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Cancelling an order after its linked opportunity has already been marked won produces a
  defined reconciling action — the opportunity reopens, is flagged, or is explicitly left won
  with a recorded reason — rather than the two records simply diverging with no trace.
WHY_IT_MATTERS: >
  A won opportunity backed by a cancelled order overstates realised sales and understates true
  pipeline loss if nothing reconciles the two.
DISCONFIRMING_OBSERVATION: >
  The order is fully cancelled, and the opportunity remains marked won with no flag, note, or
  state change anywhere linking the cancellation to the win.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Convert an opportunity to an order, confirm it, mark the opportunity won, then cancel the
  order and inspect the opportunity's state and history.
```

```yaml
QID: G08-SALE_CRM-Q008
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling only some lines of an order (not the whole order) after the linked opportunity is
  won is treated differently from a full cancellation, reflecting that the deal was partly, not
  wholly, lost.
WHY_IT_MATTERS: >
  Treating a partial cancellation the same as a full one either falsely reopens a mostly-won
  deal or hides a real partial loss inside a still-won opportunity.
DISCONFIRMING_OBSERVATION: >
  Cancelling one line of a multi-line order produces the identical opportunity-side effect as
  cancelling the entire order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm a multi-line order linked to a won opportunity, cancel a single line, and compare the
  opportunity's resulting state to what happens when the whole order is cancelled instead.
```

```yaml
QID: G08-SALE_CRM-Q009
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When one opportunity produces more than one order over time, the opportunity's won state is
  driven by a defined rule (e.g. first order, any order, or a designated order) rather than by
  whichever order happened to be touched most recently.
WHY_IT_MATTERS: >
  An undefined rule means the same sequence of events can leave different opportunities in
  different states depending on incidental ordering, breaking any audit of why a deal is closed.
DISCONFIRMING_OBSERVATION: >
  Two opportunities each produce two orders in the same sequence of events, and the two
  opportunities end up in different states.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  From a single opportunity, create and confirm two separate orders, then determine which
  order's state actually governs the opportunity's own state.
```

```yaml
QID: G08-SALE_CRM-Q010
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a single order is understood to satisfy several opportunities at once (e.g. a combined
  deal), each opportunity's link to that one order, and its resulting state, is individually
  recorded rather than only the first or last link being retained.
WHY_IT_MATTERS: >
  If only one opportunity ends up linked, the others silently vanish from pipeline reporting as
  if they never existed, understating how many deals actually closed.
DISCONFIRMING_OBSERVATION: >
  Several opportunities are each converted toward one shared order, and afterward only one of
  them shows any link to that order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt to link multiple distinct opportunities to the same single order and inspect each
  opportunity's resulting link and state afterward.
```

```yaml
QID: G08-SALE_CRM-Q011
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the salesperson recorded on the opportunity differs from the salesperson recorded on the
  resulting order, commission or performance credit is attributed according to one clearly
  governing record, not both or neither.
WHY_IT_MATTERS: >
  Ambiguous credit attribution is a direct compensation and morale risk, and double credit or no
  credit both erode trust in the reporting.
DISCONFIRMING_OBSERVATION: >
  A performance or commission report counts the same closed deal twice, once under each
  salesperson, or counts it under neither.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Convert an opportunity owned by one salesperson into an order assigned to a different
  salesperson, confirm it, and inspect every report that attributes sales credit.
```

```yaml
QID: G08-SALE_CRM-Q012
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reassigning the salesperson on an opportunity after its order is already confirmed does not
  silently reassign the salesperson already recorded on the order.
WHY_IT_MATTERS: >
  A confirmed order's salesperson reflects who actually closed and serviced that transaction; a
  later opportunity reassignment silently rewriting it would falsify the historical record.
DISCONFIRMING_OBSERVATION: >
  Changing the opportunity's salesperson after order confirmation changes the salesperson
  already recorded on the confirmed order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order linked to an opportunity, then change the opportunity's assigned salesperson
  and check whether the order's salesperson field changes as a result.
```

```yaml
QID: G08-SALE_CRM-Q013
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Reopening an opportunity after its order has already shipped is either blocked with an
  explanation or permitted with a clear note that the underlying fulfilment already occurred,
  rather than silently returning the deal to an "open" pipeline state as if nothing had shipped.
WHY_IT_MATTERS: >
  A reopened opportunity that looks like an ordinary open deal, while goods already left the
  warehouse, double-counts pipeline value that has in fact already been realised.
DISCONFIRMING_OBSERVATION: >
  An opportunity behind a fully shipped order is reopened and appears in the open pipeline with
  no indication that fulfilment already took place.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Win an opportunity, confirm and fully ship its order, then attempt to reopen the opportunity
  and inspect how it is presented afterward.
```

```yaml
QID: G08-SALE_CRM-Q014
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reopening an opportunity after its order has already been invoiced does not retract, alter, or
  contradict the existing invoice; the two records diverge in a recorded, explainable way.
WHY_IT_MATTERS: >
  An invoice is a financial and often legal document; letting a pipeline-side state change
  silently imply it should not have existed is an accounting integrity risk.
DISCONFIRMING_OBSERVATION: >
  Reopening the opportunity changes the invoice's status, amount, or existence, or the system
  gives no way to explain why an "open" opportunity has an issued invoice behind it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Win an opportunity, confirm its order, issue an invoice against it, then reopen the
  opportunity and inspect the invoice and any note explaining the discrepancy.
```

```yaml
QID: G08-SALE_CRM-Q015
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a customer record is auto-created from an opportunity's contact details and later merged
  into an existing customer record, the resulting order keeps a valid, working link to a
  customer rather than pointing at a record that no longer exists.
WHY_IT_MATTERS: >
  A broken customer link on a confirmed, possibly invoiced order corrupts the customer's order
  history and any statement or ledger built from it.
DISCONFIRMING_OBSERVATION: >
  After the merge, the order's customer field is blank, points at a deleted record, or fails to
  resolve when the order is opened.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an opportunity that auto-creates a new customer record, convert it to a confirmed
  order, merge that customer record into a pre-existing one, then reopen the order.
```

```yaml
QID: G08-SALE_CRM-Q016
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the customer records behind two separate orders are merged, both orders remain visible
  and individually intact under the surviving customer record, rather than one silently
  disappearing from that customer's history.
WHY_IT_MATTERS: >
  A customer's order history is relied on for credit decisions and service context; a silently
  dropped order understates what that customer has actually bought.
DISCONFIRMING_OBSERVATION: >
  After merging two customer records, the surviving customer's order history shows only one of
  the two orders that existed before the merge.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two confirmed orders under two different customer records that are then merged into
  one, and inspect the surviving customer's order history afterward.
```

```yaml
QID: G08-SALE_CRM-Q017
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Editing the opportunity (value, stage, or expected close date) after its order is confirmed is
  recorded in a trail, but does not silently rewrite the already-confirmed order's own figures.
WHY_IT_MATTERS: >
  A confirmed order is a commercial commitment; letting upstream pipeline edits quietly alter it
  after confirmation would undermine the meaning of "confirmed."
DISCONFIRMING_OBSERVATION: >
  Changing the opportunity's value after order confirmation changes the confirmed order's line
  values or total without any explicit action taken on the order itself.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order from an opportunity, then edit the opportunity's value or stage and inspect
  whether the order changed and whether the edit is logged anywhere.
```

```yaml
QID: G08-SALE_CRM-Q018
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Editing a confirmed order's value or lines is reflected, in some observable form, on the
  linked opportunity's forecast figure, rather than the opportunity retaining a now-stale
  estimate indefinitely.
WHY_IT_MATTERS: >
  Order-side changes are common (renegotiation, added lines); if the opportunity never reflects
  them, every downstream forecast built from the opportunity is wrong from that point on.
DISCONFIRMING_OBSERVATION: >
  A confirmed order's total is changed substantially, and the linked opportunity's value field
  and any forecast built from it remain exactly as they were before the change.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order from an opportunity, materially change the order's value after confirmation,
  and inspect the opportunity and any forecast report referencing it.
```

```yaml
QID: G08-SALE_CRM-Q019
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once an order exists against an opportunity, one single record is treated as authoritative for
  the expected close date used in scheduling and reporting, rather than the opportunity's and
  the order's own dates being used interchangeably by different reports.
WHY_IT_MATTERS: >
  Two reports quietly using two different dates for "when this deal closes" produces
  contradictory schedules that cannot be reconciled without knowing which report used which date.
DISCONFIRMING_OBSERVATION: >
  Two different standard reports show two different close dates for the same opportunity-order
  pair, with no indication of which is authoritative.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Set differing dates on the opportunity's expected close and the order's commitment date, then
  compare every report that surfaces either date for that deal.
```

```yaml
QID: G08-SALE_CRM-Q020
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the opportunity's estimate and the resulting order are in different currencies, the
  conversion used to compare or roll them up together is applied at a defined, documented point
  in time rather than an arbitrary or inconsistent one.
WHY_IT_MATTERS: >
  An undocumented conversion point makes pipeline value in a base currency non-reproducible,
  since the same deal can be worth different amounts depending on when it was last recalculated.
DISCONFIRMING_OBSERVATION: >
  The same opportunity-order pair shows two different base-currency values in two reports
  generated on the same day, with no documented reason for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an opportunity estimated in one currency, convert it to an order confirmed in another,
  and compare the base-currency value shown in at least two different reports.
```

```yaml
QID: G08-SALE_CRM-Q021
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Once an order exists for an opportunity, a probability-weighted pipeline report excludes or
  clearly separates that opportunity's weighted value so the same revenue is not counted once
  as probable pipeline and again as an actual order.
WHY_IT_MATTERS: >
  Double counting probable and actual revenue in the same rollup overstates total expected
  revenue for as long as both records are simultaneously visible to that report.
DISCONFIRMING_OBSERVATION: >
  A total revenue rollup counts both the opportunity's probability-weighted value and the
  linked order's full actual value as separate, additive contributions.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Convert an opportunity to a confirmed order without closing the opportunity as won, then
  inspect a combined pipeline-plus-actuals revenue report.
```

```yaml
QID: G08-SALE_CRM-Q022
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Marking an opportunity won without ever creating an order behind it is either prevented or
  requires an explicit, recorded reason, rather than being accepted silently as equivalent to a
  normal order-backed win.
WHY_IT_MATTERS: >
  An order-less win with no recorded justification is indistinguishable from a data-entry error
  and pollutes win-rate metrics with deals that never produced revenue.
DISCONFIRMING_OBSERVATION: >
  An opportunity is marked won with no order ever linked, and no prompt, warning, or reason
  field is available or required anywhere in that action.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Attempt to close an opportunity as won without first creating any order and observe what, if
  anything, the system requires or records.
```

```yaml
QID: G08-SALE_CRM-Q023
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The sales team recorded on the opportunity and the sales team recorded on its resulting order
  are compared, or at least both retained, so that team-level performance metrics can be
  attributed consistently even when the two differ.
WHY_IT_MATTERS: >
  Team-level quota and performance rollups silently using only one of the two team fields can
  misattribute a closed deal to the wrong team without anyone noticing.
DISCONFIRMING_OBSERVATION: >
  An opportunity owned by one sales team produces an order recorded under a different team, and
  team performance reporting shows the deal under only one of the two with no way to see both.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Assign an opportunity to one sales team, convert and confirm its order under a different
  team, and inspect team-level performance reports for both teams.
```

```yaml
QID: G08-SALE_CRM-Q024
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the order's confirmed line items differ in scope from what the opportunity described
  (products, quantities), that difference is visible on the opportunity side rather than the
  opportunity implying a scope that was never actually sold.
WHY_IT_MATTERS: >
  Product-level pipeline analysis (what is expected to sell) becomes wrong if the opportunity's
  described scope and the order's real scope silently diverge with no visible link.
DISCONFIRMING_OBSERVATION: >
  An order confirmed with an entirely different product mix than the opportunity described
  shows no discrepancy anywhere the opportunity's expected scope is displayed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an opportunity describing specific products, convert it to an order with a materially
  different product mix, confirm it, and inspect the opportunity's product-level detail.
```

```yaml
QID: G08-SALE_CRM-Q025
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A line added to an order after confirmation, which was never part of the originating
  opportunity, is still attributed to that opportunity's salesperson for credit purposes rather
  than becoming invisible to sales-credit reporting.
WHY_IT_MATTERS: >
  Post-confirmation upsell is common; if it falls outside the opportunity's credit trail
  entirely, the salesperson who closed the upsell gets no recognition for it.
DISCONFIRMING_OBSERVATION: >
  A line added after confirmation contributes to the order's realised revenue but is excluded
  from every report that attributes revenue back to the originating opportunity's salesperson.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order from an opportunity, add a new line to the order afterward, and inspect
  salesperson-credit reporting for that additional line.
```

```yaml
QID: G08-SALE_CRM-Q026
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting (not cancelling) an order that is linked to a won opportunity is either blocked or
  leaves the opportunity in a state that clearly reflects the order no longer exists, rather
  than leaving the opportunity won with a link to nothing.
WHY_IT_MATTERS: >
  A won opportunity pointing at a deleted order is a broken audit trail for a closed deal,
  which is exactly the record most likely to be checked later.
DISCONFIRMING_OBSERVATION: >
  After the order behind a won opportunity is deleted, the opportunity still shows as won with
  no indication that its supporting order is gone.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Win an opportunity backed by a confirmed order, then delete that order (where the action is
  available) and inspect the opportunity's resulting state and history.
```

```yaml
QID: G08-SALE_CRM-Q027
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting an opportunity that has a confirmed order linked to it is either blocked, or the
  order retains a valid, intact link (or an explicit record that its source opportunity was
  removed) rather than being left pointing at nothing.
WHY_IT_MATTERS: >
  A confirmed, possibly invoiced order losing its link to pipeline history erases the origin
  story of real revenue with no way to trace it back to a campaign, forecast, or salesperson.
DISCONFIRMING_OBSERVATION: >
  Deleting the opportunity behind a confirmed order is permitted, and the order afterward shows
  no trace that it ever came from a tracked opportunity.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order from an opportunity, then attempt to delete the opportunity and inspect the
  order's resulting state.
```

```yaml
QID: G08-SALE_CRM-Q028
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the opportunity and its linked order are edited by two different users at effectively the
  same time, the system resolves the conflict in a defined way (last-write, lock, or explicit
  error) rather than silently accepting both edits and leaving an inconsistent combined state.
WHY_IT_MATTERS: >
  Undefined concurrent-edit behaviour across two linked records is a data-integrity risk that
  only surfaces under real usage load, exactly when it is hardest to diagnose.
DISCONFIRMING_OBSERVATION: >
  Simultaneous edits to the opportunity and the order complete without error, and the resulting
  combined state contradicts itself (e.g. opportunity value and order total tell different,
  irreconcilable stories about the same edit).
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Arrange for two sessions to edit the linked opportunity and order at nearly the same moment
  and observe whether either save is rejected, queued, or silently merged.
```

```yaml
QID: G08-SALE_CRM-Q029
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Marking an opportunity lost after its order has already been confirmed produces a defined,
  visible contradiction marker rather than two records that simply say opposite things with
  nothing connecting them.
WHY_IT_MATTERS: >
  "Lost" and "confirmed order exists" cannot both be quietly true; whichever report is trusted
  determines whether the business believes this revenue exists at all.
DISCONFIRMING_OBSERVATION: >
  An opportunity is marked lost while its order remains confirmed, and no report, flag, or
  warning anywhere reflects that the two records disagree.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order from an opportunity, then mark that same opportunity lost, and inspect every
  place the opportunity and order states are shown.
```

```yaml
QID: G08-SALE_CRM-Q030
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When several quotations are drafted from one opportunity but only one is ever confirmed, the
  unconfirmed ones are clearly distinguishable from the confirmed one in the opportunity's own
  record, rather than all appearing as equally valid pending orders.
WHY_IT_MATTERS: >
  Unconfirmed quotations left looking like live commitments overstate what is actually pending
  for that deal and can mislead anyone reviewing the opportunity's pipeline value.
DISCONFIRMING_OBSERVATION: >
  After one of several quotations is confirmed, the opportunity's record still lists all of them
  without indicating which one is the actual, live order.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create multiple quotations from a single opportunity, confirm only one, and inspect how the
  opportunity presents the full set afterward.
```

```yaml
QID: G08-SALE_CRM-Q031
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A salesperson without permission to view a given order cannot reach that order's detail by
  navigating through an opportunity they do have permission to see.
WHY_IT_MATTERS: >
  A permission boundary that holds on one document type but not its linked counterpart is a
  data-exposure gap, not a real boundary.
DISCONFIRMING_OBSERVATION: >
  A user without order-view permission can open the full order detail by clicking through from
  an opportunity they are permitted to see.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  As a user permitted to see a given opportunity but explicitly denied access to its linked
  order, attempt to reach the order's detail through the opportunity's interface.
```

```yaml
QID: G08-SALE_CRM-Q032
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the user who closes an opportunity as won is different from the user who confirms its
  order, both actions are individually attributed in the audit trail rather than the second
  action overwriting who performed the first.
WHY_IT_MATTERS: >
  Splitting these actions across roles (e.g. a rep closes the deal, an admin confirms the order)
  is a normal workflow; losing either actor's attribution weakens accountability for both steps.
DISCONFIRMING_OBSERVATION: >
  The audit trail for the opportunity-and-order pair shows only one user for both the win and
  the confirmation, even though two different users actually performed them.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Have one user mark the opportunity won and a different user confirm the resulting order, then
  inspect the audit trail for both actions.
```

```yaml
QID: G08-SALE_CRM-Q033
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Sales-cycle-length reporting (time from opportunity creation to close) uses a single,
  consistently-defined closing date rather than switching between the opportunity's won date and
  the order's confirmation date depending on which report is run.
WHY_IT_MATTERS: >
  A metric as basic as sales-cycle length becomes uncomparable across reports if the underlying
  "closed" date is not the same event every time.
DISCONFIRMING_OBSERVATION: >
  Two different standard reports compute a different sales-cycle length for the same deal
  because one uses the opportunity's won date and the other the order's confirmation date.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a deal where the opportunity's won date and the order's confirmation date differ by a
  meaningful margin, then compare cycle-length figures across available reports.
```

```yaml
QID: G08-SALE_CRM-Q034
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once an order is linked to an opportunity, the opportunity's win probability field either
  freezes, is superseded by the order's own certainty, or is clearly marked as no longer driving
  the forecast, rather than continuing to feed a probability-weighted total for a deal that
  already has a real order.
WHY_IT_MATTERS: >
  A probability field still discounting a deal that already has a confirmed order understates
  that deal's pipeline contribution for no defensible reason.
DISCONFIRMING_OBSERVATION: >
  A confirmed order exists, yet the opportunity's probability remains below 100 percent and
  continues to discount the deal's contribution in a weighted pipeline total.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Convert an opportunity to a confirmed order while leaving its probability below 100 percent,
  then inspect a probability-weighted pipeline report.
```

```yaml
QID: G08-SALE_CRM-Q035
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A full refund or return against an order tied to a won opportunity produces a visible
  reconciling record on the opportunity side, rather than the opportunity remaining a clean,
  unqualified "won" with no trace that the sale was later reversed.
WHY_IT_MATTERS: >
  A win-rate metric that never reflects later reversals overstates true sales performance
  indefinitely, since the original win is never revisited once recorded.
DISCONFIRMING_OBSERVATION: >
  An order is fully refunded after its opportunity was marked won, and the opportunity's record
  and any win-rate report show no trace of the reversal.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Win an opportunity, confirm and invoice its order, fully refund or credit the order, then
  inspect the opportunity and any win-rate report referencing it.
```

```yaml
QID: G08-SALE_CRM-Q036
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An opportunity recorded under one company cannot produce a confirmed order under a different
  company without an explicit, permitted multi-company action, rather than the conversion
  silently crossing the company boundary.
WHY_IT_MATTERS: >
  An opportunity-to-order conversion that silently crosses company boundaries breaks
  company-level financial and pipeline reporting and can misstate which legal entity sold what.
DISCONFIRMING_OBSERVATION: >
  Converting an opportunity recorded under one company produces a confirmed order under a
  different company with no explicit action, warning, or permission check involved.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  In a multi-company setup, create an opportunity under one company and attempt to convert and
  confirm its order under a different company.
```

```yaml
QID: G08-SALE_CRM-Q037
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Converting many opportunities to orders in a single bulk action preserves an individual,
  per-opportunity audit trail rather than collapsing the batch into one undifferentiated log
  entry that cannot be traced back to any single deal.
WHY_IT_MATTERS: >
  A collapsed bulk-action log makes it impossible to answer "which specific opportunity became
  which specific order, by whom, and when" for any one deal caught up in that batch.
DISCONFIRMING_OBSERVATION: >
  After a bulk conversion, the audit trail shows only that a batch action occurred, with no way
  to trace an individual resulting order back to its specific source opportunity.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Select multiple opportunities and convert them to orders in one bulk action, then inspect the
  audit trail for traceability of each individual conversion.
```

```yaml
QID: G08-SALE_CRM-Q038
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The opportunity's source or campaign attribution is carried onto the resulting order (or
  remains reachable from it), rather than being lost the moment the order is created.
WHY_IT_MATTERS: >
  Marketing attribution and return-on-campaign analysis depend on tracing realised revenue back
  to its originating source; losing that link at conversion breaks the analysis at its root.
DISCONFIRMING_OBSERVATION: >
  An opportunity with a recorded source or campaign produces an order from which that source or
  campaign can no longer be determined by any means.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create an opportunity with a recorded source or campaign, convert and confirm its order, and
  attempt to trace the order back to that source.
```

```yaml
QID: G08-SALE_CRM-Q039
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When an order confirmed from an opportunity is later fully cancelled or credited and a new,
  separate order is created from the same opportunity, the opportunity's link reflects the
  current, live order rather than still pointing at the cancelled one.
WHY_IT_MATTERS: >
  An opportunity pointing at a dead order while a live replacement order exists elsewhere makes
  it impossible to find "the" order for that deal from the opportunity side.
DISCONFIRMING_OBSERVATION: >
  After the original order is cancelled and a replacement order is confirmed from the same
  opportunity, the opportunity's order link still resolves only to the cancelled order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm and then fully cancel an order from an opportunity, create a second order from the
  same opportunity, and check which order the opportunity links to.
```

```yaml
QID: G08-SALE_CRM-Q040
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Creating a new opportunity for a customer and product combination that already has a
  confirmed order elsewhere surfaces some indication of the existing order, rather than treating
  the new opportunity as if no prior relationship existed.
WHY_IT_MATTERS: >
  Without any surfaced context, a salesperson can unknowingly duplicate outreach on a deal that
  already closed, wasting effort and confusing the customer.
DISCONFIRMING_OBSERVATION: >
  A new opportunity is created for a customer with an existing confirmed order for the same
  product line, and nothing in the opportunity's creation or detail view reflects that history.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a confirmed order for a customer and product, then create a new opportunity for the
  same customer and product and inspect whether prior order history is surfaced.
```

```yaml
QID: G08-SALE_CRM-Q041
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Notes or logged activities added to the opportunity after its order is confirmed remain
  visible from the order side (or vice versa), rather than the two records' histories becoming
  siloed the moment the order exists.
WHY_IT_MATTERS: >
  Whoever services the order after the sale (fulfilment, support) benefits from the full
  pre-sale context; a silo forces them to hunt for information that already exists elsewhere.
DISCONFIRMING_OBSERVATION: >
  A note added to the opportunity after order confirmation is not visible or reachable from the
  confirmed order's own detail view, and vice versa.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Confirm an order from an opportunity, add a note or logged activity to the opportunity
  afterward, and check whether it is reachable from the order's view.
```

```yaml
QID: G08-SALE_CRM-Q042
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When one opportunity leads to a recurring or subscription arrangement that produces further
  orders on an ongoing basis, the opportunity's own "won" state does not depend on all future
  renewal orders continuing to be created.
WHY_IT_MATTERS: >
  If the opportunity's win state is somehow tied to ongoing renewals, a missed or paused renewal
  could retroactively call into question a deal that was genuinely won at the time.
DISCONFIRMING_OBSERVATION: >
  A renewal order in the recurring sequence is skipped or delayed, and the originating
  opportunity's own won state changes or is flagged as a result.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Win an opportunity that establishes a recurring order arrangement, then skip or delay one
  scheduled renewal and inspect the opportunity's state afterward.
```

```yaml
QID: G08-SALE_CRM-Q043
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Historical pipeline reports use the exchange rate that was actually in effect when the
  opportunity's estimate was recorded, rather than silently re-pricing past pipeline entries at
  today's rate whenever the report is re-run.
WHY_IT_MATTERS: >
  A pipeline history that changes value every time it is re-run at a new exchange rate cannot be
  used to measure forecast accuracy over time, since the numbers being compared keep moving.
DISCONFIRMING_OBSERVATION: >
  Running the same historical pipeline report twice, on different days, produces two different
  base-currency values for the same past, unchanged opportunity.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Record an opportunity's estimate in a foreign currency on one date, then run the historical
  pipeline report on two different later dates and compare the reported value.
```

```yaml
QID: G08-SALE_CRM-Q044
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Marking an opportunity lost does not automatically cancel a draft order still attached to it;
  the order is left in a state a user can deliberately act on, rather than being silently
  removed or silently left live and contradicting the "lost" status.
WHY_IT_MATTERS: >
  Silent automatic cancellation can destroy work in progress a user still intended to pursue;
  silently leaving it live contradicts the recorded loss. Either failure mode is a real cost.
DISCONFIRMING_OBSERVATION: >
  Marking the opportunity lost either deletes/cancels the attached draft order with no user
  action, or leaves it fully live and confirmable with no indication the opportunity was lost.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a draft (unconfirmed) order attached to an opportunity, mark the opportunity lost, and
  inspect the draft order's resulting state.
```

```yaml
QID: G08-SALE_CRM-Q045
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When two separate opportunity records are recognised as duplicates of the same underlying deal
  and merged, the merge retains a link to whichever order already exists, rather than the order
  link being dropped because it was only attached to the losing side of the merge.
WHY_IT_MATTERS: >
  Losing the order link during opportunity deduplication severs the connection between a real
  sale and the pipeline record that produced it, right at the moment the data is being cleaned up.
DISCONFIRMING_OBSERVATION: >
  One of two duplicate opportunities has a confirmed order linked; after merging the duplicates,
  the surviving opportunity record has no link to that order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two opportunities recognised as duplicates, link a confirmed order to one of them,
  merge the duplicates, and inspect the surviving record's order link.
```

```yaml
QID: G08-SALE_CRM-Q046
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an order's fulfilment fails entirely after its opportunity was marked won (e.g. the goods
  can never be supplied), the failure is recorded in a way that is distinguishable from an
  ordinary successful win, rather than the opportunity remaining an unqualified, indistinguishable
  "won."
WHY_IT_MATTERS: >
  A won deal that never actually delivers anything, recorded identically to one that did, hides
  real fulfilment risk from anyone reviewing win-rate or delivery-reliability metrics.
DISCONFIRMING_OBSERVATION: >
  An order behind a won opportunity fails fulfilment entirely and permanently, and the
  opportunity's record remains indistinguishable from any other successful win.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Win an opportunity, confirm its order, then drive the order to a state where fulfilment is
  permanently impossible, and inspect the opportunity's resulting record.
```

```yaml
QID: G08-SALE_CRM-Q047
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Marking an opportunity won through a manual override, without the order-side precondition that
  would normally be required (e.g. without any confirmed order), requires an elevated permission
  and leaves a distinct record of the override, rather than being available to the same users and
  indistinguishable from an ordinary win.
WHY_IT_MATTERS: >
  An unrestricted, unmarked override path for the single most consequential status in the sales
  pipeline is an integrity control gap that anyone could exploit or misuse without detection.
DISCONFIRMING_OBSERVATION: >
  Any ordinary sales user can mark an opportunity won with no order behind it, using the exact
  same action available for a normal, order-backed win, with no distinguishing record.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  As an ordinary (non-elevated) user, attempt to mark an opportunity won with no order ever
  created or confirmed, and inspect what permission is required and what is recorded.
```

```yaml
QID: G08-SALE_CRM-Q048
MODULE: sale_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the opportunity behind a confirmed order is later deleted or archived, the order retains
  enough of its own data to stand alone in reporting, rather than historical reports that joined
  through the opportunity silently losing that order from their results.
WHY_IT_MATTERS: >
  Opportunities are more likely to be cleaned up or archived than orders; if reporting depends on
  the opportunity still existing, routine housekeeping quietly erases real revenue from history.
DISCONFIRMING_OBSERVATION: >
  After the opportunity behind a confirmed, invoiced order is deleted or archived, a historical
  revenue report that previously included that order no longer includes it.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Confirm and invoice an order from an opportunity, delete or archive the opportunity, and re-run
  a historical revenue report that would have included that order.
```
