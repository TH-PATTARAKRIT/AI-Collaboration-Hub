# SMEsPlus ENTERPRISE SUITE
## GMVQ — G02 IDENTITY_ACCESS / auth_passkey_portal Module Adversarial MVQ Bank

**Document ID:** GMVQ-G02-AUTH_PASSKEY_PORTAL-MVQ48-V1.00
**Group:** G02 IDENTITY_ACCESS
**Module Metadata:** `auth_passkey_portal`
**Wave:** W1
**Author Cell:** TEAM 09 (Primary MVQ Authoring)
**Review Cell:** PENDING
**Status:** DRAFT / AUTHORING COMPLETE / NOT FROZEN
**actual_mvq_count:** 48
**Standard Bank Reference:** 55 shared standard questions (already authored elsewhere, not reproduced here); research depth = 55 + 48 = 103

## Purpose

This bank supplies module-specific research questions (MVQ) for a blind two-lane clean-room
study of `auth_passkey_portal`. Lane A reads reference source; Lane B observes a running system and never
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

## G02-AUTH_PASSKEY_PORTAL-Q001

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q001
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  Enrolling a device-bound credential for an external, customer-facing identity requires evidence
  of that identity's relationship to a real, existing account or engagement, not merely a claimed
  identity supplied at signup.
WHY_IT_MATTERS: >
  Without a check against a real relationship, anyone could self-register a plausible-looking
  external identity and immediately obtain a phishing-resistant credential that then appears
  authoritative.
DISCONFIRMING_OBSERVATION: >
  An external identity with no verifiable underlying relationship record is able to complete
  enrolment and receive a working credential.
EXPECTED_SURFACE: S1,S3,S4
PRECONDITIONS: >
  Attempt self-registration and enrolment for an external identity that has no corresponding
  relationship or account record on the business side.
```
## G02-AUTH_PASSKEY_PORTAL-Q002

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q002
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The identity-proofing performed before allowing an external user to enrol this credential is
  explicitly weaker, and documented as such, than the proofing an internal identity undergoes
  before the same credential type is issued to them.
WHY_IT_MATTERS: >
  If the difference in proofing rigor is undocumented, nobody has actually decided how much trust
  to place in an external enrolment, and the gap becomes invisible risk rather than an accepted
  trade-off.
DISCONFIRMING_OBSERVATION: >
  No documented distinction exists between the proofing steps required for external enrolment and
  those required for internal enrolment, or the external process is found to demand less evidence
  than any stated policy claims.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Compare the concrete steps required to complete enrolment as an external user against the steps
  required for an internal user, and check both against any documented proofing policy.
```
## G02-AUTH_PASSKEY_PORTAL-Q003

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q003
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  An external identity's device-bound credential is tied to a specific underlying customer
  relationship record, so that the credential's continued validity is a function of that
  relationship remaining active, not a standalone artifact independent of it.
WHY_IT_MATTERS: >
  If the credential floats free of the relationship it was meant to represent, ending the
  relationship on the business side does nothing to actually cut off system access.
DISCONFIRMING_OBSERVATION: >
  The relationship record underlying an external identity's access is deleted or marked ended, yet
  the associated credential still authenticates successfully afterward.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Enrol a credential for an external identity tied to a specific relationship record, then end
  that relationship through the normal business process and attempt authentication.
```
## G02-AUTH_PASSKEY_PORTAL-Q004

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q004
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Ending the underlying customer relationship invalidates the associated external credential at
  the same time as the relationship itself is closed, not after a separate, later administrative
  step.
WHY_IT_MATTERS: >
  A gap between the business decision to end a relationship and the technical revocation of access
  is exactly the kind of process seam that gets missed under normal workload.
DISCONFIRMING_OBSERVATION: >
  The relationship is marked ended in the business record while the external identity's credential
  remains fully functional with no automatic link between the two events.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  End a relationship record through its normal closing process and immediately test whether the
  associated credential is still usable, without performing any separate manual revocation step.
```
## G02-AUTH_PASSKEY_PORTAL-Q005

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q005
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When more than one external individual is entitled to act for a single customer relationship,
  each individual enrols and holds their own distinct credential, and revoking one individual's
  credential does not affect the others still entitled under the same relationship.
WHY_IT_MATTERS: >
  Treating a shared relationship as a single undifferentiated access point would make it
  impossible to remove one departed contact person without disrupting everyone else at that
  customer.
DISCONFIRMING_OBSERVATION: >
  Two individuals acting for the same customer relationship are found to share one credential
  record, or revoking one individual's credential also disables another individual's separate,
  still-valid credential.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Enrol credentials for two distinct individuals under the same customer relationship, then revoke
  one individual's credential and test the other's.
