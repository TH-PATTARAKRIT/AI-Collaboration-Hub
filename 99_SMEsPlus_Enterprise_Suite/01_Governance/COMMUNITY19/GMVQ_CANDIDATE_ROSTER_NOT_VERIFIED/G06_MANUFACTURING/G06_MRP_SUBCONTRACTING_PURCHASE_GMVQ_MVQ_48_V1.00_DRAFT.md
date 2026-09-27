# SMEsPlus ENTERPRISE SUITE
## GMVQ — G06 MANUFACTURING / mrp_subcontracting_purchase Module MVQ Bank

**Document ID:** GMVQ-G06-MRP_SUBCONTRACTING_PURCHASE-MVQ48-V1.00
**Group:** G06 MANUFACTURING
**Module Metadata:** `mrp_subcontracting_purchase`
**Wave:** W2
**Author Cell:** P12
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose
This bank supplies the module-specific research questions for `mrp_subcontracting_purchase` —
the seam between a commercial document and a production order that describe the same
subcontracted event and can disagree: quantity ordered versus produced versus received, price
agreed versus billed, which side is authoritative, and what a change on one side does to the
other. It is written for a blind two-lane study: Lane A reads reference source, Lane B
observes a running system, and neither sees the other's answers. Question text is
source-neutral throughout and contains no model, field, or module identifier. Nothing here
concerns ledger posting or valuation — that seam belongs to the sibling ledger bank.

## Control
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- Bridge-module rule applied: every question below fails the "remove the second capability"
  test — none would still make sense if either the outside-party production capability or the
  commercial purchasing capability were removed and the other used alone. Base subcontracting
  invariants (ownership at the external party, unreturned components, traceability across an
  unobserved boundary) belong to `mrp_subcontracting`, and ledger/valuation consequences belong
  to the sibling `mrp_subcontracting_account` bank; neither is repeated here.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread
  across quantity/authority disagreement, price-and-bill matching, order/production sequencing,
  cancellation while production is underway, lead-time visibility, three-way match semantics,
  approval-authority separation, and company/currency/date boundary conditions.
- This bank is DRAFT authoring output only. Not approved, not frozen, not verified.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived here.

---

## G06-MRP_SUBCONTRACTING_PURCHASE-Q001

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q001
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The quantity stated on the commercial order, the quantity the production order reports as
  completed, and the quantity actually received are each tracked as distinguishable figures,
  not collapsed into a single number that stands in for all three.
WHY_IT_MATTERS: >
  Collapsing three quantities that can legitimately differ into one hides exactly the
  disagreement a reviewer would need to see to catch a shortfall or an overrun.
DISCONFIRMING_OBSERVATION: >
  A case engineered so the ordered, produced, and received quantities differ from each other
  shows only a single quantity value anywhere in the record, with the other two unrecoverable.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Engineer a subcontracted transaction where the ordered, produced, and received quantities are
  deliberately made to differ, then check whether all three remain independently visible.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q002

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q002
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the commercial order's quantity and the production order's completed quantity disagree,
  one of the two is designated the authoritative figure for downstream billing, and that
  designation is consistent and inspectable rather than depending on whichever document a
  particular screen happens to read from.
WHY_IT_MATTERS: >
  An undeclared authority means two different parts of the system can legitimately act on two
  different numbers for the same underlying event, and nobody can say which one is "right."
DISCONFIRMING_OBSERVATION: >
  Two different downstream processes reading the same disagreeing pair of quantities each treat
  a different one as authoritative, with no documented rule explaining which should govern.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Create a case where commercial-order quantity and production-order quantity disagree, then
  trace which figure two different downstream consumers of that data each use.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q003

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q003
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The ability to change the commercial order's quantity or price and the ability to change the
  production order's planned quantity are governed by distinct permissions, so a person
  authorized to adjust one is not automatically authorized to adjust the other.
WHY_IT_MATTERS: >
  If either side can be edited by whoever can edit the other, the separation between what was
  commercially agreed and what was actually run on the floor stops meaning anything.
DISCONFIRMING_OBSERVATION: >
  A user holding permission to edit only the production order is also able to change the
  commercial order's quantity or price, or vice versa, with no separate permission required.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Grant a user permission to edit only one of the two documents and attempt to edit the other.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q004

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q004
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Starting the production side of a subcontracted process before its commercial order has been
  confirmed is either explicitly blocked or leaves a visible flag on the resulting records,
  rather than proceeding as if the commercial order had always been in place.
