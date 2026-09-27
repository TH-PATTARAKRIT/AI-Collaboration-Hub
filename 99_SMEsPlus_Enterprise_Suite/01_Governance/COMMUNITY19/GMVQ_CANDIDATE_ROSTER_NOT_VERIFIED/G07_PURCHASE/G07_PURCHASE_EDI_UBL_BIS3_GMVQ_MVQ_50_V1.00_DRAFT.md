# SMEsPlus ENTERPRISE SUITE
## GMVQ — G07 PURCHASE / purchase_edi_ubl_bis3 Module Adversarial MVQ Bank

**Document ID:** GMVQ-G07-PURCHASE_EDI_UBL_BIS3-MVQ50-V1.00
**Group:** G07 PURCHASE
**Module Metadata:** `purchase_edi_ubl_bis3`
**Wave:** W2
**Author Cell:** P17 (GMVQ Question Factory — Internal Production Team 17, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50

## Purpose

`purchase_edi_ubl_bis3` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Its seam is the order and its
documents exchanged as structured messages with a counterparty — generation, transmission, and receipt of a
counterparty's own documents. Per the Bridge Module Rule, every question in this bank was tested against the
seam question: "if this capability were removed and the order and the exchange mechanism were used entirely
apart, would the question still make sense?" A YES answer means the question belongs to the base `purchase`
bank, not here, and was cut. Every question below is a NO — it fails only at the seam between the internal order
and what actually moves to and from the counterparty as a structured document.

The module's metadata name carries standards-body tokens (the exchange standard family and its profile). Per
the Group Brief and the Authoring Standard's clean-room rule, that name appears in the `MODULE:` field only.
Question text refers throughout to "the structured document exchange," "the exchanged document," or "the
counterparty's system" — never to the standard, the profile, or any technical identifier.

## Control

- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$DIR"/*.md | sort` was run before
  writing a single question. At the time of authoring, the only sibling bank on disk in this group was the BASE
  module bank `G07_PURCHASE_GMVQ_MVQ_62_V1.00_DRAFT.md` (Author Cell P14). Its 62 hypotheses were read in full;
  they cover order confirmation and post-confirmation change, quantity ordered/received/billed and tolerance,
  price and tax timing, three-way match and receipt/bill exceptions, and approval/segregation of duties — all of
  it about the ORDER'S OWN lifecycle, none of it about the structured exchange of that order or its documents
  with a counterparty. No overlap was found, and no question in this bank restates any of that bank's ground
  with a noun swapped. No other sibling bridge banks (`purchase_stock`, `purchase_mrp`,
  `purchase_product_matrix`, `purchase_repair`) existed on disk at authoring time to check against; this bank
  does not touch stock movement, production demand, attribute-grid entry, or repair-driven procurement, so no
  collision with those grounds is expected, but that has not been independently verified against their banks
  because they do not yet exist.
- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong, and the
  disconfirming observation is a distinct event for every question — no two questions share one failure event.
- No padding: 50 questions exist because they test 50 distinct material hypotheses at the seam, spread across
  ordering, partiality, ownership, timing, reversal, quantity-and-money, lifecycle mismatch, error asymmetry,
  and authority (Bridge Module Rule §3), and across the Authoring Standard's dimension list (business rule,
  state transition, configuration dependency, role/permission, exception path, cross-module dependency,
  auditability, tenant/company boundary, concurrency, runtime/configuration reachability).
- This module carries one layer at the seam; the `LAYER` field is omitted throughout.
- Clean-room compliance: no vendor or product name, no technical identifier (model, table, field, method, XML
  ID, API path, standard or profile name), and no implementation shape appears anywhere in question text.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a Research
  Evidence Join Key only; no Formal Coverage is derived from this bank. Lane A / Lane B: NOT STARTED for this
  module until rolling batch freeze is recorded.
- Coverage map: post-transmission edit divergence Q001-Q004 · duplicate/retry transmission Q005-Q008 ·
  counterparty rejection after internal confirmation Q009-Q012 · inbound document matching none/two orders
  Q013-Q017 · mandatory-element gaps and blocked/degraded send Q018-Q021 · cross-reference identifier mismatch
  Q022-Q025 · rounding/unit/currency representation divergence Q026-Q029 · transport-accepted but
  counterparty-system-rejected later Q030-Q033 · legal status of exchanged document versus internal record
  Q034-Q036 · retention and reproducibility Q037-Q040 · per-company sender identity Q041-Q043 · outage
  mid-exchange ambiguity Q044-Q047 · concurrency, atomicity, and per-company channel boundary Q048-Q050.