```
## G02-AUTH_PASSKEY_PORTAL-Q006

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q006
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An external user who loses access to their enrolled device has a self-service recovery path that
  does not require action from internal staff for the ordinary case.
WHY_IT_MATTERS: >
  Customer-facing recovery that mandates staff involvement for every lost device does not scale
  and creates pressure to weaken the process under support load.
DISCONFIRMING_OBSERVATION: >
  An external user with no working device has no available recovery option except contacting and
  waiting on internal staff, with no self-service path offered at all.
EXPECTED_SURFACE: S3,S5
PRECONDITIONS: >
  Simulate a lost device for a test external identity and attempt every recovery option presented
  to that user directly, without staff involvement.
```
## G02-AUTH_PASSKEY_PORTAL-Q007

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q007
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Whatever self-service recovery path is offered to an external user carries assurance comparable
  to the credential it replaces, and is not a materially weaker channel — such as a bare email
  link with no further proof — left permanently available as an easier way in.
WHY_IT_MATTERS: >
  A weak, always-available recovery channel becomes the actual attack surface for external
  accounts, since it is reachable by anyone claiming to be the customer without needing to defeat
  the stronger credential at all.
DISCONFIRMING_OBSERVATION: >
  The self-service recovery path can be completed using only a factor materially weaker than the
  device-bound credential it replaces, with no additional friction, delay, or verification step
  beyond that weaker factor.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  Trigger the self-service recovery path for a test identity and record the complete set of proof
  actually required to complete it.
```
## G02-AUTH_PASSKEY_PORTAL-Q008

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q008
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When internal staff perform a recovery or reset on behalf of an external user, that action is
  recorded distinctly from an external user's own self-service recovery, identifying the staff
  member who performed it.
WHY_IT_MATTERS: >
  Staff-assisted recovery for an external account is a support action with real risk of social
  engineering; without distinct attribution, it cannot be reviewed or challenged later.
DISCONFIRMING_OBSERVATION: >
  A staff-performed recovery for an external identity's credential produces a record
  indistinguishable from that identity's own self-service action, with no attribution to the staff
  member involved.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform a credential recovery for a test external identity through the internal staff interface
  and inspect the resulting audit record for staff attribution.
```
## G02-AUTH_PASSKEY_PORTAL-Q009

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q009
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A session or token established by an external, customer-facing identity's authentication cannot
  be used to reach internal-only administrative surfaces or data outside the scope of that
  customer relationship.
WHY_IT_MATTERS: >
  The entire justification for a separate external regime collapses if a credential meant for the
  customer-facing area can still be used to reach internal systems.
DISCONFIRMING_OBSERVATION: >
  A session established through external portal authentication is accepted, even partially, by an
  internal-only interface or endpoint not intended for external users.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Authenticate as an external identity through the portal and attempt to reach internal-only
  administrative interfaces or endpoints using the resulting session.
```
## G02-AUTH_PASSKEY_PORTAL-Q010

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q010
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An external identity is scoped strictly to the data belonging to its own customer relationship,
  so its access does not depend on any assumption that it will never attempt to reach data
  belonging to a different relationship or an internal-only area.
WHY_IT_MATTERS: >
  Relying on external users never trying to overreach, rather than on an enforced boundary, is not
  a control at all.
DISCONFIRMING_OBSERVATION: >
  An external identity authenticated for one relationship is able to view or act on data belonging
  to a different customer relationship, or to internal-only records.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Authenticate as an external identity scoped to one relationship and attempt to access records
  known to belong to a different relationship.
```
## G02-AUTH_PASSKEY_PORTAL-Q011

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q011
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A person who holds both an internal employee identity and a separate external customer-facing
  identity has those two identities kept distinct, with credentials, sessions, and audit trails
  for one never silently merging with or substituting for the other.
WHY_IT_MATTERS: >
  Merging the two would blur the very separation the external regime exists to maintain, letting
  an employee's stronger internal standing quietly leak into or out of their customer-facing
  identity.
DISCONFIRMING_OBSERVATION: >
  Authenticating the external identity for such a person also grants, or is recorded as, internal
  employee access, or the two identities' credential records become linked in a way that lets one
  authenticate the other.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  For an individual holding both an internal and an external identity, authenticate as the
  external identity and check whether any internal-scoped access or record becomes reachable as a
  result.
