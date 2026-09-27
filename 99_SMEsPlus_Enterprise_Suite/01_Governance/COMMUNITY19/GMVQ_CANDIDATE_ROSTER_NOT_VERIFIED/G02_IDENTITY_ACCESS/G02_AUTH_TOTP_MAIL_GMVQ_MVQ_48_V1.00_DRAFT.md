# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / auth_totp_mail Module Adversarial MVQ Bank

**Document ID:** GMVQ-G02-AUTH_TOTP_MAIL-MVQ48-V1.00
**Group:** G02 IDENTITY_ACCESS
**Module Metadata:** `auth_totp_mail`
**Wave:** W1
**Author Cell:** TEAM 12 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**Standing Authorization:** governs this production run under directive SMEPLUS-GMVQ-25TEAM-
ACCELERATION-20260927-001
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded
**actual_mvq_count:** 48

## Purpose

This bank supplies module-specific research questions for the second factor delivered over a
messaging channel in place of an authenticator. It targets the ground where a delivered-code
design differs from a locally generated one: channel collapse with the primary-credential reset
path, destination-address trust and change control, delivery failure/delay/duplication, code
validity anchored to delivery latency, rate limiting as both an abuse and a denial-of-service
surface, and whether this channel may be configured as a fallback that silently downgrades a
stronger enrolled factor.

The question text is source-neutral. It does not expose vendor or product names, model or field
names, method names, XML IDs, API shapes, or any other implementation identifier, and it never
repeats the module's own metadata name outside the `MODULE:` field.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a failure state,
  never a restatement of the hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across
  channel-collapse risk, destination trust and change control, delivery failure and timing, rate
  limiting and abuse, fallback/downgrade configuration, non-interactive access, tenancy, and
  auditability.
- Questions are not evidence. A later ANSWERED state requires an actual artifact or observation.
- `MODULE + QID` is a Research Evidence Join Key only; it does not by itself constitute coverage.
- This bank is DRAFT / AUTHORING COMPLETE / NOT FROZEN. It is not approved, not verified, and not
  MASTER-ready.

## G02-AUTH_TOTP_MAIL-Q001

```yaml
QID: G02-AUTH_TOTP_MAIL-Q001
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The messaging channel used to deliver the second-factor code is not the same channel that can be
  used to reset or recover the primary credential, unless that overlap is an explicit, reviewed
  policy decision.
WHY_IT_MATTERS: >
  If both factors route through the same channel, compromising that one channel defeats both
  factors at once, collapsing two-factor protection into one.
DISCONFIRMING_OBSERVATION: >
  The destination used to deliver the second-factor code is found to be the same destination that
  can independently be used to reset the primary credential, with no documented policy addressing
  the overlap.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Identify the destination used for second-factor delivery and separately test whether the primary
  credential can be reset through the same destination.
```

## G02-AUTH_TOTP_MAIL-Q002

```yaml
QID: G02-AUTH_TOTP_MAIL-Q002
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A destination address is not trusted to receive live authentication codes until it has itself
  been confirmed as reachable and controlled by the account holder.
WHY_IT_MATTERS: >
  An unconfirmed destination could belong to someone other than the account holder, in which case
  sending live codes there defeats the purpose of the factor entirely.
DISCONFIRMING_OBSERVATION: >
  A live authentication code is delivered to a destination address that has not yet completed its
  own confirmation step.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Add a new destination address without completing its confirmation step and attempt to trigger a
  live authentication code to it.
```

## G02-AUTH_TOTP_MAIL-Q003

```yaml
QID: G02-AUTH_TOTP_MAIL-Q003
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Between adding a destination address and confirming it, the account is not treated as having an
  active second factor for any policy or compliance check.
WHY_IT_MATTERS: >
  Treating an unconfirmed destination as an active factor creates a false compliance signal
  exactly like an incomplete enrolment elsewhere in the system.
DISCONFIRMING_OBSERVATION: >
  An account with only an unconfirmed destination address is reported or treated as second-factor-
  compliant by a policy or compliance check.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Add an unconfirmed destination address to a test account and inspect its reported second-factor
  compliance state.
```

## G02-AUTH_TOTP_MAIL-Q004

```yaml
QID: G02-AUTH_TOTP_MAIL-Q004
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Changing the destination address used for this factor requires some proof of control derived
  through the previously registered destination, or an equivalent strong re-authentication, before
  the change takes effect.
WHY_IT_MATTERS: >
  Without this, anyone who gains temporary access to the account can silently redirect all future
  second-factor codes to a destination they control.
DISCONFIRMING_OBSERVATION: >
  The destination address can be changed to a new value without any verification step involving
  the previously registered destination or an equivalent strong re-authentication.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt to change the registered destination address using only the current session, without
  triggering any verification through the old destination.
```