## G07-PURCHASE_EDI_UBL_BIS3-Q001

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q001
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once the order's content has been sent as a structured document to the counterparty, editing the order
  afterward does not retroactively alter what is recorded as having been sent; the transmitted content and the
  current order content are held as two distinct, independently inspectable facts.
WHY_IT_MATTERS: >
  If the sent record can be silently overwritten by a later edit, no one can ever prove what the counterparty
  actually saw, which defeats the exchange's evidentiary purpose.
DISCONFIRMING_OBSERVATION: >
  Editing a field on the order after transmission causes the previously recorded transmitted content to display
  the new value instead of the value that was actually sent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send an order as a structured document, note a specific field's transmitted value, then edit that field on the
  order, and re-inspect the transmitted record.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q002

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q002
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the order is edited after transmission, the system distinguishes between "amended and a corrected
  document sent" and "changed internally but not yet communicated," presenting the two states differently to a
  user working the order.
WHY_IT_MATTERS: >
  A user who cannot tell the two apart may treat an uncommunicated change as if the counterparty already knows
  about it, causing the counterparty to act on stale terms.
DISCONFIRMING_OBSERVATION: >
  After an internal-only edit with no re-send, the order's presentation gives no indication that the
  counterparty's copy is now out of date.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Edit a transmitted order without triggering a re-send, and inspect how that state is surfaced.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q003

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q003
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  There is a single designated authoritative value used for downstream matching (receipt, billing) when the
  current order content and the last-transmitted content disagree and no correction has been communicated,
  rather than each downstream process picking whichever value it happens to read first.
WHY_IT_MATTERS: >
  Two downstream processes silently using different values for the same disagreement produces inconsistent
  matching results that are hard to trace back to a cause.
DISCONFIRMING_OBSERVATION: >
  A receiving action and a billing action, triggered from the same diverged order, are found to have used
  different values for the same disputed field.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a divergence between current order content and last-transmitted content, then separately trigger a
  receiving action and a billing-matching action and compare which value each used.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q004

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q004
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an edit after transmission is permitted outright, requires a fresh confirmation step, or is blocked
  until a correction is transmitted, is a defined and consistent behavior rather than varying by which field is
  edited.
WHY_IT_MATTERS: >
  Inconsistent edit-permission behavior after transmission is a governance gap that lets sensitive terms bypass
  the same control that protects everything else.
DISCONFIRMING_OBSERVATION: >
  Two comparably significant fields (for example quantity and delivery commitment) are found to have different
  edit-after-transmission rules with no documented reason.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt post-transmission edits on several different fields of comparable business significance and compare
  which are blocked, warned, or silently allowed.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q005

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q005
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Sending the same order content to the counterparty a second time, with nothing having changed, is recognizable
  afterward as a duplicate transmission rather than appearing as two unrelated, independent exchanges.
WHY_IT_MATTERS: >
  An unrecognized duplicate can cause the counterparty to act twice on a single commitment, doubling a delivery,
  a payment expectation, or a dispute.
DISCONFIRMING_OBSERVATION: >
  Two identical transmissions of the same order content leave no trace distinguishing them as related; each
  looks like a first-time, independent exchange.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger transmission twice for an order whose content has not changed in between, and inspect the resulting
  records for a duplicate indicator.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q006

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q006
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Triggering a second transmission after the order has changed produces a document that is identifiable as a
  correction or amendment of the earlier one, not an unrelated new document with no link back.
WHY_IT_MATTERS: >
  Without a link between versions, the counterparty and any later audit cannot reconstruct which document
  superseded which.
DISCONFIRMING_OBSERVATION: >
  A second transmission after a change carries no reference, in the exchanged content or the retained record,
  back to the document it supersedes.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transmit an order, change it, transmit again, and inspect whether the second document references the first.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q007

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q007
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A retry after a failed or uncertain transmission attempt does not produce a second live transmission if the
  first attempt actually succeeded; the system distinguishes "resend because it failed" from "resend that
  duplicates a success."
WHY_IT_MATTERS: >
  Blind retries after network uncertainty are a primary real-world cause of counterparties receiving the same
  commitment twice.
DISCONFIRMING_OBSERVATION: >
  Retrying after an attempt whose outcome was actually a success, but was not confirmed back to the user in
  time, results in the counterparty receiving two live copies with no de-duplication.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Simulate an acknowledgement delay or loss immediately after a successful send, trigger a manual or automatic
  retry, and determine whether de-duplication occurs.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q008

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q008
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The point at which the order becomes locked against casual further change, if such a lock exists, is tied to a
  transmission actually occurring, not merely to a user opening or previewing the document to be sent.
WHY_IT_MATTERS: >
  Locking on preview rather than actual transmission would block legitimate work for no real exchange event, or
  conversely locking too late would allow changes mid-transmission.