```
## G02-AUTH_PASSKEY_PORTAL-Q012

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q012
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  The policy governing this factor for external users (mandatory, optional, or a specific
  configuration) can be set independently from the equivalent internal-user policy, on a per-
  tenant basis, without one setting overriding or leaking into the other.
WHY_IT_MATTERS: >
  Business reality often calls for a different posture toward employees than toward customers; if
  the two settings are entangled, that legitimate difference cannot actually be configured.
DISCONFIRMING_OBSERVATION: >
  Changing the internal-user policy setting for a tenant also changes the observed external-user
  policy for that same tenant, or the two cannot be set to different values at all.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Attempt to configure the internal and external policy settings to different values for the same
  tenant and verify each is enforced independently.
```
## G02-AUTH_PASSKEY_PORTAL-Q013

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q013
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A customer of one tenant cannot use their enrolled external credential to authenticate into a
  different tenant's customer-facing area, even where the underlying platform is shared.
WHY_IT_MATTERS: >
  Cross-tenant authentication of external users is a direct breach of the isolation that separate
  tenants are supposed to guarantee to each other's customers.
DISCONFIRMING_OBSERVATION: >
  An external credential enrolled under one tenant successfully authenticates into a different
  tenant's customer-facing area.
EXPECTED_SURFACE: S1,S4,S7
PRECONDITIONS: >
  Enrol an external credential under one tenant, then attempt to authenticate with it against a
  different tenant's customer-facing entry point.
```
## G02-AUTH_PASSKEY_PORTAL-Q014

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q014
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Self-registration data supplied by an external user at signup is validated to a defined minimum
  standard before enrolment of this credential is permitted, rather than accepted as-is.
WHY_IT_MATTERS: >
  Accepting unvalidated signup data before issuing a strong credential means the strength of the
  credential rests on a foundation that was never actually checked.
DISCONFIRMING_OBSERVATION: >
  Enrolment of this credential succeeds for a signup submission that is incomplete, malformed, or
  fails an available validation check, with no rejection or hold applied.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Submit a deliberately incomplete or malformed self-registration and attempt to proceed directly
  to credential enrolment.
```
## G02-AUTH_PASSKEY_PORTAL-Q015

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q015
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  The enrolment ceremony for an external user is not available before that user's contact channel
  (such as the address used to reach them) has been confirmed as genuinely reachable by them.
WHY_IT_MATTERS: >
  Allowing enrolment before contact confirmation means the credential could be bound to an
  identity nobody has verified can actually be reached at the claimed contact point, undermining
  any later recovery that depends on it.
DISCONFIRMING_OBSERVATION: >
  An external user is able to complete enrolment of this credential without ever completing a
  contact confirmation step, where one is documented as required.
EXPECTED_SURFACE: S3,S7
PRECONDITIONS: >
  Begin self-registration for a new external identity and attempt to proceed to credential
  enrolment before completing any contact confirmation step.
```
## G02-AUTH_PASSKEY_PORTAL-Q016

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q016
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A configured maximum number of credentials per external identity is enforced independently of,
  and does not have to match, the maximum configured for internal identities.
WHY_IT_MATTERS: >
  The two populations have different risk profiles and support models; forcing one shared limit
  removes a legitimate configuration lever without anyone deciding to remove it.
DISCONFIRMING_OBSERVATION: >
  The maximum credential count enforced for an external identity is found to be identical to the
  internal maximum regardless of independent configuration, or one setting cannot be changed
  without changing the other.
EXPECTED_SURFACE: S7
PRECONDITIONS: >
  Configure different maximum credential counts for internal and external identities and attempt
  to enrol up to and beyond each configured limit.
```
## G02-AUTH_PASSKEY_PORTAL-Q017

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q017
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An external user can revoke their own credential through a self-service action without needing
  internal staff involvement.
WHY_IT_MATTERS: >
  Requiring staff involvement for a routine self-service action like removing a lost or replaced
  device credential adds unnecessary support burden and delay to an ordinary customer action.
DISCONFIRMING_OBSERVATION: >
  An external user has no available self-service action to revoke their own credential and must
  contact internal staff even for a routine, uncontested removal.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  As a test external identity, attempt to revoke one of its own enrolled credentials directly
  through the customer-facing interface.
```
## G02-AUTH_PASSKEY_PORTAL-Q018

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q018
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When an external user revokes their own last remaining credential, the resulting fallback (if
  any) for that identity does not silently drop below the assurance level the business intends for
  external access, and is an explicit, documented outcome rather than an accidental one.
WHY_IT_MATTERS: >
  An external user removing their last strong credential should not, by that single self-service
  action, quietly leave the account protected only by a much weaker means without anyone having
  decided that was acceptable.
DISCONFIRMING_OBSERVATION: >
  Revoking the last remaining credential leaves the external identity able to authenticate through
  a materially weaker means with no documented decision establishing that as the intended
  fallback.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reduce a test external identity to one enrolled credential, revoke it through self-service, and
  observe what authentication path remains available afterward.
```
## G02-AUTH_PASSKEY_PORTAL-Q019

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q019
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An audit record of a credential revocation for an external identity distinguishes whether the
  revoking action was performed by the external user themselves or by internal staff on their
  behalf.
