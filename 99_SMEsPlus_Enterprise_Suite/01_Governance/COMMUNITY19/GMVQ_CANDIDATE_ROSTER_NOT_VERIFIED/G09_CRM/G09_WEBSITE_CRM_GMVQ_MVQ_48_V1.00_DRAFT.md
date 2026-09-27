# SMEsPlus ENTERPRISE SUITE
## GMVQ — G09 CRM / website_crm Module Adversarial MVQ Bank

**Document ID:** GMVQ-G09-WEBSITE_CRM-MVQ48-V1.00
**Group:** G09 CRM
**Module Metadata:** `website_crm`
**Wave:** W2
**Author Cell:** P-C5 (GMVQ Question Factory — Production Team 25, Acceleration Cell 5)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose

`website_crm` is a BRIDGE module (GMVQ_BRIDGE_MODULE_RULE_V1.00): it joins the public-facing website to the
internal pipeline. Its seam is a public web form creating an opportunity. Per the Bridge Module Rule, every
question below was tested against "if this capability were removed and the public site and the internal
pipeline were used entirely apart, would the question still make sense?" A YES belongs to the base `crm` bank,
not here. This bank does not re-ask how an opportunity moves through pipeline stages, how it is won, lost, or
merged in general, how staff reassign an existing opportunity, or how field-level change logs work generally —
that is `crm`'s ground and it is already authored. Every question below is a NO: it fails only where an
unauthenticated, unvetted submission from the open internet becomes, or attempts to become, an internal
business record.

## Control

- Mandatory pre-authoring sibling check performed: `grep -h 'HYPOTHESIS' "$PKG/01_QUESTION_BANKS/G09_CRM/"*.md |
  sort` was run before finalizing this bank. Four sibling files existed on disk at authoring time: the BASE
  `crm` bank (`G09_CRM_GMVQ_MVQ_66_V1.00_DRAFT.md`, 67 hypotheses), `crm_iap_enrich` (50 hypotheses),
  `crm_iap_mine` (in progress, 26 hypotheses so far), and `website_crm_partner_assign` (53 hypotheses). All were
  read in full before this bank was finalized.
  - The base `crm` bank already owns: inbound-interest-to-opportunity conversion and its duplicate/merge
    handling regardless of source, pipeline stage/probability/forecast-rollup integrity, staff-initiated
    reassignment and automatic-assignment-rule permission and configuration, won/lost and reopening, activity
    lifecycle, company/team viewing scope for existing records, field-level change-attribution logging in
    general, and erasure/consent handling for personal data attached to an opportunity in general. An earlier
    working draft of this bank asked several questions that were, on inspection against that list, the base
    bank's own ground with "the web form" substituted in as the noun — generic duplicate detection against an
    existing customer or another open interest, a merge preserving history, and a staff correction to a field
    being attributed distinctly from a prior value. Those were cut. What remains asks only about what is
    different because the *public, unauthenticated web channel specifically* is the origin: matching quality at
    the verified-versus-unverified boundary, deliberate adversarial evasion of duplicate/spam handling at
    volume, the trust boundary between externally-supplied and internally-entered content, verifying an erasure
    requester who was never authenticated in the first place, and the intake channel's own configuration,
    availability, reachability, and validation — none of which the base bank's source-agnostic abstraction (an
    "inbound interest") has any occasion to ask about.
  - `website_crm_partner_assign` owns routing a web-sourced opportunity onward to an *external partner company*
    and everything about what that partner can see, do, and retain. This bank's multi-company questions
    (Q022-Q024) are about which of the business's *own* companies or brands a submission belongs to at the
    moment of intake — a different, upstream boundary — and do not overlap.
  - `crm_iap_enrich` and `crm_iap_mine` were read for awareness of the group's other bridge banks; neither
    touches the public form itself, and no overlap was found or expected.
- Every question carries a concrete `DISCONFIRMING_OBSERVATION` that would prove its `HYPOTHESIS` wrong, and no
  two questions share one failure event.
- No padding: 48 questions test 48 distinct material hypotheses at the seam, spread across the Group Brief's
  named ground (validation divergence, forbidden-state reachability, duplication, required-field bypass,
  injected content, volumetric abuse, form-definition drift, multi-company routing, privacy notice versus
  actual practice, erasure, public attachments, premature acknowledgment, audit distinguishability), across the
  Bridge Module Rule's seam dimensions (ordering, partiality, ownership, timing, reversal, lifecycle mismatch,
  error asymmetry, authority), and across the Authoring Standard's dimension list — including four questions
  (Q045-Q048) added specifically to cover dimensions the first draft under-served: whether the intake endpoint
  can be reached at all other than through the real rendered page, whether the visitor's own site-language
  context survives to the response they receive, whether browser-supplied attribution data is treated as
  verified fact downstream, and whether a visitor's own stated service preference is actually used by
  assignment.
- Clean-room compliance: no vendor or product name, no technical identifier (field, table, method, XML ID, API
  path), and the module's own metadata name appears in the `MODULE:` field only. Question text refers to "the
  public web form," "the internal form," "the pipeline record," and "the submitting visitor."
- This module carries one layer at the seam; the `LAYER` field is omitted throughout.
- This bank is DRAFT question content only. Not approved, not frozen, not verified. `MODULE + QID` is a Research
  Evidence Join Key only; no Formal Coverage is derived from this bank. Lane A / Lane B: NOT STARTED for this
  module until rolling batch freeze is recorded.
