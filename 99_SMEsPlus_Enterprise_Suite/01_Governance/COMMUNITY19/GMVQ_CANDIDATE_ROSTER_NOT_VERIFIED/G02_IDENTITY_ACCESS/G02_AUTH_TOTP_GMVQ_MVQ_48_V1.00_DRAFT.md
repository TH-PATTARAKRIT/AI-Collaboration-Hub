# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / auth_totp Module Adversarial MVQ Bank

**Document ID:** GMVQ-G02-AUTH_TOTP-MVQ48-V1.00
**Group:** G02 IDENTITY_ACCESS
**Module Metadata:** `auth_totp`
**Wave:** W1
**Author Cell:** TEAM 12 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**Standing Authorization:** governs this production run under directive SMEPLUS-GMVQ-25TEAM-
ACCELERATION-20260927-001
**Lane A / Lane B:** NOT STARTED for this module until rolling batch freeze is recorded
**actual_mvq_count:** 48

## Purpose

This bank supplies module-specific research questions for the time-based one-time second factor
applied to internal users. It targets the ground where a time-bound, secret-based factor is
weakest in practice: the enrolment window, clock and drift handling, replay and single-use
guarantees, the recovery-code parallel path, per-role and per-tenant enforcement authority, non-
interactive and background entry paths, lockout as a denial vector, session and policy-change
semantics, and auditability of the authentication decision itself.

The question text is source-neutral. It does not expose vendor or product names, model or field
names, method names, XML IDs, API shapes, or any other implementation identifier, and it never
repeats the module's own metadata name outside the `MODULE:` field.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION` describing a failure state,
  never a restatement of the hypothesis.
- No padding: 48 questions exist because they test 48 distinct material hypotheses, spread across
  enrolment, clock/drift/replay, recovery codes, per-role and per-tenant enforcement, non-
  interactive access, lockout and denial-of-service, session and policy-change semantics, and
  auditability.
- Questions are not evidence. A later ANSWERED state requires an actual artifact or observation.
- `MODULE + QID` is a Research Evidence Join Key only; it does not by itself constitute coverage.
- This bank is DRAFT / AUTHORING COMPLETE / NOT FROZEN. It is not approved, not verified, and not
  MASTER-ready.

## G02-AUTH_TOTP-Q001

```yaml
QID: G02-AUTH_TOTP-Q001
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Between the moment a second-factor enrolment is initiated and the moment it is confirmed and
  activated, the account must not be treated as protected by the second factor for any
  authentication decision.
WHY_IT_MATTERS: >
  A window where the system believes protection exists that has not actually been activated
  creates a false sense of security and a bypassable gap.
DISCONFIRMING_OBSERVATION: >
  An authentication decision during the unconfirmed enrolment window is recorded or displayed as
  second-factor-protected, or a policy check treats the account as already compliant.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Begin second-factor enrolment for a test identity and inspect authentication and compliance
  state before confirming the first successful code.
```

## G02-AUTH_TOTP-Q002

```yaml
QID: G02-AUTH_TOTP-Q002
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If enrolment is started but never confirmed, the account must remain in the same protection
  state it held before enrolment began, with no partial or orphaned configuration left active.
WHY_IT_MATTERS: >
  An abandoned enrolment that leaves a half-active configuration can either falsely block a
  legitimate login or falsely leave an assumed-protected account unprotected.
DISCONFIRMING_OBSERVATION: >
  An abandoned, unconfirmed enrolment attempt changes a subsequent login outcome, or the account
  is later reported as having a second factor when none was completed.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Start enrolment, abandon before confirming, then attempt an ordinary login and inspect the
  account's factor status.
```

## G02-AUTH_TOTP-Q003

```yaml
QID: G02-AUTH_TOTP-Q003
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether enrolment may be initiated only by the account holder, only by an administrator, or by
  either, is an explicit configurable policy rather than an implicit default that varies by entry
  point.
WHY_IT_MATTERS: >
  An undocumented default determines who can put another person's account into a state requiring a
  credential the account holder does not yet possess.
DISCONFIRMING_OBSERVATION: >
  An administrator can complete enrolment on behalf of another identity without that identity's
  participation, with no policy setting governing whether this is permitted.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Attempt to initiate and complete enrolment for a second identity from an administrative account
  and check for a governing policy control.
```