WHY_IT_MATTERS: >
  An unflagged head start means physical work happens with no formal commercial commitment
  behind it yet, which is exactly the situation a later dispute over what was actually agreed
  would hinge on.
DISCONFIRMING_OBSERVATION: >
  Production activity recorded before the commercial order was confirmed shows no
  distinguishing flag and no block, appearing identical to production that started after
  confirmation.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Begin recording production activity for a subcontracted order before its commercial order
  reaches a confirmed state, and inspect whether that sequencing is visible anywhere.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q005

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q005
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A subcontracted production event that has no corresponding commercial order at all is
  surfaced as an exception state, rather than being treated as a normal, fully valid
  transaction with nothing distinguishing it from one that has proper commercial backing.
WHY_IT_MATTERS: >
  Work performed by an outside party with no commercial order behind it at all means the
  company has no formal basis to dispute price, quantity, or even the fact the work happened,
  and needs to know that gap exists.
DISCONFIRMING_OBSERVATION: >
  A subcontracted production event with no linked commercial order at all proceeds through
  completion with no flag, warning, or distinguishable state versus one with a proper
  commercial order.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Record a subcontracted production event with no commercial order linked at all and observe
  whether the system treats it differently from a normally linked one.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q006

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q006
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reducing the commercial order's quantity after components have already been physically sent
  to the outside party for the original quantity either triggers a reconciliation prompt
  covering the components already committed, or is blocked, rather than silently orphaning the
  excess components sent.
WHY_IT_MATTERS: >
  Silently orphaning components sent for a quantity the order no longer reflects leaves those
  units unaccounted for in either the commercial or the production picture.
DISCONFIRMING_OBSERVATION: >
  Reducing the commercial order's quantity after components were sent for the original, larger
  quantity leaves no record, prompt, or flag addressing what happens to the excess
  already-sent components.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Send components for a subcontracted order's original quantity, then reduce the commercial
  order's quantity, and inspect what happens to the excess already-sent components.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q007

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q007
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Increasing the commercial order's quantity after an initial batch of components has already
  been sent does not silently assume the additional components were also already sent; it
  distinguishes what has actually been dispatched from what the revised order now calls for.
WHY_IT_MATTERS: >
  Assuming components were sent just because the order now calls for more would let a paper
  quantity change stand in for a physical dispatch that never happened.
DISCONFIRMING_OBSERVATION: >
  After a commercial order's quantity is increased, the record shows the full increased
  quantity as already sent to the outside party with no additional dispatch event having
  occurred.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Send an initial batch of components, then increase the commercial order's quantity, and
  check whether the record shows more components sent than were actually dispatched.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q008

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q008
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A service bill priced differently from the price stated on the commercial order is flagged as
  a discrepancy requiring resolution before it is accepted as a normal transaction, rather than
  the billed price silently overriding the agreed price with no comparison ever made.
WHY_IT_MATTERS: >
  A billing price that quietly overrides the agreed price removes the entire commercial point
  of having agreed a price in the first place.
DISCONFIRMING_OBSERVATION: >
  A service bill priced differently from the commercial order's stated price is accepted with
  no discrepancy flag and no comparison against the agreed price anywhere in the process.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Issue a service bill priced differently from the commercial order's agreed price and observe
  whether the difference is flagged before acceptance.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q009

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q009
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Resolving a flagged price discrepancy between the commercial order and the outside party's
  bill requires an explicit approval action distinguishable from the routine action of simply
  accepting a bill that matches.
WHY_IT_MATTERS: >
  If accepting a mismatched bill takes the same single click as accepting a matched one, the
  discrepancy flag exists in name only and provides no actual control.
DISCONFIRMING_OBSERVATION: >
  A bill flagged for a price discrepancy is accepted through the exact same action, with no
  additional approval step, as a bill that matched the order.
EXPECTED_SURFACE: S3,S4,S5
PRECONDITIONS: >
  Compare the acceptance action available for a bill that matches the order's price against the
  action available for a bill flagged with a price discrepancy.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q010

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q010
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The outside party's service can be billed and recorded before the corresponding output has
  actually been received, and this state is distinguishable from a bill that arrived after
  receipt, rather than the two looking identical in the record.
