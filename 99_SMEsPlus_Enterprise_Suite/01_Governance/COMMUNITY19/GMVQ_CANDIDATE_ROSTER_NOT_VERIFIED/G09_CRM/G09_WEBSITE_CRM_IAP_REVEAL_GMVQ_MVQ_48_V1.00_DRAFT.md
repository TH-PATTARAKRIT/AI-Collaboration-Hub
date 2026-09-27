# SMEsPlus ENTERPRISE SUITE
## GMVQ — G09 CRM / website_crm_iap_reveal Module Adversarial MVQ Bank

**Document ID:** GMVQ-G09-WEBSITE_CRM_IAP_REVEAL-MVQ48-V1.00
**Group:** G09 CRM
**Module Metadata:** `website_crm_iap_reveal`
**Wave:** W2
**Author Cell:** P-C5 (GMVQ Question Factory — Production Team 25, Acceleration Cell 5)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

This module is the third of the Group Brief's "paid-service family" and a BRIDGE module
(GMVQ_BRIDGE_MODULE_RULE_V1.00). Its seam is unique among the three: it identifies a visitor who never took any
action to identify themselves, by paying a metered external identification service to name who an anonymous
website visit belongs to. Where `crm_iap_enrich` adds data to a record the business already has, and
`crm_iap_mine` acquires records the business did not have, this module's entire subject is a person or
organisation who volunteered nothing at all. Per the Bridge Module Rule, every question below was tested against
"if this capability were removed and an anonymous site visit and a paid, metered external identification service
were used entirely apart, would the question still make sense?" A YES was cut. Question text throughout calls the
external service "a metered external identification service" or "the external service"; it names no vendor,
product, or technical identifier anywhere.

## Control

- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$PKG/01_QUESTION_BANKS/G09_CRM/"*.md |
  sort`. At authoring time this returned the BASE `crm` bank (67 hypotheses), `crm_iap_enrich` (50 hypotheses,
  complete), `crm_iap_mine` (26 hypotheses, still in progress by another cell), and `website_crm_partner_assign`
  (53 hypotheses). All were read in full. This is the sibling check the Bridge Module Rule calls mandatory
  specifically because this module shares a family with two of them.
- Shared-ground discipline against `crm_iap_enrich` and `crm_iap_mine` (Group Brief: shared ground "belongs to
  whichever of the three it bites hardest, not to all three"). A working draft of this bank asked several
  questions that, on inspection, were `crm_iap_enrich`'s or `crm_iap_mine`'s own ground with a noun swapped:
  whether a weak or low-confidence match is carried into a record at full strength (`crm_iap_enrich` already asks
  this generically for any enriched field); whether spend with no usable result is visible (`crm_iap_enrich`
  already asks this); whether per-tenant metering and quota exhaustion mid-operation are handled and visible
  (both siblings already ask this generically for their own paid calls); whether disabling the feature
  retroactively touches records already created (`crm_iap_enrich` already asks this in those exact words for
  enrichment); whether a billed-but-failed call is traceable (`crm_iap_enrich`'s mid-call error question already
  covers this shape); and whether triggering the feature and enabling it tenant-wide are gated by distinct,
  elevated permissions (both siblings already ask this, in `crm_iap_mine`'s case in nearly identical wording).
  Ten questions of that shape were cut entirely rather than kept with a swapped noun. What replaced them, and
  what was kept, asks only what is true of *this* module and neither sibling: the subject never volunteered
  anything, at all, at any point — not a record the business already held (`crm_iap_enrich`), not a name on a
  list the business paid to acquire (`crm_iap_mine`), but a live, anonymous act of browsing the business's own
  site. That fact is what the surviving lawful-basis, disclosure, consent-suppression, shared-device and
  subject-access questions are built around, phrased throughout in terms specific to a live visit rather than to
  a static acquired or existing record.
- `website_crm_partner_assign` and the base `crm` bank were read for awareness; neither touches paid external
  identification of an anonymous visitor, and no overlap was found.
- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong, and no
  two questions share one failure event.
- No padding: 48 questions test 48 distinct material hypotheses, weighted deliberately toward the one fact that
  makes this module's seam different from its two siblings: the subject never identified themselves. Of the 48,
  29 turn directly on that fact (see the per-question count in the handoff report); the remainder cover the
  seam dimensions the Bridge Module Rule and Authoring Standard also require (ordering, partiality, ownership,
  reversal, authority, cross-module boundary, configuration and runtime reachability).
- Clean-room compliance: no vendor or product name, no technical identifier, and the module's own metadata name
  appears in the `MODULE:` field only; question text uses "this feature," "the external service," and "a metered
  external identification service."
- This module carries one layer at the seam; the `LAYER` field is omitted throughout.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. Lane A / Lane B: NOT STARTED
  for this module until rolling batch freeze is recorded.
- Coverage map: certainty, scope, and escalation of an identification Q001-Q007 · misattribution via shared
  context Q008-Q011 · general dispute/correction mechanism Q012 · cost and per-company attribution Q013-Q014 ·
  lawful basis and disclosure Q015-Q018 · consent suppression for declined tracking Q019-Q022 · existing-
  relationship collisions (customer, competitor, employee, master data) Q023-Q026 · forecast/pipeline pollution
  Q027-Q029 · retention duration Q030-Q032 · subject access and erasure rights Q033-Q035 · behavioural scope and
  persistence over time Q036-Q037 · seam ordering, partiality, ownership, reversal, authority and cross-module
  boundary Q038-Q043 · operational/interface seam Q044-Q048.

## G09-WEBSITE_CRM_IAP_REVEAL-Q001

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q001
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The identification's default output is scoped to the organisation level unless a distinct, separately governed
  step resolves it to an individual person.
WHY_IT_MATTERS: >
  Identifying a company that visited a website is a materially different act, with different legal weight, than
  identifying the specific human being who was at the keyboard; collapsing the two by default removes a
  distinction the business needs to manage its exposure.
DISCONFIRMING_OBSERVATION: >
  A visit that the external service can only resolve to an organisation is nonetheless presented or stored as an
  identification of a specific named individual.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Trigger identification for a visit where only organisation-level resolution is available; inspect what is
  stored and shown, and whether it is scoped as an organisation or a person.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q002

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q002
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the identification can escalate from an organisation-level result to naming a specific person, that
  escalation is a distinct, separately recorded event, not something that happens invisibly inside a single
  identification call.
WHY_IT_MATTERS: >
  The escalation from "a company visited" to "this named person visited" is the moment this ground is built
  around; if it is not separately visible, no review can ever tell it happened.
DISCONFIRMING_OBSERVATION: >
  A record's identification moves from organisation-level to naming a specific individual with no separate event,
  log entry, or additional record marking that escalation as having occurred.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger an identification sequence capable of escalating from organisation to individual; inspect the audit
  trail for whether that escalation is distinctly recorded.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q003

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q003
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an organisation-level identification is associated with a specific individual as a likely contact rather
  than the actual visitor, the record makes clear that the named individual is a suggested contact at that
  organisation, not asserted as the person who actually visited.
WHY_IT_MATTERS: >
  Presenting "a plausible contact at the identified company" as though it were "the person who visited"
  attributes an actual visit and interest to someone who may have had nothing to do with it.
DISCONFIRMING_OBSERVATION: >
  A record names a specific individual as though they were the visitor, when the underlying identification only
  ever established the organisation and separately suggested a likely contact there.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Trigger an identification that returns an organisation plus a suggested contact person; inspect how the record
  and its presentation distinguish "visitor" from "suggested contact."
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q004

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q004
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Any consent, disclosure, or retention rule that differs between organisation-level and individual-level
  identification is applied according to which level the record actually reached, not applied uniformly
  regardless of level.
WHY_IT_MATTERS: >
  If the stricter individual-level obligations are never actually triggered because the system does not
  distinguish levels operationally, the business is out of compliance without any visible failure to point to.
DISCONFIRMING_OBSERVATION: >
  A record that reached individual-level identification is handled under the same retention or disclosure
  treatment as an organisation-level-only record, with no distinction applied.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare the retention/disclosure configuration or behaviour applied to an organisation-level record against an
  individual-level record; check whether they differ as the business's own policy would require.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q005

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q005
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where an identification has escalated to naming a specific individual rather than only an organisation, access
  to that individual-level detail is restricted to a narrower set of roles than access to the organisation-level
  result alone.
WHY_IT_MATTERS: >
  The organisation-level fact and the individual-level fact carry different sensitivity, and access should narrow
  accordingly; if every role that can see one can see the other, the more sensitive fact gets no additional
  protection at all.
DISCONFIRMING_OBSERVATION: >
  A role permitted to view organisation-level identification results can view individual-level identification
  results with no additional restriction.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Compare the role/permission required to view an organisation-level-only result against an individual-level
  result; check whether access differs.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q006

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q006
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If the external service later retracts or corrects an identification it previously returned, that correction is
  reflected against the already-created record rather than the original, now-known-wrong identification standing
  unchanged indefinitely.
WHY_IT_MATTERS: >
  An identification is a claim from a third party, not a fact the business generated itself; leaving a retracted
  claim standing after the source withdraws it means the business is knowingly acting on information it has
  reason to believe is wrong.
DISCONFIRMING_OBSERVATION: >
  An identification later corrected or retracted by the external service leaves the originally created record
  entirely unchanged, with no mechanism by which such a correction could ever reach it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Determine whether any mechanism exists for the external service's corrections or retractions to be received and
  applied; assess what would happen to an existing record if one arrived.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q007

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q007
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The language and presentation shown to a salesperson about an identified visitor describes it as an inference or
  a match, not as an established fact about who the visitor is.
WHY_IT_MATTERS: >
  Wording that overstates certainty directly causes the exact harm this ground names: a salesperson treating a
  probabilistic guess as settled truth when contacting or reporting on that visitor.
DISCONFIRMING_OBSERVATION: >
  The staff-facing presentation of an identified visitor states or strongly implies certainty rather than framing
  it as a probabilistic match from an external source.
EXPECTED_SURFACE: S5
PRECONDITIONS: >
  Trigger an identification and review the exact wording and presentation shown to staff describing the result.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q008

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q008
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A visit attributable to a network address known to be shared across many unrelated occupants, rather than a
  single organisation's dedicated connection, is treated with a distinctly lower confidence, or flagged, rather
  than being identified with the same certainty as a dedicated one.
WHY_IT_MATTERS: >
  Attributing a visit to whoever is registered against a shared address misidentifies the visitor as an
  organisation that may have had no employee anywhere near that visit.
DISCONFIRMING_OBSERVATION: >
  A visit from a network address known or knowable to be broadly shared is identified and presented with the same
  confidence and treatment as one from a dedicated, single-occupant address.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Identify or simulate a visit from a network address known to be shared across many occupants; compare the
  resulting record's confidence/flagging against one from a dedicated address.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q009

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q009
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Repeated visits from the same shared network address do not accumulate into an increasingly "confirmed-looking"
  record for the wrongly attributed organisation merely because the volume of visits is high.
WHY_IT_MATTERS: >
  A misattribution that grows more convincing purely from repetition, with no actual increase in evidence quality,
  misleads staff into treating volume as verification.
DISCONFIRMING_OBSERVATION: >
  A record built from many visits originating from a known-shared network address is presented with higher
  confidence or stronger signal purely because of visit count, with no correction for the shared nature of the
  address.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Simulate repeated visits from the same known-shared network address; inspect whether the resulting record's
  presented confidence increases with volume alone.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q010

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q010
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When staff determine that an identification was a shared-network misattribution, a defined action exists to
  correct or suppress that record, distinct from an ordinary data-quality edit.
WHY_IT_MATTERS: >
  Without a defined remedy, a known-bad identification either lingers indefinitely or is corrected inconsistently,
  and there is no way to know how often this failure mode occurs.
DISCONFIRMING_OBSERVATION: >
  No distinct action or process exists for correcting or suppressing a record identified as a shared-network
  misattribution; staff have only the same generic edit tools used for any other data error, with no way to
  record why the correction was needed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Identify a record believed to be a shared-network misattribution; determine what action staff can take against
  it and whether the reason for that action is captured.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q011

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q011
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeat visits from the same device or browser are not assumed to be the same individual without at least the
  same level of caution applied to shared network addresses, since a personal device can also be used by more than
  one person.
WHY_IT_MATTERS: >
  Attributing a family member's or colleague's browsing to whoever was first identified on that device compounds
  the misidentification risk into an ongoing, incorrect profile of activity that was never theirs.
DISCONFIRMING_OBSERVATION: >
  All browsing activity from a given device or browser is attributed to a single identified individual
  indefinitely, with no mechanism to reconsider that assumption.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Simulate two distinct browsing patterns from the same device/browser context after one has been identified;
  inspect whether both are attributed to the same identity.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q012

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q012
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Staff have a defined way to flag a specific identification as believed wrong, for any reason, distinct from the
  shared-network-specific remedy (Q010), and that flag is recorded against the record rather than only correctable
  through an ordinary, unmarked data edit.
WHY_IT_MATTERS: >
  Without a general dispute mechanism distinct from routine editing, wrong identifications of every kind — not
  just the shared-network case — accumulate with no way to measure how often the feature gets it wrong or to feed
  that back into how much staff should trust it.
DISCONFIRMING_OBSERVATION: >
  No mechanism exists for staff to mark a specific identification as disputed or believed incorrect other than
  editing the record's fields the same way any ordinary data correction would be made, indistinguishable from a
  routine edit.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Locate a record produced by this feature; determine whether any distinct dispute/flag mechanism exists beyond
  ordinary field editing, and whether using it produces a different, recorded outcome than a routine edit.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q013

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q013
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A repeat visit within a defined window by a visitor already successfully identified does not itself trigger a
  second billable lookup call, as distinct from retrying a call that had previously failed.
WHY_IT_MATTERS: >
  Paying twice for the same answer to a repeat visit, as opposed to a legitimate retry of a failed attempt, is a
  direct, avoidable cost with no corresponding business benefit, and left unchecked can multiply for a visitor who
  returns frequently.
DISCONFIRMING_OBSERVATION: >
  A repeat visit within whatever window the business considers current, by a visitor already successfully
  identified on an earlier visit, triggers a fresh billable lookup call rather than reusing the existing result.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Identify a visitor once, then simulate a return visit from the same visitor within a short window; inspect
  whether a second billable lookup call is triggered.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q014

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q014
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where multiple companies operate under one tenant, spend on identification calls triggered by one company's site
  traffic can be attributed to that specific company, distinct from the tenant-wide usage tracking that governs
  the tenant as a whole.
WHY_IT_MATTERS: >
  Without company-level attribution nested inside whatever tenant-level tracking already exists, one company's
  traffic silently consumes budget that another company on the same tenant believed was its own, and no one can
  tell the two apart.
DISCONFIRMING_OBSERVATION: >
  Spend triggered by one company's public site traffic cannot be distinguished from another company's spend
  anywhere the tenant's cost is reported, even though the tenant-level total itself is tracked.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  In a multi-company tenant, trigger identification spend against one company's site; inspect whether spend
  reporting can attribute it to that company specifically versus another, distinct from the tenant-wide total.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q015

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q015
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Each real-time identification of a live, otherwise-anonymous visit captures what basis is being relied on for
  that specific visit, rather than the business relying on one blanket basis statement covering every anonymous
  visitor generally, with nothing tying it to this particular visit's own circumstances.
WHY_IT_MATTERS: >
  A basis that covers "anonymous visitors" as one blanket category, rather than being tied to a specific visit's
  own circumstances, cannot actually answer for what made this particular, individual act of identification
  justified when it is challenged.
DISCONFIRMING_OBSERVATION: >
  An individual identification event carries no recorded link to any basis specific to that visit; whatever basis
  exists is only a blanket statement covering all anonymous visitors generally, with nothing tying it to this
  particular event.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger an identification event; inspect whether the resulting record or its audit trail references any basis
  specific to that visit, distinct from a general policy statement.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q016

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q016
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The website discloses to visitors, before or at the point their visit could be identified, that this kind of
  identification takes place, through the same kind of notice mechanism used for other data practices on the
  site.
WHY_IT_MATTERS: >
  An identification practice with no visitor-facing disclosure at all denies visitors the one thing that could let
  them make an informed choice, or exercise a right, about a practice happening to them without their
  participation.
DISCONFIRMING_OBSERVATION: >
  No disclosure of the identification practice is findable anywhere a visitor could reasonably be expected to see
  it before or in connection with their visit.
EXPECTED_SURFACE: S5
PRECONDITIONS: >
  Review the site's visitor-facing notices for any disclosure of the identification practice; assess whether it
  is present and reasonably discoverable.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q017

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q017
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the lawful basis available for this kind of identification differs by the visitor's jurisdiction, the
  system's behaviour, whether it identifies at all and under what basis, can actually vary by jurisdiction, rather
  than applying one basis globally regardless of where the visitor is.
WHY_IT_MATTERS: >
  Applying a basis that is only valid in some jurisdictions to visitors everywhere means the business is relying
  on a justification it does not actually have for a portion of the people it identifies.
DISCONFIRMING_OBSERVATION: >
  The system has no capability to vary whether or how identification occurs based on the visitor's jurisdiction,
  applying one uniform behaviour regardless of where a plausible basis would differ.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Determine whether the system has any jurisdiction-aware configuration for this feature; assess whether it can
  restrict or alter identification behaviour by region.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q018

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q018
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If the external identification service itself changes what it says it is lawfully permitted to provide, that
  change is something the business would actually notice and could act on, rather than the integration continuing
  to request and accept whatever is returned with no review trigger.
WHY_IT_MATTERS: >
  The business's own lawful basis can rest partly on the external service's certifications or terms; if that
  changes upstream with nothing downstream noticing, the business keeps relying on a basis that no longer holds.
DISCONFIRMING_OBSERVATION: >
  No process, configuration, or point of visibility exists by which a change in the external service's stated
  terms or permitted use would ever come to the business's attention.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Determine whether any mechanism exists tied to the external service's terms of use for this feature: a
  contractual review trigger, configuration flag, or periodic check.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q019

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q019
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the external identification service itself maintains or honors a general opt-out that applies across its
  client businesses, a visitor covered by that broader opt-out is not identified by this integration either,
  rather than only this site's own local consent choice being capable of preventing identification.
WHY_IT_MATTERS: >
  A visitor who has taken the trouble to opt out of this entire category of service, rather than just this one
  site's consent banner, has expressed a broader preference; an integration that only respects the local banner
  and ignores the service's own opt-out defeats a choice the visitor already made elsewhere.
DISCONFIRMING_OBSERVATION: >
  A visitor known to be covered by the external service's own general opt-out is still returned as an identified
  match by this integration, with only the local site's consent banner treated as capable of suppression.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Determine whether the external service exposes any opt-out or suppression signal of its own; simulate a visitor
  covered by it; inspect whether identification is still attempted or honored.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q020

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q020
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  For a visitor who has declined tracking through the site's own consent mechanism, the specific request that
  would be sent to the external identification service is itself suppressed, rather than the request still being
  sent while only the resulting local record is hidden or discarded afterward.
WHY_IT_MATTERS: >
  If the outbound request to the third party still happens regardless of a decline, the visitor's data has already
  left the business's control to the paid service before any local suppression could matter — the harm the
  decline exists to prevent has already occurred.
DISCONFIRMING_OBSERVATION: >
  For a visitor who has declined tracking, a request is still transmitted to the external identification service,
  even if the response is then discarded or hidden locally.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Decline tracking as a visitor; using any observable means, determine whether an outbound request to the external
  service is nonetheless made for that visit.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q021

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q021
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A visitor's decision to decline tracking is remembered across a return visit within any period the consent
  mechanism itself claims to honor, not reset so that identification resumes on every new visit regardless of the
  earlier decline.
WHY_IT_MATTERS: >
  A decline that only holds for a single visit provides no real protection for a visitor who returns, and
  misrepresents what the consent mechanism claims to do.
DISCONFIRMING_OBSERVATION: >
  A visitor who declined tracking on an earlier visit, still within the period the consent mechanism claims to
  honor that choice, triggers identification on a subsequent visit as though no decline had occurred.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Decline tracking on one visit, then return within the claimed honor period on a later visit; inspect whether
  identification is triggered on the return visit.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q022

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q022
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A decline of tracking that takes effect between the moment a visit begins and the moment the identification call
  would actually be dispatched still prevents that call, rather than only a decline already in place before the
  visit started being honored.
WHY_IT_MATTERS: >
  If only the state at visit-start governs, a visitor who declines partway through their visit, well before any
  call is actually sent, is identified anyway, despite having acted in time to prevent it.
DISCONFIRMING_OBSERVATION: >
  A visitor who declines tracking after their visit begins but before the identification call is actually
  dispatched is identified anyway, as though the decline had no effect because it came after some earlier
  checkpoint.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Begin a visit without declining, then decline tracking before the point at which the identification call would
  normally be dispatched; inspect whether the call still occurs.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q023

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q023
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A visitor identified by the paid service who matches an existing customer record is linked to that record rather
  than a new, separate identity being created for them.
WHY_IT_MATTERS: >
  Creating a second identity for someone the business already has a relationship with fragments history and can
  also mean paying for information the business already possessed for free.
DISCONFIRMING_OBSERVATION: >
  A visitor matching an existing customer is identified and recorded as a wholly new entity, with no link to the
  existing customer record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Have an existing customer visit the site anonymously; trigger identification; inspect whether the result links
  to the existing customer record.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q024

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q024
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An identified visitor recognized as belonging to a known competitor is handled through some distinct path or
  flag, not fed into the ordinary sales pipeline as though it were a genuine prospect.
WHY_IT_MATTERS: >
  Treating a competitor's research visit as a sales opportunity wastes staff effort and, depending on what a
  salesperson does with it, risks exposing pricing or approach to a competitor unnecessarily.
DISCONFIRMING_OBSERVATION: >
  A visit identified as belonging to a known competitor organisation is processed into the ordinary pipeline with
  no distinguishing flag or different handling from a genuine prospect.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Determine whether any competitor list or flagging mechanism exists; simulate a visit identified as belonging to
  a listed competitor; inspect how the resulting record is handled.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q025

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q025
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A visit from the business's own staff, such as someone testing the site or an employee visiting from a personal
  device, that gets identified through the paid service is distinguishable, once recognized, from an external
  prospect, and does not silently pollute the pipeline as a fabricated lead.
WHY_IT_MATTERS: >
  Internal traffic misclassified as a prospect wastes the same paid lookup budget and clutters the pipeline with
  records that can never convert, quietly distorting whatever metrics are drawn from it.
DISCONFIRMING_OBSERVATION: >
  A visit later recognized as internal staff traffic remains in the pipeline as an ordinary prospect record with
  no means of excluding or flagging it once recognized.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Simulate an internal staff visit that is identified by the feature; determine what means, if any, exist to
  exclude or flag it once recognized as internal.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q026

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q026
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an identified visitor's organisation already exists as a master record with its own maintained details,
  the paid service's returned details do not silently overwrite the maintained master data without any staff
  decision.
WHY_IT_MATTERS: >
  An external, purchased data point overwriting carefully maintained internal master data with no review can
  degrade data quality the business has invested effort to keep accurate.
DISCONFIRMING_OBSERVATION: >
  Details returned by the external identification service for an organisation already present as a master record
  overwrite the existing maintained fields automatically, with no staff review step.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Identify a visitor belonging to an organisation with an existing, maintained master record with differing
  details; trigger identification; inspect whether the master record changes automatically.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q027

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q027
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A record created purely from an identified anonymous visit, where the visitor took no action indicating actual
  interest such as filling in any form, is distinguishable in the pipeline from a record created from an active
  inbound inquiry.
WHY_IT_MATTERS: >
  Collapsing "someone merely visited a page" with "someone actively asked to be contacted" into the same-looking
  pipeline record inflates the apparent number of genuine prospects with records that carry no real signal of
  interest.
DISCONFIRMING_OBSERVATION: >
  A record created solely from an identified anonymous visit is presented and categorized identically to a record
  created from an active inbound inquiry, with no distinguishing indicator of its lower-signal origin.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Trigger identification for an anonymous visit with no accompanying form submission or other explicit action;
  inspect how the resulting record is categorized relative to an active inquiry.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q028

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q028
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A record created purely because a visitor's own browsing behaviour on the business's site was identified — with
  no qualification step and no request from that visitor for any contact — is not automatically included in a
  forecast total the same way a qualified inbound inquiry is.
WHY_IT_MATTERS: >
  A forecast inflated by every anonymous visit the business happens to be able to identify, none of it requested by
  the visitor, misleads decisions built on the assumption that pipeline size reflects actual expressed customer
  interest — a different distortion than a purchased list record with no interaction at all.
DISCONFIRMING_OBSERVATION: >
  A record created purely from visitor identification, with no qualification step performed and no action taken by
  the visitor beyond browsing, is included in a forecast total alongside qualified pipeline records with no
  distinction in how the total is computed or presented.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a record from identification alone with no qualification and no visitor-initiated action; inspect whether
  it is included in a forecast view or total, and how.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q029

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q029
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A high volume of identification-only records does not degrade a salesperson's or manager's ability to find and
  prioritize the genuine, actively-expressed-interest records in the same pipeline view.
WHY_IT_MATTERS: >
  If low-signal records are indistinguishable and numerous, the very people meant to act on real interest can lose
  it in noise generated by a feature meant to help them.
DISCONFIRMING_OBSERVATION: >
  A pipeline view containing a large number of identification-only records provides no way to filter, sort, or
  otherwise separate them from actively-expressed-interest records.
EXPECTED_SURFACE: S5
PRECONDITIONS: >
  Populate a pipeline view with a mix of identification-only and actively-expressed-interest records; inspect what
  filtering or sorting capability exists to separate them.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q030

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q030
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The default retention of an identification result is a deliberate, documented choice, whether session-only or a
  defined longer period, not an unexamined default inherited from wherever the general record-storage mechanism
  happens to keep things indefinitely.
WHY_IT_MATTERS: >
  An identification about someone who never chose to be known to the business is a more sensitive category of data
  than most a CRM holds, and its retention default deserves to be a decision, not an accident of implementation.
DISCONFIRMING_OBSERVATION: >
  No documented or configurable retention decision exists for identification results; they persist under whatever
  the general record-storage default happens to be, applied without having been considered for this specific kind
  of data.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Locate any documented or configurable retention setting specific to identification results; assess whether one
  exists distinct from the general record retention default.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q031

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q031
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where the business has configured identification data to be session-only, that data is actually removed or not
  persisted beyond the session, not merely hidden from the interface while still present underneath.
WHY_IT_MATTERS: >
  A "session-only" setting that only hides data from view while leaving it stored underneath does not deliver what
  it claims, and misleads anyone relying on that setting for a compliance reason.
DISCONFIRMING_OBSERVATION: >
  With identification data configured as session-only, the underlying data is still retrievable after the session
  has ended, whether or not it remains visible in the ordinary interface.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure or determine the session-only retention setting; end the session; attempt to retrieve the
  identification data through any available means afterward.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q032

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q032
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once an identification result has become the basis for an actual pipeline record a salesperson is working, the
  record's retention follows the pipeline's normal retention rules for business records, and a separate short
  "identification-only" retention setting does not cause the record itself to be deleted out from under active
  sales work.
WHY_IT_MATTERS: >
  If a short retention setting meant for a raw, unused identification also silently erases a record that has since
  become active sales work, staff lose their own work with no warning tied to a setting they may not even know
  applies to it.
DISCONFIRMING_OBSERVATION: >
  A record that has become an actively worked pipeline item is deleted or altered due to a retention setting
  intended for unused, raw identification data.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Convert an identification result into an actively worked pipeline record; allow the raw-identification
  retention period to elapse; inspect whether the now-active record is affected.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q033

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q033
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A subject access request can be resolved against records created through this feature using only the kind of
  identifying detail the requester themselves could reasonably provide, such as their name or company, without
  requiring them to already know a record exists or under what identifier it was filed.
WHY_IT_MATTERS: >
  Someone who was identified without their knowledge cannot be expected to know what identifier their record was
  filed under; if the request process assumes that knowledge, the right is theoretical rather than actually usable
  by exactly the people this ground concerns.
DISCONFIRMING_OBSERVATION: >
  No means exists to search for or locate a record created through this feature using only the ordinary
  identifying details a requester who does not know a record exists could reasonably supply.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt to locate a record created through this feature using only the kind of detail an unaware data subject
  could supply, without prior knowledge of any internal identifier.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q034

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q034
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A response to a subject access request about a record created through this feature discloses that the data came
  from an identification of their anonymous website visit via a paid external service, rather than describing the
  record's origin in a way that obscures how it was actually obtained.
WHY_IT_MATTERS: >
  A person exercising this right is specifically trying to understand how the business came to have information
  about them; an origin description that obscures the actual mechanism defeats the purpose of answering the
  request at all.
DISCONFIRMING_OBSERVATION: >
  A subject access response concerning a record created through this feature does not state, or actively obscures,
  that the data originated from a paid identification of an anonymous visit.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Locate a record created through this feature and construct what its subject access response would state about
  its origin; assess whether that origin is accurately disclosed.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q035

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q035
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A deletion or objection request against a record created through this feature is honored through the same
  process and to the same extent as any other personal data the business holds, with no exception carved out
  because the data originated from a purchased identification rather than being volunteered.
WHY_IT_MATTERS: >
  If purchased identification data is treated as somehow exempt from the rights that apply to volunteered data,
  the business has created a category of personal data specifically immune to the rights that exist to govern it.
DISCONFIRMING_OBSERVATION: >
  A deletion or objection request against a record created through this feature is refused, only partially
  honored, or handled through a different, weaker process than the same request against volunteered personal
  data.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit a deletion or objection request against a record created through this feature and against a comparable
  volunteered record; compare how each is processed.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q036

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q036
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an anonymous visit is identified, the specific pages or content the visitor viewed before being identified
  becoming attached to a now-named record is itself something the stated basis and disclosure (Q015-Q016) account
  for — the business is not only naming who visited but also permanently attaching what a specific person or
  organisation looked at.
WHY_IT_MATTERS: >
  Naming a visitor after the fact retroactively turns previously anonymous browsing behaviour into a named
  individual's or organisation's permanent behavioural record, a materially bigger disclosure than the identity
  alone, and one the stated basis may not have contemplated.
DISCONFIRMING_OBSERVATION: >
  The browsing detail preceding identification is attached to the resulting named record with no consideration in
  the stated basis or disclosure for behavioural detail being retroactively tied to a name.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger identification following a visit with specific, recorded browsing activity; inspect whether that
  activity is attached to the resulting named record and whether the basis/disclosure addresses this.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q037

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q037
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Once a visitor has been identified once, a subsequent, otherwise-anonymous return visit is not automatically and
  permanently attributed to that same identity without a fresh consideration of whether the original basis for
  identification still covers a new, separate visit.
WHY_IT_MATTERS: >
  Treating a one-time paid identification as a permanent unlock that attributes all future visits to the same
  person indefinitely expands what was purchased once into ongoing tracking the original act may never have
  justified.
DISCONFIRMING_OBSERVATION: >
  A later, separate visit by the same individual is silently and permanently attributed to their earlier
  identification with no fresh trigger, review, or time-bound limit governing how long a past identification
  continues to attach to new activity.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Identify a visitor once; on a materially later, separate visit, inspect whether that new activity is
  automatically attributed to the earlier identity and whether any time bound governs this.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q038

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q038
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where identification is resolved asynchronously after the visit itself has ended, the eventual result is still
  correctly associated with the specific visit that triggered it, not attached to whatever visit happens to be
  active when the response arrives.
WHY_IT_MATTERS: >
  Misassociating a delayed identification result to the wrong visit would attribute one visitor's interest or
  behaviour to a completely different visit, corrupting exactly the record the feature exists to produce.
DISCONFIRMING_OBSERVATION: >
  An identification result that returns after the triggering visit has ended is associated with a different,
  unrelated visit rather than the one that actually triggered the lookup.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Trigger an identification call, end the visit/session before a response would normally return, allow a
  different visit to begin, and inspect which visit the eventual result is attached to.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q039

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q039
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A partial identification result, where part of the lookup succeeded and another part failed or timed out, is
  stored and presented in a way that is distinguishable from a fully completed identification.
WHY_IT_MATTERS: >
  A partial result presented as though it were complete leaves staff acting on less information than they believe
  they have, with no way to know a further, unresolved piece was attempted at all.
DISCONFIRMING_OBSERVATION: >
  A record built from a partially failed or partially timed-out identification call is presented identically to
  one built from a fully successful call, with no indication that part of the lookup did not complete.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Force or simulate a partial failure in a multi-step identification call; inspect whether the resulting record or
  its presentation distinguishes this from a fully successful call.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q040

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q040
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A record created by identifying a visitor from an organisation that already has an assigned owner within the
  business is routed to that existing owner, rather than being independently assigned without regard to the
  existing relationship.
WHY_IT_MATTERS: >
  Routing a new record to someone other than the account's existing owner fragments a single business relationship
  across two salespeople with no coordination, a well-known source of internal conflict and a confused customer
  experience.
DISCONFIRMING_OBSERVATION: >
  A record created via identification for an organisation with an existing assigned owner elsewhere in the
  business is routed to a different owner with no reference to the existing assignment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Identify a visitor belonging to an organisation with an existing assigned owner in the business; trigger the
  feature; inspect who the resulting record is routed to.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q041

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q041
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Correcting or removing a record found to be misidentified preserves a clear account of what activity was
  actually performed against it, such as contact attempts or notes, even though the identity itself is now known
  to be wrong, rather than silently discarding that activity history along with the bad identification.
WHY_IT_MATTERS: >
  If a salesperson already reached out based on a bad identification, that outreach happened to a real recipient
  and has its own consequences; losing the record of it prevents the business from ever knowing it occurred or
  correcting course with that recipient.
DISCONFIRMING_OBSERVATION: >
  Correcting or removing a misidentified record also removes any trace that activity had already been performed
  against it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a record via identification, log some activity against it, then correct or remove it as misidentified;
  inspect whether the prior activity remains traceable.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q042

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q042
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Access to the raw identification data — what the external service actually returned, and on what basis — is at
  least as restricted as, and may be more restricted than, access to the ordinary business fields of the record it
  produced.
WHY_IT_MATTERS: >
  The raw identification data is the more sensitive artifact: it is direct evidence of how a person was identified
  without their participation, and deserves at least the same protection as the record it feeds, not looser access
  because it sits one layer beneath the visible record.
DISCONFIRMING_OBSERVATION: >
  A staff role able to view a record's ordinary business fields can also view the raw identification data behind
  it, even where that role has no defined need for the more sensitive underlying detail.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Identify a role with ordinary read access to records produced by this feature; check whether that same role can
  access the raw identification data behind a given record.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q043

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q043
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a record created by this feature is subsequently enriched through the separate paid data-enrichment
  capability, the enrichment step still has access to the fact that the record's underlying subject never took any
  action to identify themselves, rather than treating it as an ordinary record of unknown origin.
WHY_IT_MATTERS: >
  Losing this context at the handoff to enrichment means later processing, and anyone reviewing the record
  afterward, loses track of exactly the origin fact this whole ground is built around, at the one point another
  capability might otherwise compound it with more purchased data.
DISCONFIRMING_OBSERVATION: >
  A record created by this feature and subsequently passed through the enrichment capability shows no trace, after
  enrichment, that its original subject never took any identifying action themselves.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a record via this feature, then run it through the enrichment capability if reachable; inspect whether
  the record's origin context survives that step.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q044

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q044
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  At the point a salesperson is about to act on a record produced by this feature, for example before placing an
  outbound contact, the interface makes clear that the subject never initiated contact or identified themselves,
  rather than that fact being available only if the salesperson goes looking for it.
WHY_IT_MATTERS: >
  A salesperson who does not realize they are about to contact someone who never asked to be found is far more
  likely to open that contact in a way that surprises or alarms the recipient, and to disclose the mechanism poorly
  if asked how the business found them.
DISCONFIRMING_OBSERVATION: >
  A salesperson can reach the point of contacting an identified visitor with no indication in the immediate
  interface that the subject never initiated any contact or identified themselves.
EXPECTED_SURFACE: S5
PRECONDITIONS: >
  Create a record via identification; walk through the interface path a salesperson would use to initiate contact;
  check what, if anything, warns them of the record's unprompted origin at that point.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q045

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q045
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A defined engagement threshold, such as depth or duration of the visit, governs which anonymous visits are even
  eligible to trigger identification, rather than the lightest, most fleeting visit being just as eligible as an
  extended one.
WHY_IT_MATTERS: >
  Identifying someone who barely glanced at a page for a moment they never chose to spend investigating the
  business is a proportionally harder case to justify than identifying someone who engaged deeply; without a
  defined threshold, the feature is applied at its most invasive setting by default.
DISCONFIRMING_OBSERVATION: >
  A visit lasting a trivial amount of time, on a single incidental page, triggers full identification with no
  eligibility threshold distinguishing it from a deep, sustained visit.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Simulate a very brief, shallow visit and a longer, deeper visit; inspect whether both trigger identification
  identically or whether an eligibility threshold distinguishes them.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q046

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q046
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A visitor who was already identified through this feature, and who then submits the public web form themselves,
  is reconciled to the same underlying identity rather than the explicit submission and the earlier passive
  identification producing two separate, unlinked records.
WHY_IT_MATTERS: >
  Failing to reconcile the two means the business ends up with a passively-identified guess and a freely-given,
  higher-trust submission sitting as two disconnected records for the same person, and staff working the guess may
  never see that the person has since actually reached out on their own.
DISCONFIRMING_OBSERVATION: >
  A visitor identified through this feature who subsequently submits the public form themselves produces a second,
  independent record with no link to the earlier identification-based record.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Trigger identification for a visitor, then have that same visitor submit the public web form under their real
  details; inspect whether the two are reconciled or remain separate.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q047

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q047
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once an identified visitor's organisation converts into an actual paying customer through the normal sales
  process, the fact that the relationship began from an unprompted identification of an anonymous visit remains
  part of that customer's permanent history rather than being absorbed and lost once ordinary customer records
  take over.
WHY_IT_MATTERS: >
  Losing this origin fact once a relationship "graduates" to customer status would mean the one moment a subject
  access or audit request most needs an answer, how did the business first come to know this now-customer, becomes
  unanswerable precisely because the relationship succeeded.
DISCONFIRMING_OBSERVATION: >
  A converted customer's record retains no trace that the relationship originated from an unprompted identification
  of an anonymous website visit, once ordinary customer records and processes have taken over.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Identify a visitor, progress that record through to a converted customer via the normal sales process, and
  inspect whether the origin fact is still traceable in the resulting customer record's history.
```

## G09-WEBSITE_CRM_IAP_REVEAL-Q048

```yaml
QID: G09-WEBSITE_CRM_IAP_REVEAL-Q048
MODULE: website_crm_iap_reveal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where an identification result returns only after a delay long enough that the visit's business context has
  materially moved on, the delayed result is marked or timestamped clearly enough that staff can judge its
  staleness rather than presenting it as current.
WHY_IT_MATTERS: >
  A salesperson acting on a stale identification as though it were fresh may reach out referencing interest or
  context that no longer reflects what is actually happening, undermining the very credibility the outreach is
  meant to build.
DISCONFIRMING_OBSERVATION: >
  A materially delayed identification result is presented to staff with no timestamp or staleness indicator
  distinguishing it from an immediate result.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Force or simulate a materially delayed identification response; inspect how it is presented to staff and whether
  its age or staleness is indicated.
```
