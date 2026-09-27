# GMVQ MODULE-SPECIFIC QUESTION BANK

Document ID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-GMVQ-MVQ-V1.00-DRAFT
Group: G06 MANUFACTURING
Module Metadata: mrp_subcontracting_dropshipping
Wave: W2
Author Cell: P13
Review Cell: PENDING
Status: DRAFT / AUTHORING COMPLETE / NOT FROZEN
actual_mvq_count: 48
Purpose: Module-specific research questions (MVQ) for the blind two-lane ROOM A study of
  mrp_subcontracting_dropshipping. Answered independently by Lane A (source reading) and Lane B
  (runtime observation only) and compared cell-to-cell by the Reconciler under MODULE + QID.
Control: Authored under GMVQ_AUTHORING_STANDARD_V1.00.md and GMVQ_BRIDGE_MODULE_RULE_V1.00.md.
  Clean Room absolute - generic ERP business/behavioural concepts only, no vendor names and no
  technical identifiers. This bank governs seam behaviour only: what breaks when direct-to-customer
  delivery is attached to a subcontracted production event (the double absence of physical
  custody - the operator never made the item and never received it). Subcontracting's own
  invariants belong to mrp_subcontracting (cell P11); the ledger seam and the commercial-document
  seam belong to mrp_subcontracting_account / mrp_subcontracting_purchase (cell P12) and are out
  of scope here.

Note on cross-check: at authoring time no sibling bank existed on disk under
01_QUESTION_BANKS/G06_MANUFACTURING/ for mrp_subcontracting, mrp_subcontracting_account, or
mrp_subcontracting_purchase. The mandatory grep required by GMVQ_BRIDGE_MODULE_RULE_V1.00.md
Section 5 was run and returned no results because no sibling file exists yet, not because the
check was skipped. Overlap against those three siblings could not be verified against actual
authored text and should be re-checked once they exist on disk.

This bank produces DRAFT question content only. Not approved, not frozen, not verified. No merge,
release, STATE closure or gate approval is authorized by this document.

---

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q001
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When output is shipped directly from the external party to the end customer, the system
  does not fabricate an internal receipt event to represent stock the operator never
  physically held.
WHY_IT_MATTERS: >
  A fabricated receipt would overstate on-hand inventory and could mislead anyone relying
  on stock counts, valuation, or physical audit.
DISCONFIRMING_OBSERVATION: >
  An internal document marks the finished item as received into the operator's own stock
  location at a point when it is confirmed the item moved directly to the customer and
  never passed through operator custody.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A subcontracted production order exists whose finished item is routed to ship directly
  from the external party to the end customer, carried through to completion.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q002
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The system exposes a specific document or state that stands in for "received" when no
  physical receipt occurred, clearly distinguishable from a genuine physical receipt.
WHY_IT_MATTERS: >
  If the two are indistinguishable, no one downstream (finance, audit, customer service)
  can tell inferred custody from verified custody.
DISCONFIRMING_OBSERVATION: >
  A user or report cannot distinguish a direct-to-customer completion from an ordinary
  warehouse receipt using any field, status, or label the system exposes.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  One order completed via direct external-to-customer shipment and one comparable order
  completed via a normal warehouse receipt, viewed side by side.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q003
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The end customer's identity and delivery address are transmitted to the external party
  only through a controlled, logged channel, not silently embedded in a document the party
  sees for an unrelated purpose.
WHY_IT_MATTERS: >
  Uncontrolled disclosure of end-customer data to a third party is a commercial and
  data-handling exposure the operator did not choose to accept.
DISCONFIRMING_OBSERVATION: >
  The external party gains access to the customer's identifying details through a document
  or interface not intended to carry them, with no record of that disclosure.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  A subcontracted order with direct-to-customer delivery, reviewed for what information is
  issued to the external party during fulfillment.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q004
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The system provides a way to require or record a quality check before an externally
  produced item reaches the customer, even though the operator cannot physically inspect
  it.