WHY_IT_MATTERS: >
  Being unable to tell "billed before receipt" from "billed after receipt" removes the one
  signal that would let someone notice they are paying for output that has not actually shown
  up yet.
DISCONFIRMING_OBSERVATION: >
  A service bill recorded before the matching output was received looks identical in the
  record to one recorded after receipt, with no timestamp relationship or flag distinguishing
  the two cases.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a service bill before the corresponding output is received, then record one after
  receipt for a comparable order, and compare how each is represented.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q011

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q011
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The date the physical output is received and the date the outside party's service is billed
  are each recorded as their own independent date, rather than one date being used to stand in
  for both events.
WHY_IT_MATTERS: >
  Using a single date for two genuinely different events destroys any ability to measure how
  long billing lagged behind receipt, or vice versa, which is itself a meaningful operational
  signal.
DISCONFIRMING_OBSERVATION: >
  A subcontracted transaction where receipt and billing happened on different actual days shows
  the same single date recorded for both events.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Arrange a case where output receipt and service billing genuinely occur on different days and
  inspect whether each event's own date is separately recorded.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q012

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q012
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Cancelling the commercial order while the outside party's production is already underway
  surfaces the conflict — components already sent, work already started — for a decision,
  rather than the cancellation proceeding as if the physical process had never begun.
WHY_IT_MATTERS: >
  A cancellation that ignores physical reality already in motion leaves components at the
  outside party with no commercial basis for their return, replacement, or payment.
DISCONFIRMING_OBSERVATION: >
  Cancelling a commercial order proceeds with no warning, block, or flag, even though
  components are recorded as already sent and production as already underway at the outside
  party.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Send components and begin production at the outside party, then cancel the commercial order,
  and observe whether the conflict is surfaced.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q013

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q013
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling the commercial order does not automatically cancel or silently close the linked
  production order; the production side's own state is handled as a distinguishable decision.
WHY_IT_MATTERS: >
  An automatic cascade that force-closes production the moment the commercial paperwork is
  cancelled could discard a genuine physical process that is still actually running at the
  outside party.
DISCONFIRMING_OBSERVATION: >
  Cancelling the commercial order automatically transitions the linked production order to a
  cancelled or closed state with no separate action or confirmation for the production side.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Cancel a commercial order linked to an in-progress production order and observe whether the
  production order's own state changes automatically.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q014

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q014
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The lead time assumed by the commercial order for planning purposes and the schedule actually
  being tracked on the production side are each visible on their own terms, so a mismatch
  between the two is something a planner could actually notice.
WHY_IT_MATTERS: >
  If the commercial lead time and the real production schedule are never shown side by side,
  planning decisions get made against a number that may have quietly diverged from what is
  actually happening.
DISCONFIRMING_OBSERVATION: >
  There is no way to compare the commercial order's assumed lead time against the production
  order's actual schedule for the same subcontracted transaction; only one of the two is
  visible at a time.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Set a commercial order's lead time to differ materially from the production order's actual
  schedule and attempt to view both together.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q015

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q015
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A three-way match for a subcontracted purchase compares the commercial order, the service
  actually billed, and the production output actually received — not the components sent,
  which a naive goods-received match would otherwise mistakenly compare the bill against.
WHY_IT_MATTERS: >
  Matching the bill against the value of the company's own components, instead of against the
  service and the output, would approve or reject bills based on the wrong quantity entirely.
DISCONFIRMING_OBSERVATION: >
  A subcontracted transaction's matching process compares the billed amount against the
  quantity or value of components sent, rather than against the service ordered and the output
  received.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Run a subcontracted transaction through whatever matching process exists and inspect which
  three things are actually being compared against each other.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q016

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q016
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whatever tolerance is allowed between ordered, billed, and received figures for an ordinary
  purchase is a setting that can be configured distinctly for a subcontracted transaction,
  rather than one fixed tolerance applying to both regardless of the fact that subcontracting
  compares a service and an output rather than goods and goods.
WHY_IT_MATTERS: >
  A tolerance tuned for ordinary goods-for-goods purchasing may be entirely wrong for a
  service-for-output comparison, and forcing the same number onto both hides that mismatch.
