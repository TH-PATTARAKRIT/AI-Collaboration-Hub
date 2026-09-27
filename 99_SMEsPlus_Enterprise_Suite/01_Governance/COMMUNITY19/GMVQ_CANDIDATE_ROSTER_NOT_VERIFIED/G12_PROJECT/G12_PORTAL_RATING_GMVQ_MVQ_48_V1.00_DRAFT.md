# SMEsPlus ENTERPRISE SUITE
## GMVQ — G12 PROJECT / portal_rating Module MVQ Bank

**Document ID:** GMVQ-G12-PORTAL_RATING-MVQ48-V1.00
**Group:** G12 PROJECT (Wave 3)
**Module Metadata:** `portal_rating`
**Wave:** W3
**Author Cell:** P12-1 (GMVQ Question Factory — Production Cell P12-1)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies the module-specific (MVQ) tier for the generic satisfaction-rating mechanism
that can be attached to any parent record (a task, a case, a delivery, or similar) and reached by an
external party, typically through an unauthenticated, token-based link. Material ground: the
mechanism's own generic behaviour independent of any specific parent model — token security and
scope, submission integrity (single submission, editability, expiry), aggregation and averaging
correctness, moderation of free-text feedback, and cross-tenant boundary of who can see whose
rating. Questions here are deliberately generic to the mechanism itself; a project-specific angle
(such as configuring ratings on a project stage) belongs to the `project` bank, not here.

Question text is source-neutral. It does not name the module, any vendor or product, or any
technical identifier (field, model, method, XML ID, API path).

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because each tests a distinct material hypothesis, spread across
  the required dimensions (business capability, business rule, state transition, configuration
  dependency, role and permission, exception path, cancellation, reversal, negative case,
  cross-module dependency, optional behaviour, auditability, tenant/company boundary, concurrency
  and ordering, runtime reachability, configuration reachability).
- Questions are not evidence. A later ANSWERED state requires an actual artifact.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This document is PREPARED ONLY. It is not approved, not frozen, not MASTER-ready.

## G12-PORTAL_RATING-Q001

```yaml
QID: G12-PORTAL_RATING-Q001
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A rating access link grants visibility and submission rights scoped only to the single specific
  record it was generated for, not to any other record belonging to the same external party.
WHY_IT_MATTERS: >
  A link that leaks scope beyond its own record would let one external party see or influence
  ratings on records that are not theirs.
DISCONFIRMING_OBSERVATION: >
  A rating link generated for one record allows viewing or submitting a rating for a different
  record belonging to the same or a different external party.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Generate a rating link for one record and attempt to use it to reach or affect a different record.
```

## G12-PORTAL_RATING-Q002

```yaml
QID: G12-PORTAL_RATING-Q002
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rating access token cannot be reused to submit a second, different rating for the same event
  once a rating has already been submitted through it.
WHY_IT_MATTERS: >
  A reusable token allows the rated party, or anyone with the link, to overwrite an inconvenient
  rating with a more favourable one after the fact.
DISCONFIRMING_OBSERVATION: >
  The same rating token, after already being used to submit a rating, can be used again to submit a
  different rating value for the same event.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit a rating through a token, then attempt to submit a different rating using the same token.
```

## G12-PORTAL_RATING-Q003

```yaml
QID: G12-PORTAL_RATING-Q003
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rating token is not guessable or predictable from another token already known, such as by
  incrementing or pattern-matching a visible identifier.
WHY_IT_MATTERS: >
  A predictable token turns the entire rating mechanism into an open door for anyone who obtains one
  legitimate link.
DISCONFIRMING_OBSERVATION: >
  A valid rating token for a different record can be derived or guessed from a known token through an
  observable pattern.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Obtain two legitimate rating tokens for different records and inspect them for any derivable
  pattern.
```

## G12-PORTAL_RATING-Q004

```yaml
QID: G12-PORTAL_RATING-Q004
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating token, once expired or after the record it targets has moved past the point where a rating
  is relevant, no longer allows a new rating to be submitted through it.
WHY_IT_MATTERS: >
  A token that remains usable indefinitely lets a rating be submitted long after the interaction it
  is meant to reflect, undermining the rating's relevance.
DISCONFIRMING_OBSERVATION: >
  A rating token remains usable to submit a new rating well after its expected validity window has
  passed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Wait until a rating token's expected validity window has passed and attempt to submit a rating
  through it.
```