WHY_IT_MATTERS: >
  With no inspection gate, defective output reaches the customer with no internal
  checkpoint at all, and the first the operator learns of a defect is a complaint.
DISCONFIRMING_OBSERVATION: >
  An order can be marked delivered to the customer with no quality-related field, step, or
  hold ever available or recorded, even optionally.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A subcontracted order routed for direct-to-customer delivery, walked from confirmation
  to completion.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q005
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the customer reports receiving less than ordered, the system supports recording
  that discrepancy against the original order even though the operator never counted the
  goods itself.
WHY_IT_MATTERS: >
  Without a way to log a customer-reported shortfall, there is no system record of the
  discrepancy or its resolution.
DISCONFIRMING_OBSERVATION: >
  A customer-reported quantity shortfall cannot be attached to the original order or
  production event anywhere in the system.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order for which the customer later disputes
  the quantity received.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q006
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A customer-reported wrong item can be linked back to the specific production order and
  external party responsible, not just to the sale.
WHY_IT_MATTERS: >
  Without that link, the operator cannot hold the correct party accountable or spot a
  pattern with a specific external partner.
DISCONFIRMING_OBSERVATION: >
  The system offers no path from a customer complaint about a wrong item back to the
  originating production order or external party.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order later flagged by the customer as the
  wrong item.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q007
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A defined return path exists for goods the customer wants to send back, even though
  those goods were never in the operator's own location.
WHY_IT_MATTERS: >
  Without a defined path, a return either becomes untrackable or is forced into a workflow
  built for goods that trace back to the operator's own stock.
DISCONFIRMING_OBSERVATION: >
  Attempting to process a return for a directly-shipped item requires forcing it through a
  workflow that assumes the goods are coming from the operator's own prior receipt.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order for which the customer initiates a
  return.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q008
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system records proof of delivery as externally sourced evidence, distinct in status
  from proof the operator captured itself.
WHY_IT_MATTERS: >
  Treating externally asserted proof as equivalent to operator-verified proof overstates
  the operator's certainty about what actually happened.
DISCONFIRMING_OBSERVATION: >
  Proof of delivery supplied by the external party is stored and displayed with no marker
  distinguishing it from evidence the operator captured directly.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order with delivery confirmation supplied
  by the external party.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q009
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A customer delivery document can legitimately exist for an order with no corresponding
  operator-side receipt document at all, by design, not as a data gap.
WHY_IT_MATTERS: >
  If the document chain assumes a receipt must precede delivery, direct-to-customer orders
  will either be blocked or will force a fabricated receipt to satisfy the sequence.
DISCONFIRMING_OBSERVATION: >
  The order cannot progress to a completed delivery state without a receipt document
  existing somewhere in the chain, forcing one to be created even without physical
  receipt.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A subcontracted order configured for direct-to-customer delivery, followed from
  confirmation through to customer delivery.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q010
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The quantity recorded as "produced" for a direct-to-customer subcontracted order is
  clearly marked as based on the external party's own report, not on any count the
  operator performed.
WHY_IT_MATTERS: >
  Presenting an unverified quantity as a factual count misstates the reliability of the
  number to anyone using it for planning or reconciliation.
DISCONFIRMING_OBSERVATION: >
  The recorded produced quantity is presented identically to a physically verified
  quantity, with nothing indicating it originates solely from the external party's own
  claim.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order, quantity field reviewed against its
  source.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q011
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling the customer's order after the external party has already shipped directly to
  the customer produces a distinct, flagged exception state rather than a silent
  cancellation.
WHY_IT_MATTERS: >
  A silent cancellation would leave goods in the customer's hands with no order to account
  for them, and no signal that reconciliation is needed.
DISCONFIRMING_OBSERVATION: >
  The customer order cancels cleanly with no warning, flag, or exception raised, despite
  the external party's shipment already being recorded as sent.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  A direct-to-customer subcontracted order where the external shipment is recorded as
  sent, then the customer order is cancelled.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q012
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A single production output can be split so that part returns to the operator's own stock
  and part ships directly onward to the customer, with both portions separately
  traceable.
