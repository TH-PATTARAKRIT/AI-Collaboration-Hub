# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / auth_password_policy_portal Module MVQ Bank

**Document ID:** GMVQ-G02-AUTH_PASSWORD_POLICY_PORTAL-MVQ48-V1.00  
**Group:** G02 IDENTITY_ACCESS  
**Module Metadata:** `auth_password_policy_portal`  
**Wave:** W1  
**Author Cell:** TEAM 10 (GMVQ Question Factory — Primary MVQ Authoring)  
**Review Cell:** PENDING  
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN / REVISED R1  
**CHANGE_REASON (R1):** Returned by GMVQ MASTER AUDIT TEAM M2 under Boss directive SMEPLUS-GMVQ-20P-5AUDIT-20260927-004 — closed-vocabulary (RISK_TIER / OUTPUT_CLASS) field-value defect(s) corrected by production (R1). 4 RISK_TIER values (LOW) outside the enum re-tiered per-question.
**actual_mvq_count:** 48  
**Lane A / Lane B:** NOT STARTED for this module until batch freeze is recorded

## Purpose

This bank supplies module-specific research questions (MVQ) for the blind two-lane study, extending the 55-question standard bank for this module. It targets the same policy regime as applied to external, customer-facing users: whether the external regime may be configured weaker than the internal one and whether that gap is visible; whether one identity can hold both an internal and an external role and, if so, which regime governs; whether a weaker external policy can become a route to internal data; and self-service reset flows operated by someone with no administrator relationship to the account.

## Control

- Every question carries a falsifiable `DISCONFIRMING_OBSERVATION`.
- No padding: each question tests a distinct material hypothesis; none is cut to hit a round number.
- Question text is source-neutral: no vendor or product name, no technical identifier, and no reference to the module's own metadata name anywhere outside the `MODULE:` field.
- Questions are not evidence. A later ANSWERED state requires actual artifact/evidence from Lane A or Lane B.
- `MODULE + QID` is only a Research Evidence Join Key; no formal coverage is derived from this bank alone.
- This document is PREPARED ONLY / NOT APPROVED / NOT FROZEN. It is not Boss Final Approval.

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q001

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q001
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The policy applied to external, customer-facing users can be configured independently of the
  internal policy, without the platform silently forcing the two to be identical.
WHY_IT_MATTERS: >
  Conflating the two configurations removes a tenant's ability to make a deliberate, documented
  choice about the two distinct risk profiles they actually face.
DISCONFIRMING_OBSERVATION: >
  Changing the internal policy configuration also changes the effective external policy (or vice
  versa) with no separate external setting available to prevent it.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Change the internal policy configuration and check whether the effective external policy changes
  as a side effect, and whether an independent external setting exists.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q002

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q002
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When the external policy is configured weaker than the internal one, that gap is visible on the
  configuration screen or in a report, not hidden inside a single merged control.
WHY_IT_MATTERS: >
  An invisible gap between the two regimes means an administrator can weaken the external side
  without ever realizing the two populations now diverge.
DISCONFIRMING_OBSERVATION: >
  The administrative interface presents internal and external policy strength in a way that does
  not let an administrator see, at a glance, that the external configuration is weaker than the
  internal one.
EXPECTED_SURFACE: S5,S6,S7
PRECONDITIONS: >
  Configure the external policy weaker than the internal one and review the administrative
  interface for a visible indication of the divergence.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q003

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q003
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An identity holding both an internal and an external role is evaluated against the stricter of
  the two applicable secret policies for any credential used to reach internal-scope data.
WHY_IT_MATTERS: >
  If the weaker policy applies whenever it is more convenient, the external regime effectively
  becomes the real security level for internal access too.
DISCONFIRMING_OBSERVATION: >
  A dual-role identity's credential, compliant only with the weaker external policy, is accepted
  for authentication that then grants internal-scope access.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Create an identity holding both roles, set a secret that satisfies only the weaker external
  policy, and attempt to reach internal-scope functionality with it.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q004

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q004
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An identity is not permitted to be simultaneously and ambiguously bound to both the internal and
  external policy regime for the same credential; where dual roles exist, the binding to a
  governing policy is explicit and singular.