DISCONFIRMING_OBSERVATION: >
  Merely previewing or generating the document without sending it applies the same restriction on further
  editing as an actual transmission would.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Generate or preview the document without completing a send, and attempt to edit the order.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q009

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q009
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rejection notice received from the counterparty after the order was already confirmed internally is
  recorded as an event on the order and is visible to whoever manages it, rather than being consumed silently by
  the exchange mechanism with no trace on the order itself.
WHY_IT_MATTERS: >
  An invisible rejection leaves the business team believing a commitment is live when the counterparty has
  already refused it.
DISCONFIRMING_OBSERVATION: >
  A received rejection notice does not appear anywhere on the order record a business user would normally check.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Simulate a counterparty rejection of a transmitted document for an order already confirmed internally, then
  inspect the order for any visible indication.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q010

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q010
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rejection does not automatically revert the internal confirmation state without a deliberate decision; the
  internal and external states can legitimately disagree for a period while someone decides what to do.
WHY_IT_MATTERS: >
  Automatically unwinding an internal confirmation the moment a rejection arrives could cascade into premature
  reversal of receiving or billing steps already begun on the strength of that confirmation.
DISCONFIRMING_OBSERVATION: >
  Receiving a rejection notice immediately and automatically changes the order's internal confirmation state
  with no intervening decision point.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Simulate a rejection on a confirmed order and observe whether the internal confirmation state changes
  unattended.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q011

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q011
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whoever is authorized to act on a rejection (resubmit, cancel, escalate) is defined, and is not simply whoever
  happens to be looking at the order when the rejection notice arrives.
WHY_IT_MATTERS: >
  An undefined authority boundary on rejection handling means a rejection can sit unattended, or be resolved by
  someone without the standing to decide it.
DISCONFIRMING_OBSERVATION: >
  No role or permission distinction exists between viewing a rejection notice and acting on it (resubmitting or
  cancelling).
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Compare the permission required to view a rejection notice against the permission required to act on it.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q012

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q012
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rejection arriving after part of the goods movement or billing tied to the order has already proceeded is
  flagged as a higher-consequence case than a rejection on an order with nothing yet done against it, rather
  than being handled identically.
WHY_IT_MATTERS: >
  Treating a clean rejection and a rejection-after-partial-execution the same way hides the cases that actually
  need urgent attention.
DISCONFIRMING_OBSERVATION: >
  A rejection on an order with completed partial receipt or billing produces exactly the same notification and
  handling path as a rejection on an order with no activity yet.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Simulate a rejection on two otherwise similar orders, one with partial receipt/billing already recorded and
  one without, and compare the resulting handling.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q013

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q013
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An inbound structured document that cannot be matched to exactly one open order is held in a distinct, visible
  unresolved state rather than being silently discarded or forced onto the nearest-looking order.
WHY_IT_MATTERS: >
  Silent discarding loses a real transaction; forcing a mismatch onto the wrong order corrupts that order's
  record.
DISCONFIRMING_OBSERVATION: >
  An inbound document with no matching open order, or with a match to more than one, is auto-attached to a
  guessed order with no flag, or disappears with no retained trace.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit an inbound document referencing an order identifier that does not exist, and separately one that
  ambiguously matches two open orders, and inspect the outcome of each.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q014

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q014
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The criteria used to attempt a match (the cross-reference identifier, not incidental similarity such as
  counterparty and rough amount) are fixed and documented, not a best-effort heuristic that can attach a document
  to the wrong order under coincidental similarity.
WHY_IT_MATTERS: >
  A heuristic match on incidental similarity can silently misattach a real financial document to the wrong
  commercial transaction.
DISCONFIRMING_OBSERVATION: >
  Two genuinely unrelated orders that happen to share a similar amount and the same counterparty cause an
  inbound document to be offered as a plausible match to the wrong one.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create two unrelated orders with the same counterparty and similar amounts, then submit an inbound document
  intended for only one, and observe the matching candidates offered.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q015

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q015
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Resolving an ambiguous or unmatched inbound document (choosing which order it belongs to, or rejecting it)
  requires a level of authorization distinct from ordinary order data entry.
WHY_IT_MATTERS: >
  Letting anyone silently attach an unresolved financial document to whichever order they choose is a control
  gap in the matching process.
DISCONFIRMING_OBSERVATION: >
  Any user able to view orders can resolve an ambiguous inbound-document match with no additional permission
  check.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Compare the permission needed for ordinary order viewing against the permission needed to resolve an ambiguous
  inbound-document match.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q016

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q016
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An inbound document rejected because it cannot be matched is retained with its content intact for later
  reprocessing, rather than being dropped once rejected.
