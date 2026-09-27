# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / partner_autocomplete Module MVQ Bank

**Document ID:** GMVQ-G03-PARTNER_AUTOCOMPLETE-MVQ48-V1.00
**Group:** G03 MASTER_DATA
**Module Metadata:** `partner_autocomplete`
**Wave:** W1
**Author Cell:** TEAM 16 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN / REVISED R3
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific MVQ set for `partner_autocomplete` under Group G03 MASTER_DATA,
targeting the reach areas named in GROUP_BRIEF_G03_MASTER_DATA.md: externally sourced values overwriting
human-entered or human-corrected values; provenance of externally sourced data; the external record being
wrong, stale, or describing a different legal entity; tax-registration and legal-name values flowing into
posted documents; per-tenant credentials, quota and third-party data exposure; service unavailability
mid-entry; and bulk enrichment over existing records with transactional history.

The question text is source-neutral: it does not name any vendor, product, table, field, method, XML ID
or API shape, and does not name the module itself outside the MODULE field.

## Control

- Every question carries a falsifiable DISCONFIRMING_OBSERVATION that is a failure state, not a restatement.
- No padding: 48 questions exist because they test 48 distinct material hypotheses.
- Questions are not evidence. A later ANSWERED state requires an actual artifact or evidence reference.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- Clean Room: authored from generic ERP domain knowledge only; no reference or vendor source tree opened.

## G03-PARTNER_AUTOCOMPLETE-Q001

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q001
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Invoking the external lookup during entry only stages suggested values for review; it does not
  commit any value to the record without an explicit accept action.
WHY_IT_MATTERS: >
  Silent auto-commit removes the human decision point that exists specifically to catch a bad
  external match.
DISCONFIRMING_OBSERVATION: >
  A field on the record is populated and saved with no separate accept step observable to the user.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Trigger the lookup on a new record and stop short of any explicit confirm action; then check
  whether the record already carries the suggested values.
```

## G03-PARTNER_AUTOCOMPLETE-Q002

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q002
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A field the user has explicitly cleared back to blank is not silently re-filled by a later
  external suggestion as though it had never been touched at all; a deliberate clearing is
  treated differently from a field that was simply never populated in the first place.
WHY_IT_MATTERS: >
  Treating a deliberate clear the same as a field nobody ever filled would let a value the
  user removed on purpose quietly reappear the next time the lookup runs.
DISCONFIRMING_OBSERVATION: >
  A field the user has explicitly emptied is refilled by the next lookup with no
  distinguishable confirmation, treated exactly as if the field had always been blank.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Accept a suggestion into a field, deliberately clear that field back to empty, then trigger
  the lookup again on the same record and observe whether the field is silently refilled.
```

## G03-PARTNER_AUTOCOMPLETE-Q003

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q003
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Re-invoking the lookup on a record that has already been populated and then further edited by a
  human treats the human's later edits as authoritative over any new suggestion.
WHY_IT_MATTERS: >
  Without this, a routine refresh silently reverses work a person already did.
DISCONFIRMING_OBSERVATION: >
  A field edited by a human after the first enrichment is silently reset by a second enrichment pass.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enrich a record, manually edit one of the populated fields, then re-trigger enrichment and compare.
```

## G03-PARTNER_AUTOCOMPLETE-Q004

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q004
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A field value that originated from the external lookup remains distinguishable, after the fact,
  from a value a person typed directly.
WHY_IT_MATTERS: >
  Without provenance, a reviewer cannot judge how much to trust a given value or investigate a bad one.
DISCONFIRMING_OBSERVATION: >
  No record state, log, or trail lets a reviewer determine, after saving, whether a given field's
  current value came from the external service or from direct entry.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Populate a record via the lookup, save it, then attempt to determine origin of each field's value
  using only normal record inspection and any audit trail available.
```

