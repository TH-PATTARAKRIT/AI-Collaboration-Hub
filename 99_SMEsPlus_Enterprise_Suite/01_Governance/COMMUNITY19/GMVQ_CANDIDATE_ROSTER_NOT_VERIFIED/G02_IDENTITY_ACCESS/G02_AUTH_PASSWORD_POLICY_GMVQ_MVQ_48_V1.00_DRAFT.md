# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / auth_password_policy Module MVQ Bank

**Document ID:** GMVQ-G02-AUTH_PASSWORD_POLICY-MVQ48-V1.00  
**Group:** G02 IDENTITY_ACCESS  
**Module Metadata:** `auth_password_policy`  
**Wave:** W1  
**Author Cell:** TEAM 10 (GMVQ Question Factory — Primary MVQ Authoring)  
**Review Cell:** PENDING  
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN / REVISED R1  
**CHANGE_REASON (R1):** Returned by GMVQ MASTER AUDIT TEAM M2 under Boss directive SMEPLUS-GMVQ-20P-5AUDIT-20260927-004 — closed-vocabulary (RISK_TIER / OUTPUT_CLASS) field-value defect(s) corrected by production (R1). 1 RISK_TIER value (LOW) outside the enum re-tiered to MEDIUM.
**actual_mvq_count:** 48  
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies module-specific research questions (MVQ) for the blind two-lane study, extending the 55-question standard bank for this module. It targets the internal-user secret policy regime: strength, reuse, expiry and lockout rules, how a policy change reaches existing secrets and live sessions, enforcement at every entry path (not only the interactive one), per-tenant isolation of configuration, and auditability of which policy version governed a given decision.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: each question tests a distinct material hypothesis; none is cut to hit a round number.
- Question text is source-neutral: no vendor or product name, no technical identifier, and no reference to the module's own metadata name anywhere outside the `MODULE:` field.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence from Lane A or Lane B.
- `MODULE + QID` is only a Research Evidence Join Key; no formal coverage is derived from this bank alone.
- This document is PREPARED ONLY / NOT APPROVED / NOT FROZEN. It is not Boss Final Approval.

## G02-AUTH_PASSWORD_POLICY-Q001

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q001
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A minimum secret-strength rule is enforced identically at every path capable of setting or
  replacing an internal user's secret, not only the primary interactive form.
WHY_IT_MATTERS: >
  A strength rule that only guards one entry path gives a false sense of protection while a weaker
  or unchecked path remains fully exploitable.
DISCONFIRMING_OBSERVATION: >
  A secret that fails the minimum-strength rule through the primary interactive path is
  nevertheless accepted through another supported path (for example an administrative screen, a
  bulk-provisioning path, or a documented interface).
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Identify every path capable of setting a secret for an internal identity; attempt to set a
  below-minimum secret through each one and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY-Q002

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q002
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Complexity requirements apply the same way regardless of the client or channel used to submit
  the new secret.
WHY_IT_MATTERS: >
  A client-specific gap becomes the attacker's preferred channel and defeats the stated policy
  without any configuration change.
DISCONFIRMING_OBSERVATION: >
  A secret rejected by one client submitting the change is accepted when the identical value is
  submitted through a different supported client or channel.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Submit an identical non-conforming secret through two distinct supported channels for the same
  identity and compare acceptance.
```

## G02-AUTH_PASSWORD_POLICY-Q003

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q003
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A configured reuse restriction prevents an identity from returning to a secret it used within
  the defined history window.
WHY_IT_MATTERS: >
  Without an effective reuse check, a forced rotation policy becomes cosmetic because a user can
  simply alternate between two values.
DISCONFIRMING_OBSERVATION: >
  An identity successfully re-adopts a secret it held within the configured history window.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a distinctive secret, rotate through the configured number of subsequent changes, then
  attempt to reuse the original value.
```

## G02-AUTH_PASSWORD_POLICY-Q004

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q004
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The reuse restriction is enforced identically whether the new secret is chosen through an
  ordinary change or through a full reset/recovery flow.
WHY_IT_MATTERS: >
  A reset flow that skips the reuse check becomes a documented workaround for restoring a
  prohibited secret.