WHY_IT_MATTERS: >
  If an unmatched document is dropped, the transaction it represents may be permanently lost to the record even
  after the matching order is later created or corrected.
DISCONFIRMING_OBSERVATION: >
  An inbound document that failed matching is not retrievable in its original form after the immediate
  processing attempt.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit an unmatched inbound document, let the match fail, then attempt to retrieve and reprocess the original
  content later.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q017

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q017
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two inbound documents that both plausibly match the same single open order are not both silently applied to
  it; applying a second one to an order that already absorbed one candidate is blocked or flagged.
WHY_IT_MATTERS: >
  Applying two colliding documents to one order can double-count a commitment that was only ever a single
  transaction.
DISCONFIRMING_OBSERVATION: >
  A second inbound document is applied to the same order that already absorbed an earlier ambiguous match, with
  no warning that this is a repeat application.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit two separate inbound documents that could each plausibly match the same order, resolve the first, then
  attempt to resolve the second onto the same order.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q018

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q018
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An attempt to transmit a document for which the underlying master data cannot supply a mandatory element is
  blocked before transmission rather than sent with the element blank, defaulted, or fabricated.
WHY_IT_MATTERS: >
  Sending a document with a fabricated or blank mandatory element to satisfy the format can create a legally
  exchanged document that misstates the transaction.
DISCONFIRMING_OBSERVATION: >
  A document is successfully transmitted despite a mandatory element having no real source value, with the gap
  filled by a default, blank, or placeholder value.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Remove or leave unset a master-data value that feeds a mandatory element, then attempt to transmit the
  associated order.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q019

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q019
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a send is blocked for a missing mandatory element, the person responsible for the order is told
  specifically which element is missing and where it should come from, not given a generic failure.
WHY_IT_MATTERS: >
  A generic failure with no specific cause forces manual investigation every time and delays legitimate
  exchanges.
DISCONFIRMING_OBSERVATION: >
  A blocked send due to a missing mandatory element produces only a generic error with no indication of which
  element or which master-data source is the gap.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Trigger a blocked send due to a missing mandatory element and inspect the message given to the user.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q020

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q020
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a missing non-critical element degrades the send (sent with a warning) versus a missing critical
  element blocks it outright is a defined, consistent distinction, not decided ad hoc per element.
WHY_IT_MATTERS: >
  An undefined line between "block" and "degrade but send" produces inconsistent behavior that no one can
  predict or rely on.
DISCONFIRMING_OBSERVATION: >
  Two elements of comparable declared importance are found to have different block-versus-degrade behavior with
  no documented rule explaining the difference.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Identify two comparably important elements fed from master data, remove each in turn, and compare whether the
  send blocks or degrades.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q021

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q021
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A degraded send (sent despite a non-critical gap) leaves a retained record that it was degraded and why, not
  just the resulting document with no memory of the compromise made.
WHY_IT_MATTERS: >
  Without a retained record of a degraded send, no one can later explain why a document looks incomplete or why
  the counterparty raised a question about it.
DISCONFIRMING_OBSERVATION: >
  A document sent in degraded form leaves no trace, after the fact, that it was sent with a known gap rather than
  in its ordinary complete form.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Force a degraded send and then inspect whatever record is kept of that transmission afterward.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q022

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q022
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The identifier used to reference the order in exchanged documents with the counterparty is tracked as separate
  from whatever identifier is used to refer to the order internally, and a mapping between the two is maintained
  explicitly rather than inferred by matching on shape or pattern.
WHY_IT_MATTERS: >
  Relying on pattern-matching between two different identifier schemes is a systemic source of silent
  misattachment as either scheme evolves.
DISCONFIRMING_OBSERVATION: >
  The system has no explicit stored mapping between the counterparty-facing identifier and the internal one,
  relying instead on inferring the connection at the moment it is needed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Inspect how an inbound document's counterparty-side reference is connected back to the internal order and
  whether an explicit stored link exists.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q023

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q023
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the counterparty-facing identifier scheme changes (for example a new numbering agreed with that
  counterparty) mid-relationship, orders already referenced under the old scheme remain resolvable, rather than
  becoming orphaned.
WHY_IT_MATTERS: >
  A hard cut-over in identifier scheme that leaves old references unresolved breaks traceability for every
  transaction that predates the change.
DISCONFIRMING_OBSERVATION: >
  An inbound document referencing an order by the identifier scheme in effect at the time it was created fails
  to resolve after the scheme has since changed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Change the counterparty-facing identifier convention mid-relationship and then submit an inbound document
  referencing an order under the old convention.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q024

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q024
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two different orders are never assigned the same counterparty-facing identifier within the period that
  identifier remains meaningful to that counterparty.
