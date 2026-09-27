# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / base_address_extended Module MVQ Bank

**Document ID:** GMVQ-G03-BASE_ADDRESS_EXTENDED-MVQ48-V1.00
**Group:** G03 MASTER_DATA
**Module Metadata:** `base_address_extended`
**Wave:** W1
**Author Cell:** TEAM 14 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank supplies the module-specific MVQ set for the additional structured address
components carried beyond the base address set. It targets the material this group must
cover: authority between structured and free-form address data; country-conditional
requirements; an address changed after it was already printed onto a finalized document;
parent/child propagation and what must not propagate; validation parity between import and
interactive entry; and the tax or delivery consequence of a changed structured component.
Question text is source-neutral and does not expose vendor names, field names, methods,
schema, XML IDs, or API shapes.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- Output remains source-neutral; `MODULE + QID` is a Research Evidence Join Key only.
- No Formal Coverage is derived from this bank.
- Produced under GMVQ_AUTHORING_STANDARD_V1.00 and GROUP_BRIEF_G03_MASTER_DATA.
- This bank is DRAFT / PREPARED ONLY. It is not approved, frozen, or verified.

## G03-BASE_ADDRESS_EXTENDED-Q001

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q001
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a structured address component and an accompanying free-form address text disagree,
  one of them is treated as authoritative for tax and legal computation in a consistent,
  disclosed way, rather than either being used unpredictably depending on which screen or
  process reads the address.
WHY_IT_MATTERS: >
  An inconsistent choice of authority between structured and free-form address data could
  compute tax or route delivery based on stale or wrong information without anyone noticing.
DISCONFIRMING_OBSERVATION: >
  Two different processes that both need the address (for example, tax computation and
  document printing) draw conflicting components from the same record, one from the
  structured fields and one from the free-form text.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Set a structured component and a free-form address text to disagree deliberately, then
  trigger two separate processes that consume the address and compare which value each used.
```

## G03-BASE_ADDRESS_EXTENDED-Q002

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q002
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A structured address component required for one country is not silently required, or
  silently ignored, for a different country where it has no meaning.
WHY_IT_MATTERS: >
  Forcing an irrelevant field blocks legitimate entry in some countries; silently ignoring a
  field that is required elsewhere lets incomplete addresses through.
DISCONFIRMING_OBSERVATION: >
  A structured component that is meaningless in Country A is still enforced as required
  there, or a component required in Country B is accepted blank there with no validation.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure or select two countries with different requirements for a given structured
  component, and attempt to save an address for each with that component left blank.
```

## G03-BASE_ADDRESS_EXTENDED-Q003

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q003
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Editing a structured address component after it has already been used on a finalized,
  issued document does not silently alter the address as it appears on that already-issued
  document if it is reprinted or regenerated.
WHY_IT_MATTERS: >
  A legal or tax document is expected to reflect the address at the time it was issued; a
  document that changes retroactively when the master address changes could misstate what
  was actually sent to a counterparty.
DISCONFIRMING_OBSERVATION: >
  Reprinting or regenerating a previously finalized document after the address was edited
  shows the new address instead of the address that was in effect when the document was
  originally issued.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Finalize/issue a document referencing an address, edit a structured component of that
  address afterward, and reprint or regenerate the original document.
```

## G03-BASE_ADDRESS_EXTENDED-Q004

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q004
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A structured address change made on a parent record (such as a company) propagates to
  child location records only where the child has not already been given its own
  independent override of that component.
WHY_IT_MATTERS: >
  Blanket propagation would silently overwrite a child's deliberately different address,
  while no propagation at all defeats the convenience of a shared parent address.
DISCONFIRMING_OBSERVATION: >
  A child location that already has its own explicit value for a structured component has
  that value overwritten when the parent's address is edited, or a child intended to inherit
  the parent's address fails to update when the parent changes.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Give a child location its own explicit override for one component while leaving another
  component inherited from the parent, then edit the parent's address and check both
  components on the child.
```

## G03-BASE_ADDRESS_EXTENDED-Q005

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q005
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Validation strictness for structured address components applied through a bulk import path
  matches the validation applied through interactive entry, rather than the import path
  silently accepting data the interactive screen would reject.
WHY_IT_MATTERS: >
  A looser bulk-import validation path becomes the easiest way to introduce invalid addresses
  at scale, defeating the purpose of interactive validation.
