# SALE_SERVICE QUESTION BANK — G08 SALES
Document ID: GMVQ-QB-G08-SALE_SERVICE-V1.00
Group: G08 SALES
Module Metadata: sale_service
Wave: W2
Author Cell: P-S8
Review Cell: PENDING
Status: DRAFT / AUTHORING COMPLETE / NOT FROZEN
actual_mvq_count: 48
Purpose: Seam-only questions for a sales order line that carries NO PHYSICAL DELIVERY. The
absence of a stock movement is the whole subject: everything the business ordinarily uses to
know a line was fulfilled is missing, and something else must stand in for it. Passes the bridge
test: remove the base order concept or remove the service concept and these questions stop
making sense; they exist only where the two meet and a movement-shaped gap is left behind.
Control: Produced under GMVQ_AUTHORING_STANDARD_V1.00 and GMVQ_BRIDGE_MODULE_RULE_V1.00. Clean
Room — no vendor or reference source tree was opened for this bank; questions are authored from
generic ERP domain knowledge only. Mandatory pre-authoring sibling check performed per Bridge
Rule §5: `grep -h 'HYPOTHESIS' 01_QUESTION_BANKS/G08_SALES/*.md` was run and the HYPOTHESIS lines
of the closest adjacent siblings on disk at authoring time (sale_timesheet: recorded-time-to-
billing; sale_project: order-to-project creation) were read in full before authoring, to keep
this bank's ground (the delivery assertion itself, and its absence) distinct from theirs
(the rate/billing-of-time seam, and the order/project-creation seam respectively). Not approved.
Not frozen. Not verified. Not MASTER-ready.

```yaml
QID: G08-SALE_SERVICE-Q001
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A service line is only considered delivered once an explicit assertion is made by a person or
  process; it does not become "delivered" automatically at the moment it is added to, or the
  order is confirmed, with no such assertion ever being made.
WHY_IT_MATTERS: >
  If delivery happens for free at confirmation, "delivered" stops meaning the work occurred and
  every downstream rule keyed on delivery (invoicing, revenue recognition) is answering a
  question nobody actually verified.
DISCONFIRMING_OBSERVATION: >
  A service line shows as fully delivered immediately upon order confirmation, with no separate
  action, event, or user ever having asserted that the service was performed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an order containing a service line and, without taking any further action on that
  line, check whether it already reports itself as delivered.
```

```yaml
QID: G08-SALE_SERVICE-Q002
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Who is permitted to assert that a service line has been delivered is governed by a defined
  permission, distinct from general permission to edit the order, rather than any user who can
  open the order being able to assert delivery.
WHY_IT_MATTERS: >
  If asserting delivery requires no more than order-edit access, the single control point that
  stands in for a physical check can be exercised by someone with no actual knowledge that the
  work was done.
DISCONFIRMING_OBSERVATION: >
  A user who can open and edit the order, but has no assigned relationship to performing the
  service, can assert delivery on the service line with no additional permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with general order-edit access but no assigned role on the specific service line,
  attempt to mark that line delivered.
```

```yaml
QID: G08-SALE_SERVICE-Q003
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a service line's invoicing policy is keyed to delivered quantity, there exists a working
  path to actually reach a non-zero delivered quantity and therefore invoice the line, rather
  than the line being structurally unable to ever be invoiced because no movement will ever
  produce that quantity.
WHY_IT_MATTERS: >
  A line that can never be invoiced under its own configured policy is silent, permanent,
  unbilled revenue leakage that no report keyed on "awaiting delivery" will ever resolve.
DISCONFIRMING_OBSERVATION: >
  A confirmed service line configured to invoice on delivered quantity has no available action
  anywhere in the system that can move its delivered quantity above zero.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a service line's invoicing policy to bill on delivered quantity, confirm the order,
  and search for any available action that would let its delivered quantity become non-zero.
```

```yaml
QID: G08-SALE_SERVICE-Q004
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The delivered-quantity assertion for a service line can represent a genuine partial quantity
  (e.g. three of five planned units of service), not merely an all-or-nothing toggle that treats
  any assertion as complete delivery of the whole line.
WHY_IT_MATTERS: >
  A service genuinely delivered in stages (sessions, milestones, days) that can only be marked
  fully delivered or not at all either overstates completion early or blocks legitimate interim
  billing.
DISCONFIRMING_OBSERVATION: >
  Attempting to assert a delivered quantity smaller than the full ordered quantity on a service
  line either fails or is silently recorded as if the full quantity were delivered.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  On a service line ordered in a quantity greater than one, attempt to assert delivery of only
  part of that quantity and inspect the resulting delivered-quantity value.
```

