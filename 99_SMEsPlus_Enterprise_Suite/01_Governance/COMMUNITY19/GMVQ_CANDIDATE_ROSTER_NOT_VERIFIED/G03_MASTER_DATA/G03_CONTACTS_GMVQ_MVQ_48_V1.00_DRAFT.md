# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / contacts Module MVQ Bank

**Document ID:** GMVQ-G03-CONTACTS-MVQ48-V1.00
**Group:** G03 MASTER_DATA
**Module Metadata:** `contacts`
**Wave:** W1
**Author Cell:** TEAM 15 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank provides the module-specific MVQ set for the business-partner record: companies,
individuals, child contacts, addresses, and the parent/child relationship. This is the single
most consequential master record in the system, so the set targets it hard: merge of two
records that both carry posted history, balances, and open documents; what happens to
receivable/payable attribution on merge and on later change; child promotion and re-parenting;
address propagation and what must never propagate; archiving with open documents; duplicate
detection and the cost of a false merge; per-company override on a shared record; and
auditability of any change that alters a financial outcome.

The question text is source-neutral and does not expose vendor names, model names, field
names, method names, XML IDs, or API shapes.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material hypothesis.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no coverage is claimed from this bank.
- Clean Room: generic ERP domain knowledge only; question text was drafted without opening
  any reference or vendor source tree.
- `LAYER: BASE` marks the record's structural/data-foundation questions; `LAYER: PROCESS`
  marks its financial and lifecycle-event questions.

## G03-CONTACTS-Q001

```yaml
QID: G03-CONTACTS-Q001
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Fields and behaviors that make sense only for an organization (such as the ability to hold
  child contacts) are not silently available, in a way that produces meaningful data, on a
  record representing an individual person.
WHY_IT_MATTERS: >
  Organization-only structure appearing on a personal record produces confusing, meaningless
  relationships that pollute reporting.
DISCONFIRMING_OBSERVATION: >
  An individual-type record is able to hold child contacts in a way that is later treated the
  same as an organization's child contacts by downstream logic.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Create a record marked as an individual and attempt to attach a child contact to it, then
  check how a downstream process treats that relationship.
```

## G03-CONTACTS-Q002

```yaml
QID: G03-CONTACTS-Q002
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A newly created child contact under a company inherits defaults explicitly intended to be
  shared (such as the parent's primary address), not the parent's private commercial terms
  without an explicit rule saying they should propagate.
WHY_IT_MATTERS: >
  Over-broad inheritance can silently grant a new child contact terms (credit, pricing) that
  were never approved for it specifically.
DISCONFIRMING_OBSERVATION: >
  A newly created child contact carries the parent's commercial terms (such as credit limit or
  payment terms) with no explicit rule or action that authorized that inheritance.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set distinct commercial terms on a parent company, create a new child contact under it, and
  inspect what that child inherits by default.
```

## G03-CONTACTS-Q003

```yaml
QID: G03-CONTACTS-Q003
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Updating a company's primary address propagates to a child contact's address only when that
  child has not been given its own distinct address.
WHY_IT_MATTERS: >
  Overwriting a child's deliberately distinct address because the parent changed defeats the
  purpose of allowing a distinct child address at all.
DISCONFIRMING_OBSERVATION: >
  Updating the parent's address changes the address of a child contact that already has its
  own distinct, previously set address.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Give a child contact its own distinct address different from its parent, then change the
  parent's address and check whether the child's address changed.
```

## G03-CONTACTS-Q004

```yaml
QID: G03-CONTACTS-Q004
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  A change to the parent's accounting attribution (such as which receivable account applies)
  does not automatically overwrite an accounting attribution the child was explicitly given on
  its own.
WHY_IT_MATTERS: >
  Silent propagation of financial attribution can redirect a child's transactions to the wrong
  account without anyone deciding that should happen.
DISCONFIRMING_OBSERVATION: >
  Changing the parent company's accounting attribution changes a child contact's own,
  separately configured accounting attribution.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Give a child contact its own distinct accounting attribution different from its parent, then
  change the parent's attribution and check the child's value afterward.
```