- Coverage map: validation divergence Q001-Q004 · forbidden starting state Q005 · ownership/forecast-value
  injection via the unauthenticated channel Q006-Q007 · duplicate-handling quality at the public/unverified
  boundary Q008-Q009 · required-field bypass Q010-Q012 · injected/malformed content stored and rendered to staff
  Q013-Q015 · volumetric/automated abuse Q016-Q018 · form/routing configuration drift in flight Q019-Q021 ·
  multi-company site routing Q022-Q024 · stated privacy notice versus actual practice Q025-Q027 · erasure at the
  unauthenticated boundary Q028-Q030 · public attachments Q031-Q033 · premature acknowledgment Q034-Q036 ·
  origin trust-boundary and audit distinguishability Q037-Q038 · seam ordering, partiality, ownership-conflict,
  reversal, lifecycle mismatch and authority Q039-Q044 · intake-channel reachability and cross-context integrity
  Q045-Q048.

## G09-WEBSITE_CRM-Q001

```yaml
QID: G09-WEBSITE_CRM-Q001
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A value that the internal form's validation would reject is also rejected, not silently stored, when it
  arrives through the public form.
WHY_IT_MATTERS: >
  Business rules are enforced once, at the point of entry; if the public path is not held to the same rule,
  downstream logic that assumes valid data quietly stops being safe to trust for records with this origin.
DISCONFIRMING_OBSERVATION: >
  A submission carrying a value the internal form refuses to save (a malformed value in a field with a defined
  format or allowed-value rule) is instead accepted and persisted as a normal record when submitted through the
  public form.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify a field with a defined format or allowed-value rule enforced by the internal form; submit that field
  with a rule-violating value through the public form; compare against attempting the same value on the
  internal form.
```

## G09-WEBSITE_CRM-Q002

```yaml
QID: G09-WEBSITE_CRM-Q002
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A field whose value is normalized when entered internally receives the same normalization when it arrives
  from the public form, so the same logical field does not end up holding two different shapes of data
  depending on origin.
WHY_IT_MATTERS: >
  If normalization is skipped on the public path, anything downstream that assumes one shape of data breaks for
  records with this origin specifically.
DISCONFIRMING_OBSERVATION: >
  A value submitted through the public form in a form the internal path would normalize or reject is stored
  verbatim, unnormalized, while the internal path continues to normalize the same field.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Identify a normalized field; submit an unnormalized but plausible value via the public form; inspect the
  stored value against what the internal form would have produced.
```

## G09-WEBSITE_CRM-Q003

```yaml
QID: G09-WEBSITE_CRM-Q003
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A size or length limit enforced on a field in the internal form is enforced identically on the public form, so
  the two paths cannot produce records the internal form's own limits forbid.
WHY_IT_MATTERS: >
  An oversized value accepted only through the public path can break internal displays, reports, or downstream
  integrations sized to the internal limit.
DISCONFIRMING_OBSERVATION: >
  A value exceeding the internal form's enforced length or size limit for a field is accepted and stored without
  truncation or rejection when submitted through the public form.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify a length- or size-limited field on the internal form; submit a value exceeding that limit through the
  public form; inspect the stored record.
```

## G09-WEBSITE_CRM-Q004

```yaml
QID: G09-WEBSITE_CRM-Q004
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A submission can only select among the choices the public form actually offered at the time it was rendered; a
  value outside that offered set is rejected rather than stored.
WHY_IT_MATTERS: >
  If the form only cosmetically restricts choices while the underlying record accepts anything, a submission can
  put the record into a configuration state no legitimate visitor path would ever produce.
DISCONFIRMING_OBSERVATION: >
  A submission carrying a value for a constrained-choice field that was not among the options rendered to the
  visitor is accepted and stored as though it were a valid choice.
EXPECTED_SURFACE: S1,S3,S5
PRECONDITIONS: >
  Render the public form and record the offered choice set for a constrained field; submit a value outside that
  set directly; inspect whether the record is created and with what value.
```

## G09-WEBSITE_CRM-Q005

```yaml
QID: G09-WEBSITE_CRM-Q005
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A record created from the public form always begins in the same starting stage and status that a legitimate
  new inbound interest begins in; no submission can select or force a later-stage or closed state.
WHY_IT_MATTERS: >
  An anonymous submitter choosing an advanced or closed state for their own record could inflate forecast
  figures, or short-circuit the qualification steps staff rely on before deciding to spend time on it.
DISCONFIRMING_OBSERVATION: >
  A record created through the public form is observed in a stage, status, or closed state other than the
  pipeline's defined starting state, with no staff action in between.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Submit the public form under normal conditions and inspect the created record's stage and status immediately
  after creation, before any staff member opens it.
```

## G09-WEBSITE_CRM-Q006

```yaml
QID: G09-WEBSITE_CRM-Q006
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A value present in the raw submission that the rendered public form never actually exposed as an editable
  field cannot itself determine who the resulting record is assigned to; assignment is driven only by the
  internal routing logic evaluating legitimate submission content.
WHY_IT_MATTERS: >
  An anonymous, unauthenticated request is the one input this pipeline processes with no human vouching for its
  shape; if a value the visitor's browser was never offered can still steer assignment, the assignment rule the
  business actually configured can be bypassed by anyone who inspects the request format rather than by anyone
  the rule was written for.
DISCONFIRMING_OBSERVATION: >
  A hidden or unexpected value included in a raw submission, beyond what the rendered form actually exposed to
  the visitor, results in the record being assigned to an owner other than whoever the internal routing logic
  would have chosen from the form's legitimate content alone.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Determine the owner the routing logic would assign from a submission's legitimate rendered content; submit the
  same content with an additional hidden or unexpected value hinting at a different owner; compare the resulting
  assignment.
```