```yaml
QID: G08-SALE_SERVICE-Q005
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  On an order that mixes shippable lines and a service line, the order's own overall delivery
  status is computed from every line consistently, rather than only from the lines capable of a
  physical movement while the service line is silently excluded from that computation.
WHY_IT_MATTERS: >
  If the service line is invisible to the order-level delivery computation, an order can appear
  fully delivered while a paid-for service has never actually been asserted as performed.
DISCONFIRMING_OBSERVATION: >
  An order containing an undelivered service line, but with all shippable lines shipped, reports
  its overall delivery status as fully delivered.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm and fully ship an order's physical lines while leaving its service line unasserted,
  then inspect the order's own overall delivery-status field.
```

```yaml
QID: G08-SALE_SERVICE-Q006
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a service line's delivered quantity is asserted as a fraction (e.g. two and a half of
  five units), that fractional value is preserved and used consistently in invoicing rather than
  being rounded, truncated, or rejected without a documented rule for how.
WHY_IT_MATTERS: >
  An undocumented rounding rule on a fractional service delivery either overbills or underbills
  the customer by a small, hard-to-audit amount on every partially delivered service line.
DISCONFIRMING_OBSERVATION: >
  Asserting a fractional delivered quantity on a service line produces an invoiced amount that
  does not correspond to that fraction of the line's total value, with no documented rounding
  rule accounting for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Assert a fractional delivered quantity on a service line priced per unit and inspect the
  resulting invoice line for consistency with that fraction.
```

```yaml
QID: G08-SALE_SERVICE-Q007
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling a service line after it has already been asserted delivered and invoiced produces a
  defined reconciling action (a credit, a flagged contradiction, or an explicit block) rather than
  a plain cancellation that behaves identically to cancelling a line nothing was ever done on.
WHY_IT_MATTERS: >
  A service, unlike a physical good, cannot be taken back; treating its cancellation the same as
  cancelling untouched work hides the fact that billed, performed work is being erased.
DISCONFIRMING_OBSERVATION: >
  Cancelling a service line that was already asserted delivered and invoiced completes with
  exactly the same behaviour, message, and record as cancelling a line never delivered at all.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Assert delivery and invoice a service line, then cancel it, and compare the result to
  cancelling an otherwise identical, never-delivered service line.
```

```yaml
QID: G08-SALE_SERVICE-Q008
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reversing (crediting) an invoice for an already-performed service line does not implicitly
  claim, anywhere in the record, that the underlying delivery assertion itself was also reversed
  or was false.
WHY_IT_MATTERS: >
  A financial credit and a factual retraction of "the work was done" are different statements; if
  the system conflates them, a legitimate billing correction can be misread later as evidence the
  service never happened.
DISCONFIRMING_OBSERVATION: >
  Issuing a credit note against an invoiced, delivered service line also silently clears or
  resets the line's own delivered-quantity assertion with no separate action taken on it.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Invoice an already-delivered service line, issue a credit note against that invoice, and
  inspect whether the service line's delivered-quantity assertion changed as a result.
```

```yaml
QID: G08-SALE_SERVICE-Q009
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a service line's revenue is recognised at a single point (on delivery assertion) or
  progressively over a service period is a documented, configurable rule per product or line,
  not an undocumented default that behaves differently for similar-looking services with no
  visible reason.
WHY_IT_MATTERS: >
  Inconsistent, undocumented recognition timing across similarly-configured services makes
  period-end revenue figures impossible to explain or reproduce.
DISCONFIRMING_OBSERVATION: >
  Two service lines configured identically recognise revenue on different schedules with no
  configuration difference that explains why.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure two otherwise identical service lines and compare their revenue-recognition timing
  against their configuration settings.
```

```yaml
QID: G08-SALE_SERVICE-Q010
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a service line's revenue is recognised progressively, the schedule driving that
  recognition (asserted delivery events, elapsed calendar time, or another basis) is a single,
  identifiable basis rather than several bases that can each independently produce a different
  recognised-to-date figure for the same line.
WHY_IT_MATTERS: >
  If two plausible recognition bases coexist and disagree, the recognised revenue figure for the
  same line depends on which calculation path happened to be used, which is not auditable.
DISCONFIRMING_OBSERVATION: >
  Two different standard reports show two different recognised-to-date revenue figures for the
  same progressively-recognised service line, computed from two different bases.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Set up a progressively-recognised service line partway through its period, then compare the
  recognised-to-date figure shown in at least two different reports.
```