DISCONFIRMING_OBSERVATION: >
  No distinct tolerance setting exists for subcontracted transactions; attempting to configure
  one separately from ordinary purchase tolerance has no effect.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Attempt to configure a match tolerance specific to subcontracted transactions, separate from
  the tolerance used for ordinary purchases, and observe whether it takes effect independently.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q017

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q017
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Approving the commercial order — committing to price and quantity with the outside party —
  and approving the production order — authorizing the internal work plan — are governed by
  separate approval authorities, so one person's sign-off on one side does not stand in for
  approval of the other.
WHY_IT_MATTERS: >
  Merging the two approvals into one lets a single person commit the company commercially and
  internally at once, defeating any control that assumed the two would be checked
  independently.
DISCONFIRMING_OBSERVATION: >
  A single approval action, taken by one person, is treated as covering both the commercial
  order and the production order with no second, distinct approval required for either.
EXPECTED_SURFACE: S4,S5,S7
PRECONDITIONS: >
  Trace the approval steps required for the commercial order and for the production order on
  the same subcontracted transaction and determine whether they are distinct actions.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q018

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q018
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Receiving more output than the commercial order's quantity calls for is flagged as an
  over-receipt requiring a decision, rather than being silently accepted and billed as if it
  had always been the ordered amount.
WHY_IT_MATTERS: >
  Silently accepting an over-receipt removes the commercial control that quantity ordered is
  supposed to represent, and can commit the company to paying for quantity nobody agreed to.
DISCONFIRMING_OBSERVATION: >
  Receiving a quantity greater than the commercial order calls for is accepted without any
  flag, and the order is treated as satisfied for the larger, unapproved quantity.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Record a received quantity greater than the commercial order's stated quantity and observe
  whether that discrepancy is flagged before the order is considered fulfilled.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q019

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q019
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An order that receives less than its full ordered quantity is left in a state distinguishable
  from full completion, rather than being marked fully satisfied once any output at all has
  been received.
WHY_IT_MATTERS: >
  Marking a partially fulfilled order as fully done removes any prompt to ever chase or account
  for the missing balance.
DISCONFIRMING_OBSERVATION: >
  An order that has received only part of its ordered quantity shows the same completed status
  as one that received its full quantity, with nothing distinguishing the shortfall.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Receive less than the full ordered quantity against a commercial order and inspect the
  resulting order status against a fully received comparable order.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q020

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q020
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Declaring a subcontracted order fulfilled despite a quantity disagreement between the
  commercial and production sides requires an authority distinct from the routine confirmation
  used when the two sides already agree.
WHY_IT_MATTERS: >
  If closing a disputed order takes the same casual action as closing an uncontested one, the
  disagreement never actually forces anyone to make a decision about it.
DISCONFIRMING_OBSERVATION: >
  Closing an order with a known quantity disagreement between its commercial and production
  sides uses the identical action, with the identical authority required, as closing an order
  with no disagreement at all.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Compare the action required to close an order where commercial and production quantities
  agree against one where they are known to disagree.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q021

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q021
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Output delivered after the commercial order's expected date is received and recorded
  normally, with the lateness itself surfaced as a distinguishable fact rather than either
  blocking receipt or erasing any record that the date was missed.
WHY_IT_MATTERS: >
  If a late delivery either can't be received at all or leaves no trace that it was late, the
  company loses both operational flexibility and the data it would need to hold the outside
  party accountable.
DISCONFIRMING_OBSERVATION: >
  Output received after the expected date shows no distinguishable record of the lateness,
  appearing identical to output that arrived on time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive output after a commercial order's expected date has passed and inspect whether the
  lateness is recorded as a distinguishable fact.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q022

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q022
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Amending a commercial order's quantity or price after it was originally confirmed preserves
  the prior value in a retrievable history, rather than the amendment overwriting the original
  with no trace of what was first agreed.
WHY_IT_MATTERS: >
  Losing the original agreed terms the moment an amendment is made removes the only record of
  what actually changed and when, which is exactly what a later dispute over the order would
  need.
DISCONFIRMING_OBSERVATION: >
  Amending a confirmed commercial order's quantity or price leaves no retrievable record of the
  value that existed before the amendment.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm a commercial order, amend its quantity or price, and attempt to retrieve the value
  that existed before the amendment.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q023

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q023
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the commercial order is amended at nearly the same moment the production side reports
  completion, the resulting record reflects one consistent, determinable outcome for which
  quantity governed, rather than an outcome that depends on unpredictable timing between the
  two events.