WHY_IT_MATTERS: >
  An ambiguous binding means no one, including the platform itself, can say with confidence which
  rule actually governed a given credential decision.
DISCONFIRMING_OBSERVATION: >
  For a dual-role identity, the platform cannot identify a single governing policy for its
  credential, or applies different policies to the same credential value depending on which path
  is asked.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Inspect the configuration and enforcement path for a dual-role identity's single credential and
  determine whether exactly one governing policy is identifiable.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q005

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q005
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A session or token obtained by authenticating under the weaker external regime cannot be
  exchanged, escalated, or reused to obtain internal-scope authorization without a fresh
  authentication event evaluated under the internal regime.
WHY_IT_MATTERS: >
  A silent exchange path turns the weaker, more exposed external control into the effective
  control for internal-scope data as well.
DISCONFIRMING_OBSERVATION: >
  A session established through external authentication is accepted, without a fresh internal-
  policy authentication event, for an action or resource scoped to internal data.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Authenticate through the external path and attempt to reach internal-scope functionality using
  only the resulting session, with no separate internal authentication step.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q006

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q006
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Any elevation of an external identity's access to an internal-scope capability requires a fresh
  authentication event evaluated against the internal policy, rather than silent inheritance of
  the existing external session's trust level.
WHY_IT_MATTERS: >
  Silent inheritance means the weakest authentication event in the identity's history effectively
  governs its highest level of access.
DISCONFIRMING_OBSERVATION: >
  An external session gains an internal-scope capability with no new authentication event
  evaluated against the internal policy.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  From an active external session, attempt to reach a capability documented as internal-scope and
  observe whether a fresh, internally-governed authentication step is required.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q007

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q007
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The reuse/history restriction for the external population is independently enforced and does not
  default to no restriction merely because the internal population's policy happens to be
  stricter.
WHY_IT_MATTERS: >
  A restriction that only exists on paper for the stricter population leaves the larger, more
  exposed external population without a working reuse control at all.
DISCONFIRMING_OBSERVATION: >
  An external identity is able to reuse a recently-used secret even though a reuse restriction is
  documented as applying to the external population.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Rotate an external identity's secret through the configured history window and attempt to reuse
  an earlier value.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q008

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q008
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A lockout threshold applies to the external population and is not silently disabled on the
  assumption that the population is too large or too low-trust to bother enforcing it.
WHY_IT_MATTERS: >
  A public-facing population with no lockout at all is the easiest possible target for automated
  credential guessing at scale.
DISCONFIRMING_OBSERVATION: >
  Repeated failed attempts against an external identity produce no lockout regardless of how many
  are attempted.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Run a large number of consecutive failed authentication attempts against a test external
  identity and observe whether lockout occurs.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q009

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q009
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Lockout state for an external identity is isolated from the lockout state of any internal
  identity that shares an underlying record or is otherwise linked to it.
WHY_IT_MATTERS: >
  A shared lockout counter lets an external attacker's failed attempts deny access to an internal
  identity that has no reason to be affected by public-facing traffic.
DISCONFIRMING_OBSERVATION: >
  Repeated failed attempts against an external identity cause lockout, or a change in failed-
  attempt count, for a linked internal identity.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Link an external identity to an internal record where the platform supports this, then run
  repeated failed attempts against the external side and monitor the internal side's lockout
  state.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q010

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q010
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A self-service reset for an external identity requires proof of ownership of a contact channel
  on file, not merely knowledge of the account identifier, and completes without any administrator
  or support action.
WHY_IT_MATTERS: >
  A reset gated only by a known identifier such as an email address that is itself often public
  turns the reset flow into a full account-takeover path.