## G02-AUTH_TOTP_MAIL-Q005

```yaml
QID: G02-AUTH_TOTP_MAIL-Q005
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Every change to the registered destination address is recorded as an attributable, timestamped
  event, including the fact that a change occurred, even if the new value is not retained in
  cleartext.
WHY_IT_MATTERS: >
  A silent, unrecorded redirection of the delivery destination is the single most direct way to
  hijack this factor without touching the primary credential at all.
DISCONFIRMING_OBSERVATION: >
  The destination address is changed and no attributable, timestamped record of that change exists
  afterward.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change the registered destination address for a test account and search for a corresponding
  audit record.
```

## G02-AUTH_TOTP_MAIL-Q006

```yaml
QID: G02-AUTH_TOTP_MAIL-Q006
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing the destination address does not retroactively affect a code already in flight for a
  login that started before the change, and does not silently redirect an in-progress
  authentication attempt.
WHY_IT_MATTERS: >
  A mid-flight redirection of an authentication attempt in progress could hand a legitimate
  login's code to a different destination without the account holder noticing.
DISCONFIRMING_OBSERVATION: >
  A code requested before a destination address change is delivered to, or otherwise reachable at,
  the newly changed destination instead of the one active when it was requested.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a code request, change the destination address before the code is used, and observe
  where the outstanding code is ultimately delivered or valid.
```

## G02-AUTH_TOTP_MAIL-Q007

```yaml
QID: G02-AUTH_TOTP_MAIL-Q007
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The system distinguishes between a code being generated and a code being confirmed delivered,
  and does not leave an account holder with no path forward when delivery silently fails.
WHY_IT_MATTERS: >
  A factor that depends entirely on an external delivery step that can fail invisibly must have a
  defined behavior for that failure, or it becomes an unpredictable lockout mechanism.
DISCONFIRMING_OBSERVATION: >
  A delivery failure produces no distinguishable system behavior from a successful delivery,
  leaving the account holder unable to tell whether to wait, retry, or seek another path.
EXPECTED_SURFACE: S3,S5,S6
PRECONDITIONS: >
  Simulate a delivery failure at the transport level and observe what the account holder is shown
  and what options remain available.
```

## G02-AUTH_TOTP_MAIL-Q008

```yaml
QID: G02-AUTH_TOTP_MAIL-Q008
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Requesting a fresh delivery after a prior one is not confirmed received either issues a
  genuinely new code that supersedes the old one, or clearly resends the identical outstanding
  code, and the two are not silently conflated in a way that leaves multiple different valid codes
  active at once by accident.
WHY_IT_MATTERS: >
  Accidentally-active multiple codes widen the set of values that would validate at any moment,
  weakening the factor without anyone deciding that trade-off.
DISCONFIRMING_OBSERVATION: >
  After a retry, more than one distinct code value is found simultaneously valid for the same
  pending authentication attempt with no documented policy permitting that.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a code request, then trigger a retry before using the first code, and test whether both
  resulting values remain valid.
```

## G02-AUTH_TOTP_MAIL-Q009

```yaml
QID: G02-AUTH_TOTP_MAIL-Q009
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The validity window for a code is set with enough margin, or is measured from delivery rather
  than generation, such that realistic delivery delay does not routinely cause a code to arrive
  already expired.
WHY_IT_MATTERS: >
  A factor that fails by design under ordinary delivery latency creates a denial of access that
  has nothing to do with any actual security compromise.
DISCONFIRMING_OBSERVATION: >
  A code is observed to arrive after its own validity window has already elapsed under a
  realistic, non-adversarial delivery delay.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Introduce a realistic delivery delay and measure the elapsed time between generation and actual
  receipt against the documented validity window.
```

## G02-AUTH_TOTP_MAIL-Q010

```yaml
QID: G02-AUTH_TOTP_MAIL-Q010
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If two authentication attempts for the same account are started in close succession, the system
  has a defined, consistent rule for which resulting code, if any, remains valid, rather than an
  unpredictable outcome.
WHY_IT_MATTERS: >
  An unpredictable outcome here directly causes account holder confusion and support burden, and
  could also mask an attacker triggering a parallel attempt.
DISCONFIRMING_OBSERVATION: >
  Two authentication attempts started in close succession result in an outcome where it cannot be
  determined, even by the system's own design, which delivered code is the valid one.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger two authentication attempts for the same account in close succession and determine which
  delivered code, if either, is accepted.
```

## G02-AUTH_TOTP_MAIL-Q011