## G03-PARTNER_AUTOCOMPLETE-Q005

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q005
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a field is touched by the external lookup, the timestamp and acting identity recorded for
  that change are distinguishable from a routine manual save.
WHY_IT_MATTERS: >
  Same value, different actor: merging the two into one audit signature hides who is actually
  responsible for what is on the record.
DISCONFIRMING_OBSERVATION: >
  The change history shows an enrichment-driven update as indistinguishable from an ordinary manual
  edit by the same session's user.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger enrichment under a known user session and inspect the resulting change history entries.
```

## G03-PARTNER_AUTOCOMPLETE-Q006

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q006
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When several external candidates could plausibly match the entered name but represent different
  legal entities, the interface requires a human to pick among them rather than silently taking the
  closest text match.
WHY_IT_MATTERS: >
  A silent pick can attach one company's legal identity and obligations to an unrelated company's
  record.
DISCONFIRMING_OBSERVATION: >
  A record is populated with details from one legal entity when the entered information was ambiguous
  between two or more distinct entities, with no selection step shown.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Enter a partial or ambiguous name known to match more than one distinct entity in the external
  source and observe how the match is resolved.
```

## G03-PARTNER_AUTOCOMPLETE-Q007

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q007
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  There is a way, short of manual cross-check, for a user to recognize that an accepted external
  match may describe a different legal entity than intended.
WHY_IT_MATTERS: >
  Without any such signal, a wrong-entity match is indistinguishable from a correct one until a
  downstream failure (tax, payment) exposes it.
DISCONFIRMING_OBSERVATION: >
  The interface offers no distinguishing detail (such as registration status, address, or entity
  type) that would let a user catch a wrong-entity match before accepting it.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Trigger a lookup that returns a plausible but wrong-entity candidate and review what information
  is shown before acceptance.
```

## G03-PARTNER_AUTOCOMPLETE-Q008

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q008
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A locally cached or previously fetched external result is not reapplied as if fresh when the
  underlying external record has since changed.
WHY_IT_MATTERS: >
  Reapplying stale data can silently reintroduce a value the source itself has already corrected.
DISCONFIRMING_OBSERVATION: >
  A re-enrichment applies a cached result without any indication that the external record may have
  changed since it was first fetched.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Fetch and accept a suggestion, note its content, then re-trigger enrichment for the same record
  after enough time that the external source could plausibly have changed, and compare freshness
  handling.
```

## G03-PARTNER_AUTOCOMPLETE-Q009

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q009
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A legal-name or tax-registration value already used on a posted transaction is not altered by a
  later enrichment pass over the partner record without an explicit, separate action.
WHY_IT_MATTERS: >
  Changing identity details behind an already-posted transaction breaks the link between what was
  posted and what the record now says.
DISCONFIRMING_OBSERVATION: >
  Enriching a partner record after one of its transactions has been posted changes the legal-name or
  tax-registration value with no separate confirmation tied to the posted transaction's integrity.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a transaction for a partner, then trigger enrichment on that partner and observe whether
  identity fields change and whether the posted transaction is flagged.
```

## G03-PARTNER_AUTOCOMPLETE-Q010

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q010
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A tax-registration value supplied by the external service is validated against the same format and
  consistency rules as one typed by a human before it is accepted.
WHY_IT_MATTERS: >
  An external source is not inherently more trustworthy than a person and should not bypass
  validation a manual entry would face.
DISCONFIRMING_OBSERVATION: >
  An externally supplied tax-registration value that would fail validation if typed manually is
  accepted without triggering the same validation error.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Arrange or simulate an external response containing a malformed tax-registration value and observe
  whether normal field validation still applies.
```

## G03-PARTNER_AUTOCOMPLETE-Q011

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q011
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Credentials and quota for the external lookup service are scoped per tenant, so one tenant's usage
  cannot exhaust or degrade another tenant's access.
WHY_IT_MATTERS: >
  Shared quota across tenants turns one customer's activity into another customer's outage.