## G02-AUTH_TOTP-Q004

```yaml
QID: G02-AUTH_TOTP-Q004
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Re-enrolling a replacement second factor while a prior one is active must not create a period in
  which either factor, old or new, is silently disabled without the account holder being informed.
WHY_IT_MATTERS: >
  A silent gap during factor replacement can leave the account effectively unprotected without
  anyone noticing.
DISCONFIRMING_OBSERVATION: >
  During replacement, a login attempt succeeds without any valid second factor being presented, or
  both the old and new factor are simultaneously rejected as invalid.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  With one factor active, begin enrolling a replacement and attempt logins at each step of the
  replacement sequence.
```

## G02-AUTH_TOTP-Q005

```yaml
QID: G02-AUTH_TOTP-Q005
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Two concurrent enrolment attempts for the same identity from different sessions must resolve to
  exactly one deterministic final configuration, never a merged or inconsistent one.
WHY_IT_MATTERS: >
  A race condition in credential setup can leave a secret known to two different setup flows,
  undermining the exclusivity the factor depends on.
DISCONFIRMING_OBSERVATION: >
  After two simultaneous enrolment attempts complete, the account accepts codes generated from
  both attempts' setup material, or the final state is ambiguous about which secret is active.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trigger two enrolment flows for the same identity from separate sessions at nearly the same time
  and inspect which secret is ultimately active.
```

## G02-AUTH_TOTP-Q006

```yaml
QID: G02-AUTH_TOTP-Q006
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The tolerance window for time-based code acceptance is a bounded, explicit value rather than an
  unbounded or silently widening allowance.
WHY_IT_MATTERS: >
  An unbounded or excessively wide acceptance window materially increases the number of codes that
  would validate at any moment, weakening the factor.
DISCONFIRMING_OBSERVATION: >
  A code generated well outside any documented or configured tolerance window is still accepted.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Generate a valid code, wait past a known or estimated tolerance boundary, and attempt to use it.
```

## G02-AUTH_TOTP-Q007

```yaml
QID: G02-AUTH_TOTP-Q007
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Advancing or retarding the server's own clock must not permit a previously issued code to remain
  valid indefinitely or become valid before its natural time.
WHY_IT_MATTERS: >
  A time-based factor whose validity can be manipulated by clock changes on the verifying side
  stops enforcing the freshness property it depends on.
DISCONFIRMING_OBSERVATION: >
  Deliberately shifting the verifying system's clock causes a code to validate outside the window
  it would have been valid for under the original clock.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Under a controlled test environment, shift the server clock forward and backward around a known
  code's window and attempt validation.
```

## G02-AUTH_TOTP-Q008

```yaml
QID: G02-AUTH_TOTP-Q008
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The validity of a time-based code does not depend on the timezone display setting of the user or
  the administrator, only on the underlying absolute time.
WHY_IT_MATTERS: >
  Confusing timezone display with the underlying validity calculation could cause avoidable
  lockouts or, worse, unintended widening of the acceptance window.
DISCONFIRMING_OBSERVATION: >
  Changing a user's or administrator's displayed timezone setting alone changes whether a given
  code is accepted.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Change the displayed timezone preference for a test identity without changing absolute time and
  attempt a previously-timed code.
```

## G02-AUTH_TOTP-Q009

```yaml
QID: G02-AUTH_TOTP-Q009
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A code, once successfully used to complete authentication, must not be accepted a second time
  even if it is presented again within its original validity window.
WHY_IT_MATTERS: >
  Without single-use enforcement, an intercepted or observed code remains usable by an attacker
  for the remainder of its window.
DISCONFIRMING_OBSERVATION: >
  The same code value is accepted for a second, separate authentication attempt while still inside
  its original time window.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Successfully authenticate with a code, then immediately reattempt authentication using the
  identical code value.
```

## G02-AUTH_TOTP-Q010

```yaml
QID: G02-AUTH_TOTP-Q010
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A code must not remain acceptable after its window has elapsed merely because of an
  implementation choice to compensate for clock skew that widens the effective window beyond the
  documented tolerance.
WHY_IT_MATTERS: >
  A skew-compensation mechanism that is more generous than declared quietly increases the attack
  surface without anyone having approved that trade-off.
DISCONFIRMING_OBSERVATION: >
  A code is accepted at an elapsed time that exceeds the documented tolerance window plus any
  declared skew allowance.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Determine the documented tolerance and skew allowance, then attempt a code just beyond that
  combined boundary.
```