## G03-CONTACTS-Q005

```yaml
QID: G03-CONTACTS-Q005
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: BASE
HYPOTHESIS: >
  Converting a child contact into an independent company-level record preserves that record's
  prior transactional history under its own identity.
WHY_IT_MATTERS: >
  Losing history at the moment of promotion breaks continuity for a customer relationship that
  is simply growing in structure, not starting over.
DISCONFIRMING_OBSERVATION: >
  After a child contact is promoted to an independent company, its prior transactional history
  is no longer attributable to it or appears to belong to another record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create a child contact with some transactional history, promote it to an independent
  company-level record, and verify the history is still attached to the same identity.
```

## G03-CONTACTS-Q006

```yaml
QID: G03-CONTACTS-Q006
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Re-parenting a child contact to a different company does not retroactively re-attribute that
  child's already-posted historical documents to the new parent.
WHY_IT_MATTERS: >
  Retroactively moving posted history to a different parent changes historical financial
  attribution without any transaction actually having involved the new parent.
DISCONFIRMING_OBSERVATION: >
  Re-parenting a child contact causes its already-posted historical documents to display or
  aggregate under the new parent as if they always belonged there.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create a child contact with posted historical documents under one parent, re-parent it to a
  different company, and check how the historical documents are attributed afterward.
```

## G03-CONTACTS-Q007

```yaml
QID: G03-CONTACTS-Q007
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When two partner records are merged, which record survives as the retained identity is an
  explicit choice, not an arbitrary or unstated rule (such as always keeping whichever was
  created first) applied without the operator's awareness.
WHY_IT_MATTERS: >
  An unstated survivorship rule can retain the wrong record's identity, silently losing
  whichever attributes belonged only to the discarded one.
DISCONFIRMING_OBSERVATION: >
  A merge completes without the operator being shown, or able to control, which of the two
  records becomes the surviving identity.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Initiate a merge of two partner records with different attribute values and observe whether
  the surviving identity is explicit and controllable.
```

## G03-CONTACTS-Q008

```yaml
QID: G03-CONTACTS-Q008
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When two partner records that each carry a receivable or payable balance are merged, the
  combined balance after the merge equals the sum of both prior balances, not a value that
  silently drops one side.
WHY_IT_MATTERS: >
  A dropped balance during merge is a direct, silent financial loss or gain that would not be
  caught until a reconciliation much later.
DISCONFIRMING_OBSERVATION: >
  The combined balance after merging two records with existing balances does not equal the sum
  of the two pre-merge balances, with no explanation recorded.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Establish distinct known receivable and payable balances on two separate partner records,
  merge them, and verify the resulting balance against the sum of the originals.
```

## G03-CONTACTS-Q009

```yaml
QID: G03-CONTACTS-Q009
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Open, not-yet-posted documents referencing either of the two merged records are reassigned to
  the surviving record so that no open document is left pointing at a partner identity that no
  longer exists.
WHY_IT_MATTERS: >
  A document left pointing at a discarded identity becomes unfindable or unprocessable through
  any normal partner-based search.
DISCONFIRMING_OBSERVATION: >
  After a merge, an open document that referenced the discarded record still references that
  discarded identity rather than the surviving one.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create an open, unposted document against one of two records about to be merged, perform the
  merge, and check which identity the document references afterward.
```

## G03-CONTACTS-Q010

```yaml
QID: G03-CONTACTS-Q010
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Already-posted historical documents referencing the discarded record remain traceable to
  that original identity after a merge, rather than being silently rewritten to appear as if
  they always belonged to the surviving record.
WHY_IT_MATTERS: >
  Rewriting posted history changes what a previously filed financial record says happened,
  which is a serious audit and legal concern.
DISCONFIRMING_OBSERVATION: >
  A posted historical document's original party attribution is altered by the merge with no
  trace remaining of its original attribution.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create a posted document against one of two records about to be merged, perform the merge,
  and verify whether the document's original attribution remains traceable.
```

## G03-CONTACTS-Q011