DISCONFIRMING_OBSERVATION: >
  Heavy use of the lookup feature by one tenant measurably reduces availability or remaining quota
  for a different tenant.
EXPECTED_SURFACE: S4,S7,S8
PRECONDITIONS: >
  Identify how credentials/quota are configured, and compare behavior across two distinct tenants
  under load on one of them.
```

## G03-PARTNER_AUTOCOMPLETE-Q012

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q012
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A tenant administrator can determine, from configuration alone, which external service is being
  used and what data is being sent to it, without inspecting network traffic.
WHY_IT_MATTERS: >
  An enrichment feature that transmits customer data to a third party is a data-sharing decision the
  tenant must be able to see and govern.
DISCONFIRMING_OBSERVATION: >
  No configuration screen or documentation-equivalent surface discloses which fields are transmitted
  externally when the feature runs.
EXPECTED_SURFACE: S5,S7
PRECONDITIONS: >
  Inspect the tenant-facing configuration for the feature and identify what it discloses about data
  transmitted outward.
```

## G03-PARTNER_AUTOCOMPLETE-Q013

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q013
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The feature can be fully disabled at the tenant level, and disabling it stops any outbound call
  for that tenant rather than only hiding the action in the interface.
WHY_IT_MATTERS: >
  A feature that still calls out after being "disabled" continues the data-sharing exposure the
  tenant believed they had turned off.
DISCONFIRMING_OBSERVATION: >
  With the feature disabled in configuration, an outbound call to the external service still occurs
  for that tenant through any normal path.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Disable the feature at the tenant level, then attempt every normal path that could trigger the
  lookup and observe for any outbound call.
```

## G03-PARTNER_AUTOCOMPLETE-Q014

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q014
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Only the minimum data needed to perform the lookup (such as the text the user is typing) is sent
  externally, not the full draft record.
WHY_IT_MATTERS: >
  Sending more than necessary increases exposure with no functional benefit.
DISCONFIRMING_OBSERVATION: >
  Fields unrelated to the lookup, already present in the draft record, are transmitted to the
  external service.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Populate unrelated fields on a draft record before triggering the lookup, then determine what was
  actually sent.
```

## G03-PARTNER_AUTOCOMPLETE-Q015

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q015
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the external service is unavailable when the lookup is triggered, the user can still save the
  record with manually entered values; the failure does not block record creation.
WHY_IT_MATTERS: >
  An external dependency should degrade gracefully, not become a hard blocker for basic record entry.
DISCONFIRMING_OBSERVATION: >
  With the external service made unavailable, the user cannot complete and save a new partner record
  through any normal path.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Make the external service unreachable (or simulate its absence) and attempt to create and save a
  partner record normally.
```

## G03-PARTNER_AUTOCOMPLETE-Q016

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q016
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A failed or timed-out lookup leaves no partial, half-applied field values on the record.
WHY_IT_MATTERS: >
  Partial application from a failed call is worse than no data at all, because it looks complete
  but is not.
DISCONFIRMING_OBSERVATION: >
  After a lookup fails partway through, some but not all of the expected fields are populated with
  no indication that the operation did not complete.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Interrupt or force a timeout during a lookup and inspect the record's field state immediately after.
```

## G03-PARTNER_AUTOCOMPLETE-Q017

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q017
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Retrying a lookup after a timeout does not create a duplicate business-partner record; the retry
  operates on the same in-progress record.
WHY_IT_MATTERS: >
  A duplicate created by a mechanical retry pollutes master data with no business cause.
DISCONFIRMING_OBSERVATION: >
  Retrying a timed-out lookup results in two separate partner records for what was one entry attempt.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a lookup, force a timeout, retry, and check whether more than one record now exists for
  the entry.