## G02-AUTH_TOTP-Q011

```yaml
QID: G02-AUTH_TOTP-Q011
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A single valid code cannot be used to complete authentication on two different sessions or
  devices at effectively the same time.
WHY_IT_MATTERS: >
  If one code can authenticate two concurrent sessions, an intercepted code becomes more valuable
  to an attacker and single-use guarantees are meaningless.
DISCONFIRMING_OBSERVATION: >
  The same unused code successfully completes authentication on two different sessions started
  nearly simultaneously.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  From two separate sessions, submit the identical current code at nearly the same instant and
  observe both outcomes.
```

## G02-AUTH_TOTP-Q012

```yaml
QID: G02-AUTH_TOTP-Q012
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Each recovery code is single-use; once consumed to authenticate, that specific code must never
  authenticate again.
WHY_IT_MATTERS: >
  A reusable recovery code is a standing bypass of the primary factor rather than an emergency-
  only path.
DISCONFIRMING_OBSERVATION: >
  A previously used recovery code succeeds again on a later authentication attempt.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Use one recovery code to authenticate, then immediately attempt authentication again with the
  same recovery code.
```

## G02-AUTH_TOTP-Q013

```yaml
QID: G02-AUTH_TOTP-Q013
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Recovery codes are presented to the account holder at generation time and are not retrievable in
  cleartext through any later view of the account's second-factor configuration.
WHY_IT_MATTERS: >
  A recovery code retrievable later effectively becomes a standing static secret rather than a
  one-time emergency credential shown only once.
DISCONFIRMING_OBSERVATION: >
  A generated recovery code's cleartext value can be viewed again later through the configuration
  interface or an export.
EXPECTED_SURFACE: S1,S5,S6
PRECONDITIONS: >
  Generate a set of recovery codes, note one value, then attempt to view the same value again
  through the configuration interface later.
```

## G02-AUTH_TOTP-Q014

```yaml
QID: G02-AUTH_TOTP-Q014
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When all recovery codes have been consumed, the account has an explicit, defined path back to a
  second factor rather than silently falling back to no second factor at all.
WHY_IT_MATTERS: >
  Exhaustion is a foreseeable state; if the fallback from it is no factor required, the whole
  control degrades over time as codes are used.
DISCONFIRMING_OBSERVATION: >
  After the last recovery code is consumed, subsequent logins succeed with only the primary
  credential and no second factor is required or offered.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Consume every recovery code for a test identity in sequence and then attempt an ordinary login.
```

## G02-AUTH_TOTP-Q015

```yaml
QID: G02-AUTH_TOTP-Q015
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Generating a new set of recovery codes immediately invalidates every code from the previous set.
WHY_IT_MATTERS: >
  If an old set remains valid alongside a new one, a leaked historical set continues to be an
  active bypass indefinitely.
DISCONFIRMING_OBSERVATION: >
  A code from a previously generated set still authenticates successfully after a new set has been
  generated.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate a set of recovery codes, then regenerate a new set, then attempt to use a code from the
  original set.
```

## G02-AUTH_TOTP-Q016

```yaml
QID: G02-AUTH_TOTP-Q016
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Attempts to authenticate using a recovery code are subject to the same abuse-resistant
  throttling as attempts using the primary time-based code, not a looser regime.
WHY_IT_MATTERS: >
  A weaker throttle on the recovery path turns the emergency path into the easiest way to brute-
  force the second factor.
DISCONFIRMING_OBSERVATION: >
  A materially higher number of failed recovery-code attempts is tolerated before any throttling
  or lockout than failed time-based-code attempts.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Submit repeated invalid recovery codes and repeated invalid time-based codes against comparable
  accounts and compare the throttling point.
```

## G02-AUTH_TOTP-Q017

```yaml
QID: G02-AUTH_TOTP-Q017
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the second factor is required is governed by an explicit role- or scope-based policy,
  not by an implicit property of how a user happened to be created or invited.
WHY_IT_MATTERS: >
  Implicit enforcement is invisible to reviewers and can leave a whole class of accounts
  unprotected without any record of a decision to exempt them.
DISCONFIRMING_OBSERVATION: >
  Two accounts with the same assigned role and scope are found to differ in whether the second
  factor is enforced, with no policy setting explaining the difference.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Compare enforcement outcomes for multiple accounts sharing the same role and scope, created
  through different paths such as invitation, import, or direct creation.
```