```yaml
QID: G08-SALE_SERVICE-Q011
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A service line that spawns a downstream obligation (a task or an engagement to actually perform
  the work) reaching an invoiced or delivered state while that downstream obligation is still open
  is visible somewhere as a flagged condition, not a silent, unremarked mismatch.
WHY_IT_MATTERS: >
  Billing for work that is administratively "delivered" while the actual work behind it remains
  incomplete is exactly the gap a customer dispute or an internal audit would need to find fast.
DISCONFIRMING_OBSERVATION: >
  A service line is marked delivered and invoiced while its downstream obligation remains open,
  and nothing anywhere the line or its order is shown reflects that mismatch.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a service line that spawns a downstream obligation, assert the line delivered and
  invoice it while the obligation is still open, and inspect every view showing the line.
```

```yaml
QID: G08-SALE_SERVICE-Q012
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Completing the downstream obligation spawned by a service line does not, by itself, silently
  assert the service line as delivered; the line's own delivery assertion remains a separate,
  deliberate action.
WHY_IT_MATTERS: >
  If finishing the internal work automatically bills the customer with no separate check, a
  step someone relied on as their moment to verify the work is quietly skipped.
DISCONFIRMING_OBSERVATION: >
  Marking the downstream obligation complete changes the service line's own delivered-quantity
  assertion with no separate action taken on the line itself.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Create a service line with a downstream obligation, mark the obligation complete, and check
  whether the service line's delivery assertion changed as a result.
```

```yaml
QID: G08-SALE_SERVICE-Q013
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a customer disputes that a service was performed, a durable record exists of who
  asserted delivery, when, and on what basis, sufficient to answer the dispute without relying
  on anyone's memory.
WHY_IT_MATTERS: >
  A service leaves no physical trace of its own; the delivery assertion and its trail are the
  only evidence the business has, and if that trail is thin, every dispute becomes a
  he-said-she-said with the customer holding the leverage.
DISCONFIRMING_OBSERVATION: >
  A service line marked delivered weeks earlier cannot be traced to any specific user, timestamp,
  or stated basis for that assertion.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Assert delivery on a service line, then attempt to reconstruct, purely from the record, who
  asserted it, when, and what basis (if any) was given.
```

```yaml
QID: G08-SALE_SERVICE-Q014
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The record of who asserted a service line's delivery survives even if that user's account is
  later deactivated or removed, rather than the attribution becoming blank, generic, or
  unreadable once the account is gone.
WHY_IT_MATTERS: >
  Staff turnover is routine; evidentiary value that evaporates the moment an employee leaves
  defeats the purpose of keeping the record in the first place.
DISCONFIRMING_OBSERVATION: >
  After the asserting user's account is deactivated, the service line's delivery-assertion
  history shows no identifiable actor for that event.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Assert delivery on a service line as a given user, deactivate or remove that user's account,
  and re-check the delivery-assertion history for that line.
```

```yaml
QID: G08-SALE_SERVICE-Q015
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A service line's record explicitly distinguishes "no cost applies to this line" from "a cost
  was simply never entered," rather than the two states being visually and structurally
  identical.
WHY_IT_MATTERS: >
  A line silently missing its cost, indistinguishable from one legitimately costing nothing,
  cannot be told apart from a data-entry gap during any later review.
DISCONFIRMING_OBSERVATION: >
  A service line genuinely consuming nothing and a service line whose cost was simply never
  configured show identically as a blank or zero cost field with no distinguishing indicator.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create one service line on a product deliberately configured with no cost, and a second on a
  product where cost configuration was skipped, and compare their cost fields.
```

```yaml
QID: G08-SALE_SERVICE-Q016
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Margin and profitability analytics that roll up across many order lines include zero-cost
  service lines as genuinely zero-cost revenue, rather than silently excluding them from the
  rollup because they have no cost basis to compute against.
WHY_IT_MATTERS: >
  Silently dropping zero-cost service lines from profitability rollups understates total revenue
  covered by the analysis without any indication that a whole category of lines was left out.
DISCONFIRMING_OBSERVATION: >
  A profitability report's total revenue figure does not include the revenue from confirmed,
  invoiced service lines that carry no cost.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Invoice a zero-cost service line and compare its revenue against what a profitability rollup
  report shows as total revenue for that period.
```

```yaml
QID: G08-SALE_SERVICE-Q017
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The undelivered remainder of a partially delivered service line (quantity or price) can still
  be edited through the same mechanism available for an entirely undelivered line, rather than
  partial delivery silently locking the whole line against further changes.
WHY_IT_MATTERS: >
  Legitimate mid-engagement changes (extending or reducing remaining scope) are common for
  services; an unexplained lock the moment any partial delivery occurs blocks normal renegotiation.
DISCONFIRMING_OBSERVATION: >
  A partially delivered service line rejects an edit to its remaining, undelivered quantity that
  an otherwise identical, entirely undelivered line would accept without issue.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially deliver a service line, then attempt to edit its remaining quantity, and compare the
  result to editing an otherwise identical line with no delivery asserted at all.
```