```

## G03-PARTNER_AUTOCOMPLETE-Q018

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q018
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Running the enrichment feature in bulk over a set of existing partner records with transactional
  history is a distinct, deliberately gated action from single-record entry-time enrichment.
WHY_IT_MATTERS: >
  Bulk enrichment over records with history has a materially larger blast radius than filling in one
  new contact and should not be reachable by accident.
DISCONFIRMING_OBSERVATION: >
  The same unrestricted action used for one new record can be applied, without any additional gate,
  to a bulk selection of existing records carrying transactional history.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Select a group of existing partner records known to carry transactional history and attempt to run
  enrichment across them, noting any additional confirmation required.
```

## G03-PARTNER_AUTOCOMPLETE-Q019

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q019
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A bulk enrichment run that encounters an ambiguous or low-confidence match for one record in the
  batch does not silently apply that low-confidence match; it is excluded or flagged for individual
  review.
WHY_IT_MATTERS: >
  Batch convenience should not lower the acceptance bar that would apply to the same match handled
  one record at a time.
DISCONFIRMING_OBSERVATION: >
  A low-confidence or ambiguous match is auto-applied during a bulk run under conditions that would
  have required explicit confirmation in single-record entry.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Include in a bulk run at least one record whose entered details are ambiguous among external
  candidates, and observe how that specific record is handled.
```

## G03-PARTNER_AUTOCOMPLETE-Q020

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q020
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user without edit rights on a given partner record's fields cannot use the enrichment action to
  change those same fields indirectly.
WHY_IT_MATTERS: >
  An enrichment shortcut must not become a side door around field-level permission.
DISCONFIRMING_OBSERVATION: >
  A user lacking direct edit rights on a field is nonetheless able to change that field's value by
  triggering enrichment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Restrict a user's edit rights on specific partner fields, then have that user trigger enrichment
  and observe whether those fields change.
```

## G03-PARTNER_AUTOCOMPLETE-Q021

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q021
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The enrichment action itself is subject to its own permission check, independent of general
  record-edit permission.
WHY_IT_MATTERS: >
  Sending a person's typed text to an external service is a distinct action from editing a record
  and may warrant separate authorization.
DISCONFIRMING_OBSERVATION: >
  Any user who can open the record for editing can trigger the external lookup, with no separate
  permission check for that specific action.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare the permission required to edit a partner record generally against the permission required
  to trigger the lookup specifically.
```

## G03-PARTNER_AUTOCOMPLETE-Q022

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q022
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the external lookup returns no result, the record is left exactly as the user had typed it,
  with no field cleared or altered.
WHY_IT_MATTERS: >
  A no-match result carries no information and must not be treated as a reason to change anything.
DISCONFIRMING_OBSERVATION: >
  A field the user had already typed is cleared, blanked, or altered after a lookup that returns no
  candidates.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enter values likely to produce no external match, trigger the lookup, and compare field values
  before and after.
```

## G03-PARTNER_AUTOCOMPLETE-Q023

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q023
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling or aborting the lookup partway through (closing the entry, navigating away) leaves the
  record in its pre-lookup state, not a partially applied one.
WHY_IT_MATTERS: >
  An abandoned action should not leave a residue the user never agreed to.
DISCONFIRMING_OBSERVATION: >
  Aborting the lookup before completion results in some suggested values being retained on the
  record.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Trigger the lookup and abandon the entry screen before any suggestion is accepted, then reopen the
  record and inspect its field values.
```

## G03-PARTNER_AUTOCOMPLETE-Q024

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q024
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  After a suggested value has been accepted onto a record, there is a way to revert specifically that
  change back to what was there before, without discarding unrelated edits made since.
WHY_IT_MATTERS: >
  Without a scoped undo, correcting one bad enrichment forces a user to manually reconstruct
  everything else that changed at the same time.
DISCONFIRMING_OBSERVATION: >
  The only way to remove an accepted enrichment value is to manually retype it, because no operation
  restores the specific prior value.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Accept an enrichment suggestion, make an unrelated edit afterward, then attempt to revert only the
  enrichment-sourced value.
```

