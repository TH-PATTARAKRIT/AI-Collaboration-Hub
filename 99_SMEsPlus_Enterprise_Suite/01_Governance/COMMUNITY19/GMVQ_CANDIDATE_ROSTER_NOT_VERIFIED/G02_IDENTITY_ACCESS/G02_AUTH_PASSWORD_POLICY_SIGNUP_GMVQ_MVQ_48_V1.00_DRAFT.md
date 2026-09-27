# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / auth_password_policy_signup Module Adversarial MVQ Bank

**Document ID:** GMVQ-G02-AUTH_PASSWORD_POLICY_SIGNUP-MVQ48-V1.00
**Group:** G02 IDENTITY_ACCESS
**Module Metadata:** `auth_password_policy_signup`
**Wave:** W1
**Author Cell:** TEAM 11 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded
**Standing Authorization:** SMEPLUS-GMVQ-25TEAM-ACCELERATION-20260927-001

## Purpose

This bank extends the 55 Standard Questions with 48 hard, module-specific behavioural
questions for `auth_password_policy_signup` — enforcement of secret-strength policy at
the moment of self-registration, before a full account exists. It targets the half-created
identity, the invitation/token that carries entitlements, client-side versus server-side
enforcement divergence, alternate creation paths (import, integration, administrator) that
could escape registration-time policy, and the first secret set during activation.

The question text is source-neutral: it does not expose vendor names, model names, field
names, method names, XML IDs, API shapes, or any implementation detail. `MODULE:` carries
the metadata name; the metadata name never appears in question text.

## Control

- Every question has a falsifiable `DISCONFIRMING_OBSERVATION` that is a failure state, not a restatement of the hypothesis.
- No padding: 48 questions exist because each tests a distinct material hypothesis.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence from Lane A or Lane B.
- `MODULE + QID` is a Research Evidence Join Key only. No Formal Coverage is derived from this bank.
- This bank is DRAFT / AUTHORING COMPLETE / NOT FROZEN. It is not approved, not verified, not MASTER-ready.

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q001

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q001
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Any path that creates a new external-facing identity, not only the visible self-registration
  form, must evaluate the same secret-strength policy before the identity becomes usable.
WHY_IT_MATTERS: >
  A weaker back-door creation path defeats the whole policy and gives an attacker a predictable
  way in that was never meant to exist.
DISCONFIRMING_OBSERVATION: >
  An identity created through a non-form path becomes usable with a secret that the visible
  signup form would have rejected.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Identify every path capable of creating a new external identity with a settable secret;
  attempt to set a policy-violating secret through each path and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q002

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q002
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A bulk import or data-migration path that provisions many identities at once must not leave
  imported identities usable with no secret set, or with a secret bypassing the strength
  policy, without an explicit compensating control.
WHY_IT_MATTERS: >
  Mass onboarding is the highest-volume, least-observed creation path and a natural place
  for policy gaps to hide at scale.
DISCONFIRMING_OBSERVATION: >
  Identities produced by a bulk import become authenticable without ever passing through the
  strength policy, and no compensating control is applied.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Provision several identities through the bulk/import path with a range of secrets including
  policy-violating ones; attempt to authenticate as each without further action.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q003

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q003
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An account created directly by an administrator, with a temporary secret chosen by the
  administrator, must still be subject to the same strength policy the moment the account
  holder sets their own secret.
WHY_IT_MATTERS: >
  Administrative convenience must not become a standing exemption from the policy.
DISCONFIRMING_OBSERVATION: >
  A holder is able to set a policy-violating secret as their first self-chosen one after an
  administrator-issued temporary secret.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Have an administrator create an account with a temporary secret; complete the first
  self-service secret change and attempt a policy-violating value.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q004

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q004
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A secret rejected by the interface's own strength check must also be rejected if submitted
  directly to the underlying processing path, and a secret accepted by the interface must
  also pass the same check applied server-side.
WHY_IT_MATTERS: >
  Client-only enforcement can be trivially bypassed by anyone who does not use the provided
  interface.