WHY_IT_MATTERS: >
  A collision in the counterparty-facing identifier makes every downstream reference by the counterparty
  ambiguous between two unrelated transactions.
DISCONFIRMING_OBSERVATION: >
  Two distinct orders are found to carry, or to have carried within an overlapping active period, the same
  counterparty-facing identifier.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Generate counterparty-facing identifiers for a volume of orders in a short window and check for collisions.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q025

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q025
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the counterparty requires its own reference to be echoed back on related documents (for example their
  tender or agreement reference), that reference is carried through consistently across every document in the
  exchange rather than only on the first one.
WHY_IT_MATTERS: >
  Dropping the counterparty's own reference partway through an exchange breaks their ability to reconcile the
  sequence on their side.
DISCONFIRMING_OBSERVATION: >
  The counterparty's own reference, present on the first document exchanged, is missing from a later document
  in the same transaction sequence.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record a counterparty reference on the initial document and check whether it persists onto every subsequent
  related document.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q026

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q026
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A monetary amount represented in the exchanged document and the same amount as stored internally always agree
  to the last unit of currency; the exchanged form is never independently rounded in a way that can diverge from
  the stored value.
WHY_IT_MATTERS: >
  A silent rounding divergence between the exchanged and stored forms of the same amount is the beginning of a
  reconciliation gap that compounds across a long-running relationship.
DISCONFIRMING_OBSERVATION: >
  The total shown in the exchanged document differs from the internally stored total for the same order line by
  more than a documented, explicit rounding rule accounts for.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Choose an amount that exercises a rounding edge case and compare its representation in the exchanged document
  against the internally stored value.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q027

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q027
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A unit of measure used internally that has no direct equivalent in the exchange standard's permitted unit
  codes is either converted using a documented, consistent conversion or blocks the send; it is never sent with
  a silently wrong or approximate unit code.
WHY_IT_MATTERS: >
  An exchanged document asserting the wrong unit of measure changes the actual meaning of a quantity, which the
  counterparty has no way to detect.
DISCONFIRMING_OBSERVATION: >
  A quantity is transmitted with a unit code that does not correctly correspond to the internally recorded unit
  of measure, with no conversion applied and no block raised.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Use an internal unit of measure with no exact standard equivalent and attempt to transmit an order line
  expressed in it.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q028

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q028
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the order is expressed in a currency different from a reference currency the exchange format requires,
  the rate used for that representation is the same rate the internal record uses for the same moment, not a
  separately looked-up rate.
WHY_IT_MATTERS: >
  Two different rates being used for the same transaction, one internal and one for the exchanged form, creates
  a value that neither side's books actually agree with.
DISCONFIRMING_OBSERVATION: >
  The rate embedded in or implied by the exchanged document differs from the rate recorded on the internal order
  for the same transaction date.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create an order in a foreign currency and compare the rate reflected in the exchanged document with the rate
  stored on the internal order.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q029

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q029
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A quantity or amount that would require truncation or scientific-notation-style representation to fit the
  exchange format's numeric constraints is either handled by a defined precision rule or blocks the send, rather
  than being silently truncated to a value that no longer matches the source.
WHY_IT_MATTERS: >
  Silent truncation to fit a format constraint produces a legally exchanged document that states a different
  quantity than what was actually agreed.
DISCONFIRMING_OBSERVATION: >
  A value requiring more precision than the exchange format allows is sent truncated with no warning, and the
  truncated value differs materially from the source value.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Construct an order line with a quantity or price requiring unusually high precision and attempt to transmit
  it.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q030

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q030
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An acknowledgement that the transmission mechanism accepted the message is not treated as equivalent to the
  counterparty's own system having accepted the document; the two are tracked as separate states, and a later
  rejection by the counterparty's system after transport-level acceptance updates that separate state.
WHY_IT_MATTERS: >
  Treating transport acceptance as final closure means a later real-world rejection is never followed up because
  the system already considers the matter settled.
DISCONFIRMING_OBSERVATION: >
  Once transport-level acceptance is recorded, the order or document shows no further open state that a later
  counterparty-system rejection could update.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Simulate transport-level acceptance followed some time later by a counterparty-system-level rejection of the
  same document, and inspect whether the order's state reflects the later event.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q031

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q031
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  There is a defined maximum period after which a document that has not received counterparty-system-level
  confirmation (only transport acceptance) is surfaced as overdue for confirmation, rather than remaining
  indefinitely in an unconfirmed state with nothing prompting a check.
WHY_IT_MATTERS: >
  An exchange with no confirmation timeout can leave a genuinely failed transaction looking dormant instead of
  actionable.