## G03-PARTNER_AUTOCOMPLETE-Q025

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q025
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A malformed or unexpected response from the external service (wrong shape, unexpected characters,
  truncated data) is rejected by validation rather than partially written to the record.
WHY_IT_MATTERS: >
  Treating the external service as fully trustworthy input skips the safety net that protects data
  quality.
DISCONFIRMING_OBSERVATION: >
  A malformed external response results in a garbled or truncated value being saved to a record
  field.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Arrange or simulate a malformed response from the external service and observe what, if anything,
  is written to the record.
```

## G03-PARTNER_AUTOCOMPLETE-Q026

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q026
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The lookup is only triggered by an explicit user action on the partner record itself, not
  automatically as a side effect of an unrelated action in another part of the system.
WHY_IT_MATTERS: >
  An invisible trigger from another workflow removes the user's opportunity to decide whether
  external data-sharing should happen at all.
DISCONFIRMING_OBSERVATION: >
  Completing an unrelated action elsewhere in the system causes the external lookup to fire for a
  partner record without the user having asked for it there.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Exercise flows in other areas that reference or create partner records and observe whether any of
  them silently trigger the external lookup.
```

## G03-PARTNER_AUTOCOMPLETE-Q027

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q027
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The feature can be turned off tenant-wide through configuration, and doing so is honored
  consistently across every entry point that could otherwise trigger it.
WHY_IT_MATTERS: >
  A feature that can be disabled from one entry point but not another gives a false sense of control.
DISCONFIRMING_OBSERVATION: >
  Disabling the feature suppresses it at one entry point (for example, manual creation) but it still
  fires from another entry point (for example, an import or a related workflow).
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Disable the feature tenant-wide, then exercise every known entry point that could invoke it and
  compare results.
```

## G03-PARTNER_AUTOCOMPLETE-Q028

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q028
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Every accepted enrichment action leaves an audit trail entry sufficient to identify what changed,
  when, and under which session.
WHY_IT_MATTERS: >
  Without this, an incorrect external value discovered later cannot be traced to when or how it
  entered the record.
DISCONFIRMING_OBSERVATION: >
  An accepted enrichment change to a record leaves no trace distinguishing it from the record's other
  history, or leaves no trace at all.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Accept an enrichment suggestion and inspect the record's available history or audit surface for a
  corresponding entry.
```

## G03-PARTNER_AUTOCOMPLETE-Q029

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q029
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A suggestion the user was shown but declined or discarded is not silently forgotten in a way that
  prevents later investigation of why a record looks the way it does.
WHY_IT_MATTERS: >
  When a wrong value later causes a problem, knowing what was offered and rejected matters as much as
  knowing what was accepted.
DISCONFIRMING_OBSERVATION: >
  There is no way, after the fact, to determine that a lookup was performed and its suggestion
  declined, versus no lookup ever having happened.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger a lookup, decline the suggestion offered, and then attempt to determine afterward that this
  occurred.
```

## G03-PARTNER_AUTOCOMPLETE-Q030

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q030
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An external match resolved while working in the context of one company does not populate or affect
  a shared partner record's data as seen from a different company without an explicit cross-company
  rule.
WHY_IT_MATTERS: >
  An enrichment performed under one company's context should not silently become another company's
  data.
DISCONFIRMING_OBSERVATION: >
  A value applied to a partner record while working under one company appears, without an explicit
  sharing rule, on that same partner as seen under a different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Trigger enrichment on a partner shared across two companies while operating under one company
  context, then inspect the record under the other company context.
```

## G03-PARTNER_AUTOCOMPLETE-Q031

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q031
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two users triggering the lookup and each accepting a different candidate for the same record at
  nearly the same time results in a deterministic, non-corrupted final state, not a mixed record
  combining both suggestions.
WHY_IT_MATTERS: >
  Concurrent acceptance without conflict handling can leave a record with an internally inconsistent
  mix of two different entities' details.
