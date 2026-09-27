# SMEsPlus ENTERPRISE SUITE
## GMVQ — G03 MASTER_DATA / base_geolocalize Module MVQ Bank

**Document ID:** GMVQ-G03-BASE_GEOLOCALIZE-MVQ48-V1.00
**Group:** G03 MASTER_DATA
**Module Metadata:** `base_geolocalize`
**Wave:** W1
**Author Cell:** TEAM 15 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded

## Purpose

This bank provides the module-specific MVQ set for the module responsible for deriving map
coordinates for an address from an external lookup service. It targets staleness, precedence
between human-provided and machine-derived location data, third-party data exposure and tenant
isolation, bulk-processing failure modes, and the downstream business decisions that end up
trusting a derived coordinate.

The question text is source-neutral and does not expose vendor names, model names, field
names, method names, XML IDs, or API shapes.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material hypothesis.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `MODULE + QID` is a Research Evidence Join Key only; no coverage is claimed from this bank.
- Clean Room: generic ERP domain knowledge only; question text was drafted without opening
  any reference or vendor source tree.

## G03-BASE_GEOLOCALIZE-Q001

```yaml
QID: G03-BASE_GEOLOCALIZE-Q001
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A location for a record with a complete address is derived automatically without requiring
  an explicit user action.
WHY_IT_MATTERS: >
  If derivation is not automatic, records silently lack location data and any process relying
  on it is blind for those records with no visible cause.
DISCONFIRMING_OBSERVATION: >
  A record with a complete, valid address is saved and no location is derived without a
  separate explicit trigger, with no error or notice explaining why.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Create a record with a complete, unambiguous address and observe whether a location value
  appears without further action.
```

## G03-BASE_GEOLOCALIZE-Q002

```yaml
QID: G03-BASE_GEOLOCALIZE-Q002
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the address on a record changes, a previously derived location is not silently kept
  as if it still matched the new address.
WHY_IT_MATTERS: >
  A stale location silently attached to a changed address misroutes any downstream decision
  that trusts it.
DISCONFIRMING_OBSERVATION: >
  A record's address is changed to a materially different location and the previously derived
  coordinate remains displayed and usable with no re-derivation, invalidation, or warning.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Derive a location for a record, then edit the address to a distant location and inspect the
  stored location value afterward.
```

## G03-BASE_GEOLOCALIZE-Q003

```yaml
QID: G03-BASE_GEOLOCALIZE-Q003
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An address missing a required component (such as no locality or no country) does not
  produce a silently accepted, low-precision location presented as equivalent to a fully
  resolved one.
WHY_IT_MATTERS: >
  A coarse guess indistinguishable from a precise result misleads any use that assumes
  precision.
DISCONFIRMING_OBSERVATION: >
  An address missing a required component still yields a location with no indication that
  precision is degraded compared to a fully specified address.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt derivation for an address missing one required structural component and compare the
  result and its metadata against a complete address.
```

## G03-BASE_GEOLOCALIZE-Q004

```yaml
QID: G03-BASE_GEOLOCALIZE-Q004
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external lookup service is unreachable, the record is left without a location and
  the failure is surfaced rather than a fabricated or default coordinate being stored.
WHY_IT_MATTERS: >
  A fabricated coordinate stored during an outage looks identical to a real one and silently
  corrupts later decisions.
DISCONFIRMING_OBSERVATION: >
  While the external service is unreachable, a record still receives a stored location value,
  or a placeholder value indistinguishable from a real derived one.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Make the external lookup path unreachable (network block, invalid endpoint) and attempt
  derivation for a valid address.
```

## G03-BASE_GEOLOCALIZE-Q005

```yaml
QID: G03-BASE_GEOLOCALIZE-Q005
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external service reports a quota or rate limit has been exceeded, pending
  derivations are queued or deferred rather than treated as permanent failures.
WHY_IT_MATTERS: >
  Treating a temporary throttle as permanent failure can strand records without location
  indefinitely or trigger unnecessary manual rework.
DISCONFIRMING_OBSERVATION: >
  A rate-limit response from the external service causes an affected record to be marked as
  permanently failed or unresolvable rather than retried later.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Simulate or reach a rate-limited response from the external service during a batch of
  derivations and inspect the state of the throttled records afterward.
```