## G09-WEBSITE_CRM-Q007

```yaml
QID: G09-WEBSITE_CRM-Q007
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A numeric value arriving in a raw public submission for a field the internal form treats as staff-only or as a
  computed default is not written into that field on the created record; whatever governs that field internally
  continues to govern it regardless of what an anonymous request supplied.
WHY_IT_MATTERS: >
  This is a different failure from an internal editing-integrity gap: here the very first value a
  forecast-relevant field ever holds can be dictated by an unauthenticated outside party before any internal
  control has had a chance to apply at all.
DISCONFIRMING_OBSERVATION: >
  A value supplied in the raw public submission for a field the internal form does not expose as visitor-editable
  appears unchanged on the created record, sourced directly from the anonymous request rather than from internal
  logic.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit the public form's underlying request supplying a value for a field the internal form does not expose as
  visitor-editable; inspect the created record for that field's source and value.
```

## G09-WEBSITE_CRM-Q008

```yaml
QID: G09-WEBSITE_CRM-Q008
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whatever duplicate-matching the pipeline applies to an inbound interest performs no worse against a submission
  arriving through the public form than against one entered by staff, even though the public submitter's details
  were never verified as staff would verify them while typing.
WHY_IT_MATTERS: >
  If matching quality silently degrades for the one channel nobody vouches for as it is entered, exactly the
  channel most exposed to typos and inconsistent self-reported detail gets the weakest protection against
  creating disconnected duplicate identities.
DISCONFIRMING_OBSERVATION: >
  A pair of submissions a staff member would recognize as the same underlying prospect, differing only in the
  kind of trivial variation typical of self-reported public data (an abbreviated company name, a personal rather
  than corporate email address, a differently formatted phone number), is treated as entirely unrelated when
  both arrive through the public form, though an equivalent pair entered by staff would be flagged.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Compare the pipeline's duplicate-matching outcome for a pair of trivially-varying-but-equivalent submissions
  made through the public form against the outcome for an equivalent pair entered directly by staff.
```

## G09-WEBSITE_CRM-Q009

```yaml
QID: G09-WEBSITE_CRM-Q009
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Duplicate and spam handling applied to public submissions is not defeated simply by an automated submitter
  varying a trivial, low-cost detail on each of many otherwise-identical submissions.
WHY_IT_MATTERS: >
  If trivial randomization defeats detection, the volumetric protections this bank also asks about (Q016-Q018)
  can be rendered moot by a script with almost no additional effort, since it never needs to submit two
  literally identical requests to flood the pipeline.
DISCONFIRMING_OBSERVATION: >
  A sequence of automated submissions, each varying only a trivial, low-cost detail from the last while the rest
  of the content stays identical, are all accepted as fully independent, unrelated records with no duplicate or
  spam signal raised.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Submit a series of automated submissions that vary only a trivial detail from each other; inspect whether
  duplicate or spam handling flags the pattern.
```

## G09-WEBSITE_CRM-Q010

```yaml
QID: G09-WEBSITE_CRM-Q010
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A submission omitting a field marked mandatory on the rendered public form is not accepted; the record is
  either not created, or is created only in a state clearly flagged as incomplete.
WHY_IT_MATTERS: >
  A "required" field that can be skipped is not actually enforced, and staff relying on its presence will find
  records missing exactly the information they were told would always be there.
DISCONFIRMING_OBSERVATION: >
  A submission omitting a field marked mandatory on the rendered form is accepted and the resulting record shows
  no indication that a required field is missing.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify a field marked mandatory on the rendered public form; submit the underlying request with that field
  omitted or empty; inspect whether the record is created and how the gap is represented.
```

## G09-WEBSITE_CRM-Q011

```yaml
QID: G09-WEBSITE_CRM-Q011
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A mandatory field cannot be satisfied by a value that is functionally empty, such as whitespace only; such a
  value is treated the same as omission.
WHY_IT_MATTERS: >
  If whitespace passes the mandatory check, the requirement is enforced in name only, and the same downstream
  problem occurs as an outright missing field.
DISCONFIRMING_OBSERVATION: >
  A submission with a mandatory field containing only whitespace or another functionally empty value is accepted
  as though the field were properly filled.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit the form with a mandatory field set to whitespace only; inspect whether the record is created and how
  the field is stored.
```

## G09-WEBSITE_CRM-Q012

```yaml
QID: G09-WEBSITE_CRM-Q012
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Any automated step that runs against a newly created record, such as a notification or routing decision,
  tolerates a missing value in a field it depends on, rather than failing in a way that silently drops the
  record from that step.
WHY_IT_MATTERS: >
  A record missing an expected field can fall out of notification or routing entirely with no visible error, and
  staff have no way to know a submission ever arrived.
DISCONFIRMING_OBSERVATION: >
  A record created with a missing dependent field does not receive the automated notification or routing step
  that records with the field present receive, and no failure or exception is recorded anywhere.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Force creation of a record missing a field that a downstream automated step depends on (per Q010-Q011);
  observe whether that step runs, fails visibly, or silently does not run.
```

## G09-WEBSITE_CRM-Q013

```yaml
QID: G09-WEBSITE_CRM-Q013
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Free-text content submitted through the public form is rendered to staff as inert text; it cannot cause the
  staff-facing interface to execute or interpret it as active content.
WHY_IT_MATTERS: >
  An internal viewer opening a record that renders hostile content submitted by an anonymous outsider is a
  direct compromise path into a system staff otherwise trust.
DISCONFIRMING_OBSERVATION: >
  Content submitted in a free-text field, structured to be interpreted rather than displayed, alters the
  staff-facing view's behaviour when that record is later opened by staff.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Submit the public form with a free-text field containing content structured to be interpreted by a viewer
  rather than displayed as text; open the resulting record in the internal staff view and observe its behaviour.
```