```yaml
QID: G02-AUTH_TOTP_MAIL-Q011
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Once a new code has been issued for an account's pending authentication, any earlier still-
  unexpired code for the same pending attempt is invalidated, rather than leaving multiple
  historical codes simultaneously acceptable.
WHY_IT_MATTERS: >
  Accumulating multiple simultaneously valid historical codes widens the acceptance surface in a
  way nobody explicitly decided on.
DISCONFIRMING_OBSERVATION: >
  An older code from an earlier request in the same pending attempt still succeeds after a newer
  code has been issued for that same attempt.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger two sequential code requests for the same pending attempt without using the first, then
  attempt to use the first, older code.
```

## G02-AUTH_TOTP_MAIL-Q012

```yaml
QID: G02-AUTH_TOTP_MAIL-Q012
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The point in time from which a code's validity window is measured, generation versus confirmed
  delivery, is an explicit, documented design choice, not an accidental artifact of
  implementation.
WHY_IT_MATTERS: >
  Which anchor is used materially changes how much of the validity window is actually usable once
  delivery latency is accounted for, and that trade-off should be a deliberate decision.
DISCONFIRMING_OBSERVATION: >
  The actual anchor point used for validity cannot be determined to match any documented design
  choice, or differs from what is documented.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Measure the actual validity window boundary against both the generation timestamp and the
  delivery timestamp and compare against documentation.
```

## G02-AUTH_TOTP_MAIL-Q013

```yaml
QID: G02-AUTH_TOTP_MAIL-Q013
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A clock discrepancy between the component that generates the code and the component that
  delivers or reports on it does not itself cause valid codes to be rejected or invalid codes to
  be accepted.
WHY_IT_MATTERS: >
  A distributed system with more than one clock in its delivery path introduces a skew risk that a
  single-component design would not have, and it must be accounted for explicitly.
DISCONFIRMING_OBSERVATION: >
  A code that should be valid under the generating component's clock is rejected, or one that
  should be expired is accepted, due to a discrepancy with another component's clock in the
  delivery path.
EXPECTED_SURFACE: S3,S8
PRECONDITIONS: >
  Where feasible in a controlled environment, introduce a clock discrepancy between delivery-
  related components and test codes near their validity boundary.
```

## G02-AUTH_TOTP_MAIL-Q014

```yaml
QID: G02-AUTH_TOTP_MAIL-Q014
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The action that triggers sending a code to a destination is rate-limited per account and per
  destination such that an actor cannot cause an unbounded number of deliveries to be sent.
WHY_IT_MATTERS: >
  Each delivery carries a real-world cost and can constitute harassment of the destination's
  owner; unbounded triggering turns a security feature into an abuse vector.
DISCONFIRMING_OBSERVATION: >
  A large number of code-send requests can be triggered for the same account or destination in a
  short period with no rate limit engaging.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Repeatedly trigger the code-send action for the same account and destination in quick succession
  and observe whether limiting engages.
```

## G02-AUTH_TOTP_MAIL-Q015

```yaml
QID: G02-AUTH_TOTP_MAIL-Q015
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rate limit intended to prevent abuse of the send action cannot itself be triggered by an
  attacker against a specific victim account in a way that then prevents the legitimate account
  holder from receiving their own code when needed.
WHY_IT_MATTERS: >
  If the anti-abuse control and the legitimate user share the same limited resource, an attacker
  can weaponize the protection itself to lock out the real account holder.
DISCONFIRMING_OBSERVATION: >
  An actor without valid credentials can exhaust the send-rate limit for a targeted account such
  that the legitimate account holder's own subsequent, legitimate code request is refused.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Without valid credentials, repeatedly trigger send requests against a targeted account up to its
  limit, then attempt a legitimate send request as the account holder.
```

## G02-AUTH_TOTP_MAIL-Q016

```yaml
QID: G02-AUTH_TOTP_MAIL-Q016
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When two distinct accounts share the same destination address, sending activity or rate-limit
  consumption triggered by one account is isolated from the other account's ability to receive and
  use its own codes.
WHY_IT_MATTERS: >
  Shared destinations are a realistic real-world scenario, such as a shared mailbox or a shared
  line; a limiter that does not separate them lets one account's activity deny service to another.
DISCONFIRMING_OBSERVATION: >
  Sending activity for one account exhausts a limit or otherwise prevents delivery for a second,
  unrelated account that happens to share the same destination.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Configure two distinct accounts to share one destination address, exhaust sending activity from
  one, and test delivery for the other.
```

## G02-AUTH_TOTP_MAIL-Q017