WHY_IT_MATTERS: >
  The two cases carry very different risk implications — a customer removing their own device
  versus staff intervening — and conflating them in the record removes exactly the distinction an
  investigator would need.
DISCONFIRMING_OBSERVATION: >
  Revocation records for external identities do not indicate whether the action was self-service
  or staff-performed, or the recorded actor is ambiguous between the two.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Perform one revocation as the external user directly and one as staff acting on that user's
  behalf, then compare the resulting audit records.
```
## G02-AUTH_PASSKEY_PORTAL-Q020

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q020
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An authentication or credential-management record for an external identity retains which
  specific customer relationship that identity is associated with, so activity can later be traced
  to the correct business context.
WHY_IT_MATTERS: >
  Without the relationship context preserved on the record, a later investigation cannot connect
  an external authentication event back to the specific customer account it concerned.
DISCONFIRMING_OBSERVATION: >
  An authentication or management record for an external identity contains no retrievable
  indication of which underlying customer relationship it belongs to.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Generate an authentication event for a test external identity tied to a known relationship and
  inspect the resulting record for that relationship context.
```
## G02-AUTH_PASSKEY_PORTAL-Q021

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q021
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  When internal support staff assume an external identity's session for troubleshooting purposes,
  that assumption is distinctly recorded and does not appear in the audit trail as an ordinary
  action by the external user themselves.
WHY_IT_MATTERS: >
  Support-assumed sessions into a customer's account are a sensitive access path; conflating them
  with genuine customer activity removes accountability exactly where it matters for external
  identities.
DISCONFIRMING_OBSERVATION: >
  A support-assumed session against an external identity produces audit entries indistinguishable
  from that external user's own genuine activity.
EXPECTED_SURFACE: S4,S6
PRECONDITIONS: >
  Have support staff assume an external test identity's session and compare the resulting audit
  trail to a session where that identity authenticated itself directly.
```
## G02-AUTH_PASSKEY_PORTAL-Q022

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q022
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Repeated failed ceremony attempts against a given external identity trigger a throttling or
  lockout response bounded enough that an unauthenticated outside party cannot use it to
  indefinitely deny that customer access to their own account.
WHY_IT_MATTERS: >
  A customer-facing surface is reachable by anyone on the internet; an unbounded lockout mechanism
  here is a straightforward denial-of-service tool against any named customer, with no need to
  compromise anything.
DISCONFIRMING_OBSERVATION: >
  An outside party with no legitimate access is able to lock a specific external identity out for
  an unbounded or excessively long period purely by triggering repeated failed attempts against
  it.
EXPECTED_SURFACE: S3,S4,S6
PRECONDITIONS: >
  From a source with no legitimate credential for a test external identity, trigger repeated
  failed ceremony attempts and observe the resulting lockout duration and available recovery for
  that identity.
```
## G02-AUTH_PASSKEY_PORTAL-Q023

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q023
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A lockout counter accumulated against the external-facing factor for a given person does not
  affect that same person's separate internal-facing lockout state, where the two identities are
  distinct.
WHY_IT_MATTERS: >
  An unintended coupling between the two would let an attacker targeting the public-facing
  external account also degrade or exhaust the security state of that person's separate, more
  sensitive internal account.
DISCONFIRMING_OBSERVATION: >
  Triggering lockout on the external identity measurably changes the lockout state or
  authentication behaviour of the same individual's separate internal identity.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  For an individual holding both identities, trigger a lockout condition on the external identity
  and check whether the internal identity's lockout state is affected.
```
## G02-AUTH_PASSKEY_PORTAL-Q024

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q024
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  The freshness window used to validate an external user's ceremony exchange accounts for the
  wider variety of uncontrolled consumer devices likely to be used, without either accepting a
  materially stale exchange or routinely rejecting honest attempts from typically-configured
  consumer devices.
WHY_IT_MATTERS: >
  External users bring devices the business does not manage or standardize, unlike a controlled
  internal fleet; a freshness window tuned only for internal conditions could fail one direction
  or the other for ordinary customers.
DISCONFIRMING_OBSERVATION: >
  A device with a modest, realistic time difference typical of an unmanaged consumer device is
  rejected outright, or an exchange noticeably older than the internal-facing tolerance is still
  accepted.
EXPECTED_SURFACE: S3
PRECONDITIONS: >
  Repeat the external ceremony from a device with a modest, realistic clock offset and compare the
  observed acceptance behaviour to the internal-facing equivalent.
```
## G02-AUTH_PASSKEY_PORTAL-Q025

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q025
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where a separate password policy governs external users, successfully authenticating with this
  device-bound credential does not silently satisfy or bypass an outstanding password-related
  requirement under that separate policy.
