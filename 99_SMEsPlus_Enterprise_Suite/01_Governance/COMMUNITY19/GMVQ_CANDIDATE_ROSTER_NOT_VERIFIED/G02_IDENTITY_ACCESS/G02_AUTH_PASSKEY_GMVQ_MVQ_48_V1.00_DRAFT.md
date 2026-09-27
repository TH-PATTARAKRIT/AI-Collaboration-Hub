# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / auth_passkey Module Adversarial MVQ Bank

**Document ID:** GMVQ-G02-AUTH_PASSKEY-MVQ48-V1.00
**Group:** G02 IDENTITY_ACCESS
**Module Metadata:** `auth_passkey`
**Wave:** W1
**Author Cell:** TEAM 09 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard Bank Reference:** 55 shared standard questions (already authored elsewhere, not reproduced here); research depth = 55 + 48 = 103

## Purpose

This bank supplies module-specific research questions (MVQ) for a blind two-lane clean-room
study of `auth_passkey`. Lane A reads reference source; Lane B observes a running system and never
sees source or Lane A's output. Both lanes answer the same question, joined by MODULE + QID,
and the Reconciler compares answers cell to cell without studying anything itself.

Question text is written in generic identity/access and business-behaviour language. It
contains no vendor or product name, no technical identifier (model, table, field, method, XML
ID, API path), and no reference to the module's own metadata name outside the MODULE field, so
that a blind observational lane cannot infer implementation from the question text.

## Control

- Every question carries a falsifiable HYPOTHESIS and a DISCONFIRMING_OBSERVATION that states a
  concrete failure state, not a restatement of the hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses,
  spread across business capability, business rule, state transition, configuration dependency,
  role/permission, exception path, cancellation, reversal, negative case, cross-module
  dependency, optional behaviour, auditability, tenant/company boundary, concurrency and
  ordering, runtime reachability, configuration reachability, and source/runtime contradiction
  potential.
- Questions are not evidence. A later ANSWERED state requires an actual artifact or observation.
- This bank makes no claim of APPROVED, FINAL APPROVED, FROZEN, or MASTER-ready status.
- `MODULE + QID` is a Research Evidence Join Key only. No formal coverage is derived here.
- Author cell (TEAM 09) is not RED TEAM and approves nothing produced by this bank.

## G02-AUTH_PASSKEY-Q001

```yaml
QID: G02-AUTH_PASSKEY-Q001
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A new device-bound credential can only be enrolled from within a session that is already
  authenticated by an existing accepted factor; enrolment itself must never be usable to establish
  first-time access to an identity.
WHY_IT_MATTERS: >
  If enrolment could bootstrap access on its own, anyone able to intercept the enrolment step
  could seed a credential against a victim identity without ever proving prior legitimate access.
DISCONFIRMING_OBSERVATION: >
  An identity that has never successfully authenticated by any other accepted means ends up with a
  working device-bound credential attached to it.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Create a fresh identity with no prior successful authentication and attempt the enrolment
  ceremony directly against it, without first establishing an authenticated session by another
  accepted means.
```
## G02-AUTH_PASSKEY-Q002

```yaml
QID: G02-AUTH_PASSKEY-Q002
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A second device-bound credential can be added to an identity without disabling, replacing, or
  weakening the first one.
WHY_IT_MATTERS: >
  Users legitimately carry more than one device; if adding a second credential silently drops the
  first, they lose access unexpectedly and support load increases.
DISCONFIRMING_OBSERVATION: >
  Enrolling a second credential causes the first previously working credential to stop
  authenticating, or its record to be altered without an explicit action against it.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Enrol one credential, confirm it authenticates, then enrol a second credential on a different
  device and re-test the first.
```
## G02-AUTH_PASSKEY-Q003

```yaml
QID: G02-AUTH_PASSKEY-Q003
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A user-supplied label for a credential is stored and displayed for that user's own reference and
  does not affect how the credential is evaluated at authentication time.
WHY_IT_MATTERS: >
  If a label influenced trust or matching, an attacker able to influence label text could
  manipulate authentication outcomes rather than merely aid user recognition.
DISCONFIRMING_OBSERVATION: >
  Changing a credential's label changes whether that credential is accepted, its assigned trust
  level, or which account it authenticates.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Enrol a credential, record its behaviour, rename its label to an unrelated value, and re-test
  authentication with no other change.
```
## G02-AUTH_PASSKEY-Q004

```yaml
QID: G02-AUTH_PASSKEY-Q004
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Revoking one credential belonging to an identity leaves every other credential belonging to that
  identity fully usable.
WHY_IT_MATTERS: >
  A revocation action is expected to be scoped to the specific compromised or retired device, not
  to silently sweep unrelated credentials.
DISCONFIRMING_OBSERVATION: >
  Revoking one credential causes another, untouched credential on the same identity to stop
  authenticating or to require re-enrolment.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Enrol two credentials on one identity, revoke one through the normal revocation path, then
  attempt authentication with the other.
```
## G02-AUTH_PASSKEY-Q005