```yaml
QID: G02-AUTH_TOTP_MAIL-Q017
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Configuring this channel as an available fallback for accounts that already use a stronger
  second-factor method does not silently make the weaker channel usable to satisfy the requirement
  for those accounts without an explicit, separate decision to allow it.
WHY_IT_MATTERS: >
  A security assurance level is only as strong as its weakest accepted path; a fallback enabled
  system-wide can quietly undercut every stronger factor already deployed.
DISCONFIRMING_OBSERVATION: >
  An account enrolled in a stronger second-factor method can complete authentication using this
  messaging-based channel instead, with no separate, explicit decision permitting that account to
  use the fallback.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Enroll a test account in a stronger method, then enable the messaging-based channel as a system
  fallback, and attempt authentication using only the fallback channel.
```

## G02-AUTH_TOTP_MAIL-Q018

```yaml
QID: G02-AUTH_TOTP_MAIL-Q018
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an authentication succeeds, the record of that event distinctly identifies whether the
  messaging-based channel or a stronger enrolled method was actually used to satisfy the
  requirement.
WHY_IT_MATTERS: >
  Without this distinction, a security review cannot tell whether the strong method deployed for
  an account is actually being used in practice, or quietly bypassed via the fallback every time.
DISCONFIRMING_OBSERVATION: >
  A successful authentication record does not indicate which specific factor type was actually
  used when more than one is enrolled for that account.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  For an account enrolled in both a stronger method and this channel, authenticate once using each
  and compare the resulting log entries.
```

## G02-AUTH_TOTP_MAIL-Q019

```yaml
QID: G02-AUTH_TOTP_MAIL-Q019
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Enabling this channel as a fallback for an account is either a self-service choice made by the
  account holder or an explicit administrative decision, and which of the two applies is a
  deliberate, documented policy rather than an ambiguous default.
WHY_IT_MATTERS: >
  If it is unclear who controls this choice, an administrator could weaken an individual account's
  assurance level without the account holder's knowledge or consent, or vice versa.
DISCONFIRMING_OBSERVATION: >
  The fallback can be enabled for an account by an actor other than the one the documented policy
  names as the authorized decision-maker.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Identify the documented policy for who may enable this fallback, then attempt to enable it from
  a different actor's context.
```

## G02-AUTH_TOTP_MAIL-Q020

```yaml
QID: G02-AUTH_TOTP_MAIL-Q020
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If an account holder later enrolls a stronger second-factor method, the previously available
  messaging-based fallback either remains available only by an explicit, separate re-decision, or
  is automatically removed as an accepted path, rather than continuing to be silently accepted
  alongside the new stronger method.
WHY_IT_MATTERS: >
  An account holder who believes they have upgraded to a stronger method may not realize the
  weaker path is still open and could still be exploited through it.
DISCONFIRMING_OBSERVATION: >
  After enrolling a stronger method, the account still accepts the messaging-based channel to
  satisfy the requirement with no separate decision having kept it enabled.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Enroll a test account first in the messaging-based channel, then in a stronger method, and
  attempt authentication using only the original channel afterward.
```

## G02-AUTH_TOTP_MAIL-Q021

```yaml
QID: G02-AUTH_TOTP_MAIL-Q021
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If this module offers its own emergency backup codes independent of live delivery, each such
  code is single-use and is invalidated after one successful authentication.
WHY_IT_MATTERS: >
  A reusable backup code under this channel would be a standing bypass exactly as it would be for
  any other second-factor method.
DISCONFIRMING_OBSERVATION: >
  A backup code issued under this channel succeeds a second time after having already been used
  once.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  If backup codes exist for this channel, use one to authenticate and immediately attempt to reuse
  the same value.
```

## G02-AUTH_TOTP_MAIL-Q022

```yaml
QID: G02-AUTH_TOTP_MAIL-Q022
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a given role or scope is permitted to satisfy its second-factor requirement using this
  messaging-based channel, as opposed to being required to use a stronger method, is an explicit,
  reviewable policy rather than an incidental default.
WHY_IT_MATTERS: >
  If higher-privilege roles can quietly default into the weaker channel, the accounts with the
  most to protect end up with the weakest realistic assurance.
DISCONFIRMING_OBSERVATION: >
  A higher-privilege role is found able to rely on this channel to satisfy its requirement with no
  policy record addressing whether that is intended for that role.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Identify a higher-privilege role and test whether it can complete its second-factor requirement
  using only this channel, then check for a governing policy.
```

## G02-AUTH_TOTP_MAIL-Q023