## G03-BASE_GEOLOCALIZE-Q006

```yaml
QID: G03-BASE_GEOLOCALIZE-Q006
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the external service returns more than one plausible match for an address, the system
  does not silently pick one without recording that the match was ambiguous.
WHY_IT_MATTERS: >
  A silently chosen ambiguous match presented as a single confident answer hides real
  uncertainty from anyone relying on it.
DISCONFIRMING_OBSERVATION: >
  An address known to produce multiple plausible external matches results in one location
  being stored with no trace that alternatives existed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit an address expected to be ambiguous (a common street name with no additional
  disambiguation) and inspect what is stored and whether ambiguity is recorded.
```

## G03-BASE_GEOLOCALIZE-Q007

```yaml
QID: G03-BASE_GEOLOCALIZE-Q007
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A location that a human has manually set or corrected is not overwritten by a later
  automatic derivation unless that overwrite is explicitly requested.
WHY_IT_MATTERS: >
  Silently discarding a human correction reintroduces the exact error the human fixed, without
  warning.
DISCONFIRMING_OBSERVATION: >
  A manually corrected location is replaced by a fresh automatic derivation through an
  ordinary save or background pass, with no explicit instruction to re-derive.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Manually set a location value that differs from what automatic derivation would produce,
  then trigger an ordinary save or scheduled pass and check whether the manual value survives.
```

## G03-BASE_GEOLOCALIZE-Q008

```yaml
QID: G03-BASE_GEOLOCALIZE-Q008
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a record with a manually set location has an unrelated field edited (not the address),
  the manual location is preserved.
WHY_IT_MATTERS: >
  An overly broad re-derivation trigger destroys manual corrections on every unrelated edit,
  making manual correction pointless.
DISCONFIRMING_OBSERVATION: >
  Editing a field unrelated to the address on a record with a manually set location causes
  that location to be silently recalculated or cleared.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Manually set a location, then edit an unrelated field on the same record and inspect the
  location value afterward.
```

## G03-BASE_GEOLOCALIZE-Q009

```yaml
QID: G03-BASE_GEOLOCALIZE-Q009
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The precision level of a derived location (an exact point versus an area-level
  approximation) is retrievable, not only the coordinate itself.
WHY_IT_MATTERS: >
  Without a precision indicator, a rough approximation is indistinguishable from an exact
  result to anyone consuming it.
DISCONFIRMING_OBSERVATION: >
  Two addresses that were resolved at clearly different precision levels expose no retrievable
  difference beyond the raw coordinate pair.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Derive locations for one precise address and one only resolvable to a coarse area, and
  compare what metadata is available for each.
```

## G03-BASE_GEOLOCALIZE-Q010

```yaml
QID: G03-BASE_GEOLOCALIZE-Q010
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A bulk pass that derives locations for historical records processes only records that
  actually lack a location, not every record in scope.
WHY_IT_MATTERS: >
  Reprocessing records that already have a trustworthy location wastes quota and risks
  silently overwriting values a human had set.
DISCONFIRMING_OBSERVATION: >
  Running the bulk pass causes records that already carry a location to be re-derived and
  changed without being selected for that purpose.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Set up a mix of records with and without existing locations, including at least one manually
  set value, then run the bulk backfill and inspect which records changed.
```

## G03-BASE_GEOLOCALIZE-Q011

```yaml
QID: G03-BASE_GEOLOCALIZE-Q011
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A bulk backfill pass does not overwrite a location a human has manually set, even when that
  record is included in the backfill's scope.
WHY_IT_MATTERS: >
  A backfill silently clobbering manual corrections at scale destroys trust in the correction
  mechanism across the whole dataset at once.
DISCONFIRMING_OBSERVATION: >
  A record with a manually set location, included in a bulk backfill run, ends up with its
  location replaced by the automatic value.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Include a manually corrected record inside the scope of a bulk backfill run and compare its
  location before and after.
```

## G03-BASE_GEOLOCALIZE-Q012