```yaml
QID: G02-AUTH_PASSKEY-Q005
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Revoking an identity's only remaining device-bound credential produces one explicit, defined
  outcome — either a clearly defined fallback path is offered or the identity is left unable to
  complete that factor — and this outcome does not vary by accident of timing or interface used to
  revoke it.
WHY_IT_MATTERS: >
  An undefined outcome here becomes either an unplanned lockout of a legitimate user or, worse, a
  silent bypass of the intended factor requirement.
DISCONFIRMING_OBSERVATION: >
  Revoking the last remaining credential produces different outcomes depending on which supported
  interface performed the revocation, or leaves the identity's authentication requirement
  undefined rather than explicitly resolved.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Reduce an identity to exactly one enrolled credential, then revoke it through each supported
  interface in turn (self-service and administrative) and compare outcomes.
```
## G02-AUTH_PASSKEY-Q006

```yaml
QID: G02-AUTH_PASSKEY-Q006
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An identity that has lost access to its only enrolled device has a defined recovery path that
  does not require the device itself.
WHY_IT_MATTERS: >
  Without a recovery path, a lost or destroyed device permanently locks a legitimate user out,
  which becomes an operational and support burden severe enough to pressure weaker workarounds.
DISCONFIRMING_OBSERVATION: >
  An identity with no working device and no other accepted factor has no supported way to regain
  access short of an undocumented manual intervention.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Enrol a single credential for a test identity, simulate the device becoming unavailable, and
  attempt every documented recovery route.
```
## G02-AUTH_PASSKEY-Q007

```yaml
QID: G02-AUTH_PASSKEY-Q007
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Whatever recovery path exists for a lost device carries assurance comparable to the credential
  it replaces, and is not simply a lower-assurance factor left permanently available as a side
  door.
WHY_IT_MATTERS: >
  A recovery path weaker than the primary factor becomes the attacker's preferred target,
  defeating the purpose of requiring a phishing-resistant credential in the first place.
DISCONFIRMING_OBSERVATION: >
  The recovery path can be completed using only a factor materially weaker than a device-bound
  credential, and remains usable indefinitely rather than being a one-time, tightly scoped
  exception.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Trigger the recovery path for a test identity and record every piece of proof it actually
  demands, then check whether that same path remains available for repeated use afterward.
```
## G02-AUTH_PASSKEY-Q008

```yaml
QID: G02-AUTH_PASSKEY-Q008
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An administrator can revoke another identity's credential through a distinct administrative
  action, and that action is effective immediately, independent of whether the affected user is
  available to confirm it.
WHY_IT_MATTERS: >
  Emergency revocation (lost device, offboarding, suspected compromise) cannot depend on the
  affected user's cooperation or presence.
DISCONFIRMING_OBSERVATION: >
  An administrative revocation action either fails to take effect without the affected user's
  participation, or does not actually invalidate the credential for new authentication attempts.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  As an administrator, revoke a credential belonging to a different, currently logged-out
  identity, then attempt to authenticate as that identity using the revoked credential.
```
## G02-AUTH_PASSKEY-Q009

```yaml
QID: G02-AUTH_PASSKEY-Q009
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A device-bound credential remains permanently associated with the single identity and device
  pairing it was enrolled against, and cannot be reassigned to a different identity without a
  fresh enrolment ceremony.
WHY_IT_MATTERS: >
  Silent reassignment would let a credential migrate across identities, breaking the entire
  premise that the credential proves possession by one specific party.
DISCONFIRMING_OBSERVATION: >
  The same enrolled credential record becomes usable to authenticate a different identity than the
  one it was originally enrolled against, without a new enrolment ceremony against that identity.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Enrol a credential against one identity, then attempt any supported administrative or data-level
  action that might reassign, copy, or merge that credential record onto a second identity.
```
## G02-AUTH_PASSKEY-Q010

```yaml
QID: G02-AUTH_PASSKEY-Q010
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A policy requiring this factor applies equally to authentication performed through a
  programmatic or integration entry path, not only the interactive sign-in screen.
WHY_IT_MATTERS: >
  An integration path that never asks for the factor is a permanent bypass of the policy for
  anyone who can reach it.
DISCONFIRMING_OBSERVATION: >
  An identity subject to a mandatory-factor policy can complete a programmatic or integration
  authentication flow without ever satisfying that factor.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Configure the factor as mandatory for a test identity, then attempt authentication through every
  supported non-interactive entry path.
```
## G02-AUTH_PASSKEY-Q011