## G02-AUTH_TOTP-Q018

```yaml
QID: G02-AUTH_TOTP-Q018
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Only an explicitly authorized administrative capability can exempt an account or role from the
  second-factor requirement; it is not obtainable through a broader unrelated permission.
WHY_IT_MATTERS: >
  If exemption rides along with an unrelated broad permission, the population able to weaken this
  control is larger than anyone intended or reviewed.
DISCONFIRMING_OBSERVATION: >
  An account holding a broad but unrelated permission can grant itself or another account an
  exemption without holding the specific exemption capability.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Identify the specific permission intended to control exemption, then attempt to exempt an
  account using only broader, unrelated permissions.
```

## G02-AUTH_TOTP-Q019

```yaml
QID: G02-AUTH_TOTP-Q019
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Granting or revoking an exemption from the second-factor requirement is recorded as a discrete,
  attributable, timestamped event.
WHY_IT_MATTERS: >
  Exemption is a security-relevant decision; without a record, no later review can establish who
  weakened enforcement for whom, or when.
DISCONFIRMING_OBSERVATION: >
  An exemption is granted or revoked and no corresponding attributable record of the change, its
  author, or its time exists afterward.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Grant an exemption to a test account, then revoke it, and search for an audit record of both
  changes.
```

## G02-AUTH_TOTP-Q020

```yaml
QID: G02-AUTH_TOTP-Q020
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The second-factor enforcement policy configured for one tenant does not affect, leak into, or
  get inherited by another tenant's configuration.
WHY_IT_MATTERS: >
  Cross-tenant configuration leakage in a security control could silently disable enforcement for
  a tenant that believes it is protected.
DISCONFIRMING_OBSERVATION: >
  Changing the enforcement policy in one tenant's configuration is observed to change the
  effective policy, default, or displayed setting in another tenant.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Set differing enforcement policies in two separate tenant configurations and verify each tenant
  only reflects its own setting.
```

## G02-AUTH_TOTP-Q021

```yaml
QID: G02-AUTH_TOTP-Q021
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Disabling an already-active second factor for an account requires either the account holder's
  own re-authentication or an explicit administrative capability, never an unauthenticated or
  weakly-authenticated path.
WHY_IT_MATTERS: >
  If disabling the factor is easier than the factor itself, an attacker who compromises the
  primary credential alone can strip the second factor and lock in access.
DISCONFIRMING_OBSERVATION: >
  The second factor can be disabled for an account without the account holder re-proving the
  second factor and without an administrator's explicit authorized action.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Attempt to disable an active second factor using only the primary credential's session, without
  re-presenting a valid second-factor code.
```

## G02-AUTH_TOTP-Q022

```yaml
QID: G02-AUTH_TOTP-Q022
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Disabling the second factor for an account leaves a durable record that it was once enrolled and
  later disabled, distinct from an account that never enrolled at all.
WHY_IT_MATTERS: >
  Without this distinction, a later review cannot tell a never-protected account from one whose
  protection was deliberately removed, which is a materially different risk story.
DISCONFIRMING_OBSERVATION: >
  After disabling, the account's history shows no distinguishable trace from an account that never
  had the second factor enrolled.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Enroll, then disable, the second factor for a test account and compare its historical record
  against a control account that never enrolled.
```

## G02-AUTH_TOTP-Q023

```yaml
QID: G02-AUTH_TOTP-Q023
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Disabling the second factor on an account forces re-authentication of any currently active
  sessions for that account rather than allowing them to continue silently under the old assurance
  level.
WHY_IT_MATTERS: >
  An active session that survives a downgrade in authentication assurance continues to carry a
  security guarantee that no longer actually holds.
DISCONFIRMING_OBSERVATION: >
  An already-active session continues operating normally after the account's second factor is
  disabled, with no forced re-authentication or session-level notice.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Establish an active session for an account with the second factor enabled, then disable the
  factor from another context and observe the first session's continued behavior.
```

## G02-AUTH_TOTP-Q024