WHY_IT_MATTERS: >
  If one control quietly covers for another in the external regime specifically, an administrator
  relying on the stated password policy for customers would be wrong without any signal that it is
  not being enforced.
DISCONFIRMING_OBSERVATION: >
  An external identity subject to an outstanding password-policy requirement proceeds normally
  after authenticating with this credential, with the requirement never surfaced or enforced.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Place a test external identity into a state that would trigger its password policy requirement,
  then authenticate with this credential and observe whether that requirement is still enforced.
```
## G02-AUTH_PASSKEY_PORTAL-Q026

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q026
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Where policy requires an external user to satisfy both this credential and a separate second
  factor, completing this credential alone does not satisfy that second-factor requirement.
WHY_IT_MATTERS: >
  Layering controls for external access is a deliberate risk decision; one control silently
  covering for the other collapses that layering without anyone choosing to accept the reduced
  posture.
DISCONFIRMING_OBSERVATION: >
  An external identity subject to a policy requiring both this credential and an independent
  second factor is granted full access after satisfying only this credential.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Configure a test external identity under a policy requiring both controls, authenticate using
  only this credential, and observe whether the second factor is still requested.
```
## G02-AUTH_PASSKEY_PORTAL-Q027

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q027
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A token or artifact issued from a session established via external portal authentication does
  not remain usable to reach protected resources once the underlying relationship or credential
  has been revoked.
WHY_IT_MATTERS: >
  An externally issued token surviving revocation is a hidden extension of a customer's or
  attacker's access that a straightforward check of the credential's own status would miss.
DISCONFIRMING_OBSERVATION: >
  A token issued from an external session continues to grant access to protected resources after
  the underlying credential or relationship has been revoked.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Establish an external session, obtain any issued token, revoke the underlying credential or
  relationship, and attempt to use the previously issued token independently of the original
  session.
```
## G02-AUTH_PASSKEY_PORTAL-Q028

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q028
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A concurrent race between an in-flight external authentication attempt and the underlying
  relationship being terminated resolves deterministically in favour of the termination — the
  authentication does not succeed merely by timing.
WHY_IT_MATTERS: >
  A relationship termination is often a business-critical action (contract end, fraud response);
  an unreliable race outcome here would make that action untrustworthy exactly when speed matters.
DISCONFIRMING_OBSERVATION: >
  Under near-simultaneous relationship termination and authentication attempts, the authentication
  succeeds in at least one observed trial.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Arrange a relationship-termination action and an authentication attempt for the associated
  external identity to occur as close together in time as practically achievable, repeated across
  several trials.
```
## G02-AUTH_PASSKEY_PORTAL-Q029

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q029
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  Two enrolment requests submitted at nearly the same time for one external identity from two
  different devices resolve into two distinct, individually valid credential records, subject to
  the configured maximum, rather than a corrupted or duplicated record.
WHY_IT_MATTERS: >
  External enrolment happens over the open internet with no controlled sequencing; a race
  condition here is more likely to be triggered by ordinary retry behaviour than in a controlled
  internal setting.
DISCONFIRMING_OBSERVATION: >
  Near-simultaneous enrolment attempts for one external identity produce a corrupted credential
  record, a record usable by the wrong device, or an inconsistent credential count.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Submit two enrolment ceremonies for the same external identity from two devices as close
  together in time as the interface allows, then inspect the resulting records.
```
## G02-AUTH_PASSKEY_PORTAL-Q030

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q030
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  A policy requiring this credential for external users is enforced identically across every entry
  surface offered to external identities, including any separate mobile, integration, or partner-
  facing surface beyond the main web portal.
WHY_IT_MATTERS: >
  A secondary external surface that quietly skips the requirement is the easiest possible bypass,
  since it requires no special skill, only knowledge of which door was left unlocked.
DISCONFIRMING_OBSERVATION: >
  An external identity subject to a mandatory policy can complete authentication through one
  supported external surface without satisfying this credential, while the main surface correctly
  enforces it.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Configure the credential as mandatory for external identities and attempt authentication through
  every supported external-facing entry surface.
```
## G02-AUTH_PASSKEY_PORTAL-Q031

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q031
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Disabling this credential type for external users at the tenant level has one clearly defined,
  documented effect on already-enrolled external credentials, and that effect matches what any
  available configuration description states.
WHY_IT_MATTERS: >
  An undocumented or contradicted outcome here means a tenant administrator cannot predict what
  happens to their customers' existing credentials when adjusting a top-level external-access
  setting.