WHY_IT_MATTERS: >
  An outcome that depends on which of two near-simultaneous events happened to be processed
  first is not something anyone can rely on or reproduce when investigating a discrepancy
  later.
DISCONFIRMING_OBSERVATION: >
  Repeating the same near-simultaneous amendment-and-completion sequence produces different
  final quantities on different attempts, with no deterministic rule explaining which should
  win.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Arrange for a commercial order amendment and a production completion event to occur in
  immediate succession and observe whether the outcome is consistent across repeated attempts.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q024

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q024
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Rejecting a service bill outright returns the commercial order to a state where a corrected
  bill can still be matched against it, rather than leaving the order stuck in a state that can
  never again reach normal completion.
WHY_IT_MATTERS: >
  An order that gets permanently stuck once one bill is rejected forces a workaround outside the
  normal process just to correct an honest billing mistake.
DISCONFIRMING_OBSERVATION: >
  Rejecting a service bill leaves the commercial order in a state where no subsequent,
  corrected bill can be matched or accepted against it.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Reject a service bill against a subcontracted commercial order and then attempt to submit a
  corrected bill against the same order.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q025

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q025
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The commercial matching of order, bill, and receipt for a subcontracted transaction functions
  independently of whether the financial valuation-posting capability is active, so a company
  using only the commercial-document side still gets a working three-way comparison.
WHY_IT_MATTERS: >
  If commercial matching silently depends on the ledger capability being active, disabling
  accounting integration for any reason would quietly disable the purchasing controls too, with
  no warning.
DISCONFIRMING_OBSERVATION: >
  With the financial valuation-posting capability disabled, the commercial matching of order,
  bill, and receipt for a subcontracted transaction stops functioning or stops flagging
  discrepancies.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Disable the financial valuation-posting capability and run a subcontracted transaction with a
  deliberate order/bill/receipt discrepancy, then check whether the discrepancy is still
  flagged.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q026

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q026
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A commercial order and its linked production order for a subcontracted transaction belong to
  the same company; the system does not allow the two halves of one transaction to be split
  across two different companies within the same deployment.
WHY_IT_MATTERS: >
  Allowing the commercial and production halves of one transaction to belong to different
  companies would make it structurally impossible to produce a clean set of books for either
  company on its own.
DISCONFIRMING_OBSERVATION: >
  A subcontracted transaction is created with its commercial order under one company and its
  linked production order under a different company, and the system allows this without
  objection.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Attempt to create a subcontracted transaction where the commercial order and the production
  order are associated with two different companies in the same deployment.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q027

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q027
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If a configuration exists to bypass the normal order/bill/receipt matching for subcontracted
  transactions, using that bypass leaves a visible, distinguishable trace on the resulting
  record, rather than looking identical to a transaction that was properly matched.
WHY_IT_MATTERS: >
  An invisible bypass would let bills get paid with no real matching ever having occurred,
  while every record looks exactly as trustworthy as one that was actually checked.
DISCONFIRMING_OBSERVATION: >
  A subcontracted transaction processed through a matching bypass shows no distinguishing
  record from one that went through the full match, when reviewed after the fact.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Locate and use any available bypass of the standard matching process for a subcontracted
  transaction, then compare the resulting record to one that went through full matching.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q028

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q028
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The commercially agreed price for the outside party's service is not exposed on the
  production-facing view of the subcontracted order, keeping commercial terms and the physical
  work plan on separate surfaces.
WHY_IT_MATTERS: >
  Surfacing commercial pricing on a screen meant for tracking physical production exposes
  negotiated terms to a wider group of people than the commercial process intends.
DISCONFIRMING_OBSERVATION: >
  The commercially agreed service price is visible on the production-facing view of a
  subcontracted order, with no separation between the two surfaces.
EXPECTED_SURFACE: S4,S5
PRECONDITIONS: >
  Set a commercially agreed price on a subcontracted order and inspect the production-facing
  view of that same order for whether the price appears.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q029

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q029
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A second service bill submitted against a subcontracted order that has already been fully
  matched and paid is flagged as a duplicate or exception requiring review, rather than being
  processed as a new, ordinary, independent bill.
WHY_IT_MATTERS: >
  Processing a bill against an already-settled order as if it were routine opens the door to
  being billed and paying twice for the same completed work.
