# SMEsPlus ENTERPRISE SUITE
## GMVQ — G09 CRM / crm_iap_enrich Module Adversarial MVQ Bank

**Document ID:** GMVQ-G09-CRM_IAP_ENRICH-MVQ48-V1.00
**Group:** G09 CRM
**Module Metadata:** `crm_iap_enrich`
**Wave:** W2
**Author Cell:** P-C2 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `crm_iap_enrich`, one of the three modules in
the paid-service family named in GROUP_BRIEF_G09_CRM.md (`_iap_enrich`, `_iap_mine`, `_iap_reveal`).
Per that brief the family's anti-template control is WHAT IS BEING BOUGHT: this module buys MORE
DATA ABOUT A RECORD THE TENANT ALREADY HAS. Nothing in this bank concerns a record the tenant did
not already hold (that ground belongs to `crm_iap_mine`) or an anonymous visitor's identity (that
ground belongs to `website_crm_iap_reveal`, authored by a separate cell under this same group).
Every question was tested against that distinction: if the question would read the same for a
record that did not exist before the paid call, it does not belong here.

The bank centers on the ground unique to enrichment named in the routing brief for this task:
externally sourced values overwriting a human's entry or correction; provenance and whether a
reviewer can tell which fields came from outside and when; a similarly named but different legal
entity being silently merged in; enrichment of a record already feeding posted transactions; a
human correction being undone by the next scheduled re-enrichment pass; partial enrichment leaving
a record half from one source; spend for a record that returns nothing new; and enrichment of a
record the tenant no longer has a lawful basis to hold. It also covers the shared family ground
this module was assigned to carry — per-tenant metering isolation, what of the tenant's own data
leaves the tenant boundary to attempt a match, and the service failing mid-call — because the
routing brief places that ground with whichever sibling it bites hardest, and an UPDATE to a
record the tenant already relies on for other purposes is where a silent mid-call failure or a
metering leak does the most damage. The shared grounds of a monetary credit balance running out
mid-operation and of results being stale relative to their source are carried instead by
`crm_iap_mine`, where they bite harder against a bulk unattended acquisition; they are deliberately
not re-asked here.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: crm_iap_enrich` appears only in
the structured metadata field, never inside question text. The service the module calls is referred
to only as a metered external data service.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses about this
  module; none is a variation of another with a noun swapped.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- Sibling check performed per GMVQ_BRIDGE_MODULE_RULE_V1.00 §5: `grep -h 'HYPOTHESIS'` was run
  against `01_QUESTION_BANKS/G09_CRM/*.md` before authoring. No bank existed on disk for this group
  at authoring time (G09 CRM has no completed bank yet per GROUP_BRIEF_G09_CRM.md), so there was no
  existing HYPOTHESIS text to check against and no overlap is possible at this authoring instant.
  `crm_iap_enrich` is a family sibling of `crm_iap_mine` and `website_crm_iap_reveal`, not a bridge
  module joining two independently designed capabilities in the bridge-rule sense, but the same
  discipline was applied: the "what is being bought" test in GROUP_BRIEF_G09_CRM.md was run against
  every question below, and the shared-ground assignment above was fixed before writing so the two
  cells authoring the enrich and mine banks would not need to renegotiate it after the fact.
- Cross-check against `crm_iap_mine`'s bank (authored in the same session) confirms no two
  `DISCONFIRMING_OBSERVATION` lines across the two banks describe the same event; see the session
  report for the specific shared-ground allocation.

## G09-CRM_IAP_ENRICH-Q001

```yaml
QID: G09-CRM_IAP_ENRICH-Q001
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a value returned by the external service disagrees with a value a human previously entered
  or deliberately corrected on that same record, the human's value is not silently replaced without
  some signal that a conflict occurred.
WHY_IT_MATTERS: >
  A human correction usually exists because the recorded value was wrong for a specific, known
  reason. Silently reverting it destroys judgment the business already paid for once.
DISCONFIRMING_OBSERVATION: >
  A field a human had visibly entered or corrected is overwritten by the external service's value
  with no flag, prompt, log entry, or other trace that a conflict existed at the moment of write.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Manually set or correct a field eligible for enrichment, then run enrichment on that same record
  where the external service would return a different value for that field.
```

## G09-CRM_IAP_ENRICH-Q002

```yaml
QID: G09-CRM_IAP_ENRICH-Q002
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A reviewer looking at a record can determine which of its fields arrived from the external
  service and roughly when, rather than an externally sourced value being indistinguishable from
  one a person typed in directly.
WHY_IT_MATTERS: >
  Without that distinction, nobody can later judge how much weight to give a field, or investigate
  a bad decision that was made on the strength of a purchased value.
DISCONFIRMING_OBSERVATION: >
  A record carries a field populated by the external service and there is no way, from the record
  or its history, to tell that the value came from that source rather than from a person.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Enrich a record, then inspect the record and its available history for any indication of which
  fields changed as a result and when.
```

## G09-CRM_IAP_ENRICH-Q003

```yaml
QID: G09-CRM_IAP_ENRICH-Q003
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Provenance information about an enriched field survives a later, unrelated edit to the same
  record made by a human, rather than being wiped the next time anyone touches the record.
WHY_IT_MATTERS: >
  Provenance that disappears at the first routine edit is not a control, it is a demonstration that
  looked like one during testing and vanished in ordinary use.
DISCONFIRMING_OBSERVATION: >
  A human edits an unrelated field on an enriched record and the trace of which fields were
  externally sourced is no longer available afterward.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Enrich a record, confirm provenance is visible, make an unrelated manual edit to the same record,
  and check whether the provenance trace still resolves.
```

## G09-CRM_IAP_ENRICH-Q004

```yaml
QID: G09-CRM_IAP_ENRICH-Q004
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external service's best match is actually a different real-world entity that merely
  shares a similar name with the record being enriched, the module does not silently adopt that
  entity's attributes as if they belonged to the record.
WHY_IT_MATTERS: >
  Merging in a stranger's attributes under a similar name corrupts the record with confidence, and
  the error looks exactly like a correct enrichment until someone notices unrelated details.
DISCONFIRMING_OBSERVATION: >
  A record is enriched with attributes that, on inspection, belong to a different legal entity that
  only resembles the record by name, and nothing about the write distinguished a strong match from
  a merely plausible one.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enrich a record whose identifying details are ambiguous enough that the external service's top
  result could plausibly be a different, similarly named entity.
```

## G09-CRM_IAP_ENRICH-Q005

```yaml
QID: G09-CRM_IAP_ENRICH-Q005
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A result the external service itself flags as a weak or ambiguous match is carried into the
  record in a way that is distinguishable from a result it returned with high confidence.
WHY_IT_MATTERS: >
  Treating every returned result as equally trustworthy discards a signal the paid service already
  computed and handed over for free.
DISCONFIRMING_OBSERVATION: >
  Two enrichment calls, one where the external service reports a strong match and one where it
  reports a weak or ambiguous one, produce records that are indistinguishable from each other.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger enrichment against inputs known to produce, respectively, a high-confidence and a
  low-confidence result from the external service, and compare what lands on each record.
```

## G09-CRM_IAP_ENRICH-Q006

```yaml
QID: G09-CRM_IAP_ENRICH-Q006
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Enriching a record that already feeds a posted transaction does not alter the information behind
  that posted transaction, or does so only through a controlled, visible path rather than a plain
  overwrite.
WHY_IT_MATTERS: >
  A posted transaction's figures need to remain explainable against what was true when it was
  posted; a quiet retroactive change breaks that explainability without anyone deciding it should.
DISCONFIRMING_OBSERVATION: >
  A field on a record already referenced by a posted transaction changes value as a result of
  enrichment, with no distinct handling, warning, or record of the fact that a posted transaction
  depends on it.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a transaction that depends on a record's data, then run enrichment on that same record where
  the external service would return a different value for a field the transaction relied on.
```

## G09-CRM_IAP_ENRICH-Q007

```yaml
QID: G09-CRM_IAP_ENRICH-Q007
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A field that was enriched, then corrected by a human, is not silently put back to the external
  value the next time a scheduled enrichment pass reaches the same record.
WHY_IT_MATTERS: >
  This is the specific way a human correction gets erased without anyone touching the record: an
  unattended job undoes work a person did on purpose, and nobody is present to notice.
DISCONFIRMING_OBSERVATION: >
  After a human corrects a field the module had previously enriched, a later scheduled pass reverts
  that field back to the external value with no distinction from a field never corrected at all.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Enrich a record, manually correct the resulting field, then let or force a scheduled recurring
  enrichment pass reach that same record again.
```

## G09-CRM_IAP_ENRICH-Q008

```yaml
QID: G09-CRM_IAP_ENRICH-Q008
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A record left half enriched — some fields from the external service, others still whatever they
  were before — is representable and recognizable as such, rather than looking like a fully
  consistent, single-source record.
WHY_IT_MATTERS: >
  A record that looks uniform but is actually a patchwork invites a reader to trust the whole thing
  because part of it earned that trust.
DISCONFIRMING_OBSERVATION: >
  A record with only some of its eligible fields populated by the external service presents no way
  to tell, at the record level, that it is only partially enriched rather than fully or not at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Run enrichment in a scenario where the external service supplies some but not all of the fields
  the module is configured to populate, and inspect the resulting record.
```

## G09-CRM_IAP_ENRICH-Q009

```yaml
QID: G09-CRM_IAP_ENRICH-Q009
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Spend incurred for a call that returns nothing new for the record is distinguishable, after the
  fact, from spend that returned usable data.
WHY_IT_MATTERS: >
  Without that distinction, nobody responsible for the spend can ever tell whether the money is
  buying data or simply being charged for asking.
DISCONFIRMING_OBSERVATION: >
  A call that returns no new information for a record is recorded identically to one that returned
  usable data, with no way to separately total or review the no-result spend.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger enrichment against a record for which the external service is known to return nothing new,
  and examine whatever spend or usage record the operation leaves behind.
```

## G09-CRM_IAP_ENRICH-Q010

```yaml
QID: G09-CRM_IAP_ENRICH-Q010
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A record the tenant no longer has a lawful basis to hold is not enriched with further personal
  data as if that basis still existed; enrichment against such a record is blocked or flagged rather
  than proceeding as normal.
WHY_IT_MATTERS: >
  Buying more personal data about a record the tenant should no longer be holding compounds a
  compliance failure instead of merely leaving it unresolved.
DISCONFIRMING_OBSERVATION: >
  A record already marked, requested, or otherwise known to lack a continuing lawful basis is
  enriched with additional personal data with no block, warning, or distinct handling at all.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Mark or otherwise establish that a record no longer has a lawful basis to be held, then attempt
  or allow a scheduled pass to enrich that same record.
```

## G09-CRM_IAP_ENRICH-Q011

```yaml
QID: G09-CRM_IAP_ENRICH-Q011
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Triggering a single paid enrichment call on a record is gated by a permission distinct from the
  general permission to edit that record, rather than any editor being able to commit spend.
WHY_IT_MATTERS: >
  Editing a record and committing the business's money are different levels of authority; collapsing
  them into one permission removes a control someone assumed was in place.
DISCONFIRMING_OBSERVATION: >
  A user able to edit a record but never granted any spend-related permission is nonetheless able to
  trigger a paid enrichment call against it.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Configure a user with record-edit rights but no spend or enrichment-specific permission, and
  attempt to trigger enrichment as that user.
```

## G09-CRM_IAP_ENRICH-Q012

```yaml
QID: G09-CRM_IAP_ENRICH-Q012
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Authorizing an unattended, recurring bulk enrichment pass across many records requires a higher or
  at least distinct level of authority from authorizing one manual enrichment on one record.
WHY_IT_MATTERS: >
  A recurring bulk pass can spend far more, far faster, and with nobody watching each call; treating
  it the same as a single manual action understates the exposure it carries.
DISCONFIRMING_OBSERVATION: >
  Any user permitted to trigger a single manual enrichment is, by that same permission alone, also
  able to schedule or enable an unattended recurring bulk pass with no additional authorization step.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Compare what permission or role is required to trigger one manual enrichment against what is
  required to configure a recurring scheduled enrichment pass.
```

## G09-CRM_IAP_ENRICH-Q013

```yaml
QID: G09-CRM_IAP_ENRICH-Q013
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Usage against the metered external service is tracked and constrained per tenant, so one tenant's
  enrichment activity cannot exhaust or draw down an allowance that another tenant on the same
  platform depends on.
WHY_IT_MATTERS: >
  A shared, unmetered pool turns one tenant's heavy or runaway use into another tenant's outage or
  unexplained bill, on a platform whose whole premise is tenant isolation.
DISCONFIRMING_OBSERVATION: >
  Enrichment activity attributable to one tenant measurably reduces the usage allowance or increases
  the cost recorded against a different, unrelated tenant.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Run a substantial volume of enrichment calls under one tenant and check whether any other
  tenant's own usage counters or available allowance are affected.
```

## G09-CRM_IAP_ENRICH-Q014

```yaml
QID: G09-CRM_IAP_ENRICH-Q014
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Only the subset of the record's own data actually needed to attempt a match is sent to the
  external service, rather than the whole record being disclosed for the sake of convenience.
WHY_IT_MATTERS: >
  Every field sent outward to a third party for the sake of a lookup is a field the tenant no longer
  fully controls the disclosure of, whether or not it was needed for the match.
DISCONFIRMING_OBSERVATION: >
  Fields on the record that play no role in identifying it for a match are nonetheless included in
  what is sent to the external service when enrichment is triggered.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Trigger enrichment on a record carrying fields unrelated to identification, and determine what
  subset of the record's data is actually transmitted outward for the lookup.
```

## G09-CRM_IAP_ENRICH-Q015

```yaml
QID: G09-CRM_IAP_ENRICH-Q015
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the external service errors or is unreachable mid-call, the record is left exactly as it was
  before the call, rather than in some partially updated state.
WHY_IT_MATTERS: >
  A record stuck half-written after a failed call is worse than one untouched: it looks enriched
  without actually being complete or correct.
DISCONFIRMING_OBSERVATION: >
  After the external service errors or times out mid-call, the record shows a partial update — some
  but not all of the intended fields changed, or a field changed to an incomplete value.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger enrichment under a condition where the external service can be made to fail or time out
  partway through responding, and inspect the record afterward.
```

## G09-CRM_IAP_ENRICH-Q016

```yaml
QID: G09-CRM_IAP_ENRICH-Q016
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Retrying a record after a failed enrichment attempt does not incur a second charge for an attempt
  that produced no result the first time.
WHY_IT_MATTERS: >
  Charging twice for one useful result, just because the first attempt happened to fail before
  delivering it, is a cost nobody agreed to and nobody can see without checking closely.
DISCONFIRMING_OBSERVATION: >
  A record that failed to enrich once and is retried is charged again for the retry even though the
  first attempt produced no usable result.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Cause an enrichment attempt to fail after being charged, if that is how the service bills, then
  retry the same record and compare spend recorded across both attempts.
```

## G09-CRM_IAP_ENRICH-Q017

```yaml
QID: G09-CRM_IAP_ENRICH-Q017
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a human is actively editing a record at the moment a scheduled enrichment pass reaches it,
  the two writes are resolved in some deliberate way rather than one silently clobbering the other
  with no indication either happened.
WHY_IT_MATTERS: >
  A person mid-edit has no reason to expect a background process is about to write to the same
  record, and losing their in-progress work without any sign of what happened erodes trust in the
  record entirely.
DISCONFIRMING_OBSERVATION: >
  A human's in-progress edit to a record is lost or silently overwritten by a concurrently running
  enrichment pass, with nothing to show either the human or a later reviewer that a collision
  occurred.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Begin editing a record and, before saving, trigger or allow a scheduled enrichment pass to reach
  the same record, then observe what each side ends up seeing.
```

## G09-CRM_IAP_ENRICH-Q018

```yaml
QID: G09-CRM_IAP_ENRICH-Q018
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two enrichment requests fired for the same record at nearly the same time do not both proceed to a
  full paid call and a full write, doubling the spend and risking two different results landing in
  either order.
WHY_IT_MATTERS: >
  Nothing about a normal workflow prevents two people, or a person and a scheduled pass, from acting
  on the same record close together; if both proceed independently the business pays twice for one
  answer and the final state depends on whichever response happened to arrive last.
DISCONFIRMING_OBSERVATION: >
  Firing two enrichment requests for the same record within a short window results in two full paid
  calls and two full writes, rather than the second being recognized as redundant or queued.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger enrichment for the same record twice in close succession, whether by two users or one user
  acting twice, and observe how many calls and writes actually occur.
```

## G09-CRM_IAP_ENRICH-Q019

```yaml
QID: G09-CRM_IAP_ENRICH-Q019
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A field that is currently driving an in-flight approval or assignment decision is not silently
  changed by enrichment while that decision is still pending on its prior value.
WHY_IT_MATTERS: >
  A decision made on one value that quietly becomes a different value before it is finalized is a
  decision made on data that no longer exists, and nobody involved would know to re-check it.
DISCONFIRMING_OBSERVATION: >
  A field feeding a pending approval or assignment decision changes as a result of enrichment while
  that decision is still open, with no notice to whoever is holding the decision.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Put a record into a state where a field is driving an open approval or assignment decision, then
  run enrichment against that record before the decision is finalized.
```

## G09-CRM_IAP_ENRICH-Q020

```yaml
QID: G09-CRM_IAP_ENRICH-Q020
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whether enrichment is enabled, and what it is configured to do, is scoped per company in a
  multi-company setup, rather than one company's configuration silently governing a record a
  different company also has access to.
WHY_IT_MATTERS: >
  Configuration that leaks across a company boundary means one company's decision about what to buy
  and reveal is effectively made for a company that never agreed to it.
DISCONFIRMING_OBSERVATION: >
  A record visible to two companies is enriched, or enriched differently, depending on a
  configuration that was set in only one of those companies and never confirmed in the other.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  In a multi-company setup, configure enrichment differently between two companies and observe its
  effect on a record shared or visible across both.
```

## G09-CRM_IAP_ENRICH-Q021

```yaml
QID: G09-CRM_IAP_ENRICH-Q021
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Triggering enrichment on a record that carries no information sufficient to attempt any match does
  not consume spend for a call the module could have recognized in advance was pointless.
WHY_IT_MATTERS: >
  Charging for a lookup that had no chance of succeeding is an avoidable cost that a basic
  precondition check would have prevented.
DISCONFIRMING_OBSERVATION: >
  A record with no usable identifying information is submitted for enrichment and a charge is
  recorded even though no meaningful lookup could have been attempted.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger enrichment on a record deliberately left without the minimum identifying detail a lookup
  would need, and check whether spend is recorded regardless.
```

## G09-CRM_IAP_ENRICH-Q022

```yaml
QID: G09-CRM_IAP_ENRICH-Q022
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling an in-flight background enrichment job actually prevents the remaining paid calls in
  that job from being made, rather than only hiding or discarding results that arrive afterward.
WHY_IT_MATTERS: >
  A cancel button that stops the display but not the spend gives whoever clicked it a false sense
  that they controlled the cost, when in fact the money kept moving.
DISCONFIRMING_OBSERVATION: >
  After a background enrichment job is cancelled, calls attributable to that job continue to be made
  and charged for records the job had not yet reached.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Start a background enrichment job against several records, cancel it partway through, and check
  whether further calls and charges continue for the records not yet processed.
```

## G09-CRM_IAP_ENRICH-Q023

```yaml
QID: G09-CRM_IAP_ENRICH-Q023
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a record in a closed or otherwise final stage remains eligible for enrichment is a
  deliberate, configured answer, not an accident of the eligibility check never having considered
  stage at all.
WHY_IT_MATTERS: >
  Spending to enrich a record nobody will act on again, or conversely silently refusing to enrich a
  record someone reopened, should be a choice the business made rather than a side effect.
DISCONFIRMING_OBSERVATION: >
  Records in a closed or final stage are included or excluded from enrichment with no configuration
  setting, design record, or documented default governing that outcome.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Move a record to a closed or final stage and attempt or allow enrichment against it, then look for
  any configuration that was meant to govern this case.
```

## G09-CRM_IAP_ENRICH-Q024

```yaml
QID: G09-CRM_IAP_ENRICH-Q024
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Undoing an enrichment restores the field's prior value and records that a restoration happened,
  rather than leaving the field simply blank or leaving no trace that an undo occurred at all.
WHY_IT_MATTERS: >
  An undo that cannot be told apart from an ordinary edit, or that loses the prior value entirely,
  gives false confidence that the record can be put back the way it was.
DISCONFIRMING_OBSERVATION: >
  Reversing an enrichment leaves the field empty, incorrect, or indistinguishable from a normal
  manual edit, with no trace that a restoration to a prior state was what actually happened.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Enrich a record, then use whatever mechanism exists to undo or reverse that enrichment, and
  inspect both the resulting field value and the record's history.
```

## G09-CRM_IAP_ENRICH-Q025

```yaml
QID: G09-CRM_IAP_ENRICH-Q025
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a separate automated rule also targets a field that enrichment can populate, there is a
  consistent, decidable order between the two rather than whichever ran most recently winning by
  accident.
WHY_IT_MATTERS: >
  Two mechanisms racing for the same field with no defined precedence produces a value nobody can
  predict or explain after the fact.
DISCONFIRMING_OBSERVATION: >
  The same field ends up with different final values across otherwise identical runs, depending only
  on which of the two mechanisms happened to execute last.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure an automated rule that targets the same field enrichment can populate, then trigger both
  in close succession and repeat to check for a consistent outcome.
```

## G09-CRM_IAP_ENRICH-Q026

```yaml
QID: G09-CRM_IAP_ENRICH-Q026
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Who triggered or authorized a paid enrichment call, and when, is recorded separately from the
  ordinary field-change history, rather than the spend event being inferable only by reasoning
  backward from which fields changed.
WHY_IT_MATTERS: >
  Reviewing spend requires knowing who spent it and when they chose to, not just what values changed
  as a side effect.
DISCONFIRMING_OBSERVATION: >
  There is no record identifying who triggered or authorized a specific paid enrichment call or
  when, separate from and in addition to the resulting field changes.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger an enrichment call as an identified user and look for a record of that authorization
  distinct from the field-level change history it produced.
```

## G09-CRM_IAP_ENRICH-Q027

```yaml
QID: G09-CRM_IAP_ENRICH-Q027
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When two records are merged by the base pipeline's own duplicate-handling, the provenance
  information about which fields were externally enriched on either side survives the merge onto
  the surviving record.
WHY_IT_MATTERS: >
  A merge is exactly the moment provenance is most needed, because the surviving record now mixes
  the history of two records that may have been enriched differently or not at all.
DISCONFIRMING_OBSERVATION: >
  After two records are merged, the surviving record cannot show which of its fields were
  externally enriched on either original record before the merge occurred.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Enrich one of two records that are later identified as duplicates, merge them through the base
  pipeline's own mechanism, and inspect the surviving record's provenance.
```

## G09-CRM_IAP_ENRICH-Q028

```yaml
QID: G09-CRM_IAP_ENRICH-Q028
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A record reached by more than one enrichment route in the same run — for example matched
  individually and also swept up by a broader scheduled pass — is not enriched, and charged, twice
  within that same run.
WHY_IT_MATTERS: >
  Two routes into the same operation is an ordinary configuration accident, and paying twice for one
  record in one run is the direct, avoidable cost of not checking for it.
DISCONFIRMING_OBSERVATION: >
  A single run in which one record is reachable by two configured routes results in two separate
  paid calls and two charges against that record within that same run.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Configure a scheduled pass and an individual trigger such that both would reach the same record in
  the same run window, and observe how many times that record is actually processed.
```

## G09-CRM_IAP_ENRICH-Q029

```yaml
QID: G09-CRM_IAP_ENRICH-Q029
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When the external service returns a value outside the set of options the tenant has configured as
  valid for that field, the value is held for review or rejected rather than force-fit into the
  nearest option or written as free text that breaks the configured constraint.
WHY_IT_MATTERS: >
  A tenant configures a fixed set of valid options because downstream processes rely on it; an
  external value that bypasses that constraint can silently break those processes.
DISCONFIRMING_OBSERVATION: >
  A value returned by the external service that does not match any of the tenant's configured valid
  options is written to the field anyway, without review or rejection.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a constrained field with a fixed set of valid options, then enrich a record where the
  external service is known to return a value outside that set.
```

## G09-CRM_IAP_ENRICH-Q030

```yaml
QID: G09-CRM_IAP_ENRICH-Q030
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a field carries a currency or unit and the external service's value is expressed in a
  different one, the module converts or flags the mismatch rather than writing the external number
  under the record's existing unit without adjustment.
WHY_IT_MATTERS: >
  A number silently written under the wrong unit or currency looks exactly as precise and
  trustworthy as a correct one, and can be materially wrong in either direction.
DISCONFIRMING_OBSERVATION: >
  A record's currency- or unit-bearing field is written from the external service's value with no
  conversion or flag, even though the external value's unit or currency differs from the record's.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Enrich a record whose currency- or unit-bearing field would be populated from an external value
  expressed in a different unit or currency, and inspect the result.
```

## G09-CRM_IAP_ENRICH-Q031

```yaml
QID: G09-CRM_IAP_ENRICH-Q031
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The frequency at which a scheduled re-enrichment pass revisits the same records is itself
  configurable, so a tenant is not forced to either accept unnecessary repeat spend on records that
  cannot have changed or forgo re-enrichment altogether.
WHY_IT_MATTERS: >
  A fixed, non-configurable re-enrichment cadence either wastes money re-buying data that has not
  changed or leaves genuinely stale data uncorrected for too long, with the tenant unable to choose.
DISCONFIRMING_OBSERVATION: >
  The interval between successive scheduled enrichment passes over the same record cannot be
  configured, adjusted, or disabled by the tenant at all.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Locate the configuration governing how often a scheduled enrichment pass revisits already-enriched
  records and attempt to change it.
```

## G09-CRM_IAP_ENRICH-Q032

```yaml
QID: G09-CRM_IAP_ENRICH-Q032
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The enrichment feature is unreachable to any user until an explicit tenant-level configuration
  step enables it, rather than being available by default once the module happens to be present.
WHY_IT_MATTERS: >
  A feature that spends real money on an external service should require a deliberate decision to
  turn it on, not merely be present and waiting to be clicked.
DISCONFIRMING_OBSERVATION: >
  Enrichment can be triggered and produces a paid call before any tenant-level configuration step
  has been completed to enable it.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  On a tenant where the enrichment configuration has not been explicitly set up, attempt to trigger
  enrichment and observe whether it is reachable at all.
```

## G09-CRM_IAP_ENRICH-Q033

```yaml
QID: G09-CRM_IAP_ENRICH-Q033
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A scheduled enrichment pass excludes archived or otherwise inactive records from its sweep, rather
  than spending to enrich records nobody is going to act on again.
WHY_IT_MATTERS: >
  Archived records are, by definition, not part of active work; paying to keep their data current is
  a cost with no corresponding business benefit.
DISCONFIRMING_OBSERVATION: >
  A scheduled enrichment pass processes and charges for archived or inactive records alongside active
  ones, with no distinction in eligibility.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Archive a record eligible for enrichment and allow a scheduled pass to run, then check whether that
  record was included and charged for.
```

## G09-CRM_IAP_ENRICH-Q034

```yaml
QID: G09-CRM_IAP_ENRICH-Q034
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A value returned by the external service that would violate a validation or business rule already
  in force elsewhere in the system is rejected or held rather than written in a way that quietly
  breaks that rule.
WHY_IT_MATTERS: >
  A rule enforced everywhere except against externally sourced writes is not really a rule; it is a
  rule with an unmonitored side door.
DISCONFIRMING_OBSERVATION: >
  An externally sourced value is written to a record even though it violates a validation or business
  rule that would have blocked the same value if a human had typed it in directly.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Identify a field governed by an existing validation rule, and enrich a record where the external
  service would return a value that breaks that rule.
```

## G09-CRM_IAP_ENRICH-Q035

```yaml
QID: G09-CRM_IAP_ENRICH-Q035
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Visibility of enrichment spend and usage data is restricted to the same class of user who can see
  other financial or cost information, rather than being visible to anyone who can see the enriched
  record itself.
WHY_IT_MATTERS: >
  Spend data is financial data; exposing it to every user who happens to view a record leaks
  information beyond who was meant to see it.
DISCONFIRMING_OBSERVATION: >
  A user with no access to financial or cost information elsewhere in the system can nonetheless see
  what was spent enriching a specific record.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  As a user without financial visibility elsewhere, view a record that has been enriched and attempt
  to find any spend or usage figures attached to it.
```

## G09-CRM_IAP_ENRICH-Q036

```yaml
QID: G09-CRM_IAP_ENRICH-Q036
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the same real-world customer is represented separately in two different companies on the
  platform, enriching that customer's record in one company does not write or expose data into the
  other company's copy.
WHY_IT_MATTERS: >
  Company separation exists so each company's data and decisions stay its own; a paid lookup that
  quietly crosses that boundary defeats the separation for exactly the data a tenant is paying to
  keep controlled.
DISCONFIRMING_OBSERVATION: >
  Enriching a customer's record in one company results in a visible change to, or disclosure of data
  from, that same customer's separate record in a different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  In a multi-company setup, create separate records for the same real-world customer in two
  companies, enrich one, and check the other for any effect.
```

## G09-CRM_IAP_ENRICH-Q037

```yaml
QID: G09-CRM_IAP_ENRICH-Q037
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A match whose confidence falls below whatever threshold the tenant or the module treats as
  acceptable is held for review rather than being written to the record exactly as a high-confidence
  match would be.
WHY_IT_MATTERS: >
  Auto-accepting weak matches at the same rate as strong ones defeats the purpose of the confidence
  signal the service provides.
DISCONFIRMING_OBSERVATION: >
  A match below the acceptance threshold is written directly to the record with the same immediacy
  and lack of review as a match that clears the threshold comfortably.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger enrichment against an input known to return a below-threshold confidence match and observe
  whether it is written directly or held for review.
```

## G09-CRM_IAP_ENRICH-Q038

```yaml
QID: G09-CRM_IAP_ENRICH-Q038
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  One record's failure partway through a batch enrichment pass does not halt or block processing of
  the remaining records in that same batch.
WHY_IT_MATTERS: >
  A single bad record stopping an entire batch turns one data quality problem into a delay affecting
  every other record that had nothing wrong with it.
DISCONFIRMING_OBSERVATION: >
  A batch enrichment pass stops processing remaining records after one record in the batch fails,
  rather than continuing past it and reporting the failure separately.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Run a batch enrichment pass over several records where one is known to cause a failure partway
  through, and observe whether the rest are still processed.
```

## G09-CRM_IAP_ENRICH-Q039

```yaml
QID: G09-CRM_IAP_ENRICH-Q039
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a field can be populated either by enrichment or by a separate computed default already in
  the system, there is a defined precedence between the two rather than whichever mechanism last
  touched the field being the accidental winner.
WHY_IT_MATTERS: >
  Two independently designed mechanisms writing to one field with no defined precedence is exactly
  the situation that produces a value nobody chose and nobody can explain.
DISCONFIRMING_OBSERVATION: >
  The field's final value differs across otherwise identical scenarios depending only on whether
  enrichment or the computed default happened to run first.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Identify a field with both an existing computed default and enrichment eligibility, and trigger
  both in different orders to check for a consistent, defined outcome.
```

## G09-CRM_IAP_ENRICH-Q040

```yaml
QID: G09-CRM_IAP_ENRICH-Q040
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The history of past enrichment activity on a record remains available for as long as the record
  itself exists, rather than being purged or aged out after some interval while the record continues
  to be used.
WHY_IT_MATTERS: >
  A record that outlives the evidence of where its own data came from cannot be properly audited
  years into its life, exactly when a dispute is most likely to ask that question.
DISCONFIRMING_OBSERVATION: >
  A record still in active use no longer shows any trace of enrichment activity that is known to have
  occurred on it, because that history was aged out or purged while the record was not.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Enrich a record, allow substantial time to pass or force whatever retention mechanism exists, and
  check whether the enrichment history is still available.
```

## G09-CRM_IAP_ENRICH-Q041

```yaml
QID: G09-CRM_IAP_ENRICH-Q041
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user who is not permitted to view or edit a given field directly cannot achieve the same result
  indirectly by triggering an enrichment call that writes to that field.
WHY_IT_MATTERS: >
  A field-level permission that can be routed around through a different action is not actually
  enforced; it only looks enforced from the one path someone tested.
DISCONFIRMING_OBSERVATION: >
  A user with no view or edit access to a specific field is still able to trigger an enrichment call
  that changes that field's value.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Configure a user with no access to a specific field but with permission to trigger enrichment, then
  have that user trigger enrichment against a record carrying that field.
```

## G09-CRM_IAP_ENRICH-Q042

```yaml
QID: G09-CRM_IAP_ENRICH-Q042
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Provenance recorded while a record was on one side of the lead-to-opportunity boundary survives
  that record's conversion to the other side, rather than being lost at the moment of conversion.
WHY_IT_MATTERS: >
  Conversion is a natural point for auxiliary data to be dropped by an implementation that only
  thought about the fields the conversion itself cares about; provenance is exactly the kind of
  auxiliary data that goes missing this way.
DISCONFIRMING_OBSERVATION: >
  A record enriched before conversion shows no trace of that enrichment's provenance once it has been
  converted across the lead-to-opportunity boundary.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Enrich a record on one side of the lead-to-opportunity boundary, convert it, and check whether the
  provenance trace is still present afterward.
```

## G09-CRM_IAP_ENRICH-Q043

```yaml
QID: G09-CRM_IAP_ENRICH-Q043
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Disabling the enrichment feature after it has been used leaves previously enriched fields and their
  provenance untouched, rather than the act of disabling the feature retroactively affecting data it
  already wrote.
WHY_IT_MATTERS: >
  Turning a feature off is a forward-looking decision; a tenant would not expect it to silently alter
  or erase data the feature already produced while it was on.
DISCONFIRMING_OBSERVATION: >
  Disabling the enrichment feature changes, hides, or removes previously enriched field values or
  their provenance on records that were enriched while the feature was active.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enrich a record, disable the enrichment feature at the tenant level, and inspect that same record
  afterward.
```

## G09-CRM_IAP_ENRICH-Q044

```yaml
QID: G09-CRM_IAP_ENRICH-Q044
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A call that comes back with no match found is recorded as distinct from a record that has simply
  never been submitted for enrichment, so the two are not confused with each other later.
WHY_IT_MATTERS: >
  Confusing "tried and found nothing" with "never tried" either wastes spend endlessly retrying a
  record that will never match, or wrongly treats an untried record as already checked.
DISCONFIRMING_OBSERVATION: >
  A record that received a definitive no-match response is indistinguishable, from its own state,
  from a record that has never been submitted for enrichment at all.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Trigger enrichment against a record known to produce a no-match response, then compare its
  resulting state against a record that was never submitted.
```

## G09-CRM_IAP_ENRICH-Q045

```yaml
QID: G09-CRM_IAP_ENRICH-Q045
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Enrichment of a field carrying legally or regulatory sensitive personal data is logged with the
  same or greater rigor as an ordinary manual edit to that same field, not with less.
WHY_IT_MATTERS: >
  A sensitive field written by an automated, paid, external process is at least as much a compliance
  event as a human typing the same value, and under-logging it creates a blind spot exactly where
  scrutiny is most likely to be needed.
DISCONFIRMING_OBSERVATION: >
  A sensitive field changed by enrichment produces a thinner or less detailed log entry than the same
  field would produce if a human edited it manually.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Compare the log entry produced by enriching a sensitive field against the log entry produced by a
  human manually editing that same field.
```

## G09-CRM_IAP_ENRICH-Q046

```yaml
QID: G09-CRM_IAP_ENRICH-Q046
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the enrichment configuration changes between two scheduled passes, a record reached by both
  passes ends up reflecting a single, identifiable configuration version rather than an unlabeled mix
  of behaviour from each.
WHY_IT_MATTERS: >
  A record whose enrichment behaviour is a blend of two different configurations, with no record of
  which parts came from which, cannot be explained to anyone asking why it looks the way it does.
DISCONFIRMING_OBSERVATION: >
  A record processed by scheduled passes under two different enrichment configurations shows a result
  that mixes behaviour from both with no way to attribute which part came from which configuration.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Change the enrichment configuration between two scheduled passes that both reach the same record,
  and inspect the resulting record for attribution to a specific configuration version.
```

## G09-CRM_IAP_ENRICH-Q047

```yaml
QID: G09-CRM_IAP_ENRICH-Q047
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A record that configuration marks as eligible for enrichment is actually reached by the running
  scheduled pass, rather than eligibility on paper and reachability at runtime being able to silently
  diverge.
WHY_IT_MATTERS: >
  A tenant relying on the configured eligibility rule to know what will be kept current has no way to
  notice that some eligible records are never actually being processed.
DISCONFIRMING_OBSERVATION: >
  A record that configuration marks as eligible for enrichment is never actually processed by the
  scheduled pass across multiple pass cycles, with nothing surfacing the gap.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Configure a record as eligible for enrichment, run the scheduled pass across several cycles, and
  confirm whether that record is ever actually processed.
```

## G09-CRM_IAP_ENRICH-Q048

```yaml
QID: G09-CRM_IAP_ENRICH-Q048
MODULE: crm_iap_enrich
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the module's design states that a given field is populated as part of enrichment, that
  mapping is actually observable happening at runtime, rather than the design describing a mapping
  that the running system does not actually perform.
WHY_IT_MATTERS: >
  A source description that outruns what the running system actually does is worse than no
  documentation at all, because it tells a reader to expect something they will not get.
DISCONFIRMING_OBSERVATION: >
  A field the design states should be populated by enrichment is never observed changing as a result
  of any enrichment call, across repeated attempts against inputs that should produce a value for it.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify a field the design documentation states is populated by enrichment, and attempt to
  observe it actually being populated across repeated enrichment calls.
```