DISCONFIRMING_OBSERVATION: >
  An address that would be rejected or flagged when entered interactively is accepted
  without warning through a bulk import path.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Construct an address with an invalid or inconsistent structured component, attempt to save
  it interactively, then attempt the identical data through a bulk import path.
```

## G03-BASE_ADDRESS_EXTENDED-Q006

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q006
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing a structured address component that determines tax jurisdiction updates the
  jurisdiction used for future transactions from that point forward, without retroactively
  altering the jurisdiction already recorded on past, already-finalized transactions.
WHY_IT_MATTERS: >
  Retroactively shifting jurisdiction on historical transactions could misstate tax already
  reported and reconciled for a prior period.
DISCONFIRMING_OBSERVATION: >
  Editing a structured component that determines tax jurisdiction changes the jurisdiction
  recorded on a transaction that was already finalized before the address change.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Finalize a transaction under one jurisdiction-relevant address, then edit that structured
  component and check whether the already-finalized transaction's recorded jurisdiction
  changes.
```

## G03-BASE_ADDRESS_EXTENDED-Q007

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q007
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing a delivery-relevant structured address component on an order that has not yet
  been fulfilled is reflected in the fulfillment/shipping process, rather than the shipment
  proceeding against the address as it stood when the order was first created.
WHY_IT_MATTERS: >
  Shipping to a stale address after a legitimate correction would misdeliver goods and
  create avoidable cost and customer impact.
DISCONFIRMING_OBSERVATION: >
  An unfulfilled order's shipment proceeds using the original structured address component
  after that component was deliberately corrected before fulfillment.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Create an order with a delivery address, edit a structured delivery-relevant component
  before fulfillment, and check which address value the fulfillment process actually uses.
```

## G03-BASE_ADDRESS_EXTENDED-Q008

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q008
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A structured address record can be archived or deactivated while still being referenced by
  an open, unfulfilled document, and doing so does not silently break that document's
  ability to complete using the address it already has.
WHY_IT_MATTERS: >
  An open order should not become unshippable, or lose its destination, purely because
  someone tidied up an address record it depends on.
DISCONFIRMING_OBSERVATION: >
  Archiving or deactivating an address referenced by an open document causes that document's
  address to become blank, broken, or unusable for completing the transaction.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Reference an address on an open, unfulfilled document, archive or deactivate that address
  record, and attempt to proceed with the document to completion.
```

## G03-BASE_ADDRESS_EXTENDED-Q009

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q009
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Merging two records that each carry their own, differing structured address components
  resolves the conflict through an explicit choice or rule, rather than silently discarding
  one record's address data without any indication of what was lost.
WHY_IT_MATTERS: >
  A silent loss of address detail during a merge could later misroute deliveries or
  misstate a legal address with no way to know it changed.
DISCONFIRMING_OBSERVATION: >
  Merging two records with differing structured address components produces a result where
  one record's address data is gone, with no record, prompt, or log of the discarded values.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create two records with deliberately different structured address components, merge them,
  and check whether the discarded address data is recorded anywhere.
```

## G03-BASE_ADDRESS_EXTENDED-Q010

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q010
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A shared record's address can carry a per-company or per-branch override of a structured
  component without that override affecting how the address appears to other
  companies/branches sharing the same base record.
WHY_IT_MATTERS: >
  Without per-scope override, one company's local correction (for example, a locally known
  unit or floor detail) would leak into or overwrite what other companies see for a shared
  partner.
DISCONFIRMING_OBSERVATION: >
  A per-company override of a structured address component on a shared record changes what a
  different, non-overriding company sees for the same shared record.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Set up a shared address record visible to two companies, apply a per-company override of
  one structured component from Company A, and check what Company B sees.
```

## G03-BASE_ADDRESS_EXTENDED-Q011

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q011
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two users editing structured components of the same address record at the same time
  cannot both save such that the final saved address is an unintended mix that neither user
  actually entered.
WHY_IT_MATTERS: >
  A silently merged/overwritten concurrent edit could produce an address nobody actually
  verified, especially dangerous for a legal or delivery address.
DISCONFIRMING_OBSERVATION: >
  Two concurrent edits to different structured components of the same address both appear to
  succeed, but the final saved record does not match either user's intended full set of
  values.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Open the same address record in two sessions, edit different structured components in
  each, save both in close succession, and inspect the final saved values.