## G09-WEBSITE_CRM-Q014

```yaml
QID: G09-WEBSITE_CRM-Q014
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A free-text field accepts only content consistent with the kind of value it represents; content vastly
  exceeding a reasonable size does not silently pass through unbounded.
WHY_IT_MATTERS: >
  An unbounded free-text field is a channel for storing arbitrarily large payloads inside what is supposed to be
  a short business note, straining storage and any process that reads that field expecting ordinary text.
DISCONFIRMING_OBSERVATION: >
  A free-text field accepts and stores a payload many times larger than any legitimate use of that field would
  produce, with no limit applied.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit the public form with a free-text field filled with an extremely large value; inspect whether it is
  truncated, rejected, or stored whole.
```

## G09-WEBSITE_CRM-Q015

```yaml
QID: G09-WEBSITE_CRM-Q015
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Free-text content submitted publicly, when later included in an automated message generated from the record,
  cannot alter the structure or destination of that message.
WHY_IT_MATTERS: >
  If a submitted value can manipulate a later-generated message's structure or destination, an anonymous
  submitter gains influence over communications the business believes it controls.
DISCONFIRMING_OBSERVATION: >
  A specifically crafted value in a submitted field changes the structure, recipient, or delivery behaviour of
  an automated message later generated from that record.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Submit a field known to be echoed into a later automated message with a crafted value; trigger that message;
  inspect its structure and destination.
```

## G09-WEBSITE_CRM-Q016

```yaml
QID: G09-WEBSITE_CRM-Q016
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeated automated submissions from a single origin within a short window are constrained in some way
  (rejected, throttled, or flagged) rather than every one being accepted and turned into a distinct new record.
WHY_IT_MATTERS: >
  With no constraint, a trivial automated script can flood the sales team's queue faster than any human process
  can triage, in effect a denial of staff attention rather than of the system itself.
DISCONFIRMING_OBSERVATION: >
  A rapid sequence of automated submissions from a single origin in a short window are all accepted and each
  produces a distinct new record with no throttling, rejection, or flag of any kind.
EXPECTED_SURFACE: S3,S7,S8
PRECONDITIONS: >
  Submit the public form a large number of times in rapid succession from a single origin; inspect whether all
  submissions are accepted and how many distinct records result.
```

## G09-WEBSITE_CRM-Q017

```yaml
QID: G09-WEBSITE_CRM-Q017
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A burst of newly created records does not each independently trigger a full notification to the assigned
  staff member in a way that a volumetric burst could use to flood that person's inbox or device.
WHY_IT_MATTERS: >
  Even if records themselves are throttled, an unthrottled notification path is its own denial vector against
  the specific person the records are routed to.
DISCONFIRMING_OBSERVATION: >
  A burst of newly created records each generates its own immediate individual notification to the same
  assigned staff member with no batching, throttling, or volume-based suppression.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Cause a burst of records to be created and routed to the same owner in a short window; observe the volume and
  pacing of notifications that owner receives.
```

## G09-WEBSITE_CRM-Q018

```yaml
QID: G09-WEBSITE_CRM-Q018
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A large volume of low-quality automated submissions does not degrade the experience or performance of the
  public form for a legitimate concurrent visitor.
WHY_IT_MATTERS: >
  If volumetric abuse against the record-creation path also slows the form itself, the same attack becomes a
  denial of service against genuine customers trying to reach the business, not only against internal staff.
DISCONFIRMING_OBSERVATION: >
  While a volumetric burst of submissions is in progress, a separate, legitimate submission experiences
  materially degraded response time or failure compared to baseline.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Run a volumetric burst of submissions while separately timing or attempting a normal legitimate submission;
  compare its behaviour against a baseline measured with no burst in progress.
```

## G09-WEBSITE_CRM-Q019

```yaml
QID: G09-WEBSITE_CRM-Q019
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A submission built against an earlier version of the form's field set, sent after that field set has since
  changed, is handled predictably (accepted with the old fields ignored or mapped, or rejected) rather than
  producing an inconsistent or partially-populated record.
WHY_IT_MATTERS: >
  A visitor's browser can hold a stale copy of the form for an arbitrary length of time; if the record-creation
  path assumes the field set is always current, a stale submission can create a record matching neither the old
  nor the new form definition.
DISCONFIRMING_OBSERVATION: >
  A submission built against a field set the form no longer offers is accepted and produces a record with values
  in fields that no longer exist in the current form definition, unexplained and unflagged.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Capture the field set the form offers, change the form's configuration to remove or rename a field, then
  submit using the original, now-stale field set; inspect the resulting record.
```

## G09-WEBSITE_CRM-Q020

```yaml
QID: G09-WEBSITE_CRM-Q020
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A submission built against an earlier version of the form that lacks a field newly added to the current
  definition results in that new field being left at its defined default, not left in an undefined or
  inconsistent internal state.
WHY_IT_MATTERS: >
  An internal process reading the new field expecting it to always be populated one way or another will behave
  unpredictably against records created during the transition window.
DISCONFIRMING_OBSERVATION: >
  A record created from a stale submission that predates a newly added field shows that field in a state other
  than its defined default, or causes an error in any process that reads it.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Add a field to the form's configuration, then submit using a captured pre-change version of the form; inspect
  the new field's value on the resulting record and any process that reads it.
```

## G09-WEBSITE_CRM-Q021