```yaml
QID: G02-AUTH_TOTP_MAIL-Q023
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A programmatic or non-interactive access path for an account whose second factor is satisfied
  through this channel cannot obtain equivalent access without ever having a code delivered and
  consumed through that channel at issuance.
WHY_IT_MATTERS: >
  If a programmatic path never has to go through delivery and consumption, it becomes a bypass of
  the very mechanism this channel is meant to enforce.
DISCONFIRMING_OBSERVATION: >
  A programmatic or non-interactive credential is issued for an account requiring this channel's
  factor without any delivery-and-consumption step occurring at issuance.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  For an account whose requirement is satisfied via this channel, attempt to obtain a programmatic
  access credential and trace whether delivery and consumption occurred.
```

## G02-AUTH_TOTP_MAIL-Q024

```yaml
QID: G02-AUTH_TOTP_MAIL-Q024
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The credential-reset flow, which is among the most sensitive operations an account can perform,
  does not rely solely on the same channel used for the second factor to prove the requester's
  identity.
WHY_IT_MATTERS: >
  If the single most sensitive recovery action and the second factor both reduce to control of one
  channel, the entire two-factor design collapses precisely at the moment it matters most.
DISCONFIRMING_OBSERVATION: >
  The credential-reset flow can be completed using only proof of control of the same destination
  used for the second factor, with no additional distinct verification.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt a full credential-reset flow for an account and identify every verification step used,
  checking whether any step other than the shared channel is required.
```

## G02-AUTH_TOTP_MAIL-Q025

```yaml
QID: G02-AUTH_TOTP_MAIL-Q025
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A session or elevated access is not granted until the delivered code has actually been correctly
  presented back by the account holder, not merely once a send has been attempted.
WHY_IT_MATTERS: >
  Granting access on the assumption that delivery will succeed, rather than on proof that it did
  and was used correctly, defeats the purpose of requiring the factor at all.
DISCONFIRMING_OBSERVATION: >
  An authenticated session or elevated state is granted after a send is triggered but before any
  correct code has been presented back by the account holder.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a code send and inspect the account's session or access state before submitting any code
  back.
```

## G02-AUTH_TOTP_MAIL-Q026

```yaml
QID: G02-AUTH_TOTP_MAIL-Q026
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Newly requiring this factor for a role or scope that previously did not require it is applied to
  already-active sessions within a bounded, defined grace period.
WHY_IT_MATTERS: >
  An unbounded grace period means closing a gap has no practical effect until sessions happen to
  end on their own.
DISCONFIRMING_OBSERVATION: >
  An already-active session for a newly in-scope role continues indefinitely without the new
  requirement for this channel ever being enforced.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Establish an active session under a role, then change policy to require this channel's factor
  for that role, and observe how long the session remains unaffected.
```

## G02-AUTH_TOTP_MAIL-Q027

```yaml
QID: G02-AUTH_TOTP_MAIL-Q027
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Disabling this factor for an account requires either the account holder's own re-authentication
  or an explicit administrative capability, and the action leaves a durable, attributable record
  distinct from an account that never enrolled.
WHY_IT_MATTERS: >
  A quietly disabled factor with no trace is indistinguishable from one that was never protected,
  hiding a deliberate weakening from later review.
DISCONFIRMING_OBSERVATION: >
  The factor is disabled without the account holder re-proving it and without an attributable
  administrative record, or the resulting state is indistinguishable from never having enrolled.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Enroll, then disable, this factor for a test account through each available path and inspect the
  resulting record and required authorization at each.
```

## G02-AUTH_TOTP_MAIL-Q028

```yaml
QID: G02-AUTH_TOTP_MAIL-Q028
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If this channel is the only second factor an account has enrolled, disabling it either falls
  back to a defined, policy-required alternative or is itself blocked by policy, rather than
  silently leaving the account with no second factor at all when one is still required.
WHY_IT_MATTERS: >
  A required control that can be silently reduced to nothing by disabling its only enrolled
  instance is not actually enforced.
DISCONFIRMING_OBSERVATION: >
  An account for which a second factor is policy-required ends up with no active second factor
  after disabling this channel, with no block or forced alternative enrolment.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  For an account whose only enrolled factor is this channel, and for which policy requires a
  second factor, attempt to disable it.
```

## G02-AUTH_TOTP_MAIL-Q029

```yaml
QID: G02-AUTH_TOTP_MAIL-Q029
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The sending identity and any associated cost or usage accounting for this channel are isolated
  per tenant, such that one tenant's configuration or usage does not appear under, or draw
  against, another tenant's.
WHY_IT_MATTERS: >
  Cross-tenant leakage of sending configuration or cost attribution is both a privacy boundary
  failure and a billing integrity failure.
DISCONFIRMING_OBSERVATION: >
  A message sent under one tenant's configuration is found attributed to, billed to, or configured
  using another tenant's sending identity or usage accounting.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure distinct sending identities for two tenants, trigger sends from each, and verify
  attribution and accounting remain separated.
```