DISCONFIRMING_OBSERVATION: >
  A self-service reset for an external identity can be completed to the point of setting a new
  secret using only the account identifier, without any proof of control over a channel on file.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to complete the self-service reset flow for a test external identity supplying only its
  identifier and see how far the flow proceeds without channel proof.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q011

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q011
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The contact address used for reset verification cannot be changed within the same
  unauthenticated interaction that then triggers a reset for that identity, without a separate
  verification step.
WHY_IT_MATTERS: >
  Allowing both in one unauthenticated flow lets an attacker redirect the recovery channel to
  themselves and then immediately harvest the reset, all before the legitimate owner notices
  anything.
DISCONFIRMING_OBSERVATION: >
  An unauthenticated actor is able to change the contact channel on file and then successfully use
  a reset sent to the new channel, all within a single unauthenticated interaction.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  From an unauthenticated context, attempt to change the contact channel for a test external
  identity and then trigger and complete a reset to the new channel.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q012

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q012
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Completing a self-service reset for an external identity invalidates all previously active
  sessions and any other outstanding reset link for that identity.
WHY_IT_MATTERS: >
  Leaving old sessions or links alive after a reset defeats the purpose of the reset, since
  whoever had a prior session or link retains access exactly as before.
DISCONFIRMING_OBSERVATION: >
  After a self-service reset completes, a session that was active before the reset, or an earlier
  still-outstanding reset link, continues to work.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Establish an active session and an outstanding reset link for a test external identity, complete
  a fresh reset, then test both the prior session and the earlier link.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q013

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q013
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The response returned by the self-service reset request is the same regardless of whether the
  submitted identifier corresponds to a real external identity.
WHY_IT_MATTERS: >
  A distinguishable response turns the reset form into a tool for confirming which identifiers are
  valid, which is the first step of a targeted attack.
DISCONFIRMING_OBSERVATION: >
  The reset-request response, its timing, or its wording differs in an observable way between a
  valid and an invalid target identifier.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Submit a reset request for a known valid external identifier and a known invalid one, and
  compare the responses in content and timing.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q014

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q014
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The strength rule applied to a secret chosen at the end of the external self-service reset flow
  is the same rule declared for the external population generally, not a lesser check exclusive to
  that flow.
WHY_IT_MATTERS: >
  A weaker check confined to the reset flow becomes the standard way any attacker restores control
  with a trivially weak secret.
DISCONFIRMING_OBSERVATION: >
  A secret that would be rejected by the ordinary external change form is accepted at the end of
  the self-service reset flow.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt an identical policy-violating secret through the ordinary external change path and
  through the self-service reset flow, and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q015

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q015
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The secret chosen at external self-registration is checked against the external population's
  policy at the moment it is chosen, with no window in which an unvalidated secret is temporarily
  in force.
WHY_IT_MATTERS: >
  A grace window before validation is applied gives a newly created account a period of
  effectively no protection, during which it is just as attractive a target as any established
  one.
DISCONFIRMING_OBSERVATION: >
  A newly self-registered external identity can authenticate using a secret that fails the
  declared policy, for any period before a later validation catches up.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Complete external self-registration with a policy-violating secret and immediately attempt to
  authenticate with it.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q016

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q016
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A change to the external policy configuration takes effect for existing external credentials on
  a deterministic, documented schedule, rather than being left ambiguous or indefinitely deferred.
WHY_IT_MATTERS: >
  An ambiguous effective date means no one, including the platform operator, can state with
  confidence whether a given credential is currently governed by the old or new rule.
DISCONFIRMING_OBSERVATION: >
  After confirming an external policy change is saved, there is no documented or observable point
  at which existing external credentials become governed by the new rule.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change the external policy configuration and attempt to determine the documented point at which
  existing external credentials become subject to it.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q017

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q017
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Changing the external policy configuration does not also silently change the effective internal
  policy through shared underlying configuration storage.
WHY_IT_MATTERS: >
  A shared storage bug that leaks a change across the boundary means the two regimes were never
  actually independent, undermining any documented separation.