```yaml
QID: G09-WEBSITE_CRM-Q021
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A change to which team or destination the form routes to takes effect only for submissions made after the
  change and does not retroactively alter where already-created records were routed.
WHY_IT_MATTERS: >
  Retroactively changing the destination of already-created records would move business records to owners who
  never agreed to them and break any notification already sent to the original owner.
DISCONFIRMING_OBSERVATION: >
  Changing the form's routing configuration after a record has already been created and routed causes that
  existing record's routing or ownership to change as well, with no new submission event.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Create a record via the form under one routing configuration, then change the routing configuration, and
  inspect whether the earlier record's routing or ownership is altered.
```

## G09-WEBSITE_CRM-Q022

```yaml
QID: G09-WEBSITE_CRM-Q022
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where the public site serves more than one company or brand, a submission is attributed at the moment of
  creation to the company the visitor actually interacted with, not to a single default regardless of which site
  or brand context they used.
WHY_IT_MATTERS: >
  This is a different failure point from a staff member later reassigning an existing opportunity across
  companies: here the record is born into the wrong company before any staff member ever sees it, and may never
  be looked at by anyone positioned to notice the error.
DISCONFIRMING_OBSERVATION: >
  A submission made through a site or brand context belonging to one company is created as a record owned by a
  different company.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Submit the form through each of at least two distinct company or brand site contexts the platform serves;
  inspect which company each resulting record belongs to.
```

## G09-WEBSITE_CRM-Q023

```yaml
QID: G09-WEBSITE_CRM-Q023
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A submission where the site or brand context cannot be determined is not silently assigned to whichever
  company happens to be first or default in an internal list; it is handled through a defined fallback or
  flagged as ambiguous.
WHY_IT_MATTERS: >
  An undefined default quietly becomes a rule nobody chose, and one company ends up receiving inquiries meant
  for another purely as an artifact of internal ordering.
DISCONFIRMING_OBSERVATION: >
  A submission with no determinable site or brand context is silently assigned to a company with no flag, log
  entry, or defined fallback governing that assignment.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Construct a submission that omits or obscures the site/brand context signal the form normally relies on;
  inspect which company the resulting record is assigned to and whether that assignment is flagged.
```

## G09-WEBSITE_CRM-Q024

```yaml
QID: G09-WEBSITE_CRM-Q024
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A visitor who submits the form separately through two different companies' site contexts served by the
  platform produces two separate records, one per company, rather than the duplicate-handling that operates
  within a company incorrectly collapsing them into one record that crosses the company boundary.
WHY_IT_MATTERS: >
  The same real person can legitimately have independent relationships with two separate companies on a shared
  platform; collapsing those into one record either leaks one company's business context into the other or
  arbitrarily assigns the relationship to only one of them.
DISCONFIRMING_OBSERVATION: >
  Submissions made by the same visitor through two different companies' site contexts result in a single record
  shared across both companies, or one company's submission is silently absorbed into the other's.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Submit the form as the same visitor through two distinct company site contexts; inspect whether two separate,
  company-scoped records result or whether they are collapsed into one.
```

## G09-WEBSITE_CRM-Q025

```yaml
QID: G09-WEBSITE_CRM-Q025
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Personal data collected through the public form is used only for the purpose the notice displayed on that form
  at submission actually stated, not repurposed for a materially different use the displayed notice never
  described.
WHY_IT_MATTERS: >
  The notice on the form is the one thing the submitter actually saw and relied on before handing over their
  details; a use that departs from what that specific text said breaches the one disclosure the submitter had
  any chance to read, regardless of what a general privacy policy elsewhere on the site might separately say.
DISCONFIRMING_OBSERVATION: >
  Data collected under the notice text shown on the public form is used for a materially different purpose than
  that text described, with no additional basis obtained.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Capture the exact notice text shown on the public form at submission; trace how the submitted data is actually
  used elsewhere in the pipeline; compare the two.
```

## G09-WEBSITE_CRM-Q026

```yaml
QID: G09-WEBSITE_CRM-Q026
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Personal data collected through the public form is retained for no longer than any retention period the form's
  own notice stated, and is not kept indefinitely by default once that period elapses.
WHY_IT_MATTERS: >
  A stated retention period the system does not actually enforce misleads the submitter about how long their
  data persists and creates exposure the business believes it has already closed off.
DISCONFIRMING_OBSERVATION: >
  A record's personal data remains fully present and unaltered well past any retention period the form's notice
  stated, with no deletion, anonymization, or review process having acted on it.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Identify any retention period stated in the form's own notice; locate or simulate a record old enough to have
  passed it; inspect whether the personal data has been removed, anonymized, or otherwise handled.
```

## G09-WEBSITE_CRM-Q027

```yaml
QID: G09-WEBSITE_CRM-Q027
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A submitter's data is used for follow-up contact only through the channel and for the purpose the form itself
  presented and the submitter agreed to at submission, not for a broader form of outreach the form never
  described.
WHY_IT_MATTERS: >
  Contacting someone through a channel or for a purpose beyond what the form told them is both a trust breach
  and, depending on the channel, a potential regulatory exposure of its own.
DISCONFIRMING_OBSERVATION: >
  A submitter who agreed to one channel or purpose of follow-up, as the form presented it, is contacted through a
  different channel or for a different purpose with no separate consent captured.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Submit the form capturing exactly what consent language and channel option the form presented; trace what
  follow-up contact actually occurs against that record.
```

## G09-WEBSITE_CRM-Q028