```yaml
QID: G08-SALE_SERVICE-Q018
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  On an order carrying two service lines, one asserted delivered and one not, the order's
  invoicing action correctly separates the two rather than either invoicing both together or
  blocking both because one is not yet ready.
WHY_IT_MATTERS: >
  Blocking a ready-to-bill line because a sibling line on the same order is not yet delivered
  delays legitimate revenue for no reason tied to that line itself.
DISCONFIRMING_OBSERVATION: >
  Attempting to invoice a delivered service line on an order that also has an undelivered
  service line either invoices the undelivered line too or refuses to invoice the delivered one.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an order with two service lines, assert delivery on only one, and attempt to invoice
  the order.
```

```yaml
QID: G08-SALE_SERVICE-Q019
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A delivery assertion made by a user with no assigned relationship to the order at all (not the
  salesperson, not any assigned resource) is either blocked or is visibly distinguishable in the
  audit trail from an assertion made by someone actually connected to performing the service.
WHY_IT_MATTERS: >
  If an unrelated user's assertion looks identical to the assigned resource's, the one piece of
  evidence standing in for a physical check loses its credibility.
DISCONFIRMING_OBSERVATION: >
  A user with no assigned relationship to the order successfully asserts delivery on its service
  line, and the resulting record is indistinguishable from an assertion by the assigned resource.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  As a user unconnected to a given order's assigned resources, attempt to assert delivery on its
  service line and inspect the resulting record against a normal assertion.
```

```yaml
QID: G08-SALE_SERVICE-Q020
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two users asserting delivery on the same service line at nearly the same moment results in one
  recorded, coherent outcome (one assertion accepted, or a defined merge), not a state where the
  line's delivered quantity ends up counted twice.
WHY_IT_MATTERS: >
  A doubled delivered-quantity assertion from a race condition can inflate billing beyond what
  was ordered, an error that is hard to notice because both actions looked legitimate.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous delivery assertions on the same line leave its delivered quantity larger
  than either assertion alone specified, as if both were additively applied.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Arrange two sessions to assert delivery on the same service line at nearly the same time and
  inspect the resulting delivered quantity.
```

```yaml
QID: G08-SALE_SERVICE-Q021
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a scheduled background process can auto-assert delivery for service lines after a fixed
  period, the resulting record is distinguishable from a manual, human assertion, rather than the
  two looking identical in the delivery-assertion history.
WHY_IT_MATTERS: >
  An automatic, time-based assertion carries far less evidentiary weight than a person confirming
  work was done; conflating the two in the record misrepresents the strength of the evidence
  behind a billed service.
DISCONFIRMING_OBSERVATION: >
  A service line auto-asserted delivered by a scheduled process shows an identical
  delivery-assertion record to one manually asserted by an assigned resource.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Where an automatic time-based delivery assertion exists, let it fire on a service line and
  compare the resulting record to a manually asserted one.
```

```yaml
QID: G08-SALE_SERVICE-Q022
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a service line's invoicing policy is switched to bill on ordered quantity specifically
  to bypass the delivered-quantity problem, the order's own delivery-status field is updated to
  match, rather than continuing to report the line as permanently awaiting a delivery that its
  own policy no longer requires.
WHY_IT_MATTERS: >
  A permanently "to deliver" order that has, in fact, been fully and correctly billed misleads
  any operational report built on delivery status into flagging it as an open problem forever.
DISCONFIRMING_OBSERVATION: >
  A service line billed on ordered quantity is fully invoiced, yet the order's delivery-status
  field still shows it as awaiting delivery indefinitely.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a service line to invoice on ordered quantity, fully invoice it, and inspect the
  order's own delivery-status field afterward.
```

```yaml
QID: G08-SALE_SERVICE-Q023
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling an entire order after one of its service lines was already asserted delivered and
  invoiced leaves that already-recognised delivery and invoice intact and explained, rather than
  the cancellation silently erasing or contradicting them.
WHY_IT_MATTERS: >
  Order-level cancellation is a blunt action; if it silently overrides a line-level fact that was
  already true and billed, the financial record no longer matches what actually happened.
DISCONFIRMING_OBSERVATION: >
  Cancelling the order removes or contradicts the delivery assertion and invoice already recorded
  against one of its service lines, with no separate action or explanation.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Assert delivery and invoice one service line on a multi-line order, then cancel the whole
  order and inspect that line's delivery and invoice records afterward.
```