WHY_IT_MATTERS: >
  Without a clean split, mixed fulfillment either loses traceability on one portion or
  forces the whole batch into a single fulfillment path it doesn't fit.
DISCONFIRMING_OBSERVATION: >
  Attempting a split fulfillment forces the entire output quantity into one path (fully
  received or fully direct-shipped) with no way to represent a genuine partial split.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A subcontracted production order whose output quantity is intended to be divided between
  operator stock and direct customer delivery.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q013
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Components sent to the external party are recorded as consumed based on a defined
  trigger point, not at an arbitrary or inconsistent moment relative to the direct
  shipment event.
WHY_IT_MATTERS: >
  Inconsistent timing of consumption would misstate on-hand component stock and misalign
  cost recognition with the actual production event.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical direct-to-customer orders show component consumption recorded at
  two different relative points in the flow with no configuration difference to explain
  it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Two comparable direct-to-customer subcontracted orders processed through to completion,
  component consumption timing compared.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q014
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  While components sit at the external party awaiting use in a direct-to-customer order,
  the system still records the operator as their owner until the defined consumption or
  shipment point.
WHY_IT_MATTERS: >
  Losing ownership tracking on components at a third-party site removes the basis for any
  claim if they are lost, damaged, or misused before the finished item ships.
DISCONFIRMING_OBSERVATION: >
  Components sent to the external party for a direct-to-customer order drop out of any
  ownership-tracked state before the defined consumption or shipment point is reached.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Components issued to an external party for a subcontracted order routed for
  direct-to-customer delivery, ownership status checked while work is in progress.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q015
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Finished goods that ship directly to the customer still pass through the operator's own
  valuation logic at the defined event point, even without ever occupying a physical
  location.
WHY_IT_MATTERS: >
  Skipping valuation entirely would leave the cost of goods sold unrecorded or recorded
  through an inconsistent path for these orders.
DISCONFIRMING_OBSERVATION: >
  A completed direct-to-customer order shows no valuation entry at all for the finished
  item, where a comparable warehouse-received order does.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order compared against a comparable
  warehouse-received order for the same item.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q016
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a shipment confirmation from the external party and a customer cancellation are
  processed within a short window of each other, the system resolves them deterministically
  rather than by whichever happens to be processed first.
WHY_IT_MATTERS: >
  A race-dependent outcome means the same real-world situation could be recorded two
  different ways depending on timing alone.
DISCONFIRMING_OBSERVATION: >
  Processing the two events in reverse order produces a different final state for the
  order than processing them in the original order, with no reconciling step.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  A direct-to-customer subcontracted order with both a shipment confirmation and a
  cancellation request pending at nearly the same time.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q017
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A full lot or serial trace can be produced for a direct-to-customer order even though the
  item never entered the operator's own warehouse.
WHY_IT_MATTERS: >
  A broken trace on these orders creates a blind spot precisely where recall or quality
  investigation would need it most.
DISCONFIRMING_OBSERVATION: >
  Running a trace on a direct-to-customer order's finished item returns an incomplete
  chain that stops at the external party with no link forward to the customer, or vice
  versa.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order for a lot- or serial-tracked item.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q018
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The handoff of order and customer information to the external party exposes only that
  one operator's data, with no channel through which another tenant's data could appear.
WHY_IT_MATTERS: >
  A cross-tenant leak during a third-party handoff is a severe breach of the isolation the
  platform is expected to guarantee.
DISCONFIRMING_OBSERVATION: >
  Information belonging to a different tenant appears anywhere in the documents or
  interface exposed to the external party during a direct-to-customer handoff.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Two separate tenants each with a direct-to-customer subcontracted order routed through
  the same external party.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q019
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Only a defined, permission-checked role can record a direct-to-customer delivery as
  complete on the external party's behalf.
WHY_IT_MATTERS: >
  If any user can mark such a delivery complete, the completion event carries no assurance
  it reflects anything the external party actually did.