```yaml
QID: G03-BASE_GEOLOCALIZE-Q012
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a bulk backfill run is interrupted partway through, resuming or re-running it does not
  silently skip the records that had not yet been processed.
WHY_IT_MATTERS: >
  Silent skipping after an interruption leaves an unknown subset of historical records
  permanently without location, with no visible trace of the gap.
DISCONFIRMING_OBSERVATION: >
  After an interrupted bulk run, a subsequent run or resume completes as if finished while
  records that were never reached remain without a location and without any flag identifying
  them.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Start a bulk backfill covering many records, interrupt it partway, then resume or re-run it
  and check whether every originally targeted record was eventually reached or flagged.
```
## G03-BASE_GEOLOCALIZE-Q013

```yaml
QID: G03-BASE_GEOLOCALIZE-Q013
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A downstream process that assigns territory, routing, or delivery based on a record's
  location uses the currently stored value, and that value is not silently reused after being
  marked stale.
WHY_IT_MATTERS: >
  A downstream routing or territory decision made on a coordinate known to be stale can
  misdirect a delivery or misassign a legal or tax boundary.
DISCONFIRMING_OBSERVATION: >
  A downstream assignment decision is made using a location value that has already been
  flagged or known as stale, with no re-check or warning.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Mark a record's location stale (through an address change not yet re-derived) and then
  trigger a downstream process that depends on location before re-derivation occurs.
```

## G03-BASE_GEOLOCALIZE-Q014

```yaml
QID: G03-BASE_GEOLOCALIZE-Q014
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a downstream business decision (routing, delivery zone, territory) is made using a
  derived location, which location value and precision were used at that moment is
  reconstructable afterward.
WHY_IT_MATTERS: >
  Without that trace, a misrouted outcome cannot be diagnosed back to a specific coordinate or
  precision level.
DISCONFIRMING_OBSERVATION: >
  After a downstream assignment is made, there is no way to determine which location value or
  precision level was in effect at the time the decision was taken.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger a downstream assignment dependent on location, then attempt to reconstruct which
  stored location and precision were used for that specific decision.
```

## G03-BASE_GEOLOCALIZE-Q015

```yaml
QID: G03-BASE_GEOLOCALIZE-Q015
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Each tenant's use of the external lookup service is authenticated with credentials scoped to
  that tenant, not a credential shared indistinguishably across tenants.
WHY_IT_MATTERS: >
  A shared credential prevents attributing cost, quota consumption, or a data exposure
  incident to the responsible tenant.
DISCONFIRMING_OBSERVATION: >
  Two distinct tenants' lookup requests are indistinguishable from the external service's
  perspective, or from any internal log, as coming from different tenants.
EXPECTED_SURFACE: S4,S6,S7
PRECONDITIONS: >
  Configure two tenants with the feature enabled and inspect what credential or identifying
  context each tenant's requests carry.
```

## G03-BASE_GEOLOCALIZE-Q016

```yaml
QID: G03-BASE_GEOLOCALIZE-Q016
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A tenant without valid credentials configured for the external service receives a clear
  configuration failure rather than requests silently failing or falling back to another
  tenant's credentials.
WHY_IT_MATTERS: >
  Falling back to another tenant's credential would leak paid quota or access across a tenant
  boundary; a silent failure hides a fixable misconfiguration.
DISCONFIRMING_OBSERVATION: >
  A tenant with no valid credential configured either has requests succeed (implying another
  tenant's credential was used) or fails with no indication that credentials are the cause.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Remove or invalidate the credential for one tenant while leaving the feature enabled, then
  attempt a derivation for that tenant.
```

## G03-BASE_GEOLOCALIZE-Q017

```yaml
QID: G03-BASE_GEOLOCALIZE-Q017
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Quota consumed against the external service is attributable to the specific tenant whose
  records triggered it, not pooled in a way that makes one tenant's usage invisible.
WHY_IT_MATTERS: >
  Without attribution, one tenant's heavy usage can exhaust quota for every other tenant with
  no way to identify the cause.
DISCONFIRMING_OBSERVATION: >
  After heavy usage by one tenant, there is no record that lets that tenant's consumption be
  distinguished from any other tenant's.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Generate a burst of derivations for one tenant and attempt to determine, from available
  records, how much quota that tenant specifically consumed.
```