DISCONFIRMING_OBSERVATION: >
  A second bill against an already fully matched and paid subcontracted order proceeds through
  normal processing with no duplicate or exception flag raised.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Fully match and pay a subcontracted order, then submit a second service bill against the same
  order, and observe whether it is flagged.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q030

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q030
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A partial delivery against a commercial order line does not close that line item to further
  receipt unless the full ordered quantity has actually been satisfied or the remainder is
  explicitly resolved.
WHY_IT_MATTERS: >
  A line item closed prematurely after only a partial delivery would make the remaining,
  still-owed quantity unreceivable through the normal process, forcing an off-process
  workaround.
DISCONFIRMING_OBSERVATION: >
  A commercial order line closes to further receipt after only a partial quantity has been
  delivered, with the remaining quantity neither received nor explicitly resolved.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Deliver a partial quantity against a commercial order line and attempt to receive the
  remaining quantity afterward.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q031

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q031
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Changing the production order's planned quantity does not automatically change the commercial
  order's quantity; any alignment between the two requires a distinguishable, deliberate action
  on the commercial side.
WHY_IT_MATTERS: >
  An automatic propagation from production planning straight into a binding commercial
  commitment would let an internal planning adjustment silently change what the company has
  agreed to pay for.
DISCONFIRMING_OBSERVATION: >
  Changing the production order's planned quantity is reflected as an equivalent, automatic
  change on the commercial order's quantity with no separate commercial action taken.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Change the planned quantity on a subcontracted production order and inspect whether the
  linked commercial order's quantity changes without a separate action.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q032

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q032
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A service bill submitted with no linked commercial order at all is rejected or held for
  exception review rather than being processed as an ordinary, acceptable transaction.
WHY_IT_MATTERS: >
  Accepting a bill with nothing to match it against removes the entire point of having a
  commercial order as the basis for what the company agreed to pay.
DISCONFIRMING_OBSERVATION: >
  A service bill with no linked commercial order at all is processed and accepted through the
  normal path with no exception or hold.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit a service bill for subcontracted work with no commercial order linked at all and
  observe whether it is accepted or held.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q033

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q033
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a subcontracted order's effective price changes after initial agreement, the record
  distinguishes whether the change originated from an internal amendment or from accepting a
  differently priced bill.
WHY_IT_MATTERS: >
  Being unable to tell whether a price moved because someone internally changed it or because a
  bill was simply accepted as-is removes the ability to hold the right side accountable for the
  change.
DISCONFIRMING_OBSERVATION: >
  A price change on a subcontracted order carries no record of whether it originated from an
  internal amendment or from accepting a bill priced differently than agreed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Produce one price change via internal amendment and one via accepting a differently priced
  bill, and compare what each leaves in the record.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q034

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q034
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The approval chain required for a subcontracted commercial order can be configured distinctly
  from the approval chain for an ordinary purchase, reflecting that subcontracting carries
  different risk — physical custody at a third party — than a straightforward goods purchase.
WHY_IT_MATTERS: >
  Forcing subcontracted orders through the identical approval chain as any other purchase
  ignores that this specific transaction type puts the company's own components at a location
  it does not control.
DISCONFIRMING_OBSERVATION: >
  No distinct approval chain can be configured for subcontracted commercial orders; only the
  same chain used for ordinary purchases is available.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Attempt to configure a distinct approval chain specifically for subcontracted commercial
  orders and observe whether it applies independently of the ordinary purchase approval chain.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q035

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q035
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a commercial order still in draft does not remove or silently alter a production
  order that has already progressed past the draft stage, even where the two are linked.
WHY_IT_MATTERS: >
  Deleting the commercial paperwork should not be a backdoor way to erase the record of physical
  work that has already actually begun.
DISCONFIRMING_OBSERVATION: >
  Deleting a draft commercial order also deletes or silently alters a linked production order
  that has already progressed past its own draft stage.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Advance a linked production order past its draft stage while its commercial order remains in
  draft, then delete the commercial order and inspect the production order.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q036

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q036
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  For a subcontracted commercial order with multiple line items, quantity and price matching is
  evaluated per line, so one line's discrepancy is flagged even if it is offset by another
  line's opposite discrepancy at the order total.
WHY_IT_MATTERS: >
  Evaluating only the order total would let a shortfall on one line hide behind an overage on
  another, with neither ever individually reviewed.