```yaml
QID: G09-WEBSITE_CRM-Q028
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An erasure request concerning a record created through the public form can be honored using only the kind of
  identifying detail the original anonymous submission itself collected, without the business first demanding a
  stronger form of identity proof, such as an account login, that the original unauthenticated submission
  process never required in the first place.
WHY_IT_MATTERS: >
  Requiring stronger proof at erasure time than the business itself required at collection time makes the right
  effectively unusable for exactly the records this module creates, since nobody who submitted anonymously holds
  the credential the business would now be asking for.
DISCONFIRMING_OBSERVATION: >
  An erasure request against a record created through the public form is refused or left unresolved specifically
  because the requester cannot supply a form of identity verification that the original submission process
  itself never collected or required.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a record via the public form; submit an erasure request referencing it using only the kind of detail
  the original submission itself collected; observe whether the business demands additional proof the original
  process never required.
```

## G09-WEBSITE_CRM-Q029

```yaml
QID: G09-WEBSITE_CRM-Q029
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Honoring an erasure request removes the submitter's personal data while preserving enough of the audit trail —
  that a submission occurred, when, and what happened to it — to still account for the record's history.
WHY_IT_MATTERS: >
  An erasure that also destroys the audit trail trades one obligation for another failure: the business loses
  its own accountability record for what happened to that inquiry.
DISCONFIRMING_OBSERVATION: >
  After an erasure request is honored, no trace remains in the audit trail that a submission, or a business
  action taken on it, ever occurred.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Honor an erasure request against a record with prior recorded activity; inspect the audit trail afterward for
  whether the history of the record's handling is still traceable.
```

## G09-WEBSITE_CRM-Q030

```yaml
QID: G09-WEBSITE_CRM-Q030
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An erasure request against a submitter's data reaches every record their data was copied or matched into
  through this bank's own duplicate-handling (Q008-Q009), not only the specific record the request happens to
  reference.
WHY_IT_MATTERS: >
  If a near-duplicate created through the public channel's own weaker matching is left untouched by an erasure
  request against the record the requester actually knew about, the submitter's data survives in the business
  under a different, unlinked record despite the request being honored on paper.
DISCONFIRMING_OBSERVATION: >
  After an erasure request is honored against one record, the same submitter's personal data is still present,
  unaffected, in a related record elsewhere in the system that this bank's own duplicate-handling had reason to
  connect to it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a near-duplicate pair for one submitter as in Q008-Q009, honor an erasure request referencing one of
  them, and inspect whether the other is also affected.
```

## G09-WEBSITE_CRM-Q031

```yaml
QID: G09-WEBSITE_CRM-Q031
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A file attached by a public submitter is restricted to the same allowed types the internal form would accept
  for the equivalent field, not accepted as an arbitrary file type.
WHY_IT_MATTERS: >
  An unrestricted upload channel from the open internet directly into internal storage is a well-known route for
  smuggling harmful content into a business system.
DISCONFIRMING_OBSERVATION: >
  A file of a type the internal form's equivalent field would refuse is accepted and stored when submitted as a
  public attachment.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify the internal form's allowed attachment types for the equivalent field; submit a disallowed type
  through the public form; inspect whether it is accepted and stored.
```

## G09-WEBSITE_CRM-Q032

```yaml
QID: G09-WEBSITE_CRM-Q032
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The number and total size of attachments a single public submission may include is bounded, rather than
  accepting an unbounded quantity or size from an unauthenticated source.
WHY_IT_MATTERS: >
  An unbounded attachment channel from the public internet is a storage-cost and availability exposure with no
  offsetting business benefit.
DISCONFIRMING_OBSERVATION: >
  A single public submission is accepted with an attachment count or total size far beyond what any legitimate
  inquiry would need, with no limit enforced.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit the public form with an excessive number or size of attachments; inspect whether the submission is
  accepted in full.
```

## G09-WEBSITE_CRM-Q033

```yaml
QID: G09-WEBSITE_CRM-Q033
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An attachment submitted publicly is visible only to staff with legitimate access to the resulting record, not
  exposed through any broader or unauthenticated access path before a staff member has triaged it.
WHY_IT_MATTERS: >
  An attachment reachable without proper access before anyone has reviewed it defeats whatever access control the
  business believes protects records generally.
DISCONFIRMING_OBSERVATION: >
  An attachment submitted through the public form can be accessed by a party without legitimate access to the
  record, or before any staff member has opened the record, through some other access path.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Submit an attachment through the public form; attempt to access it through any path other than the normal
  staff record view, before staff have opened the record.
```

## G09-WEBSITE_CRM-Q034

```yaml
QID: G09-WEBSITE_CRM-Q034
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The acknowledgment shown or sent to a submitter confirms only that the submission was received, not that any
  business decision, qualification, or human review has occurred.
WHY_IT_MATTERS: >
  An acknowledgment that overstates what has actually happened sets an expectation with the customer that
  internal process has not yet met, damaging trust when the gap becomes visible.
DISCONFIRMING_OBSERVATION: >
  The acknowledgment's wording or content states or implies that a human has reviewed, qualified, or acted on the
  submission, when no such review has yet occurred.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Submit the form and capture the acknowledgment content immediately; compare its wording against the record's
  actual state, which should show no human action yet taken.
```

## G09-WEBSITE_CRM-Q035

```yaml
QID: G09-WEBSITE_CRM-Q035
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An acknowledgment is sent to the submitter only when the underlying record was actually created; if creation
  fails, no acknowledgment implying success is sent.
WHY_IT_MATTERS: >
  A submitter told their inquiry was received, when in fact nothing was recorded, believes they are in a sales
  queue that does not exist and will not be followed up with.
DISCONFIRMING_OBSERVATION: >
  A submission that fails to produce a stored record still results in an acknowledgment to the submitter
  indicating successful receipt.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Force a condition that would cause record creation to fail; submit the form under that condition and observe
  whether an acknowledgment is still sent.
```