```yaml
QID: G02-AUTH_PASSKEY-Q011
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A scheduled or background process running under a given identity's authority is subject to the
  same factor policy as an interactive session for that identity, or is governed by an explicit,
  separately documented exception.
WHY_IT_MATTERS: >
  An unstated exception for automated access is an unmonitored gap that never shows up in
  interactive testing.
DISCONFIRMING_OBSERVATION: >
  A scheduled or background process authenticates and acts under an identity subject to a
  mandatory-factor policy without ever having satisfied that factor, and no documented exception
  covers the case.
EXPECTED_SURFACE: S3,S4,S8
PRECONDITIONS: >
  Identify a background or scheduled process that authenticates as a policy-covered identity and
  trace how that process establishes its authenticated context.
```
## G02-AUTH_PASSKEY-Q012

```yaml
QID: G02-AUTH_PASSKEY-Q012
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a support or administrative user assumes another identity's session ("acting as" that
  identity), the factor requirement already satisfied by the assuming user is not silently treated
  as satisfying that policy for the assumed identity's own record.
WHY_IT_MATTERS: >
  Conflating the supporter's authentication with the assumed identity's authentication would let
  impersonation quietly bypass a policy meant to gate that specific identity's access.
DISCONFIRMING_OBSERVATION: >
  An assumed-identity session is recorded, audited, or restricted identically to a session where
  that identity itself completed the required factor, with no distinguishing trace that
  impersonation occurred.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Have a support-privileged user assume a policy-covered identity's session and compare the
  resulting audit trail and effective restrictions to a session where that identity authenticated
  itself directly.
```
## G02-AUTH_PASSKEY-Q013

```yaml
QID: G02-AUTH_PASSKEY-Q013
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Changing the factor policy from optional to mandatory produces a defined, bounded transition for
  identities that have not yet enrolled — such as a grace period or a forced enrolment prompt —
  rather than an unannounced access cutoff or an unenforced mandate.
WHY_IT_MATTERS: >
  Flipping a switch that instantly locks out every non-enrolled user, or that claims to be
  mandatory while quietly admitting non-enrolled users, both represent governance failures around
  a security control.
DISCONFIRMING_OBSERVATION: >
  After the policy changes to mandatory, previously unenrolled identities are either cut off with
  no defined transition path, or continue to authenticate without ever completing enrolment.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  With a test identity that has never enrolled the factor, toggle the tenant policy from optional
  to mandatory and observe the identity's next authentication attempt.
```
## G02-AUTH_PASSKEY-Q014

```yaml
QID: G02-AUTH_PASSKEY-Q014
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A policy change made mandatory takes effect for sessions already open at the moment of the
  change according to an explicit, documented rule (either enforced at next re-authentication, or
  immediately terminated) rather than an undefined mixture of both.
WHY_IT_MATTERS: >
  Undefined behaviour for already-open sessions means the same policy change produces different
  real-world protection depending on unrelated timing.
DISCONFIRMING_OBSERVATION: >
  Two sessions open at the moment of the same policy change are treated differently from each
  other with no configuration or documented rule explaining the difference.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Open two sessions for the same policy scope, then toggle the mandatory policy and observe both
  sessions' subsequent behaviour under identical conditions.
```
## G02-AUTH_PASSKEY-Q015

```yaml
QID: G02-AUTH_PASSKEY-Q015
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Turning the factor off at the tenant level does not delete or silently invalidate previously
  enrolled credential records; they remain intact and become usable again if the policy is re-
  enabled.
WHY_IT_MATTERS: >
  Losing enrolment data on a policy toggle forces every user to re-enrol after any temporary
  policy experiment, which is disproportionate to a configuration change.
DISCONFIRMING_OBSERVATION: >
  Disabling the tenant-level policy and then re-enabling it requires previously enrolled users to
  enrol from scratch because their prior credential records no longer exist or no longer validate.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enrol a credential, disable the tenant policy, re-enable it, and attempt authentication with the
  originally enrolled credential.
```
## G02-AUTH_PASSKEY-Q016

```yaml
QID: G02-AUTH_PASSKEY-Q016
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The factor policy setting for one tenant has no effect on the factor requirement enforced for
  any other tenant sharing the same platform.
WHY_IT_MATTERS: >
  Cross-tenant policy leakage would mean one customer's security configuration silently changes
  another customer's exposure, which is a fundamental isolation failure.
DISCONFIRMING_OBSERVATION: >
  Changing the mandatory/optional policy setting for one tenant changes the observed enforcement
  for an identity in a different tenant.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure two tenants with opposite policy settings, then authenticate a representative identity
  in each and confirm each is governed only by its own tenant's setting.
```
## G02-AUTH_PASSKEY-Q017