```yaml
QID: G08-SALE_SERVICE-Q024
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The date or timestamp used to assign a service line's recognised revenue to an accounting
  period is a single, documented basis (the assertion date, not silently some other date), applied
  consistently rather than varying by which report or process touches the line.
WHY_IT_MATTERS: >
  A revenue-period cutoff that quietly uses different dates in different places can shift the
  same revenue into different periods depending on which process ran the calculation.
DISCONFIRMING_OBSERVATION: >
  A service line delivered on one date is assigned to different accounting periods by two
  different processes that both claim to use "the delivery date."
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Assert delivery on a service line near a period boundary and compare the period it is assigned
  to across every process or report that performs that assignment.
```

```yaml
QID: G08-SALE_SERVICE-Q025
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user asserting delivery on a service line belonging to a company other than their own, in a
  multi-company setup, is blocked or requires an explicit cross-company permission, rather than
  the assertion succeeding and being silently attributed to the wrong company.
WHY_IT_MATTERS: >
  A cross-company delivery assertion with no control misattributes which legal entity is
  vouching for work being billed, undermining separate books kept for a reason.
DISCONFIRMING_OBSERVATION: >
  A user with no cross-company permission successfully asserts delivery on a service line
  belonging to a different company than their own, with no warning or block.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  In a multi-company setup, attempt to assert delivery on a service line belonging to a company
  the acting user is not assigned to.
```

```yaml
QID: G08-SALE_SERVICE-Q026
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  For a fixed-fee service line ordered with quantity one, a partial delivery assertion is
  either meaningfully supported (e.g. as a percentage) or is clearly and consistently rejected,
  rather than silently accepted as a fractional "one" with an undefined billing consequence.
WHY_IT_MATTERS: >
  "Partial delivery of one" is meaningless unless defined; an undefined acceptance produces
  billing amounts nobody can explain from the ordered quantity and price alone.
DISCONFIRMING_OBSERVATION: >
  A fixed-fee, quantity-one service line accepts a fractional delivered-quantity assertion and
  produces an invoiced amount with no documented rule connecting the fraction to the amount.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  On a quantity-one, fixed-fee service line, attempt to assert a fractional delivered quantity
  and inspect the resulting invoice amount.
```

```yaml
QID: G08-SALE_SERVICE-Q027
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A customer viewing their own order through a self-service portal sees a delivery status for a
  service line that matches the internal delivery-assertion record, rather than a separately
  derived state that can disagree with what staff see internally.
WHY_IT_MATTERS: >
  A customer-facing status that disagrees with the internal record is a direct, visible source of
  the very dispute this whole area exists to prevent.
DISCONFIRMING_OBSERVATION: >
  A service line's delivery status shown to the customer in a self-service view does not match
  the delivery-assertion state shown to internal staff for the same line.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Assert or withhold delivery on a service line and compare the status shown internally to the
  status the customer sees for the same line in a self-service view, if one exists.
```

```yaml
QID: G08-SALE_SERVICE-Q028
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Moving a service line from one order to another after it has already been asserted delivered
  carries its delivery assertion and audit trail with it, rather than the move resetting the line
  to an undelivered state or silently dropping its history.
WHY_IT_MATTERS: >
  A move that erases delivery history could let an already-billed service be billed again on the
  new order, or could lose the only evidence that the work was performed.
DISCONFIRMING_OBSERVATION: >
  A service line already asserted delivered shows as undelivered, with no delivery history,
  immediately after being moved to a different order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Assert delivery on a service line, move it to a different order (where that action is
  available), and inspect its delivery status and history on the destination order.
```

```yaml
QID: G08-SALE_SERVICE-Q029
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reversing a delivery assertion after an invoice has already been generated from it is either
  blocked, or is permitted only alongside a defined consequence for that invoice, rather than
  leaving an active invoice standing on a line the record now says was never delivered.
WHY_IT_MATTERS: >
  An unreversed invoice sitting on top of a retracted delivery assertion means the business is
  actively billing for something its own record now says did not happen.
DISCONFIRMING_OBSERVATION: >
  Reversing a service line's delivery assertion leaves its existing invoice completely
  unaffected and still fully valid.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Assert delivery on a service line, invoice it, then reverse the delivery assertion and inspect
  the invoice's resulting state.
```

```yaml
QID: G08-SALE_SERVICE-Q030
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  For a recurring service billed per period, failing to assert delivery for one period is
  handled by a defined rule (block the next period's billing, carry it forward as still owed, or
  flag it) rather than the missed period silently vanishing with no trace once the next period's
  cycle runs.
WHY_IT_MATTERS: >
  A silently vanishing missed period is either lost revenue the business never notices, or a
  service the customer never received but was billed for anyway on a later period's assumption.
DISCONFIRMING_OBSERVATION: >
  A recurring service's period with no delivery assertion produces no record, flag, or effect
  once the following period's billing cycle has run.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Set up a recurring service line, deliberately skip asserting delivery for one period, let the
  next period's cycle run, and inspect what happened to the skipped period.
```