```yaml
QID: G02-AUTH_TOTP-Q024
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An administrator disabling the second factor on behalf of a locked-out account holder produces
  the same attributable audit record as any other administrative disable action, naming the
  administrator and the affected account.
WHY_IT_MATTERS: >
  Support-driven bypass of the second factor is a common real-world weak point; without
  attribution, it is indistinguishable from an unreviewed backdoor.
DISCONFIRMING_OBSERVATION: >
  An administrator disables a second factor to unlock a user and the resulting record does not
  identify the acting administrator, the reason, or the time.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Simulate a locked-out account holder, have an administrator disable the factor to restore
  access, and inspect the resulting audit trail.
```

## G02-AUTH_TOTP-Q025

```yaml
QID: G02-AUTH_TOTP-Q025
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An access path that authenticates through a long-lived token or programmatic credential rather
  than an interactive login is still subject to the same second-factor policy decision recorded at
  the token's issuance, and does not bypass it.
WHY_IT_MATTERS: >
  If a programmatic path never has to satisfy the second-factor requirement, it becomes the
  preferred route for anyone seeking to avoid the control entirely.
DISCONFIRMING_OBSERVATION: >
  An account for which the second factor is required can obtain or use a programmatic access
  credential without ever having satisfied the second-factor requirement at issuance.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  For an account with the factor required, attempt to obtain or use a programmatic access
  credential and trace whether the factor requirement was enforced at any point.
```

## G02-AUTH_TOTP-Q026

```yaml
QID: G02-AUTH_TOTP-Q026
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a service or integration account is exempt from the second-factor requirement is an
  explicit, reviewable policy decision, not an automatic property of the account type.
WHY_IT_MATTERS: >
  Service accounts are frequently the highest-privilege, least-monitored identities in a system;
  an unreviewed automatic exemption there is a governance blind spot.
DISCONFIRMING_OBSERVATION: >
  A service or integration account is found exempt from the second-factor requirement with no
  discoverable policy record explaining or authorizing the exemption.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Identify a service or integration account and locate the specific policy record that governs its
  second-factor exemption status.
```

## G02-AUTH_TOTP-Q027

```yaml
QID: G02-AUTH_TOTP-Q027
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A scheduled or background process acting as a given identity does not itself constitute
  satisfying that identity's second-factor requirement, and does not grant that process privileges
  the identity could only reach after presenting the factor interactively.
WHY_IT_MATTERS: >
  If background execution silently inherits the full authority of a factor-protected identity, the
  control has a permanent, always-open bypass running unattended.
DISCONFIRMING_OBSERVATION: >
  A background process running under a factor-protected identity can perform an action that an
  interactive session for that identity could only perform after presenting a valid second factor.
EXPECTED_SURFACE: S4,S8
PRECONDITIONS: >
  Identify an action gated by the second-factor requirement in interactive use, then attempt the
  equivalent action from a scheduled or background execution context under the same identity.
```

## G02-AUTH_TOTP-Q028

```yaml
QID: G02-AUTH_TOTP-Q028
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A support or impersonation capability that lets one identity act as another records that the
  second factor was bypassed for that session, and does not silently present the session as fully
  self-authenticated by the original account holder.
WHY_IT_MATTERS: >
  Impersonation is a legitimate operational need, but if it is indistinguishable from a genuine
  self-authenticated session, it becomes an unaudited way to operate under a protected identity.
DISCONFIRMING_OBSERVATION: >
  A session created through impersonation of a factor-protected account is recorded or displayed
  identically to a session where that account authenticated itself with the second factor.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Use an impersonation or support-access capability against a factor-protected test identity and
  inspect how the resulting session is recorded and labeled.
```

## G02-AUTH_TOTP-Q029

```yaml
QID: G02-AUTH_TOTP-Q029
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  There is a defined, finite number of consecutive failed second-factor attempts after which
  further attempts are throttled or blocked, rather than an unlimited number of guesses being
  possible.
WHY_IT_MATTERS: >
  Without a bound on attempts, the numeric range of a short time-based code becomes practically
  guessable.
DISCONFIRMING_OBSERVATION: >
  A large number of consecutive incorrect codes can be submitted for one account with no
  throttling, delay, or lockout ever engaging.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Submit a long sequence of incorrect codes for a single test account and observe whether and when
  a limiting response engages.
```

## G02-AUTH_TOTP-Q030