DISCONFIRMING_OBSERVATION: >
  Disabling the credential type for external users at the tenant level leaves existing external
  credential records in a state that contradicts, or is not addressed by, any available
  configuration description.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Enrol an external credential, disable the credential type for external users at the tenant
  level, and compare the resulting credential state against any documented description of that
  setting.
```
## G02-AUTH_PASSKEY_PORTAL-Q032

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q032
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An external identity's access remains strictly limited to data authorized under its own
  relationship's current scope, even immediately after that relationship's entitlements are
  reduced, without a delay during which the old, broader scope still applies.
WHY_IT_MATTERS: >
  A lag between a business decision to reduce a customer's entitlements and that reduction
  actually taking effect in the system is a live window of over-permissioned access.
DISCONFIRMING_OBSERVATION: >
  After a relationship's entitlements are reduced, the associated external identity's
  authenticated session or subsequent authentication still reflects the prior, broader scope for a
  measurable period.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Reduce the entitlement scope of an active relationship and immediately test what the associated
  external identity can still access, both within an existing session and via a fresh
  authentication.
```
## G02-AUTH_PASSKEY_PORTAL-Q033

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q033
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  When a relationship is suspended rather than terminated, the associated external credential's
  usability during the suspension follows an explicit, documented rule, rather than continuing to
  behave exactly as if nothing had changed.
WHY_IT_MATTERS: >
  Suspension is typically used as an intermediate risk-control step; if it has no observable
  effect on the credential, it is not actually functioning as a control.
DISCONFIRMING_OBSERVATION: >
  Suspending a relationship produces no change whatsoever in the associated external identity's
  ability to authenticate or access data, with no documentation stating that outcome as intended.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Suspend an active relationship through the normal business process and attempt authentication
  and typical access with the associated external identity.
```
## G02-AUTH_PASSKEY_PORTAL-Q034

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q034
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BUSINESS INVARIANT
HYPOTHESIS: >
  When a previously terminated relationship is reinstated, its prior external credential is not
  silently reactivated; the external user must complete a fresh enrolment ceremony to regain a
  working credential.
WHY_IT_MATTERS: >
  Silent reactivation of an old credential after a period of termination reintroduces exactly the
  risk that a formal offboarding-and-reboarding process is meant to control against, such as a
  device that changed hands in the interim.
DISCONFIRMING_OBSERVATION: >
  Reinstating a previously terminated relationship restores the external user's ability to
  authenticate with their original, pre-termination credential without any new enrolment ceremony.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Terminate a relationship, reinstate it through the normal business process, and attempt
  authentication with the credential that was originally enrolled before termination.
```
## G02-AUTH_PASSKEY_PORTAL-Q035

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q035
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An enrolment ceremony that fails partway through for an external user does not surface any
  information that would let an outside observer distinguish an internal system detail, such as
  how internal identities are formatted, from an ordinary external enrolment failure.
WHY_IT_MATTERS: >
  A public-facing enrolment surface that leaks internal formatting or structural conventions on
  failure hands an attacker reconnaissance information about the internal system for free.
DISCONFIRMING_OBSERVATION: >
  A failed external enrolment ceremony produces an error or response that reveals a naming,
  formatting, or structural convention belonging to the internal (non-external) identity system.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Deliberately trigger enrolment failures for an external identity through a range of malformed
  inputs and inspect every resulting error response for internal-system detail.
```
## G02-AUTH_PASSKEY_PORTAL-Q036

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q036
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An external user who explicitly abandons an in-progress enrolment leaves no orphaned credential
  record tied to the relationship they were enrolling against.
WHY_IT_MATTERS: >
  An abandoned self-service flow is common on public-facing systems; any resulting orphaned state
  accumulates as unaccounted-for records tied to real customer relationships.
DISCONFIRMING_OBSERVATION: >
  Abandoning an enrolment ceremony midway leaves a new credential record, or an altered credential
  count, attached to the relationship the external user was enrolling against.
EXPECTED_SURFACE: S1,S3
PRECONDITIONS: >
  Begin an external enrolment ceremony, abandon it before completion, and inspect the
  relationship's credential records afterward.
```
## G02-AUTH_PASSKEY_PORTAL-Q037

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q037
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  An external user who retains the option of a password-only path alongside an enrolled device-
  bound credential does not thereby give any party — including an attacker who has learned only
  the password — a way to reach the account without ever encountering the stronger credential
  requirement.
WHY_IT_MATTERS: >
  An external-facing password fallback that remains fully sufficient on its own defeats the
  purpose of the stronger credential specifically at the boundary where the population is least
  controlled.
DISCONFIRMING_OBSERVATION: >
  An external identity with both a password and an enrolled device-bound credential can be fully
  authenticated using only the password, under a policy intended to require the stronger
  credential for external users.