```yaml
QID: G02-AUTH_PASSKEY-Q017
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The same physical device can hold independently enrolled credentials for identities in different
  tenants without either enrolment record being able to authenticate into the other tenant.
WHY_IT_MATTERS: >
  Reuse of the underlying hardware is normal; cross-tenant credential leakage from that reuse
  would be a boundary failure regardless of how the credential itself is implemented.
DISCONFIRMING_OBSERVATION: >
  A credential enrolled for an identity in one tenant successfully authenticates an identity in a
  different tenant.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Enrol the same physical device against a distinct identity in each of two tenants, then attempt
  to use each tenant's enrolment record to authenticate into the other tenant.
```
## G02-AUTH_PASSKEY-Q018

```yaml
QID: G02-AUTH_PASSKEY-Q018
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A single enrolment ceremony result can be permanently attached to exactly one identity record,
  and cannot be claimed or attached by a second identity, whether by coincidence or deliberate
  action.
WHY_IT_MATTERS: >
  A collision here would let one proof of possession quietly grant access to two separate
  identities, undermining every downstream assumption of one credential meaning one accountable
  person.
DISCONFIRMING_OBSERVATION: >
  The same enrolment ceremony outcome, or a copy of its resulting record, becomes attached to and
  usable for authenticating a second identity.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Attempt to complete or replay an enrolment ceremony's outcome against a second identity distinct
  from the one it was originally issued to.
```
## G02-AUTH_PASSKEY-Q019

```yaml
QID: G02-AUTH_PASSKEY-Q019
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Disabling or deprovisioning an identity's account invalidates its device-bound credentials at
  the same time as the account itself becomes unable to authenticate by any other means.
WHY_IT_MATTERS: >
  A credential surviving account deprovisioning is a live, working back door into a supposedly
  closed account.
DISCONFIRMING_OBSERVATION: >
  An identity's account is disabled or deprovisioned, yet one of its previously enrolled
  credentials still successfully authenticates afterward.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Enrol a credential for a test identity, deprovision that identity's account through the normal
  offboarding path, and immediately attempt authentication with the credential.
```
## G02-AUTH_PASSKEY-Q020

```yaml
QID: G02-AUTH_PASSKEY-Q020
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  There is no meaningful window between an account being deprovisioned and its credentials being
  rejected; the two happen effectively together rather than one lagging the other by a batch
  cycle.
WHY_IT_MATTERS: >
  A lagging window is a known, exploitable gap for anyone who anticipates their own offboarding or
  compromises credentials belonging to someone about to be offboarded.
DISCONFIRMING_OBSERVATION: >
  A credential belonging to a just-deprovisioned identity continues to authenticate successfully
  for a measurable period after deprovisioning completes.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Deprovision a test identity's account and, immediately and at short intervals afterward, attempt
  authentication with its previously valid credential, recording the exact point rejection begins.
```
## G02-AUTH_PASSKEY-Q021

```yaml
QID: G02-AUTH_PASSKEY-Q021
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Revoking the specific credential that established a currently open session results in that
  session being terminated, or an explicit, documented decision states that open sessions are
  intentionally allowed to continue until their own natural expiry.
WHY_IT_MATTERS: >
  An unstated, silent continuation of a session founded on a now-revoked credential defeats the
  purpose of the revocation for as long as that session happens to remain open.
DISCONFIRMING_OBSERVATION: >
  A session that was established using a credential later revoked continues to function normally
  with no policy anywhere documenting that outcome as intended.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Authenticate a session using a specific credential, revoke that same credential without ending
  the session, and continue using the session to observe whether and when it is affected.
```
## G02-AUTH_PASSKEY-Q022

```yaml
QID: G02-AUTH_PASSKEY-Q022
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An access token or similar artifact issued from a session established via a since-revoked
  credential does not remain independently usable to reach protected resources after the
  credential's revocation.
WHY_IT_MATTERS: >
  A token that outlives the credential that produced it becomes a hidden extension of an
  attacker's access window, invisible to anyone checking only the credential's own status.
DISCONFIRMING_OBSERVATION: >
  A token issued from a session tied to a since-revoked credential continues to grant access to
  protected resources after the revocation.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Establish a session with a credential, obtain any token or artifact that session issues, revoke
  the credential, and attempt to use the previously issued token independently of the original
  session.
```
## G02-AUTH_PASSKEY-Q023

```yaml
QID: G02-AUTH_PASSKEY-Q023
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeated failed completion attempts against the enrolment or authentication ceremony trigger a
  defined throttling or lockout behaviour, and that behaviour has a bound so it cannot be used to
  deny a legitimate user's access indefinitely by a third party who cannot otherwise authenticate.
WHY_IT_MATTERS: >
  A lockout mechanism intended to slow an attacker becomes, without a bound, a tool the attacker
  can use to deny service to the legitimate user instead.
DISCONFIRMING_OBSERVATION: >
  Enough attempts are triggered from outside the legitimate device or identity that the legitimate
  user is locked out for an unbounded or excessively long period with no self-service recovery.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Repeatedly trigger failed ceremony attempts against a test identity from a source other than its
  own enrolled device and observe the resulting lockout duration and recovery options.
```
## G02-AUTH_PASSKEY-Q024