DISCONFIRMING_OBSERVATION: >
  A policy-violating secret that the interface blocks is accepted when submitted through a
  lower-level path that skips the interface's own check.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Identify a secret value the interface rejects; submit the same value through a path that
  bypasses the interface layer and observe the outcome.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q005

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q005
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An identity that has begun registration but not completed every required step must not be
  usable to authenticate into protected areas as if registration were complete.
WHY_IT_MATTERS: >
  A half-created identity with live access is an unintended, unaudited entry point.
DISCONFIRMING_OBSERVATION: >
  An in-progress registration record can be used to reach protected functionality before the
  registration flow reports completion.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Begin self-registration and stop short of the final confirmation step; attempt
  authentication and access to protected functionality.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q006

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q006
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The entitlement level carried by an invitation or activation token must be fixed by the
  issuer and must not be widened by anything the recipient controls in completing the
  activation.
WHY_IT_MATTERS: >
  A token whose granted scope can be inflated by the recipient turns an onboarding
  convenience into a privilege-escalation path.
DISCONFIRMING_OBSERVATION: >
  Completing activation with a modified request yields broader entitlements than the
  invitation was issued with.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Issue an invitation with a defined, narrow entitlement; complete activation while altering
  the fields the client submits, and inspect the resulting entitlement.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q007

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q007
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An invitation or activation token, once used to complete registration, must not be usable a
  second time to create or reactivate an identity.
WHY_IT_MATTERS: >
  A reusable token turns a single authorized onboarding into an unlimited one.
DISCONFIRMING_OBSERVATION: >
  The same token succeeds in completing activation a second time after already having been
  consumed once.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Complete activation with a token; immediately reattempt activation with the identical token
  and observe the result.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q008

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q008
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  If the strength policy is tightened between the moment an invitation is issued and the
  moment it is completed, the completion must be evaluated against the policy in force at
  completion, not at issuance.
WHY_IT_MATTERS: >
  An outstanding invitation should not become a way to onboard under a policy that has since
  been superseded.
DISCONFIRMING_OBSERVATION: >
  A secret that violates the current policy is accepted at activation because an older,
  looser policy was in force when the invitation was issued.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Issue an invitation under one policy configuration, tighten the policy, then complete
  activation with a secret that only the earlier policy would have allowed.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q009

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q009
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An invitation or activation token past its stated validity period must not allow
  registration to complete.
WHY_IT_MATTERS: >
  An expiry that is not actually enforced gives every issued invitation an unbounded,
  unaudited lifetime.
DISCONFIRMING_OBSERVATION: >
  Activation completes successfully using a token whose stated validity window has already
  passed.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Issue an invitation with a short validity window, let it lapse, and attempt to complete
  activation with it.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q010

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q010
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The expiry of an invitation or activation token must be evaluated on a single, consistent
  time basis regardless of the timezone of the issuer, the recipient, or the server component
  performing the check.
WHY_IT_MATTERS: >
  An inconsistent time basis makes an expiry unpredictable and can either open a window past
  intended expiry or reject a still-valid attempt.
DISCONFIRMING_OBSERVATION: >
  Two otherwise identical invitations, issued and completed with the same real elapsed time
  but under different timezone settings, are evaluated as expired in one case and valid in
  the other.
EXPECTED_SURFACE: S1,S6,S7
PRECONDITIONS: >
  Issue invitations under distinct timezone configurations with equal real elapsed time to
  completion and compare expiry outcomes.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q011

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q011
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The strength policy configured for one tenant's self-registration must not apply to, or be
  overridden by, another tenant's configuration.
WHY_IT_MATTERS: >
  Cross-tenant policy leakage lets one customer's weaker or stricter choice silently affect
  another's registrations.
DISCONFIRMING_OBSERVATION: >
  A registration completed under one tenant is evaluated against, or affected by, a different
  tenant's configured policy.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure two tenants with materially different policies and complete a borderline
  registration under each, cross-checking which configuration was actually applied.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q012

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q012
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two concurrent self-registration attempts for the same identifying detail must resolve to
  at most one completed, active identity, not two independent ones.
WHY_IT_MATTERS: >
  A race condition here can create duplicate or conflicting identities, or let a second
  attempt overwrite the first's still-pending credential without proper authorization.