## G03-BASE_GEOLOCALIZE-Q018

```yaml
QID: G03-BASE_GEOLOCALIZE-Q018
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  One tenant exhausting its own quota does not prevent another tenant's derivations from
  proceeding.
WHY_IT_MATTERS: >
  A shared quota pool turns one tenant's usage spike into an outage for every unrelated
  tenant.
DISCONFIRMING_OBSERVATION: >
  Exhausting the quota available to one tenant causes derivation requests from an unrelated
  tenant to fail or queue.
EXPECTED_SURFACE: S3,S4,S8
PRECONDITIONS: >
  Drive one tenant's usage to its configured limit and, in the same window, attempt a
  derivation for a different tenant.
```

## G03-BASE_GEOLOCALIZE-Q019

```yaml
QID: G03-BASE_GEOLOCALIZE-Q019
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Which region or jurisdiction processes an address sent to the external service is known and
  documented, not left undetermined.
WHY_IT_MATTERS: >
  Sending a customer address to an undetermined jurisdiction can conflict with a
  data-residency obligation the business has committed to.
DISCONFIRMING_OBSERVATION: >
  No documentation or observable configuration indicates which region processes the
  transmitted address data, and it cannot be constrained.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Review the configuration surface for the external lookup integration for any control or
  documentation of processing region.
```

## G03-BASE_GEOLOCALIZE-Q020

```yaml
QID: G03-BASE_GEOLOCALIZE-Q020
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Only the address fields necessary for the lookup are transmitted to the external service,
  not the full customer record.
WHY_IT_MATTERS: >
  Sending unrelated customer data externally expands the exposure surface with no business
  benefit.
DISCONFIRMING_OBSERVATION: >
  Fields unrelated to the address (unrelated personal or financial fields) are observed
  leaving the system as part of the lookup request.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Inspect or intercept the outbound request made during a derivation to see exactly which
  fields are transmitted.
```

## G03-BASE_GEOLOCALIZE-Q021

```yaml
QID: G03-BASE_GEOLOCALIZE-Q021
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An identical address that has already been resolved for one record can be served from a
  stored result without a fresh external call for every occurrence.
WHY_IT_MATTERS: >
  Without reuse, quota is consumed and cost incurred repeatedly for addresses already known,
  unnecessarily increasing exposure and expense.
DISCONFIRMING_OBSERVATION: >
  Deriving a location for an address identical to one already resolved elsewhere always issues
  a fresh external call with no reuse of the existing result.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Resolve one address, then create a second record with the identical address and observe
  whether a new external call occurs.
```

## G03-BASE_GEOLOCALIZE-Q022

```yaml
QID: G03-BASE_GEOLOCALIZE-Q022
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A reused prior result has a defined age after which it is no longer trusted without
  re-verification.
WHY_IT_MATTERS: >
  An indefinitely reused result can silently diverge from reality (a real-world address
  renumbering) with no mechanism to catch it.
DISCONFIRMING_OBSERVATION: >
  A very old cached result is reused indefinitely with no policy or mechanism that would ever
  trigger re-verification.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Locate a long-unchanged cached result and determine whether any configured policy would ever
  cause it to be re-checked.
```

## G03-BASE_GEOLOCALIZE-Q023

```yaml
QID: G03-BASE_GEOLOCALIZE-Q023
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When many derivations are requested at once, they are throttled and queued rather than a
  subset being silently dropped.
WHY_IT_MATTERS: >
  Silent dropping under load leaves an unpredictable subset of records without location with
  no error to explain why.
DISCONFIRMING_OBSERVATION: >
  A large simultaneous batch of derivation requests results in some requests vanishing with no
  record of having been attempted, queued, or failed.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Submit a large batch of derivation requests at once and account for every request's eventual
  outcome.
```

## G03-BASE_GEOLOCALIZE-Q024