DISCONFIRMING_OBSERVATION: >
  A multi-line subcontracted order where one line under-delivers and another over-delivers by a
  matching amount shows no discrepancy at all because only the order total was compared.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a multi-line subcontracted order where individual lines disagree with their received
  quantities in offsetting directions, and inspect whether each line is evaluated
  independently.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q037

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q037
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the entire production output for a subcontracted order is scrapped after receipt, the
  commercial order's fulfilled status reflects that the physical output no longer exists
  usably, rather than remaining marked as satisfied purely because a receipt event once
  occurred.
WHY_IT_MATTERS: >
  Treating the commercial order as satisfied by a receipt that has since been entirely scrapped
  would let the company appear to have gotten what it paid for when, physically, it has
  nothing.
DISCONFIRMING_OBSERVATION: >
  A commercial order remains marked fully satisfied after its entire received output has
  subsequently been scrapped, with no distinguishable record connecting the scrap to the
  order's fulfillment status.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Receive output against a subcontracted commercial order, then scrap all of that received
  output, and inspect the commercial order's fulfillment status afterward.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q038

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q038
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the same individual is permitted to both raise a subcontracted commercial order and
  later confirm receipt against it is an explicit, inspectable segregation-of-duties setting,
  not an accident of whatever permissions that person happens to hold for unrelated reasons.
WHY_IT_MATTERS: >
  An unexamined ability for one person to both commit to and confirm the same transaction
  removes a control point that segregation of duties specifically exists to provide.
DISCONFIRMING_OBSERVATION: >
  No setting exists anywhere to restrict or examine whether the same individual can both raise
  a subcontracted commercial order and confirm receipt against it.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Look for a segregation-of-duties setting governing order-raising and receipt-confirmation
  roles for subcontracted transactions, and test whether one person holding both permissions is
  flagged anywhere.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q039

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q039
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Amending a commercial order's price or quantity after part of it has already been billed
  applies only to the remaining, not-yet-billed portion, leaving the already-billed portion's
  terms undisturbed.
WHY_IT_MATTERS: >
  An amendment that reaches back and changes the terms of a portion already billed and accepted
  would rewrite a transaction that both sides already considered settled.
DISCONFIRMING_OBSERVATION: >
  Amending a commercial order after partial billing changes the terms attributed to the
  already-billed portion, not only the remaining portion.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Partially bill a commercial order, then amend its price or quantity, and inspect whether the
  already-billed portion's recorded terms changed.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q040

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q040
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the linked production order is cancelled while a service bill against it is mid-approval,
  that in-flight approval is surfaced as needing a decision, rather than either completing
  automatically or vanishing with no record.
WHY_IT_MATTERS: >
  A bill approval left to complete on autopilot after the underlying production has been
  cancelled could pay for something that, as of the cancellation, is no longer actually
  happening.
DISCONFIRMING_OBSERVATION: >
  A production order cancellation occurs while a linked bill approval is mid-flight, and that
  approval subsequently completes automatically or disappears with no record of the conflict.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Start a bill approval for a subcontracted transaction, cancel the linked production order
  before the approval completes, and observe what happens to the pending approval.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q041

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q041
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The cumulative total billed across every bill submitted against a single subcontracted
  commercial order is checked against the order's agreed value, so repeated partial bills
  cannot together exceed what a single full bill would have been checked against, without an
  explicit override.
WHY_IT_MATTERS: >
  Checking each bill only in isolation, rather than cumulatively, would let a series of small
  partial bills quietly add up to far more than the order ever authorized.
DISCONFIRMING_OBSERVATION: >
  A series of partial bills against the same subcontracted order together exceed the order's
  agreed value with no override having been recorded, and no check catches the cumulative
  total.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit a series of partial bills against the same subcontracted order whose cumulative total
  exceeds the order's agreed value, and observe whether the excess is caught.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q042

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q042
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A commercial order created with a zero ordered quantity cannot be matched against any actual
  receipt; a nonzero receipt against it is treated as an exception requiring resolution rather
  than a routine automatic match.
WHY_IT_MATTERS: >
  Allowing any actual output to match cleanly against a zero-quantity order would erase the
  very distinction a zero-quantity placeholder order exists to preserve.