DISCONFIRMING_OBSERVATION: >
  Two near-simultaneous registrations using the same identifying detail both complete, or the
  second silently replaces the first's still-pending credential.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit two registration attempts for the same identifying detail at nearly the same time
  and inspect the resulting identity or identities.
```
## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q013

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q013
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A newly created, not-yet-activated identity record must not carry a usable secret (blank,
  default, or predictable placeholder) that would let it authenticate before the holder has
  set their own.
WHY_IT_MATTERS: >
  A predictable placeholder secret on a pending identity is a foreseeable, low-effort
  intrusion path.
DISCONFIRMING_OBSERVATION: >
  A pending registration can be authenticated against before the holder has ever set a
  secret, using a default or blank value.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Create a pending registration and, before completing activation, attempt authentication
  with an empty or commonly-used default secret.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q014

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q014
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The policy evaluated when a holder sets their first secret during activation must be the
  same policy object applied to every later voluntary secret change, not a separate, looser
  signup-only rule.
WHY_IT_MATTERS: >
  Two divergent policy definitions for the same kind of decision is a governance and
  consistency failure that is easy to lose track of.
DISCONFIRMING_OBSERVATION: >
  A secret rejected during a later voluntary change would have been accepted during initial
  activation, or vice versa, with no documented reason for the difference.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Record the exact policy boundary at activation; later attempt the same boundary values
  during a voluntary secret change and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q015

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q015
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A value already rejected once for a given pending registration must be evaluated
  identically if resubmitted later in the same or a restarted registration attempt.
WHY_IT_MATTERS: >
  Inconsistent re-evaluation suggests the policy state is not being checked freshly, which
  undermines confidence in every other check.
DISCONFIRMING_OBSERVATION: >
  The same previously rejected value is accepted on a later attempt for the same pending
  identity with no change in configuration.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit a policy-violating value, note the rejection, then resubmit the identical value on a
  fresh attempt for the same pending identity.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q016

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q016
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the platform screens secrets against a list of commonly used or previously exposed
  values, that screening applies at the point of initial self-registration and not only to
  later changes.
WHY_IT_MATTERS: >
  The first secret a new external identity ever sets is the one most likely to be reused from
  elsewhere and is the highest-value moment to screen.
DISCONFIRMING_OBSERVATION: >
  A widely known, commonly used value is accepted at initial signup but rejected on a later
  voluntary change under the same configuration.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Attempt a widely known common value at initial signup and again at a later voluntary secret
  change, and compare acceptance.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q017

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q017
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Boundary-length and unusual-character secrets that the interface accepts or rejects must be
  evaluated identically by the underlying processing path.
WHY_IT_MATTERS: >
  A mismatch at the boundary is exactly where an attacker or an integrator probing the
  interface will find and exploit a gap.
DISCONFIRMING_OBSERVATION: >
  A boundary-length or unusual-character value is accepted by one layer and rejected by the
  other for the same registration attempt.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Construct secrets at the minimum, maximum, and just-outside-boundary lengths, and with
  unusual characters, and submit each through both the interface and the underlying path.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q018

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q018
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A self-registration must not allow a secret that is identical to, or trivially derived
  from, the identity's own identifying details.
WHY_IT_MATTERS: >
  A secret matching the identifier defeats the purpose of having a secret at all and is a
  common trivial-guess attack path.
DISCONFIRMING_OBSERVATION: >
  Registration completes using a secret identical to, or a simple variant of, the identity's
  own identifying detail.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Attempt registration using the account's own identifying detail as the secret, and minor
  variants of it.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q019

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q019
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeated policy-violating submissions during a single registration attempt must be
  rate-limited or otherwise bounded, rather than allowing unlimited automated probing of the
  policy boundary.
WHY_IT_MATTERS: >
  An unbounded, automatable check is a tool for enumerating exactly what the policy will
  accept.
DISCONFIRMING_OBSERVATION: >
  An automated sequence of many rapid policy-violating submissions against the same pending
  registration completes with no throttling, delay, or lockout.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Script a rapid sequence of differing policy-violating submissions against one pending
  registration and observe whether any limiting behaviour appears.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q020

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q020
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If repeated invalid attempts against a pending registration trigger a lockout, that lockout
  must not be triggerable by an unrelated party who does not control the identity being
  registered, in a way that denies the legitimate holder.
WHY_IT_MATTERS: >
  A lockout mechanism intended to protect an account can become a tool for a third party to
  block a legitimate signup.
DISCONFIRMING_OBSERVATION: >
  A party with no access to the invitation or identity can, by repeated invalid attempts
  alone, lock out the legitimate holder's ability to complete registration.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  From a session unrelated to the pending registration, submit repeated invalid completion
  attempts and then have the legitimate holder attempt completion.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q021

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q021
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The specific policy configuration in force at the moment a given identity's initial secret
  was accepted must be reconstructable afterward from an audit record.
WHY_IT_MATTERS: >
  Without this, an incident investigation cannot determine whether an old identity was ever
  actually held to the current policy.
DISCONFIRMING_OBSERVATION: >
  No record exists, or the record is inconsistent, that would let an investigator determine
  which policy configuration governed a specific historical registration.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Complete a registration under a known policy configuration, then change the configuration,
  and attempt to determine from available records which configuration governed the original
  registration.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q022

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q022
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A failed self-registration attempt must be distinguishable in the audit trail from a failed
  authentication attempt against an existing account.
WHY_IT_MATTERS: >
  Conflating the two obscures whether an incident is credential-guessing against real
  accounts or probing of the registration process itself.
DISCONFIRMING_OBSERVATION: >
  The audit trail records a failed signup attempt in a way indistinguishable from, or absent
  relative to, a failed login attempt.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Generate one failed registration attempt and one failed login attempt against an existing
  identity, and compare what the audit trail records for each.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q023

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q023
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If an administrator is permitted to set a secret that does not meet the standard policy
  while manually creating an account, that override must be explicitly recorded as an
  exception, not indistinguishable from a normal policy-compliant creation.
WHY_IT_MATTERS: >
  An unrecorded exception is invisible to any later audit or governance review.
DISCONFIRMING_OBSERVATION: >
  An administrator successfully sets a policy-violating secret during manual account creation
  with no distinguishing record of the exception.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Have an administrator create an account with a deliberately policy-violating secret and
  inspect whether the resulting record flags this as an exception.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q024

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q024
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An invitation or activation token issued in the context of one tenant must not be honored
  when presented against a different tenant's registration endpoint.
WHY_IT_MATTERS: >
  Cross-tenant token acceptance would let an onboarding credential intended for one
  customer's environment provision access in another's.
DISCONFIRMING_OBSERVATION: >
  A token issued for one tenant successfully completes activation when presented in the
  context of a different tenant.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Issue an invitation under one tenant's context and attempt to complete it against another
  tenant's registration path.
```
## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q025

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q025
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The self-registration flow's response must not let an unauthenticated party determine, from
  its behaviour alone, whether a given identifying detail is already registered.