```yaml
QID: G03-CONTACTS-Q011
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  When the two records being merged carry different accounting attributions (such as different
  receivable accounts), the merge requires an explicit resolution rather than silently picking
  one without flagging the conflict.
WHY_IT_MATTERS: >
  A silently resolved attribution conflict can redirect all future transactions for the
  surviving identity to an account nobody explicitly chose.
DISCONFIRMING_OBSERVATION: >
  Two records with different accounting attributions are merged and the resulting attribution
  is set with no indication that a conflict existed or was resolved.
EXPECTED_SURFACE: S1,S2,S5,S6
PRECONDITIONS: >
  Give two records about to be merged different accounting attributions and perform the merge,
  checking whether the conflict is surfaced.
```

## G03-CONTACTS-Q012

```yaml
QID: G03-CONTACTS-Q012
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The fact that a merge occurred, which two records were involved, and who performed it,
  remains discoverable after the fact.
WHY_IT_MATTERS: >
  Without this record, an unexpected change in a partner's history or balance after the fact
  cannot be traced back to a merge event at all.
DISCONFIRMING_OBSERVATION: >
  After a merge, there is no discoverable record of the merge having occurred, which records
  were involved, or who performed it.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform a merge of two records and then attempt to find any record of the merge event, its
  participants, and its operator.
```
## G03-CONTACTS-Q013

```yaml
QID: G03-CONTACTS-Q013
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A merge performed in error can be identified and its effect understood well enough to
  manually reconstruct the prior state, even if full automatic reversal is not offered.
WHY_IT_MATTERS: >
  Without any reconstructable trace, an erroneous merge becomes a permanent, undiagnosable
  change to the customer record and its history.
DISCONFIRMING_OBSERVATION: >
  After a merge, no information is retained that would allow a human to reconstruct what
  either original record looked like before the merge.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record the full state of two records, merge them, and attempt to reconstruct each original
  record's state from what remains afterward.
```

## G03-CONTACTS-Q014

```yaml
QID: G03-CONTACTS-Q014
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  A likely duplicate is flagged for human review rather than being merged automatically without
  any human confirmation.
WHY_IT_MATTERS: >
  Automatic merging without confirmation removes the one safeguard against merging two records
  that only superficially resemble each other.
DISCONFIRMING_OBSERVATION: >
  Two records that share matching identifying details are merged automatically with no human
  confirmation step.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Create two records with closely matching identifying details and observe whether any merge
  that follows requires explicit human confirmation.
```

## G03-CONTACTS-Q015

```yaml
QID: G03-CONTACTS-Q015
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If two records that turn out to represent genuinely distinct parties are merged in error, the
  transactional history of each remains individually identifiable well enough to support
  separating them again.
WHY_IT_MATTERS: >
  If the two histories become indistinguishable after a false merge, the two distinct legal
  entities' financial records are permanently commingled.
DISCONFIRMING_OBSERVATION: >
  After merging two records that turn out to be distinct, their individual transactional
  histories can no longer be told apart even with full access to the merge's own record.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Merge two records each carrying distinguishable transactional history and check whether each
  transaction's original party can still be identified afterward.
```

## G03-CONTACTS-Q016

```yaml
QID: G03-CONTACTS-Q016
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Duplicate detection relies on more than one identifying signal (such as a formal identifier
  in addition to name), so that two clearly distinct parties that happen to share a common name
  are not flagged as likely duplicates on name alone.
WHY_IT_MATTERS: >
  Name-only matching in populations with common names produces a high false-positive rate that
  erodes trust in the whole duplicate-detection mechanism.
DISCONFIRMING_OBSERVATION: >
  Two records with a common shared name but a different formal identifier and address are
  flagged as a likely duplicate based on the name match alone.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two records with an identical common name but distinct formal identifiers and
  addresses and check what duplicate signal, if any, is raised.
```

## G03-CONTACTS-Q017

```yaml
QID: G03-CONTACTS-Q017
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A partner record cannot be archived, or is at minimum clearly flagged, while it still has
  open, unresolved documents referencing it.
WHY_IT_MATTERS: >
  An archived partner with open documents can become invisible to normal workflows while still
  owing or being owed money.
DISCONFIRMING_OBSERVATION: >
  A partner record with open, unresolved documents is archived with no warning, block, or flag
  referencing those open documents.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Create an open, unresolved document against a partner and attempt to archive that partner.
```