## G12-PORTAL_RATING-Q005

```yaml
QID: G12-PORTAL_RATING-Q005
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Once a rating has been submitted for a given event, the same recipient is not sent a further,
  duplicate rating request for that identical event.
WHY_IT_MATTERS: >
  Repeated requests for feedback already given train recipients to ignore the requests entirely,
  degrading response rates for every future request.
DISCONFIRMING_OBSERVATION: >
  A recipient who has already rated a specific event receives a further rating request for that same
  event.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Submit a rating for an event and check whether any further rating request for that same event is
  sent.
```

## G12-PORTAL_RATING-Q006

```yaml
QID: G12-PORTAL_RATING-Q006
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An average or aggregate satisfaction score computed for a parent record reflects exactly the set of
  ratings actually submitted for it, with no submitted rating silently excluded and no rating counted
  more than once.
WHY_IT_MATTERS: >
  An aggregate score that does not match its own underlying ratings misrepresents satisfaction to
  anyone relying on the summary figure.
DISCONFIRMING_OBSERVATION: >
  The displayed average disagrees with a manual average computed from the individual submitted
  ratings for the same record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Submit several ratings for the same record and compare the displayed average against a manual
  calculation.
```

## G12-PORTAL_RATING-Q007

```yaml
QID: G12-PORTAL_RATING-Q007
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting the parent record a rating was submitted for either preserves the rating as a standalone
  historical record or removes it explicitly, but does not leave an orphaned rating silently still
  counted in aggregate figures with no parent to attribute it to.
WHY_IT_MATTERS: >
  An orphaned rating still counted in totals distorts aggregate satisfaction figures with a data
  point nobody can trace back to what it was actually about.
DISCONFIRMING_OBSERVATION: >
  After the parent record is deleted, its rating remains counted in an aggregate figure with no
  traceable link to any parent.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Submit a rating for a record, delete the parent record, and inspect whether the rating is still
  counted anywhere and whether it remains traceable.
```

## G12-PORTAL_RATING-Q008

```yaml
QID: G12-PORTAL_RATING-Q008
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The rating scale (its number of points and their meaning) presented to an external party is
  consistent for a given parent record type across every occasion a rating request is generated for
  that type, not silently varying between requests.
WHY_IT_MATTERS: >
  A scale that changes silently between requests makes ratings incomparable across time even for the
  same kind of interaction.
DISCONFIRMING_OBSERVATION: >
  Two rating requests generated for the same parent record type at different times present different
  scales with no configuration change explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Generate two rating requests for the same parent record type at different times and compare the
  presented scale.
```

## G12-PORTAL_RATING-Q009

```yaml
QID: G12-PORTAL_RATING-Q009
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Free-text feedback submitted alongside a rating is not published or surfaced to any audience beyond
  its intended internal reviewers without a defined moderation or approval step.
WHY_IT_MATTERS: >
  Unmoderated free-text feedback published automatically can expose defamatory, confidential, or
  simply inaccurate content with no review.
DISCONFIRMING_OBSERVATION: >
  Free-text feedback submitted with a rating becomes visible beyond its intended internal reviewers
  with no moderation step having occurred.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Submit a rating with free-text feedback and check what becomes visible to whom before any explicit
  moderation action.
```

## G12-PORTAL_RATING-Q010

```yaml
QID: G12-PORTAL_RATING-Q010
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A submitted rating value is validated against the defined scale at submission time; a value outside
  the valid range is rejected rather than stored as-is.
WHY_IT_MATTERS: >
  An out-of-range value silently stored corrupts every aggregate calculation that assumes ratings
  fall within the defined scale.
DISCONFIRMING_OBSERVATION: >
  A rating value outside the defined scale is accepted and stored without rejection.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to submit a rating value outside the defined valid range through the available submission
  path.
```

## G12-PORTAL_RATING-Q011

```yaml
QID: G12-PORTAL_RATING-Q011
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Ratings and their associated identifying information are scoped to the company that owns the
  parent record in a multi-company environment; a user restricted to one company cannot see ratings
  belonging to a different company's records.
WHY_IT_MATTERS: >
  Ratings often carry named feedback about specific interactions; leaking them across company
  boundaries exposes commercially sensitive customer feedback outside its intended scope.
DISCONFIRMING_OBSERVATION: >
  A user restricted to one company can view a rating, or its identifying detail, belonging to a
  record scoped to a different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create ratings against records scoped to two different companies and attempt cross-company access
  as a single-company user.
```