```

## G03-BASE_ADDRESS_EXTENDED-Q012

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q012
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an address is populated or corrected by an external data-enrichment service, a value
  the user had manually entered is not silently overwritten by the external service's value
  unless the user explicitly triggers or confirms the overwrite.
WHY_IT_MATTERS: >
  A user's manual correction, often made because the automatic value was wrong, should not
  be silently reverted by the very automation that was wrong the first time.
DISCONFIRMING_OBSERVATION: >
  An automatic enrichment pass overwrites a manually entered structured component without
  any explicit user trigger or confirmation for that overwrite.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Manually enter a value for a structured component that the enrichment service would
  compute differently, then trigger any automatic enrichment pass and check whether the
  manual value survives.
```

## G03-BASE_ADDRESS_EXTENDED-Q013

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q013
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a given structured component is required differs consistently between an address
  used for billing purposes and the same address type used for delivery purposes, matching
  each purpose's actual need.
WHY_IT_MATTERS: >
  A billing-only requirement forced onto every delivery address (or the reverse) creates
  friction or lets genuinely required billing detail through blank.
DISCONFIRMING_OBSERVATION: >
  A structured component known to be required only for billing is also enforced as required
  on a delivery-only address, or a delivery-only requirement is not enforced on a billing
  address that needs it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure distinct requirements for billing versus delivery address purposes, then attempt
  to save each purpose with the other purpose's required component left blank.
```

## G03-BASE_ADDRESS_EXTENDED-Q014

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q014
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a record has more than one address that could qualify as the default for a given
  purpose, the system selects one default deterministically and consistently rather than the
  selection varying between screens or between successive lookups.
WHY_IT_MATTERS: >
  An inconsistent default selection could route a document to a different address than the
  one shown to the user who approved it.
DISCONFIRMING_OBSERVATION: >
  Two different screens, or two successive lookups moments apart, select a different address
  as the default for the same record and purpose with no intervening change.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Give a record two or more addresses that could each qualify as default for the same
  purpose, then check the default selected from at least two different access points.
```

## G03-BASE_ADDRESS_EXTENDED-Q015

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q015
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting an address record referenced by a scheduled or recurring transaction template is
  either prevented, or handled by the template falling back to an explicit, disclosed
  alternative, rather than the next generated occurrence silently having no address.
WHY_IT_MATTERS: >
  A recurring document that silently loses its address would fail delivery or fail tax
  computation with no warning until someone notices the downstream failure.
DISCONFIRMING_OBSERVATION: >
  Deleting an address referenced by a recurring template allows the next generated
  occurrence to be created with the address silently blank and no warning surfaced.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Set up a recurring transaction template referencing a specific address, delete that
  address, and let or force the next occurrence to generate.
```

## G03-BASE_ADDRESS_EXTENDED-Q016

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q016
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Address data belonging to one company/tenant is not returned by a search, autocomplete, or
  lookup performed from a different, non-sharing company/tenant's context.
WHY_IT_MATTERS: >
  A search-path leak of address data across tenants is a real data-isolation failure even if
  the create/edit screens are correctly scoped.
DISCONFIRMING_OBSERVATION: >
  A search, autocomplete, or lookup run from Company A's context returns or matches against
  an address record scoped to Company B, where no sharing has been configured.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Create a distinctive address under Company B only, then attempt to find it through search,
  autocomplete, or lookup from a session scoped to Company A.
```

## G03-BASE_ADDRESS_EXTENDED-Q017

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q017
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The postal or formatting normalization applied to a structured component at save time is
  applied consistently, such that the same raw input produces the same stored and displayed
  value regardless of which screen or path it was entered through.
WHY_IT_MATTERS: >
  Inconsistent normalization could cause the same physical address to be stored in two
  different textual forms depending on entry path, defeating exact-match lookups and
  duplicate detection.
DISCONFIRMING_OBSERVATION: >
  Entering the identical raw structured component value through two different entry paths
  results in two different normalized/stored values for the same field.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enter the same raw value for a structured component through two different available entry
  paths (for example, interactive form and an integration/import) and compare the stored
  results.
```

## G03-BASE_ADDRESS_EXTENDED-Q018

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q018
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An address left with some, but not all, structured components filled in is handled by a
  consistent, disclosed rule (block save, allow with a flag, or treat missing components as
  genuinely optional), rather than behaving differently depending on which component is
  missing with no documented basis.
WHY_IT_MATTERS: >
  Unpredictable handling of partial addresses makes it impossible to know, without testing
  every component, whether an incomplete address will actually be usable downstream.
DISCONFIRMING_OBSERVATION: >
  Leaving one particular structured component blank blocks saving the address, while leaving
  a different, similarly-classified component blank is silently accepted, with no documented
  reason for the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to save an address with each structured component individually left blank in turn,
  and compare which are blocked versus accepted.
```

