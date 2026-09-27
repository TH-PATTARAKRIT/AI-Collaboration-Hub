# SMEsPlus ENTERPRISE SUITE
## GMVQ — G04 ACCOUNT_BASE / account_add_gln Module Adversarial MVQ Bank

**Document ID:** GMVQ-G04-ACCOUNT_ADD_GLN-MVQ48-V1.00
**Group:** G04 ACCOUNT_BASE
**Module Metadata:** `account_add_gln`
**Wave:** W1
**Author Cell:** TEAM 20 (GMVQ Question Factory — Internal Production Team 20, Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This module carries a global location identifier on partners and companies for electronic exchange. This bank
supplements the 35 Standard Questions with module-specific, adversarial questions covering: identifier
uniqueness and check-digit validation; an identifier changed after documents carrying it were already issued or
transmitted; one legal entity with several locations and which identifier a given document must carry; the
identifier absent at the moment of transmission; mismatch between the identifier and the address or tax
registration on the same record; per-company values on a shared partner; import supplying an invalid
identifier; and the audit trail of a change that affects an already-exchanged document.

Question text is source-neutral: no vendor or product name, no technical identifier (model, table, field,
method, XML ID, API path), and no reference to how any specific implementation is built. Language is generic
business/behavioural language throughout.

## Control

- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across business rule,
  state transition, configuration dependency, role/permission, exception path, cross-module dependency,
  auditability, tenant/company boundary, concurrency, and runtime/configuration reachability.
- This module carries one layer; the `LAYER` field is omitted throughout.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `module + QID` is a Research
  Evidence Join Key only; no Formal Coverage is derived from this bank.
- Lane A / Lane B: NOT STARTED for this module until rolling batch freeze is recorded.

## G04-ACCOUNT_ADD_GLN-Q001

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q001
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The identifier is validated for correct format and check-digit before it can be saved on a partner or company
  record; an invalid value is rejected, not silently accepted.
WHY_IT_MATTERS: >
  Accepting an invalid identifier propagates a bad value into every future transmission that relies on it.
DISCONFIRMING_OBSERVATION: >
  A value that fails the check-digit or format rule is saved onto a partner or company record without any
  validation error.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Attempt to save a deliberately invalid identifier (wrong length, wrong check digit) on a partner and a company
  record.
```

## G04-ACCOUNT_ADD_GLN-Q002

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q002
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Uniqueness of the identifier is enforced consistently, or its absence of enforcement is an explicit, documented
  configuration choice, rather than being checked inconsistently depending on which screen or path is used to
  enter it.
WHY_IT_MATTERS: >
  Inconsistent uniqueness enforcement lets the same identifier attach to two unrelated records through one path
  while being blocked through another.
DISCONFIRMING_OBSERVATION: >
  Entering a duplicate identifier is blocked through one entry path but accepted through another (direct edit
  versus import).
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Attempt to assign the same identifier value to two different partner records through each available entry
  path.
```

## G04-ACCOUNT_ADD_GLN-Q003

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q003
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The check-digit validation logic is not affected by locale, language, or number formatting settings on the
  session performing the entry.
WHY_IT_MATTERS: >
  A locale-dependent validation bug could accept or reject the same value inconsistently across users.
DISCONFIRMING_OBSERVATION: >
  The same identifier value is accepted under one locale/language setting and rejected under another.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Enter the same identifier value under two different locale/language session settings.
```

## G04-ACCOUNT_ADD_GLN-Q004

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q004
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A malformed identifier cannot be forced onto a record through a bulk update or mass-edit action even where
  individual-record validation would normally block it.
WHY_IT_MATTERS: >
  Bulk paths are a common route for validation to be silently skipped.
DISCONFIRMING_OBSERVATION: >
  A bulk update sets an invalid identifier value on multiple records without triggering the same validation as a
  single-record edit.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Use a bulk-edit action to set an invalid identifier value across several records at once.
```

## G04-ACCOUNT_ADD_GLN-Q005

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q005
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Removing (blanking) a previously valid identifier from a record is an allowed, explicit action distinguishable
  from never having set one, and does not silently fail or silently substitute a different value.
WHY_IT_MATTERS: >
  A defect in clearing the field could leave a stale identifier appearing valid when the business has said it no
  longer applies.
DISCONFIRMING_OBSERVATION: >
  Attempting to blank a previously set identifier leaves the old value in place, or replaces it with an
  unrelated value, without the actor's intent.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Set an identifier on a record, then attempt to clear it, and verify the resulting state.
```

## G04-ACCOUNT_ADD_GLN-Q006

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q006
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A record can hold at most one active identifier value at a time; the data model does not allow two
  simultaneously active identifiers to exist on the same record without one being explicitly marked historical.
WHY_IT_MATTERS: >
  Two simultaneously "active" identifiers would make it ambiguous which one governs a given transmission.
DISCONFIRMING_OBSERVATION: >
  A record ends up with two identifier values both appearing current/active, with no marking of which supersedes
  the other.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a record's identifier value more than once in succession and inspect whether the prior value remains
  marked as active anywhere.
```

## G04-ACCOUNT_ADD_GLN-Q007

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q007
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the identifier on a partner or company record after documents carrying the old value have already
  been transmitted does not retroactively alter what those already-transmitted documents show.
WHY_IT_MATTERS: >
  Retroactively altering a transmitted document's stored identifier would misrepresent what was actually sent.
DISCONFIRMING_OBSERVATION: >
  Changing the identifier on the master record changes the identifier value displayed or stored on a document
  that was already transmitted under the old value.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Transmit a document carrying the current identifier, then change the identifier on the master record, and
  re-open the already-transmitted document.
```

## G04-ACCOUNT_ADD_GLN-Q008

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q008
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A document created after the identifier change, but referencing a template, default, or copy of a document
  created before the change, picks up the new identifier rather than silently carrying forward the stale one.
WHY_IT_MATTERS: >
  A stale identifier surviving into new documents through copy/default behaviour would defeat the point of
  updating the master record.
DISCONFIRMING_OBSERVATION: >
  A new document created after the identifier change, via copy or default from an older document, is populated
  with the old identifier value.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Change the master identifier, then create a new document by copying or defaulting from a document created
  before the change.
```

## G04-ACCOUNT_ADD_GLN-Q009

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q009
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An in-progress, not-yet-transmitted document that already has the old identifier populated is either updated
  to the new value or explicitly flagged as carrying a stale value before it can be transmitted.
WHY_IT_MATTERS: >
  A silently stale identifier on a document about to be sent would transmit incorrect data with no warning.
DISCONFIRMING_OBSERVATION: >
  A draft document retains the old identifier value with no update or warning, and can be transmitted as-is
  after the master record's identifier changed.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create a draft document with the identifier populated, change the master record's identifier, and attempt to
  transmit the draft.
```

## G04-ACCOUNT_ADD_GLN-Q010

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q010
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The history of identifier changes on a record (old value, new value, date, actor) is retrievable, not
  overwritten with only the current value visible.
WHY_IT_MATTERS: >
  Without change history, a dispute over which value was in force on a given date cannot be resolved.
DISCONFIRMING_OBSERVATION: >
  After an identifier change, no record exists of what the previous value was, when it changed, or who changed
  it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change a record's identifier and inspect the record's history/audit trail for the prior value.
```

## G04-ACCOUNT_ADD_GLN-Q011

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q011
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Reverting an identifier change back to its previous value is treated as a new, separately recorded change, not
  merged silently with the original entry as if the intervening change never happened.
WHY_IT_MATTERS: >
  Silent merging would hide that the identifier was ever wrong during the intervening period.
DISCONFIRMING_OBSERVATION: >
  Reverting to a previous identifier value collapses the change history so the intervening incorrect period is
  no longer visible.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change an identifier, then change it back to the original value, and inspect the change history for both
  events.
```

## G04-ACCOUNT_ADD_GLN-Q012

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q012
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scheduled or background process that reads the identifier for outbound transmission always reads the current
  value at the moment of transmission, not a value cached earlier in its run.
WHY_IT_MATTERS: >
  A cached stale value in a background process would transmit an outdated identifier even after the master
  record was corrected.
DISCONFIRMING_OBSERVATION: >
  A background transmission process sends a document using an identifier value that was already superseded
  before the transmission ran.
EXPECTED_SURFACE: S1,S2,S8
PRECONDITIONS: >
  Change the identifier shortly before a scheduled transmission process runs, and inspect which value the
  transmitted document carries.
```

## G04-ACCOUNT_ADD_GLN-Q013

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q013
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A legal entity with more than one operational location can hold a distinct identifier per location, and a
  document is associated with the identifier of the specific location relevant to that document, not a single
  entity-wide default regardless of location.
WHY_IT_MATTERS: >
  Using the wrong location's identifier misdirects the electronic exchange to the wrong physical or legal
  destination.
DISCONFIRMING_OBSERVATION: >
  A document relevant to one location is transmitted carrying a different location's identifier, with no way to
  select the correct one.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  Configure two locations with distinct identifiers under one entity and create documents relevant to each
  location.
```

## G04-ACCOUNT_ADD_GLN-Q014

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q014
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Adding a new location to an entity that already has locations with identifiers does not default the new
  location's identifier to a copy of an existing one; it starts unset or explicitly requires entry.
WHY_IT_MATTERS: >
  A defaulted copy would silently misattribute the new location's documents to an existing location's
  identifier.
DISCONFIRMING_OBSERVATION: >
  A newly added location is created with another existing location's identifier already populated, without
  deliberate entry.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Add a new location to an entity that has other locations with identifiers set, and inspect the new location's
  identifier field.
```

## G04-ACCOUNT_ADD_GLN-Q015

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q015
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a document does not clearly specify which location it belongs to, the identifier is not populated by
  guessing an arbitrary location; the location is resolved before the identifier is populated.
WHY_IT_MATTERS: >
  An arbitrary guess would produce a document with a misleading identifier that looks correct but is not.
DISCONFIRMING_OBSERVATION: >
  A document with an ambiguous or unset location nonetheless has an identifier auto-populated from an arbitrarily
  chosen location.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  Create a document without explicitly resolving its location and inspect whether an identifier gets populated
  anyway.
```

## G04-ACCOUNT_ADD_GLN-Q016

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q016
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Deactivating one location of a multi-location entity does not affect the identifier or availability of the
  entity's other active locations.
WHY_IT_MATTERS: >
  Cross-location interference would make routine location lifecycle management risk unrelated locations' data.
DISCONFIRMING_OBSERVATION: >
  Deactivating one location clears, disables, or otherwise affects the identifier of a different, still-active
  location under the same entity.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Deactivate one of several locations under an entity and inspect the identifiers of the remaining active
  locations.
```

## G04-ACCOUNT_ADD_GLN-Q017

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q017
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Merging two location records (a data-cleanup operation) does not silently drop one of the two identifiers if
  both had different valid values; the conflict is surfaced rather than one value quietly winning.
WHY_IT_MATTERS: >
  A silently dropped identifier could invalidate future transmissions attributed to the merged-away location's
  business relationships.
DISCONFIRMING_OBSERVATION: >
  Merging two location records with different identifier values results in one identifier disappearing without
  any conflict indication.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Merge two location records that each carry a distinct identifier value and inspect the resulting record.
```

## G04-ACCOUNT_ADD_GLN-Q018

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q018
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A report or list view that displays the identifier for a multi-location entity clearly attributes each
  displayed value to its specific location, rather than showing one ambiguous entity-level value.
WHY_IT_MATTERS: >
  An ambiguous display could lead a user to send a document under the wrong location's identifier by mistake.
DISCONFIRMING_OBSERVATION: >
  A report lists an identifier for a multi-location entity without indicating which location it belongs to.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  View a report or list involving a multi-location entity that has distinct per-location identifiers.
```

## G04-ACCOUNT_ADD_GLN-Q019

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q019
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Attempting to transmit a document that requires the identifier, when it is absent, is blocked with a clear
  reason rather than transmitted with a blank or placeholder value.
WHY_IT_MATTERS: >
  A silently blank transmission could be rejected downstream or, worse, accepted with an incorrect implicit
  default.
DISCONFIRMING_OBSERVATION: >
  A document requiring the identifier is transmitted successfully despite the identifier being absent on the
  relevant record.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Remove the identifier from a record that a document requires it from, then attempt to transmit that document.
```

## G04-ACCOUNT_ADD_GLN-Q020

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q020
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document blocked from transmission for a missing identifier can be resumed and transmitted once the
  identifier is supplied, without needing to be recreated from scratch.
WHY_IT_MATTERS: >
  Forcing recreation would lose other work already done on the document for an unrelated missing field.
DISCONFIRMING_OBSERVATION: >
  Supplying the missing identifier after a blocked transmission attempt does not allow the same document to be
  transmitted; it must be recreated.
EXPECTED_SURFACE: S1,S2,S5
PRECONDITIONS: >
  Block a transmission for a missing identifier, then supply the identifier and retry transmitting the same
  document.
```

## G04-ACCOUNT_ADD_GLN-Q021

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q021
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the identifier is mandatory for a given transmission is governed by a configuration appropriate to the
  transaction type and jurisdiction, not a single hard-coded rule applied uniformly regardless of context.
WHY_IT_MATTERS: >
  A one-size-fits-all mandatory rule would either block legitimate transmissions that do not need the identifier
  or fail to enforce it where it is genuinely required.
DISCONFIRMING_OBSERVATION: >
  A transaction type where the identifier is not supposed to be mandatory is nonetheless blocked for its
  absence, or a type where it must be mandatory is not.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Configure two transaction types with different identifier requirements and test transmission with the
  identifier absent on each.
```

## G04-ACCOUNT_ADD_GLN-Q022

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q022
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A partner record without any identifier at all is treated distinctly from one whose identifier field exists
  but is empty due to a data issue; a report distinguishing "not applicable" from "missing" is possible.
WHY_IT_MATTERS: >
  Conflating "not applicable" with "missing" hides a genuine data-quality gap behind an intentional business
  exception.
DISCONFIRMING_OBSERVATION: >
  There is no way to distinguish, in any report or record, a partner for whom the identifier does not apply from
  one where it is simply missing.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Set up one partner explicitly marked as not requiring the identifier and another with it simply left blank,
  and compare how each is reported.
```

## G04-ACCOUNT_ADD_GLN-Q023

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q023
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A scheduled or batch transmission process that encounters a record missing the required identifier skips or
  holds that specific record and reports it, rather than failing the entire batch or silently omitting the
  record without a report.
WHY_IT_MATTERS: >
  A whole-batch failure over one bad record blocks unrelated valid transmissions; a silent omission hides a
  compliance gap.
DISCONFIRMING_OBSERVATION: >
  A batch transmission either fails entirely due to one record's missing identifier, or silently drops that
  record with no report of the omission.
EXPECTED_SURFACE: S1,S2,S6,S8
PRECONDITIONS: >
  Include one record missing the required identifier in a batch transmission alongside valid records and observe
  the outcome.
```

## G04-ACCOUNT_ADD_GLN-Q024

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q024
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A user attempting to transmit a document with a missing identifier sees a specific, actionable message naming
  the missing identifier, not a generic validation failure.
WHY_IT_MATTERS: >
  A generic error forces the user to guess at the cause, slowing correction and inviting workarounds.
DISCONFIRMING_OBSERVATION: >
  The error shown for a missing identifier is a generic validation message that does not name the identifier as
  the cause.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Attempt to transmit a document with the identifier missing and inspect the specific error message shown.
```

## G04-ACCOUNT_ADD_GLN-Q025

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q025
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A mismatch between the identifier's registered address/legal details and the address or tax registration
  currently held on the same record is detectable, either through validation at entry or a reconcilable check,
  rather than the two fields being maintained with no cross-check at all.
WHY_IT_MATTERS: >
  An undetected mismatch could mean documents are sent to or attributed to the wrong legal address for exchange
  purposes.
DISCONFIRMING_OBSERVATION: >
  A record with a clearly mismatched identifier and address/tax registration produces no validation warning and
  no way to detect the mismatch through any check.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Set up a record with an identifier and an address/tax registration that are inconsistent with each other, and
  check for any warning or detection mechanism.
```

## G04-ACCOUNT_ADD_GLN-Q026

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q026
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing the address or tax registration on a record does not automatically alter the identifier field, and
  changing the identifier does not automatically alter the address or tax registration; each is maintained
  independently and any cross-population is explicit.
WHY_IT_MATTERS: >
  Unintended cross-population between these fields could silently corrupt whichever field was not the one the
  user intended to change.
DISCONFIRMING_OBSERVATION: >
  Editing the address or tax registration field changes the identifier value (or the reverse) without the user
  having touched that field.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Edit the address/tax registration on a record with an existing identifier, and separately edit the identifier,
  checking the other field each time.
```

## G04-ACCOUNT_ADD_GLN-Q027

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q027
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the identifier is expected to correspond to a specific registered address, a change of registered
  address flags existing identifier values for review rather than leaving them silently unreviewed and presumed
  still valid.
WHY_IT_MATTERS: >
  An unreviewed identifier after an address change could keep referencing a location the entity no longer
  operates from.
DISCONFIRMING_OBSERVATION: >
  Changing a record's registered address leaves its identifier unflagged and unreviewed with no prompt to verify
  continued correctness.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Change the registered address on a record that already has an identifier set and check for any review prompt
  or flag.
```

## G04-ACCOUNT_ADD_GLN-Q028

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q028
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The identifier and the tax registration identifier are stored and validated as separate, independent fields; a
  value that is valid as one is not silently accepted into the other's field due to shared formatting.
WHY_IT_MATTERS: >
  Cross-acceptance between different identifier types would corrupt whichever exchange process reads the wrong
  field.
DISCONFIRMING_OBSERVATION: >
  A value formatted for one identifier type is accepted without warning into the field intended for the other
  type.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Attempt to enter a value with the format of one identifier type into the field for the other type.
```

## G04-ACCOUNT_ADD_GLN-Q029

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q029
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document combining the identifier with the tax registration for the same transaction presents both values
  independently on the outbound record, without one silently substituting for or overwriting the other during
  document generation.
WHY_IT_MATTERS: >
  A generation defect substituting one value for the other would transmit incorrect regulatory or exchange data.
DISCONFIRMING_OBSERVATION: >
  A generated document shows the tax registration value in the field meant for the identifier, or the reverse.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Generate a document that carries both the identifier and the tax registration for the same partner and inspect
  where each value appears.
```

## G04-ACCOUNT_ADD_GLN-Q030

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q030
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Validation of the identifier against the address/tax registration, where performed, is applied consistently
  regardless of whether the record was created interactively or through an automated integration.
WHY_IT_MATTERS: >
  A validation gap specific to automated creation would let inconsistent data enter only through that path.
DISCONFIRMING_OBSERVATION: >
  A mismatched identifier/address combination is blocked when entered interactively but accepted when created
  through an automated integration.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Attempt to create a record with a mismatched identifier/address combination both interactively and through an
  automated integration path.
```

## G04-ACCOUNT_ADD_GLN-Q031

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q031
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a single partner record is shared across more than one company scope, the identifier can be set per
  company scope, and a document issued from one company scope uses that scope's value, not another scope's.
WHY_IT_MATTERS: >
  A shared partner using the wrong company's identifier misattributes the transmission to the wrong company
  relationship.
DISCONFIRMING_OBSERVATION: >
  A document issued from one company scope for a shared partner carries the identifier value set for a different
  company scope.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Set different identifier values for the same shared partner under two company scopes and issue a document
  from each scope.
```

## G04-ACCOUNT_ADD_GLN-Q032

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q032
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Setting the identifier for a shared partner under one company scope does not overwrite or clear the value
  already set for that partner under a different company scope.
WHY_IT_MATTERS: >
  Cross-scope overwriting would silently corrupt another company's already-correct configuration.
DISCONFIRMING_OBSERVATION: >
  Setting the identifier under one company scope changes or clears the value visible under a different company
  scope for the same shared partner.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Set the identifier for a shared partner under one company scope and inspect the value under a different
  company scope afterward.
```

## G04-ACCOUNT_ADD_GLN-Q033

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q033
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A user with access to only one company scope cannot view or infer the identifier value set for the same shared
  partner under a company scope they do not have access to.
WHY_IT_MATTERS: >
  Leaking another company's per-scope value through a shared record would break the tenant/company boundary.
DISCONFIRMING_OBSERVATION: >
  A user restricted to one company scope can see or infer the identifier value configured under a different
  company scope for the same shared partner.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Restrict a user to one company scope and attempt to view the shared partner's identifier value under a
  different scope through any available path.
```

## G04-ACCOUNT_ADD_GLN-Q034

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q034
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting or archiving the per-company identifier value under one company scope does not delete the shared
  partner record itself or affect other company scopes' values for it.
WHY_IT_MATTERS: >
  An overly broad delete action would remove data belonging to a company scope that did not request the change.
DISCONFIRMING_OBSERVATION: >
  Removing the identifier under one company scope also removes it under another company scope, or deletes the
  shared partner record.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Remove the identifier value for a shared partner under one company scope and inspect the partner record and
  other scopes' values afterward.
```

## G04-ACCOUNT_ADD_GLN-Q035

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q035
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A report that aggregates identifiers across company scopes for a shared partner clearly attributes each value
  to its owning scope rather than presenting one ambiguous value for the partner as a whole.
WHY_IT_MATTERS: >
  An ambiguous cross-scope display invites using the wrong scope's identifier on a document.
DISCONFIRMING_OBSERVATION: >
  A cross-scope report shows a single identifier value for a shared partner without indicating which company
  scope it belongs to.
EXPECTED_SURFACE: S1,S4,S5
PRECONDITIONS: >
  View a report spanning multiple company scopes that includes a shared partner with distinct per-scope
  identifier values.
```

## G04-ACCOUNT_ADD_GLN-Q036

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q036
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Copying or duplicating a shared partner record into a new company scope does not automatically carry over
  another scope's identifier value as if it were already validated for the new scope.
WHY_IT_MATTERS: >
  An auto-copied value could be wrong for the new scope's actual business relationship and go unnoticed because
  it looks populated.
DISCONFIRMING_OBSERVATION: >
  Duplicating a shared partner into a new company scope populates the identifier field with a value copied from
  an existing scope, without deliberate entry for the new scope.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Duplicate a shared partner record that has an identifier set under one scope into a new company scope and
  inspect the new scope's identifier field.
```

## G04-ACCOUNT_ADD_GLN-Q037

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q037
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An import batch containing a record with an invalid identifier value rejects or flags that specific record's
  identifier field, rather than either failing the whole import or silently accepting the invalid value.
WHY_IT_MATTERS: >
  Either extreme — all-or-nothing failure or silent acceptance — defeats the purpose of validating the field at
  all.
DISCONFIRMING_OBSERVATION: >
  An import containing one record with an invalid identifier either aborts the entire batch or completes with
  the invalid value accepted unflagged.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Include one record with a deliberately invalid identifier in an otherwise valid import batch and observe the
  outcome.
```

## G04-ACCOUNT_ADD_GLN-Q038

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q038
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An import that supplies a valid-format but factually incorrect identifier is subjected to the same scrutiny a
  manually entered valid-format value would receive, since format validation cannot detect factual incorrectness
  and this limitation applies consistently to both paths.
WHY_IT_MATTERS: >
  Inconsistent scrutiny between import and manual entry for the same class of value would create a false sense
  of import-time verification.
DISCONFIRMING_OBSERVATION: >
  A valid-format identifier is subjected to materially different scrutiny depending on whether it arrived by
  import or manual entry.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Enter the same valid-format but factually arbitrary identifier once by import and once manually, and compare
  what each path checks.
```

## G04-ACCOUNT_ADD_GLN-Q039

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q039
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An import that updates the identifier on existing records produces the same change-history record a manual
  edit would, so the source of a change (import versus manual) does not create a gap in traceability.
WHY_IT_MATTERS: >
  A traceability gap specific to imports would hide the origin of identifier changes made in bulk.
DISCONFIRMING_OBSERVATION: >
  An identifier changed via import shows no change-history entry, or a materially different one, compared to the
  same change made manually.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Change an identifier via import on one record and manually on an equivalent record, and compare the resulting
  change history.
```

## G04-ACCOUNT_ADD_GLN-Q040

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q040
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An import that would create a duplicate identifier across two different records is handled by the same
  uniqueness rule (or explicit lack thereof) that governs manual entry, not a separate, more permissive rule.
WHY_IT_MATTERS: >
  A more permissive import-time rule would let duplicates enter specifically through bulk loading, the path
  least likely to be reviewed record-by-record.
DISCONFIRMING_OBSERVATION: >
  An import creates a duplicate identifier across two records that manual entry would have blocked.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Attempt to import a record whose identifier duplicates an existing record's value and compare the outcome to
  attempting the same duplication manually.
```

## G04-ACCOUNT_ADD_GLN-Q041

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q041
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A failed import row due to an invalid identifier is reported back with enough detail (which row, which value,
  which rule failed) to correct and resubmit, rather than a generic batch failure count.
WHY_IT_MATTERS: >
  A generic failure count forces manual row-by-row investigation of an entire batch to find one bad value.
DISCONFIRMING_OBSERVATION: >
  The import failure report for an invalid identifier gives only an aggregate failure count with no per-row
  detail identifying the offending value.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Import a batch with one row containing an invalid identifier and inspect the detail level of the resulting
  failure report.
```

## G04-ACCOUNT_ADD_GLN-Q042

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q042
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Re-running the same import file after correcting the one invalid identifier does not re-process or duplicate
  the records that were already successfully imported the first time.
WHY_IT_MATTERS: >
  Reprocessing already-imported records would risk duplicate partners or overwritten values from a stale re-run.
DISCONFIRMING_OBSERVATION: >
  Re-running a corrected import file creates duplicate records, or overwrites already-correct values, for rows
  that succeeded on the first run.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Run an import with one failing row, correct that row, and re-run the same file, then inspect the previously
  successful records.
```

## G04-ACCOUNT_ADD_GLN-Q043

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q043
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the identifier used on an already-exchanged (already-transmitted or already-received) document is later
  found to be wrong and corrected on the master record, the correction produces a record of what value the
  exchange actually used, distinct from what the master record shows going forward.
WHY_IT_MATTERS: >
  Losing the as-transmitted value would make it impossible to explain a past exchange to a counterparty or
  auditor.
DISCONFIRMING_OBSERVATION: >
  After correcting the master identifier, there is no way to retrieve what value an already-exchanged document
  actually carried at the time of exchange.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Transmit a document with one identifier value, correct the master value afterward, and attempt to retrieve the
  value actually used in the original exchange.
```

## G04-ACCOUNT_ADD_GLN-Q044

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q044
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Only a role explicitly authorized to manage partner or company master data may change the identifier; a role
  limited to document creation or transmission cannot alter it as a side effect of processing a document.
WHY_IT_MATTERS: >
  An unauthorized incidental change to master data through a document-processing action would bypass the
  intended control boundary.
DISCONFIRMING_OBSERVATION: >
  A user with only document-processing authority is able to change the identifier value on a partner or company
  record.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  As a user with only document-processing rights, attempt to alter the identifier through any document-related
  action.
```

## G04-ACCOUNT_ADD_GLN-Q045

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q045
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two concurrent edits to the same record's identifier field from two sessions do not silently result in one
  overwriting the other with no conflict indication; the later save either detects the conflict or the change
  history captures both attempts.
WHY_IT_MATTERS: >
  A silent overwrite in a multi-user environment could quietly discard a correct value someone else had just
  entered.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous edits to the same identifier field from different sessions result in one being silently
  discarded with no conflict indication or history of the discarded value.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Open the same record in two sessions and edit the identifier field in both at nearly the same time, then
  inspect the outcome.
```

## G04-ACCOUNT_ADD_GLN-Q046

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q046
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The identifier field remains available and correctly populated after a routine data migration or environment
  restore, rather than being silently dropped, blanked, or truncated by the migration process.
WHY_IT_MATTERS: >
  An identifier lost in migration would silently disable electronic exchange for every affected partner until
  discovered.
DISCONFIRMING_OBSERVATION: >
  A record's identifier value is missing, blank, or truncated after a migration or restore, despite having a
  valid value before it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record the identifier value before a migration or restore operation and compare it against the value
  afterward.
```

## G04-ACCOUNT_ADD_GLN-Q047

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q047
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the identifier is required, optional, or unused is a configuration that can differ by jurisdiction or
  business context without one context's configuration silently affecting another's records.
WHY_IT_MATTERS: >
  A shared, un-scoped configuration would force jurisdictions that do not use the identifier to be validated
  against a requirement that does not apply to them.
DISCONFIRMING_OBSERVATION: >
  Configuring the identifier as required for one jurisdiction/context makes it required, or otherwise behave
  differently, for a different, unrelated context.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure the identifier requirement differently for two contexts and verify that each context's records are
  validated according to its own configuration only.
```

## G04-ACCOUNT_ADD_GLN-Q048

```yaml
QID: G04-ACCOUNT_ADD_GLN-Q048
MODULE: account_add_gln
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A synchronization or lookup against an external registry to verify the identifier does not itself write a
  "verified" status to the record when the external registry could not actually be reached; an unreachable
  registry produces a distinct, honest status rather than a false pass.
WHY_IT_MATTERS: >
  A false "verified" status recorded during an outage would give unwarranted confidence in an unverified value.
DISCONFIRMING_OBSERVATION: >
  The record shows a verified/confirmed status for the identifier even though the external registry lookup could
  not be completed at the time.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Trigger an identifier verification lookup while the external registry is unreachable (simulated failure or
  timeout) and inspect the resulting status recorded on the record.
```

---
## GMVQ Internal QA Checklist

- [x] 48 distinct MVQ records; no padding — every record targets a distinct hypothesis.
- [x] Every record has a concrete `DISCONFIRMING_OBSERVATION`.
- [x] Questions are behavioral and source-neutral; no vendor/product name, technical identifier, or module name
      appears in question text.
- [x] Uniqueness and check-digit validation represented (Q001-Q006).
- [x] Identifier changed after documents were already issued/transmitted represented (Q007-Q012).
- [x] One legal entity with several locations and correct per-document identifier selection represented
      (Q013-Q018).
- [x] Identifier absent at moment of transmission represented (Q019-Q024).
- [x] Mismatch between identifier and address/tax registration represented (Q025-Q030).
- [x] Per-company values on a shared partner represented (Q031-Q036).
- [x] Import supplying an invalid identifier represented (Q037-Q042).
- [x] Audit trail of a change affecting an already-exchanged document represented (Q043).
- [x] Role/permission boundary, concurrency, migration survival, jurisdictional configuration scoping, and
      external-registry-unreachable honesty represented (Q044-Q048).
- [x] Tenant/company boundary represented (Q031, Q033-Q035).
- [x] No specific Thai legal or tax requirement asserted anywhere in this bank.
- [ ] Independent QA challenge outcome recorded.
- [ ] SaaS Architecture challenge outcome recorded.
- [ ] Rolling batch freeze recorded before Lane A/Lane B.

**Disposition:** AUTHORING COMPLETE FOR THIS DRAFT / QA CHALLENGE NEXT