## G12-PORTAL_RATING-Q012

```yaml
QID: G12-PORTAL_RATING-Q012
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A person can decline or opt out of receiving further rating requests, and that preference is
  actually honoured for subsequent requests rather than only cosmetically acknowledged.
WHY_IT_MATTERS: >
  An opt-out that is not honoured continues to contact someone who explicitly asked to stop, which is
  both a trust and a compliance concern.
DISCONFIRMING_OBSERVATION: >
  A person who opted out of rating requests receives a further request afterward.
EXPECTED_SURFACE: S3,S7,S8
PRECONDITIONS: >
  Where an opt-out exists, exercise it and then trigger a further event that would normally generate
  a rating request.
```

## G12-PORTAL_RATING-Q013

```yaml
QID: G12-PORTAL_RATING-Q013
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An internal user (not an external customer) triggering the same event a rating request is normally
  tied to does not itself receive an external-style rating request, since the mechanism is intended
  for external parties.
WHY_IT_MATTERS: >
  Internal users receiving external-style rating requests pollutes rating data with entries that do
  not represent genuine external customer sentiment.
DISCONFIRMING_OBSERVATION: >
  An internal user triggering the same event type receives a rating request identical to what an
  external customer would receive.
EXPECTED_SURFACE: S3,S7,S8
PRECONDITIONS: >
  Trigger a rating-generating event as an internal user rather than an external customer, and check
  whether a rating request is generated for them.
```

## G12-PORTAL_RATING-Q014

```yaml
QID: G12-PORTAL_RATING-Q014
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A parent record that transitions through the same rating-triggering state more than once (for
  example, reopened and closed again) generates a new, distinct rating opportunity each time, rather
  than being permanently limited to only the first occurrence.
WHY_IT_MATTERS: >
  If only the first transition can ever be rated, feedback specifically about a later, possibly worse
  handling of the same record is permanently lost.
DISCONFIRMING_OBSERVATION: >
  A record that re-enters the rating-triggering state a second time does not generate any new rating
  opportunity, even though the first opportunity was already used.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Move a record through the rating-triggering state, then reopen it and move it through that state
  again, checking for a new rating opportunity.
```

## G12-PORTAL_RATING-Q015

```yaml
QID: G12-PORTAL_RATING-Q015
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An aggregate satisfaction score is not displayed as meaningful, or is shown with an explicit
  low-sample caveat, when the number of underlying ratings is too small to be statistically
  meaningful.
WHY_IT_MATTERS: >
  A single rating presented with the same confidence as an average of hundreds misleads anyone using
  the score to judge overall performance.
DISCONFIRMING_OBSERVATION: >
  An aggregate score based on a single rating, or a very small number, is displayed identically to one
  based on a large, statistically meaningful sample, with no distinguishing caveat.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Compare the display of an aggregate score based on one rating against one based on many ratings for
  a comparable record type.
```

## G12-PORTAL_RATING-Q016

```yaml
QID: G12-PORTAL_RATING-Q016
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A failure to deliver a rating request (an email bounce or similar delivery failure) is recorded and
  distinguishable from a request that was delivered but never answered.
WHY_IT_MATTERS: >
  Treating a bounced request the same as an ignored one hides a delivery problem that could be
  silently suppressing response rates for reasons unrelated to actual customer engagement.
DISCONFIRMING_OBSERVATION: >
  A rating request that failed to deliver shows the same status as one that delivered successfully
  but received no response.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Trigger a rating request to an address known to bounce and compare its resulting status to a
  successfully delivered but unanswered request.
```

## G12-PORTAL_RATING-Q017

```yaml
QID: G12-PORTAL_RATING-Q017
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Resending a rating request for the same event, where explicitly permitted, either invalidates the
  earlier token or clearly manages the relationship between old and new tokens, rather than leaving
  multiple simultaneously valid tokens for the identical rating opportunity with no defined
  relationship.
WHY_IT_MATTERS: >
  Multiple live tokens for the same opportunity, with no relationship defined, create ambiguity about
  which one governs if both are eventually used.
DISCONFIRMING_OBSERVATION: >
  After a rating request is resent, both the original and the new token remain independently valid
  with no defined relationship or precedence between them.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Where resending a rating request is possible, resend it and check the validity and relationship of
  the original and new tokens.
```