DISCONFIRMING_OBSERVATION: >
  A secret that the ordinary change flow would reject as a recent reuse is accepted when chosen
  through the reset/recovery flow instead.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Establish a recent-history value, then attempt to set that same value through the reset/recovery
  flow rather than the ordinary change form.
```

## G02-AUTH_PASSWORD_POLICY-Q005

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q005
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The age used to trigger forced expiry is measured from the date of the identity's most recent
  legitimate secret change, and that reference date updates on every such change.
WHY_IT_MATTERS: >
  An expiry clock anchored to the wrong event either expires secrets that were just changed or,
  worse, never expires ones that should be.
DISCONFIRMING_OBSERVATION: >
  After a legitimate secret change, the next forced-expiry deadline is unchanged from what it was
  before the change, or is computed from the account's original creation date.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Record the current forced-expiry deadline, perform a legitimate secret change, and re-check the
  deadline that now applies.
```

## G02-AUTH_PASSWORD_POLICY-Q006

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q006
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An identity that does not authenticate during the period in which its secret expires is still
  required to change it at the next authentication, rather than the deadline silently advancing.
WHY_IT_MATTERS: >
  A deadline that quietly slides forward for inactive accounts defeats the purpose of a maximum-
  age policy for exactly the accounts most likely to be forgotten and later reused by someone
  else.
DISCONFIRMING_OBSERVATION: >
  An identity that authenticates for the first time well after its computed expiry date is allowed
  in without being required to change its secret, and the expiry deadline has moved to a later
  date with no explicit change event to justify it.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Let a configured maximum age lapse for an identity that performs no interactive activity, then
  authenticate and inspect both the outcome and the recorded expiry deadline.
```

## G02-AUTH_PASSWORD_POLICY-Q007

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q007
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Tightening the policy does not force a change on an existing secret that already satisfies the
  new, stricter rule.
WHY_IT_MATTERS: >
  Forcing changes on already-compliant secrets creates unnecessary friction and trains users to
  treat forced changes as noise, weakening response to real violations.
DISCONFIRMING_OBSERVATION: >
  A secret that already satisfies the newly tightened rule is nonetheless flagged or forced for
  change purely because the policy version changed.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Set a secret that satisfies both the current and a stricter candidate policy, apply the stricter
  policy, and observe whether a forced change is triggered.
```

## G02-AUTH_PASSWORD_POLICY-Q008

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q008
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a policy is tightened, an identity whose existing secret no longer conforms is required to
  change it at its next authentication, rather than the non-conforming secret remaining silently
  accepted indefinitely.
WHY_IT_MATTERS: >
  A tightened rule that is not actually enforced against existing secrets provides no real
  security improvement and misrepresents the platform's posture.
DISCONFIRMING_OBSERVATION: >
  An identity continues to authenticate indefinitely using a secret that fails the current policy,
  with no forced-change prompt ever presented.
EXPECTED_SURFACE: S1,S3,S7
PRECONDITIONS: >
  Set a secret conforming to the old policy but not the new one, tighten the policy, and
  authenticate as that identity.
```

## G02-AUTH_PASSWORD_POLICY-Q009

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q009
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Weakening the policy does not retroactively force identities holding stronger, previously-
  compliant secrets to replace them.
WHY_IT_MATTERS: >
  Forcing replacement of a perfectly adequate secret purely because the floor was lowered wastes
  effort and can push a user toward a weaker replacement.
DISCONFIRMING_OBSERVATION: >
  An identity holding a secret that satisfies both the old and the new, weaker policy is
  nonetheless forced to change it after the policy is weakened.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Weaken the configured policy and observe whether identities with already-compliant secrets are
  prompted to change them.
```

## G02-AUTH_PASSWORD_POLICY-Q010

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q010
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A change to the policy configuration takes effect at a single deterministic point, after which
  every session and entry path enforces the same version.
WHY_IT_MATTERS: >
  An indefinite window of mixed enforcement means the same action can be accepted or rejected
  depending on which server, cache, or session happens to answer it.