DISCONFIRMING_OBSERVATION: >
  The saved record after two concurrent, different acceptances contains a field-level mixture
  inconsistent with either candidate on its own.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Have two sessions trigger the lookup on the same new record concurrently, each accepting a
  different candidate, and inspect the final saved state.
```

## G03-PARTNER_AUTOCOMPLETE-Q032

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q032
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An enrichment acceptance that completes after a concurrent manual edit to the same field does not
  silently overwrite the more recent manual edit without some conflict signal.
WHY_IT_MATTERS: >
  A slow external round-trip should not be allowed to win a race against a person's real-time
  correction.
DISCONFIRMING_OBSERVATION: >
  A manual edit made after an enrichment was triggered is overwritten when that enrichment's
  suggestion is later accepted, with no warning of the conflict.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger enrichment, then before accepting its suggestion, manually edit the same field, then accept
  the suggestion and observe the outcome.
```

## G03-PARTNER_AUTOCOMPLETE-Q033

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q033
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The lookup can be invoked both when a partner record is first created and later during an edit of
  an existing record, not only at creation.
WHY_IT_MATTERS: >
  A record's details drift out of date over time, and restricting the capability to creation-only
  removes a legitimate later use.
DISCONFIRMING_OBSERVATION: >
  The lookup action is unavailable when editing an already-saved partner record, even though the same
  details might legitimately need refreshing.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Open an existing, previously saved partner record for editing and check whether the lookup action
  is available.
```

## G03-PARTNER_AUTOCOMPLETE-Q034

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q034
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If the required external credential is missing or invalid for a tenant, the feature fails in a way
  that is visible to an administrator, rather than silently doing nothing.
WHY_IT_MATTERS: >
  A silent no-op looks identical to "there was simply no match," hiding a configuration problem
  indefinitely.
DISCONFIRMING_OBSERVATION: >
  With the credential missing or invalid, triggering the lookup produces no error, warning, or log
  distinguishable from a normal no-match result.
EXPECTED_SURFACE: S3,S6,S7
PRECONDITIONS: >
  Remove or invalidate the tenant's configured credential for the service, then trigger the lookup
  and observe the resulting behavior and any diagnostic signal.
```

## G03-PARTNER_AUTOCOMPLETE-Q035

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q035
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The behavior described for when and how a suggestion is applied (automatic versus requiring
  explicit acceptance) matches what is actually observed when the feature runs.
WHY_IT_MATTERS: >
  A gap between described and actual behavior means whoever relies on the description is operating on
  a false assumption about a data-sharing and data-integrity control.
DISCONFIRMING_OBSERVATION: >
  The feature applies a suggestion automatically in a situation where the intended behavior is an
  explicit accept step, or the reverse.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Compare the documented or configured expected behavior for suggestion application against what is
  actually observed for at least one concrete case.
```

## G03-PARTNER_AUTOCOMPLETE-Q036

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q036
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Data entered by a tenant and sent to the external service is not knowingly transmitted to a service
  location outside the jurisdiction the tenant has configured or agreed to.
WHY_IT_MATTERS: >
  Sending customer data across a jurisdiction boundary without disclosure is a data-residency exposure
  separate from the accuracy of the lookup itself.
DISCONFIRMING_OBSERVATION: >
  The external service used for a tenant is hosted or operated in a jurisdiction different from what
  the tenant's configuration or agreement specifies, with no disclosure.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Determine which external service endpoint is actually used for a tenant and compare it against that
  tenant's configured or expected jurisdiction.
```

## G03-PARTNER_AUTOCOMPLETE-Q037

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q037
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the external service's usage limit is reached, the user triggering the lookup receives a clear
  indication that the limit was hit, rather than an unexplained no-result outcome.
WHY_IT_MATTERS: >
  An unexplained failure indistinguishable from "no match" leads users to conclude incorrectly that
  the partner simply isn't in the external source.