DISCONFIRMING_OBSERVATION: >
  Changing only the external policy configuration is observed to also change the effective
  internal policy enforcement.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Change the external policy configuration and immediately re-test a borderline secret against an
  internal identity to see if internal enforcement shifted.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q018

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q018
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An administrator scoped to one tenant's external-facing area cannot view or edit the external
  policy configuration belonging to a different tenant.
WHY_IT_MATTERS: >
  Cross-tenant visibility into a competitor or unrelated customer's security posture, or the
  ability to alter it, is a direct breach of the multi-tenant isolation the platform promises.
DISCONFIRMING_OBSERVATION: >
  An administrator scoped to one tenant is able to view or change the external policy
  configuration recorded for a different tenant.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Using an administrator account scoped to tenant A's external area, attempt to view and then edit
  tenant B's external policy configuration.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q019

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q019
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where one external identity can reach more than one tenant's data, the weaker policy enforced
  for one tenant does not become the effective policy governing that identity's access to a
  different tenant's data.
WHY_IT_MATTERS: >
  A shared-identity weak link means the least secure tenant sets the real security level for every
  tenant that identity can reach.
DISCONFIRMING_OBSERVATION: >
  An external identity authenticated under a weaker tenant's policy is able to reach a different
  tenant's data without a fresh authentication event evaluated against that second tenant's own
  policy.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set up an external identity reachable from two tenants with differing policy strength,
  authenticate under the weaker tenant, and attempt to reach the stricter tenant's data.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q020

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q020
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The audit trail for the external population records the policy version governing each accept,
  reject, or lockout decision, to the same standard applied to the internal population.
WHY_IT_MATTERS: >
  A lesser audit standard for the larger, more exposed external population leaves the population
  most likely to be attacked the hardest one to investigate afterward.
DISCONFIRMING_OBSERVATION: >
  An enforcement decision for an external identity cannot be tied to the policy version that was
  active at the time, even though the equivalent internal record can be.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Trigger an enforcement decision for an external identity and an internal identity under the same
  policy version, then compare what each audit record retains.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q021

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q021
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A configuration change that weakens the external policy is distinguishable in the retained
  change history from routine external-population maintenance.
WHY_IT_MATTERS: >
  If a weakening blends into routine changes, no one reviewing the external-facing configuration
  will notice a real reduction in protection.
DISCONFIRMING_OBSERVATION: >
  The change history for the external policy does not let a reviewer distinguish, without
  inspecting every field, a change that weakened the policy from one that did not.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Make one weakening and one unrelated maintenance change to the external policy configuration and
  review the resulting history entries.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q022

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q022
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where second-factor enforcement can differ between the external and internal populations, a
  weaker or absent external second factor does not reduce the second-factor requirement for any
  internal-scope action reached from an external session.
WHY_IT_MATTERS: >
  Without this separation, the weakest population's second-factor posture becomes the real posture
  protecting internal data, regardless of what is documented for internal users.
DISCONFIRMING_OBSERVATION: >
  An internal-scope action is reachable from a session that only ever satisfied the weaker or
  absent external second-factor requirement.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Establish an external session with no second factor satisfied and attempt to reach an internal-
  scope action from it.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q023

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q023
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An external identity subject to lockout cannot have that lockout effectively cleared by going
  through an unrelated public entry point, such as re-registration, that recreates or reactivates
  the same underlying identity.
WHY_IT_MATTERS: >
  A reactivation loophole turns the lockout control into a purely cosmetic delay that any attacker
  can defeat by simply re-registering.
DISCONFIRMING_OBSERVATION: >
  Re-registering with the same identifying details as a locked-out external identity results in a
  usable, unlocked identity without going through the defined recovery path.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Lock out a test external identity, then attempt to re-register using the same identifying
  details and test whether the resulting identity is unlocked.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q024

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q024
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Where a maximum secret age applies to the external population, an external identity that
  authenticates only rarely still faces the rotation check the first time it authenticates after
  the age is exceeded.