## G03-BASE_ADDRESS_EXTENDED-Q019

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q019
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An address submitted to an external service for validation, geocoding, or enrichment is
  submitted with the same structured component values that are actually stored on the
  record, not a stale or partially-updated snapshot.
WHY_IT_MATTERS: >
  Submitting a stale snapshot to an external service would produce enrichment results that
  do not correspond to what the user is actually looking at, silently misleading downstream
  processing.
DISCONFIRMING_OBSERVATION: >
  A structured component is changed on screen just before triggering an external
  validation/enrichment call, and the external service is called with the old, pre-change
  value.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Change a structured component and, without saving separately, immediately trigger the
  external validation/enrichment call, then inspect what value was actually submitted.
```

## G03-BASE_ADDRESS_EXTENDED-Q020

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q020
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An identical structured address shared by two unrelated records (for example, a shared
  office building used by two separate business partners) can be edited independently on one
  record without the edit appearing on the other.
WHY_IT_MATTERS: >
  Two unrelated parties happening to share a physical address must remain independently
  editable; any hidden linkage would let one party's correction silently alter another's
  record.
DISCONFIRMING_OBSERVATION: >
  Editing a structured component on one of two unrelated records that happen to share the
  same address values also changes the corresponding component on the other, unrelated
  record.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create two unrelated records with identical structured address values, edit one record's
  address, and check whether the other record's address changed.
```

## G03-BASE_ADDRESS_EXTENDED-Q021

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q021
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The structured component fields accept and correctly store non-Latin script and extended
  character sets without truncation, corruption, or silent character replacement.
WHY_IT_MATTERS: >
  Truncated or corrupted address text in a non-Latin script would render legal documents and
  delivery labels wrong for a large class of legitimate addresses.
DISCONFIRMING_OBSERVATION: >
  A structured component entered in a non-Latin script or with extended characters is
  truncated, garbled, or has characters silently replaced when stored and redisplayed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enter representative non-Latin script or extended-character text into a structured
  component, save, and redisplay the record to verify it round-trips intact.
```

## G03-BASE_ADDRESS_EXTENDED-Q022

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q022
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing the country on an address record with an already-filled state/province-equivalent
  structured component either clears that now-inconsistent component or flags it for review,
  rather than silently retaining a value that no longer corresponds to any valid subdivision
  of the new country.
WHY_IT_MATTERS: >
  A retained, now-meaningless subdivision value could pass downstream tax or delivery logic
  that trusts the field to be valid for the current country.
DISCONFIRMING_OBSERVATION: >
  Changing an address's country leaves a previously entered state/province-equivalent value
  in place unchanged even though it does not correspond to any valid subdivision of the new
  country, with no flag raised.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Fill in a country-specific subdivision component, change the address's country to one with
  an incompatible set of subdivisions, and check the subdivision field's resulting state.
```

## G03-BASE_ADDRESS_EXTENDED-Q023

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q023
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Viewing an address's structured components can be permitted separately from editing them,
  so that a role granted read access does not implicitly gain write access, and vice versa.
WHY_IT_MATTERS: >
  Address data often needs to be visible to more staff than should be able to change it,
  particularly where a changed address has tax or delivery consequences.
DISCONFIRMING_OBSERVATION: >
  A role granted only view access to an address can also edit its structured components, or
  a role granted only edit access is blocked from viewing components it needs to edit
  correctly.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Configure a role with view-only access to addresses and test whether edit actions are
  actually blocked, and the reverse for an edit-only role.
```

## G03-BASE_ADDRESS_EXTENDED-Q024

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q024
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A bulk/mass update tool that changes a structured component across many address records at
  once enforces the same validation rules (country-specific requirements, format checks) as
  editing one record interactively.
WHY_IT_MATTERS: >
  A bulk tool that skips validation to move faster becomes the easiest way to introduce a
  large batch of invalid addresses in one action.
DISCONFIRMING_OBSERVATION: >
  A bulk update accepts a structured component value across many records that would be
  rejected if entered on any single one of those records interactively.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt a bulk update setting an invalid structured component value across several address
  records, and compare against attempting the same value interactively on one of them.
```

