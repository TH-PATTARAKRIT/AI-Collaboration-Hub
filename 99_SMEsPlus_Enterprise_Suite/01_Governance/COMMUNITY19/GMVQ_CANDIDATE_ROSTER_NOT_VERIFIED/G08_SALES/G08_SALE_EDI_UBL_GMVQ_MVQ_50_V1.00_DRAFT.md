# SMEsPlus ENTERPRISE SUITE
## GMVQ — G08 SALES / sale_edi_ubl Module Adversarial MVQ Bank

**Document ID:** GMVQ-G08-SALE_EDI_UBL-MVQ50-V1.00
**Group:** G08 SALES
**Module Metadata:** `sale_edi_ubl`
**Wave:** W2
**Author Cell:** P-S9 (GMVQ Question Factory — Internal Production Team S9, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 50

## Purpose

`sale_edi_ubl` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00). Its seam is the order and its invoice exchanged as structured documents with the customer — generation, transmission, and receipt of the customer's own feedback. Per the Bridge Module Rule, every question in this bank was tested against the seam question: "if this capability were removed and the order and the exchange mechanism were used entirely apart, would the question still make sense?" A YES answer means the question belongs to the base `sale` bank, not here, and was cut. Every question below is a NO.

This bank is the mirror-opposite seam of a purchase-side structured-exchange bank already on disk (`purchase_edi_ubl_bis3`), and the direction was treated as material rather than cosmetic: here the business is the SENDER of the commercial document, the counterparty's system decides whether to accept it, and the business's own revenue recognition — not its spend — depends on that acceptance. Every question below is built around a sender/revenue-side failure mode (revenue posted ahead of confirmed acceptance, a customer-specific requirement the business cannot generically validate, silent transformation on the customer's side the business cannot observe, correction chains tied to revenue, legal-instrument identity, retention for tax/audit defensibility, acknowledgment as a recognition gate, order/invoice acceptance independence, customer-specific identifier mapping, per-customer channel routing, selling-entity identity, concurrency/double-posting, credit-note discipline, and partial-invoice reconciliation) rather than being the purchase-side receiver/spend bank with nouns swapped.

The module's metadata name carries standards-body tokens. Per the Group Brief and the Authoring Standard's clean-room rule, that name appears in the `MODULE:` field only. Question text refers throughout to "the structured document exchange," "the exchanged document," or "the customer's system" — never to the standard, the profile, or any technical identifier.

## Control

- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$DIR"/*.md | sort` was run before writing a single question. At authoring time G08_SALES held no other banks on disk. The sibling bridge bank actually checked, per this module's specific brief instruction, was the purchase-side structured-exchange bank `G07_PURCHASE_EDI_UBL_BIS3_GMVQ_MVQ_50_V1.00_DRAFT.md` (Author Cell P17, 50 questions); its hypotheses were read in full and this bank was authored to be the sender/revenue-side seam, not that bank with the direction reversed. No question here restates a purchase-side hypothesis with the transaction direction swapped; each targets a failure mode specific to being the party whose revenue depends on the counterparty's acceptance.
- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong, and the disconfirming observation is a distinct event for every question — no two questions share one failure event.
- No padding: 50 questions exist because they test 50 distinct material hypotheses at the seam. Depth requirement (55 shared + 48 module minimum = 103) is met once combined with the shared standard bank.
- This module carries one layer at the seam; the `LAYER` field is omitted throughout.
- Clean-room compliance: no vendor or product name, no technical identifier (model, table, field, method, XML ID, API path, standard or profile name), and no implementation shape appears anywhere in question text.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank. Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.
- Seam dimensions represented (GMVQ_BRIDGE_MODULE_RULE_V1.00 §3): timing (Q001-Q002, Q015, Q026-Q027, Q047), authority (Q003, Q008, Q023, Q025, Q028, Q036), partiality (Q004, Q029, Q032, Q049), ownership (Q005-Q006, Q009-Q012, Q017-Q018, Q020, Q024, Q031, Q033, Q035, Q037-Q038, Q040-Q042), lifecycle mismatch (Q007, Q014, Q019, Q021-Q022, Q030, Q034, Q039), reversal (Q013, Q046, Q048), ordering (Q016, Q043, Q045), error asymmetry (Q044), quantity and money (Q050).
- Coverage map: revenue posted ahead of confirmed customer acceptance Q001-Q004 · customer-specific mandatory reference gaps Q005-Q008 · silent transformation on the customer's side Q009-Q012 · correction/resend chain tied to revenue Q013-Q016 · legal instrument identity: exchanged form vs internal record Q017-Q020 · retention and reproducibility for audit defensibility Q021-Q024 · customer acknowledgment as a recognition gate Q025-Q028 · order-level vs invoice-level acceptance independence Q029-Q032 · customer-specific identifier mapping drift Q033-Q036 · per-customer channel/format configuration Q037-Q039 · selling company/branch identity vs revenue holder Q040-Q042 · concurrency and double-transmission risk Q043-Q045 · credit note / cancellation exchange discipline Q046-Q048 · partial invoicing reconciliation across the exchange Q049-Q050

## G08-SALE_EDI_UBL-Q001

```yaml
QID: G08-SALE_EDI_UBL-Q001
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Revenue is not treated as final and unqualified the moment an invoice is transmitted; a rejection notice
  received from the customer's system after internal posting reopens the transmitted invoice's status rather
  than being ignored because posting already occurred.
WHY_IT_MATTERS: >
  If posting is treated as the end of the story, a later rejection has nowhere to attach, and revenue believed
  earned may not reflect an invoice the customer's own system ever actually accepted.
DISCONFIRMING_OBSERVATION: >
  A rejection notice arrives for an invoice already posted to revenue, and the system shows no visible link
  between the rejection and the posted invoice, and the posted amount is left completely unaffected with no
  flag.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Transmit and post an invoice as revenue, then simulate a customer-system rejection notice arriving afterward,
  and inspect whether the posted invoice reflects any change of status.
```

## G08-SALE_EDI_UBL-Q002

```yaml
QID: G08-SALE_EDI_UBL-Q002
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The interval between transmitting an invoice and knowing whether the customer's system actually accepted it is
  treated as a defined risk window, with revenue recognized during that window distinguishable afterward from
  revenue recognized once acceptance is confirmed.
WHY_IT_MATTERS: >
  Without that distinction, the business cannot tell how much posted revenue actually rests on unconfirmed
  acceptance versus confirmed acceptance, which understates real exposure.
DISCONFIRMING_OBSERVATION: >
  There is no way to later query which posted invoices were posted before, versus after, confirmation was
  received from the customer's side.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Post several invoices at different points in the acceptance lifecycle, then attempt to distinguish, from the
  record alone, which were posted pre-acceptance.
```

## G08-SALE_EDI_UBL-Q003

```yaml
QID: G08-SALE_EDI_UBL-Q003
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A rejection received after posting does not automatically reverse the posted revenue entry on its own;
  reversal requires a deliberate decision by someone authorized to make it, since the underlying commercial
  dispute may still be unresolved.
WHY_IT_MATTERS: >
  Automatic silent reversal on any rejection would let a customer's system unilaterally alter the seller's
  books, but no reversal path at all leaves incorrect revenue standing indefinitely.
DISCONFIRMING_OBSERVATION: >
  A rejection notice causes the posted revenue entry to reverse automatically with no user action, or
  alternatively causes no prompt or visible task for anyone to act on at all.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Trigger a post-posting rejection and observe whether the revenue entry changes on its own or a deliberate
  action is required, and by whom.
```

## G08-SALE_EDI_UBL-Q004

```yaml
QID: G08-SALE_EDI_UBL-Q004
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rejection arriving after a customer has already paid, in part or in full, against the rejected invoice is
  flagged as materially different from a rejection on an invoice with nothing yet collected, since unwinding
  paid revenue is a different action than unwinding merely posted revenue.
WHY_IT_MATTERS: >
  Treating a paid-and-rejected invoice the same as an unpaid one risks either improperly holding a customer's
  money or improperly reversing revenue that has already actually been collected.
DISCONFIRMING_OBSERVATION: >
  A rejection on an invoice with recorded payment is presented and handled identically to a rejection on an
  invoice with no payment recorded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Record a payment against a transmitted invoice, then simulate a rejection, and compare the resulting handling
  to a rejection on an unpaid invoice.
```

## G08-SALE_EDI_UBL-Q005

```yaml
QID: G08-SALE_EDI_UBL-Q005
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A reference or identifier that a specific customer's system requires, but that is not a universal requirement
  of the exchange format itself, is captured as a property of that customer relationship rather than assumed to
  be the same for every customer.
WHY_IT_MATTERS: >
  If the requirement is treated as universal, an order for a customer with no such requirement gets an
  unnecessary block, and an order for a customer who does require it gets no warning at all.
DISCONFIRMING_OBSERVATION: >
  Two different customers with different reference requirements produce the identical validation outcome for the
  same order content, one of them wrongly.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure two customer relationships with different required references, and attempt to send the same order
  content under each.
```

## G08-SALE_EDI_UBL-Q006

```yaml
QID: G08-SALE_EDI_UBL-Q006
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order missing a reference that a specific customer requires is held before transmission with a specific,
  attributable reason, rather than being sent and left to fail or be silently accepted without it on the
  customer's side.
WHY_IT_MATTERS: >
  A generic send-and-hope approach shifts discovery of the gap to a rejection days later, after revenue may
  already be recognized.
DISCONFIRMING_OBSERVATION: >
  An order lacking a known customer-specific required reference transmits successfully with no warning, and any
  resulting rejection cannot be traced back to the missing reference.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Attempt to transmit an order for a customer with a known required reference, deliberately leaving that
  reference blank, and observe whether the gap is caught before send.
```

## G08-SALE_EDI_UBL-Q007

```yaml
QID: G08-SALE_EDI_UBL-Q007
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a customer's own required reference changes (renegotiated, reissued) mid-relationship, orders already
  transmitted under the old reference remain identifiable and traceable, rather than becoming orphaned once the
  requirement changes.
WHY_IT_MATTERS: >
  Losing traceability on historical orders after a reference scheme changes undermines dispute resolution and
  reconciliation with that customer for everything sent before the change.
DISCONFIRMING_OBSERVATION: >
  After a customer's required reference scheme changes, a previously transmitted order under the old scheme can
  no longer be located by that old reference.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transmit an order under one customer reference scheme, change the customer's required scheme, then attempt to
  retrieve the earlier order by its original reference.
```

## G08-SALE_EDI_UBL-Q008

```yaml
QID: G08-SALE_EDI_UBL-Q008
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Responsibility for knowing and maintaining a specific customer's required references sits with a defined role,
  not with whoever happens to be entering the order, so the requirement is not lost when personnel handling that
  account changes.
WHY_IT_MATTERS: >
  An informally-known customer requirement that lives only in one person's memory disappears the moment that
  person is unavailable, reintroducing the failure the requirement was meant to prevent.
DISCONFIRMING_OBSERVATION: >
  A customer's required reference is only ever entered correctly when one specific person happens to process the
  order, and is missed whenever someone else does.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Have a different, otherwise-authorized user process an order for a customer with a known required reference
  and observe whether the requirement is surfaced to them.
```

## G08-SALE_EDI_UBL-Q009

```yaml
QID: G08-SALE_EDI_UBL-Q009
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The system distinguishes 'the customer's system reported acceptance' from 'the customer's system reported
  acceptance of content identical to what was intended', since transport- or counterparty-level acceptance says
  nothing about whether the content was altered on arrival.
WHY_IT_MATTERS: >
  Treating any acceptance as proof of faithful receipt hides the case where what the customer's system actually
  recorded diverges from what was sent, without anyone knowing.
DISCONFIRMING_OBSERVATION: >
  An accepted document with content demonstrably altered on arrival, for instance a value that changed range or
  precision, shows the same acceptance status as one received unchanged.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Simulate an accepted document later shown to differ from the transmitted content, and compare its recorded
  status to an accepted, unaltered document.
```

## G08-SALE_EDI_UBL-Q010

```yaml
QID: G08-SALE_EDI_UBL-Q010
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the customer's system provides any feedback describing how it actually interpreted the received content,
  such as an item or reference it resolved differently, that feedback is retained and linked to the specific
  document sent, not discarded once a bare acceptance is recorded.
WHY_IT_MATTERS: >
  That feedback is the only signal available that something was reinterpreted on the far side; discarding it
  removes the one chance to catch a silent divergence before it causes a dispute.
DISCONFIRMING_OBSERVATION: >
  Interpretive feedback returned by the customer's system is not retrievable after the fact, even though a bare
  acceptance status is.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Receive interpretive feedback alongside an acceptance and attempt to retrieve it later from the record of that
  document.
```

## G08-SALE_EDI_UBL-Q011

```yaml
QID: G08-SALE_EDI_UBL-Q011
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A dispute over what was actually agreed is resolved by comparing what is held as sent against whatever the
  customer can independently produce, rather than one side's copy being assumed correct by default within the
  seller's own system.
WHY_IT_MATTERS: >
  Assuming the seller's own retained copy is automatically the truth removes the incentive to investigate a
  genuine divergence and can misrepresent a real dispute as already settled.
DISCONFIRMING_OBSERVATION: >
  The system presents its own retained transmitted content as the undisputed record of what the customer
  received, with no accommodation for the customer producing a differing copy.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Raise a dispute referencing a customer-held version of a document that differs from the retained transmitted
  copy, and observe how the disagreement is represented.
```

## G08-SALE_EDI_UBL-Q012

```yaml
QID: G08-SALE_EDI_UBL-Q012
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A pattern of repeated silent-transformation feedback from the same customer relationship is visible in
  aggregate, not only as isolated per-document events, so a systemic mismatch with a specific customer's system
  can be recognized rather than rediscovered document by document.
WHY_IT_MATTERS: >
  Without an aggregate view, a recurring, correctable mismatch with one customer looks like a string of
  unrelated one-off surprises instead of a pattern worth fixing at the source.
DISCONFIRMING_OBSERVATION: >
  Several documents to the same customer each carry transformation feedback, but nothing in the system groups or
  surfaces them together as a pattern tied to that customer.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate transformation feedback across multiple documents to one customer and check whether the system can
  present them as a related group.
```

## G08-SALE_EDI_UBL-Q013

```yaml
QID: G08-SALE_EDI_UBL-Q013
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an already-transmitted invoice must be corrected, revenue recognized against the original is reconciled
  to the corrected version through a defined step, rather than the original amount continuing to stand alongside
  a separately transmitted correction with no link drawn between the two.
WHY_IT_MATTERS: >
  An uncorrected mismatch between what was recognized and what was actually corrected overstates or understates
  revenue without anyone noticing.
DISCONFIRMING_OBSERVATION: >
  A corrected invoice is transmitted, but the originally posted revenue amount is left unchanged with no task,
  flag, or link connecting it to the correction.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Issue a correction to an already-posted, already-transmitted invoice and inspect whether the posted revenue
  reflects or references the correction.
```

## G08-SALE_EDI_UBL-Q014

```yaml
QID: G08-SALE_EDI_UBL-Q014
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Once a correction has been transmitted, the original document is marked as superseded in a way visible to
  anyone later reviewing it, rather than the original appearing as though it were still the live, current
  version.
WHY_IT_MATTERS: >
  A reviewer or auditor who encounters only the original, with no indication a correction exists, will draw
  conclusions from a document that is no longer the operative one.
DISCONFIRMING_OBSERVATION: >
  Viewing the original transmitted invoice after a correction has gone out gives no indication that a correction
  exists or what it changed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transmit a correction to a prior invoice, then open the original invoice's record and check whether its
  superseded status is visible.
```

## G08-SALE_EDI_UBL-Q015

```yaml
QID: G08-SALE_EDI_UBL-Q015
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Whether the customer's system has actually replaced its own held copy with the correction, as opposed to
  merely having received it, is tracked separately, since transmission of a correction does not guarantee the
  customer's side has resolved which version it now treats as current.
WHY_IT_MATTERS: >
  Assuming the correction took effect on the customer's side without confirmation risks both parties acting on
  different totals indefinitely.
DISCONFIRMING_OBSERVATION: >
  A correction is transmitted and treated as fully resolved with no distinction from confirmation that the
  customer's system actually adopted it.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Transmit a correction and check whether the record distinguishes 'correction sent' from 'correction confirmed
  accepted by the customer's system.'
```

## G08-SALE_EDI_UBL-Q016

```yaml
QID: G08-SALE_EDI_UBL-Q016
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Issuing a second correction to the same original document produces a chain that can be followed in sequence,
  original then each correction in turn, rather than each new correction only referencing the immediately
  original document with the intermediate correction lost from the chain.
WHY_IT_MATTERS: >
  A broken chain makes it impossible to reconstruct which values were actually in force at any given moment,
  which matters directly for a revenue or tax dispute.
DISCONFIRMING_OBSERVATION: >
  A second correction to the same invoice cannot be traced back through the first correction to the original in
  one connected sequence.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue two successive corrections to the same original invoice and attempt to reconstruct the full sequence
  from the record.
```

## G08-SALE_EDI_UBL-Q017

```yaml
QID: G08-SALE_EDI_UBL-Q017
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where the exchanged document and the internal record of the same invoice differ in any respect, the system
  identifies which one is treated as the legally operative instrument for that customer relationship, rather
  than leaving the question unanswered until a dispute forces it.
WHY_IT_MATTERS: >
  Not knowing in advance which version governs turns every discrepancy into an ad hoc argument instead of a
  resolved policy question.
DISCONFIRMING_OBSERVATION: >
  Asked which of two differing versions of the same invoice is authoritative, the system and the process around
  it have no defined answer.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a case where the exchanged document and internal record diverge and check whether a defined authority
  rule resolves which one governs.
```

## G08-SALE_EDI_UBL-Q018

```yaml
QID: G08-SALE_EDI_UBL-Q018
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Reporting used for tax or statutory purposes is built from whichever version is designated the legal
  instrument, not from whichever version happens to be more convenient to query at reporting time.
WHY_IT_MATTERS: >
  Reporting off the wrong version could misstate a tax position even when the correct legal document was in fact
  issued and retained.
DISCONFIRMING_OBSERVATION: >
  A tax or statutory report is generated from the internal record's figures in a case where the exchanged
  document was designated as legally authoritative and the two differ.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create a divergence between the two versions where the exchanged document is authoritative, then generate a
  downstream report and check which figures it used.
```

## G08-SALE_EDI_UBL-Q019

```yaml
QID: G08-SALE_EDI_UBL-Q019
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change made only to the internal record, with no corresponding retransmission to the customer, is visibly
  flagged as not reflected in what the customer actually holds, rather than presented as though it were already
  communicated.
WHY_IT_MATTERS: >
  A user editing the internal record without realizing nothing was resent could reasonably but wrongly believe
  the customer has the updated figures.
DISCONFIRMING_OBSERVATION: >
  An internal-only edit to an already-transmitted invoice displays with no indication that the customer's held
  copy still reflects the earlier, untransmitted state.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Edit an already-transmitted invoice's internal record without retransmitting, then view the document and check
  for any indication of the gap.
```

## G08-SALE_EDI_UBL-Q020

```yaml
QID: G08-SALE_EDI_UBL-Q020
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  For a customer relationship where no structured exchange is configured at all, the internal record is treated
  as the legal instrument by default, so the authority question only becomes live where an actual exchange
  exists.
WHY_IT_MATTERS: >
  Forcing an authority determination even where there is nothing to compare against would create false ambiguity
  where none exists.
DISCONFIRMING_OBSERVATION: >
  A customer with no configured structured exchange still triggers a prompt or hold asking which version is
  authoritative.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Issue an invoice to a customer with no structured exchange configured and confirm no authority ambiguity is
  raised.
```

## G08-SALE_EDI_UBL-Q021

```yaml
QID: G08-SALE_EDI_UBL-Q021
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The exact content of a transmitted invoice, as actually sent, can be reproduced unchanged at any later point,
  independent of whatever the order or invoice record has since become, for as long as the applicable retention
  period runs.
WHY_IT_MATTERS: >
  An auditor or tax authority needs to see what was actually issued at the time, not a reconstruction based on
  the document's current state.
DISCONFIRMING_OBSERVATION: >
  Attempting to reproduce the exact content of a transmitted invoice months later returns the document's current
  state rather than the content actually sent at transmission time.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transmit an invoice, materially alter its internal record afterward, then attempt to retrieve the exact
  originally transmitted content.
```

## G08-SALE_EDI_UBL-Q022

```yaml
QID: G08-SALE_EDI_UBL-Q022
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: R4-remediation
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the structured exchange format's version is upgraded, a previously transmitted record
  retained under the older format version can still be correctly retrieved and read back as
  originally transmitted, rather than becoming unreadable or being silently reinterpreted under
  the newer version's rules.
WHY_IT_MATTERS: >
  A retained record silently reinterpreted under a newer format version's rules no longer matches
  what was actually transmitted at the time, destroying it as reliable evidence of that exchange.
DISCONFIRMING_OBSERVATION: >
  A record transmitted and retained under an older format version displays or exports differently
  after a format-version upgrade than it did when first retained, with no indication that its
  original format version differs from the current one.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Transmit and retain a record under one format version, apply a supported upgrade to a newer
  format version, then retrieve the same retained record and compare its content and stated
  format version against what was originally retained.
```

## G08-SALE_EDI_UBL-Q023

```yaml
QID: G08-SALE_EDI_UBL-Q023
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Retrieving the historical exact content of a transmitted invoice for audit purposes does not require broader
  access than an auditor would already need to review the invoice itself, and any additional requirement is a
  deliberate, documented control rather than an incidental barrier.
WHY_IT_MATTERS: >
  An accidental access barrier at audit time can make a business appear unable to produce evidence it in fact
  retains.
DISCONFIRMING_OBSERVATION: >
  A user authorized to review invoices generally is unable to retrieve the exact historically transmitted
  content for one, with no documented reason for the extra restriction.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user with ordinary invoice-review access, attempt to retrieve the historical transmitted content of a
  past invoice.
```

## G08-SALE_EDI_UBL-Q024

```yaml
QID: G08-SALE_EDI_UBL-Q024
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The retained transmitted content carries enough context, such as which customer, which channel, and what
  outcome was received back, to stand as usable evidence on its own, rather than being an isolated file that
  requires cross-referencing several other records to make sense of.
WHY_IT_MATTERS: >
  Evidence that cannot be understood without extensive cross-referencing is materially weaker in a dispute or
  audit than a self-contained record.
DISCONFIRMING_OBSERVATION: >
  The retained transmitted content, viewed alone, gives no indication of which customer or channel it relates to
  or what result it received.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Retrieve a retained transmitted invoice in isolation and check whether its context is legible without
  consulting other records.
```

## G08-SALE_EDI_UBL-Q025

```yaml
QID: G08-SALE_EDI_UBL-Q025
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether customer-side acknowledgment is required before revenue may be recognized is a defined, configurable
  policy rather than an implicit assumption baked into when the invoice happens to post.
WHY_IT_MATTERS: >
  Leaving this implicit means different people can each assume a different rule is in force, and no one can
  verify which one the business is actually operating under.
DISCONFIRMING_OBSERVATION: >
  Asked whether acknowledgment gates recognition, no configuration or documented setting exists that answers the
  question either way.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Inspect the system configuration governing revenue posting timing relative to structured-exchange
  acknowledgment.
```

## G08-SALE_EDI_UBL-Q026

```yaml
QID: G08-SALE_EDI_UBL-Q026
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where acknowledgment is configured as a gate, revenue posting is actually held until that acknowledgment is
  received, rather than the gate existing as configuration with no enforcement behind it.
WHY_IT_MATTERS: >
  A configured-but-unenforced gate is worse than no gate, because it gives false assurance that recognition is
  controlled when it is not.
DISCONFIRMING_OBSERVATION: >
  With the acknowledgment gate enabled, revenue posts before any acknowledgment has been received.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Enable the acknowledgment-gate configuration, transmit an invoice, and attempt to post revenue before an
  acknowledgment arrives.
```

## G08-SALE_EDI_UBL-Q027

```yaml
QID: G08-SALE_EDI_UBL-Q027
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An invoice that never receives acknowledgment within a defined period is surfaced as overdue for a decision,
  rather than sitting indefinitely in an unrecognized, unresolved state with no one prompted to act.
WHY_IT_MATTERS: >
  An invoice stuck forever in limbo neither contributes to reported revenue nor gets resolved, quietly
  understating the business's position.
DISCONFIRMING_OBSERVATION: >
  A gated invoice that never receives acknowledgment remains unflagged and unrecognized indefinitely with no
  prompt to anyone.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transmit a gated invoice, let the acknowledgment window elapse with no response, and check whether it is
  surfaced for action.
```

## G08-SALE_EDI_UBL-Q028

```yaml
QID: G08-SALE_EDI_UBL-Q028
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Overriding the acknowledgment gate to recognize revenue without waiting for acknowledgment, where that
  override exists, requires a distinct authorization beyond ordinary invoice posting.
WHY_IT_MATTERS: >
  If anyone who can post an invoice can also silently bypass the gate, the gate provides no real control at all.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary invoice-posting permission is able to override the acknowledgment gate and recognize
  revenue anyway.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with ordinary posting permission only, attempt to override the acknowledgment gate on a gated
  invoice.
```

## G08-SALE_EDI_UBL-Q029

```yaml
QID: G08-SALE_EDI_UBL-Q029
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The customer's acceptance of the exchanged order and the customer's acceptance of the exchanged invoice for
  that order are tracked as two separate states, since one can be accepted while the other is rejected.
WHY_IT_MATTERS: >
  Collapsing the two into one status hides the specific case where, for instance, the order was fine but the
  invoice itself was not.
DISCONFIRMING_OBSERVATION: >
  The system exposes only a single combined acceptance status covering both the order and the invoice, with no
  way to see them independently.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Simulate an accepted order followed by a rejected invoice for the same transaction, and check whether both
  states are visible independently.
```

## G08-SALE_EDI_UBL-Q030

```yaml
QID: G08-SALE_EDI_UBL-Q030
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An order rejected by the customer's system does not prevent an invoice from later being generated and
  transmitted for that same order without a deliberate decision to proceed despite the rejection.
WHY_IT_MATTERS: >
  Automatically invoicing against an order the customer's own system never accepted risks issuing a legal
  document for a transaction the customer disputes exists.
DISCONFIRMING_OBSERVATION: >
  An invoice is generated and transmitted for an order whose own exchange was rejected, with no warning or block
  referencing that rejection.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Reject an order at the exchange level, then attempt to generate and transmit an invoice against it.
```

## G08-SALE_EDI_UBL-Q031

```yaml
QID: G08-SALE_EDI_UBL-Q031
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the order was never exchanged as a structured document at all and only the invoice is, the invoice's
  acceptance state is not confused with, or assumed to inherit, any order-level state that was never
  established.
WHY_IT_MATTERS: >
  Assuming an order-level acceptance that never happened could mask the fact that only the invoice was ever
  actually validated by the customer's system.
DISCONFIRMING_OBSERVATION: >
  An invoice-only exchange displays an order-level acceptance status despite no order having ever been
  exchanged.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Configure a customer relationship that exchanges invoices only, and check what order-level status, if any, is
  displayed.
```

## G08-SALE_EDI_UBL-Q032

```yaml
QID: G08-SALE_EDI_UBL-Q032
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A summary view of exchange status for an order presents order-level and invoice-level status as clearly
  distinct entries, not merged into one status that could be read as covering both.
WHY_IT_MATTERS: >
  A merged status inevitably gets misread by someone relying on it to decide whether it is safe to proceed.
DISCONFIRMING_OBSERVATION: >
  A summary view shows one status field for an order-and-invoice pair where the two levels actually disagree.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a disagreement between order-level and invoice-level exchange status and inspect how a summary view
  represents it.
```

## G08-SALE_EDI_UBL-Q033

```yaml
QID: G08-SALE_EDI_UBL-Q033
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A mapping between the seller's own item or reference identifiers and a specific customer's own required
  identifiers is maintained as an explicit, per-customer record, not inferred freshly from matching text or
  codes at the moment of each send.
WHY_IT_MATTERS: >
  A best-effort match redone every time can silently produce a different mapping result as data changes, without
  anyone deciding that it should.
DISCONFIRMING_OBSERVATION: >
  The same internal item maps to a different customer-facing identifier on two separate transmissions to the
  same customer with no change having been made to the mapping.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Transmit the same item to the same customer twice, with unrelated data changes in between, and compare the
  customer-facing identifier used each time.
```

## G08-SALE_EDI_UBL-Q034

```yaml
QID: G08-SALE_EDI_UBL-Q034
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a customer's own required identifier for an item changes, orders already transmitted under the prior
  identifier remain correctly attributable to that item historically, rather than the change rewriting how past
  transmissions are interpreted.
WHY_IT_MATTERS: >
  Rewriting history to match a new mapping would make past transmitted documents describe something other than
  what was actually sent at the time.
DISCONFIRMING_OBSERVATION: >
  After a customer's required identifier for an item changes, a previously transmitted document under the old
  identifier is now shown, or interpreted, as if it used the new one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transmit a document using one customer-required identifier, change the mapping, then re-inspect the historical
  document.
```

## G08-SALE_EDI_UBL-Q035

```yaml
QID: G08-SALE_EDI_UBL-Q035
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An item with no defined mapping to a specific customer's required identifier scheme blocks transmission for
  that customer with a specific, attributable reason, rather than being sent under the seller's own internal
  identifier as a fallback.
WHY_IT_MATTERS: >
  Silently substituting the seller's own identifier for a customer-specific one produces a document the
  customer's system may not be able to resolve at all.
DISCONFIRMING_OBSERVATION: >
  An item lacking a customer-specific identifier mapping still transmits successfully under the internal
  identifier with no warning.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to transmit an order containing an item with no defined mapping for that customer, and observe the
  outcome.
```

## G08-SALE_EDI_UBL-Q036

```yaml
QID: G08-SALE_EDI_UBL-Q036
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Maintaining or changing a customer-specific identifier mapping requires a level of authorization distinct from
  ordinary order entry, since an incorrect mapping can misdirect every future transmission to that customer.
WHY_IT_MATTERS: >
  If anyone entering an order can casually alter the mapping, a single mistake propagates silently into every
  subsequent document sent to that customer.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary order-entry permission is able to alter a customer's identifier mapping.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with ordinary order-entry permission, attempt to change a customer's identifier mapping.
```

## G08-SALE_EDI_UBL-Q037

```yaml
QID: G08-SALE_EDI_UBL-Q037
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A document is transmitted through the specific channel and format configured for that particular customer, not
  a default channel applied uniformly regardless of which customer it is going to.
WHY_IT_MATTERS: >
  Sending through the wrong channel or format for a customer whose system expects a specific one produces a
  document that customer's system may not process at all.
DISCONFIRMING_OBSERVATION: >
  An order for a customer configured to use a specific channel is transmitted through a different, default
  channel instead.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Configure a customer with a non-default channel, transmit an order, and verify which channel was actually
  used.
```

## G08-SALE_EDI_UBL-Q038

```yaml
QID: G08-SALE_EDI_UBL-Q038
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a customer's channel or format configuration is incomplete or missing entirely, transmission for that
  customer is blocked with a specific reason rather than silently falling back to a generic default that the
  customer's system may reject.
WHY_IT_MATTERS: >
  A silent fallback converts a configuration gap into a customer-facing failure discovered only after the fact.
DISCONFIRMING_OBSERVATION: >
  An order for a customer with incomplete channel configuration transmits anyway under a generic default with no
  warning.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Remove part of a customer's channel configuration, then attempt to transmit an order for that customer.
```

## G08-SALE_EDI_UBL-Q039

```yaml
QID: G08-SALE_EDI_UBL-Q039
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to a customer's channel or format configuration does not retroactively alter how documents already
  transmitted under the prior configuration are represented in the retained record.
WHY_IT_MATTERS: >
  Retroactively reinterpreting past transmissions under a new configuration would misstate what channel or
  format was actually used at the time.
DISCONFIRMING_OBSERVATION: >
  After a customer's channel configuration changes, a previously transmitted document's retained record now
  shows the new configuration instead of the one actually used.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transmit a document under one channel configuration, change the configuration, then inspect the retained
  record of the earlier document.
```

## G08-SALE_EDI_UBL-Q040

```yaml
QID: G08-SALE_EDI_UBL-Q040
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The legal entity identity presented to the customer on the exchanged document is determined by which company
  actually holds the revenue for that sale, and is never a separate, unrelated identity chosen for convenience.
WHY_IT_MATTERS: >
  A mismatch between the entity the customer believes it transacted with and the entity actually recognizing the
  revenue creates both a legal and an accounting inconsistency.
DISCONFIRMING_OBSERVATION: >
  The exchanged document presents a different company's identity than the company under which the sale's revenue
  is recorded.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure a sale where the selling and invoicing companies could plausibly differ, transmit the document, and
  compare identities.
```

## G08-SALE_EDI_UBL-Q041

```yaml
QID: G08-SALE_EDI_UBL-Q041
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where a sale is contracted by one company but fulfilled through another company's branch or facility, the
  exchanged document's identity follows the contracting company, not the fulfilling one, unless a defined
  arrangement says otherwise.
WHY_IT_MATTERS: >
  The customer's contractual relationship, and therefore their expectation of who is legally obligated to them,
  runs with the contracting company.
DISCONFIRMING_OBSERVATION: >
  A sale contracted by one company but fulfilled by another produces an exchanged document under the fulfilling
  company's identity with no defined arrangement authorizing that.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a sale with distinct contracting and fulfilling companies with no special arrangement, and inspect
  which identity the exchanged document carries.
```

## G08-SALE_EDI_UBL-Q042

```yaml
QID: G08-SALE_EDI_UBL-Q042
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a company is not fully configured with what is needed to transmit under its own identity, transmission
  for its sales is blocked rather than falling back to another company's identity to get the document sent
  regardless.
WHY_IT_MATTERS: >
  Sending under a substitute identity to work around a configuration gap creates a document that misrepresents
  who the customer is actually transacting with.
DISCONFIRMING_OBSERVATION: >
  A company missing part of its exchange identity configuration still has documents transmitted under a
  different company's identity as a fallback.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Remove part of one company's exchange identity configuration and attempt to transmit a document for a sale
  under that company.
```

## G08-SALE_EDI_UBL-Q043

```yaml
QID: G08-SALE_EDI_UBL-Q043
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Two nearly simultaneous attempts to transmit the same invoice, whether both manual, both automated, or one of
  each, do not both result in a live transmission and a live posted revenue entry.
WHY_IT_MATTERS: >
  A duplicate live transmission risks the customer receiving two demands for the same amount and the seller
  recognizing the revenue twice.
DISCONFIRMING_OBSERVATION: >
  Triggering transmission for the same invoice from two near-simultaneous sources produces two live
  transmissions and two revenue postings.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Trigger transmission for the same invoice from two sources at nearly the same moment and observe whether both
  proceed.
```

## G08-SALE_EDI_UBL-Q044

```yaml
QID: G08-SALE_EDI_UBL-Q044
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If marking an invoice as transmitted and actually posting its revenue are not a single atomic action, a
  failure between the two steps does not leave the invoice recorded as transmitted-and-recognized when only one
  of the two actually completed.
WHY_IT_MATTERS: >
  A partial failure that leaves a false combined state is worse than either step failing cleanly on its own,
  because it looks fully successful.
DISCONFIRMING_OBSERVATION: >
  A simulated failure between marking transmission and posting revenue leaves the invoice showing both as
  complete when only one occurred.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Simulate a failure occurring between the transmission-marking step and the revenue-posting step, and inspect
  the resulting invoice state.
```

## G08-SALE_EDI_UBL-Q045

```yaml
QID: G08-SALE_EDI_UBL-Q045
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A scheduled background process that periodically attempts to transmit outstanding invoices does not transmit
  an invoice a second time because an earlier attempt's success was not yet recorded when the background pass
  ran.
WHY_IT_MATTERS: >
  A background retry mechanism unaware of an in-flight or just-completed send is a direct path to an unintended
  duplicate transmission.
DISCONFIRMING_OBSERVATION: >
  A background transmission pass sends an invoice again shortly after a manual transmission succeeded, because
  the success had not yet been recorded when the pass ran.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Manually transmit an invoice immediately before a scheduled background transmission pass runs, and observe
  whether it is sent again.
```

## G08-SALE_EDI_UBL-Q046

```yaml
QID: G08-SALE_EDI_UBL-Q046
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A cancellation or credit note issued internally against an already-transmitted invoice generates its own
  distinct exchanged notice to the customer, where the exchange channel supports one, rather than existing only
  as an internal reversal with nothing communicated outward.
WHY_IT_MATTERS: >
  A customer holding the original invoice with no notice of its cancellation may reasonably continue to treat
  the original amount as owed.
DISCONFIRMING_OBSERVATION: >
  An internal credit note is posted against a transmitted invoice with no corresponding exchanged document
  generated for the customer.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Issue an internal credit note against a transmitted invoice and check whether a corresponding exchanged
  document is generated.
```

## G08-SALE_EDI_UBL-Q047

```yaml
QID: G08-SALE_EDI_UBL-Q047
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Revenue reversal from a credit note is not treated as complete purely on internal posting; where the credit
  note itself requires exchange and acknowledgment, the same acceptance-tracking discipline applied to invoices
  applies to the credit note.
WHY_IT_MATTERS: >
  Treating credit notes as exempt from the same acceptance discipline as invoices creates an inconsistency where
  the error could be just as large as an invoice error, with weaker controls.
DISCONFIRMING_OBSERVATION: >
  A credit note posts and reverses revenue instantly with no acceptance-tracking behavior, even though the
  customer relationship requires exchange for such documents.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Issue a credit note for a customer relationship requiring structured exchange of credit notes, and check
  whether the same acceptance-tracking applies.
```

## G08-SALE_EDI_UBL-Q048

```yaml
QID: G08-SALE_EDI_UBL-Q048
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rejected credit note is distinguishable from an accepted one in the same way a rejected invoice is, so that
  a customer disputing the reversal itself is visible rather than assumed resolved.
WHY_IT_MATTERS: >
  A silently-accepted assumption on credit notes specifically would let a genuinely disputed reversal pass
  unnoticed.
DISCONFIRMING_OBSERVATION: >
  A customer-side rejection of a transmitted credit note produces no different outcome than an accepted one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Simulate a customer-side rejection of a transmitted credit note and compare the resulting state to an accepted
  credit note.
```

## G08-SALE_EDI_UBL-Q049

```yaml
QID: G08-SALE_EDI_UBL-Q049
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where an order is invoiced in more than one partial invoice, each partial invoice is exchanged and tracked for
  acceptance independently, rather than the whole order's exchange status being judged by only the first or only
  the last partial invoice sent.
WHY_IT_MATTERS: >
  Treating the group as one status hides the specific case where an earlier partial invoice was rejected while a
  later one was accepted, or vice versa.
DISCONFIRMING_OBSERVATION: >
  An order invoiced through several partial invoices shows one combined exchange status that does not reflect
  that one specific partial invoice was rejected.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Invoice an order in two partial invoices, reject one and accept the other, and inspect how the order's overall
  exchange status is presented.
```

## G08-SALE_EDI_UBL-Q050

```yaml
QID: G08-SALE_EDI_UBL-Q050
MODULE: sale_edi_ubl
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The cumulative total across all partial invoices actually transmitted for an order can be reconciled against
  the order's own total, so an omitted or duplicated partial invoice would be detectable rather than passing
  unnoticed inside an aggregate figure.
WHY_IT_MATTERS: >
  Without reconciliation, a missed or doubled partial invoice changes total recognized revenue with no mechanism
  ever likely to catch it.
DISCONFIRMING_OBSERVATION: >
  The sum of transmitted partial invoices for an order cannot be compared against the order's total through any
  available view or check.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Transmit several partial invoices against one order and attempt to reconcile their total against the order's
  own total.
```

---
## GMVQ Internal QA Checklist

- [x] 50 distinct MVQ records; no padding — every record targets a distinct seam hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`, and no two records share one failure event.
- [x] Bridge Module Rule seam test applied to every question: removing the second capability and using the base order and that capability apart would make the question meaningless. No question restates base-module (`sale`) behavior with the bridge's name attached.
- [x] Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$DIR"/*.md | sort` was run before writing a single question. At authoring time G08_SALES held no other banks on disk. The sibling bridge bank actually checked, per this module's specific brief instruction, was the purchase-side structured-exchange bank `G07_PURCHASE_EDI_UBL_BIS3_GMVQ_MVQ_50_V1.00_DRAFT.md` (Author Cell P17, 50 questions); its hypotheses were read in full and this bank was authored to be the sender/revenue-side seam, not that bank with the direction reversed. No question here restates a purchase-side hypothesis with the transaction direction swapped; each targets a failure mode specific to being the party whose revenue depends on the counterparty's acceptance.
- [x] Questions are behavioral and source-neutral; no vendor/product/standard name, technical identifier, or the module's own metadata name appears in question text.
- [x] Seam dimensions represented: timing (Q001-Q002, Q015, Q026-Q027, Q047), authority (Q003, Q008, Q023, Q025, Q028, Q036), partiality (Q004, Q029, Q032, Q049), ownership (Q005-Q006, Q009-Q012, Q017-Q018, Q020, Q024, Q031, Q033, Q035, Q037-Q038, Q040-Q042), lifecycle mismatch (Q007, Q014, Q019, Q021-Q022, Q030, Q034, Q039), reversal (Q013, Q046, Q048), ordering (Q016, Q043, Q045), error asymmetry (Q044), quantity and money (Q050).
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