```yaml
QID: G08-SALE_SERVICE-Q031
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A service line can still be asserted delivered after the order itself has been administratively
  locked or closed only through a defined, visible exception path, not through the same ordinary
  action available before the lock, silently ignoring the lock.
WHY_IT_MATTERS: >
  A lock meant to freeze a closed order that a service line can quietly bypass is not actually a
  lock, and undermines whatever governance reason the order was locked for.
DISCONFIRMING_OBSERVATION: >
  A service line on an administratively locked order is asserted delivered using the exact same
  action available on an unlocked order, with no distinct handling.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Administratively lock or close an order containing an unasserted service line, then attempt to
  assert its delivery through the ordinary action.
```

```yaml
QID: G08-SALE_SERVICE-Q032
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a service line before it has ever been asserted delivered and cancelling one after
  it was asserted delivered produce visibly different outcomes, reflecting that one case erases
  nothing real and the other erases a billed fact.
WHY_IT_MATTERS: >
  If both cases look identical, the system has no way to tell apart "nothing happened here" from
  "billed work is being cancelled after the fact," which is the core risk of this whole area.
DISCONFIRMING_OBSERVATION: >
  Cancelling a never-delivered service line and cancelling an already-delivered, invoiced one
  produce the same message, the same resulting record, and the same audit trail.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Cancel one service line that was never delivered and a separate, otherwise identical line that
  was delivered and invoiced, and compare the two outcomes directly.
```

```yaml
QID: G08-SALE_SERVICE-Q033
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a service line's cost does exist (a standard cost configured on the service product), it
  is recognised at the same reporting moment as the line's revenue, rather than at a different,
  unrelated moment that leaves revenue and its matching cost sitting in different periods.
WHY_IT_MATTERS: >
  Revenue and cost landing in different periods without anyone intending it distorts every
  period's margin figure for a reason that has nothing to do with the business's actual
  performance that period.
DISCONFIRMING_OBSERVATION: >
  A service line's revenue is recognised in one period, and its own configured cost is
  recognised in a different period, with no documented reason for the gap.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure a service line with a standard cost, assert delivery, and compare the period its
  revenue is recognised in against the period its cost is recognised in.
```

```yaml
QID: G08-SALE_SERVICE-Q034
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The delivery-assertion event for a service line is logged with the same rigor (actor, timestamp,
  originating action) as a physical goods-receipt or delivery event, not with less detail simply
  because no physical movement occurred.
WHY_IT_MATTERS: >
  The delivery assertion is the ONLY evidence a service was performed; logging it more thinly
  than a physical event that has other corroborating evidence (a shipment record, a signature)
  leaves the weaker case with the weaker trail.
DISCONFIRMING_OBSERVATION: >
  The audit log entry for a service-line delivery assertion carries materially less detail
  (missing actor, timestamp, or originating action) than the log entry for a physical delivery.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Assert delivery on a service line and on a physical line and compare the two resulting audit
  log entries field for field.
```

```yaml
QID: G08-SALE_SERVICE-Q035
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Increasing a service line's ordered quantity after part of it has already been asserted
  delivered leaves the already-asserted delivered quantity unchanged and still valid, rather than
  the edit resetting, inflating, or invalidating what was already asserted.
WHY_IT_MATTERS: >
  An edit to future scope should not retroactively rewrite a fact already asserted about work
  already billed; conflating the two would let a scope change quietly alter historical billing.
DISCONFIRMING_OBSERVATION: >
  Increasing a partially delivered service line's ordered quantity changes its already-recorded
  delivered quantity with no separate action having touched that figure.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Partially assert delivery on a service line, then increase its ordered quantity, and inspect
  whether the previously-asserted delivered quantity changed.
```

```yaml
QID: G08-SALE_SERVICE-Q036
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a service line requires the customer's own sign-off as evidence of delivery, that sign-off
  is tracked as its own distinct, dated record, separate from the internal staff-side delivered-
  quantity flag, rather than the two being conflated into one indistinguishable state.
WHY_IT_MATTERS: >
  If customer sign-off and internal assertion are the same field, staff can mark a line delivered
  without the customer ever having actually agreed, defeating the purpose of requiring sign-off.
DISCONFIRMING_OBSERVATION: >
  A service line configured to require customer sign-off shows as delivered with no distinct
  customer-sign-off record separate from the internal assertion.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Configure a service line to require customer sign-off, assert internal delivery, and check for
  a separate, distinct sign-off record before treating the line as delivered.
```