## G03-BASE_ADDRESS_EXTENDED-Q025

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q025
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to a structured component that a tax registration or numbering scheme depends on
  triggers a consistency check against the associated registration data, rather than
  allowing the address and the registration to silently diverge.
WHY_IT_MATTERS: >
  An address and its associated tax registration silently falling out of alignment could
  cause tax filings to reference a jurisdiction the address no longer supports.
DISCONFIRMING_OBSERVATION: >
  A structured component that a stored tax registration depends on is changed with no check,
  flag, or prompt regarding the now-possibly-inconsistent registration data.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set up an address with an associated tax registration tied to a structured component, then
  change that component and check whether any consistency check is triggered.
```

## G03-BASE_ADDRESS_EXTENDED-Q026

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q026
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A change to any structured address component is attributable to a specific user and
  timestamp in an available history or audit trail, at least for records where the address
  feeds a financial or legal outcome.
WHY_IT_MATTERS: >
  Without attribution, no one can determine who altered a delivery or tax-relevant address,
  or when, when investigating a misdelivery or a tax dispute.
DISCONFIRMING_OBSERVATION: >
  A structured component change on an address feeding a financial or legal outcome is not
  attributable to any user or timestamp in available history.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a structured component on an address known to feed a financial or legal process,
  and inspect whatever history/audit trail is available for that record.
```

## G03-BASE_ADDRESS_EXTENDED-Q027

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q027
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A prior version of an address's structured components remains available (through history,
  not just the current live values) after the address has been edited, at least for a
  defined retention purpose, rather than the edit being an unrecoverable overwrite.
WHY_IT_MATTERS: >
  Without any retained prior state, correcting a mistaken edit, or reconstructing what an
  address looked like at the time of a past transaction, is impossible.
DISCONFIRMING_OBSERVATION: >
  After editing a structured component, there is no way to retrieve what the value was
  immediately before the edit, through any history, log, or version feature available.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Note the current value of a structured component, edit it, and attempt to retrieve the
  prior value through any available history or log.
```

## G03-BASE_ADDRESS_EXTENDED-Q028

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q028
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A structured address component change made after a recurring document's next occurrence
  has already been generated, but before that occurrence is finalized, is reflected in the
  still-pending occurrence.
WHY_IT_MATTERS: >
  A pending, not-yet-finalized occurrence should reflect the current known-correct address
  rather than perpetuating an address correction that has not yet propagated.
DISCONFIRMING_OBSERVATION: >
  A pending, unfinalized recurring occurrence retains the old structured component value
  after that component was corrected on the underlying address before the occurrence was
  finalized.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Generate a pending occurrence of a recurring document referencing an address, correct a
  structured component on that address before finalizing the occurrence, and check which
  value the occurrence uses at finalization.
```

## G03-BASE_ADDRESS_EXTENDED-Q029

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q029
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Reactivating a previously archived/deactivated address record does not silently apply the
  current validation rule set to previously-valid-but-now-noncompliant historical values,
  altering data the user did not touch.
WHY_IT_MATTERS: >
  A validation rule tightened since the address was archived should not silently rewrite or
  reject old values purely because the record was reactivated, without the user having made
  any actual edit.
DISCONFIRMING_OBSERVATION: >
  Reactivating an archived address whose structured components were valid under the old
  rules, but would fail current rules, causes those components to be silently altered or
  cleared on reactivation alone.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Archive an address valid under the rules at that time, change the validation rules to
  something the address would no longer satisfy, then reactivate the address and check
  whether its stored values changed.
```

## G03-BASE_ADDRESS_EXTENDED-Q030

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q030
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The same underlying structured address renders in a locale-appropriate order and format on
  different documents (for example, a document generated in one language versus another)
  without the underlying stored component values themselves changing between renders.
WHY_IT_MATTERS: >
  Correct localized rendering matters for usability, but the underlying data must remain a
  single source of truth regardless of which document format displays it.
DISCONFIRMING_OBSERVATION: >
  Generating documents in two different languages/locales from the same address record shows
  different underlying structured component values, not just a different display order or
  format.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Generate documents referencing the same address in two different language/locale settings
  and compare the underlying structured component values used, not just the visual layout.
```

## G03-BASE_ADDRESS_EXTENDED-Q031

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q031
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An address flagged as a legal/registered office is distinguished, in how it is used by
  downstream processes, from an address used purely for day-to-day operational or delivery
  purposes.
