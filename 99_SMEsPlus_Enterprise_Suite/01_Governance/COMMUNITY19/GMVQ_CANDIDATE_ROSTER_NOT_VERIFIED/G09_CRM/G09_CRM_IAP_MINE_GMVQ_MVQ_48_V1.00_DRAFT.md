# SMEsPlus ENTERPRISE SUITE
## GMVQ — G09 CRM / crm_iap_mine Module Adversarial MVQ Bank

**Document ID:** GMVQ-G09-CRM_IAP_MINE-MVQ48-V1.00
**Group:** G09 CRM
**Module Metadata:** `crm_iap_mine`
**Wave:** W2
**Author Cell:** P-C2 (GMVQ Question Factory — Wave W2 Acceleration)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard bank reference:** 55 (shared, not reproduced here)
**Research depth:** 55 + 48 = 103
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank authors the module-specific MVQ set for `crm_iap_mine`, one of the three modules in the
paid-service family named in GROUP_BRIEF_G09_CRM.md (`_iap_enrich`, `_iap_mine`, `_iap_reveal`). Per
that brief the family's anti-template control is WHAT IS BEING BOUGHT: this module buys RECORDS THE
TENANT DID NOT ALREADY HAVE. Nothing in this bank concerns improving a record the tenant already
held (that ground belongs to `crm_iap_enrich`) or identifying an anonymous visitor who never
identified themselves (that ground belongs to `website_crm_iap_reveal`, authored by a separate cell
under this same group). Every question was tested against that distinction: if the question would
read the same for an existing record the tenant was merely updating, it does not belong here.

The bank centers on the ground unique to mining named in the routing brief for this task: acquired
records duplicating customers already held or duplicating each other within or across batches; a
purchased filter whose actual application cannot be independently verified; spend committed before
any quality signal exists; acquired records inflating a pipeline forecast with contacts nobody has
spoken to; the lawful basis for holding a person who never contacted the business and what must be
recorded at the moment of acquisition; suppression lists and previously erased records being
re-acquired; a batch delivered partially or twice; attribution of a record back to its originating
batch months later; a per-call quota exhausted mid-batch; and an acquired record's accuracy never
being verified or marked as such. It also carries the shared family ground this module was assigned
to carry — a monetary credit balance running out mid-operation, and delivered results being stale
relative to when the source data was actually current — because the routing brief places that ground
with whichever sibling it bites hardest, and an unattended bulk acquisition of records nobody has
seen yet is where a mid-operation credit failure or an unnoticed staleness does the most damage. The
shared grounds of per-tenant metering isolation, what of the tenant's own data leaves the tenant
boundary, and the service failing mid-call are carried instead by `crm_iap_enrich`, where they bite
harder against an update to a record the tenant already relies on; they are deliberately not
re-asked here.

The question text is source-neutral and does not expose vendor model names, field names, methods,
schema, XML IDs, API shapes, or implementation algorithms. `MODULE: crm_iap_mine` appears only in
the structured metadata field, never inside question text. The service the module calls is referred
to only as a metered external data service, and the records it delivers are referred to only as
acquired records.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that states a concrete failure state.
- No padding: 48 questions exist because they test 48 distinct material hypotheses about this
  module; none is a variation of another with a noun swapped.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence.
- `module + QID` is a Research Evidence Join Key only; no Formal Coverage is derived from this bank.
- This bank is PREPARED ONLY. It is not approved, not frozen, not verified, not MASTER-ready.
- Sibling check performed per GMVQ_BRIDGE_MODULE_RULE_V1.00 §5: `grep -h 'HYPOTHESIS'` was run
  against `01_QUESTION_BANKS/G09_CRM/*.md` before authoring this bank. Only this cell's own
  `crm_iap_enrich` bank existed on disk at that point (authored earlier in this same session); its
  48 HYPOTHESIS lines were read in full. No overlap exists: the enrich bank concerns updates to
  records already held, and every hypothesis below concerns records the tenant did not already hold.
  `website_crm_iap_reveal` had no bank on disk at authoring time.