## G12-PORTAL_RATING-Q018

```yaml
QID: G12-PORTAL_RATING-Q018
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rating value that would trigger an internal escalation (a low score against a configured
  threshold) actually generates the escalation notification, and does not silently sit unnoticed
  because it was submitted through an unusual path, such as a resent request or an integration.
WHY_IT_MATTERS: >
  A low rating is often the single most actionable piece of feedback the system captures; silently
  missing the escalation defeats the entire purpose of collecting the rating.
DISCONFIRMING_OBSERVATION: >
  A rating below the configured escalation threshold, submitted through a non-default path, does not
  trigger the escalation notification that the same score submitted through the default path would.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Configure an escalation threshold, submit a below-threshold rating through both the default and a
  non-default path, and compare escalation outcomes.
```

## G12-PORTAL_RATING-Q019

```yaml
QID: G12-PORTAL_RATING-Q019
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A satisfaction trend calculation over time (such as week-over-week or month-over-month change) uses
  a consistent, documented method for grouping ratings by period, rather than an undocumented method
  that can silently shift which ratings fall into which period.
WHY_IT_MATTERS: >
  An undocumented, inconsistent period-grouping method makes a reported trend impossible to verify or
  reproduce independently.
DISCONFIRMING_OBSERVATION: >
  Recomputing a reported trend from the underlying individual ratings, using the stated period
  boundaries, does not reproduce the displayed trend figures.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Take a displayed trend figure and attempt to reproduce it manually from the underlying individual
  ratings and stated period boundaries.
```

## G12-PORTAL_RATING-Q020

```yaml
QID: G12-PORTAL_RATING-Q020
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk export of ratings for external handling masks or omits any directly identifying detail about
  the person who submitted each rating by default, unless identification is explicitly required for
  the export's purpose.
WHY_IT_MATTERS: >
  A routine export of satisfaction data should not casually carry identifying detail about the
  individuals who provided it beyond what the export actually needs.
DISCONFIRMING_OBSERVATION: >
  A standard ratings export includes directly identifying detail about each respondent by default
  with no explicit requirement driving that inclusion.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Produce a standard export of ratings and inspect whether identifying respondent detail is included
  by default.
```

## G12-PORTAL_RATING-Q021

```yaml
QID: G12-PORTAL_RATING-Q021
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating page reached through an expired or already-used token displays a clear, distinct message
  explaining why the rating cannot be submitted, rather than a generic error indistinguishable from
  an unrelated system failure.
WHY_IT_MATTERS: >
  A generic error on an expired token leaves the external party unsure whether the problem is on
  their end, and unable to tell whether their original rating was actually recorded.
DISCONFIRMING_OBSERVATION: >
  Accessing an expired or already-used rating link produces the same generic error as an unrelated
  system failure, with no explanation of the actual cause.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Access a rating link after it has expired or already been used, and inspect the resulting message.
```

## G12-PORTAL_RATING-Q022

```yaml
QID: G12-PORTAL_RATING-Q022
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating request is sent in a language consistent with the recipient's known language preference,
  where such a preference is recorded, rather than defaulting to a single fixed language regardless
  of who is being asked.
WHY_IT_MATTERS: >
  A rating request in the wrong language for the recipient reduces response rates and can make the
  scale itself harder to interpret correctly.
DISCONFIRMING_OBSERVATION: >
  A rating request sent to a recipient with a recorded language preference arrives in a different
  language with no override explaining the mismatch.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Set a recipient's language preference and trigger a rating request, then inspect the language it
  arrives in.
```

## G12-PORTAL_RATING-Q023

```yaml
QID: G12-PORTAL_RATING-Q023
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rating record cannot be edited by the rated party (the internal team or individual whose
  performance the rating reflects) after submission, only by the original external respondent within
  whatever edit window is defined, or by an internal reviewer through an explicit, traceable
  moderation action.
WHY_IT_MATTERS: >
  A rated party able to quietly edit their own rating after the fact defeats the entire purpose of
  collecting independent external feedback.
DISCONFIRMING_OBSERVATION: >
  The rated party is able to directly change a submitted rating's value with no distinct, traceable
  moderation action recorded.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  As the rated party, attempt to directly change the value of a rating already submitted about their
  own performance.
```