DISCONFIRMING_OBSERVATION: >
  A user without any role tied to fulfillment or external-party confirmation is able to
  mark the direct-to-customer delivery complete.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  A direct-to-customer subcontracted order awaiting a delivery-complete confirmation,
  attempted by users with different role assignments.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q020
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The audit trail for a direct-to-customer delivery records it as a distinct event type
  from an ordinary warehouse delivery, not merely reusing the same log entry shape.
WHY_IT_MATTERS: >
  Without a distinguishing trail, later audit or investigation cannot separate the two
  custody histories.
DISCONFIRMING_OBSERVATION: >
  The audit log entries for a direct-to-customer delivery and an ordinary warehouse
  delivery are identical in content and cannot be told apart.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  One completed direct-to-customer order and one completed ordinary order, audit trails
  compared.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q021
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing the setting that allows direct-to-customer routing for subcontracted output
  does not alter the fulfillment path of an order already in progress under the prior
  setting.
WHY_IT_MATTERS: >
  A retroactive change to in-flight orders when a setting is toggled could silently
  redirect goods or documents in a way no one authorized for that specific order.
DISCONFIRMING_OBSERVATION: >
  Toggling the setting changes the expected fulfillment path of an order that was already
  confirmed under the previous setting.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  A direct-to-customer subcontracted order confirmed while the setting is enabled, then
  the setting is disabled before the order completes.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q022
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system provides no automated check on the delivery address used by the external
  party beyond what was captured on the original customer order.
WHY_IT_MATTERS: >
  Knowing this is a manual-only control tells the operator exactly where their exposure
  lies and that no system safeguard should be assumed.
DISCONFIRMING_OBSERVATION: >
  The system is found to perform some automated validation or alert on the delivery
  address used for external fulfillment that was not otherwise documented.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A direct-to-customer subcontracted order with a delivery address reviewed against what
  is passed to the external party.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q023
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A direct-to-customer order that is short-shipped by the external party leaves a
  trackable remaining balance rather than being closed as fully satisfied.
WHY_IT_MATTERS: >
  Silently closing a short-shipped order as complete would understate what the customer is
  still owed.
DISCONFIRMING_OBSERVATION: >
  A short-shipped direct-to-customer order is marked fully complete with no remaining
  balance recorded anywhere.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A direct-to-customer subcontracted order where the external party ships less than the
  full ordered quantity.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q024
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reversing a completed direct-to-customer delivery restores the components already
  marked consumed to a defined state rather than leaving them permanently consumed
  against a delivery that no longer stands.
WHY_IT_MATTERS: >
  Components left consumed against a reversed delivery would misstate both inventory and
  cost with no path to correct it.
DISCONFIRMING_OBSERVATION: >
  Reversing the completed delivery leaves the consumed components with no available
  action to restore or reconcile their state.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order later reversed or corrected.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q025
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a customer order is cancelled after components were already sent to the external
  party but before shipment, the components-sent record moves into a defined follow-up
  state rather than being left indefinitely open.
WHY_IT_MATTERS: >
  An indefinitely open record with no resolution path hides real exposure (components at a
  third party with no destination) inside normal-looking data.
DISCONFIRMING_OBSERVATION: >
  The components-sent record for the cancelled order remains in its original in-progress
  state with no flag, follow-up state, or required action ever appearing.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A direct-to-customer subcontracted order cancelled after components were sent to the
  external party but before the external party shipped.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q026
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Commercial terms the operator has with the end customer (price, discount, contract
  terms) are not included in any document or interface exposed to the external party for
  fulfillment.
WHY_IT_MATTERS: >
  Exposing the operator's customer pricing to a subcontracted party could undermine the
  operator's commercial position.
DISCONFIRMING_OBSERVATION: >
  A price, discount, or contract term specific to the end customer appears in a document or
  interface the external party can see.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  A direct-to-customer subcontracted order reviewed for the content of documents issued to
  the external party.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q027
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The direct-to-customer fulfillment path for subcontracted output is reachable through
  the standard order-to-delivery flow without requiring an undocumented manual override.