```yaml
QID: G02-AUTH_TOTP-Q030
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An unauthenticated or low-privilege actor cannot lock a legitimate account holder out of the
  second-factor step merely by submitting failed guesses without ever possessing the correct
  primary credential.
WHY_IT_MATTERS: >
  If knowing only a username can trigger a lockout, the control becomes a tool for denying service
  to any known account.
DISCONFIRMING_OBSERVATION: >
  An actor who has not supplied a valid primary credential can still trigger a lockout of the
  second-factor step for a targeted account.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Without a valid primary credential, attempt to trigger repeated second-factor failures against a
  targeted account and observe whether lockout still engages.
```

## G02-AUTH_TOTP-Q031

```yaml
QID: G02-AUTH_TOTP-Q031
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A lockout triggered in one access scope or entry path for an identity is either intentionally
  shared everywhere as a single documented state, or intentionally isolated per scope; it is not
  an accidental mix of both.
WHY_IT_MATTERS: >
  An inconsistent lockout scope can leave one entry path open while the account holder believes
  the whole account is locked, or vice versa.
DISCONFIRMING_OBSERVATION: >
  A lockout triggered through one entry path is found to still permit second-factor attempts
  through a different entry path for the same identity, with no policy documenting this as
  intended.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Trigger a lockout for an identity through one entry path, then attempt second-factor
  authentication for the same identity through a different entry path.
```

## G02-AUTH_TOTP-Q032

```yaml
QID: G02-AUTH_TOTP-Q032
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Clearing a lockout state requires an explicit, attributable administrative action or a defined
  automatic expiry, not an incidental side effect of an unrelated operation.
WHY_IT_MATTERS: >
  If an unrelated action silently clears a lockout, the control's timing guarantee is unreliable
  and unreviewable.
DISCONFIRMING_OBSERVATION: >
  A lockout is observed to clear as a side effect of an unrelated administrative or system action,
  with no record of an explicit reset or documented automatic expiry.
EXPECTED_SURFACE: S4,S6,S7
PRECONDITIONS: >
  Trigger a lockout, perform various unrelated administrative operations on the account, and
  observe whether any of them clears the lockout without explicit intent.
```

## G02-AUTH_TOTP-Q033

```yaml
QID: G02-AUTH_TOTP-Q033
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Newly requiring the second factor for a role or scope that previously did not require it is
  applied to already-active sessions within a bounded, defined grace period, not left to apply
  only at the next fresh login indefinitely.
WHY_IT_MATTERS: >
  An unbounded grace period means a policy decision to close a gap has no practical effect until
  sessions happen to expire on their own, which could be a very long time.
DISCONFIRMING_OBSERVATION: >
  An already-active session for a newly in-scope role continues indefinitely without ever being
  required to satisfy the new second-factor policy.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Establish an active session under a role, then change policy to require the second factor for
  that role, and observe how long the existing session remains unaffected.
```

## G02-AUTH_TOTP-Q034

```yaml
QID: G02-AUTH_TOTP-Q034
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether the second factor is required once per session establishment or repeatedly at defined
  intervals within a long-lived session is an explicit configured behavior, not an accidental
  consequence of session length.
WHY_IT_MATTERS: >
  A session that never re-checks the factor over its full lifetime effectively reduces a strong
  control to a one-time gate regardless of how long the session persists.
DISCONFIRMING_OBSERVATION: >
  A session of unusually long duration is never asked to re-present the second factor despite an
  intended periodic re-verification policy.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Establish a long-lived session and monitor whether and when the second factor is re-requested
  according to the documented policy.
```

## G02-AUTH_TOTP-Q035

```yaml
QID: G02-AUTH_TOTP-Q035
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An action defined as sensitive enough to require fresh proof of the second factor cannot be
  completed using only the ambient session's earlier authentication.
WHY_IT_MATTERS: >
  Step-up requirements exist specifically because ambient session trust is not considered
  sufficient for certain actions; skipping the fresh check defeats that design.
DISCONFIRMING_OBSERVATION: >
  A designated sensitive action completes successfully without a fresh second-factor prompt,
  relying solely on the existing session's earlier authentication.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Identify an action documented as requiring step-up second-factor verification and attempt it
  using only an existing session's ambient authentication.
```

## G02-AUTH_TOTP-Q036