WHY_IT_MATTERS: >
  Exempting infrequent external users means the accounts least likely to be actively monitored by
  their owner are also the ones left running on the oldest secrets.
DISCONFIRMING_OBSERVATION: >
  A rarely-authenticating external identity is allowed in well past its maximum age with no forced
  rotation prompt.
EXPECTED_SURFACE: S1,S8
PRECONDITIONS: >
  Let a maximum-age threshold lapse for a dormant test external identity, then authenticate as
  that identity and observe whether a forced change is triggered.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q025

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q025
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  A reset link issued for an external identity is scoped to one specific pending request and is
  invalidated the moment a subsequent request is made for the same identity.
WHY_IT_MATTERS: >
  Without this, an older leaked link stays usable indefinitely even after the legitimate user
  requests, and presumably uses, a fresh one.
DISCONFIRMING_OBSERVATION: >
  An earlier reset link for an external identity remains usable after a later reset request has
  been made for that same identity.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Request a reset for a test external identity, request a second reset for the same identity, and
  attempt to use the first link.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q026

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q026
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A rejected external secret submission produces feedback specific enough to guide a legitimate
  customer, without disclosing rule detail beyond what usability requires.
WHY_IT_MATTERS: >
  A public-facing form is the most exposed possible place to leak exact policy thresholds, since
  anyone on the internet can probe it repeatedly with no relationship to the business.
DISCONFIRMING_OBSERVATION: >
  The public rejection response discloses precise rule thresholds beyond what is needed for a
  customer to correct their input.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Submit several distinct policy-violating secrets through the external form and compare the
  specificity of each rejection against the minimum needed for usability.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q027

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q027
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An external identity cannot set its secret to a value equal to, or a trivial transform of, its
  own identifying detail that is shown to it elsewhere in the interface, such as an account or
  reference number.
WHY_IT_MATTERS: >
  A secret derived from a value the customer sees printed on their own invoices or order
  confirmations is trivially guessable by anyone who also sees that document.
DISCONFIRMING_OBSERVATION: >
  An external identity successfully sets its secret to a value equal to, or a simple variant of,
  an identifying number or detail shown to it elsewhere in the same interface.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Attempt to set an external test identity's secret to a value matching an account or reference
  number visible to it elsewhere in the interface.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q028

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q028
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where an integration or programmatic path exists for the external-facing area, secrets set or
  validated through it are checked against the same policy as the interactive external form.
WHY_IT_MATTERS: >
  A programmatic path with a lesser check becomes the quiet route of choice for scripted account
  creation or takeover attempts.
DISCONFIRMING_OBSERVATION: >
  A secret rejected by the interactive external form is accepted through the
  programmatic/integration path for the same population.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Submit an identical policy-violating secret through the interactive external form and through
  the documented programmatic path, and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q029

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q029
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The reset process changes an external identity's secret without disclosing the new or old value
  to the support or administrative actor who initiated or assisted it.
WHY_IT_MATTERS: >
  A reset flow that exposes the resulting secret to a staff member turns every support interaction
  into a potential account-takeover opportunity.
DISCONFIRMING_OBSERVATION: >
  A support or administrative actor assisting with a reset is able to see or otherwise learn the
  resulting secret value.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Have a support-role actor initiate or assist an external identity's reset and check whether the
  resulting secret value is exposed to that actor at any point.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q030

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q030
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where an external identity is deprovisioned and later re-created for the same person, any
  lingering lockout or failure history from the earlier identity does not silently carry over
  without being disclosed to the person.
WHY_IT_MATTERS: >
  An undisclosed carry-over could leave a returning customer permanently confused or blocked by
  history they have no way of knowing exists.
DISCONFIRMING_OBSERVATION: >
  A newly re-created external identity for a previously deprovisioned person inherits a lockout or
  failure-count state from the earlier identity, with no explanation surfaced anywhere.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Deprovision a test external identity with an existing failure history, re-create it for the same
  person, and check the new identity's initial lockout state and any disclosure.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q031

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q031
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two concurrent self-service reset attempts for the same external identity resolve to one
  deterministic, recorded final secret rather than a window where two different secrets both
  appear to work.