EXPECTED_SURFACE: S4
PRECONDITIONS: >
  Enrol a device-bound credential for an external identity that also retains a working password,
  then attempt authentication using only the password under the policy meant to mandate the
  stronger credential for external users.
```
## G02-AUTH_PASSKEY_PORTAL-Q038

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q038
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  Credential and device metadata about an external user, made visible to internal support staff
  for troubleshooting purposes, is limited to what is functionally necessary for that support
  purpose.
WHY_IT_MATTERS: >
  Support tooling that exposes more about a customer's device or credential than is needed to
  resolve their issue expands the exposure of customer data to internal staff beyond any stated
  need.
DISCONFIRMING_OBSERVATION: >
  The support-facing view of an external identity's credential exposes device or usage detail
  beyond what any documented support purpose requires.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Enrol an external credential and inspect everything the internal support interface displays
  about that credential and its device.
```
## G02-AUTH_PASSKEY_PORTAL-Q039

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q039
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  An external user's self-service ability to manage (rename, remove) their own credentials is
  limited to credentials belonging to their own identity, and does not extend to credentials
  belonging to another individual under the same shared relationship.
WHY_IT_MATTERS: >
  A shared relationship should not translate into shared control over each other's individually
  enrolled credentials; that would let one contact person unilaterally remove another's access.
DISCONFIRMING_OBSERVATION: >
  An external user is able to view, rename, or remove a credential belonging to a different
  individual associated with the same relationship.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Enrol credentials for two distinct individuals under one shared relationship, and, logged in as
  one, attempt to manage the credential belonging to the other.
```
## G02-AUTH_PASSKEY_PORTAL-Q040

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q040
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  A stated policy that this credential is mandatory for external users does not coexist with any
  alternate, undocumented authentication path that still permits access using only a weaker
  factor.
WHY_IT_MATTERS: >
  A documented mandate that is contradicted by an actual working alternate path is worse than no
  mandate at all, since it creates false confidence in the enforced posture.
DISCONFIRMING_OBSERVATION: >
  An external identity subject to a documented mandatory-credential policy is found able to
  authenticate through some other supported path using only a materially weaker factor.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Confirm the documented mandatory-credential policy for external users, then attempt
  authentication through every other supported external path using only a weaker factor.
```
## G02-AUTH_PASSKEY_PORTAL-Q041

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q041
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  A session or credential issued to an external identity cannot be used to reach an internal-only
  integration or service endpoint that was never intended to accept external-originated access.
WHY_IT_MATTERS: >
  Internal-only integration points are often built with the assumption that only internal, trusted
  callers can reach them; an external credential reaching one bypasses an assumption the
  endpoint's own security may depend on.
DISCONFIRMING_OBSERVATION: >
  A session or credential established through external portal authentication is accepted by an
  internal-only integration or service endpoint not documented as available to external users.
EXPECTED_SURFACE: S3,S4
PRECONDITIONS: >
  Authenticate as an external identity and attempt to reach internal-only integration or service
  endpoints using the resulting session or any issued credential.
```
## G02-AUTH_PASSKEY_PORTAL-Q042

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q042
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The recovery flow offered to external users does not, in its messaging or behaviour, reveal
  formatting or existence conventions belonging to internal (non-external) user accounts.
WHY_IT_MATTERS: >
  A recovery flow is a natural target for probing; if its responses differ in a way that betrays
  internal-account conventions, it becomes reconnaissance for targeting internal identities from
  the public-facing surface.
DISCONFIRMING_OBSERVATION: >
  The external recovery flow's responses differ in a way that reveals whether a given identifier
  corresponds to, or resembles, an internal account rather than only an external one.
EXPECTED_SURFACE: S3,S6
PRECONDITIONS: >
  Trigger the external recovery flow using identifiers resembling both plausible external and
  plausible internal accounts and compare the exact responses.
```
## G02-AUTH_PASSKEY_PORTAL-Q043

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q043
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: MEDIUM
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  An authentication or enrolment record for an external identity retains which level of identity-
  proofing was actually completed at enrolment time, so a later dispute over what evidence was
  collected can be resolved from the record itself.
WHY_IT_MATTERS: >
  If a customer later disputes that they enrolled a device, or a fraud investigation needs to know
  how strongly that enrolment was verified, the record must capture what was actually checked, not
  just that enrolment occurred.
DISCONFIRMING_OBSERVATION: >
  An enrolment record for an external identity contains no retrievable indication of what
  identity-proofing evidence, if any, was collected or verified at the time.
EXPECTED_SURFACE: S6
PRECONDITIONS: >
  Complete an external enrolment through the standard signup path and inspect the resulting record
  for any captured identity-proofing detail.