```yaml
QID: G02-AUTH_PASSKEY-Q024
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A lockout counter accumulated against this factor is scoped explicitly (either shared with, or
  independent of, lockouts on other factors for the same identity) rather than interacting with
  other factors' counters in an undocumented way.
WHY_IT_MATTERS: >
  An undocumented shared counter means a failure on one factor can silently exhaust the allowance
  for an unrelated factor, producing confusing and hard-to-diagnose denial of access.
DISCONFIRMING_OBSERVATION: >
  Failed attempts against this factor measurably affect the lockout state of a different,
  unrelated authentication factor for the same identity with no documented link between them.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Trigger failed attempts against this factor for a test identity and then check whether an
  unrelated factor's own lockout counter for that identity has changed.
```
## G02-AUTH_PASSKEY-Q025

```yaml
QID: G02-AUTH_PASSKEY-Q025
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The freshness window used to accept a challenge-response exchange is evaluated using a time
  reference that is not vulnerable to an ordinary client-side clock difference causing a
  legitimate attempt to be rejected, or an attacker's clock manipulation extending the acceptance
  window.
WHY_IT_MATTERS: >
  A freshness check anchored to an untrusted client clock can either lock out honest users on
  slightly misconfigured devices or hand an attacker extra replay time by lying about the time.
DISCONFIRMING_OBSERVATION: >
  Setting a test device's clock a small, realistic amount out of sync with the reference time
  either rejects an otherwise legitimate attempt or measurably widens the window during which a
  captured exchange could be replayed.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Adjust a test device's clock by a modest, realistic offset in both directions and attempt the
  ceremony each time, measuring acceptance and the resulting freshness window.
```
## G02-AUTH_PASSKEY-Q026

```yaml
QID: G02-AUTH_PASSKEY-Q026
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Every successful enrolment of a new credential produces a retrievable audit record identifying
  the identity, the point in time, and that an enrolment (as distinct from an authentication)
  occurred.
WHY_IT_MATTERS: >
  Without a distinct enrolment record, an investigator cannot reconstruct when and how a new
  device gained standing access to an identity.
DISCONFIRMING_OBSERVATION: >
  A completed enrolment produces no retrievable record distinguishing it from an ordinary
  authentication event, or produces no record at all.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Complete an enrolment for a test identity and then search the available audit or log surface for
  a record of that specific event.
```
## G02-AUTH_PASSKEY-Q027

```yaml
QID: G02-AUTH_PASSKEY-Q027
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Every revocation of a credential produces a retrievable audit record identifying which
  credential was revoked, when, and through which actor or interface the revocation was performed.
WHY_IT_MATTERS: >
  Revocation is a security-relevant action; without attribution, a later dispute over who removed
  access cannot be resolved from the system's own records.
DISCONFIRMING_OBSERVATION: >
  A revocation action completes successfully but the resulting audit record does not identify the
  acting party, the interface used, or the specific credential affected.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Revoke a credential through both a self-service and an administrative interface in turn, and
  inspect the resulting audit records for actor attribution in each case.
```
## G02-AUTH_PASSKEY-Q028

```yaml
QID: G02-AUTH_PASSKEY-Q028
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Every successful authentication event using this factor records which specific credential was
  used, distinguishable from any other factor or credential the identity might also hold.
WHY_IT_MATTERS: >
  Investigating a suspected compromise requires knowing precisely which device authenticated a
  given session, not merely that "a factor" was satisfied.
DISCONFIRMING_OBSERVATION: >
  An authentication event's record does not identify which specific enrolled credential was used,
  when the identity holds more than one.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Enrol two credentials for one identity, authenticate using each in turn, and inspect whether the
  resulting records distinguish which credential was used on each occasion.
```
## G02-AUTH_PASSKEY-Q029

```yaml
QID: G02-AUTH_PASSKEY-Q029
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  An authentication record captures which version of the applicable factor policy was in force at
  the moment of that authentication, so a later dispute about what was required at the time can be
  resolved from the record itself.
WHY_IT_MATTERS: >
  Policy changes over time; without a recorded policy version tied to each event, a later audit
  cannot determine whether a given login complied with the rules in force when it happened.
DISCONFIRMING_OBSERVATION: >
  The factor policy is changed, and authentication events recorded before and after the change are
  indistinguishable from each other with respect to which policy applied.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Record an authentication event, change the applicable policy, record a second authentication
  event, and compare what each record states about the governing policy.
```
## G02-AUTH_PASSKEY-Q030