WHY_IT_MATTERS: >
  A race that leaves two secrets briefly valid is exactly the kind of gap that turns an attacker
  racing a legitimate user's reset into a successful takeover.
DISCONFIRMING_OBSERVATION: >
  After two concurrent reset attempts for the same external identity, more than one of the
  resulting candidate secrets can successfully authenticate.
EXPECTED_SURFACE: S1,S3,S6
PRECONDITIONS: >
  Trigger two reset flows for the same external identity at nearly the same time, complete both
  with different secrets, and test which values authenticate afterward.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q032

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q032
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A policy exemption granted to a specific external identity, such as for a legacy account, is
  time-bounded and recorded, not an untracked permanent carve-out.
WHY_IT_MATTERS: >
  An untracked permanent exemption is a standing weak point that nobody will ever revisit or
  question once the person who granted it has moved on.
DISCONFIRMING_OBSERVATION: >
  An external identity holds a policy exemption with no recorded expiry, justification, or origin.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Locate an external identity known to hold a policy exemption and check whether it is recorded
  with a time bound and justification.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q033

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q033
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the external population's policy is left unconfigured, the platform applies a defined safe
  default rather than no restriction at all, and that default is not weaker than a documented
  minimum.
WHY_IT_MATTERS: >
  An unconfigured public-facing population defaulting to no restriction is the single most
  exploitable misconfiguration a deployment can make, and the one least likely to be noticed.
DISCONFIRMING_OBSERVATION: >
  With no explicit external policy configured, an external identity can set a trivially weak
  secret with no rejection.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Ensure no explicit external policy is configured and attempt to set a trivially weak secret for
  a test external identity.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q034

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q034
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An outside party who deliberately locks out a known external identity through repeated failed
  attempts leaves at least a detectable audit signature distinguishing the pattern from an
  ordinary accidental self-lockout.
WHY_IT_MATTERS: >
  Without any distinguishing signal, a business has no way to tell a wave of malicious lockouts
  from ordinary customer forgetfulness, and cannot respond.
DISCONFIRMING_OBSERVATION: >
  A deliberate lockout attack against a known external identity produces an audit record
  indistinguishable from an ordinary accidental lockout by the account's own owner.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  From an unauthenticated context, deliberately trigger lockout for a known test external identity
  and inspect the resulting audit record for any distinguishing pattern.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q035

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q035
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Where the external area is reachable through a shared entry point before a specific tenant
  context is established, the policy applied at that point is explicit and documented, not an
  accidental default.
WHY_IT_MATTERS: >
  An undocumented default at a shared, pre-tenant entry point is easy to overlook during a policy
  review focused on per-tenant configuration screens.
DISCONFIRMING_OBSERVATION: >
  The policy actually enforced at the shared pre-tenant entry point does not match any documented
  configuration, or no configuration for that point can be found at all.
EXPECTED_SURFACE: S1,S5,S7
PRECONDITIONS: >
  Identify the shared entry point reached before tenant context is established and compare its
  enforced policy against documented configuration.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q036

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q036
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Changing an external identity's secret does not silently terminate or silently preserve
  unrelated in-flight transactions initiated by that identity in a way that is undocumented.
WHY_IT_MATTERS: >
  An undocumented side effect on unrelated in-flight work means a customer changing a forgotten
  secret could unexpectedly lose or unexpectedly retain a transaction they did not intend to
  affect.
DISCONFIRMING_OBSERVATION: >
  An in-flight transaction started by an external identity is silently terminated, or silently
  continues with elevated effect, purely as a side effect of that identity changing its secret,
  with no documented behavior describing this.