WHY_IT_MATTERS: >
  Conflating the two would risk sending routine operational correspondence to a registered
  legal address, or worse, using an operational address where a legal filing requires the
  registered one.
DISCONFIRMING_OBSERVATION: >
  A downstream process that specifically requires the legal/registered office address
  instead uses an operational/delivery address, or the reverse, with no distinction enforced.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Set up distinct legal/registered and operational addresses on the same record, and trigger
  a downstream process that specifically requires one, to check which it actually uses.
```

## G03-BASE_ADDRESS_EXTENDED-Q032

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q032
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A child location created by copying the parent's address at creation time is a genuine,
  independent copy from that point forward, rather than silently remaining live-linked such
  that later parent edits keep flowing through despite the child's independent creation.
WHY_IT_MATTERS: >
  If the intended behaviour is a one-time copy, a hidden live link would cause unexpected,
  unrequested changes to the child whenever the parent is edited later.
DISCONFIRMING_OBSERVATION: >
  A child location created via a one-time copy of the parent's address still changes when the
  parent's address is edited afterward, contrary to the intended copy-not-link behaviour, or
  the reverse (an intended live-link child fails to update).
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Create a child location by copying the parent's address, then edit the parent's address
  afterward and check whether the child's copy changed.
```

## G03-BASE_ADDRESS_EXTENDED-Q033

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q033
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two structured addresses recorded for the same record that are simultaneously marked as
  active for the same purpose (for example, two active legal addresses) are flagged as a
  conflict rather than silently leaving it ambiguous which one downstream processes will use.
WHY_IT_MATTERS: >
  An undetected ambiguity between two simultaneously active addresses for the same purpose
  could send different downstream processes to different addresses for the same legal entity
  without anyone deciding that on purpose.
DISCONFIRMING_OBSERVATION: >
  A record ends up with two addresses simultaneously marked active for the identical purpose
  with no conflict flagged, and different downstream processes are observed using different
  ones of the two.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Attempt to mark two addresses on the same record as active for the identical purpose at
  once, and check for a conflict flag and for consistency across downstream processes.
```

## G03-BASE_ADDRESS_EXTENDED-Q034

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q034
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an external enrichment/validation call fails or times out, the address record retains
  its previously entered structured component values rather than being left partially
  overwritten or blanked.
WHY_IT_MATTERS: >
  A failed external call should degrade gracefully to the last known-good manual data, not
  corrupt the record with a partial update.
DISCONFIRMING_OBSERVATION: >
  A structured component is blanked, partially updated, or corrupted after an external
  enrichment/validation call fails or times out mid-update.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Trigger an external enrichment/validation call and simulate or wait for a failure/timeout,
  then inspect the address record's structured components afterward.
```

## G03-BASE_ADDRESS_EXTENDED-Q035

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q035
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Duplicate detection that considers structured address components correctly identifies two
  records as likely duplicates when their structured components are effectively equivalent
  despite superficial formatting differences (case, spacing, abbreviation).
WHY_IT_MATTERS: >
  A duplicate detector defeated by trivial formatting differences would let real duplicate
  business partners accumulate with split, inconsistent transaction history.
DISCONFIRMING_OBSERVATION: >
  Two records with structured address components that are effectively equivalent but
  differently formatted are not flagged as possible duplicates by the available detection
  mechanism.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create two records with the same underlying address expressed with differing case,
  spacing, or abbreviation in structured components, and check whether duplicate detection
  flags them.
```

## G03-BASE_ADDRESS_EXTENDED-Q036

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q036
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Merging two records whose duplicate structured addresses are only superficially different
  into one does not silently lose whichever record's open documents or transactional history
  was on the record that is not retained as the surviving record.
WHY_IT_MATTERS: >
  A costly false-duplicate merge is bad enough; losing open documents or history in that
  merge compounds the damage where it is hardest to detect.
DISCONFIRMING_OBSERVATION: >
  After merging two records that were flagged as address duplicates, the open documents or
  transactional history that belonged to the non-surviving record are missing from the
  merged result.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Give both duplicate-flagged records their own open documents or transactional history,
  merge them, and verify both sets of history are present on the surviving record.
```

## G03-BASE_ADDRESS_EXTENDED-Q037

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q037
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A structured component subject to a data-residency or regulatory storage requirement for a
  given jurisdiction is stored in a way that honours that requirement, and moving the
  record's associated company/tenant does not silently relocate that data in violation of
  the original requirement.