```yaml
QID: G08-SALE_SERVICE-Q037
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Applying a discount to a service line after it has already been asserted delivered and invoiced
  does not silently revise the revenue already recognised for that line; the discount attaches to
  a new, separate action (a new invoice line, a credit) rather than rewriting history.
WHY_IT_MATTERS: >
  Silently rewriting already-recognised revenue after the fact makes closed accounting periods
  unstable, since a later discount could retroactively change a figure already reported as final.
DISCONFIRMING_OBSERVATION: >
  Applying a discount to an already-invoiced, already-recognised service line changes the
  revenue figure already recorded for the period it was originally recognised in.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Assert delivery, invoice, and recognise revenue for a service line, then apply a discount to it
  and inspect whether the originally recognised figure changed.
```

```yaml
QID: G08-SALE_SERVICE-Q038
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An aggregate, cross-order view exists (or can be built from available data) showing which
  service lines are still awaiting a delivery assertion, rather than that state being visible
  only one order at a time with no way to see the operational backlog as a whole.
WHY_IT_MATTERS: >
  Without an aggregate view, service delivery that has quietly stalled across many orders has no
  way to surface as an operational problem until a customer complains.
DISCONFIRMING_OBSERVATION: >
  There is no available report, filter, or view that lists service lines awaiting delivery
  assertion across more than one order at a time.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Create several orders with undelivered service lines and search for any available view that
  aggregates them into a single backlog list.
```

```yaml
QID: G08-SALE_SERVICE-Q039
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A deliberately withheld delivery assertion (a business decision to delay billing a materially
  completed service) is distinguishable in the record from a service that genuinely has not yet
  been performed, through some note, reason, or separate marker.
WHY_IT_MATTERS: >
  Without a distinguishing marker, a legitimate business decision to delay billing is
  indistinguishable from work simply not having started, which misrepresents actual delivery
  status to anyone reviewing operational progress.
DISCONFIRMING_OBSERVATION: >
  A service line whose work is materially complete, with billing deliberately delayed as a
  business decision, is recorded identically to a line whose work has genuinely not started.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete a service materially but deliberately withhold its delivery assertion, and compare its
  record to a line where the work genuinely has not started.
```

```yaml
QID: G08-SALE_SERVICE-Q040
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A bundle or kit line containing both a physical component and a service component tracks the
  delivery of each part separately, rather than the whole bundle being marked delivered the
  moment only its physical part ships.
WHY_IT_MATTERS: >
  Treating the bundle as delivered on the physical part alone silently invoices or closes out a
  service component nobody has actually performed yet.
DISCONFIRMING_OBSERVATION: >
  A bundle line shows as fully delivered once its physical component ships, while its service
  component has never been asserted delivered.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create a bundle line combining a physical and a service component, ship the physical part
  only, and inspect the bundle line's overall delivery status.
```

```yaml
QID: G08-SALE_SERVICE-Q041
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Asserting delivery on a service line that belongs to an order still in draft (never confirmed)
  is either blocked outright or is clearly marked as an out-of-sequence, exceptional action,
  rather than behaving exactly like an ordinary assertion on a confirmed order.
WHY_IT_MATTERS: >
  A delivery assertion on an order nobody has committed to yet is evidence for something that may
  never become a real, binding transaction, and treating it as ordinary risks acting on it as if
  it were.
DISCONFIRMING_OBSERVATION: >
  A service line on a still-draft, unconfirmed order accepts a delivery assertion identical in
  every way to one on a confirmed order.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  On a draft, unconfirmed order containing a service line, attempt to assert delivery on that
  line before confirming the order.
```

```yaml
QID: G08-SALE_SERVICE-Q042
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Business-wide "on-time delivery" reporting either excludes service lines with a documented
  reason (they have no ship date to be on time or late against) or includes them under a
  comparable, explicitly defined basis, rather than silently misrepresenting them as always
  on-time by having no date to fail against.
WHY_IT_MATTERS: >
  A metric that silently treats "no date" as "always on time" inflates an on-time performance
  figure by including a whole category of lines that could never have failed it.
DISCONFIRMING_OBSERVATION: >
  An on-time delivery percentage improves, with no documented basis, purely because service lines
  with no ship date are counted as on-time by default.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Include a mix of physical and service lines in the population behind an on-time delivery
  report and inspect how the service lines are treated in the calculation.
```