## G12-PORTAL_RATING-Q024

```yaml
QID: G12-PORTAL_RATING-Q024
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a respondent is allowed to revise their own rating within a defined edit window, doing so
  updates the aggregate score to reflect the revised value rather than counting both the original and
  the revised value in the aggregate.
WHY_IT_MATTERS: >
  Counting both an original and a revised rating from the same person double-counts one respondent's
  opinion in the aggregate.
DISCONFIRMING_OBSERVATION: >
  After a respondent revises their rating within the edit window, the aggregate reflects both the
  original and the revised value rather than only the current one.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Submit a rating, revise it within the permitted edit window, and inspect the aggregate before and
  after.
```

## G12-PORTAL_RATING-Q025

```yaml
QID: G12-PORTAL_RATING-Q025
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A rating's recorded submission timestamp reflects when the respondent actually submitted it, not
  when the request was originally generated or sent.
WHY_IT_MATTERS: >
  Conflating request time with submission time misrepresents how quickly, or how long after the
  interaction, a respondent actually gave their feedback.
DISCONFIRMING_OBSERVATION: >
  A rating's recorded timestamp matches when the request was generated rather than when the
  respondent actually submitted the rating.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a rating request, wait a meaningful interval, then submit the rating, and inspect its
  recorded timestamp.
```

## G12-PORTAL_RATING-Q026

```yaml
QID: G12-PORTAL_RATING-Q026
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rating submitted anonymously, where an anonymous option is offered, does not still carry a
  recoverable link to the respondent's identity accessible through some other view or export.
WHY_IT_MATTERS: >
  An anonymity option that is not actually anonymous misleads the respondent about the privacy of
  their feedback at the moment they decide how honestly to answer.
DISCONFIRMING_OBSERVATION: >
  A rating submitted with the anonymous option selected can still be traced back to the respondent
  through some other available view or export.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Where an anonymous submission option exists, submit a rating anonymously and attempt to trace it
  back to the respondent through any available means.
```

## G12-PORTAL_RATING-Q027

```yaml
QID: G12-PORTAL_RATING-Q027
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating widget embedded on a public-facing page presents only the information intended for public
  display (such as an aggregate score) and not internal detail such as respondent identity or
  free-text feedback awaiting moderation.
WHY_IT_MATTERS: >
  A public embed that leaks unmoderated or identifying content exposes it far beyond any access
  control the system otherwise enforces.
DISCONFIRMING_OBSERVATION: >
  A public-facing rating widget exposes respondent identity or unmoderated free-text content beyond
  the intended aggregate display.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Inspect a public-facing rating widget's actual output against what internal detail exists behind
  it.
```

## G12-PORTAL_RATING-Q028

```yaml
QID: G12-PORTAL_RATING-Q028
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a rating request is generated at all for a given event is governed by an explicit,
  discoverable configuration per parent record type, rather than every type behaving identically by
  an undocumented default.
WHY_IT_MATTERS: >
  An undocumented default that silently differs between record types produces unpredictable customer
  contact that nobody explicitly decided on.
DISCONFIRMING_OBSERVATION: >
  Two different parent record types produce different rating-request behaviour with no discoverable
  configuration explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare rating-request generation behaviour across two different parent record types and look for
  the governing configuration.
```

## G12-PORTAL_RATING-Q029

```yaml
QID: G12-PORTAL_RATING-Q029
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating value contributes to only the specific parent record's own aggregate and does not bleed
  into the aggregate of an unrelated record merely because both share the same respondent or the same
  general category.
WHY_IT_MATTERS: >
  Cross-contamination of aggregates between unrelated records would misattribute one interaction's
  outcome to another that had nothing to do with it.
DISCONFIRMING_OBSERVATION: >
  Submitting a rating for one record measurably changes the aggregate score of a different,
  unrelated record.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Note the aggregate score of an unrelated record, submit a rating for a different record by the same
  respondent, and check whether the unrelated record's aggregate changed.
```

## G12-PORTAL_RATING-Q030