```yaml
QID: G02-AUTH_PASSKEY-Q030
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A configured limit on the number of credentials an identity may hold at once is actually
  enforced at the point of enrolment, not merely stated as a rule.
WHY_IT_MATTERS: >
  An unenforced limit is not a control at all; it exists only as documentation while the
  underlying system permits unlimited accumulation.
DISCONFIRMING_OBSERVATION: >
  An identity is able to enrol more credentials than the configured maximum permits, with no
  rejection or warning at the point the limit is exceeded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Configure a low maximum credential count for a test identity and attempt to enrol one more
  credential than that maximum allows.
```
## G02-AUTH_PASSKEY-Q031

```yaml
QID: G02-AUTH_PASSKEY-Q031
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An enrolment ceremony that fails partway through leaves no partial or orphaned credential record
  capable of later being completed or exploited.
WHY_IT_MATTERS: >
  A half-created credential record is an unaccounted-for artifact that later processes or
  attackers might mistakenly treat as valid or attempt to complete without the original context.
DISCONFIRMING_OBSERVATION: >
  After deliberately interrupting an enrolment ceremony partway through, a credential record for
  that attempt exists and either authenticates successfully or can later be completed without
  repeating the full ceremony.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Begin an enrolment ceremony and interrupt it after the initial step but before final
  confirmation, then inspect the identity's credential records and attempt authentication.
```
## G02-AUTH_PASSKEY-Q032

```yaml
QID: G02-AUTH_PASSKEY-Q032
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A user who explicitly cancels an in-progress enrolment leaves the identity's credential state
  unchanged from before the ceremony began.
WHY_IT_MATTERS: >
  A cancelled action should be a true no-op; any residual state from a cancelled ceremony is
  confusing at best and a latent security gap at worst.
DISCONFIRMING_OBSERVATION: >
  Cancelling an enrolment ceremony midway leaves behind a new credential record, a changed count
  of credentials, or an altered policy state for the identity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Record an identity's full credential state, begin an enrolment ceremony, explicitly cancel it
  before completion, and compare the resulting state to the original.
```
## G02-AUTH_PASSKEY-Q033

```yaml
QID: G02-AUTH_PASSKEY-Q033
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A credential that has been revoked cannot be returned to an active, authenticating state without
  the identity completing a new enrolment ceremony; there is no administrative "un-revoke" that
  reactivates the original credential record.
WHY_IT_MATTERS: >
  If revocation were reversible without a fresh proof of possession, a compromised device removed
  in response to a suspected takeover could simply be reinstated without re-establishing
  legitimate control.
DISCONFIRMING_OBSERVATION: >
  A previously revoked credential record becomes usable to authenticate again through any action
  short of a new enrolment ceremony.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Revoke a credential, then attempt every available administrative and self-service action that
  might restore it, and finally attempt authentication with the original credential.
```
## G02-AUTH_PASSKEY-Q034

```yaml
QID: G02-AUTH_PASSKEY-Q034
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An authentication attempt using a credential that has already been revoked is rejected outright,
  not merely deprioritized in favour of another factor or silently ignored while another path
  succeeds.
WHY_IT_MATTERS: >
  Silent tolerance of a revoked credential in the authentication flow means revocation has not
  actually closed the door it claims to close.
DISCONFIRMING_OBSERVATION: >
  Presenting a revoked credential during authentication results in successful access, whether
  directly or by falling through to an unintended alternate path.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Revoke a credential and then attempt to authenticate using exactly that credential with no other
  change to the identity's configuration.
```
## G02-AUTH_PASSKEY-Q035

```yaml
QID: G02-AUTH_PASSKEY-Q035
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A previously used and completed challenge-response exchange cannot be captured and replayed
  later to authenticate again.
WHY_IT_MATTERS: >
  Replay protection is the core property that makes this class of factor resistant to
  interception; its absence would reduce the factor to no better than a reusable secret.
DISCONFIRMING_OBSERVATION: >
  A captured, previously completed exchange is accepted a second time to establish a new
  authenticated session.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Capture the full exchange from one legitimate authentication attempt and resubmit it unmodified
  in a subsequent attempt.
```
## G02-AUTH_PASSKEY-Q036

```yaml
QID: G02-AUTH_PASSKEY-Q036
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Successfully authenticating with this factor does not itself satisfy or bypass an unrelated
  password-expiry or password-change requirement that would otherwise apply to the same identity.
WHY_IT_MATTERS: >
  If one control silently satisfies an unrelated control, an administrator who believes password
  expiry is being enforced would be wrong, without any indication that it is not.
DISCONFIRMING_OBSERVATION: >
  An identity subject to an outstanding password-expiry requirement is allowed to proceed normally
  after authenticating with this factor, with the expiry requirement never surfaced or enforced.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Place a test identity into an expired-password state, then authenticate using this factor and
  observe whether the password-expiry requirement is still enforced afterward.
```
## G02-AUTH_PASSKEY-Q037