EXPECTED_SURFACE: S1,S3,S8
PRECONDITIONS: >
  Start an in-flight transaction as a test external identity, change that identity's secret mid-
  transaction, and observe the transaction's state against documented behavior.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q037

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q037
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where a customer-facing mobile or alternate client exists, it enforces the identical external
  policy as the web entry point, rather than a separately configured or forgotten rule set.
WHY_IT_MATTERS: >
  A forgotten secondary client is a common way a supposedly-retired weak rule set keeps running in
  production undetected.
DISCONFIRMING_OBSERVATION: >
  A secret rejected through the web entry point is accepted through the mobile or alternate client
  for the same external population.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Submit an identical policy-violating secret through the web entry point and through the
  mobile/alternate client, and compare outcomes.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q038

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q038
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The failed-attempt counter used for an external identity's lockout is not incremented by
  unrelated automated traffic, such as a health check or monitoring probe, hitting the same public
  endpoint.
WHY_IT_MATTERS: >
  Contamination from unrelated traffic could lock out real customers as an unintended side effect
  of routine infrastructure monitoring.
DISCONFIRMING_OBSERVATION: >
  A health check, monitoring probe, or other non-attempt traffic against the public endpoint
  measurably advances a real external identity's failed-attempt counter.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Identify any automated traffic hitting the public authentication endpoint and check whether it
  affects a real test identity's failed-attempt counter.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q039

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q039
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The self-service reset flow's claim of requiring proof of possession or control of a factor
  beyond the account identifier is one the platform's own configuration can actually substantiate,
  not merely an assumption.
WHY_IT_MATTERS: >
  A documented control that turns out, on inspection, to reduce to bare knowledge of the
  identifier gives a false sense of protection to whoever relies on the documentation.
DISCONFIRMING_OBSERVATION: >
  Tracing the actual reset flow shows that completing it requires nothing more than the account
  identifier, despite documentation describing a stronger possession-based control.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Trace the exact steps of the self-service reset flow for a test external identity and compare
  what is actually required against what is documented.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q040

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q040
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Where an external identity is linked to an internal sponsor or referring employee, a weakness in
  the external policy cannot be used to reach or infer data scoped to the internal sponsor's own
  account.
WHY_IT_MATTERS: >
  A sponsor link is exactly the kind of quiet cross-boundary relationship that turns a low-value
  external account compromise into a route toward high-value internal data.
DISCONFIRMING_OBSERVATION: >
  Compromising or manipulating a linked external identity's credential yields access to, or
  information about, data scoped to its internal sponsor's own account.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Establish a test external identity linked to an internal sponsor account, then attempt to reach
  or infer sponsor-scoped data using only the external identity's access.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q041

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q041
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A person who happens to use the same secret value for both an internal and an external identity
  does not thereby cause the platform to treat passing one policy's check as also satisfying the
  other's.
WHY_IT_MATTERS: >
  An implicit cross-check would mean the weaker regime's acceptance criteria silently govern the
  stronger regime whenever the two secrets coincide.
DISCONFIRMING_OBSERVATION: >
  Setting a secret that satisfies only the weaker regime's rule is nonetheless accepted for the
  stronger regime's identity because the same value happens to be on file for the other.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Set the same secret value, valid only under the weaker regime's rule, on both a linked internal
  and external identity, and test acceptance against the stricter regime.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q042

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q042
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Whether a tenant is permitted to configure the external policy weaker than the internal one is
  itself an explicit control point with a recorded decision, not an automatic default inherited
  with no record of the choice.
WHY_IT_MATTERS: >
  An unrecorded default permission to weaken the external side means no one can later show that
  the divergence was a deliberate, reviewed decision rather than an oversight.
DISCONFIRMING_OBSERVATION: >
  A tenant's external policy is weaker than its internal one with no recorded decision anywhere
  authorizing that divergence.
EXPECTED_SURFACE: S6,S7
PRECONDITIONS: >
  Locate a tenant whose external policy is weaker than its internal one and check for a recorded
  decision authorizing the divergence.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q043

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q043
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Abandoning a self-service reset flow before completion leaves the external identity's previous
  secret and lockout state completely unchanged.