- `crm_iap_mine` is a family sibling, not a bridge module joining two independently designed
  capabilities in the bridge-rule sense, but the same discipline was applied: the "what is being
  bought" test in GROUP_BRIEF_G09_CRM.md was run against every question below, and the shared-ground
  allocation was fixed before either bank in this cell was written (see this bank's Purpose and the
  `crm_iap_enrich` bank's Purpose for the matching allocation).
- Cross-check against the `crm_iap_enrich` bank authored in the same session confirms no two
  `DISCONFIRMING_OBSERVATION` lines across the two banks describe the same event; see the session
  report for the specific shared-ground allocation.

## G09-CRM_IAP_MINE-Q001

```yaml
QID: G09-CRM_IAP_MINE-Q001
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An acquired record that in fact represents a customer the tenant already holds is detected or
  flagged as a likely duplicate rather than being loaded into the pipeline as if it were a new
  relationship.
WHY_IT_MATTERS: >
  Paying to reacquire a customer the business already knows, and then treating that purchase as a
  new lead, wastes money and pollutes the pipeline with a relationship that already has history
  elsewhere.
DISCONFIRMING_OBSERVATION: >
  An acquired record matching an existing customer by the tenant's own ordinary matching signals is
  loaded as a distinct new record with no duplicate flag or link to the existing one.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Acquire a record whose identifying details match an existing customer already held by the tenant,
  and observe how it is loaded.
```

## G09-CRM_IAP_MINE-Q002

```yaml
QID: G09-CRM_IAP_MINE-Q002
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Records within the same purchased batch that duplicate each other are deduplicated, or at least
  flagged against each other, rather than each being loaded as if it were a separate relationship.
WHY_IT_MATTERS: >
  A single purchase that quietly contains the same person or company more than once inflates the
  apparent size of what was bought and the apparent size of the resulting pipeline.
DISCONFIRMING_OBSERVATION: >
  Two records within one purchased batch that clearly represent the same person or company are both
  loaded as separate, unlinked records.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Acquire a batch known to contain two records representing the same underlying person or company,
  and observe how both are loaded.
```

## G09-CRM_IAP_MINE-Q003

```yaml
QID: G09-CRM_IAP_MINE-Q003
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A record duplicating one acquired in an earlier, separate purchase is detected against that prior
  acquisition, not only against records already in day-to-day use.
WHY_IT_MATTERS: >
  Checking only against actively used records misses the very common case of buying overlapping
  populations across two purchases made months apart, which is exactly where repeat spend on the same
  people goes unnoticed.
DISCONFIRMING_OBSERVATION: >
  A record acquired in a new purchase duplicates a record acquired in an earlier purchase, and no
  duplicate detection catches the overlap between the two purchases.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Make two separate acquisitions whose populations are known to overlap, and check whether the
  overlap is detected across the two purchases.
```

## G09-CRM_IAP_MINE-Q004

```yaml
QID: G09-CRM_IAP_MINE-Q004
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  What was actually delivered can be checked against the filter criteria that were paid for, rather
  than the tenant having to simply trust that the criteria were applied as stated.
WHY_IT_MATTERS: >
  The filter criteria are themselves the product being purchased; if there is no way to verify they
  were honored, the tenant has no way to know what it actually paid for.
DISCONFIRMING_OBSERVATION: >
  There is no way, after an acquisition, to check the delivered records against the filter criteria
  that defined the purchase.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Make an acquisition against a specific, checkable filter criterion and attempt to verify after
  delivery that every delivered record actually satisfies it.
```

## G09-CRM_IAP_MINE-Q005

```yaml
QID: G09-CRM_IAP_MINE-Q005
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A delivered record that plainly does not satisfy the purchased filter criteria is flaggable or
  visibly distinguishable, rather than being indistinguishable from a record that does satisfy it.
WHY_IT_MATTERS: >
  Without a way to flag an out-of-criteria record, a systematic filtering failure on the vendor's
  side would never surface, however often it happened.
DISCONFIRMING_OBSERVATION: >
  A delivered record that clearly fails the purchased filter criteria is loaded and presented no
  differently from a record that clearly satisfies it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Arrange or identify a delivered record that fails the stated filter criteria, and check whether
  anything distinguishes it once loaded.
```

## G09-CRM_IAP_MINE-Q006

```yaml
QID: G09-CRM_IAP_MINE-Q006
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Spend for an acquisition is committed only once there is at least some basis for expecting the
  delivered records to be usable, rather than being charged purely on the size of the request before
  any quality signal exists.
WHY_IT_MATTERS: >
  Charging strictly per record requested, with no relationship to what is eventually usable, removes
  any incentive on the paying side to notice or push back on poor quality.
DISCONFIRMING_OBSERVATION: >
  The full charge for a requested acquisition is committed at the moment of request, with no
  adjustment or held-back portion tied to the quality of what is actually delivered.
EXPECTED_SURFACE: S2,S3
PRECONDITIONS: >
  Make an acquisition request and observe at what point spend is committed relative to when delivered
  quality becomes known.
```

## G09-CRM_IAP_MINE-Q007

```yaml
QID: G09-CRM_IAP_MINE-Q007
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A delivered record later found to be unusable can be marked as such in a way that is retrievable
  later, rather than the poor outcome simply disappearing once the record is dismissed or deleted.
WHY_IT_MATTERS: >
  Without any lasting record of which purchases turned out badly, there is nothing to point to when
  deciding whether to keep buying from the same source on the same terms.
DISCONFIRMING_OBSERVATION: >
  A delivered record identified as unusable, once dismissed, leaves no lasting indication anywhere
  that this particular acquisition produced a poor outcome.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Identify a delivered record as unusable, dismiss or remove it from active use, and check whether
  any lasting record of that outcome remains.
```

## G09-CRM_IAP_MINE-Q008

```yaml
QID: G09-CRM_IAP_MINE-Q008
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Records that entered the pipeline through acquisition are distinguishable from ones that entered
  organically, so a forecast or pipeline total does not silently blend contacts nobody has spoken to
  with relationships the business actually has.
WHY_IT_MATTERS: >
  A forecast that management reads as fact should not be inflated by purchased contacts who have had
  no interaction with the business, without that difference even being visible.
DISCONFIRMING_OBSERVATION: >
  A record loaded through acquisition is indistinguishable, in the ordinary pipeline and forecast
  views, from a record that arose from an actual interaction with the business.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Load an acquired record into the pipeline and compare its representation in ordinary forecast or
  pipeline views against a record that arose from a real interaction.
```

## G09-CRM_IAP_MINE-Q009

```yaml
QID: G09-CRM_IAP_MINE-Q009
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A forecast or pipeline metric can be filtered or configured to exclude acquired records that have
  never actually been contacted, rather than there being no way to see the pipeline with that
  population removed.
WHY_IT_MATTERS: >
  Even if acquired and organic records are distinguishable, a metric that cannot be filtered to
  exclude uncontacted acquired records still gets read at face value by whoever has no reason to dig
  further.
DISCONFIRMING_OBSERVATION: >
  There is no available filter or configuration that produces a pipeline or forecast view excluding
  acquired records that have never been contacted.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  With a mix of acquired-but-uncontacted and organic records in the pipeline, attempt to produce a
  forecast view that excludes the uncontacted acquired ones.
```

## G09-CRM_IAP_MINE-Q010

```yaml
QID: G09-CRM_IAP_MINE-Q010
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  At the moment a record is acquired for a person who has never contacted the business, whatever
  establishes the lawful basis for holding that person's data is captured and attached to the record,
  not left to be reconstructed later if ever questioned.
WHY_IT_MATTERS: >
  A basis reconstructed after the fact, under pressure from a complaint or a request, is far weaker
  than one recorded as a matter of course at the moment the data was acquired.
DISCONFIRMING_OBSERVATION: >
  An acquired record for a person who never contacted the business carries no recorded basis for
  holding their data, and none can be produced after the fact either.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Acquire a record for a person with no prior contact with the business, and look for what, if
  anything, is recorded to establish the basis for holding their data.
```

## G09-CRM_IAP_MINE-Q011

```yaml
QID: G09-CRM_IAP_MINE-Q011
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When no lawful basis can be established for an acquired record, that record is blocked from being
  loaded or is held for review, rather than being loaded into the pipeline the same as any other
  acquisition.
WHY_IT_MATTERS: >
  Loading a record with no basis at all, purely because the purchase mechanics succeeded, treats a
  commercial transaction as if it settled a legal question it never touched.
DISCONFIRMING_OBSERVATION: >
  An acquired record with no identifiable lawful basis for being held is loaded into the pipeline
  exactly as any properly grounded record would be, with no block or review step.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Arrange or identify an acquisition where no lawful basis for holding the resulting record can be
  established, and observe whether it is loaded regardless.
```

## G09-CRM_IAP_MINE-Q012

```yaml
QID: G09-CRM_IAP_MINE-Q012
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A suppression list — people who have opted out or been removed before — is checked before an
  acquisition request is even made, not only after records have already been delivered and paid for.
WHY_IT_MATTERS: >
  Checking only after delivery means the tenant has already paid to reacquire someone it was
  obligated not to hold, and the harm of having briefly reacquired them has already occurred.
DISCONFIRMING_OBSERVATION: >
  A person on the tenant's own suppression list is included in what is requested and paid for, with
  the suppression check happening only after delivery, if at all.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Add a person to the suppression list, then make an acquisition request whose criteria would
  otherwise include that person, and observe when, if ever, the suppression list is consulted.
```

## G09-CRM_IAP_MINE-Q013

```yaml
QID: G09-CRM_IAP_MINE-Q013
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A record that was previously deleted specifically in response to an erasure or retention request is
  not silently repopulated by a later acquisition that happens to reach the same person.
WHY_IT_MATTERS: >
  Recreating specifically erased data through a different channel defeats the purpose of having
  honored the erasure in the first place, and does so in a way the original request would have had no
  way to anticipate.
DISCONFIRMING_OBSERVATION: >
  A person whose record was deleted in response to an erasure request reappears in the pipeline
  through a later acquisition, with nothing checking for or flagging the prior erasure.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Delete a record in response to an erasure or retention request, then make a later acquisition whose
  criteria would reach the same person, and observe what happens.
```

## G09-CRM_IAP_MINE-Q014

```yaml
QID: G09-CRM_IAP_MINE-Q014
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a purchased batch is only partially delivered — fewer records than paid for — the shortfall is
  detectable and reconcilable against what was charged, rather than a partial delivery looking
  identical to a complete one.
WHY_IT_MATTERS: >
  A partial delivery that looks complete means the tenant has no way to notice it was short-changed,
  let alone seek an adjustment.
DISCONFIRMING_OBSERVATION: >
  A batch delivered with fewer records than the acquisition specified shows no discrepancy between
  what was charged and what was actually received.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Arrange or identify a batch that is delivered short of the number of records the acquisition
  specified, and check whether the shortfall is detectable against the charge.
```

## G09-CRM_IAP_MINE-Q015

```yaml
QID: G09-CRM_IAP_MINE-Q015
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When the same batch, or overlapping records within it, is delivered more than once for a single
  purchase, the duplicate delivery is detected rather than being loaded as though it were additional
  new records.
WHY_IT_MATTERS: >
  A duplicate delivery within one purchase doubles the apparent size of the pipeline for no reason and
  masks a delivery-side fault that ought to be visible.
DISCONFIRMING_OBSERVATION: >
  The same batch, or overlapping records within it, is delivered twice for one purchase and both
  deliveries are loaded as though each contained distinct new records.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Arrange or identify a single purchase whose batch, or part of it, is delivered more than once, and
  observe how the repeat delivery is handled.
```

## G09-CRM_IAP_MINE-Q016

```yaml
QID: G09-CRM_IAP_MINE-Q016
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Months after acquisition, a record can still be traced back to the specific batch or purchase it
  came from, rather than that attribution being available only for a limited period or only shortly
  after delivery.
WHY_IT_MATTERS: >
  Questions about where a given record came from tend to arise long after acquisition, often when
  something has already gone wrong; attribution that has since faded answers nothing at the moment it
  is actually needed.
DISCONFIRMING_OBSERVATION: >
  A record acquired months earlier can no longer be traced back to the specific batch or purchase it
  originated from.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Acquire a record, allow substantial time to pass, and attempt to trace that record back to its
  originating batch or purchase.
```

## G09-CRM_IAP_MINE-Q017

```yaml
QID: G09-CRM_IAP_MINE-Q017
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an acquired record is later updated by some other source — a merge, a manual edit, or a
  different mechanism entirely — its original batch attribution is preserved rather than lost at the
  moment something else touches the record.
WHY_IT_MATTERS: >
  A record's origin should not depend on nobody having touched it since; a business relationship that
  develops normally would otherwise lose its acquisition trail as soon as it starts being worked.
DISCONFIRMING_OBSERVATION: >
  A record's original batch attribution is no longer available after the record is updated or merged
  through some other mechanism.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Acquire a record, then update or merge it through a separate mechanism, and check whether the
  original batch attribution still resolves afterward.
```

## G09-CRM_IAP_MINE-Q018

```yaml
QID: G09-CRM_IAP_MINE-Q018
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a per-call or per-request allowance is exhausted partway through a requested acquisition, the
  outcome for the batch as a whole is a defined, visible partial result rather than an unclear or
  silently truncated one.
WHY_IT_MATTERS: >
  A tenant that requested a specific number of records needs to know clearly whether it received all
  of them or fewer, and why, rather than discovering the shortfall by accident.
DISCONFIRMING_OBSERVATION: >
  An allowance exhausted partway through a requested acquisition produces a batch with fewer records
  than requested and no indication that the shortfall was caused by the allowance running out.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Request an acquisition sized to exhaust the per-call or per-request allowance partway through, and
  observe what the resulting batch communicates about the shortfall.
```

## G09-CRM_IAP_MINE-Q019

```yaml
QID: G09-CRM_IAP_MINE-Q019
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the tenant's monetary credit balance runs out partway through an acquisition operation, the
  operation stops at a defined, reported point rather than continuing to attempt delivery it can no
  longer pay for or leaving the tenant unaware that the balance was the cause of an incomplete result.
WHY_IT_MATTERS: >
  A billing-level failure is a different event from a rate or count limit, and confusing the two, or
  reporting neither clearly, leaves whoever manages the account unable to tell why an acquisition came
  up short.
DISCONFIRMING_OBSERVATION: >
  An acquisition operation that runs out of credit balance partway through produces an incomplete
  result with no indication that the credit balance, specifically, was the reason.
EXPECTED_SURFACE: S2,S3
PRECONDITIONS: >
  Reduce the available credit balance to a level that will be exhausted partway through a requested
  acquisition, and observe what the resulting outcome communicates.
```

## G09-CRM_IAP_MINE-Q020

```yaml
QID: G09-CRM_IAP_MINE-Q020
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A record whose accuracy the tenant has not independently verified carries a visible unverified
  status, distinguishing it from a record confirmed accurate through some other means.
WHY_IT_MATTERS: >
  Treating unverified and verified records identically means every downstream user has to assume the
  worst case, or unknowingly assumes the best case, about data that has never actually been checked.
DISCONFIRMING_OBSERVATION: >
  A newly acquired, never-verified record presents no different status from a record whose accuracy
  has been independently confirmed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Load a newly acquired record with no independent verification performed, and compare its status
  against a record known to have been verified.
```

## G09-CRM_IAP_MINE-Q021

```yaml
QID: G09-CRM_IAP_MINE-Q021
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An unverified acquired record is not used to drive an automated outbound action — a communication,
  an assignment, or similar — before any verification step has had a chance to run against it.
WHY_IT_MATTERS: >
  Acting outward on data nobody has checked risks reaching the wrong person, or a person who should
  never have been contacted at all, in the business's name.
DISCONFIRMING_OBSERVATION: >
  An acquired record with no verification performed triggers an automated outbound action before any
  verification step is applied to it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Acquire a record with automated outbound actions enabled downstream, and observe whether such an
  action can fire before verification occurs.
```

## G09-CRM_IAP_MINE-Q022

```yaml
QID: G09-CRM_IAP_MINE-Q022
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Authorizing the spend for a bulk acquisition is gated by a permission distinct from the permission
  merely to define or browse the filter criteria that would be purchased.
WHY_IT_MATTERS: >
  Deciding what population is worth buying and deciding to actually spend the tenant's money on it are
  different levels of authority; collapsing them lets configuration access alone commit real spend.
DISCONFIRMING_OBSERVATION: >
  A user permitted only to define or browse filter criteria is nonetheless able to commit the spend
  that executes an acquisition against those criteria.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Configure a user with rights to define filter criteria but no explicit spend-authorization
  permission, and attempt to have that user execute a paid acquisition.
```

## G09-CRM_IAP_MINE-Q023

```yaml
QID: G09-CRM_IAP_MINE-Q023
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The acquisition feature is unreachable until an explicit tenant-level configuration step enables
  it, as a decision distinct from whether the tenant happens to have sufficient credit available.
WHY_IT_MATTERS: >
  Having credit available should not, by itself, be enough to make a feature that buys and loads
  external personal data reachable; a tenant should have to deliberately turn it on.
DISCONFIRMING_OBSERVATION: >
  A tenant with sufficient credit but no completed configuration step for the acquisition feature can
  still reach and execute it.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  On a tenant with credit available but no explicit configuration enabling acquisition, attempt to
  reach and execute the feature.
```

## G09-CRM_IAP_MINE-Q024

```yaml
QID: G09-CRM_IAP_MINE-Q024
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  One tenant's acquisition history and the records it has already purchased are not visible to, or
  reusable by, a different tenant on the same platform.
WHY_IT_MATTERS: >
  Acquisition history can reveal a tenant's market strategy and spend, and the acquired records
  themselves are personal data the tenant paid to hold under its own basis; either leaking to another
  tenant is a serious isolation failure.
DISCONFIRMING_OBSERVATION: >
  A different tenant on the same platform can see another tenant's acquisition history, or gains
  access to records that tenant acquired.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  As a user of one tenant, attempt to view or access the acquisition history or acquired records of a
  different, unrelated tenant on the same platform.
```
## G09-CRM_IAP_MINE-Q025

```yaml
QID: G09-CRM_IAP_MINE-Q025
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A delivered record carries some indication of how current the underlying information was at its
  source, rather than being presented with the same apparent freshness whether it was current
  yesterday or long stale.
WHY_IT_MATTERS: >
  Acting on stale information as though it were current leads to wasted outreach and decisions based
  on a state of affairs that no longer holds, with no way to tell that risk applied.
DISCONFIRMING_OBSERVATION: >
  A record known to be based on stale source information is presented identically to one based on
  current information, with no freshness indicator carried into the loaded record.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Acquire a record known to be based on information that was current at some point well in the past,
  and check whether any freshness indicator accompanies it once loaded.
```

## G09-CRM_IAP_MINE-Q026

```yaml
QID: G09-CRM_IAP_MINE-Q026
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Cancelling an in-flight acquisition request actually stops further charges for records not yet
  delivered, rather than only stopping their display while the operation continues to draw down spend
  in the background.
WHY_IT_MATTERS: >
  A cancel action that does not actually stop the spend gives a false sense of control over cost at
  exactly the moment someone chose to exercise it.
DISCONFIRMING_OBSERVATION: >
  After an in-flight acquisition request is cancelled, charges continue to accrue for records that had
  not yet been delivered at the moment of cancellation.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Start a sizeable acquisition request, cancel it partway through, and check whether further spend
  accrues for the portion not yet delivered.
```

## G09-CRM_IAP_MINE-Q027

```yaml
QID: G09-CRM_IAP_MINE-Q027
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Removing or reverting an acquired batch after the fact also addresses activities, assignments, or
  communications already created against those records, rather than leaving them pointing at records
  that have been pulled back out.
WHY_IT_MATTERS: >
  Work already done against a batch does not disappear just because the batch is reverted; leaving it
  orphaned creates confusing, unexplained loose ends for whoever encounters it later.
DISCONFIRMING_OBSERVATION: >
  After an acquired batch is removed or reverted, activities, assignments, or communications already
  created against its records remain in place with no indication that their underlying record was
  pulled back out.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Acquire a batch, create activities or assignments against some of its records, then remove or revert
  the batch and inspect what happens to that downstream work.
```

## G09-CRM_IAP_MINE-Q028

```yaml
QID: G09-CRM_IAP_MINE-Q028
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an acquired record is being loaded at the same time the base pipeline's own duplicate-handling
  is running, the two do not race in a way that leaves an inconsistent or duplicated result.
WHY_IT_MATTERS: >
  Two mechanisms touching the same incoming record at once, with no coordination, is exactly the kind
  of timing gap that produces a record nobody would have designed on purpose.
DISCONFIRMING_OBSERVATION: >
  Loading an acquired record while duplicate-handling runs concurrently against it produces an
  inconsistent result, such as a duplicate that duplicate-handling should have caught, or a record
  left in a contradictory state.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Load an acquired record at a moment engineered to overlap with the base pipeline's own
  duplicate-handling pass, and inspect the outcome.
```

## G09-CRM_IAP_MINE-Q029

```yaml
QID: G09-CRM_IAP_MINE-Q029
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When the company scope that recorded the acquisition's spend differs from the company scope the
  acquired records are loaded into, that difference is deliberate and visible rather than an
  unexplained mismatch between where the money was booked and where the data ended up.
WHY_IT_MATTERS: >
  Spend booked in one company for data landing in another crosses the same boundary the company
  structure exists to keep clear, and should not happen as an unnoticed side effect.
DISCONFIRMING_OBSERVATION: >
  An acquisition's spend is recorded in one company while its records are loaded into a different
  company, with nothing surfacing that the two scopes differ.
EXPECTED_SURFACE: S2,S4
PRECONDITIONS: >
  In a multi-company setup, execute an acquisition where the spend-recording company and the
  record-loading company could plausibly differ, and check whether any mismatch is surfaced.
```

## G09-CRM_IAP_MINE-Q030

```yaml
QID: G09-CRM_IAP_MINE-Q030
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An acquired batch loaded into one company's scope is not visible to users whose access is limited
  to a different company on the same platform.
WHY_IT_MATTERS: >
  Company-scoped access is a control the tenant relies on; a bulk load that bypasses it exposes
  newly acquired personal data to people who were never meant to see it.
DISCONFIRMING_OBSERVATION: >
  A user whose access is limited to one company can see records from an acquired batch that was loaded
  into a different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Load an acquired batch into one company's scope and, as a user limited to a different company,
  attempt to view its records.
```

## G09-CRM_IAP_MINE-Q031

```yaml
QID: G09-CRM_IAP_MINE-Q031
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An acquired record that automatic assignment rules cannot place with any eligible owner is
  distinguishable from a record that became ownerless through the pipeline's own ordinary activity,
  rather than the two ending up looking the same.
WHY_IT_MATTERS: >
  A backlog of unowned records caused by a bulk import behaves differently, and needs a different fix,
  from ordinary attrition of ownership; conflating them hides which problem is actually occurring.
DISCONFIRMING_OBSERVATION: >
  An acquired record left without an eligible owner by the assignment rules is indistinguishable from
  a record that became unowned through ordinary pipeline activity.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Acquire a batch under assignment rules configured with no eligible owner for at least some records,
  and compare the resulting unowned records against ones unowned through ordinary activity.
```

## G09-CRM_IAP_MINE-Q032

```yaml
QID: G09-CRM_IAP_MINE-Q032
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the person behind an acquired record later asks what the business holds about them and how it
  was obtained, the acquisition source for that specific record can actually be retrieved to answer
  the question.
WHY_IT_MATTERS: >
  This is a specific, foreseeable question a business acquiring third-party data must be able to
  answer; being unable to retrieve the source turns a routine disclosure into one it cannot honestly
  make.
DISCONFIRMING_OBSERVATION: >
  Asked to explain how a specific acquired record's data was obtained, nobody can retrieve the
  acquisition source that would answer the question.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Pick a specific acquired record and attempt to retrieve enough information to answer, for that
  record alone, how and from where its data was obtained.
```

## G09-CRM_IAP_MINE-Q033

```yaml
QID: G09-CRM_IAP_MINE-Q033
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A deletion request against a person behind an acquired record actually locates and removes that
  record, rather than the record persisting because its acquisition-driven origin made it harder to
  find than an ordinarily entered one.
WHY_IT_MATTERS: >
  A record that cannot actually be found and removed on request, regardless of how it entered the
  system, leaves the business holding data it was specifically asked to stop holding.
DISCONFIRMING_OBSERVATION: >
  A deletion request against a specific acquired record's subject fails to actually locate or remove
  that record, or removes only part of what was acquired about them.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Acquire a record, then process a deletion request against the person it represents, and verify
  whether the record is actually located and fully removed.
```

## G09-CRM_IAP_MINE-Q034

```yaml
QID: G09-CRM_IAP_MINE-Q034
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Running two acquisition requests with substantially the same filter criteria in close succession
  surfaces some warning or comparison, rather than the second proceeding exactly as if it were an
  unrelated, distinct purchase.
WHY_IT_MATTERS: >
  Without any check, nothing stops a business from unknowingly paying twice for close to the same
  population, simply because nobody remembered or could see the earlier request.
DISCONFIRMING_OBSERVATION: >
  Two acquisition requests with substantially overlapping filter criteria, made close together, both
  proceed with no warning or comparison surfaced to whoever authorized the second one.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Make two acquisition requests with deliberately overlapping filter criteria close together in time,
  and observe whether the second surfaces any relationship to the first.
```

## G09-CRM_IAP_MINE-Q035

```yaml
QID: G09-CRM_IAP_MINE-Q035
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Who defined the purchased filter criteria and who authorized the resulting spend is recorded
  separately from the ordinary field-level history of the records that were delivered.
WHY_IT_MATTERS: >
  Reviewing a purchasing decision requires knowing who decided to buy what and approved paying for
  it, not just what the delivered records eventually contained.
DISCONFIRMING_OBSERVATION: >
  There is no record identifying who defined the filter criteria or who authorized the spend for a
  specific acquisition, separate from the delivered records' own field values.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Execute an acquisition as an identified user and look for a record of who defined its criteria and
  authorized its spend, distinct from the resulting records' field history.
```

## G09-CRM_IAP_MINE-Q036

```yaml
QID: G09-CRM_IAP_MINE-Q036
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A delivered field value that would violate a validation or business rule already in force
  elsewhere in the system is rejected or held for review rather than being loaded in a way that
  quietly breaks that rule.
WHY_IT_MATTERS: >
  A rule enforced against manual entry but not against a bulk external load is not really enforced;
  it simply has an unmonitored side door for large volumes of data at once.
DISCONFIRMING_OBSERVATION: >
  A delivered record is loaded with a field value that violates an existing validation rule, with no
  rejection or review step applied because the value arrived through acquisition rather than manual
  entry.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Identify a field governed by an existing validation rule and acquire a batch containing a record
  whose value for that field would break the rule.
```

## G09-CRM_IAP_MINE-Q037

```yaml
QID: G09-CRM_IAP_MINE-Q037
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a batch succeeds at the external source but fails partway through being imported into the
  pipeline, the spend already committed is reconciled against the count actually loaded rather than
  simply standing as charged for the originally requested count.
WHY_IT_MATTERS: >
  An import failure after a successful purchase is a different fault from a short delivery at the
  source, and paying the full requested amount for records that never actually made it into the
  pipeline is money spent for nothing that can be checked.
DISCONFIRMING_OBSERVATION: >
  A batch that fails partway through import leaves the tenant charged for the full originally
  requested count with no reconciliation against how many records actually ended up loaded.
EXPECTED_SURFACE: S2,S3
PRECONDITIONS: >
  Arrange or identify an acquisition that succeeds at the source but fails partway through import, and
  check whether the resulting charge is reconciled against the actually loaded count.
```

## G09-CRM_IAP_MINE-Q038

```yaml
QID: G09-CRM_IAP_MINE-Q038
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A tenant configured as eligible to run acquisitions is actually able to trigger one at runtime,
  rather than eligibility on paper and reachability in practice being able to silently diverge.
WHY_IT_MATTERS: >
  A tenant or administrator relying on the configured eligibility setting to know the feature works has
  no way to notice a gap where it is configured on but not actually triggerable.
DISCONFIRMING_OBSERVATION: >
  A tenant whose configuration marks acquisition as enabled is unable to actually trigger or complete
  an acquisition at runtime, with nothing surfacing the contradiction.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Configure a tenant as eligible for acquisition and attempt to actually trigger and complete one at
  runtime.
```

## G09-CRM_IAP_MINE-Q039

```yaml
QID: G09-CRM_IAP_MINE-Q039
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a filter criterion used for a past acquisition is later changed, records already acquired
  under the old criterion are not silently treated as if they no longer belong, without that change
  being surfaced anywhere.
WHY_IT_MATTERS: >
  A record's standing in the pipeline should not shift retroactively just because someone later edited
  an unrelated definition; if it does, that shift ought to be visible rather than a quiet side effect.
DISCONFIRMING_OBSERVATION: >
  Editing a filter criterion definition changes how previously acquired records under that criterion
  appear to qualify, with nothing surfacing that the change was retroactive.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Acquire records under a specific filter criterion, then edit that criterion's definition, and check
  whether the previously acquired records are affected and whether any change is surfaced.
```

## G09-CRM_IAP_MINE-Q040

```yaml
QID: G09-CRM_IAP_MINE-Q040
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Duplicate detection applied to acquired records uses the same standard for what counts as the same
  customer that the tenant's own ordinary duplicate handling uses, rather than a separate, undocumented
  standard specific to acquisition.
WHY_IT_MATTERS: >
  Two different definitions of "the same customer" operating side by side in one system means a match
  the tenant would recognize under one standard can be missed entirely under the other.
DISCONFIRMING_OBSERVATION: >
  Two records that the tenant's own ordinary duplicate handling would treat as the same customer are
  not matched as duplicates when one of them arrives through acquisition.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Acquire a record that matches an existing customer under the tenant's own ordinary duplicate
  criteria, and check whether acquisition-side duplicate detection catches it the same way.
```

## G09-CRM_IAP_MINE-Q041

```yaml
QID: G09-CRM_IAP_MINE-Q041
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Each run of a recurring scheduled acquisition is separately attributable as its own batch, rather
  than repeated runs blurring together into one another over time.
WHY_IT_MATTERS: >
  If successive runs cannot be told apart, attribution, spend review, and later troubleshooting all
  collapse into guessing which run a given record or charge actually belongs to.
DISCONFIRMING_OBSERVATION: >
  Records or charges from two different runs of a recurring scheduled acquisition cannot be
  distinguished from one another after the fact.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Configure a recurring scheduled acquisition, let it run more than once, and attempt to attribute
  specific records or charges to a specific run.
```

## G09-CRM_IAP_MINE-Q042

```yaml
QID: G09-CRM_IAP_MINE-Q042
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When records acquired for one stated purpose are later reused for a different, unrelated purpose,
  that reuse remains traceable back to the original acquisition and its stated purpose.
WHY_IT_MATTERS: >
  Data bought for one purpose being quietly repurposed, with no trace of the original justification,
  is exactly the kind of drift that turns a defensible acquisition into one that cannot be explained.
DISCONFIRMING_OBSERVATION: >
  Records acquired for one stated purpose are used for a different purpose later, with no way to trace
  that use back to the original acquisition or its stated purpose.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Acquire records under a specific stated purpose, later use them for an unrelated purpose, and
  attempt to trace that later use back to the original acquisition.
```

## G09-CRM_IAP_MINE-Q043

```yaml
QID: G09-CRM_IAP_MINE-Q043
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The number of records from an acquisition that turn out usable — correct, non-duplicate, matching
  criteria — can be compared against the number originally billed, rather than the billed count being
  the only figure anyone ever sees.
WHY_IT_MATTERS: >
  Without that comparison ever being produced, the billed count stands in, unchallenged, for quality
  that was never actually confirmed.
DISCONFIRMING_OBSERVATION: >
  For a completed acquisition, no comparison exists or can be produced between the number of records
  originally billed and the number that turned out to be usable.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Complete an acquisition, determine how many of its records are actually usable by the tenant's own
  standards, and attempt to produce a comparison against the billed count.
```

## G09-CRM_IAP_MINE-Q044

```yaml
QID: G09-CRM_IAP_MINE-Q044
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a requested filter matches zero eligible records at the source, the tenant is informed before
  any charge is committed, rather than being charged for a request that could never have returned
  anything.
WHY_IT_MATTERS: >
  Charging for a request the source already knows will return nothing is an avoidable cost that a
  basic pre-check would prevent.
DISCONFIRMING_OBSERVATION: >
  A filter that matches zero eligible records at the source still results in a charge being committed
  before the tenant is informed that nothing would be returned.
EXPECTED_SURFACE: S2,S3
PRECONDITIONS: >
  Submit an acquisition request using filter criteria known to match zero eligible records at the
  source, and observe whether a charge is committed regardless.
```

## G09-CRM_IAP_MINE-Q045

```yaml
QID: G09-CRM_IAP_MINE-Q045
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the design states that every acquired record is checked against the suppression list before
  being loaded, that check is actually observable happening at runtime for a given batch, rather than
  the design describing a check the running system does not actually perform every time.
WHY_IT_MATTERS: >
  A documented safeguard that cannot be observed operating is not a safeguard the tenant can actually
  rely on, whatever the design says it should do.
DISCONFIRMING_OBSERVATION: >
  For a specific delivered batch, no observable evidence exists that the suppression-list check
  described in the design actually ran against that batch before it was loaded.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Complete an acquisition and attempt to find observable evidence, specific to that batch, that the
  documented suppression-list check actually ran before loading.
```

## G09-CRM_IAP_MINE-Q046

```yaml
QID: G09-CRM_IAP_MINE-Q046
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The marking that a record originated through acquisition, rather than organic entry, survives that
  record's conversion or promotion further into the pipeline, rather than being lost at that
  transition.
WHY_IT_MATTERS: >
  Conversion is a natural point for auxiliary data an implementation was not specifically built to
  carry forward to be dropped, and origin marking is exactly the kind of auxiliary fact that matters
  most once a record has advanced.
DISCONFIRMING_OBSERVATION: >
  A record known to have originated through acquisition shows no trace of that origin once it has been
  converted or promoted further into the pipeline.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Acquire a record, advance it through conversion or promotion further into the pipeline, and check
  whether its acquisition origin is still marked afterward.
```

## G09-CRM_IAP_MINE-Q047

```yaml
QID: G09-CRM_IAP_MINE-Q047
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When two users in the same tenant submit acquisition requests with overlapping filter criteria at
  close to the same time, the resulting records are attributable back to whichever specific request
  actually produced them, rather than both requests claiming or blending into the same result.
WHY_IT_MATTERS: >
  Without clear attribution between concurrent requests, two people could each believe they
  authorized and paid for a batch that was, in whole or part, actually the other person's.
DISCONFIRMING_OBSERVATION: >
  Two concurrent acquisition requests with overlapping criteria produce records that cannot be
  attributed back to whichever specific request actually caused each one.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Have two users submit acquisition requests with overlapping filter criteria at close to the same
  time, and attempt to attribute the resulting records back to each specific request.
```

## G09-CRM_IAP_MINE-Q048

```yaml
QID: G09-CRM_IAP_MINE-Q048
MODULE: crm_iap_mine
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A single acquisition request far larger than typical batch sizes is subject to some additional
  configured control — a review step, an approval threshold, or similar — rather than being processed
  identically to a routine small request regardless of its size.
WHY_IT_MATTERS: >
  An unusually large single request carries proportionally larger exposure on cost, data volume, and
  lawful-basis risk all at once; treating it as routine misses the one moment extra scrutiny would be
  cheapest to apply.
DISCONFIRMING_OBSERVATION: >
  A single acquisition request many times the size of a typical one proceeds through exactly the same
  path, with no additional review or approval step, as a routine small request.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Submit a single acquisition request far larger than a typical one and compare the path it takes
  against that of a routine small request.
```