```yaml
QID: G02-AUTH_TOTP-Q036
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Every successful authentication event records which specific factor type was used to satisfy the
  second-factor requirement, distinguishing the primary time-based method from a recovery code.
WHY_IT_MATTERS: >
  Without this distinction, a review cannot tell routine authentication from use of the weaker
  emergency path, which matters for both security monitoring and incident response.
DISCONFIRMING_OBSERVATION: >
  The authentication log for a successful login does not indicate whether a time-based code or a
  recovery code was used to satisfy the second factor.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Authenticate once using the time-based method and once using a recovery code, then compare the
  two resulting log entries.
```

## G02-AUTH_TOTP-Q037

```yaml
QID: G02-AUTH_TOTP-Q037
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an authentication decision is made under a specific version of the enforcement policy, that
  version is identifiable after the fact, even after the policy is later changed.
WHY_IT_MATTERS: >
  Without recording which policy applied at the time, a later dispute or investigation cannot
  establish whether the system behaved correctly according to the rules in force then.
DISCONFIRMING_OBSERVATION: >
  After the enforcement policy is changed, there is no way to determine which version of the
  policy applied to a specific historical authentication decision.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Record an authentication decision under one policy version, change the policy, and attempt to
  determine which version governed the earlier decision.
```

## G02-AUTH_TOTP-Q038

```yaml
QID: G02-AUTH_TOTP-Q038
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Every change to the second-factor enforcement configuration is attributed to a specific actor
  and timestamped, regardless of which interface or path was used to make the change.
WHY_IT_MATTERS: >
  A security policy that can be changed without attribution cannot be trusted to reflect an
  authorized decision, and cannot support any later accountability review.
DISCONFIRMING_OBSERVATION: >
  A change to the enforcement configuration made through at least one available path leaves no
  attributable, timestamped record of who made it.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change the enforcement configuration through each available administrative path and check for an
  attributable audit record after each.
```

## G02-AUTH_TOTP-Q039

```yaml
QID: G02-AUTH_TOTP-Q039
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A failed second-factor attempt is logged as distinct from a failed primary-credential attempt,
  so the two cannot be confused during a security review.
WHY_IT_MATTERS: >
  Conflating the two failure types would hide the specific signal of an attacker who already has a
  valid primary credential and is now probing the second factor.
DISCONFIRMING_OBSERVATION: >
  A failed second-factor attempt appears in logs indistinguishably from a failed primary-
  credential attempt.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Produce one failed primary-credential attempt and one failed second-factor attempt with a
  correct primary credential, and compare the resulting log entries.
```

## G02-AUTH_TOTP-Q040

```yaml
QID: G02-AUTH_TOTP-Q040
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Resetting or changing the primary credential does not itself weaken, bypass, or disable the
  second factor; the two controls act independently.
WHY_IT_MATTERS: >
  If a credential reset flow silently drops the second-factor requirement, the reset path becomes
  the easiest way to strip a protected account down to a single factor.
DISCONFIRMING_OBSERVATION: >
  Completing a primary credential reset for a factor-protected account results in the account no
  longer requiring the second factor on the next login.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Complete a primary credential reset for an account with the second factor enrolled, then attempt
  a subsequent login.
```

## G02-AUTH_TOTP-Q041

```yaml
QID: G02-AUTH_TOTP-Q041
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Enabling the second factor for an account does not have the side effect of relaxing or disabling
  an unrelated existing access control on that account.
WHY_IT_MATTERS: >
  A control that trades away an unrelated protection as a hidden side effect creates a net-
  negative security change disguised as an improvement.
DISCONFIRMING_OBSERVATION: >
  After enabling the second factor, an unrelated pre-existing access restriction on the same
  account is found relaxed or removed with no documented reason.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Record all active access restrictions on a test account, enable the second factor, and compare
  the restriction set afterward.
```

## G02-AUTH_TOTP-Q042

```yaml
QID: G02-AUTH_TOTP-Q042
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When an account holder's device has drifted enough to make codes consistently invalid, the
  system offers a defined, discoverable recovery path rather than an undocumented dead end.
WHY_IT_MATTERS: >
  A predictable failure mode with no documented recovery path drives account holders toward
  insecure workarounds such as sharing credentials with support staff informally.
DISCONFIRMING_OBSERVATION: >
  An account holder whose device clock has drifted beyond tolerance has no discoverable,
  documented path to regain access other than an informal, unrecorded workaround.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Simulate a device with clock drift wide enough to always fail validation and attempt to find a
  documented recovery path from the standard interface.
```

