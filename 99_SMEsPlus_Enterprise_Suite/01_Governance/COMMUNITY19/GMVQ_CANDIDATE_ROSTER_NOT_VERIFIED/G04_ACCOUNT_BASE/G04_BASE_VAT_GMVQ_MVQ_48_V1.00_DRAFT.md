# SMEsPlus ENTERPRISE SUITE
## GMVQ — G04 ACCOUNT_BASE / base_vat Module MVQ Bank

**Document ID:** GMVQ-G04-BASE_VAT-MVQ48-V1.00
**Group:** G04 ACCOUNT_BASE
**Module Metadata:** `base_vat`
**Wave:** W1
**Author Cell:** TEAM 23 (GMVQ Question Factory — Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48

## Purpose
This bank supplies the module-specific research questions for `base_vat` — the handling of
business tax-registration identifiers and their validation, including validation against an
external registry. It is written for a blind two-lane study: Lane A reads reference source,
Lane B observes a running system, and neither sees the other's answers. Question text is
source-neutral throughout.

## Control
- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: 48 questions exist because they test 48 distinct material hypotheses,
  spread across format-vs-registry-vs-live-status validation, registry unavailability,
  post-issuance identifier change, tax-treatment coupling, multi-jurisdiction partners,
  per-company values on a shared partner, import/enrichment provenance, evidence retention,
  and the audit trail of treatment-altering changes.
- This bank is DRAFT authoring output only. Not approved, not frozen, not verified.
- `MODULE + QID` is a Research Evidence Join Key only; no Formal Coverage is derived here.

---

## G04-BASE_VAT-Q001

```yaml
QID: G04-BASE_VAT-Q001
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An identifier that only satisfies a structural format check must be distinguishable, as a
  stored fact, from one that has been confirmed against an external registry.
WHY_IT_MATTERS: >
  Treating a merely well-formed identifier as confirmed lets an unverified tax status drive
  real tax treatment.
DISCONFIRMING_OBSERVATION: >
  A record that has only passed a structural format check reports, or is treated downstream
  as, registry-confirmed with no distinguishing state.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enter an identifier that is structurally well-formed but not yet checked against any
  external source, and inspect what state is persisted before any registry call occurs.
```

## G04-BASE_VAT-Q002

```yaml
QID: G04-BASE_VAT-Q002
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Registry confirmation obtained at one point in time must not be treated as proof that the
  registration is live on a later, different tax point date without re-confirmation or an
  explicit as-of qualifier.
WHY_IT_MATTERS: >
  Registrations lapse or change; reusing a stale confirmation misstates tax treatment on
  documents dated later.
DISCONFIRMING_OBSERVATION: >
  A document dated well after the original confirmation relies on that same confirmation as
  current proof, with no as-of date attached or re-check performed.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Confirm an identifier, let a business-relevant interval pass, then create a document
  referencing the same identifier and inspect what proof of currency is used.
```

## G04-BASE_VAT-Q003

```yaml
QID: G04-BASE_VAT-Q003
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A registration that the registry confirms as currently active is not automatically proof
  that it was live specifically on the transaction's tax point date.
WHY_IT_MATTERS: >
  Tax treatment is anchored to the tax point date; conflating "active now" with "active then"
  misapplies treatment to historical documents.
DISCONFIRMING_OBSERVATION: >
  A document with a tax point date preceding a registration's known start (or following its
  known end) is treated as fully valid solely because the identifier is active today.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Use an identifier with a known registration start or end date and create a document whose
  tax point date falls outside that window.
```

## G04-BASE_VAT-Q004

```yaml
QID: G04-BASE_VAT-Q004
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether registry confirmation is mandatory before a document may proceed is an explicit,
  inspectable configuration choice rather than an unstated default.
WHY_IT_MATTERS: >
  An unstated default silently decides risk tolerance that should be a deliberate business
  decision.
DISCONFIRMING_OBSERVATION: >
  Documents proceed, or are blocked, based on confirmation status with no corresponding
  configuration setting an operator can locate and change.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Search the available configuration surface for a setting governing whether unconfirmed
  identifiers may be used, and attempt to change its value.
```

## G04-BASE_VAT-Q005

```yaml
QID: G04-BASE_VAT-Q005
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Format validity and registry-confirmed validity are stored as two separable facts, so that
  one can regress (e.g. a later edit breaks the format) without silently updating the other.
WHY_IT_MATTERS: >
  Collapsing the two into one flag hides which check actually last passed.
DISCONFIRMING_OBSERVATION: >
  Editing an identifier so that it no longer satisfies the format rule leaves a prior
  registry-confirmed status unchanged and still reported as confirmed.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Confirm an identifier successfully, then edit it into a structurally invalid value and
  inspect both stored facts.
```

## G04-BASE_VAT-Q006

```yaml
QID: G04-BASE_VAT-Q006
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An identifier whose registry-confirmation outcome was never determined (neither confirmed
  nor rejected) is never silently read downstream as equivalent to confirmed.
WHY_IT_MATTERS: >
  An indeterminate state defaulting to "treated as valid" understates risk on every document
  that depends on it.
DISCONFIRMING_OBSERVATION: >
  A record whose confirmation field is blank or indeterminate is used by a downstream tax
  calculation exactly as a confirmed record would be.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create a record with the confirmation outcome left undetermined and trace how a tax
  calculation that depends on confirmation status treats it.
```

## G04-BASE_VAT-Q007

```yaml
QID: G04-BASE_VAT-Q007
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external registry cannot be reached at the moment a document is created, the
  document's proceeding or blocking is a defined, observable outcome rather than an
  unhandled failure.
WHY_IT_MATTERS: >
  An unhandled external dependency failure either silently blocks business activity or
  silently waives a control meant to catch bad identifiers.
DISCONFIRMING_OBSERVATION: >
  With the external registry made unreachable, document creation either hangs with no
  defined outcome, or proceeds with no record that the check was skipped.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Make the external registry endpoint unreachable and attempt to create a document that
  would normally trigger a registry check.
```

## G04-BASE_VAT-Q008

```yaml
QID: G04-BASE_VAT-Q008
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A registry call that times out after a long wait is distinguished, in the resulting state,
  from a registry call that fails immediately with a network error.
WHY_IT_MATTERS: >
  A slow-but-eventually-correct source and a genuinely broken one carry different retry and
  trust implications; conflating them misleads later reconciliation.
DISCONFIRMING_OBSERVATION: >
  The stored outcome after a slow timeout is identical in every field to the stored outcome
  after an immediate connection failure, with no way to tell them apart later.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Simulate a slow (timeout) registry response and, separately, an immediate connection
  failure, and compare the persisted results.
```

## G04-BASE_VAT-Q009

```yaml
QID: G04-BASE_VAT-Q009
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A registry response that is ambiguous or inconclusive (neither a clear pass nor a clear
  fail) is never silently recorded as a pass.
WHY_IT_MATTERS: >
  Defaulting an ambiguous answer to "valid" converts uncertainty into false confidence.
DISCONFIRMING_OBSERVATION: >
  An ambiguous or partial registry response results in the identifier being marked confirmed
  with no indication that the answer was inconclusive.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Simulate a registry response that is neither a definite match nor a definite non-match and
  inspect the resulting stored status.
```

## G04-BASE_VAT-Q010

```yaml
QID: G04-BASE_VAT-Q010
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A retry or later re-check that eventually reaches the registry after an earlier failure
  updates the record's status through a visible, attributable event, not a silent overwrite.
WHY_IT_MATTERS: >
  A silent later change to tax-relevant status defeats anyone relying on the state as it
  stood when a document was created.
DISCONFIRMING_OBSERVATION: >
  A record's confirmation status changes value between two points in time with no
  accompanying event, actor, or timestamp explaining the change.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Leave a record unconfirmed after a registry failure, allow any background re-check
  mechanism to run once the registry is reachable, and inspect what trail the change leaves.
```

## G04-BASE_VAT-Q011

```yaml
QID: G04-BASE_VAT-Q011
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two documents created for the same partner while the registry is unreachable end up with
  consistent, not divergent, unconfirmed status for the same underlying identifier.
WHY_IT_MATTERS: >
  Divergent status for the same fact on the same partner indicates a race or an
  inconsistent write path rather than a genuine business difference.
DISCONFIRMING_OBSERVATION: >
  Two documents created moments apart for the same partner and identifier, both during a
  registry outage, end up recording different confirmation states.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  With the registry unreachable, create two documents in quick succession referencing the
  same partner and identifier, then compare recorded status.
```

## G04-BASE_VAT-Q012

```yaml
QID: G04-BASE_VAT-Q012
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When the registry becomes reachable again after an outage, any automatic reconciliation of
  previously unconfirmed identifiers is itself visible to a reviewer, not an invisible
  background correction.
WHY_IT_MATTERS: >
  An invisible retroactive correction can quietly change the basis on which past documents
  were treated, without anyone being able to see that it happened.
DISCONFIRMING_OBSERVATION: >
  A previously unconfirmed identifier's status changes automatically once the registry is
  reachable again, with no log entry a reviewer can find.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Restore registry reachability after an outage that left records unconfirmed, and check
  the audit surface for any resulting automatic status change.
```

## G04-BASE_VAT-Q013

```yaml
QID: G04-BASE_VAT-Q013
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Correcting a partner's identifier after documents already carry the earlier value does not
  change the value shown on those already-issued documents.
WHY_IT_MATTERS: >
  Issued documents are a record of what was true when they were created; retroactively
  rewriting them destroys their evidentiary value.
DISCONFIRMING_OBSERVATION: >
  After the partner's identifier is corrected, a previously issued document displays or
  reports the new value instead of the one that was current when it was issued.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Issue a document referencing a partner's identifier, then change that identifier on the
  partner, and re-open the already-issued document.
```

## G04-BASE_VAT-Q014

```yaml
QID: G04-BASE_VAT-Q014
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A posted, historical transaction's stored identifier value cannot be silently rewritten by
  a later correction to the partner's current identifier.
WHY_IT_MATTERS: >
  Silent rewriting of posted history breaks reconciliation against anything filed or
  reported using the original value.
DISCONFIRMING_OBSERVATION: >
  A posted transaction's stored identifier value changes as a side effect of editing the
  partner record, with no separate action taken on the transaction itself.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post a transaction carrying an identifier snapshot, then edit the identifier on the
  partner master record, and re-inspect the posted transaction.
```

## G04-BASE_VAT-Q015

```yaml
QID: G04-BASE_VAT-Q015
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Changing a partner's identifier does not, by itself, trigger any automatic re-evaluation
  of the tax treatment already applied to documents posted before the change.
WHY_IT_MATTERS: >
  Automatic silent re-evaluation of posted, closed documents crosses a governance boundary
  that should require an explicit, visible action.
DISCONFIRMING_OBSERVATION: >
  Posted documents predating an identifier change show a different computed tax treatment
  immediately after the change, without any explicit re-evaluation being run.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Post documents under one identifier value, change the identifier, and check whether the
  posted documents' treatment changed without explicit action.
```

## G04-BASE_VAT-Q016

```yaml
QID: G04-BASE_VAT-Q016
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Reversing a document that was issued under an identifier value that has since changed
  produces a reversing entry carrying the same value the original document carried, not the
  partner's current value.
WHY_IT_MATTERS: >
  A reversal must mirror what it reverses; substituting the current value breaks the
  correspondence an auditor needs between an entry and its reversal.
DISCONFIRMING_OBSERVATION: >
  A reversing entry for a document issued under an old identifier value shows the partner's
  new, current identifier instead of the value on the original document.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Issue a document, change the partner's identifier, then reverse the original document and
  compare the identifier value on each side.
```

## G04-BASE_VAT-Q017

```yaml
QID: G04-BASE_VAT-Q017
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An exempt tax treatment that depends on the presence or status of a business identifier is
  re-examined if that identifier's status was actually wrong at the time the treatment was
  applied.
WHY_IT_MATTERS: >
  Exemptions granted on a false premise misstate a filed tax position and are hard to find
  after the fact if nothing flags them.
DISCONFIRMING_OBSERVATION: >
  A document treated as exempt because of an identifier that is later found to have been
  invalid at that time carries no flag, exception, or reviewable trace of the discrepancy.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Apply an exempt treatment based on an identifier, later discover the identifier was
  invalid at the treatment date, and look for any resulting exception record.
```

## G04-BASE_VAT-Q018

```yaml
QID: G04-BASE_VAT-Q018
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A reverse-charge treatment that depends on the counterparty's registration status is
  computed from that status as it stood at the tax point date, not from whatever status
  happens to be current when the document is later viewed.
WHY_IT_MATTERS: >
  Computing from the current status instead of the tax-point status can silently change a
  document's displayed or reported treatment after the fact.
DISCONFIRMING_OBSERVATION: >
  Re-opening a posted document after the counterparty's registration status changes shows a
  different reverse-charge determination than what was applied at posting.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Post a document under a reverse-charge determination, change the counterparty's
  registration status, and re-open the posted document.
```

## G04-BASE_VAT-Q019

```yaml
QID: G04-BASE_VAT-Q019
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A zero-rated treatment that depends on a qualifying identifier for a given transaction
  scope is not granted to a partner who lacks a qualifying identifier in that scope, even if
  they hold one in an unrelated scope.
WHY_IT_MATTERS: >
  Treating any identifier as sufficient regardless of scope grants a favourable treatment
  the transaction has not actually earned.
DISCONFIRMING_OBSERVATION: >
  A partner holding a qualifying identifier only in an unrelated scope still receives the
  zero-rated treatment for a transaction outside that scope.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Set up a partner with a qualifying identifier in one scope only, then create a transaction
  in a different scope and observe the treatment applied.
```

## G04-BASE_VAT-Q020

```yaml
QID: G04-BASE_VAT-Q020
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When registry confirmation completes after a document has already been created and
  invalidates the treatment that was applied at creation, the affected document is flagged
  for review rather than left silently inconsistent.
WHY_IT_MATTERS: >
  A document whose applied treatment is now known to be wrong, with nothing pointing to it,
  will not get corrected before it is filed or reported.
DISCONFIRMING_OBSERVATION: >
  A document created before confirmation completes, whose treatment confirmation later
  contradicts, remains unflagged and indistinguishable from a correctly treated document.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Create a document before registry confirmation resolves, let the resolution contradict the
  treatment applied, and check for a resulting flag or exception.
```

## G04-BASE_VAT-Q021

```yaml
QID: G04-BASE_VAT-Q021
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A document created under one determined treatment retains a record of which
  determination was in effect at creation, independent of what the current determination
  would be if recomputed today.
WHY_IT_MATTERS: >
  Without that retained record, no one can tell in hindsight whether a document's treatment
  was consistent with the facts known at the time.
DISCONFIRMING_OBSERVATION: >
  There is no way to determine, after the fact, which treatment determination a given
  document was created under, only what the determination would be if computed now.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Locate an older document and attempt to determine, from its own record, the treatment
  basis that applied when it was created.
```

## G04-BASE_VAT-Q022

```yaml
QID: G04-BASE_VAT-Q022
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Overriding a tax treatment that is inconsistent with the current identifier status
  requires an authorization distinct from ordinary document entry, and that override is
  itself recorded as an override.
WHY_IT_MATTERS: >
  If any ordinary user can force an inconsistent treatment unremarked, the identifier check
  provides no real control.
DISCONFIRMING_OBSERVATION: >
  A user with only ordinary document-entry rights can force a treatment contradicting the
  current identifier status, and the result is stored indistinguishably from a normal
  determination.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  As a user with ordinary entry rights only, attempt to force a treatment inconsistent with
  the identifier's current status.
```

## G04-BASE_VAT-Q023

```yaml
QID: G04-BASE_VAT-Q023
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A document cannot be posted while carrying a tax treatment that is inconsistent with the
  identifier status recorded for that same document, without at least a visible warning or
  block.
WHY_IT_MATTERS: >
  Silent posting of an internally inconsistent document defeats the purpose of tracking
  identifier status at all.
DISCONFIRMING_OBSERVATION: >
  A document posts successfully with no warning while its applied treatment contradicts the
  identifier status recorded on the same document.
EXPECTED_SURFACE: S1,S2,S3
PRECONDITIONS: >
  Construct a document whose applied treatment does not match its own recorded identifier
  status and attempt to post it.
```

## G04-BASE_VAT-Q024

```yaml
QID: G04-BASE_VAT-Q024
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a partner holds valid identifiers in more than one jurisdiction, which identifier
  applies to a given document is an explicit, inspectable determination rather than an
  implicit pick of whichever value happens to be listed first.
WHY_IT_MATTERS: >
  An implicit, unexplained selection among several valid identifiers can silently apply the
  wrong jurisdiction's tax logic.
DISCONFIRMING_OBSERVATION: >
  A partner with identifiers in two jurisdictions produces a document whose applied
  identifier cannot be explained by any visible selection rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a partner with valid identifiers in two distinct jurisdictions and create a
  document, then trace which identifier was actually used and why.
```

## G04-BASE_VAT-Q025

```yaml
QID: G04-BASE_VAT-Q025
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A multi-jurisdiction partner's applicable identifier can differ by document type (for
  example, a sale versus a purchase) without one document type's selection contaminating the
  other's.
WHY_IT_MATTERS: >
  Cross-contamination between transaction directions would apply the wrong jurisdiction's
  identifier to at least one side of the business.
DISCONFIRMING_OBSERVATION: >
  Creating a document of one type changes which identifier is subsequently offered or
  applied for the other document type for the same partner.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  With a multi-jurisdiction partner, create a sales document and then a purchase document,
  comparing the identifier selection behaviour for each.
```

## G04-BASE_VAT-Q026

```yaml
QID: G04-BASE_VAT-Q026
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When none of a partner's several jurisdiction-specific identifiers cleanly matches a given
  transaction, the system surfaces this as a blocking exception rather than guessing.
WHY_IT_MATTERS: >
  Guessing among mismatched identifiers can apply an identifier, and its jurisdiction's tax
  logic, that has nothing to do with the actual transaction.
DISCONFIRMING_OBSERVATION: >
  A transaction that matches none of the partner's jurisdiction-specific identifiers still
  proceeds with one silently selected, and no exception is raised.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Construct a transaction whose jurisdiction does not correspond to any identifier held by
  the partner and attempt to proceed.
```

## G04-BASE_VAT-Q027

```yaml
QID: G04-BASE_VAT-Q027
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The company or branch location on a transaction is considered together with the partner's
  jurisdiction-specific identifier when tax logic is determined, rather than the identifier
  being applied independently of where the transaction itself is booked.
WHY_IT_MATTERS: >
  Ignoring the booking company's own location while only looking at the partner's identifier
  can select tax logic that applies to neither side correctly.
DISCONFIRMING_OBSERVATION: >
  Changing only the booking company or branch on an otherwise identical transaction produces
  no difference in which identifier or tax logic is applied.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Repeat an otherwise identical transaction under two different booking companies or
  branches and compare the identifier and tax logic applied.
```

## G04-BASE_VAT-Q028

```yaml
QID: G04-BASE_VAT-Q028
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A missing jurisdiction-specific configuration for a required scenario is surfaced as a
  gap requiring attention, rather than silently defaulting to a behaviour nobody chose.
WHY_IT_MATTERS: >
  A silent default in place of a deliberately configured jurisdiction rule hides a business
  decision that was never actually made.
DISCONFIRMING_OBSERVATION: >
  A transaction requiring jurisdiction-specific configuration that has never been set
  proceeds normally with no indication that a required setting is absent.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Leave a jurisdiction-specific configuration unset and create a transaction that would
  require it.
```

## G04-BASE_VAT-Q029

```yaml
QID: G04-BASE_VAT-Q029
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  When a single partner is shared across companies and holds a distinct identifier value
  per company, a document booked in one company uses that company's own value, never
  another company's.
WHY_IT_MATTERS: >
  Cross-company leakage of a tax identifier value misstates the tax position for whichever
  company's document used the wrong value.
DISCONFIRMING_OBSERVATION: >
  A document booked in one company uses the identifier value stored for that same shared
  partner under a different company.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  Share one partner across two companies with distinct per-company identifier values, and
  create a document in each company against that partner.
```

## G04-BASE_VAT-Q030

```yaml
QID: G04-BASE_VAT-Q030
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Editing a shared partner's identifier value for one company does not change, or expose,
  the value held for that same partner under a different company.
WHY_IT_MATTERS: >
  A single shared record must still preserve per-company boundary even under direct edits.
DISCONFIRMING_OBSERVATION: >
  Editing the identifier value in the context of one company changes the stored value
  visible in the context of another company for the same shared partner.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Edit the per-company identifier value for a shared partner while acting in one company's
  context, then inspect the value visible from another company's context.
```

## G04-BASE_VAT-Q031

```yaml
QID: G04-BASE_VAT-Q031
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a shared partner has no company-specific identifier set for the current company but
  does have one recorded generally, the fallback to that general value is an explicit,
  visible behaviour rather than an unstated default.
WHY_IT_MATTERS: >
  An unstated fallback can apply an identifier to a company that never actually confirmed it
  is correct for that company.
DISCONFIRMING_OBSERVATION: >
  A document proceeds using a general identifier value with no indication that the current
  company had no specific value of its own.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a general identifier value on a shared partner but no company-specific value, then
  create a document from a company lacking its own value.
```

## G04-BASE_VAT-Q032

```yaml
QID: G04-BASE_VAT-Q032
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two companies updating their respective per-company identifier values on the same shared
  partner at nearly the same time do not corrupt or overwrite each other's value.
WHY_IT_MATTERS: >
  A shared underlying record is a natural point of contention; a race here silently loses
  one company's correct value.
DISCONFIRMING_OBSERVATION: >
  Concurrent updates from two companies to their own respective per-company values on the
  same shared partner result in one company's value being lost or overwritten by the other's.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  From two company contexts, submit near-simultaneous updates to each company's own
  per-company identifier value on the same shared partner.
```

## G04-BASE_VAT-Q033

```yaml
QID: G04-BASE_VAT-Q033
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A change to a shared partner's per-company identifier value is logged with which company's
  context the change was made in, not just that a change occurred.
WHY_IT_MATTERS: >
  Without the acting company recorded, a cross-company change cannot be traced back to who
  was actually authorized to make it.
DISCONFIRMING_OBSERVATION: >
  The change log for a per-company identifier value shows that a change occurred but not
  which company's context the actor was operating in.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change a per-company identifier value while acting in a specific company context and
  inspect the resulting log entry's fields.
```

## G04-BASE_VAT-Q034

```yaml
QID: G04-BASE_VAT-Q034
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Identifiers introduced through a bulk import pass through the same validation as
  identifiers entered one at a time by a user.
WHY_IT_MATTERS: >
  A bulk path that bypasses validation is a much larger source of bad tax-relevant data than
  any single manual entry.
DISCONFIRMING_OBSERVATION: >
  An identifier that would be rejected or flagged when typed manually is accepted without
  comment when it arrives through a bulk import.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Prepare an import batch containing an identifier that manual entry would reject, and run
  the import.
```

## G04-BASE_VAT-Q035

```yaml
QID: G04-BASE_VAT-Q035
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An identifier value supplied automatically by an enrichment source is distinguishable, by
  its recorded provenance, from one a person entered and confirmed themselves.
WHY_IT_MATTERS: >
  An automatically supplied value has not been vouched for by a human; treating it the same
  as a confirmed manual entry overstates its reliability.
DISCONFIRMING_OBSERVATION: >
  A value populated by an automatic enrichment pass carries no recorded provenance
  distinguishing it from a manually entered and confirmed value.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Let an enrichment mechanism populate an identifier automatically and inspect what, if
  anything, records where the value came from.
```

## G04-BASE_VAT-Q036

```yaml
QID: G04-BASE_VAT-Q036
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An import that introduces a conflicting identifier for a partner who already has a
  different confirmed identifier on file is surfaced as a conflict, not silently overwritten
  or silently duplicated.
WHY_IT_MATTERS: >
  A silent overwrite destroys a previously confirmed value; a silent duplicate creates two
  competing truths for the same partner.
DISCONFIRMING_OBSERVATION: >
  Importing a conflicting identifier for a partner that already has a different confirmed
  one produces neither a visible conflict nor any trace that the prior value was replaced.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Import a record carrying an identifier that conflicts with a partner's existing confirmed
  identifier and observe the outcome.
```

## G04-BASE_VAT-Q037

```yaml
QID: G04-BASE_VAT-Q037
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether an imported or enrichment-sourced identifier requires a subsequent manual
  confirmation before it can be relied upon for tax treatment is an enforceable setting, not
  merely a documented recommendation.
WHY_IT_MATTERS: >
  A recommendation nobody enforces is equivalent to no control at all once volume makes
  manual review impractical.
DISCONFIRMING_OBSERVATION: >
  With the setting requiring manual confirmation enabled, an imported identifier still drives
  tax treatment on a document before any manual confirmation has occurred.
EXPECTED_SURFACE: S1,S2,S7
PRECONDITIONS: >
  Enable any available setting requiring manual confirmation of imported identifiers, import
  one, and attempt to use it in a document before confirming it.
```

## G04-BASE_VAT-Q038

```yaml
QID: G04-BASE_VAT-Q038
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An enrichment source silently updating a partner's identifier value in the background does
  not carry forward a prior human confirmation as if it still applied to the new value.
WHY_IT_MATTERS: >
  Carrying a confirmation forward onto a value nobody actually confirmed converts an
  unverified change into a false assurance.
DISCONFIRMING_OBSERVATION: >
  After an enrichment pass silently changes the identifier value, the record still shows a
  confirmed status that predates the change.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Confirm an identifier manually, then let a background enrichment pass change the value,
  and inspect whether the confirmed status persists unchanged.
```

## G04-BASE_VAT-Q039

```yaml
QID: G04-BASE_VAT-Q039
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A durable record of what the external registry actually returned at confirmation time is
  retained, separate from a boolean confirmed/not-confirmed flag.
WHY_IT_MATTERS: >
  A bare flag cannot later prove what was actually known; only the retained response can.
DISCONFIRMING_OBSERVATION: >
  After a registry confirmation, no retrievable record of the registry's actual response
  exists beyond the resulting flag.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Confirm an identifier against the registry, then search for a retained copy of the actual
  response received, apart from the resulting status flag.
```

## G04-BASE_VAT-Q040

```yaml
QID: G04-BASE_VAT-Q040
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Evidence of a past registry confirmation remains retrievable after a substantial passage
  of time, not only immediately after the check was performed.
WHY_IT_MATTERS: >
  Evidence that only exists transiently is worthless for an audit conducted months or years
  later.
DISCONFIRMING_OBSERVATION: >
  A confirmation performed well in the past can no longer be retrieved in its original
  supporting detail, only as a current flag with no history behind it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Locate a registry confirmation performed a significant time ago and attempt to retrieve
  its original supporting detail.
```

## G04-BASE_VAT-Q041

```yaml
QID: G04-BASE_VAT-Q041
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A record cannot show a confirmed status with no corresponding evidence of the check that
  produced it; the two are structurally linked, not independently settable.
WHY_IT_MATTERS: >
  A confirmed flag with nothing behind it is indistinguishable from one that was set in
  error or set without ever actually checking.
DISCONFIRMING_OBSERVATION: >
  A record shows confirmed status while no supporting evidence of any registry check can be
  found for it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Survey confirmed records for whether each one has a corresponding evidence record, looking
  for any that do not.
```

## G04-BASE_VAT-Q042

```yaml
QID: G04-BASE_VAT-Q042
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Given a document and its tax point date, an operator can produce evidence of what was
  known about the relevant identifier's status specifically as of that date, not only what
  is known now.
WHY_IT_MATTERS: >
  A reviewer asking "what did you know then" cannot be answered with "here is what we know
  today" without that being a materially different, and weaker, answer.
DISCONFIRMING_OBSERVATION: >
  For an older document, the only status information retrievable is the current one; nothing
  distinguishes it from the status as of the document's own tax point date.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Pick a document whose tax point date is well in the past and attempt to produce evidence
  of the identifier status specifically as of that date.
```

## G04-BASE_VAT-Q043

```yaml
QID: G04-BASE_VAT-Q043
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Removing or purging a confirmation evidence record also changes the derived confirmed
  status it supported, rather than leaving that status standing on nothing.
WHY_IT_MATTERS: >
  A status left standing after its own supporting evidence is gone is an unsupported claim
  masquerading as a verified one.
DISCONFIRMING_OBSERVATION: >
  Deleting or purging the evidence behind a confirmation leaves the confirmed status
  displayed exactly as before, with no indication the support is gone.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Where evidence purging is possible, remove the evidence record behind a confirmed
  identifier and inspect the resulting status.
```

## G04-BASE_VAT-Q044

```yaml
QID: G04-BASE_VAT-Q044
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A change to a partner's identifier that would alter the tax treatment of a not-yet-posted
  document is logged with both the treatment that applied before the change and the
  treatment that applies after.
WHY_IT_MATTERS: >
  Recording only that a change happened, without the before-and-after treatment, leaves a
  reviewer unable to assess the change's actual consequence.
DISCONFIRMING_OBSERVATION: >
  The log for an identifier change that alters a draft document's treatment records the
  identifier values changed but not the treatment before and after.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Create a draft document, change the partner's identifier so that the applicable treatment
  would differ, and inspect the resulting log entry.
```

## G04-BASE_VAT-Q045

```yaml
QID: G04-BASE_VAT-Q045
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A user without rights to configure tax treatment cannot, merely by editing a partner's
  identifier, change the tax treatment applied to that partner's documents.
WHY_IT_MATTERS: >
  If identifier edits are a side door to changing tax treatment, permission controls placed
  on tax configuration itself are meaningless.
DISCONFIRMING_OBSERVATION: >
  A user with no tax-configuration rights edits a partner's identifier and thereby changes
  the tax treatment subsequently applied to that partner's documents.
EXPECTED_SURFACE: S1,S2,S4
PRECONDITIONS: >
  As a user without tax-configuration rights, edit a partner's identifier so that it would
  change applicable treatment, and observe the resulting document treatment.
```

## G04-BASE_VAT-Q046

```yaml
QID: G04-BASE_VAT-Q046
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether an identifier change automatically cascades a new treatment onto existing draft
  documents, or instead requires an explicit re-evaluation action, is itself an observable,
  consistent behaviour rather than varying unpredictably by document.
WHY_IT_MATTERS: >
  Unpredictable cascading means no one can reliably know, without checking every document
  individually, whether a change has actually taken effect.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical draft documents affected by the same identifier change end up with
  different treatments, one cascaded and one not, with no explanation for the difference.
EXPECTED_SURFACE: S1,S2
PRECONDITIONS: >
  Create two comparable draft documents for the same partner, change the identifier, and
  compare whether and how each document's treatment updates.
```

## G04-BASE_VAT-Q047

```yaml
QID: G04-BASE_VAT-Q047
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the audit trail's record of an identifier's status at posting time is later found to
  disagree with the registry's own history for that date, that disagreement is flagged
  rather than silently left as two unreconciled facts.
WHY_IT_MATTERS: >
  An internal record that quietly contradicts the authoritative external source is worse
  than useless evidence — it is misleading evidence.
DISCONFIRMING_OBSERVATION: >
  An internal record of confirmed status at posting time is contradicted by the registry's
  own historical record for that date, with nothing surfacing the contradiction.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Compare an internally recorded confirmation-at-posting-time against the registry's own
  historical record for the same date, for a case engineered to disagree.
```

## G04-BASE_VAT-Q048

```yaml
QID: G04-BASE_VAT-Q048
MODULE: base_vat
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The audit trail connects an identifier-status event to the specific accounting entries
  whose treatment depended on it by an explicit reference, not merely by both occurring
  around the same time.
WHY_IT_MATTERS: >
  A time-only correlation forces a reviewer to guess which entries a status event actually
  affected, which does not hold up as evidence.
DISCONFIRMING_OBSERVATION: >
  The only way to associate an identifier-status event with the entries it affected is by
  comparing timestamps, with no explicit reference linking the two.
EXPECTED_SURFACE: S1,S2,S6
PRECONDITIONS: >
  Trigger an identifier-status event that affects a specific document's treatment and
  attempt to trace an explicit link from the event to the affected accounting entries.
```