DISCONFIRMING_OBSERVATION: >
  After a policy change is confirmed saved, some concurrent sessions or entry paths continue
  enforcing the previous version well beyond a reasonable propagation delay.
EXPECTED_SURFACE: S3,S7,S8
PRECONDITIONS: >
  Change the policy configuration while multiple sessions are active on different entry paths,
  then test the same borderline secret against each shortly after the change.
```

## G02-AUTH_PASSWORD_POLICY-Q011

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q011
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Tightening the secret-strength policy does not, by itself, immediately terminate an already-
  authenticated session, unless that behavior is an explicit, documented policy choice.
WHY_IT_MATTERS: >
  Undocumented session termination as a side effect of an unrelated configuration change causes
  unexplained outages that are hard to diagnose.
DISCONFIRMING_OBSERVATION: >
  An active session is silently ended the moment the strength policy is tightened, with no
  documented setting describing that this is intended behavior.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Open an active session, tighten the strength policy, and observe whether the session is
  terminated and whether that behavior is documented.
```

## G02-AUTH_PASSWORD_POLICY-Q012

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q012
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The system retains enough record of policy configuration history to determine, after the fact,
  which policy version governed a specific accept or reject decision.
WHY_IT_MATTERS: >
  Without this record, an investigation into a disputed rejection or an accepted weak secret
  cannot establish whether the platform behaved correctly for the rules in force at the time.
DISCONFIRMING_OBSERVATION: >
  After a subsequent policy change, there is no way to reconstruct which policy version was in
  force at an earlier point in time when a specific enforcement decision was made.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Trigger an enforcement decision, change the policy configuration, and attempt to determine which
  version was active at the time of the original decision using only recorded evidence.
```

## G02-AUTH_PASSWORD_POLICY-Q013

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q013
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where a scheduled or background process can set or rotate an internal identity's secret, it
  applies the same strength and reuse rules as an interactive change.
WHY_IT_MATTERS: >
  An automated path exempt from the policy becomes a silent backdoor for weak or reused secrets
  that bypasses every interactive control.
DISCONFIRMING_OBSERVATION: >
  A background or scheduled process sets a secret that would be rejected by the interactive change
  form.
EXPECTED_SURFACE: S7,S8
PRECONDITIONS: >
  Trigger the scheduled/background secret-setting path with a value that violates the current
  policy and compare the outcome to the interactive form.
```

## G02-AUTH_PASSWORD_POLICY-Q014

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q014
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When a privileged actor sets or resets another identity's secret on their behalf, the same
  strength and reuse rules apply as when the identity changes it directly.
WHY_IT_MATTERS: >
  An administrative shortcut that skips policy checks becomes the easiest way to plant a weak,
  memorable, or previously-compromised secret on any account.
DISCONFIRMING_OBSERVATION: >
  A privileged actor is able to set a policy-violating secret for another identity through an
  administrative or support path.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Using a privileged account, attempt to set a policy-violating secret for a different identity
  through every available administrative path.
```

## G02-AUTH_PASSWORD_POLICY-Q015

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q015
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A non-human, system, or integration account's credential is subject to the same strength policy
  as a human identity's, unless an explicit, documented exemption states otherwise.
WHY_IT_MATTERS: >
  An undocumented blanket exemption for system accounts is a common and high-value target because
  those credentials are long-lived and broadly privileged.
DISCONFIRMING_OBSERVATION: >
  A system or integration account's credential can be set to a value that would fail the human-
  facing policy, with no documented exemption covering that account class.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Identify a system or integration account and attempt to set a policy-violating credential for
  it; check for a documented exemption.
```

## G02-AUTH_PASSWORD_POLICY-Q016

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q016
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A secret value introduced through a bulk import or provisioning path is subject to the same
  strength and reuse checks as a single-record interactive change.
WHY_IT_MATTERS: >
  A bulk path that skips validation can introduce hundreds of non-conforming or duplicate secrets
  in a single unreviewed action.
DISCONFIRMING_OBSERVATION: >
  A batch import containing a policy-violating secret value completes without rejection or flag
  for that record.
EXPECTED_SURFACE: S3,S7,S8
PRECONDITIONS: >
  Prepare a bulk import containing at least one policy-violating secret value and run it through
  the supported import path.