```yaml
QID: G02-AUTH_PASSKEY-Q037
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where policy requires both this factor and an additional second factor, completing this factor
  alone does not satisfy the second-factor requirement; both are independently checked.
WHY_IT_MATTERS: >
  Layered controls exist because each addresses a different failure mode; one factor quietly
  covering for another collapses the intended layering without anyone deciding that trade-off
  deliberately.
DISCONFIRMING_OBSERVATION: >
  An identity subject to a policy requiring both this factor and a separate second factor is
  granted full access after satisfying only this factor.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Configure a test identity under a policy requiring both this factor and an independent second
  factor, then authenticate using only this factor and observe whether the second factor is still
  requested.
```
## G02-AUTH_PASSKEY-Q038

```yaml
QID: G02-AUTH_PASSKEY-Q038
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An identity that retains a working password alongside an enrolled device-bound credential does
  not thereby reduce the effective assurance level required to access the account, since either
  factor remaining reachable on its own would undercut the purpose of adding the stronger one.
WHY_IT_MATTERS: >
  If keeping the weaker factor available in parallel silently lowers the bar, enrolling the
  stronger factor gives a false sense of improved security while the weaker path remains fully
  exploitable.
DISCONFIRMING_OBSERVATION: >
  An identity with both a password and an enrolled device-bound credential can still be fully
  authenticated using the password alone, under a policy that was intended to require the stronger
  factor.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Enrol a device-bound credential for an identity that also retains a working password, then
  attempt authentication using only the password under the policy meant to mandate the stronger
  factor.
```
## G02-AUTH_PASSKEY-Q039

```yaml
QID: G02-AUTH_PASSKEY-Q039
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two enrolment requests submitted at effectively the same moment for one identity resolve into
  two distinct, individually valid credential records, or one is cleanly rejected — never a
  corrupted or duplicated single record.
WHY_IT_MATTERS: >
  A race condition in credential creation could produce an inconsistent record that either fails
  silently or, worse, grants unintended access.
DISCONFIRMING_OBSERVATION: >
  Submitting two enrolment requests for one identity at nearly the same time produces a corrupted
  credential record, a record that authenticates for the wrong device, or a system error that
  leaves the identity's credential state ambiguous.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit two enrolment ceremonies for the same identity as close together in time as the available
  interfaces allow, then inspect the resulting credential records.
```
## G02-AUTH_PASSKEY-Q040

```yaml
QID: G02-AUTH_PASSKEY-Q040
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a revocation of a credential and an authentication attempt using that same credential occur
  at nearly the same moment, the outcome is deterministically the revocation taking effect — the
  authentication attempt does not succeed merely by timing.
WHY_IT_MATTERS: >
  A race that occasionally favours the attacker's in-flight authentication over an administrator's
  revocation would make emergency revocation unreliable exactly when it matters most.
DISCONFIRMING_OBSERVATION: >
  Under near-simultaneous revocation and authentication using the same credential, the
  authentication succeeds in at least one observed trial.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Arrange a revocation action and an authentication attempt using the same credential to be
  submitted as close together in time as practically achievable, and repeat several trials.
```
## G02-AUTH_PASSKEY-Q041

```yaml
QID: G02-AUTH_PASSKEY-Q041
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A tenant-level policy requiring this factor is enforced identically across every supported login
  surface offered to that tenant's identities, not only the one most commonly tested.
WHY_IT_MATTERS: >
  A policy enforced on the main interface but silently absent on a secondary or less-used surface
  is a bypass waiting to be found.
DISCONFIRMING_OBSERVATION: >
  An identity subject to a mandatory-factor policy can complete authentication through one
  supported surface without satisfying the factor, while another surface correctly enforces it.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Configure the factor as mandatory for a test identity and attempt authentication in turn through
  every supported login surface offered.
```
## G02-AUTH_PASSKEY-Q042

```yaml
QID: G02-AUTH_PASSKEY-Q042
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Disabling this factor entirely at the tenant level has one clearly defined effect on existing
  enrolled credentials — either they are all explicitly invalidated as part of that action, or
  they are explicitly preserved and simply not required — and this is a deliberate configuration
  outcome, not an accidental byproduct.
WHY_IT_MATTERS: >
  An accidental, undocumented outcome here means administrators cannot predict or explain what
  happens to existing credentials when they change a top-level setting.
DISCONFIRMING_OBSERVATION: >
  Disabling the factor at the tenant level leaves existing credentials in a state that is neither
  documented as preserved nor documented as invalidated, and differs from what any available
  configuration description states.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enrol a credential, disable the factor at the tenant level, and check both the resulting
  credential record state and whether it matches any documented description of that setting's
  effect.
```
## G02-AUTH_PASSKEY-Q043