WHY_IT_MATTERS: >
  If the path only works through an unofficial workaround, its actual behavior in daily
  use may not match what any specification describes.
DISCONFIRMING_OBSERVATION: >
  Completing a direct-to-customer subcontracted order requires a manual step or workaround
  outside the documented standard flow.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  A subcontracted order configured for direct-to-customer delivery, processed using only
  the standard flow with no manual intervention.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q028
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Any documented quality-hold or inspection step in the general fulfillment process is
  either genuinely enforced for direct-to-customer orders or explicitly documented as not
  applicable to them.
WHY_IT_MATTERS: >
  A silent gap between documented process and actual runtime behavior on this path would
  mean quality controls exist on paper only for the riskiest fulfillment type.
DISCONFIRMING_OBSERVATION: >
  A quality-hold or inspection step described for standard fulfillment is skipped entirely
  for a direct-to-customer order with no configuration or documentation explaining the
  difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A direct-to-customer subcontracted order compared against documented fulfillment process
  steps.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q029
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the external party's shipment never actually occurs despite being reported, the
  system retains enough independent evidence to distinguish that from a normal delay.
WHY_IT_MATTERS: >
  Without independent evidence, an operator cannot tell a lost shipment from a slow one,
  delaying any recovery action.
DISCONFIRMING_OBSERVATION: >
  There is no observable difference in the system between a shipment that is merely
  delayed and one that never occurred at all, beyond elapsed time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A direct-to-customer subcontracted order where the external party's reported shipment
  does not arrive within the expected window.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q030
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If a general rule elsewhere requires an item to be received before it can be delivered,
  the direct-to-customer path's exemption from that rule is an explicit, visible
  configuration rather than an undocumented special case.
WHY_IT_MATTERS: >
  An undocumented exemption from a core sequencing rule is exactly the kind of gap that
  later gets treated as a defect rather than a known design choice.
DISCONFIRMING_OBSERVATION: >
  The exemption for direct-to-customer orders cannot be located in any configuration or
  setting, only inferred from the fact that the flow happens to work.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  A direct-to-customer subcontracted order compared against the general
  receive-before-deliver rule applied elsewhere in fulfillment.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q031
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A return authorization created for a direct-to-customer order is routed toward a defined
  destination (operator or external party) by rule, not left for a person to decide case
  by case with no guidance.
WHY_IT_MATTERS: >
  Undefined routing means returns for this order type are handled inconsistently, with no
  predictable disposition.
DISCONFIRMING_OBSERVATION: >
  Creating a return for a direct-to-customer order gives no indication of where the goods
  should go, leaving the destination entirely to the handling person's own judgment.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order for which a return is initiated.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q032
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Customer invoicing for a direct-to-customer order is keyed to a defined trigger
  appropriate to that flow, not to a receipt event that never occurs for it.
WHY_IT_MATTERS: >
  If invoicing depends on a receipt event that never happens, these orders could never be
  billed, or could be billed through an inconsistent workaround.
DISCONFIRMING_OBSERVATION: >
  A direct-to-customer order cannot be invoiced through the standard flow because the
  trigger it depends on is a receipt event that never occurs for this order type.
EXPECTED_SURFACE: S2
PRECONDITIONS: >
  A direct-to-customer subcontracted order carried through to the point where customer
  invoicing would normally occur.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q033
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Given a production order with several direct-to-customer deliveries drawn from it, the
  system can show which customer received which portion of the output.
WHY_IT_MATTERS: >
  Without this, a quality issue traced to a production order cannot be followed through to
  the specific customers affected.
DISCONFIRMING_OBSERVATION: >
  The system can show that a production order fed several direct-to-customer deliveries
  but cannot show which customer received which specific portion.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  A subcontracted production order whose output was split across more than one
  direct-to-customer delivery.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q034
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A direct-to-customer order's status field moves through each defined intermediate state
  in order and cannot jump from an early state directly to fully delivered.