## G03-CONTACTS-Q018

```yaml
QID: G03-CONTACTS-Q018
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Archiving a partner does not hide or remove access to its already-posted historical
  documents for reporting and audit purposes.
WHY_IT_MATTERS: >
  Losing access to a retired partner's posted history breaks audit continuity and historical
  reporting.
DISCONFIRMING_OBSERVATION: >
  After archiving a partner, its previously posted historical documents become inaccessible or
  excluded from standard historical reports.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Archive a partner with posted historical documents and verify whether those documents remain
  accessible in historical reporting.
```

## G03-CONTACTS-Q019

```yaml
QID: G03-CONTACTS-Q019
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A partner record that has ever been referenced by a posted document cannot be permanently
  deleted, only archived or deactivated.
WHY_IT_MATTERS: >
  Permanently deleting a party referenced by posted financial history would leave that history
  pointing at nothing, which is an audit failure.
DISCONFIRMING_OBSERVATION: >
  A partner record with posted document history can be permanently deleted rather than only
  archived.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Attempt to permanently delete a partner record that has at least one posted document
  referencing it.
```

## G03-CONTACTS-Q020

```yaml
QID: G03-CONTACTS-Q020
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  Reactivating an archived partner restores it with the same configuration it had at the time
  of archiving, not defaults that silently differ from what was previously set.
WHY_IT_MATTERS: >
  Silently reset configuration on reactivation (such as accounting attribution reverting to a
  default) can misdirect the very next transaction against that partner.
DISCONFIRMING_OBSERVATION: >
  A reactivated partner shows different accounting attribution, terms, or settings than it had
  immediately before it was archived.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Record a partner's full configuration, archive it, reactivate it, and compare the
  configuration before and after.
```

## G03-CONTACTS-Q021

```yaml
QID: G03-CONTACTS-Q021
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A partner shared across multiple companies can carry a different accounting attribution per
  company, and each company's transactions use that company's own attribution.
WHY_IT_MATTERS: >
  Without per-company override, one company's transactions against a shared partner could post
  to another company's account by mistake.
DISCONFIRMING_OBSERVATION: >
  A transaction created in one company against a shared partner uses the accounting
  attribution configured for a different company.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Configure different accounting attributions for the same shared partner under two different
  companies and create a transaction in each company to check which attribution applies.
```

## G03-CONTACTS-Q022

```yaml
QID: G03-CONTACTS-Q022
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
LAYER: PROCESS
HYPOTHESIS: >
  When a shared partner has no company-specific accounting attribution set for the company
  creating a transaction, a defined, documented fallback applies rather than the transaction
  proceeding with no attribution at all.
WHY_IT_MATTERS: >
  A transaction that ends up with no clear accounting attribution cannot be posted correctly
  and may block or misdirect downstream processing.
DISCONFIRMING_OBSERVATION: >
  A transaction is created for a company with no specific override set for that shared
  partner, and the resulting attribution is undefined, missing, or unexplained.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Remove the company-specific attribution for a shared partner under one company and create a
  transaction there, checking what attribution actually gets applied.
```

## G03-CONTACTS-Q023

```yaml
QID: G03-CONTACTS-Q023
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  Changing a partner's accounting attribution does not retroactively alter which account
  already-posted documents report against.
WHY_IT_MATTERS: >
  Retroactively changing posted history's account attribution would silently rewrite closed
  financial periods.
DISCONFIRMING_OBSERVATION: >
  Changing a partner's accounting attribution causes a previously posted document's reported
  account to change as well.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a document against a partner's current accounting attribution, change that attribution,
  and check whether the posted document's reported account changed.
```

## G03-CONTACTS-Q024