```yaml
QID: G03-BASE_GEOLOCALIZE-Q024
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a record's address is edited by one process while a background derivation for the prior
  address is still in flight, the in-flight result does not overwrite the newer address's
  eventual result.
WHY_IT_MATTERS: >
  A race between an in-flight stale lookup and a newer edit can leave a record with a location
  that matches neither address it ever had.
DISCONFIRMING_OBSERVATION: >
  A record ends up with a location that corresponds to neither its address at the time the
  lookup started nor its address at the time the lookup returned.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger a derivation for a record, immediately change its address before the derivation
  returns, and inspect the final stored location once both operations settle.
```
## G03-BASE_GEOLOCALIZE-Q025

```yaml
QID: G03-BASE_GEOLOCALIZE-Q025
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A manual correction made to a record while a bulk backfill is running is not overwritten by
  that same in-progress bulk run.
WHY_IT_MATTERS: >
  Without this protection, the timing of an unrelated bulk job determines whether a manual
  correction survives, which is not a business-meaningful rule.
DISCONFIRMING_OBSERVATION: >
  A manual correction applied during a running bulk backfill is overwritten by that bulk run
  before it completes.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Start a bulk backfill covering a record, and while it is running, manually correct that
  record's location, then check the value once the bulk run finishes.
```

## G03-BASE_GEOLOCALIZE-Q026

```yaml
QID: G03-BASE_GEOLOCALIZE-Q026
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Clearing a record's address also clears or clearly invalidates its previously derived
  location, rather than leaving an orphaned coordinate attached to no address.
WHY_IT_MATTERS: >
  An orphaned coordinate with no corresponding address can be used downstream without anyone
  realizing it no longer corresponds to anything.
DISCONFIRMING_OBSERVATION: >
  An address is fully cleared from a record while a previously derived location remains
  present and usable as if still valid.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Derive a location for a record, then clear its address entirely and inspect whether the
  location value is also cleared or flagged.
```

## G03-BASE_GEOLOCALIZE-Q027

```yaml
QID: G03-BASE_GEOLOCALIZE-Q027
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two unrelated records that happen to share the exact same address each hold their own
  independent location value, not a single shared reference that changes for both if one is
  corrected.
WHY_IT_MATTERS: >
  A shared reference would let correcting one record's location silently change an unrelated
  record's location too.
DISCONFIRMING_OBSERVATION: >
  Manually correcting the location on one record changes the stored location on a different,
  unrelated record that happens to share the same address text.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Create two unrelated records with identical address text, then manually correct the location
  on one and check whether the other changed.
```

## G03-BASE_GEOLOCALIZE-Q028

```yaml
QID: G03-BASE_GEOLOCALIZE-Q028
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An address written in a local script or format for one country resolves with comparable
  reliability to one written in a Western/Latin format, not silently failing only for
  non-Latin input.
WHY_IT_MATTERS: >
  A silent bias toward one script or format leaves certain customer populations permanently
  without usable location data.
DISCONFIRMING_OBSERVATION: >
  An address in a non-Latin local script or a locally standard format fails to resolve or
  resolves at markedly worse precision than an equivalent Western-format address, with no
  indication of the limitation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit comparable addresses in a local non-Latin script and in a Western format and compare
  the results and any surfaced precision or error.
```

## G03-BASE_GEOLOCALIZE-Q029

```yaml
QID: G03-BASE_GEOLOCALIZE-Q029
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If more than one external lookup provider can be configured, a failure with the primary
  provider does not silently leave the record unresolved when a fallback is configured and
  available.
WHY_IT_MATTERS: >
  An unused fallback defeats the purpose of configuring resilience and hides an avoidable gap
  in coverage.
DISCONFIRMING_OBSERVATION: >
  With a fallback provider configured and available, a primary-provider failure still leaves
  the record without an attempted fallback resolution.
EXPECTED_SURFACE: S3,S7,S8
PRECONDITIONS: >
  Configure a fallback provider, force the primary to fail, and observe whether the fallback is
  attempted.
```

## G03-BASE_GEOLOCALIZE-Q030