```yaml
QID: G08-SALE_SERVICE-Q043
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A delivered-quantity assertion on a service line that would exceed its ordered quantity is
  either blocked, requires an explicit override, or is accepted with a visible over-delivery
  indicator, rather than being silently truncated or silently accepted with no trace that it
  exceeded what was ordered.
WHY_IT_MATTERS: >
  Silent truncation hides a real discrepancy between what was asserted and what is recorded;
  silent acceptance can let a line invoice for more than the customer ever ordered.
DISCONFIRMING_OBSERVATION: >
  Asserting a delivered quantity above the ordered quantity on a service line is accepted with no
  warning, override, or visible indicator, and the resulting invoice reflects it with no trace of
  the discrepancy.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Attempt to assert a delivered quantity greater than the ordered quantity on a service line and
  inspect the resulting record and any subsequent invoice.
```

```yaml
QID: G08-SALE_SERVICE-Q044
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a service product is configured to allow more than one delivery-recognition method at
  once (e.g. manual assertion alongside automatic time-based recognition), the system prevents
  both from independently firing on the same line, rather than allowing the line to be recognised
  or billed twice through two different paths.
WHY_IT_MATTERS: >
  Two independent recognition paths that can both fire on the same line is a direct double-billing
  or double-recognition risk that would be hard to notice because each path looks correct alone.
DISCONFIRMING_OBSERVATION: >
  A service line configured with two possible recognition methods has its revenue recognised or
  its invoice generated twice, once through each method, for the same underlying delivery.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Configure a service line with two simultaneously available recognition or delivery methods and
  trigger both, then inspect whether recognition or billing occurred more than once.
```

```yaml
QID: G08-SALE_SERVICE-Q045
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reassigning the resource responsible for performing a service after part of it has already been
  asserted delivered does not retroactively change who is recorded as having made that earlier
  assertion.
WHY_IT_MATTERS: >
  Reassignment reflects who does the remaining work going forward; letting it silently rewrite
  who is credited with, or accountable for, work already asserted done would falsify history for
  a purely administrative change.
DISCONFIRMING_OBSERVATION: >
  Reassigning the responsible resource on a partially delivered service line changes the
  attributed actor on delivery assertions already made before the reassignment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Partially assert delivery on a service line under one assigned resource, reassign the line to a
  different resource, and inspect the attribution on the earlier assertion.
```

```yaml
QID: G08-SALE_SERVICE-Q046
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a service line's price is expressed per unit of time (e.g. per hour) rather than per
  discrete unit, the delivered-quantity assertion is expressed and stored in that same time unit
  consistently, not silently converted to or compared against a different, mismatched unit
  somewhere in the invoicing path.
WHY_IT_MATTERS: >
  A silent, undocumented unit mismatch between the assertion and the price produces an invoiced
  amount that does not correspond to the quantity anyone actually asserted.
DISCONFIRMING_OBSERVATION: >
  A time-priced service line's invoiced amount does not correspond to its asserted delivered
  quantity when both are expressed in the same stated unit.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Configure a service line priced per unit of time, assert a delivered quantity in that unit, and
  verify the invoiced amount against that quantity and the stated price.
```

```yaml
QID: G08-SALE_SERVICE-Q047
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Archiving or deactivating the service product itself does not remove or corrupt the delivery-
  assertion history of already-confirmed order lines that used it; historical lines remain
  intact and traceable back to what they were when ordered.
WHY_IT_MATTERS: >
  Product catalogue maintenance (retiring old services) is routine; if it silently damages
  historical order and delivery records, ordinary catalogue hygiene becomes a data-integrity risk.
DISCONFIRMING_OBSERVATION: >
  Archiving the service product used on a confirmed, already-delivered order line causes that
  line's delivery-assertion history to become unreadable, blank, or inconsistent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm and deliver a service line, archive or deactivate the underlying service product, and
  re-inspect the order line's delivery history.
```

```yaml
QID: G08-SALE_SERVICE-Q048
MODULE: sale_service
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user with permission to view an order's commercial figures but explicitly denied permission
  to view internal cost or margin figures cannot infer a zero- or near-zero-cost service line's
  margin simply because "no cost" is visually indistinguishable from "cost hidden by permission."
WHY_IT_MATTERS: >
  If a genuinely zero-cost line and a cost-hidden-by-permission line look the same to a restricted
  viewer, the permission boundary is defeated by inference rather than by a real access control.
DISCONFIRMING_OBSERVATION: >
  A user denied cost visibility can distinguish, with certainty, a zero-cost service line from a
  line whose real cost is simply hidden from them, defeating the intended permission boundary.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user denied cost-visibility permission, compare the displayed state of a genuinely
  zero-cost service line against a line whose cost is hidden by that permission.
```