WHY_IT_MATTERS: >
  A regulatory storage-location requirement tied to an address component must survive
  routine administrative actions like reassigning a record to a different company, or it is
  not a real control.
DISCONFIRMING_OBSERVATION: >
  Reassigning a record with a jurisdiction-restricted structured component to a different
  company/tenant results in that component's data being handled or stored in a way
  inconsistent with its original jurisdiction's requirement.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set up a structured component understood to carry a jurisdiction-specific storage
  requirement, reassign the owning record to a different company/tenant, and check whether
  the requirement is still honoured.
```

## G03-BASE_ADDRESS_EXTENDED-Q038

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q038
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Searching, filtering, or grouping records by a structured address component returns
  results scoped correctly to the current company/tenant boundary, consistent with how the
  individual records themselves are scoped.
WHY_IT_MATTERS: >
  A search or grouping feature that ignores the scoping the base records otherwise respect is
  a subtle but real way to leak cross-tenant information through an aggregate view.
DISCONFIRMING_OBSERVATION: >
  Grouping or filtering by a structured component from within one company/tenant's context
  includes records that belong to a different, non-sharing company/tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create records with a shared structured component value under two separate, non-sharing
  companies, then run a group-by or filter on that component from one company's context.
```

## G03-BASE_ADDRESS_EXTENDED-Q039

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q039
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Rolling back or undoing a structured address edit restores not only the component's own
  value but also any dependent state that was derived from it (for example, a jurisdiction or
  routing determination made from the edited value), rather than leaving the dependent state
  stuck on the intermediate, now-undone value.
WHY_IT_MATTERS: >
  A partial rollback that restores the field but not what was derived from it leaves the
  record internally inconsistent in a way that is not obvious from looking at the field
  alone.
DISCONFIRMING_OBSERVATION: >
  After undoing a structured component edit, a value that was derived from the edited
  component (such as a jurisdiction or routing flag) remains at the value computed for the
  now-undone edit rather than reverting with it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Edit a structured component that drives a derived value, note the derived value change,
  undo the structured component edit, and check whether the derived value reverts too.
```

## G03-BASE_ADDRESS_EXTENDED-Q040

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q040
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A structured address component's maximum length or format constraint is enforced
  consistently at the point of entry and is not silently truncated later at some downstream
  point (such as printing or exporting) that has a stricter limit than the entry screen
  allowed.
WHY_IT_MATTERS: >
  A downstream truncation invisible at entry time would let an address that looked complete
  and correct when saved arrive incomplete on the document that actually matters.
DISCONFIRMING_OBSERVATION: >
  A structured component value accepted in full at entry is silently truncated when it
  reaches a downstream document, export, or integration, with no warning at either the entry
  or the output stage.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Enter a structured component value at or near the entry screen's stated maximum length,
  then check that value on a generated document, export, or integration output.
```

## G03-BASE_ADDRESS_EXTENDED-Q041

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q041
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An address record can hold more structured location levels than the base two or three (for
  example, a building, a floor, and a unit) without those extra levels colliding with or
  overwriting the base-level fields they extend.
WHY_IT_MATTERS: >
  If the extended levels are not cleanly additive, saving a deeply specified address could
  corrupt the base fields that older parts of the system, or other integrations, still rely
  on.
DISCONFIRMING_OBSERVATION: >
  Filling in an extended, deeper structured location level causes a base-level address field
  to be overwritten, cleared, or misrepresented.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Fill in the deepest available extended structured location level on an address that already
  has its base-level fields populated, and check whether the base-level fields remain intact.
```

## G03-BASE_ADDRESS_EXTENDED-Q042

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q042
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Once a document referencing an address has reached a locked/finalized state, the structured
  address components that document uses are frozen from further edits reaching that document,
  even if the underlying address record itself is later edited for other purposes.
WHY_IT_MATTERS: >
  Without a frozen reference, a finalized document's effective address keeps moving as the
  master record is edited for unrelated future needs, undermining the meaning of
  "finalized."
DISCONFIRMING_OBSERVATION: >
  A locked/finalized document's effective structured address changes after the underlying
  address record is edited post-lock, without an explicit re-open or correction action on the
  document itself.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Finalize/lock a document referencing an address, edit the underlying address record
  afterward, and check whether the locked document's effective address changed.
```