```

## G02-AUTH_PASSWORD_POLICY-Q017

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q017
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A secret changed while a privileged actor is impersonating or acting as another identity is
  subject to the same policy checks as that identity's own direct change.
WHY_IT_MATTERS: >
  An impersonation path that bypasses the check gives a privileged actor an unaudited route to
  plant a weak secret on any identity.
DISCONFIRMING_OBSERVATION: >
  A policy-violating secret is accepted for an identity while a different, privileged actor is
  acting in that identity's session context.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Start an impersonation/act-as session for a test identity and attempt to set a policy-violating
  secret from within it.
```

## G02-AUTH_PASSWORD_POLICY-Q018

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q018
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The number of failed attempts that triggers lockout for a given identity is counted consistently
  across entry paths, so an attacker cannot obtain a larger effective attempt budget by switching
  paths.
WHY_IT_MATTERS: >
  A per-path counter multiplies the attacker's effective guess budget by the number of available
  entry paths, defeating the purpose of the threshold.
DISCONFIRMING_OBSERVATION: >
  An identity that has reached the lockout threshold via one entry path (for example the
  interactive form) can still be attempted additional times via a different path (for example a
  documented API) before lockout applies there.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Exhaust the failed-attempt threshold for an identity via one entry path, then immediately
  attempt authentication for the same identity via a different entry path.
```

## G02-AUTH_PASSWORD_POLICY-Q019

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q019
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An identity's lockout state and failed-attempt count survive a restart of the serving component,
  rather than resetting to a clean state.
WHY_IT_MATTERS: >
  A lockout that clears on every restart gives an attacker a way to reset their own attempt budget
  by triggering or waiting for routine maintenance.
DISCONFIRMING_OBSERVATION: >
  An identity's lockout is lifted, or its failed-attempt counter returns to zero, solely as a
  result of a service restart with no explicit unlock action taken.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Lock out a test identity, restart the serving component through a normal operational procedure,
  and re-check the identity's lockout state.
```

## G02-AUTH_PASSWORD_POLICY-Q020

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q020
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The failed-attempt counter used to trigger lockout is scoped strictly to the identity being
  attempted and cannot be incremented or exhausted by activity targeting a different identity.
WHY_IT_MATTERS: >
  A shared or miscounted budget lets an attacker's failed attempts against one identity consume,
  or falsely trigger, lockout for an unrelated identity.
DISCONFIRMING_OBSERVATION: >
  Repeated failed attempts against one identity cause the failed-attempt counter, or the lockout
  state, of a different, unrelated identity to change.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Run repeated failed authentication attempts against one test identity and monitor the counter
  and lockout state of a second, unrelated identity.
```

## G02-AUTH_PASSWORD_POLICY-Q021

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q021
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An outside party who can guess or learn a valid identifier cannot use repeated failed attempts
  to lock out the legitimate holder of that identity without the platform recording a detectable
  pattern distinguishing this from ordinary failed logins.
WHY_IT_MATTERS: >
  Undetected lockout abuse denies a legitimate user access on demand and, if unlogged, leaves the
  organization unable to even recognize it happened.
DISCONFIRMING_OBSERVATION: >
  A known identity can be locked out by an unauthenticated party through ordinary failed attempts,
  and the resulting lockout event is indistinguishable in the audit trail from an accidental self-
  lockout by the legitimate user.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  From an unauthenticated context, deliberately trigger lockout for a known test identity and
  inspect the resulting audit record for distinguishing detail.
```

## G02-AUTH_PASSWORD_POLICY-Q022

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q022
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Once an identity is locked out, the lockout itself is lifted only through a defined recovery or
  administrative action, not merely by the failed-attempt counter aging out on its own.
WHY_IT_MATTERS: >
  If the counter aging out alone lifts a full lockout, the platform is effectively enforcing a
  much shorter, undocumented lockout duration than the one it claims.
DISCONFIRMING_OBSERVATION: >
  An identity that has been placed in a locked-out state becomes able to authenticate again purely
  because time has passed, with no distinct unlock action or event recorded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Lock out a test identity, wait past the point where only the failed-attempt counter would reset,
  and attempt authentication with the correct secret.