```yaml
QID: G12-PORTAL_RATING-Q030
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Submitting a rating through an automated or scripted request at a rate far exceeding plausible human
  interaction is detected or throttled rather than being accepted identically to genuine, isolated
  human submissions.
WHY_IT_MATTERS: >
  An unthrottled submission path is an easy way to flood an aggregate score with fabricated ratings
  in either direction.
DISCONFIRMING_OBSERVATION: >
  A large number of rating submissions in rapid succession from the same source are all accepted with
  no detection or throttling.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit a rapid sequence of rating submissions from the same source and observe whether any are
  detected or throttled.
```

## G12-PORTAL_RATING-Q031

```yaml
QID: G12-PORTAL_RATING-Q031
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating request generated through an integration or automated feed follows the same token-scope
  and expiry rules as one generated through the primary interactive path.
WHY_IT_MATTERS: >
  A weaker integration-generated token would provide an easier route to a broadly scoped or
  long-lived access point than the interactive path allows.
DISCONFIRMING_OBSERVATION: >
  A rating token generated through an integration carries broader scope or a longer validity window
  than an equivalent token generated interactively.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Generate a rating request through an integration path and compare its token's scope and expiry to
  one generated interactively.
```

## G12-PORTAL_RATING-Q032

```yaml
QID: G12-PORTAL_RATING-Q032
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Archiving or deactivating the internal user or team associated with a rated record does not alter
  or hide the historical ratings already recorded against records they were responsible for.
WHY_IT_MATTERS: >
  Historical performance feedback should not disappear or misattribute simply because the person or
  team involved is no longer active.
DISCONFIRMING_OBSERVATION: >
  Deactivating the internal party associated with a rated record causes the historical rating to
  disappear or lose its attribution.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Record a rating tied to an internal party, deactivate that party, and inspect the rating's
  historical attribution afterward.
```

## G12-PORTAL_RATING-Q033

```yaml
QID: G12-PORTAL_RATING-Q033
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two concurrent submission attempts through the same rating token — such as a double-click or a
  retried network request — result in exactly one rating being recorded, not two.
WHY_IT_MATTERS: >
  A duplicate submission from an ordinary double-click would inflate an aggregate with a single
  respondent's opinion counted twice.
DISCONFIRMING_OBSERVATION: >
  Submitting the same rating token's form twice in quick succession records two separate ratings
  rather than one.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit a rating through the same token twice in quick succession and check how many ratings are
  recorded.
```

## G12-PORTAL_RATING-Q034

```yaml
QID: G12-PORTAL_RATING-Q034
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Data captured through the rating mechanism under a test or non-production configuration is not
  reachable by, or counted in, live production aggregate scores under any shared-data condition.
WHY_IT_MATTERS: >
  Test ratings leaking into production aggregates would silently distort a genuine satisfaction
  metric with fabricated test data.
DISCONFIRMING_OBSERVATION: >
  A rating submitted under a test configuration appears in or affects a live production aggregate
  score.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Where a test/sandbox configuration exists, submit a rating there and check for leakage into
  production aggregates.
```

## G12-PORTAL_RATING-Q035

```yaml
QID: G12-PORTAL_RATING-Q035
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Accessing the rating submission page does not, by itself before any rating is actually submitted,
  reveal any information about the parent record beyond what is needed to present the rating request
  itself.
WHY_IT_MATTERS: >
  A rating page is reachable by anyone holding the link; leaking parent-record detail on that page
  before submission widens exposure well past the rating mechanism's intended purpose.
DISCONFIRMING_OBSERVATION: >
  Loading the rating page, without submitting anything, reveals detail about the parent record beyond
  what the rating request itself needs to display.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Load a rating page from a valid link without submitting a rating, and inspect exactly what
  information is exposed.
```

## G12-PORTAL_RATING-Q036

```yaml
QID: G12-PORTAL_RATING-Q036
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating request configured for a parent record type applies consistently to every record of that
  type across every company in a multi-company environment, rather than silently applying to only
  some companies with no discoverable reason.
WHY_IT_MATTERS: >
  An inconsistently applied configuration across companies produces unpredictable customer contact
  that nobody explicitly scoped that way.
DISCONFIRMING_OBSERVATION: >
  The same rating-request configuration for a record type is honoured in one company and silently
  ignored in another with no discoverable per-company override explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a rating request for a record type and compare its behaviour for equivalent records
  under two different companies.
```