```yaml
QID: G03-CONTACTS-Q024
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A document already approved but not yet posted at the moment a partner's accounting
  attribution changes uses a defined, predictable rule for which attribution it posts under,
  not an unpredictable one depending on timing.
WHY_IT_MATTERS: >
  An unpredictable outcome for in-flight documents means the same business situation can post
  two different ways depending on exact timing, which is not a controlled business rule.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical in-progress documents post under different accounting attributions
  purely because of small timing differences relative to when the partner's attribution
  changed, with no documented rule explaining the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Approve a document against a partner, change that partner's accounting attribution before
  posting, and observe which attribution the document posts under.
```
## G03-CONTACTS-Q025

```yaml
QID: G03-CONTACTS-Q025
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  Fields on a shared partner that are meant to be company-specific are only visible or editable
  from within that company's own context, not from another company sharing the same partner.
WHY_IT_MATTERS: >
  A company-specific field visible from an unrelated company context leaks that company's
  private commercial terms to users who should not see them.
DISCONFIRMING_OBSERVATION: >
  A user working in one company's context can view or edit a company-specific field belonging
  to a different company on a shared partner.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set a company-specific field for a shared partner in one company and attempt to view or edit
  it while working in a different company's context.
```

## G03-CONTACTS-Q026

```yaml
QID: G03-CONTACTS-Q026
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  A partner record created under one tenant is never visible, searchable, or editable from a
  different, unrelated tenant.
WHY_IT_MATTERS: >
  Cross-tenant visibility of partner data is a fundamental multi-tenant isolation failure with
  direct customer-data exposure consequences.
DISCONFIRMING_OBSERVATION: >
  A partner record from one tenant appears in a search, listing, or edit view accessible from a
  different, unrelated tenant.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Create a partner under one tenant and, from a session belonging to a different unrelated
  tenant, attempt to find or access that record.
```

## G03-CONTACTS-Q027

```yaml
QID: G03-CONTACTS-Q027
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
LAYER: PROCESS
HYPOTHESIS: >
  A field a human has manually entered or corrected on a partner record is not silently
  overwritten by a later externally sourced enrichment pass.
WHY_IT_MATTERS: >
  Silent overwrite of a human correction by external enrichment reintroduces the original error
  without the human noticing.
DISCONFIRMING_OBSERVATION: >
  A field manually corrected by a human is overwritten by an externally sourced enrichment
  update with no explicit instruction to allow that overwrite.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Manually correct a field on a partner record whose value would otherwise come from external
  enrichment, then trigger the enrichment path and check whether the manual value survives.
```

## G03-CONTACTS-Q028

```yaml
QID: G03-CONTACTS-Q028
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
LAYER: PROCESS
HYPOTHESIS: >
  Which fields on a partner record are eligible to be updated by an external enrichment source
  is explicitly scoped, not every field on the record being equally subject to overwrite.
WHY_IT_MATTERS: >
  An unscoped enrichment pass could overwrite sensitive or manually curated fields, such as
  accounting attribution, that were never meant to come from an external source.
DISCONFIRMING_OBSERVATION: >
  An externally sourced enrichment update changes a field, such as an accounting attribution,
  that should never be sourced externally.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Trigger an external enrichment update for a partner and inspect which fields it is capable of
  changing.
```

## G03-CONTACTS-Q029

```yaml
QID: G03-CONTACTS-Q029
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A bulk import of partner records checks incoming rows against existing records for likely
  duplicates rather than creating a new record for every row regardless of existing matches.
WHY_IT_MATTERS: >
  An import that ignores existing matches multiplies the duplicate-partner problem at scale in
  a single operation.
DISCONFIRMING_OBSERVATION: >
  A bulk import creates a new record for a row that clearly matches an existing partner record
  on identifying details, with no duplicate check performed.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Include in a bulk import one row that closely matches an existing partner record and observe
  whether a duplicate is created or flagged.
```

## G03-CONTACTS-Q030

```yaml
QID: G03-CONTACTS-Q030
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  When a bulk import of partner records partially fails partway through, the rows already
  successfully created are clearly identifiable and distinguishable from the rows that failed,
  rather than the outcome being ambiguous.
WHY_IT_MATTERS: >
  An ambiguous partial-failure outcome makes it impossible to know which records exist and
  which need to be reattempted, risking duplicate reattempts or gaps.
DISCONFIRMING_OBSERVATION: >
  After a bulk import partially fails, there is no way to distinguish which rows were
  successfully created from which failed.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Run a bulk import designed to fail partway through and inspect the result for a clear
  success/failure breakdown per row.
```