```yaml
QID: G02-AUTH_PASSKEY-Q043
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The error presented after a failed ceremony attempt does not disclose enough detail to let an
  outside party distinguish between "this is not a recognized device for this identity" and "this
  identity does not exist at all."
WHY_IT_MATTERS: >
  A distinguishing error response turns the authentication surface into a tool for enumerating
  valid identities, aiding a targeted attack against real accounts.
DISCONFIRMING_OBSERVATION: >
  Attempting the ceremony against a nonexistent identity produces a different observable response
  than attempting it with a valid identity and an unrecognized device.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Attempt the ceremony against a known nonexistent identity, then against a known valid identity
  using a device that was never enrolled, and compare the exact responses.
```
## G02-AUTH_PASSKEY-Q044

```yaml
QID: G02-AUTH_PASSKEY-Q044
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The metadata retained about an enrolled credential's device is limited to what is needed to
  manage and identify that credential, and does not include broader device fingerprinting
  information beyond that stated purpose.
WHY_IT_MATTERS: >
  Retaining more device detail than the stated management purpose requires expands the privacy and
  breach-exposure surface without a corresponding functional need.
DISCONFIRMING_OBSERVATION: >
  The stored record for a credential includes device-identifying detail beyond what is presented
  to the user or used for credential management, with no documented purpose for the additional
  detail.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Enrol a credential and, where inspection is possible, compare everything retained about the
  device against what is displayed to the user and what the management function actually uses.
```
## G02-AUTH_PASSKEY-Q045

```yaml
QID: G02-AUTH_PASSKEY-Q045
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing a credential's user-facing label through the self-service interface has no effect on
  any other property of that credential record, including its trust level, creation date, or last-
  used history.
WHY_IT_MATTERS: >
  A cosmetic action should not have side effects on security-relevant fields; any coupling here is
  unexpected and untested by ordinary use.
DISCONFIRMING_OBSERVATION: >
  Renaming a credential's label alters its recorded creation date, last-used history, or any
  property other than the label itself.
EXPECTED_SURFACE: S1,S5
PRECONDITIONS: >
  Record a credential's full set of visible properties, rename only its label, and compare the
  resulting record to the original.
```
## G02-AUTH_PASSKEY-Q046

```yaml
QID: G02-AUTH_PASSKEY-Q046
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The "last used" indicator on a credential record updates to reflect a genuinely recent
  authentication whenever that credential is actually used, so it cannot present a stale,
  reassuring picture of a credential that is in fact being actively used by someone other than its
  expected holder.
WHY_IT_MATTERS: >
  A stale or unreliable last-used indicator removes a key early-warning signal a user or
  administrator would otherwise rely on to notice unexpected use of a credential.
DISCONFIRMING_OBSERVATION: >
  A credential is used to authenticate successfully, but its recorded last-used indicator does not
  change, or changes to a time inconsistent with the actual authentication.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Note a credential's current last-used indicator, authenticate with it, and immediately re-check
  the indicator for an accurate update.
```
## G02-AUTH_PASSKEY-Q047

```yaml
QID: G02-AUTH_PASSKEY-Q047
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A credential's lifecycle state — pending enrolment, active, and revoked — is explicit and
  mutually exclusive, and no supported action moves a revoked credential directly back to active
  without passing through a fresh enrolment ceremony.
WHY_IT_MATTERS: >
  An ambiguous or reversible state model is exactly the kind of implementation detail most likely
  to hide a shortcut back to access that was meant to be permanently closed.
DISCONFIRMING_OBSERVATION: >
  A credential record is found, or can be placed, in a state that is not clearly one of pending,
  active, or revoked, or a revoked record transitions back to active without a new enrolment
  ceremony.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Move a credential through enrolment, active use, and revocation while inspecting its recorded
  state at each step, and attempt any available action that might reactivate it directly.
```
## G02-AUTH_PASSKEY-Q048

```yaml
QID: G02-AUTH_PASSKEY-Q048
MODULE: auth_passkey
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Revoking a single suspected-compromised credential is, by itself, immediately sufficient to
  fully deny further authentication attempts from that device, without depending on any batch,
  scheduled, or delayed background process to take effect.
WHY_IT_MATTERS: >
  If revocation only takes effect after a delayed background pass, the window between a compromise
  being discovered and the revocation actually closing the door is a live gap an attacker can use.
DISCONFIRMING_OBSERVATION: >
  A revoked credential continues to authenticate successfully for a measurable period until an
  unrelated scheduled or background process eventually applies the revocation.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Revoke a credential and immediately attempt authentication with it, then repeat the attempt at
  short intervals to determine whether any delay exists before it is consistently rejected.
```