## G12-PORTAL_RATING-Q037

```yaml
QID: G12-PORTAL_RATING-Q037
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A rating record, once submitted, retains a reference to which specific parent-record state
  transition it was requested for, so a record rated multiple times over its life (once per relevant
  transition) can be broken down transition by transition rather than blended into one
  undifferentiated total.
WHY_IT_MATTERS: >
  Blending ratings from different stages of a record's life into one figure hides whether an issue
  happened early or late in the process.
DISCONFIRMING_OBSERVATION: >
  A record rated at more than one distinct stage of its life shows only a single blended figure with
  no way to break it down by which stage each rating was actually about.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate ratings for the same record at two distinct stages of its life and check whether they can
  be distinguished afterward.
```

## G12-PORTAL_RATING-Q038

```yaml
QID: G12-PORTAL_RATING-Q038
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A change to the rating scale's configuration (such as widening or narrowing the number of points)
  does not retroactively remap or reinterpret ratings that were already submitted under the previous
  scale.
WHY_IT_MATTERS: >
  Retroactively remapping historical ratings to a new scale silently changes what a respondent is
  understood to have actually said.
DISCONFIRMING_OBSERVATION: >
  Changing the rating scale's configuration causes previously submitted ratings to display a
  different value than what was originally recorded under the old scale.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit ratings under one scale configuration, change the scale configuration, and re-inspect the
  earlier ratings.
```

## G12-PORTAL_RATING-Q039

```yaml
QID: G12-PORTAL_RATING-Q039
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Filtering or searching ratings by score, date range, or parent record type returns a result
  consistent with the same criteria applied manually against the full set of ratings.
WHY_IT_MATTERS: >
  A filter that silently disagrees with a manual check undermines confidence in every filtered report
  produced from the same underlying data.
DISCONFIRMING_OBSERVATION: >
  A filtered view of ratings omits or includes ratings that a manual check of the same criteria
  against the full set would not.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Apply a filter to the ratings list and compare its result against a manual check of the same
  criteria.
```

## G12-PORTAL_RATING-Q040

```yaml
QID: G12-PORTAL_RATING-Q040
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Deleting a rating outright is distinguishable in the audit trail from a rating that was never
  submitted, so a reviewer can tell that a rating was actually removed rather than simply never given.
WHY_IT_MATTERS: >
  An undetectable rating deletion is indistinguishable from a respondent who never rated at all,
  defeating any audit of removed feedback, including feedback removed to hide an unfavourable score.
DISCONFIRMING_OBSERVATION: >
  Deleting a rating leaves no trace distinguishing that record's history from one that simply never
  received a rating.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit and then delete a rating, and inspect whether any trace of its prior existence remains
  auditable.
```

## G12-PORTAL_RATING-Q041

```yaml
QID: G12-PORTAL_RATING-Q041
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating submission does not require the respondent to authenticate as a registered portal user;
  where anonymous, token-based access is the intended design, an unauthenticated submission is
  accepted on the same terms rather than silently blocked pending a login the design never intended
  to require.
WHY_IT_MATTERS: >
  A mechanism designed for frictionless, unauthenticated feedback that silently starts demanding
  login would suppress response rates without anyone deciding to add that requirement.
DISCONFIRMING_OBSERVATION: >
  A rating submission through a valid token is blocked or redirected to a login requirement that the
  mechanism's intended design does not call for.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt to submit a rating through a valid token without any portal authentication.
```

## G12-PORTAL_RATING-Q042

```yaml
QID: G12-PORTAL_RATING-Q042
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A rating shown on an internal dashboard reflects the same underlying value as the same rating shown
  on the record's own detail view, rather than the two surfaces disagreeing about what was actually
  submitted.
WHY_IT_MATTERS: >
  A dashboard figure that disagrees with the record's own detail undermines trust in whichever view a
  manager happens to be using.
DISCONFIRMING_OBSERVATION: >
  The same rating's value differs between an internal dashboard view and the record's own detail
  view.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Submit a rating and compare its value on an internal dashboard against the record's own detail
  view.
```

## G12-PORTAL_RATING-Q043