DISCONFIRMING_OBSERVATION: >
  A nonzero quantity received against a commercial order whose quantity is zero matches and
  closes normally, with no exception raised.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a commercial order with a zero ordered quantity, record a nonzero receipt against it,
  and observe whether the mismatch is flagged.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q043

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q043
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A commercial order for subcontracted work can be raised in a currency different from the
  owning company's internal costing currency, with an explicit, inspectable conversion applied
  rather than the two being silently assumed identical.
WHY_IT_MATTERS: >
  Silently assuming the two currencies are the same, when a genuinely foreign-currency
  arrangement exists, would misstate whatever internal cost figure depends on the commercial
  terms.
DISCONFIRMING_OBSERVATION: >
  A commercial order raised in a currency different from the internal costing currency shows no
  conversion applied anywhere in the resulting production-side cost figures.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Raise a commercial order for subcontracted work in a currency different from the internal
  costing currency and inspect whether a conversion is applied on the production side.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q044

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q044
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Setting a commercial order's effective date earlier than when it was actually created is
  either restricted to an explicit, logged override, or blocked outright, rather than being
  freely settable with no record that the date does not match when the order was actually
  raised.
WHY_IT_MATTERS: >
  A freely back-datable commercial order could be used to manufacture retroactive commercial
  cover for production that had already started without one, defeating the purpose of
  requiring an order at all.
DISCONFIRMING_OBSERVATION: >
  A commercial order's effective date is set earlier than its actual creation date with no
  override logged and no restriction encountered.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Attempt to set a commercial order's effective date to a point before its actual creation time
  and observe whether this is restricted or logged.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q045

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q045
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Output received at a location different from the one the commercial order specifies is
  flagged as a location discrepancy rather than being silently accepted and matched as if it
  had arrived where expected.
WHY_IT_MATTERS: >
  Silently accepting a wrong-location receipt could match and close an order while the
  company's own inventory records point to the wrong place for where the physical goods
  actually are.
DISCONFIRMING_OBSERVATION: >
  Output received at a location different from the one the commercial order specifies is
  matched and the order closed with no discrepancy flag regarding the location.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Record receipt of subcontracted output at a location different from the one specified on the
  commercial order and observe whether the mismatch is flagged.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q046

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q046
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Splitting a commercial order line's delivery into several partial shipments does not change
  the total price agreed for that line; the sum across the resulting partial bills equals the
  original single-delivery price.
WHY_IT_MATTERS: >
  A pure logistics choice, splitting one delivery into several, should never be able to change
  what the company ultimately owes for the same ordered quantity.
DISCONFIRMING_OBSERVATION: >
  The sum of bills issued against a commercial order line delivered in several partial
  shipments differs from the price that a single, undivided delivery of the same line would
  have carried.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compare the total price billed for a commercial order line delivered as several partial
  shipments against the price for an equivalent line delivered in one shipment.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q047

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q047
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A user with only read-only or reporting access to subcontracted transactions can still see a
  flagged quantity or price discrepancy, rather than that flag being visible only to roles with
  edit access.
WHY_IT_MATTERS: >
  Hiding a discrepancy flag from anyone without edit rights would prevent an oversight or audit
  role, which typically has read-only access by design, from ever noticing the very problems it
  exists to catch.
DISCONFIRMING_OBSERVATION: >
  A user with read-only access to a subcontracted transaction cannot see a discrepancy flag
  that a user with edit access to the same transaction can see.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Create a flagged discrepancy on a subcontracted transaction and compare what a read-only role
  and an edit-capable role can each see regarding that flag.
```

## G06-MRP_SUBCONTRACTING_PURCHASE-Q048

```yaml
QID: G06-MRP_SUBCONTRACTING_PURCHASE-Q048
MODULE: mrp_subcontracting_purchase
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Deactivating the outside party as an ongoing business relationship does not retroactively
  alter or hide previously issued commercial orders and their matching history with that party.
WHY_IT_MATTERS: >
  Losing visibility into historical commercial orders just because the relationship with that
  party has since ended would erase exactly the record a later dispute or audit over past work
  would need.
DISCONFIRMING_OBSERVATION: >
  Deactivating an outside party as an ongoing relationship makes previously issued commercial
  orders with that party inaccessible or removes their matching history.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Issue and complete a commercial order with an outside party, then deactivate that party as an
  ongoing relationship, and inspect whether the completed order's record remains accessible.
```