## G02-AUTH_TOTP_MAIL-Q030

```yaml
QID: G02-AUTH_TOTP_MAIL-Q030
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  High sending volume generated by one tenant does not materially delay or degrade delivery timing
  for another tenant sharing the same underlying delivery infrastructure, at least not without a
  defined fairness policy.
WHY_IT_MATTERS: >
  If one tenant's volume can push another tenant's codes past their validity window, a shared
  resource becomes an indirect denial-of-service path between unrelated customers.
DISCONFIRMING_OBSERVATION: >
  A surge in sending volume from one tenant is observed to measurably delay delivery timing for
  another tenant's codes, with no fairness or isolation mechanism documented.
EXPECTED_SURFACE: S8
PRECONDITIONS: >
  Generate a high volume of sends for one tenant while measuring delivery timing for a second
  tenant on the same infrastructure.
```

## G02-AUTH_TOTP_MAIL-Q031

```yaml
QID: G02-AUTH_TOTP_MAIL-Q031
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  There is a defined, finite number of consecutive incorrect code submissions after which further
  attempts against this channel's pending authentication are throttled or blocked.
WHY_IT_MATTERS: >
  Without a bound, the limited character space of a short delivered code becomes practically
  guessable within its validity window.
DISCONFIRMING_OBSERVATION: >
  A large number of consecutive incorrect codes can be submitted for one pending authentication
  with no throttling, delay, or lockout ever engaging.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Submit a long sequence of incorrect codes against a single pending authentication and observe
  whether a limiting response engages.
```

## G02-AUTH_TOTP_MAIL-Q032

```yaml
QID: G02-AUTH_TOTP_MAIL-Q032
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Whether a lockout triggered on this channel's code attempts shares state with, or is independent
  of, the primary credential's own lockout mechanism is an explicit, documented design choice.
WHY_IT_MATTERS: >
  An undocumented interaction between the two lockout mechanisms could produce either an easier
  combined denial-of-service path or an unexpected gap where one lockout does not actually block
  the other path.
DISCONFIRMING_OBSERVATION: >
  The actual relationship between the two lockout mechanisms, once tested, does not match any
  documented description of that relationship.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Trigger a lockout on this channel's code attempts and separately test whether the primary
  credential path is also affected, then compare against documentation.
```

## G02-AUTH_TOTP_MAIL-Q033

```yaml
QID: G02-AUTH_TOTP_MAIL-Q033
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Every authentication event that used this channel records which destination address was used, in
  a form sufficient to support a later investigation, without necessarily storing the message
  content itself.
WHY_IT_MATTERS: >
  Without recording the destination used, an investigation cannot later determine whether a login
  was authenticated through a destination the account holder still controls.
DISCONFIRMING_OBSERVATION: >
  An authentication event completed through this channel leaves no record of which destination
  address was used.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Complete an authentication using this channel and inspect the resulting log entry for
  destination information.
```

## G02-AUTH_TOTP_MAIL-Q034

```yaml
QID: G02-AUTH_TOTP_MAIL-Q034
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The history of which destination addresses have been registered for an account over time is
  retained for audit purposes, independent of whether any delivered message content is retained or
  redacted.
WHY_IT_MATTERS: >
  Destination history is what lets an investigation reconstruct whether a takeover happened
  through an address change, and it must survive even strict message-content redaction policies.
DISCONFIRMING_OBSERVATION: >
  After a destination address change, no historical record of the previous destination remains
  available even though message-content retention policy is unrelated to that history.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Change the destination address for a test account and, separately from any message-content
  retention setting, check for retained address history.
```

## G02-AUTH_TOTP_MAIL-Q035

```yaml
QID: G02-AUTH_TOTP_MAIL-Q035
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A delivered code is not retrievable in cleartext from any stored copy of the message once its
  validity window has elapsed, whether through an inbox-like view, an export, or a support tool.
WHY_IT_MATTERS: >
  A code that remains retrievable after its window closes could still be used if the underlying
  single-use and expiry checks have any independent weakness, and its lingering presence is an
  unnecessary exposure.
DISCONFIRMING_OBSERVATION: >
  A stored copy of a previously delivered message reveals the code's cleartext value after its
  validity window has elapsed.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  After a code's validity window elapses, attempt to retrieve its cleartext value from any stored
  copy of the delivered message.
```

## G02-AUTH_TOTP_MAIL-Q036