DISCONFIRMING_OBSERVATION: >
  Reaching the usage limit produces the same visible outcome to the user as a genuine no-match result.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Drive tenant usage of the lookup to its configured limit and then trigger one more lookup,
  observing the message shown.
```

## G03-PARTNER_AUTOCOMPLETE-Q038

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q038
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The lookup only fills fields that are currently empty; it does not overwrite a field that already
  holds any value, whether previously entered manually or by an earlier enrichment.
WHY_IT_MATTERS: >
  Otherwise, "already partially filled" and "genuinely blank" get treated identically, silently
  overriding anything already present.
DISCONFIRMING_OBSERVATION: >
  A field that already contains a value, however it got there, is replaced by a new suggestion
  without a distinct confirmation for that already-filled field.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Pre-fill one field with a value, leave others empty, trigger the lookup, and compare which fields
  changed.
```

## G03-PARTNER_AUTOCOMPLETE-Q039

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q039
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When more than one external candidate is returned, some indication of match confidence or quality
  is shown to the user before they choose one.
WHY_IT_MATTERS: >
  Without any signal of confidence, a user has no basis to prefer one plausible-looking candidate over
  another.
DISCONFIRMING_OBSERVATION: >
  Multiple candidates are presented with no distinguishing quality or confidence indicator, forcing an
  uninformed choice.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Trigger a lookup known to return multiple candidates and inspect what is shown about each.
```

## G03-PARTNER_AUTOCOMPLETE-Q040

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q040
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Accepting an external suggestion does not, by itself, change the record's own verification or trust
  status to anything resembling "confirmed" or "verified."
WHY_IT_MATTERS: >
  External data is a starting point, not a substitute for whatever verification process the business
  actually requires.
DISCONFIRMING_OBSERVATION: >
  A record's status or classification changes to a verified-like state solely because an external
  suggestion was accepted, with no separate verification step performed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Accept an enrichment suggestion on a new record and check whether any status field changed as a
  side effect.
```

## G03-PARTNER_AUTOCOMPLETE-Q041

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q041
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An external match that closely resembles an existing partner record already in the system triggers
  the same duplicate-detection response that a manually entered near-duplicate would.
WHY_IT_MATTERS: >
  Enrichment is still a way of creating or changing partner data and should not bypass the safeguard
  against duplicate master data.
DISCONFIRMING_OBSERVATION: >
  Accepting an external suggestion creates or leaves a near-duplicate of an existing partner record
  with no duplicate warning that a manual entry of the same data would have raised.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger enrichment with details that closely match an existing partner record and observe whether
  duplicate detection engages.
```

## G03-PARTNER_AUTOCOMPLETE-Q042

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q042
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Address or registration details belonging to one entity within a related group of entities are not
  applied to a different, related-but-distinct entity's record merely because the two share a name or
  brand.
WHY_IT_MATTERS: >
  Related entities in a group commonly share a public name while remaining legally and financially
  distinct; conflating them misattributes tax and legal obligations.
DISCONFIRMING_OBSERVATION: >
  A record for one entity in a related group receives registration or address details belonging to a
  different, distinct entity in the same group.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a lookup using a name shared by two distinct, related entities and observe which entity's
  details are actually offered or applied.
```

## G03-PARTNER_AUTOCOMPLETE-Q043

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q043
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  After a human has corrected a value that was originally populated by enrichment, a later scheduled
  or background synchronization does not silently reapply the original external value over the
  human's correction.
WHY_IT_MATTERS: >
  A background process re-introducing an already-rejected value defeats the correction with no
  visible cause.
DISCONFIRMING_OBSERVATION: >
  A field corrected by a human reverts to its earlier external value after a scheduled or background
  process runs, with no new explicit user action.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Correct a field that was originally set by enrichment, then allow or trigger any scheduled
  background processing associated with the feature and check the field afterward.