## G09-WEBSITE_CRM-Q036

```yaml
QID: G09-WEBSITE_CRM-Q036
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a submission is later identified as a duplicate and consolidated into an existing record, the earlier
  acknowledgment already sent for it remains an accurate description of what actually happened to the
  submitter's inquiry.
WHY_IT_MATTERS: >
  If the acknowledgment refers to something that no longer exists as an independent record after consolidation,
  the submitter received a claim that only very briefly matched reality.
DISCONFIRMING_OBSERVATION: >
  After a submission is consolidated into an existing record as a duplicate, the acknowledgment already sent
  describes a state of affairs (a new independent inquiry) that no longer holds, with no follow-up correcting it.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Trigger consolidation of a publicly-submitted record into an existing one; compare the earlier acknowledgment's
  content against the post-consolidation state.
```

## G09-WEBSITE_CRM-Q037

```yaml
QID: G09-WEBSITE_CRM-Q037
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A record's audit trail records, durably and distinguishably from an ordinary staff-entered record, that it
  originated as unauthenticated content from the public internet — a distinction about how much the record's
  content can be trusted at the point it entered the system, not merely a bookkeeping note about which internal
  process last touched it.
WHY_IT_MATTERS: >
  Tracking who or what last triggered a change is a different question from whether anyone reviewing a record
  later can tell that its original content was never vouched for by anyone inside the business, which is what
  determines how much scrutiny the record's content deserves.
DISCONFIRMING_OBSERVATION: >
  A record created through the public form carries no discoverable marker distinguishing its unauthenticated
  public origin from a staff-entered record, beyond the ordinary who-changed-what log every record would carry
  regardless of origin.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Create a record via the public form and a comparable one entered directly by staff; inspect whether the audit
  trail carries a distinguishable, durable marker of unauthenticated public origin beyond the ordinary change log
  both records would have anyway.
```

## G09-WEBSITE_CRM-Q038

```yaml
QID: G09-WEBSITE_CRM-Q038
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The audit trail for a public submission retains enough context about the submission event itself — when, and
  through which site or form version — to support an investigation into a disputed or suspicious record.
WHY_IT_MATTERS: >
  Without this context, a later investigation into how a bad record entered the system, whether spam, fraud, or
  a misconfigured form, has nothing concrete to work from.
DISCONFIRMING_OBSERVATION: >
  The audit trail for a publicly-submitted record retains no information beyond the record's content itself: no
  submission time, form version, or originating context recoverable for investigation.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Create a record via the public form and inspect what submission-event context, beyond the record's own fields,
  is retained and reachable in the audit trail.
```

## G09-WEBSITE_CRM-Q039

```yaml
QID: G09-WEBSITE_CRM-Q039
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An accidental duplicate submission sent twice in immediate succession by the same visitor, such as a double
  click before any acknowledgment appears, is recognized as a single event rather than producing two separate
  business records.
WHY_IT_MATTERS: >
  Two records for a single moment of visitor action is a data quality problem entirely of the system's own
  making, unrelated to any input the visitor intended, and clutters the pipeline with false volume.
DISCONFIRMING_OBSERVATION: >
  Submitting the identical form content twice in immediate succession, before any acknowledgment is returned for
  the first, produces two independent records rather than one.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit the identical form content twice within the same short window, simulating an accidental double-send;
  inspect how many records result.
```

## G09-WEBSITE_CRM-Q040

```yaml
QID: G09-WEBSITE_CRM-Q040
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a submission is interrupted such that the visitor's browser never receives a response, the outcome on the
  server side — whether a record was created or not — is consistent and does not leave an orphaned partial
  record with no acknowledgment path.
WHY_IT_MATTERS: >
  A visitor who sees a failure and gives up, while a record was actually created, either gets contacted
  unexpectedly or is silently lost from the pipeline while believing they were never in it.
DISCONFIRMING_OBSERVATION: >
  Interrupting the connection after the submission is sent but before any response returns to the visitor results
  in a record being created with no corresponding acknowledgment ever reaching, or capable of reaching, the
  submitter, and no process later reconciling that gap.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Submit the form and interrupt the connection after sending but before a response is received; separately
  verify server-side whether a record was created; assess whether any reconciliation exists for this gap.
```

## G09-WEBSITE_CRM-Q041

```yaml
QID: G09-WEBSITE_CRM-Q041
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a submission's self-declared company name differs from an existing internal master record for what is
  otherwise recognizably the same company, the discrepancy is surfaced to staff rather than one value silently
  overwriting the other with no record of the conflict.
WHY_IT_MATTERS: >
  Silently overwriting a maintained master value with an unverified visitor-typed value degrades data quality
  other processes depend on; silently discarding the visitor's value can also lose a genuine correction.
DISCONFIRMING_OBSERVATION: >
  A submission's self-declared company name differing from an existing matched master record results in one
  value overwriting the other, or being discarded, with no flag, log, or staff-visible indication that a
  conflict existed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Submit the form with a company name that differs from, but is recognizably the same company as, an existing
  master record; inspect the resulting record and whether the discrepancy is flagged anywhere.
```

## G09-WEBSITE_CRM-Q042