```yaml
QID: G02-AUTH_TOTP_MAIL-Q036
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Explicitly requesting that a code be resent invalidates the previously delivered code for that
  same pending attempt, rather than leaving both simultaneously valid.
WHY_IT_MATTERS: >
  Leaving both valid after an explicit resend request widens the acceptance surface without a
  corresponding decision to accept that trade-off.
DISCONFIRMING_OBSERVATION: >
  After explicitly requesting a resend, the original, previously delivered code still succeeds.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger an initial code delivery, then explicitly request a resend, then attempt to use the
  original code.
```

## G02-AUTH_TOTP_MAIL-Q037

```yaml
QID: G02-AUTH_TOTP_MAIL-Q037
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two near-simultaneous requests for a code on the same pending authentication resolve
  deterministically to one clearly valid outcome, not an ambiguous or racing state.
WHY_IT_MATTERS: >
  An ambiguous outcome under concurrency is both a usability failure and a sign that the
  underlying state management cannot be relied on for a security-relevant decision.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous requests produce a state where it cannot be determined which resulting
  code, if either, is actually valid.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  From two separate devices or sessions, request a code for the same pending authentication at
  nearly the same instant and determine the resulting valid state.
```

## G02-AUTH_TOTP_MAIL-Q038

```yaml
QID: G02-AUTH_TOTP_MAIL-Q038
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the underlying delivery infrastructure for this channel is entirely unreachable, the
  account holder is not left with an unrecoverable, undocumented dead end; a defined alternative
  path exists or the condition is clearly surfaced.
WHY_IT_MATTERS: >
  A single point of infrastructure failure that silently locks out every account depending on it
  is a resiliency and availability risk on top of a security one.
DISCONFIRMING_OBSERVATION: >
  With the delivery infrastructure simulated as entirely unreachable, an affected account holder
  has no documented alternative path and receives no clear indication of what has failed.
EXPECTED_SURFACE: S3,S5,S8
PRECONDITIONS: >
  Simulate complete unavailability of the delivery infrastructure and attempt authentication as an
  affected account holder.
```

## G02-AUTH_TOTP_MAIL-Q039

```yaml
QID: G02-AUTH_TOTP_MAIL-Q039
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a send is accepted by the transport layer but never actually reaches the destination, the
  system's internal state reflects this distinctly from a fully successful delivery, rather than
  assuming success.
WHY_IT_MATTERS: >
  Assuming success on partial failure leaves the account holder waiting indefinitely for a code
  that will never arrive, with no system-level awareness of the problem.
DISCONFIRMING_OBSERVATION: >
  A send that is accepted by the transport layer but never delivered is recorded or treated by the
  system identically to a fully successful delivery.
EXPECTED_SURFACE: S1,S6,S8
PRECONDITIONS: >
  Simulate a transport-accepted but undelivered send and inspect the resulting internal state
  compared to a genuinely successful delivery.
```

## G02-AUTH_TOTP_MAIL-Q040

```yaml
QID: G02-AUTH_TOTP_MAIL-Q040
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a destination address change and an in-progress code request race against each other, the
  code is never delivered to a destination that is no longer the account's registered one at the
  moment of send.
WHY_IT_MATTERS: >
  Delivering a live code to a just-superseded destination during a race condition could hand
  access to whoever previously controlled that destination.
DISCONFIRMING_OBSERVATION: >
  A code is delivered to the previous destination address after that address has already been
  superseded by a completed address change.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger a code request and a destination address change at nearly the same time and determine
  which destination actually receives the code.
```

## G02-AUTH_TOTP_MAIL-Q041

```yaml
QID: G02-AUTH_TOTP_MAIL-Q041
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where this channel is also used somewhere in the primary-credential reset flow, completing a
  reset does not itself silently satisfy or bypass the separate second-factor requirement for that
  same login.
WHY_IT_MATTERS: >
  If one delivered message can be reused to satisfy two supposedly independent security decisions,
  the two controls are not actually independent.
DISCONFIRMING_OBSERVATION: >
  Completing a primary-credential reset through this channel allows the following login to proceed
  without separately satisfying the second-factor requirement.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Complete a primary-credential reset using this channel for a factor-protected test account, then
  attempt the next login.
```

## G02-AUTH_TOTP_MAIL-Q042

```yaml
QID: G02-AUTH_TOTP_MAIL-Q042
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A support or impersonation capability that lets one identity act as another either goes through
  an equivalent delivery-and-consumption step for this channel, or is recorded as an explicit
  bypass; it is not silently indistinguishable from the account holder's own authentication.
WHY_IT_MATTERS: >
  An unflagged bypass through impersonation is an unaudited way to operate as the protected
  identity without ever touching the factor meant to guard it.
DISCONFIRMING_OBSERVATION: >
  A session created through impersonation of an account requiring this channel is recorded
  identically to one where the account holder authenticated through the channel themselves.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Use an impersonation or support-access capability against a test identity requiring this channel
  and inspect how the resulting session is recorded.
```