## G03-CONTACTS-Q031

```yaml
QID: G03-CONTACTS-Q031
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
LAYER: BASE
HYPOTHESIS: >
  A formal tax identifier entered for a partner is checked against the format or checksum rule
  appropriate to its stated jurisdiction, not accepted as any arbitrary string.
WHY_IT_MATTERS: >
  An unchecked tax identifier can silently propagate an invalid value into every tax-relevant
  document generated for that partner.
DISCONFIRMING_OBSERVATION: >
  A tax identifier that is clearly invalid for its stated jurisdiction's format is accepted
  without warning.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enter a tax identifier that violates the known format rule for its stated jurisdiction and
  observe whether it is accepted.
```

## G03-CONTACTS-Q032

```yaml
QID: G03-CONTACTS-Q032
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Changing a partner's tax identifier does not retroactively alter the tax identifier shown on
  documents already posted under the previous identifier.
WHY_IT_MATTERS: >
  Retroactively changing the tax identifier on already-issued documents would misstate what was
  actually declared at the time of the original transaction.
DISCONFIRMING_OBSERVATION: >
  Changing a partner's tax identifier causes an already-posted document to display the new
  identifier instead of the one in effect when it was posted.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a document against a partner's current tax identifier, change that identifier, and check
  whether the posted document's displayed identifier changed.
```

## G03-CONTACTS-Q033

```yaml
QID: G03-CONTACTS-Q033
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  When a child contact has its own explicitly set commercial terms different from its parent
  company, a transaction created against that child uses the child's own terms, not the
  parent's.
WHY_IT_MATTERS: >
  If the parent's terms silently override an explicitly set child override, the override
  becomes meaningless and any deliberate exception is lost.
DISCONFIRMING_OBSERVATION: >
  A transaction created against a child contact with its own explicitly set commercial terms
  applies the parent company's terms instead.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set distinct commercial terms on both a parent company and one of its child contacts, then
  create a transaction against the child and check which terms apply.
```

## G03-CONTACTS-Q034

```yaml
QID: G03-CONTACTS-Q034
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A child contact designated for a specific function (such as billing or delivery) is the one
  automatically used by a downstream document created for that function, rather than defaulting
  to the parent or an arbitrary contact.
WHY_IT_MATTERS: >
  A document that ignores the designated functional contact can be sent to or address the wrong
  party for that function.
DISCONFIRMING_OBSERVATION: >
  A downstream document for a specific function is generated referencing a contact other than
  the one explicitly designated for that function, with no override requested.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Designate a specific child contact for a function on a partner, generate a downstream
  document for that function, and check which contact it references.
```

## G03-CONTACTS-Q035

```yaml
QID: G03-CONTACTS-Q035
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  When a partner has more than one address of different purposes (such as billing and
  shipping), a downstream document defaults to the address matching its own purpose, not an
  arbitrary one among those available.
WHY_IT_MATTERS: >
  A shipping document defaulting to a billing address, or vice versa, sends goods or invoices
  to the wrong physical location.
DISCONFIRMING_OBSERVATION: >
  A downstream document defaults to an address whose purpose does not match the document's own
  purpose, when a matching-purpose address exists.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Set distinct billing and shipping addresses on a partner and generate documents of each type,
  checking which address each defaults to.
```

## G03-CONTACTS-Q036

```yaml
QID: G03-CONTACTS-Q036
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  Changing a partner's address does not retroactively change the address already recorded on a
  document that was created, and is still in progress, before the change.
WHY_IT_MATTERS: >
  Retroactively changing the address on an in-flight document could redirect a delivery already
  being physically prepared against the original address.
DISCONFIRMING_OBSERVATION: >
  A document already created and in progress shows an updated address after the partner's
  address was changed, without the document itself being explicitly updated.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an in-progress document referencing a partner's current address, change the partner's
  address, and check whether the document's own recorded address changed.
```
## G03-CONTACTS-Q037