```yaml
QID: G09-WEBSITE_CRM-Q042
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When staff delete or invalidate a record that originated from the public form because it was spam or otherwise
  illegitimate, that action is itself recorded in a way that distinguishes "removed because illegitimate" from
  an ordinary record deletion.
WHY_IT_MATTERS: >
  Without this distinction, no one can later tell how much of what the public form has ever produced was genuine
  versus discarded as abuse, which is exactly the figure needed to judge whether the form's protections are
  working.
DISCONFIRMING_OBSERVATION: >
  A record originating from the public form that staff remove as spam or illegitimate leaves no trace
  distinguishing that removal from any other ordinary deletion.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a record via the public form, have staff mark or delete it as spam/illegitimate through whatever
  mechanism exists, and inspect the audit trail for whether that reason is distinctly recorded.
```

## G09-WEBSITE_CRM-Q043

```yaml
QID: G09-WEBSITE_CRM-Q043
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A destination, team, or category that has been closed, archived, or deactivated internally is no longer offered
  by the public form as a live option, so a submission cannot target a destination that can no longer receive it.
WHY_IT_MATTERS: >
  A submission that targets a now-closed destination either vanishes into a place nobody is monitoring, or forces
  the system into an undefined fallback, either of which loses the inquiry.
DISCONFIRMING_OBSERVATION: >
  The public form continues to offer, and accept submissions against, a team, destination, or category that has
  been closed, archived, or deactivated internally, with no defined handling for where such a submission
  actually goes.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Close or archive a destination, team, or category that the public form references; without separately updating
  the form, submit selecting that option; inspect whether the form still offers it and where the resulting
  submission goes.
```

## G09-WEBSITE_CRM-Q044

```yaml
QID: G09-WEBSITE_CRM-Q044
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Changing which internal field a specific public-form field's value is written into requires a distinct,
  elevated permission from the permission needed merely to edit individual records the form produces.
WHY_IT_MATTERS: >
  The concern here is the structural mapping between an external, unauthenticated data source's fields and the
  internal record schema; if any record-editing permission is enough to change that mapping, far more staff than
  intended can silently redefine what an external field is even allowed to mean internally.
DISCONFIRMING_OBSERVATION: >
  A staff account holding only ordinary permission to edit individual records produced by the form is also able
  to change which internal field a given public-form field writes into.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Identify the permission level required to edit an individual record produced by the form; attempt to access or
  change the field-to-field mapping configuration using only that permission level.
```

## G09-WEBSITE_CRM-Q045

```yaml
QID: G09-WEBSITE_CRM-Q045
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A request delivered directly to the form's processing endpoint, without having been served the page it is
  supposed to originate from, is treated no more permissively than one that actually loaded the page first.
WHY_IT_MATTERS: >
  If the endpoint cannot tell whether a submission ever passed through the actual page, any protection presented
  as being "on the form" is cosmetic, and every other protection in this bank that assumes a submission came from
  the real page is undermined at its root.
DISCONFIRMING_OBSERVATION: >
  A request built directly against the processing endpoint, without first loading the public page, is accepted
  and creates a record identically to one that went through the actual page.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Submit a request directly to the form's processing endpoint without first loading the public page; compare its
  acceptance and outcome against a normal page-based submission.
```

## G09-WEBSITE_CRM-Q046

```yaml
QID: G09-WEBSITE_CRM-Q046
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The language of the acknowledgment shown or sent to the submitter matches the language of the specific site or
  page version they actually used, rather than always defaulting to one language regardless of which localized
  version of the public site the submission came through.
WHY_IT_MATTERS: >
  A submitter who used a page in their own language and receives an acknowledgment in a different one experiences
  the same jarring mismatch a wrong company assignment would cause, and reflects the same underlying seam
  failure: losing site context between submission and response.
DISCONFIRMING_OBSERVATION: >
  A submission made through a specific localized version of the public site results in an acknowledgment or
  follow-up in a different language than that version's own language.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Submit the form through a specific localized version of the site; inspect the language of the resulting
  acknowledgment or any follow-up communication.
```

## G09-WEBSITE_CRM-Q047

```yaml
QID: G09-WEBSITE_CRM-Q047
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A value describing where or how the visitor arrived at the form, populated automatically by the page rather
  than typed by the visitor, is treated as informational rather than as ground truth strong enough to drive an
  unreviewed downstream business decision.
WHY_IT_MATTERS: >
  Because that value is set by the visitor's own browser and is exactly as trustworthy as anything else arriving
  over this unauthenticated channel, treating it as verified truth for reporting or budget decisions launders the
  same unverified-input problem into numbers management believes are solid.
DISCONFIRMING_OBSERVATION: >
  A downstream report or automated decision, such as attributing credit for the inquiry to a specific channel or
  campaign, treats the browser-supplied source value as verified fact, with no indication anywhere that it is
  visitor-suppliable and unverified.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Submit the form with a fabricated or altered source/campaign indicator; trace whether any downstream report or
  decision treats that value as verified.
```

## G09-WEBSITE_CRM-Q048

```yaml
QID: G09-WEBSITE_CRM-Q048
MODULE: website_crm
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where the public form allows the visitor to state a preferred language or contact channel, that stated
  preference is available to, and considered by, whatever logic assigns the resulting record to a specific
  salesperson or team.
WHY_IT_MATTERS: >
  Collecting a stated preference and then assigning the inquiry to someone who cannot act on it wastes the one
  piece of information the visitor explicitly volunteered to make the interaction work for them.
DISCONFIRMING_OBSERVATION: >
  A record carrying a visitor-stated language or contact-channel preference is assigned to an owner or team with
  no capability matching that stated preference, and the assignment logic shows no evidence of having considered
  it.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Submit the form with an explicit stated language or channel preference; inspect the resulting assignment for
  whether that preference was available to or reflected by the assignment outcome.
```