DISCONFIRMING_OBSERVATION: >
  A document sits with only transport-level acceptance and no counterparty-system confirmation indefinitely,
  with nothing in the system surfacing it as needing attention.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Leave a transmitted document unconfirmed at the counterparty-system level for an extended period and check
  whether it is surfaced anywhere as needing follow-up.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q032

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q032
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whoever is notified of a late counterparty-system-level rejection is defined by the order's ownership, not by
  who happened to trigger the original transmission, who may no longer be the order's owner by that point.
WHY_IT_MATTERS: >
  Notifying the wrong person about a rejection delays the response by however long it takes to reach whoever can
  actually act on it.
DISCONFIRMING_OBSERVATION: >
  A late rejection notification goes only to whoever originally triggered the send, even after the order's
  ownership has since changed.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Reassign an order's ownership after transmission, then simulate a late counterparty-system rejection and check
  who is notified.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q033

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q033
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Goods movement or billing steps triggered on the strength of a transport-accepted document are flagged for
  review, not automatically reversed, if a counterparty-system-level rejection arrives afterward.
WHY_IT_MATTERS: >
  Automatic reversal of already-completed physical or financial steps on a late rejection can itself create a
  second inconsistency rather than resolving the first.
DISCONFIRMING_OBSERVATION: >
  A late counterparty-system rejection automatically triggers reversal of receiving or billing steps already
  completed, with no review step.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Complete a receiving or billing step after transport-level acceptance, then simulate a late counterparty-system
  rejection and observe what happens to those completed steps.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q034

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q034
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the internal order and the last-transmitted document disagree, the system does not present the internal
  order as though it were itself the legally exchanged document; the two are always distinguishable as to which
  one actually left the business.
WHY_IT_MATTERS: >
  Presenting an internally-edited order as if it were the exchanged document misleads anyone relying on it for
  legal or contractual purposes.
DISCONFIRMING_OBSERVATION: >
  A printed or displayed view of the order, after a divergent internal edit, is indistinguishable from, or is
  labeled as, the document actually transmitted.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Diverge the internal order from the last-transmitted document, then view or print the order and compare its
  presentation and labeling to the actual transmitted document.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q035

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q035
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a correction to an already-transmitted document is required, the mechanism used produces a new,
  separately identifiable corrective document rather than overwriting the record of the original in place.
WHY_IT_MATTERS: >
  Overwriting the original transmitted record in place destroys the ability to show what was actually exchanged
  at each point in time.
DISCONFIRMING_OBSERVATION: >
  Correcting a transmitted document replaces the retained record of the original rather than adding a new,
  separately dated corrective record alongside it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger a correction to an already-transmitted document and inspect whether the original transmitted record
  still exists separately afterward.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q036

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q036
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cancellation of the order after transmission produces its own distinct exchanged notice to the counterparty,
  where the exchange format supports one, rather than the cancellation existing only as an internal state with
  the counterparty left to infer it from silence.
WHY_IT_MATTERS: >
  A counterparty left to infer cancellation from the absence of further communication may continue acting on a
  commitment the business considers void.
DISCONFIRMING_OBSERVATION: >
  The order is cancelled internally after transmission with no corresponding notice generated for the
  counterparty, even though the exchange format has a defined way to express one.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Cancel an order after it has been transmitted and check whether any cancellation-related document or notice is
  generated for the counterparty.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q037

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q037
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The exact content of a document as actually transmitted can be reproduced later, unchanged, independent of
  whatever the current state of the order has since become.
WHY_IT_MATTERS: >
  Without an exact, immutable retained copy, a dispute months later about what was actually sent cannot be
  resolved from the system at all.
DISCONFIRMING_OBSERVATION: >
  Attempting to retrieve the exact transmitted content of an old document instead returns a regeneration based
  on the order's current data, which differs from what was originally sent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transmit a document, substantially edit the underlying order afterward, then retrieve the "sent" record for
  the original transmission and compare it against the edited order's current data.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q038

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q038
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The retained copy of a transmitted document is kept for at least as long as any documented retention
  requirement that applies to the business records it represents, not governed by an unrelated, shorter general
  storage or log-cleanup period.
WHY_IT_MATTERS: >
  A retained document purged on a generic housekeeping schedule shorter than the applicable record-retention
  expectation leaves the business unable to produce evidence it is otherwise expected to hold.
DISCONFIRMING_OBSERVATION: >
  The retained copy of a transmitted document becomes unavailable before any documented retention period for
  that class of record has elapsed.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Identify the retention or cleanup rule governing stored transmitted documents and compare its horizon against
  any documented record-retention expectation for that class of document.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q039

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q039
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Retrieving the historical exact content of a transmitted document requires no greater access than viewing the
  order itself would, or if it requires more, that additional requirement is consistent and documented rather
  than arbitrary.