```

## G03-PARTNER_AUTOCOMPLETE-Q044

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q044
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing which external data provider is configured for the lookup does not affect a request that
  is already in flight; an in-flight request completes against the provider it started with.
WHY_IT_MATTERS: >
  An in-flight switch of provider mid-request risks mixing behavior or data from two different
  services without the user knowing which one actually answered.
DISCONFIRMING_OBSERVATION: >
  An in-flight lookup returns a result that appears to have come from a provider different from the
  one configured when it was triggered, with no indication of the switch.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Trigger a lookup, change the configured provider before the request completes, and observe which
  provider's characteristics the result reflects.
```

## G03-PARTNER_AUTOCOMPLETE-Q045

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q045
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The lookup's write scope is limited to the specific fields it is meant to populate; it never
  touches unrelated fields elsewhere on the record.
WHY_IT_MATTERS: >
  An enrichment feature with an unbounded write scope is a much larger integrity risk than one
  confined to its stated purpose.
DISCONFIRMING_OBSERVATION: >
  A field with no stated connection to the lookup's purpose changes value after an enrichment action.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record the full field state of a partner record before triggering enrichment, then compare the full
  state after, looking beyond the fields the feature is meant to fill.
```

## G03-PARTNER_AUTOCOMPLETE-Q046

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q046
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Triggering the lookup on an archived or inactive partner record is either blocked or clearly
  flagged as unusual, rather than treated identically to an active record.
WHY_IT_MATTERS: >
  Enriching an inactive record is rarely intended and may indicate the wrong record was selected.
DISCONFIRMING_OBSERVATION: >
  The lookup runs on an archived or inactive partner record exactly as it would on an active one, with
  no distinguishing prompt.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Archive or deactivate a partner record, then attempt to trigger the lookup on it and observe the
  result.
```

## G03-PARTNER_AUTOCOMPLETE-Q047

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q047
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A reviewer can determine, for any given field on a record, whether it has ever been touched by the
  enrichment feature at any point in its history, not only for the most recent change.
WHY_IT_MATTERS: >
  A field's full provenance, not just its latest change, matters when investigating how a record
  ended up the way it did.
DISCONFIRMING_OBSERVATION: >
  A field that was touched by enrichment at some point in the past, then edited manually since, shows
  no trace of the earlier enrichment touch anywhere available to a reviewer.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Enrich a field, later edit it manually, and then attempt to determine the field's full history of
  origin.
```

## G03-PARTNER_AUTOCOMPLETE-Q048

```yaml
QID: G03-PARTNER_AUTOCOMPLETE-Q048
MODULE: partner_autocomplete
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A value supplied by the external service that would fail the record's own validation rules is
  rejected outright and never partially saved to the record.
WHY_IT_MATTERS: >
  Otherwise, an external source can put a record into a state a manual entry would never have been
  allowed to create.
DISCONFIRMING_OBSERVATION: >
  An externally supplied value that fails the record's own validation is nonetheless saved, wholly or
  in part, to the record.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Arrange or simulate an external suggestion containing a value that would fail normal field
  validation, and observe what is saved.
```

## CHANGE_REASON (R3)

- **QID revised:** G03-PARTNER_AUTOCOMPLETE-Q002
- **Returned by:** M3 (GMVQ Master Audit Team), DUPLICATE_OVERLAP finding against
  G03-PARTNER_AUTOCOMPLETE-Q038
- **Directive:** SMEPLUS-GMVQ-20P-5AUDIT-20260927-004
- **Old event tested:** a manually entered or corrected value being overwritten by a later
  external suggestion (a strict subset of Q038's broader "any already-held value overwritten"
  event).
- **New event tested:** a field the user has deliberately cleared back to blank being
  silently re-filled by the next lookup as though it had never been touched, rather than the
  clear being treated as a deliberate signal.
- **Disposition:** QID preserved, question rewritten in place per authoring standard section 7.
  No silent correction — recorded here per governance requirement.