WHY_IT_MATTERS: >
  Skipped states would hide the fact that an expected checkpoint (such as shipment
  confirmation) was never actually recorded.
DISCONFIRMING_OBSERVATION: >
  The order's status advances directly from an early state to fully delivered with an
  intermediate state never recorded at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A direct-to-customer subcontracted order tracked through each status change from
  confirmation to completion.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q035
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If the external party's association with a particular company or legal entity changes
  while a direct-to-customer order is in progress, the order retains the entity context it
  started under.
WHY_IT_MATTERS: >
  A mid-flow change in company context could misattribute the transaction to the wrong
  legal entity's books.
DISCONFIRMING_OBSERVATION: >
  The order's recorded company or entity context changes partway through processing to
  match a change made to the external party's own record, without an explicit transaction
  to justify it.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  A direct-to-customer subcontracted order in progress while the external party's company
  or entity association is changed.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q036
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The operator can configure a requirement for documentary evidence of the item's
  condition from the external party before a direct-to-customer delivery is marked
  complete.
WHY_IT_MATTERS: >
  Without this option, the operator has no system-enforced way to reduce the risk of
  shipping a defective item sight-unseen.
DISCONFIRMING_OBSERVATION: >
  No configuration exists anywhere that can require documentary evidence before
  completion, even as an optional setting.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  A direct-to-customer subcontracted order type reviewed for available configuration
  options ahead of completion.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q037
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The customer delivery for a direct-to-customer order cannot be marked complete while the
  underlying production order is still open.
WHY_IT_MATTERS: >
  Allowing delivery to close ahead of production would let the system assert a customer
  received something not yet confirmed as produced.
DISCONFIRMING_OBSERVATION: >
  The customer delivery is successfully marked complete while the underlying production
  order remains open.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A direct-to-customer subcontracted order with its production order deliberately left
  open, delivery completion attempted.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q038
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling a direct-to-customer order after components were sent to the external party
  but before the party has shipped produces a clear recovery instruction for those
  components.
WHY_IT_MATTERS: >
  With no recovery instruction, components at a third party become effectively untracked
  exposure with no assigned next step.
DISCONFIRMING_OBSERVATION: >
  Cancelling at this point leaves the components-sent record with no recovery action,
  reminder, or instruction of any kind.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A direct-to-customer subcontracted order cancelled after components were sent but before
  the external party ships.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q039
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A direct-to-customer order's finished item is never simultaneously counted as both
  received into operator stock and delivered to the customer.
WHY_IT_MATTERS: >
  A transient double count would overstate on-hand inventory at the exact moment stock
  figures might be checked or reported.
DISCONFIRMING_OBSERVATION: >
  At some point during processing, the same finished-item quantity appears counted as both
  on-hand received stock and as delivered to the customer.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A direct-to-customer subcontracted order tracked closely through its transaction
  sequence for a brief window around completion.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q040
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A customer's outright refusal of a direct-to-customer delivery is recorded as a distinct
  outcome, not folded into an ordinary successful-delivery record.
WHY_IT_MATTERS: >
  Recording a refusal as a success would hide a fulfillment failure from anyone reviewing
  delivery performance.
DISCONFIRMING_OBSERVATION: >
  There is no way to record a full customer refusal separately from a normal successful
  delivery.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A direct-to-customer subcontracted order where the customer refuses the delivery
  entirely.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q041
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external party, not the operator, physically applies a serial or lot
  identifier, the system still records that identifier as authoritative for later trace
  and warranty purposes.
WHY_IT_MATTERS: >
  If the externally applied identifier isn't captured, any later trace or warranty lookup
  for that unit has no starting point.
DISCONFIRMING_OBSERVATION: >
  The identifier the external party applied to the physical unit is never captured
  anywhere in the system record for that order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A direct-to-customer subcontracted order for a lot- or serial-tracked item where the
  external party applies the identifier.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q042
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An order created before the routing rule enabling direct-to-customer fulfillment existed
  is not silently reinterpreted as eligible for that path once the rule is added.