## G02-AUTH_TOTP_MAIL-Q043

```yaml
QID: G02-AUTH_TOTP_MAIL-Q043
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  If this channel is enabled as a requirement without a valid, working sending configuration in
  place, the system fails closed by blocking the affected logins with a clear condition, rather
  than failing open by allowing logins through without ever actually delivering or checking a
  code.
WHY_IT_MATTERS: >
  A misconfiguration that silently fails open turns a security requirement into a no-op the moment
  the sending setup breaks, with no one aware the control has stopped functioning.
DISCONFIRMING_OBSERVATION: >
  With the sending configuration deliberately broken or absent, an account for which this channel
  is required is still able to complete authentication without ever presenting a valid code.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Deliberately misconfigure or remove the sending identity configuration and attempt
  authentication for an account requiring this channel.
```

## G02-AUTH_TOTP_MAIL-Q044

```yaml
QID: G02-AUTH_TOTP_MAIL-Q044
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the system offers any explicit action to revoke or cancel an already-issued code before its
  natural expiry, that revocation is actually enforced against subsequent use of the code.
WHY_IT_MATTERS: >
  A revocation control that does not actually prevent later use of the revoked value gives a false
  sense of having closed off an exposed code.
DISCONFIRMING_OBSERVATION: >
  A code explicitly revoked or cancelled before its natural expiry still succeeds on a later
  attempt.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  If a revocation action exists, issue a code, revoke it before it would naturally expire, and
  attempt to use it.
```

## G02-AUTH_TOTP_MAIL-Q045

```yaml
QID: G02-AUTH_TOTP_MAIL-Q045
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Whether this channel is offered to external, non-employee users under the same or a different
  policy than internal users is an explicit, documented decision, not an unreviewed side effect of
  how the two user populations happen to be configured.
WHY_IT_MATTERS: >
  An unreviewed weaker regime for external users, who by definition are less known to the
  organization, could expose internal-facing data through the less-scrutinized population.
DISCONFIRMING_OBSERVATION: >
  The actual policy applied to external users for this channel differs from what is documented, or
  no documentation addresses the external population at all.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Compare the documented policy for this channel against its actual behavior for an external, non-
  employee test account.
```

## G02-AUTH_TOTP_MAIL-Q046

```yaml
QID: G02-AUTH_TOTP_MAIL-Q046
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The response an unauthenticated actor receives when attempting to trigger a send for a given
  identifier does not reveal, through timing or content differences, whether that identifier
  corresponds to a real account.
WHY_IT_MATTERS: >
  An observable difference here lets an attacker enumerate valid accounts as a first step toward a
  targeted attack, without needing any valid credential.
DISCONFIRMING_OBSERVATION: >
  The system's response to a send-trigger request for a known-valid identifier is measurably or
  visibly different from its response for a nonexistent identifier.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Trigger the send action for a known-valid identifier and for a nonexistent one, and compare
  timing and content of the responses.
```

## G02-AUTH_TOTP_MAIL-Q047

```yaml
QID: G02-AUTH_TOTP_MAIL-Q047
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A destination address in the process of being added, but not yet confirmed, cannot be used to
  receive a live authentication code for an unrelated, already-in-progress login on that same
  account.
WHY_IT_MATTERS: >
  If an in-progress unconfirmed address can intercept a live authentication code, the confirmation
  requirement is not actually preventing an unverified destination from participating in real
  authentication.
DISCONFIRMING_OBSERVATION: >
  A destination address still awaiting confirmation is found capable of receiving a live code for
  an unrelated, already-in-progress authentication attempt on the same account.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Begin adding a new, unconfirmed destination address while a separate authentication attempt is
  in progress, and observe where its code is deliverable.
```

## G02-AUTH_TOTP_MAIL-Q048

```yaml
QID: G02-AUTH_TOTP_MAIL-Q048
MODULE: auth_totp_mail
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Every distinct way of establishing an authenticated session for an account requiring this
  channel's factor is actually gated by it at runtime, with no entry path silently exempted by
  omission.
WHY_IT_MATTERS: >
  A control enforced only at the interactive login page while other entry paths remain open gives
  false confidence and hands an attacker the easiest way around it.
DISCONFIRMING_OBSERVATION: >
  At least one distinct way of establishing an authenticated session for an account requiring this
  channel's factor succeeds without ever completing a delivery-and-consumption step, and no
  reviewed decision documents that exemption.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Enumerate every distinct way of establishing an authenticated session for the tested identity
  and attempt each without completing the channel's delivery-and-consumption step.
```