```yaml
QID: G12-PORTAL_RATING-Q043
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rating submitted through a link that has already been forwarded or shared beyond the intended
  original recipient does not silently attribute the resulting rating to the original recipient's
  identity as though they personally submitted it.
WHY_IT_MATTERS: >
  Misattributing a forwarded submission to the original recipient could unfairly credit or blame the
  wrong person for feedback they never actually gave.
DISCONFIRMING_OBSERVATION: >
  A rating submitted by someone other than the original recipient, through a forwarded link, is
  attributed identically to the original recipient with no distinction.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Forward a rating link to someone other than the original recipient, have them submit a rating, and
  inspect who the rating is attributed to.
```

## G12-PORTAL_RATING-Q044

```yaml
QID: G12-PORTAL_RATING-Q044
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating value can be submitted with an accompanying free-text comment even when the numeric value
  itself is at either extreme of the scale, without the system silently discarding the comment for
  extreme values.
WHY_IT_MATTERS: >
  Extreme ratings are usually the ones with the most valuable accompanying explanation; losing the
  comment specifically at the extremes discards the most actionable feedback.
DISCONFIRMING_OBSERVATION: >
  Submitting a rating at either extreme of the scale along with a comment results in the comment
  being dropped while a comment on a mid-scale rating is retained.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit a rating at each extreme of the scale with an accompanying comment, and inspect whether the
  comment is retained.
```

## G12-PORTAL_RATING-Q045

```yaml
QID: G12-PORTAL_RATING-Q045
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a rating is required or merely optional for a given interaction is an explicit,
  discoverable configuration, not an undocumented default that behaves inconsistently between
  otherwise similar record types.
WHY_IT_MATTERS: >
  An undocumented, inconsistent requirement makes it unclear whether a missing rating for a given
  record reflects a deliberate choice or an unexplained gap.
DISCONFIRMING_OBSERVATION: >
  Two otherwise similar record types differ in whether a rating is required to proceed, with no
  discoverable configuration explaining the difference.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Compare whether a rating is enforced as required across two otherwise similar record types and look
  for the governing configuration.
```

## G12-PORTAL_RATING-Q046

```yaml
QID: G12-PORTAL_RATING-Q046
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A bulk moderation action affecting many pending free-text comments in one operation produces a
  per-comment trace of what was approved, rejected, or edited, not a single undifferentiated
  bulk-action log line.
WHY_IT_MATTERS: >
  A single generic log line for a bulk moderation action makes it impossible to review which specific
  comments were approved, rejected, or altered.
DISCONFIRMING_OBSERVATION: >
  A bulk moderation action across several pending comments produces one generic log entry with no way
  to see which specific comments were affected or how.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Perform a bulk moderation action across several pending comments and inspect the resulting trace.
```

## G12-PORTAL_RATING-Q047

```yaml
QID: G12-PORTAL_RATING-Q047
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The full lifecycle of a rating — the request being generated, sent, opened, submitted, and any
  subsequent moderation or escalation — can be reconstructed end to end from stored records alone,
  without relying on anyone's recollection.
WHY_IT_MATTERS: >
  If the lifecycle of a disputed or escalated rating cannot be reconstructed from records, an
  internal dispute over what was actually said and when has no way to be settled on evidence alone.
DISCONFIRMING_OBSERVATION: >
  The full lifecycle of a rating that went through request, submission, and escalation cannot be
  fully reconstructed from stored records alone.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Take a rating through request, submission, and escalation, then attempt to reconstruct the full
  timeline using only stored records.
```

## G12-PORTAL_RATING-Q048

```yaml
QID: G12-PORTAL_RATING-Q048
MODULE: portal_rating
TYPE: MODULE
AUTHOR: P12-1
RISK_TIER: LOW
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A rating request template's content (wording, branding, scale labels) can be customised per parent
  record type without that customisation affecting the stored, comparable numeric scale used for
  aggregation across types.
WHY_IT_MATTERS: >
  If customising the wording for one record type silently changes the underlying numeric scale, scores
  across different record types stop being comparable without anyone intending that.
DISCONFIRMING_OBSERVATION: >
  Customising a rating request template's wording for one record type changes the underlying stored
  numeric scale in a way that breaks comparability with other record types.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Customise a rating request template's wording for one record type and verify the underlying
  numeric scale remains consistent with other record types.
```