```yaml
QID: G03-CONTACTS-Q037
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  A category or tag assigned to a partner that is meant to drive a business rule (such as a
  pricing or terms rule) only applies going forward, not retroactively to documents already
  created before the tag was assigned.
WHY_IT_MATTERS: >
  A retroactively applied rule based on a later tag assignment can silently change the terms or
  pricing of a transaction that was already agreed under different terms.
DISCONFIRMING_OBSERVATION: >
  Assigning a new category or tag to a partner changes the pricing or terms shown on a document
  that was already created before the tag was assigned.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a document against a partner, then assign a new category or tag to that partner that
  would drive different pricing or terms, and check whether the existing document changed.
```

## G03-CONTACTS-Q038

```yaml
QID: G03-CONTACTS-Q038
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Changing which internal owner or salesperson is assigned to a partner does not retroactively
  reassign the ownership already recorded on a transaction created before the change.
WHY_IT_MATTERS: >
  Retroactive reassignment would misattribute credit or responsibility for a transaction to
  someone who was not involved when it happened.
DISCONFIRMING_OBSERVATION: >
  An already-created transaction's recorded owner or salesperson changes automatically after
  the partner's assigned owner is changed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a transaction against a partner with one assigned owner, then change the partner's
  assigned owner and check whether the transaction's recorded owner changed.
```

## G03-CONTACTS-Q039

```yaml
QID: G03-CONTACTS-Q039
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Editing a partner's financially significant attribution (such as its accounting attribution)
  requires a distinct, higher level of permission than editing general descriptive fields on
  the same record.
WHY_IT_MATTERS: >
  If both require the same permission, any user allowed to fix a typo in a partner's name could
  also redirect its financial postings.
DISCONFIRMING_OBSERVATION: >
  A user permitted to edit only general descriptive fields on a partner is also able to change
  its accounting attribution.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user granted access to edit only general fields on a partner, attempt to change its
  accounting attribution.
```

## G03-CONTACTS-Q040

```yaml
QID: G03-CONTACTS-Q040
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  Performing a merge of two partner records requires a distinct, elevated permission beyond
  ordinary edit access to either record.
WHY_IT_MATTERS: >
  A merge is a much higher-consequence, harder-to-reverse action than an ordinary edit and
  warrants a correspondingly higher permission bar.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary edit access to partner records is able to perform a merge without
  any additional permission check.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user with ordinary edit access but no elevated merge permission, attempt to perform a
  merge of two partner records.
```

## G03-CONTACTS-Q041

```yaml
QID: G03-CONTACTS-Q041
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  A change to a financially relevant field on a partner record (such as its accounting
  attribution or tax identifier) is individually logged with who changed it and when, distinct
  from a generic "record updated" entry.
WHY_IT_MATTERS: >
  A generic update log with no field-level detail cannot answer which specific financially
  significant value changed or who was responsible.
DISCONFIRMING_OBSERVATION: >
  A change to a financially relevant field produces no field-level log entry distinguishable
  from an unrelated, non-financial field change.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change a financially relevant field on a partner and a separate, non-financial field, then
  compare what each change produces in the audit log.
```

## G03-CONTACTS-Q042

```yaml
QID: G03-CONTACTS-Q042
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  The audit log for a partner field change distinguishes a change made by an automated
  enrichment process from one made directly by a human user.
WHY_IT_MATTERS: >
  Without this distinction, an investigation into who changed a value cannot tell whether a
  person or an automated process was responsible.
DISCONFIRMING_OBSERVATION: >
  The audit log entry for a field changed by automated enrichment is indistinguishable from one
  made by a human user directly editing the same field.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change the same type of field once through automated enrichment and once through direct human
  edit, and compare the resulting audit log entries.
```

## G03-CONTACTS-Q043