WHY_IT_MATTERS: >
  An arbitrary access gap between viewing an order and viewing what was actually sent about it either blocks
  legitimate audit work or under-protects sensitive exchanged content.
DISCONFIRMING_OBSERVATION: >
  Two users with identical permission to view an order find they have different ability to retrieve the
  historical transmitted content for it, for no documented reason.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Compare the permission needed to view an order against the permission needed to retrieve its historical
  transmitted content, across more than one role.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q040

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q040
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The retained transmitted content includes enough context (which counterparty, which channel, the outcome
  received back, if any) to be useful as evidence on its own, rather than being an isolated file that requires
  cross-referencing several other records to mean anything.
WHY_IT_MATTERS: >
  A retained document with no surrounding context is much weaker evidence months later, when the people who
  handled the original exchange may no longer be available to explain it.
DISCONFIRMING_OBSERVATION: >
  The retained transmitted content, viewed on its own months later, gives no indication of the counterparty,
  channel, or outcome without consulting separate records.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Retrieve an old transmitted document's retained record in isolation and assess what context it carries
  without cross-referencing other records.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q041

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q041
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The sender identity asserted in an exchanged document (the legal entity the counterparty understands itself to
  be transacting with) is determined by which company the order belongs to, and is never a fixed, shared identity
  used regardless of which company actually placed the order.
WHY_IT_MATTERS: >
  Asserting the wrong legal entity as sender misrepresents who the counterparty is actually contracting with,
  which has real legal consequence.
DISCONFIRMING_OBSERVATION: >
  Orders belonging to two different companies produce exchanged documents asserting the same sender identity,
  with no per-company distinction.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Place comparable orders under two different companies and compare the sender identity asserted in each one's
  exchanged document.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q042

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q042
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a company has not been configured with everything needed to send under its own identity, transmission
  for its orders is blocked rather than falling back to another company's identity to get the message out.
WHY_IT_MATTERS: >
  A silent fallback to another company's sender identity creates a document asserting a legal entity that did
  not actually make the commitment.
DISCONFIRMING_OBSERVATION: >
  An order under a company missing its sender-identity configuration is transmitted successfully anyway,
  asserting a different company's identity.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Remove or leave incomplete the sender-identity configuration for one company, then attempt to transmit a
  document for an order under that company.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q043

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q043
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to a company's sender identity configuration does not retroactively alter how already-transmitted
  documents for that company are represented in the retained record.
WHY_IT_MATTERS: >
  Retroactively rewriting historical sent documents to reflect a later identity change misstates what was
  actually asserted to the counterparty at the time.
DISCONFIRMING_OBSERVATION: >
  Changing a company's sender-identity configuration causes the retained record of a previously transmitted
  document to display the new identity instead of the one actually sent.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Transmit a document under a company's current sender identity, change that company's identity configuration,
  then re-inspect the retained record of the earlier transmission.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q044

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q044
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an outage occurs during transmission such that whether the counterparty received the document is
  genuinely unknown, the order is left in a distinct "uncertain" state rather than being assumed either sent or
  unsent.
WHY_IT_MATTERS: >
  Assuming an uncertain transmission succeeded risks the counterparty never having received it; assuming it
  failed risks a duplicate if it actually did arrive.
DISCONFIRMING_OBSERVATION: >
  After a simulated mid-transmission outage with no delivery confirmation, the order is marked definitively as
  either sent or not sent, with no distinct uncertain state.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Simulate a network or system outage occurring during a transmission attempt, after the message has left but
  before any acknowledgement is received, and inspect the resulting order state.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q045

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q045
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Recovery from an uncertain mid-exchange state requires a deliberate reconciliation step (confirming with the
  counterparty or checking a delivery record) rather than the system automatically resolving the ambiguity one
  way after some elapsed time with no such check.
WHY_IT_MATTERS: >
  Auto-resolving a genuine ambiguity without checking reality just replaces uncertainty with confident wrongness
  half the time.
DISCONFIRMING_OBSERVATION: >
  An order left in an uncertain transmission state automatically flips to "sent" or "not sent" after a timeout,
  with no reconciliation action having occurred.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Leave an order in the uncertain state produced by a simulated mid-transmission outage and observe its state
  after an extended period with no manual reconciliation.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q046

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q046
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Retrying a transmission that is in the uncertain state is possible without first forcing a duplicate if the
  original attempt actually succeeded; some safeguard exists against blindly resending into that ambiguity.