```yaml
QID: G03-BASE_GEOLOCALIZE-Q030
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Switching the configured external provider does not silently leave historical records
  derived under the old provider indistinguishable from ones derived under the new provider,
  when the two could disagree.
WHY_IT_MATTERS: >
  Two providers can disagree on the same address; not knowing which provider produced a
  historical value prevents explaining a discrepancy later.
DISCONFIRMING_OBSERVATION: >
  After switching providers, there is no way to determine whether an existing stored location
  came from the old or the new provider.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Derive locations under one provider configuration, switch the configured provider, and check
  whether existing records retain any indication of which provider produced their value.
```

## G03-BASE_GEOLOCALIZE-Q031

```yaml
QID: G03-BASE_GEOLOCALIZE-Q031
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A background derivation pass does not spend quota re-deriving locations for records that have
  been archived or deactivated.
WHY_IT_MATTERS: >
  Processing inactive records wastes quota that active, in-use records need and increases
  needless external exposure of retired data.
DISCONFIRMING_OBSERVATION: >
  An archived or deactivated record is included and processed in a routine background
  derivation pass alongside active records.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Archive or deactivate a record lacking a location, then run the routine background pass and
  check whether that record was processed.
```

## G03-BASE_GEOLOCALIZE-Q032

```yaml
QID: G03-BASE_GEOLOCALIZE-Q032
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Triggering a manual re-derivation for a record requires the same level of access as editing
  that record, not a lesser one.
WHY_IT_MATTERS: >
  If re-derivation needs less access than editing, a lower-privileged user could indirectly
  overwrite a value they are not otherwise allowed to change.
DISCONFIRMING_OBSERVATION: >
  A user without edit access to a record can still trigger a re-derivation that changes its
  stored location.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user without edit rights on a given record, attempt to trigger a manual re-derivation
  for it.
```

## G03-BASE_GEOLOCALIZE-Q033

```yaml
QID: G03-BASE_GEOLOCALIZE-Q033
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Visibility of the raw derived coordinate follows the same access scope as the address it was
  derived from, not a broader one.
WHY_IT_MATTERS: >
  A coordinate visible beyond the scope of its source address exposes precise location
  information to users who should not have it.
DISCONFIRMING_OBSERVATION: >
  A user without access to a record's address can still view its derived coordinate through
  another surface.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  As a user without access to a specific record's address field, attempt to view that record's
  derived coordinate through any other available view or export.
```

## G03-BASE_GEOLOCALIZE-Q034

```yaml
QID: G03-BASE_GEOLOCALIZE-Q034
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to a record's stored location, whether automatic or manual, leaves a traceable
  record of what the prior value was and when the change occurred.
WHY_IT_MATTERS: >
  Without this trace, a wrong routing or territory decision traced back to a bad coordinate
  cannot be explained or corrected at its source.
DISCONFIRMING_OBSERVATION: >
  After a location value changes, there is no way to determine what the previous value was or
  when the change happened.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change a record's location (by either path) and then attempt to retrieve the prior value and
  the time of change.
```

## G03-BASE_GEOLOCALIZE-Q035

```yaml
QID: G03-BASE_GEOLOCALIZE-Q035
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The audit trail for a location change distinguishes a machine-derived update from a
  human-entered one.
WHY_IT_MATTERS: >
  Treating a human correction and a machine guess as indistinguishable in the trail prevents
  identifying when automation has been overriding human judgment.
DISCONFIRMING_OBSERVATION: >
  The audit trail for a location change gives no way to tell whether the new value came from
  automatic derivation or from manual entry.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Make one location change through automatic derivation and one through manual entry, then
  compare what the audit trail records for each.
```

## G03-BASE_GEOLOCALIZE-Q036

```yaml
QID: G03-BASE_GEOLOCALIZE-Q036
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The feature can be disabled for a specific tenant without affecting other tenants' use of it.
WHY_IT_MATTERS: >
  A tenant that does not want customer addresses sent externally needs a way to opt out without
  a change affecting anyone else.
DISCONFIRMING_OBSERVATION: >
  Disabling the feature for one tenant also disables or otherwise affects another tenant's
  ability to use it.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Disable the feature for one tenant while it remains enabled for another, then verify each
  tenant's behavior independently.
```
## G03-BASE_GEOLOCALIZE-Q037