```

## G02-AUTH_PASSWORD_POLICY-Q023

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q023
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Once an identity is locked out, that state is enforced identically across every entry path
  capable of authenticating it, rather than each surface maintaining independent state.
WHY_IT_MATTERS: >
  A lockout that only applies on one surface leaves every other surface fully open, giving an
  attacker a trivial way around the control.
DISCONFIRMING_OBSERVATION: >
  An identity locked out on one entry path can still successfully authenticate with the correct
  secret through a different entry path.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Lock out a test identity via one entry path, then attempt authentication with the correct secret
  via a different entry path.
```

## G02-AUTH_PASSWORD_POLICY-Q024

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q024
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The self-service reset/recovery flow checks and respects an identity's current lockout state
  rather than granting a fresh secret regardless of lockout.
WHY_IT_MATTERS: >
  If reset ignores lockout, the reset flow becomes a standing bypass that defeats the lockout
  control entirely.
DISCONFIRMING_OBSERVATION: >
  A locked-out identity is able to complete a self-service reset and immediately authenticate with
  the new secret while the lockout would otherwise still apply.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Lock out a test identity, then attempt the self-service reset flow for that same identity and
  check whether the resulting secret can be used to authenticate immediately.
```

## G02-AUTH_PASSWORD_POLICY-Q025

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q025
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Proving ownership of the reset/recovery channel requires an authentication strength at least
  equal to what would otherwise be required of the primary factor, not a materially weaker side
  channel.
WHY_IT_MATTERS: >
  A weaker recovery channel becomes the attacker's preferred target, turning the strongest primary
  control into a formality.
DISCONFIRMING_OBSERVATION: >
  An identity can be fully taken over through the reset/recovery flow using proof weaker than what
  the primary authentication path would require.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Compare the verification strength required by the primary authentication path against that
  required by the reset/recovery path for the same identity.
```

## G02-AUTH_PASSWORD_POLICY-Q026

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q026
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A reset link or code has a bounded lifetime and stops working once it has been used
  successfully.
WHY_IT_MATTERS: >
  A reset credential with no expiry or that survives reuse remains a standing takeover risk for as
  long as anyone retains a copy of it.
DISCONFIRMING_OBSERVATION: >
  A reset link or code can still be used successfully well past a reasonable time bound, or can be
  used more than once to set a secret.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Request a reset link/code, wait past a reasonable bound, and separately attempt to reuse an
  already-consumed one.
```

## G02-AUTH_PASSWORD_POLICY-Q027

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q027
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Requesting a new reset link or code invalidates any earlier, still-unused one issued for the
  same identity.
WHY_IT_MATTERS: >
  Without this, an old leaked link keeps working even after the legitimate user has moved on to a
  fresh request, extending an attacker's window indefinitely.
DISCONFIRMING_OBSERVATION: >
  An earlier reset link remains usable after a subsequent reset request for the same identity has
  been made.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Request a reset for a test identity, then request a second reset for the same identity, and
  attempt to use the first link.
```

## G02-AUTH_PASSWORD_POLICY-Q028

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q028
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The secret chosen at the end of the reset/recovery flow is checked against the same strength and
  reuse rules as an ordinary change.
WHY_IT_MATTERS: >
  A reset flow with a lesser check becomes the easiest route to plant a weak or previously-used
  secret, undermining the whole policy.
DISCONFIRMING_OBSERVATION: >
  A secret that would be rejected by the ordinary change form is accepted when submitted at the
  end of the reset/recovery flow.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to set an identical policy-violating secret through the ordinary change form and through
  the reset/recovery flow, and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY-Q029

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q029
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Each tenant/company can hold its own policy configuration, and a laxer configuration in one
  tenant does not weaken enforcement for identities scoped to a different tenant.
WHY_IT_MATTERS: >
  Shared enforcement logic that leaks configuration across tenant boundaries turns one customer's
  deliberately relaxed setting into every customer's problem.
DISCONFIRMING_OBSERVATION: >
  Weakening the policy for one tenant measurably weakens the effective enforcement observed for an
  identity scoped to a different tenant.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure two tenants with different policy strength, then test a borderline secret against an
  identity in each tenant.