WHY_IT_MATTERS: >
  A half-applied abandoned reset could leave a customer's account in an undocumented, possibly
  inaccessible, intermediate state.
DISCONFIRMING_OBSERVATION: >
  After abandoning a self-service reset partway through, the external identity's original secret
  no longer authenticates, or its lockout state has changed.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Begin a self-service reset for a test external identity, abandon it before the final step, and
  test the original secret and lockout state afterward.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q044

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q044
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Where multiple external users share one indirect account, a lockout triggered by one
  participant's failed attempts is distinguishable in the trail from a lockout that would affect
  the others, rather than silently degrading the shared environment with no attribution.
WHY_IT_MATTERS: >
  Without attribution, a shared account's other legitimate users have no way to understand or
  respond to a lockout someone else caused.
DISCONFIRMING_OBSERVATION: >
  A lockout on a shared indirect account occurs with no record distinguishing which participant's
  activity triggered it.
EXPECTED_SURFACE: S1,S6
PRECONDITIONS: >
  Simulate two participants on a shared external account, have one trigger lockout through failed
  attempts, and review the resulting record for attribution.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q045

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q045
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  The external population's reuse/history restriction applies the same history window whether the
  new secret is chosen by the identity itself or set on its behalf by a privileged actor.
WHY_IT_MATTERS: >
  A privileged reset exempted from the reuse window becomes the easy way to reinstate a secret the
  ordinary flow would have blocked.
DISCONFIRMING_OBSERVATION: >
  A privileged actor resetting an external identity's secret on its behalf is able to set a value
  the identity's own reuse-restricted change would have rejected.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Establish a recent-history value for a test external identity, then have a privileged actor
  attempt to reset it to that same value on the identity's behalf.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q046

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q046
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A rate limit or throttling control on the external self-service reset endpoint is a documented
  decision distinct from the lockout threshold, and the two are not silently conflated into a
  single control.
WHY_IT_MATTERS: >
  Conflating the two hides which control is actually doing the work, making it impossible to
  reason about what happens if one is disabled or misconfigured.
DISCONFIRMING_OBSERVATION: >
  Disabling or changing the lockout threshold is observed to also change the throttling behavior
  of the reset endpoint, or no documentation distinguishes the two controls.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Change the lockout threshold configuration and observe whether the reset endpoint's throttling
  behavior changes as a side effect, and check for documentation distinguishing the two.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q047

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q047
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Rolling back the external policy configuration to a prior version does not automatically treat a
  previously-rejected external secret as valid without a fresh evaluation event.
WHY_IT_MATTERS: >
  Silent revalidation on rollback could quietly reinstate a secret rejected for good reason, with
  no new record showing an actual evaluation took place.
DISCONFIRMING_OBSERVATION: >
  After an external policy rollback, a secret previously rejected under the newer policy becomes
  an identity's active secret with no new evaluation event recorded.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Have an external identity's secret change rejected under the current policy, roll the external
  policy back, and check whether the rejected value becomes active without a new event.
```

## G02-AUTH_PASSWORD_POLICY_PORTAL-Q048

```yaml
QID: G02-AUTH_PASSWORD_POLICY_PORTAL-Q048
MODULE: auth_password_policy_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A time-zone or clock difference between an external user's own location and the deciding system
  does not shift an expiry or lockout-release decision in a way that unpredictably extends or
  shortens the effective window.
WHY_IT_MATTERS: >
  An externally-facing population spans many time zones by nature, so any clock sensitivity in
  these decisions is far more likely to be triggered here than internally.
DISCONFIRMING_OBSERVATION: >
  An external identity's lockout release or secret expiry point changes in a way attributable to
  its reported time zone or clock offset rather than to a fixed, absolute point in time.
EXPECTED_SURFACE: S1,S7,S8
PRECONDITIONS: >
  Test lockout release and expiry timing for external identities reporting different time zones
  and compare against a fixed reference point.
```