```yaml
QID: G03-CONTACTS-Q043
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
LAYER: BASE
HYPOTHESIS: >
  When two users edit different fields on the same partner record at nearly the same time, both
  changes are preserved rather than one silently overwriting the other.
WHY_IT_MATTERS: >
  Silent last-write-wins overwrite on unrelated fields destroys one user's legitimate change
  with no warning to either user.
DISCONFIRMING_OBSERVATION: >
  Two users editing different, unrelated fields on the same partner record at nearly the same
  time end up with only one of the two changes actually saved.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have two sessions each edit a different field on the same partner record concurrently and
  save both, then check whether both changes persisted.
```

## G03-CONTACTS-Q044

```yaml
QID: G03-CONTACTS-Q044
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  If a new transaction is created against one of the two records in the middle of a merge
  operation being performed on them, that transaction is not silently lost or left orphaned once
  the merge completes.
WHY_IT_MATTERS: >
  A transaction created in the narrow window of an in-progress merge could otherwise disappear
  or attach to neither the source nor the surviving record.
DISCONFIRMING_OBSERVATION: >
  A transaction created against one of the two records while a merge involving it is in progress
  is unaccounted for once the merge completes.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Begin a merge of two records and, while it is in progress, create a new transaction against
  one of them, then verify the transaction's final attribution once the merge completes.
```

## G03-CONTACTS-Q045

```yaml
QID: G03-CONTACTS-Q045
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
LAYER: BASE
HYPOTHESIS: >
  Changing a partner's communication language preference affects documents generated after the
  change, not one already generated and queued for delivery before the change.
WHY_IT_MATTERS: >
  A document already generated and queued should not silently change language underneath a
  process that already committed to sending it as originally generated.
DISCONFIRMING_OBSERVATION: >
  A document already generated and queued for delivery changes its language after the partner's
  communication preference is updated.
EXPECTED_SURFACE: S1,S5,S8
PRECONDITIONS: >
  Generate and queue a document for a partner, then change that partner's communication
  language preference, and check whether the already-queued document changed.
```

## G03-CONTACTS-Q046

```yaml
QID: G03-CONTACTS-Q046
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: BASE
HYPOTHESIS: >
  When both a partner's own payment detail and a company-level default exist, a payment created
  against that partner uses the partner's own detail, not the company-level default silently
  overriding it.
WHY_IT_MATTERS: >
  A payment silently routed to a generic default instead of the partner's own specified detail
  could send money to the wrong destination.
DISCONFIRMING_OBSERVATION: >
  A payment created for a partner with its own explicit payment detail set instead uses a
  company-level default detail.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set a partner's own payment detail distinct from any company-level default, create a payment
  against that partner, and check which detail is actually used.
```

## G03-CONTACTS-Q047

```yaml
QID: G03-CONTACTS-Q047
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
LAYER: PROCESS
HYPOTHESIS: >
  Flagging a partner as blocked (such as a do-not-deal status) prevents new documents from being
  created against it but the effect on documents already in progress at the moment of flagging
  is an explicit, documented rule, not an unpredictable one.
WHY_IT_MATTERS: >
  An in-progress document silently continuing to completion, or silently halting with no
  visibility, against a newly blocked partner both carry real business and compliance risk if
  the rule is not deliberate and known.
DISCONFIRMING_OBSERVATION: >
  An in-progress document against a partner flagged as blocked continues or halts with no
  documented rule governing which of those outcomes should occur.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create an in-progress document against a partner, flag that partner as blocked before the
  document completes, and observe what happens to the document.
```

## G03-CONTACTS-Q048

```yaml
QID: G03-CONTACTS-Q048
MODULE: contacts
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
LAYER: PROCESS
HYPOTHESIS: >
  When the same partner record is used as both a customer and a vendor, its receivable balance
  and its payable balance are tracked and reported separately, not netted together into a single
  ambiguous figure without an explicit netting action.
WHY_IT_MATTERS: >
  An automatically netted balance can hide that a partner both owes money and is owed money,
  which are two different legal and collection situations.
DISCONFIRMING_OBSERVATION: >
  A partner used as both customer and vendor shows a single combined balance with no way to see
  the separate receivable and payable figures that make it up.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create both a receivable-generating and a payable-generating transaction against the same
  partner and check whether each balance remains separately visible.
```