WHY_IT_MATTERS: >
  Retrying blind into a genuinely uncertain outcome is exactly how duplicate transmissions to the counterparty
  happen in practice.
DISCONFIRMING_OBSERVATION: >
  Retrying a transmission from the uncertain state sends a full new transmission with no check for, or warning
  about, the possibility that the original already arrived.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Put a transmission into the uncertain state via a simulated outage, then attempt a retry and observe whether
  any duplicate-risk safeguard is applied.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q047

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q047
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Resolving an order stuck in the uncertain transmission state (deciding it was sent, was not sent, or needs a
  fresh attempt) requires the same or greater authority as confirming the order in the first place, not merely
  whoever notices the stuck state.
WHY_IT_MATTERS: >
  An unresolved authority boundary on ambiguous-state resolution lets an under-qualified user make a call with
  real counterparty-facing consequences.
DISCONFIRMING_OBSERVATION: >
  Any user with ordinary order-viewing access can resolve an uncertain transmission state with no additional
  permission check.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Compare the permission needed to view an order in the uncertain transmission state against the permission
  needed to resolve that state.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q048

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q048
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two users concurrently triggering transmission for the same order (for example one from an automated schedule,
  one manually) do not both produce a live transmission to the counterparty; a lock or equivalent safeguard
  prevents a race from becoming a duplicate send.
WHY_IT_MATTERS: >
  Concurrent triggers are an ordinary operational occurrence, and if they can race, duplicate transmission is
  not a rare edge case but a routine risk.
DISCONFIRMING_OBSERVATION: >
  Triggering transmission for the same order from two paths at effectively the same time results in two separate
  live transmissions to the counterparty.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Arrange for a scheduled and a manual transmission trigger to fire for the same order at nearly the same moment
  and observe whether both complete as live sends.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q049

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q049
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the internal commitment (marking the order as transmitted) and the actual network send are not a single
  atomic action, a failure between the two does not leave the order falsely marked as transmitted when nothing
  actually left the business, nor silently re-attempt without visibility.
WHY_IT_MATTERS: >
  A false "transmitted" mark with no message actually sent is worse than an outright failure, because nothing
  then prompts anyone to follow up.
DISCONFIRMING_OBSERVATION: >
  A simulated failure occurring after the order is marked transmitted internally but before the message is
  confirmed to have left the business results in the order remaining marked as transmitted with no visible
  discrepancy.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Simulate a failure at the boundary between recording the order as transmitted and the message actually
  leaving the business, then inspect the order's resulting state.
```

## G07-PURCHASE_EDI_UBL_BIS3-Q050

```yaml
QID: G07-PURCHASE_EDI_UBL_BIS3-Q050
MODULE: purchase_edi_ubl_bis3
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whether an order can be transmitted at all is governed by the exchange configuration in force for that
  specific company, so that an order under one company is never transmitted using another company's exchange
  configuration (channel, endpoint, credentials) by mistake.
WHY_IT_MATTERS: >
  Sending an order under the wrong company's exchange configuration could deliver it through the wrong channel
  or under the wrong contractual relationship entirely.
DISCONFIRMING_OBSERVATION: >
  An order belonging to one company is transmitted using the exchange configuration (channel, endpoint, or
  credentials) belonging to a different company.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure two companies with distinct exchange channels or endpoints, then transmit an order under one
  company and verify which configuration was actually used.
```

---
## GMVQ Internal QA Checklist

- [x] 50 distinct MVQ records; no padding — every record targets a distinct seam hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`, and no two records share one failure event.
- [x] Bridge Module Rule seam test applied to every question: removing the exchange capability and using the
      order and the counterparty relationship apart would make the question meaningless. No question restates
      base-module (`purchase`) behavior with the bridge's name attached.
- [x] Pre-authoring sibling check performed against the only bank on disk at authoring time (`purchase`, P14,
      62 questions); no overlap found.
- [x] Questions are behavioral and source-neutral; no vendor/product/standard/profile name, technical
      identifier, or the module's own metadata name appears in question text.
- [x] Seam dimensions represented: ordering (Q001-Q008, Q048), partiality (Q018-Q021, Q044-Q047), ownership
      (Q003, Q022-Q025), timing (Q026-Q029, Q030-Q033), reversal (Q009-Q012, Q036), quantity-and-money
      (Q026-Q029), lifecycle mismatch (Q034-Q036), error asymmetry (Q030-Q033, Q049), authority (Q011, Q015,
      Q032, Q047).
- [x] Tenant/company boundary represented (Q041-Q043, Q050).
- [x] Concurrency represented (Q007, Q044-Q049).
- [x] No specific standard, profile, or vendor technical detail asserted anywhere in this bank.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