```

## G02-AUTH_PASSWORD_POLICY-Q030

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q030
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An administrator scoped to one tenant cannot view or edit the policy configuration belonging to
  a different tenant.
WHY_IT_MATTERS: >
  Cross-tenant visibility or edit rights over security configuration breaks the isolation the
  whole multi-tenant model depends on.
DISCONFIRMING_OBSERVATION: >
  An administrator scoped to one tenant is able to view or change the policy configuration
  recorded for a different tenant.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Using an administrator account scoped to tenant A, attempt to view and then edit the policy
  configuration recorded for tenant B.
```

## G02-AUTH_PASSWORD_POLICY-Q031

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q031
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where both an organization-wide default policy and a tenant-specific override can exist, the
  platform applies one deterministic, documented precedence rather than an ambiguous merge of the
  two.
WHY_IT_MATTERS: >
  An ambiguous merge between default and override produces enforcement that differs from what
  either configuration screen shows, and cannot be reasoned about or trusted.
DISCONFIRMING_OBSERVATION: >
  The effective policy enforced for a tenant with an override configured differs from what either
  the organization-wide default or the tenant override, taken alone, would produce, with no
  documented merge rule explaining the result.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure an organization-wide default and a conflicting tenant override, then test a secret
  that the two configurations would judge differently.
```

## G02-AUTH_PASSWORD_POLICY-Q032

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q032
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rejected secret produces feedback that is useful for the legitimate user but does not disclose
  enough specific rule detail to materially assist an attacker probing the policy remotely.
WHY_IT_MATTERS: >
  An overly specific rejection response turns the policy screen into a free tool for reverse-
  engineering exactly which rule to satisfy with minimum effort, without any corresponding
  usability benefit.
DISCONFIRMING_OBSERVATION: >
  The rejection response for a failed secret submission discloses the exact rule thresholds (such
  as precise character-class counts or exact history depth) in a way that goes beyond what is
  needed to guide the legitimate user.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Submit several distinct policy-violating secrets and compare the specificity of each rejection
  message against the minimum needed for a user to correct the input.
```

## G02-AUTH_PASSWORD_POLICY-Q033

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q033
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An identity cannot set its secret to a value equal to, or a trivial transform of, its own name,
  login, or contact address.
WHY_IT_MATTERS: >
  A secret derived from public or semi-public identity attributes is trivially guessable and
  defeats the purpose of any strength rule layered on top.
DISCONFIRMING_OBSERVATION: >
  An identity successfully sets its secret to a value equal to, or a simple variant of, its own
  login name or displayed identifying attribute.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to set an identity's secret to its own login name or a minor variant of a known
  identifying attribute.
```

## G02-AUTH_PASSWORD_POLICY-Q034

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q034
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A secret-change attempt that fails validation leaves the previous secret and the requesting
  session's authentication state completely unchanged.
WHY_IT_MATTERS: >
  A partially applied failed change could silently lock a legitimate user out of their own account
  or leave the account in an undefined credential state.
DISCONFIRMING_OBSERVATION: >
  After a secret-change attempt fails validation, the identity can no longer authenticate with the
  original secret, or the session's authentication state has changed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt a policy-violating secret change for a test identity, then confirm the original secret
  and the current session both still work exactly as before.
```

## G02-AUTH_PASSWORD_POLICY-Q035

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q035
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two concurrent secret-change requests for the same identity from different sessions resolve to
  one deterministic, recorded outcome rather than an unrecorded race.
WHY_IT_MATTERS: >
  A silent race leaves the user unsure which secret is actually active and can silently invalidate
  a legitimate concurrent session with no explanation in the trail.
DISCONFIRMING_OBSERVATION: >
  Two concurrent secret-change requests for the same identity both appear to succeed, or the
  losing request's outcome and effect on the other active session are not recorded anywhere.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Submit two different valid secret-change requests for the same identity at nearly the same time
  from two separate sessions, then examine the outcome and the audit trail.