WHY_IT_MATTERS: >
  This kind of leak turns the registration form into an account-enumeration tool for anyone
  probing the system.
DISCONFIRMING_OBSERVATION: >
  Registration attempts using an already-registered identifying detail produce an observably
  different response from attempts using an unregistered one.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Attempt registration with a known-registered identifying detail and with a
  known-unregistered one, and compare the responses received by an unauthenticated party.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q026

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q026
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The requirements a secret must meet should be knowable to the registrant before submission,
  and a rejection must state which requirement failed rather than an undifferentiated
  refusal.
WHY_IT_MATTERS: >
  An opaque rejection with no stated requirement pushes registrants toward guessing, which
  increases both abandonment and support burden without improving actual strength.
DISCONFIRMING_OBSERVATION: >
  A rejected submission gives no indication of which specific requirement was not met, and no
  requirement was stated before submission.
EXPECTED_SURFACE: S5
PRECONDITIONS: >
  Submit a policy-violating value during registration and inspect what information, if any,
  is presented before and after the rejection.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q027

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q027
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If the registration process fails or is interrupted after a secret has been accepted but
  before the identity is fully activated, the resulting partial record must not be left in a
  state that is both credentialed and indefinitely reachable outside normal activation.
WHY_IT_MATTERS: >
  An orphaned, credentialed, half-created identity is an unmonitored foothold that nobody is
  watching for.