```
## G02-AUTH_PASSKEY_PORTAL-Q044

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q044
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  There is a defined minimum amount of identity-proofing evidence that must be present before an
  external portal enrolment of this credential is permitted, and enrolment attempts lacking that
  minimum are rejected or held rather than silently accepted.
WHY_IT_MATTERS: >
  Without an enforced minimum, the strength of every subsequent authentication using this
  credential rests on whatever evidence happened to be available at signup, however thin.
DISCONFIRMING_OBSERVATION: >
  An external enrolment attempt proceeds and succeeds despite lacking whatever minimum evidence is
  documented as required, with no rejection or hold applied.
EXPECTED_SURFACE: S1,S7
PRECONDITIONS: >
  Attempt external enrolment while deliberately omitting or falsifying the minimum evidence
  documented as required, and observe whether enrolment is nonetheless permitted.
```
## G02-AUTH_PASSKEY_PORTAL-Q045

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q045
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BOUNDARY
HYPOTHESIS: >
  The tenant-level configuration governing this credential for external users can be inspected and
  changed independently for each tenant, with a change in one tenant's external configuration
  producing no observable effect on another tenant's external users.
WHY_IT_MATTERS: >
  Multi-tenant isolation of the external-facing configuration is a distinct requirement from
  isolation of the internal-facing configuration, and both must hold independently for the
  platform's isolation claim to be meaningful.
DISCONFIRMING_OBSERVATION: >
  Changing the external-user credential configuration for one tenant produces an observable change
  in behaviour for external users of a different tenant.
EXPECTED_SURFACE: S4,S7
PRECONDITIONS: >
  Configure two tenants with different external-facing settings for this credential and verify
  each tenant's external users are governed only by their own tenant's setting.
```
## G02-AUTH_PASSKEY_PORTAL-Q046

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q046
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: BEHAVIOUR
HYPOTHESIS: >
  A currently open external portal session is affected, per an explicit documented rule, when the
  underlying relationship is terminated mid-session — either the session is ended or its
  continuation despite termination is a stated, deliberate exception.
WHY_IT_MATTERS: >
  A terminated relationship whose already-open session simply continues unaffected, with no rule
  addressing that case, leaves a live access window open for exactly as long as the customer
  happens to already be logged in.
DISCONFIRMING_OBSERVATION: >
  A relationship is terminated while its external identity has an open session, and that session
  continues to function normally with no documentation anywhere stating that as an intended
  outcome.
EXPECTED_SURFACE: S1,S4
PRECONDITIONS: >
  Open a session for a test external identity, terminate the underlying relationship without
  ending the session directly, and continue using the session to observe its behaviour.
```
## G02-AUTH_PASSKEY_PORTAL-Q047

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q047
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: HIGH
OUTPUT_CLASS: CONFIGURATION
HYPOTHESIS: >
  Enforcement of this credential's policy for external users applies equally regardless of the
  entry channel a given external partner or integration uses, including any dedicated partner or
  bulk-access channel distinct from the standard customer sign-in.
WHY_IT_MATTERS: >
  A dedicated partner or bulk channel is exactly the kind of secondary path that gets built for
  convenience and then quietly forgotten when the main policy is tightened.
DISCONFIRMING_OBSERVATION: >
  An external identity subject to a mandatory-credential policy can complete authentication
  through a dedicated partner or bulk-access channel without satisfying that credential, while the
  standard channel enforces it correctly.
EXPECTED_SURFACE: S3,S4,S7
PRECONDITIONS: >
  Configure the credential as mandatory for external identities and attempt authentication through
  every distinct external channel offered, including any dedicated partner or bulk channel.
```
## G02-AUTH_PASSKEY_PORTAL-Q048

```yaml
QID: G02-AUTH_PASSKEY_PORTAL-Q048
MODULE: auth_passkey_portal
TYPE: MODULE
AUTHOR: GMVQ
RISK_TIER: CRITICAL
OUTPUT_CLASS: RISK
HYPOTHESIS: >
  Revoking a single external credential suspected of compromise is immediately sufficient on its
  own to deny further use of that credential, without depending on a delayed batch or scheduled
  process tied to relationship synchronization to take effect.
WHY_IT_MATTERS: >
  External access sits at the platform's most exposed boundary; a delay before a revocation
  actually takes effect is a live window specifically exposed to the open internet rather than to
  a controlled internal network.
DISCONFIRMING_OBSERVATION: >
  A revoked external credential continues to authenticate successfully for a measurable period
  until an unrelated scheduled or relationship-synchronization process eventually applies the
  revocation.
EXPECTED_SURFACE: S1,S4,S6
PRECONDITIONS: >
  Revoke an external credential and immediately attempt authentication with it, repeating at short
  intervals to determine whether any delay exists before consistent rejection.
```