```

## G02-AUTH_PASSWORD_POLICY-Q036

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q036
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Every accept, reject, lockout-trigger, and lockout-release decision for a secret is captured in
  a trail identifying what happened and when.
WHY_IT_MATTERS: >
  Without a complete decision trail, an investigation into a compromised account cannot establish
  what the policy actually did at the relevant moment.
DISCONFIRMING_OBSERVATION: >
  A specific accept, reject, lockout, or unlock event that is known to have occurred cannot be
  located in any retained trail.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Trigger one instance each of an accepted change, a rejected change, a lockout, and an unlock,
  then attempt to locate each event in the retained trail.
```

## G02-AUTH_PASSWORD_POLICY-Q037

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q037
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The record of an accept or reject decision includes, or can be tied to, the specific policy
  version that was active at the time.
WHY_IT_MATTERS: >
  An outcome record with no version reference cannot be checked for correctness once the policy
  has since changed.
DISCONFIRMING_OBSERVATION: >
  After the policy configuration changes, an earlier accept or reject decision cannot be verified
  against the version of the policy that was actually in force when it happened.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Record an enforcement decision, change the policy configuration, and attempt to determine which
  version governed the earlier decision.
```

## G02-AUTH_PASSWORD_POLICY-Q038

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q038
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A change to the policy configuration itself is recorded with who made it, when, and what the
  prior configuration was.
WHY_IT_MATTERS: >
  Unaudited configuration changes let a weakening of security posture go completely unnoticed
  until it is exploited.
DISCONFIRMING_OBSERVATION: >
  The policy configuration is changed and no record exists identifying the actor, time, or prior
  value.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Change the policy configuration through the administrative interface and inspect whatever change
  history is retained.
```

## G02-AUTH_PASSWORD_POLICY-Q039

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q039
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A configuration change that weakens the policy is distinguishable in the retained record from a
  routine or unrelated configuration change, not merged into one generic 'settings updated' entry.
WHY_IT_MATTERS: >
  If a weakening blends into routine noise, no reviewer will notice it during a normal audit
  sweep.
DISCONFIRMING_OBSERVATION: >
  Reviewing the change history for the policy configuration does not allow a reviewer to identify,
  without inspecting every individual field, that a specific change was a weakening of the
  effective policy.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Make one weakening change and one unrelated maintenance change to the policy configuration, then
  review the resulting history entries for distinguishability.
```

## G02-AUTH_PASSWORD_POLICY-Q040

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q040
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Disabling or bypassing a second authentication factor does not implicitly relax the secret-
  strength policy, and vice versa; the two controls are configured and enforced independently.
WHY_IT_MATTERS: >
  An implicit coupling between unrelated controls means a change intended to affect only one
  silently changes the other, defeating whatever protection the untouched control was assumed to
  still provide.
DISCONFIRMING_OBSERVATION: >
  Disabling the second factor for an identity is observed to also relax the strength or lockout
  behavior applied to that identity's secret, without an explicit setting causing that link.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Disable the second factor for a test identity where applicable, and compare secret-policy
  enforcement for that identity before and after.
```

## G02-AUTH_PASSWORD_POLICY-Q041

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q041
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where an identity is permitted to authenticate via an external identity source, the presence of
  the internal secret policy does not create a documented impression of protection that does not
  actually apply to that identity's real authentication path.
WHY_IT_MATTERS: >
  A policy that only covers a path an identity does not actually use gives a false sense of
  security to anyone relying on the policy documentation.
DISCONFIRMING_OBSERVATION: >
  An identity that authenticates exclusively through an external source is nonetheless reported or
  documented as covered by the internal secret policy with no note explaining that the policy does
  not apply to its actual authentication path.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Identify an identity configured to authenticate via an external source and check how its
  coverage is represented against the internal secret policy documentation.
```

## G02-AUTH_PASSWORD_POLICY-Q042

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q042
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where no explicit strength policy has been configured, the platform enforces a defined safe
  default rather than accepting any value with no restriction at all.
WHY_IT_MATTERS: >
  A silent absence of restriction is the easiest possible misconfiguration to make and the hardest
  to notice, since nothing in the interface signals a problem.
DISCONFIRMING_OBSERVATION: >
  With no explicit policy configured, an identity can set a trivially weak secret (such as a
  single character) with no rejection.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Ensure no explicit strength policy is configured and attempt to set a trivially weak secret for
  a test identity.
```