```yaml
QID: G03-BASE_GEOLOCALIZE-Q037
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where more than one external provider can be configured, the choice can be set independently
  per tenant or company rather than being a single global setting.
WHY_IT_MATTERS: >
  A single global provider choice prevents a tenant from meeting its own contractual, quality,
  or residency requirements independently of other tenants.
DISCONFIRMING_OBSERVATION: >
  Changing the provider for one tenant or company changes it for others as well, with no
  independent per-tenant or per-company setting available.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Attempt to configure two tenants or companies with different providers and verify whether
  both settings hold independently.
```

## G03-BASE_GEOLOCALIZE-Q038

```yaml
QID: G03-BASE_GEOLOCALIZE-Q038
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A failed derivation attempt is surfaced to a user or a monitoring surface rather than failing
  silently with the record simply left unresolved and no trace of the attempt.
WHY_IT_MATTERS: >
  A silently swallowed failure looks identical to a record that was never expected to have a
  location, hiding a real, fixable problem.
DISCONFIRMING_OBSERVATION: >
  A derivation attempt fails and no user-visible message, log entry, or monitoring signal
  reflects that the attempt was made and failed.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Force a derivation attempt to fail (invalid address or unreachable service) and check for any
  surfaced indication of the failure.
```

## G03-BASE_GEOLOCALIZE-Q039

```yaml
QID: G03-BASE_GEOLOCALIZE-Q039
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A transient failure (timeout, temporary service error) results in a bounded, automatic retry
  rather than requiring a human to notice and manually re-trigger every affected record.
WHY_IT_MATTERS: >
  Without automatic retry, every transient blip becomes a manual cleanup task that scales with
  the size of the affected batch.
DISCONFIRMING_OBSERVATION: >
  A record that failed due to a clearly transient condition remains unresolved indefinitely
  with no automatic retry ever attempted.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Force a transient failure for one record's derivation and observe whether it is retried
  automatically within a reasonable window.
```

## G03-BASE_GEOLOCALIZE-Q040

```yaml
QID: G03-BASE_GEOLOCALIZE-Q040
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a scheduled background derivation pass fails outright (not just individual record
  failures), that failure is visible to whoever is responsible for operating the system.
WHY_IT_MATTERS: >
  A silently failing scheduled pass can leave the backlog of unresolved records growing for an
  extended period before anyone notices.
DISCONFIRMING_OBSERVATION: >
  A scheduled background pass fails to run or errors out entirely and no operator-visible
  signal reflects that failure.
EXPECTED_SURFACE: S6,S8
PRECONDITIONS: >
  Force the scheduled background pass itself to fail (not an individual record) and check for
  any operator-visible notification.
```

## G03-BASE_GEOLOCALIZE-Q041

```yaml
QID: G03-BASE_GEOLOCALIZE-Q041
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a record is visible across more than one company within the same tenant, its derived
  location is a single consistent value, not one that a user could see differently depending on
  which company context they are viewing it from.
WHY_IT_MATTERS: >
  Two different location values shown for the same physical record depending on viewing
  context would be a data-integrity contradiction inside a single tenant.
DISCONFIRMING_OBSERVATION: >
  The same shared record shows a different derived location value when viewed under one company
  context versus another within the same tenant.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  View a record shared across two companies within the same tenant from each company's context
  and compare the location value shown.
```

## G03-BASE_GEOLOCALIZE-Q042

```yaml
QID: G03-BASE_GEOLOCALIZE-Q042
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a record's location is included in a data export, whether that value was human-entered
  or machine-derived, and at what precision, is either preserved in the export or the export
  at least does not imply a precision the data does not have.
WHY_IT_MATTERS: >
  An export that presents a coarse guess with the same apparent confidence as a precise value
  can mislead whoever consumes the export downstream.
DISCONFIRMING_OBSERVATION: >
  An export of location data presents a low-precision, machine-guessed value with no
  distinguishable difference from a precise, verified one.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Export a set of records mixing precise and low-precision derived locations and inspect
  whether the export distinguishes them.
```

## G03-BASE_GEOLOCALIZE-Q043