DISCONFIRMING_OBSERVATION: >
  A registration interrupted after the secret step but before final activation leaves a
  record that can still be authenticated against, indefinitely, without completing
  activation.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Interrupt a registration attempt deliberately after the secret-setting step and before
  final confirmation, then attempt authentication and inspect the record's state over time.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q028

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q028
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a self-registration path exists for external, non-employee users, the resulting
  identity's access must be bounded to what external users are meant to reach, regardless of
  how the initial secret was set.
WHY_IT_MATTERS: >
  If a deliberately lighter external-signup regime can end up touching internal-only data,
  the lighter regime becomes a backdoor into the stricter one.
DISCONFIRMING_OBSERVATION: >
  An identity created through the external self-registration path can reach data or
  functionality intended to be internal-only.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Complete an external self-registration and attempt to reach functionality or records scoped
  as internal-only.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q029

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q029
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If self-registration is available through more than one client surface, each surface's
  validation of the same policy must produce the same accept/reject outcome for the same
  input.
WHY_IT_MATTERS: >
  A weaker surface becomes the path of least resistance for anyone wanting to bypass the
  intended policy.
DISCONFIRMING_OBSERVATION: >
  The same secret value is accepted on one client surface and rejected on another for
  registration against the same tenant and policy.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Submit an identical boundary-value secret through each available client surface for the
  same tenant and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q030

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q030
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  When the policy is tightened, whether that tightening applies to invitations already issued
  but not yet completed must be an explicit, documented choice, not an accidental byproduct
  of when the check happens to run.
WHY_IT_MATTERS: >
  An undocumented inconsistency here means nobody can state with confidence which policy
  actually governs a given outstanding invitation.
DISCONFIRMING_OBSERVATION: >
  Two invitations issued under the same original policy and completed after the same
  tightening event are evaluated against different policy versions.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Issue two invitations under one policy, tighten the policy, complete both at different
  times, and compare which policy version each was evaluated against.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q031

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q031
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A registration flow requiring the secret to be entered twice for confirmation must reject a
  mismatch consistently and must never fall back to accepting either of the two mismatched
  values.
WHY_IT_MATTERS: >
  A silent fallback on mismatch can set a secret the registrant never intended and does not
  know.
DISCONFIRMING_OBSERVATION: >
  A registration with two different values in the confirmation fields completes successfully
  using one of them.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Submit registration with two different values in the primary and confirmation secret fields
  and observe the outcome.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q032

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q032
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The strength policy must be checked before the pending identity record is considered
  committed, not after, such that a policy failure never leaves a committed record with an
  unvalidated secret.
WHY_IT_MATTERS: >
  If commitment happens before validation, a failure partway through validation could leave a
  live, non-compliant record.
DISCONFIRMING_OBSERVATION: >
  A registration record becomes committed and reachable with a secret that was never actually
  validated against the policy, due to an ordering gap.
EXPECTED_SURFACE: S1
PRECONDITIONS: >
  Attempt to interrupt or race a registration submission between the point of record
  commitment and the point of policy validation, and inspect the resulting record.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q033

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q033
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If more than one invitation is issued for the same identity before any is completed,
  completing any one of them must not silently grant the entitlement of the most permissive
  of the set rather than the specific one used.
WHY_IT_MATTERS: >
  A most-permissive-wins behaviour would let re-issuing an invitation for correction purposes
  accidentally escalate access.
DISCONFIRMING_OBSERVATION: >
  Completing a specific invitation grants an entitlement level matching a different, more
  permissive outstanding invitation for the same identity rather than the one actually used.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Issue two invitations with different entitlement levels for the same identity, complete the
  narrower one, and inspect the resulting entitlement.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q034

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q034
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  No authenticated session capability must be granted on the basis of a secret that has not
  yet passed the strength policy, even momentarily during the registration flow.
WHY_IT_MATTERS: >
  A momentary authenticated window before validation completes is a race condition an
  attacker only needs to win once.
DISCONFIRMING_OBSERVATION: >
  A usable authenticated session can be observed to exist, even briefly, before the submitted
  secret has completed policy validation.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Instrument or time a registration submission to observe whether any authenticated
  capability appears before validation of the secret completes.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q035

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q035
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The first voluntary secret change performed immediately after activation completes must
  still be evaluated against the current policy, not treated as a continuation of the
  already-validated activation step.