WHY_IT_MATTERS: >
  Retroactively reinterpreting an older order under a newly added rule could apply a
  fulfillment path no one intended for it at the time it was created.
DISCONFIRMING_OBSERVATION: >
  An order created before the routing rule existed becomes eligible for direct-to-customer
  fulfillment once the rule is added, without anyone re-confirming that order.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  An order created before any direct-to-customer routing rule exists, followed by that
  rule being introduced.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q043
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A single subcontracted production order can be represented with part of its output
  received into operator stock and part routed direct-to-customer, without requiring the
  order itself to be split into two separate records.
WHY_IT_MATTERS: >
  If it cannot be represented on one order, an artificial second order has to be created
  just to model something that is really one production event.
DISCONFIRMING_OBSERVATION: >
  Representing a partial receipt and a partial direct-to-customer shipment from the same
  production event requires creating a second, artificial production order.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A subcontracted production order whose output is intended to be split between operator
  stock and direct customer delivery.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q044
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Redirecting a direct-to-customer shipment already reported as sent requires a defined
  role's authorization, not any user with order access.
WHY_IT_MATTERS: >
  Unrestricted rerouting authority over goods already in transit to a customer creates an
  avoidable diversion risk.
DISCONFIRMING_OBSERVATION: >
  A user with only general order-viewing access, and no fulfillment or exception-handling
  role, can successfully redirect an in-transit shipment.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  A direct-to-customer subcontracted order already reported as shipped, redirection
  attempted by users with different role assignments.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q045
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A single subcontracted production batch can be represented as fulfilling more than one
  customer's direct-to-customer order by quantity, each portion separately traceable.
WHY_IT_MATTERS: >
  Without this, batches produced to fill several small customer orders at once cannot be
  modeled accurately, forcing artificial single-customer batches.
DISCONFIRMING_OBSERVATION: >
  A single production batch cannot be split across more than one customer's
  direct-to-customer order without merging their records or losing the separate
  traceability.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  A subcontracted production order whose output is intended to satisfy more than one
  customer's direct-to-customer order.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q046
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The date used for customer revenue recognition on a direct-to-customer order is a date
  the operator can independently corroborate, not solely a date self-reported by the
  external party.
WHY_IT_MATTERS: >
  Revenue timing based entirely on an unverifiable third-party claim is a control weakness
  in period-close and financial reporting.
DISCONFIRMING_OBSERVATION: >
  The only date available to drive revenue recognition on the order is one entered by or
  sourced entirely from the external party's own report, with no independent corroborating
  event.
EXPECTED_SURFACE: S2,S6
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order reviewed for which date drives
  revenue recognition.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q047
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the external party's claimed shipped quantity and the customer's claimed received
  quantity disagree, the system records both figures rather than silently adopting one as
  fact.
WHY_IT_MATTERS: >
  Silently picking one figure over the other hides a genuine discrepancy that someone
  needs to resolve.
DISCONFIRMING_OBSERVATION: >
  Only one of the two conflicting quantities can be recorded in the system at all, with no
  way to capture that a discrepancy exists.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A direct-to-customer subcontracted order where the external party's reported shipped
  quantity differs from the customer's reported received quantity.
```

```yaml
QID: G06-MRP_SUBCONTRACTING_DROPSHIPPING-Q048
MODULE: mrp_subcontracting_dropshipping
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  For a direct-to-customer order, some record distinguishable from the sales transaction
  itself exists to show that a production event, not just a sale, occurred.
WHY_IT_MATTERS: >
  If the only evidence of production is the existence of the sale, then a fabricated or
  mistaken sale would be indistinguishable from an actual completed production event.
DISCONFIRMING_OBSERVATION: >
  The only trace of the production event for a direct-to-customer order is the sales
  record itself, with no separate production-side evidence findable anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  A completed direct-to-customer subcontracted order reviewed for what evidence of the
  production event exists independent of the sale.
```