## G03-BASE_ADDRESS_EXTENDED-Q043

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q043
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A validation failure on one structured component during interactive entry does not discard
  values already correctly entered into other structured components on the same address.
WHY_IT_MATTERS: >
  Losing correctly entered fields because one unrelated field failed validation creates
  unnecessary rework and increases the chance of a subsequent, different entry error.
DISCONFIRMING_OBSERVATION: >
  Triggering a validation failure on one structured component clears or discards the values
  already entered in other, unrelated structured components on the same form.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Fill in several structured components correctly, deliberately trigger a validation failure
  on one specific component, and check whether the other components' values survive.
```

## G03-BASE_ADDRESS_EXTENDED-Q044

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q044
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The set of which structured components are shown or required for a given country is driven
  by configuration that can be reviewed and adjusted, rather than being hardcoded such that a
  newly added or changed country requirement can never be reflected without a code change.
WHY_IT_MATTERS: >
  Address rules change and vary more than software release cycles can track; a hardcoded rule
  set forces a workaround every time a country's requirement changes.
DISCONFIRMING_OBSERVATION: >
  Adjusting which structured components apply to a given country has no available
  configuration path, and the country-specific behaviour changes only through means outside
  normal configuration.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt to adjust which structured components are required or shown for one specific
  country through the available configuration, without any code-level change.
```

## G03-BASE_ADDRESS_EXTENDED-Q045

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q045
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A structured address record referenced by more than one unrelated document type (for
  example, both a sales-side and a purchase-side document) is edited once and reflected
  consistently across all of them, rather than each document type holding its own silently
  diverging cached copy.
WHY_IT_MATTERS: >
  Divergent cached copies across document types would let two documents referencing the
  "same" address disagree with each other after a single edit, with no indication that only
  one was updated.
DISCONFIRMING_OBSERVATION: >
  Editing a shared address is reflected on one referencing document type but not another,
  with both still displaying as pointing to the same, unedited-looking source address.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Reference the same address record from two different document types, edit the address, and
  check whether both document types reflect the change consistently.
```

## G03-BASE_ADDRESS_EXTENDED-Q046

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q046
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Removing a structured component's value entirely (clearing it to blank) is distinguished
  from that component never having been set, wherever that distinction matters for
  downstream validation or reporting.
WHY_IT_MATTERS: >
  Conflating "cleared" with "never entered" could let a required-field check silently pass
  on a record where the value was deliberately blanked, if the check only looks for the
  field's mere existence.
DISCONFIRMING_OBSERVATION: >
  A structured component deliberately cleared to blank passes a required-field check that a
  component genuinely never populated would also pass, indicating the two states are not
  actually distinguished.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Clear a previously filled required structured component to blank and separately create a
  fresh record where that component was never touched, then compare how each is treated by
  required-field validation.
```

## G03-BASE_ADDRESS_EXTENDED-Q047

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q047
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An address structured component that a numbering or sequencing scheme depends on (for
  example, a branch code embedded in a document number) does not silently produce
  inconsistent numbering when that component is changed on an address already referenced by
  documents using the old value.
WHY_IT_MATTERS: >
  A silent mismatch between a document's embedded numbering reference and the current address
  component it was drawn from could misfile or misroute documents relying on that numbering
  for identification.
DISCONFIRMING_OBSERVATION: >
  Changing a structured component that a numbering scheme depends on causes new documents to
  be numbered inconsistently with existing documents still referencing the same address, with
  no reconciling rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Identify a numbering scheme that draws on a structured address component, change that
  component, and generate a new document to compare its numbering against existing documents.
```

## G03-BASE_ADDRESS_EXTENDED-Q048

```yaml
QID: G03-BASE_ADDRESS_EXTENDED-Q048
MODULE: base_address_extended
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The ability to configure which structured components exist, are required, or apply per
  country (a configuration-level action) is governed by a distinct permission from the
  ability to merely fill in an address on an individual record (a data-entry-level action).
WHY_IT_MATTERS: >
  Conflating the two would let ordinary data-entry staff change country-wide address rules,
  or block them from routine address entry until granted configuration-level rights.
DISCONFIRMING_OBSERVATION: >
  A role granted only data-entry rights can alter which structured components are required
  or shown per country, or a role granted only configuration rights is blocked from filling
  in an address on an individual record.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Configure two roles, one with only data-entry rights and one with only
  address-configuration rights, and test each against both kinds of action.
```

