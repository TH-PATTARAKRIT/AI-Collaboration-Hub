# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_pdf_quote_builder Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE_PDF_QUOTE_BUILDER-MVQ50-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_pdf_quote_builder`
**Wave:** W2
**Author Cell:** P-S9 (GMVQ Question Factory — Internal Production Team S9, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50

## Purpose

`sale_pdf_quote_builder` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Its seam is the customer-facing RENDERED quotation document as a distinct artefact from the order record it is generated from. Per the Bridge Module Rule, every question in this bank was tested against the seam question: "if this capability were removed and the order and the rendering mechanism were used entirely apart, would the question still make sense?" A YES answer means the question belongs to the base `sale` bank, not here, and was cut.

Every question below targets the gap between the record and the artefact the customer actually received: a document rendered at one moment against an order that changes afterward; optional or alternative lines shown to the customer that are not commitments in the record; internal information (cost, margin, notes, another customer's detail) leaking into a customer-facing render; a customer accepting a version that no longer matches the record and which one binds; terms and conditions versioned into the document; a document regenerated and silently different; locale, currency, and rounding presentation divergence from stored values; whether the exact artefact sent can be reproduced later as evidence; and who may edit the document's content independently of the order.

## Control

- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$DIR"/*.md | sort` was run before writing a single question. At authoring time G08_SALES held no other banks on disk, so there was no sibling bank content to check within this group; the base `sale` module's own ground (quotation lifecycle, confirmation, price/discount, modification after confirmation) is covered by the base bank per the Group Brief and was deliberately excluded here — every question in this bank fails specifically at the record-versus-rendered-artefact seam and would be meaningless if the rendering capability were removed and the order were used without ever producing a customer-facing document.
- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong, and the disconfirming observation is a distinct event for every question — no two questions share one failure event.
- No padding: 50 questions exist because they test 50 distinct material hypotheses at the seam. Depth requirement (55 shared + 48 module minimum = 103) is met once combined with the shared standard bank.
- This module carries one layer at the seam; the `LAYER` field is omitted throughout.
- Clean-room compliance: no vendor or product name, no technical identifier (model, table, field, method, XML ID, API path, standard or profile name), and no implementation shape appears anywhere in question text.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank. Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.
- Seam dimensions represented (GMVQ_BRIDGE_MODULE_RULE_V1.00 §3): lifecycle mismatch (Q001, Q003, Q005, Q021-Q022, Q024, Q026-Q028, Q030, Q036-Q037, Q046, Q050), timing (Q002, Q016), ownership (Q004, Q006-Q009, Q011-Q014, Q017-Q019, Q023, Q025, Q032-Q035, Q039-Q041, Q043, Q047-Q049), quantity and money (Q010, Q031), authority (Q015, Q038, Q042, Q044), partiality (Q020), error asymmetry (Q029), ordering (Q045).
- Coverage map: rendered snapshot diverging from a since-changed record Q001-Q005 · optional and alternative lines not committed in the record Q006-Q010 · internal information leaking into the customer-facing render Q011-Q015 · conflicting accepted version and which one binds Q016-Q020 · terms and conditions versioning Q021-Q025 · regeneration producing a silently different document Q026-Q030 · locale, currency, and rounding presentation divergence Q031-Q035 · reproducing the exact sent artefact as evidence Q036-Q040 · authority to edit rendered content independently of the order Q041-Q045 · revision identity, signature binding, and multi-party/tenant identity Q046-Q050

## G08-SALE_PDF_QUOTE_BUILDER-Q001

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q001
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A quotation document, once rendered and sent to the customer, is retained as a fixed snapshot of the order's
  content at that moment, so a later change to the order does not alter what the retained rendered document
  shows.
WHY_IT_MATTERS: >
  If the rendered document is not fixed, the business cannot know what the customer actually saw when they later
  refer back to the quote they were sent.
DISCONFIRMING_OBSERVATION: >
  Changing the order after the quote was rendered and sent causes the previously rendered document, when
  reopened, to display the new values instead of the ones actually shown to the customer.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Render and send a quote, change the order afterward, then reopen the originally rendered document.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q002

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q002
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The system distinguishes, for any given order, whether a rendered document has ever been sent, so that the
  order having changed since the last document was generated can be flagged rather than assumed always true or
  always false.
WHY_IT_MATTERS: >
  Without that distinction, staff cannot tell whether the customer's copy is stale or still current, and either
  false assumption causes a real error.
DISCONFIRMING_OBSERVATION: >
  An order changed after its quote was rendered and sent shows no indication, anywhere, that the sent document
  is now stale relative to the current record.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Render and send a quote, modify the order, then view the order and check for a staleness indicator.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q003

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q003
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Re-rendering a document after the order has changed produces a document that is distinguishable, by version or
  timestamp, from the one originally sent, rather than looking identical except for the values that changed.
WHY_IT_MATTERS: >
  An indistinguishable re-render makes it impossible to tell, from the document alone, which version of several
  a given customer copy actually is.
DISCONFIRMING_OBSERVATION: >
  Two renders of the same order taken before and after a change carry no version marker, timestamp, or other
  distinguishing feature beyond the changed values themselves.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Render a document, change the order, render again, and compare the two documents for a distinguishing marker.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q004

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q004
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Sending a re-rendered document to the customer after a change does not retroactively alter the retained copy
  of the document actually sent before the change; both remain independently retrievable.
WHY_IT_MATTERS: >
  Collapsing the two into one retained copy destroys the ability to show what the customer held at each point in
  time.
DISCONFIRMING_OBSERVATION: >
  After a second document is sent, retrieving the document sent to this customer returns only the newer one,
  with the earlier one no longer retrievable.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a document, change the order, send a re-rendered document, then attempt to retrieve the first one
  specifically.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q005

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q005
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An order-level lock or restriction intended to prevent further change after a certain point does not stop a
  document from still being re-rendered for viewing purposes, since viewing a locked order's current state is a
  different action from altering it.
WHY_IT_MATTERS: >
  Conflating cannot-render with cannot-edit would block a legitimate need to reprint or resend an unchanged,
  already-locked quotation.
DISCONFIRMING_OBSERVATION: >
  An order that is locked against further edits also cannot have its quotation document re-rendered at all, even
  with no change involved.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Lock an order against edits, then attempt to render its quotation document again with no changes made.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q006

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q006
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A line marked optional or alternative on the rendered document is not counted toward the order's committed
  total held in the record, so the customer-facing total shown for firm items matches what the record treats as
  actually committed.
WHY_IT_MATTERS: >
  Blurring optional lines into the committed total misleads the customer about what they are actually agreeing
  to pay if they simply accept the document as shown.
DISCONFIRMING_OBSERVATION: >
  The total shown on the rendered document includes an optional or alternative line's value as though it were
  part of the firm total.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Add an optional line to an order alongside firm lines, render the document, and check whether the optional
  line is separated from the firm total.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q007

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q007
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Selecting or deselecting an optional or alternative line on the customer-facing document, where the tooling
  allows a customer or representative to do so interactively, updates the underlying record through a defined,
  auditable action rather than only changing what is displayed.
WHY_IT_MATTERS: >
  A display-only selection that never reaches the record creates a document the customer believes reflects their
  choice while the business's own system never learns of it.
DISCONFIRMING_OBSERVATION: >
  Toggling an optional line's selection on the rendered document produces no corresponding change, or any record
  of an intended change, in the underlying order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Toggle an optional line's selection on an interactive rendered document, then check the underlying order for
  any resulting change or log entry.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q008

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q008
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An alternative line presented on the document as a substitute for a firm line, rather than an addition to it,
  is rendered in a way that makes clear only one of the pair is intended to be ordered, not both simultaneously.
WHY_IT_MATTERS: >
  An ambiguous rendering of mutually exclusive alternatives risks the customer, or staff processing acceptance,
  treating both as separately ordered.
DISCONFIRMING_OBSERVATION: >
  A firm line and its designated alternative both appear on the rendered document with nothing indicating they
  are mutually exclusive.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Configure a firm line with a designated alternative and render the document, checking how the exclusivity is
  communicated.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q009

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q009
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Converting an accepted alternative line into the order's firm content is a defined, traceable action distinct
  from ordinary line entry, since it represents the customer's choice among options that were never all
  committed at once.
WHY_IT_MATTERS: >
  If accepting an alternative looks identical in the record to an ordinary added line, the fact that a choice
  was made among presented options is lost.
DISCONFIRMING_OBSERVATION: >
  An alternative line the customer accepted becomes an ordinary firm order line indistinguishable from one
  entered directly, with no trace that it was chosen from alternatives.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Have a customer accept a specific alternative line and inspect the resulting order line for any indication of
  its origin as a chosen alternative.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q010

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q010
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A price or discount shown against an optional or alternative line on the document reflects the same pricing
  rules that would apply if that line were firm, not a placeholder or simplified figure specific to the optional
  state.
WHY_IT_MATTERS: >
  A placeholder figure that differs from the real applicable price misleads the customer about what accepting
  the option would actually cost.
DISCONFIRMING_OBSERVATION: >
  The price shown for an optional line on the document differs from the price that would actually apply if that
  same line were made firm.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Compare the price shown for an optional line to the price that results when that same line is converted to
  firm.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q011

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q011
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The rendered customer-facing document never includes the item's cost or margin figures, regardless of what the
  underlying record stores or what other internal views display.
WHY_IT_MATTERS: >
  Cost and margin are commercially sensitive; their accidental inclusion on a customer-facing document discloses
  the business's negotiating position.
DISCONFIRMING_OBSERVATION: >
  A rendered quotation includes a cost or margin figure anywhere in its content.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Render a quotation for an order whose lines carry cost and margin data, and inspect the full rendered content
  for their presence.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q012

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q012
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An internal note or comment attached to an order for internal use is excluded from the customer-facing
  rendered document by default, requiring a deliberate, separate action to include any note that is genuinely
  meant for the customer.
WHY_IT_MATTERS: >
  A note written for internal coordination may contain commentary never intended for the customer's eyes, and
  default inclusion turns every internal note into a leak risk.
DISCONFIRMING_OBSERVATION: >
  An internal-only note attached to the order appears on the rendered customer-facing document without any
  deliberate action to include it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attach an internal note to an order and render its customer-facing document, checking whether the note
  appears.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q013

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q013
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A template or layout element carried over from a previous document, such as a header, footer, or reused block,
  never carries another customer's name, reference, or detail into a newly rendered document for a different
  customer.
WHY_IT_MATTERS: >
  A carried-over fragment naming a different customer is both an embarrassment and a data-protection failure.
DISCONFIRMING_OBSERVATION: >
  A rendered document for one customer contains a name, reference, or detail belonging to a different customer.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Render documents in succession for two different customers using the same template and inspect each for cross-
  contamination.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q014

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q014
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a specific field, such as an internal reference code or a warehouse location, appears on the customer-
  facing document is governed by an explicit template configuration, not by whatever happens to be present on
  the underlying record.
WHY_IT_MATTERS: >
  Without explicit configuration, any new internal field added to the record risks silently appearing on
  customer-facing output the next time the template is touched.
DISCONFIRMING_OBSERVATION: >
  A newly added internal-only field on the order record appears on the rendered document with no configuration
  step having authorized it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Add a new internal-only field to the order record and render the document without changing template
  configuration, checking whether the field appears.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q015

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q015
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A user permitted to render and send customer-facing documents but not permitted to view cost or margin data
  cannot obtain that data indirectly by rendering a document and inspecting its content or underlying source.
WHY_IT_MATTERS: >
  A document-rendering permission that indirectly exposes data a role is otherwise blocked from seeing defeats
  the purpose of that restriction.
DISCONFIRMING_OBSERVATION: >
  A user without cost or margin visibility can see cost or margin figures by rendering a document or inspecting
  the file the rendering step produces.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user without cost or margin visibility, render a customer-facing document and inspect its full content
  and underlying source for such figures.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q016

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q016
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a customer returns an accepted or signed copy of a document that does not match the current record, the
  system identifies the discrepancy rather than proceeding as though the current record were what was accepted.
WHY_IT_MATTERS: >
  Proceeding on the current record when the customer actually agreed to something else risks confirming an order
  the customer never actually accepted.
DISCONFIRMING_OBSERVATION: >
  A customer's returned acceptance of an older rendered version is processed by confirming the order at its
  current, different values with no discrepancy identified.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change the order after a document was rendered, then process a returned acceptance referencing the earlier
  rendered version, and check whether the mismatch is surfaced.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q017

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q017
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Confirming an order from a customer's acceptance uses the specific rendered version the customer actually
  accepted as the basis for what becomes the confirmed order, not whatever the order's live values happen to be
  at the moment confirmation is processed.
WHY_IT_MATTERS: >
  Confirming against live values rather than the accepted version silently substitutes different terms for what
  the customer actually agreed to.
DISCONFIRMING_OBSERVATION: >
  Confirming an order from an accepted document produces a confirmed order whose values differ from the specific
  rendered version the customer accepted.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Render a document, change the order, then process an acceptance of the original rendered version, and compare
  the resulting confirmed order's values against that accepted version.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q018

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q018
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where more than one rendered version of the same order has been sent, an acceptance is attributed to the
  specific version it actually corresponds to, not assumed to be of the most recently sent version by default.
WHY_IT_MATTERS: >
  Assuming the latest version was accepted, when the customer was actually responding to an earlier one,
  misrepresents what was agreed.
DISCONFIRMING_OBSERVATION: >
  An acceptance referencing an earlier rendered version is recorded as acceptance of the latest version instead.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send two versions of a document to the same customer, then process an acceptance that references the earlier
  one specifically, and check which version it is attributed to.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q019

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q019
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An acceptance that cannot be matched to any rendered version actually sent is held in a distinct, visible
  unresolved state, rather than being applied to whichever order looks like the closest match.
WHY_IT_MATTERS: >
  Silently guessing which order an unmatched acceptance belongs to risks confirming the wrong order entirely.
DISCONFIRMING_OBSERVATION: >
  An acceptance that does not correspond to any document actually sent is nonetheless applied to an order
  without any flag that the match was uncertain.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit an acceptance referencing content that was never actually rendered or sent, and observe how the system
  handles the mismatch.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q020

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q020
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two different accepted versions of the same order arriving from the customer, for example one from each of two
  people at the customer's organization, are both retained and flagged as conflicting rather than the second
  silently overwriting the first with no record of the disagreement.
WHY_IT_MATTERS: >
  A silent overwrite hides a genuine internal disagreement on the customer's side that the seller may need to
  resolve before proceeding.
DISCONFIRMING_OBSERVATION: >
  A second acceptance for the same order replaces the first with no indication that two different accepted
  versions were ever received.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit two differing accepted versions of the same rendered document in succession and inspect whether both
  are retained and the conflict flagged.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q021

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q021
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The specific version of terms and conditions included in a rendered document is recorded against that
  document, so it remains known which version of the terms a given customer actually received, independent of
  whatever version is current later.
WHY_IT_MATTERS: >
  If the specific version is not recorded, a later dispute over which terms governed a given sale cannot be
  resolved from the record alone.
DISCONFIRMING_OBSERVATION: >
  A rendered document's retained record does not indicate which version of the terms and conditions text it
  included at the time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Render a document, later change the standard terms and conditions text, then inspect the earlier document's
  record for which version it used.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q022

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q022
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing the standard terms and conditions text does not retroactively alter what a previously rendered and
  sent document is understood to have contained.
WHY_IT_MATTERS: >
  Retroactively rewriting history of what terms a customer received would misstate the actual contractual basis
  of that sale.
DISCONFIRMING_OBSERVATION: >
  After the standard terms and conditions text changes, reopening an earlier rendered document shows the new
  text rather than the version actually included at the time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Render and send a document, change the standard terms text, then reopen the earlier document and check which
  version of the text displays.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q023

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q023
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where different terms and conditions apply depending on the customer, region, or product line, the document
  renders the specific terms applicable to that order's actual context, not a single generic version applied
  uniformly.
WHY_IT_MATTERS: >
  Applying the wrong terms to an order misrepresents the actual legal basis the customer is agreeing to.
DISCONFIRMING_OBSERVATION: >
  Two orders with genuinely different applicable terms both render the identical generic terms text.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure two orders with distinct applicable terms sets and render each, comparing the resulting terms text.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q024

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q024
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An order confirmed under one version of the terms and conditions retains that version's association even if
  the order is later reopened, amended, or re-rendered for an unrelated reason.
WHY_IT_MATTERS: >
  An amendment for an unrelated reason should not silently upgrade a customer to different terms they never
  agreed to for the parts of the order that did not change.
DISCONFIRMING_OBSERVATION: >
  Re-rendering an already-confirmed order for an unrelated line change also updates its associated terms and
  conditions version with no separate decision to do so.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an order under one terms version, change the standard terms, make an unrelated amendment to the order,
  and re-render, checking which terms version is now associated.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q025

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q025
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A customer-negotiated deviation from the standard terms, where one has been agreed, is reflected in that
  customer's rendered documents specifically, rather than the standard terms being rendered regardless of the
  negotiated deviation on file.
WHY_IT_MATTERS: >
  Rendering the standard terms over a genuinely negotiated deviation presents the customer with a document that
  misstates the actual agreement.
DISCONFIRMING_OBSERVATION: >
  A customer with an on-file negotiated deviation from standard terms still receives a rendered document showing
  the unmodified standard terms.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record a negotiated terms deviation for a customer, render a document for that customer, and check whether the
  deviation is reflected.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q026

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q026
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Regenerating a document from the same order with nothing changed produces content identical to the original
  render, so a document is never silently different purely because it was rendered a second time.
WHY_IT_MATTERS: >
  An unexplained difference between two renders of the same unchanged data would make every regenerated document
  suspect.
DISCONFIRMING_OBSERVATION: >
  Rendering the same unchanged order twice, back to back, produces two documents with a difference not
  attributable to any change in the order.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Render a document twice in succession from an unchanged order and compare the two outputs in full.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q027

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q027
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the rendering template itself is updated between two renders of the same order data, the resulting
  difference is attributable to the template change and is not presented as though the order's own content had
  changed.
WHY_IT_MATTERS: >
  Conflating a template change with a content change misleads anyone comparing two documents about what actually
  happened to the order.
DISCONFIRMING_OBSERVATION: >
  Two renders differing only because the template was updated in between show no indication that a template
  change, rather than an order change, caused the difference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Render a document, update the rendering template with no order change, render again, and compare the two for
  any indication of the cause.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q028

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q028
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A regenerated document replacing a previously sent one is distinguishable to whoever handles the customer
  relationship as a re-issue, not indistinguishable from a first-time send of a brand-new quotation.
WHY_IT_MATTERS: >
  A salesperson unaware that a document is a re-issue might describe it to the customer inconsistently with what
  was already communicated.
DISCONFIRMING_OBSERVATION: >
  Regenerating and resending a document for an order that was already quoted gives the person sending it no
  indication that this is a re-issue rather than a first send.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Render and send a document, then regenerate and resend for the same order, and check whether the sending
  interface indicates a re-issue.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q029

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q029
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A failure partway through regenerating a document, such as an error rendering one section, does not result in
  a partially rendered or corrupted document being sent to the customer as though it were complete.
WHY_IT_MATTERS: >
  A partially rendered document reaching a customer looks unprofessional at best and can present materially
  wrong figures at worst.
DISCONFIRMING_OBSERVATION: >
  A simulated rendering failure partway through document generation still results in a document being sent to
  the customer.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Simulate a rendering failure partway through generating a document and observe whether a document is
  nonetheless sent.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q030

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q030
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Regenerating a document for an order that has since moved to a state where quotations are no longer the
  relevant document type, such as after full invoicing, either reflects that changed context explicitly or is
  blocked, rather than producing a quotation-styled document for a transaction that has already moved past that
  stage.
WHY_IT_MATTERS: >
  Sending a quotation-styled document for an already-invoiced transaction confuses the customer about what stage
  the transaction is actually at.
DISCONFIRMING_OBSERVATION: >
  An order already fully invoiced still allows generation of a plain quotation-styled document with no
  indication of the order's actual current stage.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Advance an order to a fully invoiced state, then attempt to regenerate its original quotation document and
  observe the result.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q031

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q031
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A monetary amount shown on the rendered document, after any presentation-level rounding for display, always
  reconciles to the precise stored value used for the order's own calculations, so the displayed figure is never
  the actual value relied upon for computation.
WHY_IT_MATTERS: >
  If the displayed, rounded figure were also the one used internally, accumulated rounding across many lines
  could produce a total that does not match the sum of the displayed lines.
DISCONFIRMING_OBSERVATION: >
  Summing the individually displayed, rounded line amounts on the document does not equal the displayed total,
  with the difference unexplained.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Render a document with several lines whose amounts require display rounding, and check whether the displayed
  lines sum to the displayed total.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q032

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q032
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A document rendered in a language other than the one the underlying record is maintained in translates only
  presentation text, such as labels and terms, and never alters a numeric value, a date, or an identifier in the
  process.
WHY_IT_MATTERS: >
  A translation step that inadvertently alters a number or date would silently misstate the actual transaction
  to the customer.
DISCONFIRMING_OBSERVATION: >
  A document rendered in a different language shows a numeric value, date, or identifier different from the same
  document rendered in the original language.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Render the same order's document in two different languages and compare all numeric values, dates, and
  identifiers between them.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q033

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q033
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where an order's amounts are stored in one currency but the document is rendered showing a converted display
  currency for the customer's convenience, the document makes clear which currency is actually binding, rather
  than presenting the converted figure without qualification.
WHY_IT_MATTERS: >
  An unqualified converted figure could be mistaken by the customer for the actual amount owed, especially if
  the rate moves before payment.
DISCONFIRMING_OBSERVATION: >
  A document showing a converted currency figure gives no indication of which currency is the binding one or
  what rate was used.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Render a document with a converted display currency and inspect whether the binding currency and conversion
  basis are disclosed.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q034

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q034
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A date shown on the rendered document, such as a validity date or expected delivery date, reflects the same
  value and the same calculation basis as the equivalent date held in the record, not a value computed
  independently by the rendering step.
WHY_IT_MATTERS: >
  An independently computed date that drifts from the record's own date creates two different answers to when
  the quote is valid until, with no way to know which one governs.
DISCONFIRMING_OBSERVATION: >
  The validity or delivery date shown on the rendered document differs from the equivalent date held in the
  order record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Compare a date field on a rendered document against the equivalent field in the underlying order record.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q035

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q035
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A numeric formatting convention appropriate to the customer's locale, such as which character separates
  thousands from decimals, is applied consistently across every number on the document, not correctly on some
  fields and left in a different convention on others.
WHY_IT_MATTERS: >
  Inconsistent formatting on the same document can make a number's actual magnitude genuinely ambiguous to the
  reader.
DISCONFIRMING_OBSERVATION: >
  One numeric field on a rendered document uses a different locale formatting convention than the rest of the
  document.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Render a document for a locale with a distinct numeric formatting convention and check every numeric field for
  consistency.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q036

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q036
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The exact rendered file actually sent to the customer, byte for byte, can be retrieved later, rather than only
  the data used to render it, since the data alone re-rendered later may not reproduce the same file if the
  template has since changed.
WHY_IT_MATTERS: >
  Evidence of what was sent must be the artefact itself; recomputing a lookalike from current data and a current
  template is not the same evidence.
DISCONFIRMING_OBSERVATION: >
  Retrieving the document sent to the customer after the template has since changed returns a freshly
  regenerated file rather than the original file actually transmitted.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a document, change the rendering template, then attempt to retrieve the exact original file rather than a
  fresh regeneration.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q037

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q037
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The retained artefact of a sent document is kept for at least as long as the applicable retention requirement
  for the type of commercial document it represents, not governed by a shorter, unrelated general file-retention
  setting.
WHY_IT_MATTERS: >
  A shorter general policy purging the artefact early would leave no way to produce it if it were needed as
  evidence within the legitimate retention period.
DISCONFIRMING_OBSERVATION: >
  A retained sent document becomes unavailable before the retention period applicable to that type of commercial
  document has elapsed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the configured retention period for sent document artefacts against the applicable retention
  requirement for that document type.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q038

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q038
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Retrieving the exact artefact of a document sent to a specific customer requires no broader access than
  viewing that customer's order already would, or if it does require more, that additional requirement is a
  deliberate, documented control.
WHY_IT_MATTERS: >
  An incidental extra barrier at the moment evidence is needed can make the business appear unable to produce
  something it in fact retains.
DISCONFIRMING_OBSERVATION: >
  A user with ordinary access to a customer's order cannot retrieve the exact artefact of a document sent for
  that order, with no documented reason for the restriction.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user with ordinary order access, attempt to retrieve the exact sent-document artefact for that order.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q039

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q039
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a document was sent through more than one channel, such as attached to an outbound message and
  separately made available through a customer-facing portal, the retained record identifies which specific
  artefact went through which channel, rather than treating all sends as interchangeable copies of one file.
WHY_IT_MATTERS: >
  If a dispute concerns what a customer saw through a specific channel, treating all sends as interchangeable
  prevents answering that specific question.
DISCONFIRMING_OBSERVATION: >
  A document sent through two different channels is retained as a single undifferentiated record with no way to
  tell which artefact went through which channel.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send the same document through two different channels and inspect whether the retained record distinguishes
  them.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q040

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q040
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The retained artefact of a sent document carries enough context, such as which order, which customer, and when
  it was sent, to be usable as evidence on its own, without requiring correlation against other records purely
  to establish what it even was.
WHY_IT_MATTERS: >
  An artefact that cannot be identified on its own is materially weaker evidence than one that is self-
  contained.
DISCONFIRMING_OBSERVATION: >
  Retrieving a retained document artefact in isolation gives no indication of which order, customer, or send
  date it belongs to.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Retrieve a retained document artefact by itself and check whether its context is legible without consulting
  other records.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q041

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q041
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Free-text content added directly onto a rendered document, where the tooling allows editing the document
  itself rather than only the order, is retained as part of that document's record, so a later dispute over what
  was actually written can be resolved from the record rather than relying on memory.
WHY_IT_MATTERS: >
  A direct edit to the rendered output that leaves no trace becomes an unrecorded commitment the moment it is
  sent, since it exists nowhere else.
DISCONFIRMING_OBSERVATION: >
  Text added directly to a rendered document before sending does not appear anywhere in the retained record of
  that document afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Add free text directly to a rendered document before sending, then inspect the retained record of what was
  sent.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q042

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q042
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Editing a rendered document's content directly, independent of the underlying order, requires a level of
  authorization distinct from ordinary order entry, since such an edit can create a document that promises
  something the order itself does not reflect.
WHY_IT_MATTERS: >
  If anyone who can create an order can also freely alter the rendered output text, the document stops reliably
  representing the order at all.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary order-entry permission is able to directly edit a rendered document's content before
  it is sent.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with ordinary order-entry permission, attempt to directly edit a rendered document's content before
  sending.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q043

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q043
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A direct edit made to a rendered document's content is visibly flagged as a manual deviation from what the
  order data alone would have produced, so a later reviewer can tell the document does not purely reflect the
  order.
WHY_IT_MATTERS: >
  An invisible deviation makes the document look like a faithful rendering of the order when it in fact contains
  an unrecorded manual addition or change.
DISCONFIRMING_OBSERVATION: >
  A rendered document containing a direct manual edit displays identically to one produced purely from order
  data, with no indication a manual change was made.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Directly edit a rendered document's content and compare its appearance to an unedited rendering, checking for
  any deviation indicator.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q044

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q044
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A direct edit to a rendered document's content that materially changes a committed price, quantity, or term is
  treated as requiring the same review or approval as an equivalent change made directly on the order, not
  exempted because it was made on the document rather than the order.
WHY_IT_MATTERS: >
  Routing a material change through document editing rather than order editing to skip a required approval
  defeats the point of the approval control.
DISCONFIRMING_OBSERVATION: >
  A material price or term change made through direct document editing bypasses an approval that the equivalent
  change on the order itself would require.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Make a material change through direct document editing that would normally require approval if made on the
  order, and check whether the approval is still triggered.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q045

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q045
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two people editing the rendered content of the same document at nearly the same time do not have one person's
  changes silently overwritten by the other with no conflict indication.
WHY_IT_MATTERS: >
  A silent overwrite loses a genuine change with no record that it ever existed or that a conflict occurred.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous edits to the same document's content result in one being silently discarded with no
  conflict indication to either editor.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have two sessions edit the same rendered document's content at nearly the same time and observe the outcome.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q046

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q046
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Each distinct rendered and sent version of a document for the same order carries its own identifiable revision
  marker, so that which revision the customer actually received always has a specific, retrievable answer.
WHY_IT_MATTERS: >
  Without a revision marker, two different documents for the same order become indistinguishable from each other
  in later conversation or dispute.
DISCONFIRMING_OBSERVATION: >
  Two different rendered and sent versions of the same order's document carry no distinguishing revision marker
  between them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Render and send two different versions of the same order's document and check for a distinguishing revision
  marker on each.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q047

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q047
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where the document supports a signature or explicit acceptance mechanism, a completed signature is bound to
  the exact rendered content it was applied to, so the signed artefact cannot later be presented as though it
  had applied to different content.
WHY_IT_MATTERS: >
  A signature not bound to specific content could be claimed to cover a different version than the one actually
  signed, undermining the entire point of collecting it.
DISCONFIRMING_OBSERVATION: >
  A signed document's underlying content can be altered after signing while the recorded signature still shows
  as valid for the document.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Collect a signature on a rendered document, then attempt to alter the document's underlying content and check
  whether the signature still shows as valid.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q048

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q048
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a sale spans more than one company or branch, the rendered document presents a single, coherent selling-
  party identity to the customer consistent with which company the order actually belongs to, rather than mixing
  identifying details from more than one company on the same document.
WHY_IT_MATTERS: >
  A document mixing identities from more than one company confuses the customer about who they are actually
  contracting with and can misstate legal responsibility.
DISCONFIRMING_OBSERVATION: >
  A rendered document for an order belonging to one company shows a branding or identity detail belonging to a
  different company.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure an order under one company with document elements sourced from shared templates, render it, and
  check for cross-company identity leakage.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q049

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q049
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A tenant's document templates, branding, and rendered documents are never visible or selectable from within
  another tenant's document-rendering session, even where template names or structures happen to coincide.
WHY_IT_MATTERS: >
  Cross-tenant visibility of rendering assets or output would breach the isolation the platform is expected to
  guarantee between unrelated businesses.
DISCONFIRMING_OBSERVATION: >
  A user in one tenant's session can select or view a document template or rendered output belonging to a
  different tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user in one tenant, attempt to select or view a document template or rendered output belonging to a
  different tenant.
```

## G08-SALE_PDF_QUOTE_BUILDER-Q050

```yaml
QID: G08-SALE_PDF_QUOTE_BUILDER-Q050
MODULE: sale_pdf_quote_builder
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document rendered and sent under an account or session that is later deactivated remains attributable to the
  specific person who actually sent it at the time, rather than the historical record reassigning attribution to
  whoever currently holds that role.
WHY_IT_MATTERS: >
  Reassigning historical attribution when a role changes hands would misstate who actually made a specific
  commitment to a specific customer at the time.
DISCONFIRMING_OBSERVATION: >
  After the user who sent a document is deactivated, the retained record of that document reattributes the send
  to a different, current user.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Send a document as one user, deactivate that user's account, and check whether the retained record's
  attribution of the send changes.
```

---
## GMVQ Internal QA Checklist

- [x] 50 distinct MVQ records; no padding — every record targets a distinct seam hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`, and no two records share one failure event.
- [x] Bridge Module Rule seam test applied to every question: removing the second capability and using the base order and that capability apart would make the question meaningless. No question restates base-module (`sale`) behavior with the bridge's name attached.
- [x] Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$DIR"/*.md | sort` was run before writing a single question. At authoring time G08_SALES held no other banks on disk, so there was no sibling bank content to check within this group; the base `sale` module's own ground (quotation lifecycle, confirmation, price/discount, modification after confirmation) is covered by the base bank per the Group Brief and was deliberately excluded here — every question in this bank fails specifically at the record-versus-rendered-artefact seam and would be meaningless if the rendering capability were removed and the order were used without ever producing a customer-facing document.
- [x] Questions are behavioral and source-neutral; no vendor/product/standard name, technical identifier, or the module's own metadata name appears in question text.
- [x] Seam dimensions represented: lifecycle mismatch (Q001, Q003, Q005, Q021-Q022, Q024, Q026-Q028, Q030, Q036-Q037, Q046, Q050), timing (Q002, Q016), ownership (Q004, Q006-Q009, Q011-Q014, Q017-Q019, Q023, Q025, Q032-Q035, Q039-Q041, Q043, Q047-Q049), quantity and money (Q010, Q031), authority (Q015, Q038, Q042, Q044), partiality (Q020), error asymmetry (Q029), ordering (Q045).
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