```yaml
QID: G03-BASE_GEOLOCALIZE-Q043
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a customer's address data is deleted in response to an erasure request, its derived
  location is deleted along with it rather than surviving as an orphaned value.
WHY_IT_MATTERS: >
  A coordinate surviving an erasure request can still identify where that person lived even
  after the rest of their data was supposedly removed.
DISCONFIRMING_OBSERVATION: >
  After an address is deleted as part of an erasure request, the previously derived location
  remains retrievable.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Perform an address deletion in the context of an erasure request and check whether the
  associated derived location is also removed.
```

## G03-BASE_GEOLOCALIZE-Q044

```yaml
QID: G03-BASE_GEOLOCALIZE-Q044
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Derivation requests made from a test or sandbox environment do not consume the same quota or
  credentials as the live production environment for the same tenant.
WHY_IT_MATTERS: >
  Testing activity silently consuming production quota can exhaust the live budget without any
  production usage having occurred.
DISCONFIRMING_OBSERVATION: >
  Requests made from a test or sandbox copy of a tenant's environment are found to draw against
  the same quota counter as its production environment.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Perform derivations from a test/sandbox copy of a tenant and check whether the production
  quota counter for that tenant is affected.
```

## G03-BASE_GEOLOCALIZE-Q045

```yaml
QID: G03-BASE_GEOLOCALIZE-Q045
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change in the shape or content of the external service's response (a new optional field, a
  changed error format) does not cause the derivation to silently store an incorrect or
  malformed location without detection.
WHY_IT_MATTERS: >
  An external service can change its response format without notice; a system that trusts an
  unexpected shape can silently persist garbage as if it were valid.
DISCONFIRMING_OBSERVATION: >
  An externally supplied response shape not seen before results in a malformed or clearly
  wrong location being stored with no error or flag raised.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Return a response from the external service with an unexpected shape or an unfamiliar error
  format and observe what gets stored.
```

## G03-BASE_GEOLOCALIZE-Q046

```yaml
QID: G03-BASE_GEOLOCALIZE-Q046
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A location resolved only to a coarse, low-precision level is not used, on its own, to
  determine a jurisdiction-sensitive outcome such as a tax or legal boundary assignment.
WHY_IT_MATTERS: >
  Using a coarse guess to decide a jurisdiction-sensitive outcome can produce an incorrect tax
  or legal determination that looks confidently correct.
DISCONFIRMING_OBSERVATION: >
  A jurisdiction-sensitive determination is made using a location known to be resolved only at
  a coarse precision level, with no additional check or human confirmation involved.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Produce a low-precision derived location near a jurisdiction boundary and trigger a
  downstream process that determines a jurisdiction-sensitive outcome from it.
```

## G03-BASE_GEOLOCALIZE-Q047

```yaml
QID: G03-BASE_GEOLOCALIZE-Q047
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk data migration or import that touches unrelated fields on many records does not
  incidentally trigger mass re-derivation of locations as a side effect.
WHY_IT_MATTERS: >
  An unrelated migration silently consuming the entire external quota as a side effect is an
  unbudgeted, hard-to-diagnose cost and risk event.
DISCONFIRMING_OBSERVATION: >
  A bulk update or migration targeting fields unrelated to address causes a spike in external
  lookup calls as an unintended side effect.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Run a bulk update touching an unrelated field across many records already holding a location,
  and monitor whether unexpected external lookup activity occurs.
```

## G03-BASE_GEOLOCALIZE-Q048

```yaml
QID: G03-BASE_GEOLOCALIZE-Q048
MODULE: base_geolocalize
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A report or dashboard aggregating records by location clearly distinguishes records with no
  resolved location from those genuinely located at a default or fallback point, rather than
  folding both into the same bucket.
WHY_IT_MATTERS: >
  Silently folding "no location" together with a real default location skews any geographic
  aggregate without anyone knowing part of the data is actually missing.
DISCONFIRMING_OBSERVATION: >
  A geographic report or aggregate groups records with no resolved location together with
  records genuinely located at a shared default point, with no way to tell the two groups
  apart.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Include some records with no resolved location and some with a genuine default/fallback
  location in a geographic aggregate report and inspect whether they are distinguishable.
```