## G02-AUTH_PASSWORD_POLICY-Q043

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q043
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where no explicit lockout configuration exists, the platform still enforces a defined safe
  default threshold rather than permitting unlimited failed attempts.
WHY_IT_MATTERS: >
  Unlimited attempts by default turns every unconfigured deployment into an open invitation for
  automated guessing.
DISCONFIRMING_OBSERVATION: >
  With no explicit lockout configuration, a large number of consecutive failed attempts against
  one identity produces no lockout at all.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Ensure no explicit lockout configuration exists and run a large number of consecutive failed
  attempts against a test identity.
```

## G02-AUTH_PASSWORD_POLICY-Q044

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q044
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A difference in time zone or clock between the component deciding expiry and the identity's own
  environment does not shift the effective expiry point in a way that is materially exploitable.
WHY_IT_MATTERS: >
  An expiry decision sensitive to an uncontrolled clock difference could be nudged, deliberately
  or accidentally, to extend a secret's effective life well beyond the intended maximum age.
DISCONFIRMING_OBSERVATION: >
  An identity is able to keep an otherwise-expired secret valid, or is forced to change a secret
  well before its intended age, purely by virtue of a time-zone or clock difference between client
  and server.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Bring an identity's secret close to its expiry boundary and test authentication from
  environments reporting different time zones or clock offsets.
```

## G02-AUTH_PASSWORD_POLICY-Q045

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q045
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Abandoning a secret-change flow before completion leaves no partial or intermediate secret value
  in force.
WHY_IT_MATTERS: >
  A half-applied change could leave an account in an undocumented state where neither the old nor
  the intended new secret works, or worse, a predictable intermediate value does.
DISCONFIRMING_OBSERVATION: >
  After abandoning a secret-change flow partway through, the identity's original secret no longer
  works, or a predictable intermediate value does.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Begin a secret-change flow, abandon it before the final confirming step, and test whether the
  original secret still authenticates.
```

## G02-AUTH_PASSWORD_POLICY-Q046

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q046
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A secret set through a documented programmatic interface is checked against the identical
  strength and reuse rules as the interactive form.
WHY_IT_MATTERS: >
  A programmatic path with a lesser check becomes the preferred route for any automated or
  scripted attempt to plant a non-conforming secret.
DISCONFIRMING_OBSERVATION: >
  A secret rejected by the interactive form is accepted when submitted through the documented
  programmatic interface.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Submit an identical policy-violating secret through the interactive form and through the
  documented programmatic interface, and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY-Q047

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q047
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Rolling back a policy configuration to a prior version does not automatically treat a
  previously-rejected secret as now valid without a fresh evaluation event taking place.
WHY_IT_MATTERS: >
  Silent revalidation on rollback could reinstate a secret that was rejected for good reason, with
  no new record showing that a real evaluation happened.
DISCONFIRMING_OBSERVATION: >
  After a policy rollback, a secret that had been rejected under the newer policy becomes the
  identity's active secret with no new change or evaluation event recorded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Have an identity's secret change rejected under the current policy, roll the policy back to the
  prior version, and check whether the rejected value becomes active without a new event.
```

## G02-AUTH_PASSWORD_POLICY-Q048

```yaml
QID: G02-AUTH_PASSWORD_POLICY-Q048
MODULE: auth_password_policy
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An identity that authenticates only rarely still faces the configured maximum-age rotation check
  the first time it authenticates after the age is exceeded, regardless of how long the gap was.
WHY_IT_MATTERS: >
  An accidental exemption for infrequent accounts means exactly the accounts most likely to be
  dormant, shared, or forgotten are the ones left running on the oldest, least-reviewed secrets.
DISCONFIRMING_OBSERVATION: >
  An identity that authenticates for the first time long after its maximum age was exceeded is
  allowed in without being required to change its secret.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Let a maximum-age threshold lapse by a wide margin for a dormant test identity, then
  authenticate as that identity and observe whether a forced change is triggered.
```