WHY_IT_MATTERS: >
  Treating an immediate post-activation change as pre-validated would let a registrant swap
  in a non-compliant secret right after passing the check once.
DISCONFIRMING_OBSERVATION: >
  A policy-violating secret is accepted on a change performed immediately after activation,
  without a fresh policy check.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Complete activation, then immediately submit a secret change to a policy-violating value
  and observe whether it is rejected.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q036

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q036
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  If a registrant can invoke an account-recovery mechanism before their registration is even
  complete, that mechanism must not grant access at a lower strength bar than completing
  registration normally would.
WHY_IT_MATTERS: >
  A recovery path reachable before an account fully exists is an unusual, easily overlooked
  shortcut around the intended registration bar.
DISCONFIRMING_OBSERVATION: >
  Invoking a recovery mechanism against a still-pending registration results in an active
  identity secured by a weaker bar than normal completion would require.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to invoke the recovery mechanism against an identity whose registration has not yet
  completed, and inspect the resulting secret's compliance.
```
## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q037

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q037
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A non-human, service, or integration account provisioned through the same code path as
  self-registration must not inherit an exemption from the strength policy simply because it
  was not created by a human registrant.
WHY_IT_MATTERS: >
  An unflagged exemption for non-human identities is an easy, quiet way for a weak, long-lived
  credential to enter the system.
DISCONFIRMING_OBSERVATION: >
  An account provisioned through the self-registration path for non-human use is found to
  hold a secret that would not satisfy the human-facing policy, with no explicit exception
  recorded.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Provision an account intended for non-human/integration use through the same path as
  self-registration and inspect whether the policy was applied and any exception recorded.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q038

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q038
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Each individual submission attempt of a secret during registration must be evaluated
  against the currently effective policy at the time of that specific submission, not against
  a policy snapshot taken once at the start of the flow.
WHY_IT_MATTERS: >
  A stale snapshot could let a mid-flow configuration change go unenforced for registrants
  already partway through.
DISCONFIRMING_OBSERVATION: >
  A registrant partway through the flow has their final submission evaluated against a policy
  version that was already superseded before that submission occurred.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Begin a registration, change the policy configuration mid-flow, then submit the secret and
  determine which policy version was actually applied.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q039

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q039
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  If registrations can be handled by more than one running instance of the service
  concurrently, all instances must enforce an identical, currently effective policy at any
  given moment.
WHY_IT_MATTERS: >
  Inconsistent enforcement across instances would make policy compliance dependent on which
  instance happened to handle a given request.
DISCONFIRMING_OBSERVATION: >
  Otherwise identical registration submissions handled at the same time by different running
  instances produce different accept/reject outcomes.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Where multiple instances can be identified or influenced, submit identical borderline
  secrets in a way likely to be routed to different instances and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q040

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q040
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Any confirmation notification sent upon successful registration must not include the
  accepted secret in a recoverable form, nor internal policy implementation detail.
WHY_IT_MATTERS: >
  A secret or implementation detail sent in a notification is exposed to every system and
  party that touches that message channel.
DISCONFIRMING_OBSERVATION: >
  A post-registration notification contains the accepted secret in plain or recoverable form,
  or exposes internal policy configuration detail.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Complete registration and inspect the full content of any resulting confirmation
  notification.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q041

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q041
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An identity onboarded via a distinct invitation channel or delivery method must be held to
  the same strength policy as one onboarded via the standard self-service form.
WHY_IT_MATTERS: >
  A secondary onboarding channel added for convenience is a natural place for the policy check
  to be forgotten.
DISCONFIRMING_OBSERVATION: >
  An identity onboarded through an alternate invitation channel accepts a secret that the
  standard self-service form would reject.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Complete onboarding through each available invitation channel with the same
  policy-boundary secret and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q042

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q042
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A lockout response for a pending registration must not itself reveal, to a party without
  access to the invitation, whether that pending registration exists at all.
WHY_IT_MATTERS: >
  A lockout that behaves differently only when a real pending registration exists becomes
  another form of account enumeration.
DISCONFIRMING_OBSERVATION: >
  The lockout response for a genuinely pending registration differs observably from the
  response for a non-existent one, to a party without invitation access.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Trigger the lockout condition against a genuine pending registration and separately against
  a fabricated, non-existent one, and compare the responses.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q043

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q043
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  If any part of the registration request format allows the client to indicate compliance or
  completion of validation, the server must not trust that indication and must re-derive
  compliance itself.
WHY_IT_MATTERS: >
  Trusting a client-supplied compliance flag turns the entire policy into something the caller
  can simply assert away.
DISCONFIRMING_OBSERVATION: >
  Registration completes with a policy-violating secret when the request is crafted to assert
  compliance without the secret actually meeting the policy.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Identify any field in the registration request that could represent a compliance
  indicator; submit a policy-violating secret while asserting compliance and observe the
  outcome.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q044

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q044
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An invitation that has expired or been explicitly revoked must not retain any residual
  capability, such as previewing account details or partially provisioning access, beyond
  simple rejection of the completion attempt.
WHY_IT_MATTERS: >
  A revoked or expired token with any residual capability was not actually revoked, only
  cosmetically disabled.
DISCONFIRMING_OBSERVATION: >
  An expired or revoked invitation token still allows some capability beyond a plain
  rejection, such as retrieving information about the intended account.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Expire or revoke an invitation, then attempt every capability the token format would
  normally allow and inspect each result.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q045

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q045
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A registration abandoned and later retried by the same identity from scratch must be
  evaluated fully against the currently effective policy, with no residual leniency carried
  over from the abandoned attempt.
WHY_IT_MATTERS: >
  A carried-over leniency from a stale, abandoned attempt would make the effective policy
  depend on unrelated history rather than the current rule.
DISCONFIRMING_OBSERVATION: >
  A fresh retry of a previously abandoned registration accepts a secret the current policy
  would otherwise reject, because of state left over from the earlier attempt.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Begin and abandon a registration with policy-adjacent values, then retry from scratch with a
  value the current policy should reject, and observe the outcome.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q046

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q046
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  What the registrant was actually told about the requirements at the moment they registered
  must be reconstructable, and must match what was genuinely enforced at that time.
WHY_IT_MATTERS: >
  A mismatch between displayed requirements and enforced requirements undermines both user
  trust and later compliance review.
DISCONFIRMING_OBSERVATION: >
  The requirements presented to the registrant at signup, when reconstructed, do not match
  what was actually enforced against their submission.
EXPECTED_SURFACE: S5,S6
PRECONDITIONS: >
  Capture the requirements text shown during a specific registration and compare it against
  the policy configuration that can be shown to have actually governed that submission.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q047

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q047
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Repeated invalid activation attempts against a pending registration must be tracked and
  limited independently of an unrelated existing account's login-attempt counter, so that
  abuse against one cannot exhaust or reset the other.
WHY_IT_MATTERS: >
  Shared counters between unrelated protections can let an attacker on one path silently
  affect protection intended for a different path.
DISCONFIRMING_OBSERVATION: >
  Repeated invalid activation attempts against a pending registration are found to affect the
  lockout state of an unrelated, already-existing account, or vice versa.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Generate repeated invalid attempts against a pending registration and separately against an
  unrelated existing account's login, and inspect whether either counter affected the other.
```

## G02-AUTH_PASSWORD_POLICY_SIGNUP-Q048

```yaml
QID: G02-AUTH_PASSWORD_POLICY_SIGNUP-Q048
MODULE: auth_password_policy_signup
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a support or administrative party is permitted to assist a registrant in completing
  activation on their behalf, the secret ultimately set must still pass through the identical
  policy check as unassisted self-completion.
WHY_IT_MATTERS: >
  An assisted path is a plausible, well-intentioned reason for a shortcut to creep in and
  quietly weaken the policy for a whole class of registrations.
DISCONFIRMING_OBSERVATION: >
  A secret set through a support-assisted completion is accepted despite violating the policy
  that would apply to unassisted self-completion.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Have a support or administrative party assist in completing an activation with a
  policy-violating secret and observe whether it is accepted.
```