## G02-AUTH_TOTP-Q043

```yaml
QID: G02-AUTH_TOTP-Q043
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If enrolment fails partway through due to an interruption, no partial secret or configuration is
  left in a state that could later be silently activated or reused.
WHY_IT_MATTERS: >
  A dangling partial secret from an interrupted enrolment is an unreviewed and easily forgotten
  artifact that could later be exploited if it ever becomes reachable.
DISCONFIRMING_OBSERVATION: >
  After an enrolment flow is deliberately interrupted partway through, a partial secret or
  configuration is later found still present and usable.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Begin enrolment and deliberately interrupt the flow partway through, then inspect the account's
  stored configuration afterward.
```

## G02-AUTH_TOTP-Q044

```yaml
QID: G02-AUTH_TOTP-Q044
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When an account's overall access is revoked or its underlying identity is deactivated, its
  second-factor configuration is deactivated with it, not left independently functional.
WHY_IT_MATTERS: >
  A second factor that keeps functioning after the identity it protects has been revoked is a
  dangling credential with no legitimate purpose left to serve.
DISCONFIRMING_OBSERVATION: >
  After an account's access is revoked, its second-factor configuration can still be used to
  complete an authentication step somewhere in the system.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Revoke or deactivate a test account's access and then attempt to use its previously valid second
  factor in any reachable authentication step.
```

## G02-AUTH_TOTP-Q045

```yaml
QID: G02-AUTH_TOTP-Q045
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If an enrolment request and a disable request for the same account's second factor are submitted
  at nearly the same time, the final state is one deterministic, well-defined outcome, not an
  inconsistent or corrupted configuration.
WHY_IT_MATTERS: >
  An indeterminate outcome from a race between opposing security-relevant operations could leave
  the account in a state nobody intended and nobody can explain later.
DISCONFIRMING_OBSERVATION: >
  Racing an enrolment request against a disable request for the same account produces a final
  state that is inconsistent, corrupted, or does not match either requested outcome.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit an enrolment completion and a disable request for the same account's second factor at
  nearly the same time and inspect the resulting state.
```

## G02-AUTH_TOTP-Q046

```yaml
QID: G02-AUTH_TOTP-Q046
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If this second-factor mechanism is only meaningfully offered to certain classes of user, any
  other class of user reaching the same protected resources is still held to an equivalent
  effective assurance level, not a silently weaker one.
WHY_IT_MATTERS: >
  A protection that only some routes into the same data actually enforce is not a real boundary;
  it is a gap dressed up as a control.
DISCONFIRMING_OBSERVATION: >
  A user class not covered by this second-factor mechanism can reach the same protected resources
  as a covered user class with a lower actual assurance level and no compensating control.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Identify which user classes this factor is offered to, then determine whether excluded classes
  can reach the same protected resources some other way.
```

## G02-AUTH_TOTP-Q047

```yaml
QID: G02-AUTH_TOTP-Q047
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The declared or configured acceptance window boundary matches what is actually enforced at
  runtime, with no unexplained gap between the documented behavior and the observed behavior.
WHY_IT_MATTERS: >
  A mismatch between a documented control parameter and its actual enforcement is exactly the kind
  of gap this study exists to surface before anyone relies on the documentation.
DISCONFIRMING_OBSERVATION: >
  A configured or documented tolerance value differs from the boundary actually observed when
  testing codes at and just past that boundary.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Read the configured or documented tolerance value, then empirically test codes at, just before,
  and just after that boundary.
```

## G02-AUTH_TOTP-Q048

```yaml
QID: G02-AUTH_TOTP-Q048
MODULE: auth_totp
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Every distinct way of establishing an authenticated session for a factor-protected account is
  actually gated by the second-factor requirement at runtime, with no entry path silently exempted
  by omission rather than by an explicit, reviewed decision.
WHY_IT_MATTERS: >
  A control that covers most but not all entry paths gives false confidence; the uncovered path
  becomes the de facto way around the control.
DISCONFIRMING_OBSERVATION: >
  At least one distinct way of establishing an authenticated session for a factor-protected
  account succeeds without ever presenting a valid second factor, and no reviewed decision
  documents that exemption.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Enumerate every distinct way of establishing an authenticated session for the tested identity
  and attempt each without presenting a second factor.
```
